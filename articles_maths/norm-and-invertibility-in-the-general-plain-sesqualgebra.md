# __Norm and Invertibility in the General Plain Sesqualgebra__

## Introduction

The general plain sesqualgebra is the operation $\tilde Q_1\star\tilde Q_2=\tilde Q_1\tilde Q_2^{*}$ on the biquaternion space, the general plain sesquilinear product read as a multiplication, the operation of *Introduction to the General Plain Sesqualgebra*. This article studies the algebraic norm that the block carries and the invertibility that it does not.

A norm is relative to a product, and the algebraic norm of a product is the diagonal of its scalar-part form, the definition of *The Four Forms and the Four Algebraic Norms*. For the block the form is

$$
\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}\bigl(\tilde Q_1\star\tilde Q_2\bigr)=\mathrm{Sc}\bigl(\tilde Q_1\tilde Q_2^{*}\bigr),
$$

and its diagonal is

$$
\langle\tilde Q\rangle_{*}=\langle\tilde Q,\tilde Q\rangle_{*}=\mathrm{Sc}\bigl(\tilde Q\star\tilde Q\bigr)=\sum_{\mu\in\{t,x,y,z\}}\lvert Q_\mu\rvert^{2},
$$

the general plain sesquilinear algebraic norm, **real and positive definite** of signature $(8,0)$, one of the four algebraic norms of the space and not one of the other three.

The invertibility is where the article records an **absence**. The block has a **right unit** $e_t$ and no left unit, so it has no two-sided unit and no group of units in the ordinary sense; the one-sided inverse equations are stated, and their solvability is decided by a different quadratic form, which is **not** the algebraic norm of the block and is not studied here. Its algebraic norm is definite and does not decide invertibility: $\langle\tilde Q\rangle_{*}=0$ exactly at $\tilde Q=0$.

$$
\langle\tilde Q\rangle_{*}=\langle\tilde Q,\tilde Q\rangle_{*}=\mathrm{Sc}\bigl(\tilde Q\star\tilde Q\bigr)=\sum_{\mu\in\{t,x,y,z\}}\lvert Q_\mu\rvert^{2},
$$

with the form $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\sum_\mu Q_{1\mu}\overline{Q_{2\mu}}$.

**The results.** The block $\tilde Q_1\star\tilde Q_2=\tilde Q_1\tilde Q_2^{*}$ has the right unit $e_t$ and no left unit, hence no two-sided unit and no group of units, and its one-sided inverse equations are decided by a form that is not the algebraic norm. Its algebraic norm is the diagonal of the scalar-part form, $\langle\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_2\star\tilde Q_2)=\sum_{\mu\in\{t,x,y,z\}}\lvert Q_{2\mu}\rvert^{2}$, real and positive definite of signature $(8,0)$ and Gram matrix the identity, one of the four algebraic norms of the space. It is **not** multiplicative but submultiplicative, $\langle\tilde Q_1\star\tilde Q_2\rangle_{*}=\lvert \langle\tilde Q_1,\tilde Q_2\rangle_{*}\rvert^{2}$, so $\langle\tilde Q_1\rangle_{*}\langle\tilde Q_2\rangle_{*}-\langle\tilde Q_1\star\tilde Q_2\rangle_{*}\geq0$, and the absence of a criterion is the definiteness, $\langle\tilde Q_2\rangle_{*}=0$ exactly at $\tilde Q_2=0$.

## The Relative Notions

The word *unit*, the word *inverse* and the word *group of units* name a product, so the definitions are stated once for a general product and read on the block; they are *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*The Unit and the Inverse*.

**Definition (recalled).** Let $\star$ be a product on $\mathbb{B}$. An element $e$ is a **left unit of $\star$** when $e\star\tilde Q=\tilde Q$ for every $\tilde Q$, a **right unit** when $\tilde Q\star e=\tilde Q$ for every $\tilde Q$, and a **two-sided unit** when it is both. When a two-sided unit $e$ exists, an element $\tilde Q$ is **invertible of $\star$** when there is a $\tilde Q_1$ with $\tilde Q\star\tilde Q_1=\tilde Q_1\star\tilde Q=e$, the element $\tilde Q_1$ being the **inverse of $\tilde Q$**, and the invertible elements form the **group of units of $\star$**. When no two-sided unit exists, the two-sided inverse is not defined.

Throughout this article the product is the block $\tilde Q_1\star\tilde Q_2=\tilde Q_1\tilde Q_2^{*}$.

