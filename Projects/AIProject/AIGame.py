#I used ChatGPT for this assignment

import pygame
import random

# Initialize pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tetris")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
ORANGE = (255, 165, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Define block size and grid
block_size = 25
grid_width = 10 
grid_height = screen_height // block_size

# Initialize the grid
grid = [[BLACK] * grid_width for _ in range(grid_height)]


# Define shapes and their colors
SHAPES = [
    [[1, 1, 1, 1]],  # I-shape
    [[1, 1], [1, 1]],  # O-shape
    [[1, 1, 1], [0, 1, 0]],  # T-shape
    [[1, 1, 0], [0, 1, 1]],  # Z-shape
    [[0, 1, 1], [1, 1, 0]],  # S-shape
    [[1, 1, 1], [0, 0, 1]],  # J-shape
    [[1, 1, 1], [1, 0, 0]],  # L-shape
]
SHAPE_COLORS = [CYAN, YELLOW, MAGENTA, ORANGE, GREEN, BLUE, RED]

# Define game variables
current_shape = None
current_shape_color = None
current_shape_x = 0
current_shape_y = 0
current_shape_rotation = 0
score = 0

# Generate a new random shape
def generate_shape():
    global current_shape, current_shape_color, current_shape_x, current_shape_y, current_shape_rotation
    current_shape = random.choice(SHAPES)
    current_shape_color = random.choice(SHAPE_COLORS)
    current_shape_x = grid_width // 2 - len(current_shape[0]) // 2
    current_shape_y = 0
    current_shape_rotation = 0

#make sure the shapes are placed in a vlid area
def is_valid_position(shape, x, y, rotation):
    global current_shape
    rotated_shape = rotate_matrix(shape, rotation)
    for row in range(len(rotated_shape)):
        for col in range(len(rotated_shape[row])):
            if (
                rotated_shape[row][col]
                and (
                    x + col < 0
                    or x + col >= grid_width
                    or y + row >= grid_height
                    or y + row < 0
                    or (y + row >= 0 and grid[y + row][x + col] != BLACK)  # Add this condition to handle top boundary
                )
            ):
                return False
    return True

# Place the current shape on the grid
def place_shape():
    for row in range(len(current_shape)):
        for col in range(len(current_shape[0])):
            if current_shape[row][col]:
                grid[current_shape_y + row][current_shape_x + col] = current_shape_color

#Allows rotation
def rotate_shape():
    global current_shape_rotation, current_shape
    current_shape_rotation = (current_shape_rotation + 1) % 4
    current_shape = rotate_matrix(current_shape, current_shape_rotation)

def rotate_matrix(shape, rotation):
    rotated_shape = shape
    for _ in range(rotation):
        rotated_shape = list(zip(*rotated_shape[::-1]))
    return rotated_shape


# Remove completed rows from the grid
def remove_completed_rows():
    global score
    full_rows = []
    for row in range(grid_height):
        if all(cell != BLACK for cell in grid[row]):
            full_rows.append(row)
    for row in full_rows:
        del grid[row]
        grid.insert(0, [BLACK] * grid_width)
        score += 10

# Draw the grid and shapes on the screen
def draw_screen():
    screen.fill(BLACK)
    # Draw the grid
    for row in range(grid_height):
        for col in range(grid_width):
            pygame.draw.rect(screen, grid[row][col], (col * block_size, row * block_size, block_size, block_size), 0)
    
    # Draw the current falling shape
    for row in range(len(current_shape)):
        for col in range(len(current_shape[0])):
            if current_shape[row][col]:
                pygame.draw.rect(screen, current_shape_color,
                                 ((current_shape_x + col) * block_size, (current_shape_y + row) * block_size,
                                  block_size, block_size), 0)

    pygame.display.flip()

# Game loop
clock = pygame.time.Clock()
generate_shape()
running = True
while running:
    clock.tick(5)  # Adjust the speed of the game here

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and is_valid_position(current_shape, current_shape_x - 1, current_shape_y, current_shape_rotation):
                current_shape_x -= 1
            elif event.key == pygame.K_RIGHT and is_valid_position(current_shape, current_shape_x + 1, current_shape_y, current_shape_rotation):
                current_shape_x += 1
            elif event.key == pygame.K_DOWN and is_valid_position(current_shape, current_shape_x, current_shape_y + 1, current_shape_rotation) and current_shape_y + len(current_shape) < grid_height:
                current_shape_y += 1
            elif event.key == pygame.K_SPACE:
                while is_valid_position(current_shape, current_shape_x, current_shape_y + 1, current_shape_rotation) and current_shape_y + len(current_shape) < grid_height:
                    current_shape_y += 1
            # A key for counterclockwise rotation
            elif event.key == pygame.K_a:
                rotate_shape()
                rotate_shape()
                rotate_shape()
            # D key for clockwise rotation
            elif event.key == pygame.K_d:
                rotate_shape()
                rotate_shape()
                rotate_shape()

    if is_valid_position(current_shape, current_shape_x, current_shape_y + 1, current_shape_rotation) and current_shape_y + len(current_shape) < grid_height:
        current_shape_y += 1
    else:
        place_shape()
        remove_completed_rows()
        generate_shape()
        if not is_valid_position(current_shape, current_shape_x, current_shape_y, current_shape_rotation):
            running = False

    draw_screen()

pygame.quit()