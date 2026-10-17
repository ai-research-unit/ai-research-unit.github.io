# __The Specificities of the Symmetric Plain Sesqualgebra__

## Introduction

The symmetric plain sesqualgebra is the operation $\tilde P\star\tilde Q = \langle\tilde P,\tilde Q\rangle_{*}e_t$ on the biquaternion space, the Hermitian form $\langle\cdot,\cdot\rangle_{*}$ read as a multiplication (*Introduction to the Symmetric Plain Sesqualgebra*). This article isolates what makes the block unlike the other eleven structures of the space and states it as a **criterion** of the block.

The criterion is that the product is a **Hermitian form read as a multiplication**. A product is called **Hermitian** here when it satisfies the two clauses

$$
\text{(C1)}\quad \tilde P\circ\tilde Q = \overline{\tilde Q\circ\tilde P}, \qquad
\text{(C2)}\quad \tilde P\circ\tilde Q\in\mathbb{C}e_t\quad\text{for all }\tilde P,\tilde Q,
$$

that is, when it is **conjugate-commutative** and when its **image is the centre**. The block satisfies both clauses: C1 is the conjugate-commutative law of the block and C2 is the centrality of its value. **No other of the twelve structures satisfies both**, and this is the specificity: the block is the only **Hermitian** product of the twelve, and the only one whose multiplication is a Hermitian form. The two clauses are not a matter of taste, and each is separately necessary: the symmetric quaternionic sesqualgebra $\mathrm{SQS}$ satisfies C1 and fails C2, the symmetric plain product satisfies neither, and the four general products fail C2.

**Placement.** The article is the closing entry of the *Specific Theory* section of the block, after *The Conjugate-Commutative Law and the Idempotents of the Symmetric Plain Sesqualgebra* and the form and operator articles. It is the fourth of the family that *The Specificities of the Biquaternion Algebra* began and that *The Specificities of the General Quaternionic Algebra* and *The Specificities of the Symmetric Quaternionic Algebra* continued; it is the entry that carries the Hermitian clause of the family's comparison table.

**Boundaries.** The product, its class and its table are *Introduction to the Symmetric Plain Sesqualgebra*; the conjugate-commutative law, its two reading involutions and its comparison with the siblings are *The Conjugate-Commutative Law and the Idempotents of the Symmetric Plain Sesqualgebra*. The eleven other products are *The 12 Products of the Biquaternioid Complex Space*, their generation by the twists is *The Symmetric and Antisymmetric Parts of an Algebra Product* and *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*, and the general comparison table is *The Specificities of the Biquaternion Algebra*. The multiplication operators and the composition law of the block are *The Multiplication Operators of the Symmetric Plain Sesqualgebra*. Nothing topological and nothing metric appears.

**Conventions.** $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_t,\vec e_x,\vec e_y,\vec e_z$ with $\vec e_x \vec e_y = \vec e_z$ and central scalar imaginary $i$. A general element is $\tilde{Q} = \sum_{\mu\in\{t,x,y,z\}}Q_\mu e_\mu = Q_te_t + \vec Q$ with $Q_\mu\in\mathbb{C}$; the natural conjugation is $\tilde{Q}^{\natural} = \sum_\mu\varepsilon_\mu Q_\mu e_\mu$ with $\varepsilon = (1,-1,-1,-1)$, the coefficientwise conjugation is $\overline{\tilde{Q}} = \sum_\mu\overline{Q_\mu}e_\mu$, and the Hermitian conjugation is $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}$. The product of the block is written $\star$ and the products of the other blocks keep the signs of *The 12 Products of the Biquaternioid Complex Space*; a general product in a statement is written $\circ$. The centre is $\mathbb{C}_{\mathbb{B}} = \mathbb{C}e_t$ and the vector subspace is $\mathrm{Vect}(\mathbb{B}) = \{Q_t = 0\}$.

## The Criterion

**Definition (Hermitian product).** Let $\circ$ be a product on $\mathbb{B}$. It is **conjugate-commutative** when

$$
\tilde P\circ\tilde Q = \overline{\tilde Q\circ\tilde P}
$$

for all $\tilde P,\tilde Q$, the bar acting coefficientwise, and it has **central image** when $\tilde P\circ\tilde Q\in\mathbb{C}e_t$ for all $\tilde P,\tilde Q$. The product is **Hermitian** when it is conjugate-commutative with central image.

