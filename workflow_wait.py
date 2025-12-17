from prefect import flow, task
import time

@task
def wait_task():
    time.sleep

@flow
def wait_workflow():
    wait_task()
