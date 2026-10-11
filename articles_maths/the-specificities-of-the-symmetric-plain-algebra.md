# __The Specificities of the Symmetric Plain Algebra__

## Introduction

Of the twelve algebraic structures that the complex space $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries, exactly one makes it a **Jordan algebra**: the **symmetric plain product** $\tilde P\bullet\tilde Q=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ of *Introduction to the Symmetric Plain Algebra of Biquaternions*, the multiplication named $\mathrm{SPA}$ in *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*. Every structural result of the block belongs to it alone — the generic trace and norm, the quadratic representation, the cubic Peirce identity and the Jordan Peirce decomposition — and this article states the exact reason, in one pair of laws, and then separates the twelve.

The reason is not commutativity as such but the conjunction of commutativity with the **Jordan identity**. The sentence "an element satisfies a generic minimal polynomial of degree two" is a statement about the multiplication operator $L^{\circ}_{\tilde X}$, and it is the **operator identity**

$$
L^{\circ}_{\tilde X}\circ L^{\circ}_{\tilde X^{\circ2}}=L^{\circ}_{\tilde X^{\circ2}}\circ L^{\circ}_{\tilde X}\qquad\text{for every }\tilde X
$$

that carries it; for a commutative product this identity is exactly the Jordan identity, and among the twelve the symmetric plain product is the only commutative structure that satisfies it. Each of the eleven others is built from the plain product by twisting a slot with a conjugation or by (anti)symmetrising, and the four general products are not commutative, the two antisymmetric non-alternating parts fail the identity, the symmetric quaternionic product is commutative and fails the identity, and the two symmetric sesquilinear products are conjugate-commutative and fail it, so the failure is a structural consequence of how the twelve are made and not the accident of one witness.

The consequence is the point of the article. Only in the symmetric plain algebra are the generic trace and norm, the quadratic representation, the cubic Peirce identity and the Jordan Peirce decomposition available as **theorems**. The identity itself holds elsewhere — at every element of the associative general plain product, at every element of the general quaternionic product, whose square is central, and vacuously for the two alternating antisymmetrisations — but no other structure carries the theory, because the criterion is the conjunction of the identity with commutativity and none of those four structures is commutative. The one genuine border case is the symmetric quaternionic product, whose product is commutative but whose operators fail the identity; it is *The Specificities of the Symmetric Quaternionic Algebra* and is stated here only as the boundary of the criterion.

**Placement.** The article is the closing entry of the *Specific Theory* section of the block, after *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra* and after the Common Theory articles *Norm and Invertibility in the Symmetric Plain Algebra*, *Zero Divisors of the Symmetric Plain Algebra*, *Square Roots of Minus One, Zero and Plus One in the Symmetric Plain Algebra*, *Square Roots of a General Element in the Symmetric Plain Algebra*, *Idempotents of the Symmetric Plain Algebra* and *Nilpotents of the Symmetric Plain Algebra*, whose results it reads back as consequences of one law. It is the twin of *The Specificities of the General Plain Algebra*, which states left alternativity as the criterion of the parent product and proves that the symmetric plain product fails it; the two are read together, and the pair of criteria is the reason the block and its parent share the square and share nothing of the operator theory.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ with $e_1e_2=e_3$ and central scalar imaginary $i$. The product written $\circ$ is a generic one, its identity stated at each use, and $\tilde X^{\circ2}=\tilde X\circ\tilde X$. The **left multiplication** of a product $\circ$ by $\tilde X$ is $L^{\circ}_{\tilde X}:\tilde Y\mapsto\tilde X\circ\tilde Y$, and $\mathrm{id}$ is the identity operator. An **idempotent** is an element equal to its square, a **projector** is an idempotent operator; the two levels are never interchanged. The twelve structures are coded as in *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*: the four rows $\mathrm{G/A}$ with $\mathrm P$ or $\mathrm Q$ and $\mathrm A$ or $\mathrm S$, as $\mathrm{GPA},\mathrm{SPA},\mathrm{APA}$ and so on.

## The Criterion

**Definition (the Jordan product law).** A product $\circ$ satisfies the **Jordan product law**, and is called a **Jordan product**, when it is **commutative**,

$$
\tilde X\circ\tilde Y=\tilde Y\circ\tilde X\qquad\text{for all }\tilde X,\tilde Y,
$$

and satisfies the **Jordan identity**

