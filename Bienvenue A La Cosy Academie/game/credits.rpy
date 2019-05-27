label credits:
    play music journeys

    image ending_cosy = "ending/Photo-de-fin_mercilesgars.png"

    image perso_gauche:
        xpos 0.0 xanchor 0.0 ypos 1.1 yanchor 1.0 zoom 0.9
        pause 6.0
        "Caro/main_PoseSpeciale_06_Sourire.png"
        pause 6.0
        "Chuenpodo/main_PoseSpeciale_06_Sourire.png"
        pause 6.0
        "din/main_PoseSpeciale_06_Sourire.png"
        pause 6.0
        "Lock/main_PoseSpeciale_06_Sourire.png"    
        pause 6.0    
        "Metalice/main_PoseSpeciale_06_Sourire.png"
        pause 6.0
        "Pansepignon/main_PoseSpeciale_06_Sourire.png"
        pause 6.0
        "Von/main_PoseSpeciale_06_Sourire.png"
        pause 6.0

    image perso_droite:
        xpos 1.0 xanchor 1.0 ypos 1.1 yanchor 1.0 zoom 0.9
        pause 12.0
        "Dieuvomi/main_PoseSpeciale_06_Sourire.png"
        pause 6.0
        xpos 1.0 xanchor 1.0 ypos 1.0 yanchor 1.0 zoom 0.6
        "Cheerleaders/main_Groupe_01_Cheer.png"
        pause 6.0
        xpos 1.0 xanchor 1.0 ypos 1.1 yanchor 1.0 zoom 0.9
        "Foulk/main_PoseSpeciale_06_Sourire.png"
        pause 6.0
        "Mathilde/main_PoseSpeciale_06_Sourire.png"
        pause 6.0
        "Mickey/main_PoseSpeciale_06_Sourire.png"
        pause 6.0
        "ZePilot/main_PoseSpeciale_06_Sourire.png"
        pause 6.0


    image splash = "BienvenueAlaCosyAcademie_logo.png" #Text("{size=90}Le Cosy Cover", text_align=0.5, ypos=0.5) #Placeholder code if you don't have anything to use as a splash image or are just pure lazy.
#    image splash = "images/Company-Logo.png" #This is usually going to be located in an init block executed early in the code to show it when the game loads up as a splash screen.
#    image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, text_align=0.5)
    
    image thanks = Text("{size=80}Merci Medoc & Moguri !", text_align=0.5)
    $ credits_speed = 50 #scrolling speed in seconds
    scene black 
    window hide
    show cred with dissolve:
        yanchor 0.0 ypos 0.5
        xanchor 0.5 xpos 0.5
    with Pause(5.0)
    hide cred
    show cred at Move((0.5, .5), (0.5, -3.5), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="top")
    show perso_gauche
    show perso_droite
    with Pause(credits_speed-1)
    hide cred with dissolve
    hide perso_droite with dissolve
    hide perso_gauche with dissolve
    show splash
    with dissolve
    with Pause(3)
    hide splash
    with dissolve
    with Pause(1)
    show Medoc PoseGauche Sourire at full_left
    show Moguri PoseDroite Sourire at full_right
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(4)
    show Medoc PoseSpeciale Sourire 
    show Moguri PoseSpeciale Sourire
    hide thanks
    with Pause(3)
    with dissolve
    stop music fadeout 6.0
    hide Medoc with dissolve
    hide Moguri with dissolve
    show ending_cosy with dissolve
    pause 6.0
    hide ending_cosy with dissolve
    return

init python:
    credits = ('Personnages', 'din'), ('Backgrounds', 'Ze_PilOt'), ('Les Cheerleaders', 'Ecrit par Clornide'), ('Le club Comédie', 'Ecrit par Dieuvomi'),('Le club Comédie', 'Spectacle de Foulk : Twitter @Foulk32'), ('Le club Tech', 'Ecrit par Decade'), ('Le club Otaku', 'Ecrit par din'), ('Le club des Jeux', 'Ecrit par Clornide'), ('Le club Rando', 'Ecrit par Von Yaourt'), ('Le club de Bagarre', 'Ecrit par KupowY'), ('Le conseil des élèves', 'Ecrit par Decade'), ('Le Cosy Culture Club', 'Ecrit par Ze_PilOt'), ('Le Verdict', 'Ecrit par Clornide'), ('Relecture et corrections', 'KupowY'), ('Relecture et corrections', 'Samaël'),('Relecture et corrections', 'Von Yaourt'), ('Programmation', 'Ze_PilOt'), ('Mise en scène', 'Ze_PilOt'), ('Musique (Creative Common)', 'Scott Buckley'), ('Musique (Creative Common)', 'Myuu'), ('Musique (Creative Common)', 'KODOMOi')
    credits_s = "{size=80}La Fin\n\n\n\n\n\n{size=80}Bienvenue\n{size=20}à la\n{size=80} Cosy Académie\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=60}" + c[0] + "\n"
        credits_s += "{size=40}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=60}Réalisé avec\n{size=40}" + renpy.version()