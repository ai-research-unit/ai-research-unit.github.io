import re, os
REPO = '/home/hp/Documents/1_Doc/Projects/ai-research/ai-research-unit'
AD = os.path.join(REPO, 'articles_maths')
lines = open(os.path.join(REPO, 'maths.md'), encoding='utf-8').read().splitlines()

def cat(a):
    s = next(i for i, l in enumerate(lines) if l == a)
    e = next(i for i, l in enumerate(lines) if i > s and l.startswith('## '))
    return [re.search(r'articles_maths/([^"]+)\.html', l).group(1) for l in lines[s:e] if 'articles_maths' in l]

Q = cat('## Quaternions')
QA = cat('## Quaternioid Algebraic Structures')
terms = ['quaternioid', 'Quaternioid', 'SPA', 'SQA', 'AQA', 'GPA', 'six', 'Six']
print('=== QUATERNIONS FORBIDDEN-TERM SCAN ===')
for s in Q:
    p = os.path.join(AD, s + '.md')
    if not os.path.exists(p):
        print('MISSING', s); continue
    t = open(p, encoding='utf-8').read()
    hits = {k: len(re.findall(r'\b' + k + r'\b', t)) for k in terms}
    hits = {k: v for k, v in hits.items() if v}
    if hits:
        print(f'{s}: {hits}')
print()
print('=== QUATERNIOID ARTICLES WITH "six" ===')
for s in QA:
    p = os.path.join(AD, s + '.md')
    if not os.path.exists(p):
        print('MISSING', s); continue
    t = open(p, encoding='utf-8').read()
    n = len(re.findall(r'\bsix\b|\bSix\b', t))
    if n:
        print(f'{n:3d}  {len(t.split()):6d} w  {s}')
