label Premiercours:
    scene classe with fade

    inc "Aller aller, un peu de silence !"

    show mickeyPoseStandardSourire with fade

    mic "Bonjour à tous !"
    tlm "Bonjour monsieur Max !"
    mic "Asseyez-vous."

    hide mickeyPoseStandardSourire
    show mickeyPoseStandardBadBoy

    if sex=="m":
        mic "Aujourd'hui, nous avons l'honneur d'accueillir un nouvel étudiant parmi nous."
    else:
        mic "Aujourd'hui, nous avons l'honneur d'accueillir une nouvelle étudiante parmi nous."
    mic "[povname], tu veux bien venir au tableau te présenter quelques secondes ?"
    pov "..."
    pov "Bien sûr monsieur Max..."
    "En parcourant brièvement la classe des yeux, j'essaie de graver toutes ces nouvelles têtes dans ma mémoire."

    hide mickeyPoseStandardBadBoy

    show moguriBrasCroisesSourireYeuxFermes at right
    show medocPoseStandardSourireYeuxFermes at left

    "Medoc et Moguri, évidemment..."

    hide medocPoseStandardSourireYeuxFermes at left
    hide moguriBrasCroisesSourireYeuxFermes at right

    show metalicePoseCoucouSourireYeuxFermes

    "Metalice ! Ses renseignements de tout à l'heure vont m'être très utiles... Je pense m'être fait ma première amie !"

    hide metalicePoseCoucouSourireYeuxFermes

    "Mais aussi d'autres personnes..."

    show dieuvBrasCroisesDegoute

    "Celui là par exemple, dégage une aura de malfrat."
    "Mais il étudie ici... Je ne pense pas qu'il soit si méchant que ça !"
    "Ca ne me ressemble pas de juger sur les apparences pourtant..."
    "Bref."

    hide dieuvBrasCroisesDegoute

    pov "Bonjour tout le monde. Mon nom est [povname] et c'est mon premier jour à l'Académie."
    pov "Mes passions sont la littérature, le cinéma et les jeux-vidéo..."
    if sex=="m":
        pov "Je suis ravi d'avoir été accepté dans cette classe, même si je ne suis pas aussi exceptionnel que v-"
    else:
        pov "Je suis ravie d'avoir été acceptée dans cette classe, même si je ne suis pas aussi exceptionnelle que v-"

    with shortflash
    show medocPosePoingsColere with shortflash

    "BLAM!!"
    med "Bon t'as pas bientôt fini avec ses histoires de 'Je n'ai pas ma place ici, vous valez mieux que moi' ou je sais pas quoi !?"
    med "T'as pas écouté ce que t'a dit Moguri ou quoi ?!"

    hide medocPosePoingsColere
    show moguriBrasCroisesDegoute

    mog "C'est bon Medoc, lâche l'affaire."

    hide moguriBrasCroisesDegoute
    show moguriBrasCroisesSourireYeuxFermes

    if sex=="m":
        mog "Il ne pense clairement pas à mal, n'est-ce pas ?"
    else:
        mog "Elle ne pense clairement pas à mal, n'est-ce pas ?"

    hide moguriBrasCroisesSourireYeuxFermes
    show dieuvBrasCroisesColere

    if sex=="m":
        inc "Ouais Medoc, c'est son problème de confiance en lui, pas le tieng !"
    else:
        inc "Ouais Medoc, c'est son problème de confiance en elle, pas le tieng !"

    "Ce type a vraiment un drôle d'accent..."

    hide dieuvBrasCroisesColere
    show dieuvBrasCroisesSourireYeuxFermes

    inc "Même si on sait que t'es un pro pour t'approprier des trucs qui ne t'appartiennent pas..."

    hide dieuvBrasCroisesSourireYeuxFermes
    show medocPosePoingsColere

    med "Ah ouais ?! Répète ça pour voir ?"

    hide medocPosePoingsColere
    show dieuvBrasCroisesColere

    inc "Un peu que je vais répéter peuchèreuh ! Tu crois que j'ai oublié pour Jeud-"

    hide dieuvBrasCroisesColere

    with shortflash
    with shortflash

    show metalicePoseCoucouColereRougit

    met "Aller c'est bon ! Laissez tomber les gars ! Vous vous donnez en spectacle"

    hide metalicePoseCoucouColereRougit
    show mickeyPoseStandardColere

    mic "Elle a raison... Rasseyez-vous les garçons, je croyais que c'était derrière vous tout ça..."

    hide mickeyPoseStandardColere
    show mickeyPoseStandardSourireYeuxFermes

    mic "Quant à toi Metalice, tu as accompli ton rôle de déléguée à la perfection."

    hide mickeyPoseStandardSourireYeuxFermes
    show metalicePoseCoucouSourireYeuxFermes

    met "Merci monsieur Max !"

    hide metalicePoseCoucouSourireYeuxFermes
    show mickeyPoseStandardSourire

    mic "Tu peux retourner à ta place [povname], merci pour ta présentation."

    hide mickeyPoseStandardSourire
    show mickeyPoseStandardBadBoy

    mic "Je suis désolé que tu aies eu à être témoin de cette altercation."

    hide mickeyPoseStandardBadBoy
    show mickeyPoseStandardDegoute

    mic "Medoc, Dieuvomi, vous viendrez me voir à la fin du cours..."

    hide mickeyPoseStandardDegoute
    show medocPoseStandardDegoute

    med "Tch."

    hide medocPoseStandardDegoute
    show dieuvBrasCroisesDegoute

    dieuv "Mmmm."

    hide dieuvBrasCroisesDegoute
    show mickeyPoseStandardSourire

    mic "Bien ! Ouvrez vos livres page 77, on va commencer la trigonométrie..."

    hide mickeyPoseStandardSourire
    show mickeyPoseStandardSourireYeuxFermes

    with longfade

    mic "Aller, ce sera tout pour aujourd'hui, vous pouvez y aller !"

    hide mickeyPoseStandardSourireYeuxFermes
    show mickeyPoseStandardDegoute

    mic "Sauf vous, Medoc et Dieuvomi, évidemment..."

    hide mickeyPoseStandardDegoute

    scene couloir with fade
    show metalicePoseCoucouSourireYeuxFermes

    met "Bon. Et bien c'était une grosse première journée pour toi n'est-ce pas ?"
    pov "Oui on peut dire ça..."

    hide metalicePoseCoucouSourireYeuxFermes
    show metalicePoseCoucouSourire

    pov "Dis, c'était qui ce type au style de voyou, avec l'accent exotique ?"

    hide metalicePoseCoucouSourire
    show metalicePoseCoucouCligne

    met "Dieuvomi ? C'est pas VRAIMENT un voyou, c'est juste un style qu'il se donne."

    hide metalicePoseCoucouCligne
    show metalicePoseCoucouSourire

    met "Il ne te fera jamais de mal, à moins que tu sois un apocope de bandage pneumatique"
    pov "Un quoi ?"

    hide metalicePoseCoucouSourire
    show metalicePoseCoucouDegoute

    met "Un pneu. Il a un souci avec ça je crois, il aime beaucoup les crever."

    hide metalicePoseCoucouDegoute
    show metalicePoseCoucouSourire

    met "Il s'est débarassé d'un gang qui gangrenait la ville à lui tout seul d'ailleurs !"
    pov "Je t'avoue que je ne vois pas particulièrement le rapport..."

    hide metalicePoseCoucouSourire
    show metalicePoseCoucouCligne

    met "La spécificité de ce gang était que ses membres ne se déplaçaient qu'en BMX. Leur principale méthode d'agression était de rouler sur leurs victimes..."
    pov "Mais... C'est stupide ?"

    hide metalicePoseCoucouCligne
    show metalicePoseCoucouSourireYeuxFermes

    met "Peut être, mais ça fait mal !"
    met "Dieuvomi a crevé tous les pneus de tous les BMX du gang en l'espace d'une heure, en pleine nuit..."
    pov "Ouaaaaah..."

    hide metalicePoseCoucouSourireYeuxFermes
    show metalicePoseCoucouSourire

    met "N'est-ce pas ? Du coup, sans pneus, le gang s'est dissout de lui même. C'est aussi pour ça qu'il est aussi respecté !"
    met "Et autre point de détail de cette anecdote, le leader de ce gang était un cousin de Medoc..."
    pov "Aaaaaah ! C'est donc de là que vient cette animosité entre eux ?"

    hide metalicePoseCoucouSourire
    show metalicePoseCoucouSourireYeuxFermes

    met "Pas du tout ! Medoc ne tolérait absolument pas les agissements de son cousin."
    pov "D'où est-ce que ça vient alors ?"

    hide metalicePoseCoucouSourireYeuxFermes
    show metalicePoseCoucouTriste

    met "On n'aime pas trop en parler ici... Ca nous rappelle des événements un peu sombre. Tu l'apprendras bien assez tôt je pense."
    pov "..."

    hide metalicePoseCoucouTriste
    show metalicePoseCoucouSourireYeuxFermes

    met "Bon allez, je te ramène chez toi ? J'ai encore pas mal de chose à te raconter tu sais ?"

    pause 3

    hide metalicePoseCoucouSourireYeuxFermes

    jump coursPhysique
