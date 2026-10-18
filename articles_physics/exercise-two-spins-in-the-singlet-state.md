# __Exercise: Two Spins in the Singlet State__

## Introduction

This article is one of a series of **worked exercises** that illustrate quantum physics in two parallel presentations: the standard Hilbert-space formulation, and the biquaternion formulation developed in the companion articles. The goal is not to derive new physics, but to give the reader a concrete, computationally explicit demonstration of the correspondence between the two formalisms.

Each exercise in the series is solved twice: first in the standard way, then in the biquaternion way. The results agree, as they must: the two formulations are the same mathematics in different notation. To keep the two solutions strictly parallel, each is presented in the same steps, and the final result is stated in the same form.

Earlier exercises treated a single qubit: a single measurement (Exercise: Measuring Spin Along an Arbitrary Direction), time evolution (Exercise: Spin Precession in a Magnetic Field), and successive measurements (Exercise: Successive Measurements of Spin). This exercise treats a **two-qubit system**, and introduces the first genuinely quantum-mechanical correlation: **entanglement**.

The conventions are those of the companion articles. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with the Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$. The quaternion units are $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ with $\vec e_k^2 = -e_t$, and $i$ is the scalar imaginary. The trace of an element of $\mathbb{M}_+$ is twice its scalar part: $\mathrm{Tr}(\tilde Q)=2\,\mathrm{Sc}(\tilde Q)$. For the two-qubit system, the state space is the tensor product $\mathbb{B}\otimes\mathbb{B}$, which is isomorphic to $M_4(\mathbb{C})$. The trace on $\mathbb{B}\otimes\mathbb{B}$ is the tensor product of the traces on each factor: $\mathrm{Tr}(x\otimes y) = \mathrm{Tr}_\mathbb{B}(x)\cdot\mathrm{Tr}_\mathbb{B}(y)$.

## The Exercise

Two spin-$\tfrac{1}{2}$ particles are prepared in the **singlet state**

$$
|\Psi^-\rangle = \frac{1}{\sqrt{2}}\left(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle\right).
$$

Particle 1 is measured along a direction $\vec u_a$ that makes an angle $\theta_a$ with the $z$-axis, and particle 2 is measured along a direction $\vec u_b$ that makes an angle $\theta_b$ with the $z$-axis. Both directions lie in the $xz$-plane. What is the **joint probability $p(+,+)$ of both outcomes being spin-up**?

This is the canonical **EPR/Bell** exercise. It illustrates that the two particles are **entangled**: the joint state is not a product state, and the joint probabilities depend on the angle between the two measurement directions.

## Solution in the Standard Formulation

### Step 1: The state

The singlet state is the antisymmetric combination of the two spin states in the 4-dimensional Hilbert space $\mathbb{C}^2\otimes\mathbb{C}^2$:

$$
|\Psi^-\rangle = \frac{1}{\sqrt{2}}\left(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle\right).
$$

It is a **maximally entangled** state: it cannot be written as a product $|\psi_1\rangle\otimes|\psi_2\rangle$ for any single-qubit states $|\psi_1\rangle, |\psi_2\rangle$.

### Step 2: The measurement operators

The projector onto spin-up along $\vec u_a$ for particle 1 is

$$
\tilde\Pi(\vec u_a) = \frac{1}{2}\left(I + \vec u_a\cdot\boldsymbol{\sigma}\right),
$$

and similarly for particle 2 along $\vec u_b$. The joint measurement operator is the tensor product

$$
P_{++}(\vec u_a,\vec u_b) = \tilde\Pi(\vec u_a)\otimes \tilde\Pi(\vec u_b) = \frac{1}{4}\left(I + \vec u_a\cdot\boldsymbol{\sigma}_1\right)\otimes\left(I + \vec u_b\cdot\boldsymbol{\sigma}_2\right),
$$

where $\boldsymbol{\sigma}_1 = \boldsymbol{\sigma}\otimes I$ acts on particle 1, and $\boldsymbol{\sigma}_2 = I\otimes\boldsymbol{\sigma}$ acts on particle 2.

### Step 3: The probability

The joint probability is the Born rule applied to the two-qubit state:

$$
p(+,+) = \langle\Psi^-|\,P_{++}(\vec u_a,\vec u_b)\,|\Psi^-\rangle.
$$

Expanding the product,

$$
p(+,+) = \frac{1}{4}\Bigl[\langle I\rangle + \langle\vec u_a\cdot\boldsymbol{\sigma}_1\rangle + \langle\vec u_b\cdot\boldsymbol{\sigma}_2\rangle + \langle(\vec u_a\cdot\boldsymbol{\sigma}_1)(\vec u_b\cdot\boldsymbol{\sigma}_2)\rangle\Bigr].
$$

