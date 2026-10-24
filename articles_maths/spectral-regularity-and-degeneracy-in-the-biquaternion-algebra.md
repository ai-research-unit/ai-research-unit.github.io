# __Spectral Regularity and Degeneracy in the Biquaternion Algebra__

## Introduction

The biquaternion algebra carries two quadratic conditions. The first is the reduced norm $N(\tilde Q)=Q_t^2+B^2$, with $B^2=Q_x^2+Q_y^2+Q_z^2$. Its zero locus is the null cone of the reduced norm; the norm is multiplicative and decides invertibility: that is *Norm Regularity and Degeneracy in the Biquaternion Algebra*. The second is $B^2$ itself, the square of the vector part. Its zero locus is the **spectral-degenerate cone** $\mathcal S$; the cone is not multiplicative, and it decides whether the two eigenvalues of the element can be told apart.

The article states the eigenvalue problem without a module or an acting operator. An eigenvalue is a scalar for which a left ideal is proper, an eigenvector is an element of a left annihilator, and a spectral idempotent is a Peirce idempotent adapted to the element. On that vocabulary the spectral criterion is proved: $\lambda$ is an eigenvalue of $\tilde Q$ exactly when $N(\tilde Q-\lambda e_t)=0$. The characteristic polynomial follows, with discriminant $-4B^2$, and the degenerate side $\mathcal S$ is stratified into three regimes: scalar, Jordan and nilpotent. The adapted Peirce decomposition is shown to exist exactly on the non-scalar side where $B^2\neq0$, and to fail on the Jordan and nilpotent regimes. The last sections show that the two degeneration loci are independent: a zero divisor can have distinct eigenvalues, and a unit can have a repeated one.

**Scope and naming.** The two problems are the two quadratic problems of the algebra. The norm problem asks whether the element can be inverted; its degeneration locus is the null cone $\mathcal C=\{N=0\}$. The spectral problem asks whether the two eigenvalues can be separated; its degeneration locus is $\mathcal S=\{B^2=0\}$. Three naming rules are held throughout. First, $\mathcal C$ is the **null cone of the reduced norm**, qualified at first use, and then the null cone. Second, $\mathcal S$ is the **spectral-degenerate cone** and is never called a null cone: $B^2$ is the square of the vector part, not a norm on $\mathbb{B}$, so $\mathcal S$ is not the null cone of a norm on the algebra. Third, unqualified **regular** means **spectrally regular**, that is $B^2\neq0$; the companion article's regular side, the unit group, is written **norm-regular** wherever the two could collide.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ on the basis $e_t,\vec e_x,\vec e_y,\vec e_z$, with $\vec e_x\vec e_y=\vec e_z$ and $\vec e_k^2=-e_t$, and with complex coefficients. The natural conjugation is the $\mathbb{C}$-linear quaternion conjugation $\tilde Q^{\natural}=Q_t-\vec Q$, an anti-involution of order two fixing the centre. The vector part is $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$, and

$$
B^2=Q_x^2+Q_y^2+Q_z^2,\qquad \vec Q^2=-B^2e_t,\qquad N(\tilde Q)=\tilde Q^{\natural}\tilde Q=\tilde Q\tilde Q^{\natural}=(Q_t^2+B^2)e_t.
$$

The number $B$ is a fixed complex square root of $Q_x^2+Q_y^2+Q_z^2$; the other root only exchanges the two eigenvalues. The algebra and its conventions are *The Biquaternion Algebra and Its Vector Spaces*; the spectrum and the characteristic polynomial are *Biquaternion Spectral Theory*; the eigenvalue decomposition is *The Biquaternion Eigenvalue Decomposition*; the Peirce decomposition is *Ideals and Peirce Decompositions of the Biquaternion Algebra*.

## The Spectral Criterion

**Definition (eigenvalue).** A scalar $\lambda\in\mathbb{C}$ is an **eigenvalue** of $\tilde Q$ if the left ideal $\mathbb{B}(\tilde Q-\lambda e_t)$ is proper, that is $\mathbb{B}(\tilde Q-\lambda e_t)\neq\mathbb{B}$.

