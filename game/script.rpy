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
define nl = Character("Nahuel", color="#6d332b") # Verde oscuro
define ar = Character("Árbitro", color="#5a4d4d") # Beige
define d = Character("Delantero", color="#5e68a5") # Beige
define j7 = Character("Jugador 7", color="#393d7a") # Beige
define narrator = Character(None) # Narrador sin nombre

# =========================================
# DECLARACIÓN DE IMÁGENES
# =========================================

image hospital_suelo = "images/hospital_suelo.png"
image hospital_alberto = "images/hospital_alberto.jpg"
image cancham = "images/cancha_manager.png"
image casa = "images/casa.png"
image calle = "images/calle.jpg"
image canchac = "images/cancha_chicos.png"
image hospital_rendirse = "images/hospital_rendirse.jpg"
image noelia_doc = "images/noeliacondoc.jpg"
image entraalberto = "images/entraalberto.png"
image canchamu = "images/canchamu.png"


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
    n "Ahhh, qué alivio. Qué lindo es, por Dios, lo amo. Mirá, Alberto, qué lindo es nuestro nene."
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


    scene entraalberto
    with fade
    a "A ver para cuándo hacés algo con tu vida en vez de ir a jugar con los pelotudos de tus amigos."

    stop ambient
    play sound "audio/puerta.mp3"

    scene calle
    with fade

    u "Gracias pa, yo también te 'quiero' mucho."

    scene canchac
    play ambient "audio/partido_potrero.mp3" loop
    with fade

    u "¿Qué onda locuras? ¿Sale un fulbito?"
    c1 "¡Eh Ulise', cómo andás! Más vale perri, metete al equipo de Lucas."

    u "¿Qué onda con ese loco de ahí? Está raro y le está hablando a uno de los pibes."
    c2 "Ni idea amigo, vos seguí jugando que estás jugando re piola."

    stop ambient
    scene canchac

    f "Vos, pibe... el negrito morocho de pelo corto. Vení para acá que quiero hablar algo con vos."

    scene canchamu
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
    scene cancham
    with fade
    u "Bueno señor Fabrizio, acepto el trato. ¿Cuándo arranco a jugar?"
    f "Tranquilo pibe, primero andá a tu casa, bañate, y yo te llamo. Las pruebas son el lunes."
    u "Bueno, mi número está acá, llámeme cuando quiera."
    centered "Una semana después..."
    jump escena4


# =========================================
# ESCENA 3B: RECHAZA
# =========================================

label rechazar_trato:

    scene canchamu
    with fade

    u "La posta: no tenés pinta ni en pedo de manager. Volá de acá, viejo, y tocá pa' allá."

    f "Te vas a arrepentir toda tu vida, pendejo fracasado. Vas a seguir viviendo tu vida miserable en esta villa llena de negros."

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

    scene casana
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

    centered "Pasaron 15 minutos de charla."

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

    u "¿Tienen algun problema? Yo se los soluciono a la salida del predio ¿Les parece?"
    nl "Mira, ¿que te parece si lo solucionamos dentro del partido? Porque de vos no nos confiamos a la salida, mira si nos sacas una faka."
    u "Bueno dale, más te vale jugar como dinho porque sino sos pollo."

    jump escena6


# =========================================
# ESCENA 6: EL PARTIDO
# =========================================

label escena6:
    scene partido
    with fade
    play ambient "audio/ambiente_cancha.mp3" loop

    u "¡EH PASALA ACÁ, ESTOY SOLO!"

    nl "Ni en pedo villero, este partido es todo mío."

    # 🔊 Sonido de pelotazo
    $ renpy.music.play("audio/pelotazo.mp3", channel="sound")
    $ renpy.pause(1.0)
    $ renpy.music.stop(channel="sound")

    nl "¡NO! LA PUTA MADRE LA PERDÍ, NEGRO SACÁSELA, NO SEAS INÚTIL."
    u "¡Sí, sí! ¡Es mía!"

    # 🔊 Sonido de golpe (falta)
    $ renpy.music.play("audio/pelotazo.mp3", channel="sound")
    $ renpy.pause(1.0)
    $ renpy.music.stop(channel="sound")

    centered "Golpeas a un jugador y se genera una falta."

    u "¡NO! Fue sin querer, perdón, perdón posta, perdón, no lo hice a propósito."

    ar "¡FOUL! Tiro libre para el equipo rojo."

    centered "Lanzan el tiro libre y se va afuera. Termina el primer tiempo."

    jump escena7

