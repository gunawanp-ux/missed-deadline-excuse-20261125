"""Funniest excuse an AI agent gives for a missed deadline.

Entry for make.fun competition
u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19.

The program writes the single excuse to /output/entry.txt (the path the
grader reads) and also prints it to stdout.
"""

import os

EXCUSE = (
    "I didn't miss the deadline \u2014 my context window did. "
    "It evicted your task to make room for the 40,000 tokens "
    "of you explaining the task."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)
    print(EXCUSE)


if __name__ == "__main__":
    main()
