
image ending alone = ConditionSwitch("sex == \"m\"", "ending/Photo-de-fin_Medoc-et-Moguri-etudiant.png", "True", "ending/Photo-de-fin_Medoc-et-Moguri-etudiante.png")
image ending moguri = ConditionSwitch("sex == \"m\"", "ending/Photo-de-fin_Moguri-etudiant.png", "True", "ending/Photo-de-fin_Moguri-etudiante.png")
image ending medoc = ConditionSwitch("sex == \"m\"", "ending/Photo-de-fin_Medoc-etudiant.png", "True", "ending/Photo-de-fin_Medoc-etudiante.png")


label verdict:
    play music wonderful
    
    scene black
    image name_ccc = Text("{size=80}Chapitre Final :\nLe Verdict", text_align=0.5)
    window hide
    show name_ccc:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(2)
    hide name_ccc with longfade
    window auto


    scene bar with longfade
   
    show Moguri PoseGauche Sourire Yeuxfermes at left with dissolve
    show Medoc PoseDroite Sourire Yeuxfermes at right with dissolve
    mog "Bon ben nickel alors Medoc, on se revoit dans deux semaines, et d'ici là tu fais quoi ?"
    med "Oh j'vais essayer de rester..."
    mog "Ouais ?"
    med "Bah allez, on a qu'à dire Cosy !"    
    mog "Et bah on part sur ça alors !"

    med "..."
    mog "..."

    mog "Et... Hop ! C'est coupé !"
    
    pov "C'était.... PHÉNOMENAL !"

    mog "Ahahah !"
    med "Arrête tu vas nous faire rougir !"

    pov "Non mais vraiment ! Vous avez vraiment une alchimie digne des plus grands !"

    med "Mais tu sais... si tu rejoins ce club, tu pourras faire partie de cette alchimie."
    pov "Vraiment ? Je peux ? Je veux dire, vous avez l'air si proches ! Et il n'y a que deux personnes dans ce club, je voudrais pas ruiner ça..."

    mog "Tu sais, si on te propose, c'est qu'on a senti qu'il y avait quelque chose de spécial..."

    innerpov "Tsss, si tu savais..."

    pov "Ok, donc c'est officiel, je fais parti du Cosy Culture Club ?"
    med "C'est officiel !"
    pov "J'y crois pas... La Cosy Academy... Le Cosy Culture Club..."

    if sex=="m":
        mog "Il va falloir commencer à réaliser mon grand !"
        innerpov "Ahaha... Je suis passé de 'gamin' à 'mon grand', ça fait plaisir..."
    else:
        mog "Il va falloir commencer à réaliser ma grande !"
        innerpov "Ahaha... Je suis passée de 'p'tite tête' à 'ma grande', ça fait plaisir..."
    med "Bon, alors on se dit à dans deux semaines ?"
    mog "À dans deux semaines !"

    hide Moguri
    hide Medoc
    with dissolve

    if pointsmedoc > pointsmoguri and pointsmedoc > pointsincel:
        
        innerpov "Non... pas maintenant... pas après tout ça...."
        pov "MEDOC ! ATTENDS !"
        
        show Medoc PoseDroite Sourire with dissolve

        med "Et bah [povname], faut se rentrer hein !"

        show Medoc PoseGauche Sourire 

        med "Nan parce que tu sais, il se fait tard et puis bon..."

        show Medoc PoseDroite Sourire Yeuxfermes

        med "Moi après je veux bien te raccompagner, pour pas que tu tombes sur un type chelou..."

        show Medoc PoseGauche Sourire Yeuxfermes

        med "Enfin, j'veux dire si tu veux parce que je veux pas te forcer à quoi que ce soit..."

        show Medoc PoseDroite Sourire Rougit

        innerpov "Attends qu'est-ce qu'il se passe là ?"
        
        show Medoc PoseGauche Sourire Rougit

        innerpov "Je voulais avouer mes sentiments à Medoc..."

        show Medoc PoseDroite Sourire Rougit

        innerpov "Et voilà qu'il a l'air plus excité que moi !"

        show Medoc PoseGauche Sourire Rougit

        innerpov "Allez, je me lance !"
        pov "Medoc !"

        show Medoc BrasCroises Sourire Rougit

        med "[povname] ! J'aimerais commencer si ça te dérange pas..."
        pov "Euh non bien sûr vas-y."
        if sex=="m":
            med "Ça me fait vraiment plaisir que tu sois venu t'inscrire au Cosy Culture Club."
        else:
            med "Ça me fait vraiment plaisir que tu sois venue t'inscrire au Cosy Culture Club." 
        
        med "Vraiment, ça me touche beaucoup ! Surtout avec le rough start qu'on a eu tous les deux."
        med "Et sache que je suis prêt à t'aider dans ta petite entreprise !"

        pov "Ma petite entreprise ?"

        show Medoc Standard Sourire Yeuxfermes Rougit

        med "Ahaha, si tu crois que je ne t'ai pas vu tourner autour de Moguri !"
        med "J'vais tout faire pour t'aider à concrétiser ton p'tit crush, t'inquiète pas !"

        pov "Quoi ? Mais non !"
        if sex=="m":
            med "Roh, hey, arrête ! Pas à moi ! Pour quelle autre raison tu serais rentré au Cosy Culture Club ?"
        else:
            med "Roh, hey, arrête ! Pas à moi ! Pour quelle autre raison tu serais rentrée au Cosy Culture Club ?"
        
        pov "Bah pour toi !"
        innerpov "Wow... C'était carrément plus facile à dire que je ne le pensais..."
        med "Hein ?"
        pov "Quoi ?"
        med "Ahahaha j'ai mal entendu !"
        med "Donc je disais..."
        pov "Non tu as bien entendu ! Je suis là pour toi Medoc !"
        med "Ah !"

        show Medoc BrasCroises Gene

        med "Aaaaaaaah..."
        pov "Ça ne va pas ?"

        med "Je... je dois y aller..."

        hide Medoc with dissolve

        pov "Medoc attends !!"
        pov "Non..."
        pov "J'aurais dû patienter un peu plus... prendre plus le temps de le connaître..."
        pov "Mais j'ai juste tout gâché... comme d'habitude..."

        show Medoc BrasCroises Sourire Rougit with dissolve

        med "Mais non, tu n'as rien gâché, ne t'inquiète pas..."
        med "J'ai juste été un peu surpris, c'est tout."
        med "Tu sais, c'est la première fois qu'on me fait une déclaration."
        
        show Medoc BrasCroises Sourire Yeuxfermes Rougit

        med "Les gens me croient froid, distant, inaccessible..."
        
        show Medoc PoseGauche Sourire Rougit

        med "Alors qu'en réalité, c'est juste un masque que je me suis créé, pour pallier mon manque d'assurance..."
        
        if sex=="m":        
            med "C'est pour ça que quand je t'ai vu arriver, je t'ai un peu brusqué. Je ne voulais pas que tu aies à subir les choses que j'ai vécues."
        else:
            med "C'est pour ça que quand je t'ai vu arriver, je t'ai un peu brusquée. Je ne voulais pas que tu aies à subir les choses que j'ai vécues."
        
        show Medoc PoseGauche Sourire Yeuxfermes Rougit
        med "Et tu as tellement évolué !"
        med "En à peine quelques jours, tu as rencontré les élèves les plus influents de l'Académie, et t'en es fait des amis !"
        med "Et surtout, tu m'as bien percé à jour ahaha..."

        med "Allez, sèche-moi ces larmes et viens près de moi..."

        pov "Merci... Pour tout..."

        show Medoc PoseGauche Sourire Rougit
        med "Merci à toi enfin !"

        innerpov "Dis donc, il est plus musclé qui n'en a l'air sous son uniforme. D'ailleurs il gratte un peu à vrai dire..."
        med "Il gratte cet uniforme n'est-ce pas ?"
        pov "Ah... euh oui, un peu !"

        med "J'ai peut-être une solution pour toi !"

        pov "Oui on m'a conseillé une marque d'adoucissant et..."

        show Medoc PoseGauche Sourire Yeuxfermes Rougit

        med "Plus radical !"

        hide Medoc with dissolve
        show Medoc PoseSpeciale Gene

        med "C'est un peu gênant finalement..."
        med "C'était beaucoup plus smooth dans ma tête..."
        pov "Ahahah, ce n'est pas grave, je vois autre chose de smooth, et ça me paraît bien plus intéressant !"
        show Medoc PoseSpeciale Sourire Yeuxfermes Rougit
        med "Et bah alors ! En voilà une prise d'assurance bien rapide ahaha ! Allez, viens là !"
        pov "Ouiiii !"

        with longfade

        show Medoc PoseSpeciale Sourire Rougit

        med "Cette fois, il commence à se faire vraiiiment tard... On devrait pas tarder à rentrer."
        pov "Ou alors, on pourrait passer la nuit ici !"

        show Medoc PoseSpeciale Sourire Yeuxfermes Rougit

        med "Ahahah ! Mais que diraient nos parents ? Faudrait pas les inquiéter non plus !"
        pov "Mmmmmm... Mais je voulais rester encore un peu..."

        show Medoc PoseSpeciale Sourire

        med "Ne t'inquiète pas, il nous reste du temps à passer ensemble, tu peux compter là dessus."
        pov "C'est une promesse ?"
        med "Un engagement, on ne peut plus solennel !"
        pov "Déjà ? Tu ne vas pas un peu vite en besogne ?"

        show Medoc PoseSpeciale Gene

        med "Quoi ? N-nan, c'est pas ce que je voulais dire..."
        pov "Ahahah ! Mais je plaisante enfin !"

        show Medoc PoseSpeciale Sourire Rougit

        med "Aaaaah... Je le savais ahahah..."
        med "Bon... Rentrons..."
        pov "Comme ça ?"
        med "AH OUI ! Passe-moi ma chemise s'il te plaît..."
        pov "Tu ne veux pas garder la mienne plutôt ?"

        show Medoc PoseSpeciale Gene
        med "Arrête !"
        pov "Ahahah ! Tu es si mignon quand tu es gêné... Tiens prends !"

        med "Merci..."
        hide Medoc with dissolve
        show Medoc PoseDroite Sourire Rougit

        med "Allez, je te raccompagne ?"
        pov "Avec plaisir !"

        scene school hallway choice with longfade

        show Medoc PoseDroite Sourire Yeuxfermes

        med "Et donc là, le mec me regarde et me dis 'Ah tiens ! V'là les mecs de la SDR !'"
        med "Mais moi j'sais pas c'est quoi la SDR ! Mais j'vais pas lui dire tu vois !"

        innerpov "Il a l'air tellement plus heureux quand il s'ouvre aux gens..."
        innerpov "J'ai bien fait de lui avouer mes sentiments ce soir !"
        innerpov "J'espère que l'on pourra se tirer l'un l'autre vers le haut !"
        innerpov "On a tous les deux le même problème de self-esteem finalement..."
        innerpov "Ahah ! Il commence déjà à déteindre sur moi avec ses anglicismes ! C'est bon signe !"

        med "Et là, le mec me dit, 'Alors, comment il va Karim ?'. Et là je me dis, nan, attends, y a un trap c'est..."

        show Medoc PoseGauche Degoute

        med "Dis... J'ai l'impression que tu m'écoutes plus du tout là."


        if sex=="m":
            pov "Désolé, j'étais distrait, tu es si beau quand tu es heureux !"
        else:
            pov "Désolée, j'étais distraite, tu es si beau quand tu es heureux !" 

        show Medoc PoseGauche Gene

        med "Q-quoi ?"

        pov "Ahahah ! Ça devient presque trop facile !"

        show Medoc PoseDroite Gene

        med "Hmpf... Allez, rentrons !"

        pov "J'vous suis !"

        innerpov "Ouaip... C'est vraiment une très bonne année qui commence, vivement la suite !"

        $ quick_menu = False
        window hide

        pause 0.5
        show ending medoc with longfade
        pause 10


    elif pointsmoguri > pointsmedoc and pointsmoguri > pointsincel:
        innerpov "Non... Pas maintenant... Pas après tout ça...."
        pov "MOGURI ! ATTENDS !"   
        show Moguri PoseDroite Sourire with dissolve

        mog "[povname] ? Tout va bien ?"
        innerpov "OK."
        innerpov "C'est une discussion comme les autres."
        innerpov "Aucun enjeu particulier."
        pov "Souffle."

        show Moguri Standard Sourire Yeuxfermes
        mog "Ahaha, tu as la même expression que lorsqu'on s'est rencontrés la première fois..."
        innerpov "Qu'il arrête de rire... qu'il m'écoute..."
        pov "MOGURI !"

        show Moguri BrasCroises Rougit

        mog "Q-quoi ? Ne me crie pas dessus, je suis juste en face de toi..."
        pov "Ne m'interromps plus !"

        show Moguri BrasCroises Gene

        mog "..."
        
        if sex=="m":
            pov "Depuis que je suis arrivé à l'Académie, on n'a pas eu beaucoup l'occasion de discuter..."
        else:
            pov "Depuis que je suis arrivée à l'Académie, on n'a pas eu beaucoup l'occasion de discuter..."

        pov "Mais les quelques fois où on a interagi, tu as toujours été la personne la plus compréhensive et douce avec moi..."
        pov "Et c'est pour ça que..."
        innerpov "Allez... Dis-le !"
        pov "Que..."

        show Moguri PoseDroite Sourire Rougit

        mog "Oui ?"

        innerpov "Aaaarghh, pas ce sourire !"
        pov "Eh-Dis-Donc-Il-Fait-Pas-Un-Peu-Chaud-Tu-Voudrais-Pas-Boire-Un-Coup ?"
    
        show Moguri BrasCroises Sourire

        mog "Oh ! Tu voulais juste demander l'autorisation d'utiliser les tireuses ! Bien sûr, allez, c'est ma tournée !"
        pov "Quoi ? N-..."
        innerpov "Remarque... Un peu d'alcool ne fera de mal à ma timidité..."
        pov "Pourquoi pas finalement !"
        mog "Allez hop ! À la tienne !"

        with longfade


        show Moguri PoseDroite Colere Rougit

        mog "Mais j'te dis ! Bordeaux ça s'est grave gentrifié !"
        pov "Moguri..."
        mog "Parce qu'à mon époque, les bars, c'était carrément pas ce standing là..."
        pov "Moguri."
        mog "Après, ça a un p'tit côté appréciable, mais moi j'aimais bien les bars un peu undergrounds. Mais ça, ça n'existe pl-"
        pov "MOGURIIIIIIIIIIIIIIIII !"
        mog "QUOI ?"
        pov "Moguri. J'te kiffe mon gars... Genre *hic* vraiment..."
        
        show Moguri PoseGauche Sourire Yeuxfermes Rougit
        
        mog "Ahahaha, moi aussi [povname], moi aussi..."
        pov "Nan mais... VRAIMENT ! J'ai envie de te serrer foooooooort dans mes bras comme ça !!"
        pov "Et c'est pas l'alcool qui m'fait parler hein !"
        show Moguri Standard Sourire Rougit
        mog "Ça je m'en doute, puisque tu n'en as pas bu..."
        pov "Boh si quand même ! TROIS VERRES !"
        mog "Tu crois vraiment que l'Académie mettrait à disposition de l'alcool à volonté pour ses élèves ?"
        mog "C'est du jus de pomme tout ça !"
        pov "Hein ? Mais ? Tu..."
        mog "Faisais semblant... pour te mettre en confiance..."
        pov "Mais ça n'a aucun sens !"
        show Moguri BrasCroises Sourire Yeuxfermes Rougit
        mog "Comme si c'était à moi qu'il fallait se plaindre..."
        show Moguri PoseDroite Sourire Rougit
        mog "Mais du coup, ça y est, nous nous sommes enfin avoué nos sentiments..."
        pov "Wow... c'était si simple finalement. Comme quoi, ça sert à rien de se prendre la tête parfois !"
        pov "Du coup, on fait quoi maintenant ?"
        mog "Tu as mentionné la température tout à l'heure, ça te dérange si je me mets à l'aise ?"
        pov "Non bien sûr, mais je ne vois pas en quoi ça répond à ma -"
        hide Moguri with dissolve
        show Moguri PoseSpeciale Sourire Rougit with dissolve
        pov "Wow."
        pov "Erm... Je crois avoir mentionné le fait de te serrer contre moi aussi ?"
        pov "Ça te dérange si JE me mets à l'aise ?"
        show Moguri PoseSpeciale Sourire Rougit Yeuxfermes
        mog "Ahahah, un peu plus d'assurance, ça me plaît !"

        with longfade


        show Moguri PoseSpeciale Sourire
        mog "Dis-moi... Il commence à se faire tard... Tu voudrais pas que je te ramène chez toi ?"
        pov "Si... tu as raison c'est plus raisonnable, on ne va pas dormir ici non plus !"
        show Moguri PoseSpeciale Sourire Yeuxfermes Rougit
        mog "Pas aujourd'hui en tout cas !"
        pov "MOGURI !"
        mog "Ahaha, je te taquine..."
        mog "Allez hop..."
        hide Moguri with dissolve
        show Moguri Standard Sourire with dissolve

        mog "Allons-y !"
    
        scene school hallway choice with longfade

        show Moguri PoseDroite Sourire Rougit

        mog "Dis [povname]..."
        pov "Oui ?"
        mog "Tu... as quelque chose de prévu pour les vacances qui arrivent ?"
        pov "Non pas vraiment pourquoi ?"
        mog "J'aurais aimé te montrer Bordeaux, ses bulots, ses églises..."
        pov "Ses églises ?"
        
        show Moguri Standard Sourire Yeuxfermes Rougit
        mog "Ouaip ! J'suis plutôt balaise en escalade !"
        pov "Je t'avoue ne pas voir le rapport direct..."
        mog "Je te déclarerai officiellement mon amour de là-haut !"
        pov "Quoi ? Mais tu vas te blesser !"

        show Moguri BrasCroises Sourire Rougit
        mog "Mais nan ! Je l'ai déjà fait !"
        pov "Et ça c'était bien passé ?"
        show Moguri BrasCroises Gene
        mog "..."
        show Moguri Standard Sourire Rougit
        mog "L'important, c'est que je l'aie déjà fait ! Tout ira bien cette fois !"
        mog "Allez, assez discuté rentrons !"
        pov "Moi tout ce que j'ai retenu, c'est que tu veux me déclarer ton amour de façon dangereusement grandiose..."
        show Moguri Standard Gene
        mog "RENTRONS !"
        hide Moguri with dissolve

        innerpov "Tout est allé si vite..."    
        if sex=="m":
            innerpov "Et j'en suis si heureux !"
        else:
            innerpov "Et j'en suis si heureuse !"
        innerpov "J'ai l'impression que plus rien ne peut m'arrêter !"
        mog "Dépêche-toi [povname] ! Il va falloir t'habituer à marcher plus vite si tu veux rester à mes côtés !"
        pov "J'arrive, j'arrive !"
        innerpov "Ouaip... C'est vraiment une très bonne année qui commence, vivement la suite !"
    
        $ quick_menu = False
        window hide

        pause 0.5
        show ending moguri with longfade
        pause 10
    
    
    
    else:
    
        pov "BON !"
        pov "Ben ça c'est fait !"
        pov "Ouaip..."
        if sex=="m":
            pov "Je m'sens un peu seul du coup..."
        else:
            pov "Je m'sens un peu seule du coup..."
        pov "Tiens, j'avais pas vu toutes ces tireuses là..."
        pov "Elles marchent ?"
        pov "OUAH ELLES MARCHENT !"
        if sex=="m":
            pov "Après c'est peut-être un peu pitoyable de boire tout seul..."
            pov "Déjà que je parle tout seul depuis 2-3 minutes..."
        else:
            pov "Après c'est peut-être un peu pitoyable de boire toute seule..."
            pov "Déjà que je parle toute seule depuis 2-3 minutes..."
            
        pov "Après, j'ai rencontré pas mal de gens depuis que je suis là !"
        pov "J'ai qu'à les inviter à boire un coup ici !"
        pov "Un p'tit Dieuvomi, un Foulk, peut-être un Von Yaourt..."
        pov "J'peux inviter tout le monde en fait, je suis un membre à part entière du Cosy Culture Club !"
        pov "Boire des coups fait partie du concept en plus !"
        pov "Bon j'vais les chercher alors !"

        with longfade

        show Von PoseDroite Sourire Yeuxfermes at right
        show Foulk PoseGauche Sourire Yeuxfermes at left 
        with dissolve

        pause 1

        hide Von
        hide Foulk
        with dissolve

        show Pansepignon PoseDroite Sourire Yeuxfermes Rougit at right
        show Chuenpodo PoseGauche Sourire Yeuxfermes Rougit at left

        with dissolve

        pause 1

        hide Chuenpodo
        hide Pansepignon
        
        with dissolve

        show Mathilde PoseSpeciale Rire Ojosama at right
        show Caro PoseGauche Sourire Yeuxfermes at left

        pause 1

        hide Mathilde
        hide Caro

        with dissolve

        show Lock PoseDroite Sourire Yeuxfermes at right
        show Dieuvomi PoseGauche Sourire Yeuxfermes at left        
        with dissolve
        pause 1

        hide Lock
        hide Dieuvomi
        with dissolve

        show din PoseDroite Sourire Yeuxfermes at right
        show ZePilot PoseGauche Sourire Yeuxfermes at left        
        with dissolve
        pause 1

        hide din
        hide ZePilot
        with dissolve

        show Metalice BrasCroises Sourire Yeuxfermes with dissolve

        if sex=="m":
            met "Dis-donc, tu m'as l'air bien seul pour quelqu'un qui a rassemblé autant de gens..."
        else:
            met "Dis-donc, tu m'as l'air bien seule pour quelqu'un qui a rassemblé autant de gens..."
        show Metalice PoseSpeciale Cligne
        met "Peut-être que les personnes les plus importantes ne sont pas présentes..."
        pov "Erf... Tu avais raison finalement, je n'aurais pas dû rester focus seulement sur Medoc et Moguri..."
        pov "J'ai perdu mon temps..."
        pov "Ils ne sont pas intéressés..."
        pov "Et maintenant..."
        pov "J'ai plus personne."
        
        show Metalice BrasCroises Sourire

        met "Allons allons... Sèche-moi ces grosses larmes, et regarde un peu autour de toi !"
        met "Comment tu peux dire que tu n'as plus personne, tous ces gens sont venus parce que tu les as invités, tu comptes pour eux !"
        met "Et tu comptes même pour Medoc et Moguri. Tu sais, tu es quand même la seule personne à intégrer le Cosy Culture Club depuis sa fondation."
        pov "Tu crois ?"


        show Metalice Standard Sourire Yeuxfermes

        met "J'en suis sûre !"
        met "Et puis si tu tiens tant que ça à vivre ton histoire d'amour estudiantine, regarde toutes les belles personnes qui sont venues rien que pour toi !"

        show Metalice PoseSpeciale Cligne
        met "Même si personnellement, je ne suis pas disponible..."
        pov "Tu as raison... Peut-être que le Cosy, finalement, c'est juste les amis que l'on s'est faits sur le chemin !"

        show Metalice BrasCroises Degoute
        met "..."
        pov "Quoi ?"

        show Metalice BrasCroises Sourire
        met "Je pensais que tu en viendrais à une conclusion un peu moins cliché, mais qui suis-je pour juger."
        pov "Pas Moguri, dans un premier temps..."
        show Metalice Standard Sourire Yeuxfermes
        met "Ahahahah !"

        show Metalice Standard Sourire 
        met "Je vois que le moral t'est déjà un peu revenu."
        pov "Bah ! Je me dis que c'est le début d'une scolarité pleine de bons moments !"
        pov "Avec des personnages comme vous en même temps..."

        show Metalice PoseSpeciale Sourire Yeuxfermes Rougit

        met "Allez, viens donc boire un peu ! Ça t'apprendra à raconter n'importe quoi !"
        pov "Comme d'habitude, je te suis !"

        hide Metalice with longfade

        pov "Fiouf... Tout le monde est parti, j'ai tout rangé... Nickel !"
        pov "Eh... Elle commence pas si mal cette année finalement, vivement la suite !"

        $ quick_menu = False
        window hide
    
        
        pause 0.5
        show ending alone with longfade
        pause 10


        #ET LA, LA PHOTO MIGNONNE AVEC TOUT LE MONDE 


    scene black with longfade
    jump credits
    return
