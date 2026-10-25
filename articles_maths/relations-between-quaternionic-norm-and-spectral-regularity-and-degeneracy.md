# __Relations between Quaternionic Norm and Spectral Regularity and Degeneracy__

## Introduction

The biquaternion algebra carries two quadratic conditions. The **quaternionic norm** $N(\tilde Q)=Q_t^2+B^2$, with $B^2=Q_x^2+Q_y^2+Q_z^2$, is multiplicative and decides invertibility; its zero locus is the **null cone** $\mathcal N$. The **square of the vector part** $B^2$ carries no scalar term, is not multiplicative, and decides whether the two eigenvalues $\lambda_\pm=Q_t\pm iB$ can be told apart; its zero locus is the **spectral-degenerate cone** $\mathcal S$. The two conditions are studied one at a time in *Quaternionic Norm Regularity and Degeneracy in the Biquaternion Algebra* and *Spectral Regularity and Degeneracy in the Biquaternion Algebra*. This article studies them together.

The relation is a relation between two conditions on the same unordered pair of eigenvalues. The norm is the product, $N=\lambda_+\lambda_-$; the spectral condition is the coincidence, $\lambda_+=\lambda_-$. The norm vanishes exactly when one eigenvalue vanishes, and the discriminant vanishes exactly when the two coincide. These are different conditions on the same pair, and neither implies the other. Both are degenerations of one quadratic, the characteristic polynomial $p_{\tilde Q}(X)=X^2-2Q_tX+N$: a zero constant term, and a vanishing discriminant.

**Naming.** $\mathcal N$ is the **null cone of the quaternionic norm**, qualified at first use and then the null cone. $\mathcal S$ is the **spectral-degenerate cone** and is never called a null cone, because $B^2$ is not a norm on $\mathbb{B}$. An element is **norm-regular** when $N\neq0$ and **norm-degenerate** when $N=0$; it is **spectrally regular** when $B^2\neq0$ and **spectrally degenerate** when $B^2=0$. The adjective is written in full wherever the two could collide, and the bare word regular is not used.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ on the basis $e_t,\vec e_x,\vec e_y,\vec e_z$, with $\vec e_x\vec e_y=\vec e_z$ and $\vec e_k^2=-e_t$, and with complex coefficients. The natural conjugation is the $\mathbb{C}$-linear quaternion conjugation $\tilde Q^{\natural}=Q_t-\vec Q$, an anti-involution of order two fixing the centre. The vector part is $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$, and

$$
B^2=Q_x^2+Q_y^2+Q_z^2,\qquad \vec Q^2=-B^2e_t,\qquad N(\tilde Q)=\langle\tilde Q\rangle_{\natural}=\tilde Q^{\natural}\tilde Q=\tilde Q\tilde Q^{\natural}=(Q_t^2+B^2)e_t.
$$

The number $B$ is a fixed complex square root of $B^2$; the other root only exchanges the two eigenvalues. The spectral article, the sector articles and this one all write $B^2$ for the square and $B$ for the root. The algebra and its conventions are *The Biquaternion Algebra and Its Vector Spaces*; the norm and its two cases are *Quaternionic Norm Regularity and Degeneracy in the Biquaternion Algebra*; the spectral criterion, the characteristic polynomial and the cone are *Spectral Regularity and Degeneracy in the Biquaternion Algebra*.

## The Characteristic Polynomial and the Two Conditions

**Definition (the two conditions).** For $\tilde Q=Q_te_t+\vec Q$,

$$
N(\tilde Q)=Q_t^2+B^2,\qquad B^2=Q_x^2+Q_y^2+Q_z^2,
$$

and the two cones are

$$
\mathcal N=\{N=0\},\qquad \mathcal S=\{B^2=0\}.
$$

**Theorem (the spectrum reads both conditions).** Let $\lambda_\pm=Q_t\pm iB$ be the eigenvalues, with $B$ a fixed square root of $B^2$. Then

$$
p_{\tilde Q}(X)=X^2-2Q_tX+N=(X-\lambda_+)(X-\lambda_-),
$$

and the two conditions are read in the coefficients and the discriminant:

