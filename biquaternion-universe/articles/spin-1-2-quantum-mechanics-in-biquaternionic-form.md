
# __Spin-1/2 Quantum Mechanics in Biquaternionic Form__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ is isomorphic, as an algebra, to the algebra $M_2(\mathbb{C})$ of $2 \times 2$ complex matrices (article 5). This is a structural fact: two algebras that are isomorphic have the same abstract structure, and any statement about one translates into a statement about the other.

$M_2(\mathbb{C})$ is also, mathematically, the algebra of **observables of a two-state quantum system**. Its Hermitian elements are the observables of a **spin-1/2** particle, and the state space on which it acts is the two-dimensional complex vector space $\mathbb{C}^2$.

The consequence is a **structural identification**:

> The biquaternion algebra $\mathbb{B}$ contains the complete algebraic structure of a spin-1/2 quantum-mechanical system.

This is not an analogy. It is an identity of algebras. Every idempotent of $\mathbb{M}_+$ is a spin-1/2 pure-state projector. Every Hermitian element of $\mathbb{M}_+$ is a spin observable. The trace formula $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ is the Born rule for spin-1/2. The unitary biquaternions of $SU(2)$ are the spin rotation operators.

This article develops the identification in detail. It is not an article about new physics: the physics it describes (spin-1/2 quantum mechanics) is standard and well established. The article is about **where** this standard physics lives within the biquaternion algebra, and what structural features of the biquaternion framework it reveals.

The article is organized as follows. First the two-state system of quantum mechanics is recalled. Then the isomorphism $\mathbb{B} \cong M_2(\mathbb{C})$ is stated explicitly. Then the identification of $\mathbb{M}_+$ with the observables is given, and the idempotents with the states. Then the trace formula is stated as the Born rule. Then the relation to the four-vector space $\mathbb{M}_-$ is discussed. The article closes with a summary of what the biquaternion framework does and does not contain.

The conventions are those of the companion articles: the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$, the scalar imaginary is $i$, and the four fixed-point subspaces are $\mathbb{C}_\mathbb{B}, \mathbb{H}_\mathbb{B}, \mathbb{M}_+, \mathbb{M}_-$.

## The Two-State System in Quantum Mechanics

A **two-state quantum system** is a quantum system whose state space is a two-dimensional complex Hilbert space $\mathcal{H} \cong \mathbb{C}^2$. Equivalently, the pure states are rays in $\mathbb{C}^2$, and the observables are Hermitian operators on $\mathbb{C}^2$.

### States

A **pure state** is a unit vector $\psi \in \mathbb{C}^2$, up to a global phase. In the density matrix formalism, the pure state is represented by the rank-1 projector

$$
\rho_\psi = |\psi\rangle\langle\psi|,
$$

which satisfies $\rho_\psi^2 = \rho_\psi$ (idempotent), $\rho_\psi^\dagger = \rho_\psi$ (Hermitian), and $\mathrm{Tr}(\rho_\psi) = 1$.

A general (mixed) state is a positive semidefinite Hermitian operator with trace 1. The pure states are the extreme points of the convex set of states.

### Observables

An **observable** is a Hermitian operator $A$ on $\mathbb{C}^2$. In the Pauli basis, every Hermitian operator has the form

$$
A = a_0 I_2 + a_1 \sigma_1 + a_2 \sigma_2 + a_3 \sigma_3,
$$

with $a_0, a_1, a_2, a_3 \in \mathbb{R}$, where $\sigma_1, \sigma_2, \sigma_3$ are the Pauli matrices:

$$
\sigma_1 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad \sigma_2 = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \qquad \sigma_3 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}.
$$

The observables form a real 4-dimensional vector space, closed under addition and multiplication by real scalars, but not under complex multiplication.

### The Born Rule

For a state $\rho$ and an observable $A$, the **expectation value** is

$$
\langle A \rangle_\rho = \mathrm{Tr}(\rho A).
$$

For a pure state $\rho_\psi = |\psi\rangle\langle\psi|$ and an observable $A$, this reduces to $\langle \psi | A | \psi \rangle$.

### Spin-1/2

The **spin-1/2 system** is the specific physical realization of a two-state system in which the observables are the spin components

$$
\hat{S}_k = \frac{\hbar}{2}\sigma_k, \qquad k = 1, 2, 3.
$$

