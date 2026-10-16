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
 ("## The Reconstruction and the Six", "## The Reconstruction"),
 ("### The Reconstruction $\\mathrm{GPA}=\\mathrm{SPA}+\\mathrm{APA}$", "### The Reconstruction of the Algebra Product"),
 ("*Proof.* Adding the two halves restores the product, and the antisymmetric half of the plain product is the cross product of the two vector parts, as *Introduction to the Antisymmetric Plain Algebra of Quaternions*, below this article in this category, develops. The identity is one of the two row reconstructions $\\mathrm{GPA}=\\mathrm{SPA}+\\mathrm{APA}$ and $\\mathrm{GQA}=\\mathrm{SQA}+\\mathrm{AQA}$ of *The 6 Products of the Quaternioid Real Space*.",
  "*Proof.* Adding the two halves restores the product, and the antisymmetric half of the algebra product is the cross product of the two vector parts, as *Introduction to the Antisymmetric Plain Algebra*, below this article in this category, develops. The identity is the plain row reconstruction $\\tilde p\\tilde q=\\tilde p\\bullet\\tilde q+\\tilde p\\wedge\\tilde q$ of *The 6 Products of the Quaternioid Real Space*."),
 ("The plain row is the one whose symmetric part is the Jordan product and whose antisymmetric part is the Lie product; the companion block that reads the antisymmetric half is *Introduction to the Antisymmetric Plain Algebra of Quaternions*, below this article in this category.",
  "The algebra product is the one whose symmetric part is the Jordan product and whose antisymmetric part is the Lie product; the block that reads the antisymmetric half is *Introduction to the Antisymmetric Plain Algebra*, below this article in this category."),
 ("### The Placement among the Six", "### The Placement among the Companion Products"),
 ("The name $\\mathrm{SPA}$ is read with the code of *The Algebraic Structures over the Quaternioid $\\mathbb{R}$ Space*: the first letter $\\mathrm{S}$ says that the operation is the symmetric part of the row, the second letter $\\mathrm{P}$ that it comes from the plain product, and the third letter $\\mathrm{A}$ that it is a real bilinear algebra product.",
  "The name $\\mathrm{SPA}$ is read with the code of *The Algebraic Structures over the Quaternioid $\\mathbb{R}$ Space*: the first letter $\\mathrm{S}$ says that the operation is a symmetric part, the second letter $\\mathrm{P}$ that it comes from the plain product, and the third letter $\\mathrm{A}$ that it is a real bilinear algebra product."),
 ("""| the row | general | symmetric | antisymmetric |
|---|---|---|---|
| the plain algebra | $\\mathrm{GPA}$ | $\\mathrm{SPA}$ | $\\mathrm{APA}$ |
| the quaternionic algebra | $\\mathrm{GQA}$ | $\\mathrm{SQA}$ | $\\mathrm{AQA}$ |""",
  """| the algebra product | symmetric half | antisymmetric half |
|---|---|---|
| $\\tilde p\\tilde q$ | $\\mathrm{SPA}$ | $\\mathrm{APA}$ |"""),
 ("**Remark (the place of the block).** The block $\\mathrm{SPA}$ is the symmetrisation of the associative product $\\mathrm{GPA}$, and the companion block $\\mathrm{SQA}$ is the symmetrisation of the quaternionic product $\\mathrm{GQA}$; the antisymmetric parts $\\mathrm{APA}$ and $\\mathrm{AQA}$ are the two Lie candidates. Two of the six operations pass the identity of a classical nonassociative algebra, both in the plain row: $\\mathrm{APA}$ is the Lie product and $\\mathrm{SPA}$ the Jordan product. **Of the six operations, $\\mathrm{SPA}$ is the commutative unital Jordan product; it is the only one of the two symmetric parts that satisfies the Jordan identity, and it is the block whose generic norm is positive definite** — the symmetric quaternionic product is commutative, scalar valued and without a unit, and its square of $e_1$ is $+e_0$, not $-e_0$. The laws are owned by *The 6 Products of the Quaternioid Real Space* and the names by *The Algebraic Structures over the Quaternioid $\\mathbb{R}$ Space*.",
  "**Remark (the place of the block).** The block $\\mathrm{SPA}$ is the symmetrisation of the algebra product $\\tilde p\\tilde q$, whose antisymmetrisation is $\\mathrm{APA}$; the two halves carry the two classical nonassociative laws, $\\mathrm{SPA}$ the Jordan product and $\\mathrm{APA}$ the Lie product. **$\\mathrm{SPA}$ is the commutative unital Jordan product of the space**, and it is the block whose generic norm is positive definite. The laws are owned by *The 6 Products of the Quaternioid Real Space* and the names by *The Algebraic Structures over the Quaternioid $\\mathbb{R}$ Space*."),
 ("and it is the one Jordan product of the six operations.", "and it is the one Jordan product among the companion products."),
 ("The plain product reconstructs as $\\mathrm{GPA}=\\mathrm{SPA}+\\mathrm{APA}$, the symmetrisation of an associative product in the plain row of *The 6 Products of the Quaternioid Real Space*.",
  "The algebra product reconstructs as $\\tilde p\\tilde q=\\tilde p\\bullet\\tilde q+\\tilde p\\wedge\\tilde q$, the symmetrisation of an associative product, read in *The 6 Products of the Quaternioid Real Space*."),
 ("| $\\mathrm{SPA}$ | the name of the operation among the six |", "| $\\mathrm{SPA}$ | the name of the operation among the companion products |"),
 ("| $\\mathrm{GPA}=\\mathrm{SPA}+\\mathrm{APA}$ | the reconstruction of the plain product |", "| $\\tilde p\\tilde q=\\tilde p\\bullet\\tilde q+\\tilde p\\wedge\\tilde q$ | the reconstruction of the algebra product |"),
])

