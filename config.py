#encoding=utf-8
port = 8889
md_dir = '.'
html_dir = '.'
plantuml_path = './plantuml.jar'
fs_charset = 'utf-8'
md_charset = 'utf-8'
title = 'zhouzm的笔记'

if __name__ == '__main__':
    import sys
    if sys.argv[1] == 'md_dir':
        print md_dir
    elif sys.argv[1] == 'html_dir':
        print html_dir
