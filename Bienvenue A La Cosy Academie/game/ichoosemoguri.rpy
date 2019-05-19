label Ichoosemoguri:
    scene school hallway with longfade

    innerpov "Ca commence à faire un petit bout de temps que je l'attends, il ne devrait plus tarder..."
    innerpov "Je crois que je l'entends d'ailleurs, mais il a l'air de discuter avec quelqu'un."

    mog "Et donc ?"
    inc "Et bien là je lui ai dit, 'QUOI !? JEUDICOUVERTE !?'. C'était hilarant !"
    mog "Oui enfin, comme à ton habitude quoi... Tu devrais peut être arrêter de le taquiner avec ça, un jour il pourrait mal le prendre."
    inc "Ahahah mais non, tout le monde sait que Dieuvomi et moi, c'est pour la vie !"

    innerpov "Ah, je les vois !"
    python:
        name_chuen="???"
    show Moguri BrasCroises Degoute at left
    show Chuenpodo Standard Sourire Yeuxfermes at right
    with dissolve
    pause 0.5
    show Moguri Standard Sourire
    chuen "Tiens, [povname] c'est bien ça ? Que fais-tu encore ici ?"
    pov "Et bien je... Enfin j'aurais voulu discuter avec Moguri !"
    show Chuenpodo BrasCroises Sourire at right
    chuen "Ohoh ! Pas mal de succès Moguri à ce que je vois..."
    show Moguri Standard Sourire Yeuxfermes
    if sex=="m":
        mog "Ahahah arrête de le taquiner, regarde comme il rougit !"
    else:
        mog "Ahahah arrête de la taquiner, regarde comme elle rougit !"
    show Moguri Standard Sourire
    mog "D'ailleurs je crois que tu ne connais pas Chuen ?"
    pov "Euh non, effectivement..."
    mog "Et bien je te présente Chuenpodo, l'élève le plus brillant de notre Académie !"
    python:
        name_chuen="Chuenpodo"    
    show Chuenpodo Standard Sourire Rougit
    chuen "Ahahah mais arrête enfin Moguri..."
    show Moguri BrasCroises Sourire
    mog "Il est aussi manager de l'équipe de cheerleaders de l'école, donc si tu veux l'intégrer, il faudra te présenter à lui."
    show Chuenpodo Standard Sourire
    chuen "Effectivement, je te les présenterai demain après les cours si ça t'intéresse."
    pov "Avec plaisir !"
    show Moguri Standard Sourire
    mog "Parfait ! Donc tu voulais me parler de quelque chose ?"
    pov "Oui... Enfin si ça ne te dérange pas."
    show Moguri Standard Sourire Yeuxfermes
    mog "Bien sûr que non !"
    show Chuenpodo Standard Sourire Yeuxfermes
    chuen "Bon, et bien je vais y aller alors ! Bon courage [povname]."
    pov "Bon courage ?"
    chuen "Et à demain !"
    hide Chuenpodo with dissolve
    hide Moguri
    show Moguri Standard Sourire Yeuxfermes with dissolve
    mog "Je peux te raccompagner chez toi si tu veux, on discutera sur le chemin ?"
    pov "Allons-y !"

    scene street day with longfade

    show Moguri Standard Sourire with dissolve

    mog "Tu voulais me parler de quelque chose donc ?"
    pov "Je voulais juste te remercier de m'avoir défendu tout à l'heure."

    show Moguri BrasCroises Badboy

    mog "Sans vouloir paraître désagréable, je ne suis pas vraiment intervenu pour toi..."
    mog "Je sais très bien que ce genre de comportement agace Medoc, j'ai voulu désamorcer la situation avant que ça ne dégénère."

    show Moguri BrasCroises Degoute

    mog "A vrai dire ton comportement m'énerve un peu aussi, mais je ne peux pas y faire grand chose, le changement doit venir de toi, pas des autres."

    if sex=="m":
        pov "D-désolé..."
    else:
        pov "D-désolée..."

    show Moguri BrasCroises Colere

    mog "Tu vois, tu recommences !"
    show Moguri BrasCroises Triste

    mog "Tu fais partie de la Cosy Académie maintenant, il faut arrêter de s'écraser comme ça..."
    mog "Il va falloir changer. Je comprends que le début soit compliqué pour toi, mais sache que ton comportements affecte d'autres personnes."

    show Moguri Standard Badboy
    mog "Et ça, je ne peux pas l'accepter."
    mog "Je te laisse."

    hide Moguri with dissolve

    innerpov "Je ne peux pas le laisser partir... Pas maintenant."

    pov "MOGURI ! ATTENDS !!"

    show Moguri Standard Badboy with dissolve

    pov "Je veux changer... Vraiment ! Mais je pense qu'il va me falloir de l'aide..."
    pov "Et si possible, j'aimerais que la personne qui m'aide... Ce soit toi."

    show Moguri Gene

    mog "M-moi ?"
    innerpov "Tiens, je ne m'attendais pas à cette réaction..."

    show Moguri BrasCroises Badboy Rougit

    mog "Je ne suis peut être pas la personne la mieux placée pour t'aider sur ce point..."
    pov "Comment ça ?"
    mog "J'ai... Pas vraiment envie d'en parler..."
    pov "Sois tu acceptes, sois tu m'en parles !"

    show Moguri BrasCroises Sourire Yeuxfermes

    mog "Ahaha ! Alors disons que j'accepte."
    pov "Mais j'aurais ma réponse, un jour !"
    mog "Si tu le dis... Bon, je te raccompagne ?"
    pov "Allons-y."

    scene street day with longfade
    show Metalice Standard Sourire Yeuxfermes at left
    show Moguri BrasCroises Sourire Yeuxfermes at right
    mog "Ho ! Voilà Metalice !"
    met "Salut vous deux ! Tout va bien ?"
    mog "Oui, je raccompagnais [povname] chez lui.. Mais tu habites dans son quartier non ?"
    mog "Je te laisse entre de bonnes mains, je vais dans l'autre direction !"
    innerpov "Oh nooon...."
    hide Moguri with dissolve

    if sex=="m":       
        met "Je suis à peine surprise que tu sois rentré avec un de tes prétendants..."
    else:
        met "Je suis à peine surprise que tu sois rentrée avec un de tes prétendants..."

    pov "Comment ça ?"

    show Metalice Standard Sourire Yeuxfermes

    met "Moguri enfin !"

    pov "Raaah mais laisse moi avec lui !"

    met "Tu dis ça mais je te vois très bien rougir hein !"
    pov "Tu parles quand même de lui beaucoup plus que moi, c'est peut être toi qui est intéressée finalement !"

    jump Rentreavecmetalice2

    return
