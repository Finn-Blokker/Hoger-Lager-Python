import random

import pygame
import pygame_widgets
from pygame_widgets.button import Button


class Hoger_Lager():
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

            button = Button(
                # Mandatory Parameters
                screen,  # Surface to place button on
                760,  # X-coordinate of top left corner
                850,  # Y-coordinate of top left corner
                400,  # Width
                150,  # Height

                # Optional Parameters
                text='Hello',  # Text to display
                textColour=(255, 255, 255),
                fontSize=50,  # Size of font
                margin=20,  # Minimum distance between text/image and edge of button
                inactiveColour=(0, 0, 0),  # Colour of button when not being interacted with
                hoverColour=(0, 255, 0),  # Colour of button when being hovered over
                pressedColour=(0, 200, 20),  # Colour of button when being clicked
                onClick=lambda: Hoger_Lager.start_game())  # Function to call when clicked on

            pygame.draw.rect(screen, (255, 0, 0),  # border start button
                             [760, 850, 400, 150], 7)

            # flip() the display to put your work on screen
            pygame_widgets.update(event)
            pygame.display.flip()
            dt = clock.tick(60) / 1000

    def start_game():
        Hoger_Lager.game()
        exit()

    def game():
        pygame.init()
        pygame.font.init()
        my_title_font = pygame.font.SysFont("comic Sans MS", 90)
        screen = pygame.display.set_mode((1920, 1080))
        clock = pygame.time.Clock()
        hoger_lager = True
        dt = 0

        nr = int(random.uniform(1, 52))

        while hoger_lager == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    hoger_lager = False

            # dingen op het scherm
            screen.fill("#005012")

            text_surface = my_title_font.render("SCORE", False, (0, 255, 0))
            screen.blit(text_surface, (100, 120))

            card = pygame.image.load(f"cards/back_card.png")
            scaled_card = pygame.transform.scale(card, (360, 480))
            screen.blit(scaled_card, (120, 300))

            card = pygame.image.load(f"cards/8BitDeck{nr}.png")
            scaled_card = pygame.transform.scale(card, (360, 480))
            screen.blit(scaled_card, (650, 300))

            pygame.display.flip()
            dt = clock.tick(60) / 1000

    pygame.quit()


class Kaart:
    def __init__(self, waarde, sprite):
        self.waarde = waarde
        self.sprite = sprite

    def __str__(self):
        return f"{self.naam(self.waarde)} van {self.sprite}"

    def naam(self, waarde):
        namen = {11: "Boer", 12: "Vrouw", 13: "Heer", 14: "Aas"}
        return namen.get(waarde, str(waarde))

Hoger_Lager.title()
