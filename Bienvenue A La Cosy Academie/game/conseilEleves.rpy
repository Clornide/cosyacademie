
label conseil_eleves:
    play music wonderful    
    scene school hallway night with longfade

    show Metalice BrasCroises Sourire
    met "Bon, je t'emmène à la salle du conseil des élèves."
    show Metalice BrasCroises Cligne
    met "Par contre je te demanderais de tenir tranquille certains membres sont... un peu à cheval sur le protocole."
    innerpov "Houlà, ça a l'air hyper sérieux !"
    if sex == "m":
        pov "Ok pas de soucis, je me ferait tout petit."
    else:
        pov "Ok pas de soucis, je me ferait toute petite."

    scene classroom night with longfade

    show Metalice PoseSpeciale Sourire at right
    met "Coucou tout le mo..."
    show Metalice PoseSpeciale Degoute
    show Lock BrasCroises Colere at left
    lock "NON ! JE VOUS LAISSERAIS PAS FAIRE ! C'EST CONTRE LES RÈGLES !" with vpunch
    innerpov "Ouah, ça chauffe !"
    show Metalice BrasCroises Degoute
    show Mickey PoseSpeciale Colere with vpunch
    mic "Tout le monde fait comme ça, lâche un peu du lest !"
    lock "SI TOUT LE MONDE COMMENCE À NE PLUS SUIVRE LES RÈGLES ÇA VA ÊTRE LE CHAOS !"
    show Mickey PoseSpeciale Sourire
    mic "Oui, bah là, tu suis ces règles là et tu pioches 4 cartes parce qu'on peut cumuler les +2 et +4 en contre."
    pov "… De quoi ?"
    show Metalice PoseDroite Cligne
    if sex == "m":
        met "Du calme Lock! On a un invité."
    else:
        met "Du calme Lock! On a une invitée."
    show Mickey Standard Sourire
    mic "Bonjour [povname] !"
    show Lock PoseGauche Colere
    lock "Tu tombes bien [povname], tu vas pouvoir trancher :"
    
    menu:
        lock "Il vaut mieux respecter les règles qui nous permettent de vivre correctement en société ou bien tomber dans la destruction et le chaos ?"
        
        "Les règles c'est important !":
            show Metalice PoseDroite Colere Rougit
            met "Ça suffit Lock![povname] est pas là pour ça."
        "Le fun avant tout !":
            show Metalice PoseDroite Colere Rougit
            met "Ça suffit Lock![povname] est pas là pour ça."
        "Elle est pas un peu orientée ta question ?":
            show Metalice PoseDroite Colere Rougit
            met "Ça suffit Lock![povname] est pas là pour ça."

    show Mickey Standard Badboy
    mic "Alors comme ça tu veux rejoindre le conseil des élèves ?"
    pov "Je sais pas encore. C'est quoi le travail concrètent du conseil ?"

    show Lock PoseDroite Sourire
    lock "On est là pour protéger les élèves, rendre la justice et défendre l'honneur et le prestige de l'école contre tous ses détracteurs !"
    
    show Mickey Standard Sourire
    mic "Alors dans les fait vous servez surtout de lien privilégié entre les professeurs et les élèves et surveillez que personne ne fasse de grosses bêtises."
    show Metalice PoseDroite Sourire
    met "On est là pour désamorcer les problèmes avant qu'ils arrivent, sous la tutelle de M. Max."
    show Mickey Standard Sourire Yeuxfermes Rougit
    pov "Vous avez de grosses responsabilités quand même."
    show Lock PoseGauche Sourire
    show Mickey Standard Sourire Yeuxfermes
    show Metalice PoseDroite Badboy
    met "C'est pas rien de le dire!"
    show Metalice PoseDroite Gene
    show Mickey Standard Sourire 
    met"Avec toutes les fortes tête de la Cosy Académie et les différentes tensions internes, on est tout le temps sur la brèche."
    pov "Ça c'est sûr. Mais vous avez déjà réglé des problèmes graves ou due prendre des décisions difficiles ?"
    show Metalice PoseDroite Sourire
    met "Bien sûr, c'est notre pain quotidien même."
    show Metalice PoseDroite Sourire
    met "La fermeture du club d'archerie suite au contact tête/flèche, la mise en place de vidéo surveillance autour du parc à vélo pour éviter le creuvage industriel de pneus..."
    show Lock PoseGauche Badboy
    lock "On a fait retirer toutes les échelles suite à l'incident de la chute aussi."
    pov "« L'incident de la chute ? »"
    show Metalice PoseDroite Gene
    met "Un accident bête et regrettable."
    show Metalice PoseDroite Badboy
    show Mickey Standard Triste
    mic "Oui, pendant un cours de sport, les élèves devaient effectué un parcours d'obstacle avec un moment donné un mur avec une échelle à monter et une à descendre."
    show Mickey Standard Gene
    mic "Mais Médoc, par fierté sans doute, n'a jamais voulue avouer qu'il ne savait pas descendre les échelles. Donc une fois arriver en haut, il a sauté."
    pov "NON ?!"
    show Mickey Standard Badboy Rougit
    show Lock PoseGauche Degoute
    lock "Si. Résultats : 2 chevilles brisées nets, 6 fractures en tout et interdiction de mettre des échelles dans l'académie."
    show Mickey Standard Badboy
    show Metalice PoseDroite Degoute
    met "Ça a fait des milliers d'euros pour changer toutes les échelles de secours en escalier."
    show Metalice PoseDroite Sourire
    show Mickey Standard Sourire
    pov "Vous rigolez pas avec la sécurité !"
    show Lock PoseGauche Sourire
    lock "HAHAHA! Mais c'est pas la sécurité ça !"
    pov "Ah bon ?"
    show Mickey Standard Badboy
    show Lock BrasCroises Badboy
    lock "La sécurité c'est quand le Défenseur Élémentaire Tactique Avec Force d'Opération de Riposte Circulaire E prend les choses en main."
    pov "Le quoi ?"
    show Metalice PoseDroite Badboy
    met "Oh non, pas encore..."
    show Lock PoseGauche Sourire
    lock "Le DELTA FORCE, le membre le plus actif en terme de sécurité de la Cosy Académie!"
    show Lock PoseGauche Badboy
    lock "Le fleuron de la justice, le défenseur de la veuve et de l'orphelin !"
    show Metalice PoseDroite Degoute
    met "Alors, déjà on a pas de veuve et les orphelins se débrouillent très biens tous seuls à nos âge."
    show Metalice PoseDroite Badboy
    met "Pour le nom à rallonge, c'est comme ça que Lock veut qu'on l'appelle quand il est en patrouille."
    innerpov "Il a l'air un peu trop dans son délire sécurité, il me fait limite penser à Von Yaort quand il est comme ça."
    show Mickey PoseSpeciale Sourire
    mic "Faudrait que tu penses à mieux suivre mes cours sur les terrasses Lock, ça te calmerait je pense."
