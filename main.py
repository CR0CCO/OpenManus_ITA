import argparse
import asyncio

from app.agent.manus import Manus
from app.logger import logger


async def main():
    # Analizza gli argomenti della riga di comando
    parser = argparse.ArgumentParser(description="Avvia l'agente Manus con un prompt")
    parser.add_argument(
        "--prompt", type=str, required=False, help="Prompt di input per l'agente"
    )
    args = parser.parse_args()

    # Crea e inizializza l'agente Manus
    agent = await Manus.create()
    try:
        # Usa il prompt da riga di comando se fornito, altrimenti chiedi l'input
        prompt = args.prompt if args.prompt else input("Inserisci il tuo prompt: ")
        if not prompt.strip():
            logger.warning("Fornito un prompt vuoto.")
            return

        logger.warning("Elaborazione della richiesta in corso...")
        await agent.run(prompt)
        logger.info("Elaborazione della richiesta completata.")
    except KeyboardInterrupt:
        logger.warning("Operazione interrotta.")
    finally:
        # Assicura il rilascio delle risorse dell'agente prima di uscire
        await agent.cleanup()


if __name__ == "__main__":
    asyncio.run(main())
