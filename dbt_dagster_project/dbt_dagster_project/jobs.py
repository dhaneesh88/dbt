# jobs.py
# from dagster import job, op
# from .hooks import email_on_success, email_on_failure

from dagster import define_asset_job
from .assets import dbtlearn_dbt_assets
from .hooks import email_on_success, email_on_failure

# @op
# def say_hello():
#     return "Hello every 5 minutes!"

# @job(hooks={email_on_success, email_on_failure})
# def every_five_minutes_job():
#     say_hello()

every_five_minutes_job = define_asset_job(
    name="every_five_minutes_job",
    selection="*",  # materialize all assets
    hooks={email_on_success, email_on_failure}
)