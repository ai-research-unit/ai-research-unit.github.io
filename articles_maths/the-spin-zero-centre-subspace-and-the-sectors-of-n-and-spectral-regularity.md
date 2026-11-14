# __The Spin-Zero Centre Subspace and the Sectors of N and Spectral Regularity__

## Introduction

The spin-zero carrier is the real line $\mathbb{R}e_t$, and its closure is the centre $\mathbb{C}e_t$. This article places the centre in the four
sectors cut by the two predicates $N\neq0$ and $B^{2}\neq0$.

The answer is short. The square of the vector part vanishes at every point of the centre, so one of the two predicates is constant there and the four
sectors collapse to two. Every nonzero element of the centre is norm-regular and spectrally degenerate, and the origin is the only element that is
degenerate for both. The centre therefore meets $\Sigma_{10}$ and $\Sigma_{00}$, and neither of the other two sectors.

The article states two refinements of that list. The centre meets $\Sigma_{10}$ in exactly the scalar stratum of that sector, so no element of the
centre is a Jordan element and no element of the centre has a minimal polynomial of degree two. And the centre is the carrier on which the two
conditions are as far apart as they can be, because the difference of the conditions is the square of the scalar part, and on a central element the
scalar part is the whole element.

The predicates, the sectors and the strata are defined in *Relations between the N Norm and Spectral Regularity and Degeneracy*, and the definitions
are repeated below so that the article stands alone. The subspace itself is *Introduction to the Spin-Zero Centre Subspace*. The two predicates taken
one at a time are *The Spin-Zero Centre Subspace and N Norm Regularity* and *The Spin-Zero Centre Subspace and Spectral Regularity*, and this article
is the two of them read together and against the sectors.

Nothing below is a statement of physics. The elements are written $X,Y$. The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ on the
basis $e_t,\vec e_x,\vec e_y,\vec e_z$, with $e_t$ the identity, $\vec e_k^{2}=-e_t$ and $\vec e_x\vec e_y=\vec e_z$, with complex coefficients.
The element $i$ commutes with the units and satisfies $i^{2}=-e_t$. A general element is $\tilde Q=Q_te_t+\vec Q$ with $Q_\mu=q_\mu+iq'_\mu$ complex
and $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$. The star is the Hermitian conjugation and $G$ is the group of unitary elements, $G=\mathrm{U}(2)=\{u:uu^{*}=e_t\}$.

## The Two Predicates and the Four Sectors

**Definition (the norm and the square of the vector part).** For $\tilde Q=Q_te_t+\vec Q$,

$$
N(\tilde Q)=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2},\qquad B^{2}(\tilde Q)=Q_x^{2}+Q_y^{2}+Q_z^{2}.
$$

Both are complex-valued quadratic forms on $\mathbb{B}$, of real dimension eight over $\mathbb{R}$ and four over $\mathbb{C}$.

**Theorem (the two conditions differ by the scalar square).**

$$
N(\tilde Q)-B^{2}(\tilde Q)=Q_t^{2}.
$$

*Proof.* Subtract the second display of the definition from the first; the three vector squares cancel.

**Definition (the two predicates).** An element is **norm-regular** when $N(\tilde Q)\neq0$ and **spectrally regular** when $B^{2}(\tilde Q)\neq0$.
The zero loci are the **null cone** $\mathcal N=\{N=0\}$ and the **spectral-degenerate cone** $\mathcal S=\{B^{2}=0\}$.

**Definition (the four sectors).** For $i,j\in\{0,1\}$ the sector $\Sigma_{ij}$ is the set of elements with $N\neq0$ if $i=1$ and $N=0$ if $i=0$,
and with $B^{2}\neq0$ if $j=1$ and $B^{2}=0$ if $j=0$. The four sectors partition $\mathbb{B}$.

| sector | conditions | name |
|---|---|---|
| $\Sigma_{11}$ | $N\neq0$, $B^{2}\neq0$ | doubly regular |
| $\Sigma_{10}$ | $N\neq0$, $B^{2}=0$ | norm-regular, spectrally degenerate |
| $\Sigma_{01}$ | $N=0$, $B^{2}\neq0$ | norm-degenerate, spectrally regular |
| $\Sigma_{00}$ | $N=0$, $B^{2}=0$ | doubly degenerate |

