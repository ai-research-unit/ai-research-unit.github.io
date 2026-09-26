# __Geometric Phases of Non-Relativistic Spin in Biquaternionic Form__

## Introduction

A spin-1/2 whose Bloch vector is carried around a closed curve on the Bloch sphere returns to its initial **state** but not necessarily to its initial **spinor**: the state is an idempotent, and the idempotent returns exactly, while the spinor returns only up to a phase. That phase has two parts. One is **dynamical** and proportional to the elapsed time and to the energy; the other is **geometric**, depends only on the curve, and for a spin-1/2 equals minus one half of the oriented solid angle that the curve subtends at the origin. This is the geometric phase of non-relativistic spin.

The adiabatic form of the statement — a Hamiltonian transported slowly around a loop, with the spin following the instantaneous eigenstate — is the **Berry phase**, and it is the subject of the companion article *The Berry Phase and Geometric Phases in Biquaternionic Form*, which computes the Berry connection and curvature and verifies the two-route agreement on a slowly rotating field. The present article treats the **non-adiabatic** form, the **Aharonov–Anandan (AA) phase**, and the spin-specific structures that accompany it: the exact phase of a precessing spin, the $4\pi$ periodicity of the spinor, and the holonomy as a rotor in the real-quaternion subspace. It does not repeat the connection-and-curvature computation of the Berry article; it cites it.

The findings are stated in advance.

1. **The geometric phase is a holonomy of the spinor, not a property of the idempotent.** The instantaneous state $\tilde{P}_\pm(\hat n)$ contains no phase information; the phase is carried by the spinor and is removed by the idempotent. This is the structural fact the Berry article records for the adiabatic connection, and it holds unchanged for the AA phase.
2. **For spin-1/2 the geometric phase is one half the oriented solid angle, with a sign:** $\gamma_{\mathrm{geo}} = -\tfrac12\Omega_{\mathrm{sgn}}$, where $\Omega_{\mathrm{sgn}}$ is the solid angle subtended by the closed curve, counted positive for the orientation given by the right-hand rule about the curve.
3. **The AA phase is exact for a precessing spin.** A spin prepared along $\hat{m}$ and left in a fixed field along $\hat{n}$ has a Bloch vector that precesses on a cone of half-angle $\theta_0$; over one period the AA phase is $\tfrac12$ of the unsigned solid angle of the cap, with the sign fixed by the sense of precession. This is computed exactly below, with no adiabatic approximation.
4. **The spinor is double-valued.** A full $2\pi$ rotation of the spin returns the idempotent but sends the spinor to its negative; only after $4\pi$ does the spinor return. The geometric phase of the equator loop is the cleanest instance: the phase is $\pi$ after one period, a sign change, and $2\pi$ (i.e. the identity) after two.
5. **The holonomy is a rotor.** The accumulated spin evolution is the product of a central phase and conjugation by a unit real quaternion $\tilde{R} = e^{-\frac{1}{2}\Phi\,\hat{n}}$, where $\Phi$ is the angle through which the Bloch vector is turned; the central phase and the rotation are the two faces of the same element of $\mathbb{B}$.
6. **The adiabatic Berry phase is the slow limit of the same holonomy.** Using the rotating-frame effective field of a circularly polarised drive, the AA phase reduces to the solid-angle formula when the drive is slow, with the sign set by the sense of the loop, and it departs from it as the drive speeds up.

The notation is that of the read-list articles: $\tilde{S}_k = \tfrac{\hbar}{2}ie_k$, $\tilde{P}_\pm(\hat\mu) = \tfrac12(e_0\pm i\hat\mu)$, $\tilde{\rho} = \tfrac12(e_0+i\mathbf{r})$, the trace formula $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$, and the isomorphism $\Phi$ with $ie_k\mapsto\sigma_k$.

