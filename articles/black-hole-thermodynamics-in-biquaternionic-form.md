# __Black Hole Thermodynamics in Biquaternionic Form__

## Introduction

A black hole is a thermodynamic system. Its horizon carries a temperature and an entropy, its mass satisfies a first law against variations of its area and its charges, and the relation among its mass and those charges is the Euler relation of a homogeneous system. The purpose of this article is to set out that thermodynamics inside the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, in the notation of the companion articles.

**The structural spine is a single claim: the four laws of black hole mechanics are the ordinary laws of thermodynamics applied to the horizon.** None of the four laws is a new physical law. Each is a geometric identity about a Killing horizon — the constancy of the surface gravity, the first law of Bardeen, Carter, and Hawking, the area theorem, the unattainability of the extremal limit — read through a **dictionary** that maps surface gravity to temperature and horizon area to entropy:

$$
\kappa \;\longleftrightarrow\; T = \frac{\kappa}{2\pi},
\qquad
A \;\longleftrightarrow\; S = \frac{A}{4},
$$

in Planck units. What makes the dictionary more than a translation is that it is *consistent*: the geometric quantities defined on the horizon satisfy the thermodynamic relations, with coefficients that are fixed rather than fitted, and the scaling of the black-hole family promotes the first law into a further relation — the Smarr formula — that is not a tautology.

**The temperature is not derived here.** *Hawking Radiation in Biquaternionic Form* established, from the KMS structure and the mode mixing and verified independently against the Euclidean period, that

$$
T = \frac{\hbar\,\kappa}{2\pi c\,k_B},
$$

with $\kappa$ the surface gravity of the horizon. This article takes that result as its input, together with the framework reading that accompanies it — the horizon-generating flow as the modular flow, the modular Hamiltonian $K=-\log\rho$ as a Hermitian element of $\mathbb{M}_+$, and the Euclidean period as a period along the intrinsic imaginary time of $\mathbb{M}_-$ — and asks what else the horizon's thermodynamics contains. The three things it contains are the **entropy**, the **first law**, and the **Smarr relation**.

**Three traps organise the treatment, and one prohibition closes it.**

1. **The entropy is the area, and the area — not a volume — is the surprising fact.** Section "The Entropy Is the Horizon Area" gives the reasons it is the area, and they are not a coincidence: the horizon's intrinsic geometry is two-dimensional; the first law's geometric conjugate to $\kappa$ is $\delta A$; dimensional analysis leaves $A/\ell_P^2$ as the only dimensionless combination; and the Euclidean section localises the entropy at the codimension-two locus where the time circle shrinks. The interior "volume" is not even a state function — it depends on the slicing and grows with the age of the hole.
2. **The first law must be checked term by term.** Its coefficient $\kappa/(8\pi G)$ and the signs of the angular-momentum and charge terms are fixed by the sign conventions of the horizon's angular velocity and potential. Section "The First Law, Term by Term" verifies all three terms for the general Kerr–Newman horizon, symbolically and numerically, and then on each specialisation separately.
3. **The Smarr relation is a scaling statement.** It is the Euler relation for a weighted-homogeneous mass, and Section "The Smarr Relation, by Scaling" derives it by scaling the black-hole family rather than quoting it. Its weights are $(2,2,1)$ for $(S,J,Q)$, and they are exactly the scaling weights of the area, the angular momentum, and the charge under $g_{\mu\nu}\to\lambda^2 g_{\mu\nu}$. Where an extra dimensionful parameter is present — a cosmological constant — the scaling argument acquires a correction, given in Section "Beyond the Asymptotically Flat Case".

**The prohibition is that no microscopic counting is claimed.** The entropy $S=A/4$ is a thermodynamic and geometric statement here. The biquaternion framework supplies no microstate count and no horizon Hilbert space; a claim that the entropy has been *counted* would be a defect, and none is made. The framework's informational sector carries a von Neumann entropy functional on its own states, but that is a different object, and it is not the black-hole entropy.

**What the framework contributes, and what it imports.** The framework houses the effect and its thermodynamics: the material sector $\mathbb{M}_-$ carries the four-vector charges — energy–momentum, angular momentum, current — whose horizon values are $(M,J,Q)$; the informational sector $\mathbb{M}_+$ carries the modular Hamiltonian of the horizon flow; the intrinsic imaginary time of $\mathbb{M}_-$ is the direction whose compactification period is the inverse temperature. The framework does **not** supply the metric, the horizon geometry, the Euclidean action, or the area law: all of these are imported, exactly as in the parent article, and the algebra's role is that of a consistent home rather than a derivation. The gaps are collected in Section "What Is Established, What Is Interpretation, and the Gaps".

## Conventions and Units

The conventions are those of the companion articles, and none is redefined. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$; the quaternion basis is $e_0=1,e_1,e_2,e_3$ with $e_k^2=-e_0$; the scalar imaginary is $i$, $i^2=-1$, commuting with every $e_k$. The material (anti-Hermitian) subspace is $\mathbb{M}_-$ and the informational (Hermitian) subspace is $\mathbb{M}_+$, with $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ and $i\mathbb{M}_\pm=\mathbb{M}_\mp$; $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace and $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ the complex scalars. The material coordinate is $\tilde X=ict\,e_0+x\,e_1+y\,e_2+z\,e_3$ with norm form $N(\tilde X)=\tilde X\bar{\tilde X}$, and the trace formula is $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$, inherited unchanged. The metric signature is $(-,+,+,+)$. The surface gravity is the parent's: the **acceleration-normalized** $\kappa$, with $T=\hbar\kappa/(2\pi c k_B)$; the **frequency normalization** is $\kappa_\omega=\kappa/c$. The horizon is the null surface $f(r_+)=0$, generated by the Killing field $\xi=\partial_t+\Omega\,\partial_\varphi$ that is null on it, normalized to $\xi\cdot\xi=-c^2$ at infinity; for the non-rotating case $\Omega=0$ and $\xi=\partial_t$. This is the parent's $\xi$ and its $\kappa$.

**Units.** The thermodynamic identities of a horizon are cleanest in Planck units