The four expectation values in the singlet state are:

- $\langle I\rangle = 1$.
- $\langle\vec u_a\cdot\boldsymbol{\sigma}_1\rangle = \sum_j a_j\langle\sigma_{1j}\rangle = 0$, because the singlet is rotationally invariant and $\langle\sigma_{1j}\rangle = 0$ for all $j$.
- $\langle\vec u_b\cdot\boldsymbol{\sigma}_2\rangle = 0$, by the same argument.
- $\langle(\vec u_a\cdot\boldsymbol{\sigma}_1)(\vec u_b\cdot\boldsymbol{\sigma}_2)\rangle = \sum_{j,k}a_j b_k\langle\sigma_{1j}\sigma_{2k}\rangle = -\sum_j a_j b_j = -\vec u_a\cdot\vec u_b$.

The last equality uses the standard singlet correlation $\langle\sigma_{1j}\sigma_{2k}\rangle = -\delta_{jk}$.

Substituting,

$$
p(+,+) = \frac{1}{4}\left(1 - \vec u_a\cdot\vec u_b\right).
$$

### Step 4: The result

$$
p(+,+) = \frac{1}{4}\left(1 - \vec u_a\cdot\vec u_b\right).
$$

In terms of the angle $\theta$ between the two directions,

$$
p(+,+) = \frac{1}{4}\left(1 - \cos\theta\right) = \frac{1}{2}\sin^2\!\left(\frac{\theta}{2}\right).
$$

## Solution in the Biquaternion Formulation

### Step 1: The state

In the biquaternion framework, a single-qubit pure state is an idempotent of $\mathbb{M}_+$, of the form $\tilde\Pi(\vec u_m) = \tfrac{1}{2}(e_t + i\vec u_m)$. For a **two-qubit system**, the state space is the tensor product $\mathbb{B}\otimes\mathbb{B}$, and a two-qubit pure state is an idempotent of $\mathbb{M}_+\otimes\mathbb{M}_+$.

The singlet state corresponds to the idempotent

$$
\tilde\Pi_{\mathrm{singlet}} = \frac{1}{4}\left(e_t\otimes e_t + \vec e_x\otimes \vec e_x + \vec e_y\otimes \vec e_y + \vec e_z\otimes \vec e_z\right).
$$


*Idempotency.* Using $(x\otimes y)\circ(z\otimes w) = (x\circ z)\otimes(y\circ w)$ and the quaternion multiplication rules,

$$
\tilde\Pi_{\mathrm{singlet}}\circ \tilde\Pi_{\mathrm{singlet}} = \frac{1}{16}\sum_{\mu,\nu\in\{t,x,y,z\}}(e_\mu\circ \vec e_\nu)\otimes(e_\mu\circ \vec e_\nu).
$$

For the diagonal pairs $\mu = \nu$, the product $e_\mu\circ e_\mu$ equals $e_t$ for $\mu = t$ and $-e_t$ for $\mu\in\{x,y,z\}$. In both cases the tensor product $(e_\mu\circ e_\mu)\otimes(e_\mu\circ e_\mu)$ equals $e_t\otimes e_t$, so the four diagonal terms contribute $4\,e_t\otimes e_t$ in total.

For the off-diagonal pairs $\mu \neq \nu$, the twelve ordered pairs $(\mu,\nu)$ with $\mu \neq \nu$ group into six unordered pairs $\{\mu,\nu\}$. Each unordered pair contributes two terms to the sum, and in every case the two terms are equal: for pairs involving the identity (of the form $\{t,\nu\}$), the products $e_t \vec e_\nu$ and $\vec e_\nu e_t$ are both equal to $\vec e_\nu$, so the two terms $\vec e_\nu\otimes \vec e_\nu$ coincide; for pairs not involving the identity (of the form $\{\mu,\nu\}$ with $\mu, \nu \in \{x,y,z\}$), the products $e_\mu \vec e_\nu = \epsilon_{\mu\nu\lambda} e_\lambda$ and $\vec e_\nu e_\mu = -\epsilon_{\mu\nu\lambda} e_\lambda$ are opposites, and the tensor product squares the sign, so again the two terms $e_\lambda\otimes e_\lambda$ coincide. Concretely, the three pairs involving $e_t$ contribute $2\,\vec e_k\otimes \vec e_k$ for $k = 1, 2, 3$, and the three pairs not involving $e_t$ contribute $2\,e_\lambda\otimes e_\lambda$ for $\lambda$ equal to the remaining index. Summing, each of $\vec e_x\otimes \vec e_x$, $\vec e_y\otimes \vec e_y$, $\vec e_z\otimes \vec e_z$ appears four times, and the off-diagonal terms contribute

