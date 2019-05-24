
transform centerzoomed:
  xpos 0.5 xanchor 0.5 ypos 1.0 yanchor 0.65 zoom 1.5 

transform leftzoomed:
  xpos 0.0 xanchor 0.0 ypos 1.0 yanchor 0.65 zoom 1.5

transform rightzoomed:
  xpos 1.0 xanchor 1.0 ypos 1.0 yanchor 0.65 zoom 1.5

transform left:
    xpos 0.1 xanchor 0.0 ypos 1.0 yanchor 1.0

transform full_left:
    xpos 0.0 xanchor 0.0 ypos 1.0 yanchor 1.0    

transform right:
    xpos 0.9 xanchor 1.0 ypos 1.0 yanchor 1.0

transform full_right:
    xpos 1.0 xanchor 1.0 ypos 1.0 yanchor 1.0    

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
  ypos 1.3 zoom 1.3 yanchor 1.0

transform lightzoom:
  ypos 1.4 zoom 1.4 yanchor 1.0

transform mediumzoom:
  ypos 1.5 zoom 1.5 yanchor 1.0

transform bigzoom:
  ypos 1.7 zoom 1.7 yanchor 1.0

transform hugezoom:
  ypos 2.0 zoom 2.0 yanchor 1.0

transform normalzoom:
  ypos 1.0 zoom 1.0 yanchor 1.0

transform yanchorreset:
  yanchor 1.0


transform jumping:
    linear 0.1 ypos 1.2 
    linear 0.1 ypos .9
    linear 0.1 ypos 1.0
    
transform go_away_interrupt:
    #xpos 0.9 xanchor 1.0 ypos 2.0 yanchor 1.0 zoom 1.3
    linear 0.1 xpos 0.9 ypos 1.2
    linear 0.1 xpos 0.95 ypos 1.35
    linear 0.1 xpos 1.0 ypos 1.2
    linear 0.1 xpos 1.05 ypos 1.35
    linear 0.1 xpos 1.1 ypos 1.2
    linear 0.1 xpos 1.15 ypos 1.35
    linear 0.1 xpos 1.20 ypos 1.2
    linear 0.1 xpos 1.25 ypos 1.35
    linear 0.1 xpos 1.30 ypos 1.2
    linear 0.1 xpos 1.35 ypos 1.35
    linear 0.1 xpos 1.4 ypos 1.2
    linear 0.1 xpos 1.45 ypos 1.35
    linear 0.1 xpos 1.5 ypos 1.2
    linear 0.1 xpos 1.55 ypos 1.35

transform go_away_chuen:

    linear 0.1 xpos 0.1 ypos 1.4
    linear 0.1 xpos .2 ypos 1.55
    linear 0.1 xpos 0.3 ypos 1.4
    linear 0.1 xpos 0.4 ypos 1.55
    linear 0.1 xpos 0.5 ypos 1.4
    linear 0.1 xpos 0.6 ypos 1.55
    linear 0.1 xpos 0.7 ypos 1.4
    linear 0.1 xpos 0.8 ypos 1.55
    linear 0.1 xpos 0.9 ypos 1.4
    linear 0.1 xpos 1.0 ypos 1.55
    linear 0.1 xpos 1.1 ypos 1.4
    linear 0.1 xpos 1.2 ypos 1.55
    linear 0.1 xpos 1.3 ypos 1.4
    linear 0.1 xpos 1.4 ypos 1.55
    linear 0.1 xpos 1.5 ypos 1.4

transform go_away:
    linear 0.1 xpos 1.1 ypos 1.1
    linear 0.1 xpos 1.2 ypos .9
    linear 0.1 xpos 1.3 ypos 1.1
    linear 0.1 xpos 1.4 ypos .9
    linear 0.1 xpos 1.5 ypos 1.1
    linear 0.1 xpos 1.6 ypos .9
    linear 0.1 xpos 1.7 ypos 1.1
    linear 0.1 xpos 1.8 ypos .9
    linear 0.1 xpos 1.9 ypos 1.1

transform go_back_in_place:
    xpos 2.0 ypos 1.1 zoom 1.0
    linear 0.1 xpos 1.9 ypos 1.1 
    linear 0.1 xpos 1.8 ypos .9
    linear 0.1 xpos 1.7 ypos 1.1
    linear 0.1 xpos 1.6 ypos .9
    linear 0.1 xpos 1.5 ypos 1.1
    linear 0.1 xpos 1.4 ypos .9
    linear 0.1 xpos 1.3 ypos 1.1
    linear 0.1 xpos 1.2 ypos .9
    linear 0.1 xpos 1.1 ypos 1.1
    linear 0.1 xpos 1.0 ypos 1.0


