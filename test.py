from src.code.pipeline.prediction import PredictionPipeline

obj=PredictionPipeline()
text="I am a victim of mortage loan that I took last year. It is very difficult to understand the reason why it is painful"
prob,label=obj.transform_and_predict(text)
print(f"{label}:{prob}")
