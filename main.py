import pygame
import pygame_widgets
from pygame_widgets.button import Button


def title():
    pygame.init()
    pygame.font.init()
    my_title_font = pygame.font.SysFont("comic Sans MS", 90)
    screen = pygame.display.set_mode((1920, 1080))
    clock = pygame.time.Clock()
    title_screen = True
    dt = 0

    while title_screen == True:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                title_screen = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("#005012")

        text_surface = my_title_font.render("HOGER", False, (0, 255, 0))
        screen.blit(text_surface, (650, 120))

        text_surface = my_title_font.render("LAGER", False, (255, 0, 0))
        screen.blit(text_surface, (1050, 120))

        pygame.draw.rect(screen, (0, 0, 0),
                         [640, 200, 640, 350])
        pygame.draw.rect(screen, (255, 0, 0),  # border highscore box
                         [640, 200, 640, 350], 7)  # pixels vanaf links, pixels vanaf boven, breedte, hoogte

        pygame.draw.rect(screen, (255, 0, 0),  # border username box
                         [640, 600, 640, 180], 7)  # pixels vanaf links, pixels vanaf boven, breedte, hoogte

        pygame.draw.rect(screen, (255, 0, 0),  # border start button
                         [760, 850, 400, 150], 7)

        button = Button(
            # Mandatory Parameters
            screen,  # Surface to place button on
            100,  # X-coordinate of top left corner
            100,  # Y-coordinate of top left corner
            300,  # Width
            150,  # Height

            # Optional Parameters
            text='Hello',  # Text to display
            fontSize=50,  # Size of font
            margin=20,  # Minimum distance between text/image and edge of button
            inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
            hoverColour=(150, 0, 0),  # Colour of button when being hovered over
            pressedColour=(0, 200, 20),  # Colour of button when being clicked
            onClick=lambda: start_game()) # Function to call when clicked on


        # flip() the display to put your work on screen
        pygame_widgets.update(event)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

def start_game():
    game()
    exit()

def game():
    pygame.init()
    pygame.font.init()
    my_title_font = pygame.font.SysFont("comic Sans MS", 90)
    screen = pygame.display.set_mode((1920, 1080))
    clock = pygame.time.Clock()
    hoger_lager = True
    dt = 0
    while hoger_lager == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                hoger_lager = False
        screen.fill("#FF0000")
        pygame.display.flip()
        dt = clock.tick(60) / 1000

pygame.quit()


title()
