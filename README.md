🧭 Tutorial Completo: Cómo montar tu servidor de Minecraft en GitHub Codespaces con Playit.gg

Bueno, este es un tutorial pensado para quienes quieren hacer lo mismo que se muestra en este repositorio, pero aplicándolo a sus propios repositorios.

0. Preparación previa

Antes que nada, necesitas tener el .jar de tu servidor. Este archivo depende completamente de ti, ya que existen diferentes tipos de servidores de Minecraft, como por ejemplo:

Arclight

Fabric

Forge

Vanilla

En este tutorial, yo usaré Fabric.
Para obtenerlo, dirígete a su página web oficial y descarga el fabric-server.jar de la versión que desees (por ejemplo, 1.20.1).
Luego, el archivo que descargues lo vas a renombrar como java-execute.jar, que es el nombre recomendado para este tutorial.

🟡 Importante: También debes tener una cuenta activa en Playit.gg
, ya que la usaremos más adelante.

1. Crear el repositorio en GitHub

En GitHub, crea un nuevo repositorio.
Te recomiendo usar el nombre que te sugiere GitHub automáticamente para evitar problemas de rutas.
⚠️ No añadas ningún archivo adicional como el README.md en esta etapa.

2. Subir los archivos al repositorio

Luego de crear tu repositorio, en el apartado de Quick setup, busca la opción "uploading an existing file".

Haz clic ahí y sube los siguientes archivos que usarás en tu proyecto:

backup.sh

iniciar.py

java-execute.jar

Estos tres archivos son fundamentales para que el servidor funcione correctamente.

3. Crear el Codespace

Una vez que tu repositorio ya tiene los archivos, dirígete a la parte superior izquierda (las tres rayitas del menú lateral) y selecciona la opción Codespaces.

En la parte superior derecha, haz clic en el botón New Codespace.

4. Configurar el Codespace

Aquí debes seleccionar tu repositorio recién creado, la región en la que te encuentres y el tipo de máquina (machine type).

🔹 Recomendación: Usa una máquina de 4 cores y 16 GB de RAM.

🕒 Nota importante sobre los límites gratuitos:

El plan de 2 cores tiene 50 horas gratis al mes.

El plan de 4 cores tiene 25 horas gratis al mes.
(Es decir, la mitad de tiempo si usas más potencia).

Lo bueno es que estas horas se reinician automáticamente cada mes, por lo que puedes volver a usarlas sin problema.

5. Crear el entorno dentro del Codespace

Después de crear tu Codespace:

Crea dos carpetas nuevas dentro del proyecto:

Una llamada server

Otra llamada playit

Ve al apartado de extensiones (icono de cuadrado en la barra lateral) y añade la extensión de Python, ya que se necesita para ejecutar el script iniciar.py.

6. Instalar Playit dentro del Codespace

En la consola del Codespace, entra a la carpeta de playit con el siguiente comando:

cd playit


Ahora ejecuta estos comandos para descargar e instalar Playit:

curl -L -o playit https://github.com/playit-cloud/playit-agent/releases/latest/download/playit-linux-amd64
chmod +x playit


Esto descargará el ejecutable de Playit y le dará permisos para poder ejecutarlo.

7. Mover el archivo del servidor

El archivo java-execute.jar (tu servidor) debes moverlo a la carpeta server.

Haz clic derecho sobre él y selecciona Mover o Cortar, y luego pégalo dentro de /server.

8. Configurar los archivos backup.sh e iniciar.py

Ahora que ya tienes todo organizado, debes editar los archivos backup.sh y iniciar.py.

backup.sh: su función es guardar todo el progreso del servidor directamente en tu repositorio de GitHub. Esto te permite descargar tu mundo como copia de seguridad, ya sea con git clone desde tu PC o directamente en formato .zip desde GitHub.

iniciar.py: como su nombre indica, se encarga de iniciar el servidor de Minecraft y Playit automáticamente.

9. Editar backup.sh

Dentro del archivo backup.sh, localiza la parte donde dice:

# Navegar al repositorio
cd /workspaces/upgraded-octo-tribble


Ahí debes reemplazar la ruta /workspaces/upgraded-octo-tribble con el nombre real de tu repositorio.

Por ejemplo, si tu repo se llama serverasdasd, debe quedar así:

cd /workspaces/serverasdasd


Más abajo, busca la parte de:

# Hacer commit con mensaje
git commit -m "Backup automático"


Ahí puedes cambiar el mensaje del commit por uno personalizado.
💡 Consejo: cambia el mensaje cada vez que hagas una copia de seguridad, para que puedas identificar fácilmente cada backup.

10. Editar iniciar.py

En este archivo debes ajustar los directorios para que coincidan con el nombre de tu repositorio.
Por ejemplo:

