# Entropia Engine

Entropia Engine é um motor de **engenharia automática** que transforma requisitos em texto em **arquitetura de software** e **código inicial**, usando um loop de agentes de IA:

- **Criador**: propõe arquitetura e código.
- **Crítico**: destrói, aponta falhas e melhorias.
- (Futuro) **Juiz / Testador**: valida, executa testes e decide pela versão final.

O fluxo básico é:

```bash
entropia run "Quero um app de chat P2P criptografado"
```

O sistema cria um debate multi‑agente, converge para uma solução e salva:

- `architecture.md` – arquitetura final.
- `code/` – arquivos de código sugeridos.
- `metadata.json` – decisões, trade‑offs, modelos usados.

## Instalação (desenvolvimento)

Requisitos:

- Python 3.11+
- Poetry instalado

No diretório do projeto:

```bash
poetry install
poetry run entropia --help
```

## Uso rápido

```bash
entropia run "Quero um serviço de crawling distribuído com fila e workers"
```

Por padrão, a saída será gravada em um diretório como:

- `entropia_out/2026-03-09T12-00-00/`

## Estrutura planejada

- `entropia_engine/`
  - `cli.py` – interface de linha de comando (`entropia run`).
  - `core/orchestrator.py` – loop Criador ↔ Crítico ↔ (Juiz/Testador).
  - `core/state_manager.py` – gestão de estado e contexto (resumos, `state.json`).
  - `core/model_router.py` – escolha de modelos (cloud vs local, forte vs fraco).
  - `agents/creator.py` – agente Criador.
  - `agents/critic_security.py` – crítico focado em segurança.
  - `agents/critic_architecture.py` – crítico focado em arquitetura/performance.
  - `agents/tester.py` – executa testes, linters, compile gate.
  - `agents/judge.py` – sintetiza e aprova a versão final.
  - `execution/sandbox.py` – sandbox para executar código sugerido.
  - `execution/code_runner.py` – roda testes/linters (pytest, mypy, ruff, etc.).
  - `output/writer.py` – grava arquivos (`architecture.md`, `code/`, `metadata.json`).
  - `config/settings.py` – leitura de `.env`, `config.toml`, flags do CLI.

Nas primeiras versões, alguns módulos podem ser stubs, evoluindo à medida que os fluxos ficarem mais sofisticados.