**Definition (the strata of $\Sigma_{10}$).** The sector $\Sigma_{10}$ splits into the **scalar stratum**
$\Sigma_{10}^{\mathrm{s}}=\{Q_te_t:Q_t\in\mathbb{C}^{\times}\}$ and the **Jordan stratum**
$\Sigma_{10}^{\mathrm{J}}=\{Q_t(e_t+\vec\Upsilon):Q_t\in\mathbb{C}^{\times},\ \vec\Upsilon\neq0,\ \vec\Upsilon^{2}=0\}$. The two strata are
separated by the minimal polynomial, which is $X-Q_t$ on the first and $(X-Q_t)^{2}$ on the second.

## The Centre and the Two Predicates

**Definition (the centre).** The centre is

$$
\mathbb{B}_C=\mathbb{C}e_t=\{\lambda e_t:\lambda\in\mathbb{C}\},
$$

of real dimension $2$ and complex dimension $1$. Its real part is the fixed line $\mathbb{R}e_t$ of real dimension $1$, the carrier of spin $0$.

**Theorem (the norm is the square of the coordinate).** For complex $\lambda$,

$$
N(\lambda e_t)=\lambda^{2}.
$$

In particular $N$ vanishes on the centre at $\lambda=0$ and nowhere else.

*Proof.* The coordinates are $Q_t=\lambda$ and $Q_x=Q_y=Q_z=0$, so the norm is $Q_t^{2}$.

**Theorem (the vector part vanishes identically).** For complex $\lambda$,

$$
B^{2}(\lambda e_t)=0 .
$$

*Proof.* The three vector coordinates of a central element vanish, so their squares sum to zero.

**Corollary (the centre lies in the degenerate cone).** $\mathbb{C}e_t\subseteq\mathcal S$, and $\mathbb{C}e_t\cap\mathcal N=\{0\}$.

**Lemma (one vanishing predicate collapses the partition).** Let $W$ be a subset of $\mathbb{B}$ on which $B^{2}$ vanishes. Then
$W\subseteq\Sigma_{10}\cup\Sigma_{00}$, and $W$ meets neither $\Sigma_{11}$ nor $\Sigma_{01}$. Likewise, if $N$ vanishes on $W$ then
$W\subseteq\Sigma_{01}\cup\Sigma_{00}$.

*Proof.* The second index of the sector is decided by $B^{2}$, and it is $0$ at every point of $W$; the first index is then free, which leaves the
two sectors named. The second statement is the same argument on the first index.

The lemma is what makes the count of this article two rather than four, and the same lemma organises the two companion articles: the spin-half plane
lies in $\mathcal N$, so it meets $\Sigma_{01}$ and $\Sigma_{00}$ only, and the vector part lies in neither cone, so it meets $\Sigma_{11}$ and
$\Sigma_{00}$ only.

## The Four Intersections

Each sector is intersected with the centre in turn. The four results are stated before the table, and two of them are empties.

### The Sector $\Sigma_{11}$

**Theorem.** $\mathbb{C}e_t\cap\Sigma_{11}=\varnothing$.

*Proof.* An element of $\Sigma_{11}$ has $B^{2}\neq0$, and $B^{2}$ vanishes at every point of the centre by the theorem above.

**Remark.** The sector of the doubly regular elements is the generic sector of the algebra: it is open, dense and of real dimension eight. The centre
avoids it entirely, and it avoids it at the identity too, since $e_t$ is central. A reader who expects the identity of the algebra to be a generic
element is answered here: $e_t$ has a double eigenvalue and lies in $\Sigma_{10}$.

### The Sector $\Sigma_{10}$

**Theorem.** $\mathbb{C}e_t\cap\Sigma_{10}=\mathbb{C}^{\times}e_t$.

*Proof.* On the centre $B^{2}=0$, so the second predicate holds everywhere and the sector is decided by the first. The condition is
$N(\lambda e_t)=\lambda^{2}\neq0$, which holds exactly for $\lambda\neq0$.

**Corollary (the intersection is the whole centre minus one point).** The centre is the disjoint union

$$
\mathbb{C}e_t=\bigl(\mathbb{C}^{\times}e_t\bigr)\sqcup\{0\},
$$

with the punctured line in $\Sigma_{10}$ and the origin in $\Sigma_{00}$.

**Remark (a subgroup inside one sector).** The punctured centre is closed under multiplication and under inversion, and its inverse is
$\lambda^{-1}e_t$, so it is a subgroup of the group of invertible elements. Every element of it lies in $\Sigma_{10}$, and this is the only carrier on which the
elements of one sector form a group. The sector $\Sigma_{10}$ is not a group, since it also contains the Jordan stratum and the product of two Jordan
elements need not stay in it; the centre is the part of it that is.

