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

patch('introduction-to-the-symmetric-plain-algebra-of-quaternioid.md', [
 ("The reading is one of the six operations of *The 6 Products of the Quaternioid Real Space*, where the operation is named $\\mathrm{SPA}$; it is the one commutative unital Jordan product of the six, and its structure among them is *The Algebraic Structures over the Quaternioid $\\mathbb{R}$ Space*.",
  "The reading is one of the companion products of *The 6 Products of the Quaternioid Real Space*, where the operation is named $\\mathrm{SPA}$; it is the one commutative unital Jordan product among them, and its structure is *The Algebraic Structures over the Quaternioid $\\mathbb{R}$ Space*."),
 ("the reconstruction, and the placement of the block among the six.", "the reconstruction, and the placement of the block among the companion products."),
 ("**Remark (the identity is what singles out the block).** Of the two symmetric parts of the six operations of *The Algebraic Structures over the Quaternioid $\\mathbb{R}$ Space*, exactly one satisfies the Jordan identity, and of the two antisymmetric parts exactly one satisfies the Jacobi identity; both sit in the plain row, $\\mathrm{SPA}$ being the Jordan product and $\\mathrm{APA}$ the Lie product. The symmetric quaternionic product is commutative but fails the Jordan identity, with the witness $x=(-3,-3,3,2)$, $y=(2,-3,1,2)$, where the two sides are $310e_0$ and $-186e_0$; it is scalar valued and has no unit, so the two symmetric parts are separated by the identity.",
  "**Remark (the identity is what singles out the block).** Of the two symmetrisations the space carries, exactly one satisfies the Jordan identity, and of the two antisymmetrisations exactly one satisfies the Jacobi identity; both sit in the plain row, $\\mathrm{SPA}$ being the Jordan product and $\\mathrm{APA}$ the Lie product. The scalar-valued symmetrisation of the quaternionic product is commutative but fails the Jordan identity; it is scalar valued and has no unit, so the two symmetric parts are separated by the identity."),
 ("- *The 6 Products of the Quaternioid Real Space*, for the six operations, their names and their table.",
  "- *The 6 Products of the Quaternioid Real Space*, for the companion products, their names and their table."),
 ("- *The Algebraic Structures over the Quaternioid $\\mathbb{R}$ Space*, for the structures the six define and the two laws that separate them.",
  "- *The Algebraic Structures over the Quaternioid $\\mathbb{R}$ Space*, for the structures the companion products define and the two laws that separate them."),
])

patch('the-specificities-of-the-symmetric-plain-algebra-of-quaternioid.md', [
 ("It closes with the isolation of the block among the six operations of the chapter.",
  "It closes with the isolation of the block among the companion products of the chapter."),
 ("The names of the six operations are those of *The Algebraic Structures over the Quaternioid $\\mathbb{R}$ Space*.",
  "The names of the companion products are those of *The Algebraic Structures over the Quaternioid $\\mathbb{R}$ Space*."),
 ("it is the spin factor of *Jordan Algebras*, §*Spin Factors*, and it is **not one of the six operations** of the menu. So **the block is the only commutative unital Jordan algebra of the six, and the owner of the definite norm, but its product is not formally real**, the sum-of-squares condition for the product being carried by two operations that are not commutative Jordan products.",
  "it is the spin factor of *Jordan Algebras*, §*Spin Factors*, and it is **not one of the companion products** of the menu. So **the block is the only commutative unital Jordan algebra among the companion products, and the owner of the definite norm, but its product is not formally real**, the sum-of-squares condition for the product being carried by the general quaternionic product, which is not a commutative Jordan product."),
 ("- *The 6 Products of the Quaternioid Real Space* and *The Algebraic Structures over the Quaternioid $\\mathbb{R}$ Space*, for the six operations and their laws.",
  "- *The 6 Products of the Quaternioid Real Space* and *The Algebraic Structures over the Quaternioid $\\mathbb{R}$ Space*, for the companion products and their laws."),
])

patch('introduction-to-the-antisymmetric-plain-algebra-of-quaternioid.md', [
 ("| $\\mathrm{GPA}=\\mathrm{SPA}+\\mathrm{APA}$ | the reconstruction of the plain product from its two halves |",
  "| $\\tilde p\\tilde q=\\tilde p\\bullet\\tilde q+\\tilde p\\wedge\\tilde q$ | the reconstruction of the algebra product from its two halves |"),
 ("and *The Algebraic Structures over the Quaternioid $\\mathbb{R}$ Space*, for the six products and their names.",
  "and *The Algebraic Structures over the Quaternioid $\\mathbb{R}$ Space*, for the companion products and their names."),
])

patch('the-specificities-of-the-antisymmetric-plain-algebra-of-quaternioid.md', [
 ("the block out among the six products of the space:", "the block out among the companion products of the space:"),
 ("The block is the **only** product of the six that is at once alternating and Jacobi; the two",
  "The block is the **only** companion product that is at once alternating and Jacobi; the two"),
 ("the Jacobi identity is a Lie bracket, so $(\\mathbb{H},\\times)$ is a Lie algebra. Among the six",
  "the Jacobi identity is a Lie bracket, so $(\\mathbb{H},\\times)$ is a Lie algebra. Among the companion"),
 ("## The Isolation among the Six", "## The Isolation among the Companion Products"),
 ("The antisymmetric plain block is isolated among the six products by a single pair of identities: it is",
  "The antisymmetric plain block is isolated among the companion products by a single pair of identities: it is"),
 ("| $\\mathrm{APA}$ | the unique Lie structure of the six |", "| $\\mathrm{APA}$ | the unique Lie structure of the companion products |"),
])

