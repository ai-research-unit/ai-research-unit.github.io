import re, os
REPO = '/home/hp/Documents/1_Doc/Projects/ai-research/ai-research-unit'
AD = os.path.join(REPO, 'articles_maths')
lines = open(os.path.join(REPO, 'maths.md'), encoding='utf-8').read().splitlines()
s = lines.index('## Quaternions')
e = next(i for i, l in enumerate(lines) if i > s and l.startswith('## '))
Q = [re.search(r'articles_maths/([^"]+)\.html', l).group(1) for l in lines[s:e] if 'articles_maths' in l]

TITLE_MAP = [
    ('*Definitions for the Study of the Algebraic Structures over the Quaternioid $\\mathbb{R}$ Space*', '*Algebras: A General Introduction*'),
    ('*The 2 Algebraic Norms over the Quaternioid $\\mathbb{R}$ Space*', '*Norm and Invertibility in the Quaternion Algebra*'),
    ('*The 2 Forms over the Quaternioid $\\mathbb{R}$ Space*', '*Association and the Transpose on the Quaternion Algebra*'),
    ('*The Two General Products of the Quaternioid $\\mathbb{R}$ Space*', ''),
    ('*The 6 Products of the Quaternioid Real Space*', ''),
    ('*The Algebraic Structures over the Quaternioid $\\mathbb{R}$ Space*', ''),
    ('*The Group of Involutions of the Quaternioid*', '*Quaternion Involutions and Projections*'),
    ('*The Quaternioid as a Vector Space over $\\mathbb{R}$*', '*Quaternion Algebra*'),
    ('*Introduction to the Symmetric Quaternionic Algebra of Quaternions*', '*Introduction to the Quaternion Algebra*'),
    ('*The 6 Products of the Quaternioid $\\mathbb{R}$ Space*', ''),
]
SWAP = [
    ('the general plain bilinear product', 'the quaternion product'),
    ('general plain bilinear product', 'quaternion product'),
    ('the general plain product', 'the quaternion product'),
    ('general plain product', 'quaternion product'),
    ('the general plain structure', 'the quaternion algebra'),
    ('general plain structure', 'quaternion algebra'),
    ('the General Plain Algebra', 'the Quaternion Algebra'),
    ('General Plain Algebra', 'Quaternion Algebra'),
    ('the general plain algebra', 'the quaternion algebra'),
    ('general plain algebra', 'quaternion algebra'),
    ('general plain', 'quaternion'),
    ('the plain product', 'the quaternion product'),
    ('plain product', 'quaternion product'),
    ('the plain square', 'the square'),
    ('plain square', 'square'),
    ('the plain structure', 'the quaternion algebra'),
    ('§*The Element Vocabulary*', ''),
    ('§*The Criterion for an Empty Class*', ''),
]

def run(fn, pairs):
    p = os.path.join(AD, fn)
    t = open(p, encoding='utf-8').read()
    for a, b in pairs:
        if a in t:
            t = t.replace(a, b)
        else:
            print('MISS', fn, '::', a[:60].replace('\n', '\\n'))
    open(p, 'w', encoding='utf-8').write(t)

Z = 'zero-divisors-of-the-quaternion-algebra.md'
run(Z, [
 ("The definition is stated once for a general product in\n*Definitions for the Study of the Algebraic Structures over the Quaternioid $\\mathbb{R}$ Space*, §*The Element Vocabulary*; the unqualified\n\"zero divisor\" means \"zero divisor of the general plain bilinear product\", the multiplication of the\nquaternion algebra, and every other product is named.",
  "The definition is stated once for a general product in *Algebras: A General Introduction*; the unqualified \"zero divisor\" means \"zero divisor of the quaternion product\", the multiplication of the quaternion algebra."),
 ("*Introduction to the Quaternion Algebra*, *The Two General Products of the\nQuaternioid $\\mathbb{R}$ Space* and *Introduction to the Remarkable Subspaces of the Quaternions*,",
  "*Introduction to the Quaternion Algebra* and *Introduction to the Remarkable Subspaces of the Quaternions*,"),
 ("$N(\\tilde p\\tilde q) = N(\\tilde p)N(\\tilde q)$, by *Norm and Invertibility in the General Plain\nAlgebra*, above this article in this category.",
  "$N(\\tilde p\\tilde q) = N(\\tilde p)N(\\tilde q)$, by *Norm and Invertibility in the Quaternion Algebra*, above this article in this category."),
 (" The two forms are\n*The 2 Forms over the Quaternioid $\\mathbb{R}$ Space*.", ""),
 ("and the two restrictions of the norm are *The 2 Algebraic Norms over\nthe Quaternioid $\\mathbb{R}$ Space*.",
  "and the two restrictions of the norm are read in *Norm and Invertibility in the Quaternion Algebra*."),
 ("for the folding of the empty classes and the isolation of the plain product among the six.",
  "for the folding of the empty classes."),
])

