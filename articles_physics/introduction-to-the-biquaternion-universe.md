# __Introduction to the Biquaternion Universe__

## Core Proposal

The fundamental structure of the universe is a biquaternionic space, of which Minkowski space is a slice. A point in this complexified spacetime is an element of the **biquaternion algebra** $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$, written as a biquaternionic coordinate

$$
\tilde{Q} = Q_t e_t + \vec Q = Q_t e_t + Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z,
$$

where $e_t = 1$ and $\vec e_x, \vec e_y, \vec e_z$ are the quaternion units, so that $\vec Q = Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z$ is the vector part. The four coefficients $Q_\mu$ are **complex**, and everything that follows turns on how each of them is split. Writing every coefficient as a real part plus $i$ times a real part,

$$
Q_t = q_t + iq'_t, \qquad Q_x = q_x + iq'_x, \qquad Q_y = q_y + iq'_y, \qquad Q_z = q_z + iq'_z, \qquad q_\mu, q'_\mu \in \mathbb{R},
$$

replaces the four complex coefficients by **eight real parameters**: $q_\mu$ is the real part of $Q_\mu$, the coefficient of $e_\mu$, and $q'_\mu$ its imaginary part, the coefficient of $ie_\mu$, so the eight parameters are the coordinates of one point. Each number takes the letter of its sector: the material four are $r'_t$ and $r_x, r_y, r_z$, the informational four $h_t$ and $h'_x, h'_y, h'_z$, with $q'_t=r'_t$, $q_\eta=r_\eta$, $q_t=h_t$ and $q'_\eta=h'_\eta$. The four coefficients are lengths, and the two temporal parameters are lengths as well, so one element carries one unit in all four of its directions and no constant stands between the parameters. The prime therefore marks the parameter that carries the $i$. As a real vector space $\mathbb{B}$ is eight-dimensional, and it splits naturally into two four-dimensional real subspaces — one taking $r'_t$ together with $r_x, r_y, r_z$, the other taking $h_t$ together with $h'_x, h'_y, h'_z$. The complex structure — the identification of which direction is "real" and which is "imaginary" — is **local**, determined by the electromagnetic properties of the medium at each point.

The hypothesis of this article is that this biquaternionic structure is the natural language in which the fundamental structures of physics are written, and that the fact that the framework contains both relativity and quantum physics is evidence for the proposal.

## Two Sectors: Material and Informational

The biquaternion algebra splits naturally into two complementary four-dimensional real subspaces:

$$
\mathbb{B} = \mathbb{B}_{\Phi} \oplus \mathbb{B}_{\Psi}.
$$

The subspace $\mathbb{B}_{\Phi}$ is the **anti-Hermitian subspace**, the fixed-point set of the anti-Hermitian conjugation $\flat$ (equivalently, the eigenspace of the Hermitian conjugation ${}^{*}$ with eigenvalue $-1$). The subspace $\mathbb{B}_{\Psi}$ is the **Hermitian subspace**, the fixed-point set of the Hermitian conjugation ${}^{*}$ (equivalently, its eigenspace with eigenvalue $+1$). The two are complementary: together they span $\mathbb{B}$, and their intersection is trivial. Every element of the algebra splits accordingly, $\tilde Q=\tilde H_\Psi+\tilde R_\Phi$, into its **material part** $\tilde R_\Phi\in\mathbb{B}_{\Phi}$ and its **informational part** $\tilde H_\Psi\in\mathbb{B}_{\Psi}$; an element of $\mathbb{B}_{\Phi}$ is its own material part, and an element of $\mathbb{B}_{\Psi}$ its own informational part. The two halves carry one glyph each, and the sector mark alone separates them; the general element $\tilde Q$ takes no sector mark, since its sector depends on its value. The letter carries the sector: the material half is $i r'_t\,e_t+\vec r_\Phi$ and the informational half is $h_t\,e_t+i\vec h_\Psi$, and the eight numbers of an element do not change with the letter.

The two subspaces have distinct physical roles:

- **$\mathbb{B}_{\Phi}$ is the material sector.** Its coordinates are **$i r'_t$** (an imaginary temporal coordinate, a length) and **$r_x, r_y, r_z$** (three real spatial coordinates). It is the home of the four-vectors of relativistic physics. The imaginary time coordinate reflects a simple fact: time can be measured, but it cannot be touched, held, or moved through.
- **$\mathbb{B}_{\Psi}$ is the informational sector.** Its coordinates are **$h_t$** (a real temporal coordinate, a length) and **$i h'_{x}, i h'_{y}, i h'_{z}$** (three imaginary spatial coordinates). It is the home of the Hermitian operators, whose algebraic structure is that of a quantum-mechanical state space. The elements of $\mathbb{B}_{\Psi}$ carry quantum-informational content, in the sense established in the companion article on quantum physics: they are the states, observables, and measurement operators of a qubit. The name "informational sector" reflects this content. It is not a claim about entropy or any other thermodynamic property of the sector.

