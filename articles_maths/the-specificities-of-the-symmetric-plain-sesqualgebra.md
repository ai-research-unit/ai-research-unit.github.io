# __The Specificities of the Symmetric Plain Sesqualgebra__

## Introduction

The symmetric plain sesqualgebra is the operation $\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0$ on the biquaternion space, the Hermitian form $H$ read as a multiplication (*Introduction to the Symmetric Plain Sesqualgebra of Biquaternions*). This article isolates what makes the block unlike the other eleven structures of the space, states it as a **criterion**, and tests the criterion on the other eleven.

The criterion is that the product is a **Hermitian form read as a multiplication**. A product is called **Hermitian** here when it satisfies the two clauses

$$
\text{(C1)}\quad \tilde P\circ\tilde Q = \overline{\tilde Q\circ\tilde P}, \qquad
\text{(C2)}\quad \tilde P\circ\tilde Q\in\mathbb{C}e_0\quad\text{for all }\tilde P,\tilde Q,
$$

that is, when it is **conjugate-commutative** and when its **image is the centre**. The block satisfies both clauses: C1 is the conjugate-commutative law of the block and C2 is the centrality of its value. **No other of the twelve structures satisfies both**, and this is the specificity: the block is the only **Hermitian** product of the twelve, and the only one whose multiplication is a Hermitian form. The two clauses are not a matter of taste, and each is separately necessary: the symmetric quaternionic sesqualgebra $\mathrm{SQS}$ satisfies C1 and fails C2, the symmetric plain product satisfies neither, and the four general products fail C2.

**Placement.** The article is the closing entry of the *Specific Theory* section of the block, after *The Conjugate-Commutative Law and the Idempotents of the Symmetric Plain Sesqualgebra* and the form and operator articles. It is the fourth of the family that *The Specificities of the General Plain Algebra* began and that *The Specificities of the General Quaternionic Algebra* and *The Specificities of the Symmetric Quaternionic Algebra* continued; it is the entry that carries the Hermitian clause of the family's comparison table.

**Boundaries.** The product, its class and its table are *Introduction to the Symmetric Plain Sesqualgebra of Biquaternions*; the conjugate-commutative law, its two reading involutions and its comparison with the siblings are *The Conjugate-Commutative Law and the Idempotents of the Symmetric Plain Sesqualgebra*. The eleven other products are *The 12 Products of the Biquaternion Complex Space*, their generation by the twists is *The Symmetric and Antisymmetric Parts of an Algebra Product* and *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*, and the general comparison table is *The Specificities of the General Plain Algebra*. The multiplication operators and the composition law of the block are *The Multiplication Operators of the Symmetric Plain Sesqualgebra*. Nothing topological and nothing metric appears.

**Conventions.** $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ with $e_1e_2 = e_3$ and central scalar imaginary $i$. A general element is $\tilde{Q} = \sum_{\mu=0}^{3}Q_\mu e_\mu = Q_0e_0 + \mathbf Q$ with $Q_\mu\in\mathbb{C}$; the natural conjugation is $\tilde{Q}^{\natural} = \sum_\mu\varepsilon_\mu Q_\mu e_\mu$ with $\varepsilon = (1,-1,-1,-1)$, the coefficientwise conjugation is $\overline{\tilde{Q}} = \sum_\mu\overline{Q_\mu}e_\mu$, and the Hermitian conjugation is $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}$. The product of the block is written $\star$ and the products of the other blocks keep the signs of *The 12 Products of the Biquaternion Complex Space*; a general product in a statement is written $\circ$. The centre is $\mathbb{C}_{\mathbb{B}} = \mathbb{C}e_0$ and the vector subspace is $\mathrm{Vect}(\mathbb{B}) = \{Q_0 = 0\}$.

## The Criterion

**Definition (Hermitian product).** Let $\circ$ be a product on $\mathbb{B}$. It is **conjugate-commutative** when

$$
\tilde P\circ\tilde Q = \overline{\tilde Q\circ\tilde P}
$$