$$
N=\lambda_+\lambda_-,\qquad 2Q_t=\lambda_++\lambda_-,\qquad \operatorname{disc}p_{\tilde Q}=(\lambda_+-\lambda_-)^2=-4B^2=4(Q_t^2-N).
$$

*Proof.* The product and the sum of the roots give the first two identities. The discriminant is the square of the difference of the roots, $(\lambda_+-\lambda_-)^2=-4B^2$, and $N=Q_t^2+B^2$ gives $-4B^2=4(Q_t^2-N)$.

**Corollary (two degenerations of one quadratic).** The norm vanishes exactly when $0$ is a root of $p_{\tilde Q}$; the spectral condition vanishes exactly when $p_{\tilde Q}$ has a double root. In the coefficients, $\mathcal N$ is the vanishing of the constant term and $\mathcal S$ the vanishing of the discriminant.

**Corollary (the four spectral patterns).** Write $\sigma(\tilde Q)=\{\lambda_+,\lambda_-\}$.

1. $\tilde Q\in\mathcal N$ exactly when $0\in\sigma(\tilde Q)$.
2. $\tilde Q\in\mathcal S$ exactly when $\sigma(\tilde Q)$ is a singleton.
3. $\tilde Q\in\mathcal N\cap\mathcal S$ exactly when $\sigma(\tilde Q)=\{0\}$.
4. Off the two cones, $\sigma(\tilde Q)$ is a pair of distinct non-zero complex numbers.

*Proof.* (1) By the spectral criterion of *Spectral Regularity and Degeneracy in the Biquaternion Algebra*, §*The Spectral Criterion*, $\lambda\in\sigma(\tilde Q)$ exactly when $(\lambda-Q_t)^2+B^2=0$; and $N(\tilde Q-\lambda e_t)=(\lambda-Q_t)^2+B^2$, so this is $N(\tilde Q-\lambda e_t)=0$. At $\lambda=0$ it is $N(\tilde Q)=0$. The same statement follows from $N=\lambda_+\lambda_-$. (2) is $\lambda_+-\lambda_-=2iB$. (3) combines (1) and (2). (4) is the negation of (1) and (2).

**The two conditions side by side.** The table collects the two readings.

| **item** | quaternionic norm | spectral condition |
|---|---|---|
| quantity | $N=Q_t^2+B^2$ | $B^2=Q_x^2+Q_y^2+Q_z^2$ |
| role in $p_{\tilde Q}$ | the constant term | the discriminant, up to $-4$ |
| spectral reading | $N=\lambda_+\lambda_-$ | $\lambda_+-\lambda_-=2iB$ |
| zero locus | $\mathcal N$ | $\mathcal S$ |
| vanishing means | an eigenvalue is $0$ | the two eigenvalues coincide |
| multiplicative | yes | no |
| decides | invertibility | separation of the spectrum |

**Corollary (the independence is a statement about a quadratic).** The two cones are independent because a quadratic over $\mathbb C$ can have a double non-zero root without a zero root, and a zero root without a double root. The algebraic witnesses are the two elements of §*Independence of the Two Cones*.

## The Norm as a Function of the Spectrum

**Theorem (the norm is determined by the spectrum).** The norm is the product of the eigenvalues,

$$
N=\lambda_+\lambda_-.
$$

The spectrum is not determined by the norm.

*Proof.* The first statement is the previous theorem. For the second, fix $N$ and vary $Q_t$: the eigenvalues $Q_t\pm iB$ with $B^2=N-Q_t^2$ change with $Q_t$, while the product stays $N$.

**Corollary (norm-regular exactly when no eigenvalue vanishes).** $\tilde Q$ is norm-regular exactly when both eigenvalues are non-zero.

*Proof.* $N=\lambda_+\lambda_-$ and $\mathbb C$ is a field.

**Corollary (the norm on each cone).**

