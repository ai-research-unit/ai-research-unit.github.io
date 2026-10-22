# __Exponential Polar Decomposition of Biquaternions__

## Introduction

This article treats the **exponential polar decomposition** of an invertible biquaternion: the writing

$$
\tilde Q=r\,\exp(i\alpha)\,\exp(i\frac{\psi}{2}\vec u_{\mathrm b})\,\exp(\frac{\theta}{2}\vec u_{\mathrm r}),
\qquad r>0,\quad \alpha\in\Bigl(-\frac{\pi}{2},\frac{\pi}{2}\Bigr],\quad \psi\ge0,\quad \theta\in[0,2\pi],
$$

with $\vec u_{\mathrm b}$ and $\vec u_{\mathrm r}$ unit vectors of $\mathbb{R}^{3}$. The four exponentials are the four factors of the modulus–unit polar decomposition of *Modulus–Unit Polar Decomposition of Biquaternions*,

$$
\tilde Q=r\,\zeta\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r},
\qquad \zeta=\exp(i\alpha),\quad \tilde U_{\mathrm b}=\exp(i\frac{\psi}{2}\vec u_{\mathrm b}),\quad \tilde u_{\mathrm r}=\exp(\frac{\theta}{2}\vec u_{\mathrm r}),
$$

read with the parameters of each factor displayed. The scale is $r=\exp(\ln r)$, the central phase is $\zeta=\exp(i\alpha)$, the boost is the Hermitian positive unit-norm element of rapidity $\psi$ and axis $\vec u_{\mathrm b}$, and the rotor is the unit real quaternion of angle $\theta$ and axis $\vec u_{\mathrm r}$.

The exponential and the logarithm are those of *Biquaternion Elementary Functions*, §*The Exponential*, §*The Logarithm* and §*The Exponential in the Two Real Directions*; the eigenvalues $\lambda_\pm=Q_t\pm iB$, the eigenprojections $\tilde\Pi_\pm$, the pure unit $\vec U$, the pure root $\vec\Xi$ and the Peirce decomposition are those of *Eigenvalue Decomposition of a Biquaternion*. §*The Spectral Setting* states these results in the form used below, and they are not derived again.

The quaternion case of *Exponential Polar Decomposition of Quaternions* amalgamates the scale and the rotor into a single exponential, $\tilde q=\exp(\ln r+\vec v)$, because the logarithmic scale is real and central and the remaining exponent is one pure quaternion. **The biquaternion case does not amalgamate.** The boost exponent $i\frac{\psi}{2}\vec u_{\mathrm b}$ and the rotor exponent $\frac{\theta}{2}\vec u_{\mathrm r}$ do not commute unless the two axes are parallel or antiparallel, so

$$
\exp(i\frac{\psi}{2}\vec u_{\mathrm b})\exp(\frac{\theta}{2}\vec u_{\mathrm r})
\neq \exp(i\frac{\psi}{2}\vec u_{\mathrm b}+\frac{\theta}{2}\vec u_{\mathrm r})
$$

in general. The four exponents are therefore kept separate, and the decomposition is a product of four exponentials. A single logarithm of $\tilde Q$ still exists — the group of units is $\mathrm{GL}_2(\mathbb{C})$, which is exponential — but it is not the sum of the four exponents; the difference is the Baker–Campbell–Hausdorff correction, computed in §*The Exponent and the Logarithm*.

The word is defined on the invertible elements, and its boundary is the null cone, the set where the norm vanishes. The boundary is not a harmless edge: the rapidity diverges there, the scale collapses, and the word has no single limit there, only boundary values along paths. The elements that carry these boundary values are the rank-one elements — the minimal idempotents, the simplest zero divisors, and, in the degenerate case, the nilpotents. The final part of the article reads the polar data at the boundary.

The boundary has two strata: the nonzero complex multiples of the minimal idempotents, where the scalar part is nonzero, and the nilpotents, where it vanishes. Every minimal idempotent is $\tfrac12(e_t+\vec\Xi)$ with $\vec\Xi$ a pure root of $+1$, and the Hermitian ones, $\tfrac12(e_t+i\vec u)$ with $\vec u$ a real unit vector, form a sphere. The polar word reaches them at infinite rapidity with the scale collapsing; the rotor moves them to the other minimal idempotents, and the relative orientation of the boost and the rotor decides between the two strata. §*The Boundary of the Word* proves the three statements.

The article recalls the spectral data and the two analytic facts it uses (§*The Spectral Setting*), states the four exponentials and their ranges (§*The Decomposition*), proves existence and uniqueness (§*Existence and Uniqueness*), separates the Cartan logarithm from the single logarithm and describes the kernel and the fibre (§*The Logarithm*), reads the group law as the bracket of the two kinds of exponent (§*The Group Law*), gives the matrix picture (§*The Matrix Picture*), compares the three polar forms (§*The Three Polar Decompositions*), and reads the parameters as coordinates on the group of units (§*The Exponential Coordinates*). It then treats the boundary in one block: the null cone and its two strata, the minimal idempotents, the Hermitian idempotents and the sphere they form, the Peirce decomposition, the boundary limits of the word, the exponential limit and the action on the idempotents (§*The Boundary of the Word*). Two worked examples illustrate the interior and the boundary (§*Worked Examples* and §*Worked Examples at the Boundary*).

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_t,\vec e_x,\vec e_y,\vec e_z$, $\vec e_x\vec e_y=\vec e_z$, and central imaginary $i$, $i^{2}=-1$; a general element is $\tilde Q=Q_te_t+\vec Q$ with $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ and complex coefficients. The quaternion conjugation is $\tilde Q^{\natural}=Q_te_t-\vec Q$, the coefficientwise conjugation is $\overline{\tilde Q}=\overline{Q_t}e_t+\overline{\vec Q}$, and the Hermitian conjugation is $\tilde Q^{*}=\overline{\tilde Q^{\natural}}$. The norm is $\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}=\sum_{\mu}Q_\mu^{2}$, and $\tilde Q$ is invertible exactly when $\langle\tilde Q\rangle_{\natural}\neq0$. The matrix model is $\mathsf M_2:\mathbb{B}\to M_2(\mathbb{C})$, $\mathsf M_2(e_t)=I_2$, $\mathsf M_2(\vec e_k)=-i\sigma_k$, with $\det\mathsf M_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}$, $\operatorname{tr}\mathsf M_2(\tilde Q)=2Q_t$ and $\mathsf M_2(\tilde Q^{*})=\mathsf M_2(\tilde Q)^{\dagger}$. Every numerical value displayed below was recomputed in double precision.

## The Spectral Setting

The decomposition rests on two results of the category, and neither is proved again here: the eigenvalue decomposition of *Eigenvalue Decomposition of a Biquaternion* and the exponential and logarithm of *Biquaternion Elementary Functions*.

### The Eigenvalue Data

| quantity | value |
|---|---|
| element | $\tilde Q=Q_te_t+\vec Q$, with $Q_\mu\in\mathbb{C}$ |
| eigenvalues | $\lambda_\pm=Q_t\pm iB$, $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$ |
| eigenprojections | $\tilde\Pi_\pm=(\tilde Q-\lambda_\mp e_t)/(\lambda_\pm-\lambda_\mp)$, for $\lambda_+\neq\lambda_-$ |
| decomposition | $\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-$ in the distinct regime |
| norm | $\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}=\lambda_+\lambda_-$ |
| matrix model | $\mathsf M_2$, $\det\mathsf M_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}$, $\operatorname{tr}\mathsf M_2(\tilde Q)=2Q_t$ |
| units | $\langle\tilde Q\rangle_{\natural}\neq0$; the group is $\mathbb{B}^{\times}\cong\mathrm{GL}_2(\mathbb{C})$ |
| centre | $\mathbb{C}e_t$ |

These are the statements of *Eigenvalue Decomposition of a Biquaternion*, §*The Spectrum and the Characteristic Polynomial*, §*The Eigenprojections* and §*The Eigenvalue Decomposition*.

### The Regimes

The spectral data fall into five regimes. The table gives the spectral type and the logarithm of each; the rows marked boundary lie on the null cone and are excluded from the polar domain.

| Regime | Condition | Spectral type | Logarithm |
|---|---|---|---|
| Distinct | $B\neq0$, $\langle\tilde Q\rangle_{\natural}\neq0$ | two distinct eigenvalues, diagonalisable | two independent complex logarithms |
| Zero divisor, boundary | $B\neq0$, $\langle\tilde Q\rangle_{\natural}=0$ | two distinct eigenvalues, one zero; rank one | none: not a unit |
| Scalar | $B=0$, $\vec Q=0$, $Q_t\neq0$ | $\lambda_+=\lambda_-=Q_t$, central | the scalar logarithm, ambiguity $2\pi i\mathbb{Z}$ |
| Jordan | $B=0$, $\vec Q\neq0$, $Q_t\neq0$ | $\lambda_+=\lambda_-$, one Jordan block | the scalar logarithm, ambiguity $2\pi i\mathbb{Z}$; no lattice from the eigendirection |
| Nilpotent, boundary | $B=0$, $\vec Q\neq0$, $Q_t=0$ | one eigenvalue $0$, one Jordan block | none: not a unit |

The five rows are those of *Eigenvalue Decomposition of a Biquaternion*, §*Degenerate Regimes*. The zero element is the apex of the cone; it is not a unit and has no polar word. The regime decides the shape of the fibre of the exponential, and therefore the sense in which the polar parameters are unique.

### The Exponential and the Logarithm

| Property | Value |
|---|---|
| Closed form | $\exp(X_t)(\cos B\,e_t+\sin B\,\vec U)$ for $B\neq0$, and $\exp(X_t)(e_t+\tilde X)$ for $B=0$ |
| Image | the unit group $\mathbb{B}^{\times}$ |
| Kernel | the elements whose eigenvalues lie in $2\pi i\mathbb{Z}$; it is not a subgroup |
| Logarithm | exists for every unit, unique only after a branch |
| Principal domain | the arguments of $\lambda_\pm$ in $(-\pi,\pi]$ |
| Fibre | $\mathbb{Z}^{2}$ for distinct eigenvalues, continuous for a repeated diagonalisable eigenvalue, discrete for a Jordan block |

These are the statements of *Biquaternion Elementary Functions*, §*The Exponential* and §*The Logarithm*, and of *Eigenvalue Decomposition of a Biquaternion*, §*Degenerate Regimes*. The present article reads them as a product of four exponentials on the unit group.

## The Decomposition

### The Definition

**Definition.** An **exponential polar decomposition** of an invertible biquaternion $\tilde Q$ is a writing

$$
\tilde Q=r\,\exp(i\alpha)\,\exp\Bigl(i\frac{\psi}{2}\vec u_{\mathrm b}\Bigr)\,\exp\Bigl(\frac{\theta}{2}\vec u_{\mathrm r}\Bigr),
$$

with $r>0$, $\alpha\in(-\frac{\pi}{2},\frac{\pi}{2}]$, $\psi\ge0$, $\theta\in[0,2\pi]$, and unit vectors $\vec u_{\mathrm b},\vec u_{\mathrm r}\in\mathbb{R}^{3}$. The four factors are the **scale**, the **phase**, the **boost** and the **rotor**, in this order. The order matters: the scale and the phase are central and may be moved, but the boost and the rotor do not commute.

The ranges select one representative of each factor. The phase is half-open because the sign it leaves out is the rotor of angle $2\pi$; the rapidity is non-negative because the axis absorbs the sign; the rotor angle is closed because $\theta=0$ and $\theta=2\pi$ are the two signs of the identity.

### The Exponent and Its Four Components

The exponent is the sum of the four blocks,

$$
\tilde Q_{\log}=\ln r+i\alpha+i\frac{\psi}{2}\vec u_{\mathrm b}+\frac{\theta}{2}\vec u_{\mathrm r},
$$

