import os

""" 
- abrir o diretorio
- ler o arquivo
- abrir o /bin
- escrever ele no arquivo art.css
"""

if os.path.exists('bin/art.css'):
    os.remove('bin/art.css');

dir = [
    'main.css',
    'modules/background/bg-color.css',
    'modules/text/txt.css'
    ]
    
content = [];
""" 
for file in dir: 
    with open(file, 'r') as css_file:
        content.append( css_file.read() );

    print(file)

with open('art-css/art.css', 'w', encoding='utf-8') as file:
    content_as_string = ''.join(content)
    file.write(''.join(content_as_string))
 """