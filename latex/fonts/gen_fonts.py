# create a XeTex document which lists all available TrueType font
import subprocess

# sub to print out tags
def font_tag(tag, font_name):
    print('\\IfFontExistsTF{{{}}}{{'.format(font_name))
    print('\t\\{}{{{}}}'.format(tag, font_name))
    print('\t\\textbf{{{}}}: The quick brown fox jumps over the lazy dog.}}'.format(font_name))    
    print('\t{}\n')


# the command to get all fonts is fc-list which comes with the Texlive package
result = subprocess.run(['fc-list', ':lang=fr', 'family'], stdout=subprocess.PIPE)

# split
font_list = sorted(result.stdout.decode('utf-8').strip().split('\n'))

# remove this font
font_list.remove('EB Garamond 12 All SC')

# print doc header
print(r"""
\documentclass[]{article}
\usepackage{fontspec}
%\usepackage{xltxtra,fontspec,xunicode}
\usepackage[left=1.9cm,top=2cm,bottom=2.5cm,right=1.9cm,nohead,nofoot]{geometry}
%\defaultfontfeatures{Scale=MatchLowercase}
\title{Fonttest}  
 
\begin{document} 
""")

# sort and reduce to unique name
for font in font_list:
    # do not select if font name contains a comma
    if ',' in font: 
        continue

    # chose right formatting tag
    if 'Sans' in font:
        font_tag('setsansfont', font)
    elif 'Mono'in font:
        font_tag('setmonofont', font)
    else:
        font_tag('setmainfont', font)
# end doc
print("""\end{document}""")