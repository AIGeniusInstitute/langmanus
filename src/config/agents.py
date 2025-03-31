from typing import Literal

# Define available LLM types:
# basic: Doubao 1.5 Pro
# reasoning:  DeepSeek R1
# vision:  Doubao 1.5 Pro
# report:   DeepSeek V3 20250324
LLMType = Literal["basic", "reasoning", "vision", "report"]

# Define agent-LLM mapping
AGENT_LLM_MAP: dict[str, LLMType] = {
    "coordinator": "basic",  # 协调
    "planner": "reasoning",  # 计划
    "supervisor": "basic",  # 监督
    "researcher": "report",  # 调研
    "coder": "report",  # 编程
    "browser": "vision",  # 浏览器操作
    "reporter": "report",  # 编写报告
}
