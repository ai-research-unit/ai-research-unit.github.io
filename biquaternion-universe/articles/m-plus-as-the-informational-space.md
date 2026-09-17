
# __$\mathbb{M}_+$ as the Informational Space__

## Introduction

The companion article identified the anti-Hermitian subspace $\mathbb{M}_-$ as the material space: the four-dimensional real subspace of $\mathbb{B}$ whose elements are the four-vectors of relativistic physics. This article is about the **complementary subspace** $\mathbb{M}_+$, the Hermitian subspace.

The mathematics of $\mathbb{M}_+$ is standard: it is a four-dimensional real subspace consisting of elements with real scalar part and imaginary vector part. It contains the boost biquaternions, the Hermitian forms, the idempotents, and the identity. It acts on $\mathbb{M}_-$ by rotor conjugation, and its elements satisfy a natural trace formula. All of this is established mathematics.

The **interpretation** of $\mathbb{M}_+$ as the "informational space" is a hypothesis, and it should be read as such. The structural facts about $\mathbb{M}_+$ — that its elements are Hermitian operators on $\mathbb{M}_-$ — are the same structural facts that underlie quantum information theory. Whether this mathematical coincidence reflects a physical fact about the world — whether the biquaternion algebra has an informational sector that is as real as its material sector — is the central question of this article, and the article's answer is: **we do not yet know, but the structure is compelling enough to be worth writing down.**

The article is organized as follows. First the mathematical structure of $\mathbb{M}_+$ is recalled. Then the natural action of $\mathbb{M}_+$ on $\mathbb{M}_-$ is developed. Then the structural analogy with quantum information theory is presented in detail. Then the informational hypothesis is stated clearly, with the honest position on what it does and does not claim. The article closes with open questions.

The conventions are those of the companion articles. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$, the scalar imaginary is $i$, and the biquaternionic gradient is $\tilde{\nabla} = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z$. Throughout, the symbol $c$ denotes the **speed of light in the medium**, $c = 1/\sqrt{\epsilon\mu}$, and $c_0$ denotes the **vacuum speed of light**. In vacuum, $c = c_0$.

## The Hermitian Subspace

### Definition and Basis

The **Hermitian subspace** $\mathbb{M}_+$ is the fixed-point set of the Hermitian conjugation:

$$
\mathbb{M}_+ = \{\tilde{Q} \in \mathbb{B} : \tilde{Q}^\dagger = \tilde{Q}\},
$$

where $\tilde{Q}^\dagger = \bar{\tilde{Q}}^*$. Explicitly, a biquaternion is in $\mathbb{M}_+$ if and only if it has the form

$$
\tilde{Q} = q_0\,e_0 + i q_1\,e_1 + i q_2\,e_2 + i q_3\,e_3, \qquad q_0, q_1, q_2, q_3 \in \mathbb{R}.
$$

The scalar part is **real** and the vector part is **purely imaginary**. Equivalently, if we write $\tilde{Q} = Q_0 e_0 + \mathbf{Q}$, then $\tilde{Q} \in \mathbb{M}_+$ iff $Q_0$ is real and $Q_1, Q_2, Q_3$ are purely imaginary.

A natural basis of $\mathbb{M}_+$ is

$$
\{e_0,\; i\,e_1,\; i\,e_2,\; i\,e_3\}.
$$

As a real vector space, $\mathbb{M}_+$ has dimension $4$. It is **not** a subalgebra of $\mathbb{B}$: for example, $(ie_1)(ie_1) = -e_0 \in \mathbb{M}_-$.

### Properties

**Quadratic form.** The biquaternion **norm form** restricts to a real quadratic form on $\mathbb{M}_+$:

$$
N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = q_0^2 + (iq_1)^2 + (iq_2)^2 + (iq_3)^2 = q_0^2 - q_1^2 - q_2^2 - q_3^2.
$$

This is a real quadratic form of **signature** $(1,3)$: one positive direction (the scalar component $q_0$) and three negative directions (the vector components $q_1, q_2, q_3$). This is the **mirror image** of the signature on $\mathbb{M}_-$.

