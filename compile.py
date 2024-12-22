import os

# if not (os.path.exists('bin')):
    # os.mkdir('bin');

dir = [
    'src/main.css',
    'src/modules/background/bg-color.css',
    'src/modules/font/ft-color.css',
    'src/modules/hovers/bg-hover.css',
    'src/modules/hovers/ft-hover.css'
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
