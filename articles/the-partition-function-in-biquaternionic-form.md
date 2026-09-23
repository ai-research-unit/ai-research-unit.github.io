# __The Partition Function in Biquaternionic Form__

## Introduction

The **partition function**

$$
Z = \mathrm{Tr}\big(e^{-\beta \tilde H}\big)
$$

is the central object of equilibrium statistical mechanics. It normalizes the thermal state, generates the free energy, and encodes the spectrum of the Hamiltonian. The question this article addresses is narrow and concrete: does $Z$ have a **biquaternion reading**, and does the split of the biquaternion algebra into the material and informational sectors force any modification of it?

The answer has two parts, and they should be kept apart from the outset.

The first part is that, for a **Hermitian** Hamiltonian — an element $\tilde H$ of the informational sector $\mathbb{M}_+$ — the partition function is exactly the ordinary one, and the algebra contributes a *reading* rather than a new object. The thermal operator $e^{-\beta\tilde H}$ is itself an element of $\mathbb{M}_+$; the trace formula $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$ identifies the trace with twice the scalar part; and $Z$ is therefore that scalar part, doubled. What the trace discards is the **imaginary vector part** of $e^{-\beta\tilde H}$. The material sector $\mathbb{M}_-$ does not appear in the thermal operator at all in this case; it appears in the **imaginary-time direction** along which $\beta$ is measured. So the honest finding is negative in the sense the subject demands: the algebra does not produce a second, rival partition function, and a "biquaternionic partition function" distinct from $Z$ is not needed.

The second part is the only place where the sector split changes the answer. If the generator is permitted an $\mathbb{M}_-$ component — that is, if $\tilde H$ is allowed to be **non-Hermitian** — then $Z$ can cease to be real and become complex, and the free energy can acquire an imaginary part. This extension is not forced by the framework, because observables are defined to be Hermitian elements of $\mathbb{M}_+$. It is recorded here as a boundary of the reading, not as a result.

The article proceeds as follows: the standard partition function and thermal state are recalled; the trace is identified with the scalar part; the thermal operator and the partition function are computed explicitly; the part the trace discards is examined; the place where the material sector genuinely enters — imaginary time — is made precise against the companion article on the KMS condition; and the non-Hermitian extension is computed.

**Conventions.** Those of the companion articles. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with quaternion basis $e_0=1,e_1,e_2,e_3$ satisfying $e_k^2=-e_0$, and scalar imaginary $i$ with $i^2=-1$. The Hermitian subspace $\mathbb{M}_+$ is the fixed-point set of the Hermitian conjugation $\dagger$; its elements have real scalar part and imaginary vector part. The anti-Hermitian subspace $\mathbb{M}_-$ is the fixed-point set of the anti-Hermitian conjugation $\flat=-\dagger$; its elements have imaginary scalar part and real vector part. The real-quaternion subspace $\mathbb{H}_{\mathbb{B}}$ is the fixed-point set of complex conjugation. We work in units with $\hbar=1$, so that $\beta=1/(k_BT)$ coincides with the KMS article's $\beta=\hbar/(k_BT)$; restoring $\hbar$ multiplies $\tilde H$ in the exponent by $1/\hbar$.

## The Partition Function and the Thermal State

For a quantum system with Hamiltonian $\tilde H$ at inverse temperature $\beta$, the partition function and thermal state are

$$
Z(\beta)=\mathrm{Tr}\big(e^{-\beta\tilde H}\big),\qquad
\tilde\rho=\frac{1}{Z}\,e^{-\beta\tilde H}.
$$

The standard derived quantities are the free energy, the internal energy, and the entropy,

$$
F=-\frac{1}{\beta}\log Z,\qquad
U=-\frac{\partial \log Z}{\partial \beta}=\mathrm{Tr}(\tilde\rho\,\tilde H),\qquad
S=-\mathrm{Tr}(\tilde\rho\log\tilde\rho),
$$

and the expectation value of any observable $\tilde A$ is $\langle\tilde A\rangle=\mathrm{Tr}(\tilde\rho\tilde A)$.

