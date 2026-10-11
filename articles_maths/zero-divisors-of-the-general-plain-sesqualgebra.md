# __Zero Divisors of the General Plain Sesqualgebra__

## Introduction

The general plain sesqualgebra is the operation $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ on the biquaternion space (*Introduction to the General Plain Sesqualgebra of Biquaternions*). This article studies its **zero divisors**: the nonzero elements that annihilate a nonzero element.

A zero divisor names a product, and the definition is relative; it is stated once for a general product in *Definitions for the Study of the 12 Algebraic Structures* and is read here on the block. The criterion of the block is **one element**: because the involution ${}^{*}$ is a bijection of $\mathbb{B}$, the vanishing of $\tilde Q\star\tilde R=\tilde Q\tilde R^{*}$ is the vanishing of the plain product $\tilde Q\tilde R^{*}$, and $\tilde R^{*}$ ranges over all of $\mathbb{B}$ as $\tilde R$ does, so the block's zero-divisor set is exactly the plain one, the nonzero elements of the zero-divisor cone $\{c(\tilde Q)=\sum_\mu Q_\mu^{2}=0\}$, which is also the common set of the four general products (*The Zero Divisors and the Four General Products*). The **set** is therefore inherited unchanged; what is not inherited is the **internal structure** the parent reads on it. The parent reads a square, and its pure family is the nonzero nilpotents of index two; the block reads its own square, the Hermitian element $\tilde Q\star\tilde Q=\tilde Q\tilde Q^{*}$, on which the pure family is **not** square-zero, and it is the pure family that is the block's nilpotent family, with the index three instead of two (*Nilpotents of the General Plain Sesqualgebra*). The article states the coincidence, computes the annihilators, and separates the part of the classification that survives from the part that does not.

**Placement.** The article is the third entry of the *Common Theory* section of the block, after *Norm and Invertibility in the General Plain Sesqualgebra* and before the square roots of the central values. It uses the product and the class of the introduction, the algebraic norm and the invertibility criterion of *Norm and Invertibility in the General Plain Sesqualgebra*, and the common zero-divisor set of the four general products.

**Boundaries.** The product, its class and its placement are *Introduction to the General Plain Sesqualgebra of Biquaternions*; the relative definitions of the zero divisor, the annihilator and the regular element are *Definitions for the Study of the 12 Algebraic Structures*; the common set of the four general products and the theorem that the four coincide are *The Zero Divisors and the Four General Products*, and the same set read on the plain product with its two families and their geometry is *Zero Divisors of the General Plain Algebra*, *Idempotents of the General Plain Algebra* and *Nilpotents of the General Plain Algebra*. The algebraic norm and the invertibility criterion are *Norm and Invertibility in the General Plain Sesqualgebra*; the square-zero set of the block is *The Square-Zero Elements of the Four General Products*. Nothing topological and nothing metric appears.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ with $e_1e_2=e_3$ and central scalar imaginary $i$. A general element is $\tilde Q=\sum_{\mu=0}^{3}Q_\mu e_\mu=Q_0e_0+\mathbf Q$ with $\mathbf Q=Q_1e_1+Q_2e_2+Q_3e_3$ and $Q_\mu\in\mathbb{C}$; the natural conjugation is $\tilde Q^{\natural}=Q_0-\mathbf Q$, the coefficientwise conjugation is $\overline{\tilde Q}=\overline{Q_0}e_0+\overline{\mathbf Q}$, and the Hermitian conjugation is $\tilde Q^{*}=\overline{\tilde Q^{\natural}}=\overline{Q_0}-\overline{\mathbf Q}$. Juxtaposition is the **plain** product and $\star$ the block, $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$. The **central square** is $c(\tilde Q)=\tilde Q\tilde Q^{\natural}=Q_0^{2}+(\mathbf Q,\mathbf Q)$ with $(\mathbf Q,\mathbf Q)=Q_1^{2}+Q_2^{2}+Q_3^{2}$, and its vanishing set, the origin removed, is the common zero-divisor cone.