- On $\mathcal S$ one has $N=Q_t^2$. So a point of $\mathcal S$ is norm-regular exactly when its repeated eigenvalue $Q_t$ is non-zero; the norm-degenerate points of $\mathcal S$ are the origin and the non-zero nilpotents.
- On $\mathcal N$ the spectrum is $\{2Q_t,0\}$. Off $\mathcal S$ one has $Q_t\neq0$, so exactly one eigenvalue is zero and the other is $2Q_t$.
- On $\mathcal S\setminus\mathcal N$ the spectrum is $\{Q_t,Q_t\}$ with $Q_t\neq0$.
- On $\mathcal N\setminus\mathcal S$ the spectrum is $\{2Q_t,0\}$ with $Q_t\neq0$.

*Proof.* On $\mathcal N$ one has $B^2=-Q_t^2$, so $iB=\pm Q_t$ and the eigenvalues $Q_t\pm iB$ are $2Q_t$ and $0$. The other statements follow from $N=Q_t^2+B^2$.

**Theorem (the norm does not separate the scalar line from the Jordan part).** Let $Q_t\neq0$ and let $\vec\Upsilon\neq0$ with $\vec\Upsilon^2=0$. The scalar $Q_te_t$ and the Jordan element $Q_te_t+\vec\Upsilon$ have the same norm $Q_t^2$, the same trace $2Q_t$, and therefore the same characteristic polynomial $(X-Q_t)^2$. They have different minimal polynomials, $X-Q_t$ and $(X-Q_t)^2$. No function of the norm alone distinguishes them.

*Proof.* The element $\vec\Upsilon$ is pure and square-zero, so $N(Q_te_t+\vec\Upsilon)=Q_t^2$ and the trace is $2Q_t$. The scalar satisfies $\tilde Q-Q_te_t=0$; the Jordan element satisfies $(\tilde Q-Q_te_t)^2=0$ and $\tilde Q-Q_te_t\neq0$.

**Remark (what the norm sees).** The norm is one of the two elementary symmetric functions of the spectrum, the product; the trace is the other, the sum. The norm alone leaves the sum free, hence leaves the spectrum free. The characteristic polynomial is the pair of the two symmetric functions, and it is the finer invariant; §*What the Spectrum Determines* states how much finer.

## Independence of the Two Cones

The two cones are independent: neither contains the other.

### Neither Cone Contains the Other

**Theorem.** $\mathcal N\not\subseteq\mathcal S$ and $\mathcal S\not\subseteq\mathcal N$.

*Proof.* Two witnesses.

- **A zero divisor with distinct eigenvalues.** Let $\tilde Q=e_t+i\vec e_x$. Then $N=1+i^2=0$, so $\tilde Q\in\mathcal N$, and $B^2=i^2=-1\neq0$, so $\tilde Q\notin\mathcal S$. Its eigenvalues are $1\pm i\cdot i$, that is $0$ and $2$; they are distinct, and the spectral decomposition exists, with the idempotents $\tilde Q/2$ and $e_t-\tilde Q/2$.
- **A unit with a repeated eigenvalue.** Let $\tilde Q=e_t+\vec e_x+i\vec e_y$. Then $B^2=1+i^2=0$, so $\tilde Q\in\mathcal S$, and $N=1+1+i^2=1\neq0$, so $\tilde Q\notin\mathcal N$. Its only eigenvalue is $1$, its minimal polynomial is $(X-1)^2$, and it is a unit with no spectral decomposition.

The first is a norm-degenerate, spectrally regular element; the second is a norm-regular, spectrally degenerate element.

### The Intersection

**Theorem (the intersection is the nilpotent cone).**

$$
\mathcal N\cap\mathcal S=\{N=0,\ B^2=0\}=\{Q_t=0,\ \vec Q^2=0\}=\{\tilde Q:\tilde Q^2=0\}.
$$

It is the origin together with the non-zero pure nilpotents.

*Proof.* If $N=0$ and $B^2=0$ then $Q_t^2=N-B^2=0$, so $Q_t=0$ and $\vec Q^2=-B^2e_t=0$. Conversely, $\tilde Q^2=(Q_t^2-B^2)e_t+2Q_t\vec Q$. If $\tilde Q^2=0$ and $\vec Q\neq0$, the vector part of the square gives $2Q_t\vec Q=0$, hence $Q_t=0$, and the scalar part gives $B^2=0$. If $\vec Q=0$, the square is $Q_t^2e_t$, so $Q_t=0$.