**Definition (eigenvector).** A non-zero $v\in\mathbb{B}$ is an **eigenvector** of $\tilde Q$ for $\lambda$ if $(\tilde Q-\lambda e_t)v=0$. The eigenvectors for $\lambda$, with the origin, are the left annihilator

$$
\operatorname{Ann}_{\ell}(\tilde Q-\lambda e_t)=\{v:\ (\tilde Q-\lambda e_t)v=0\},
$$

which is a right ideal of $\mathbb{B}$.

**Definition (spectral idempotent).** A non-zero idempotent $e$ is a **spectral idempotent** of $\tilde Q$ if $e\tilde Q=\tilde Qe=\lambda e$ for some scalar $\lambda$.

**Definition (spectral decomposition).** A **spectral decomposition** of $\tilde Q$ is a pair of orthogonal idempotents $e_+,e_-$ with

$$
e_++e_-=e_t,\qquad e_+e_-=0,\qquad \tilde Qe_\pm=\lambda_\pm e_\pm,\qquad \lambda_+\neq\lambda_-.
$$

No module and no acting operator enters the definitions: the primitives are the left ideal, the left annihilator and the idempotent.

**Theorem (the spectral criterion).** For $\tilde Q\in\mathbb{B}$ and $\lambda\in\mathbb{C}$, the following are equivalent:

1. $\lambda$ is an eigenvalue of $\tilde Q$;
2. $\tilde Q-\lambda e_t$ is not a unit of the plain product;
3. $N(\tilde Q-\lambda e_t)=0$.

*Proof.* Write $a=\tilde Q-\lambda e_t$.

*(1)$\iff$(2).* If $a$ is a unit then $\mathbb{B}a=\mathbb{B}$, and the left ideal is not proper. Conversely, if $\mathbb{B}a=\mathbb{B}$, then $e_t=xa$ for some $x$, so $x$ is a left inverse of $a$. The left multiplication by $a$ is then injective: $ay=0$ gives $y=xay=0$. In finite dimension an injective endomorphism is bijective, so there is $b$ with $ab=e_t$; then

$$
x=x e_t=x(ab)=(xa)b=e_tb=b,
$$

and $a$ has the two-sided inverse $b$. Hence a proper left ideal forces a non-unit.

*(2)$\iff$(3).* If $a$ is not a unit, the left multiplication by $a$ is not surjective, since a surjective endomorphism of the finite-dimensional space $\mathbb{B}$ is bijective and would give a right inverse, hence a unit. By rank–nullity there is $v\neq0$ with $av=0$; then

$$
N(a)v=a^{\natural}av=0,
$$

and $N(a)$ is central, so $N(a)=0$. Conversely, if $a$ were a unit $u$ and $N(a)=0$, then $N(a)N(u)=N(e_t)=1$ by multiplicativity, a contradiction.

**Corollary (the characteristic polynomial).** For every $\lambda$,

$$
N(\tilde Q-\lambda e_t)=(\lambda-Q_t)^2+B^2,
$$

so the characteristic polynomial is

$$
p_{\tilde Q}(X)=X^2-2Q_tX+N(\tilde Q),
$$

of discriminant

$$
\operatorname{disc}p_{\tilde Q}=4Q_t^2-4N(\tilde Q)=-4B^2.
$$

The eigenvalues are

$$
\lambda_\pm=Q_t\pm iB,
$$

and they coincide exactly when $B=0$, that is exactly when $B^2=0$.

**Corollary (the eigenspaces).** For a non-scalar $\tilde Q$ and each eigenvalue $\lambda$, the eigenspace $\operatorname{Ann}_{\ell}(\tilde Q-\lambda e_t)$ is a right ideal of complex dimension $2$. For $\tilde Q=Q_te_t$ the only eigenvalue is $Q_t$, and its eigenspace is all of $\mathbb{B}$.

