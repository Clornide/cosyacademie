

label club_lock:

    play music gym    
    scene gym with fade

    show Metalice Standard Sourire
    met "Voilà, on y est..."
    pov "Mais, c'est une salle d'entrainement aux sports de combat ?"
    show Metalice Standard Cligne
    met "Non! C'est une salle de bagarre!"
    show Metalice Standard Sourire
    met "En tant que responsable autoproclamé de la sécurité de l'établissement Lock y a ses habitudes..."
    pov "Ah ? Mais il n'y a personne."
    python:
        name_lock="???"
    lock "Hé ! Hé ! Hé ! Hé ! Hé !"
    show Metalice Standard Colere Rougit
    met "Lock... On sait que c'est toi ! Montre-toi !"
    python:
        name_lock="Lock"
    show Metalice Standard Colere Rougit at left
    show Lock PoseDroite Degoute at right with hpunch
    lock "Je t'ai déjà demandé de ne pas m'appeler comme ça!"
    lock "Pour vous je suis Patrick DeltaForce... Grand maître justicier de la bagarre !"
    show Metalice Standard Degoute
    met "Moui..."
    show Lock PoseDroite Badboy
    lock "La raison de votre présence s'il-vous plaît ?"
    show Metalice Standard Sourire Yeuxfermes
    met "[povname] aimerait faire partie de ton club."
    show Lock PoseDroite Sourire
    lock "Ah ! Vous venez pour l'épreuve ?!"
    pov "L'épreuve ? Je pensais qu'un classique formulaire d'inscription suffirait..."
    show Metalice PoseSpeciale Cligne Rougit 
    met "Heu... Bon je vous laisse! Bonne chance [povname] !"
    pov "..."
    hide Metalice
    hide Lock
    show Lock Standard Degoute at center with fade
    lock "Avance d'un pas prétendant !"
    show Lock Standard Degoute at mediumzoom
    lock "Pour faire partie de mon club tu devras triompher des trois épreuves !"
    show Lock Standard Sourire
    lock "Es-tu prêt ?"
    pov "Oui... Je crois..."
    show Lock Standard Triste
    lock "Première épreuve : La Question !"
    lock "Cherche au plus profond de ton coeur et tu trouveras l'évidente réponse."

    menu:

        "{cps=0}Qui saura, mieux que quiconque, t'enseigner l'art de la bagarre ?{/cps}"

        "Patrick DELTAFORCE !":
            python:
                pointsincel+=1
                reponsebagarre = 1

        "Choukran Norris !":
            python:
                pointsmedoc+=1
                reponsebagarre = 2

        "Ruhe ! Ruhe !":
            python:
                pointsmoguri+=1
                reponsebagarre = 3


    if reponsebagarre==2:
        show Lock Standard Colere
        lock "Quoi ?!"
        show Lock Standard Degoute
        lock "Ce n'était pas vraiment à lui que je pensais, mais je veux bien admettre que ses discours sont inspirants et qu'une énergie particulière se dégage de lui."
    elif reponsebagarre==3:
        show Lock Standard Gene
        lock "Qu'est ce que..."
        lock "Serait-ce une technique secrète ? Bien ! Prépare-toi !"
    else:
        show Lock Standard Sourire
        lock "Absolument !"
        lock "Et l'heure est venue de te montrer l'étendue de mes pouvoirs !"

    show Lock Standard Colere
    lock "Deuxième épreuve : la bagarre !"
    pov "???"
    show Moguri PoseGauche Colere at left with flash
    show Lock Standard Colere at right with hpunch
    mog "Lock ! Non ! Je ne te laisserai pas assouvir tes pulsions destructrices sur [povname] !"
    show Lock PoseDroite Colere at right
    lock "??!!"
    hide Moguri
    show Medoc PoseGauche Colere at left
    med "Moguri a raison! Ton règne tyrannique sur la salle de bagarre n'a que trop duré !"
    lock "Qu'est-ce que vous faites là vous deux ?"
    show Medoc Standard Rougit at left
    med "Heu, bah en fait on j'ai oublié mon t-shirt et..."
    hide Medoc
    show Moguri PoseGauche Colere at left
    mog "Medoc laisse tomber ! On fait la bagarre !"
    mog "Lock ! J'vais t'mettre une poussette ! Grrrrr..."
    show Moguri Standard Triste at left

    mog "Rhaaaaaaaaaaaaaaaaa !"
    scene gym_shonen
       
    play music "<from 10.0>music/sb_pursuit.mp3"
    show Moguri Standard Colere with hpunch
    show auraDBZ zorder 1000  with flash
    mog "KHAAA !"
    hide Moguri
    hide auraDBZ
    show Medoc Standard Badboy
    med "Ahummmmm ! Ahummmmmm !"
    show auraSaintSeya zorder 1000  with flash
    show Medoc Standard Colere
    med "Que brûle ma cosmo-énergie !" with hpunch
    hide auraSaintSeya
    hide Medoc
    show Lock Standard Colere
    lock "Yaaaaaaa !"
    show aura3 zorder 1000  with flash
    lock "ATATATATATATA !" with hpunch
    scene gym
    show din Standard Colere at center with flash
    play music "<from 1.0>music/sb_tomorrow.mp3"
    din "STOOOOOP !!!" with hpunch
    din "On a dit que c'était un visual novel, pas un shônen ! Alors on se calme !"
    hide din
    show Lock Standard Colere at center with flash
    lock "TU te calmes ! C'est MON arc narratif !"
    hide Lock
    scene gym_shonen
    show Medoc Standard Sourire at center
    play music "<from 31.0>music/sb_pursuit.mp3"
    show auraSaintSeya zorder 1000
    med "Brûle ! Brûle ! Ma cosmo-énergie !" with hpunch
    hide Medoc

    scene gym with fade
    play music "<from 31.0>music/sb_tomorrow.mp3"

    show din Standard Colere at center
    din "Allez hop ! Police des auras ! On enlève tout ça !"

    scene gym_shonen
    show Medoc Standard Sourire at center
    play music "<from 31.0>music/sb_pursuit.mp3"
    show auraSaintSeya zorder 1000
    show Medoc BrasCroises Degoute at center
    

    med "Mais non..."
    hide auraSaintSeya
    hide Medoc

    show auraDBZ zorder 1000
    show Moguri PoseDroite Degoute at center
    mog "Ok, police des auras je l'ai, mais désolé ça marche pas..."
    


    scene gym 
    play music "<from 31.0>music/sb_tomorrow.mp3"

    show din Standard Colere Rougit at center
    din "Ouais bah en attendant je dessine, et je décide qu'on est pas dans un shônen !"
    hide din

    scene gym_shonen
    
    play music "<from 31.0>music/sb_pursuit.mp3"

    show Lock Standard Colere  
    show aura3 zorder 1000 with flash


    lock "Wowowowo ! C'est MON arc narratif!"
    hide Lock

    hide aura3
    show auraDBZ zorder 1000
    show Moguri Standard Degoute
    mog "Mais qui a écrit ça ?"
    mog "Les personnages arrivent comme ça sans prévenir et ils modifient l'histoire ?"

    show Moguri Standard Triste 
    mog "Et on peut tous casser le quatrième mur... comme ça ?"
    show Moguri Standard Colere
    mog "C'est complètement baisé votre truc là !"
    show Moguri Standard Badboy
    mog "Ah bah d'ailleurs, moi aussi je parle la langue des serpents ! Allez hop !"
    hide Moguri
    menu:

        "{cps=0}Moguri décide que c'est la fin du jeu. Avec quel personnage souhaites-tu vivre longtemps et avoir beaucoup d'enfants ? Ou juste passer la nuit, c'est comme tu veux...{/cps}"

        "Moguri évidemment ! ":
            python:
                pointsmoguri+=1

        "Ah bah Moguri alors !":
            python:
                pointsmoguri+=1

        "Medoc ! (Mais en fait non ! Moguri !)":
            python:
                pointsmoguri+=1

    show Moguri Standard Sourire at center
    mog "Meilleur choix!"
    hide Moguri
    hide auraDBZ

    show aura3 zorder 1000
    show Lock Standard Colere  with flash
    lock "Ici c'est l'école du petit couteau ! Pas le club tech ! Alors CALMEZ-VOUS ! "
    scene gym
    python:
        pointsmoguri-=1
        renpy.movie_cutscene("movies/le_petit_couteau.webm")
    hide Lock

    
    show din Standard Colere  with flash
    din "Aie !" with hpunch
    hide din
    show Medoc Standard Colere at left with hpunch
    med "Hey !"
    hide Medoc
    show Moguri Standard Colere at right with hpunch
    mog "Waaaaa !"
    hide Moguri
    show Lock Standard Colere at center
    lock "Allez ! Cassez-vous avant que je ne m'énerve vraiment !"
    lock "C'est pas un club de bébé Cadum ici!"
    show Lock Standard Badboy at center
    lock "[povname], c'est bon on peut continuer ?!"
    lock "Troisème épreuve : le lancer des mille petits couteaux !"
    pov "Ça, je devrais pouvoir y arriver."
    show Lock Standard Sourire at center
    lock "Ah! Mais c'est moi qui lance, toi tu fais la cible !"
    pov "Que... QUOI ???"
    pov "Mais t'es complètement malade?"
    pov "En fait, tu sais quoi ? Je vais trouver un autre club..."
    show Lock Standard Degoute at center

    pause 3

    return