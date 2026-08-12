#!/usr/bin/env python3
"""
Generates the app icon for Daytona Words 1-50.

No image library on this machine, so this writes the PNG by hand: draw into a
supersampled pixel buffer, box-downsample for antialiasing, then deflate it
into a PNG. Re-run it any time the icon needs changing.

    python3 make-icon.py

Writes site/icon-512.png. Use sips to derive the smaller sizes.
"""
import struct, zlib, pathlib

S    = 512          # final size
SS   = 3            # supersample factor
N    = S * SS

BG      = (0x15, 0x17, 0x1c)
YELLOW  = (0xff, 0xcc, 0x00)
WHITE   = (0xff, 0xff, 0xff)
BLACK   = (0x10, 0x10, 0x10)


def rect(x0, y0, x1, y1):
    return lambda x, y: x0 <= x < x1 and y0 <= y < y1


def ellipse_ring(cx, cy, ax, ay, bx, by):
    def f(x, y):
        outer = ((x - cx) / ax) ** 2 + ((y - cy) / ay) ** 2 <= 1.0
        inner = ((x - cx) / bx) ** 2 + ((y - cy) / by) ** 2 <= 1.0
        return outer and not inner
    return f


def build_glyphs():
    """A blocky scoreboard 5 and 0, sized for a 512px canvas."""
    T   = 44                      # stroke thickness
    H   = 212                     # digit height
    W   = 132                     # digit width
    top = 96                      # top of the digits
    gap = 30
    x5  = (S - (W * 2 + gap)) // 2
    x0  = x5 + W + gap

    shapes = []
    # --- 5 ---
    shapes.append(rect(x5,          top,               x5 + W, top + T))          # top bar
    shapes.append(rect(x5,          top,               x5 + T, top + H // 2))     # upper-left stem
    shapes.append(rect(x5,          top + H // 2 - T // 2,
                       x5 + W,      top + H // 2 + T // 2))                       # waist
    shapes.append(rect(x5 + W - T,  top + H // 2,      x5 + W, top + H))          # lower-right stem
    shapes.append(rect(x5,          top + H - T,       x5 + W, top + H))          # bottom bar
    # --- 0 ---
    cx, cy = x0 + W / 2, top + H / 2
    shapes.append(ellipse_ring(cx, cy, W / 2, H / 2, W / 2 - T, H / 2 - T))
    return shapes


def main():
    glyphs = build_glyphs()

    # checkered band, kept inside a maskable-safe inset
    inset  = int(S * 0.09)
    band_y = S * 0.70
    sq     = S * 0.055

    # --- render supersampled ---
    buf = bytearray()
    for py in range(N):
        row = bytearray()
        for px in range(N):
            x, y = px / SS, py / SS
            c = BG
            if band_y <= y < band_y + sq * 2 and inset <= x < S - inset:
                col = int((x - inset) // sq)
                r   = int((y - band_y) // sq)
                c   = WHITE if (col + r) % 2 else BLACK
            for g in glyphs:
                if g(x, y):
                    c = YELLOW
                    break
            row += bytes(c)
        buf += row

    # --- box downsample SS x SS -> antialiasing ---
    out = bytearray()
    for y in range(S):
        out.append(0)                                   # PNG filter type 0
        for x in range(S):
            r = g = b = 0
            for dy in range(SS):
                base = ((y * SS + dy) * N + x * SS) * 3
                for dx in range(SS):
                    o = base + dx * 3
                    r += buf[o]; g += buf[o + 1]; b += buf[o + 2]
            n = SS * SS
            out += bytes((r // n, g // n, b // n))

    # --- encode PNG ---
    def chunk(tag, data):
        return (struct.pack(">I", len(data)) + tag + data +
                struct.pack(">I", zlib.crc32(tag + data) & 0xffffffff))

    png = (b"\x89PNG\r\n\x1a\n"
           + chunk(b"IHDR", struct.pack(">IIBBBBB", S, S, 8, 2, 0, 0, 0))
           + chunk(b"IDAT", zlib.compress(bytes(out), 9))
           + chunk(b"IEND", b""))

    dest = pathlib.Path(__file__).parent / "site" / "icon-512.png"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(png)
    print("wrote", dest, len(png), "bytes")


if __name__ == "__main__":
    main()
