from src.code.logging import LogTool
from src.code.pipeline.stage1 import DataIngestionPipeline
from src.code.pipeline.stage2 import DataValidationPipeline
from src.code.pipeline.stage3 import DataTransformationModelEvaluationPipeline

stage_1="Data Ingestion"

try:
    LogTool.info(f"----------- {stage_1} phase started -----------")
    data_ingestion=DataIngestionPipeline()
    data_ingestion.run()
    LogTool.info(f"----------- {stage_1} phase completed -----------")

except Exception as e:
    LogTool.exception(e)
    raise e


stage_2="Data Validation"

try:
    LogTool.info(f"----------- {stage_2} phase started -----------")
    data_validation=DataValidationPipeline()
    data_validation.run()
    LogTool.info(f"----------- {stage_2} phase completed -----------")

except Exception as e:
    LogTool.exception(e)
    raise e

stage_3="Data Transformation and Model Evaluation"
try:
    LogTool.info(f"------------- {stage_3} started -------------")
    obj = DataTransformationModelEvaluationPipeline()
    obj.run()
    LogTool.info(f"------------- {stage_3} completed -----------")
except Exception as e:
    LogTool.exception(e)
    raise e