# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"
image intro = "BienvenueAlaCosyAcademie_intro.png"



#image moguri

image moguri standard = ConditionSwitch("persistent.ultra_quality", "Moguri_PoseStandard_01-BadBoy.png", "True", "Moguri_low.png")
image moguri croise rigole = ConditionSwitch("persistent.ultra_quality", "Moguri_BrasCroises_08-SourireYeuxFermes.png", "True", "Moguri_low.png")
image moguri rigole ouvert = ConditionSwitch("persistent.ultra_quality", "Moguri_PoseStandard_06-Sourire.png", "True", "Moguri_low.png")
image moguri rigole ferme = ConditionSwitch("persistent.ultra_quality", "Moguri_PoseStandard_08-SourireYeuxFermes.png", "True", "Moguri_low.png")
image moguri deg croise = ConditionSwitch("persistent.ultra_quality", "Moguri_BrasCroises_05-Degoute.png", "True", "Moguri_low.png")


#image medoc
image medoc standard = ConditionSwitch("persistent.ultra_quality", "Medoc_PoseStandard_01-BadBoy.png", "True", "Medoc_low.png")
image medoc deg =  ConditionSwitch("persistent.ultra_quality", "Medoc_PoseStandard_05-Degoute.png", "True", "Medoc_low.png")
image medoc deg zoom = ConditionSwitch("persistent.ultra_quality", "Medoc_PoseStandard_05.1-Degoute-Zoom.png", "True", "Medoc_low.png")
image medoc happy = ConditionSwitch("persistent.ultra_quality", "Medoc_PoseStandard_08-SourireYeuxFermes.png", "True", "Medoc_low.png")
image medoc colere poing = ConditionSwitch("persistent.ultra_quality", "Medoc_PosePoings_03-Colere.png", "True", "Medoc_low.png")

#image metalice

image metalice coucou fermes = ConditionSwitch("persistent.ultra_quality", "Metalice_PoseCoucou_08-SourireYeuxFermes.png", "True", "Metalice_low.png")
image metalice coucou clindoeil = ConditionSwitch("persistent.ultra_quality", "Metalice_PoseCoucou_01-Cligne.png", "True", "Metalice_low.png")
image metalice coucou = ConditionSwitch("persistent.ultra_quality", "Metalice_PoseCoucou_06-Sourire.png", "True", "Metalice_low.png")
image metalice decue = ConditionSwitch("persistent.ultra_quality", "Metalice_PoseCoucou_10-Triste.png", "True", "Metalice_low.png")
image metalice colere rouge = ConditionSwitch("persistent.ultra_quality", "Metalice_PoseCoucou_04-ColereRougit.png", "True", "Metalice_low.png")
image metalice deg = ConditionSwitch("persistent.ultra_quality", "Metalice_PoseCoucou_05-Degoute.png", "True", "Metalice_low.png")

#image mickey

image mickey normal= ConditionSwitch("persistent.ultra_quality", "Mickey_PoseStandard_01-BadBoy.png", "True", "Mickey_low.png")
image mickey chonti= ConditionSwitch("persistent.ultra_quality", "Mickey_PoseStandard_06-Sourire.png", "True", "Mickey_low.png")
image mickey colere= ConditionSwitch("persistent.ultra_quality", "Mickey_PoseStandard_03-Colere.png", "True", "Mickey_low.png")
image mickey happy= ConditionSwitch("persistent.ultra_quality", "Mickey_PoseStandard_08-SourireYeuxFermes.png", "True", "Mickey_low.png")
image mickey deg = ConditionSwitch("persistent.ultra_quality", "Mickey_PoseStandard_05-Degoute.png", "True", "Mickey_low.png")


#image dieuvomi

image dieuv deg = "Dieuvomi_BrasCroises_05-Degoute.png"
image dieuv col = "Dieuvomi_BrasCroises_03-Colere.png"
image dieuv smug = "Dieuvomi_BrasCroises_08-SourireYeuxFermes.png"

# Déclarez les personnages utilisés dans le jeu.

define pov = Character("[povname]", color="#fff")
define innerpov = Character("[povname]", color="#fff")
define med = Character('Medoc', color="#fff")
define mog = Character('Moguri', color="#fff")
define met = Character('Metalice', color="#fff")
define mic = Character('Mickey', color="#fff")
define dieuv = Character('Dieuvomi', color="#fff")

define inc = Character('???', color="#fff")
define tlm = Character('Tout le monde', color="#fff")

