# __Exercise: Successive Measurements of Spin__

## Introduction

This article is one of a series of **worked exercises** that illustrate quantum physics in two parallel presentations: the standard Hilbert-space formulation, and the biquaternion formulation developed in the companion articles. The goal is not to derive new physics, but to give the reader a concrete, computationally explicit demonstration of the correspondence between the two formalisms.

Each exercise in the series is solved twice: first in the standard way, then in the biquaternion way. The results agree, as they must: the two formulations are the same mathematics in different notation. To keep the two solutions strictly parallel, each is presented in the same steps, and the final result is stated in the same form.

The first exercise treated the Born rule for a single measurement. The second exercise treated the time evolution of a spin state. This third exercise treats **successive measurements**: what happens when a spin state is measured twice in a row, along different directions.

The conventions are those of the companion articles. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with the Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$. The quaternion units are $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ with $\vec e_k^2 = -e_t$, and $i$ is the scalar imaginary. The trace of an element of $\mathbb{M}_+$ is twice its scalar part: $\mathrm{Tr}(\tilde Q)=2\,\mathrm{Sc}(\tilde Q)$.

## The Exercise

A spin-$\tfrac{1}{2}$ particle is prepared in the **spin-up state along the $z$-axis**. It is then measured along a direction $\vec u_x$ that makes an angle $\theta_1$ with the $z$-axis, and immediately after, it is measured along a direction $\vec u_y$ that makes an angle $\theta_2$ with the $z$-axis. Both directions lie in the $xz$-plane. What is the **joint probability of both outcomes being spin-up**?

This exercise illustrates two structural features of quantum physics: the Born rule for a single measurement (already treated in Exercise: Measuring Spin Along an Arbitrary Direction), and the fact that a measurement **changes the state**, so that successive measurements are not independent.

## Solution in the Standard Formulation

### Step 1: The initial state

The spin-up state along the $z$-axis is the eigenvalue-$+1$ eigenvector of the Pauli matrix $\sigma_3$:

$$
|+z\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}.
$$

### Step 2: The eigenstates along the measurement directions

The spin-up state along a direction $\vec u = (\sin\theta, 0, \cos\theta)$ in the $xz$-plane is the eigenvalue-$+1$ eigenvector of $\vec u\cdot\boldsymbol{\sigma}$:

$$
|+n(\theta)\rangle = \begin{pmatrix} \cos(\theta/2) \\ \sin(\theta/2) \end{pmatrix}.
$$

In particular, the states for the two measurement directions are

$$
|+\vec u_x\rangle = \begin{pmatrix} \cos(\theta_1/2) \\ \sin(\theta_1/2) \end{pmatrix}, \qquad |+\vec u_y\rangle = \begin{pmatrix} \cos(\theta_2/2) \\ \sin(\theta_2/2) \end{pmatrix}.
$$

### Step 3: The joint probability

The joint probability of the two measurements both yielding the outcome spin-up is the product of the probability of the first outcome and the conditional probability of the second outcome given the first:

$$
p(+,+) = \bigl|\langle +\vec u_x \mid +z\rangle\bigr|^2 \cdot \bigl|\langle +\vec u_y \mid +\vec u_x\rangle\bigr|^2.
$$

**First factor.** The overlap of the initial state with $|+\vec u_x\rangle$ is

$$
\langle +\vec u_x \mid +z\rangle = \cos(\theta_1/2).
$$

So the first factor is

$$
p_1 = \bigl|\langle +\vec u_x \mid +z\rangle\bigr|^2 = \cos^2(\theta_1/2).
$$

**Second factor.** The angle between the two measurement directions is $\theta_2 - \theta_1$, so the overlap is

$$
\langle +\vec u_y \mid +\vec u_x\rangle = \cos\bigl((\theta_2 - \theta_1)/2\bigr).
$$

So the second factor is

$$
p_2 = \bigl|\langle +\vec u_y \mid +\vec u_x\rangle\bigr|^2 = \cos^2\bigl((\theta_2 - \theta_1)/2\bigr).
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
\tilde\Pi(\vec u) = \tfrac{1}{2}\left(e_t + i\vec u\right),
$$

where $\vec u$ is a unit pure real quaternion. The spin-up state along $z$ corresponds to

$$
\tilde\Pi_z = \tfrac{1}{2}\left(e_t + i \vec e_z\right).
$$

### Step 2: The idempotents along the measurement directions

The idempotents for the spin-up states along the two measurement directions are

$$
\tilde\Pi_{\vec u_x} = \tfrac{1}{2}\left(e_t + i\vec u_x\right), \qquad \tilde\Pi_{\vec u_y} = \tfrac{1}{2}\left(e_t + i\vec u_y\right),
$$

