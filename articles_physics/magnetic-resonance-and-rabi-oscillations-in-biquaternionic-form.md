# __Magnetic Resonance and Rabi Oscillations in Biquaternionic Form__

## Introduction

A spin-1/2 placed in a static magnetic field $B_0\vec u_z$ precesses at the Larmor frequency $\omega_0 = \gamma B_0$. If a weak transverse field oscillating at the same frequency is added, the precession is interrupted and the spin is driven coherently between its two energy eigenstates. The transition probability oscillates — the **Rabi oscillation** — with a frequency proportional to the transverse amplitude, and it reaches unity at exact resonance after a time $\pi/\omega_1$. This is the elementary mechanism of magnetic resonance, nuclear and electron spin resonance, and the qubit gate.

This article presents the driven spin-1/2 in the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ of the companion articles. The physical content is standard and is reproduced here exactly. What the article establishes is **where** the driven problem lives in the algebra and which of the framework's structures the resonance condition and the Rabi formula expose:

1. **The drive is a pair of Hermitian elements with time-dependent real coefficients.** The transverse coupling is built from $\tilde{S}_{\Psi,1} =\frac{m\,c}{2\,k_m}i\vec e_x$ and $\tilde{S}_{\Psi,2} =\frac{m\,c}{2\,k_m}i\vec e_y$, both in $\mathbb{B}_{\Psi}$; the total Hamiltonian remains in $\mathbb{B}_{\Psi}$ for all times. No element of the material sector enters the spin dynamics.
2. **The rotating frame is a rotor.** The transformation that removes the Larmor precession is conjugation by the unit real quaternion $\tilde u_{\mathrm r}(r'_t) = \exp(-\tfrac{\omega r'_t}{2\,c}\vec e_z)\in\mathbb{B}_{H}$, the same one-parameter rotor that the spin-precession exercise uses. The frame is not an approximation; it is an exact change of description.
3. **The effective Hamiltonian is static and traceless**,
   $$
   \tilde{R}_{\Psi,R} = -\frac{m\,c}{2\,k_m}\Big[(\omega_0-\omega)\,i\vec e_z + \omega_1\,i\vec e_x\Big] \in  \mathbb{B}_{\Psi},
   $$
   and the generalized Rabi frequency is its spectral gap, $\Omega = \sqrt{(\omega_0-\omega)^2+\omega_1^2}$.
4. **Resonance is the vanishing of the longitudinal component.** At $\omega = \omega_0$ the effective field is purely transverse, the effective Hamiltonian is $\propto i\vec e_x$, and the spin precesses about the transverse axis, so the two eigenstates exchange with unit amplitude after a $\pi$-pulse.
5. **The transition probability is the normalised Hermitian form, read through the trace**, $P_\downarrow(r'_t) = \mathrm{Tr}(\tilde\Pi_2(\vec u_z)\tilde{Ϛ}_{\Psi}(r'_t)^{*})$, and it equals the standard Rabi expression. The whole Rabi problem is thus a single rotor acting on an idempotent, read by the trace formula.