### The Sector $\Sigma_{01}$

**Theorem.** $\mathbb{C}e_t\cap\Sigma_{01}=\varnothing$.

*Proof.* The sector requires $N=0$ and $B^{2}\neq0$. On the centre $N=\lambda^{2}$ forces $\lambda=0$, and there $B^{2}=0$ as well, so no point of
the centre has the two values the sector asks for.

**Remark (why the emptiness is structural).** The two predicates are two conditions, and on the centre one of them is identically true, so only one
condition remains. A sector defined by the simultaneous holding of both can therefore be empty, and here it is empty because the surviving condition
and the failed one cannot hold together.

### The Sector $\Sigma_{00}$

**Theorem.** $\mathbb{C}e_t\cap\Sigma_{00}=\{0\}$.

*Proof.* The sector requires $N=0$, that is $\lambda=0$, and the point $\lambda=0$ has $B^{2}=0$.

**Corollary (the origin is the only point of contact).** The origin is the single element at which the centre meets $\Sigma_{00}$, and it is a limit
point of the punctured line, so the two cells of the centre are a line minus a point and the point itself.

**Remark (the origin in every closure).** The origin lies in the closure of each of the four sectors, since each sector is defined by the
non-vanishing of a polynomial and the origin is a zero of both. Its presence in $\Sigma_{00}$ is therefore compatible with its being a limit point of
the three others, and it is the only element of the centre of which that can be said.

**The intersections in one table.**

| sector | condition on $\lambda$ | intersection | dimension over $\mathbb{R}$ |
|---|---|---|---|
| $\Sigma_{11}$ | none, $B^{2}\neq0$ impossible | $\varnothing$ | — |
| $\Sigma_{10}$ | $\lambda\neq0$ | $\mathbb{C}^{\times}e_t$ | $2$ |
| $\Sigma_{01}$ | $N=0$ and $B^{2}\neq0$ impossible | $\varnothing$ | — |
| $\Sigma_{00}$ | $\lambda=0$ | $\{0\}$ | $0$ |

## The Intersection with the Scalar Stratum

**Theorem (the centre is the scalar stratum).** The two sets coincide:

$$
\mathbb{C}e_t\cap\Sigma_{10}=\Sigma_{10}^{\mathrm{s}} .
$$

*Proof.* The scalar stratum is $\{Q_te_t:Q_t\in\mathbb{C}^{\times}\}$ by definition, and that is the punctured centre, which is the intersection by
the theorem of the previous section.

**Corollary (no Jordan element in the centre).** The centre meets $\Sigma_{10}^{\mathrm{J}}$ in no point, so no element of the centre has a
nilpotent part, a minimal polynomial of degree two, or a nontrivial unipotent factor.

**Remark (the centre is the vertex of the cone).** The degenerate cone $\mathcal S$ is singular exactly along the scalar line, and the centre is that
line. The intersection of the centre with $\Sigma_{10}$ is therefore the singular locus of the cone with the origin removed, and the sector of a
central element is read off the cone it sits in.

**Remark (why the stratum, not just the sector).** The sector $\Sigma_{10}$ is of real dimension six and has two strata; the centre occupies one of
them completely and is the smallest subspace that does. A statement that the centre lies in $\Sigma_{10}$ would leave open whether a central element
can be defective, and it cannot. The stratum is the precise location.

## The Difference of the Two Conditions

**The identity at the centre.** At a central element the identity $N-B^{2}=Q_t^{2}$ reads

$$
N-B^{2}=\lambda^{2}=N ,
$$

because $B^{2}=0$. The two conditions are therefore as far apart as the algebra allows: one of them is the whole norm and the other is identically
zero, and the difference between them is the larger of the two.

**The same identity at the other carriers.** The formula is one formula, and the three carriers read it three ways.

| carrier | $Q_t$ | $N$ | $B^{2}$ | $N-B^{2}$ |
|---|---|---|---|---|
| centre $\mathbb{C}e_t$ | $\lambda$ | $\lambda^{2}$ | $0$ | $\lambda^{2}$ |
| plane $\mathbb{C}\tilde\Pi_+$ | $\lambda/2$ | $0$ | $-\lambda^{2}/4$ | $\lambda^{2}/4$ |
| vector part $\mathfrak{k}$ | $0$ | $\lvert\vec v\rvert^{2}$ | $\lvert\vec v\rvert^{2}$ | $0$ |

