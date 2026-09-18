

# Exercise 6: The Correlation Function of the Bell States

## Introduction

This article is the sixth in a series of **worked exercises** that illustrate quantum mechanics in two parallel presentations: the standard Hilbert-space formulation, and the biquaternion formulation developed in the companion articles. The goal is not to derive new physics, but to give the reader a concrete, computationally explicit demonstration of the correspondence between the two formalisms.

Each exercise in the series is solved twice: first in the standard way, then in the biquaternion way. The results agree, as they must: the two formulations are the same mathematics in different notation. To keep the two solutions strictly parallel, each is presented in the same steps, and the final result is stated in the same form.

The first five exercises treated a single qubit (Exercises 1–3), an entangled pair of qubits in the singlet state (Exercise 4), and the reduced state of one subsystem (Exercise 5). This sixth exercise treats **all four Bell states** — the four maximally entangled two-qubit states — and the **spin correlation function**, the quantity that encodes the full dependence of joint measurement outcomes on the two measurement directions.

The correlation function is the object measured in Bell-inequality experiments. It is also the natural bilinear pairing on the tensor-product algebra, and it reveals a clean structural fact: the four Bell states correspond to the four sign patterns $\epsilon_j = \pm 1$ with $\epsilon_1\epsilon_2\epsilon_3 = +1$, and their correlation functions are $E(\hat a, \hat b) = -\sum_j \epsilon_j\,a_j b_j$.

The conventions are those of the companion articles. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with the Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$. The quaternion units are $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$, and $i$ is the scalar imaginary. The trace of an element of $\mathbb{M}_+$ is twice its scalar part: $\mathrm{Tr}(\tilde{H}) = 2\,\mathrm{Sc}(\tilde{H})$. The two-qubit state space is the tensor product $\mathbb{B}\otimes\mathbb{B}$, isomorphic to $M_4(\mathbb{C})$, with the trace $\mathrm{Tr}(x\otimes y) = \mathrm{Tr}_\mathbb{B}(x)\cdot\mathrm{Tr}_\mathbb{B}(y)$.

## The Exercise

Consider the four **Bell states** of two spin-$\tfrac{1}{2}$ particles:

$$
|\Phi^\pm\rangle = \frac{1}{\sqrt{2}}\left(|\uparrow\uparrow\rangle \pm |\downarrow\downarrow\rangle\right), \qquad
|\Psi^\pm\rangle = \frac{1}{\sqrt{2}}\left(|\uparrow\downarrow\rangle \pm |\downarrow\uparrow\rangle\right).
$$

For two measurement directions $\hat{a}$ and $\hat{b}$, define the **spin correlation function**

$$
E(\hat{a}, \hat{b}) = \langle \left(\hat{a}\cdot\boldsymbol{\sigma}_1\right)\left(\hat{b}\cdot\boldsymbol{\sigma}_2\right)\rangle,
$$

where $\boldsymbol{\sigma}_1 = \boldsymbol{\sigma}\otimes I$ acts on particle 1, and $\boldsymbol{\sigma}_2 = I\otimes\boldsymbol{\sigma}$ acts on particle 2.

Compute $E(\hat{a}, \hat{b})$ for each of the four Bell states. Express the result in the form

$$
E(\hat{a}, \hat{b}) = \sum_{j,k=1}^{3} a_j\,T_{jk}\,b_k = \hat{a}^T T\, \hat{b},
$$

and identify the $3\times 3$ matrix $T$ for each Bell state.

## Solution in the Standard Formulation

### Step 1: The four Bell states

The four Bell states are the maximally entangled two-qubit states

$$
|\Phi^\pm\rangle = \frac{1}{\sqrt{2}}\left(|\uparrow\uparrow\rangle \pm |\downarrow\downarrow\rangle\right), \qquad
|\Psi^\pm\rangle = \frac{1}{\sqrt{2}}\left(|\uparrow\downarrow\rangle \pm |\downarrow\uparrow\rangle\right).
$$

They form an orthonormal basis of the two-qubit Hilbert space $\mathbb{C}^2\otimes\mathbb{C}^2$. The singlet $|\Psi^-\rangle$ was treated in Exercise 4; the other three are its companions.

Each Bell state is a rank-one projector. Using the identity

