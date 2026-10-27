"""Portfolio reporting example written now; not a historical work artifact."""
import csv
from pathlib import Path

def main():
    path = Path(__file__).with_name("verified_metrics.csv")
    with path.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            before, after = float(row["before"]), float(row["after"])
            if before <= 0 or after < 0:
                raise ValueError("Times must be valid nonnegative measurements.")
            print(f"{row['metric']}: {before:g} -> {after:g} {row['unit']}; "
                  f"reduction {before-after:g} {row['unit']} "
                  f"({(before-after)/before:.0%}); source {row['evidence']}")
    print("Reported figures are self-reported; measurement scope is unverified.")

if __name__ == "__main__":
    main()
