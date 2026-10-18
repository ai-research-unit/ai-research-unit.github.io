# __Introduction to the Biquaternion Universe__

## Core Proposal

The fundamental structure of the universe is a biquaternionic space, of which Minkowski space is a slice. A point in this complexified spacetime is an element of the **biquaternion algebra** $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$, written as a biquaternionic coordinate

$$
\tilde{Q} = Q_t e_t + Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z,
$$

where $e_t = 1$ and $\vec e_x, \vec e_y, \vec e_z$ are the quaternion units. The four coefficients $Q_\mu$ are **complex**, and everything that follows turns on how each of them is split. Writing every coefficient as a real part plus $i$ times a real part,

$$
Q_t = q_t + iq'_t, \qquad Q_x = q_x + iq'_x, \qquad Q_y = q_y + iq'_y, \qquad Q_z = q_z + iq'_z, \qquad q_\mu, q'_\mu \in \mathbb{R},
$$

replaces the four complex coefficients by **eight real parameters**: $q_\mu$ is the real part of $Q_\mu$, the coefficient of $e_\mu$, and $q'_\mu$ its imaginary part, the coefficient of $ie_\mu$. The prime therefore marks the parameter that carries the $i$. As a real vector space $\mathbb{B}$ is eight-dimensional, and it splits naturally into two four-dimensional real subspaces — one taking $q'_t$ together with $q_x, q_y, q_z$, the other taking $q_t$ together with $q'_x, q'_y, q'_z$. The complex structure — the identification of which direction is "real" and which is "imaginary" — is **local**, determined by the electromagnetic properties of the medium at each point.

The hypothesis of this article is that this biquaternionic structure is the natural language in which the fundamental structures of physics are written, and that the fact that the framework contains both relativity and quantum physics is evidence for the proposal.

## Two Sectors: Material and Informational

The biquaternion algebra splits naturally into two complementary four-dimensional real subspaces:

$$
\mathbb{B} = \mathbb{M}_- \oplus \mathbb{M}_+.
$$

The subspace $\mathbb{M}_-$ is the **anti-Hermitian subspace**, the fixed-point set of the anti-Hermitian conjugation $\flat$ (equivalently, the eigenspace of the Hermitian conjugation ${}^{*}$ with eigenvalue $-1$). The subspace $\mathbb{M}_+$ is the **Hermitian subspace**, the fixed-point set of the Hermitian conjugation ${}^{*}$ (equivalently, its eigenspace with eigenvalue $+1$). The two are complementary: together they span $\mathbb{B}$, and their intersection is trivial.

The two subspaces have distinct physical roles:

- **$\mathbb{M}_-$ is the material sector.** Its coordinates are **$ict$** (an imaginary temporal coordinate, $c$ being the speed of light) and **$x, y, z$** (three real spatial coordinates). It is the home of the four-vectors of relativistic physics. The imaginary time coordinate reflects a simple fact: time can be measured, but it cannot be touched, held, or moved through.
- **$\mathbb{M}_+$ is the informational sector.** Its coordinates are **$ct'$** (a real temporal coordinate) and **$ix', iy', iz'$** (three imaginary spatial coordinates). It is the home of the Hermitian operators, whose algebraic structure is that of a quantum-mechanical state space. The elements of $\mathbb{M}_+$ carry quantum-informational content, in the sense established in the companion article on quantum physics: they are the states, observables, and measurement operators of a qubit. The name "informational sector" reflects this content. It is not a claim about entropy or any other thermodynamic property of the sector.

Written as elements of the algebra, each sector carries its own four real parameters, and each has two equivalent writings — one in those parameters, one in the physical coordinates:

- **$\mathbb{M}_-$**, the material sector, with the dictionary between the two writings:

    $$
    \tilde{R} = iq'_te_t + q_x\vec e_x + q_y\vec e_y + q_z\vec e_z = ic\,t\,e_t + x\,\vec e_x + y\,\vec e_y + z\,\vec e_z \in \mathbb{M}_-, \qquad q'_t = ct,\;\; q_x = x,\;\; q_y = y,\;\; q_z = z.
    $$

