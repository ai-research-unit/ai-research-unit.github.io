# __Relations between Exponential Polar Decomposition and Eigenbasis a Reduced Biquaternion__

## Introduction

A reduced biquaternion carries two decompositions of the same element. The **eigenvalue decomposition** of *Eigenvalue Decomposition and Eigenbasis of a Reduced Biquaternion* writes $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ as

$$
\breve Q=\lambda_+\Pi_++\lambda_-\Pi_-,
\qquad
\lambda_\pm=Q_\pm=Q_{\blacktriangle}\pm Q_{\blacktriangledown},
\quad
\Pi_\pm=\tfrac12(1\pm j),
$$

with $\lambda_\pm$ the complex eigenvalues and $\Pi_\pm$ the fixed central idempotents. The **exponential polar decomposition** of *Exponential Polar Decomposition of Reduced Biquaternions* writes a unit $\breve Q$ as

$$
\breve Q=\exp(\breve Q_{\log})
=\rho\bigl(\cosh\phi+j\sinh\phi\bigr)\exp(i\alpha)\exp(ij\beta),
\qquad
\breve Q_{\log}=\ln\rho+j\phi+i\alpha+ij\beta,
$$

with $\rho>0$, $\phi\in\mathbb{R}$ and $(\alpha,\beta)$ modulo the lattice $\Lambda$. This article states the dictionary between the two writings. It repeats no proof from the three source articles: the spectrum and the idempotents are those of the eigenvalue article, and the exponential, the logarithm and the polar word are those of the elementary and polar articles.

The two decompositions answer different questions. The spectral writing separates $\breve Q$ into its two complex components $\lambda_+=Q_{\blacktriangle}+Q_{\blacktriangledown}$ and $\lambda_-=Q_{\blacktriangle}-Q_{\blacktriangledown}$, with fixed directions $\Pi_\pm$. The polar writing separates it into a modulus $\breve r=\rho(\cosh\phi+j\sinh\phi)$ and a torus factor $u=\exp(i\alpha)\exp(ij\beta)$, which carry the two real scales $\rho_\pm=\rho e^{\pm\phi}$ and the two phases $\theta_\pm=\alpha\pm\beta$. The dictionary is a change of coordinates on the unit group: the two complex numbers $\lambda_\pm$ are replaced by the four real numbers $(\rho,\phi,\alpha,\beta)$, and the product and ratio of the eigenvalues give the sum and difference of the two phases.

**The results.** The eigenvalues are recovered from the polar data by

$$
\lambda_+=\rho e^{i\alpha}e^{\phi+i\beta},
\qquad
\lambda_-=\rho e^{i\alpha}e^{-\phi-i\beta},
$$

so that

$$
\lambda_+\lambda_-=\rho^2e^{2i\alpha}=Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2,
\qquad
\frac{\lambda_+}{\lambda_-}=e^{2\phi}e^{2i\beta}.
$$

The polar data are recovered from the eigenvalues by

$$
\rho=\sqrt{\lvert\lambda_+\lambda_-\rvert},
\qquad
\phi=\tfrac12\ln\left\lvert\frac{\lambda_+}{\lambda_-}\right\rvert,
\qquad
\alpha=\tfrac12\bigl(\operatorname{Arg}\lambda_++\operatorname{Arg}\lambda_-\bigr),
\qquad
\beta=\tfrac12\bigl(\operatorname{Arg}\lambda_+-\operatorname{Arg}\lambda_-\bigr),
$$

with $\operatorname{Arg}$ the principal argument in $(-\pi,\pi]$. The first two formulas give the modulus and the boost; the last two give the two phases, and the principal diamond selects the representative. The dictionary is a bijection on the unit group, and the exponential's lattice is the spectral ambiguity of the two complex logarithms.

| Question | Answer |
|---|---|
| Element | $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ |
| Eigenvalues | $\lambda_\pm=Q_{\blacktriangle}\pm Q_{\blacktriangledown}$ |
| Eigenprojections | $\Pi_\pm=\tfrac12(1\pm j)$, fixed and central |
| Polar parameters | $\rho>0$, $\phi\in\mathbb{R}$, $(\alpha,\beta)\in\mathbb{R}^2/\Lambda$ |
| Eigenvalues from polar data | $\lambda_\pm=\rho e^{i\alpha}e^{\pm(\phi+i\beta)}$ |
| Polar data from eigenvalues | $\rho=\sqrt{\lvert\lambda_+\lambda_-\rvert}$, $\phi=\tfrac12\ln\lvert\lambda_+/\lambda_-\rvert$ |
| Phases from eigenvalues | $\alpha=\tfrac12(\operatorname{Arg}\lambda_++\operatorname{Arg}\lambda_-)$, $\beta=\tfrac12(\operatorname{Arg}\lambda_+-\operatorname{Arg}\lambda_-)$ |
| Factor decompositions | $\breve r=\rho_+\Pi_++\rho_-\Pi_-$ with $\rho_\pm=\rho e^{\pm\phi}$; $u=e^{i\theta_+}\Pi_++e^{i\theta_-}\Pi_-$ with $\theta_\pm=\alpha\pm\beta$ |
| Exponential on idempotents | $\exp(\breve Q_{\log})=\lambda_+\Pi_++\lambda_-\Pi_-$ |
| Product | $\lambda_+\lambda_-=Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2$ |
| Ratio | $\lambda_+/\lambda_-=e^{2\phi}e^{2i\beta}$ |
| Common domain | the units, $Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2\neq0$ |
| Spectral domain | all $\breve Q$; the zero divisors have a spectrum but no polar word |
| Kernel | $2\pi i\mathbb{Z}\oplus\pi i(1+j)\mathbb{Z}\cong\mathbb{Z}^2$ |

