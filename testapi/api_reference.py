"""
Python API 使用示例文档 | Python API Usage Examples Documentation
===============================================

本文档展示了使用 OpenAI API 的两种方法：OpenAI 官方库和 Requests 库
This document demonstrates two methods of using OpenAI API: OpenAI official library and Requests library
"""

# 方法一：使用 OpenAI 库 | Method 1: Using OpenAI Library
# ================================================

from openai import OpenAI
from pathlib import Path
import warnings

# 1. 基础聊天功能 | Basic Chat Function
def openai_chat_example():
    """聊天功能示例 | Chat Function Example"""
    client = OpenAI(
        base_url='https://api.nuwaapi.com/v1',
        api_key='sk-xxx'  # 替换为你的API密钥 | Replace with your API key
    )
    
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello!"}
        ]
    )
    return completion.choices[0].message

# 2. 图片识别功能 | Image Recognition Function
def openai_vision_example():
    """图片识别示例 | Vision Analysis Example"""
    client = OpenAI(
        base_url='https://api.nuwaapi.com/v1',
        api_key='sk-xxx'
    )
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What's in this image?"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                        }
                    },
                ],
            }
        ],
        max_tokens=300,
    )
    return response.choices[0]

# 3. 文本向量化 | Text Embeddings
def openai_embeddings_example():
    """文本向量化示例 | Text Embedding Example"""
    client = OpenAI(
        base_url='https://api.nuwaapi.com/v1',
        api_key='sk-xxx'
    )
    
    response = client.embeddings.create(
        model="text-embedding-ada-002",
        input="The food was delicious and the waiter...",
        encoding_format="float"
    )
    return response

# 4. 图片生成 | Image Generation
def openai_image_generation_example():
    """图片生成示例 | Image Generation Example"""
    client = OpenAI(
        base_url='https://api.nuwaapi.com/v1',
        api_key='sk-xxx'
    )
    
    response = client.images.generate(
        model="dall-e-3",
        prompt="A cute baby sea otter",
        n=1,
        size="1024x1024"
    )
    return response

# 5. 语音生成 | Speech Generation
def openai_audio_example():
    """语音生成示例 | Speech Generation Example"""
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    client = OpenAI(
        base_url='https://api.nuwaapi.com/v1',
        api_key='sk-xxx'
    )
    
    speech_file_path = Path(__file__).parent / "speech.mp3"
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input="The quick brown fox jumped over the lazy dog."
    )
    response.stream_to_file(speech_file_path)
    return "Speech file generated: speech.mp3"

# 方法二：使用 Requests 库 | Method 2: Using Requests Library
# ====================================================

import requests
import json

# 1. 基础聊天功能 | Basic Chat Function
def requests_chat_example():
    """使用 Requests 的聊天示例 | Chat Example Using Requests"""
    url = "https://api.nuwaapi.com/v1/chat/completions"
    payload = {
        "messages": [
            {"role": "system", "content": "你是一个大语言模型机器人 | You are an AI assistant"},
            {"role": "user", "content": "你好 | Hello"}
        ],
        "stream": False,
        "model": "gpt-3.5-turbo",
        "temperature": 0.5,
        "presence_penalty": 0,
        "frequency_penalty": 0,
        "top_p": 1
    }
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer sk-xxx"  # 替换为你的API密钥 | Replace with your API key
    }
    
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

# 2. 图片识别功能 | Image Recognition Function
def requests_vision_example():
    """使用 Requests 的图片识别示例 | Vision Analysis Example Using Requests"""
    url = "https://api.nuwaapi.com/v1/chat/completions"
    payload = {
        "model": "gpt-4o",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "这是什么 | What is this?"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
                        }
                    }
                ]
            }
        ]
    }
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer sk-xxx"
    }
    
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

# 3. 文本向量化 | Text Embeddings
def requests_embeddings_example():
    """使用 Requests 的文本向量化示例 | Text Embedding Example Using Requests"""
    url = "https://api.nuwaapi.com/v1/embeddings"
    payload = {
        "input": "The food was delicious and the waiter...",
        "model": "text-embedding-ada-002",
        "encoding_format": "float"
    }
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer sk-xxx"
    }
    
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

# 4. 图片生成 | Image Generation
def requests_image_generation_example():
    """使用 Requests 的图片生成示例 | Image Generation Example Using Requests"""
    url = "https://api.nuwaapi.com/v1/images/generations"
    payload = {
        "model": "dall-e-3",
        "prompt": "A cute baby sea otter",
        "n": 1,
        "size": "1024x1024"
    }
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer sk-xxx"
    }
    
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

# 5. 语音生成 | Speech Generation
def requests_audio_example():
    """使用 Requests 的语音生成示例 | Speech Generation Example Using Requests"""
    url = "https://api.nuwaapi.com/v1/audio/speech"
    payload = {
        "model": "tts-1",
        "input": "The quick brown fox jumped over the lazy dog.",
        "voice": "alloy"
    }
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer sk-xxx"
    }
    
    response = requests.post(url, headers=headers, json=payload)
    return response.content  # 返回二进制音频数据 | Returns binary audio data

# 使用示例 | Usage Examples
if __name__ == "__main__":
    print("=== OpenAI 库示例 | OpenAI Library Examples ===")
    print("\n1. 聊天示例 | Chat Example:")
    print(openai_chat_example())
    
    print("\n2. 图片识别示例 | Vision Example:")
    print(openai_vision_example())
    
    print("\n3. 向量化示例 | Embedding Example:")
    print(openai_embeddings_example())
    
    print("\n4. 图片生成示例 | Image Generation Example:")
    print(openai_image_generation_example())
    
    print("\n5. 语音生成示例 | Speech Generation Example:")
    print(openai_audio_example())
    
    print("\n=== Requests 库示例 | Requests Library Examples ===")
    print("\n1. 聊天示例 | Chat Example:")
    print(requests_chat_example())
    
    print("\n2. 图片识别示例 | Vision Example:")
    print(requests_vision_example())
    
    print("\n3. 向量化示例 | Embedding Example:")
    print(requests_embeddings_example())
    
    print("\n4. 图片生成示例 | Image Generation Example:")
    print(requests_image_generation_example())
    
    print("\n5. 语音生成示例 | Speech Generation Example:")
    print("Audio data received") 