run('annihilators-of-the-quaternion-algebra.md', [
 ("\nThe chapter carries the structure-level article *Annihilators in the Algebraic Structures over the Quaternioid $\\mathbb{R}$ Space*\n(`articles_maths/annihilators-in-the-algebraic-structures-over-the-quaternioid-r-space.md`), whose annihilating set asks the other question:\nwhich elements kill the whole space for a fixed product, the radical of that product, where this\narticle asks which elements a fixed element kills. The two notions are transposed, not equal.\n", "\n"),
])

run('square-roots-of-one-and-the-idempotents-of-the-quaternion-algebra.md', [
 ("the multiplication of the algebra and the operation named the algebra in *The Algebraic Structures over the Quaternioid $\\mathbb{R}$ Space*. It is the only one of the six products of the space that is associative with a two-sided unit, and it is a division rule; that product is the one read throughout this article.",
  "the multiplication of the quaternion algebra. It is associative with a two-sided unit, and it is a division rule; that product is the one read throughout this article."),
 ("The general definition of the power, the square and the root of a central value, and the general definition of an idempotent, are *Definitions for the Study of the Algebraic Structures over the Quaternioid $\\mathbb{R}$ Space*, §*The Element Vocabulary*; the orthogonal, complete and primitive families, the projection and the Peirce decomposition are *Unital Algebras*, §*Idempotents and the Peirce Decomposition*. Throughout this article the square is the one of the general plain bilinear product, the multiplication of the algebra; the other five structures over the same space carry roots and idempotents of their own.",
  "The general definition of the power, the square and the root of a central value, and the general definition of an idempotent, are *Algebras: A General Introduction*; the orthogonal, complete and primitive families, the projection and the Peirce decomposition are *Unital Algebras*, §*Idempotents and the Peirce Decomposition*. Throughout this article the square is the one of the quaternion product, the multiplication of the algebra."),
])

run('square-roots-of-zero-and-the-nilpotents-of-the-quaternion-algebra.md', [
 ("the multiplication of the algebra and the operation named the algebra in *The Algebraic Structures over the Quaternioid $\\mathbb{R}$ Space*. That product is the one read throughout this article.",
  "the multiplication of the quaternion algebra. That product is the one read throughout this article."),
 ("the folding of the empty classes, with the isolation of the plain product among the six, is *The Specificities of the Quaternion Algebra*.",
  "the folding of the empty classes is *The Specificities of the Quaternion Algebra*."),
 ("*Definitions for the Study of the Algebraic Structures over the Quaternioid $\\mathbb{R}$ Space*, §*The Element Vocabulary*. Throughout this article the square is the one of the general plain bilinear product, the multiplication of the algebra; the other five structures over the same space carry roots of $0$ and square-zero sets of their own.",
  "*Algebras: A General Introduction*. Throughout this article the square is the one of the quaternion product, the multiplication of the algebra."),
 ("(*Definitions for the Study of the Algebraic Structures over the Quaternioid $\\mathbb{R}$ Space*, §*The Criterion for an Empty Class*)",
  "(*Algebras: A General Introduction*)"),
 ("the two restrictions of the norm are *The 2 Algebraic Norms over the Quaternioid $\\mathbb{R}$ Space*.",
  "the two restrictions of the norm are read in *Norm and Invertibility in the Quaternion Algebra*."),
 ("for the folding of the empty classes and the isolation of the plain product among the six.",
  "for the folding of the empty classes."),
])

