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

def ref(s):
    return ('M' if (s + '.html') in M else '-') + ('P' if (s + '.html') in P else '-')

groups = [(k, v) for k, v in sorted(d.items()) if len(v) > 1]
print('dup groups', len(groups))
cats = collections.Counter()
for k, v in groups:
    if len(v) != 2:
        print('ODD-SIZE', k, v); continue
    a, b = [x[:-3] for x in v]
    q = [t for t in (a, b) if t.endswith('-of-quaternioid')]
    p = [t for t in (a, b) if not t.endswith('-of-quaternioid')]
    if len(q) != 1 or len(p) != 1:
        print('ODD-NAME', k, v); continue
    q, p = q[0], p[0]
    key = (ref(q), ref(p))
    cats[key] += 1
for key, n in sorted(cats.items()):
    print(f'  qref={key[0]!r:6} pref={key[1]!r:6} : {n}')
