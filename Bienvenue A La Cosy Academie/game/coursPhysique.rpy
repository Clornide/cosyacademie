label coursPhysique:
    play music wonderful
    scene classePhysique with fade
   
    show dieuvBrasCroisesBadBoy
    dieuv "Ouah le prof est pas là !"
    
    hide dieuvBrasCroisesBadBoy
    show metalicePoseCoucouTriste
    
    met "Quoi ??"

    hide metalicePoseCoucouTriste
    show metalicePoseCoucouCligneRougit

    met "J'aime tellement la physique..."

    hide metalicePoseCoucouCligneRougit
    show dieuvBrasCroisesBadBoy

    dieuv "Ben s'il est pas là, je m'en vais !"

    hide dieuvBrasCroisesBadBoy
    show medocPoseStandardBadBoy

    med "Normallement il faut attendre 15 min !"
    med "Et de toutes façons, c'est le prof qui a les clés, on est coincés ici..."    
    
    hide medocPoseStandardBadBoy
    show dieuvBrasCroisesBadBoy
    
    dieuv "Pfft ..."
    dieuv "Ben moi, je veux me tirer d'ici !"

    hide dieuvBrasCroisesBadBoy

    innerpov "Quel rebelle ce Dieuvomi !"

    show dieuvBrasCroisesBadBoy

    dieuv "Allez medoc, va demander si le prof est là !"

    hide dieuvBrasCroisesBadBoy

    stop music 
    play music haunted fadein 1.0

    show medocPoseStandardSourire
    med "Bon ok...."
    med "Alors..."

    hide medocPoseStandardSourire
    show medocPoseStandardSourireYeuxFermes

    med "Esprism... Es-tu là ?"
    inc "kr kr krr"
    play sound woosh

    hide medocPoseStandardSourireYeuxFermes
    show esprism at left

    with flash   
    esprism "Mais oui Je suis là !"
    esprism "Asseyez-vous !"

    stop music fadeout 1.0

    pause 3

    hide esprism at left

    jump coursPhysique
    return
