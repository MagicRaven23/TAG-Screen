# Raspberry Screen Streamer

<img src="tag-logo.png" width="200" />

Dies ist ein einfaches Tkinter-Interface zur Steuerung eines `ffmpeg`-basierten Screen-Streamers, der den Bildschirm an ein Raspberry Pi-Gerät sendet. Das Programm erkennt automatisch das Betriebssystem und passt die `ffmpeg`-Befehle entsprechend an.

## Funktionen
- Starten und Stoppen des Bildschirm-Streamings.
- Dynamische Anpassung der Framerate auf Windows.
- Unterstützung für Windows und Linux.
- IP-Adresse des Raspberry Pi konfigurierbar.

## Installation

### 1. Voraussetzungen

- Python 3.x muss installiert sein (Windows und Linux).
- ffmpeg muss auf dem System installiert sein und im Pfad verfügbar sein.
- Installiere die notwendigen Python-Pakete:
  ```bash
  pip install tkinter

<details>

<summary>Linux</summary>

## Installation

### 1. Clone Repository
```bash
git clone https://github.com/MagicRaven23/TAG-Screen
cd TAG-Screen
```
### 2. Install ffmpeg
```bash 
sudo apt install ffmpeg
```
### 3. Start Programm
```bash
python3 Raspberry-screen.py
```
### 4. Executable File
* #### Install pyinstaller
  ```bash
  pip install pyinstaller
  ```
* #### Create Executable File
  ```bash
  pyinstaller --onefile --windowed --icon=logo.ico code/Screen-Streamer.py
  ```
* #### The executable file is located in the `dist` folder
</details>

<details>

<summary>Windows</summary>

## Installation

### 1. Clone Repository
```bash
git clone https://github.com/MagicRaven23/TAG-Screen
cd TAG-Screen
```
### 2. Start Programm
```bash
python3 Raspberry-screen.py
```
### 3. Executable File
* #### Install pyinstaller
  ```bash
  pip install pyinstaller
  ```
* #### Create Executable File
  ```bash
  pyinstaller --onefile --windowed --icon=logo.ico code/Screen-Streamer.py
  ```
* #### The executable file is located in the `dist` folder
</details>

> [!NOTE]
> Install `ffmpeg` on Windows </br>
> https://cran.r-project.org/web/packages/act/vignettes/install_ffmpeg.html
