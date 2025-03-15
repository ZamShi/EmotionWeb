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
                hub="ms",
                cache_dir=MODEL_CACHE_DIR
            )
        return cls._instance