one block for each factor. The table collects the data; the ranges are those of the definition.

| Block | Exponent | Range | Factor | Character |
|---|---|---|---|---|
| Scale $r$ | $\ln r$ | $\mathbb{R}$ | $\exp(\ln r)$ | central, non-compact, aperiodic |
| Phase $\zeta$ | $i\alpha$ | $(-\frac{\pi}{2},\frac{\pi}{2}]$ | $\cos\alpha+i\sin\alpha$ | central, compact, period $2\pi$ |
| Boost $\tilde U_{\mathrm b}$ | $i\frac{\psi}{2}\vec u_{\mathrm b}$ | $\psi\ge0$, $\lvert\vec u_{\mathrm b}\rvert=1$ | $\cosh\frac{\psi}{2}+i\sinh\frac{\psi}{2}\vec u_{\mathrm b}$ | Hermitian positive, non-compact, aperiodic |
| Rotor $\tilde u_{\mathrm r}$ | $\frac{\theta}{2}\vec u_{\mathrm r}$ | $\theta\in[0,2\pi]$, $\lvert\vec u_{\mathrm r}\rvert=1$ | $\cos\frac{\theta}{2}+\sin\frac{\theta}{2}\vec u_{\mathrm r}$ | unitary, compact; the rotation has period $2\pi$ |

The two central blocks $\ln r$ and $i\alpha$ lie in the centre $\mathbb{C}e_t$. The boost block lies in $\mathfrak p$ and the rotor block in $\mathfrak k$, the two summands of $\mathfrak{sl}(2,\mathbb{C})$ introduced in §*The Cartan Logarithm*. The four blocks do not commute in general, and the exponent is not a logarithm of $\tilde Q$; that is the subject of §*The Exponent and the Logarithm*.

### The Four Factors

Each factor is defined in *Biquaternion Elementary Functions*, and the paragraphs below record the closed forms and the parameter ranges used by the polar decomposition. The two central factors commute with everything and may be written on either side of the two non-central ones.

The scale is the positive real exponential

$$
r=\exp(\ln r),\qquad \ln r\in\mathbb{R},
$$

and it is central: it multiplies every element of the algebra by $r$ and every image of the sandwich by $r^{2}$. In the exponential picture it is the one central factor that is neither periodic nor bounded, and the logarithmic scale is the same in the quaternion case.

The phase is the central unitary exponential

$$
\zeta=\exp(i\alpha),\qquad \alpha\in\Bigl(-\frac{\pi}{2},\frac{\pi}{2}\Bigr],
$$

the branch of *Modulus–Unit Polar Decomposition of Biquaternions*: the closed right half of the unit circle with the point $-i$ removed. The interval is half-open and has length $\pi$, not $2\pi$, because the sign it leaves out is absorbed by the rotor; the element $-1$ is the rotor of angle $2\pi$, not a phase. The phase is periodic in $\alpha$ with period $2\pi$, and the branch selects one representative of each pair $\{\alpha,\alpha+\pi\}$ up to the central sign.

Their product is the complex modulus $\Rho=r\exp(i\alpha)$, with $r=\lvert\Rho\rvert$ and $\alpha=\arg\Rho$ in the branch.

Let $\vec u_{\mathrm b}$ be a unit vector of $\mathbb{R}^{3}$ and $\psi\ge0$. The **boost** is

$$
\tilde U_{\mathrm b}=\exp(i\frac{\psi}{2}\vec u_{\mathrm b})
=\cosh\frac{\psi}{2}\,e_t+i\sinh\frac{\psi}{2}\,\vec u_{\mathrm b}.
$$

The exponent is Hermitian and pure, $i\frac{\psi}{2}\vec u_{\mathrm b}$, and its square is the positive real number $\frac{\psi^{2}}{4}$:

$$
\Bigl(i\frac{\psi}{2}\vec u_{\mathrm b}\Bigr)^{2}
=-\frac{\psi^{2}}{4}\,\vec u_{\mathrm b}^{\,2}=\frac{\psi^{2}}{4}\,e_t,
$$

because $\vec u_{\mathrm b}^{\,2}=-e_t$. This is the hyperbolic case of the exponential: the argument $B$ of the closed form is $\pm i\frac{\psi}{2}$, purely imaginary, and the complex cosine and sine are the hyperbolic cosine and $i$ times the hyperbolic sine. The result is Hermitian, $\tilde U_{\mathrm b}^{*}=\tilde U_{\mathrm b}$, positive, of norm one, and unbounded as $\psi\to\infty$. It is not periodic, and $\psi\mapsto\tilde U_{\mathrm b}$ is injective on $[0,\infty)$.

The rapidity is recovered from the factor by

$$
\cosh\frac{\psi}{2}=\operatorname{Sc}\tilde U_{\mathrm b},\qquad
\sinh\frac{\psi}{2}=\bigl\lvert\operatorname{Vect}\tilde U_{\mathrm b}\bigr\rvert,
\qquad
\psi=2\operatorname{arcosh}\bigl(\operatorname{Sc}\tilde U_{\mathrm b}\bigr),
$$

the second identity because the vector part is $i\sinh\frac{\psi}{2}\vec u_{\mathrm b}$ and its coefficientwise modulus is $\sinh\frac{\psi}{2}$. The axis is the normalised vector part divided by $i$.

Let $\vec u_{\mathrm r}$ be a unit vector of $\mathbb{R}^{3}$ and $\theta\in[0,2\pi]$. The **rotor** is

$$
\tilde u_{\mathrm r}=\exp(\frac{\theta}{2}\vec u_{\mathrm r})
=\cos\frac{\theta}{2}\,e_t+\sin\frac{\theta}{2}\,\vec u_{\mathrm r}.
$$

The exponent is real and pure, $\frac{\theta}{2}\vec u_{\mathrm r}$, and its square is $-\frac{\theta^{2}}{4}e_t$: this is the circular case of the exponential, with $B=\pm\frac{\theta}{2}$, real, and the complex cosine and sine the ordinary ones. The result is a unit real quaternion, unitary as well as norm-one; the rotation it induces is periodic with period $2\pi$ in $\theta$, while the rotor itself is $4\pi$-periodic. The angle is recovered by

$$
\cos\frac{\theta}{2}=\operatorname{Sc}\tilde u_{\mathrm r},\qquad
\sin\frac{\theta}{2}=\bigl\lvert\operatorname{Vect}\tilde u_{\mathrm r}\bigr\rvert,
\qquad
\theta=2\arccos\bigl(\operatorname{Sc}\tilde u_{\mathrm r}\bigr),
$$

and the axis is the normalised vector part.

### One Exponential

The two central factors commute with the two non-central ones and with each other. The boost and the rotor commute exactly when their axes are parallel or antiparallel:

$$
\Bigl[i\frac{\psi}{2}\vec u_{\mathrm b},\frac{\theta}{2}\vec u_{\mathrm r}\Bigr]
=\frac{i\psi\theta}{4}\,[\vec u_{\mathrm b},\vec u_{\mathrm r}]
=\frac{i\psi\theta}{2}\,\vec u_{\mathrm b}\times\vec u_{\mathrm r},
$$

which vanishes exactly when $\vec u_{\mathrm b}\times\vec u_{\mathrm r}=0$, that is, when the axes are parallel or antiparallel, or one of the two parameters is zero. In that case, and only in that case, the four exponentials amalgamate into one:

$$
\tilde Q=\exp\Bigl(\ln r+i\alpha+\frac{\theta+i\psi}{2}\vec u\Bigr),
\qquad \vec u_{\mathrm b}=\vec u_{\mathrm r}=\vec u,
$$

with the complex angle $\frac{\theta+i\psi}{2}$ and $\vec u^{2}=-e_t$; for opposite axes, replace $\theta$ by $-\theta$. The right-hand side is the exponential of a single element, read through the complex cosine and sine. When the axes are not parallel, no single exponent of this shape exists, and the word stays a product.

## Existence and Uniqueness

**Theorem (the exponential polar decomposition).** Every invertible biquaternion $\tilde Q$ has a unique writing

$$
\tilde Q=r\,\exp(i\alpha)\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r},
$$

with $r>0$, $\alpha\in(-\frac{\pi}{2},\frac{\pi}{2}]$, $\tilde U_{\mathrm b}$ Hermitian positive of norm one, and $\tilde u_{\mathrm r}$ a unit real quaternion. Consequently it has the exponential writing above, with the rapidity $\psi\ge0$, the angle $\theta\in[0,2\pi]$, and the two axes; the axes are unique when $\psi>0$ and $\theta\notin\{0,2\pi\}$.

**Proof.** The algebraic statement is the theorem of *Modulus–Unit Polar Decomposition of Biquaternions*. For the exponential statement, write the unit factor as $\tilde U=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ with $\tilde U_{\mathrm b}$ Hermitian positive of norm one and $\tilde u_{\mathrm r}$ unitary of norm one. The matrix image of $\tilde U$ lies in $SL(2,\mathbb{C})$, and the two matrix images lie in the positive definite cone and in $SU(2)$; this is the global Cartan decomposition $SL(2,\mathbb{C})=P\cdot K$, which is unique because $P\cap K=\{e_t\}$. A Hermitian positive element of norm one is $\exp$ of a unique Hermitian traceless element, and a unitary element of determinant one is $\exp$ of an anti-Hermitian traceless element, with the angle $\theta\in[0,2\pi]$; the endpoint $\theta=2\pi$ is the central rotor $-1$, where the axis is undefined and the logarithm is not the principal one. The scale and the phase are the polar coordinates of the complex modulus, unique in the branch.

The theorem is the exponential form of the modulus–unit decomposition: the algebraic article gives the factors, and the Cartan decomposition gives the coordinates on the unit fibre. The count of parameters is

$$
\underbrace{1}_{\ln r}+\underbrace{1}_{\alpha}+\underbrace{1+2}_{\psi,\vec u_{\mathrm b}}+\underbrace{1+2}_{\theta,\vec u_{\mathrm r}}=8,
$$

the real dimension of $\mathbb{B}^{\times}$.

**Degeneracies.** The axis of the boost is undefined at $\psi=0$, where the boost is the identity, and the axis of the rotor is undefined at $\theta=0$, where the rotor is the identity, and at $\theta=2\pi$, where the rotor is $-e_t$ for every axis. These are the usual coordinate singularities of polar coordinates; the element itself is smooth there, and the word is unique. The angle $\theta=2\pi$ is the only point at which the rotor is central without being the identity, and it is the point the branch of the phase leaves to the rotor.

The parameters and their ranges are collected in one table.

| Parameter | Range | Unique? |
|---|---|---|
| $r$ | $(0,\infty)$ | yes |
| $\alpha$ | $(-\frac{\pi}{2},\frac{\pi}{2}]$ | yes: the branch |
| $\psi$ | $[0,\infty)$ | yes |
| $\vec u_{\mathrm b}$ | $S^{2}$ | no: undefined at $\psi=0$ |
| $\theta$ | $[0,2\pi]$ | yes |
| $\vec u_{\mathrm r}$ | $S^{2}$ | no: undefined at $\theta\in\{0,2\pi\}$ |

**The boundary.** The word is defined on the complement of the null cone. As an element approaches the cone, the scale vanishes and the rapidity diverges: the limit is a rank-one null element, either a complex multiple of a minimal idempotent or a nilpotent. The boundary is treated in §*The Boundary of the Word*. The polar word has no limit at the boundary; it has boundary values, reached with $r\to0$ and $\psi\to\infty$ at the rate $r\exp(\psi/2)\to R$ with $0<R<\infty$.

## The Logarithm

### The Cartan Logarithm

The first logarithm is a **pair**, not an element. Write the unit factor as $\tilde U=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ and put

