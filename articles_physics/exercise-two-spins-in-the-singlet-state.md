# __Exercise: Two Spins in the Singlet State__

## Introduction

This article is one of a series of **worked exercises** that illustrate quantum mechanics in two parallel presentations: the standard Hilbert-space formulation, and the biquaternion formulation developed in the companion articles. The goal is not to derive new physics, but to give the reader a concrete, computationally explicit demonstration of the correspondence between the two formalisms.

Each exercise in the series is solved twice: first in the standard way, then in the biquaternion way. The results agree, as they must: the two formulations are the same mathematics in different notation. To keep the two solutions strictly parallel, each is presented in the same steps, and the final result is stated in the same form.

Earlier exercises treated a single qubit: a single measurement (Exercise: Measuring Spin Along an Arbitrary Direction), time evolution (Exercise: Spin Precession in a Magnetic Field), and successive measurements (Exercise: Successive Measurements of Spin). This exercise treats a **two-qubit system**, and introduces the first genuinely quantum-mechanical correlation: **entanglement**.

The conventions are those of the companion articles. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with the Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$. The quaternion units are $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$, and $i$ is the scalar imaginary. The trace of an element of $\mathbb{M}_+$ is twice its scalar part: $\mathrm{Tr}(\tilde{H}) = 2\,\mathrm{Sc}(\tilde{H})$. For the two-qubit system, the state space is the tensor product $\mathbb{B}\otimes\mathbb{B}$, which is isomorphic to $M_4(\mathbb{C})$. The trace on $\mathbb{B}\otimes\mathbb{B}$ is the tensor product of the traces on each factor: $\mathrm{Tr}(x\otimes y) = \mathrm{Tr}_\mathbb{B}(x)\cdot\mathrm{Tr}_\mathbb{B}(y)$.

## The Exercise

Two spin-$\tfrac{1}{2}$ particles are prepared in the **singlet state**

$$
|\Psi^-\rangle = \frac{1}{\sqrt{2}}\left(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle\right).
$$

Particle 1 is measured along a direction $\hat{a}$ that makes an angle $\theta_a$ with the $z$-axis, and particle 2 is measured along a direction $\hat{b}$ that makes an angle $\theta_b$ with the $z$-axis. Both directions lie in the $xz$-plane. What is the **joint probability $p(+,+)$ of both outcomes being spin-up**?

This is the canonical **EPR/Bell** exercise. It illustrates that the two particles are **entangled**: the joint state is not a product state, and the joint probabilities depend on the angle between the two measurement directions.

## Solution in the Standard Formulation

### Step 1: The state

The singlet state is the antisymmetric combination of the two spin states in the 4-dimensional Hilbert space $\mathbb{C}^2\otimes\mathbb{C}^2$:

$$
|\Psi^-\rangle = \frac{1}{\sqrt{2}}\left(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle\right).
$$

It is a **maximally entangled** state: it cannot be written as a product $|\psi_1\rangle\otimes|\psi_2\rangle$ for any single-qubit states $|\psi_1\rangle, |\psi_2\rangle$.

### Step 2: The measurement operators

The projector onto spin-up along $\hat{a}$ for particle 1 is

$$
P_+(\hat{a}) = \frac{1}{2}\left(I + \hat{a}\cdot\boldsymbol{\sigma}\right),
$$

and similarly for particle 2 along $\hat{b}$. The joint measurement operator is the tensor product

$$
P_{++}(\hat{a},\hat{b}) = P_+(\hat{a})\otimes P_+(\hat{b}) = \frac{1}{4}\left(I + \hat{a}\cdot\boldsymbol{\sigma}_1\right)\otimes\left(I + \hat{b}\cdot\boldsymbol{\sigma}_2\right),
$$

where $\boldsymbol{\sigma}_1 = \boldsymbol{\sigma}\otimes I$ acts on particle 1, and $\boldsymbol{\sigma}_2 = I\otimes\boldsymbol{\sigma}$ acts on particle 2.

### Step 3: The probability

The joint probability is the Born rule applied to the two-qubit state:

$$
p(+,+) = \langle\Psi^-|\,P_{++}(\hat{a},\hat{b})\,|\Psi^-\rangle.
$$

Expanding the product,

