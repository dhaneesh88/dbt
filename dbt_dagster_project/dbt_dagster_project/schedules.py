"""
To add a daily schedule that materializes your dbt assets, uncomment the following lines.
"""
from dagster import ScheduleDefinition

from dagster_dbt import build_schedule_from_dbt_selection

from .assets import dbtlearn_dbt_assets

from .jobs import every_five_minutes_job  # import it

schedules = [
    build_schedule_from_dbt_selection(
        [dbtlearn_dbt_assets],
        job_name="materialize_dbt_models",
        cron_schedule="0 0 * * *",
        dbt_select="fqn:*",
    ),
    ScheduleDefinition(
        job=every_five_minutes_job,
        cron_schedule="*/5 * * * *",
        name="every_five_minutes_schedule",
    ),
]