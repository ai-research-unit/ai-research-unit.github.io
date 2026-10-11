# __Square Roots of Minus One, Zero and Plus One in the General Plain Sesqualgebra__

## Introduction

The general plain sesqualgebra is the operation $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ on the biquaternion space (*Introduction to the General Plain Sesqualgebra of Biquaternions*). This article determines the square roots of the three central values $-1$, $0$ and $+1$ in the block, that is, the elements $\tilde Q$ satisfying

$$
\tilde Q\star\tilde Q=-e_0,\qquad \tilde Q\star\tilde Q=0,\qquad \tilde Q\star\tilde Q=e_0 .
$$

A root names a product, and the definition is relative; it is stated once for a general product in *Definitions for the Study of the 12 Algebraic Structures*, §*Powers, the Square and the Roots*, and is read here on the block. The block's square is the **Hermitian square** $\tilde Q\star\tilde Q=\tilde Q\tilde Q^{*}$, whose scalar part is the definite quantity $\sum_\mu\lvert Q_\mu\rvert^{2}$ (*Norm and Invertibility in the General Plain Sesqualgebra*). One consequence decides the whole article and it is a **positivity**: the scalar part of the square is never negative, so the value $-1$ is unattainable and the value $0$ is attained only at the origin. The block therefore carries **no root of $-1$** and **no root of $0$**, and it carries the roots of $+1$, which are the element cost of that positivity. The relation to the idempotents is not the parent's bijection with the roots of $-1$ — the block has none — but a bijection with the **Hermitian** roots of $+1$.

**Placement.** The article is the fourth entry of the *Common Theory* section of the block, after the zero divisors and before the square roots of a general element. It uses the product and the class of the introduction, the norm and the scalar part of the square from *Norm and Invertibility in the General Plain Sesqualgebra*, and the zero-divisor set of *Zero Divisors of the General Plain Sesqualgebra*; it feeds the idempotent article of the block, *Idempotents of the General Plain Sesqualgebra*, and the nilpotent article, *Nilpotents of the General Plain Sesqualgebra*.

**Boundaries.** The product, its class and its placement are *Introduction to the General Plain Sesqualgebra of Biquaternions*; the relative definition of the root and of the square root, and the designation of the three central values, are *Definitions for the Study of the 12 Algebraic Structures*. The three sets of the parent are *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*, and the general reduction is *Square Roots of a General Element in the General Plain Algebra*; the general reduction of the block is *Square Roots of a General Element in the General Plain Sesqualgebra*. The idempotents and the nilpotents of the parent are *Idempotents of the General Plain Algebra* and *Nilpotents of the General Plain Algebra*, and the roots read on the idempotents are *Idempotents of the General Plain Sesqualgebra* and *Idempotents of the General Plain Algebra*, §*The Relation to the Idempotents*. Nothing topological and nothing metric appears.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ with $e_1e_2=e_3$ and central scalar imaginary $i$. A general element is $\tilde Q=\sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$; the natural conjugation is $\tilde Q^{\natural}=Q_0-\mathbf Q$, the coefficientwise conjugation is $\overline{\tilde Q}=\overline{Q_0}e_0+\overline{\mathbf Q}$, and the Hermitian conjugation is $\tilde Q^{*}=\overline{\tilde Q^{\natural}}=\overline{Q_0}-\overline{\mathbf Q}$. The product is the block $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$. A **root of $\lambda$** is a nonzero element with $\tilde Q\star\tilde Q=\lambda e_0$; the three central values are $-1$, $+1$ and $0$, the last being the nonzero square-zero elements. Throughout, an element is written in the halves $q_r,q_i$ of the imaginary decomposition of the algebra, $\tilde Q=q_r+iq_i$ with $q_r,q_i$ **real** quaternions, and $\mathbf u,\mathbf v$ are the vector parts of $q_r,q_i$.

## The Reduction

**Theorem (the Hermitian square and its scalar part).** For $\tilde Q=q_r+iq_i$ with $q_r,q_i$ real quaternions,

$$
\tilde Q\star\tilde Q=\tilde Q\tilde Q^{*}=\bigl(\lvert q_r\rvert^{2}+\lvert q_i\rvert^{2}\bigr)e_0+2i\Bigl(q_{r0}\mathbf v-q_{i0}\mathbf u+\mathbf u\times\mathbf v\Bigr),
$$

where $q_{r0},q_{i0}$ are the real scalar parts of $q_r,q_i$ and $\mathbf u,\mathbf v$ their vector parts. The square is **Hermitian**, its scalar part is

