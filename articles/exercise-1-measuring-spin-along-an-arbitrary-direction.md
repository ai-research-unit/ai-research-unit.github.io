
# __Exercise 1: Measuring Spin Along an Arbitrary Direction__

## Introduction

This article is the first in a series of **worked exercises** that illustrate quantum mechanics in two parallel presentations: the standard Hilbert-space formulation, and the biquaternion formulation developed in the companion articles. The goal is not to derive new physics, but to give the reader a concrete, computationally explicit demonstration of the correspondence between the two formalisms.

Each exercise in the series is solved twice: first in the standard way, then in the biquaternion way. The results agree, as they must: the two formulations are the same mathematics in different notation. The pedagogical value is in seeing the same physical result emerge from both frameworks, and in observing how the algebraic structure of the biquaternion framework handles the objects of quantum mechanics.

To keep the two solutions strictly parallel, each is presented in the same four steps: **the state**, **the measurement operator**, **the outcome object**, and **the probability**. The final result is stated in the same form in both solutions.

The conventions are those of the companion articles. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with the Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$. The quaternion units are $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$, and $i$ is the scalar imaginary. The trace of an element of $\mathbb{M}_+$ is twice its scalar part: $\mathrm{Tr}(\tilde{H}) = 2\,\mathrm{Sc}(\tilde{H})$.

## The Exercise

A spin-$\tfrac{1}{2}$ particle is prepared in the **spin-up state along the $z$-axis**. We measure the spin along a direction $\hat{n}$ that makes an angle $\theta$ with the $z$-axis, in the $xz$-plane. What is the probability of finding the particle spin-up along $\hat{n}$?

This is the canonical "rotate the Stern–Gerlach apparatus" exercise. It involves states, observables, and the Born rule, but no dynamics and no interactions.

## Solution in the Standard Formulation

### Step 1: The state

The spin-up state along the $z$-axis is the eigenvector of the Pauli matrix $\sigma_3$ with eigenvalue $+1$:

$$
|+z\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}.
$$

### Step 2: The measurement operator

The measurement is along the direction

$$
\hat{n} = (\sin\theta,\, 0,\, \cos\theta).
$$

The measurement operator is the spin projection along $\hat{n}$:

$$
\hat{n}\cdot\mathbf{S} = \frac{\hbar}{2}\,\hat{n}\cdot\boldsymbol{\sigma} = \frac{\hbar}{2}\begin{pmatrix} \cos\theta & \sin\theta \\ \sin\theta & -\cos\theta \end{pmatrix},
$$

where $\boldsymbol{\sigma} = (\sigma_1, \sigma_2, \sigma_3)$ are the Pauli matrices.

### Step 3: The eigenstate for the outcome

The eigenvalue-$+1$ eigenvector of $\hat{n}\cdot\mathbf{S}$, up to a global phase, is

$$
|+n\rangle = \begin{pmatrix} \cos(\theta/2) \\ \sin(\theta/2) \end{pmatrix}.
$$

### Step 4: The probability

The probability of finding the particle spin-up along $\hat{n}$, given that it was prepared spin-up along $z$, is given by the Born rule:

$$
p_+ = \bigl|\langle +n \mid +z\rangle\bigr|^2.
$$

Computing the inner product:

$$
\langle +n \mid +z \rangle = \cos(\theta/2).
$$

Therefore

$$
p_+ = \bigl|\cos(\theta/2)\bigr|^2 = \cos^2(\theta/2) = \frac{1 + \cos\theta}{2}.
$$

## Solution in the Biquaternion Formulation

### Step 1: The state

In the biquaternion framework, a pure spin state is an **idempotent** of the Hermitian subspace $\mathbb{M}_+$, of the form

$$
P(\hat{m}) = \tfrac{1}{2}\left(e_0 + i\hat{m}\right),
$$

where $\hat{m}$ is a unit pure real quaternion (a unit vector in $\mathbb{R}^3$). The spin-up state along $z$ corresponds to

$$
P_z = \tfrac{1}{2}\left(e_0 + i e_3\right).
$$

### Step 2: The measurement operator

The same measurement direction $\hat{n} = \sin\theta\, e_1 + \cos\theta\, e_3$ is now written as a unit pure real quaternion. The measurement operator is the Hermitian element of $\mathbb{M}_+$ corresponding to the spin projection along $\hat{n}$:

$$
\tilde{H} = \frac{\hbar}{2}\, i\hat{n}.
$$

### Step 3: The projector for the outcome

The projector onto the eigenvalue-$+1$ eigenstate of $\tilde{H}$ is the idempotent

$$
P_n = \tfrac{1}{2}\left(e_0 + i\hat{n}\right).
$$

### Step 4: The probability

The probability of finding the particle spin-up along $\hat{n}$, given that it was prepared spin-up along $z$, is given by the **trace formula**:

$$
p_+ = \mathrm{Tr}\!\left(P_n \circ P_z\right) = 2\,\mathrm{Sc}\!\left(P_n \circ P_z\right),
$$

where $\circ$ is the biquaternion product.

Computing the product:

$$
P_n \circ P_z = \tfrac{1}{4}\left(e_0 + i\hat{n}\right)\left(e_0 + i e_3\right) = \tfrac{1}{4}\left[e_0 + i e_3 + i\hat{n} - \hat{n}\,e_3\right].
$$

Evaluating $\hat{n}\,e_3$, using $\hat{n} = \sin\theta\, e_1 + \cos\theta\, e_3$ and the quaternion product rules $e_1 e_3 = -e_2$, $e_3 e_3 = -e_0$:

$$
\hat{n}\,e_3 = \sin\theta\, e_1 e_3 + \cos\theta\, e_3 e_3 = -\sin\theta\, e_2 - \cos\theta\, e_0.
$$

Substituting:

$$
P_n \circ P_z = \tfrac{1}{4}\left[e_0 + i e_3 + i\hat{n} + \sin\theta\, e_2 + \cos\theta\, e_0\right].
$$

The scalar part (coefficient of $e_0$) is $\tfrac{1}{4}\left(1 + \cos\theta\right)$; the other terms $i e_3$, $i\hat{n}$, and $\sin\theta\, e_2$ are vector terms with vanishing coefficient of $e_0$.

Applying the trace formula:

$$
p_+ = 2 \cdot \tfrac{1}{4}\left(1 + \cos\theta\right) = \cos^2(\theta/2) = \frac{1 + \cos\theta}{2}.
$$

## Limiting Cases

Both formulations give the same result, and both give the same limits:

- **$\theta = 0$** (measurement along $z$): $p_+ = \cos^2(0) = 1$.
- **$\theta = \pi/2$** (measurement along $x$): $p_+ = \cos^2(\pi/4) = 1/2$.
- **$\theta = \pi$** (measurement along $-z$): $p_+ = \cos^2(\pi/2) = 0$.

These agree with the physical expectation.

## What the Biquaternion Solution Illustrates

**1. States and observables are elements of the same subspace.** The state $P_z$ and the outcome projector $P_n$ are both idempotents of $\mathbb{M}_+$. The entire calculation involves only the algebra of the biquaternion units and the extraction of the scalar part.

**2. The Born rule is the trace formula.** The probability is $p_+ = \mathrm{Tr}(P_n \circ P_z) = 2\,\mathrm{Sc}(P_n \circ P_z)$. This is not an additional postulate: it is the natural pairing between two elements of the algebra, given by the trace. It is the same formula as $p_+ = \mathrm{Tr}(\rho_n \rho_z)$ for density matrices, applied to the idempotents that represent the pure states.

**3. No complex vectors are needed.** In the standard solution, the calculation involves complex column vectors and their inner product. In the biquaternion solution, it involves only the algebra of $\mathbb{B}$: products of quaternion units, extraction of the scalar part, application of the trace formula. The complex structure is absorbed into the scalar imaginary $i$ of the algebra.

**4. The geometry enters through the algebra.** The angle $\theta$ enters through the unit vector $\hat{n} = \sin\theta\, e_1 + \cos\theta\, e_3$ that parametrizes the measurement direction. The result depends on $\theta$ only through the scalar product $\hat{n}\cdot e_3 = \cos\theta$, which appears in the trace formula through the product $\hat{n}\,e_3$. The geometry of the Bloch sphere is encoded in the multiplication rules of the algebra.

**5. The result agrees with the standard formulation.** This is not surprising, because the two formulations are the same mathematics in different notation: $\mathbb{B} \cong M_2(\mathbb{C})$, and the idempotent $P(\hat{n}) = \tfrac{1}{2}(e_0 + i\hat{n})$ corresponds exactly to the rank-one projector $\tfrac{1}{2}(I + \hat{n}\cdot\boldsymbol{\sigma})$. But seeing the same result emerge from the algebra is a useful sanity check on the biquaternion framework.

