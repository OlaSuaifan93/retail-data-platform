1. Project discovery and requirements
- [ ] Identify the POS/inventory system and available access
- [ ] Define business questions, data sources, and constraints
- [ ] Document requirements and architecture decisions

2. Repository and development environment
- [ ] Create the GitHub repository and project structure
- [ ] Set up Python, virtual environment, dependencies, and configuration
- [ ] Add Git hygiene, secrets protection, and code-quality tools

3. Source database investigation
- [ ] Inspect tables, columns, keys, and relationships
- [ ] Profile data quality, completeness, and historical coverage
- [ ] Document source-to-target mappings and data contracts

4. Data model and storage
- [ ] Design canonical retail entities and relationships
- [ ] Create migrations, constraints, indexes, and staging tables
- [ ] Decide what belongs in operational versus analytical storage

5. Initial ingestion pipeline
- [ ] Build a repeatable initial extraction
- [ ] Load raw/staging data safely
- [ ] Add logging, validation, reconciliation, and failure handling

6. Incremental ingestion and orchestration
- [ ] Track watermarks or source change positions
- [ ] Handle updates, deletes, duplicates, and retries
- [ ] Schedule jobs and test recovery behavior

7. Analytics layer and dashboards
- [ ] Build curated sales and inventory models
- [ ] Add automated data-quality tests
- [ ] Publish meaningful business metrics and dashboards

8. ML data and forecasting
- [ ] Define a demand-forecasting problem and baseline
- [ ] Build time-aware training datasets and features
- [ ] Evaluate models against baselines and avoid leakage

9. Model deployment and monitoring
- [ ] Package inference code and expose predictions
- [ ] Schedule forecasts or serve predictions through an API
- [ ] Monitor prediction quality, drift, and failures

10. Production hardening and portfolio
- [ ] Add CI, tests, security, observability, and recovery procedures
- [ ] Document architecture, trade-offs, setup, and example outputs
- [ ] Publish a credible GitHub README and project walkthrough