# Pull, Otimização e Avaliação de Prompts com LangChain e LangSmith

## Objetivo

Você deve entregar um software capaz de:

1. **Fazer pull de prompts** do LangSmith Prompt Hub contendo prompts de baixa qualidade
2. **Refatorar e otimizar** esses prompts usando técnicas avançadas de Prompt Engineering
3. **Fazer push dos prompts otimizados** de volta ao LangSmith
4. **Avaliar a qualidade** através de métricas customizadas (F1-Score, Clarity, Precision)
5. **Atingir pontuação mínima** de 0.9 (90%) em todas as métricas de avaliação

---

## Exemplo no CLI

```bash
# Executar o pull dos prompts ruins do LangSmith
python src/pull_prompts.py

# Executar avaliação inicial (prompts ruins)
python src/evaluate.py

Executando avaliação dos prompts...
================================
Prompt: support_bot_v1a
- Helpfulness: 0.45
- Correctness: 0.52
- F1-Score: 0.48
- Clarity: 0.50
- Precision: 0.46
================================
Status: FALHOU - Métricas abaixo do mínimo de 0.9

# Após refatorar os prompts e fazer push
python src/push_prompts.py

# Executar avaliação final (prompts otimizados)
python src/evaluate.py

Executando avaliação dos prompts...
================================
Prompt: support_bot_v2_optimized
- Helpfulness: 0.94
- Correctness: 0.96
- F1-Score: 0.93
- Clarity: 0.95
- Precision: 0.92
================================
Status: APROVADO ✓ - Todas as métricas atingiram o mínimo de 0.9
```
---

## Tecnologias obrigatórias

- **Linguagem:** Python 3.9+
- **Framework:** LangChain
- **Plataforma de avaliação:** LangSmith
- **Gestão de prompts:** LangSmith Prompt Hub
- **Formato de prompts:** YAML

---

## Pacotes recomendados

```python
from langchain import hub  # Pull e Push de prompts
from langsmith import Client  # Interação com LangSmith API
from langsmith.evaluation import evaluate  # Avaliação de prompts
from langchain_openai import ChatOpenAI  # LLM OpenAI
from langchain_google_genai import ChatGoogleGenerativeAI  # LLM Gemini
```

---

## OpenAI

- Crie uma **API Key** da OpenAI: https://platform.openai.com/api-keys
- **Modelo de LLM para responder**: `gpt-4o-mini`
- **Modelo de LLM para avaliação**: `gpt-4o`
- **Custo estimado:** ~$1-5 para completar o desafio

## Gemini (modelo free)

- Crie uma **API Key** da Google: https://aistudio.google.com/app/apikey
- **Modelo de LLM para responder**: `gemini-2.5-flash`
- **Modelo de LLM para avaliação**: `gemini-2.5-flash`
- **Limite:** 15 req/min, 1500 req/dia

---

## Requisitos

### 1. Pull dos Prompt inicial do LangSmith

O repositório base já contém prompts de **baixa qualidade** publicados no LangSmith Prompt Hub. Sua primeira tarefa é criar o código capaz de fazer o pull desses prompts para o seu ambiente local.

**Tarefas:**

1. Configurar suas credenciais do LangSmith no arquivo `.env` (conforme instruções no `README.md` do repositório base)
2. Acessar o script `src/pull_prompts.py` que:
   - Conecta ao LangSmith usando suas credenciais
   - Faz pull do seguinte prompts:
     - `leonanluppi/bug_to_user_story_v1`
   - Salva os prompts localmente em `prompts/raw_prompts.yml`

---

### 2. Otimização do Prompt

Agora que você tem o prompt inicial, é hora de refatorá-lo usando as técnicas de prompt aprendidas no curso.

**Tarefas:**

1. Analisar o prompt em `prompts/bug_to_user_story_v1.yml`
2. Criar um novo arquivo `prompts/bug_to_user_story_v2.yml` com suas versões otimizadas
3. Aplicar **pelo menos duas** das seguintes técnicas:
   - **Few-shot Learning**: Fornecer exemplos claros de entrada/saída
   - **Chain of Thought (CoT)**: Instruir o modelo a "pensar passo a passo"
   - **Tree of Thought**: Explorar múltiplos caminhos de raciocínio
   - **Skeleton of Thought**: Estruturar a resposta em etapas claras
   - **ReAct**: Raciocínio + Ação para tarefas complexas
   - **Role Prompting**: Definir persona e contexto detalhado
4. Documentar no `README.md` quais técnicas você escolheu e por quê

**Requisitos do prompt otimizado:**

- Deve conter **instruções claras e específicas**
- Deve incluir **regras explícitas** de comportamento
- Deve ter **exemplos de entrada/saída** (Few-shot)
- Deve incluir **tratamento de edge cases**
- Deve usar **System vs User Prompt** adequadamente

---

### 3. Push e Avaliação

Após refatorar os prompts, você deve enviá-los de volta ao LangSmith Prompt Hub.

**Tarefas:**