$$
\tilde H=\operatorname{Log}\tilde U_{\mathrm b}=i\frac{\psi}{2}\vec u_{\mathrm b},
\qquad
\tilde K=\operatorname{Log}\tilde u_{\mathrm r}=\frac{\theta}{2}\vec u_{\mathrm r}.
$$

The pair $(\tilde H,\tilde K)$ is the **Cartan logarithm** of $\tilde U$. It is unique with the ranges of the theorem, except at the central rotor $-e_t$, where the axis is undefined. It consists of a Hermitian traceless element and an anti-Hermitian traceless element, and it satisfies

$$
\tilde U=\exp(\tilde H)\exp(\tilde K).
$$

The name is the one of the Cartan decomposition: the Lie algebra of $SL(2,\mathbb{C})$ splits as

$$
\mathfrak{sl}(2,\mathbb{C})=\mathfrak{k}\oplus\mathfrak{p},
\qquad
\mathfrak{k}=\{\tilde X:\tilde X^{*}=-\tilde X,\ \operatorname{Sc}\tilde X=0\},
\qquad
\mathfrak{p}=\{\tilde X:\tilde X^{*}=\tilde X,\ \operatorname{Sc}\tilde X=0\},
$$

of real dimensions $3$ and $3$. The rotor exponent lies in $\mathfrak{k}$, the boost exponent in $\mathfrak{p}$, and the group decomposition $SL(2,\mathbb{C})=\exp(\mathfrak p)\exp(\mathfrak k)$ is global and unique. The full algebra splits as

$$
\mathbb{B}=\mathbb{R}e_t\ \oplus\ i\mathbb{R}e_t\ \oplus\ \mathfrak p\ \oplus\ \mathfrak k,
$$

with the scale exponent in the first summand, the phase exponent in the second, the boost exponent in the third and the rotor exponent in the fourth. This is the exponential reading of the four coordinate blocks of *The Polar Decomposition and Remarkable Subspaces*.

### The Single Logarithm

The second logarithm is an element. Since $\mathbb{B}\cong M_2(\mathbb{C})$ and every invertible complex matrix has a logarithm, the exponential

$$
\exp:\mathbb{B}\longrightarrow\mathbb{B}^{\times}
$$

is surjective. For every invertible $\tilde Q$ there is an element $\operatorname{Log}\tilde Q$ with

$$
\exp\bigl(\operatorname{Log}\tilde Q\bigr)=\tilde Q,
$$

and it is unique only after a branch is fixed.

A single logarithm is related to the Cartan logarithm by

$$
\operatorname{Log}\tilde Q=\ln r+i\alpha+\operatorname{Log}\bigl(\tilde U_{\mathrm b}\tilde u_{\mathrm r}\bigr)
$$

for a compatible choice of branches; the principal branch of $\tilde Q$ may differ from the sum by $2\pi i$ times an integer combination of the eigenprojections. The last term is a logarithm of the unit factor inside $\mathfrak{gl}(2,\mathbb{C})$, not inside $\mathfrak{sl}(2,\mathbb{C})$: its trace may be a nonzero multiple of $2\pi i$, and this trace obstruction is what makes the norm-one group not globally exponential even though the group of units is.

### The Principal Logarithm

The principal branch is fixed by the eigenvalues. By *Eigenvalue Decomposition of a Biquaternion*, §*The Spectrum and the Characteristic Polynomial* and §*Degenerate Regimes*, the matrix image has eigenvalues

$$
\lambda_\pm=Q_t\pm iB,\qquad B=\sqrt{Q_x^{2}+Q_y^{2}+Q_z^{2}},
$$

and the principal logarithm takes the arguments of $\lambda_\pm$ in $(-\pi,\pi]$. The eigenvalues may coincide, and then the matrix may fail to be diagonalisable; the logarithm still exists, and it is computed on the Jordan form, as the example below shows.

The cut is the set of units with an eigenvalue on $(-\infty,0)$. On the cut the principal argument jumps from $\pi$ to $-\pi$, and the principal logarithm jumps by $\pm2\pi i$ times the eigenprojection of the eigenvalue that crosses the cut, the sign depending on the direction of the crossing; in the Jordan case there is one eigenvalue and the jump is $\pm2\pi i\,e_t$. The principal logarithm is real-analytic on the complement of the cut, and on the distinct regime it is the branch used in the rest of the article.

### The Kernel and the Fibre

The exponential is not injective. Its kernel is the set of exponents that exponentiate to the identity. The elementary article computes it: $\exp(\tilde X)=e_t$ exactly when $\tilde X$ is diagonalisable over $\mathbb{C}$ and every eigenvalue lies in $2\pi i\mathbb{Z}$. In the algebra the kernel contains

| exponent | exponential | reason |
|---|---|---|
| $2\pi i\,e_t$ | $e_t$ | the complex period of the phase |
| $2\pi\vec U$, $\vec U^{2}=-e_t$ | $e_t$ | a period on a pure root of $-1$, $\cos2\pi=1$ and $\sin2\pi=0$ |
| $\pi i\,e_t+\pi\vec U$ | $e_t$ | the two eigenvalues $\pi i(1\pm1)$ are multiples of $2\pi i$ |
| $2\pi i k\,e_t+2\pi j\vec U$ | $e_t$ | the sum of two commuting periods |

The kernel is **not a subgroup**. It is not closed under addition, because $\exp$ is not a homomorphism: the sum of two kernel elements need not lie in the kernel. It is a union of conjugacy classes of the diagonal matrices $\operatorname{diag}(2\pi i m,2\pi i n)$, and it meets the null cone: the element $\pi i e_t+\pi\vec e_z$ has norm zero and exponentiates to the identity.

The fibre over an element is not a coset of the kernel either. For an element with distinct eigenvalues $\lambda_\pm$ and eigenprojections $\tilde\Pi_\pm$ (*Eigenvalue Decomposition of a Biquaternion*, §*The Eigenvalue Decomposition*), the logarithms are

$$
\operatorname{Log}\tilde Q+2\pi i\bigl(k\tilde\Pi_+ + l\tilde\Pi_-\bigr),
\qquad k,l\in\mathbb{Z},
$$

a copy of the lattice $2\pi i\mathbb{Z}^{2}$, one integer coordinate for each eigendirection. For a diagonalisable element with a repeated eigenvalue the fibre contains a continuous family of conjugates, because the two eigenvalues of the logarithm may differ by $2\pi i$; for a non-diagonalisable Jordan block it is discrete, one point for each choice of the logarithm of the scalar eigenvalue. The polar parameters do not cut the fibre of the exponential to one point: the four exponents sum to the formal exponent, which is not a logarithm. What they cut to one point, up to the degeneracies of the axes, is the fibre of the **word map** $(r,\alpha,\psi,\vec u_{\mathrm b},\theta,\vec u_{\mathrm r})\mapsto r \exp(i\alpha)\tilde U_{\mathrm b}\tilde u_{\mathrm r}$: $r$ by positivity, $\alpha$ by the branch, $\psi$ by $\psi\ge0$, and $\theta$ by $[0,2\pi]$. The exponential polar decomposition is therefore a **section** of the word map, a global parametrization of $\mathbb{B}^{\times}$; it is neither a section of the exponential nor a quotient.

### The Exponent and the Logarithm

The sum of the four exponents is the **formal exponent**

$$
\tilde Q_{\log}=\ln r+i\alpha+i\frac{\psi}{2}\vec u_{\mathrm b}+\frac{\theta}{2}\vec u_{\mathrm r}.
$$

It is the element the quaternion case would call the logarithm. Here it is not one:

$$
\exp\bigl(\tilde Q_{\log}\bigr)\neq\tilde Q
\qquad\text{unless}\qquad
[\vec u_{\mathrm b},\vec u_{\mathrm r}]=0\quad\text{or}\quad\psi\theta=0.
$$

The defect is the Baker–Campbell–Hausdorff correction. To first order,

$$
\operatorname{Log}\bigl(\exp(\tilde H)\exp(\tilde K)\bigr)
=\tilde H+\tilde K+\tfrac12[\tilde H,\tilde K]+\cdots,
$$

and the first correction is again a boost, because

$$
\tfrac12[\tilde H,\tilde K]
=\frac{i\psi\theta}{4}\,\vec u_{\mathrm b}\times\vec u_{\mathrm r}
\in\mathfrak p .
$$

So the sum of a boost and a rotor exponent is corrected by another boost, and the true logarithm is not the sum of the four exponents. The correction vanishes exactly when the axes are parallel or antiparallel, or one of the two parameters vanishes, which is the amalgamation of §*One Exponential*. The higher terms are the iterated commutators; the series is the one of *Biquaternion Lie Group and Exponential Structure*, §*The Correspondence with the Lie Algebra*.

The defect is not a rounding effect. In the worked example below the four exponents sum to an element whose exponential misses the element by $0.54$ in the largest coefficient, while the true logarithm reproduces it to $2.2\times10^{-16}$.

## The Group Law

The product of two words is

$$
\bigl(r_1\exp(i\alpha_1)\exp(\tilde H_1)\exp(\tilde K_1)\bigr)
\bigl(r_2\exp(i\alpha_2)\exp(\tilde H_2)\exp(\tilde K_2)\bigr)
=r_1r_2\,\exp(i(\alpha_1+\alpha_2))\,\exp(\tilde H_1)\exp(\tilde K_1)\exp(\tilde H_2)\exp(\tilde K_2).
$$

The central factors add. The non-central ones do not: the middle product $\exp(\tilde K_1)\exp(\tilde H_2)$ has to be re-split as a boost times a rotor, and the re-splitting is the Cartan decomposition of a product of two exponentials. The first correction is the commutator,

$$
\exp(\tilde K_1)\exp(\tilde H_2)
=\exp(\tilde H_2+[\tilde K_1,\tilde H_2]+\cdots)\exp(\tilde K_1+\cdots),
$$

so the rotor of the first word changes the boost of the second by a term in $\mathfrak p$: the boost is conjugated, not added. The rotor itself is unchanged at second order; its correction is of higher order. The parameters of the product are not the sums of the parameters.

The brackets of the two summands close as a **symmetric pair**:

| bracket | lies in | reading |
|---|---|---|
| $[\mathfrak k,\mathfrak k]$ | $\mathfrak k$ | two rotors compose to a rotor |
| $[\mathfrak p,\mathfrak p]$ | $\mathfrak k$ | two boosts compose to a boost times a rotor |
| $[\mathfrak k,\mathfrak p]$ | $\mathfrak p$ | the commutator of a rotor and a boost is a boost |

The first row is the subgroup $SU(2)$ of the rotor. The second is the Thomas–Wigner rotation: the product of two boosts is a boost times a rotor, and the residual rotor is the one computed in *The Polar Decomposition and Remarkable Subspaces*, §*The Boost Family and the Rotor Group*. The third is the statement that the boost set is a symmetric space and not a group: the commutator of an infinitesimal boost and an infinitesimal rotation is an infinitesimal boost, so the boost directions are stable under the adjoint action of the rotor, while the boost set itself is not closed under multiplication. The four factors obey the following laws.

| Data | Law |
|---|---|
| Scale and phase | multiply |
| Boost | conjugated by the rotor, not added |
| Rotor | multiplies |
| Exponent | does not add: the Baker–Campbell–Hausdorff correction |
| Group | $\mathbb{B}^{\times}\cong\mathrm{GL}_2(\mathbb{C})$, generated by the scalars and $SL(2,\mathbb{C})$ |

## The Matrix Picture

The matrix model turns the exponential into the matrix exponential, because $\mathsf M_2$ is a $\mathbb{C}$-algebra homomorphism:

$$
\mathsf M_2\bigl(\exp\tilde X\bigr)=\exp\bigl(\mathsf M_2(\tilde X)\bigr).
$$

