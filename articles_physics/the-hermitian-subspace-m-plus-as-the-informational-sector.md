# __The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector__

## Introduction

This article is about the **informational sector** $\mathbb{M}_+$, the Hermitian subspace: the sector of the boost biquaternions, of the Hermitian forms and of the quantum-information structure. It is the fixed space of the Hermitian conjugation, and the article treats its definition and basis, its algebraic properties and its action by conjugation.

The mathematics of $\mathbb{M}_+$ is standard: it is a four-dimensional real subspace consisting of elements with real scalar part and imaginary vector part. It contains the boost biquaternions, the Hermitian forms, the idempotents, and the identity. It acts on $\mathbb{M}_-$ by rotor conjugation, and its elements satisfy a natural trace formula. All of this is established mathematics.

The **algebraic identification** of $\mathbb{M}_+$ with the operator algebra of a two-state quantum system is now also established: it is developed in detail in the companion article *Quantum Physics in Biquaternionic Form*, and it is not a conjecture. What remains a **hypothesis** is whether this algebraic structure is **physically realised** as a distinct sector of the world, in the same sense as the material sector $\mathbb{M}_-$. This is the central question of the article, and the article's honest position is: **we do not yet know, but the structure is rich enough to be worth writing down.**

The article is organized as follows. First the mathematical structure of $\mathbb{M}_+$ is recalled. Then the physical hypothesis is stated clearly, with the honest position on what it does and does not claim. Then the action of $\mathbb{M}_+$ on $\mathbb{M}_-$ and the algebraic identification with the qubit operator algebra are developed. The distinguished elements of $\mathbb{M}_+$ are collected as examples, and the article closes with open questions.

The conventions are those of the companion articles. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$, the scalar imaginary is $i$, and the biquaternionic gradient is $\tilde{\nabla} = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z$. Throughout, the symbol $c$ denotes the **speed of light in the medium**, $c = 1/\sqrt{\epsilon\mu}$, and $c_0$ denotes the **vacuum speed of light**. In vacuum, $c = c_0$.

## Basic Definition and Properties

### Definition and Basis

The **Hermitian subspace** $\mathbb{M}_+$ is the fixed-point set of the Hermitian conjugation:

$$
\mathbb{M}_+ = \{\tilde{Q} \in \mathbb{B} : \tilde{Q}^{*} = \tilde{Q}\},
$$

where $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}$. Explicitly, a biquaternion is in $\mathbb{M}_+$ if and only if it has the form

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

As a real vector space, $\mathbb{M}_+$ has dimension $4$. It is **not** a subalgebra of $\mathbb{B}$: for example, $(ie_1)(ie_2) = -e_3$, whose vector coefficient is real, so the product lies outside the subspace. The obstruction is the antisymmetric part of the product. For $\tilde{Q} = q_0e_0 + i\mathbf{u}$ and $\tilde{R} = r_0e_0 + i\mathbf{v}$ with $q_0, r_0$ real and $\mathbf{u}, \mathbf{v}$ real vectors,

$$
\tilde{Q}\tilde{R} = \left(q_0r_0 + (\mathbf{u},\mathbf{v})\right)e_0 + i\left(q_0\mathbf{v} + r_0\mathbf{u}\right) - \mathbf{u}\times\mathbf{v},
$$

so the product stays in the sector exactly when the real vector $\mathbf{u}\times\mathbf{v}$ vanishes, that is when the two elements commute; the antisymmetric part alone leaves, and it leaves as the commutator

$$
\tilde{Q}\tilde{R} - \tilde{R}\tilde{Q} = -2\,\mathbf{u}\times\mathbf{v} \in \mathbb{M}_- .
$$

The symmetrised product therefore always stays in the sector, while the commutator leaves it whenever it is not zero, and the square is the commuting case $\tilde{R} = \tilde{Q}$: it is the one product of an element with an element that can never witness the failure of closure, and for $\tilde{Q} = q_0e_0 + i\mathbf{q}'$ it is $\tilde{Q}^2 = q_0^2 + |\mathbf{q}'|^2 + 2iq_0\mathbf{q}'$. The product rule in its four complex forms, one for each pair of the remarkable subspaces, is computed in *Remarkable Subspaces and the Four General Products*.

### The Defining Involution

The subspace is the fixed space of the **Hermitian conjugation**

$$
\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}},
$$

which is an involution: applying it twice returns the original element, $(\tilde{Q}^{*})^{*} = \tilde{Q}$. Write the general biquaternion out in full, with the real and the imaginary part of each of its four coefficients,

$$
\tilde{Q} = (q_0 + iq'_0)\,e_0 + (q_1 + iq'_1)\,e_1 + (q_2 + iq'_2)\,e_2 + (q_3 + iq'_3)\,e_3, \qquad q_\mu, q'_\mu \in \mathbb{R}.
$$

Quaternion conjugation negates the three vector units and leaves the unit, the scalar imaginary, and every coefficient untouched,

$$
\tilde{Q}^{\natural} = (q_0 + iq'_0)\,e_0 - (q_1 + iq'_1)\,e_1 - (q_2 + iq'_2)\,e_2 - (q_3 + iq'_3)\,e_3,
$$

and complex conjugation then replaces $i$ by $-i$ throughout, leaving the quaternion units fixed, so that

$$
\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}} = (q_0 - iq'_0)\,e_0 - (q_1 - iq'_1)\,e_1 - (q_2 - iq'_2)\,e_2 - (q_3 - iq'_3)\,e_3 ,
$$

so that the scalar coefficient is negated in its imaginary part and each vector coefficient in its real part. Coordinate by coordinate,

| | $q_0$ | $q'_0$ | $q_1$ | $q'_1$ | $q_2$ | $q'_2$ | $q_3$ | $q'_3$ |
|---|---|---|---|---|---|---|---|---|
| image under ${}^{*}$ | $q_0$ | $-q'_0$ | $-q_1$ | $q'_1$ | $-q_2$ | $q'_2$ | $-q_3$ | $q'_3$ |
| $\tilde{Q}^{*} = \tilde{Q}$ requires | free | $q'_0 = 0$ | $q_1 = 0$ | free | $q_2 = 0$ | free | $q_3 = 0$ | free |

**The fixed space.** The two sides of $\tilde{Q}^{*} = \tilde{Q}$ must agree in each of the four units $e_0, e_1, e_2, e_3$, and within a unit they must agree separately in the real and the imaginary part. That is four complex conditions, hence eight real ones, and they read

$$
q_0 - iq'_0 = q_0 + iq'_0 \iff q'_0 = 0, \qquad
-q_k + iq'_k = q_k + iq'_k \iff q_k = 0 \qquad (k = 1, 2, 3),
$$

the first from the scalar unit and the remaining three from the vector units. The solutions are the elements with $q'_0 = 0$ and $q_1 = q_2 = q_3 = 0$, that is,

$$
\tilde{Q}^{*} = \tilde{Q} \iff \tilde{Q} = q_0\,e_0 + iq'_1\,e_1 + iq'_2\,e_2 + iq'_3\,e_3 .
$$

**Conversely**, every element of this form is fixed. For such an element $\tilde{Q}^{\natural} = q_0\,e_0 - iq'_1\,e_1 - iq'_2\,e_2 - iq'_3\,e_3$, hence $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}} = q_0\,e_0 + iq'_1\,e_1 + iq'_2\,e_2 + iq'_3\,e_3 = \tilde{Q}$. The two directions together say that the displayed set is *exactly* the fixed space. The coordinates that survive are the four $q_0, q'_1, q'_2, q'_3$, which is the parametrisation recorded above: the scalar coefficient is real, the three vector coefficients are purely imaginary, and the fixed space is this four-dimensional real subspace, carved out of the eight real coordinates by the four $\mathbb{R}$-linear equations $q'_0 = 0$ and $q_k = 0$.

### Properties

**Quadratic form.** The biquaternion **biquaternion norm** restricts to a real quadratic form on $\mathbb{M}_+$:

$$
N(\tilde{Q}) = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = q_0^2 + (iq'_1)^2 + (iq'_2)^2 + (iq'_3)^2 = q_0^2 - (q'_1)^2 - (q'_2)^2 - (q'_3)^2 = c^2(t')^2 - (x')^2 - (y')^2 - (z')^2.
$$

