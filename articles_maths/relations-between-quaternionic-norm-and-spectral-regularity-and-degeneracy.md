# __Relations between Quaternionic Norm and Spectral Regularity and Degeneracy__

## Introduction

The biquaternion algebra carries two quadratic conditions on one element. The **quaternionic norm** $N(\tilde Q)=Q_t^2+B^2$, with $B^2=Q_x^2+Q_y^2+Q_z^2$, is multiplicative; it vanishes exactly on the non-units, and its zero locus is the **null cone** $\mathcal{N}$. The **square of the vector part** $B^2$ carries no scalar term and is not multiplicative; it vanishes exactly when the two eigenvalues of $\tilde Q$ coincide, and its zero locus is the **spectral-degenerate cone** $\mathcal S$. The first condition decides invertibility, the second decides whether the spectrum is separated. The two are studied one at a time in *Quaternionic Norm Regularity and Degeneracy in the Biquaternion Algebra* and *Spectral Regularity and Degeneracy in the Biquaternion Algebra*; this article compares them.

The comparison is organised by the pair of predicates $(N\neq0,\ B^2\neq0)$. The pair cuts $\mathbb{B}$ into four **sectors**, and the same four sectors are the four degeneration patterns of the characteristic polynomial. Each sector is treated in its own article: *The Quaternionic Norm-Regular, Spectrally Regular Sector*, *The Quaternionic Norm-Regular, Spectrally Degenerate Sector*, *The Quaternionic Norm-Degenerate, Spectrally Regular Sector* and *The Quaternionic Norm-Degenerate, Spectrally Degenerate Sector*.

**Naming.** $\mathcal N$ is the **null cone of the quaternionic norm**, qualified at first use and then the null cone. $\mathcal S$ is the **spectral-degenerate cone** and is never called a null cone, because $B^2$ is not a norm on $\mathbb{B}$. An element is **norm-regular** when $N\neq0$ and **norm-degenerate** when $N=0$; it is **spectrally regular** when $B^2\neq0$ and **spectrally degenerate** when $B^2=0$. The adjective is written in full wherever the two could collide.

**Conventions.** Throughout, $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ on the basis $e_t,\vec e_x,\vec e_y,\vec e_z$, with $\vec e_x\vec e_y=\vec e_z$, $\vec e_k^2=-e_t$ and complex coefficients. The conjugation is the $\mathbb{C}$-linear quaternion conjugation $\tilde Q^{\natural}=Q_t-\vec Q$, an anti-involution of order two fixing the centre. The vector part is $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$, and

$$
B^2=Q_x^2+Q_y^2+Q_z^2,\qquad \vec Q^2=-B^2e_t,\qquad N(\tilde Q)=\langle\tilde Q\rangle_{\natural}=\tilde Q^{\natural}\tilde Q=\tilde Q\tilde Q^{\natural}=(Q_t^2+B^2)e_t.
$$

The number $B$ is a fixed complex square root of $B^2$; the other root only exchanges the two eigenvalues. The algebra and its conventions are *The Biquaternion Algebra and Its Vector Spaces*.

## The Four Sectors

**Definition (the sectors).** For $i,j\in\{0,1\}$, let $\Sigma_{ij}$ be the set of elements with $N\neq0$ if $i=1$ and $N=0$ if $i=0$, and with $B^2\neq0$ if $j=1$ and $B^2=0$ if $j=0$. Explicitly,

$$
\Sigma_{11}=\{N\neq0,\ B^2\neq0\},\qquad
\Sigma_{01}=\{N=0,\ B^2\neq0\},\qquad
\Sigma_{10}=\{N\neq0,\ B^2=0\},\qquad
\Sigma_{00}=\{N=0,\ B^2=0\}.
$$

**Theorem (partition into four sectors).** The algebra is the disjoint union

$$
\mathbb{B}=\Sigma_{11}\sqcup\Sigma_{01}\sqcup\Sigma_{10}\sqcup\Sigma_{00}.
$$

