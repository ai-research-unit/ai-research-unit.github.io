# __Exercise: Successive Measurements of Spin__

## Introduction

This article is one of a series of **worked exercises** that illustrate quantum mechanics in two parallel presentations: the standard Hilbert-space formulation, and the biquaternion formulation developed in the companion articles. The goal is not to derive new physics, but to give the reader a concrete, computationally explicit demonstration of the correspondence between the two formalisms.

Each exercise in the series is solved twice: first in the standard way, then in the biquaternion way. The results agree, as they must: the two formulations are the same mathematics in different notation. To keep the two solutions strictly parallel, each is presented in the same steps, and the final result is stated in the same form.

The first exercise treated the Born rule for a single measurement. The second exercise treated the time evolution of a spin state. This third exercise treats **successive measurements**: what happens when a spin state is measured twice in a row, along different directions.

The conventions are those of the companion articles. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with the Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$. The quaternion units are $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$, and $i$ is the scalar imaginary. The trace of an element of $\mathbb{M}_+$ is twice its scalar part: $\mathrm{Tr}(\tilde{H}) = 2\,\mathrm{Sc}(\tilde{H})$.

## The Exercise

A spin-$\tfrac{1}{2}$ particle is prepared in the **spin-up state along the $z$-axis**. It is then measured along a direction $\hat{n}_1$ that makes an angle $\theta_1$ with the $z$-axis, and immediately after, it is measured along a direction $\hat{n}_2$ that makes an angle $\theta_2$ with the $z$-axis. Both directions lie in the $xz$-plane. What is the **joint probability of both outcomes being spin-up**?

This exercise illustrates two structural features of quantum mechanics: the Born rule for a single measurement (already treated in Exercise: Measuring Spin Along an Arbitrary Direction), and the fact that a measurement **changes the state**, so that successive measurements are not independent.

## Solution in the Standard Formulation

### Step 1: The initial state

The spin-up state along the $z$-axis is the eigenvalue-$+1$ eigenvector of the Pauli matrix $\sigma_3$:

$$
|+z\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}.
$$

### Step 2: The eigenstates along the measurement directions

The spin-up state along a direction $\hat{n} = (\sin\theta, 0, \cos\theta)$ in the $xz$-plane is the eigenvalue-$+1$ eigenvector of $\hat{n}\cdot\boldsymbol{\sigma}$:

$$
|+n(\theta)\rangle = \begin{pmatrix} \cos(\theta/2) \\ \sin(\theta/2) \end{pmatrix}.
$$

In particular, the states for the two measurement directions are

$$
|+n_1\rangle = \begin{pmatrix} \cos(\theta_1/2) \\ \sin(\theta_1/2) \end{pmatrix}, \qquad |+n_2\rangle = \begin{pmatrix} \cos(\theta_2/2) \\ \sin(\theta_2/2) \end{pmatrix}.
$$

### Step 3: The joint probability

The joint probability of the two measurements both yielding the outcome spin-up is the product of the probability of the first outcome and the conditional probability of the second outcome given the first:

$$
p(+,+) = \bigl|\langle +n_1 \mid +z\rangle\bigr|^2 \cdot \bigl|\langle +n_2 \mid +n_1\rangle\bigr|^2.
$$

**First factor.** The overlap of the initial state with $|+n_1\rangle$ is

$$
\langle +n_1 \mid +z\rangle = \cos(\theta_1/2).
$$

So the first factor is

$$
p_1 = \bigl|\langle +n_1 \mid +z\rangle\bigr|^2 = \cos^2(\theta_1/2).
$$

**Second factor.** The angle between the two measurement directions is $\theta_2 - \theta_1$, so the overlap is

$$
\langle +n_2 \mid +n_1\rangle = \cos\bigl((\theta_2 - \theta_1)/2\bigr).
$$

So the second factor is

$$
p_2 = \bigl|\langle +n_2 \mid +n_1\rangle\bigr|^2 = \cos^2\bigl((\theta_2 - \theta_1)/2\bigr).
$$

### Step 4: The result

Multiplying the two factors,

$$
p(+,+) = \cos^2(\theta_1/2) \cdot \cos^2\bigl((\theta_2 - \theta_1)/2\bigr).
$$

## Solution in the Biquaternion Formulation

### Step 1: The initial state