$$
|\Phi^\pm\rangle\langle\Phi^\pm| = \tfrac{1}{4}\left(I\otimes I \pm \sigma_x\otimes\sigma_x \mp \sigma_y\otimes\sigma_y + \sigma_z\otimes\sigma_z\right),
$$

$$
|\Psi^\pm\rangle\langle\Psi^\pm| = \tfrac{1}{4}\left(I\otimes I \pm \sigma_x\otimes\sigma_x \pm \sigma_y\otimes\sigma_y - \sigma_z\otimes\sigma_z\right),
$$

we may expand each Bell projector in the **Pauli-string basis** $\{I\otimes I, \sigma_j\otimes\sigma_k\}$. The Pauli strings are trace-orthogonal:

$$
\mathrm{Tr}\!\left[(\sigma_j\otimes\sigma_k)(\sigma_l\otimes\sigma_m)\right] = 4\,\delta_{jl}\,\delta_{km}.
$$

### Step 2: The correlation matrix

The correlation function is the expectation of the tensor-product observable $\hat{a}\cdot\boldsymbol{\sigma}_1\otimes\hat{b}\cdot\boldsymbol{\sigma}_2$:

$$
E(\hat{a}, \hat{b}) = \langle\Psi|\left(\sum_j a_j\sigma_j\otimes I\right)\left(\sum_k b_k I\otimes\sigma_k\right)|\Psi\rangle = \sum_{j,k} a_j b_k\,\langle\Psi|\sigma_j\otimes\sigma_k|\Psi\rangle.
$$

So the correlation function is determined by the $3\times 3$ matrix

$$
T_{jk} = \langle\Psi|\sigma_j\otimes\sigma_k|\Psi\rangle = \mathrm{Tr}\!\left(|\Psi\rangle\langle\Psi|\cdot\sigma_j\otimes\sigma_k\right).
$$

Because the Pauli strings are trace-orthogonal, the projector admits the expansion

$$
|\Psi\rangle\langle\Psi| = \tfrac{1}{4}\sum_{j,k} T_{jk}\,\sigma_j\otimes\sigma_k,
$$

and $T_{jk}$ can be read off directly as the coefficient of $\sigma_j\otimes\sigma_k$ inside the bracket. The off-diagonal entries vanish because the Bell projectors contain only the diagonal Pauli strings $\sigma_x\otimes\sigma_x$, $\sigma_y\otimes\sigma_y$, $\sigma_z\otimes\sigma_z$.

### Step 3: Computing $T$ for each Bell state

**Singlet $|\Psi^-\rangle$.** The projector is

$$
|\Psi^-\rangle\langle\Psi^-| = \tfrac{1}{4}\left(I\otimes I - \sigma_x\otimes\sigma_x - \sigma_y\otimes\sigma_y - \sigma_z\otimes\sigma_z\right).
$$

Reading off the coefficients:

$$
T_{11} = T_{22} = T_{33} = -1, \qquad T_{jk} = 0 \text{ for } j \neq k.
$$

So $T_{\Psi^-} = -\mathrm{diag}(1,1,1)$, and $E = -\hat{a}\cdot\hat{b}$. This reproduces the result of Exercise 4.

**State $|\Phi^+\rangle$.** The projector is

$$
|\Phi^+\rangle\langle\Phi^+| = \tfrac{1}{4}\left(I\otimes I + \sigma_x\otimes\sigma_x - \sigma_y\otimes\sigma_y + \sigma_z\otimes\sigma_z\right).
$$

Reading off the coefficients:

$$
T_{11} = +1, \quad T_{22} = -1, \quad T_{33} = +1, \qquad T_{jk} = 0 \text{ for } j \neq k.
$$

So $T_{\Phi^+} = \mathrm{diag}(1,-1,1)$, and $E = a_1 b_1 - a_2 b_2 + a_3 b_3$.

**State $|\Phi^-\rangle$.** The projector is

$$
|\Phi^-\rangle\langle\Phi^-| = \tfrac{1}{4}\left(I\otimes I - \sigma_x\otimes\sigma_x + \sigma_y\otimes\sigma_y + \sigma_z\otimes\sigma_z\right).
$$

Reading off the coefficients:

$$
T_{11} = -1, \quad T_{22} = +1, \quad T_{33} = +1.
$$

