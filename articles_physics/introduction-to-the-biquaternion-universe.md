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

The subspace $\mathbb{B}_{\Phi}$ is the **anti-Hermitian subspace**, the fixed-point set of the anti-Hermitian conjugation $\flat$ (equivalently, the eigenspace of the Hermitian conjugation ${}^{*}$ with eigenvalue $-1$). The subspace $\mathbb{B}_{\Psi}$ is the **Hermitian subspace**, the fixed-point set of the Hermitian conjugation ${}^{*}$ (equivalently, its eigenspace with eigenvalue $+1$). The two are complementary: together they span $\mathbb{B}$, and their intersection is trivial. Every element of the algebra splits accordingly, $\tilde Q=\tilde Q_\Psi+\tilde Q_\Phi$, into its **material part** $\tilde Q_\Phi\in\mathbb{B}_{\Phi}$ and its **informational part** $\tilde Q_\Psi\in\mathbb{B}_{\Psi}$; an element of $\mathbb{B}_{\Phi}$ is its own material part, and an element of $\mathbb{B}_{\Psi}$ its own informational part. Both halves carry the one glyph, and the sector mark alone separates them; the general element $\tilde Q$ takes no sector mark, since its sector depends on its value.

The two subspaces have distinct physical roles.

- **$\mathbb{B}_{\Phi}$ is the material sector**, the anti-Hermitian subspace. It is the home of the four-vectors of relativistic physics, with an imaginary temporal coordinate; time can be measured, but it cannot be touched, held or moved through. Written out in four real parameters,

    $$
    \tilde Q_\Phi = i q'_t\,e_t + \vec Q_\Phi = i q'_t\,e_t + q_x\vec e_x + q_y\vec e_y + q_z\vec e_z \in \mathbb{B}_{\Phi},
    $$

    where $q'_t$ is the material temporal coordinate, a length, and $\vec Q_\Phi = q_x\vec e_x + q_y\vec e_y + q_z\vec e_z$ the material space.

