import re, os
REPO = '/home/hp/Documents/1_Doc/Projects/ai-research/ai-research-unit'
menu = open(os.path.join(REPO, 'maths.md'), encoding='utf-8').read().splitlines()
start = next(i for i, l in enumerate(menu) if l.startswith('## PART VI'))
cats = [(i, l[3:]) for i, l in enumerate(menu) if i >= start and re.match(r'^## ', l)]
cats.append((len(menu), 'E'))

def entries(t):
    for k in range(len(cats) - 1):
        a, title = cats[k]; b = cats[k + 1][0]
        if title != t: continue
        out = []
        for l in menu[a:b]:
            m = re.search(r'href="articles_maths/([^"]+)\.html">([^<]+)</a>', l)
            if m: out.append((m.group(1), m.group(2)))
        return out
    return []

def headings(t):
    for k in range(len(cats) - 1):
        a, title = cats[k]; b = cats[k + 1][0]
        if title != t: continue
        return [(i + a + 1, l) for i, l in enumerate(menu[a:b]) if re.match(r'^#{3,4} ', l)]
    return []

Q = entries('Quaternions'); QA = entries('Quaternioid Algebraic Structures'); SQ = entries('Split-Quaternions')
qa = set(s for s, _ in QA)
allslugs = set()
for f in os.listdir(os.path.join(REPO, 'articles_maths')):
    if f.endswith('.md'): allslugs.add(f[:-3])

LINK = re.compile(r'articles_maths/([A-Za-z0-9_\-]+)\.(?:md|html)')

print('=== headings of Quaternioid ===')
for ln, h in headings('Quaternioid Algebraic Structures'): print(ln, h)

print('\n=== Quaternions -> quaternioid links (any form) ===')
for s, label in Q:
    p = os.path.join(REPO, 'articles_maths', s + '.md')
    txt = open(p, encoding='utf-8').read()
    refs = sorted(set(LINK.findall(txt)) & qa)
    if refs: print(f'{s}\n    -> ' + '\n    -> '.join(refs))

print('\n=== Quaternioid -> what does it cite (broken links) ===')
broken = {}
for s, label in QA:
    p = os.path.join(REPO, 'articles_maths', s + '.md')
    if not os.path.exists(p): print('MISSING FILE', s); continue
    txt = open(p, encoding='utf-8').read()
    for t in sorted(set(LINK.findall(txt))):
        if t not in allslugs:
            broken.setdefault(t, []).append(s)
for t, srcs in sorted(broken.items()):
    print(f'  {t}  <- {len(srcs)}: {srcs[:4]}')

print('\n=== Quaternions broken links ===')
b2 = {}
for s, label in Q:
    p = os.path.join(REPO, 'articles_maths', s + '.md')
    if not os.path.exists(p): print('MISSING FILE', s); continue
    txt = open(p, encoding='utf-8').read()
    for t in sorted(set(LINK.findall(txt))):
        if t not in allslugs:
            b2.setdefault(t, []).append(s)
for t, srcs in sorted(b2.items()):
    print(f'  {t}  <- {len(srcs)}: {srcs[:4]}')

print('\n=== QA articles pointing to Quaternions titles but not existing ===')
# search for prose citations of *...* titles that have no file
