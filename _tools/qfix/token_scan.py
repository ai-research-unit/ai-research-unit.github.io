import re, os
REPO = '/home/hp/Documents/1_Doc/Projects/ai-research/ai-research-unit'
m = open(os.path.join(REPO, 'maths.md'), encoding='utf-8').read().splitlines()
s = m.index('## Quaternioid Algebraic Structures')
e = next(i for i, l in enumerate(m) if i > s and l.startswith('## '))
slugs = [re.search(r'articles_maths/([^"]+)\.html', l).group(1) for l in m[s:e] if 'articles_maths' in l]
keys = ['SQA', 'AQA', 'GPA', 'six', 'Six', 'Quaternioid']
tot = 0
for x in slugs:
    p = os.path.join(REPO, 'articles_maths', x + '.md')
    if not os.path.exists(p):
        print('MISSING', x); continue
    t = open(p, encoding='utf-8').read()
    d = {k: len(re.findall(r'\b' + k + r'\b', t)) for k in keys}
    d = {k: v for k, v in d.items() if v}
    if d:
        tot += 1
        print(f'{str(d):50s} {x}')
print('articles with issues:', tot, 'of', len(slugs))