$$
p(+,+) = \frac{1}{4}\Bigl[\langle I\rangle + \langle\hat{a}\cdot\boldsymbol{\sigma}_1\rangle + \langle\hat{b}\cdot\boldsymbol{\sigma}_2\rangle + \langle(\hat{a}\cdot\boldsymbol{\sigma}_1)(\hat{b}\cdot\boldsymbol{\sigma}_2)\rangle\Bigr].
$$

The four expectation values in the singlet state are:

- $\langle I\rangle = 1$.
- $\langle\hat{a}\cdot\boldsymbol{\sigma}_1\rangle = \sum_j a_j\langle\sigma_{1j}\rangle = 0$, because the singlet is rotationally invariant and $\langle\sigma_{1j}\rangle = 0$ for all $j$.
- $\langle\hat{b}\cdot\boldsymbol{\sigma}_2\rangle = 0$, by the same argument.
- $\langle(\hat{a}\cdot\boldsymbol{\sigma}_1)(\hat{b}\cdot\boldsymbol{\sigma}_2)\rangle = \sum_{j,k}a_j b_k\langle\sigma_{1j}\sigma_{2k}\rangle = -\sum_j a_j b_j = -\hat{a}\cdot\hat{b}$.

The last equality uses the standard singlet correlation $\langle\sigma_{1j}\sigma_{2k}\rangle = -\delta_{jk}$.

Substituting,

$$
p(+,+) = \frac{1}{4}\left(1 - \hat{a}\cdot\hat{b}\right).
$$

### Step 4: The result

$$
p(+,+) = \frac{1}{4}\left(1 - \hat{a}\cdot\hat{b}\right).
$$

In terms of the angle $\theta$ between the two directions,

$$
p(+,+) = \frac{1}{4}\left(1 - \cos\theta\right) = \frac{1}{2}\sin^2\!\left(\frac{\theta}{2}\right).
$$

## Solution in the Biquaternion Formulation

### Step 1: The state

In the biquaternion framework, a single-qubit pure state is an idempotent of $\mathbb{M}_+$, of the form $P(\hat{m}) = \tfrac{1}{2}(e_0 + i\hat{m})$. For a **two-qubit system**, the state space is the tensor product $\mathbb{B}\otimes\mathbb{B}$, and a two-qubit pure state is an idempotent of $\mathbb{M}_+\otimes\mathbb{M}_+$.

The singlet state corresponds to the idempotent

$$
P_{\mathrm{singlet}} = \frac{1}{4}\left(e_0\otimes e_0 + e_1\otimes e_1 + e_2\otimes e_2 + e_3\otimes e_3\right).
$$

**Verification.** We check that this is idempotent and of trace $1$ under the tensor-product trace.

*Idempotency.* Using $(x\otimes y)\circ(z\otimes w) = (x\circ z)\otimes(y\circ w)$ and the quaternion multiplication rules,

$$
P_{\mathrm{singlet}}\circ P_{\mathrm{singlet}} = \frac{1}{16}\sum_{j,k=0}^{3}(e_j\circ e_k)\otimes(e_j\circ e_k).
$$

For the diagonal pairs $j = k$, the product $e_j\circ e_j$ equals $e_0$ for $j = 0$ and $-e_0$ for $j = 1, 2, 3$. In both cases the tensor product $(e_j\circ e_j)\otimes(e_j\circ e_j)$ equals $e_0\otimes e_0$, so the four diagonal terms contribute $4\,e_0\otimes e_0$ in total.

For the off-diagonal pairs $j \neq k$, the twelve ordered pairs $(j,k)$ with $j \neq k$ group into six unordered pairs $\{j,k\}$. Each unordered pair contributes two terms to the sum, and in every case the two terms are equal: for pairs involving the identity (of the form $\{0,k\}$), the products $e_0 e_k$ and $e_k e_0$ are both equal to $e_k$, so the two terms $e_k\otimes e_k$ coincide; for pairs not involving the identity (of the form $\{j,k\}$ with $j, k \in \{1,2,3\}$), the products $e_j e_k = \epsilon_{jkl} e_l$ and $e_k e_j = -\epsilon_{jkl} e_l$ are opposites, and the tensor product squares the sign, so again the two terms $e_l\otimes e_l$ coincide. Concretely, the three pairs involving $e_0$ contribute $2\,e_k\otimes e_k$ for $k = 1, 2, 3$, and the three pairs not involving $e_0$ contribute $2\,e_l\otimes e_l$ for $l$ equal to the remaining index. Summing, each of $e_1\otimes e_1$, $e_2\otimes e_2$, $e_3\otimes e_3$ appears four times, and the off-diagonal terms contribute

