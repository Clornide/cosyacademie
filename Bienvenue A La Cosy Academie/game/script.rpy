# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"
image intro = "BienvenueAlaCosyAcademie_intro.png"

#esprism
image Esprism = "Esprism_Naked.png"

#joueur
image side player = ConditionSwitch("sex==\"m\"", "boy.png", "True", "girl.png")
image brise = "vent.png"

#fonds
image reverie = "reverie.jpg"
image school entrance = "background/schoolEntrance.png"
image school hallway = "background/hallway.png"
image school hallway night = "background/hallway_night.png"


image school hallway choice = "background/hallway_choice.png"
image school hallway choice alt1 = "background/hallway_choice_alt_1.png"
image school hallway choice alt2 = "background/hallway_choice_alt_2.png"
image school hallway choice alt3 = "background/hallway_choice_alt_3.png"
image school hallway choice alt4 = "background/hallway_choice_alt_4.png"
image school hallway choice alt5 = im.Flip("background/hallway_choice.png", horizontal=True)
image school hallway choice alt6 = im.Flip("background/hallway_choice_alt_1.png", horizontal=True)
image school hallway choice alt7 = im.Flip("background/hallway_choice_alt_2.png", horizontal=True)
image school hallway choice alt8 = im.Flip("background/hallway_choice_alt_3.png", horizontal=True)
image school hallway choice alt9 = im.Flip("background/hallway_choice_alt_4.png", horizontal=True)
image school hallway choice creepy = "background/couloir_creepy.png"

image theater = "background/theater.png"
image bar = "background/cosyBar.png"
image gym = "background/gym.png"
image tracks = "background/tracks.png"
image street day = "background/streetDay.png"
image rando = "background/rando.png"
image classroom = "background/classroom.png"
image classroom night = "background/classroom_night.png"


# Déclarez les personnages utilisés dans le jeu.

init python:

    txt1 = ""
    txt2 = ""
    txt3 = ""
    
    renpy.music.register_channel("talking", mixer="sfx", loop=True)
    

    def word_effect(txt):

        global txt1, txt2, txt3
        txt1 = txt
        txt2 = ""
        txt3 = ""
        i = 2
        for letter in txt:
            i += 1
            if i % 2 == 0:
                txt2 += "{size=+1}" + letter + "{/size}"
                # Instead of "size" any text tag can be applied here,
                # see: http://www.renpy.org/doc/html/text.html#styling-and-text-tags
                txt3 += "{size=-2}" + letter + "{/size}"
            else:
                txt2 += "{size=-2}" + letter + "{/size}"
                txt3 += letter


    def has_zoom_tag(tag):
        attributes = renpy.get_at_list(tag)
        if zoom in attributes:
            return True
        return False


    def is_shaded(tag):
        attributes = renpy.get_at_list(tag)
        if shade_transform in attributes:
            return True
        return False        

   

    def char_callback(event, interact=True, **kwargs):

        if event == "show" or event == "begin":
            
            
            #renpy.music.set_pause(False, channel="talking")
            renpy.sound.play("sounds/text-sound.mp3", channel="talking")

        if event == "slow_done" or event == "end":
            #renpy.music.set_pause(True, channel="talking")
            renpy.sound.stop(channel="talking")


        showing_tags = renpy.get_showing_tags(layer='master')

        current_tag = renpy.get_say_image_tag()

        

        png = ["Medoc", "Moguri", "Metalice", "Mickey", "Dieuvomi", "Esprism", "Von", "Mathilde", "Chuenpodo", "Caro", "din", "Foulk", "Lock", "ZePilot"]
        
        character_displayed_tags = [
            t for t in png
            if t in showing_tags
        ]

        character_tags = [
            t for t in
            character_displayed_tags
            if  t != current_tag
        ]


        if current_tag == "player":

            for tag in character_tags:
                renpy.show(tag, at_list = [normalalpha])
                    

            return 

        if current_tag and event == "begin":
            
            char_speaking = True
            for tag in character_tags:
                renpy.show(tag, at_list = [shade_transform])

            if current_tag in showing_tags:
                if len(character_displayed_tags) > 1:
                    renpy.show( current_tag)
                else:
                    renpy.show( current_tag, at_list = [normalalpha])

        return (), kwargs



    config.all_character_callbacks.append( char_callback )


image we1:
    Text("[txt2]")
    pause .2
    Text("[txt3]")
    pause .2
    repeat

