import os

# if not (os.path.exists('bin')):
    # os.mkdir('bin');

background = [
    'src/modules/background/bg.css',
    'src/modules/background/bg-no-dark.css',
]

border = [
    'src/modules/border/border-size.css',
    'src/modules/border/border-color.css',
    'src/modules/border/border-radius.css',
    'src/modules/border/border-style.css'
]

cursor = [
    'src/modules/cursor/cursor.css'
]

elements_html = [
    'src/modules/elements-html/button/button.css',
    'src/modules/elements-html/input.css',
    'src/modules/elements-html/link.css',
    'src/modules/elements-html/scroll-bar.css',
]

flex_box = [
    'src/modules/flex-box/align.css',
    'src/modules/flex-box/display.css',
    'src/modules/flex-box/flex.css',
    'src/modules/flex-box/gap.css',
    'src/modules/flex-box/justify.css'
]


layout = [
   'src/modules/layout/position.css',
   'src/modules/layout/sides/bottom.css',
   'src/modules/layout/sides/left.css',
   'src/modules/layout/sides/right.css',
   'src/modules/layout/sides/top.css',
]

overflow = [
    'src/modules/overflow/overflow.css'
]

sizes = [
    'src/modules/sizes/height.css',
    'src/modules/sizes/width.css',
]

spacing = [
    'src/modules/spacing/margin.css',
    'src/modules/spacing/padding.css'
]

transition = [
    'src/modules/transition/ease/ease.css',
    'src/modules/transition/ease/ease-in.css',
    'src/modules/transition/ease/ease-in-out.css',
    'src/modules/transition/ease/ease-out.css'
]

typography = [
    'src/modules/typography/color.css',
    'src/modules/typography/color-no-dark.css',
    'src/modules/typography/font-decoration.css',
    'src/modules/typography/font-size.css',
    'src/modules/typography/font-transform.css',
    'src/modules/typography/font-weight.css'
]

#modules = [background, border, cursor]

directories = ['src/art-main.css'] + background + border + cursor + elements_html + flex_box + layout + overflow + sizes + spacing + transition + typography
    
file_content = [];

for file in directories: 
    with open(file, 'r') as css_file:
        file_content.append( css_file.read() );

    print(file)

#ou bin/art.css

with open('art.css', 'w', encoding='utf-8') as file:
    file_content_as_string = ''.join(file_content);
    file.write(''.join(file_content_as_string));
