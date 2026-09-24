# __POVMs and the Positive Cone in Biquaternionic Form__

## Introduction

The most general measurement that quantum mechanics admits is not a projective measurement. It is a **positive operator-valued measure**: a family of positive elements summing to the identity, each paired with the state by the Born rule. In the biquaternion framework these elements are elements of the Hermitian subspace $\mathbb{M}_+$, and the condition that a measurement be possible is the condition that they lie in the **positive cone** of the algebra. This article develops the cone, the effects it contains, and the general measurement, in the framework's own terms.

The central observation is that the positive cone of $\mathbb{M}_+$ is the positive cone of the norm form. For a Hermitian element $\tilde{E} = a_0e_0 + i\mathbf{a}$ with $a_0\in\mathbb{R}$, $\mathbf{a}\in\mathbb{R}^3$, positivity of the operator is

$$
\tilde{E}\geq0 \quad\Longleftrightarrow\quad N(\tilde{E}) = a_0^2 - |\mathbf{a}|^2 \geq 0 \ \text{ and }\ a_0\geq0
\quad\Longleftrightarrow\quad a_0\geq|\mathbf{a}| ,
$$

so the cone of the algebra is the future light cone of the norm form. An **effect** is an element of the operator interval $0\leq\tilde{E}\leq e_0$, which in coefficients reads $|\mathbf{a}|\leq\min(a_0,1-a_0)$; a **POVM** is a resolution of the identity by effects, $\sum_y\tilde{E}_y = e_0$; and the Born rule for the measurement is the trace pairing $p_y = \mathrm{Tr}(\tilde{\rho}\tilde{E}_y)$. The projective measurements are the special case in which the effects are idempotents, and they are the extreme elements of the set of effects; the general measurement is a convex decomposition of the identity into non-extreme effects, and it is strictly more powerful.

The cone is self-dual with respect to the trace pairing, which is the algebraic reason the pairing serves both as the Born rule and as the duality that makes the measurement formalism work. The article derives this, characterizes the effects, exhibits the general POVM, and works two examples: the **trine** POVM, which distinguishes three equatorial states better than any projective measurement, and unambiguous discrimination, which two non-orthogonal states admit with a POVM and not with a projective measurement. The general measurement's realization as a projective measurement on a larger system — Naimark's dilation — is stated in the framework's language, and its status as an extension of the algebra is noted.

## The Positive Cone

### Positivity as the norm form

Let $\tilde{H} = h_0e_0 + i\mathbf{h}$ be a general Hermitian element, with $h_0\in\mathbb{R}$ and $\mathbf{h}\in\mathbb{R}^3$. Its matrix image is $h_0I_2 + \mathbf{h}\cdot\boldsymbol{\sigma}$, whose eigenvalues are $h_0\pm|\mathbf{h}|$. Hence

$$
\tilde{H}\geq0 \quad\Longleftrightarrow\quad h_0 \geq |\mathbf{h}| ,
$$

and the norm form is

$$
N(\tilde{H}) = \tilde{H}\bar{\tilde{H}} = h_0^2 - |\mathbf{h}|^2 = \det M(\tilde{H}),
$$

a real scalar. The two conditions $N(\tilde{H})\geq0$ and $h_0\geq0$ are together equivalent to $h_0\geq|\mathbf{h}|$, so the set of positive elements is the future light cone of the norm form:

$$
C_+ = \bigl\{h_0e_0 + i\mathbf{h}\in\mathbb{M}_+ : h_0 \geq |\mathbf{h}|\bigr\} .
$$

This is the **positive cone** of the algebra. Its boundary $h_0 = |\mathbf{h}|$ is the set of positive elements of rank one — the rank-one projectors and their non-negative multiples — which are the zero divisors of the norm form. Its interior $h_0>|\mathbf{h}|$ is the set of positive definite elements.

### The cone is self-dual

The trace pairing on $\mathbb{M}_+$ is

$$
\mathrm{Tr}(\tilde{H}\tilde{E}) = 2\,\mathrm{Sc}(\tilde{H}\tilde{E}) = 2\bigl(h_0a_0 + \mathbf{h}\cdot\mathbf{a}\bigr),
$$

