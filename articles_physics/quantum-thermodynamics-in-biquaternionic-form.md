# __Quantum Thermodynamics in Biquaternionic Form__

## Introduction

Quantum thermodynamics is the thermodynamics of systems whose state is a density operator: equilibrium is the Gibbs state, and the thermodynamic quantities — internal energy, entropy, free energy, heat capacity — are functionals of that state. This article asks what the biquaternion framework adds to that account, and it keeps the answer modest: the framework supplies a **reading** of the standard objects, not a new law.

The reading rests on one formula, inherited from the companion articles:

$$
\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H).
$$

The trace is **twice the scalar part**. This is not a convenience of notation: in the biquaternion algebra the trace *is* the scalar extraction, so the partition function and every thermal average are computed by taking the scalar part of a product and doubling it. The present article uses this formula as the computational spine throughout, in place of a generic matrix trace.

Two structural facts follow and are developed below. First, the Gibbs state of a qubit is an element of the Hermitian subspace $\mathbb{M}_+$ — a point in the Bloch ball — and its thermodynamic functionals are scalars extracted from $\mathbb{M}_+$-valued objects. Second, the free energy is the additive real scalar carried by the **modular Hamiltonian** $K=-\log\tilde\rho$, which also lies in $\mathbb{M}_+$; and the temperature $\beta$ that parametrises the state measures a displacement along the imaginary-time direction of the material sector $\mathbb{M}_-$, as the companion articles on the KMS condition and on the partition function record.

The article proceeds as follows. The Gibbs state is defined and its existence condition — the convergence of $Z$ — is treated as part of the content rather than as a technicality. The thermodynamic quantities are then written as functionals of the state and computed through the trace formula. The Gibbs state is characterised variationally, as the minimiser of the free-energy functional, and the Legendre structure relating $\log Z$, the entropy, and the free energy is set out with its signs checked against the thermodynamic identities. The low- and high-temperature limits are computed, the KMS condition is identified as the operator-algebraic characterisation of the same state, and the closing section separates what the framework adds from what it does not.

**Conventions.** Those of the companion articles. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with quaternion basis $e_0=1,e_1,e_2,e_3$ satisfying $e_k^2=-e_0$, and scalar imaginary $i$ with $i^2=-1$. The four fixed-point subspaces are the complex subspace $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ (the complex scalars, the centre of $\mathbb{B}$), the real-quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the Hermitian subspace $\mathbb{M}_+$ (real scalar part, imaginary vector part; the informational sector), and the anti-Hermitian subspace $\mathbb{M}_-$ (imaginary scalar part, real vector part; the material sector, whose time coordinate is $ict$). A Hermitian element is written $\tilde H=h_0e_0+i\mathbf h$ with $h_0\in\mathbb{R}$, $\mathbf h\in\mathbb{R}^3$; a state is $\tilde\rho=\tfrac12(e_0+i\mathbf r)$ with $|\mathbf r|\le1$. The trace formula is $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$. Units are $\hbar=1$ and $k_B=1$, so $\beta=1/T$ and the entropy is measured in units of $k_B$; restoring $k_B$ multiplies the entropy and the heat capacity by $k_B$.

## The Gibbs State and the Convergence of $Z$

At inverse temperature $\beta$ a quantum system with Hamiltonian $\tilde H$ is described by the **Gibbs state**

$$
\tilde\rho_\beta=\frac{1}{Z}\,e^{-\beta\tilde H},\qquad
Z(\beta)=\mathrm{Tr}\big(e^{-\beta\tilde H}\big),
$$

provided the trace converges. The convergence condition is part of the content, because when it fails the state does not exist.

For a **finite-level** system the trace is a finite sum of exponentials, so $Z$ is an entire function of $\beta$ and the Gibbs state exists for every real $\beta$. A single biquaternion is a two-level system, and $n$ of them span $M_{2^n}(\mathbb{C})$; this is the case in which the framework's exact computations live, and it is why no restriction appears on the closed formulas below.

For a system whose spectrum is unbounded above and bounded below — the generic many-body case — convergence depends on the real part of $\beta$. With eigenvalues $E_n\to+\infty$,

$$
|Z(\beta)|\le\sum_n e^{-\mathrm{Re}(\beta)E_n},
$$