So $T_{\Phi^-} = \mathrm{diag}(-1,1,1)$, and $E = -a_1 b_1 + a_2 b_2 + a_3 b_3$.

**State $|\Psi^+\rangle$.** The projector is

$$
|\Psi^+\rangle\langle\Psi^+| = \tfrac{1}{4}\left(I\otimes I + \sigma_x\otimes\sigma_x + \sigma_y\otimes\sigma_y - \sigma_z\otimes\sigma_z\right).
$$

Reading off the coefficients:

$$
T_{11} = +1, \quad T_{22} = +1, \quad T_{33} = -1.
$$

So $T_{\Psi^+} = \mathrm{diag}(1,1,-1)$, and $E = a_1 b_1 + a_2 b_2 - a_3 b_3$.

### Step 4: The result

The four Bell states give the four diagonal correlation matrices:

| Bell state | $T = \mathrm{diag}(T_{11}, T_{22}, T_{33})$ | $E(\hat{a}, \hat{b})$ |
|---|---|---|
| $\|\Psi^-\rangle$ | $\mathrm{diag}(-1,-1,-1)$ | $-\hat{a}\cdot\hat{b}$ |
| $\|\Phi^+\rangle$ | $\mathrm{diag}(+1,-1,+1)$ | $a_1 b_1 - a_2 b_2 + a_3 b_3$ |
| $\|\Phi^-\rangle$ | $\mathrm{diag}(-1,+1,+1)$ | $-a_1 b_1 + a_2 b_2 + a_3 b_3$ |
| $\|\Psi^+\rangle$ | $\mathrm{diag}(+1,+1,-1)$ | $a_1 b_1 + a_2 b_2 - a_3 b_3$ |

Each diagonal entry is $\pm 1$, and the product $T_{11}T_{22}T_{33}$ equals $-1$ in every case. Equivalently, writing $T_{jj} = -\epsilon_j$, the signs satisfy $\epsilon_1\epsilon_2\epsilon_3 = +1$. Only the singlet has $T = -I$, and hence the rotationally invariant correlation $E = -\hat{a}\cdot\hat{b}$.

## Solution in the Biquaternion Formulation

### Step 1: The four Bell idempotents

In the biquaternion framework, a single-qubit pure state is an idempotent of $\mathbb{M}_+$, of the form $P(\hat{m}) = \tfrac{1}{2}(e_0 + i\hat{m})$. A two-qubit pure state is an idempotent of $\mathbb{M}_+\otimes\mathbb{M}_+ \subset \mathbb{B}\otimes\mathbb{B}$.

The four Bell states correspond to the four **Bell idempotents**

$$
P_{\epsilon} = \frac{1}{4}\left(e_0\otimes e_0 + \epsilon_1\,e_1\otimes e_1 + \epsilon_2\,e_2\otimes e_2 + \epsilon_3\,e_3\otimes e_3\right),
$$

where $\epsilon = (\epsilon_1, \epsilon_2, \epsilon_3)$ runs over the four sign patterns with $\epsilon_1\epsilon_2\epsilon_3 = +1$:

| State | $\epsilon = (\epsilon_1, \epsilon_2, \epsilon_3)$ | Biquaternion idempotent |
|---|---|---|
| $\|\Psi^-\rangle$ | $(+1,+1,+1)$ | $\tfrac{1}{4}(e_0\otimes e_0 + e_1\otimes e_1 + e_2\otimes e_2 + e_3\otimes e_3)$ |
| $\|\Phi^+\rangle$ | $(-1,+1,-1)$ | $\tfrac{1}{4}(e_0\otimes e_0 - e_1\otimes e_1 + e_2\otimes e_2 - e_3\otimes e_3)$ |
| $\|\Phi^-\rangle$ | $(+1,-1,-1)$ | $\tfrac{1}{4}(e_0\otimes e_0 + e_1\otimes e_1 - e_2\otimes e_2 - e_3\otimes e_3)$ |
| $\|\Psi^+\rangle$ | $(-1,-1,+1)$ | $\tfrac{1}{4}(e_0\otimes e_0 - e_1\otimes e_1 - e_2\otimes e_2 + e_3\otimes e_3)$ |

