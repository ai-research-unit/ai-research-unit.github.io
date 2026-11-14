# __The Spin-Zero Centre Subspace and Spectral Regularity__

## Introduction

The spin-zero carrier is the real line $\mathbb{R}e_t$ and its closure is the centre $\mathbb{C}e_t$. This article computes the second predicate on the closure: whether the two eigenvalues of an element are separated.

The answer is the extreme one, and it is the opposite of the answer for the spin-half carrier. Every element of the centre has a single eigenvalue of multiplicity two, so the whole centre lies in the spectral-degenerate cone and no element of it is spectrally regular. The centre is a copy of the complex field, and a copy of a field is exactly the case in which there is only one eigenvalue to have.

Two qualifications keep the result from being misread, and both are treated below. A double eigenvalue is not a defect of the element: the element satisfies a relation of degree one, so there is nothing to separate, and the multiplicity is the multiplicity of the space and not a failure. And the centre is not the whole of the degenerate cone: the cone contains noncentral elements, and the centre is the part of the cone on which the vector part vanishes.

The companion article is *The Spin-Zero Centre Subspace and N Norm Regularity*, where the first predicate is computed and the answer is the opposite: the norm separates the points of the centre and vanishes only at the origin. The subspace itself is *Introduction to the Spin-Zero Centre Subspace*. The predicates and the four sectors are defined in *Relations between the N Norm and Spectral Regularity and Degeneracy*.

Nothing below is a statement of physics. The algebra $\mathbb{B}$ is real, of dimension $8$, with units $e_t,\vec e_x,\vec e_y,\vec e_z$, $e_t$ the identity and $\vec e_k^{2}=-e_t$, and with $i$ an element commuting with the units and $i^2=-e_t$. An element is $\tilde Q=Q_te_t+\vec Q$ with $Q_\mu=q_\mu+iq'_\mu$ complex and $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$.

## The Two Eigenvalues

**The quadratic relation.** Every element of the algebra satisfies

$$
X^{2}-2Q_tX+N(X)e_t=0 .
$$

*Proof.* Write $X=Q_te_t+\vec Q$. The pure part squares to $\vec Q^{2}=-B^{2}e_t$ with $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$, since the three pure units anticommute in pairs. Then

$$
X^{2}=Q_t^{2}e_t+2Q_t\vec Q-B^{2}e_t ,
$$

and subtracting $2Q_tX=2Q_t^{2}e_t+2Q_t\vec Q$ and adding $N(X)e_t=(Q_t^{2}+B^{2})e_t$ leaves zero.

**Definition (the two eigenvalues).** The two eigenvalues of $X$ are the roots of the quadratic relation,

$$
\lambda_{\pm}=Q_t\pm iB ,
$$

with $B$ a fixed square root of $B^{2}$. The other root of $B^{2}$ only exchanges the two eigenvalues, so the pair is well defined. The **spectrum** is the set $\{\lambda_{+},\lambda_{-}\}$, and

$$
\lambda_{+}+\lambda_{-}=2Q_t,\qquad \lambda_{+}\lambda_{-}=N(X).
$$

**Definition (the predicate).** An element is **spectrally regular** when $B^{2}\neq0$, that is when the two eigenvalues are distinct, and **spectrally degenerate** when $B^{2}=0$, that is when they coincide. The zero locus is the **spectral-degenerate cone** $\mathcal S=\{B^{2}=0\}$.

**Remark (the two spectra are different objects).** The two eigenvalues of an element are computed from that element. The weights of a carrier, computed elsewhere, are the eigenvalues of the operator of the action and belong to the carrier and not to the element. The two are related but distinct, and the word *spectrum* alone will not say which is meant.

## The Predicate on the Centre

**Theorem (the vector part vanishes identically).** For every complex $\lambda$,

$$
B^{2}(\lambda e_t)=0 .
$$

*Proof.* The vector part of $\lambda e_t$ is zero, so all three of $Q_x,Q_y,Q_z$ vanish and the sum of their squares vanishes.

**Corollary (the centre lies in the degenerate cone).** $\mathbb{C}e_t\subseteq\mathcal S$, and every element of the centre is spectrally degenerate.

**Theorem (the spectrum of an element of the centre).**

$$
\lambda_{+}=\lambda_{-}=\lambda,\qquad \operatorname{spec}(\lambda e_t)=\{\lambda\},
$$

with $\lambda$ of multiplicity two.

*Proof.* The coordinates give $Q_t=\lambda$ and $B=0$, so both roots of $Q_t\pm iB$ equal $\lambda$.

**Corollary (no element of the centre is spectrally regular).** The predicate fails at every point of the closure, the origin included.

## Degenerate and Yet Not Defective

**The relation of degree one.** The quadratic relation collapses for a central element. With $B=0$ and $N=\lambda^{2}$ it reads

$$
X^{2}-2\lambda X+\lambda^{2}e_t=(X-\lambda e_t)^{2}=0 ,
$$

and the element itself satisfies the linear relation

$$
X-\lambda e_t=0 .
$$

So the element is the scalar $\lambda$ and nothing else. There is one eigenvalue because the element is one number.

**Why the multiplicity is not a failure.** The two eigenvalues coincide, and the natural question is whether the element can be separated into two independent directions. For a central element the question does not arise: the element does not mix any two directions, since it does not move anything at all. The multiplicity two is the multiplicity of the two-dimensional real space over the one-dimensional complex space, and it is the same factor of two that appears in the norm article as the two copies of the line.

