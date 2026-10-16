import re, os, collections
REPO = '/home/hp/Documents/1_Doc/Projects/ai-research/ai-research-unit'
AD = os.path.join(REPO, 'articles_maths')
files = [f for f in os.listdir(AD) if f.endswith('.md')]
h1 = {}
for f in files:
    for l in open(os.path.join(AD, f), encoding='utf-8'):
        if l.startswith('# '):
            h1[f[:-3]] = l[2:].strip().strip('_').strip()
            break
pat = re.compile(r'\*([^*\n]+)\* \(`articles_maths/([a-z0-9\-]+)\.md`\)')
mis = collections.Counter()
samples = collections.defaultdict(list)
for f in files:
    t = open(os.path.join(AD, f), encoding='utf-8').read()
    for m in pat.finditer(t):
        cited, slug = m.group(1), m.group(2)
        if slug in h1 and cited != h1[slug]:
            key = (cited, h1[slug])
            mis[key] += 1
            if len(samples[key]) < 2:
                samples[key].append(f)
print('distinct title mismatches:', len(mis), 'total:', sum(mis.values()))
for (c, a), n in mis.most_common(40):
    print(f'{n:4d}  {c!r}  ->  {a!r}')
