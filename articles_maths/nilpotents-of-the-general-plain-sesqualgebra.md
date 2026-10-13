# __Nilpotents of the General Plain Sesqualgebra__

## Introduction

The general plain sesqualgebra is the operation $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ on the biquaternion space (*Introduction to the General Plain Sesqualgebra of Biquaternions*). This article determines its **nilpotents**: the nonzero elements $\tilde\Upsilon$ with a vanishing power,

$$
\tilde\Upsilon^{\star k}=0\quad\text{for some }k\geq1,
$$

the power being the left-nested reading of *Definitions for the Study of the 12 Algebraic Structures*, $\tilde X^{\star k}=\bigl(\cdots(\tilde X\star\tilde X)\star\tilde X\cdots\bigr)$, which for the block is $\tilde X^{\star k}=\tilde X(\tilde X^{*})^{k-1}$. A nilpotent is relative to a product, and throughout this article the product is the block's: the general definition is §*The Nilpotent* of *Definitions for the Study of the 12 Algebraic Structures*. The origin is a nilpotent, the **trivial** one, and the article is concerned with the nonzero ones.

The answer is not the parent's. The block has **no nonzero square-zero element**, so its index of nilpotency is never two; but it **has** nilpotents, of index three, and they are exactly the parent's **pure zero divisors**, the elements with vanishing scalar coordinate and isotropic vector part. The block therefore keeps the parent's nilpotent **set** — the pure cone $\{\Upsilon_0=0,\ (\boldsymbol\Upsilon,\boldsymbol\Upsilon)=0\}$ — and changes its **index**, from two to three, because its square is the Hermitian square $\tilde X\tilde X^{*}$ instead of the plain square $\tilde X^{2}$. The non-pure zero divisors of the parent are zero divisors of the block and are **not** nilpotents of it, so the implication of the parent, "the pure family is the nilpotent family", holds here in a transmuted form: the pure family is the nilpotent family and the index is three.

**Placement.** The article is the seventh and last entry of the *Common Theory* section of the block, after the idempotents. It uses the product and the class of the introduction, the square and the zero-divisor criterion of *Norm and Invertibility in the General Plain Sesqualgebra* and *Zero Divisors of the General Plain Sesqualgebra*, the roots of the central values of *Square Roots of Minus One, Zero and Plus One in the General Plain Sesqualgebra*, and the matrix model.

**Boundaries.** The product, its class and its placement are *Introduction to the General Plain Sesqualgebra of Biquaternions*; the relative definition of the nilpotent, of the index of nilpotency and of the square-zero element is *Definitions for the Study of the 12 Algebraic Structures*, §*The Nilpotent*. The square-zero set of the block and of the four general products is *Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*; the nilpotents and the two families of the parent are *Nilpotents of the General Plain Algebra* and *Zero Divisors of the General Plain Algebra*; the matrix model that carries the powers is *The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*; the idempotents are *Idempotents of the General Plain Sesqualgebra*. Nothing topological and nothing metric appears.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ with $e_1e_2=e_3$ and central scalar imaginary $i$. An element is $\tilde Q=Q_0e_0+\mathbf Q$ with $\mathbf Q=Q_1e_1+Q_2e_2+Q_3e_3$ and $Q_\mu\in\mathbb{C}$; the Hermitian conjugation is $\tilde Q^{*}=\overline{\tilde Q^{\natural}}=\overline{Q_0}-\overline{\mathbf Q}$. The product is $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$, and the **central square** is $C(\tilde Q)=\sum_\mu Q_\mu^{2}=Q_0^{2}+(\mathbf Q,\mathbf Q)$. An element is **pure** when $Q_0=0$, that is when it lies in the vector part $\mathbb{C}\otimes\mathbb{R}^{3}$. A nilpotent is written $\tilde\Upsilon$ (§*The nilpotent convention* of *Conventions in Mathematics*), with $\tilde\Upsilon=\Upsilon_0e_0+\boldsymbol\Upsilon$; a general element whose powers are at stake keeps the letter $\tilde X$.

## The Powers of the Block

**Proposition (the powers are conjugate-linear iterations).** For every $\tilde X$ and every $k\geq1$,

$$
\tilde X^{\star k}=\tilde X(\tilde X^{*})^{k-1},
$$

