# __Introduction to the Biquaternion Universe__

In theoretical physics, progress often begins by finding the right algebraic arena — a single mathematical structure in which seemingly separate phenomena appear as complementary facets of one object. Standard physics treats special relativity and quantum mechanics in distinct formalisms: real four-vectors and Lorentzian intervals on one side, complex Hilbert spaces and Hermitian operators on the other. This programme begins with the observation that both structures already live inside a single eight-dimensional algebra, the biquaternions $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$, splitting cleanly into its anti-Hermitian material subspace $\mathbb{B}_\Phi$ and its Hermitian informational subspace $\mathbb{B}_\Psi$. Unifying the two sectors at the algebraic level does not alter their established predictions; instead, it puts causal geometry, spinor symmetries, quantum states, and measurement rules into a common language — exposing cross-sector links and structural constraints that remain hidden when the two theories are kept apart.

## Core Hypothesis

The central hypothesis of this programme is that the biquaternion algebra is not merely a convenient representation of known physics, but the underlying structure from which the familiar relativistic and quantum sectors arise. What is mathematics is stated as such: the algebra carries a definite form, a Lorentzian form and a positive cone, and those facts hold whatever the universe turns out to be. What is hypothesis is the further claim that this structure is the one nature uses. A point of that space is an element of the **biquaternion algebra** $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$, written as a biquaternionic coordinate

$$
\tilde{Q} = Q_t e_t + \vec Q = Q_t e_t + Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z,
$$

where $e_t = 1$ and $\vec e_x, \vec e_y, \vec e_z$ are the quaternion units, so that $\vec Q = Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z$ is the vector part. The four coefficients $Q_\mu$ are **complex**, and everything that follows turns on how each of them is split. Writing every coefficient as a real part plus $i$ times a real part,

$$
Q_t = q_t + iq'_t, \quad Q_x = q_x + iq'_x, \quad Q_y = q_y + iq'_y, \quad Q_z = q_z + iq'_z, \qquad q_\mu, q'_\mu \in \mathbb{R},
$$

replaces the four complex coefficients by **eight real parameters**: $q_\mu$ is the real part of $Q_\mu$, the coefficient of $e_\mu$, and $q'_\mu$ its imaginary part, the coefficient of $ie_\mu$, so the eight parameters are the coordinates of one point. Which parameter belongs to which sector is decided below, in *The Complex Coordinates*, once the two sectors have been named. The four coefficients are lengths, and the two temporal parameters are lengths as well, so one element carries one unit in all four of its directions and no constant stands between the parameters. The prime therefore marks the parameter that carries the $i$. As a real vector space $\mathbb{B}$ is eight-dimensional, and it splits into two four-dimensional real subspaces; which four parameters each takes is stated in *The Complex Coordinates*. The identification of which direction is "real" and which is "imaginary" is the same at every point. What is local is the **unit** of the temporal axis, set by the local speed of light $c=1/\sqrt{\epsilon\mu}$.

The evidence currently available for this hypothesis is structural rather than empirical: the same algebra naturally contains both the relativistic and quantum frameworks, together with relationships between them that become visible only when they are expressed in a common algebraic language.

## Two Sectors: Material and Informational

The biquaternion algebra splits naturally into two complementary four-dimensional real subspaces:

$$
\mathbb{B} = \mathbb{B}_{\Phi} \oplus \mathbb{B}_{\Psi}.
$$

The subspace $\mathbb{B}_{\Phi}$ is the **anti-Hermitian subspace**, the fixed-point set of the anti-Hermitian conjugation $\flat$ (equivalently, the eigenspace of the Hermitian conjugation ${}^{*}$ with eigenvalue $-1$). The subspace $\mathbb{B}_{\Psi}$ is the **Hermitian subspace**, the fixed-point set of the Hermitian conjugation ${}^{*}$ (equivalently, its eigenspace with eigenvalue $+1$). The two are complementary: together they span $\mathbb{B}$, and their intersection is trivial. Every element of the algebra splits accordingly, $\tilde Q=\tilde Q_\Psi+\tilde Q_\Phi$, into its **material part** $\tilde Q_\Phi\in\mathbb{B}_{\Phi}$ and its **informational part** $\tilde Q_\Psi\in\mathbb{B}_{\Psi}$; an element of $\mathbb{B}_{\Phi}$ is its own material part, and an element of $\mathbb{B}_{\Psi}$ its own informational part. Both halves carry the one glyph of the element, and the sector mark alone separates them; the general element $\tilde Q$ takes no sector mark, since its sector depends on its value. The prime carries the reading rather than the sector: it marks the time in the material half $i q'_t\,e_t+\vec Q_\Phi$, and the space in the informational half $q_t\,e_t+i\vec Q_\Psi$, and the eight parameters are the same eight whichever half is read.

The two subspaces have distinct physical roles:

- **$\mathbb{B}_{\Phi}$ is the material sector.** Its coordinates are **$i q'_t$** (an imaginary temporal coordinate, a length) and **$q_x, q_y, q_z$** (three real spatial coordinates). It is the home of the four-vectors of relativistic physics. The imaginary time coordinate reflects a simple fact: time can be measured, but it cannot be touched, held, or moved through.
- **$\mathbb{B}_{\Psi}$ is the informational sector.** Its coordinates are **$q_t$** (a real temporal coordinate, a length) and **$i q'_{x}, i q'_{y}, i q'_{z}$** (three imaginary spatial coordinates). It is the home of the Hermitian operators, whose algebraic structure is that of a quantum-mechanical state space. The elements of $\mathbb{B}_{\Psi}$ carry quantum-informational content, in the sense established in the companion article on quantum physics: they are the states, observables, and measurement operators of a qubit. The name "informational sector" reflects this content. It is not a claim about entropy or any other thermodynamic property of the sector.

Written as elements of the algebra, each sector carries its own four real parameters: the parameter is the coordinate, and no conversion stands between them.

- **$\mathbb{B}_{\Phi}$**, the material sector, corresponding to the anti-Hermitian subspace:

    $$
    \tilde Q_\Phi = i q'_t\,e_t + \vec Q_\Phi = i q'_t\,e_t + q_x\vec e_x + q_y\vec e_y + q_z\vec e_z \in \mathbb{B}_{\Phi},
    $$

    with $q'_t$ the material temporal coordinate, a length, and $\vec Q_\Phi = q_x\vec e_x + q_y\vec e_y + q_z\vec e_z$ the material space.

