import re, os, collections
REPO = '/home/hp/Documents/1_Doc/Projects/ai-research/ai-research-unit'
AD = os.path.join(REPO, 'articles_maths')
files = [f for f in os.listdir(AD) if f.endswith('.md')]
have = {f[:-3] for f in files}
bad = collections.Counter()
for f in files:
    t = open(os.path.join(AD, f), encoding='utf-8').read()
    for m in re.finditer(r'articles_maths/([a-z0-9\-]+)\.md', t):
        s = m.group(1)
        if s not in have:
            bad[s] += 1
print('distinct stale paths:', len(bad), 'occurrences:', sum(bad.values()))
for s, n in bad.most_common(25):
    print(f'{n:4d}  {s}')