so $\tilde X^{\star2}=\tilde X\tilde X^{*}$, $\tilde X^{\star3}=\tilde X\tilde X^{*}\tilde X^{*}$, and in the matrix model $\mathsf{M}_2(\tilde X^{\star k})=\mathsf{M}_2(\tilde X)\mathsf{M}_2(\tilde X)^{\dagger(k-1)}$.

*Proof.* By induction on the left-nested reading: $\tilde X^{\star(k+1)}=\tilde X^{\star k}\star\tilde X=\tilde X^{\star k}\tilde X^{*}=\tilde X(\tilde X^{*})^{k-1}\tilde X^{*}=\tilde X(\tilde X^{*})^{k}$. The matrix display is the multiplicativity $\mathsf{M}_2(\tilde P\star\tilde Q)=\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger}$ and $\mathsf{M}_2(\tilde X^{*})=\mathsf{M}_2(\tilde X)^{\dagger}$.

**Remark (why the index can be larger than two).** The square of the block is $\tilde X\tilde X^{*}$, the Hermitian square, and the iterated powers are the products of $\tilde X$ with the successive powers of the conjugate transpose. The index is therefore a property of the pair $(\mathsf{M}_2(\tilde X),\mathsf{M}_2(\tilde X)^{\dagger})$ and not of the plain square, and it can be larger than two even when the plain element is a square-zero element of index two.

## The Criterion of the Nilpotent

**Theorem (the nilpotents are the pure zero divisors, of index three).** For $\tilde\Upsilon\neq0$ the following are equivalent:

1. $\tilde\Upsilon$ is a nilpotent of the block;
2. $\tilde\Upsilon^{\star3}=0$;
3. $\tilde\Upsilon$ is pure and of vanishing central square: $\Upsilon_0=0$ and $C(\tilde\Upsilon)=0$;
4. $\tilde\Upsilon$ is a pure zero divisor of the plain product.

When they hold, the index of nilpotency is exactly three: $\tilde\Upsilon^{\star2}\neq0$.

*Proof.* Write $A=\mathsf{M}_2(\tilde\Upsilon)$, so that $\tilde\Upsilon^{\star k}=0$ is $A(A^{\dagger})^{k-1}=0$ and $\det A=C(\tilde\Upsilon)$, $\operatorname{Tr}A=2\Upsilon_0$. First, if $A$ is invertible then $\det\bigl(A(A^{\dagger})^{m}\bigr)=(\det A)\,\overline{(\det A)}^{m}$ has modulus $\lvert\det A\rvert^{m+1}\neq0$, so no nilpotent is regular and $\operatorname{rank}A\leq1$, that is $\det A=0$; with $\tilde\Upsilon\neq0$ this is $\operatorname{rank}A=1$. Write $A=\sigma\,\mathbf u\mathbf v^{\dagger}$ with $\sigma>0$ and $\mathbf u,\mathbf v$ unit; then $A(A^{\dagger})^{m}=\sigma^{m+1}(\mathbf u^{\dagger}\mathbf v)^{m-1}\mathbf u\mathbf u^{\dagger}$, whose vanishing for some $m$ is $\mathbf u^{\dagger}\mathbf v=0$, and $\operatorname{Tr}A=\sigma\mathbf v^{\dagger}\mathbf u=\sigma\overline{\mathbf u^{\dagger}\mathbf v}$. Hence $A(A^{\dagger})^{m}=0$ for some $m$ if and only if $\operatorname{Tr}A=0$, and then $m=2$ already gives $A(A^{\dagger})^{2}=0$, that is $\tilde\Upsilon^{\star3}=0$; the case $m=1$ is impossible because $AA^{\dagger}=\sigma^{2}\mathbf u\mathbf u^{\dagger}\neq0$. Now $\operatorname{Tr}A=0$ is $\Upsilon_0=0$, and $\operatorname{rank}A=1$ is $C(\tilde\Upsilon)=0$; the equivalence of the first three statements follows, and the fourth is the description of the pure family of the parent. Finally $\tilde\Upsilon^{\star2}=\tilde\Upsilon\tilde\Upsilon^{*}$ has matrix $AA^{\dagger}$, of rank one, so it is nonzero: the index is three and not two.