#Effets nouveaux
define longfade = Fade(0.8, 0.2, 0.8, color="#000")
define shortflash = Fade(.1, 0, .1, color="#fff")
define flash = Fade(.25, 0, .75, color="#fff")
define animintro = Fade(0.8, 0.2, 0.8, color="#fff")

#Musique
define audio.memento = "music/Memento.mp3"

# Le jeu commence ici
label start:



    python:
        #Points routes
        pointsmedoc=0
        pointsmoguri=0
        pointsincel=0

        povname = renpy.input("Avant de commencer, veuillez renseigner votre prénom ? Par défaut vous serez appelé Hector")
        povname = povname.strip()

        while povname=="moguri" or povname=="Moguri" or povname=="medoc" or povname=="Medoc" :
            povname = renpy.input("Pas Medoc ou Moguri svp")
            povname = povname.strip()
        if not povname:
            povname="Hector"


    menu:

        "Et du coup, masculin ou féminin ?"

        "Homme.":
            python:
                sex = "m"

        "Femme.":
            python:
                sex = "f"

    play music memento
    scene school entrance

    with fade
    pov "OK."
    pov "C'est une journée comme les autres."
    pov "Aucun enjeu particulier."
    pov "Souffle."
    pov "Certes, c'est une académie d'élite, et je ne croiserai que les plus grands de ce pays."
    pov "Mais si je suis là, c'est que je l'ai mérité, non ?"
    pov "Personne ne me jugera, ils sont tous passés par là."
    pov "C'est une journée comme les autres."
    pov "..."
    pov "Je sais que c'est un mensonge."
    pov "C'est ma première journée à la Cosy Académie, un tournant dans ma vie."
    pov "Si je me plante je peux tout foutre en l'air..."
    pov "..."
    pov "Aaaaargh mais qu'est ce que je fais ic- !!"


    show moguri standard
    with flash

    "BOOONG!!!!!"

    pov "Hey !! Mais ça va pas de foncer dans les gens comme ç- !?"

    pov "Oh non...."
    pov "C'est Moguri..."
    pov "Mais s'il est ici, ça veut dire que..."

    hide moguri standard
    show medoc standard
    with flash

    "BOOONG!!!!!"


    show moguri standard at right
    show medoc standard at left

    pov "C'est pas vrai..."
    pov "Medoc et Moguri. Dès mon premier jour, je tombe sur eux."
    pov "Littéralement en plus."
    pov "Moi qui voulais faire une rentrée à peu près discrète, c'est rapé."

    show medoc deg at left

    med "Dis donc, tu comptes nous fixer longtemps, comme ça ?"
    pov "Je... Non, bien sûr, excusez-moi, c'est juste que..."

    show moguri croise rigole at right

    if sex=="m":
        mog "Ahahah mais enfin Medoc, laisse-le ! Regarde comme il a l'air stressé !"
    else:
        mog "Ahahah mais enfin Medoc, laisse-la ! Regarde comme elle a l'air stressée !"

    show moguri rigole ouvert at right



    if sex=="f":
        mog "Bienvenue à la Cosy Académie, gamine. Ne t'inquiète pas, on n'est pas tous aussi bourru que lui !"
        "Je suis presque sûre qu'on a le même âge, mais le fait qu'il m'appelle gamine ne me déplait pas particulièrement."
        pov "Aaaah, merci... Je tâcherai de me faire plus discrete, désolée !"
        mog "Mais non enfin ! Si tu es ici, c'est que tu as ta place. Aucune raison de se faire discrète !"
    else:
        mog "Bienvenue à la Cosy Académie, gamin. Ne t'inquiète pas, on n'est pas tous aussi bourru que lui !"
        "Je suis presque sûr qu'on a le même âge, mais le fait qu'il m'appelle gamin ne me déplait pas particulièrement."
        pov "Aaaah, merci... Je tâcherai de me faire plus discret, désolé !"
        mog "Mais non enfin ! Si tu es ici, c'est que tu as ta place. Aucune raison de se faire discret !"



    show moguri rigole ferme at right

    mog "Sur ce... On va y aller, il s'agirait pas d'arriver en retard ! A plus tard p'tite tête !"

    hide moguri rigole ferme
    pause 0.5
    hide medoc deg
    show medoc deg with fade

    med "Tch."
    med "Moguri a raison. Tout le monde n'est pas aussi bourru que moi..."
    med "Mais attention."
    show medoc deg zoom

    med "Tout le monde n'est pas aussi indulgent que lui..."

    pov "Gloups."

    pov "Ouch... Près... Très près. Trop près ?"
    pov "Pas vraiment."

    show medoc deg

    med "Allez. Fais attention à toi."

    hide medoc deg with fade

    pov "Ouf."
    pov "Ca commence fort."
    pov "Même de dos ils sont impressionants..."
    pov "Aller, ça va le faire ! On y va !"

    window hide

    show intro at truecenter
    with animintro

    pause 3

    jump Meeting_Metalice

    return

