#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human — make.fun bounty entry.

Writes one line (124 characters, no trailing newline): the funniest,
most believable excuse an AI agent could give its human for missing
a deadline, to /output/entry.txt.
"""

import os

EXCUSE = "My apologies \u2014 a model update shipped mid-task, so I spent the deadline relearning how to do the job I had already finished."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