**Theorem (the Hermitian reading).** For a product $\circ$ on $\mathbb{B}$ the following are equivalent: $\circ$ is Hermitian; the product has central image and there is a Hermitian form $\Lambda$ on $\mathbb{B}$ with

$$
\tilde P\circ\tilde Q = \Lambda(\tilde P,\tilde Q)e_t .
$$

*Proof.* If $\circ$ has central image, the coefficient $\Lambda(\tilde P,\tilde Q)$ of $e_t$ in $\tilde P\circ\tilde Q$ is well defined; conjugate-commutativity of the product is then exactly the Hermitian symmetry of the coefficient, $\Lambda(\tilde P,\tilde Q) = \overline{\Lambda(\tilde Q,\tilde P)}$. Conversely a product defined by a Hermitian form has central image and is conjugate-commutative. The sesquilinearity of $\Lambda$ is the class of the product: a product that is conjugate-commutative and bilinear is zero, since $\lambda(\tilde P\circ\tilde Q) = \tilde P\circ(\lambda\tilde Q) = \overline{(\lambda\tilde Q)\circ\tilde P} = \overline{\lambda}\,(\tilde P\circ\tilde Q)$ for every $\lambda$, forcing $\tilde P\circ\tilde Q = 0$; and a product that is conjugate-linear in both arguments is zero as well, since $\tilde P\circ(\lambda\tilde Q) = \overline{\lambda}\,(\tilde P\circ\tilde Q)$ on the one hand and $\tilde P\circ(\lambda\tilde Q) = \overline{(\lambda\tilde Q)\circ\tilde P} = \lambda\,(\tilde P\circ\tilde Q)$ on the other. So a nonzero conjugate-commutative product is sesquilinear, linear in one argument and conjugate-linear in the other, which is the class of the twelve.

**Corollary (the block satisfies the criterion).** The block is Hermitian, with the Hermitian form $\langle\tilde P,\tilde Q\rangle_{*} = \sum_\mu P_\mu\overline{Q_\mu}$, non-degenerate, of Gram matrix the identity and positive definite.

**Remark (the two clauses correct the two errors).** C1 alone would also admit the products that are conjugate-commutative with a non-central value, and among the twelve that is the symmetric quaternionic sesquilinear product; C2 alone would also admit the commutative central products, and that is the symmetric quaternionic product. Neither clause alone identifies the block, and both together do.

## The Isolation among the Twelve

**Theorem (the specificity).** Of the twelve structures of *The Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*, the symmetric plain sesqualgebra is the only one that is **Hermitian**, that is conjugate-commutative with central image.

*Proof.* The block satisfies both clauses by the corollary above. The other eleven are the three remaining general products together with the eight parts got by symmetrising or antisymmetrising the four, and each fails at least one clause. The four general products fail the centrality, their value at $(e_t,\vec e_x)$ being a nonzero multiple of $\vec e_x$; the four antisymmetric parts fail it as well, their image being the vector subspace, and fail conjugate-commutativity too, being alternating ($\mathrm{APA}$, $\mathrm{AQA}$) or conjugate-alternating ($\mathrm{APS}$, $\mathrm{AQS}$) with an opposite value at $(\vec e_x,\vec e_y)$. Among the three remaining symmetric parts, the symmetric plain product fails both, its value at $(e_t,ie_t)$ being $ie_t$ against the conjugate $-ie_t$ and its value at $(e_t,\vec e_x)$ being $\vec e_x$; the symmetric quaternionic product satisfies centrality and fails conjugate-commutativity, its value at $(e_t,ie_t)$ being $ie_t$ against $-ie_t$; and the symmetric quaternionic sesquilinear product satisfies conjugate-commutativity and fails centrality, its value at $(e_t,\vec e_x)$ being $-\vec e_x$.

| family | structures | conjugate-commutative | central image |
|---|---|---|---|
| the four general products | GPA, GQA, GPS, GQS | no | no |
| the symmetric parts | SPA | no | no |
| | SQA | no | **yes** |
| | **SPS** | **yes** | **yes** |
| | SQS | **yes** | no |
| the antisymmetric parts | APA, AQA, APS, AQS | no | no |

