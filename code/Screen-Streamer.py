import tkinter as tk
import subprocess

# Hauptfenster erstellen
root = tk.Tk()
root.title("FFmpeg Screen Streamer")

# Globale Variable für den ffmpeg-Prozess
ffmpeg_process = None

# Funktion zum Starten von ffmpeg
def start_stream():
    global ffmpeg_process
    if ffmpeg_process is None:
        # Starten des ffmpeg-Prozesses
        ffmpeg_process = subprocess.Popen([
            "ffmpeg", "-f", "gdigrab", "-framerate", "30", "-s", "1920x1080", "-i", "desktop", 
            "-c:v", "libx264", "-b:v", "6M", "-preset", "ultrafast", "-tune", "zerolatency", "-f", "mpegts", "udp://127.0.0.1:12345"
        ])
        status_label.config(text="Streaming läuft...")

# Funktion zum Stoppen von ffmpeg
def stop_stream():
    global ffmpeg_process
    if ffmpeg_process is not None:
        # Beende den ffmpeg-Prozess
        ffmpeg_process.terminate()
        ffmpeg_process = None
        status_label.config(text="Streaming gestoppt")

# Buttons für Start und Stop
start_button = tk.Button(root, text="Start Stream", command=start_stream)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop Stream", command=stop_stream)
stop_button.pack(pady=10)

# Statuslabel für Rückmeldung
status_label = tk.Label(root, text="Bereit")
status_label.pack(pady=10)

# Tkinter Hauptloop starten
root.mainloop()
import tkinter as tk
import subprocess

# Hauptfenster erstellen
root = tk.Tk()
root.title("FFmpeg Screen Streamer")

# Globale Variable für den ffmpeg-Prozess
ffmpeg_process = None

# Funktion zum Starten von ffmpeg
def start_stream():
    global ffmpeg_process
    if ffmpeg_process is None:
        # Starten des ffmpeg-Prozesses
        ffmpeg_process = subprocess.Popen([
            "ffmpeg", "-f", "gdigrab", "-framerate", "30", "-s", "1440x900", "-i", "desktop", 
            "-c:v", "libx264", "-preset", "ultrafast", "-tune", "zerolatency", "-f", "mpegts", "udp://127.0.0.1:12345"
        ])
        status_label.config(text="Streaming läuft...")

# Funktion zum Stoppen von ffmpeg
def stop_stream():
    global ffmpeg_process
    if ffmpeg_process is not None:
        # Beende den ffmpeg-Prozess
        ffmpeg_process.terminate()
        ffmpeg_process = None
        status_label.config(text="Streaming gestoppt")

# Buttons für Start und Stop
start_button = tk.Button(root, text="Start Stream", command=start_stream)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop Stream", command=stop_stream)
stop_button.pack(pady=10)

# Statuslabel für Rückmeldung
status_label = tk.Label(root, text="Bereit")
status_label.pack(pady=10)

# Tkinter Hauptloop starten
root.mainloop()