**Zero divisors.** The norm form vanishes on the cone

$$
q_0^2 = q_1^2 + q_2^2 + q_3^2,
$$

which is the mirror image of the light cone of $\mathbb{M}_-$. The complement of the cone has two connected components, corresponding to the regions $N > 0$ and $N < 0$.

**Not a division algebra.** As for $\mathbb{M}_-$, the presence of the zero divisor cone means that $\mathbb{M}_+$ is not a division algebra.

**Relation to $\mathbb{M}_-$.** The two subspaces are complementary:

$$
\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-,
$$

and they are exchanged by multiplication by $i$: $i\mathbb{M}_+ = \mathbb{M}_-$ and $i\mathbb{M}_- = \mathbb{M}_+$. Under quaternion conjugation, $\overline{\mathbb{M}_+} = \mathbb{M}_-$.

### The Interpretation of the Two Parts of $\mathbb{M}_+$

A general element of $\mathbb{M}_+$ has a real scalar part and an imaginary vector part. The **interpretation** that motivates this article is:

- The **imaginary vector part** $i(q_1 e_1 + q_2 e_2 + q_3 e_3)$ corresponds to three **imaginary spatial directions** — the directions of an "imagined" or "informational" space, which, like the time direction of $\mathbb{M}_-$, cannot be touched or moved through in the ordinary sense.
- The **real scalar part** $q_0 e_0$ corresponds to a **material temporal direction** — a direction that is real (in the sense of being "accessible") and that carries the storage or ordering of information.

This is not a derivation; it is a proposed reading of the structure. We flag it here as the interpretive content of the article and return to it in the section on the informational hypothesis.

## Elements of $\mathbb{M}_+$ in the Series

The companion articles already contain several distinguished elements of $\mathbb{M}_+$. It is worth collecting them, because they are the natural candidates for the "informational objects" of the hypothesis.

### The Boost Biquaternion

The **boost biquaternion**

$$
\tilde{\Lambda} = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\,\hat{\mathbf{u}}, \qquad \hat{\mathbf{u}}^2 = -e_0,
$$

lies in $\mathbb{M}_+$: its scalar part $\cosh(\psi/2)$ is real, and its vector part $i\sinh(\psi/2)\hat{\mathbf{u}}$ is purely imaginary. It is Hermitian ($\tilde{\Lambda}^\dagger = \tilde{\Lambda}$) and has unit norm ($\tilde{\Lambda}\bar{\tilde{\Lambda}} = e_0$). It acts on $\mathbb{M}_-$ by rotor conjugation, implementing the Lorentz boost.

The boost biquaternion is the **prototype** of an operator in $\mathbb{M}_+$ acting on the material space $\mathbb{M}_-$. The other elements of $\mathbb{M}_+$ discussed below are also operators on $\mathbb{M}_-$, in the same sense.

### The Idempotents

The **idempotents** of $\mathbb{B}$ of the form

$$
P_\pm = \tfrac{1}{2}\left(e_0 \pm \mu i\right), \qquad \mu^2 = -e_0, \; \mu \text{ real unit pure quaternion},
$$

lie in $\mathbb{M}_+$: their scalar part $\tfrac{1}{2}$ is real, and their vector part $\pm \tfrac{1}{2} i \mu$ is purely imaginary. They satisfy:

- **Hermitian:** $P_\pm^\dagger = P_\pm$, since $P_\pm \in \mathbb{M}_+$.
- **Idempotent:** $P_\pm^2 = P_\pm$.
- **Trace one:** $\mathrm{Tr}(P_\pm) = 2\,\mathrm{Sc}(P_\pm) = 1$ (using the trace from the matrix representation).
- **Rank one:** in the matrix representation $\mathbb{B} \cong M_2(\mathbb{C})$, $P_\pm$ is a rank-one projection matrix.

These are the biquaternion analogues of **pure-state density matrices** of quantum mechanics. They are the natural "states" of the informational sector.

