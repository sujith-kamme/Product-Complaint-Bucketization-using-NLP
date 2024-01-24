from src.code.config.config import ConfigurationManager
from src.code.components.data_transform_and_model_evaluation import DataTransformationModelEval
from src.code.logging import LogTool

STAGE_NAME = "Data Transformation and Model Evaluation"

class DataTransformationModelEvaluationPipeline:
    def __init__(self):
        pass

    def run(self):
        config = ConfigurationManager()
        dt_me_config = config.get_dt_me_config()
        dt_me_obj = DataTransformationModelEval(config=dt_me_config)
        dt_me_obj.transform_and_evaluation()




if __name__ == '__main__':
    try:
        LogTool.info(f"------------- {STAGE_NAME} started -------------")
        obj = DataTransformationModelEvaluationPipeline()
        obj.run()
        LogTool.info(f"------------- {STAGE_NAME} completed -----------")
    except Exception as e:
        LogTool.exception(e)
        raise e