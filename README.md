# Raspberry Screen Streamer

![Logo](logo.png)

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
