# __Magnetic Resonance and Rabi Oscillations in Biquaternionic Form__

## Introduction

A spin-1/2 placed in a static magnetic field $B_0\hat{z}$ precesses at the Larmor frequency $\omega_0 = \gamma B_0$. If a weak transverse field oscillating at the same frequency is added, the precession is interrupted and the spin is driven coherently between its two energy eigenstates. The transition probability oscillates — the **Rabi oscillation** — with a frequency proportional to the transverse amplitude, and it reaches unity at exact resonance after a time $\pi/\omega_1$. This is the elementary mechanism of magnetic resonance, nuclear and electron spin resonance, and the qubit gate.

This article presents the driven spin-1/2 in the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ of the companion articles. The physical content is standard and is reproduced here exactly. What the article establishes is **where** the driven problem lives in the algebra and which of the framework's structures the resonance condition and the Rabi formula expose:

1. **The drive is a pair of Hermitian elements with time-dependent real coefficients.** The transverse coupling is built from $\tilde{S}_1 = \tfrac{\hbar}{2}ie_1$ and $\tilde{S}_2 = \tfrac{\hbar}{2}ie_2$, both in $\mathbb{M}_+$; the total Hamiltonian remains in $\mathbb{M}_+$ for all times. No element of the material sector enters the spin dynamics.
2. **The rotating frame is a rotor.** The transformation that removes the Larmor precession is conjugation by the unit real quaternion $\tilde{U}_R(t) = \exp(-\tfrac{\omega t}{2}e_3)\in\mathbb{H}_{\mathbb{B}}$, the same one-parameter rotor that the spin-precession exercise uses. The frame is not an approximation; it is an exact change of description.
3. **The effective Hamiltonian is static and traceless**,
   $$
   \tilde{H}_R = -\frac{\hbar}{2}\Big[(\omega_0-\omega)\,ie_3 + \omega_1\,ie_1\Big] \in \mathbb{M}_+,
   $$
   and the generalized Rabi frequency is its spectral gap, $\tilde\Omega = \sqrt{(\omega_0-\omega)^2+\omega_1^2}$.
4. **Resonance is the vanishing of the longitudinal component.** At $\omega = \omega_0$ the effective field is purely transverse, the effective Hamiltonian is $\propto ie_1$, and the spin precesses about the transverse axis, so the two eigenstates exchange with unit amplitude after a $\pi$-pulse.
5. **The transition probability is a trace pairing**, $P_\downarrow(t) = \mathrm{Tr}(\tilde{P}_-(\hat{z})\tilde{\rho}(t))$, and it equals the standard Rabi expression. The whole Rabi problem is thus a single rotor acting on an idempotent, read by the trace formula.

The notation is that of the read-list articles: $\tilde{S}_k = \tfrac{\hbar}{2}ie_k$, $\tilde{P}_\pm(\hat{\mu}) = \tfrac12(e_0\pm i\hat{\mu})$, $\tilde{\rho} = \tfrac12(e_0+i\mathbf{r})$, $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$, and the isomorphism $\Phi$ sends $e_0\mapsto I_2$, $ie_k\mapsto\sigma_k$.

The companion articles supply the pieces:
- Companion article *Spin-1/2 Quantum Mechanics in Biquaternionic Form*, for the spin operators and the two-level Hamiltonian.
- Companion article *Exercise: Spin Precession in a Magnetic Field*, for the Larmor precession and the evolution biquaternion.
- Companion article *Quantum Mechanics in Biquaternionic Form*, for the Schrödinger evolution in the algebra and the trace pairing.
- Companion article *The Berry Phase and Geometric Phases in Biquaternionic Form*, for the phase accumulated under a driven field.

## The Driven Two-Level System

### The Hamiltonian

A spin-1/2 of gyromagnetic ratio $\gamma$ in the field

$$
\mathbf{B}(t) = B_0\,\hat{z} + B_1\left(\cos\omega t\,\hat{x} - \sin\omega t\,\hat{y}\right)
$$

