"""
Testes automatizados para validação de prompts.
"""
import pytest
import yaml
import sys
from pathlib import Path

# Adicionar src ao path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

def load_prompts(file_path: str):
    """Carrega prompts do arquivo YAML."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

class TestPrompts:
    def test_prompt_has_system_prompt(self):
        """Verifica se o campo 'system_prompt' existe e não está vazio."""
        prompts = load_prompts("prompts/bug_to_user_story_v2.yml")
        assert "system_prompt" in prompts
        assert prompts["system_prompt"] is not None and prompts["system_prompt"].strip() != "", \
            "❌ Campo 'system_prompt' está vazio ou não definido."
        print("✅ Prompt possui system_prompt válido.")

    def test_prompt_has_role_definition(self):
        """Verifica se o prompt define uma persona (ex: "Você é um Product Manager")."""
        prompts = load_prompts("prompts/bug_to_user_story_v2.yml")
        assert "system_prompt" in prompts
        assert "Você é" in prompts["system_prompt"], \
            "❌ Prompt não define uma persona clara (ex: 'Você é um Product Manager')."
        print("✅ Prompt define uma persona válida.")

    def test_prompt_mentions_format(self):
        """Verifica se o prompt exige formato Markdown ou User Story padrão."""
        prompts = load_prompts("prompts/bug_to_user_story_v2.yml")
        assert "system_prompt" in prompts
        assert "Markdown" in prompts["system_prompt"] or "User Story" in prompts["system_prompt"], \
            "❌ Prompt não menciona formato de saída esperado (Markdown ou User Story)."
        print("✅ Prompt menciona formato de saída esperado.")

    def test_prompt_has_few_shot_examples(self):
        """Verifica se o prompt contém exemplos de entrada/saída (técnica Few-shot)."""
        prompts = load_prompts("prompts/bug_to_user_story_v2.yml")
        prompt_text = prompts["system_prompt"]
        # Verifica se contém indicadores de exemplos estruturados
        has_example_section = any([
            "Exemplo" in prompt_text and ":" in prompt_text,
            "Input:" in prompt_text or "Entrada:" in prompt_text,
            "Output:" in prompt_text or "Saída:" in prompt_text,
            "##" in prompt_text and "Exemplo" in prompt_text  # Headers Markdown
        ])
        # Verifica se há pelo menos 2 blocos de código (indicando exemplo completo)
        code_blocks = prompt_text.count("```")
        has_multiple_examples = code_blocks >= 2
        assert has_example_section or has_multiple_examples, \
            "❌ Prompt não contém exemplos de entrada/saída estruturados."
        print("✅ Prompt contém exemplos de entrada/saída.")

    def test_prompt_no_todos(self):
        """Garante que você não esqueceu nenhum `[TODO]` no texto."""
        prompts = load_prompts("prompts/bug_to_user_story_v2.yml")
        prompt_text = prompts.get("system_prompt", "") + " " + prompts.get("user_prompt", "")
        assert "[TODO]" not in prompt_text, \
            "❌ Prompt contém placeholders [TODO] que precisam ser preenchidos."
        print("✅ Prompt não contém placeholders [TODO].")

    def test_minimum_techniques(self):
        """Verifica (através dos metadados do yaml) se pelo menos 2 técnicas foram listadas."""
        prompts = load_prompts("prompts/bug_to_user_story_v2.yml")
        assert "techniques" in prompts
        assert isinstance(prompts["techniques"], list)
        assert len(prompts["techniques"]) >= 2, \
            f"❌ Prompt deve listar pelo menos 2 técnicas."
        print("✅ Prompt lista pelo menos 2 técnicas utilizadas.")

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])