The state space is the spinor space $\mathbb{C}^2$, and the spin states are the eigenstates of $\mathbf{S}\cdot\hat{\mathbf{n}}$ for a unit vector $\hat{\mathbf{n}}$. The spin-up and spin-down projectors along the direction $\hat{\mathbf{n}}$ are

$$
P_\pm^{\hat{\mathbf{n}}} = \frac{1}{2}\left(I_2 \pm \hat{\mathbf{n}}\cdot\boldsymbol{\sigma}\right).
$$

These are Hermitian, idempotent, and of trace 1. They are the **pure-state projectors** of the spin system.

The group of spin rotations is $SU(2)$, which acts on the spinor space $\mathbb{C}^2$ and is the double cover of the rotation group $SO(3)$.

## The Biquaternion Algebra as $M_2(\mathbb{C})$

### The Isomorphism

The biquaternion algebra is isomorphic to $M_2(\mathbb{C})$ (article 5):

$$
\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H} \cong M_2(\mathbb{C}).
$$

An explicit isomorphism, consistent with the quaternion multiplication rules of the algebra, is given by

$$
e_0 \mapsto I_2, \qquad e_1 \mapsto -i\sigma_1, \qquad e_2 \mapsto -i\sigma_2, \qquad e_3 \mapsto -i\sigma_3, \qquad i \mapsto iI_2,
$$

where $i$ on the left is the scalar imaginary of $\mathbb{B}$ and $i$ on the right is the complex unit in $M_2(\mathbb{C})$.

It is useful to verify that this is indeed an isomorphism of algebras. The quaternion units satisfy $e_k^2 = -e_0$ and $e_j e_k = \epsilon_{jkl} e_l$ for $j \neq k$. Under the map:

$$
e_k^2 \mapsto (-i\sigma_k)^2 = -\sigma_k^2 = -I_2 = -e_0,
$$

$$
e_1 e_2 \mapsto (-i\sigma_1)(-i\sigma_2) = (-i)^2 \sigma_1 \sigma_2 = -\sigma_1 \sigma_2 = -i\sigma_3 = e_3.
$$

So the map preserves the multiplication rules. The scalar imaginary $i$ maps to $iI_2$, which satisfies $(iI_2)^2 = -I_2$ and commutes with all $(-i\sigma_k)$. Both properties are required.

### The Two Subspaces Under the Isomorphism

Under this isomorphism, the fixed-point subspaces of the algebra acquire concrete matrix forms.

**Hermitian subspace $\mathbb{M}_+$.** A general element is $\tilde{H} = h_0 e_0 + i h_1 e_1 + i h_2 e_2 + i h_3 e_3$ with $h_k \in \mathbb{R}$. Under the isomorphism:

$$
\tilde{H} \mapsto h_0 I_2 + h_1 \sigma_1 + h_2 \sigma_2 + h_3 \sigma_3.
$$

This is a **Hermitian $2 \times 2$ matrix**. So $\mathbb{M}_+$ is isomorphic to the space of Hermitian operators on $\mathbb{C}^2$.

**Anti-Hermitian subspace $\mathbb{M}_-$.** A general element is $\tilde{X} = i x_0 e_0 + x_1 e_1 + x_2 e_2 + x_3 e_3$ with $x_k \in \mathbb{R}$. Under the isomorphism:

$$
\tilde{X} \mapsto i x_0 I_2 - i x_1 \sigma_1 - i x_2 \sigma_2 - i x_3 \sigma_3 = i\left(x_0 I_2 - x_1\sigma_1 - x_2\sigma_2 - x_3\sigma_3\right).
$$

This is $i$ times a Hermitian matrix, i.e., an **anti-Hermitian** matrix. So $\mathbb{M}_-$ is isomorphic to the space of anti-Hermitian operators on $\mathbb{C}^2$.

**Real quaternion subspace $\mathbb{H}_\mathbb{B}$.** A general element is $\tilde{Q} = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ with $q_k \in \mathbb{R}$. Under the isomorphism:

$$
\tilde{Q} \mapsto q_0 I_2 - i q_1\sigma_1 - i q_2\sigma_2 - i q_3\sigma_3 = \begin{pmatrix} q_0 - i q_3 & -i(q_1 - i q_2) \\ -i(q_1 + i q_2) & q_0 + i q_3 \end{pmatrix}.
$$