Two elementary facts about $Z$ govern everything below. First, **$Z$ depends only on the spectrum of $\tilde H$**: if $\tilde H$ has eigenvalues $E_n$, then $Z=\sum_n e^{-\beta E_n}$. Equivalently, it is invariant under any unitary change of basis. These are not features of the biquaternion framework; they are features of the trace, and the framework inherits them.

The framework adds two things to this standard picture. It gives the Hamiltonian and the state a definite home — the Hermitian subspace $\mathbb{M}_+$ — and it gives the trace a definite algebraic meaning, as the projection onto the scalar part. The rest of the article works out those two points and their consequences.

## The Trace as a Scalar Extraction

The biquaternion algebra is isomorphic to the algebra of $2\times2$ complex matrices, $\mathbb{B}\cong M_2(\mathbb{C})$. In the isomorphism of the companion articles,

$$
e_0\mapsto I_2,\qquad e_1\mapsto -i\sigma_1,\qquad e_2\mapsto -i\sigma_2,\qquad e_3\mapsto -i\sigma_3,
$$

and the scalar imaginary $i$ maps to $iI_2$. The **trace** of a general biquaternion $\tilde Q=Q_0e_0+Q_1e_1+Q_2e_2+Q_3e_3$, with $Q_\mu\in\mathbb{C}$, is therefore

$$
\mathrm{Tr}(\tilde Q)=2Q_0=2\,\mathrm{Sc}(\tilde Q).
$$

Here $\mathrm{Sc}(\tilde Q)=Q_0$ is the coefficient of $e_0$, which is a complex number for a general biquaternion and a **real** number when $\tilde Q\in\mathbb{M}_+$. The trace is thus a **scalar extraction**: it retains the $e_0$ coefficient and annihilates the three vector directions $e_1,e_2,e_3$.

On $\mathbb{M}_+$ this extraction is the trace pairing used throughout the corpus. Writing

$$
\tilde P=p_0e_0+i\mathbf p,\qquad \tilde H=h_0e_0+i\mathbf h,\qquad p_0,h_0\in\mathbb{R},\ \ \mathbf p,\mathbf h\in\mathbb{R}^3,
$$

for two elements of $\mathbb{M}_+$, the product has scalar part

$$
\mathrm{Sc}(\tilde P\tilde H)=p_0h_0+\mathbf p\cdot\mathbf h,
$$

and hence

$$
\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)=2\,(p_0h_0+\mathbf p\cdot\mathbf h).
$$

The derivation of this formula and its role in the Born rule are the subject of the companion article *The Born Rule as a Trace Formula*; here we only use it. Two features matter for the partition function. The formula is **bilinear and symmetric**, and it is **real** when both factors lie in $\mathbb{M}_+$. Note also that the product $\tilde P\tilde H$ need not itself lie in $\mathbb{M}_+$ — it acquires a real vector part $-\mathbf p\times\mathbf h$ in the quaternion product — and yet its scalar part, and therefore the trace, is still given by the formula above. The trace does not require the product to remain in $\mathbb{M}_+$; it requires only the factors to.

A remark on the alternative. The trace is not the only natural scalar that can be extracted from an element of $\mathbb{M}_+$; the **norm form** $N(\tilde Q)=\tilde Q\bar{\tilde Q}$ is another. On $\tilde H=h_0e_0+i\mathbf h$ it gives $N(\tilde H)=h_0^2-|\mathbf h|^2$, of signature $(1,3)$, and it is the form whose future cone defines the state space. A later section shows that the norm form of the thermal operator is blind to the level splitting and so cannot serve as a partition function. The trace, not the norm, is the scalar that thermodynamics uses; the companion article *The Born Rule as a Trace Formula* makes the general case for why.

## The Thermal Operator and the Partition Function

Let the Hamiltonian be a Hermitian element of the informational sector,

$$
\tilde H=h_0e_0+i\mathbf h,\qquad h_0\in\mathbb{R},\quad \mathbf h\in\mathbb{R}^3,
$$

with $|\mathbf h|$ the modulus. The first computation is the square of the imaginary vector part. For a pure real quaternion, $\mathbf h^2=-|\mathbf h|^2e_0$, so

