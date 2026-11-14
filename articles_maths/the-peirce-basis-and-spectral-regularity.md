# __The Peirce Basis and Spectral Regularity__

## Introduction

In the Peirce basis the spectral data of an element are the elementary invariants of its coefficient matrix. The trace is the sum of the two diagonal coefficients, the determinant is the norm, and the characteristic polynomial is the characteristic polynomial of a $2\times2$ matrix. The predicate on the spectrum — whether the two eigenvalues separate — therefore reads

$$
(a-d)^{2}+4bc\neq0 ,
$$

with the three coefficients taken in the four corners.

The article proves the formulas, identifies the degenerate locus as a quadric cone with three strata, and computes what the basis does to the spectrum. Two statements organise the whole: the idempotents $e$ and $f$ are the spectral projections of the square root of the unit $J$, so the Peirce basis is the eigenbasis of $J$; and an element is diagonal in the Peirce basis exactly when it commutes with $J$. The spectral predicate is not a statement about $J$, and that is why the basis records it without resolving it.

The construction of the basis is *Introduction to the Peirce Basis over C*, and the other predicate in the same coordinates is *The Peirce Basis and Norm Regularity*. Nothing below is a statement of physics.

## Conventions

The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ on the units $e_t,\vec e_x,\vec e_y,\vec e_z$ with $e_t^{2}=e_t$, $\vec e_k^{2}=-e_t$, $\vec e_x\vec e_y=\vec e_z$, and complex coefficients. An element is $\tilde Q=Q_te_t+\vec Q$ with $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$.

The **characteristic polynomial** is

$$
p_{\tilde Q}(X)=X^{2}-2Q_tX+N(\tilde Q),\qquad N(\tilde Q)=Q_t^{2}+B^{2},\qquad B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2},
$$

with roots $\lambda_{\pm}=Q_t\pm iB$ for a fixed square root $B$ of $B^{2}$ and discriminant $-4B^{2}$. An element is **spectrally regular** when $B^{2}\neq0$ and **spectrally degenerate** when $B^{2}=0$; the zero locus is the **spectral-degenerate cone** $\mathcal S$. The **trace** is $\operatorname{Sc}(2\tilde Q)=2Q_t$.

At a unit real axis $\vec u$ let $J=i\vec u\cdot\vec e$, $e=\tfrac12(e_t+J)$, $f=\tfrac12(e_t-J)$, and at $\vec u=\vec e_z$ let $\nu=\tfrac12(i\vec e_x+\vec e_y)$, $\nu'=\tfrac12(i\vec e_x-\vec e_y)$. The Peirce coordinates of $\tilde Q$ are $a,b,c,d$ in $\tilde Q=ae+b\nu+c\nu'+df$.

## The Three Invariants in Peirce Coordinates

**Theorem (trace, determinant and characteristic polynomial).** For $\tilde Q=ae+b\nu+c\nu'+df$,

$$
\operatorname{tr}\tilde Q=a+d,\qquad N(\tilde Q)=ad-bc,\qquad p_{\tilde Q}(X)=X^{2}-(a+d)X+(ad-bc).
$$

*Proof.* The trace and the determinant are those of the coefficient matrix $\begin{pmatrix}a&c\\b&d\end{pmatrix}$, since the Peirce basis is the matrix-unit basis and the trace and the determinant are invariant under the identification. The characteristic polynomial of a $2\times2$ matrix is $X^{2}-\operatorname{tr}X+\det$. Independently, $2Q_t=a+d$ from the coordinates of $e$ and $f$, and $N=ad-bc$ by the Peirce formula.

**Corollary (the discriminant).**

$$
\operatorname{disc}p_{\tilde Q}=(a+d)^{2}-4(ad-bc)=(a-d)^{2}+4bc=-4B^{2}.
$$

**Corollary (the predicate in Peirce coordinates).**

$$
\tilde Q\ \text{is spectrally degenerate}\iff (a-d)^{2}+4bc=0 .
$$

**Theorem (the square of the vector part).** For $\tilde Q=ae+b\nu+c\nu'+df$,

$$
B^{2}=-bc-\tfrac14(a-d)^{2}=\det\tilde Q-\tfrac14\bigl(\operatorname{tr}\tilde Q\bigr)^{2}.
$$

*Proof.* Substitute $Q_x=\tfrac i2(b+c)$, $Q_y=\tfrac12(b-c)$, $Q_z=\tfrac i2(a-d)$ in $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$. Then