## The Two Decompositions

### The Eigenvalue Decomposition

For $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$, the spectrum is

$$
\sigma(\breve Q)=\{\lambda_+,\lambda_-\}
=\{Q_{\blacktriangle}+Q_{\blacktriangledown},\,Q_{\blacktriangle}-Q_{\blacktriangledown}\}.
$$

The eigenvalues are complex, and they are distinct exactly when $Q_{\blacktriangledown}\neq0$. In that case

$$
\boxed{\;
\breve Q=\lambda_+\Pi_++\lambda_-\Pi_-,
\qquad
\Pi_\pm=\frac{1\pm j}{2}
\;},
$$

with $\Pi_\pm$ primitive, orthogonal, complete and central. These are the statements of *Eigenvalue Decomposition and Eigenbasis of a Reduced Biquaternion*, §*The Spectrum and the Characteristic Polynomial*, §*The Eigenprojections* and §*The Eigenvalue Decomposition*. In the scalar case $Q_{\blacktriangledown}=0$, the eigenvalue is repeated, $\lambda_+=\lambda_-=Q_{\blacktriangle}$, and the decomposition is the one-term writing $\breve Q=Q_{\blacktriangle}\cdot1$.

| Spectral item | Value |
|---|---|
| Spectrum | $\{\lambda_+,\lambda_-\}=\{Q_{\blacktriangle}+Q_{\blacktriangledown},Q_{\blacktriangle}-Q_{\blacktriangledown}\}$ |
| Sum | $\lambda_++\lambda_-=2Q_{\blacktriangle}$ |
| Product | $\lambda_+\lambda_-=Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2$ |
| Distinctness | $\lambda_+\neq\lambda_-\iff Q_{\blacktriangledown}\neq0$ |
| Eigenprojections | $\Pi_\pm=\tfrac12(1\pm j)$ |
| Decomposition | $\breve Q=\lambda_+\Pi_++\lambda_-\Pi_-$ |

### The Exponential Polar Decomposition

Every unit $\breve Q\in\mathbb{B}_{\mathrm{r}}^\times=\{Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2\neq0\}$ has a unique writing

$$
\boxed{\;
\breve Q=\exp(\breve Q_{\log})
=\breve r\,u,
\qquad
\breve Q_{\log}=\ln\rho+j\phi+i\alpha+ij\beta
\;},
$$

with

$$
\breve r=\rho(\cosh\phi+j\sinh\phi),
\qquad
u=\exp(i\alpha)\exp(ij\beta),
$$

and $\rho>0$, $\phi\in\mathbb{R}$, $(\alpha,\beta)$ in the principal diamond $\lvert\alpha\rvert+\lvert\beta\rvert\le\pi$ (boundary half-open). The factor $\breve r$ is the modulus, $u$ the unit factor, $\phi$ the boost, and $\alpha,\beta$ the two phases. These are the statements of *Exponential Polar Decomposition of Reduced Biquaternions*, §*The Decomposition*, §*Existence and Uniqueness* and §*The Exponential Coordinates*.

| Polar item | Value |
|---|---|
| Domain | $\mathbb{B}_{\mathrm{r}}^\times=\{\breve Q:Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2\neq0\}$ |
| Decomposition | $\breve Q=\breve r\,u=\rho(\cosh\phi+j\sinh\phi)\exp(i\alpha)\exp(ij\beta)$ |
| Modulus | $\breve r=\rho(\cosh\phi+j\sinh\phi)$, $\rho>0$ |
| Unit factor | $u=\exp(i\alpha)\exp(ij\beta)$ |
| Parameters | $\ln\rho,\phi\in\mathbb{R}$; $(\alpha,\beta)\in\mathbb{R}^2/\Lambda$ |
| Principal domain | $\lvert\alpha\rvert+\lvert\beta\rvert\le\pi$ |
| Kernel | $2\pi i\mathbb{Z}\oplus\pi i(1+j)\mathbb{Z}\cong\mathbb{Z}^2$ |
| Fibre of the exponential | $\operatorname{Log}\breve Q+\ker\exp\cong\mathbb{Z}^2$ |

### The Common Domain

The spectral decomposition exists for every $\breve Q$, including the zero divisors and the zero element. The polar decomposition exists exactly on the units. The two conditions that separate the regimes are

$$
Q_{\blacktriangledown}\neq0\quad\text{(distinct eigenvalues)},
\qquad
Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2=\lambda_+\lambda_-\neq0\quad\text{(invertibility)}.
$$

They are independent: a zero divisor has $Q_{\blacktriangledown}\neq0$ and $Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2=0$, so it has two distinct eigenvalues and no polar word. The table records the four possibilities.

| Condition | Spectrum | Polar decomposition |
|---|---|---|
| $Q_{\blacktriangledown}\neq0$, $Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2\neq0$ | two distinct nonzero eigenvalues | exists, unique in the principal diamond |
| $Q_{\blacktriangledown}\neq0$, $Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2=0$ | two distinct eigenvalues, one zero | does not exist: $\breve Q$ is a zero divisor |
| $Q_{\blacktriangledown}=0$, $Q_{\blacktriangle}^2\neq0$ | one repeated nonzero eigenvalue | exists with $\phi=\beta=0$ and $u=\exp(i\alpha)$ |
| $Q_{\blacktriangledown}=0$, $Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2=0$ | the eigenvalue $0$ | does not exist: $\breve Q=0$ |

The spectral domain is strictly larger than the polar domain. The gap is exactly the null set $Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2=0$: the nonzero zero divisors and the zero element, on which the eigenvalue decomposition survives and the logarithm does not.

## The Dictionary

### The Eigenvalues from the Polar Parameters

