# __Exercise: Spin Precession in a Magnetic Field__

## Introduction

This article is one of a series of **worked exercises** that illustrate quantum physics in two parallel presentations: the standard Hilbert-space formulation, and the biquaternion formulation developed in the companion articles. The goal is not to derive new physics, but to give the reader a concrete, computationally explicit demonstration of the correspondence between the two formalisms.

Each exercise in the series is solved twice: first in the standard way, then in the biquaternion way. The results agree, as they must: the two formulations are the same mathematics in different notation. To keep the two solutions strictly parallel, each is presented in the same steps, and the final result is stated in the same form.

The first exercise treated the Born rule and the measurement of spin along an arbitrary direction. This second exercise treats **dynamics**: the time evolution of a spin state under a time-independent Hamiltonian.

The conventions are those of the companion articles. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with the Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$. The quaternion units are $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ with $\vec e_k^2 = -e_t$, and $i$ is the scalar imaginary. The trace of an element of $\mathbb{M}_+$ is twice its scalar part: $\mathrm{Tr}(\tilde Q)=2\,\mathrm{Sc}(\tilde Q)$.

## The Exercise

A spin-$\tfrac{1}{2}$ particle is prepared in the **spin-up state along the $x$-axis**, and is then placed in a uniform magnetic field

$$
\vec B = B_0\,\vec u_z
$$

pointing along the $z$-axis. The magnetic moment of the particle is $\vec\mu = \gamma\vec S$, where $\gamma$ is the gyromagnetic ratio and $\vec S$ is the spin operator. What is the **expectation value of the spin along the $x$-axis** as a function of time?

This is the classic **Larmor precession** exercise. It exercises the Hamiltonian, the evolution operator, and the time-dependent expectation value, in a setting where the answer is a simple harmonic function of time.

## Solution in the Standard Formulation

### Step 1: The state

The spin-up state along the $x$-axis is the eigenvalue-$+1$ eigenvector of the Pauli matrix $\sigma_1$:

$$
|+x\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix}.
$$

### Step 2: The Hamiltonian

The Hamiltonian of a magnetic moment $\vec\mu = \gamma\vec S$ in a magnetic field $\vec B = B_0\vec u_z$ is

$$
H = -\vec\mu\cdot\vec B = -\gamma B_0 S_z = -\frac{\hbar\omega_L}{2}\sigma_3,
$$

where

$$
\omega_L = \gamma B_0
$$

is the **Larmor frequency** and $S_z = \frac{\hbar}{2}\sigma_3$.

### Step 3: The evolution

The evolution operator is

$$
T(t') = \exp(-iHt'/\hbar) = \exp(\,i\omega_L t'\,\sigma_3/2) = \begin{pmatrix} \exp(\,i\omega_L t'/2) & 0 \\ 0 & \exp(-i\omega_L t'/2) \end{pmatrix}.
$$

The evolved state is

$$
|\psi(t')\rangle = T(t')\,|+x\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} \exp(\,i\omega_L t'/2) \\ \exp(-i\omega_L t'/2) \end{pmatrix}.
$$

### Step 4: The expectation value

