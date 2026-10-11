# __Square Roots of a General Element in the General Plain Sesqualgebra__

## Introduction

The general plain sesqualgebra is the operation $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ on the biquaternion space (*Introduction to the General Plain Sesqualgebra of Biquaternions*). This article solves the square-root problem of the block: for a given element $\tilde a\in\mathbb{B}$, decide whether there is a **square root** $\tilde X$ with

$$
\tilde X\star\tilde X=\tilde a,
$$

and describe the set of them. A square root names a product, and the definition is relative; it is stated once for a general product in *Definitions for the Study of the 12 Algebraic Structures*, §*Powers, the Square and the Roots*, and throughout this article the square is the block's, the **Hermitian square** $\tilde X\star\tilde X=\tilde X\tilde X^{*}$. The equation is therefore free of the involution arithmetic of the parent, and it has a clean image: the **Hermitian cone**

$$
\mathcal{C}=\{\tilde a=\alpha e_0+i\mathbf w:\alpha\in\mathbb{R},\ \mathbf w\in\mathbb{R}^{3},\ \alpha\geq\lvert\mathbf w\rvert\},
$$

the set of the Hermitian elements whose scalar part dominates the modulus of the vector part. The theorem of the article is that the square map $\tilde X\mapsto\tilde X\star\tilde X$ has **exactly** this image, that a square root exists exactly when $\tilde a$ lies in $\mathcal{C}$, that on the interior of $\mathcal{C}$ the root set is a real four-parameter family, and that the roots of a central value are the special case of the previous article, whose only nonempty class is $+1$.

**Placement.** The article is the fifth entry of the *Common Theory* section of the block, after the roots of the three central values and before the idempotents and the nilpotents. It uses the product and the class of the introduction, the square and its scalar part from *Norm and Invertibility in the General Plain Sesqualgebra* and *Square Roots of Minus One, Zero and Plus One in the General Plain Sesqualgebra*, and the Hermitian cone.

**Boundaries.** The product, its class and its placement are *Introduction to the General Plain Sesqualgebra of Biquaternions*; the relative definition of the square root is *Definitions for the Study of the 12 Algebraic Structures*, and the two-involution arithmetic of the parent is *Square Roots of a General Element in the General Plain Algebra*. The three central values of the block, and their root sets, are *Square Roots of Minus One, Zero and Plus One in the General Plain Sesqualgebra*; the Hermitian subspace, the positivity and the cone are *Hermitian and Skew-Hermitian Elements* and *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*; the idempotents that the roots of $+1$ produce are *Idempotents of the General Plain Sesqualgebra*. Nothing topological and nothing metric appears.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ with $e_1e_2=e_3$ and central scalar imaginary $i$. An element is $\tilde Q=\sum_{\mu=0}^{3}Q_\mu e_\mu=Q_0e_0+\mathbf Q$ with $\mathbf Q=Q_1e_1+Q_2e_2+Q_3e_3$; the natural conjugation is $\tilde Q^{\natural}=Q_0-\mathbf Q$, the coefficientwise conjugation is $\overline{\tilde Q}=\overline{Q_0}e_0+\overline{\mathbf Q}$, and the Hermitian conjugation is $\tilde Q^{*}=\overline{\tilde Q^{\natural}}$. The product is $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$. In the imaginary decomposition $\tilde Q=q_r+iq_i$ the halves $q_r,q_i$ are real quaternions, with real scalar parts $q_{r0},q_{i0}$ and vector parts $\mathbf u,\mathbf v$.

## The Reduction of the General Square

**Theorem (the square in the real halves).** For $\tilde Q=q_r+iq_i$,

$$
\tilde Q\star\tilde Q=\tilde Q\tilde Q^{*}=\bigl(\lvert q_r\rvert^{2}+\lvert q_i\rvert^{2}\bigr)e_0+2i\Bigl(q_{r0}\mathbf v-q_{i0}\mathbf u+\mathbf u\times\mathbf v\Bigr) .
$$

