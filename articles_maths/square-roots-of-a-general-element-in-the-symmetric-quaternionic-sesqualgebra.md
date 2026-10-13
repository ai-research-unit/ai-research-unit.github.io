# __Square Roots of a General Element in the Symmetric Quaternionic Sesqualgebra__

## Introduction

This article solves the equation $\tilde\Xi\star\tilde\Xi=\tilde R$ in the block, the symmetric quaternionic
sesquilinear product
$\tilde\Xi\star\tilde Q=\tfrac12(\tilde\Xi^{\natural}\tilde Q^{*}+\tilde Q^{*}\tilde\Xi^{\natural})$ of
*Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions*, for an arbitrary biquaternion
$\tilde R$. It follows *Square Roots of One and the Idempotents of the Symmetric Quaternionic
Sesqualgebra* and *Square Roots of Zero and the Nilpotents of the Symmetric Quaternionic Sesqualgebra*, which
treat the two central values, and completes the element theory of the block opened
by *Zero Divisors of the Symmetric Quaternionic Sesqualgebra*.

The root is relative to a product, and the product is part of the definition: it is stated once for a
general product in *Definitions for the Study of the 12 Algebraic Structures*, §*Powers, the Square and the
Roots*. The unqualified word means the block. The block's square is not a self-map of the whole space: its
value on any element is a **real** quaternion, so the equation is solvable only for the values of the real
quaternion subspace, and there every value is attained. The article states the image of the square map, the
existence theorem with an explicit root, and the fibre over a general value.

The product is *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions*; the diagonal is
*The Non-Central Algebraic Norm and the Two Halves of the Symmetric Quaternionic Sesqualgebra*; the roots of the
two central values are *Square Roots of One and the Idempotents of the Symmetric Quaternionic Sesqualgebra* and
*Square Roots of Zero and the Nilpotents of the Symmetric Quaternionic Sesqualgebra*; the zero divisors are
*Zero Divisors of the Symmetric Quaternionic Sesqualgebra*; the real
quaternion subspace and its structure are *Introduction to the Remarkable Subspaces*; and the same equation
in the plain product is *Square Roots of a General Element in the General Plain Algebra*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$,
$e_k^2=-e_0$ and $e_1e_2=e_3$; $\tilde Q=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$ and central
scalar imaginary $i$; $\mathbf Q=\sum_kQ_ke_k$; $(\mathbf\Xi,\mathbf Q)=\sum_k\Xi_kQ_k$; ${}^{\natural}$ negates
$e_1,e_2,e_3$ and fixes the coefficients, $\bar{\cdot}$ conjugates the coefficients, and
${}^{*}={}^{\natural}\circ\bar{\cdot}$; and the **real quaternion subspace** is
$\mathbb{H}_{\mathbb{B}}=\mathbb{R}e_0+\mathbb{R}e_1+\mathbb{R}e_2+\mathbb{R}e_3$, the set of the elements
with real coefficients. The diagonal is
$\tilde Q\star\tilde Q=K(\tilde Q,\tilde Q)e_0-Q_0\overline{\mathbf Q}-\overline{Q_0}\mathbf Q$ with
$K(\tilde Q,\tilde Q)=|Q_0|^2-\sum_k|Q_k|^2$. Throughout this article the product is the block and
$\varphi(\tilde\Xi)=\tilde\Xi\star\tilde\Xi$ is its square map.

**The results.** The square map $\varphi(\tilde\Xi)=\tilde\Xi\star\tilde\Xi$ lands in the real quaternion subspace $\mathbb{H}_{\mathbb{B}}$ and fills it, so $\tilde\Xi\star\tilde\Xi=\tilde R$ is solvable exactly for a real quaternion $\tilde R$. An explicit root of $\tilde R=\rho e_0+\mathbf r$ is $\tilde\Xi=\sqrt t\,e_0-\tfrac{1}{2\sqrt t}\mathbf r$ with $t=\tfrac{\rho+\sqrt{\rho^2+\lVert\mathbf r\rVert^2}}{2}$. Over a central value the roots are the pure family, present for $\lambda\leq0$, together with the non-pure family $\mathcal R_\lambda$; over a value with non-vanishing vector part the fibre is a parametrised family, a real manifold of dimension four. A value with a non-real coefficient has no root.

