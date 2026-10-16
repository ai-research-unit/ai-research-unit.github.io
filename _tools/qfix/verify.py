import re, os, collections
REPO = '/home/hp/Documents/1_Doc/Projects/ai-research/ai-research-unit'
m = open(os.path.join(REPO, 'maths.md'), encoding='utf-8').read()
lines = m.splitlines()
AD = os.path.join(REPO, 'articles_maths')
real = set(f[:-3] for f in os.listdir(AD) if f.endswith('.md'))

# menu hrefs resolve
hrefs = re.findall(r'href="articles_maths/([^"]+)\.html"', m)
missing = sorted(set(h for h in hrefs if h not in real))
print('menu hrefs:', len(hrefs), 'missing:', len(missing), missing[:5])

for a, b, name in [('## Quaternions', '## Quaternioid Algebraic Structures', 'Quaternions'),
                   ('## Quaternioid Algebraic Structures', '## Split-Quaternions', 'Quaternioid')]:
    s = lines.index(a); e = next(i for i, l in enumerate(lines) if i > s and l.startswith('## '))
    print(name, 'entries:', sum(1 for l in lines[s:e] if 'articles_maths' in l))

def cat(a):
    s = next(i for i, l in enumerate(lines) if l == a)
    e = next(i for i, l in enumerate(lines) if i > s and l.startswith('## '))
    return set(re.search(r'articles_maths/([^"]+)\.html', l).group(1) for l in lines[s:e] if 'articles_maths' in l)

Q, QA = cat('## Quaternions'), cat('## Quaternioid Algebraic Structures')
deps = []
for slug in sorted(Q):
    p = os.path.join(AD, slug + '.md')
    if not os.path.exists(p):
        continue
    for n, line in enumerate(open(p, encoding='utf-8'), 1):
        for tgt in re.findall(r'articles_maths/([A-Za-z0-9_\-]+)\.md', line):
            if tgt in QA:
                deps.append(f'{slug}:{n}->{tgt}')
print('Quaternions -> Quaternioid deps:', len(deps), deps[:5])

d = collections.defaultdict(list)
for f in os.listdir(AD):
    if not f.endswith('.md'):
        continue
    for l in open(os.path.join(AD, f), encoding='utf-8'):
        if l.startswith('# '):
            d[l[2:].strip()].append(f); break
dups = [k for k, v in d.items() if len(v) > 1]
print('duplicate H1 groups:', len(dups))
print('reserve:', len(os.listdir(os.path.join(REPO, 'articles_reserve'))))
print('articles_maths md:', len(real))