label Meeting_Metalice:
    scene couloir with fade

    window show

    "Bon. Classe 103, classe 103..."
    "Ah voilà !"
    "Bon ben on y va alors !"

    if sex=="m":
        inc "Hep toi, le nouveau là-bas !"
    else:
        inc "Hep toi, la nouvelle là-bas !"

    show metalice coucou fermes with fade

    met "Ah, salut ! C'est bien [povname] c'est ça ? Moi c'est Metalice !"

    show metalice coucou

    met "J'ai été désignée pour être ta marraine à ton arrivée, donc si tu as la moindre question, n'hésite pas !"

    if sex=="m":
        pov "Enchanté Metalice ! Je m'en remets à toi alors. "
    else:
        pov "Enchantée Metalice ! Je m'en remets à toi alors."

    met "Alors, tu as pu faire connaissance avec quelques personnes ? J'ai vu que tu discutais avec Medoc et Moguri à l'entrée."
    met "Tu ferais bien de te méfier de ces deux gaillards. Ils pensent que rien ni personne ne leur résiste."

    show metalice coucou fermes

    met "Et au vu de ta réaction, ils ont déjà fait forte impression sur toi apparemment, ahaha !"

    show metalice coucou

    if sex=="m":
        pov "Q-quoi ? Non pas du tout, ils m'ont juste surpris tout à l'heure, rien de plus !"
    else:
        pov "Q-quoi ? Non pas du tout, ils m'ont juste surprise tout à l'heure, rien de plus !"

    show metalice coucou clindoeil

    met "Oh arrête, pas à moi hein ! Je suis là pour te donner TOUTES sortes de conseils."
    innerpov "Très subtil ce clin d'oeil..."

    show metalice coucou

    met "Alors, t'as flashé sur lequel ?"

    menu:

        met "Alors, t'as flashé sur lequel ?"

        "Medoc et son air bre-som...":
            python:
                pointsmedoc+=1

        "Moguri, il a l'air si doux et gentil...":
            python:
                pointsmoguri+=1

        "Mais personne je te dis !!":
            python:
                pointsincel+=1

    if pointsmedoc!=0:
        show metalice coucou fermes

        met "Ah ! C'est vrai qu'il impressionne beaucoup de gens, mais il ne faut pas se laisser avoir, il se fait plus dur qu'il ne l'est vraiment !"
        pov "Ah bon ?"

        show metalice coucou

        met "Il réagit surtout comme ça avec les gens qu'il apprécie. Il est plus protecteur qu'autre chose finalement !"
        show metalice coucou clindoeil
        met "Tu ne l'as pas entendu de moi, hein !"
        show metalice coucou
        pov "Et... Tu penses qu'il y aura moyen ?"
        if sex=="m":
            met "Et bien ! Je te trouve bien ambitieux pour tes premières heures à la Cosy Académie."
        else:
            met "Et bien ! Je te trouve bien ambitieuse pour tes premières heures à la Cosy Académie."
        pov "Non ! Ce n'est pas ce que je voulais dire. Enfin..."

        show metalice coucou clindoeil

        met "Ne t'en fais pas, je vois très bien ce que tu veux dire !"
        innerpov "Encore ce clin d'oeil..."

        show metalice coucou

        if sex=="m":
            met "Enfin bon ce ne sont pas les seuls étudiants de ce lycée, aucune raison de rester bloqué sur ces deux là !"
        else:
            met "Enfin bon ce ne sont pas les seuls étudiants de ce lycée, aucune raison de rester bloquée sur ces deux là !"

    elif pointsmoguri!=0:
        show metalice coucou fermes

        met "Moguri ? Doux et gentil ? Il est plus du genre à juger les gens d'habitude. Tu as du lui taper dans l'oeil !"
        show metalice coucou
        pov "Quoi ? V-vraiment ?"
        show metalice coucou clindoeil
        met "Ahaha, oui vraiment ! Tu apprendras que je suis l'une des sources d'informations les plus fiables de l'école, tu peux me faire confiance !"
        show metalice coucou
        pov "D'accord, merci ! Du coup, tu penses que... Enfin qu'il y a moyen quoi ?"
        if sex=="m":
            met "Et bien ! Je te trouve bien ambitieux pour tes premières heures à la Cosy Académie."
        else:
            met "Et bien ! Je te trouve bien ambitieuse pour tes premières heures à la Cosy Académie."
        pov "Non ! Ce n'est pas ce que je voulais dire. Enfin..."
        show metalice coucou clindoeil
        met "Ne t'en fais pas, je vois très bien ce que tu veux dire !"
        innerpov "Encore ce clin d'oeil..."
        show metalice clindoeil
        if sex=="m":
            met "Enfin bon ce ne sont pas les seuls étudiants de ce lycée, aucune raison de rester bloqué sur ces deux là !"
        else:
            met "Enfin bon ce ne sont pas les seuls étudiants de ce lycée, aucune raison de rester bloquée sur ces deux là !"

    elif pointsincel!=0:

        show metalice decue

        met "Mouais ! Si tu le dis..."

        show metalice coucou

        if sex=="m":
            met "Enfin bon tu as raison, ce ne sont pas les seuls étudiants de ce lycée. Aucune raison de rester bloqué sur ces deux là !"
        else:
            met "Enfin bon tu as raison, ce ne sont pas les seuls étudiants de ce lycée. Aucune raison de rester bloquée sur ces deux là !"


    pov "D'ailleurs, ce serait possible de me présenter rapidement à d'autres élèves ?"

    show metalice coucou fermes

    met "Bien sûr ! Mais pas là, on va arriver en retard, allons-y !"

    jump Premiercours

    return

