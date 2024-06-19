from fastnode.agents.base_agent import BaseAgent
from fastnode.llms.base_llm import BaseLlm
from fastnode.prompts.openai_prompt import (AUTONODE_PLANNER_PROMPT_APOLLO,
                                            AUTONODE_PLANNER_PROMPT_TWITTER,
                                            AUTONODE_PLANNER_PROMPT_GMAIL)


class PlanningAgent(BaseAgent):

    def __init__(self, planner_prompt: str, llm_instance: BaseLlm):
        self.llm = llm_instance
        self.prompt_hash = {
            "apollo": AUTONODE_PLANNER_PROMPT_APOLLO,
            "twitter": AUTONODE_PLANNER_PROMPT_TWITTER,
            "gmail": AUTONODE_PLANNER_PROMPT_GMAIL
        }
        self.prompt = self.prompt_hash.get(planner_prompt)
        fast().__init__(llm_instance)

    def execute(self, objective: str) -> str:

        prompt = self.prompt.format(objective=objective)
        response = self.llm.chat_completion(messages=[{"role": "system", "content": prompt},
                                                      {"role": "user", "content": ""}])
        content = response["content"]
        return content