The companion articles supply the pieces:
- Companion article *The Berry Phase and Geometric Phases in Biquaternionic Form*, for the adiabatic connection, the curvature and the two-route check.
- Companion article *Spin-1/2 Quantum Mechanics in Biquaternionic Form*, for the spin operators and the pure-state idempotents.
- Companion article *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, for the trace pairing and the Hermitian sector.
- Companion article *Exercise: Spin Precession in a Magnetic Field*, for the Larmor precession used for the cyclic evolution.

## The Two Phases

### The Dynamical Phase

A state that evolves under a time-independent Hamiltonian $\tilde{H}$ acquires the phase

$$
\psi(t) = e^{-\frac{i}{\hbar}\tilde{H}t}\,\psi(0),
\qquad\text{so}\qquad
\psi(T) = e^{-\frac{i}{\hbar}E\,T}\,\psi(0)
$$

for an eigenstate of energy $E$. The phase $-\frac{1}{\hbar}\int_0^T E\,dt$ is the **dynamical phase**; it is proportional to the duration, so a longer journey accumulates more of it. For a general state the energy in the exponent is the expectation $\langle\tilde{H}\rangle$, and the same statement holds with $\int_0^T\langle\tilde{H}\rangle\,dt/\hbar$.

The dynamical phase is not what this article is about. It is removed by a standard subtraction, and the residue is the geometric part. The subtraction is meaningful because the two parts respond differently to a change of the speed of the journey at fixed geometry: the dynamical phase scales with the duration and the geometric phase does not.

### The Aharonov–Anandan Phase

Let $|\psi(t)\rangle$ be a normalized solution of the Schrödinger equation that is **cyclic**, $|\psi(T)\rangle = e^{i\phi_{\mathrm{tot}}}|\psi(0)\rangle$ for some real $\phi_{\mathrm{tot}}$. Define

$$
\gamma_{AA} = \phi_{\mathrm{tot}} + \frac{1}{\hbar}\int_0^T\langle\psi(t)|\tilde{H}(t)|\psi(t)\rangle\,dt .
$$

This is the **Aharonov–Anandan phase**. It is well defined for any cyclic evolution, adiabatic or not; it is invariant under a rephasing of the initial state; and it depends on the curve traced by the state in projective space, not on the speed at which the curve is traversed. In the biquaternion language the two terms are both real numbers built from the trace pairing:

$$
\langle\tilde{H}\rangle = \mathrm{Tr}(\tilde{\rho}\tilde{H}), \qquad
\phi_{\mathrm{tot}} = \arg\,\mathrm{Tr}(\psi(0)^\dagger\psi(T)) .
$$

The subtraction is the statement that the AA phase is the part of the total phase not accounted for by the energy integral.

### The Berry Phase as the Adiabatic Limit

If the Hamiltonian is transported slowly around a loop in parameter space and the system follows the instantaneous eigenstate, the AA phase becomes the **Berry phase**

$$
\gamma_{\mathrm{Berry}} = \oint \mathcal{A}, \qquad
\mathcal{A} = i\,\langle n(R)|\,d\,|n(R)\rangle ,
$$

the line integral of the Berry connection. The companion article *The Berry Phase and Geometric Phases in Biquaternionic Form* derives $\mathcal{A}$ in the biquaternion algebra, shows that it lives on the spinor rather than on the idempotent, computes the curvature $\mathcal{F} = d\mathcal{A}$, and verifies the line and surface routes on the spin-1/2 loop. Here the Berry phase is used only as the adiabatic limit against which the AA phase is checked.

## The Spin-1/2 Holonomy

### The Solid-Angle Formula

For a spin-1/2 whose Bloch vector traces a closed curve $\mathcal{C}$ on the unit sphere, the geometric phase is

$$
\boxed{\;\gamma_{\mathrm{geo}} = -\frac{1}{2}\,\Omega_{\mathrm{sgn}}(\mathcal{C})\;}
$$

where $\Omega_{\mathrm{sgn}}(\mathcal{C})$ is the **oriented** solid angle of the curve, counted positive when the curve is traversed in the sense given by the right-hand rule about the outward normal of the cap it bounds. For a latitude circle at polar angle $\theta_0$, the unsigned solid angle of the cap is

