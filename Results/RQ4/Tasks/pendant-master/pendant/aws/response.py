from typing import Mapping, Optional

__all__ = ['AwsResponse', 'SubmitJobResponse']


class AwsResponse(object):
    """A generic HTTP response from AWS."""

    pass


class SubmitJobResponse(AwsResponse):
    """A Batch submit-job response."""

    def __init__(self, response):
        self._response = response
        self.metadata = response.get('ResponseMetadata', {})
        self.job_name = response.get('jobName', None)
        self.job_id = response.get('jobId', None)

    def is_ok(self):
        """Return if response was successful."""
        return self.http_code() == 200

    def http_code(self):
        """Return the HTTP status code of this response."""
        http_code = self.metadata.get('HTTPStatusCode', 500)
        return http_code