- **$\mathbb{B}_{\Psi}$ is the informational sector**, the Hermitian subspace. It is the home of the Hermitian operators, whose algebraic structure is that of a quantum-mechanical state space: its elements are the states, observables and measurement operators of a qubit. The name reflects that content, and claims nothing about entropy. Written out in four real parameters,

    $$
    \tilde Q_\Psi = q_t\,e_t + i\vec Q_\Psi = q_t\,e_t + i\bigl(q'_x\vec e_x + q'_y\vec e_y + q'_z\vec e_z\bigr) \in \mathbb{B}_{\Psi},
    $$

    where $q_t$ is the informational temporal coordinate, a length, and $\vec Q_\Psi = q'_x\vec e_x + q'_y\vec e_y + q'_z\vec e_z$ the informational space.

In both cases the parameter is the coordinate, and no conversion stands between them. The prime falls on the **scalar** $q'_t$ in $\mathbb{B}_{\Phi}$ and on the **three vectors** $q'_\eta$ in $\mathbb{B}_{\Psi}$, which is what makes the two sectors mirror images. The complex structure is then visible as a count: the material sector has three real spatial directions and one imaginary temporal direction, the informational sector three imaginary spatial directions and one real temporal direction.

## The Complex Coordinates

Writing the biquaternion coordinate in terms of its material and informational parts,

$$
\tilde{Q} = \underbrace{(i q'_t)\,e_t + (q_x\,\vec e_x + q_y\,\vec e_y + q_z\,\vec e_z)}_{=\,\tilde Q_\Phi\,\in\,\mathbb{B}_{\Phi}} \;+\; \underbrace{(q_t)\,e_t + (i q'_{x}\,\vec e_x + i q'_{y}\,\vec e_y + i q'_{z}\,\vec e_z)}_{=\,\tilde Q_\Psi\,\in\,\mathbb{B}_{\Psi}},
$$

Each sector is four-dimensional, and the complexified spacetime is their direct sum.

The unprimed parameter is throughout the **real part** of the complex coefficient and the primed one its **imaginary part**. The two sectors take disjoint halves of the eight parameters — $\mathbb{B}_{\Phi}$ takes $q'_t$ together with the three $q_\eta$, $\mathbb{B}_{\Psi}$ takes $q_t$ together with the three $q'_\eta$ — so four complex coefficients and eight real parameters carry exactly the same information.

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

The norm $\langle\cdot\rangle_{\natural}$ and the quaternion conjugate ${}^{\natural}$ that appear here are defined in *Summary of Notation*, at the end of the article.

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

The informational sector $\mathbb{B}_{\Psi}$ is, exactly, the **Hermitian part** of the operator algebra of a two-state quantum system: its elements are the observables, and they generate the full matrix algebra. The subspace is a real vector space and not a subalgebra: the product of two Hermitian elements is not in general Hermitian, and only its symmetric half stays in the sector. The operator product is therefore taken with a conjugation on one factor (*The Four Products*), not as a multiplication internal to $\mathbb{B}_{\Psi}$. This is established in the companion article *Quantum Physics in Biquaternionic Form*, and it can be summarized as follows. The Hermitian form $\langle\cdot,\cdot\rangle_{*}$ that appears below is defined in *Summary of Notation*, at the end of the article.

- The **elements** of $\mathbb{B}_{\Psi}$, of the form $\tilde Q_\Psi = q_t\,e_t + i\vec Q_\Psi$ with $\vec Q_\Psi = q'_x\vec e_x + q'_y\vec e_y + q'_z\vec e_z$ and $q_t, q'_x, q'_y, q'_z \in \mathbb{R}$ — the scalar coefficient real and the vector coefficients imaginary, which is the usual writing of quantum physics — are the observables (they are automatically Hermitian by definition of $\mathbb{B}_{\Psi}$), with spectral decomposition in terms of idempotents. The correspondence runs both ways: the Hermitian elements of $\mathbb{B}$ are exactly the elements of $\mathbb{B}_{\Psi}$, and the observables of the two-state system are exactly the Hermitian $2\times2$ matrices, so nothing outside $\mathbb{B}_{\Psi}$ is an observable and no element of $\mathbb{B}_{\Psi}$ is idle. The four parameters are then the four numbers a measurement of that observable reports: the two outcomes are $q_t \pm \lvert\vec Q_\Psi\rvert$, so $q_t$ is their mean and the vector $\vec Q_\Psi$ fixes their half-splitting.
- The **idempotents** in $\mathbb{B}_{\Psi}$, of the form $\tilde\Pi_{\mathrm{id},1,2}(\vec u) = \tfrac{1}{2}(e_t \pm i\vec u)$ with $\vec u$ a unit pure real quaternion, are the pure states of a qubit. They parametrize the Bloch sphere $S^2$.
- The **positive elements** in $\mathbb{B}_{\Psi}$ normalised by $\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}=\tfrac12\langle e_t\rangle_{*}$, of the form $\tilde{Ϛ}_{\Psi} = \tfrac{1}{2}(e_t + i\vec s_{\Psi})$ with $|\vec s_{\Psi}| \leq 1$, are the mixed states (trace one in the $2\times2$ image), parametrizing the Bloch ball.
- The **two-sided operation** $\tilde{Ϛ}_{\Psi} \mapsto \tilde\Pi_{\mathrm{id}}\tilde{Ϛ}_{\Psi}\tilde\Pi_{\mathrm{id}}/\langle\tilde\Pi_{\mathrm{id}}\tilde{Ϛ}_{\Psi}\tilde\Pi_{\mathrm{id}},e_t\rangle_{*}$ gives the projective measurement and state update (the denominator normalises the post-measurement state; its $2\times2$ reading is $2\,\mathrm{Sc}(\tilde\Pi_{\mathrm{id}}\tilde{Ϛ}_{\Psi}\tilde\Pi_{\mathrm{id}})$).
- The **$*$-unitary elements** of $\mathbb{B}$, and their conjugation action $\tilde{Ϛ}_{\Psi} \mapsto \tilde Q\tilde{Ϛ}_{\Psi}\tilde Q^{*}$, give the reversible evolution.
- The distinction between **reversible evolution** and **irreversible measurement** is a property of the acting element ($*$-unitary vs. idempotent), not an additional postulate.
The operator algebra of quantum physics, its state space, its Born rule, and its measurement rule are all **structural consequences** of the algebra of $\mathbb{B}_{\Psi}$. They are not imposed from outside. The two-state formalism at large is *Quantum Physics in Biquaternionic Form*; the derivation of the Born rule, and its comparison with the postulate it replaces, are *The Born Rule from the Hermitian Form — Derivation and Comparison*; the states that the indefinite fourth product cannot normalise are *The Physical Interpretation of the 12 Products*; and the decoherence of a measurement is *Decoherence as Idempotent Projection*.

