import re, os, subprocess, collections, sys
REPO = '/home/hp/Documents/1_Doc/Projects/ai-research/ai-research-unit'
AD = os.path.join(REPO, 'articles_maths')
APPLY = '--apply' in sys.argv
files = [f for f in os.listdir(AD) if f.endswith('.md')]

def norm(s):
    s = s.replace('\\', '')
    return re.sub(r'\s+', ' ', s).strip().strip('_').strip()

h1raw, h1norm = {}, {}
for f in files:
    for l in open(os.path.join(AD, f), encoding='utf-8'):
        if l.startswith('# '):
            raw = l[2:].strip().strip('_').strip()
            h1raw[f[:-3]] = raw
            h1norm[f[:-3]] = norm(raw)
            break
h1set = set(h1norm.values())

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
        if slug in h1raw:
            c = norm(cited)
            if c != h1norm[slug] and c not in h1set and re.match(r'^[A-Z]', c) and '*' not in c:
                rename.setdefault(c, h1raw[slug])
print('guarded rename map:', len(rename))

def make_pat(old):
    out = []
    for ch in old:
        if ch == '$':
            out.append(r'\$\\?')
        elif ch == '{':
            out.append(r'\{')
        elif ch == '}':
            out.append(r'\}')
        else:
            out.append(re.escape(ch))
    return ''.join(out)

pats = [(re.compile(r'\*' + make_pat(o) + r'\*'), n) for o, n in rename.items()]
splitpat = re.compile(r'\*([^*\n]+)\*\s*\n\s*\((`?articles_maths/([a-z0-9\-]+)\.md`?)\)')

count = collections.Counter()
changed = 0
for f in files:
    p = os.path.join(AD, f)
    t = open(p, encoding='utf-8').read()
    o0 = t
    for pat, new in pats:
        t, n = pat.subn(lambda m, new=new: '*' + new + '*', t)
        if n:
            count[new] += n

    def sub(m):
        slug = m.group(3)
        return f'*{h1raw.get(slug, m.group(1))}* (`articles_maths/{slug}.md`)'
    t = splitpat.sub(sub, t)
    if t != o0:
        changed += 1
        if APPLY:
            open(p, 'w', encoding='utf-8').write(t)
print('title replacements:', sum(count.values()), 'files changed:', changed, '(apply)' if APPLY else '(dry run)')
for k, v in count.most_common(10):
    print(f'{v:4d}  {k}')