**Corollary (the difference measures the distance of the two predicates).** On the centre the two predicates share no common factor, in the sense
that one is a square and the other is zero; on the plane they are opposite in sign, $N=0$ against $B^{2}=-\lambda^{2}/4$; on the vector part they
coincide, $N=B^{2}$. The scalar part is the whole of the measure, and the centre is the case in which it is largest.

## The Sector Is a Property of the Orbit

**Theorem (scaling preserves the sector).** For complex $c\neq0$ and every element $X$,

$$
N(cX)=c^{2}N(X),\qquad B^{2}(cX)=c^{2}B^{2}(X).
$$

*Proof.* Both forms are homogeneous of degree two in the four coordinates, and $c$ multiplies each coordinate.

**Corollary.** Multiplication by a nonzero complex scalar preserves each of the four sectors. Each sector is a cone with its apex removed, except
$\Sigma_{00}$, which contains the apex.

**Theorem (conjugation preserves both predicates).** For a unitary element $u$, one with $uu^{*}=e_t$, and every element $X$,

$$
N(uXu^{*})=N(X),\qquad B^{2}(uXu^{*})=B^{2}(X).
$$

*Proof.* The norm is multiplicative, so $N(uXu^{*})=N(u)N(X)N(u^{*})=N(X)$, since $N(u)N(u^{*})=N(e_t)=1$. The scalar part is half the trace in the
matrix model and the trace is invariant under conjugation, so $Q_t$ is preserved; then $B^{2}=N-Q_t^{2}$ is preserved as well.

**Corollary (the sector belongs to the orbit).** The conjugation by unitary elements preserves the sector of every element, so the sector is a
function of the orbit and not of the representative. On the centre the orbit is a single point, since every unitary element fixes every central element; the sector of a central
element is therefore a property of the element alone, and no representative can be chosen to change it.

## The Centre Against the Other Two Carriers

**The three carriers in the four sectors.**

| carrier | sectors met | the part in $\Sigma_{11}$ | in $\Sigma_{10}$ | the part in $\Sigma_{01}$ | in $\Sigma_{00}$ |
|---|---|---|---|---|---|
| centre $\mathbb{C}e_t$ | two | $\varnothing$ | $\mathbb{C}^{\times}e_t$ | $\varnothing$ | $\{0\}$ |
| plane $\mathbb{C}\tilde\Pi_+$ | two | $\varnothing$ | $\varnothing$ | $\mathbb{C}^{\times}\tilde\Pi_+$ | $\{0\}$ |
| vector part $\mathfrak{k}$ | two | $\mathfrak{k}\setminus\{0\}$ | $\varnothing$ | $\varnothing$ | $\{0\}$ |

**Remark (the pattern of the three).** Each carrier meets exactly two sectors. The three regular sectors receive one carrier each, so no two carriers
share a regular sector, and the only sector the three share is $\Sigma_{00}$, where they share a single point. The three carriers are therefore a
partition of the three regular sectors, up to their common origin.

**Remark (why the centre is the degenerate one).** The centre is the only carrier that sits inside a cone: it lies in $\mathcal S$ entirely, whereas
the plane lies in $\mathcal N$ entirely and the vector part lies in neither. The two cones are the two ways a carrier can lose a predicate, and the
centre loses the spectral one at every point, the identity included.

## Summary

The centre $\mathbb{C}e_t$ is the closure of the spin-zero carrier $\mathbb{R}e_t$. On it the norm is $N(\lambda e_t)=\lambda^{2}$ and the square of the
vector part vanishes identically, so the four sectors collapse to two: the punctured line $\mathbb{C}^{\times}e_t$ lies in $\Sigma_{10}$ and the
origin lies in $\Sigma_{00}$, and the sectors $\Sigma_{11}$ and $\Sigma_{01}$ are met by no element of the centre. Every nonzero central element is
therefore norm-regular and spectrally degenerate, and it is invertible; the origin is the only doubly degenerate element.

The intersection with $\Sigma_{10}$ is exactly the scalar stratum of that sector, so no element of the centre is a Jordan element and the minimal
polynomial of a central element is always of degree one. The punctured centre is a subgroup of the group of invertible elements contained in a single sector, which no
other carrier supplies.

The difference of the two conditions is the square of the scalar part, and at the centre it equals the whole norm, so the centre is the carrier on
which the two predicates are farthest apart. Both predicates are invariant under scaling by a nonzero complex scalar and under conjugation by a
unitary element, so the sector belongs to the orbit; on the centre the orbit is a point.

