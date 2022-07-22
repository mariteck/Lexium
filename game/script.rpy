define d = Character("Dylan", color="#b0db98")
define m = Character("Mamá", color="6cb8eb")

label start:
    
    scene bg_room
    with fade

    "Lo triste es así.      
    -Peter Altenberg"
    

    show dylan_idle_small

    d "M-much-chos a-años d-despu-ués, fre-ente al pel-lotón.... ah, me rindo."
    d "De que servirá leer con esta bendita discapacidad."
    hide dylan_idle_small
    
    show mom_placeholder
    m "No te rindas hijo. Todo valdrá la pena en el futuro."