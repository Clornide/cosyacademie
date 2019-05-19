
image panneau = "Assets/PanneauxTech.png"

init python:

    last_choice = -1

    inner_pov_couloirs = ["Pourquoi il n'y pas de carte de l'Académie... Ça sert de lire une carte !",
            "Pourquoi il n'y pas de carte de l'Académie... Ça sert de lire une carte !",
            "Le club #tech ne doit plus être très loin !",
            "Nom de nom ! J'en reviens pas que Metalice éternue de la sorte. C'est vraiment la preuve que c'est une femme de caractère !",
            "J'en reviens pas qu'ils laissent faire des spectacles à ce Foulk. C'est surement subventionné par la région...",
            "Le club #tech ne doit plus être très loin, ça sent les nouilles !",
            "Trouvons ce club #tech ! Ze PilOt avait l'air tellement talentueux !",
            "Le Club #tech ? ah non, c'est #radiohead... aucun intérêt.",
            "Mais #tech et Matt Pokora... J'en peux plus, vivement que j'arrive...",
            "Encore un couloir et pas de club #tech...",
            "Ce club #tech est une opportunité unique ! ",
            "Dépot sauvage de peuneus interdit. Signé La direction.",
            "Mais c'est pas possible, je tourne en rond !",
            "Encore un couloir et pas de club #tech..."
    ]

    num_inner_pov_couloirs = len(inner_pov_couloirs)
    inner_pov_chosen = range(0, num_inner_pov_couloirs)

label club_tech:
    play music rainbow
    scene black
    image name_club_tech = Text("{size=80}Chapitre 3 :\nLe club #Tech", text_align=0.5)
    window hide
    show name_club_tech:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(2)
    hide name_club_tech
    window auto

    
    scene school hallway with longfade

    innerpov "La Cosy Académie... Je n'arrive toujours pas à y croire... C'est comme si je rêvais..."
    innerpov "Le secrétariat m'a indiqué de finaliser mon inscription auprès du club #tech afin d'obtenir ma Cosy carte d'élève... Ça sera la preuve que je ne rêve pas !"
    innerpov "Tiens, ne serait-ce pas Moguri ? Il a l'air agité... et quel est ce type à qui il parle ?"
    
    show Moguri PoseGauche Colere at right  with dissolve
    mog "... Mais utiliser mon nom, comme ça, tu aurais pu me demander avant quand même !"

    show ZePilot BrasCroises Sourire at left with dissolve
    zep "Ne le prend pas mal Mog' c'est juste un hommage... C'est un petit mod de Final Fantasy, personne ne remarquera que ça existe, et ca finira dans l'ombre."
    mog "Mais, tu ne te rends pas compte... Ton hommage, aussi génial soit-il, me met une pression de fou. J'ai déjà le Kevins Battle Royal à préparer ! C'est bien plus qu'un tournoi !"
    mog "Alors oui, c'est gentil, mais la prochaine fois, demande moi avant de diffuser ça sur les interwebs s'il te plait !"

    show ZePilot PoseGauche Sourire Yeuxfermes
    zep "Euh... on dit Internet Mog'."
    mog "Et arrête de m'appeler Mog !"
    innerpov "Ouh là. Ça a l'air tendu, je ne devrai peut-être pas les déranger, comme dirais Medoc ''un repli stratégique s'impose''. Demi tour et fuyons !"

    show Moguri Standard Sourire 
    mog "Oh [povname] ! Salut !"
    pov "Yo !"
    pov "Ah, Moguri, c'est toi ! Je..."
    innerpov "vite, vite [povname] trouve un truc ! Ils te regardent bizarrement."
    pov "Je... cherche... les PHOTOCOPIEUSES !"
    innerpov "Mais n'importe quoi ! Tu cherches le club #tech !"

    show Moguri PoseDroite Sourire Yeuxfermes
    mog "Ok, ok, ça a l'air de te tenir à coeur...Tu as de la chance, je suis justement avec la personne qu'il te faut."
    mog "Ze PilOt est notre petit génie de l'informatique à l'Académie ! Il est président du club #tech."
    mog "Ze PilOt, je te présen..."

    python:
        global name_zep
        name_zep="Ze_PilOt"

    show ZePilot Standard Sourire Yeuxfermes    
    zep "Bonjour 192.168.1.77 !"
    innerpov "Oh... ok...mais qu'est ce que raconte ce type ?"
    pov "Bonjour ! je suis [povname] et je viens d'arriver à l'Académie. C'est un honneur de vous rencontrer !"
    zep "C'est chouette que tu utilises le dernier Sansung, ses capacités d'encodages dynamiques sont assez folles ! Tu feras attention, ton firmware a des failles de sécurités bien connues."
    innerpov "Mais comment il sait ça ?"
    pov "Euh... oui, merci, je ferai attention..."
    zep "Tu trouveras les photocopieuses des élèves au club ''Technologies et Créations Hétéroclites (T.E.C.H)''. "
    zep "Profite-en pour rencontrer les membres du club, tu verras que l'Académie est à la pointe technologique : nous faisons tout en Ultra."
    zep "Notre club regroupe toutes sortes de talents : développeurs, serpentistes, memeurs fascinateurs, et bien plus encore !"
    zep "Je les préviens de ta visite imminente."

    pause 0.2
    show ZePilot Standard Badboy
    zep "Jarod ?"
    pov "Non, je suis [povname]."

    show Moguri PoseGauche Sourire Rougit
    mog "Haha, non, Ze PilOt a developpé un assistant personnel qui s'appelle Jarod... en référence à la Guerre des étoiles, je crois... Ils sont connectés en permanence, mais il y a encore quelques réglages à faire."

    show ZePilot Standard Colere Rougit
    zep "Mais arrête Jarod, puisque je te dis que non, je ne connais pas cette Siri !"
    zep "Mais... non ! Quoi ? Mon historique ? Mais ça n'a absolument rien à voir, ce n'est pas Siri à la pomme, c'est Siri la généreuse suédoise !"
    zep "Et comment... Oui bin j'étais intraçable en navigation privée !"

    mog "Ouh, ça devient génant ! File [povname],  tu n'as qu'à suivre les panneaux #tech, c'est relativement indiqué."
    if sex=="f":
        pov "Merci ! Je vous laisse ! Désolée de vous avoir interrompu... Et bon courage avec Jarod..."
    else:
        pov "Merci ! Je vous laisse ! Désolé de vous avoir interrompu... Et bon courage avec Jarod..."

    scene school hallway choice with longfade
    call .ChooseCouloir(0)
    jump club_otaku
    return

    

