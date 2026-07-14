import asyncio
import time

from app.agent.data_analysis import DataAnalysis
from app.agent.manus import Manus
from app.config import config
from app.flow.flow_factory import FlowFactory, FlowType
from app.logger import logger


async def run_flow():
    agents = {
        "manus": Manus(),
    }
    if config.run_flow_config.use_data_analysis_agent:
        agents["data_analysis"] = DataAnalysis()
    try:
        prompt = input("Inserisci il tuo prompt: ")

        if prompt.strip().isspace() or not prompt:
            logger.warning("Fornito un prompt vuoto.")
            return

        flow = FlowFactory.create_flow(
            flow_type=FlowType.PLANNING,
            agents=agents,
        )
        logger.warning("Elaborazione della richiesta in corso...")

        try:
            start_time = time.time()
            result = await asyncio.wait_for(
                flow.execute(prompt),
                timeout=3600,  # Timeout di 60 minuti per l'intera esecuzione
            )
            elapsed_time = time.time() - start_time
            logger.info(f"Richiesta elaborata in {elapsed_time:.2f} secondi")
            logger.info(result)
        except asyncio.TimeoutError:
            logger.error("Tempo di elaborazione della richiesta scaduto dopo 1 ora")
            logger.info(
                "Operazione interrotta per timeout. Riprova con una richiesta più semplice."
            )

    except KeyboardInterrupt:
        logger.info("Operazione annullata dall'utente.")
    except Exception as e:
        logger.error(f"Errore: {str(e)}")


if __name__ == "__main__":
    asyncio.run(run_flow())