*Proof.* A non-zero non-unit in $\mathbb{B}$ has left multiplication of complex rank $2$, by *Norm Regularity and Degeneracy in the Biquaternion Algebra*, §*The Annihilators*; at the scalar the difference $\tilde Q-Q_te_t$ is zero.

## The Spectral-Degenerate Cone

**Definition.** The **spectral-degenerate cone** is

$$
\mathcal S=\{B^2=0\}=\{\vec Q^2=0\}=\{\operatorname{disc}p_{\tilde Q}=0\}.
$$

**Theorem (three readings of one equation).** The equation $B^2=0$ is simultaneously:

- **geometric:** the vector part is isotropic for the quaternionic bilinear form, $\langle\vec Q,\vec Q\rangle_{\natural}=Q_x^2+Q_y^2+Q_z^2=0$;
- **algebraic:** the vector part is square-zero, $\vec Q^2=0$, hence nilpotent of index two when it is non-zero;
- **spectral:** the discriminant vanishes, and the two eigenvalues coalesce at $Q_t$.

**Theorem (the geometry).** The cone is the product of the scalar line and the isotropic cone of the vector subspace,

$$
\mathcal S=\mathbb{C}e_t\times\{\vec Q\in\operatorname{Vect}(\mathbb{B}):\vec Q^2=0\}.
$$

It is a complex cone of complex dimension $3$ and real dimension $6$. Its singular locus is the **vertex** $\{\vec Q=0\}$, the whole scalar line; off the vertex it is a smooth hypersurface.

*Proof.* The equation $B^2=0$ is one complex equation in the four complex coefficients, homogeneous of degree two. Its gradient with respect to $(Q_t,Q_x,Q_y,Q_z)$ is

$$
(0,\,2Q_x,\,2Q_y,\,2Q_z),
$$

which vanishes exactly when $\vec Q=0$. Off the vertex the gradient is non-zero and the equation cuts a smooth hypersurface, of complex dimension $4-1=3$ and real dimension $8-2=6$. On the vertex the cone is $\mathbb{C}e_t\times C$, with $C$ the isotropic cone of $\mathbb{C}^3$, which is singular at its apex; the product is singular along the whole line.

**The cone is not a subspace.** The elements $\vec e_x+i\vec e_y$ and $\vec e_x-i\vec e_y$ lie on $\mathcal S$, since their vector squares are $1+i^2=0$, but their sum $2\vec e_x$ has $B^2=4$ and lies off it.

**Warning (the vertex is not defective).** A point of the vertex is a scalar $\tilde Q=Q_te_t$. Its only eigenvalue is $Q_t$, repeated, and its minimal polynomial is $X-Q_t$: it is semisimple and diagonalisable. The cone $\mathcal S$ is therefore the set of elements with a repeated eigenvalue, not the set of non-diagonalisable elements. The defective elements of $\mathcal S$ are the Jordan and nilpotent regimes of §*The Three Regimes of the Cone*. This distinction is invisible in the equation $B^2=0$.

**Warning (the name).** The form $B^2$ is the restriction of the quaternionic bilinear algebraic norm to the vector subspace. It does not see the scalar part, so it is degenerate as a form on $\mathbb{B}$ and is not a norm on $\mathbb{B}$. The only multiplicative norm of the algebra is the reduced norm $N$, whose null cone is $\mathcal C$. The cone $\mathcal S$ is the zero set of a quadratic form that does not involve $Q_t$, and it is never called a null cone.

## The Adapted Peirce Decomposition

**Two Peirce objects.** Let $e$ be an idempotent and $f=e_t-e$. The **weak Peirce decomposition** of an element $X$ is

$$
X=eXe+eXf+fXe+fXf,
$$

and it holds for every $X$ and every idempotent $e$: its availability is a property of the algebra, not of $X$. The **adapted Peirce decomposition** of $\tilde Q$ relative to $e$ is the stronger statement that the two off-diagonal components vanish,

$$
e\tilde Qf=f\tilde Qe=0,
$$

