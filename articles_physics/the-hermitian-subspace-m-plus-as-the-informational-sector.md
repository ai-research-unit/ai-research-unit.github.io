# __The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector__

## Introduction

This article is about the **Hermitian subspace** $\mathbb{M}_+$, the fixed space of the Hermitian conjugation: its definition and basis, its algebraic properties, its action by conjugation, and the quantum-information structure it carries.

The mathematics of $\mathbb{M}_+$ is standard: it is a four-dimensional real subspace consisting of elements with real scalar part and imaginary vector part. It contains the boost biquaternions, the Hermitian forms, the idempotents, and the identity. It acts on $\mathbb{M}_-$ by rotor conjugation, and its elements satisfy a natural trace formula. All of this is established mathematics.

The **algebraic identification** of $\mathbb{M}_+$ with the operator algebra of a two-state quantum system is now also established: it is developed in detail in the companion article *Quantum Mechanics in Biquaternionic Form*, and it is not a conjecture. What remains a **hypothesis** is whether this algebraic structure is **physically realised** as a distinct sector of the world, in the same sense as the material sector $\mathbb{M}_-$. This is the central question of the article, and the article's honest position is: **we do not yet know, but the structure is rich enough to be worth writing down.**

The article is organized as follows. First the mathematical structure of $\mathbb{M}_+$ is recalled. Then the physical hypothesis is stated clearly, with the honest position on what it does and does not claim. Then the action of $\mathbb{M}_+$ on $\mathbb{M}_-$ and the algebraic identification with the qubit operator algebra are developed. The distinguished elements of $\mathbb{M}_+$ are collected as examples, and the article closes with open questions.

The conventions are those of the companion articles. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$, the scalar imaginary is $i$, and the biquaternionic gradient is $\tilde{\nabla} = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z$. Throughout, the symbol $c$ denotes the **speed of light in the medium**, $c = 1/\sqrt{\epsilon\mu}$, and $c_0$ denotes the **vacuum speed of light**. In vacuum, $c = c_0$.

## Basic Definition and Properties

### Definition and Basis

The **Hermitian subspace** $\mathbb{M}_+$ is the fixed-point set of the Hermitian conjugation:

$$
\mathbb{M}_+ = \{\tilde{Q} \in \mathbb{B} : \tilde{Q}^\dagger = \tilde{Q}\},
$$

where $\tilde{Q}^\dagger = \bar{\tilde{Q}}^*$. Explicitly, a biquaternion is in $\mathbb{M}_+$ if and only if it has the form

$$
\tilde{Q} = q_0\,e_0 + i q'_1\,e_1 + i q'_2\,e_2 + i q'_3\,e_3, \qquad q_0, q'_1, q'_2, q'_3 \in \mathbb{R}.
$$

The scalar part is **real** and the vector part is **purely imaginary**. Equivalently, if we write $\tilde{Q} = Q_0 e_0 + \mathbf{Q}$, then $\tilde{Q} \in \mathbb{M}_+$ iff $Q_0$ is real and $Q_1, Q_2, Q_3$ are purely imaginary — that is, $Q_0 = q_0$ and $Q_k = iq'_k$.

**The two writings.** The four real parameters are the components of the informational coordinate, the temporal one scaled by $c$:

$$
\tilde{Q} = q_0e_0 + iq'_1e_1 + iq'_2e_2 + iq'_3e_3 = (ct')\,e_0 + (ix')\,e_1 + (iy')\,e_2 + (iz')\,e_3, \qquad q_0 = ct',\;\; q'_1 = x',\;\; q'_2 = y',\;\; q'_3 = z' .
$$

The left-hand writing is in the sector's own parameters and is the one used for algebraic statements; the right-hand one is in the coordinates of physics. The prime marks the coefficient that carries the $i$, which in $\mathbb{M}_+$ is the **three vectors** $q'_k$ — the space. The temporal parameter $q_0 = ct'$ is unprimed and real. The four parameters are the real and imaginary parts of the four complex coefficients of a general biquaternion, $Q_\mu = q_\mu + iq'_\mu$, read off in the pattern that defines this sector: scalar real, vector imaginary.

A natural basis of $\mathbb{M}_+$ is

$$
\{e_0,\; i\,e_1,\; i\,e_2,\; i\,e_3\}.
$$

As a real vector space, $\mathbb{M}_+$ has dimension $4$. It is **not** a subalgebra of $\mathbb{B}$: for example, $(ie_1)(ie_2) = -e_3$, whose vector coefficient is real, so the product lies outside the subspace. (The square of a single element, by contrast, stays in the subspace: for $\tilde{Q} = q_0e_0 + i\mathbf{q}'$ one has $\tilde{Q}^2 = q_0^2 + |\mathbf{q}'|^2 + 2iq_0\mathbf{q}'$.)

### The Defining Involution

The subspace is the fixed space of the **Hermitian conjugation**

$$
\tilde{Q}^\dagger = \bar{\tilde{Q}}^{\,*},
$$

which is an involution: applying it twice returns the original element, $(\tilde{Q}^\dagger)^\dagger = \tilde{Q}$. Write the general biquaternion out in full, with the real and the imaginary part of each of its four coefficients,

$$
\tilde{Q} = (q_0 + iq'_0)\,e_0 + (q_1 + iq'_1)\,e_1 + (q_2 + iq'_2)\,e_2 + (q_3 + iq'_3)\,e_3, \qquad q_\mu, q'_\mu \in \mathbb{R}.
$$

Quaternion conjugation negates the three vector units and leaves the unit, the scalar imaginary, and every coefficient untouched,

$$
\bar{\tilde{Q}} = (q_0 + iq'_0)\,e_0 - (q_1 + iq'_1)\,e_1 - (q_2 + iq'_2)\,e_2 - (q_3 + iq'_3)\,e_3,
$$

and complex conjugation then replaces $i$ by $-i$ throughout, leaving the quaternion units fixed, so that

$$
\tilde{Q}^\dagger = \bar{\tilde{Q}}^{\,*} = (q_0 - iq'_0)\,e_0 - (q_1 - iq'_1)\,e_1 - (q_2 - iq'_2)\,e_2 - (q_3 - iq'_3)\,e_3 ,
$$

so that the scalar coefficient is negated in its imaginary part and each vector coefficient in its real part. Coordinate by coordinate,

| | $q_0$ | $q'_0$ | $q_1$ | $q'_1$ | $q_2$ | $q'_2$ | $q_3$ | $q'_3$ |
|---|---|---|---|---|---|---|---|---|
| image under $\dagger$ | $q_0$ | $-q'_0$ | $-q_1$ | $q'_1$ | $-q_2$ | $q'_2$ | $-q_3$ | $q'_3$ |
| $\tilde{Q}^\dagger = \tilde{Q}$ requires | free | $q'_0 = 0$ | $q_1 = 0$ | free | $q_2 = 0$ | free | $q_3 = 0$ | free |

**The fixed space.** The two sides of $\tilde{Q}^\dagger = \tilde{Q}$ must agree in each of the four units $e_0, e_1, e_2, e_3$, and within a unit they must agree separately in the real and the imaginary part. That is four complex conditions, hence eight real ones, and they read

$$
q_0 - iq'_0 = q_0 + iq'_0 \iff q'_0 = 0, \qquad
-q_k + iq'_k = q_k + iq'_k \iff q_k = 0 \qquad (k = 1, 2, 3),
$$

the first from the scalar unit and the remaining three from the vector units. The solutions are the elements with $q'_0 = 0$ and $q_1 = q_2 = q_3 = 0$, that is,

$$
\tilde{Q}^\dagger = \tilde{Q} \iff \tilde{Q} = q_0\,e_0 + iq'_1\,e_1 + iq'_2\,e_2 + iq'_3\,e_3 .
$$

**Conversely**, every element of this form is fixed. For such an element $\bar{\tilde{Q}} = q_0\,e_0 - iq'_1\,e_1 - iq'_2\,e_2 - iq'_3\,e_3$, hence $\tilde{Q}^\dagger = \bar{\tilde{Q}}^{\,*} = q_0\,e_0 + iq'_1\,e_1 + iq'_2\,e_2 + iq'_3\,e_3 = \tilde{Q}$. The two directions together say that the displayed set is *exactly* the fixed space. The coordinates that survive are the four $q_0, q'_1, q'_2, q'_3$, which is the parametrisation recorded above: the scalar coefficient is real, the three vector coefficients are purely imaginary, and the fixed space is this four-dimensional real subspace, carved out of the eight real coordinates by the four $\mathbb{R}$-linear equations $q'_0 = 0$ and $q_k = 0$.

### Properties

**Quadratic form.** The biquaternion **norm form** restricts to a real quadratic form on $\mathbb{M}_+$:

$$
N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = q_0^2 + (iq'_1)^2 + (iq'_2)^2 + (iq'_3)^2 = q_0^2 - q'^2_1 - q'^2_2 - q'^2_3 = c^2t'^2 - x'^2 - y'^2 - z'^2.
$$

This is a real quadratic form of **signature** $(1,3)$: one positive direction (the temporal one, whose coordinate is $ct'$) and three negative directions (the vector components $q'_1, q'_2, q'_3$). The single positive direction is the temporal one, so the form is Lorentzian with a distinguished timelike axis in the sector's own coordinates.

**Zero divisors.** The norm form vanishes on the cone

$$
q_0^2 = q'^2_1 + q'^2_2 + q'^2_3, \qquad \text{that is} \qquad c^2t'^2 = x'^2 + y'^2 + z'^2,
$$

which is a double cone with apex at the origin. The complement of the cone has three connected components: the region $N < 0$ ($q_0^2 < q'^2_1 + q'^2_2 + q'^2_3$, connected) and the two components of the region $N > 0$ ($q_0 > |\mathbf{q}'|$ and $q_0 < -|\mathbf{q}'|$).

**Not a division algebra.** The presence of the zero divisor cone means that $\mathbb{M}_+$ is not a division algebra: there are nonzero elements of $\mathbb{M}_+$ with no inverse in $\mathbb{B}$.

**Multiplication by $i$.** Since $i$ is central, $i\mathbb{M}_+$ is again a four-dimensional real subspace. It is **not** $\mathbb{M}_+$ itself: multiplying a Hermitian element by $i$ produces an anti-Hermitian one. The sector is therefore not closed under multiplication by the central scalar, which is the visible sign that the Hermitian condition is $\mathbb{R}$-linear and not $\mathbb{C}$-linear. Under quaternion conjugation the sector is preserved: conjugation negates the vector part and leaves the scalar part alone, so $q_0 + i\mathbf{q}' \mapsto q_0 - i\mathbf{q}'$ stays in $\mathbb{M}_+$.

**The parameter pattern.** The defining property of the sector is visible in the parameters alone: the scalar coefficient is real and the three vector coefficients are imaginary. Each of the four complex coefficients $Q_\mu = q_\mu + iq'_\mu$ therefore contributes exactly one real number, and the prime selects which one — for the scalar it is the real part $q_0$, for the three vectors the imaginary parts $q'_1, q'_2, q'_3$. This is why a single conjugation carves a four-dimensional real subspace out of an eight-dimensional real algebra: it fixes one real number in each complex coefficient, in the pattern real-scalar, imaginary-vector.

## Physical Meaning

We now state the hypothesis that motivates this article, in the clearest terms possible.

### Statement of the Hypothesis

**Hypothesis (informational sector).** The Hermitian subspace $\mathbb{M}_+$ is not only a mathematical structure but the arena of an **informational sector** of physics, physically realised in the same sense as the material sector $\mathbb{M}_-$. Its elements are Hermitian operators on the spinor module of $\mathbb{B}$, and the two sectors together constitute the full physical world. The **material sector** $\mathbb{M}_-$ describes the observable, causal structure of spacetime. The **informational sector** $\mathbb{M}_+$ carries the operations, measurements, and information-theoretic content associated with the material sector.

In this reading:

- A **state** of the informational sector is an element $\tilde{\rho} \in \mathbb{M}_+$ that is Hermitian, positive, and of trace one.
- An **observable** of the informational sector is a general Hermitian element $\tilde{Q} \in \mathbb{M}_+$.
- **Evolution** is generated by rotor conjugation $\tilde{\rho} \mapsto \tilde{\Lambda}\tilde{\rho}\tilde{\Lambda}^\dagger$, with $\tilde{\Lambda}$ a unit-norm biquaternion.
- **Measurement** is the idempotent projection $\tilde{\rho} \mapsto \tilde{P}\tilde{\rho}\tilde{P}$.
- **Expectation values** are given by the trace formula $2\,\mathrm{Sc}(\tilde{\rho}\tilde{Q})$.

### The Sector's Own Coordinates

The coordinates of the sector carry the $i$ in a definite place, and this placement is what gives the sector its character. With the temporal parameter $q_0 = ct'$ real and the three spatial parameters $q'_1, q'_2, q'_3$ imaginary, the general element is

$$
\tilde{Q} = q_0e_0 + iq'_1e_1 + iq'_2e_2 + iq'_3e_3 = (ct')\,e_0 + (ix')\,e_1 + (iy')\,e_2 + (iz')\,e_3.
$$

The temporal direction therefore carries a real coordinate while the three spatial directions carry imaginary ones. Two consequences follow. First, the norm form has signature $(1,3)$, so the temporal axis is the single positive direction and the three spatial axes are the negative ones. Second, it is the vectors of this sector, not its scalar, that carry the $i$ — which is why the vectors are the primed parameters while the scalar is not. The placement of the $i$ is a property of the sector, fixed by the conjugation that defines it.

### What the Hypothesis Does and Does Not Claim

**It does claim:**

- The mathematics of $\mathbb{M}_+$ is structurally identical to the mathematics of a quantum-informational system.
- The elements of $\mathbb{M}_+$ act as operators on the spinor module of $\mathbb{B}$.
- The reversible/irreversible dichotomy of $\mathbb{M}_+$ (unitary vs. idempotent) mirrors the evolution/measurement dichotomy of quantum information.
- The **hypothesis** is that this structure is physically realised as a distinct sector.

**It does not claim:**

- That the informational sector has been observed.
- That the informational sector has a specified dynamics (a wave equation, a field equation, a conservation law) beyond the quantum formalism itself.
- That there is a specified coupling between the informational and material sectors beyond the standard Lorentz coupling via the rotor conjugation.
- That the informational sector provides any empirical prediction that distinguishes it from standard physics.
- That the imaginary directions of $\mathbb{M}_+$ are "extra space" in the ordinary sense.

### The Honest Position

The physical hypothesis is a **research program**, not a theory. It proposes a structural reading of the biquaternion algebra in which the Hermitian subspace is given a physical meaning as the arena of operations and information. The mathematics is established; the physical interpretation is a hypothesis.

The hypothesis is **not** in conflict with established physics, because it does not claim to replace any of it. The material sector $\mathbb{M}_-$ reproduces the four-vectors of relativistic physics, and the informational sector $\mathbb{M}_+$ carries the full operator algebra of a qubit. Whether $\mathbb{M}_+$ is a distinct physical sector, or only a mathematical structure that happens to describe the kinematics of a qubit, is an open question.

### Open Questions

The hypothesis raises several concrete questions. We list them here as a research agenda.

**1. Physical reality of the informational sector.** Is $\mathbb{M}_+$ realised physically as a distinct sector, or is it only a mathematical structure that happens to describe the kinematics of a qubit? A genuine physical realisation would require a coupling to the material sector that has observable consequences.

**2. The dynamics of the informational sector.** Beyond the standard quantum dynamics of the operator algebra, does $\mathbb{M}_+$ have its own dynamics as a sector? Are there $\mathbb{M}_+$-valued fields with wave equations? The biquaternion operators $\tilde{\nabla}$, $\bar{\tilde{\nabla}}$, and $\Box$ are available, but it is not clear which (if any) governs $\mathbb{M}_+$-valued fields.

**3. The coupling between the two sectors.** Beyond the Lorentz coupling via the rotor conjugation, is there a genuinely new coupling between $\mathbb{M}_+$ and $\mathbb{M}_-$? A new coupling would require an equation or a field that mixes the two sectors in a non-trivial way.

**4. Entropy and thermodynamics.** In quantum information theory, the von Neumann entropy $S(\rho) = -\mathrm{Tr}(\rho \log \rho)$ quantifies the information content of a state. Does the biquaternion framework admit an entropy functional on the states of $\mathbb{M}_+$? The logarithm on $\mathbb{B}$ exists (see the elementary functions article) but is multivalued; the trace is available but is a scalar. A natural candidate would be $S(\tilde{\rho}) = -2\mathrm{Sc}(\tilde{\rho}\log\tilde{\rho})$, but this needs verification.

**5. The role of the non-Hermitian idempotents.** The non-trivial roots of $-1$ give idempotents that are **not** in $\mathbb{M}_+$. What is their role in the interpretation? Are they "virtual" states, or do they have a physical meaning?

**6. The relation to quantum field theory.** Quantum information theory is most naturally formulated in the context of quantum field theory, where information is carried by fields. How does the biquaternion framework connect to QFT? Is there a biquaternion version of the entanglement structure?

**7. Empirical contact.** The most important question: what quantitative prediction distinguishes the informational hypothesis from standard physics? Without an empirical signature, the hypothesis remains a mathematical interpretation. Candidates for empirical contact include: modifications of the Lorentz transformation at very high energies, a new long-range force associated with the informational sector, or a modification of the light cone structure. None of these has been worked out.

**8. The interpretation of the "imaginary directions".** The imaginary vector part of $\mathbb{M}_+$ carries the $i$. What is the precise sense in which these imaginary directions are "informational" rather than "spatial"? The formal structure is clear; the physical interpretation is not yet formal.

These questions are open, and they constitute the research program associated with the informational hypothesis.

## Advanced Algebraic Properties

### The Action of $\mathbb{M}_+$ on $\mathbb{M}_-$

The most important structural fact about $\mathbb{M}_+$ is that its elements **act** on the elements of $\mathbb{M}_-$ by **conjugation**:

$$
\tilde{Q}_- \;\longmapsto\; \tilde{Q}_+\,\tilde{Q}_-\,\tilde{Q}_+^\dagger, \qquad \tilde{Q}_+ \in \mathbb{M}_+, \; \tilde{Q}_- \in \mathbb{M}_-.
$$

### Basic Properties of the Action

**1. The image is in $\mathbb{M}_-$.** If $\tilde{Q}_-^\dagger = -\tilde{Q}_-$ (anti-Hermitian) and $\tilde{Q}_+^\dagger = \tilde{Q}_+$ (Hermitian), then

$$
(\tilde{Q}_+\tilde{Q}_-\tilde{Q}_+^\dagger)^\dagger = \tilde{Q}_+^{\dagger\dagger}\tilde{Q}_-^\dagger\tilde{Q}_+^\dagger = \tilde{Q}_+(-\tilde{Q}_-)\tilde{Q}_+^\dagger = -\tilde{Q}_+\tilde{Q}_-\tilde{Q}_+^\dagger,
$$

so the image is anti-Hermitian, i.e., in $\mathbb{M}_-$. The action maps the material space to itself.

**2. The action is linear in $\tilde{Q}_-$.** This follows from the bilinearity of the biquaternion product.

**3. The action preserves the norm form when $\tilde{Q}_+$ has unit norm form.** If $\tilde{Q}_+\bar{\tilde{Q}}_+ = e_0$ — for example a boost biquaternion, or any element of $SL(2,\mathbb{C})$ — then the action preserves $N(\tilde{Q}_-) = \tilde{Q}_-\bar{\tilde{Q}}_-$: by multiplicativity of the norm form, $N(\tilde{Q}_+\tilde{Q}_-\tilde{Q}_+^\dagger) = N(\tilde{Q}_+)N(\tilde{Q}_-)N(\tilde{Q}_+)^* = N(\tilde{Q}_-)$ when $N(\tilde{Q}_+) = 1$. This is the biquaternion expression of the Lorentz invariance of the Minkowski interval. The condition is on the norm form and not on $\tilde{Q}_+\tilde{Q}_+^\dagger$: a boost biquaternion is Hermitian, so $\tilde{Q}_+\tilde{Q}_+^\dagger = \tilde{Q}_+^2 = \cosh\tfrac{\psi}{2} + i\sinh\tfrac{\psi}{2}\,\hat{\mathbf{u}} \neq e_0$, and only the rotation rotors satisfy $\tilde{Q}\tilde{Q}^\dagger = e_0$.

**4. The action is a group action.** Compositions of actions compose:

$$
\tilde{Q}_{+2}\bigl(\tilde{Q}_{+1}\tilde{Q}_-\tilde{Q}_{+1}^\dagger\bigr)\tilde{Q}_{+2}^\dagger = (\tilde{Q}_{+2}\tilde{Q}_{+1})\,\tilde{Q}_-\,(\tilde{Q}_{+2}\tilde{Q}_{+1})^\dagger.
$$

### The Structural Relation: Operators and States

The action of $\mathbb{M}_+$ on the four-vector space has the structure of **operators acting on states**:

- The four-vector space is the space of **kinematic configurations** (the four-vectors of position, velocity, momentum, potential, current).
- $\mathbb{M}_+$ is the space of **operators** (the Hermitian biquaternions that act on these configurations).

This is the algebraic content of the reading of $\mathbb{M}_+$ as "informational" (or "operational"): its elements are the things that act, rather than the things that are acted upon. The two roles are not symmetric — one acts, the other is acted upon — and the asymmetry is what earns the sector its name.

### Reversible Versus Irreversible Actions

The elements of $\mathbb{M}_+$ include two important classes.

**Unit-norm-form elements** ($\tilde{Q}\bar{\tilde{Q}} = e_0$, i.e. $\tilde{Q} \in SL(2,\mathbb{C})$). These preserve the norm form and act by **reversible** transformations. Examples: the boost biquaternions $\tilde{\Lambda}$ and the spatial rotation rotors. These correspond to Lorentz transformations. The stronger condition $\tilde{Q}\tilde{Q}^\dagger = e_0$ is satisfied by the rotation rotors, which are real quaternions, but not by the boosts.

**Idempotent elements** ($\tilde{Q}^2 = \tilde{Q}$). These do not preserve the norm form (unless $\tilde{Q} = e_0$). They act by **irreversible** projections: $\tilde{Q}_- \mapsto \tilde{P}\tilde{Q}_-\tilde{P}$. Examples: the pure-state projectors $\tilde{P}_\pm(\hat{\boldsymbol\mu}) = \tfrac{1}{2}(e_0 \pm i\hat{\boldsymbol\mu})$. These correspond to quantum-mechanical measurements.

The **dichotomy between reversible and irreversible actions** is intrinsic to the structure of $\mathbb{M}_+$: it is the biquaternion version of the fundamental dichotomy of quantum information theory between unitary evolution and measurement.

### The Trace Formula

For $\tilde{P} \in \mathbb{M}_+$ idempotent (a state) and $\tilde{Q} \in \mathbb{M}_+$ Hermitian (an observable), the quantity

$$
\langle \tilde{Q} \rangle_{\tilde{P}} = \mathrm{Tr}(\tilde{P}\tilde{Q}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{Q})
$$

is **real**. It has the form of a **quantum-mechanical expectation value**: the trace of the product of a state and an observable. For example, if $\tilde{P} = \tfrac{1}{2}(e_0 + i\hat{\boldsymbol\mu})$ and $\tilde{Q} = h_0 e_0 + i\mathbf{h}\cdot\mathbf{e}$, then

$$
\langle \tilde{Q} \rangle_{\tilde{P}} = h_0 + \hat{\boldsymbol\mu}\cdot\mathbf{h},
$$

which is the standard spin-1/2 expectation value along the direction $\hat{\boldsymbol\mu}$. The trace formula is the biquaternion expression of the Born rule.

### The Algebraic Identification with Quantum Information

The mathematics of $\mathbb{M}_+$ and its action on $\mathbb{M}_-$ is **structurally identical** to the mathematics of quantum information theory for a single qubit. This is an algebraic fact, established in detail in the companion article *Quantum Mechanics in Biquaternionic Form*.

### The Correspondence

| Quantum information | Biquaternion framework |
|---|---|
| State space $\mathbb{C}^2$ | Spinor module of $\mathbb{B}$ |
| Density matrix $\rho$ (Hermitian, positive, trace 1) | Element $\tilde{\rho} \in \mathbb{M}_+$ (Hermitian, positive, trace 1) |
| Pure state $\lvert\psi\rangle\langle\psi\rvert$ | Idempotent $\tfrac{1}{2}(e_0 + i\hat{\boldsymbol\mu})$ |
| Observable (Hermitian operator) | Hermitian element $\tilde{Q} \in \mathbb{M}_+$ |
| Unitary gate $U$ | Unit-norm element $\tilde{\Lambda}$ of $SL(2,\mathbb{C})$ |
| Expectation value $\mathrm{Tr}(\rho H)$ | Trace formula $2\,\mathrm{Sc}(\tilde{\rho}\tilde{Q})$ |
| Reversible evolution $U\rho U^\dagger$ | Rotor conjugation $\tilde{\Lambda}\tilde{\rho}\tilde{\Lambda}^\dagger$ |
| Projective measurement $\rho \mapsto P\rho P$ | Idempotent projection $\tilde{\rho} \mapsto \tilde{P}\tilde{\rho}\tilde{P}$ |

The correspondence is not an analogy. **It is the same mathematics**, expressed in two different notations: the Hermitian elements of the algebra are the operators of a two-state system.

### What the Correspondence Is and Is Not

**What it is:** A structural fact about the algebra. The elements of $\mathbb{M}_+$ are Hermitian operators on the spinor module of $\mathbb{B}$, and the algebra they generate is the algebra of observables of a two-state system. The mathematics of quantum information applies to $\mathbb{M}_+$ as it applies to any such algebra.

**What it is not (yet):** A physical theory. The structural correspondence does not by itself establish that $\mathbb{M}_+$ **is** an informational sector of physics. It establishes that if $\mathbb{M}_+$ were given an informational interpretation, the mathematics would be available. Whether the interpretation is realised in nature is a separate question.

### The Spin Analogy

The correspondence with quantum information is closely related to the **spin-1/2 formalism** of non-relativistic quantum mechanics.

- In spin-1/2 quantum mechanics, the state space is $\mathbb{C}^2$, and the observables are the Pauli matrices $\sigma_k$ generating $\mathfrak{su}(2)$. The rotation group $SU(2)$ acts on the states.
- In the biquaternion framework, the spinor module of $\mathbb{B}$ is the state space, and the Hermitian elements of $\mathbb{M}_+$ are the observables. The action is by rotor conjugation on the module.

The difference is:

- In spin-1/2, the operators generate the **compact** group $SU(2)$ (rotations).
- In $\mathbb{M}_+$, the Hermitian elements generate the **non-compact** group $SL(2,\mathbb{C})$ (Lorentz transformations).

The compact/non-compact distinction reflects the difference between rotations in a spacelike plane (compact) and boosts in a timelike plane (non-compact). The biquaternion framework extends the spin-1/2 structure to the relativistic setting: the operators generate the Lorentz group rather than the rotation group, and the corresponding observables include boosts (Hermitian biquaternions with imaginary vector part) alongside rotations.

The biquaternion framework can therefore be read as a **relativistic generalisation of the spin-1/2 formalism**, in which the state space is the spinor module of $\mathbb{B}$ and the symmetry group is the Lorentz group.

## Examples

The companion articles already contain several distinguished elements of $\mathbb{M}_+$. It is worth collecting them, because they are the natural candidates for the objects of the informational sector.

### The Boost Biquaternion

The **boost biquaternion**

$$
\tilde{\Lambda} = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\,\hat{\mathbf{u}}, \qquad \hat{\mathbf{u}}^2 = -e_0,
$$

lies in $\mathbb{M}_+$: its scalar part $\cosh(\psi/2)$ is real, and its vector part $i\sinh(\psi/2)\hat{\mathbf{u}}$ is purely imaginary. It is Hermitian ($\tilde{\Lambda}^\dagger = \tilde{\Lambda}$) and has unit norm ($\tilde{\Lambda}\bar{\tilde{\Lambda}} = e_0$). It acts on $\mathbb{M}_-$ by rotor conjugation, implementing a Lorentz boost.

The boost biquaternion is a distinguished element of $\mathbb{M}_+$, and it is the **prototype** of an operator acting on the material sector $\mathbb{M}_-$. More generally, every unit-norm biquaternion $\tilde{\Lambda} \in \mathbb{B}$ acts on $\mathbb{M}_-$ by rotor conjugation $\tilde{Q} \mapsto \tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^\dagger$. For pure boosts, $\tilde{\Lambda}$ lies in $\mathbb{M}_+$. For pure spatial rotations, $\tilde{\Lambda}$ lies in $\mathbb{H}_{\mathbb{B}}$. For general Lorentz transformations, $\tilde{\Lambda}$ is a general unit-norm biquaternion in $\mathbb{B}$. The point is that the action of any such rotor on $\mathbb{M}_-$ preserves $\mathbb{M}_-$.

### The Idempotents

The **idempotents** of $\mathbb{B}$ of the form

$$
\tilde{P}_\pm(\hat{\boldsymbol\mu}) = \tfrac{1}{2}\left(e_0 \pm i\hat{\boldsymbol\mu}\right), \qquad \hat{\boldsymbol\mu}^2 = -e_0, \; \hat{\boldsymbol\mu} \text{ a real unit pure quaternion},
$$

lie in $\mathbb{M}_+$: their scalar part $\tfrac{1}{2}$ is real, and their vector part $\pm \tfrac{1}{2} i \hat{\boldsymbol\mu}$ is purely imaginary. They satisfy:

- **Hermitian:** $\tilde{P}_\pm^\dagger = \tilde{P}_\pm$, since $\tilde{P}_\pm(\hat{\boldsymbol\mu}) \in \mathbb{M}_+$.
- **Idempotent:** $\tilde{P}_\pm^2 = \tilde{P}_\pm$.
- **Unit trace:** $\mathrm{Tr}(\tilde{P}_\pm) = 2\,\mathrm{Sc}(\tilde{P}_\pm) = 1$.

These are the biquaternion analogues of **pure-state density matrices** of quantum mechanics. They are the natural "states" of the informational sector.

### The Hermitian Forms

For any biquaternion $\tilde{Q} \in \mathbb{B}$, the **Hermitian form**

$$
\tilde{Q}\tilde{Q}^\dagger
$$

is an element of $\mathbb{M}_+$: it is Hermitian by construction. Its scalar part is $\|\tilde{Q}\|_E^2 = \sum_\mu |Q_\mu|^2$, the Euclidean norm squared, which is non-negative.
The Hermitian form is the natural "weight" or "energy" of the state $\tilde{Q}$, and it is the closest biquaternion analogue of the trace of a density matrix.

### The Identity

The identity $e_0$ is trivially in $\mathbb{M}_+$. It corresponds to the trivial state or the identity operator.

### Summary of the Elements of $\mathbb{M}_+$

| Object | Structure | Role |
|---|---|---|
| Identity $e_0$ | Real scalar | Identity operator |
| Boost biquaternion $\tilde{\Lambda}$ | Hermitian, unit norm | Lorentz boost rotor |
| Idempotent $\tilde{P}_\pm(\hat{\boldsymbol\mu})$ | Hermitian, idempotent, trace 1 | Pure state / projector |
| Hermitian form $\tilde{Q}\tilde{Q}^\dagger$ | Hermitian, positive scalar part | Weight of a state |

The common feature of these objects is that they are **Hermitian** (fixed under $\dagger$). This is what defines membership in $\mathbb{M}_+$.

## Summary

The Hermitian subspace $\mathbb{M}_+$ is a four-dimensional real subspace of the biquaternion algebra, consisting of elements with real scalar part and imaginary vector part. Its norm form has signature $(1,3)$, the temporal direction being the single positive one. It contains the identity, the boost biquaternions, the idempotents $\tilde{P}_\pm(\hat{\boldsymbol\mu}) = \tfrac{1}{2}(e_0 \pm i\hat{\boldsymbol\mu})$, and the Hermitian forms $\tilde{Q}\tilde{Q}^\dagger$.

The elements of $\mathbb{M}_+$ act on the material space $\mathbb{M}_-$ by conjugation: $\tilde{Q}_- \mapsto \tilde{Q}_+\tilde{Q}_-\,\tilde{Q}_+^\dagger$. The action is linear, preserves $\mathbb{M}_-$, and preserves the norm form when $\tilde{Q}_+$ has unit norm form. The natural dichotomy between unit-norm-form and idempotent elements corresponds to the dichotomy between reversible evolution and irreversible measurement.

The mathematics of $\mathbb{M}_+$ is structurally identical to the mathematics of quantum information theory for a two-state system. The idempotents are pure-state density matrices, the Hermitian elements are observables, the unitary elements are gates, and the trace formula $\mathrm{Tr}(\tilde{P}\tilde{Q}) = 2\mathrm{Sc}(\tilde{P}\tilde{Q})$ is the Born rule. The structural correspondence is not an analogy: it is the same mathematics, expressed in the biquaternion algebra.

The **physical hypothesis** is that this mathematics reflects physics: that $\mathbb{M}_+$ is not only a mathematical structure but an **informational sector** of the world, physically realised in the same sense as the material sector. The hypothesis is offered as a research program. The mathematical structure is established; the empirical content is not yet specified. The article closes with the open questions that constitute the agenda for developing the hypothesis into a physical theory.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\mathbb{M}_+$ | Hermitian subspace (informational sector): real scalar, imaginary vector; parameters $q_0, q'_1, q'_2, q'_3$, with $q_0 = ct'$ |
| $Q_\mu = q_\mu + iq'_\mu$ | Complex coefficient of $e_\mu$: $q_\mu$ its real part, $q'_\mu$ its imaginary part |
| $\tilde{Q} = q_0e_0 + iq'_ke_k = (ct')\,e_0 + i\mathbf{x}'$ | Informational element, both writings; $q_0 = ct'$, $q'_k = x'_k$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$ | Norm form |
| $\tilde{\Lambda} \in \mathbb{B}$, $\tilde{\Lambda}\bar{\tilde{\Lambda}} = e_0$ | Lorentz rotor (unit-norm biquaternion) |
| $\tilde{P}_\pm(\hat{\boldsymbol\mu}) = \tfrac{1}{2}(e_0 \pm i\hat{\boldsymbol\mu})$ | Idempotent (pure-state projector) of unit trace |
| $\tilde{Q}$ | General Hermitian element (observable) |
| $\tilde{Q}_- \mapsto \tilde{Q}_+\tilde{Q}_-\,\tilde{Q}_+^\dagger$ | Conjugation action of $\mathbb{M}_+$ on $\mathbb{M}_-$ |
| $\tilde{Q}_+$, $\tilde{Q}_-$ | Hermitian element of $\mathbb{M}_+$ (operator) and anti-Hermitian element of $\mathbb{M}_-$ (acted upon); written $\tilde{Q}$ when only one element is in play |
| $\mathrm{Tr}(\tilde{P}\tilde{Q}) = 2\mathrm{Sc}(\tilde{P}\tilde{Q})$ | Trace formula (Born rule) |
| $SL(2,\mathbb{C})$ | Group of unit-norm biquaternions |

## Further Reading

- John von Neumann, *Mathematical Foundations of Quantum Mechanics* (Princeton, 1932), for the original formulation of quantum mechanics in terms of Hermitian operators and density matrices.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the standard treatment of qubits, gates, and measurements.
- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford, 1930), for the spin-1/2 formalism.
- Roger Penrose, *The Road to Reality* (Knopf, 2004), for the complex structure of quantum mechanics and its relation to spacetime.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the geometric algebra formulation of quantum mechanics.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the modern geometric algebra treatment of spinors and operators.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the algebraic structure of the Clifford algebra $\mathrm{Cl}_{1,3}$.
- Asher Peres, *Quantum Theory: Concepts and Methods* (Kluwer, 1993), for the operational reading of states, observables, and measurements used here.
- *Conventions in the Biquaternion Universe* and *Relations Between Subspaces*, the companion articles, for the notation and for the place of $\mathbb{M}_+$ among the six subspaces.