$$
\Omega = 2\pi\left(1-\cos\theta_0\right),
$$

and the oriented value is $\Omega_{\mathrm{sgn}} = \pm\Omega$ according to the sense of traversal. The factor $\tfrac12$ is the spin-1/2 value; for spin $j$ it would be $j$ times the solid angle (with a sign), which is outside the scope of this subcategory.

The formula has three immediate consequences. It is **reparametrisation invariant**, since the solid angle does not know the speed. It is **defined modulo $2\pi$**, since a phase is. And it is **sign-sensitive**: reversing the traversal of the same curve reverses the sign of the phase.

### The Exact Precessing Spin

The cleanest exactly solvable case is the fixed field. Take the field along $\hat{z}$,

$$
\tilde{H} = -\frac{\hbar\omega_L}{2}\,ie_3,
\qquad \omega_L = \gamma B > 0,
$$

in the convention of the companion exercise *Exercise: Spin Precession in a Magnetic Field*, where the Bloch vector of a state initially along $+\hat{x}$ precesses as $\mathbf{r}(t) = (\cos\omega_L t, -\sin\omega_L t, 0)$. Prepare the spin along

$$
\hat{m} = \left(\sin\theta_0,\,0,\,\cos\theta_0\right),
$$

so that its Bloch vector makes an angle $\theta_0$ with the field axis. Under the evolution $\tilde{U}(t) = \exp(-\tfrac{\omega_L t}{2}e_3)$ the Bloch vector precesses on the cone of half-angle $\theta_0$ about $\hat z$, and at the period

$$
T = \frac{2\pi}{\omega_L}
$$

it returns to its initial position. The spinor returns only up to a phase, which is computed exactly.

In the matrix representation the spinor is $\psi(0) = (\cos\tfrac{\theta_0}{2},\,\sin\tfrac{\theta_0}{2})^{\!T}$ and the propagator is

$$
U(T) = \exp\!\left(+\frac{i}{2}\omega_L T\,\sigma_3\right) = e^{i\pi\sigma_3} = -I_2 ,
$$

so the total phase is $\phi_{\mathrm{tot}} = \pi$ and $\psi(T) = -\psi(0)$. The dynamical integral is elementary because $\langle\sigma_3\rangle = \cos\theta_0$ is conserved by the precession:

$$
\frac{1}{\hbar}\int_0^T\langle\tilde{H}\rangle\,dt
= -\frac{\omega_L}{2}\cos\theta_0\,T = -\pi\cos\theta_0 .
$$

Hence the AA phase is

$$
\gamma_{AA} = \pi - \pi\cos\theta_0 = \pi(1-\cos\theta_0) = \frac{\Omega}{2},
\qquad \Omega = 2\pi(1-\cos\theta_0).
$$

The traversal here is clockwise as seen from $+\hat z$ (the corpus Larmor sense), so $\Omega_{\mathrm{sgn}} = -\Omega$ and the general formula gives $\gamma_{\mathrm{geo}} = -\tfrac12(-\Omega) = +\tfrac{\Omega}{2}$, in exact agreement. The result was verified numerically for $\theta_0 = 0.3, 0.9, 1.57, 2.4, 3.0$; in every case $\gamma_{AA}\equiv +\Omega/2\pmod{2\pi}$, with the continuous branch passing through $0$ at $\theta_0 = 0$ and at $\theta_0 = \pi$ as it must.

Two limits make the formula transparent. At $\theta_0\to0$ the state is the eigenstate along the field and does not precess; the curve degenerates to a point, $\Omega\to0$, and the geometric phase vanishes. At $\theta_0\to\pi$ the state is again an eigenstate (the opposite one), the curve again degenerates, and $\Omega\to4\pi$, so $\gamma_{AA}\to2\pi\equiv0$. The geometric phase is largest at the equator, where it is $\pi$: the spinor changes sign after a full precession at $\theta_0 = \pi/2$.