By contrast, the idempotents from the **non-trivial** roots of $-1$ (of the form $\xi = b\mu + d\nu i$ with $b^2 - d^2 = 1$, $\mu \perp \nu$) are **not** Hermitian and do not lie in $\mathbb{M}_+$. So $\mathbb{M}_+$ contains only the "physically meaningful" (Hermitian) idempotents.

### The Hermitian Forms

For any biquaternion $\tilde{Q} \in \mathbb{B}$, the **Hermitian form**

$$
\tilde{Q}\tilde{Q}^\dagger
$$

is an element of $\mathbb{M}_+$: it is Hermitian by construction. Its scalar part is $\|\tilde{Q}\|_E^2 = \sum_\mu |Q_\mu|^2$, the Euclidean norm squared, which is non-negative. In the matrix representation, the Hermitian form corresponds to $M M^\dagger$, whose trace is the Frobenius norm squared.

The Hermitian form is the natural "weight" or "energy" of the state $\tilde{Q}$, and it is the closest biquaternion analogue of the trace of a density matrix.

### The Identity

The identity $e_0$ is trivially in $\mathbb{M}_+$. It corresponds to the "trivial" state or the identity operator.

### Summary of the Elements of $\mathbb{M}_+$

| Object | Structure | Role |
|---|---|---|
| Identity $e_0$ | Real scalar | Identity operator |
| Boost biquaternion $\tilde{\Lambda}$ | Hermitian, unit norm | Lorentz operator (reversible) |
| Idempotent $P_\pm$ | Hermitian, idempotent, trace 1 | Pure state / projector (irreversible) |
| Hermitian form $\tilde{Q}\tilde{Q}^\dagger$ | Hermitian, positive scalar part | Energy / weight of a state |

The common feature of these objects is that they are **Hermitian** (fixed under $\dagger$). This is what defines membership in $\mathbb{M}_+$.

## The Action of $\mathbb{M}_+$ on $\mathbb{M}_-$

The most important structural fact about $\mathbb{M}_+$ is that its elements **act** on the elements of $\mathbb{M}_-$ by **conjugation**:

$$
\tilde{X} \;\longmapsto\; \tilde{H}\,\tilde{X}\,\tilde{H}^\dagger, \qquad \tilde{H} \in \mathbb{M}_+, \; \tilde{X} \in \mathbb{M}_-.
$$

### Basic Properties of the Action

**1. The image is in $\mathbb{M}_-$.** If $\tilde{X}^\dagger = -\tilde{X}$ (anti-Hermitian) and $\tilde{H}^\dagger = \tilde{H}$ (Hermitian), then

$$
(\tilde{H}\tilde{X}\tilde{H}^\dagger)^\dagger = \tilde{H}^{\dagger\dagger}\tilde{X}^\dagger\tilde{H}^\dagger = \tilde{H}(-\tilde{X})\tilde{H}^\dagger = -\tilde{H}\tilde{X}\tilde{H}^\dagger,
$$

so the image is anti-Hermitian, i.e., in $\mathbb{M}_-$. The action maps the material space to itself.

**2. The action is linear in $\tilde{X}$.** This follows from the bilinearity of the biquaternion product.

**3. The action preserves the norm form when $\tilde{H}$ is unitary.** If $\tilde{H}\tilde{H}^\dagger = e_0$ (unit-norm, e.g., a boost biquaternion), then the action preserves $N(\tilde{X}) = \tilde{X}\bar{\tilde{X}}$. This is the biquaternion expression of the Lorentz invariance of the Minkowski interval.

**4. The action is a group action.** Compositions of actions compose:

$$
\tilde{H}_2(\tilde{H}_1\tilde{X}\tilde{H}_1^\dagger)\tilde{H}_2^\dagger = (\tilde{H}_2\tilde{H}_1)\tilde{X}(\tilde{H}_2\tilde{H}_1)^\dagger.
$$

### The Structural Relation: Operators and States

The action of $\mathbb{M}_+$ on $\mathbb{M}_-$ has the structure of **operators acting on states**:

- $\mathbb{M}_-$ is the space of **states** (the material configurations: position, velocity, momentum, potential, current).
- $\mathbb{M}_+$ is the space of **operators** (the Hermitian biquaternions that act on the states).

This is the algebraic content of the interpretation of $\mathbb{M}_-$ as "material" and $\mathbb{M}_+$ as "informational" (or "operational"). The two subspaces are not symmetric: one acts, the other is acted upon.

### Reversible Versus Irreversible Actions

The elements of $\mathbb{M}_+$ fall into two important classes.

**Unitary elements** ($\tilde{H}\tilde{H}^\dagger = e_0$). These preserve the norm form and act by **reversible** transformations. Examples: the boost biquaternions $\tilde{\Lambda}$, the spatial rotation rotors, the unit-norm elements of the group $SL(2,\mathbb{C})$. These correspond to Lorentz transformations.

**Idempotent elements** ($\tilde{H}^2 = \tilde{H}$). These do not preserve the norm form (unless $\tilde{H} = e_0$). They act by **irreversible** projections: $\tilde{X} \mapsto \tilde{P}\tilde{X}\tilde{P}$. Examples: the pure-state projectors $P_\pm = \tfrac{1}{2}(e_0 \pm \mu i)$. These correspond to quantum-mechanical measurements.

The **dichotomy between reversible and irreversible actions** is intrinsic to the structure of $\mathbb{M}_+$: it is the biquaternion version of the fundamental dichotomy of quantum information theory between unitary evolution and measurement.

### The Trace Formula

For $\tilde{P} \in \mathbb{M}_+$ idempotent (a state) and $\tilde{H} \in \mathbb{M}_+$ Hermitian (an observable), the quantity

$$
\langle \tilde{H} \rangle_{\tilde{P}} = \mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})
$$

is **real**. It has the form of a **quantum-mechanical expectation value**: the trace of the product of a state and an observable. For example, if $\tilde{P} = \tfrac{1}{2}(e_0 + \mu i)$ and $\tilde{H} = h_0 e_0 + i\mathbf{h}\cdot\mathbf{e}$, then

$$
\langle \tilde{H} \rangle_{\tilde{P}} = h_0 + \boldsymbol{\mu}\cdot\mathbf{h},
$$

which is the standard spin-1/2 expectation value $\langle \mu | \hat{H} | \mu \rangle$. The trace formula is the biquaternion expression of the Born rule.

## The Structural Analogy with Quantum Information

The mathematics of $\mathbb{M}_+$ and its action on $\mathbb{M}_-$ is **structurally identical** to the mathematics of quantum information theory for a single qubit. This is the central observation of this article.

### The Correspondence

| Quantum information | Biquaternion framework |
|---|---|
| State space $\mathbb{C}^2$ | Material space $\mathbb{M}_-$ |
| Density matrix $\rho$ (Hermitian, positive, trace 1) | Idempotent $\tilde{P} \in \mathbb{M}_+$ (Hermitian, idempotent, trace 1) |
| Pure state $\|\psi\rangle\langle\psi\|$ | Idempotent $\tfrac{1}{2}(e_0 + \mu i)$ |
| Observable (Hermitian operator) | Hermitian element $\tilde{H} \in \mathbb{M}_+$ |
| Unitary gate $U$ | Unit-norm element $\tilde{\Lambda}$ of $SL(2,\mathbb{C})$ |
| Expectation value $\mathrm{Tr}(\rho H)$ | Trace formula $2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ |
| Reversible evolution $U\rho U^\dagger$ | Rotor conjugation $\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$ |
| Projective measurement $\rho \mapsto P\rho P$ | Idempotent projection $\tilde{X} \mapsto \tilde{P}\tilde{X}\tilde{P}$ |

The correspondence is not an analogy. **It is the same mathematics**, expressed in two different notations. The biquaternion algebra $\mathbb{B} \cong M_2(\mathbb{C})$ contains the algebra of $2 \times 2$ complex matrices, which is the algebra of observables of a two-state system.