$$
(i\mathbf h)^2=i^2\mathbf h^2=(-1)\big(-|\mathbf h|^2e_0\big)=|\mathbf h|^2e_0.
$$

The imaginary vector part therefore behaves like a **real** number of square $+|\mathbf h|^2$ — it is a boost-type generator, not a phase — and the scalar part $h_0e_0$ commutes with it. Hence

$$
e^{-\beta\tilde H}=e^{-\beta h_0}e^{-\beta i\mathbf h}
=e^{-\beta h_0}\Big(\cosh(\beta|\mathbf h|)\,e_0-i\sinh(\beta|\mathbf h|)\,\hat{\mathbf h}\Big),
\qquad \hat{\mathbf h}=\frac{\mathbf h}{|\mathbf h|}.
$$

This is the **thermal operator**. It is Hermitian, since $\tilde H^\dagger=\tilde H$ implies $(e^{-\beta\tilde H})^\dagger=e^{-\beta\tilde H}$, so it is an element of $\mathbb{M}_+$: its scalar part is real and its vector part is imaginary. Equivalently, it is $e^{-\beta h_0}$ times the unit-norm-form element $\tilde\Lambda=\cosh(\beta|\mathbf h|)e_0-i\sinh(\beta|\mathbf h|)\hat{\mathbf h}$, which is a **boost biquaternion** in $\mathbb{M}_+$ — the natural home of boosts, as the companion article on $\mathbb{M}_+$ records. The boost rapidity is $2\beta|\mathbf h|$ in the parametrization $\tilde\Lambda=\cosh(\psi/2)+i\sinh(\psi/2)\hat{\mathbf u}$, with $\hat{\mathbf u}=-\hat{\mathbf h}$.

Applying the trace formula with $\tilde P=e_0$ (the identity, which lies in $\mathbb{M}_+$) and using $e^{-\beta\tilde H}\in\mathbb{M}_+$,

$$
Z=\mathrm{Tr}\big(e^{-\beta\tilde H}\big)=2\,\mathrm{Sc}\big(e^{-\beta\tilde H}\big)=2e^{-\beta h_0}\cosh(\beta|\mathbf h|).
$$

This is the ordinary partition function of a two-level system with energies $h_0\pm|\mathbf h|$, since

$$
e^{-\beta h_0}\big(e^{-\beta|\mathbf h|}+e^{+\beta|\mathbf h|}\big)=2e^{-\beta h_0}\cosh(\beta|\mathbf h|).
$$

The two expressions agree because the eigenvalues of $\tilde H=h_0e_0+i\mathbf h$ are $h_0\pm|\mathbf h|$, in accordance with the matrix identification $\tilde H\mapsto h_0I+\mathbf h\cdot\boldsymbol\sigma$. The state is $\tilde\rho=e^{-\beta\tilde H}/Z$, whose scalar part is $\mathrm{Sc}(\tilde\rho)=\tfrac12$, so it has the Bloch form

$$
\tilde\rho=\tfrac12\big(e_0+i\mathbf r\big),\qquad \mathbf r=-\tanh(\beta|\mathbf h|)\,\hat{\mathbf h},\qquad |\mathbf r|=\tanh(\beta|\mathbf h|)\le 1.
$$

The thermal state is mixed for every finite $\beta$ and approaches the pure ground state $\tilde P_-(\hat{\mathbf h})=\tfrac12(e_0-i\hat{\mathbf h})$ only as $\beta\to\infty$. Its internal energy is

$$
U=\mathrm{Tr}(\tilde\rho\tilde H)=h_0+\mathbf r\cdot\mathbf h=h_0-|\mathbf h|\tanh(\beta|\mathbf h|),
$$

in agreement with $-\partial_\beta\log Z=h_0-|\mathbf h|\tanh(\beta|\mathbf h|)$, and its purity and entropy are the standard functions of $|\mathbf r|$.