This is a real quadratic form of **signature** $(1,3)$: one positive direction (the temporal one, whose coordinate is $ct'$) and three negative directions (the vector components $q'_1, q'_2, q'_3$). The single positive direction is the temporal one, so the form is Lorentzian with a distinguished timelike axis in the sector's own coordinates.

**Zero divisors.** The biquaternion norm vanishes on the cone

$$
q_0^2 = (q'_1)^2 + (q'_2)^2 + (q'_3)^2, \qquad \text{that is} \qquad c^2(t')^2 = (x')^2 + (y')^2 + (z')^2,
$$

which is a double cone with apex at the origin. The complement of the cone has three connected components: the region $N < 0$ ($q_0^2 < (q'_1)^2 + (q'_2)^2 + (q'_3)^2$, connected) and the two components of the region $N > 0$ ($q_0 > |\mathbf{q}'|$ and $q_0 < -|\mathbf{q}'|$).

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
- **Evolution** is generated by rotor conjugation $\tilde{\rho} \mapsto \tilde{\Lambda}\tilde{\rho}\tilde{\Lambda}^{*}$, with $\tilde{\Lambda}$ a unit-norm biquaternion.
- **Measurement** is the idempotent projection $\tilde{\rho} \mapsto \tilde{P}\tilde{\rho}\tilde{P}$.
- **Expectation values** are given by the trace formula $2\,\mathrm{Sc}(\tilde{\rho}\tilde{Q})$.

### The Sector's Own Coordinates

The coordinates of the sector carry the $i$ in a definite place, and this placement is what gives the sector its character. With the temporal parameter $q_0 = ct'$ real and the three spatial parameters $q'_1, q'_2, q'_3$ imaginary, the general element is

$$
\tilde{Q} = q_0e_0 + iq'_1e_1 + iq'_2e_2 + iq'_3e_3 = (ct')\,e_0 + (ix')\,e_1 + (iy')\,e_2 + (iz')\,e_3.
$$

The temporal direction therefore carries a real coordinate while the three spatial directions carry imaginary ones. Two consequences follow. First, the biquaternion norm has signature $(1,3)$, so the temporal axis is the single positive direction and the three spatial axes are the negative ones. Second, it is the vectors of this sector, not its scalar, that carry the $i$ — which is why the vectors are the primed parameters while the scalar is not. The placement of the $i$ is a property of the sector, fixed by the conjugation that defines it.

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

**2. The dynamics of the informational sector.** Beyond the standard quantum dynamics of the operator algebra, does $\mathbb{M}_+$ have its own dynamics as a sector? Are there $\mathbb{M}_+$-valued fields with wave equations? The biquaternion operators $\tilde{\nabla}$, $\tilde{\nabla}^{\natural}$, and $\Box$ are available, but it is not clear which (if any) governs $\mathbb{M}_+$-valued fields.

**3. The coupling between the two sectors.** Beyond the Lorentz coupling via the rotor conjugation, is there a genuinely new coupling between $\mathbb{M}_+$ and $\mathbb{M}_-$? A new coupling would require an equation or a field that mixes the two sectors in a non-trivial way.

**4. Entropy and thermodynamics.** In quantum information theory, the von Neumann entropy $S(\rho) = -\mathrm{Tr}(\rho \log \rho)$ quantifies the information content of a state. Does the biquaternion framework admit an entropy functional on the states of $\mathbb{M}_+$? The logarithm on $\mathbb{B}$ exists (see the elementary functions article) but is multivalued; the trace is available but is a scalar. A natural candidate would be $S(\tilde{\rho}) = -2\mathrm{Sc}(\tilde{\rho}\log\tilde{\rho})$, but this needs verification.

**5. The role of the non-Hermitian idempotents.** The non-trivial roots of $-1$ give idempotents that are **not** in $\mathbb{M}_+$. What is their role in the interpretation? Are they "virtual" states, or do they have a physical meaning?

**6. The relation to quantum field theory.** Quantum information theory is most naturally formulated in the context of quantum field theory, where information is carried by fields. How does the biquaternion framework connect to QFT? Is there a biquaternion version of the entanglement structure?

**7. Empirical contact.** The most important question: what quantitative prediction distinguishes the informational hypothesis from standard physics? Without an empirical signature, the hypothesis remains a mathematical interpretation. Candidates for empirical contact include: modifications of the Lorentz transformation at very high energies, a new long-range force associated with the informational sector, or a modification of the light cone structure. None of these has been worked out.

**8. The interpretation of the "imaginary directions".** The imaginary vector part of $\mathbb{M}_+$ carries the $i$. What is the precise sense in which these imaginary directions are "informational" rather than "spatial"? The formal structure is clear; the physical interpretation is not yet formal. One partial formalisation is in *The Biquaternion Fourier Transform and the Imaginary Directions*: there the imaginary directions are the **conjugate** directions, the axis that the root of $-1$ in the Fourier kernel selects and along which the conjugate variable — the frequency, the wavevector — is paired, so that an imaginary direction is a direction the pairing uses and not a direction in which anything propagates.

These questions are open, and they constitute the research program associated with the informational hypothesis.

## Advanced Algebraic Properties

### The Action of $\mathbb{M}_+$ on $\mathbb{M}_-$

The most important structural fact about $\mathbb{M}_+$ is that its elements **act** on the elements of $\mathbb{M}_-$ by **conjugation**:

$$
\tilde{Q}_- \;\longmapsto\; \tilde{Q}_+\,\tilde{Q}_-\,\tilde{Q}_+^{*}, \qquad \tilde{Q}_+ \in \mathbb{M}_+, \; \tilde{Q}_- \in \mathbb{M}_-.
$$

### Basic Properties of the Action

**1. The image is in $\mathbb{M}_-$.** If $\tilde{Q}_-^{*} = -\tilde{Q}_-$ (anti-Hermitian) and $\tilde{Q}_+^{*} = \tilde{Q}_+$ (Hermitian), then

$$
(\tilde{Q}_+\tilde{Q}_-\tilde{Q}_+^\dagger)^{*} = (\tilde{Q}_+^{*})^{*}\tilde{Q}_-^{*}\tilde{Q}_+^{*} = \tilde{Q}_+(-\tilde{Q}_-)\tilde{Q}_+^{*} = -\tilde{Q}_+\tilde{Q}_-\tilde{Q}_+^{*},
$$

so the image is anti-Hermitian, i.e., in $\mathbb{M}_-$. The action maps the material space to itself.

**2. The action is linear in $\tilde{Q}_-$.** This follows from the bilinearity of the biquaternion product.

**3. The action preserves the biquaternion norm when $\tilde{Q}_+$ has unit norm.** If $\tilde{Q}_+\tilde{Q}^{\natural}_+ = e_0$ — for example a boost biquaternion, or any element of $SL(2,\mathbb{C})$ — then the action preserves $N(\tilde{Q}_-) = \tilde{Q}_-\tilde{Q}^{\natural}_-$: by multiplicativity of the biquaternion norm, $N(\tilde{Q}_+\tilde{Q}_-\tilde{Q}_+^{*}) = N(\tilde{Q}_+)N(\tilde{Q}_-)N(\tilde{Q}_+)^* = N(\tilde{Q}_-)$ when $N(\tilde{Q}_+) = 1$. This is the biquaternion expression of the Lorentz invariance of the Minkowski interval. The condition is on the biquaternion norm and not on $\tilde{Q}_+\tilde{Q}_+^{*}$: a boost biquaternion is Hermitian, so $\tilde{Q}_+\tilde{Q}_+^{*} = \tilde{Q}_+^2 = \cosh\tfrac{\psi}{2} + i\sinh\tfrac{\psi}{2}\,\hat{\mathbf{u}} \neq e_0$, and only the rotation rotors satisfy $\tilde{Q}\tilde{Q}^{*} = e_0$.

**4. The action is a group action.** Compositions of actions compose:

$$
\tilde{Q}_{+2}\bigl(\tilde{Q}_{+1}\tilde{Q}_-\tilde{Q}_{+1}^{*}\bigr)\tilde{Q}_{+2}^{*} = (\tilde{Q}_{+2}\tilde{Q}_{+1})\,\tilde{Q}_-\,(\tilde{Q}_{+2}\tilde{Q}_{+1})^{*}.
$$

### The Structural Relation: Operators and States

The action of $\mathbb{M}_+$ on the four-vector space has the structure of **operators acting on states**:

- The four-vector space is the space of **kinematic configurations** (the four-vectors of position, velocity, momentum, potential, current).
- $\mathbb{M}_+$ is the space of **operators** (the Hermitian biquaternions that act on these configurations).

This is the algebraic content of the reading of $\mathbb{M}_+$ as "informational" (or "operational"): its elements are the things that act, rather than the things that are acted upon. The two roles are not symmetric — one acts, the other is acted upon — and the asymmetry is what earns the sector its name.

### Reversible Versus Irreversible Actions

The elements of $\mathbb{M}_+$ include two important classes.

**Unit-norm elements** ($\tilde{Q}\tilde{Q}^{\natural} = e_0$, i.e. $\tilde{Q} \in SL(2,\mathbb{C})$). These preserve the biquaternion norm and act by **reversible** transformations. Examples: the boost biquaternions $\tilde{\Lambda}$ and the spatial rotation rotors. These correspond to Lorentz transformations. The stronger condition $\tilde{Q}\tilde{Q}^{*} = e_0$ is satisfied by the rotation rotors, which are real quaternions, but not by the boosts.

**Idempotent elements** ($\tilde{Q}^2 = \tilde{Q}$). These do not preserve the biquaternion norm (unless $\tilde{Q} = e_0$). They act by **irreversible** projections: $\tilde{Q}_- \mapsto \tilde{P}\tilde{Q}_-\tilde{P}$. Examples: the pure-state projectors $\tilde\Pi_{1,2}(\hat{\boldsymbol\mu}) = \tfrac{1}{2}(e_0 \pm i\hat{\boldsymbol\mu})$. These correspond to quantum-mechanical measurements.

The **dichotomy between reversible and irreversible actions** is intrinsic to the structure of $\mathbb{M}_+$: it is the biquaternion version of the fundamental dichotomy of quantum information theory between unitary evolution and measurement.

Both ends of the dichotomy have their physics names, and both are owned by later articles, but the statements belong here. The idempotent end is **decoherence**: the irreversible projection of a state onto an idempotent is the algebraic form of a measurement, and the projection onto a minimal left ideal is what a measurement completes. The distinguished projection of the sector is the **vacuum** of a single fermionic mode, the minimal idempotent $\tilde\Pi_1=\tfrac12(e_0+ie_3)$, which is simultaneously a pure state, a rank-one projector and a zero divisor. The two are *Decoherence as Idempotent Projection* and *The Biquaternion Vacuum as a Minimal Idempotent*.

### The Trace Formula

For $\tilde{P} \in \mathbb{M}_+$ idempotent (a state) and $\tilde{Q} \in \mathbb{M}_+$ Hermitian (an observable), the quantity

$$
\langle \tilde{Q} \rangle_{\tilde{P}} = \mathrm{Tr}(\tilde{P}\tilde{Q}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{Q}) = 2\langle\tilde{P},\tilde{Q}\rangle
$$

is **real**. It has the form of a **quantum-mechanical expectation value**: the trace of the product of a state and an observable. For example, if $\tilde{P} = \tfrac{1}{2}(e_0 + i\hat{\boldsymbol\mu})$ and $\tilde{Q} = h_0 e_0 + i\mathbf{h}\cdot\mathbf{e}$, then

$$
\langle \tilde{Q} \rangle_{\tilde{P}} = h_0 + \hat{\boldsymbol\mu}\cdot\mathbf{h},
$$

which is the standard spin-1/2 expectation value along the direction $\hat{\boldsymbol\mu}$. For an idempotent and a state the same pairing is the **probability formula** $p_\pm=\mathrm{Tr}(\tilde\Pi_{1,2}(\hat{\mathbf{n}})\tilde\rho)=\tfrac12(1\pm\hat{\mathbf{n}}\cdot\mathbf{r})$; the derivation of the rule from the algebra, and its comparison with the postulate it replaces, are *The Born Rule as a Trace Formula — Derivation and Comparison*.

What the trace form gives is the probability formula; what it does not give is the identification of those numbers with physical frequencies. The framework relocates the Born rule from a postulate to a property of the pairing; it does not remove the interpretive step. The idea answers the axiomatic status of the Born rule in the structural sense and not in the operational sense, and that separation is stated in the article just cited.

### The Four Forms on the Sector, and the Absence of an Area Pairing

The four forms of *Conventions in the Biquaternion Universe* are read on $\mathbb{M}_+$ in *Remarkable Subspaces and the Four Forms*, and the reading says in one line what the informational sector is not: **the sector carries no area pairing.**

**Every form is real on the sector, so each is its own real part.** An element of $\mathbb{M}_+$ is $a_0e_0 + i\mathbf{p}$ with $a_0$ and $\mathbf{p}$ real, and each of the four forms takes real values on a pair of such elements. The imaginary part of each of the four therefore **vanishes identically on $\mathbb{M}_+$**, and every form is a real symmetric bilinear form in four real variables, recovered from its own diagonal. There is no second, independent pairing on the sector; its whole pairing structure is one symmetric form per form.

**The four forms collapse in pairs, and the defining involution is the reason.** With $\tilde P = c_0e_0 + i\mathbf{q}$ and $\tilde Q = a_0e_0 + i\mathbf{p}$,

$$
\langle\tilde P,\tilde Q\rangle = \langle\tilde P,\tilde Q\rangle_{*} = a_0c_0 + (\mathbf{p},\mathbf{q}), \qquad
\langle\tilde P,\tilde Q\rangle_{\natural} = \langle\tilde P,\tilde Q\rangle_{\natural*} = a_0c_0 - (\mathbf{p},\mathbf{q}).
$$

The first pair is the positive definite form of signature $(4,0)$, the Euclidean square; the second is indefinite of signature $(1,3)$, its one positive direction being the temporal one, and its null cone the sector's light cone. The reason for the collapse is the definition of the sector and nothing else: $\mathbb{M}_+$ is the fixed space of the Hermitian conjugation, so $\tilde Q^{*} = \tilde Q$ on it, and the star being the identity in the second slot is exactly what makes the general plain sesquilinear form equal the general plain bilinear one. This is why the Born pairing of this article needs no second slot on the sector.

**The absence of the area pairing, and why it is exact.** The four forms carry a second real pairing on a subspace only when the multiplication by the central imaginary preserves that subspace: there the imaginary part is generally non-zero and, for the two sesquilinear forms, alternating — the **area pairing**, of rank $2$ on the complex time sector and rank $6$ on the complex space sector. On $\mathbb{M}_+$ the multiplication by $i$ carries the sector out of itself, $i\mathbb{M}_+ = \mathbb{M}_-$, so the companion has no pair of directions to join inside the sector: it is zero, and **the informational sector is a phase-free sector.** Every physical pairing it carries is symmetric — a probability, an interval, a square — and none is an area.

**Two objects that must not be conflated.** The imaginary part meant here is the **scalar-valued** real form $\sigma(\tilde P,\tilde Q) = \mathrm{Im}\,\mathrm{Sc}(\tilde P\tilde Q^{*})$ read off the value of a form. It is not the **vector-valued** antisymmetric half of the sesquilinear **product**, $\mathrm{Vect}(\tilde P\tilde Q^{*})$, which the corpus also reads as a phase and which is **not** zero on the sector: at $\tilde P = \tilde Q = \tilde\rho$ that half is the Bloch vector $\tfrac12 i\mathbf{r}$, and the corpus reads it as the coherence and the interference term (*The Imaginary Part of the Born Pairing: the Antisymmetric Sesquilinear Product*). One block, two parts: the central, scalar part and the vector part. The two statements are therefore complementary and not opposed — **on the informational sector the relative-phase content of a pairing sits in the vector part of the product, while the imaginary part of the scalar form is zero**. The sector carries phase information and carries no area, and the two are carried by different parts of the same block.

The consequence for the reading of this article is one sentence, and it is the reason the statement is worth making here. The informational sector supplies the **symmetric** pairings, the probability $H$ and the Euclidean square among them, and it supplies the operators that act on them; it does not supply an area. The area pairing of the framework — the canonical pairing of two conjugate directions — belongs to the complex time and the complex space sector, where each direction has its partner under the central imaginary (*Other Remarkable Subspaces*), and it vanishes on both physical sectors. The same alternating companion is what the Kähler identity ties to the real part on those two sectors, $\omega(\tilde P,\tilde Q) = \langle\tilde P,i\tilde Q\rangle_{*}$, so that there the probability pairing and the area are one object read twice; on $\mathbb{M}_+$ the identity has no content and the two are simply absent together.

### The Sesqualgebra Behind the Reading

Eight statements of the sections above are not properties of the vector space $\mathbb{M}_+$ alone. Each names an object of a sesqualgebra structure on $\mathbb{B}$ — a product, a form, an involution and the operators they generate — and each is owned, for its own sake, by an article of the mathematical menu. They are collected here so that the physics reading carries the algebraic address of each of its claims.

**1. The Born pairing is the Hilbert–Schmidt pairing.** In the matrix model $\mathbb{B}\cong M_2(\mathbb{C})$ the Hermitian conjugation is the conjugate transpose and the general plain sesquilinear form is the Hilbert–Schmidt form of the matrices, $\langle\tilde Q,\tilde P\rangle_{*}=\tfrac12\operatorname{Tr}\bigl(\Phi(\tilde P)^{\dagger}\Phi(\tilde Q)\bigr)$. With $\tilde\rho$ and $\tilde Q$ Hermitian this reads $\operatorname{Tr}(\Phi(\tilde\rho)\Phi(\tilde Q))=\operatorname{Tr}(\tilde\rho\tilde Q)=2\,\mathrm{Sc}(\tilde\rho\tilde Q)$, so the expectation value of §*The Trace Formula* is a matrix trace in the literal sense and not only in name. The pairing, its Cauchy–Schwarz inequality and the positive functionals it induces are *The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*.

**2. The form makes the algebra a Hilbert space.** The form $\mathrm{Sc}(\tilde R^{*}\tilde S)$ of §*The Hermitian Forms* is positive definite, of signature $(8,0)$ on the real space $\mathbb{B}\cong\mathbb{R}^8$, so $\mathbb{B}$ is a finite-dimensional Hilbert space, the trace formula is continuous in its norm, and the topology the physics uses is the Euclidean one. The completion of the sesqualgebra with respect to that norm is a later and separate construction; nothing above needs it. *Biquaternion Norm and Invertibility*; *The Completion of a Sesqualgebra with a Form*.

**3. The level sets are the groups the physics uses.** Each of the four forms singles out a level set, and the physics reads three of them. The level set of the unit form, $Q^{*}Q=e_0$, is the unitary slice $U(\mathbb{B})\cong U(2)$, the internal unitary group of the evolution. The level set of the norm form, $\langle\tilde Q,\tilde Q\rangle_{\natural}=1$, is the norm-one group $\mathbb{B}^{\times}_{1}$, the Lorentz rotors. The Euclidean sphere $S^{7}$, the level set of the general plain sesquilinear form, is **not** used, and the reason is that the general plain bilinear form is not multiplicative: the witness is the element $e_1+ie_2$, whose Euclidean norm is $\sqrt2$ while $\sum_\mu Q_\mu^{2}=0$, so the sphere contains zero divisors and is not a group at all. *The Four Pairings of the Biquaternion Algebra*; *The Euclidean Topology of the Biquaternion Algebra*.

**4. The operator dictionary is the adjointness dictionary.** Observables are the self-adjoint elements, that is $\mathbb{M}_+$; generators are the skew-adjoint elements, that is $\mathbb{M}_-$; unitaries are the slice of the first item above. This is why the series of mathematical articles is titled "with Hermitian Adjoint": the physical roles are read from the adjoint of one element and nothing else. *Observables, Gauge Generators and the Chirality of the Internal Action*.

**5. One operator carries both evolutions.** The evolution $\tilde\rho\mapsto\tilde\Lambda\tilde\rho\tilde\Lambda^{*}$ and the measurement $\tilde\rho\mapsto\tilde P\tilde\rho\tilde P$ of §*Reversible Versus Irreversible Actions* are the same two-sided operator $\Theta_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{\dagger}}$, the **dagger sandwich**, evaluated at a unitary parameter and at an idempotent one. The reversible–irreversible dichotomy of the physics is therefore the unitary–self-adjoint dichotomy of the operator theory, and no second operator is needed to hold the two. The operator is quadratic in its parameter and its adjoint is linear, which is why the two parameters read differently; *Two-Sided Operators on a Hermitian Algebra with Signed Hermitian Adjoint*.

**6. Projections come from one sector only.** A measurement projection is an idempotent, and no nonzero idempotent lies in $\mathbb{M}_-$: if $\tilde P^{2}=\tilde P$ and $\tilde P^{*}=-\tilde P$, then applying the anti-automorphism to the first relation gives $-\tilde P=(\tilde P^{*})^{2}=(-\tilde P)^{2}=\tilde P^{2}=\tilde P$, whence $\tilde P=0$. The material sector therefore owns no projector, and the Peirce decomposition of a measurement runs through $\mathbb{M}_+$ alone. *Hermitian Idempotents and the Peirce Decomposition*.

**7. Two pairings, because one of them is not Hermitian.** The Lorentzian interval on $\mathbb{M}_-$ is the quaternion **bilinear** form $N=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)$ of *Mass, Rank and the Positivity of the Dagger*, the second slot without the star, of signature $(-,+,+,+)$ on the four real directions $ict\,e_0,\mathbf{x}$. It is excluded from the Witt classification of Hermitian forms for exactly one reason: it is not Hermitian for the dagger, being complex-valued, indefinite and isotropic on the null cone, and the two types of form must not be placed in the same classification. The framework therefore needs two pairings and not one — $H=\mathrm{Sc}(\tilde P\tilde Q^{*})$ for probability, $N$ for the metric — and on each sector the two agree up to sign, $\langle\tilde P,\tilde Q\rangle_{*}=\pm\langle\tilde P,\tilde Q\rangle$ and $\langle\tilde P,\tilde Q\rangle_{\natural*}=\pm\langle\tilde P,\tilde Q\rangle_{\natural}$, with $+$ on $\mathbb{M}_+$ and $-$ on $\mathbb{M}_-$. The relation was checked on $200$ random elements of each sector and holds identically, the sign being the only difference. *The Four Pairings of the Biquaternion Algebra*; *Hermitian Forms over the Biquaternion Algebra and the Unitary Witt Group with Hermitian Adjoint*.

**8. The two pairings have no alternating companion on the sector.** §*The Four Forms on the Sector, and the Absence of an Area Pairing*: the four forms restricted to $\mathbb{M}_+$ are real-valued, so their imaginary parts vanish and the sector carries no alternating companion and no conjugate pair of its own, since $i\mathbb{M}_+=\mathbb{M}_-$; every canonical pair of the framework has one leg in each sector, the two times $e_0$ and $ie_0$ in the complex time sector and the three spatial pairs $(e_k,ie_k)$ in the complex space sector (*Other Remarkable Subspaces*). The statement is a property of the restriction of a form to a subspace and of where the multiplication by the central imaginary closes, and it is owned, for the remarkable subspaces at once, by *Remarkable Subspaces and the Four Forms* — with the four forms themselves, their two slots and their four names in *The 4 Forms over the Biquaternion $\mathbb{C}$ Space* and the convention of the four pairings in *Conventions in the Biquaternion Universe*.

### The Spectral Decomposition

Every Hermitian element has a spectrum read off in closed form. Write $\tilde{Q} = h_0e_0 + i\mathbf{h}$ with $h_0$ real and $\mathbf{h}$ a real vector, and let $\hat{\mathbf{h}} = \mathbf{h}/|\mathbf{h}|$ for $\mathbf{h}\neq0$. Then

$$
\tilde{Q} = \left(h_0 + |\mathbf{h}|\right)\tilde\Pi_1(\hat{\mathbf{h}}) + \left(h_0 - |\mathbf{h}|\right)\tilde\Pi_2(\hat{\mathbf{h}}),
$$

with the two idempotents of §*The Idempotents* along the axis $\hat{\mathbf{h}}$. The two coefficients are the **eigenvalues**,

$$
\lambda_\pm = h_0 \pm |\mathbf{h}|,
$$

real, and the two idempotents are the **eigenprojectors**, $\tilde{Q}\tilde\Pi_{1,2} = \lambda_\pm\tilde\Pi_{1,2}$. Because $\tilde\Pi_1 + \tilde\Pi_2 = e_0$ and $\tilde\Pi_1\tilde\Pi_2 = 0$, the pair is a resolution of the identity, and the formula is a genuine spectral decomposition: every Hermitian element of $\mathbb{M}_+$ is a real combination of two orthogonal idempotents, and the decomposition degenerates to $h_0$ alone exactly when $\mathbf{h} = 0$. The trace and the biquaternion norm read

$$
\mathrm{Tr}(\tilde{Q}) = 2h_0 = \lambda_+ + \lambda_-, \qquad N(\tilde{Q}) = h_0^2 - |\mathbf{h}|^2 = \lambda_+\lambda_-,
$$

so the norm is **indefinite**: it is negative exactly when the two eigenvalues have opposite signs. This is the difference from the ordinary Hermitian matrix case, where the analogous form $\mathrm{Tr}(H^2)$ is a sum of squares. Here positivity is a statement about the **eigenvalues** $h_0 \pm |\mathbf{h}|$, not about the biquaternion norm.

### The Positive Cone and the Bloch Ball

An element $\tilde{Q} \in \mathbb{M}_+$ is **positive** when it is $\tilde{R}^{*}\tilde{R}$ for some $\tilde{R}$, equivalently when its spectrum lies in $[0,\infty)$, equivalently, by the decomposition above, when $h_0 \geq |\mathbf{h}|$. The positive elements form a cone with apex at the origin, and its interior is the set of Hermitian elements with strictly positive spectrum. The one-parameter family through the identity is the **trace-one slice**: with $\tilde\rho = \tfrac{1}{2}(e_0 + i\mathbf{r})$ one has $\mathrm{Tr}(\tilde\rho) = 1$, and writing $\mathbf{r} = r\hat{\boldsymbol\mu}$ the spectral decomposition gives

$$
\tilde\rho = \frac{1+r}{2}\,\tilde\Pi_1(\hat{\boldsymbol\mu}) + \frac{1-r}{2}\,\tilde\Pi_2(\hat{\boldsymbol\mu}),
$$

so **$\tilde\rho$ is positive exactly when $|\mathbf{r}| \leq 1$**. This is an iff, and its two ends are the two ends of the ball:

- $|\mathbf{r}| = 1$: one eigenvalue is $1$ and the other $0$, the element is an idempotent $\tilde\Pi_{1,2}(\hat{\boldsymbol\mu})$, a **pure state**; these points are the two-sphere of §*The Idempotents*.
- $|\mathbf{r}| = 0$: $\tilde\rho = \tfrac{1}{2}e_0$, the **maximally mixed** state.

The intermediate values $0 < |\mathbf{r}| < 1$ are the **mixed states**, and the whole set is the **Bloch ball**, the unit ball of the three-dimensional real vector part. The convexity is manifest in the formula: $\tilde\rho$ is a convex combination of two orthogonal idempotents with weights $(1\pm r)/2$, which sum to $1$. The pure states form the boundary sphere and the mixed states the interior, so that a state is pure exactly when it is idempotent — the two notions coincide in the sector and nowhere else. Because $\mathbb{M}_+$ is a real vector space of dimension $4$ and the trace-one condition is one real equation, the state space is three-dimensional, as it must be for a two-state system.

Positivity is not preserved by the biquaternion norm: the mixed state $\tilde\rho$ has $N(\tilde\rho) = \tfrac{1}{4}(1 - r^2) \geq 0$, which vanishes on the whole boundary sphere rather than at a point. Every pure state is therefore a **zero divisor**, in agreement with §*Properties*.

One structural fact joins the ball to the material sector and is stated here rather than only in its own article: the ball is the intersection of the affine hyperplane $\{\mathrm{Sc}=\tfrac12\}$ of $\mathbb{M}_+$ with the **future light cone** of the biquaternion norm. The positivity of the probability form and the causal cone of the interval therefore have one and the same boundary, and the state space of the frame is a slice of the cone that carries its causality. The geometry is *The Bloch Ball as the Trace-One Slice of the Future Light Cone*.

### The Bracket Table of the Two Sectors

The two sectors are not closed under the product in a haphazard way; the antisymmetric and the symmetric parts go to opposite sectors, and the rule is uniform. Write $[\tilde{Q},\tilde{R}] = \tilde{Q}\tilde{R} - \tilde{R}\tilde{Q}$ and $\{\tilde{Q},\tilde{R}\} = \tilde{Q}\tilde{R} + \tilde{R}\tilde{Q}$. Then the sector of the result is determined by the sectors of the two arguments:

| bracket | $\mathbb{M}_+,\mathbb{M}_+$ | $\mathbb{M}_+,\mathbb{M}_-$ | $\mathbb{M}_-,\mathbb{M}_-$ |
|---|---|---|---|
| commutator $[\tilde{Q},\tilde{R}]$ | $\mathbb{M}_-$ | $\mathbb{M}_+$ | $\mathbb{M}_-$ |
| anticommutator $\{\tilde{Q},\tilde{R}\}$ | $\mathbb{M}_+$ | $\mathbb{M}_-$ | $\mathbb{M}_+$ |

In coordinates the rule is transparent. For two Hermitian elements $\tilde{Q} = q_0e_0 + i\mathbf{u}$ and $\tilde{R} = r_0e_0 + i\mathbf{v}$ the product rule of §*Definition and Basis* gives

$$
[\tilde{Q},\tilde{R}] = -2\,\mathbf{u}\times\mathbf{v} \in \mathbb{M}_-, \qquad \{\tilde{Q},\tilde{R}\} = 2\left(q_0r_0 + (\mathbf{u},\mathbf{v})\right)e_0 + 2i\left(q_0\mathbf{v} + r_0\mathbf{u}\right) \in \mathbb{M}_+,
$$

and for two anti-Hermitian elements $\tilde{Q} = iq'_0e_0 + \mathbf{q}$, $\tilde{R} = ir'_0e_0 + \mathbf{r}$ the same computation gives

$$
[\tilde{Q},\tilde{R}] = 2\,\mathbf{q}\times\mathbf{r} \in \mathbb{M}_-, \qquad \{\tilde{Q},\tilde{R}\} \in \mathbb{M}_+.
$$

The reason for the alternation is that ${}^{*}$ is an **anti**-automorphism: $(\tilde{Q}\tilde{R})^{*} = \tilde{R}^{*}\tilde{Q}^{*}$, so the sign of the involution on a product is the product of the two signs, and the antisymmetric part collects the difference while the symmetric part collects the sum. Read on the sectors, the rule is fixed by whether the two arguments share a sector: on two elements of **one** sector the commutator lands in $\mathbb{M}_-$ and the anticommutator in $\mathbb{M}_+$, while on two elements of **different** sectors the two are exchanged. The commutator and the anticommutator therefore always land in **opposite** sectors. Two consequences:

- The two sectors are closed under **different** brackets, and neither is closed under both. The anticommutator closes on $\mathbb{M}_+$, which is therefore a **special Jordan algebra** under the symmetrised product; the commutator closes on $\mathbb{M}_-$ and not on $\mathbb{M}_+$. The **square** of an element of either sector nevertheless lies in $\mathbb{M}_+$, because $\{Q,Q\} = 2Q^2$ and the two arguments of the anticommutator then lie in one sector; this is the structural fact behind the square formula of §*Definition and Basis*, and it is the reason a square can never witness the failure of closure.
- The material sector is a **Lie algebra** under the commutator; the informational sector is not, its bracket landing in the other sector. The asymmetry between "the sector that carries the brackets" and "the sector that carries the states" is algebraic, not interpretive, and it is the precise sense in which the two sectors have different characters.

### The Algebraic Identification with Quantum Information

The mathematics of $\mathbb{M}_+$ and its action on $\mathbb{M}_-$ is **structurally identical** to the mathematics of quantum information theory for a single qubit. This is an algebraic fact, established in detail in the companion article *Quantum Physics in Biquaternionic Form*.

### The Correspondence

| Quantum information | Biquaternion framework |
|---|---|
| State space $\mathbb{C}^2$ | Spinor module of $\mathbb{B}$ |
| Basis of the state space | $\{\tilde{\Pi}_1,\tilde{T}\}$: one idempotent and one nilpotent, Gram matrix $\tfrac{1}{2}I_2$ |
| Density matrix $\rho$ (Hermitian, positive, trace 1) | Element $\tilde{\rho} \in \mathbb{M}_+$ (Hermitian, positive, trace 1) |
| Pure state $\lvert\psi\rangle\langle\psi\rvert$ | Idempotent $\tfrac{1}{2}(e_0 + i\hat{\boldsymbol\mu})$ |
| Observable (Hermitian operator) | Hermitian element $\tilde{Q} \in \mathbb{M}_+$ |
| Unitary gate $U$ | Unit-norm element $\tilde{\Lambda}$ with $\tilde{\Lambda}\tilde{\Lambda}^{*} = e_0$: a rotation rotor, the $SU(2)$ of the real quaternions. The general unit-norm element of $SL(2,\mathbb{C})$ also carries the boosts, which are Hermitian and not unitary |
| Expectation value $\mathrm{Tr}(\rho H)$ | Trace formula $2\,\mathrm{Sc}(\tilde{\rho}\tilde{Q})$ |
| Reversible evolution $U\rho U^\dagger$ | Rotor conjugation $\tilde{\Lambda}\tilde{\rho}\tilde{\Lambda}^{*}$ |
| Projective measurement $\rho \mapsto P\rho P$ | Idempotent projection $\tilde{\rho} \mapsto \tilde{P}\tilde{\rho}\tilde{P}$ |

The correspondence is not an analogy. **It is the same mathematics**, expressed in two different notations: the Hermitian elements of the algebra are the operators of a two-state system.

The state space in the right-hand column is the spinor module $S=\mathbb{B}\tilde{\Pi}_1=\mathbb{C}\{\tilde{\Pi}_1,\tilde{T}\}$ of *Particle Types, Discrete Charge and Three-Particle Couplings*, spanned by the idempotent $\tilde{\Pi}_1=\tfrac12(e_0+ie_3)$ and the **nilpotent** $\tilde{T}=\tfrac12(ie_1+e_2)$. The distinction of the two is what the table means by a basis: $\tilde{\Pi}_1^{2}=\tilde{\Pi}_1$, while $\tilde{T}^{2}=0$ and $\tilde{T}^{*}=\tfrac12(ie_1-e_2)\neq\tilde{T}$, so $\tilde{T}$ is **not** a state — it is the off-diagonal half of the Peirce decomposition. A general spinor is the pair $s_1\tilde{\Pi}_1+s_2\tilde{T}$ of complex coefficients, the Born pairing restricted to the module has Gram matrix $\tfrac12 I_2$, and $\langle\psi,\psi\rangle_{*}=\tfrac12(\lvert s_1\rvert^{2}+\lvert s_2\rvert^{2})$ is positive definite. The two states of the two-state system are carried by the two **coefficients**, as in $\mathbb{C}^2$, and not by the two basis elements; the module is a genuine Hilbert space, and not the isotropic module that a general Clifford algebra can present.

### What the Correspondence Is and Is Not

**What it is:** A structural fact about the algebra. The elements of $\mathbb{M}_+$ are Hermitian operators on the spinor module of $\mathbb{B}$, and the algebra they generate is the algebra of observables of a two-state system. The mathematics of quantum information applies to $\mathbb{M}_+$ as it applies to any such algebra.

**What it is not (yet):** A physical theory. The structural correspondence does not by itself establish that $\mathbb{M}_+$ **is** an informational sector of physics. It establishes that if $\mathbb{M}_+$ were given an informational interpretation, the mathematics would be available. Whether the interpretation is realised in nature is a separate question.

### The Spin Analogy

The correspondence with quantum information is closely related to the **spin-1/2 formalism** of non-relativistic quantum physics.

- In spin-1/2 quantum physics, the state space is $\mathbb{C}^2$, and the observables are the Pauli matrices $\sigma_k$ generating $\mathrm{SU}(2)$. The rotation group $SU(2)$ acts on the states.
- In the biquaternion framework, the spinor module of $\mathbb{B}$ is the state space, and the Hermitian elements of $\mathbb{M}_+$ are the observables. The action is by rotor conjugation on the module.

The difference is:

- In spin-1/2, the operators generate the **compact** group $SU(2)$ (rotations).
- In $\mathbb{M}_+$, the Hermitian elements are a **real four-dimensional space and not a group**: exponentiated, the traceless ones $i\mathbf{h}$ with $\mathbf{h}$ real give the **non-compact** boosts of $SL(2,\mathbb{C})$, and the central one $h_0e_0$ gives a dilation, $e^{h_0}e_0$, which is not of unit norm. Their products with the rotation rotors — the unit-norm *anti*-Hermitian elements $\exp(\theta\hat{\mathbf{u}})$ — generate all of $SL(2,\mathbb{C})$.

The compact/non-compact distinction reflects the difference between rotations in a spacelike plane (compact) and boosts in a timelike plane (non-compact). The biquaternion framework extends the spin-1/2 structure to the relativistic setting: the observables include the boost generators $i\mathbf{h}$ alongside the rotation generators, so the group they act in is the Lorentz group rather than the rotation group.

The biquaternion framework can therefore be read as a **relativistic generalisation of the spin-1/2 formalism**, in which the state space is the spinor module of $\mathbb{B}$ and the symmetry group is the Lorentz group.

The three operations of the correspondence are one formula. The conjugation $\Gamma_{\tilde A}(\tilde Q)=\tilde A\tilde Q\tilde A^{*}$ is the Lorentz rotor when $\tilde A$ has unit biquaternion norm, the reversible evolution when $\tilde A$ is a unitary element of the slice, and the measurement update when $\tilde A$ is an idempotent; the three cases differ in the normalisation condition imposed on the parameter and not in the operation performed.

The formula is relativistic at its source, but the single-qubit formalism is not: its state space is a fixed Bloch ball $|\mathbf{r}|\leq1$, and a boost carries a trace-one element **off** the trace-one slice. Making the state space itself relativistic, and not only the transformation group, is open work and not a result of the framework. The relativistic state space is *The Relativistic Qubit in Biquaternionic Form*, and the difficulty is the second of the seven of *The Quantum–Relativity Tension and the Biquaternion Framework*.

## Examples

The companion articles already contain several distinguished elements of $\mathbb{M}_+$. It is worth collecting them, because they are the natural candidates for the objects of the informational sector.

### The Boost Biquaternion

The **boost biquaternion**

$$
\tilde{\Lambda} = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\,\hat{\mathbf{u}}, \qquad \hat{\mathbf{u}}^2 = -e_0,
$$

lies in $\mathbb{M}_+$: its scalar part $\cosh(\psi/2)$ is real, and its vector part $i\sinh(\psi/2)\hat{\mathbf{u}}$ is purely imaginary. It is Hermitian ($\tilde{\Lambda}^{*} = \tilde{\Lambda}$) and has unit norm ($\tilde{\Lambda}\tilde{\Lambda}^{\natural} = e_0$). It acts on $\mathbb{M}_-$ by rotor conjugation, implementing a Lorentz boost.

The boost biquaternion is a distinguished element of $\mathbb{M}_+$, and it is the **prototype** of an operator acting on the material sector $\mathbb{M}_-$. More generally, every unit-norm biquaternion $\tilde{\Lambda} \in \mathbb{B}$ acts on $\mathbb{M}_-$ by rotor conjugation $\tilde{Q} \mapsto \tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{*}$. For pure boosts, $\tilde{\Lambda}$ lies in $\mathbb{M}_+$. For pure spatial rotations, $\tilde{\Lambda}$ lies in $\mathbb{H}_{\mathbb{B}}$. For general Lorentz transformations, $\tilde{\Lambda}$ is a general unit-norm biquaternion in $\mathbb{B}$. The point is that the action of any such rotor on $\mathbb{M}_-$ preserves $\mathbb{M}_-$.

### The Idempotents

The **idempotents** of $\mathbb{B}$ of the form

$$
\tilde\Pi_{1,2}(\hat{\boldsymbol\mu}) = \tfrac{1}{2}\left(e_0 \pm i\hat{\boldsymbol\mu}\right), \qquad \hat{\boldsymbol\mu}^2 = -e_0, \; \hat{\boldsymbol\mu} \text{ a real unit pure quaternion},
$$

lie in $\mathbb{M}_+$: their scalar part $\tfrac{1}{2}$ is real, and their vector part $\pm \tfrac{1}{2} i \hat{\boldsymbol\mu}$ is purely imaginary. They satisfy:

- **Hermitian:** $\tilde\Pi_{1,2}^{*} = \tilde\Pi_{1,2}$, since $\tilde\Pi_{1,2}(\hat{\boldsymbol\mu}) \in \mathbb{M}_+$.
- **Idempotent:** $\tilde\Pi_{1,2}^2 = \tilde\Pi_{1,2}$.
- **Unit trace:** $\mathrm{Tr}(\tilde\Pi_{1,2}) = 2\,\mathrm{Sc}(\tilde\Pi_{1,2}) = 1$.

These are the biquaternion analogues of **pure-state density matrices** of quantum physics. They are the natural "states" of the informational sector.

**Why they are idempotent.** The single fact behind the whole family is the sign

$$
(i\hat{\boldsymbol\mu})^2 = i^2\,\hat{\boldsymbol\mu}^2 = (-1)(-e_0) = +e_0,
$$

which is the opposite of the material sector's $\mathbf{q}^2 = -|\mathbf{q}|^2e_0$ for a real vector $\mathbf{q}$. With it,

$$
\tilde\Pi_{1,2}^2 = \tfrac{1}{4}\left(e_0 \pm 2i\hat{\boldsymbol\mu} + (i\hat{\boldsymbol\mu})^2\right) = \tfrac{1}{4}\left(e_0 \pm 2i\hat{\boldsymbol\mu} + e_0\right) = \tilde\Pi_{1,2} .
$$

The two minus signs cancel: the minus from $i^2$ and the minus from the square of a real vector. In the material sector there is only the second of them, so the corresponding combination is not idempotent — $\tfrac{1}{2}(e_0 + \mathbf{q})$ fails, and indeed $\mathbb{M}_-$ contains no nontrivial idempotent at all. This one sign is why the idempotents, the positive cone and the spectral decomposition all live in $\mathbb{M}_+$ and not in $\mathbb{M}_-$.

**Orthogonality and completeness.** The two idempotents along one axis are complementary and orthogonal,

$$
\tilde\Pi_1(\hat{\boldsymbol\mu}) + \tilde\Pi_2(\hat{\boldsymbol\mu}) = e_0, \qquad \tilde\Pi_1(\hat{\boldsymbol\mu})\,\tilde\Pi_2(\hat{\boldsymbol\mu}) = \tilde\Pi_2\tilde\Pi_1 = 0,
$$

because $\tfrac{1}{4}\left(e_0 + i\hat{\boldsymbol\mu}\right)\left(e_0 - i\hat{\boldsymbol\mu}\right) = \tfrac{1}{4}\left(e_0 - (i\hat{\boldsymbol\mu})^2\right) = 0$. The pair is a **complete orthogonal pair**, a frame of the algebra, and it is what the spectral decomposition of §*The Spectral Decomposition* is written in.

**Every pure state is a zero divisor.** The biquaternion norm of the idempotent vanishes identically on the sphere,

$$
N\!\left(\tilde\Pi_{1,2}(\hat{\boldsymbol\mu})\right) = \tfrac{1}{4}\left(e_0 - (i\hat{\boldsymbol\mu})^2\right) = \tfrac{1}{4}\left(e_0 - e_0\right) = 0,
$$

as the product $\tilde\Pi_1\tilde\Pi_2 = 0$ already witnesses with both factors nonzero. So the pure states sit on the zero-divisor cone, while a general mixed state does not: the norm is $N(\tilde\rho) = \tfrac{1}{4}(1 - r^2)$ for $\tilde\rho = \tfrac{1}{2}(e_0 + i\mathbf{r})$.

### The Hermitian Forms

For any biquaternion $\tilde{Q} \in \mathbb{B}$, the **Hermitian form**

$$
\tilde{Q}\tilde{Q}^{*}
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
| Idempotent $\tilde\Pi_{1,2}(\hat{\boldsymbol\mu})$ | Hermitian, idempotent, trace 1 | Pure state / projector |
| Mixed state $\tilde\rho = \tfrac{1}{2}(e_0 + i\mathbf{r})$, $|\mathbf{r}| \leq 1$ | Hermitian, positive, trace 1 | Density matrix (Bloch ball) |
| Observable $\tilde{Q} = h_0e_0 + i\mathbf{h}$ | Hermitian, eigenvalues $h_0 \pm |\mathbf{h}|$ | Observable with spectral decomposition |
| Hermitian form $\tilde{Q}\tilde{Q}^{*}$ | Hermitian, positive scalar part | Weight of a state |

The common feature of these objects is that they are **Hermitian** (fixed under ${}^{*}$). This is what defines membership in $\mathbb{M}_+$.

## Physical Readings

The informational sector reads as the state space, as the carrier of the informational time and as one half of a clock. The state-space reading is the article's own: the idempotents are the pure states, the Bloch ball is the mixtures and the positive sesquilinear form is the probability. The temporal reading is that the real scalar coefficient $ct'$ is the informational projection of the central coordinate $z = ct' + i\,ct$, so an element of $\mathbb{M}_+$ carries one projection of the clock and its partner in $\mathbb{M}_-$ carries the other (*Each Sector Is the Other's Clock: the Sector Exchange as Relational Time*).