patch('the-specificities-of-the-symmetric-plain-algebra-of-quaternioid.md', [
 ("**Remark (which operation carries the sum-of-squares condition of the product).** The sum-of-squares condition for the product is met by the **general quaternionic** and the **symmetric quaternionic** products, whose squares are $|\\tilde x|^2e_0$ and are non-negative; but neither is a commutative Jordan product, $\\mathrm{GQA}$ being non-commutative and $\\mathrm{SQA}$ failing the Jordan identity, so neither carries the formal reality of a Jordan algebra.",
  "**Remark (which operation carries the sum-of-squares condition of the product).** The sum-of-squares condition for the product is met by the **general quaternionic** product, whose square is $|\\tilde x|^2e_0$ and is non-negative; but it is not a commutative Jordan product, $\\mathrm{GQA}$ being non-commutative, so it does not carry the formal reality of a Jordan algebra."),
 ("## The Isolation of the Block among the Six", "## The Isolation of the Block among the Companion Products"),
 ("Among the six operations of *The 6 Products of the Quaternioid Real Space*, the symmetric plain product is the unique one that is **commutative, unital and Jordan**, and it is the unique one whose algebra is a commutative unital Jordan algebra.",
  "Among the companion products of *The 6 Products of the Quaternioid Real Space*, the symmetric plain product is the unique one that is **commutative, unital and Jordan**, and it is the unique one whose algebra is a commutative unital Jordan algebra."),
 ("*Proof.* The plain product $\\mathrm{GPA}$ is associative and unital but not commutative; the antisymmetric plain product $\\mathrm{APA}$ is alternating, has no unit and is not commutative; the general quaternionic product $\\mathrm{GQA}$ is not commutative and only left unital; the symmetric quaternionic product $\\mathrm{SQA}$ is commutative, scalar valued and without a unit, and it fails the Jordan identity; the antisymmetric quaternionic product $\\mathrm{AQA}$ is alternating and has no unit. So $\\mathrm{SPA}$ is the only one of the six with all three properties. **The three properties single out the block, but they do not make its product formally real**: the block is a Jordan algebra whose underlying product is not formally real, and the two operations whose squares are non-negative, $\\mathrm{GQA}$ and $\\mathrm{SQA}$, are not commutative Jordan products.",
  "*Proof.* The algebra product $\\tilde p\\tilde q$ is associative and unital but not commutative; the antisymmetric plain product $\\mathrm{APA}$ is alternating, has no unit and is not commutative; the general quaternionic product $\\mathrm{GQA}$ is not commutative and only left unital. So $\\mathrm{SPA}$ is the only one of the companion products with all three properties. **The three properties single out the block, but they do not make its product formally real**: the block is a Jordan algebra whose underlying product is not formally real, and the operation whose square is non-negative, $\\mathrm{GQA}$, is not a commutative Jordan product."),
 ("**Remark (the three generating operations).** The isolation is read off three operations and no more: **commutativity** separates the plain row from the general products and the quaternionic row; the **unit** separates the two symmetric parts, which have it and do not respectively; and the **Jordan identity**, which $\\mathrm{SQA}$ alone of the commutative candidates fails, completes the criterion. The three together single out $\\mathrm{SPA}$; each alone fails to, because the antisymmetric parts are also Jordan-vacuous and the plain product is also unital.",
  "**Remark (the three generating operations).** The isolation is read off three operations and no more: **commutativity** separates the block from the algebra product and the general quaternionic product; the **unit** separates it from the structures without a two-sided unit; and the **Jordan identity** completes the criterion. The three together single out $\\mathrm{SPA}$; each alone fails to."),
 ("| the six | $\\mathrm{GPA},\\mathrm{SPA},\\mathrm{APA},\\mathrm{GQA},\\mathrm{SQA},\\mathrm{AQA}$ |",
  "| the companion products | $\\mathrm{SPA},\\mathrm{APA},\\mathrm{GQA}$ |"),
 ("Among the six operations the block is the unique one that is commutative, unital and Jordan, and the criterion is read off those three operations.",
  "Among the companion products the block is the unique one that is commutative, unital and Jordan, and the criterion is read off those three operations."),
])
print('big2 part 1 done')