for all $\tilde P,\tilde Q$, the bar acting coefficientwise, and it has **central image** when $\tilde P\circ\tilde Q\in\mathbb{C}e_0$ for all $\tilde P,\tilde Q$. The product is **Hermitian** when it is conjugate-commutative with central image.

**Theorem (the Hermitian reading).** For a product $\circ$ on $\mathbb{B}$ the following are equivalent: $\circ$ is Hermitian; the product has central image and there is a Hermitian form $\Lambda$ on $\mathbb{B}$ with

$$
\tilde P\circ\tilde Q = \Lambda(\tilde P,\tilde Q)e_0 .
$$

*Proof.* If $\circ$ has central image, the coefficient $\Lambda(\tilde P,\tilde Q)$ of $e_0$ in $\tilde P\circ\tilde Q$ is well defined; conjugate-commutativity of the product is then exactly the Hermitian symmetry of the coefficient, $\Lambda(\tilde P,\tilde Q) = \overline{\Lambda(\tilde Q,\tilde P)}$. Conversely a product defined by a Hermitian form has central image and is conjugate-commutative. The sesquilinearity of $\Lambda$ is the class of the product: a product that is conjugate-commutative and bilinear is zero, since $\lambda(\tilde P\circ\tilde Q) = \tilde P\circ(\lambda\tilde Q) = \overline{(\lambda\tilde Q)\circ\tilde P} = \overline{\lambda}\,(\tilde P\circ\tilde Q)$ for every $\lambda$, forcing $\tilde P\circ\tilde Q = 0$; and a product that is conjugate-linear in both arguments is zero as well, since $\tilde P\circ(\lambda\tilde Q) = \overline{\lambda}\,(\tilde P\circ\tilde Q)$ on the one hand and $\tilde P\circ(\lambda\tilde Q) = \overline{(\lambda\tilde Q)\circ\tilde P} = \lambda\,(\tilde P\circ\tilde Q)$ on the other. So a nonzero conjugate-commutative product is sesquilinear, linear in one argument and conjugate-linear in the other, which is the class of the twelve.

**Corollary (the block satisfies the criterion).** The block is Hermitian, with the Hermitian form $H(\tilde P,\tilde Q) = \sum_\mu P_\mu\overline{Q_\mu}$, non-degenerate, of Gram matrix the identity and positive definite.

**Remark (the two clauses correct the two errors).** C1 alone would also admit the products that are conjugate-commutative with a non-central value, and among the twelve that is the symmetric quaternionic sesquilinear product; C2 alone would also admit the commutative central products, and that is the symmetric quaternionic product. Neither clause alone identifies the block, and both together do.

## The Eleven Comparisons

**Theorem (the specificity).** Of the twelve structures of *The 12 Products of the Biquaternion Complex Space*, the symmetric plain sesqualgebra is the only one that is Hermitian.

*Proof.* The block is Hermitian by the corollary above. The remaining eleven are disposed of in the three sections below, each by a witness: the four general products fail C2, the four antisymmetric parts fail C2, and among the three remaining symmetric parts the two bilinear ones fail C1 while the sesquilinear one fails C2. Since every structure of the twelve is one of these, and each fails at least one clause, the block is the only one that satisfies both.

### The Four General Products

The four general products are $\tilde P\tilde Q$, $\tilde P^{\natural}\tilde Q$, $\tilde P\tilde Q^{*}$ and $\tilde P^{\natural}\tilde Q^{*}$ (*The Four General Products of the Biquaternion $\mathbb{C}$ Space*). Each fails C2, and the witness is the same for all four: the value on $e_0$ and $e_1$ is a nonzero multiple of $e_1$, which is not central.

| product | $\tilde P\circ\tilde Q$ | value at $(e_0,e_1)$ | central |
|---|---|---|---|
| $\tilde P\tilde Q$ | the plain product | $e_1$ | no |
| $\tilde P^{\natural}\tilde Q$ | the natural product | $e_1$ | no |
| $\tilde P\tilde Q^{*}$ | the plain sesquilinear product | $-e_1$ | no |
| $\tilde P^{\natural}\tilde Q^{*}$ | the quaternionic sesquilinear product | $-e_1$ | no |