## Definition

**Definition (square root of an element in a product).** Let $\star$ be a product on $\mathbb{B}$ and let
$\tilde R\in\mathbb{B}$. A **square root of $\tilde R$ in $\star$** is an element $\tilde\Xi$ with

$$
\tilde\Xi\star\tilde\Xi=\tilde R .
$$

The set of the square roots of $\tilde R$ is its **fibre** $\varphi^{-1}(\tilde R)$ over $\tilde R$.

This is *Definitions for the Study of the 12 Algebraic Structures*, §*Powers, the Square and the Roots*.
Unqualified, the product is the block and the square map is $\varphi$. The central values
$\tilde R=\lambda e_0$ are the subject of *Square Roots of One and the Idempotents of the Symmetric
Quaternionic Sesqualgebra* and *Square Roots of Zero and the Nilpotents of the Symmetric Quaternionic
Sesqualgebra* and of the §*The Roots of a Complex Scalar* below.

## The Image of the Square Map

**The square of every element is a real quaternion, with real scalar part $K(\tilde\Xi,\tilde\Xi)$ and real vector part $-2\,\mathrm{Re}(\Xi_0\overline{\mathbf\Xi})$, so the equation $\tilde\Xi\star\tilde\Xi=\tilde R$ has a solution only if $\tilde R$ is a real quaternion.**

**Theorem (the square is a real quaternion).** For every $\tilde\Xi$ the element $\tilde\Xi\star\tilde\Xi$ is a
real quaternion: its scalar part is the real number $K(\tilde\Xi,\tilde\Xi)$ and its vector part is the real
vector $-2\,\mathrm{Re}(\Xi_0\overline{\mathbf\Xi})$.

*Proof.* The diagonal formula of *The Non-Central Algebraic Norm and the Two Halves of the Symmetric Quaternionic
Sesqualgebra* gives $\tilde\Xi\star\tilde\Xi=K(\tilde\Xi,\tilde\Xi)e_0-\Xi_0\overline{\mathbf\Xi}-\overline{\Xi_0}\mathbf\Xi$;
the scalar part is $K=|\Xi_0|^2-\lVert\mathbf\Xi\rVert^2$, real, and the vector part is
$-\Xi_0\overline{\mathbf\Xi}-\overline{\Xi_0}\mathbf\Xi=-2\mathrm{Re}(\Xi_0\overline{\mathbf\Xi})$, real in each
component.

**Corollary (the necessary condition).** The equation $\tilde\Xi\star\tilde\Xi=\tilde R$ has a solution only if
$\tilde R$ is a real quaternion.

*Proof.* The left side is a real quaternion for every $\tilde\Xi$ by the theorem, so a value with a non-real
coefficient is not attained.

## Existence

**The image of the square map is exactly the real quaternion subspace $\mathbb{H}_{\mathbb{B}}$; an explicit root of $\tilde R=\rho e_0+\mathbf r$ is $\tilde\Xi=\sqrt t\,e_0-\tfrac{1}{2\sqrt t}\mathbf r$ with $t=\tfrac{\rho+\sqrt{\rho^2+\lVert\mathbf r\rVert^2}}{2}$, and every real quaternion has a root.**

**Theorem (the image is the real quaternion subspace).** Every real quaternion has a square root in the
block, and the image of the square map is exactly $\mathbb{H}_{\mathbb{B}}$. An explicit root of
$\tilde R=\rho e_0+\mathbf r$ with $\rho\in\mathbb{R}$ and $\mathbf r\in\mathbb{R}^3$ is

$$
\tilde\Xi=\sqrt t\,e_0-\frac{1}{2\sqrt t}\,\mathbf r ,
\qquad
t=\frac{\rho+\sqrt{\rho^2+\lVert\mathbf r\rVert^2}}{2},
$$

when $\tilde R\neq0$, and $\tilde\Xi=0$ when $\tilde R=0$.

