# __Introduction to the Antisymmetric Plain Algebra of Biquaternions__

## Introduction

The plain product of the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ splits into a symmetric half and an antisymmetric half,

$$
\tilde P\tilde Q=\tilde P\bullet\tilde Q+\tilde P\wedge\tilde Q,\qquad
\tilde P\bullet\tilde Q=\tfrac12\bigl(\tilde P\tilde Q+\tilde Q\tilde P\bigr),\qquad
\tilde P\wedge\tilde Q=\tfrac12\bigl(\tilde P\tilde Q-\tilde Q\tilde P\bigr),
$$

and the two halves are independent data. The symmetric half is the subject of *Introduction to the Symmetric Plain Algebra of Biquaternions*; this article introduces the antisymmetric half, the operation

$$
\tilde P\wedge\tilde Q=\mathbf{P}\times\mathbf{Q},
$$

the cross product of the two vector parts. The operation is the twelfth and last row-entry of the table of *The 12 Products of the Biquaternion Complex Space*, and it is the row's Lie product: it alone of the twelve operations satisfies the Jacobi identity. This article establishes the class of the operation, its alternation, its image, the absence of a unit, the Jacobi identity with the cyclic sum recomputed on the units, the sixteen brackets of the basis, the reconstruction of the plain product from its two halves, and the placement of the block among the twelve.

The article is the common theory of the block of six articles that follows it: the Lie algebra it makes of $\mathbb{B}$ is *The Lie Algebra of the Antisymmetric Plain Algebra*, the invariant form it carries is *The Killing Form of the Antisymmetric Plain Algebra*, its reading on the six distinguished subspaces is *The Six Subspaces under the Antisymmetric Plain Algebra of Biquaternions*, its adjoints and derivations are *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra*, and its two matrix models are *The Antisymmetric Plain Algebra in the Matrix Representations*.

The general construction of the two halves of a product is not repeated here: it is *The Symmetric and Antisymmetric Parts of an Algebra Product*, whose definitions of the commutator $[\tilde P,\tilde Q]=\tilde P\tilde Q-\tilde Q\tilde P$, of the outer product $\tilde P\wedge\tilde Q=\tfrac12[\tilde P,\tilde Q]$ and of the symmetrised product $\tilde P\bullet\tilde Q$ are the ones used throughout. The plain product and its pairings are *Introduction to the General Plain Algebra of Biquaternions* and *The Four Pairings of the Biquaternion Algebra*; the two halves of the other three products of the algebra are the other rows of *The 12 Products of the Biquaternion Complex Space*. Everything below is algebra: the Lie algebra of the block is a module with an alternating bracket, and no group and no analytic notion enters.

## The Antisymmetric Part of the Plain Product

### The Operation

**Definition.** For $\tilde P=\sum_\mu P_\mu e_\mu$ and $\tilde Q=\sum_\mu Q_\mu e_\mu$ in $\mathbb{B}$ put

$$
\tilde P\wedge\tilde Q=\tfrac12\bigl(\tilde P\tilde Q-\tilde Q\tilde P\bigr).
$$

The **antisymmetric plain algebra** of the biquaternions is the operation $\wedge$ on $\mathbb{B}$, and it is the block denoted $\mathrm{APA}$ in the table of the twelve.

**Proposition (the cross product of the vector parts).** For all $\tilde P,\tilde Q$,

$$
\tilde P\wedge\tilde Q=\mathbf{P}\times\mathbf{Q},
$$

where $\mathbf{P}=(P_1,P_2,P_3)$ and $\mathbf{Q}=(Q_1,Q_2,Q_3)$ are the vector parts, and the scalar part of the product is zero, $\operatorname{Sc}(\tilde P\wedge\tilde Q)=0$.