This is a general element of the complexified form $q_0 I - i \mathbf{q}\cdot\boldsymbol{\sigma}$, i.e., an **arbitrary complex $2 \times 2$ matrix** with a specific structure. This is the full algebra $M_2(\mathbb{C})$.

## The Observables

The identification of $\mathbb{M}_+$ with the observables is direct.

**Statement.** The Hermitian subspace $\mathbb{M}_+$ is isomorphic, as a real vector space, to the space of observables of a spin-1/2 quantum system.

**Proof.** Under the isomorphism of the previous section, an element $\tilde{H} \in \mathbb{M}_+$ with components $(h_0, h_1, h_2, h_3)$ maps to the Hermitian matrix $h_0 I_2 + h_1\sigma_1 + h_2\sigma_2 + h_3\sigma_3$. This is exactly the general Hermitian operator on $\mathbb{C}^2$, which is the general observable of a two-state quantum system.

### Corollaries

**Real dimension.** $\mathbb{M}_+$ has real dimension 4, matching the dimension of the space of Hermitian $2\times 2$ matrices. This is the same as the dimension of the space of observables of a two-state system.

**Basis.** The four elements $e_0, ie_1, ie_2, ie_3$ of $\mathbb{M}_+$ map to $I_2, \sigma_1, \sigma_2, \sigma_3$ respectively. These are the standard generators of the observable algebra.

**The identity and the traceless part.** The scalar part $h_0 e_0$ maps to the identity component $h_0 I_2$, which is the "trivial" observable. The vector part $i(h_1 e_1 + h_2 e_2 + h_3 e_3)$ maps to the traceless part $h_1\sigma_1 + h_2\sigma_2 + h_3\sigma_3$. The trace of an element of $\mathbb{M}_+$ is $2h_0$ (twice the scalar part), which corresponds to the trace of the matrix.

## The Idempotents as Pure States

The idempotents of $\mathbb{M}_+$ are the pure-state projectors of the spin-1/2 system.

**Statement.** The idempotents of $\mathbb{M}_+$ are exactly the elements

$$
P_\pm = \tfrac{1}{2}\left(e_0 \pm \mu i\right),
$$

where $\mu = \mu_1 e_1 + \mu_2 e_2 + \mu_3 e_3$ is a unit pure real quaternion, $\mu_1^2 + \mu_2^2 + \mu_3^2 = 1$.

**Properties.** Each such $P_\pm$ satisfies:

1. **Hermitian:** $P_\pm^\dagger = P_\pm$, since $P_\pm \in \mathbb{M}_+$.
2. **Idempotent:** $P_\pm^2 = P_\pm$.
3. **Trace one:** $\mathrm{Tr}(P_\pm) = 2\,\mathrm{Sc}(P_\pm) = 1$.
4. **Rank one:** in the matrix representation, $P_\pm$ maps to a rank-1 projection matrix.

**Proof.** The idempotent form follows from the classification in article 4: every idempotent of $\mathbb{B}$ is $\tfrac{1}{2}(e_0 \pm \xi i)$ with $\xi$ a root of $-1$. The idempotents in $\mathbb{M}_+$ correspond to the "real roots" $\xi = \pm \mu$ with $\mu$ a unit pure real quaternion. The Hermitian, idempotent, trace-1 properties are direct computations (article 3).

**Identification with spin projectors.** Under the isomorphism, $P_\pm$ maps to

$$
P_\pm \mapsto \frac{1}{2}\left(I_2 \pm \mu_1\sigma_1 \pm \mu_2\sigma_2 \pm \mu_3\sigma_3\right) = \frac{1}{2}\left(I_2 \pm \boldsymbol{\mu}\cdot\boldsymbol{\sigma}\right).
$$

This is exactly the spin projector $|\pm\hat{\boldsymbol{\mu}}\rangle\langle\pm\hat{\boldsymbol{\mu}}|$ onto the spin-up or spin-down state along the direction $\hat{\boldsymbol{\mu}}$.

So **every spin-1/2 pure state corresponds to exactly one idempotent of $\mathbb{M}_+$**, and vice versa.

## The Trace Formula as the Born Rule

The expectation value of an observable in a state is given by the trace formula.

**Statement.** For an idempotent $P \in \mathbb{M}_+$ (a pure state) and a Hermitian element $\tilde{H} \in \mathbb{M}_+$ (an observable), the quantity

$$
\langle \tilde{H} \rangle_P = \mathrm{Tr}(P\tilde{H}) = 2\,\mathrm{Sc}(P\tilde{H})
$$

