from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv


@dataclass
class EntropiaSettings:
    """
    Configurações principais do Entropia Engine.
    """

    max_turns: int = 5
    model_name: str = "gpt-4.1-mini"
    # No futuro: provider, chaves, modo low-resource, etc.


def load_settings(config_path: Optional[Path] = None, max_turns: Optional[int] = None) -> EntropiaSettings:
    """
    Carrega configurações a partir de variáveis de ambiente / arquivo de configuração.
    Nesta primeira versão, apenas respeita o max_turns recebido via CLI e carrega .env.
    """
    load_dotenv()

    settings = EntropiaSettings()
    if max_turns is not None:
        settings.max_turns = max_turns
    return settings

