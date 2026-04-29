import pygame
import random
import sys

pygame.init()

# Window settings
WIDTH = 600
HEIGHT = 600
CELL_SIZE = 12  # Changed from 20 to 12 (smaller snake)

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DARK_GREEN = (0, 150, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

class Snake:
    def __init__(self):
        # Start in the middle
        self.body = [[WIDTH//2, HEIGHT//2]]
        self.direction = "RIGHT"
        self.grow = False
    
    def move(self):
        head = self.body[0].copy()
        
        if self.direction == "RIGHT":
            head[0] += CELL_SIZE
        elif self.direction == "LEFT":
            head[0] -= CELL_SIZE
        elif self.direction == "UP":
            head[1] -= CELL_SIZE
        elif self.direction == "DOWN":
            head[1] += CELL_SIZE
        
        self.body.insert(0, head)
        
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
    
    def change_direction(self, new_dir):
        if new_dir == "RIGHT" and self.direction != "LEFT":
            self.direction = new_dir
        elif new_dir == "LEFT" and self.direction != "RIGHT":
            self.direction = new_dir
        elif new_dir == "UP" and self.direction != "DOWN":
            self.direction = new_dir
        elif new_dir == "DOWN" and self.direction != "UP":
            self.direction = new_dir
    
    def check_self_collision(self):
        head = self.body[0]
        return head in self.body[1:]
    
    def check_wall_collision(self):
        head = self.body[0]
        if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
            return True
        return False
    
    def eat_food(self, food_pos):
        if self.body[0] == food_pos:
            self.grow = True
            return True
        return False
    
    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, DARK_GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE), 1)

class Food:
    def __init__(self, snake_body):
        self.position = [0, 0]
        self.randomize_position(snake_body)
    
    def randomize_position(self, snake_body):
        while True:
            # Calculate max grid cells
            max_x = WIDTH // CELL_SIZE
            max_y = HEIGHT // CELL_SIZE
            
            x = random.randint(0, max_x - 1) * CELL_SIZE
            y = random.randint(0, max_y - 1) * CELL_SIZE
            new_pos = [x, y]
            
            if new_pos not in snake_body:
                self.position = new_pos
                break
    
    def draw(self):
        pygame.draw.rect(screen, RED, (self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))

def show_score_and_level(score, level):
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(level_text, (WIDTH - 100, 10))

def game_over_screen(score, level):
    screen.fill(BLACK)
    
    game_over_text = font.render("GAME OVER", True, RED)
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    restart_text = font.render("Press SPACE to restart | ESC to quit", True, WHITE)
    
    screen.blit(game_over_text, (WIDTH//2 - 70, HEIGHT//2 - 60))
    screen.blit(score_text, (WIDTH//2 - 50, HEIGHT//2 - 20))
    screen.blit(level_text, (WIDTH//2 - 50, HEIGHT//2 + 20))
    screen.blit(restart_text, (WIDTH//2 - 220, HEIGHT//2 + 80))
    
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
                if event.key == pygame.K_ESCAPE:
                    return False

def main():
    running = True
    
    while running:
        snake = Snake()
        food = Food(snake.body)
        score = 0
        level = 1
        foods_eaten = 0
        speed = 8
        
        game_active = True
        
        while game_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        snake.change_direction("RIGHT")
                    elif event.key == pygame.K_LEFT:
                        snake.change_direction("LEFT")
                    elif event.key == pygame.K_UP:
                        snake.change_direction("UP")
                    elif event.key == pygame.K_DOWN:
                        snake.change_direction("DOWN")
            
            snake.move()
            
            if snake.check_wall_collision() or snake.check_self_collision():
                game_active = False
                break
            
            if snake.eat_food(food.position):
                score += 1
                foods_eaten += 1
                food.randomize_position(snake.body)
                
                # Level up every 3 foods
                if foods_eaten >= 3:
                    level += 1
                    speed += 2
                    foods_eaten = 0
                    print(f"Level {level}! Speed: {speed}")
            
            screen.fill(BLACK)
            snake.draw()
            food.draw()
            show_score_and_level(score, level)
            
            pygame.display.flip()
            clock.tick(speed)
        
        running = game_over_screen(score, level)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()