Let $\breve Q=\rho(\cosh\phi+j\sinh\phi)\exp(i\alpha)\exp(ij\beta)$ be a unit. Since $\breve Q\Pi_\pm=\lambda_\pm\Pi_\pm$, $j\Pi_+=\Pi_+$ and $j\Pi_-=-\Pi_-$, the eigenvalue on $\Pi_+$ is the coefficient of $\Pi_+$:

$$
\lambda_+=\rho e^{i\alpha}\bigl(\cosh\phi+\sinh\phi\bigr)\bigl(\cos\beta+i\sin\beta\bigr)
=\rho e^{i\alpha}e^{\phi}e^{i\beta}
=\rho e^{i\alpha}e^{\phi+i\beta},
$$

and on $\Pi_-$ the signs of $\phi$ and $\beta$ are reversed:

$$
\lambda_-=\rho e^{i\alpha}e^{-\phi}e^{-i\beta}
=\rho e^{i\alpha}e^{-\phi-i\beta}.
$$

The two formulas are the componentwise reading of the closed form: the scalar factor $\rho e^{i\alpha}$ multiplies both eigenvalues, and the split factor $\phi+i\beta$ enters with opposite signs. The table collects the data.

| Quantity | Value |
|---|---|
| Eigenvalues | $\lambda_\pm=\rho e^{i\alpha}e^{\pm(\phi+i\beta)}$ |
| Product | $\lambda_+\lambda_-=\rho^2e^{2i\alpha}=Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2$ |
| Ratio | $\lambda_+/\lambda_-=e^{2(\phi+i\beta)}=e^{2\phi}e^{2i\beta}$ |
| Moduli | $\lvert\lambda_\pm\rvert=\rho e^{\pm\phi}$ |
| Arguments | $\operatorname{Arg}\lambda_\pm=\alpha\pm\beta$ (mod $2\pi$) |
| Sum of arguments | $\operatorname{Arg}\lambda_++\operatorname{Arg}\lambda_-=2\alpha$ (mod $2\pi$) |
| Difference of arguments | $\operatorname{Arg}\lambda_+-\operatorname{Arg}\lambda_-=2\beta$ (mod $2\pi$) |

The product gives the modulus and the total phase; the ratio gives the boost and the relative phase:

$$
Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2=\rho^2e^{2i\alpha},
\qquad
\frac{\lambda_+}{\lambda_-}=e^{2\phi}e^{2i\beta}.
$$

The polar parameters are therefore the polar coordinates of the product and the ratio, with the branch fixed by the principal diamond. This is the exact structural difference from the split-complex case: the modulus of the ratio is a positive real number and carries only the boost; here it is a nonzero complex number and carries the boost and one phase.

### The Polar Parameters from the Eigenvalues

For a unit $\breve Q=\lambda_+\Pi_++\lambda_-\Pi_-$, the modulus and the boost are

$$
\rho=\sqrt{\lvert\lambda_+\lambda_-\rvert}=\sqrt{\lvert Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2\rvert},
\qquad
\phi=\tfrac12\ln\left\lvert\frac{\lambda_+}{\lambda_-}\right\rvert.
$$

The phases are read from the principal arguments:

$$
\alpha=\tfrac12\bigl(\operatorname{Arg}\lambda_++\operatorname{Arg}\lambda_-\bigr),
\qquad
\beta=\tfrac12\bigl(\operatorname{Arg}\lambda_+-\operatorname{Arg}\lambda_-\bigr),
$$

so that $\alpha+\beta=\operatorname{Arg}\lambda_+$ and $\alpha-\beta=\operatorname{Arg}\lambda_-$. The principal diamond contains the pair: $\lvert\alpha\rvert+\lvert\beta\rvert=\max(\lvert\operatorname{Arg}\lambda_+\rvert,\lvert\operatorname{Arg}\lambda_-\rvert)\le\pi$. The formulas for $\alpha$ and $\beta$ use the individual arguments, not the argument of the product or of the ratio: the latter are defined only modulo $2\pi$ and their halves only modulo $\pi$, which is the lattice ambiguity.

**Proposition (the dictionary).** On the unit group, the map

$$
\boxed{\;
(\rho,\phi,\alpha,\beta)\longmapsto
(\lambda_+,\lambda_-)
=\bigl(\rho e^{i\alpha}e^{\phi+i\beta},\ \rho e^{i\alpha}e^{-\phi-i\beta}\bigr)
\;}
$$

is a bijection from $\{\rho>0,\ \phi\in\mathbb{R},\ \lvert\alpha\rvert+\lvert\beta\rvert\le\pi\}$, with the boundary half-open, onto the set of pairs of nonzero complex numbers. Its inverse is the formula above.

*Proof.* The map is the coordinate change of *Exponential Polar Decomposition of Reduced Biquaternions*, §*The Four Real Coordinates*, with $C_\pm=\lambda_\pm$; its inverse and its lattice ambiguity are established there. The only new point is the identification $C_\pm=\lambda_\pm$, which is the eigenvalue formula of *Eigenvalue Decomposition and Eigenbasis of a Reduced Biquaternion*.

The inverse formulas are collected in the table.

| Polar parameter | Spectral formula | Range |
|---|---|---|
| $\rho$ | $\lvert\lambda_+\lambda_-\rvert^{1/2}$ | $(0,\infty)$ |
| $\phi$ | $\tfrac12\ln\lvert\lambda_+/\lambda_-\rvert$ | $\mathbb{R}$ |
| $\alpha$ | $\tfrac12(\operatorname{Arg}\lambda_++\operatorname{Arg}\lambda_-)$ | $\lvert\alpha\rvert+\lvert\beta\rvert\le\pi$ |
| $\beta$ | $\tfrac12(\operatorname{Arg}\lambda_+-\operatorname{Arg}\lambda_-)$ | $\lvert\alpha\rvert+\lvert\beta\rvert\le\pi$ |