where $\tilde{E} = a_0e_0 + i\mathbf{a}$. Direct computation of the pairing on the Hermitian basis gives

$$
\mathrm{Tr}(e_0e_0) = 2, \qquad \mathrm{Tr}(e_0\,ie_k) = 0, \qquad \mathrm{Tr}(ie_j\,ie_k) = 2\delta_{jk},
$$

so the trace pairing is the positive definite Euclidean form of signature $(4,0)$ in the coefficients, up to the factor two. The **dual cone** is

$$
C_+^{*} = \bigl\{\tilde{H} : \mathrm{Tr}(\tilde{H}\tilde{E})\geq0 \ \text{ for all } \tilde{E}\in C_+\bigr\},
$$

and it coincides with $C_+$. To see this, if $h_0\geq|\mathbf{h}|$ then $h_0a_0+\mathbf{h}\cdot\mathbf{a}\geq h_0a_0-|\mathbf{h}|\,|\mathbf{a}|\geq0$ for every $a_0\geq|\mathbf{a}|$, so $C_+^{*}\supseteq C_+$. Conversely, if $h_0<|\mathbf{h}|$, take $\tilde{E}$ on the boundary with $\mathbf{a} = -\lambda\,\hat{\mathbf{h}}$ and $a_0 = \lambda$; then $h_0a_0+\mathbf{h}\cdot\mathbf{a} = \lambda(h_0-|\mathbf{h}|)<0$ for $\lambda>0$, so $\tilde{H}\notin C_+^{*}$. Hence $C_+^{*}=C_+$: **the positive cone is self-dual with respect to the trace pairing.**

The self-duality is what makes the trace pairing the natural pairing of measurement theory. The same pairing that gives the Born rule, $p_y = \mathrm{Tr}(\tilde{\rho}\tilde{E}_y)$, expresses the duality between states and effects, and it makes the cone its own dual. There is no second pairing needed to define the allowed measurements.

### Extremal rays and the pure states

The extreme rays of $C_+$ are the rays through the rank-one projectors $\tilde{P}_+(\hat{\mu}) = \tfrac12(e_0+i\hat{\mu})$ and their positive multiples; every positive element is a non-negative combination of these. On the trace-one slice — the intersection of $C_+$ with the affine hyperplane $\mathrm{Tr}(\tilde{\rho}) = 1$ — the extreme points are exactly the pure states. This is the cone-theoretic statement of the fact, developed in the companion articles, that the Bloch ball is the trace-one slice of the cone and its boundary is the set of idempotents. The normalized states are a section of the cone, and the pure states are its extreme rays.

## Effects

### Definition

An **effect** is a positive element bounded above by the identity:

$$
0 \;\leq\; \tilde{E} \;\leq\; e_0 .
$$

Effects are the possible measurement outcomes. Writing $\tilde{E} = a_0e_0+i\mathbf{a}$, the two inequalities are

$$
a_0 \geq |\mathbf{a}| \qquad \text{and} \qquad 1-a_0 \geq |\mathbf{a}|,
$$

because $e_0-\tilde{E} = (1-a_0)e_0 - i\mathbf{a}$ is positive exactly when $1-a_0\geq|\mathbf{a}|$. Equivalently,

$$
|\mathbf{a}| \;\leq\; \min\bigl(a_0,\ 1-a_0\bigr),
$$

which requires $0\leq a_0\leq1$. The set of effects is thus the intersection of the cone $C_+$ with its reflection $e_0 - C_+$; it is a compact convex body, the **operator interval** $[0,e_0]$.

### The extremes of the effect body

The extreme points of the operator interval are exactly the idempotents,

$$
\tilde{E}^2 = \tilde{E} \quad\Longleftrightarrow\quad \tilde{E}\in\mathrm{ext}[0,e_0],
$$

i.e. the elements $a_0 = 1$ with $|\mathbf{a}|=0$ (the identity) and $a_0 = \tfrac12$ with $|\mathbf{a}| = \tfrac12$ (the rank-one projectors). A **projective measurement** uses only these extreme effects; a general measurement uses interior effects, which are convex combinations $\tilde{E} = t\tilde{P}_+ + (1-t)\tilde{P}_-$ of orthogonal idempotents. An interior effect is a "soft" outcome: it responds partially to both alternatives, which is exactly what allows a measurement to have more outcomes than the dimension.