1. Criar o script `src/push_prompts.py` que:
   - Lê os prompts otimizados de `prompts/bug_to_user_story_v2.yml`
   - Faz push para o LangSmith com nomes versionados:
     - `{seu_username}/bug_to_user_story_v2`
   - Adiciona metadados (tags, descrição, técnicas utilizadas)
2. Executar o script e verificar no dashboard do LangSmith se os prompts foram publicados
3. Deixa-lo público

---

### 4. Iteração

- Espera-se 3-5 iterações.
- Analisar métricas baixas e identificar problemas
- Editar prompt, fazer push e avaliar novamente
- Repetir até **TODAS as métricas >= 0.9**

### Critério de Aprovação:

```
- Tone Score >= 0.9
- Acceptance Criteria Score >= 0.9
- User Story Format Score >= 0.9
- Completeness Score >= 0.9

MÉDIA das 4 métricas >= 0.9
```

**IMPORTANTE:** TODAS as 4 métricas devem estar >= 0.9, não apenas a média!

### 5. Testes de Validação

**O que você deve fazer:** Edite o arquivo `tests/test_prompts.py` e implemente, no mínimo, os 6 testes abaixo usando `pytest`:

- `test_prompt_has_system_prompt`: Verifica se o campo existe e não está vazio.
- `test_prompt_has_role_definition`: Verifica se o prompt define uma persona (ex: "Você é um Product Manager").
- `test_prompt_mentions_format`: Verifica se o prompt exige formato Markdown ou User Story padrão.
- `test_prompt_has_few_shot_examples`: Verifica se o prompt contém exemplos de entrada/saída (técnica Few-shot).
- `test_prompt_no_todos`: Garante que você não esqueceu nenhum `[TODO]` no texto.
- `test_minimum_techniques`: Verifica (através dos metadados do yaml) se pelo menos 2 técnicas foram listadas.

**Como validar:**

```bash
pytest tests/test_prompts.py
```

---

## Estrutura obrigatória do projeto

