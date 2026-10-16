import re, os, sys

REPO = '/home/hp/Documents/1_Doc/Projects/ai-research/ai-research-unit'
menu = open(os.path.join(REPO, 'maths.md'), encoding='utf-8').read().splitlines()

start = next(i for i, l in enumerate(menu) if l.startswith('## PART VI'))
cats = [(i, l[3:]) for i, l in enumerate(menu) if i >= start and re.match(r'^## ', l)]
cats.append((len(menu), 'E'))

def entries(t):
    for k in range(len(cats) - 1):
        a, title = cats[k]
        b = cats[k + 1][0]
        if title != t:
            continue
        out = []
        for l in menu[a:b]:
            m = re.search(r'href="articles_maths/([^"]+)\.html">([^<]+)</a>', l)
            if m:
                out.append((m.group(1), m.group(2)))
        return out
    return []

Q = entries('Quaternions')
QA = entries('Quaternioid Algebraic Structures')
SQ = entries('Split-Quaternions')
qa_slugs = set(s for s, _ in QA)

print('Quaternions entries:', len(Q))
print('Quaternioid entries:', len(QA))
print('Split-Quaternions entries:', len(SQ))

print('\n=== Quaternions articles referencing quaternioid slugs ===')
hits = 0
for s, label in Q:
    p = os.path.join(REPO, 'articles_maths', s + '.md')
    if not os.path.exists(p):
        print('MISSING', s); continue
    txt = open(p, encoding='utf-8').read()
    refs = sorted(set(m for m in re.findall(r'articles_maths/([A-Za-z0-9\-]+)\.html', txt) if m in qa_slugs))
    refs_md = sorted(set(m for m in re.findall(r'\(articles_maths/([A-Za-z0-9\-]+)\.md\)', txt) if m in qa_slugs))
    if refs or refs_md:
        hits += 1
        print(s, '->', refs or refs_md)
print('total with refs:', hits)

print('\n=== Quaternions articles mentioning six/quaternioid keywords ===')
for s, label in Q:
    p = os.path.join(REPO, 'articles_maths', s + '.md')
    txt = open(p, encoding='utf-8').read()
    for kw in ['quaternioid', 'six algebraic structures', 'the six structures', 'six operations', 'six products']:
        n = txt.lower().count(kw.lower())
        if n:
            print(f'  {s}: "{kw}" x{n}')