## The Right Unit and the Absence of the Left One

**The block has the right unit $e_t$, since $\tilde Q\star e_t=\tilde Q$, and no left unit, since $e_t\star\tilde Q=\tilde Q^{*}$ is the involution; consequently it has no two-sided unit and no group of units.**

**Theorem (the block has a right unit and no left unit).** For every $\tilde Q$,

$$
\boxed{\;\tilde Q\star e_t=\tilde Q,\qquad e_t\star\tilde Q=\tilde Q^{*}\;}.
$$

Consequently $e_t$ is a **right unit** of $\star$, it is **not** a left unit, and the block has **no two-sided unit**.

*Proof.* The first display is $\tilde Q\star e_t=\tilde Q e_t^{*}=\tilde Q e_t=\tilde Q$, and the second is $e_t\star\tilde Q=e_t\tilde Q^{*}=\tilde Q^{*}$. The left action of $e_t$ is the involution ${}^{*}$, which is not the identity because $\tilde Q^{*}\neq\tilde Q$ for an element with a nonzero vector part, for instance $\tilde Q=\vec e_x$, whose image is $\vec e_x^{*}=-\vec e_x$. A left unit $e$ would satisfy $e\star\tilde Q=\tilde Q$ for all $\tilde Q$, hence $e\tilde Q^{*}=\tilde Q$; at $\tilde Q=e_t$ this gives $e=e_t$, and then at $\tilde Q=\vec e_x$ it gives $e_t\star \vec e_x=-\vec e_x\neq \vec e_x$, a contradiction. So there is no left unit and no two-sided unit.

**Remark (the reason is the derived-operation shape).** The second display is the identity that fixes the whole block: the row of $e_t$ is the involution, because the product is the derived operation $\tilde Q_1\star\tilde Q_2=\tilde Q_1\tilde Q_2^{*}$ and the involution sits in the second slot. The right unit is the plain unit, unaffected, and the left action is twisted by the involution; the block is therefore **right-unital and not left-unital**, the mirror of the general quaternionic algebra, which is left-unital and not right-unital (*The Four General Products and Their Relations*).

**Corollary (no inverse, no group of units).** Since the block has no two-sided unit, no element has a two-sided inverse and the block has no group of units. The two-sided inverse of the block is not defined.

*Proof.* The definition of the two-sided inverse presupposes a two-sided unit, which the theorem excludes.

## The One-Sided Inverse Equations

**The block carries no two-sided invertibility; its one-sided inverse equations are solved on a set decided by a quadratic form that is not the algebraic norm of the block, so the algebraic norm does not decide the one-sided question.**

The one-sided equations are those of *Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*The One-Sided Inverse Equations*, and in the block they read

$$
\tilde Q\star\tilde Q_1=e_t\qquad\text{(the right-inverse equation)},\qquad \tilde Q_1\star\tilde Q=e_t\qquad\text{(the left-inverse equation)},
$$

with $e_t$ the right unit of the block on the right-hand side. The equations have a solution for a set of elements that is decided by a quadratic form; that form is **not** the algebraic norm of the block, it is not one of the four algebraic norms of this space, and it is not studied here. What the article records is that the block carries **no two-sided invertibility** and that its own algebraic norm does not decide the one-sided question, read in §*The Absence of a Criterion from the Algebraic Norm*.

## The Algebraic Norm of the Block

**The block carries one algebraic norm, the diagonal of its scalar-part form, $\langle\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde Q\star\tilde Q)=\sum_{\mu\in\{t,x,y,z\}}\lvert Q_\mu\rvert^{2}$, real and positive definite of signature $(8,0)$ with Gram matrix the identity, and the block-square $\tilde Q\star\tilde Q=\tilde Q\tilde Q^{*}$ is Hermitian with that scalar part and is not the plain square.**

**Definition.** The **algebraic norm of the block** is the diagonal of the scalar-part form of the product,

$$
\langle\tilde Q\rangle_{*}=\mathrm{Sc}\bigl(\tilde Q\star\tilde Q\bigr)=\sum_{\mu\in\{t,x,y,z\}}\lvert Q_\mu\rvert^{2}\in\mathbb{R}_{\geq0},
$$

equivalently $\langle\tilde Q\rangle_{*}=\langle\tilde Q,\tilde Q\rangle_{*}$ for the form