**The scheme.** As a scheme the intersection is

$$
(Q_t^2+B^2,\ B^2)=(Q_t^2,\ B^2),
$$

an ideal generated by two squares. Its reduction is the nilpotent cone; the scheme is not reduced.

**The tangency.** The gradients are

$$
\nabla N=2(Q_t,Q_x,Q_y,Q_z),\qquad \nabla B^2=2(0,Q_x,Q_y,Q_z).
$$

They coincide exactly when $Q_t=0$: along the smooth part of the intersection they are equal and non-zero, and at the origin both vanish. The two cones are therefore tangent along the nilpotent cone minus the origin, and both are singular at the origin.

### The Non-Multiplicativity

**The null cone is a semigroup.** The norm is multiplicative, $N(\tilde P\tilde Q)=N(\tilde P)N(\tilde Q)$, so both $\mathcal N$ and its complement are stable under the product. The spectral-degenerate cone is stable under neither the product nor the sum. The witness

$$
(\vec e_x+i\vec e_y)(\vec e_x-i\vec e_y)=-2e_t-2i\vec e_z
$$

is a product of two points of $\mathcal S$, since both factors have $B^2=1+i^2=0$. The product has $B^2=(-2i)^2=-4\neq0$, so it lies off $\mathcal S$; its norm is $4-4=0$, so it lies on $\mathcal N$. The sum

$$
(\vec e_x+i\vec e_y)+(\vec e_x-i\vec e_y)=2\vec e_x
$$

has $B^2=4\neq0$ as well. The cone $\mathcal S$ is a discriminant locus attached to the eigenvalue map, not a multiplicative subset.

## The Five Zones

**Definition (the five zones).** The two cones and their complements cut the algebra into four sectors: the complement of the union, the null cone minus the spectral cone, the spectral cone minus the null cone, and the intersection. The spectral sector minus the null cone is cut by the scalar part into the punctured scalar line and the Jordan part; the origin is adjoined to the scalar line to form the scalar zone. The resulting five zones are the joint refinement.

| zone | condition | eigenvalue pair | norm | minimal polynomial |
|---|---|---|---|---|
| **distinct** | $B^2\neq0$, $N\neq0$ | $\{\lambda_+,\lambda_-\}$, distinct and non-zero | $N\neq0$, unit | $p_{\tilde Q}$, squarefree |
| **zero divisor** | $B^2\neq0$, $N=0$ | $\{2Q_t,0\}$, $Q_t\neq0$ | $0$, zero divisor | squarefree |
| **scalar** | $\vec Q=0$ | $\{Q_t\}$ | $Q_t^2$ | $X-Q_t$ |
| **Jordan** | $B^2=0$, $\vec Q\neq0$, $Q_t\neq0$ | $\{Q_t,Q_t\}$, $Q_t\neq0$ | $Q_t^2$, unit | $(X-Q_t)^2$ |
| **nilpotent** | $B^2=0$, $\vec Q\neq0$, $Q_t=0$ | $\{0,0\}$ | $0$, zero divisor | $X^2$ |

**The zones and the sectors.** Write $\Sigma_{ij}$ for the sector with $i=1$ if $N\neq0$ and $j=1$ if $B^2\neq0$. The distinct zone is $\Sigma_{11}$, the complement of the union. The zero-divisor zone is $\Sigma_{01}=\mathcal N\setminus\mathcal S$. The union of the Jordan zone and the punctured scalar zone is $\Sigma_{10}=\mathcal S\setminus\mathcal N$, with the scalar zone the vertex of $\mathcal S$ and the Jordan zone its smooth part. The nilpotent zone is $\Sigma_{00}\setminus\{0\}$, and the origin belongs to the scalar zone. Each sector is treated in its own article: *The Norm-Regular, Spectrally Regular Sector*, *The Norm-Regular, Spectrally Degenerate Sector*, *The Norm-Degenerate, Spectrally Regular Sector* and *The Norm-Degenerate, Spectrally Degenerate Sector*.