$$
(\tilde X^{\circ2}\circ\tilde Y)\circ\tilde X=\tilde X^{\circ2}\circ(\tilde Y\circ\tilde X)\qquad\text{for all }\tilde X,\tilde Y.
$$

A commutative algebra whose product is a Jordan product is a **Jordan algebra**.

**Theorem (the criterion).** For a commutative product the Jordan identity is equivalent to the operator identity

$$
L^{\circ}_{\tilde X}\circ L^{\circ}_{\tilde X^{\circ2}}=L^{\circ}_{\tilde X^{\circ2}}\circ L^{\circ}_{\tilde X}\qquad\text{for every }\tilde X .
$$

*Proof.* Suppose first the Jordan identity. Write it as $(\tilde X^{\circ2}\circ\tilde Y)\circ\tilde X=\tilde X^{\circ2}\circ(\tilde Y\circ\tilde X)$ and use commutativity twice, $(\tilde X^{\circ2}\circ\tilde Y)\circ\tilde X=\tilde X\circ(\tilde X^{\circ2}\circ\tilde Y)$ and $\tilde Y\circ\tilde X=\tilde X\circ\tilde Y$; the identity becomes $\tilde X\circ(\tilde X^{\circ2}\circ\tilde Y)=\tilde X^{\circ2}\circ(\tilde X\circ\tilde Y)$, that is $L^{\circ}_{\tilde X}L^{\circ}_{\tilde X^{\circ2}}\tilde Y=L^{\circ}_{\tilde X^{\circ2}}L^{\circ}_{\tilde X}\tilde Y$ for every $\tilde Y$, which is the operator identity. Conversely the operator identity, evaluated at $\tilde Y$ and read with the two commutativities in reverse, is the Jordan identity.

**Corollary (the block satisfies the law).** The symmetric plain product is commutative and satisfies the Jordan identity, so it is a Jordan product, and its algebra is a commutative unital Jordan algebra over $\mathbb{C}$:

$$
(\tilde P\bullet\tilde Q)\bullet(\tilde P\bullet\tilde P)=\tilde P\bullet\bigl(\tilde Q\bullet(\tilde P\bullet\tilde P)\bigr),\qquad
L^{\bullet}_{\tilde P}L^{\bullet}_{\tilde P^{\bullet2}}=L^{\bullet}_{\tilde P^{\bullet2}}L^{\bullet}_{\tilde P}.
$$

*Proof.* The product $\bullet$ is the symmetrisation, $\tilde P\bullet\tilde Q=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$, of the plain product, which is associative, so the algebra is Jordan-admissible by the theorem *Every associative algebra is Jordan-admissible* of *The Symmetric and Antisymmetric Parts of an Algebra Product*: the symmetrisation is a Jordan product, commutative and satisfying the Jordan identity, and the display is the nested form of the identity. The plain unit $e_0$ is a two-sided unit of the symmetrisation, $e_0\bullet\tilde P=\tfrac12(e_0\tilde P+\tilde Pe_0)=\tilde P$, so the Jordan algebra is unital.

## The Operator Identity of the Idempotents

The model of this pair of articles states its criterion as an identity of the operators of the **idempotents**; the block's criterion is stated at every element, and its content at an idempotent is the **cubic Peirce identity** and the decomposition it produces.

**Corollary (the cubic Peirce identity).** Let $\tilde\Pi$ be an idempotent of the block. Then

$$
L^{\bullet}_{\tilde\Pi}\bigl(2L^{\bullet}_{\tilde\Pi}-\mathrm{id}\bigr)\bigl(L^{\bullet}_{\tilde\Pi}-\mathrm{id}\bigr)=0,
$$

equivalently $2L^{\bullet}_{\tilde\Pi}{}^{3}-3L^{\bullet}_{\tilde\Pi}{}^{2}+L^{\bullet}_{\tilde\Pi}=0$, and the eigenvalues of $L^{\bullet}_{\tilde\Pi}$ lie in $\{0,\tfrac12,1\}$.

**Corollary (the Jordan Peirce decomposition).** For a non-trivial idempotent $\tilde\Pi$ the space splits as

$$
\mathbb{B}=\mathbb{B}_{1}\oplus\mathbb{B}_{1/2}\oplus\mathbb{B}_{0},\qquad
\mathbb{B}_{\lambda}=\{\tilde Y:\tilde\Pi\bullet\tilde Y=\lambda\tilde Y\},
$$

