# jobs.py
from dagster import job, op
from .hooks import email_on_success, email_on_failure

@op
def say_hello():
    return "Hello every 5 minutes!"

@job(hooks={email_on_success, email_on_failure})
def every_five_minutes_job():
    say_hello()