**Theorem (the three partitions).** The norm, the characteristic polynomial and the minimal polynomial separate the five zones as follows.

| invariant | classes of zones | what it cannot separate |
|---|---|---|
| norm | $2$: units, the null cone | distinct from scalar and Jordan; zero divisor from nilpotent; the origin from the rest of the null cone |
| characteristic polynomial | $4$: distinct, zero divisor, scalar or Jordan, origin or nilpotent | scalar from Jordan; origin from nilpotent |
| minimal polynomial | $5$: one per zone | nothing |

*Proof.* The norm separates the units from the non-units; the origin is not separated from the rest of the null cone. The characteristic polynomial is the spectrum with multiplicity: it has two distinct roots on the distinct and zero-divisor zones, the double root $Q_t$ on the scalar zone, the double root $Q_t\neq0$ on the Jordan zone, and the double root $0$ on the nilpotent zone. The minimal polynomial is $X-Q_t$ on the scalar zone, $(X-Q_t)^2$ on the Jordan zone, $X$ at the origin, $X^2$ on the nilpotent zone, and the squarefree characteristic polynomial on the distinct and zero-divisor zones.

**Corollary (the norm is the coarser projection).** The spectral problem is finer than the norm problem: every norm class is a union of zones. The norm cannot separate the scalar line from the Jordan part, because both have $N=Q_t^2$, and it cannot separate the zero-divisor zone from the nilpotent zone, because both have $N=0$.

## The Two Decompositions

**The eigenbasis follows the discriminant, and the polar decomposition follows the norm. The two failures are therefore independent.**

### The Eigenbasis

By *Spectral Regularity and Degeneracy in the Biquaternion Algebra*, §*The Spectral Decomposition*, a non-scalar element has a unique spectral decomposition exactly when $B^2\neq0$. On the scalar line the decomposition exists with one term and every idempotent commutes with the element; on the Jordan and nilpotent zones no non-trivial idempotent commutes with it. In the zones: the spectral decomposition exists with two terms on the distinct and zero-divisor zones, with one term on the scalar zone, and it fails on the Jordan and nilpotent zones.

### The Polar Decomposition

The modulus–unit polar decomposition $\tilde Q=\Rho\tilde U$ requires $\Rho^2=N$ with $\Rho\neq0$, so it exists exactly on the complement of the null cone. It therefore fails on the zero-divisor and nilpotent zones and at the origin, and it exists on the distinct, scalar and Jordan zones. On the scalar line it exists exactly when $Q_t\neq0$, that is everywhere except the origin. The decomposition itself is *Modulus–Unit Polar Decomposition of Biquaternions*, and the comparison with the eigenbasis, factor by factor, is *Relations between Exponential Polar Decomposition and Eigenbasis of a Biquaternion*.

**The two decompositions in the zones.**

| zone | spectral decomposition | polar decomposition |
|---|---|---|
| distinct | yes, two terms, unique | yes |
| zero divisor | yes, two terms, unique | no |
| scalar, $Q_t\neq0$ | yes, one term | yes |
| origin | yes, one term | no |
| Jordan | no | yes |
| nilpotent | no | no |

**Corollary (the two sharpest witnesses).** The zero-divisor zone is a zero divisor with an eigenbasis, and the Jordan zone is a unit without one. The eigenbasis and the polar decomposition fail on different loci, and the Jordan zone is the sharpest witness of the independence: it is norm-regular, so the polar decomposition exists, and spectrally degenerate, so the eigenbasis does not.

## The Two Operator Loci

**Three operators read the two conditions: the rank of left multiplication and the sandwich follow the norm, and the inner derivation follows the discriminant.**

### The Rank of Left Multiplication

**Theorem.** The left multiplication $L_{\tilde Q}(X)=\tilde QX$ has complex rank $4$ when $N\neq0$, rank $2$ when $\tilde Q$ is a non-zero point of $\mathcal N$, and rank $0$ at the origin.