$$
4\left(\vec e_x\otimes \vec e_x + \vec e_y\otimes \vec e_y + \vec e_z\otimes \vec e_z\right).
$$

Combining the diagonal and off-diagonal contributions,

$$
\tilde\Pi_{\mathrm{singlet}}\circ \tilde\Pi_{\mathrm{singlet}} = \frac{1}{16}\cdot 4\left(e_t\otimes e_t + \vec e_x\otimes \vec e_x + \vec e_y\otimes \vec e_y + \vec e_z\otimes \vec e_z\right) = \tilde\Pi_{\mathrm{singlet}}.
$$

*Trace.* The trace is $\mathrm{Tr}(\tilde\Pi_{\mathrm{singlet}}) = \frac{1}{4}\sum_{\mu\in\{t,x,y,z\}}\mathrm{Tr}_\mathbb{B}(e_\mu)^2$. Each $\mathrm{Tr}_\mathbb{B}(e_\mu) = 2$ for $\mu = t$ (since $\mathrm{Tr}_\mathbb{B}(e_t) = 2$) and $0$ for $\mu\in\{x,y,z\}$ (since the trace of a pure quaternion vanishes). So the sum is $4$, and $\mathrm{Tr}(\tilde\Pi_{\mathrm{singlet}}) = \frac{1}{4}\cdot 4 = 1$.

### Step 2: The measurement operators

The single-qubit pure-state idempotent for spin-up along $\vec u_a$ is $\tilde\Pi(\vec u_a) = \tfrac{1}{2}(e_t + i\vec u_a)$. The joint measurement operator is the tensor product

$$
\tilde\Pi_{++}(\vec u_a,\vec u_b) = \tilde\Pi(\vec u_a)\otimes \tilde\Pi(\vec u_b) = \frac{1}{4}\left(e_t + i\vec u_a\right)\otimes\left(e_t + i\vec u_b\right).
$$

### Step 3: The probability

The joint probability is the trace formula on $\mathbb{B}\otimes\mathbb{B}$:

$$
p(+,+) = \mathrm{Tr}\!\left(\tilde\Pi_{\mathrm{singlet}}\circ \tilde\Pi_{++}(\vec u_a,\vec u_b)\right).
$$

Computing the product,

$$
\tilde\Pi_{\mathrm{singlet}}\circ \tilde\Pi_{++} = \frac{1}{16}\sum_{\mu\in\{t,x,y,z\}}\left[e_\mu(e_t + i\vec u_a)\right]\otimes\left[e_\mu(e_t + i\vec u_b)\right].
$$

Applying the tensor-product trace,

$$
p(+,+) = \frac{1}{16}\sum_{\mu\in\{t,x,y,z\}}\mathrm{Tr}_\mathbb{B}\!\left[e_\mu(e_t + i\vec u_a)\right]\cdot\mathrm{Tr}_\mathbb{B}\!\left[e_\mu(e_t + i\vec u_b)\right].
$$

**Term $\mu = t$.** $\mathrm{Tr}_\mathbb{B}(e_t + i\vec u_a) = 2$, and similarly for $\vec u_b$. Contribution: $2\cdot 2 = 4$.

**Terms $\mu\in\{x,y,z\}$.** We have $e_\mu(e_t + i\vec u_a) = e_\mu + ie_\mu\vec u_a$. The scalar part of $e_\mu\vec u_a$ is $-\vec {u_a}_\mu e_t$, so $\mathrm{Tr}_\mathbb{B}(e_\mu\vec u_a) = -2\vec {u_a}_\mu$ and $\mathrm{Tr}_\mathbb{B}(e_\mu + ie_\mu\vec u_a) = -2i\vec {u_a}_\mu$. Similarly $\mathrm{Tr}_\mathbb{B}(e_\mu + ie_\mu\vec u_b) = -2i\vec {u_b}_\mu$. Contribution of term $j$: $(-2i\vec {u_a}_\mu)(-2i\vec {u_b}_\mu) = -4\vec {u_a}_\mu\vec {u_b}_\mu$.

Summing over $\mu\in\{x,y,z\}$: $-4\,\vec u_a\cdot\vec u_b$.

**Total.** $p(+,+) = \frac{1}{16}\left(4 - 4\,\vec u_a\cdot\vec u_b\right) = \frac{1}{4}\left(1 - \vec u_a\cdot\vec u_b\right)$.