**Direct proof of the pure case.** When $\Upsilon_0=0$ the element is $\tilde\Upsilon=\sum_{k=1}^{3}\Upsilon_ke_k$, its conjugate transpose is $\tilde\Upsilon^{*}=-\overline{\tilde\Upsilon}$, and the plain square of a pure element is $\tilde\Upsilon^{2}=-C(\tilde\Upsilon)e_0$; so if in addition $C(\tilde\Upsilon)=0$ then $\tilde\Upsilon^{2}=0$ and $\overline{\tilde\Upsilon}^{2}=\overline{\tilde\Upsilon^{2}}=0$, whence $\tilde\Upsilon^{\star3}=\tilde\Upsilon(\tilde\Upsilon^{*})^{2}=\tilde\Upsilon\overline{\tilde\Upsilon}^{2}=0$. The witness $\tilde\Upsilon=e_1+ie_2$ has $\Upsilon_0=0$, $C(\tilde\Upsilon)=1+i^{2}=0$ and $\tilde\Upsilon^{\star3}=0$, while $\tilde\Upsilon^{\star2}=2e_0+2ie_3\neq0$.

## The Absence of Square-Zero Elements

**Theorem (no nonzero square-zero element).** There is no nonzero $\tilde X$ with $\tilde X\star\tilde X=0$, so the block has no nilpotent of index two and its square-zero set is $\{0\}$.

*Proof.* The scalar part of the square is $\mathrm{Sc}(\tilde X\star\tilde X)=\sum_\mu\lvert X_\mu\rvert^{2}$ (*Norm and Invertibility in the General Plain Sesqualgebra*), which vanishes only at $\tilde X=0$. In the matrix model the square is $AA^{\dagger}$, positive semidefinite, whose vanishing forces $A=0$. The same statement is *Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, where the square-zero set of the general plain sesquilinear product is the origin alone.

**Remark (the parent and the sibling).** The parent has square-zero elements, the pure isotropic cone; the block has none but the origin, and its square-zero set is the origin alone. This is the one clause on which the block and the parent separate at the level of the square, and it is the reason the block's index is three: a pure isotropic element, square-zero for the parent, has a non-vanishing Hermitian square for the block and vanishes only at the third power. The sibling symmetric plain sesqualgebra also has no **nonzero** square-zero element, and it has index-three nilpotents whose square is the nonzero central element $\bigl(\sum_\mu\lvert\Upsilon_\mu\rvert^{2}\bigr)e_0$ (written $H(\tilde\Upsilon)e_0$ in that block, where $H$ is the algebraic norm of the block); the block's index-three nilpotents have a **non-central** square $\tilde\Upsilon\tilde\Upsilon^{*}$, and that is the difference between the two siblings.

## The Nilpotent Set

**Corollary (the set).** The nilpotent set of the block is

$$
\mathcal{N}_\star=\{\tilde\Upsilon\neq0:\ \Upsilon_0=0,\ (\boldsymbol\Upsilon,\boldsymbol\Upsilon)=0\},
$$

the nonzero elements of the **pure isotropic cone**, of complex dimension two, which is the pure zero-divisor cone of the parent. Every nilpotent is a two-sided zero divisor, and the non-pure zero divisors — the nonzero complex multiples of the nontrivial idempotents with $\Upsilon_0\neq0$ — are **not** nilpotent.

*Proof.* The first display is the criterion. The set is the isotropic quadric of the two-complex-dimensional vector part, of complex dimension two, and it is a subset of the zero-divisor set $\mathcal{C}\setminus\{0\}$ of *Zero Divisors of the General Plain Sesqualgebra*. A non-pure zero divisor has $\Upsilon_0\neq0$, so it fails the criterion and is not nilpotent.

**Remark (the two families of the parent, re-read).** The parent partitions its zero divisors into the pure family, which is its nilpotent family of index two, and the non-pure family, which is not nilpotent. The block inherits the partition and moves the nilpotent family from the index two to the index three: the partition is the same, the criterion $\Upsilon_0=0$ is the same, the index is not. The **index of nilpotency is therefore a product-relative notion** even on the same set, and the block is the clean illustration: the same elements, the same cone, the same partition, and the index changed by one.

## The Comparison with the Parent and with the Sibling

| clause | general plain algebra | general plain sesqualgebra |
|---|---|---|
| square | $\tilde X^{2}$, bilinear, central | $\tilde X\star\tilde X=\tilde X\tilde X^{*}$, Hermitian |
| square-zero set | the pure isotropic cone | $\{0\}$ alone |
| nilpotent set | the pure isotropic cone, index two | the pure isotropic cone, index three |
| index | two, always | three, always |
| nilpotent implies zero divisor | yes | yes, and every nilpotent is in the pure family |
| non-pure zero divisors | not nilpotent | not nilpotent |

