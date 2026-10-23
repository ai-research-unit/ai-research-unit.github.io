# __Square Roots of a General Element in the General Plain Sesqualgebra__

## Introduction

The general plain sesqualgebra is the operation $\tilde Q_1\star\tilde Q_2=\tilde Q_1\tilde Q_2^{*}$ on the biquaternion space (*Introduction to the General Plain Sesqualgebra*). This article solves the square-root problem of the block: for a given element $\tilde Q\in\mathbb{B}$, decide whether there is a **square root** $\tilde\Xi$ with

$$
\tilde\Xi\star\tilde\Xi=\tilde Q,
$$

and describe the set of them. A square root names a product, and the definition is relative; it is stated once for a general product in *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*Powers, the Square and the Roots*, and throughout this article the square is the block's, the **Hermitian square** $\tilde\Xi\star\tilde\Xi=\tilde\Xi\tilde\Xi^{*}$. The equation is therefore free of the involution arithmetic of the parent, and it has a clean image: the **Hermitian cone**

$$
\mathcal{C}=\{\tilde Q=\alpha e_t+i\vec w:\alpha\in\mathbb{R},\ \vec w\in\mathbb{R}^{3},\ \alpha\geq\lvert\vec w\rvert\},
$$

the set of the Hermitian elements whose scalar part dominates the modulus of the vector part. The theorem of the article is that the square map $\tilde\Xi\mapsto\tilde\Xi\star\tilde\Xi$ has **exactly** this image, that a square root exists exactly when $\tilde Q$ lies in $\mathcal{C}$, that on the interior of $\mathcal{C}$ the root set is a real four-parameter family, and that the roots of a central value are the special case of the two companion articles, whose nonempty class of the central values is $+1$.

**The results.** The block-square is the Hermitian element $\tilde Q\star\tilde Q=\tilde Q\tilde Q^{*}=(\lvert q_r\rvert^{2}+\lvert q_i\rvert^{2})e_t+2i(q_{r0}\vec v-q_{i0}\vec q+\vec q\times\vec v)$ in the real halves, with scalar part $s=\lvert q_r\rvert^{2}+\lvert q_i\rvert^{2}$ and vector part $\vec w=2(q_{r0}\vec v-q_{i0}\vec q+\vec q\times\vec v)$ satisfying $\lvert\vec w\rvert\leq s$. Its image is exactly the Hermitian cone $\mathcal{C}=\{\alpha e_t+i\vec w:\alpha\geq\lvert\vec w\rvert\}$, so the equation $\tilde\Xi\star\tilde\Xi=\tilde Q$ has a solution exactly when $\tilde Q\in\mathcal{C}$, the boundary being the image of the zero divisors and the interior the image of the regular elements. On the interior the root set of a value is a single orbit $\{\exp(i\theta)\tilde\Xi_0u\}$ of real dimension four under $\mathrm{U}(1)\times S^{3}$, and on the central line a root exists exactly for $\lambda\geq0$ real.

## The Reduction of the General Square

**The block-square in the real halves is the Hermitian element $\tilde Q\star\tilde Q=\tilde Q\tilde Q^{*}=(\lvert q_r\rvert^{2}+\lvert q_i\rvert^{2})e_t+2i(q_{r0}\vec v-q_{i0}\vec q+\vec q\times\vec v)$, whose scalar part is the definite $s=\lvert q_r\rvert^{2}+\lvert q_i\rvert^{2}$ and whose vector part is $\vec w=2(q_{r0}\vec v-q_{i0}\vec q+\vec q\times\vec v)$.**

**Theorem (the square in the real halves).** For $\tilde Q=q_r+iq_i$,

$$
\boxed{\;\tilde Q\star\tilde Q=\tilde Q\tilde Q^{*}=\bigl(\lvert q_r\rvert^{2}+\lvert q_i\rvert^{2}\bigr)e_t+2i\Bigl(q_{r0}\vec v-q_{i0}\vec q+\vec q\times\vec v\Bigr)\;}.
$$

The square is **Hermitian**; its scalar part is $s=\lvert q_r\rvert^{2}+\lvert q_i\rvert^{2}\geq0$ and its vector part, written $\vec w$, is $\vec w=2\bigl(q_{r0}\vec v-q_{i0}\vec q+\vec q\times\vec v\bigr)$. Consequently the equation $\tilde\Xi\star\tilde\Xi=\tilde Q$ has a solution only when $\tilde Q$ is **Hermitian**, and when $\tilde Q=\alpha e_t+i\vec w$ with $\alpha\in\mathbb{R}$, $\vec w\in\mathbb{R}^{3}$ it splits into the two real equations