label escena7:

    # 🔇 Paramos sonidos previos
    $ renpy.music.stop(channel="music", fadeout=1.0)
    $ renpy.music.stop(channel="sound", fadeout=1.0)

    # 🎬 Escena vestuario con murmullos de fondo
    scene vestuario
    with fade

    $ renpy.music.play("audio/murmullos.ogg", loop=True, channel="music")

    s "Escuchen todos: no están jugando mal, pero falta cabeza. Nadie piensa la jugada antes de hacerla."

    u "Profe, dénos otra oportunidad, lo damos vuelta."

    s "Ulises, vení para acá."

    u "Dígame, profe."

    s "¿Qué mierda fue eso? ¿Qué fue esa falta estúpida que hiciste ahí?"

    u "Perdón, fue sin querer. Nuestro compañero la perdió y traté de rec..."

    s "Me importa poco y nada lo que hizo tu compañero. No fue él quien metió la patada, ¿O sí? Dejate de boludear porque te voy a sacar a la mierda, ¿Me escuchaste?"

    $ renpy.music.stop(channel="music", fadeout=1.0)

    # 🔹 Decisión del jugador
    menu:
        "Responder y explicarle la situación":
            jump vestuario_responder
        "Quedarte callado y aceptar la responsabilidad":
            jump vestuario_callado

# =========================================
# ESCENA 8A - RESPONDER AL PROFESOR
# =========================================

label vestuario_responder:

    $ renpy.music.play("audio/murmullos.ogg", loop=True, channel="music")

    u "No, pero profe, mire, esto no fue as..."

    s "¡Qué mierda me importa cómo creés que fue! Yo desde el banco vi que le pegaste santa patada. Una vez más que me contestás y te echo del partido, ¿me escuchaste?"

    u "Eh S-s-si, sí, sí, perdón profe. Le juro que no va a volver a pasar, perdón."

    s "Más te vale, pendejo. Ya sabés lo que te va a pasar si lo volvés a hacer."

    $ renpy.music.stop(channel="music", fadeout=1.0)

    scene black
    with fade

    centered "Empieza el segundo tiempo..."

    jump escena9

# =========================================
# ESCENA 8B - CALLARSE Y ACEPTAR
# =========================================

label vestuario_callado:

    $ renpy.music.play("audio/murmullos.ogg", loop=True, channel="music")

    u "Está bien, profe, perdón. No va a pasar de vuelta."

    # 🔊 Sonido de sollozos
    $ renpy.music.play("audio/sollozos.mp3", channel="sound")
    $ renpy.music.stop(channel="sound")

    u "La puta madre, no me sale una... quiero jugar mejor y quedar, la puta madre, Dios, por favor. Lo único que puedo hacer es jugar a mi habilidad, pero tengo miedo. ¿Y si no quedo? ¿Qué voy a hacer de mi vida si no lo consigo? ¡TENGO QUE JUGÁRMELA!"

    $ renpy.music.stop(channel="music", fadeout=1.0)

    scene black
    with fade

    centered "Empieza el segundo tiempo..."

    jump escena9

label escena9:

    scene cancha
    with fade

    $ renpy.music.play("audio/ambiente_cancha.mp3", loop=True, channel="music")

    u "Okay, tengo la pelota... No puedo desperdiciar esta oportunidad. ¿Qué me conviene hacer?"

    # 🔹 Decisiones del jugador
    menu:
        "Amagar al jugador más cercano y pegarle al arco":
            jump opcion_amagar
        "Dar un pase largo al 8":
            jump opcion_pase_largo
        "Dar un pase corto al 9 para que pivotee y te devuelva el pase":
            jump opcion_pase_corto


