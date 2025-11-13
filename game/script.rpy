# =========================================
# CONFIGURACIÓN DE PERSONAJES
# =========================================

define a = Character("Alberto", color="#1E90FF")       # Azul
define m = Character("Marido", color="#FFA500")        # Naranja
define d1 = Character("Doctor 1", color="#4CAF50")  # Verde
define d2 = Character("Doctor 2", color="#9C27B0")  # Violeta
define u = Character("Ulises", color="#00BFFF")     # Celeste
define n = Character("Noelia", color="#FF69B4")     # Rosa claro
define f = Character("Fabrizio", color="#FFD700")   # Amarillo
define s = Character("Sebastián", color="#8B0000")  # Rojo oscuro
define c1 = Character("Chico 1", color="#ADFF2F")   # Verde claro
define c2 = Character("Chico 2", color="#7FFFD4")   # Aguamarina
define narrator = Character(None) # Narrador sin nombre

# =========================================
# DECLARACIÓN DE IMÁGENES
# =========================================

image hospital_suelo = "images/hospital_suelo.png"
image hospital_alberto = "images/hospital_alberto.jpg"
image cancham = "images/cancha_manager.png"
image casa = "images/casa.jpg"
image calle = "images/calle.jpg"
image canchac = "images/cancha_chicos.png"
image hospital_rendirse = "images/hospital_rendirse.jpg"
image noelia_doc = "images/noeliacondoc.jpg"

# =========================================
# ACTO 1 - ESCENA 1: EL HOSPITAL
# =========================================

label start:

    scene black

    # 🔊 Murmullos de fondo — usando canal MUSIC (más estable que ambient)
    $ renpy.music.play("audio/murmullos.ogg", loop=True, channel="music")

    d1 "¡Está sangrando mucho! Necesitamos que los doctores se apuren en la operación."
    d2 "¡Bajen un cambio! Estamos laburando lo mejor que podemos. Enfermeras, saquen a la familia y que quede solo el marido de la mujer."
    m "Ojo con el pibe, tengan cuidado que es el futuro de mi familia. Nos va a sacar de esta situación nefasta y nos va a volver millonarios."

    # 🔊 Grito de mujer — detenemos murmullos antes de reproducirlo
    $ renpy.music.stop(channel="music", fadeout=1.5)
    $ renpy.music.play("audio/gritos_mujer.mp3", channel="sound")
    n "¡¡¡AHHHH!!!... ¡Cómo duele, por favor que termine esto rápido, por el amor de Dios!"
    $ renpy.music.stop(channel="sound")

    "Tu vida pende de un hilo..."
    "¿Qué harás?"

    menu:
        "Pelear por tu vida":
            jump luchar
        "Rendirse":
            jump rendirse

# =========================================
# PELEAR POR TU VIDA
# =========================================

label luchar:

    # Nos aseguramos de que no quede sonido residual
    $ renpy.music.stop(channel="music", fadeout=1.0)
    $ renpy.music.stop(channel="sound", fadeout=1.0)

    # 🔊 Llanto del bebé (solo en este diálogo)
    scene hospital_suelo
    with fade

    $ renpy.music.play("audio/bebe_llorando.mp3", channel="sound")
    n "Ahhh, qué alivio; no aguantaba más, necesitaba soltarlo. Qué lindo es por Dios, lo amo."
    $ renpy.music.stop(channel="sound")

    n "Mirá Alberto, qué lindo es nuestro nene."

    scene hospital_alberto
    with dissolve

    a "Qué bien, Noelia... este pendejo nos va a sacar adelante."
    a "Va a estar obligado a jugar a la pelota toda su vida. ¡Jajajajaja!"

    scene black
    with fade

    centered "14 años después..."

    jump escena2

# =========================================
# RENDIRSE
# =========================================

label rendirse:

    scene hospital_rendirse
    with fade

    d1 "Señora, lamentamos informarle que su hijo nació fallecido. Nuestras más sinceras condolencias."

    n "¡¡NOOOOOO!! No me pueden estar diciendo esto, por favor, tiene que ser mentira. ¿O no es un chiste, Alberto?"

    a "Ni me hables, mujer. Un solo trabajo tenías: dar a luz a mi futuro, y no lo hiciste. No te quiero volver a ver en mi vida."

    narrator "Alberto sale de la habitación..."

    scene noelia_doc
    with fade
   
    n "¡Alberto, volvé! Te necesito. Tu hijo sigue acá, te lo juro. ¡Es todo una mentira de los doctores! ¿O no, doctor?"

    d2 "... Mis más sinceras condolencias, señora. La dejaremos sola para que pueda procesar todo lo que está pasando."

    # 🔊 Sollozos de fondo
    $ renpy.music.play("audio/llantomujer.mp3", channel="sound")
    n "¿Por qué, Dios? ¿Por qué me hacés esto a mí? ¿Qué hice mal? Decímelo."
    $ renpy.music.stop(channel="sound")

    # Fundido final
    scene black
    with fade

    centered "Fin del juego. FINAL MALO."

    return

