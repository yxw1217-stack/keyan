"""RDKit-based molecular descriptor and similarity analysis.

Populate the CIL database before running this module.
"""

from pathlib import Path


def main() -> None:
    database = Path(__file__).parents[1] / "02_CIL_Database" / "CIL_database.csv"
    print(f"RDKit analysis entry point: {database}")


if __name__ == "__main__":
    main()