*Proof.* Each element has exactly one truth value for each of the two predicates $N\neq0$ and $B^2\neq0$, hence lies in exactly one of the four combinations.

| sector | conditions | name |
|---|---|---|
| $\Sigma_{11}$ | $N\neq0$, $B^2\neq0$ | doubly regular |
| $\Sigma_{01}$ | $N=0$, $B^2\neq0$ | norm-degenerate, spectrally regular |
| $\Sigma_{10}$ | $N\neq0$, $B^2=0$ | norm-regular, spectrally degenerate |
| $\Sigma_{00}$ | $N=0$, $B^2=0$ | doubly degenerate |

**Remark (the origin).** The origin has $N=0$ and $B^2=0$, so it lies in $\Sigma_{00}$. Degeneracy is a value of a condition, not an extra case: an element that is degenerate for both conditions is doubly degenerate. The same reading places the punctured scalar line in $\Sigma_{10}$ and the non-zero nilpotents in $\Sigma_{00}$; neither is a sector, because a sector is fixed by the two predicates alone.

**Remark (sectors and strata).** Inside two sectors the elements split further: $\Sigma_{10}$ into the punctured scalar line $\Sigma_{10}^{\mathrm{s}}$ and the Jordan part $\Sigma_{10}^{\mathrm{J}}$, and $\Sigma_{00}$ into the origin and the non-zero nilpotents. These four subsets are **strata**, not sectors: they are separated by the minimal polynomial, not by the pair of predicates. §*The Chain of Invariants* gives the count.

## The Two Conditions in One Quadratic

**Definition (the characteristic polynomial).** For $\tilde Q=Q_te_t+\vec Q$,

$$
p_{\tilde Q}(X)=X^2-2Q_tX+N(\tilde Q)=X^2-2Q_tX+Q_t^2+B^2,
$$

of discriminant

$$
\operatorname{disc}p_{\tilde Q}=4Q_t^2-4N=-4B^2=4(Q_t^2-N).
$$

**Theorem (the spectrum reads both conditions).** Let $\lambda_\pm=Q_t\pm iB$, with $B$ a fixed square root of $B^2$. Then

$$
p_{\tilde Q}(X)=(X-\lambda_+)(X-\lambda_-),
$$

and

$$
N=\lambda_+\lambda_-,\qquad 2Q_t=\lambda_++\lambda_-,\qquad \operatorname{disc}p_{\tilde Q}=(\lambda_+-\lambda_-)^2=-4B^2.
$$

*Proof.* The product and the sum of the roots give the first two identities. The discriminant is the square of the difference of the roots, $(\lambda_+-\lambda_-)^2=(2iB)^2=-4B^2$, and $N=Q_t^2+B^2$ gives $-4B^2=4(Q_t^2-N)$.

**Corollary (two degenerations of one quadratic).** $\tilde Q\in\mathcal N$ exactly when $0$ is a root of $p_{\tilde Q}$; $\tilde Q\in\mathcal S$ exactly when $p_{\tilde Q}$ has a double root. In the coefficients, $\mathcal N$ is the vanishing of the constant term and $\mathcal S$ the vanishing of the discriminant.

**Corollary (the sectors are the spectral patterns).** The four sectors are exactly the four degeneration patterns of $p_{\tilde Q}$:

(i) $\Sigma_{11}$: two distinct non-zero roots;
(ii) $\Sigma_{01}$: two distinct roots, exactly one of them zero;
(iii) $\Sigma_{10}$: a double non-zero root;
(iv) $\Sigma_{00}$: a double root at zero.

*Proof.* The roots are $\lambda_\pm$. If $B^2\neq0$ they are distinct, and their product is $N=Q_t^2+B^2$; the product is non-zero exactly on $\Sigma_{11}$ and zero on $\Sigma_{01}$. If $B^2=0$ the roots coincide at $Q_t$, and $Q_t^2=N$; the double root is non-zero exactly on $\Sigma_{10}$ and zero on $\Sigma_{00}$.

