import re, os
REPO = '/home/hp/Documents/1_Doc/Projects/ai-research/ai-research-unit'
AD = os.path.join(REPO, 'articles_maths')
files = [f for f in os.listdir(AD) if f.endswith('.md')]
h1 = {}
for f in files:
    for l in open(os.path.join(AD, f), encoding='utf-8'):
        if l.startswith('# '):
            h1[f[:-3]] = l[2:].strip().strip('_').strip()
            break
pat = re.compile(r'\*([^*\n]+)\* \(`?articles_maths/([a-z0-9\-]+)\.md`?\)')
total = 0
changed = 0
for f in files:
    p = os.path.join(AD, f)
    t = open(p, encoding='utf-8').read()
    def sub(m):
        global total
        cited, slug = m.group(1), m.group(2)
        if slug in h1 and cited != h1[slug]:
            total += 1
            return f'*{h1[slug]}* (`articles_maths/{slug}.md`)'
        return m.group(0)
    nt = pat.sub(sub, t)
    if nt != t:
        open(p, 'w', encoding='utf-8').write(nt)
        changed += 1
print('citations normalized:', total, 'files changed:', changed)