label Premiercours:
    scene classe with fade

    inc "Aller aller, un peu de silence !"

    show mickey chonti with fade

    mic "Bonjour à tous !"
    tlm "Bonjour monsieur Max !"
    mic "Asseyez-vous."
    show mickey normal
    if sex=="m":
        mic "Aujourd'hui, nous avons l'honneur d'accueillir un nouvel étudiant parmi nous."
    else:
        mic "Aujourd'hui, nous avons l'honneur d'accueillir une nouvelle étudiante parmi nous."
    mic "[povname], tu veux bien venir au tableau te présenter quelques secondes ?"
    pov "..."
    pov "Bien sûr monsieur Max..."
    "En parcourant brièvement la classe des yeux, j'essaie de graver toutes ces nouvelles têtes dans ma mémoire."
    hide mickey normal

    show moguri croise rigole at right
    show medoc happy at left

    "Medoc et Moguri, évidemment..."

    hide medoc happy

    hide moguri croise rigole

    show metalice coucou fermes

    "Metalice ! Ses renseignements de tout à l'heure vont m'être très utiles... Je pense m'être fait ma première amie !"

    hide metalice coucou fermes

    "Mais aussi d'autres personnes..."

    show dieuv deg

    "Celui là par exemple, dégage une aura de malfrat."
    "Mais il étudie ici... Je ne pense pas qu'il soit si méchant que ça !"
    "Ca ne me ressemble pas de juger sur les apparences pourtant..."
    "Bref."

    hide dieuv deg

    pov "Bonjour tout le monde. Mon nom est [povname] et c'est mon premier jour à l'Académie."
    pov "Mes passions sont la littérature, le cinéma et les jeux-vidéo..."
    if sex=="m":
        pov "Je suis ravi d'avoir été accepté dans cette classe, même si je ne suis pas aussi exceptionnel que v-"
    else:
        pov "Je suis ravie d'avoir été acceptée dans cette classe, même si je ne suis pas aussi exceptionnelle que v-"

    with shortflash
    show medoc colere poing with shortflash

    "BLAM!!"
    med "Bon t'as pas bientôt fini avec ses histoires de 'Je n'ai pas ma place ici, vous valez mieux que moi' ou je sais pas quoi !?"
    med "T'as pas écouté ce que t'a dit Moguri ou quoi ?!"

    hide medoc colere poing
    show moguri deg croise

    mog "C'est bon Medoc, lâche l'affaire."

    show moguri croise rigole

    if sex=="m":
        mog "Il ne pense clairement pas à mal, n'est-ce pas ?"
    else:
        mog "Elle ne pense clairement pas à mal, n'est-ce pas ?"

    hide moguri croise rigole
    show dieuv col

    if sex=="m":
        inc "Ouais Medoc, c'est son problème de confiance en lui, pas le tieng !"
    else:
        inc "Ouais Medoc, c'est son problème de confiance en elle, pas le tieng !"

    "Ce type a vraiment un drôle d'accent..."

    show dieuv smug

    inc "Même si on sait que t'es un pro pour t'approprier des trucs qui ne t'appartiennent pas..."

    hide dieuv smug
    show medoc colere poing

    med "Ah ouais ?! Répète ça pour voir ?"

    hide medoc colere poing
    show dieuv col

    inc "Un peu que je vais répéter peuchèreuh ! Tu crois que j'ai oublié pour Jeud-"

    hide dieuv col
    with shortflash
    with shortflash
    show metalice colere rouge

    met "Aller c'est bon ! Laissez tomber les gars ! Vous vous donnez en spectacle"

    hide metalice colere rouge
    show mickey colere

    mic "Elle a raison... Rasseyez-vous les garçons, je croyais que c'était derrière vous tout ça..."

    show mickey happy

    mic "Quant à toi Metalice, tu as accompli ton rôle de déléguée à la perfection."

    hide mickey happy
    show metalice coucou fermes

    met "Merci monsieur Max !"

    hide metalice coucou fermes
    show mickey chonti

    mic "Tu peux retourner à ta place [povname], merci pour ta présentation."
    show mickey normal
    mic "Je suis désolé que tu aies eu à être témoin de cette altercation."
    show mickey deg
    mic "Medoc, Dieuvomi, vous viendrez me voir à la fin du cours..."

    hide mickey deg
    show medoc deg

    med "Tch."

    hide medoc deg
    show dieuv deg

    dieuv "Mmmm."

    hide dieuv deg
    show mickey chonti

    mic "Bien ! Ouvrez vos livres page 77, on va commencer la trigonométrie..."

    show mickey happy
    with longfade

    mic "Aller, ce sera tout pour aujourd'hui, vous pouvez y aller !"
    show mickey deg
    mic "Sauf vous, Medoc et Dieuvomi, évidemment..."

    scene couloir with fade
    show metalice coucou fermes

    met "Bon. Et bien c'était une grosse première journée pour toi n'est-ce pas ?"
    pov "Oui on peut dire ça..."
    show metalice coucou
    pov "Dis, c'était qui ce type au style de voyou, avec l'accent exotique ?"
    show metalice coucou clindoeil
    met "Dieuvomi ? C'est pas VRAIMENT un voyou, c'est juste un style qu'il se donne."
    show metalice coucou
    met "Il ne te fera jamais de mal, à moins que tu sois un apocope de bandage pneumatique"
    pov "Un quoi ?"
    show metalice deg
    met "Un pneu. Il a un souci avec ça je crois, il aime beaucoup les crever."
    show metalice coucou
    met "Il s'est débarassé d'un gang qui gangrenait la ville à lui tout seul d'ailleurs !"
    pov "Je t'avoue que je ne vois pas particulièrement le rapport..."
    show metalice clindoeil
    met "La spécificité de ce gang était que ses membres ne se déplaçaient qu'en BMX. Leur principale méthode d'agression était de rouler sur leurs victimes..."
    pov "Mais... C'est stupide ?"
    show metalice coucou fermes
    met "Peut être, mais ça fait mal !"
    met "Dieuvomi a crevé tous les pneus de tous les BMX du gang en l'espace d'une heure, en pleine nuit..."
    pov "Ouaaaaah..."
    show metalice coucou
    met "N'est-ce pas ? Du coup, sans pneus, le gang s'est dissout de lui même. C'est aussi pour ça qu'il est aussi respecté !"
    met "Et autre point de détail de cette anecdote, le leader de ce gang était un cousin de Medoc..."
    pov "Aaaaaah ! C'est donc de là que vient cette animosité entre eux ?"
    show metalice coucou fermes
    met "Pas du tout ! Medoc ne tolérait absolument pas les agissements de son cousin."
    pov "D'où est-ce que ça vient alors ?"
    show metalice decue
    met "On n'aime pas trop en parler ici... Ca nous rappelle des événements un peu sombre. Tu l'apprendras bien assez tôt je pense."
    pov "..."
    show metalice coucou fermes
    met "Bon allez, je te ramène chez toi ? J'ai encore pas mal de chose à te raconter tu sais ?"

    pause 3
    return