The two clauses are independent, each with a witness among the four symmetric parts; the block alone meets both, and the product it defines is the Hermitian form $\langle\cdot,\cdot\rangle_{*}$.

## The Operator Face

The criterion has an operator reading, taken from *The Multiplication Operators of the Symmetric Plain Sesqualgebra*. The left and the right multiplications of the block are $L^{\star}_{\tilde A}\tilde R = \langle\tilde A,\tilde R\rangle_{*}e_t$ and $R^{\star}_{\tilde A}\tilde R = \langle\tilde R,\tilde A\rangle_{*}e_t$, and they obey the composition law

$$
L^{\star}_{\tilde A}L^{\star}_{\tilde Q_1} = A_t\,R^{\star}_{\tilde Q_1}, \qquad R^{\star}_{\tilde A} = \overline{L^{\star}_{\tilde A}},
$$

in which $A_t$ is the scalar coordinate and the bar is the coefficientwise conjugation of an operator. The second identity is the operator form of C1: the right multiplication is the conjugate of the left, which is exactly the operator statement of conjugate-commutativity. The first identity is the operator form of C2: the composite is a scalar times a single right multiplication, because the image of every operator is the centre.

**Corollary (the projectors collapse).** The left multiplication of the block is conjugate-linear, and a conjugate-linear operator that is idempotent is zero; the projectors of the block are therefore the zero operator alone. It is the smallest projector class of the four symmetric structures, shared with the symmetric quaternionic sesquilinear block; the symmetric plain product has the identity as well, from its unit, and the symmetric quaternionic product has the affine hyperplane of rank-one projections onto the centre. As an element theory the block is a rank-one pairing, and as an operator theory it is a family of conjugate-linear maps whose only idempotent is the zero operator.

## The Consequence

**Corollary (what belongs to the block alone).** The block is the only one of the twelve that is at once **conjugate-commutative** and **central-valued**, and it is therefore the only one whose multiplication is a **Hermitian form**. Neither clause alone identifies it, and each has a witness among the symmetric parts: $\mathrm{SQA}$ carries C2 alone (a central value with a commutative law) and the sibling $\mathrm{SQS}$ carries C1 alone (a conjugate-commutative law with a non-central value). The **definiteness** of the form is a third ingredient and is not shared with $\mathrm{SQA}$, whose form is the quaternion form $\langle\cdot,\cdot\rangle_{\natural}$, indefinite, so that $\mathrm{SQA}$ has a nonzero isotropic cone and nonzero square-zero elements, while the form of the block is $\langle\cdot,\cdot\rangle_{*}$, definite; the definiteness is that of the plain sesquilinear family, and it is shared with the parent $\mathrm{GPS}$, the general plain sesquilinear product, whose scalar part is the same $H$ and whose square-zero elements are therefore the origin alone — but the parent carries neither clause, its image being all of $\mathbb{B}$, and the block is exactly the part of it that carries the two. The **marks of the block** are then the **ray image** of its square map, the square of the parent $\tilde Q_2\mapsto\tilde Q_2\tilde Q_2^{*}$ being a Hermitian element that leaves the ray, at $\tilde Q_2= e_t+i\vec e_x$ with the value $2e_t+2i\vec e_x$, while the square of the sibling vanishes at the same element, $(e_t+i\vec e_x)$ being square-zero in $\mathrm{SQS}$; and, inside the symmetric family, the **linear subspace** of the nilpotents of index **three**, where the other three symmetric products have nilpotent cones of index two. The other eleven structures reproduce some of these features one by one, but no other reproduces the pair of clauses, and the pair is the specificity.

**Remark (the criterion and the family of the specificities).** The specificities of the general plain algebra read the element theory, and the specificities of the symmetric quaternionic algebra read the operator identity $L_{\tilde Q_2}^{2} = Q_{2t}L_{\tilde Q_2}$. The present article reads a clause about the product itself, because the block's element and operator theories are both degenerate: its idempotents are two points, its nilpotents are a subspace of index three, and its projectors are the zero operator. What survives, and what is peculiar to the block, is that its product is a Hermitian form; the criterion is the statement of that, and this article is its proof.

## Summary

