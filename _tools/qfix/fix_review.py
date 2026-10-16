import os
AD = '/home/hp/Documents/1_Doc/Projects/ai-research/ai-research-unit/articles_maths'

def patch(fn, pairs):
    p = os.path.join(AD, fn)
    t = open(p, encoding='utf-8').read()
    for a, b in pairs:
        if a in t:
            t = t.replace(a, b)
        else:
            print('MISS', fn, '::', a[:60].replace('\n', '\\n'))
    open(p, 'w', encoding='utf-8').write(t)

patch('zero-divisors-of-the-quaternion-algebra.md', [
 ("it opens the element theory of the block: the two families into which the zero divisors of the\ncomplexified block separate have their real counterparts in *Idempotents of the General Plain\nAlgebra* and *Nilpotents of the Quaternion Algebra*, both below this article in this category, and\nthe vocabulary of pure and non-pure is used throughout.",
  "it opens the element theory of the block: the zero divisors of the complexified block, of the\nidempotent and the nilpotent type, are *Zero Divisors of the Biquaternion Algebra*, in the\nneighbouring *Biquaternion* category, and the vocabulary of pure and non-pure is used throughout."),
])

patch('annihilators-of-the-quaternion-algebra.md', [
 ("the left and the right multiplication of the algebra (*One-Sided Operators on the General Plain\nAlgebra of Quaternions*), and",
  "the left and the right multiplication of the algebra (*One-Sided Operators on the Quaternion Algebra*), and"),
])

patch('introduction-to-the-antisymmetric-plain-algebra-of-quaternioid.md', [
 ("antisymmetric half carries no square and no norm; this is why the block is its own product and not a\nreading of the plain one.",
  "antisymmetric half carries no square and no norm; this is why the block is its own product and not a\nreading of the algebra product."),
 ("The space $\\mathbb{H}$ carries six bilinear products, set out in *The 6 Products of the Quaternioid $\\mathbb{R}$ Space* and structured in *The Algebraic Structures over the Quaternioid $\\mathbb{R}$ Space*: the two general products, their symmetrisations and their antisymmetrisations. The block of\nthis article is the antisymmetrisation of the plain product. The block of this article is the antisymmetrisation of the algebra product, the one **alternating** structure of the category.",
  "The space $\\mathbb{H}$ carries, beside the algebra product of the *Quaternions* category, the companion products set out in *The 6 Products of the Quaternioid $\\mathbb{R}$ Space* and named in *The Algebraic Structures over the Quaternioid $\\mathbb{R}$ Space*. The block of this article is the antisymmetrisation of the algebra product, the one **alternating** structure of the category."),
])

patch('the-two-general-products-and-the-reason-there-are-only-two.md', [
 ("| general | $\\mathrm{GPA}$, $\\tilde p\\tilde q$, the *Quaternions* algebra product |",
  "| general | $\\tilde p\\tilde q$, the *Quaternions* algebra product |"),
])
print('fix_review done')