$$
\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}\bigl(\tilde Q_1\star\tilde Q_2\bigr)=\mathrm{Sc}\bigl(\tilde Q_1\tilde Q_2^{*}\bigr)=\sum_{\mu\in\{t,x,y,z\}}Q_{1\mu}\overline{Q_{2\mu}},
$$

the general plain sesquilinear form of *The Four Forms and the Four Algebraic Norms*. The equation names the product: the algebraic norm is relative to the product, and the other three rows carry different quadratic maps on the same space.

**Theorem (the square and the algebraic norm).** For every $\tilde Q$ the square $\tilde Q\star\tilde Q=\tilde Q\tilde Q^{*}$ is Hermitian and its scalar part is the algebraic norm,

$$
\mathrm{Sc}\bigl(\tilde Q\star\tilde Q\bigr)=\langle\tilde Q\rangle_{*}=\sum_{\mu\in\{t,x,y,z\}}\lvert Q_\mu\rvert^{2}\geq0,
$$

which vanishes only at $\tilde Q=0$. The block-square is **not** the plain square, and its vector part need not vanish.

*Proof.* $(\tilde Q\tilde Q^{*})^{*}=\tilde Q\tilde Q^{*}$ gives the Hermitianness, and $\mathrm{Sc}(\tilde Q\tilde Q^{*})=\sum_\mu Q_\mu\overline{Q_\mu}=\sum_\mu\lvert Q_\mu\rvert^{2}$. At the zero divisor $\tilde Q=\vec e_x+i\vec e_y$ the plain square is $\tilde Q^{2}=0$ while the block-square is $\tilde Q\star\tilde Q=2e_t+2i\vec e_z\neq0$, computed from the table of *Introduction to the General Plain Sesqualgebra*.

**Basic properties.** Each is a direct reading of the definition.

- $\langle\tilde Q\rangle_{*}$ is a **real** number, and **non-negative**, vanishing exactly at $\tilde Q=0$: the quadratic form is **positive definite** of signature $(8,0)$ on the realification $\mathbb{B}\cong\mathbb{R}^{8}$.
- $\langle\cdot,\cdot\rangle_{*}$ is **invariant under the three conjugations**, because each preserves the moduli $\lvert Q_\mu\rvert$.
- $\langle\cdot,\cdot\rangle_{*}$ is **homogeneous of degree two over the reals**, $\langle\lambda\tilde Q\rangle_{*}=\lvert\lambda\rvert^{2}\langle\tilde Q\rangle_{*}$ for $\lambda\in\mathbb{C}$.
- Its polarisation is the sesquilinear form $\langle\tilde Q_1,\tilde Q_2\rangle_{*}$, and $\langle\tilde Q_2,\tilde Q_1\rangle_{*}=\overline{\langle\tilde Q_1,\tilde Q_2\rangle_{*}}$: the form is Hermitian.

**Proposition (the Gram matrix).** On the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ the form has Gram matrix the identity, $\langle e_\mu,e_\nu\rangle_{*}=\delta_{\mu\nu}$, so $\langle e_\mu\rangle_{*}=1$.

*Proof.* $\langle e_\mu,e_\nu\rangle_{*}=\sum_\sigma(e_\mu)_\sigma\overline{(e_\nu)_\sigma}=\delta_{\mu\nu}$.

## The Failure of Multiplicativity

**The algebraic norm of the block is not multiplicative but submultiplicative: $\langle\tilde Q_1\star\tilde Q_2\rangle_{*}=\lvert \langle\tilde Q_1,\tilde Q_2\rangle_{*}\rvert^{2}$, so $\langle\tilde Q_1\star\tilde Q_2\rangle_{*}=\langle\tilde Q_1\rangle_{*}\langle\tilde Q_2\rangle_{*}$ exactly on linearly dependent pairs, and the defect $\langle\tilde Q_1\rangle_{*}\langle\tilde Q_2\rangle_{*}-\lvert \langle\tilde Q_1,\tilde Q_2\rangle_{*}\rvert^{2}\geq0$.**

**Theorem (the algebraic norm of a product).** For all $\tilde Q_1,\tilde Q_2$,

$$
\boxed{\;\langle\tilde Q_1\star\tilde Q_2\rangle_{*}=\lvert \langle\tilde Q_1,\tilde Q_2\rangle_{*}\rvert^{2}\;},
$$

so that $\langle\tilde Q_1\star\tilde Q_2\rangle_{*}=\langle\tilde Q_1\rangle_{*}\langle\tilde Q_2\rangle_{*}$ exactly when $\tilde Q_1$ and $\tilde Q_2$ are linearly dependent over $\mathbb{C}$.

