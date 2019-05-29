label Ichoosemedoc:
    play music tomorrow
    scene school hallway with longfade

    innerpov "Ça commence à faire un petit bout de temps que je l'attends, il ne devrait plus tarder..."
    innerpov "Je crois que je l'entends d'ailleurs, mais il a l'air de discuter avec quelqu'un."

    med "Bon, et t'y fais attention surtout. J'aurais l'air fin si quelqu'un d'autre que toi les lisait !"
    inc "Mais t'inquiète pas Medoc... Elles sont en sécurité avec moi !"
    med "Ouais, tu dis ça mais je les vois quand même dépasser de ta poche."

    innerpov "Il a l'air beaucoup plus sympathique que d'habitude... Je me demande avec qui il discute."
    innerpov "Ah ! Je les vois arriver !"


    show Medoc Standard Sourire Yeuxfermes at left with dissolve

    med "Je te fais confiance alors !"

    python:
        name_mathilde="???"

    show Mathilde PoseDroite Sourire at right with dissolve
    pause 1
    show Medoc Standard Colere Rougit

    med "[povname] ?! Mais qu'est-ce que tu fais là ? Tu es là depuis longtemps ? T'as rien entendu j'espère ?"
    pov "Q-quoi ? Non rien, je te promets !"

    show Mathilde PoseSpeciale Bad Girl

    if sex=="m":
        mat "Il ment Medoc... Il va falloir s'en débarrasser..."
    else:
        mat "Elle ment Medoc... Il va falloir s'en débarrasser..."
    
    show Medoc BrasCroises Triste    
    med "Tu... Tu crois ?"
    med "Je ne suis pas sûr d'en être capable tu sais..."
    if sex=="m":
        mat "C'est une nécessité... À moins qu'il n'avoue ses crimes... Je vais chercher ma barre à mine."
    else:
        mat "C'est une nécessité... À moins qu'elle n'avoue ses crimes... Je vais chercher ma barre à mine."

    med "Mathilde attends... N'en venons pas à ces extrêmes..."
    show Mathilde PoseDroite Badboy
    pov "Arrêtez ! J'avoue ! J'avoue tout !"
    pov "Tu parlais d'un truc que les gens ne devaient pas voir Medoc ! Quelque chose qui dépasse d'une poche !"
    pov "J'en sais pas plus, je le jure !"
    
    show Medoc Standard Colere Rougit
    python:
        name_mathilde = "Mathilde"
        mathilde_medoc = True
    if sex=="m":
        med "C'est bon Mathilde, il a tout avoué ! Pas besoin de ta barre à mine !"
    else:
        med "C'est bon Mathilde, elle a tout avoué ! Pas besoin de ta barre à mine !"
    show Medoc BrasCroises Gene
    show Mathilde PoseDroite Badboy at lightzoom with vpunch
    mat "..."
    show Mathilde PoseDroite Badboy at mediumzoom with vpunch
    mat "..."    
    show Mathilde PoseDroite Badboy at bigzoom with vpunch
    mat "..."
    show Mathilde PoseGauche Sourire Yeuxfermes
    mat "Huhuhuhuh !!"
    mat "Évidemment que je ne vais pas te faire de mal ! J'ai besoin de nouvelles recrues pour mon club moi !"
    show Medoc PoseGauche Gene
    med "Mathilde..."
    mat "Hmmm ?"
    med "Les cartes..."
    pov "NON ! ON VOIT RIEN MEDOC ! PROMIS ! AAAAAAAAAH !"
    show Mathilde PoseGauche Sourire Yeuxfermes Rougit 
    if sex=="m":
        mat "Tu vois il a rien vu, Medoc, alors tout va bien !"
    else:
        mat "Tu vois elle a rien vu, Medoc, alors tout va bien !"
    show Mathilde Standard Badboy
    mat "N'est-ce pas ?"
    pov "M-m-mais... Bien sûr ! Je n'sais même pas de quoi on parle ahahah !"
    show Mathilde Standard Sourire Yeuxfermes
    mat "Parfait ! Alors je m'attends à ce que tu passes à mon club hein ! Si tu veux pas de problèmes je veux dire..."
    pov "SANS FAUTE ! J'Y SERAI !"
    if sex=="m":
        mat "A plus Medoc, bye Machin !"
    else:
        mat "A plus Medoc, bye Machine !"
    hide Mathilde with dissolve
    pov "Euh moi c'est [povname] ! Aaaah... Elle est partie..."
    mat "NAN MAIS C'EST BON J'AI ENTENDU, T'INQUIETE !"
    pov "Ah euh... Super..."
    mat "HEIN ?!"
    pov "JE DISAIS SUPER !"
    inc "VOUS VOULEZ PAS ARRÊTER D'HURLER DANS LES COULOIRS ?!"
    pov "Ah oui pardon..."
    pov "Bon ben je suppose que je vais devoir passer au club jeux de société alors, c'est ça Medoc ?"
    show Medoc PoseDroite Sourire at center
    med "Effectivement... C'est dommage, je te voyais plus du genre physique ! À l'occasion tu devrais quand même aller voir les cheerleaders."
    pov "Ah bah alors là, avec plaisir ! Je dois m'adresser à qui ?"
    show Medoc PoseDroite Sourire Yeuxfermes
    med "Notre Chuenpodo national ! Tu verras, tu peux le repérer aussi facilement qu'un phare dans la nuit !"
    pov "Et bah super ! Erm... Tu fais quelque chose du coup maintenant ?"
    show Medoc BrasCroises Degoute
    med "Hm ? Bah je rentre chez moi, j'commence à avoir une p'tite dalle moi..."
    pov "Ah euh ça tombe bien... Moi aussi !"
    med "Et bah va te chercher à manger alors, je sais pas moi..."
    pov "Non je veux dire, moi aussi je rentre chez moi !"
    show Medoc BrasCroises Sourire
    med "Ah bah super, à demain alors !"
    pov "MAIS NAN MAIS MEDOC JE VEUX RENTRER AVEC TOI !!"
    show Medoc BrasCroises Gene
    med "Tu... Hein ?"
    show Medoc PoseDroite Gene
    med "Rentrer ?"
    show Medoc PoseGauche Gene
    med "Avec moi ?"
    pov "Si tu veux bien en tout cas !"
    show Medoc PoseGauche Sourire Rougit
    med "Bien sûr, c'est juste que j'ai plus l'habitude que les gens me prennent pour un gros dur, ça me fait plaisir comme proposition !"
    pov "Et bien je te suis alors !"
    med "Allons-y !"
    
    

    jump lendemainMatin 




    return
