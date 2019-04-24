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
define innerpov = Character("[povname]", color="#a1e7df", text_color="#a1e7df")
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