The notation is that of the read-list articles: $\tilde{S}_{\Psi,k} =\frac{m\,c}{2\,k_m}i\vec e_k$, $\tilde\Pi_{1,2}(\vec u) = \tfrac12(e_t\pm i\vec u)$, $\tilde{Ϛ}_{\Psi} = \tfrac12(e_t+i\vec r)$, $\mathrm{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$, and the isomorphism $\mathsf{M}_2$ sends $e_t\mapsto I_2$, $i\vec e_k\mapsto\sigma_k$.

The companion articles supply the pieces:
- Companion article *Spin-1/2 Quantum Physics in Biquaternionic Form*, for the spin operators and the two-level Hamiltonian.
- Companion article *Exercise: Spin Precession in a Magnetic Field*, for the Larmor precession and the evolution biquaternion.
- Companion article *Quantum Physics in Biquaternionic Form*, for the Schrödinger evolution in the algebra and the plain form.
- Companion article *The Berry Phase and Geometric Phases in Biquaternionic Form*, for the phase accumulated under a driven field.

## The Driven Two-Level System

### The Hamiltonian

A spin-1/2 of gyromagnetic ratio $\gamma$ in the field

$$
\vec B(r'_t) = B_0\,\vec u_z + B_1\left(\cos(\omega r'_t/c)\,\vec u_x - \sin(\omega r'_t/c)\,\vec u_y\right)
$$

has the Hamiltonian $H(r'_t) = -\vec\mu\cdot\vec B(r'_t)$ with $\vec\mu = \gamma\vec S$. In the biquaternion algebra the spin operator is $\tilde S_{\Psi} =\frac{m\,c}{2\,k_m}i \vec e_k$ along $\vec e_k$, and the Hamiltonian is the Hermitian element

$$
\tilde R_\Psi(r'_t) = -\frac{m\,c\,\omega_{0}}{2\,k_m}\,i\vec e_z
-\frac{m\,c\,\omega_{1}}{2\,k_m}\left(i\vec e_x\cos(\omega r'_t/c) - i\vec e_y\sin(\omega r'_t/c)\right),
\qquad
\omega_0 = \gamma B_0, \quad \omega_1 = \gamma B_1 .
$$

Here $\omega_0$ is the Larmor frequency and $\omega_1$ is the **Rabi frequency**, the rate set by the transverse amplitude. Each of the three terms lies in $\mathbb{B}_{\Psi}$: the longitudinal term is a multiple of $i\vec e_z$ and the transverse terms are multiples of $i\vec e_x$ and $i\vec e_y$, each with a real time-dependent coefficient. The Hamiltonian is therefore Hermitian at every instant, and the evolution it generates preserves the biquaternion norm and the trace, as the Schrödinger article requires.

The choice of the $-\vec u_y$ sense for the second transverse component is the one that corotates with the Larmor precession in the convention of the companion exercise *Exercise: Spin Precession in a Magnetic Field*, where the Bloch vector of a spin in a static field precesses as $\vec r(r'_t) = (\cos(\omega_0 r'_t/c), -\sin(\omega_0 r'_t/c), 0)$ for a state initially along $+\vec u_x$. The field of the equation above rotates in the same sense, so the drive remains in phase with the precession; a linearly polarised drive is the sum of this circular component and its counter-rotating partner, and the rotating-wave approximation discards the latter, as discussed below.

### The Larmor Precession as a Rotor

With $B_1 = 0$ the propagator is $\tilde u_0(r'_t) = \exp(-\frac{k_m\,i\,H_{0}\,r'_{t}}{m\,c^{2}})$ with $\tilde{R}_{\Psi,0} = -\frac{m\,c\,\omega_{0}}{2\,k_m}i\vec e_z$. Since $-i H_{0}/\hbar = \tfrac{\omega_0}{2}(i\cdot i\vec e_z) = -\tfrac{\omega_0}{2}\vec e_z$ and $\vec e_z^2 = -e_t$,

$$
\tilde u_0(r'_t) = \exp\!\left(-\frac{\omega_0 r'_t}{2\,c}\vec e_z\right)
= \cos\frac{\omega_0 r'_t}{2\,c}\,e_t - \sin\frac{\omega_0 r'_t}{2\,c}\,\vec e_z
\;\in \mathbb{B}_{H} .
$$

This is a unit real quaternion, a rotor; it acts on states and observables by conjugation and generates the Larmor precession. The key algebraic point is the one the Schrödinger article makes: the generator of the *physical* rotation is a real quaternion $\vec e_z$, obtained from the Hermitian observable $i\vec e_z$ by multiplication by the central $i$. The imaginary unit that makes the observable Hermitian is the same one that converts its exponential into a rotation rather than a boost.

### The Formal Solution

Because $\tilde R_\Psi(r'_t)$ at different times need not commute, the propagator is the time-ordered exponential

$$
\tilde{U}(r'_t) = \mathcal{T}\exp\!\left(-\frac{k_m\,i}{m\,c}\int_0^{r'_{t}}  \tilde R_\Psi(\tau)\,d\tau\right),
$$

which in the algebra is a product of unitaries in the limit of infinitesimal steps, $\tilde Q(r'_t) = \lim_{N\to\infty}\prod_{k=0}^{N-1}\exp(-\frac{k_m\,i}{m\,c}\tilde R_\Psi(r'_{t,k})\Delta r'_t)$. Each factor is a $*$-unitary element of $\mathbb{B}$; the product is $*$-unitary too, and lies in the group generated by $\mathbb{B}_{\Psi}$ together with the central $i$, which is the $\mathrm{U}(2)$ of the informational sector. The rotating frame below turns this time-ordered product into a single exponential.

## The Rotating Frame

### The Rotor Transformation

Define the rotating-frame state and observable by

$$
\tilde{Ξ}_{\mathrm{sp},R}(r'_t) = \tilde u_{\mathrm r}(r'_t)^{*}\,\tilde{Ξ}_{\mathrm{sp}}(r'_t),
\qquad
\tilde u_{\mathrm r}(r'_t) = \exp\!\left(-\frac{\omega r'_t}{2\,c}\vec e_z\right)
= \cos\frac{\omega r'_t}{2\,c}\,e_t - \sin\frac{\omega r'_t}{2\,c}\,\vec e_z .
$$

The rotor $\tilde u_{\mathrm r}$ is the Larmor rotor taken at the drive frequency $\omega$ rather than at $\omega_0$; it rotates the reference frame at the drive frequency. The Schrödinger equation $\frac{m\,c\,i\,d\,\tilde{Ξ}_{\mathrm{sp}}}{k_m\,dr'_{t}}= \tilde R_\Psi\tilde{Ξ}_{\mathrm{sp}}$ becomes $\frac{m\,c\,i\,d\,\tilde{Ξ}_{\mathrm{sp},R}}{k_m\,dr'_{t}}= \tilde{R}_{\Psi,R}\tilde{Ξ}_{\mathrm{sp},R}$ with

$$
\tilde{R}_{\Psi,R} = \tilde u_{\mathrm r}^{*}\,\tilde R_\Psi\,\tilde u_{\mathrm r} -\frac{m\,c\,i\,\tilde{u}_{\mathrm r}^{*}}{k_m}\partial/\partial r'_t\tilde u_{\mathrm r} .
$$

The second term is the "fictitious" term produced by the time dependence of the frame; it is what makes the transformation a change of description rather than a mere relabelling.

### The Effective Hamiltonian

The three terms of $\tilde R_\Psi$ transform as follows. The longitudinal term is proportional to $i\vec e_z$, which commutes with the rotor, so it is unchanged. The transverse combination is rotated into a fixed direction: using the conjugation rule for a rotor about $\vec e_z$, one finds

$$
\tilde u_{\mathrm r}^{*}\left(i\vec e_x\cos(\omega r'_t/c) - i\vec e_y\sin(\omega r'_t/c)\right)\tilde u_{\mathrm r} = i\vec e_x ,
$$

so the drive becomes a static transverse field. The fictitious term computes to $-\frac{m\,c\,i\,\tilde{u}_{\mathrm r}^{*}}{k_m}\partial/\partial r'_t\tilde u_{\mathrm r} = +\frac{m\,c\,\omega}{2\,k_m}i\vec e_z$. Adding the three contributions,

$$
\boxed{\;\tilde{R}_{\Psi,R} = -\frac{m\,c}{2\,k_m}\Big[(\omega_0-\omega)\,i\vec e_z + \omega_1\,i\vec e_x\Big] \in  \mathbb{B}_{\Psi} \;}
$$

which is time independent. Writing $\Delta = \omega_0-\omega$ for the **detuning**, the effective Hamiltonian is a fixed Hermitian element of the informational sector,

$$
\tilde{R}_{\Psi,R} = -\frac{m\,c}{2\,k_m}\,i\left(\omega_1 \vec e_x + \Delta \vec e_z\right)
= -\frac{m\,c\,\Omega}{2\,k_m}\,i\,\vec u_R,
\qquad
\vec u_R = \frac{\omega_1 \vec e_x + \Delta \vec e_z}{\Omega},
$$

with

$$
\boxed{\;\Omega = \sqrt{\omega_1^2 + \Delta^2}\;}
$$

the **generalized Rabi frequency**. Every quantity in the driven problem has now been reduced to a single real vector $\vec u_R$ on the unit sphere and a single frequency $\Omega$: the effective Hamiltonian is a spin observable along $\vec u_R$ with coupling $\frac{m\,c\,\Omega}{2\,k_m}$, exactly the structure of a static spin in a field.

### Resonance

Resonance is the condition $\omega = \omega_0$, i.e. $\Delta = 0$. Then

$$
\tilde{R}_{\Psi,R}\big|_{\Delta=0} = -\frac{m\,c\,\omega_{1}}{2\,k_m}\,i\vec e_x,
$$

a purely transverse effective Hamiltonian: the longitudinal component of the effective field vanishes, $\vec u_R = \vec e_x$, and the effective Larmor precession is about the $x$-axis at the Rabi frequency $\omega_1$. This is the algebraic statement of resonance: the rotating frame corotates with the drive exactly, so the longitudinal part of the field, $B_0-\omega/\gamma$, is cancelled. Off resonance the residual longitudinal field tilts $\vec u_R$ away from the equator, the effective precession cone opens, and the maximum transition probability is reduced.

## Rabi Oscillations

### The Transition Probability

Prepare the spin in the upper eigenstate of the static field, $\tilde{Ϛ}_{\Psi}(0) = \tilde\Pi_1(\vec u_z)$, and ask for the probability of finding it in the lower eigenstate $\tilde\Pi_2(\vec u_z)$ at time $r'_t$. In the rotating frame the state evolves by the static Hamiltonian, so

$$
\tilde{Ϛ}_{\Psi,R}(r'_t) = \tilde u_H(r'_t)\,\tilde{Ϛ}_{\Psi}(0)\,\tilde u_H(r'_t)^{*},
\qquad
\tilde u_H(r'_t) = \exp\!\left(-\frac{k_m\,i\,\tilde{R}_{\Psi,R}\,r'_{t}}{m\,c^{2}}\right).
$$

Since $-\frac{k_m\,i\,H_{R}}{m\,c}= -\tfrac12(\omega_1 \vec e_x + \Delta \vec e_z)$ and the square of the generator is $-\tfrac14(\omega_1^2+\Delta^2)e_t = -\tfrac14\Omega^2 e_t$, the exponential is a rotation about $\vec u_R$:

$$
\tilde u_H(r'_t) = \exp\!\left(-\frac{\Omega r'_t}{2}\,\vec u_R\right)
= \cos\frac{\Omega r'_t}{2}\,e_t - \sin\frac{\Omega r'_t}{2}\;\frac{\omega_1 \vec e_x + \Delta \vec e_z}{\Omega} .
$$

The exponent is a real quaternion, so $\tilde u_H\in\mathbb{B}_{H}$ is a rotor and the rotation it generates is a spatial rotation of the Bloch vector about $\vec u_R$ at the rate $\Omega$. The state in the laboratory frame is $\tilde{Ϛ}_{\Psi}(r'_t) = \tilde u_{\mathrm r}(r'_t)\tilde{Ϛ}_{\Psi,R}(r'_t)\tilde u_{\mathrm r}(r'_t)^{*}$, and the transition probability is the normalised Hermitian form, read through the trace with the fixed idempotent $\tilde\Pi_2(\vec u_z)$. Restoring the frame rotor and evaluating the trace gives the standard result

$$
\boxed{\;P_{\downarrow}(r'_t) = \mathrm{Tr}\!\left(\tilde\Pi_2(\vec u_z)\,\tilde{Ϛ}_{\Psi}(r'_t)\right)
= \frac{\omega_1^2}{\omega_1^2+\Delta^2}\,\sin^2\!\left(\frac{\sqrt{\omega_1^2+\Delta^2}}{2}\,r'_t\right)\;}.
$$

This is the **Rabi formula**. On resonance it simplifies to

$$
P_\downarrow(r'_t)\big|_{\omega=\omega_0} = \sin^2\!\left(\frac{\omega_1 r'_t}{2\,c}\right),
$$

the elementary sinusoidal oscillation between the two levels at the Rabi frequency.

The derivation contains one geometric fact worth isolating. In the rotating frame the evolution is a rotation of the Bloch vector about the fixed axis $\vec u_R$; the laboratory measurement axis $\vec u_z$ is itself carried by the rotor $\tilde u_{\mathrm r}(r'_t)$ in the laboratory frame, and the overlap of the two rotations is what produces the factor $\omega_1^2/\Omega^2$ and the argument $\Omega r'_t/2$. Both factors are the standard ones; the biquaternion setting writes each rotation as a rotor and the probability as a trace.

### The Rotating-Wave Approximation

The circularly polarised drive used above is a single rotating component. A practical magnetic-resonance experiment uses a **linearly** polarised field,

$$
\vec B_1(r'_t) = 2B_1\cos(\omega r'_t/c)\;\vec u_x,
$$

which is the sum of the corotating component $B_1(\cos(\omega r'_t/c)\,\vec u_x-\sin(\omega r'_t/c)\,\vec u_y)$ considered above and the counter-rotating component $B_1(\cos(\omega r'_t/c)\,\vec u_x+\sin(\omega r'_t/c)\,\vec u_y)$. The corotating component is static in the rotating frame; the counter-rotating component rotates at $2\omega$ and contributes rapidly oscillating terms. The **rotating-wave approximation** (RWA) drops the counter-rotating terms, and it is accurate when $\omega_1\ll\omega_0$; the neglected terms produce the Bloch–Siegert shift, of order $\omega_1^2/\omega_0$. In the biquaternion algebra the split is the decomposition of the linear drive into the two circular components $i\vec e_x\cos(\omega r'_t/c)\mp i\vec e_y\sin(\omega r'_t/c)$, each a Hermitian combination; the RWA keeps the component that corotates with the Larmor rotor $\tilde u_0$ and discards its conjugate. The approximation is thus a statement about which rotor the drive is in phase with, and it has no special algebraic status.

### $\pi$ and $\pi/2$ Pulses

Two pulse durations have a distinguished role. At resonance, $\Omega = \omega_1$, and

$$
r'_t = \frac{\pi}{\omega_1}:\quad P_\downarrow = \sin^2\frac{\pi}{2} = 1,
\qquad
r'_t = \frac{\pi}{2\omega_1}:\quad P_\downarrow = \sin^2\frac{\pi}{4} = \frac12 .
$$

The first is a $\pi$-pulse: it inverts the spin, carrying $\tilde\Pi_1(\vec u_z)$ to $\tilde\Pi_2(\vec u_z)$ with unit probability. The second is a $\pi/2$-pulse: it prepares the equal coherent superposition. In the algebra these are the statements that the rotor $\tilde u_H(\pi/\omega_1) = -\vec e_x$, a $\pi$-rotation about the effective axis $\vec e_x$, exchanges the two idempotents, and that $\tilde u_H(\pi/2\omega_1)$ carries the pole of the Bloch sphere to its equator. A $\pi/2$-pulse followed by a free Larmor evolution and a second $\pi/2$-pulse is the standard Ramsey interferometer; its fringes are governed by the phase accumulated in the interval, in which a dynamical part and a geometric part can be separated.

## The Bloch Picture

The state at any time can be written $\tilde{Ϛ}_{\Psi}(r'_t) = \tfrac12(e_t + i\vec r(r'_t))$, with $\vec r(r'_t)$ the Bloch vector. Substituting into the Schrödinger equation and using the commutator identity $[\tilde{R}_{\Psi,1},\tilde{R}_{\Psi,2}] = -2(\vec r_{\Psi,1}\times\vec r_{\Psi,2})$ of the companion article *Quantum Physics in Biquaternionic Form*, the Bloch vector obeys

$$
\boxed{\;d\vec r/dr'_t = \vec\omega_{\mathrm{eff}}\times\vec r\;},
\qquad
\vec\omega_{\mathrm{eff}} = (-\omega_1, 0, -\Delta),
$$

for the effective Hamiltonian $\tilde{R}_{\Psi,R} = -\frac{m\,c}{2\,k_m}i(\omega_1 \vec e_x+\Delta \vec e_z)$. This is a rigid rotation of $\vec r$ about the fixed axis $-\vec u_R$ at the rate $\Omega$. Three cases are worth separating.

- **Resonance** ($\Delta = 0$): the rotation axis is the $x$-axis, the Bloch vector rotates in the $yz$-plane, and a spin initially along $+z$ passes through the equator and reaches $-z$ after a half-period — the $\pi$-pulse.
- **Large detuning** ($|\Delta|\gg\omega_1$): the axis is close to $-z$, the rotation cone is narrow, and the spin remains near its initial pole, executing small oscillations of amplitude $\sim\omega_1/|\Delta|$ — the dispersive regime.
- **Exact antiresonance** is not a special point for a circular drive; it is special only for a linear drive, where the counter-rotating component becomes corotating. This is the algebraic content of the distinction between the two polarisations.

The Bloch picture is the material of the companion article *Quantum Physics in Biquaternionic Form*; here it is used only to display the effective rotation, and the reader is referred to that article for the derivation of the Bloch equation from the Hermitian form, read through the trace.

## The Biquaternion Reading

**Standard physics, transcribed.** The Larmor precession, the rotating-frame transformation, the effective Hamiltonian, the generalized Rabi frequency, the Rabi formula, the RWA and the $\pi$ and $\pi/2$ pulses are all standard. The article claims no deviation from the standard predictions.

**What the algebra organises.**

- **A single sector.** The drive, the static field and the effective field are all Hermitian elements of $\mathbb{B}_{\Psi}$, and the whole problem is the conjugation of a state in that sector by a product of unitaries. The material sector does not appear, except in the frame rotor $\tilde u_{\mathrm r}$, which is a real quaternion in $\mathbb{B}_{H}$.
- **The rotor as the natural variable.** The rotating frame is not an ad hoc complex exponential; it is conjugation by the unit real quaternion $\exp(-\tfrac{\omega r'_t}{2\,c}\vec e_z)$, the same rotor that carries the Larmor precession. The effective Hamiltonian is the transformed observable, and the resonance condition is the vanishing of its longitudinal component.
- **The spectral gap as the Rabi frequency.** The generalized Rabi frequency is the difference of the two eigenvalues of the effective Hamiltonian, $\pm\frac{m\,c\,\Omega}{2\,k_m}$, so it is a spectral quantity of a Hermitian element of $\mathbb{B}_{\Psi}$. The maximum transition amplitude $\omega_1^2/(\omega_1^2+\Delta^2)$ is the square of the transverse fraction of the effective field, i.e. the geometric tilt of $\vec u_R$ from the equator.
- **No privileged counter-rotating terms.** Because the drive is written as a Hermitian element with an explicit time dependence, the RWA is exposed as a physical approximation about which rotor the drive tracks, not as an algebraic necessity.

**What the algebra does not supply.** The Rabi frequency $\omega_1 = \gamma B_1$ and the Larmor frequency $\omega_0 = \gamma B_0$ contain the gyromagnetic ratio $\gamma$ and the field amplitudes; these are external data, like the mass and the action in the other articles of the series. The algebra also does not supply the time $r'_t$ or the drive frequency $\omega$; the rotating frame is defined by inserting them. Finally, dissipation and relaxation — the Bloch $T_1$ and $T_2$ times — lie outside the Hamiltonian evolution entirely and are not addressed by the framework, which is $*$-unitary.

## Open Questions

1. **Bloch–Siegert and the counter-rotating sector.** The counter-rotating component has the opposite helicity, which in the algebra is the opposite sign of the generator $i\vec e_y$. Is there a natural way to separate the two helicities in the algebra, in the way the chirality projectors separate the two Weyl components of a Dirac spinor? If so, the RWA might acquire an algebraic character it does not have here.

2. **Dissipation.** The framework is $*$-unitary, and the Rabi problem is closed. The open-system version — the Bloch equations with relaxation — requires a density operator that is not merely conjugated by a rotor. Whether the informational sector admits a completely positive map with a natural algebraic form is left open by the companion article *The Measurement Problem in Algebraic Form*.

3. **The rotating frame and the local complex structure.** The rotor $\exp(-\tfrac{\omega r'_t}{2\,c}\vec e_z)$ uses the real unit $\vec e_z$, not the central imaginary. The central imaginary of the Schrödinger equation is fixed, but the series makes the complex structure local, set by the medium. Whether the frame rotor should be regarded as a local object, and how it would then differ from a global one, is unresolved.

4. **Dressed states.** The eigenstates of $\tilde{R}_{\Psi,R}$ are the dressed states of the driven two-level system, and the Mollow triplet in resonance fluorescence is their spectrum. Is there an algebraic statement of the dressed-state structure — for instance a spectral decomposition of $\tilde{R}_{\Psi,R}$ that makes the Autler–Townes splitting immediate?

5. **Empirical content.** As elsewhere, the reformulation reproduces the standard predictions; whether its additional structure implies a measurable deviation is open.

## Summary

A spin-1/2 driven by $\vec B(r'_t) = B_0\vec u_z + B_1(\cos(\omega r'_t/c)\,\vec u_x-\sin(\omega r'_t/c)\,\vec u_y)$ has the biquaternion Hamiltonian

$$
\tilde R_\Psi(r'_t) = -\frac{m\,c\,\omega_{0}}{2\,k_m}i\vec e_z -\frac{m\,c\,\omega_{1}}{2\,k_m}\left(i\vec e_x\cos(\omega r'_t/c) - i\vec e_y\sin(\omega r'_t/c)\right) \in  \mathbb{B}_{\Psi},
$$

with $\omega_0 = \gamma B_0$ and $\omega_1 = \gamma B_1$. The transformation to the frame rotating with the drive is conjugation by the unit real quaternion $\tilde u_{\mathrm r}(r'_t) = \exp(-\tfrac{\omega r'_t}{2\,c}\vec e_z)$, and it produces the static effective Hamiltonian

$$
\tilde{R}_{\Psi,R} = \tilde u_{\mathrm r}^{*}\tilde R_\Psi\tilde u_{\mathrm r} -\frac{m\,c\,i\,\tilde{u}_{\mathrm r}^{*}}{k_m}\partial/\partial r'_t\tilde u_{\mathrm r}
= -\frac{m\,c}{2\,k_m}\Big[(\omega_0-\omega)i\vec e_z + \omega_1 i\vec e_x\Big].
$$

The effective Hamiltonian is a spin observable along the unit vector $\vec u_R = (\omega_1 \vec e_x + \Delta \vec e_z)/\Omega$, with $\Delta = \omega_0-\omega$ the detuning and $\Omega = \sqrt{\omega_1^2+\Delta^2}$ the generalized Rabi frequency equal to its spectral gap. Resonance $\omega = \omega_0$ makes $\tilde{R}_{\Psi,R} = -\frac{m\,c\,\omega_{1}}{2\,k_m}i\vec e_x$ purely transverse, and then the spin precesses about the transverse axis.

The transition probability is the normalised Hermitian form, read through the trace $P_\downarrow(r'_t) = \mathrm{Tr}(\tilde\Pi_2(\vec u_z)\tilde{Ϛ}_{\Psi}(r'_t)^{*})$, and it equals the Rabi formula

$$
P_\downarrow(r'_t) = \frac{\omega_1^2}{\omega_1^2+\Delta^2}\,\sin^2\!\left(\frac{\Omega r'_t}{2}\right),
$$

which reduces to $\sin^2(\omega_1r'_t/c/2)$ on resonance. The $\pi$-pulse $r'_t = \pi/\omega_1$ inverts the spin and the $\pi/2$-pulse $r'_t = \pi/(2\omega_1)$ prepares the equal superposition. The Bloch vector obeys $d\vec r/dr'_t = \vec\omega_{\mathrm{eff}}\times\vec r$ with $\vec\omega_{\mathrm{eff}} = (-\omega_1,0,-\Delta)$, a rigid rotation about the fixed effective axis. The rotating-wave approximation is the discarding of the counter-rotating helicity of a linear drive; it is a statement about which rotor the drive tracks, not an algebraic identity.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_k^2 = -e_t$ |
| $i$ | Central scalar imaginary |
| $\mathbb{B}_{\Psi}$ | Hermitian (informational) subspace; home of all Hamiltonians here |
| $\mathbb{B}_{H}$ | Real-quaternion subspace; home of the frame rotor |
| $\tilde{S}_{\Psi,k} =\frac{m\,c}{2\,k_m}i\vec e_k$ | Spin observable along $\vec e_k$ |
| $\vec B(r'_t) = B_0\vec u_z+B_1(\cos(\omega r'_t/c)\,\vec u_x-\sin(\omega r'_t/c)\,\vec u_y)$ | Static field plus corotating drive |
| $\omega_0 = \gamma B_0$ | Larmor frequency |
| $\omega_1 = \gamma B_1$ | Rabi frequency |
| $\Delta = \omega_0-\omega$ | Detuning |
| $\tilde R_\Psi(r'_t) = -\frac{m\,c\,\omega_{0}}{2\,k_m}i\vec e_z-\frac{m\,c\,\omega_{1}}{2\,k_m}(i\vec e_x\cos(\omega r'_t/c)-i\vec e_y\sin\omega r'_t/c)$ | Laboratory Hamiltonian |
| $\tilde u_{\mathrm r}(r'_t) = \exp(-\tfrac{\omega r'_t}{2\,c}\vec e_z)$ | Rotating-frame rotor |
| $\tilde{R}_{\Psi,R} = -\frac{m\,c}{2\,k_m}[(\omega_0-\omega)i\vec e_z+\omega_1i\vec e_x]$ | Effective Hamiltonian in the rotating frame |
| $\Omega = \sqrt{\omega_1^2+\Delta^2}$ | Generalized Rabi frequency (spectral gap) |
| $\vec u_R = (\omega_1\vec e_x+\Delta \vec e_z)/\Omega$ | Effective rotation axis |
| $P_\downarrow(r'_t) = \tfrac{\omega_1^2}{\omega_1^2+\Delta^2}\sin^2(\Omega r'_t/2)$ | Rabi transition probability |
| $\pi/\omega_1$, $\pi/(2\omega_1)$ | $\pi$-pulse, $\pi/2$-pulse durations |
| $d\vec r/dr'_t = \vec\omega_{\mathrm{eff}}\times\vec r$ | Bloch equation in the rotating frame |

## Further Reading

- I. I. Rabi, "On the Process of Space Quantization," *Physical Review* **49** (1936) 324–328, for the original resonance method.
- I. I. Rabi, S. Millman, P. Kusch, and J. R. Zacharias, "The Molecular Beam Resonance Method for Measuring Nuclear Magnetic Moments," *Physical Review* **55** (1939) 526–535, for the molecular-beam resonance experiment.
- F. Bloch, "Nuclear Induction," *Physical Review* **70** (1946) 460–474, for the Bloch equations and relaxation.
- E. M. Purcell, H. C. Torrey, and R. V. Pound, "Resonance Absorption by Nuclear Magnetic Moments in a Solid," *Physical Review* **69** (1946) 37–38, for nuclear magnetic resonance in condensed matter.
- L. Allen and J. H. Eberly, *Optical Resonance and Two-Level Atoms* (Wiley, 1975), for the dressed states, the Rabi formula, and the rotating-wave approximation.
- Claude Cohen-Tannoudji, Jacques Dupont-Roc, and Gilbert Grynberg, *Atom–Photon Interactions* (Wiley, 1992), for the dressed-state and resonance-fluorescence treatment.
- L. D. Landau and E. M. Lifshitz, *Quantum Mechanics: Non-Relativistic Theory* (Pergamon, 1977), for the two-level system in a resonant field.
- J. J. Sakurai and Jim Napolitano, *Modern Quantum Mechanics* (Pearson, 2017), for the spin-1/2 treatment of magnetic resonance and the rotating frame.