**Verification of the general form.** For any sign pattern with $\epsilon_1\epsilon_2\epsilon_3 = +1$, the element $P_\epsilon$ is idempotent and of trace one.

*Idempotency.* The square of $P_\epsilon$ is

$$
P_\epsilon^2 = \frac{1}{16}\sum_{m,m'=0}^{3}\epsilon_m\epsilon_{m'}\,(e_m e_{m'})\otimes(e_m e_{m'}),
$$

with $\epsilon_0 \equiv 1$. We group the sixteen pairs $(m,m')$ into three classes.

**Diagonal pairs $m = m'$.** For $m = 0$, $e_0 e_0 = e_0$; for $m = 1, 2, 3$, $e_m e_m = -e_0$. In all four cases the tensor product $(e_m e_m)\otimes(e_m e_m)$ equals $e_0\otimes e_0$, with coefficient $\epsilon_m^2 = 1$. Contribution: $4\,e_0\otimes e_0$.

**Off-diagonal pairs involving $e_0$.** The pairs $(0,j)$ and $(j,0)$ with $j \in \{1,2,3\}$ both give $e_j\otimes e_j$, with coefficient $\epsilon_j$. Contribution: $2\epsilon_j\,e_j\otimes e_j$ for each $j$.

**Off-diagonal pairs among $\{1,2,3\}$.** For $j \neq k$ in $\{1,2,3\}$, let $l$ be the remaining index. Then $e_j e_k = \epsilon_{jkl}e_l$ and $e_k e_j = -\epsilon_{jkl}e_l$, and the two tensor products are both $e_l\otimes e_l$. The coefficients $\epsilon_j\epsilon_k$ and $\epsilon_k\epsilon_j$ are equal. Contribution: $2\epsilon_j\epsilon_k\,e_l\otimes e_l$.

Collecting, the coefficient of $e_l\otimes e_l$ in $16\,P_\epsilon^2$ is $2\epsilon_l + 2\epsilon_j\epsilon_k$, where $\{j,k,l\} = \{1,2,3\}$. Since

$$
16\,P_\epsilon = 4\,e_0\otimes e_0 + 4\sum_{l=1}^{3}\epsilon_l\,e_l\otimes e_l,
$$

the requirement $P_\epsilon^2 = P_\epsilon$ reduces to

$$
\epsilon_j\epsilon_k = \epsilon_l \qquad \text{for each cyclic triple } (j,k,l).
$$

Multiplying the three equations and using $\epsilon_j^2 = 1$ gives $\epsilon_1\epsilon_2\epsilon_3 = +1$. Conversely, if $\epsilon_1\epsilon_2\epsilon_3 = +1$, multiplying by $\epsilon_1$ gives $\epsilon_2\epsilon_3 = \epsilon_1$, and similarly for the other two cyclic triples. So idempotency holds if and only if $\epsilon_1\epsilon_2\epsilon_3 = +1$.

*Trace.* The trace is

$$
\mathrm{Tr}(P_\epsilon) = \frac{1}{4}\sum_{j=0}^{3}\mathrm{Tr}_\mathbb{B}(e_j)^2 = \frac{1}{4}\cdot 4 = 1,
$$

because $\mathrm{Tr}_\mathbb{B}(e_0) = 2$ and $\mathrm{Tr}_\mathbb{B}(e_j) = 0$ for $j = 1,2,3$.

### Step 2: The correlation observable

The correlation function is the expectation of the tensor-product Hermitian element

$$
\tilde{H}_{ab} = (i\hat{a})\otimes(i\hat{b}),
$$

where $\hat{a} = \sum_j a_j e_j$ and $\hat{b} = \sum_k b_k e_k$ are pure real quaternions. The expectation is given by the tensor-product trace formula:

$$
E(\hat{a}, \hat{b}) = \mathrm{Tr}\!\left(P_\epsilon \circ \tilde{H}_{ab}\right).
$$

### Step 3: Computing the trace for each Bell state

We compute the trace term by term. Multiplying $P_\epsilon$ by $\tilde{H}_{ab}$,

$$
P_\epsilon \circ \tilde{H}_{ab} = \frac{1}{4}\sum_{m=0}^{3}\epsilon_m\,(e_m \cdot i\hat{a})\otimes(e_m \cdot i\hat{b}),
$$

with $\epsilon_0 \equiv 1$.

**Term $m = 0$.** The trace is $\mathrm{Tr}_\mathbb{B}(i\hat{a})\cdot\mathrm{Tr}_\mathbb{B}(i\hat{b}) = 0$, because the scalar part of $i\hat{a}$ vanishes.

**Terms $m = 1, 2, 3$.** We have

$$
e_m\cdot i\hat{a} = i\,e_m \hat{a} = i\left(-a_m e_0 + \text{vector}\right),
$$

using $e_m e_k = -a_m e_0 + \sum_{k \neq m} a_k e_m e_k$. The scalar part is $-i a_m$, so

$$
\mathrm{Tr}_\mathbb{B}(e_m \cdot i\hat{a}) = -2 i a_m,
$$

and similarly $\mathrm{Tr}_\mathbb{B}(e_m\cdot i\hat{b}) = -2 i b_m$. The product of the two traces is

$$
(-2 i a_m)(-2 i b_m) = 4 i^2\, a_m b_m = -4\,a_m b_m.
$$

**Assembly.** Substituting,

$$
E(\hat{a}, \hat{b}) = \frac{1}{4}\sum_{m=1}^{3}\epsilon_m\,(-4\,a_m b_m) = -\sum_{m=1}^{3}\epsilon_m\,a_m b_m.
$$

So the correlation function is

$$
\boxed{\;E(\hat{a}, \hat{b}) = -\epsilon_1\,a_1 b_1 - \epsilon_2\,a_2 b_2 - \epsilon_3\,a_3 b_3.\;}
$$

### Step 4: The result

Applying this formula to the four sign patterns:

| Bell state | $\epsilon = (\epsilon_1,\epsilon_2,\epsilon_3)$ | $E(\hat{a}, \hat{b})$ |
|---|---|---|
| $\|\Psi^-\rangle$ | $(+1,+1,+1)$ | $-a_1 b_1 - a_2 b_2 - a_3 b_3 = -\hat{a}\cdot\hat{b}$ |
| $\|\Phi^+\rangle$ | $(-1,+1,-1)$ | $+a_1 b_1 - a_2 b_2 + a_3 b_3$ |
| $\|\Phi^-\rangle$ | $(+1,-1,-1)$ | $-a_1 b_1 + a_2 b_2 + a_3 b_3$ |
| $\|\Psi^+\rangle$ | $(-1,-1,+1)$ | $+a_1 b_1 + a_2 b_2 - a_3 b_3$ |

These match the standard results exactly.

## Limiting Cases

Both formulations give the same results, and both give the same limits. The cleanest way to read the table is by the direction of the measurements.

**Parallel measurements $\hat{a} = \hat{b} = \hat{n}$.** The correlation is the diagonal entry of $T$ in the direction $\hat{n}$:

| Direction | $\Psi^-$ | $\Phi^+$ | $\Phi^-$ | $\Psi^+$ |
|---|---|---|---|---|
| $\hat{n} = \hat{x}$ | $-1$ | $+1$ | $-1$ | $+1$ |
| $\hat{n} = \hat{y}$ | $-1$ | $-1$ | $+1$ | $+1$ |
| $\hat{n} = \hat{z}$ | $-1$ | $+1$ | $+1$ | $-1$ |

The singlet is the unique Bell state for which the parallel correlation is $-1$ along **every** direction: the singlet is perfectly anti-correlated along any common axis, and its correlation matrix is $-I$. The other three Bell states are perfectly correlated (or anti-correlated) only along the three coordinate axes, with sign patterns that depend on the direction.

**Joint probabilities.** For any Bell state, the four joint probabilities of the measurement outcomes are

$$
p(+,+) = p(-,-) = \tfrac{1}{4}\left(1 + E\right), \qquad p(+,-) = p(-,+) = \tfrac{1}{4}\left(1 - E\right).
$$

This follows from $\langle \sigma_j \otimes I\rangle = \langle I \otimes \sigma_k\rangle = 0$ in every Bell state: the single-particle expectations vanish, and the Born probabilities reduce to $\tfrac{1}{4}(1 \pm E)$. Exercise 4's probability $p(+,+) = \tfrac{1}{4}(1 - \hat{a}\cdot\hat{b})$ is the special case $E = -\hat{a}\cdot\hat{b}$ for the singlet.

**Consistency with Exercise 4.** For the singlet, $E(\hat{a}, \hat{b}) = -\hat{a}\cdot\hat{b}$, so $p(+,+) = \tfrac{1}{4}(1 - \hat{a}\cdot\hat{b})$, recovering Exercise 4.

## What the Biquaternion Solution Illustrates

**1. The four Bell states have a uniform algebraic form.** Each is an idempotent

$$
P_\epsilon = \frac{1}{4}\left(e_0\otimes e_0 + \epsilon_1\,e_1\otimes e_1 + \epsilon_2\,e_2\otimes e_2 + \epsilon_3\,e_3\otimes e_3\right),
$$

with a sign pattern satisfying $\epsilon_1\epsilon_2\epsilon_3 = +1$. This is the algebraic characterization of the Bell basis: four idempotents, differing only by the sign pattern of the three vector-vector terms.

**2. The correlation function is a bilinear pairing.** The correlation function $E(\hat{a}, \hat{b}) = \mathrm{Tr}(P_\epsilon\circ\tilde{H}_{ab})$ is the tensor-product trace pairing between the state idempotent and the observable $\tilde{H}_{ab} = (i\hat{a})\otimes(i\hat{b})$. The trace pairing is the same algebraic operation that gives the Born rule (Exercise 1) and the expectation value (Exercise 2).

**3. The sign pattern encodes the correlation matrix.** In the standard formulation, the correlation matrix $T$ is computed by expanding the Bell projector in the Pauli-string basis and reading off the coefficients. In the biquaternion formulation, the same coefficients appear directly as the signs $\epsilon_j$ in the idempotent. The matrix $T$ is $-\mathrm{diag}(\epsilon_1,\epsilon_2,\epsilon_3)$.

**4. The singlet is the isotropic case.** Among the four Bell states, only the singlet has all signs equal, giving $T = -I$ and the rotationally invariant correlation $E = -\hat{a}\cdot\hat{b}$. The other three break rotational symmetry; their correlation matrices have one sign pattern of the form $(+,-,+)$ up to permutation, and their correlations depend on the direction of the measurements. The four sign patterns with $\epsilon_1\epsilon_2\epsilon_3 = +1$ correspond exactly to the four Bell states, and no other patterns are possible because the idempotency condition enforces the product to be $+1$.

**5. The result agrees with the standard formulation.** This is not surprising, because the two formulations are the same mathematics in different notation: $\mathbb{B}\otimes\mathbb{B} \cong M_4(\mathbb{C})$, and the Bell idempotent $P_\epsilon$ corresponds exactly to the rank-one projector $|\Psi_\epsilon\rangle\langle\Psi_\epsilon|$ under the isomorphism. But seeing the same result emerge from the algebra is a useful sanity check, and it illustrates the structural claim of the companion articles: **the kinematics of two-qubit entanglement is contained in the tensor-product algebra $\mathbb{B}\otimes\mathbb{B}$, with the Born rule given by the tensor-product trace, and the four Bell states are the four idempotents with sign pattern satisfying $\epsilon_1\epsilon_2\epsilon_3 = +1$.**

## Comparison with Exercises 1–5

| | Exercise 1 | Exercise 2 | Exercise 3 | Exercise 4 | Exercise 5 | Exercise 6 |
|---|---|---|---|---|---|---|
| System | One qubit | One qubit | One qubit | Two qubits | Two qubits | Two qubits |
| Physical process | Single measurement | Evolution | Successive measurements | Singlet measurement | Reduced state | Correlation function |
| Structural object | Idempotent + idempotent | Idempotent + unitary | Sequence of idempotents | Idempotent in $\mathbb{B}\otimes\mathbb{B}$ | Partial trace | Bell idempotents |
| Rule used | Trace formula | Trace formula + rotor conjugation | Product of trace formulas | Tensor-product trace formula | Partial trace + trace formula | Tensor-product trace pairing |
| Result | $\cos^2(\theta/2)$ | $(\hbar/2)\cos(\omega_L t)$ | $\cos^2(\theta_1/2)\cos^2((\theta_2-\theta_1)/2)$ | $(1/4)(1 - \hat{a}\cdot\hat{b})$ | $\rho_1 = \tfrac{1}{2}e_0$ | $E = -\sum_j \epsilon_j a_j b_j$ |

## Summary

We have solved a sixth exercise in quantum mechanics — the spin correlation function of the four Bell states — in two parallel presentations.

In the **standard formulation**, the solution proceeds through the four Bell projectors, their expansions in the Pauli-string basis, and the trace-orthogonality of the Pauli strings, giving the four diagonal correlation matrices $T = \mathrm{diag}(\pm 1, \pm 1, \pm 1)$ and the correlation functions $E = \hat{a}^T T\hat{b}$.

In the **biquaternion formulation**, the solution proceeds through the four Bell idempotents $P_\epsilon$ in $\mathbb{B}\otimes\mathbb{B}$, the correlation observable $(i\hat{a})\otimes(i\hat{b})$, and the tensor-product trace pairing, giving the general formula $E = -\sum_j \epsilon_j a_j b_j$ for the sign pattern $\epsilon$ with $\epsilon_1\epsilon_2\epsilon_3 = +1$.

The two formulations agree, as they must. The biquaternion formulation makes explicit the algebraic structure of the Bell basis: the four Bell states are the four idempotents with the sign pattern $\epsilon_1\epsilon_2\epsilon_3 = +1$; the correlation function is the tensor-product trace pairing between the state idempotent and the correlation observable; and the singlet is the unique Bell state with the rotationally invariant correlation $E = -\hat{a}\cdot\hat{b}$.

The correlation function is the object measured in Bell-inequality experiments, and the four correlation matrices exhibited here are the full content of the two-qubit spin correlations in the Bell basis.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $\mathbb{M}_+$ | Hermitian subspace (states, observables) |
| $\mathbb{B}\otimes\mathbb{B}$ | Tensor product, isomorphic to $M_4(\mathbb{C})$ |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\boldsymbol{\sigma} = (\sigma_1, \sigma_2, \sigma_3)$ | Pauli matrices |
| $\boldsymbol{\sigma}_1 = \boldsymbol{\sigma}\otimes I$ | Spin operator on particle 1 |
| $\boldsymbol{\sigma}_2 = I\otimes\boldsymbol{\sigma}$ | Spin operator on particle 2 |
| $\|\Phi^\pm\rangle, \|\Psi^\pm\rangle$ | The four Bell states |
| $P_\epsilon = \tfrac{1}{4}(e_0\otimes e_0 + \sum_j \epsilon_j\,e_j\otimes e_j)$ | Bell idempotent, with $\epsilon_1\epsilon_2\epsilon_3 = +1$ |
| $\tilde{H}_{ab} = (i\hat{a})\otimes(i\hat{b})$ | Correlation observable |
| $E(\hat{a}, \hat{b}) = \mathrm{Tr}(P_\epsilon\circ\tilde{H}_{ab})$ | Correlation function |
| $T_{jk} = \langle\Psi\|\sigma_j\otimes\sigma_k\|\Psi\rangle$ | Correlation matrix |
| $\mathrm{Tr}(x\otimes y) = \mathrm{Tr}_\mathbb{B}(x)\cdot\mathrm{Tr}_\mathbb{B}(y)$ | Trace on the tensor product |

## Further Reading

- A. Einstein, B. Podolsky, N. Rosen, "Can quantum-mechanical description of physical reality be considered complete?" *Physical Review* **47** (1935) 777–780, for the original EPR argument.
- J. S. Bell, "On the Einstein–Podolsky–Rosen paradox," *Physics* **1** (1964) 195–200, for the Bell inequalities and the singlet correlations.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the standard treatment of the Bell basis and the correlation function.
- J. J. Sakurai and Jim Napolitano, *Modern Quantum Mechanics* (Pearson, 2017), for the standard textbook treatment of two-spin correlations.
- The companion articles of this series: *Quantum Mechanics in Biquaternionic Form*, *Spin-1/2 Quantum Mechanics in Biquaternionic Form*, *Exercise 1: Measuring Spin Along an Arbitrary Direction*, *Exercise 2: Spin Precession in a Magnetic Field*, *Exercise 3: Successive Measurements of Spin*, *Exercise 4: Two Spins in the Singlet State*, and *Exercise 5: The Reduced State of an Entangled Subsystem*.

