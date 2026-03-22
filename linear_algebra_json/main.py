import json
from task_processor import TaskProcessor
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # 强制加入当前目录

def main():
    with open("./data.json", "r", encoding="utf-8") as f:
      data = json.load(f)

    processor = TaskProcessor(data)
    processor.run()

if __name__ == "__main__":
    main()
