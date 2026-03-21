import subprocess
import time
import os
import sys

# Resolución dinámica de directorios
base_dir = os.path.dirname(os.path.abspath(__file__))
server_dir = os.path.join(base_dir, "server")
playit_dir = os.path.join(base_dir, "playit")
jar_path = os.path.join(server_dir, "java-execute.jar")
playit_executable = os.path.join(playit_dir, "playit")

# Iniciar el túnel de Playit
print("Iniciando el túnel de Playit...")
playit_process = subprocess.Popen(
    [playit_executable],
    cwd=playit_dir,
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)
time.sleep(5)

# Iniciar el servidor de Minecraft con parámetros Aikar optimizados y RAM segura
print("Iniciando el servidor de Minecraft...")
server_process = subprocess.Popen(
    [
        "java",
        "-Xms12G",
        "-Xmx12G",
        "-XX:+UseG1GC",
        "-XX:+ParallelRefProcEnabled",
        "-XX:MaxGCPauseMillis=200",
        "-XX:+UnlockExperimentalVMOptions",
        "-XX:+DisableExplicitGC",
        "-XX:G1NewSizePercent=40",
        "-XX:G1MaxNewSizePercent=50",
        "-XX:G1HeapRegionSize=16M",
        "-XX:G1ReservePercent=15",
        "-XX:G1HeapWastePercent=5",
        "-XX:G1MixedGCCountTarget=4",
        "-XX:InitiatingHeapOccupancyPercent=20",
        "-XX:G1MixedGCLiveThresholdPercent=90",
        "-XX:G1RSetUpdatingPauseTimePercent=5",
        "-XX:SurvivorRatio=32",
        "-XX:+PerfDisableSharedMem",
        "-XX:MaxTenuringThreshold=1",
        "-Dusing.aikars.flags=https://mcflags.emc.gs",
        "-Daikars.new.flags=true",
        "-jar",
        jar_path
    ],
    cwd=server_dir,
    stdout=sys.stdout,
    stderr=sys.stderr
)

# Control de cierre de procesos
try:
    server_process.wait()
    playit_process.wait()
except KeyboardInterrupt:
    print("\nInterrupción detectada; deteniendo los procesos en curso...")
    server_process.terminate()
    playit_process.terminate()