As a check on a case chosen independently of the derivation, take $h_0=0.7$, $\mathbf h=(0.3,-0.5,0.8)$, $\beta=1.2$, so that $|\mathbf h|^2=0.98$ and $|\mathbf h|=0.98995$. The formula gives $Z=2e^{-0.84}\cosh(1.18794)=1.547753$, while summing the exponential of the eigenvalues $h_0\pm|\mathbf h|$ gives $e^{-2.02794}+e^{0.34794}=1.547753$; the matrix exponential of the corresponding $2\times2$ matrix agrees with the biquaternion form to machine precision. The Bloch modulus is $\tanh(1.18794)=0.829939$, and $U=h_0-|\mathbf h|\tanh(\beta|\mathbf h|)=-0.121597$ equals $\mathrm{Tr}(\tilde\rho\tilde H)$.

## What the Trace Discards

The thermal operator has a scalar part and an imaginary vector part,

$$
e^{-\beta\tilde H}=\underbrace{e^{-\beta h_0}\cosh(\beta|\mathbf h|)}_{\text{scalar}}\;e_0\;-\;i\underbrace{e^{-\beta h_0}\sinh(\beta|\mathbf h|)}_{\text{coefficient}}\;\hat{\mathbf h},
$$

and the trace keeps the first and annihilates the second. Three consequences are worth stating explicitly.

**The discarded part is the coherence.** The imaginary vector part of $e^{-\beta\tilde H}$ points along $-\hat{\mathbf h}$, and it is fixed by the same combination $\beta|\mathbf h|$ that fixes the Bloch vector $\mathbf r=-\tanh(\beta|\mathbf h|)\hat{\mathbf h}$ of the thermal state. It encodes the **orientation** of the thermal polarization. The partition function is blind to that orientation. $Z$ depends on $h_0$ and $|\mathbf h|$ but not on the direction $\hat{\mathbf h}$; equivalently, $Z$ is invariant under the conjugation $\tilde H\mapsto\tilde U\tilde H\tilde U^\dagger$ by any unitary biquaternion, which rotates $\hat{\mathbf h}$ while preserving the spectrum. The whole dependence of the thermal state on the axis of the Hamiltonian is invisible to $Z$ and appears only in $\tilde\rho$ and in expectation values.

**The discarded part is not lost.** The information the trace removes from $Z$ is retained by the **correlation functions**. The expectation value $\mathrm{Tr}(\tilde\rho\tilde A)=2\,\mathrm{Sc}(\tilde\rho\tilde A)$ and, in the thermal field-theoretic setting, the KMS correlation functions of the companion article are sensitive to the imaginary vector part. The partition function is thus the crudest unitary invariant of the thermal operator: it is the piece invariant under the full unitary group, and everything else is delegated to the correlators.

**The discarded part is not the material sector.** It is tempting to say that the trace "projects away the $\mathbb{M}_-$ sector". Read literally, that statement is not correct for a Hermitian Hamiltonian. Since $\tilde H\in\mathbb{M}_+$ implies $e^{-\beta\tilde H}\in\mathbb{M}_+$, the thermal operator has **no $\mathbb{M}_-$ component at all**; the subspace $\mathbb{M}_-$ does not appear in it. What the trace discards is the **imaginary vector part of $\mathbb{M}_+$**, which is $i$ times a real spatial vector — the same three real spatial directions that, with real coefficients, are the spatial part of $\mathbb{M}_-$. The correct division is therefore between the scalar (energy-like, spectral) content of the thermal operator, which $Z$ keeps, and its coherence content, which $Z$ discards. The material sector enters elsewhere, through imaginary time.

## Imaginary Time: Where the Material Sector Enters

The partition function can be written as the trace of the evolution operator at an **imaginary time**,

$$
Z=\mathrm{Tr}\big(e^{-\beta\tilde H}\big)=\mathrm{Tr}\,\tilde U(-i\beta),\qquad \tilde U(t)=e^{-i\tilde Ht},
$$

the analytic continuation $t\to-i\beta$ of the real-time evolution. This is not a convenience of the biquaternion framework; it is the standard relationship between the thermal trace and imaginary time, and it is the same continuation that makes the Matsubara formalism work.

