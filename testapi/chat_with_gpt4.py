import openai
import json
from typing import List, Dict

class ChatBot:
    def __init__(self, config_path: str = "config.json"):
        """初始化聊天机器人 | Initialize chatbot"""
        self.config = self._load_config(config_path)
        self.api_key = self.config["api_key"]
        openai.api_key = self.api_key
        self.conversation_history: List[Dict[str, str]] = []
        
    def _load_config(self, config_path: str) -> dict:
        """加载配置文件 | Load configuration file"""
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"配置文件不存在 | Configuration file does not exist: {config_path}")
        except json.JSONDecodeError:
            raise ValueError(f"配置文件格式错误 | Invalid configuration file format: {config_path}")
        
    def chat(self, user_input: str) -> str:
        """
        处理用户输入并获取GPT-4的回复 | Process user input and get GPT-4 response
        :param user_input: 用户输入的文本 | User input text
        :return: AI的回复 | AI response
        """
        try:
            # 添加用户输入到对话历史 | Add user input to conversation history
            self.conversation_history.append({"role": "user", "content": user_input})
            
            # 调用GPT-4 API | Call GPT-4 API
            response = openai.ChatCompletion.create(
                model=self.config["model"],
                messages=self.conversation_history,
                temperature=self.config["temperature"],
                max_tokens=self.config["max_tokens"]
            )
            
            # 获取AI回复 | Get AI response
            ai_response = response.choices[0].message.content
            
            # 添加AI回复到对话历史 | Add AI response to conversation history
            self.conversation_history.append({"role": "assistant", "content": ai_response})
            
            return ai_response
            
        except Exception as e:
            return f"发生错误 | Error occurred: {str(e)}"
    
    def clear_history(self):
        """清除对话历史 | Clear conversation history"""
        self.conversation_history = []

def main():
    try:
        # 创建聊天机器人实例 | Create chatbot instance
        chatbot = ChatBot()
        
        print("欢迎使用GPT-4聊天机器人！| Welcome to GPT-4 Chatbot!")
        print("输入'退出'结束对话，输入'清除'清除对话历史。| Enter 'exit' to end chat, 'clear' to clear history.")
        
        while True:
            user_input = input("\n你 | You: ")
            
            if user_input.lower() in ['退出', 'exit']:
                print("感谢使用，再见！| Thank you for using, goodbye!")
                break
            elif user_input.lower() in ['清除', 'clear']:
                chatbot.clear_history()
                print("对话历史已清除！| Conversation history cleared!")
                continue
                
            response = chatbot.chat(user_input)
            print("\nGPT-4:", response)
            
    except Exception as e:
        print(f"程序启动失败 | Program startup failed: {str(e)}")

if __name__ == "__main__":
    main() 