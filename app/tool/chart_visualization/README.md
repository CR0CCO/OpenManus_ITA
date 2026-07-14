# Strumento di Visualizzazione dei Grafici

Lo strumento di visualizzazione dei grafici genera codice di elaborazione dati tramite Python e infine richiama [@visactor/vmind](https://github.com/VisActor/VMind) per ottenere le specifiche del grafico. Il rendering del grafico è implementato utilizzando [@visactor/vchart](https://github.com/VisActor/VChart).

## Installazione (Mac / Linux)

1. Installa node >= 18

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
# Attiva nvm, ad esempio in Bash
source ~/.bashrc
# Quindi installa l'ultima versione stabile di Node
nvm install node
# Attiva l'uso, ad esempio se l'ultima versione stabile è la 22, usa 22
nvm use 22
```

2. Installa le dipendenze

```bash
# Naviga nella posizione appropriata all'interno della repository corrente
cd app/tool/chart_visualization
npm install
```

## Installazione (Windows)
1. Installa nvm-windows

    Scarica l'ultima versione di `nvm-setup.exe` dalla [pagina ufficiale di GitHub](https://github.com/coreybutler/nvm-windows?tab=readme-ov-file#readme) e installala.

2. Usa nvm per installare node

```powershell
# Installa l'ultima versione stabile di Node
nvm install node
# Attiva l'uso, ad esempio se l'ultima versione stabile è la 22, usa 22
nvm use 22
```

3. Installa le dipendenze

```bash
# Naviga nella posizione appropriata all'interno della repository corrente
cd app/tool/chart_visualization
npm install
```

## Strumenti
### python_execute

Esegue le parti necessarie dell'analisi dei dati (esclusa la visualizzazione) tramite codice Python, inclusi l'elaborazione dei dati, il riepilogo dei dati, la generazione di report e codice generico di script Python.

#### Input
```typescript
{
  // Tipo di codice: elaborazione dati / report dati / altre attività generiche
  code_type: "process" | "report" | "others"
  // Codice finale da eseguire
  code: string;
}
```

#### Output
Risultati dell'esecuzione di Python, compreso il salvataggio dei file intermedi e la stampa dei risultati dell'output.

### visualization_preparation

Uno strumento preliminare per la visualizzazione dei dati con due scopi:

#### Dati -> Grafico
Utilizzato per estrarre i dati necessari per l'analisi (.csv) e la corrispondente descrizione di visualizzazione dai dati stessi, producendo infine un file di configurazione JSON.

#### Grafico + Insight -> Grafico
Seleziona grafici esistenti e i relativi approfondimenti (insight), sceglie quali approfondimenti aggiungere al grafico sotto forma di annotazioni di dati e infine genera un file di configurazione JSON.

#### Input
```typescript
{
  // Tipo di codice: visualizzazione dati o aggiunta di annotazioni insight
  code_type: "visualization" | "insight"
  // Codice Python utilizzato per produrre il file JSON finale
  code: string;
}
```

#### Output
Un file di configurazione per la visualizzazione dei dati, utilizzato dallo strumento `data_visualization`.

## data_visualization

Genera visualizzazioni di dati specifiche in base al contenuto di `visualization_preparation`.

### Input
```typescript
{
  // Percorso del file di configurazione
  json_path: string;
  // Scopo attuale, visualizzazione dei dati o aggiunta di annotazioni insight
  tool_type: "visualization" | "insight";
  // Prodotto finale: png o html; html supporta il rendering e l'interazione vchart
  output_type: 'png' | 'html'
  // Lingua, attualmente supporta cinese e inglese
  language: "zh" | "en"
}
```

## Configurazione di VMind

### LLM

VMind richiede la chiamata a un LLM per la generazione intelligente dei grafici. Di default, utilizza la configurazione `config.llm["default"]`.

### Impostazioni di Generazione

Le configurazioni principali includono le dimensioni del grafico, il tema e il metodo di generazione:
### Metodo di Generazione
Predefinito: png. Attualmente supporta la selezione automatica di `output_type` da parte dell'LLM in base al contesto.

### Dimensioni
Le dimensioni predefinite non sono specificate. Per l'output HTML, i grafici riempiono l'intera pagina per impostazione predefinita. Per l'output PNG, il valore predefinito è `1000*1000`.

### Tema
Tema predefinito: `'light'`. VChart supporta più temi. Vedi [Temi](https://www.visactor.io/vchart/guide/tutorial_docs/Theme/Theme_Extension).

## Test

Attualmente, sono impostate tre attività di diversi livelli di difficoltà per il test.

### Attività di Generazione di Grafici Semplici

Fornisce dati e requisiti specifici per la generazione dei grafici, esegue il comando di test:
```bash
python -m app.tool.chart_visualization.test.chart_demo
```
I risultati dovrebbero trovarsi sotto `workspace\visualization`, coinvolgendo 9 diversi risultati di grafici.

### Attività di Report Dati Semplice

Fornisce requisiti semplici di analisi dei dati grezzi, che richiedono una semplice elaborazione dei dati, esegue il comando:
```bash
python -m app.tool.chart_visualization.test.report_demo
```
Anche questi risultati si trovano sotto `workspace\visualization`.