*Proof.* The form is computed on the block-square, $\mathrm{Sc}(\tilde Q_1\star\tilde Q_2)=\langle\tilde Q_1,\tilde Q_2\rangle_{*}$; the square $\tilde Q_1\star\tilde Q_2$ is too, so polarising the diagonal $\langle\cdot,\cdot\rangle_{*}$ gives $\langle\tilde Q_1\star\tilde Q_2\rangle_{*}=\langle\tilde Q_1\tilde Q_2^{*}\rangle_{*}$ with the explicit value $\lvert \langle\tilde Q_1,\tilde Q_2\rangle_{*}\rvert^{2}$. Indeed $\tilde Q_1\star\tilde Q_2$ is a single element and $\langle\cdot,\cdot\rangle_{*}$ of an element of the form $\lambda\tilde Q_1$ is $\lvert\lambda\rvert^{2}\langle\tilde Q_1\rangle_{*}$; the identity $\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})=\langle\tilde Q_1,\tilde Q_2\rangle_{*}$ closes the computation. For the equality case, the form $t\mapsto \langle\tilde Q_1-t\tilde Q_2\rangle_{*}\geq0$ has discriminant $\langle\tilde Q_1\rangle_{*}\langle\tilde Q_2\rangle_{*}-\lvert \langle\tilde Q_1,\tilde Q_2\rangle_{*}\rvert^{2}$, non-negative, vanishing exactly at proportionality.

**Corollary (the defect is the discriminant).** For all $\tilde Q_1,\tilde Q_2$,

$$
\langle\tilde Q_1\rangle_{*}\langle\tilde Q_2\rangle_{*}-\langle\tilde Q_1\star\tilde Q_2\rangle_{*}=\langle\tilde Q_1\rangle_{*}\langle\tilde Q_2\rangle_{*}-\lvert \langle\tilde Q_1,\tilde Q_2\rangle_{*}\rvert^{2}\geq0,
$$

with equality exactly on linearly dependent pairs. The algebraic norm is **submultiplicative**.

**Remark (multiplicativity on the centre).** On the central line $\mathbb{C}e_t$ the block is the field rule and the algebraic norm is the squared modulus, $\langle \lambda e_t\rangle_{*}=\lvert\lambda\rvert^{2}$, multiplicative there. Multiplicativity holds on the centre and fails off it, and the failure is measured by the corollary.

## The Polarisation of the Algebraic Norm

**The polar form of the algebraic norm is twice the real part of the sesquilinear form, $\langle\tilde Q_1+\tilde Q_2\rangle_{*}-\langle\tilde Q_1\rangle_{*}-\langle\tilde Q_2\rangle_{*}=2\Re \langle\tilde Q_1,\tilde Q_2\rangle_{*}$, and the full Hermitian form is recovered by $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\tfrac{1}{4}\sum_{k=0}^{3}i^{k}\langle\tilde Q_1+i^{k}\tilde Q_2\rangle_{*}$.**

**Theorem (the polarisation).** The polar form of the algebraic norm is twice the real part of the sesquilinear form,

$$
\langle\tilde Q_1+\tilde Q_2\rangle_{*}-\langle\tilde Q_1\rangle_{*}-\langle\tilde Q_2\rangle_{*}=2\Re \langle\tilde Q_1,\tilde Q_2\rangle_{*},
$$

and the full Hermitian form is recovered by

$$
\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\tfrac{1}{4}\sum_{k=0}^{3}i^{k}\,\langle\tilde Q_1+i^{k}\tilde Q_2\rangle_{*}.
$$

*Proof.* The first display expands $\langle\tilde Q_1+\tilde Q_2\rangle_{*}=\langle\tilde Q_1\rangle_{*}+\langle\tilde Q_2\rangle_{*}+\langle\tilde Q_1,\tilde Q_2\rangle_{*}+\overline{\langle\tilde Q_1,\tilde Q_2\rangle_{*}}$. The second is the four-term Hermitian polarisation, the coefficients being the fourth roots of unity.

**Remark (the polarisation is the Hermitian one).** The four coefficients $1,i,-1,-i$ are the fourth roots of unity, not the pair $\pm1$ of the symmetric polarisation; the first display extracts the real part, because the diagonal of a Hermitian form is real; the imaginary part is carried by the four-term display.