**The two conditions side by side.**

| item | quaternionic norm | spectral condition |
|---|---|---|
| quantity | $N=Q_t^2+B^2$ | $B^2=Q_x^2+Q_y^2+Q_z^2$ |
| role in $p_{\tilde Q}$ | the constant term | the discriminant, up to $-4$ |
| spectral reading | the product $\lambda_+\lambda_-$ | the difference $\lambda_+-\lambda_-=2iB$ |
| zero locus | $\mathcal N$ | $\mathcal S$ |
| vanishing means | one eigenvalue is $0$ | the two eigenvalues coincide |
| multiplicative | yes | no |
| decides | invertibility | separation of the spectrum |

**Remark (why four).** A monic quadratic over $\mathbb{C}$ has only four degeneration patterns: two distinct roots, both non-zero; two distinct roots, one zero; a double non-zero root; a double root at zero. There is no fifth. A five-way reading, separating the punctured scalar line, the Jordan part, the origin and the non-zero nilpotents, refines $\Sigma_{10}$ and $\Sigma_{00}$ by the minimal polynomial; it does not add a sector.

## Independence of the Two Cones

**Theorem (neither cone contains the other).** $\mathcal N\not\subseteq\mathcal S$ and $\mathcal S\not\subseteq\mathcal N$.

*Proof.* Two witnesses.

- **A zero divisor with distinct eigenvalues.** Let $\tilde Q=e_t+i\vec e_x$. Then $N=1+i^2=0$, so $\tilde Q\in\mathcal N$, and $B^2=i^2=-1\neq0$, so $\tilde Q\notin\mathcal S$. Its eigenvalues are $1\pm i\cdot i$, that is $0$ and $2$; they are distinct, and the spectral decomposition exists, with the idempotents $\tilde Q/2$ and $e_t-\tilde Q/2$.
- **A unit with a repeated eigenvalue.** Let $\tilde Q=e_t+\vec e_x+i\vec e_y$. Then $B^2=1+i^2=0$, so $\tilde Q\in\mathcal S$, and $N=1+1+i^2=1\neq0$, so $\tilde Q\notin\mathcal N$. Its only eigenvalue is $1$, its minimal polynomial is $(X-1)^2$, and it is a unit with no two-term spectral decomposition.

The first is in $\Sigma_{01}$, the second in $\Sigma_{10}$.

**Theorem (the intersection is the nilpotent cone).**

$$
\mathcal N\cap\mathcal S=\{N=0,\ B^2=0\}=\{Q_t=0,\ \vec Q^2=0\}=\{\tilde Q:\tilde Q^2=0\}.
$$

It is the origin together with the non-zero pure nilpotents.

*Proof.* If $N=0$ and $B^2=0$ then $Q_t^2=N-B^2=0$, so $Q_t=0$ and $\vec Q^2=-B^2e_t=0$. Conversely, $\tilde Q^2=(Q_t^2-B^2)e_t+2Q_t\vec Q$. If $\tilde Q^2=0$ and $\vec Q\neq0$, the vector part of the square gives $2Q_t\vec Q=0$, hence $Q_t=0$, and the scalar part gives $B^2=0$. If $\vec Q=0$, the square is $Q_t^2e_t$, so $Q_t=0$.

**Remark (tangency).** The gradients in the coordinates $(Q_t,Q_x,Q_y,Q_z)$ are

$$
\nabla N=2(Q_t,Q_x,Q_y,Q_z),\qquad \nabla B^2=2(0,Q_x,Q_y,Q_z).
$$

They coincide exactly when $Q_t=0$, that is along $\Sigma_{00}$. On $\Sigma_{00}\setminus\{0\}$ they are equal and non-zero, so the two cones are tangent there; at the origin both vanish, and both cones are singular.

