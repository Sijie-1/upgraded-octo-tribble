import subprocess
import time
import os
import sys

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

# Iniciar el servidor de Minecraft
print("Iniciando servidor de Minecraft...")
server_process = subprocess.Popen(
    [
        "java",
        "-Xms15G",
        "-Xmx15G",
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
        "/workspaces/upgraded-octo-tribble/server/java-execute.jar"
    ],
    cwd=server_dir,
    stdout=sys.stdout,
    stderr=sys.stderr
)

try:
    server_process.wait()
    playit_process.wait()
except KeyboardInterrupt:
    print("\nDeteniendo procesos...")
    server_process.terminate()
    playit_process.terminate()