from PIL import Image, ImageDraw, ImageFont
import os

# Define face colors (traditional Rubik's cube colors)
faces = {
    'left': (255, 165, 0),   # Orange
    'front': (0, 255, 0),    # Green
    'right': (255, 0, 0),    # Red
    'back': (0, 0, 255),     # Blue
    'down': (255, 255, 0),   # Yellow
    'up': (255, 255, 255),   # White
}

# Create texture atlas - 4 columns × 2 rows
# Layout: [Left, Front, Right, Empty]
#         [Back, Down,  Up,    Empty]
atlas_width = 2048  # 4 columns × 512
atlas_height = 1024  # 2 rows × 512
tile_size = 512

# Initialize with black background
atlas = Image.new('RGB', (atlas_width, atlas_height), color=(0, 0, 0))

# Define positions in atlas (column, row)
# Corrected mapping based on what appears where
positions = {
    'up': (0, 0),      # was left
    'front': (1, 0),   # stays same
    'left': (2, 0),    # was right
    'down': (0, 1),    # was back
    'back': (1, 1),    # was down
    'right': (2, 1),   # was up
    # Positions (3,0) and (3,1) remain black (unused)
}

# Try to load font
try:
    font = ImageFont.truetype("arial.ttf", 80)
except:
    try:
        font = ImageFont.truetype("Arial.ttf", 80)
    except:
        font = ImageFont.load_default()

for face_name, (col, row) in positions.items():
    # Create tile
    tile = Image.new('RGB', (tile_size, tile_size), color=faces[face_name])
    draw = ImageDraw.Draw(tile)
    
    # Draw face name centered
    text = face_name.upper()
    position = (tile_size // 2, tile_size // 2)
    
    # Draw outline
    outline_color = (0, 0, 0) if face_name in ['up', 'down'] else (100, 100, 100)
    for adj_x in [-2, -1, 0, 1, 2]:
        for adj_y in [-2, -1, 0, 1, 2]:
            draw.text((position[0] + adj_x, position[1] + adj_y), text, font=font, fill=outline_color, anchor='mm')
    
    # Draw main text
    text_color = (0, 0, 0) if face_name in ['up', 'down'] else (255, 255, 255)
    draw.text(position, text, font=font, fill=text_color, anchor='mm')
    
    # Paste tile into atlas
    x = col * tile_size
    y = row * tile_size
    atlas.paste(tile, (x, y))

# Save atlas
output_path = 'assets/textures/cube_atlas.png'
atlas.save(output_path)
print(f'Created texture atlas: {output_path}')
print('Atlas layout (4×2):')
print('  [Up]    [Front] [Left]  [Empty]')
print('  [Down]  [Back]  [Right] [Empty]')