### The $4\pi$ Periodicity

The sign change $\psi(T) = -\psi(0)$ at the equator is not special to the equator: for every $\theta_0$ the spinor after one period differs from the initial spinor by a phase, and at $\theta_0 = \pi/2$ that phase is exactly $\pi$. The general statement is the double-valuedness of the spinor representation of the rotation group: a rotation of the spin by $2\pi$ is the identity on the idempotent,

$$
\tilde{R}(2\pi)\,\tilde{P}_\pm(\hat{n})\,\tilde{R}(2\pi)^\dagger = \tilde{P}_\pm(\hat{n}),
\qquad
\tilde{R}(2\pi) = e^{-2\pi e_3/2} = -e_0,
$$

but acts on the spinor as multiplication by $-e_0$, and only a rotation by $4\pi$ is the identity on the spinor. In the biquaternion algebra this is the statement that the rotation group realised on the spinor is $SU(2)$, the double cover of the $SO(3)$ realised on the idempotents. The rotor $\tilde{R}(2\pi) = -e_0$ is the nontrivial element of the kernel of the covering map, and the geometric phase of the equator loop is the phase it carries.

The physical consequences are standard: the spinor must be rotated by $4\pi$ to return, and the interference of spinor amplitudes can reveal the sign. The neutron interferometry of Rauch and collaborators and of Werner and collaborators are the standard demonstrations, and the $4\pi$ periodicity has since been confirmed with neutron resonance interferometry.

## The Holonomy as a Rotor

### The Spinor Carries the Phase

The geometric phase is invisible in the density matrix. Write a pure state as $\tilde{\rho} = \tilde{P}_\pm(\hat n) = \tfrac12(e_0\pm i\hat n)$; the idempotent is quadratic in the spinor,

$$
\tilde{P} = \frac{\psi\psi^\dagger}{\mathrm{Tr}(\psi^\dagger\psi)},
$$

and a spinor phase $\psi\mapsto e^{i\alpha}\psi$ cancels between $\psi$ and $\psi^\dagger$. So the state that the Bloch ball records is exactly the object in which the geometric phase is absent. This is the same observation the Berry article makes about the Berry connection — $\mathrm{Tr}(\tilde{P}\partial_\mu\tilde{P}) = 0$ identically — and it applies verbatim to the AA phase: the phase lives in the spinor, which is the lift of the Bloch vector to the double cover.

### The Rotor and Its Two Faces

The evolution over a closed loop of the state is, in the algebra, the product of a rotor and a central phase,

$$
\tilde{U} = e^{i\alpha}\,\tilde{R},
\qquad
\tilde{R} = e^{-\frac{1}{2}\Phi\,\hat{n}} = \cos\frac{\Phi}{2}\,e_0 - \sin\frac{\Phi}{2}\,\hat{n},
$$

for some axis $\hat{n}$, where $\Phi$ is the angle through which the Bloch vector is turned and $e^{i\alpha}$ carries the dynamical part $e^{-\frac{i}{\hbar}\int\langle\tilde{H}\rangle dt}$. The two faces are:

- the **rotor** $\tilde{R}\in\mathbb{H}_{\mathbb{B}}$, which rotates the Bloch vector and is observable through the orientation of the state;
- the **central phase** $e^{i\alpha}\in\mathbb{C}_{\mathbb{B}}$, which multiplies the spinor and is observable only through interference with another amplitude.

The AA phase is the statement that the spinor phase and the geometry of the loop are locked together for a spin-1/2: the geometric phase is one half of the oriented solid angle swept by the Bloch vector, $\gamma_{\mathrm{geo}} = -\tfrac12\Omega_{\mathrm{sgn}}$. For the equator loop the swept solid angle has magnitude $2\pi$ and the phase is $\pi$ — one half of the full turn of the vector, which is why the spinor returns only to minus itself after one period. In general the relation between the geometric phase and the holonomy is a lift of an $SO(3)$ element to $SU(2)$, and the factor $\tfrac12$ is the statement that the lift is two-to-one.