The expectation value of $S_x = \frac{\hbar}{2}\sigma_1$ in the state $|\psi(t')\rangle$ is

$$
\langle S_x\rangle(t') = \langle\psi(t')|S_x|\psi(t')\rangle.
$$

Computing the matrix element,

$$
\langle\psi(t')|\sigma_1|\psi(t')\rangle = \frac{1}{2}\left(\exp(-i\omega_L t'/2) \cdot \exp(-i\omega_L t'/2) + \exp(\,i\omega_L t'/2) \cdot \exp(\,i\omega_L t'/2)\right) = \frac{1}{2}\left(\exp(-i\omega_L t') + \exp(\,i\omega_L t')\right) = \cos(\omega_L t').
$$

Therefore

$$
\langle S_x\rangle(t') = \frac{\hbar}{2}\cos(\omega_L t').
$$

## Solution in the Biquaternion Formulation

### Step 1: The state

In the biquaternion framework, a pure spin state is an **idempotent** of the Hermitian subspace $\mathbb{M}_+$, of the form

$$
\tilde\Pi(\vec u_m) = \tfrac{1}{2}\left(e_t + i\vec u_m\right),
$$

where $\vec u_m$ is a unit pure real quaternion. The spin-up state along $x$ corresponds to $\vec u_m = \vec e_x$, giving

$$
\tilde\Pi_x = \tfrac{1}{2}\left(e_t + i \vec e_x\right).
$$

### Step 2: The Hamiltonian

The spin observable along $z$ is $\tilde{S}_z = \frac{\hbar}{2}\,i \vec e_z$. The Hamiltonian is therefore the Hermitian element of $\mathbb{M}_+$

$$
\tilde{H} = -\gamma B_0 \tilde{S}_z = -\frac{\hbar\omega_L}{2}\,i \vec e_z,
$$

with $\omega_L = \gamma B_0$.

### Step 3: The evolution

The evolution operator is the unit-norm biquaternion

$$
\tilde{U}(t') = \exp\!\left(-i\tilde{H}t'/\hbar\right) = \exp\!\left(-\frac{\omega_L t'}{2}\,\vec e_z\right) = \cos\!\left(\frac{\omega_L t'}{2}\right)e_t - \sin\!\left(\frac{\omega_L t'}{2}\right)\vec e_z,
$$

where we have used the identity $\exp(\theta\,\vec e_z) = \cos\theta\,e_t + \sin\theta\,\vec e_z$, which follows from $\vec e_z^2 = -e_t$, and set $\theta = -\omega_L t'/2$.

The evolved state is

$$
\tilde{Ϛ}(t') = \tilde{U}(t')\,\tilde\Pi_x\,\tilde{U}(t')^{*}.
$$

Computing the product, using $\tilde{U}(t')^{*} = \tilde{U}^{\natural}(t') = \cos(\omega_L t'/2)\,e_t + \sin(\omega_L t'/2)\,\vec e_z$ (since $\tilde{U}$ is a real quaternion), gives

$$
\tilde{Ϛ}(t') = \tfrac{1}{2}\left(e_t + i\cos(\omega_L t')\,\vec e_x - i\sin(\omega_L t')\,\vec e_y\right).
$$

### Step 4: The expectation value

The expectation value of the spin along $x$ is given by the normalised Hermitian form

$$
\langle\tilde{S}_x\rangle(t') = \frac{\langle\tilde{Ϛ}(t'),\tilde{S}_x\rangle_{*}}{\langle\tilde{Ϛ}(t'),e_t\rangle_{*}}
= \frac{\mathrm{Sc}\bigl(\tilde{Ϛ}(t')\,\tilde{S}_x^{*}\bigr)}{\mathrm{Sc}\bigl(\tilde{Ϛ}(t')\bigr)}
= 2\,\mathrm{Sc}\!\left(\tilde{Ϛ}(t')\,\tilde{S}_x\right),
$$

whose trace reading at normalisation is $\operatorname{Tr}(\tilde{Ϛ}(t')\tilde{S}_x)=2\,\mathrm{Sc}(\tilde{Ϛ}(t')\tilde{S}_x)$, with $\tilde{S}_x = \frac{\hbar}{2}\,i \vec e_x$. Computing the product

$$
\tilde{Ϛ}(t')\,\tilde{S}_x = \frac{\hbar}{4}\left(i \vec e_x + \cos(\omega_L t')\,e_t - \sin(\omega_L t')\,\vec e_z\right),
$$

the scalar part is $\frac{\hbar}{4}\cos(\omega_L t')$. Applying the Hermitian form, with the trace reading last,

$$
\boxed{\;\langle\tilde{S}_x\rangle(t') = \frac{\hbar}{2}\cos(\omega_L t')\;}.
$$

## Limiting Cases

Both formulations give the same result, and both give the same limits:

- **$t' = 0$** (initial time): $\langle S_x\rangle = \hbar/2$, as expected since the state is spin-up along $x$.
- **$\omega_L t' = \pi/2$** (quarter period): $\langle S_x\rangle = 0$.
- **$\omega_L t' = \pi$** (half period): $\langle S_x\rangle = -\hbar/2$, the state has precessed to spin-down along $x$.
- **$\omega_L t' = 2\pi$** (full period): $\langle S_x\rangle = \hbar/2$, the state has returned to its initial orientation.

The spin precesses in the $xy$-plane with angular frequency $\omega_L$, as expected for Larmor precession.

## What the Biquaternion Solution Illustrates

**1. The Hamiltonian is a Hermitian element of $\mathbb{M}_+$.** The observable $\tilde{S}_z = \frac{\hbar}{2}i \vec e_z$ is an element of $\mathbb{M}_+$, and the Hamiltonian $\tilde{H} = -\gamma B_0 \tilde{S}_z$ inherits this property. The Hamiltonian is a **Hermitian element of the same subspace** as the observables and the states.

**2. The evolution operator is a unit-norm biquaternion.** The exponential $\tilde{U}(t') = \exp(-i\tilde{H}t'/\hbar)$ is a unit-norm element of $\mathbb{B}$, lying in the real quaternion subspace $\mathbb{H}_\mathbb{B}$ for this particular Hamiltonian (because $\tilde{H}$ is proportional to $i \vec e_z$, and the exponential of $\vec e_z$ is a real quaternion). The evolution is a **rotor** in the sense of geometric algebra.

**3. The state evolves by rotor conjugation.** The evolved state is $\tilde{Ϛ}(t') = \tilde{U}(t')\tilde{Ϛ}(0)\tilde{U}(t')^{*}$. This is the standard form of the von Neumann evolution, expressed as a **rotor conjugation** on the algebra. The evolution is automatically unitary: $\tilde{U}\tilde{U}^{*} = e_t$ is preserved by the exponential form.

**4. The precession is a rotation of the Bloch vector.** The evolved state has the form $\tilde{Ϛ}(t') = \frac{1}{2}(e_t + i\vec r(t'))$ with

$$
\boxed{\;\vec r(t') = \cos(\omega_L t')\,\vec e_x - \sin(\omega_L t')\,\vec e_y\;}.
$$

This is a **unit vector rotating** in the $xy$-plane with angular frequency $\omega_L$. The Bloch vector precesses about the $z$-axis, which is the direction of the magnetic field. The precession is the algebraic content of Larmor precession.

**5. The expectation value is the normalised Hermitian form, read through the trace last.** As in Exercise: Measuring Spin Along an Arbitrary Direction, the expectation value is

$$
\langle\tilde{S}_x\rangle(t') = \frac{\langle\tilde{Ϛ}(t'),\tilde{S}_x\rangle_{*}}{\langle\tilde{Ϛ}(t'),e_t\rangle_{*}} = 2\,\mathrm{Sc}\!\left(\tilde{Ϛ}(t')\,\tilde{S}_x\right),
$$

whose trace reading is $\operatorname{Tr}(\tilde{Ϛ}(t')\tilde{S}_x)$, the same Hermitian form that gives the Born probabilities. Both the Born rule and the expectation values of observables are instances of the same Hermitian form on $\mathbb{M}_+$.

**6. The result agrees with the standard formulation.** This is not surprising, because the two formulations are the same mathematics in different notation: $\mathbb{B} \cong M_2(\mathbb{C})$, and the biquaternion evolution $\tilde{U}(t') = \exp(-i\tilde{H}t'/\hbar)$ corresponds exactly to the standard matrix evolution $T(t') = \exp(-iHt'/\hbar)$ under the isomorphism. But seeing the same result emerge from the algebra is a useful sanity check on the framework, and it illustrates the structural claim of the companion articles: **the dynamics of a qubit is contained in the Hermitian subspace $\mathbb{M}_+$, with the evolution given by rotor conjugation by a unit-norm biquaternion.**

## Comparison with Exercise: Measuring Spin Along an Arbitrary Direction

| | Measuring Spin Along an Arbitrary Direction | Spin Precession in a Magnetic Field |
|---|---|---|
| Physical process | Measurement | Time evolution |
| Structural object | Idempotent (state) + idempotent (projector) | Idempotent (state) + unitary (evolution) |
| Rule used | Trace reading at normalisation (Born rule) | Trace formula (expectation value) |
| Result | $\cos^2(\theta/2)$ | $(\hbar/2)\cos(\omega_L t')$ |

These two exercises illustrate the two fundamental operations of the quantum formalism: **measurement** (Exercise: Measuring Spin Along an Arbitrary Direction) and **evolution** (Exercise: Spin Precession in a Magnetic Field). In both cases, the biquaternion framework expresses the operation as an algebraic manipulation of the elements of $\mathbb{M}_+$ and $\mathbb{H}_\mathbb{B}$.

## Summary

We have solved a second exercise in quantum physics — the Larmor precession of a spin in a magnetic field — in two parallel presentations.

In the **standard formulation**, the solution proceeds through ket vectors, Pauli matrices, the Hamiltonian, the evolution operator, and the expectation value, giving $\langle S_x\rangle(t') = \frac{\hbar}{2}\cos(\omega_L t')$.

In the **biquaternion formulation**, the solution proceeds through the idempotent $\tilde\Pi_x$, the Hermitian Hamiltonian $\tilde{H}$, the unit-norm evolution biquaternion $\tilde{U}(t')$, the evolved state $\tilde{Ϛ}(t')$, and the trace formula, giving the same result.

The two formulations agree, as they must. The biquaternion formulation makes explicit the algebraic structure of the evolution: the Hamiltonian is a Hermitian element of $\mathbb{M}_+$, the evolution operator is a unit-norm biquaternion, the evolved state is the rotor conjugate of the initial state, and the expectation value is the normalised Hermitian form, read through the trace.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $\mathbb{M}_+$ | Hermitian subspace (states, observables, Hamiltonians) |
| $\mathbb{H}_\mathbb{B}$ | Quaternion subspace (home of the real rotation rotors) |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_k^2 = -e_t$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\boldsymbol{\sigma} = (\sigma_1, \sigma_2, \sigma_3)$ | Pauli matrices |
| $\gamma$ | Gyromagnetic ratio |
| $\omega_L = \gamma B_0$ | Larmor frequency |
| $\tilde\Pi_x = \tfrac{1}{2}(e_t + i\vec e_x)$ | Spin-up state along $x$ |
| $\tilde{S}_x = \tfrac{\hbar}{2} i\vec e_x$ | Spin observable along $x$ |
| $\tilde{H} = -\tfrac{\hbar\omega_L}{2} i\vec e_z$ | Hamiltonian |
| $\tilde{U}(t') = \exp(-i\tilde{H}t'/\hbar)$ | Evolution biquaternion |
| $\tilde{Ϛ}(t') = \tilde{U}(t')\tilde{Ϛ}(0)\tilde{U}(t')^{*}$ | Evolved state |
| $\langle\tilde{S}_x\rangle(t') = \mathrm{Tr}(\tilde{Ϛ}(t')\tilde{S}_x)$ | Expectation value |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural}$ | the general quaternionic bilinear form, $\mathrm{Sc}(\tilde{Q}_1^{\natural}\tilde{Q}_2)$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{\natural}=\langle\tilde{Q}_2\rangle_{\natural}$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{*}=\sum_\mu\lvert Q_{2\mu}\rvert^{2}$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ |

## Further Reading

- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford, 1930), for the standard formulation of spin dynamics.
- J. J. Sakurai and Jim Napolitano, *Modern Quantum Mechanics* (Pearson, 2017), for the standard textbook treatment of Larmor precession.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the Bloch sphere and the evolution of qubits.
- The companion articles of this series: [Quantum Physics in Biquaternionic Form](quantum-physics-in-biquaternionic-form.html), [Spin-1/2 Quantum Physics in Biquaternionic Form](spin-1-2-quantum-physics-in-biquaternionic-form.html), and [Exercise: Measuring Spin Along an Arbitrary Direction](exercise-measuring-spin-along-an-arbitrary-direction.html).