The square is **Hermitian**; its scalar part is $s=\lvert q_r\rvert^{2}+\lvert q_i\rvert^{2}\geq0$ and its vector part, written $\mathbf w$, is $\mathbf w=2\bigl(q_{r0}\mathbf v-q_{i0}\mathbf u+\mathbf u\times\mathbf v\bigr)$. Consequently the equation $\tilde X\star\tilde X=\tilde a$ has a solution only when $\tilde a$ is **Hermitian**, and when $\tilde a=\alpha e_0+i\mathbf w$ with $\alpha\in\mathbb{R}$, $\mathbf w\in\mathbb{R}^{3}$ it splits into the two real equations

$$
\lvert q_r\rvert^{2}+\lvert q_i\rvert^{2}=\alpha,\qquad 2\bigl(q_{r0}\mathbf v-q_{i0}\mathbf u+\mathbf u\times\mathbf v\bigr)=\mathbf w .
$$

*Proof.* The display is *Square Roots of Minus One, Zero and Plus One in the General Plain Sesqualgebra*, §*The Reduction*, and the Hermitianness is $(\tilde Q\tilde Q^{*})^{*}=\tilde Q\tilde Q^{*}$. Comparing the Hermitian element $\tilde X\star\tilde X$ with $\alpha e_0+i\mathbf w$ is comparing the scalar parts and the vector parts, which are the two equations.

