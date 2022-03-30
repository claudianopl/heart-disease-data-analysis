# The ingestion class; we'll need this to read, treat and load our data on another csv file
# On the future, it can load the data on a database
# from airflow import DAG
"""Example DAG demonstrating the usage of the TaskGroup."""
from datetime import datetime

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.utils.task_group import TaskGroup

# [START howto_task_group]
with DAG(
    dag_id="example_task_group", start_date=datetime(2021, 1, 1), catchup=False, tags=["example"]
) as dag:
    start = DummyOperator(task_id="start")

    # [START howto_task_group_section_1]
    with TaskGroup("section_1", tooltip="Tasks for section_1") as section_1:
        task_1 = DummyOperator(task_id="task_1")
        task_2 = BashOperator(task_id="task_2", bash_command='echo 1')
        task_3 = DummyOperator(task_id="task_3")

        task_1 >> [task_2, task_3]
    # [END howto_task_group_section_1]

    # [START howto_task_group_section_2]
    with TaskGroup("section_2", tooltip="Tasks for section_2") as section_2:
        task_1 = DummyOperator(task_id="task_1")

        # [START howto_task_group_inner_section_2]
        with TaskGroup("inner_section_2", tooltip="Tasks for inner_section2") as inner_section_2:
            task_2 = BashOperator(task_id="task_2", bash_command='echo 1')
            task_3 = DummyOperator(task_id="task_3")
            task_4 = DummyOperator(task_id="task_4")

            [task_2, task_3] >> task_4
        # [END howto_task_group_inner_section_2]

    # [END howto_task_group_section_2]

    end = DummyOperator(task_id='end')

    start >> section_1 >> section_2 >> end
# [END howto_task_group]


def main():
  pass

if __name__ == '__main__':
  main()
