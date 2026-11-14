# __The Carrier of Dimension 1 and Spectral Regularity__

## Introduction

The carrier of complex dimension $1$ is the centre $\mathbb{C}e_t$, and this article computes the second predicate on it: whether the spectrum of an element is separated. The answer is the extreme one. Every element of the carrier has a double eigenvalue, so the whole carrier lies in the spectral-degenerate locus, and the carrier never meets the spectrally regular part of the algebra.

Two points are worth separating from the start, because they are often confused. A double root of the characteristic polynomial is not a failure of diagonalisability: the elements of the carrier are scalar matrices, they are diagonal, and their minimal polynomial has degree one. And a spectrally degenerate element need not be central: the nilpotent $\nu$ of the dimension-two carriers also has a double root, and it is not in the carrier. The carrier is the axis of the degenerate locus, not the whole of it.

The companion article is *The Carrier of Dimension 1 and Norm Regularity*. The line itself is *Introduction to the Carrier of Dimension 1 over C*.

Nothing below is a statement of physics. The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ on the units $e_t,\vec e_x,\vec e_y,\vec e_z$ with $e_t$ the unit, $\vec e_k^{2}=-e_t$ and $\vec e_x\vec e_y=\vec e_z$, with complex coefficients. An element is $\tilde Q=Q_t+\vec Q$, and $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$.

## The Predicate

**Definition (the characteristic polynomial).** For $\tilde Q=Q_t+\vec Q$,

$$
p_{\tilde Q}(X)=X^{2}-2Q_tX+N(\tilde Q),\qquad N(\tilde Q)=Q_t^{2}+B^{2},\qquad B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}.
$$

The roots are $\lambda_{\pm}=Q_t\pm iB$ for a fixed complex square root $B$ of $B^{2}$, the discriminant is $-4B^{2}$, and $N$ is the $N$ norm.

**Definition (the predicate).** An element is **spectrally regular** when $B^{2}\neq0$, that is when $p_{\tilde Q}$ has two distinct roots, and **spectrally degenerate** when $B^{2}=0$, that is when the two roots coincide. The zero locus is the **spectral-degenerate cone** $\mathcal S=\{B^{2}=0\}$.

## The Predicate on the Carrier

**Theorem (the vector part vanishes identically).** For $\lambda e_t$,

$$
B^{2}(\lambda e_t)=0.
$$

*Proof.* The vector part of $\lambda e_t$ is $0$, so all three of $Q_x,Q_y,Q_z$ vanish.

**Corollary (the carrier is contained in the degenerate cone).** $\mathbb{C}e_t\subseteq\mathcal S$, and every element of the carrier is spectrally degenerate.

**Theorem (the characteristic polynomial and the spectrum).** For $\lambda e_t$,

$$
p_{\lambda e_t}(X)=(X-\lambda)^{2},\qquad \operatorname{disc}p_{\lambda e_t}=0,\qquad \operatorname{spec}(\lambda e_t)=\{\lambda\},
$$

with $\lambda$ of multiplicity two.

*Proof.* $Q_t=\lambda$ and $B^{2}=0$, so $p=X^{2}-2\lambda X+\lambda^{2}=(X-\lambda)^{2}$ and the two roots $Q_t\pm iB$ both equal $\lambda$.

**Corollary (the carrier never meets the regular part).** No element of the carrier is spectrally regular. In the sector notation of *Relations between the N Norm and Spectral Regularity and Degeneracy*, the carrier meets neither $\Sigma_{11}$ nor $\Sigma_{01}$.

## The Degree of the Minimal Polynomial

**Theorem (the minimal polynomial is linear).** For $\lambda e_t$,

$$
m_{\lambda e_t}(X)=X-\lambda .
$$

*Proof.* $\lambda e_t$ is the scalar $\lambda$ in the matrix model, and the annihilating polynomials of the scalar $\lambda$ are the multiples of $X-\lambda$.

**Remark (double root, diagonalisable, not a defect).** The characteristic polynomial has a double root and the minimal polynomial has degree one: the element is semisimple with one eigenvalue. In the language of Jordan forms, the matrix is $\lambda\mathrm I_2$, in Jordan form already, with two blocks of size one and no nilpotent part. Spectral degeneracy in this algebra is the coincidence of the eigenvalues, and the coincidence here costs nothing: the eigenspace is the whole plane.

**Corollary (every vector is an eigenvector).** The eigenspace of $\lambda e_t$ at $\lambda$ is $\mathbb{C}^{2}$, and every basis of the plane diagonalises it.

**Remark (the two degenerations are different).** The nilpotent $\nu=\tfrac12(i\vec e_x+\vec e_y)$ also has $B^{2}=0$, because $-1+1=0$; its characteristic polynomial is $X^{2}$, its minimal polynomial is also $X^{2}$, and it is not diagonalisable. Both elements are spectrally degenerate by the predicate, and they differ in the degree of the minimal polynomial. The predicate reads the eigenvalues and not the Jordan structure.

