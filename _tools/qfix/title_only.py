import re, os, subprocess, collections, sys
REPO = '/home/hp/Documents/1_Doc/Projects/ai-research/ai-research-unit'
AD = os.path.join(REPO, 'articles_maths')
APPLY = '--apply' in sys.argv
files = [f for f in os.listdir(AD) if f.endswith('.md')]

def norm(s):
    s = s.replace('\\', '')
    return re.sub(r'\s+', ' ', s).strip().strip('_').strip()

h1 = {}
for f in files:
    for l in open(os.path.join(AD, f), encoding='utf-8'):
        if l.startswith('# '):
            h1[f[:-3]] = norm(l[2:])
            break
h1set = set(h1.values())
h1raw = set()
for f in files:
    for l in open(os.path.join(AD, f), encoding='utf-8'):
        if l.startswith('# '):
            h1raw.add(l[2:].strip().strip('_').strip())
            break

pathpat = re.compile(r'\*([^*\n]+)\* \(`articles_maths/([a-z0-9\-]+)\.md`\)')
rename = {}
for f in files:
    try:
        old = subprocess.run(['git', '-C', REPO, 'show', 'HEAD:articles_maths/' + f],
                             capture_output=True, text=True, check=True).stdout
    except Exception:
        continue
    for m in pathpat.finditer(old):
        cited, slug = m.group(1), m.group(2)
        if slug in h1:
            c = norm(cited)
            new = h1[slug]
            if c != new and c not in h1set:
                rename.setdefault(c, new)

print('rename map size:', len(rename))
cnt = collections.Counter()
for f in files:
    t = open(os.path.join(AD, f), encoding='utf-8').read()
    for old, new in rename.items():
        n = t.count('*' + old + '*')
        if n:
            cnt[(old, new)] += n
print('title-only occurrences to fix:', sum(cnt.values()))
for (old, new), n in cnt.most_common(20):
    print(f'{n:4d}  {old!r} -> {new!r}')
if APPLY:
    changed = 0
    for f in files:
        p = os.path.join(AD, f)
        t = open(p, encoding='utf-8').read()
        o = t
        for old, new in rename.items():
            t = t.replace('*' + old + '*', '*' + new + '*')
        if t != o:
            open(p, 'w', encoding='utf-8').write(t)
            changed += 1
    print('files changed:', changed)
