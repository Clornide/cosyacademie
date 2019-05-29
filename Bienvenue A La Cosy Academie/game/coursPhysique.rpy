label cours_physique:
    
    scene school hallway with fade
    play music extrapolation
    window auto
    

    show Pansepignon PoseSpeciale Sourire with dissolve
    pov "HEP TOI LA BAS !"   
    pov "Je te reconnais, je t'ai croisé à l'entrée je ne sais plus quand..."
    panse "Effectivement, tu as bonne mémoire !"
    pov "Tu es Pansepignon n'est-ce pas ?"
    show Pansepignon PoseSpeciale Gene
    panse "Oh... Je vois qu'on t'a déjà parlé de ce jeune génie incompris..."
    show Pansepignon PoseSpeciale Sourire Yeuxfermes
    panse "Si dans ton coeur, c'est ce que tu ressens, alors oui. Je suis Pansepignon."
    innerpov "Ok... c'est complètement lui..."
    $ name_panse = "Pansepignon"
    panse "Mais tu sais, son histoire est bien plus compliquée qu'on ne le Panse."
    show Pansepignon PoseSpeciale Cligne
    panse "Pignon."
    pov "..."
    panse "Bref. J'ai à faire ! Faut que je file !"
    pov "Attends ! Qu'est-ce-que tu fais ici ? Que cherches-tu à accomplir ?"
    show Pansepignon PoseSpeciale Degoute
    panse "La... vengeance..."
    pov "Nan, mais en vrai ?"
    show Pansepignon PoseSpeciale Triste
    panse "En vrai ? J'ai perdu un truc dans l'école, j'aimerais bien le retrouver..."
    pov "Ah c'est tout ? Je peux peut-être t'aider du coup, tu cherches quel genre de truc ?"
    show Pansepignon PoseSpeciale Gene
    panse "Mon... Innocence..."
    pov "..."
    panse "Nan, c'est un p'tit disque, que j'avais ramené à un ami, il doit être dans le coin !"
    panse "Allez, je file vraiment cette fois ! Bon courage pour la suite !"
    hide Pansepignon with dissolve
    innerpov "Bon c'est pas tout ça mais je vais être en retard pour le cours de physique..."
    scene classroom with fade

    
    

    show Dieuvomi BrasCroises Badboy at left
    dieuv "Ouah le prof est pas là !"
    
    show Metalice PoseSpeciale Degoute at right
    
    met "Quoi ??"
    
    show Metalice PoseSpeciale Cligne Rougit
    met "J'aime tellement la physique..."

    show Dieuvomi BrasCroises Badboy

    dieuv "Ben s'il est pas là, je m'en vais !"

    show Foulk Standard Colere

    foulk "Normalement il faut attendre 15 min !"
    foulk "Et de toute façon, c'est le prof qui a les clés, on est coincés ici..."    

    show Dieuvomi BrasCroises Badboy
    
    dieuv "Pfft..."
    dieuv "Ben moi, je veux me tirer d'ici !"

    innerpov "Quel rebelle ce Dieuvomi !"

    show Dieuvomi BrasCroises Colere
    dieuv "Allez medoc, va demander si le prof est là !"    
    hide Dieuvomi with dissolve
    hide Foulk with dissolve
    hide Metalice with dissolve


    play music haunted fadein 1.0

    show Medoc Standard Sourire
    med "Bon ok..."
    med "Alors..."
    show Medoc Standard Sourire Yeuxfermes
    med "Esprism... es-tu là ?"
    med "Kr kr krr"
    play sound woosh
    hide Medoc
    show Esprism:
     xpos 0.1 xanchor 0.0 ypos .8 yanchor 1.0
    with flash   
    esprism "Mais oui Je suis là !" with hpunch
    esprism "Asseyez-vous !"

    stop music fadeout 1.0
    play music wonderful

    esprism "Je fais l'appel..."    
    show Esprism:
        xpos 0.0 xanchor 0.0 ypos .8 yanchor 1.0

    show Medoc PoseDroite Sourire at right
    show Moguri PoseDroite Sourire behind Esprism

    esprism "Je vois Medoc et Moguri qui font les pitres là derrière..."
    hide Medoc
    hide Moguri
    esprism "Dieuvomi et Foulk ?"

    show Dieuvomi PoseDroite Sourire at right
    show Foulk PoseDroite Sourire behind Esprism
    dieuv "Ouais !" 
    foulk "Présent cong !"

    esprism "Caro ?" 

    hide Dieuvomi
    hide Foulk
    show Caro PoseDroite Sourire at right       
    caro "Présente !"
    show din PoseDroite Sourire behind Esprism with dissolve
    esprism "Et son amie din à côté, très bien..." 
    
    
    esprism "Mathilde ?" 
    hide Caro
    hide din


    if name_mathilde == "???":
        python:
            name_mathilde = "Mathilde"
        show Mathilde PoseDroite Sourire at right
        mat "Présente !"
        esprism "Ha Mathilde, je ne pourrai pas venir à ton club ce soir..."
        show Mathilde PoseDroite Triste at right
        esprism "Même si c'est facile, je n'ai pas terminé ma nouvelle théorie des jeux..."
        innerpov "Un club de jeux ? Il faudra que j'aille faire un tour là-bas si je ne trouve rien d'autre !"
        hide Mathilde

    esprism "[povname] ?"
    
    if sex=="m":
        pov "Heuu présent !"
    else:
        pov "Heuu présente !"
    
    esprism "Ha, [povname], je vois que ta fiche n'est pas complète !"
    esprism "Va au secrétariat de suite !"
    innerpov "Argh !"

    jump club_tech
    return