## The Carrier Is the Axis of the Degenerate Cone

**Theorem (the cone is a cylinder over the isotropic cone of the vector part).** The condition $B^{2}=0$ involves the vector coordinates alone, so

$$
\mathcal S=\mathbb{C}e_t\oplus\{\vec Q:B^{2}(\vec Q)=0\},
$$

and $\mathcal S$ is a cylinder whose axis is the carrier.

*Proof.* $B^{2}$ does not depend on $Q_t$; the coordinates split as $\mathbb{C}\oplus\mathbb{C}^{3}$, and the defining equation is imposed on the second factor alone.

**Corollary (the carrier is the central part of the cone).** The elements of $\mathcal S$ that are central are exactly the elements of the carrier:

$$
\{X\in\mathcal S:XY=YX\ \text{for all}\ Y\in\mathbb{B}\}=\mathbb{C}e_t .
$$

*Proof.* An element is central exactly when its vector part vanishes, since the commutant of the algebra is the centre.

**Remark (how much of the cone the carrier is).** $\mathcal S$ has complex dimension $3$ and the carrier has complex dimension $1$: the carrier is a line inside a threefold, along its axis. The elements of $\mathcal S$ outside the carrier are degenerate and not scalar, so "spectrally degenerate" is weaker than "central", and the carrier is the intersection of the two conditions.

## The Stratum of the Carrier

**Definition (strata).** Inside the sectors, elements are separated by their minimal polynomial: the scalar line and the nilpotent cone are different strata although both are spectrally degenerate.

**Theorem (the punctured carrier is one stratum).** The set $\mathbb{C}e_t\setminus\{0\}$ is a single stratum, the set of elements whose minimal polynomial has degree one and whose spectrum is the single value $\lambda\neq0$.

*Proof.* Every element of the set is a non-zero scalar, and two non-zero scalars are related by a change of scalar, so they have the same minimal-polynomial type; and no element of the set is nilpotent or non-scalar.

**Remark (the carrier as a stratum of $\Sigma_{10}$).** The sector $\Sigma_{10}$ contains the punctured scalar line and the nilpotent part; the carrier supplies the first and none of the second. The article *The N-Regular, Spectrally Degenerate Sector* uses this split.

| carrier point | $B^{2}$ | char. poly | min. poly | stratum |
|---|---|---|---|---|
| $\lambda e_t$, $\lambda\neq0$ | $0$ | $(X-\lambda)^{2}$ | $X-\lambda$ | punctured scalar line |
| $0$ | $0$ | $X^{2}$ | $X$ | origin |

## Summary

On the carrier of complex dimension $1$ the predicate is degenerate everywhere: $B^{2}=0$ identically, the characteristic polynomial is $(X-\lambda)^{2}$, the discriminant vanishes, and the spectrum is the single value $\lambda$ with multiplicity two.

The elements are nevertheless semisimple: the minimal polynomial is $X-\lambda$, of degree one, the eigenspace is the whole plane and every basis diagonalises the element. Spectral degeneracy here is the coincidence of two eigenvalues and not a Jordan defect; the nilpotent $\nu$ has the same coincidence with a minimal polynomial of degree two, and it is not in the carrier.

The carrier is the axis of the spectral-degenerate cone, which is a cylinder over the isotropic cone of the vector part; the carrier is the part of the cone whose elements are central, one complex dimension inside a threefold.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $p_{\tilde Q}(X)=X^{2}-2Q_tX+N$ | the characteristic polynomial |
| $m_{\tilde Q}(X)$ | the minimal polynomial |
| $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$ | the square of the vector part |
| $\lambda_{\pm}=Q_t\pm iB$ | the two roots |
| $\mathcal S=\{B^{2}=0\}$ | the spectral-degenerate cone |
| $\Sigma_{ij}$ | the sector with the $N$ predicate $i$ and the $B^{2}$ predicate $j$ |
| $\mathbb{C}e_t$ | the carrier of dimension $1$, the centre |
| $\nu=\tfrac12(i\vec e_x+\vec e_y)$ | the nilpotent of the dimension-two carriers |

## Further Reading

- [Introduction to the Carrier of Dimension 1 over C](the-carrier-of-dimension-1.html), for the line and its uniqueness.
- [The Carrier of Dimension 1 and Norm Regularity](the-carrier-of-dimension-1-and-norm-regularity.html), for the other predicate on the same carrier.
- [The Spectrum](the-spectrum.html), for the eigenvalues, the discriminant and the characteristic polynomial.
- [Relations between the N Norm and Spectral Regularity and Degeneracy](relations-between-the-n-norm-and-spectral-regularity-and-degeneracy.html), for the four sectors.
- [The N-Regular, Spectrally Degenerate Sector](the-n-regular-spectrally-degenerate-sector.html), for the scalar and nilpotent strata.
- [The Companion Nilpotents of the Biquaternion Algebra](the-companion-nilpotents-of-the-biquaternion-algebra.html), for the nilpotent with a double root and a minimal polynomial of degree two.