### Step 4: The result

$$
p(+,+) = \frac{1}{4}\left(1 - \vec u_a\cdot\vec u_b\right).
$$

In terms of the angle $\theta$ between the two directions,

$$
p(+,+) = \frac{1}{4}\left(1 - \cos\theta\right) = \frac{1}{2}\sin^2\!\left(\frac{\theta}{2}\right).
$$

## Limiting Cases

Both formulations give the same result, and both give the same limits.

**Case $\vec u_a = \vec u_b$** (both measurements along the same direction, $\theta = 0$). Then

$$
p(+,+) = \frac{1}{4}(1 - 1) = 0.
$$

The two outcomes with the **same sign** have probability $0$, and the two with **different signs** have probability $1/2$ each. Both particles are never found spin-up along the same direction: the singlet has perfectly anti-correlated spins along any common axis.

**Case $\vec u_a = -\vec u_b$** (opposite directions, $\theta = \pi$). Then

$$
p(+,+) = \frac{1}{4}(1 - (-1)) = \frac{1}{2}.
$$

The two outcomes with the **same sign** have probability $1/2$ each, and the two with **different signs** have probability $0$. This is the **opposite** of the previous case, and it is a direct consequence of the perfect anti-correlation along $\vec u_a$: the outcome "spin-up along $\vec u_b$" for particle 2 coincides with "spin-down along $\vec u_a$", so the two spins are found with the same sign label when measured in their respective directions.

**Case $\vec u_a \perp \vec u_b$** (perpendicular directions, $\theta = \pi/2$). Then

$$
p(+,+) = \frac{1}{4}(1 - 0) = \frac{1}{4}.
$$

All four outcomes are equally likely with probability $1/4$, by the symmetry $\vec u_a \to -\vec u_a$, $\vec u_b \to -\vec u_b$ of the singlet state and the perpendicularity $\vec u_a\cdot\vec u_b = 0$.

These agree with the physical expectation: the singlet state is perfectly anti-correlated along any direction, and the joint probabilities depend only on the angle between the two measurement directions.

## What the Biquaternion Solution Illustrates

**1. Entanglement as a non-product state.** The singlet state $\tilde\Pi_{\mathrm{singlet}}$ is an element of $\mathbb{B}\otimes\mathbb{B}$ that is **not** of the form $\tilde\Pi_1\otimes\tilde\Pi_2$ for any single-qubit idempotents $\tilde\Pi_1, \tilde\Pi_2$. This is the algebraic content of entanglement: the joint state is not a product of the two subsystems' states.

**2. The trace formula generalizes to two qubits.** The joint probability is

$$
p(+,+) = \mathrm{Tr}\!\left(\tilde\Pi_{\mathrm{singlet}}\circ \tilde\Pi_{++}(\vec u_a,\vec u_b)\right),
$$

the natural pairing between the joint state and the joint measurement operator. The trace is the tensor product of the single-qubit traces, $\mathrm{Tr}(x\otimes y) = \mathrm{Tr}_\mathbb{B}(x)\cdot\mathrm{Tr}_\mathbb{B}(y)$.

**3. The correlations arise from the tensor-product structure.** The single-qubit idempotents $\tilde\Pi(\vec u_a)$ and $\tilde\Pi(\vec u_b)$ are independent, but the joint state $\tilde\Pi_{\mathrm{singlet}}$ is entangled. The correlation $\vec u_a\cdot\vec u_b$ enters through the cross terms $\sum_k \vec e_k\otimes \vec e_k$ in the singlet idempotent, which couple the two qubits.

**4. The geometry enters through the algebra.** The angle $\theta$ enters through the scalar product $\vec u_a\cdot\vec u_b$, which appears in the trace formula through the products $\vec e_\nu\vec u_a$ and $\vec e_\nu\vec u_b$. The Bloch sphere geometry of each qubit is thus combined into the joint probability through the algebra of $\mathbb{B}\otimes\mathbb{B}$.

**5. The result agrees with the standard formulation.** This is not surprising, because the two formulations are the same mathematics in different notation: $\mathbb{B}\otimes\mathbb{B} \cong M_4(\mathbb{C})$, and the singlet idempotent corresponds exactly to the rank-one projector $|\Psi^-\rangle\langle\Psi^-|$ under the isomorphism. But seeing the same result emerge from the algebra is a useful sanity check on the framework, and it illustrates the structural claim of the companion articles: **the kinematics of two qubits is contained in the tensor product $\mathbb{M}_+\otimes\mathbb{M}_+$, with the Born rule given by the tensor-product trace.**