which is equivalent to $e\tilde Q=\tilde Qe$: the idempotent commutes with the element. The equivalence uses that the algebra is split: every non-trivial idempotent of $\mathbb{B}$ is primitive, by *Ideals and Peirce Decompositions of the Biquaternion Algebra*, §*Idempotents and Orthogonal Idempotents*, so its corner $e\mathbb{B}e$ is a finite-dimensional complex division algebra, hence $\mathbb{C}e$. Then $e\tilde Q=\tilde Qe$ forces $\tilde Qe\in\mathbb{C}e$ and $\tilde Qf\in\mathbb{C}f$, and the two off-diagonal blocks vanish.

**Theorem (existence).** Let $\tilde Q$ be non-scalar. The following are equivalent:

1. $B^2\neq0$;
2. $\tilde Q$ has a spectral decomposition;
3. there is a non-trivial idempotent $e$ with $e\tilde Q=\tilde Qe$;
4. $\tilde Q$ is semisimple.

*Proof.* (1)$\Rightarrow$(2). When the eigenvalues are distinct, the Lagrange idempotents

$$
e_\pm=\frac{\tilde Q-\lambda_\mp e_t}{\lambda_\pm-\lambda_\mp}
$$

are defined. The algebra identities give

$$
e_\pm^2=e_\pm,\qquad e_+e_-=0,\qquad e_++e_-=e_t,\qquad \tilde Qe_\pm=\lambda_\pm e_\pm,
$$

so they form a spectral decomposition.

(2)$\Rightarrow$(3). The idempotent $e_+$ is non-trivial: if $e_+=0$ then $\tilde Q=\lambda_-e_t$, and if $e_+=e_t$ then $\tilde Q=\lambda_+e_t$; both are contrary to the hypothesis. It commutes with $\tilde Q$ because $\tilde Qe_+=\lambda_+e_+=e_+\tilde Q$.

(3)$\Rightarrow$(1). Suppose $B^2=0$. Since $\tilde Q$ is non-scalar, $\vec Q\neq0$ and $\vec Q^2=0$. The minimal polynomial is then $(X-Q_t)^2$, and the centraliser of $\tilde Q$ is

$$
\mathbb{C}[\tilde Q]=\mathbb{C}[\varepsilon]/(\varepsilon^2),\qquad \varepsilon=\tilde Q-Q_te_t=\vec Q,
$$

by *The Biquaternion Eigenvalue Decomposition*, §*The Degenerate Regimes*. An idempotent $ae_t+b\varepsilon$ satisfies $a^2=a$ and $2ab=b$, so $a=b=0$ or $a=1$, $b=0$: the only idempotents are $0$ and $e_t$, and there is no non-trivial one. Contradiction.

(1)$\iff$(4). For a non-scalar element the minimal polynomial is the characteristic polynomial, of degree two. It is squarefree exactly when the two roots are distinct, that is exactly when $B^2\neq0$.

**Corollary (uniqueness).** If $B^2\neq0$, the spectral decomposition is unique. The centraliser of $\tilde Q$ is $\mathbb{C}[\tilde Q]\cong\mathbb{C}\times\mathbb{C}$, whose only idempotents are $0,e_t,e_+,e_-$, and every adapted Peirce decomposition uses the pair $e_+,e_-$.

*Proof.* The minimal polynomial has two distinct roots, so the Chinese remainder theorem gives $\mathbb{C}[X]/((X-\lambda_+)(X-\lambda_-))\cong\mathbb{C}\times\mathbb{C}$, and the idempotents of the product are the four listed. An idempotent adapted to $\tilde Q$ lies in its centraliser and is therefore one of them.

**The scalar exception.** The theorem excludes the scalar elements, and it must: if $\tilde Q=Q_te_t$ is central, every idempotent commutes with it, so condition (3) holds while $B^2=0$. The scalar regime is treated separately below.

## The Three Regimes of the Cone

