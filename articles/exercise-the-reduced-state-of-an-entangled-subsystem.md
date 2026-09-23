# __Exercise: The Reduced State of an Entangled Subsystem__

## Introduction

This article is one of a series of **worked exercises** that illustrate quantum mechanics in two parallel presentations: the standard Hilbert-space formulation, and the biquaternion formulation developed in the companion articles. The goal is not to derive new physics, but to give the reader a concrete, computationally explicit demonstration of the correspondence between the two formalisms.

Each exercise in the series is solved twice: first in the standard way, then in the biquaternion way. The results agree, as they must: the two formulations are the same mathematics in different notation. To keep the two solutions strictly parallel, each is presented in the same steps, and the final result is stated in the same form.

The earlier exercises treated single measurements, time evolution, successive measurements, and entangled measurements of two spins. This exercise treats a complementary aspect of entanglement: the **state of one subsystem** when the joint system is in an entangled state. This introduces the **reduced density matrix**, and with it the concept of a **mixed state**.

The conventions are those of the companion articles. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with the Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$. The quaternion units are $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$, and $i$ is the scalar imaginary. The trace of an element of $\mathbb{M}_+$ is twice its scalar part: $\mathrm{Tr}(\tilde{H}) = 2\,\mathrm{Sc}(\tilde{H})$. The two-qubit state space is the tensor product $\mathbb{B}\otimes\mathbb{B}$, isomorphic to $M_4(\mathbb{C})$. Throughout, $\log$ denotes the natural logarithm.

## The Exercise

Two spin-$\tfrac{1}{2}$ particles are prepared in the **singlet state**

$$
|\Psi^-\rangle = \frac{1}{\sqrt{2}}\left(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle\right).
$$

We measure particle 1 alone, along any direction. What is the **state of particle 1**, ignoring particle 2?

The answer, as we shall see, is that the state of particle 1 is the **maximally mixed state** — a mixed state, not a pure state. This is the quantum-mechanical signature of entanglement: the information about particle 1 is not contained in any pure state, but is distributed between the two particles.

## Solution in the Standard Formulation

### Step 1: The joint state

The singlet state is the antisymmetric combination of the two spin states in the 4-dimensional Hilbert space $\mathbb{C}^2\otimes\mathbb{C}^2$:

$$
|\Psi^-\rangle = \frac{1}{\sqrt{2}}\left(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle\right).
$$

The joint state is the rank-one projector

$$
\rho = |\Psi^-\rangle\langle\Psi^-| = \frac{1}{2}\Bigl(|\uparrow\downarrow\rangle\langle\uparrow\downarrow| - |\uparrow\downarrow\rangle\langle\downarrow\uparrow| - |\downarrow\uparrow\rangle\langle\uparrow\downarrow| + |\downarrow\uparrow\rangle\langle\downarrow\uparrow|\Bigr).
$$

### Step 2: The reduced state

The state of particle 1 alone is the **reduced density matrix**, obtained by taking the **partial trace** over particle 2:

$$
\rho_1 = \mathrm{Tr}_2(\rho).
$$

The partial trace over the second factor is defined on the tensor product by

$$
\mathrm{Tr}_2(A\otimes B) = A \cdot \mathrm{Tr}(B),
$$

and extended by linearity.

### Step 3: The computation

We compute the partial trace term by term.

**First diagonal term.** $\frac{1}{2}|\uparrow\downarrow\rangle\langle\uparrow\downarrow| = \frac{1}{2}|\uparrow\rangle\langle\uparrow| \otimes |\downarrow\rangle\langle\downarrow|$, so

$$
\mathrm{Tr}_2\!\left(\frac{1}{2}|\uparrow\rangle\langle\uparrow| \otimes |\downarrow\rangle\langle\downarrow|\right) = \frac{1}{2}|\uparrow\rangle\langle\uparrow| \cdot \mathrm{Tr}(|\downarrow\rangle\langle\downarrow|) = \frac{1}{2}|\uparrow\rangle\langle\uparrow|.
$$