**The count.** The number of distinct eigenvalues is one, and the real dimension of the centre is two, and the complex dimension is one. The identity $2s+1=\dim_{\mathbb{R}}$ is a statement about the carrier of real dimension one, where $s=0$; it is not a statement about the closure, whose dimension over $\mathbb{R}$ is two. The two counts agree in the complex dimension and not in the real one.

## The Centre Is Not the Whole Degenerate Cone

**A degenerate element outside the centre.** Let $\vec u_{\mathrm r}$ be a unit real axis and $\vec u_2,\vec u_3$ an oriented orthonormal pair completing it. The element

$$
N_{\mathrm d}=\vec u_2-i\vec u_3
$$

is not central, and it is spectrally degenerate:

$$
N_{\mathrm d}^{2}=\vec u_2^{2}-\vec u_3^{2}-i\bigl(\vec u_2\vec u_3+\vec u_3\vec u_2\bigr)=-e_t+e_t-0=0 ,
$$

because the two pure units anticommute and each squares to $-e_t$. Its vector part is nonzero and its square is zero, so it is a degenerate element that is not in the centre.

**The centre inside the cone.** The centre is exactly the part of the cone on which the vector part vanishes:

$$
\mathcal S\cap\{\vec Q=0\}=\mathbb{C}e_t .
$$

*Proof.* If the vector part vanishes the element is central and $B^{2}=0$ automatically, which gives the inclusion of the centre in the intersection. Conversely an element of the intersection is central by definition.

**Remark (how much bigger the cone is).** The cone $\mathcal S$ is not a subspace and not a cone over a sphere; it is the set where the three complex numbers $Q_x,Q_y,Q_z$ satisfy one complex equation, and it contains the centre as a thin part. The element $N_{\mathrm d}$ above is the first example, and the degenerate elements of a spinor space, treated in *The Spin-Half Bispinor Spaces and Spectral Regularity*, are the members of the cone that lie inside an ideal.

## The Centre Against the Other Carriers

| carrier | $B^{2}$ on it | spectrally degenerate locus in it |
| --- | --- | --- |
| centre $\mathbb{C}e_t$ | $0$ | the whole centre |
| spinor plane $\Sigma$ | $-\lambda^{2}/4$ | $\{0\}$ |
| vector part $\mathfrak{k}$ | $\lvert\vec v\rvert^{2}$ | $\{0\}$ |

**The two extremes again.** On the centre the second predicate fails everywhere; on the plane and on the vector part it holds everywhere except at the origin. The centre and the plane are the two extremes, and each is extreme for one predicate and not for the other.

**The sector of the centre.** With the two predicates taken together, every nonzero element of the centre is norm-regular and spectrally degenerate, so the centre away from the origin lies in the sector $\Sigma_{10}$. The plane away from the origin lies in $\Sigma_{01}$, and the vector part away from the origin in $\Sigma_{11}$. The fourth sector, $\Sigma_{00}$, is met by no carrier except at the origin, where all three meet.

## Summary

Every element of the centre is spectrally degenerate: its vector part vanishes, $B^{2}=0$, and its spectrum is the single value $\lambda$ with multiplicity two. The relation satisfied by a central element is of degree one, so the double eigenvalue is the multiplicity of the space and not a defect of the element. The centre is not the whole degenerate cone, since the element $\vec u_2-i\vec u_3$ is degenerate and noncentral; it is exactly the degenerate part on which the vector part vanishes. Away from the origin the centre lies in the sector $\Sigma_{10}$, the sector of the norm-regular and spectrally degenerate elements.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra, real, of dimension $8$ |
| $\tilde Q=Q_te_t+\vec Q$ | an element, with $Q_\mu$ complex |
| $N(\tilde Q)$ | the $N$ norm, complex-valued and multiplicative |
| $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$ | the square of the vector part |
| $\lambda_{\pm}=Q_t\pm iB$ | the two eigenvalues of an element |
| spectral-regular | $B^{2}\neq0$ |
| $\mathcal S=\{B^{2}=0\}$ | the spectral-degenerate cone |
| $\mathbb{C}e_t$ | the centre, the closure of the carrier |
| $\vec u_{\mathrm r},\vec u_2,\vec u_3$ | a unit real axis and an oriented orthonormal pair completing it |
| $\vec u_2-i\vec u_3$ | a degenerate noncentral element, of square zero |
| $\Sigma_{ij}$ | the sector with $N\neq0$ for $i=1$ and $B^{2}\neq0$ for $j=1$ |

## Further Reading

- [Introduction to the Spin-Zero Centre Subspace](the-spin-zero-centre-subspace.html), for the line, the closure and the action on it
- [The Spin-Zero Centre Subspace and N Norm Regularity](the-spin-zero-centre-subspace-and-n-norm-regularity.html), for the other predicate on the same space
- [The Carrier of Dimension 1 and Spectral Regularity](the-carrier-of-dimension-1-and-spectral-regularity.html), for the same computation in the complex reading of the algebra
- [Relations between the N Norm and Spectral Regularity and Degeneracy](relations-between-the-n-norm-and-spectral-regularity-and-degeneracy.html), for the definitions of the two predicates and the four sectors
- [The Spectrum](the-spectrum.html), for the characteristic polynomial and the two eigenvalues of an element
- [The N-Regular, Spectrally Degenerate Sector](the-n-regular-spectrally-degenerate-sector.html), for the sector in which the centre away from the origin lies
- [Centre, Units, Zero Divisors and Division Algebras](centre-units-zero-divisors-and-division-algebras.html), for the centre as a division algebra inside the algebra
- [The Carriers, the Representation, the Spin and the Closure](the-carriers-the-representation-the-spin-and-the-closure.html), for the three carriers taken together
