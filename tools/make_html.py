#encoding=utf-8
import re
import sys

sys.path.append('./external/python-markdown')
import markdown

def make_html(src, css):
    style = css.endswith('.css') and '<link rel="stylesheet" href="%s" />' % css \
            or '<style>%s</style>' % css
    converter = markdown.Markdown(
            extensions=['tables', 'fenced_code', 'toc', 'codehilite'],
            extension_configs={
                'codehilite':
                {
                    'linenums': False,
                    'noclasses': True,
                    'pygments_style': 'native',
                }
            })
    title = ''
    match = re.search(r'#.*', src)
    if match:
        title = match.group(0).strip('# ')
    
    body = converter.convert(src)
    return '''<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>%s</title>
    %s
</head>
<body>
%s
</body>
</html>
''' % (title.encode('utf-8'), style, body.encode('utf-8'))


