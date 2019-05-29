label cosy_culture_club:
    play music sundaysmooth

    scene black
    image name_ccc = Text("{size=80}Chapitre 9 :\nLe Cosy Culture Club", text_align=0.5)
    window hide
    show name_ccc:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(2)
    hide name_ccc
    window auto


    scene bar with fade
   
    show Moguri PoseGauche Sourire Yeuxfermes at left
    show Medoc PoseDroite Sourire Yeuxfermes at right
    mog "Nous y voici enfin [povname] !"
    med "On t'attendait..."
    innerpov "Medoc et Moguri... M'attendre ? Moi ??"
    innerpov "Est-ce vraiment le vrai Medoc ??"
    
    pov "Heuuu..."
    show Moguri PoseGauche Sourire
    show Medoc PoseDroite Sourire
    mog "On sait que tu avais peur de venir, c'est pour ça qu'on t'a laissé essayer les autres clubs."
    med "Bah oui, ils sont gentils mais bon..."
    mog "C'est pas les couteaux les plus affutés du tiroir..."
    pov "C'est un peu méchant non ?"
    
    show Moguri PoseGauche Gene
    mog "Ha mais je juge pas !"
    show Medoc BrasCroises Sourire
    med "Mais si gars tu juges trop !"
    show Medoc PoseDroite Badboy
    show Moguri BrasCroises Gene
    mog "Non mais regarde les pansepignoles là..."
    show Medoc PoseDroite Gene
    med "Ouais bon okay, leur keikaku il est pas tight..."
    med "Pourtant j'essaie de les aider, la dernière fois je leur ai dit que même s'ils étaient pas dans l'ordre c'était bon !"
    show Moguri PoseGauche Sourire
    mog "Et ?"
    show Medoc BrasCroises Sourire
    med "Ben ils ont oublié des lettres !!"

    show Moguri PoseGauche Triste
    mog "Et Lock et son couteau, dangereux !! Regarde ce qui est arrivé à Chop !"
    show Medoc PoseDroite Gene
    med "Ouais bon pour Chop c'est pas entièrement sa faute..."
    show Medoc PoseDroite Sourire
    med "Mais il devrait trouver une activité plus calme. S'entraîner avec Choukrane par exemple ! Il est zen et inspirant !"
    
    show Moguri PoseGauche Sourire
    mog "Paraît qu'il trouve l'alchimie mignonne. Il y a les réponses à tout dedans. N'importe quoi."
    
    show Medoc PoseDroite Colere
    med "Mais tu juges encore !!"
    innerpov "J'ose pas les interrompre, ils sont si..."
    
    
    show Moguri BrasCroises Badboy
    mog "Bah ouais mais en même temps on t'a écouté pour le club tech..."
    show Moguri PoseGauche Badboy
    show Medoc BrasCroises Badboy
    med "Hé gars ! C'est toi qui l'a incité avec ton mod chépa quoi là !"
    mog "J'ai rien demandé, j'ai juste dit que j'aimais les portes ! Regarde ce qui se passe comme bordel dans l'académie maintenant !" 
    show Medoc PoseDroite Badboy
    med "Le club tech, c'était pour lui faire plaisir. Puis il est seul dedans..."
    mog "Il est seul et j'aime pas ça. La dernière fois que j'ai utilisé mon portable, il m'a demandé de plus l'utiliser aux toilettes, il trouvait ça dégueulasse !"
    med "Ouais c'est vrai que ... J'pense qu'il m'a hackou avec ses trucs..."
    mog "T'imagines, il a sûrement des photos privates !"
    innerpov "Intéressant..."
    show Moguri PoseGauche Sourire
    mog "Et quitte à faire plaisir à quelqu'un, tu devrais retourner au club de comédie, tu as vu ce qu'ils font ? Ça rime à rien et c'est gênant !"
    show Medoc PoseDroite Triste
    med "Ouais c'est un peu triste, mais tu sais avec les histoires je peux pas..."
    mog "C'est du passé ! Et puis Mr Tshirt est heureux au SNL..."
    show Medoc PoseDroite Gene
    med "Je parle pas de ça... Mais je veux pas en parler devant des gens."

    menu:

        innerpov "Oups..."

        "Je suis sûr que Dieuvomi tient encore à toi, ça se voit...":
            
            show Medoc BrasCroises Gene
            med "Je tiens à lui aussi, quelque part..."
            show Medoc PoseDroite Sourire Yeuxfermes Rougit
            med "Je devrais peut-être lui faire un p'tit plat pour me faire pardonner..."
            python:
                pointsmoguri+=1
                

        "Dieuvomi m'a tout raconté...":
            show Moguri BrasCroises Colere
            show Medoc BrasCroises Colere
            mog "Hé ! Poucaves obtiennent marrave !" with hpunch
            if sex=="m":
                med "C'est tellement sale ce que tu fais gars !" with vpunch
            else:
                med "C'est tellement sale ce que tu fais meuf !" with vpunch
            
            python:
                pointsincel+=1
            

        "Heuuuu oui ça ne me regarde pas !":
            show Medoc PoseDroite Sourire Yeuxfermes Rougit
            med "De toutes façons on doit tous passer à autre chose."
            python:
                pointsmedoc+=1
            

    show Moguri PoseGauche Sourire
    show Medoc PoseDroite Sourire
    med "Bon, [povname], faut quand même qu'on t'explique ce qu'on fait ici."
    mog "On fait les choses super importantes et cruciales !"
    pov "Vraiment ?"

    mog "On se réunit tous les 15 jours, et on discute de ce qu'on aime."
    
    show Moguri PoseGauche Colere
    mog "Sauf tous les 150 jours, où on dit ce qu'on aime pas."
    pov "Pourquoi ça ?"
    show Moguri PoseGauche Sourire
    show Medoc PoseDroite Gene
    med "C'est la tradition gars !"
    show Moguri PoseGauche Gene
    mog "Faut lâcher la pression !"
    show Medoc PoseDroite Sourire
    innerpov "À propos de lâcher la pression, il fait chaud ici..."
    pov "À propos de lâcher la pression, il fait chaud ici..."
    show Medoc BrasCroises Degoute
    show Moguri BrasCroises Degoute
    med "Hein ?"

    innerpov "J'ai dit ça tout haut !?"
    show Moguri PoseGauche Degoute
    show Medoc PoseDroite Degoute
    pov "Je dis qu'il fait chaud ici, avec ce feu ouvert et tout ça..."
    show Medoc BrasCroises Sourire Yeuxfermes
    show Moguri PoseGauche Sourire Yeuxfermes
    med "Ah, oui, et encore, on a pas ouvert les bouteilles !"

    show Moguri PoseGauche Badboy
    show Medoc PoseDroite Sourire
    mog "Il y a un souci par contre..."
    show Moguri PoseGauche Sourire Rougit
    mog "On aime bien faire ça qu'à deux..."

    innerpov "Houlàlà !"
    show Medoc PoseDroite Degoute
    med "Même si bon, j'ai l'impression qu'il y a des gars qui écoutent à la porte !"
    show Moguri PoseGauche Degoute
    mog "Non mais c'est sûr, on arrête pas de me parler de recettes de bulot ces derniers temps..."

    pov "Je vais vous laisser alors..."

    show Medoc PoseDroite Sourire
    show Moguri PoseGauche Sourire
    med "Mais non ! Attends on va trouver un truc !"
    mog "Ouais nous on veut que tu sois confortable à l'académie !"

    innerpov "Ouuuuuuh..."

    pov "C'est très gentil..."

    mog "Qu'est-ce que tu dirais qu'on t'invite et c'est toi qui nous racontes des trucs !"
    mog "Mais n'importe quoi hein, le principal c'est que tu sois à l'aise !"
    
    show Medoc BrasCroises Sourire Yeuxfermes Rougit
    med "Blaise !"
    show Moguri PoseGauche Degoute
    mog "Hein ?"
    show Medoc PoseDroite Badboy
    med "J'ai senti que je tenais un truc mais je l'ai plus."
    show Moguri PoseGauche Sourire
    mog "Par contre, on enregistre ça, parce qu'on doit rendre des comptes au secrétariat."
    show Medoc PoseDroite Sourire
    med "Ouais, on a dit qu'on faisait un club, mais ils pensent que c'est juste une excuse pour se voir et boire des coups !"
    show Medoc BrasCroises Degoute
    med "Comme si on avait besoin d'une excuse pour faire la fête..."
    show Medoc PoseDroite Sourire
    mog "Ouais enfin bon soit, on doit rendre des comptes, donc on doit enregistrer !"

    innerpov "Faire une \"tape\" avec Medoc et Moguri.. Ouah !"

    pov "Heu ça ne devrait pas être un souci..."

    mog "Parfait ! Parce que mine de rien on a 6 mois de retard sur les rapports..."

    innerpov "J'ai attendu toute ma vie pour ce rapport !"
    
    pov "Je vais vous aider ! C'est le plus beau jour de ma vie !"
  
    if sex=="m":
        med "Hé hé calme-toi gars, c'est la cosy académie ici, c'est normal !"
    else:
        med "Hé hé calme-toi meuf, c'est la cosy académie ici, c'est normal !"
    
    mog "Allez, assieds-toi confortablement, tu vas nous regarder jouer à un jeu aujourd'hui..."
    med "En buvant des verres bien sûr... Quel serait le jeu idéal pour ça ?"
    menu:
        med "{cps=0}En buvant des verres bien sûr... Quel serait le jeu idéal pour ça ?{/cps}"
        "Cul à cul sec !":
            med "Haha t'es un chef [povname] !"
        "Le gin te nique !":
            med "Mais oui pourquoi pas ! T'es un chef !"
        "Biere hockey !":
            med "Haha ! T'es le chef !"

    window hide
    pause 3

    scene black with longfade
    jump verdict
    return