The polar word becomes the polar decomposition of $\mathrm{GL}_2(\mathbb{C})$,

$$
\mathsf M_2(\tilde Q)=r\,\exp(i\alpha)\,\mathsf M_2(\tilde U_{\mathrm b})\,\mathsf M_2(\tilde u_{\mathrm r}),
$$

with $\mathsf M_2(\tilde U_{\mathrm b})$ positive definite of determinant one and $\mathsf M_2(\tilde u_{\mathrm r})$ unitary of determinant one. The four exponents are the four summands of the decomposition of the Lie algebra

$$
\mathfrak{gl}_2(\mathbb{C})=\mathfrak{u}(2)\oplus\mathfrak{H},
\qquad
\mathfrak{u}(2)=\{X:X^{\dagger}=-X\},
\qquad
\mathfrak{H}=\{X:X^{\dagger}=X\},
$$

of real dimensions $4$ and $4$. The exponents of the scale and the boost lie in $\mathfrak H$, those of the phase and the rotor in $\mathfrak u(2)$; the central real line is the scale, the central imaginary line is the phase, and the traceless parts are the boost and the rotor.

| matrix object | algebra object | dimension | factor |
|---|---|---|---|
| positive determinant-one matrix | Hermitian positive unit-norm element | $3$ | boost |
| unitary determinant-one matrix | unit real quaternion | $3$ | rotor |
| positive real scalar | scale | $1$ | $r$ |
| unit complex scalar | phase | $1$ | $\zeta$ |

The exponential is surjective onto $\mathrm{GL}_2(\mathbb{C})$ because every invertible matrix has a logarithm, and it is not injective because the logarithm is multivalued. The determinant gives

$$
\det\mathsf M_2\bigl(\exp\tilde X\bigr)=\exp\bigl(\operatorname{tr}\mathsf M_2(\tilde X)\bigr)\neq0,
$$

so the image lies in the units, and the trace is the logarithmic scale of the determinant. By *Eigenvalue Decomposition of a Biquaternion*, §*The Spectrum and the Characteristic Polynomial* and §*Degenerate Regimes*, the eigenvalues of $\mathsf M_2(\tilde Q)$ are $Q_t\pm iB$, and the Jordan type at $B=0$ decides the shape of the fibre: distinct eigenvalues give two integer lattices, one for each eigenvalue; a double eigenvalue with a nontrivial Jordan block gives a discrete family; and a scalar matrix gives a continuous family of conjugates.

## The Three Polar Decompositions

The exponential form is one of three presentations of the same factorisation. The algebraic word $\tilde Q=\Rho\tilde U$ of *Modulus–Unit Polar Decomposition of Biquaternions* is the coarsest; the Cartan form splits the unit factor into a Hermitian positive factor and a unitary factor; the exponential form writes each factor as an exponential. The three agree on the element and differ in the functions they use and in the group law.

### The Three Forms

| decomposition | formula | parameters | domain | uniqueness | functions | group reading |
|---|---|---|---|---|---|---|
| modulus–unit | $\tilde Q=\Rho\tilde U$ | $\Rho=r\exp(i\alpha)\in\mathbb{C}^{\times}$, $\tilde U\in SL(2,\mathbb{C})$ | all units | unique | complex polar coordinates | $\mathbb{C}^{\times}\times SL(2,\mathbb{C})$ |
| Cartan | $\tilde Q=r\zeta\,\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | $r>0$, $\alpha$, $\psi$, $\vec u_{\mathrm b}$, $\theta$, $\vec u_{\mathrm r}$ | all units | unique factors; axes degenerate | square roots | $P\cdot K$ |
| exponential | each factor written $\exp$ | the same six data | all units | unique word; axes degenerate | exponential and logarithm | four exponents |

### The Modulus–Unit Form

The modulus–unit form writes $\tilde Q=\Rho\tilde U$ with $\Rho=r\exp(i\alpha)\in\mathbb{C}^{\times}$ and $\tilde U=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ of norm one. The complex modulus carries the scale and the central phase; the unit factor carries the six remaining real dimensions. It is global, algebraic and unique, and it is the form from which the other two are read.

### The Cartan Form

The Cartan form is the split $\tilde U=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ of the unit factor into a Hermitian positive element of norm one and a unit real quaternion. In the matrix model it is $SL(2,\mathbb{C})=P\cdot K$, unique because $P\cap K=\{e_t\}$. It is algebraic and parameter-free: the two factors are determined by $\tilde U$, and the rapidity and angle are their polar coordinates.

### The Exponential Form

The exponential form writes each of the four factors as an exponential,

$$
r=\exp(\ln r),\qquad \zeta=\exp(i\alpha),\qquad
\tilde U_{\mathrm b}=\exp(i\frac{\psi}{2}\vec u_{\mathrm b}),\qquad
\tilde u_{\mathrm r}=\exp(\frac{\theta}{2}\vec u_{\mathrm r}),
$$

and multiplies them in the order scale, phase, boost, rotor. It is the transcendental coordinate on the Cartan form. Its four exponents do not add: the boost and the rotor exponents do not commute, and the single logarithm differs from their sum by the Baker–Campbell–Hausdorff correction of §*The Exponent and the Logarithm*.

### What the Comparison Says

The modulus–unit form is the coarsest and the most algebraic. The Cartan form is the finest algebraic split, and the form that identifies the two real forms of the Lie algebra. The exponential form is the only one that names a logarithm of the element; it is global because every invertible matrix has a logarithm, but it is neither a homomorphism nor unique. The four parameters select a canonical word, not a canonical logarithm.

| Property | Modulus–unit | Cartan | Exponential |
|---|---|---|---|
| Algebraic or transcendental | algebraic | algebraic | transcendental |
| Global on the units | yes | yes | yes |
| Unique without a choice | yes | yes | up to the axis degeneracies |
| Non-uniqueness | none | none | the axis degeneracies |
| Group law | multiplication of the factors | re-splitting of $P$ and $K$ | Baker–Campbell–Hausdorff |
| Logarithm | none: a square root is used | the Cartan pair | the single logarithm, multivalued |

## The Exponential Coordinates

### The Coordinate Map

The four parameters are coordinates on the group of units, and their ranges make the map a bijection up to the degeneracies of the axes. The coordinate lines are the four one-parameter families:

- the **scale line** $r\mapsto r\exp(i\alpha)\tilde U_{\mathrm b}\tilde u_{\mathrm r}$, a half-line, non-compact;
- the **phase circle** $\alpha\mapsto r \exp(i\alpha)\tilde U_{\mathrm b}\tilde u_{\mathrm r}$, a circle of length $2\pi$ before the branch cuts it to $\pi$;
- the **boost hyperbola** $\psi\mapsto r \exp(i\alpha)\exp(i\frac{\psi}{2}\vec u_{\mathrm b})\tilde u_{\mathrm r}$, a non-compact ray;
- the **rotor arc** $\theta\mapsto r \exp(i\alpha)\tilde U_{\mathrm b}\exp(\frac{\theta}{2}\vec u_{\mathrm r})$, a great semicircle from $e_t$ to $-e_t$.

### The Topology

The topology is read from the polar decomposition, not from the word. The positive cone $P$ is homeomorphic to $\mathbb{R}^{3}$ and the rotor sphere $K=SU(2)$ is $S^{3}$, so

$$
SL(2,\mathbb{C})\simeq \mathbb{R}^{3}\times S^{3}.
$$

The group of units retracts onto $U(2)$, and the determinant splits $U(2)\cong U(1)\times SU(2)$ as a space, so

$$
\mathbb{B}^{\times}\simeq U(2)\cong S^{1}\times S^{3}.
$$

The branch of the modulus makes $\tilde Q\mapsto(\Rho,\tilde U)$ a bijection onto $\mathcal H\times SL(2,\mathbb{C})$, but not a homeomorphism: on the cut the phase jumps by the factor $-1$ and the rotor changes sign, so the circular direction is carried by the phase, and the branch coordinate does not see it continuously. The fundamental group of the group of units is therefore $\mathbb{Z}$, carried by the phase alone; the rotor contributes the simply connected factor $S^{3}$, and the scale and the boost are the two non-compact directions. This is the exponential reading of the homotopy statement of *Modulus–Unit Polar Decomposition of Biquaternions*, §*The Group of Units and the Unitary Group*.

### The Conformal Factor

The **conformal factor** of the action is also read in the coordinates. The sandwich of $\tilde Q$ multiplies the quadratic form of either half by

$$
r^{4}=\exp(4\ln r)=\bigl\lvert\langle\tilde Q\rangle_{\natural}\bigr\rvert^{2},
$$

so lengths are multiplied by $r^{2}=\lvert\langle\tilde Q\rangle_{\natural}\rvert$. The scale exponent is thus a quarter of the logarithm of the conformal factor: the form scales by $\exp(4\ln r)$ and lengths by $\exp(2\ln r)$. The phase, the boost and the rotor are isometries of the form; only the scale moves it.

## The Boundary of the Word

The word is defined on the complement of the null cone. On the cone the rapidity diverges, the scale collapses, and the word has boundary values rather than a value. The nonzero elements of the cone are the rank-one elements: the minimal idempotents and the nilpotents. Their classification is that of *Square Roots of One and the Idempotents of the Biquaternion Algebra* and *Eigenvalue Decomposition of a Biquaternion*; this section reads them as the boundary of the polar word.

### The Null Cone and Its Two Strata

The **null cone** is the zero set of the norm,

$$
\mathcal N=\{\tilde Q\in\mathbb{B}:\langle\tilde Q\rangle_{\natural}=0\}.
$$

It is one complex equation, hence two real equations on the eight real dimensions of the algebra: a cone of real dimension six. In the matrix model it is the determinant-zero set, so its nonzero elements are exactly the rank-one matrices. These are exactly the zero divisors of the algebra, by the criterion of *Norm and Invertibility in the General Quaternionic Algebra*: a nonzero element is a zero divisor if and only if its norm vanishes.

The scalar part cuts the cone into two strata.

**Theorem (the two strata).** Let $\tilde Q\neq0$ with $\langle\tilde Q\rangle_{\natural}=0$.

1. If $Q_t\neq0$, then $\tilde Q=2Q_t\,\tilde\Pi$ with

    $$
    \tilde\Pi=\frac{\tilde Q}{2Q_t},
    \qquad \tilde\Pi^{2}=\tilde\Pi,\qquad \tilde\Pi\neq0,\quad \tilde\Pi\neq e_t,
    $$

    a minimal idempotent. The scalar part of $\tilde\Pi$ is $\tfrac12$, its matrix image has trace $1$ and rank $1$, and $\tilde Q$ is a nonzero complex multiple of a minimal idempotent.
2. If $Q_t=0$, then $\tilde Q$ is a **nilpotent**, $\tilde Q^{2}=0$, with a purely vector, isotropic part: $\tilde Q=\vec Q$ and $\langle\vec Q\rangle_{\natural}=\vec Q\cdot\vec Q=0$.

**Proof.** In the matrix model, $\langle\tilde Q\rangle_{\natural}=\det\mathsf M_2(\tilde Q)$, so a nonzero null element has rank one. If $Q_t\neq0$ then the trace $2Q_t$ is nonzero, and the Cayley–Hamilton identity for a rank-one matrix gives $\mathsf M_2(\tilde Q)^{2}=\operatorname{tr}\mathsf M_2(\tilde Q)\,\mathsf M_2(\tilde Q)$, that is, $\tilde Q^{2}=2Q_t\tilde Q$; dividing by $2Q_t$ gives $\tilde\Pi^{2}=\tilde\Pi$, and $\tilde\Pi\neq0,e_t$ because $\tilde Q$ has rank one and trace $1$. The vanishing of the norm of $\tilde\Pi$ is the corollary of the classification below. If $Q_t=0$ then $\tilde Q^{2}=\vec Q^{2}=-\langle\vec Q\rangle_{\natural}e_t=0$, and the vector part is isotropic.