## The Criterion

**Theorem (the criterion of the block).** For nonzero $\tilde Q$, the following are equivalent:

1. $\tilde Q$ is a left zero divisor of $\star$: there is a nonzero $\tilde R$ with $\tilde Q\star\tilde R=0$;
2. $\tilde Q$ is a right zero divisor of $\star$: there is a nonzero $\tilde R$ with $\tilde R\star\tilde Q=0$;
3. $\tilde Q$ is a zero divisor of the plain product: there is a nonzero $\tilde R$ with $\tilde Q\tilde R=0$;
4. $c(\tilde Q)=0$.

*Proof.* The equation $\tilde Q\star\tilde R=\tilde Q\tilde R^{*}=0$ is, because ${}^{*}$ is a bijection, the existence of a nonzero $\tilde Z=\tilde R^{*}$ with $\tilde Q\tilde Z=0$, which is (3). The right equation is the same: $\tilde R\star\tilde Q=\tilde R\tilde Q^{*}=0$, and applying ${}^{*}$ gives $\tilde Q\tilde R^{*}=0$ again, which is (1). The equivalence of (3) and (4) is the invertibility criterion of the parent algebra, reproduced in *Zero Divisors of the General Plain Algebra*: $\tilde Q$ is a zero divisor of the plain product exactly when $c(\tilde Q)=0$.

**Corollary (the set).** The zero-divisor set of the block is

$$
\mathcal{Z}_\star=\{\tilde Q\neq0: c(\tilde Q)=0\}=\{\tilde Q\neq0: Q_0^{2}+(\mathbf Q,\mathbf Q)=0\},
$$

the nonzero elements of the complex cone $\{c=0\}$, of complex dimension three; every zero divisor of the block is **two-sided**, and the set is the common zero-divisor set of the four general products.

*Proof.* The criterion gives the set, and the equivalence of the one-sided statements makes every member two-sided. The cone is the zero set of a non-degenerate quadratic form on $\mathbb{C}^{4}$, hence of complex dimension three, and it is the common set by *The Zero Divisors and the Four General Products*, §*The Four Zero-Divisor Sets Coincide*.