$$
4\left(e_1\otimes e_1 + e_2\otimes e_2 + e_3\otimes e_3\right).
$$

Combining the diagonal and off-diagonal contributions,

$$
P_{\mathrm{singlet}}\circ P_{\mathrm{singlet}} = \frac{1}{16}\cdot 4\left(e_0\otimes e_0 + e_1\otimes e_1 + e_2\otimes e_2 + e_3\otimes e_3\right) = P_{\mathrm{singlet}}.
$$

*Trace.* The trace is $\mathrm{Tr}(P_{\mathrm{singlet}}) = \frac{1}{4}\sum_{j=0}^{3}\mathrm{Tr}_\mathbb{B}(e_j)^2$. Each $\mathrm{Tr}_\mathbb{B}(e_j) = 2$ for $j = 0$ (since $\mathrm{Tr}_\mathbb{B}(e_0) = 2$) and $0$ for $j = 1, 2, 3$ (since the trace of a pure quaternion vanishes). So the sum is $4$, and $\mathrm{Tr}(P_{\mathrm{singlet}}) = \frac{1}{4}\cdot 4 = 1$.

### Step 2: The measurement operators

The single-qubit projector onto spin-up along $\hat{a}$ is the idempotent $P_+(\hat{a}) = \tfrac{1}{2}(e_0 + i\hat{a})$. The joint measurement operator is the tensor product

$$
P_{++}(\hat{a},\hat{b}) = P_+(\hat{a})\otimes P_+(\hat{b}) = \frac{1}{4}\left(e_0 + i\hat{a}\right)\otimes\left(e_0 + i\hat{b}\right).
$$

### Step 3: The probability

The joint probability is the trace formula on $\mathbb{B}\otimes\mathbb{B}$:

$$
p(+,+) = \mathrm{Tr}\!\left(P_{\mathrm{singlet}}\circ P_{++}(\hat{a},\hat{b})\right).
$$

Computing the product,

$$
P_{\mathrm{singlet}}\circ P_{++} = \frac{1}{16}\sum_{j=0}^{3}\left[e_j(e_0 + i\hat{a})\right]\otimes\left[e_j(e_0 + i\hat{b})\right].
$$

Applying the tensor-product trace,

$$
p(+,+) = \frac{1}{16}\sum_{j=0}^{3}\mathrm{Tr}_\mathbb{B}\!\left[e_j(e_0 + i\hat{a})\right]\cdot\mathrm{Tr}_\mathbb{B}\!\left[e_j(e_0 + i\hat{b})\right].
$$

**Term $j = 0$.** $\mathrm{Tr}_\mathbb{B}(e_0 + i\hat{a}) = 2$, and similarly for $\hat{b}$. Contribution: $2\cdot 2 = 4$.

**Terms $j = 1, 2, 3$.** We have $e_j(e_0 + i\hat{a}) = e_j + ie_j\hat{a}$. The scalar part of $e_j\hat{a}$ is $-\hat{a}_j e_0$, so $\mathrm{Tr}_\mathbb{B}(e_j\hat{a}) = -2\hat{a}_j$ and $\mathrm{Tr}_\mathbb{B}(e_j + ie_j\hat{a}) = -2i\hat{a}_j$. Similarly $\mathrm{Tr}_\mathbb{B}(e_j + ie_j\hat{b}) = -2i\hat{b}_j$. Contribution of term $j$: $(-2i\hat{a}_j)(-2i\hat{b}_j) = -4\hat{a}_j\hat{b}_j$.

Summing over $j = 1, 2, 3$: $-4\,\hat{a}\cdot\hat{b}$.

**Total.** $p(+,+) = \frac{1}{16}\left(4 - 4\,\hat{a}\cdot\hat{b}\right) = \frac{1}{4}\left(1 - \hat{a}\cdot\hat{b}\right)$.

### Step 4: The result

$$
p(+,+) = \frac{1}{4}\left(1 - \hat{a}\cdot\hat{b}\right).
$$

