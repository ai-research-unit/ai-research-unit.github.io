import re, os
REPO = '/home/hp/Documents/1_Doc/Projects/ai-research/ai-research-unit'
AD = os.path.join(REPO, 'articles_maths')
m = open(os.path.join(REPO, 'maths.md'), encoding='utf-8').read().splitlines()

def cat(a):
    s = next(i for i, l in enumerate(m) if l == a)
    e = next(i for i, l in enumerate(m) if i > s and l.startswith('## '))
    return set(re.search(r'articles_maths/([^"]+)\.html', l).group(1) for l in m[s:e] if 'articles_maths' in l)

Q = cat('## Quaternions')
changed = []

# --- 1. annihilators: drop the body paragraph, fix the two claims ---
p = os.path.join(AD, 'annihilators-of-the-quaternion-algebra.md')
t = open(p, encoding='utf-8').read()
t = re.sub(r'\nThe chapter carries the structure-level article \*Annihilators in the Algebraic Structures over the Quaternion \$\\mathbb\{R\}\$ Space\*.*?The two notions are transposed, not equal\.\n', '\n', t, flags=re.S)
t = re.sub(r'has no zero divisors\s+and no Zero Divisors article, because there is no set to characterise\. What is left of the element\s+theory is the vanishing of the annihilator, and the article is short for that reason\.',
           'has no zero divisors. The zero-divisor set, empty here, is read in *Zero Divisors of the Quaternion Algebra*, above this article in this category. What is left for this article is the vanishing of the annihilator, and it is short for that reason.', t)
t = re.sub(r'The block has no Zero Divisors article, and this one is short, because there is nothing for\s+it to characterise\.',
           'The zero divisors are the empty set, read in *Zero Divisors of the Quaternion Algebra*, above this article in this category, and this article is short because there is nothing beyond the division property for the annihilator to characterise.', t)
open(p, 'w', encoding='utf-8').write(t)
changed.append('annihilators')

# --- 2. topology intro ---
p = os.path.join(AD, 'introduction-to-topology-on-the-quaternions.md')
t = open(p, encoding='utf-8').read()
t = t.replace('| the metric read for each of the six products | *Topology and Metric for Each of the Six Operations* |\n', '')
t = t.replace('and the metrics of the quaternion space and of the six products.', 'and the metrics of the quaternion space.')
t = re.sub(r'\n- \*Topology and Metric for Each of the Six Operations\* \(`articles_maths/topology-and-metric-for-each-of-the-six-operations\.md`\), for the metric reading of the six products', '', t)
open(p, 'w', encoding='utf-8').write(t)
changed.append('topology-intro')

# --- 3. cross-category citations inside the Quaternions category ---
REPL = [
    ('*The Group of Involutions of the Quaternions* (`articles_maths/the-group-of-involutions-of-the-quaternioid.md`)',
     '*Quaternion Involutions and Projections* (`articles_maths/quaternion-involutions-and-projections.md`)'),
    ('*The Quaternions as a Vector Space over $\\mathbb{R}$* (`articles_maths/the-quaternioid-as-a-vector-space-over-r.md`)',
     '*Quaternion Algebra* (`articles_maths/quaternion-algebra.md`)'),
    ('*The 2 Algebraic Norms over the Quaternion $\\mathbb{R}$ Space* (`articles_maths/the-2-algebraic-norms-over-the-quaternioid-r-space.md`)',
     '*Norm and Invertibility in the Quaternion Algebra* (`articles_maths/norm-and-invertibility-in-the-quaternion-algebra.md`)'),
    ('*Zero Divisors of the Quaternion Algebra* (`articles_maths/zero-divisors-of-the-biquaternion-algebra.md`)',
     '*Zero Divisors of the Biquaternion Algebra* (`articles_maths/zero-divisors-of-the-biquaternion-algebra.md`)'),
    ('*Square Roots of Zero and the Nilpotents of the Quaternion Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-biquaternion-algebra.md`)',
     '*Square Roots of Zero and the Nilpotents of the Biquaternion Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-biquaternion-algebra.md`)'),
    ('*Square Roots of One and the Idempotents of the Quaternion Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.md`)',
     '*Square Roots of One and the Idempotents of the Biquaternion Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.md`)'),
    ('*Idempotents of the Quaternion Algebra* (`articles_maths/idempotents-of-the-general-plain-algebra-of-quaternions.md`)',
     '*Square Roots of One and the Idempotents of the Quaternion Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-quaternion-algebra.md`)'),
    ('*Nilpotents of the Quaternion Algebra* (`articles_maths/nilpotents-of-the-general-plain-algebra-of-quaternions.md`)',
     '*Square Roots of Zero and the Nilpotents of the Quaternion Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-quaternion-algebra.md`)'),
]
for slug in sorted(Q):
    p = os.path.join(AD, slug + '.md')
    if not os.path.exists(p):
        continue
    t = open(p, encoding='utf-8').read()
    o = t
    # drop bullets that only point into the companion vocabulary
    t = re.sub(r'\n- \*Definitions for the Study of the Algebraic Structures over the Quaternion \$\\mathbb\{R\}\$ Space\*[^\n]*', '', t)
    for a, b in REPL:
        t = t.replace(a, b)
    if t != o:
        open(p, 'w', encoding='utf-8').write(t)
        changed.append(slug)
print('changed', len(changed))
for c in changed: print('  ', c)
