
#Juan Sebastian Peña Angarita

#importando os
import os

#Definiendo el tamaño de la ventana en donde se despliega el juego
SCREENSIZE= (956, 556)

FONTPATH = os.path.join(os.getcwd(), 'resources/font/simkai.ttf')

#Diccionaro que contiene las imagenes de mi carpeta
IMAGEPATHS = {
    'asteroid': os.path.join(os.getcwd(), 'resources/images/asteroid.png'),
    'image1': os.path.join(os.getcwd(), 'resources/images/image2.png'),
    'unam': os.path.join(os.getcwd(), 'resources/images/unam.png'),
    'bg_big': os.path.join(os.getcwd(), 'resources/images/bg_big.png'),
    'bullet': os.path.join(os.getcwd(), 'resources/images/bullet.png'),
    'seamless_space': os.path.join(os.getcwd(), 'resources/images/seamless_space.png'),
    'ship': os.path.join(os.getcwd(), 'resources/images/uamito.png'),
    'ship_exploded': os.path.join(os.getcwd(), 'resources/images/ship_exploded.png'),
    'space3': os.path.join(os.getcwd(), 'resources/images/space3.jpg')
}

#diccionario que contiene los sonidos de mi juego
SOUNDPATHS = {
    'boom': os.path.join(os.getcwd(), 'resources/sounds/boom.wav'),
    'Cool Space Music': os.path.join(os.getcwd(), 'resources/sounds/Cool Space Music.mp3'),
    'shot': os.path.join(os.getcwd(), 'resources/sounds/shot.ogg'),
    'tequila': os.path.join(os.getcwd(), 'resources/sounds/tequila.mp3'),
    'molinos': os.path.join(os.getcwd(), 'resources/sounds/molinos.mp3')
}

