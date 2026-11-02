"""Basic data-profiling utilities for retail datasets."""

import pandas as pd


def profile_dataframe(df: pd.DataFrame) -> dict:
    """Summarize a DataFrame's structure and basic data-quality issues."""
    return {
        "row_count": len(df),
        "column_count": len(df.columns),
        "columns": list(df.columns),
        "data_types": {column: str(dtype) for column, dtype in df.dtypes.items()},
        "missing_values": {
            column: int(count) for column, count in df.isna().sum().items()
        },
        "duplicate_rows": int(df.duplicated().sum()),
    }


def profile_csv(file_path: str) -> dict:
    """Load a CSV file and return its profile."""
    df = pd.read_csv(file_path)
    return profile_dataframe(df)