label .Clubtechmetalice:
    innerpov "Mais où se trouve ce club #tech ? C'est un vrai dédale cette Académie..."
    innerpov "Là ! un panneau !"
    met "WAAAAAARRRGGGGTCCHHHAAAAAA !" with vpunch
    pov "Kya !"

    show Metalice PoseSpeciale Sourire
    met "COUCOU [povname] ! Qu'est-ce qui t'arrive ? Quelque chose t'as fait peur ?"
    pov "Oh ! Metalice ! C'est toi ! Tu m'as... surprise. J'avais... la tête en l'air."
    met "Pardonne-moi ! Je ne voulais pas te faire sursauter. J'ai tellement l'habitude de carry que j'ai développé un sens hyperdeveloppé de la discrétion."
    innerpov "De la discré... Oh my... Je ne m'attendais pas à cet éternuement !"
    
    show Metalice PoseSpeciale Gene
    met "Je t'avoue que ça m'aide beaucoup pour attraper mon coup de vent de petit ami !"

    show Metalice BrasCroises Sourire
    met "D'ailleurs, tu ne l'aurais pas vu par hasard ? Je le cherche... Il doit encore trainer au Respawn Point, le café où se retrouvent les joueurs de sa trempe."
    if sex=="f":
        pov "Je ne l'ai pas vue, désolée."
    else:
        pov "Je ne l'ai pas vue, désolé."
    met "Mais, qu'est ce que tu fais dans ces couloirs au fait ?"
    pov "Je cherche le club #tech. J'ai croisé Ze PilOt qui m'a indiqué que des photocopieuses sont là bas."
    met "Oui, tu devrais trouver facilement !"

    show Metalice PoseGauche Degoute
    met "Au fait ? Tu as entendu la rumeur ?"
    pov "Non, de quoi s'agit-il ?"
    met "Ecoute, ce n'est surement qu'une rumeur, rien de plus, mais il parait qu'une nouvelle drogue circule à l'Académie. La DELTA FORCE mène l'enquête."
    pov "De la drogue !? Mais c'est affreux ! Compte sur moi pour ne pas y toucher !"
    met "Parfait ! Rappelle toi que ton comportement doit être à la hauteur de l'académie."
    met "Je file ! À plus tard !"
    pov "Metaaahh..."
    innerpov "Elle est partie si vite !"
    innerpov "Cette histoire de drogue m'inquiète..."

    return




