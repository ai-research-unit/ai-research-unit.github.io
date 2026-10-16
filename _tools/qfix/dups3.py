import os, re, collections
D = 'articles_maths'
d = collections.defaultdict(list)
for f in sorted(os.listdir(D)):
    if not f.endswith('.md'):
        continue
    txt = open(os.path.join(D, f), encoding='utf-8').read()
    m = re.search(r'^# (.+)$', txt, re.M)
    d[m.group(1).strip() if m else 'NO'].append(f)
M = open('maths.md', encoding='utf-8').read()
P = open('physics.md', encoding='utf-8').read()
MH = set(re.findall(r'href="articles_maths/([^"]+)\.html"', M))
PH = set(re.findall(r'href="articles_maths/([^"]+)\.html"', P))
ML = set(re.findall(r'articles_maths/([A-Za-z0-9_\-]+)\.md', M))
PL = set(re.findall(r'articles_maths/([A-Za-z0-9_\-]+)\.md', P))

def ref(s):
    return ('M' if s in MH else '-') + ('m' if s in ML else '-') + ('P' if s in PH else '-') + ('p' if s in PL else '-')

groups = [(k, v) for k, v in sorted(d.items()) if len(v) > 1]
cats = collections.Counter()
odd = []
for k, v in groups:
    if len(v) != 2:
        odd.append((k, v)); continue
    a, b = [x[:-3] for x in v]
    q = [t for t in (a, b) if t.endswith('-of-quaternioid')]
    p = [t for t in (a, b) if not t.endswith('-of-quaternioid')]
    if len(q) != 1 or len(p) != 1:
        odd.append((k, v)); continue
    cats[(ref(q[0]), ref(p[0]))] += 1
for key, n in sorted(cats.items()):
    print(f'  qref={key[0]:6} pref={key[1]:6} : {n}')
print('\nodd groups:', len(odd))
for k, v in odd:
    print(' ', k, v)