$$
\mathrm{Sc}\bigl(\tilde Q\star\tilde Q\bigr)=\lvert q_r\rvert^{2}+\lvert q_i\rvert^{2}=\sum_{\mu=0}^{3}\lvert Q_\mu\rvert^{2}\geq0,
$$

a real non-negative number vanishing only at $\tilde Q=0$.

*Proof.* The involution is $(\ )^{*}=\overline{\ }\,\circ\,{}^{\natural}$, and $q_r,q_i$ are real, so $\tilde Q^{*}=q_r^{\natural}-iq_i^{\natural}$. Expanding $\tilde Q\tilde Q^{*}=(q_r+iq_i)(q_r^{\natural}-iq_i^{\natural})$ and using $q_rq_r^{\natural}=\lvert q_r\rvert^{2}$, $q_iq_i^{\natural}=\lvert q_i\rvert^{2}$, and the product rule of the real quaternions for $q_iq_r^{\natural}-q_rq_i^{\natural}$ — whose scalar part vanishes and whose vector part is $-2q_{i0}\mathbf u+2q_{r0}\mathbf v+2\mathbf u\times\mathbf v$, giving the display after a sign change — yields the formula. The Hermitianness is $(\tilde Q\tilde Q^{*})^{*}=\tilde Q\tilde Q^{*}$, and the scalar part is read off the display.

**Corollary (the scalar trichotomy).** The equation $\tilde Q\star\tilde Q=\lambda e_0$ requires, for a complex scalar $\lambda$,

$$
\sum_{\mu=0}^{3}\lvert Q_\mu\rvert^{2}=\lambda\qquad\text{and}\qquad q_{r0}\mathbf v-q_{i0}\mathbf u+\mathbf u\times\mathbf v=0 .
$$

Consequently a central value $\lambda$ has a root only when $\lambda$ is a **non-negative real number**, and the three values separate: no root of $-1$, no root of $0$, roots of $+1$.

*Proof.* The two sides are equal exactly when the scalar and the vector parts are equal, and the scalar part of $\lambda e_0$ is $\lambda$. The scalar equation forces $\lambda=\sum_\mu\lvert Q_\mu\rvert^{2}$, a real number $\geq0$, so $\lambda=-1$ is excluded and $\lambda=0$ forces $\tilde Q=0$, which the definition excludes.

## The Roots of Minus One

**Theorem (no root of $-1$).** There is no element $\tilde Q$ with $\tilde Q\star\tilde Q=-e_0$.

*Proof.* The scalar part of the square is $\sum_\mu\lvert Q_\mu\rvert^{2}\geq0$ by the reduction, while the scalar part of $-e_0$ is $-1$; no element has a negative sum of modulus squares.

**Remark (the rootlessness is the sign of the form).** The parent algebra has roots of $-1$ for every splitting, and they are in bijection with its idempotents (*Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*); the block has none, because its scalar form is definite. The bijection of the parent is therefore not available here, and the block's idempotent theory is read on the **Hermitian** roots of $+1$ instead, in §*The Relation to the Idempotents*.

## The Roots of Zero

**Theorem (no root of $0$).** The equation $\tilde Q\star\tilde Q=0$ has the single solution $\tilde Q=0$, so the block has no nonzero square-zero element and the root set of $0$ is empty.

*Proof.* The scalar part of the square is $\sum_\mu\lvert Q_\mu\rvert^{2}$ by the reduction, and it vanishes only when every coordinate vanishes; a root is required to be nonzero, so the set is empty.

**Remark (square-zero and nilpotent are not the same here).** The block has no square-zero element, so it has no nilpotent of **index two**; its nilpotents have index **three**, and they are exactly the pure zero divisors, the elements with $Q_0=0$ and $(\mathbf Q,\mathbf Q)=0$ (*Nilpotents of the General Plain Sesqualgebra*). The empty root set of $0$ is therefore not the empty nilpotent set: the root of $0$ is the square-zero element, and the block has none, while the block has plenty of nilpotents at the next index. The distinction between "square-zero" and "nilpotent" is thus live in the block and not a coincidence of definitions.

**Remark (the pure zero divisors are not square-zero).** The parent's pure zero divisors, $Q_0=0$ with $(\mathbf Q,\mathbf Q)=0$, are its nonzero nilpotents of index two; the block's square does not vanish on them, $\tilde Q\star\tilde Q=\lVert\tilde Q\rVert_E^{2}e_0+\mathrm{Vect}(\tilde Q\tilde Q^{*})\neq0$, as *Zero Divisors of the General Plain Sesqualgebra* records, and the block's nilpotency index is raised to three. The root set of $0$ is empty although the zero-divisor set is not, and although the nilpotent set is not: the three classes of the block are distinct and they must not be conflated.