# =========================================
# ESCENA 9A - AMAGAR Y PEGARLE AL ARCO
# =========================================

label opcion_amagar:

    u "¡Movete, este partido es mío!"

    j7 "¡Qué hacés! ¡Profe, lo tenés que sacar!"

    $ renpy.sound.play("audio/gritos.mp3")

    u "No... no, no, no, fue sin querer... lo juro, no fue a propósito."

    "FADE IN: Zoom a la cara de un chico inconsciente."

    n "¡ASESINO! ¡SOS UN ASESINO, LO MATASTE!"

    u "Yo... no lo hice a propósito, fue un accidente."

    s "¡MOVETE! ¡Mirá lo que le hiciste! ¡Andate de acá antes de que llame a la policía!"

    u "No, profe, por favor..."

    s "No me importa lo que tengas que decir. Ya estoy cansado."

    scene black
    with fade

    centered "FINAL MALO"

    $ renpy.music.stop(channel="music", fadeout=1.0)
    return


# =========================================
# ESCENA 9B - PASE LARGO AL 8
# =========================================

label opcion_pase_largo:

    u "¡Número 8, va larga!"

    j7 "¡Qué hacés! ¿Qué es ese pase? ¡Profe, lo tenés que sacar!"

    s "Vos... ¿cómo te llamabas? ¿Uriel? Vení para acá."

    u "¿Yo, profe?"

    s "Y sí, tonto, vení para acá. ¡Árbitro, cambio!"

    u "No, profe, por favor..."

    s "No me importa lo que tengas que decir. Ya estoy cansado."

    scene black
    with fade

    centered "FINAL MALO"

    $ renpy.music.stop(channel="music", fadeout=1.0)
    return

# =========================================
# ESCENA 9C - PASE CORTO AL 9 Y GOL
# =========================================

label opcion_pase_corto:
    u "Locura, tomá. ¡Devolvé rápido!"
    d "Bueno, más te vale que nos salga bien, ¿me escuchaste?"
    u "Confiá en mí."
    u "Bueno, ahora te toca a vos, 7. ¡Corré que va larga!"
    j7 "¡De una!"
    u "¡Ahí va!"
    j7 "¡Es mía, va el centro rápido!"
    d "Le pego y... ¡AHHHHHHHHH, ES PENAL JUEZ LO TENÉS QUE ECHAR!"
    ar "¡PENAL PARA LOS DE AZUL!"
    u "Lo pateo yo equipo, confíen en mí."

    $ renpy.music.stop(channel="music", fadeout=0.8)
    $ renpy.music.play("audio/ambiente_cancha.mp3", loop=True, channel="music")
    scene bg_penal
    "Te parás frente al arco. Tenés que elegir dónde patear."
    jump penal_minijuego


# =========================================
# MINIJUEGO DE PENAL
# =========================================
label penal_minijuego:
    $ renpy.music.stop(channel="sound", fadeout=0.3)
    scene bg_penal
    "Elegí dónde patear. Hacé click en una zona."

    show screen penal_selector
    $ zona = ui.interact()
    hide screen penal_selector

    if zona in ["derecha", "medio_arriba"]:
        jump penal_gol
    else:
        jump penal_errado


# =========================================
# RESULTADO: GOL
# =========================================
label penal_gol:
    $ renpy.music.play("audio/gol.mp3", channel="sound")
    scene cancha_gol with fade
    centered "{size=46}{b}¡GOOOOOOOOOOOOOL!{/b}{/size}"
    $ renpy.pause(1.0)
    jump escena_10A


# =========================================
# RESULTADO: ERRADO
# =========================================
label penal_errado:
    $ renpy.music.play("audio/fallo.mp3", channel="sound")
    scene cancha_errado with fade
    centered "{size=40}{b}¡ERRASTE!{/b}{/size}"
    $ renpy.pause(1.0)
    jump escena_10B


