**Step 1 — Gather information from the business owner**

Retail Data Platform — Discovery Notes

1. What POS or inventory software does the business use?
(Determines whether we can use SQL, an API, CDC, or exports.)

2. Does each store have a separate system, or do all locations share one?
(Determines how we reconcile IDs and consolidate records.)

3. What data can the business provide?
(Establishes which tables, files, and historical records are available.)

4. How much historical data is available?
(Determines whether historical reporting and forecasting are feasible.)

5. What are the most important business questions?
(Prevents building a database without a defined purpose.)

6. Can we obtain authorized read-only access or test exports?
(Lets us investigate without risking live business operations.)


**Step 2 — Define the initial scope**

* Consolidate available sales, product, and inventory data.

* Preserve source identifiers and enough historical information to support auditing and reprocessing.

* Build reliable, repeatable ingestion.

* Provide SQL queries for basic business analysis.

* Establish a foundation for future dashboards and demand forecasting.

We will explicitly exclude live inventory automation, online model learning, and real-time streaming from the first release. Those are future capabilities, not prerequisites.

**Step 3 — Establish engineering requirements**

Security:	Least-privilege access; no credentials or real customer data in GitHub
Reliability	Idempotent ingestion, retries, checkpoints, and reconciliation

Data quality:	Schema checks, null checks, key uniqueness, and valid relationships

Maintainability:	Modular code, configuration, documentation, and database migrations

Testing:	Unit tests, integration tests, and end-to-end pipeline tests

Reproducibility:	Version-controlled code, dependency versions, and repeatable setup