with $\mathbb{B}_1=\mathbb{C}\tilde\Pi$, $\mathbb{B}_0=\mathbb{C}(e_0-\tilde\Pi)$ and $\dim\mathbb{B}_{1/2}=2$.

*Proof.* Both are *Idempotents of the Symmetric Plain Algebra*; the eigenvalue statement is verified there on the witness $\tilde\Pi=\tfrac12(e_0+ie_1)$, whose operator has eigenvalues $0,\tfrac12,1$ and whose Peirce dimensions are $1,2,1$.

**Remark (the contrast with the model).** The model's criterion, left alternativity, is the condition $L^{\circ}_{\tilde X}{}^{2}=L^{\circ}_{\tilde X^{\circ2}}$ for every $\tilde X$, and its corollary is that an idempotent gives a **projector**, $L^{\circ}_{\tilde\Pi}{}^{2}=L^{\circ}_{\tilde\Pi}$, with an image, a kernel and a Peirce calculus of corners and ideals. The block satisfies the weaker Jordan law and **fails left alternativity**: the witness is $e_1$ against $e_2$, $(e_1\bullet e_1)\bullet e_2=-e_2$ against $e_1\bullet(e_1\bullet e_2)=0$ (*Introduction to the Symmetric Plain Algebra of Biquaternions*). So in the block no non-trivial idempotent gives a projector, the unit alone does, and the Peirce calculus is the cubic one above and not the quadratic one. The two criteria are the two halves of the same comparison: the block is the Jordan algebra of the pair and the parent is the associative one, and each fails the other's law.

## The Eleven Failures

The twelve structures are generated from the plain product by three independent operations — the twist of the first slot, the twist of the second slot, and the (anti)symmetrisation — and this is why the symmetric plain product stands alone.

**Theorem (the symmetric plain product is the only Jordan product).** Of the twelve structures of *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, the symmetric plain product is the only one that is commutative and satisfies the Jordan identity.

*Proof.* The four general products are $\tilde X\circ\tilde Y=\theta(\tilde X)\phi(\tilde Y)$ with $\theta$ the identity or the natural conjugation ${}^{\natural}$ and $\phi$ the identity or the star ${}^{*}$ (*The Four General Products of the Biquaternion $\mathbb{C}$ Space*); each family contributes the product, its symmetrisation and its antisymmetrisation. The proof is the case analysis of the four subsections below: the four general products are non-commutative; the four antisymmetric parts are non-commutative; the symmetric quaternionic product is commutative but fails the Jordan identity; and the two symmetric sesquilinear products are only conjugate-commutative and fail the Jordan identity. The symmetric plain product is commutative and satisfies the identity.

### The Four General Products Are Not Commutative

**Proposition.** None of the four general products is commutative.

*Proof.* The plain product: $e_1e_2=e_3$ and $e_2e_1=-e_3$. The general quaternionic product $\tilde X\circ\tilde Y=\tilde X^{\natural}\tilde Y$: $e_0\circ e_1=e_1$ and $e_1\circ e_0=-e_1$. The general plain sesquilinear product $\tilde X\circ\tilde Y=\tilde X\tilde Y^{*}$: $e_0\circ e_1=-e_1$ and $e_1\circ e_0=e_1$. The general quaternionic sesquilinear product: $e_0\circ ie_1=ie_1$ and $ie_1\circ e_0=-ie_1$. Each pair differs.

The failure is structural: the twist of a slot by a conjugation is an anti-automorphism, and an anti-automorphism in a slot reverses the order of the product. The general plain product is *associative*, so it satisfies the Jordan identity, and it is excluded from the criterion by commutativity alone.

### The Four Antisymmetric Parts Are Not Commutative

**Proposition.** None of the four antisymmetric parts is commutative, and the two that are alternating satisfy the Jordan identity vacuously.

*Proof.* The antisymmetric plain product: $e_1\wedge e_2=e_3$ and $e_2\wedge e_1=-e_3$. The antisymmetric quaternionic product: $e_0\circ e_1=e_1$ and $e_1\circ e_0=-e_1$. The antisymmetric plain sesquilinear product: $e_0\circ e_1=-e_1$ and $e_1\circ e_0=e_1$. The antisymmetric quaternionic sesquilinear product: $e_1\circ e_2=e_3$ and $e_2\circ e_1=-e_3$. The first and the second are alternating, $\tilde X\circ\tilde X=0$ for every $\tilde X$, so $\tilde X^{\circ2}=0$ and the Jordan identity reads $0=0$; the last two are conjugate-alternating and do not vanish on the diagonal.