It is here that the material sector $\mathbb{M}_-$ genuinely enters. The material sector's time coordinate is $ict$, imaginary by construction, so the continuation $t\to-i\beta$ of the evolution is a displacement along the $\mathbb{M}_-$ time direction: the analytic continuation to $t=-i\beta$ moves the Minkowski time coordinate to $ict=c\beta$, and the thermal operator is the evolution operator evaluated at that displaced point. In this sense the thermal circle of circumference $\beta$ — the compact imaginary-time direction over which the Euclidean formulation is defined — **lies along the time axis of $\mathbb{M}_-$**. The KMS article states the structural point that accompanies this: the complexified time direction in which the KMS continuation takes place is the sum of the imaginary time direction of $\mathbb{M}_-$ and the real time direction of $\mathbb{M}_+$, so that $\mathbb{M}_-\oplus i\mathbb{M}_-=\mathbb{B}$.

Two further facts tie the partition function to that structure, and both are consistent with the KMS article rather than additional to it.

First, the **normalization of the thermal state** is what makes the modular Hamiltonian a Hermitian element. From $\tilde\rho=e^{-\beta\tilde H}/Z$,

$$
K=-\log\tilde\rho=\beta\tilde H+\big(\log Z\big)e_0,
$$

which is Hermitian, hence an element of $\mathbb{M}_+$; the log-partition function $\log Z$ appears as the real scalar part of the modular Hamiltonian. The companion article records the general fact that $K=-\log\tilde\rho$ lies in $\mathbb{M}_+$; the partition function is precisely the additive scalar that makes this true for the Gibbs state.

Second, the **KMS boundary relation** $F_{AB}(t+i\beta)=F_{BA}(-t)$ of the companion article is the imaginary-time statement whose finite-dimensional shadow is the Gibbs form used here. The partition function is the normalization of the KMS state, and the strip width in that relation is the same $\beta$ that measures the imaginary-time displacement of the thermal trace. Nothing in the present article changes the KMS boundary relation; the partition function presupposes it.

So the material sector enters the partition function not as a component of the thermal operator but as the **direction and period** of the thermal trace: $Z$ is computed from the $\mathbb{M}_+$ Hamiltonian and normalized by an $\mathbb{M}_+$ modular Hamiltonian, while the circle on which the trace is taken lies along the $\mathbb{M}_-$ time.

## Is There a Genuine Modification?

We can now separate the two cases cleanly.

**Hermitian Hamiltonian: no modification.** For $\tilde H\in\mathbb{M}_+$, the object $Z=\mathrm{Tr}(e^{-\beta\tilde H})=2\,\mathrm{Sc}(e^{-\beta\tilde H})$ is exactly the ordinary partition function. The algebra's contribution is a reading with three components: the trace is a scalar extraction, the thermal operator is a scalar Boltzmann weight times a boost biquaternion in $\mathbb{M}_+$, and $\beta$ measures a displacement along the imaginary-time axis of $\mathbb{M}_-$. No second partition function arises, and none is required. If the framework is to have content here beyond notation, it must be content of this interpretive kind; the algebra alone does not supply a new $Z$.

It is worth confirming that the obvious rival scalar does not work. The norm form of the thermal operator is

$$
N\big(e^{-\beta\tilde H}\big)=e^{-2\beta h_0}\Big(\cosh^2(\beta|\mathbf h|)-\sinh^2(\beta|\mathbf h|)\Big)e_0=e^{-2\beta h_0}e_0,
$$

which is **independent of $|\mathbf h|$**. The norm form sees only the trace part $h_0$ of the Hamiltonian and is blind to the level splitting $|\mathbf h|$; its logarithm is linear in $\beta$ and would give a free energy independent of $\beta$, with no thermal population of the excited level. The trace is the scalar that thermodynamics requires, and the norm form is not a candidate partition function.

**Non-Hermitian generator: a complex partition function.** The one place where the sector split changes the answer is if the generator is allowed to leave $\mathbb{M}_+$. Let

$$
\tilde H=i a_0e_0-\mathbf a,\qquad a_0\in\mathbb{R},\quad \mathbf a\in\mathbb{R}^3,
$$

