import os
p = '/home/hp/Documents/1_Doc/Projects/ai-research/ai-research-unit/articles_maths/the-6-products-of-the-quaternioid-real-space.md'
t = open(p, encoding='utf-8').read()
pairs = [
    ('The six are the products of the six algebraic structures of the chapter, and the reconstruction '
     '$\\tilde p\\tilde q=\\tilde p\\bullet\\tilde q+\\tilde p\\wedge\\tilde q$ and '
     '$\\tilde p^{\\natural}\\tilde q=N(\\tilde p,\\tilde q)e_0+\\tilde p\\wedge^{\\natural}\\tilde q$ recovers the general '
     'products from their halves.',
     'The six are the products of the carrier, and the reconstruction '
     '$\\tilde p\\tilde q=\\tilde p\\bullet\\tilde q+\\tilde p\\wedge\\tilde q$ and '
     '$\\tilde p^{\\natural}\\tilde q=N(\\tilde p,\\tilde q)e_0+\\tilde p\\wedge^{\\natural}\\tilde q$ recovers the general '
     'products from their halves. Three of the six are the products of the structures of this category, the symmetric plain, '
     'the antisymmetric plain and the general quaternionic; the algebra product belongs to the *Quaternions* category, and the '
     'two quaternionic halves carry no separate structure here.'),
    ('The six products here are the six products of the six algebraic structures of *The Algebraic Structures over the '
     'Quaternioid $\\mathbb{R}$ Space*, below this article in this category; the antisymmetric ones are the two Lie-layer '
     'products, and the symmetric ones the two Jordan-layer products.',
     'The products here are those of *The Algebraic Structures over the Quaternioid $\\mathbb{R}$ Space*, below this article '
     'in this category. Of the six, the antisymmetric plain product is the Lie-layer product and the symmetric plain product '
     'the Jordan-layer product; the antisymmetric plain algebra is the only one of the structures satisfying the Jacobi '
     'identity, and the general quaternionic product is not a Lie product.'),
]
for a, b in pairs:
    if a in t:
        t = t.replace(a, b); print('ok')
    else:
        print('NOT FOUND:', a[:60])
open(p, 'w', encoding='utf-8').write(t)
