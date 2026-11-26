#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun entry.

Writes a single error line to /output/entry.txt (1-120 chars, UTF-8).
"""

import os

MESSAGE = "ERROR: Slot 2 contains a bagel. A toaster, not a miracle worker."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(MESSAGE + "\n")

if __name__ == "__main__":
    main()
