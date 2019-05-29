
label conseil_eleves:
    play music wonderful    
    scene school hallway night with longfade

    show Metalice BrasCroises Sourire
    met "Bon, je t'emmène à la salle du conseil des élèves."

    scene black
    image name_club_conseil = Text("{size=80}Chapitre 8 :\nLe conseil des élèves", text_align=0.5)
    window hide
    show name_club_conseil:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(2)
    hide name_club_conseil
    window auto

    scene school hallway night
    show Metalice BrasCroises Cligne
    met "Par contre je te demanderai de te tenir tranquille certains membres sont... un peu à cheval sur le protocole."
    innerpov "Houlà, ça a l'air hyper sérieux !"
    if sex == "m":
        pov "Ok pas de soucis, je me ferai tout petit."
    else:
        pov "Ok pas de soucis, je me ferai toute petite."

    scene classroom night with longfade

    show Metalice PoseSpeciale Sourire at right
    met "Coucou tout le mo..."
    show Metalice PoseSpeciale Degoute
    show Lock BrasCroises Colere at left
    lock "NON ! JE VOUS LAISSERAI PAS FAIRE ! C'EST CONTRE LES RÈGLES !" with vpunch
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
    lock "Il vaut mieux respecter les règles qui nous permettent de vivre correctement en société ou bien tomber dans la destruction et le chaos ?"
    menu:
        lock "{cps=0}Il vaut mieux respecter les règles qui nous permettent de vivre correctement en société ou bien tomber dans la destruction et le chaos ?{/cps}"    
        
        "Les règles c'est important !":
            show Metalice PoseDroite Colere Rougit
            met "Ça suffit Lock ! [povname] n'est pas là pour ça."
        "Le fun avant tout !":
            show Metalice PoseDroite Colere Rougit
            met "Ça suffit Lock ! [povname] n'est pas là pour ça."
        "Elle est pas un peu orientée ta question ?":
            show Metalice PoseDroite Colere Rougit
            met "Ça suffit Lock ! [povname] n'est pas là pour ça."

    show Mickey Standard Badboy
    mic "Alors comme ça tu veux rejoindre le conseil des élèves ?"
    pov "Je ne sais pas encore. Quel est, concrètement, le travail du conseil ?"

    show Lock PoseDroite Sourire
    lock "On est là pour protéger les élèves, rendre la justice et défendre l'honneur et le prestige de l'école contre tous ses détracteurs !"
    
    show Mickey Standard Sourire
    mic "Alors dans les faits, vous servez surtout de lien privilégié entre les professeurs et les élèves et surveillez que personne ne fasse de grosses bêtises."
    show Metalice PoseDroite Sourire
    met "On est là pour désamorcer les problèmes avant qu'ils arrivent, sous la tutelle de M. Max."
    show Mickey Standard Sourire Yeuxfermes Rougit
    pov "Vous avez de grosses responsabilités quand même."
    show Lock PoseGauche Sourire
    show Mickey Standard Sourire Yeuxfermes
    show Metalice PoseDroite Cligne
    met "C'est rien de le dire !"
    show Metalice PoseDroite Gene
    show Mickey Standard Sourire 
    met"Avec toutes les fortes têtes de la Cosy Académie et les différentes tensions internes, on est tout le temps sur la brèche."
    pov "Ça c'est sûr. Mais vous avez déjà réglé des problèmes graves ou dû prendre des décisions difficiles ?"
    show Metalice PoseDroite Sourire
    met "Bien sûr, c'est notre pain quotidien même."
    show Metalice PoseDroite Sourire
    met "La fermeture du club d'archerie suite à un contact tête/flèche, la mise en place de vidéo surveillance autour du parc à vélo pour éviter le crevage industriel de pneus..."
    show Lock PoseGauche Badboy
    lock "On a fait retirer toutes les échelles suite à l'incident de La Chute aussi."
    pov "« L'incident de la chute ? »"
    show Metalice PoseDroite Gene
    met "Un accident bête et regrettable."
    show Metalice PoseDroite Cligne
    show Mickey Standard Triste
    mic "Oui, pendant un cours de sport, les élèves devaient effectuer un parcours d'obstacles avec un moment donné un mur avec une échelle à monter et une à descendre."
    mic "La plupart des élèves s'en sont sortis haut la main... À part..."
    show Mickey Standard Gene
    mic "À part Medoc... C'est sans doute par fierté, mais il n'a jamais voulu avouer qu'il ne savait pas descendre les échelles. Un traumatisme de l'enfance, sûrement... Donc une fois arrivé en haut, il a sauté."
    pov "NON ?!"
    show Mickey Standard Badboy Rougit
    show Lock PoseGauche Degoute
    lock "Si. Résultats : 2 chevilles brisées nettes, pour un total de 6 fractures ouvertes ! D'où l'interdiction de mettre des échelles dans l'Académie."
    show Mickey Standard Badboy
    show Metalice PoseDroite Degoute
    met "Des milliers d'euros pour changer toutes les échelles de secours en escaliers. Mais qu'est-ce que l'argent quand il s'agit de la vie d'un élève, aussi turbulent soit-il ?"
    show Metalice PoseDroite Sourire
    show Mickey Standard Sourire
    pov "Vous ne rigolez pas avec la sécurité !"
    show Lock PoseGauche Sourire
    lock "HAHAHA! Mais c'est pas la sécurité ça !"
    pov "Ah bon ?"
    show Mickey Standard Badboy
    show Lock BrasCroises Badboy
    lock "La sécurité c'est quand le Défenseur Élémentaire Tactique Avec Force d'Opération de Riposte Circulaire E prend les choses en main."
    pov "Le quoi ?"
    show Metalice PoseDroite Cligne
    met "Oh non, pas encore..."
    show Mickey PoseGauche Gene
    mic "Et il remet ça..."
    show Lock PoseGauche Sourire
    lock "Le DELTA FORCE, le membre le plus actif en terme de sécurité de la Cosy Académie !"
    show Lock PoseGauche Badboy
    lock "Le fleuron de la justice nationale de la région, le défenseur de la veuve, de l'orphelin et du mignon !"
    show Metalice PoseDroite Degoute
    met "Alors, déjà, on a pas de veuves et les orphelins se débrouillent très bien tous seuls à nos âges."
    show Metalice PoseDroite Cligne
    met "Pour le nom à rallonge, c'est le nom de code que Lock s'attribue quand il est en patrouille."
    show Metalice PoseDroite Gene
    met "Enfin, il est un peu tout seul dans son truc..."
    innerpov "Il a l'air un peu trop dans son délire sécurité, il me fait limite penser à Von Yaourt quand il est comme ça."

    lock "Je crois que vous ne vous rendez pas compte des enjeux qui se jouent sous nos yeux."
    lock "Pas plus tard qu'hier, j'ai croisé un type bizarre au regard louche qui traînait autour des labos de chimie."
    met "Moguri ?"
    lock "Non ! Je l'ai intimé de décliner son identité, mais il a disparu dans un nuage de fumée."
    met "Ah ! Un petit ? Avec un oeil tourné vers le passé, et l'autre vers l'avenir ?"
    lock "Oui ! C'est le bon signalement !"
    met "Plutôt caucasien, la chevelure bouclée ? Portant une tunique ?"
    lock "Tout à fait !"
    met "Ah non, ça ne me dit rien du tout..."
    lock "MAIS...?"
    mic "Alors, il me semble qu'il s'agit du Sire Flamel... C'est un intervenant extérieur ! Il est la pour dispenser des cours de chimie autour du thème ''le THC Philosophal'', un type brillant."

    lock "Pourquoi personne ne m'a prévenu ? Où se trouve son formulaire d'inscription ? Comment je peux préserver le calme si on me met des bâtons dans les roues ?"
    met "Au moins tes roues ont toujours leurs peuneus..."
    innerpov "Oh Dieuvomi, mais qu'es-tu devenu ?"
    lock "Tu vois [povname], on a clairement besoin de quelqu'un qui sait remplir les formulaires."
    lock "D'ailleurs, remplis-moi ce petit questionnaire à destination des nouveaux élèves s'il te plaît. Il en va de la sécurité de tout un chacun."
    innerpov "Wow, mais il y a au moins 100 pages ! Ce type est fou !"
    met "Mais Lock ? On avait dit non au questionnaire à la dernière réunion !"
    lock "Non, vous m'avez demandé de condenser. J'ai condensé et divisé par 4 le nombre de questions."
    met "..."
    mic "..."
    lock "Faites bien attention."
    met "À quoi ?"
    lock "Réfléchissez-y, vous le saurez. Moi. Je. Sais."

    show Mickey PoseSpeciale Sourire
    mic "Faudrait vraiment que tu penses à mieux suivre mes cours sur les terrasses Lock, ça te calmerait je pense."
    innerpov "Lock est vraiment mignon et chaotique à la fois, c'est... troublant."
        
    met "Tu as vu [povname], le conseil des élèves nécessite une main d'enfer, dans un gant dévolu."
    met "En plus de la rédaction des formulaires, leur diffusion, leur réception, ainsi que le maintien de l'ordre, ou la délation, nous aurions besoin de tes compétences."

    lock "Concernant les délations, l'élève Von Yaourt a encore rempli la banette. Principalement pour des délits mineurs commis par, je cite : ''des personnes aux accents étrange(r)s''. Je donne suite ?"
    met "Comme tu veux Lock, mais fais-le loin."
    met "Alors [povname], je t'inscris au conseil ?"
    menu:
        met "{cps=0}Alors [povname], je t'inscris au conseil ?{/cps}"
        
        "Ah, j'aurais adoré, mais je crois que vous avez la maîtrise de la situation.":
            show Metalice PoseDroite Colere Rougit
            met "Je comprends, j'ai l'habitude de carry tout le monde. Je me rends compte du vertige que donnent les responsabilités du conseil."
        "Bien entendu. Mais pas de facon officielle, je préfère euh... être un agent de l'ombre ?":
            show Metalice PoseDroite Colere Rougit
            met "Quelle bonne idée ! Alors, ne reste pas là, nous devons rester discrets, special agent [povname] !"

    jump sad_no_club
    return
