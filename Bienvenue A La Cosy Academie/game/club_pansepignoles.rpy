label club_pansepignoles:
    
    scene black
    image name_club_panse = Text("{size=80}Chapitre 1 :\nLe club des Cheerleaders", text_align=0.5)
    window hide
    show name_club_panse:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(2)
    hide name_club_panse
    window auto
    python:
        name_chuen = "Chuenpodo"

    #play music journeys
    scene school entrance with fade



    show Chuenpodo PoseSpeciale Sourire
    chuen "Ah [povname], c'est pour l'inscription chez les cheerleaders c'est ça ?"

    pov "Oui enfin inscription... Je suis là pour venir voir déjà, on verra ensuite."

    show Chuenpodo PoseSpeciale Sourire Rougit
    if sex=="m":
        chuen "Ah ! Mais c'est tout vu ! Une fois que tu auras posé les yeux sur eux tu seras comme... hypnotisé..."
    else:
        chuen "Ah ! Mais c'est tout vu ! Une fois que tu auras posé les yeux sur eux tu seras comme... hypnotisée..."
        
    pov "Moui admettons. Je te suis alors !"

    play music wonderful
    scene tracks with fade
    show Cheerleaders Groupe Cheer at right
    show Chuenpodo PoseSpeciale Sourire zorder 101 at full_left, mediumzoom
    
    chuen  "Et les voilà ! Nos stars du campus ! Est-ce qu'ils sont pas merveilleux ?"
    pov "Quoi mais ? Nan mais attends ils sont que trois ?"   
    chuen "Oui enfin... Momentanément quoi..."
    pov "Momentanément en attendant quoi ?"
    show Chuenpodo PoseSpeciale Triste at full_left, mediumzoom
    chuen "Que... tu les rejoignes ?"
    innerpov "Ok. Je sens le traquenard à plein nez."
    show Chuenpodo PoseSpeciale Sourire Yeuxfermes  at full_left, mediumzoom
    chuen "Ok, faut l'impressionner les gars ! Alors je te présente Clornide, Samaël et Décade, et ce sont... les Panthusiasts !"
    python:
        name_cheers = "Les Panthusiasts"
    cheers "Yeeeah !"
    show Chuenpodo PoseSpeciale Triste at full_left, mediumzoom
    clornide Cheer "Sachant que moi à la toute base j'étais plus Pansepeople..."
    show Chuenpodo PoseSpeciale Colere at full_left, mediumzoom
    decade Cheer "Ah ? Moi je trouvais que Pansepignoles c'était plus marrant..."
    samael Cheer "Ah ouais nan mais moi aussi !"
    show Chuenpodo PoseSpeciale Degoute at full_left, mediumzoom
    clornide  "Un poil vulgaire quand même non ?"
    samael "Tu trouves ?"

    show Chuenpodo PoseSpeciale Colere zorder 101 at full_left, mediumzoom 
    chuen "HEY ! CA SUFFIT OUI ? L'Académie a voté, et c'est Panthusiasts qui a gagné, c'est comme ça..."
    innerpov "Il est bien moins commode qu'il n'en a l'air..."

    clornide "Tsk... de toute façon je suis convaincu que c'est Dieuvomi qui a truqué les votes..."

    chuen "NE PARLEZ PAS COMME ÇA DE DIEUVOMI, VOUS NE CONNAISSEZ PAS SON HISTOIRE !"

    innerpov "Tiens ? Je ne les aurais pas pensé si proches..."

    chuen "ALLEZ VOUS ME FAITES TROIS TOURS DE TERRAIN ET PLUS VITE QUE ÇA !"
    show Cheerleaders at go_away
    show Chuenpodo PoseSpeciale Sourire at full_left, mediumzoom
    chuen  "Tu vois, ici, en plus de beaucoup s'amuser, on met aussi beaucoup en avant la forme physique."
    show Cheerleaders Fail at dezoom, go_left_to_right
    pov  "Je vois ça... Enfin, ils ont quand même l'air très en souffrance là !"
    show Cheerleaders Fail at dezoom, go_right_to_left
    show Chuenpodo PoseSpeciale Badboy at full_left, mediumzoom
    chuen "Meuh non ! Regarde, ils en pleurent de joie !"

    pov "Si tu le dis... Dis-moi, ça vient d'où ce nom du coup ?"
    show Chuenpodo PoseSpeciale Sourire 
    chuen "Et bien en voilà une bonne question ! C'est en hommage à notre ancien manager Pansepignon... À l'époque j'étais moi même cheerleader !"
    show Chuenpodo PoseSpeciale Sourire Yeuxfermes
    chuen "C'était un étudiant à la Cosy Académie comme nous, mais il était génial." 
    show Chuenpodo PoseSpeciale Sourire Yeuxfermes Rougit
    chuen "C'était le meilleur. Et il n'arrêtait pas de dire que c'était moi le meilleur."
    show Cheerleaders at dezoom, go_left_to_right
    pov "Une admiration réciproque on va dire..."
    show Chuenpodo PoseSpeciale Colere Rougit
    chuen "MAIS C'ÉTAIT LUI LE MEILLEUR !"
    innerpov "Tiens... ça me rappelle vaguement quelqu'un..."
    pov "Oui oui bon d'accord... et ensuite ?"
    show Chuenpodo PoseSpeciale Colere Rougit
    chuen "Non mais il faut le garder en tête. C'est lui. Bref, il était tout aussi fascinant qu'il était bavard."
    show Chuenpodo PoseSpeciale Sourire
    show Cheerleaders  at dezoom, go_right_to_left
    chuen "Insupportable selon certains. Des mauvaises langues lui demandaient souvent d'arrêter de \"spammer\". Jusqu'au jour où..."
    show Chuenpodo PoseSpeciale Triste
    chuen "Notre Pansepignon a disparu..."
    
    pov "Quoi ? Comme ça ? Pouf ?"
    show Chuenpodo PoseSpeciale Degoute
    chuen "POUF ! Après il y a des rumeurs..."
    show Cheerleaders at dezoom, go_left_to_right
    chuen "Tout le monde a entendu dire qu'un élève du nom de Von Yaourt s'était servi de son influence pour le faire bannir."
    chuen "Depuis on ne l'a plus jamais revu. Mais on essaie de le faire revenir !"

    pov "Et comment vous faites ça ?"
    
    chuen "Et bien on scande son nom bien sûr ! Du moins on essaie, je pense qu'on est maudits, ou que toute l'école est liguée contre nous..."
    show Cheerleaders at dezoom, go_right_to_left

    chuen "Tiens ! Les revoilà, attends, on va te montrer !"
    innerpov "Mais de quoi il parle..."
    pov "Oui oui allez-y montrez moi !"
    chuen "Allez les gars ! En place !"
    show Cheerleaders at go_back_in_place
    pause 1.0
    clornide Clornide Fail "Attends... moi j'en peux plus... j'ai pas l'habitude.... on fait une pause...."
    decade Decade Fail "Pareil... j'suis trop vieux pour ces bêtises..."
    show Chuenpodo PoseSpeciale Colere
    chuen "Bah quoi, vous voulez pas votre DROP ?"
    show Cheerleaders Cheer
    decade Decade Cheer "SI ! SI C'EST BON, ALLEZ GO LES MECS !"
    show Chuenpodo PoseSpeciale Sourire
    chuen "Trois, quatre et..."
    show Cheerleaders at jumping
    cheers "P{p=1.0}{nw}" 
    
    show Cheerleaders at jumping
    cheers "A{p=1.0}{nw}"
    
    show Cheerleaders at jumping
    cheers "N{p=1.0}{nw}"
    

    show Medoc Standard Sourire zorder 105:
        xpos 0.9 xanchor 1.0 ypos 2.0 yanchor 1.0 zoom 1.3
        linear .5 ypos 1.3
    pause .2

    show Cheerleaders Fail  with hpunch 
    show Chuenpodo PoseSpeciale Colere
    pause .3
    show Cheerleaders Fail at shade_transform
    med "Hey salut [povname], tiens Chuenpodo, qu'est-ce que tu fais là ?"


    cheers "NOOOOOOON !!!!"
    show Chuenpodo PoseSpeciale Triste
    chuen "MAIS C'EST PAS POSSIBLE !!!!"
    show Medoc PoseGauche Gene
    med "Oula ! Ils ont l'air tendus... Bon, bah je m'éclipse hein ! À plus tard !"
    show Medoc at go_away_interrupt
    pause 1.5
    show Chuenpodo PoseSpeciale Colere
    show Cheerleaders Fail at normalalpha
    hide Medoc

    chuen "C'EST TOUJOURS COMME ÇA ! TOUJOURS !"
    decade Decade Fail "Ouais, on en a marre... On en a besoin de ce DROP..."
    show Chuenpodo PoseSpeciale Colere Rougit
    chuen "SI VOUS Y ARRIVEZ UN JOUR ! ALLEZ ON REPREND !!"
    show Chuenpodo PoseSpeciale Sourire
    show Cheerleaders Cheer at jumping
    cheers "P{p=1.0}{nw}"
    

    show Chuenpodo PoseSpeciale Sourire Rougit



    show Cheerleaders at jumping
    cheers "A{p=1.0}{nw}"
    
    show Chuenpodo PoseSpeciale Sourire Yeuxfermes

    show Cheerleaders at jumping
    cheers "N{p=1.0}{nw}"

    show Chuenpodo PoseSpeciale Sourire Yeuxfermes Rougit
    show Cheerleaders at jumping
    cheers "S{p=1.0}{nw}"

    show Chuenpodo PoseSpeciale Yeuxfermes Rougit
    show Cheerleaders at jumping
    cheers "E{p=1.0}{nw}"

    show Chuenpodo PoseSpeciale Sourire Rougit
    show Cheerleaders at jumping
    cheers "P{p=1.0}{nw}"


    show Metalice Standard Cligne zorder 120:
        xpos 0.9 xanchor 1.0 ypos 2.0 yanchor 1.0 zoom 1.3
        linear .5 ypos 1.3

    pause .2
    show Cheerleaders Fail with hpunch
    show Chuenpodo PoseSpeciale Colere
    pause .3
    show Cheerleaders Fail at shade_transform
    met "Coucou ! Ça va les Pansepignoles, ça avance votre invocation ?"

    python:
        name_cheers = "Les Pansepignoles"

    innerpov "Hein ?"

    cheers "NOOOOOOOOOOOON !!!!!"

    show Chuenpodo PoseSpeciale Triste
    chuen "J'EN PEUX PLUS ! REVIENS PANSE !!!!"

    show Chuenpodo PoseSpeciale Colere
    chuen "ALLEZ LES GARS 5 TOURS DE TERRAIN, ET JE VOUS SUIS CETTE FOIS !"

    samael Samael Fail "Pitié..."
    clornide Clornide Fail "Pas encore..."
    decade Decade Fail "Mes vieux os..."
    show Chuenpodo PoseSpeciale Badboy
    chuen "ALLEZ ON Y VA !"
    show Cheerleaders Fail at normalalpha
    show Metalice at shade_transform
    show Cheerleaders at go_away
    show Chuenpodo at go_away_chuen
    pause 2.0
    hide Cheerleaders
    hide Chuenpodo
    show Metalice at normalalpha

    pov "Tiens salut Metalice, tu veux pas venir me secourir ?"

    show Metalice Standard Sourire
    met "Ahahah, et bien quoi il te plaît pas ce club ?"

    pov "Non, ils sont carrément bizarres... Dis, c'est quoi cette histoire d'invocation ?"
    show Metalice Standard Cligne
    met "T'as bien vu qu'ils n'arrivent jamais à épeler Pansepignon correctement sans être interrompus ?"

    pov "Oui Chuenpodo m'a même dit qu'ils devaient être maudits !"
    show Metalice Standard Sourire
    met "Exactement ! Et ce n'était pas une façon de parler... Ces types pensent vraiment qu'ils sont maudits !"

    pov "Sans rire ?"
    show Metalice PoseSpeciale Cligne
    met "Je te jure ! Leur local est flippant !"
    met "Du coup ils sont convaincus que s'ils arrivent à scander Pansepignon jusqu'au bout, ils pourront l'invoquer."
    show Metalice PoseSpeciale Gene
    met "Chuen a vraiment mal vécu sa disparition..."

    pov "Mais, ce Pansepignon, il n'est pas mort ?"
    show Metalice Standard Sourire
    met "Pas aux dernières nouvelles..."

    pov "Bah ils veulent l'invoquer d'où alors ?"

    show Metalice Standard Cligne
    met "Qui sait ?"

    pov "Bah EUX ! Enfin j'espère !"

    show Metalice PoseGauche Sourire Yeuxfermes
    met "Ahah, je pense que tu vas aller de surprise en surprise ici. "

    pov "Bon je raye les cheerleaders alors, une autre proposition ?"

    
    show Metalice Standard Sourire
    met "Hmmmm je ne sais pas... Tu aimes l'humour ?"

    pov "Oui, comme tout le monde je suppose."
    show Metalice PoseSpeciale Cligne
    met "Bon... laissons le club de comédie de côté alors."

    pov "Quoi ! Mais si ! J'ai bien envie d'aller y faire un tour moi !"
    show Metalice Standard Sourire
    met "Très bien, alors suis-moi, mais je te préviens, je ne mettrai pas les pieds dans cet endroit !"

    pov "Je te suis !"


    jump club_comedie
    return