**Remark (the square map is not the parent's).** The parent's square is bilinear, $\tilde Q^{2}=(\text{quadratic form})e_0+\cdots$, and it is the source of the two-involution arithmetic; the block's square is the Hermitian square, and the whole article rests on the two real quantities it produces, the definite scalar part and the vector part. The first decides invertibility and the second is what the cone constrains.

## The Image: the Hermitian Cone

**Theorem (the vector part is dominated by the scalar part).** For every $\tilde Q$,

$$
\lvert\mathbf w\rvert\leq s=\mathrm{Sc}\bigl(\tilde Q\star\tilde Q\bigr),
$$

so the square takes its values in the Hermitian cone $\mathcal{C}$.

*Proof.* Note that $q_rq_i^{\natural}$ is a real quaternion of modulus $\lvert q_r\rvert\lvert q_i\rvert$, and its vector part is $\pm\mathbf w/2$, since $\mathrm{Vect}(q_rq_i^{\natural})=-(q_{r0}\mathbf v-q_{i0}\mathbf u+\mathbf u\times\mathbf v)$. Since the vector part of a real quaternion has modulus at most that of the quaternion, $\lvert\mathbf w\rvert/2=\lvert\mathrm{Vect}(q_rq_i^{\natural})\rvert\leq\lvert q_rq_i^{\natural}\rvert=\lvert q_r\rvert\lvert q_i\rvert\leq\tfrac12(\lvert q_r\rvert^{2}+\lvert q_i\rvert^{2})=s/2$, the last being the arithmetic–geometric inequality. So $\lvert\mathbf w\rvert\leq s$.

**Theorem (the square map is onto the cone).** For every $\tilde a=\alpha e_0+i\mathbf w$ in $\mathcal{C}$ there is a $\tilde X$ with $\tilde X\star\tilde X=\tilde a$. Hence the image of the square map is exactly $\mathcal{C}$.

*Proof.* Choose $q_r,q_i$ **pure** ($q_{r0}=q_{i0}=0$), so the scalar and vector equations become $\lvert q_r\rvert^{2}+\lvert q_i\rvert^{2}=\alpha$ and $2\,\mathbf u\times\mathbf v=\mathbf w$. Take the perpendicular vectors $\mathbf u,\mathbf v$ with $\lvert\mathbf u\rvert^{2}=p_+$, $\lvert\mathbf v\rvert^{2}=p_-$ and $\lvert\mathbf u\rvert\lvert\mathbf v\rvert=\lvert\mathbf w\rvert/2$, where

$$
p_{\pm}=\frac{\alpha\pm\sqrt{\alpha^{2}-\lvert\mathbf w\rvert^{2}}}{2},
$$

which is real and non-negative exactly because $\alpha\geq\lvert\mathbf w\rvert$; then $\lvert\mathbf u\rvert^{2}+\lvert\mathbf v\rvert^{2}=\alpha$ and $\lvert\mathbf u\times\mathbf v\rvert=\lvert\mathbf w\rvert/2$. Choosing the plane of $\mathbf u$ and $\mathbf v$ and the ordered pair so that $\mathbf u\times\mathbf v=\mathbf w/2$, the element $\tilde X=q_r+iq_i$ solves the two equations. The image is $\mathcal{C}$ by the two theorems.

**Remark (the boundary is the square of the zero divisors).** The inequality $\lvert\mathbf w\rvert\leq s$ is an equality exactly when $\lvert q_r\rvert=\lvert q_i\rvert$ and $q_r\perp q_i$ as real quaternions; then $\tilde Q$ is a zero divisor unless it is the origin, because $c(\tilde Q)=\lvert q_r\rvert^{2}-\lvert q_i\rvert^{2}+2i\langle q_r,q_i\rangle$ vanishes under these two conditions. The boundary $\{\alpha=\lvert\mathbf w\rvert\}$ of the cone is therefore the set of the squares of the zero divisors, its vertex $\tilde a=0$ alone excepted, which is the image of the origin; and the witness $\tilde X=e_1+ie_2$ has $\tilde X\star\tilde X=2e_0+2ie_3$, that is $\alpha=2$ and $\mathbf w=2\hat e_3$, on the boundary with $\alpha=\lvert\mathbf w\rvert=2$. The interior $\{\alpha>\lvert\mathbf w\rvert\}$ is the set of the squares of the regular elements, and its image is the interior of the cone.

## The Roots of a Central Value

**Corollary (the central reduction).** For $\lambda\in\mathbb{C}$ the equation $\tilde X\star\tilde X=\lambda e_0$ has a solution exactly when $\lambda\geq0$ is real; then the root set is the family $\{e^{i\theta}w:\theta\in\mathbb{R},\ w\in\mathbb{H}\ \text{real},\ \lvert w\rvert=\sqrt{\lambda}\}$, of real dimension four, and for $\lambda=0$ the only solution is $\tilde X=0$.

*Proof.* The cone membership of $\lambda e_0$ is $\lambda\geq\lvert\mathbf 0\rvert=0$ with $\lambda$ real; the root set is read in *Square Roots of Minus One, Zero and Plus One in the General Plain Sesqualgebra*, which computes it for $\lambda=1$ and which scales by $\sqrt{\lambda}$. The value $0$ is the single point of the cone where the theorem's $p_\pm$ coincide and the only solution is the origin.

**Remark (the three central values, recovered).** This corollary is the whole of the trichotomy of the previous article: the negative and the non-real scalars are outside the cone, the scalar $0$ has only the excluded origin, and the positive scalars have the four-parameter family of roots. The general theorem of this article is what the trichotomy specialises, and the specialisation is the cone's intersection with the central line.

## The Structure of a Root Set

**Theorem (the symmetry of the square).** The group $U(1)\times S^{3}$ acts on $\mathbb{B}$ by $\tilde X\mapsto e^{i\theta}\,\tilde X\,u$, where $\theta\in\mathbb{R}$ and $u$ is a real unit quaternion, and the square map is invariant under the action:

$$
(e^{i\theta}\tilde Xu)\star(e^{i\theta}\tilde Xu)=e^{i\theta}\tilde Xuu^{*}\tilde X^{*}e^{-i\theta}=\tilde X\tilde X^{*}=\tilde X\star\tilde X .
$$

The kernel of the action is the central subgroup $\{(0,e_0),(\pi,-e_0)\}\cong\mathbb{Z}/2$, so each orbit is of real dimension four, and the action carries the root set of every element into itself.

*Proof.* The right factor is $uu^{*}=\lvert u\rvert^{2}=1$, and the central scalars $e^{i\theta}$ commute with the coefficientwise conjugation, so the two factors cancel against their conjugates. The kernel is the solution of $e^{i\theta}u=e_0$ with $u$ real, which forces $u=e^{-i\theta}$ real, hence $e^{i\theta}=\pm1$ and $u=\pm e_0$.

**Proposition (the root set of an interior value is a single orbit).** Let $\tilde a$ be in the interior of the cone and let $\tilde X_0$ be one of its roots. Then the root set of $\tilde a$ is exactly the orbit of $\tilde X_0$ under the action,

$$
\{\tilde X:\tilde X\star\tilde X=\tilde a\}=\{e^{i\theta}\tilde X_0u:\theta\in\mathbb{R},\ u\in\mathbb{H}\ \text{real},\ \lvert u\rvert=1\},
$$

so it is a single real four-parameter family.

*Proof.* The value is interior, $\alpha>\lvert\mathbf w\rvert$, so every root is regular, by the reading of the interior as the set of the squares of the regular elements in §*The Image: the Hermitian Cone*; in particular $\tilde X_0^{-1}$ exists. For any root $\tilde X$ the quotient $\tilde Y=\tilde X_0^{-1}\tilde X$ satisfies

$$
\tilde Y\tilde Y^{*}=\tilde X_0^{-1}\tilde X\tilde X^{*}\bigl(\tilde X_0^{-1}\bigr)^{*}=\tilde X_0^{-1}\tilde X_0\tilde X_0^{*}\bigl(\tilde X_0^{*}\bigr)^{-1}=\tilde X_0^{*}\bigl(\tilde X_0^{*}\bigr)^{-1}=e_0 ,
$$

using $\tilde X\tilde X^{*}=\tilde X_0\tilde X_0^{*}=\tilde a$ and $\bigl(\tilde X_0^{-1}\bigr)^{*}=\bigl(\tilde X_0^{*}\bigr)^{-1}$; so $\tilde Y$ is a root of $+1$, and $\tilde Y=e^{i\theta}u$ by the classification of the roots of $+1$ of *Square Roots of Minus One, Zero and Plus One in the General Plain Sesqualgebra*. Hence $\tilde X=\tilde X_0\tilde Y=e^{i\theta}\tilde X_0u$ lies in the orbit of $\tilde X_0$; conversely every element of the orbit is a root, by the theorem on the symmetry of the square. The orbit is of real dimension four, the kernel of the action being $\mathbb{Z}/2$.

**Remark (the orbit and the fiber).** The map $\tilde X\mapsto\tilde X\star\tilde X$ is $U(1)\times S^{3}$-equivariant for the trivial action on the target and the action above on the source, so each fibre is a union of orbits, and over an interior value it is the single orbit of the proposition. The degenerate values are the origin ($\alpha=\lvert\mathbf w\rvert=0$), whose only root is $\tilde X=0$, and the boundary, whose roots are the zero divisors. The element $e^{i\theta}\tilde Xu$ is a **root transform**: the block's square is invariant under the right multiplication by the real unit quaternions, because the involution fixes the real subalgebra and therefore the second slot is blind to it.

## The Comparison with the Parent

| clause | general plain algebra | general plain sesqualgebra |
|---|---|---|
| square | $\tilde Q^{2}$, bilinear | $\tilde Q\star\tilde Q=\tilde Q\tilde Q^{*}$, Hermitian |
| image | the whole space except the nonzero nilpotents, the pure isotropic cone | the Hermitian cone $\{\alpha\geq\lvert\mathbf w\rvert\}$ |
| existence | for every element except the nonzero nilpotents | exactly on the cone |
| root set | two-involution arithmetic, parametrised by the square | a real four-parameter $U(1)\times S^{3}$ family on the interior |
| central value | three classes, all nonempty | only $\lambda\geq0$ |

The parent has a square root of every element except its nonzero nilpotents, and the block has one only on the cone; on the cone the block's root set is the orbit of a single root under the four-dimensional group $U(1)\times S^{3}$, and its equality with the fibre is the element-level reason the block's right multiplication is the faithful side (*The Specificities of the General Plain Sesqualgebra*).

## Summary

The square of an element of the general plain sesqualgebra is the Hermitian element $\tilde X\star\tilde X=\tilde X\tilde X^{*}$, whose scalar part $s=\lvert q_r\rvert^{2}+\lvert q_i\rvert^{2}$ and vector part $\mathbf w=2(q_{r0}\mathbf v-q_{i0}\mathbf u+\mathbf u\times\mathbf v)$ satisfy $\lvert\mathbf w\rvert\leq s$ in the real halves $\tilde X=q_r+iq_i$. The **image** of the square map is therefore contained in the **Hermitian cone** $\mathcal{C}=\{\alpha e_0+i\mathbf w:\alpha\geq\lvert\mathbf w\rvert\}$, and the containment is an equality: a square root of $\alpha e_0+i\mathbf w$ exists exactly when $\alpha\geq\lvert\mathbf w\rvert$, the boundary being the image of the zero divisors, its vertex excepted and the vertex the image of the origin, and the interior the image of the regular elements. The equation $\tilde X\star\tilde X=\tilde a$ has a solution exactly for $\tilde a\in\mathcal{C}$, and on the interior the root set is the orbit $\{e^{i\theta}\tilde X_0u\}$ of any one root under the action $\tilde X\mapsto e^{i\theta}\tilde Xu$ of $U(1)\times S^{3}$, whose kernel is $\mathbb{Z}/2$: a single real four-parameter family. The roots of a central value are the cone's intersection with the central line: only $\lambda\geq0$ real, with the four-parameter family for $\lambda>0$ and the excluded origin for $\lambda=0$, which is the trichotomy of *Square Roots of Minus One, Zero and Plus One in the General Plain Sesqualgebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ | the product of the block |
| $\tilde X=q_r+iq_i$ | the imaginary decomposition, $q_r,q_i$ real quaternions |
| $\mathbf u,\mathbf v$ | the vector parts of $q_r,q_i$ |
| $\tilde X\star\tilde X=\tilde X\tilde X^{*}$ | the square, Hermitian |
| $s=\lvert q_r\rvert^{2}+\lvert q_i\rvert^{2}$ | the scalar part of the square, definite |
| $\mathbf w=2(q_{r0}\mathbf v-q_{i0}\mathbf u+\mathbf u\times\mathbf v)$ | the vector part of the square |
| $\lvert\mathbf w\rvert\leq s$ | the domination, the cone inequality |
| $\mathcal{C}=\{\alpha e_0+i\mathbf w:\alpha\geq\lvert\mathbf w\rvert\}$ | the Hermitian cone, the image of the square |
| $p_{\pm}=\tfrac12(\alpha\pm\sqrt{\alpha^{2}-\lvert\mathbf w\rvert^{2}})$ | the modulus squares of the pure halves in the construction |
| $\tilde X\mapsto e^{i\theta}\tilde Xu$ | the $U(1)\times S^{3}$ action preserving the square |

## Further Reading

- *Introduction to the General Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-general-plain-sesqualgebra-of-biquaternions.md`), for the product, its class and the two scalar rules.
- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the relative definition of the square root.
- *Square Roots of Minus One, Zero and Plus One in the General Plain Sesqualgebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-general-plain-sesqualgebra.md`), for the reduction of the square and the three central cases.
- *Norm and Invertibility in the General Plain Sesqualgebra* (`articles_maths/norm-and-invertibility-in-the-general-plain-sesqualgebra.md`), for the square and the definiteness of its scalar part.
- *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/positivity-and-the-hermitian-cone-of-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the Hermitian cone and the positivity of the quadratic form.
- *Idempotents of the General Plain Sesqualgebra* (`articles_maths/idempotents-of-the-general-plain-sesqualgebra.md`), for the idempotents, the roots of $+1$ halved.
- *Square Roots of a General Element in the General Plain Algebra* (`articles_maths/square-roots-of-a-general-element-in-the-general-plain-algebra.md`), for the two-involution arithmetic of the parent.