*Proof.* Let $\tilde\Xi=p_0e_0+\mathbf v$ be a **real** quaternion, $p_0\in\mathbb{R}$ and
$\mathbf v\in\mathbb{R}^3$. For such an element ${}^{\natural}$ and $\bar{\cdot}$ agree, and the product
reads $\tilde\Xi\star\tilde\Xi=K(\tilde\Xi,\tilde\Xi)e_0-2p_0\mathbf v$ with
$K=p_0^2-\lVert\mathbf v\rVert^2$. Matching the two sides of $\tilde\Xi\star\tilde\Xi=\rho e_0+\mathbf r$
gives $\rho=p_0^2-\lVert\mathbf v\rVert^2$ and $\mathbf r=-2p_0\mathbf v$. If $\mathbf r\neq0$ then
$p_0\neq0$ and $\mathbf v=-\mathbf r/(2p_0)$; substituting into the scalar equation gives
$4p_0^4-4\rho p_0^2-\lVert\mathbf r\rVert^2=0$, a quadratic in $p_0^2$ whose positive solution is
$t=p_0^2=(\rho+\sqrt{\rho^2+\lVert\mathbf r\rVert^2})/2$, always positive because
$\sqrt{\rho^2+\lVert\mathbf r\rVert^2}\geq|\rho|$. If $\mathbf r=0$ and $\rho>0$ the root is
$\tilde\Xi=\sqrt\rho\,e_0$; if $\mathbf r=0$ and $\rho<0$ the scalar equation $p_0^2=\rho$ has no real
solution and the real root is instead the pure vector $\tilde\Xi=\sqrt{-\rho}\,\mathbf u$ over any real unit
vector $\mathbf u$; if $\rho=0$ and $\mathbf r=0$ the root is $\tilde\Xi=0$. So every real quaternion is
attained. The corollary of §*The Image of the Square Map* gives the converse.

**Remark (no root in the other directions).** The proof uses a real root, but the argument also shows that
a real quaternion with a non-vanishing vector part has no pure solution and, as the next section shows, a
whole family of non-real ones. The existence is a statement about the value and not about the root.

## The Roots of a Complex Scalar

**Over a central value $\lambda$ the roots are the pure family, present only for $\lambda\leq0$, together with the non-pure family $\mathcal R_\lambda=\{\alpha e_0+\tfrac{i\alpha}{|\alpha|^2}\mathbf c:\alpha\in\mathbb{C}^{\times},\ \lVert\mathbf c\rVert^2=|\alpha|^2(|\alpha|^2-\lambda)\}$ over the punctured $\alpha$-plane.**

For a central value the fibre is the root set computed in *Square Roots of One and the Idempotents of the
Symmetric Quaternionic Sesqualgebra* and *Square Roots of Zero and the Nilpotents of the Symmetric
Quaternionic Sesqualgebra* and, for a general real $\lambda$, it is the union of the pure
family, present only for $\lambda\leq0$, and the non-pure family

$$
\mathcal R_\lambda=
\Bigl\{
\alpha e_0+\frac{i\alpha}{|\alpha|^2}\mathbf c:
\alpha\in\mathbb{C}^{\times},\ \mathbf c\in\mathbb{R}^3,\
\lVert\mathbf c\rVert^2=|\alpha|^2\bigl(|\alpha|^2-\lambda\bigr)
\Bigr\},
$$

the parameter $\alpha$ running over the punctured plane and the parameter $\mathbf c$ over a sphere in
$\mathbb{R}^3$. For $\lambda=-1$ the pure family is the unit sphere of $\mathbb{C}^3$; for $\lambda=+1$ it
is absent and the non-pure family requires $|\alpha|\geq1$; for $\lambda=0$ the non-pure family is the
nilpotent cone and the pure family reduces to the origin.

## The Fibres over a General Value

**Over a real quaternion $\tilde R=\rho e_0+\mathbf r$ with $\mathbf r=\mathbf 0$ the roots are the pure vectors with $\lVert\mathbf\Xi\rVert^2=-\rho$, present when $\rho\leq0$, together with the non-pure family $\mathcal R_\rho$; when $\mathbf r\neq\mathbf 0$ every root has non-vanishing scalar part and the fibre is a parametrised family, a real manifold of dimension four.**