run('the-specificities-of-the-quaternion-algebra.md', [
 ("carry the classes in full. The companion products the same space carries belong to the *Quaternioid Algebraic Structures* category and are cited there rather than here.",
  "carry the classes in full."),
 ("**Theorem.** The quaternion product is the only product the space $\\mathbb{R}^4$ carries that is associative with a two-sided unit, and the only one with the division property. The companion products, and the reading of these properties on each of them, are the subject of the *Quaternioid Algebraic Structures* category; no companion product is re-derived here.",
  "**Theorem.** The quaternion product is associative with a two-sided unit and has the division property."),
])

run('introduction-to-topology-on-the-quaternions.md', [
 ("The algebra is *Introduction to the Symmetric Quaternionic Algebra of Quaternions* and its block, above this article in this category;",
  "The algebra is *Introduction to the Quaternion Algebra* and its block, above this article in this category;"),
 ("the metrics are *Quaternion Metrics* and *Topology and Metric for Each of the Six Operations*, below this article in this category.",
  "the metrics are *Quaternion Metrics*, below this article in this category."),
])

run('introduction-to-the-remarkable-subspaces-of-the-quaternions.md', [
 ("the norm is quoted from *The 2 Algebraic Norms over the Quaternioid $\\mathbb{R}$ Space*, below this article in this category, and the invertibility criterion from *Norm and Invertibility in the Quaternion Algebra*, below this article in this category.",
  "the norm and the invertibility criterion are *Norm and Invertibility in the Quaternion Algebra*, below this article in this category."),
])

run('association-and-the-transpose-on-the-quaternion-algebra.md', [
 ("The two products and the two forms are owned by *The 6 Products of the Quaternioid Real Space* and *The 2 Forms over the Quaternioid $\\mathbb{R}$ Space*, above this article in this category; the operators themselves are",
  "The form of the quaternion product is read in this article; the operators themselves are"),
])

# generic passes over all Quaternions files
for slug in Q:
    p = os.path.join(AD, slug + '.md')
    if not os.path.exists(p):
        continue
    t = open(p, encoding='utf-8').read()
    o = t
    for a, b in TITLE_MAP:
        t = t.replace(a, b)
    for a, b in SWAP:
        t = t.replace(a, b)
    t = t.replace(' ,', ',').replace(' .', '.').replace(',,', ',').replace('( ', '(').replace(' )', ')')
    if slug == 'association-and-the-transpose-on-the-quaternion-algebra':
        t = t.replace('plain form', 'product form')
    if t != o:
        open(p, 'w', encoding='utf-8').write(t)

# explicit intro cleanup
p = os.path.join(AD, 'introduction-to-the-quaternion-algebra.md')
t = open(p, encoding='utf-8').read()
if '## The Other Five Products' in t:
    i = t.index('## The Other Five Products')
    j = t.index('\n## ', i + 1)
    t = t[:i] + t[j + 1:]
t = t.replace('The quaternion space $\\mathbb{R}^4$, with basis $e_0,e_1,e_2,e_3$ and a bilinear product, carries six products; the present one is the **quaternion product** $\\tilde p\\tilde q$, the multiplication of the quaternion algebra $\\mathbb{H}$.',
              'The quaternion algebra $\\mathbb{H}$ is the space $\\mathbb{R}^4$ with basis $e_0,e_1,e_2,e_3$ under the **quaternion product** $\\tilde p\\tilde q$, the multiplication of the algebra.')
t = t.replace(' It is the entry point of the block; the norm and the group of units are *Norm and Invertibility in the Quaternion Algebra*, below this article in this category, the ideal theory is *Ideals and Simplicity of the Quaternion Algebra*, below this article in this category, and the remaining five products are, above this article in this category, which owns the family and is cited here rather than restated.',
              ' It is the entry point of the block; the norm and the group of units are *Norm and Invertibility in the Quaternion Algebra*, below this article in this category, and the ideal theory is *Ideals and Simplicity of the Quaternion Algebra*, below this article in this category.')
open(p, 'w', encoding='utf-8').write(t)
print('q_hygiene done')