define pov = Character("[povname]", color="#fff", image="player", screen = "say_classic")
define innerpov = Character("[povname]", color="#a1e7df", text_color="#a1e7df", image="player", who_suffix=" {i}{size=-5}[toSelf]{/size}{/i}", what_prefix="{i}", what_suffix="{/i}", screen="say_innerpov" )
define med = Character('name_medoc', color="#fff", image="Medoc", dynamic = True, screen = "say_classic" )
define mog = Character('name_moguri', color="#fff", image="Moguri", dynamic = True, screen = "say_classic")
define met = Character('name_metalice', color="#fff", image="Metalice", dynamic = True, screen = "say_classic")
define mic = Character('name_mickey', color="#fff" , image="Mickey", dynamic = True, screen = "say_classic")
define dieuv = Character('name_dieuvomi', color="#fff", image="Dieuvomi", dynamic = True, screen = "say_classic")
define esprism = Character('name_esprism', color="#fff", image="Esprism", dynamic = True, screen = "say_classic")
define lock = Character('name_lock', color="#fff", image="Lock", dynamic = True, screen = "say_classic")
define zep = Character('name_zep', color="#fff", image="ZePilot", dynamic = True, screen = "say_classic")
define von = Character('name_von', color="#fff", image="Von", screen="say_von", dynamic = True)
define mat = Character('name_mathilde', color="#fff", image="Mathilde", dynamic = True, screen = "say_classic")
define chuen = Character('name_chuen', color="#fff", image="Chuenpodo", screen="say_chuen", dynamic = True)
define caro = Character('name_caro', color="#fff", image="Caro", dynamic = True, screen = "say_classic")
define din = Character('name_din', color="#fff", image="din", dynamic = True, screen = "say_classic")
define foulk = Character('name_foulk', color="#fff", image="Foulk", dynamic = True, screen = "say_classic")
define clornide = Character('Clornide', color="#fff", image="Clornide", screen = "say_classic")
define samael = Character('Samaël', color="#fff", image="Samael", screen = "say_classic")
define decade = Character('Decade', color="#fff", image="Decade", screen = "say_classic")
define cheers = Character('name_cheers', color="#fff", dynamic = True, screen = "say_classic")
define inc = Character('???', color="#fff", screen = "say_classic")
define tlm = Character('Tout le monde', color="#fff", screen = "say_classic")
define noName = Character('', color="#fff", screen = "say_classic")


#Effets nouveaux
define longfade = Fade(0.8, 0.2, 0.8, color="#000")
define shortflash = Fade(.1, 0, .1, color="#fff")
define flash = Fade(.25, 0, .75, color="#fff")
define animintro = Fade(0.8, 0.2, 0.8, color="#fff")


image petit couteau movie = Movie(play="movies/le_petit_couteau.mp4")

#Musique
define audio.memento = "music/Memento.mp3"
define audio.haunted = "music/Haunted House.mp3"
define audio.journeys = "music/sb_journeys.mp3"
define audio.tomorrow = "music/sb_tomorrow.mp3"
define audio.wonderful = "music/sb_wonderful.mp3"
define audio.comedy = "music/sb_skyscrapersamba_eq_lessdrums.mp3"
define audio.gym = "music/sb_red_altmix.mp3"
define audio.epic = "music/sb_pursuit.mp3"
define audio.rainbow = "music/sb_rainbows.mp3"
define audio.kawaii = "music/Cute_Upbeat_Kawaii.mp3"

#FX
define audio.woosh = "sounds/creepy-hifreq-woosh.mp3"
define audio.wind = "sounds/Wind-Mark_DiAngelo-1940285615.wav"
define audio.badamtsss = "sounds/badamtsss.mp3"
define audio.auraDBZStart = "sounds/aura_dbz_start.mp3"
define audio.auraDBZ = "sounds/aura_dbz.mp3"
define audio.auraSeiya = "sounds/aura_seiya.mp3"
define audio.ATATATATA = "sounds/ATATATATA.mp3"

# Le jeu commence ici
label start:

    menu:

        noName "Avant de commencer, voulez-vous incarner un personnage féminin ou masculin ?"

        "Féminin.":
            python:
                sex = "f"
                toSelf= "à elle-même"
        "Masculin.":
            python:
                sex = "m"
                toSelf= "à lui-même"

    noName "{nw}"
    #window hide
    
    show screen affection
    python:

        name_dieuvomi = "???"
        name_medoc = "Medoc"
        name_moguri = "Moguri"
        name_metalice = "Metalice"
        name_mickey = "Mickey"
        name_esprism = "Esprism"
        name_von = "Von Yaourt"
        name_chuen = "???"
        name_mathilde = "???"
        name_caro = "Caro"
        name_din = "din"
        name_foulk = "Foulk"
        name_lock = "Lock"
        name_zep = "???"
        name_clornide = "Clornide"
        name_cheers = "Panthusiasts"

        #Points routes
        pointsmedoc=0
        pointsmoguri=0
        pointsincel=0

        mathilde_medoc = False

        if sex=="m":
            povname = renpy.input("Veuillez renseigner votre prénom ? Par défaut vous serez appelé Hector.", length = 40)
            povname = povname.strip()

            while povname=="moguri" or povname=="Moguri" or povname=="medoc" or povname=="Medoc" :
                povname = renpy.input("Pas Medoc ou Moguri svp")
                povname = povname.strip()
            if not povname:
                povname="Hector"

        else:
            povname = renpy.input("Veuillez renseigner votre prénom ? Par défaut vous serez appelé Cassandre.", length = 40)
            povname = povname.strip()

            while povname=="moguri" or povname=="Moguri" or povname=="medoc" or povname=="Medoc" :
                povname = renpy.input("Pas Medoc ou Moguri svp")
                povname = povname.strip()
            if not povname:
                povname="Cassandre"

    window auto
    

    jump intro

        

    


    