### The Born rule for effects

For any state $\tilde{\rho}$ and effect $\tilde{E}$,

$$
p = \mathrm{Tr}(\tilde{\rho}\tilde{E}) = 2\,\mathrm{Sc}(\tilde{\rho}\tilde{E}) \in [0,1],
$$

because $\tilde{\rho}\geq0$, $\tilde{E}\geq0$ make the trace non-negative, and $\tilde{E}\leq e_0$ gives $p\leq\mathrm{Tr}(\tilde{\rho}) = 1$. This is the Born rule in its general form; the projective case is $\tilde{E} = \tilde{P}$, and then $p = \mathrm{Tr}(\tilde{\rho}\tilde{P})$ is the usual probability of an eigenspace. No additional postulate is required for the general measurement: functions of effects are obtained by the same trace pairing that gives the projective Born rule.

## POVMs

### Definition and statistics

A **positive operator-valued measure** is a finite or countable family of effects resolving the identity:

$$
\tilde{E}_y \geq 0, \qquad \sum_y \tilde{E}_y = e_0 .
$$

Given a state $\tilde{\rho}$, the outcome probabilities are $p_y = \mathrm{Tr}(\tilde{\rho}\tilde{E}_y)$. They are non-negative and sum to one:

$$
\sum_y p_y = \mathrm{Tr}\!\left(\tilde{\rho}\sum_y\tilde{E}_y\right) = \mathrm{Tr}(\tilde{\rho}) = 1 .
$$

A **projection-valued measure** is the special case in which every $\tilde{E}_y$ is idempotent; then the effects are orthogonal, $\tilde{E}_y\tilde{E}_{y'} = \delta_{yy'}\tilde{E}_y$, and the POVM is a projective measurement. Every PVM is a POVM; the converse fails.

### The post-measurement state

A general measurement is specified not only by the outcome probabilities but by the state left behind. If the effect is written in a Kraus form

$$
\tilde{E}_y = \tilde{M}_y^\dagger\tilde{M}_y , \qquad \tilde{M}_y\in\mathbb{B},
$$

then the unnormalized post-measurement state is $\tilde{M}_y\tilde{\rho}\tilde{M}_y^\dagger$ and the normalized state is

$$
\tilde{\rho}_y = \frac{\tilde{M}_y\tilde{\rho}\tilde{M}_y^\dagger}{\mathrm{Tr}(\tilde{M}_y\tilde{\rho}\tilde{M}_y^\dagger)} .
$$

The outcome probability is $p_y = \mathrm{Tr}(\tilde{M}_y\tilde{\rho}\tilde{M}_y^\dagger) = \mathrm{Tr}(\tilde{\rho}\tilde{E}_y)$, and the resolution of the identity is $\sum_y\tilde{M}_y^\dagger\tilde{M}_y = e_0$. The measurement is therefore an **instrument**: a family of completely positive maps indexed by the outcome, one of which occurs. This is the measurement side of the channel formalism of the companion article *Quantum Channels and the Reversible/Irreversible Dichotomy*; a measurement followed by discarding the outcome is the channel $\Phi(\tilde{\rho}) = \sum_y\tilde{M}_y\tilde{\rho}\tilde{M}_y^\dagger$.

### Naimark dilation

Every POVM on the defining module $S$ is the compression of a projective measurement on a larger module. There is an ancillary space $\mathbb{C}^d$, an isometry $V:S\to S\otimes\mathbb{C}^d$, and a PVM $\{\tilde{F}_y\}$ on the larger space such that

$$
\tilde{E}_y = V^\dagger \tilde{F}_y V .
$$

This is **Naimark's dilation theorem**, the measurement analogue of Stinespring's dilation for channels. In the framework's language, the dilation adjoins an ancillary factor and replaces the general effects by orthogonal idempotents; the price is that the ancillary system must be traced out, which is precisely the information loss that a non-projective measurement represents. The dilation is standard; it is cited, not derived, and it belongs to the same circle of ideas as the Kraus representation of channels. It also shows why the framework's general measurement theory does not require abandoning the idempotent picture of a projective measurement: it embeds it in a larger algebra.

