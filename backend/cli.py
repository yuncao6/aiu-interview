# CLI 命令行交互客户
from agent import ask_agent

def main():
    print("=== AIU 智能体 CLI 客户端 ===")
    print("输入 'quit' 退出\n")
    while True:
        user_input = input("你: ")
        if user_input.lower() in ['quit', 'exit']:
            break
        print("AI: ", end="", flush=True)
        print(ask_agent(user_input))

if __name__ == "__main__":
    main()