### What the Correspondence Is and Is Not

**What it is:** A structural fact about the algebra. The elements of $\mathbb{M}_+$ are Hermitian operators on $\mathbb{M}_-$, and the algebra they generate is the algebra of observables of a two-state system. The mathematics of quantum information applies to $\mathbb{M}_+$ as it applies to any such algebra.

**What it is not (yet):** A physical theory. The structural correspondence does not by itself establish that $\mathbb{M}_+$ **is** an informational sector of physics. It establishes that if $\mathbb{M}_+$ were given an informational interpretation, the mathematics would be available. Whether the interpretation is realized in nature is a separate question.

### The Spin Analogy

The correspondence with quantum information is closely related to the **spin-1/2 formalism** of non-relativistic quantum mechanics.

- In spin-1/2 quantum mechanics, the state space is $\mathbb{C}^2$, and the observables are the Pauli matrices $\sigma_k$ generating $\mathfrak{su}(2)$. The rotation group $SU(2)$ acts on the states.
- In the biquaternion framework, the material space $\mathbb{M}_-$ is analogous to the state space, and the Hermitian biquaternions in $\mathbb{M}_+$ are analogous to the observables. The action is by rotor conjugation.

The difference is:

- In spin-1/2, the operators generate the **compact** group $SU(2)$ (rotations).
- In $\mathbb{M}_+$, the Hermitian elements generate the **non-compact** group $SL(2,\mathbb{C})$ (Lorentz transformations).

The compact/non-compact distinction reflects the difference between rotations in a spacelike plane (compact) and boosts in a timelike plane (non-compact). The biquaternion framework extends the spin-1/2 structure to the relativistic setting: the operators generate the Lorentz group rather than the rotation group, and the corresponding observables include boosts (Hermitian biquaternions with imaginary vector part) alongside rotations.

The biquaternion framework can therefore be read as a **relativistic generalisation of the spin-1/2 formalism**, in which the state space $\mathbb{M}_-$ is four-dimensional and the symmetry group is the Lorentz group.

## The Informational Hypothesis

We now state the hypothesis that motivates this article, in the clearest terms possible.

### Statement of the Hypothesis

**Hypothesis (informational sector).** The Hermitian subspace $\mathbb{M}_+$ is not only a mathematical structure but the arena of an **informational sector** of physics. Its elements are Hermitian operators on the material space $\mathbb{M}_-$, and the two sectors together constitute the full physical world. The **material sector** $\mathbb{M}_-$ describes the observable, causal structure of spacetime. The **informational sector** $\mathbb{M}_+$ describes the operations, measurements, and information-theoretic content associated with the material sector.

In this reading:

- A **state** of the informational sector is an idempotent $P_\pm \in \mathbb{M}_+$, a pure-state projector.
- An **observable** of the informational sector is a general Hermitian element $\tilde{H} \in \mathbb{M}_+$.
- **Evolution** is generated by rotor conjugation $\tilde{X} \mapsto \tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$, with $\tilde{\Lambda}$ a unit-norm biquaternion.
- **Measurement** is the idempotent projection $\tilde{X} \mapsto \tilde{P}\tilde{X}\tilde{P}$.
- **Expectation values** are given by the trace formula $2\,\mathrm{Sc}(\tilde{P}\tilde{H})$.

### Interpretation of the Two Parts of $\mathbb{M}_+$

The real scalar part and the imaginary vector part of an element of $\mathbb{M}_+$ have natural readings under the hypothesis.

- The **real scalar part** $q_0 e_0$ corresponds to a **temporal material direction**: a direction in which information can be stored and ordered. It is the "memory" direction of the informational sector.
- The **imaginary vector part** $i(q_1 e_1 + q_2 e_2 + q_3 e_3)$ corresponds to three **imaginary spatial directions**: the directions of an "imagined" or "informational" space. These are the directions in which information is organised, in contrast to the ordinary material space $\mathbb{M}_-$ in which matter is extended.