*Proof.* The scalar parts of $\tilde P\tilde Q$ and of $\tilde Q\tilde P$ are equal, both being $P_0Q_0-\mathbf{P}\cdot\mathbf{Q}$, so they cancel in the difference and the scalar part of the half-difference is zero. The vector part of $\tilde P\tilde Q$ is $P_0\mathbf{Q}+Q_0\mathbf{P}+\mathbf{P}\times\mathbf{Q}$ and the vector part of $\tilde Q\tilde P$ is $Q_0\mathbf{P}+P_0\mathbf{Q}+\mathbf{Q}\times\mathbf{P}$, so the half-difference is $\tfrac12(\mathbf{P}\times\mathbf{Q}-\mathbf{Q}\times\mathbf{P})=\mathbf{P}\times\mathbf{Q}$. Verified on general elements of $\mathbb{Q}(i)$ coefficients and on the units. $\square$

**Corollary (the class).** The operation is $\mathbb{C}$-bilinear, and it is alternating, $\tilde P\wedge\tilde P=0$ and $\tilde P\wedge\tilde Q=-\tilde Q\wedge\tilde P$ for all $\tilde P,\tilde Q$.

*Proof.* The cross product of vector parts is $\mathbb{C}$-bilinear because the plain product is, and it is alternating because $\mathbf{P}\times\mathbf{P}=0$. $\square$

**Remark.** The operation is therefore of the class $\mathbb{C}$-bilinear and alternating, and its values lie in the vector subspace $\mathrm{Vect}(\mathbb{B})$: **the image of the antisymmetric plain algebra is the vector subspace**, of complex dimension three and real dimension six. The scalar direction is invisible to the operation, and the three complex coordinate directions $e_1,e_2,e_3$ carry the whole of it.

### The Absence of a Unit

**Proposition.** The operation has no unit: there is no $\tilde U\in\mathbb{B}$ with $\tilde U\wedge\tilde P=\tilde P$ for all $\tilde P$, and there is no $\tilde U$ with $\tilde P\wedge\tilde U=\tilde P$ for all $\tilde P$.

*Proof.* Every value of the operation has scalar part zero, whereas $\tilde P$ has scalar part $P_0$ in general; a unit would have to satisfy $\operatorname{Sc}(\tilde U\wedge\tilde P)=P_0$ for all $\tilde P$, and the left side is zero while the right side is not. $\square$

**Remark.** The absence of a unit is the first of the two structural differences from the symmetric half: the antisymmetric half is a multiplication without an identity and with values in a proper subspace, and it is the reason the operation generates a Lie algebra rather than an associative or a Jordan algebra. **The half is a bracket and not a product.**

### The Relation to the Commutator

**Proposition.** The operation is half the commutator of the algebra,

$$
[\tilde P,\tilde Q]=\tilde P\tilde Q-\tilde Q\tilde P=2\,(\tilde P\wedge\tilde Q),
$$

and the commutator is the cross product of the vector parts with the factor two, $[\tilde P,\tilde Q]=2\,\mathbf{P}\times\mathbf{Q}$.

*Proof.* The commutator is the difference of the two products, which is twice their half-difference; the value is twice the cross product of the previous proposition. $\square$

**Remark.** The commutator is alternating and $\mathbb{C}$-bilinear as well, and the two operations carry the same Lie algebra up to the scalar factor $2$: the assignment $\tilde P\mapsto2\tilde P$ is an isomorphism of $(\mathbb{B},[\ ,\ ])$ onto $(\mathbb{B},\wedge)$ read with the factor. The block uses the halved form $\wedge$, which is the form in which the structure constants are the signs of the cross product; the commutator is used in *The Unitary Lie Algebra*, where the bracket of the skew-Hermitian elements is the unhalved difference.

## The Jacobi Identity

### The Cyclic Sum

**Definition.** The **cyclic sum** of the operation on a triple $\tilde P,\tilde Q,\tilde R$ is

$$
\mathfrak J(\tilde P,\tilde Q,\tilde R)=(\tilde P\wedge\tilde Q)\wedge\tilde R+(\tilde Q\wedge\tilde R)\wedge\tilde P+(\tilde R\wedge\tilde P)\wedge\tilde Q.
$$