## Two Worked Examples

### The trine POVM

Let $\hat{n}_k$, $k=1,2,3$, be three unit vectors in the equatorial plane at $120^\circ$ from one another, so that $\sum_k\hat{n}_k = 0$ and $\sum_k\tilde{P}_+(\hat{n}_k) = \tfrac32 e_0$. Define

$$
\tilde{E}_k = \tfrac{2}{3}\,\tilde{P}_+(\hat{n}_k), \qquad k=1,2,3 .
$$

Each $\tilde{E}_k$ is an effect — its coefficients are $a_0 = \tfrac13$ and $|\mathbf{a}| = \tfrac13$, on the boundary of the interval — and they resolve the identity:

$$
\sum_{k=1}^{3}\tilde{E}_k = \tfrac{2}{3}\sum_{k=1}^{3}\tilde{P}_+(\hat{n}_k) = \tfrac{2}{3}\cdot\tfrac{3}{2}e_0 = e_0 .
$$

The trine POVM has three outcomes, which no projective measurement of a qubit can have. For the three equally likely states $\tilde{\rho}_k = \tilde{P}_+(\hat{n}_k)$, the probability of correctly identifying the state is

$$
P_{\mathrm{succ}} = \frac{1}{3}\sum_{k=1}^{3}\mathrm{Tr}(\tilde{\rho}_k\tilde{E}_k)
= \frac{1}{3}\sum_{k=1}^{3}\mathrm{Tr}\!\left(\tilde{\rho}_k\,\tfrac23\tilde{\rho}_k\right)
= \frac{1}{3}\sum_{k=1}^{3}\frac{2}{3} = \frac{2}{3},
$$

since $\tilde{\rho}_k^2 = \tilde{\rho}_k$ and $\mathrm{Tr}(\tilde{\rho}_k) = 1$. A projective measurement of a qubit has only two outcomes and cannot separate three symmetric states as well; the trine POVM is the standard example of a genuinely non-projective measurement, and it is expressed here purely in terms of the idempotents and the trace pairing of the algebra.

### Unambiguous discrimination

Let two non-orthogonal pure states have overlap $c = |\langle\psi_0|\psi_1\rangle|\in(0,1)$. A **projective** measurement of a qubit has two outcomes, each of which responds to both states, so neither outcome can certify which state was prepared. A POVM with three effects can:

$$
\tilde{E}_0 = \frac{1}{1+c}\,\tilde{P}\bigl(\psi_1^\perp\bigr), \qquad
\tilde{E}_1 = \frac{1}{1+c}\,\tilde{P}\bigl(\psi_0^\perp\bigr), \qquad
\tilde{E}_? = e_0-\tilde{E}_0-\tilde{E}_1 ,
$$

where $\tilde{P}(\psi^\perp)$ is the idempotent orthogonal to $|\psi\rangle$. The effect $\tilde{E}_0$ annihilates $|\psi_1\rangle$, so the outcome $0$ certifies $|\psi_0\rangle$; symmetrically for outcome $1$; and outcome $?$ is inconclusive. The resolution holds because the largest eigenvalue of $\tilde{E}_0+\tilde{E}_1$ is $1$ at this normalization, and the success probability for equal priors is

$$
P_{\mathrm{succ}} = \tfrac12\mathrm{Tr}(\tilde{\rho}_0\tilde{E}_0) + \tfrac12\mathrm{Tr}(\tilde{\rho}_1\tilde{E}_1)
= \tfrac12(1-c)+\tfrac12(1-c) = 1-c ,
$$

which is the standard Ivanovic–Dieks–Peres value. Unambiguous discrimination is thus possible exactly with a non-projective measurement, and its failure probability is the overlap. In the algebra the construction uses three effects, each of them a scaled idempotent of rank one and therefore on the boundary of the cone: the two conclusive outcomes are the idempotents orthogonal to the state they exclude, and the inconclusive outcome — the scaled idempotent $\tilde{E}_? = \frac{2c}{1+c}\tilde{P}(\hat{m})$ for a suitable direction $\hat{m}$ — is the effect that makes the resolution complete.