$$
B^{2}=-\tfrac14(b+c)^{2}+\tfrac14(b-c)^{2}-\tfrac14(a-d)^{2}=-bc-\tfrac14(a-d)^{2}.
$$

For the second form, $ad-bc-\tfrac14(a+d)^{2}=-bc-\tfrac14(a-d)^{2}$.

**Remark (the shape of the predicate).** The predicate involves the difference $a-d$ and the product $bc$, and not the sum $a+d$ which is the trace. So the spectrum's separation is independent of the trace, and the trace is independent of it. This is the $2\times2$ statement that the discriminant is not a function of the trace.

## The Basis Is the Eigenbasis of the Square Root of the Unit

**Theorem (the idempotents are the spectral projections of $J$).**

$$
Je=e,\qquad Jf=-f .
$$

*Proof.* $J=e-f$ by the definition of the pair, and $e^{2}=e$, $f^{2}=f$, $ef=0$, so $Je=(e-f)e=e$ and $Jf=(e-f)f=-f$.

**Corollary (the Peirce basis diagonalises $J$).** In the Peirce basis the matrix of $J$ is $\operatorname{diag}(1,0,0,-1)$ acting on the coordinates, that is $J=e-f$ written in the four corners.

**Theorem (the diagonal elements are the centraliser of $J$).** An element $\tilde Q$ is diagonal in the Peirce basis exactly when $bc=0$ and $ac=bd=0$, that is exactly when $b=c=0$; and this holds exactly when $\tilde Q$ commutes with $J$. The subspace is

$$
\mathbb{C}e\oplus\mathbb{C}f=\mathbb{C}e_t\oplus\mathbb{C}J,
$$

of complex dimension $2$.

