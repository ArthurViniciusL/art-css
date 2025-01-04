import os

# if not (os.path.exists('bin')):
    # os.mkdir('bin');

background = [
    'src/modules/background/bg-color.css',
    'src/modules/background/bg-hover.css'
]

font = [
    'src/modules/font/font-color.css',
    'src/modules/font/font-decoration.css',
    'src/modules/font/font-hover.css',
    'src/modules/font/font-size.css',
    'src/modules/font/font-style.css'
]

border = [
    'src/modules/border/border-size.css',
    'src/modules/border/border-color.css',
    'src/modules/border/border-hover.css',
    'src/modules/border/border-radius.css',
    'src/modules/border/border-style.css'
]

buttons = [
    'src/modules/button/button.css'
]

lines = [
    'src/modules/lines/lines.css'
]

no_dark = [
    'src/modules/no-dark/bg.css',
    'src/modules/no-dark/font.css'
]

padding = [
    'src/modules/padding/padding.css'
]

directories = ['src/art-main.css'] + background + font + border + buttons + lines + no_dark + padding
    
file_content = [];

for file in directories: 
    with open(file, 'r') as css_file:
        file_content.append( css_file.read() );

    print(file)

#ou bin/art.css

with open('art.css', 'w', encoding='utf-8') as file:
    file_content_as_string = ''.join(file_content);
    file.write(''.join(file_content_as_string));