transform dezoom:
    zoom 0.5

transform go_left_to_right:
    xpos 1.5
    linear 0.2 xpos 1.5 ypos 1.1
    linear 0.2 xpos 1.4 ypos 1.0
    linear 0.2 xpos 1.3 ypos 1.1
    linear 0.2 xpos 1.2 ypos 1.0
    linear 0.2 xpos 1.1 ypos 1.1
    linear 0.2 xpos 1.0 ypos 1.0
    linear 0.2 xpos 0.9 ypos 1.1
    linear 0.2 xpos 0.8 ypos 1.0
    linear 0.2 xpos 0.7 ypos 1.1
    linear 0.2 xpos 0.6 ypos 1.0
    linear 0.2 xpos 0.5 ypos 1.1
    linear 0.2 xpos 0.4 ypos 1.0
    linear 0.2 xpos 0.3 ypos 1.1
    linear 0.2 xpos 0.2 ypos 1.0
    linear 0.2 xpos 0.1 ypos 1.1
    linear 0.2 xpos 0.0 ypos 1.0
    linear 0.2 xpos -0.1 ypos 1.1
    linear 0.2 xpos -0.2 ypos 1.0
    linear 0.2 xpos -0.3 ypos 1.1
    linear 0.2 xpos -0.4 ypos 1.0
    linear 0.2 xpos -0.5 ypos 1.1
    
transform go_right_to_left:
    xpos -0.5
    linear 0.2 xpos -0.5 ypos 1.1
    linear 0.2 xpos -0.4 ypos 1.0
    linear 0.2 xpos -0.3 ypos 1.1
    linear 0.2 xpos -0.2 ypos 1.0
    linear 0.2 xpos -0.1 ypos 1.1
    linear 0.2 xpos 0.0 ypos 1.0
    linear 0.2 xpos 0.1 ypos 1.1
    linear 0.2 xpos 0.2 ypos 1.0
    linear 0.2 xpos 0.3 ypos 1.1
    linear 0.2 xpos 0.4 ypos 1.0
    linear 0.2 xpos 0.5 ypos 1.1
    linear 0.2 xpos 0.6 ypos 1.0
    linear 0.2 xpos 0.7 ypos 1.1
    linear 0.2 xpos 0.8 ypos 1.0
    linear 0.2 xpos 0.9 ypos 1.1
    linear 0.2 xpos 1.0 ypos 1.0
    linear 0.2 xpos 1.1 ypos 1.1
    linear 0.2 xpos 1.2 ypos 1.0
    linear 0.2 xpos 1.3 ypos 1.1
    linear 0.2 xpos 1.4 ypos 1.0
    linear 0.2 xpos 1.5 ypos 1.1

transform go_to_center:
    linear 1.0 xpos 2.0
    

transform alphatransform:
    alpha 0.8

image gym_shonen:
    
    ypos 1.0 zoom 1.01
    "background/gym.png"
    pause 0.01
    ypos 1.01 zoom 1.01
    pause 0.01

    repeat

image jumpscare:
    xpos 0.5 xanchor 0.5 ypos 0.0 yanchor 0.0 zoom 2.0
    "Cheerleaders/main_Groupe_03_Drop.png"
    pause 0.1
    xpos 0.5 xanchor 0.5 ypos 0.0 yanchor 0.0 zoom 2.5 
    pause 0.1
    repeat



image auraFN:
    zoom 1.0 ypos 1.0 alpha 0.4 yanchor 0.85 xpos 0.5
    "Assets/auraVon/auraFN.0.png"
    pause 0.03        
    "Assets/auraVon/auraFN.1.png"  
    pause 0.03
    "Assets/auraVon/auraFN.2.png"
    pause 0.03
    "Assets/auraVon/auraFN.3.png"
    pause 0.03
    "Assets/auraVon/auraFN.4.png"
    pause 0.03
    "Assets/auraVon/auraFN.5.png"
    pause 0.03
    "Assets/auraVon/auraFN.6.png"
    pause 0.03
    "Assets/auraVon/auraFN.7.png"
    pause 0.03        
    repeat

image auraFN_back:
    zoom 1.0 ypos 1.0 alpha 1.0 yanchor 0.85 xpos 0.5
    "Assets/auraVon/auraFN.0.png"
    pause 0.03        
    "Assets/auraVon/auraFN.1.png"  
    pause 0.03
    "Assets/auraVon/auraFN.2.png"
    pause 0.03
    "Assets/auraVon/auraFN.3.png"
    pause 0.03
    "Assets/auraVon/auraFN.4.png"
    pause 0.03
    "Assets/auraVon/auraFN.5.png"
    pause 0.03
    "Assets/auraVon/auraFN.6.png"
    pause 0.03
    "Assets/auraVon/auraFN.7.png"
    pause 0.03        
    repeat

