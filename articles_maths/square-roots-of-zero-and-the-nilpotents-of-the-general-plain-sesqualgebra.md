# __Square Roots of Zero and the Nilpotents of the General Plain Sesqualgebra__

## Introduction

The general plain sesqualgebra is the operation $\tilde Q_1\star\tilde Q_2=\tilde Q_1\tilde Q_2^{*}$ on the biquaternion space $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ (*Introduction to the General Plain Sesqualgebra*, *The Four General Products and Their Relations over the Biquaternion Algebra*). This article treats two subjects, and in this order. The first is the square roots of the central value $0$, the elements $\tilde\Xi$ with

$$
\tilde\Xi\star\tilde\Xi=0 ,
$$

the square-zero elements, and the second is the **nilpotents** of the block, the nonzero elements $\tilde\Upsilon$ with a vanishing power,

$$
\tilde\Upsilon^{\star k}=0\quad\text{for some }k\geq1,
$$

the power being the left-nested reading of *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, $\tilde Q_1^{\star k}=\bigl(\cdots(\tilde Q_1\star\tilde Q_1)\star\tilde Q_1\cdots\bigr)$, which for the block is $\tilde Q_1^{\star k}=\tilde Q_1(\tilde Q_1^{*})^{k-1}$. The two subjects are one subject: a root of $0$ is a square-zero element, that is a nilpotent of **index two**, and the nilpotents of the block are exactly the roots of $0$ that the emptiness of the root set pushes to the **next index**.

The answer is not the parent's. The block has **no nonzero square-zero element**, so the root set of $0$ is empty and no nilpotent has index two; but it **has** nilpotents, of index three, and they are exactly the parent's **pure zero divisors**, the elements with vanishing scalar coordinate and isotropic vector part. The block therefore keeps the parent's nilpotent **set** — the pure cone $\{\Upsilon_t=0,\ (\vec\Upsilon,\vec\Upsilon)=0\}$ — and changes its **index**, from two to three, because its square is the Hermitian square $\tilde Q_1\tilde Q_1^{*}$ instead of the plain square $\tilde Q_1^{2}$. The non-pure zero divisors of the parent are zero divisors of the block and are **not** nilpotents of it, so the implication of the parent, "the pure family is the nilpotent family", holds here in a transmuted form: the pure family is the nilpotent family and the index is three.

**The results.** The left-nested powers of the block are conjugate-linear iterations, $\tilde Q_1^{\star k}=\tilde Q_1(\tilde Q_1^{*})^{k-1}$, so the index is a property of the pair $(\mathsf{M}_2(\tilde Q_1),\mathsf{M}_2(\tilde Q_1)^{\dagger})$ and can exceed two. The scalar part of the square is $\sum_\mu\lvert Q_{1\mu}\rvert^{2}$, which vanishes only at the origin, so the root set of $0$ is empty and there is no nonzero square-zero element; the nonzero nilpotents are exactly the parent's pure zero divisors, the elements $\Upsilon_t=0$ with $C(\tilde\Upsilon)=(\vec\Upsilon,\vec\Upsilon)=0$, of index exactly three, $\tilde\Upsilon^{\star2}\neq0$ and $\tilde\Upsilon^{\star3}=0$. The nilpotent set is the nonzero pure isotropic cone, of complex dimension two, and it is the parent's set with the index changed from two to three; the non-pure zero divisors are not nilpotent.

The equations name a product, so the powers, the square-zero elements and the nilpotents are relative to it. Throughout this article the product is the block $\tilde Q_1\star\tilde Q_2=\tilde Q_1\tilde Q_2^{*}$; the general definition of the nilpotent is §*The Nilpotent* of *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*. The origin is a nilpotent, the **trivial** one, and the article is concerned with the nonzero ones.

## The Roots of Zero

**The block has no root of $0$: the equation $\tilde\Xi\star\tilde\Xi=0$ has the single solution $\tilde\Xi=0$, so the root set of $0$ is empty and there is no nonzero square-zero element; the nilpotents of the block are at the next index, and they are the pure zero divisors.**

A **root of $0$** is a nonzero element $\tilde\Xi\in\mathbb{B}$ with $\tilde\Xi\star\tilde\Xi=0$, that is a nonzero square-zero element; the equation is the block's, the Hermitian square $\tilde\Xi\star\tilde\Xi=\tilde\Xi\tilde\Xi^{*}$.

**Theorem (no root of $0$; no nonzero square-zero element).** The equation $\tilde\Xi\star\tilde\Xi=0$ has the single solution $\tilde\Xi=0$, so the block has no nonzero square-zero element, no nilpotent of index two, and the root set of $0$ is empty.