In terms of the angle $\theta$ between the two directions,

$$
p(+,+) = \frac{1}{4}\left(1 - \cos\theta\right) = \frac{1}{2}\sin^2\!\left(\frac{\theta}{2}\right).
$$

## Limiting Cases

Both formulations give the same result, and both give the same limits.

**Case $\hat{a} = \hat{b}$** (both measurements along the same direction, $\theta = 0$). Then

$$
p(+,+) = \frac{1}{4}(1 - 1) = 0.
$$

The two outcomes with the **same sign** have probability $0$, and the two with **different signs** have probability $1/2$ each. Both particles are never found spin-up along the same direction: the singlet has perfectly anti-correlated spins along any common axis.

**Case $\hat{a} = -\hat{b}$** (opposite directions, $\theta = \pi$). Then

$$
p(+,+) = \frac{1}{4}(1 - (-1)) = \frac{1}{2}.
$$

The two outcomes with the **same sign** have probability $1/2$ each, and the two with **different signs** have probability $0$. This is the **opposite** of the previous case, and it is a direct consequence of the perfect anti-correlation along $\hat{a}$: the outcome "spin-up along $\hat{b}$" for particle 2 coincides with "spin-down along $\hat{a}$", so the two spins are found with the same sign label when measured in their respective directions.

**Case $\hat{a} \perp \hat{b}$** (perpendicular directions, $\theta = \pi/2$). Then

$$
p(+,+) = \frac{1}{4}(1 - 0) = \frac{1}{4}.
$$

All four outcomes are equally likely with probability $1/4$, by the symmetry $\hat{a} \to -\hat{a}$, $\hat{b} \to -\hat{b}$ of the singlet state and the perpendicularity $\hat{a}\cdot\hat{b} = 0$.

These agree with the physical expectation: the singlet state is perfectly anti-correlated along any direction, and the joint probabilities depend only on the angle between the two measurement directions.

## What the Biquaternion Solution Illustrates

**1. Entanglement as a non-product state.** The singlet state $P_{\mathrm{singlet}}$ is an element of $\mathbb{B}\otimes\mathbb{B}$ that is **not** of the form $P_1\otimes P_2$ for any single-qubit idempotents $P_1, P_2$. This is the algebraic content of entanglement: the joint state is not a product of the two subsystems' states.

**2. The trace formula generalizes to two qubits.** The joint probability is

$$
p(+,+) = \mathrm{Tr}\!\left(P_{\mathrm{singlet}}\circ P_{++}(\hat{a},\hat{b})\right),
$$

the natural pairing between the joint state and the joint measurement operator. The trace is the tensor product of the single-qubit traces, $\mathrm{Tr}(x\otimes y) = \mathrm{Tr}_\mathbb{B}(x)\cdot\mathrm{Tr}_\mathbb{B}(y)$.

**3. The correlations arise from the tensor-product structure.** The single-qubit projectors $P_+(\hat{a})$ and $P_+(\hat{b})$ are independent, but the joint state $P_{\mathrm{singlet}}$ is entangled. The correlation $\hat{a}\cdot\hat{b}$ enters through the cross terms $\sum_k e_k\otimes e_k$ in the singlet idempotent, which couple the two qubits.

**4. The geometry enters through the algebra.** The angle $\theta$ enters through the scalar product $\hat{a}\cdot\hat{b}$, which appears in the trace formula through the products $e_k\hat{a}$ and $e_k\hat{b}$. The Bloch sphere geometry of each qubit is thus combined into the joint probability through the algebra of $\mathbb{B}\otimes\mathbb{B}$.

**5. The result agrees with the standard formulation.** This is not surprising, because the two formulations are the same mathematics in different notation: $\mathbb{B}\otimes\mathbb{B} \cong M_4(\mathbb{C})$, and the singlet idempotent corresponds exactly to the rank-one projector $|\Psi^-\rangle\langle\Psi^-|$ under the isomorphism. But seeing the same result emerge from the algebra is a useful sanity check on the framework, and it illustrates the structural claim of the companion articles: **the kinematics of two qubits is contained in the tensor product $\mathbb{M}_+\otimes\mathbb{M}_+$, with the Born rule given by the tensor-product trace.**

## Comparison with Exercises: Measuring Spin Along an Arbitrary Direction, Spin Precession in a Magnetic Field and Successive Measurements of Spin

