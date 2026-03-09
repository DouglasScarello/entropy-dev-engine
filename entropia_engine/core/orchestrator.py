from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from ..config.settings import EntropiaSettings


@dataclass
class EntropiaResult:
    architecture_path: Path
    code_dir: Path
    metadata_path: Path


def run_entropia_session(idea: str, settings: EntropiaSettings, output_dir: Path) -> EntropiaResult:
    """
    Orquestra o loop Criador ↔ Crítico (e futuros agentes) e grava os artefatos em disco.

    Nesta primeira versão, não chama AutoGen de verdade; apenas grava stubs que
    já respeitam o formato final (útil para testar o CLI e a integração).
    """
    architecture_path = output_dir / "architecture.md"
    code_dir = output_dir / "code"
    metadata_path = output_dir / "metadata.json"

    code_dir.mkdir(parents=True, exist_ok=True)

    # Stubs iniciais – serão substituídos pela integração real com AutoGen.
    architecture_path.write_text(
        "# Arquitetura (stub)\n\n"
        "Esta é uma versão inicial apenas para validar o fluxo do Entropia Engine.\n\n"
        f"## Ideia original\n\n{idea}\n"
    )

    (code_dir / "main.py").write_text(
        '"""Stub gerado pelo Entropia Engine.\n\n'
        "Substitua este conteúdo pela saída real do loop Criador ↔ Crítico.\n"
        '"""\n\n'
        "def main() -> None:\n"
        f'    print({idea!r})\n'
    )

    metadata_path.write_text(
        "{\n"
        f'  "idea": {idea!r},\n'
        f'  "max_turns": {settings.max_turns},\n'
        '  "status": "stub",\n'
        '  "notes": "Integração com AutoGen ainda não implementada."\n'
        "}\n"
    )

    return EntropiaResult(
        architecture_path=architecture_path,
        code_dir=code_dir,
        metadata_path=metadata_path,
    )