$$
G=c=\hbar=k_B=1,
$$

and that is the working convention below. In these units $S$ is measured in units of $k_B$ and

$$
T=\frac{\kappa}{2\pi},
\qquad
S=\frac{A}{4},
\qquad
dM=\frac{\kappa}{8\pi}\,dA+\Omega\,dJ+\Phi\,dQ,
\qquad
M=2TS+2\Omega J+\Phi Q .
$$

The constants are restored in every physical result, and the restorations are

$$
T=\frac{\hbar\kappa}{2\pi c\,k_B},
\qquad
S=\frac{k_B c^3 A}{4G\hbar}=\frac{k_B A}{4\ell_P^2},
\qquad
\ell_P^2=\frac{\hbar G}{c^3},
$$

$$
d(Mc^2)=\frac{\kappa c^2}{8\pi G}\,dA+\Omega\,dJ+\Phi\,dQ,
\qquad
Mc^2=2TS+2\Omega J+\Phi Q .
$$

Equivalently, if one sets $c=\hbar=k_B=1$ but keeps $G$ explicit, the same relations read

$$
S=\frac{A}{4G},
\qquad
T=\frac{\kappa}{2\pi},
\qquad
dM=\frac{\kappa}{8\pi G}\,dA+\Omega\,dJ+\Phi\,dQ,
\qquad
M=\frac{\kappa A}{4\pi G}+2\Omega J+\Phi Q .
$$

The form with the explicit $1/G$ is the one in which the geometric coefficient is displayed; setting $G=1$ gives the Planck-unit form used below.

The conjugate quantities are fixed by their physical meaning. $\Omega$ is the **angular velocity of the horizon**, $J$ the angular momentum, $\Phi$ the **electric potential** of the horizon relative to infinity, and $Q$ the electric charge. The charge is normalized so that the Reissner–Nordström metric function is $f=1-2M/r+Q^2/r^2$ and the potential is $\Phi=Q/r_+$; the angular momentum is normalized so that the Kerr–Newman function has $a=J/M$ and $\Delta=r^2-2Mr+a^2+Q^2$. With these normalizations the work terms are **positive** when angular momentum or charge of the same sign is added, which fixes the signs in the first law: $\Omega>0$ and $\Phi>0$ for a co-rotating, positively charged hole.

Throughout, $M$ is the mass (the total energy in Planck units), $A$ the area of the horizon cross-section, $\beta=\hbar/(k_BT)$ the inverse temperature, and $r_\pm=M\pm\sqrt{M^2-a^2-Q^2}$ the outer and inner horizon radii of the Kerr–Newman family.

## The Horizon as a Thermodynamic System

The four laws of black hole mechanics were formulated by Bardeen, Carter, and Hawking as geometric statements. It is worth placing them beside their thermodynamic counterparts before any computation, because the comparison is the spine of the article.

| Thermodynamics | Black-hole mechanics (geometric) |
|---|---|
| **Zeroth:** the temperature is uniform in equilibrium | the surface gravity $\kappa$ is constant over the horizon |
| **First:** $dE=T\,dS+\text{work}$ | $dM=\dfrac{\kappa}{8\pi G}\,dA+\Omega\,dJ+\Phi\,dQ$ |
| **Second:** $\delta S\ge 0$ | the horizon area is non-decreasing, $\delta A\ge 0$ |
| **Third:** $T=0$ is unattainable | $\kappa=0$ (the extremal limit) is unattainable |

The **dictionary** that turns the right-hand column into the left is the pair of identifications

$$
T=\frac{\kappa}{2\pi},
\qquad
S=\frac{A}{4G},
$$

the second being the Bekenstein–Hawking entropy (in units $c=\hbar=k_B=1$; the full restoration is in the Conventions). With it, the geometric first law becomes the thermodynamic one, $dM=T\,dS+\Omega\,dJ+\Phi\,dQ$, provided the coefficient in the area term is $1/(8\pi G)$ and the entropy is the area over $4G$. This is the sense in which the four laws "are" thermodynamics: the dictionary is fixed by the temperature, and the first law then determines the entropy's conjugate coefficient.

**Why the horizon is a thermodynamic system at all.** A thermodynamic system is specified by a small number of state variables, with an entropy and a temperature that are functions of them. The **no-hair theorem** — the uniqueness of the Kerr–Newman family among stationary, asymptotically flat electrovacuum black holes (Israel, Carter, Robinson, with later completions) — is what makes the horizon such a system: its state is $(M,J,Q)$ and nothing else. There are no additional "hair" variables on which the area, the surface gravity, or the potentials could depend. The thermodynamic functions $A(M,J,Q)$, $\kappa(M,J,Q)$, $\Omega(M,J,Q)$, and $\Phi(M,J,Q)$ are therefore functions on a three-dimensional state space, and the first law is a one-form identity on that space, checked in Section "The First Law, Term by Term".

**What is established here and what is read into it.** The zeroth law ($\kappa$ constant over a Killing horizon, under the dominant energy condition), the area theorem, the unattainability statement, and the first law are established results of general relativity; the entropy $S=A/4G$ is established by the Euclidean action and by Bekenstein's argument; the temperature is the parent's established result. The **interpretation** is the reading of this structure through the framework — the horizon flow as modular flow, the entropy as a geometric rather than a state-counted quantity. The reading changes no number in the geometric laws, and the section "What Is Established, What Is Interpretation, and the Gaps" separates the two.

**A caveat on the third law.** The third-law entry in the table is the one place the analogy is strained, and it is worth flagging rather than smoothing. The unattainability statement holds in the sense that $\kappa$ cannot be driven to zero by a finite sequence of operations; but a black hole that *is* extremal has $T=\kappa/2\pi=0$ while its horizon area — and hence its entropy — remains finite and nonzero. A thermodynamic system with $T=0$ and $S\ne0$ is a degenerate ground state with a residual entropy, not a system obeying the Nernst postulate $S\to0$. The extremal limit is singular (the near-horizon geometry is not Rindler: for the extremal Reissner–Nordström hole it is $\mathrm{AdS}_2\times S^2$, and for extremal Kerr the near-horizon extremal Kerr geometry, and the surface gravity vanishes), and the third law's exact status is a standard open point of black-hole thermodynamics, not something this article resolves.