**Remark (multiplicativity).** The norm is multiplicative, $N(\tilde P\tilde Q)=N(\tilde P)N(\tilde Q)$, so $\mathcal N$ and its complement are stable under the product. The cone $\mathcal S$ is stable under neither the product nor the sum. Both factors of

$$
(\vec e_x+i\vec e_y)(\vec e_x-i\vec e_y)=-2e_t-2i\vec e_z
$$

have $B^2=1+i^2=0$, while the product has $B^2=(-2i)^2=-4\neq0$; and

$$
(\vec e_x+i\vec e_y)+(\vec e_x-i\vec e_y)=2\vec e_x
$$

has $B^2=4\neq0$. The cone $\mathcal S$ is a discriminant locus attached to the eigenvalue map, not a multiplicative subset.

## The Four Sectors Compared

**The algebraic data of the four sectors.**

| sector | conditions | spectrum | normal form | norm | minimal polynomial |
|---|---|---|---|---|---|
| $\Sigma_{11}$ | $N\neq0$, $B^2\neq0$ | $\{\lambda_+,\lambda_-\}$, distinct and non-zero | $\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-$, both terms non-zero | $\lambda_+\lambda_-\neq0$ | $p_{\tilde Q}$, squarefree |
| $\Sigma_{01}$ | $N=0$, $B^2\neq0$ | $\{c,0\}$, $c\neq0$ | $c\tilde\Pi$, $\tilde\Pi$ a non-trivial idempotent | $0$ | $p_{\tilde Q}$, squarefree |
| $\Sigma_{10}$ | $N\neq0$, $B^2=0$ | $\{Q_t\}$, $Q_t\neq0$ | $Q_te_t$ on $\Sigma_{10}^{\mathrm{s}}$; $Q_tu$ with $u\neq e_t$ unipotent on $\Sigma_{10}^{\mathrm{J}}$ | $Q_t^2\neq0$ | $X-Q_t$ or $(X-Q_t)^2$ |
| $\Sigma_{00}$ | $N=0$, $B^2=0$ | $\{0\}$ | $0$ or a non-zero nilpotent of index two | $0$ | $X$ or $X^2$ |

**Remark (the two mixed sectors).** $\Sigma_{01}$ and $\Sigma_{10}$ are the independence witnesses: $\Sigma_{01}$ is a zero divisor with a full eigenbasis, $\Sigma_{10}$ is a unit with none. Neither cone contains the other, and these are the sectors that show it.

**Theorem (the norm does not separate the strata).** Let $Q_t\neq0$ and let $\vec\Upsilon\neq0$ with $\vec\Upsilon^2=0$. The scalar $Q_te_t$ and the Jordan element $Q_te_t+\vec\Upsilon$ have the same norm $Q_t^2$, the same trace $2Q_t$, and therefore the same characteristic polynomial $(X-Q_t)^2$. Their minimal polynomials are $X-Q_t$ and $(X-Q_t)^2$. At the other degenerate sector the same happens: the origin and a non-zero nilpotent share the norm $0$, the trace $0$ and the characteristic polynomial $X^2$, and differ in the minimal polynomial, $X$ against $X^2$.

*Proof.* The element $\vec\Upsilon$ is pure and square-zero, so $N(Q_te_t+\vec\Upsilon)=Q_t^2$ and the trace is $2Q_t$. The scalar satisfies $\tilde Q-Q_te_t=0$; the Jordan element satisfies $(\tilde Q-Q_te_t)^2=0$ and $\tilde Q-Q_te_t\neq0$. The nilpotent case is the same computation at $Q_t=0$.

**Corollary (the norm does not see the strata).** The norm is constant on each of the two strata of $\Sigma_{10}$ and on each of the two strata of $\Sigma_{00}$. It cannot distinguish the scalar line from the Jordan part, nor the origin from the non-zero nilpotents.

## The Chain of Invariants

**Theorem (what each invariant separates).**