In the biquaternion framework, a pure spin state is an **idempotent** of the Hermitian subspace $\mathbb{M}_+$, of the form

$$
P(\hat{m}) = \tfrac{1}{2}\left(e_0 + i\hat{m}\right),
$$

where $\hat{m}$ is a unit pure real quaternion. The spin-up state along $z$ corresponds to

$$
P_z = \tfrac{1}{2}\left(e_0 + i e_3\right).
$$

### Step 2: The projectors along the measurement directions

The projectors onto the spin-up states along the two measurement directions are the idempotents

$$
P_{n_1} = \tfrac{1}{2}\left(e_0 + i\hat{n}_1\right), \qquad P_{n_2} = \tfrac{1}{2}\left(e_0 + i\hat{n}_2\right),
$$

with $\hat{n}_1 = \sin\theta_1\, e_1 + \cos\theta_1\, e_3$ and $\hat{n}_2 = \sin\theta_2\, e_1 + \cos\theta_2\, e_3$ as unit pure real quaternions.

### Step 3: The joint probability

The joint probability of the two measurements both yielding spin-up is the product of the two trace formulas:

$$
p(+,+) = \mathrm{Tr}\!\left(P_{n_1} \circ P_z\right) \cdot \mathrm{Tr}\!\left(P_{n_2} \circ P_{n_1}\right).
$$

**First factor.** From Exercise: Measuring Spin Along an Arbitrary Direction, the first factor is

$$
\mathrm{Tr}\!\left(P_{n_1} \circ P_z\right) = 2\,\mathrm{Sc}\!\left(P_{n_1} \circ P_z\right) = \cos^2(\theta_1/2).
$$

**Second factor.** Computing the product $P_{n_2} \circ P_{n_1}$,

$$
P_{n_2} \circ P_{n_1} = \tfrac{1}{4}\left(e_0 + i\hat{n}_2\right)\left(e_0 + i\hat{n}_1\right) = \tfrac{1}{4}\left[e_0 + i\hat{n}_1 + i\hat{n}_2 - \hat{n}_2 \hat{n}_1\right].
$$

For pure real quaternions, the product is $\hat{n}_2 \hat{n}_1 = -\hat{n}_2 \cdot \hat{n}_1\, e_0 + \hat{n}_2 \times \hat{n}_1$. Substituting,

$$
P_{n_2} \circ P_{n_1} = \tfrac{1}{4}\left[\bigl(1 + \hat{n}_2 \cdot \hat{n}_1\bigr) e_0 + i\hat{n}_1 + i\hat{n}_2 - \hat{n}_2 \times \hat{n}_1\right].
$$

The scalar part (coefficient of $e_0$) is $\tfrac{1}{4}(1 + \hat{n}_2 \cdot \hat{n}_1)$; the other terms $i\hat{n}_1$, $i\hat{n}_2$, and $\hat{n}_2 \times \hat{n}_1$ are vector terms with vanishing coefficient of $e_0$. Therefore

$$
\mathrm{Tr}\!\left(P_{n_2} \circ P_{n_1}\right) = 2 \cdot \tfrac{1}{4}\left(1 + \hat{n}_2 \cdot \hat{n}_1\right) = \tfrac{1}{2}\left(1 + \hat{n}_2 \cdot \hat{n}_1\right).
$$

Since both $\hat{n}_1$ and $\hat{n}_2$ lie in the $xz$-plane, the scalar product is $\hat{n}_2 \cdot \hat{n}_1 = \cos(\theta_2 - \theta_1)$, and the second factor is

$$
\mathrm{Tr}\!\left(P_{n_2} \circ P_{n_1}\right) = \tfrac{1}{2}\left(1 + \cos(\theta_2 - \theta_1)\right) = \cos^2\bigl((\theta_2 - \theta_1)/2\bigr).
$$

### Step 4: The result

Multiplying the two factors,

$$
p(+,+) = \cos^2(\theta_1/2) \cdot \cos^2\bigl((\theta_2 - \theta_1)/2\bigr).
$$

## Limiting Cases

Both formulations give the same result, and both give the same limits.

**Case $\theta_1 = 0$, $\theta_2 = 0$** (both measurements along $z$). Then

$$
p(+,+) = \cos^2(0) \cdot \cos^2(0) = 1.
$$

