# __The Peirce Basis and Norm Regularity__

## Introduction

In the Peirce basis the $N$ norm is not merely computable: it becomes the determinant. For an element written in the four corners,

$$
\tilde Q=ae+b\nu+c\nu'+df,
$$

the norm is

$$
N(\tilde Q)=ad-bc,
$$

which is the determinant of the $2\times2$ matrix of Peirce coordinates. Everything about the norm then follows from one sentence about determinants, and the two summands of the carrier are read off as the two coordinate planes on which the determinant vanishes identically.

The article proves the formula, draws the four consequences — multiplicativity, the polar form, the isotropic planes, the null cone as the rank-one locus — and closes with the position of the basis in the partition by the two predicates. The result is that the carrier as a whole is norm-regular almost everywhere, while each of its two summands is norm-degenerate everywhere. That contrast is the reason the basis, and not one summand, is the carrier.

The construction of the basis, the multiplication table and the corner rules are *Introduction to the Peirce Basis over C*. The other predicate on the same coordinates is *The Peirce Basis and Spectral Regularity*. Nothing below is a statement of physics.

## Conventions

The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ on the units $e_t,\vec e_x,\vec e_y,\vec e_z$ with $e_t^{2}=e_t$, $\vec e_k^{2}=-e_t$, $\vec e_x\vec e_y=\vec e_z$, and complex coefficients. An element is $\tilde Q=Q_te_t+\vec Q$ with $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$.

The **$N$ norm** is

$$
N(\tilde Q)=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}=\langle\tilde Q\rangle_{\natural},
$$

the determinant of the matrix of $\tilde Q$ in the model $\mathbb{B}\cong M_2(\mathbb{C})$, and its **polar form** is $\beta(X,Y)=\tfrac12\bigl(N(X+Y)-N(X)-N(Y)\bigr)$. An element is **norm-regular** when $N(\tilde Q)\neq0$ and **norm-degenerate** when $N(\tilde Q)=0$; the zero locus is the **null cone** $\mathcal N$. The Hermitian conjugation is $\tilde Q^{*}=\overline{\tilde Q^{\natural}}$.

At a unit real axis $\vec u$ let $J=i\vec u\cdot\vec e$, $e=\tfrac12(e_t+J)$, $f=\tfrac12(e_t-J)$, and at $\vec u=\vec e_z$ let $\nu=\tfrac12(i\vec e_x+\vec e_y)$ and $\nu'=\tfrac12(i\vec e_x-\vec e_y)$. The **Peirce basis** is $e,\nu,\nu',f$, with corners $\mathbb{B}_{ee}=\mathbb{C}e$, $\mathbb{B}_{ef}=\mathbb{C}\nu'$, $\mathbb{B}_{fe}=\mathbb{C}\nu$, $\mathbb{B}_{ff}=\mathbb{C}f$.

## The Norm on the Basis

**Theorem (the norm vanishes on every basis element).**

