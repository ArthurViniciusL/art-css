import os

# if not (os.path.exists('bin')):
    # os.mkdir('bin');

background = [
    'src/modules/background/bg.css',
]

border = [
    'src/modules/border/b-size.css',
    'src/modules/border/b-color.css',
    'src/modules/border/b-hover.css',
    'src/modules/border/b-radius.css',
    'src/modules/border/b-style.css'
]

cursor = [
    'src/modules/cursor/cursor.css'
]

direction = [
    'src/modules/direction/bottom.css',
    'src/modules/direction/left.css',
    'src/modules/direction/right.css',
    'src/modules/direction/top.css',
]

views = [
    'src/modules/views/height.css',
    'src/modules/views/width.css',    
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

margin = [
    'src/modules/margin/margin.css'
]

no_dark = [
    'src/modules/no-dark/bg-no-dark.css',
    'src/modules/no-dark/font-no-dark.css',
    'src/modules/no-dark/hover-no-dark.css'
]

overflow = [
    'src/modules/overflow/overflow.css'
]

padding = [
    'src/modules/padding/padding.css'
]


position = [
    'src/modules/position/position.css'
]

transition = [
    'src/modules/transition/ease-in-out.css',
    'src/modules/transition/ease-in.css',
    'src/modules/transition/ease-out.css',
    'src/modules/transition/ease.css',
]

typography = [
    'src/modules/typography/color.css',
    'src/modules/typography/font-decoration.css',
    'src/modules/typography/font-size.css',
    'src/modules/typography/font-transform.css',
    'src/modules/typography/font-weight.css'
]

modules = [background]

directories = ['src/art-main.css'] + background + border + cursor + direction + views + elements_html + flex_box + typography + margin + no_dark + overflow + padding + position + transition
    
file_content = [];

for file in directories: 
    with open(file, 'r') as css_file:
        file_content.append( css_file.read() );

    print(file)

#ou bin/art.css

with open('art.css', 'w', encoding='utf-8') as file:
    file_content_as_string = ''.join(file_content);
    file.write(''.join(file_content_as_string));
