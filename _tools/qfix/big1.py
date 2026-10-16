import os
AD = '/home/hp/Documents/1_Doc/Projects/ai-research/ai-research-unit/articles_maths'

def patch(fn, pairs):
    p = os.path.join(AD, fn)
    t = open(p, encoding='utf-8').read()
    for a, b in pairs:
        if a in t:
            t = t.replace(a, b)
        else:
            print('MISS', fn, '::', a[:70].replace('\n', '\\n'))
    open(p, 'w', encoding='utf-8').write(t)

# ---- GQA intro ----
patch('introduction-to-the-general-quaternionic-algebra-of-quaternioid.md', [
 ("The real space $\\mathbb{H}$ carries six operations, set out in *The 6 Products of the Quaternioid Real Space* and structured in *The Algebraic Structures over the Quaternioid $\\mathbb{R}$ Space*.",
  "The real space $\\mathbb{H}$ carries, beside the algebra product of the *Quaternions* category, the companion products set out in *The 6 Products of the Quaternioid Real Space* and named in *The Algebraic Structures over the Quaternioid $\\mathbb{R}$ Space*."),
 ("It then places the algebra among the six operations of the space.",
  "It then places the algebra among the companion structures of the space."),
 ("The real space $\\mathbb{H}$ carries six operations (*The 6 Products of the Quaternioid Real Space*) and they organise into six algebraic structures (*The Algebraic Structures over the Quaternioid $\\mathbb{R}$ Space*). This article's product is one of the two bilinear ones. The other is the plain product $\\tilde p\\tilde q$, the multiplication of the general plain algebra of the same space, and it is the only associative and the only unital one of the six.",
  "The real space $\\mathbb{H}$ carries, beside the algebra product of the *Quaternions* category, the companion products of *The 6 Products of the Quaternioid Real Space*, which the category organises into three structures in *The Algebraic Structures over the Quaternioid $\\mathbb{R}$ Space*. This article's product is one of the two bilinear ones; the other is the algebra product $\\tilde p\\tilde q$, the multiplication of the quaternion algebra, and it is the only associative and the only unital one of them."),
 ("The remaining operations of the six are the companions of the two bilinear laws:",
  "The remaining companion products are the companions of the two bilinear laws:"),
])

# ---- GQA specificities ----
patch('the-specificities-of-the-general-quaternionic-algebra-of-quaternioid.md', [
 ("among the six algebraic structures of the space", "among the three companion structures of the space"),
 ("The last section records the position of the algebra among the six.",
  "The last section records the position of the algebra among the three companion structures."),
 ("The plain algebra is the only one of the six with a two-sided unit; the two antisymmetric products and the two symmetrised ones have none, so unitality is rare in the list and *one-sided* unitality is this product's alone.",
  "The symmetric plain algebra is the only one of the three companion structures with a two-sided unit; the antisymmetric plain structure has none, so unitality is rare in the list and *one-sided* unitality is this product's alone."),
 ("Among the six algebraic structures of the quaternion real space, the general quaternionic algebra is the only one that is left-unital and not right-unital;",
  "Among the three companion structures of the quaternion real space, the general quaternionic algebra is the only one that is left-unital and not right-unital;"),
 ("The companions are excluded by the shared list of facts of the chapter: the two symmetrised products have zero divisors, the two antisymmetrised products are alternating with every element square-zero, and the plain product is associative with a two-sided unit.",
  "The companions are excluded by the shared list of facts: the symmetric plain product has zero divisors, the antisymmetric plain product is alternating with every element square-zero, and the algebra product is associative with a two-sided unit."),
 ("""| structure | product | character |
|---|---|---|
| general plain (GPA) | $\\tilde p\\tilde q$ | associative, two-sided unit, division |
| symmetric plain (SPA) | $\\tfrac12(\\tilde p\\tilde q+\\tilde q\\tilde p)$ | commutative, Jordan, no unit, zero divisors |
| antisymmetric plain (APA) | $\\tfrac12(\\tilde p\\tilde q-\\tilde q\\tilde p)$ | alternating, Lie, no unit |
| general quaternionic (GQA) | $\\tilde p^{\\natural}\\tilde q$ | not associative, left unit only, division |
| symmetric quaternionic (SQA) | $\\tfrac12(\\tilde p^{\\natural}\\tilde q+\\tilde q^{\\natural}\\tilde p)$ | commutative, scalar-valued, no unit, zero divisors |
| antisymmetric quaternionic (AQA) | $\\tfrac12(\\tilde p^{\\natural}\\tilde q-\\tilde q^{\\natural}\\tilde p)$ | alternating, Jacobi fails |""",
  """| structure | product | character |
|---|---|---|
| symmetric plain (SPA) | $\\tfrac12(\\tilde p\\tilde q+\\tilde q\\tilde p)$ | commutative, Jordan, no unit, zero divisors |
| antisymmetric plain (APA) | $\\tfrac12(\\tilde p\\tilde q-\\tilde q\\tilde p)$ | alternating, Lie, no unit |
| general quaternionic (GQA) | $\\tilde p^{\\natural}\\tilde q$ | not associative, left unit only, division |"""),
 ("it is reproduced here for the relation only. The symmetric and antisymmetric quaternionic blocks are below this article in this category, as is the synthesis.",
  "it is reproduced here for the relation only."),
 ("Among the six structures of the space it is the one left-unital, non-associative, zero-divisor-free member.",
  "Among the three companion structures of the space it is the one left-unital, non-associative, zero-divisor-free member."),
])
print('done part 1')