*Proof.* If $N\neq0$ then $\tilde Q$ is a unit and $L_{\tilde Q}$ is invertible. If $N=0$ and $\tilde Q\neq0$, the rank is $2$ by *The Four General Products and Their Relations over the Biquaternion Algebra*, §*The Annihilators*. At the origin the map is zero.

**Corollary.** The rank follows the norm, not the discriminant: the distinct zone and the Jordan zone both have rank $4$, and the zero-divisor zone and the nilpotent zone both have rank $2$.

### The Sandwich

**Definition.** The **sandwich** of $\tilde Q$ is the $\mathbb{C}$-linear operator

$$
\Theta_{\tilde Q}(X)=\tilde QX\tilde Q^{*}.
$$

**Theorem.** $\Theta_{\tilde Q}$ is singular exactly on the null cone.

*Proof.* Suppose first that $\langle\tilde Q\rangle_{\natural}=0$ with $\tilde Q\neq0$. Then $\tilde Q^{\natural}\neq0$, since $\tilde Q^{\natural}=Q_te_t-\vec Q=0$ forces $Q_t=0$ and $\vec Q=0$, hence $\tilde Q=0$. And

$$
\Theta_{\tilde Q}(\tilde Q^{\natural})=\tilde Q\,\tilde Q^{\natural}\,\tilde Q^{*}=\langle\tilde Q\rangle_{\natural}\,\tilde Q^{*}=0.
$$

So $\Theta_{\tilde Q}$ is singular. At the origin the operator is zero, hence singular. Conversely, if $N\neq0$ then $\tilde Q$ is a unit and

$$
\Theta_{\tilde Q}^{-1}=\Theta_{\tilde Q^{-1}}.
$$

Hence $\Theta_{\tilde Q}$ is singular exactly on $\mathcal N$.

### The Inner Derivation

**Definition.** The **inner derivation** of $\tilde Q$ is

$$
\mathrm{ad}_{\tilde Q}(X)=\tilde QX-X\tilde Q.
$$

**Theorem.** $\mathrm{ad}_{\tilde Q}$ is nilpotent exactly on the spectral-degenerate cone.

*Proof.* The scalar part is central, so $\mathrm{ad}_{\tilde Q}=\mathrm{ad}_{\vec Q}$. Since $\vec Q^{2}=-B^{2}e_t$,

$$
\mathrm{ad}_{\vec Q}^{2}(X)=\vec Q^{2}X-2\vec QX\vec Q+X\vec Q^{2}=-2B^{2}X-2\vec QX\vec Q.
$$

Applying $\mathrm{ad}_{\vec Q}$ once more, and using $\vec Q^{2}=-B^{2}e_t$ again,

$$
\mathrm{ad}_{\vec Q}^{3}(X)
=-2B^{2}(\vec QX-X\vec Q)-2(\vec Q^{2}X\vec Q-\vec QX\vec Q^{2})
=-4B^{2}\,\mathrm{ad}_{\vec Q}(X).
$$

If $B^{2}=0$ then $\mathrm{ad}_{\vec Q}^{3}=0$, so the derivation is nilpotent, of index at most three. If $B^{2}\neq0$, then $\vec Q\neq0$; a central element has zero vector part, so the derivation is not zero and $\mathrm{ad}_{\vec Q}^{3}\neq0$. In dimension four a nilpotent operator satisfies $\mathrm{ad}^{4}=0$; here $\mathrm{ad}^{4}=-4B^{2}\mathrm{ad}^{2}$, and $\mathrm{ad}^{2}\neq0$ because $\mathrm{ad}^{3}\neq0$, so $\mathrm{ad}^{4}\neq0$. The derivation is not nilpotent.

### The Table of the Operators

**The three operator readings in the zones.**

| zone | rank $L_{\tilde Q}$ | $\Theta_{\tilde Q}$ | $\mathrm{ad}_{\tilde Q}$ |
|---|---|---|---|
| distinct | $4$ | invertible | not nilpotent |
| zero divisor | $2$ | singular | not nilpotent |
| scalar, $Q_t\neq0$ | $4$ | invertible | nilpotent, zero |
| origin | $0$ | singular, zero | nilpotent |
| Jordan | $4$ | invertible | nilpotent |
| nilpotent | $2$ | singular | nilpotent |