The cone $\mathcal S$ is cut by $B^2=0$, but the geometry of its points is decided by two further questions: whether the scalar part vanishes, and whether the vector part vanishes. The answers give the **scalar regime** ($\vec Q=0$), the **Jordan regime** ($B^2=0$, $\vec Q\neq0$, $Q_t\neq0$) and the **nilpotent regime** ($B^2=0$, $\vec Q\neq0$, $Q_t=0$).

| regime | condition | spectrum | minimal polynomial | adapted Peirce | the element is |
|---|---|---|---|---|---|
| **scalar** | $\vec Q=0$ | $\{Q_t\}$ | $X-Q_t$ | every idempotent | central, semisimple; a unit iff $Q_t\neq0$ |
| **Jordan** | $B^2=0$, $\vec Q\neq0$, $Q_t\neq0$ | $\{Q_t\}$ | $(X-Q_t)^2$ | none non-trivial | a unit, defective, one Jordan block |
| **nilpotent** | $B^2=0$, $\vec Q\neq0$, $Q_t=0$ | $\{0\}$ | $X^2$ | none non-trivial | a non-unit, $\tilde Q^2=0$ |

### The Scalar Regime

Let $\tilde Q=Q_te_t$. The element is central, its minimal polynomial is $X-Q_t$, and it is semisimple with the single eigenvalue $Q_t$. Every idempotent commutes with it, so every idempotent is adapted. The spectral decomposition in the sense of the general theory has one term, $\tilde Q=Q_te_t$, and it is unique; a two-term writing with two orthogonal idempotents summing to $e_t$ has the equal coefficient $Q_t$ on both terms and is not determined by $\tilde Q$. This is the only regime in which a two-term writing exists without being a spectral decomposition.

### The Jordan Regime

Let $\tilde Q=Q_te_t+\vec\Upsilon$ with $\vec\Upsilon^2=0$ and $\vec\Upsilon\neq0$, and let $Q_t\neq0$. The minimal polynomial is $(X-Q_t)^2$, the spectrum is the single eigenvalue $Q_t$, and the element is a unit, since $N(\tilde Q)=Q_t^2\neq0$. Its centraliser is $\mathbb{C}[\tilde Q]=\{ae_t+b\vec\Upsilon\}$, whose only idempotents are $0$ and $e_t$, so no non-trivial adapted Peirce decomposition exists. The element is a single Jordan block: it is defective, and the two eigenvalues of the spectrally regular side have coalesced at $Q_t$ without the element becoming scalar.

The closest available structure is the Peirce form relative to an idempotent $e$ with $\vec\Upsilon\in e\mathbb{B}f$, where $f=e_t-e$. Such an idempotent exists, and for it

$$
e\tilde Qe=Q_te,\qquad e\tilde Qf=\vec\Upsilon,\qquad f\tilde Qe=0,\qquad f\tilde Qf=Q_tf,
$$

so the element is diagonal on the two Peirce corners and carries its nilpotent part in one off-diagonal corner.

### The Nilpotent Regime

Let $\tilde Q=\vec\Upsilon$ with $\vec\Upsilon^2=0$ and $\vec\Upsilon\neq0$. The spectrum is $\{0\}$, the minimal polynomial is $X^2$, and the element is not a unit: it lies on the null cone of the reduced norm, and it is a zero divisor. The centraliser and the absence of a non-trivial adapted Peirce decomposition are the same as in the Jordan regime. Relative to an idempotent $e$ with $\vec\Upsilon\in e\mathbb{B}f$, the Peirce form is purely off-diagonal,

$$
e\tilde Qe=0,\qquad e\tilde Qf=\vec\Upsilon,\qquad f\tilde Qe=0,\qquad f\tilde Qf=0.
$$

This regime is the pure stratum of the null cone, with the origin removed.

### The Vertex

The scalar regime is the vertex $\{\vec Q=0\}$. A point of the vertex is semisimple, has a repeated eigenvalue, and is not defective. The singular locus of $\mathcal S$ is this line, made of the elements of $\mathcal S$ with the mildest spectral degeneration: the eigenvalue is repeated, but the element still has a spectral decomposition, with one term.