**Second diagonal term.** $\frac{1}{2}|\downarrow\uparrow\rangle\langle\downarrow\uparrow| = \frac{1}{2}|\downarrow\rangle\langle\downarrow| \otimes |\uparrow\rangle\langle\uparrow|$, so

$$
\mathrm{Tr}_2\!\left(\frac{1}{2}|\downarrow\rangle\langle\downarrow| \otimes |\uparrow\rangle\langle\uparrow|\right) = \frac{1}{2}|\downarrow\rangle\langle\downarrow|.
$$

**First cross term.** $\frac{1}{2}|\uparrow\downarrow\rangle\langle\downarrow\uparrow| = \frac{1}{2}|\uparrow\rangle\langle\downarrow| \otimes |\downarrow\rangle\langle\uparrow|$, so

$$
\mathrm{Tr}_2\!\left(\frac{1}{2}|\uparrow\rangle\langle\downarrow| \otimes |\downarrow\rangle\langle\uparrow|\right) = \frac{1}{2}|\uparrow\rangle\langle\downarrow| \cdot \mathrm{Tr}(|\downarrow\rangle\langle\uparrow|) = \frac{1}{2}|\uparrow\rangle\langle\downarrow| \cdot \langle\uparrow|\downarrow\rangle = 0,
$$

since $|\uparrow\rangle$ and $|\downarrow\rangle$ are orthogonal.

**Second cross term.** Similarly,

$$
\mathrm{Tr}_2\!\left(\frac{1}{2}|\downarrow\rangle\langle\uparrow| \otimes |\uparrow\rangle\langle\downarrow|\right) = \frac{1}{2}|\downarrow\rangle\langle\uparrow| \cdot \langle\downarrow|\uparrow\rangle = 0.
$$

Summing the four contributions,

$$
\rho_1 = \frac{1}{2}|\uparrow\rangle\langle\uparrow| + \frac{1}{2}|\downarrow\rangle\langle\downarrow| = \frac{1}{2} I.
$$

### Step 4: The result

$$
\rho_1 = \frac{1}{2} I.
$$

This is the **maximally mixed state** of a qubit. Its purity and von Neumann entropy are

$$
\mathrm{Tr}(\rho_1^2) = \frac{1}{2}, \qquad S(\rho_1) = -\mathrm{Tr}(\rho_1 \log \rho_1) = \log 2.
$$

The reduced state is not pure: it is a mixed state, and it carries the maximum possible entropy for a qubit.

## Solution in the Biquaternion Formulation

### Step 1: The joint state

In the biquaternion framework, a single-qubit pure state is an idempotent of $\mathbb{M}_+$, of the form $P(\hat{m}) = \tfrac{1}{2}(e_0 + i\hat{m})$. The two-qubit state space is the tensor product $\mathbb{B}\otimes\mathbb{B}$, and the singlet state corresponds to the idempotent

$$
P_{\mathrm{singlet}} = \frac{1}{4}\left(e_0\otimes e_0 + e_1\otimes e_1 + e_2\otimes e_2 + e_3\otimes e_3\right).
$$

### Step 2: The reduced state

The state of particle 1 alone is the **partial trace** of $P_{\mathrm{singlet}}$ over the second factor:

$$
\rho_1 = \mathrm{Tr}_2(P_{\mathrm{singlet}}).
$$

The partial trace on $\mathbb{B}\otimes\mathbb{B}$ is defined on the elementary tensor products by

$$
\mathrm{Tr}_2(a\otimes b) = a \cdot \mathrm{Tr}_\mathbb{B}(b),
$$

and extended by linearity.

### Step 3: The computation

We compute the partial trace term by term.

**First term.** $\frac{1}{4}e_0\otimes e_0$ contributes

$$
\mathrm{Tr}_2\!\left(\frac{1}{4}e_0\otimes e_0\right) = \frac{1}{4}e_0 \cdot \mathrm{Tr}_\mathbb{B}(e_0) = \frac{1}{4}e_0 \cdot 2 = \frac{1}{2}e_0.
$$

**Remaining terms.** For $k = 1, 2, 3$, the term $\frac{1}{4}e_k\otimes e_k$ contributes

