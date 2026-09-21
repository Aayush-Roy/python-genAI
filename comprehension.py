menus = [
    "Masala chai",
    "lemom Tea",
    "Iced Tea",
    "ginger Tea",
    "Iced lemon Tea"
]

iced_tea = [tea for tea in menus if len(tea) <12]
print(iced_tea)