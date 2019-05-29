image SNL = "Assets/SNL.png"

label club_comedie:

    scene black
    image name_club_comedie = Text("{size=80}Chapitre 2 :\nLe club de comédie", text_align=0.5)
    window hide
    show name_club_comedie:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(2)
    hide name_club_comedie
    window auto

    play music wonderful
    scene school hallway with fade
   
    show Dieuvomi BrasCroises Badboy

    dieuv "Hey, salut ? Bah alors t'as décidé de pas rester avec les gros nazes ? Tu viens avec nous ?"
    

    pov "Ça dépend, heu vous faites quoi concrètement ?"
    
    show Dieuvomi Standard Sourire
    dieuv "Ce qu'on fait ? Mais on change le monde une blague à la fois avé le Foulk là."
    pov "Heu, c'est possible ça ? C'est pas juste un club d'humour ?"
    show Dieuvomi Standard Badboy
    dieuv "Si, si je te jure. On utilise un genre d'humour pour lutter contre l'oppression de droite, et aussi pour crever des peuneus."
    show Dieuvomi BrasCroises Sourire
    dieuv "C'est que ça fait voyager. Et bah oui c'est un club, on a pas trouvé autre chose encore."
    pov "Et... ça marche ?"
    show Dieuvomi PoseGauche Degoute
    dieuv "Bah pour l'instant on a été à une salle des fêtes à coté une fois... pour voir un autre truc. Mais hé. C'est normal qu'on galère, on dérange, on bouge les choses."
    show Dieuvomi PoseGauche Sourire
    dieuv "Mais assez parlé notre avenir, et le tien ? T'en penses quoi ? T'aimerais nous rejoindre ? Tu veux faire partie du problème ou nous rejoindre et faire partie de la solution ?"
    pov "Houlà ! vous avez l'air vachement engagés !"
    show Dieuvomi Standard Badboy
    dieuv "Mais ouais ! Moi j'écris, je compose, je suis un peu un genre de cerveau."
    dieuv "Et Foulk, lui se charge de transmettre le message."
    pov "Et du coup, par exemple, de quoi vous parlez ?"
    show Dieuvomi Standard Sourire
    
    if sex=="m":
        dieuv "Ahahahah t'es curieux, c'est marrant et je te comprends."
    else:
        dieuv "Ahahahah t'es curieuse, c'est marrant et je te comprends."
    
    dieuv "Je peux rien te dire, imagine un peu que les pouvoirs en place tombent sur ce brûlot d'humour, comment on serait pas dans la merde."
    show Dieuvomi Standard Sourire Rougit
    dieuv "Pour l'instant je peux dévoiler que le titre : « Foulk'on Rigole »"
    pov "Mais... c'est nul."
    show Dieuvomi Standard Colere at bigzoom with vpunch 
    dieuv "JE SAIS QUE C'EST NUL !"
    show Dieuvomi PoseDroite Colere
    dieuv "C'est pas ce que je voulais de toute façon, j'avais « C'est quoi le problème avec la bouffe dans les avions ?», un spectacle qui crève les peuneus de l'esprit."
    show Dieuvomi BrasCroises Colere at normalzoom
    dieuv "Mais ouais, Foulk voulait faire le sien d'abord. J'y peux quoi ? Hein tu me cherches en fait ?"
    pov "Non... je.."
    show Dieuvomi Standard Sourire
   
    if sex=="m":
        dieuv "AHAHAHAHAH je déconne, tu vois, tu t'es laissé piéger par les pièges de mon humour."
    else:
        dieuv "AHAHAHAHAH je déconne, tu vois, tu t'es laissée piéger par les pièges de mon humour."
    
    dieuv "T'as gambergé un peu le délire ? Tu crois que je vais te casser la gueule à coups de chaînes et en fait c'était pour déconner. La base de l'humour."
    pov "Ahahah..."
    innerpov "C'est gênant."
    pov "Ben c'est vrai que c'est plutôt étonnant effectivement."
    if sex=="m":
        innerpov "Mon dieu qu'ils sont nuls je suis plus vraiment sûr d'avoir envie de faire partie de ça."
    else:
        innerpov "Mon dieu qu'ils sont nuls je suis plus vraiment sûre d'avoir envie de faire partie de ça."
    
    if sex=="m":
        dieuv "Bon alors, tu penses que tu pourrais nous rejoindre ? Tu m'as l'air un peu trop mignon pour ça."
    else:
        dieuv "Bon alors, tu penses que tu pourrais nous rejoindre ? Tu m'as l'air un peu trop mignonne pour ça."
    innerpov "Oh je vais rougir..."
    innerpov "On dirait bien que dieuvomi a des sentiments sous cette carapace de gros dur, peut-être que... "
    show Dieuvomi BrasCroises Badboy
    dieuv "OH ! Tu jactes rien là, tu viens ou quoi ?"
    pov "Je veux bien essayer, je te suis !"


    stop music fadeout 1.0

    scene theater with fade
    play music comedy
    pov "Alors c'est ici que la magie opère ?"
    show Dieuvomi PoseGauche Badboy at left
    dieuv "Et ouais, bon fais pas gaffe à l'esthétique bourgeoise, on va bosser là-dessus."
    show Dieuvomi PoseGauche Colere
    dieuv "Apparemment les bidons d'essences c'est interdit dans l'enceinte de l'académie... "
    dieuv "Tu parles, on aurait fait une super déco."
    show Dieuvomi PoseGauche Badboy
    dieuv "Mais bon on fait avec ce qu'on a. Bon alors Foulk va t'interpréter un extrait de son spectacle."
    pov "Wah vraiment ? Tu crois que... "
    show Dieuvomi PoseGauche Colere
    if sex=="m":
        dieuv "Tais-toi, tu dois dire à personne ce que t'as vu. Comment t'es venu au bahut ce matin ?"
    else:
        dieuv "Tais-toi, tu dois dire à personne ce que t'as vu. Comment t'es venue au bahut ce matin ?"
    pov "Ben à vélo comme tous les... "
    show Dieuvomi PoseGauche Degoute
    dieuv "Très bien, disons que... si tu dis quoi que ce soit t'aimerais pas que... hein ?"
    pov "J'ai rien compris..."
    show Dieuvomi PoseGauche Badboy
    dieuv "Ben dis rien et ça se passera bien pour une certaine partie de l'anatomie mécanique de ton vélo. Tu piges ?"
    innerpov "Il pense vraiment qu'à crever des trucs... Et... Il crève vraiment des pneus avec ses chaînes ? C'est physiquement possible ? "
    show Dieuvomi PoseGauche Colere with hpunch
    dieuv "FOULK !"
    show Dieuvomi PoseGauche Badboy
    show Foulk PoseDroite Colere at right with fade
    foulk "QUOI ?"
    show Dieuvomi PoseGauche Colere
    show Foulk PoseDroite Badboy
    dieuv "T'AS DU PUBLIC, T'ES PRÊT ?"
    show Foulk PoseDroite Colere
    show Dieuvomi PoseGauche Badboy
    foulk "OUAIS CONG MILADIOU!"
    hide Dieuvomi
    hide Foulk
    show Foulk BrasCroises Badboy at center with fade

    
    foulk "Tout le monde : *se drague sur Tinder et en soirée, crée un jeu de séduction sensuel et mystérieux où se mêle le non-dit et une promesse de luxure*"
    foulk "Moi : des fois je prends des douches tout nu !"
    show Foulk PoseDroite Sourire Yeuxfermes
    pause 1.0
    show Foulk PoseGauche Sourire Yeuxfermes
    pause 1.0
    show Foulk PoseDroite Sourire Yeuxfermes
    play sound badamtsss
    pause 1.0
    

    show Foulk PoseSpeciale Badboy
    foulk "Hé t'aimes jouer ? Putin mais les g@m3rs vous êtes vraiment les Jacky Tuning du 21è siècle !"
    play sound badamtsss
    pause 1.0
    
    show Foulk PoseSpeciale Sourire
    foulk "Hé, je vous ai pas dit ? J'ai ajouté fafiot à mon vocabulaire comme tu ajoutes un poulet rôti à ta panse !"
    play sound badamtsss
    pause 1.0
    
    show Foulk Standard Sourire
    foulk "Au boulot, je crois que mon collègue pense regarder Game Of Thrones mais qu'il télécharge les feux de l'amour à la place !"
    foulk "Il a RIEN compris à l'épisode, c'est assez hallucinant."
    play sound badamtsss
    pause 1.0
    show Foulk PoseSpeciale Badboy
    
    foulk "D'ailleurs, j'ai une question qui me turlupine : pourquoi Jon Snow s'appelle Jon Snow, alors qu'il n'est pas né dans le Nord genre, du tout ?"
    play sound badamtsss
    pause 1.0
    show Foulk PoseSpeciale Sourire Rougit
    foulk "Hé, Mélissandre, call me, tu peux mettre des sangsues sur mon zgigou si tu veux."
    show Foulk PoseSpeciale Sourire Yeuxfermes Rougit
    foulk "Gendry, tu peux venir aussi, y a pas de soucis."
    play sound badamtsss
    pause 1.0

    
    show Foulk BrasCroises Triste
    foulk "Et c'est quoi cette haine autour de Pete Davidson d'un coup ?"
    show Foulk BrasCroises Badboy
    foulk "Y a des vrais bails qui traînent ou c'est les fans d'Ariana Grande qui s'excitent ? Les heu...Grandos ? Les Arianistes ?"
    play sound badamtsss
    pause 1.0
    
    show Foulk PoseDroite Sourire
    foulk "Ah, très très content que Joe Biden soit candidat parce que là, d'un coup, du Jason Sudeikis dans mon SNL."
    play sound badamtsss
    pause 1.0
    
    show Foulk PoseDroite Triste
    foulk "Mangez pas de la colle les enfants, c'est pas délicieux c'est pas vrai."
    play sound badamtsss
    pause 1.0
    
    show Foulk PoseSpeciale Sourire
    foulk "T'as vu avengers Endgame ?"
    show Foulk PoseSpeciale Sourire Rougit
    foulk "À 15 minutes du début, je suis excité comme une pute."
    play sound badamtsss
    show Foulk PoseSpeciale Degoute
    foulk "Attention spoiler : Le vrai grand méchant dans ce film, c'est ta propre vessie. La menace vient de l'intérieur."
    play sound badamtsss
    pause 1.0

    show Foulk Standard Sourire Rougit at left with fade
    foulk "Alors cong ? T'as bieng aimé ? Je sais je suis le poil à gratter dans la chaussure au vitriol."
    foulk " Mais voilà aussi cong, il faut bieng dénoncer."
    if sex=="m":
        innerpov "Ouah je suis pas sûr d'avoir déjà vu un truc aussi nul de ma vie !"
    else:
        innerpov "Ouah je suis pas sûre d'avoir déjà vu un truc aussi nul de ma vie !"
    
    show Foulk Standard Sourire at left
    show Dieuvomi BrasCroises Sourire Rougit at right

    dieuv "Alors ? Je te demande pas ton avis en vrai, je sais que c'est drôle."
    show Foulk Standard Sourire Rougit
    dieuv "Par contre je suis pas sûr que t'aies tout compris, je t'ai pas vu rigoler."
    pov "Heu ben c'est spécial, c'est beaucoup d'informations...."
    show Dieuvomi PoseDroite Sourire
    dieuv "Je sais, c'est possible que tu mettes plusieurs jours à saisir les subtilités de notre génie comique."
    show Dieuvomi PoseDroite Sourire Rougit
    dieuv "Mais fais gaffe, ta vie pourrait changer suite à ça."

    show Foulk PoseGauche Sourire
    if sex=="m":
        foulk "Hé oui milledieu, c'est normal que tu sois dérangé, on est toujours engagés ici cong."
    else:
        foulk "Hé oui milledieu, c'est normal que tu sois dérangée, on est toujours engagés ici cong."
    show Foulk PoseGauche Degoute
    foulk "J'espère que t'es pas de droite parce que sinon oulala. Je pense que tu vas changer d'avis."
    show Foulk PoseGauche Sourire Yeuxfermes
    show Dieuvomi PoseDroite Sourire Yeuxfermes
    pov "J'en doute pas une seconde..."
    innerpov "Mon dieu ils sont bien mignons les deux là, mais je vais quand même tenter de me tirer discrètement..."
    innerpov "Je peux pas faire partie de ce club c'est... nul."
    show Foulk PoseGauche Badboy
    show Dieuvomi Standard Sourire
    dieuv "Eh ouais... En vérité, j'utilise l'humour pour tenter de faire comprendre aux gens que sous ces chaînes se cache un coeur qui bat."
    show Foulk PoseGauche Gene
    foulk "NONG dieuvomi, ne te livre pas comme ça puté !"
    show Foulk PoseGauche Badboy
    innerpov "QUOI ? Mais qu'est-ce qu'il me fait là !?"
    show Dieuvomi Standard Sourire Rougit

    if sex == "m":
         dieuv "Tu vois, je peux te le dire à toi, t'as l'air inoffensif. Mais... tu sais avé le Médoc... t'as peut-être vu qu'on était... en froid..."
    else:
         dieuv "Tu vois, je peux te le dire à toi, t'as l'air inoffensive. Mais... tu sais avé le Médoc... t'as peut-être vu qu'on était... en froid..."
   
    show Foulk PoseGauche Sourire Yeuxfermes
    foulk "Oulala et voilà, tu nous l'as rendu triste. Attends je RT."
    pov "Oh ben à peine tu sais c'est norm..."
    show Dieuvomi PoseDroite Sourire
    dieuv "Ouais ben bref. En fait à la base, c'était lui le président du club."
    show Dieuvomi BrasCroises Badboy
    dieuv "On était les meilleurs, on avait une liste d'attente pour rejoindre le club. Tout le monde nous enviait."
    dieuv "Et puis... RAH ça fait mal d'en parler."
    show Dieuvomi BrasCroises Colere at bigzoom with vpunch
    dieuv "Mais... TU DIRAS RIEN HEIN ?"
    pov "Non promis, tu sais j'ai pas envie de me faire des ennemis, ici. Tu peux me dire !"
    show Dieuvomi BrasCroises Badboy at normalzoom
    dieuv "Hé bien, avé le Médoc un jour, on a trouvé la blague ultime."
    dieuv "Tu vois il avait un sketch où il jouait aux jeux vidéo le jeudi, il découvrait un jeu."
    dieuv "Au début c'était un peu poussif, on savait pas comment l'améliorer."
    dieuv "Puis j'ai désamorcé tout le truc. J'ai trouvé la molise ultime. Celle qui pourrait sauver le spectacle."
    pov "La quoi ?"
    show Dieuvomi BrasCroises Colere at normalzoom
    dieuv "MOT-VALISE"
    pov "Oooooh !"
    show Dieuvomi BrasCroises Badboy at normalzoom
    dieuv "Je disais donc que j'avais trouvé la molise ultime :"
    show Dieuvomi PoseSpeciale Sourire
    show Foulk PoseGauche Gene
    dieuv "JEUDICOUVERTE."
    pov "Jeudicouverte ?"
    show Dieuvomi PoseSpeciale Colere with vpunch
    dieuv "MAIS OUAIS PUTAIN, JEUDICOUVERTE !"
    show Dieuvomi BrasCroises Colere
    show Foulk PoseGauche Badboy
    dieuv "T'imagines ? Les jeux, le jeudi et la découverte ! Les trois concepts dans un seul mot."
    pov "OH MON DIEU MAIS CEST..."
    show Dieuvomi PoseSpeciale Gene
    dieuv "Génial je sais."
    show Dieuvomi PoseDroite Sourire
    show Foulk PoseGauche Badboy
    dieuv "Hé bien figure-toi que c'est ce que tout le monde pensait. On allait percer !"
    show Dieuvomi PoseDroite Triste
    dieuv "On allait bousculer le monde. Et puis Médoc s'est mis à changer, il était plus solitaire, plus secret. Il s'est attribué Jeudicouverte."
    
    show Foulk PoseGauche Sourire Yeuxfermes
    foulk "Attends cong, t'as pas vu le sketch du SNL, c'est le MEILLEUR. Attends, attends."

    dieuv "Mais putain Foulk, on parle de Médoc qui s'attribue Jeudicouverte là. Donc ouais, il s'est totalement approprié le truc."
    pov "Non ?"
    show Foulk PoseGauche Badboy
    show Dieuvomi BrasCroises Triste
    dieuv "Comme j'te dis. Il a monté son spectacle. Il a eu le succès qu'on connaît."
    show Dieuvomi PoseDroite Triste
    dieuv "Tu en as sûrement entendu parler ? C'était « Moi, Médoc et Jeudicouverte »."
    show Dieuvomi BrasCroises Triste
    dieuv "Tout le monde a adoré. Et, bien sûr, il m'a pas crédité."
    show Dieuvomi BrasCroises Colere
    dieuv "Pire, il m'a accusé de lui avoir volé concept."
    pov "Mais... c'est horrible."
    show Dieuvomi PoseDroite Colere
    pov "Et t'es sûr qu'il n'y a pas eu de malentendu ? Enfin, Médoc a l'air d'être une chouette personne, non ?"
    show Dieuvomi PoseDroite Triste
    dieuv "Gaffe à ce que tu dis. C'est sensible. Arf, je peux pas m'empêcher de toujours bien l'aimer, mais ça... il ne le sait pas."
    show Foulk PoseGauche Colere
    foulk "Quel guindoule celui là aussi le Médoc hein ? On aurait pu être plus gros que Jimmy Fallon puté."
    show Foulk PoseGauche Gene
    foulk "Et pis aussi ils s'aimaient bieng avec la dieuve là. C'était bieng ce temps-là."
    show Foulk PoseGauche Sourire Yeuxfermes
    foulk "On était comme dans le SNL, attends je vais te montrer le sketch."

    pov "Tu... l'aimes toujours ?"
    show Dieuvomi BrasCroises Triste
    dieuv "Je sais pas, tu comprends. Quelque chose s'est brisé ce jour là."
    show Dieuvomi Standard Badboy
    dieuv "Jeudicouverte... tu te rends compte ? Une telle puissance comique entre de mauvaises mains ?"
    show Dieuvomi PoseSpeciale Badboy
    dieuv "Enfin, depuis j'ai sombré dans la délinquance et je crève des peuneus."
    show Dieuvomi PoseSpeciale Sourire
    dieuv "Comme un acte de désespoir. Pour dire « je t'aime », BONNEUH MEREUH."
    pov "J'espère que ça s'arrangera."  
    show Dieuvomi BrasCroises Triste
    innerpov  "Mince qui aurait cru que ce délinquant juvénile cachait des sentiments ?"
    show Dieuvomi PoseDroite Badboy
    innerpov "La Cosy Académie n'est décidément pas un endroit comme les autres"
    show Dieuvomi PoseDroite Triste
    innerpov "Enfin, c'est bien beau tout ça mais il faudrait VRAIMENT que je trouve une issue."
    show Dieuvomi PoseDroite Badboy
    innerpov "Je n'ai vraiment pas envie de me ridiculiser avec les deux et leurs accents horribles là."
    pov "Tu penses que je pourrais en toucher deux mots à Médoc ?"
    pov "L'air de rien, il saura pas que je suis au courant de ce que tu ressens, je te le promets !"
    show Dieuvomi BrasCroises Badboy
    dieuv "QUOI ? Hmmmm... Et pourquoi pas ? Après tout on a jamais essayé le dialogue."
    pov "Tu lui en as jamais parlé ? "
    show Foulk PoseGauche Badboy
    show Dieuvomi PoseDroite Badboy Rougit
    dieuv "Non, pour quoi faire ? Il était au sommet et j'étais si petit. Je pouvais plus rien faire. Alors j'ai crevé des peuneus."
    pov "Mais... quel est le rapport ?"
    show Dieuvomi BrasCroises Badboy
    dieuv "Tu vois pas ? Hm je suis pas sûr que tu aies l'étoffe d'un vrai comique."
    dieuv "Tu vois pas à quel point c'est drôle de voir des peuneus crevés ? Ou des trucs en feu à la limite ? Ou les deux ?"
    show Dieuvomi PoseDroite Sourire Yeuxfermes Rougit
    dieuv "MMOUAHAHAHAHAHAHAHAH"
    show Foulk BrasCroises Degoute
    foulk "Oué là par contre cong, je te suis plus dieuvomi."
    show Foulk PoseSpeciale Sourire
    foulk "Faut toujours que tu fasses le comique avec les peuneus alors qu'on pourrait faire les sketches comme Bo Burnam."
    show Foulk PoseSpeciale Sourire Yeuxfermes Rougit
    foulk "Ouh oui, lui il est bieng. Il est siiiii bieng. On devrait être comme lui. TOUT LE MONDE. T'y es pas comme Bo Burnam toi, le nouveau là."
    show Foulk PoseSpeciale Sourire Yeuxfermes
    show Dieuvomi BrasCroises Badboy
    innerpov "Ok, donc c'est un psychopathe... je vais couper court."
    pov "Ahahah si, mais t'as raison."
    show Foulk PoseGauche Sourire Yeuxfermes
    show Dieuvomi PoseDroite Badboy
    pov "Je pense qu'il me reste beaucoup à apprendre sur l'humour."
    pov "Je vais pour l'instant garder ma place dans le public et je vous rejoindrai quand j'aurai saisi toutes les subtilités, d'accord ?"
    show Dieuvomi PoseDroite Triste
    dieuv "C'est le mieux pour l'instant."
    show Dieuvomi BrasCroises Colere at normalzoom
    dieuv "Mais RAPPELLE-TOI -"
    show Dieuvomi BrasCroises Colere with vpunch
    dieuv "PERSONNE -"
    show Dieuvomi BrasCroises Colere at lightzoom with vpunch
    dieuv "NE -"
    show Dieuvomi BrasCroises Colere at mediumzoom with vpunch
    dieuv "DOIT -"
    show Dieuvomi BrasCroises Colere at bigzoom with vpunch
    dieuv "RIEN -"
    show Dieuvomi BrasCroises Colere at hugezoom with vpunch
    dieuv "SAVOIR."
    show Dieuvomi PoseDroite Colere
    dieuv "Il vaut mieux pour toi. Et pour Médoc... bonne chance."
    hide Dieuvomi with dissolve
    show Foulk PoseSpeciale Sourire Yeuxfermes Rougit

        
    
    foulk "ATTENDS T'AS PAS VU LE SKETCH DU SNL !!"
    window hide
    pause 0.5
    show SNL zorder 1000 at snl_pos
    pause 5

    jump cours_physique

    return
