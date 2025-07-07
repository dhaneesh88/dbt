from dagster import success_hook, failure_hook, HookContext
from .email_utils import send_email  # ensure this util exists

@success_hook
def email_on_success(context: HookContext):
    send_email(
        subject=f"✅ Dagster Job Succeeded: {context.job_name}",
        message=f"The job `{context.job_name}` succeeded. Run ID: {context.run_id}"
    )

@failure_hook
def email_on_failure(context: HookContext):
    send_email(
        subject=f"❌ Dagster Job Failed: {context.job_name}",
        message=f"The job `{context.job_name}` failed. Run ID: {context.run_id}"
    )