Each of the four also fails C1, at the same witness $(e_1,e_2)$: the value is $e_3$ for the first and the fourth and $-e_3$ for the second and the third, while the conjugate of the value on the reversed pair is the opposite sign in each case. The clause that already suffices is C2. The four general products are therefore not Hermitian, and the block, which is a part of the third of them, splits off from its parent exactly by acquiring C1 and C2.

### The Four Antisymmetric Parts

The four antisymmetric parts are $\mathrm{APA} = \tfrac12(\tilde P\tilde Q - \tilde Q\tilde P)$, $\mathrm{AQA} = \tfrac12(\tilde P^{\natural}\tilde Q - \tilde Q^{\natural}\tilde P)$, $\mathrm{APS} = \tfrac12(\tilde P\tilde Q^{*} - \overline{\tilde Q}\tilde P^{\natural})$ and $\mathrm{AQS} = \tfrac12(\tilde P^{\natural}\tilde Q^{*} - \tilde Q^{*}\tilde P^{\natural})$ (*The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*). Each fails C1: the two bilinear ones, $\mathrm{APA}$ and $\mathrm{AQA}$, are alternating, $\tilde P\circ\tilde Q = -\,\tilde Q\circ\tilde P$, and the two sesquilinear ones, $\mathrm{APS}$ and $\mathrm{AQS}$, are conjugate-alternating, $\tilde P\circ\tilde Q = -\,\overline{\tilde Q\circ\tilde P}$, and at the witnesses below the value is not equal to the conjugate of the reversed value in either case. Each also fails C2, because its image is the vector subspace $\mathrm{Vect}(\mathbb{B})$. The witnesses are collected below.

| product | value at $(e_1,e_2)$ | position |
|---|---|---|
| $\mathrm{APA}$ | $e_3$ | vector subspace |
| $\mathrm{AQA}$ | $-e_3$ | vector subspace |
| $\mathrm{APS}$ | $-e_3$ | vector subspace |
| $\mathrm{AQS}$ | $e_3$ | vector subspace |

### The Symmetric Parts

The four symmetric parts are $\mathrm{SPA}$, $\mathrm{SQA}$, the block $\mathrm{SPS}$ and $\mathrm{SQS}$, the four products of the symmetric family. The block is Hermitian; the three others are separated by the clauses:

- **$\mathrm{SPA} = \tfrac12(\tilde P\tilde Q + \tilde Q\tilde P)$** is commutative, with $\tilde P\bullet\tilde Q = \tilde Q\bullet\tilde P$, and its value carries a vector part; it fails C1, because $\tilde P\bullet\tilde Q = \overline{\tilde Q\bullet\tilde P}$ would force the value to be real, and at $(e_0,ie_0)$ the value is $ie_0$ against the conjugate $-ie_0$; it fails C2 as well, its value at $(e_0,e_1)$ being $e_1$.
- **$\mathrm{SQA} = N(\tilde P,\tilde Q)e_0$** is commutative with central image, so it satisfies C2; it fails C1, since at $(e_0,ie_0)$ the value is $ie_0$ against the conjugate $-ie_0$. The law of $\mathrm{SQA}$ is commutativity and not conjugate-commutativity (*The Specificities of the Symmetric Quaternionic Algebra*).
- **$\mathrm{SQS} = \tfrac12(\tilde P^{\natural}\tilde Q^{*} + \tilde Q^{*}\tilde P^{\natural})$** is conjugate-commutative, so it satisfies C1; it fails C2, since its value at $(e_0,e_1)$ is $-e_1$, in the vector subspace. The law without the centrality is exactly what the present criterion excludes.

**Corollary (the separation inside the symmetric family).** The three clauses *commutativity*, *centrality* and *conjugate-commutativity* separate the four symmetric structures two by two, and the block is the unique cell of the two clauses C1 and C2. The comparison of the laws alone is *The Conjugate-Commutative Law and the Idempotents of the Symmetric Plain Sesqualgebra*; here the second clause is the new one.

## The Operator Face

