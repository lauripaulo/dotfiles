#!/usr/bin/env python3
"""Install Homebrew packages listed in brews-installed-list.txt."""

import subprocess
import sys
from pathlib import Path


def main() -> int:
    list_path = Path(__file__).parent / "brews-installed-list.txt"

    if not list_path.exists():
        print(f"Error: {list_path} not found.", file=sys.stderr)
        return 1

    packages = []
    with list_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.split("#", 1)[0].strip()
            if line:
                packages.append(line)

    if not packages:
        print("No packages to install.")
        return 0

    print(f"Installing {len(packages)} package(s) from {list_path}...")
    for package in packages:
        print(f"\n>>> brew install {package}")
        result = subprocess.run(
            ["brew", "install", package],
            check=False,
        )
        if result.returncode != 0:
            print(
                f"Warning: failed to install {package} (exit {result.returncode}).",
                file=sys.stderr,
            )

    print("\nDone.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
