# __Introduction to the Biquaternion Universe__

## Core Proposal

The fundamental structure of the universe is a biquaternionic space, of which Minkowski space is a slice. A point in this complexified spacetime is an element of the **biquaternion algebra** $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$, written as a biquaternionic coordinate

$$
\tilde{R} = R_t e_t + R_x \vec e_x + R_y \vec e_y + R_z \vec e_z,
$$

where $e_t = 1$ and $\vec e_x, \vec e_y, \vec e_z$ are the quaternion units. The four coefficients $R_\mu$ are **complex**, and everything that follows turns on how each of them is split. Writing every coefficient as a real part plus $i$ times a real part,

$$
R_t = c\,(r_t + ir'_t), \qquad R_x = r_x + ir'_x, \qquad R_y = r_y + ir'_y, \qquad R_z = r_z + ir'_z, \qquad r_\mu, r'_\mu \in \mathbb{R},
$$

replaces the four complex coefficients by **eight real parameters**: $r_\mu$ is the real part of $R_\mu$, the coefficient of $e_\mu$, and $r'_\mu$ its imaginary part, the coefficient of $ie_\mu$, so the eight parameters are the coordinates of one point. The factor $c$ stands on the time coefficient alone and on both of its halves, so that $r_t$ and $r'_t$ are times and every coefficient is a length. The prime therefore marks the parameter that carries the $i$. As a real vector space $\mathbb{B}$ is eight-dimensional, and it splits naturally into two four-dimensional real subspaces — one taking $r'_t$ together with $r_x, r_y, r_z$, the other taking $r_t$ together with $r'_x, r'_y, r'_z$. The complex structure — the identification of which direction is "real" and which is "imaginary" — is **local**, determined by the electromagnetic properties of the medium at each point.

The hypothesis of this article is that this biquaternionic structure is the natural language in which the fundamental structures of physics are written, and that the fact that the framework contains both relativity and quantum physics is evidence for the proposal.

## Two Sectors: Material and Informational

The biquaternion algebra splits naturally into two complementary four-dimensional real subspaces:

$$
\mathbb{B} = \mathbb{B}_{\Phi} \oplus \mathbb{B}_{\Psi}.
$$

The subspace $\mathbb{B}_{\Phi}$ is the **anti-Hermitian subspace**, the fixed-point set of the anti-Hermitian conjugation $\flat$ (equivalently, the eigenspace of the Hermitian conjugation ${}^{*}$ with eigenvalue $-1$). The subspace $\mathbb{B}_{\Psi}$ is the **Hermitian subspace**, the fixed-point set of the Hermitian conjugation ${}^{*}$ (equivalently, its eigenspace with eigenvalue $+1$). The two are complementary: together they span $\mathbb{B}$, and their intersection is trivial. Every element of the algebra splits accordingly, $\tilde Q=\tilde R_\psi+\tilde R_\varphi$, into its **informational part** $\tilde R_\psi\in\mathbb{B}_{\Psi}$ and its **material part** $\tilde R_\varphi\in\mathbb{B}_{\Phi}$; an element of $\mathbb{B}_{\Psi}$ is its own informational part, and an element of $\mathbb{B}_{\Phi}$ its own material part.

The two subspaces have distinct physical roles:

- **$\mathbb{B}_{\Phi}$ is the material sector.** Its coordinates are **$i c r'_t$** (an imaginary temporal coordinate, $c$ being the speed of light) and **$x, y, z$** (three real spatial coordinates). It is the home of the four-vectors of relativistic physics. The imaginary time coordinate reflects a simple fact: time can be measured, but it cannot be touched, held, or moved through.
- **$\mathbb{B}_{\Psi}$ is the informational sector.** Its coordinates are **$c r_t$** (a real temporal coordinate) and **$i r'_{x}, i r'_{y}, i r'_{z}$** (three imaginary spatial coordinates). It is the home of the Hermitian operators, whose algebraic structure is that of a quantum-mechanical state space. The elements of $\mathbb{B}_{\Psi}$ carry quantum-informational content, in the sense established in the companion article on quantum physics: they are the states, observables, and measurement operators of a qubit. The name "informational sector" reflects this content. It is not a claim about entropy or any other thermodynamic property of the sector.

Written as elements of the algebra, each sector carries its own four real parameters, and there is **one** writing, not two: the parameter is the coordinate, and $c$ is the only conversion the scheme needs.

- **$\mathbb{B}_{\Phi}$**, the material sector, corresponding to the anti-Hermitian subspace:

    $$
    \tilde R_\varphi = i c\,r'_t\,e_t + r_x\vec e_x + r_y\vec e_y + r_z\vec e_z \in \mathbb{B}_{\Phi},
    $$

    with $r'_t = t'$ the material time and $(r_x,r_y,r_z) = (x,y,z)$ the material space.

- **$\mathbb{B}_{\Psi}$**, the informational sector, corresponding to the Hermitian subspace:

    $$
    \tilde R_\psi = c\,r_t\,e_t + i\bigl(r'_x\vec e_x + r'_y\vec e_y + r'_z\vec e_z\bigr) \in \mathbb{B}_{\Psi},
    $$

    with $r_t = t$ the informational time and $(r'_x,r'_y,r'_z) = (r'_{x},r'_{y},r'_{z})$ the informational space.

Where the prime falls is what distinguishes the sectors: in $\mathbb{B}_{\Phi}$ it is the **scalar** $r'_t$ (the time), in $\mathbb{B}_{\Psi}$ the **three vectors** $r'_k$ (the space). This is why the prime is not attached to a sector — $r'_t$ is a material parameter, $r'_k$ an informational one — and it is the one rule that makes the two sectors mirror images of each other. The complex structure is then visible as a count: the material sector has three real spatial directions and one imaginary temporal direction, the informational sector three imaginary spatial directions and one real temporal direction.

## The Complex Coordinates

Writing the biquaternion coordinate in terms of its material and informational parts,

$$
\tilde{R} = \underbrace{(i c r'_t)\,e_t + (r_x\,\vec e_x + r_y\,\vec e_y + r_z\,\vec e_z)}_{=\,\tilde R_\varphi\,\in\,\mathbb{B}_{\Phi}} \;+\; \underbrace{(c r_t)\,e_t + (i r'_{x}\,\vec e_x + i r'_{y}\,\vec e_y + i r'_{z}\,\vec e_z)}_{=\,\tilde R_\psi\,\in\,\mathbb{B}_{\Psi}},
$$

the coefficients $R_t, R_x, R_y, R_z$ take the explicit form

$$
\begin{aligned}
R_t &= c\,(r_t + i r'_t), \\
R_x &= r_x + i r'_x, \\
R_y &= r_y + i r'_y, \\
R_z &= r_z + i r'_z.
\end{aligned}
$$

Each coefficient is thus shown in its two guises: the complex coefficient $R_\mu$ itself, and the pair of coordinates it carries, $r_\mu$ from one sector and $r'_\mu$ from the other, with $c$ on the two times.

The **real parameters** $(r'_t,r_x,r_y,r_z)$ describe the material sector, and the **real parameters** $(r_t, r'_{x}, r'_{y}, r'_{z})$ describe the informational sector. Each sector is four-dimensional, and the full complexified spacetime is the direct sum of the two.

**The same decomposition, read on the coordinates.** The algebraic split of the opening and the coordinate values above are the same statement twice: matching the two writings coefficient by coefficient identifies each of the eight parameters with a coordinate, the two times carrying the factor $c$,

$$
r_t = t,\quad r'_t = t',\quad (r_x,r_y,r_z)=(x,y,z),\quad (r'_x,r'_y,r'_z)=(x',y',z').
$$

The unprimed parameter is throughout the **real part** of the complex coefficient and the primed one its **imaginary part**. It is worth noting which is which for the temporal coefficient: the real part of $R_t$ is $c r_t = ct$, an informational quantity, while its imaginary part $c r'_t = cr'_t$ is the material time. The two sectors take disjoint halves of the eight parameters — $\mathbb{B}_{\Phi}$ takes $r'_t$ together with the three $r_k$, $\mathbb{B}_{\Psi}$ takes $r_t$ together with the three $r'_k$ — so four complex coefficients and eight real parameters carry exactly the same information.

**One element, one point, one label.** The eight parameters split four and four between the parts, and the split gives the element its second interpretation. Read on its material part, the element is a spacetime event, $\tilde R_\varphi=i c r'_t\,e_t+r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$, and its informational part $\tilde R_\psi$ supplies the four parameters of its **internal label**; read on its informational part, it is an event of the informational sector, $\tilde R_\psi=c r_t\,e_t+i(r'_{x}\,\vec e_x+r'_{y}\,\vec e_y+r'_{z}\,\vec e_z)$, and its material part $\tilde R_\varphi$ supplies the four parameters of its **spacetime label**. The four complex coefficients therefore read as a spacetime point together with the matching point of the other sector, and no coefficient is idle: each carries one coordinate of each sector at once. That is why one element of $\mathbb{B}$ serves both as a four-vector and as a state — the two interpretations use the two halves of the same four coefficients.

### The Vacuum Limit

In vacuum, $c = c_0$, and the material time coordinate becomes $ic_0 r'_t$ — the familiar $i c r'_t$ form with the vacuum speed of light. The $i c r'_t$ convention is therefore the vacuum limit of the more general local structure. In a material medium, the complex structure uses $c$, the local speed of light, and varies from point to point. This makes the complex structure **local**, in the same spirit as the metric in general relativity.

## The Metric

The natural quadratic form on the biquaternion algebra is the **biquaternion norm**

$$
\langle d\tilde{R}\rangle_{\natural} = d\tilde{R} \circ d\tilde{R}^{\natural} = \sum_{\mu\in\{t,x,y,z\}} (dR_\mu)^2,
$$

where $\circ$ is the biquaternion product and ${}^{\natural}$ is the **quaternion conjugate**, the involution that reverses the three quaternion directions and leaves the complex coefficients alone: $e_t^{\natural}=e_t$, $\vec e_k^{\natural}=-\vec e_k$, hence $d\tilde{R}^{\natural} = dR_t\,e_t - dR_x\,\vec e_x - dR_y\,\vec e_y - dR_z\,\vec e_z$. A second conjugation appears later in the article, the **bar**, and it acts on the other factor: it conjugates the complex coefficients and leaves the quaternion basis alone, $\overline{\tilde{R}} = \sum_\mu \overline{R_\mu}\,e_\mu$. The two are different operations on the same element, and the norm uses the first. The quaternion conjugate is what produces the sum of squares: the product $d\tilde{R} \circ d\tilde{R}$ of $d\tilde{R}$ with itself is not $\sum_\mu (dR_\mu)^2$. Expanding in real and imaginary parts,

$$
(dR_t)^2 = c^2\bigl((dr_t)^2 - (dr'_t)^2 + 2i\,dr_t\,dr'_t\bigr),\qquad (dR_k)^2 = (dr_k)^2 - (dr'_k)^2 + 2i\,dr_k\,dr'_k .
$$

The **real part** of $\langle d\tilde{R}\rangle_{\natural} = \sum_\mu (dR_\mu)^2$ reproduces the Lorentzian interval on the material sector. The minus sign in the time–time component arises algebraically from $i^2 = -1$ in the imaginary time coordinate $i c r'_t$, not from an independently postulated metric signature. The **imaginary part** couples the material and informational sectors through cross terms.

Because each part retains only half of the eight parameters, the same biquaternion norm reads off as a real quadratic form on each, and it is again worth having both writings. On the material part, where $d\tilde R=d\tilde R_\varphi$ and only $dr'_t$ and the $dr_k$ are non-zero,

$$
\boxed{\;\langle d\tilde R_\varphi\rangle_{\natural} = -c^2(dr'_t)^2 + dr_x^2 + dr_y^2 + dr_z^2 = -c^2\,d{r'_{t}}^2 + dr_x^2+dr_y^2+dr_z^2\;},
$$

the Minkowski interval of signature $(3,1)$. On the informational part, where $d\tilde R=d\tilde R_\psi$ and only $dr_t$ and the $dr'_k$ are non-zero,

$$
\boxed{\;\langle d\tilde R_\psi\rangle_{\natural} = c^2 dr_t^2 - (dr'_x)^2 - (dr'_y)^2 - (dr'_z)^2 = c^2\,{dt}^2 - {dx'}^2 - {dy'}^2 - {dz'}^2\;},
$$

the mirror interval of signature $(1,3)$. The two are exchanged by $i$, and the sign of the form reverses with them, $\langle i\tilde{R}\rangle_{\natural} = -\langle\tilde{R}\rangle_{\natural}$. In both cases the null cone — the zero divisor set, discussed in the companion articles — has the same two interpretations:

$$
\mathbb{B}_{\Phi}:\;\; (dr'_t)^2 = dr_x^2 + dr_y^2 + dr_z^2 \iff c^2d{r'_{t}}^2 =dr_x^2+dr_y^2+dr_z^2, \qquad
\mathbb{B}_{\Psi}:\;\; dr_t^2 = (dr'_x)^2 + (dr'_y)^2 + (dr'_z)^2 \iff c^2{dt}^2 = {dx'}^2+{dy'}^2+{dz'}^2 .
$$

Each of these is one equation written twice: on the left in the parameters $r$, with $c$ on the time, and on the right in the metric form of physics.

**Where the minus comes from.** Read as a form on $\mathbb{C}$, the same norm is the identity, $\langle\tilde{R}\rangle_{\natural}=\sum_\mu R_\mu^2$, with every entry positive and the four directions of $\mathbb{B}$ on an equal footing: there is no minus sign in the complex form itself, and none is needed, since a complex coefficient can carry the sign. The minus appears only when a *real* coordinate is placed on a direction whose coefficient carries a factor of $i$, as it is in each of the two real sectors above. The Minkowski signature is therefore not an independent input of the theory: it is what the algebra's own form looks like once the material time is written $i c r'_t$, with $i^2=-1$ supplying the minus. The norm as a complex form, and the four forms it takes, are treated in *Algebra and Element Conventions*; the local complex structure behind the choice of $i$ is *The Local Complex Structure and the Speed of Light*.

**One root, three names.** The minus of the metric is one case of a single algebraic fact: the equation $\tilde{R}^{2}=\lambda e_t$ in the plain product has three distinguished radicands: a root of $-1$ is a complex structure, a root of $0$ a nilpotent of the light cone, and a root of $+1$ an involution. The central root $i$ is the scalar imaginary that writes $i c r'_t$; a non-central root is an internal complex structure of the real space, not a change of the algebra's scalars. The three answers are one equation, and the subspace in which the root is sought decides the physical name. Read on the elements, the same observation gives the massive, the massless and the spacelike as the interior, the boundary and the exterior of one quadric. The trichotomy is *Roots, Idempotents and Observables* and *The Zero-Divisor Cone and the Massless Spectrum*; the boundary is *The Light Cone as the Biquaternion Zero-Divisor Cone*; and the mass shell is *The Physical Interpretation of the 12 Products*.

### The Two Forms of One Element

The body has so far developed one form, the biquaternion norm $\langle\cdot\rangle_{\natural}$. The second is the **Hermitian form** on $\mathbb{B}_{\Psi}$, $\langle\tilde{R}_1,\tilde{R}_2\rangle_{*}=\sum_\mu R_{1\mu}\overline{R_{2\mu}}$, the sum of the four coordinates of one element against the conjugates of the other — the bar, the coefficient conjugation, and not the quaternion conjugate ${}^{\natural}$ of the norm. The two forms are two interpretations of one element, and they part company at once: the norm is complex and vanishes on the null cone, the Hermitian form is positive and vanishes only at the origin. At $\tilde{R}=e_t+i\vec e_z$ the two already differ: the norm is $\langle\tilde{R}\rangle_{\natural}=0$, while the Hermitian form is $\langle\tilde{R},\tilde{R}\rangle_{*}=2$. The same element is a null direction for the interval and a state of positive weight. The norm is the **interval**, whose zero set is the light cone; the Hermitian form is the **probability weight**, the form the Born rule draws on. One element carries both, and the framework's account of why the causal and the probabilistic structures coexist is that they are two forms on one biquaternion space and not two algebras. The form read as a product, and the positivity and the rank it carries, are treated in *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*; the probability reading is *The Informational Sector: States, Observables and Probability*.

## What the Framework Achieves

The main result of the framework so far is that the biquaternion algebra **contains, as a matter of algebra, the structures required for both relativity and quantum physics**. They are not incompatible sectors of physics that must be glued together; they are two aspects of the same biquaternion space, appearing in its two complementary subspaces. Two further classifications are read from that algebra and developed elsewhere: the **reality condition** that fixes the type of a particle, and the split of the internal symmetry into a compact part carrying a discrete charge and a non-compact part carrying a continuous label. Both are treated in *The Physical Interpretation of the 12 Products*; the antilinear structure behind them is *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*.

### Relativity in $\mathbb{B}_{\Phi}$

A point of the material sector is written in the coordinates of relativistic physics as

$$
\tilde R_\varphi = i c r'_{t}\,e_t + r_x\,\vec e_x + r_y\,\vec e_y + r_z\,\vec e_z \in \mathbb{B}_{\Phi},
$$

the imaginary time $i c r'_{t}$ together with the three real spatial coordinates $x, y, z$. The material sector $\mathbb{B}_{\Phi}$ carries the four-vectors of relativistic physics: position, velocity, momentum, force, potential, current. The **proper orthochronous Lorentz group** $SO^+(1,3)$ is realized through its double cover $SL(2,\mathbb{C})$, which is the **group of biquaternions of unit norm** in $\mathbb{B}$; its elements are the Lorentz rotors, written $\tilde U_{\mathrm{lor}}$:

$$
\boxed{\;SL(2,\mathbb{C}) \;\cong\; \{\tilde U_{\mathrm{lor}} \in \mathbb{B} : \tilde U_{\mathrm{lor}}\tilde U_{\mathrm{lor}}{}^{\natural} = e_t\}\;}.
$$

This group **acts** on the material sector by the **rotor conjugation**

$$
\tilde R_\varphi \;\longmapsto\; \tilde U_{\mathrm{lor}}\,\tilde R_\varphi\,\tilde U_{\mathrm{lor}}{}^{*}.
$$

The group itself lives in the full algebra $\mathbb{B}$ (since $\mathbb{B}_{\Phi}$ is not closed under multiplication and cannot carry a group structure). The four-vectors it acts on live in $\mathbb{B}_{\Phi}$. The different types of Lorentz transformation have rotors in different subspaces: pure boosts have rotors in $\mathbb{B}_{\Psi}$ (they are Hermitian), pure spatial rotations have rotors in $\mathbb{B}_{H}$ (they are real quaternions), and general Lorentz transformations have rotors in the full algebra.

The relativistic wave equations — **Maxwell's equations** and the **Dirac equation** — have natural biquaternion forms, as developed in the companion articles.

### Quantum Physics in $\mathbb{B}_{\Psi}$

A point of the informational sector is written in its own coordinates as

$$
\tilde R_\psi = (c r_t)\,e_t + (i r'_{x})\,\vec e_x + (i r'_{y})\,\vec e_y + (i r'_{z})\,\vec e_z \in \mathbb{B}_{\Psi},
$$

the real time $c r_t$ together with the three imaginary spatial coordinates $i r'_{x}, i r'_{y}, i r'_{z}$. The informational sector $\mathbb{B}_{\Psi}$ is, exactly, the **Hermitian part** of the operator algebra of a two-state quantum system: its elements are the observables, and they generate the full matrix algebra. This is established in the companion article *Quantum Physics in Biquaternionic Form*, and it can be summarized as follows.

- The **elements** of $\mathbb{B}_{\Psi}$, of the form $\tilde R_\psi = c r_t e_t + i\vec r_\psi$ — equivalently written $\tilde R_\psi = c r_t\,e_t + ir'_x\vec e_x + ir'_y\vec e_y + ir'_z\vec e_z$ with $c r_t, r'_x, r'_y, r'_z \in \mathbb{R}$, which is the usual writing of quantum physics — are the observables (they are automatically Hermitian by definition of $\mathbb{B}_{\Psi}$), with spectral decomposition in terms of idempotents.
- The **idempotents** in $\mathbb{B}_{\Psi}$, of the form $\tilde\Pi_{1,2}(\vec u) = \tfrac{1}{2}(e_t \pm i\vec u)$ with $\vec u$ a unit pure real quaternion, are the pure states of a qubit. They parametrize the Bloch sphere $S^2$.
- The **positive elements** in $\mathbb{B}_{\Psi}$ normalised by $\langle\tilde{Ϛ},e_t\rangle_{*}=\tfrac12\langle e_t\rangle_{*}$, of the form $\tilde{Ϛ} = \tfrac{1}{2}(e_t + i\vec r)$ with $|\vec r| \leq 1$, are the mixed states (trace one in the $2\times2$ image), parametrizing the Bloch ball.
- The **normalised Hermitian form** $\langle\tilde{Ϛ},\tilde R_\psi\rangle_{*}/\langle\tilde{Ϛ},e_t\rangle_{*} = c r_t + \vec r\cdot\vec r_\psi$ gives the Born rule, read in the $2\times2$ image as $\operatorname{Tr}(\tilde{Ϛ}\tilde R_\psi^{*})/\operatorname{Tr}(\tilde{Ϛ})=\operatorname{Tr}(\tilde{Ϛ}\tilde R_\psi)/\operatorname{Tr}(\tilde{Ϛ}) = c r_t + \vec r\cdot\vec r_\psi$, the star being inert on $\mathbb{B}_{\Psi}$ and the unstarred trace real; it is a consequence of the algebra rather than an independent postulate.
- The **sandwich operation** $\tilde{Ϛ} \mapsto \tilde\Pi\tilde{Ϛ}\tilde\Pi/\langle\tilde\Pi\tilde{Ϛ}\tilde\Pi,e_t\rangle_{*}$ gives the projective measurement and state update (the denominator normalises the post-measurement state; its $2\times2$ reading is $\mathrm{Tr}(\tilde\Pi\tilde{Ϛ}\tilde\Pi)$).
- The **$*$-unitary elements** of $\mathbb{B}$, and their conjugation action $\tilde{Ϛ} \mapsto \tilde Q\tilde{Ϛ}\tilde Q^{*}$, give the reversible evolution.
- The distinction between **reversible evolution** and **irreversible measurement** is a property of the acting element ($*$-unitary vs. idempotent), not an additional postulate.

The operator algebra of quantum physics, its state space, its Born rule, and its measurement rule are all **structural consequences** of the algebra of $\mathbb{B}_{\Psi}$. They are not imposed from outside. The two-state formalism at large is *Quantum Physics in Biquaternionic Form*; the derivation of the Born rule, and its comparison with the postulate it replaces, are *The Born Rule from the Hermitian Form — Derivation and Comparison*; the states that the indefinite fourth product cannot normalise are *The Physical Interpretation of the 12 Products*; and the decoherence of a measurement is *Decoherence as Idempotent Projection*.

### The Shared Home

The most significant feature of the framework is that **relativity and quantum physics share the same biquaternion space**. The Lorentz group is realized (via its double cover $SL(2,\mathbb{C})$) as the group of biquaternions of unit norm in $\mathbb{B}$, and the operator algebra of quantum physics is realized in the Hermitian subspace $\mathbb{B}_{\Psi}$. The two structures are not independent; they are aspects of the same biquaternion space.

This is the sense in which the framework is proposed as an alternative to the standard formulation: not as a modification of relativity or of quantum physics, but as a **common biquaternion space** on which both can be expressed.

### The Two Slots of One Product

Every product of the algebra reads two elements, one in each **slot**, and in the framework's two sesquilinear products the slots are not interchangeable: one is read plainly and the other through a conjugation. That asymmetry is the algebraic form of the two roles a quantum description pairs — an element and the adjoint of another — and it is the reason the Born weight above can be read as the scalar part of a product on the algebra rather than as a pairing imposed from outside. The four products, the two slots and their four interpretations are treated in *The Four General Products: Composition, Probability, Causality, Gauge*; the state and observable roles, the gauge action generated inside the algebra, and the chirality of that action are treated in *The Physical Interpretation of the 12 Products*.

**Four jobs, one grid.** The four products are read as the four jobs a relativistic quantum theory needs — composition, causality, probability and gauge — and each splits into a symmetric half and an antisymmetric half, so that the twelve products of the space are the four general products together with the two halves of each. What the algebra fixes is the grid and the signs; that these are the four jobs, and that the interpretation is exhaustive, is the framework's claim. The jobs are tabulated in *The Four General Products: Composition, Probability, Causality, Gauge*.

**The reading order.** The corpus is organised in four blocks. **Algebra** fixes the vocabulary: the elements, the twelve products, the four forms and the four norms. **Topology** reads the unit group, the cone and the orders. **Analysis** reads the exponential, the logarithm and the poles. **Geometry** reads the sectors, the frames, the bundles and the null quadric. The physical articles follow the same order: the algebra first, then the material and informational sectors, then the processes and the spectra. A reader who wants one path through the series can take the algebra block, then *The Material Sector: Four-Vectors, Interval and Lorentz Action* and *The Informational Sector: States, Observables and Probability*, then the analysis of the exponential, and then the spectral articles.

## Status and Open Questions

The framework is a **research program**, not a finished theory. The algebraic results — that $\mathbb{B}_{\Phi}$ carries the four-vectors of relativity and that $\mathbb{B}_{\Psi}$ carries the operator algebra of quantum physics — are established mathematics, and the identifications with the physical theories are developed in the companion articles.

What is not established is whether the framework has consequences beyond a reformulation of known physics. The key open questions are:

1. **Physical reality of the biquaternionic structure.** Is the biquaternion algebra merely a convenient reformulation of known physics, or does the structure of the universe genuinely follow the algebra? A structural hypothesis of this kind can only be evaluated by the richness of the consequences it produces.

2. **Coupling between the two sectors.** Beyond the Lorentz coupling via the rotor conjugation, is there a genuinely new coupling between the anti-Hermitian subspace $\mathbb{B}_{\Phi}$ and the Hermitian subspace $\mathbb{B}_{\Psi}$? Any such coupling would be where new physical content could reside. One minimal instance is already algebraic and not imposed: the **square**. For a material element the quaternionic square is the interval, $\tilde R_\varphi^{\natural}\tilde R_\varphi=\langle\tilde R_\varphi\rangle_{\natural}e_t$ with $\langle\cdot\rangle_{\natural}$ real, and the real scalar line lies in $\mathbb{B}_{\Psi}$, so squaring is a map $\mathbb{B}_{\Phi}\to\mathbb{B}_{\Psi}$ supplied by the product itself — the interpretation carried by *The Physical Interpretation of the 12 Products*. What remains open is a coupling with a dynamics; the square is a map, not an evolution.

3. **Extension to many qubits and to quantum field theory.** The quantum formalism presented in the companion article is for a single qubit. The extension to $n$ qubits (via the tensor product $\mathbb{B}^{\otimes n} \cong M_{2^n}(\mathbb{C})$), the second-quantized version, and the connection to quantum field theory remain to be developed.

4. **Relativistic quantum theory.** The biquaternion algebra contains both the Lorentz group and the operator algebra of quantum physics. A fully relativistic quantum theory of spinor fields — whose classical precursor is the biquaternion Dirac equation — is the natural continuation of the framework.

5. **Curved spacetime.** The framework so far is formulated on flat spacetime. Its extension to curved spacetime, and its relation to general relativity, remain open.

6. **Empirical contact.** What quantitative prediction distinguishes this framework from standard physics? This is the central open question, and the one on which the eventual evaluation of the hypothesis will depend.

The framework is offered as a structural intuition: that the two natural subspaces of the biquaternion algebra have distinct physical roles — one material, one informational — and that the algebra $\mathbb{B}$ is the natural home in which both relativity and quantum physics are expressed. The local speed of light $c = 1/\sqrt{\epsilon\mu}$ plays the role of the local scale factor of the complex structure, making the $i c r'_t$ convention a vacuum approximation of a more general local structure, in the same way that special relativity is a local approximation of general relativity.

## Physical Readings

Two interpretations of the introduction are worth separating. Read as a statement about invariance, the universe of the article is the sesquilinear pair: a change of the local complex structure moves the interval and the composition and leaves the probability form, the gauge calibration and the zero-divisor cone where they were (*Algebra and Element Conventions*). Read in time, its two sectors are two clocks reading one hand: the material time and the informational time are the two projections of one central coordinate, so each sector's time is read against the phase of the other (*Each Sector Is the Other's Clock: the Sector Exchange as Relational Time*). Four further readings can be named.

- **Amplitude interpretation.** Each complex coefficient $R_\mu$ is one complex number, that is, a magnitude and a phase, so the arena of the framework is complex before any quantum interpretation is imposed: the two sectors are read as the real and the imaginary halves of one amplitude, and an element is a point of the complexified spacetime together with its conjugate amplitude data. Boundary: the interpretation names the shape of the coefficient and supplies neither a quantisation nor a measurement rule.
- **State-preparation interpretation.** The central map $\tilde R_\psi=-\tfrac{i}{2}\tilde R_\varphi$ carries a material four-vector to an informational element, and on the trace-one slice of the future cone to a state: the four-vector $i c r'_t\,e_t+r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$ is carried to $\tfrac12(c r'_{t}\,e_t-i(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z))$, with $\mathrm{Tr}(\tilde R_\psi)=c r'_{t}$ and $\langle\tilde R_\psi\rangle_{\natural}=-\tfrac14\langle\tilde R_\varphi\rangle_{\natural}$, so at $c r'_{t}=1$ it is the Hermitian state $\tilde{Ϛ}=\tfrac12(e_t+i\vec r)$ with $\vec r=-(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)$ and $|\vec r|\le1$. Boundary: the map is the mirror dictionary of *The Bloch Ball as the Normalised Slice of the Future Light Cone*, which owns it, and the interpretation names a preparation and not a dynamics.
- **Cross-sector coupling by the square.** For a material element the quaternionic square is the interval itself, $\tilde R_\varphi^{\natural}\tilde R_\varphi=\langle\tilde R_\varphi\rangle_{\natural}e_t$ with $\langle\cdot\rangle_{\natural}$ real, and the real scalar line lies in $\mathbb{B}_{\Psi}$: squaring is therefore one algebraic map $\mathbb{B}_{\Phi}\to\mathbb{B}_{\Psi}$, the minimal instance of the coupling asked for in question 2 above, supplied by the product rather than added by hand. The product of *two* material elements is not in general informational, while the *square of one* is. Boundary: one map, with image the real scalar line, and no dynamics; the identity is owned by *The Physical Interpretation of the 12 Products*, and its grid-level pointer is *The Four General Products: Composition, Probability, Causality, Gauge*.
- **One locus, two lists.** The norm's zero set $\langle\tilde{R}\rangle_{\natural}=0$ is the light cone of the material sector and it is also the locus on which the pure states of the informational sector sit: the idempotents $\tilde\Pi=\tfrac12(e_t\pm i\vec u)$ have $\langle\tilde\Pi\rangle_{\natural}=0$. The causal boundary and the list of pure states are one algebraic locus read twice, the zero-divisor cone. Boundary: the interpretation identifies sets, and it does not make every null element a pure state, the null cone being strictly larger than the set of idempotents; the state side is *The Physical Interpretation of the 12 Products*, and the cone itself *The Light Cone as the Biquaternion Zero-Divisor Cone*.

## Summary

The framework is stated in one sentence: the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ is the common biquaternion space of relativity and quantum physics, and its two natural real subspaces carry the two theories. The **anti-Hermitian subspace** $\mathbb{B}_{\Phi}$ carries the four-vectors of relativity, the material sector, in the coordinates $(i c r'_t,r_x,r_y,r_z)$; the **Hermitian subspace** $\mathbb{B}_{\Psi}$ carries the operator algebra of quantum physics, the informational sector, in the coordinates $(c r_t,i r'_{x},i r'_{y},i r'_{z})$. Multiplication by $i$ exchanges the two.

Both sectors are written in the one biquaternion space. A material element is $\tilde R_\varphi=i c r'_t\,e_t+r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$ and an informational element is $\tilde R_\psi=c r_t\,e_t+i(r'_{x}\,\vec e_x+r'_{y}\,\vec e_y+r'_{z}\,\vec e_z)$; the two are the parts of one element, $\tilde R=\tilde R_\psi+\tilde R_\varphi$, and the norm $\langle\tilde{R}\rangle_{\natural}=\sum_\mu R_\mu^2$ is the interval on $\mathbb{B}_{\Phi}$, of signature $(-,+,+,+)$ there, and the Hermitian form $\langle\tilde{R}_1,\tilde{R}_2\rangle_{*}=\sum_\mu R_{1\mu}\overline{R_{2\mu}}$ is the probability weight on $\mathbb{B}_{\Psi}$. The Lorentz rotors are the unit-norm elements $\tilde U_{\mathrm{lor}}$ with $\tilde U_{\mathrm{lor}}\tilde U_{\mathrm{lor}}{}^{\natural}=e_t$, acting by conjugation; the idempotents $\tilde\Pi_{1,2}(\vec u)=\tfrac12(e_t\pm i\vec u)$ are the pure states of the informational sector; and the observables are the Hermitian elements $\tilde R_\psi=c r_t\,e_t+i\vec r_\psi$ with $c r_t$ real.

The framework is a research program, not a finished theory. The algebraic identifications above are established mathematics; what is open is whether the framework has consequences beyond a reformulation of known physics. Six questions are recorded: the physical reality of the biquaternionic structure; a coupling between the sectors beyond the Lorentz conjugation, of which the square $\mathbb{B}_{\Phi}\to\mathbb{B}_{\Psi}$ is the minimal algebraic instance already supplied by the product; the extension to many qubits and to quantum field theory; a fully relativistic quantum theory; curved spacetime; and empirical contact. The local speed of light $c=1/\sqrt{\epsilon\mu}$ plays the role of the local scale factor of the complex structure, making the $i c r'_t$ convention the vacuum approximation of a more general local structure.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\tilde{R} = \sum_\mu R_\mu e_\mu$ | Biquaternionic coordinate |
| $R_t = c\,(r_t+ir'_t)$, $R_k = r_k+ir'_k$ | Complex coefficient: $r_\mu$ its real part (the coefficient of $e_\mu$), $r'_\mu$ its imaginary part (the coefficient of $ie_\mu$); the factor $c$ stands on the time alone |
| $\tilde R = \tilde R_\psi + \tilde R_\varphi$ | The split of the coordinate into its informational and material parts |
| $\tilde R_\varphi = i c\,r'_t\,e_t + \vec r = i c\,r'_t\,e_t + r_x\vec e_x + r_y\vec e_y + r_z\vec e_z$ | Material element, both readings, with $\vec r=r_x\vec e_x+r_y\vec e_y+r_z\vec e_z$; $r'_t = t'$, $(r_x,r_y,r_z)=(x,y,z)$ |
| $\tilde R_\psi = c\,r_t\,e_t + i\vec r_\psi = c\,r_t\,e_t + i(r'_{x}\,\vec e_x+r'_{y}\,\vec e_y+r'_{z}\,\vec e_z)$ | Informational element, both readings, with $\vec r_\psi=r'_x\vec e_x+r'_y\vec e_y+r'_z\vec e_z$; $r_t = t$, $(r'_x,r'_y,r'_z)=(x',y',z')$ |
| $\langle\tilde{R}\rangle_{\natural} = \tilde{R}\tilde{R}^{\natural} = \sum_\mu R_\mu^2$ | Biquaternion norm; the identity matrix $\mathrm{diag}(+1,+1,+1,+1)$ as a metric on $\mathbb{C}$, signature $(-,+,+,+)$ on the real material sector |
| $\langle\tilde{R}_1,\tilde{R}_2\rangle_{*} = \sum_\mu R_{1\mu}\overline{R_{2\mu}}$ | Hermitian form, positive definite; the probability weight, $\langle\tilde{R}_2,\tilde{R}_2\rangle_{*} = \sum_\mu\lvert R_{2\mu}\rvert^{2}$; the coefficient of $e_t$ in $\tilde{R}\tilde{R}^{*}$ |
| ${}^{\natural}$ | Quaternion conjugate: reverses the quaternion basis, $e_t^{\natural}=e_t$ and $\vec e_k^{\natural}=-\vec e_k$, and leaves the complex coefficients $R_\mu$ untouched; the conjugation of the norm, $\langle\tilde{R}\rangle_{\natural} = \tilde{R}\tilde{R}^{\natural}$ |
| $\overline{\cdot}$ | Bar, the coefficient conjugation: conjugates each complex coefficient $R_\mu$ and leaves the quaternion basis untouched, $\overline{\tilde{R}} = \sum_\mu \overline{R_\mu}\,e_\mu$; the conjugation of the Hermitian form, $\langle\tilde{R}_1,\tilde{R}_2\rangle_{*} = \sum_\mu R_{1\mu}\overline{R_{2\mu}}$ |
| ${}^{*} = \overline{\cdot}\circ{}^{\natural}$ | Hermitian conjugation: conjugates both factors, $\tilde{R}^{*} = \overline{R_t}e_t - \overline{R_x}\vec e_x - \overline{R_y}\vec e_y - \overline{R_z}\vec e_z$; the conjugation that defines the two sectors, the fixed points of ${}^{*}$ being $\mathbb{B}_{\Psi}$ |
| ${}^{\flat} = -{}^{*}$ | Anti-Hermitian conjugation: the star composed with the central sign, $\tilde{R}^{\flat} = -\tilde{R}^{*}$, of which the material sector $\mathbb{B}_{\Phi}$ is the fixed-point set |
| $\mathbb{B}_{\Phi}$ | Anti-Hermitian subspace (material sector): coordinates $(i c r'_t, r_x, r_y, r_z)$, parameters $r'_t, r_x, r_y, r_z$ |
| $\mathbb{B}_{\Psi}$ | Hermitian subspace (informational sector): coordinates $(c r_t, i r'_{x}, i r'_{y}, i r'_{z})$, parameters $r_t, r'_x, r'_y, r'_z$ |
| $\mathbb{B}_{H}$ | Real quaternion subspace (home of the rotation rotors): the real half, all four coefficients real, fixed points of complex conjugation; a subalgebra |
| $\mathbb{B}_{iH}$ | Antiquaternion subspace: the imaginary half, all four coefficients purely imaginary, the partner of $\mathbb{B}_{H}$ in $\mathbb{B} = \mathbb{B}_{H} \oplus \mathbb{B}_{iH}$. This split crosses the $\mathbb{B}_{\Psi,\Phi}$ split: the scalar of $\mathbb{B}_{\Phi}$ and the vectors of $\mathbb{B}_{\Psi}$ come from here |
| $\tilde\Pi_{1,2}(\vec u) = \tfrac{1}{2}(e_t \pm i\vec u)$ | Idempotent (pure state of the informational sector) |
| $\tilde R_\psi = c r_t e_t + i\vec r_\psi$ | Hermitian element (observable of the informational sector); $c r_t \in \mathbb{R}$ is the scalar component and $\vec r_\psi = (r'_x,r'_y,r'_z)$ the vector components. These are the generic names used for these components throughout the series; written as a coordinate-carrying element, the same object is $c\,r_t\,e_t+i\,r'_k\vec e_k$ |
| $(r'_t,r_x,r_y,r_z)$ | Real coordinates of the material sector ($c$ is a scale factor, not a coordinate) |
| $(t, r'_{x}, r'_{y}, r'_{z})$ | Real coordinates of the informational sector |
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
