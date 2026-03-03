import pygame
import sys
import requests
from datetime import datetime

pygame.init()

# ^ Ajout des polices
font20 = pygame.font.Font('freesansbold.ttf', 20)
font48 = pygame.font.Font('freesansbold.ttf', 48)

# ^ Ajout des couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# ^ Fenetre
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# ^ Horloge
clock = pygame.time.Clock()
FPS = 30

# class Striker pour les joueurs
class Striker:
    def __init__(self, posx, posy, width, height, speed, color): # Constructeur
        self.posx = posx # Position x
        self.posy = posy # Position y
        self.width = width # Largeur
        self.height = height # Hauteur
        self.speed = speed # Vitesse
        self.color = color # Couleur
        self.geekRect = pygame.Rect(posx, posy, width, height) # Rectangle pour le joueur
        self.geek = pygame.draw.rect(screen, self.color, self.geekRect) # Dessin du joueur

    def display(self): # Fonction pour afficher le joueur
        self.geek = pygame.draw.rect(screen, self.color, self.geekRect) # Dessin du joueur

    def update(self, yFac): # Fonction pour mettre à jour la position du joueur
        self.posy = self.posy + self.speed * yFac # Mise à jour de la position y

        if self.posy <= 0: # Si le joueur touche le haut de l'écran
            self.posy = 0  # La position y est égale à 0
        elif self.posy + self.height >= HEIGHT: # Si le joueur touche le bas de l'écran
            self.posy = HEIGHT - self.height # La position y est égale à la hauteur de l'écran moins la hauteur du joueur

        self.geekRect = (self.posx, self.posy, self.width, self.height) # Mise à jour du rectangle du joueur

    def displayScore(self, text, score, x, y, color): # Fonction pour afficher le score
        text = font20.render(text + str(score), True, color) # Texte du score
        textRect = text.get_rect() # Rectangle du texte
        textRect.center = (x, y) # Position du texte

        screen.blit(text, textRect) # Affichage du texte

    def getRect(self): # Fonction pour récupérer le rectangle du joueur
        return self.geekRect # Retourne le rectangle du joueur

# Ball class
class Ball: # Classe pour la balle
    def __init__(self, posx, posy, radius, speed, color): # Constructeur
        self.posx = posx # Position x
        self.posy = posy # Position y
        self.radius = radius # Rayon
        self.speed = speed # Vitesse
        self.color = color # Couleur
        self.xFac = 1 # Facteur de déplacement x
        self.yFac = -1 # Facteur de déplacement y
        self.ball = pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.radius) # Dessin de la balle
        self.firstTime = 1 # Indique si c'est la première fois que la balle touche un joueur

    def display(self): # Fonction pour afficher la balle
        self.ball = pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.radius) # Dessin de la balle

    def update(self): # Fonction pour mettre à jour la position de la balle
        self.posx += self.speed * self.xFac # Mise à jour de la position x
        self.posy += self.speed * self.yFac # Mise à jour de la position y

        if self.posy <= 0 or self.posy >= HEIGHT: # Si la balle touche le haut ou le bas de l'écran
            self.yFac *= -1 # Inversion du facteur de déplacement y

        if self.posx <= 0 and self.firstTime: # Si la balle touche le côté gauche de l'écran
            self.firstTime = 0 # La balle a déjà touché un joueur
            return 1 # Retourne 1
        elif self.posx >= WIDTH and self.firstTime: # Si la balle touche le côté droit de l'écran
            self.firstTime = 0 # La balle a déjà touché un joueur
            return -1 # Retourne -1
        else: # Si la balle ne touche pas un joueur
            return 0 # Retourne 0

    def reset(self): # Fonction pour réinitialiser la balle
        self.posx = WIDTH // 2 # La position x est égale à la moitié de la largeur de l'écran
        self.posy = HEIGHT // 2 # La position y est égale à la moitié de la hauteur de l'écran
        self.xFac *= -1 # Inversion du facteur de déplacement x
        self.firstTime = 1 # La balle n'a pas encore touché un joueur

    def hit(self): # Fonction pour faire rebondir la balle
        self.xFac *= -1 # Inversion du facteur de déplacement x

    def getRect(self): # Fonction pour récupérer le rectangle de la balle
        return self.ball # Retourne le rectangle de la balle

# Fonction pour envoyer les données du joueur gagnant à l'API
def send_winner_data_to_api(player_name, score): 
    api_url = "http://127.0.0.1:8000/save_result/"  
    result_data = {
        "player_name": player_name,
        "score": score,
    }
    try: 
        response = requests.post(api_url, json=result_data) # Envoi des données à l'API
        if response.status_code == 200: # Si la requête a réussi
            print("Résultat de la partie enregistré avec succès dans l'API") 
        else: # Si la requête a échoué
            print("Erreur lors de l'enregistrement du résultat dans l'API")
    except Exception as e: # Si une erreur s'est produite
        print("Erreur lors de la connexion à l'API :", str(e))

