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

cursor = [
    'src/modules/cursor/cursor.css'
]

border = [
    'src/modules/border/b-size.css',
    'src/modules/border/b-color.css',
    'src/modules/border/b-hover.css',
    'src/modules/border/b-radius.css',
    'src/modules/border/b-style.css'
]

no_dark = [
    'src/modules/no-dark/bg-no-dark.css',
    'src/modules/no-dark/font-no-dark.css',
    'src/modules/no-dark/hover-no-dark.css'
]

padding = [
    'src/modules/padding/padding.css'
]

margin = [
    'src/modules/margin/margin.css'
]


directories = ['src/art-main.css'] + background + font + cursor + border + no_dark + padding + margin
    
file_content = [];

for file in directories: 
    with open(file, 'r') as css_file:
        file_content.append( css_file.read() );

    print(file)

#ou bin/art.css

with open('art.css', 'w', encoding='utf-8') as file:
    file_content_as_string = ''.join(file_content);
    file.write(''.join(file_content_as_string));
