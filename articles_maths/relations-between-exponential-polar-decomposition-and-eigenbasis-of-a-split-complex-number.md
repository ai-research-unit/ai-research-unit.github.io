# __Relations between Exponential Polar Decomposition and Eigenbasis of a Split-Complex Number__

## Introduction

A split-complex number carries two decompositions of the same element. The **eigenvalue decomposition** of *Eigenbasis of a Split-Complex Number* writes $Q=q+jq'$ as

$$
Q=\lambda_+\Pi_++\lambda_-\Pi_-,
\qquad
\lambda_\pm=q\pm q',
\quad
\Pi_\pm=\tfrac12(1\pm j),
$$

with $\lambda_\pm$ the eigenvalues and $\Pi_\pm$ the fixed central idempotents. The **exponential polar decomposition** of *Exponential Polar Decomposition of Split-Complex Numbers* writes an invertible $Q$ as

$$
Q=\epsilon\exp(Q_{\log})=r\,\epsilon\exp(\phi j),
\qquad
Q_{\log}=\ln r+j\phi,
$$

with $r>0$, $\phi\in\mathbb{R}$ and $\epsilon\in\{\pm1,\pm j\}$ the component sign. This article states the dictionary between the two writings. It repeats no proof from the three source articles: the spectrum and the idempotents are those of the eigenvalue article, and the exponential, the logarithm and the components are those of the elementary and polar articles.

The two decompositions answer different questions. The spectral writing separates $Q$ into its two real coordinates $\lambda_+=q+q'$ and $\lambda_-=q-q'$, with fixed directions $\Pi_\pm$. The polar writing separates $Q$ into a positive modulus $r$, a hyperbolic angle $\phi$, and a discrete sign $\epsilon$ that records the component. The dictionary is therefore a change of coordinates on the unit group: the continuous pair $(\lambda_+,\lambda_-)$ is replaced by $(r,\phi)$, and the two signs of $\lambda_\pm$ are replaced by the single discrete factor $\epsilon$.

**The results.** The eigenvalues are recovered from the polar data by

$$
\lambda_\pm=\sigma_\pm\,r\,e^{\pm\phi},
\qquad
\sigma_\pm=\operatorname{sgn}\lambda_\pm,
$$

where the sign pair $(\sigma_+,\sigma_-)$ is the spectral reading of $\epsilon$. The polar data are recovered from the eigenvalues by

$$
r=\sqrt{\lvert\lambda_+\lambda_-\rvert},
\qquad
\phi=\tfrac12\ln\left\lvert\frac{\lambda_+}{\lambda_-}\right\rvert,
$$

