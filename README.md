# demo_dab_cicd 2

#### Check local CLI is configured properly
```
databricks api get /api/2.0/preview/scim/v2/Me --profile dev
```

#### Starting a new project
```
cd databricks_pipelines
databricks bundle init --profile dev
```

#### Starting a new project
```
cd <<new_folder>>
databricks bundle validate --target dev --profile dev
databricks bundle deploy --target dev --profile dev
databricks bundle run --target dev --profile dev 
databricks bundle destroy --target dev --profile dev
```