Two further readings of the state space can be named. Read as **quantum logic**, the idempotents of $\mathbb{M}_+$ are the sharp effects and the partial order of effects makes the sector an effect algebra, and its failure to be a Boolean lattice is the framework's form of contextuality, the obstruction appearing at two qubits and not in the two-dimensional module (*Effect Algebras and Orthomodular Lattices*, *Contextuality and the Kochen–Specker Theorem in Biquaternionic Form*). Read as **information geometry**, the positive sesquilinear form induces a statistical distance on the states — the Fubini–Study metric on the boundary of the ball and the Bures metric inside it — and the Fisher information of a measurement is the same form read on a family of states, so the sector carries a metric on states as well as a probability (*The Fubini–Study Geometry and the Biquaternion Norm*, *Fisher Information and the Biquaternion Norm*). Boundary: both readings are of the state space as it is; neither adds a measurement postulate, and the identification of the probabilities with frequencies remains the corpus's standing interpretive step.

## Summary

The Hermitian subspace $\mathbb{M}_+$ is a four-dimensional real subspace of the biquaternion algebra, consisting of elements with real scalar part and imaginary vector part. Its biquaternion norm has signature $(1,3)$, the temporal direction being the single positive one. It contains the identity, the boost biquaternions, the idempotents $\tilde\Pi_{1,2}(\hat{\boldsymbol\mu}) = \tfrac{1}{2}(e_0 \pm i\hat{\boldsymbol\mu})$, and the Hermitian forms $\tilde{Q}\tilde{Q}^{*}$.