with $\vec u_x = \sin\theta_1\, \vec e_x + \cos\theta_1\, \vec e_z$ and $\vec u_y = \sin\theta_2\, \vec e_x + \cos\theta_2\, \vec e_z$ as unit pure real quaternions.

### Step 3: The joint probability

The joint probability of the two measurements both yielding spin-up is the product of the two trace formulas:

$$
p(+,+) = \mathrm{Tr}\!\left(\tilde\Pi_{\vec u_x} \circ \tilde\Pi_z\right) \cdot \mathrm{Tr}\!\left(\tilde\Pi_{\vec u_y} \circ \tilde\Pi_{\vec u_x}\right).
$$

**First factor.** From Exercise: Measuring Spin Along an Arbitrary Direction, the first factor is

$$
\mathrm{Tr}\!\left(\tilde\Pi_{\vec u_x} \circ \tilde\Pi_z\right) = 2\,\mathrm{Sc}\!\left(\tilde\Pi_{\vec u_x} \circ \tilde\Pi_z\right) = \cos^2(\theta_1/2).
$$

**Second factor.** Computing the product $\tilde\Pi_{\vec u_y} \circ \tilde\Pi_{\vec u_x}$,

$$
\tilde\Pi_{\vec u_y} \circ \tilde\Pi_{\vec u_x} = \tfrac{1}{4}\left(e_t + i\vec u_y\right)\left(e_t + i\vec u_x\right) = \tfrac{1}{4}\left[e_t + i\vec u_x + i\vec u_y - \vec u_y \vec u_x\right].
$$

For pure real quaternions, the product is $\vec u_y \vec u_x = -\vec u_y \cdot \vec u_x\, e_t + \vec u_y \times \vec u_x$. Substituting,

$$
\tilde\Pi_{\vec u_y} \circ \tilde\Pi_{\vec u_x} = \tfrac{1}{4}\left[\bigl(1 + \vec u_y \cdot \vec u_x\bigr) e_t + i\vec u_x + i\vec u_y - \vec u_y \times \vec u_x\right].
$$

The scalar part (coefficient of $e_t$) is $\tfrac{1}{4}(1 + \vec u_y \cdot \vec u_x)$; the other terms $i\vec u_x$, $i\vec u_y$, and $\vec u_y \times \vec u_x$ are vector terms with vanishing coefficient of $e_t$. Therefore

$$
\mathrm{Tr}\!\left(\tilde\Pi_{\vec u_y} \circ \tilde\Pi_{\vec u_x}\right) = 2 \cdot \tfrac{1}{4}\left(1 + \vec u_y \cdot \vec u_x\right) = \tfrac{1}{2}\left(1 + \vec u_y \cdot \vec u_x\right).
$$

Since both $\vec u_x$ and $\vec u_y$ lie in the $xz$-plane, the scalar product is $\vec u_y \cdot \vec u_x = \cos(\theta_2 - \theta_1)$, and the second factor is

$$
\mathrm{Tr}\!\left(\tilde\Pi_{\vec u_y} \circ \tilde\Pi_{\vec u_x}\right) = \tfrac{1}{2}\left(1 + \cos(\theta_2 - \theta_1)\right) = \cos^2\bigl((\theta_2 - \theta_1)/2\bigr).
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

These agree with the physical expectation: a measurement along a direction $\vec u$ destroys the information about the spin along any non-parallel direction, and the information about parallel directions is preserved.

## What the Biquaternion Solution Illustrates

**1. The trace formula applies to successive measurements.** The joint probability of two successive measurements is a **product of two trace formulas**:

$$
p(+,+) = \mathrm{Tr}\!\left(\tilde\Pi_{\vec u_x} \circ \tilde\Pi_z\right) \cdot \mathrm{Tr}\!\left(\tilde\Pi_{\vec u_y} \circ \tilde\Pi_{\vec u_x}\right).
$$

The first factor is the Born rule for the initial measurement; the second factor is the Born rule for the conditional measurement. Both use the same trace pairing on $\mathbb{M}_+$.

**2. Measurement is a projection onto an idempotent.** After the first measurement, the state is not the original $\tilde\Pi_z$ but the new idempotent $\tilde\Pi_{\vec u_x}$. This is the algebraic content of the "state update" or "collapse" rule. The biquaternion framework expresses this as a **change of the idempotent**: from $\tilde\Pi_z$ to $\tilde\Pi_{\vec u_x}$.