$$
N(e)=N(\nu)=N(\nu')=N(f)=0 .
$$

*Proof.* Read the coordinates of the four elements. For $e=\tfrac12e_t+\tfrac i2\vec e_z$ one has $Q_t=\tfrac12$, $Q_z=\tfrac i2$ and $Q_x=Q_y=0$, so $B^{2}=Q_z^{2}=-\tfrac14$ and $N=\tfrac14-\tfrac14=0$. For $f$ the sign of $Q_z$ is reversed and $B^{2}$ is unchanged. For $\nu=\tfrac i2\vec e_x+\tfrac12\vec e_y$ one has $Q_t=0$ and $B^{2}=-\tfrac14+\tfrac14=0$. For $\nu'$ the sign of $Q_y$ is reversed and $B^{2}$ is unchanged.

**Remark (why the vanishing is not the whole story).** The norm is a quadratic form, not a linear one, so its values on a basis do not determine it on sums. The four zeros above are consistent with a norm that vanishes identically, and also with a norm that is indefinite and non-degenerate. The next theorem decides which.

## The Norm Is the Determinant of the Coordinates

**Theorem (the Peirce formula).** For $\tilde Q=ae+b\nu+c\nu'+df$ with $a,b,c,d\in\mathbb{C}$,

$$
N(\tilde Q)=ad-bc .
$$

*Proof.* By the basis theorem of *Introduction to the Peirce Basis over C* the four elements are the matrix units $E_{11},E_{21},E_{12},E_{22}$, and $\tilde Q$ is the matrix $\begin{pmatrix}a&c\\b&d\end{pmatrix}$. The norm is the determinant of that matrix, hence $ad-bc$. Alternatively, read the coordinates: from $e$ and $f$ the scalar part is $Q_t=\tfrac12(a+d)$ and the third coordinate is $Q_z=\tfrac i2(a-d)$; from $\nu$ and $\nu'$ the first two coordinates are $Q_x=\tfrac i2(b+c)$ and $Q_y=\tfrac12(b-c)$. Then

$$
N=\tfrac14(a+d)^{2}-\tfrac14(b+c)^{2}+\tfrac14(b-c)^{2}-\tfrac14(a-d)^{2}=ad-bc .
$$

**Corollary (the norm is multiplicative, and this is the determinant identity).** For $X=ae+b\nu+c\nu'+df$ and $Y=a'e+b'\nu+c'\nu'+d'f$,

$$
N(XY)=N(X)N(Y),
$$

because the Peirce coordinates multiply by the matrix product $\begin{pmatrix}a&c\\b&d\end{pmatrix}\begin{pmatrix}a'&c'\\b'&d'\end{pmatrix}$.

**Corollary (the polar form).**

$$
\beta(X,Y)=\tfrac12\bigl(ad'+a'd-bc'-b'c\bigr),
$$

and in particular

$$
\beta(e,f)=\tfrac12,\qquad \beta(\nu,\nu')=-\tfrac12,\qquad \beta(e,\nu)=\beta(e,\nu')=\beta(f,\nu)=\beta(f,\nu')=0 .
$$

*Proof.* Polarise $ad-bc$. The only non-zero pairings are the two cross terms, and the substitutions give the four values.

**Corollary (the form is non-degenerate).** In the order $e,\nu,\nu',f$ the matrix of $\beta$ is

$$
\tfrac12\begin{pmatrix}0&0&0&1\\0&0&-1&0\\0&-1&0&0\\1&0&0&0\end{pmatrix},
$$

of determinant $\tfrac1{16}\neq0$.

**Remark (what the formula says).** The quaternionic norm is the determinant of the regular representation, and the Peirce basis is the basis in which the regular representation is literally the algebra of $2\times2$ matrices. The four corners are the four matrix units, and the norm is the determinant of the coefficient matrix. No other basis of this algebra has that property, because no other basis is the corner decomposition of a pair of complementary idempotents.

## The Two Summands Are Isotropic

**Definition (the summands).** $S_{+}=\mathbb{C}e\oplus\mathbb{C}\nu$ and $S_{-}=\mathbb{C}\nu'\oplus\mathbb{C}f$, the two left summands.

**Theorem (each summand is totally isotropic).** On $S_{+}$ the coordinates satisfy $c=d=0$, hence $N=0$ identically; on $S_{-}$ they satisfy $a=b=0$, hence $N=0$ identically.

*Proof.* Substitute in $N=ad-bc$.

**Corollary (no element of a summand is a unit).** Every element of $S_{+}$ and of $S_{-}$ is norm-degenerate, so neither summand meets the group of units of the algebra.

**Theorem (the summands are maximal isotropic).** $S_{+}$ and $S_{-}$ are totally isotropic planes, and no totally isotropic subspace of $\mathbb{B}$ has dimension $3$.

*Proof.* The form $\beta$ is non-degenerate, so for any subspace $W$ one has $\dim W+\dim W^{\perp}=4$. A totally isotropic $W$ satisfies $W\subseteq W^{\perp}$, hence $\dim W\leq2$. The planes above attain the bound.

**Corollary (the Witt index is two).** The norm has Witt index $2$, and the two summands are a hyperbolic pair of maximal isotropic planes.

**Corollary (the summands are not isotropic for the pair's own form).** The restriction of $N$ to $S_{+}\oplus S_{-}=\mathbb{B}$ is non-degenerate, by the determinant of the Gram matrix. The pair is therefore not a null object even though both of its members are.

**Remark (the contrast that motivates the basis).** On $S_{+}$ the norm is identically zero, so the norm distinguishes no two points of $S_{+}$ and the polar decomposition has no modulus there. On the pair the norm is non-zero on the complement of a hypersurface, so the modulus exists at almost every point. The carrier, being the pair, is the smallest object on which the norm is a usable invariant.

## The Null Cone in Peirce Coordinates

**Theorem (the null cone is the degenerate locus of the coefficient matrix).**

$$
\mathcal N=\{\tilde Q:ad=bc\}=\{\tilde Q:\operatorname{rank}\tilde Q\leq1\}.
$$

*Proof.* $N=ad-bc$ is the determinant, and a $2\times2$ matrix is singular exactly when its rank is at most one.

**Corollary (the cone is a quadric of complex dimension three).** $\mathcal N$ is defined by one quadratic equation in four coordinates, so it is a hypersurface; it is a cone with vertex $0$, homogeneous of degree two.

**Corollary (the two rulings, in coordinates).** The cone is covered by the two families of planes

$$
S_{+}(\vec u)=\{c=d=0\},\qquad S_{-}(\vec u)=\{a=b=0\},
$$

for the axis $\vec u$ of the basis, and by the two families of the right summands $T_{+}=\{b=d=0\}$ and $T_{-}=\{a=c=0\}$. Every point of $\mathcal N$ lies in one plane of each family.

*Proof.* A singular matrix has a kernel of dimension at least one, and the four planes are the four coordinate planes of the Peirce basis; a singular matrix lies in a plane of each ruling according to its kernel and its image.

**Corollary (the strata of the cone).** The complement of the origin in $\mathcal N$ splits into the four punctured coordinate planes of the two rulings, and the origin.

**Remark (the cone is not a subspace).** The sum of two null elements need not be null: $e$ and $f$ are null and $e+f=e_t$ has norm $1$. The null cone carries no linear structure beyond its vertex, and its pieces are the isotropic planes of the two rulings.

## The Group of Units

**Theorem (the units are the invertible coefficient matrices).**

$$
\mathbb{B}^{\times}=\{\tilde Q:N(\tilde Q)\neq0\}=\{\tilde Q:ad\neq bc\},
$$

a Zariski-open subset of complex dimension $4$ and real dimension $8$, isomorphic to $GL_2(\mathbb{C})$.

*Proof.* $N$ is the determinant and the determinant is non-zero exactly on the invertible matrices.

**Corollary (the inverse in Peirce coordinates).** For $\tilde Q$ a unit,

$$
\tilde Q^{-1}=(ad-bc)^{-1}\bigl(d\,e-b\,\nu-c\,\nu'+a\,f\bigr),
$$

the Peirce form of the inverse matrix $\frac{1}{ad-bc}\begin{pmatrix}d&-c\\-b&a\end{pmatrix}$.

*Proof.* Multiply and use the table. The term $d\,e$ contributes $d$ to the corner $\mathbb{B}_{ee}$, the term $a\,f$ contributes $a$ to $\mathbb{B}_{ff}$, and the two mixed terms cancel the off-diagonal entries: $-b\,\nu\cdot c\,\nu'=-bc\,f$ and $-c\,\nu'\cdot b\,\nu=-bc\,e$, so the sum is $(ad-bc)e_t$. The other product, with the factors reversed, is the same by symmetry of the corner table.

**Corollary (inversion preserves the diagonal and negates the two mixed coordinates).** In Peirce coordinates inversion sends $(a,b,c,d)$ to $(ad-bc)^{-1}(d,-b,-c,a)$. An element of $\mathbb{C}e\oplus\mathbb{C}f$ therefore inverts inside $\mathbb{C}e\oplus\mathbb{C}f$, and no element of a summand is invertible.

*Proof.* Read the formula. On the diagonal $b=c=0$ the inverse is $\frac1a e+\frac1d f$, which needs $ad\neq0$.

**Remark (the summands contain no units).** This is the sharpest form of the previous section: the group of units is the complement of the cone, and both summands lie inside the cone. A basis element is never invertible, and no product of basis elements in one summand is either.

## The Position in the Sector Partition

**Definition (the sectors).** For $i,j\in\{0,1\}$ let $\Sigma_{ij}$ be the set of elements with $N\neq0$ if $i=1$ and $N=0$ if $i=0$, and with $B^{2}\neq0$ if $j=1$ and $B^{2}=0$ if $j=0$, where $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$.

**Theorem (the basis elements lie on two sectors, two and two).** All four basis elements have $N=0$. The mixed corners have $B^{2}=0$ and lie in $\Sigma_{00}$; the diagonal corners have $B^{2}=-\tfrac14$ and lie in $\Sigma_{01}$.

*Proof.* The norm vanishes on the four elements by the first theorem of this article. For $e=\tfrac12(e_t+i\vec e_z)$ the vector part is $\tfrac i2\vec e_z$, so $B^{2}=-\tfrac14$; for $f$ the sign is reversed and $B^{2}$ is unchanged. For $\nu=\tfrac i2\vec e_x+\tfrac12\vec e_y$ the two non-zero coordinates contribute $-\tfrac14$ and $+\tfrac14$, so $B^{2}=0$, and $\nu'$ is the same with the sign of $\vec e_y$ reversed.

**Theorem (the summands lie in two sectors).** On $S_{+}\setminus\{0\}$ the element $ae+b\nu$ has $N=0$ and $B^{2}=-\tfrac{a^{2}}4$, so it lies in $\Sigma_{01}$ when $a\neq0$ and in $\Sigma_{00}$ when $a=0$. The same holds on $S_{-}$ with $d$ in place of $a$.

**Corollary (the carrier meets all four sectors).** The carrier, being the pair, meets $\Sigma_{00}$ on the two nilpotent lines $\mathbb{C}\nu$ and $\mathbb{C}\nu'$ and at the origin, $\Sigma_{01}$ on the rest of each summand, $\Sigma_{10}$ on the scalar line $\mathbb{C}e_t$ away from the origin, and $\Sigma_{11}$ on the complement of the null cone.

| locus in the carrier | $N$ | $B^{2}$ | sector |
|---|---|---|---|
| $0$, $\mathbb{C}\nu$, $\mathbb{C}\nu'$ | $0$ | $0$ | $\Sigma_{00}$ |
| $ae+b\nu$ with $a\neq0$, and the same on $S_{-}$ | $0$ | $-\tfrac{a^{2}}4\neq0$ | $\Sigma_{01}$ |
| $\lambda e_t$, $\lambda\neq0$ | $\lambda^{2}\neq0$ | $0$ | $\Sigma_{10}$ |
| general element of the pair | $\neq0$ | $\neq0$ | $\Sigma_{11}$ |

**Remark (the count of the carrier).** The pair is the only one of the three carriers that meets all four sectors. The centre meets two, the isotropic plane of a single summand meets two, and the pair meets four, because the pair is the whole algebra.

## Summary

In the Peirce basis the $N$ norm is the determinant of the coefficient matrix: for $\tilde Q=ae+b\nu+c\nu'+df$ one has $N=ad-bc$. Its values on the four basis elements are all zero, and that is not a degeneracy of the form but a consequence of the form being quadratic.

The two summands $S_{+}=\mathbb{C}e\oplus\mathbb{C}\nu$ and $S_{-}=\mathbb{C}\nu'\oplus\mathbb{C}f$ are the two coordinate planes $c=d=0$ and $a=b=0$. On each the determinant vanishes identically, so each is a maximal totally isotropic plane, the Witt index of the norm is two, and neither summand contains a unit.

The null cone is the set $ad=bc$, which is the rank-one locus of the coefficient matrix, and it is doubly ruled by the four coordinate planes of the Peirce basis. The group of units is the complement, isomorphic to $GL_2(\mathbb{C})$, and the inverse is the cofactor formula written in the four corners.

The carrier, being the pair, is norm-regular on the complement of a hypersurface and meets all four sectors of the partition by the two predicates; a single summand is norm-degenerate everywhere and meets only two.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $N(\tilde Q)=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}$ | the $N$ norm, equal to $ad-bc$ in the Peirce basis |
| $\beta$ | the polar form of $N$ |
| $\mathcal N=\{N=0\}=\{ad=bc\}$ | the null cone, the rank-one locus |
| $e,\nu,\nu',f$ | the Peirce basis, the four corners |
| $a,b,c,d$ | the Peirce coordinates of $\tilde Q=ae+b\nu+c\nu'+df$ |
| $S_{\pm}$ | the left summands $\mathbb{B}e$ and $\mathbb{B}f$ |
| $T_{\pm}$ | the right summands $e\mathbb{B}$ and $f\mathbb{B}$ |
| $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$ | the square of the vector part |
| $\Sigma_{ij}$ | the sector with the $N$ predicate $i$ and the $B^{2}$ predicate $j$ |

## Further Reading

- [Introduction to the Peirce Basis over C](the-peirce-basis-over-c.html), for the construction, the corner rules and the multiplication table.
- [The Peirce Basis and Spectral Regularity](the-peirce-basis-and-spectral-regularity.html), for the other predicate in the same coordinates.
- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the norm, its polar form and the group of units.
- [Relations between the N Norm and Spectral Regularity and Degeneracy](relations-between-the-n-norm-and-spectral-regularity-and-degeneracy.html), for the four sectors and their geometry.
- [The N-Regular Sector](the-n-regular-sector.html), for the complement of the null cone.
- [The N-Degenerate, Spectrally Regular Sector](the-n-degenerate-spectrally-regular-sector.html), for the complement of the four basis lines inside a summand.
- [The Minimal Left Ideals of the Biquaternion Algebra](the-minimal-left-ideals-of-the-biquaternion-algebra.html), for the family of isotropic planes.