### The Eigenprojections

The eigenprojections are the fixed idempotents $\Pi_\pm$; they do not depend on $\breve Q$ and are not part of the polar data. In the polar writing they read the two factors separately:

$$
\breve Q=\breve r\,u
=\rho_+e^{i\theta_+}\Pi_++\rho_-e^{i\theta_-}\Pi_-,
\qquad
u=e^{i\theta_+}\Pi_++e^{i\theta_-}\Pi_-,
$$

with

$$
\rho_\pm=\rho e^{\pm\phi},
\qquad
\theta_+=\alpha+\beta,
\quad
\theta_-=\alpha-\beta.
$$

The modulus has eigenvalues $\rho_\pm$, the unit factor has eigenvalues $e^{i\theta_\pm}$, and the product has eigenvalues $\lambda_\pm=\rho_\pm e^{i\theta_\pm}$. The exponent has eigenvalues $\ln\rho_\pm+i\theta_\pm$, which are logarithms of $\lambda_\pm$. The table records the three levels.

| Object | Eigenvalue decomposition | Polar reading |
|---|---|---|
| $\breve Q$ | $\lambda_+\Pi_++\lambda_-\Pi_-$ | $\breve r\,u$ |
| Modulus $\breve r$ | $\rho_+\Pi_++\rho_-\Pi_-$ | $\rho(\cosh\phi+j\sinh\phi)$ |
| Unit factor $u$ | $e^{i\theta_+}\Pi_++e^{i\theta_-}\Pi_-$ | $\exp(i\alpha)\exp(ij\beta)$ |
| Exponent $\breve Q_{\log}$ | $(\ln\rho_++i\theta_+)\Pi_++(\ln\rho_-+i\theta_-)\Pi_-$ | $\ln\rho+j\phi+i\alpha+ij\beta$ |

The table shows the division of labour: the modulus carries the two scales $\rho_\pm$, the unit factor carries the two phases $\theta_\pm$, and the exponent carries the two complex logarithms. The idempotents are fixed at every level.

### The Factors One by One

Each factor of the polar word has its own spectral decomposition on the fixed idempotents:

$$
\rho=\rho\Pi_++\rho\Pi_-,
\qquad
\cosh\phi+j\sinh\phi=e^{\phi}\Pi_++e^{-\phi}\Pi_-,
$$

$$
e^{i\alpha}=e^{i\alpha}\Pi_++e^{i\alpha}\Pi_-,
\qquad
e^{ij\beta}=e^{i\beta}\Pi_++e^{-i\beta}\Pi_-.
$$

The modulus, the unit factor and the element follow:

$$
\breve r=\rho(\cosh\phi+j\sinh\phi)
=\rho e^{\phi}\Pi_++\rho e^{-\phi}\Pi_-,
$$

$$
u=e^{i\alpha}e^{ij\beta}
=e^{i(\alpha+\beta)}\Pi_++e^{i(\alpha-\beta)}\Pi_-,
\qquad
\breve Q=\breve r u
=\lambda_+\Pi_++\lambda_-\Pi_-.
$$

The table collects the seven levels.

| Factor | Closed form | Spectral decomposition | Eigenvalues |
|---|---|---|---|
| Radius | $\rho$ | $\rho\Pi_++\rho\Pi_-$ | $\rho,\rho$ |
| Boost factor | $\cosh\phi+j\sinh\phi$ | $e^{\phi}\Pi_++e^{-\phi}\Pi_-$ | $e^{\phi},e^{-\phi}$ |
| Central phase | $e^{i\alpha}$ | $e^{i\alpha}\Pi_++e^{i\alpha}\Pi_-$ | $e^{i\alpha},e^{i\alpha}$ |
| Relative phase | $e^{ij\beta}$ | $e^{i\beta}\Pi_++e^{-i\beta}\Pi_-$ | $e^{i\beta},e^{-i\beta}$ |
| Modulus | $\breve r=\rho(\cosh\phi+j\sinh\phi)$ | $\rho_+\Pi_++\rho_-\Pi_-$ | $\rho_\pm=\rho e^{\pm\phi}$ |
| Unit factor | $u=e^{i\alpha}e^{ij\beta}$ | $e^{i\theta_+}\Pi_++e^{i\theta_-}\Pi_-$ | $e^{i\theta_\pm}$ |
| Element | $\breve Q=\breve r u$ | $\lambda_+\Pi_++\lambda_-\Pi_-$ | $\lambda_\pm=\rho e^{i\alpha}e^{\pm(\phi+i\beta)}$ |

The central phase has the same eigenvalue on both idempotents; the relative phase is the factor that distinguishes them. This is the reduced-biquaternion analogue of the boost and rotor split: the boost $\phi$ and the relative phase $\beta$ act with opposite signs, while the total phase $\alpha$ acts with the same sign.

### The Exponential on the Idempotents

The exponent splits as

$$
\breve Q_{\log}=\ln\rho+j\phi+i\alpha+ij\beta
=(\ln\rho+\phi+i\theta_+)\Pi_++(\ln\rho-\phi+i\theta_-)\Pi_-,
$$

with $\theta_\pm=\alpha\pm\beta$. Its exponential acts on the two idempotents by

$$
\exp(\breve Q_{\log})
=e^{\ln\rho+\phi+i\theta_+}\Pi_++e^{\ln\rho-\phi+i\theta_-}\Pi_-
=\rho_+e^{i\theta_+}\Pi_++\rho_-e^{i\theta_-}\Pi_-
=\lambda_+\Pi_++\lambda_-\Pi_-=\breve Q.
$$