The two strata have different dimensions and different normal forms.

| stratum | condition | normal form | real dimension | matrix normal form |
|---|---|---|---|---|
| idempotent | $Q_t\neq0$ | $\tilde Q=2Q_t\tilde\Pi$, $\tilde\Pi^{2}=\tilde\Pi$ | $6$ | $cE_{11}$, $c\neq0$ |
| nilpotent | $Q_t=0$ | $\tilde Q=N$, $N^{2}=0$ | $4$ | $cE_{12}$, $c\neq0$ |

The idempotent stratum is open and dense in the cone; the nilpotent stratum is a closed subvariety of it, of real codimension two, and it lies in the closure of the idempotent stratum. The two strata are nevertheless disjoint, and the scalar part distinguishes them pointwise.

The scalar part is therefore the exact invariant that separates the two kinds of boundary point. This is the boundary form of the trichotomy of the exponential: a root of $-1$ lies in the interior, a nilpotent has square zero, and an idempotent is $\tfrac12(e_t+\vec\Xi)$ with $\vec\Xi$ a pure root of $+1$. The three values of the square are the three behaviours of the exponential, and the two behaviours that degenerate at the boundary are the two strata of the cone.

### The Minimal Idempotents

**Definition.** An **idempotent** is an element $\tilde\Pi\neq0$ with $\tilde\Pi^{2}=\tilde\Pi$. It is **minimal** when $\tilde\Pi\neq e_t$. The minimal idempotents of $\mathbb{B}$ are the rank-one projections of the matrix model.

**Theorem (the classification).** The minimal idempotents of $\mathbb{B}$ are exactly the elements

$$
\tilde\Pi=\frac{1}{2}\bigl(e_t+\vec\Xi\bigr),
\qquad \vec\Xi^{2}=e_t,\quad \vec\Xi\neq\pm e_t ,
$$

with $\vec\Xi$ a pure root of $+1$.

This is *Square Roots of One and the Idempotents of the Biquaternion Algebra*, §*The Classification of the Idempotents* and §*The Correspondence With the Roots of One*, restricted to the roots other than $\pm e_t$: the halving map $\vec\Xi\mapsto\tfrac12(e_t+\vec\Xi)$ is a bijection onto the minimal idempotents, with inverse $\vec\Xi=2\tilde\Pi-e_t$.

**Corollary (the norm is zero).** Every minimal idempotent has norm zero, $\tilde\Pi\tilde\Pi^{\natural}=0$. This is the zero-divisor property of the non-trivial idempotents, *Square Roots of One and the Idempotents of the Biquaternion Algebra*, §*Idempotents and the Non-Pure Zero Divisors*.

The two idempotents attached to one root are $\tilde\Pi_{+}=\tfrac12(e_t+\vec\Xi)$ and $\tilde\Pi_{-}=\tfrac12(e_t-\vec\Xi)$; they satisfy

$$
\tilde\Pi_{+}+\tilde\Pi_{-}=e_t,\qquad
\tilde\Pi_{+}\tilde\Pi_{-}=0,\qquad
\tilde\Pi_{\pm}^{2}=\tilde\Pi_{\pm},
$$

the relations of a pair of complementary projections. In the matrix model they are conjugate to $E_{11}$ and $E_{22}$.

**The root of a projection.** The element $\vec\Xi=2\tilde\Pi-e_t$ is the root attached to $\tilde\Pi$, and $\tilde\Pi\mapsto\vec\Xi$ is a bijection onto the pure roots other than $\pm e_t$. The Hermitian idempotents are the case $\vec\Xi=i\vec u$ with $\vec u$ a real unit vector, where the pair $\{\tilde\Pi_{+},\tilde\Pi_{-}\}$ determines $\vec u$ up to sign. The left annihilator of $\tilde\Pi_{+}$ is the left ideal $\mathbb{B}\tilde\Pi_{-}$, the second column in the matrix model; the left annihilator of $\tilde\Pi_{-}$ is $\mathbb{B}\tilde\Pi_{+}$, the first column.

### The Hermitian Idempotents and the Sphere

The minimal idempotents that are fixed by the star are the **Hermitian idempotents**: $\tilde\Pi^{*}=\tilde\Pi$. By the classification they are exactly those with $\vec\Xi=i\vec u$ for a **real** unit vector $\vec u$:

$$
\tilde\Pi_{+}=\frac{1}{2}\bigl(e_t+i\vec u\bigr),
\qquad \vec u\in S^{2}.
$$

The star of the idempotent is

$$
\tilde\Pi_{+}^{*}=\frac12\bigl(e_t+(i\vec u)^{*}\bigr)
=\frac12\bigl(e_t+i\vec u\bigr)=\tilde\Pi_{+},
$$

because $(i\vec u)^{*}=i\vec u$ for a real vector: the quaternion conjugation negates the vector, and the coefficientwise conjugation negates the factor $i$, and the two signs cancel.

**Theorem (the sphere).** The map $\vec u\mapsto\tfrac12(e_t+i\vec u)$ is a diffeomorphism from $S^{2}$ onto the set of Hermitian minimal idempotents. The inverse is $\vec u=-i(2\tilde\Pi-e_t)$.

**Proof.** The map is smooth and injective, since $2\tilde\Pi-e_t=i\vec u$ recovers $\vec u$. It is surjective by the classification and the reality of $\vec u$, and its inverse is the restriction of the affine map $\tilde\Pi\mapsto-i(2\tilde\Pi-e_t)$, which is smooth. A smooth bijection with a smooth inverse is a diffeomorphism.

The Hermitian idempotents are the **pure states** of the algebra: rank-one projections, of trace one, positive semidefinite, with $\tilde\Pi^{2}=\tilde\Pi=\tilde\Pi^{*}$. The matrix image is

$$
\mathsf M_2(\tilde\Pi_{+})=\frac12\bigl(I_2+\vec u\cdot\boldsymbol\sigma\bigr),
$$

the density matrix of a spin state with Bloch vector $\vec u$. The Bloch sphere of the two-level system is therefore the set of Hermitian minimal idempotents of the biquaternion algebra; the physical interpretation is that of *The Informational Sector: States, Observables and Probability*, and the mathematics uses only the algebra.

The same sphere is the **celestial sphere**. A future-pointing null element of the anti-Hermitian half is $\tilde Q_-=ia\,e_t+\vec b$ with $a=\lvert\vec b\rvert>0$. Its matrix image is $iA$ with $A=aI_2-\vec b\cdot\boldsymbol\sigma$, of rank one and trace $2a$, so $-i\mathsf M_2(\tilde Q_-)/(2a)=A/(2a)$ is a Hermitian minimal idempotent, and

$$
\frac{-i\,\mathsf M_2(\tilde Q_-)}{2a}
=\frac{A}{2a}
=\frac12\Bigl(I_2-\frac{\vec b}{a}\cdot\boldsymbol\sigma\Bigr)
=\mathsf M_2\Bigl(\frac12\bigl(e_t+i\vec u\bigr)\Bigr),
\qquad \vec u=-\frac{\vec b}{a}.
$$

The null direction is the point $\vec u$ of the sphere, and the scale $a$ is forgotten: the celestial sphere of null directions is the set of Hermitian idempotents. The two signs of $\vec u$ correspond to the two idempotents $\tilde\Pi_{\pm}$, that is, to the two antipodal points $\pm\vec u$ of the celestial sphere. The projective statement, with the Möbius action, is in *Biquaternion Lorentzian and Conformal Geometry*.

**The conjugations.** For $\vec u$ real,

$$
\tilde\Pi_{+}^{\natural}=\tilde\Pi_{-},\qquad
\overline{\tilde\Pi_{+}}=\tilde\Pi_{-},\qquad
\tilde\Pi_{+}^{*}=\tilde\Pi_{+}.
$$

The quaternion conjugation and the coefficientwise conjugation both exchange the two idempotents of the pair; the star fixes each. On the Hermitian idempotents the two real structures $\natural$ and $\overline{\phantom{Q}}$ agree, and the star is the involution that selects them.

### The Peirce Decomposition

Let $\tilde\Pi$ be a minimal idempotent and $\tilde\Pi'=e_t-\tilde\Pi$ its complement. The **Peirce decomposition** relative to $\tilde\Pi$ is

$$
\mathbb{B}
=\tilde\Pi\mathbb{B}\tilde\Pi\ \oplus\ \tilde\Pi\mathbb{B}\tilde\Pi'\ \oplus\ \tilde\Pi'\mathbb{B}\tilde\Pi\ \oplus\ \tilde\Pi'\mathbb{B}\tilde\Pi',
$$

four complex lines. This is the decomposition of *Eigenvalue Decomposition of a Biquaternion*, §*The Peirce Decomposition Relative to the Eigenprojection*: the diagonal part is the centraliser $\mathbb{C}[\tilde Q]$ of any element with eigenprojections $\tilde\Pi,\tilde\Pi'$, and the two mixed corners are the directions that fail to commute with $\tilde Q$. The multiplication table, the minimal left and right ideals and the classification of the nilpotents are in *Ideals and Peirce Decomposition of the Biquaternion Algebra* and *Hermitian Idempotents and the Peirce Decomposition*; they are not repeated here. Only two facts are used below: the mixed corners are nilpotent directions, and for a Hermitian pair the coefficientwise conjugation exchanges them.

### The Boundary Limits

The polar word has no value on the cone, but it has a boundary behaviour, and the boundary behaviour produces exactly the two strata.

**Theorem (the boundary limits).** Let $\vec u_{\mathrm b}$ and $\vec u_{\mathrm r}$ be unit vectors, $\zeta$ a unit complex number and $R>0$, and let

$$
\tilde Q(\psi)=R\,\exp(-\frac{\psi}{2})\,\zeta\,\exp(i\frac{\psi}{2}\vec u_{\mathrm b})\,\tilde u_{\mathrm r},
\qquad \psi>0 .
$$

Then $\tilde Q(\psi)$ is invertible for every $\psi$, and

$$
\tilde Q(\psi)\longrightarrow
\frac{R\zeta}{2}\bigl(e_t+i\vec u_{\mathrm b}\bigr)\tilde u_{\mathrm r}
\qquad(\psi\to\infty),
$$

a nonzero null element of rank one. It is a complex multiple of a minimal idempotent when $\tilde u_{\mathrm r}$ does not anticommute with $\vec u_{\mathrm b}$, and it is a nilpotent exactly when $\tilde u_{\mathrm r}$ anticommutes with $\vec u_{\mathrm b}$.

**Proof.** The closed form of the boost gives

$$
\exp(-\frac{\psi}{2})\exp(i\frac{\psi}{2}\vec u_{\mathrm b})
=\frac{1+\exp(-\psi)}{2}e_t+\frac{1-\exp(-\psi)}{2}\,i\vec u_{\mathrm b}
\longrightarrow \frac12\bigl(e_t+i\vec u_{\mathrm b}\bigr).
$$

The norm of the limit is zero by the corollary of the classification, and its matrix image has rank one because the first factor has rank one and $\tilde u_{\mathrm r}$ is invertible. Write $\tilde u_{\mathrm r}=a\,e_t+b\,\vec u_{\mathrm b}+\tilde u_{\perp}$ with $a,b\in\mathbb{R}$ and $\tilde u_{\perp}$ a real vector orthogonal to $\vec u_{\mathrm b}$. Then $\operatorname{tr}\mathsf M_2(\tilde u_{\mathrm r})=2a$ and $\operatorname{tr}\mathsf M_2(\vec u_{\mathrm b}\tilde u_{\mathrm r})=-2b$, so

