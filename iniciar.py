import subprocess
import time
import os

# Directorios
server_dir = "/workspaces/upgraded-octo-tribble/server"
playit_dir = "/workspaces/upgraded-octo-tribble/playit"

# Iniciar playit
print("Iniciando Playit...")
playit_process = subprocess.Popen(
    [os.path.join(playit_dir, "playit")],
    cwd=playit_dir,
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)

time.sleep(5)

# Iniciar el sv de mc
print("Iniciando servidor de Minecraft...")
server_process = subprocess.Popen(
    [
        "java",
        "-Xms15G",
        "-Xmx15G",
        "-jar",
        "/workspaces/upgraded-octo-tribble/server/java-execute.jar"
    ],
    cwd=server_dir
)

try:
    server_process.wait()
    playit_process.wait()
except KeyboardInterrupt:
    print("\nDeteniendo procesos...")
    server_process.terminate()
    playit_process.terminate()