patch('introduction-to-the-general-quaternionic-algebra-of-quaternioid.md', [
 ("the reading on the distinguished subspaces is *The Remarkable Subspaces under the Six Operations*, below this article in this category,",
  "the reading on the distinguished subspaces is *Remarkable Subspaces and the Two General Products*, below this article in this category,"),
])

patch('the-two-general-products-and-the-reason-there-are-only-two.md', [
 ("The quaternion algebra $\\mathbb{H}$ carries six algebraic structures, and all six descend from two multiplications. This article states the general construction that produces those multiplications, proves that exactly two general products arise over $\\mathbb{R}$, and reads the six structures the two generate.",
  "The quaternion algebra $\\mathbb{H}$ carries, besides the algebra product of the *Quaternions* category, the companion products of this category, and they all descend from two multiplications. This article states the general construction that produces those multiplications, proves that exactly two general products arise over $\\mathbb{R}$, and reads the companion products the two generate."),
 ("the six structures and their names are *The Algebraic Structures over the Quaternioid $\\mathbb{R}$ Space*; this article re-derives none of them. What it owns is the construction, the count, and the passage from the two general products to the six structures.",
  "the three companion structures and their names are *The Algebraic Structures over the Quaternioid $\\mathbb{R}$ Space*; this article re-derives none of them. What it owns is the construction, the count, and the passage from the two general products to the companion products."),
 ("## The Six Structures the Two Products Generate", "## The Companion Structures the Two Products Generate"),
 ("The two general products and the four halves are the six products of the chapter, and the six products carry the six structures.",
  "The two general products and their four halves are the six products of the chapter, and three of them — the symmetric plain, the antisymmetric plain and the general quaternionic — carry the companion structures."),
 ("**Theorem (the two general products generate the six structures, and no more).** The split of the two general products under the interchange of their slots produces exactly four halves, the two general products together with the four halves are six distinct products, and every structure of the chapter is one of the six.",
  "**Theorem (the two general products generate the companion products, and no more).** The split of the two general products under the interchange of their slots produces exactly four halves, the two general products together with the four halves are six distinct products, and the three companion structures of the category are the symmetric plain, the antisymmetric plain and the general quaternionic one."),
 ("Hence the split produces no seventh product, and the six structures are exactly the two general products and their halves.",
  "Hence the split produces no seventh product, and no companion product is missed."),
 ("the plain symmetric half $\\mathrm{SPA}$ is a Jordan algebra, the quaternionic symmetric half $\\mathrm{SQA}$ is not.",
  "the plain symmetric half $\\mathrm{SPA}$ is a Jordan algebra, the scalar-valued symmetrisation of the quaternionic product $N(\\tilde p,\\tilde q)e_0$ is not."),
 ("The reason there are two general products is the reason there are six structures. The algebra has one nontrivial conjugation and the base field none, so the slot construction yields two general products; each general product yields exactly two halves; two general products therefore yield four halves and six structures in all.",
  "The reason there are two general products is the reason the category keeps three companion structures. The algebra has one nontrivial conjugation and the base field none, so the slot construction yields two general products; each general product yields exactly two halves; two general products therefore yield four halves, of which three carry the companion structures."),
 ("The two general products and the four halves are six distinct products, carrying the six structures $\\mathrm{GPA}$, $\\mathrm{GQA}$, $\\mathrm{SPA}$, $\\mathrm{SQA}$, $\\mathrm{APA}$, $\\mathrm{AQA}$, indexed by the family and the half;",
  "The two general products and the four halves are six distinct products; three of them carry the companion structures, $\\mathrm{SPA}$, $\\mathrm{APA}$ and $\\mathrm{GQA}$, indexed by the family and the half;"),
 ("| $\\mathrm{GPA},\\mathrm{GQA},\\mathrm{SPA},\\mathrm{SQA},\\mathrm{APA},\\mathrm{AQA}$ | the six structures, one to a cell of the family-and-half grid |",
  "| $\\mathrm{SPA},\\mathrm{APA},\\mathrm{GQA}$ | the three companion structures of the category |"),
 ("for the six names and the law table.", "for the names and the law table."),
 ("""| general | $\\mathrm{GPA}$, $\\tilde p\\tilde q$ | $\\mathrm{GQA}$, $\\tilde p^{\\natural}\\tilde q$ |
| symmetric | $\\mathrm{SPA}$, $\\tilde p\\bullet\\tilde q$ | $\\mathrm{SQA}$, $N(\\tilde p,\\tilde q)e_0$ |
| antisymmetric | $\\mathrm{APA}$, $\\tilde p\\wedge\\tilde q$ | $\\mathrm{AQA}$, $\\tilde p\\wedge^{\\natural}\\tilde q$ |""",
  """| general | $\\mathrm{GPA}$, $\\tilde p\\tilde q$, the *Quaternions* algebra product | $\\mathrm{GQA}$, $\\tilde p^{\\natural}\\tilde q$ |
| symmetric | $\\mathrm{SPA}$, $\\tilde p\\bullet\\tilde q$ | $N(\\tilde p,\\tilde q)e_0$, the scalar-valued symmetrisation |
| antisymmetric | $\\mathrm{APA}$, $\\tilde p\\wedge\\tilde q$ | $\\tilde p\\wedge^{\\natural}\\tilde q$, the quaternionic cross product |"""),
 ("below this article in this category, for the first of the element theories read across the six.",
  "below this article in this category, for the first of the element theories read across the companion products."),
 ("$\\mathrm{GPA}$, $\\tilde p\\tilde q$, the *Quaternions* algebra product",
  "$\\tilde p\\tilde q$, the *Quaternions* algebra product"),
])
print('big3 done')
