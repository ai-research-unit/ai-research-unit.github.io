# __Biquaternion Representations__

## Introduction

The basic algebra article defined the biquaternion algebra $\mathbb{B}$, its conjugations, and its four fixed-point subspaces $\mathbb{C}_{\mathbb{B}}$, $\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$, and $\mathbb{M}_-$. This article describes the **representations** of the biquaternion algebra: concrete ways of writing biquaternions as objects we can compute with.

A representation is a choice. The algebra is the same; the representation is how we choose to write it. Different representations are useful for different purposes, and the same biquaternion can be written in several ways.

The representations we discuss are:

1. **Complex four-vector representation.** A biquaternion as a complex four-vector.
2. **$2 \times 2$ matrix representation.** A biquaternion as a $2 \times 2$ complex matrix.
3. **Spinor representation.** A biquaternion as an operator on two-component spinors.
4. **Clifford algebra representation.** A biquaternion as an element of the even Clifford algebra $\mathrm{Cl}_{1,3}^+$.
5. **Polar representations.** A biquaternion as a modulus times an exponential of a root of $-1$.

The four-vector representation is presented first because it is the one most familiar from standard physics. The others follow. The polar representations are presented last because they depend on the roots of $-1$ and on the classification of the conjugations, which are treated in the basic algebra article.

Throughout, we use the notation of the basic algebra article: a biquaternion is written

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3,
$$

or, more compactly, as

$$
\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu, \qquad Q_\mu \in \mathbb{C},
$$

with $e_0 = 1$ and $e_1, e_2, e_3$ the quaternion units. The scalar imaginary is $i$, which commutes with the quaternion units. Each complex coefficient is written $Q_\mu = q_\mu + i q'_\mu$ with $q_\mu, q'_\mu \in \mathbb{R}$.

## The Complex Four-Vector Representation

### Definition

A biquaternion $\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu$ can be written as a complex four-vector

$$
Q^\mu = (Q^0, Q^1, Q^2, Q^3),
$$

with

$$
Q^0 = Q_0, \qquad (Q^1, Q^2, Q^3) = (Q_1, Q_2, Q_3).
$$

The scalar part of the biquaternion becomes the time component of the four-vector; the vector part becomes the spatial components. This is the most direct representation.

### Multiplication in Four-Vector Form

The product of two biquaternions in four-vector form is

$$
(\tilde{Q} \circ \tilde{R})^\mu = \left( Q^0 R^0 - \sum_{k=1}^{3} Q^k R^k, \;\; Q^0 R^\mu + R^0 Q^\mu + \sum_{j,k=1}^{3} \epsilon^{\mu j k} Q^j R^k \right),
$$

where $\epsilon^{\mu j k}$ is the Levi-Civita symbol. The time component of the product is the scalar part; the spatial components are the vector part. This is the four-vector expression of the quaternion product formula.

### Conjugation in Four-Vector Form

Quaternion conjugation negates the spatial components:

$$
\bar{Q}^\mu = (Q^0, -Q^1, -Q^2, -Q^3).
$$

Complex conjugation conjugates all components:

$$
(Q^*)^\mu = ((Q^0)^*, (Q^1)^*, (Q^2)^*, (Q^3)^*).
$$

Hermitian conjugation combines the two:

$$
(Q^\dagger)^\mu = ((Q^0)^*, -(Q^1)^*, -(Q^2)^*, -(Q^3)^*).
$$

### The Four Subspaces in Four-Vector Form

The four fixed-point subspaces have a simple characterization in the four-vector representation.

