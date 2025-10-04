🧭 TUTORIAL COMPLETO: Servidor de Minecraft en GitHub Codespaces con Playit.gg

DESCRIPCIÓN:
Este tutorial guía paso a paso para configurar un servidor de Minecraft funcional en GitHub Codespaces, utilizando Playit.gg para el tunneling. Es ideal para entornos de desarrollo y pruebas.

TABLA DE CONTENIDOS:
1.  Prerrequisitos
2.  Configuración Inicial del Repositorio
3.  Creación y Configuración del Codespace
4.  Instalación y Configuración de Playit.gg
5.  Configuración del Servidor de Minecraft
6.  Puesta en Marcha y Conexión
7.  Operación y Mantenimiento
8.  Preguntas Frecuentes (FAQ)

1. PRERREQUISOS
- Cuenta en GitHub.
- Cuenta en Playit.gg :cite[7].
- Archivo .jar del servidor (Fabric, Forge, Vanilla, etc.).

2. CONFIGURACIÓN INICIAL DEL REPOSITORIO
- Crear un nuevo repositorio en GitHub. No añadir README.md, .gitignore o licencia inicialmente.
- Subir los siguientes archivos al repositorio:
    * `java-execute.jar` (Tu servidor de Minecraft renombrado).
    * `iniciar.py`
    * `backup.sh`

3. CREACIÓN Y CONFIGURACIÓN DEL CODESPACE
- En GitHub, ve a la pestaña "Codespaces" de tu repositorio.
- Haz clic en "New codespace". Selecciona:
    * Máquina: 4 cores, 16 GB de RAM.
- Una vez abierto, en el codespace:
    * Crear dos carpetas: `server` y `playit`.
    * Instalar la extensión de Python desde el marketplace de VS Code.
    * Mover `java-execute.jar` a la carpeta `server`.

4. INSTALACIÓN Y CONFIGURACIÓN DE PLAYIT.GG
- Abrir una terminal en el codespace.
- Navegar a la carpeta `playit` e instalar el agente :cite[10]:
    cd playit
    curl -L -o playit https://github.com/playit-cloud/playit-agent/releases/latest/download/playit-linux-amd64
    chmod +x playit

5. CONFIGURACIÓN DEL SERVIDOR DE MINECRAFT
- Editar `backup.sh`:
    * Actualizar la ruta del repositorio: `cd /workspaces/NOMBRE-DE-TU-REPO`
    * Personalizar el mensaje de commit si se desea.
- Editar `iniciar.py`:
    * Asegurar que las rutas `server_dir` y `playit_dir` apunten a tu repositorio.
    * Verificar que la ruta al .jar en el comando de Java sea correcta.
    * Ajustar los parámetros de RAM (`-Xmx`, `-Xms`) según los recursos de tu codespace.

6. PUESTA EN MARCHA Y CONEXIÓN
- Aceptar el EULA:
    * Ejecutar en terminal: `cd server && java -jar java-execute.jar`
    * Tras la primera ejecución, editar `server/eula.txt` y cambiar `eula=false` por `eula=true`.
- Iniciar Playit.gg y configurar túneles:
    * En una terminal: `cd playit && ./playit`
    * Se mostrará un enlace; abrirlo y configurar un nuevo túnel.
    * En "Tunnel Type", seleccionar "Minecraft Java".
- Conectar al servidor:
    * Usar la IP y puerto que aparecen en el panel de Playit.gg.

7. OPERACIÓN Y MANTENIMIENTO
- Ejecución automática:
    * Para iniciar todo: ejecutar el script `iniciar.py`.
    * Para detener: `Ctrl+C` en la terminal.
- Copias de seguridad:
    * Ejecutar: `./backup.sh`

8. PREGUNTAS FRECUENTES (FAQ)
- ¿Cómo permitir jugadores sin Minecraft Premium?
    * En `server.properties`, cambiar `online-mode=true` a `online-mode=false`.
- ¿Cómo cambiar la dificultad?
    * En `server.properties`, modificar `difficulty=...` (peaceful, easy, normal, hard).
- ¿Cómo cambiar la descripción (MOTD) del servidor?
    * En `server.properties`, editar la línea `motd=Tu mensaje aquí`.
- ¿Cómo añadir mods, datapacks, etc.?
    * Subir los archivos directamente a la carpeta correspondiente dentro de `server` en el codespace.

¡LISTO! Tu servidor de Minecraft ya está funcionando en GitHub Codespaces.