$$
\mathrm{Tr}_2\!\left(\frac{1}{4}e_k\otimes e_k\right) = \frac{1}{4}e_k \cdot \mathrm{Tr}_\mathbb{B}(e_k) = \frac{1}{4}e_k \cdot 0 = 0,
$$

since $\mathrm{Tr}_\mathbb{B}(e_k) = 2\,\mathrm{Sc}(e_k) = 0$ for the pure quaternion units.

Summing the contributions,

$$
\rho_1 = \frac{1}{2}e_0.
$$

### Step 4: The result

$$
\rho_1 = \frac{1}{2}e_0.
$$

This is the maximally mixed state of a qubit, expressed in biquaternion form. Its purity and von Neumann entropy are

$$
\mathrm{Tr}(\rho_1^2) = \mathrm{Tr}\!\left(\frac{1}{4}e_0\right) = \frac{1}{4}\cdot 2 = \frac{1}{2},
$$

$$
S(\rho_1) = -\mathrm{Tr}(\rho_1 \log \rho_1) = -\mathrm{Tr}\!\left(\frac{1}{2}e_0 \cdot \log\tfrac{1}{2}e_0\right) = -\log\tfrac{1}{2} \cdot \mathrm{Tr}\!\left(\frac{1}{2}e_0\right) = \log 2.
$$

The same values as in the standard formulation.

## Properties of the Reduced State

The reduced state $\rho_1 = \frac{1}{2} e_0$ has three notable properties.

**1. It is a mixed state.** In the biquaternion framework, a general state of $\mathbb{M}_+$ has the form $\rho = \tfrac{1}{2}(e_0 + i\mathbf{r})$ with $|\mathbf{r}| \leq 1$. The pure states are the ones with $|\mathbf{r}| = 1$ (the idempotents), and the maximally mixed state is the one with $\mathbf{r} = 0$. The reduced state $\rho_1 = \frac{1}{2} e_0$ corresponds to $\mathbf{r} = 0$, i.e., the center of the Bloch ball. It is a mixed state, at the maximal distance from the pure states.

**2. It is invariant under all unitary transformations.** Under a rotor conjugation $\rho_1 \mapsto \tilde{U}\rho_1\tilde{U}^\dagger$ with $\tilde{U}\tilde{U}^\dagger = e_0$, the reduced state is unchanged:

$$
\tilde{U}\left(\tfrac{1}{2}e_0\right)\tilde{U}^\dagger = \tfrac{1}{2}\tilde{U}\tilde{U}^\dagger = \tfrac{1}{2}e_0.
$$

This invariance is a specific property of the maximally mixed state.

**3. It is the state of maximum ignorance.** The von Neumann entropy is $\log 2$ (in natural units), the maximum possible for a qubit. This reflects that the reduced state contains no information about which pure state particle 1 is in, because the information is stored entirely in the correlations with particle 2.

## Comparison with a Product State

It is instructive to compare with a product state. Consider the two-qubit state

$$
|\uparrow\uparrow\rangle = |\uparrow\rangle\otimes|\uparrow\rangle,
$$

which is a product state (not entangled). The reduced state of particle 1 is

$$
\rho_1^{\mathrm{prod}} = \mathrm{Tr}_2\!\left(|\uparrow\rangle\langle\uparrow| \otimes |\uparrow\rangle\langle\uparrow|\right) = |\uparrow\rangle\langle\uparrow| \cdot \mathrm{Tr}(|\uparrow\rangle\langle\uparrow|) = |\uparrow\rangle\langle\uparrow|.
$$

In biquaternion form, the joint state is

$$
P_{\mathrm{prod}} = P_+(\hat{z}) \otimes P_+(\hat{z}),
$$

with $P_+(\hat{z}) = \tfrac{1}{2}(e_0 + ie_3)$. Computing the partial trace,

$$
\rho_1^{\mathrm{prod}} = \mathrm{Tr}_2(P_{\mathrm{prod}}) = P_+(\hat{z}) \cdot \mathrm{Tr}_\mathbb{B}(P_+(\hat{z})) = P_+(\hat{z}) \cdot 1 = P_+(\hat{z}),
$$