*Proof.* The scalar part of the square is $\mathrm{Sc}(\tilde\Xi\star\tilde\Xi)=\sum_\mu\lvert\Xi_\mu\rvert^{2}$ by the reduction of *Square Roots of One and the Idempotents of the General Plain Sesqualgebra*, §*The Reduction*, and it vanishes only when every coordinate vanishes. A root is required to be nonzero, so the root set is empty; the same computation is the statement that the square-zero set is $\{0\}$. In the matrix model the square is $AA^{\dagger}$, positive semidefinite, whose vanishing forces $A=0$; the same statement is *Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, where the square-zero set of the general plain sesquilinear product is the origin alone.

**Remark (square-zero and nilpotent are not the same here).** The block has no square-zero element, so it has no nilpotent of **index two**; its nilpotents have index **three**, and they are exactly the pure zero divisors, the elements with $\Upsilon_t=0$ and $(\vec\Upsilon,\vec\Upsilon)=0$. The empty root set of $0$ is therefore not the empty nilpotent set: the root of $0$ is the square-zero element, and the block has none, while the block has plenty of nilpotents at the next index. The distinction between *square-zero* and *nilpotent* is thus live in the block and not a coincidence of definitions.

**Remark (the pure zero divisors are not square-zero).** The parent's pure zero divisors, $\Xi_t=0$ with $(\vec\Xi,\vec\Xi)=0$, are its nonzero nilpotents of index two; the block's square does not vanish on them, $\tilde\Xi\star\tilde\Xi=\langle\tilde\Xi\rangle_{*}e_t+\mathrm{Vect}(\tilde\Xi\tilde\Xi^{*})\neq0$, as *Zero Divisors of the General Plain Sesqualgebra* records, and the block's nilpotency index is raised to three. The root set of $0$ is empty although the zero-divisor set is not, and although the nilpotent set is not: the three classes of the block are distinct and they must not be conflated.

**Remark (the parent, the block and the sibling).** The parent has square-zero elements, the pure isotropic cone; the block has none but the origin, and its square-zero set is the origin alone. This is the one clause on which the block and the parent separate at the level of the square, and it is the reason the block's index is three: a pure isotropic element, square-zero for the parent, has a non-vanishing Hermitian square for the block and vanishes only at the third power. The sibling symmetric plain sesqualgebra also has no **nonzero** square-zero element, and it has index-three nilpotents whose square is the nonzero central element $\bigl(\sum_\mu\lvert\Upsilon_\mu\rvert^{2}\bigr)e_t$ (written $\langle\tilde\Upsilon\rangle_{*}e_t$ in that block, where $\langle\cdot\rangle_{*}$ is the algebraic norm of the block); the block's index-three nilpotents have a **non-central** square $\tilde\Upsilon\tilde\Upsilon^{*}$, and that is the difference between the two siblings.

## The Powers of the Block

The left-nested powers of the block are conjugate-linear iterations, $\tilde Q_1^{\star k}=\tilde Q_1(\tilde Q_1^{*})^{k-1}$, so the index is a property of the pair $(\mathsf{M}_2(\tilde Q_1),\mathsf{M}_2(\tilde Q_1)^{\dagger})$ and not of the plain square, and it can be larger than two.

**Proposition (the powers are conjugate-linear iterations).** For every $\tilde Q_1$ and every $k\geq1$,

$$
\boxed{\;\tilde Q_1^{\star k}=\tilde Q_1(\tilde Q_1^{*})^{k-1}\;},
$$

so $\tilde Q_1^{\star2}=\tilde Q_1\tilde Q_1^{*}$, $\tilde Q_1^{\star3}=\tilde Q_1\tilde Q_1^{*}\tilde Q_1^{*}$, and in the matrix model $\mathsf{M}_2(\tilde Q_1^{\star k})=\mathsf{M}_2(\tilde Q_1)\mathsf{M}_2(\tilde Q_1)^{\dagger(k-1)}$.

*Proof.* By induction on the left-nested reading: $\tilde Q_1^{\star(k+1)}=\tilde Q_1^{\star k}\star\tilde Q_1=\tilde Q_1^{\star k}\tilde Q_1^{*}=\tilde Q_1(\tilde Q_1^{*})^{k-1}\tilde Q_1^{*}=\tilde Q_1(\tilde Q_1^{*})^{k}$. The matrix display is the multiplicativity $\mathsf{M}_2(\tilde Q_1\star\tilde Q_2)=\mathsf{M}_2(\tilde Q_1)\mathsf{M}_2(\tilde Q_2)^{\dagger}$ and $\mathsf{M}_2(\tilde Q_1^{*})=\mathsf{M}_2(\tilde Q_1)^{\dagger}$.