### Gauge Freedom and the Pancharatnam Connection

The AA phase is defined for a cyclic evolution, but the geometric phase can be extended to non-cyclic paths by the **Pancharatnam connection**: for two non-orthogonal states $|\psi_1\rangle$, $|\psi_2\rangle$, the relative phase is $\arg\langle\psi_1|\psi_2\rangle$, and the geometric phase of a sequence is the total Pancharatnam phase minus the dynamical phases. In the algebra the Pancharatnam connection is again the trace pairing,

$$
\arg\langle\psi_1|\psi_2\rangle = \arg\,\mathrm{Tr}\!\left(\psi_1^\dagger\psi_2\right),
$$

and it is gauge-covariant: a rephasing $\psi_a\mapsto e^{i\alpha_a}\psi_a$ shifts the connection by a total derivative, exactly as in the Berry article. The gauge freedom of the geometric phase is the freedom to rephase the spinor at each point of the path, and the curvature is the gauge-invariant content.

## The Rotating Field at Arbitrary Rate

### The Rotating-Frame Effective Field

The adiabatic limit is the slow end of a one-parameter family. Consider a field whose direction rotates about $\hat{z}$ at angular frequency $\omega$ in the Larmor sense of the corpus,

$$
\hat{n}(t) = \left(\sin\theta_0\cos\omega t,\,-\sin\theta_0\sin\omega t,\,\cos\theta_0\right),
$$

with Hamiltonian $\tilde{H}(t) = -\tfrac{\hbar\omega_L}{2}i\,\hat{n}(t)$ and $\hat{n}(t)_k\tilde{S}_k$ the instantaneous spin along the field. Transforming to the frame that corotates with the field, $\tilde{U}_R(t) = \exp(-\tfrac{\omega t}{2}e_3)$, gives the static effective Hamiltonian

$$
\tilde{H}_R = \tilde{U}_R^\dagger\tilde{H}\tilde{U}_R - i\hbar\,\tilde{U}_R^\dagger\partial_t\tilde{U}_R
= -\frac{\hbar}{2}\Big[\left(\omega_L\cos\theta_0-\omega\right)ie_3 + \omega_L\sin\theta_0\,ie_1\Big],
$$

which is the same rotating-frame structure as the Rabi problem. The rotating-frame Hamiltonian is $\tilde{H}_R = -\tfrac{\hbar}{2}\,i\,\mathbf{h}_{\mathrm{eff}}\cdot\mathbf{e}$ with

$$
\mathbf{h}_{\mathrm{eff}} = \left(\omega_L\sin\theta_0,\;0,\;\omega_L\cos\theta_0-\omega\right),
\qquad
\Omega_{\mathrm{eff}} = \sqrt{\omega_L^2 + \omega^2 - 2\omega\omega_L\cos\theta_0},
$$

so the effective spin observable points along $\hat{\mathbf{h}}_{\mathrm{eff}}$, and the Bloch vector precesses about $-\hat{\mathbf{h}}_{\mathrm{eff}}$ at the rate $\Omega_{\mathrm{eff}}$. Two limits are immediate.

- **Adiabatic limit** $\omega\ll\omega_L$: $\Omega_{\mathrm{eff}}\to\omega_L$ and $\mathbf{h}_{\mathrm{eff}}\to\omega_L\hat{n}(0)$; the spin follows the instantaneous eigenstate, and the holonomy is the solid-angle phase $-\tfrac12\Omega_{\mathrm{sgn}}$. For the clockwise loop used here the oriented solid angle is $-\Omega$ with $\Omega = 2\pi(1-\cos\theta_0)$, so the holonomy is $+\tfrac{\Omega}{2}$; the companion article uses the opposite (counterclockwise) orientation of the rotating field and therefore reports $-\tfrac{\Omega}{2}$. The magnitude is the same and the sign is fixed by the orientation, as the general formula requires.
- **Sudden limit** $\omega\gg\omega_L$: $\Omega_{\mathrm{eff}}\to\omega$ and the effective field is dominated by the $-\omega$ term; the spin cannot follow the field and the geometric phase is suppressed.

