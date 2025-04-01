import openai
import json
import requests
from typing import Dict

class TextAnalyzer:
    def __init__(self, config_path: str = "config.json"):
        """初始化文本分析器 | Initialize text analyzer"""
        self.config = self._load_config(config_path)
        self.api_key = self.config["api_key"]
        self.api_url = self.config["api_url"]
        
    def _load_config(self, config_path: str) -> dict:
        """加载配置文件 | Load configuration file"""
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"配置文件不存在 | Configuration file does not exist: {config_path}")
        except json.JSONDecodeError:
            raise ValueError(f"配置文件格式错误 | Invalid configuration file format: {config_path}")
    
    def analyze_text(self, text: str, analysis_type: str = "general") -> str:
        """
        分析文本 | Analyze text
        :param text: 要分析的文本 | Text to analyze
        :param analysis_type: 分析类型（general-通用分析, sentiment-情感分析, summary-摘要, keywords-关键词提取）
                            Analysis type (general-general analysis, sentiment-sentiment analysis, 
                            summary-text summary, keywords-keyword extraction)
        :return: 分析结果 | Analysis result
        """
        try:
            # 根据分析类型构建提示词 | Build prompts based on analysis type
            prompts = {
                "general": "请对以下文本进行全面分析，包括主要内容、写作风格、逻辑结构等方面：\n" +
                          "Please provide a comprehensive analysis of the following text, including main content, writing style, and logical structure:\n",
                "sentiment": "请对以下文本进行情感分析，包括情感倾向、情感强度等方面：\n" +
                           "Please analyze the sentiment of the following text, including emotional tendency and intensity:\n",
                "summary": "请对以下文本进行摘要，提取主要观点和关键信息：\n" +
                         "Please summarize the following text, extracting main points and key information:\n",
                "keywords": "请从以下文本中提取关键词和主题词，并简要说明其重要性：\n" +
                          "Please extract keywords and themes from the following text, and briefly explain their importance:\n"
            }
            
            prompt = prompts.get(analysis_type, prompts["general"])
            
            # 准备请求数据 | Prepare request data
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}"
            }
            
            data = {
                "model": self.config["model"],
                "messages": [
                    {"role": "system", "content": "你是一个专业的文本分析助手，请提供详细的分析结果。\n" +
                                                "You are a professional text analysis assistant, please provide detailed analysis results."},
                    {"role": "user", "content": prompt + text}
                ],
                "temperature": self.config["temperature"],
                "max_tokens": self.config["max_tokens"]
            }
            
            # 发送请求 | Send request
            response = requests.post(
                self.api_url,
                headers=headers,
                json=data
            )
            
            if response.status_code == 200:
                result = response.json()
                return result["choices"][0]["message"]["content"]
            else:
                return f"API请求失败 | API request failed: {response.status_code} - {response.text}"
            
        except Exception as e:
            return f"分析过程中发生错误 | Error occurred during analysis: {str(e)}"

def main():
    try:
        # 创建文本分析器实例 | Create text analyzer instance
        analyzer = TextAnalyzer()
        
        print("欢迎使用文本分析工具！| Welcome to Text Analysis Tool!")
        print("分析类型 | Analysis Types:")
        print("1. 通用分析 | General Analysis")
        print("2. 情感分析 | Sentiment Analysis")
        print("3. 文本摘要 | Text Summary")
        print("4. 关键词提取 | Keyword Extraction")
        print("输入'退出'结束程序 | Enter 'exit' to end program")
        
        while True:
            analysis_type = input("\n请选择分析类型（1-4）| Please select analysis type (1-4): ")
            
            if analysis_type.lower() in ['退出', 'exit']:
                print("感谢使用，再见！| Thank you for using, goodbye!")
                break
                
            if analysis_type not in ['1', '2', '3', '4']:
                print("无效的选择，请重新输入！| Invalid choice, please try again!")
                continue
                
            text = input("\n请输入要分析的文本 | Please enter the text to analyze:\n")
            
            # 将数字选择转换为对应的分析类型 | Convert number choice to corresponding analysis type
            type_mapping = {
                '1': 'general',
                '2': 'sentiment',
                '3': 'summary',
                '4': 'keywords'
            }
            
            result = analyzer.analyze_text(text, type_mapping[analysis_type])
            print("\n分析结果 | Analysis Result:")
            print(result)
            
    except Exception as e:
        print(f"程序启动失败 | Program startup failed: {str(e)}")

if __name__ == "__main__":
    main() 