**Theorem (the fibre).** Let $\tilde R=\rho e_0+\mathbf r$ be a real quaternion with
$\rho\in\mathbb{R}$ and $\mathbf r\in\mathbb{R}^3$.

1. If $\mathbf r=\mathbf 0$: the roots are the pure vectors $\mathbf\Xi\in\mathbb{C}^3$ with
   $\lVert\mathbf\Xi\rVert^2=-\rho$, present when $\rho\leq0$, together with the non-pure family
   $\mathcal R_\rho$.
2. If $\mathbf r\neq\mathbf 0$: every root has $\Xi_0=\alpha\neq0$, and the roots are

$$
\tilde\Xi=\alpha e_0+\sum_{k=1}^{3}\Bigl(-\frac{r_k\alpha}{2|\alpha|^2}+i\alpha t_k\Bigr)e_k ,
\qquad
\alpha\in\mathbb{C}^{\times},\quad
\mathbf t\in\mathbb{R}^3,\quad
\lVert\mathbf t\rVert^2=\frac{|\alpha|^2-\rho}{|\alpha|^2}-\frac{\lVert\mathbf r\rVert^2}{4|\alpha|^4}\geq0 .
$$

*Proof.* Let $\tilde\Xi=\alpha e_0+\mathbf x$, with $\mathbf x=\mathbf\Xi$. The vector equation of
$\tilde\Xi\star\tilde\Xi=\rho e_0+\mathbf r$ is $-\Xi_0\overline{\mathbf\Xi}-\overline{\Xi_0}\mathbf\Xi=\mathbf r$,
which componentwise reads $2\mathrm{Re}(\alpha\overline{x_k})=-r_k$. For a fixed $k$ the solutions form the
real line $\{-\dfrac{r_k\alpha}{2|\alpha|^2}+i\alpha t_k:t_k\in\mathbb{R}\}$ when $\alpha\neq0$: the
particular value satisfies the equation and the direction $i\alpha$ does not change the real part. The
scalar equation is $\lVert\mathbf x\rVert^2=|\alpha|^2-\rho$, and substituting the line gives
$\lVert\mathbf t\rVert^2=\dfrac{|\alpha|^2-\rho}{|\alpha|^2}-\dfrac{\lVert\mathbf r\rVert^2}{4|\alpha|^4}$.
If $\alpha=0$ the vector equation forces $\mathbf r=\mathbf 0$, so there is no pure root when
$\mathbf r\neq\mathbf 0$; the case $\mathbf r=\mathbf 0$ reduces to the two families of §*The Roots of a
Complex Scalar*.

**Corollary (the dimension of the fibre).** Over a value $\rho e_0$ with $\rho>0$ and over a value with
non-vanishing vector part the fibre is a real manifold of dimension four, a sphere bundle over the
admissible annulus of the punctured $\alpha$-plane; over a value $\rho e_0$ with $\rho\leq0$ the pure
family adds a real five-dimensional piece, and $\rho=0$ adds only the origin.

*Proof.* The parameter $\alpha$ runs over the punctured plane, of real dimension two, and for each admissible
$\alpha$ the parameter $\mathbf t$ runs over a sphere in $\mathbb{R}^3$, of real dimension two when the
radius is positive. The congruence $\lVert\mathbf t\rVert^2\geq0$ cuts out the annulus
$\bigl(|\alpha|^2-\rho\bigr)|\alpha|^2\geq\tfrac14\lVert\mathbf r\rVert^2$ in the $\alpha$-plane, of real
dimension two; the pure piece is the sphere of dimension five.

The fibre is empty for no real quaternion, by §*Existence*.

## Worked Examples

**A root of $e_1$.** $\tilde R=e_1$ has $\rho=0$, $\mathbf r=e_1$; the explicit real root is
$\tilde\Xi=\tfrac{1}{\sqrt2}e_0-\tfrac{1}{\sqrt2}e_1$, and one checks
$\tilde\Xi\star\tilde\Xi=e_1$. This is a root of a pure non-zero value, which the general construction
produces in the real quaternion subspace.

**A root of $e_0$.** $\tilde R=e_0$: the real root is $\tilde\Xi=e_0$, and the whole non-pure family
$\mathcal R_{+1}$ plus the pure family of the previous article are the roots.

