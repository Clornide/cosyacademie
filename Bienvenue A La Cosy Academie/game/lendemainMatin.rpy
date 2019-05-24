label lendemainMatin:
    play music skyward
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

    pov "Huff... huff... j'ai failli arriver en retard pour mon deuxième jour à l'Académie."
    pov "Franchement, c'est pas sérieux..."
    
    panse "Tout va bien, tu as encore quelque minutes avant d'être vraiment en retard !"
    
    show Pansepignon PoseSpeciale Sourire
    
    panse "Tu devrais surement te dépécher, tu sais !"
    
    pov "Ah merci ! Je ne crois pas t'avoir déjà croisé, t'es élève à l'Académie ?"
    
    show Pansepignon PoseSpeciale Degoute
    
    panse "..."
    panse "On peut voir ça comme ça."
    
    show Pansepignon PoseSpeciale Sourire
    
    panse "Tu n'as qu'à me voir comme une espèce de mascotte du cœur de l'école !"
    
    pov "C'est... hyper vague."
    panse "Tu en apprendras sûrement plus bientôt, ne t'inquiète pas !"
    panse "Tu devrais te dépécher, je crois que tu as rendez-vous avec la meilleure personne de cette établissement."
    panse "Allez, bye !"
    
    hide Pansepignon with dissolve
    
    pov "Quoi ? Nan mais attends !"
    pov "Wow, il était carrément bizarre ce type..."

    if sex=="m":
       innerpov "Bref... il faut que j'aille voir les cheerleaders ce matin. Mieux vaut attendre Chuenpodo, je ne suis pas encore très familier des locaux de l'école, j'ai pas envie de me perdre..."
    else:
       innerpov "Bref... il faut que j'aille voir les cheerleaders ce matin. Mieux vaut attendre Chuenpodo, je ne suis pas encore très familière des locaux de l'école, j'ai pas envie de me perdre..."
  
    innerpov "Ah le voilà !"
    jump club_pansepignoles
