label intro:
    play music journeys
    
    scene school entrance with fade

    innerpov "OK."
    innerpov "C'est une journée comme les autres."
    innerpov "Aucun enjeu particulier."
    pov "Souffle."
    innerpov "Certes, c'est une académie d'élite, et je ne croiserai que les plus grands de ce pays."
    innerpov "Mais si je suis là, c'est que je l'ai mérité, non ?"
    innerpov "Personne ne me jugera, ils sont tous passés par là."
    innerpov "C'est une journée comme les autres."
    innerpov "..."
    innerpov "Je sais que c'est un mensonge."
    innerpov "C'est ma première journée à la Cosy Académie, un tournant dans ma vie."
    innerpov "Si je me plante je peux tout foutre en l'air..."
    innerpov "..."
    pov "Aaaaargh mais qu'est ce que je fais ic- !!"


    show Moguri Standard Badboy
    with flash

    noName "BOOONG!!!!!"  with hpunch

    pov "Hey !! Mais ça va pas de foncer dans les gens comme ç- !?"

    innerpov "Oh non...."
    innerpov "C'est Moguri..."
    innerpov "Mais s'il est ici, ça veut dire que..."

    hide Moguri
    show Medoc Standard Badboy
    with flash

    noName "BOOONG!!!!!" with hpunch


    show Moguri Standard Badboy at right
    show Medoc Standard Badboy at left

    innerpov "C'est pas vrai..."
    innerpov "Medoc et Moguri. Dès mon premier jour, je tombe sur eux."
    innerpov "Littéralement en plus."
    innerpov "Moi qui voulais faire une rentrée à peu près discrète, c'est râpé."

    show Medoc Standard Degoute at left

    med "Dis donc, tu comptes nous fixer longtemps, comme ça ?"
    pov "Je... Non, bien sûr, excusez-moi, c'est juste que..."

    show Moguri BrasCroises Sourire at right

    if sex=="m":
        mog "Ahahah mais enfin Medoc, laisse-le ! Regarde comme il a l'air stressé !"
    else:
        mog "Ahahah mais enfin Medoc, laisse-la ! Regarde comme elle a l'air stressée !"

    show Moguri Standard Sourire at right



    if sex=="f":
        mog "Bienvenue à la Cosy Académie, gamine. Ne t'inquiète pas, on n'est pas tous aussi bourrus que lui !"
        innerpov "Je suis presque sûre qu'on a le même âge, mais le fait qu'il m'appelle gamine ne me déplaît pas particulièrement."
        pov "Aaaah, merci... Je tâcherai de me faire plus discrète, désolée !"
        mog "Mais non enfin ! Si tu es ici, c'est que tu as ta place. Aucune raison de se faire discrète !"
    else:
        mog "Bienvenue à la Cosy Académie, gamin. Ne t'inquiète pas, on n'est pas tous aussi bourrus que lui !"
        innerpov "Je suis presque sûr qu'on a le même âge, mais le fait qu'il m'appelle gamin ne me déplaît pas particulièrement."
        pov "Aaaah, merci... Je tâcherai de me faire plus discret, désolé !"
        mog "Mais non enfin ! Si tu es ici, c'est que tu as ta place. Aucune raison de se faire discret !"



    show Moguri BrasCroises Sourire at right

    mog "Sur ce... On va y aller, il ne s'agirait pas d'arriver en retard ! À plus tard p'tite tête !"

    hide Moguri with dissolve
    pause 0.5
    hide Medoc
    show Medoc Standard Degoute with dissolve

    med "Tch."
    med "Moguri a raison. Tout le monde n'est pas aussi bourru que moi..."
    med "Mais attention."
    show Medoc Standard Degoute at bigzoom

    med "Tout le monde n'est pas aussi indulgent que lui..." with vpunch

    pov "Gloups."

    pov "Ouch... Près... Très près. Trop près ?"
    pov "Pas vraiment."

    show Medoc Standard Degoute at normalzoom
    med "Allez. Fais attention à toi."

    hide Medoc with dissolve

    pov "Ouf."
    pov "Ok, ça commence fort."
    pov "Même de dos ils sont impressionnants..."
    pov "Aller, ça va le faire ! On y va !"

    window hide

    show intro at truecenter
    with animintro

    pause 3

    jump Meeting_Metalice

    return
