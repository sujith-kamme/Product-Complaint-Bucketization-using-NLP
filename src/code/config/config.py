from src.code.entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from src.code.constants import *
from src.code.utils.common import read_yaml, create_directories


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        keys_filepath = KEYS_FILE_PATH
        ):

        self.config = read_yaml(config_filepath)
        self.keys = read_yaml(keys_filepath)

        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.dataset

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir ,
            s3_bucket=config.s3_bucket,
            s3_dataset=config.s3_dataset
        )
        return data_ingestion_config
    
    def get_keys(self):
        keys=self.keys
        return keys
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            ALL_DATASET_FILES=config.ALL_DATASET_FILES
        )
        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path
        )
        return data_transformation_config
    
    