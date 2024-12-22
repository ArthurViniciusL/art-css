import os

if (os.path.exists('bin/art.css')):
    os.remove('bin/art.css');

else:
    os.mkdir('bin')

dir = [
    'src/main.css',
    'src/modules/background/bg-color.css',
    'src/modules/text/txt.css'
    ]
    
content = [];

for file in dir: 
    with open(file, 'r') as css_file:
        content.append( css_file.read() );

    print(file)

with open('bin/art.css', 'w', encoding='utf-8') as file:
    content_as_string = ''.join(content);
    file.write(''.join(content_as_string));
