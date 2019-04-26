label Premiercours:
    scene classe with fade

    inc "Aller aller, un peu de silence !"

    show Mickey Standard Sourire Yeuxfermes with fade

    mic "Bonjour à tous !"
    tlm "Bonjour monsieur Max !"
    mic "Asseyez-vous."
    show Mickey Standard Badboy
    if sex=="m":
        mic "Aujourd'hui, nous avons l'honneur d'accueillir un nouvel étudiant parmi nous."
    else:
        mic "Aujourd'hui, nous avons l'honneur d'accueillir une nouvelle étudiante parmi nous."
    mic "[povname], tu veux bien venir au tableau te présenter quelques secondes ?"
    pov "..."
    pov "Bien sûr monsieur Max..."
    "En parcourant brièvement la classe des yeux, j'essaie de graver toutes ces nouvelles têtes dans ma mémoire."
    hide Mickey

    show Moguri BrasCroises Sourire at right
    show Medoc Standard Sourire at left

    "Medoc et Moguri, évidemment..."

    hide Medoc

    hide Moguri

    show Metalice PoseCoucou Sourire Yeuxfermes

    "Metalice ! Ses renseignements de tout à l'heure vont m'être très utiles... Je pense m'être fait ma première amie !"

    hide Metalice

    "Mais aussi d'autres personnes..."

    show Dieuvomi BrasCroises Triste

    "Celui là par exemple, dégage une aura de malfrat."
    "Mais il étudie ici... Je ne pense pas qu'il soit si méchant que ça !"
    "Ca ne me ressemble pas de juger sur les apparences pourtant..."
    "Bref."

    hide Dieuvomi

    pov "Bonjour tout le monde. Mon nom est [povname] et c'est mon premier jour à l'Académie."
    pov "Mes passions sont la littérature, le cinéma et les jeux-vidéo..."
    if sex=="m":
        pov "Je suis ravi d'avoir été accepté dans cette classe, même si je ne suis pas aussi exceptionnel que v-"
    else:
        pov "Je suis ravie d'avoir été acceptée dans cette classe, même si je ne suis pas aussi exceptionnelle que v-"

    with shortflash
    show Medoc PosePoings Degoute with shortflash

    "BLAM!!"
    med "Bon t'as pas bientôt fini avec ses histoires de 'Je n'ai pas ma place ici, vous valez mieux que moi' ou je sais pas quoi !?"
    med "T'as pas écouté ce que t'a dit Moguri ou quoi ?!"

    hide Medoc
    show Moguri BrasCroises Triste

    mog "C'est bon Medoc, lâche l'affaire."

    show Moguri BrasCroises Sourire

    if sex=="m":
        mog "Il ne pense clairement pas à mal, n'est-ce pas ?"
    else:
        mog "Elle ne pense clairement pas à mal, n'est-ce pas ?"

    hide Moguri
    show Dieuvomi BrasCroises Colere

    if sex=="m":
        inc "Ouais Medoc, c'est son problème de confiance en lui, pas le tieng !"
    else:
        inc "Ouais Medoc, c'est son problème de confiance en elle, pas le tieng !"

    "Ce type a vraiment un drôle d'accent..."

    show Dieuvomi BrasCroises Sourire

    inc "Même si on sait que t'es un pro pour t'approprier des trucs qui ne t'appartiennent pas..."

    show Dieuvomi BrasCroises Triste
    show Medoc PosePoings Colere

    med "Ah ouais ?! Répète ça pour voir ?"

    hide Medoc
    show Dieuvomi BrasCroises Colere

    inc "Un peu que je vais répéter peuchèreuh ! Tu crois que j'ai oublié pour Jeud-"

    hide Dieuvomi
    with shortflash
    with shortflash
    show Metalice Standard Colere Rougit

    met "Aller c'est bon ! Laissez tomber les gars ! Vous vous donnez en spectacle"

    hide Metalice
    show Mickey Standard Colere

    mic "Elle a raison... Rasseyez-vous les garçons, je croyais que c'était derrière vous tout ça..."

    show Mickey Standard Sourire

    mic "Quant à toi Metalice, tu as accompli ton rôle de déléguée à la perfection."

    hide Mickey
    show Metalice Standard Sourire Yeuxfermes

    met "Merci monsieur Max !"

    hide Metalice
    show Mickey Standard Sourire Yeuxfermes

    mic "Tu peux retourner à ta place [povname], merci pour ta présentation."
    show Mickey Standard Badboy
    mic "Je suis désolé que tu aies eu à être témoin de cette altercation."
    show Mickey Standard Triste
    mic "Medoc, Dieuvomi, vous viendrez me voir à la fin du cours..."

    hide Mickey
    show Medoc Standard Badboy

    med "Tch."

    hide Medoc
    show Dieuvomi BrasCroises Badboy

    dieuv "Mmmm."

    hide Dieuvomi deg
    show Mickey Standard Sourire Yeuxfermes

    mic "Bien ! Ouvrez vos livres page 77, on va commencer la trigonométrie..."

    show Mickey Standard Sourire
    with longfade

    mic "Aller, ce sera tout pour aujourd'hui, vous pouvez y aller !"
    show Mickey Standard Degoute
    mic "Sauf vous, Medoc et Dieuvomi, évidemment..."

    scene couloir with fade
    show Metalice PoseCoucou Sourire Yeuxfermes

    met "Bon. Et bien c'était une grosse première journée pour toi n'est-ce pas ?"
    pov "Oui on peut dire ça..."
    show Metalice PoseCoucou Sourire
    pov "Dis, c'était qui ce type au style de voyou, avec l'accent exotique ?"
    show Metalice PoseCoucou Cligne
    met "Dieuvomi ? C'est pas VRAIMENT un voyou, c'est juste un style qu'il se donne."
    show Metalice PoseCoucou Sourire
    met "Il ne te fera jamais de mal, à moins que tu sois un apocope de bandage pneumatique"
    pov "Un quoi ?"
    show Metalice PoseCoucou Degoute
    met "Un pneu. Il a un souci avec ça je crois, il aime beaucoup les crever."
    show Metalice PoseCoucou Sourire
    met "Il s'est débarassé d'un gang qui gangrenait la ville à lui tout seul d'ailleurs !"
    pov "Je t'avoue que je ne vois pas particulièrement le rapport..."
    show Metalice PoseCoucou Cligne
    met "La spécificité de ce gang était que ses membres ne se déplaçaient qu'en BMX. Leur principale méthode d'agression était de rouler sur leurs victimes..."
    pov "Mais... C'est stupide ?"
    show Metalice PoseCoucou Sourire Yeuxfermes
    met "Peut être, mais ça fait mal !"
    met "Dieuvomi a crevé tous les pneus de tous les BMX du gang en l'espace d'une heure, en pleine nuit..."
    pov "Ouaaaaah..."
    show Metalice PoseCoucou Sourire
    met "N'est-ce pas ? Du coup, sans pneus, le gang s'est dissout de lui même. C'est aussi pour ça qu'il est aussi respecté !"
    met "Et autre point de détail de cette anecdote, le leader de ce gang était un cousin de Medoc..."
    pov "Aaaaaah ! C'est donc de là que vient cette animosité entre eux ?"
    show Metalice PoseCoucou Sourire Yeuxfermes
    met "Pas du tout ! Medoc ne tolérait absolument pas les agissements de son cousin."
    pov "D'où est-ce que ça vient alors ?"
    show Metalice PoseCoucou Triste
    met "On n'aime pas trop en parler ici... Ca nous rappelle des événements un peu sombre. Tu l'apprendras bien assez tôt je pense."
    pov "..."
    show Metalice PoseCoucou Sourire Yeuxfermes
    met "Bon allez, je te ramène chez toi ? J'ai encore pas mal de chose à te raconter tu sais ?"

    pause 3
    jump coursPhysique