| invariant | data | classes |
|---|---|---|
| norm | $N$ | $2$: the unit group $\Sigma_{11}\cup\Sigma_{10}$ and the null cone $\Sigma_{01}\cup\Sigma_{00}$ |
| characteristic polynomial | $(2Q_t,N)$ | $4$: the sectors |
| minimal polynomial | $m_{\tilde Q}$ | $6$: the strata |

*Proof.* The norm separates the units from the non-units. The characteristic polynomial determines the sector by the root pattern of §*The Two Conditions in One Quadratic*, and within a sector the values of $Q_t$ and $N$ vary freely. The minimal polynomial is $p_{\tilde Q}$ on $\Sigma_{11}$ and $\Sigma_{01}$; it is $X-Q_t$ on $\Sigma_{10}^{\mathrm{s}}$, $(X-Q_t)^2$ on $\Sigma_{10}^{\mathrm{J}}$, $X$ at the origin and $X^2$ on the non-zero nilpotents.

**Corollary (the characteristic polynomial is exactly the sector).** The partition of $\mathbb{B}$ by the type of $p_{\tilde Q}$ is the partition into the four sectors, refined by the values of $Q_t$ and $N$.

**Corollary (completeness off the cone).** Off $\mathcal S$ the characteristic polynomial is a complete invariant of the similarity class. On $\mathcal S$ exactly two similarity classes share each characteristic polynomial: the scalar class and the Jordan class, or the origin and the nilpotent class at $Q_t=0$. The minimal polynomial separates them.

*Proof.* This is *Spectral Regularity and Degeneracy in the Biquaternion Algebra*, §*The Similarity Classification*. Off $\mathcal S$ the eigenvalues are distinct, so the element is diagonalisable with that spectrum. On $\mathcal S$ the scalar class is central and the Jordan class has minimal polynomial $(X-Q_t)^2$.

**Remark (the chain).** Each invariant is a function of the next: the norm is the constant term of $p_{\tilde Q}$, and $p_{\tilde Q}$ is determined by $m_{\tilde Q}$, being $m_{\tilde Q}$ when the minimal polynomial has degree two and $m_{\tilde Q}^2$ when it has degree one. Read downward, information is lost: the norm forgets the sum of the eigenvalues, the characteristic polynomial forgets the defect, the minimal polynomial forgets nothing.

## The Two Decompositions

**Definition (two-term spectral decomposition).** A **two-term spectral decomposition** of $\tilde Q$ is a writing

$$
\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-,\qquad \lambda_+\neq\lambda_-,
$$

with $\tilde\Pi_\pm$ orthogonal idempotents, $\tilde\Pi_+\tilde\Pi_-=\tilde\Pi_-\tilde\Pi_+=0$ and $\tilde\Pi_++\tilde\Pi_-=e_t$.

**Theorem (the eigenbasis follows the discriminant).**

(i) On $\Sigma_{11}\cup\Sigma_{01}$ there is a unique two-term spectral decomposition, with non-trivial idempotents $\tilde\Pi_\pm=(\tilde Q-\lambda_\mp e_t)/(\lambda_\pm-\lambda_\mp)$.
(ii) On $\Sigma_{10}^{\mathrm{s}}$ the element is scalar and the decomposition has one term.
(iii) On $\Sigma_{10}^{\mathrm{J}}$ no non-trivial idempotent commutes with $\tilde Q$, so there is no two-term decomposition.
(iv) On $\Sigma_{00}$ the same holds off the origin; at the origin every idempotent commutes and the decomposition has one term.

*Proof.* The first two statements and the last are *Spectral Regularity and Degeneracy in the Biquaternion Algebra*, §*The Spectral Decomposition* and §*The Degenerate Case: The Cone and Its Three Regimes*. On $\Sigma_{10}^{\mathrm{J}}$ the minimal polynomial is $(X-Q_t)^2$ and the centraliser is the algebra of dual numbers, whose only idempotents are $0$ and $e_t$.

