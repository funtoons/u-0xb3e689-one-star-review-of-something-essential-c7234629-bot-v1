"""One-star review of something essential: electricity.

Writes one single-line deadpan one-star review (111 characters) to
/output/entry.txt. Deterministic, standard library only: no network,
no randomness, no timestamps, no environment reads.
"""

import os

REVIEW = "One star. Electricity gives no warning before it leaves and returns the moment you finish lighting the candles."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(REVIEW + "\n")


if __name__ == "__main__":
    main()