so the sum converges absolutely for $\mathrm{Re}\,\beta>0$ and diverges for $\mathrm{Re}\,\beta<0$. The physical domain is the half-plane $\mathrm{Re}\,\beta>0$, that is, positive temperature. The boundary $\beta\to0^+$ is the infinite-temperature limit, and whether the limit exists is a property of the spectrum. A harmonic oscillator of frequency $\omega$ has $Z=e^{-\beta\omega/2}/(1-e^{-\beta\omega})$, finite for $\beta>0$ and divergent as $\beta\to0^+$; a qubit has $Z\to2$, finite. The convergence condition therefore decides the behaviour at infinite temperature, not merely at zero.

The framework's Hamiltonian is Hermitian, $\tilde H\in\mathbb{M}_+$, so its eigenvalues are real; in the two-level case they are $h_0\pm|\mathbf h|$. From the companion article on the partition function, the thermal operator is

$$
e^{-\beta\tilde H}=e^{-\beta h_0}\Big(\cosh(\beta|\mathbf h|)\,e_0-i\sinh(\beta|\mathbf h|)\,\hat{\mathbf h}\Big),
\qquad \hat{\mathbf h}=\frac{\mathbf h}{|\mathbf h|},
$$

an element of $\mathbb{M}_+$. Applying the trace formula with $\tilde P=e_0$ gives

$$
Z=2\,\mathrm{Sc}\big(e^{-\beta\tilde H}\big)=2e^{-\beta h_0}\cosh(\beta|\mathbf h|),
$$

and division gives the state

$$
\tilde\rho_\beta=\tfrac12\big(e_0+i\mathbf r\big),\qquad
\mathbf r=-\tanh(\beta|\mathbf h|)\,\hat{\mathbf h}.
$$

Its scalar part is $\mathrm{Sc}(\tilde\rho_\beta)=\tfrac12$, so $\mathrm{Tr}(\tilde\rho_\beta)=2\,\mathrm{Sc}(\tilde\rho_\beta)=1$: normalization is itself the trace formula. The state lies in the Bloch ball, with $|\mathbf r|=\tanh(\beta|\mathbf h|)\le1$. It is mixed for every finite $\beta$ and approaches the pure ground state $\tilde P_-(\hat{\mathbf h})=\tfrac12(e_0-i\hat{\mathbf h})$ only as $\beta\to\infty$; as $\beta\to0$ it tends to the maximally mixed state $\tfrac12e_0$, the centre of the ball. The Gibbs state is thus a temperature-parametrised path in the Bloch ball from the centre toward the boundary, and thermodynamics is the study of the scalars along that path.

## Thermodynamic Quantities as Functionals of the State

Every thermodynamic quantity of the canonical ensemble is a functional of the Gibbs state, and in the framework each is a scalar extracted by the trace formula:

- internal energy: $U[\tilde\rho]=\mathrm{Tr}(\tilde\rho\tilde H)=2\,\mathrm{Sc}(\tilde\rho\tilde H)$;
- entropy: $S[\tilde\rho]=-\mathrm{Tr}(\tilde\rho\log\tilde\rho)=-2\,\mathrm{Sc}(\tilde\rho\log\tilde\rho)$;
- free energy: $F[\tilde\rho]=U[\tilde\rho]-\tfrac1\beta S[\tilde\rho]$;
- heat capacity: $C=\partial U/\partial T$.

The entropy functional needs the logarithm, which exists on $\mathbb{B}$ but is multivalued. The companion exercise on entanglement entropy establishes that $S=-2\,\mathrm{Sc}(\tilde\rho\log\tilde\rho)$ is correct in the interior of the Bloch ball when the principal branch is used, and that the logarithm — hence the formula written this way — is undefined at the pure states, which are zero divisors; the value $S=0$ there is the continuous extension, not a value the logarithm takes. This edge is kept visible rather than smoothed over, and it returns in the variational section below.

For the qubit the trace formula evaluates each functional explicitly. With $x=\beta|\mathbf h|$ and $\mathbf r=-\tanh x\,\hat{\mathbf h}$, the product $\tilde\rho\tilde H$ has scalar part

$$
\mathrm{Sc}(\tilde\rho\tilde H)=\tfrac12\big(h_0+\mathbf r\cdot\mathbf h\big)=\tfrac12\big(h_0-|\mathbf h|\tanh x\big),
$$