The elements of $\mathbb{M}_+$ act on the material space $\mathbb{M}_-$ by conjugation: $\tilde{Q}_- \mapsto \tilde{Q}_+\tilde{Q}_-\,\tilde{Q}_+^{*}$. The action is linear, preserves $\mathbb{M}_-$, and preserves the biquaternion norm when $\tilde{Q}_+$ has unit norm. The natural dichotomy between unit-norm and idempotent elements corresponds to the dichotomy between reversible evolution and irreversible measurement, the idempotent end being the decoherence of a measurement and the minimal idempotent $\tilde\Pi_1=\tfrac12(e_0+ie_3)$ the vacuum of a single fermionic mode.

Two further structures are carried by the sector and are developed above. Every Hermitian element has a **spectral decomposition** $\tilde{Q} = (h_0 + |\mathbf{h}|)\tilde\Pi_1(\hat{\mathbf{h}}) + (h_0 - |\mathbf{h}|)\tilde\Pi_2(\hat{\mathbf{h}})$ into two orthogonal idempotents, with real eigenvalues $h_0 \pm |\mathbf{h}|$, and the **positive elements** are those with $h_0 \geq |\mathbf{h}|$. On the trace-one slice the positive elements are exactly the $\tilde\rho = \tfrac{1}{2}(e_0 + i\mathbf{r})$ with $|\mathbf{r}| \leq 1$, the **Bloch ball**: the boundary sphere is the pure states, the interior the mixed states, and the centre the maximally mixed state. The whole family rests on one sign, $(i\hat{\boldsymbol\mu})^2 = +e_0$, which is what makes a Hermitian vector square to $+1$ and the corresponding combination idempotent.