## The Temperature, Taken from the Hawking Article

The temperature is the parent's result, and this article uses it without rederiving it. For a horizon with surface gravity $\kappa$,

$$
T_{\mathrm H}=\frac{\hbar\,\kappa}{2\pi c\,k_B}
\qquad\longleftrightarrow\qquad
T=\frac{\kappa}{2\pi}
\ \text{in Planck units},
$$

and for the Schwarzschild horizon, with $\kappa=c^4/(4GM)$ and $r_s=2GM/c^2$,

$$
T_{\mathrm H}=\frac{\hbar c^3}{8\pi G M k_B}.
$$

Two features of the parent's result are used below and are not re-established here. First, $\kappa$ is the **redshifted** surface gravity — finite at the horizon, the limit of $a(r)\sqrt f$ for the static observer, not the divergent proper acceleration $a(r)$ — so the temperature is the same function of the state regardless of the observer. Second, the parent identified the inverse temperature with the Euclidean period, $\beta=2\pi c/\kappa=8\pi GM/c^3$, which is the length of the compact imaginary-time circle. That identification is the operational meaning of the imaginary time of $\mathbb{M}_-$ and is the reason the thermodynamics below can be read as a statement about the horizon's own geometry rather than about a distant observer's detector.

The framework content inherited here is likewise the parent's: the horizon-generating flow is the modular flow, and its modular Hamiltonian $K=-\log\rho$ is a Hermitian element of the informational sector $\mathbb{M}_+$. The horizon's temperature is fixed by the period of that flow. The entropy developed in the next section is, by contrast, **not** a functional of an $\mathbb{M}_+$ state; the framework supplies no such state for a horizon, and the distinction is kept explicit.

## The Entropy Is the Horizon Area

The entropy of a black hole is the **Bekenstein–Hawking entropy**

$$
S=\frac{k_B c^3 A}{4G\hbar}=\frac{k_B A}{4\ell_P^2},
\qquad
\ell_P^2=\frac{\hbar G}{c^3},
$$

and in Planck units simply $S=A/4$, with $A$ the area of the horizon cross-section. For Schwarzschild, $A=16\pi G^2M^2/c^4$ and $S=4\pi k_BGM^2/(\hbar c)$; for Kerr–Newman,

$$
A=4\pi\left(r_+^2+a^2\right),
\qquad
a=\frac{J}{M},
\qquad
r_\pm=M\pm\sqrt{M^2-a^2-Q^2}.
$$

Two facts in this formula are load-bearing, and neither is a coincidence: the entropy is the **area** rather than a volume, and its coefficient is **$1/4$**.

### Why the Area, and Not a Volume

The interior of a black hole has a perfectly good coordinate volume on any given spatial slice, and a naive dimensional argument might suggest that the entropy, being extensive, should scale with it. The following reasons show why the state function is the area and why a volume could not play the role.

**1. A state function must be determined by the state.** The no-hair theorem fixes the state to $(M,J,Q)$, and the horizon area $A(M,J,Q)=4\pi(r_+^2+a^2)$ is a function of exactly those parameters. The interior has no such status. Inside the horizon the radial coordinate is time-like, so a "slice" is not a moment of time in the ordinary sense; different slicings of the same hole give different interior volumes, and on the maximal slices usually chosen the volume grows with the age of the hole. It is therefore not a function of $(M,J,Q)$ at all, and cannot be a thermodynamic state function. The area is also the intrinsically defined quantity: it is the area of the horizon cross-section, independent of any slicing.

**2. The first law's geometric conjugate to $\kappa$ is $\delta A$.** The intensive quantity the horizon carries is the surface gravity $\kappa$, and the first law pairs it with the variation of the area, $(\kappa/8\pi G)\,\delta A$. There is no $\kappa\,\delta V$ term. The first law therefore singles out the area as the geometric variable conjugate to the horizon's temperature, and the entropy is the accumulation of that conjugate: $dS=(\delta A)/(4G)$ follows from $T\,dS=(\kappa/8\pi G)\,dA$ together with $T=\kappa/2\pi$.

**3. Dimensions leave no other choice.** With $\hbar,c,G,k_B$ available, the only dimensionless combination linear in the horizon's own geometry is $c^3A/(G\hbar)=A/\ell_P^2$. A dimensionless entropy assembled from the horizon data must therefore be $S/k_B=c\,A/\ell_P^2$ for a pure number $c$, and the number is fixed to $1/4$ by reason 2. There is no corresponding dimensionless "volume per Planck volume" that is a state function, by reason 1.

**4. The Euclidean section localises the entropy at the horizon.** The Euclidean Schwarzschild (or Kerr–Newman) section is a "cigar"; the Euclidean time circle shrinks to a point at the horizon, a **codimension-two** locus. The on-shell gravitational action's horizon contribution is a boundary term at that locus and is proportional to its area; differentiating the resulting free energy with respect to the temperature gives $S=A/4G$ (Gibbons and Hawking). This is the same Euclidean computation the Hawking article used to fix the period $\beta=2\pi c/\kappa$, read as an action rather than as a period. The localisation is what makes the result an area and not a volume: the entropy is the contribution of the shrinking circle, and that circle shrinks on a two-surface, not on a three-volume.

**5. The area is the monotone quantity.** Bekenstein's original argument reaches the same conclusion from the second law. The classical area theorem makes $A$ non-decreasing, and the generalized second law requires $S_{BH}+S_{\text{matter}}$ to be non-decreasing; the geometric entropy consistent with both must be a function of the area, and the function is fixed by dimensional analysis and the first law to $A/(4\ell_P^2)$.

The area law is thus **forced** by the thermodynamics, not fitted to it. A volume law would fail at the first step: no volume determined by $(M,J,Q)$ exists, and the scaling argument of the Smarr section would be inconsistent with a quantity of scaling weight three. The area, of weight two, is the quantity the Euler relation requires.

### The Coefficient $1/4$ Is Fixed

