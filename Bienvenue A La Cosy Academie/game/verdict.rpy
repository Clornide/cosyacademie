label verdict:
    play music wonderful

    scene black
    image name_verdict = Text("{size=80}Chapitre Final :\nLe Verdict", text_align=0.5)
    window hide
    show name_verdict:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(2)
    hide name_verdict
    window auto


    scene bar with fade
   
    show Moguri PoseGauche Sourire Yeuxfermes at left
    show Medoc PoseDroite Sourire Yeuxfermes at right
    mog "Bon ben nickel alors Medoc, on se revoit dans deux semaines, et d'ici là tu fais quoi ?"
    med "Oh j'vais essayer de rester..."
    mog "Ouais ?"
    med "Bah allez, on a qu'à dire Cosy !"    
    mog "Et bah on part sur ça alors !"
    mog "Et... Hop ! C'est coupé !"
    
    pov "C'était.... PHENOMENAL !"

    mog "Ahahah !"
    med "Arrête tu vas nous faire rougir !"

    pov "Non mais vraiment ! Vous avez vraiment une alchimie digne des plus grands !"

    med "Mais tu sais... Si tu rejoins ce club, tu pourras faire partie de cette alchimie."
    pov "Vraiment ? Je peux ? Je veux dire, vous avez l'air si proches ! Et il n'y a que deux personnes dans ce club, je voudrais pas ruiner ça..."

    mog "Tu sais, si on te propose, c'est qu'on a senti qu'il y avait quelque chose de spécial..."

    innerpov "Tsss, si tu savais..."

    pov "Ok, donc c'est officiel, je fais parti du Cosy Culture Club ?"
    med "C'est officiel !"
    pov "J'y crois pas... La Cosy Academy... Le Cosy Culture Club..."

    if sex=="m":
        mog "Il va falloir commencer à réaliser mon grand !"
        innerpov "Ahaha... Je suis passé de 'gamin' à 'mon grand', ça fait plaisir..."
    else:
        mog "Il va falloir commencer à réaliser ma grande !"
        innerpov "Ahaha... Je suis passé de 'gamin' à 'mon grand', ça fait plaisir..."
    med "Bon, alors on se dit à dans deux semaines ?"
    mog "A dans deux semaines !"

    hide Moguri
    hide Medoc
    with dissolve

    if pointsmedoc > pointsmoguri and pointsmedoc > pointsincel:
        
        innerpov "Non... Pas maintenant... Pas après tout ça...."
        pov "MEDOC ! ATTENDS !"


    elif pointsmoguri > pointsmedoc and pointsmoguri > pointsincel:
        innerpov "Non... Pas maintenant... Pas après tout ça...."
        pov "MOGURI ! ATTENDS !"      

    else:
    
        pov "BON !"
        pov "Ben ça c'est fait !"
        pov "Ouaip..."
        if sex=="m":
            pov "Je m'sens un peu seul du coup..."
        else:
            pov "Je m'sens un peu seule du coup..."
        pov "Tiens, j'avais pas vu toutes ces tireuses là..."
        pov "Elles marchent ?"
        pov "OUAH ELLES MARCHENT !"
        pov "Après c'est peut être un peu pitoyable de boire tout seul..."
        pov "Déjà que je parle tout seul depuis 2-3 minutes..."
        pov "Après, j'ai recontré pas mal de gens depuis que je suis arrivé !"
        pov "J'ai qu'à les inviter à boire un coup ici !"
        pov "Un p'tit Dieuvomi, un Foulk, peut être un VonYaourt..."
        pov "J'peux inviter tout le monde en fait, je suis un membre à part entière du Cosy Culture Club !"
        pov "Boire des coups fait partie du concept en plus !"
        pov "Bon j'vais les chercher alors !"

        with longfade

        show Von PoseDroite Sourire Yeuxfermes at right
        show Foulk PoseGauche Sourire Yeuxfermes at left 
        with dissolve

        pause 1

        hide Von
        hide Foulk
        with dissolve

        show Pansepignon PoseDroite Sourire Yeuxfermes Rougit at right
        show Chuenpodo PoseGauche Sourire Yeuxfermes Rougit at left

        with dissolve

        hide Chuenpodo
        hide Pansepignon
        
        with dissolve

        show Caro Pose



    jump credits
    return