using $\mathrm{Tr}_\mathbb{B}(P_+(\hat{z})) = 1$ for an idempotent of trace one.

So the reduced state is the pure state $P_+(\hat{z}) = \tfrac{1}{2}(e_0 + ie_3)$, which is an idempotent with Bloch vector $\mathbf{r} = e_3$ and purity $1$. The purity and entropy are

$$
\mathrm{Tr}((\rho_1^{\mathrm{prod}})^2) = 1, \qquad S(\rho_1^{\mathrm{prod}}) = 0.
$$

This is in sharp contrast with the singlet case.

| State | Reduced state $\rho_1$ | Purity | Entropy |
|---|---|---|---|
| Singlet $|\Psi^-\rangle$ | $\frac{1}{2}e_0$ (mixed) | $\frac{1}{2}$ | $\log 2$ |
| Product $|\uparrow\uparrow\rangle$ | $\frac{1}{2}(e_0 + ie_3)$ (pure) | $1$ | $0$ |

The contrast is the operational signature of entanglement: **product states have pure reduced states; entangled states have mixed reduced states**. The more entangled the joint state, the more mixed the reduced state.

## What the Biquaternion Solution Illustrates

**1. The reduced state is obtained by a partial trace.** The partial trace $\mathrm{Tr}_2$ is a linear map $\mathbb{B}\otimes\mathbb{B} \to \mathbb{B}$, defined on elementary tensors by $\mathrm{Tr}_2(a\otimes b) = a\,\mathrm{Tr}_\mathbb{B}(b)$. This is the biquaternion form of the standard partial trace.

**2. The reduced state of an entangled subsystem is mixed.** The biquaternion framework represents pure states as idempotents of $\mathbb{M}_+$ and mixed states as general positive trace-one elements. The reduced state $\frac{1}{2} e_0$ is not idempotent; it is a genuine mixed state, with $\mathbf{r} = 0$.

**3. The entanglement is encoded in the tensor-product structure.** The singlet idempotent $P_{\mathrm{singlet}}$ has non-trivial components in the tensor-product terms $e_k\otimes e_k$ with $k \neq 0$, and none of the form $e_k\otimes e_0$. The entangled terms are traceless in the second factor, so they drop out of the partial trace, and only the $e_0\otimes e_0$ term survives, giving the maximally mixed reduced state. In a product state the terms $e_k\otimes e_0$ are present, and they carry the pure reduced state.

**4. The purity and entropy are natural functions on $\mathbb{M}_+$.** Both the purity $\mathrm{Tr}(\rho_1^2)$ and the entropy $-\mathrm{Tr}(\rho_1\log\rho_1)$ are expressed in terms of the trace on $\mathbb{B}$. The reduced state's mixedness is measured by these functions, and for the singlet the reduced state is maximally mixed.

**5. The result agrees with the standard formulation.** The two formulations give the same reduced state $\rho_1 = \frac{1}{2} I$, the same purity $\frac{1}{2}$, and the same entropy $\log 2$. The biquaternion framework expresses these results through the algebra of $\mathbb{B}\otimes\mathbb{B}$ and the trace on $\mathbb{B}$.

## Comparison with Exercises: Measuring Spin Along an Arbitrary Direction, Spin Precession in a Magnetic Field, Successive Measurements of Spin and Two Spins in the Singlet State

| | Measuring Spin Along an Arbitrary Direction | Spin Precession in a Magnetic Field | Successive Measurements of Spin | Two Spins in the Singlet State | Reduced State of an Entangled Subsystem |
|---|---|---|---|---|---|
| System | One qubit | One qubit | One qubit | Two qubits | Two qubits |
| Physical process | Measurement | Evolution | Successive measurements | Entangled measurement | Reduced state |
| Structural object | Idempotent + idempotent | Idempotent + unitary | Sequence of idempotents | State in $\mathbb{B}\otimes\mathbb{B}$ | Partial trace of a state |
| Rule used | Trace formula | Trace formula + rotor conjugation | Product of trace formulas | Tensor-product trace formula | Partial trace + trace formula |
| Result | $\cos^2(\theta/2)$ | $(\hbar/2)\cos(\omega_L t)$ | $\cos^2(\theta_1/2)\cos^2((\theta_2-\theta_1)/2)$ | $(1/4)(1-\hat{a}\cdot\hat{b})$ | $\rho_1 = \frac{1}{2}e_0$, purity $\frac{1}{2}$, entropy $\log 2$ |

