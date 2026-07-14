<p align="center">
  <img src="assets/logo.jpg" width="200"/>
</p>

Italiano | [English](README_en.md) | [中文](README_zh.md) | [한국어](README_ko.md) | [日本語](README_ja.md)

[![GitHub stars](https://img.shields.io/github/stars/FoundationAgents/OpenManus?style=social)](https://github.com/FoundationAgents/OpenManus/stargazers)
&ensp;
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) &ensp;
[![Discord Follow](https://dcbadge.vercel.app/api/server/DYn29wFk9z?style=flat)](https://discord.gg/DYn29wFk9z)
[![Demo](https://img.shields.io/badge/Demo-Hugging%20Face-yellow)](https://huggingface.co/spaces/lyh-917/OpenManusDemo)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15186407.svg)](https://doi.org/10.5281/zenodo.15186407)

# 👋 OpenManus

Manus è incredibile, ma OpenManus può realizzare qualsiasi idea senza bisogno di un *Codice d'Invito* 🛫!

I membri del nostro team [@Xinbin Liang](https://github.com/mannaandpoem) e [@Jinyu Xiang](https://github.com/XiangJinyu) (autori principali), insieme a [@Zhaoyang Yu](https://github.com/MoshiQAQ), [@Jiayi Zhang](https://github.com/didiforgithub) e [@Sirui Hong](https://github.com/stellaHSR), provengono da [@MetaGPT](https://github.com/geekan/MetaGPT). Il prototipo è stato lanciato in sole 3 ore e continuiamo a svilupparlo costantemente!

Si tratta di un'implementazione semplice, quindi accogliamo con favore qualsiasi suggerimento, contributo e feedback!

Goditi il tuo agente personale con OpenManus!

Siamo inoltre entusiasti di presentare [OpenManus-RL](https://github.com/OpenManus/OpenManus-RL), un progetto open-source dedicato a metodi di ottimizzazione (tuning) per agenti LLM basati sul Reinforcement Learning (RL) (come GRPO), sviluppato in collaborazione tra i ricercatori della UIUC e OpenManus.

## Demo del Progetto

<video src="https://private-user-images.githubusercontent.com/61239030/420168772-6dcfd0d2-9142-45d9-b74e-d10aa75073c6.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDEzMTgwNTksIm5iZiI6MTc0MTMxNzc1OSwicGF0aCI6Ii82MTIzOTAzMC80MjAxNjg3NzItNmRjZmQwZDItOTE0Mi00NWQ5LWI3NGUtZDEwYWE3NTA3M2M2Lm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAzMDclMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMzA3VDAzMjIzOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTdiZjFkNjlmYWNjMmEzOTliM2Y3M2VlYjgyNDRlZDJmOWE3NWZhZjE1MzhiZWY4YmQ3NjdkNTYwYTU5ZDA2MzYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.UuHQCgWYkh0OQq9qsUWqGsUbhG3i9jcZDAMeHjLt5T4" data-canonical-src="https://private-user-images.githubusercontent.com/61239030/420168772-6dcfd0d2-9142-45d9-b74e-d10aa75073c6.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDEzMTgwNTksIm5iZiI6MTc0MTMxNzc1OSwicGF0aCI6Ii82MTIzOTAzMC80MjAxNjg3NzItNmRjZmQwZDItOTE0Mi00NWQ5LWI3NGUtZDEwYWE3NTA3M2M2Lm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAzMDclMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMzA3VDAzMjIzOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTdiZjFkNjlmYWNjMmEzOTliM2Y3M2VlYjgyNDRlZDJmOWE3NWZhZjE1MzhiZWY4YmQ3NjdkNTYwYTU5ZDA2MzYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.UuHQCgWYkh0OQq9qsUWqGsUbhG3i9jcZDAMeHjLt5T4" controls="controls" muted="muted" class="d-block rounded-bottom-2 border-top width-fit" style="max-height:640px; min-height: 200px"></video>

## Installazione

Forniamo due metodi di installazione. Il Metodo 2 (tramite uv) è consigliato per un'installazione più rapida e una migliore gestione delle dipendenze.

### Metodo 1: Utilizzando Conda

1. Crea un nuovo ambiente conda:

```bash
conda create -n open_manus python=3.12
conda activate open_manus
```

2. Clona la repository:

```bash
git clone https://github.com/CR0CCO/OpenManus_ITA.git
cd OpenManus_ITA
```

3. Installa le dipendenze:

```bash
pip install -r requirements.txt
```

### Metodo 2: Utilizzando uv (Consigliato)

1. Installa uv (uno strumento ultraveloce per installare e risolvere pacchetti Python):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Clona la repository:

```bash
git clone https://github.com/CR0CCO/OpenManus_ITA.git
cd OpenManus_ITA
```

3. Crea un nuovo ambiente virtuale e attivalo:

```bash
uv venv --python 3.12
source .venv/bin/activate  # Su Unix/macOS
# Oppure su Windows:
# .venv\Scripts\activate
```

4. Installa le dipendenze:

```bash
uv pip install -r requirements.txt
```

### Strumento di Automazione Browser (Opzionale)
```bash
playwright install
```

## Configurazione

OpenManus richiede la configurazione delle API dei modelli LLM utilizzati. Segui questi passaggi per configurare l'ambiente:

1. Crea un file `config.toml` nella directory `config` (puoi copiarlo dall'esempio):

```bash
cp config/config.example.toml config/config.toml
```

2. Modifica `config/config.toml` per inserire le tue chiavi API e personalizzare le impostazioni:

```toml
# Configurazione globale dell'LLM
[llm]
model = "gpt-4o"
base_url = "https://api.openai.com/v1"
api_key = "sk-..."  # Sostituisci con la tua chiave API reale
max_tokens = 4096
temperature = 0.0

# Configurazione opzionale per modelli LLM specifici
[llm.vision]
model = "gpt-4o"
base_url = "https://api.openai.com/v1"
api_key = "sk-..."  # Sostituisci con la tua chiave API reale
```

## Avvio Rapido

Esegui OpenManus con una singola riga di comando:

```bash
python main.py
```

Quindi digita la tua richiesta o idea direttamente nel terminale!

Per la versione con strumenti MCP, puoi eseguire:
```bash
python run_mcp.py
```

Per la versione multi-agente (ancora instabile), puoi eseguire:

```bash
python run_flow.py
```

### Aggiunta Personalizzata di Agenti Multipli

Attualmente, oltre al generico OpenManus Agent, abbiamo integrato il DataAnalysis Agent, adatto per attività di analisi e visualizzazione dei dati. Puoi aggiungere questo agente a `run_flow` nel file `config.toml`.

```toml
# Configurazione opzionale per run-flow
[runflow]
use_data_analysis_agent = true     # Disattivato di default, imposta su true per attivarlo
```
Inoltre, è necessario installare le relative dipendenze per garantire il corretto funzionamento dell'agente: [Guida all'installazione dettagliata](app/tool/chart_visualization/README.md##Installation)

## Come Contribuire

Accogliamo con piacere suggerimenti amichevoli e contributi utili! Basta creare una Issue o inviare una Pull Request.

Oppure contatta @mannaandpoem via 📧email: mannaandpoem@gmail.com

**Nota**: Prima di inviare una pull request, utilizza lo strumento pre-commit per verificare le modifiche. Esegui `pre-commit run --all-files` per avviare i controlli.

## Gruppo Community
Unisciti al nostro gruppo su Feishu e condividi la tua esperienza con altri sviluppatori!

<div align="center" style="display: flex; gap: 20px;">
    <img src="assets/community_group.jpg" alt="OpenManus 交流群" width="300" />
</div>

## Cronologia Star

[![Star History Chart](https://api.star-history.com/svg?repos=FoundationAgents/OpenManus&type=Date)](https://star-history.com/#FoundationAgents/OpenManus&Date)

## Sponsor
Si ringrazia [PPIO](https://ppinfra.com/user/register?invited_by=OCPKCN&utm_source=github_openmanus&utm_medium=github_readme&utm_campaign=link) per il supporto alle risorse di calcolo.
> PPIO: La soluzione cloud GPU e MaaS più economica e facile da integrare.

## Ringraziamenti

Grazie a [anthropic-computer-use](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo), [browser-use](https://github.com/browser-use/browser-use) e [crawl4ai](https://github.com/unclecode/crawl4ai) per aver fornito il supporto di base a questo progetto!

Inoltre, siamo grati a [AAAJ](https://github.com/metauto-ai/agent-as-a-judge), [MetaGPT](https://github.com/geekan/MetaGPT), [OpenHands](https://github.com/All-Hands-AI/OpenHands) e [SWE-agent](https://github.com/SWE-agent/SWE-agent).

Ringraziamo anche stepfun (阶跃星辰) per il supporto al nostro spazio demo su Hugging Face.

OpenManus è costruito dai contributori di MetaGPT. Un ringraziamento enorme a questa community di agenti!

## Citazione
```bibtex
@misc{openmanus2025,
  author = {Xinbin Liang and Jinyu Xiang and Zhaoyang Yu and Jiayi Zhang and Sirui Hong and Sheng Fan and Xiao Tang and Bang Liu and Yuyu Luo and Chenglin Wu},
  title = {OpenManus: An open-source framework for building general AI agents},
  year = {2025},
  publisher = {Zenodo},
  doi = {10.5281/zenodo.15186407},
  url = {https://doi.org/10.5281/zenodo.15186407},
}
```