The framework is proposed in this sense: not as a modification of relativity or of quantum physics, but as a **common biquaternion space** on which both are already expressed.

### The Four Products

The biquaternion algebra carries four products, and each takes two elements. In each of them the first element is read as it stands or through the quaternion conjugate ${}^{\natural}$, and the second as it stands or through the Hermitian conjugation ${}^{*}$. The two choices are independent, so the four are

$$
\tilde Q_1\tilde Q_2,\qquad \tilde Q_1^{\natural}\tilde Q_2,\qquad \tilde Q_1\tilde Q_2^{*},\qquad \tilde Q_1^{\natural}\tilde Q_2^{*},
$$

all read on the same eight coordinates. In the last two the conjugation falls on the second argument, so the order cannot be swapped. Each of the four also splits into a symmetric and an antisymmetric part, which gives twelve products in all. The four, with their halves and their names, are tabulated in *The Four General Products: Composition, Probability, Causality, Gauge*.

## The Vacuum Limit

In vacuum the local speed of light is the constant $c_0$; in a material medium it is $c=1/\sqrt{\epsilon\mu}$ and varies from point to point. Neither value enters the coordinate, because the four coefficients are lengths in either case. The identification $r'_t\mapsto i r'_t$ is the same at every point; what is local is its scale, and the scale is read through the one conversion the scheme still uses, $t=q'_t/c$, wherever a clock is compared with a length. The writing of an element is therefore the same in vacuum and in a medium, in the same spirit as the metric of general relativity, which is local while the coordinates of a chart are not.

## Physical Readings

Two interpretations of the introduction are worth separating. Read as a statement about invariance, the universe of the article is the sesquilinear pair: a change of the local complex structure moves the interval and the composition and leaves the probability form, the gauge calibration and the zero-divisor cone where they were (*Algebra and Element Conventions*). Read in time, its two sectors are two clocks reading one hand: the material time and the informational time are the two projections of one central coordinate, so each sector's time is read against the phase of the other (*Relational Time from the Sector Exchange: The Material and Informational Clocks*). Four further readings can be named:

- The **amplitude interpretation** treats each complex coefficient $Q_\mu$ as one complex number, a magnitude and a phase, so the arena of the framework is complex before any quantum interpretation is imposed: an element is a point of the complexified spacetime together with its conjugate amplitude data. Boundary: the interpretation names the shape of the coefficient and supplies neither a quantisation nor a measurement rule.
- The **state-preparation interpretation** reads the central map $\tilde Q_\Psi=-\tfrac{i}{2}\tilde Q_\Phi$ as carrying a material four-vector to an informational element, and on the normalised slice of the future cone to a state: the four-vector $i q'_t\,e_t+\vec Q_\Phi$ is carried to $\tfrac12(q_t\,e_t+i\vec Q_\Psi)$ with $q_t=q'_{t}$ and $\vec Q_\Psi=-\vec Q_\Phi$, so that $2\,\mathrm{Sc}(\tilde Q_\Psi)=q_t=q'_{t}$ and $\langle\tilde Q_\Psi\rangle_{\natural}=-\tfrac14\langle\tilde Q_\Phi\rangle_{\natural}$, so on the slice $q'_{t}=1$ of the length unit, with $\lvert\vec Q_\Phi\rvert\le1$, it is the Hermitian state $\tilde{Ϛ}_{\Psi}=\tfrac12(e_t+i\vec s_{\Psi})$ with $\vec s_{\Psi}=-\vec Q_\Phi$ and $|\vec s_{\Psi}|\le1$. Boundary: the map is the dictionary of *The Bloch Ball as the Normalised Slice of the Future Light Cone*, and it names a preparation, not a dynamics.
- The **cross-sector coupling by the square** is the minimal instance of the coupling asked for under *Coupling between the sectors* in *Status and Open Questions*: for a material element the quaternionic square is the interval itself, $\tilde Q_\Phi^{\natural}\tilde Q_\Phi=\langle\tilde Q_\Phi\rangle_{\natural}e_t$ with $\langle\cdot\rangle_{\natural}$ real, and the real scalar line lies in $\mathbb{B}_{\Psi}$: squaring is therefore one algebraic map $\mathbb{B}_{\Phi}\to\mathbb{B}_{\Psi}$, supplied by the product rather than added by hand. The product of *two* material elements is not in general informational, while the *square of one* is. Boundary: one map, with the real scalar line as image, and no dynamics; the identity is *The Physical Interpretation of the 12 Products*.
- The **one locus, two lists** reading notes that the norm's zero set $\langle\tilde{Q}\rangle_{\natural}=0$ is the light cone of the material sector and it is also the locus on which the pure states of the informational sector sit: the idempotents $\tilde\Pi_{\mathrm{id}}=\tfrac12(e_t\pm i\vec u)$ have $\langle\tilde\Pi_{\mathrm{id}}\rangle_{\natural}=0$. The causal boundary and the list of pure states are one algebraic locus read twice, the zero-divisor cone. Boundary: it identifies sets, and it does not make every null element a pure state, the null cone being strictly larger than the set of idempotents.

## New Results, a Non-Exhaustive List

The list below is **not exhaustive**. It holds some results obtained in the corpus. Each entry names the article that owns it and carries one status word: *proved* when the algebra fixes it, *proposed* when one physical premise is added to a proved algebraic statement, and *ledger* when the content is measured data used arithmetically.

- The **Lorentz action on the informational sector** (*The Lorentz Group on the Bloch Ball*). A rotation rotor is a real quaternion, hence $*$-unitary: its congruence preserves the trace-one slice, rotates the Bloch vector, and is a channel. A boost rotor is Hermitian, of unit biquaternion norm and not $*$-unitary: it preserves the cone and that norm, it does not preserve the slice — it carries the slice off itself, positivity kept and normalisation lost — and after renormalisation the read radius rises, the maximally mixed state going to $\lvert\vec s_{\Psi}\rvert=\tanh\theta_{\mathrm{rpd}}$, where $\theta_{\mathrm{rpd}}$ is the rapidity of the boost. Proved algebraically. Only one premise is proposed physically: that the frame dependence so obtained is the frame dependence of a quantum state.

- The **Four Colours Left–Right Model** (*The Four Colours Left–Right Model*). An extension of the Standard Model, fully compatible with the biquaternion algebra and without contradiction to any experimental result: no measurement contradicts it, because every departure from the Standard Model sits at or above the colour-breaking scale, and that scale enters as a lower bound and never as an upper one. It corresponds structurally with the Pati–Salam model, without its coupling overclaims. Every observed elementary particle and its antiparticle is inside it, and none is put in by hand: the sixteen of one generation, taken three times, holds the six quarks, the electron, the muon, the tau and their neutrinos, each antiparticle being a conjugate mode of the same field and not a second multiplet; the boson table holds the eight gluons, the photon, $W^{\pm}$ and $Z$; and the scalar sector holds the $125$ GeV state. The states the model adds — six leptoquarks, $W_R^{\pm}$, $Z_R$ and the heavier scalars — are its own predictions and not observations, and where the model is recorded as failing it fails on a mass relation and not on a missing state. Status: a model, whose group content is derived and whose couplings are declared.