label .Clubtechfoulk:

    innerpov "Ah ! Enfin quelqu'un ! Peut-être qu'il pourra me renseigner..."
    pov "Bonjour, est-ce que tu pourrais me dire où se trouve le club #tech ?"

    show Foulk PoseDroite Sourire Yeuxfermes with dissolve
    foulk "Ah le film d'Eric et Ramzy ?"
    pov "..."

    show Foulk PoseDroite Sourire
    foulk "Tu l'as ? Steack.... Eric, Ramzy, grosse source d'inspiration... Ni vous, minou...? Non ?"

    show Foulk PoseDroite Rougit
    foulk "Haha, t'aimes pas l'humour ? Moi j'adore l'humour ! L'humour ça fait bouger le monde !"
    innerpov "Pourquoi il me mets tellement mal à l'aise ?"

    show Foulk PoseDroite Sourire Yeuxfermes
    foulk "J'déconne Cong ! Tu trouveras le club tech en prenant à gauche au prochain couloir. Et surtout, passe voir mon spectacle !"
    hide Foulk with dissolve
    innerpov "Un spectacle !? Mais je l'ai déjà vu ! Soit il y a un problème temporel, soit ils ont un AUTRE spectacle..."
    innerpov "Ces deux perspectives m'angoissent..."

    show Foulk BrasCroises Triste
    foulk "Ah, et si tu croises un type de mauvais gout, à la cravate et aux chaussettes bleues, n'écoute pas ses indications : à part la droite, il ne connait rien d'autre."
    foulk "Eh beh, appelez moi Joseph Gordon Levitt'riole aujourd'hui ! Il faut que je la note celle-là, elle est trop fraiche !"
    pov "Ok ! Salut hein !"
    innerpov "Rho le lourd..."

    return



label .Clubtechcheerleaders:

    innerpov "Mais quel est ce bruit ?"
    noName "..."
    innerpov "On dirait des prières..."
    innerpov "Ça vient de derrière cette porte."

    noName "Ne regarde pas en arrière, nous sommes là pour rester \n la vie que nous avons connu, viendra un jour,"
    scene school hallway choice creepy with longfade
    show Cheerleaders Groupe Drop 
    innerpov "Encore eux ? Ces cheerleaders sont vraiment étranges ! Qu'est-ce qu'ils font ? "
    clornide Clornide Drop "On y est, à la limite, là où le futur (pas compris) \nle feu brulera, et ne mourra jamais..."
    samael Samael Drop "Ô grand Pansepignon, nous invoquons ton nom !"
    clornide "Regarde dans les yeux d'une nouvelle vie\n alors trouve moi, juste, trouve moi..."
    samael "Ô Grand Pansepignon, Bénis Nous de ta Présence, et Accepte ces Offrandes !"
    innerpov "Ils font flipper ces types !"
    clornide "Des étincelles voleront\n si nous crions non..."
    samael "Ô Grand Pansepignon, nous nous inclinons devant ton Drop !"
    clornide "Ce n'est pas comme ça que nous partirons \n nous sommes ceux qui ne lachons jamais !!"
    clornide "(pas compris)\n Nous ne grandirons jamaiiiis !!!"
    innerpov "Ils se partagent des pillules bizarres... Le Drop ! Metalice m'avait prévenu(e) !"
    clornide "Mais qui est là ? KONTAK !"
    if sex=="f":
        innerpov "Je suis reperée ! Vite le couloir !"
    else:
        innerpov "Je suis reperé ! Vite le couloir !"

    return


label .Clubtechdin:

    innerpov "Bon, je ne trouve pas ce satané club #tech ! "
    if sex=="f":
        innerpov "Je suis perdue, j'ai mal aux pieds, ces Pansepignoufs m'ont terrorisée ! Je n'en peux plus ! "
    else:
        innerpov "Je suis perdu, j'ai mal aux pieds, ces Pansepignoufs m'ont terrorisé ! Je n'en peux plus ! "
    
    show din PoseSpeciale Cligne Rougit
    din    "Tiens, [povname] ! QU'est ce que tu fais là ?"
    pov    "Oh Din ! Tu tombes bien ! Je cherchais la salle du club #tech... J'ai suivi des panneaux, mais tous les couloirs se ressemblent ici."
    
    show din PoseSpeciale Degoute
    din    "Ah, le club #tech ? Ecoute, je l'ai cherché pendant longtemps aussi... Mais..."
    din    "Je crois que c'est une légende urbaine... Tout le monde en parle, mais personne ne l'a jamais vu."
    pov    "Quoi ? Mais comment je fais mes photocopies ?"
    
    show din PoseSpeciale Cligne
    if sex=="f":
        din    "Si tu n'es pas pressée, passe au club Otaku, on en a une !"
    else:
        din    "Si tu n'es pas pressé, passe au club Otaku, on en a une !"

    show din PoseSpeciale Triste
    din    "Je t'aurai bien accompagnée, mais ça va être l'heure de l'entrainement des cheerleaders, et j'en profite pour travailler des poses anatomiques réalistes."
    pov    "Ta pugnacité t'honore Din ! Tu seras une super artiste !"

    show din PoseSpeciale Perv
    din    "Oh, l'important c'est de prendre du plaisir en ce que tu fais ! Et les corps tendus et en sueurs des cheerleaders sont une source d'inspiration sans fin... mais c'est TOI qui es supair !"
    din    "Je file, je ne veux pas en râter une miette ! A très vite [povname] !"

    return


