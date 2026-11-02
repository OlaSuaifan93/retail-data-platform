import pandas as pd

from retail_data.profiling import profile_dataframe


def test_profile_dataframe_counts_rows_columns_and_duplicates():
    df = pd.DataFrame(
        {
            "store_id": ["STORE_1", "STORE_1", "STORE_2"],
            "quantity": [2, 2, 1],
        }
    )

    report = profile_dataframe(df)

    assert report["row_count"] == 3
    assert report["column_count"] == 2
    assert report["duplicate_rows"] == 1


def test_profile_dataframe_counts_missing_values():
    df = pd.DataFrame(
        {
            "product_id": ["P101", None],
            "quantity": [2, 1],
        }
    )

    report = profile_dataframe(df)

    assert report["missing_values"]["product_id"] == 1
    assert report["missing_values"]["quantity"] == 0
