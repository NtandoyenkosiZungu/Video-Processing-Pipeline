from datetime import datetime

class JobStatus:
    """
    Job Status constants, to use constants instead of raw strings
    """
    QUEUED = "queued"
    PROCESSING = "processing"
    FINISHED = "finished"
    FAILED = "failed"

class Job:
    """
    Represents a video processng job.
    This is a model/class that will hold information relating to the video processing job.

    It does not store any database logic.
    """

    def __init__(
            self, 
            job_id:str, 
            status: str, 
            raw_file_path: str,
            output_path: str = None,
            error_message: str = None
        ):
        """
        job_id: unique identifier for a job - what is returned to the client.

        status: where along the pipeline is the job currently

        raw_file_path: where the file upload was saved

        output_path: where the processed file will be go - Empty when the job has not been processed

        error_message: what went wrong - Empty when the job has not been processed
        """
        self.job_id = job_id
        self.status = status
        self.raw_file_path = raw_file_path
        self.output_path = output_path
        self.error_message = error_message
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        Converts the Job to a dictionary
        """
        return {
            "job_id": self.job_id,
            "status": self.status,
            "raw_file_path": self.raw_file_path,
            "output_path": self.output_path,
            "error_message": self.error_message,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

