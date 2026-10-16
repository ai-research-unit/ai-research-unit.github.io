import os, re, collections
D = 'articles_maths'
d = collections.defaultdict(list)
for f in sorted(os.listdir(D)):
    if not f.endswith('.md'): continue
    txt = open(os.path.join(D, f), encoding='utf-8').read()
    m = re.search(r'^# (.+)$', txt, re.M)
    d[m.group(1).strip() if m else 'NO-H1'].append(f)
dups = {k: v for k, v in d.items() if len(v) > 1}
print('true duplicate-H1 groups:', len(dups))
for k, v in sorted(dups.items()):
    print(k)
    for x in v: print('    ', x)

# which of these are referenced in maths.md / physics.md
M = open('maths.md', encoding='utf-8').read()
P = open('physics.md', encoding='utf-8').read()
print('\n=== which duplicate files are referenced ===')
for k, v in sorted(dups.items()):
    state = []
    for x in v:
        s = x[:-3]
        state.append(f'{s}:' + ('M' if (s + '.html' in M) else '-') + ('P' if (s + '.html' in P) else '-'))
    print('  ', ' | '.join(state))