patch('introduction-to-the-antisymmetric-plain-algebra-of-quaternioid.md', [
 ("**Proposition (the reconstruction).** The plain product is the sum of its two halves,",
  "**Proposition (the reconstruction).** The algebra product is the sum of its two halves,"),
 ("$$\n\\mathrm{GPA}=\\mathrm{SPA}+\\mathrm{APA},\\qquad\n\\tilde p\\tilde q=\\tilde p\\bullet\\tilde q+\\tilde p\\times\\tilde q ,\n$$",
  "$$\n\\tilde p\\tilde q=\\tilde p\\bullet\\tilde q+\\tilde p\\times\\tilde q ,\n$$"),
 ("## The Placement of the Block among the Six", "## The Placement of the Block among the Companion Products"),
 ("It is the one **alternating** product of\nthe plain row; the other antisymmetric operation of the six, the antisymmetrisation of the\nquaternionic product, is *Introduction to the Antisymmetric Quaternionic Algebra of Quaternions*,\nbelow this article in this category.",
  "The block of this article is the antisymmetrisation of the algebra product, the one **alternating** structure of the category."),
 ("The\nplain product is reconstructed as $\\mathrm{GPA}=\\mathrm{SPA}+\\mathrm{APA}$, and the square map sees\nonly the symmetric half",
  "The\nalgebra product is reconstructed as $\\tilde p\\tilde q=\\tilde p\\bullet\\tilde q+\\tilde p\\wedge\\tilde q$, and the square map sees\nonly the symmetric half"),
 ("Among the six products the block\nis one of the two antisymmetrisations, the plain one; the quaternionic one fails the Jacobi identity\nand is the neighbouring block.",
  "Among the companion products of the category the block is the antisymmetrisation of the algebra product, the Lie bracket of the space."),
])

