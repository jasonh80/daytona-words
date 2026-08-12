#!/usr/bin/env python3
"""Render the FCS Daytona Words icon master into the PWA icon sizes.

This project is designed on macOS, so the script uses the system Quick Look
SVG renderer and sips. The actual artwork lives in icon-master.svg.
"""

from pathlib import Path
import shutil
import subprocess
import tempfile


def main():
    site = Path(__file__).parent
    master = site / "icon-master.svg"

    with tempfile.TemporaryDirectory(prefix="daytona-icon-") as tmp:
        subprocess.run(
            ["qlmanage", "-t", "-s", "512", "-o", tmp, str(master)],
            check=True,
            stdout=subprocess.DEVNULL,
        )
        rendered = Path(tmp) / f"{master.name}.png"
        shutil.copyfile(rendered, site / "icon-512.png")

    subprocess.run(["sips", "-z", "192", "192", str(site / "icon-512.png"),
                    "--out", str(site / "icon-192.png")], check=True, stdout=subprocess.DEVNULL)
    subprocess.run(["sips", "-z", "180", "180", str(site / "icon-512.png"),
                    "--out", str(site / "apple-touch-icon.png")], check=True, stdout=subprocess.DEVNULL)
    print("rendered", master)


if __name__ == "__main__":
    main()
