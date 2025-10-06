label start:

    # Pantalla en negro con sonidos de fondo
    scene black
    play sound "estruendos.ogg"
    play sound "murmullos.mp3"

    "Se escuchan estruendos de fondo y ruido de murmullos..."

    "??? " "¡Está sangrando mucho! necesitamos que los doctores se apuren en la operación."
    "??? (2)" "¡Bajen un cambio! Estamos laburando lo mejor que podemos, enfermeras saquen a la familia y que quede solo el marido de la mujer."
    "Marido" "Ojo con el pibe, tengan cuidado que es el futuro de mi familia y el que me va a sacar de esta situación nefasta en la que vivimos y nos va a llevar a ser millonarios."

    play sound "gritos_mujer.mp3"

    "Mujer" "¡¡¡AHHHH!!!... ¡Cómo duele, por favor que termine esto rápido, por el amor de Dios!"

    # Texto antes del menú
    "Tu vida pende de un hilo..."

    # Primera decisión interactiva
    menu:
        "Pelear por tu vida":
            jump luchar

        "Rendirse":
            jump rendirse


label luchar:
    "Los gritos continúan pero se van apagando poco a poco..."
    stop sound fadeout 2.0
    play sound "bebe_llorando.mp3"

    scene hospital_suelo
    with fade

    "Un bebé llora mientras es sostenido por unas manos, el piso del hospital de fondo."

    "Madre" "Ahhh, qué alivio; no aguantaba más, necesitaba soltarlo. Qué lindo es por Dios, lo amo. Mira Alberto, qué lindo es nuestro nene."
    
    scene hospital_alberto
    with dissolve

    "Alberto sonríe... pero su expresión tiene algo siniestro."
    "Alberto" "Qué bien Gabriela, este pendejo nos va a sacar adelante. Va a estar obligado a jugar a la pelota toda su vida. ¡Jajajajaja!"

    "..."

    scene black
    with fade
    centered "14 años después..."

    jump acto1


label rendirse:
    "El silencio invade la sala... los gritos cesan."
    "El llanto de un bebé no llega a escucharse."
    "..."
    scene black
    with fade
    centered "Game Over"

    return


label acto1:
    # Arranca el Acto 1
    scene barrio_cancha
    play music "cumbia_de_barrio.mp3"
    "Una pelota rueda en el potrero... comienza tu historia."
    return