so

$$
U=2\,\mathrm{Sc}(\tilde\rho\tilde H)=h_0-|\mathbf h|\tanh x .
$$

The eigenvalues of $\tilde\rho$ are the level populations, $\lambda_\pm=\tfrac12(1\pm\tanh x)$ with $\lambda_+$ the ground-state population, and the entropy is the binary entropy of the pair:

$$
S=-\lambda_+\log\lambda_+-\lambda_-\log\lambda_-=\log 2+\log\cosh x-x\tanh x .
$$

The free energy is $F=U-S/\beta$, which also equals $-\beta^{-1}\log Z$:

$$
F=h_0-\frac{\log 2+\log\cosh x}{\beta}.
$$

The **heat capacity** is a fluctuation. Differentiating $U$ at fixed spectrum,

$$
C=\frac{\partial U}{\partial T}=k_B\,\beta^2\,\mathrm{Var}(\tilde H),
\qquad
\mathrm{Var}(\tilde H)=\mathrm{Tr}(\tilde\rho\tilde H^2)-\big(\mathrm{Tr}(\tilde\rho\tilde H)\big)^2 .
$$

Since $\tilde H^2=(h_0^2+|\mathbf h|^2)e_0+2ih_0\mathbf h$ lies in $\mathbb{M}_+$, the variance is computed by the same trace formula:

$$
\mathrm{Var}(\tilde H)=2\,\mathrm{Sc}(\tilde\rho\tilde H^2)-\big(2\,\mathrm{Sc}(\tilde\rho\tilde H)\big)^2=|\mathbf h|^2\,\mathrm{sech}^2x .
$$

Hence $C=x^2\mathrm{sech}^2x$ in units of $k_B$: the two-level **Schottky heat capacity**. It is non-negative because a variance is, and it vanishes at both ends of the temperature range, with a maximum $C_{\max}=0.439229$ at $x=1.199679$, the root of $x\tanh x=1$. The framework adds nothing to the value; it supplies the route, since both $\mathrm{Tr}(\tilde\rho\tilde H)$ and $\mathrm{Tr}(\tilde\rho\tilde H^2)$ are scalar extractions.

**Numerical check on an independently chosen case.** Take $h_0=0.4$, $\mathbf h=(0.5,0.2,-0.6)$, $\beta=0.8$. Then $|\mathbf h|=0.8062258$, $x=0.6449806$, and the eigenvalues are $h_0\pm|\mathbf h|=1.2062258$ and $-0.4062258$. The trace formula gives

$$
Z=2\,\mathrm{Sc}\big(e^{-\beta\tilde H}\big)=2e^{-0.32}\cosh(0.6449806)=1.7649944,
$$

while the direct sum over levels gives $e^{-0.8(1.2062258)}+e^{-0.8(-0.4062258)}=1.7649944$. The functionals are $U=-0.0581630$, $S=0.5216171$, $F=-0.7101844$, and $C=0.2816555$; they satisfy $F=U-S/\beta$ to machine precision. A four-level **product** Hamiltonian — two independent qubits with $(h_{01},\mathbf h_1)=(0.3,(0.2,0,-0.4))$ and $(h_{02},\mathbf h_2)=(-0.7,(0.1,0.5,0.2))$ at $\beta=1.1$ — gives $Z=8.2828313$, equal both to the product of the two single-qubit partition functions and to the direct sum of the four level weights; its functionals satisfy the same Legendre relations.

## The Variational Characterisation

The Gibbs state is not merely the state obtained by exponentiating the Hamiltonian; it is selected by a variational principle, and the principle can be stated entirely in the framework's terms.

Consider the free-energy functional on states,

$$
\mathcal F[\tilde\rho]=\mathrm{Tr}(\tilde\rho\tilde H)-\frac{1}{\beta}S[\tilde\rho]
=\mathrm{Tr}(\tilde\rho\tilde H)+\frac{1}{\beta}\mathrm{Tr}(\tilde\rho\log\tilde\rho),
$$

with $S[\tilde\rho]=-\mathrm{Tr}(\tilde\rho\log\tilde\rho)$. Extremise $\mathcal F[\tilde\rho]-\mu\,(\mathrm{Tr}\tilde\rho-1)$ over Hermitian elements of $\mathbb{M}_+$. The variation gives

