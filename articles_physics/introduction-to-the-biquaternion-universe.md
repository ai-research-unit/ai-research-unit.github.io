# __Introduction to the Biquaternion Universe__

## Core Proposal

The fundamental structure of the universe is a biquaternion space, of which Minkowski space is one real slice. A point in this complexified spacetime is an element of the **biquaternion algebra** $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$, written as a biquaternionic coordinate

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3,
$$

where $e_0 = 1$ and $e_1, e_2, e_3$ are the quaternion units. The four coefficients $Q_\mu$ are **complex**, and everything that follows turns on how each of them is split. Writing every coefficient as a real part plus $i$ times a real part,

$$
Q_0 = q_0 + iq'_0, \qquad Q_1 = q_1 + iq'_1, \qquad Q_2 = q_2 + iq'_2, \qquad Q_3 = q_3 + iq'_3, \qquad q_\mu, q'_\mu \in \mathbb{R},
$$

replaces the four complex coefficients by **eight real parameters**: $q_\mu$ is the real part of $Q_\mu$, the coefficient of $e_\mu$, and $q'_\mu$ its imaginary part, the coefficient of $ie_\mu$. The prime therefore marks the parameter that carries the $i$. As a real vector space $\mathbb{B}$ is eight-dimensional, and it splits naturally into two four-dimensional real subspaces — one taking $q'_0$ together with $q_1, q_2, q_3$, the other taking $q_0$ together with $q'_1, q'_2, q'_3$. The complex structure — the identification of which direction is "real" and which is "imaginary" — is **local**, determined by the electromagnetic properties of the medium at each point.

The hypothesis of this article is that this biquaternionic structure is the natural language in which the fundamental structures of physics are written, and that the fact that the framework contains both relativity and quantum mechanics is evidence for the proposal.

## Two Sectors: Material and Informational

The biquaternion algebra splits naturally into two complementary four-dimensional real subspaces:

$$
\mathbb{B} = \mathbb{M}_- \oplus \mathbb{M}_+.
$$

The subspace $\mathbb{M}_-$ is the **anti-Hermitian subspace**, the fixed-point set of the anti-Hermitian conjugation $\flat$ (equivalently, the eigenspace of the Hermitian conjugation $\dagger$ with eigenvalue $-1$). The subspace $\mathbb{M}_+$ is the **Hermitian subspace**, the fixed-point set of the Hermitian conjugation $\dagger$ (equivalently, its eigenspace with eigenvalue $+1$). The two are complementary: together they span $\mathbb{B}$, and their intersection is trivial.

The two subspaces have distinct physical roles:

- **$\mathbb{M}_-$ is the material sector.** Its coordinates are **$ict$** (an imaginary temporal coordinate, $c$ being the speed of light) and **$x, y, z$** (three real spatial coordinates). It is the home of the four-vectors of relativistic physics. The imaginary time coordinate reflects a simple fact: time can be measured, but it cannot be touched, held, or moved through.
- **$\mathbb{M}_+$ is the informational sector.** Its coordinates are **$ct'$** (a real temporal coordinate) and **$ix', iy', iz'$** (three imaginary spatial coordinates). It is the home of the Hermitian operators, whose algebraic structure is that of a quantum-mechanical state space. The elements of $\mathbb{M}_+$ carry quantum-informational content, in the sense established in the companion article on quantum mechanics: they are the states, observables, and measurement operators of a qubit. The name "informational sector" reflects this content. It is not a claim about entropy or any other thermodynamic property of the sector.

Written as elements of the algebra, each sector carries its own four real parameters, and each has two equivalent writings — one in those parameters, one in the physical coordinates:

- **$\mathbb{M}_-$**, the material sector, with the dictionary between the two writings:

    $$
    \tilde{Q} = iq'_0e_0 + q_1e_1 + q_2e_2 + q_3e_3 = ic\,t\,e_0 + x\,e_1 + y\,e_2 + z\,e_3 \in \mathbb{M}_-, \qquad q'_0 = ct,\;\; q_1 = x,\;\; q_2 = y,\;\; q_3 = z.
    $$

