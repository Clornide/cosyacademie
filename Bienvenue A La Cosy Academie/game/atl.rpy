
transform centerzoomed:
  xpos 0.5 xanchor 0.5 ypos 1.0 yanchor 0.65 zoom 1.5 

transform leftzoomed:
  xpos 0.0 xanchor 0.0 ypos 1.0 yanchor 0.65 zoom 1.5

transform rightzoomed:
  xpos 1.0 xanchor 1.0 ypos 1.0 yanchor 0.65 zoom 1.5

transform left:
    xpos 0.1 xanchor 0.0 ypos 1.0 yanchor 1.0

transform right:
    xpos 0.9 xanchor 1.0 ypos 1.0 yanchor 1.0

transform center:
    xpos 0.5 xanchor 0.5 ypos 1.0 yanchor 1.0

transform truecenter:
    xpos 0.5 xanchor 0.5 ypos 0.5 yanchor 0.5

transform topleft:
    xpos 0.0 xanchor 0.0 ypos 0.0 yanchor 0.0

transform topright:
    xpos 1.0 xanchor 1.0 ypos 0.0 yanchor 0.0

transform top:
    xpos 0.5 xanchor 0.5 ypos 0.0 yanchor 0.0

transform snl_pos:
  xpos 1.0 xanchor 1.0 ypos 0.5 yanchor 0.5 zoom 1.0 rotate -5.0

transform normalalpha:
  alpha 1.0

transform zoom:
  ypos 1.3 zoom 1.3
  alpha 1.0

transform lightzoom:
  ypos 1.4 zoom 1.4

transform mediumzoom:
  ypos 1.5 zoom 1.5

transform bigzoom:
  ypos 1.7 zoom 1.7

transform hugezoom:
  ypos 2.0 zoom 2.0

transform normalzoom:
  ypos 1.0 zoom 1.0  
  alpha 1.0
  

transform alphatransform:
    alpha 0.8

init python:
    def shade_transform(d):
        return AlphaBlend(alphatransform(d), d, Solid("#000", xysize=(1920, 1080)), True)

transform panse_pignoles_anim:
    zoom 0.5
    ypos 2.0
    "pansepignoles/1.png"
    linear 1.0 ypos 1.0     
    
    pause 1
    "pansepignoles/2.png"
    zoom 0.5
    pause 1
    "pansepignoles/3.png"
    zoom 0.5
    pause 1

image panse_pignoles_chouine:
    zoom 0.5
    "pansepignoles/4.png"
    on hide:
        xalign 0.5
        
        ypos 1.0
        linear 1.0 ypos 2.0     

image chuen_stop_show:
    "Chuenpodo/main_BrasCroises_01_Badboy.png"
    on show:
        xalign 0.3
        zoom 0.4
        ypos 2.0
        linear 1.0 ypos 1.0  


image chuen_stop_hide:        
    zoom 0.4
    xalign 0.3
    "Chuenpodo/main_BrasCroises_03_Colere.png"
    on hide:
        xalign 0.3
        zoom 0.4
        ypos 1.0
        linear 1.0 ypos 2.0 


image panse_pignoles:
    panse_pignoles_anim

        


    # window hide
    # show panse_pignoles
    # pause 3
    # show chuen_stop_show
    # pause 1
    # show chuen_stop_hide with flash
    # pause 3
    # hide chuen_stop_show
    # hide chuen_stop_hide
    # pause 1
    # hide panse_pignoles
    # show panse_pignoles_chouine
    # pause 2
    # hide panse_pignoles_chouine
    # pause 2
    # window show