The eigenvalues of the exponent are $\ln\rho_\pm+i\theta_\pm$, the principal complex logarithms of $\lambda_\pm$; the eigenvalues of $\breve Q$ are their exponentials. The lattice $\Lambda$ is exactly the ambiguity of the two logarithms: adding $2\pi i m$ on $\Pi_+$ and $2\pi i n$ on $\Pi_-$ leaves the exponential unchanged, and the principal diamond selects one representative.

### What Each Side Carries

| Spectral datum | What it fixes | Formula | What it leaves free |
|---|---|---|---|
| $\lambda_+\lambda_-$ | radius and total phase | $\rho=\lvert\lambda_+\lambda_-\rvert^{1/2}$, $2\alpha=\arg(\lambda_+\lambda_-)$ | $\alpha$ modulo $\pi$ |
| $\lambda_+/\lambda_-$ | boost and relative phase | $\phi=\tfrac12\ln\lvert\lambda_+/\lambda_-\rvert$, $2\beta=\arg(\lambda_+/\lambda_-)$ | $\beta$ modulo $\pi$ |
| Individual arguments | the representative | $\theta_\pm=\operatorname{Arg}\lambda_\pm$, $\alpha=\tfrac12(\theta_++\theta_-)$, $\beta=\tfrac12(\theta_+-\theta_-)$ | — (the representative is fixed) |
| $\lambda_\pm$ | the element | $\breve Q=\lambda_+\Pi_++\lambda_-\Pi_-$ | — |
| $\rho,\phi,\alpha,\beta$ | the element | $\breve Q=\rho(\cosh\phi+j\sinh\phi)e^{i\alpha}e^{ij\beta}$ | the lattice |
| $\breve Q_{\log}$ | the element | $\exp(\breve Q_{\log})=\breve Q$ | the kernel lattice |

The product and the ratio determine $\alpha$ and $\beta$ only modulo $\pi$; the individual arguments fix the representative in the principal diamond, and then the dictionary is a bijection. There is no continuous free direction once the individual arguments are used: the eigenprojections are fixed, so the four polar parameters are coordinates on the unit group, not a section of a larger word map.

## The Regimes

The spectral regimes of the eigenvalue article and the polar coordinates fit together as follows.

| Regime | Condition | Spectral data | Polar data |
|---|---|---|---|
| Distinct interior | $Q_{\blacktriangledown}\neq0$, $Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2\neq0$ | $\lambda_+\neq\lambda_-$, both nonzero | $\rho>0$, $\phi\in\mathbb{R}$, $(\alpha,\beta)$ in the diamond |
| Zero divisor | $Q_{\blacktriangledown}\neq0$, $Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2=0$ | $\lambda_+\neq\lambda_-$, one zero | none: not a unit |
| Scalar nonzero | $Q_{\blacktriangledown}=0$, $Q_{\blacktriangle}\neq0$ | $\lambda_+=\lambda_-=Q_{\blacktriangle}$ | $\rho=\lvert Q_{\blacktriangle}\rvert$, $\phi=0$, $\beta=0$, $\alpha=\operatorname{Arg}Q_{\blacktriangle}$ |
| Zero | $Q_{\blacktriangle}=Q_{\blacktriangledown}=0$ | $\lambda_+=\lambda_-=0$ | none |
| Jordan | absent: the algebra is reduced | — | — |
| Nilpotent | absent: only $\breve Q=0$ | — | — |

### The Zero-Divisor Regime

A nonzero zero divisor has $Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2=0$ and $Q_{\blacktriangledown}\neq0$, so $\lambda_+\lambda_-=0$ and one eigenvalue vanishes. The element is a nonzero complex multiple of one of the fixed idempotents,

$$
\breve Q=\lambda_+\Pi_+\quad\text{or}\quad\breve Q=\lambda_-\Pi_-,
\qquad
\Pi_\pm=\tfrac12(1\pm j).
$$

Its spectrum is distinct, and the eigenvalue decomposition exists. The polar decomposition does not: the boost formula diverges, $\phi=\tfrac12\ln\lvert\lambda_+/\lambda_-\rvert\to\pm\infty$, when one eigenvalue is zero, and the complex logarithm of the zero eigenvalue does not exist. The zero-divisor set is the boundary of the polar domain, not a spectral degeneration.

### The Scalar Regime

For $\breve Q=Q_{\blacktriangle}$ with $Q_{\blacktriangle}\neq0$, the two eigenvalues coincide at $Q_{\blacktriangle}$. The polar data are $\rho=\lvert Q_{\blacktriangle}\rvert$, $\phi=0$, $\beta=0$ and $\alpha=\operatorname{Arg}Q_{\blacktriangle}$; the unit factor is $e^{i\alpha}$, the complex phase of $Q_{\blacktriangle}$. The repeated eigenvalue is therefore not a repeated polar datum: the boost and the relative phase vanish, and the two-term spectral writing collapses to $\breve Q=Q_{\blacktriangle}\Pi_++Q_{\blacktriangle}\Pi_-$, while the polar writing keeps the modulus and the single phase.

### The Absence of the Jordan and Nilpotent Regimes

The algebra is $\mathbb{C}\times\mathbb{C}$, hence reduced. There is no nonzero nilpotent, so there is no Jordan-block regime and no nilpotent boundary. Every element is semisimple; the only spectral degeneracy is the scalar case, and the only polar boundary is the zero-divisor set. This is the structural difference from the biquaternion dictionary, where the Jordan and nilpotent regimes are nonempty and the eigenprojections vary.

## The Exponential and the Logarithm

### The Kernel

The exponential of $\mathbb{B}_{\mathrm{r}}$ has kernel

$$
\ker\exp=2\pi i(\mathbb{Z}\Pi_+\oplus\mathbb{Z}\Pi_-)
=2\pi i\mathbb{Z}\oplus\pi i(1+j)\mathbb{Z}\cong\mathbb{Z}^2,
$$