Against the other two carriers the centre occupies $\Sigma_{10}$, the plane occupies $\Sigma_{01}$, the vector part occupies $\Sigma_{11}$, and the
three meet only in the origin of $\Sigma_{00}$.

## The Boxed Summary

| the point | in plain words |
| --- | --- |
| the plan | A sector records two answers at once: whether the norm is nonzero, and whether the square of the vector part is nonzero. |
| the carrier | The centre is a copy of the complex numbers inside the algebra, and the only central element with a vanishing coordinate is zero. |
| the first answer | The norm is nonzero everywhere on it except at the origin. |
| the second answer | The square of the vector part is never nonzero, because a central element has no vector part. |
| the sectors met | The centre without its origin lies in the sector that is norm-regular and spectrally degenerate. The origin lies in the doubly degenerate sector. |
| the sectors not met | No central element is doubly regular, and none is norm-degenerate and spectrally regular. |
| the scalar stratum | The intersection just described is exactly the scalar stratum of its sector, so a central element is never a Jordan element. |
| what is peculiar here | The punctured centre is a subgroup of the invertible elements lying inside a single sector, which no other carrier supplies. |
| how far apart the questions are | On the centre the difference between the two conditions equals the whole norm, so the two questions are as far apart as they can be. |
| why the answer is stable | Both conditions survive scaling by a nonzero complex number and conjugation by an invertible element, so the sector belongs to the orbit. On the centre an orbit is a single point. |
| the three carriers side by side | The centre occupies the norm-regular spectrally degenerate sector, the spin-half plane the norm-degenerate spectrally regular one, and the vector part the doubly regular one. The three meet only at the origin, which is doubly degenerate. |

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra, real dimension $8$ |
| $\tilde Q=Q_te_t+\vec Q$ | a general element, with $Q_\mu$ complex |
| $N(\tilde Q)=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}$ | the norm, the first predicate |
| $B^{2}(\tilde Q)=Q_x^{2}+Q_y^{2}+Q_z^{2}$ | the square of the vector part, the second predicate |
| $N-B^{2}=Q_t^{2}$ | the difference of the two conditions |
| $\mathcal N=\{N=0\}$ | the null cone |
| $\mathcal S=\{B^{2}=0\}$ | the spectral-degenerate cone |
| $\Sigma_{ij}$ | the sector with $N\neq0$ for $i=1$ and $B^{2}\neq0$ for $j=1$ |
| $\Sigma_{10}^{\mathrm{s}},\Sigma_{10}^{\mathrm{J}}$ | the scalar and the Jordan strata of $\Sigma_{10}$ |
| $\mathbb{C}e_t$ | the centre, the closure of the carrier, real dimension $2$ |
| $\mathbb{R}e_t$ | the carrier of spin $0$, real dimension $1$ |
| $\vec\Upsilon$ | a nonzero pure nilpotent, $\vec\Upsilon^{2}=0$ |
| $u$ | a unitary element, $uu^{*}=e_t$ |

## Further Reading

- [Introduction to the Spin-Zero Centre Subspace](the-spin-zero-centre-subspace.html), for the line, the closure and the action on it.
- [The Spin-Zero Centre Subspace and N Norm Regularity](the-spin-zero-centre-subspace-and-n-norm-regularity.html), for the norm alone, its two
real forms and the polar form.
- [The Spin-Zero Centre Subspace and Spectral Regularity](the-spin-zero-centre-subspace-and-spectral-regularity.html), for the second predicate
alone, the double eigenvalue and the degenerate cone.
- [Relations between the N Norm and Spectral Regularity and Degeneracy](relations-between-the-n-norm-and-spectral-regularity-and-degeneracy.html),
for the two predicates, the four sectors and the strata.
- [The N-Regular, Spectrally Degenerate Sector](the-n-regular-spectrally-degenerate-sector.html), for the sector that contains the punctured centre
and its scalar stratum.
- [The N-Degenerate, Spectrally Degenerate Sector](the-n-degenerate-spectrally-degenerate-sector.html), for the sector that contains the origin.
- [The Spin-Half Bispinors and the Sectors of N and Spectral Regularity](the-spin-half-bispinor-spaces-and-the-sectors-of-n-and-spectral-regularity.html),
for the same question answered on the plane, the spinor spaces and the bispinor space.
- [The Spin-One Anti-Hermitian Subspace and the Sectors of N and Spectral Regularity](the-spin-one-anti-hermitian-subspace-and-the-sectors-of-n-and-spectral-regularity.html),
for the same question answered on the vector part and on the anti-Hermitian space.