The product of two elements of one sector is governed by a single rule: the two brackets always land in **opposite** sectors — on two elements of one sector the **commutator** lands in $\mathbb{M}_-$ and the **anticommutator** in $\mathbb{M}_+$, and on two elements of different sectors the two are exchanged — since ${}^{*}$ is an anti-automorphism. $\mathbb{M}_+$ is therefore a Jordan algebra for the anticommutator and $\mathbb{M}_-$ a Lie algebra for the commutator, and neither sector is closed under the other bracket. The square of an element of either sector always lies in $\mathbb{M}_+$, which is why a square can never witness the failure of closure.

A third structure is the **absence** of one. Read as pairings, the four forms restricted to $\mathbb{M}_+$ are all real-valued, so the sector carries **no area pairing and no conjugate pair of its own**: no two of its directions are exchanged by the central imaginary, and its pairings are symmetric, the probability $H$ and the Euclidean square of signature $(4,0)$, together with the interval $N$ of signature $(1,3)$, and the two sesquilinear forms coincide with the two bilinear ones because the Hermitian conjugation fixes the sector pointwise. The alternating companion that the four forms carry on the complex time and the complex space sector is identically zero here, and the same holds on the material sector: **the two physical sectors are the phase-free ones, and the area pairing belongs to the complex sectors** (*Remarkable Subspaces and the Four Forms*, *Other Remarkable Subspaces*).

