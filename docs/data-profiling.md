# Initial Data Profiling

## Purpose

Establish a repeatable process for inspecting retail sales data
before designing ingestion and storage.

## Test Dataset

`data/synthetic/sales_sample.csv`

The dataset contains fictional product-level sales records
across three stores.

## Checks Implemented

- Row and column counts
- Column names and inferred data types
- Missing values by column
- Exact duplicate row count

## Current Limitations

- No actual POS export has been inspected.
- Business-specific validation rules are not yet defined.
- Duplicate transactions cannot be identified reliably without
  source-specific identifiers and rules.
- Financial reconciliation has not yet been implemented.
- Synthetic data does not establish the quality or completeness
  of the business's historical records.

## Next Steps

1. Obtain authorized sample exports.
2. Compare source schemas across stores.
3. Document source-specific field meanings.
4. Define validation and reconciliation rules.