$$
\tilde H+\frac{1}{\beta}\big(\log\tilde\rho+e_0\big)-\mu\,e_0=0,
$$

hence $\log\tilde\rho=-\beta\tilde H+(\mu\beta-1)e_0$ and

$$
\tilde\rho=\frac{e^{-\beta\tilde H}}{Z},\qquad Z=\mathrm{Tr}\,e^{-\beta\tilde H}.
$$

The stationary point is the Gibbs state, and it is a minimum: $\mathcal F$ is convex, because $-\tfrac1\beta S$ is convex ($S$ is concave) while $\mathrm{Tr}(\tilde\rho\tilde H)$ is linear. The minimum value is the free energy,

$$
\min_{\tilde\rho}\mathcal F[\tilde\rho]=\mathcal F[\tilde\rho_\beta]=-\frac{1}{\beta}\log Z .
$$

The same statement can be read as the **maximum-entropy principle**: at fixed internal energy $\mathrm{Tr}(\tilde\rho\tilde H)=U$, the Gibbs state maximises $S[\tilde\rho]$, and the two variational problems are Legendre transforms of one another. The derivation uses only the trace formula and the entropy functional, both of which are framework objects.

One caveat belongs here. The functional $\mathcal F$ is defined where $\log\tilde\rho$ exists, that is, in the interior of the Bloch ball. The minimiser is interior for every finite $\beta$, since $|\mathbf r|=\tanh(\beta|\mathbf h|)<1$, but as $\beta\to\infty$ it approaches the boundary, where the functional is undefined. The variational characterisation therefore describes the finite-$\beta$ states exactly and the zero-temperature state only as a limit — the same boundary already noted for the entropy.


## Legendre Structure and Thermodynamic Identities

The thermodynamic potentials are not independent; they are Legendre transforms of one another, with $\log Z$ as the generating function. In the present units ($\hbar=k_B=1$, $\beta=1/T$),

$$
A(\beta):=\log Z,\qquad
U=-\frac{\partial A}{\partial\beta},\qquad
S=A+\beta U=A-\beta\frac{\partial A}{\partial\beta},\qquad
F=-\frac{A}{\beta}=U-\frac{S}{\beta}.
$$

The first two say that $A$ and $S$ are Legendre conjugates in the variables $\beta$ and $U$: from $S=A+\beta U$ and $U=-A'$ one finds

$$
\frac{\partial S}{\partial U}=\beta,
$$

which is the thermodynamic identity $\mathrm{d}U=T\,\mathrm{d}S$ at fixed spectrum, and the involution returns $A=S-\beta U$. The relation $F=U-TS$ says that $F$ is the Legendre transform of the energy in the entropy, with $T=\partial U/\partial S$, and it satisfies

$$
\frac{\partial F}{\partial T}=-S .
$$

All four identities hold for the explicit qubit functions of the preceding section. On the case checked above they hold numerically: $S=A+\beta U$ and $F=U-S/\beta$ to $10^{-31}$, while finite differences reproduce $\partial S/\partial U=\beta=0.8$ and $\partial F/\partial T=-S$ to eight digits. The same relations hold for the four-level product Hamiltonian.

In the framework each of $A$, $U$, $S$, $F$ is a scalar obtained by the trace formula from an $\mathbb{M}_+$-valued object: $U=2\,\mathrm{Sc}(\tilde\rho\tilde H)$, $S=-2\,\mathrm{Sc}(\tilde\rho\log\tilde\rho)$, and $F=-\beta^{-1}A$ with $A=\log Z=\mathrm{Sc}(K-\beta\tilde H)$, the scalar part of the modular Hamiltonian once the Hamiltonian's own scalar part is removed (next section). The Legendre structure itself is standard thermodynamics; the framework's contribution is that every member of the chain is a scalar extraction from $\mathbb{M}_+$.

## Low- and High-Temperature Limits

The limits test the signs and the normalizations of the preceding sections, and they display where the convergence condition bites.

**Low temperature, $\beta\to\infty$ ($T\to0$).** Since $\tanh x\to1$ and $\log\cosh x-x\tanh x\to-\log2$,