The mathematics of $\mathbb{M}_+$ is structurally identical to the mathematics of quantum information theory for a two-state system. The idempotents are pure-state density matrices, the Hermitian elements are observables, the unitary elements are gates, and the trace formula $\mathrm{Tr}(\tilde{P}\tilde{Q}) = 2\mathrm{Sc}(\tilde{P}\tilde{Q}) = 2\langle\tilde{P},\tilde{Q}\rangle$ is the Born rule. The structural correspondence is not an analogy: it is the same mathematics, expressed in the biquaternion algebra.

The **physical hypothesis** is that this mathematics reflects physics: that $\mathbb{M}_+$ is not only a mathematical structure but an **informational sector** of the world, physically realised in the same sense as the material sector. The hypothesis is offered as a research program. The mathematical structure is established; the empirical content is not yet specified. The article closes with the open questions that constitute the agenda for developing the hypothesis into a physical theory.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\mathbb{M}_+$ | Hermitian subspace (informational sector): real scalar, imaginary vector; parameters $q_0, q'_1, q'_2, q'_3$, with $q_0 = ct'$ |
| $Q_\mu = q_\mu + iq'_\mu$ | Complex coefficient of $e_\mu$: $q_\mu$ its real part, $q'_\mu$ its imaginary part |
| $\tilde{Q} = q_0e_0 + iq'_ke_k = (ct')\,e_0 + i\mathbf{x}'$ | Informational element, both writings; $q_0 = ct'$, $q'_k = x'_k$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $N(\tilde{Q}) = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural}$ | Biquaternion norm |
| $\tilde{\Lambda} \in \mathbb{B}$, $\tilde{\Lambda}\tilde{\Lambda}^{\natural} = e_0$ | Lorentz rotor (unit-norm biquaternion) |
| $\tilde\Pi_{1,2}(\hat{\boldsymbol\mu}) = \tfrac{1}{2}(e_0 \pm i\hat{\boldsymbol\mu})$ | Idempotent (pure-state projector) of unit trace |
| $\tilde\rho = \tfrac{1}{2}(e_0 + i\mathbf{r})$, $|\mathbf{r}| \leq 1$ | Density matrix (Bloch ball); $\mathbf{r}$ the Bloch vector |
| $\lambda_\pm = h_0 \pm |\mathbf{h}|$ | Eigenvalues of the Hermitian element $h_0e_0 + i\mathbf{h}$ |
| $[\tilde{Q},\tilde{R}]$, $\{\tilde{Q},\tilde{R}\}$ | Commutator and anticommutator; the two always land in opposite sectors — on two elements of one sector the first in $\mathbb{M}_-$ and the second in $\mathbb{M}_+$, exchanged on two elements of different sectors |
| $\tilde{Q}$ | General Hermitian element (observable) |
| $\tilde{Q}_- \mapsto \tilde{Q}_+\tilde{Q}_-\,\tilde{Q}_+^{*}$ | Conjugation action of $\mathbb{M}_+$ on $\mathbb{M}_-$ |
| $\tilde{Q}_+$, $\tilde{Q}_-$ | Hermitian element of $\mathbb{M}_+$ (operator) and anti-Hermitian element of $\mathbb{M}_-$ (acted upon); written $\tilde{Q}$ when only one element is in play |
| $\mathrm{Tr}(\tilde{P}\tilde{Q}) = 2\mathrm{Sc}(\tilde{P}\tilde{Q}) = 2\langle\tilde{P},\tilde{Q}\rangle$ | Trace formula (Born rule) |
| $SL(2,\mathbb{C})$ | Group of unit-norm biquaternions |
| $\langle\tilde{P},\tilde{Q}\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{P}\tilde{Q}^{*})$; on the diagonal $\langle\tilde{Q},\tilde{Q}\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$ |
| the four forms | $B=\mathrm{Sc}(\tilde P\tilde Q)$, $N=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)$, $H=\mathrm{Sc}(\tilde P\tilde Q^{*})$, $K=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})$; on $\mathbb{M}_+$ all four are real, with $H=B$ and $K=N$ |
| the area pairing | The alternating companion of the four forms; **zero** on $\mathbb{M}_+$, non-degenerate on the complex time and the complex space sector |