The parent's **set** is kept and the parent's **index** is not: this is the whole content of the article, and it is the sharpest illustration in the corpus of the sentence of *Definitions for the Study of the 12 Algebraic Structures* that the index of nilpotency is a property of the product and not of the element.

## Summary

The powers of the general plain sesqualgebra are $\tilde X^{\star k}=\tilde X(\tilde X^{*})^{k-1}$, and the block has **no nonzero square-zero element**: the Hermitian square $\tilde X\star\tilde X=\tilde X\tilde X^{*}$ has scalar part $\sum_\mu\lvert X_\mu\rvert^{2}$, which vanishes only at the origin, so no nilpotent has index two. The origin is the **trivial** nilpotent, and the nonzero nilpotents are exactly the parent's **pure zero divisors**: with $\tilde\Upsilon$ a nilpotent, $\Upsilon_0=0$ and $C(\tilde\Upsilon)=(\boldsymbol\Upsilon,\boldsymbol\Upsilon)=0$, so the nilpotent set is the pure isotropic cone $\{\Upsilon_0=0,\ (\boldsymbol\Upsilon,\boldsymbol\Upsilon)=0\}$, of complex dimension two. The index is **exactly three**: $\tilde\Upsilon^{\star2}=\tilde\Upsilon\tilde\Upsilon^{*}\neq0$ and $\tilde\Upsilon^{\star3}=0$, proved directly for the pure elements and proved in the $2\times2$ matrix model, where the nilpotents are the rank-one traceless matrices and the condition is $\operatorname{Tr}=0$, that is $\Upsilon_0=0$. The non-pure zero divisors of the parent are zero divisors of the block and not nilpotents of it; the nilpotent set, the zero-divisor partition and the criterion $\Upsilon_0=0$ are inherited, and the index is changed from two to three.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ | the product of the block |
| $\tilde\Upsilon=\Upsilon_0e_0+\boldsymbol\Upsilon$ | a nilpotent of the block |
| $\tilde X^{\star k}=\tilde X(\tilde X^{*})^{k-1}$ | the left-nested power |
| $\tilde X\star\tilde X=\tilde X\tilde X^{*}$ | the Hermitian square |
| $\mathrm{Sc}(\tilde X\star\tilde X)=\sum_\mu\lvert X_\mu\rvert^{2}$ | the scalar part, definite: no nonzero square-zero element |
| $C(\tilde X)=\sum_\mu X_\mu^{2}=X_0^{2}+(\mathbf X,\mathbf X)$ | the central square |
| $\Upsilon_0=0,\ (\boldsymbol\Upsilon,\boldsymbol\Upsilon)=0$ | the criterion of the nilpotent, the pure isotropic cone |
| $\mathcal{N}_\star$ | the nilpotent set, the nonzero pure isotropic cone, complex dimension two |
| index three | $\tilde\Upsilon^{\star2}\neq0$, $\tilde\Upsilon^{\star3}=0$ |
| $\mathsf{M}_2(\tilde X^{\star k})=\mathsf{M}_2(\tilde X)\mathsf{M}_2(\tilde X)^{\dagger(k-1)}$ | the powers in the matrix model, rank-one traceless for the nilpotents |

## Further Reading

- *Introduction to the General Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-general-plain-sesqualgebra-of-biquaternions.md`), for the product, its class and the involution in the second slot.
- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the relative definition of the nilpotent and of the index of nilpotency.
- *Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/zero-divisors-in-the-12-algebraic-structures-over-the-biquaternion-c-space.md`), for the square-zero set of the block, the origin alone.
- *Nilpotents of the General Plain Algebra* (`articles_maths/nilpotents-of-the-general-plain-algebra.md`), for the parent's nilpotents, the pure isotropic cone of index two.
- *Zero Divisors of the General Plain Sesqualgebra* (`articles_maths/zero-divisors-of-the-general-plain-sesqualgebra.md`), for the zero-divisor set and the pure and non-pure families that the nilpotents refine.
- *The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-general-plain-sesqualgebra-in-the-2x2-matrix-element-representation.md`), for the model in which the nilpotents are the rank-one traceless matrices.
- *Idempotents of the General Plain Sesqualgebra* (`articles_maths/idempotents-of-the-general-plain-sesqualgebra.md`), for the companion class, the Hermitian idempotents.