- The **Excitation Ladder Theory of Flavour** (*The Excitation Ladder Theory of Flavour*). A theory of flavour, the species of an elementary particle: the flavours are rungs of one tower, the tower has three rungs, and the count is measured rather than derived. Status: a ledger, every mass, lifetime and ratio in it being measured data, with exact arithmetic on measured numbers as the whole of the test.

- The **thermality, renormalization-group and Matsubara constructions without the Wick rotation** (*The Matsubara Thermal Formalism in Biquaternionic Form*; *The KMS Condition and the Biquaternion Framework*; *The Renormalization Group in Biquaternionic Form*). The Gibbs state is the orbit of the maximally mixed state under a boost of the thermal rapidity $\Theta$, $\tilde\varsigma_\beta=\tfrac12(e_t+i\tanh\Theta\,\vec u_B)$, so the thermal family is a diameter of the Bloch ball, of radius $\tanh\Theta$. The cutoff is the invariant of a material element, $\tilde P_{\Phi,E}=ik_{\mathrm{eu},0}e_t+\vec p$, read through the Hermitian form, $\langle\tilde P_{\Phi,E},\tilde P_{\Phi,E}\rangle_{*}=(k_{\mathrm{eu},0})^{2}+\lvert\vec p\rvert^{2}\ge 0$, positive because that form is definite. The thermal circle is the material direction $i r'_t$ already present in $\mathbb{B}_{\Phi}$, and it supplies the propagator, the frequency grid and the free energy. The identity $\langle i k_{\mathrm{eu},0}e_t+\vec p,\,i k_{\mathrm{eu},0}e_t+\vec p\rangle_{*}=\langle -k_{\mathrm{eu},0}e_t+\vec p\rangle_{\natural}=k_{\mathrm{eu},0}^{2}+\lvert\vec p\rvert^{2}$ reads the same four numbers twice, as the probability and as the Euclidean interval of the real element $-k_{\mathrm{eu},0}e_t+\vec p$; the Minkowski interval of that material element is the same number with the sign of its time term reversed, $\langle\tilde P_{\Phi,E}\rangle_{\natural}=-k_{\mathrm{eu},0}^{2}+\lvert\vec p\rvert^{2}$. Proved from the definitions; the temperature and the cutoff remain inputs.

- The **improvement over quaternionic quantum mechanics** (*The Biquaternion Universe as an Improvement of the Quaternionic Quantum Theory*). Taking the complex numbers as scalars and the quaternion units as elements of the algebra removes three of the five limits recorded by the earlier quaternionic programme: the non-commuting scalars, the conjugacy-class spectrum and the phase group $\mathrm{SU}(2)$. A fourth survives only in its algebra form, the non-closure $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}\cong M_{4}(\mathbb{C})\neq\mathbb{B}$ that every matrix algebra shares. The fifth, the complex structure that programme found to be forced, is adopted and proved, since an invertible element preserving the Hermitian norm for every Hermitian generator lies in the centre, and the centre is $\mathbb{C}e_t$. Status: a comparison theorem, with an interpretation of which limits are physical; its price is empirical equivalence with ordinary quantum mechanics.

- A **multi-qubit extension** (*Composite Systems and the Multi-Qubit Extension*; *The Multi-Qubit Split, I*; *The Multi-Qubit Split, II*). $n$ qubits are $S^{\otimes n}=\mathbb{C}^{2^{n}}$ with joint algebra $M_{2^{n}}(\mathbb{C})$, the biquaternion algebra at $n=1$ and never again. The per-subsystem sector label does not descend, and the four corners of the tensor product collapse pairwise, the two aligned ones onto the Hermitian part and the two cross ones onto the anti-Hermitian part, so the one bit that survives is the parity of the number of material factors, read as the sign under the total star $*^{\otimes n}$, a property of the whole and not of any member. Nothing observable is lost, the observables of $n$ qubits being exactly the Hermitian part of $M_{2^{n}}(\mathbb{C})$. What composes is the module and not the element; the alternating form of the one-qubit space tensors, and its tensor square evaluated on a two-qubit state is twice the determinant of the coefficient array, whose modulus is the concurrence. Proved.