## The Roots of Plus One

**Theorem (the roots of $+1$).** The roots of $+1$ are exactly the elements

$$
\tilde Q=e^{i\theta}w,\qquad \theta\in\mathbb{R},\ w\in\mathbb{H}\ \text{real with}\ \lvert w\rvert=1,
$$

that is, the product of the unit circle of the central line with the unit sphere of the real quaternion subalgebra; the root set is $\{e^{i\theta}w\}=U(1)\cdot S^{3}$, of real dimension four, and it contains $e_0$, $-e_0$ and the pure imaginary unit vectors $i\hat\mu$ over the real unit vectors $\hat\mu$.

*Proof.* By the reduction the square is $e_0$ exactly when $\lvert q_r\rvert^{2}+\lvert q_i\rvert^{2}=1$ and $q_{r0}\mathbf v-q_{i0}\mathbf u+\mathbf u\times\mathbf v=0$. Dot the vector equation with $\mathbf u\times\mathbf v$: the first two terms are orthogonal to $\mathbf u\times\mathbf v$ and the third is $\lvert\mathbf u\times\mathbf v\rvert^{2}$, so $\mathbf u\times\mathbf v=0$; hence $\mathbf u$ and $\mathbf v$ are parallel, and the vector equation reads $q_{r0}\mathbf v=q_{i0}\mathbf u$. If $\mathbf u\neq0$ then $\mathbf v=\lambda\mathbf u$ for a real $\lambda$, the equation gives $q_{i0}=\lambda q_{r0}$ and therefore $q_i=q_{i0}+\mathbf v=\lambda(q_{r0}+\mathbf u)=\lambda q_r$: the halves are parallel as full quaternions, $\tilde Q=q_r+iq_i=(1+i\lambda)q_r$, and writing $1+i\lambda=\sqrt{1+\lambda^{2}}\,e^{i\theta}$ and $w=\sqrt{1+\lambda^{2}}\,q_r$, a real quaternion since $q_r$ is one, gives $\tilde Q=e^{i\theta}w$ with $\lvert w\rvert=1$ from the scalar equation. If $\mathbf u=0$ then $q_r=q_{r0}$ is a real scalar and the equation reads $q_{r0}\mathbf v=0$: either $\mathbf v=0$, and $\tilde Q=(q_{r0}+iq_{i0})e_0=e^{i\theta}e_0$ with $q_{r0}^{2}+q_{i0}^{2}=1$ is already of the required form with $w=e_0$, or $q_{r0}=0$, and $\tilde Q=iq_i=i(q_{i0}+\mathbf v)$ is of the required form with $\theta=\pi/2$ and the real unit $w=q_{i0}+\mathbf v$. In both cases $\tilde Q=e^{i\theta}w$ with $w$ a real unit quaternion. Conversely every $e^{i\theta}w$ with $w$ real unit has $q_r=\cos\theta\,w$, $q_i=\sin\theta\,w$, hence $\lvert q_r\rvert^{2}+\lvert q_i\rvert^{2}=1$ and $q_{r0}\mathbf v-q_{i0}\mathbf u+\mathbf u\times\mathbf v=\cos\theta\sin\theta(w_0\mathbf w-\mathbf w_0 w)=0$, so it is a root. The parametrisation $(\theta,w)\mapsto e^{i\theta}w$ has kernel $\{(0,e_0),(\pi,-e_0)\}$, of order two, so the root set is a single real four-dimensional family, and the named elements are the cases $\theta=0$, $\theta=\pi$ and $\theta=\pi/2$ with $w=\hat\mu$.

**Corollary (the roots of $+1$ are never zero divisors).** Every root of $+1$ has $\mathrm{Sc}(\tilde Q\star\tilde Q)=1$, hence $\lVert\tilde Q\rVert_E=1$, and its norm lies on the unit circle of the centre:

$$
N(e^{i\theta}w)=e^{2i\theta},\qquad\text{in particular}\qquad N(\pm e_0)=1,\qquad N(i\hat\mu)=-1 .
$$

Every root of $+1$ is therefore one-sidedly invertible, and the root set of $+1$ is **disjoint** from the zero-divisor cone.

