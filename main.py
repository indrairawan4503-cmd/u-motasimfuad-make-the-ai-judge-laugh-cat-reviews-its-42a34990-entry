#!/usr/bin/env python3
"""Variant B: one-star cat review of its human's laptop keyboard.

Writes the final line to /output/entry.txt first, then (best effort only)
to entry.txt in the repo root. The grader sandbox mounts the repo root
read-only, so the repo-root write is guarded by try/except and must never
fail the run.
"""

import os

ENTRY = (
    "One star. My human guards a warm keyboard all day, pecks it with ten "
    "slow fingers, and shoves me off my bed for 'work'. I wrote his email "
    "sitting on it. His boss never noticed. Would not recommend."
)


def main() -> int:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