At the **resonance** $\omega = \omega_L\cos\theta_0$ the longitudinal component vanishes, $\mathbf{h}_{\mathrm{eff}} = \omega_L\sin\theta_0\,\hat{x}$, and the effective spin field lies in the equatorial plane; the spin then precesses about the equatorial axis at the rate $\omega_L\sin\theta_0$. The Floquet quasi-energy over one period is the phase of the effective evolution; the geometric part is obtained by subtracting it from the total phase, exactly as in the AA definition.

### What Changes and What Does Not

The rotating field exhibits the interpolation between the adiabatic Berry phase and the sudden limit. The **geometric part** of the phase is always the holonomy of the spinor connection; what changes with $\omega$ is how much of the evolution is adiabatic, i.e. how closely the actual state tracks the instantaneous eigenstate. The AA phase removes the dynamical part exactly and leaves the geometric part; for a non-cyclic evolution at intermediate $\omega$ the state does not return to its initial ray, and the geometric phase is defined only after a cyclic protocol (for instance, a Floquet period or a spin-echo sequence) is specified.

## What the Algebra Adds and What It Does Not

**Standard physics, transcribed.** The dynamical/geometric split, the AA phase, the Berry phase, the solid-angle formula, the $4\pi$ periodicity, and the rotating-field effective Hamiltonian are all standard. The article claims no deviation.

**What the algebra organises.**

- **The double cover is explicit.** The rotor group is $\mathbb{H}_{\mathbb{B}}$, the unit real quaternions, and the kernel of the spinor representation is $\{\pm e_0\}$; the $4\pi$ periodicity is the statement that $-e_0$ acts trivially on the idempotents and non-trivially on the spinor. The algebra makes the covering map manifest.
- **The phase lives in the spinor.** The idempotent contains no phase, as the Berry article records; the trace pairing on the spinor carries the Pancharatnam connection. The geometric phase is thus a property of the lift of the Bloch vector, not of the Bloch vector.
- **The holonomy is a rotor with two faces.** The same unit quaternion produces the spatial rotation (observable in the orientation) and the spinor phase (observable in interference). The factor $\tfrac12$ relating them is the lift $\mathbb{H}_{\mathbb{B}}\to SO(3)$.
- **A common rotating-frame structure.** The rotating-field problem has the same effective Hamiltonian form as the Rabi problem, with the detuning replaced by $\omega_L\cos\theta_0-\omega$ and the transverse coupling by $\omega_L\sin\theta_0$. The framework makes the identity of the two problems visible.

**What the algebra does not supply.** The field amplitude, the gyromagnetic ratio and the rate $\omega$ are external data. The algebra does not select the loop or the protocol; it describes the holonomy of whatever spinor path the protocol produces. And the numerical value of the geometric phase, being an angle, is defined modulo $2\pi$; the framework does not remove that ambiguity, which is physical.

## Open Questions

1. **Non-abelian geometric phases.** The AA and Berry phases here are abelian ($U(1)$) because the spin-1/2 level is non-degenerate. For a degenerate level the holonomy is non-abelian. The framework of a single spin-1/2 cannot host the non-abelian case; the question is whether the algebra's idempotent structure extends to it, and it is left open by the Berry article as well.

2. **The geometric phase of a mixed state.** A mixed state $\tilde\rho = \tfrac12(e_0+i\mathbf{r})$, $|\mathbf{r}|<1$, can also be transported around a loop, and a geometric phase can be defined for it (the Uhlmann phase). Does the algebra's null cone of zero divisors, which the companion article *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* identifies with a mirror light cone, support a natural phase for the boundary and the interior?

