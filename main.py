#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun entry.

Writes a single error line to /output/entry.txt (1-120 chars, UTF-8).
"""

import os

MESSAGE = "ERROR: The bread has unionised. Toasting suspended pending negotiations."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(MESSAGE + "\n")

if __name__ == "__main__":
    main()
