import re, os, shutil, sys, collections

REPO = '/home/hp/Documents/1_Doc/Projects/ai-research/ai-research-unit'
AD = os.path.join(REPO, 'articles_maths')
RES = os.path.join(REPO, 'articles_reserve')
APPLY = '--apply' in sys.argv

MOVED = {
    'remarkable-subspaces-under-the-six-operations': 'the-2-forms-over-the-quaternioid-r-space',
    'norm-and-invertibility-in-the-symmetric-plain-algebra-of-quaternioid': 'the-2-algebraic-norms-over-the-quaternioid-r-space',
    'zero-divisors-of-the-symmetric-plain-algebra-of-quaternioid': 'zero-divisors-in-the-algebraic-structures-over-the-quaternioid-r-space',
    'annihilators-of-the-symmetric-plain-algebra-of-quaternioid': 'annihilators-in-the-algebraic-structures-over-the-quaternioid-r-space',
    'square-roots-of-one-and-the-idempotents-of-the-symmetric-plain-algebra-of-quaternioid': 'the-square-the-idempotents-and-the-jordan-inverse-of-the-symmetric-plain-algebra-of-quaternioid',
    'square-roots-of-zero-and-the-nilpotents-of-the-symmetric-plain-algebra-of-quaternioid': 'square-roots-of-zero-and-the-nilpotents-in-the-algebraic-structures-over-the-quaternioid-r-space',
    'square-roots-of-a-general-element-in-the-symmetric-plain-algebra-of-quaternioid': 'square-roots-of-a-general-element-in-the-algebraic-structures-over-the-quaternioid-r-space',
    'norm-and-invertibility-in-the-antisymmetric-plain-algebra-of-quaternioid': 'the-killing-form-of-the-antisymmetric-plain-algebra-of-quaternioid',
    'zero-divisors-of-the-antisymmetric-plain-algebra-of-quaternioid': 'zero-divisors-in-the-algebraic-structures-over-the-quaternioid-r-space',
    'annihilators-of-the-antisymmetric-plain-algebra-of-quaternioid': 'annihilators-in-the-algebraic-structures-over-the-quaternioid-r-space',
    'square-roots-of-one-and-the-idempotents-of-the-antisymmetric-plain-algebra-of-quaternioid': 'square-roots-of-one-and-the-idempotents-in-the-algebraic-structures-over-the-quaternioid-r-space',
    'square-roots-of-zero-and-the-nilpotents-of-the-antisymmetric-plain-algebra-of-quaternioid': 'square-roots-of-zero-and-the-nilpotents-in-the-algebraic-structures-over-the-quaternioid-r-space',
    'square-roots-of-a-general-element-in-the-antisymmetric-plain-algebra-of-quaternioid': 'square-roots-of-a-general-element-in-the-algebraic-structures-over-the-quaternioid-r-space',
    'norm-and-invertibility-in-the-general-quaternionic-algebra-of-quaternioid': 'the-2-algebraic-norms-over-the-quaternioid-r-space',
    'zero-divisors-of-the-general-quaternionic-algebra-of-quaternioid': 'zero-divisors-in-the-algebraic-structures-over-the-quaternioid-r-space',
    'annihilators-of-the-general-quaternionic-algebra-of-quaternioid': 'annihilators-in-the-algebraic-structures-over-the-quaternioid-r-space',
    'square-roots-of-one-and-the-idempotents-of-the-general-quaternionic-algebra-of-quaternioid': 'square-roots-of-one-and-the-idempotents-in-the-algebraic-structures-over-the-quaternioid-r-space',
    'square-roots-of-zero-and-the-nilpotents-of-the-general-quaternionic-algebra-of-quaternioid': 'square-roots-of-zero-and-the-nilpotents-in-the-algebraic-structures-over-the-quaternioid-r-space',
    'square-roots-of-a-general-element-in-the-general-quaternionic-algebra-of-quaternioid': 'square-roots-of-a-general-element-in-the-algebraic-structures-over-the-quaternioid-r-space',
    'introduction-to-the-symmetric-quaternionic-algebra-of-quaternioid': 'the-symmetrised-quaternionic-product-and-the-hermitian-subspace-of-quaternioid',
    'norm-and-invertibility-in-the-symmetric-quaternionic-algebra-of-quaternioid': 'the-symmetrised-quaternionic-product-and-the-hermitian-subspace-of-quaternioid',
    'zero-divisors-of-the-symmetric-quaternionic-algebra-of-quaternioid': 'zero-divisors-in-the-algebraic-structures-over-the-quaternioid-r-space',
    'annihilators-of-the-symmetric-quaternionic-algebra-of-quaternioid': 'annihilators-in-the-algebraic-structures-over-the-quaternioid-r-space',
    'square-roots-of-one-and-the-idempotents-of-the-symmetric-quaternionic-algebra-of-quaternioid': 'square-roots-of-one-and-the-idempotents-in-the-algebraic-structures-over-the-quaternioid-r-space',
    'square-roots-of-zero-and-the-nilpotents-of-the-symmetric-quaternionic-algebra-of-quaternioid': 'square-roots-of-zero-and-the-nilpotents-in-the-algebraic-structures-over-the-quaternioid-r-space',
    'square-roots-of-a-general-element-in-the-symmetric-quaternionic-algebra-of-quaternioid': 'square-roots-of-a-general-element-in-the-algebraic-structures-over-the-quaternioid-r-space',
    'the-specificities-of-the-symmetric-quaternionic-algebra-of-quaternioid': 'the-specificities-of-the-general-quaternionic-algebra-of-quaternioid',
    'the-radical-and-the-isotropic-elements-of-the-symmetric-quaternionic-algebra-of-quaternioid': 'the-isotropic-structure-of-the-general-quaternionic-algebra-of-quaternioid',
    'the-quaternioid-form-as-a-product-on-the-symmetric-quaternionic-algebra-of-quaternioid': 'the-symmetrised-quaternionic-product-and-the-hermitian-subspace-of-quaternioid',
    'the-multiplication-operators-of-the-symmetric-quaternionic-algebra-of-quaternioid': 'the-left-multiplications-of-the-quaternionic-product-and-the-opposite-monoid-of-quaternioid',
    'the-symmetric-quaternionic-algebra-in-the-2x2-matrix-element-representation-of-quaternioid': 'the-general-quaternionic-algebra-in-the-2x2-matrix-element-representation-of-quaternioid',
    'the-symmetric-quaternionic-algebra-in-the-4x4-matrix-element-representation-of-quaternioid': 'the-general-quaternionic-algebra-in-the-4x4-matrix-element-representation-of-quaternioid',
    'introduction-to-the-antisymmetric-quaternionic-algebra-of-quaternioid': 'introduction-to-the-general-quaternionic-algebra-of-quaternioid',
    'norm-and-invertibility-in-the-antisymmetric-quaternionic-algebra-of-quaternioid': 'the-specificities-of-the-general-quaternionic-algebra-of-quaternioid',
    'zero-divisors-of-the-antisymmetric-quaternionic-algebra-of-quaternioid': 'zero-divisors-in-the-algebraic-structures-over-the-quaternioid-r-space',
    'annihilators-of-the-antisymmetric-quaternionic-algebra-of-quaternioid': 'annihilators-in-the-algebraic-structures-over-the-quaternioid-r-space',
    'square-roots-of-minus-one-zero-and-plus-one-in-the-antisymmetric-quaternionic-algebra-of-quaternioid': 'square-roots-of-one-and-the-idempotents-in-the-algebraic-structures-over-the-quaternioid-r-space',
    'square-roots-of-a-general-element-in-the-antisymmetric-quaternionic-algebra-of-quaternioid': 'square-roots-of-a-general-element-in-the-algebraic-structures-over-the-quaternioid-r-space',
    'idempotents-of-the-antisymmetric-quaternionic-algebra-of-quaternioid': 'square-roots-of-one-and-the-idempotents-in-the-algebraic-structures-over-the-quaternioid-r-space',
    'nilpotents-of-the-antisymmetric-quaternionic-algebra-of-quaternioid': 'square-roots-of-zero-and-the-nilpotents-in-the-algebraic-structures-over-the-quaternioid-r-space',
    'the-specificities-of-the-antisymmetric-quaternionic-algebra-of-quaternioid': 'the-specificities-of-the-general-quaternionic-algebra-of-quaternioid',
    'the-jacobi-failure-and-the-associator-defect-of-the-antisymmetric-quaternionic-algebra-of-quaternioid': 'the-associator-and-the-ternary-product-of-the-quaternionic-product-of-quaternioid',
    'the-invariant-bilinear-forms-of-the-antisymmetric-quaternionic-algebra-of-quaternioid': 'the-2-forms-over-the-quaternioid-r-space',
    'the-adjoint-operators-of-the-antisymmetric-quaternionic-algebra-of-quaternioid': 'one-sided-operators-on-the-general-quaternionic-algebra-of-quaternioid',
    'the-antisymmetric-quaternionic-algebra-in-the-2x2-matrix-element-representation-of-quaternioid': 'the-general-quaternionic-algebra-in-the-2x2-matrix-element-representation-of-quaternioid',
    'the-antisymmetric-quaternionic-algebra-in-the-4x4-matrix-element-representation-of-quaternioid': 'the-general-quaternionic-algebra-in-the-4x4-matrix-element-representation-of-quaternioid',
    'topology-and-metric-for-each-of-the-six-operations': 'the-2-forms-over-the-quaternioid-r-space',
}