The coefficient is not free. With $T=\kappa/(2\pi)$ from the parent and $S=A/4$, the entropy term of the first law is

$$
T\,dS=\frac{\kappa}{2\pi}\cdot\frac{dA}{4}=\frac{\kappa}{8\pi}\,dA,
$$

which is exactly the geometric work term of Bardeen–Carter–Hawking. Conversely, given the parent's temperature and the first law, $dS=dM/T$ determines the entropy up to an additive constant, and the constant is fixed by the Euclidean normalisation (equivalently, by requiring a zero-area horizon to carry no entropy). The two dictionary entries $T=\kappa/2\pi$ and $S=A/4$ are therefore one consistency condition, not two independent postulates.

### The Entropy Here Is Not a State Count

The formula $S=A/4$ is **thermodynamic and geometric**. It is obtained from the first law and the Euclidean action; it is not obtained by counting microstates, and the biquaternion framework supplies no microstate count. A stationary black hole in this series has a three-parameter state $(M,J,Q)$ and a geometric entropy; it has no horizon Hilbert space whose dimension would be $e^{A/4G}$. Where a microscopic counting exists — in string theory and in loop quantum gravity — it is imported from those frameworks and is not part of this one; the agreement of a state count with $A/4G$ in those settings is evidence for the area law, not a derivation of it here.

It is important not to conflate this entropy with the framework's own entropy functional. The informational sector $\mathbb{M}_+$ carries the von Neumann functional $S(\tilde\rho)=-2\,\mathrm{Sc}(\tilde\rho\log\tilde\rho)$ on its states (the biquaternion form of $-\mathrm{Tr}(\rho\log\rho)$), and that functional is a transcription of the standard quantum-mechanical entropy of a qubit; the series records it as posited and not yet verified. It applies to a density matrix in $\mathbb{M}_+$, and it is a different object from the black-hole entropy. The black-hole entropy is a property of the horizon's geometry; reading $S=A/4$ as the von Neumann entropy of some $\mathbb{M}_+$ state would require a horizon state that the framework does not provide. Whether such a state exists is the central open question of this article, and it is left as a question.

## The First Law, Term by Term

The first law of black hole mechanics is

$$
dM=\frac{\kappa}{8\pi G}\,dA+\Omega\,dJ+\Phi\,dQ
\qquad\longleftrightarrow\qquad
dM=T\,dS+\Omega\,dJ+\Phi\,dQ,
$$

in units $c=\hbar=k_B=1$, with the dictionary of the Conventions. In the explicit checks below we set $G=1$ as well — equivalently, $G$ is absorbed into the normalization of the mass and the area — so that the coefficient in the area term is $\kappa/8\pi$. Everything on the right is a function of the state $(M,J,Q)$, and the statement is an identity among one-forms on that three-dimensional space. The coefficients are not free: the $\kappa/(8\pi G)$ multiplies $\delta A$, and $\Omega$ and $\Phi$ are the horizon's angular velocity and electric potential. This section checks all three terms on the general Kerr–Newman horizon.

### The Kerr–Newman Horizon

In units $G=c=1$ the Kerr–Newman solution has

$$
\Delta=r^2-2Mr+a^2+Q^2,
\qquad
a=\frac{J}{M},
\qquad
r_\pm=M\pm\sqrt{M^2-a^2-Q^2},
$$

and the horizon quantities are

$$
A=4\pi\left(r_+^2+a^2\right),
\qquad
\kappa=\frac{r_+-r_-}{2\left(r_+^2+a^2\right)},
\qquad
\Omega=\frac{a}{r_+^2+a^2},
\qquad
\Phi=\frac{Q\,r_+}{r_+^2+a^2}.
$$

The first law is equivalent to the three derivative identities

$$
\frac{\partial A}{\partial M}=\frac{8\pi}{\kappa},
\qquad
\frac{\partial A}{\partial J}=-\frac{8\pi\,\Omega}{\kappa},
\qquad
\frac{\partial A}{\partial Q}=-\frac{8\pi\,\Phi}{\kappa},
$$

obtained by comparing the coefficient of $dM$, $dJ$, and $dQ$ on the two sides. All three were verified symbolically on the general Kerr–Newman family (with $M,J,Q$ as independent parameters and $a=J/M$), and each vanishes identically. The signs are the content of the second and third: the area *decreases* when angular momentum or charge is added at fixed mass, which is why the work terms in $dM$ are positive and why the identities carry minus signs.

### The Specialisations

Each known case was checked separately, so that the general identity is not certified only by the case that suggested it.

- **Schwarzschild** ($J=Q=0$): $a=0$, $r_+=2M$, $A=16\pi M^2$, $\kappa=1/(4M)$, $T=1/(8\pi M)$, $S=4\pi M^2$. The first law reduces to $dM=T\,dS$: indeed $T\,dS=(1/8\pi M)\cdot 8\pi M\,dM=dM$.
- **Reissner–Nordström** ($J=0$): $r_\pm=M\pm\sqrt{M^2-Q^2}$, $A=4\pi r_+^2$, $\kappa=(r_+-r_-)/(2r_+^2)$, $\Phi=Q/r_+$. The first law is $dM=(\kappa/8\pi)\,dA+\Phi\,dQ$, and both derivative identities hold; the Smarr limit $M=2TS+\Phi Q$ is verified below.
- **Kerr** ($Q=0$): $r_+=M+\sqrt{M^2-a^2}$, $A=8\pi Mr_+$, $\Omega=a/(2Mr_+)$, and the first law is $dM=(\kappa/8\pi)\,dA+\Omega\,dJ$; the identity $\partial A/\partial J=-8\pi\Omega/\kappa$ holds.

### A Numerical Spot Check

As an independent check at a point that is neither Schwarzschild nor extremal, take $M=1$, $J=0.5$, $Q=0.3$ (so that $M^2-a^2-Q^2=0.66>0$ and the horizon exists). The horizon quantities are

$$
A=44.4197\ldots,\quad
\kappa=0.229830\ldots,\quad
\Omega=0.141450\ldots,\quad
\Phi=0.153819\ldots,
$$

