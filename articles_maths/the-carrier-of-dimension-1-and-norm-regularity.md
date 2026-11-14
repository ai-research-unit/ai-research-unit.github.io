# __The Carrier of Dimension 1 and Norm Regularity__

## Introduction

The carrier of complex dimension $1$ is the centre $\mathbb{C}e_t$, and this article computes the $N$ norm on it. The answer is short: the norm of $\lambda e_t$ is $\lambda^{2}$, so the norm is a perfect square on the line, it vanishes only at the origin, and every non-zero element of the carrier is norm-regular. Nothing in the carrier lies on the null cone except the origin itself.

That outcome is the opposite of the one for the carriers of dimension $2$, where the norm vanishes identically, and it is the reason the centre is the only carrier on which the norm is a genuine invariant of the coordinate. The article proves the formula, draws the three consequences — multiplicativity, invertibility, non-isotropy — and places the carrier inside the four sectors of *Relations between the N Norm and Spectral Regularity and Degeneracy*.

The companion article is *The Carrier of Dimension 1 and Spectral Regularity*, where the other condition is computed. The line itself is *Introduction to the Carrier of Dimension 1 over C*. The definitions of the norm and of norm-regularity are *N-Regularity and N-Degeneracy in the Biquaternion Algebra*.

Nothing below is a statement of physics. The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ on the units $e_t,\vec e_x,\vec e_y,\vec e_z$ with $e_t$ the unit, $\vec e_k^{2}=-e_t$ and $\vec e_x\vec e_y=\vec e_z$, with complex coefficients. An element is written $\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$, briefly $\tilde Q=Q_t+\vec Q$.

## The Norm and the Two Predicates

**Definition (the $N$ norm).** For $\tilde Q=Q_t+\vec Q$ put

$$
N(\tilde Q)=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}=\langle\tilde Q\rangle_{\natural},
$$

the quaternionic norm, equal to the determinant of the matrix of $\tilde Q$ in the $M_2(\mathbb{C})$ representation. It is a complex-valued quadratic form, not a positive norm.

**Definition (the predicate).** An element is **norm-regular** when $N(\tilde Q)\neq0$ and **norm-degenerate** when $N(\tilde Q)=0$. The zero locus is the **null cone** $\mathcal N=\{N=0\}$.

**Theorem (the norm is multiplicative).** For $X,Y\in\mathbb{B}$,

$$
N(XY)=N(X)N(Y).
$$

*Proof.* In the matrix model $N$ is the determinant and the determinant is multiplicative.

**Corollary (a product with a null factor is null).** If $N(Y)=0$ then $N(XY)=0$ for every $X$.

## The Norm on the Carrier

**Theorem (the formula).** For $\lambda\in\mathbb{C}$,

$$
N(\lambda e_t)=\lambda^{2}.
$$

*Proof.* In the coordinates of $\lambda e_t=Q_t+\vec Q$ one has $Q_t=\lambda$ and $\vec Q=0$, so $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}=0$ and $N=Q_t^{2}+B^{2}=\lambda^{2}$.

**Corollary (the norm-degenerate locus of the carrier is the origin).** On the carrier,

$$
\{X\in\mathbb{C}e_t:N(X)=0\}=\{0\}.
$$

*Proof.* $\lambda^{2}=0$ if and only if $\lambda=0$.

**Corollary (every non-zero element of the carrier is norm-regular).** The intersection of the carrier with the null cone is a single point, namely $0$, and it is not a null line: the carrier is a line whose generator has norm $1$.

**Remark (the contrast with the other carriers).** On a carrier of dimension $2$ the norm vanishes identically, so the whole of it is null; on the halves of dimension $4$ the norm is indefinite and the null locus is a cone. The centre is the only one of the three where the norm separates points of the carrier.

**Remark (where the square comes from).** The norm of an element of the centre is the norm of a scalar in the algebra, and the algebra is $\mathbb{C}$-central; the determinant of a scalar matrix $\lambda\mathrm I_2$ is $\lambda^{2}$. The exponent $2$ is the size of the matrix model and not a property of the carrier.

## The Polar Form on the Carrier

**Definition (the polar form).** The polar form of $N$ is the bilinear form $\beta(X,Y)=\tfrac12\bigl(N(X+Y)-N(X)-N(Y)\bigr)$, so that

$$
\beta(X,Y)=X_tY_t+X_xY_x+X_yY_y+X_zY_z
$$

in the coordinates above.

**Theorem (the restriction is non-degenerate).** On the carrier,

$$
\beta(\lambda e_t,\mu e_t)=\lambda\mu,
$$

so the form restricted to the carrier is non-degenerate, of rank $1$, and the carrier is a non-isotropic line.

*Proof.* Take $X=\lambda e_t$ and $Y=\mu e_t$: the only non-zero coordinates are the scalar ones, so $\beta=\lambda\mu$.

**Corollary (no element of the carrier is isotropic).** $\beta(X,X)=N(X)=\lambda^{2}$, which vanishes only at $X=0$. The carrier therefore contains no isotropic line for $N$.

## Multiplicativity and Inversion