def h1(path):
    if not os.path.exists(path):
        return None
    for l in open(path, encoding='utf-8'):
        if l.startswith('# '):
            t = l[2:].strip()
            if t.startswith('__') and t.endswith('__'):
                t = t[2:-2]
            return t
    return None

missing = [s for s in MOVED if not os.path.exists(os.path.join(AD, s + '.md'))]
print('retire count:', len(MOVED), 'missing:', missing)

TITLE = {s: h1(os.path.join(AD, s + '.md')) for s in MOVED}
TARGET_TITLE = {t: h1(os.path.join(AD, t + '.md')) for t in set(MOVED.values())}

if APPLY:
    os.makedirs(RES, exist_ok=True)
    for s in MOVED:
        for ext in ('.md', '.context'):
            src = os.path.join(AD, s + ext)
            if os.path.exists(src):
                shutil.move(src, os.path.join(RES, s + ext))
    print('moved', len(MOVED), 'articles (+ contexts) to articles_reserve/')

# ---- redirect references in surviving files ----
files = [os.path.join(AD, f) for f in os.listdir(AD) if f.endswith('.md')]
files += [os.path.join(REPO, 'maths.md'), os.path.join(REPO, 'physics.md')]

# order matters: longest slug first if prefixes overlap
order = sorted(MOVED, key=len, reverse=True)
stats = collections.Counter()
changed_files = []
for fp in files:
    txt = open(fp, encoding='utf-8').read()
    orig = txt
    for old in order:
        new = MOVED[old]
        for ext in ('.md', '.html'):
            n = txt.count(f'articles_maths/{old}{ext}')
            if n:
                txt = txt.replace(f'articles_maths/{old}{ext}', f'articles_maths/{new}{ext}')
                stats[ext] += n
    # fix the fenced title sitting just before a redirected path
    for old in order:
        new = MOVED[old]
        ot, nt = TITLE.get(old), TARGET_TITLE.get(new)
        if not ot or not nt:
            continue
        for ext in ('.md', '.html'):
            pat = '*' + ot + '* (`articles_maths/' + new + ext + '`)'
            rep = '*' + nt + '* (`articles_maths/' + new + ext + '`)'
            if pat in txt:
                stats['title'] += txt.count(pat)
                txt = txt.replace(pat, rep)
    if txt != orig:
        changed_files.append(os.path.basename(fp))
        if APPLY:
            open(fp, 'w', encoding='utf-8').write(txt)

print('path replacements:', dict(stats))
print('files changed:', len(changed_files))
