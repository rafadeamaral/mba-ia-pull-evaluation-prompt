"""
Script para fazer pull de prompts do LangSmith Prompt Hub.

Este script:
1. Conecta ao LangSmith usando credenciais do .env
2. Faz pull dos prompts do Hub
3. Salva localmente em prompts/bug_to_user_story_v1.yml

SIMPLIFICADO: Usa serialização nativa do LangChain para extrair prompts.
"""

import sys
from datetime import date
from pathlib import Path
from dotenv import load_dotenv
from langsmith import Client
from utils import save_yaml, check_env_vars, print_section_header, save_yaml

load_dotenv()


def pull_prompts_from_langsmith():
    print("🔄 Conectando ao LangSmith Prompt Hub...")

    client = Client()
    prompt = client.pull_prompt("leonanluppi/bug_to_user_story_v1")

    prompt_dict = extract_prompt_from_response(prompt)

    output_path = Path("prompts/bug_to_user_story_v1.yml")

    if save_yaml(prompt_dict, output_path):
        print(f"✅ Prompt salvo em: {output_path}")
    else:
        print("❌ Falha ao salvar o prompt.")

def extract_prompt_from_response(prompt) -> dict:
    
    # Extrai system_prompt do primeiro template (SystemMessagePromptTemplate)
    system_prompt = prompt.messages[0].prompt.template if len(prompt.messages) > 0 else ""
    
    # Extrai user_prompt do segundo template (HumanMessagePromptTemplate)
    user_prompt = prompt.messages[1].prompt.template if len(prompt.messages) > 1 else ""

    # Extrai o nome do repositório do hub
    repo_name = prompt.metadata.get("lc_hub_repo")
    
    return {
        "name": repo_name,
        "description": "Prompt para converter relatos de bugs em User Stories",
        "system_prompt": system_prompt,
        "user_prompt": user_prompt,
        "version": "v1",
        "created_at": date.today(),
        "tags": ["bug-analysis", "user-story", "product-management"]
    }

def main():
    print_section_header("Pull de Prompts do LangSmith Prompt Hub")
    
    required_vars = ["LANGSMITH_API_KEY"]
    if not check_env_vars(required_vars):
        return 1

    pull_prompts_from_langsmith()

    return 0


if __name__ == "__main__":
    sys.exit(main())