generated by $2\pi i$ and $\pi i(1+j)$ (*Reduced Biquaternion Elementary Functions*, §*The Kernel and the Image*). In spectral terms, a logarithm is a pair $(\log\lambda_+,\log\lambda_-)$, and adding $2\pi i k$ to the first and $2\pi i l$ to the second gives the same element. In the phases this is

$$
(\alpha,\beta)\longmapsto\bigl(\alpha+\pi(k+l),\ \beta+\pi(k-l)\bigr),
$$

which is the lattice $\Lambda=\langle(2\pi,0),(\pi,\pi)\rangle$. The scalar period $2\pi i$ shifts $(\alpha,\beta)$ by $(2\pi,0)$; the split period $\pi i(1+j)$ shifts it by $(\pi,\pi)$. The period $\pi i(1-j)$ shifts it by $(\pi,-\pi)$ and is the difference of the other two modulo $2\pi$.

| Kernel element | Shift in $(\log\lambda_+,\log\lambda_-)$ | Shift in $(\alpha,\beta)$ |
|---|---|---|
| $2\pi i$ | $(2\pi i,2\pi i)$ | $(2\pi,0)$ |
| $\pi i(1+j)$ | $(2\pi i,0)$ | $(\pi,\pi)$ |
| $\pi i(1-j)$ | $(0,2\pi i)$ | $(\pi,-\pi)$ |

### The Fibre

For a unit $\breve Q$, the fibre of the exponential is

$$
\exp^{-1}(\breve Q)=\operatorname{Log}\breve Q+\ker\exp\cong\mathbb{Z}^2.
$$

In the principal diamond exactly one point of the fibre lies, so the polar data $(\rho,\phi,\alpha,\beta)$ are unique in the diamond and unique modulo $\Lambda$ in general. This is the spectral content of the uniqueness theorem of *Exponential Polar Decomposition of Reduced Biquaternions*: the ambiguity is one integer for each eigenvalue, and the diamond is a fundamental domain for the two integers.

| Item | Value |
|---|---|
| Kernel | $\mathbb{Z}^2$, generated by $2\pi i$ and $\pi i(1+j)$ |
| Fibre | $\operatorname{Log}\breve Q+\mathbb{Z}^2$ |
| Fundamental domain | $\lvert\alpha\rvert+\lvert\beta\rvert\le\pi$, area $2\pi^2$ |
| Spectral coordinates of the exponent | $(\log\lambda_+,\log\lambda_-)$ modulo $2\pi i\mathbb{Z}^2$ |
| Polar coordinates | $(\ln\rho,\phi,\alpha,\beta)$ with $(\alpha,\beta)$ modulo $\Lambda$ |

The table records the exact correspondence: the two integer ambiguities of the spectral logarithms are the two integer ambiguities of the phases, and the principal diamond is the image of the product of the two principal strips.

## The Matrix Picture

In the complex basis $\{1,j\}$ the left multiplication by $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ is

$$
\mathsf M(\breve Q)=\begin{pmatrix}Q_{\blacktriangle}&Q_{\blacktriangledown}\\Q_{\blacktriangledown}&Q_{\blacktriangle}\end{pmatrix},
\qquad
S=\begin{pmatrix}1&1\\1&-1\end{pmatrix},
\qquad
S\,\mathsf M(\breve Q)\,S^{-1}
=\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}.
$$

The polar decomposition is the same identity read through the two factors:

$$
\mathsf M(\breve Q)=\mathsf M(\breve r)\,\mathsf M(u),
$$

with

$$
\mathsf M(\breve r)=\begin{pmatrix}\rho\cosh\phi&\rho\sinh\phi\\\rho\sinh\phi&\rho\cosh\phi\end{pmatrix},
\qquad
\mathsf M(u)=\begin{pmatrix}e^{i\alpha}\cos\beta&ie^{i\alpha}\sin\beta\\ie^{i\alpha}\sin\beta&e^{i\alpha}\cos\beta\end{pmatrix}.
$$

The first has eigenvalues $\rho e^{\pm\phi}=\rho_\pm$; the second has eigenvalues $e^{i(\alpha\pm\beta)}=e^{i\theta_\pm}$; the product has eigenvalues $\lambda_\pm=\rho_\pm e^{i\theta_\pm}$. The diagonalisation by $S$ is the matrix form of the dictionary.

| Matrix | Eigenvalues | Spectral role |
|---|---|---|
| $\mathsf M(\breve Q)$ | $\lambda_+,\lambda_-$ | the element |
| $\mathsf M(\breve r)$ | $\rho e^{\phi},\rho e^{-\phi}$ | the modulus and the boost |
| $\mathsf M(u)$ | $e^{i(\alpha+\beta)},e^{i(\alpha-\beta)}$ | the two phases |
| $S\,\mathsf M(\breve Q)\,S^{-1}$ | $\lambda_+,\lambda_-$ | the diagonal form |

The matrix picture shows that the polar decomposition is the factorisation of the diagonal matrix $\operatorname{diag}(\lambda_+,\lambda_-)$ into a positive real diagonal factor $\operatorname{diag}(\rho e^\phi,\rho e^{-\phi})$ and a unitary diagonal factor $\operatorname{diag}(e^{i\theta_+},e^{i\theta_-})$. The boost is the logarithm of the ratio of the two positive scales; the phases are the arguments.

The full case-by-case computation is in *Worked Examples of Exponential Polar Decomposition of Reduced Biquaternions*; the examples here isolate the dictionary.

### A Generic Element

Take $\breve Q=3+4i+j(1-i)$, with $Q_{\blacktriangle}=3+4i$ and $Q_{\blacktriangledown}=1-i$. The eigenvalues are