**Definition (modulus–unit polar decomposition).** A **modulus–unit polar decomposition** of $\tilde Q$ is a writing $\tilde Q=\Rho\tilde U$ with $\Rho^2=N(\tilde Q)$ and $\Rho\neq0$.

**Theorem (the polar decomposition follows the norm).** It exists exactly on $\Sigma_{11}\cup\Sigma_{10}$.

*Proof.* If $N\neq0$, take $\Rho=\sqrt N$ and $\tilde U=\tilde Q/\Rho$. If $N=0$ and $\tilde Q\neq0$, no $\Rho\neq0$ has $\Rho^2=0$; at the origin the same equation forces $\Rho=0$. This is the modulus of *Modulus–Unit Polar Decomposition of Biquaternions*.

**The two decompositions in the strata.**

| stratum | spectral decomposition | polar decomposition |
|---|---|---|
| $\Sigma_{11}$ | two terms, unique | yes |
| $\Sigma_{01}$ | two terms, unique | no |
| $\Sigma_{10}^{\mathrm{s}}$ | one term | yes |
| $\Sigma_{10}^{\mathrm{J}}$ | none | yes |
| origin | one term | no |
| $\Sigma_{00}\setminus\{0\}$ | none | no |

**Corollary (the two sharpest witnesses).** $\Sigma_{01}$ is a zero divisor with an eigenbasis and no polar decomposition; $\Sigma_{10}^{\mathrm{J}}$ is a unit with a polar decomposition and no eigenbasis. The two failures are independent, and they occur in opposite mixed sectors. The comparison factor by factor is *Relations between Exponential Polar Decomposition and Eigenbasis of a Biquaternion*.

## The Two Operator Loci

**Theorem (the rank of left multiplication).** The left multiplication $L_{\tilde Q}(\tilde X)=\tilde Q\tilde X$ has complex rank $4$ on $\Sigma_{11}\cup\Sigma_{10}$, rank $2$ on $\Sigma_{01}$ and on $\Sigma_{00}\setminus\{0\}$, and rank $0$ at the origin.

*Proof.* If $N\neq0$ then $\tilde Q$ is a unit and $L_{\tilde Q}$ is invertible. If $N=0$ and $\tilde Q\neq0$, the rank is $2$ by *The Four General Products and Their Relations over the Biquaternion Algebra*, §*The Annihilators*. At the origin the map is zero.

**Definition (the sandwich).** The **sandwich** of $\tilde Q$ is the $\mathbb{C}$-linear operator

$$
\Theta_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*},
$$

where ${}^{*}$ is the Hermitian conjugate of the matrix model.

**Theorem (the sandwich is singular on the null cone).** $\Theta_{\tilde Q}$ is singular exactly on $\mathcal N$.

*Proof.* If $N=0$ and $\tilde Q\neq0$, then $\tilde Q^{\natural}\neq0$ and

$$
\Theta_{\tilde Q}(\tilde Q^{\natural})=\tilde Q\tilde Q^{\natural}\tilde Q^{*}=N\tilde Q^{*}=0.
$$

At the origin the operator is zero. Conversely, if $N\neq0$ then $\tilde Q$ is a unit and $\Theta_{\tilde Q}^{-1}=\Theta_{\tilde Q^{-1}}$.

**Definition (the inner derivation).** The **inner derivation** of $\tilde Q$ is

$$
\mathrm{ad}_{\tilde Q}(\tilde X)=\tilde Q\tilde X-\tilde X\tilde Q.
$$

**Theorem (the inner derivation is nilpotent on the spectral cone).** $\mathrm{ad}_{\tilde Q}$ is nilpotent exactly on $\mathcal S$.

*Proof.* The scalar part is central, so $\mathrm{ad}_{\tilde Q}=\mathrm{ad}_{\vec Q}$. Since $\vec Q^2=-B^2e_t$,