This is the fine point of the comparison and it is stated exactly. **The Jordan identity alone does not isolate the block**: the associative general plain product satisfies it by associativity, the general quaternionic product satisfies it because its square is central, and the two alternating antisymmetrisations satisfy it vacuously. What isolates the block is the **conjunction** with commutativity, and it is the conjunction that the definition names.

### The Symmetric Quaternionic Product Is Commutative but Fails the Jordan Identity

**Proposition.** The symmetric quaternionic product $\tilde X\circ\tilde Y=\tfrac12(\tilde X^{\natural}\tilde Y+\tilde Y^{\natural}\tilde X)$ is commutative and fails the Jordan identity at $\tilde X=e_1$:

$$
(\tilde X^{\circ2}\circ\tilde X)\circ\tilde X=0,\qquad \tilde X^{\circ2}\circ(\tilde X\circ\tilde X)=e_0,\qquad \tilde X=e_1 .
$$

*Proof.* $e_1^{\natural}e_1=-e_1^2=e_0$, so $e_1\circ e_1=e_0$; then $e_1\circ e_1=e_0$ gives $(\tilde X^{\circ2}\circ\tilde X)\circ\tilde X=(e_0\circ e_1)\circ e_1$, and $e_0\circ e_1=\tfrac12(e_0^{\natural}e_1+e_1^{\natural}e_0)=\tfrac12(e_1-e_1)=0$, so the left side is $0\circ e_1=0$; while $\tilde X^{\circ2}\circ(\tilde X\circ\tilde X)=e_0\circ e_0=e_0$. The two differ.

**Remark (why this is the border case).** The symmetric quaternionic product is commutative and its values are central, so its operators are scalars times plain operators with a conjugated index; the identity fails because the conjugate index is carried by a product that is not commutative. It is the closest of the eleven to the block, and it is *The Specificities of the Symmetric Quaternionic Algebra*.

### The Two Symmetric Sesquilinear Products Fail the Jordan Identity

**Proposition.** The symmetric plain sesquilinear product and the symmetric quaternionic sesquilinear product are conjugate-commutative and not commutative, and they fail the Jordan identity at $\tilde X=e_1$:

$$
(\tilde X^{\circ2}\circ\tilde X)\circ\tilde X=0,\qquad
\tilde X^{\circ2}\circ(\tilde X\circ\tilde X)=e_0\quad(\mathrm{SPS}),
(\tilde X^{\circ2}\circ\tilde X)\circ\tilde X=-e_0,\qquad
\tilde X^{\circ2}\circ(\tilde X\circ\tilde X)=e_0\quad(\mathrm{SQS}),
$$

at $\tilde X=e_1$.

*Proof.* For the symmetric plain sesquilinear product $e_1\circ e_1=H(e_1,e_1)e_0=e_0$, and $e_0\circ e_1=H(e_0,e_1)e_0=0$, so the left side is $(e_0\circ e_1)\circ e_1=0$; while $e_1\circ e_1=e_0$ gives $e_0\circ e_0=H(e_0,e_0)e_0=e_0$. For the symmetric quaternionic sesquilinear product the symmetric square of $e_1$ is $-e_0$, so the left side is $((-e_0)\circ e_1)\circ e_1=-e_0$ and the right is $(-e_0)\circ(-e_0)=e_0$, the sesquilinear form of that row being the anti-Hermitian one. The failure of commutativity is the failure of the conjugate-commutativity, $e_1\circ ie_1=\mp ie_0$ against $ie_1\circ e_1=\pm ie_0$.

## The Verdicts

The twelve structures are compared below. The second column is the criterion's first clause, the third its second, and the fourth the witness of the failure for the eleven; for the three commutative failures (SQA, SPS and SQS) the witness is the element $\tilde X=e_1$ and the fourth column lists the two sides of the identity, and "$--$" is the block.