**A root of a general real quaternion.** $\tilde R=2e_0+e_1$: $\rho=2$, $\lVert\mathbf r\rVert^2=1$,
$t=(2+\sqrt5)/2$, and $\tilde\Xi=\sqrt t\,e_0-\tfrac{1}{2\sqrt t}e_1$ satisfies
$\tilde\Xi\star\tilde\Xi=2e_0+e_1$.

**A non-solvable value.** $\tilde R=ie_0$ has a non-real scalar coefficient, so $\tilde\Xi\star\tilde\Xi=ie_0$
has no solution: the square map never leaves $\mathbb{H}_{\mathbb{B}}$.

## Summary

The square map of the block lands in the real quaternion subspace and fills it: $\tilde\Xi\star\tilde\Xi$ has
real scalar part $K(\tilde\Xi,\tilde\Xi)$ and real vector part $-2\mathrm{Re}(\Xi_0\overline{\mathbf\Xi})$, the
equation $\tilde\Xi\star\tilde\Xi=\tilde R$ is solvable exactly for a real quaternion $\tilde R$, and the
explicit real root of $\tilde R=\rho e_0+\mathbf r$ is
$\sqrt t\,e_0-\mathbf r/(2\sqrt t)$ with $t=(\rho+\sqrt{\rho^2+\lVert\mathbf r\rVert^2})/2$. Over a central
value the roots are the union of a pure family, present for $\lambda\leq0$, and the non-pure family
$\mathcal R_\lambda$; over a general real quaternion the roots are the parametrised family
$\alpha e_0+\sum(-\tfrac{r_k\alpha}{2|\alpha|^2}+i\alpha t_k)e_k$ with $\mathbf t$ on a sphere, a real
manifold of dimension four. A value with a non-real coefficient has no root.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\varphi(\tilde\Xi)=\tilde\Xi\star\tilde\Xi$ | the square map of the block |
| $\mathbb{H}_{\mathbb{B}}=\mathbb{R}e_0+\mathbb{R}e_1+\mathbb{R}e_2+\mathbb{R}e_3$ | the image, the real quaternion subspace |
| $\rho e_0+\mathbf r,\ \rho\in\mathbb{R},\ \mathbf r\in\mathbb{R}^3$ | a general real quaternion value |
| $\sqrt t\,e_0-\mathbf r/(2\sqrt t),\ t=\tfrac{\rho+\sqrt{\rho^2+\lVert\mathbf r\rVert^2}}{2}$ | the explicit real root |
| $\mathcal R_\lambda$ | the non-pure roots of the central value $\lambda$ |
| $\alpha e_0+\sum(-\tfrac{r_k\alpha}{2|\alpha|^2}+i\alpha t_k)e_k$ | the roots of a value with non-vanishing vector part |
| $K(\tilde\Xi,\tilde\Xi)=|\Xi_0|^2-\lVert\mathbf\Xi\rVert^2$ | the scalar part of the square |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), §*Powers, the Square and the Roots*, for the definitions of the square and of a root relative to a general product.
- *Square Roots of One and the Idempotents of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-symmetric-quaternionic-sesqualgebra.md`), for the central value $+1$, the roots of $-1$ and the idempotents, with the families $\mathcal R_\lambda$.
- *Square Roots of Zero and the Nilpotents of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-symmetric-quaternionic-sesqualgebra.md`), for the central value $0$ and the nilpotents, with the families $\mathcal R_\lambda$.
- *Square Roots of a General Element in the General Plain Algebra* (`articles_maths/square-roots-of-a-general-element-in-the-general-plain-algebra.md`), for the same equation in the plain product, where the image is the whole space.
- *The Non-Central Algebraic Norm and the Two Halves of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/the-non-central-algebraic-norm-and-the-two-halves-of-the-symmetric-quaternionic-sesqualgebra.md`), for the diagonal formula that gives the image.
- *Introduction to the Remarkable Subspaces* (`articles_maths/introduction-to-the-remarkable-subspaces.md`), for the real quaternion subspace among the remarkable subspaces.
- *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-sesqualgebra-of-biquaternions.md`), for the product and its table.