## Independence of the Two Cones

The two cones are independent: neither contains the other.

### The Two Witnesses

The witnesses are the mixed cells.

- **A zero divisor with distinct eigenvalues.** Let $\tilde Q=e_t+i\vec e_x$. Then $N(\tilde Q)=1+i^2=0$, so $\tilde Q$ lies on the null cone, and $B^2=i^2=-1\neq0$, so it lies off the spectral-degenerate cone. Its eigenvalues are $1\pm i\cdot i$, that is $0$ and $2$; they are distinct, and the spectral decomposition exists, with the idempotents $\tilde Q/2$ and $e_t-\tilde Q/2$. A zero divisor can be spectrally regular.
- **A unit with a repeated eigenvalue.** Let $\tilde Q=e_t+\vec e_x+i\vec e_y$. Then $B^2=1+i^2=0$, so $\tilde Q$ lies on the spectral-degenerate cone, and $N(\tilde Q)=1+1+i^2=1\neq0$, so it lies off the null cone. Its only eigenvalue is $1$, its minimal polynomial is $(X-1)^2$, and it is a unit with no spectral decomposition. This is the Jordan regime, and it is the cell that proves the independence.

### The Intersection

The two cones meet exactly on the pure stratum of the null cone, with the origin adjoined. Here $\mathcal C_{\mathrm p}=\{Q_t=0,\ \vec Q^2=0,\ \vec Q\neq0\}$ is the pure stratum of the companion article, so

$$
\mathcal C\cap\mathcal S=\{Q_t^2+B^2=0,\ B^2=0\}=\{Q_t=0,\ \vec Q^2=0\}=\mathcal C_{\mathrm p}\cup\{0\}.
$$

As a scheme, the intersection is

$$
(Q_t^2+B^2,\ B^2)=(Q_t^2,\ B^2),
$$

an ideal generated by two squares: its reduction is the pure stratum with the origin adjoined, and the scheme is non-reduced along both defining hypersurfaces. The two defining equations have equal gradients along the smooth part of the intersection: the gradients are $2(Q_t,Q_x,Q_y,Q_z)$ and $(0,2Q_x,2Q_y,2Q_z)$, which agree where $Q_t=0$.

### The Non-Multiplicativity

The null cone is a semigroup, because $N$ is multiplicative. The spectral-degenerate cone is not. The witness

$$
(\vec e_x+i\vec e_y)(\vec e_x-i\vec e_y)=-2e_t-2i\vec e_z
$$

is a product of two points of $\mathcal S$, since $1+i^2=0$ in both factors, and the product has $B^2=(-2i)^2=-4\neq0$, so it lies off $\mathcal S$; its reduced norm is $4-4=0$, so it lies on $\mathcal C$. The cone $\mathcal S$ is a discriminant locus attached to the eigenvalue map, not a multiplicative subset.

### The Five Zones

The joint refinement of the two cones partitions the algebra into the **distinct** zone ($B^2\neq0$, $N\neq0$), the **zero-divisor** zone ($B^2\neq0$, $N=0$), the **scalar** zone ($\vec Q=0$), the **Jordan** zone ($B^2=0$, $\vec Q\neq0$, $Q_t\neq0$) and the **nilpotent** zone ($B^2=0$, $\vec Q\neq0$, $Q_t=0$):

| zone | condition | norm | spectral data |
|---|---|---|---|
| **distinct** | $B^2\neq0$, $N\neq0$ | unit | two distinct eigenvalues |
| **zero divisor** | $B^2\neq0$, $N=0$ | zero divisor | two distinct eigenvalues, $0$ one of them |
| **scalar** | $\vec Q=0$ | $N=Q_t^2$ | one eigenvalue, semisimple |
| **Jordan** | $B^2=0$, $\vec Q\neq0$, $Q_t\neq0$ | unit | one eigenvalue, defective |
| **nilpotent** | $B^2=0$, $\vec Q\neq0$, $Q_t=0$ | zero divisor | one eigenvalue $0$, defective |

