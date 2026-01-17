from PIL import Image, ImageDraw, ImageFont
import os

# Define face colors (traditional Rubik's cube colors)
faces = {
    'front': (0, 255, 0),    # Green
    'back': (0, 0, 255),     # Blue
    'left': (255, 165, 0),   # Orange
    'right': (255, 0, 0),    # Red
    'up': (255, 255, 255),   # White
    'down': (255, 255, 0)    # Yellow
}

# Create textures directory if it doesn't exist
textures_dir = 'assets/textures'
os.makedirs(textures_dir, exist_ok=True)

# Create each face texture
size = 512
for face_name, color in faces.items():
    # Create a new image with the face color
    img = Image.new('RGB', (size, size), color=color)
    draw = ImageDraw.Draw(img)
    
    # Try to add text label
    try:
        font = ImageFont.truetype("arial.ttf", 60)
    except:
        try:
            font = ImageFont.truetype("Arial.ttf", 60)
        except:
            font = ImageFont.load_default()
    
    # Draw face name - centered both horizontally and vertically
    text = face_name.upper()
    position = (size // 2, size // 2)
    
    # Draw black outline for better visibility
    outline_color = (0, 0, 0) if face_name != 'down' else (100, 100, 100)
    for adj_x in [-2, -1, 0, 1, 2]:
        for adj_y in [-2, -1, 0, 1, 2]:
            draw.text((position[0] + adj_x, position[1] + adj_y), text, font=font, fill=outline_color, anchor='mm')
    
    # Draw the main text
    text_color = (0, 0, 0) if face_name == 'up' or face_name == 'down' else (255, 255, 255)
    draw.text(position, text, font=font, fill=text_color, anchor='mm')
    
    # Save the image
    filename = os.path.join(textures_dir, f'face_{face_name}.png')
    img.save(filename)
    print(f'Created {filename}')

print('\nAll face textures created successfully!')
print('You can now replace these with your own custom images.')
