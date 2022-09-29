define d = Character("Dylan", color="#b0db98")
define m = Character("Mamá", color="6cb8eb")
define mr = Character("Miss. Ramos", color="#74C7EF")
define a1 = Character("Joel", color="#FFFFFF")
define a2 = Character("Pedrito", color="#FFFFFF")
define a3 = Character("Camilo", color="#FFFFFF")
define b = Character("Bibliotecaria", color="#FFFFFF") 
label start:
    #first level start
    default sour = False
    default sweet = False
    default l_solve = False 
    scene black
    hide bg_day1 with fade
    play music salem volume 0.2

    "Si la raiz de cuarenta y nueve es... "
    "..¿6?"
    "¡Dylan!"
    "Entones la raiz de 121 puede ser..."
    "¡DYLAN!"
    "¿...?"
    "...hm..."
    "...Entonces la raiz de kuɐtro..."
    
    play sound fo

    "¿Dylan?"  

    stop sound 
    stop music
    
    hide black
    scene bg_room
    with fade

    show dylan_idle_small
    with dissolve

    d "¿Qué es esto?"
    
    hide dylan_idle_small
    with dissolve
    show dylan_idle_small at left
    with dissolve
    show paper_piece at right
    with dissolve

    d "Una pieza de papel. Me pregunto que hará aqui."
    hide paper_piece
    with dissolve
    "{i}Un póster nuevo en la sala llama tu atención.{/i}"
    show poster_placeholder_m at right
    with dissolve   
    "¿Que dice el póster?"
    menu:
        "Procsimamente em teatroz cercanoz a ti...":
            d "{color=#f5a5a4}Quisiera saber que dice el afiche en realidad...{/color}" 
            default wrongans = 1
        "Próximamente en teatros cercanos a tí...":
            d "{color=#b1f5a4}Quisiera saber que dice el afiche en realidad...{/color}" 
            default rightans = 1
    hide poster_placeholder_m with dissolve
    m "¡DYLAN!"
    d "¡En camino!"
    hide dylan_idle_small with dissolve
    
    scene bg_kitchen with fade
    hide bg_room 
    image dylan_smile_anim:
        "dylan_idle_small.png"
        pause 3.0
        "dylan_smile_small.png"
        pause 2.0
        "dylan_idle_small.png"
   
    show mom_idle at right
    with dissolve
    show dylan_smile_anim at left
    with dissolve

    m "Necesito que me vayas a hacer un mandado, hijo."

    "{i}Te sientes incomodado por la solicitud. {/i}"
    d "Claro ma. ¿Que necesitas?"
    
    m "Necesito que vayas al súper, y me consigas salsa de tomate con{i} mostaza dulce {/i}. No te confundas."
    
    d "Bueno, enseguida vengo."

    hide mom_idle with dissolve 
    hide dylan_smile_anim with dissolve
    
    scene bg_street with fade
    hide bg_kitchen 
    
    "{i}Después de una corta caminata, llegas al supermercado.{/i}"
    "{i}Nunca te gusta salir a caminar, hay mucho ruido y demás;{/i}"
    "{i}Pero hoy la tarde se veía especialmente magnífica, y no pudiste saber porqué.{/i}"
    scene bg_market with fade
    hide bg_street 
    show dylan_idle_small with dissolve
    "{i}Entras al pasillo, y ves dos recipientes de salsa."
    d "{i}{color=#8f8f8f}¿Cuál fue la salsa que pidió mamá?{/color}{/i}"
    menu:
        "Escoges el que dice \"moztasa argai\"":
            $ sour=True
        "Escoges el que dice \"moztasa dluse\"":
            $ sweet=True
    "{i}Pagas por la salsa y regresas a casa.{/i}"
    hide dylan_idle_small with dissolve
    scene bg_kitchen with fade
    hide bg_market 
    show dylan_talk_small at left 
    with dissolve
    d "¡Llegué mamá!"
    show mom_idle at right
    with dissolve
    if sour == True:
        show dylan_smile_anim at left
        m "{color=#b1f5a4}¡Bien! Te va a encantar la comida.{/color}"
        $ rightans = rightans + 1
        hide dylan_smile_anim with dissolve
    elif sweet == True:
        show dylan_idle_small at left  
        m "{color=#f5a5a4}Ay hijo, esta no era... No te preocupes, de igual manera sabrá bien.{/color}"
        $ wrongans = wrongans + 1
        hide dylan_idle_small with dissolve
    hide mom_idle with dissolve
    "{i}Mamá y tú cenaron juntos, y te sentías tan cansado que fuiste a dormir enseguida."
    hide dylan_talk_small
    show black 
    hide bg_kitchen with fade
    
    "{i}Normalmente, no sueñas mucho.{/i}"
    "{i}Tu realidad de videojuegos y películas deja mucho que desear en términos de soñar.{/i}"
    scene dream_bg_street with fade
    hide black
    "{i}Solo deseas que un día pudieras caminar por la calle sin la ansiedad de los sonidos que tanto te molestan.{/i}"
    "{i}De repente, te das cuenta de que el parque al que usualmente vas está cubierto de nieve.{/i}"
    scene dream_forest with fade
    hide dream_bg_street
    "{i}De repente, el parque que visitabas todos los días se había convertido en un bosque, extenso, inmiscuido en un aura de oscuridad, y neblina.{/i}"
    "{i}Continuaste caminando, y te encontraste a la distancia con una pequeña ave...{/i}"
    d "¿Un petirrojo? ¿Que haces aquí amigo?"
    "{i}El petirrojo, casi conociendote, despegó, revoloteando hasta posarse en tu hombro.{i}"
    "{i}Casi al instante, el petirrojo comenzó a cantar una melodía suave y dulce...{/i}"
    scene dream_river with fade
    hide dream_forest
    "{i}De la nada, fuiste transportado a otra parte del bosque.{/i}"
    "{i}Era un río, iridiscente, como si hubiera una bombilla por debajo del mismo...{/i}"
    "{i}Parecía algo {b}mágico{/b}, y no podías explicar el porqué.{/i}"
    "{i}Fue en ese entonces que notaste una hojita, con algo escrito en ella.{/i}"
    d "{i}El futuro está en tus manos...{/i}"
    "{i}De repente te diste cuenta; no tuviste problemas para leer.{/i}"
    "{i}Algo te decía, 'Acércate... tengo el secreto que buscas...'{/i}"
    "{i}La curiosidad te ganó la batalla, y decidiste entrar al río.{/i}"
    scene black with fade
    hide dream_river
    "{i}Te estabas acercando más y más al río, y fue justo entonces cuando...{/i}"
    "{i}{color=#8f8f8f}¡¡DESPIERTA!!{/i}{/color}"
    scene bg_room with dissolve
    hide black 
    show mom_idle at right
    show dylan_idle_small at left
    d "¡GAAAH!"
    m "Por dios hijo, ¡que vas tarde a la escuela!"
    m "Levántate ya mijo, dale, dale rápido."
    "{i}No puedes contenerte y bostezas fuertemente.{/i}"
    d "Ok, ok, voy."
    "{i}Te cambiaste lo más rapido posible, y saliste al colegio.{/i}"
    scene bg_street with fade
    hide bg_room
    "{i} Después de ese sueño, querías pasar por el parque.{/i}"
    "{i}Ahora ibas un poco corto de tiempo, así que solo fuiste directo a la escuela.{/i}"
    scene black with pixellate
    "{i}Después de una corta caminata, llegaste a la escuela.{/i}"
    "{i}Tu 'problema', al menos asi lo llamaban todos. no te dejaba estudiar muy bien.{/i}"
    "{i}Para ir al colegio, era necesaria mucha fuerza de voluntad para seguir adelante.{/i}"
    "{i}No te detuviste a hablar con nadie, y solo llegaste directo al salón."
    scene bg_classroom with pixellate
    hide black
    show professor with dissolve
    mr "Ok, clase. Hoy vamos a hacer una actividad en grupo."
    mr "¡Grupos de 4 por favor! ¡Y rápido!"
    hide professor with dissolve
    "{i}Seguías pesado por el sueño, asi que lentamente te paraste a buscar a tus amigos.{/i}"
    "{i}Al cabo de unos minutos de gritos y ruido, el salón estaba organizado.{/i}"
    show professor with dissolve 
    mr "Hoy les tengo una actividad de búsqueda del tesoro."
    mr "Alrededor del colegio, hay unos elementos escondidos. Cada grupo tiene una lista de ellos, ojo que no se les pierda."
    mr "-Porque no les voy a dar más."
    mr "Junto a esos elementos, habrá unos acertijos."
    mr "¡El primer grupo en traer los elementos completos tendra una recompensa en la asignaura!"
    mr "Ahora vayan, que no tienen todo el día."
    hide professor with dissolve 
    "{i}Te reúnes con tu grupo de amigos para que hablen sobre su estrategia.{/i}"
    show dylan_idle_small with fade
    a1 "Empezaremos por la biblioteca y los pasillos, ¿alguien me quiere acompañar a la biblioteca?"
    "{i}Figurabas que- al ser la biblioteca, habría más silencio que afuera de esta.{/i}"
    d "¡¡YO!!"
    a1 "Em, ok pues."
    scene bg_hall with pixellate
    hide bg_classroom
    "{i}Te encaminas a la biblioteca junto a Joel.{/i}"
    scene bg_library with pixellate
    hide bg_classroom
    a1 "Esto es genial, ¡¿muy emocionante no?!"
    d "Totalmente...."
    "{i}No te sientes muy llamado a esto, pero aun así sigues buscando.{/i}"
    d "¡Encontre uno!"
    b "¡SHHHHH! ¡Estamos en una biblioteca joven, no en el mercado!" 
    d "¡Lo siento!"
    "{i}Sales rápidamente de la biblioteca, junto a Joel."
    a1 "¡Bien! A ver el acertijo."
    d "{i}{color=#8f8f8f}Hay Z qabres y Z hijos, qero zolo hay 3 qersonas. ¿Puienez som?{/i}{/color}"
    menu:
        "¿No serán un abuelo, un padre y un hijo?":
            a1 "Hmmm... puede ser, habrá que ver a futuro."
            $ l_solve=True
        "Ay, no sé. Nunca me gustaron estos problemas.":
            a1 "Pero, si sigues actúando así nunca llegarás a nada...."
            $ l_solve=False
        "¿Tu que crees que es?":
            a1 "Hmm... de pronto son una pareja y un abuelo.. no sé."
            $ l_solve=False
        "{i}Te quedas callado, nervioso.{/i}":
            a1 "¿Dylan? Estás raro, man."
            d "¡AH! Ah, si si. No pasa nada."
            $ l_solve=False
    a1 "Regresemos a estos chicos, vamos a ver que han visto."
    "{i}Aún distraido y cansado, respondes-{/i}"
    d "Ok, vamos."
    
    
    
    