**3. The overlap of two idempotents is their scalar product.** The trace $\mathrm{Tr}(\tilde\Pi_{\vec u_y} \circ \tilde\Pi_{\vec u_x})$ is a symmetric function of the two idempotents, equal to $\frac{1}{2}(1 + \vec u_y \cdot \vec u_x)$, which depends only on the angle between the directions $\vec u_x$ and $\vec u_y$. This is the biquaternion expression of the transition probability between two spin states.

**4. The geometry enters through the algebra.** The angle between the measurement directions enters through the scalar product $\vec u_y \cdot \vec u_x = \cos(\theta_2 - \theta_1)$, which appears in the trace formula through the product $\vec u_y \vec u_x$. The Bloch sphere geometry is encoded in the multiplication rules of the algebra.

**5. The result agrees with the standard formulation.** This is not surprising, because the two formulations are the same mathematics in different notation: $\mathbb{B} \cong M_2(\mathbb{C})$, and the trace formula corresponds exactly to $\mathrm{Tr}(P_{\vec u_y}P_{\vec u_x})$ for rank-one projectors. But seeing the same result emerge from the algebra is a useful sanity check on the framework.

## Comparison with Exercises: Measuring Spin Along an Arbitrary Direction and Spin Precession in a Magnetic Field

| | Measuring Spin Along an Arbitrary Direction | Spin Precession in a Magnetic Field | Successive Measurements of Spin |
|---|---|---|---|
| Physical process | Single measurement | Time evolution | Successive measurements |
| Structural object | Idempotent + idempotent | Idempotent + unitary | Sequence of idempotents |
| Rule used | Trace formula | Trace formula + rotor conjugation | Product of trace formulas |
| Result | $\cos^2(\theta/2)$ | $(\hbar/2)\cos(\omega_L t)$ | $\cos^2(\theta_1/2)\cos^2((\theta_2-\theta_1)/2)$ |

These exercises illustrate three fundamental operations of the quantum formalism: **measurement** (Exercise: Measuring Spin Along an Arbitrary Direction), **evolution** (Exercise: Spin Precession in a Magnetic Field), and **sequential measurement** (Exercise: Successive Measurements of Spin). In each case, the biquaternion framework expresses the operation as an algebraic manipulation of the elements of $\mathbb{M}_+$ and $\mathbb{H}_\mathbb{B}$.

## Summary

We have solved a third exercise in quantum physics — the joint probability of two successive spin measurements along different directions — in two parallel presentations.

In the **standard formulation**, the solution proceeds through ket vectors, projection operators, and the Born rule for the first measurement followed by the conditional Born rule for the second, giving $p(+,+) = \cos^2(\theta_1/2)\cos^2((\theta_2-\theta_1)/2)$.

In the **biquaternion formulation**, the solution proceeds through the idempotents $\tilde\Pi_z, \tilde\Pi_{\vec u_x}, \tilde\Pi_{\vec u_y}$ and the product of the two trace formulas $\mathrm{Tr}(\tilde\Pi_{\vec u_x}\circ \tilde\Pi_z)\mathrm{Tr}(\tilde\Pi_{\vec u_y}\circ \tilde\Pi_{\vec u_x})$, giving the same result.

The two formulations agree, as they must. The biquaternion formulation makes explicit the algebraic structure of successive measurements: each measurement is a projection onto an idempotent, the transition probability between two idempotents is their trace pairing, and the joint probability is the product of the trace formulas.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $\mathbb{M}_+$ | Hermitian subspace (states, observables) |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_k^2 = -e_t$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\boldsymbol{\sigma} = (\sigma_1, \sigma_2, \sigma_3)$ | Pauli matrices |
| $\tilde\Pi_z = \tfrac{1}{2}(e_t + i\vec e_z)$ | Spin-up state along $z$ |
| $\tilde\Pi_{n_k} = \tfrac{1}{2}(e_t + i\vec u_k)$ | Idempotent along direction $\vec u_k$ |
| $\vec u_k = \sin\theta_k\,\vec e_x + \cos\theta_k\,\vec e_z$ | Unit vector for the $k$-th direction |
| $\mathrm{Tr}(\tilde\Pi_{\vec u_y} \circ \tilde\Pi_{\vec u_x})$ | Transition probability between idempotents |

## Further Reading

- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford, 1930), for the standard formulation of successive measurements.
- J. J. Sakurai and Jim Napolitano, *Modern Quantum Mechanics* (Pearson, 2017), for the standard textbook treatment of the Stern–Gerlach experiment and successive measurements.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the Bloch sphere and the composition of qubit measurements.
- The companion articles of this series: *Quantum Physics in Biquaternionic Form*, *Spin-1/2 Quantum Physics in Biquaternionic Form*, *Exercise: Measuring Spin Along an Arbitrary Direction*, and *Exercise: Spin Precession in a Magnetic Field*.

