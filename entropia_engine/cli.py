import datetime
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.panel import Panel

from .core.orchestrator import run_entropia_session
from .config.settings import EntropiaSettings, load_settings


app = typer.Typer(help="Entropia Engine - debate Criador ↔ Crítico para gerar arquitetura e código.")
console = Console()


@app.command()
def run(
    idea: str = typer.Argument(..., help="Descrição da ideia/sistema a ser projetado."),
    out_dir: Path = typer.Option(
        Path("entropia_out"),
        "--out-dir",
        help="Diretório base onde a saída será gravada.",
    ),
    max_turns: int = typer.Option(
        5,
        "--turnos",
        "--max-turns",
        help="Número máximo de rodadas de debate entre Criador e Crítico.",
    ),
    config_path: Optional[Path] = typer.Option(
        None,
        "--config",
        help="Caminho opcional para um arquivo de configuração do Entropia Engine.",
    ),
) -> None:
    """
    Executa uma sessão do Entropia Engine a partir de uma descrição de ideia.
    """
    console.print(Panel.fit("🚀 [bold cyan]Entropia Engine[/bold cyan] – iniciando sessão", border_style="cyan"))

    settings: EntropiaSettings = load_settings(config_path=config_path, max_turns=max_turns)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    session_dir = out_dir / timestamp
    session_dir.mkdir(parents=True, exist_ok=True)

    console.print(f"[bold]Ideia:[/bold] {idea}")
    console.print(f"[bold]Rodadas máximas:[/bold] {settings.max_turns}")
    console.print(f"[bold]Diretório de saída:[/bold] {session_dir}")

    result = run_entropia_session(
        idea=idea,
        settings=settings,
        output_dir=session_dir,
    )

    console.print()
    console.print(Panel.fit("[bold green]Sessão concluída[/bold green]", border_style="green"))
    console.print(f"[bold]Arquitetura:[/bold] {result.architecture_path}")
    console.print(f"[bold]Código:[/bold] {result.code_dir}")
    console.print(f"[bold]Metadados:[/bold] {result.metadata_path}")


if __name__ == "__main__":
    app()

