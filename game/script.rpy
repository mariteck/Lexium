define d = Character("Dylan", color="#b0db98")
define m = Character("Mamá", color="6cb8eb")
label start:
    #first level start
    default sour = False
    default sweet = False
    scene black
    hide bg_day1 with fade
    "¡Dylan, ven acá!"
    
    "¡Ya va!"    
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
    


#first level end
