import os
import urllib.request as request
import zipfile
from src.code.logging import LogTool
from src.code.utils.common import get_size
import boto3
from botocore.exceptions import NoCredentialsError
from src.code.entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self, config, keys):
        self.config = config
        self.keys = keys

    def download_file_from_s3(self):
        if not os.path.exists(self.config.local_data_file):
            self._download_file_from_s3()
        else:
            LogTool.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    def _download_file_from_s3(self):
        try:
            s3 = boto3.client(
                's3',
                aws_access_key_id=self.keys.aws_access_key_id,
                aws_secret_access_key=self.keys.aws_secret_access_key
            )

            s3.download_file(self.config.s3_bucket, self.config.s3_dataset, self.config.local_data_file)

            LogTool.info(f"{self.config.local_data_file} downloaded from S3!")

        except NoCredentialsError:
            LogTool.error("Credentials not available. Unable to download file from S3.")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)