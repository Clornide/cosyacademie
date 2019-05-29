label club_jeux_societe:
    play music ashes

    scene black
    image name_club_jeux = Text("{size=80}Chapitre 6 :\nLe club de Jeux", text_align=0.5)
    window hide
    show name_club_jeux:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(2)
    hide name_club_jeux
    window auto

    scene school hallway night with fade    

    innerpov "Allez, jeux de société maintenant ! J'espère que les membres seront normaux cette fois parce qu'il faut vraiment que je trouve un club à la fin de la semaine…"

    innerpov "Ah je crois que c'est ici."

    noName "*Knock knock knock*"

    innerpov "Wow… La porte s'est ouverte toute seule... Ça a l'air desert… Et pourtant plutôt cosy !"

    scene classroom night with fade

    pov "Hello ? Y a quelqu'un ? Personne ?"

    pov "Bon et bien… demi-tour alors…"

    noName "BIENVENUE, MORTEL, DANS L'ANTRE DE… Hmm… FLÛTE J'AI OUBLIÉ !!!"

    show Mathilde BrasCroises Colere with dissolve
    if mathilde_medoc == True:
        pov "Hum Mathilde, c'est ça ? Celle qui traîne avec Médoc ? Je savais pas que tu étais membre de ce club !"
    else:
        if sex=="m":
             pov "Hum Mathilde, c'est ça ? On s'est croisés au cours de physique. J'ai entendu dire que tu faisais partie de ce club ?"
        else:
             pov "Hum Mathilde, c'est ça ? On s'est croisées au cours de physique. J'ai entendu dire que tu faisais partie de ce club ?"
        
    show Mathilde BrasCroises Sourire

    mat "Oui c'est moi ! Je suis même présidente du club pour tout te dire !"

    show Mathilde BrasCroises Badboy

    mat "Attends c'est tout ce que t'inspire mon introduction ? Tu sais que ça fait des mois que j'attends que quelqu'un entre pour la placer !"

    pov "Pardon, mais le fait que tu aies oublié le nom a un peu minimisé l'effet..."

    pov "D'ailleurs, comment ça plusieurs mois ? Me dis pas que tu es toute seule dans ce club ?"

    show Mathilde Standard Colere Rougit

    mat "Quoi ? Non ! Pour qui tu me prends ! Je ne te permets pas de te moquer de moi !" 

    pov "Hein ? Mais non je posais juste une question ! Y a qui d'autre alors ?"

    show Mathilde Standard Gene

    mat "…"
    mat "Y a Medoc, il passe des fois…"

    pov "Donc deux membres ?"

    mat "Medoc n'est pas... vraiment membre en fait. Il vient pour être sympa je pense."

    pov "Donc tu es bien toute seule ?"

    show Mathilde Standard Colere Rougit

    mat "LA FERME ! Ça ne me dérange pas ! C'est juste que les gens sont trop stupides pour jouer à mes jeux !"

    pov "Je peux essayer quand même ?"

    show Mathilde Standard Degoute

    mat "Quoi ? Tu veux jouer ? À mes jeux ? Avec moi ? Arrête, je te crois pas !"


    
    if sex=="m":
        pov "Bah je me suis bien déplacé jusqu'ici non ?"
    else:
        pov "Bah je me suis bien déplacée jusqu'ici non ?"
    

    show Mathilde Standard Sourire 

    mat "Mmmm ok… Je vais chercher Médoc alors !"


    hide Mathilde with longfade

    show Mathilde Standard Sourire Yeuxfermes at left
    show Medoc PoseDroite Badboy at right 
    with dissolve

    if sex=="m":
        mat "Ah super nous revoilà [povname] ! Prêt ?"
    else:
        mat "Ah super nous revoilà [povname] ! Prête ?"
    

    med "[povname] ?"

    pov "Ah tiens salut Medoc ! Dis Mathilde, j'ai regardé les règles de ton jeu là, c'est pas hyper clair quand même…"

    show Mathilde PoseGauche Sourire Yeuxfermes

    mat "Mais si c'est simple ! Tu commences avec 3 cartes de ce paquet, et trois de celui-ci, tu commences en lançant ce dé et…"

    show Medoc PoseDroite Sourire Yeuxfermes

    med "PUH ! On n'a qu'à faire un tour et on verra !"

    if sex=="m":
        pov "Je suis pas sûr que…"
    else:
        pov "Je suis pas sûre que…"
    

    show Mathilde PoseGauche Sourire

    mat "Allez commençons ! Alors on est trois donc je pense qu'il faut utiliser le mode de jeu 'Thalès'…"

    pov "Comme le truc du triangle là ?"

    show Medoc BrasCroises Sourire Yeuxfermes

    med "Nan comme le jeu, Thalès of Symphonia !"

    pov "Hein ?"

    show Mathilde Standard Colere Rougit

    mat "Roh ca va hein ! Je me suis trompée UNE fois !"

    med "Ahahah !"

    hide Medoc
    hide Mathilde
    show Mickey BrasCroises Sourire Yeuxfermes with dissolve

    mic "Dites, vous en faites du bruit ici… Tu as réussi à recruter Mathilde ?"

    show Mickey BrasCroises Sourire Yeuxfermes at left
    show Mathilde PoseDroite Sourire at right

    mat "Oh, m'sieur Max ! Non pas encore, mais c'est en cours on va dire… Vous voulez vous joindre à nous, on fera du 2v2 comme ça !"

    show Mickey PoseGauche Sourire

    mic "Allez, pourquoi pas !"

    hide Mathilde

    show Medoc BrasCroises Sourire Yeuxfermes at right

    med "J'me mets avec Mathilde ! On va vous écraser m'sieur Max !"

    show Mickey BrasCroises Sourire Yeuxfermes

    mic "Wow… Bon et bien allons-y [povname] !"

    hide Mickey
    hide Medoc
    with longfade

    show Mickey BrasCroises Triste

    mic "[povname]…"

    show Mickey BrasCroises Colere
    
    if sex=="m":
        mic "Mais comment on se fait défoncer gars !!!"
    else:
        mic "Mais comment on se fait défoncer meuf !!!"

    pov "Mais je SAIS ! Et puis comment vous parlez à vos élèves ?!"

    hide Mickey

    show Medoc PoseGauche Sourire Yeuxfermes at left
    show Mathilde PoseDroite Sourire Yeuxfermes at right

    med "Hinhinhin…"

    mat "Huhuhu…"

    pov "En même temps, à chaque fois que je pense comprendre les règles, je reprends un coup de Trafalgar… Comme s'ils…"

    pov "M'sieur Max... Je crois qu'ils trichent…"

    hide Medoc
    hide Mathilde
    show Mickey BrasCroises Degoute

    mic "Quoi ?! Mais évidemment qu'ils trichent ! C'est presque le principe de ce club !"

    mic "Je viens souvent jouer avec eux, et leur but c'est juste de m'écraser, peu importent les moyens mis en œuvre !"

    pov "Mais j'avais pas cette info ! Donc faut qu'on les en empêche je suppose ?"

    show Mickey BrasCroises Triste

    mic "Malheureusement je crois que vu l'écart des scores, il va falloir qu'on se mette à tricher aussi…"

    if sex=="m":
        pov "Quoi ? Mais je suis le pire menteur que je connaisse ! On va jamais y arriver !"
    else:
        pov "Quoi ? Mais je suis la pire menteuse que je connaisse ! On va jamais y arriver !" 

    show Mickey BrasCroises Sourire Yeuxfermes

    mic "Il va falloir faire de vot' mieux soldat.…"

    hide Mickey

    show Medoc PoseGauche Sourire Yeuxfermes at left
    show Mathilde PoseDroite Sourire Yeuxfermes at right

    med "Hinhinhin…"

    mat "Huhuhu…"


    hide Medoc
    hide Mathilde
    with longfade

    show Mickey BrasCroises Triste

    mic "Argh…"

    pov "Ooof..."

    mic "[povname]…."

    mic "ON S'EST FAIT LAMINER !"

    pov "Je vous avait dit que je savais pas mentir !"

    show Mickey PoseDroite Colere

    mic "Oui, enfin je ne pensais pas que tu allais me tendre un mouchoir quand je t'ai fait 3 clins d'œil quand même..."

    pov "Je pensais que vous aviez quelque chose dans l'œil..."

    hide Mickey

    show Mathilde BrasCroises Sourire Yeuxfermes

    mat "Bon… Assez chouiné… Passons au gage !"

    hide Mathilde
    show Medoc PoseGauche Sourire

    med "Oula… Je veux pas être là pour voir ça, bon courage, bye !"

    hide Medoc with dissolve

    pov "Quoi ? Quel gage ? Reviens Médoc !"

    show Mickey Standard Triste at left

    mic "Il est parti... Rien ne pourra nous sauver…."

    pov "Mais j'étais pas au courant moi ! C'est quoi ce club de l'entourloupe !"

    show Mathilde PoseSpeciale Sourire Yeuxfermes Rougit at right

    mat "Huhuhu… Comme tu n'étais pas au courant, je te donnerai un truc simple… Mais vous m'sieur Max, c'est tarif !"

    mat "J'veux vous voir a l'entraînement des cheerleaders la semaine prochaine ! Et en costume je vous prie !"

    show Mickey BrasCroises Triste

    mic "Aaargh pas eux..."

    pov "Mais pourquoi vous vous pliez à ça ? Vous êtes prof, vous pouvez vous rebiffer un peu !"

    show Mickey BrasCroises Badboy

    mic "Ça fait partie des règles, je joue en connaissance de cause…"

    pov "Mais… Pourquoi ?"

    show Mickey BrasCroises Sourire

    mic "Parce c'est réciproque… Si on gagne, on peut aussi faire la même chose. Lui demander ce qu'on veut. Et tu sais, toute l'école rêve de les voir, même moi ! Je pourrais prendre des photos et les partager à tous !"

    pov "M'sieur Max… C'est…"

    show Mickey BrasCroises Gene

    mic "Oui… Je sais.…"

    pov "C'EST DÉGOÛTANT, VOUS ÊTES UN PERVERS !" with hpunch

    show Mickey BrasCroises Colere Rougit

    mic "Hein ? Quoi ? Mais non ! Je parle des cartes des pickup lines ! Von Yaourt me paie grassement pour participer à ces jeux et les récupérer à son profit…"

    pov "Ah… J'ai eu peur… Mais vous avez tant besoin d'argent ?"

    show Mickey BrasCroises Sourire Yeuxfermes Rougit

    mic "Ahahah, tu sais je reste prof, et même à la Cosy Académie c'est pas la folie ! En plus j'ai beaucoup de frais, je refais ma terrasse à neuf en ce moment..."

    show Mathilde PoseSpeciale Rire Ojosama

    mat "Assez blablaté, oust M'sieur Max ! J'vous revois la semaine prochaine, et n'oubliez pas vos pompons ! Huhuhu…"

    show Mickey PoseGauche Sourire

    mic "Bon courage [povname] !"

    hide Mickey with dissolve

    show Mathilde Standard Badboy at center

    mat "Bien ! Pour commencer doucement alors... Je te propose même un choix de gage !"

    pov "Gloups…"

    mat "Alors…"

    mat "Tu préfères…"

    show Mathilde BrasCroises Sourire Yeuxfermes

    mat "Action ou Vérité ?"

    innerpov "Quoi c'est tout ?"

    pov "Et bien euh… Vérité ?"

    show Mathilde Standard Sourire

    mat "Je suppose que tu as eu le temps de te décider depuis ta rentrée du coup…"

    menu:
            
        mat "Medoc ou Moguri ?"

        "Medoc, définitivement...":
            python:
                pointsmedoc+=1
            show Mathilde BrasCroises Sourire Yeuxfermes
            mat "Je le savais !"

        "Moguri et son regard perçant me font beaucoup d'effet":
            python:
                pointsmoguri+=1
            show Mathilde BrasCroises Sourire Yeuxfermes    
            mat "Je le savais !"

        "Euh action ! Action !!":
            python:
                pointsincel+=1
            show Mathilde BrasCroises Sourire Yeuxfermes
            mat "Et bien je suppose que je te verrai en cheerleaders avec m'sieur Max alors !"

    pov "Argh…"

    show Mathilde Standard Sourire

    mat "Allez c'est pas grave, pense à autre chose !"

    show Mathilde PoseSpeciale Sourire Yeuxfermes Rougit

    mat "Comme rejoindre mon club par exemple !"

    pov "Dit-elle après m'avoir fait chanter ! Il faudrait vraiment que ce Von Yaourt me paie très cher pour me faire intégrer ce club…"

    show Mathilde PoseGauche Triste

    mat "Arf… Je m'en doutais bien ! Mais bon, si jamais tu veux te faire une petite partie juste comme ça, n'hésite pas à passer !  La porte sera toujours ouverte !"

    pov "J'hésiterai un peu quand même... Bonne soirée Mathilde !"

    show Mathilde PoseGauche Sourire
    mat "Et en parlant de Von... Tu peux toujours essayer son club de randonnée ! Ils partent demain matin !"
    if sex=="m":
        mat "Ils visitent des coins en bordure de la ville. C'est un peu dangereux à cause des cailloux, mais tu es un dur !"
    else:
        mat "Ils visitent des coins en bordure de la ville. C'est un peu dangereux à cause des cailloux, mais tu es une dure !"
    
    pov "Merci du conseil !"
    show Mathilde PoseDroite Sourire Yeuxfermes

    mat "Bonne soirée [povname] !"

    jump club_rando
    return
