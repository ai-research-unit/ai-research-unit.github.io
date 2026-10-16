import re, os
AD = '/home/hp/Documents/1_Doc/Projects/ai-research/ai-research-unit/articles_maths'

def edit(slug, pairs, drop_section=None):
    p = os.path.join(AD, slug + '.md')
    t = open(p, encoding='utf-8').read()
    o = t
    for a, b in pairs:
        t = t.replace(a, b)
    if drop_section:
        i = t.index(drop_section)
        j = t.index('\n## ', i + 1)
        t = t[:i] + t[j + 1:]
    if t != o:
        open(p, 'w', encoding='utf-8').write(t)
        print('fixed', slug)
    else:
        print('NO CHANGE', slug)

edit('introduction-to-the-quaternion-algebra', [
    ('these are what is written out. The further products the same space carries — the symmetrisation, the '
     'antisymmetrisation and the product with the conjugation read in the first slot — belong to the *Quaternioid '
     'Algebraic Structures* category and are cited there rather than here.',
     'these are what is written out.'),
], drop_section='## The Companion Products')

edit('the-specificities-of-the-quaternion-algebra', [
    ('carry the classes in full. The companion products the same space carries belong to the *Quaternioid '
     'Algebraic Structures* category and are cited there rather than here.',
     'carry the classes in full.'),
    ('**Theorem.** The quaternion product is the only product the space $\\mathbb{R}^4$ carries that is associative '
     'with a two-sided unit, and the only one with the division property. The companion products, and the reading of '
     'these properties on each of them, are the subject of the *Quaternioid Algebraic Structures* category; no '
     'companion product is re-derived here.',
     '**Theorem.** The quaternion product is associative with a two-sided unit and has the division property.'),
])

edit('zero-divisors-of-the-quaternion-algebra', [
    ('The Specificities of the Quaternion Algebra* (`articles_maths/the-specificities-of-the-quaternion-algebra.md`), '
     'below this article in this category, for the folding of the empty classes and the isolation of the plain '
     'product among the six.',
     'The Specificities of the Quaternion Algebra* (`articles_maths/the-specificities-of-the-quaternion-algebra.md`), '
     'below this article in this category, for the classes of element and the place of the algebra among the real '
     'division algebras.'),
])

edit('square-roots-of-zero-and-the-nilpotents-of-the-quaternion-algebra', [
    ('the folding of the empty classes, with the isolation of the plain product among the six, is *The Specificities '
     'of the Quaternion Algebra*.',
     'the classes of element and the place of the algebra among the real division algebras are *The Specificities of '
     'the Quaternion Algebra*.'),
    ('for the folding of the empty classes and the isolation of the plain product among the six.',
     'for the classes of element and the place of the algebra among the real division algebras.'),
])

edit('square-roots-of-one-and-the-idempotents-of-the-quaternion-algebra', [
    ('the multiplication of the algebra and the operation named the algebra in *The Algebraic Structures over the '
     'Quaternion $\\mathbb{R}$ Space*. It is the only one of the six products of the space that is associative with a '
     'two-sided unit, and it is a division rule;',
     'the multiplication of the algebra. It is an associative algebra with a two-sided unit, and a division rule;'),
])

edit('introduction-to-topology-on-the-quaternions', [
    ('The algebra is *Introduction to the Symmetric Quaternionic Algebra of Quaternions* and its block, above this '
     'article in this category;',
     'The algebra is *Introduction to the Quaternion Algebra* and its block, above this article in this category;'),
    ('the metrics are *Quaternion Metrics* and *Topology and Metric for Each of the Six Operations*, below this '
     'article in this category.',
     'the metrics are *Quaternion Metrics*, below this article in this category.'),
])
