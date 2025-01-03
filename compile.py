import os

# if not (os.path.exists('bin')):
    # os.mkdir('bin');

dir = [
    'src/art-main.css',
    'src/modules/background/bg-color.css',
    'src/modules/border/boder-size.css',
    'src/modules/border/border-color.css',
    'src/modules/border/border-radius.css',
    'src/modules/border/border-styles.css',
    'src/modules/button/button.css',
    'src/modules/cursor/cursor.css',
    'src/modules/font/font-color.css',
    'src/modules/font/font-decoration.css',
    'src/modules/font/font-size.css',
    'src/modules/font/font-style.css',
    'src/modules/hovers/bg-hover.css',
    'src/modules/hovers/border-hover.css',
    'src/modules/hovers/font-hover.css',
    'src/modules/lines/lines.css',
    'src/modules/padding/padding.css'
    ]
    
file_content = [];

for file in dir: 
    with open(file, 'r') as css_file:
        file_content.append( css_file.read() );

    print(file)

#ou bin/art.css

with open('art.css', 'w', encoding='utf-8') as file:
    file_content_as_string = ''.join(file_content);
    file.write(''.join(file_content_as_string));
