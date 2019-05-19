label lendemainMatin:
    scene black with longfade

    
    image name_lendemain = Text("{size=80}Le Lendemain matin...", text_align=0.5)
    window hide
    show name_lendemain:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(2)
    hide name_lendemain
    window auto

    scene school entrance with longfade

    if sex=="m":
       innerpov "Alors... Il faut que j'aille voir les cheerleaders ce matin. Mieux vaut attendre Chuenpodo, je ne suis pas encore très familier des locaux de l'école, j'ai pas envie de me perdre..."
    else:
       innerpov "Alors... Il faut que j'aille voir les cheerleaders ce matin. Mieux vaut attendre Chuenpodo, je ne suis pas encore très familière des locaux de l'école, j'ai pas envie de me perdre..."
  
    innerpov "Ah le voilà !"
    jump club_pansepignoles
