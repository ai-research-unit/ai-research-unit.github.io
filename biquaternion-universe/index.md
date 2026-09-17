
# __Complexified Spacetime with a Local Complex Structure__

## Core Proposal

The fundamental structure of the universe is a biquaternion space, of which Minkowski space is one real slice. A point in this complexified spacetime is an element of the **biquaternion algebra** $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$, written as a biquaternionic coordinate

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3,
$$

where $e_0 = 1$ and $e_1, e_2, e_3$ are the quaternion units. The four coefficients $Q_\mu$ are complex numbers, and they split naturally into two sectors, as described below. The complex structure — the identification of which direction is "real" and which is "imaginary" — is **local**, determined by the electromagnetic properties of the medium at each point.

The hypothesis of this blog is that this biquaternionic structure is the natural language in which the fundamental structures of physics are written, and that the fact that the framework contains both relativity and quantum mechanics is evidence for the proposal.

## Two Sectors: Material and Informational

The biquaternion algebra splits naturally into two complementary four-dimensional real subspaces:

$$
\mathbb{B} = \mathbb{M}_- \oplus \mathbb{M}_+.
$$

The subspace $\mathbb{M}_-$ is the **anti-Hermitian subspace**, the fixed-point set of the anti-Hermitian conjugation $\flat$ (equivalently, the eigenspace of the Hermitian conjugation $\dagger$ with eigenvalue $-1$). The subspace $\mathbb{M}_+$ is the **Hermitian subspace**, the fixed-point set of the Hermitian conjugation $\dagger$ (equivalently, its eigenspace with eigenvalue $+1$). The two are complementary: together they span $\mathbb{B}$, and their intersection is trivial.

The two subspaces have distinct physical roles:

- **$\mathbb{M}_-$ is the material sector.** Its coordinates are **$ict$** (an imaginary temporal coordinate, $c$ being the speed of light) and **$x, y, z$** (three real spatial coordinates). It is the home of the four-vectors of relativistic physics. The imaginary time coordinate reflects a simple fact: time can be measured, but it cannot be touched, held, or moved through.
- **$\mathbb{M}_+$ is the informational sector.** Its coordinates are **$ct'$** (a real temporal coordinate) and **$ix', iy', iz'$** (three imaginary spatial coordinates). It is the home of the Hermitian operators, whose algebraic structure is that of a quantum-mechanical state space. The elements of $\mathbb{M}_+$ carry quantum-informational content, in the sense established in the companion article on quantum mechanics: they are the states, observables, and measurement operators of a qubit. The name "informational sector" reflects this content. It is not a claim about entropy or any other thermodynamic property of the sector.

The complex structure makes the two sectors complementary: the material sector has three real spatial directions and one imaginary temporal direction; the informational sector has three imaginary spatial directions and one real temporal direction.

## The Complex Coordinates

Writing the biquaternion coordinate in terms of its material and informational parts,

$$
\tilde{Q} = \underbrace{(ict)\,e_0 + (x\,e_1 + y\,e_2 + z\,e_3)}_{\in\,\mathbb{M}_-} \;+\; \underbrace{(ct')\,e_0 + (ix'\,e_1 + iy'\,e_2 + iz'\,e_3)}_{\in\,\mathbb{M}_+},
$$

the coefficients $Q_0, Q_1, Q_2, Q_3$ take the explicit form

$$
Q_0 = ct' + ict, \qquad Q_1 = x + i x', \qquad Q_2 = y + i y', \qquad Q_3 = z + i z'.
$$

The **real parameters** $(t, x, y, z)$ describe the material sector, and the **real parameters** $(t', x', y', z')$ describe the informational sector. Each sector is four-dimensional, and the full complexified spacetime is the direct sum of the two.

### The Vacuum Limit

In vacuum, $c = c_0$, and the material time coordinate becomes $ic_0 t$ — the familiar $ict$ form with the vacuum speed of light. The $ict$ convention is therefore the vacuum limit of the more general local structure. In a material medium, the complex structure uses $c$, the local speed of light, and varies from point to point. This makes the complex structure **local**, in the same spirit as the metric in general relativity.

## The Metric

The natural quadratic form on the biquaternion algebra is the complex bilinear form

$$
d\tilde{Q} \circ d\tilde{Q} = \sum_{\mu=0}^{3} (dQ_\mu)^2,
$$

