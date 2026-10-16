import re, os
REPO = '/home/hp/Documents/1_Doc/Projects/ai-research/ai-research-unit'
AD = os.path.join(REPO, 'articles_maths')
m = open(os.path.join(REPO, 'maths.md'), encoding='utf-8').read().splitlines()

def cat_slugs(a):
    s = next(i for i, l in enumerate(m) if l == a)
    e = next(i for i, l in enumerate(m) if i > s and l.startswith('## '))
    return set(re.search(r'articles_maths/([^"]+)\.html', l).group(1) for l in m[s:e] if 'articles_maths' in l)

q = cat_slugs('## Quaternions')
for slug in sorted(q):
    p = os.path.join(AD, slug + '.md')
    if not os.path.exists(p):
        print('MISSING FILE', slug); continue
    for n, line in enumerate(open(p, encoding='utf-8'), 1):
        for tgt in re.findall(r'articles_maths/([A-Za-z0-9_\-]+)\.md', line):
            if tgt not in q:
                print(f'{slug}:{n} -> {tgt}')