The symmetric plain sesqualgebra is the only one of the twelve structures that is **Hermitian**: it is **conjugate-commutative**, $\tilde P\star\tilde Q = \overline{\tilde Q\star\tilde P}$, and it has **central image**, $\tilde P\star\tilde Q\in\mathbb{C}e_t$, and the two clauses together are equivalent to the product being a Hermitian form read as a multiplication. The other eleven fail at least one clause: the four general products fail the centrality; the four antisymmetric parts fail both, being alternating ($\mathrm{APA}$, $\mathrm{AQA}$) or conjugate-alternating ($\mathrm{APS}$, $\mathrm{AQS}$) with image in the vector subspace; and among the symmetric parts the plain one fails both, the quaternionic one satisfies the centrality and fails conjugate-commutativity, and the quaternionic sesquilinear one satisfies conjugate-commutativity and fails the centrality. The operator face of the criterion is the composition law $L^{\star}_{\tilde A}L^{\star}_{\tilde Q_1} = A_tR^{\star}_{\tilde Q_1}$ with $R^{\star}_{\tilde Q_1} = \overline{L^{\star}_{\tilde Q_1}}$, the second identity being conjugate-commutativity read on the operators, and the projectors collapse to the zero operator because a conjugate-linear idempotent operator is zero. Everything peculiar to the block follows from the pair of clauses and not from the centrality alone: the definite norm and the vanishing of the isotropic and of the square-zero sets come from the definite form $\langle\cdot,\cdot\rangle_{*}$, which the block shares with the parent $\mathrm{GPS}$ — a parent that carries neither clause, its image being all of $\mathbb{B}$ — and not with $\mathrm{SQA}$, the structure that carries the centrality alone and whose form is the indefinite quaternion form; the conjugate-commutativity and the collapse of the projectors are shared with the sibling $\mathrm{SQS}$, which carries C1 alone; and the ray image of the square map and the linear subspace of the index-three nilpotents are the marks of the pair.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q = \langle\tilde P,\tilde Q\rangle_{*}e_t$ | the product of the block, the Hermitian one |
| $\langle\tilde P,\tilde Q\rangle_{*} = \sum_\mu P_\mu\overline{Q_\mu}$ | the Hermitian form the block is |
| (C1) $\tilde P\circ\tilde Q = \overline{\tilde Q\circ\tilde P}$ | conjugate-commutativity |
| (C2) $\tilde P\circ\tilde Q\in\mathbb{C}e_t$ | centrality of the image |
| Hermitian product | a product satisfying C1 and C2 |
| the eleven | the other structures, each failing C1 or C2 |
| $L^{\star}_{\tilde A}L^{\star}_{\tilde Q_1} = A_tR^{\star}_{\tilde Q_1}$ | the composition law, the operator form of C2 |
| $R^{\star}_{\tilde A} = \overline{L^{\star}_{\tilde A}}$ | the operator form of C1 |
| the origin alone | the projectors of the block |

## Further Reading

- *The Specificities of the Biquaternion Algebra* (`articles_maths/the-specificities-of-the-biquaternion-algebra.md`), for the criterion of the plain product, the model of the family.
- *The Specificities of the Symmetric Quaternionic Algebra* (`articles_maths/the-specificities-of-the-symmetric-quaternionic-algebra.md`), for the sibling criterion $L_{\tilde Q_2}^{2} = Q_{2t}L_{\tilde Q_2}$ and the hyperplane of rank-one projectors onto the centre.
- *Introduction to the Symmetric Plain Sesqualgebra* (`articles_maths/introduction-to-the-symmetric-plain-sesqualgebra.md`), for the product, its class and its placement among the twelve.
- *The Conjugate-Commutative Law and the Idempotents of the Symmetric Plain Sesqualgebra* (`articles_maths/the-conjugate-commutative-law-and-the-idempotents-of-the-symmetric-plain-sesqualgebra.md`), for the clause C1, its two reading involutions and its comparison with the siblings.
- *The Multiplication Operators of the Symmetric Plain Sesqualgebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-plain-sesqualgebra.md`), for the composition law, the rank, the trace and the adjoint of the operators.
- *The 12 Products of the Biquaternioid Complex Space* (`articles_maths/the-12-products-of-the-biquaternioid-complex-space.md`), for the twelve products among which the criterion is read.
