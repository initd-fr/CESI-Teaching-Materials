import pygame
import subprocess
import time
import sys
# Initialisation de Pygame
pygame.init()

# ^ FENETRE

# Dimensions de la fenêtre
screen_width = 800
screen_height = 800

# Création de la fenêtre
screen = pygame.display.set_mode((screen_width, screen_height))

# Titre de la fenêtre
pygame.display.set_caption("MENU")

# ^ VARIABLES

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Police de caractères
font = pygame.font.SysFont("Arial", 30)

# ^ LOGO

# Logo
logo = pygame.image.load("./img/logo.png")
logo = pygame.transform.scale(logo, (logo.get_width() // 2, logo.get_height() // 2))

# ^ INPUTS PSEUDO

# État du formulaire
input_active = [False, False]  # Activation de la saisie pour les deux joueurs
player_names = ["", ""]
current_player = 0  # Joueur actuellement en train de saisir
show_names = False  # Indique si les noms des joueurs doivent être affichés
show_names_timer = 2  # Délai avant l'affichage des noms des joueurs en secondes
show_names_start_time = None # Temps auquel l'affichage des noms des joueurs a commencé

# Texte des joueurs
joueur_texts = ["Joueur 1 :", "Joueur 2 :"] # Texte des joueurs
joueur_surfaces = [font.render(joueur_texts[0], True, WHITE), font.render(joueur_texts[1], True, WHITE)] # Surfaces des textes des joueurs

# Inputs Pseudo
input_rects = [
    pygame.Rect(300, 350, 200, 40),
    pygame.Rect(300, 450, 200, 40)
]

# ^ BOUTONS

# Boutons
button_bg = BLACK
button_border = WHITE
button_quit_bg = RED
button_width = 200
button_height = 50
button_border_width = 2
button_spacing = 5

play_text = "Play" 
play_font = pygame.font.Font(None, 36)
play_surface = play_font.render(play_text, True, WHITE)
play_rect = pygame.Rect(
    (screen_width - button_width) // 2,
    500,
    button_width,
    button_height
)

quit_text = "Quit"
quit_font = pygame.font.Font(None, 36)
quit_surface = quit_font.render(quit_text, True, WHITE)
quit_rect = pygame.Rect(
    (screen_width - button_width) // 2,
    play_rect.bottom + button_spacing,
    button_width,
    button_height
)

# ^ Boucle de jeu
running = True # Boucle de jeu
while running:  # Tant que la boucle est active
    for event in pygame.event.get(): # Pour chaque événement
        if event.type == pygame.QUIT: # Si l'utilisateur ferme la fenêtre
            running = False # On arrête la boucle
        elif event.type == pygame.MOUSEBUTTONDOWN: # Si l'utilisateur clique
            if play_rect.collidepoint(event.pos): # Si le clic est sur le bouton "Play"
                if all(player_names): # Si les deux joueurs ont saisi leur nom
                    show_names_start_time = time.time() # On enregistre le temps auquel l'affichage des noms des joueurs a commencé
                    show_names = True # On indique que les noms des joueurs doivent être affichés
                    subprocess.run([sys.executable, "game.py", player_names[0], player_names[1]]) # On lance le jeu
                    exit() # On quitte le menu
            elif quit_rect.collidepoint(event.pos): # Si le clic est sur le bouton "Quitter"
                running = False # On arrête la boucle
            for i, input_rect in enumerate(input_rects): # Pour chaque input
                if input_rect.collidepoint(event.pos): # Si le clic est sur l'input
                    current_player = i # On indique que le joueur actuellement en train de saisir est celui de l'input
                    input_active = [False, False] # On désactive la saisie pour les deux joueurs
                    input_active[current_player] = True # On active la saisie pour le joueur actuel

        elif event.type == pygame.KEYDOWN: # Si l'utilisateur appuie sur une touche
            if any(input_active): # Si la saisie est active pour au moins un joueur
                if event.key == pygame.K_SPACE: # Si la touche est la touche espace 
                    current_player = (current_player + 1) % 2 # On passe au joueur suivant
                elif event.key == pygame.K_BACKSPACE: # Si la touche est la touche retour arrière
                    player_names[current_player] = player_names[current_player][:-1] # On supprime le dernier caractère du nom du joueur actuel
                else: # Si la touche est une autre touche
                    player_names[current_player] += event.unicode # On ajoute le caractère de la touche au nom du joueur actuel

    screen.fill((0, 0, 0)) # Fond noir

# ^ AFFICHAGE

    # Affichage du logo
    screen.blit(logo, (265, 0))  # Affichage du logo

    # Affichage du texte des joueurs et des inputs
    for i in range(2): # Pour chaque joueur
        joueur_rect = joueur_surfaces[i].get_rect(topleft=(300, 300 + i * 100)) # Position du texte du joueur
        input_rect = input_rects[i] # Position de l'input du joueur

        # Fond noir pour les inputs, texte blanc et bordure blanche
        pygame.draw.rect(screen, BLACK, input_rect) # Fond noir
        pygame.draw.rect(screen, WHITE, input_rect, 2)  # Bordure blanche
        input_surface = font.render(player_names[i], True, WHITE) # Texte blanc
        screen.blit(joueur_surfaces[i], joueur_rect) # Affichage du texte du joueur
        screen.blit(input_surface, (input_rect.x + 5, input_rect.y + 5)) # Affichage de l'input du joueur

    # Affichage du bouton "Play"
    pygame.draw.rect(screen, button_bg, play_rect) # Fond noir
    pygame.draw.rect(screen, button_border, play_rect, button_border_width) # Bordure blanche
    play_text_x = play_rect.centerx - play_surface.get_width() // 2 # Position du texte
    play_text_y = play_rect.centery - play_surface.get_height() // 2 # Position du texte
    screen.blit(play_surface, (play_text_x, play_text_y)) # Affichage du texte

    # Affichage du bouton "Quitter"
    pygame.draw.rect(screen, button_quit_bg, quit_rect) # Fond rouge
    quit_text_x = quit_rect.centerx - quit_surface.get_width() // 2 # Position du texte
    quit_text_y = quit_rect.centery - quit_surface.get_height() // 2 # Position du texte
    screen.blit(quit_surface, (quit_text_x, quit_text_y)) # Affichage du texte

    # Affichage des noms des joueurs si nécessaire
    if show_names: # Si les noms des joueurs doivent être affichés
        if time.time() - show_names_start_time >= show_names_timer: # Si le délai est écoulé
            show_names = False # On indique que les noms des joueurs ne doivent plus être affichés
        else: # Si le délai n'est pas écoulé
            names_text = f"{player_names[0]} VS {player_names[1]}" # Texte des noms des joueurs
            names_surface = font.render(names_text, True, WHITE) # Surface des noms des joueurs
            screen.blit(names_surface, (260, 300)) # Affichage des noms des joueurs

    pygame.display.flip() # Mise à jour de l'affichage

pygame.quit() # Fermeture de Pygame