The interpretation is the mirror of the interpretation of $\mathbb{M}_-$ as the material sector (three real spatial directions and one imaginary temporal direction). Where $\mathbb{M}_-$ has three touchable spatial directions and one untouchable temporal direction, $\mathbb{M}_+$ has three untouchable spatial directions and one touchable temporal direction.

### What the Hypothesis Does and Does Not Claim

**It does claim:**

- The mathematics of $\mathbb{M}_+$ is structurally identical to the mathematics of a quantum-informational system.
- The elements of $\mathbb{M}_+$ act as operators on the material space $\mathbb{M}_-$.
- The reversible/irreversible dichotomy of $\mathbb{M}_+$ (unitary vs. idempotent) mirrors the evolution/measurement dichotomy of quantum information.

**It does not claim:**

- That the informational sector has been observed.
- That the informational sector has a specified dynamics (a wave equation, a field equation, a conservation law).
- That there is a specified coupling between the informational and material sectors (beyond the standard Lorentz coupling via the boost biquaternion).
- That the informational sector provides any empirical predictions that distinguish it from standard physics.
- That the imaginary directions of $\mathbb{M}_+$ are "extra space" in the ordinary sense.

### The Honest Position

The informational hypothesis is a **research program**, not a theory. It proposes a structural reading of the biquaternion algebra in which the Hermitian subspace is given a physical meaning as the arena of operations and information. The mathematics is established; the interpretation is a hypothesis.

The hypothesis is **not** in conflict with established physics, because it does not claim to replace any of it. The material sector $\mathbb{M}_-$ reproduces the four-vectors of relativistic physics exactly as in the companion articles. The informational sector $\mathbb{M}_+$ is an **additional** structure, whose physical significance remains to be determined.

The honest position is that the mathematical structure of $\mathbb{M}_+$ is suggestive but the empirical content is not yet specified. The hypothesis is offered because the structure is compelling enough to be worth writing down, and because it connects the biquaternion algebra to a well-established body of mathematical physics (quantum information theory) in a way that is unlikely to be accidental.

## Open Questions

The hypothesis raises several concrete questions. We list them here as a research agenda.

**1. The dynamics of the informational sector.** The material sector has a dynamics: Maxwell's equations for the electromagnetic field, the wave equation for free fields, the Dirac equation for spinors. Does the informational sector have its own dynamics? A natural candidate would be a wave equation for $\mathbb{M}_+$-valued fields, but the precise form is not known. The biquaternion framework provides the operators $\tilde{\nabla}$, $\bar{\tilde{\nabla}}$, and $\Box$, but it is not clear which of these (if any) governs the informational sector.

**2. The coupling between the two sectors.** Beyond the Lorentz coupling via the boost biquaternion, is there a genuinely new coupling between $\mathbb{M}_+$ and $\mathbb{M}_-$? In the standard framework, the only coupling is through the rotor conjugation (the Lorentz transformation). A new coupling would require an equation or a field that mixes the two sectors in a non-trivial way. The analogy with gauge theory suggests that such a coupling might exist, but its form is unknown.

**3. Entropy and thermodynamics.** In quantum information theory, the von Neumann entropy $S(\rho) = -\mathrm{Tr}(\rho \log \rho)$ quantifies the information content of a state. Does the biquaternion framework admit an entropy functional on the states $P_\pm \in \mathbb{M}_+$? The logarithm on $\mathbb{B}$ exists (see the elementary functions article) but is multivalued; the trace is available but is a scalar. A natural candidate would be $S(P) = -2\mathrm{Sc}(P \log P)$, but this needs verification.

**4. The role of the non-Hermitian idempotents.** The non-trivial roots of $-1$ give idempotents that are **not** in $\mathbb{M}_+$. What is their role in the interpretation? Are they "virtual" states, or do they have a physical meaning?

**5. The relation to quantum field theory.** Quantum information theory is most naturally formulated in the context of quantum field theory, where information is carried by fields. How does the biquaternion framework connect to QFT? Is there a biquaternion version of the entanglement structure that plays a role in holography?