$$
\operatorname{tr}\mathsf M_2\bigl(\tilde Q(\infty)\bigr)
=R\zeta\,(a-ib).
$$

A rank-one matrix $L$ satisfies $L^{2}=(\operatorname{tr}L)L$ by Cayley–Hamilton. Hence, if $a-ib\neq0$, the limit is $(\operatorname{tr}L)\tilde\Pi$ with $\tilde\Pi=L/\operatorname{tr}L$ a minimal idempotent; if $a-ib=0$, the trace vanishes and $L^{2}=0$. Now $a-ib=0$ with real $a,b$ means $a=b=0$, that is, $\tilde u_{\mathrm r}=\tilde u_{\perp}$ orthogonal to $\vec u_{\mathrm b}$, that is, $\tilde u_{\mathrm r}$ anticommutes with $\vec u_{\mathrm b}$.

**Corollary (every boundary point is a limit).** Every nonzero element of the null cone is the limit of a family $\tilde Q(\psi)$ of the theorem, and the limit is reached with the scale collapsing as $\exp(-\psi/2)$ while the boost diverges.

**Proof.** If $\tilde Q=2Q_t\tilde\Pi$ is in the idempotent stratum, let $\tilde\Pi_{\mathrm H}=\tilde\Pi\tilde\Pi^{*}/\operatorname{tr}(\tilde\Pi\tilde\Pi^{*})$ be the Hermitian projection onto the range of $\tilde\Pi$; it is $\tfrac12(e_t+i\vec u)$ with $\vec u$ real. Choose $w\in SU(2)$ with $\tilde\Pi_{\mathrm H}w=\lambda\tilde\Pi$ and $\lambda>0$: in a unitary basis, which preserves $SU(2)$, where $\tilde\Pi_{\mathrm H}=\operatorname{diag}(1,0)$ and $\tilde\Pi=\begin{pmatrix}1&p\\0&0\end{pmatrix}$, the matrix $w=\lambda\begin{pmatrix}1&p\\-\bar p&1\end{pmatrix}$ with $\lambda=(1+\lvert p\rvert^{2})^{-1/2}$ is unitary of determinant one and has the required first row. Take $\vec u_{\mathrm b}=\vec u$, $\tilde u_{\mathrm r}=w$ and $R\zeta=2Q_t/\lambda$, flipping the signs of $\zeta$ and $w$ if necessary to place $\zeta$ in the branch; the limit is $2Q_t\tilde\Pi=\tilde Q$. If $\tilde Q=N$ is nilpotent, write $N=a(e_1+ie_2)$ with $e_1,e_2$ orthonormal and $e_3=e_1\times e_2$; take $\vec u_{\mathrm b}=e_3$, $\tilde u_{\mathrm r}=e_1$, $R\zeta=2a$, with the same sign adjustment.

The theorem is the precise sense in which the idempotents are the **boundary values** of the polar word: the scale has to vanish and the rapidity has to diverge, at the same rate, and the direction of the divergence, together with the rotor, selects the stratum. The boundary of the domain and the set of minimal idempotents are not the same set — the nilpotents are also on the boundary — but the idempotent stratum is the part reached when the rotor has a component in the plane spanned by $e_t$ and the boost axis, and the nilpotent stratum is reached when the rotor is orthogonal to both $e_t$ and the boost axis.

**The rate.** The word of the theorem has norm

$$
\langle\tilde Q(\psi)\rangle_{\natural}=R^{2}\exp(-\psi)\zeta^{2},
$$

so the distance to the cone is exponential in the rapidity, and the modulus is $R\exp(-\psi/2)$. The boundary is approached along the exponential coordinate line of the boost, with the scale line compensating: this is the coordinate picture of the statement that the boost is the non-compact factor that drives the word to the boundary, and that the scale is the factor that keeps the element finite.

### The Exponential Limit

The idempotents are not in the image of the exponential, because every value of the exponential is invertible and an idempotent is not. They are in its closure, in the following precise sense.

**Proposition (the exponential limit).** For a real unit vector $\vec u$,

$$
\tilde\Pi_{+}=\frac12\bigl(e_t+i\vec u\bigr)
=\lim_{\psi\to\infty}\frac{\exp(i\frac{\psi}{2}\vec u)}{2\cosh\frac{\psi}{2}}
=\lim_{\psi\to\infty}\exp(-\frac{\psi}{2})\exp(i\frac{\psi}{2}\vec u).
$$

**Proof.** The closed form of the boost gives

$$
\frac{\exp(i\frac{\psi}{2}\vec u)}{2\cosh\frac{\psi}{2}}
=\frac12\Bigl(e_t+i\tanh\frac{\psi}{2}\,\vec u\Bigr)
\longrightarrow\frac12\bigl(e_t+i\vec u\bigr).
$$

The idempotent is therefore the **direction** of an infinite boost, with the scale removed. It is the limit of the polar word with $r=\exp(-\psi/2)$, $\zeta=1$, $\tilde u_{\mathrm r}=e_t$; the phase multiplies it by a complex scalar, and the rotor moves it by the unitary action.

The nilpotent stratum has its own exponential description. For $N$ with $N^{2}=0$,

$$
\exp(tN)=e_t+tN
$$

for every complex $t$, a unipotent line. The line is invertible for every finite $t$ and tends to infinity with $t$; it never reaches the nilpotent $N$ itself, and it does not reach an idempotent. The two strata are therefore reached only at infinity: the idempotent by the divergence of the boost, and the nilpotent as the rescaled limit of the unipotent line, $\tilde Q=\lim_{t\to\infty}(\exp(tN)-e_t)/t$.

The idempotent has no logarithm: a logarithm $\tilde L$ with $\exp(\tilde L)=\tilde\Pi$ would make $\tilde\Pi$ invertible. It has no polar decomposition either, since its norm vanishes. What it has is a **normalised word**: the limit of the polar words with the scale collapsing. This is the sense in which the polar decomposition extends to the boundary as a *boundary value*, not as a value.

### The Action on the Idempotents

Let $\tilde Q$ be invertible. The sandwich of a Hermitian minimal idempotent is

$$
\Theta_{\tilde Q}(\tilde\Pi)=\tilde Q\,\tilde\Pi\,\tilde Q^{*}.
$$

It is Hermitian and positive semidefinite, of rank one, because $\tilde\Pi$ is Hermitian of rank one and the congruence preserves rank and inertia. It is therefore a **positive multiple of a Hermitian minimal idempotent**:

$$
\Theta_{\tilde Q}(\tilde\Pi)=\lambda\,\tilde\Pi_{\tilde Q},\qquad
\lambda=\operatorname{tr}\mathsf M_2\bigl(\tilde Q\tilde\Pi\tilde Q^{*}\bigr)>0,
\qquad \tilde\Pi_{\tilde Q}=\tilde\Pi_{\tilde Q}^{*}=\tilde\Pi_{\tilde Q}^{2}.
$$

The scalar $\lambda$ is the **unnormalised Born weight** of the projection $\tilde\Pi$ in the state $\tilde Q^{*}\tilde Q/\operatorname{tr}(\tilde Q\tilde Q^{*})$: the probability is $\lambda/\operatorname{tr}(\tilde Q\tilde Q^{*})$. The order $\tilde Q^{*}\tilde Q$ is the one compatible with the sandwich: $\operatorname{tr}(\tilde Q^{*}\tilde Q\tilde\Pi)=\operatorname{tr}(\tilde Q\tilde\Pi\tilde Q^{*})=\lambda$, while $\tilde Q\tilde Q^{*}$ would put the factors in the other order and give a different number for a non-Hermitian $\tilde Q$. In the geometric reading it is the scale of the image on the null direction. The projective class of $\tilde\Pi_{\tilde Q}$ is the image of the projective class of $\tilde\Pi$, so the group acts on the sphere of Hermitian idempotents.

**Theorem (the projective action).** The map $\tilde\Pi\mapsto[\tilde\Pi_{\tilde Q}]$ descends to an action of $\mathbb{B}^{\times}$ on the sphere of Hermitian minimal idempotents. The kernel is the centre $\mathbb{C}^{\times}$; the unitary subgroup acts by rotations, and the full group acts by the Möbius transformations of $\mathbb{C}P^{1}\cong S^{2}$.

**Proof.** The sandwich is multiplicative, $\Theta_{\tilde Q\tilde Q_1}=\Theta_{\tilde Q}\circ\Theta_{\tilde Q_1}$, and a central scalar $c$ multiplies $\Theta$ by $\lvert c\rvert^{2}$, so the whole centre lies in the kernel projectively. A unitary element $\tilde V$ gives $\tilde\Pi_{\tilde Q}=\tilde V\tilde\Pi\tilde V^{*}$, a conjugation, which is the rotation of the Bloch sphere by the image of $\tilde V$ in $SO(3)$. A general element is the product of a unitary and a Hermitian positive factor; the Hermitian positive factor gives the Möbius transformation of the conformal action, read on the celestial sphere in *Biquaternion Lorentzian and Conformal Geometry*.

The **stabiliser** of a single idempotent is larger than the kernel of the action on the algebra: the central circle acts trivially projectively, and the stabiliser has real dimension six in $\mathbb{B}^{\times}$ — four in the projective group — and it is the parabolic subgroup that fixes a null direction. The orbit is the sphere, of real dimension two, and the quotient of the group by the stabiliser is the sphere. This is the group-theoretic form of the boundary dictionary: the idempotents are a homogeneous space, and the polar word is the coordinate system in which its limiting directions are read.

**The Hermitian idempotents as pure states.** In the informational reading, a Hermitian minimal idempotent is a pure state, the sandwich is the update by a general element, and the positive scalar $\lambda$, normalised by $\operatorname{tr}(\tilde Q\tilde Q^{*})$, is the Born weight. The two idempotents of a pair are the two outcomes of a yes–no measurement, and the Peirce decomposition is the algebra of the two outcomes. The mathematical statements above are independent of the reading; the reading is recorded because it is the one the algebra serves.

## Worked Examples

### A Generic Element

Take the element of *Modulus–Unit Polar Decomposition of Biquaternions*,

$$
\tilde Q=(1+i)e_t+\vec e_x+i\vec e_y .
$$

Its norm is $2i$, its modulus is $\Rho=1+i$, and

$$
r=\sqrt{2},\qquad \alpha=\frac{\pi}{4},\qquad
\tilde U=e_t+\frac{1-i}{2}\vec e_x+\frac{1+i}{2}\vec e_y .
$$

The Hermitian element and the two non-central factors are

$$
\tilde U\tilde U^{*}=2e_t-i\vec e_x+i\vec e_y+i\vec e_z,\qquad
\tilde U_{\mathrm b}=\frac{3e_t-i\vec e_x+i\vec e_y+i\vec e_z}{\sqrt{6}},\qquad
\tilde u_{\mathrm r}=\sqrt{\frac{2}{3}}\,e_t+\frac{1}{\sqrt{6}}\vec e_x+\frac{1}{\sqrt{6}}\vec e_y .
$$

The parameters of the two exponentials are

$$
\psi=2\operatorname{arcosh}\frac{3}{\sqrt{6}}=\operatorname{arcosh}2=\ln(2+\sqrt{3})=1.3169578969,
\qquad
\vec u_{\mathrm b}=\frac{-\vec e_x+\vec e_y+\vec e_z}{\sqrt{3}},
$$

and

$$
\theta=2\arccos\sqrt{\frac{2}{3}}=\arccos\frac{1}{3}=1.2309594173,
\qquad
\vec u_{\mathrm r}=\frac{\vec e_x+\vec e_y}{\sqrt{2}} .
$$

The two closed forms reproduce the factors:

$$
\exp(i\frac{\psi}{2}\vec u_{\mathrm b})
=\sqrt{\frac{3}{2}}\,e_t+\frac{i}{\sqrt{6}}\bigl(-\vec e_x+\vec e_y+\vec e_z\bigr)
=\tilde U_{\mathrm b},
\qquad
\exp(\frac{\theta}{2}\vec u_{\mathrm r})
=\sqrt{\frac{2}{3}}\,e_t+\frac{1}{\sqrt{6}}\bigl(\vec e_x+\vec e_y\bigr)
=\tilde u_{\mathrm r},
$$

each to $10^{-16}$ in the four coefficients. The word is therefore

$$
\tilde Q=\sqrt{2}\,\exp(i\frac{\pi}{4})\,
\exp(i\frac{1.3169578969}{2}\frac{-\vec e_x+\vec e_y+\vec e_z}{\sqrt{3}})\,
\exp(\frac{1.2309594173}{2}\frac{\vec e_x+\vec e_y}{\sqrt{2}}) .
$$

### The Two Logarithms

The four exponents sum to the formal exponent

$$
\tilde Q_{\log}
=0.3465735903+0.7853981634\,i
+\bigl(0.4352098757-0.3801729982\,i\bigr)\vec e_x
+\bigl(0.4352098757+0.3801729982\,i\bigr)\vec e_y
+0.3801729982\,i\,\vec e_z .
$$

Its exponential is **not** the element: the largest coefficient of $\exp(\tilde Q_{\log})-\tilde Q$ is $0.5425679115$. The failure is the commutator of the boost and the rotor, not a rounding effect.

The true logarithm is much simpler, because the vector part of $\tilde Q$ is null:

$$
\langle\vec Q\rangle_{\natural}=Q_x^{2}+Q_y^{2}+Q_z^{2}=1+i^{2}=0 .
$$

So $\tilde Q=(1+i)(e_t+\vec N)$ with $\vec N=\frac{1}{1+i}(\vec e_x+i\vec e_y)$ and $\vec N^{2}=0$. The logarithm of a unipotent element truncates,

$$
\operatorname{Log}\tilde Q
=\ln\sqrt{2}+i\frac{\pi}{4}+\vec N
=0.3465735903+0.7853981634\,i
+\frac{1-i}{2}\vec e_x+\frac{1+i}{2}\vec e_y ,
$$

and

$$
\exp\bigl(\operatorname{Log}\tilde Q\bigr)=\tilde Q
$$

to $2.2\times10^{-16}$ in every coefficient. The single logarithm differs from the formal exponent by at most $0.3802$ in a coefficient, and the formal exponent misses the element by $0.54$; the difference is the Baker–Campbell–Hausdorff defect of the aligned formula.

The table collects the values.

| quantity | value |
|---|---|
| $r$ | $\sqrt{2}=1.4142135624$ |
| $\alpha$ | $\pi/4=0.7853981634$ |
| $\psi$ | $\ln(2+\sqrt{3})=1.3169578969$ |
| $\vec u_{\mathrm b}$ | $(-\vec e_x+\vec e_y+\vec e_z)/\sqrt{3}$ |
| $\theta$ | $\arccos(1/3)=1.2309594173$ |
| $\vec u_{\mathrm r}$ | $(\vec e_x+\vec e_y)/\sqrt{2}$ |
| $\exp(\tilde Q_{\log})-\tilde Q$ | $0.5425679115$ in the largest coefficient |
| $\exp(\operatorname{Log}\tilde Q)-\tilde Q$ | $2.2\times10^{-16}$ in every coefficient |

The example is the one of the algebraic article, so the four factors agree with the table there. It is also the simplest case in which the two logarithms can be compared: the vector part is null, the matrix has a single eigenvalue and a nontrivial Jordan block, and the logarithm is nevertheless unique once the scalar branch is fixed.

## Worked Examples at the Boundary

The example takes the axis $\vec e_z$, its two idempotents, the Peirce basis they define, and the two boundary paths.

### The Idempotents of the Axis $\vec e_z$

Take $\vec u=\vec e_z$. The two idempotents are

$$
\tilde\Pi_{+}=\frac12\bigl(e_t+i\vec e_z\bigr),
\qquad
\tilde\Pi_{-}=\frac12\bigl(e_t-i\vec e_z\bigr).
$$

Their norm is zero:

$$
\langle\tilde\Pi_{+}\rangle_{\natural}
=\frac14\bigl(e_t+i\vec e_z\bigr)\bigl(e_t-i\vec e_z\bigr)
=\frac14\bigl(e_t+\vec e_z^{2}\bigr)
=\frac14\bigl(e_t-e_t\bigr)=0,
$$

and their square is themselves:

$$
\tilde\Pi_{+}^{2}
=\frac14\bigl(e_t+2i\vec e_z+i^{2}\vec e_z^{2}\bigr)
=\frac14\bigl(e_t+2i\vec e_z+e_t\bigr)
=\tilde\Pi_{+}.
$$

The two are Hermitian, complementary and orthogonal: $\tilde\Pi_{+}^{*}=\tilde\Pi_{+}$, $\tilde\Pi_{-}^{*}=\tilde\Pi_{-}$, $\tilde\Pi_{+}+\tilde\Pi_{-}=e_t$, $\tilde\Pi_{+}\tilde\Pi_{-}=0$. The matrix images are the diagonal projections

$$
\mathsf M_2(\tilde\Pi_{+})=\begin{pmatrix}1&0\\0&0\end{pmatrix}=E_{11},
\qquad
\mathsf M_2(\tilde\Pi_{-})=\begin{pmatrix}0&0\\0&1\end{pmatrix}=E_{22},
$$

of trace one and determinant zero.

### The Peirce Basis

With $\tilde\Pi=\tilde\Pi_{+}$ and $\tilde\Pi'=\tilde\Pi_{-}$, the two off-diagonal directions are

$$
N=\tilde\Pi\,\vec e_x\,\tilde\Pi'=\frac12\bigl(\vec e_x+i\vec e_y\bigr),
\qquad
\bar N=\tilde\Pi'\,\vec e_x\,\tilde\Pi=\frac12\bigl(\vec e_x-i\vec e_y\bigr).
$$

The first identity is computed directly:

$$
(e_t+i\vec e_z)\vec e_x(e_t-i\vec e_z)
=2\bigl(\vec e_x+i\vec e_y\bigr),
$$

using $\vec e_z\vec e_x=\vec e_y$ and $\vec e_x\vec e_z=-\vec e_y$. The nilpotence is also direct:

$$
N^{2}=\frac14\bigl(\vec e_x^{2}+i\vec e_x\vec e_y+i\vec e_y\vec e_x+i^{2}\vec e_y^{2}\bigr)
=\frac14\bigl(-e_t+i\vec e_z-i\vec e_z+e_t\bigr)=0.
$$

So $N$ is a nilpotent of the second stratum, and it is not a complex multiple of an idempotent: a multiple $c\tilde\Pi$ has square $c^{2}\tilde\Pi=c(c\tilde\Pi)\neq0$ for $c\neq0$.

### The Boundary Path

The polar path of the theorem, with $\vec u_{\mathrm b}=\vec e_z$, $\tilde u_{\mathrm r}=e_t$, $\zeta=1$ and $R=1$, is

$$
\tilde Q(\psi)=\exp(-\frac{\psi}{2})\exp(i\frac{\psi}{2}\vec e_z)
=\frac{1+\exp(-\psi)}{2}e_t+\frac{1-\exp(-\psi)}{2}i\vec e_z .
$$

At $\psi=0$ it is $e_t$; at $\psi=1$ it is $0.6839\,e_t+0.3161\,i\vec e_z$; as $\psi\to\infty$ it tends to $\tilde\Pi_{+}$. Its norm is $\exp(-\psi)$, so the path approaches the cone exponentially. The rotor $e_t$ commutes with $\vec e_z$, and the limit is the idempotent stratum.

With $\tilde u_{\mathrm r}=\vec e_x$, which anticommutes with $\vec e_z$, the same path gives

$$
\tilde Q(\psi)\longrightarrow\frac12\bigl(e_t+i\vec e_z\bigr)\vec e_x
=\frac12\bigl(\vec e_x+i\vec e_y\bigr)=N,
$$

the nilpotent of the Peirce basis. The two limits are the two strata of the cone, reached from the same boost line by two rotor orientations.

### The Two Strata in One Table

| element | scalar part | norm | square | stratum |
|---|---|---|---|---|
| $\tilde\Pi_{+}=\tfrac12(e_t+i\vec e_z)$ | $\tfrac12$ | $0$ | $\tilde\Pi_{+}$ | idempotent |
| $\tilde\Pi_{-}=\tfrac12(e_t-i\vec e_z)$ | $\tfrac12$ | $0$ | $\tilde\Pi_{-}$ | idempotent |
| $N=\tfrac12(\vec e_x+i\vec e_y)$ | $0$ | $0$ | $0$ | nilpotent |
| $\bar N=\tfrac12(\vec e_x-i\vec e_y)$ | $0$ | $0$ | $0$ | nilpotent |
| $2\tilde\Pi_{+}=e_t+i\vec e_z$ | $1$ | $0$ | $2(2\tilde\Pi_{+})$ | idempotent |

The table exhibits the boundary dictionary: the scalar part is nonzero exactly on the idempotent stratum, where the square is a nonzero multiple of the element, $\tilde Q^{2}=2Q_t\tilde Q$; on the nilpotent stratum the scalar part and the square both vanish. The nilpotents are the boundary of the boundary, the stratum where even the scalar part has collapsed.

## Summary

### Main Results

| Result | Statement |
|---|---|
| Domain | the invertible biquaternions, $\langle\tilde Q\rangle_{\natural}\neq0$ |
| Decomposition | $\tilde Q=r\exp(i\alpha)\exp(i\frac{\psi}{2}\vec u_{\mathrm b})\exp(\frac{\theta}{2}\vec u_{\mathrm r})$ |
| Factors | scale $r>0$; phase $\alpha\in(-\frac{\pi}{2},\frac{\pi}{2}]$; boost $\psi\ge0$; rotor $\theta\in[0,2\pi]$; unit axes |
| Existence | every invertible element has a word |
| Uniqueness | the word is unique; the axes are undefined at $\psi=0$ and $\theta\in\{0,2\pi\}$ |
| Cartan logarithm | $(\tilde H,\tilde K)=(i\frac{\psi}{2}\vec u_{\mathrm b},\frac{\theta}{2}\vec u_{\mathrm r})$ |
| Single logarithm | $\operatorname{Log}\tilde Q=\ln r+i\alpha+\operatorname{Log}(\tilde U_{\mathrm b}\tilde u_{\mathrm r})$, multivalued |
| Formal exponent | $\ln r+i\alpha+i\frac{\psi}{2}\vec u_{\mathrm b}+\frac{\theta}{2}\vec u_{\mathrm r}$, not a logarithm unless the axes commute |
| Kernel | eigenvalues in $2\pi i\mathbb{Z}$; not a subgroup |
| Fibre | $\mathbb{Z}^{2}$ for distinct eigenvalues, continuous for a repeated diagonalisable eigenvalue, discrete for a Jordan block |
| Group law | Baker–Campbell–Hausdorff, with the brackets of the symmetric pair $(\mathfrak k,\mathfrak p)$ |
| Matrix picture | $\mathrm{GL}_2(\mathbb{C})=\mathfrak u(2)\oplus\mathfrak H$; the two logarithms |
| Coordinates | $(\ln r,\alpha,\psi,\vec u_{\mathrm b},\theta,\vec u_{\mathrm r})$, eight real dimensions; $\mathbb{B}^{\times}\simeq S^{1}\times S^{3}$ |
| Boundary | the null cone, with the two strata of minimal idempotents and nilpotents, reached as $r\to0$ and $\psi\to\infty$ |

