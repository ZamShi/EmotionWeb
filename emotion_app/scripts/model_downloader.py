from funasr import AutoModel
import os

MODEL_CACHE_DIR = os.path.join(os.path.expanduser("~"), ".cache/emotion_model")

class EmotionModel:
    _instance = None
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = AutoModel(
                model="iic/emotion2vec_plus_large",
                hub="hf",
                model_revision="v2.0.4",  # 指定模型版本
                cache_dir=MODEL_CACHE_DIR
            )
        return cls._instance