$$
\mathrm{ad}_{\vec Q}^{2}(\tilde X)=\vec Q^{2}\tilde X-2\vec Q\tilde X\vec Q+\tilde X\vec Q^{2}=-2B^{2}\tilde X-2\vec Q\tilde X\vec Q,
$$

and applying $\mathrm{ad}_{\vec Q}$ once more gives

$$
\mathrm{ad}_{\vec Q}^{3}(\tilde X)=-4B^{2}\,\mathrm{ad}_{\vec Q}(\tilde X).
$$

If $B^{2}=0$ then $\mathrm{ad}_{\vec Q}^{3}=0$. If $B^{2}\neq0$ then $\vec Q\neq0$, so $\mathrm{ad}_{\vec Q}\neq0$ and $\mathrm{ad}_{\vec Q}^{3}\neq0$; the space has dimension four, so a nilpotent operator would satisfy $\mathrm{ad}^{4}=0$, while $\mathrm{ad}^{4}=-4B^{2}\mathrm{ad}^{2}\neq0$. Hence the derivation is not nilpotent.

**The three operator readings in the sectors.**

| sector | rank $L_{\tilde Q}$ | $\Theta_{\tilde Q}$ | $\mathrm{ad}_{\tilde Q}$ |
|---|---|---|---|
| $\Sigma_{11}$ | $4$ | invertible | not nilpotent |
| $\Sigma_{01}$ | $2$ | singular | not nilpotent |
| $\Sigma_{10}$ | $4$ | invertible | nilpotent, zero on $\Sigma_{10}^{\mathrm{s}}$ and of index $3$ on $\Sigma_{10}^{\mathrm{J}}$ |
| $\Sigma_{00}$ | $0$ at the origin, $2$ otherwise | singular | nilpotent |

**Corollary (the two operator loci).** The sandwich is singular exactly on the null cone and the inner derivation is nilpotent exactly on the spectral-degenerate cone. The rank and the sandwich follow the norm; the derivation follows the discriminant. Neither criterion separates the strata.

## Summary

The biquaternion algebra carries two quadratic conditions. The quaternionic norm $N=Q_t^2+B^2$ is the constant term of the characteristic polynomial and the product of the eigenvalues; it is multiplicative, and it decides invertibility. The square of the vector part $B^2$ is the discriminant up to $-4$ and vanishes exactly when the two eigenvalues coincide; it is not multiplicative, and it decides whether the spectrum is separated. The null cone is the locus of an eigenvalue at zero, the spectral-degenerate cone the locus of a double eigenvalue.

The pair of predicates $(N\neq0,\ B^2\neq0)$ cuts the algebra into four sectors, and the four sectors are the four degeneration patterns of a quadratic: two distinct non-zero roots, two distinct roots with one zero, a double non-zero root, a double root at zero. The origin is doubly degenerate and belongs to $\Sigma_{00}$; it is not a fifth case. The finer reading separates the punctured scalar line from the Jordan part and the origin from the non-zero nilpotents, but that split is by the minimal polynomial, not by the two conditions.

The two cones are independent: neither contains the other, and they meet exactly on the nilpotent cone, along which they are tangent away from the origin. The null cone is a semigroup, the spectral cone is neither multiplicative nor additive.

The four sectors are compared by their spectrum, normal form, norm and minimal polynomial. The norm separates two classes, the characteristic polynomial exactly the four sectors, and the minimal polynomial the six strata. The norm is therefore the coarsest invariant: it cannot separate the scalar line from the Jordan part, nor the origin from the non-zero nilpotents. The characteristic polynomial is complete off the spectral cone and exactly two-to-one on it.

