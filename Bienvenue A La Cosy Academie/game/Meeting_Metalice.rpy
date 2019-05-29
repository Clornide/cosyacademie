label Meeting_Metalice:
    scene school hallway with fade

    window show

    innerpov "Bon. Classe 104, classe 104..."
    innerpov "Ah voilà !"
    innerpov "Bon ben on y va alors !"

    if sex=="m":
        inc "Hep toi, le nouveau là-bas !"
    else:
        inc "Hep toi, la nouvelle là-bas !"

    show Metalice PoseSpeciale Sourire Yeuxfermes with dissolve

    met "Ah, salut ! C'est bien [povname] c'est ça ? Moi c'est Metalice !"

    show Metalice PoseSpeciale Sourire

    met "J'ai été désignée pour être ta marraine à ton arrivée, donc si tu as la moindre question, n'hésite pas !"

    if sex=="m":
        pov "Enchanté Metalice ! Je m'en remets à toi alors. "
    else:
        pov "Enchantée Metalice ! Je m'en remets à toi alors."

    met "Alors, tu as pu faire connaissance avec quelques personnes ? J'ai vu que tu discutais avec Medoc et Moguri à l'entrée."
    met "Tu ferais bien de te méfier de ces deux gaillards. Ils pensent que rien ni personne ne leur résiste."

    show Metalice Standard Yeuxfermes

    met "Et au vu de ta réaction, ils ont déjà fait forte impression sur toi apparemment, ahaha !"

    show Metalice Standard Sourire

    if sex=="m":
        pov "Q-quoi ? Non pas du tout, ils m'ont juste surpris tout à l'heure, rien de plus !"
    else:
        pov "Q-quoi ? Non pas du tout, ils m'ont juste surprise tout à l'heure, rien de plus !"

    show Metalice PoseSpeciale Cligne

    met "Oh arrête, pas à moi hein ! Je suis là pour te donner TOUTES sortes de conseils."
    innerpov "Très subtil ce clin d'oeil..."

    show Metalice Standard Sourire

    met "Alors, t'as flashé sur lequel ?"

    menu:

        met "{cps=0}Alors, t'as flashé sur lequel ?{/cps}"

        "Medoc et son air breu-som...":
            python:
                pointsmedoc+=1

        "Moguri, il a l'air si doux et gentil...":
            python:
                pointsmoguri+=1

        "Mais personne je te dis !!":
            python:
                pointsincel+=1

    if pointsmedoc!=0:
        show Metalice Standard Sourire Yeuxfermes

        met "Ah ! C'est vrai qu'il impressionne beaucoup de gens, mais il ne faut pas se laisser avoir, il se fait plus dur qu'il ne l'est vraiment !"
        pov "Ah bon ?"

        show Metalice Standard Sourire

        met "Il réagit surtout comme ça avec les gens qu'il apprécie. Il est plus protecteur qu'autre chose finalement !"
        show Metalice PoseSpeciale Cligne
        met "Tu ne l'as pas entendu de moi, hein !"
        show Metalice Standard Sourire
        pov "Et... Tu penses qu'il y aura moyen ?"
        if sex=="m":
            met "Et bien ! Je te trouve bien ambitieux pour tes premières heures à la Cosy Académie."
        else:
            met "Et bien ! Je te trouve bien ambitieuse pour tes premières heures à la Cosy Académie."
        pov "Non ! Ce n'est pas ce que je voulais dire. Enfin..."

        show Metalice PoseSpeciale Cligne

        met "Ne t'en fais pas, je vois très bien ce que tu veux dire !"
        innerpov "Encore ce clin d'oeil..."

        show Metalice Standard Sourire

        if sex=="m":
            met "Enfin bon ce ne sont pas les seuls étudiants de ce lycée, aucune raison de rester bloqué sur ces deux-là !"
        else:
            met "Enfin bon ce ne sont pas les seuls étudiants de ce lycée, aucune raison de rester bloquée sur ces deux-là !"

    elif pointsmoguri!=0:
        show Metalice PoseSpeciale Sourire Yeuxfermes

        met "Moguri ? Doux et gentil ? Il est plus du genre à juger les gens d'habitude. Tu as du lui taper dans l'oeil !"
        show Metalice Standard Sourire
        pov "Quoi ? V-vraiment ?"
        show Metalice PoseSpeciale Cligne
        met "Ahaha, oui vraiment ! Tu apprendras que je suis l'une des sources d'informations les plus fiables de l'école, tu peux me faire confiance !"
        show Metalice Standard Sourire
        pov "D'accord, merci ! Du coup, tu penses que... Enfin qu'il y a moyen quoi ?"
        if sex=="m":
            met "Et bien ! Je te trouve bien ambitieux pour tes premières heures à la Cosy Académie."
        else:
            met "Et bien ! Je te trouve bien ambitieuse pour tes premières heures à la Cosy Académie."
        pov "Non ! Ce n'est pas ce que je voulais dire. Enfin..."
        show Metalice Standard Cligne
        met "Ne t'en fais pas, je vois très bien ce que tu veux dire !"
        innerpov "Encore ce clin d'oeil..."
        show Metalice Standard Sourire
        if sex=="m":
            met "Enfin bon ce ne sont pas les seuls étudiants de ce lycée, aucune raison de rester bloqué sur ces deux-là !"
        else:
            met "Enfin bon ce ne sont pas les seuls étudiants de ce lycée, aucune raison de rester bloquée sur ces deux-là !"

    elif pointsincel!=0:

        show Metalice Standard Triste

        met "Mouais ! Si tu le dis..."

        show Metalice Standard Sourire

        if sex=="m":
            met "Enfin bon tu as raison, ce ne sont pas les seuls étudiants de ce lycée. Aucune raison de rester bloqué sur ces deux-là !"
        else:
            met "Enfin bon tu as raison, ce ne sont pas les seuls étudiants de ce lycée. Aucune raison de rester bloquée sur ces deux-là !"


    pov "D'ailleurs, ce serait possible de me présenter rapidement à d'autres élèves ?"

    show Metalice PoseSpeciale Sourire Yeuxfermes

    met "Bien sûr ! Mais pas là, on va arriver en retard, allons-y !"

    jump Premiercours

    return