label escena2:

    scene casa
    with fade
    play ambient "audio/murmullos.ogg" loop

    u "Bueno ma, me voy a la cancha a jugar con los chicos."
    n "Bueno hijo, que te vaya bien y lo disfrutes. Te amo."
    u "Dale ma, gracias. Te amo mucho."

    a "A ver para cuándo hacés algo con tu vida en vez de ir a jugar con los pelotudos de tus amigos."

    stop ambient
    play sound "audio/puerta.mp3"

    scene calle
    with fade

    u "Gracias pa, yo también te 'quiero' mucho."

    scene canchac
    play ambient "audio/partido_bajo.mp3" loop
    with fade

    u "¿Qué onda locuras? ¿Sale un fulbito?"
    c1 "¡Eh Ulise', cómo andás! Más vale perri, metete al equipo de Lucas."

    u "¿Qué onda con ese loco de ahí? Está raro y le está hablando a uno de los pibes."
    c2 "Ni idea amigo, vos seguí jugando que estás jugando re piola."

    stop ambient
    scene canchac

    f "Vos, pibe... el negrito morocho de pelo corto. Vení para acá que quiero hablar algo con vos."

    scene cancham
    with fade

    u "¿Qué pasó señor? Estoy un poco ocupado."
    f "Eh pibe, hablame con respeto. Soy Fabrizio, manager del Club Atlético Saint Lawrence. Estoy reclutando jóvenes promesas. ¿Querés formar parte de la reserva del club?"

    menu:
        "Aceptar el trato":
            jump aceptar_trato
        "Rechazar":
            jump rechazar_trato


# =========================================
# ESCENA 3: EL MANAGER (ACEPTA)
# =========================================

label aceptar_trato:

    u "Bueno señor Fabrizio, acepto el trato. ¿Cuándo arranco a jugar?"
    f "Tranquilo pibe, primero andá a tu casa, bañate, y yo te llamo. Las pruebas son el lunes."
    u "Bueno, mi número está acá, llámeme cuando quiera."
    centered "Una semana después..."
    jump escena4


# =========================================
# ESCENA 3B: RECHAZA
# =========================================

label rechazar_trato:

    scene cancham
    with fade

    u "La posta: no tenés pinta ni en pedo de manager. Volá de acá, viejo, y tocá pa' allá."

    f "Te vas a arrepentir toda tu vida, pendejo fracasado. Vas a seguir viviendo tu vida miserable en esta villa llena de negros."

    "El manager se va de la escena."

    u "Viejo gagá, por Dios. ¡EH, MUCHACHOS! Ahí voy, ya terminé con el pancho este."

    # Fundido y texto final
    scene black
    with fade

    centered "FINAL NORMAL."

    return


# =========================================
# ESCENA 4: DISCUSIÓN EN CASA
# =========================================

label escena4:

    scene casa_pobre
    play ambient "audio/gritos_discusion.mp3" loop
    with fade

    a "Noelia me tené’ cansao con que no me dejás tomarme una birrita con los pibes."
    n "Disculpá que no me guste ver al pelotudo de mi marido en pedo como un linyera."
    a "¡Vos y tu pendejo de mierda me tienen las bolas al plato, Mujer!"
    a "¡El fracasado ese que se cree que va a ser futbolista, y vos que no me dejás hacer nada!"

    stop ambient
    u "Bueno, que me bardees a mí me da lo mismo, ¡pero con mamá no, viejo de mierda!"
    a "¡Las pelotas llenas me tenés, pendejo! ¡VOLÁ DE ACÁ ANTES DE QUE TE CAGUE A SOPAPOS!"
    u "¿Sabés qué? Tenés razón: Me voy a la mierda, pelotudo. ¿Y sabés adónde? A unas pruebas para jugar en Saint Lawrence."

    play sound "audio/puerta.mp3"
    scene calle
    with fade

    u "Este borracho gil viene a hacerse el zarpado... Le voy a cerrar la boca cuando llegue a primera."

    jump escena5


# =========================================
# ESCENA 5: LAS PRUEBAS
# =========================================

label escena5:

    scene cancha
    with fade

    # 🎵 Inicia el audio de entrenamiento en loop para toda la escena 5
    $ renpy.music.play("audio/entrenamiento.mp3", channel="music", loop=True)

    u "Hola, soy Ulises. Vengo por la oferta del señor Fabrizio."
    f "Perfecto, ya llegó el último pibe. Seba, podemos arrancar."
    s "Bueno muchachos, hoy se juegan cambiar sus vidas."

    narrator "Pasaron 15 minutos de charla."

    u "Al fin terminaron de hablar, ya arranca el partido."
    
    # 🛑 Detenemos el audio al pasar a la siguiente escena
    $ renpy.music.stop(channel="music", fadeout=1.0)

    c1 "Eh vos, negrito, ¿qué hacés acá? ¿Te perdiste?"
    c2 "Sí, villerito, tomatelas que este no es lugar para vos."

    menu:
        "Ignorar y seguir":
            jump ignorar
        "Responderles y discutir":
            jump discutir


label ignorar:

    u "Ajá, seguro. Nos vemos en el partido."

  

    jump escena6


label discutir:

    u "¿Qué dijiste, gil? En la cancha te lo demuestro."


    jump escena6


# =========================================
# ESCENA 6: EL PARTIDO
# =========================================

label escena6:

    play ambient "audio/cancha_ambiente.mp3" loop
    scene cancha
    with fade

    u "¡Eh, pasala! ¡Estoy solo!"
    c1 "Ni en pedo, villero. Este partido es mío."
    stop ambient

    centered "Continuará..."

    return