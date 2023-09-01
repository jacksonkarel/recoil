import argparse
from selfmodifai.agents.hf_agent.llama2_agent.llama2_agent import llama2_agent
from selfmodifai.agents.openai_agents.openai_func_agent.openai_func_agent import openai_func_agent
from selfmodifai.agents.openai_agents.gpt4_agent.agents.gpt_4_training_editor_agent.agents.gpt4_te_alpaca_lora_agent import (
    gpt4_te_alapca_lora_agent,
)


def cli_parser():
    sm_parser = argparse.ArgumentParser(description="Autonomous AI agents modifying the training code of ML models")

    sm_parser.add_argument("agent", action="store", choices=["llama2", "gpt4", "gpt4_alpaca_lora"], help="Agent type")

    args = sm_parser.parse_args()

    agent = args.agent
    agents = {"llama2": llama2_agent, "gpt4": openai_func_agent, "gpt4_alapca_lora": gpt4_te_alapca_lora_agent}

    chosen_agent = agents[agent]
    chosen_agent()