**Theorem (the carrier is a subalgebra, and the norm is a character).** The carrier is closed under the product and under inversion of its non-zero elements, and on it

$$
N(XY)=N(X)N(Y),\qquad N(X^{-1})=\frac{1}{N(X)}\quad(N(X)\neq0).
$$

*Proof.* $(\lambda e_t)(\mu e_t)=\lambda\mu\,e_t$ and $(\lambda e_t)^{-1}=\lambda^{-1}e_t$ for $\lambda\neq0$; the norm statements are the theorem above applied twice, and $N(e_t)=1$.

**Corollary (invertibility on the carrier).** An element $\lambda e_t$ is a unit of the algebra if and only if it is norm-regular, and then its inverse lies in the carrier. On this carrier, and only here among the three, the two notions coincide pointwise.

**Remark (the norm is a coordinate map).** The map $\lambda\mapsto N(\lambda e_t)=\lambda^{2}$ is two-to-one away from $0$: the two values $\pm\lambda$ have the same norm. The carrier therefore inherits the sign ambiguity that the norm has on the whole algebra, and the square root of the norm is the coordinate up to sign.

## The Carrier in the Sector Partition

**Definition (the sectors).** For $i,j\in\{0,1\}$ let $\Sigma_{ij}$ be the set of elements with $N\neq0$ if $i=1$ and $N=0$ if $i=0$, and with $B^{2}\neq0$ if $j=1$ and $B^{2}=0$ if $j=0$. The algebra is the disjoint union of the four.

**Theorem (the carrier meets two sectors).** On the carrier, $B^{2}=0$ identically. Hence

$$
\mathbb{C}e_t\setminus\{0\}\subseteq\Sigma_{10},\qquad 0\in\Sigma_{00},
$$

and the carrier meets neither $\Sigma_{11}$ nor $\Sigma_{01}$.

*Proof.* The vector part of $\lambda e_t$ is zero, so $B^{2}=0$; and $N=\lambda^{2}$ is non-zero away from the origin. The element $0$ has both predicates false.

**Remark (one stratum).** The punctured carrier is a single stratum of the partition by the minimal polynomial: its elements are the non-zero scalar matrices. The article *The N-Regular, Spectrally Degenerate Sector* calls this set $\Sigma_{10}^{\mathrm{s}}$, the scalar part of the punctured line, and places the nilpotents of $\Sigma_{10}$ outside it.

| carrier point | $N$ | $B^{2}$ | sector |
|---|---|---|---|
| $\lambda e_t$, $\lambda\neq0$ | $\lambda^{2}\neq0$ | $0$ | $\Sigma_{10}$ |
| $0$ | $0$ | $0$ | $\Sigma_{00}$ |

## Summary

On the carrier of complex dimension $1$ the $N$ norm is the square of the coordinate, $N(\lambda e_t)=\lambda^{2}$. It vanishes only at the origin, so every non-zero element of the carrier is norm-regular and the intersection of the carrier with the null cone is the single point $0$.

The polar form restricts to $\beta(\lambda e_t,\mu e_t)=\lambda\mu$ and is non-degenerate: the carrier is a non-isotropic line, and it contains no isotropic direction. The carrier is a subalgebra, the norm is multiplicative on it, and invertibility coincides with norm-regularity there.

The carrier lies in the sector $\Sigma_{10}$ away from the origin and in $\Sigma_{00}$ at the origin; it never meets $\Sigma_{11}$ or $\Sigma_{01}$, because the vector part of its elements vanishes identically.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra, $M_2(\mathbb{C})$, complex dimension $4$ |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the units, $e_t^{2}=e_t$, $\vec e_k^{2}=-e_t$, $\vec e_x\vec e_y=\vec e_z$ |
| $\tilde Q=Q_t+\vec Q$ | an element with its scalar and vector parts |
| $N(\tilde Q)=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}$ | the $N$ norm, the determinant |
| $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$ | the square of the vector part |
| $\mathcal N=\{N=0\}$ | the null cone |
| $\beta$ | the polar form of $N$ |
| $\Sigma_{ij}$ | the sector with the $N$ predicate $i$ and the $B^{2}$ predicate $j$ |
| $\mathbb{C}e_t$ | the carrier of dimension $1$, the centre |

## Further Reading

- [Introduction to the Carrier of Dimension 1 over C](the-carrier-of-dimension-1.html), for the line, its uniqueness and its place among the Peirce corners.
- [The Carrier of Dimension 1 and Spectral Regularity](the-carrier-of-dimension-1-and-spectral-regularity.html), for the other predicate on the same carrier.
- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the norm and its vanishing set.
- [Relations between the N Norm and Spectral Regularity and Degeneracy](relations-between-the-n-norm-and-spectral-regularity-and-degeneracy.html), for the four sectors and their geometry.
- [The N-Regular, Spectrally Degenerate Sector](the-n-regular-spectrally-degenerate-sector.html), for the scalar stratum containing the punctured carrier.
- [The N-Degenerate, Spectrally Degenerate Sector](the-n-degenerate-spectrally-degenerate-sector.html), for the origin among the doubly degenerate elements.
- [The Biquaternion Algebra](the-biquaternion-algebra.html), for the conventions of the units and the products.