The criterion has an operator reading, taken from *The Multiplication Operators of the Symmetric Plain Sesqualgebra*. The left and the right multiplications of the block are $L^{\star}_{\tilde A}\tilde R = H(\tilde A,\tilde R)e_0$ and $R^{\star}_{\tilde A}\tilde R = H(\tilde R,\tilde A)e_0$, and they obey the composition law

$$
L^{\star}_{\tilde A}L^{\star}_{\tilde B} = A_0\,R^{\star}_{\tilde B}, \qquad R^{\star}_{\tilde A} = \overline{L^{\star}_{\tilde A}},
$$

in which $A_0$ is the scalar coordinate and the bar is the coefficientwise conjugation of an operator. The second identity is the operator form of C1: the right multiplication is the conjugate of the left, which is exactly the operator statement of conjugate-commutativity. The first identity is the operator form of C2: the composite is a scalar times a single right multiplication, because the image of every operator is the centre.

**Corollary (the projectors collapse).** The left multiplication of the block is conjugate-linear, and a conjugate-linear operator that is idempotent is zero; the projectors of the block are therefore the zero operator alone, and the block's class of projectors is the smallest of the four symmetric structures, tied with the symmetric quaternionic sesquilinear block.

| structure | idempotent left multiplications | the operator they are |
|---|---|---|
| $\mathrm{SPA}$ | $0$ and $e_0$ | $0$ and the identity |
| $\mathrm{SQA}$ | the origin and the hyperplane $X_0 = 1$ | $0$ and the rank-one projections onto the centre |
| $\mathrm{SPS}$ | the origin alone | $0$ |
| $\mathrm{SQS}$ | the origin alone | $0$ |

The table is the symmetric-family row of the comparison of *The Specificities of the Symmetric Quaternionic Algebra*. The block is a member whose operator family is the smallest, together with the symmetric quaternionic sesquilinear block: as an element theory it is a rank-one pairing, and as an operator theory it is a family of conjugate-linear maps whose only idempotent is the zero operator.

## The Consequence

**Corollary (what belongs to the block alone).** The block is the only one of the twelve that is at once **conjugate-commutative** and **central-valued**, and it is therefore the only one whose multiplication is a **Hermitian form**. Neither clause alone identifies it, and each has a witness among the symmetric parts: $\mathrm{SQA}$ carries C2 alone (a central value with a commutative law) and the sibling $\mathrm{SQS}$ carries C1 alone (a conjugate-commutative law with a non-central value). The **definiteness** of the form is a third ingredient and is not shared with $\mathrm{SQA}$, whose form is the quaternion form $N$, indefinite, so that $\mathrm{SQA}$ has a nonzero isotropic cone and nonzero square-zero elements, while the form of the block is $H$, definite; the definiteness is that of the plain sesquilinear family, and it is shared with the parent $\mathrm{GPS}$, the general plain sesquilinear product, whose scalar part is the same $H$ and whose square-zero elements are therefore the origin alone — but the parent carries neither clause, its image being all of $\mathbb{B}$, and the block is exactly the part of it that carries the two. The **marks of the block** are then the **ray image** of its square map, the square of the parent $\tilde X\mapsto\tilde X\tilde X^{*}$ being a Hermitian element that leaves the ray, at $\tilde X = e_0+ie_1$ with the value $2e_0+2ie_1$, while the square of the sibling vanishes at the same element, $(e_0+ie_1)$ being square-zero in $\mathrm{SQS}$; and, inside the symmetric family, the **linear subspace** of the nilpotents of index **three**, where the other three symmetric products have nilpotent cones of index two. The other eleven structures reproduce some of these features one by one, but no other reproduces the pair of clauses, and the pair is the specificity.

**Remark (the criterion and the family of the specificities).** The specificities of the general plain algebra read the element theory, and the specificities of the symmetric quaternionic algebra read the operator identity $L_{\tilde X}^{2} = X_0L_{\tilde X}$. The present article reads a clause about the product itself, because the block's element and operator theories are both degenerate: its idempotents are two points, its nilpotents are a subspace of index three, and its projectors are the zero operator. What survives, and what is peculiar to the block, is that its product is a Hermitian form; the criterion is the statement of that, and this article is its proof against the eleven.