**Remark (the criterion of the block is one element, like the parent's).** Unlike the symmetric plain sesqualgebra, whose criterion is a bilinear equation in the element and its partner, the block's criterion is a single quadratic equation $c(\tilde Q)=0$ in the element alone, and the reason is that its annihilation equation $\tilde Q\tilde R^{*}=0$ still has the element alone on the left. The block changes the square and not the shape of the criterion, and its zero divisors are a cone.

## The Two Annihilators

**Definition.** For $\tilde Q$ a zero divisor of the block, the **right annihilator** is $B_\star(\tilde Q)=\{\tilde X:\tilde Q\star\tilde X=0\}$ and the **left annihilator** is $A_\star(\tilde Q)=\{\tilde X:\tilde X\star\tilde Q=0\}$. The annihilator is relative to the product as the zero divisor is, and the general definition is *Definitions for the Study of the 12 Algebraic Structures*, §*The Zero Divisor and the Annihilator*; the product here is the general plain sesquilinear product $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ of the block.

**Theorem (the two annihilators are equal, and they are the conjugate of the plain annihilator).** For every $\tilde Q$,

$$
A_\star(\tilde Q)=B_\star(\tilde Q)=K(\tilde Q)^{*},\qquad K(\tilde Q)=\{\tilde Z:\tilde Q\tilde Z=0\},
$$

where $K(\tilde Q)^{*}=\{\tilde Z^{*}:\tilde Z\in K(\tilde Q)\}$ is the image of $K(\tilde Q)$ under the involution. For a nonzero zero divisor the common annihilator has **complex dimension two**; for a regular element ($c(\tilde Q)\neq0$) it is $\{0\}$. The **two-sided annihilator** of the block is $\{0\}$.

*Proof.* The right annihilator is $B_\star(\tilde Q)=\{\tilde X:\tilde Q\tilde X^{*}=0\}=\{\tilde X:\tilde X^{*}\in K(\tilde Q)\}=K(\tilde Q)^{*}$, because $\tilde X\mapsto\tilde X^{*}$ is a bijection. For the left annihilator, $\tilde X\star\tilde Q=\tilde X\tilde Q^{*}=0$ is equivalent to $\bigl(\tilde X\tilde Q^{*}\bigr)^{*}=\tilde Q\tilde X^{*}=0$, so $A_\star(\tilde Q)=B_\star(\tilde Q)$. The dimension is that of the plain annihilator: in the matrix model *The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* a nonzero zero divisor is a nonzero singular matrix of rank one, and $K(\tilde Q)$ consists of the matrices whose columns lie in the kernel line of $\tilde Q$, a complex space of dimension two; a regular element is invertible and its annihilator is $\{0\}$. The two-sided annihilator is the set of $\tilde A$ with $\tilde A\star\tilde X=0$ for all $\tilde X$, that is $\tilde A\tilde X^{*}=0$ for all $\tilde X$; taking $\tilde X=e_0$ gives $\tilde A=0$.

**Remark (the annihilator is a plane, and the two sides are identified).** The block's annihilators are the plain annihilator $K(\tilde Q)=\{\tilde Z:\tilde Q\tilde Z=0\}$ carried through the involution; they are the same on the two sides, they have complex dimension two for every nonzero zero divisor, and they collapse to the origin exactly off the cone. The parent's two annihilators, $\{\tilde Z:\tilde Q\tilde Z=0\}$ and $\{\tilde X:\tilde X\tilde Q=0\}$, are different subspaces in general — at a rank-one $\tilde Q$ an element can annihilate on one side and not on the other — and the block makes them equal; the equality is the work of the involution that sits in the second slot.

## The Two Families, and What the Block Does to Them

The plain product partitions its zero divisors by the scalar coordinate (*Zero Divisors of the General Plain Algebra*): the **pure family** has $Q_0=0$ and $(\mathbf Q,\mathbf Q)=0$, and its nonzero members are the nilpotents, $\tilde Q^{2}=0$; the **non-pure family** has $Q_0\neq0$, and its members are the nonzero complex multiples of the nontrivial idempotents $\tfrac12(e_0+\tilde\Xi i)$ over the roots $\tilde\Xi$ of $-1$. The partition is by the scalar coordinate, which is a datum of the element and not of the product, so it survives verbatim for the block; what does not survive is the **reading of the two families through the square**.

**Proposition (the pure family is not square-zero for the block).** Let $\tilde Q$ be a nonzero pure zero divisor, $\tilde Q=\mathbf Q$ with $(\mathbf Q,\mathbf Q)=0$. Then its plain square vanishes, but its block-square does not:

$$
\tilde Q^{2}=0,\qquad \tilde Q\star\tilde Q=\tilde Q\tilde Q^{*}=\mathrm{Sc}\bigl(\tilde Q\tilde Q^{*}\bigr)e_0+\mathrm{Vect}\bigl(\tilde Q\tilde Q^{*}\bigr)\neq0 .
$$

*Proof.* The plain square vanishes because $\tilde Q^{2}=(\mathbf Q,\mathbf Q)e_0$ by the product rule and $(\mathbf Q,\mathbf Q)=0$. For the block-square, $\mathrm{Sc}(\tilde Q\tilde Q^{*})=\sum_\mu\lvert Q_\mu\rvert^{2}=H(\tilde Q)$, the algebraic norm of the block, which is positive for $\tilde Q\neq0$ by the definiteness of *Norm and Invertibility in the General Plain Sesqualgebra*; so the block-square is nonzero. The witness $\tilde Q=e_1+ie_2$ has $\tilde Q\star\tilde Q=2e_0+2ie_3$.

**Remark (the index of the pure family is raised).** The parent calls the pure family the nonzero **nilpotents** of index two; the block calls the same family its nonzero **nilpotents** of index three, because the block-square of a pure zero divisor does not vanish and the third power does (*Nilpotents of the General Plain Sesqualgebra*). The pure zero divisors are therefore a family of zero divisors that **are** nilpotents of the block, with the index raised from two to three, and the non-pure zero divisors are the family that is **not** nilpotent. The partition of the parent is kept, and the index attached to each family is read from the square of the product in force.

**Proposition (the non-pure family and the idempotents of the block).** The non-pure zero divisors are the nonzero complex multiples of the nontrivial idempotents of the plain product, and among them exactly the **Hermitian idempotents** $\tfrac12(e_0+i\hat\mu)$ over the real unit vectors $\hat\mu$ are idempotents of the block; the others are zero divisors of the block and not idempotents of it.

*Proof.* The plain description is *Zero Divisors of the General Plain Algebra*. An idempotent of the block is a Hermitian idempotent of the plain product (*Idempotents of the General Plain Sesqualgebra*), and a Hermitian idempotent $\tilde\Pi$ has $\tilde\Pi\star\tilde\Pi=\tilde\Pi\tilde\Pi^{*}=\tilde\Pi^{2}=\tilde\Pi$; the Hermitian ones are those with a real root $\tilde\Xi=\pm\hat\mu$, that is the family $\tfrac12(e_0+i\hat\mu)$. A multiple $\lambda\tilde\Pi$ with $\lambda\neq1$ is a zero divisor but is idempotent for neither product unless $\lambda=1$.

**Remark (the scalar part of a block idempotent is fixed).** The block idempotents $\tfrac12(e_0+i\hat\mu)$ have scalar part $\tfrac12$, which is the positive value the algebraic norm $H(\tilde\Pi)=\mathrm{Sc}(\tilde\Pi\star\tilde\Pi)=\sum_\mu\lvert\Pi_\mu\rvert^{2}$ forces on any idempotent of the block; in particular $c\bigl(\tfrac12(e_0+i\hat\mu)\bigr)=\tfrac14(1-(\hat\mu,\hat\mu))=0$, so every block idempotent is a zero divisor, of the non-pure family. The unit $e_0$ is not a zero divisor, $c(e_0)=1$.

## The Comparison with the Parent and with the Four General Products

| clause | general plain algebra | general plain sesqualgebra |
|---|---|---|
| criterion | $c(\tilde Q)=Q_0^{2}+(\mathbf Q,\mathbf Q)=0$ | $c(\tilde Q)=0$, the same |
| the set | the cone $\{c=0\}$ without the origin | the same cone without the origin |
| sides | left and right, generally distinct sets of partners | left and right, with the same annihilator |
| pure family | $Q_0=0$, isotropic, the nonzero nilpotents of index two | $Q_0=0$, isotropic, the nonzero nilpotents of index three |
| non-pure family | $Q_0\neq0$, multiples of idempotents, not nilpotent | the same; those that are block-idempotent are the Hermitian ones |
| annihilator of a zero divisor | the plain annihilator $K(\tilde Q)=\{\tilde Z:\tilde Q\tilde Z=0\}$, of dimension two; the two sides are generally different | the same space carried through the involution, of dimension two, equal on the two sides |

The block's set is the common set of the four general products, and the coincidence is a theorem of the space and not a property of the block (*The Zero Divisors and the Four General Products*). What the block adds is the reading of the set through its own square: the scalar-coordinate partition is inherited, because it is a partition of the elements, and the **index** attached to the pure family is read from the square in force, so it becomes three in place of two. The four general products share the set, the pure family and the criterion $Q_0=0$; they do not share the square, and the index of nilpotency is the visible consequence.

## Summary

The zero divisors of the general plain sesqualgebra are decided by one equation in the element alone, and the equation is the parent's: because $\tilde P\star\tilde R=\tilde P\tilde R^{*}$ and ${}^{*}$ is a bijection, an element is a zero divisor of the block exactly when it is a zero divisor of the plain product, that is exactly when its central square vanishes, $c(\tilde Q)=Q_0^{2}+(\mathbf Q,\mathbf Q)=0$ with $\tilde Q\neq0$. The **set** is the nonzero zero-divisor cone, of complex dimension three, which is the common set of the four general products, and every member is **two-sided**. The **annihilators** are equal on the two sides and are the image under the involution of the plain annihilator $K(\tilde Q)=\{\tilde Z:\tilde Q\tilde Z=0\}$, a **complex plane of dimension two** for every nonzero zero divisor and the origin otherwise; the two-sided annihilator is $\{0\}$. The **two families** of the parent are inherited as a partition of the elements, since the partition is read on the scalar coordinate: the pure family has $Q_0=0$ and isotropic vector part, and the non-pure family consists of the nonzero complex multiples of the nontrivial idempotents. What changes is the **square-theoretic reading**: a pure zero divisor is a nilpotent of index two for the parent and a nilpotent of **index three** for the block, its block-square being the nonzero Hermitian element $\tilde Q\tilde Q^{*}$ with positive scalar part; the non-pure zero divisors are nilpotent for neither; and of the non-pure multiples, exactly the Hermitian idempotents $\tfrac12(e_0+i\hat\mu)$ are idempotents of the block. The block keeps the set, keeps the criterion, the partition and the annihilators, and changes the index.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ | the product of the block |
| $c(\tilde Q)=\tilde Q\tilde Q^{\natural}=Q_0^{2}+(\mathbf Q,\mathbf Q)$ | the central square |
| $\mathcal{Z}_\star=\{\tilde Q\neq0:c(\tilde Q)=0\}$ | the zero-divisor set, the nonzero cone |
| $\tilde Q\star\tilde R=0\Leftrightarrow\tilde Q\tilde R^{*}=0$ | the annihilation equation |
| $A_\star(\tilde Q)$, $B_\star(\tilde Q)$ | the left and the right annihilators, equal |
| $K(\tilde Q)^{*}$, $K(\tilde Q)=\{\tilde Z:\tilde Q\tilde Z=0\}$ | the common annihilator, the plain annihilator carried through the involution |
| $Q_0=0$ | the pure family, isotropic: the nilpotents of the block, index three |
| $Q_0\neq0$ | the non-pure family, multiples of the idempotents, not nilpotent |
| $\tfrac12(e_0+i\hat\mu)$ | the Hermitian idempotents, zero divisors and block idempotents |

## Further Reading

- *Introduction to the General Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-general-plain-sesqualgebra-of-biquaternions.md`), for the product, the class and the involution in the second slot.
- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the relative definitions of the zero divisor and the annihilator.
- *The Zero Divisors and the Four General Products* (`articles_maths/the-zero-divisors-and-the-four-general-products.md`), for the theorem that the four zero-divisor sets coincide and for the one-sided inverse equations.
- *Zero Divisors of the General Plain Algebra* (`articles_maths/zero-divisors-of-the-general-plain-algebra.md`), for the criterion $c(\tilde Q)=0$, the pure and the non-pure families and their geometry.
- *Norm and Invertibility in the General Plain Sesqualgebra* (`articles_maths/norm-and-invertibility-in-the-general-plain-sesqualgebra.md`), for the algebraic norm, the invertibility criterion and the definiteness of the scalar form.
- *Idempotents of the General Plain Sesqualgebra* (`articles_maths/idempotents-of-the-general-plain-sesqualgebra.md`), for the Hermitian idempotents that are the block idempotents among the non-pure zero divisors.
- *Nilpotents of the General Plain Sesqualgebra* (`articles_maths/nilpotents-of-the-general-plain-sesqualgebra.md`), for the pure family read as the nilpotent family, of index three.