$$
\mathbf r\to-\hat{\mathbf h},\qquad
\tilde\rho\to\tilde P_-(\hat{\mathbf h})=\tfrac12\big(e_0-i\hat{\mathbf h}\big),
$$

the pure ground state, and

$$
U\to h_0-|\mathbf h|,\qquad S\to0,\qquad F\to h_0-|\mathbf h|,\qquad C\to0 .
$$

The internal energy tends to the lower eigenvalue $h_0-|\mathbf h|$ and the free energy to the same value, as it must at zero temperature; the entropy vanishes, and the heat capacity vanishes because the system is frozen into a single level. The limit is finite throughout for the qubit.

**High temperature, $\beta\to0$ ($T\to\infty$).** Since $\tanh x\to0$ and $\log\cosh x\to0$,

$$
\mathbf r\to0,\qquad \tilde\rho\to\tfrac12 e_0,
$$

the maximally mixed state, and

$$
U\to h_0,\qquad S\to\log 2,\qquad C\to0,\qquad F=-\frac{\log Z}{\beta}\to-\infty .
$$

The internal energy tends to the arithmetic mean $h_0$ of the two levels, which are equally populated; the entropy tends to $\log2$, the maximum for a two-state system; and the heat capacity vanishes because the populations are already equal and further heating changes nothing. The free energy diverges as $-(\log2)/\beta$: when $Z$ tends to the finite degeneracy $2$, $-T\log Z$ diverges in $T$, not in the state.

| Quantity | $\beta\to\infty$ ($T\to0$) | $\beta\to0$ ($T\to\infty$) |
|---|---|---|
| $\tilde\rho$ | $\tilde P_-(\hat{\mathbf h})$ (pure) | $\tfrac12 e_0$ (maximally mixed) |
| $U$ | $h_0-|\mathbf h|$ | $h_0$ |
| $S$ | $0$ | $\log 2$ |
| $F$ | $h_0-|\mathbf h|$ | $-\infty$ |
| $C$ | $0$ | $0$ |

The high-temperature limit is exactly where the convergence condition of the second section acts. The qubit's $Z\to2$ is finite, so the limit exists and gives $S\to\log2$. For the harmonic oscillator, $Z\to\infty$ as $\beta\to0^+$, so no state at $\beta=0$ exists and the entropy has no finite high-temperature limit. That difference is invisible in the finite-level formulas alone; it is a property of the spectrum, and it is why the convergence of $Z$ was treated above as content.

## The KMS Condition as the Characterisation of the Same State

The Gibbs state is one description of thermal equilibrium; the KMS condition is another, and the companion article on the KMS condition shows that they describe the same state, not two facts that happen to agree.

In the framework, with operators $\tilde A,\tilde B\in\mathbb{B}$ and thermal state $\omega_\beta$, the correlation function $F_{\tilde A\tilde B}(t)=\omega_\beta(\tilde A\,\alpha_t(\tilde B))$ extends analytically to the strip $0<\mathrm{Im}\,t<\beta$ and satisfies the boundary relation

$$
F_{\tilde A\tilde B}(t+i\beta)=F_{\tilde B\tilde A}(-t).
$$

By the Haag–Hugenholtz–Winnink theorem this relation characterises the thermal state at inverse temperature $\beta$, and the Gibbs state satisfies it; the two are the same state. The framework's contribution is the location of the objects. The analytic continuation is a shift in the complexified time plane whose imaginary direction is the time coordinate $ict$ of $\mathbb{M}_-$ and whose real direction is the time coordinate of $\mathbb{M}_+$, as the KMS article states, and the **modular Hamiltonian**

$$
K=-\log\tilde\rho_\beta=\beta\tilde H+(\log Z)\,e_0=\beta\big(\tilde H-F e_0\big)
$$

lies in $\mathbb{M}_+$ — it is Hermitian by construction. The last equality uses $\log Z=-\beta F$ and displays the role of the free energy: it is the real scalar by which the Hamiltonian must be shifted so that $K$ generates the modular flow of the Gibbs state. Equivalently, $\mathrm{Sc}(K-\beta\tilde H)=\log Z$, so $\log Z$ — and with it the whole Legendre chain — is a scalar part of an $\mathbb{M}_+$ element. Nothing here is additional to the KMS article's statement; it is recorded because the same state is the subject of both, and because the modular Hamiltonian is where the free energy sits in the framework.