$$
\lambda_+=Q_{\blacktriangle}+Q_{\blacktriangledown}=4+3i,
\qquad
\lambda_-=Q_{\blacktriangle}-Q_{\blacktriangledown}=2+5i.
$$

The dictionary gives

$$
\rho=\sqrt{\lvert(4+3i)(2+5i)\rvert}=\sqrt{5\sqrt{29}}=5.189009928268833,
\qquad
\ln\rho=1.6465429137136687,
$$

$$
\phi=\tfrac12\ln\left\lvert\frac{4+3i}{2+5i}\right\rvert
=\tfrac12\ln\frac{5}{\sqrt{29}}=-0.03710500127956826,
$$

and

$$
\alpha=\tfrac12\bigl(\operatorname{Arg}(4+3i)+\operatorname{Arg}(2+5i)\bigr)=0.916895529237908,
$$

$$
\beta=\tfrac12\bigl(\operatorname{Arg}(4+3i)-\operatorname{Arg}(2+5i)\bigr)=-0.27339442044462364.
$$

The exponent is

$$
\operatorname{Log}\breve Q=1.6465429137+0.9168955292\,i
-0.0371050013\,j-0.2733944204\,ij,
$$

and the reconstruction is

$$
\exp(\operatorname{Log}\breve Q)=3+4i+j(1-i),
$$

with Euclidean error $1.9\times10^{-15}$. The product and ratio are

$$
\lambda_+\lambda_-=-7+26i,
\qquad
\frac{\lambda_+}{\lambda_-}=\frac{23-14i}{29},
$$

whose modulus and arguments give $\rho^2=5\sqrt{29}$ and $2\alpha,2\beta$.

### A Table of Examples

| $\breve Q$ | $\lambda_+$ | $\lambda_-$ | $\rho$ | $\phi$ | $\alpha$ | $\beta$ |
|---|---|---|---|---|---|---|
| $3+4i+j(1-i)$ | $4+3i$ | $2+5i$ | $5.1890099283$ | $-0.0371050013$ | $0.9168955292$ | $-0.2733944204$ |
| $1+i$ | $1+i$ | $1+i$ | $\sqrt2$ | $0$ | $\pi/4$ | $0$ |
| $i$ | $i$ | $i$ | $1$ | $0$ | $\pi/2$ | $0$ |
| $ij$ | $i$ | $-i$ | $1$ | $0$ | $0$ | $\pi/2$ |
| $j$ | $1$ | $-1$ | $1$ | $0$ | $\pi/2$ | $-\pi/2$ |
| $\exp(j\ln2)$ | $2$ | $1/2$ | $1$ | $\ln2$ | $0$ | $0$ |
| $-1$ | $-1$ | $-1$ | $1$ | $0$ | $\pi$ | $0$ |

The scalar rows $1+i$, $i$ and $-1$ have $Q_{\blacktriangledown}=0$ and repeated eigenvalues; the row $ij$ has $Q_{\blacktriangle}=0$ and $Q_{\blacktriangledown}=i$, so $\lambda_+=i$ and $\lambda_-=-i$ are distinct; the row $j$ has $\lambda_+=1$ and $\lambda_-=-1$. The zero divisor $1+j$ has $\lambda_+=2$, $\lambda_-=0$ and no polar row.

### The Hyperbolic Line and the Phases

For $\breve Q=\exp(j\phi)=\cosh\phi+j\sinh\phi$ the eigenvalues are $e^{\phi}$ and $e^{-\phi}$, both positive real; the dictionary gives $\rho=1$, $\phi=\phi$, $\alpha=\beta=0$. For $\breve Q=i$ the two eigenvalues are both $i$; the dictionary gives $\rho=1$, $\phi=0$, $\alpha=\pi/2$, $\beta=0$. For $\breve Q=ij$ the eigenvalues are $i$ and $-i$; the dictionary gives $\rho=1$, $\phi=0$, $\alpha=0$, $\beta=\pi/2$. For $\breve Q=j$ the eigenvalues are $1$ and $-1$; the dictionary gives $\rho=1$, $\phi=0$, $\alpha=\pi/2$, $\beta=-\pi/2$, on the boundary of the principal diamond. These are the same four cases as in *Worked Examples of Exponential Polar Decomposition of Reduced Biquaternions*, cases 3 to 6, read through the spectrum.

### The Kernel and the Branch

The element $-1$ has the four corner logarithms

$$
i\pi,\qquad -i\pi,\qquad i\pi j,\qquad -i\pi j,
$$

with exponents $(\alpha,\beta)=(\pi,0),(-\pi,0),(0,\pi),(0,-\pi)$, all with exponential $-1$. The differences are generated by the kernel elements $2\pi i$, $\pi i(1+j)$ and $\pi i(1-j)$. In spectral terms, the two eigenvalues of $-1$ are both $-1$, and the four logarithms are the four choices of the argument $\pm\pi$ in each eigenvalue; the principal choice $(\theta_+,\theta_-)=(\pi,\pi)$, that is $(\alpha,\beta)=(\pi,0)$, gives $i\pi$, and the other three are obtained by adding kernel elements. This is the rank-two non-uniqueness in its simplest form.

## Summary

For a reduced biquaternion unit $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$, the eigenvalue decomposition and the exponential polar decomposition are related by

$$
\breve Q=\lambda_+\Pi_++\lambda_-\Pi_-
=\rho(\cosh\phi+j\sinh\phi)\exp(i\alpha)\exp(ij\beta),
$$

with

$$
\lambda_\pm=\rho e^{i\alpha}e^{\pm(\phi+i\beta)},
\qquad
\rho=\sqrt{\lvert\lambda_+\lambda_-\rvert},
\qquad
\phi=\tfrac12\ln\left\lvert\frac{\lambda_+}{\lambda_-}\right\rvert,
$$