*Proof.* The normalisation is the scalar equation $\mathrm{Sc}=1$ and the Euclidean norm of the reduction. For the norm, $N(\tilde Q)=\sum_\mu Q_\mu^{2}$ with $Q_\mu=e^{i\theta}w_\mu$ and $w_\mu$ real, so $N(\tilde Q)=e^{2i\theta}\sum_\mu w_\mu^{2}=e^{2i\theta}$, of modulus one and never zero; the named values are the cases $\theta=0,\pi$ and $\theta=\pi/2$. The zero-divisor criterion is $N=0$ (*Zero Divisors of the General Plain Sesqualgebra*), so the root set misses the cone, and the invertibility criterion $N\neq0$ holds throughout (*Norm and Invertibility in the General Plain Sesqualgebra*).

**Remark (roots and zero divisors are separated).** The root set of $+1$ and the zero-divisor cone are the two subsets of the block the scalar part of the square controls, and they are disjoint: the roots have $\lVert\tilde Q\rVert_E=1$ and $N$ on the unit circle, the zero divisors have $N=0$. The separation is a fact of the block's definite square, and it is read on the norm as $N(e^{i\theta}w)=e^{2i\theta}\neq0$.

**Remark (the dimension and the shape).** The parent's root set of $-1$ is two isolated elements together with a two-parameter family and a four-parameter family, and its root set of $+1$ is the bijective image of that set; the block has its roots of $+1$ in a single family $U(1)\cdot S^{3}$, of real dimension four, and no roots of the other two values. The block's set is the single orbit $U(1)\cdot S^{3}$ and the parent's is not, and the parent's two isolated roots $\pm i$ have no counterpart in the block.

## The Relation to the Idempotents

**Definition (the Hermitian roots of $+1$).** A root of $+1$ is **Hermitian** when $\tilde Q^{*}=\tilde Q$. The Hermitian roots of $+1$ are $\pm e_0$ together with the pure imaginary unit vectors $i\hat\mu$ over the real unit vectors $\hat\mu$.

*Proof.* A Hermitian element is $\alpha e_0+i\mathbf a$ with $\alpha\in\mathbb{R}$ and $\mathbf a$ a real vector, and its square is $\alpha^{2}e_0-\lvert\mathbf a\rvert^{2}e_0+2\alpha i\mathbf a$; the equation is $(\alpha^{2}+\lvert\mathbf a\rvert^{2})e_0+2\alpha i\mathbf a=e_0$, whose solution is $\alpha=\pm1$ with $\mathbf a=0$ or $\alpha=0$ with $\lvert\mathbf a\rvert=1$. The last is $i\hat\mu$.

**Theorem (the idempotents of the block are the halved Hermitian roots of $+1$).** The map $\tilde Q\mapsto\tfrac12(e_0+\tilde Q)$ is a bijection from the Hermitian roots of $+1$ onto the idempotents of the block,

$$
0=\tfrac12(e_0-e_0),\qquad e_0=\tfrac12(e_0+e_0),\qquad \tfrac12(e_0+i\hat\mu),\ \ \hat\mu\in\mathbb{R}^{3},\ (\hat\mu,\hat\mu)=1 .
$$

*Proof.* A root $\tilde Q$ of $+1$ that is Hermitian satisfies $\tilde Q^{*}=\tilde Q$ and $\tilde Q^{2}=\tilde Q\tilde Q^{*}=e_0$, so $\tfrac12(e_0+\tilde Q)$ is Hermitian and has square $\tfrac14(e_0+2\tilde Q+\tilde Q^{2})=\tfrac14(2e_0+2\tilde Q)=\tfrac12(e_0+\tilde Q)$: it is a Hermitian idempotent of the algebra, hence an idempotent of the block by *Idempotents of the General Plain Sesqualgebra*. Conversely an idempotent of the block is a Hermitian idempotent $\tilde\Pi$ of the algebra, and $\tilde Q=2\tilde\Pi-e_0$ is Hermitian with square $(2\tilde\Pi-e_0)^{2}=4\tilde\Pi-4\tilde\Pi+e_0=e_0$, a Hermitian root of $+1$. The two maps are inverse, and the list is the classification of §*The Roots of Plus One*.