$$
\lvert q_r\rvert^{2}+\lvert q_i\rvert^{2}=\alpha,\qquad 2\bigl(q_{r0}\vec v-q_{i0}\vec q+\vec q\times\vec v\bigr)=\vec w .
$$

*Proof.* The display is *Square Roots of One and the Idempotents of the General Plain Sesqualgebra*, §*The Reduction*, and the Hermitianness is $(\tilde Q\tilde Q^{*})^{*}=\tilde Q\tilde Q^{*}$. Comparing the Hermitian element $\tilde\Xi\star\tilde\Xi$ with $\alpha e_t+i\vec w$ is comparing the scalar parts and the vector parts, which are the two equations.

**Remark (the square map is not the parent's).** The parent's square is bilinear, $\tilde Q^{2}=(\text{quadratic form})e_t+\cdots$, and it is the source of the two-involution arithmetic; the block's square is the Hermitian square, and the whole article rests on the two real quantities it produces, the definite scalar part and the vector part. The first decides invertibility and the second is what the cone constrains.

## The Image: the Hermitian Cone

**The vector part of the square is dominated by its scalar part, $\lvert\vec w\rvert\leq s$, and the square map is onto the Hermitian cone $\mathcal{C}=\{\alpha e_t+i\vec w:\alpha\geq\lvert\vec w\rvert\}$, so its image is exactly $\mathcal{C}$.**

**Theorem (the vector part is dominated by the scalar part).** For every $\tilde Q$,

$$
\boxed{\;\lvert\vec w\rvert\leq s=\mathrm{Sc}\bigl(\tilde Q\star\tilde Q\bigr)\;},
$$

so the square takes its values in the Hermitian cone $\mathcal{C}$.

*Proof.* Note that $q_rq_i^{\natural}$ is a real quaternion of modulus $\lvert q_r\rvert\lvert q_i\rvert$, and its vector part is $\pm\vec w/2$, since $\mathrm{Vect}(q_rq_i^{\natural})=-(q_{r0}\vec v-q_{i0}\vec q+\vec q\times\vec v)$. Since the vector part of a real quaternion has modulus at most that of the quaternion, $\lvert\vec w\rvert/2=\lvert\mathrm{Vect}(q_rq_i^{\natural})\rvert\leq\lvert q_rq_i^{\natural}\rvert=\lvert q_r\rvert\lvert q_i\rvert\leq\tfrac12(\lvert q_r\rvert^{2}+\lvert q_i\rvert^{2})=s/2$, the last being the arithmetic–geometric inequality. So $\lvert\vec w\rvert\leq s$.

**Theorem (the square map is onto the cone).** For every $\tilde Q=\alpha e_t+i\vec w$ in $\mathcal{C}$ there is a $\tilde\Xi$ with $\tilde\Xi\star\tilde\Xi=\tilde Q$. Hence the image of the square map is exactly $\mathcal{C}$.

*Proof.* Choose $q_r,q_i$ **pure** ($q_{r0}=q_{i0}=0$), so the scalar and vector equations become $\lvert q_r\rvert^{2}+\lvert q_i\rvert^{2}=\alpha$ and $2\,\vec q\times\vec v=\vec w$. Take the perpendicular vectors $\vec q,\vec v$ with $\lvert\vec q\rvert^{2}=p_+$, $\lvert\vec v\rvert^{2}=p_-$ and $\lvert\vec q\rvert\lvert\vec v\rvert=\lvert\vec w\rvert/2$, where

$$
p_{\pm}=\frac{\alpha\pm\sqrt{\alpha^{2}-\lvert\vec w\rvert^{2}}}{2},
$$

which is real and non-negative exactly because $\alpha\geq\lvert\vec w\rvert$; then $\lvert\vec q\rvert^{2}+\lvert\vec v\rvert^{2}=\alpha$ and $\lvert\vec q\times\vec v\rvert=\lvert\vec w\rvert/2$. Choosing the plane of $\vec q$ and $\vec v$ and the ordered pair so that $\vec q\times\vec v=\vec w/2$, the element $\tilde\Xi=q_r+iq_i$ solves the two equations. The image is $\mathcal{C}$ by the two theorems.

**Remark (the boundary is the square of the zero divisors).** The inequality $\lvert\vec w\rvert\leq s$ is an equality exactly when $\lvert q_r\rvert=\lvert q_i\rvert$ and $q_r\perp q_i$ as real quaternions; then $\tilde Q$ is a zero divisor unless it is the origin, because $C(\tilde Q)=\lvert q_r\rvert^{2}-\lvert q_i\rvert^{2}+2i\langle q_r,q_i\rangle$ vanishes under these two conditions. The boundary $\{\alpha=\lvert\vec w\rvert\}$ of the cone is therefore the set of the squares of the zero divisors, its vertex $\tilde Q=0$ alone excepted, which is the image of the origin; and the witness $\tilde\Xi=\vec e_x+i\vec e_y$ has $\tilde\Xi\star\tilde\Xi=2e_t+2i\vec e_z$, that is $\alpha=2$ and $\vec w=2\vec u_z$, on the boundary with $\alpha=\lvert\vec w\rvert=2$. The interior $\{\alpha>\lvert\vec w\rvert\}$ is the set of the squares of the regular elements, and its image is the interior of the cone.

## The Roots of a Central Value

**The equation $\tilde\Xi\star\tilde\Xi=\lambda e_t$ has a solution exactly when $\lambda\geq0$ is real, with the root set $\{\exp(i\theta)w\}$ of real dimension four for $\lambda>0$ and the single origin for $\lambda=0$.**

**Corollary (the central reduction).** For $\lambda\in\mathbb{C}$ the equation $\tilde\Xi\star\tilde\Xi=\lambda e_t$ has a solution exactly when $\lambda\geq0$ is real; then the root set is the family $\{\exp(i\theta)w:\theta\in\mathbb{R},\ w\in\mathbb{H}\ \text{real},\ \lvert w\rvert=\sqrt{\lambda}\}$, of real dimension four, and for $\lambda=0$ the only solution is $\tilde\Xi=0$.

*Proof.* The cone membership of $\lambda e_t$ is $\lambda\geq\lvert\mathbf 0\rvert=0$ with $\lambda$ real; the root set is read in *Square Roots of One and the Idempotents of the General Plain Sesqualgebra*, which computes it for $\lambda=1$ and which scales by $\sqrt{\lambda}$, the value $0$ being the case of *Square Roots of Zero and the Nilpotents of the General Plain Sesqualgebra*. The value $0$ is the single point of the cone where the theorem's $p_\pm$ coincide and the only solution is the origin.

**Remark (the three central values, recovered).** This corollary is the whole of the trichotomy of the two companion articles: the negative and the non-real scalars are outside the cone, the scalar $0$ has only the excluded origin, and the positive scalars have the four-parameter family of roots. The general theorem of this article is what the trichotomy specialises, and the specialisation is the cone's intersection with the central line.

## The Structure of a Root Set

**The group $\mathrm{U}(1)\times S^{3}$ acts by $\tilde\Xi\mapsto \exp(i\theta)\tilde\Xi u$ and leaves the square invariant, and on the interior of the cone the root set of a value is a single orbit of real dimension four.**

**Theorem (the symmetry of the square).** The group $\mathrm{U}(1)\times S^{3}$ acts on $\mathbb{B}$ by $\tilde\Xi\mapsto \exp(i\theta)\,\tilde\Xi\,u$, where $\theta\in\mathbb{R}$ and $u$ is a real unit quaternion, and the square map is invariant under the action:

$$
(\exp(i\theta)\tilde\Xi u)\star(\exp(i\theta)\tilde\Xi u)=\exp(i\theta)\tilde\Xi uu^{*}\tilde\Xi^{*}\exp(-i\theta)=\tilde\Xi\tilde\Xi^{*}=\tilde\Xi\star\tilde\Xi .
$$

The kernel of the action is the central subgroup $\{(0,e_t),(\pi,-e_t)\}\cong\mathbb{Z}/2$, so each orbit is of real dimension four, and the action carries the root set of every element into itself.

*Proof.* The right factor is $uu^{*}=\lvert u\rvert^{2}=1$, and the central scalars $\exp(i\theta)$ commute with the coefficientwise conjugation, so the two factors cancel against their conjugates. The kernel is the solution of $\exp(i\theta)u=e_t$ with $u$ real, which forces $u=\exp(-i\theta)$ real, hence $\exp(i\theta)=\pm1$ and $u=\pm e_t$.

**Proposition (the root set of an interior value is a single orbit).** Let $\tilde Q$ be in the interior of the cone and let $\tilde\Xi_0$ be one of its roots. Then the root set of $\tilde Q$ is exactly the orbit of $\tilde\Xi_0$ under the action,

$$
\boxed{\;\{\tilde\Xi:\tilde\Xi\star\tilde\Xi=\tilde Q\}=\{\exp(i\theta)\tilde\Xi_0u:\theta\in\mathbb{R},\ u\in\mathbb{H}\ \text{real},\ \lvert u\rvert=1\}\;},
$$

so it is a single real four-parameter family.

*Proof.* The value is interior, $\alpha>\lvert\vec w\rvert$, so every root is regular, by the reading of the interior as the set of the squares of the regular elements in §*The Image: the Hermitian Cone*; in particular $\tilde\Xi_0^{-1}$ exists. For any root $\tilde\Xi$ the quotient $\tilde Q_3=\tilde\Xi_0^{-1}\tilde\Xi$ satisfies

$$
\tilde Q_3\tilde Q_3^{*}=\tilde\Xi_0^{-1}\tilde\Xi\tilde\Xi^{*}\bigl(\tilde\Xi_0^{-1}\bigr)^{*}=\tilde\Xi_0^{-1}\tilde\Xi_0\tilde\Xi_0^{*}\bigl(\tilde\Xi_0^{*}\bigr)^{-1}=\tilde\Xi_0^{*}\bigl(\tilde\Xi_0^{*}\bigr)^{-1}=e_t ,
$$

using $\tilde\Xi\tilde\Xi^{*}=\tilde\Xi_0\tilde\Xi_0^{*}=\tilde Q$ and $\bigl(\tilde\Xi_0^{-1}\bigr)^{*}=\bigl(\tilde\Xi_0^{*}\bigr)^{-1}$; so $\tilde Q_3$ is a root of $+1$, and $\tilde Q_3=\exp(i\theta)u$ by the classification of the roots of $+1$ of *Square Roots of One and the Idempotents of the General Plain Sesqualgebra*. Hence $\tilde\Xi=\tilde\Xi_0\tilde Q_3=\exp(i\theta)\tilde\Xi_0u$ lies in the orbit of $\tilde\Xi_0$; conversely every element of the orbit is a root, by the theorem on the symmetry of the square. The orbit is of real dimension four, the kernel of the action being $\mathbb{Z}/2$.

**Remark (the orbit and the fiber).** The map $\tilde\Xi\mapsto\tilde\Xi\star\tilde\Xi$ is $\mathrm{U}(1)\times S^{3}$-equivariant for the trivial action on the target and the action above on the source, so each fibre is a union of orbits, and over an interior value it is the single orbit of the proposition. The degenerate values are the origin ($\alpha=\lvert\vec w\rvert=0$), whose only root is $\tilde\Xi=0$, and the boundary, whose roots are the zero divisors. The element $\exp(i\theta)\tilde\Xi u$ is a **root transform**: the block's square is invariant under the right multiplication by the real unit quaternions, because the involution fixes the real subalgebra and therefore the second slot is blind to it.

## The Comparison with the Parent

**The block's square is Hermitian and its image is the Hermitian cone, where the parent's square is bilinear and its image is the whole space except the nonzero nilpotents; on the interior the block's root set is a real four-parameter $\mathrm{U}(1)\times S^{3}$ family, and on the central line only $\lambda\geq0$ occurs.**

| clause | general plain algebra | general plain sesqualgebra |
|---|---|---|
| square | $\tilde Q^{2}$, bilinear | $\tilde Q\star\tilde Q=\tilde Q\tilde Q^{*}$, Hermitian |
| image | the whole space except the nonzero nilpotents, the pure isotropic cone | the Hermitian cone $\{\alpha\geq\lvert\vec w\rvert\}$ |
| existence | for every element except the nonzero nilpotents | exactly on the cone |
| root set | two-involution arithmetic, parametrised by the square | a real four-parameter $\mathrm{U}(1)\times S^{3}$ family on the interior |
| central value | three classes, all nonempty | only $\lambda\geq0$ |

The parent has a square root of every element except its nonzero nilpotents, and the block has one only on the cone; on the cone the block's root set is the orbit of a single root under the four-dimensional group $\mathrm{U}(1)\times S^{3}$, and its equality with the fibre is the element-level reason the block's right multiplication is the faithful side (*The Specificities of the General Plain Sesqualgebra*).

## Summary

The square of an element of the general plain sesqualgebra is the Hermitian element $\tilde\Xi\star\tilde\Xi=\tilde\Xi\tilde\Xi^{*}$, whose scalar part $s=\lvert q_r\rvert^{2}+\lvert q_i\rvert^{2}$ and vector part $\vec w=2(q_{r0}\vec v-q_{i0}\vec q+\vec q\times\vec v)$ satisfy $\lvert\vec w\rvert\leq s$ in the real halves $\tilde\Xi=q_r+iq_i$. The **image** of the square map is therefore contained in the **Hermitian cone** $\mathcal{C}=\{\alpha e_t+i\vec w:\alpha\geq\lvert\vec w\rvert\}$, and the containment is an equality: a square root of $\alpha e_t+i\vec w$ exists exactly when $\alpha\geq\lvert\vec w\rvert$, the boundary being the image of the zero divisors, its vertex excepted and the vertex the image of the origin, and the interior the image of the regular elements. The equation $\tilde\Xi\star\tilde\Xi=\tilde Q$ has a solution exactly for $\tilde Q\in\mathcal{C}$, and on the interior the root set is the orbit $\{\exp(i\theta)\tilde\Xi_0u\}$ of any one root under the action $\tilde\Xi\mapsto \exp(i\theta)\tilde\Xi u$ of $\mathrm{U}(1)\times S^{3}$, whose kernel is $\mathbb{Z}/2$: a single real four-parameter family. The roots of a central value are the cone's intersection with the central line: only $\lambda\geq0$ real, with the four-parameter family for $\lambda>0$ and the excluded origin for $\lambda=0$, which is the trichotomy of *Square Roots of One and the Idempotents of the General Plain Sesqualgebra* and *Square Roots of Zero and the Nilpotents of the General Plain Sesqualgebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Q_1\star\tilde Q_2=\tilde Q_1\tilde Q_2^{*}$ | the product of the block |
| $\tilde\Xi=q_r+iq_i$ | the imaginary decomposition, $q_r,q_i$ real quaternions |
| $\vec q,\vec v$ | the vector parts of $q_r,q_i$ |
| $\tilde\Xi\star\tilde\Xi=\tilde\Xi\tilde\Xi^{*}$ | the square, Hermitian |
| $s=\lvert q_r\rvert^{2}+\lvert q_i\rvert^{2}$ | the scalar part of the square, definite |
| $\vec w=2(q_{r0}\vec v-q_{i0}\vec q+\vec q\times\vec v)$ | the vector part of the square |
| $\lvert\vec w\rvert\leq s$ | the domination, the cone inequality |
| $\mathcal{C}=\{\alpha e_t+i\vec w:\alpha\geq\lvert\vec w\rvert\}$ | the Hermitian cone, the image of the square |
| $p_{\pm}=\tfrac12(\alpha\pm\sqrt{\alpha^{2}-\lvert\vec w\rvert^{2}})$ | the modulus squares of the pure halves in the construction |
| $\tilde\Xi\mapsto \exp(i\theta)\tilde\Xi u$ | the $\mathrm{U}(1)\times S^{3}$ action preserving the square |

## Further Reading

- [Introduction to the General Plain Sesqualgebra](introduction-to-the-general-plain-sesqualgebra.html), for the product, its class and the two scalar rules.
- [Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternion-c-space.html), for the relative definition of the square root.
- [Square Roots of One and the Idempotents of the General Plain Sesqualgebra](square-roots-of-one-and-the-idempotents-of-the-general-plain-sesqualgebra.html), for the reduction of the square, the root set of $+1$ and the idempotents.
- [Square Roots of Zero and the Nilpotents of the General Plain Sesqualgebra](square-roots-of-zero-and-the-nilpotents-of-the-general-plain-sesqualgebra.html), for the root set of $0$ and the index-three nilpotents.
- [Norm and Invertibility in the General Plain Sesqualgebra](norm-and-invertibility-in-the-general-plain-sesqualgebra.html), for the square and the definiteness of its scalar part.
- [Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint](positivity-and-the-hermitian-cone-of-the-biquaternion-algebra-with-hermitian-adjoint.html), for the Hermitian cone and the positivity of the quadratic form.
- [Square Roots of a General Element in the Biquaternion Algebra](square-roots-of-a-general-element-in-the-biquaternion-algebra.html), for the two-involution arithmetic of the parent.