# Fonction principale
'''
    Fonction principale pour lancer le jeu
    Paramètres:
        player1_name: Nom du joueur 1
        player2_name: Nom du joueur 2
'''
def main(player1_name, player2_name):
    running = True

    geek1 = Striker(20, 0, 10, 100, 10, GREEN) # Création du joueur 1
    geek2 = Striker(WIDTH-30, 0, 10, 100, 10, GREEN) # Création du joueur 2
    ball = Ball(WIDTH//2, HEIGHT//2, 7, 7, WHITE) # Création de la balle

    listOfGeeks = [geek1, geek2] # Liste des joueurs

    geek1Score, geek2Score = 0, 0 # Scores des joueurs
    geek1YFac, geek2YFac = 0, 0 # Facteurs de déplacement des joueurs

    max_score = 1 # Score maximum pour gagner
    winner = None # Nom du gagnant
    game_over = False # Indique si la partie est terminée

    # Ajout du compte à rebours pour la fermeture
    countdown_start_time = None

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if not game_over:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        geek2YFac = -1
                    if event.key == pygame.K_DOWN:
                        geek2YFac = 1
                    if event.key == pygame.K_w:
                        geek1YFac = -1
                    if event.key == pygame.K_s:
                        geek1YFac = 1
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        geek2YFac = 0
                    if event.key == pygame.K_w or event.key == pygame.K_s:
                        geek1YFac = 0
        # ^ Mise à jour des scores et de la balle
        if not game_over: # Si la partie n'est pas terminée
            for geek in listOfGeeks: # Pour chaque joueur
                if pygame.Rect.colliderect(ball.getRect(), geek.getRect()): # Si la balle touche un joueur
                    ball.hit() # La balle rebondit

            geek1.update(geek1YFac)
            geek2.update(geek2YFac)
            point = ball.update()

            if point == -1: # Si le joueur 1 marque
                geek1Score += 1 # Ajout d'un point au joueur 1
            elif point == 1: # Si le joueur 2 marque
                geek2Score += 1 # Ajout d'un point au joueur 2

            if geek1Score >= max_score: # Si le joueur 1 a atteint le score maximum
                winner = player1_name # Le gagnant est le joueur 1
                game_over = True # La partie est terminée
                countdown_start_time = pygame.time.get_ticks() # Début du compte à rebours
                # Appel de la fonction pour enregistrer le résultat du joueur gagnant dans l'API
                send_winner_data_to_api(winner, geek1Score) 
            elif geek2Score >= max_score: # Si le joueur 2 a atteint le score maximum
                winner = player2_name # Le gagnant est le joueur 2
                game_over = True # La partie est terminée
                countdown_start_time = pygame.time.get_ticks() # Début du compte à rebours
                # Appel de la fonction pour enregistrer le résultat du joueur gagnant dans l'API
                send_winner_data_to_api(winner, geek2Score)
            # ^ Réinitialisation de la balle
            if point: # Si un joueur a marqué
                ball.reset() # Réinitialisation de la balle
        # ^ Affichage des scores et de la balle
        geek1.display()
        geek2.display()
        ball.display()

        geek1.displayScore(player1_name + " : ", geek1Score, 100, 20, WHITE)
        geek2.displayScore(player2_name + " : ", geek2Score, WIDTH-100, 20, WHITE)

        # Afficher le nom du gagnant et le compte à rebours
        if game_over:
            if winner:
                winner_text = font48.render(f"{winner} a gagné!", True, WHITE)
                winner_text_rect = winner_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                screen.blit(winner_text, winner_text_rect)

            current_time = pygame.time.get_ticks()
            if countdown_start_time is not None: # Si le compte à rebours a commencé
                countdown_duration = 5000  # 5 secondes en millisecondes
                elapsed_time = current_time - countdown_start_time # Temps écoulé en millisecondes temps immediat - temps de depart
                remaining_time = max(0, countdown_duration - elapsed_time) 
                seconds_remaining = remaining_time // 1000 + 1 # Temps restant en secondes est egale au temps restant en millisecondes divisé par 1000 + 1 pour arrondir
                countdown_text = font48.render(f"Fermeture dans {seconds_remaining}...", True, WHITE) # Texte du compte à rebours
                countdown_text_rect = countdown_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60)) # Position du texte du compte à rebours
                screen.blit(countdown_text, countdown_text_rect) # Affichage du texte du compte à rebours

                if remaining_time <= 0:
                    running = False

        pygame.display.update() # Mise à jour de l'affichage
        clock.tick(FPS) # Mise à jour de l'horloge

# ^ Recuperation des noms des joueurs
if __name__ == "__main__": # Si le fichier est executé directement
    if len(sys.argv) == 3: # Si le nombre d'arguments est égal à 3
        player1_name = sys.argv[1] # Le nom du joueur 1 est le premier argument
        player2_name = sys.argv[2] # Le nom du joueur 2 est le deuxième argument
        main(player1_name, player2_name) # Appel de la fonction principale
    else:
        print("Erreur") # Affichage du message d'erreur
    pygame.quit() # Fermeture de pygame