server_dir = "/workspaces/TU-REPO/server"
playit_dir = "/workspaces/TU-REPO/playit"


Además, en la sección que dice # Iniciar el servidor de Minecraft, casi al final, revisa la ruta al archivo .jar.
Debe coincidir con tu configuración, por ejemplo:

"/workspaces/TU-REPO/server/java-execute.jar"


También puedes editar los argumentos de ejecución de Java, ya que el script está configurado para que el servidor use 15 GB de RAM (de los 16 GB disponibles).
Si estás usando una máquina con menos RAM (por ejemplo, 8 GB), ajusta los valores según tus necesidades.

Estos argumentos incluyen las Aikar’s Flags, las cuales sirven para optimizar el rendimiento del servidor. Puedes buscar más información sobre ellas y personalizarlas si lo deseas, pero los valores actuales funcionan bien con 16 GB.

11. Aceptar el EULA del servidor

Ahora pasamos a la primera ejecución:

Entra a la carpeta del servidor:

cd server


Inicia el servidor por primera vez:

java -jar java-execute.jar


Cuando se cierre automáticamente, abre el archivo /server/eula.txt y cambia:

eula=false


por

eula=true


El archivo se guarda automáticamente dentro del Codespace.

Luego vuelve a ejecutar:

java -jar java-execute.jar


Esto sirve para que el servidor genere todos los archivos necesarios.

12. Ejecutar Playit por primera vez

En la parte inferior derecha verás las terminales activas.
Añade una nueva terminal sin cerrar la del servidor de Minecraft.

En esta nueva terminal:

Entra a la carpeta de Playit:

cd playit


Ejecuta el agente:

./playit


Esto te mostrará un enlace en la consola para unir tu cuenta de Playit y configurar los túneles.

13. Configurar túneles en Playit

Cuando abras el enlace:

Haz clic en crear túnel.

En la nueva página, asegúrate de que:

En Region, esté seleccionada la versión gratuita.

En Tunnel Type, selecciona Minecraft Java.

Acepta los cambios y espera que en la consola y en Playit aparezca "Connected".

14. Obtener la IP del servidor

Dentro del panel de Playit, selecciona el túnel de Minecraft.
A la derecha del título Minecraft Java (en negrita) verás la IP asignada.
Te recomiendo usar la IP numérica y no la DNS.

Para probar si funciona, entra en Minecraft y usa esa IP para conectarte.
Si todo está bien, deberías ver tu servidor en línea.

15. Cerrar correctamente

Cuando termines de probar, cierra ambas terminales (la del servidor y la de Playit) con Ctrl + C.
Esto detendrá correctamente los procesos.

16. Ejecución automática (Post-instalación)

Si configuraste todo correctamente, ahora solo debes abrir el archivo iniciar.py y hacer clic en el botón de iniciar (play) arriba a la derecha.

Esto ejecutará automáticamente el servidor de Minecraft y Playit al mismo tiempo.

Para cerrar el servidor, simplemente presiona Ctrl + C en la terminal.

17. Hacer copias de seguridad

Cuando hayas jugado por bastante tiempo y quieras hacer un respaldo, ejecuta en la terminal:

./backup.sh


Luego, entra a tu repositorio y descarga el .zip o usa git clone desde tu PC para guardar tu mundo.

❓ Ayuda general
a. ¿Por qué no me deja unirme o me pide reiniciar el launcher?

Esto sucede porque el servidor está configurado solo para jugadores con Minecraft Premium.
Para permitir que jugadores no premium se unan, abre el archivo server.properties y cambia:

online-mode=true


por

online-mode=false

b. ¿Cómo cambio la dificultad del juego?

Abre el archivo server.properties y busca:

difficulty=easy


Puedes reemplazarlo por:

peaceful

easy

normal

hard

c. ¿Cómo cambio la descripción y la imagen del servidor?

Para cambiar la descripción (MOTD), busca en server.properties:

motd=A Minecraft Server


y escribe lo que quieras mostrar.

Para cambiar la imagen, crea una imagen 64x64 píxeles, nómbrala server-icon.png y colócala dentro de la carpeta /server.

d. ¿Cómo añado archivos al servidor (mods, imagen, datapacks, etc.)?

Haz clic derecho en la carpeta donde quieras añadir el archivo → selecciona Cargar → elige el archivo.
Se subirá automáticamente al Codespace.

Esto sirve para subir mods, datapacks, o cualquier otro archivo adicional que necesite tu servidor.

✅ ¡Y listo! Si seguiste todos los pasos al pie de la letra, ya tienes un servidor de Minecraft funcional, con Playit y GitHub Codespaces, totalmente gratuito y optimizado.