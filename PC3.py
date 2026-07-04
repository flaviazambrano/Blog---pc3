# Antes de ejecutar un script de Python en Streamlit debes definir la carpeta donde se encuentra tus archivos
# cd ruta_de_tu_carpeta o abrimos el folder desde visual Studio Code 

# Primero creamos un entorno virtual para instalar Streamlit y otras librerías que necesitemos.
# python -m venv .venv
# Esto nos permite crear un entorno virtual donde instalaremos Streamlit 
# y observaremos la página web que se está generando en este script.

# Opcional: Activaremos el entorno virtual.
# En Windows:
# .venv\Scripts\activate
# deactivate
# En MacOS/Linux:
# source .venv/bin/activate

# Acontinuación instalamos Streamlit 
# pip install Streamlit
# pip install streamlit_option_menu
# pip install streamlit.components.v1

# Este código sirve para acceder una página web en tu navegador que te brinda información sobre Streamlit.
# Pero se ejecuta en la terminal Python de tu ordenador.
# python -m streamlit hello

# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu ordenador.
# OJO: Debes antes tener instalado Streamlit en tu ordenador, 
## también debes antes definir la ruta de tus archivos y 
## tener un script de Python (nombre_de_tu_script.py) que quieras ejecutar en Streamlit.
# python -m streamlit run PC3.py
# python -m streamlit run nombre_de_tu_script.py

# Librería principal para desarrollar aplicaciones web con Streamlit.
import streamlit as st
# Herramienta para crear menús de navegación personalizados en Streamlit.
from streamlit_option_menu import option_menu
# Este módulo permite incrustar componentes personalizados escritos en HTML, CSS y JavaScript dentro de una aplicación.
# components.html() permite mostrar código HTML interactivo directamente en la interfaz.
import streamlit.components.v1 as components

# Menú vertical en una barra lateral
# Crea una barra lateral (sidebar) en la aplicación.
with st.sidebar:
    opciones = option_menu("Selecciona una sección: ",['Inicio', 'Experiencia', 'Gráficos'] , 
        icons=['emoji-laughing','gem', 'graph-up-arrow'], menu_icon="filetype-py", default_index=0)
    # Crea un menú de opciones dentro de la barra lateral -> option_menu(...)
    # Título que se mostrará encima del menú -> "Selecciona una sección: "
    # Lista de opciones disponibles para navegar -> ['Inicio', 'Experiencia', 'Gráficos']
    # Iconos asociados a cada opción del menú -> ['0-circle','1-circle', '2-circle']
    # Icono principal que aparece junto al título del menú -> menu_icon="filetype-py"
    # Opción seleccionada por defecto (0 = Inicio) -> default_index=0

# Menú horizontal en una barra horizontal
# OJO: Se puede eliminar el título del menú con None
# Crea un menú de navegación horizontal y guarda la opción seleccionada por el usuario en la variable 'selected'
# selected = option_menu(
    # menu_title="Selecciona una sección: ", 
    # options=['Inicio', 'Experiencia', 'Gráficos'], 
    # icons=['person-heart', 'globe-americas', 'pencil-square'], 
    # menu_icon="cast", default_index=0, orientation="horizontal")
    # Título que aparece antes de las opciones del menú -> menu_title="Selecciona una sección: "
    # Lista de opciones que estarán disponibles en el menú -> ['Inicio', 'Experiencia', 'Gráficos']
    # Iconos asociados a cada opción del menú -> ['person-heart', 'globe-americas', 'pencil-square']
    # Icono principal que aparece junto al título del menú -> menu_icon="cast"
    # Opción seleccionada por defecto (0 = Inicio) -> default_index=0
    # Hace que el menú se muestre horizontalmente en lugar de verticalmente -> orientation="horizontal"