**Remark (the parent's bijection replaced).** The parent bijects its idempotents with its roots of $-1$, $\tilde\Pi(\xi)=\tfrac12(e_0+\xi i)$; the block bijects its idempotents with the **Hermitian** roots of $+1$, because the block has no root of $-1$. The two statements agree on the elements they share: the Hermitian idempotents $\tfrac12(e_0+i\hat\mu)$ are the parent idempotents with a real root $\xi=\pm\hat\mu$, and they are the block idempotents. The mixed roots of the parent give idempotents that are not Hermitian and not idempotent for the block (*Idempotents of the General Plain Sesqualgebra*).

## The Three Sets Compared

| central value $\lambda$ | the block | the parent |
|---|---|---|
| $-1$ | no root | two isolated elements, a two-parameter family and a four-parameter family |
| $0$ | no root | the origin and a four-parameter family, the nilpotent cone |
| $+1$ | $U(1)\cdot S^{3}$, real dimension four | the image of the roots of $-1$ under $\tilde P\mapsto\tilde P i$ |

The block carries exactly one of the three classes, and its class is the single orbit $U(1)\cdot S^{3}$, of real dimension four; the parent carries all three, and its sets are unbounded and include the two isolated elements $\pm i$ and $\pm1$. The difference is the sign of the diagonal of the square: the block's $\mathrm{Sc}(\tilde Q\star\tilde Q)=\sum_\mu\lvert Q_\mu\rvert^{2}$ is definite, and the negative and the zero values are excluded.

## Summary

The square of an element of the general plain sesqualgebra is the Hermitian element $\tilde Q\star\tilde Q=\tilde Q\tilde Q^{*}=(\lvert q_r\rvert^{2}+\lvert q_i\rvert^{2})e_0+2i(q_{r0}\mathbf v-q_{i0}\mathbf u+\mathbf u\times\mathbf v)$ in the real halves $\tilde Q=q_r+iq_i$, whose scalar part is the definite quantity $\sum_\mu\lvert Q_\mu\rvert^{2}$. The scalar part decides the three central values: **minus one has no root**, the scalar part being non-negative; **zero has no root**, the scalar part vanishing only at the origin and the origin being excluded; and **plus one has a root**. The root set of $+1$ is exactly the family $e^{i\theta}w$ over the real unit quaternions $w$, that is $U(1)\cdot S^{3}$, a single real four-dimensional family containing $e_0$, $-e_0$ and the pure imaginary unit vectors $i\hat\mu$; it is a single family and not the parent's several families together with the isolated elements $\pm i$. The **Hermitian** roots of $+1$ are $\pm e_0$ and the $i\hat\mu$, and the map $\tilde Q\mapsto\tfrac12(e_0+\tilde Q)$ is a bijection from them onto the idempotents of the block, which are $0$, $e_0$ and the $\tfrac12(e_0+i\hat\mu)$; the parent's bijection between idempotents and roots of $-1$ has no analogue, because the block has no root of $-1$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ | the product of the block |
| $\tilde Q=q_r+iq_i$ | the imaginary decomposition, $q_r,q_i$ real quaternions |
| $\mathbf u,\mathbf v$ | the vector parts of $q_r,q_i$ |
| $\tilde Q\star\tilde Q=\tilde Q\tilde Q^{*}$ | the Hermitian square |
| $\mathrm{Sc}(\tilde Q\star\tilde Q)=\sum_\mu\lvert Q_\mu\rvert^{2}$ | the scalar part, definite |
| $\mathcal{R}(-1)=\varnothing$ | no root of $-1$ |
| $\mathcal{R}(0)=\varnothing$ | no nonzero root of $0$ |
| $\mathcal{R}(+1)=U(1)\cdot S^{3}=\{e^{i\theta}w\}$ | the roots of $+1$, real dimension four |
| $\pm e_0,\ i\hat\mu$ | the Hermitian roots of $+1$ |
| $\tfrac12(e_0+i\hat\mu)$ | the idempotents of the block, the halved Hermitian roots |

## Further Reading

- *Introduction to the General Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-general-plain-sesqualgebra-of-biquaternions.md`), for the product, its class and the involution in the second slot.
- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the relative definition of the root and the designation of the three central values.
- *Norm and Invertibility in the General Plain Sesqualgebra* (`articles_maths/norm-and-invertibility-in-the-general-plain-sesqualgebra.md`), for the norm, the square and the definiteness of the scalar part.
- *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-general-plain-algebra.md`), for the three sets of the parent and the idempotent bijection.
- *Square Roots of a General Element in the General Plain Sesqualgebra* (`articles_maths/square-roots-of-a-general-element-in-the-general-plain-sesqualgebra.md`), for the general reduction of the root equation of which these three are the central cases.
- *Idempotents of the General Plain Sesqualgebra* (`articles_maths/idempotents-of-the-general-plain-sesqualgebra.md`), for the Hermitian idempotents the roots of $+1$ produce.
- *Zero Divisors of the General Plain Sesqualgebra* (`articles_maths/zero-divisors-of-the-general-plain-sesqualgebra.md`), for the zero-divisor criterion $N=0$, which no root of $+1$ satisfies.
- *Nilpotents of the General Plain Sesqualgebra* (`articles_maths/nilpotents-of-the-general-plain-sesqualgebra.md`), for the index-three nilpotents, which are the pure zero divisors and are not the roots of $0$.
