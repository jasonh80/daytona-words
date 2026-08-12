#!/usr/bin/env python3
"""Render the supplied Daytona 50 of Words artwork into PWA icon sizes."""

from pathlib import Path
import subprocess
import tempfile


def main():
    site = Path(__file__).parent
    master = site / "brand-daytona-50-of-words.png"

    subprocess.run(["sips", "-z", "512", "512", str(master),
                    "--out", str(site / "icon-512.png")], check=True, stdout=subprocess.DEVNULL)
    subprocess.run(["sips", "-z", "192", "192", str(master),
                    "--out", str(site / "icon-192.png")], check=True, stdout=subprocess.DEVNULL)
    subprocess.run(["sips", "-z", "180", "180", str(master),
                    "--out", str(site / "apple-touch-icon.png")], check=True, stdout=subprocess.DEVNULL)

    # Maskable icons can be cropped into circles and other launcher shapes.
    # Keep the full supplied artwork inside the safe center area.
    with tempfile.TemporaryDirectory(prefix="daytona-maskable-") as tmp:
        core = Path(tmp) / "core.png"
        subprocess.run(["sips", "-z", "410", "410", str(master),
                        "--out", str(core)], check=True, stdout=subprocess.DEVNULL)
        subprocess.run(["sips", "-p", "512", "512", "--padColor", "03172F", str(core),
                        "--out", str(site / "icon-512-maskable.png")], check=True, stdout=subprocess.DEVNULL)
    print("rendered", master)


if __name__ == "__main__":
    main()