## Summary

The symmetric plain sesqualgebra is the only one of the twelve structures that is **Hermitian**: it is **conjugate-commutative**, $\tilde P\star\tilde Q = \overline{\tilde Q\star\tilde P}$, and it has **central image**, $\tilde P\star\tilde Q\in\mathbb{C}e_0$, and the two clauses together are equivalent to the product being a Hermitian form read as a multiplication. The other eleven fail at least one clause: the four general products fail the centrality; the four antisymmetric parts fail both, being alternating ($\mathrm{APA}$, $\mathrm{AQA}$) or conjugate-alternating ($\mathrm{APS}$, $\mathrm{AQS}$) with image in the vector subspace; and among the symmetric parts the plain one fails both, the quaternionic one fails the centrality, and the quaternionic sesquilinear one fails the centrality after satisfying conjugate-commutativity. The operator face of the criterion is the composition law $L^{\star}_{\tilde A}L^{\star}_{\tilde B} = A_0R^{\star}_{\tilde B}$ with $R^{\star}_{\tilde B} = \overline{L^{\star}_{\tilde B}}$, the second identity being conjugate-commutativity read on the operators, and the projectors collapse to the zero operator because a conjugate-linear idempotent operator is zero. Everything peculiar to the block follows from the pair of clauses and not from the centrality alone: the definite norm and the vanishing of the isotropic and of the square-zero sets come from the definite form $H$, which the block shares with the parent $\mathrm{GPS}$ — a parent that carries neither clause, its image being all of $\mathbb{B}$ — and not with $\mathrm{SQA}$, the structure that carries the centrality alone and whose form is the indefinite quaternion form; the conjugate-commutativity and the collapse of the projectors are shared with the sibling $\mathrm{SQS}$, which carries C1 alone; and the ray image of the square map and the linear subspace of the index-three nilpotents are the marks of the pair.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0$ | the product of the block, the Hermitian one |
| $H(\tilde P,\tilde Q) = \sum_\mu P_\mu\overline{Q_\mu}$ | the Hermitian form the block is |
| (C1) $\tilde P\circ\tilde Q = \overline{\tilde Q\circ\tilde P}$ | conjugate-commutativity |
| (C2) $\tilde P\circ\tilde Q\in\mathbb{C}e_0$ | centrality of the image |
| Hermitian product | a product satisfying C1 and C2 |
| the eleven | the other structures, each failing C1 or C2 |
| $L^{\star}_{\tilde A}L^{\star}_{\tilde B} = A_0R^{\star}_{\tilde B}$ | the composition law, the operator form of C2 |
| $R^{\star}_{\tilde A} = \overline{L^{\star}_{\tilde A}}$ | the operator form of C1 |
| the origin alone | the projectors of the block |

## Further Reading

- *The Specificities of the General Plain Algebra* (`articles_maths/the-specificities-of-the-general-plain-algebra.md`), for the criterion that classifies the twelve structures and for the family this article closes.
- *The Specificities of the Symmetric Quaternionic Algebra* (`articles_maths/the-specificities-of-the-symmetric-quaternionic-algebra.md`), for the sibling criterion $L_{\tilde X}^{2} = X_0L_{\tilde X}$ and the projector table of the symmetric family.
- *Introduction to the Symmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-plain-sesqualgebra-of-biquaternions.md`), for the product, its class and its placement among the twelve.
- *The Conjugate-Commutative Law and the Idempotents of the Symmetric Plain Sesqualgebra* (`articles_maths/the-conjugate-commutative-law-and-the-idempotents-of-the-symmetric-plain-sesqualgebra.md`), for the clause C1, its two reading involutions and its comparison with the siblings.
- *The Multiplication Operators of the Symmetric Plain Sesqualgebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-plain-sesqualgebra.md`), for the composition law, the rank, the trace and the adjoint of the operators.
- *The 12 Products of the Biquaternion Complex Space* (`articles_maths/the-12-products-of-the-biquaternion-complex-space.md`), for the eleven products the criterion is tested against.
