from typing import Literal

# Define available LLM types
LLMType = Literal["basic", "reasoning", "vision", "report"]

# Define agent-LLM mapping
AGENT_LLM_MAP: dict[str, LLMType] = {
    "coordinator": "basic",  # 协调
    "planner": "reasoning",  # 计划
    "supervisor": "basic",  # 决策
    "researcher": "report",  # 调研
    "coder": "report",  # 编程
    "browser": "vision",  # 浏览器操作
    "reporter": "report",  # 编写报告
}