and $\epsilon$ is the component determined by the signs of $\lambda_\pm$. The product of the eigenvalues is $\lambda_+\lambda_-=q^2-q'^2=(q+q')(q-q')$, and the ratio is the exponential of twice the hyperbolic angle, up to the sign of $q^2-q'^2$. The dictionary is a bijection between the four components of $\mathbb{D}^\times$ and the four sign patterns.

| Question | Answer |
|---|---|
| Element | $Q=q+jq'$ |
| Eigenvalues | $\lambda_\pm=q\pm q'$ |
| Eigenprojections | $\Pi_\pm=\tfrac12(1\pm j)$, fixed and central |
| Polar parameters | $r>0$, $\phi\in\mathbb{R}$, $\epsilon\in\{\pm1,\pm j\}$ |
| Eigenvalues from polar data | $\lambda_\pm=\sigma_\pm r e^{\pm\phi}$ |
| Polar data from eigenvalues | $r=\sqrt{\lvert\lambda_+\lambda_-\rvert}$, $\phi=\tfrac12\ln\lvert\lambda_+/\lambda_-\rvert$ |
| Sign pattern | $(\sigma_+,\sigma_-)$ is the spectral reading of $\epsilon$ |
| Factor decompositions | $r=r\Pi_++r\Pi_-$, $\epsilon=\sigma_+\Pi_++\sigma_-\Pi_-$, $e^{\phi j}=e^{\phi}\Pi_++e^{-\phi}\Pi_-$ |
| Exponential on idempotents | $\exp(Q_{\log})=r e^{\phi}\Pi_++r e^{-\phi}\Pi_-$ |
| Common domain | the units, $q^2-q'^2=\lambda_+\lambda_-\neq0$ |
| Spectral domain | all $Q$; the zero divisors have a spectrum but no polar word |
| Kernel | trivial: no continuous period |

## The Two Decompositions

### The Eigenvalue Decomposition

For $Q=q+jq'$, the spectrum is

$$
\sigma(Q)=\{\lambda_+,\lambda_-\},
\qquad
\lambda_+=q+q'=Q_+,
\quad
\lambda_-=q-q'=Q_-.
$$

The eigenvalues are real, and they are distinct exactly when $q'\neq0$. In that case

$$
Q=\lambda_+\Pi_++\lambda_-\Pi_-,
\qquad
\Pi_\pm=\frac{1\pm j}{2},
$$

with $\Pi_\pm$ primitive, orthogonal, complete and central. These are the statements of *Eigenbasis of a Split-Complex Number*, §*The Spectrum and the Characteristic Polynomial*, §*The Eigenprojections* and §*The Eigenvalue Decomposition*. In the scalar case $q'=0$, the eigenvalue is repeated, $\lambda_+=\lambda_-=q$, and the decomposition is the one-term writing $Q=q\cdot1$.

| Spectral item | Value |
|---|---|
| Spectrum | $\{\lambda_+,\lambda_-\}=\{q+q',q-q'\}$ |
| Sum | $\lambda_++\lambda_-=2q$ |
| Product | $\lambda_+\lambda_-=q^2-q'^2$ |
| Distinctness | $\lambda_+\neq\lambda_-\iff q'\neq0$ |
| Eigenprojections | $\Pi_\pm=\tfrac12(1\pm j)$ |
| Decomposition | $Q=\lambda_+\Pi_++\lambda_-\Pi_-$ |

### The Exponential Polar Decomposition

Every unit $Q\in\mathbb{D}^\times=\{q^2-q'^2\neq0\}$ has a unique writing

$$
Q=\epsilon\exp(Q_{\log})=r\,\epsilon\exp(\phi j),
\qquad
Q_{\log}=\ln r+j\phi,
$$

with $r>0$, $\phi\in\mathbb{R}$ and $\epsilon\in\{\pm1,\pm j\}$. The factor $r=\sqrt{\lvert q^2-q'^2\rvert}$ is the modulus, $\phi$ is the hyperbolic angle, and $\epsilon$ is the component sign; the unit factor is $u=\epsilon\exp(\phi j)=Q/r$, of modulus one. These are the statements of *Exponential Polar Decomposition of Split-Complex Numbers*, §*The Decomposition*, §*Existence and Uniqueness* and §*The Four Components*.

| Polar item | Value |
|---|---|
| Domain | $\mathbb{D}^\times=\{Q:q^2-q'^2\neq0\}$ |
| Decomposition | $Q=r\,\epsilon\exp(\phi j)$ |
| Modulus | $r=\sqrt{\lvert q^2-q'^2\rvert}>0$ |
| Angle | $\phi\in\mathbb{R}$ |
| Component sign | $\epsilon\in\{\pm1,\pm j\}$ |
| Exponent | $Q_{\log}=\ln r+j\phi$ |
| Kernel | $\{0\}$ |
| Fibre of the polar map | one point on each component, empty off the units |

### The Common Domain

The spectral decomposition exists for every $Q$, including the zero divisors and the zero element. The polar decomposition exists exactly on the units. The two conditions that separate the regimes are

$$
q'\neq0\quad\text{(distinct eigenvalues)},
\qquad
q^2-q'^2=\lambda_+\lambda_-\neq0\quad\text{(invertibility)}.
$$

They are independent: a zero divisor has $q'\neq0$ and $q^2-q'^2=0$, so it has two distinct eigenvalues and no polar word. The table records the four possibilities.

| Condition | Spectrum | Polar decomposition |
|---|---|---|
| $q'\neq0$, $q^2-q'^2\neq0$ | two distinct nonzero eigenvalues | exists, and the component sign is one of four |
| $q'\neq0$, $q^2-q'^2=0$ | two distinct eigenvalues, one zero | does not exist: $Q$ is a zero divisor |
| $q'=0$, $q^2\neq0$ | one repeated nonzero eigenvalue | exists with $\phi=0$ and $\epsilon=\operatorname{sgn}q$ |
| $q'=0$, $q^2-q'^2=0$ | the eigenvalue $0$ | does not exist: $Q=0$ |

The spectral domain is therefore strictly larger than the polar domain. The gap is exactly the null set $q^2-q'^2=0$: the nonzero zero divisors and the zero element, on which the eigenvalue decomposition survives and the logarithm does not.

## The Dictionary

### The Eigenvalues from the Polar Parameters

Let $Q=r\,\epsilon\exp(\phi j)$ be a unit, and let $\sigma_\pm=\operatorname{sgn}\lambda_\pm$. Applying the eigenvalue relations $Q\Pi_\pm=\lambda_\pm\Pi_\pm$ to the polar writing gives

$$
\lambda_\pm=\sigma_\pm\,r\,e^{\pm\phi}.
$$

The formula is checked on the two idempotents:

$$
Q\Pi_+=r\,\epsilon\exp(\phi j)\Pi_+,
\qquad
\exp(\phi j)\Pi_+=e^{\phi}\Pi_+,
\qquad
\epsilon\Pi_+=\sigma_+\Pi_+,
$$

and similarly for $\Pi_-$; the signs $\sigma_\pm$ are the eigenvalues of the component sign $\epsilon$, read through $\Pi_\pm$. The table lists the four components.

| Component | Condition | $\epsilon$ | $\sigma_+$ | $\sigma_-$ | Unit factor eigenvalues | Exponent eigenvalues |
|---|---|---|---|---|---|---|
| Future cone | $q>\lvert q'\rvert$ | $1$ | $+$ | $+$ | $e^{\phi}$, $e^{-\phi}$ | $\ln r+\phi$, $\ln r-\phi$ |
| Past cone | $q<-\lvert q'\rvert$ | $-1$ | $-$ | $-$ | $-e^{\phi}$, $-e^{-\phi}$ | $\ln r+\phi$, $\ln r-\phi$ |
| Right spacelike | $q'>\lvert q\rvert$ | $j$ | $+$ | $-$ | $e^{\phi}$, $-e^{-\phi}$ | $\ln r+\phi$, $\ln r-\phi$ |
| Left spacelike | $q'<-\lvert q\rvert$ | $-j$ | $-$ | $+$ | $-e^{\phi}$, $e^{-\phi}$ | $\ln r+\phi$, $\ln r-\phi$ |

The exponent eigenvalues are always $\ln r\pm\phi$; the component sign changes the eigenvalues of the unit factor, not those of the exponent. This is the discrete part of the dictionary.

The two spectral invariants of the polar data are

$$
\lambda_+\lambda_-=\sigma_+\sigma_-\,r^2,
\qquad
\frac{\lambda_+}{\lambda_-}=\frac{\sigma_+}{\sigma_-}e^{2\phi}.
$$

Since $\sigma_+\sigma_-=\operatorname{sgn}(q^2-q'^2)$ and $\sigma_+/\sigma_-=\operatorname{sgn}(q^2-q'^2)$, both identities reduce to

$$
\lambda_+\lambda_-=q^2-q'^2,
\qquad
\left\lvert\frac{\lambda_+}{\lambda_-}\right\rvert=e^{2\phi}.
$$

The product is independent of the component; the modulus of the ratio is the exponential of twice the hyperbolic angle.

### The Polar Parameters from the Eigenvalues

For a unit $Q=\lambda_+\Pi_++\lambda_-\Pi_-$, the modulus and the angle are

$$
\boxed{\; r=\sqrt{\lvert\lambda_+\lambda_-\rvert}=\sqrt{\lvert q^2-q'^2\rvert},
\qquad
\phi=\tfrac12\ln\left\lvert\frac{\lambda_+}{\lambda_-}\right\rvert \;}
$$

The component sign is recovered from the signs of the two eigenvalues:

| $(\sigma_+,\sigma_-)$ | Component | $\epsilon$ |
|---|---|---|
| $(+,+)$ | future cone | $1$ |
| $(-,-)$ | past cone | $-1$ |
| $(+,-)$ | right spacelike | $j$ |
| $(-,+)$ | left spacelike | $-j$ |

The exponent is then $Q_{\log}=\ln r+j\phi$, with real eigenvalues $\ln r\pm\phi=\ln\lvert\lambda_\pm\rvert$. The imaginary parts of the complex logarithms of $\lambda_\pm$ are $0$ or $\pi$, and they are carried by $\epsilon$, not by a continuous angle. This is the exact point at which the split-complex dictionary differs from the complex one: the sign of a real eigenvalue is a discrete datum, not a phase.

**Proposition (the dictionary).** On the unit group, the map

$$
\boxed{\; (r,\phi,\epsilon)\longmapsto(\lambda_+,\lambda_-)=(\sigma_+re^{\phi},\sigma_-re^{-\phi}) \;}
$$

is a bijection from the four components, each parametrised by $(r,\phi)\in(0,\infty)\times\mathbb{R}$, onto the four open quadrants of $\mathbb{R}^2$. Its inverse is the formula above.

*Proof.* The forward map gives $\lambda_+\lambda_-=\sigma_+\sigma_-r^2e^{0}=q^2-q'^2$, whose sign is $\sigma_+\sigma_-$, and $\lvert\lambda_+/\lambda_-\rvert=e^{2\phi}$. Hence $r$ and $\phi$ are recovered by the displayed formulas, and the sign pair is recovered from $\lambda_\pm$. Conversely, the formulas reproduce $\lambda_\pm$ from $(r,\phi,\epsilon)$.

### The Eigenprojections

The eigenprojections are the fixed idempotents $\Pi_\pm$; they do not depend on $Q$ and are not part of the polar data. In the polar writing they read the unit factor:

$$
\frac{Q}{r}=\epsilon\exp(\phi j)
=\frac{\lambda_+}{r}\Pi_++\frac{\lambda_-}{r}\Pi_-
=\sigma_+e^{\phi}\Pi_++\sigma_-e^{-\phi}\Pi_-.
$$

The modulus $r$ is scalar and disappears from the eigenprojections; the component sign $\epsilon$ acts on them by the sign pair $(\sigma_+,\sigma_-)$; the angle $\phi$ acts by the hyperbolic factor $e^{\pm\phi}$. The spectral decomposition of $Q$ and the spectral decomposition of its unit factor therefore have the same idempotents and eigenvalues differing by the scalar $r$.

| Object | Eigenvalue decomposition | Polar reading |
|---|---|---|
| $Q$ | $\lambda_+\Pi_++\lambda_-\Pi_-$ | $r\,\epsilon\exp(\phi j)$ |
| Unit factor $Q/r$ | $\sigma_+e^{\phi}\Pi_++\sigma_-e^{-\phi}\Pi_-$ | $\epsilon\exp(\phi j)$ |
| Exponent $Q_{\log}$ | $(\ln r+\phi)\Pi_++(\ln r-\phi)\Pi_-$ | $\ln r+j\phi$ |
| Modulus $r$ | $r\Pi_++r\Pi_-$ | $r$ |
| Component sign $\epsilon$ | $\sigma_+\Pi_++\sigma_-\Pi_-$ | $\epsilon$ |

The table shows the division of labour: the eigenvalues carry the continuous scale $r$ and angle $\phi$, the idempotents are fixed, and the discrete factor $\epsilon$ is the spectral sign pair.

### The Factors One by One

Each factor of the polar word has its own spectral decomposition on the fixed idempotents. The modulus is scalar, the component sign is the sign pair, and the hyperbolic factor is the exponential of $\phi j$:

$$
r=r\Pi_++r\Pi_-,
\qquad
\epsilon=\sigma_+\Pi_++\sigma_-\Pi_-,
\qquad
e^{\phi j}=e^{\phi}\Pi_++e^{-\phi}\Pi_-.
$$

The unit factor and the element follow:

$$
u=\epsilon e^{\phi j}
=\sigma_+e^{\phi}\Pi_++\sigma_-e^{-\phi}\Pi_-,
\qquad
Q=r u
=\lambda_+\Pi_++\lambda_-\Pi_-.
$$

The table collects the five levels.

| Factor | Closed form | Spectral decomposition | Eigenvalues |
|---|---|---|---|
| Modulus | $r$ | $r\Pi_++r\Pi_-$ | $r,r$ |
| Component sign | $\epsilon$ | $\sigma_+\Pi_++\sigma_-\Pi_-$ | $\sigma_+,\sigma_-$ |
| Hyperbolic factor | $e^{\phi j}$ | $e^{\phi}\Pi_++e^{-\phi}\Pi_-$ | $e^{\phi},e^{-\phi}$ |
| Unit factor | $u=\epsilon e^{\phi j}$ | $\sigma_+e^{\phi}\Pi_++\sigma_-e^{-\phi}\Pi_-$ | $\sigma_+e^{\phi},\sigma_-e^{-\phi}$ |
| Element | $Q=r\epsilon e^{\phi j}$ | $\lambda_+\Pi_++\lambda_-\Pi_-$ | $\lambda_\pm=\sigma_\pm r e^{\pm\phi}$ |

The table is the split-complex analogue of the factor table of the biquaternion article, with two differences: the idempotents are fixed, and there are only four components, so the factor $\epsilon$ is discrete and no axes occur.

### The Exponential on the Idempotents

The exponent is

$$
Q_{\log}=\ln r+j\phi
=(\ln r+\phi)\Pi_++(\ln r-\phi)\Pi_-,
$$

and its exponential acts on the two idempotents by

$$
\exp(Q_{\log})
=e^{\ln r+\phi}\Pi_++e^{\ln r-\phi}\Pi_-
=r e^{\phi}\Pi_++r e^{-\phi}\Pi_-.
$$

On the future cone, where $\epsilon=1$, this is $Q$. On the other three components $Q=\epsilon\exp(Q_{\log})$, and the exponent is the logarithm of the future-cone element $r e^{\phi j}$, not of $Q$ itself. In every component the eigenvalues of the exponent are $\ln r\pm\phi=\ln\lvert\lambda_\pm\rvert$, while the eigenvalues of $Q$ are $\sigma_\pm r e^{\pm\phi}$. The exponential sees the modulus and the absolute values of the eigenvalues; the signs are the discrete factor $\epsilon$, outside the image of the exponential.

This is the exact sense in which the exponential is a bijection onto the future cone and the polar word is a section of the word map, not a logarithm, on the other three components. The kernel is trivial, and the failure is not multivaluedness but the four-component cover.

### What Each Side Carries

| Spectral datum | What it fixes | Formula | What it leaves free |
|---|---|---|---|
| $\lambda_+\lambda_-$ | modulus and the sign of the product | $r=\sqrt{\lvert\lambda_+\lambda_-\rvert}$, $\sigma_+\sigma_-=\operatorname{sgn}(\lambda_+\lambda_-)$ | the exchange $\sigma_+\leftrightarrow\sigma_-$, one bit |
| $\lambda_+/\lambda_-$ | hyperbolic angle and the sign of the ratio | $\phi=\tfrac12\ln\lvert\lambda_+/\lambda_-\rvert$, $\sigma_+/\sigma_-=\operatorname{sgn}(\lambda_+/\lambda_-)$ | the exchange $\sigma_+\leftrightarrow\sigma_-$, one bit |
| Sign pair $(\sigma_+,\sigma_-)$ | component sign | the table of components | — |
| $\lambda_\pm$ | the element | $Q=\lambda_+\Pi_++\lambda_-\Pi_-$ | — |
| $r,\phi,\epsilon$ | the element | $Q=r\epsilon e^{\phi j}$ | — |
| $Q_{\log}$ | the future-cone part | $\exp(Q_{\log})=r e^{\phi j}$ | the component sign |

Read down the table for the direction spectral to polar and up for the direction polar to spectral. Because the idempotents are fixed and the sign pair is discrete, every row closes: no continuous degree of freedom is left. This is the structural difference from the biquaternion case, where the eigenprojections vary and the eigenvalues leave a one-parameter family.

## The Regimes

The spectral regimes of the eigenvalue article and the components of the polar article fit together as follows.

| Regime | Condition | Spectral data | Polar data |
|---|---|---|---|
| Distinct interior | $q'\neq0$, $q^2-q'^2\neq0$ | $\lambda_+\neq\lambda_-$, both nonzero | $r>0$, $\phi\in\mathbb{R}$, one of four $\epsilon$ |
| Zero divisor | $q'\neq0$, $q^2-q'^2=0$ | $\lambda_+\neq\lambda_-$, one zero | none: not a unit |
| Scalar nonzero | $q'=0$, $q\neq0$ | $\lambda_+=\lambda_-=q$ | $r=\lvert q\rvert$, $\phi=0$, $\epsilon=\operatorname{sgn}q$ |
| Zero | $q'=0$, $q=0$ | $\lambda_+=\lambda_-=0$ | none |
| Jordan | absent: the algebra is reduced | — | — |
| Nilpotent | absent: only $Q=0$ | — | — |

### The Zero-Divisor Regime

A nonzero zero divisor has $q^2-q'^2=0$ and $q'\neq0$, so $q'=\pm q$ and

$$
Q=q(1\pm j)=2q\,\Pi_\pm.
$$

Its eigenvalues are $\lambda_+=2q$, $\lambda_-=0$ for $Q=2q\Pi_+$, and they are exchanged for $Q=2q\Pi_-$. The spectrum is distinct, and the eigenvalue decomposition exists. The polar decomposition does not: the angle formula gives $\phi=\tfrac12\ln\lvert\lambda_+/\lambda_-\rvert=+\infty$, and the logarithm of the zero eigenvalue does not exist. The zero-divisor cone is the boundary of the polar domain, not a spectral degeneration.

### The Scalar Regime

For $Q=q$ with $q\neq0$, the two eigenvalues coincide at $q$. The polar data are $r=\lvert q\rvert$, $\phi=0$ and $\epsilon=\operatorname{sgn}q$; the unit factor is $\epsilon=\pm1$. The repeated eigenvalue is therefore not a repeated polar datum: the angle vanishes and the two-term spectral writing collapses to $Q=q\Pi_++q\Pi_-$, while the polar writing keeps the single modulus and the single sign.

### The Absence of the Jordan and Nilpotent Regimes

The algebra is $\mathbb{R}\times\mathbb{R}$, hence reduced. There is no nonzero nilpotent, so there is no Jordan-block regime and no nilpotent boundary. Every element is semisimple; the only spectral degeneracy is the scalar case, and the only polar boundary is the zero-divisor cone. This is the structural difference from the biquaternion dictionary, where the Jordan and nilpotent regimes are nonempty and the eigenprojections vary.

## The Exponential and the Logarithm

### The Kernel

The exponential of $\mathbb{D}$ has trivial kernel, $\ker\exp=\{0\}$ (*Split-Complex Elementary Functions*, §*The Exponential*). In spectral terms, if $X=x+jy$ then

$$
\exp(X)=e^{x}\bigl(\cosh y+j\sinh y\bigr),
\qquad
\lambda_\pm(\exp X)=e^{x\pm y},
$$

so $\exp X=1$ exactly when $e^{x+y}=e^{x-y}=1$, that is when $x+y=x-y=0$, hence $X=0$. There is no lattice and no continuous period. This is the spectral reason why the polar exponent $Q_{\log}$ is unique: the two real eigenvalues $\ln r\pm\phi$ are the logarithms of $\lvert\lambda_\pm\rvert$, and the only ambiguity is the discrete sign pair.

### The Fibre

For a unit $Q$, the equation $\exp X=Q$ has exactly one solution, and it exists exactly when $Q$ lies in the future cone $F$. In spectral coordinates the condition is $\lambda_\pm>0$, and the solution is

$$
\boxed{\; X=\tfrac12\ln(\lambda_+\lambda_-)+\tfrac12\ln\frac{\lambda_+}{\lambda_-}\,j
=\ln r+j\phi \;}
$$

For the other three components, the polar writing is not a logarithm of $Q$ but a logarithm of $\epsilon Q$:

$$
Q=\epsilon\exp(Q_{\log}),
\qquad
\epsilon Q\in F,
\qquad
Q_{\log}=\operatorname{Log}(\epsilon Q).
$$

The fibre of the exponential is therefore one point on $F$ and empty on the other three components. The extended polar map $(\epsilon,X)\mapsto\epsilon\exp X$ is a bijection from $\{\pm1,\pm j\}\times\mathbb{R}^2$ onto $\mathbb{D}^\times$; its "fibre" over $Q$ is the single pair $(\epsilon,Q_{\log})$.

| Item | Value |
|---|---|
| Kernel | $\{0\}$ |
| Fibre of $\exp$ over $Q$ | one point if $Q\in F$, empty otherwise |
| Extended fibre | one pair $(\epsilon,Q_{\log})$ per unit |
| Spectral condition for $\exp X=Q$ | $\lambda_+(Q)>0$ and $\lambda_-(Q)>0$ |
| Spectral coordinates of $X$ | $(\ln\lvert\lambda_+\rvert,\ln\lvert\lambda_-\rvert)$ up to the sign pair |

The table records the essential difference from the reduced biquaternion and biquaternion cases: there the exponential has a nontrivial kernel and a lattice of periods; here the discrete factor is finite and the kernel is trivial.

## The Matrix Picture

Under the regular representation,

$$
\mathsf M_2(Q)=\begin{pmatrix}q&q'\\q'&q\end{pmatrix},
\qquad
S=\begin{pmatrix}1&1\\1&-1\end{pmatrix},
\qquad
S\,\mathsf M_2(Q)\,S^{-1}
=\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}.
$$

The polar decomposition is the same identity read through the two factors:

$$
\mathsf M_2(Q)=\mathsf M_2(\epsilon)\,\exp(\ln r\,I+\phi K),
\qquad
K=\mathsf M_2(j)=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
$$

The matrix $\mathsf M_2(\epsilon)$ is $I$, $-I$, $K$ or $-K$ for $\epsilon=1,-1,j,-j$; its eigenvalues are the sign pair $(\sigma_+,\sigma_-)$. The exponential factor has eigenvalues $e^{\ln r\pm\phi}=r e^{\pm\phi}$. Hence the eigenvalues of the product are $\sigma_\pm r e^{\pm\phi}=\lambda_\pm$, which is the dictionary in matrix form.

| Matrix | Eigenvalues | Spectral role |
|---|---|---|
| $\mathsf M_2(Q)$ | $\lambda_+,\lambda_-$ | the element |
| $\mathsf M_2(\epsilon)$ | $\sigma_+,\sigma_-$ | the component sign |
| $\exp(\ln r\,I+\phi K)$ | $r e^{\phi},r e^{-\phi}$ | the modulus and the angle |
| $S\,\mathsf M_2(Q)\,S^{-1}$ | $\lambda_+,\lambda_-$ | the diagonal form |

The matrix picture shows that the polar decomposition is not a different decomposition of the matrix: it is the factorisation of the diagonal matrix $\operatorname{diag}(\lambda_+,\lambda_-)$ into a sign matrix and a positive diagonal matrix. The sign matrix is discrete, and the positive diagonal is the exponential of the real diagonal $(\ln r+\phi,\ln r-\phi)$.

The full case-by-case computation is in *Worked Examples of Exponential Polar Decomposition of Split-Complex Numbers*; the examples here isolate the dictionary.

### The Four Components of One Modulus and One Angle

Take $r=4$ and $\phi=\ln2$. The four components are obtained by the four values of $\epsilon$:

| $\epsilon$ | $Q=r\epsilon\exp(\phi j)$ | $\lambda_+$ | $\lambda_-$ | $(\sigma_+,\sigma_-)$ |
|---|---|---|---|---|
| $1$ | $4(\cosh\ln2+j\sinh\ln2)=5+3j$ | $8$ | $2$ | $(+,+)$ |
| $-1$ | $-5-3j$ | $-8$ | $-2$ | $(-,-)$ |
| $j$ | $4j(\cosh\ln2+j\sinh\ln2)=3+5j$ | $8$ | $-2$ | $(+,-)$ |
| $-j$ | $-3-5j$ | $-8$ | $2$ | $(-,+)$ |

The table is the dictionary in one line: the modulus and the angle are common, and the four sign patterns are the four components. The product $\lambda_+\lambda_-$ is $16$ in the first two rows and $-16$ in the last two, equal to $q^2-q'^2$; the ratio $\lvert\lambda_+/\lambda_-\rvert$ is $4=e^{2\phi}$ in every row.

### From the Spectrum to the Polar Data

| $Q$ | $\lambda_+$ | $\lambda_-$ | $r$ | $\phi$ | $\epsilon$ |
|---|---|---|---|---|---|
| $5+3j$ | $8$ | $2$ | $4$ | $\ln2$ | $1$ |
| $3+5j$ | $8$ | $-2$ | $4$ | $\ln2$ | $j$ |
| $-5-3j$ | $-8$ | $-2$ | $4$ | $\ln2$ | $-1$ |
| $-3-5j$ | $-8$ | $2$ | $4$ | $\ln2$ | $-j$ |
| $3$ | $3$ | $3$ | $3$ | $0$ | $1$ |
| $-3$ | $-3$ | $-3$ | $3$ | $0$ | $-1$ |
| $1+j$ | $2$ | $0$ | — | — | none: zero divisor |

The first four rows have the same modulus and angle and differ only by the component. The scalar rows have a repeated eigenvalue and a vanishing angle. The last row has a distinct spectrum and no polar decomposition: it is the zero-divisor boundary.

### A Direct Check

For $Q=3+5j$, the eigenvalues are $\lambda_+=8$ and $\lambda_-=-2$, so

$$
r=\sqrt{\lvert8\cdot(-2)\rvert}=4,
\qquad
\phi=\tfrac12\ln\left\lvert\frac{8}{-2}\right\rvert=\ln2,
\qquad
(\sigma_+,\sigma_-)=(+,-),
$$

hence $\epsilon=j$. The reconstruction is

$$
4j\exp(j\ln2)=4j\left(\frac54+\frac34j\right)=3+5j.
$$

The exponent is $Q_{\log}=\ln4+j\ln2$, with eigenvalues $\ln4\pm\ln2=\ln8$ and $\ln2$, which are the logarithms of $\lvert\lambda_+\rvert=8$ and $\lvert\lambda_-\rvert=2$. The complex logarithm of $\lambda_-=-2$ is $\ln2+i\pi$; the imaginary part $\pi$ is the spectral sign, carried by $\epsilon=j$ and not by $\phi$.

## Summary

For a split-complex unit $Q=q+jq'$, the eigenvalue decomposition and the exponential polar decomposition are related by

$$
Q=\lambda_+\Pi_++\lambda_-\Pi_-
=r\,\epsilon\exp(\phi j),
\qquad
\lambda_\pm=\sigma_\pm r e^{\pm\phi},
$$

with $\Pi_\pm=\tfrac12(1\pm j)$, $\sigma_\pm=\operatorname{sgn}\lambda_\pm$, $r=\sqrt{\lvert\lambda_+\lambda_-\rvert}$ and $\phi=\tfrac12\ln\lvert\lambda_+/\lambda_-\rvert$. The component sign $\epsilon$ is the spectral sign pair. The dictionary is a bijection on the unit group; the zero divisors have a spectrum but no polar word, and the scalar elements have a repeated eigenvalue and a vanishing angle.

### Main Results

The table collects the formulas in one place.

| Result | Expression |
|---|---|
| Eigenvalues from polar data | $\lambda_\pm=\sigma_\pm r e^{\pm\phi}$ |
| Polar data from eigenvalues | $r=\sqrt{\lvert\lambda_+\lambda_-\rvert}$, $\phi=\tfrac12\ln\lvert\lambda_+/\lambda_-\rvert$ |
| Sign pair | $(\sigma_+,\sigma_-)$ is the spectral reading of $\epsilon$ |
| Factor decompositions | $r=r\Pi_++r\Pi_-$, $\epsilon=\sigma_+\Pi_++\sigma_-\Pi_-$, $e^{\phi j}=e^{\phi}\Pi_++e^{-\phi}\Pi_-$ |
| Exponential on idempotents | $\exp(Q_{\log})=r e^{\phi}\Pi_++r e^{-\phi}\Pi_-$ |
| Product | $\lambda_+\lambda_-=q^2-q'^2=r^2\operatorname{sgn}(q^2-q'^2)$ |
| Ratio | $\lvert\lambda_+/\lambda_-\rvert=e^{2\phi}$ |
| Exponent eigenvalues | $\ln r\pm\phi=\ln\lvert\lambda_\pm\rvert$ |
| Kernel of $\exp$ | $\{0\}$ |
| Fibre of $\exp$ | one point on $F$, empty elsewhere |
| Zero divisors | distinct spectrum, no polar decomposition |
| Scalars | repeated eigenvalue, $\phi=0$, $\epsilon=\operatorname{sgn}q$ |

### The Dictionary Across the Three Algebras

The table compares the three relation articles; in the split-complex column, $\sigma_\pm=\operatorname{sgn}\lambda_\pm$; in the biquaternion column, $\tilde U=U_te_t+\vec U=\tilde Q/(re^{i\alpha})$ is the unit factor and $\vec\Xi=-i\vec Q\bigl(Q_x^2+Q_y^2+Q_z^2\bigr)^{-1/2}$.

| Feature | Split-complex | Reduced biquaternion | Biquaternion |
|---|---|---|---|
| Eigenvalues | $\lambda_\pm=q\pm q'$ | $\lambda_\pm=Q_{\blacktriangle}\pm Q_{\blacktriangledown}$ | $\lambda_\pm=Q_t\pm i\bigl(Q_x^2+Q_y^2+Q_z^2\bigr)^{1/2}$ |
| Eigenprojections | fixed $\Pi_\pm$ | fixed $\Pi_\pm$ | variable $\tilde\Pi_\pm$ |
| Polar parameters | $r,\phi,\epsilon$ | $\rho,\phi,\alpha,\beta$ | $r,\alpha,\psi,\theta,\vec u_{\mathrm b},\vec u_{\mathrm r}$ |
| Eigenvalues from polar data | $\sigma_\pm r e^{\pm\phi}$ | $\rho e^{i\alpha}e^{\pm(\phi+i\beta)}$ | $r e^{i\alpha}\bigl(U_t\pm i(\vec U\cdot\vec U)^{1/2}\bigr)$ |
| Polar factors from spectrum | $r$, $\epsilon=\sigma_+\Pi_++\sigma_-\Pi_-$, $e^{\phi j}=e^{\phi}\Pi_++e^{-\phi}\Pi_-$ | $\breve r=\rho_+\Pi_++\rho_-\Pi_-$, $u=e^{i\theta_+}\Pi_++e^{i\theta_-}\Pi_-$ | $\tilde U=\dfrac{\lambda_+}{r e^{i\alpha}}\tilde\Pi_++\dfrac{\lambda_-}{r e^{i\alpha}}\tilde\Pi_-$, $\tilde U_{\mathrm b}=(\tilde U\tilde U^*)^{1/2}$, $\tilde u_{\mathrm r}=\tilde U_{\mathrm b}^{-1}\tilde U$ |
| Discrete data | $\epsilon\in(\mathbb{Z}/2)^2$ | lattice $\Lambda$ in $(\alpha,\beta)$ | none |
| Polar domain | $q^2-q'^2\neq0$ | $Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2\neq0$ | $Q_t^2+Q_x^2+Q_y^2+Q_z^2\neq0$ |
| Spectral domain | all $Q$ | all $\breve Q$ | $Q_x^2+Q_y^2+Q_z^2\neq0$, or $\vec Q=0$ |
| Zero divisors | spectral, no polar word | spectral, no polar word | spectral, no polar word |
| Zero element | spectral, no polar word | spectral, no polar word | spectral, no polar word |
| Jordan elements | absent | absent | polar word, no two-term spectrum |
| Nilpotent elements | absent | absent | no polar word, no spectrum |

Read down a column for one algebra and across a row for one concept. The first three rows are the common pattern: two eigenvalues, two eigenprojections, a polar word. The fourth and fifth rows are the dictionary; they are explicit in the two commutative cases and obstructed in the noncommutative case by the variable eigenprojections. The last rows record the domain and the degeneracies.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}=\mathbb{R}[j]$, $j^2=1$ | the split-complex algebra |
| $Q=q+jq'$ | a split-complex number |
| $\lambda_\pm=q\pm q'$ | the eigenvalues |
| $\Pi_\pm=\tfrac12(1\pm j)$ | the fixed central idempotents |
| $q^2-q'^2=\lambda_+\lambda_-$ | the product |
| $r=\sqrt{\lvert q^2-q'^2\rvert}$ | the modulus |
| $\phi$ | the hyperbolic angle |
| $\epsilon\in\{\pm1,\pm j\}$ | the component sign |
| $\sigma_\pm=\operatorname{sgn}\lambda_\pm$ | the eigenvalue signs |
| $Q_{\log}=\ln r+j\phi$ | the exponent |
| $\epsilon\exp(\phi j)=Q/r$ | the unit factor |
| $\ker\exp=\{0\}$ | the trivial kernel |
| $\operatorname{sgn}$ | the sign of a nonzero real number |

## Further Reading

- [Worked Examples of Exponential Polar Decomposition of Split-Complex Numbers](worked-examples-of-exponential-polar-decomposition-of-split-complex-numbers.html), for the eight cases and the reconstruction tables.
- [Worked Examples of Exponential Polar Decomposition with Eigenbasis of Split-Complex Numbers](worked-examples-of-exponential-polar-decomposition-with-eigenbasis-of-split-complex-numbers.html), for the same eight cases read in the eigenbasis, with the idempotents and the spinors.
- [Eigenbasis of a Split-Complex Number](eigenbasis-of-a-split-complex-number.html), for the spectrum, the characteristic polynomial, the idempotents and the degenerate regimes.
- [Split-Complex Elementary Functions](split-complex-elementary-functions.html), for the exponential, the logarithm and the branches.
- [Exponential Polar Decomposition of Split-Complex Numbers](exponential-polar-decomposition-of-split-complex-numbers.html), for the decomposition, the components, existence and uniqueness, and the matrix picture.
- [Modulus–Unit Polar Decomposition of Split-Complex Numbers](modulus-unit-polar-decomposition-of-split-complex-numbers.html), for the modulus and the unit factor.
- [Split-Complex Exponential and Lie Group Structure](split-complex-exponential-and-lie-group-structure.html), for the group of units and the exponential parametrisation.
- [Relations between Exponential Polar Decomposition and Eigenbasis a Reduced Biquaternion](relations-between-exponential-polar-decomposition-and-eigenbasis-a-reduced-biquaternion.html), for the reduced biquaternion analogue.
- [Relations between Exponential Polar Decomposition and Eigenbasis of a Biquaternion](relations-between-exponential-polar-decomposition-and-eigenbasis-of-a-biquaternion.html), for the noncommutative analogue.
- [Conventions in Mathematics](conventions-in-mathematics.html), for the notation.