# Verifica si el usuario ha seleccionado la opción "Inicio" en el menú de navegación horizontal.
# OJO: En caso que elijas el menú de la barra lateral (sidebar) debes cambiar "selected" por "opciones"
if opciones == 'Inicio':
    st.markdown("<h1 style='text-align: center;'>Blog :)))</h1>", unsafe_allow_html=True)
    # Muestra un título principal utilizando HTML -> st.markdown("...", unsafe_allow_html=True)
    # La etiqueta <h1> define un encabezado de nivel 1 -> "<h1 ...>...</h1>"
    # El estilo CSS 'text-align: center' centra el texto -> style='text-align: center;'
    # unsafe_allow_html=True permite que Streamlit interprete y renderice el código HTML incluido en la cadena

    # Crea dos columnas de igual tamaño para organizar el contenido de forma horizontal en la aplicación.
    col1, col2 = st.columns(2)

    # Muestra una imagen en la primera columna
    col1.image("yo.png", caption='Flavia :3', width=300)
    # "ellie.png" es el archivo de imagen que se visualizará -> Aquí debes reemplazar por tu foto de perfil
    # El texto "Ellie" aparecerá como descripción de la imagen
    # width=300 establece el ancho de la imagen en 300 píxeles

    # Define una cadena de texto multilínea que contiene una guía para redactar una presentación personal.
    texto = """
    ¡Hola! Soy Flavia Zambrano, estudiante de quinto ciclo de Periodismo en la PUCP. 
    Vivo en el Centro de Lima, Perú, y me apasiona descubrir historias, investigar e informar 
    sobre distintas realidades de mi país y del mundo. Uno de los aspectos que más disfruto es 
    la fotografía periodística, porque me permite contar historias a través de imágenes.
    En el futuro, me gustaría conducir un programa sobre moda indígena y contribuir a visibilizar 
    la riqueza cultural del Perú. En mi tiempo libre disfruto jugar vóley, escribir poemas 
    y escuchar mucha música.
    """

    # Muestra el texto en la segunda columna utilizando HTML
    col2.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto}</div>", unsafe_allow_html=True)
    # El estilo CSS justifica el texto y establece un tamaño de fuente de 18 píxeles
    # f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>"
    # unsafe_allow_html=True permite que Streamlit interprete las etiquetas HTML incluidas en la cadena

elif opciones == 'Experiencia':
    st.markdown("<h1 style='text-align: center;'>Nombre a la sección de experiencia 💻</h1>", unsafe_allow_html=True)

    # Agregar un  texto para la respuesta
    texto_2 = """
    Aprender a programar ha sido un reto para mí. 
    Al principio me sentí muy confundida porque es una 
    forma de pensar diferente y, muchas veces, el código no 
    salía como esperaba. Aunque programar me parece difícil 
    y a veces estresante, siento mucha satisfacción cuando 
    logro que el código funcione correctamente. En el futuro no 
    me gustaría dedicarme a la programación, pero sí aprender 
    lo básico para desarrollar proyectos sencillos. Como estudiante de Periodismo, 
    creo que estos conocimientos son útiles porque me ayudan a comprender
    mejor las herramientas digitales y la tecnología que cada vez tienen más importancia en mi carrera.
    """

    # Mostramos el texto
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_2}</div>", unsafe_allow_html=True)

    # Formato A
    # Agregamos todo los videos realizados en las prácticas anteriores
    # Muestra un subtítulo para identificar el contenido del video
    st.subheader("🎥 Video 1 - YouTube")
    # Inserta un video de YouTube directamente en la aplicación.
    # El usuario puede reproducirlo sin salir de Streamlit.
    st.video("https://www.youtube.com/watch?v=SJ-UMN_M62k")
    # Agrega una breve descripción del video.
    st.markdown(
        """En este video se presenta una explicación de los tipos de datos 
        y las expresiones booleanas en Python, utilizando ejemplos prácticos 
        desarrollados en Google Colab. A lo largo del video se explica el 
        funcionamiento de los principales tipos de datos (string, integer, 
        float y boolean), el uso de variables, la función print(), las 
        f-strings, los operadores aritméticos y las expresiones booleanas, 
        con el propósito de comprender cómo se utilizan estos conceptos 
        básicos en la programación en Python."""
    )
    st.subheader("🎥 Video 2 - YouTube")
    # Inserta un video de YouTube directamente en la aplicación.
    # El usuario puede reproducirlo sin salir de Streamlit.
    st.video("https://www.youtube.com/watch?v=BY72HAKRFqM")
    # Agrega una breve descripción del video.
    st.markdown(
        """En este video se presenta una explicación sobre las diferencias entre 
        las declaraciones condicionales if, if-else e if-elif-else en Python. 
        Para ello, se utilizan ejemplos propios relacionados con objetos de una fiesta 
        y con una lista de números, con el fin de mostrar cómo funciona cada estructura, 
        en qué situaciones se utiliza y cuáles son sus principales diferencias."""
    )
 