**6. Empirical contact.** The most important question: what quantitative prediction distinguishes the informational hypothesis from standard physics? Without an empirical signature, the hypothesis remains a mathematical interpretation. Candidates for empirical contact include: modifications of the Lorentz transformation at very high energies, a new long-range force associated with the informational sector, or a modification of the light cone structure. None of these has been worked out.

**7. The interpretation of the "imaginary directions".** The imaginary vector part of $\mathbb{M}_+$ is interpreted as three "imagined" spatial directions. What is the precise sense in which these directions are "informational" rather than "spatial"? The interpretation is intuitive but not yet formal.

These questions are open, and they constitute the research program associated with the informational hypothesis.

## Summary

The Hermitian subspace $\mathbb{M}_+$ is the complement of the material space $\mathbb{M}_-$ in the biquaternion algebra: $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$. Its elements have real scalar part and imaginary vector part, and its norm form has signature $(1,3)$. It contains the identity, the boost biquaternions, the idempotents $P_\pm = \tfrac{1}{2}(e_0 \pm \mu i)$, and the Hermitian forms $\tilde{Q}\tilde{Q}^\dagger$.

The elements of $\mathbb{M}_+$ act on the material space $\mathbb{M}_-$ by conjugation: $\tilde{X} \mapsto \tilde{H}\tilde{X}\tilde{H}^\dagger$. The action is linear, preserves $\mathbb{M}_-$, and preserves the norm form when $\tilde{H}$ is unitary. The natural dichotomy between unitary and idempotent elements corresponds to the dichotomy between reversible evolution and irreversible measurement.

The mathematics of $\mathbb{M}_+$ is structurally identical to the mathematics of quantum information theory for a two-state system. The idempotents are pure-state density matrices, the Hermitian elements are observables, the unitary elements are gates, and the trace formula $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\mathrm{Sc}(\tilde{P}\tilde{H})$ is the Born rule. The structural correspondence is not an analogy: it is the same mathematics, expressed in the biquaternion algebra.

The **informational hypothesis** is that the mathematics reflects physics: that $\mathbb{M}_+$ is not only a mathematical structure but an **informational sector** of the world, whose elements are the operators acting on the material sector. The hypothesis is offered as a research program. The mathematical structure is established; the empirical content is not yet specified. The article closes with the open questions that constitute the agenda for developing the hypothesis into a physical theory.

The companion article, *$\mathbb{M}_-$ as the Material Space*, presents the established physics of the material sector. Together, the two articles describe the two complementary subspaces of the biquaternion algebra and the structural relation between them.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $\mathbb{M}_+$ | Hermitian subspace: real scalar, imaginary vector |
| $\mathbb{M}_-$ | Anti-Hermitian subspace: imaginary scalar, real vector |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$ | Norm form |
| $\tilde{\Lambda}$ | Boost biquaternion |
| $P_\pm = \tfrac{1}{2}(e_0 \pm \mu i)$ | Idempotent (pure-state projector) |
| $\tilde{H}$ | General Hermitian element (observable) |
| $\tilde{X} \mapsto \tilde{H}\tilde{X}\tilde{H}^\dagger$ | Conjugation action |
| $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace formula (Born rule) |
| $SL(2,\mathbb{C})$ | Group of unit-norm biquaternions |

## Further Reading

- John von Neumann, *Mathematical Foundations of Quantum Mechanics* (Princeton, 1932), for the original formulation of quantum mechanics in terms of Hermitian operators and density matrices.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the standard treatment of qubits, gates, and measurements.
- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford, 1930), for the spin-1/2 formalism.
- Roger Penrose, *The Road to Reality* (Knopf, 2004), for the complex structure of quantum mechanics and its relation to spacetime.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the geometric algebra formulation of quantum mechanics.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the modern geometric algebra treatment of spinors and operators.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the algebraic structure of the Clifford algebra $\mathrm{Cl}_{1,3}$.
- Edward Witten, "Anti-de Sitter Space and Holography" (1998), for the geometric interpretation of information in modern theoretical physics.


