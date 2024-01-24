from dataclasses import dataclass #used for creating entities
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    s3_bucket: str
    s3_dataset: str


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_DATASET_FILES: list

@dataclass(frozen=True)
class DataTransformationModelEvalConfig:
    root_dir: Path
    data_path: Path
    model_path: Path
    metric_file_name: Path