**Remark (why the index can be larger than two).** The square of the block is $\tilde Q_1\tilde Q_1^{*}$, the Hermitian square, and the iterated powers are the products of $\tilde Q_1$ with the successive powers of the conjugate transpose. The index is therefore a property of the pair $(\mathsf{M}_2(\tilde Q_1),\mathsf{M}_2(\tilde Q_1)^{\dagger})$ and not of the plain square, and it can be larger than two even when the plain element is a square-zero element of index two.

## The Criterion of the Nilpotent

**For a nonzero element the following are equivalent: it is a nilpotent of the block, $\tilde\Upsilon^{\star3}=0$, it is pure with vanishing central square ($\Upsilon_t=0$, $C(\tilde\Upsilon)=0$), and it is a pure zero divisor of the plain product; the index is then exactly three, $\tilde\Upsilon^{\star2}\neq0$.**

**Theorem (the nilpotents are the pure zero divisors, of index three).** For $\tilde\Upsilon\neq0$ the following are equivalent:

1. $\tilde\Upsilon$ is a nilpotent of the block;
2. $\tilde\Upsilon^{\star3}=0$;
3. $\tilde\Upsilon$ is pure and of vanishing central square: $\Upsilon_t=0$ and $C(\tilde\Upsilon)=0$;
4. $\tilde\Upsilon$ is a pure zero divisor of the plain product.

When they hold, the index of nilpotency is exactly three: $\tilde\Upsilon^{\star2}\neq0$.

*Proof.* Write $A=\mathsf{M}_2(\tilde\Upsilon)$, so that $\tilde\Upsilon^{\star k}=0$ is $A(A^{\dagger})^{k-1}=0$ and $\det A=C(\tilde\Upsilon)$, $\operatorname{Tr}A=2\Upsilon_t$. First, if $A$ is invertible then $\det\bigl(A(A^{\dagger})^{m}\bigr)=(\det A)\,\overline{(\det A)}^{m}$ has modulus $\lvert\det A\rvert^{m+1}\neq0$, so no nilpotent is regular and $\operatorname{rank}A\leq1$, that is $\det A=0$; with $\tilde\Upsilon\neq0$ this is $\operatorname{rank}A=1$. Write $A=\sigma\,\vec q\vec v^{\dagger}$ with $\sigma>0$ and $\vec q,\vec v$ unit; then $A(A^{\dagger})^{m}=\sigma^{m+1}(\vec q^{\dagger}\vec v)^{m-1}\vec q\vec q^{\dagger}$, whose vanishing for some $m$ is $\vec q^{\dagger}\vec v=0$, and $\operatorname{Tr}A=\sigma\vec v^{\dagger}\vec q=\sigma\overline{\vec q^{\dagger}\vec v}$. Hence $A(A^{\dagger})^{m}=0$ for some $m$ if and only if $\operatorname{Tr}A=0$, and then $m=2$ already gives $A(A^{\dagger})^{2}=0$, that is $\tilde\Upsilon^{\star3}=0$; the case $m=1$ is impossible because $AA^{\dagger}=\sigma^{2}\vec q\vec q^{\dagger}\neq0$. Now $\operatorname{Tr}A=0$ is $\Upsilon_t=0$, and $\operatorname{rank}A=1$ is $C(\tilde\Upsilon)=0$; the equivalence of the first three statements follows, and the fourth is the description of the pure family of the parent. Finally $\tilde\Upsilon^{\star2}=\tilde\Upsilon\tilde\Upsilon^{*}$ has matrix $AA^{\dagger}$, of rank one, so it is nonzero: the index is three and not two.

**Direct proof of the pure case.** When $\Upsilon_t=0$ the element is $\tilde\Upsilon=\sum_{\mu\in\{x,y,z\}}\Upsilon_\mu\vec e_\mu$, its conjugate transpose is $\tilde\Upsilon^{*}=-\overline{\tilde\Upsilon}$, and the plain square of a pure element is $\tilde\Upsilon^{2}=-C(\tilde\Upsilon)e_t$; so if in addition $C(\tilde\Upsilon)=0$ then $\tilde\Upsilon^{2}=0$ and $\overline{\tilde\Upsilon}^{2}=\overline{\tilde\Upsilon^{2}}=0$, whence $\tilde\Upsilon^{\star3}=\tilde\Upsilon(\tilde\Upsilon^{*})^{2}=\tilde\Upsilon\overline{\tilde\Upsilon}^{2}=0$. The witness $\tilde\Upsilon=\vec e_x+i\vec e_y$ has $\Upsilon_t=0$, $C(\tilde\Upsilon)=1+i^{2}=0$ and $\tilde\Upsilon^{\star3}=0$, while $\tilde\Upsilon^{\star2}=2e_t+2i\vec e_z\neq0$.

