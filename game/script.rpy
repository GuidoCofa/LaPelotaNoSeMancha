# =========================================
# CONFIGURACIÓN DE PERSONAJES
# =========================================

define a = Character("Alberto", color="#1E90FF")       # Azul
define g = Character("Gabriela", color="#E91E63")      # Rosa
define m = Character("Marido", color="#FFA500")        # Naranja
define e1 = Character("Enfermero 1", color="#4CAF50")  # Verde
define e2 = Character("Enfermero 2", color="#9C27B0")  # Violeta

# =========================================
# DECLARACIÓN DE IMÁGENES
# =========================================

image hospital_suelo = "images/hospital_suelo.png"
image hospital_alberto = "images/hospital_alberto.jpg"
image barrio_cancha = "images/barrio_cancha.png"

# =========================================
# INICIO DEL JUEGO
# =========================================

label start:

    # Pantalla inicial negra + sonidos ambientales
    scene black
    play sound "audio/estruendos.mp3"
    play sound "audio/murmullos.mp3"

    # Diálogos iniciales
    e1 "¡Está sangrando mucho! Necesitamos que los doctores se apuren en la operación."
    e2 "¡Bajen un cambio! Estamos laburando lo mejor que podemos. Enfermeras, saquen a la familia y que quede solo el marido de la mujer."
    m "Ojo con el pibe, tengan cuidado que es el futuro de mi familia. Nos va a sacar de esta situación nefasta y nos va a volver millonarios."

    play sound "audio/gritos_mujer.mp3"

    g "¡¡¡AHHHH!!!... ¡Cómo duele, por favor que termine esto rápido, por el amor de Dios!"

    # Texto previo a la decisión
    "Tu vida pende de un hilo..."

    # Primera decisión interactiva
    "¿Qué harás?"

    menu:
        "Pelear por tu vida":
            jump luchar

        "Rendirse":
            jump rendirse


# =========================================
# RUTA: PELEAR POR TU VIDA
# =========================================

label luchar:

    stop sound fadeout 2.0
    play sound "audio/bebe_llorando.mp3"

    scene hospital_suelo
    with fade

    g "Ahhh, qué alivio; no aguantaba más, necesitaba soltarlo. Qué lindo es por Dios, lo amo."
    g "Mirá Alberto, qué lindo es nuestro nene."

    scene hospital_alberto
    with dissolve

    a "Qué bien, Gabriela... este pendejo nos va a sacar adelante."
    a "Va a estar obligado a jugar a la pelota toda su vida. ¡Jajajajaja!"

    scene black
    with fade

    centered "14 años después..."

    jump acto1


# =========================================
# RUTA: RENDIRSE
# =========================================

label rendirse:

    stop sound fadeout 2.0

    scene black
    with fade

    centered "Game Over"

    return


# =========================================
# ACTO 1
# =========================================

label acto1:

    scene barrio_cancha
    play music "audio/cumbia_de_barrio.mp3"

    a "Continuará..."

    return
