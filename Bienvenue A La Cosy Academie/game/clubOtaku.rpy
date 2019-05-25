label club_otaku:

    
    play music kawaii
    scene black
    image name_club_otak = Text("{size=80}Chapitre 4 :\nLe club Otaku", text_align=0.5)
    window hide
    show name_club_otak:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(2)
    hide name_club_otak
    window auto

    scene school hallway night with longfade
    innerpov "Houlàlà, il est tard..."
    innerpov "Bon, din m'a dit qu'ils avaient une photocopieuse dans ce club..."
    innerpov "C'est ici !"

    scene classroom sunset with longfade

    innerpov "Tiens ? Ça sent le matcha."

    show din PoseGauche Gene at left
    show Caro PoseSpeciale Triste at right
    
    show din PoseGauche Sourire Yeuxfermes Rougit

    din "Mais là je lui ai dit \"On peut avoir des tentacules et quand même droit à l'amour\"... et on était d'accord, au final !"
    show Caro PoseDroite Cligne
    $ word_effect("Sugoi !")
    caro "On peut donc se réconcilier sur Twitter ! {image=we1}"
    show din BrasCroises Sourire
    $ word_effect("otaku")
    din "Ah tiens te voilà [povname] ! Tu t'intéresses au club {image=we1} alors ?"
    show Caro PoseDroite Sourire Yeuxfermes
    $ word_effect("Irasshaimaseee")
    caro "Entre donc, on a des gâteaux et du thé ! {image=we1}"
    show din BrasCroises Sourire Yeuxfermes
    din "Tu viens de louper rockmanshii qui est rentré chez lui !"
    show Caro PoseDroite Triste
    
    if sex=="m":
        caro "Quand je pense qu'avant on était une quinzaine, il ne reste plus que nous trois maintenant... Tu es donc sacrément le bienvenu [povname] !"
    else:
        caro "Quand je pense qu'avant on était une quinzaine, il ne reste plus que nous trois maintenant... Tu es donc sacrément la bienvenue [povname] !"

    pov "Ça alors, comment ça se fait ?"
    show din Standard Cligne Rougit
    din "Franchement, on est un club sympa et convivial, c'est juste comme ça, les gens sont partis réaliser leurs rêves chacun leur tour..."
    innerpov "C'est louche..."
    pov "Et en quoi consistent vos activités ?"
    show Caro BrasCroises Cligne
    caro "Eh bien par exemple on discute de nos derniers coups de cœur, on se prête nos mangas."
    show din Standard Sourire
    din "C'est carrément le club du partage, on se refile même nos identifiants de sites de VOD pour regarder des animes."
    show Caro BrasCroises Sourire Yeuxfermes Rougit
    caro "Et des dramas bien sûr."
    innerpov "OK, jusqu'ici ça a l'air normal."
    show din PoseGauche Sourire Rougit
    din "Et puis surtout on encourage la créativité, ça c'est super important."
    show Caro PoseSpeciale Cligne
    caro "Ah oui, on supporte les artistes !"
    innerpov "J'ai dû me faire des idées."
    pov "Formidable !"
    show din PoseGauche Sourire Yeuxfermes
    $ word_effect("fanfics")
    din "Donc voilà, en gros on lit aussi beaucoup de {image=we1}."
    show Caro PoseDroite Sourire
    caro "Et on achète des fanzines en convention ! Il y en a toute une étagère là-bas si tu veux."
    pov "Vous avez l'air motivées !"
    innerpov "... Et d'avoir vraiment beaucoup de temps à disposition..."
    show din PoseSpeciale Sourire Yeuxfermes Rougit
    din "Et on laisse libre cours à notre passion en écrivant et dessinant nous-même nos fanfics !"
    show Caro PoseSpeciale Gene
    $ word_effect("personnages")
    caro "Faut dire qu'on aime tellement de séries ! Tellement de {image=we1} !"
    pov "Sympa !"
    show din PoseSpeciale Cligne
    din "Bon et puis nos camarades bien sûr..."
    pov "Hein ?"
    show Caro PoseDroite Colere Rougit
    $ word_effect("profiter")
    caro "Comme je dis toujours, \"on est dans une Académie remplie de gens canons, ce serait un crime de ne pas en {image=we1} !\""
    pov "Mais qu'est-ce que tu veux dire par-là...?"
    show din PoseGauche Sourire Yeuxfermes
    $ word_effect("dynamiques subtiles")
    din "Tu viens de débarquer, tu n'as pas encore eu l'occasion de saisir les {image=we1} de notre vie étudiante..."
    show Caro PoseDroite Gene
    $ word_effect("inspire beaucoup")
    caro "Oh oui ça nous {image=we1}."
    show din PoseGauche Gene
    din "Vraiment beaucoup..."
    pov "Euh..."
    show Caro PoseSpeciale Perv
    $ word_effect("Medoc et Moguri")
    caro "D'ailleurs din, dis-moi que tu as vu {image=we1} tout à l'heure pendant la pause déjeuner hi hi hi"
    show din PoseGauche Cligne Rougit
    $ word_effect("tactiles")
    din "Ils ne sont jamais {image=we1} ces deux-là, mais tout est dans le regard hi hi"
    innerpov "Mais enfin..."
    show Caro BrasCroises Degoute
    $ word_effect("Moguri x Chuen")
    caro "Je sais que tu shippes {image=we1}..."
    show din BrasCroises Colere
    din "Un beau gosse brun + un beau gosse blond c'est la base, Caro ! Tout le monde sait ça !"
    show Caro PoseSpeciale Colere Rougit
    $ word_effect("Moguri x Medoc")
    caro "... mais rien à faire, LE ship c'est {image=we1} !"
    innerpov "Fais une poker face et souris [povname], c'est le moment."
    show din BrasCroises Cligne Rougit
    $ word_effect("Medoc x Moguri")
    din "Ou {image=we1}..."
    show Caro PoseSpeciale Perv
    $ word_effect("HI HI HI")
    caro "{image=we1}"
    show din PoseSpeciale Perv
    din "Eh oui, ça varie les fan arts MWEHEHE !"
    innerpov "Mais qu'est-ce que ça peut bien changer ?! Est-ce que je tiens vraiment à le savoir ?!"
    show Caro PoseSpeciale Sourire Yeuxfermes Rougit
    caro "L'important c'est de soutenir la créativité, hi hi pardon [povname] on se répète !"
    pov "Ha ha euh d'accord c'est... cool..."
    show din PoseSpeciale Sourire Yeuxfermes
    $ word_effect("Von x Foulk")
    din "De toute façon tu sais bien que mon ship préféré c'est {image=we1}, la Droite et la Gauche, du vrai bon hate sex frr frr frr"
    show Caro PoseDroite Gene
    caro "OH TOI ALORS !"
    innerpov "Il faut que je m'en aille maintenant et que j'oublie tout ça. Très vite."
    show din PoseSpeciale Perv
    $ word_effect("Dieuvomi")
    din "Je t'ai pas montré ma dernière œuvre avec {image=we1} et ses chaînes au fait !"
    show Caro PoseSpeciale Perv
    $ word_effect("Pansepignon ET Chuen")
    caro "Est-ce que c'est celle avec {image=we1} aussi ?"
    show din PoseSpeciale Gene
    $ word_effect("beaucoup d'ardeur")
    din "Ces trois-là il faut toujours qu'ils se congratulent avec {image=we1}, j'y peux rien, ça m'inspire..."
    show Caro Standard Cligne Rougit
    $ word_effect(povname)
    caro "Alors {image=we1} ? On t'a pas carrément donné envie de rejoindre notre club ?"
    show din PoseSpeciale Sourire Yeuxfermes Rougit
    $ word_effect("plutôt pas mal")
    din "Comme tu peux le voir c'est beaucoup d'ondes positives et d'amour de l'art ! D'ailleurs t'es {image=we1} toi aussi..."
    pov "Je... vais prendre le temps de réfléchir..."
    innerpov "AU. SECOURS. CASSOS."
    
    jump fin_journee
    return