## Further Reading

- John von Neumann, *Mathematical Foundations of Quantum Mechanics* (Princeton, 1932), for the original formulation of quantum physics in terms of Hermitian operators and density matrices.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the standard treatment of qubits, gates, and measurements.
- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford, 1930), for the spin-1/2 formalism.
- Roger Penrose, *The Road to Reality* (Knopf, 2004), for the complex structure of quantum physics and its relation to spacetime.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the geometric algebra formulation of quantum physics.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the modern geometric algebra treatment of spinors and operators.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the algebraic structure of the Clifford algebra $\mathrm{Cl}_{1,3}$.
- Asher Peres, *Quantum Theory: Concepts and Methods* (Kluwer, 1993), for the operational reading of states, observables, and measurements used here.
- *Conventions in the Biquaternion Universe* and *Relations Between Subspaces*, the companion articles, for the notation and for the place of $\mathbb{M}_+$ among the remarkable subspaces.
- Within the corpus, the structures used above are developed for their own sake in *Biquaternion Spectral Theory* (the spectral decomposition and the eigenvalues $Q_0 \pm iB$), *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint* (the positive cone and the trace-one slice), *Hermitian Idempotents and the Peirce Decomposition* (the idempotents), *The 12 Products of the Biquaternion Complex Space* (the bracket table, the $\mathbb{Z}/2$-grading of the two sectors and the symmetrised product), and the product rule of the remarkable subspaces is *Remarkable Subspaces and the Four General Products*.
- The sesqualgebra side of §*The Sesqualgebra Behind the Reading* is *The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (the Hilbert–Schmidt pairing) and *Two-Sided Operators on a Hermitian Algebra with Signed Hermitian Adjoint* (the dagger sandwich of the evolution and the measurement).
- The forms and the topology of the same section are *The Four Pairings of the Biquaternion Algebra* (the four forms, their Gram matrices, their signatures, the level sets and the isometry groups) and *Biquaternion Norm and Invertibility* (the zero divisors of $N$).
- The four forms read on the sector itself — their real and imaginary parts, the collapse of the four into two and the vanishing of the alternating companion — are *Remarkable Subspaces and the Four Forms*; the two sectors on which the alternating companion is instead non-degenerate are *Other Remarkable Subspaces*.
- The two pairings and the exclusion of the norm form from the Witt theory are *Hermitian Forms over the Biquaternion Algebra and the Unitary Witt Group with Hermitian Adjoint*, and the analytic completion is *The Completion of a Sesqualgebra with a Form*.