has the Hamiltonian $H(t) = -\boldsymbol{\mu}\cdot\mathbf{B}(t)$ with $\boldsymbol{\mu} = \gamma\mathbf{S}$. In the biquaternion algebra the spin operator is $\tilde{\mathbf{S}} = \tfrac{\hbar}{2}i e_k$ along $e_k$, and the Hamiltonian is the Hermitian element

$$
\tilde{H}(t) = -\frac{\hbar\omega_0}{2}\,ie_3
-\frac{\hbar\omega_1}{2}\left(ie_1\cos\omega t - ie_2\sin\omega t\right),
\qquad
\omega_0 = \gamma B_0, \quad \omega_1 = \gamma B_1 .
$$

Here $\omega_0$ is the Larmor frequency and $\omega_1$ is the **Rabi frequency**, the rate set by the transverse amplitude. Each of the three terms lies in $\mathbb{M}_+$: the longitudinal term is a multiple of $ie_3$ and the transverse terms are multiples of $ie_1$ and $ie_2$, each with a real time-dependent coefficient. The Hamiltonian is therefore Hermitian at every instant, and the evolution it generates preserves the norm form and the trace, as the Schrödinger article requires.

The choice of the $-\hat{y}$ sense for the second transverse component is the one that corotates with the Larmor precession in the convention of the companion exercise *Exercise: Spin Precession in a Magnetic Field*, where the Bloch vector of a spin in a static field precesses as $\mathbf{r}(t) = (\cos\omega_0 t, -\sin\omega_0 t, 0)$ for a state initially along $+\hat{x}$. The field of the equation above rotates in the same sense, so the drive remains in phase with the precession; a linearly polarised drive is the sum of this circular component and its counter-rotating partner, and the rotating-wave approximation discards the latter, as discussed below.

### The Larmor Precession as a Rotor

With $B_1 = 0$ the propagator is $\tilde{U}_0(t) = \exp(-i\tilde{H}_0t/\hbar)$ with $\tilde{H}_0 = -\tfrac{\hbar\omega_0}{2}ie_3$. Since $-i\tilde{H}_0/\hbar = \tfrac{\omega_0}{2}(i\cdot ie_3) = -\tfrac{\omega_0}{2}e_3$ and $e_3^2 = -e_0$,

$$
\tilde{U}_0(t) = \exp\!\left(-\frac{\omega_0 t}{2}e_3\right)
= \cos\frac{\omega_0 t}{2}\,e_0 - \sin\frac{\omega_0 t}{2}\,e_3
\;\in \mathbb{H}_{\mathbb{B}} .
$$

This is a unit real quaternion, a rotor; it acts on states and observables by conjugation and generates the Larmor precession. The key algebraic point is the one the Schrödinger article makes: the generator of the *physical* rotation is a real quaternion $e_3$, obtained from the Hermitian observable $ie_3$ by multiplication by the central $i$. The imaginary unit that makes the observable Hermitian is the same one that converts its exponential into a rotation rather than a boost.

### The Formal Solution

Because $\tilde{H}(t)$ at different times need not commute, the propagator is the time-ordered exponential

