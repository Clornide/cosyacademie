label fin_journee:
    scene street day with longfade
    show Metalice Standard Sourire Yeuxfermes

    met "Ah te voilà [povname] !"
    met "Tu rentres chez toi ? Dure journée hein !"
    met "T'inquiète pas, j'ai réglé ton inscription, tout est en ordre !"
    pov "Oh merci à toi !"
    met "J'ai cru comprendre que tu n'avais toujours pas trouvé de club ?"
    pov "Non... Ils sont un peu..."
    met "Haha ne dit rien, je sais !"
    met "Il faut que tu apprennes à te défendre..."
    show Metalice PoseDroite Sourire
    met "Mais oui !" with hpunch
    pov "!?"
    met "Le club de bagarre ! C'est un ami qui le dirige !"
    met "Je t'y emmène demain après les cours !"
    show Metalice PoseSpeciale Sourire Yeuxfermes
    met "Allez bonne nuit [povname] !"
    hide Metalice with dissolve
    innerpov "Quelle ninja..."

    jump unAutreLendemainMatin
    return