elif opciones == 'Gráficos':
    st.markdown("<h2 style='text-align: center;'>Nombre a la sección 'Gráficos'</h2>", unsafe_allow_html=True)

    graficos = ['Gráfico_1', 'Gráfico_2', 'Grafico_3' , 'Mapa_1']

    grafico_seleccionado = st.selectbox('Seleccionar un gráfico', graficos)

    # Mostramos el gráfico seleccionado
    if grafico_seleccionado == 'Gráfico_1':
        # Título de la sección
        st.subheader("Comparación del rendimiento ofensivo y defensivo del Real Madrid como local y visitante")

        # Interpretación del gráfico
        st.markdown(
            """
            <div style='text-align: justify; font-size: 20px;'>
           Esta figura presenta cuatro histogramas que analizan el rendimiento del Real Madrid durante la temporada, 
           diferenciando los partidos disputados como local y como visitante. Los gráficos muestran la frecuencia 
           con la que el equipo anotó y recibió determinada cantidad de goles en cada condición de juego.

            Los dos primeros histogramas corresponden al desempeño del Real Madrid como local: el primero representa 
            los goles anotados y el segundo los goles recibidos. Los dos últimos muestran el comportamiento del equipo 
            cuando juega como visitante, diferenciando nuevamente entre los goles anotados y los goles recibidos.

            En conjunto, estos gráficos permiten comparar el rendimiento ofensivo y defensivo del equipo tanto en casa 
            como fuera de ella, identificando las cantidades de goles que se presentan con mayor frecuencia en cada situación.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Centrar la imagen utilizando tres columnas
        col3, col4, col5 = st.columns([1, 5, 1])

        with col4:
            st.image(
                "barras.png",
                width=800
            )

    elif grafico_seleccionado == 'Gráfico_2':
        # Título de la sección
        st.subheader("Real Madrid: goles recibidos como local")

        # Interpretación del gráfico
        st.markdown(
            """
            <div style='text-align: justify; font-size: 18px;'>
           Este gráfico representa los goles que recibió el Real Madrid jugando como local.
           Sirve para analizar su desempeño defensivo en casa y ver con qué frecuencia recibió 
           pocos o muchos goles en sus partidos.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Centrar la imagen
        col6, col7, col8 = st.columns([1, 5, 1])

        with col7:
            st.image(
                "hisstograma .png",
                width=800
            )
    elif grafico_seleccionado == 'Grafico_3':
        # Título de la sección
        st.subheader("Rendimiento del Real Madrid como visitante")

        # Interpretación del gráfico
        st.markdown(
            """
            <div style='text-align: justify; font-size: 18px;'>
           Este gráfico de pastel muestra la distribución de los resultados obtenidos 
           por el Real Madrid en los partidos que disputó como visitante durante la temporada.
           Se observa que el 57.9 % de los encuentros terminaron en victoria, lo que representa 
           la mayor proporción del gráfico y evidencia un buen desempeño del equipo fuera de casa.

            Por otro lado, tanto los empates como las derrotas representan el 21.1 % cada uno, 
            lo que indica que ambos resultados ocurrieron con la misma frecuencia. En conjunto, 
            el gráfico permite concluir que el Real Madrid obtuvo un rendimiento positivo como visitante, 
            ya que ganó más de la mitad de los partidos disputados fuera de su estadio, mientras que los empates 
            y las derrotas tuvieron una participación considerablemente menor.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Centrar la imagen
        col6, col7, col8 = st.columns([1, 5, 1])

        with col7:
            st.image(
                "pastel.png",
                width=800
            )
    elif grafico_seleccionado == 'Mapa_1':
        # Título de la sección
        st.subheader("Lugares de grabación de mi top 5 de películas favoritas")

        # Interpretación del mapa
        st.markdown(
            """
            <div style='text-align: justify; font-size: 18px;'>
            Este mapa interactivo muestra los lugares de grabación de mis cinco películas favoritas. 
            Cada marcador representa una película y contiene información relevante como el director, 
            el año de estreno, el género, el país y el lugar donde fue grabada. Gracias a las coordenadas 
            geográficas, es posible ubicar cada producción en el mapa y explorar su información 
            de manera interactiva.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Cargar el mapa HTML generado previamente
        with open("mapa.html", "r", encoding="utf-8") as f:
            html_content = f.read()

        # Mostrar el mapa interactivo
        components.html(
            html_content,
            height=600
        )

        