**Theorem (the Jacobi identity).** The operation satisfies

$$
(\tilde P\wedge\tilde Q)\wedge\tilde R+(\tilde Q\wedge\tilde R)\wedge\tilde P+(\tilde R\wedge\tilde P)\wedge\tilde Q=0
$$

for all $\tilde P,\tilde Q,\tilde R\in\mathbb{B}$.

*Proof.* Write the operation as the cross product of the vector parts, $\tilde P\wedge\tilde Q=\mathbf{P}\times\mathbf{Q}$. The three terms are $(\mathbf{P}\times\mathbf{Q})\times\mathbf{R}$, $(\mathbf{Q}\times\mathbf{R})\times\mathbf{P}$ and $(\mathbf{R}\times\mathbf{P})\times\mathbf{Q}$, and the vector triple product gives

$$
(\mathbf{P}\times\mathbf{Q})\times\mathbf{R}=\mathbf{Q}(\mathbf{P}\cdot\mathbf{R})-\mathbf{P}(\mathbf{Q}\cdot\mathbf{R}),
$$

with the two cyclic analogues. The six terms cancel in pairs, since $\mathbf{Q}(\mathbf{P}\cdot\mathbf{R})$ from the first term cancels $-\mathbf{Q}(\mathbf{R}\cdot\mathbf{P})$ from the third, and similarly for the other two pairs, using the symmetry of the scalar product of vectors. The identity therefore holds on arbitrary arguments; it was also verified on all sixty-four triples of the units and on general elements of $\mathbb{Q}(i)$ coefficients, where the cyclic sum vanishes identically. $\square$

**Remark.** The cyclic sum on the units is zero, and the vanishing is the whole content of the theorem: it is not a numerical accident of the basis but the Jacobi identity of the cross product, and it is inherited by the vector subspace, which is where the values lie. **The operation is a Lie bracket.**

### The Uniqueness among the Twelve

**Theorem (the only Lie product of the twelve).** Of the twelve operations $f_{+},f_{-}$ of the four general products of *The 12 Products of the Biquaternion Complex Space*, the antisymmetric plain algebra is the only one that satisfies the Jacobi identity.

*Proof.* The verification is the table of that article, computed there on the basis. Of the four antisymmetric parts, $\mathrm{AQA}$, $\mathrm{APS}$ and $\mathrm{AQS}$ fail the identity, with the witnesses $(e_0,e_1,e_2)$, $(e_0,e_1,e_2)$ and $(e_1,e_1,ie_2)$ and the cyclic sums $-e_3$, $e_3$ and $-2ie_2$; the witnesses were recomputed here, and the first of them, $\mathrm{AQA}$, is the failure nearest to the present block. The three symmetric parts other than $\mathrm{SPA}$ fail the Jordan identity, so none of them is a Lie product. Only $\mathrm{APA}$ remains, and the cyclic sum of the previous theorem shows that it passes. $\square$

**Remark.** The uniqueness is the reason the present block is the Lie Theory block of the row: the antisymmetric part of the plain product is the one place in the batch where a classical non-associative algebra, a Lie algebra, appears. The other three antisymmetric parts are brackets that fail their defining identity, and their failure is the subject of the corresponding blocks of the batch.

## The Sixteen Brackets of the Basis

The units $e_0,e_1,e_2,e_3$ satisfy $e_1e_2=e_3$, $e_2e_3=e_1$, $e_3e_1=e_2$ and $e_k^2=-e_0$, and the operation is read on them from the cross product of their vector parts.

**Theorem.** On the units,

$$
e_0\wedge e_j=0,\qquad e_i\wedge e_0=0,\qquad e_1\wedge e_2=e_3,\qquad e_2\wedge e_3=e_1,\qquad e_3\wedge e_1=e_2,
$$

