import re, os
REPO = '/home/hp/Documents/1_Doc/Projects/ai-research/ai-research-unit'
AD = os.path.join(REPO, 'articles_maths')
m = open(os.path.join(REPO, 'maths.md'), encoding='utf-8').read().splitlines()

def cat(a):
    s = next(i for i, l in enumerate(m) if l == a)
    e = next(i for i, l in enumerate(m) if i > s and l.startswith('## '))
    return set(re.search(r'articles_maths/([^"]+)\.html', l).group(1) for l in m[s:e] if 'articles_maths' in l)

QA = cat('## Quaternioid Algebraic Structures')
Q = cat('## Quaternions')
changed = []
for slug in sorted(Q):
    p = os.path.join(AD, slug + '.md')
    if not os.path.exists(p):
        continue
    lines = open(p, encoding='utf-8').read().split('\n')
    keep = []
    for ln in lines:
        tg = re.findall(r'articles_maths/([A-Za-z0-9_\-]+)\.md', ln)
        if ln.lstrip().startswith('- ') and tg and all(x in QA for x in tg):
            changed.append(f'{slug}: dropped bullet -> {tg[0]}')
            continue
        keep.append(ln)
    if len(keep) != len(lines):
        open(p, 'w', encoding='utf-8').write('\n'.join(keep))
print('drops', len([c for c in changed if 'dropped' in c]))
for c in changed: print('  ', c)