The origin belongs to the scalar zone; the nilpotent zone excludes it. The norm problem puts the zero-divisor zone, the nilpotent zone and the origin on one side, and the distinct zone, the non-zero scalar line and the Jordan zone on the other. The spectral problem separates all five zones, because its data include the minimal polynomial: the eigenvalues give $Q_t$ and $B^2$, and the minimal polynomial separates the scalar line from the Jordan regime. The norm problem is therefore the coarser projection: it cannot separate the scalar line from the Jordan zone, because both have $N=Q_t^2$. The independence is between the loci, not between the information: the product of the eigenvalues is $N$, so the spectrum determines the norm, but the norm does not determine $B^2$.

## The Two Failures Compared

The independence of the loci has a concrete form in the two decompositions the corpus uses.

### The Eigenbasis

The spectral decomposition exists on the distinct zone and on the zero-divisor zone, where $B^2\neq0$, and it fails on the Jordan and nilpotent zones. On the null cone it exists on the non-pure stratum, where $N=0$, $B^2=-Q_t^2\neq0$ and the eigenvalues are $2Q_t$ and $0$; it fails on the nilpotent stratum, which is the pure stratum. On the Jordan regime it fails although the element is a unit: the modulus–unit polar decomposition exists and the eigenbasis does not.

### The Polar Decomposition

The modulus–unit polar decomposition $\tilde Q=\Rho\tilde U$ requires $\Rho^2=N(\tilde Q)$ with $\Rho\neq0$, so it exists exactly off the null cone. It therefore fails on the zero-divisor zone, where the eigenbasis exists, and it exists on the Jordan zone, where the eigenbasis fails. On the scalar zone it exists exactly when $Q_t\neq0$, that is everywhere except the origin.

### The Operators

The left and the right multiplication by $\tilde Q$ have complex rank $4$ when $N\neq0$, rank $2$ when $\tilde Q$ is a non-zero point of the null cone, and rank $0$ at the origin. The discriminant does not change these ranks: the distinct zone and the Jordan zone both have rank $4$, and the zero-divisor zone and the nilpotent zone both have rank $2$. The rank follows the norm, not the discriminant.

| zone | spectral decomposition | polar decomposition | rank of left multiplication |
|---|---|---|---|
| distinct | yes | yes | $4$ |
| zero divisor | yes | no | $2$ |
| scalar, $Q_t\neq0$ | one term | yes | $4$ |
| origin | one term | no | $0$ |
| Jordan | no | yes | $4$ |
| nilpotent | no | no | $2$ |

## Summary

The biquaternion algebra carries two quadratic conditions. The reduced norm $N=Q_t^2+B^2$ is multiplicative and decides invertibility; its zero locus is the null cone $\mathcal C$. The discriminant of the characteristic polynomial is $-4B^2$; its zero locus is the spectral-degenerate cone $\mathcal S$, and it decides whether the two eigenvalues $Q_t\pm iB$ can be separated.

The spectral problem is stated without a module or an acting operator. An eigenvalue is a scalar for which the left ideal $\mathbb{B}(\tilde Q-\lambda e_t)$ is proper, equivalently for which $\tilde Q-\lambda e_t$ is a non-unit, equivalently for which $N(\tilde Q-\lambda e_t)=0$. The eigenspace is the left annihilator, a right ideal of complex dimension $2$ for a non-scalar element. A spectral idempotent is an idempotent commuting with the element, and on the regular side the spectral decomposition is the pair of Lagrange idempotents.

The cone $\mathcal S$ is $\mathbb{C}e_t$ times the isotropic cone of the vector subspace, of complex dimension $3$ and real dimension $6$. It is smooth off the scalar vertex and singular along it. It is not a subspace, and it is not the set of defective elements: the vertex is semisimple. It is not a null cone, because $B^2$ is not a norm on the algebra; the only multiplicative norm is $N$.