The two decompositions follow the two conditions. The eigenbasis follows the discriminant: it exists on $\Sigma_{11}\cup\Sigma_{01}$, has one term on the punctured scalar line, and fails on the Jordan part and on the non-zero nilpotents. The polar decomposition follows the norm: it exists on $\Sigma_{11}\cup\Sigma_{10}$ and fails on the null cone. The operator readings are the same pair of loci: the sandwich is singular exactly on the null cone, and the inner derivation is nilpotent exactly on the spectral-degenerate cone.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra |
| $\tilde Q=Q_te_t+\vec Q$ | a general element |
| $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ | the vector part |
| $N(\tilde Q)=Q_t^2+B^2$ | the quaternionic norm, the constant term of $p_{\tilde Q}$ and the product of the eigenvalues |
| $B^2=Q_x^2+Q_y^2+Q_z^2$ | the square of the vector part, the discriminant up to $-4$ |
| $p_{\tilde Q}(X)=X^2-2Q_tX+N$ | the characteristic polynomial |
| $\lambda_\pm=Q_t\pm iB$ | the eigenvalues |
| $\operatorname{disc}p_{\tilde Q}=-4B^2=4(Q_t^2-N)$ | the discriminant |
| $\mathcal N=\{N=0\}$ | the null cone |
| $\mathcal S=\{B^2=0\}$ | the spectral-degenerate cone |
| $\Sigma_{11},\Sigma_{01},\Sigma_{10},\Sigma_{00}$ | the four sectors of the two predicates |
| $\Sigma_{10}^{\mathrm{s}},\Sigma_{10}^{\mathrm{J}}$ | the scalar and Jordan strata of $\Sigma_{10}$ |
| $L_{\tilde Q}(\tilde X)=\tilde Q\tilde X$ | left multiplication; rank $4$ on the units, $2$ on the non-zero null elements, $0$ at the origin |
| $\Theta_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}$ | the sandwich, singular exactly on $\mathcal N$ |
| $\mathrm{ad}_{\tilde Q}(\tilde X)=\tilde Q\tilde X-\tilde X\tilde Q$ | the inner derivation, nilpotent exactly on $\mathcal S$ |

## Further Reading

- [Quaternionic Norm Regularity and Degeneracy in the Biquaternion Algebra](quaternionic-norm-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the multiplicative norm, the null cone, its pure and non-pure strata, the unit group and the zero divisors.
- [Spectral Regularity and Degeneracy in the Biquaternion Algebra](spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the spectral criterion, the characteristic polynomial, the spectral-degenerate cone, the three regimes, the spectral decomposition and the eigenbasis.
- [The Quaternionic Norm-Regular, Spectrally Regular Sector](the-quaternionic-norm-regular-spectrally-regular-sector.html), for $\Sigma_{11}$, the complement of the union of the two cones.
- [The Quaternionic Norm-Regular, Spectrally Degenerate Sector](the-quaternionic-norm-regular-spectrally-degenerate-sector.html), for $\Sigma_{10}$, the scalar line and the Jordan part.
- [The Quaternionic Norm-Degenerate, Spectrally Regular Sector](the-quaternionic-norm-degenerate-spectrally-regular-sector.html), for $\Sigma_{01}$, the scaled idempotents and the spectrum $\{c,0\}$.
- [The Quaternionic Norm-Degenerate, Spectrally Degenerate Sector](the-quaternionic-norm-degenerate-spectrally-degenerate-sector.html), for $\Sigma_{00}$, the nilpotent cone and the origin.
- [Relations between Exponential Polar Decomposition and Eigenbasis of a Biquaternion](relations-between-exponential-polar-decomposition-and-eigenbasis-of-a-biquaternion.html), for the comparison of the two decompositions factor by factor.
- [Two-Sided Operator and the Polar Decomposition](two-sided-operator-and-the-polar-decomposition.html), for the sandwich, its spectrum and its rank on the null cone.
- [The Biquaternion Eigenvalue Decomposition](the-biquaternion-eigenvalue-decomposition.html), for the eigenvalue decomposition, the eigenprojections and the degenerate regimes.
- [Modulus–Unit Polar Decomposition of Biquaternions](modulus-unit-polar-decomposition-of-biquaternions.html), for the modulus $\Rho=\sqrt{N}$ and its failure at $N=0$.