$$
\tilde{U}(t) = \mathcal{T}\exp\!\left(-\frac{i}{\hbar}\int_0^t \tilde{H}(t')\,dt'\right),
$$

which in the algebra is a product of unitaries in the limit of infinitesimal steps, $\tilde{U}(t) = \lim_{N\to\infty}\prod_{k=0}^{N-1}\exp(-\tfrac{i}{\hbar}\tilde{H}(t_k)\Delta t)$. Each factor is a unitary element of $\mathbb{B}$; the product is unitary too, and lies in the group generated by $\mathbb{M}_+$ together with the central $i$, which is the $U(2)$ of the informational sector. The rotating frame below turns this time-ordered product into a single exponential.

## The Rotating Frame

### The Rotor Transformation

Define the rotating-frame state and observable by

$$
\psi_R(t) = \tilde{U}_R(t)^\dagger\,\psi(t),
\qquad
\tilde{U}_R(t) = \exp\!\left(-\frac{\omega t}{2}e_3\right)
= \cos\frac{\omega t}{2}\,e_0 - \sin\frac{\omega t}{2}\,e_3 .
$$

The rotor $\tilde{U}_R$ is the Larmor rotor taken at the drive frequency $\omega$ rather than at $\omega_0$; it rotates the reference frame at the drive frequency. The Schrödinger equation $i\hbar\dot\psi = \tilde{H}\psi$ becomes $i\hbar\dot\psi_R = \tilde{H}_R\psi_R$ with

$$
\tilde{H}_R = \tilde{U}_R^\dagger\,\tilde{H}\,\tilde{U}_R - i\hbar\,\tilde{U}_R^\dagger\,\partial_t\tilde{U}_R .
$$

The second term is the "fictitious" term produced by the time dependence of the frame; it is what makes the transformation a change of description rather than a mere relabelling.

### The Effective Hamiltonian

The three terms of $\tilde{H}$ transform as follows. The longitudinal term is proportional to $ie_3$, which commutes with the rotor, so it is unchanged. The transverse combination is rotated into a fixed direction: using the conjugation rule for a rotor about $e_3$, one finds

$$
\tilde{U}_R^\dagger\left(ie_1\cos\omega t - ie_2\sin\omega t\right)\tilde{U}_R = ie_1 ,
$$

so the drive becomes a static transverse field. The fictitious term computes to $-i\hbar\tilde{U}_R^\dagger\partial_t\tilde{U}_R = +\tfrac{\hbar\omega}{2}ie_3$. Adding the three contributions,

$$
\boxed{\;\tilde{H}_R = -\frac{\hbar}{2}\Big[(\omega_0-\omega)\,ie_3 + \omega_1\,ie_1\Big] \in \mathbb{M}_+ \;}
$$

which is time independent. Writing $\Delta = \omega_0-\omega$ for the **detuning**, the effective Hamiltonian is a fixed Hermitian element of the informational sector,

$$
\tilde{H}_R = -\frac{\hbar}{2}\,i\left(\omega_1 e_1 + \Delta e_3\right)
= -\frac{\hbar\tilde\Omega}{2}\,i\,\hat{n}_R,
\qquad
\hat{n}_R = \frac{\omega_1 e_1 + \Delta e_3}{\tilde\Omega},
$$

with

$$
\tilde\Omega = \sqrt{\omega_1^2 + \Delta^2}
$$

the **generalized Rabi frequency**. Every quantity in the driven problem has now been reduced to a single real vector $\hat{n}_R$ on the unit sphere and a single frequency $\tilde\Omega$: the effective Hamiltonian is a spin observable along $\hat{n}_R$ with coupling $\hbar\tilde\Omega/2$, exactly the structure of a static spin in a field.

### Resonance

Resonance is the condition $\omega = \omega_0$, i.e. $\Delta = 0$. Then

$$
\tilde{H}_R\big|_{\Delta=0} = -\frac{\hbar\omega_1}{2}\,ie_1,
$$

a purely transverse effective Hamiltonian: the longitudinal component of the effective field vanishes, $\hat{n}_R = e_1$, and the effective Larmor precession is about the $x$-axis at the Rabi frequency $\omega_1$. This is the algebraic statement of resonance: the rotating frame corotates with the drive exactly, so the longitudinal part of the field, $B_0-\omega/\gamma$, is cancelled. Off resonance the residual longitudinal field tilts $\hat{n}_R$ away from the equator, the effective precession cone opens, and the maximum transition probability is reduced.

## Rabi Oscillations

### The Transition Probability

Prepare the spin in the upper eigenstate of the static field, $\tilde{\rho}(0) = \tilde{P}_+(\hat{z})$, and ask for the probability of finding it in the lower eigenstate $\tilde{P}_-(\hat{z})$ at time $t$. In the rotating frame the state evolves by the static Hamiltonian, so

$$
\tilde{\rho}_R(t) = \tilde{R}(t)\,\tilde{\rho}(0)\,\tilde{R}(t)^\dagger,
\qquad
\tilde{R}(t) = \exp\!\left(-\frac{i\tilde{H}_R t}{\hbar}\right).
$$

Since $-i\tilde{H}_R/\hbar = -\tfrac12(\omega_1 e_1 + \Delta e_3)$ and the square of the generator is $-\tfrac14(\omega_1^2+\Delta^2)e_0 = -\tfrac14\tilde\Omega^2 e_0$, the exponential is a rotation about $\hat{n}_R$:

$$
\tilde{R}(t) = \exp\!\left(-\frac{\tilde\Omega t}{2}\,\hat{n}_R\right)
= \cos\frac{\tilde\Omega t}{2}\,e_0 - \sin\frac{\tilde\Omega t}{2}\;\frac{\omega_1 e_1 + \Delta e_3}{\tilde\Omega} .
$$

The exponent is a real quaternion, so $\tilde{R}\in\mathbb{H}_{\mathbb{B}}$ is a rotor and the rotation it generates is a spatial rotation of the Bloch vector about $\hat{n}_R$ at the rate $\tilde\Omega$. The state in the laboratory frame is $\tilde{\rho}(t) = \tilde{U}_R(t)\tilde{\rho}_R(t)\tilde{U}_R(t)^\dagger$, and the transition probability is the trace pairing with the fixed idempotent $\tilde{P}_-(\hat{z})$. Restoring the frame rotor and evaluating the trace gives the standard result

$$
P_{\downarrow}(t) = \mathrm{Tr}\!\left(\tilde{P}_-(\hat{z})\,\tilde{\rho}(t)\right)
= \frac{\omega_1^2}{\omega_1^2+\Delta^2}\,\sin^2\!\left(\frac{\sqrt{\omega_1^2+\Delta^2}}{2}\,t\right).
$$

This is the **Rabi formula**. On resonance it simplifies to

$$
P_\downarrow(t)\big|_{\omega=\omega_0} = \sin^2\!\left(\frac{\omega_1 t}{2}\right),
$$

the elementary sinusoidal oscillation between the two levels at the Rabi frequency.

The derivation contains one geometric fact worth isolating. In the rotating frame the evolution is a rotation of the Bloch vector about the fixed axis $\hat{n}_R$; the laboratory measurement axis $\hat{z}$ is itself carried by the rotor $\tilde{U}_R(t)$ in the laboratory frame, and the overlap of the two rotations is what produces the factor $\omega_1^2/\tilde\Omega^2$ and the argument $\tilde\Omega t/2$. Both factors are the standard ones; the biquaternion setting writes each rotation as a rotor and the probability as a trace.

### The Rotating-Wave Approximation

The circularly polarised drive used above is a single rotating component. A practical magnetic-resonance experiment uses a **linearly** polarised field,

$$
\mathbf{B}_1(t) = 2B_1\cos\omega t\;\hat{x},
$$

which is the sum of the corotating component $B_1(\cos\omega t\,\hat{x}-\sin\omega t\,\hat{y})$ considered above and the counter-rotating component $B_1(\cos\omega t\,\hat{x}+\sin\omega t\,\hat{y})$. The corotating component is static in the rotating frame; the counter-rotating component rotates at $2\omega$ and contributes rapidly oscillating terms. The **rotating-wave approximation** (RWA) drops the counter-rotating terms, and it is accurate when $\omega_1\ll\omega_0$; the neglected terms produce the Bloch–Siegert shift, of order $\omega_1^2/\omega_0$. In the biquaternion algebra the split is the decomposition of the linear drive into the two circular components $ie_1\cos\omega t\mp ie_2\sin\omega t$, each a Hermitian combination; the RWA keeps the component that corotates with the Larmor rotor $\tilde{U}_0$ and discards its conjugate. The approximation is thus a statement about which rotor the drive is in phase with, and it has no special algebraic status.

### $\pi$ and $\pi/2$ Pulses

Two pulse durations have a distinguished role. At resonance, $\tilde\Omega = \omega_1$, and

$$
t = \frac{\pi}{\omega_1}:\quad P_\downarrow = \sin^2\frac{\pi}{2} = 1,
\qquad
t = \frac{\pi}{2\omega_1}:\quad P_\downarrow = \sin^2\frac{\pi}{4} = \frac12 .
$$

The first is a $\pi$-pulse: it inverts the spin, carrying $\tilde{P}_+(\hat{z})$ to $\tilde{P}_-(\hat{z})$ with unit probability. The second is a $\pi/2$-pulse: it prepares the equal coherent superposition. In the algebra these are the statements that the rotor $\tilde{R}(\pi/\omega_1) = -e_1$, a $\pi$-rotation about the effective axis $e_1$, exchanges the two idempotents, and that $\tilde{R}(\pi/2\omega_1)$ carries the pole of the Bloch sphere to its equator. A $\pi/2$-pulse followed by a free Larmor evolution and a second $\pi/2$-pulse is the standard Ramsey interferometer; its fringes are governed by the phase accumulated in the interval, in which a dynamical part and a geometric part can be separated.

## The Bloch Picture

The state at any time can be written $\tilde{\rho}(t) = \tfrac12(e_0 + i\mathbf{r}(t))$, with $\mathbf{r}(t)$ the Bloch vector. Substituting into the Schrödinger equation and using the commutator identity $[\tilde{H},\tilde{K}] = -2(\mathbf{h}\times\mathbf{k})$ of the companion article *Quantum Mechanics in Biquaternionic Form*, the Bloch vector obeys

$$
\dot{\mathbf{r}} = \boldsymbol{\omega}_{\mathrm{eff}}\times\mathbf{r},
\qquad
\boldsymbol{\omega}_{\mathrm{eff}} = (-\omega_1, 0, -\Delta),
$$

for the effective Hamiltonian $\tilde{H}_R = -\tfrac{\hbar}{2}i(\omega_1 e_1+\Delta e_3)$. This is a rigid rotation of $\mathbf{r}$ about the fixed axis $-\hat{n}_R$ at the rate $\tilde\Omega$. Three cases are worth separating.

- **Resonance** ($\Delta = 0$): the rotation axis is the $x$-axis, the Bloch vector rotates in the $yz$-plane, and a spin initially along $+z$ passes through the equator and reaches $-z$ after a half-period — the $\pi$-pulse.
- **Large detuning** ($|\Delta|\gg\omega_1$): the axis is close to $-z$, the rotation cone is narrow, and the spin remains near its initial pole, executing small oscillations of amplitude $\sim\omega_1/|\Delta|$ — the dispersive regime.
- **Exact antiresonance** is not a special point for a circular drive; it is special only for a linear drive, where the counter-rotating component becomes corotating. This is the algebraic content of the distinction between the two polarisations.

The Bloch picture is the material of the companion article *Quantum Mechanics in Biquaternionic Form*; here it is used only to display the effective rotation, and the reader is referred to that article for the derivation of the Bloch equation from the trace pairing.

## The Biquaternion Reading

**Standard physics, transcribed.** The Larmor precession, the rotating-frame transformation, the effective Hamiltonian, the generalized Rabi frequency, the Rabi formula, the RWA and the $\pi$ and $\pi/2$ pulses are all standard. The article claims no deviation from the standard predictions.

**What the algebra organises.**

- **A single sector.** The drive, the static field and the effective field are all Hermitian elements of $\mathbb{M}_+$, and the whole problem is the conjugation of a state in that sector by a product of unitaries. The material sector does not appear, except in the frame rotor $\tilde{U}_R$, which is a real quaternion in $\mathbb{H}_{\mathbb{B}}$.
- **The rotor as the natural variable.** The rotating frame is not an ad hoc complex exponential; it is conjugation by the unit real quaternion $\exp(-\tfrac{\omega t}{2}e_3)$, the same rotor that carries the Larmor precession. The effective Hamiltonian is the transformed observable, and the resonance condition is the vanishing of its longitudinal component.
- **The spectral gap as the Rabi frequency.** The generalized Rabi frequency is the difference of the two eigenvalues of the effective Hamiltonian, $\pm\hbar\tilde\Omega/2$, so it is a spectral quantity of a Hermitian element of $\mathbb{M}_+$. The maximum transition amplitude $\omega_1^2/(\omega_1^2+\Delta^2)$ is the square of the transverse fraction of the effective field, i.e. the geometric tilt of $\hat{n}_R$ from the equator.
- **No privileged counter-rotating terms.** Because the drive is written as a Hermitian element with an explicit time dependence, the RWA is exposed as a physical approximation about which rotor the drive tracks, not as an algebraic necessity.

**What the algebra does not supply.** The Rabi frequency $\omega_1 = \gamma B_1$ and the Larmor frequency $\omega_0 = \gamma B_0$ contain the gyromagnetic ratio $\gamma$ and the field amplitudes; these are external data, like the mass and the action in the other articles of the series. The algebra also does not supply the time $t$ or the drive frequency $\omega$; the rotating frame is defined by inserting them. Finally, dissipation and relaxation — the Bloch $T_1$ and $T_2$ times — lie outside the Hamiltonian evolution entirely and are not addressed by the framework, which is unitary.

## Open Questions

1. **Bloch–Siegert and the counter-rotating sector.** The counter-rotating component has the opposite helicity, which in the algebra is the opposite sign of the generator $ie_2$. Is there a natural way to separate the two helicities in the algebra, in the way the chirality projectors separate the two Weyl components of a Dirac spinor? If so, the RWA might acquire an algebraic character it does not have here.

2. **Dissipation.** The framework is unitary, and the Rabi problem is closed. The open-system version — the Bloch equations with relaxation — requires a density operator that is not merely conjugated by a rotor. Whether the informational sector admits a completely positive map with a natural algebraic form is left open by the companion article *The Measurement Problem in Algebraic Form*.

3. **The rotating frame and the local complex structure.** The rotor $\exp(-\tfrac{\omega t}{2}e_3)$ uses the real unit $e_3$, not the central imaginary. The central imaginary of the Schrödinger equation is fixed, but the series makes the complex structure local, set by the medium. Whether the frame rotor should be regarded as a local object, and how it would then differ from a global one, is unresolved.

4. **Dressed states.** The eigenstates of $\tilde{H}_R$ are the dressed states of the driven two-level system, and the Mollow triplet in resonance fluorescence is their spectrum. Is there an algebraic statement of the dressed-state structure — for instance a spectral decomposition of $\tilde{H}_R$ that makes the Autler–Townes splitting immediate?

5. **Empirical content.** As elsewhere, the reformulation reproduces the standard predictions; whether its additional structure implies a measurable deviation is open.

## Summary

A spin-1/2 driven by $\mathbf{B}(t) = B_0\hat{z} + B_1(\cos\omega t\,\hat{x}-\sin\omega t\,\hat{y})$ has the biquaternion Hamiltonian

$$
\tilde{H}(t) = -\frac{\hbar\omega_0}{2}ie_3 - \frac{\hbar\omega_1}{2}\left(ie_1\cos\omega t - ie_2\sin\omega t\right) \in \mathbb{M}_+,
$$

with $\omega_0 = \gamma B_0$ and $\omega_1 = \gamma B_1$. The transformation to the frame rotating with the drive is conjugation by the unit real quaternion $\tilde{U}_R(t) = \exp(-\tfrac{\omega t}{2}e_3)$, and it produces the static effective Hamiltonian

$$
\tilde{H}_R = \tilde{U}_R^\dagger\tilde{H}\tilde{U}_R - i\hbar\tilde{U}_R^\dagger\partial_t\tilde{U}_R
= -\frac{\hbar}{2}\Big[(\omega_0-\omega)ie_3 + \omega_1 ie_1\Big].
$$

The effective Hamiltonian is a spin observable along the unit vector $\hat{n}_R = (\omega_1 e_1 + \Delta e_3)/\tilde\Omega$, with $\Delta = \omega_0-\omega$ the detuning and $\tilde\Omega = \sqrt{\omega_1^2+\Delta^2}$ the generalized Rabi frequency equal to its spectral gap. Resonance $\omega = \omega_0$ makes $\tilde{H}_R = -\tfrac{\hbar\omega_1}{2}ie_1$ purely transverse, and then the spin precesses about the equator.

The transition probability is the trace pairing $P_\downarrow(t) = \mathrm{Tr}(\tilde{P}_-(\hat{z})\tilde{\rho}(t))$, and it equals the Rabi formula

$$
P_\downarrow(t) = \frac{\omega_1^2}{\omega_1^2+\Delta^2}\,\sin^2\!\left(\frac{\tilde\Omega t}{2}\right),
$$

which reduces to $\sin^2(\omega_1t/2)$ on resonance. The $\pi$-pulse $t = \pi/\omega_1$ inverts the spin and the $\pi/2$-pulse $t = \pi/(2\omega_1)$ prepares the equal superposition. The Bloch vector obeys $\dot{\mathbf{r}} = \boldsymbol{\omega}_{\mathrm{eff}}\times\mathbf{r}$ with $\boldsymbol{\omega}_{\mathrm{eff}} = (-\omega_1,0,-\Delta)$, a rigid rotation about the fixed effective axis. The rotating-wave approximation is the discarding of the counter-rotating helicity of a linear drive; it is a statement about which rotor the drive tracks, not an algebraic identity.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Central scalar imaginary |
| $\mathbb{M}_+$ | Hermitian (informational) subspace; home of all Hamiltonians here |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace; home of the frame rotor |
| $\tilde{S}_k = \tfrac{\hbar}{2}ie_k$ | Spin observable along $\hat{k}$ |
| $\mathbf{B}(t) = B_0\hat{z}+B_1(\cos\omega t\,\hat{x}-\sin\omega t\,\hat{y})$ | Static field plus corotating drive |
| $\omega_0 = \gamma B_0$ | Larmor frequency |
| $\omega_1 = \gamma B_1$ | Rabi frequency |
| $\Delta = \omega_0-\omega$ | Detuning |
| $\tilde{H}(t) = -\tfrac{\hbar\omega_0}{2}ie_3-\tfrac{\hbar\omega_1}{2}(ie_1\cos\omega t-ie_2\sin\omega t)$ | Laboratory Hamiltonian |
| $\tilde{U}_R(t) = \exp(-\tfrac{\omega t}{2}e_3)$ | Rotating-frame rotor |
| $\tilde{H}_R = -\tfrac{\hbar}{2}[(\omega_0-\omega)ie_3+\omega_1ie_1]$ | Effective Hamiltonian in the rotating frame |
| $\tilde\Omega = \sqrt{\omega_1^2+\Delta^2}$ | Generalized Rabi frequency (spectral gap) |
| $\hat{n}_R = (\omega_1e_1+\Delta e_3)/\tilde\Omega$ | Effective rotation axis |
| $P_\downarrow(t) = \tfrac{\omega_1^2}{\omega_1^2+\Delta^2}\sin^2(\tilde\Omega t/2)$ | Rabi transition probability |
| $\pi/\omega_1$, $\pi/(2\omega_1)$ | $\pi$-pulse, $\pi/2$-pulse durations |
| $\dot{\mathbf{r}} = \boldsymbol{\omega}_{\mathrm{eff}}\times\mathbf{r}$ | Bloch equation in the rotating frame |

## Further Reading

- I. I. Rabi, "On the Process of Space Quantization," *Physical Review* **49** (1936) 324–328, for the original resonance method.
- I. I. Rabi, S. Millman, P. Kusch, and J. R. Zacharias, "The Molecular Beam Resonance Method for Measuring Nuclear Magnetic Moments," *Physical Review* **55** (1939) 526–535, for the molecular-beam resonance experiment.
- F. Bloch, "Nuclear Induction," *Physical Review* **70** (1946) 460–474, for the Bloch equations and relaxation.
- E. M. Purcell, H. C. Torrey, and R. V. Pound, "Resonance Absorption by Nuclear Magnetic Moments in a Solid," *Physical Review* **69** (1946) 37–38, for nuclear magnetic resonance in condensed matter.
- L. Allen and J. H. Eberly, *Optical Resonance and Two-Level Atoms* (Wiley, 1975), for the dressed states, the Rabi formula, and the rotating-wave approximation.
- Claude Cohen-Tannoudji, Jacques Dupont-Roc, and Gilbert Grynberg, *Atom–Photon Interactions* (Wiley, 1992), for the dressed-state and resonance-fluorescence treatment.
- L. D. Landau and E. M. Lifshitz, *Quantum Mechanics: Non-Relativistic Theory* (Pergamon, 1977), for the two-level system in a resonant field.
- J. J. Sakurai and Jim Napolitano, *Modern Quantum Mechanics* (Pearson, 2017), for the spin-1/2 treatment of magnetic resonance and the rotating frame.