These exercises illustrate five fundamental operations of the quantum formalism: **measurement** (Exercise: Measuring Spin Along an Arbitrary Direction), **evolution** (Exercise: Spin Precession in a Magnetic Field), **sequential measurement** (Exercise: Successive Measurements of Spin), **entangled measurement** (Exercise: Two Spins in the Singlet State), and **partial trace** (Exercise: The Reduced State of an Entangled Subsystem). In each case, the biquaternion framework expresses the operation as an algebraic manipulation of the elements of $\mathbb{M}_+$, $\mathbb{H}_\mathbb{B}$, and their tensor products.

## Summary

We have solved a fifth exercise in quantum mechanics — the reduced state of one subsystem of an entangled pair — in two parallel presentations.

In the **standard formulation**, the solution proceeds through the joint density matrix, the partial trace, and the result $\rho_1 = \frac{1}{2}I$, giving a maximally mixed state with purity $\frac{1}{2}$ and entropy $\log 2$.

In the **biquaternion formulation**, the solution proceeds through the singlet idempotent in $\mathbb{B}\otimes\mathbb{B}$, the partial trace on the tensor product, and the result $\rho_1 = \frac{1}{2}e_0$, giving the same values.

The two formulations agree, as they must. The biquaternion formulation makes explicit the algebraic origin of the mixedness: the entanglement of the joint state is encoded in the off-diagonal tensor-product terms, and tracing out one subsystem produces a mixed state whose mixedness measures the entanglement.

The comparison with a product state — where the reduced state is pure — illustrates the operational distinction between entangled and product states.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $\mathbb{M}_+$ | Hermitian subspace (states, observables) |
| $\mathbb{B}\otimes\mathbb{B}$ | Tensor product, isomorphic to $M_4(\mathbb{C})$ |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $|\Psi^-\rangle$ | Singlet state |
| $P_{\mathrm{singlet}} = \tfrac{1}{4}(e_0\otimes e_0 + \sum_k e_k\otimes e_k)$ | Singlet idempotent |
| $\mathrm{Tr}_2(a\otimes b) = a\,\mathrm{Tr}_\mathbb{B}(b)$ | Partial trace over the second factor |
| $\rho_1 = \mathrm{Tr}_2(P_{\mathrm{singlet}})$ | Reduced state of particle 1 |
| $\frac{1}{2}e_0$ | Maximally mixed state of a qubit |
| $\mathrm{Tr}(\rho_1^2)$ | Purity of the reduced state |
| $S(\rho_1) = -\mathrm{Tr}(\rho_1\log\rho_1)$ | von Neumann entropy |
| $\log$ | Natural logarithm |

## Further Reading

- A. Einstein, B. Podolsky, N. Rosen, "Can quantum-mechanical description of physical reality be considered complete?" *Physical Review* **47** (1935) 777–780, for the original EPR argument.
- E. Schrödinger, "Discussion of probability relations between separated systems," *Mathematical Proceedings of the Cambridge Philosophical Society* **31** (1935) 555–563, for the original discussion of the reduced density matrix.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the standard treatment of reduced states and the partial trace.
- J. J. Sakurai and Jim Napolitano, *Modern Quantum Mechanics* (Pearson, 2017), for the standard textbook treatment of the singlet state and the reduced density matrix.
- The companion articles of this series: *Quantum Mechanics in Biquaternionic Form*, *Spin-1/2 Quantum Mechanics in Biquaternionic Form*, *Exercise: Measuring Spin Along an Arbitrary Direction*, *Exercise: Spin Precession in a Magnetic Field*, *Exercise: Successive Measurements of Spin*, and *Exercise: Two Spins in the Singlet State*.