with the alternating relations $e_2\wedge e_1=-e_3$, $e_3\wedge e_2=-e_1$, $e_1\wedge e_3=-e_2$, and $e_k\wedge e_k=0$; the sixteen brackets are the table

| $\wedge$ | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
|---|---|---|---|---|
| $e_0$ | $0$ | $0$ | $0$ | $0$ |
| $e_1$ | $0$ | $0$ | $e_3$ | $-e_2$ |
| $e_2$ | $0$ | $-e_3$ | $0$ | $e_1$ |
| $e_3$ | $0$ | $e_2$ | $-e_1$ | $0$ |

*Proof.* Each entry is the cross product of the vector parts of the two units. The unit $e_0$ has vector part zero, so its row and its column vanish; on $e_1,e_2,e_3$ the cross product reproduces the quaternion units, $e_1\times e_2=e_3$ and its cyclic analogues, and is alternating. Computed exactly on the sixteen pairs. $\square$

**Remark.** The table is the structure-constant table of the block, and it is the single table of the block that cannot be shortened: the seven entries of the first row and column are zero (the corner counted once), the three cyclic entries above the diagonal are the units, the three below are their negatives, and the three further diagonal entries vanish. **The tail of the table, on $e_1,e_2,e_3$, is the cross-product table of $\mathbb{C}^3$ and hence that of $\mathfrak{sl}(2,\mathbb{C})$**; the block is thus the complexification of the cross product, read inside the biquaternions.

## The Two Halves of the Plain Product

### The Reconstruction

**Theorem (the reconstruction).** The plain product is the sum of its two halves,

$$
\tilde P\tilde Q=\tilde P\bullet\tilde Q+\tilde P\wedge\tilde Q=\tfrac12\bigl(\tilde P\tilde Q+\tilde Q\tilde P\bigr)+\tfrac12\bigl(\tilde P\tilde Q-\tilde Q\tilde P\bigr),
$$

and the two halves determine one another's complement: the plain product is recovered from the symmetric plain algebra and the antisymmetric plain algebra together.

*Proof.* Adding the two halves gives $\tilde P\tilde Q$. The two are the symmetrisation and the antisymmetrisation of the same product, and the uniqueness of the split, *The Symmetric and Antisymmetric Parts of an Algebra Product*, says that no other pair of a symmetric and an antisymmetric operation has the same sum. $\square$

**Remark.** The two halves are the SPA block and the APA block, and the reconstruction is the statement that the general plain algebra $\mathrm{GPA}$ is the sum $\mathrm{SPA}+\mathrm{APA}$ of its two parts, read as operations on the same space.

### What the Square Sees

**Proposition (the square is the symmetric half).** The diagonal of the antisymmetric half is zero, $\tilde P\wedge\tilde P=0$, and the polarisation of the square of the algebra involves only the symmetric half:

$$
(\tilde P+\tilde Q)^2-\tilde P^2-\tilde Q^2=\tilde P\tilde Q+\tilde Q\tilde P=2\,(\tilde P\bullet\tilde Q).
$$

*Proof.* The first statement is the alternation of the previous section. The second is the polarisation identity of *The Symmetric and Antisymmetric Parts of an Algebra Product*, and it is displayed here only to record its consequence. $\square$

**Remark.** **The square map is invisible to the antisymmetric half.** The symmetrisation and the square determine one another, by the polarisation and by the identity $\tilde P\bullet\tilde P=\tilde P^2$, whereas the square of an element carries no information about the antisymmetric half; the plain product and its opposite have the same square and the same symmetric half, and differ exactly in the sign of the antisymmetric half. The antisymmetric plain algebra is therefore the half of the plain product that the power maps of the algebra cannot see, and it is recovered from the product only through the commutator.

## Worked Examples

**Two pure units.** $e_1\wedge e_2=e_3$ and $e_2\wedge e_1=-e_3$: the value is a pure vector, the scalar part is zero, and the reversal of the arguments reverses the value.