## The Absence of a Criterion from the Algebraic Norm

**The block has no two-sided invertible element, and its algebraic norm has no nonzero zero, $\langle\tilde Q\rangle_{*}=0\Leftrightarrow\tilde Q=0$; the definiteness is the absence of a criterion, the one-sided equations' solvability being decided by a different form.**

**Theorem (the algebraic norm does not decide invertibility).** The block has no two-sided invertible element, so no criterion can name one; and its algebraic norm has no nonzero zero:

$$
\boxed{\;\langle\tilde Q\rangle_{*}=0\quad\Longleftrightarrow\quad\tilde Q=0\;}.
$$

*Proof.* The first clause is the absence of a two-sided inverse. The equivalence is the positive definiteness: $\langle\tilde Q\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$ is a sum of non-negative reals, vanishing exactly at the origin.

**Remark (what replaces the criterion).** For the block the algebraic norm is definite, so it separates nothing: there is **no nonzero element of zero algebraic norm**, that is **no nonzero isotropic vector**. The one-sided inverse equations of §*The One-Sided Inverse Equations* have a solution for a proper set of elements, and its solvability is decided by a different quadratic form, not the algebraic norm of the block and not studied here. The block therefore carries an algebraic norm that is definite and an invertibility that the algebraic norm does not see, the exact mirror of the general plain algebra, whose algebraic norm $\langle\cdot\rangle$ is indefinite and does not decide invertibility either (*Norm and Invertibility in the Biquaternion Algebra*).

**Corollary (no substitute group).** The block has no group of units and no subgroup of its own elements to play that role; what it does have is the set on which the one-sided equations are solvable, defined by a form not read here. The group that does exist is the group of the linear maps of $\mathbb{B}$ that preserve the algebraic norm $\langle\cdot\rangle_{*}$, read in *The Multiplication Operators of the General Plain Sesqualgebra* where the block has such an article.

## The Comparison with the General Plain Algebra

**The block and the parent carry different algebraic norms, $\langle\cdot\rangle_{*}$ real and definite against $\langle\cdot\rangle$ complex and indefinite, and neither algebraic norm decides invertibility; the block keeps a right unit and loses the left unit, the two-sided unit, the two-sided invertible elements and the group of units.**

| clause | general plain algebra | general plain sesqualgebra |
|---|---|---|
| algebraic norm | $\langle\tilde Q\rangle=\mathrm{Sc}(\tilde Q\tilde Q)=Q_t^2-(\vec Q,\vec Q)$, complex, indefinite | $\langle\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde Q\star\tilde Q)=\sum_\mu\lvert Q_\mu\rvert^{2}$, real, definite |
| multiplicativity of the algebraic norm | $\langle\cdot\rangle$ not multiplicative | $\langle\cdot\rangle_{*}$ submultiplicative, $\langle\tilde Q_1\star\tilde Q_2\rangle_{*}=\lvert \langle\tilde Q_1,\tilde Q_2\rangle_{*}\rvert^{2}$ |
| isotropic vectors | the complex cone of $B$ | none but the origin |
| unit | $e_t$, two-sided | $e_t$ right unit only, no left unit |
| two-sided invertible elements | defined | none |
| group of units | defined | none |

The two products carry **different** algebraic norms, $\langle\cdot\rangle$ and $\langle\cdot\rangle_{*}$, and neither algebraic norm decides invertibility: the parent has invertible elements that its algebraic norm $\langle\cdot\rangle$ does not see, and the block has no two-sided invertible element at all. The block keeps a right unit, loses the left one and the group, and the algebraic norm it carries is the definite form whose diagonal is the scalar part of the block-square.

## Summary

The general plain sesqualgebra $\tilde Q_1\star\tilde Q_2=\tilde Q_1\tilde Q_2^{*}$ has a **right unit** $e_t$, because $\tilde Q_2\star e_t=\tilde Q_2$, and **no left unit**, because the left action of $e_t$ is the involution, $e_t\star\tilde Q_2=\tilde Q_2^{*}$; consequently it has **no two-sided unit** and **no group of units** in the ordinary sense. The one-sided inverse equations exist, and their solvability is decided by a quadratic form that is **not** the algebraic norm of the block and is not studied here. The block carries one algebraic norm, the diagonal of its scalar-part form,

$$
\langle\tilde Q\rangle_{*}=\mathrm{Sc}\bigl(\tilde Q\star\tilde Q\bigr)=\sum_{\mu\in\{t,x,y,z\}}\lvert Q_\mu\rvert^{2},
$$