label .ChooseCouloir(count_couloir = 0):

    if count_couloir == 0:
        scene school hallway choice
    else:
        $ randomnum = renpy.random.randint(1,10)
        if randomnum == 1:
            scene school hallway choice
        elif randomnum == 2:
            scene school hallway choice alt1
        elif randomnum == 3:
            scene school hallway choice alt2
        elif randomnum == 4:
            scene school hallway choice alt3
        elif randomnum == 5:
            scene school hallway choice alt4
        elif randomnum == 6:
            scene school hallway choice alt5
        elif randomnum == 7:
            scene school hallway choice alt6
        elif randomnum == 8:
            scene school hallway choice alt7
        elif randomnum == 9:
            scene school hallway choice alt8
        elif randomnum == 10:
            scene school hallway choice alt9

    with fade

    $ line_choice = "ERROR !!!"
    if count_couloir == 5:
        $ line_choice = "Ils auraient quand même pu faire un peu d'efforts sur ces décors, ça se voit le color swap.."
    elif count_couloir == 2:
        $ line_choice = "J'espère que ce n'est pas réellement un labyrinthe !"
    elif count_couloir == 7:
        $ line_choice = "Plus le temps passe, et plus la droite me tente..."
    elif count_couloir == 8:
        $ line_choice = "Ces types sont des malades ! Ils m'ont fait flipper !"

    else:
        $ randomnum = renpy.random.randint(1,5)
        if randomnum == 1:
            $ line_choice = "Tant de choix..."
        elif randomnum == 2:
            $ line_choice = "Autant lancer un dé..."
        elif randomnum == 3:
            $ line_choice = "ARGH !"
        elif randomnum == 4:
            $ line_choice = "J'aurais du m'acheter un mac."
        elif randomnum == 5:
            $ line_choice = "Gauche droite, c'est pareil au final non ?"

    
    innerpov "[line_choice]"
    menu:
        innerpov "{cps=0}[line_choice]{/cps}"

        "Prendre le couloir de Gauche":
            python:
                last_choice = 0

        "Aller tout droit":
            python:
                last_choice = 1        

        "Prendre le couloir de Droite":
            python:
                last_choice = 2
    python:
        count_couloir+=1

    if count_couloir == 1:
        call .Clubtechmetalice from _call_club_tech_Clubtechmetalice

    elif count_couloir == 3 and last_choice == 2:
        show Von Standard Sourire with dissolve
        von "A droite, toujours à droite !"
        hide Von with dissolve

    elif count_couloir == 4:
        if last_choice == 0:
            innerpov "Mais pourquoi ça sent le melon de Lectoure et le fois gras ?"
        else:
            innerpov "J'ai comme envie d'une croustade à la pomme vanillée..."

        call .Clubtechfoulk from _call_club_tech_Clubtechfoulk

    elif count_couloir == 5:
        innerpov "Là un panneau ! Enfin !"
        show panneau  at truecenter
        pause 4.0        

    elif count_couloir == 7:
        if last_choice == 0:
            show Von PoseSpeciale Colere with dissolve
            von "C'EST À DROITE !"
            hide Von with dissolve
        elif last_choice == 1:
            show Von Standard Badboy with dissolve
            von "Ne va pas à gauche, c'est un mirage. Droit devant, c'est une impasse."
            hide Von with dissolve


    elif count_couloir == 8:
        if last_choice == 0:
            if sex=="f":
                innerpov "Mais pourquoi il fait si froid d'un coup ici ? Je suis glacée !"
            else:
                innerpov "Mais pourquoi il fait si froid d'un coup ici ? Je suis glacé !"
        elif last_choice == 1:
            innerpov "C'est lugubre par ici..."
        else:
            innerpov "Quelque chose d'inhumain/de diabolique se dégage de ces murs..."

        call .Clubtechcheerleaders from _call_club_tech_Clubtechcheerleaders

        
    

    elif count_couloir==10:
        if last_choice == 0:
            innerpov "Ça sent le matcha et la peinture à l'huile. J'espère que c'est le club #tech !"
        elif last_choice == 1:
            innerpov "Ça sent le matcha et les crayons de couleurs. J'espère que c'est le club #tech !"
        else:
            innerpov "Ça sent le thé et les petits gateaux... J'espère que c'est le club #tech !"
        call .Clubtechdin from _call_club_tech_Clubtechdin
        return

    else:
        python:
            inner_chosen = inner_pov_couloirs[inner_pov_chosen.pop(renpy.random.randint(0,len(inner_pov_chosen)-1))]
        innerpov "[inner_chosen]"
    
    call .ChooseCouloir(count_couloir) from _call_club_tech_ChooseCouloir
    return