- **$\mathbb{B}_{\Psi}$**, the informational sector, corresponding to the Hermitian subspace:

    $$
    \tilde Q_\Psi = q_t\,e_t + i\vec Q_\Psi = q_t\,e_t + i\bigl(q'_x\vec e_x + q'_y\vec e_y + q'_z\vec e_z\bigr) \in \mathbb{B}_{\Psi},
    $$

    with $q_t$ the informational temporal coordinate, a length, and $\vec Q_\Psi = q'_x\vec e_x + q'_y\vec e_y + q'_z\vec e_z$ the informational space.

Where the prime falls is what distinguishes the sectors: in $\mathbb{B}_{\Phi}$ it is the **scalar** $q'_t$ (the time), in $\mathbb{B}_{\Psi}$ the **three vectors** $q'_\eta$ (the space). This is why the prime is not attached to a sector — $q'_t$ is a material parameter, $q'_\eta$ an informational one — and it is the one rule that makes the two sectors mirror images of each other. The complex structure is then visible as a count: the material sector has three real spatial directions and one imaginary temporal direction, the informational sector three imaginary spatial directions and one real temporal direction.

## The Complex Coordinates

Writing the biquaternion coordinate in terms of its material and informational parts,

$$
\tilde{Q} = \underbrace{(i q'_t)\,e_t + (q_x\,\vec e_x + q_y\,\vec e_y + q_z\,\vec e_z)}_{=\,\tilde Q_\Phi\,\in\,\mathbb{B}_{\Phi}} \;+\; \underbrace{(q_t)\,e_t + (i q'_{x}\,\vec e_x + i q'_{y}\,\vec e_y + i q'_{z}\,\vec e_z)}_{=\,\tilde Q_\Psi\,\in\,\mathbb{B}_{\Psi}},
$$

Written on its own part, each of the two blocks is four real numbers in the four slots: the material block is $\tilde Q_\Phi = i q'_t\,e_t+\vec Q_\Phi$ with $\vec Q_\Phi=q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$, and the informational block is $\tilde Q_\Psi = q_t\,e_t+i\vec Q_\Psi$ with $\vec Q_\Psi=q'_x\vec e_x+q'_y\vec e_y+q'_z\vec e_z$. The two blocks take four parameters each, and between them they take the eight of the element.

Each coefficient is shown in its two guises: the complex coefficient $Q_\mu$ itself, and the pair of parameters it carries, $q_\mu$ from one sector and $q'_\mu$ from the other, the two times in metres like the two spaces.

The **real parameters** $(q'_t,q_x,q_y,q_z)$ describe the material sector, and the **real parameters** $(q_t, q'_{x}, q'_{y}, q'_{z})$ describe the informational sector. Each sector is four-dimensional, and the full complexified spacetime is the direct sum of the two.

**The same decomposition, read on the coordinates.** The algebraic split of the opening and the coordinate values above are the same statement twice: matching the two writings coefficient by coefficient identifies each of the eight parameters with one coordinate of the element, the two times in the same unit as the three spaces. The eight numbers are one set read once: the parameters are the coordinates, and a part of the element is read by reading its four slots.

The unprimed parameter is throughout the **real part** of the complex coefficient and the primed one its **imaginary part**. It is worth noting which is which for the temporal coefficient: the real part of $Q_t$ is $q_t$, an informational coordinate, while its imaginary part $q'_t$ is the material one. The two sectors take disjoint halves of the eight parameters — $\mathbb{B}_{\Phi}$ takes $q'_t$ together with the three $q_\eta$, $\mathbb{B}_{\Psi}$ takes $q_t$ together with the three $q'_\eta$ — so four complex coefficients and eight real parameters carry exactly the same information.

**One element, one point, one label.** The eight parameters split four and four between the parts, and the split gives the element its second interpretation. Read on its material part, the element is a spacetime event, $\tilde Q_\Phi=i q'_t\,e_t+\vec Q_\Phi$, and its informational part $\tilde Q_\Psi$ supplies the four parameters of its **internal label**; read on its informational part, it is an event of the informational sector, $\tilde Q_\Psi=q_t\,e_t+i\vec Q_\Psi$, and its material part $\tilde Q_\Phi$ supplies the four parameters of its **spacetime label**. The four complex coefficients therefore read as a spacetime point together with the matching point of the other sector, and no coefficient is idle: each carries one coordinate of each sector at once. That is why one element of $\mathbb{B}$ serves both as a four-vector and as a state — the two interpretations use the two halves of the same four coefficients.

## What the Framework Achieves

The main result of the framework so far is that the biquaternion algebra **contains, as a matter of algebra, the structures required for both relativity and quantum physics**. They are not incompatible sectors of physics that must be glued together; they are two aspects of the same biquaternion space, appearing in its two complementary subspaces. Two further classifications are read from that algebra and developed elsewhere: the **reality condition** that fixes the type of a particle, and the split of the internal symmetry into a compact part carrying a discrete charge and a non-compact part carrying a continuous label. Both are treated in *The Physical Interpretation of the 12 Products*; the antilinear structure behind them is *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*.

### Relativity in $\mathbb{B}_{\Phi}$

A point of the material sector is written in the coordinates of relativistic physics as

$$
\tilde Q_\Phi = i q'_{t}\,e_t + \vec Q_\Phi = i q'_{t}\,e_t + q_x\,\vec e_x + q_y\,\vec e_y + q_z\,\vec e_z \in \mathbb{B}_{\Phi},
$$

the imaginary temporal coordinate $i q'_{t}$, a length, together with the three real spatial coordinates $\vec Q_\Phi = q_x\,\vec e_x + q_y\,\vec e_y + q_z\,\vec e_z$.

The material sector $\mathbb{B}_{\Phi}$ carries the four-vectors of relativistic physics: position, velocity, momentum, force, potential, current. The **proper orthochronous Lorentz group** $SO^+(1,3)$ is realized through its double cover $SL(2,\mathbb{C})$, which is the **group of biquaternions of unit norm** in $\mathbb{B}$; its elements are the Lorentz rotors, written $\tilde U_{\mathrm{lor}}$:

$$
SL(2,\mathbb{C}) \;\cong\; \{\tilde U_{\mathrm{lor}} \in \mathbb{B} : \tilde U_{\mathrm{lor}}\tilde U_{\mathrm{lor}}{}^{\natural} = e_t\}.
$$

The norm $\langle\cdot\rangle_{\natural}$ and the quaternion conjugate ${}^{\natural}$ that appear here are defined in *The Metric*, later in the article.

This group **acts** on the material sector by the **rotor conjugation**

$$
\tilde Q_\Phi \;\longmapsto\; \tilde U_{\mathrm{lor}}\,\tilde Q_\Phi\,\tilde U_{\mathrm{lor}}{}^{*}.
$$

The group itself lives in the full algebra $\mathbb{B}$ (since $\mathbb{B}_{\Phi}$ is not closed under multiplication and cannot carry a group structure). The four-vectors it acts on live in $\mathbb{B}_{\Phi}$. The different types of Lorentz transformation have rotors in different subspaces: pure boosts have rotors in $\mathbb{B}_{\Psi}$ (they are Hermitian), pure spatial rotations have rotors in $\mathbb{B}_{H}$ (they are real quaternions), and general Lorentz transformations have rotors in the full algebra. The rotation rotors sit in the **real half** $\mathbb{B}_{H}$, whose four coefficients are all real, a subalgebra in its own right; the **imaginary half** $\mathbb{B}_{iH}$, whose four coefficients are purely imaginary, is its partner in $\mathbb{B}=\mathbb{B}_{H}\oplus\mathbb{B}_{iH}$. That split crosses the material–informational one: the scalar of $\mathbb{B}_{\Phi}$ and the vector of $\mathbb{B}_{\Psi}$ come from $\mathbb{B}_{iH}$.

The relativistic wave equations — **Maxwell's equations** and the **Dirac equation** — have natural biquaternion forms, as developed in the companion articles.

### Quantum Physics in $\mathbb{B}_{\Psi}$

A point of the informational sector is written in its own coordinates as

$$
\tilde Q_\Psi = q_t\,e_t + i\vec Q_\Psi = q_t\,e_t + (i q'_{x})\,\vec e_x + (i q'_{y})\,\vec e_y + (i q'_{z})\,\vec e_z \in \mathbb{B}_{\Psi},
$$

the real temporal coordinate $q_t$, a length, together with the three imaginary spatial coordinates $i q'_{x}, i q'_{y}, i q'_{z}$.

The informational sector $\mathbb{B}_{\Psi}$ is, exactly, the **Hermitian part** of the operator algebra of a two-state quantum system: its elements are the observables, and they generate the full matrix algebra. The subspace is a real vector space and not a subalgebra: the product of two Hermitian elements is not in general Hermitian, and only its symmetric half stays in the sector. The operator product is therefore read through the two slots (*The Two Slots of One Product*) and not as a multiplication internal to $\mathbb{B}_{\Psi}$. This is established in the companion article *Quantum Physics in Biquaternionic Form*, and it can be summarized as follows. The Hermitian form $\langle\cdot,\cdot\rangle_{*}$ that appears below is defined in *The Metric*, later in the article.

- The **elements** of $\mathbb{B}_{\Psi}$, of the form $\tilde Q_\Psi = q_t\,e_t + i\vec Q_\Psi$ with $\vec Q_\Psi = q'_x\vec e_x + q'_y\vec e_y + q'_z\vec e_z$ and $q_t, q'_x, q'_y, q'_z \in \mathbb{R}$ — the scalar coefficient real and the vector coefficients imaginary, which is the usual writing of quantum physics — are the observables (they are automatically Hermitian by definition of $\mathbb{B}_{\Psi}$), with spectral decomposition in terms of idempotents. The correspondence runs both ways: the Hermitian elements of $\mathbb{B}$ are exactly the elements of $\mathbb{B}_{\Psi}$, and the observables of the two-state system are exactly the Hermitian $2\times2$ matrices, so nothing outside $\mathbb{B}_{\Psi}$ is an observable and no element of $\mathbb{B}_{\Psi}$ is idle. The four parameters are then the four numbers a measurement of that observable reports: the two outcomes are $q_t \pm \lvert\vec Q_\Psi\rvert$, so $q_t$ is their mean and the vector $\vec Q_\Psi$ fixes their half-splitting.
- The **idempotents** in $\mathbb{B}_{\Psi}$, of the form $\tilde\Pi_{1,2}(\vec u) = \tfrac{1}{2}(e_t \pm i\vec u)$ with $\vec u$ a unit pure real quaternion, are the pure states of a qubit. They parametrize the Bloch sphere $S^2$.
- The **positive elements** in $\mathbb{B}_{\Psi}$ normalised by $\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}=\tfrac12\langle e_t\rangle_{*}$, of the form $\tilde{Ϛ}_{\Psi} = \tfrac{1}{2}(e_t + i\vec s_{\Psi})$ with $|\vec s_{\Psi}| \leq 1$, are the mixed states (trace one in the $2\times2$ image), parametrizing the Bloch ball.
- The **two-sided operation** $\tilde{Ϛ}_{\Psi} \mapsto \tilde\Pi\tilde{Ϛ}_{\Psi}\tilde\Pi/\langle\tilde\Pi\tilde{Ϛ}_{\Psi}\tilde\Pi,e_t\rangle_{*}$ gives the projective measurement and state update (the denominator normalises the post-measurement state; its $2\times2$ reading is $2\,\mathrm{Sc}(\tilde\Pi\tilde{Ϛ}_{\Psi}\tilde\Pi)$).
- The **$*$-unitary elements** of $\mathbb{B}$, and their conjugation action $\tilde{Ϛ}_{\Psi} \mapsto \tilde Q\tilde{Ϛ}_{\Psi}\tilde Q^{*}$, give the reversible evolution.
- The distinction between **reversible evolution** and **irreversible measurement** is a property of the acting element ($*$-unitary vs. idempotent), not an additional postulate.

The operator algebra of quantum physics, its state space, its Born rule, and its measurement rule are all **structural consequences** of the algebra of $\mathbb{B}_{\Psi}$. They are not imposed from outside. The two-state formalism at large is *Quantum Physics in Biquaternionic Form*; the derivation of the Born rule, and its comparison with the postulate it replaces, are *The Born Rule from the Hermitian Form — Derivation and Comparison*; the states that the indefinite fourth product cannot normalise are *The Physical Interpretation of the 12 Products*; and the decoherence of a measurement is *Decoherence as Idempotent Projection*.

### The Shared Home

The most significant feature of the framework is that **relativity and quantum physics share the same biquaternion space**. The Lorentz group is realized (via its double cover $SL(2,\mathbb{C})$) as the group of biquaternions of unit norm in $\mathbb{B}$, and the operator algebra of quantum physics is realized in the Hermitian subspace $\mathbb{B}_{\Psi}$. The two structures are not independent; they are aspects of the same biquaternion space.

This is the sense in which the framework is proposed as an alternative to the standard formulation: not as a modification of relativity or of quantum physics, but as a **common biquaternion space** on which both can be expressed.

### The Two Slots of One Product

Every product of the algebra reads two elements, one in each **slot**, and in the framework's two sesquilinear products the slots are not interchangeable: one is read plainly and the other through a conjugation. That asymmetry is the algebraic form of the two roles a quantum description pairs — an element and the adjoint of another — and it is the reason the Born weight above can be read as the scalar part of a product on the algebra rather than as a pairing imposed from outside. The four products, the two slots and their four interpretations are treated in *The Four General Products: Composition, Probability, Causality, Gauge*; the state and observable roles, the gauge action generated inside the algebra, and the chirality of that action are treated in *The Physical Interpretation of the 12 Products*.

**Four jobs, one grid.** The four products are read as the four jobs a relativistic quantum theory needs — composition, causality, probability and gauge — and each splits into a symmetric half and an antisymmetric half, so that the twelve products of the space are the four general products together with the two halves of each. What the algebra fixes is the grid and the signs; that these are the four jobs, and that the interpretation is exhaustive, is the framework's claim. The jobs are tabulated in *The Four General Products: Composition, Probability, Causality, Gauge*.

**The reading order.** The corpus is organised in four blocks. **Algebra** fixes the vocabulary: the elements, the twelve products, the four forms and the four norms. **Topology** reads the group of invertibles, the cone and the orders. **Analysis** reads the exponential, the logarithm and the poles. **Geometry** reads the sectors, the frames, the bundles and the null quadric. The physical articles follow the same order: the algebra first, then the material and informational sectors, then the processes and the spectra. A reader who wants one path through the series can take the algebra block, then *The Material Sector: Four-Vectors, Interval and Lorentz Action* and *The Informational Sector: States, Observables and Probability*, then the analysis of the exponential, and then the spectral articles.

## The Metric

The quadratic form on the biquaternion algebra is the **biquaternion norm**

$$
\langle d\tilde{Q}\rangle_{\natural} = d\tilde{Q}\, d\tilde{Q}^{\natural} = \sum_{\mu\in\{t,x,y,z\}} (dQ_\mu)^2,
$$

where ${}^{\natural}$ is the **quaternion conjugate**, the involution that reverses the three quaternion directions and leaves the complex coefficients alone: $e_t^{\natural}=e_t$, $\vec e_\eta^{\natural}=-\vec e_\eta$, hence $d\tilde{Q}^{\natural} = dQ_t\,e_t - dQ_x\,\vec e_x - dQ_y\,\vec e_y - dQ_z\,\vec e_z$. A second conjugation appears later in the article, the **bar**, and it acts on the other factor: it conjugates the complex coefficients and leaves the quaternion basis alone, $\overline{\tilde{Q}} = \sum_\mu \overline{Q_\mu}\,e_\mu$. The two are different operations on the same element, and the norm uses the first. The quaternion conjugate is what produces the sum of squares: the plain square $d\tilde{Q}\,d\tilde{Q}$ is not $\sum_\mu (dQ_\mu)^2$. Expanding in real and imaginary parts,

$$
(dQ_t)^2 = \bigl((dq_t)^2 - (dq'_t)^2 + 2i\,dq_t\,dq'_t\bigr),\qquad (dQ_\eta)^2 = (dq_\eta)^2 - (dq'_\eta)^2 + 2i\,dq_\eta\,dq'_\eta .
$$

The **real part** of $\langle d\tilde{Q}\rangle_{\natural} = \sum_\mu (dQ_\mu)^2$ reproduces the Lorentzian interval on the material sector and the mirror interval on the informational one. The minus sign in the time–time component arises algebraically from $i^2 = -1$ in the imaginary time coordinate $i q'_t$, not from an independently postulated metric. The **imaginary part** couples the material and informational sectors through cross terms.

Because each part retains only half of the eight parameters, the same biquaternion norm reads off as a real quadratic form on each, and it is again worth having both writings. On the material part, where $d\tilde Q=d\tilde Q_\Phi$ and only $dq'_t$ and the $dq_\eta$ are non-zero,

$$
\langle d\tilde Q_\Phi\rangle_{\natural} = -(dq'_t)^2 + dq_x^2 + dq_y^2 + dq_z^2
$$

the Minkowski interval, one negative direction and three positive. On the informational part, where $d\tilde Q=d\tilde Q_\Psi$ and only $dq_t$ and the $dq'_\eta$ are non-zero,

$$
\langle d\tilde Q_\Psi\rangle_{\natural} = dq_t^2 - (dq'_x)^2 - (dq'_y)^2 - (dq'_z)^2
$$

the mirror interval, one positive direction and three negative. The two are exchanged by $i$ — left multiplication by $i$ carries $\mathbb{B}_{\Phi}$ onto $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Psi}$ onto $\mathbb{B}_{\Phi}$ — and the sign of the form reverses with them, $\langle i\tilde{Q}\rangle_{\natural} = -\langle\tilde{Q}\rangle_{\natural}$. In both cases the null cone — each sector's part of the zero divisor set of the algebra, discussed in the companion articles — has the same two interpretations:

$$
\mathbb{B}_{\Phi}:\;\; (dq'_t)^2 = dq_x^2 + dq_y^2 + dq_z^2, \qquad
\mathbb{B}_{\Psi}:\;\; dq_t^2 = (dq'_x)^2 + (dq'_y)^2 + (dq'_z)^2 .
$$

Each of these is one equation in the four parameters of its sector, with the temporal parameter squared against the three spatial ones.

**Where the minus comes from.** Read as a form on $\mathbb{C}$, the same norm has the unit metric $\delta_{\mu\nu}=(1,1,1,1)$ for its coefficient tuple, $\langle\tilde{Q}\rangle_{\natural}=\sum_\mu Q_\mu^2$, with every entry $+1$ and the four directions of $\mathbb{B}$ on an equal footing: there is no minus sign in the complex form itself, and none is needed, since a complex coefficient can carry the sign. The minus appears only when a *real* coordinate is placed on a direction whose coefficient carries a factor of $i$, as it is in each of the two real sectors above. The Minkowski signs are therefore not an independent input of the theory: it is what the algebra's own form looks like once the material time is written $i q'_t$, with $i^2=-1$ supplying the minus. The metric is *The Unit Metric in the Biquaternion Universe*, which also states the absorbed alternative $g=\mathrm{diag}(-1,1,1,1)$ and why the series refuses it. The norm as a complex form, and the four forms it takes, are treated in *Algebra and Element Conventions*; the local complex structure behind the choice of $i$ is *The Local Complex Structure and the Speed of Light*.

**One root, three names.** The minus of the interval is one case of a single algebraic fact: the equation $\tilde{Q}^{2}=\lambda e_t$ in the plain product has three distinguished radicands: a root of $-1$ is a complex structure, a root of $0$ a nilpotent of the light cone, and a root of $+1$ an involution. The central root $i$ is the scalar imaginary that writes $i q'_t$; a non-central root is an internal complex structure of the real space, not a change of the algebra's scalars. The three answers are one equation, and the subspace in which the root is sought decides the physical name. Read on the elements, the same observation gives the massive, the massless and the spacelike as the interior, the boundary and the exterior of one quadric. The trichotomy is *Roots, Idempotents and Observables* and *The Zero-Divisor Cone and the Massless Spectrum*; the boundary is *The Light Cone as the Biquaternion Zero-Divisor Cone*; and the mass shell is *The Physical Interpretation of the 12 Products*.

### The Two Forms of One Element

The body has so far developed one form, the biquaternion norm $\langle\cdot\rangle_{\natural}$. The second is the **Hermitian form** on $\mathbb{B}_{\Psi}$, $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}=\sum_\mu Q_{1\mu}\overline{Q_{2\mu}}$, the sum of the four coordinates of one element against the conjugates of the other — the bar, the coefficient conjugation, and not the quaternion conjugate ${}^{\natural}$ of the norm. The two forms are two interpretations of one element, and they part company at once: the norm is complex and vanishes on the null cone, the Hermitian form is positive and vanishes only at the origin. At $\tilde{Q}=e_t+i\vec e_z$ the two already differ: the norm is $\langle\tilde{Q}\rangle_{\natural}=0$, while the Hermitian form is $\langle\tilde{Q},\tilde{Q}\rangle_{*}=2$. The same element is a null direction for the interval and a state of positive weight. The norm is the **interval**, whose zero set is the light cone; the Hermitian form is the **probability weight**, the form the Born rule draws on. One element carries both, and the framework's account of why the causal and the probabilistic structures coexist is that they are two forms on one biquaternion space and not two algebras. The form read as a product, and the positivity and the rank it carries, are treated in *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*; the probability reading is *The Informational Sector: States, Observables and Probability*.

## The Vacuum Limit

In vacuum the local speed of light is the constant $c_0$; in a material medium it is $c=1/\sqrt{\epsilon\mu}$ and varies from point to point. Neither value enters the coordinate, because the four coefficients are lengths in either case. The identification $r'_t\mapsto i r'_t$ is the same at every point; what is local is its scale, and the scale is read through the one conversion the scheme still uses, $t=q'_t/c$, wherever a clock is compared with a length. The writing of an element is therefore the same in vacuum and in a medium, in the same spirit as the metric of general relativity, which is local while the coordinates of a chart are not.

## Status and Open Questions

The framework is a **research programme**, not a finished theory. The algebraic results — that $\mathbb{B}_{\Phi}$ carries the four-vectors of relativity and that $\mathbb{B}_{\Psi}$ carries the operator algebra of quantum physics — are established mathematics, and the identifications with the physical theories are developed in the companion articles.

What is not established is whether the framework has consequences beyond a reformulation of known physics. Six questions are recorded below. Each has gained work in the companion articles, and none is closed. Each entry states what has been built and what is missing.

1. **Physical reality of the biquaternionic structure.** Sharpened, not answered. *The Empirical Status of the Biquaternion Framework* finds the framework empirically equivalent to standard physics on every domain developed so far, and states why: every quantity that the algebra fixes is fixed identically by the standard theory, so a test requires an input the algebra does not contain — a scale, a coupling, or a selection principle. *The Parameter Count as the Measure of the Framework's Boundary* turns the same finding into a count, with three grades of fixing — a value, a relation, a selection — and records that the framework fixes none of the nineteen Standard Model parameters. What remains is an argument that the algebra is selected rather than convenient. No article in the corpus supplies one.

2. **Coupling between the two sectors.** Built as maps and as thermodynamics, open as dynamics. Neither sector is an algebra in its own right: the product of two Hermitian elements is Hermitian exactly when they commute, and the product of two material elements is material exactly when they anticommute, so a composition cannot be written inside one sector and read off in the other (*The Sector Map and Its Exact Parts*). The map the corpus does have, multiplication by the scalar imaginary $J(\tilde Q)=i\tilde Q$, is exact on the Lorentz congruence, negates the quaternionic norm and preserves the Hermitian form. The **square** is still the minimal algebraic coupling: for a material element $\tilde Q_\Phi^{\natural}\tilde Q_\Phi=\langle\tilde Q_\Phi\rangle_{\natural}e_t$ with $\langle\cdot\rangle_{\natural}$ real, and the real scalar line lies in $\mathbb{B}_{\Psi}$, so squaring is a map $\mathbb{B}_{\Phi}\to\mathbb{B}_{\Psi}$ supplied by the product and not by hand. The exchange has also been written as thermodynamics: erasure costs at least one bit (*Landauer's Principle and the Material–Informational Exchange in Biquaternionic Form*), the demon's cycle closes (*Maxwell's Demon and the Informational Sector in Biquaternionic Form*), and the two sector times are read against each other (*Relational Time from the Sector Exchange: The Material and Informational Clocks*). What is still missing is a coupling with a field, an action and a constant. The empirical-status article names it as the framework's largest gap.

3. **Extension to many qubits and to quantum field theory.** Both built, with named remainders. The many-qubit side composes the defining module and not the element: $n$ qubits are $S^{\otimes n}=\mathbb{C}^{2^n}$, the partial sector label provably does not descend, the observables are exactly the Hermitian part of $M_{2^n}(\mathbb{C})$, and the entanglement articles develop the concurrence, the three-qubit GHZ and W classification, monogamy and the CKW inequality, discord, and the area law (*Composite Systems and the Multi-Qubit Extension*; *The Multi-Qubit Split, I*; *The Multi-Qubit Split, II*). The field-theoretic side is built for the free fields: the Klein–Gordon, Dirac, Maxwell, Proca and Rarita–Schwinger fields are canonically quantized, the graviton field is quantized in the linearized sector, and the scalar and fermionic Fock spaces are written in the algebra. Three items inside the quantized Dirac field stay open: whether a $\mathbb{B}$-intrinsic Lagrangian with a scalar pairing reproduces the normal-ordered observables of the parent, whether the parity grading can be carried inside the algebra for the whole field and not only for one mode, and whether a conserved current exists that carries no fixed frame unit (*The Quantized Dirac Field in Biquaternionic Form*).

4. **Relativistic quantum theory.** Built for one particle and for the free field, open for the interacting theory. The relativistic qubit is the defining module with the left action of $SL(2,\mathbb{C})$ and the little-group Wigner rotation (*The Relativistic Qubit in Biquaternionic Form*). The Dirac equation is written in biquaternion form with its plane-wave solutions, its non-relativistic limit and its discrete symmetries; the hydrogen spectrum is reproduced in the relativistic case; and the anomalous magnetic moment is carried by the bivector part of the electromagnetic vertex. That vertex is the one-particle object transcribed into the algebra, and the value $a=\alpha/2\pi$ is transcribed with it; an intrinsic biquaternion three-point function is not constructed (*The Anomalous Magnetic Moment in Biquaternionic Form*). What is missing is an interacting theory that the algebra derives rather than imports: the gauge principle is an input of the corpus, and the radiative corrections enter with it.

5. **Curved spacetime.** Kinematics carried, dynamics absent. A general Lorentzian metric is carried by a frame field of material-sector elements, the algebra supplies the pointwise $SL(2,\mathbb{C})$ and its Lie algebra, and a curved biquaternion Dirac operator has been built with its Lichnerowicz square; the Kerr–Schild class is the orbit of the flat form under a null shear, which is square-zero because a null element is a zero divisor; linearized gravity and gravitational waves are written in the algebra; and the KMS flow and the Hawking temperature are carried as standard results (*Curved Spacetime and the Biquaternion Framework*). What is missing is the theory: no action, no field equation, no Einstein equation and no selection of a metric. The gravitating rank-two tensors are not the framework's four-vectors, global and topological structure lie outside a pointwise algebra, and the informational sector has no curved-space treatment at all. *The Einstein Field Equations under the Biquaternion Framework — A Research Agenda* records that even the linearized equation is transcribed rather than derived.

6. **Empirical contact.** No measurement today separates the framework from standard physics. *The Empirical Status of the Biquaternion Framework* takes each candidate test in turn — modified dispersion, the local complex structure, birefringence, a second light cone, quaternionic deviations, dimensionless relations — and shows that none is a test, because none depends on a quantity the algebra fixes and standard physics does not. A test would need a measured cross-sector effect, or a bound on one, at a stated scale. Without it the framework is reproduced by every experiment and tested by none.

From that shared foundation, the programme investigates where this algebraic unity leads next: whether a cross-sector coupling can be given a field and an action, whether the interaction terms of the quantized fields can be derived instead of imported, and whether a local complex structure can be given a curved spacetime with a dynamics.

The framework is offered as a structural intuition: that the two natural subspaces of the biquaternion algebra have distinct physical roles — one material, one informational — and that the algebra $\mathbb{B}$ is the natural home in which both relativity and quantum physics are expressed. The local speed of light $c = 1/\sqrt{\epsilon\mu}$ is the local scale of the complex structure. Since the four coefficients are lengths, that scale does not appear in the element itself; it appears in the conversion $t=q'_t/c$, and in the numbers a clock and a ruler report of the same point. The vacuum case $c=c_0$ is the special case of it, in the same way that special relativity is a local approximation of general relativity.

**Many qubits.** One qubit is the module $S=\mathbb{C}^2$, and $\mathbb{B}\cong M_2(\mathbb{C})$ is its endomorphism algebra. Two qubits are $S\otimes S=\mathbb{C}^4$, whose endomorphism algebra is $M_4(\mathbb{C})$, and that is not a biquaternion algebra. The sector label therefore does not survive the tensor product. The partial star does not descend, and the four corners collapse onto two spaces, the Hermitian and the anti-Hermitian parts of $M_4(\mathbb{C})$. One global bit remains. Nothing observable is lost, because the observables of $n$ qubits are exactly the Hermitian part of $M_{2^n}(\mathbb{C})$. The alternating form of the one-qubit space tensors without obstruction, and its tensor square gives the concurrence. The same module carries the Bell basis, the reduced states and their entropy, the three-qubit classification, monogamy, discord and the area law. The construction is *Composite Systems and the Multi-Qubit Extension*, the boundary is *The Multi-Qubit Boundary*, and the two theorems are *The Multi-Qubit Split, I* and *The Multi-Qubit Split, II*.

## Physical Readings

Two interpretations of the introduction are worth separating. Read as a statement about invariance, the universe of the article is the sesquilinear pair: a change of the local complex structure moves the interval and the composition and leaves the probability form, the gauge calibration and the zero-divisor cone where they were (*Algebra and Element Conventions*). Read in time, its two sectors are two clocks reading one hand: the material time and the informational time are the two projections of one central coordinate, so each sector's time is read against the phase of the other (*Relational Time from the Sector Exchange: The Material and Informational Clocks*). Four further readings can be named.

- **Amplitude interpretation.** Each complex coefficient $Q_\mu$ is one complex number, that is, a magnitude and a phase, so the arena of the framework is complex before any quantum interpretation is imposed: the two sectors are read as the real and the imaginary halves of one amplitude, and an element is a point of the complexified spacetime together with its conjugate amplitude data. Boundary: the interpretation names the shape of the coefficient and supplies neither a quantisation nor a measurement rule.
- **State-preparation interpretation.** The central map $\tilde Q_\Psi=-\tfrac{i}{2}\tilde Q_\Phi$ carries a material four-vector to an informational element, and on the normalised slice of the future cone to a state: the four-vector $i q'_t\,e_t+\vec Q_\Phi$ is carried to $\tfrac12(q_t\,e_t+i\vec Q_\Psi)$ with $q_t=q'_{t}$ and $\vec Q_\Psi=-\vec Q_\Phi$, so that $2\,\mathrm{Sc}(\tilde Q_\Psi)=q_t=q'_{t}$ and $\langle\tilde Q_\Psi\rangle_{\natural}=-\tfrac14\langle\tilde Q_\Phi\rangle_{\natural}$, so on the slice $q'_{t}=1$ of the length unit, with $\lvert\vec Q_\Phi\rvert\le1$, it is the Hermitian state $\tilde{Ϛ}_{\Psi}=\tfrac12(e_t+i\vec s_{\Psi})$ with $\vec s_{\Psi}=-\vec Q_\Phi$ and $|\vec s_{\Psi}|\le1$. Boundary: the map is the dictionary of *The Bloch Ball as the Normalised Slice of the Future Light Cone*, which owns it, and the interpretation names a preparation and not a dynamics.
- **Cross-sector coupling by the square.** For a material element the quaternionic square is the interval itself, $\tilde Q_\Phi^{\natural}\tilde Q_\Phi=\langle\tilde Q_\Phi\rangle_{\natural}e_t$ with $\langle\cdot\rangle_{\natural}$ real, and the real scalar line lies in $\mathbb{B}_{\Psi}$: squaring is therefore one algebraic map $\mathbb{B}_{\Phi}\to\mathbb{B}_{\Psi}$, the minimal instance of the coupling asked for in question 2 above, supplied by the product rather than added by hand. The product of *two* material elements is not in general informational, while the *square of one* is. Boundary: one map, with image the real scalar line, and no dynamics; the identity is owned by *The Physical Interpretation of the 12 Products*, and its grid-level pointer is *The Four General Products: Composition, Probability, Causality, Gauge*.
- **One locus, two lists.** The norm's zero set $\langle\tilde{Q}\rangle_{\natural}=0$ is the light cone of the material sector and it is also the locus on which the pure states of the informational sector sit: the idempotents $\tilde\Pi=\tfrac12(e_t\pm i\vec u)$ have $\langle\tilde\Pi\rangle_{\natural}=0$. The causal boundary and the list of pure states are one algebraic locus read twice, the zero-divisor cone. Boundary: the interpretation identifies sets, and it does not make every null element a pure state, the null cone being strictly larger than the set of idempotents; the state side is *The Physical Interpretation of the 12 Products*, and the cone itself *The Light Cone as the Biquaternion Zero-Divisor Cone*.

## Summary

The framework is stated in one sentence: the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ is the common biquaternion space of relativity and quantum physics, and its two natural real subspaces carry the two theories. The **anti-Hermitian subspace** $\mathbb{B}_{\Phi}$ carries the four-vectors of relativity, the material sector, in the coordinates $(i q'_t,q_x,q_y,q_z)$; the **Hermitian subspace** $\mathbb{B}_{\Psi}$ carries the operator algebra of quantum physics, the informational sector, in the coordinates $(q_t,i q'_{x},i q'_{y},i q'_{z})$. Multiplication by $i$ exchanges the two.

Both sectors are written in the one biquaternion space. A material element is $\tilde Q_\Phi=i q'_t\,e_t+\vec Q_\Phi$ and an informational element is $\tilde Q_\Psi=q_t\,e_t+i\vec Q_\Psi$, with $\vec Q_\Phi = q_x\,\vec e_x+q_y\,\vec e_y+q_z\,\vec e_z$ and $\vec Q_\Psi = q'_{x}\,\vec e_x+q'_{y}\,\vec e_y+q'_{z}\,\vec e_z$; the two are the parts of one element, $\tilde Q=\tilde Q_\Psi+\tilde Q_\Phi$, and the norm $\langle\tilde{Q}\rangle_{\natural}=\sum_\mu Q_\mu^2$ is the interval on $\mathbb{B}_{\Phi}$, one negative direction there, and the Hermitian form $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}=\sum_\mu Q_{1\mu}\overline{Q_{2\mu}}$ is the probability weight on $\mathbb{B}_{\Psi}$. The Lorentz rotors are the unit-norm elements $\tilde U_{\mathrm{lor}}$ with $\tilde U_{\mathrm{lor}}\tilde U_{\mathrm{lor}}{}^{\natural}=e_t$, acting by conjugation; the idempotents $\tilde\Pi_{1,2}(\vec u)=\tfrac12(e_t\pm i\vec u)$ are the pure states of the informational sector; and the observables are the Hermitian elements $\tilde Q_\Psi=q_t\,e_t+i\vec Q_\Psi$ with $q_t$ real.

The framework is a research programme, not a finished theory. The algebraic identifications above are established mathematics; what is open is whether the framework has consequences beyond a reformulation of known physics. Six questions are recorded, each with what the corpus has built and what it still lacks: the physical reality of the biquaternionic structure, given a criterion and not an answer; a coupling between the sectors with a dynamics, the algebraic square and the thermodynamic exchange being built; the extension to many qubits and to quantum field theory, built on the module route with the sector label provably lost in composition; a relativistic quantum theory, built for one particle and the free field and open for the interaction; curved spacetime, where the kinematics is carried and the dynamics is absent; and empirical contact, where no measurement today separates the framework from standard physics. The local speed of light $c=1/\sqrt{\epsilon\mu}$ is the local scale of the complex structure; it stays out of the element, whose four coefficients are lengths, and enters only the conversion between the length coordinate and the second.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H} \cong M_2(\mathbb{C})$ | Biquaternion algebra |
| $S=\mathbb{C}^2$, $S^{\otimes n}=\mathbb{C}^{2^n}$ | Defining module of $\mathbb{B}$, carrier of one qubit; $n$ qubits are its $n$-th tensor power, whose endomorphism algebra is $M_{2^n}(\mathbb{C})$ |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\tilde{Q} = Q_t e_t + \vec Q = \sum_\mu Q_\mu e_\mu$ | General biquaternion (eight real parameters), with $\vec Q = Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ its vector part |
| $Q_\mu = q_\mu+iq'_\mu$ | Complex coefficient: $q_\mu$ its real part (the coefficient of $e_\mu$), $q'_\mu$ its imaginary part (the coefficient of $ie_\mu$); the four coefficients are lengths, and no factor of $c$ stands on the time |
| $\tilde Q = \tilde Q_\Psi + \tilde Q_\Phi$ | The split into the informational part $\tilde Q_\Psi$, Hermitian, and the material part $\tilde Q_\Phi$, anti-Hermitian |
| $\tilde Q_\Phi = i q'_t\,e_t + \vec Q_\Phi = i q'_t\,e_t + q_x\vec e_x + q_y\vec e_y + q_z\vec e_z$ | Material element, with $\vec Q_\Phi=q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$ its vector part |
| $\tilde Q_\Psi = q_t\,e_t + i\vec Q_\Psi = q_t\,e_t + i(q'_{x}\,\vec e_x+q'_{y}\,\vec e_y+q'_{z}\,\vec e_z)$ | Informational part, Hermitian, with $\vec Q_\Psi=q'_x\vec e_x+q'_y\vec e_y+q'_z\vec e_z$ its vector part; $q_t$ is real, the three $q'_\eta$ are imaginary, and the four are the informational coordinates |
| $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$ | Biquaternion norm; its coefficient tuple is the unit metric $\delta_{\mu\nu}=(1,1,1,1)$, the identity, in every frame; the interval it gives on the real material sector has one negative direction |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*} = \sum_\mu Q_{1\mu}\overline{Q_{2\mu}}$ | Hermitian form, positive definite; the probability weight, $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{*} = \sum_\mu\lvert Q_{2\mu}\rvert^{2}$; the coefficient of $e_t$ in $\tilde{Q}\tilde{Q}^{*}$ |
| ${}^{\natural}$ | Quaternion conjugate: reverses the quaternion basis, $e_t^{\natural}=e_t$ and $\vec e_\eta^{\natural}=-\vec e_\eta$, and leaves the complex coefficients $Q_\mu$ untouched; the conjugation of the norm, $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural}$ |
| $\overline{\cdot}$ | Bar, the coefficient conjugation: conjugates each complex coefficient $Q_\mu$ and leaves the quaternion basis untouched, $\overline{\tilde{Q}} = \sum_\mu \overline{Q_\mu}\,e_\mu$; the conjugation of the Hermitian form, $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*} = \sum_\mu Q_{1\mu}\overline{Q_{2\mu}}$ |
| ${}^{*} = \overline{\cdot}\circ{}^{\natural}$ | Hermitian conjugation: conjugates both factors, $\tilde{Q}^{*} = \overline{Q_t}e_t - \overline{Q_x}\vec e_x - \overline{Q_y}\vec e_y - \overline{Q_z}\vec e_z$; the conjugation that defines the two sectors, the fixed points of ${}^{*}$ being $\mathbb{B}_{\Psi}$ |
| ${}^{\flat} = -{}^{*}$ | Anti-Hermitian conjugation: the star composed with the central sign, $\tilde{Q}^{\flat} = -\tilde{Q}^{*}$, of which the material sector $\mathbb{B}_{\Phi}$ is the fixed-point set |
| $\mathbb{B}_{\Phi}$ | Anti-Hermitian subspace (material sector): coordinates $(i q'_t, q_x, q_y, q_z)$, parameters $q'_t, q_x, q_y, q_z$ |
| $\mathbb{B}_{\Psi}$ | Hermitian subspace (informational sector): coordinates $(q_t, i q'_{x}, i q'_{y}, i q'_{z})$, parameters $q_t, q'_x, q'_y, q'_z$ |
| $\mathbb{B}_{H}$ | Real quaternion subspace (home of the rotation rotors): the real half, all four coefficients real, fixed points of complex conjugation; a subalgebra |
| $\mathbb{B}_{iH}$ | Antiquaternion subspace: the imaginary half, all four coefficients purely imaginary, the partner of $\mathbb{B}_{H}$ in $\mathbb{B} = \mathbb{B}_{H} \oplus \mathbb{B}_{iH}$. This split crosses the $\mathbb{B}_{\Psi}/\mathbb{B}_{\Phi}$ split: the scalar of $\mathbb{B}_{\Phi}$ and the vectors of $\mathbb{B}_{\Psi}$ come from here |
| $\tilde\Pi_{1,2}(\vec u) = \tfrac{1}{2}(e_t \pm i\vec u)$ | Idempotent (pure state of the informational sector) |
| $\tilde{Ϛ}_{\Psi} = \tfrac{1}{2}(e_t + i\vec s_{\Psi})$, $\lvert\vec s_{\Psi}\rvert \le 1$ | Mixed state (positive, trace one). The Bloch vector $\vec s_{\Psi}$ carries no sector label and is distinct from the two vector parts $\vec Q_\Phi$ and $\vec Q_\Psi$ |
| $(q'_t,q_x,q_y,q_z)$ | Real coordinates of the material sector, all four in metres; the speed of light is a conversion and not a coordinate |
| $(q_t, q'_{x}, q'_{y}, q'_{z})$ | Real coordinates of the informational sector, all four in metres |
| $\tilde U_{\mathrm{lor}} \in \mathbb{B}$ with $\tilde U_{\mathrm{lor}}\tilde U_{\mathrm{lor}}{}^{\natural} = e_t$ | Lorentz rotor (unit-norm biquaternion) |
| $c = 1/\sqrt{\epsilon\mu}$ | Speed of light in the medium (local) |
| $c_0 = 1/\sqrt{\epsilon_0\mu_0}$ | Speed of light in vacuum (global constant) |
| $v$ | Particle or frame velocity |

## Further Reading

- Hermann Minkowski, "Space and Time" (1908), reprinted in *The Principle of Relativity* (Dover).
- Roger Penrose, *The Road to Reality* (Knopf, 2004), for the complex structure of spacetime.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection between Clifford algebras and the structures discussed here.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric algebra perspective on the same structures.
- Vladimir V. Kassandrov, "Relativistic Algebra of Space-Time and Algebrodynamics" (2006), for a related biquaternionic approach to complexified geometry.