real, positive definite of signature $(8,0)$, the general plain sesquilinear algebraic norm, one of the four algebraic norms of the space and not one of the other three. It is **not multiplicative**: $\langle\tilde Q_1\star\tilde Q_2\rangle_{*}=\lvert \langle\tilde Q_1,\tilde Q_2\rangle_{*}\rvert^{2}$, submultiplicative, the defect $\langle\tilde Q_1\rangle_{*}\langle\tilde Q_2\rangle_{*}-\lvert \langle\tilde Q_1,\tilde Q_2\rangle_{*}\rvert^{2}\geq0$ vanishing exactly on linearly dependent pairs; it polarises to the Hermitian form, $\Re H$ at the symmetric step and $\langle\cdot,\cdot\rangle_{*}$ at the four-term display. The **absence of a criterion** is the definiteness, $\langle\tilde Q_2\rangle_{*}=0\Leftrightarrow\tilde Q_2=0$: the block has no nonzero isotropic vector and no two-sided invertible element, and its algebraic norm does not decide the invertibility that its one-sided equations leave open.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Q_1\star\tilde Q_2=\tilde Q_1\tilde Q_2^{*}$ | the product of the block |
| $e_t$ | the right unit; $e_t\star\tilde Q=\tilde Q^{*}$ is the involution |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\star\tilde Q_2)=\sum_\mu Q_{1\mu}\overline{Q_{2\mu}}$ | the general plain sesquilinear form, the scalar-part form of the product |
| $\langle\tilde Q\rangle_{*}=\langle\tilde Q,\tilde Q\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$ | the algebraic norm of the block, one of the four algebraic norms of the space |
| $\tilde Q\star\tilde Q=\tilde Q\tilde Q^{*}$ | the block-square, Hermitian, scalar part $\langle\tilde Q\rangle_{*}$ |
| $\langle\tilde Q_1\star\tilde Q_2\rangle_{*}=\lvert \langle\tilde Q_1,\tilde Q_2\rangle_{*}\rvert^{2}$ | the algebraic norm of a product |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\tfrac14\sum_k i^{k}\langle\tilde Q_1+i^{k}\tilde Q_2\rangle_{*}$ | the Hermitian polarisation of the algebraic norm |
| $\langle\tilde Q\rangle_{*}=0\Leftrightarrow\tilde Q=0$ | the definiteness, the substitute for the criterion |
| no left unit, no two-sided unit, no group of units | the absence carried by the block |

## Further Reading

- [The Four Forms and the Four Algebraic Norms](the-four-forms-and-the-four-algebraic-norms.html), for the definition of the algebraic norm as the form at the two equal arguments and the four algebraic norms of the space.
- [The Four Forms and the Four Algebraic Norms](the-four-forms-and-the-four-algebraic-norms.html), for the Hermitian form $\langle\cdot,\cdot\rangle_{*}$ and the table of the four forms.
- [Introduction to the General Plain Sesqualgebra](introduction-to-the-general-plain-sesqualgebra.html), for the product, the right unit and the involution in the second slot.
- [Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternion-c-space.html), §*The Unit and the Inverse*, for the relative definitions of the unit, the inverse and the group of units.
- [The Four General Products and Their Relations](the-four-general-products-and-their-relations.html), for the one-sided unit table of the four products.
- [Norm and Invertibility in the Biquaternion Algebra](norm-and-invertibility-in-the-biquaternion-algebra.html), for the algebraic norm $\langle\cdot\rangle$ of the plain product, which is not the form $\langle\cdot,\cdot\rangle_{*}$ of this article.
- [Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](zero-divisors-in-the-algebraic-structures-over-the-biquaternion-c-space.html), for the one-sided inverse equations and the common zero-divisor set.
- [The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$](the-general-plain-sesqualgebra-in-the-2x2-matrix-element-representation.html), for the matrix model $\mathsf{M}_2(\tilde Q_1\star\tilde Q_2)=\mathsf{M}_2(\tilde Q_1)\mathsf{M}_2(\tilde Q_2)^{\dagger}$ in which the block-square is positive semidefinite.
- [The Squares and the Positive Cone of the Biquaternion Sesqualgebra](the-squares-and-the-positive-cone-of-the-biquaternion-sesqualgebra.html), for the image of the block-square and the cone it generates in the Hermitian subspace.
