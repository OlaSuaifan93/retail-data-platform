"""Command-line entry point for profiling a sales CSV."""

import json
import sys

from retail_data.profiling import profile_csv


def main() -> None:
    if len(sys.argv) != 2:
        print(
            "Usage: python scripts/profile_sales.py <path-to-csv>",
            file=sys.stderr,
        )
        raise SystemExit(2)

    report = profile_csv(sys.argv[1])
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
