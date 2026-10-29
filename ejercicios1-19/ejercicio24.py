# 1
videojuegos = ["Castlevania","Street Fighter II","Super mario bros"]
videojuegos.append("Tetris")
videojuegos.remove("Castlevania")
for v in videojuegos:
    print(f"{v:-<20} es genial")
    
    print(f"{v:-<20} es genial".upper())

# 2
consolas = ("GameCube","SNES","PlayStation 2")
for c in consolas:
    print(f"{c:-<20} es la mejor consola")
print(consolas[2])

# 3
videojuego_precio = {"Castlevania": 4.55,
                     "Street Fighter II":8.00,
                     "Super Mario": 6}
for k,v in videojuego_precio.items():
    print(f"{k:*<20}: {v:>7}€")

#4
print(f"{'':*<50}")
for juego in videojuego_precio:
    videojuego_precio[juego] +=2
for k,v in videojuego_precio.items():
    print(f"{k:*<20}: {v:>10.2f}€")

#5

for j in videojuego_precio.values():
    print(f"{j:.2f}€")

#6

videojuego = "Super Mario Maker"
texto_final= ''
for letra in videojuego:
    texto_final += letra
    print(texto_final)