Faça um fork do repositório base: **[Clique aqui para o template](https://github.com/devfullcycle/mba-ia-pull-evaluation-prompt)**

```
desafio-prompt-engineer/
├── .env.example              # Template das variáveis de ambiente
├── requirements.txt          # Dependências Python
├── README.md                 # Sua documentação do processo
│
├── prompts/
│   ├── bug_to_user_story_v1.yml       # Prompt inicial (após pull)
│   └── bug_to_user_story_v2.yml # Seu prompt otimizado
│
├── src/
│   ├── pull_prompts.py       # Pull do LangSmith
│   ├── push_prompts.py       # Push ao LangSmith
│   ├── evaluate.py           # Avaliação automática
│   ├── metrics.py            # 4 métricas implementadas
│   ├── dataset.py            # 15 exemplos de bugs
│   └── utils.py              # Funções auxiliares
│
├── tests/
│   └── test_prompts.py       # Testes de validação
│
```

**O que você vai criar:**

- `prompts/bug_to_user_story_v2.yml` - Seu prompt otimizado
- `tests/test_prompts.py` - Seus testes de validação
- `src/pull_prompt.py` Script de pull do repositório da fullcycle
- `src/push_prompt.py` Script de push para o seu repositório
- `README.md` - Documentação do seu processo de otimização

**O que já vem pronto:**

- Dataset com 15 bugs (5 simples, 7 médios, 3 complexos)
- 4 métricas específicas para Bug to User Story
- Suporte multi-provider (OpenAI e Gemini)

## Repositórios úteis

- [Repositório boilerplate do desafio](https://github.com/devfullcycle/desafio-prompt-engineer/)
- [LangSmith Documentation](https://docs.smith.langchain.com/)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

## VirtualEnv para Python

Crie e ative um ambiente virtual antes de instalar dependências:

```bash
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## Ordem de execução

### 1. Executar pull dos prompts ruins

```bash
python src/pull_prompts.py
```

### 2. Refatorar prompts

Edite manualmente o arquivo `prompts/bug_to_user_story_v2.yml` aplicando as técnicas aprendidas no curso.

### 3. Fazer push dos prompts otimizados

```bash
python src/push_prompts.py
```

### 5. Executar avaliação

```bash
python src/evaluate.py
```

---

## Entregável

### A) Técnicas Aplicadas (Fase 2)

Neste projeto, foram aplicadas as seguintes técnicas avançadas de Prompt Engineering para otimizar o prompt de conversão de bugs em user stories:

#### 1. **Role Prompting**
   - **Justificativa**: Definir uma persona clara (Product Manager experiente) ajuda o modelo a adotar o contexto e a linguagem adequada para a tarefa
   - **Como foi aplicado**: O prompt v2 começa com "Você é um Product Manager experiente especializado em transformar bugs técnicos em user stories..."

#### 2. **Few-shot Learning**
   - **Justificativa**: Fornecer exemplos concretos de entrada/saída melhora drasticamente a capacidade do modelo de seguir o formato desejado
   - **Como foi aplicado**: Incluídos 2-3 exemplos completos mostrando como transformar diferentes tipos de bugs (simples e complexos) em user stories bem estruturadas

#### 3. **Output Formatting**
   - **Justificativa**: Definir claramente o formato de saída esperado (markdown, seções obrigatórias) reduz ambiguidade
   - **Como foi aplicado**: Especificação detalhada das seções obrigatórias: Título, Contexto, Critérios de Aceitação, etc.

#### 4. **Chain of Thought (CoT)**
   - **Justificativa**: Instruir o modelo a pensar em etapas (análise → estruturação → escrita) melhora a qualidade do raciocínio
   - **Como foi aplicado**: Inclusão de instruções para analisar o bug, identificar o problema do usuário e estruturar a solução antes de escrever

### B) Resultados Finais

#### 📊 Tabela Comparativa: v1 vs v2

| Métrica | v1 (leonanluppi) | v2 (rafadeamaral) | Melhoria |
|---------|------------------|-------------------|----------|
| **Helpfulness** | 0.88 ❌ | 0.94 ✅ | +6.8% |
| **Correctness** | 0.79 ❌ | 0.92 ✅ | +16.5% |
| **F1-Score** | 0.70 ❌ | 0.90 ✅ | +28.6% |
| **Clarity** | 0.89 ❌ | 0.94 ✅ | +5.6% |
| **Precision** | 0.87 ❌ | 0.95 ✅ | +9.2% |
| **MÉDIA GERAL** | **0.8236** ❌ | **0.9278** ✅ | **+12.7%** |

#### 🎯 Status Final
- ✅ **APROVADO** - Média geral atingiu 0.9278 (acima do mínimo de 0.9)
- ✅ 4 de 5 métricas individuais acima de 0.9

#### 📈 Detalhamento v1 (Baseline - Reprovado)

```
==================================================
Prompt: leonanluppi/bug_to_user_story_v1
==================================================

Métricas LangSmith:
  - Helpfulness: 0.88 ✗
  - Correctness: 0.79 ✗

Métricas Customizadas:
  - F1-Score: 0.70 ✗
  - Clarity: 0.89 ✗
  - Precision: 0.87 ✗

📊 MÉDIA GERAL: 0.8236 ❌
STATUS: REPROVADO (média < 0.9)
```

#### 📈 Detalhamento v2 (Otimizado - Aprovado)

```
==================================================
Prompt: bug_to_user_story_v2
==================================================

Métricas LangSmith:
  - Helpfulness: 0.94 ✓
  - Correctness: 0.92 ✓

Métricas Customizadas:
  - F1-Score: 0.90 ✓
  - Clarity: 0.94 ✓
  - Precision: 0.95 ✓

📊 MÉDIA GERAL: 0.9278 ✅
STATUS: APROVADO (média >= 0.9)
```

#### 🔗 Links Públicos do LangSmith

- **Prompt v2 no Hub**: https://smith.langchain.com/hub/rafadeamaral/bug_to_user_story_v2
- **Dashboard do Projeto**: https://smith.langchain.com/projects/prompt-optimization-challenge-resolved

### C) Como Executar

#### Pré-requisitos

1. Python 3.9+
2. Conta no LangSmith (https://smith.langchain.com)
3. API Key do Google Gemini (https://aistudio.google.com/app/apikey) ou OpenAI (https://platform.openai.com/api-keys)

#### Instalação

```bash
# 1. Clone o repositório
git clone <seu-repositorio>
cd mba-ia-pull-evaluation-prompt

# 2. Crie e ative o ambiente virtual
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure as variáveis de ambiente
cp .env.example .env
# Edite o .env com suas credenciais:
# - LANGCHAIN_API_KEY
# - GOOGLE_API_KEY ou OPENAI_API_KEY
```

#### Ordem de Execução

```bash
# 1. Executar testes de validação
pytest tests/test_prompts.py -v

# 2. Pull do prompt inicial (v1) do LangSmith Hub
python src/pull_prompts.py

# 3. Push do prompt otimizado (v2) para o LangSmith Hub
python src/push_prompts.py

# 4. Executar avaliação
python src/evaluate.py
```

#### Estrutura de Arquivos Criados

```
mba-ia-pull-evaluation-prompt/
├── prompts/
│   ├── bug_to_user_story_v1.yml  # Prompt baseline (após pull)
│   └── bug_to_user_story_v2.yml  # Prompt otimizado
├── src/
│   ├── pull_prompts.py           # ✅ Implementado
│   ├── push_prompts.py           # ✅ Implementado
└── tests/
    └── test_prompts.py           # ✅ Implementado
```

---

## Dicas Finais

- **Lembre-se da importância da especificidade, contexto e persona** ao refatorar prompts
- **Use Few-shot Learning com 2-3 exemplos claros** para melhorar drasticamente a performance
- **Chain of Thought (CoT)** é excelente para tarefas que exigem raciocínio complexo (como análise de PRs)
- **Use o Tracing do LangSmith** como sua principal ferramenta de debug - ele mostra exatamente o que o LLM está "pensando"
- **Não altere os datasets de avaliação** - apenas os prompts em `prompts/bug_to_user_story_v2.yml`
- **Itere, itere, itere** - é normal precisar de 3-5 iterações para atingir 0.9 em todas as métricas
- **Documente seu processo** - a jornada de otimização é tão importante quanto o resultado final