is **real** and is the **Born-rule expectation value** of $\tilde{H}$ in the state $P$.

**Proof.** Under the isomorphism, $P$ maps to the projector $|\psi\rangle\langle\psi|$ and $\tilde{H}$ maps to the Hermitian matrix $H$. The trace formula $\mathrm{Tr}(P\tilde{H})$ maps to $\mathrm{Tr}(|\psi\rangle\langle\psi| H) = \langle\psi|H|\psi\rangle$, which is the standard Born-rule expectation. The biquaternion trace formula $2\,\mathrm{Sc}(P\tilde{H})$ is the same quantity, expressed in biquaternion language.

### Example

Take $\mu = e_3$, so that $P_+ = \tfrac{1}{2}(e_0 + e_3 i)$ corresponds to the spin-up state along the $z$ axis, and let $\tilde{H} = i e_1$ (the spin observable along the $x$ axis). Then

$$
P_+ \tilde{H} = \tfrac{1}{2}(e_0 + e_3 i)(ie_1) = \tfrac{1}{2}(ie_1 + e_3 i \cdot i e_1) = \tfrac{1}{2}(ie_1 - e_3 e_1) = \tfrac{1}{2}(ie_1 - e_2).
$$

Taking twice the scalar part:

$$
2\,\mathrm{Sc}(P_+ \tilde{H}) = 2 \cdot 0 = 0,
$$

which is the correct expectation $\langle \uparrow_z | S_x | \uparrow_z \rangle = 0$. ✓

Take instead $\tilde{H} = ie_3$ (the spin observable along the $z$ axis):

$$
P_+ \tilde{H} = \tfrac{1}{2}(e_0 + e_3 i)(ie_3) = \tfrac{1}{2}(ie_3 + e_3 i \cdot ie_3) = \tfrac{1}{2}(ie_3 - e_3 e_3) = \tfrac{1}{2}(ie_3 + e_0).
$$

Taking twice the scalar part:

$$
2\,\mathrm{Sc}(P_+ \tilde{H}) = 2 \cdot \tfrac{1}{2} = 1,
$$

which is the correct expectation $\langle \uparrow_z | S_z | \uparrow_z \rangle$ (up to the factor $\hbar/2$, which is absorbed in the normalization). ✓

So the trace formula reproduces the standard spin-1/2 expectation values.

## The State Space and the Spinor

### The Spinor Space

The state space of a spin-1/2 particle is the **spinor space** $\mathbb{C}^2$. It is a complex two-dimensional vector space, i.e., a real four-dimensional vector space.

### The Action of the Algebra

The biquaternion algebra $\mathbb{B} \cong M_2(\mathbb{C})$ acts on the spinor space $\mathbb{C}^2$ by matrix multiplication. The action is complex-linear in the spinor.

The action of $\mathbb{B}$ on $\mathbb{C}^2$ is the **fundamental representation** of $\mathbb{B}$. In the language of modules, $\mathbb{C}^2$ is the unique irreducible module of $\mathbb{B}$, and every finite-dimensional module is a direct sum of copies of it.

### The Relation to $\mathbb{M}_+$ and $\mathbb{M}_-$

The subspaces $\mathbb{M}_+$ and $\mathbb{M}_-$ act on the spinor space in specific ways:

- **Hermitian elements** (in $\mathbb{M}_+$) act as **Hermitian operators** on $\mathbb{C}^2$. These are the observables, whose eigenvalues are real.
- **Anti-Hermitian elements** (in $\mathbb{M}_-$) act as **anti-Hermitian operators** on $\mathbb{C}^2$. These are the generators of unitary transformations, whose exponentials give the unitary group $U(2)$.

The action of the algebra on the spinor space is the fundamental operation of quantum mechanics: the observables act on the states, and the generators act on the states to produce the dynamics.

### The Spinor as an Element of a Biquaternion Module

Strictly speaking, the spinor is **not** an element of $\mathbb{B}$ itself; it is an element of the two-dimensional complex module on which $\mathbb{B}$ acts. This module is the fundamental representation of the algebra, and it is one of the two summands in the decomposition of $\mathbb{B}$ as a left module over itself.

The precise identification is:

- $\mathbb{B}$ as a left module over itself decomposes as $\mathbb{B} \cong \mathbb{C}^2 \oplus \mathbb{C}^2$.
- Each summand is a copy of the spinor space.
- The biquaternion algebra acts on each summand by matrix multiplication.