3. **The local complex structure.** The spinor phase uses the central $i$, while the rotor uses the real units $e_k$. The series allows the complex structure to be local; the geometric phase, however, seems to require a globally defined spinor phase. Whether a local complex structure would modify the phase is unresolved, as it is in the companion articles *The Schrödinger Equation in Biquaternionic Form* and *The Path Integral in Biquaternionic Form*.

4. **The classical analogue.** The Hannay angle is the classical-adiabatic analogue of the Berry phase. The biquaternion framework's relation to classical spin precession is not developed here; whether the Hannay angle has an algebraic reading is open.

5. **Empirical contact.** As elsewhere, the reformulation reproduces the standard predictions; whether it implies a measurable deviation is open.

## Summary

For non-relativistic spin-1/2, a closed evolution of the Bloch vector around a curve $\mathcal{C}$ returns the state but not the spinor, and the spinor acquires the geometric phase

$$
\gamma_{\mathrm{geo}} = -\frac{1}{2}\,\Omega_{\mathrm{sgn}}(\mathcal{C}),
$$

one half the oriented solid angle of the curve, negative for the orientation given by the right-hand rule. For a latitude circle at polar angle $\theta_0$ the unsigned solid angle is $\Omega = 2\pi(1-\cos\theta_0)$.

The **Aharonov–Anandan phase** is the exact, non-adiabatic version: for a cyclic evolution, $\gamma_{AA} = \phi_{\mathrm{tot}} + \frac{1}{\hbar}\int_0^T\langle\tilde{H}\rangle\,dt$, with all quantities expressed through the trace pairing. For a spin prepared along $\hat{m}$ at angle $\theta_0$ from a fixed field along $\hat{z}$, the exact result is

$$
\gamma_{AA} = \pi(1-\cos\theta_0) = \frac{\Omega}{2},
$$

in the corpus Larmor sense (clockwise about $+\hat{z}$), which agrees with the general formula because the oriented solid angle is $-\Omega$. At $\theta_0 = \pi/2$ this is $\pi$: the spinor changes sign after one precession period, and only after two periods does it return. The propagator over one period is $\tilde{R}(2\pi) = -e_0$, the nontrivial element of the kernel of the double cover $\mathbb{H}_{\mathbb{B}}\to SO(3)$.

The **Berry phase** is the adiabatic limit of the same holonomy. For the field rotating about $\hat{z}$ at rate $\omega$, the rotating frame gives the static effective spin field $\mathbf{h}_{\mathrm{eff}} = (\omega_L\sin\theta_0,0,\omega_L\cos\theta_0-\omega)$ with gap $\Omega_{\mathrm{eff}} = \sqrt{\omega_L^2+\omega^2-2\omega\omega_L\cos\theta_0}$; in the limit $\omega\ll\omega_L$ the holonomy is $-\tfrac12\Omega_{\mathrm{sgn}}$ with the sign fixed by the traversal, and at $\omega = \omega_L\cos\theta_0$ the effective field is purely transverse.