**A unit with the identity.** $e_0\wedge e_1=0$: the identity of the algebra has vector part zero and is annihilated by the operation, on both sides.

**The central element.** $(e_0+ie_0)\wedge e_1=0$: both scalar parts have no vector component, and the central element brackets to zero with everything.

**A scalar part that cancels.** For $\tilde P=e_0+e_1$ and $\tilde Q=e_0+e_2$, the plain products are $\tilde P\tilde Q=e_0+e_1+e_2+e_3$ and $\tilde Q\tilde P=e_0+e_1+e_2-e_3$, whose scalar parts and whose $e_1$ and $e_2$ coefficients agree, so the half-difference is $e_3$: $\tilde P\wedge\tilde Q=e_3$, and the scalar parts that agree have cancelled, as the first proposition predicts.

**A cyclic sum on the units.** For $\tilde P=e_1,\tilde Q=e_2,\tilde R=e_3$ the three terms are $(e_1\wedge e_2)\wedge e_3=e_3\wedge e_3=0$, $(e_2\wedge e_3)\wedge e_1=e_1\wedge e_1=0$ and $(e_3\wedge e_1)\wedge e_2=e_2\wedge e_2=0$: the cyclic sum is zero, the basis instance of the Jacobi identity.

**A witness of the neighbouring failure.** For the antisymmetric quaternionic algebra $\mathrm{AQA}$ the same triple $(e_0,e_1,e_2)$ gives the cyclic sum $-e_3$, as recomputed here from its definition $\tfrac12(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P)$; the two brackets agree on $e_1,e_2,e_3$ and separate on $e_0$, which is the direction the natural conjugation reverses.

## The Placement of the Block among the Twelve

The twelve operations decompose by product and by half, and the present block is the antisymmetric half of the plain product.

| product | symmetric half | antisymmetric half |
|---|---|---|
| plain $\tilde P\tilde Q$ | $\mathrm{SPA}$: the Jordan product on $\mathbb{B}$ | $\mathrm{APA}$: the bracket $\mathbf{P}\times\mathbf{Q}$ |
| quaternionic $\tilde P^{\natural}\tilde Q$ | $\mathrm{SQA}$ | $\mathrm{AQA}$, no Jacobi |
| plain sesquilinear $\tilde P\tilde Q^{*}$ | $\mathrm{SPS}$ | $\mathrm{APS}$, no Jacobi |
| quaternionic sesquilinear $\tilde P^{\natural}\tilde Q^{*}$ | $\mathrm{SQS}$ | $\mathrm{AQS}$, no Jacobi |

**Remark.** The block is the second of the four blocks of the batch and it sits immediately after the SPA block in the menu. Its own Lie structure is developed in the rest of the block; its relation to the symmetric half is the reconstruction above; and its relation to the other three antisymmetric parts is the table, in which it is the row that passes the identity the other three fail. **The block owns the reading of the plain product as a bracket, and nothing of the general plain product or of its operators, which remain with the $\mathrm{GPA}$ articles.**

The Lie algebra that the operation makes of $\mathbb{B}$ is *The Lie Algebra of the Antisymmetric Plain Algebra*: its centre is the centre $\mathbb{C}_{\mathbb{B}}$ of the algebra, its image $\mathrm{Vect}(\mathbb{B})$ is a Lie subalgebra isomorphic to $\mathfrak{sl}(2,\mathbb{C})$, and on the real forms the quaternion subspace carries $\mathbb{R}e_0\oplus\mathfrak{su}(2)$ and the anti-Hermitian subspace carries $\mathfrak{u}(2)$. The invariant form of the operation is *The Killing Form of the Antisymmetric Plain Algebra*, its reading on the six subspaces is *The Six Subspaces under the Antisymmetric Plain Algebra of Biquaternions*, its adjoints and derivations are *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra*, and its two matrix models are *The Antisymmetric Plain Algebra in the Matrix Representations*.

## Summary