Measuring $z$ twice in a row gives the same result with certainty.

**Case $\theta_1 = \pi/2$, $\theta_2 = 0$** (measure $x$, then measure $z$). Then

$$
p(+,+) = \cos^2(\pi/4) \cdot \cos^2(\pi/4) = \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}.
$$

This is the canonical "successive Stern–Gerlach" result: after measuring along $x$, the information about $z$ is scrambled, and the subsequent measurement along $z$ is equally likely to be $+$ or $-$.

**Case $\theta_1 = \pi/2$, $\theta_2 = \pi/2$** (measure $x$ twice). Then

$$
p(+,+) = \cos^2(\pi/4) \cdot \cos^2(0) = \frac{1}{2} \cdot 1 = \frac{1}{2}.
$$

Here the two factors have a clean interpretation. The first measurement along $x$ has probability $1/2$ of giving $+$, since the initial state is spin-up along $z$, not along $x$. Conditionally on the first outcome being $+$, the state has collapsed to spin-up along $x$, and the second measurement along the same direction is then certain to give $+$ again. So the joint probability is $1/2 \cdot 1 = 1/2$. This illustrates that two successive measurements along the **same** direction are perfectly correlated, once the state has been collapsed.

**Case $\theta_1 = 0$, $\theta_2 = \pi/2$** (measure $z$, then measure $x$). Then

$$
p(+,+) = \cos^2(0) \cdot \cos^2(\pi/4) = 1 \cdot \frac{1}{2} = \frac{1}{2}.
$$

Measuring $z$ first leaves the state unchanged (it is already spin-up along $z$), and then measuring $x$ gives $+$ with probability $1/2$.

These agree with the physical expectation: a measurement along a direction $\hat{n}$ destroys the information about the spin along any non-parallel direction, and the information about parallel directions is preserved.

## What the Biquaternion Solution Illustrates

**1. The trace formula applies to successive measurements.** The joint probability of two successive measurements is a **product of two trace formulas**:

$$
p(+,+) = \mathrm{Tr}\!\left(P_{n_1} \circ P_z\right) \cdot \mathrm{Tr}\!\left(P_{n_2} \circ P_{n_1}\right).
$$

The first factor is the Born rule for the initial measurement; the second factor is the Born rule for the conditional measurement. Both use the same trace pairing on $\mathbb{M}_+$.

**2. Measurement is a projection onto an idempotent.** After the first measurement, the state is not the original $P_z$ but the new idempotent $P_{n_1}$. This is the algebraic content of the "state update" or "collapse" rule. The biquaternion framework expresses this as a **change of the idempotent**: from $P_z$ to $P_{n_1}$.

**3. The overlap of two idempotents is their scalar product.** The trace $\mathrm{Tr}(P_{n_2} \circ P_{n_1})$ is a symmetric function of the two idempotents, equal to $\frac{1}{2}(1 + \hat{n}_2 \cdot \hat{n}_1)$, which depends only on the angle between the directions $\hat{n}_1$ and $\hat{n}_2$. This is the biquaternion expression of the transition probability between two spin states.

**4. The geometry enters through the algebra.** The angle between the measurement directions enters through the scalar product $\hat{n}_2 \cdot \hat{n}_1 = \cos(\theta_2 - \theta_1)$, which appears in the trace formula through the product $\hat{n}_2 \hat{n}_1$. The Bloch sphere geometry is encoded in the multiplication rules of the algebra.

**5. The result agrees with the standard formulation.** This is not surprising, because the two formulations are the same mathematics in different notation: $\mathbb{B} \cong M_2(\mathbb{C})$, and the trace formula corresponds exactly to $\mathrm{Tr}(P_{n_2}P_{n_1})$ for rank-one projectors. But seeing the same result emerge from the algebra is a useful sanity check on the framework.

## Comparison with Exercises: Measuring Spin Along an Arbitrary Direction and Spin Precession in a Magnetic Field

| | Measuring Spin Along an Arbitrary Direction | Spin Precession in a Magnetic Field | Successive Measurements of Spin |
|---|---|---|---|
| Physical process | Single measurement | Time evolution | Successive measurements |
| Structural object | Idempotent + idempotent | Idempotent + unitary | Sequence of idempotents |
| Rule used | Trace formula | Trace formula + rotor conjugation | Product of trace formulas |
| Result | $\cos^2(\theta/2)$ | $(\hbar/2)\cos(\omega_L t)$ | $\cos^2(\theta_1/2)\cos^2((\theta_2-\theta_1)/2)$ |