## The Positive Cone and the Meaning of a Measurement

Collecting the structure, a measurement in the framework is a resolution of the identity into positive elements of $\mathbb{M}_+$:

- **States** are the trace-one elements of the cone $C_+$; the cone is the future light cone of the norm form.
- **Effects** are the elements of the operator interval $[0,e_0]$, i.e. the cone intersected with its reflection through $\tfrac12 e_0$; in coefficients, $|\mathbf{a}|\leq\min(a_0,1-a_0)$.
- **POVMs** are resolutions of the identity by effects; **PVMs** are the resolutions by idempotents, i.e. by extreme effects.
- **Probabilities** are the trace pairing $p_y = \mathrm{Tr}(\tilde{\rho}\tilde{E}_y)$, and the pairing is the one under which the cone is self-dual.
- **Post-measurement states** are the Kraus images $\tilde{M}_y\tilde{\rho}\tilde{M}_y^\dagger$, normalized.

The general measurement is a convex decomposition of the identity into effects that are not extreme. The idempotents remain the extreme effects, and the projective measurement remains the extreme case; what the general measurement adds is the ability to have more outcomes than the dimension of the module, which is exactly what is needed for tasks such as state discrimination with more than two candidate states.

## What the Framework Does and Does Not Claim

**What it does.**

- It identifies the positive cone of $\mathbb{M}_+$ with the future light cone of the norm form and derives the effect condition $|\mathbf{a}|\leq\min(a_0,1-a_0)$.
- It shows that the cone is self-dual with respect to the trace pairing, so that one pairing serves both the Born rule and the state-effect duality.
- It identifies the idempotents as the extreme effects and the projective measurements as the extreme resolutions, with the general POVM as a convex decomposition.
- It expresses the general measurement, its Kraus form, and its post-measurement state entirely in terms of elements of $\mathbb{B}$.

**What it does not.**

- It does not derive the cone structure from a deeper principle; the cone is the positivity condition of the algebra, and positivity of a Hermitian operator is standard.
- It does not prove Naimark's theorem; the dilation is cited as standard.
- It does not claim that every POVM is physically implementable by a given apparatus; implementability is a dynamical question the algebra does not answer.
- It does not extend the classification of effects beyond the qubit; for higher-dimensional modules the effect body is more complicated, and the framework's defining module is two-dimensional.

## Open Questions

**1. The effect body in higher dimensions.** The characterization $|\mathbf{a}|\leq\min(a_0,1-a_0)$ is special to $M_2(\mathbb{C})$. For $\mathbb{B}\otimes\mathbb{B}$ and its effects, what is the analogous coefficient condition, and does the norm form of the tensor product define the cone?

**2. Instruments and information.** A general instrument produces a post-measurement state that depends on the outcome, and the information it leaves in the system is quantified by the disturbance it causes. Is there an algebraic characterization of the instruments that are "minimally disturbing" for a given POVM, in terms of the two sectors $\mathbb{M}_\pm$?

**3. The self-duality and the two pairings.** The cone is self-dual under the trace pairing; the norm form defines the cone but is a different, indefinite pairing. Is there an algebraic relation between the two pairings — a form of Lorentzian duality — that explains why the cone is the norm form's cone and the measurement pairing is the trace pairing?

**4. Continuous POVMs.** The article treats finite POVMs. Position and momentum measurements require continuous families of effects; their biquaternion form, and the status of the norm form for unbounded effects, is open.

**5. Empirical content.** The POVM formalism in biquaternion form reproduces the standard one and predicts nothing new.

## Summary

A general measurement of a qubit is a resolution of the identity into positive elements of the Hermitian subspace. The positive cone of $\mathbb{M}_+$ is the future light cone of the norm form:

$$
\tilde{E} = a_0e_0+i\mathbf{a}\geq0 \quad\Longleftrightarrow\quad a_0\geq|\mathbf{a}| \quad\Longleftrightarrow\quad N(\tilde{E}) = a_0^2-|\mathbf{a}|^2\geq0,\ a_0\geq0,
$$