patch('the-specificities-of-the-antisymmetric-plain-algebra-of-quaternioid.md', [
 ("""| identity | $\\mathrm{GPA}$ | $\\mathrm{SPA}$ | $\\mathrm{APA}$ | $\\mathrm{GQA}$ | $\\mathrm{SQA}$ | $\\mathrm{AQA}$ |
|---|---|---|---|---|---|---|
| alternating | no | no | **yes** | no | no | yes |
| flexible | yes | yes | yes | no | yes | yes |
| power-associative | yes | yes | yes | no | yes | yes |
| Jordan identity | yes | yes | yes | yes | no | yes |
| associative | yes | no | no | no | no | no |
| Jacobi identity | no | no | **yes** | no | no | no |""",
  """| identity | $\\mathrm{SPA}$ | $\\mathrm{APA}$ | $\\mathrm{GQA}$ |
|---|---|---|---|
| alternating | no | **yes** | no |
| flexible | yes | yes | no |
| power-associative | yes | yes | no |
| Jordan identity | yes | yes | yes |
| associative | no | no | no |
| Jacobi identity | no | **yes** | no |"""),
 ("First, $\\mathrm{APA}$ is the\n**only** structure that is both alternating and Jacobi, hence the only Lie structure of the six, and\nit is the only one that is alternating together with $\\mathrm{AQA}$. Second, the block has no unit\nwhile the general plain structure does, is not associative while the general plain structure is, and\nfails the norm while the plain and symmetric structures carry one. The block is therefore\n$\\mathrm{APA}$, the first of the two antisymmetric structures in the order of the catalogue, paired\nwith the antisymmetric quaternionic structure and separated from it by the Jacobi identity alone.",
  "First, $\\mathrm{APA}$ is the\n**only** structure that is both alternating and Jacobi, hence the only Lie structure of the companion\nproducts. Second, the block has no unit while the symmetric plain structure does, is not associative,\nand fails the norm while the symmetric plain structure carries one. The block is therefore\n$\\mathrm{APA}$, the Lie bracket of the space."),
])

patch('the-antisymmetric-plain-algebra-in-the-2x2-matrix-element-representation-of-quaternioid.md', [
 ("The model exhibits the split $\\mathrm{GPA}=\\mathrm{SPA}+\\mathrm{APA}$ as the identity",
  "The model exhibits the split $\\tilde p\\tilde q=\\tilde p\\bullet\\tilde q+\\tilde p\\wedge\\tilde q$ as the identity"),
])

patch('the-2-algebraic-norms-over-the-quaternioid-r-space.md', [
 ("in the GPA block below.", "in the *Quaternions* category."),
 ("*Norm and Invertibility in the General Plain Algebra*, in the *Quaternions* category.",
  "*Norm and Invertibility in the Quaternion Algebra*, in the *Quaternions* category."),
])

patch('the-two-general-products-and-operators.md', [
 ("in the GPA block below", "in the *Quaternions* category"),
 ("*One-Sided Operators on the General Plain Algebra of Quaternions*",
  "*One-Sided Operators on the Quaternion Algebra* (`articles_maths/one-sided-operators-on-the-quaternion-algebra.md`)"),
 ("*The Enveloping Operator Algebra of the General Plain Algebra and the Bi-module Structure*",
  "*The Enveloping Operator Algebra of the Quaternion Algebra and the Bi-module Structure* (`articles_maths/the-enveloping-operator-algebra-of-the-quaternion-algebra-and-the-bi-module-structure.md`)"),
])

patch('the-symmetrised-quaternionic-product-and-the-hermitian-subspace-of-quaternioid.md', [
 ("It is the multiplication of the symmetric quaternionic algebra of the chapter, and this article does **not** develop that block: the commutative scalar-valued algebra, its zero divisors, its specificities and its matrix models are the articles of *Quaternions as a Symmetric Quaternionic Algebra (SQA) over $\\mathbb{R}$*, all below this article in this category, and the introduction of the block is *Introduction to the Symmetric Quaternionic Algebra of Quaternions*, below this article in this category.",
  "It is the symmetrisation of the general quaternionic product, and the commutative scalar-valued rule it defines is not a structure of this category: this article collects what the category keeps of it, the hermitian subspace and the trace form, and cites nothing further."),
])
print('big2 done')

