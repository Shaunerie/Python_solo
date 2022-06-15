"""
ToDo_list:
-Penser dans le futur à utiliser comme librairie pour les futurs programmes ?
-Option menu avec sa propre boucle, partage de la musique et des autres qui restent entre les boucles pygame !

!!!!!!!!:
-généraliser les 11 cases à n cases
                    
                    
                    Main menu of this game. No idea what to do here. might do everything into it

"""
import pygame
import time

#----------------------------------------------------------------------___Classes___----------------------------------------------------------------------
class SURFACE():
    """
    Class for surfaces/blit for IMAGES ;)

    __init__(self, Folder):
        - image ==> load image of the surface thanks to the Folder (location of the file)
        - rect ==> rectangle of the surface

    display(self, Screen, Coordinates):
        - blit the image at the correct coordinates on the screen-pygame-object
    
    def scale(self, Size):
        - rescale a surface
    """

    def __init__(self, Folder):
        self.image = pygame.image.load(Folder)
        self.rect = self.image.get_rect()

    def display(self, Screen, Coordinates):
        Screen.blit(self.image, Coordinates)
    
    def scale(self, Size):
        self.image = pygame.transform.scale(self.image, Size)


#----------------------------------------------------------------------___Functions___----------------------------------------------------------------------
        
def map_init(Background_surface, Window_size):
    """
    Initiate de map 11x11 (maybe a change in the future ? for zoom or things like that, then map_init will be map_evolve ?)

    Background_surface: object of surface class
    return an empty 2D list with 11x11 cases
    """
    Background_surface.scale((Window_size[0]/11, Window_size[1]/11))
    Travel_value = []
    for i in range(11):
        Travel_value.append([])
        for j in range(11):
            Travel_value[i].append(Background_surface.image)
    
    return Travel_value

def window_update(Size):
    """
    update the correct ratio for the screen

    screen(pygame object ?)
    size ==> (l,w) 
    size = (-1, -1) ==> fullscreen


    return the new screen
    """
    if Size == (-1, -1):
        pygame.display.toggle_fullscreen()
    else:
        Screen = pygame.display.set_mode(Size)
    
    return Screen

def game():
    #___load pygame___
    pygame.init()

    #___create the window___
    pygame.display.set_caption('perso bouge !')
    Screen = window_update((990, 990))
    Window_size = pygame.display.get_window_size()
    print(Window_size)

    #___basic surfaces defined___
    #Background = SURFACE('img//naruto.jpeg')
    Map_background_surface = SURFACE('img//naruto.jpeg')

    #___useful variables___
    Running = True
    Map = map_init(Map_background_surface, Window_size) 

    while Running:
        pygame.display.update()

        #___always_blits___
        for i in range(len(Map)):
            for j in range(len(Map)):
                Screen.blit(Map[i][j], ((Window_size[0]/11)*i, (Window_size[0]/11)*j))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    Running = False

game()