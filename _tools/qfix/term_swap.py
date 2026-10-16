import re, os, sys
REPO = '/home/hp/Documents/1_Doc/Projects/ai-research/ai-research-unit'
APPLY = '--apply' in sys.argv
m = open(os.path.join(REPO, 'maths.md'), encoding='utf-8').read().splitlines()
s = next(i for i, l in enumerate(m) if l == '## Quaternions')
e = next(i for i, l in enumerate(m) if i > s and l.startswith('## '))
files = [re.search(r'articles_maths/([^"]+)\.html', l).group(1) for l in m[s:e] if 'articles_maths' in l]

SUBS = [
    ('of the General Plain Algebra of Quaternions', 'of the Quaternion Algebra'),
    ('of the General Plain Algebra', 'of the Quaternion Algebra'),
    ('Introduction to the General Plain Algebra of Quaternions', 'Introduction to the Quaternion Algebra'),
    ('the General Plain Algebra', 'the Quaternion Algebra'),
    ('The General Plain Algebra', 'The Quaternion Algebra'),
    ('the general plain algebra', 'the quaternion algebra'),
    ('general plain product', 'quaternion product'),
    ('General Plain Product', 'Quaternion Product'),
    ('general plain', 'quaternion'),
    ('General Plain', 'Quaternion'),
]
tot = {}
for slug in files:
    p = os.path.join(REPO, 'articles_maths', slug + '.md')
    t = open(p, encoding='utf-8').read()
    o = t
    for a, b in SUBS:
        n = t.count(a)
        if n:
            tot[a] = tot.get(a, 0) + n
            t = t.replace(a, b)
    # de-duplicate accidental stutter introduced by the swap
    t = t.replace('of the Quaternion Algebra of Quaternions', 'of the Quaternion Algebra')
    t = t.replace('Quaternion Algebra of Quaternions', 'Quaternion Algebra')
    if t != o and APPLY:
        open(p, 'w', encoding='utf-8').write(t)
    if t != o:
        print('changed', slug)
print(tot)