$$
T=\frac{\kappa}{2\pi}=0.0365785\ldots,\qquad
S=\frac{A}{4}=11.1049\ldots .
$$

The first law holds at this point: the three central-difference combinations $(\kappa/8\pi)\,\partial A/\partial M-1$, $(\kappa/8\pi)\,\partial A/\partial J+\Omega$, and $(\kappa/8\pi)\,\partial A/\partial Q+\Phi$ vanish to better than $10^{-12}$ in a $30$-digit computation, and the same computation verifies the Smarr residual below to machine precision. The check uses the general charged and rotating case, not the Schwarzschild case from which the area law is easiest to guess.

**Sign convention, stated once.** The angular-velocity and potential terms are positive because $\Omega$ and $\Phi$ are the horizon values in the gauge where they vanish at infinity and because adding angular momentum or charge of the same sign increases the mass. A reader using the opposite sign for $\Phi$ (potential of infinity relative to the horizon) or the opposite convention for the direction of rotation must flip the corresponding term; the geometric identities above fix the convention, since $\kappa$, $A$, and $r_\pm$ are sign-definite.

## The Smarr Relation, by Scaling

The Smarr relation is often quoted as

$$
M=2TS+2\Omega J+\Phi Q=\frac{\kappa A}{4\pi G}+2\Omega J+\Phi Q,
$$

but it is not an independent law: it is the **Euler relation** for a weighted-homogeneous mass, and the weights are fixed by how the black-hole family scales. Deriving it that way shows both why it holds and where it fails.

### The Scaling of the Family

Consider the Kerr–Newman family in units $G=c=1$. A global scaling of the metric, $g_{\mu\nu}\to\lambda^2 g_{\mu\nu}$, maps a solution with parameters $(M,J,Q)$ to a solution with

$$
(M,J,Q)\;\longrightarrow\;(\lambda M,\ \lambda^2 J,\ \lambda Q).
$$

The weights follow from where the charges sit in the asymptotic fields: $M$ is the coefficient of $1/r$ in $g_{tt}$ (weight one), $J$ the coefficient of $1/r^2$ in the frame-dragging function (weight two, an angular momentum), and $Q$ the coefficient of $1/r$ in the Coulomb field (weight one, a charge). Under the same scaling the horizon data transform as

$$
r_+\to\lambda r_+,
\qquad
A\to\lambda^2 A,
\qquad
S\to\lambda^2 S,
\qquad
\kappa\to\frac{\kappa}{\lambda},
\qquad
T\to\frac{T}{\lambda},
\qquad
\Omega\to\frac{\Omega}{\lambda},
\qquad
\Phi\to\Phi,
$$

each verified symbolically: the radius and the area are lengths and areas, the surface gravity is an inverse length, the angular velocity is an inverse length, and the dimensionless potential is invariant.

### The Euler Relation

Because the family has this one-parameter scaling and no other dimensionful parameter, the mass can be written as a function $M(S,J,Q)$ of the entropy and the charges, and the scaling statement above is exactly the statement that $M$ is **weighted-homogeneous**:

$$
M\!\left(\lambda^2 S,\ \lambda^2 J,\ \lambda Q\right)=\lambda\,M(S,J,Q).
$$

Differentiating with respect to $\lambda$ at $\lambda=1$ gives the Euler relation for these weights,

$$
2S\,\frac{\partial M}{\partial S}+2J\,\frac{\partial M}{\partial J}+Q\,\frac{\partial M}{\partial Q}=M.
$$

The first law supplies the partial derivatives: $T=\partial M/\partial S$, $\Omega=\partial M/\partial J$, and $\Phi=\partial M/\partial Q$ are precisely its intensive coefficients. Substituting,

$$
M=2TS+2\Omega J+\Phi Q=\frac{\kappa A}{4\pi G}+2\Omega J+\Phi Q,
$$

where the second form uses $T=\kappa/2\pi$ and $S=A/(4G)$, so that $2TS=\kappa A/(4\pi G)$. This is the Smarr relation, and it was obtained by scaling.

### Verification

The relation was verified symbolically on the general Kerr–Newman family in the form $M-2TS-2\Omega J-\Phi Q=0$ (with the horizon quantities as defined above), and separately on each specialisation:

- **Schwarzschild:** $J=Q=0$ gives $M=2TS$. With $T=1/(8\pi M)$ and $S=4\pi M^2$, $2TS=M$.
- **Reissner–Nordström:** $M=2TS+\Phi Q$; symbolically $2TS+\Phi Q-M$ reduces to zero.
- **Kerr:** $M=2TS+2\Omega J$, symbolically zero.
- **Kerr–Newman:** the full four-term identity, symbolically zero and numerically zero at $M=1$, $J=0.5$, $Q=0.3$.

### The Parent's Temperature Closes the Thermodynamics

The Smarr relation is where the parent's temperature is used a second time, and where the area law is recovered rather than assumed. Take Schwarzschild. The parent gives $T=1/(8\pi M)$; the Smarr relation $M=2TS$ then gives

$$
S=\frac{M}{2T}=4\pi M^2=\frac{A}{4},
$$

the area law, independent of the Euclidean computation. Equivalently, integrating the first law $dS=dM/T$ gives $S=4\pi M^2+\text{const}$, and the Smarr relation fixes the constant to zero. For Kerr–Newman the same logic requires the derivative identities of the previous section together with the scaling weights; the result is again $S=A/4$. Thus the parent's temperature, the first law, and the scaling homogeneity of the family are jointly sufficient for the entropy and the Smarr relation, and the three are mutually consistent. The agreement is a check, not a derivation from a microstate count.

## Beyond the Asymptotically Flat Case

The scaling derivation of the previous section is not a general theorem about any horizon. It used two facts: that the family's parameters are exactly $(M,J,Q)$, and that a scaling of the metric maps the family to itself. A **cosmological constant breaks the second fact**. Under $g_{\mu\nu}\to\lambda^2 g_{\mu\nu}$ the Ricci tensor is unchanged while $\Lambda g_{\mu\nu}$ scales, so the scaled metric is a solution of a different theory unless $\Lambda=0$. Equivalently, $\Lambda$ has dimensions of inverse length squared and does not scale with the metric; it is a new dimensionful parameter, and the mass is no longer a function of $(S,J,Q)$ alone at fixed $\Lambda$.

