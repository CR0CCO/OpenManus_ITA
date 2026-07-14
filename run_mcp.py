#!/usr/bin/env python
import argparse
import asyncio
import sys

from app.agent.mcp import MCPAgent
from app.config import config
from app.logger import logger


class MCPRunner:
    """Classe Runner per l'Agente MCP con corretta gestione dei percorsi e configurazione."""

    def __init__(self):
        self.root_path = config.root_path
        self.server_reference = config.mcp_config.server_reference
        self.agent = MCPAgent()

    async def initialize(
        self,
        connection_type: str,
        server_url: str | None = None,
    ) -> None:
        """Inizializza l'agente MCP con la connessione appropriata."""
        logger.info(f"Inizializzazione di MCPAgent con connessione {connection_type}...")

        if connection_type == "stdio":
            await self.agent.initialize(
                connection_type="stdio",
                command=sys.executable,
                args=["-m", self.server_reference],
            )
        else:  # sse
            await self.agent.initialize(connection_type="sse", server_url=server_url)

        logger.info(f"Connesso al server MCP tramite {connection_type}")

    async def run_interactive(self) -> None:
        """Avvia l'agente in modalità interattiva."""
        print("\nModalità Interattiva dell'Agente MCP (digita 'exit' per uscire)\n")
        while True:
            user_input = input("\nInserisci la tua richiesta: ")
            if user_input.lower() in ["exit", "quit", "q"]:
                break
            response = await self.agent.run(user_input)
            print(f"\nAgente: {response}")

    async def run_single_prompt(self, prompt: str) -> None:
        """Avvia l'agente con un singolo prompt."""
        await self.agent.run(prompt)

    async def run_default(self) -> None:
        """Avvia l'agente in modalità predefinita."""
        prompt = input("Inserisci il tuo prompt: ")
        if not prompt.strip():
            logger.warning("Fornito un prompt vuoto.")
            return

        logger.warning("Elaborazione della richiesta in corso...")
        await self.agent.run(prompt)
        logger.info("Elaborazione della richiesta completata.")

    async def cleanup(self) -> None:
        """Rilascia le risorse dell'agente."""
        await self.agent.cleanup()
        logger.info("Sessione terminata")


def parse_args() -> argparse.Namespace:
    """Analizza gli argomenti della riga di comando."""
    parser = argparse.ArgumentParser(description="Avvia l'Agente MCP")
    parser.add_argument(
        "--connection",
        "-c",
        choices=["stdio", "sse"],
        default="stdio",
        help="Tipo di connessione: stdio o sse",
    )
    parser.add_argument(
        "--server-url",
        default="http://127.0.0.1:8000/sse",
        help="URL per la connessione SSE",
    )
    parser.add_argument(
        "--interactive", "-i", action="store_true", help="Avvia in modalità interattiva"
    )
    parser.add_argument("--prompt", "-p", help="Singolo prompt da eseguire per poi uscire")
    return parser.parse_args()


async def run_mcp() -> None:
    """Punto di ingresso principale per l'esecuzione MCP."""
    args = parse_args()
    runner = MCPRunner()

    try:
        await runner.initialize(args.connection, args.server_url)

        if args.prompt:
            await runner.run_single_prompt(args.prompt)
        elif args.interactive:
            await runner.run_interactive()
        else:
            await runner.run_default()

    except KeyboardInterrupt:
        logger.info("Programma interrotto dall'utente")
    except Exception as e:
        logger.error(f"Errore durante l'esecuzione di MCPAgent: {str(e)}", exc_info=True)
        sys.exit(1)
    finally:
        await runner.cleanup()


if __name__ == "__main__":
    asyncio.run(run_mcp())
