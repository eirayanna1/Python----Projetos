import pygame
import time
import random

# Inicialização do Pygame
pygame.init()

# Definição das cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Tamanho da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Inicialização da tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Jogo da Cobrinha')

# Velocidade inicial da cobra
snake_speed = 15

# Fonte para exibir texto
font = pygame.font.SysFont(None, 40)


class Snake:
    def __init__(self):
        # Inicializa a cobra no centro da tela
        self.body = [(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)]
        # Escolhe uma direção aleatória para começar
        self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])

    def move(self):
        # Move a cobra na direção atual
        x, y = self.body[0]
        if self.direction == "UP":
            y -= 10
        elif self.direction == "DOWN":
            y += 10
        elif self.direction == "LEFT":
            x -= 10
        elif self.direction == "RIGHT":
            x += 10
        self.body.insert(0, (x, y))

    def change_direction(self, direction):
        # Altera a direção da cobra, mas não permite movimentos opostos
        if direction == "UP" and self.direction != "DOWN":
            self.direction = "UP"
        elif direction == "DOWN" and self.direction != "UP":
            self.direction = "DOWN"
        elif direction == "LEFT" and self.direction != "RIGHT":
            self.direction = "LEFT"
        elif direction == "RIGHT" and self.direction != "LEFT":
            self.direction = "RIGHT"

    def draw(self):
        # Desenha a cobra na tela
        for x, y in self.body:
            pygame.draw.rect(screen, GREEN, (x, y, 10, 10))


class Food:
    def __init__(self):
        # Inicializa a comida em uma posição aleatória na tela
        self.x = random.randrange(0, SCREEN_WIDTH - 10, 10)
        self.y = random.randrange(0, SCREEN_HEIGHT - 10, 10)

    def draw(self):
        # Desenha a comida na tela
        pygame.draw.rect(screen, RED, (self.x, self.y, 10, 10))


def game_loop():
    snake = Snake()
    food = Food()
    clock = pygame.time.Clock()

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                # Captura os eventos de tecla e altera a direção da cobra
                if event.key == pygame.K_UP:
                    snake.change_direction("UP")
                elif event.key == pygame.K_DOWN:
                    snake.change_direction("DOWN")
                elif event.key == pygame.K_LEFT:
                    snake.change_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction("RIGHT")

        snake.move()

        if snake.body[0][0] == food.x and snake.body[0][1] == food.y:
            # Se a cabeça da cobra atingir a comida, gera uma nova posição para a comida
            food = Food()

        screen.fill(BLUE)
        snake.draw()
        food.draw()

        if (snake.body[0][0] < 0 or snake.body[0][0] >= SCREEN_WIDTH
                or snake.body[0][1] < 0 or snake.body[0][1] >= SCREEN_HEIGHT
                or len(snake.body) != len(set(snake.body))):
            # Verifica se a cobra atingiu a borda ou a si mesma
            game_over = True

        pygame.display.update()
        clock.tick(snake_speed)

    # Exibe "Game Over" na tela por 2 segundos antes de fechar o jogo
    screen.fill(BLUE)
    message("Game Over!", RED)
    pygame.display.update()
    time.sleep(2)

    pygame.quit()
    quit()


def message(msg, color):
    # Função para exibir mensagens na tela
    text = font.render(msg, True, color)
    screen.blit(text, [SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3])


game_loop()
