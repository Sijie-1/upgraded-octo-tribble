Desactualizado

# Servidor de Minecraft en GitHub Codespaces con Playit.gg

## Descripción
Este documento detalla el procedimiento exacto para configurar un servidor de Minecraft funcional dentro de GitHub Codespaces; además, utiliza Playit.gg para establecer el tunneling de red. Por lo tanto, esta arquitectura resulta ideal para entornos de desarrollo y pruebas cerradas.

## Advertencia de Riesgo y Términos de Servicio
El uso de GitHub Codespaces para alojar servidores de juegos de forma continua infringe los Términos de Servicio de la plataforma. GitHub asigna estos recursos computacionales de manera exclusiva para el desarrollo y la compilación de código; por consiguiente, los sistemas automatizados de telemetría suspenderán las cuentas que mantengan procesos persistentes de alto consumo. Este documento posee un propósito estrictamente educativo. Debes restringir la ejecución del servidor a periodos breves de desarrollo o configuración y destruir el entorno virtual inmediatamente después de finalizar tu sesión.

## Tabla de Contenidos
1. [Prerrequisitos](#1-prerrequisitos)
2. [Configuración Inicial del Repositorio](#2-configuración-inicial-del-repositorio)
3. [Creación y Configuración del Codespace](#3-creación-y-configuración-del-codespace)
4. [Instalación y Configuración de Playit.gg](#4-instalación-y-configuración-de-playitgg)
5. [Configuración del Servidor de Minecraft](#5-configuración-del-servidor-de-minecraft)
6. [Puesta en Marcha y Conexión](#6-puesta-en-marcha-y-conexión)
7. [Operación y Mantenimiento](#7-operación-y-mantenimiento)
8. [Preguntas Frecuentes (FAQ)](#8-preguntas-frecuentes-faq)

---

## 1. Prerrequisitos
Para ejecutar este despliegue, requieres los siguientes elementos:
1. Cuenta activa en GitHub.
2. Cuenta registrada en Playit.gg.
3. Archivo `.jar` del servidor de Minecraft seleccionado (Fabric, Forge, Vanilla u otra variante).

## 2. Configuración Inicial del Repositorio
1. Crea un nuevo repositorio en GitHub. No añadas los archivos `README.md`, `.gitignore` ni licencias en esta fase.
2. Sube los siguientes archivos a la raíz del repositorio:
   - `java-execute.jar` (Archivo de tu servidor de Minecraft, previamente renombrado).
   - `iniciar.py`
   - `backup.sh`

## 3. Creación y Configuración del Codespace
1. Navega a la pestaña **Codespaces** dentro de tu repositorio en GitHub.
2. Haz clic en **New codespace**; luego, selecciona la máquina virtual con 4 núcleos y 16 GB de RAM.
3. Espera a que el entorno se inicie de forma completa. Una vez abierto, ejecuta las siguientes acciones:
   - Crea dos directorios independientes: `server` y `playit`.
   - Instala la extensión de Python desde el marketplace integrado de VS Code.
   - Mueve el archivo `java-execute.jar` al interior de la carpeta `server`.

## 4. Instalación y Configuración de Playit.gg
1. Abre una nueva terminal en la interfaz del codespace.
2. Navega al directorio correspondiente y descarga el agente oficial mediante los siguientes comandos:

```bash
cd playit
curl -L -o playit [https://github.com/playit-cloud/playit-agent/releases/latest/download/playit-linux-amd64](https://github.com/playit-cloud/playit-agent/releases/latest/download/playit-linux-amd64)
chmod +x playit
```

## 5. Configuración del Servidor de Minecraft
1. Abre y edita el script `backup.sh`. Actualiza la ruta del directorio base a `cd /workspaces/NOMBRE-DE-TU-REPO`; además, modifica el mensaje del commit según tus convenciones de control de versiones.
2. Abre y edita el script `iniciar.py`. Verifica que las variables de ruta `server_dir` y `playit_dir` apunten directamente a tu repositorio.
3. Confirma la sintaxis de ejecución del archivo `.jar` en el comando de Java dentro del mismo script `iniciar.py`. Ajusta los parámetros de asignación de memoria RAM (`-Xmx`, `-Xms`) en función de los recursos físicos de tu codespace.

## 6. Puesta en Marcha y Conexión
1. Ejecuta el servidor por primera vez en la terminal mediante el comando `cd server && java -jar java-execute.jar`. Interrumpe el proceso con `Ctrl+C`; después, abre el archivo `server/eula.txt` y cambia la línea `eula=false` a `eula=true` para aceptar el acuerdo de licencia.
2. Abre una nueva sesión de terminal e inicia el túnel de red mediante el comando `cd playit && ./playit`. El sistema generará una URL de vinculación; por lo tanto, accede a ese enlace para conectar el agente con tu cuenta web.
3. Añade un nuevo túnel desde la interfaz web de Playit.gg y define el "Tunnel Type" como **Minecraft Java**. Copia la dirección IP y el puerto asignados dinámicamente para conectar tu cliente de juego.

## 7. Operación y Mantenimiento
1. **Ejecución automatizada:** Ejecuta el script principal en la terminal (`python iniciar.py`) para arrancar los servicios del servidor y el túnel simultáneamente.
2. **Interrupción del servicio:** Aplica la combinación `Ctrl+C` en la terminal activa para detener los procesos en ejecución.
3. **Respaldos de seguridad:** Ejecuta el script `./backup.sh` para empaquetar y subir los datos persistentes al repositorio remoto.

## 8. Preguntas Frecuentes (FAQ)
1. **¿Cómo permito el acceso a jugadores sin cuentas Premium?** Abre el archivo `server.properties`; busca la variable `online-mode=true` y modifícala a `online-mode=false`.
2. **¿Cómo modifico la dificultad del mundo?** Edita el archivo `server.properties` y asigna el parámetro deseado a la variable `difficulty=` (opciones admitidas: peaceful, easy, normal, hard).
3. **¿Cómo personalizo el mensaje de bienvenida (MOTD)?** Localiza la variable `motd=` en el archivo `server.properties` y reemplaza el valor predeterminado por el texto descriptivo de tu servidor.
4. **¿Cuál es el procedimiento para instalar mods o datapacks?** Sube los archivos en formato `.jar` o `.zip` directamente a las subcarpetas correspondientes (como `mods` o `world/datapacks`) dentro del directorio `server` de tu codespace.

## 9. Resolución de Problemas
Ejecuta la siguiente secuencia de diagnóstico para corregir fallos críticos durante el despliegue del sistema operativo virtual.

1. Audita la configuración de la máquina virtual si el entorno falla durante la fase de inicialización. Revisa la documentación oficial sobre la [creación de un Codespace](https://docs.github.com/es/codespaces/developing-in-a-codespace/creating-a-codespace-for-a-repository) para validar los prerrequisitos del repositorio.
2. Reduce la asignación de memoria RAM en el script `iniciar.py` si el servidor colapsa de forma abrupta. El núcleo de Linux aniquilará el proceso de Java forzosamente porque el contenedor virtual carece de particiones de intercambio (swap).
3. Detiene y reinicia el agente de túneles si Playit.gg omite la impresión de la URL de vinculación. Asegura la ejecución del proceso en una instancia de terminal independiente para evitar la interrupción de los hilos de red principales.
