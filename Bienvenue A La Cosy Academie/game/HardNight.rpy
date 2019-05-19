label hard_night:
    play music rainbow
    scene black
    image name_hard_night = Text("{size=80}Le lendemain matin...", text_align=0.5)
    window hide
    show name_hard_night:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(2)
    hide name_hard_night
    window auto

    scene school entrance with fade

    show Moguri Standard Sourire at right

    mog "Hey Medoc! Ça va?"

    show Medoc Standard Triste at left

    med "Oui ça va..."
    mog "T'es sûr?"
    med "Oui je suis sûr. Pourquoi ?"

    show Moguri Standard Degoute at right

    mog "Bah je sais pas... T'as l'air fatigué."

    show Medoc Standard Degoute at left

    med "Ah oui? Non, mais ça va!"
    mog "Tu peux me dire si t'as un problème... Vraiment t'as pas l'air bien !"
    med "Rhaaa mais non ! Ça va ! C'est juste que cette nuit c'était chaud..."

    show Moguri Standard Sourire Yeuxfermes at right

    mog "Ah d'accord !"

    show Medoc BrasCroises Badboy at left

    med "Oui !"

    show Moguri Standard Sourire at right

    mog "Et..."

    show Medoc BrasCroises Sourire Yeuxfermes Rougit

    med "Eh bah c'était TRÈS TRÈS chaud !"

    hide Moguri
    hide Medoc

    scene reverie with fade

    show Medoc PoseSpeciale Degoute with fade

    med "Oui... Voilà... Comme ça..."
    med "Un coup à gauche. Un coup à droite."

    show Medoc PoseSpeciale Sourire

    med "Hop la! C'est qui le boss ?"
    med "[povname]? Oh! [povname]!"

    hide Medoc

    scene school entrance with flash

    show Medoc BrasCroises Colere at left

    med "[povname] ???!!!"

    show Moguri Standard Sourire Yeuxfermes at right

    mog "On dirait que t'es pas le seul qui n'a pas dormi cette nuit Medoc..."
    menu:
    
            mog "{cps=0}On dirait que t'es pas le seul qui n'a pas dormi cette nuit Medoc...{/cps}"
            "Mais pas du tout enfin !! Moi je dors la nuit!":
                python:
                    pointsincel+=1

            "J'avoue, je découvre Borges et j'ai du mal à quitter ses livres...":
                python:
                    pointsmoguri+=1

            "Oui, j'ai expérimenté différents types d'épices sur des brochettes... Je ne vois pas le temps passer quand je cuisine!":
                python:
                    pointsmedoc+=1

    show Medoc BrasCroises Badboy at left

    med "Ouais... En attendant, tu pourrais te pousser s'il te plaît ? J'aimerais autant ne pas avoir à passer sous cette échelle pour aller en cours."

    show Moguri Standard Badboy at right

    mog "Sinon Medoc, la prochaine fois, tu m'appelles ?"
    mog "Tu sais, sans vouloir te vexer, je peux te donner deux ou trois conseils..."

    show Medoc Standard Colere at left

    med "T'es sérieux là ?"

    show Moguri Standard Degoute at right

    mog "Bah ouais !"

    hide Moguri
    hide Medoc

    scene reverie with fade

    show Moguri PoseSpeciale Badboy at right with fade

    mog "Allez vas-y ! Plus vite! Là !"

    show Medoc PoseSpeciale Badboy Rougit at left with fade

    med "Mais enfin Moguri ! Non, je peux pas..."

    show Moguri PoseSpeciale Colere at right

    mog "Mais si fais moi confiance! Ça passe !"

    show Medoc PoseSpeciale Colere Rougit at left

    med "Mais non !"
    mog "Mais si !"

    show Moguri PoseSpeciale Sourire Rougit at right

    mog "[povname] ça va ?"

    hide Moguri
    hide Medoc

    scene school entrance with flash

    show Medoc Standard Badboy at left
    show Moguri Standard Badboy at right

    med "[povname]?"
    pov "Heu... oui ?"

    mog "T'as trouvé ça chaud ?"
    pov "Hin? Quoi ????"

    show Medoc Standard Sourire Yeuxfermes at left

    med "BAH SEKIRO !"

    pov "Haha oui !"
    innerpov "Houlà, j'ai vraiment trop d'imagination..."
    pov "Heuuu Je vous laisse, je dois retrouver Metalice au club de bagarre !"
    hide Medoc with dissolve 
    hide Moguri with dissolve
    jump club_lock
    return