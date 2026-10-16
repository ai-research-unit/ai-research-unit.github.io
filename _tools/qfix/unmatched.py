import re, os, collections
REPO = '/home/hp/Documents/1_Doc/Projects/ai-research/ai-research-unit'
AD = os.path.join(REPO, 'articles_maths')
files = [f for f in os.listdir(AD) if f.endswith('.md')]

def norm(s):
    s = s.replace('\\', '')
    s = re.sub(r'\s+', ' ', s)
    return s.strip().strip('_').strip()

h1 = {}
for f in files:
    for l in open(os.path.join(AD, f), encoding='utf-8'):
        if l.startswith('# '):
            h1[f[:-3]] = norm(l[2:])
            break
h1set = set(h1.values())

# starred citations, not inside $...$, not section refs
cit_pat = re.compile(r'(?<![\w$§])\*([A-Z][^*\n]{4,120}?)\*(?![\w])')
unmatched = collections.Counter()
for f in files:
    t = open(os.path.join(AD, f), encoding='utf-8').read()
    t = re.sub(r'\$[^$\n]*\$', ' ', t)
    for m in cit_pat.finditer(t):
        c = norm(m.group(1))
        if c in h1set:
            continue
        unmatched[c] += 1
print('unmatched starred citations:', sum(unmatched.values()), 'distinct:', len(unmatched))
for c, n in unmatched.most_common(35):
    print(f'{n:4d}  {c}')