Each entry is a structure, and none is yet a measurement that separates it from standard physics.

## Status and Open Questions

The framework is a research programme, not a finished theory. Its algebraic results — that $\mathbb{B}_{\Phi}$ carries the four-vectors of relativity and $\mathbb{B}_{\Psi}$ the operator algebra of quantum physics — are established mathematics. Whether it has consequences beyond a reformulation of known physics is not established. Six questions follow, none closed:

- The **physical reality of the structure** is sharpened, not answered. *The Empirical Status of the Biquaternion Framework* finds the framework empirically equivalent to standard physics on every domain developed: every quantity the algebra fixes is fixed identically by the standard theory, so a test needs an input the algebra does not contain — a scale, a coupling, or a selection principle. *The Parameter Count as the Measure of the Framework's Boundary* records that it fixes none of the nineteen Standard Model parameters. Missing: an argument that the algebra is selected rather than convenient. No article supplies one.
- The **coupling between the sectors** is built as maps and as thermodynamics, open as dynamics. Neither sector is an algebra: the product of two Hermitian elements is Hermitian exactly when they commute, and the product of two material elements is material exactly when they anticommute, so no composition can be read inside one sector (*The Sector Map and Its Exact Parts*). Two maps exist: multiplication by $i$, exact on the Lorentz congruence and preserving the Hermitian form, and the square $\tilde Q_\Phi^{\natural}\tilde Q_\Phi=\langle\tilde Q_\Phi\rangle_{\natural}e_t$, which carries a material element into the real scalar line of $\mathbb{B}_{\Psi}$. Erasure, the demon cycle and the two sector times are written as thermodynamics. Missing: a coupling with a field, an action and a constant, named in the empirical-status article as the largest gap.
- The **many-qubit and field-theoretic extension** is built on both sides, with named remainders. $n$ qubits compose the module and not the element: $S^{\otimes n}=\mathbb{C}^{2^{n}}$, joint algebra $M_{2^{n}}(\mathbb{C})$, the partial sector label provably not descending, the observables exactly the Hermitian part. Concurrence, the GHZ and W classes, monogamy, discord and the area law follow (*Composite Systems and the Multi-Qubit Extension*; *The Multi-Qubit Split, I*; *The Multi-Qubit Split, II*). The free fields are quantized — Klein–Gordon, Dirac, Maxwell, Proca, Rarita–Schwinger, and the graviton in the linearized sector. Open inside the quantized Dirac field: a $\mathbb{B}$-intrinsic Lagrangian with a scalar pairing, a parity grading carried for the whole field, and a conserved current with no fixed frame unit (*The Quantized Dirac Field in Biquaternionic Form*).
- The **relativistic quantum theory** is built for one particle and the free field, open for the interaction. The relativistic qubit is the defining module with the left action of $SL(2,\mathbb{C})$; the Dirac equation is written with its plane waves, its non-relativistic limit and its discrete symmetries; the hydrogen spectrum is reproduced; the anomalous moment $a=\alpha/2\pi$ is transcribed with the one-particle vertex and not derived (*The Anomalous Magnetic Moment in Biquaternionic Form*). The gauge principle is an input, so the radiative corrections enter with it. Missing: an interacting theory that the algebra derives.
- The **curved-spacetime case** carries the kinematics, not the dynamics. A frame field of material elements carries a general Lorentzian metric, the algebra supplies the pointwise $SL(2,\mathbb{C})$, and a curved Dirac operator has been built with its Lichnerowicz square. Kerr–Schild is the orbit of the flat form under a null shear, which is square-zero because a null element is a zero divisor; linearized gravity and the KMS flow are carried, the Hawking temperature as a standard result (*Curved Spacetime and the Biquaternion Framework*). Missing: an action, a field equation, a selection of metric. Even the linearized Einstein equation is transcribed rather than derived (*The Einstein Field Equations in the Biquaternion Framework*).
- The **empirical contact** is absent: no measurement today separates the framework from standard physics. Candidate tests — modified dispersion, the local complex structure, birefringence, a second light cone, quaternionic deviations, dimensionless relations — each fail, because none depends on a quantity the algebra fixes and standard physics does not. A test needs a measured cross-sector effect, or a bound on one, at a stated scale. The framework is reproduced by every experiment and tested by none.