## Extension: The Expectation Value of the Spin

The same pattern applies to the calculation of the **expectation value of the spin along $\hat{n}$** in the state $|+z\rangle$. The two formulations are again strictly parallel.

### Standard formulation

$$
\langle \hat{n}\cdot\mathbf{S}\rangle_{+z} = \langle +z|\hat{n}\cdot\mathbf{S}|+z\rangle = \frac{\hbar}{2}\cos\theta.
$$

### Biquaternion formulation

The observable is $\tilde{H} = \tfrac{\hbar}{2} i\hat{n}$ and the state is $P_z = \tfrac{1}{2}(e_0 + i e_3)$. The expectation value is given by the trace formula:

$$
\langle \tilde{H}\rangle_{P_z} = \mathrm{Tr}(P_z \circ \tilde{H}) = 2\,\mathrm{Sc}(P_z \circ \tilde{H}).
$$

Computing the product:

$$
P_z \circ \tilde{H} = \tfrac{1}{2}(e_0 + i e_3)\cdot\tfrac{\hbar}{2} i\hat{n} = \tfrac{\hbar}{4}\left(i\hat{n} - e_3 \hat{n}\right).
$$

Evaluating $e_3 \hat{n}$, using $e_3 e_1 = e_2$ and $e_3 e_3 = -e_0$:

$$
e_3 \hat{n} = e_3(\sin\theta\, e_1 + \cos\theta\, e_3) = \sin\theta\, e_2 - \cos\theta\, e_0.
$$

Substituting:

$$
P_z \circ \tilde{H} = \tfrac{\hbar}{4}\left(i\hat{n} - \sin\theta\, e_2 + \cos\theta\, e_0\right).
$$

The scalar part is $\tfrac{\hbar}{4}\cos\theta$. Therefore

$$
\langle \tilde{H}\rangle_{P_z} = 2 \cdot \tfrac{\hbar}{4}\cos\theta = \frac{\hbar}{2}\cos\theta.
$$

Both formulations give the same result.

## Summary

We have solved a simple exercise in quantum mechanics — the probability of measuring spin-up along an arbitrary direction, given a spin-up state along $z$ — in two parallel presentations.

In the **standard formulation**, the solution proceeds through ket vectors, Pauli matrices, and the Born rule in the form $p_+ = |\langle +n | +z\rangle|^2$, giving $p_+ = \cos^2(\theta/2) = (1 + \cos\theta)/2$.

In the **biquaternion formulation**, the solution proceeds through the idempotents of $\mathbb{M}_+$ and the trace formula $p_+ = \mathrm{Tr}(P_n \circ P_z)$, giving the same result.

The two formulations agree, as they must. The biquaternion formulation makes explicit the algebraic structure of the qubit: states and observables are elements of the same subspace, the Born rule is the natural pairing given by the trace, and the geometry of the Bloch sphere is encoded in the multiplication rules of the algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $\mathbb{M}_+$ | Hermitian subspace (states, observables) |
| $\mathbb{M}_-$ | Anti-Hermitian subspace (generators) |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\boldsymbol{\sigma} = (\sigma_1, \sigma_2, \sigma_3)$ | Pauli matrices |
| $P(\hat{m}) = \tfrac{1}{2}(e_0 + i\hat{m})$ | Pure-state idempotent |
| $\tilde{H} = h_0 e_0 + i\mathbf{h}$ | Hermitian element (observable) |
| $\mathrm{Tr}(\tilde{H}) = 2\,\mathrm{Sc}(\tilde{H})$ | Trace of an element of $\mathbb{M}_+$ |
| $p_+ = \mathrm{Tr}(P_n \circ P_z)$ | Born rule in biquaternion form |

## Further Reading

- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford, 1930), for the standard formulation of spin-$\tfrac{1}{2}$.
- J. J. Sakurai and Jim Napolitano, *Modern Quantum Mechanics* (Pearson, 2017), for the standard textbook treatment of the spin-$\tfrac{1}{2}$ measurement.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the Bloch sphere and the Born rule for qubits.
- The companion articles of this series: *Quantum Mechanics in Biquaternionic Form*, *Spin-1/2 Quantum Mechanics in Biquaternionic Form*, and *$\mathbb{M}_+$ as the Informational Space*.