where $\circ$ is the biquaternion product. Expanding in real and imaginary parts,

$$
(dQ_\mu)^2 = (dq_\mu)^2 - (dq'_\mu)^2 + 2i\,dq_\mu\,dq'_\mu.
$$

The **real part** of $d\tilde{Q} \circ d\tilde{Q}$ reproduces the Lorentzian interval on the material sector. The minus sign in the time–time component arises algebraically from $i^2 = -1$ in the imaginary time coordinate $ict$, not from an independently postulated metric signature. The **imaginary part** couples the material and informational sectors through cross terms.

## What the Framework Achieves

The main result of the framework so far is that the biquaternion algebra **contains, as a matter of algebra, the structures required for both relativity and quantum mechanics**. They are not incompatible sectors of physics that must be glued together; they are two aspects of the same algebra, appearing in its two complementary subspaces.

### Relativity in $\mathbb{M}_-$

The material sector $\mathbb{M}_-$ carries the four-vectors of relativistic physics: position, velocity, momentum, force, potential, current. The **Lorentz group** $SL(2,\mathbb{C})$ is realized as the **group of unit-norm biquaternions in $\mathbb{B}$**,

$$
SL(2,\mathbb{C}) \;\cong\; \{\tilde{\Lambda} \in \mathbb{B} : \tilde{\Lambda}\bar{\tilde{\Lambda}} = e_0\},
$$

and it **acts** on the material sector by the **rotor conjugation**

$$
\tilde{X} \;\longmapsto\; \tilde{\Lambda}\,\tilde{X}\,\tilde{\Lambda}^\dagger.
$$

The group itself lives in the full algebra $\mathbb{B}$ (since $\mathbb{M}_-$ is not closed under multiplication and cannot carry a group structure). The four-vectors it acts on live in $\mathbb{M}_-$. The different types of Lorentz transformation have rotors in different subspaces: pure boosts have rotors in $\mathbb{M}_+$ (they are Hermitian), pure spatial rotations have rotors in $\mathbb{H}_{\mathbb{B}}$ (they are real quaternions), and general Lorentz transformations have rotors in the full algebra.

The relativistic wave equations — **Maxwell's equations** and the **Dirac equation** — have natural biquaternion forms, as developed in the companion articles.

### Quantum Mechanics in $\mathbb{M}_+$

The informational sector $\mathbb{M}_+$ is, exactly, the operator algebra of a two-state quantum system. This is established in the companion article *Quantum Mechanics in Biquaternionic Form*, and it can be summarized as follows.

- The **idempotents** of $\mathbb{M}_+$, of the form $\tilde{P}_\pm(\hat{\mu}) = \tfrac{1}{2}(e_0 \pm i\hat{\mu})$ with $\hat{\mu}$ a unit pure real quaternion, are the pure states of a qubit. They parametrize the Bloch sphere $S^2$.
- The **positive trace-one elements** of $\mathbb{M}_+$, of the form $\tilde{\rho} = \tfrac{1}{2}(e_0 + i\mathbf{r})$ with $|\mathbf{r}| \leq 1$, are the mixed states, parametrizing the Bloch ball.
- The **general Hermitian elements** of $\mathbb{M}_+$, of the form $\tilde{H} = h_0 e_0 + i\mathbf{h}$, are the observables, with spectral decomposition in terms of idempotents.
- The **trace pairing** $\mathrm{Tr}(\tilde{\rho}\tilde{H}) = h_0 + \mathbf{r}\cdot\mathbf{h}$ gives the Born rule, as a consequence of the algebra rather than an independent postulate.
- The **sandwich operation** $\tilde{\rho} \mapsto \tilde{P}\tilde{\rho}\tilde{P}$ gives the projective measurement and state update.
- The **unitary elements** of $\mathbb{B}$, and their conjugation action $\tilde{\rho} \mapsto \tilde{U}\tilde{\rho}\tilde{U}^\dagger$, give the reversible evolution.
- The distinction between **reversible evolution** and **irreversible measurement** is a property of the acting element (unitary vs. idempotent), not an additional postulate.

The operator algebra of quantum mechanics, its state space, its Born rule, and its measurement rule are all **structural consequences** of the algebra of $\mathbb{M}_+$. They are not imposed from outside.

### The Shared Home

The most significant feature of the framework is that **relativity and quantum mechanics share the same algebraic home**. The Lorentz group is realized as the group of unit-norm biquaternions in $\mathbb{B}$, and the operator algebra of quantum mechanics is realized in the Hermitian subspace $\mathbb{M}_+$. The two structures are not independent; they are aspects of the same algebra.

This is the sense in which the framework is proposed as an alternative to the standard formulation: not as a modification of relativity or of quantum mechanics, but as a **common algebraic ground** on which both can be expressed.

## Status and Open Questions

The framework is a **research program**, not a finished theory. The algebraic results — that $\mathbb{M}_-$ carries the four-vectors of relativity and that $\mathbb{M}_+$ carries the operator algebra of quantum mechanics — are established mathematics, and the identifications with the physical theories are developed in the companion articles.

What is not established is whether the framework has consequences beyond a reformulation of known physics. The key open questions are:

1. **Physical reality of the biquaternionic structure.** Is the biquaternion algebra merely a convenient reformulation of known physics, or does the structure of the universe genuinely follow the algebra? A structural hypothesis of this kind can only be evaluated by the richness of the consequences it produces.

2. **Coupling between the two sectors.** Beyond the Lorentz coupling via the rotor conjugation, is there a genuinely new coupling between the anti-Hermitian subspace $\mathbb{M}_-$ and the Hermitian subspace $\mathbb{M}_+$? Any such coupling would be where new physical content could reside.

3. **Extension to many qubits and to quantum field theory.** The quantum formalism presented in the companion article is for a single qubit. The extension to $n$ qubits (via the tensor product $\mathbb{B}^{\otimes n} \cong M_{2^n}(\mathbb{C})$), the second-quantized version, and the connection to quantum field theory remain to be developed.

4. **Relativistic quantum theory.** The biquaternion algebra contains both the Lorentz group and the operator algebra of quantum mechanics. A fully relativistic quantum theory of spinor fields — whose classical precursor is the biquaternion Dirac equation — is the natural continuation of the framework.

5. **Curved spacetime.** The framework so far is formulated on flat spacetime. Its extension to curved spacetime, and its relation to general relativity, remain open.

6. **Empirical contact.** What quantitative prediction distinguishes this framework from standard physics? This is the central open question, and the one on which the eventual evaluation of the hypothesis will depend.

The framework is offered as a structural intuition: that the two natural subspaces of the biquaternion algebra have distinct physical roles — one material, one informational — and that the algebra $\mathbb{B}$ is the natural home in which both relativity and quantum mechanics are expressed. The local speed of light $c = 1/\sqrt{\epsilon\mu}$ plays the role of the local scale factor of the complex structure, making the $ict$ convention a vacuum approximation of a more general local structure, in the same way that special relativity is a local approximation of general relativity.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ | Biquaternionic coordinate |
| $\mathbb{M}_-$ | Anti-Hermitian subspace (material sector): coordinates $(ict, x, y, z)$ |
| $\mathbb{M}_+$ | Hermitian subspace (informational sector): coordinates $(ct', x', y', z')$ |
| $\mathbb{H}_{\mathbb{B}}$ | Real quaternion subspace (home of the rotation rotors) |
| $\tilde{P}_\pm(\hat{\mu}) = \tfrac{1}{2}(e_0 \pm i\hat{\mu})$ | Idempotent (pure state of the informational sector) |
| $\tilde{H} = h_0 e_0 + i\mathbf{h}$ | Hermitian element (observable of the informational sector) |
| $\tilde{\Lambda} \in \mathbb{B}$ with $\tilde{\Lambda}\bar{\tilde{\Lambda}} = e_0$ | Lorentz rotor (unit-norm biquaternion) |
| $c = 1/\sqrt{\epsilon\mu}$ | Speed of light in the medium (local) |
| $c_0 = 1/\sqrt{\epsilon_0\mu_0}$ | Speed of light in vacuum (global constant) |
| $v$ | Particle or frame velocity |

## Further Reading

- Hermann Minkowski, "Space and Time" (1908), reprinted in *The Principle of Relativity* (Dover).
- Roger Penrose, *The Road to Reality* (Knopf, 2004), for the complex structure of spacetime.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection between Clifford algebras and the structures discussed here.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric algebra perspective on the same structures.
- Vladimir V. Kassandrov, "Relativistic Algebra of Space-Time and Algebrodynamics" (2006), for a related biquaternionic approach to complexified geometry.

