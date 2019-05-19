import random
inner_pov_couloirs = ["Pourquoi il n'y pas de carte de l'Académie... Ça sert de lire une carte !",
        "Pourquoi il n'y pas de carte de l'Académie... Ça sert de lire une carte !",
        "Le club #tech ne doit plus être très loin !",
        "Nom de nom ! J'en reviens pas que Metalice éternue de la sorte. C'est vraiment la preuve que c'est une femme de caractère !",
        "J'en reviens pas qu'ils laissent faire des spectacles à ce Foulk. C'est surement subventionné par la région...",
        "Le club #tech ne doit plus être très loin, ça sent les nouilles !",
        "Trouvons ce club #tech ! Ze PilOt avait l'air tellement talentueux !",
        "Le Club #tech ? ah non, c'est #radiohead... aucun intérêt.",
        "Mais #tech et Matt Pokora... J'en peux plus, vivement que j'arrive...",
        "Encore un couloir et pas de club #tech...",
        "Ce club #tech est une opportunité unique ! ",
        "Dépot sauvage de peuneus interdit. Signé La direction.",
        "Mais c'est pas possible, je tourne en rond !",
        "Ces types sont des malades ! Ils m'ont fait flipper !",
        "Encore un couloir et pas de club #tech..."
]

num_inner_pov_couloirs = len(inner_pov_couloirs)
inner_pov_chosen = list(range(0, num_inner_pov_couloirs))

print(inner_pov_chosen)

chosen = inner_pov_chosen.pop(random.randint(0,len(inner_pov_chosen)-1))
print(inner_pov_couloirs[chosen])

chosen = inner_pov_chosen.pop(random.randint(0,len(inner_pov_chosen)-1))
print(inner_pov_couloirs[chosen])

chosen = inner_pov_chosen.pop(random.randint(0,len(inner_pov_chosen)-1))
print(inner_pov_couloirs[chosen])

chosen = inner_pov_chosen.pop(random.randint(0,len(inner_pov_chosen)-1))
print(inner_pov_couloirs[chosen])

chosen = inner_pov_chosen.pop(random.randint(0,len(inner_pov_chosen)-1))
print(inner_pov_couloirs[chosen])

chosen = inner_pov_chosen.pop(random.randint(0,len(inner_pov_chosen)-1))
print(inner_pov_couloirs[chosen])

chosen = inner_pov_chosen.pop(random.randint(0,len(inner_pov_chosen)-1))
print(inner_pov_couloirs[chosen])

chosen = inner_pov_chosen.pop(random.randint(0,len(inner_pov_chosen)-1))
print(inner_pov_couloirs[chosen])