**Corollary (the two operator loci).** The two cones are the two loci of the two-sided operators: the sandwich is singular exactly on $\mathcal N$, and the inner derivation is nilpotent exactly on $\mathcal S$. The rank and the sandwich are built from the norm and the star; the derivation is built from the commutator and sees the vector part alone. The criteria are cone-level and do not separate the strata: the derivation vanishes on the whole scalar line, and the sandwich is singular at the origin as well.

## What the Spectrum Determines

**Theorem (completeness of the characteristic polynomial).** Off the spectral-degenerate cone the characteristic polynomial, equivalently the pair $(2Q_t,N)$, is a complete invariant of the similarity class. On $\mathcal S$ it is not: exactly two similarity classes share each characteristic polynomial, the scalar class $Q_te_t$ and the Jordan class $Q_te_t+\vec\Upsilon$ with $\vec\Upsilon^2=0$ and $\vec\Upsilon\neq0$. At $Q_t=0$ the two classes are the origin and the non-zero nilpotents.

*Proof.* This is *Spectral Regularity and Degeneracy in the Biquaternion Algebra*, §*The Similarity Classification*. Off $\mathcal S$ the two eigenvalues are distinct, so the element is diagonalisable with that spectrum, and the unordered pair determines the class. On $\mathcal S$ the only eigenvalue is $Q_t$; the scalar class is central, and the Jordan class has minimal polynomial $(X-Q_t)^2$, so the two are not similar.

**Corollary (the minimal polynomial is the finer invariant).** The two classes of $\mathcal S$ are separated by the minimal polynomial, $X-Q_t$ against $(X-Q_t)^2$. The norm, the trace, the characteristic polynomial and the spectrum do not separate them.

**The chain of invariants.** The table compares what each invariant determines.

| invariant | data | determines |
|---|---|---|
| norm | $N\in\mathbb{C}$ | the product of the eigenvalues, and invertibility |
| characteristic polynomial | $(2Q_t,N)$ | the spectrum with multiplicity; the similarity class off $\mathcal S$, two classes on $\mathcal S$ |
| minimal polynomial | $m_{\tilde Q}$ | the five zones, and the similarity class on each |
| element up to similarity | the class of $\tilde Q$ | everything |

Read from the bottom to the top, each invariant is a function of the one below it. Read from the top to the bottom, information is lost: the norm loses the sum, and the characteristic polynomial loses the defect. The norm is the crudest invariant, the minimal polynomial the finest.

**The two degenerations, one last time.** The norm and the discriminant are the two ways the quadratic can degenerate: a zero constant term and a vanishing discriminant. The spectrum determines both. The norm determines neither the discriminant nor the defect. The relation between the two problems is therefore not an implication between the two vanishing conditions: it is a pair of projections of the same spectral data, the norm reading the product of the eigenvalues, the discriminant reading their difference, and the minimal polynomial reading whether they are attached to a defect.

## Summary

The biquaternion algebra carries two quadratic conditions. The quaternionic norm $N=Q_t^2+B^2$ is the constant term of the characteristic polynomial and the product of the eigenvalues; it is multiplicative, and it decides invertibility. The square of the vector part $B^2$ vanishes exactly when the discriminant of the characteristic polynomial vanishes, equivalently when the two eigenvalues coincide; it is not multiplicative, and it decides whether the two eigenvalues can be told apart. The null cone is the locus of an eigenvalue at zero, the spectral-degenerate cone the locus of a double eigenvalue.

The two cones are independent. Neither contains the other: $e_t+i\vec e_x$ is a zero divisor with distinct eigenvalues, and $e_t+\vec e_x+i\vec e_y$ is a unit with a repeated one. They meet exactly on the nilpotent cone, the set of square-zero elements, and they are tangent along it away from the origin. The null cone is a semigroup, the spectral cone is neither multiplicative nor additive.