| structure | commutative | Jordan identity | witness of the failure |
|---|---|---|---|
| GPA | no | yes (associative) | $e_1e_2=e_3$ against $e_2e_1=-e_3$ |
| SPA | **yes** | **yes** | — (the criterion) |
| APA | no | yes (vacuous) | $e_1\wedge e_2=e_3$ against $e_2\wedge e_1=-e_3$ |
| GQA | no | yes | $e_0\circ e_1=e_1$ against $e_1\circ e_0=-e_1$ |
| SQA | yes | no | $(x^{\circ2}\circ x)\circ x=0$ against $x^{\circ2}\circ(x\circ x)=e_0$ |
| AQA | no | yes (vacuous) | $e_0\circ e_1=e_1$ against $e_1\circ e_0=-e_1$ |
| GPS | no | no | $e_0\circ e_1=-e_1$ against $e_1\circ e_0=e_1$ |
| SPS | conjugate | no | $(x^{\circ2}\circ x)\circ x=0$ against $x^{\circ2}\circ(x\circ x)=e_0$ |
| APS | no | no | $e_0\circ e_1=-e_1$ against $e_1\circ e_0=e_1$ |
| GQS | no | no | $e_0\circ ie_1=ie_1$ against $ie_1\circ e_0=-ie_1$ |
| SQS | conjugate | no | $(x^{\circ2}\circ x)\circ x=-e_0$ against $x^{\circ2}\circ(x\circ x)=e_0$ |
| AQS | no | no | $e_1\circ e_2=e_3$ against $e_2\circ e_1=-e_3$ |

The table records theorems and not coincidences. The Jordan identity holds outside the block as well — at every element of the associative general plain product by associativity, at every element of the general quaternionic product because its square is central, and vacuously at every element of the two alternating antisymmetrisations — and none of these carries a theory, because the criterion is the conjunction of the identity with commutativity, which the four lack.

## What the Criterion Delivers

Only for the symmetric plain product does the criterion hold at every element, and the whole structural theory of the block is its consequence.

- **The generic trace and norm.** Every element satisfies the quadratic identity $\tilde X^{\bullet2}-T(\tilde X)\tilde X+N(\tilde X)e_0=0$ with $T(\tilde X)=2X_0$ and $N(\tilde X)=\tilde X\tilde X^{\natural}$ (*Norm and Invertibility in the Symmetric Plain Algebra*); the identity is the generic minimal polynomial of a degree-two Jordan algebra and it is unavailable in the eleven.
- **The Jordan inverse.** The inverse is the one of the two Jordan equations, and the criterion is $N\neq0$; the naive equation alone is degenerate on the isotropic cone, the element $e_1+ie_2$ being the witness.
- **The quadratic representation.** The norm is not multiplicative and is replaced by $N(U_{\tilde X}\tilde Y)=N(\tilde X)^2N(\tilde Y)$.
- **The cubic Peirce identity and the decomposition** of §*The Operator Identity of the Idempotents*.
- **The structure algebra.** The derivations and the inner derivations of the block, the automorphism group and the structure group as groups of linear maps, with their Lie algebras (*The Multiplication Operators of the Symmetric Plain Algebra*).

**Remark (what the criterion does not deliver).** Three things the parent product has are absent, and the absence is stated and not filled. There is **no projector calculus**: a non-trivial idempotent of the block does not give a projector, the unit alone does. There is **no associative Peirce calculus**: no corner subalgebras, no ideal lattice, no module theory of the associative kind; the Jordan Peirce decomposition is the form the Jordan theory allows and it is a single middle space, not a pair. There is **no group of units under the product**: the invertible elements are not closed under $\bullet$, the pair $e_1,e_2$ being invertible with product $0$. All three are consequences of the loss of associativity, and all three are the exact content of the contrast with *The Specificities of the General Plain Algebra*.

## The Boundary of the Criterion

Two statements are easily confused and are kept apart here.

1. **As a law, the conjunction is exactly the threshold.** Commutativity with the Jordan identity, equivalently commutativity with the operator identity at every element, is satisfied by the symmetric plain product and by no other of the twelve.
2. **Read at the elements rather than as a law, the identity holds outside the block too.** An operator $L^{\circ}_{\tilde X}$ may satisfy $L^{\circ}_{\tilde X}L^{\circ}_{\tilde X^{\circ2}}=L^{\circ}_{\tilde X^{\circ2}}L^{\circ}_{\tilde X}$ in a structure that is not a Jordan product, at one element or at every one, because the criterion demands the identity together with commutativity and the identity alone is not exclusive. The structured cases are the associative general plain product, where the identity holds at every element by associativity, the general quaternionic product, where it holds at every element because the square is central, and the two alternating antisymmetrisations, where it holds vacuously; none of the four is commutative. The symmetric quaternionic product is the case where the product is commutative and the identity still fails.

