from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .model_loader import EmotionModel
from io import BytesIO
import numpy as np
import logging
import json

logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'index.html')

class NumpyEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, np.ndarray):
            return o.tolist()
        if isinstance(o, np.generic):
            return o.item()
        return super(NumpyEncoder, self).default(o)

def process_emotion_result(raw_result):
    """处理模型输出结果，确保所有数据类型可以被JSON序列化"""
    # 假设 raw_result 是一个列表，且第一个元素包含我们需要的数据
    result = raw_result[0] if isinstance(raw_result, list) else raw_result
    
    return {
        'emotions': result.get('labels', []),  # 使用 get 方法安全获取数据
        'scores': [float(score) for score in result.get('scores', [])],  # 确保分数是 float 类型
        'prediction': {
            'emotion': str(result.get('labels', ['unknown'])[0]),  # 取最可能的情绪
            'confidence': float(result.get('scores', [0])[0])  # 取最高的置信度
        }
    }

@csrf_exempt
def analyze_emotion(request):
    if request.method != 'POST':
        return JsonResponse({'error': '仅支持POST请求'}, status=405)
    
    if not request.FILES.get('audio'):
        return JsonResponse({'error': '未找到音频文件'}, status=400)

    audio_file = request.FILES['audio']
    buffer = None
    
    try:
        # 使用BytesIO在内存中处理音频文件
        buffer = BytesIO()
        for chunk in audio_file.chunks():
            buffer.write(chunk)
        buffer.seek(0)
        
        # 读取音频数据
        audio_data = buffer.read()
        
        # 获取模型实例并进行预测
        model = EmotionModel.get_instance()
        raw_result = model.generate(audio_data, output_dir="outputs")
        
        # 处理结果并返回
        processed_result = process_emotion_result(raw_result)
        json_data = json.dumps(processed_result, cls=NumpyEncoder)
        return JsonResponse(json.loads(json_data))
        
    except Exception as e:
        logger.error(f"情绪分析失败: {str(e)}", exc_info=True)
        return JsonResponse({
            'error': '分析失败',
            'detail': str(e)
        }, status=500)
    finally:
        if buffer is not None:
            buffer.close()