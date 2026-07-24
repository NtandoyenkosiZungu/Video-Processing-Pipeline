import psycopg2
import psycopg2.extras
import os
from dotenv import load_dotenv
from datetime import datetime
from core.models import Job, JobStatus


load_dotenv()

print("DB_HOST:", os.getenv("DB_HOST"))
print("DB_PORT:", os.getenv("DB_PORT"))
print("DB_NAME:", os.getenv("DB_NAME"))
print("DB_USER:", os.getenv("DB_USER"))
print("DB_PASSWD:", os.getenv("DB_PASSWD"))

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT")),
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWD")
}

def get_connection():
    """
    Opens and returns a PostgresSQL connection.
    DictCursor makes rows behave like dicitonaries
    """

    connection = psycopg2.connect(**DB_CONFIG)
    return connection

def init_db():
    """
    Creates the Jobs table if it does not already exists.
    Called once when the Application starts
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            job_id TEXT PRIMARY KEY,
            status TEXT NOT NULL,
            raw_file_path TEXT NOT NULL,
            output_path TEXT,
            error_message TEXT,
            created_at TIMESTAMP NOT NULL,
            updated_at TIMESTAMP NOT NULL    
        )
    """)

    connection.commit()
    cursor.close()
    connection.close()
    print("init_db ran successfully")

def create_job(job: Job):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO jobs (job_id, status, raw_file_path, output_path, error_message, created_at, updated_at) 
        VALUES(%s, %s, %s, %s, %s, %s, %s)
        """,
        (job.job_id, job.status, job.raw_file_path, job.output_path, job.error_message, job.created_at, job.updated_at)
    )

    connection.commit()
    cursor.close()
    connection.close()
    print("Job creation successful")

def get_job(job_id: str):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT * FROM jobs WHERE job_id = %s,
        """,
        (job_id)
    )

    row = cursor.fetchone()

    connection.commit()
    cursor.close()
    connection.close()

    if row == None:
        return None

    return Job(
        job_id= row["job_id"],
        status= row["status"],
        raw_file_path= row["raw_file_path"],
        output_path= row["output_path"],
        error_message= row["error_message"]
    )
