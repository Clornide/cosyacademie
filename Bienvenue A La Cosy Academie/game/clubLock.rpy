

label club_lock:



    play music gym    

    scene black
    image name_club_bagarre = Text("{size=80}Chapitre 5 :\nLe club de Bagarre", text_align=0.5)
    window hide
    show name_club_bagarre:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(2)
    hide name_club_bagarre
    window auto

    scene gym with fade

    show Metalice Standard Sourire
    met "Voilà, on y est..."
    pov "Mais, c'est une salle d'entraînement aux sports de combat ?"
    show Metalice Standard Cligne
    met "Non! C'est une salle de bagarre !"
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
    lock "Pour vous je suis Patrick DELTAFORCE... Grand maître justicier de la bagarre !"
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
    hide Metalice with dissolve
    pov "..."
    
    hide Lock
    show Lock Standard Degoute at center with fade
    lock "Avance d'un pas prétendant !"
    show Lock Standard Degoute at mediumzoom
    lock "Pour faire partie de mon club tu devras triompher des trois épreuves !"
    show Lock Standard Sourire
    if sex=="m":
        lock "Es-tu prêt ?"
    else:
        lock "Es-tu prête ?"
    pov "Oui... Je crois..."
    show Lock Standard Triste
    lock "Première épreuve : La Question !"
    lock "Cherche au plus profond de ton coeur et tu trouveras l'évidente réponse."
    lock "Qui saura, mieux que quiconque, t'enseigner l'art de la bagarre ?"
    menu:

        lock "{cps=0}Qui saura, mieux que quiconque, t'enseigner l'art de la bagarre ?{/cps}"

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
        lock "Qu'est-ce que..."
        lock "Serait-ce une technique secrète ? Bien ! Prépare-toi !"
    else:
        show Lock Standard Sourire
        lock "Absolument !"
        lock "Et l'heure est venue de te montrer l'étendue de mes pouvoirs !"

    show Lock Standard Colere
    lock "Deuxième épreuve : la bagarre !"
    pov "???"
    show Moguri PoseGauche Colere at left behind Lock with flash
    show Lock Standard Colere at right, normalzoom with hpunch
    mog "Lock ! Non ! Je ne te laisserai pas assouvir tes pulsions destructrices sur [povname] !"
    show Lock PoseDroite Colere at right
    lock "??!!"
    hide Moguri
    show Medoc PoseGauche Colere at left
    med "Moguri a raison ! Ton règne tyrannique sur la salle de bagarre n'a que trop duré !"
    lock "Qu'est-ce que vous faites là vous deux ?"
    show Medoc Standard Rougit at left
    med "Heu, bah en fait on j'ai oublié mon t-shirt et..."
    hide Medoc
    show Moguri PoseGauche Colere at left
    mog "Medoc laisse tomber ! On fait la bagarre !"
    mog "Lock ! J'vais t'mettre une poussette ! Grrrrr..."
    show Moguri Standard Triste at left

    
    scene gym_shonen
    
    play music "<from 10.0>music/sb_pursuit.mp3"
    show Moguri Standard Colere with hpunch
    mog "Rhaaaaaaaaaaaaaaaaa !"
    show auraDBZ zorder 1000  with flash
    play sound [ auraDBZStart, auraDBZ, auraDBZ, auraDBZ ]
    mog "KHAAA !"
    hide Moguri
    hide auraDBZ
    stop sound
    show Medoc Standard Badboy

    med "Ahummmmm ! Ahummmmmm !"
    
    show Medoc Standard Colere  
    show auraSaintSeya behind Medoc with flash 
    play sound auraSeiya
    med "Que brûle ma cosmo-énergie !" with hpunch
    stop sound
    hide auraSaintSeya
    hide Medoc
    show Lock Standard Colere
    lock "Yaaaaaaa !"
    show aura3 zorder 1000  with flash
    play sound ATATATATA
    lock "ATATATATATATA !" with hpunch
    stop sound
    scene gym
    show din Standard Colere at center with flash
    play music "<from 1.0>music/sb_tomorrow.mp3"
    din "STOOOOOP !!!" with hpunch
    din "On a dit que c'était un visual novel, pas un shônen ! Alors on se calme !"
    hide din

    scene gym_shonen
    play music "<from 31.0>music/sb_pursuit.mp3"
    show aura3 zorder 1000
    show Lock Standard Colere at center with flash
    lock "TU te calmes ! C'est MON arc narratif !"
    hide aura3
    hide Lock

    
    show Medoc Standard Sourire at center
    
    show auraSaintSeya behind Medoc with flash 
    play sound auraSeiya
    med "Brûle ! Brûle ! Ma cosmo-énergie !" with hpunch
    stop sound
    hide auraSaintSeya
    hide Medoc

    scene gym with fade
    play music "<from 31.0>music/sb_tomorrow.mp3"

    show din Standard Colere at center
    din "Allez hop ! Police des auras ! On enlève tout ça !"

    scene gym_shonen
    show Medoc Standard Sourire at center
    play music "<from 31.0>music/sb_pursuit.mp3"
    
    show Medoc BrasCroises Degoute at center
    show auraSaintSeya behind Medoc with flash 
    play sound auraSeiya
    med "Mais non..."
    hide auraSaintSeya
    hide Medoc
    stop sound

    show auraDBZ zorder 1000
    play sound auraDBZ loop
    show Moguri PoseDroite Degoute at center
    mog "Ok, police des auras je l'ai, mais désolé ça marche pas..."
    


    scene gym 
    stop sound
    play music "<from 31.0>music/sb_tomorrow.mp3"

    show din Standard Colere Rougit at center
    din "Ouais bah en attendant je dessine, et je décide qu'on n'est pas dans un shônen !"
    hide din
    show ZePilot PoseSpeciale Colere
    zep "Ouais puis tous ces effets, vous croyez que ça ce fait comme ça tout seul !? J'envoie la facture à qui ??"   

    scene gym_shonen
    
    play music "<from 31.0>music/sb_pursuit.mp3"

    show Lock Standard Colere  
    show aura3 zorder 1000 with flash


    lock "Wowowowo ! C'est MON arc narratif ! Laissez-moi faire lectrisité !"
    hide Lock

    hide aura3
    show auraDBZ zorder 1000
    play sound auraDBZ loop
    show Moguri Standard Degoute
    mog "Mais qui a écrit ça ?"
    mog "Les personnages arrivent comme ça sans prévenir et ils modifient l'histoire ?"

    show Moguri Standard Triste 
    mog "Et on peut tous casser le quatrième mur... comme ça ?"
    show Moguri Standard Colere
    mog "C'est complètement baisé votre truc là !"
    show Moguri Standard Badboy
    mog "Ah bah d'ailleurs, moi aussi je parle la langue des serpents ! Allez hop !"
    noName "Moguri décide que c'est la fin du jeu. Avec quel personnage souhaites-tu vivre longtemps et avoir beaucoup d'enfants ? Ou juste passer la nuit, c'est comme tu veux..."
    
    menu:
        "Moguri évidemment ! ":
            python:
                pointsmoguri+=1

        "Ah bah Moguri alors !":
            python:
                pointsmoguri+=1

        "Medoc ! (Mais en fait non ! Moguri !)":
            python:
                pointsmoguri+=1
    
    show auraDBZ zorder 1000
    play sound auraDBZ loop
    show Moguri Standard Sourire at center
    mog "Meilleur choix !"
    hide Moguri
    hide auraDBZ
    stop sound
    show aura3 zorder 1000
    show Lock PoseDroite Colere
    lock "Ici c'est l'école du petit couteau ! Pas le club tech ! Alors CALMEZ-VOUS ! "
    show Lock Standard Colere
    pause(0.5)
    show Lock PoseSpeciale Colere 
    pause(0.2)
    show Lock PoseSpeciale Furie with hpunch
    pause(0.2)
    hide Lock
    hide aura3
    
    python:
        pointsmoguri-=1
        renpy.movie_cutscene("movies/le_petit_couteau.webm", stop_music=False)

    
    show din Standard Colere  with flash
    din "Aie !" with hpunch
    hide din
    show Medoc Standard Colere at left with hpunch
    med "Hey !"
    hide Medoc
    show Moguri Standard Colere at right with hpunch
    mog "Waaaaa !"
    hide Moguri
    show ZePilot PoseSpeciale Furieux with hpunch
    zep "On dépasse clairement le budget là !"
    hide ZePilot  
    
    show Lock PoseSpeciale Colere at center
    lock "Allez ! Cassez-vous avant que je ne m'énerve vraiment !"
    lock "C'est pas un club de bébé Cadum ici !"
    scene gym
    show Lock Standard Badboy at center
    lock "[povname], c'est bon on peut continuer ?!"
    lock "Troisième épreuve : le lancer des mille petits couteaux !"
    pov "Ça, je devrais pouvoir y arriver."
    show Lock Standard Sourire at center
    lock "Ah! Mais c'est moi qui lance, toi tu fais la cible !"
    pov "Que... QUOI ???"
    pov "Mais t'es complètement malade ?"
    pov "En fait, tu sais quoi ? Je vais trouver un autre club... Plus calme..."
    show Lock Standard Degoute at center
    pause 3.0
    jump club_jeux_societe
    return
