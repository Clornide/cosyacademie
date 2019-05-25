label sad_no_club:
    play music memento
    scene street day with longfade
    
    innerpov "Et voilà, la semaine est finie et je n'ai toujours pas de club..."
    innerpov "Je vais sans doute devoir quitter la Cosy Académie..."

    menu:
        "Et sans avoir avoué mes sentiments à Moguri":
            python:
                pointsmoguri +=1
        "Medoc va tellement me manquer, je lui ai à peine parlé...":
            python:
                pointsmedoc +=1
        "Medoc et Moguri... Ces Chad et Stacy de mes rêves...":
            python:
                pointsincel +=1

    "Hé [povname] !"
    innerpov "???"
    
    show Medoc PoseGauche Sourire at left with dissolve
    if sex=="m":
        med "Ben où tu vas comme ça gars ?"
    else:
        med "Ben où tu vas comme ça meuf ?"
    show Moguri PoseDroite Sourire at right with dissolve
    mog "On va à notre club, tu veux venir ?"

    innerpov "Si je veux venir !?"
    pov "Je heu... "
    med "Allez, come on !"

    jump cosy_culture_club
    return