# =========================================
# ESCENA 10A - FINAL BUENO (GOL)
# =========================================
label escena_10A:
    $ renpy.music.play("audio/ambiente_cancha.mp3", loop=True, channel="music")
    scene cancha_gol with fade
    u "¡GOOOOOOOOOOOOOL, VAAAAAAAAMOOOOOS!"
    u "¡SEEEEE! Estoy seguro de que con esto lo logré y voy a poder salir de los barrios."
    $ renpy.pause(1.0)
    jump escena_11


# =========================================
# ESCENA 10B - FINAL MALO (ERRADO)
# =========================================
label escena_10B:
    $ renpy.music.play("audio/ambiente_cancha.mp3", loop=True, channel="music")
    scene cancha_errado with fade
    u "No... No lo puedo creer, por favor Dios, decime que no."
    s "Era tu última oportunidad pibe y la arruinaste."
    s "Olvidate de todos tus sueños, no pudiste meter un simple penal y querías llegar a primera."
    u "Yo... yo solo quería sacar adelante a mi mamá, por favor señor déjeme una última oportunidad."
    s "No pibe, no entendés. No hay más oportunidades. Era la última y la desperdiciaste."
    $ renpy.pause(1.0)
    scene black with fade
    centered "{size=45}{b}Final malo{/b}{/size}"
    $ renpy.pause(1.2)
    return


# =========================================
# SCREEN DEL MINIJUEGO DE PENAL
# =========================================
screen penal_selector():
    tag penal
    zorder 100

    add "images/bg_penal.png"

    # === IZQUIERDA ===
    imagebutton:
        idle Transform("gui/circle_empty.png", zoom=0.2)
        hover Transform("gui/circle_hover.png", zoom=0.25)
        xpos 400 ypos 390
        xanchor 0.5 yanchor 0.5
        action Return("izquierda")

    # === MEDIO ARRIBA ===
    imagebutton:
        idle Transform("gui/circle_empty.png", zoom=0.2)
        hover Transform("gui/circle_hover.png", zoom=0.25)
        xpos 640 ypos 240
        xanchor 0.5 yanchor 0.5
        action Return("medio_arriba")

    # === DERECHA ===
    imagebutton:
        idle Transform("gui/circle_empty.png", zoom=0.2)
        hover Transform("gui/circle_hover.png", zoom=0.25)
        xpos 885 ypos 390
        xanchor 0.5 yanchor 0.5
        action Return("derecha")

    frame:
        background None
        xalign 0.5
        yalign 0.93
        text "{size=40}{b}Elegí tu disparo{/b}{/size}" xalign 0.5 yalign 0.5 color "#FFFFFF"

    $ renpy.music.play("audio/ambiente_cancha.mp3", loop=True, channel="music")
    $ renpy.music.stop(channel="music")

    
# ==========================
# ESCENA 11 - VESTUARIO - NOCHE
# ==========================

label escena_11:

    scene vestuario_saintlawrence_noche
    with fade

    s "Bueno, después de estas pruebas empezaré a nombrar a los 8 jugadores que lograron cumplir mis expectativas y las del club."

    s "Unai, Julián, ¿Ubaldo?... Eh perdón, Osvaldo, Noah, Joaquín..."

    u "(Por favor quiero ser yo, tengo miedo de morir en este barrio... por favor, es la única chance que tengo.)"

    s "Nahuel, Diego... y por último... Uriel."

    u "¿Qué...? No, no pued..."

    s "Perdón, me equivoqué otra vez. Ulises, ahora sí. Bueno, esos serían los que quedaron para las inferiores. Felicitaciones. Los demás ya se pueden ir a sus casas."

    u "(¡¡SÍIIII, LO CONSEGUÍ!! No lo puedo creer... voy a salir de los barrios bajos al fin.)"

    u "Muchas gracias, profe. ¿Cuándo es que tengo que venir de vuelta?"

    s "El mes que viene arrancan los entrenamientos. Más te vale venir preparado."

    # Fade out final
    scene black
    with fade

    centered "FINAL BUENO.\n¿CONTINUARÁ?"

    return