## What the Framework Adds, and What It Does Not

The framework adds a **reading** with three components.

First, the computational spine is algebraic: the trace is twice the scalar part, so the partition function, every thermal average, the entropy, and the heat capacity are obtained by extracting a scalar from a product of $\mathbb{M}_+$ elements. The variance form of the heat capacity, $C=k_B\beta^2[2\,\mathrm{Sc}(\tilde\rho\tilde H^2)-(2\,\mathrm{Sc}(\tilde\rho\tilde H))^2]$, shows the reading at work.

Second, the state is geometric: the Gibbs state is the point $\mathbf r=-\tanh(\beta|\mathbf h|)\hat{\mathbf h}$ in the Bloch ball, and temperature traverses the ball from its centre toward its boundary.

Third, the temperature is a direction: $\beta$ measures a displacement along the imaginary-time axis of the material sector $\mathbb{M}_-$, while the modular Hamiltonian $K=\beta(\tilde H-Fe_0)$, which carries the free energy, lies in $\mathbb{M}_+$. The thermal structure is therefore a coupling of the two sectors of the kind the KMS article describes.

The framework does **not** produce a new thermodynamic law. The Gibbs state, the Legendre relations, the variational principle, the KMS characterisation, the Schottky heat capacity, and both temperature limits are standard, and the framework reproduces them. What it changes is where they live: the potentials become scalar extractions from the informational sector, and the temperature becomes an imaginary-time displacement in the material sector. Whether that reading has consequences beyond the standard account is open, and no such consequence is claimed here.

## Summary

Quantum thermodynamics in biquaternionic form is the thermodynamics of the Gibbs state $\tilde\rho_\beta=e^{-\beta\tilde H}/Z$, read through the trace formula $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$. The trace is the scalar extraction, so the partition function is $Z=2\,\mathrm{Sc}(e^{-\beta\tilde H})=2e^{-\beta h_0}\cosh(\beta|\mathbf h|)$ for a qubit, and every thermal average is twice a scalar part.

The Gibbs state exists only when $Z$ converges: always for a finite-level system, and in the half-plane $\mathrm{Re}\,\beta>0$ for a spectrum unbounded above. The infinite-temperature boundary $\beta\to0$ is where the condition matters, and it separates the qubit ($Z\to2$) from the oscillator ($Z\to\infty$).

The thermodynamic functionals of the state are the internal energy $U=\mathrm{Tr}(\tilde\rho\tilde H)$, the entropy $S=-\mathrm{Tr}(\tilde\rho\log\tilde\rho)$, the free energy $F=U-S/\beta$, and the heat capacity $C=\partial U/\partial T$. For a qubit they are $U=h_0-|\mathbf h|\tanh x$, $S=\log2+\log\cosh x-x\tanh x$, $F=h_0-(\log2+\log\cosh x)/\beta$, and $C=x^2\mathrm{sech}^2x$ with $x=\beta|\mathbf h|$, the Schottky form with maximum $0.439229$ at $x=1.199679$.

The Gibbs state is the minimiser of $\mathcal F[\tilde\rho]=\mathrm{Tr}(\tilde\rho\tilde H)-\beta^{-1}S[\tilde\rho]$, equivalently the maximiser of the entropy at fixed energy. The potentials are Legendre transforms: $S=\log Z+\beta U$ with $\partial S/\partial U=\beta$, and $F=U-TS$ with $\partial F/\partial T=-S$. The low-temperature limits are the pure ground state, $U=F=h_0-|\mathbf h|$, $S=C=0$; the high-temperature limits are $\tilde\rho=\tfrac12e_0$, $U=h_0$, $S=\log2$, $C=0$. The KMS condition $F_{\tilde A\tilde B}(t+i\beta)=F_{\tilde B\tilde A}(-t)$ is the operator-algebraic characterisation of the same state, and its modular Hamiltonian $K=-\log\tilde\rho=\beta(\tilde H-Fe_0)$ lies in $\mathbb{M}_+$.

The framework reproduces standard thermodynamics and claims no new law. Its addition is the reading: the potentials are scalar parts of $\mathbb{M}_+$ elements, the state is a path in the Bloch ball, and the temperature is a displacement along the imaginary-time axis of $\mathbb{M}_-$.


## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ | Complex subspace (centre of $\mathbb{B}$) |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace |
| $\mathbb{M}_+$ | Hermitian subspace (informational sector): real scalar, imaginary vector |
| $\mathbb{M}_-$ | Anti-Hermitian subspace (material sector): imaginary scalar, real vector |
| $\tilde H=h_0e_0+i\mathbf h$ | Hermitian Hamiltonian (observable) |
| $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$ | Trace formula (computational spine) |
| $Z=\mathrm{Tr}(e^{-\beta\tilde H})$ | Partition function |
| $\tilde\rho_\beta=e^{-\beta\tilde H}/Z=\tfrac12(e_0+i\mathbf r)$ | Gibbs state |
| $\mathbf r=-\tanh(\beta|\mathbf h|)\hat{\mathbf h}$ | Bloch vector of the Gibbs state |
| $x=\beta|\mathbf h|$ | Thermal parameter |
| $U=\mathrm{Tr}(\tilde\rho\tilde H)=h_0-|\mathbf h|\tanh x$ | Internal energy |
| $S=-\mathrm{Tr}(\tilde\rho\log\tilde\rho)=\log2+\log\cosh x-x\tanh x$ | Entropy (units of $k_B$) |
| $F=U-S/\beta=h_0-(\log2+\log\cosh x)/\beta$ | Free energy |
| $C=\partial U/\partial T=k_B\beta^2\mathrm{Var}(\tilde H)=x^2\mathrm{sech}^2x$ | Heat capacity (Schottky form) |
| $A(\beta)=\log Z$, $S=A+\beta U$, $F=U-TS$ | Legendre structure |
| $K=-\log\tilde\rho_\beta=\beta(\tilde H-Fe_0)$ | Modular Hamiltonian (in $\mathbb{M}_+$) |
| $F_{\tilde A\tilde B}(t+i\beta)=F_{\tilde B\tilde A}(-t)$ | KMS boundary relation |
| $\beta=1/T$ ($\hbar=k_B=1$) | Inverse temperature |

## Further Reading

- L. D. Landau and E. M. Lifshitz, *Statistical Physics, Part 1* (Pergamon, 1980), for the Gibbs state, the thermodynamic potentials, and the Legendre structure.
- H. B. Callen, *Thermodynamics and an Introduction to Thermostatistics* (Wiley, 1985), for the Legendre transforms and the thermodynamic identities.
- R. K. Pathria and P. D. Beale, *Statistical Mechanics* (Butterworth–Heinemann, 2011), for the canonical ensemble and the Schottky heat capacity of a two-level system.
- K. Huang, *Statistical Mechanics* (Wiley, 1987), for the partition function and its relation to the spectrum.
- J. Gemmer, M. Michel, and G. Mahler, *Quantum Thermodynamics* (Springer, 2009), for the quantum-statistical formulation of equilibrium thermodynamics.
- M. Le Bellac, *Thermal Field Theory* (Cambridge, 1996), for the imaginary-time formulation in which $\beta$ is the circumference of the thermal circle.
- R. Haag, N. M. Hugenholtz, and M. Winnink, "On the equilibrium states in quantum statistical mechanics," *Communications in Mathematical Physics* **5** (1967) 215–236, for the KMS characterisation of thermal equilibrium.
- M. Takesaki, *Tomita's Theory of Modular Hilbert Algebras and Its Applications* (Springer, 1970), for the modular Hamiltonian $K=-\log\rho$.
- M. A. Nielsen and I. L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the von Neumann entropy and its properties.
- Companion articles: *The Partition Function in Biquaternionic Form*, for the thermal operator and $Z$; *The KMS Condition and the Biquaternion Framework*, for the operator-algebraic characterisation and the modular Hamiltonian; *Quantum Mechanics in Biquaternionic Form*, for the state space, the trace pairing, and the entropy; *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* and *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, for the two sectors; *Exercise: Entanglement Entropy and the Partial Trace*, for the entropy functional $-2\,\mathrm{Sc}(\tilde\rho\log\tilde\rho)$ and its domain; *The Bloch Ball as the Trace-One Slice of the Future Light Cone*, for the geometry of the state space; *The Modular Theory of Tomita–Takesaki under the Biquaternion Framework*, for the modular structure in the framework.

