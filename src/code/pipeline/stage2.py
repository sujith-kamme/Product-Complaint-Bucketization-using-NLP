from src.code.config.config import ConfigurationManager
from src.code.components.data_check import DataValidation
from src.code.logging import LogTool

class DataValidationPipeline:
    def __init__(self):
        pass
    def run(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exist()

if __name__=="__main__":
    stage_2="Data Validation"

    try:
        LogTool.info(f"----------- {stage_2} phase started -----------")
        data_validation=DataValidationPipeline()
        data_validation.run()
        LogTool.info(f"----------- {stage_2} phase completed -----------")

    except Exception as e:
        LogTool.exception(e)
        raise e