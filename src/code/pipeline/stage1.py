from src.code.config.config import ConfigurationManager
from src.code.components.data_ingestion import DataIngestion
from src.code.logging import LogTool

class DataIngestionPipeline:
    def __init__(self):
        pass
    def run(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        aws_keys=config.get_keys()
        data_ingestion = DataIngestion(config=data_ingestion_config,keys=aws_keys)
        data_ingestion.download_file_from_s3()
        data_ingestion.extract_zip_file()

if __name__ == '__main__':
    stage_1="Data Ingestion"

    try:
        LogTool.info(f"----------- {stage_1} phase started -----------")
        data_ingestion=DataIngestionPipeline()
        data_ingestion.run()
        LogTool.info(f"----------- {stage_1} phase completed -----------")

    except Exception as e:
        LogTool.exception(e)
        raise e