The antisymmetric part of the plain product of the biquaternions is the operation $\tilde P\wedge\tilde Q=\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)$, equal to the cross product $\mathbf{P}\times\mathbf{Q}$ of the two vector parts, of scalar part zero, $\mathbb{C}$-bilinear and alternating, with image the vector subspace $\mathrm{Vect}(\mathbb{B})$ and without a unit. It is half the commutator, $[\tilde P,\tilde Q]=2(\tilde P\wedge\tilde Q)$, and it satisfies the Jacobi identity, with the cyclic sum recomputed as zero on the sixty-four triples of the units; of the twelve operations of the batch it is the only one that does, so it is the only Lie product among them. Its sixteen brackets on the basis have the seven vanishing entries of the identity row and column and, on $e_1,e_2,e_3$, the cross-product table of $\mathbb{C}^3$ and hence of $\mathfrak{sl}(2,\mathbb{C})$. The plain product is reconstructed as $\mathrm{GPA}=\mathrm{SPA}+\mathrm{APA}$, and the square map sees only the symmetric half, so the antisymmetric half is recovered from the product only through the commutator.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\wedge\tilde Q=\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)$ | the antisymmetric plain algebra, $\mathrm{APA}$, the operation of the block |
| $\tilde P\wedge\tilde Q=\mathbf{P}\times\mathbf{Q}$ | its value, the cross product of the vector parts |
| $\operatorname{Sc}(\tilde P\wedge\tilde Q)=0$ | the scalar part of every value vanishes |
| $[\tilde P,\tilde Q]=\tilde P\tilde Q-\tilde Q\tilde P=2(\tilde P\wedge\tilde Q)$ | the commutator of the algebra, twice the operation |
| $\tilde P\bullet\tilde Q=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ | the symmetric plain algebra, $\mathrm{SPA}$, the other half |
| $\mathrm{GPA}=\mathrm{SPA}+\mathrm{APA}$ | the reconstruction of the plain product from its two halves |
| $\mathrm{Vect}(\mathbb{B})=\mathbb{C}e_1\oplus\mathbb{C}e_2\oplus\mathbb{C}e_3$ | the image of the operation, the vector subspace |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ | the centre of the algebra, annihilated by the operation |
| $e_1\wedge e_2=e_3$, $e_2\wedge e_3=e_1$, $e_3\wedge e_1=e_2$ | the three non-trivial brackets of the units |
| $\mathfrak J(\tilde P,\tilde Q,\tilde R)=0$ | the cyclic sum, the Jacobi identity of the block |

## Further Reading

- *The Symmetric and Antisymmetric Parts of an Algebra Product* (`articles_maths/the-symmetric-and-antisymmetric-parts-of-an-algebra-product.md`), for the split of a product into its two halves, its uniqueness and the admissibility conditions
- *The 12 Products of the Biquaternion Complex Space* (`articles_maths/the-12-products-of-the-biquaternion-complex-space.md`), for the table of the twelve operations, the witnesses of the three failing Jacobi identities and the two that pass, and for the same twelve operations read from the side of the order symmetry
- *The Lie Algebra of the Antisymmetric Plain Algebra* (`articles_maths/the-lie-algebra-of-the-antisymmetric-plain-algebra.md`), for the centre, the image, the identifications with $\mathfrak{sl}(2,\mathbb{C})$, $\mathfrak{su}(2)$ and $\mathfrak{u}(2)$, and the enveloping algebra
- *The Unitary Lie Algebra* (`articles_maths/the-unitary-lie-algebra.md`), for the bracket of the skew-Hermitian elements, the unhalved commutator and the group of linear maps preserving the form
- *Introduction to the General Plain Algebra of Biquaternions* (`articles_maths/introduction-to-the-general-plain-algebra-of-biquaternions.md`), for the plain product and the group it defines
- *Introduction to the Six Subspaces* (`articles_maths/introduction-to-the-six-subspaces.md`), for the six distinguished subspaces on which the block is read