So the spinor space is a **summand** of the biquaternion algebra viewed as a left module, not a subspace of it in the naive sense. The states of a spin-1/2 system live in this summand, and the algebra acts on them by the module structure.

This is a subtle point, but it is the correct statement. The simpler (and slightly imprecise) formulation is to say that the spinor space is the "fundamental representation" of the algebra, and to identify the states with elements of $\mathbb{C}^2$. The precise statement involves the module decomposition.

## The Rotations and the Boosts

The unitary biquaternions generate the spin rotation group, and the Hermitian biquaternions generate the boost group.

### Unitary Biquaternions

A biquaternion $\tilde{U}$ is **unitary** if $\tilde{U}\tilde{U}^\dagger = e_0$. In the matrix representation, $\tilde{U}$ maps to a unitary matrix. The group of unitary biquaternions is $U(2)$.

The subgroup of $U(2)$ with determinant 1 (in the matrix representation) is $SU(2)$, which is the **spin rotation group**. It acts on the spinor space $\mathbb{C}^2$ by matrix multiplication, and its action on the material space $\mathbb{M}_-$ (by rotor conjugation) is the group of spatial rotations $SO(3)$.

So the **spin rotations of a spin-1/2 particle are realized in the biquaternion framework by the $SU(2)$ subgroup of unit-norm biquaternions**.

### Hermitian Biquaternions

The Hermitian biquaternions in $\mathbb{M}_+$ with unit norm are the **boost biquaternions** $\tilde{\Lambda} = \cosh(\psi/2) + i\sinh(\psi/2)\hat{\mathbf{u}}$. They generate the Lorentz boosts, and their action on $\mathbb{M}_-$ is the rotor conjugation.

In the quantum-mechanical context, the boosts are **not** unitary (they are Hermitian, and their squares are not the identity). They correspond to non-unitary operations, which in the quantum-information language are **non-reversible transformations**.

The full group of unit-norm biquaternions is $SL(2,\mathbb{C})$, which is the double cover of the proper orthochronous Lorentz group $SO^+(1,3)$. It contains $SU(2)$ as the compact subgroup of spatial rotations, and the Hermitian elements as the non-compact set of boosts.

So the biquaternion framework contains:

- **$SU(2)$:** spin rotations of the quantum system.
- **$SL(2,\mathbb{C})$:** the full Lorentz group, containing the spin rotations and the boosts.

The quantum-mechanical sector is $SU(2)$; the relativistic extension is $SL(2,\mathbb{C})$.

## The Dirac Equation and the Spinor Field

The identification extends from a single spin-1/2 particle to a **spin-1/2 field** on spacetime.

### The Biquaternionic Dirac Equation

The biquaternion Dirac equation (companion article) is

$$
\tilde{\nabla}\tilde{\Psi} = m\tilde{\Psi}^\flat,
$$

where $\tilde{\Psi}$ is a biquaternion-valued field, $m$ is the mass, and $\tilde{\Psi}^\flat$ is the anti-Hermitian conjugate. In the massless case ($m = 0$), the equation is

$$
\tilde{\nabla}\tilde{\Psi} = 0,
$$

which is a first-order equation for the field $\tilde{\Psi}$.

### The Interpretation as a Spinor Field

The biquaternion field $\tilde{\Psi}$ is a **spinor field** on the four-dimensional material space $\mathbb{M}_-$. At each point of spacetime, it takes values in the biquaternion algebra. Equivalently, at each point, the field can be viewed as a **pair of Weyl spinors** (one left-handed, one right-handed), following the standard identification of the biquaternion algebra with $M_2(\mathbb{C})$ and its action on $\mathbb{C}^2$.

The Dirac equation is the equation of motion for a single spin-1/2 field. Its solutions describe relativistic spin-1/2 particles: electrons, muons, quarks, and other fermions.

### What the Dirac Equation Contains

The biquaternionic Dirac equation contains:

- The **kinematics** of a relativistic spin-1/2 particle: the mass-shell condition $\tilde{k}\bar{\tilde{k}} = -m^2 c^2/\hbar^2$ for plane-wave solutions.
- The **spin structure**: the polarization biquaternion $\tilde{\Psi}_0$ in the plane-wave solution has two independent components, corresponding to the two spin states.
- The **mass term**: the biquaternion mass term $m\tilde{\Psi}^\flat$, which couples the two chiral components of the spinor.