The joint refinement is the five zones: distinct, zero-divisor, scalar, Jordan and nilpotent. The norm separates two classes, the characteristic polynomial four, and the minimal polynomial all five. The norm is therefore the coarser invariant: it cannot separate the scalar line from the Jordan part, nor the zero-divisor zone from the nilpotent zone. The characteristic polynomial is complete off the spectral cone and exactly two-to-one on it.

The two decompositions follow the two conditions. The eigenbasis follows the discriminant, and it fails on the Jordan and nilpotent zones; the polar decomposition follows the norm, and it fails on the null cone. The operator readings are the same pair of loci: the sandwich is singular exactly on the null cone, and the inner derivation is nilpotent exactly on the spectral-degenerate cone. The rank of left multiplication and the sandwich follow the norm; the derivation follows the discriminant.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde Q=Q_te_t+\vec Q$ | a general element |
| $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ | the vector part |
| $N(\tilde Q)=Q_t^2+B^2$ | the quaternionic norm, the constant term of $p_{\tilde Q}$ and the product of the eigenvalues |
| $B^2=Q_x^2+Q_y^2+Q_z^2$ | the square of the vector part, the discriminant up to $-4$ |
| $p_{\tilde Q}(X)=X^2-2Q_tX+N$ | the characteristic polynomial |
| $\lambda_\pm=Q_t\pm iB$ | the eigenvalues |
| $\operatorname{disc}p_{\tilde Q}=-4B^2=4(Q_t^2-N)$ | the discriminant |
| $\mathcal N=\{N=0\}$ | the null cone |
| $\mathcal S=\{B^2=0\}$ | the spectral-degenerate cone |
| $\Sigma_{11},\Sigma_{01},\Sigma_{10},\Sigma_{00}$ | the four sectors of the two cones |
| $L_{\tilde Q}(X)=\tilde QX$ | left multiplication; rank $4$ off $\mathcal N$, rank $2$ on $\mathcal N$ minus the origin, rank $0$ at the origin |
| $\Theta_{\tilde Q}(X)=\tilde QX\tilde Q^{*}$ | the sandwich, singular exactly on $\mathcal N$ |
| $\mathrm{ad}_{\tilde Q}(X)=\tilde QX-X\tilde Q$ | the inner derivation, nilpotent exactly on $\mathcal S$ |

## Further Reading

- [Quaternionic Norm Regularity and Degeneracy in the Biquaternion Algebra](quaternionic-norm-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the multiplicative norm, the null cone, its pure and non-pure strata, the unit group and the zero divisors.
- [Spectral Regularity and Degeneracy in the Biquaternion Algebra](spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the spectral criterion, the characteristic polynomial, the spectral-degenerate cone, the three regimes, the spectral decomposition and the eigenbasis.
- [The Norm-Regular, Spectrally Regular Sector](the-norm-regular-spectrally-regular-sector.html), for the distinct zone, the complement of the union of the two cones.
- [The Norm-Regular, Spectrally Degenerate Sector](the-norm-regular-spectrally-degenerate-sector.html), for the Jordan part, the unit with a repeated eigenvalue.
- [The Norm-Degenerate, Spectrally Regular Sector](the-norm-degenerate-spectrally-regular-sector.html), for the zero-divisor zone, the scaled idempotents and the spectrum $\{c,0\}$.
- [The Norm-Degenerate, Spectrally Degenerate Sector](the-norm-degenerate-spectrally-degenerate-sector.html), for the nilpotent cone and the origin.
- [Relations between Exponential Polar Decomposition and Eigenbasis of a Biquaternion](relations-between-exponential-polar-decomposition-and-eigenbasis-of-a-biquaternion.html), for the comparison of the two decompositions factor by factor.
- [Two-Sided Operator and the Polar Decomposition](two-sided-operator-and-the-polar-decomposition.html), for the sandwich, its spectrum and its rank on the null cone.
- [The Biquaternion Eigenvalue Decomposition](the-biquaternion-eigenvalue-decomposition.html), for the eigenvalue decomposition, the eigenprojections and the degenerate regimes.
- [Modulus–Unit Polar Decomposition of Biquaternions](modulus-unit-polar-decomposition-of-biquaternions.html), for the modulus $\Rho=\sqrt{N}$ and its failure at $N=0$.