The scaling argument can be repaired by promoting the cosmological constant to a thermodynamic variable. Writing the pressure

$$
P=-\frac{\Lambda}{8\pi G},
$$

and letting $V$ be its conjugate, the **extended first law** is

$$
dM=T\,dS+\Omega\,dJ+\Phi\,dQ+V\,dP,
\qquad
V=\left(\frac{\partial M}{\partial P}\right)_{S,J,Q},
$$

and the mass is weighted-homogeneous in $(S,J,Q,P)$ with weights $(2,2,1,-2)$ — the last being the weight of $P$ under the scaling. Euler's relation then gives the **corrected Smarr formula**

$$
M=2TS+2\Omega J+\Phi Q-2PV .
$$

The correction is therefore a term $-2PV$, absent in the asymptotically flat case, and it is not a small rescaling of the flat relation but a genuinely new term proportional to the volume conjugate to $\Lambda$.

**The Schwarzschild–AdS check.** In units $G=c=1$, with the metric function $f=1-2M/r-\Lambda r^2/3$ and $\Lambda<0$ for anti-de Sitter, the horizon condition $f(r_+)=0$ gives

$$
M=\frac{r_+}{2}-\frac{\Lambda r_+^3}{6},
\qquad
T=\frac{1}{4\pi}\left(\frac{1}{r_+}-\Lambda r_+\right),
\qquad
S=\pi r_+^2,
\qquad
V=\frac{4\pi r_+^3}{3},
\qquad
P=-\frac{\Lambda}{8\pi}.
$$

Substituting these, $M-2TS+2PV$ reduces identically to zero; and independently, $V=(\partial M/\partial P)_S=4\pi r_+^3/3$, so the volume in the extended first law is the same quantity. Both were verified symbolically. The flat relation is the $\Lambda\to0$ limit, where the correction vanishes.

**A caveat.** The **thermodynamic volume** $V$ and the exact form of the corrected relation are subtle beyond the static case: for general rotating and charged AdS black holes the volume is not simply the geometric volume of the horizon, and its definition and properties are a matter of continuing work. The relation displayed above is the standard extended-thermodynamics form, verified here for Schwarzschild–AdS; a claim of the corrected Smarr relation for a general AdS black hole would need its own check. The point for this article is the structural one: **the flat Smarr relation is exact, and if it is claimed beyond the asymptotically flat case it acquires the $-2PV$ correction, because the scaling homogeneisation that produced it is broken by the dimensionful $\Lambda$.**

## What Is Established, What Is Interpretation, and the Gaps

**Established (physics).**