which is an element of $\mathbb{M}_-$ (imaginary scalar part $ia_0$, real vector part $-\mathbf a$). Because $\mathbf a$ is a pure real quaternion, $e^{\beta\mathbf a}=\cos(\beta|\mathbf a|)e_0+\sin(\beta|\mathbf a|)\hat{\mathbf a}$, and the scalar part of the thermal operator is no longer real:

$$
e^{-\beta\tilde H}=e^{-i\beta a_0}\Big(\cos(\beta|\mathbf a|)e_0+\sin(\beta|\mathbf a|)\hat{\mathbf a}\Big),
\qquad
Z=2e^{-i\beta a_0}\cos(\beta|\mathbf a|).
$$

The partition function is complex. Its modulus is $2|\cos(\beta|\mathbf a|)|$ and its phase is $-\beta a_0$: the **imaginary scalar part** of the $\mathbb{M}_-$ generator (the imaginary-time direction, $ia_0e_0$) produces the phase, while the **real vector part** $-\mathbf a$ produces a real oscillatory factor. With $a_0=0.9$, $\mathbf a=(0.4,0.2,-0.3)$, $\beta=1.2$, one finds $Z=0.752585-1.408250\,i$, of modulus $1.596732$ and phase $-1.08=-\beta a_0$. Even with $a_0=0$ the result $2\cos(\beta|\mathbf a|)$ becomes negative for some $\beta$, so the "state" is not positive; the non-Hermitian generator does not define a thermal state at all in the ordinary sense.

This is a genuine modification, but it is **not forced** by the framework: observables are defined to be Hermitian elements of $\mathbb{M}_+$, and a Hermitian $\tilde H$ is the case treated in the body of the article. The non-Hermitian case is what one gets if one allows the generator to have an $\mathbb{M}_-$ component, and it connects to two standard ideas without deriving either: **complex temperature** (continuing $\beta\to\beta+i\theta$, which turns the trace into $\mathrm{Tr}(e^{-\beta\tilde H}e^{-i\theta\tilde H})$ and exposes real-time evolution), and the **imaginary chemical potential** used in finite-density lattice studies, where an imaginary parameter again converts a sign problem into a phase. Whether an $\mathbb{M}_-$-valued generator is physically meaningful in this framework, and whether the resulting complex free energy has an interpretation beyond these known techniques, is open.

## Summary

The partition function $Z=\mathrm{Tr}(e^{-\beta\tilde H})$ has a biquaternion form, and its content is a reading of the trace rather than a new object.

For a Hermitian Hamiltonian $\tilde H=h_0e_0+i\mathbf h$ in the informational sector, the thermal operator is

$$
e^{-\beta\tilde H}=e^{-\beta h_0}\Big(\cosh(\beta|\mathbf h|)e_0-i\sinh(\beta|\mathbf h|)\hat{\mathbf h}\Big),
$$

which is itself an element of $\mathbb{M}_+$: a scalar Boltzmann weight times a boost biquaternion. The trace formula identifies the trace with twice the scalar part, so

$$
Z=2\,\mathrm{Sc}\big(e^{-\beta\tilde H}\big)=2e^{-\beta h_0}\cosh(\beta|\mathbf h|),
$$

the ordinary two-level partition function with energies $h_0\pm|\mathbf h|$. The thermal state is $\tilde\rho=\tfrac12(e_0+i\mathbf r)$ with $\mathbf r=-\tanh(\beta|\mathbf h|)\hat{\mathbf h}$, and the internal energy $U=h_0-|\mathbf h|\tanh(\beta|\mathbf h|)$ agrees with $-\partial_\beta\log Z$.

The trace keeps the scalar part of the thermal operator and discards its imaginary vector part. That discarded part is the coherence — the orientation of the thermal polarization — and it is invisible to $Z$ but visible in expectation values and KMS correlation functions. It is not the material sector: for Hermitian $\tilde H$ the thermal operator has no $\mathbb{M}_-$ component. The material sector enters through imaginary time, since $Z=\mathrm{Tr}\,\tilde U(-i\beta)$ is the trace of the evolution operator continued along the $ict$ direction, with the thermal circle of circumference $\beta$ lying along the $\mathbb{M}_-$ time. The modular Hamiltonian $K=-\log\tilde\rho=\beta\tilde H+(\log Z)e_0$ lies in $\mathbb{M}_+$, with the log-partition function as its real scalar part, in agreement with the KMS article.