**Remark (the square of an index-three nilpotent).** The sibling symmetric plain sesqualgebra has index-three nilpotents whose square is the nonzero central element $\langle\tilde\Upsilon\rangle_{*}e_t$, where $\langle\cdot\rangle_{*}$ is its algebraic norm; the block's index-three nilpotents have the **non-central** square $\tilde\Upsilon\tilde\Upsilon^{*}$, whose scalar part is $\langle\tilde\Upsilon\rangle_{*}$, and that is the difference between the two siblings on the same set.

## The Nilpotent Set

**The nilpotent set of the block is the nonzero pure isotropic cone $\{\tilde\Upsilon\neq0:\Upsilon_t=0,\ (\vec\Upsilon,\vec\Upsilon)=0\}$, of complex dimension two; every nilpotent is a two-sided zero divisor, and the non-pure zero divisors are not nilpotent.**

**Corollary (the set).** The nilpotent set of the block is

$$
\boxed{\;\mathcal{N}_\star=\{\tilde\Upsilon\neq0:\ \Upsilon_t=0,\ (\vec\Upsilon,\vec\Upsilon)=0\}\;},
$$

the nonzero elements of the **pure isotropic cone**, of complex dimension two, which is the pure zero-divisor cone of the parent. Every nilpotent is a two-sided zero divisor, and the non-pure zero divisors, the nonzero complex multiples of the nontrivial idempotents with $\Upsilon_t\neq0$, are **not** nilpotent.

*Proof.* The first display is the criterion. The set is the isotropic quadric of the two-complex-dimensional vector part, of complex dimension two, and it is a subset of the zero-divisor set $\mathcal{C}\setminus\{0\}$ of *Zero Divisors of the General Plain Sesqualgebra*. A non-pure zero divisor has $\Upsilon_t\neq0$, so it fails the criterion and is not nilpotent.

**Remark (the two families of the parent, re-read).** The parent partitions its zero divisors into the pure family, which is its nilpotent family of index two, and the non-pure family, which is not nilpotent. The block inherits the partition and moves the nilpotent family from the index two to the index three: the partition is the same, the criterion $\Upsilon_t=0$ is the same, the index is not. The **index of nilpotency is therefore a product-relative notion** even on the same set, and the block is the clean illustration: the same elements, the same cone, the same partition, and the index changed by one. The non-pure zero divisors are the nonzero complex multiples of the nontrivial idempotents, which are the roots of $+1$ of the block read through the halving map of *Square Roots of One and the Idempotents of the General Plain Sesqualgebra*.

## The Comparison with the Parent and with the Sibling

**The block keeps the parent's nilpotent set, the pure isotropic cone, and changes the index from two to three; the parent's square-zero set is that cone and the block's is $\{0\}$ alone, and the block's index-three nilpotents have a non-central square where the symmetric sibling's have a central one.**

| clause | general plain algebra | general plain sesqualgebra |
|---|---|---|
| square | $\tilde Q_1^{2}$, bilinear, central | $\tilde Q_1\star\tilde Q_1=\tilde Q_1\tilde Q_1^{*}$, Hermitian |
| square-zero set | the pure isotropic cone | $\{0\}$ alone |
| nilpotent set | the pure isotropic cone, index two | the pure isotropic cone, index three |
| index | two, always | three, always |
| nilpotent implies zero divisor | yes | yes, and every nilpotent is in the pure family |
| non-pure zero divisors | not nilpotent | not nilpotent |

The parent's **set** is kept and the parent's **index** is not: this is the whole content of the article, and it is the sharpest illustration in the corpus of the sentence of *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* that the index of nilpotency is a property of the product and not of the element.

## Summary

