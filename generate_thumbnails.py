#!/usr/bin/env python3
from PIL import Image, ImageDraw
import os

articles = [
    {'title': 'WordPress Shortcode', 'color': '#FF6B6B', 'folder': 'add-postlink'},
    {'title': 'Broadband', 'color': '#4ECDC4', 'folder': 'broadband-homerooter'},
    {'title': 'Hugo Blog Start', 'color': '#45B7D1', 'folder': 'blog-start-rs'},
    {'title': 'Hugo Blog Ops', 'color': '#96CEB4', 'folder': 'blog-start-rs-2'},
    {'title': 'Hugo Custom', 'color': '#FFEAA7', 'folder': 'blog-start-rs-3'}
]

base_path = r'C:\Users\hreik_000\quickstart\content\posts'

for article in articles:
    img = Image.new('RGB', (1200, 630), color=article['color'])
    draw = ImageDraw.Draw(img)
    
    text = article['title']
    
    # フォントサイズを設定
    font_size = 70
    try:
        from PIL import ImageFont
        font = ImageFont.truetype('C:\\Windows\\Fonts\\meiryo.ttc', font_size)
    except:
        font = ImageFont.load_default()
    
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (1200 - text_width) // 2
    y = (630 - text_height) // 2
    
    draw.text((x, y), text, fill='white', font=font)
    
    folder_path = os.path.join(base_path, article['folder'])
    file_path = os.path.join(folder_path, 'thumbnail.webp')
    img.save(file_path, 'WEBP', quality=95)
    print(f'✓ {article["folder"]}/thumbnail.webp を生成')

print('✅ すべての画像を生成完了')