### Formulas

| Quantity | Formula |
|---|---|
| Element | $\tilde Q=Q_te_t+\vec Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-$ in the distinct regime |
| Exponent | $\tilde Q_{\log}=\ln r+i\alpha+i\frac{\psi}{2}\vec u_{\mathrm b}+\frac{\theta}{2}\vec u_{\mathrm r}$ |
| Scale | $r>0$ |
| Phase | $\zeta=\exp(i\alpha)$, $\alpha\in(-\frac{\pi}{2},\frac{\pi}{2}]$ |
| Unit factor | $\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ |
| Decomposition | $\tilde Q=r\exp(i\alpha)\exp(i\frac{\psi}{2}\vec u_{\mathrm b})\exp(\frac{\theta}{2}\vec u_{\mathrm r})$ |
| Kernel | eigenvalues in $2\pi i\mathbb{Z}$; not a subgroup |
| Principal domain | the arguments of $\lambda_\pm$ in $(-\pi,\pi]$ |
| Group law | Baker–Campbell–Hausdorff: the four exponents do not add |

Every invertible biquaternion is a product of four exponentials,

$$
\tilde Q=r\,\exp(i\alpha)\,\exp(i\frac{\psi}{2}\vec u_{\mathrm b})\,\exp(\frac{\theta}{2}\vec u_{\mathrm r}),
$$

with $r>0$, $\alpha\in(-\frac{\pi}{2},\frac{\pi}{2}]$, $\psi\ge0$, $\theta\in[0,2\pi]$, and unit axes. The writing is unique, and its four parameters are coordinates on $\mathbb{B}^{\times}$: one real scale, one phase angle, one rapidity and one angle, with two axes. The scale and the phase are central; the boost is Hermitian positive of norm one; the rotor is a unit real quaternion.

The boost and the rotor exponents commute exactly when the axes are parallel or antiparallel, or one of the two parameters vanishes, and only then do the four exponentials amalgamate into one, with the complex angle $\frac{\theta+i\psi}{2}$ (with $\theta$ replaced by $-\theta$ for opposite axes). In general the sum of the four exponents is not a logarithm of the element: the single logarithm differs from it by the Baker–Campbell–Hausdorff correction, whose first term is $\frac{i\psi\theta}{4}\vec u_{\mathrm b}\times\vec u_{\mathrm r}$, a boost. A single logarithm nevertheless exists, because $\mathbb{B}^{\times}\cong\mathrm{GL}_2(\mathbb{C})$ is exponential; it is not unique, and the four parameters select a canonical word, not a canonical logarithm.

The kernel of the exponential is the set of diagonalisable elements with eigenvalues in $2\pi i\mathbb{Z}$; it contains $2\pi i e_t$, $2\pi\vec U$ for every pure root $\vec U$ of $-1$, and the null element $\pi i e_t+\pi\vec U$. It is not a subgroup, and the fibre of the exponential is not a coset of it. The group law is the bracket of a symmetric pair: two rotors compose to a rotor, two boosts to a boost times a rotor, and the bracket of a rotor and a boost lies in the boost directions. The exponential coordinates exhibit the homotopy type $S^{1}\times S^{3}$ of the group of units, with the phase carrying the fundamental group, and the conformal factor of the sandwich is $r^{4}=\lvert\langle\tilde Q\rangle_{\natural}\rvert^{2}$.

The word is defined on the complement of the null cone, and the boundary carries the rank-one elements. The null cone is one complex equation, of real dimension six, and its nonzero elements are the zero divisors. It splits into two strata: the nonzero complex multiples of the minimal idempotents, where the scalar part is nonzero, and the nilpotents, where it vanishes. The minimal idempotents are exactly $\tfrac12(e_t+\vec\Xi)$ with $\vec\Xi$ a pure root of $+1$, $\vec\Xi^{2}=e_t$ and $\vec\Xi\neq\pm e_t$; all have norm zero. The Hermitian ones are exactly $\tfrac12(e_t+i\vec u)$ with $\vec u$ a real unit vector, and they form a sphere: the Bloch sphere of the pure states and the celestial sphere of the null directions. For a Hermitian pair, the quaternion and coefficientwise conjugations exchange the two idempotents, and the star fixes each; for a general pair the quaternion conjugation exchanges them and the coefficientwise conjugation need not.

Each idempotent induces the Peirce decomposition of *Eigenvalue Decomposition of a Biquaternion* into four complex lines; the two mixed lines are nilpotent, and every nilpotent of the cone lies in one of them for a suitable idempotent. The polar word reaches the boundary only with the rapidity divergent and the scale collapsing at the rate $\exp(-\psi/2)$: the limit is $\tfrac{R\zeta}{2}(e_t+i\vec u_{\mathrm b})\tilde u_{\mathrm r}$, an idempotent multiple when the rotor does not anticommute with the boost axis and a nilpotent when it does. Every nonzero null element arises as such a limit. The idempotents and the nilpotents are not in the image of the exponential and have no polar word, but they are its boundary values; the sandwich of an invertible element sends the Hermitian idempotents to positive multiples of Hermitian idempotents, giving the projective action of the group on the sphere.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Q=r \exp(i\alpha)\exp(i\frac{\psi}{2}\vec u_{\mathrm b})\exp(\frac{\theta}{2}\vec u_{\mathrm r})$ | the exponential polar decomposition |
| $r=\exp(\ln r)$ | the scale, positive and central |
| $\zeta=\exp(i\alpha)$ | the central phase, $\alpha\in(-\frac{\pi}{2},\frac{\pi}{2}]$ |
| $\tilde U_{\mathrm b}=\exp(i\frac{\psi}{2}\vec u_{\mathrm b})$ | the boost, Hermitian positive of norm one |
| $\tilde u_{\mathrm r}=\exp(\frac{\theta}{2}\vec u_{\mathrm r})$ | the rotor, a unit real quaternion |
| $\psi$, $\vec u_{\mathrm b}$ | rapidity and axis of the boost |
| $\theta$, $\vec u_{\mathrm r}$ | angle and axis of the rotor |
| $\Rho=r\exp(i\alpha)$ | the complex modulus, $\Rho^{2}=\langle\tilde Q\rangle_{\natural}$ |
| $\tilde Q_{\log}=\ln r+i\alpha+i\frac{\psi}{2}\vec u_{\mathrm b}+\frac{\theta}{2}\vec u_{\mathrm r}$ | the formal exponent, not a logarithm in general |
| $(\tilde H,\tilde K)$ | the Cartan logarithm, $\tilde H=i\frac{\psi}{2}\vec u_{\mathrm b}$, $\tilde K=\frac{\theta}{2}\vec u_{\mathrm r}$ |
| $\operatorname{Log}\tilde Q$ | a single logarithm, $\exp(\operatorname{Log}\tilde Q)=\tilde Q$ |
| $\mathfrak k$, $\mathfrak p$ | the anti-Hermitian and Hermitian traceless summands of $\mathfrak{sl}(2,\mathbb{C})$ |
| $B=\sqrt{Q_x^{2}+Q_y^{2}+Q_z^{2}}$ | the complex norm of the vector part |
| $\mathsf M_2$ | the matrix model, $\det\mathsf M_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}$ |
| $P$, $K$ | the positive cone and $SU(2)$ in $SL(2,\mathbb{C})=P\cdot K$ |
| $\mathcal N=\{\langle\tilde Q\rangle_{\natural}=0\}$ | the null cone, the boundary of the polar domain |
| $\tilde\Pi$, $\tilde\Pi'=e_t-\tilde\Pi$ | a minimal idempotent and its complement |
| $\lambda_\pm=Q_t\pm iB$ | the eigenvalues, as in *Eigenvalue Decomposition of a Biquaternion* |
| $\vec\Xi=2\tilde\Pi-e_t$ | the pure root of $+1$ attached to $\tilde\Pi$ |
| $\tilde\Pi_{\pm}=\tfrac12(e_t\pm\vec\Xi)$ | the two idempotents of a pure root; the Hermitian case is $\vec\Xi=i\vec u$ with $\vec u$ real |
| $N$, $\bar N$ | the two Peirce nilpotents, $N^{2}=\bar N^{2}=0$ |
| $\tilde\Pi_{\tilde Q}$ | the normalised image of $\tilde\Pi$ under the sandwich, $\Theta_{\tilde Q}(\tilde\Pi)=\lambda\tilde\Pi_{\tilde Q}$ |
| $\lambda$ | the positive scalar of the sandwich of a Hermitian idempotent |
| $[\tilde\Pi]$ | the projective class of an idempotent, a point of the sphere |
| $2Q_t$ | the trace of the boundary element, the scalar part doubled |
| $R$ | the limiting scale of the boundary path, $r=R\exp(-\psi/2)$ |

## Further Reading

- [Modulus–Unit Polar Decomposition of Biquaternions](modulus-unit-polar-decomposition-of-biquaternions.html), for the algebraic word, the modulus–unit writing, the four factors and the theorem of existence and uniqueness.
- [Biquaternion Elementary Functions](biquaternion-elementary-functions.html), for the exponential, the logarithm, the closed forms, the kernel and the two real directions.
- [Eigenvalue Decomposition of a Biquaternion](eigenvalue-decomposition-of-a-biquaternion.html), for the eigenvalues, the eigenprojections, the Peirce decomposition and the parity-matched lattice used above.
- [Biquaternion Lie Group and Exponential Structure](biquaternion-lie-group-and-exponential-structure.html), for the exponential map of the group of units, the failure of surjectivity on the norm-one group and the Baker–Campbell–Hausdorff series.
- [Exponential Polar Decomposition of Quaternions](exponential-polar-decomposition-of-quaternions.html), for the quaternion case, where the four factors reduce to two and the exponents amalgamate.
- [The Cartan Hermitian Pairing of the Polar Decomposition of Biquaternions](the-cartan-hermitian-pairing-of-the-polar-decomposition-of-biquaternions.html), for the Hermitian positive and unitary factors and the Cartan decomposition of the exponents.
- [The Polar Decomposition and Remarkable Subspaces](the-polar-decomposition-and-remarkable-subspaces.html), for the four exponents read against the four coordinate blocks, and for the product of two boosts.
- [Biquaternion Rotations and Lorentz Transformations](biquaternion-rotations-and-lorentz-transformations.html), for the sandwich, its kernel and the matrices of the Lorentz action.
- [Hermitian and Skew-Hermitian Elements](hermitian-and-skew-hermitian-elements.html), for the split $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ and the two real forms.
- [Hermitian Idempotents and the Peirce Decomposition](hermitian-idempotents-and-the-peirce-decomposition.html), for the Peirce decomposition and the Hermitian idempotents in the algebra.
- [The Unitary Group of the Biquaternion Algebra](the-unitary-group-of-the-biquaternion-algebra.html), for the unitary subgroup and its action by conjugation.
- [Biquaternion Lorentzian and Conformal Geometry](biquaternion-lorentzian-and-conformal-geometry.html), for the celestial sphere, the null directions and the Möbius action.
- [The Informational Sector: States, Observables and Probability](../articles_physics/the-informational-sector-states-observables-and-probability.html), for the pure states, the Born weight and the density-matrix reading.
- [Norm and Invertibility in the General Quaternionic Algebra](norm-and-invertibility-in-the-general-quaternionic-algebra.html), for the norm, the zero divisors and the two eigenvalue branches.
- [Conventions in Mathematics](conventions-in-mathematics.html), for the root convention and the branch of the argument.
- S. J. Sangwine and E. Hitzer, "Polar decomposition of complexified quaternions and octonions", *Advances in Applied Clifford Algebras* (2020), DOI 10.1007/s00006-020-1048-y, for the polar decomposition of a complexified quaternion.