image auraDBZ:
    zoom 2.0 ypos -0.6 alpha 0.5 yanchor 0.0 xpos 0.48
    "Assets/aura/Aura.1.png"  
    pause 0.03
    "Assets/aura/Aura.2.png"
    pause 0.03
    "Assets/aura/Aura.3.png"
    pause 0.03
    "Assets/aura/Aura.4.png"
    pause 0.03
    "Assets/aura/Aura.5.png"
    pause 0.03
    "Assets/aura/Aura.6.png"
    pause 0.03
    "Assets/aura/Aura.7.png"
    pause 0.03    
    "Assets/aura/Aura.8.png"
    pause 0.03        
    repeat

image aura3:
    zoom 1.2 ypos -0.1 alpha 1.0 yanchor 0.0
    "Assets/aura/aura3.0.png"  
    pause 0.03
    "Assets/aura/aura3.1.png"  
    pause 0.03
    "Assets/aura/aura3.2.png"  
    pause 0.03
    "Assets/aura/aura3.3.png"  
    pause 0.03
    "Assets/aura/aura3.4.png"  
    pause 0.03
    "Assets/aura/aura3.5.png"  
    pause 0.03
    "Assets/aura/aura3.6.png"  
    pause 0.03
    "Assets/aura/aura3.7.png"  
    pause 0.03
    "Assets/aura/aura3.8.png"  
    pause 0.03
    "Assets/aura/aura3.9.png"  
    pause 0.03
    "Assets/aura/aura3.10.png"  
    pause 0.03
    "Assets/aura/aura3.11.png"  
    pause 0.03
    "Assets/aura/aura3.12.png"  
    pause 0.03
    "Assets/aura/aura3.13.png"  
    pause 0.03
    "Assets/aura/aura3.14.png"  
    pause 0.03
    "Assets/aura/aura3.15.png"  
    pause 0.03
    "Assets/aura/aura3.16.png"  
    pause 0.03
    "Assets/aura/aura3.17.png"  
    pause 0.03
    "Assets/aura/aura3.18.png"  
    pause 0.03
    "Assets/aura/aura3.19.png"  
    pause 0.03
    "Assets/aura/aura3.20.png"  
    pause 0.03
    "Assets/aura/aura3.21.png"  
    pause 0.03
    "Assets/aura/aura3.22.png"  
    pause 0.03
    "Assets/aura/aura3.23.png"  
    pause 0.03
    "Assets/aura/aura3.24.png"  
    pause 0.03
    "Assets/aura/aura3.25.png"  
    pause 0.03
    "Assets/aura/aura3.26.png"  
    pause 0.03
    "Assets/aura/aura3.27.png"  
    pause 0.03
    "Assets/aura/aura3.28.png"  
    pause 0.03
    repeat

image auraSaintSeya:
    zoom 1.0 ypos 1.0 alpha 2.0 yanchor 1.0
    "Assets/aura/aura_SS.0.png"
    pause 0.04        
    "Assets/aura/aura_SS.1.png"  
    pause 0.04
    "Assets/aura/aura_SS.2.png"
    pause 0.04
    "Assets/aura/aura_SS.3.png"
    pause 0.04
    "Assets/aura/aura_SS.4.png"
    pause 0.04
    "Assets/aura/aura_SS.5.png"
    pause 0.04
    "Assets/aura/aura_SS.6.png"
    pause 0.04
    "Assets/aura/aura_SS.7.png"
    pause 0.04    
    "Assets/aura/aura_SS.8.png"
    pause 0.04
    "Assets/aura/aura_SS.9.png"
    pause 0.04
    "Assets/aura/aura_SS.10.png"
    pause 0.04
    "Assets/aura/aura_SS.11.png"
    pause 0.04
    "Assets/aura/aura_SS.12.png"
    pause 0.04
    "Assets/aura/aura_SS.13.png"
    pause 0.04
    "Assets/aura/aura_SS.14.png"
    pause 0.04
    "Assets/aura/aura_SS.15.png"
    pause 0.04
    "Assets/aura/aura_SS.16.png"
    pause 0.04
    "Assets/aura/aura_SS.17.png"
    pause 0.04
    "Assets/aura/aura_SS.18.png"
    pause 0.04
    "Assets/aura/aura_SS.19.png"
    pause 0.04
    

    repeat

init python:
    def shade_transform(d):
        return AlphaBlend(alphatransform(d), d, Solid("#000", xysize=(1920, 1080)), True)