Written as elements of the algebra, each sector carries its own four real parameters: the parameter is the coordinate, and no conversion stands between them.

- **$\mathbb{B}_{\Phi}$**, the material sector, corresponding to the anti-Hermitian subspace:

    $$
    \tilde R_\Phi = i r'_t\,e_t + \vec r_\Phi = i r'_t\,e_t + r_x\vec e_x + r_y\vec e_y + r_z\vec e_z \in \mathbb{B}_{\Phi},
    $$

    with $r'_t$ the material temporal coordinate, a length, and $\vec r_\Phi = r_x\vec e_x + r_y\vec e_y + r_z\vec e_z$ the material space.

- **$\mathbb{B}_{\Psi}$**, the informational sector, corresponding to the Hermitian subspace:

    $$
    \tilde H_\Psi = h_t\,e_t + i\vec h_\Psi = h_t\,e_t + i\bigl(h'_x\vec e_x + h'_y\vec e_y + h'_z\vec e_z\bigr) \in \mathbb{B}_{\Psi},
    $$

    with $h_t$ the informational temporal coordinate, a length, and $\vec h_\Psi = h'_x\vec e_x + h'_y\vec e_y + h'_z\vec e_z$ the informational space.

Where the prime falls is what distinguishes the sectors: in $\mathbb{B}_{\Phi}$ it is the **scalar** $r'_t$ (the time), in $\mathbb{B}_{\Psi}$ the **three vectors** $h'_\eta$ (the space). This is why the prime is not attached to a sector — $r'_t$ is a material parameter, $h'_\eta$ an informational one — and it is the one rule that makes the two sectors mirror images of each other. The complex structure is then visible as a count: the material sector has three real spatial directions and one imaginary temporal direction, the informational sector three imaginary spatial directions and one real temporal direction.

## The Complex Coordinates

Writing the biquaternion coordinate in terms of its material and informational parts,

$$
\tilde{Q} = \underbrace{(i q'_t)\,e_t + (q_x\,\vec e_x + q_y\,\vec e_y + q_z\,\vec e_z)}_{=\,\tilde R_\Phi\,\in\,\mathbb{B}_{\Phi}} \;+\; \underbrace{(q_t)\,e_t + (i q'_{x}\,\vec e_x + i q'_{y}\,\vec e_y + i q'_{z}\,\vec e_z)}_{=\,\tilde H_\Psi\,\in\,\mathbb{B}_{\Psi}},
$$

the coefficients $Q_t, Q_x, Q_y, Q_z$ take the explicit form

$$
\begin{aligned}
Q_t &= q_t + i q'_t, \\
Q_x &= q_x + i q'_x, \\
Q_y &= q_y + i q'_y, \\
Q_z &= q_z + i q'_z.
\end{aligned}
$$

Written in the letters of its sector, each of the two blocks takes its own alphabet: the material block is $\tilde R_\Phi = i r'_t\,e_t+\vec r_\Phi$ with $\vec r_\Phi=r_x\vec e_x+r_y\vec e_y+r_z\vec e_z$, and the informational block is $\tilde H_\Psi = h_t\,e_t+i\vec h_\Psi$ with $\vec h_\Psi=h'_x\vec e_x+h'_y\vec e_y+h'_z\vec e_z$. The identification is coefficient by coefficient, $q'_t=r'_t$, $q_\eta=r_\eta$, $q_t=h_t$ and $q'_\eta=h'_\eta$.

Each coefficient is thus shown in its two guises: the complex coefficient $Q_\mu$ itself, and the pair of parameters it carries, $q_\mu$ from one sector and $q'_\mu$ from the other, the two times in metres like the two spaces.

The **real parameters** $(r'_t,r_x,r_y,r_z)$ describe the material sector, and the **real parameters** $(h_t, h'_{x}, h'_{y}, h'_{z})$ describe the informational sector. Each sector is four-dimensional, and the full complexified spacetime is the direct sum of the two.

**The same decomposition, read on the coordinates.** The algebraic split of the opening and the coordinate values above are the same statement twice: matching the two writings coefficient by coefficient identifies each of the eight parameters with one coordinate of the element, the two times in the same unit as the three spaces. The eight numbers are one set read twice, $q_\mu$ as the part of the coefficient and $r$ or $h$ as the coordinate of its sector, the identification being the one above: the parameters are the coordinates.

The unprimed parameter is throughout the **real part** of the complex coefficient and the primed one its **imaginary part**. It is worth noting which is which for the temporal coefficient: the real part of $Q_t$ is $q_t$, an informational coordinate, while its imaginary part $q'_t$ is the material one. The two sectors take disjoint halves of the eight parameters — $\mathbb{B}_{\Phi}$ takes $r'_t$ together with the three $r_\eta$, $\mathbb{B}_{\Psi}$ takes $h_t$ together with the three $h'_\eta$ — so four complex coefficients and eight real parameters carry exactly the same information.

**One element, one point, one label.** The eight parameters split four and four between the parts, and the split gives the element its second interpretation. Read on its material part, the element is a spacetime event, $\tilde R_\Phi=i r'_t\,e_t+\vec r_\Phi$, and its informational part $\tilde H_\Psi$ supplies the four parameters of its **internal label**; read on its informational part, it is an event of the informational sector, $\tilde H_\Psi=h_t\,e_t+i\vec h_\Psi$, and its material part $\tilde R_\Phi$ supplies the four parameters of its **spacetime label**. The four complex coefficients therefore read as a spacetime point together with the matching point of the other sector, and no coefficient is idle: each carries one coordinate of each sector at once. That is why one element of $\mathbb{B}$ serves both as a four-vector and as a state — the two interpretations use the two halves of the same four coefficients.

### The Vacuum Limit

In vacuum the local speed of light is the constant $c_0$; in a material medium it is $c=1/\sqrt{\epsilon\mu}$ and varies from point to point. Neither value enters the coordinate, because the four coefficients are lengths in either case. What is local is the complex structure and its scale, and the scale is read through the one conversion the scheme still uses, $t'=r'_t/c$, wherever a clock is compared with a length. The writing of an element is therefore the same in vacuum and in a medium, in the same spirit as the metric of general relativity, which is local while the coordinates of a chart are not.

## The Metric

The quadratic form on the biquaternion algebra is the **biquaternion norm**

$$
\langle d\tilde{Q}\rangle_{\natural} = d\tilde{Q}\, d\tilde{Q}^{\natural} = \sum_{\mu\in\{t,x,y,z\}} (dQ_\mu)^2,
$$

where ${}^{\natural}$ is the **quaternion conjugate**, the involution that reverses the three quaternion directions and leaves the complex coefficients alone: $e_t^{\natural}=e_t$, $\vec e_\eta^{\natural}=-\vec e_\eta$, hence $d\tilde{Q}^{\natural} = dQ_t\,e_t - dQ_x\,\vec e_x - dQ_y\,\vec e_y - dQ_z\,\vec e_z$. A second conjugation appears later in the article, the **bar**, and it acts on the other factor: it conjugates the complex coefficients and leaves the quaternion basis alone, $\overline{\tilde{Q}} = \sum_\mu \overline{Q_\mu}\,e_\mu$. The two are different operations on the same element, and the norm uses the first. The quaternion conjugate is what produces the sum of squares: the plain square $d\tilde{Q}\,d\tilde{Q}$ is not $\sum_\mu (dQ_\mu)^2$. Expanding in real and imaginary parts,

$$
(dQ_t)^2 = \bigl((dq_t)^2 - (dq'_t)^2 + 2i\,dq_t\,dq'_t\bigr),\qquad (dQ_\eta)^2 = (dq_\eta)^2 - (dq'_\eta)^2 + 2i\,dq_\eta\,dq'_\eta .
$$

The **real part** of $\langle d\tilde{Q}\rangle_{\natural} = \sum_\mu (dQ_\mu)^2$ reproduces the Lorentzian interval on the material sector and the mirror interval on the informational one. The minus sign in the time–time component arises algebraically from $i^2 = -1$ in the imaginary time coordinate $i r'_t$, not from an independently postulated metric signature. The **imaginary part** couples the material and informational sectors through cross terms.

Because each part retains only half of the eight parameters, the same biquaternion norm reads off as a real quadratic form on each, and it is again worth having both writings. On the material part, where $d\tilde Q=d\tilde R_\Phi$ and only $dr'_t$ and the $dr_\eta$ are non-zero,

$$
\boxed{\;\langle d\tilde R_\Phi\rangle_{\natural} = -(dr'_t)^2 + dr_x^2 + dr_y^2 + dr_z^2\;},
$$

the Minkowski interval of signature $(3,1)$. On the informational part, where $d\tilde Q=d\tilde H_\Psi$ and only $dh_t$ and the $dh'_\eta$ are non-zero,

$$
\boxed{\;\langle d\tilde H_\Psi\rangle_{\natural} = dh_t^2 - (dh'_x)^2 - (dh'_y)^2 - (dh'_z)^2\;},
$$

the mirror interval of signature $(1,3)$. The two are exchanged by $i$, and the sign of the form reverses with them, $\langle i\tilde{Q}\rangle_{\natural} = -\langle\tilde{Q}\rangle_{\natural}$. In both cases the null cone — each sector's part of the zero divisor set of the algebra, discussed in the companion articles — has the same two interpretations:

$$
\mathbb{B}_{\Phi}:\;\; (dr'_t)^2 = dr_x^2 + dr_y^2 + dr_z^2, \qquad
\mathbb{B}_{\Psi}:\;\; dh_t^2 = (dh'_x)^2 + (dh'_y)^2 + (dh'_z)^2 .
$$

Each of these is one equation in the four parameters of its sector, with the temporal parameter squared against the three spatial ones.

**Where the minus comes from.** Read as a form on $\mathbb{C}$, the same norm has the unit metric $\delta_{\mu\nu}=(1,1,1,1)$ for its coefficient tuple, $\langle\tilde{Q}\rangle_{\natural}=\sum_\mu Q_\mu^2$, with every entry $+1$ and the four directions of $\mathbb{B}$ on an equal footing: there is no minus sign in the complex form itself, and none is needed, since a complex coefficient can carry the sign. The minus appears only when a *real* coordinate is placed on a direction whose coefficient carries a factor of $i$, as it is in each of the two real sectors above. The Minkowski signature is therefore not an independent input of the theory: it is what the algebra's own form looks like once the material time is written $i r'_t$, with $i^2=-1$ supplying the minus. The metric is *The Unit Metric in the Biquaternion Universe*, which also states the absorbed alternative $g=\mathrm{diag}(-1,1,1,1)$ and why the series refuses it. The norm as a complex form, and the four forms it takes, are treated in *Algebra and Element Conventions*; the local complex structure behind the choice of $i$ is *The Local Complex Structure and the Speed of Light*.

**One root, three names.** The minus of the interval is one case of a single algebraic fact: the equation $\tilde{Q}^{2}=\lambda e_t$ in the plain product has three distinguished radicands: a root of $-1$ is a complex structure, a root of $0$ a nilpotent of the light cone, and a root of $+1$ an involution. The central root $i$ is the scalar imaginary that writes $i r'_t$; a non-central root is an internal complex structure of the real space, not a change of the algebra's scalars. The three answers are one equation, and the subspace in which the root is sought decides the physical name. Read on the elements, the same observation gives the massive, the massless and the spacelike as the interior, the boundary and the exterior of one quadric. The trichotomy is *Roots, Idempotents and Observables* and *The Zero-Divisor Cone and the Massless Spectrum*; the boundary is *The Light Cone as the Biquaternion Zero-Divisor Cone*; and the mass shell is *The Physical Interpretation of the 12 Products*.

### The Two Forms of One Element

The body has so far developed one form, the biquaternion norm $\langle\cdot\rangle_{\natural}$. The second is the **Hermitian form** on $\mathbb{B}_{\Psi}$, $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}=\sum_\mu Q_{1\mu}\overline{Q_{2\mu}}$, the sum of the four coordinates of one element against the conjugates of the other — the bar, the coefficient conjugation, and not the quaternion conjugate ${}^{\natural}$ of the norm. The two forms are two interpretations of one element, and they part company at once: the norm is complex and vanishes on the null cone, the Hermitian form is positive and vanishes only at the origin. At $\tilde{Q}=e_t+i\vec e_z$ the two already differ: the norm is $\langle\tilde{Q}\rangle_{\natural}=0$, while the Hermitian form is $\langle\tilde{Q},\tilde{Q}\rangle_{*}=2$. The same element is a null direction for the interval and a state of positive weight. The norm is the **interval**, whose zero set is the light cone; the Hermitian form is the **probability weight**, the form the Born rule draws on. One element carries both, and the framework's account of why the causal and the probabilistic structures coexist is that they are two forms on one biquaternion space and not two algebras. The form read as a product, and the positivity and the rank it carries, are treated in *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*; the probability reading is *The Informational Sector: States, Observables and Probability*.

## What the Framework Achieves

The main result of the framework so far is that the biquaternion algebra **contains, as a matter of algebra, the structures required for both relativity and quantum physics**. They are not incompatible sectors of physics that must be glued together; they are two aspects of the same biquaternion space, appearing in its two complementary subspaces. Two further classifications are read from that algebra and developed elsewhere: the **reality condition** that fixes the type of a particle, and the split of the internal symmetry into a compact part carrying a discrete charge and a non-compact part carrying a continuous label. Both are treated in *The Physical Interpretation of the 12 Products*; the antilinear structure behind them is *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*.

### Relativity in $\mathbb{B}_{\Phi}$

A point of the material sector is written in the coordinates of relativistic physics as

$$
\tilde R_\Phi = i r'_{t}\,e_t + \vec r_\Phi = i r'_{t}\,e_t + r_x\,\vec e_x + r_y\,\vec e_y + r_z\,\vec e_z \in \mathbb{B}_{\Phi},
$$

the imaginary temporal coordinate $i r'_{t}$, a length, together with the three real spatial coordinates $\vec r_\Phi = r_x\,\vec e_x + r_y\,\vec e_y + r_z\,\vec e_z$. The material sector $\mathbb{B}_{\Phi}$ carries the four-vectors of relativistic physics: position, velocity, momentum, force, potential, current. The **proper orthochronous Lorentz group** $SO^+(1,3)$ is realized through its double cover $SL(2,\mathbb{C})$, which is the **group of biquaternions of unit norm** in $\mathbb{B}$; its elements are the Lorentz rotors, written $\tilde U_{\mathrm{lor}}$:

$$
\boxed{\;SL(2,\mathbb{C}) \;\cong\; \{\tilde U_{\mathrm{lor}} \in \mathbb{B} : \tilde U_{\mathrm{lor}}\tilde U_{\mathrm{lor}}{}^{\natural} = e_t\}\;}.
$$

This group **acts** on the material sector by the **rotor conjugation**

$$
\tilde R_\Phi \;\longmapsto\; \tilde U_{\mathrm{lor}}\,\tilde R_\Phi\,\tilde U_{\mathrm{lor}}{}^{*}.
$$

The group itself lives in the full algebra $\mathbb{B}$ (since $\mathbb{B}_{\Phi}$ is not closed under multiplication and cannot carry a group structure). The four-vectors it acts on live in $\mathbb{B}_{\Phi}$. The different types of Lorentz transformation have rotors in different subspaces: pure boosts have rotors in $\mathbb{B}_{\Psi}$ (they are Hermitian), pure spatial rotations have rotors in $\mathbb{B}_{H}$ (they are real quaternions), and general Lorentz transformations have rotors in the full algebra.

The relativistic wave equations — **Maxwell's equations** and the **Dirac equation** — have natural biquaternion forms, as developed in the companion articles.

### Quantum Physics in $\mathbb{B}_{\Psi}$

A point of the informational sector is written in its own coordinates as

$$
\tilde H_\Psi = h_t\,e_t + i\vec h_\Psi = h_t\,e_t + (i h'_{x})\,\vec e_x + (i h'_{y})\,\vec e_y + (i h'_{z})\,\vec e_z \in \mathbb{B}_{\Psi},
$$

the real temporal coordinate $h_t$, a length, together with the three imaginary spatial coordinates $i h'_{x}, i h'_{y}, i h'_{z}$.
The informational sector $\mathbb{B}_{\Psi}$ is, exactly, the **Hermitian part** of the operator algebra of a two-state quantum system: its elements are the observables, and they generate the full matrix algebra. This is established in the companion article *Quantum Physics in Biquaternionic Form*, and it can be summarized as follows.

- The **elements** of $\mathbb{B}_{\Psi}$, of the form $\tilde H_\Psi = h_t\,e_t + i\vec h_\Psi$ with $\vec h_\Psi = h'_x\vec e_x + h'_y\vec e_y + h'_z\vec e_z$ and $h_t, h'_x, h'_y, h'_z \in \mathbb{R}$ — the scalar coefficient real and the vector coefficients imaginary, which is the usual writing of quantum physics — are the observables (they are automatically Hermitian by definition of $\mathbb{B}_{\Psi}$), with spectral decomposition in terms of idempotents.
- The **idempotents** in $\mathbb{B}_{\Psi}$, of the form $\tilde\Pi_{1,2}(\vec u) = \tfrac{1}{2}(e_t \pm i\vec u)$ with $\vec u$ a unit pure real quaternion, are the pure states of a qubit. They parametrize the Bloch sphere $S^2$.
- The **positive elements** in $\mathbb{B}_{\Psi}$ normalised by $\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}=\tfrac12\langle e_t\rangle_{*}$, of the form $\tilde{Ϛ}_{\Psi} = \tfrac{1}{2}(e_t + i\vec r)$ with $|\vec r| \leq 1$, are the mixed states (trace one in the $2\times2$ image), parametrizing the Bloch ball.
- The **normalised Hermitian form** $\langle\tilde{Ϛ}_{\Psi},\tilde H_\Psi\rangle_{*}/\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*} = h_t + \vec r\cdot\vec h_\Psi$ gives the Born rule, read in the $2\times2$ image as $\operatorname{Tr}(\tilde{Ϛ}_{\Psi}\tilde H_\Psi^{*})/\operatorname{Tr}(\tilde{Ϛ}_{\Psi})=\operatorname{Tr}(\tilde{Ϛ}_{\Psi}\tilde H_\Psi)/\operatorname{Tr}(\tilde{Ϛ}_{\Psi}) = h_t + \vec r\cdot\vec h_\Psi$, the star being inert on $\mathbb{B}_{\Psi}$ and the unstarred trace real; it is a consequence of the algebra rather than an independent postulate.
- The **two-sided operation** $\tilde{Ϛ}_{\Psi} \mapsto \tilde\Pi\tilde{Ϛ}_{\Psi}\tilde\Pi/\langle\tilde\Pi\tilde{Ϛ}_{\Psi}\tilde\Pi,e_t\rangle_{*}$ gives the projective measurement and state update (the denominator normalises the post-measurement state; its $2\times2$ reading is $\mathrm{Tr}(\tilde\Pi\tilde{Ϛ}_{\Psi}\tilde\Pi)$).
- The **$*$-unitary elements** of $\mathbb{B}$, and their conjugation action $\tilde{Ϛ}_{\Psi} \mapsto \tilde Q\tilde{Ϛ}_{\Psi}\tilde Q^{*}$, give the reversible evolution.
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

2. **Coupling between the two sectors.** Beyond the Lorentz coupling via the rotor conjugation, is there a genuinely new coupling between the anti-Hermitian subspace $\mathbb{B}_{\Phi}$ and the Hermitian subspace $\mathbb{B}_{\Psi}$? Any such coupling would be where new physical content could reside. One minimal instance is already algebraic and not imposed: the **square**. For a material element the quaternionic square is the interval, $\tilde R_\Phi^{\natural}\tilde R_\Phi=\langle\tilde R_\Phi\rangle_{\natural}e_t$ with $\langle\cdot\rangle_{\natural}$ real, and the real scalar line lies in $\mathbb{B}_{\Psi}$, so squaring is a map $\mathbb{B}_{\Phi}\to\mathbb{B}_{\Psi}$ supplied by the product itself — the interpretation carried by *The Physical Interpretation of the 12 Products*. What remains open is a coupling with a dynamics; the square is a map, not an evolution.

3. **Extension to many qubits and to quantum field theory.** The quantum formalism presented in the companion article is for a single qubit. The extension to $n$ qubits (via the tensor product $\mathbb{B}^{\otimes n} \cong M_{2^n}(\mathbb{C})$), the second-quantized version, and the connection to quantum field theory remain to be developed.

4. **Relativistic quantum theory.** The biquaternion algebra contains both the Lorentz group and the operator algebra of quantum physics. A fully relativistic quantum theory of spinor fields — whose classical precursor is the biquaternion Dirac equation — is the natural continuation of the framework.

5. **Curved spacetime.** The framework so far is formulated on flat spacetime. Its extension to curved spacetime, and its relation to general relativity, remain open.

6. **Empirical contact.** What quantitative prediction distinguishes this framework from standard physics? This is the central open question, and the one on which the eventual evaluation of the hypothesis will depend.

The framework is offered as a structural intuition: that the two natural subspaces of the biquaternion algebra have distinct physical roles — one material, one informational — and that the algebra $\mathbb{B}$ is the natural home in which both relativity and quantum physics are expressed. The local speed of light $c = 1/\sqrt{\epsilon\mu}$ is the local scale of the complex structure. Since the four coefficients are lengths, that scale does not appear in the element itself; it appears in the conversion $t'=r'_t/c$, and in the numbers a clock and a ruler report of the same point. The vacuum case $c=c_0$ is the special case of it, in the same way that special relativity is a local approximation of general relativity.

## Physical Readings

Two interpretations of the introduction are worth separating. Read as a statement about invariance, the universe of the article is the sesquilinear pair: a change of the local complex structure moves the interval and the composition and leaves the probability form, the gauge calibration and the zero-divisor cone where they were (*Algebra and Element Conventions*). Read in time, its two sectors are two clocks reading one hand: the material time and the informational time are the two projections of one central coordinate, so each sector's time is read against the phase of the other (*Each Sector Is the Other's Clock: the Sector Exchange as Relational Time*). Four further readings can be named.

- **Amplitude interpretation.** Each complex coefficient $Q_\mu$ is one complex number, that is, a magnitude and a phase, so the arena of the framework is complex before any quantum interpretation is imposed: the two sectors are read as the real and the imaginary halves of one amplitude, and an element is a point of the complexified spacetime together with its conjugate amplitude data. Boundary: the interpretation names the shape of the coefficient and supplies neither a quantisation nor a measurement rule.
- **State-preparation interpretation.** The central map $\tilde H_\Psi=-\tfrac{i}{2}\tilde R_\Phi$ carries a material four-vector to an informational element, and on the trace-one slice of the future cone to a state: the four-vector $i r'_t\,e_t+\vec r_\Phi$ is carried to $\tfrac12(h_t\,e_t+i\vec h_\Psi)$ with $h_t=r'_{t}$ and $\vec h_\Psi=-\vec r_\Phi$, so that $\mathrm{Tr}(\tilde H_\Psi)=h_t=r'_{t}$ and $\langle\tilde H_\Psi\rangle_{\natural}=-\tfrac14\langle\tilde R_\Phi\rangle_{\natural}$, so on the slice $r'_{t}=1$ of the length unit, with $\lvert\vec r_\Phi\rvert\le1$, it is the Hermitian state $\tilde{Ϛ}_{\Psi}=\tfrac12(e_t+i\vec r)$ with $\vec r=-\vec r_\Phi$ and $|\vec r|\le1$. Boundary: the map is the mirror dictionary of *The Bloch Ball as the Normalised Slice of the Future Light Cone*, which owns it, and the interpretation names a preparation and not a dynamics.
- **Cross-sector coupling by the square.** For a material element the quaternionic square is the interval itself, $\tilde R_\Phi^{\natural}\tilde R_\Phi=\langle\tilde R_\Phi\rangle_{\natural}e_t$ with $\langle\cdot\rangle_{\natural}$ real, and the real scalar line lies in $\mathbb{B}_{\Psi}$: squaring is therefore one algebraic map $\mathbb{B}_{\Phi}\to\mathbb{B}_{\Psi}$, the minimal instance of the coupling asked for in question 2 above, supplied by the product rather than added by hand. The product of *two* material elements is not in general informational, while the *square of one* is. Boundary: one map, with image the real scalar line, and no dynamics; the identity is owned by *The Physical Interpretation of the 12 Products*, and its grid-level pointer is *The Four General Products: Composition, Probability, Causality, Gauge*.
- **One locus, two lists.** The norm's zero set $\langle\tilde{Q}\rangle_{\natural}=0$ is the light cone of the material sector and it is also the locus on which the pure states of the informational sector sit: the idempotents $\tilde\Pi=\tfrac12(e_t\pm i\vec u)$ have $\langle\tilde\Pi\rangle_{\natural}=0$. The causal boundary and the list of pure states are one algebraic locus read twice, the zero-divisor cone. Boundary: the interpretation identifies sets, and it does not make every null element a pure state, the null cone being strictly larger than the set of idempotents; the state side is *The Physical Interpretation of the 12 Products*, and the cone itself *The Light Cone as the Biquaternion Zero-Divisor Cone*.

## Summary

The framework is stated in one sentence: the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ is the common biquaternion space of relativity and quantum physics, and its two natural real subspaces carry the two theories. The **anti-Hermitian subspace** $\mathbb{B}_{\Phi}$ carries the four-vectors of relativity, the material sector, in the coordinates $(i r'_t,r_x,r_y,r_z)$; the **Hermitian subspace** $\mathbb{B}_{\Psi}$ carries the operator algebra of quantum physics, the informational sector, in the coordinates $(h_t,i h'_{x},i h'_{y},i h'_{z})$. Multiplication by $i$ exchanges the two.

Both sectors are written in the one biquaternion space. A material element is $\tilde R_\Phi=i r'_t\,e_t+\vec r_\Phi$ and an informational element is $\tilde H_\Psi=h_t\,e_t+i\vec h_\Psi$, with $\vec r_\Phi = r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$ and $\vec h_\Psi = h'_{x}\,\vec e_x+h'_{y}\,\vec e_y+h'_{z}\,\vec e_z$; the two are the parts of one element, $\tilde Q=\tilde H_\Psi+\tilde R_\Phi$, and the norm $\langle\tilde{Q}\rangle_{\natural}=\sum_\mu Q_\mu^2$ is the interval on $\mathbb{B}_{\Phi}$, of signature $(3,1)$ there, and the Hermitian form $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}=\sum_\mu Q_{1\mu}\overline{Q_{2\mu}}$ is the probability weight on $\mathbb{B}_{\Psi}$. The Lorentz rotors are the unit-norm elements $\tilde U_{\mathrm{lor}}$ with $\tilde U_{\mathrm{lor}}\tilde U_{\mathrm{lor}}{}^{\natural}=e_t$, acting by conjugation; the idempotents $\tilde\Pi_{1,2}(\vec u)=\tfrac12(e_t\pm i\vec u)$ are the pure states of the informational sector; and the observables are the Hermitian elements $\tilde H_\Psi=h_t\,e_t+i\vec h_\Psi$ with $h_t$ real.

The framework is a research program, not a finished theory. The algebraic identifications above are established mathematics; what is open is whether the framework has consequences beyond a reformulation of known physics. Six questions are recorded: the physical reality of the biquaternionic structure; a coupling between the sectors beyond the Lorentz conjugation, of which the square $\mathbb{B}_{\Phi}\to\mathbb{B}_{\Psi}$ is the minimal algebraic instance already supplied by the product; the extension to many qubits and to quantum field theory; a fully relativistic quantum theory; curved spacetime; and empirical contact. The local speed of light $c=1/\sqrt{\epsilon\mu}$ is the local scale of the complex structure; it stays out of the element, whose four coefficients are lengths, and enters only the conversion between the length coordinate and the second.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\tilde{Q} = Q_t e_t + \vec Q = \sum_\mu Q_\mu e_\mu$ | General biquaternion (eight real parameters), with $\vec Q = Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ its vector part |
| $Q_\mu = q_\mu+iq'_\mu$ | Complex coefficient: $q_\mu$ its real part (the coefficient of $e_\mu$), $q'_\mu$ its imaginary part (the coefficient of $ie_\mu$); the four coefficients are lengths, and no factor of $c$ stands on the time |
| $\tilde Q = \tilde H_\Psi + \tilde R_\Phi$ | The split into the informational part $\tilde H_\Psi$, Hermitian, and the material part $\tilde R_\Phi$, anti-Hermitian |
| $\tilde R_\Phi = i r'_t\,e_t + \vec r_\Phi = i r'_t\,e_t + r_x\vec e_x + r_y\vec e_y + r_z\vec e_z$ | Material element, with $\vec r_\Phi=r_x\vec e_x+r_y\vec e_y+r_z\vec e_z$ its vector part |
| $\tilde H_\Psi = h_t\,e_t + i\vec h_\Psi = h_t\,e_t + i(h'_{x}\,\vec e_x+h'_{y}\,\vec e_y+h'_{z}\,\vec e_z)$ | Informational part, Hermitian, with $\vec h_\Psi=h'_x\vec e_x+h'_y\vec e_y+h'_z\vec e_z$ its vector part; $h_t$ is real, the three $h'_\eta$ are imaginary, and the four are the informational coordinates |
| $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$ | Biquaternion norm; its coefficient tuple is the unit metric $\delta_{\mu\nu}=(1,1,1,1)$, the identity, in every frame; the interval it gives on the real material sector has signature $(3,1)$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*} = \sum_\mu Q_{1\mu}\overline{Q_{2\mu}}$ | Hermitian form, positive definite; the probability weight, $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{*} = \sum_\mu\lvert Q_{2\mu}\rvert^{2}$; the coefficient of $e_t$ in $\tilde{Q}\tilde{Q}^{*}$ |
| ${}^{\natural}$ | Quaternion conjugate: reverses the quaternion basis, $e_t^{\natural}=e_t$ and $\vec e_\eta^{\natural}=-\vec e_\eta$, and leaves the complex coefficients $Q_\mu$ untouched; the conjugation of the norm, $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural}$ |
| $\overline{\cdot}$ | Bar, the coefficient conjugation: conjugates each complex coefficient $Q_\mu$ and leaves the quaternion basis untouched, $\overline{\tilde{Q}} = \sum_\mu \overline{Q_\mu}\,e_\mu$; the conjugation of the Hermitian form, $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*} = \sum_\mu Q_{1\mu}\overline{Q_{2\mu}}$ |
| ${}^{*} = \overline{\cdot}\circ{}^{\natural}$ | Hermitian conjugation: conjugates both factors, $\tilde{Q}^{*} = \overline{Q_t}e_t - \overline{Q_x}\vec e_x - \overline{Q_y}\vec e_y - \overline{Q_z}\vec e_z$; the conjugation that defines the two sectors, the fixed points of ${}^{*}$ being $\mathbb{B}_{\Psi}$ |
| ${}^{\flat} = -{}^{*}$ | Anti-Hermitian conjugation: the star composed with the central sign, $\tilde{Q}^{\flat} = -\tilde{Q}^{*}$, of which the material sector $\mathbb{B}_{\Phi}$ is the fixed-point set |
| $\mathbb{B}_{\Phi}$ | Anti-Hermitian subspace (material sector): coordinates $(i r'_t, r_x, r_y, r_z)$, parameters $r'_t, r_x, r_y, r_z$ |
| $\mathbb{B}_{\Psi}$ | Hermitian subspace (informational sector): coordinates $(h_t, i h'_{x}, i h'_{y}, i h'_{z})$, parameters $h_t, h'_x, h'_y, h'_z$ |
| $\mathbb{B}_{H}$ | Real quaternion subspace (home of the rotation rotors): the real half, all four coefficients real, fixed points of complex conjugation; a subalgebra |
| $\mathbb{B}_{iH}$ | Antiquaternion subspace: the imaginary half, all four coefficients purely imaginary, the partner of $\mathbb{B}_{H}$ in $\mathbb{B} = \mathbb{B}_{H} \oplus \mathbb{B}_{iH}$. This split crosses the $\mathbb{B}_{\Psi}/\mathbb{B}_{\Phi}$ split: the scalar of $\mathbb{B}_{\Phi}$ and the vectors of $\mathbb{B}_{\Psi}$ come from here |
| $\tilde\Pi_{1,2}(\vec u) = \tfrac{1}{2}(e_t \pm i\vec u)$ | Idempotent (pure state of the informational sector) |
| $\tilde{Ϛ}_{\Psi} = \tfrac{1}{2}(e_t + i\vec r)$, $\lvert\vec r\rvert \le 1$ | Mixed state (positive, trace one). The Bloch vector $\vec r$ carries no sector label and is distinct from the two vector parts $\vec r_\Phi$ and $\vec h_\Psi$ |
| $(r'_t,r_x,r_y,r_z)$ | Real coordinates of the material sector, all four in metres; the speed of light is a conversion and not a coordinate |
| $(h_t, h'_{x}, h'_{y}, h'_{z})$ | Real coordinates of the informational sector, all four in metres |
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