Next: whether a cross-sector coupling can be given a field and an action, whether interaction terms can be derived instead of imported, and whether the local complex structure can be given a curved spacetime with a dynamics.

The framework is offered as a structural intuition: two natural subspaces of one algebra, one material and one informational, and $\mathbb{B}$ as the home in which both theories are already expressed. The local speed of light $c=1/\sqrt{\epsilon\mu}$ is the local scale of the complex structure. Since the coefficients are lengths, that scale does not appear in the element; it appears in the conversion $t=q'_t/c$ and in the numbers a clock and a ruler report.

## Summary

The framework is stated in one sentence: the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ is the common biquaternion space of relativity and quantum physics, and its two natural real subspaces carry the two theories. The **anti-Hermitian subspace** $\mathbb{B}_{\Phi}$ carries the four-vectors of relativity, the material sector, in the coordinates $(i q'_t,q_x,q_y,q_z)$; the **Hermitian subspace** $\mathbb{B}_{\Psi}$ carries the operator algebra of quantum physics, the informational sector, in the coordinates $(q_t,i q'_{x},i q'_{y},i q'_{z})$. Multiplication by $i$ exchanges the two.

Both sectors are written in the one biquaternion space. A material element is $\tilde Q_\Phi=i q'_t\,e_t+\vec Q_\Phi$ and an informational element is $\tilde Q_\Psi=q_t\,e_t+i\vec Q_\Psi$, with $\vec Q_\Phi = q_x\,\vec e_x+q_y\,\vec e_y+q_z\,\vec e_z$ and $\vec Q_\Psi = q'_{x}\,\vec e_x+q'_{y}\,\vec e_y+q'_{z}\,\vec e_z$; the two are the parts of one element, $\tilde Q=\tilde Q_\Psi+\tilde Q_\Phi$, and the norm $\langle\tilde{Q}\rangle_{\natural}=\sum_\mu Q_\mu^2$ is the interval on $\mathbb{B}_{\Phi}$, one negative direction there, and the Hermitian form $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}=\sum_\mu Q_{1\mu}\overline{Q_{2\mu}}$ is the probability weight on $\mathbb{B}_{\Psi}$. The Lorentz rotors are the unit-norm elements $\tilde U_{\mathrm{lor}}$ with $\tilde U_{\mathrm{lor}}\tilde U_{\mathrm{lor}}{}^{\natural}=e_t$, acting by conjugation; the idempotents $\tilde\Pi_{\mathrm{id},1,2}(\vec u)=\tfrac12(e_t\pm i\vec u)$ are the pure states of the informational sector; and the observables are the Hermitian elements $\tilde Q_\Psi=q_t\,e_t+i\vec Q_\Psi$ with $q_t$ real.

The framework is a research programme, not a finished theory. The algebraic identifications above are established mathematics; what is open is whether the framework has consequences beyond a reformulation of known physics, and *Status and Open Questions* records, for each of the six, what has been built and what is missing.

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
| $\tilde\Pi_{\mathrm{id},1,2}(\vec u) = \tfrac{1}{2}(e_t \pm i\vec u)$ | Idempotent (pure state of the informational sector) |
| $\tilde{Ϛ}_{\Psi} = \tfrac{1}{2}(e_t + i\vec s_{\Psi})$, $\lvert\vec s_{\Psi}\rvert \le 1$ | Mixed state: positive, normalised by $2\operatorname{Sc}\tilde{Ϛ}_{\Psi}=1$, so its $2\times2$ image is of trace one. The Bloch vector $\vec s_{\Psi}$ carries no sector label and is distinct from the two vector parts $\vec Q_\Phi$ and $\vec Q_\Psi$ |
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