**Remark (the sharp form of the specificity).** The correct exclusive statement is therefore not that no other structure satisfies the Jordan identity, but that no other structure is a **Jordan product**: the symmetric plain algebra is the only commutative structure of the twelve in which the operator of the square commutes with the operator. This is why the generic norm, the Jordan inverse, the quadratic representation and the Peirce decomposition are properties of the symmetric plain product and are not transferable, and it is the reason the twelve are not twelve copies of one theory but one theory with eleven deformations, the symmetric plain product being the degree-two Jordan deformation of the plain one.

## Summary

The symmetric plain product is the only one of the twelve structures of the complex space that is a **Jordan product**, that is commutative and satisfying the Jordan identity. The Jordan identity is equivalent, for a commutative product, to the operator identity $L^{\circ}_{\tilde X}L^{\circ}_{\tilde X^{\circ2}}=L^{\circ}_{\tilde X^{\circ2}}L^{\circ}_{\tilde X}$ for every $\tilde X$; its content at an idempotent is the cubic Peirce identity $L^{\bullet}_{\tilde\Pi}(2L^{\bullet}_{\tilde\Pi}-\mathrm{id})(L^{\bullet}_{\tilde\Pi}-\mathrm{id})=0$ and the Jordan Peirce decomposition $\mathbb{B}=\mathbb{C}\tilde\Pi\oplus\mathbb{B}_{1/2}\oplus\mathbb{C}(e_0-\tilde\Pi)$. The parent product, the general plain one, fails the criterion by commutativity though it is associative, and the block fails instead the parent's own criterion, left alternativity: so no non-trivial idempotent of the block gives a projector, and the Peirce calculus is cubic and not quadratic. The eleven failures are structural: the four general products are non-commutative, the four antisymmetric parts are non-commutative with two of them satisfying the identity vacuously, the symmetric quaternionic product is commutative but fails the identity at $e_1$ with the sides $0$ and $e_0$, and the two symmetric sesquilinear products are conjugate-commutative and fail it. The correct exclusive statement is about the law and not about isolated elements, and the whole structural theory of the block — the degree-two generic trace and norm, the Jordan inverse, the quadratic representation, the cubic Peirce identity and the structure algebra — is its consequence; the projector calculus, the associative Peirce calculus and the group of units are the three things it does not have.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\circ$ | a generic product, specified at each use |
| $\tilde X^{\circ2}=\tilde X\circ\tilde X$ | the square of the generic product |
| $L^{\circ}_{\tilde X}:\tilde Y\mapsto\tilde X\circ\tilde Y$ | the left multiplication |
| $L^{\circ}_{\tilde X}L^{\circ}_{\tilde X^{\circ2}}=L^{\circ}_{\tilde X^{\circ2}}L^{\circ}_{\tilde X}$ | the operator identity of the criterion |
| $L^{\bullet}_{\tilde\Pi}(2L^{\bullet}_{\tilde\Pi}-\mathrm{id})(L^{\bullet}_{\tilde\Pi}-\mathrm{id})=0$ | the cubic Peirce identity |
| $\mathbb{B}_1\oplus\mathbb{B}_{1/2}\oplus\mathbb{B}_0$ | the Jordan Peirce decomposition, of dimensions $1,2,1$ |
| $\mathrm{GPA}\dots\mathrm{AQS}$ | the twelve structures, coded as in *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* |

## Further Reading

- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the Jordan identity, the operator identity, the cubic Peirce identity and the Peirce decomposition.
- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the left and the right multiplications and the alternative laws.
- *The Specificities of the General Plain Algebra* (`articles_maths/the-specificities-of-the-general-plain-algebra.md`), the model, for the left alternativity the block fails.
- *The Specificities of the Symmetric Quaternionic Algebra* (`articles_maths/the-specificities-of-the-symmetric-quaternionic-algebra.md`), for the border case, whose product is commutative and whose operators fail the identity.
- *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-12-algebraic-structures-over-the-biquaternion-c-space.md`), for the twelve operations and the row table.
- *The Symmetric and Antisymmetric Parts of an Algebra Product* (`articles_maths/the-symmetric-and-antisymmetric-parts-of-an-algebra-product.md`), for the Jordan-admissibility of an associative algebra and the nested form of the Jordan identity.