- The four laws of black hole mechanics: the constancy of $\kappa$ over a Killing horizon, the first law $dM=(\kappa/8\pi G)\,dA+\Omega\,dJ+\Phi\,dQ$, the area theorem $\delta A\ge0$ under the dominant energy condition, and the unattainability of $\kappa=0$.
- The no-hair theorem: a stationary, asymptotically flat electrovacuum black hole is a member of the Kerr–Newman family and its state is $(M,J,Q)$.
- The Hawking temperature $T=\hbar\kappa/(2\pi c k_B)$ (the parent's result), including the Euclidean period $\beta=2\pi c/\kappa$.
- The Bekenstein–Hawking entropy $S=k_B c^3A/(4G\hbar)=k_B A/(4\ell_P^2)$, from the Euclidean action and Bekenstein's argument.
- The first law, verified term by term for Kerr–Newman and each specialisation.
- The Smarr relation $M=2TS+2\Omega J+\Phi Q$, derived by scaling and verified; and its extension $M=2TS+2\Omega J+\Phi Q-2PV$ with a cosmological constant, verified for Schwarzschild–AdS.

**Established (algebra).**

- The sectors $\mathbb{M}_-$ and $\mathbb{M}_+$, the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the complex scalars $\mathbb{C}_{\mathbb{B}}$, the norm form $N(\tilde X)=\tilde X\bar{\tilde X}$, and the trace formula $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$.
- The intrinsic imaginary time $ict$ of $\mathbb{M}_-$, whose compactification period is the inverse temperature, and the KMS condition of the parent.
- The modular Hamiltonian $K=-\log\rho$ of the horizon flow as a Hermitian element of $\mathbb{M}_+$.
- The charges $(M,J,Q)$ as material-sector Noether quantities: energy–momentum is an $\mathbb{M}_-$ four-vector, angular momentum the associated bivector, and charge the time component of the conserved current.

**Interpretation.**

- That the horizon-generating Killing flow is the modular flow (the Bisognano–Wichmann/Hartle–Hawking identification, imported), so that the thermodynamic temperature is the modular temperature. The parent already reads the KMS imaginary time as the intrinsic imaginary time of $\mathbb{M}_-$.
- That the entropy is a **geometric** property of the horizon rather than the von Neumann entropy of an $\mathbb{M}_+$ state. This is a reading consistent with the algebra; it is not a derivation, and it is the reading that keeps the framework honest about the missing microstate count.

**Gaps, left visible.**

- *No microstate count.* The framework has no horizon Hilbert space and no counting of states; the area law is imported and its microscopic interpretation belongs to other frameworks. No statistical derivation is claimed.
- *The framework's own entropy functional is a different, unverified object.* $S(\tilde\rho)=-2\,\mathrm{Sc}(\tilde\rho\log\tilde\rho)$ on $\mathbb{M}_+$ is the qubit von Neumann entropy, not the black-hole entropy; it is recorded elsewhere in the series as posited and not yet verified, and it is not used here.
- *No metric and no dynamics.* The framework contains no black-hole geometry; the metric is an imported frame field, and the local-scale route to gravity is too rigid to contain black-hole exteriors. Nothing in the algebra determines the horizon or the scaling family.
- *No backreaction.* Evaporation, the lifetime, the generalized second law with the emitted radiation, and the information question are not computed. With no microstates, the framework cannot address the Page curve, and no attempt is made.
- *The third law is strained.* Extremal holes have $T=0$ and $S\ne0$; the near-horizon geometry is not Rindler. The analogy with the Nernst postulate is incomplete and is left so.
- *No empirical contact.* Every statement here agrees with the standard theory; the framework supplies no correction to any of the thermodynamic quantities. Hawking radiation has not been observed for gravitational black holes, and no horizon entropy has been measured directly.

## Open Questions

1. **Is there a horizon state in $\mathbb{M}_+$ whose von Neumann entropy is $A/4G$?** This is the central framework question. The entropy functional $S(\tilde\rho)=-2\,\mathrm{Sc}(\tilde\rho\log\tilde\rho)$ exists on $\mathbb{M}_+$ but acts on a finite-dimensional state; a horizon would need a state (or a limit of states) whose entropy equals the area law. If such a state exists, the area law becomes a statement about the algebra; if not, the entropy remains geometric and the framework remains descriptive.

2. **Is the area intrinsically geometric, or can the algebra see it?** The norm form is pointwise and cannot produce an area; the horizon area is a global object of the imported manifold. Is there any algebraic quantity — a limit of the modular operator, a trace over a growing algebra, a boundary term — that reduces to the area in the appropriate limit?

3. **Does the algebra carry the scaling?** The Smarr derivation rests on the weighted homogeneity $M(\lambda^2S,\lambda^2J,\lambda Q)=\lambda M$. Is the scaling of the family visible as a scaling of the frame field $\tilde E_\mu$ or of the connection, and is there an algebraic statement of the Euler relation?

4. **The cosmological-constant correction.** Is the thermodynamic volume $V$ algebraically meaningful, and does the framework have anything to say about the AdS case, where the boundary description is itself informational? The $-2PV$ term is currently imported.

5. **Extremal horizons.** The near-horizon geometry of an extremal hole is not Rindler ($\mathrm{AdS}_2\times S^2$ for the extremal Reissner–Nordström hole, the near-horizon extremal Kerr geometry for the extremal Kerr hole), and the modular flow is not the boost. Does the framework distinguish extremal from non-extremal horizons, and does it say anything about the third law?

6. **Backreaction and the information question.** Without microstates the framework cannot follow the emitted radiation's entanglement or the Page curve. Can the framework be extended so as to have a state-counting mechanism at all, or is the geometric entropy its final word on the subject?

7. **Empirical contact.** The thermodynamics here is standard and supplies no discriminating prediction. Is there any regime — strong curvature, the extremal limit, a modified dispersion or a second light cone from the series' signature list — in which the horizon's thermodynamics would differ from the standard account, or is the framework's contribution structural only?

## Summary

The four laws of black hole mechanics are the ordinary laws of thermodynamics applied to the horizon, through the dictionary $T=\kappa/2\pi$, $S=A/(4G)$ in units $c=\hbar=k_B=1$ (with $G$ kept explicit). The temperature is the parent's result $T=\hbar\kappa/(2\pi c k_B)$, taken as input: $\kappa$ is the redshifted surface gravity, constant over the horizon, and the inverse temperature is the Euclidean period $2\pi c/\kappa$. The no-hair theorem gives the horizon a three-parameter state $(M,J,Q)$, which is what makes the thermodynamic description possible.

The entropy is the **Bekenstein–Hawking entropy** $S=k_B c^3A/(4G\hbar)=k_B A/(4\ell_P^2)$. It is the **area**, not a volume, and this is forced rather than coincidental: the area is a state function of $(M,J,Q)$ while the interior volume is slicing-dependent; the first law's geometric conjugate to $\kappa$ is $\delta A$; dimensional analysis leaves $A/\ell_P^2$ as the only dimensionless combination; the Euclidean section localises the entropy at the codimension-two locus where the time circle shrinks; and the area is the monotone quantity of Bekenstein's second-law argument. The coefficient $1/4$ is fixed by $T\,dS=(\kappa/2\pi)(dA/4G)=\kappa\,dA/(8\pi G)$. The entropy is thermodynamic and geometric; it is not a count of microstates, and no such count is claimed.

The **first law** $dM=(\kappa/8\pi G)\,dA+\Omega\,dJ+\Phi\,dQ=T\,dS+\Omega\,dJ+\Phi\,dQ$ was checked term by term for the general Kerr–Newman horizon, with the area's derivatives in mass, angular momentum, and charge matching the conjugate quantities in magnitude and sign, and separately on the Schwarzschild, Reissner–Nordström, and Kerr specialisations and at a numerical point with both rotation and charge.

The **Smarr relation** $M=2TS+2\Omega J+\Phi Q=\kappa A/(4\pi G)+2\Omega J+\Phi Q$ was derived by scaling: the Kerr–Newman family satisfies $(M,J,Q)\to(\lambda M,\lambda^2J,\lambda Q)$ under $g_{\mu\nu}\to\lambda^2g_{\mu\nu}$, so $M$ is weighted-homogeneous of weights $(2,2,1)$ and Euler's theorem gives the relation with the first law's conjugates. With the parent's temperature it fixes the entropy to $S=A/4$ for Schwarzschild, so the temperature, the first law, and the scaling homogeneity close the thermodynamics. A cosmological constant breaks the scaling and the relation acquires the correction $-2PV$, verified for Schwarzschild–AdS.

The biquaternion framework houses the thermodynamics — the material sector $\mathbb{M}_-$ for the charges and the intrinsic imaginary time, the informational sector $\mathbb{M}_+$ for the modular Hamiltonian of the horizon flow — and it imports the geometry, the Euclidean action, and the area law. It contains no microstate count, no horizon state whose entropy is the area, and no correction to the standard numbers. The gaps are stated rather than filled.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\mathbb{M}_-$ | Material sector: imaginary time, real space; home of the four-vectors |
| $\mathbb{M}_+$ | Informational sector: real time, imaginary space; home of $K=-\log\rho$ |
| $\mathbb{H}_{\mathbb{B}}$, $\mathbb{C}_{\mathbb{B}}$ | Real-quaternion subspace; complex scalars |
| $e_0,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\tilde X=ict\,e_0+x\,e_1+y\,e_2+z\,e_3$ | Material coordinate |
| $N(\tilde X)=\tilde X\bar{\tilde X}$ | Norm form |
| $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$ | Trace formula |
| $M$ | Mass (total energy in Planck units) |
| $J$, $Q$ | Angular momentum, electric charge |
| $a=J/M$ | Kerr rotation parameter |
| $r_\pm=M\pm\sqrt{M^2-a^2-Q^2}$ | Outer and inner Kerr–Newman horizons |
| $A=4\pi(r_+^2+a^2)$ | Horizon area |
| $\kappa=(r_+-r_-)/(2(r_+^2+a^2))$ | Surface gravity (acceleration normalization) |
| $\Omega=a/(r_+^2+a^2)$ | Horizon angular velocity |
| $\Phi=Qr_+/(r_+^2+a^2)$ | Horizon electric potential |
| $T=\hbar\kappa/(2\pi c k_B)$ | Hawking temperature (from the parent) |
| $S=k_B c^3A/(4G\hbar)=k_B A/(4\ell_P^2)$ | Bekenstein–Hawking entropy |
| $\ell_P^2=\hbar G/c^3$ | Planck area |
| $\beta=\hbar/(k_BT)=2\pi c/\kappa$ | Inverse temperature, Euclidean period |
| $dM=(\kappa/8\pi G)\,dA+\Omega\,dJ+\Phi\,dQ$ | First law (units $c=\hbar=k_B=1$) |
| $M=2TS+2\Omega J+\Phi Q$ | Smarr relation |
| $\Lambda$, $P=-\Lambda/(8\pi G)$, $V$ | Cosmological constant, pressure, thermodynamic volume |
| $M=2TS+2\Omega J+\Phi Q-2PV$ | Smarr relation with a cosmological constant |
| $K=-\log\rho$ | Modular Hamiltonian (Hermitian, in $\mathbb{M}_+$) |

## Further Reading

**Companion articles (this series).**

- *Hawking Radiation in Biquaternionic Form*, the parent: the surface gravity, the Hawking temperature, the Euclidean period, and the KMS identification of the horizon flow.
- *The KMS Condition and the Biquaternion Framework*, for the imaginary-time strip, the intrinsic imaginary time of $\mathbb{M}_-$, and the modular Hamiltonian in $\mathbb{M}_+$.
- *The Modular Hamiltonian in Biquaternionic Form*, for the modular generator, its spectral form, and the Gibbs structure.
- *The Bisognano–Wichmann Theorem under the Biquaternion Framework*, for the wedge/horizon identification of the modular flow with the boost.
- *The Unruh Effect in Biquaternionic Form*, the sibling: the Rindler horizon and the surface gravity as a boost parameter.
- *Curved Spacetime and the Biquaternion Framework*, for the frame-field route to the metric and why the framework generates no black-hole geometry of its own.
- *The Einstein Field Equations under the Biquaternion Framework — A Research Agenda*, for the status of the dynamics and of an action for the frame.
- *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* and *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, for the sectors, the four-vectors, and the operator algebra.
- *Noether's Theorem in Biquaternionic Form*, for the conserved four-momentum, angular momentum, and current that become the horizon charges.
- *Introduction to the Biquaternion Universe*, for the algebra and the notation.
- *Quantum Thermodynamics in Biquaternionic Form*, for the standard thermodynamic functionals on $\mathbb{M}_+$ and the Gibbs state of a qubit.
- *The Partition Function in Biquaternionic Form*, for the thermal trace and its imaginary-time formulation.

**Standard references.**

- J. D. Bekenstein, "Black holes and entropy," *Physical Review D* **7** (1973) 2333–2341, and "Generalized second law of thermodynamics in black-hole physics," *Physical Review D* **9** (1974) 3292–3300, for the entropy-area proposal and the generalized second law.
- J. M. Bardeen, B. Carter, and S. W. Hawking, "The four laws of black hole mechanics," *Communications in Mathematical Physics* **31** (1973) 161–170, for the four laws and the surface gravity.
- S. W. Hawking, "Gravitational radiation from colliding black holes," *Physical Review Letters* **26** (1971) 1344–1346, for the area theorem, and "Particle creation by black holes," *Communications in Mathematical Physics* **43** (1975) 199–220, for the temperature and the breakdown of the area theorem by evaporation.
- L. Smarr, "Mass formula for Kerr black holes," *Physical Review Letters* **30** (1973) 71–73, and erratum **30** (1973) 521, for the mass formula.
- G. W. Gibbons and S. W. Hawking, "Action integrals and partition functions in quantum gravity," *Physical Review D* **15** (1977) 2752–2756, for the Euclidean action and the entropy $A/4G$.
- B. Carter, "Axisymmetric black hole has only two degrees of freedom," *Physical Review Letters* **26** (1971) 331–333; W. Israel, "Event horizons in static vacuum space-times," *Physical Review* **164** (1967) 1776–1779; D. C. Robinson, "Uniqueness of the Kerr black hole," *Physical Review Letters* **34** (1975) 905–906, for the no-hair theorem.
- M. Christodoulou and C. Rovelli, "How big is a black hole?," *Physical Review D* **91** (2015) 064046, and S. A. Hayward, "The volume of a black hole," (2015), for the slicing dependence of the interior volume.
- D. Kastor, S. Ray, and J. Traschen, "Enthalpy and the mechanics of AdS black holes," *Classical and Quantum Gravity* **26** (2009) 195011, and B. P. Dolan, "The cosmological constant and the black hole equation of state," *Classical and Quantum Gravity* **28** (2011) 125020, for the extended first law and the $\Lambda$-corrected Smarr relation.
- R. M. Wald, *Quantum Field Theory in Curved Spacetime and Black Hole Thermodynamics* (University of Chicago Press, 1994), for the standard treatment of the four laws, the Euclidean section, and the entropy.
- A. Strominger and C. Vafa, "Microscopic origin of the Bekenstein–Hawking entropy," *Physics Letters B* **379** (1996) 99–104, for an example of a microscopic state count in an external framework; it is cited as external and is not used in the derivations of this article.
