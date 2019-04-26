label HardNight:
    scene school entrance with fade

    show Moguri Standard Badboy at right

    mog "Hey Medoc! Ça va?"

    show Medoc Standard Badboy at left

    med "Oui ça va..."
    mog "T'es sûr?"
    med "Oui je suis sûr. Pourquoi?"
    mog "Bah je sais pas... T'as l'air fatigué."
    med "Ah oui? Non, mais ça va!"
    mog "Tu peux me dire si t'as un problème... Vraiment t'as pas l'air bien!"
    med "Rhaaa mais non ! Ça va ! C'est juste que cette nuit c'était chaud..."
    mog "Ah d'accord!"
    med "Oui!"
    mog "Et..."
    med "Eh bah c'était TRÈS TRÈS chaud!"

    hide Moguri
    hide Medoc

    scene reverie with fade

    show Medoc Topless Badboy with fade

    med "Oui... Voilà... Comme ça..."
    med "Un coup à gauche. Un coup à droite."
    med "Hop la! C'est qui le boss ?"
    med "[povname]? Oh! [povname]!"

    hide Medoc

    scene school entrance with flash

    show Medoc PosePoings Colere at left

    med "[povname]???!!!"

    show Moguri Standard Badboy at right

    mog "On dirait que t'es pas le seul qui n'a pas dormi cette nuit Medoc..."
    menu:
            "Mais pas du tout enfin !! Moi je dors la nuit!":
                python:
                    pointsincel+=1

            "J'avoue, je découvre Borges et j'ai du mal à quitter ses livres...":
                python:
                    pointsMoguri+=1

            "Oui, j'ai expérimenté différents types d'épices sur des brochettes... Je ne vois pas le temps passer quand je cuisine!":
                python:
                    pointsMedoc+=1

    hide Moguri
    show Medoc Standard Badboy at left

    med "Ouais... En attendant, tu pourrais te pousser s'il te plaît? J'aimerais autant ne pas avoir à passer sous cette échelle pour aller en cours."

    show Moguri Standard Badboy at right

    mog "Sinon Medoc, la prochaine fois, tu m'appelles?"
    mog "Tu sais, sans vouloir te vexer, je peux te donner deux ou trois conseils..."
    med "T'es sérieux là?"
    mog "Bah ouais!"

    hide Moguri
    hide Medoc

    scene reverie with fade

    show Moguri Topless Badboy at right with fade

    mog "Allez vas-y! Plus vite! Là!"

    show Medoc Topless Badboy at left with fade

    med "Mais enfin Moguri! Non, je peux pas..."
    mog "Mais si fais moi confiance! Ça passe !"
    med "Mais non!"
    mog "Mais si!"
    mog "[povname] ça va?"

    hide Moguri
    hide Medoc

    scene school entrance with flash

    show Medoc Standard Badboy at left

    med "[povname]?"
    pov "Heu... oui?"

    show Moguri Standard Badboy at right

    mog "T'as trouvé ça chaud ?"
    pov "Hin? Quoi????"
    med "Bah Sekiro!"

    pause 3

    hide Medoc
    hide Moguri

    return