- **$\mathbb{M}_+$**, the informational sector, with the dictionary between the two writings:

    $$
    \tilde{Q} = q_0e_0 + iq'_1e_1 + iq'_2e_2 + iq'_3e_3 = (ct')\,e_0 + (ix')\,e_1 + (iy')\,e_2 + (iz')\,e_3 \in \mathbb{M}_+, \qquad q_0 = ct',\;\; q'_1 = x',\;\; q'_2 = y',\;\; q'_3 = z'.
    $$

Where the prime falls is what distinguishes the sectors: in $\mathbb{M}_-$ it is the **scalar** $q'_0$ (the time), in $\mathbb{M}_+$ the **three vectors** $q'_k$ (the space). This is why the prime is not attached to a sector — $q'_0$ is a material parameter, $q'_k$ an informational one — and it is the one rule that makes the two sectors mirror images of each other. The complex structure is then visible as a count: the material sector has three real spatial directions and one imaginary temporal direction, the informational sector three imaginary spatial directions and one real temporal direction.

## The Complex Coordinates

Writing the biquaternion coordinate in terms of its material and informational parts,

$$
\tilde{Q} = \underbrace{(ict)\,e_0 + (x\,e_1 + y\,e_2 + z\,e_3)}_{\in\,\mathbb{M}_-} \;+\; \underbrace{(ct')\,e_0 + (ix'\,e_1 + iy'\,e_2 + iz'\,e_3)}_{\in\,\mathbb{M}_+},
$$

the coefficients $Q_0, Q_1, Q_2, Q_3$ take the explicit form

$$
\begin{aligned}
Q_0 &= q_0 + iq'_0 = ct' + ict, \\
Q_1 &= q_1 + iq'_1 = x + ix', \\
Q_2 &= q_2 + iq'_2 = y + iy', \\
Q_3 &= q_3 + iq'_3 = z + iz'.
\end{aligned}
$$

Each coefficient is thus shown in its three equivalent guises: the complex coefficient $Q_\mu$ itself, its real and imaginary parameters $q_\mu, q'_\mu$, and the physical coordinates those parameters carry.

The **real parameters** $(t, x, y, z)$ describe the material sector, and the **real parameters** $(t', x', y', z')$ describe the informational sector. Each sector is four-dimensional, and the full complexified spacetime is the direct sum of the two.

**The same decomposition, read on the coordinates.** The algebraic split of the opening and the coordinate values above are the same statement twice: matching the two writings coefficient by coefficient identifies each of the eight parameters with a coordinate,

$$
q_0 = ct',\;\; q'_0 = ct, \qquad q_k = x_k,\;\; q'_k = x'_k .
$$

The unprimed parameter is throughout the **real part** of the complex coefficient and the primed one its **imaginary part**. It is worth noting which is which at $\mu = 0$: the real part of $Q_0$ is $q_0 = ct'$, an informational quantity, while its imaginary part $q'_0 = ct$ is the material time. The two sectors take disjoint halves of the eight parameters — $\mathbb{M}_-$ takes $q'_0$ together with the three $q_k$, $\mathbb{M}_+$ takes $q_0$ together with the three $q'_k$ — so four complex coefficients and eight real parameters carry exactly the same information.

### The Vacuum Limit

In vacuum, $c = c_0$, and the material time coordinate becomes $ic_0 t$ — the familiar $ict$ form with the vacuum speed of light. The $ict$ convention is therefore the vacuum limit of the more general local structure. In a material medium, the complex structure uses $c$, the local speed of light, and varies from point to point. This makes the complex structure **local**, in the same spirit as the metric in general relativity.

## The Metric

The natural quadratic form on the biquaternion algebra is the **norm form**

$$
N(d\tilde{Q}) = d\tilde{Q} \circ \overline{d\tilde{Q}} = \sum_{\mu=0}^{3} (dQ_\mu)^2,
$$

where $\circ$ is the biquaternion product and $\overline{\cdot}$ is the quaternion conjugate. The conjugate is what produces the sum of squares: the product $d\tilde{Q} \circ d\tilde{Q}$ of $d\tilde{Q}$ with itself is not $\sum_\mu (dQ_\mu)^2$. Expanding in real and imaginary parts,

$$
(dQ_\mu)^2 = (dq_\mu)^2 - (dq'_\mu)^2 + 2i\,dq_\mu\,dq'_\mu.
$$

The **real part** of $N(d\tilde{Q}) = \sum_\mu (dQ_\mu)^2$ reproduces the Lorentzian interval on the material sector. The minus sign in the time–time component arises algebraically from $i^2 = -1$ in the imaginary time coordinate $ict$, not from an independently postulated metric signature. The **imaginary part** couples the material and informational sectors through cross terms.

Because each sector retains only half of the eight parameters, the same norm form reads off as a real quadratic form on each, and it is again worth having both writings. On the material sector, where only $dq'_0$ and the $dq_k$ are non-zero,

$$
N(d\tilde{X}) = -(dq'_0)^2 + dq_1^2 + dq_2^2 + dq_3^2 = -c^2\,dt^2 + dx^2 + dy^2 + dz^2,
$$

the Minkowski interval of signature $(3,1)$. On the informational sector, where only $dq_0$ and the $dq'_k$ are non-zero,

$$
N(d\tilde{H}) = dq_0^2 - (dq'_1)^2 - (dq'_2)^2 - (dq'_3)^2 = c^2\,dt'^2 - dx'^2 - dy'^2 - dz'^2,
$$

the mirror interval of signature $(1,3)$. The two are exchanged by $i$, and the sign of the form reverses with them, $N(i\tilde{Q}) = -N(\tilde{Q})$. In both cases the null cone — the zero divisor set, discussed in the companion articles — has the same two readings:

$$
\mathbb{M}_-:\;\; (dq'_0)^2 = dq_1^2 + dq_2^2 + dq_3^2 \iff c^2dt^2 = d\mathbf{x}^2, \qquad
\mathbb{M}_+:\;\; dq_0^2 = (dq'_1)^2 + (dq'_2)^2 + (dq'_3)^2 \iff c^2dt'^2 = d\mathbf{x}'^2 .
$$

Each of these is one equation written twice: on the left in the sector's own parameters, on the right in the coordinates of physics.

### Where the Minus Comes From

The same norm form is read two ways, and keeping them apart prevents a recurring confusion. They are worth stating plainly here, at the start.

**The algebra's own form.** The biquaternion universe is a $\mathbb{C}$-universe over the quaternions, and its coefficients $Q_\mu$ are complex. Read as a metric on $\mathbb{C}$, the norm form is the identity,

$$
N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_{\mu=0}^{3} Q_\mu^2, \qquad \mathrm{diag}(+1,+1,+1,+1),
$$

with every entry positive and the four directions of $\mathbb{B}$ on an equal footing. There is no minus sign in the form itself, and none is needed. It is a *complex* bilinear form, and that is exactly what makes this possible: a complex coefficient can carry the sign, so no direction has to be singled out by the metric in advance.

**The real sectors.** A minus appears only when a *real* coordinate is placed on a direction whose coefficient carries a factor of $i$. The two four-dimensional real sectors are exactly such choices, and they read off the same form differently:

| Sector | Basis | $N$ on the basis | Signature |
|---|---|---|---|
| $\mathbb{M}_-$ (material) | $ie_0,\ e_1,\ e_2,\ e_3$ | $-1,+1,+1,+1$ | $(-,+,+,+)$ |
| $\mathbb{M}_+$ (informational) | $e_0,\ ie_1,\ ie_2,\ ie_3$ | $+1,-1,-1,-1$ | $(+,-,-,-)$ |

Multiplying by $i$ exchanges the two sectors, $i\mathbb{M}_+ = \mathbb{M}_-$, and reverses the sign of the form, $N(i\tilde{Q}) = -N(\tilde{Q})$; that is the algebraic content of the mirror relation between the two signatures. The Minkowski signature is therefore not an independent input of the theory. It is what the algebra's own form looks like once the time coordinate is written $ict$ — the same norm form, read on the material sector, with $i^2 = -1$ supplying the minus.

## What the Framework Achieves

The main result of the framework so far is that the biquaternion algebra **contains, as a matter of algebra, the structures required for both relativity and quantum mechanics**. They are not incompatible sectors of physics that must be glued together; they are two aspects of the same algebra, appearing in its two complementary subspaces.

### Relativity in $\mathbb{M}_-$

The material sector $\mathbb{M}_-$ carries the four-vectors of relativistic physics: position, velocity, momentum, force, potential, current. The **proper orthochronous Lorentz group** $SO^+(1,3)$ is realized through its double cover $SL(2,\mathbb{C})$, which is the **group of biquaternions of unit norm form** in $\mathbb{B}$:

$$
SL(2,\mathbb{C}) \;\cong\; \{\tilde{\Lambda} \in \mathbb{B} : \tilde{\Lambda}\bar{\tilde{\Lambda}} = e_0\}.
$$

This group **acts** on the material sector by the **rotor conjugation**

$$
\tilde{X} \;\longmapsto\; \tilde{\Lambda}\,\tilde{X}\,\tilde{\Lambda}^\dagger.
$$

The group itself lives in the full algebra $\mathbb{B}$ (since $\mathbb{M}_-$ is not closed under multiplication and cannot carry a group structure). The four-vectors it acts on live in $\mathbb{M}_-$. The different types of Lorentz transformation have rotors in different subspaces: pure boosts have rotors in $\mathbb{M}_+$ (they are Hermitian), pure spatial rotations have rotors in $\mathbb{H}_{\mathbb{B}}$ (they are real quaternions), and general Lorentz transformations have rotors in the full algebra.

The relativistic wave equations — **Maxwell's equations** and the **Dirac equation** — have natural biquaternion forms, as developed in the companion articles.

### Quantum Mechanics in $\mathbb{M}_+$

The informational sector $\mathbb{M}_+$ is, exactly, the operator algebra of a two-state quantum system. This is established in the companion article *Quantum Mechanics in Biquaternionic Form*, and it can be summarized as follows.

- The **idempotents** in $\mathbb{M}_+$, of the form $\tilde{P}_\pm(\hat{\mu}) = \tfrac{1}{2}(e_0 \pm i\hat{\mu})$ with $\hat{\mu}$ a unit pure real quaternion, are the pure states of a qubit. They parametrize the Bloch sphere $S^2$.
- The **positive trace-one elements** in $\mathbb{M}_+$, of the form $\tilde{\rho} = \tfrac{1}{2}(e_0 + i\mathbf{r})$ with $|\mathbf{r}| \leq 1$, are the mixed states, parametrizing the Bloch ball.
- The **elements** of $\mathbb{M}_+$, of the form $\tilde{H} = h_0 e_0 + i\mathbf{h}$, are the observables (they are automatically Hermitian by definition of $\mathbb{M}_+$), with spectral decomposition in terms of idempotents.
- The **trace pairing** $\mathrm{Tr}(\tilde{\rho}\tilde{H}) = h_0 + \mathbf{r}\cdot\mathbf{h}$ gives the Born rule, as a consequence of the algebra rather than an independent postulate.
- The **sandwich operation** $\tilde{\rho} \mapsto \tilde{P}\tilde{\rho}\tilde{P}/\mathrm{Tr}(\tilde{P}\tilde{\rho}\tilde{P})$ gives the projective measurement and state update (the trace in the denominator normalizes the post-measurement state).
- The **unitary elements** of $\mathbb{B}$, and their conjugation action $\tilde{\rho} \mapsto \tilde{U}\tilde{\rho}\tilde{U}^\dagger$, give the reversible evolution.
- The distinction between **reversible evolution** and **irreversible measurement** is a property of the acting element (unitary vs. idempotent), not an additional postulate.

The operator algebra of quantum mechanics, its state space, its Born rule, and its measurement rule are all **structural consequences** of the algebra of $\mathbb{M}_+$. They are not imposed from outside.

### The Shared Home

The most significant feature of the framework is that **relativity and quantum mechanics share the same algebraic home**. The Lorentz group is realized (via its double cover $SL(2,\mathbb{C})$) as the group of biquaternions of unit norm form in $\mathbb{B}$, and the operator algebra of quantum mechanics is realized in the Hermitian subspace $\mathbb{M}_+$. The two structures are not independent; they are aspects of the same algebra.

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
| $Q_\mu = q_\mu + iq'_\mu$ | Complex coefficient: $q_\mu$ its real part (the coefficient of $e_\mu$), $q'_\mu$ its imaginary part (the coefficient of $ie_\mu$) |
| $\tilde{X} = iq'_0e_0 + q_1e_1 + q_2e_2 + q_3e_3 = ict\,e_0 + \mathbf{x}$ | Material element, both writings; $q'_0 = ct$, $q_k = x_k$ |
| $\tilde{H} = q_0e_0 + iq'_1e_1 + iq'_2e_2 + iq'_3e_3 = (ct')\,e_0 + i\mathbf{x}'$ | Informational element, both writings; $q_0 = ct'$, $q'_k = x'_k$ |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$ | Norm form; the identity matrix $\mathrm{diag}(+1,+1,+1,+1)$ as a metric on $\mathbb{C}$, signature $(-,+,+,+)$ on the real material sector |
| $\mathbb{M}_-$ | Anti-Hermitian subspace (material sector): coordinates $(ict, x, y, z)$, parameters $q'_0, q_1, q_2, q_3$ |
| $\mathbb{M}_+$ | Hermitian subspace (informational sector): coordinates $(ct', ix', iy', iz')$, parameters $q_0, q'_1, q'_2, q'_3$ |
| $\mathbb{H}_{\mathbb{B}}$ | Real quaternion subspace (home of the rotation rotors): the real half, all four coefficients real, fixed points of complex conjugation; a subalgebra |
| $i\mathbb{H}_{\mathbb{B}}$ | Antiquaternion subspace: the imaginary half, all four coefficients purely imaginary, the partner of $\mathbb{H}_{\mathbb{B}}$ in $\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}$. This split crosses the $\mathbb{M}_\pm$ split: the scalar of $\mathbb{M}_-$ and the vectors of $\mathbb{M}_+$ come from here |
| $\tilde{P}_\pm(\hat{\mu}) = \tfrac{1}{2}(e_0 \pm i\hat{\mu})$ | Idempotent (pure state of the informational sector) |
| $\tilde{H} = h_0 e_0 + i\mathbf{h}$ | Hermitian element (observable of the informational sector); $h_0 \in \mathbb{R}$ is the scalar component and $\mathbf{h} = (h_1,h_2,h_3)$ the vector components. These are the generic names used for these components throughout the series; written as a coordinate-carrying element, the same object is $q_0e_0 + iq'_ke_k$ |
| $(t, x, y, z)$ | Real coordinates of the material sector ($c$ is a scale factor, not a coordinate) |
| $(t', x', y', z')$ | Real coordinates of the informational sector |
| $\tilde{\Lambda} \in \mathbb{B}$ with $\tilde{\Lambda}\bar{\tilde{\Lambda}} = e_0$ | Lorentz rotor (unit-norm-form biquaternion) |
| $c = 1/\sqrt{\epsilon\mu}$ | Speed of light in the medium (local) |
| $c_0 = 1/\sqrt{\epsilon_0\mu_0}$ | Speed of light in vacuum (global constant) |
| $v$ | Particle or frame velocity |

## Further Readings

- Hermann Minkowski, "Space and Time" (1908), reprinted in *The Principle of Relativity* (Dover).
- Roger Penrose, *The Road to Reality* (Knopf, 2004), for the complex structure of spacetime.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection between Clifford algebras and the structures discussed here.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric algebra perspective on the same structures.
- Vladimir V. Kassandrov, "Relativistic Algebra of Space-Time and Algebrodynamics" (2006), for a related biquaternionic approach to complexified geometry.