On the non-scalar side, the adapted Peirce decomposition exists exactly when $B^2\neq0$, and then it is unique. The degenerate side is stratified into the scalar regime, where every idempotent is adapted and the spectral decomposition has one term; the Jordan regime, where the element is a unit, defective and without a non-trivial adapted idempotent; and the nilpotent regime, where the element is a zero divisor and a nilpotent of index two. The vertex is the scalar line.

The two cones are independent: neither contains the other. A zero divisor can have distinct eigenvalues, and a unit can have a repeated one. The cones meet exactly on the pure stratum of the null cone, with the origin adjoined, and their defining equations have equal gradients along it. The spectral cone is not multiplicative, while the null cone is. The joint refinement is the five zones. The spectral problem is the finer one: its eigenvalues determine the norm, since $N=\lambda_+\lambda_-$, but the norm does not determine $B^2$. The independence is between the loci, not between the information: the norm cannot separate the scalar from the Jordan regime, while the spectral problem separates all five zones, through the minimal polynomial. The polar decomposition follows the norm and the eigenbasis follows the discriminant, so the Jordan regime, a unit with no eigenbasis, is the sharpest witness of the independence.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde Q=Q_te_t+\vec Q$ | a general element |
| $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ | the vector part |
| $B^2=Q_x^2+Q_y^2+Q_z^2$ | the square of the vector part, not a norm on $\mathbb{B}$ |
| $N(\tilde Q)=Q_t^2+B^2$ | the reduced norm, the only multiplicative one |
| $p_{\tilde Q}(X)=X^2-2Q_tX+N(\tilde Q)$ | the characteristic polynomial |
| $\operatorname{disc}p_{\tilde Q}=-4B^2$ | the discriminant |
| $\lambda_\pm=Q_t\pm iB$ | the eigenvalues |
| $\mathcal C=\{N=0\}$ | the null cone of the reduced norm |
| $\mathcal S=\{B^2=0\}$ | the spectral-degenerate cone |
| $\operatorname{Ann}_{\ell}(a)=\{v:av=0\}$ | the left annihilator, a right ideal |
| $e_\pm=(\tilde Q-\lambda_\mp e_t)/(\lambda_\pm-\lambda_\mp)$ | the spectral idempotents |
| $\vec\Upsilon$ | a non-zero vector with $\vec\Upsilon^2=0$ |
| $\mathcal C_{\mathrm p}=\{Q_t=0,\ \vec Q^2=0,\ \vec Q\neq0\}$ | the pure stratum of the null cone, the nilpotents |

## Further Reading

- [Norm Regularity and Degeneracy in the Biquaternion Algebra](norm-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the reduced norm, the null cone, its pure and non-pure strata, the unit group and the zero divisors.
- [Biquaternion Spectral Theory](biquaternion-spectral-theory.html), for the spectrum, the characteristic polynomial, Cayley–Hamilton and the spectral theorem.
- [The Biquaternion Eigenvalue Decomposition](the-biquaternion-eigenvalue-decomposition.html), for the eigenvalue decomposition and the degenerate regimes.
- [Ideals and Peirce Decompositions of the Biquaternion Algebra](ideals-and-peirce-decompositions-of-the-biquaternion-algebra.html), for the weak Peirce decomposition, the Peirce corners and the minimal left ideals.
- [The Eigenvalue Decomposition of an Element](the-eigenvalue-decomposition-of-an-element.html), for the existence and uniqueness of the spectral decomposition in the general theory.
- [The Lagrange–Sylvester Eigenprojector Formula](the-lagrange-sylvester-eigenprojector-formula.html), for the interpolating idempotents.
- [Modules over $k[x]$ and the Jordan Form](modules-over-kx-and-the-jordan-form.html), for the Jordan block behind the Jordan regime.
- [Nilpotent Elements and the Jordan–Chevalley Decomposition](nilpotent-elements-and-the-jordan-chevalley-decomposition.html), for the semisimple and nilpotent parts.
- [Modulus–Unit Polar Decomposition of Biquaternions](modulus-unit-polar-decomposition-of-biquaternions.html), for the polar decomposition that the null cone obstructs.