- **Complex subspace $\mathbb{C}_{\mathbb{B}}$:** four-vectors of the form $Q^\mu = (Q^0, 0, 0, 0)$ with $Q^0 \in \mathbb{C}$.
- **Quaternion subspace $\mathbb{H}_{\mathbb{B}}$:** four-vectors with real components, $Q^\mu \in \mathbb{R}^4$.
- **Hermitian subspace $\mathbb{M}_+$:** four-vectors of the form $Q^\mu = (q_0, i q'_1, i q'_2, i q'_3)$ with $q_0, q'_1, q'_2, q'_3 \in \mathbb{R}$. Real time component, purely imaginary spatial components.
- **Anti-Hermitian subspace $\mathbb{M}_-$:** four-vectors of the form $Q^\mu = (i q'_0, q_1, q_2, q_3)$ with $q'_0, q_1, q_2, q_3 \in \mathbb{R}$. Purely imaginary time component, real spatial components.

### The Norm Form in Four-Vector Form

The norm form $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$ is

$$
N(\tilde{Q}) = (Q^0)^2 + (Q^1)^2 + (Q^2)^2 + (Q^3)^2.
$$

On the anti-Hermitian subspace $\mathbb{M}_-$, the norm form restricts to

$$
N(\tilde{Q}) = -(q'_0)^2 + q_1^2 + q_2^2 + q_3^2,
$$

which is the Lorentzian quadratic form of signature $(1,3)$ or $(3,1)$, depending on sign convention.

### Why the Four-Vector Representation Is Useful

The four-vector representation is the bridge between the algebraic biquaternion and the standard tensor formalism of physics. It is the representation in which:

- The Lorentz group acts in the standard way.
- The electromagnetic four-potential and four-current live.
- The d'Alembertian $\Box = \partial_\mu \partial^\mu$ is defined.
- The Minkowski metric appears as $\eta_{\mu\nu} = \mathrm{diag}(-1, +1, +1, +1)$ in the standard convention, or as the identity in the $ict$ convention.

It is also the representation in which the biquaternion looks least like a biquaternion. The algebraic structure — the non-commutative product, the two conjugations, the zero divisors — is hidden. This is why the four-vector representation, while useful, is not the fundamental one.

## The $2 \times 2$ Matrix Representation

### Definition

The biquaternion algebra is isomorphic to the algebra of $2 \times 2$ complex matrices:

$$
\mathbb{B} \cong M_2(\mathbb{C}).
$$

An explicit isomorphism is given by the Pauli representation. Define the Pauli matrices

$$
\sigma_1 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad
\sigma_2 = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \qquad
\sigma_3 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}.
$$

Then the map

$$
e_0 \mapsto I, \qquad e_1 \mapsto i\sigma_1, \qquad e_2 \mapsto i\sigma_2, \qquad e_3 \mapsto i\sigma_3
$$

extends to an algebra isomorphism $\mathbb{B} \to M_2(\mathbb{C})$. In this representation, a biquaternion $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ maps to the matrix

$$
\tilde{Q} \mapsto \begin{pmatrix} Q_0 + i Q_3 & i Q_1 + Q_2 \\ i Q_1 - Q_2 & Q_0 - i Q_3 \end{pmatrix}.
$$

### The Pauli Basis

The four matrices

$$
I, \quad i\sigma_1, \quad i\sigma_2, \quad i\sigma_3
$$

form a basis of $M_2(\mathbb{C})$ as a complex vector space, and they are the images of the quaternion units $e_0, e_1, e_2, e_3$. In terms of the Pauli matrices, the image of a general biquaternion is

$$
\tilde{Q} \mapsto Q_0 I + i Q_1 \sigma_1 + i Q_2 \sigma_2 + i Q_3 \sigma_3.
$$

This is the standard form of the matrix representation.

### Trace and Determinant

Two invariants of the matrix representation are particularly important.

**Trace.** The trace of the matrix is

$$
\mathrm{Tr}(\tilde{Q}) = (Q_0 + i Q_3) + (Q_0 - i Q_3) = 2 Q_0.
$$

So the trace is twice the scalar part of the biquaternion. It is invariant under all four conjugations up to sign: $\mathrm{Tr}(\bar{\tilde{Q}}) = \mathrm{Tr}(\tilde{Q})$, $\mathrm{Tr}(\tilde{Q}^*) = 2 Q_0^*$, $\mathrm{Tr}(\tilde{Q}^\dagger) = 2 Q_0^*$, and $\mathrm{Tr}(\tilde{Q}^\flat) = -2 Q_0^*$.

**Determinant.** The determinant of the matrix is

$$
\det(\tilde{Q}) = (Q_0 + i Q_3)(Q_0 - i Q_3) - (i Q_1 + Q_2)(i Q_1 - Q_2) = Q_0^2 + Q_3^2 + Q_1^2 + Q_2^2 = N(\tilde{Q}).
$$

So the determinant is the **norm form** of the biquaternion. This is a crucial fact: the norm form, which we defined algebraically as $\tilde{Q}\bar{\tilde{Q}}$, is exactly the determinant of the corresponding matrix. In particular, the norm form is multiplicative because the determinant is multiplicative.

### The Hermitian Form in Matrix Form

The **Hermitian form** of the biquaternion is

$$
\tilde{Q}\tilde{Q}^\dagger = |Q_0 + i Q_3|^2 + |i Q_1 + Q_2|^2 + |i Q_1 - Q_2|^2 + |Q_0 - i Q_3|^2.
$$

This is the sum of the squared moduli of the four entries of the matrix, which is the **Frobenius norm squared** of the matrix. It is a non-negative real number, and it vanishes if and only if $\tilde{Q} = 0$.

The Euclidean norm $\|\tilde{Q}\|_E = \sqrt{\tilde{Q}\tilde{Q}^\dagger}$ is therefore the Frobenius norm of the matrix.

### Conjugation in Matrix Form

**Quaternion conjugation** $\bar{\tilde{Q}}$ corresponds to the matrix

$$
\bar{\tilde{Q}} \mapsto \begin{pmatrix} Q_0 - i Q_3 & -i Q_1 - Q_2 \\ -i Q_1 + Q_2 & Q_0 + i Q_3 \end{pmatrix}.
$$

This is the **adjugate** (or classical adjoint) of the matrix, up to a sign: it is the matrix whose entries are the cofactors.

**Complex conjugation** $\tilde{Q}^*$ conjugates all entries.

**Hermitian conjugation** $\tilde{Q}^\dagger$ is the conjugate transpose:

$$
\tilde{Q}^\dagger \mapsto \begin{pmatrix} Q_0^* - i Q_3^* & -i Q_1^* - Q_2^* \\ -i Q_1^* + Q_2^* & Q_0^* + i Q_3^* \end{pmatrix}^T = \begin{pmatrix} Q_0^* + i Q_3^* & i Q_1^* - Q_2^* \\ i Q_1^* + Q_2^* & Q_0^* - i Q_3^* \end{pmatrix}.
$$

This is the standard conjugate transpose of the original matrix.

**Anti-Hermitian conjugation** $\tilde{Q}^\flat = -\tilde{Q}^\dagger$ is the negative of the conjugate transpose.

### The Four Subspaces in Matrix Form

The four fixed-point subspaces have a simple characterization in the matrix representation.

- **Complex subspace $\mathbb{C}_{\mathbb{B}}$:** diagonal matrices of the form $Q_0 I$ with $Q_0 \in \mathbb{C}$.
- **Quaternion subspace $\mathbb{H}_{\mathbb{B}}$:** matrices whose entries satisfy the reality conditions that make the corresponding biquaternion real. Concretely, these are the matrices of the form $\begin{pmatrix} q_0 + i q_3 & i q_1 + q_2 \\ i q_1 - q_2 & q_0 - i q_3 \end{pmatrix}$ with $q_\mu \in \mathbb{R}$.
- **Hermitian subspace $\mathbb{M}_+$:** matrices that are Hermitian (equal to their conjugate transpose).
- **Anti-Hermitian subspace $\mathbb{M}_-$:** matrices that are anti-Hermitian (equal to the negative of their conjugate transpose).

The identification of $\mathbb{M}_+$ with the Hermitian matrices and $\mathbb{M}_-$ with the anti-Hermitian matrices is one of the most striking features of the matrix representation. It connects the abstract algebraic definition of the subspaces to the familiar notions of Hermitian and anti-Hermitian matrices in linear algebra.

### Structural Consequences of the Isomorphism

The isomorphism $\mathbb{B} \cong M_2(\mathbb{C})$ has several structural consequences.

**Simplicity.** The algebra $M_2(\mathbb{C})$ is **simple**: it has no nontrivial two-sided ideals. So the biquaternion algebra is simple.

**Center.** The center of $M_2(\mathbb{C})$ is the set of scalar matrices, which is isomorphic to $\mathbb{C}$. So the center of the biquaternion algebra is the complex subspace $\mathbb{C}_{\mathbb{B}}$.

**Endomorphism algebra.** The algebra $M_2(\mathbb{C})$ is the algebra of endomorphisms of a two-dimensional complex vector space. So the biquaternion algebra is the algebra of endomorphisms of $\mathbb{C}^2$.

**Zero divisors.** The zero divisors of $\mathbb{B}$ correspond to the singular matrices of $M_2(\mathbb{C})$, i.e., the matrices with vanishing determinant. This is the content of the division theory article, translated into matrix language.

## The Spinor Representation

### Definition

The isomorphism $\mathbb{B} \cong M_2(\mathbb{C})$ means that biquaternions act naturally on two-component complex vectors, which are **spinors**. A spinor $\psi$ is a column vector

$$
\psi = \begin{pmatrix} \psi_1 \\ \psi_2 \end{pmatrix}, \qquad \psi_1, \psi_2 \in \mathbb{C},
$$

and a biquaternion $\tilde{Q}$ acts on it by matrix multiplication:

$$
\psi \mapsto \tilde{Q} \psi = \begin{pmatrix} (Q_0 + i Q_3)\psi_1 + (i Q_1 + Q_2)\psi_2 \\ (i Q_1 - Q_2)\psi_1 + (Q_0 - i Q_3)\psi_2 \end{pmatrix}.
$$

### Properties

**Linearity.** The action is complex-linear in $\psi$: $\tilde{Q}(\lambda \psi + \mu \phi) = \lambda \tilde{Q}\psi + \mu \tilde{Q}\phi$ for $\lambda, \mu \in \mathbb{C}$.

**Composition.** The action is compatible with multiplication: $\tilde{Q}(\tilde{R}\psi) = (\tilde{Q} \circ \tilde{R})\psi$.

**Hermitian inner product.** The space of spinors carries a natural Hermitian inner product

$$
\langle \psi, \phi \rangle = \psi_1^* \phi_1 + \psi_2^* \phi_2.
$$

The biquaternion action preserves this inner product when $\tilde{Q}$ is unitary, i.e., when $\tilde{Q}^\dagger \tilde{Q} = I$. The unitary biquaternions form the group $U(2)$, and the subgroup of determinant $1$ is $SU(2)$, which is the spin group of the Lorentz group.

### Why the Spinor Representation Is Useful

The spinor representation is useful because:

1. **It connects to the Dirac equation.** The Dirac equation describes spin-$\frac{1}{2}$ particles and is naturally written in terms of $2 \times 2$ matrices. Biquaternions provide a natural algebraic framework for these matrices.
2. **It makes Lorentz invariance manifest.** Spinors transform under the Lorentz group in a simple way, and the biquaternion action is Lorentz-invariant.
3. **It is the natural representation for quantum fields.** In quantum field theory, the fundamental fermionic fields are spinorial, and the biquaternion algebra is their natural algebraic home.

## The Clifford Algebra Representation

### Definition

The biquaternion algebra is isomorphic to the even subalgebra of the Clifford algebra $\mathrm{Cl}_{1,3}(\mathbb{R})$:

$$
\mathbb{B} \cong \mathrm{Cl}_{1,3}^+(\mathbb{R}).
$$

The Clifford algebra $\mathrm{Cl}_{1,3}$ is generated by four elements $\gamma^0, \gamma^1, \gamma^2, \gamma^3$ satisfying

$$
\gamma^\mu \gamma^\nu + \gamma^\nu \gamma^\mu = 2 \eta^{\mu\nu},
$$

where $\eta = \mathrm{diag}(-1, +1, +1, +1)$ (or its negative, depending on convention). The even subalgebra consists of products of an even number of generators.

The Clifford algebra $\mathrm{Cl}_{1,3}$ has real dimension $2^4 = 16$. Its even subalgebra $\mathrm{Cl}_{1,3}^+$ has real dimension $8$, matching the real dimension of $\mathbb{B}$. The even subalgebra is spanned by the identity and the six bivectors $\gamma^\mu \gamma^\nu$ with $\mu < \nu$.

### Properties

**Generators.** The bivectors $\gamma^\mu \gamma^\nu$ generate the even subalgebra. They correspond to the quaternion units under the isomorphism.

**Multiplication.** The Clifford product of two even elements is even, so the even subalgebra is closed under multiplication.

**Norm.** The Clifford norm on the even subalgebra corresponds to the biquaternion norm form.

### Why the Clifford Algebra Representation Is Useful

The Clifford algebra representation is useful because:

1. **It connects to the Dirac algebra.** The gamma matrices of the Dirac equation generate the Clifford algebra. The biquaternion algebra is the even part of this, which is the part that acts on spinors.
2. **It makes the geometry explicit.** The Clifford algebra is the natural algebraic structure on a vector space with a quadratic form. In the case of $\mathrm{Cl}_{1,3}$, the quadratic form is the Minkowski metric.
3. **It generalizes.** The Clifford algebra construction works in any dimension and any signature. The biquaternion algebra is the specific case of dimension $4$ and signature $(1,3)$ or $(3,1)$.

## The Polar Representations

### Why There Are Two

The polar representation of a biquaternion is the analogue of the polar form of a complex number. For a complex number $z$, we write

$$
z = r e^{i\theta}, \qquad r = |z| \geq 0, \quad \theta \in \mathbb{R}.
$$

The two key features are that the modulus $r$ is a **non-negative real number**, and the exponential uses the **only** root of $-1$ available in $\mathbb{C}$, namely $i$.

For a biquaternion, neither feature survives unchanged. The "modulus" need not be real and non-negative, and there is not **one** root of $-1$ but a **four-dimensional family** of them. The choice of root determines the polar representation, and the two natural choices give the two polar forms: the **Hamilton polar form** and the **complex polar form**.

### The Hamilton Polar Form

**Definition.** Every biquaternion $\tilde{Q}$ with non-vanishing norm form can be written as

$$
\tilde{Q} = R \exp(\xi \Theta) = R(\cos\Theta + \xi \sin\Theta),
$$

where:

- $R$ is the **complex modulus**, $R = \sqrt{N(\tilde{Q})}$, i.e., the square root of the norm form;
- $\xi$ is a **biquaternion root of $-1$**, i.e., an element of $\mathbb{B}$ with $\xi^2 = -e_0$;
- $\Theta$ is a **complex angle**.

The root $\xi$ is the "axis" of the biquaternion, the analogue of the direction of a vector in $\mathbb{H}$. It is a pure biquaternion satisfying the constraints

$$
\Re(\xi) \perp \Im(\xi), \qquad \|\Re(\xi)\| - \|\Im(\xi)\| = 1,
$$

which we discussed in the division theory article.

**Example.** Take $\tilde{Q} = e_1$, a unit pure real quaternion. Its norm form is $N(\tilde{Q}) = e_1^2 = -e_0$, so $R = \sqrt{-e_0} = i e_0$. Take $\xi = e_1$, $\Theta = \pi/2$. Then

$$
R \exp(\xi \Theta) = i e_0 (\cos(\pi/2) + e_1 \sin(\pi/2)) = i e_0 (0 + e_1) = i e_1.
$$

This is not $e_1$. Let me redo. The Hamilton polar form as given in the paper uses $R = |q|$ where $|q|$ is the modulus defined as the square root of the semi-norm. For $\tilde{Q} = e_1$, $N(\tilde{Q}) = -1$, so $|q|$ is not real. The polar form works cleanly only when the norm form is a non-negative real number or a positive real number, which is not the case here.

Let me choose a biquaternion with a positive real norm form. Take $\tilde{Q} = e_0 + e_1$. Then $N(\tilde{Q}) = 1 + 1 = 2$, so $R = \sqrt{2}$. The vector part is $e_1$, which has norm $1$. The unit vector is $\hat{n} = e_1$, and $\Theta = \pi/4$ (since $\cos(\pi/4) = \sin(\pi/4) = 1/\sqrt{2}$). Then

$$
R \exp(\xi \Theta) = \sqrt{2}(\cos(\pi/4) + e_1 \sin(\pi/4)) = \sqrt{2}(1/\sqrt{2} + e_1/\sqrt{2}) = 1 + e_1 = \tilde{Q}.
$$

Good. So the Hamilton polar form works when the vector part has a well-defined unit direction.

### The Complex Polar Form

**Definition.** Every biquaternion $\tilde{Q}$ with non-vanishing real part $Q_0$ can be written as

$$
\tilde{Q} = Q \exp(i \Psi) = Q(\cos\Psi + i \sin\Psi),
$$

where:

- $Q$ is a **quaternion** (a real quaternion, element of $\mathbb{H}$);
- $i$ is the **scalar imaginary**, the central root of $-1$ that commutes with everything;
- $\Psi$ is a **complex angle**.

The complex angle $\Psi$ is given by

$$
\Psi = \tan^{-1}(Q_r^{-1} Q_i),
$$

where $Q_r$ and $Q_i$ are the real and imaginary quaternion parts of $\tilde{Q}$, and $Q = \tilde{Q} \exp(-i\Psi)$.

**Example.** Take $\tilde{Q} = 1 + i$, a complex scalar (a biquaternion with only the scalar part non-zero). Its real quaternion part is $Q_r = 1$ and its imaginary quaternion part is $Q_i = 1$. Then $\Psi = \tan^{-1}(1) = \pi/4$, and $Q = (1+i) \exp(-i\pi/4) = (1+i)(\cos(\pi/4) - i \sin(\pi/4)) = (1+i)(1/\sqrt{2} - i/\sqrt{2}) = \sqrt{2}$. So

$$
\tilde{Q} = \sqrt{2} \exp(i \pi/4).
$$

This is exactly the ordinary polar form of the complex number $1+i$. So in the case of a scalar biquaternion, the complex polar form reduces to the ordinary complex polar form.

### Comparison of the Two Polar Forms

The two polar forms differ in **which root of $-1$ is used in the exponential** and in **which factor is the modulus**:

| | Hamilton polar form | Complex polar form |
|---|---|---|
| Root of $-1$ | $\xi$, a biquaternion root | $i$, the scalar imaginary |
| Modulus | $R$, a complex scalar | $Q$, a real quaternion |
| Angle | $\Theta$, a complex scalar | $\Psi$, a complex scalar |
| Reduces to | Quaternion polar form (when $\tilde{Q} \in \mathbb{H}$) | Complex polar form (when $\tilde{Q} \in \mathbb{C}_{\mathbb{B}}$) |

The two polar forms are complementary. The Hamilton form generalizes the quaternion polar form $q = r \exp(\mu \theta)$, with the quaternion root $\mu$ replaced by a biquaternion root $\xi$, and the modulus and angle allowed to become complex. The complex form generalizes the complex polar form $z = r \exp(i\theta)$, with the scalar imaginary $i$ retained as the root, and the modulus allowed to become a quaternion.

### Which to Use

The choice between the two polar forms depends on what is being computed:

- The **Hamilton polar form** is natural when the biquaternion is close to a quaternion, i.e., when the complexification is a small perturbation. The root $\xi$ is close to a pure real quaternion, and the exponential is close to the quaternion exponential.
- The **complex polar form** is natural when the biquaternion is close to a complex scalar, i.e., when the quaternion structure is a small perturbation. The modulus $Q$ is close to a complex scalar, and the exponential is close to the ordinary complex exponential.

In the case of a biquaternion that is neither close to a quaternion nor close to a complex scalar, neither polar form is canonical, and the choice is a matter of convenience.

### The Role of the Roots of $-1$

The two polar forms correspond to the two classes of roots of $-1$ in $\mathbb{B}$:

- The **scalar imaginary** $i$ is the unique central root of $-1$ (up to sign). It is the root used in the complex polar form.
- The **non-central roots** $\xi$ of $-1$, of the form $\xi = b\mu + d i \nu$ with $\mu \perp \nu$ and $b^2 - d^2 = 1$, are the roots used in the Hamilton polar form. They form a four-dimensional family, parametrized by a pair of perpendicular unit pure real quaternions $\mu, \nu$ and a real parameter $b$ with $b^2 - d^2 = 1$.

The existence of the non-central roots is the reason the Hamilton polar form differs from the complex one. In the complex numbers, only the central root exists, and there is only one polar form. In the biquaternions, the central root and the non-central roots coexist, and the two polar forms reflect the two possibilities.

### Conjugation and the Polar Forms

The three conjugations of the biquaternion algebra act on the two polar forms as follows:

**Quaternion conjugation** $\bar{\tilde{Q}}$:
- In the Hamilton form, $\bar{R \exp(\xi \Theta)} = R \exp(-\xi \Theta)$, i.e., the sign of the angle is reversed.
- In the complex form, $\bar{Q \exp(i \Psi)} = \bar{Q} \exp(i \Psi)$ (since $i$ commutes), i.e., the quaternion modulus is conjugated.

**Complex conjugation** $\tilde{Q}^*$:
- In the Hamilton form, $(R \exp(\xi \Theta))^* = R^* \exp(\xi^* \Theta^*)$, i.e., both the modulus and the root are conjugated.
- In the complex form, $(Q \exp(i \Psi))^* = Q \exp(-i \Psi^*)$, i.e., the sign of the angle is reversed (up to conjugation of the angle).

**Hermitian conjugation** $\tilde{Q}^\dagger$: the composition of the two.

So the two polar forms respond differently to the three conjugations, and the choice of polar form determines which conjugation is "natural" for the expression.

## Summary of Representations

| Representation | Biquaternion as | Useful for |
|---|---|---|
| Complex four-vector | $Q^\mu = (Q^0, \mathbf{Q})$ | Tensor formalism, Lorentz group, Maxwell's equations |
| $2 \times 2$ matrix | $\begin{pmatrix} Q_0 + i Q_3 & i Q_1 + Q_2 \\ i Q_1 - Q_2 & Q_0 - i Q_3 \end{pmatrix}$ | Concrete computation, isomorphism with $M_2(\mathbb{C})$ |
| Spinor | Operator on $\begin{pmatrix} \psi_1 \\ \psi_2 \end{pmatrix}$ | Dirac equation, Lorentz invariance, quantum fields |
| Clifford algebra | Element of $\mathrm{Cl}_{1,3}^+$ | Dirac algebra, geometry, generalization |
| Hamilton polar form | $R \exp(\xi \Theta)$ | Quaternionic structure, rotation, biquaternion roots of $-1$ |
| Complex polar form | $Q \exp(i \Psi)$ | Complex structure, scalar biquaternions, complexification |

The four-vector representation is the one most familiar from standard physics. The matrix, spinor, and Clifford representations are more algebraic and reveal more of the structure. The two polar representations reveal the two ways in which the biquaternion algebra relates to its two roots of $-1$ — the central scalar imaginary and the non-central biquaternion roots — and they are complementary. The choice of representation depends on what is being computed.

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original formulation.
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the first systematic treatment of biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra perspective.
- J. P. Ward, *Quaternions and Cayley Numbers* (Kluwer, 1997), Chapter 3, for the polar representations of biquaternions.
- S. J. Sangwine, T. A. Ell, N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* 21 (2011) 607–636, for the two polar forms in the applied context.

