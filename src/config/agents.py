from typing import Literal

# Define available LLM types
LLMType = Literal["basic", "reasoning", "vision"]

# Define agent-LLM mapping
AGENT_LLM_MAP: dict[str, LLMType] = {
    "coordinator": "basic",  # 协调默认使用basic llm
    "planner": "reasoning",  # 计划默认使用 reasoning llm
    "supervisor": "basic",  # 决策使用 reasoning llm
    "researcher": "reasoning",  # 调研使用 reasoning llm
    "coder": "reasoning",  # 编程任务使用basic llm
    "browser": "vision",  # 浏览器操作使用vision llm
    "reporter": "basic",  # 编写报告使用basic llm
}
