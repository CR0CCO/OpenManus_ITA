@echo off
:: Attiva la codifica UTF-8 per supportare le lettere accentate nel terminale
chcp 65001 >nul
title OpenManus ITA - Gestione ed Avvio

echo =======================================================================
echo               OpenManus ITA - Installazione e Avvio
echo =======================================================================
echo.

:: 1. Verifica la presenza di Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERRORE] Python non e' installato o non e' presente nel PATH di sistema.
    echo Per favore, installa Python (consigliato 3.12) da python.org
    echo e assicurati di spuntare l'opzione "Add Python to PATH" durante l'installazione.
    echo.
    pause
    exit /b
)

:: 2. Creazione dell'ambiente virtuale se non esiste
if not exist ".venv" (
    echo [.venv] Creazione dell'ambiente virtuale Python in corso...
    python -m venv .venv
    if %errorlevel% neq 0 (
        echo [ERRORE] Impossibile creare l'ambiente virtuale.
        pause
        exit /b
    )
    echo [.venv] Ambiente virtuale creato con successo.
    echo.
)

:: 3. Attivazione dell'ambiente virtuale
call .venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo [ERRORE] Impossibile attivare l'ambiente virtuale.
    pause
    exit /b
)

:: 4. Installazione o aggiornamento delle dipendenze
echo [Dipendenze] Verifica e installazione delle librerie in corso...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo [ERRORE] Errore durante l'installazione delle dipendenze di requirements.txt.
    pause
    exit /b
)

:: 5. Installazione dei browser Playwright
echo [Playwright] Verifica e installazione dei browser in corso...
playwright install
if %errorlevel% neq 0 (
    echo [ERRORE] Impossibile installare i browser di Playwright.
    pause
    exit /b
)

:: 6. Verifica del file di configurazione config.toml
if not exist "config\config.toml" (
    echo [Configurazione] Creazione del file config.toml in corso...
    if exist "config\config.example.toml" (
        copy "config\config.example.toml" "config\config.toml" >nul
        echo [!] config.toml creato. ATTENZIONE: Devi inserire le tue chiavi API nel file:
        echo     %~dp0config\config.toml
        echo     prima di poter avviare OpenManus correttamente.
        echo.
    ) else (
        echo [ERRORE] File config.example.toml non trovato in config/
    )
)

:: 7. Creazione del collegamento sul Desktop tramite PowerShell
echo [Desktop] Creazione/aggiornamento del collegamento sul Desktop in corso...
powershell -NoProfile -Command "$W = New-Object -ComObject WScript.Shell; $S = $W.CreateShortcut([System.IO.Path]::Combine([System.Environment]::GetFolderPath('Desktop'), 'OpenManus_ITA.lnk')); $S.TargetPath = '%~dp0avvia.bat'; $S.WorkingDirectory = '%~dp0'; $S.Description = 'Avvia OpenManus ITA'; $S.Save()"

echo [Ok] Installazione e configurazione completate con successo!
echo.

:menu
echo =======================================================================
echo                              MENU DI AVVIO
echo =======================================================================
echo  1) Avvia OpenManus (Standard)
echo  2) Avvia OpenManus (MCP - Model Context Protocol)
echo  3) Avvia OpenManus (Multi-Agente - Sperimentale)
echo  4) Apri la cartella di configurazione (per inserire le chiavi API)
echo  5) Esci
echo =======================================================================
echo.
set /p scelta="Seleziona un'opzione (1-5): "

if "%scelta%"=="1" (
    echo Avvio di OpenManus Standard...
    python main.py
    pause
    goto menu
)
if "%scelta%"=="2" (
    echo Avvio di OpenManus con supporto MCP...
    python run_mcp.py
    pause
    goto menu
)
if "%scelta%"=="3" (
    echo Avvio di OpenManus Multi-Agente...
    python run_flow.py
    pause
    goto menu
)
if "%scelta%"=="4" (
    echo Apertura della cartella config...
    explorer "config"
    goto menu
)
if "%scelta%"=="5" (
    exit /b
)

echo Opzione non valida, riprova.
echo.
goto menu