The algebra does not force a modification. A genuine modification appears only if the generator is permitted an $\mathbb{M}_-$ component, in which case $Z$ can become complex, with the imaginary scalar part of the generator producing a phase and its real vector part an oscillatory modulus. That extension is possible, connects to complex temperature and imaginary chemical potential, and is not forced by the framework; it is left open.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_+$ | Hermitian subspace (informational sector): real scalar, imaginary vector |
| $\mathbb{M}_-$ | Anti-Hermitian subspace (material sector): imaginary scalar, real vector |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace (fixed points of complex conjugation) |
| $\tilde H=h_0e_0+i\mathbf h$ | Hermitian Hamiltonian (observable) |
| $\mathrm{Tr}(\tilde Q)=2\,\mathrm{Sc}(\tilde Q)$ | Trace as scalar extraction |
| $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)=2(p_0h_0+\mathbf p\cdot\mathbf h)$ | Trace formula on $\mathbb{M}_+$ |
| $Z=\mathrm{Tr}(e^{-\beta\tilde H})$ | Partition function |
| $\tilde\rho=e^{-\beta\tilde H}/Z$ | Thermal state |
| $e^{-\beta\tilde H}=e^{-\beta h_0}\big(\cosh(\beta|\mathbf h|)e_0-i\sinh(\beta|\mathbf h|)\hat{\mathbf h}\big)$ | Thermal operator |
| $\mathbf r=-\tanh(\beta|\mathbf h|)\hat{\mathbf h}$ | Bloch vector of the thermal state |
| $F=-\beta^{-1}\log Z$, $U=-\partial_\beta\log Z$ | Free energy, internal energy |
| $K=-\log\tilde\rho=\beta\tilde H+(\log Z)e_0$ | Modular Hamiltonian (in $\mathbb{M}_+$) |
| $N(\tilde Q)=\tilde Q\bar{\tilde Q}$ | Norm form |
| $\beta=1/(k_BT)$ ($\hbar=1$) | Inverse temperature |

## Further Reading

- L. D. Landau and E. M. Lifshitz, *Statistical Physics, Part 1* (Pergamon, 1980), for the partition function, the Gibbs state, and the thermodynamic potentials.
- R. K. Pathria and P. D. Beale, *Statistical Mechanics* (Butterworth–Heinemann, 2011), for the standard treatment of the canonical ensemble.
- K. Huang, *Statistical Mechanics* (Wiley, 1987), for the relation between the partition function and the spectrum.
- M. Le Bellac, *Thermal Field Theory* (Cambridge, 1996), for the imaginary-time and Matsubara formulation in which $Z$ is a Euclidean trace.
- R. Haag, N. M. Hugenholtz, and M. Winnink, "On the equilibrium states in quantum statistical mechanics," *Communications in Mathematical Physics* **5** (1967) 215–236, for the KMS characterization of thermal equilibrium.
- M. Takesaki, *Tomita's Theory of Modular Hilbert Algebras and Its Applications* (Springer, 1970), for the modular Hamiltonian $K=-\log\rho$.
- A. Roberge and N. Weiss, "Gauge theories with imaginary chemical potential and the phases of QCD," *Nuclear Physics B* **275** (1986) 734–745, for the imaginary-chemical-potential technique alluded to in the text.
- C. M. Bender and S. Boettcher, "Real spectra in non-Hermitian Hamiltonians having $\mathcal{PT}$ symmetry," *Physical Review Letters* **80** (1998) 5243–5246, for non-Hermitian generators with controlled spectra.
- Companion articles: *The KMS Condition and the Biquaternion Framework*, for the imaginary-time and modular structure; *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, for the trace formula and the action of $\mathbb{M}_+$; *The Born Rule as a Trace Formula*, for the trace pairing; *Quantum Mechanics in Biquaternionic Form*, for the thermal state as an element of the Bloch ball.