and

$$
\alpha=\tfrac12\bigl(\operatorname{Arg}\lambda_++\operatorname{Arg}\lambda_-\bigr),
\qquad
\beta=\tfrac12\bigl(\operatorname{Arg}\lambda_+-\operatorname{Arg}\lambda_-\bigr).
$$

The polar parameters are unique in the principal diamond and unique modulo the lattice $\Lambda$ in general. The zero divisors have a spectrum but no polar word; the scalar elements have a repeated eigenvalue and a vanishing boost and relative phase.

### Main Results

The table collects the formulas in one place.

| Result | Expression |
|---|---|
| Eigenvalues from polar data | $\lambda_\pm=\rho e^{i\alpha}e^{\pm(\phi+i\beta)}$ |
| Polar data from eigenvalues | $\rho=\sqrt{\lvert\lambda_+\lambda_-\rvert}$, $\phi=\tfrac12\ln\lvert\lambda_+/\lambda_-\rvert$ |
| Phases from eigenvalues | $\alpha=\tfrac12(\operatorname{Arg}\lambda_++\operatorname{Arg}\lambda_-)$, $\beta=\tfrac12(\operatorname{Arg}\lambda_+-\operatorname{Arg}\lambda_-)$ |
| Factor decompositions | $\breve r=\rho_+\Pi_++\rho_-\Pi_-$ with $\rho_\pm=\rho e^{\pm\phi}$; $u=e^{i\theta_+}\Pi_++e^{i\theta_-}\Pi_-$ with $\theta_\pm=\alpha\pm\beta$ |
| Exponential on idempotents | $\exp(\breve Q_{\log})=\lambda_+\Pi_++\lambda_-\Pi_-$ |
| Product | $\lambda_+\lambda_-=Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2=\rho^2e^{2i\alpha}$ |
| Ratio | $\lambda_+/\lambda_-=e^{2\phi}e^{2i\beta}$ |
| Exponent eigenvalues | $\log\lambda_\pm=\ln\rho\pm\phi+i(\alpha\pm\beta)$ |
| Kernel of $\exp$ | $2\pi i\mathbb{Z}\oplus\pi i(1+j)\mathbb{Z}\cong\mathbb{Z}^2$ |
| Fibre of $\exp$ | $\operatorname{Log}\breve Q+\mathbb{Z}^2$ |
| Principal domain | $\lvert\alpha\rvert+\lvert\beta\rvert\le\pi$ |
| Zero divisors | distinct spectrum, no polar decomposition |
| Scalars | repeated eigenvalue, $\phi=\beta=0$ |

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
| $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ | the reduced biquaternion algebra |
| $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ | a reduced biquaternion |
| $\lambda_\pm=Q_{\blacktriangle}\pm Q_{\blacktriangledown}$ | the eigenvalues |
| $\Pi_\pm=\tfrac12(1\pm j)$ | the fixed central idempotents |
| $Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2=\lambda_+\lambda_-$ | the reduced product |
| $\rho=\sqrt{\lvert Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2\rvert}$ | the radius |
| $\phi$ | the boost |
| $\alpha,\beta$ | the two phases |
| $\Lambda=\langle2\pi(1,0),\pi(1,1)\rangle$ | the lattice of the phases |
| $\lvert\alpha\rvert+\lvert\beta\rvert\le\pi$ | the principal diamond |
| $\breve r=\rho(\cosh\phi+j\sinh\phi)$ | the modulus |
| $u=\exp(i\alpha)\exp(ij\beta)$ | the unit factor |
| $\breve Q_{\log}=\ln\rho+j\phi+i\alpha+ij\beta$ | the exponent |
| $\rho_\pm=\rho e^{\pm\phi}$ | the two scales |
| $\theta_\pm=\alpha\pm\beta$ | the two phase arguments |
| $\operatorname{Arg}$ | the principal argument in $(-\pi,\pi]$ |

## Further Reading

- [Worked Examples of Exponential Polar Decomposition of Reduced Biquaternions](worked-examples-of-exponential-polar-decomposition-of-reduced-biquaternions.html), for the eight cases and the reconstruction tables.
- [Worked Examples of Exponential Polar Decomposition with Eigenbasis of Reduced Biquaternions](worked-examples-of-exponential-polar-decomposition-with-eigenbasis-of-reduced-biquaternions.html), for the same eight cases read in the eigenbasis, with the idempotents and the spinors.
- [Eigenvalue Decomposition and Eigenbasis of a Reduced Biquaternion](eigenvalue-decomposition-and-eigenbasis-of-a-reduced-biquaternion.html), for the spectrum, the characteristic polynomial, the idempotents and the degenerate regimes.
- [Reduced Biquaternion Elementary Functions](reduced-biquaternion-elementary-functions.html), for the exponential, the logarithm, the kernel and the principal domain.
- [Exponential Polar Decomposition of Reduced Biquaternions](exponential-polar-decomposition-of-reduced-biquaternions.html), for the decomposition, existence and uniqueness and the matrix picture.
- [Modulus–Unit Polar Decomposition of Reduced Biquaternions](modulus-unit-polar-decomposition-of-reduced-biquaternions.html), for the modulus, the torus and the uniqueness of the pair.
- [Relations between Exponential Polar Decomposition and Eigenbasis of a Split-Complex Number](relations-between-exponential-polar-decomposition-and-eigenbasis-of-a-split-complex-number.html), for the real two-dimensional analogue.
- *Relations between Exponential Polar Decomposition and Eigenbasis of a Biquaternion*, for the noncommutative analogue.
- [Conventions in Mathematics](conventions-in-mathematics.html), for the notation.
