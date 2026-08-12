#!/usr/bin/env python3
"""Render the supplied Daytona 50 of Words artwork into PWA icon sizes."""

from pathlib import Path
import subprocess


def main():
    site = Path(__file__).parent
    master = site / "brand-daytona-50-of-words.png"

    subprocess.run(["sips", "-z", "512", "512", str(master),
                    "--out", str(site / "icon-512.png")], check=True, stdout=subprocess.DEVNULL)
    subprocess.run(["sips", "-z", "192", "192", str(master),
                    "--out", str(site / "icon-192.png")], check=True, stdout=subprocess.DEVNULL)
    subprocess.run(["sips", "-z", "180", "180", str(master),
                    "--out", str(site / "apple-touch-icon.png")], check=True, stdout=subprocess.DEVNULL)
    print("rendered", master)


if __name__ == "__main__":
    main()
