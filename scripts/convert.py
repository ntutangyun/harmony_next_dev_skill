# Convert Huawei docs-portal API HTML to the skill's offline page markdown format:
#   # <title>
#   _Source: <url>_
#   <body: blocks separated by blank lines; code/table blocks keep internal newlines>
#   ## Code blocks   (fenced copies of every <pre>)
import re
from bs4 import BeautifulSoup, NavigableString, Tag

NBSP = ' '


def _inline_text(el):
    t = el.get_text()
    t = t.replace(NBSP, ' ')
    t = re.sub(r'\s+', ' ', t).strip()
    return t


def convert(html, title, source_url):
    soup = BeautifulSoup(html, 'lxml')
    for bad in soup.find_all(['script', 'style', 'img']):
        bad.decompose()

    code_blocks = []
    blocks = []

    def add_block(text):
        if text and text.strip():
            blocks.append(text)

    def handle_pre(pre):
        code = pre.get_text().replace(NBSP, ' ')
        code = '\n'.join(ln.rstrip() for ln in code.split('\n')).strip('\n')
        if code:
            code_blocks.append(code)
            add_block(code)

    def handle_table(table):
        rows = []
        for tr in table.find_all('tr'):
            cells = tr.find_all(['th', 'td'])
            if cells:
                rows.append('\t'.join(_inline_text(c) for c in cells))
        add_block('\n'.join(rows))

    NOTE_LABELS = {'note': '说明', 'notice': '须知', 'caution': '注意',
                   'warning': '警告', 'danger': '危险'}

    def walk(node):
        for child in node.children:
            if not isinstance(child, Tag):
                continue
            name = child.name
            classes = child.get('class') or []
            note_label = next((NOTE_LABELS[c] for c in classes if c in NOTE_LABELS), None)
            if name == 'div' and note_label:
                add_block(note_label)
                walk(child)
                continue
            if name == 'pre':
                handle_pre(child)
            elif name == 'table':
                handle_table(child)
            elif name == 'h1' and _inline_text(child) == title:
                continue  # duplicated by our own "# title" header
            elif name in ('p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'dt', 'caption'):
                add_block(_inline_text(child))
            elif name == 'li' or name == 'dd':
                nested = child.find(['pre', 'table', 'ul', 'ol', 'p'])
                if nested:
                    walk(child)
                else:
                    add_block(_inline_text(child))
            else:
                walk(child)

    body = soup.body or soup
    walk(body)

    out = ['# ' + title, '', f'_Source: {source_url}_', '']
    for b in blocks:
        out.append(b)
        out.append('')
    if code_blocks:
        out.append('## Code blocks')
        out.append('')
        for i, code in enumerate(code_blocks, 1):
            out.append(f'### Code block {i}')
            out.append('')
            out.append('```')
            out.append(code)
            out.append('```')
            out.append('')
    return '\n'.join(out).rstrip('\n') + '\n'


if __name__ == '__main__':
    import sys
    html = open(sys.argv[1], encoding='utf-8').read()
    md = convert(html, sys.argv[2], sys.argv[3])
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stdout.write(md)