| | Measuring Spin Along an Arbitrary Direction | Spin Precession in a Magnetic Field | Successive Measurements of Spin | Two Spins in the Singlet State |
|---|---|---|---|---|
| System | One qubit | One qubit | One qubit | Two qubits |
| Physical process | Single measurement | Time evolution | Successive measurements | Entangled measurement |
| Structural object | Idempotent + idempotent | Idempotent + unitary | Sequence of idempotents | Idempotent in $\mathbb{B}\otimes\mathbb{B}$ |
| Rule used | Trace formula | Trace formula + rotor conjugation | Product of trace formulas | Tensor-product trace formula |
| Result | $\cos^2(\theta/2)$ | $(\hbar/2)\cos(\omega_L t)$ | $\cos^2(\theta_1/2)\cos^2((\theta_2-\theta_1)/2)$ | $(1/4)(1 - \hat{a}\cdot\hat{b})$ |

These exercises illustrate four fundamental operations of the quantum formalism: **measurement** (Exercise: Measuring Spin Along an Arbitrary Direction), **evolution** (Exercise: Spin Precession in a Magnetic Field), **sequential measurement** (Exercise: Successive Measurements of Spin), and **entangled measurement** (Exercise: Two Spins in the Singlet State). In each case, the biquaternion framework expresses the operation as an algebraic manipulation of the elements of $\mathbb{M}_+$ and $\mathbb{H}_\mathbb{B}$ (and, in Exercise: Two Spins in the Singlet State, their tensor products).

## Summary

We have solved a fourth exercise in quantum mechanics — the joint spin measurement of a singlet state along two arbitrary directions — in two parallel presentations.

In the **standard formulation**, the solution proceeds through the two-qubit state, the tensor-product projector, and the Born rule, giving $p(+,+) = (1/4)(1 - \hat{a}\cdot\hat{b})$.

In the **biquaternion formulation**, the solution proceeds through the singlet idempotent in $\mathbb{B}\otimes\mathbb{B}$, the tensor-product projector, and the trace formula, giving the same result.

The two formulations agree, as they must. The biquaternion formulation makes explicit the algebraic structure of entanglement: the joint state is a **non-product idempotent** of the tensor-product algebra, and the correlations arise from the tensor-product terms in the state.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $\mathbb{M}_+$ | Hermitian subspace (states, observables) |
| $\mathbb{B}\otimes\mathbb{B}$ | Tensor product, isomorphic to $M_4(\mathbb{C})$ |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\boldsymbol{\sigma} = (\sigma_1, \sigma_2, \sigma_3)$ | Pauli matrices |
| $|\Psi^-\rangle$ | Singlet state |
| $P_{\mathrm{singlet}} = \tfrac{1}{4}(e_0\otimes e_0 + \sum_k e_k\otimes e_k)$ | Singlet idempotent |
| $P_+(\hat{a}) = \tfrac{1}{2}(e_0 + i\hat{a})$ | Single-qubit projector |
| $P_{++}(\hat{a},\hat{b}) = P_+(\hat{a})\otimes P_+(\hat{b})$ | Joint projector |
| $\mathrm{Tr}(x\otimes y) = \mathrm{Tr}_\mathbb{B}(x)\cdot\mathrm{Tr}_\mathbb{B}(y)$ | Trace on the tensor product |

## Further Reading

- A. Einstein, B. Podolsky, N. Rosen, "Can quantum-mechanical description of physical reality be considered complete?" *Physical Review* **47** (1935) 777–780, for the original EPR argument.
- J. S. Bell, "On the Einstein–Podolsky–Rosen paradox," *Physics* **1** (1964) 195–200, for the Bell inequalities and the singlet correlations.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the standard treatment of entanglement and Bell states.
- J. J. Sakurai and Jim Napolitano, *Modern Quantum Mechanics* (Pearson, 2017), for the standard textbook treatment of the singlet state.
- The companion articles of this series: *Quantum Mechanics in Biquaternionic Form*, *Spin-1/2 Quantum Mechanics in Biquaternionic Form*, *Exercise: Measuring Spin Along an Arbitrary Direction*, *Exercise: Spin Precession in a Magnetic Field*, and *Exercise: Successive Measurements of Spin*.