and the cone is self-dual with respect to the trace pairing, $\mathrm{Tr}(\tilde{H}\tilde{E}) = 2(h_0a_0+\mathbf{h}\cdot\mathbf{a})$. An effect is an element of the operator interval $0\leq\tilde{E}\leq e_0$, characterized by $|\mathbf{a}|\leq\min(a_0,1-a_0)$; its extreme points are the idempotents, so the projective measurements are the extreme resolutions. A POVM is a family $\{\tilde{E}_y\}$ with $\tilde{E}_y\geq0$ and $\sum_y\tilde{E}_y = e_0$; the outcome probabilities are the trace pairing $p_y = \mathrm{Tr}(\tilde{\rho}\tilde{E}_y)$, and the post-measurement states are the Kraus images. Every POVM is the compression of a projective measurement on a larger space (Naimark), and every measurement is an instrument, a family of completely positive maps indexed by the outcome. The cone, the effects, and the Born rule are thus all read off the algebra: positivity is the norm form's non-negativity, and measurement is the trace pairing on the effect body.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $\mathbb{M}_+$ | Hermitian subspace (states and effects) |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion units, $e_k^2 = -e_0$ |
| $i$ | Central scalar imaginary |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$ | Norm form |
| $C_+ = \{h_0e_0+i\mathbf{h}: h_0\ge|\mathbf{h}|\}$ | Positive cone (future light cone of $N$) |
| $C_+^{*} = C_+$ | Self-duality under the trace pairing |
| $\mathrm{Tr}(\tilde{H}\tilde{E}) = 2(h_0a_0+\mathbf{h}\cdot\mathbf{a})$ | Trace pairing |
| $0\le\tilde{E}\le e_0$ | Effect (operator interval) |
| $|\mathbf{a}|\le\min(a_0,1-a_0)$ | Effect condition in coefficients |
| $\mathrm{ext}[0,e_0] = \{\text{idempotents}\}$ | Extreme effects |
| $\{\tilde{E}_y\}$, $\tilde{E}_y\ge0$, $\sum_y\tilde{E}_y = e_0$ | POVM |
| $p_y = \mathrm{Tr}(\tilde{\rho}\tilde{E}_y)$ | Born rule for a POVM |
| $\tilde{E}_y = \tilde{M}_y^\dagger\tilde{M}_y$ | Kraus form of an effect |
| $\tilde{\rho}_y = \tilde{M}_y\tilde{\rho}\tilde{M}_y^\dagger/p_y$ | Post-measurement state |
| $\tilde{E}_y = V^\dagger\tilde{F}_yV$ | Naimark dilation |
| $\tilde{E}_k = \tfrac23\tilde{P}_+(\hat{n}_k)$ | Trine POVM |

## Further Reading

- A. Peres, *Quantum Theory: Concepts and Methods* (Kluwer, 1995), for POVMs, effects, and generalized measurements.
- K. Kraus, *States, Effects, and Operations* (Springer, 1983), for the operator-algebraic formulation of effects and instruments.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for POVMs, Naimark's dilation, and the post-measurement state.
- M. A. Naimark, "Spectral functions of a symmetric operator," *Izvestiya Akademii Nauk SSSR, Seriya Matematicheskaya* **4** (1940) 277–318, for the dilation of a POVM to a projective measurement.
- C. W. Helstrom, *Quantum Detection and Estimation Theory* (Academic Press, 1976), for state discrimination and the role of non-projective measurements.
- I. D. Ivanovic, "How to differentiate between non-orthogonal states," *Physics Letters A* **123** (1987) 257–259; D. Dieks, "Overlap and distinguishability of quantum states," *Physics Letters A* **126** (1988) 303–306; A. Peres, "How to differentiate between non-orthogonal states," *Physics Letters A* **128** (1988) 19, for unambiguous discrimination.
- I. Bengtsson and K. Życzkowski, *Geometry of Quantum States* (Cambridge, 2006), for the geometry of the state cone, the effect body, and self-duality.
- The companion articles of this series: *Quantum Mechanics in Biquaternionic Form*, *The Born Rule as a Trace Formula — Derivation and Comparison*, *The Bloch Ball as the Trace-One Slice of the Future Light Cone*, *Quantum Channels and the Reversible/Irreversible Dichotomy*, and *Decoherence as Idempotent Projection*.