The powers of the general plain sesqualgebra are $\tilde Q_1^{\star k}=\tilde Q_1(\tilde Q_1^{*})^{k-1}$, and the block has **no nonzero square-zero element**: the Hermitian square $\tilde Q_1\star\tilde Q_1=\tilde Q_1\tilde Q_1^{*}$ has scalar part $\sum_\mu\lvert Q_{1\mu}\rvert^{2}$, which vanishes only at the origin, so no nilpotent has index two and the root set of $0$ is empty. The origin is the **trivial** nilpotent, and the nonzero nilpotents are exactly the parent's **pure zero divisors**: with $\tilde\Upsilon$ a nilpotent, $\Upsilon_t=0$ and $C(\tilde\Upsilon)=(\vec\Upsilon,\vec\Upsilon)=0$, so the nilpotent set is the pure isotropic cone $\{\Upsilon_t=0,\ (\vec\Upsilon,\vec\Upsilon)=0\}$, of complex dimension two. The index is **exactly three**: $\tilde\Upsilon^{\star2}=\tilde\Upsilon\tilde\Upsilon^{*}\neq0$ and $\tilde\Upsilon^{\star3}=0$, proved directly for the pure elements and proved in the $2\times2$ matrix model, where the nilpotents are the rank-one traceless matrices and the condition is $\operatorname{Tr}=0$, that is $\Upsilon_t=0$. The non-pure zero divisors of the parent are zero divisors of the block and not nilpotents of it; the nilpotent set, the zero-divisor partition and the criterion $\Upsilon_t=0$ are inherited, and the index is changed from two to three.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Q_1\star\tilde Q_2=\tilde Q_1\tilde Q_2^{*}$ | the product of the block |
| $\tilde\Upsilon=\Upsilon_te_t+\vec\Upsilon$ | a nilpotent of the block |
| $\tilde Q_1^{\star k}=\tilde Q_1(\tilde Q_1^{*})^{k-1}$ | the left-nested power |
| $\tilde Q_1\star\tilde Q_1=\tilde Q_1\tilde Q_1^{*}$ | the Hermitian square |
| $\mathrm{Sc}(\tilde Q_1\star\tilde Q_1)=\sum_\mu\lvert Q_{1\mu}\rvert^{2}$ | the scalar part, definite: no nonzero square-zero element |
| $\mathcal{R}(0)=\varnothing$ | no root of $0$ |
| $C(\tilde Q_1)=\sum_\mu Q_{1\mu}^{2}=Q_{1t}^{2}+(\vec Q_1,\vec Q_1)$ | the central square |
| $\Upsilon_t=0,\ (\vec\Upsilon,\vec\Upsilon)=0$ | the criterion of the nilpotent, the pure isotropic cone |
| $\mathcal{N}_\star$ | the nilpotent set, the nonzero pure isotropic cone, complex dimension two |
| index three | $\tilde\Upsilon^{\star2}\neq0$, $\tilde\Upsilon^{\star3}=0$ |
| $\mathsf{M}_2(\tilde Q_1^{\star k})=\mathsf{M}_2(\tilde Q_1)\mathsf{M}_2(\tilde Q_1)^{\dagger(k-1)}$ | the powers in the matrix model, rank-one traceless for the nilpotents |

## Further Reading

- [Introduction to the General Plain Sesqualgebra](introduction-to-the-general-plain-sesqualgebra.html), for the product, its class and the involution in the second slot.
- [Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternion-c-space.html), for the relative definition of the power, the square-zero element, the nilpotent and the index of nilpotency.
- [Square Roots of One and the Idempotents of the General Plain Sesqualgebra](square-roots-of-one-and-the-idempotents-of-the-general-plain-sesqualgebra.html), for the reduction of the square whose scalar part excludes the roots of $0$, and for the idempotents that the non-pure zero divisors are the multiples of.
- [Norm and Invertibility in the General Plain Sesqualgebra](norm-and-invertibility-in-the-general-plain-sesqualgebra.html), for the square and the definiteness of its scalar part.
- [Zero Divisors of the General Plain Sesqualgebra](zero-divisors-of-the-general-plain-sesqualgebra.html), for the zero-divisor set and the pure and non-pure families that the nilpotents refine.
- [Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](zero-divisors-in-the-algebraic-structures-over-the-biquaternion-c-space.html), for the square-zero set of the block, the origin alone.
- [Square Roots of Zero and the Nilpotents of the Biquaternion Algebra](square-roots-of-zero-and-the-nilpotents-of-the-biquaternion-algebra.html), for the parent's nilpotents, the pure isotropic cone of index two.
- [$M_2(\mathbb{C})$ Representation : The General Plain Sesqualgebra of Biquaternions](the-general-plain-sesqualgebra-in-the-2x2-matrix-element-representation.html), for the model in which the nilpotents are the rank-one traceless matrices.
