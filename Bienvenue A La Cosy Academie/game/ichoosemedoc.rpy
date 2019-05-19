label Ichoosemedoc:
    scene school hallway with longfade

    innerpov "Ca commence à faire un petit bout de temps que je l'attends, il ne devrait plus tarder..."
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

    show Mathilde BrasCroises Sourire at right with dissolve
    pause 1
    show Medoc Standard Colere Rougit

    med "[povname] ?! Mais qu'est-ce que tu fais là ? Tu es là depuis longtemps ? T'as rien entendu j'espère ?"
    pov "Q-quoi ? Non rien, je te promets !"

    show Mathilde PoseSpeciale Bad Girl

    if sex=="m":
        mat "Il ment Medoc... Il va falloir s'en débarasser..."
    else:
        mat "Elle ment Medoc... Il va falloir s'en débarasser..."

    med "Tu... Tu crois ?"
    med "Je ne suis pas sur d'en être capable tu sais..."
    if sex=="m":
        mat "C'est une nécessité... A moins qu'il n'avoue ses crimes... Je vais chercher ma barre à mine."
    else:
        mat "C'est une nécessité... A moins qu'elle n'avoue ses crimes... Je vais chercher ma barre à mine."

    med "Mathilde attends... N'en venons pas à ces extrêmes..."
    pov "Arrêtez ! J'avoue ! J'avoue tout !"
    pov "Tu parlais d'un truc que les gens ne devaient pas voir Medoc ! Quelque chose qui dépasse d'une poche !"
    pov "J'en sais pas plus, je le jure !"


    jump Rentreavecmetalice




    return