The geometric phase is carried by the spinor, not by the idempotent: the density matrix is quadratic in the spinor and the phase cancels in it. The holonomy is a rotor in $\mathbb{H}_{\mathbb{B}}$ whose rotation angle is twice the spinor phase, and this factor of two is the statement that the spinor representation is the double cover of the rotation group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Central scalar imaginary |
| $\mathbb{M}_+$ | Hermitian (informational) subspace |
| $\mathbb{H}_{\mathbb{B}}$ | Unit real quaternions; the rotation/holonomy rotors |
| $\tilde{S}_k = \tfrac{\hbar}{2}ie_k$ | Spin observable along $\hat{k}$ |
| $\tilde{H} = -\tfrac{\hbar\omega_L}{2}ie_3$ | Fixed-field Hamiltonian |
| $\omega_L = \gamma B$ | Larmor frequency |
| $\tilde{P}_\pm(\hat\mu) = \tfrac12(e_0\pm i\hat\mu)$ | Pure-state idempotent; carries no phase |
| $\psi$ | Spinor; carries the geometric phase |
| $\gamma_{AA} = \phi_{\mathrm{tot}} + \tfrac{1}{\hbar}\int_0^T\langle\tilde{H}\rangle dt$ | Aharonov–Anandan geometric phase |
| $\mathcal{A} = i\langle n|d|n\rangle$ | Berry connection (cited from the Berry article) |
| $\gamma_{\mathrm{geo}} = -\tfrac12\Omega_{\mathrm{sgn}}(\mathcal{C})$ | Solid-angle formula for spin-1/2 |
| $\Omega = 2\pi(1-\cos\theta_0)$ | Unsigned solid angle of a latitude cap |
| $\theta_0$ | Half-angle of the precession cone / polar angle of the loop |
| $\tilde{R}(2\pi) = -e_0$ | One-period rotor; spinor double-valuedness |
| $\tilde{R} = e^{-\frac{1}{2}\Phi\hat{n}}$ | Holonomy rotor; $\Phi$ the turn of the Bloch vector |
| $\tilde{U}_R(t) = \exp(-\tfrac{\omega t}{2}e_3)$ | Rotating-frame rotor for the driven field |
| $\mathbf{h}_{\mathrm{eff}} = (\omega_L\sin\theta_0,0,\omega_L\cos\theta_0-\omega)$ | Effective spin field in the rotating frame |
| $\Omega_{\mathrm{eff}} = \sqrt{\omega_L^2+\omega^2-2\omega\omega_L\cos\theta_0}$ | Generalized (Floquet) frequency |
| $\arg\langle\psi_1|\psi_2\rangle = \arg\mathrm{Tr}(\psi_1^\dagger\psi_2)$ | Pancharatnam connection |

## Further Reading

- M. V. Berry, "Quantal Phase Factors Accompanying Adiabatic Changes," *Proceedings of the Royal Society A* **392** (1984) 45–57, for the adiabatic geometric phase.
- Y. Aharonov and J. Anandan, "Phase Change during a Cyclic Quantum Evolution," *Physical Review Letters* **58** (1987) 1593–1596, for the non-adiabatic geometric phase used here.
- S. Pancharatnam, "Generalized Theory of Interference, and Its Applications. Part I," *Proceedings of the Indian Academy of Sciences A* **44** (1956) 247–262, for the connection for non-cyclic paths.
- J. Anandan and Y. Aharonov, "Geometry of Quantum Evolution," *Physical Review Letters* **65** (1990) 1697–1700, for the geometric interpretation of the phase in projective Hilbert space.
- M. V. Berry, "Quantum Phase Corrections from Adiabatic Iteration," *Proceedings of the Royal Society A* **414** (1987) 31–46, for the relation between the adiabatic and non-adiabatic phases.
- H. Rauch, A. Zeilinger, G. Badurek, A. Wilfing, W. Bauspiess, and U. Bonse, "Verification of Coherent Spinor Rotation of Fermions," *Physics Letters A* **54** (1975) 425–427, for the $4\pi$ periodicity in neutron interferometry.
- S. A. Werner, R. Colella, A. W. Overhauser, and C. F. Eagen, "Observation of the Phase Shift of a Neutron due to Precession in a Magnetic Field," *Physical Review Letters* **35** (1975) 1053–1055, for the spinor phase in neutron interferometry.
- W. H. Kraan, S. V. Grigoriev, and M. Th. Rekveldt, "Observation of $4\pi$-Periodicity of the Spinor Using Neutron Resonance Interferometry," *Europhysics Letters* **66** (2004) 164–170, for the confirmation of the $4\pi$ periodicity.
- A. Shapere and F. Wilczek, *Geometric Phases in Physics* (World Scientific, 1989), for the collected theory and applications.
- J. J. Sakurai and Jim Napolitano, *Modern Quantum Mechanics* (Pearson, 2017), for spin-1/2 precession and the phase conventions used here.
