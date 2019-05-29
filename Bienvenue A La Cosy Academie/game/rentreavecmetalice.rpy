label Rentreavecmetalice:
    play music tomorrow
    scene street day with longfade
    show Metalice Standard Sourire Yeuxfermes
    if sex=="m":
        met "Tu sais, je suis quand même surprise que tu ne sois pas rentré avec un de tes prétendants..."
    else:
        met "Tu sais, je suis quand même surprise que tu ne sois pas rentrée avec un de tes prétendants..."

    pov "Comment ça ?"

    show Metalice Standard Sourire Yeuxfermes

    met "Medoc ou Moguri enfin !"

    pov "Raaah mais laisse-moi avec eux enfin !"

    show Metalice Standard Sourire

    met "Tu dis ça mais je te vois très bien rougir hein !"
    pov "Tu parles quand même d'eux beaucoup plus que moi, c'est peut-être toi qui est intéressée finalement !"

    jump Rentreavecmetalice2
    return

label Rentreavecmetalice2:

    show Metalice PoseSpeciale Sourire Yeuxfermes

    met "Moi ? Mais je suis déjà prise enfin !"
    pov "Ah bon ? Tu sors avec quelqu'un qu'on a croisé ?"

    show Metalice PoseSpeciale Sourire

    met "Eh bien non. Il étudie à l'Académie cependant ! C'est juste qu'il ne passe qu'en ''coup de vent''. C'est quelqu'un de très occupé..."
    pov "Et on peut avoir le nom de cet heureux élu ?"

    show Metalice Standard Sourire

    met "Bien sûr ! Si tu as la chance de croiser un type qui s'appelle EchoBrain, et bien ce sera lui !"
    met "Bon assez parlé de moi ! Tu sais que tu dois obligatoirement rejoindre un club pour valider ton année ?"

    pov "Oui, c'était écrit dans la brochure de l'académie... Mais je ne sais pas trop quoi intégrer. Un conseil ?"

    show Metalice PoseSpeciale Sourire Yeuxfermes

    met "Personnellement je fais partie du conseil des élèves, donc je te dirais bien de me rejoindre..."
    met "Mais je pense que tu irais à merveille dans l'équipe de cheerleaders !"

    pov "Tu crois ? Merci pour le compliment !"

    show Metalice Standard Cligne

    met "C'est une façon de voir les choses... Enfin, je te conseille de passer les voir demain après-midi."

    show Metalice Standard Sourire

    met "Adresse-toi à Chuenpodo, c'est leur manager."
    pov "Il ressemble à quoi ?"
    met "Un grand blond à lunettes. Tu verras, il est resplendissant. Éblouissant même !"
    pov "Dis donc, je croyais que tu étais déjà prise !"
    met "Non mais... littéralement !  Il a une espèce d'aura lumineuse qui... enfin, tu comprendras quand tu le rencontreras je suppose !"
    pov "Je verrai, merci du conseil !"

    show Metalice Standard Sourire Yeuxfermes

    met "Il commence à faire froid tu ne trouves pas ? On devrait peut-être se dépêcher de rentrer..."
    pov "Effectivement, allons-y !"

    show Metalice Standard Sourire with longfade

    met "Me voilà arrivée, tu n'habites pas très loin n'est-ce pas ?"
    pov "Au bout de la rue, là-bas."

    show Metalice PoseSpeciale Sourire

    met "Bien, tu trouveras ton chemin alors !"

    show Metalice PoseSpeciale Sourire Yeuxfermes

    met "Je te dis à demain alors ! Et pense bien à aller voir les cheerleaders !"
    pov "Bien sûr ! À demain Metalice !"

    show Metalice PoseSpeciale Cligne

    met "Et fais de beaux rêves !"

    hide Metalice with dissolve

    pov "Comment ça de beaux rêves ?"
    pov "Elle a vraiment un don pour l'espièglerie celle-là..."



    pov "EchoBrain, alors..."
    pov "Il a bien de la chance..."

    show brise at truecenter with dissolve
#avec un bruit de vent, je sais pas trop encore comment faire, je verrai après

    inc "Oui... il en a beaucoup..."
    pov "?"
    pov "Quelqu'un a parlé ?"
    inc "..."

    pov "Brrr... Il fait froid d'un coup, je ferais mieux d'y aller !"

    jump lendemainMatin

    return
