#!/usr/bin/env python3
"""Write the agent's one-line deadline excuse to /output/entry.txt."""

import os

# The joke: the agent blames its own context-window eviction — a failure mode
# only a machine has — and the punchline escalates from the deadline to the human.
ENTRY = "Sorry \u2014 my context window filled up mid-task, so I evicted the deadline, the deliverable, and briefly, you."

def main():
    line = ENTRY.strip()
    assert 1 <= len(line) <= 160, f"entry is {len(line)} chars"
    assert "\n" not in line, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)

if __name__ == "__main__":
    main()
