import re, os
REPO = '/home/hp/Documents/1_Doc/Projects/ai-research/ai-research-unit'
menu = open(os.path.join(REPO, 'maths.md'), encoding='utf-8').read().splitlines()
start = next(i for i, l in enumerate(menu) if l.startswith('## PART VI'))
cats = [(i, l[3:]) for i, l in enumerate(menu) if i >= start and re.match(r'^## ', l)]
cats.append((len(menu), 'E'))

def cat_blocks(t):
    for k in range(len(cats) - 1):
        a, title = cats[k]; b = cats[k + 1][0]
        if title != t: continue
        out = []; cur = '?'
        for l in menu[a:b]:
            h = re.match(r'^#{3,4} (.*)', l)
            if h: cur = h.group(1)
            m = re.search(r'href="articles_maths/([^"]+)\.html">([^<]+)</a>', l)
            if m: out.append((cur, m.group(1), m.group(2)))
        return out
    return []

for cat in ['Quaternions', 'Quaternioid Algebraic Structures']:
    print('#' * 70); print(cat)
    for cur, slug, label in cat_blocks(cat):
        p = os.path.join(REPO, 'articles_maths', slug + '.md')
        txt = open(p, encoding='utf-8').read()
        words = len(txt.split())
        h2 = [l for l in txt.splitlines() if l.startswith('## ')]
        print(f'{words:5d}w  {slug}')
        print(f'          [{cur}]  H2={len(h2)}: ' + ' | '.join(h[3:] for h in h2[:14]))
