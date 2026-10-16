import os
REPO = '/home/hp/Documents/1_Doc/Projects/ai-research/ai-research-unit'
SUBS = [
    ('Quaternion $\\mathbb{R}$ Space', 'Quaternioid $\\mathbb{R}$ Space'),
    ('Quaternion Real Space', 'Quaternioid Real Space'),
]
n = {}
for d in ('articles_maths', 'articles_physics'):
    dd = os.path.join(REPO, d)
    for f in os.listdir(dd):
        if not f.endswith('.md'):
            continue
        p = os.path.join(dd, f)
        t = open(p, encoding='utf-8').read()
        o = t
        for a, b in SUBS:
            c = t.count(a)
            if c:
                n[a] = n.get(a, 0) + c
                t = t.replace(a, b)
        if t != o:
            open(p, 'w', encoding='utf-8').write(t)
for f in ('maths.md', 'physics.md'):
    p = os.path.join(REPO, f)
    t = open(p, encoding='utf-8').read()
    o = t
    for a, b in SUBS:
        c = t.count(a)
        if c:
            n[a] = n.get(a, 0) + c
            t = t.replace(a, b)
    if t != o:
        open(p, 'w', encoding='utf-8').write(t)
print(n)
