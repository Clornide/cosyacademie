label Meeting_Metalice:
    scene couloir with fade

    window show

    "Bon. Classe 103, classe 103..."
    "Ah voilà !"
    "Bon ben on y va alors !"

    if sex=="m":
        inc "Hep toi, le nouveau là-bas !"
    else:
        inc "Hep toi, la nouvelle là-bas !"

    show metalice coucou fermes with fade

    met "Ah, salut ! C'est bien [povname] c'est ça ? Moi c'est Metalice !"

    show metalice coucou

    met "J'ai été désignée pour être ta marraine à ton arrivée, donc si tu as la moindre question, n'hésite pas !"

    if sex=="m":
        pov "Enchanté Metalice ! Je m'en remets à toi alors. "
    else:
        pov "Enchantée Metalice ! Je m'en remets à toi alors."

    met "Alors, tu as pu faire connaissance avec quelques personnes ? J'ai vu que tu discutais avec Medoc et Moguri à l'entrée."
    met "Tu ferais bien de te méfier de ces deux gaillards. Ils pensent que rien ni personne ne leur résiste."

    show metalice coucou fermes

    met "Et au vu de ta réaction, ils ont déjà fait forte impression sur toi apparemment, ahaha !"

    show metalice coucou

    if sex=="m":
        pov "Q-quoi ? Non pas du tout, ils m'ont juste surpris tout à l'heure, rien de plus !"
    else:
        pov "Q-quoi ? Non pas du tout, ils m'ont juste surprise tout à l'heure, rien de plus !"

    show metalice coucou clindoeil

    met "Oh arrête, pas à moi hein ! Je suis là pour te donner TOUTES sortes de conseils."
    innerpov "Très subtil ce clin d'oeil..."

    show metalice coucou

    met "Alors, t'as flashé sur lequel ?"

    menu:

        met "Alors, t'as flashé sur lequel ?"

        "Medoc et son air bre-som...":
            python:
                pointsmedoc+=1

        "Moguri, il a l'air si doux et gentil...":
            python:
                pointsmoguri+=1

        "Mais personne je te dis !!":
            python:
                pointsincel+=1

    if pointsmedoc!=0:
        show metalice coucou fermes

        met "Ah ! C'est vrai qu'il impressionne beaucoup de gens, mais il ne faut pas se laisser avoir, il se fait plus dur qu'il ne l'est vraiment !"
        pov "Ah bon ?"

        show metalice coucou

        met "Il réagit surtout comme ça avec les gens qu'il apprécie. Il est plus protecteur qu'autre chose finalement !"
        show metalice coucou clindoeil
        met "Tu ne l'as pas entendu de moi, hein !"
        show metalice coucou
        pov "Et... Tu penses qu'il y aura moyen ?"
        if sex=="m":
            met "Et bien ! Je te trouve bien ambitieux pour tes premières heures à la Cosy Académie."
        else:
            met "Et bien ! Je te trouve bien ambitieuse pour tes premières heures à la Cosy Académie."
        pov "Non ! Ce n'est pas ce que je voulais dire. Enfin..."

        show metalice coucou clindoeil

        met "Ne t'en fais pas, je vois très bien ce que tu veux dire !"
        innerpov "Encore ce clin d'oeil..."

        show metalice coucou

        if sex=="m":
            met "Enfin bon ce ne sont pas les seuls étudiants de ce lycée, aucune raison de rester bloqué sur ces deux là !"
        else:
            met "Enfin bon ce ne sont pas les seuls étudiants de ce lycée, aucune raison de rester bloquée sur ces deux là !"

    elif pointsmoguri!=0:
        show metalice coucou fermes

        met "Moguri ? Doux et gentil ? Il est plus du genre à juger les gens d'habitude. Tu as du lui taper dans l'oeil !"
        show metalice coucou
        pov "Quoi ? V-vraiment ?"
        show metalice coucou clindoeil
        met "Ahaha, oui vraiment ! Tu apprendras que je suis l'une des sources d'informations les plus fiables de l'école, tu peux me faire confiance !"
        show metalice coucou
        pov "D'accord, merci ! Du coup, tu penses que... Enfin qu'il y a moyen quoi ?"
        if sex=="m":
            met "Et bien ! Je te trouve bien ambitieux pour tes premières heures à la Cosy Académie."
        else:
            met "Et bien ! Je te trouve bien ambitieuse pour tes premières heures à la Cosy Académie."
        pov "Non ! Ce n'est pas ce que je voulais dire. Enfin..."
        show metalice coucou clindoeil
        met "Ne t'en fais pas, je vois très bien ce que tu veux dire !"
        innerpov "Encore ce clin d'oeil..."
        show metalice clindoeil
        if sex=="m":
            met "Enfin bon ce ne sont pas les seuls étudiants de ce lycée, aucune raison de rester bloqué sur ces deux là !"
        else:
            met "Enfin bon ce ne sont pas les seuls étudiants de ce lycée, aucune raison de rester bloquée sur ces deux là !"

    elif pointsincel!=0:

        show metalice decue

        met "Mouais ! Si tu le dis..."

        show metalice coucou

        if sex=="m":
            met "Enfin bon tu as raison, ce ne sont pas les seuls étudiants de ce lycée. Aucune raison de rester bloqué sur ces deux là !"
        else:
            met "Enfin bon tu as raison, ce ne sont pas les seuls étudiants de ce lycée. Aucune raison de rester bloquée sur ces deux là !"


    pov "D'ailleurs, ce serait possible de me présenter rapidement à d'autres élèves ?"

    show metalice coucou fermes

    met "Bien sûr ! Mais pas là, on va arriver en retard, allons-y !"

    jump Premiercours

    return

