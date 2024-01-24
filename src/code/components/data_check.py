import os
from src.code.logging import LogTool
from src.code.entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validate_all_files_exist(self)-> bool:
        try:
            validation_status = None

            all_files = os.listdir(os.path.join("artifacts","dataset","data"))
            #print(all_files)
            for file in all_files:
                if file not in self.config.ALL_DATASET_FILES:
                    validation_status = False
                    LogTool.info(f"{file} file is not present in the artifacts directory!! Check Data Ingestion pipeline")

                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    LogTool.info(f"{file} file is present in the artifacts directory")
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            return validation_status
        
        except Exception as e:
            raise e