- **$\mathbb{M}_+$**, the informational sector, with the dictionary between the two writings:

    $$
    \tilde{Q} = q_te_t + iq'_x\vec e_x + iq'_y\vec e_y + iq'_z\vec e_z = (ct')\,e_t + (ix')\,\vec e_x + (iy')\,\vec e_y + (iz')\,\vec e_z \in \mathbb{M}_+, \qquad q_t = ct',\;\; q'_x = x',\;\; q'_y = y',\;\; q'_z = z'.
    $$

Where the prime falls is what distinguishes the sectors: in $\mathbb{M}_-$ it is the **scalar** $q'_t$ (the time), in $\mathbb{M}_+$ the **three vectors** $q'_k$ (the space). This is why the prime is not attached to a sector — $q'_t$ is a material parameter, $q'_k$ an informational one — and it is the one rule that makes the two sectors mirror images of each other. The complex structure is then visible as a count: the material sector has three real spatial directions and one imaginary temporal direction, the informational sector three imaginary spatial directions and one real temporal direction.

## The Complex Coordinates

Writing the biquaternion coordinate in terms of its material and informational parts,

$$
\tilde{Q} = \underbrace{(ict)\,e_t + (x\,\vec e_x + y\,\vec e_y + z\,\vec e_z)}_{\in\,\mathbb{M}_-} \;+\; \underbrace{(ct')\,e_t + (ix'\,\vec e_x + iy'\,\vec e_y + iz'\,\vec e_z)}_{\in\,\mathbb{M}_+},
$$

the coefficients $Q_t, Q_x, Q_y, Q_z$ take the explicit form

$$
\begin{aligned}
Q_t &= q_t + iq'_t = ct' + ict, \\
Q_x &= q_x + iq'_x = x + ix', \\
Q_y &= q_y + iq'_y = y + iy', \\
Q_z &= q_z + iq'_z = z + iz'.
\end{aligned}
$$

Each coefficient is thus shown in its three equivalent guises: the complex coefficient $Q_\mu$ itself, its real and imaginary parameters $q_\mu, q'_\mu$, and the physical coordinates those parameters carry.

The **real parameters** $(t, x, y, z)$ describe the material sector, and the **real parameters** $(t', x', y', z')$ describe the informational sector. Each sector is four-dimensional, and the full complexified spacetime is the direct sum of the two.

**The same decomposition, read on the coordinates.** The algebraic split of the opening and the coordinate values above are the same statement twice: matching the two writings coefficient by coefficient identifies each of the eight parameters with a coordinate,

$$
q_t = ct',\;\; q'_t = ct, \qquad q_k = x_k,\;\; q'_k = x'_k .
$$

The unprimed parameter is throughout the **real part** of the complex coefficient and the primed one its **imaginary part**. It is worth noting which is which at $\mu = 0$: the real part of $Q_t$ is $q_t = ct'$, an informational quantity, while its imaginary part $q'_t = ct$ is the material time. The two sectors take disjoint halves of the eight parameters — $\mathbb{M}_-$ takes $q'_t$ together with the three $q_k$, $\mathbb{M}_+$ takes $q_t$ together with the three $q'_k$ — so four complex coefficients and eight real parameters carry exactly the same information.

**One element, one point, one label.** The eight parameters split four and four between the sectors, and the split gives the element its second interpretation. A material element is a spacetime event of the material sector, $ict\,e_t+x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$, and the informational parameters it carries are its **internal label**; an informational element is an event of the informational sector, $ct'\,e_t+i(x'\,\vec e_x+y'\,\vec e_y+z'\,\vec e_z)$, carrying a material label. The four complex coefficients therefore read as a spacetime point together with the matching point of the other sector, and no coefficient is idle: each carries one coordinate of each sector at once. That is why one element of $\mathbb{B}$ serves both as a four-vector and as a state — the two interpretations use the two halves of the same four coefficients.

### The Vacuum Limit

In vacuum, $c = c_0$, and the material time coordinate becomes $ic_0 t$ — the familiar $ict$ form with the vacuum speed of light. The $ict$ convention is therefore the vacuum limit of the more general local structure. In a material medium, the complex structure uses $c$, the local speed of light, and varies from point to point. This makes the complex structure **local**, in the same spirit as the metric in general relativity.

## The Metric

The natural quadratic form on the biquaternion algebra is the **biquaternion norm**

$$
\langle d\tilde{Q}\rangle_{\natural} = d\tilde{Q} \circ d\tilde{Q}^{\natural} = \sum_{\mu\in\{t,x,y,z\}} (dQ_\mu)^2,
$$