## Comparison with Exercises: Measuring Spin Along an Arbitrary Direction, Spin Precession in a Magnetic Field and Successive Measurements of Spin

| | Measuring Spin Along an Arbitrary Direction | Spin Precession in a Magnetic Field | Successive Measurements of Spin | Two Spins in the Singlet State |
|---|---|---|---|---|
| System | One qubit | One qubit | One qubit | Two qubits |
| Physical process | Single measurement | Time evolution | Successive measurements | Entangled measurement |
| Structural object | Idempotent + idempotent | Idempotent + unitary | Sequence of idempotents | Idempotent in $\mathbb{B}\otimes\mathbb{B}$ |
| Rule used | Trace formula | Trace formula + rotor conjugation | Product of trace formulas | Tensor-product trace formula |
| Result | $\cos^2(\theta/2)$ | $(\hbar/2)\cos(\omega_L t)$ | $\cos^2(\theta_1/2)\cos^2((\theta_2-\theta_1)/2)$ | $(1/4)(1 - \vec u_a\cdot\vec u_b)$ |

These exercises illustrate four fundamental operations of the quantum formalism: **measurement** (Exercise: Measuring Spin Along an Arbitrary Direction), **evolution** (Exercise: Spin Precession in a Magnetic Field), **sequential measurement** (Exercise: Successive Measurements of Spin), and **entangled measurement** (Exercise: Two Spins in the Singlet State). In each case, the biquaternion framework expresses the operation as an algebraic manipulation of the elements of $\mathbb{M}_+$ and $\mathbb{H}_\mathbb{B}$ (and, in Exercise: Two Spins in the Singlet State, their tensor products).

## Summary

We have solved a fourth exercise in quantum physics — the joint spin measurement of a singlet state along two arbitrary directions — in two parallel presentations.

In the **standard formulation**, the solution proceeds through the two-qubit state, the tensor-product projector, and the Born rule, giving $p(+,+) = (1/4)(1 - \vec u_a\cdot\vec u_b)$.

In the **biquaternion formulation**, the solution proceeds through the singlet idempotent in $\mathbb{B}\otimes\mathbb{B}$, the tensor-product idempotent, and the trace formula, giving the same result.

The two formulations agree, as they must. The biquaternion formulation makes explicit the algebraic structure of entanglement: the joint state is a **non-product idempotent** of the tensor-product algebra, and the correlations arise from the tensor-product terms in the state.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $\mathbb{M}_+$ | Hermitian subspace (states, observables) |
| $\mathbb{B}\otimes\mathbb{B}$ | Tensor product, isomorphic to $M_4(\mathbb{C})$ |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_k^2 = -e_t$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\boldsymbol{\sigma} = (\sigma_1, \sigma_2, \sigma_3)$ | Pauli matrices |
| $|\Psi^-\rangle$ | Singlet state |
| $\tilde\Pi_{\mathrm{singlet}} = \tfrac{1}{4}(e_t\otimes e_t + \sum_k \vec e_k\otimes \vec e_k)$ | Singlet idempotent |
| $\tilde\Pi(\vec u_a) = \tfrac{1}{2}(e_t + i\vec u_a)$ | Single-qubit idempotent |
| $\tilde\Pi_{++}(\vec u_a,\vec u_b) = \tilde\Pi(\vec u_a)\otimes \tilde\Pi(\vec u_b)$ | Joint idempotent |
| $\mathrm{Tr}(x\otimes y) = \mathrm{Tr}_\mathbb{B}(x)\cdot\mathrm{Tr}_\mathbb{B}(y)$ | Trace on the tensor product |

## Further Reading

- A. Einstein, B. Podolsky, N. Rosen, "Can quantum-mechanical description of physical reality be considered complete?" *Physical Review* **47** (1935) 777–780, for the original EPR argument.
- J. S. Bell, "On the Einstein–Podolsky–Rosen paradox," *Physics* **1** (1964) 195–200, for the Bell inequalities and the singlet correlations.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the standard treatment of entanglement and Bell states.
- J. J. Sakurai and Jim Napolitano, *Modern Quantum Mechanics* (Pearson, 2017), for the standard textbook treatment of the singlet state.
- The companion articles of this series: *Quantum Physics in Biquaternionic Form*, *Spin-1/2 Quantum Physics in Biquaternionic Form*, *Exercise: Measuring Spin Along an Arbitrary Direction*, *Exercise: Spin Precession in a Magnetic Field*, and *Exercise: Successive Measurements of Spin*.