### What the Dirac Equation Does Not Contain

The biquaternionic Dirac equation, as presented, does not contain:

- **Quantization**: the promotion of the classical field $\tilde{\Psi}$ to an operator-valued field $\hat{\Psi}$ on Fock space.
- **The full four-component Dirac spinor**: the biquaternion formulation describes the field as a pair of Weyl spinors (left-handed and right-handed). The four-component Dirac spinor, including the antiparticle components, is obtained by taking the direct sum of this pair with its complex conjugate.
- **Many-body structure**: a single Dirac field describes a single particle (or a single field mode); many-particle states require tensor products.
- **Interactions beyond electromagnetism**: the weak and strong interactions require additional structure beyond the biquaternion algebra.

## What the Biquaternion Framework Contains

We can now make a precise statement about what the biquaternion framework contains in the spin-1/2 sector.

### Contains

1. **The full algebra of observables of a spin-1/2 system.** The Hermitian subspace $\mathbb{M}_+$ is the space of Hermitian operators on $\mathbb{C}^2$, i.e., the observables.

2. **The pure states.** The idempotents of $\mathbb{M}_+$ are the rank-1 projectors, i.e., the pure states of a spin-1/2 system.

3. **The Born rule.** The trace formula $\mathrm{Tr}(P\tilde{H}) = 2\mathrm{Sc}(P\tilde{H})$ is the Born-rule expectation value.

4. **The spin rotation group.** The $SU(2)$ subgroup of unit-norm biquaternions acts as the spin rotation group.

5. **The relativistic extension.** The full $SL(2,\mathbb{C})$ group of unit-norm biquaternions acts as the Lorentz group, and the Hermitian elements of $\mathbb{M}_+$ generate the boosts.

6. **The Dirac equation.** The biquaternionic Dirac equation is the equation of motion for a relativistic spin-1/2 field, expressed in terms of a pair of Weyl spinors.

7. **Maxwell's equations.** The biquaternion framework contains Maxwell's equations in the form $\tilde{\nabla}\tilde{F} = -\tilde{R}$ (companion article). The coupling of the spinor field to the electromagnetic field — the analogue of the standard minimal coupling $\partial_\mu \to \partial_\mu - iqA_\mu/\hbar$ — has a natural biquaternion form, but the precise expression depends on the representation conventions and is not developed in this article.

### Does Not Contain

1. **Quantization.** The framework is classical. Promoting fields to operators requires additional structure (a Hilbert space, a Fock space, a quantization prescription).

2. **Bosonic fields of higher spin.** The biquaternion algebra contains only the spin-1/2 representation of the Lorentz group. Higher spins require tensor products or larger algebras.

3. **Many-body structure.** A single spin-1/2 particle (or a single spin-1/2 field) is the natural content. Multiparticle states and entangled systems require tensor products of the algebra.

4. **Dynamics beyond the Dirac equation.** The framework contains the free Dirac equation and its coupling to electromagnetism. It does not contain the weak or strong interactions.

5. **The measurement problem.** The framework contains the idempotent projection as a formal operation, but the physical interpretation of measurement is not specified.

So the correct statement is:

> The biquaternion algebra contains the **complete algebraic structure** of a spin-1/2 quantum system, and it contains the **classical field theory** of a spin-1/2 particle coupled to electromagnetism. It does not contain the **quantization** of the spin-1/2 field, the extension to **bosonic fields**, or the structure of **many-body systems**.

This is a strong structural statement. The biquaternion algebra is not a speculative alternative to quantum mechanics; it is a specific algebraic realization of the spin-1/2 sector of quantum mechanics, embedded in a larger structure that also contains the Lorentz group.

## Open Questions

The identification raises several questions.

1. **Quantization.** The biquaternionic Dirac equation is classical. Can it be quantized? What is the natural Hilbert space, and how does the biquaternion algebra extend to the quantized theory?

2. **Many-body extension.** The biquaternion algebra contains one spin-1/2 degree of freedom. How does it extend to multiple spin-1/2 particles, and how does the tensor product structure emerge?

3. **The state space.** The spinor space $\mathbb{C}^2$ is the fundamental representation of the biquaternion algebra. Is there a natural interpretation of the spinor space in the material/informational dichotomy? Does the spinor space belong to $\mathbb{M}_-$, or is it a separate structure?

