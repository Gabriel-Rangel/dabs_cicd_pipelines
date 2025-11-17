from databricks.bundles.jobs import Job

"""
A sample job for project_02.
"""

sample_job = Job.from_dict(
    {
        "name": "project_02_job",
        "trigger": {
            # Run this job every day, exactly one day from the last run; see https://docs.databricks.com/api/workspace/jobs/create#trigger
            "periodic": {
                "interval": 1,
                "unit": "DAYS",
            },
        },
        # "email_notifications": {
        #     "on_failure": [
        #         "gabriel.rangel@databricks.com",
        #     ],
        # },
        "parameters": [
            {
                "name": "schema",
                "default": "${var.schema}",
            },
        ],
        "tasks": [
            {
                "task_key": "notebook_task",
                "notebook_task": {
                    "notebook_path": "src/sample_notebook.py",
                },
            },
        ],
        "environments": [
            {
                "environment_key": "default",
                "spec": {
                    "environment_version": "2",
                },
            },
        ],
    }
)