*Proof.* By the multiplication table, $e$ and $f$ generate the two-dimensional span of $e_t$ and $J$, and every element of that span commutes with $J$ because $J$ is a combination of $e$ and $f$. Conversely an element commuting with $J$ lies in the centraliser of a matrix with two distinct eigenvalues, which is the span of $e_t$ and $J$. In Peirce coordinates $[J,\tilde Q]=2(c\,\nu'-b\,\nu)$, so commuting is $b=c=0$.

**Corollary (the spectrum of a diagonal element).** If $\tilde Q=ae+df$ then

$$
\operatorname{spec}\tilde Q=\{a,d\},\qquad m_{\tilde Q}(X)=(X-a)(X-d),
$$

and the element is spectrally degenerate exactly when $a=d$.

**Theorem (the basis elements fall two and two).** The diagonal corners $e$ and $f$ are spectrally regular, with spectrum $\{0,1\}$ and minimal polynomial $X(X-1)$. The mixed corners $\nu$ and $\nu'$ are spectrally degenerate, with spectrum $\{0,0\}$ and minimal polynomial $X^{2}$.

*Proof.* For $e$ the coordinates are $a=1$, $b=c=d=0$, so $(a-d)^{2}+4bc=1\neq0$ and the spectrum is $\{1,0\}$ by the corollary above. For $\nu$ the coordinates are $b=1$, $a=c=d=0$, so $(a-d)^{2}+4bc=0$ and $p=X^{2}$, while $\nu^{2}=0$ gives $m=X^{2}$. The other two are the same computations with the sign of the mixed corner changed.

**Remark (what the split records).** The diagonal corners carry the identity of their summand and the mixed corners carry the nilpotent. The spectral predicate separates them, and it separates them in the same way on each summand.

## The Predicate on a Summand

**Theorem (the predicate on a summand).** On $S_{+}$ the coordinates satisfy $c=d=0$, so

$$
B^{2}=-\tfrac14a^{2},\qquad \operatorname{spec}(ae+b\nu)=\{0,a\},
$$

and the element is spectrally degenerate exactly when $a=0$, that is exactly on the nilpotent line $\mathbb{C}\nu$. On $S_{-}$ the coordinates satisfy $a=b=0$, so $B^{2}=-\tfrac14d^{2}$, the spectrum is $\{0,d\}$, and the degenerate locus is the nilpotent line $\mathbb{C}\nu'$.

*Proof.* Substitute in the formula for $B^{2}$ and in the characteristic polynomial, which becomes $X(X-a)$ on $S_{+}$ and $X(X-d)$ on $S_{-}$.

**Corollary (each summand is a regular plane with a nilpotent line in it).** Inside a summand the degenerate locus is a complex line, of complex codimension one; the complement is the regular part, and it is connected.

**Corollary (the diagonal corner of a summand is regular, the mixed corner is not).** $e$ and $f$ lie in the regular part of their summands, and $\nu$ and $\nu'$ lie on the degenerate lines.

## The Degenerate Locus of the Algebra

**Theorem (a quadric cone).** The spectral-degenerate locus is

$$
\mathcal S=\{\tilde Q:(a-d)^{2}+4bc=0\},
$$

a quadric cone with vertex $0$, of complex dimension $3$ and real dimension $6$.

**Theorem (three strata).** The punctured cone splits into three subsets, distinguished by the minimal polynomial:

| stratum | condition in Peirce coordinates | minimal polynomial | example |
|---|---|---|---|
| scalar | $b=c=0$, $a=d$ | $X-a$, degree one | $e_t$, $e+f$ |
| nilpotent | $\operatorname{tr}=0$, rank one | $X^{2}$, degree two | $\nu$, $\nu'$ |
| rank one with non-zero trace | $a+d\neq0$, rank one | $X(X-\lambda)$, degree two | $e$, $f$ |

*Proof.* A degenerate element has $\det=0$, so its rank is $0$ or $1$. If it is zero it is scalar. If its trace vanishes, the Cayley–Hamilton identity $X^{2}=(\operatorname{tr}X)X$ gives $X^{2}=0$, and $X\neq0$ makes the minimal polynomial $X^{2}$. If its trace does not vanish, the same identity gives $X(X-\lambda)=0$ with $\lambda=\operatorname{tr}X\neq0$, the two roots are distinct, and the minimal polynomial is $X(X-\lambda)$.

**Corollary (degenerate is not the same as non-diagonalisable).** Only the nilpotent stratum has a minimal polynomial whose degree exceeds the number of distinct eigenvalues. The rank-one stratum of non-zero trace is degenerate and diagonalisable at once, and the scalar stratum is degenerate and central.

**Remark (the cone is not the nilpotent variety).** The nilpotent variety is the single stratum $\operatorname{tr}=0$ inside the cone. A summand meets the cone in one line, and that line is nilpotent; the rest of the cone lies in neither summand, and consists of the rank-one elements with non-zero trace together with the scalar line.

## The Spectrum in Coordinates

**Theorem (the two eigenvalues).** For $\tilde Q=ae+b\nu+c\nu'+df$,

$$
\lambda_{\pm}=\frac{a+d}{2}\pm iB,\qquad B^{2}=-bc-\tfrac14(a-d)^{2}.
$$

*Proof.* The roots of $X^{2}-(a+d)X+(ad-bc)$ are $\frac{a+d}{2}\pm\frac12\sqrt{(a-d)^{2}+4bc}$, and $(a-d)^{2}+4bc=-4B^{2}$, so the square root is $2iB$.

**Corollary (the spectrum of a diagonal element).** If $b=c=0$ then $B^{2}=-\tfrac14(a-d)^{2}$, so $iB=\pm\tfrac12(a-d)$ and $\lambda_{\pm}=\tfrac{a+d}{2}\pm\tfrac{a-d}{2}$, that is $a$ and $d$.

**Corollary (the eigenbasis degenerates exactly on the cone).** The two eigenvalues coincide exactly when $B=0$, that is on $\mathcal S$; off the cone the element has two distinct eigenvalues and a two-dimensional eigenbasis.

**Remark (the spectrum does not determine the basis).** The two eigenvalues are two complex numbers, eight real parameters; the element is four complex numbers, also eight. The eigenvalues do not determine the element, since the four coefficients enter the pair $\{a+d,(a-d)^{2}+4bc\}$ through two combinations. The missing data are the two eigenprojectors, and the Peirce basis is not the eigenbasis except on the centraliser of $J$.

## The Two Predicates in the Same Coordinates

**Theorem (the two conditions in the four corners).**

$$
N=ad-bc,\qquad B^{2}=-bc-\tfrac14(a-d)^{2},
$$

and the four sectors are

| sector | conditions |
|---|---|
| $\Sigma_{11}$ | $ad\neq bc$ and $(a-d)^{2}+4bc\neq0$ |
| $\Sigma_{10}$ | $ad\neq bc$ and $(a-d)^{2}+4bc=0$ |
| $\Sigma_{01}$ | $ad=bc$ and $(a-d)^{2}+4bc\neq0$ |
| $\Sigma_{00}$ | $ad=bc$ and $(a-d)^{2}+4bc=0$ |

**Theorem (the summands and the sectors).** On $S_{+}$, $N=0$ and $B^{2}=-\tfrac14a^{2}$, so $S_{+}\setminus\mathbb{C}\nu\subseteq\Sigma_{01}$ and $\mathbb{C}\nu\subseteq\Sigma_{00}$. On $S_{-}$ the same with $d$ and $\nu'$. The scalar line $\mathbb{C}e_t$ lies in $\Sigma_{10}$ away from the origin.

**Remark (the carrier meets all four sectors).** The pair, being the whole algebra, meets every sector; a single summand meets two; the scalar line meets two. The Peirce basis is the coordinate system in which this is visible at once, because the two summands are two coordinate planes and the scalar line is the diagonal.

**Remark (the two walls, read in the basis).** The null cone is $\{ad=bc\}$ and the spectral cone is $\{(a-d)^{2}+4bc=0\}$. They meet in the doubly degenerate set. On a summand the null cone contains the whole plane, so the first wall is unavoidable there and the second is a line; in the pair both walls are hypersurfaces.

## Summary

In the Peirce basis the spectral data are the invariants of a $2\times2$ matrix: trace $a+d$, determinant $ad-bc$, characteristic polynomial $X^{2}-(a+d)X+(ad-bc)$, and the predicate $(a-d)^{2}+4bc\neq0$. Equivalently

$$
B^{2}=-bc-\tfrac14(a-d)^{2}=\det-\tfrac14\operatorname{tr}^{2}.
$$

The idempotents $e,f$ are the spectral projections of the square root of the unit $J$, so the Peirce basis is the eigenbasis of $J$, and the elements diagonal in it are exactly the centraliser of $J$, the two-dimensional span of $e_t$ and $J$.

Each summand is a regular plane cut by a nilpotent line: on $S_{+}$ the predicate fails only on $\mathbb{C}\nu$, and on $S_{-}$ only on $\mathbb{C}\nu'$. In the pair the degenerate locus is a quadric cone of complex dimension $3$, with three strata — scalar, nilpotent, and rank one with non-zero trace — of which only the nilpotent one has a minimal polynomial of degree two with a repeated root.

The two eigenvalues are $\tfrac{a+d}{2}\pm iB$; they separate exactly off the cone, and they do not determine the element. The eigenvalues are two data of eight, and the eigenbasis is a third object which the Peirce basis supplies only on the centraliser of $J$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $a,b,c,d$ | the Peirce coordinates of $\tilde Q=ae+b\nu+c\nu'+df$ |
| $p_{\tilde Q}(X)$ | the characteristic polynomial $X^{2}-(a+d)X+(ad-bc)$ |
| $m_{\tilde Q}(X)$ | the minimal polynomial |
| $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$ | the square of the vector part, $-bc-\tfrac14(a-d)^{2}$ |
| $\lambda_{\pm}$ | the two eigenvalues $\tfrac{a+d}{2}\pm iB$ |
| $\mathcal S=\{(a-d)^{2}+4bc=0\}$ | the spectral-degenerate cone |
| $J=i\vec u\cdot\vec e$ | the square root of the unit at the axis, $J=e-f$ |
| $S_{\pm}$ | the left summands $\mathbb{B}e$ and $\mathbb{B}f$ |
| $\Sigma_{ij}$ | the sector with the $N$ predicate $i$ and the $B^{2}$ predicate $j$ |

## Further Reading

- [Introduction to the Peirce Basis over C](the-peirce-basis-over-c.html), for the construction, the corner rules and the multiplication table.
- [The Peirce Basis and Norm Regularity](the-peirce-basis-and-norm-regularity.html), for the other predicate in the same coordinates.
- [The Spectrum](the-spectrum.html), for the eigenvalues, the discriminant and the characteristic polynomial.
- [Relations between the N Norm and Spectral Regularity and Degeneracy](relations-between-the-n-norm-and-spectral-regularity-and-degeneracy.html), for the four sectors.
- [The N-Regular, Spectrally Regular Sector](the-n-regular-spectrally-regular-sector.html), for the doubly regular set.
- [The N-Degenerate, Spectrally Degenerate Sector](the-n-degenerate-spectrally-degenerate-sector.html), for the nilpotent stratum.
- [The Companion Nilpotents of the Biquaternion Algebra](the-companion-nilpotents-of-the-biquaternion-algebra.html), for the two mixed corners and their minimal polynomials.