where $\circ$ is the biquaternion product and ${}^{\natural}$ is the **quaternion conjugate**, the involution that reverses the three quaternion directions and leaves the complex coefficients alone: $e_t^{\natural}=e_t$, $\vec e_k^{\natural}=-\vec e_k$, hence $d\tilde{Q}^{\natural} = dQ_0\,e_t - dQ_1\,\vec e_x - dQ_2\,\vec e_y - dQ_3\,\vec e_z$. A second conjugation appears later in the article, the **bar**, and it acts on the other factor: it conjugates the complex coefficients and leaves the quaternion basis alone, $\overline{\tilde{Q}} = \sum_\mu \overline{Q_\mu}\,e_\mu$. The two are different operations of the same element, and the norm uses the first. The quaternion conjugate is what produces the sum of squares: the product $d\tilde{Q} \circ d\tilde{Q}$ of $d\tilde{Q}$ with itself is not $\sum_\mu (dQ_\mu)^2$. Expanding in real and imaginary parts,

$$
(dQ_\mu)^2 = (dq_\mu)^2 - (dq'_\mu)^2 + 2i\,dq_\mu\,dq'_\mu.
$$

The **real part** of $\langle d\tilde{Q}\rangle_{\natural} = \sum_\mu (dQ_\mu)^2$ reproduces the Lorentzian interval on the material sector. The minus sign in the time–time component arises algebraically from $i^2 = -1$ in the imaginary time coordinate $ict$, not from an independently postulated metric signature. The **imaginary part** couples the material and informational sectors through cross terms.

Because each sector retains only half of the eight parameters, the same biquaternion norm reads off as a real quadratic form on each, and it is again worth having both writings. On the material sector, where only $dq'_t$ and the $dq_k$ are non-zero,

$$
\langle d\tilde{Q}\rangle_{\natural} = -(dq'_t)^2 + dq_1^2 + dq_2^2 + dq_3^2 = -c^2\,dt^2 + dx^2 + dy^2 + dz^2,
$$

the Minkowski interval of signature $(3,1)$. On the informational sector, where only $dq_0$ and the $dq'_k$ are non-zero,

$$
\langle d\tilde{Q}\rangle_{\natural} = dq_0^2 - (dq'_x)^2 - (dq'_y)^2 - (dq'_z)^2 = c^2\,dt'^2 - dx'^2 - dy'^2 - dz'^2,
$$

the mirror interval of signature $(1,3)$. The two are exchanged by $i$, and the sign of the form reverses with them, $\langle i\tilde{Q}\rangle_{\natural} = -\langle\tilde{Q}\rangle_{\natural}$. In both cases the null cone — the zero divisor set, discussed in the companion articles — has the same two interpretations:

$$
\mathbb{M}_-:\;\; (dq'_t)^2 = dq_1^2 + dq_2^2 + dq_3^2 \iff c^2dt^2 =dx^2+dy^2+dz^2, \qquad
\mathbb{M}_+:\;\; dq_0^2 = (dq'_x)^2 + (dq'_y)^2 + (dq'_z)^2 \iff c^2dt'^2 = d(x'\,\vec e_x+y'\,\vec e_y+z'\,\vec e_z)^2 .
$$

Each of these is one equation written twice: on the left in the sector's own parameters, on the right in the coordinates of physics.

**Where the minus comes from.** Read as a form on $\mathbb{C}$, the same norm is the identity, $\langle\tilde{Q}\rangle_{\natural}=\sum_\mu Q_\mu^2$, with every entry positive and the four directions of $\mathbb{B}$ on an equal footing: there is no minus sign in the complex form itself, and none is needed, since a complex coefficient can carry the sign. The minus appears only when a *real* coordinate is placed on a direction whose coefficient carries a factor of $i$, as it is in each of the two real sectors above. The Minkowski signature is therefore not an independent input of the theory: it is what the algebra's own form looks like once the material time is written $ict$, with $i^2=-1$ supplying the minus. The norm as a complex form, and the four forms it takes, are *Conventions in the Biquaternion Universe*; the local complex structure behind the choice of $i$ is *The Local Complex Structure and the Speed of Light*.

**One root, three names.** The minus of the metric is one case of a single algebraic fact: the equation $\tilde{P}^{2}=\lambda e_t$ has three distinguished radicands, a root of $-1$ being a local complex structure, a root of $0$ a nilpotent of the light cone and a root of $+1$ an involution. The three answers are one equation, and the subspace in which the root is sought decides the physical name. Read on the elements, the same observation gives the massive, the massless and the spacelike as the interior, the boundary and the exterior of one quadric. The trichotomy is *Square Roots of One and the Idempotents: the Hermitian Observables and the States* and *Square Roots of Zero and the Nilpotents: the Light Cone*; the boundary is *The Light Cone as the Biquaternion Zero-Divisor Cone*; and the mass shell is *The Biquaternioid General Plain Sesqualgebra (GPS) over $\mathbb{C}$*.

### The Two Forms of One Element

The body has so far developed one form, the biquaternion norm $\langle\cdot\rangle_{\natural}$. The second is the **Hermitian form** on $\mathbb{M}_+$, $\langle\tilde{Q},\tilde{P}\rangle_{*}=\sum_\mu Q_\mu\overline{P_\mu}$, the sum of the four coordinates of one element against the conjugates of the other — the bar, the coefficient conjugation, and not the quaternion conjugate ${}^{\natural}$ of the norm. The two forms are two interpretations of one element, and they part company at once: the norm is complex and vanishes on the null cone, the Hermitian form is positive and vanishes only at the origin. At $\tilde{Q}=e_t+i\vec e_z$ the two already differ, $N=0$ while $H=2$: the same element is a null direction for the interval and a state of positive weight. The norm is the **interval**, whose zero set is the light cone; the Hermitian form is the **probability weight**, the form the Born rule draws on. One element carries both, and the framework's account of why the causal and the probabilistic structures coexist is that they are two forms on one biquaternion space and not two algebras. The form read as a product, and the positivity and the rank it carries, are *The Biquaternioid Symmetric Plain Sesqualgebra (SPS) over $\mathbb{C}$* and *The Biquaternioid General Plain Sesqualgebra (GPS) over $\mathbb{C}$*.

## What the Framework Achieves

The main result of the framework so far is that the biquaternion algebra **contains, as a matter of algebra, the structures required for both relativity and quantum physics**. They are not incompatible sectors of physics that must be glued together; they are two aspects of the same biquaternion space, appearing in its two complementary subspaces. Two further classifications are read from that algebra and developed elsewhere: the **reality condition** that fixes the type of a particle, and the split of the internal symmetry into a compact part carrying a discrete charge and a non-compact part carrying a continuous label. Both are *The Biquaternioid General Plain Sesqualgebra (GPS) over $\mathbb{C}$*; the antilinear structure behind them is *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*.

### Relativity in $\mathbb{M}_-$

A point of the material sector is written in the coordinates of relativistic physics as

$$
\tilde{R} = ic\,t\,e_t + x\,\vec e_x + y\,\vec e_y + z\,\vec e_z \in \mathbb{M}_-,
$$

the imaginary time $ic\,t$ together with the three real spatial coordinates $x, y, z$. The material sector $\mathbb{M}_-$ carries the four-vectors of relativistic physics: position, velocity, momentum, force, potential, current. The **proper orthochronous Lorentz group** $SO^+(1,3)$ is realized through its double cover $SL(2,\mathbb{C})$, which is the **group of biquaternions of unit norm** in $\mathbb{B}$:

$$
SL(2,\mathbb{C}) \;\cong\; \{\tilde{\Lambda} \in \mathbb{B} : \tilde{\Lambda}\tilde{\Lambda}^{\natural} = e_t\}.
$$

This group **acts** on the material sector by the **rotor conjugation**

$$
\tilde{Q} \;\longmapsto\; \tilde{\Lambda}\,\tilde{Q}\,\tilde{\Lambda}^{*}.
$$

The group itself lives in the full algebra $\mathbb{B}$ (since $\mathbb{M}_-$ is not closed under multiplication and cannot carry a group structure). The four-vectors it acts on live in $\mathbb{M}_-$. The different types of Lorentz transformation have rotors in different subspaces: pure boosts have rotors in $\mathbb{M}_+$ (they are Hermitian), pure spatial rotations have rotors in $\mathbb{H}_{\mathbb{B}}$ (they are real quaternions), and general Lorentz transformations have rotors in the full algebra.

The relativistic wave equations — **Maxwell's equations** and the **Dirac equation** — have natural biquaternion forms, as developed in the companion articles.

### Quantum Physics in $\mathbb{M}_+$

A point of the informational sector is written in its own coordinates as

$$
\tilde{Q} = (ct')\,e_t + (ix')\,\vec e_x + (iy')\,\vec e_y + (iz')\,\vec e_z \in \mathbb{M}_+,
$$

the real time $ct'$ together with the three imaginary spatial coordinates $ix', iy', iz'$. The informational sector $\mathbb{M}_+$ is, exactly, the operator algebra of a two-state quantum system. This is established in the companion article *Quantum Physics in Biquaternionic Form*, and it can be summarized as follows.

- The **idempotents** in $\mathbb{M}_+$, of the form $\tilde\Pi_{1,2}(\vec u) = \tfrac{1}{2}(e_t \pm i\vec u)$ with $\vec u$ a unit pure real quaternion, are the pure states of a qubit. They parametrize the Bloch sphere $S^2$.
- The **positive trace-one elements** in $\mathbb{M}_+$, of the form $\tilde{Ϛ} = \tfrac{1}{2}(e_t + i\vec r)$ with $|\vec r| \leq 1$, are the mixed states, parametrizing the Bloch ball.
- The **elements** of $\mathbb{M}_+$, of the form $\tilde{H} = h_0 e_t + i\vec h$ — equivalently written $\tilde{H} = h_0e_t + ih_1\vec e_x + ih_2\vec e_y + ih_3\vec e_z$ with $h_0, h_1, h_2, h_3 \in \mathbb{R}$, which is the usual writing of quantum physics — are the observables (they are automatically Hermitian by definition of $\mathbb{M}_+$), with spectral decomposition in terms of idempotents.
- The **trace pairing** $\mathrm{Tr}(\tilde{Ϛ}\tilde{H}) = h_0 + \vec r\cdot\vec h$ gives the Born rule, as a consequence of the algebra rather than an independent postulate.
- The **sandwich operation** $\tilde{Ϛ} \mapsto \tilde{P}\tilde{Ϛ}\tilde{P}/\mathrm{Tr}(\tilde{P}\tilde{Ϛ}\tilde{P})$ gives the projective measurement and state update (the trace in the denominator normalizes the post-measurement state).
- The **unitary elements** of $\mathbb{B}$, and their conjugation action $\tilde{Ϛ} \mapsto \tilde{U}\tilde{Ϛ}\tilde{U}^{*}$, give the reversible evolution.
- The distinction between **reversible evolution** and **irreversible measurement** is a property of the acting element (unitary vs. idempotent), not an additional postulate.

The operator algebra of quantum physics, its state space, its Born rule, and its measurement rule are all **structural consequences** of the algebra of $\mathbb{M}_+$. They are not imposed from outside. The two-state formalism at large is *Quantum Physics in Biquaternionic Form*; the derivation of the Born rule, and its comparison with the postulate it replaces, are *The Born Rule as a Trace Formula — Derivation and Comparison*; the states that the indefinite fourth product cannot normalise are *The Biquaternioid General Quaternionic Sesqualgebra (GQS) over $\mathbb{C}$*; and the decoherence of a measurement is *Decoherence as Idempotent Projection*.

### The Shared Home

The most significant feature of the framework is that **relativity and quantum physics share the same biquaternion space**. The Lorentz group is realized (via its double cover $SL(2,\mathbb{C})$) as the group of biquaternions of unit norm in $\mathbb{B}$, and the operator algebra of quantum physics is realized in the Hermitian subspace $\mathbb{M}_+$. The two structures are not independent; they are aspects of the same biquaternion space.

This is the sense in which the framework is proposed as an alternative to the standard formulation: not as a modification of relativity or of quantum physics, but as a **common biquaternion space** on which both can be expressed.

### The Two Slots of One Product

Every product of the algebra reads two elements, one in each **slot**, and in the framework's two sesquilinear products the slots are not interchangeable: one is read plainly and the other through a conjugation. That asymmetry is the algebraic form of the two roles a quantum description pairs — an element and the adjoint of another — and it is the reason the Born weight above can be read as the scalar part of a product on the algebra rather than as a pairing imposed from outside. The four products, the two slots and their four interpretations are *The Four General Products and Their Physical Readings*; the state and observable roles, the gauge action generated inside the algebra, and the chirality of that action are *The Biquaternioid General Plain Sesqualgebra (GPS) over $\mathbb{C}$*.

**Four jobs, one grid.** The four products are read as the four jobs a relativistic quantum theory needs — composition, causality, probability and gauge — and each splits into a symmetric half and an antisymmetric half, so that the twelve products of the space are the four general products together with the two halves of each. What the algebra fixes is the grid and the signs; that these are the four jobs, and that the interpretation is exhaustive, is the framework's claim. The jobs are tabulated in *The Four General Products and Their Physical Readings*.

## Status and Open Questions

The framework is a **research program**, not a finished theory. The algebraic results — that $\mathbb{M}_-$ carries the four-vectors of relativity and that $\mathbb{M}_+$ carries the operator algebra of quantum physics — are established mathematics, and the identifications with the physical theories are developed in the companion articles.

What is not established is whether the framework has consequences beyond a reformulation of known physics. The key open questions are:

1. **Physical reality of the biquaternionic structure.** Is the biquaternion algebra merely a convenient reformulation of known physics, or does the structure of the universe genuinely follow the algebra? A structural hypothesis of this kind can only be evaluated by the richness of the consequences it produces.

2. **Coupling between the two sectors.** Beyond the Lorentz coupling via the rotor conjugation, is there a genuinely new coupling between the anti-Hermitian subspace $\mathbb{M}_-$ and the Hermitian subspace $\mathbb{M}_+$? Any such coupling would be where new physical content could reside. One minimal instance is already algebraic and not imposed: the **square**. For a material element the quaternionic square is the interval, $\tilde{Q}^{\natural}\tilde{Q}=\langle\tilde{Q}\rangle_{\natural}e_t$ with $\langle\cdot\rangle_{\natural}$ real, and the real scalar line lies in $\mathbb{M}_+$, so squaring is a map $\mathbb{M}_-\to\mathbb{M}_+$ supplied by the product itself — the interpretation carried by *The Biquaternioid General Quaternionic Algebra (GQA) over $\mathbb{C}$*. What remains open is a coupling with a dynamics; the square is a map, not an evolution.

3. **Extension to many qubits and to quantum field theory.** The quantum formalism presented in the companion article is for a single qubit. The extension to $n$ qubits (via the tensor product $\mathbb{B}^{\otimes n} \cong M_{2^n}(\mathbb{C})$), the second-quantized version, and the connection to quantum field theory remain to be developed.

4. **Relativistic quantum theory.** The biquaternion algebra contains both the Lorentz group and the operator algebra of quantum physics. A fully relativistic quantum theory of spinor fields — whose classical precursor is the biquaternion Dirac equation — is the natural continuation of the framework.

5. **Curved spacetime.** The framework so far is formulated on flat spacetime. Its extension to curved spacetime, and its relation to general relativity, remain open.

6. **Empirical contact.** What quantitative prediction distinguishes this framework from standard physics? This is the central open question, and the one on which the eventual evaluation of the hypothesis will depend.

The framework is offered as a structural intuition: that the two natural subspaces of the biquaternion algebra have distinct physical roles — one material, one informational — and that the algebra $\mathbb{B}$ is the natural home in which both relativity and quantum physics are expressed. The local speed of light $c = 1/\sqrt{\epsilon\mu}$ plays the role of the local scale factor of the complex structure, making the $ict$ convention a vacuum approximation of a more general local structure, in the same way that special relativity is a local approximation of general relativity.

## Physical Readings

Two interpretations of the introduction are worth separating. Read as a statement about invariance, the universe of the article is the sesquilinear pair: a change of the local complex structure moves the interval and the composition and leaves the probability form, the gauge calibration and the zero-divisor cone where they were (*Conventions in the Biquaternion Universe*). Read in time, its two sectors are two clocks reading one hand: the material time and the informational time are the two projections of one central coordinate, so each sector's time is read against the phase of the other (*Each Sector Is the Other's Clock: the Sector Exchange as Relational Time*). Four further readings can be named.

- **Amplitude interpretation.** Each complex coefficient $Q_\mu=q_\mu+iq'_\mu$ is one complex number, that is, a magnitude and a phase, so the arena of the framework is complex before any quantum interpretation is imposed: the two sectors are read as the real and the imaginary halves of one amplitude, and an element is a point of the complexified spacetime together with its conjugate amplitude data. Boundary: the interpretation names the shape of the coefficient and supplies neither a quantisation nor a measurement rule.
- **State-preparation interpretation.** The central map $\tilde H=-\tfrac{i}{2}\tilde Q$ carries a material four-vector to an informational element, and on the trace-one slice to a state: the four-vector $ict\,e_t+x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ is carried to $\tfrac12(ct\,e_t-i(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z))$, with $\mathrm{Tr}(\tilde H)=ct$ and $\langle\tilde H\rangle_{\natural}=-\tfrac14\langle\tilde Q\rangle_{\natural}$, so at $ct=1$ it is the Hermitian state $\tilde{Ϛ}=\tfrac12(e_t+i\vec r)$ with $\vec r=-(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)$. Boundary: the map is the mirror dictionary of *The Bloch Ball as the Trace-One Slice of the Future Light Cone*, which owns it, and the interpretation names a preparation and not a dynamics.
- **Cross-sector coupling by the square.** For a material element the quaternionic square is the interval itself, $\tilde{Q}^{\natural}\tilde{Q}=\langle\tilde{Q}\rangle_{\natural}e_t$ with $\langle\cdot\rangle_{\natural}$ real, and the real scalar line lies in $\mathbb{M}_+$: squaring is therefore one algebraic map $\mathbb{M}_-\to\mathbb{M}_+$, the minimal instance of the coupling asked for in question 2 above, supplied by the product rather than added by hand. The product of *two* material elements is not informational, while the *square of one* is. Boundary: one map, with image the real scalar line, and no dynamics; the identity is owned by *The Biquaternioid General Quaternionic Algebra (GQA) over $\mathbb{C}$*, and its grid-level pointer is *The Four General Products and Their Physical Readings*.
- **One locus, two lists.** The norm's zero set $\langle\tilde{Q}\rangle_{\natural}=0$ is the light cone of the material sector and it is also the locus on which the pure states of the informational sector sit: the idempotents $\tilde\Pi=\tfrac12(e_t\pm i\vec u)$ have $\langle\tilde\Pi\rangle_{\natural}=0$. The causal boundary and the list of pure states are one algebraic locus read twice, the zero-divisor cone. Boundary: the interpretation identifies sets, and it does not make every null element a pure state, the null cone being strictly larger than the set of idempotents; the state side is *The Biquaternioid General Quaternionic Sesqualgebra (GQS) over $\mathbb{C}$*, and the cone itself *The Light Cone as the Biquaternion Zero-Divisor Cone*.

## Summary

The framework is stated in one sentence: the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ is the common biquaternion space of relativity and quantum physics, and its two natural real subspaces carry the two theories. The **anti-Hermitian subspace** $\mathbb{M}_-$ carries the four-vectors of relativity, the material sector, in the coordinates $(ict,x,y,z)$; the **Hermitian subspace** $\mathbb{M}_+$ carries the operator algebra of quantum physics, the informational sector, in the coordinates $(ct',ix',iy',iz')$. Multiplication by $i$ exchanges the two.

Both sectors are written in the one biquaternion space. A material element is $\tilde{R}=ict\,e_t+x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ and an informational element is $\tilde{Q}=ct'\,e_t+i(x'\,\vec e_x+y'\,\vec e_y+z'\,\vec e_z)$; the norm $\langle\tilde{Q}\rangle_{\natural}=\sum_\mu Q_\mu^2$ is the interval on $\mathbb{M}_-$, of signature $(-,+,+,+)$ there, and the Hermitian form on $\mathbb{M}_+$. The Lorentz rotors are the unit-norm elements $\tilde{\Lambda}$ with $\tilde{\Lambda}\tilde{\Lambda}^{\natural}=e_t$, acting by conjugation; the idempotents $\tilde\Pi_{1,2}(\vec u)=\tfrac12(e_t\pm i\vec u)$ are the pure states of the informational sector; and the observables are the Hermitian elements $\tilde{H}=h_0e_t+i\vec h$ with $h_0$ real.

The framework is a research program, not a finished theory. The algebraic identifications above are established mathematics; what is open is whether the framework has consequences beyond a reformulation of known physics. Six questions are recorded: the physical reality of the biquaternionic structure; a coupling between the sectors beyond the Lorentz conjugation, of which the square $\mathbb{M}_-\to\mathbb{M}_+$ is the minimal algebraic instance already supplied by the product; the extension to many qubits and to quantum field theory; a fully relativistic quantum theory; curved spacetime; and empirical contact. The local speed of light $c=1/\sqrt{\epsilon\mu}$ plays the role of the local scale factor of the complex structure, making the $ict$ convention the vacuum approximation of a more general local structure.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ | Biquaternionic coordinate |
| $Q_\mu = q_\mu + iq'_\mu$ | Complex coefficient: $q_\mu$ its real part (the coefficient of $e_\mu$), $q'_\mu$ its imaginary part (the coefficient of $ie_\mu$) |
| $\tilde{R} = iq'_te_t + q_x\vec e_x + q_y\vec e_y + q_z\vec e_z = ict\,e_t + x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ | Material element, both writings; $q'_t = ct$, $q_k = x_k$ |
| $\tilde{Q} = q_te_t + iq'_x\vec e_x + iq'_y\vec e_y + iq'_z\vec e_z = (ct')\,e_t + i(x'\,\vec e_x+y'\,\vec e_y+z'\,\vec e_z)$ | Informational element, both writings; $q_t = ct'$, $q'_k = x'_k$ |
| $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$ | Biquaternion norm; the identity matrix $\mathrm{diag}(+1,+1,+1,+1)$ as a metric on $\mathbb{C}$, signature $(-,+,+,+)$ on the real material sector |
| $\langle\tilde{Q},\tilde{P}\rangle_{*} = \sum_\mu Q_\mu\overline{P_\mu}$ | Hermitian form, positive definite; the probability weight, $\langle\tilde{Q},\tilde{Q}\rangle_{*} = \sum_\mu\lvert Q_\mu\rvert^{2}$; the coefficient of $e_t$ in $\tilde{Q}\tilde{Q}^{*}$ |
| ${}^{\natural}$ | Quaternion conjugate: reverses the quaternion basis, $e_t^{\natural}=e_t$ and $\vec e_k^{\natural}=-\vec e_k$, and leaves the complex coefficients $Q_\mu$ untouched; the conjugation of the norm, $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural}$ |
| $\overline{\cdot}$ | Bar, the coefficient conjugation: conjugates each complex coefficient $Q_\mu$ and leaves the quaternion basis untouched, $\overline{\tilde{Q}} = \sum_\mu \overline{Q_\mu}\,e_\mu$; the conjugation of the Hermitian form, $\langle\tilde{Q},\tilde{P}\rangle_{*} = \sum_\mu Q_\mu\overline{P_\mu}$ |
| ${}^{*} = \overline{\cdot}\circ{}^{\natural}$ | Hermitian conjugation: conjugates both factors, $\tilde{Q}^{*} = \overline{Q_t}e_t - \overline{Q_x}\vec e_x - \overline{Q_y}\vec e_y - \overline{Q_z}\vec e_z$; the conjugation that defines the two sectors, the fixed points of ${}^{*}$ being $\mathbb{M}_+$ |
| ${}^{\flat} = -{}^{*}$ | Anti-Hermitian conjugation: the star composed with the central sign, $\tilde{Q}^{\flat} = -\tilde{Q}^{*}$, of which the material sector $\mathbb{M}_-$ is the fixed-point set |
| $\mathbb{M}_-$ | Anti-Hermitian subspace (material sector): coordinates $(ict, x, y, z)$, parameters $q'_t, q_x, q_y, q_z$ |
| $\mathbb{M}_+$ | Hermitian subspace (informational sector): coordinates $(ct', ix', iy', iz')$, parameters $q_t, q'_x, q'_y, q'_z$ |
| $\mathbb{H}_{\mathbb{B}}$ | Real quaternion subspace (home of the rotation rotors): the real half, all four coefficients real, fixed points of complex conjugation; a subalgebra |
| $i\mathbb{H}_{\mathbb{B}}$ | Antiquaternion subspace: the imaginary half, all four coefficients purely imaginary, the partner of $\mathbb{H}_{\mathbb{B}}$ in $\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}$. This split crosses the $\mathbb{M}_\pm$ split: the scalar of $\mathbb{M}_-$ and the vectors of $\mathbb{M}_+$ come from here |
| $\tilde\Pi_{1,2}(\vec u) = \tfrac{1}{2}(e_t \pm i\vec u)$ | Idempotent (pure state of the informational sector) |
| $\tilde{H} = h_0 e_t + i\vec h$ | Hermitian element (observable of the informational sector); $h_0 \in \mathbb{R}$ is the scalar component and $\vec h = (h_1,h_2,h_3)$ the vector components. These are the generic names used for these components throughout the series; written as a coordinate-carrying element, the same object is $q_te_t + iq'_k\vec e_k$ |
| $(t, x, y, z)$ | Real coordinates of the material sector ($c$ is a scale factor, not a coordinate) |
| $(t', x', y', z')$ | Real coordinates of the informational sector |
| $\tilde{\Lambda} \in \mathbb{B}$ with $\tilde{\Lambda}\tilde{\Lambda}^{\natural} = e_t$ | Lorentz rotor (unit-norm biquaternion) |
| $c = 1/\sqrt{\epsilon\mu}$ | Speed of light in the medium (local) |
| $c_0 = 1/\sqrt{\epsilon_0\mu_0}$ | Speed of light in vacuum (global constant) |
| $v$ | Particle or frame velocity |

## Further Reading

- Hermann Minkowski, "Space and Time" (1908), reprinted in *The Principle of Relativity* (Dover).
- Roger Penrose, *The Road to Reality* (Knopf, 2004), for the complex structure of spacetime.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection between Clifford algebras and the structures discussed here.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric algebra perspective on the same structures.
- Vladimir V. Kassandrov, "Relativistic Algebra of Space-Time and Algebrodynamics" (2006), for a related biquaternionic approach to complexified geometry.