4. **The role of $\mathbb{M}_-$.** In the identification, $\mathbb{M}_+$ is the space of observables and $\mathbb{M}_-$ is the space of generators. The state space is the fundamental module, which is not directly $\mathbb{M}_-$ or $\mathbb{M}_+$. Is there a natural interpretation of $\mathbb{M}_-$ in the spin-1/2 framework (beyond being the generators of unitary evolution)?

5. **The extension to higher spins.** The biquaternion algebra contains only spin-1/2. How does it extend to spin-1 (the photon), spin-3/2, or spin-2 (the graviton)? These would require tensor products or larger algebras.

6. **The role of the Weyl spinors.** The biquaternion Dirac equation is expressed in terms of a pair of Weyl spinors. The full Dirac spinor is four-component. What is the precise relation between the two, and how does the chirality structure of the Standard Model fit into the biquaternion framework?

7. **The minimal coupling to electromagnetism.** The precise form of the coupling of the biquaternionic Dirac field to the electromagnetic field, in the biquaternion framework, deserves a dedicated treatment.

These questions are open.

## Summary

The biquaternion algebra $\mathbb{B} \cong M_2(\mathbb{C})$ contains the complete algebraic structure of a two-state quantum system, which is the spin-1/2 system. Under the isomorphism, the Hermitian subspace $\mathbb{M}_+$ corresponds to the space of Hermitian operators on $\mathbb{C}^2$, which are the observables of a spin-1/2 particle. The idempotents of $\mathbb{M}_+$, of the form $P_\pm = \tfrac{1}{2}(e_0 \pm \mu i)$ for a unit pure quaternion $\mu$, correspond to the rank-1 projectors, i.e., the pure spin states. The trace formula $\mathrm{Tr}(P\tilde{H}) = 2\mathrm{Sc}(P\tilde{H})$ is the Born rule.

The spin rotation group $SU(2)$ is realized in the biquaternion framework as the group of unit-norm biquaternions with real vector part. The full Lorentz group $SL(2,\mathbb{C})$ is realized as the group of unit-norm biquaternions in general, and the Hermitian elements of $\mathbb{M}_+$ generate the boosts.

The biquaternionic Dirac equation is the equation of motion for a relativistic spin-1/2 field. The biquaternion formulation describes this field as a pair of Weyl spinors (left-handed and right-handed); the full four-component Dirac spinor is recovered by taking the direct sum of this pair with its complex conjugate. The framework contains the classical Dirac field coupled to electromagnetism, but it does not contain the quantization of the field, the extension to bosonic or higher-spin fields, or the structure of many-body systems.

The identification is not an analogy. It is the same mathematics, expressed in the biquaternion algebra, and it is the deepest structural connection between the biquaternion framework and established quantum physics.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} \cong M_2(\mathbb{C})$ | Biquaternion algebra |
| $\mathbb{M}_+$ | Hermitian subspace = observables |
| $\mathbb{M}_-$ | Anti-Hermitian subspace = generators |
| $e_0, e_1, e_2, e_3$ | Quaternion units, $e_k^2 = -e_0$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\sigma_1, \sigma_2, \sigma_3$ | Pauli matrices |
| $P_\pm = \tfrac{1}{2}(e_0 \pm \mu i)$ | Idempotent (pure spin state) |
| $\tilde{H} = h_0 e_0 + ih_k e_k$ | Hermitian element (observable) |
| $\mathrm{Tr}(P\tilde{H}) = 2\mathrm{Sc}(P\tilde{H})$ | Born-rule expectation value |
| $SU(2)$ | Spin rotation group |
| $SL(2,\mathbb{C})$ | Lorentz group (double cover) |
| $\tilde{\nabla}\tilde{\Psi} = m\tilde{\Psi}^\flat$ | Biquaternionic Dirac equation |

## Further Reading

- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford, 1930), for the spin-1/2 formalism and the Dirac equation.
- John von Neumann, *Mathematical Foundations of Quantum Mechanics* (Princeton, 1932), for the density matrix formalism.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the standard treatment of two-state systems and qubits.
- J. J. Sakurai and Jim Napolitano, *Modern Quantum Mechanics* (Pearson, 2017), for the spin-1/2 algebra and the Born rule.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection between Clifford algebras and spinors.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric algebra formulation of spin-1/2.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the original formulation of the Dirac equation in geometric algebra.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the spinor formulation of the Lorentz group.