These exercises illustrate three fundamental operations of the quantum formalism: **measurement** (Exercise: Measuring Spin Along an Arbitrary Direction), **evolution** (Exercise: Spin Precession in a Magnetic Field), and **sequential measurement** (Exercise: Successive Measurements of Spin). In each case, the biquaternion framework expresses the operation as an algebraic manipulation of the elements of $\mathbb{M}_+$ and $\mathbb{H}_\mathbb{B}$.

## Summary

We have solved a third exercise in quantum mechanics — the joint probability of two successive spin measurements along different directions — in two parallel presentations.

In the **standard formulation**, the solution proceeds through ket vectors, projection operators, and the Born rule for the first measurement followed by the conditional Born rule for the second, giving $p(+,+) = \cos^2(\theta_1/2)\cos^2((\theta_2-\theta_1)/2)$.

In the **biquaternion formulation**, the solution proceeds through the idempotents $P_z, P_{n_1}, P_{n_2}$ and the product of the two trace formulas $\mathrm{Tr}(P_{n_1}\circ P_z)\mathrm{Tr}(P_{n_2}\circ P_{n_1})$, giving the same result.

The two formulations agree, as they must. The biquaternion formulation makes explicit the algebraic structure of successive measurements: each measurement is a projection onto an idempotent, the transition probability between two idempotents is their trace pairing, and the joint probability is the product of the trace formulas.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $\mathbb{M}_+$ | Hermitian subspace (states, observables) |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\boldsymbol{\sigma} = (\sigma_1, \sigma_2, \sigma_3)$ | Pauli matrices |
| $P_z = \tfrac{1}{2}(e_0 + ie_3)$ | Spin-up state along $z$ |
| $P_{n_k} = \tfrac{1}{2}(e_0 + i\hat{n}_k)$ | Projector along direction $\hat{n}_k$ |
| $\hat{n}_k = \sin\theta_k\,e_1 + \cos\theta_k\,e_3$ | Unit vector for the $k$-th direction |
| $\mathrm{Tr}(P_{n_2} \circ P_{n_1})$ | Transition probability between idempotents |

## Further Reading

- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford, 1930), for the standard formulation of successive measurements.
- J. J. Sakurai and Jim Napolitano, *Modern Quantum Mechanics* (Pearson, 2017), for the standard textbook treatment of the Stern–Gerlach experiment and successive measurements.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the Bloch sphere and the composition of qubit measurements.
- The companion articles of this series: *Quantum Mechanics in Biquaternionic Form*, *Spin-1/2 Quantum Mechanics in Biquaternionic Form*, *Exercise: Measuring Spin Along an Arbitrary Direction*, and *Exercise: Spin Precession in a Magnetic Field*.

---

## Notes on the final version

**Two changes applied.**

**Change 1 — the wording in the standard Step 3.** The sentence introducing the joint probability has been reworded for precision:

> "The joint probability of the two measurements both yielding the outcome spin-up is the product of the probability of the first outcome and the conditional probability of the second outcome given the first."

The phrase "both yielding spin-up" has been expanded to "the probability of the first outcome and the conditional probability of the second outcome given the first", which makes the conditional structure explicit and matches the level of precision used in the biquaternion solution.

**Change 2 — the interpretation in the case $\theta_1 = \pi/2$, $\theta_2 = \pi/2$.** A short paragraph has been added clarifying that the two successive measurements along the **same** direction ($x$) are perfectly correlated after the first measurement collapses the state:

> "Here the two factors have a clean interpretation. The first measurement along $x$ has probability $1/2$ of giving $+$, since the initial state is spin-up along $z$, not along $x$. Conditionally on the first outcome being $+$, the state has collapsed to spin-up along $x$, and the second measurement along the same direction is then certain to give $+$ again. So the joint probability is $1/2 \cdot 1 = 1/2$. This illustrates that two successive measurements along the **same** direction are perfectly correlated, once the state has been collapsed."

This reinforces the point that the collapse rule has observable consequences: measurements along the same direction are not independent, but perfectly correlated.

Everything else is unchanged. The article is now ready for the blog.

