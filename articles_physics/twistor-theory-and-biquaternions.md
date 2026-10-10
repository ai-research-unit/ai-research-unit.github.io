# __Twistor Theory and Biquaternions__

## Introduction

Twistor theory is the programme, initiated by Roger Penrose in the 1960s, that recasts spacetime physics in the complex geometry of a four-dimensional complex vector space, **twistor space** $T$ [Penrose 1967; Penrose and Rindler 1986]. Its elementary object, the **twistor**, is built from a pair of two-component Weyl spinors, and its central observation is that the conformal and null structure of complexified Minkowski space is encoded in the incidence geometry of twistors.

The biquaternion framework of this series is built on the complexified quaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H} \cong M_2(\mathbb{C})$. The two programmes are often treated as distant relatives. This article places them side by side and says exactly where they agree and where they diverge. The claim is not that either is a version of the other: **twistor theory is not biquaternions, and it is not subsumed by them**. The two use some of the same algebra to answer different questions. What they share is a foundation — the spinor module $S=\mathbb{C}^2$ and the isomorphism $SL(2,\mathbb{C})\cong \mathrm{Spin}(1,3)$ — and that foundation is standard, older than either programme. What separates them is aim: twistors organise the **conformal group** and **null geometry** and work by complex-projective methods; this framework keeps the observable sector real and treats the complex structure itself as the physics.

The article first outlines the twistor construction, then exhibits the shared module, then distinguishes the several four-complex-dimensional objects that are easily confused, then compares the treatment of the null cone, and finally states the divergences in aim.

## The Twistor Programme in Outline

A **twistor** is an element of $T \cong \mathbb{C}^4$. In two-spinor notation [Penrose and Rindler 1984] it is a pair

$$
Z = (\omega^A,\, \pi_{A'}), \qquad A, A' \in \{0,1\},
$$

where $\omega^A$ is a left-handed (unprimed) two-component spinor and $\pi_{A'}$ a right-handed (primed) one. **Projective twistor space** is $\mathbb{PT} = \mathbb{CP}^3$, whose points are complex lines of twistors. Thus a point of $\mathbb{PT}$ is represented by a pair of two-component spinors, not by a single one: the four components of $Z$ are two spinor components of each chirality.

Twistor space carries a nondegenerate Hermitian form of signature $(2,2)$. Writing $T = S\oplus\bar{S}$ for the splitting into the unprimed and primed parts, the form is

$$
h(Z,Z') = \omega^{*} \pi' + \pi^\dagger \omega',
$$

and the group preserving it is $U(2,2)$. Its determinant-one subgroup $SU(2,2)$ is the double cover of the conformal group $SO(2,4)$ of compactified Minkowski space. The conformal group acts **linearly** on $T$; this linearisation of an action that is nonlinear on spacetime is the technical heart of the programme.

The link to spacetime is the **incidence relation**. A point of complexified Minkowski space is a $2\times 2$ complex matrix $x^{AA'}$ — Hermitian exactly when the point is real — and it cuts out a two-dimensional complex subspace of $T$, hence a projective line $L_x \subset \mathbb{PT}$, by

$$
\omega^A = i\,x^{AA'}\pi_{A'}.
$$

For fixed $x$ this is two linear conditions on four unknowns, so the solution space is two-dimensional: a line. Two points $x, y$ are null-separated exactly when their lines meet, and this happens exactly when $\det(x-y) = 0$, the determinant of the $2\times2$ matrix being the Minkowski interval. Thus

$$
\text{points of complexified Minkowski space} \;\longleftrightarrow\; \text{lines in } \mathbb{PT},
$$

and the correspondence is the classical **Klein correspondence**: the space of lines in $\mathbb{CP}^3$ is the four-complex-dimensional Grassmannian $\mathrm{Gr}(2,4)$, which is the conformal compactification of complexified Minkowski space. Real Minkowski space is the family of lines invariant under the conjugation (the reality condition), a real four-dimensional slice inside it. Null geometry is not described by twistors as an afterthought; it is the incidence geometry of lines.

On this base the programme builds three things. The **Penrose transform** represents solutions of the massless free-field equations on spacetime — of each helicity — by elements of sheaf cohomology groups on twistor space, the twist of the sheaf being fixed by the helicity [Penrose 1969; Huggett and Tod 1985]. The **nonlinear graviton** construction represents a class of half-flat (one of the two self-duality conditions, the naming being a convention) Ricci-flat complex spacetimes by deformations of the holomorphic structure of twistor space [Penrose 1976]. The **Ward correspondence** does the same for self-dual Yang–Mills fields [Ward 1977]. The programme is conformally invariant and specific to four dimensions.

## The Shared Foundation: The Weyl Spinor and $SL(2,\mathbb{C})$

The read-list article *The Spinor Module in Biquaternionic Form and Its Lorentz Action* develops the following objects: the algebra $\mathbb{B}\cong M_2(\mathbb{C})$; its unique simple module $S=\mathbb{C}^2$, the **spinor module**; the left- and right-handed Weyl modules $(\tfrac12,0)$ and $(0,\tfrac12)$; the four-component Dirac module $\Delta = S\oplus\bar{S}$; the one-sided Lorentz action $\psi\mapsto \tilde{\Lambda}\psi$; the invariant symplectic form $\varepsilon$; and the two-to-one covering $SL(2,\mathbb{C})\to SO^+(1,3)$ whose kernel $\{\pm e_0\}$ acts as $\pm\mathrm{id}$ on spinors and trivially on four-vectors.

Every one of these objects is a twistor-theory object, and this is the honest common ground. In particular, the twistor module is

$$
T = S\oplus\bar{S} = \left(\tfrac12,0\right)\oplus\left(0,\tfrac12\right) = \Delta,
$$

which is **exactly the Dirac spinor module of that article**. A twistor is a Dirac spinor on which the conformal group, not merely the Lorentz group, acts; the extra structure distinguishing a twistor from a Dirac spinor is the Hermitian form $h$ of signature $(2,2)$, which encodes the conformal metric.

The two programmes therefore start from the same representation-theoretic fact, and both inherit from it the same kinematics of the double cover: the Lorentz group acts projectively on null directions, the spinor is two-valued, and a rotation by $2\pi$ is $-e_0$ on a spinor but $e_0$ on a four-vector. Whatever the differences in aim, the spinor module is not a point of contrast but a point of contact.

## Three Module Structures on $\mathbb{C}^4$

Because $\mathbb{B}\cong M_2(\mathbb{C})$ and $T\cong\mathbb{C}^4$ are both four-dimensional over $\mathbb{C}$, it is tempting to identify them, and to say that twistor space "is" the biquaternion algebra $(\mathbb{P}(\mathbb{B})\cong \mathbb{PT})$ as projective spaces. The identification is misleading, and it is worth separating the three distinct $SL(2,\mathbb{C})$-module structures that live on a four-complex-dimensional space in this neighbourhood.

| Space | Action of $SL(2,\mathbb{C})$ | Isomorphism class |
|---|---|---|
| $\mathbb{B}$ | left multiplication, $\tilde{Q}\mapsto\tilde{\Lambda}\tilde{Q}$ | $S\oplus S = (\tfrac12,0)\oplus(\tfrac12,0)$ |
| $\mathbb{B}$ | conjugation, $\tilde{Q}\mapsto\tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{*}$ | $S\otimes\bar{S} = (\tfrac12,\tfrac12)$ |
| $T$ | fundamental representation of $SU(2,2)$, restricted | $S\oplus\bar{S} = (\tfrac12,0)\oplus(0,\tfrac12) = \Delta$ |

The first line is the statement that the algebra is a module over itself; the second is the vector representation carried by the material sector $\mathbb{M}_-$; the third is the twistor (Dirac) module. All three are four-complex-dimensional, and they are pairwise non-isomorphic: $S\otimes\bar{S}$ is irreducible of dimension four, while the other two are reducible and their simple summands have different multiplicities or different chiralities. **Dimension alone does not identify twistor space with the algebra, and no $SL(2,\mathbb{C})$-equivariant isomorphism does.**

The concrete form of the third line is worth recording, because it is the precise sense in which the twistor module is the Dirac module written with the conformal action. If $\tilde{\Lambda}\in SL(2,\mathbb{C})$ has image $A=\mathsf{M}_2(\tilde{\Lambda})$, then on $Z=(\omega,\pi)$ the Lorentz action is

$$
\omega \longmapsto A\,\omega, \qquad \pi \longmapsto (A^\dagger)^{-1}\,\pi.
$$

The second factor is the conjugate defining representation in disguise: with $\epsilon$ the invariant form of the spinor-module article, $(A^\dagger)^{-1} = \epsilon\,\bar{A}\,\epsilon^{-1}$. Under $SU(2,2)$ this block-diagonal action is completed by the off-diagonal generators — translations and special conformal transformations — that mix $\omega$ and $\pi$ and thereby move the point $x$; the Lorentz group is the part that preserves the metric.

A related caution concerns the symbol $i$. In the framework, $i$ is the **scalar imaginary** of $\mathbb{B}$, and its appearance in the time coordinate $ict$ is what makes the signature Lorentzian. In the incidence relation $\omega = ix\pi$, $i$ is the complex unit of twistor space, and its role is to make the line $L_x$ a real line when $x$ is Hermitian. The two complex structures are not the same structure, and the projective coincidence $\mathbb{P}(\mathbb{B})\cong\mathbb{PT}$ does not equate them.

## The Null Cone: A Genuine Agreement

The two programmes do agree on one substantive geometric fact: the null cone is the fundamental object, and it is controlled by the two-component spinor.

On the biquaternion side, the biquaternion norm $N(\tilde{Q}) = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2 = \det\mathsf{M}_2(\tilde{Q})$ vanishes exactly on the zero divisors, and the nonzero null elements are exactly the rank-one matrices. Projectivising, the null cone of $\mathbb{B}$ is a cone over the **Segre quadric** $\mathbb{P}^1\times\mathbb{P}^1 \subset \mathbb{PT}$, and its two rulings are the two families of chiral spinor lines — the primed and unprimed spinor lines. This is the content of the mathematics articles *The Null Quadric and Its Projective Geometry* and *The Topology of the Zero-Divisor Cone*, and it is not repeated here.

On the twistor side, the same projective space and the same spinor lines appear, now carrying the metric. The incidence relation makes the null separation of two points a statement about the intersection of two lines: the null cone at $x$ is swept out by the points $y$ whose lines $L_y$ meet $L_x$, and this is exactly the condition $\det(x-y)=0$. The Klein correspondence is the dictionary between the two descriptions of the same projective geometry.

Two qualifications keep the agreement honest. First, the quadrics are different objects. The biquaternion norm $N$ is a **general plain bilinear** (symmetric) form on $\mathbb{B}\cong\mathbb{C}^4$, and its null cone is a complex quadric; the twistor form $h$ is **Hermitian** of signature $(2,2)$, and its null set is the real cone that defines the conformal structure. They agree in being governed by the spinor and its two chiralities, not in being the same equation. Second, the agreement is at the level of the algebra of spinors and null directions, which is standard; neither programme owns it.

**Reading (the celestial sphere and the helicity winding).** The null directions of the light cone projectivise to the **celestial two-sphere** $S^2=\mathbb{C}\mathbb{P}^1$, and the two chiral spinor lines of the Segre quadric are its two spinor parametrisations; a massless field lives on the null cone and its direction datum is a point of that sphere, with the helicity the weight of the little-group $U(1)$ phase at the point. The phase over the real sphere is a circle bundle — the unit spinors over $S^2$, the Hopf fibration $S^1\to S^3\to S^2$ — and the helicity is read as the **winding** of that fibre over the sphere; over the complexified cone the parallel object is the **link**, an $S^1$-bundle over the pair of chiral spheres, $S^1\to L\to S^2\times S^2$. The object is developed in *The Celestial Sphere of the Null Cone: Null Directions, Chirality and the Phase*; the boundary here is that the algebra supplies the two spinor lines and the sphere of directions, while the bundle and the winding are the standard little-group structure and are not a new derivation of the helicities.

## Where the Aims Diverge

The differences are not algebraic errors on either side; they are differences in what the algebra is for.

**Group.** Twistor theory is conformally invariant, and its group is the fifteen-dimensional conformal group $SO(2,4)$, linearly realized on $T$ by $SU(2,2)$. The Lorentz group is its six-dimensional subgroup preserving the metric. The biquaternion framework, by contrast, is organised around the Lorentz group $SL(2,\mathbb{C})$ itself: its material sector carries the vector representation, its symmetry is Lorentz invariance, and conformal transformations are not part of its structure. (The companion article on the null quadric observes that $SO^+(1,3)\cong PSL_2(\mathbb{C})$ is "the conformal group of the projective null cone"; that is the conformal group of the celestial two-sphere, not of Minkowski space, and it is a different statement from the one used here.)

**Complexification.** In the framework the observable sector $\mathbb{M}_-$ is **real** — imaginary scalar part $ict$, real spatial part $x,y,z$ — and the complex structure is a physical object: it is the $ict$ convention, and in a medium the scale $c=1/\sqrt{\epsilon\mu}$ makes it **local**, varying from point to point. The complexification is in the time direction and is physical. In twistor theory spacetime is complexified globally to $\mathbb{C}^4$; real Minkowski space is a reality condition (a real slice) on that complex manifold, and the work is done by holomorphic and projective methods — sheaves, cohomology, deformations of complex structure. The two complexes are different in kind: one is a physical, local, metric-level structure; the other is a global complex structure used as a computational and conceptual engine.

**Field equations.** The framework writes wave equations in the algebra: the biquaternion Maxwell and Dirac equations, with mass terms, at a point of $\mathbb{M}_-$ or of the full $\mathbb{B}$. Twistor theory's native transform is the **massless** one: the Penrose transform represents helicity-$h$ massless fields by sheaf cohomology on twistor space, and the conformal invariance is essential to it. Massive fields require additional twistor machinery and are not the natural home of the method.

**Self-duality and operators.** Twistor theory's deepest result is the nonlinear graviton, which reduces half-flat Ricci-flat complex spacetimes to deformed twistor spaces; the framework's representation theory contains the decomposition of the field strength into self-dual $(1,0)$ and anti-self-dual $(0,1)$ parts, but the framework has no analogous curved-space construction. Conversely, the framework carries the **informational sector** $\mathbb{M}_+$ with its operator algebra and the trace formula $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H}) = 2\langle\tilde{P},\tilde{H}\rangle$, the biquaternion form of the Born rule. Twistor theory has no counterpart of this Hermitian operator algebra: its Hermitian form $h$ is a fixed conformal structure, not a space of states and observables. The two programmes are asymmetric in what they provide: twistors give conformal and null geometry and a transform; the framework gives a real material sector and an operator sector on the same algebra.

## Two Further Senses of the Word: Algebraic and Congruence Twistors

The word "twistor" also occurs in the framework's literature in two further senses: once with a meaning unrelated to the one above, and once with the classical meaning in a complexified setting. The two are taken in turn, because the first is the more easily confused with Penrose's. In a four-part series on the **differential algebra of biquaternions**, L. A. Alexeyeva studies the biquaternionic wave equation

$$
\nabla^\pm B + F \circ B = G(\tau, \mathbf{x}),
\qquad
\nabla^\pm = \partial_\tau \pm i\,\nabla ,
$$

where $\tau$ is time measured in units of length, $\nabla$ the spatial gradient, $\circ$ the biquaternion product, $G$ a given source, and $F = f + \mathbf{F}$ a **constant** biquaternion — the **structural coefficient**, with scalar part $f$ and vector part $\mathbf{F}$ [Alexeyeva 2014]. She calls it a **biwave** equation, because it is of hyperbolic type and each component of its solution solves a wave equation. The naming is justified by two specialisations the corpus already knows: $F = 0$ reproduces the biquaternionic Maxwell system and $F = f$, a complex scalar, the biquaternionic Dirac system. The fourth paper takes the coefficient **vector-valued**, and its remark is that the equation, written in matrix (tensor) form, then belongs to the class of Yang–Mills equations. That comparison belongs to *The Yang–Mills Equation in Biquaternionic Form*; what matters here is the object the paper builds.

**Twistors, in this second sense, are the solutions of the homogeneous biwave equation.** Split the coefficient into real vectors,

$$
\mathbf{F} = -E - iH, \qquad E, H \in \mathbb{R}^3 ,
$$

and take the upper sign of the equation, $\nabla^+ B + \mathbf{F}\circ B = 0$. Its elementary solutions are labelled by a wave vector $\boldsymbol{\xi}$ and built from the plane harmonic wave

$$
\psi^{\pm}_{\boldsymbol{\xi}}(\tau, \mathbf{x}) = \exp\!\left(\pm i\tau\varpi - i(\mathbf{x}, \boldsymbol{\xi})\right),
\qquad
\varpi = \sqrt{|\boldsymbol{\xi} - E|^2 - |H|^2},
$$

which is a solution of the same homogeneous scalar equation whenever $|\boldsymbol{\xi} - E| > |H|$. Applying the complementary operator to it gives the **elementary $\boldsymbol{\xi}$-twistor**

$$
\Psi^{\pm}_{\boldsymbol{\xi}} = \frac{1}{\sqrt{2}\,|\boldsymbol{\xi} - E|}\left(\pm i\varpi - (\boldsymbol{\xi} - E) + iH\right)\psi^{\pm}_{\boldsymbol{\xi}},
\qquad \boldsymbol{\xi} \neq E ,
$$

a complex-vector-valued field on Minkowski space. Writing $\|\tilde{Q}\|^2 = \sum_\mu |Q_\mu|^2$ for the Euclidean norm of a biquaternion, so that its **Euclidean difference** is $|Q_0|^2 - \sum_k |Q_k|^2$, the elementary twistor is characterised by the two invariants

$$
\|\Psi^{\pm}_{\boldsymbol{\xi}}\| = 1 ,
\qquad
\langle \Psi^{\pm}_{\boldsymbol{\xi}}\rangle = i\,\frac{|H|}{|\boldsymbol{\xi} - E|} ,
$$

in which the second is the source's **pseudonorm** and not the Euclidean difference: with the amplitude above, that difference is $-|H|^2/|\boldsymbol{\xi} - E|^2$, and the printed value is $i$ times the square root of its negative. The two agree only at $H = 0$. This is stated once here and used in the table below: its pseudonorm column carries the source's values in that convention, except the static entry, which is the Euclidean difference itself.

Its energy–momentum biquaternion $\Xi = \Psi \circ \Psi^{*} = W + iP$ has scalar part $1$ — unit energy density — and a purely imaginary vector part carrying the flux:

$$
\Xi = 1 + i\,\frac{\varpi\,\mathbf{e} - \mathbf{e} \times H}{|\boldsymbol{\xi} - E|},
\qquad
\mathbf{e} = \frac{\boldsymbol{\xi} - E}{|\boldsymbol{\xi} - E|} .
$$

With $\gamma$ the angle between $\mathbf{e}$ and $H$, its norm is $\sqrt{1 + c}$ and its pseudonorm $\sqrt{1 - c}$, where $c = (|\boldsymbol{\xi} - E|^2 - |H|^2\cos^2\gamma)/|\boldsymbol{\xi} - E|^2$; so at $\gamma = \pm\pi/2$ the energy–momentum biquaternion is null in the pseudonorm, $\langle \Xi \rangle = 0$, with $\|\Xi\| = \sqrt{2}$. This is the printed form of $\Xi$: the printed numerator is $[\mathbf{e}, H] \pm \varpi\mathbf{e}$, and the paper's bracket here is taken in the **reverse** order from the corpus's $[\mathbf{Q}, \mathbf{R}] = \mathbf{Q}\times\mathbf{R}$, so that in this formula $[\mathbf{e}, H] = H \times \mathbf{e} = -\mathbf{e}\times H$. Norm, pseudonorm and both invariants agree with a hundred random coefficients and wave vectors to better than $8\times 10^{-15}$. **The symbol $\Xi$ is overloaded in the source**: it denotes the biquaternion and, in the same formulas, its two invariants, so the source's "$\Xi = 1 + c$" and "$\Xi = 1 - c$" are the *squared* norm and the Euclidean difference of the biquaternion $\Xi = 1 + i(\varpi\mathbf{e} - \mathbf{e}\times H)/|\boldsymbol{\xi} - E|$ displayed just above; the corpus keeps the biquaternion for $\Xi$ and names the two invariants in words. The overload matters in exactly one place, the $H$-twistor below, where "$\Xi = 2$" is the squared norm and $\Xi$ itself is $1 - i\mathbf{e}_H$. (In this article $\Delta$ continues to denote the Dirac module $S\oplus\bar{S}$.)

**The cases of the same family.** The label $\boldsymbol{\xi}$ is unrestricted, and the character of the solution changes with $|\boldsymbol{\xi} - E|$:

- **$|\boldsymbol{\xi} - E| > |H|$:** $\varpi$ is real; the potentials are travelling plane waves of wave vector $\boldsymbol{\xi}$, wavelength $2\pi/|\boldsymbol{\xi}|$ and phase velocity $\varpi/|\boldsymbol{\xi}|$, and the twistors above are the elementary ones.
- **$|\boldsymbol{\xi} - E| < |H|$:** $\varpi$ is imaginary and the potential becomes $\alpha^{\pm}_{\boldsymbol{\xi}} = \exp(\pm\tau\sqrt{|H|^2 - |\boldsymbol{\xi} - E|^2} - i(\mathbf{x},\boldsymbol{\xi}))$ — a standing harmonic wave with exponentially growing or decaying amplitude. A field built from such potentials is a driven or dissipative field rather than a travelling one.
- **$|\boldsymbol{\xi} - E| = |H|$:** $\varpi = 0$; the two signs of the potential coincide and the amplitude is time-independent.
- **$\boldsymbol{\xi} = E$:** the potential degenerates to a phase and the twistor is the separate **$H$-twistor** $\Psi^{\pm}_{H} = \frac{\mp 1 + i\mathbf{e}_H}{\sqrt{2}}\exp(\mp\tau |H| - i(E,\mathbf{x}))$, of unit norm and vanishing pseudonorm. Its amplitude is $\mp\sqrt{2}$ times a rank-one projector: writing $\tilde{\Pi}_\pm(\hat{\mu}) = \tfrac12(e_0 \pm i\hat{\mu})$ for the corpus's Hermitian idempotents, the upper sign gives the amplitude $-\sqrt{2}\,\tilde{\Pi}_-(\mathbf{e}_H)$ and the lower $+\sqrt{2}\,\tilde{\Pi}_+(\mathbf{e}_H)$, the two projectors being complex conjugates of one another. This is the one member of the family whose amplitude is an **idempotent** — Hermitian, hence in the informational sector $\mathbb{M}_+$ — and it is null under the algebra's bilinear norm, $N(\Psi_H) = 0$. Its energy–momentum biquaternion follows: $\Xi = 1 - i\mathbf{e}_H = 2\tilde{\Pi}_-(\mathbf{e}_H)$, the same projector again, with squared norm $2$ — the source's printed "$\Xi = 2$", read as the squared norm — and vanishing Euclidean difference. The general twistor is not of this form: $N(\Psi_{\boldsymbol{\xi}}) = -\varpi^2/|\boldsymbol{\xi} - E|^2$ for the travelling family, so $\boldsymbol{\xi} = E$ is the only member that is a zero divisor and the only one whose amplitude is a pure state of the algebra. This is the counterpart, on the informational side, of the finding recorded in *Bispinor Fields and the Fundamental Solution of the Generalized Maxwell–Dirac Equation*, where the harmonic bispinor's amplitude is $i\tilde{\Pi}_-(\hat{\boldsymbol{\xi}})$ and lies in the material sector instead.

**Twistor fields.** The homogeneous solution is not exhausted by one $\boldsymbol{\xi}$. Convolution with arbitrary biquaternionic fields $C_j$ — regular or singular, provided the convolution exists — gives the polarised twistor field $B_{\boldsymbol{\xi}} = \Psi^{+}_{\boldsymbol{\xi}} * C_1 + \Psi^{-}_{\boldsymbol{\xi}} * C_2$, and integrating over the admissible $\boldsymbol{\xi}$ with an arbitrary integrable weight $\varphi$ gives the unpolarised field $B^0 = \sum \Psi_{\varphi} * C^0$ with $\Psi_{\varphi}(\tau,\mathbf{x}) = \int_{S_{\cap}} \varphi(\boldsymbol{\xi})\,\Psi_{\boldsymbol{\xi}}(\tau,\mathbf{x})\,dS_{\cap}(\boldsymbol{\xi})$. The twistor is thus a kernel, not a state.

**The space the solutions live in.** The source's solutions are *generalized* ones, and it names the space: they are constructed in the space of **tempered generalized functions**, the weights required to be integrable on the admissible surface, $\varphi \in L^1(S_{\cap})$, and the arbitrary fields $C_j$ required only to admit the convolution. The general theorem behind the construction is not the source's, and the corpus states it in *Distributions and Fundamental Solutions*: a constant-coefficient operator with a fundamental solution $E$ solves $Pu = f$ by $u = E * f$ for $f$ of compact support, and that solution is the unique one in $\mathcal{S}'$ **provided the homogeneous equation has no non-zero tempered solution**. It is the proviso that carries the physics here. The travelling twistors are bounded, hence tempered, so the homogeneous equation *does* have non-zero tempered solutions, the proviso fails, and no uniqueness follows: the source's solution $B = (\nabla^- - \mathbf{F})(\psi * G) + B^0$ is a family, free by exactly the twistor space built above. The arbitrary $B^0$ and the arbitrary weight $\varphi$ are the same freedom seen twice.

**The names the source uses.** The series states the same construction in a journal-published English paper, where the vector-coefficient equation is called the **generalized Dirac equation** — the generalization being from a complex-scalar coefficient to a vector one — and the family is introduced as **biwave equations of general type**. The corpus uses the second name, because it is the descriptive one, and records the first here so that a reader who arrives looking for a "generalized Dirac equation" finds this object rather than concluding the corpus lacks it. Nothing in the object changes with either name.

**The biwave equation in its own right.** The equation $\nabla^\pm B + F \circ B = G$ with a constant coefficient $F = f + \mathbf{F}$ is one equation whose specialisations are the biquaternionic Maxwell ($F = 0$) and Dirac ($F = f$) systems and whose vector-coefficient case the author places in the Yang–Mills class by its matrix form. Its solution theory — the operator composition, the fundamental solution, the characteristic surface by case, and the matrix-form claim with what it does and does not say — is in *The Yang–Mills Equation in Biquaternionic Form*, and the second-order operator it produces is in *The Klein–Gordon Equation in Biquaternionic Form*. This article owns the solutions.

**Stationary and static twistors.** Separating a harmonic time dependence, $B = B(\mathbf{x})e^{-i\omega\tau}$, replaces the mutual bigradients by $\nabla^{\pm}_{\omega} = \omega \pm \nabla$ and turns the biwave equation into an elliptic one for the complex amplitude. Its elementary solutions are the **$\omega$-twistors**, built on the potential $\psi^{\omega}(\mathbf{x}) = \exp(-i(\mathbf{x}, H + \mathbf{e}_E\sqrt{\omega^2 + |E|^2}))$ with $\mathbf{e}_E \perp E$ and unit modulus: a plane wave of wave vector $K_F = H + \mathbf{e}_E\sqrt{\omega^2 + |E|^2}$, wavelength $2\pi/|K_F|$ and phase velocity $\omega/|K_F|$, of unit norm and pseudonorm $i|E|/\sqrt{\omega^2 + |E|^2}$. Letting $\omega \to 0$ gives the **static twistors**. The source prints their elementary potential as the sinusoid $\psi^0(\mathbf{x}) = \exp(-i(\mathbf{x},E+H))$ of period $2\pi/|E+H|$, with elementary twistor $\Psi^{0+} = \frac{-1+i}{\sqrt{2}}\psi^0\,\mathbf{e}_E$ of unit norm and pseudonorm $-1$. That printed wave vector does not satisfy the source's own generating equation, and it is corrected below; it is the one entry of the table not carried as printed. The families are collected below, and every other entry was recomputed to machine precision.

| Family | Generating potential | Wave vector | Norm | Pseudonorm |
|---|---|---|---|---|
| non-stationary, $\|\boldsymbol{\xi}-E\| > \|H\|$ | $\exp(\pm i\tau\varpi - i(\mathbf{x},\boldsymbol{\xi}))$ | $\boldsymbol{\xi}$ | $1$ | $i\,\|H\|/\|\boldsymbol{\xi}-E\|$ |
| non-stationary, $\|\boldsymbol{\xi}-E\| < \|H\|$ | $\exp(\pm\tau\sqrt{\|H\|^2-\|\boldsymbol{\xi}-E\|^2} - i(\mathbf{x},\boldsymbol{\xi}))$ | $\boldsymbol{\xi}$ | $\|H\|/\|\boldsymbol{\xi}-E\|$ | $i$ |
| $H$-twistor, $\boldsymbol{\xi} = E$ | $\exp(\mp\tau\|H\| - i(E,\mathbf{x}))$ | $E$ | $1$ | $0$ |
| stationary, $\omega \neq 0$ | $\exp(-i(\mathbf{x},K_F))$ | $K_F = H + \mathbf{e}_E\sqrt{\omega^2+\|E\|^2}$ | $1$ | $i\,\|E\|/\sqrt{\omega^2+\|E\|^2}$ |
| static, $\omega = 0$ | $\exp(-i(\mathbf{x},\,H+\|E\|\,\mathbf{e})),\ \ \mathbf{e}\perp E,\ \|\mathbf{e}\|=1$ | $H+\|E\|\,\mathbf{e}$ | $1$ | $-1$ |

**A slip in the printed static entry.** At $\omega = 0$ the surface is $S^0 = \{\boldsymbol{\xi} : \|\boldsymbol{\xi}-H\| = \|E\|,\ (\boldsymbol{\xi}-H,E) = 0\}$ — a circle of radius $\|E\|$ centred at $H$ in the plane perpendicular to $E$ — so the elementary static potentials are $\exp(-i(\mathbf{x},\,H + \|E\|\,\mathbf{e}))$ with $\mathbf{e}$ a **unit vector perpendicular to $E$**, and each of them solves the generating equation exactly (recomputed to $3\times10^{-15}$ over random $E$, $H$ and $\omega$). The source's printed $\exp(-i(\mathbf{x},E+H))$ takes the direction along $E$ instead of perpendicular to it. It satisfies the sphere half of the condition — since $\boldsymbol{\xi}-H = E$ gives $\|\boldsymbol{\xi}-H\| = \|E\|$ — but it fails the plane half $(\boldsymbol{\xi}-H,E) = 0$, which for this $\boldsymbol{\xi}$ reads $\|E\|^2 = 0$. Substituted into the generating equation it leaves the residual $-2i\|E\|^2$ (verified to $10^{-15}$), so it is an elementary static potential only in the limit $E = 0$. That limit is not arbitrary: it is the purely imaginary coefficient $\mathbf{F} = iH$ that the source treats two paragraphs earlier, where it correctly gives $\psi^0 = a\exp(-i(\mathbf{x},H))$, and the two printed forms agree there. The family is the same circle in both readings; only the representative the source prints is wrong. The stationary entry above is unaffected and was verified as printed.

**The energy–momentum biquaternions of the two later families.** The paper computes $\Xi$ for the stationary and static twistors as it does for the travelling one, and the stationary case is clean. With the corpus's product and the corpus's bracket $[u,v] = u\times v$,

$$
\Xi_\omega = \Psi^{+}_\omega \circ (\Psi^{+}_\omega)^\dagger = 1 + i\,\frac{\omega\,\mathbf{e} + \mathbf{e}\times E}{\sqrt{\omega^2 + \|E\|^2}},
\qquad
\mathbf{e} = \mathbf{e}_E ,
$$

of unit scalar part, squared norm $2$ and vanishing Euclidean difference — $\|\Xi_\omega\| = \sqrt2$, $\langle\Xi_\omega\rangle = 0$, so $N(\Xi_\omega) = 0$ and the energy–momentum biquaternion is itself a zero divisor, as the $H$-twistor's is — and it was checked on four hundred random coefficients and directions to machine precision. The source prints the numerator as $\omega\mathbf{e} + [\mathbf{e}, E]$ with the invariants $\sqrt2$ and $0$, so this is its printed form under the corpus's bracket. **The three printed energy–momentum biquaternions do not share one bracket**, and the collision is worth recording because each is correct in a different one. The travelling formula's printed $[\mathbf{e}, H]$ is the reverse of the corpus's bracket, $[\mathbf{e}, H] = H\times\mathbf{e} = -\mathbf{e}\times H$, as the note above records; the stationary formula's printed $[\mathbf{e}, E]$ is the corpus's bracket itself, $[\mathbf{e}, E] = \mathbf{e}\times E$, as here. Read in the other's convention each one flips the sign of its cross term: the stationary numerator matches $\mathbf{e}\times E$ in $400/400$ random cases and $E\times\mathbf{e}$ in none, and the travelling numerator matches $-(\mathbf{e}\times H)$ in $219/219$ and $+\mathbf{e}\times H$ in none. Nothing but the bracket distinguishes them, so a reader checking the two against one another must pin it first. The static entry is a different matter: the source prints it as $\Xi_0 = 1 + i[\mathbf{e}, \mathbf{e}_E]$ with $\|\Xi_0\| = \sqrt2$ and vanishing pseudonorm, but the amplitude it prints, $\Psi^{0+} = \frac{-1+i}{\sqrt2}\psi^0\,\mathbf{e}_E$, is a **pure vector** — a complex scalar times a real unit vector, with no scalar part — and the product of a pure vector with its own ${}^{*}$-conjugate is the real scalar $\|v\|^2$ with vanishing vector part. Computed directly, that printed amplitude gives $\Xi_0 = 1$ exactly in $400/400$ cases, not the stated $1 + i[\mathbf{e}, \mathbf{e}_E]$; the stated invariants $\sqrt2$ and $0$ do hold of $1 + i[\mathbf{e}, \mathbf{e}_E]$, whose vector part has unit modulus, but not of the product the printed amplitude forms. The static energy–momentum is therefore a further symptom of the static section, beside the printed potential, and the corpus carries $\Xi_\omega$ above and not a derived $\Xi_0$.

**Generating scalar potentials.** The structural finding of the paper is that the twistors are not constructed by trial: they possess **generating scalar potentials**. The elementary potentials above solve a single scalar equation — in the non-stationary case $(\Box_A + (\mathbf{F},\mathbf{F}) + 2i(\mathbf{F},\nabla))\psi = 0$ and in the stationary case

$$
\left(\Delta \pm 2(\mathbf{F},\nabla) + \omega^2 + (\mathbf{F},\mathbf{F})\right)\psi = 0 ,
$$

with $\Box_A = \partial^2_\tau - \Delta$, the operator that *The Klein–Gordon Equation in Biquaternionic Form* treats and relates to this series' $\Box$ — and the twistor is recovered from its potential by one first-order operator. The solutions of that equation are represented as **surface integrals** $\psi^0(\mathbf{x}) = \int_{S^{\omega}} \varphi(\boldsymbol{\xi})\exp(-i(\mathbf{x},\boldsymbol{\xi}))\,dS^{\omega}(\boldsymbol{\xi})$ over the surface

$$
S^{\omega} = \left\{\boldsymbol{\xi} : (\boldsymbol{\xi} + i\mathbf{F}, \boldsymbol{\xi} + i\mathbf{F}) = \omega^2\right\},
$$

with $\varphi$ an arbitrary locally integrable weight. Writing $\mathbf{F} = A + iB$ for its real and imaginary parts, the surface is the circle of radius $\sqrt{\omega^2 + \|A\|^2}$ centred at $B$ in the plane through $B$ perpendicular to $A$; when $A = 0$ it is the sphere of radius $|\omega|$ centred at $B$, and when $B = 0$ the centre is the origin. Because the weight $\varphi$ is free, the solution space is a large family rather than a finite-dimensional module, and choosing $\varphi$ to match the integral representations of the Bessel functions and the spherical harmonics reduces it to a **countable** family of still more elementary twistors — the algebraic analogue of a partial-wave expansion, carried out with the special functions of *Biquaternion Higher Special Functions*.

**The distinction that must be kept.** Nothing in this section is a Penrose twistor. Alexeyeva's twistor is a solution of a wave equation on Minkowski space, with values in the biquaternion algebra or its complex-vector part; it is not a point of $T = S\oplus\bar{S}$, it carries no incidence relation, no conformal action and no transform, and its characteristic structure is the light cone of a partial differential operator, not the twistor quadric. The paper's own description of the series confirms this: it treats biquaternionic wave equations equivalent to Maxwell, Dirac and Yang–Mills-type systems, all of them field equations on spacetime. The shared word is a coincidence of vocabulary, and the corpus records it as such.

**A third usage, and there the word is the classical one.** A neighbouring biquaternionic programme attaches the word to an object that *is* a Penrose twistor, on complexified Minkowski space. In V. V. Kassandrov's *algebrodynamics* the generalized Cauchy–Riemann conditions of the biquaternion field force each matrix component of the fundamental field to satisfy the **complex eikonal equation**, and a solution of the complex eikonal equation generates a congruence of complex null rays, one family of which is shear-free. For the congruence generated by a "virtual" point charge moving along a world line $Z = Z(\kappa)$, $\kappa \in \mathbb{C}$, the projective **twistor field** $\{\xi,\tau\}$ of the congruence at a point $Z$ is fixed by the condition

$$
\bigl(Z - \hat{Z}(\kappa)\bigr)\xi = 0
\qquad\Longleftrightarrow\qquad
\tau = Z\xi = \hat{Z}(\kappa)\xi ,
$$

which is the Penrose incidence relation written over complexified rather than real Minkowski space: the field is constant along each complex null ray, and the world line of the charge is the focal line — the caustic — of the congruence. The charge that "affects" the point $Z$ is selected by the **complex null cone** condition $\det\lvert Z-\hat{Z}(\kappa)\rvert=0$ — the vanishing of the biquaternion norm of a difference, that is, the complexified form of the zero-divisor cone of the mathematics article *The Topology of the Zero-Divisor Cone* — and over $\mathbb{C}$ that equation has generically many roots $\kappa_n$, so a point is reached by an *ensemble* of source positions. Everything the programme builds on that multiplicity — the correlated particle-like singularities it calls *duplicons*, the induced interval of the diagonal route and its invariant phase, the "observable" space-time — is recorded, once, in *The Algebrodynamical Programme: Nonlinear Cauchy–Riemann and Self-Quantized Charge*, which owns the programme; it is not restated here. What belongs to this article is the sense of the word.

Three usages of one word, then, and only two of them are the same object. Penrose's twistor and Kassandrov's twistor field are the classical incidence data, the second deployed for a congruence over complexified Minkowski space rather than for the conformal structure of real Minkowski space; Alexeyeva's twistor is a solution of a biquaternionic wave equation and is unrelated to both. The corpus records the incidence relation and does not adopt the programme's physical reading, which is kept in the article that owns it. The group-theoretic side of the same programme — the algebra automorphisms $SO(3,\mathbb{C}) \cong PGL(2,\mathbb{C})$ as the proper Lorentz group acting on bilinearly induced real coordinates — is treated in *The Lorentz Group as Biquaternion Norm Automorphisms*.

## What Is Not Claimed

It is worth stating the negative claims as plainly as the positive ones.

1. **Twistor theory is not biquaternions.** Twistor space and the biquaternion algebra are both four-complex-dimensional, and their projectivisations are both $\mathbb{CP}^3$, but as $SL(2,\mathbb{C})$-modules they are distinct ($\Delta$ versus $(\tfrac12,\tfrac12)$), and their complex structures play different roles. No equivariant identification is claimed or available.
2. **This framework does not reproduce twistor results.** Nothing here derives the Penrose transform, the nonlinear graviton, or the Ward correspondence, and no attempt is made to.
3. **The agreement is not a coincidence to be explained.** The Weyl spinor and $SL(2,\mathbb{C})$ are common to all four-dimensional relativistic formalisms; that two of them use the same module is not evidence for either.
4. **The name "twistor" is used in three senses, of which two are the classical object.** Penrose's twistor is a point of the conformal-module $T = S\oplus\bar{S}$; Alexeyeva's twistor is a solution of a biquaternionic wave equation on spacetime, tied to the first sense by vocabulary alone; Kassandrov's twistor field is a Penrose twistor — the incidence data of a complex null line — but deployed for the congruence generated by a complex world line rather than for the conformal structure of real Minkowski space, and accompanied by caustic-multiplicity vocabulary ("duplicons") that the corpus does not adopt. The first and the third sense are the same object in different settings; the second is a homonym. None is a special case of another in a way that yields a dictionary, and the corpus keeps them apart by context.
5. **Neither programme is a limit of the other.** The framework is not the real slice of twistor theory, and twistor theory is not the conformal completion of the framework.

## Summary

Twistor theory and the biquaternion framework share a precise foundation: the two-component Weyl spinor module $S=\mathbb{C}^2$ and the covering $SL(2,\mathbb{C})\to SO^+(1,3)$. Twistor space is $T = S\oplus\bar{S}$, which is exactly the Dirac spinor module $\Delta$ of the spinor-module article, equipped with a Hermitian form $h$ of signature $(2,2)$ whose isometry group $SU(2,2)$ is the double cover of the conformal group $SO(2,4)$. A point of complexified Minkowski space corresponds to a line in $\mathbb{PT}$ by the incidence relation $\omega = ix\pi$, and null separation becomes the intersection of lines — the Klein correspondence. Twistor theory uses this to organise conformal invariance, null geometry, massless fields (the Penrose transform), and half-flat solutions (the nonlinear graviton).

The biquaternion algebra $\mathbb{B}\cong M_2(\mathbb{C})$ carries three distinct four-complex-dimensional module structures — $S\oplus S$ under left multiplication, $S\otimes\bar{S}=(\tfrac12,\tfrac12)$ under conjugation, and (for $T$) $S\oplus\bar{S}$ — and it is the same spinor module, not the same space, that the two programmes share. The material sector $\mathbb{M}_-$ and the informational sector $\mathbb{M}_+$, with the trace formula $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H}) = 2\langle\tilde{P},\tilde{H}\rangle$, have no twistor counterparts, while the conformal group and the twistor transform have no counterpart here. The two programmes agree on the spinor and the null cone and diverge on what they build from them; neither contains the other.

The word "twistor" carries a second, independent sense in the framework's literature: the algebraic twistors of Alexeyeva, which are solutions of the homogeneous biquaternionic biwave equation $\nabla^+B+\mathbf{F}\circ B=0$ with a constant complex vector structural coefficient $\mathbf{F}=-E-iH$. They come in non-stationary, $H$-, stationary and static families, are unit-norm elements of the algebra with pseudonorm $i|H|/|\boldsymbol{\xi}-E|$ in the generic non-stationary case (the source's convention, defined where the families are described), and possess generating scalar potentials from which they are recovered by one first-order operator. One member is distinguished algebraically: the $H$-twistor's amplitude is a rank-one Hermitian idempotent of the algebra, $-\sqrt{2}\,\tilde{\Pi}_-(\mathbf{e}_H)$, making it the only one of the four families whose amplitude is a pure state — the informational-sector counterpart of the harmonic bispinor's amplitude $i\tilde{\Pi}_-(\hat{\boldsymbol{\xi}})$ in *Bispinor Fields and the Fundamental Solution of the Generalized Maxwell–Dirac Equation*. They are field configurations on spacetime, not points of a conformal module, and the sense must not be conflated with the classical one.

The word carries a third sense, and that one is the classical object. In Kassandrov's algebrodynamics the complex eikonal equation of the generalized Cauchy–Riemann conditions generates shear-free congruences of complex null rays, and the **twistor field** $\{\xi,\tau\}$ of the congruence generated by a point charge on a complex world line $Z(\kappa)$ is fixed by $(Z-\hat{Z}(\kappa))\xi=0$, $\tau=Z\xi$ — the Penrose incidence relation over complexified Minkowski space, with the charge's world line as the caustic. The **complex null cone** equation $\det|Z-\hat{Z}(\kappa)|=0$ fixes $\kappa$; it is the complexified zero-divisor cone, and over $\mathbb{C}$ it has many roots. So of the three senses, the first and the third are the same object — the incidence data of a complex null line — used in different settings, and only the second is a homonym. What the programme builds on the multiplicity of the roots belongs to the article that owns the programme, *The Algebrodynamical Programme: Nonlinear Cauchy–Riemann and Self-Quantized Charge*. The group-theoretic side of the third sense, in which the algebra automorphisms $SO(3,\mathbb{C})\cong PGL(2,\mathbb{C})$ act as the proper Lorentz group on bilinearly induced real coordinates, is treated in *The Lorentz Group as Biquaternion Norm Automorphisms*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ | Matrix realization; $\mathsf{M}_2(e_0)=I_2$, $\mathsf{M}_2(e_k)=-i\sigma_k$ (read list) |
| $\mathbb{M}_-$ | Anti-Hermitian subspace (material sector), fixed points of $\flat$ |
| $\mathbb{M}_+$ | Hermitian subspace (informational sector), fixed points of ${}^{*}$ |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace, fixed points of complex conjugation |
| $\mathbb{C}_{\mathbb{B}}$ | Complex subspace, fixed points of quaternion conjugation |
| $[\mathbf{Q}, \mathbf{R}]=\mathbf{Q}\times\mathbf{R}$ | Complex bilinear cross-product bracket of vector parts (corpus convention; the source's printed $[\cdot,\cdot]$ reverses it in its travelling formula) |
| $N(\tilde{Q}) = \langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\tilde{Q}\tilde{Q}^{\natural}=\sum_\mu Q_\mu^2$ | Biquaternion norm (determinant) |
| $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H}) = 2\langle\tilde{P},\tilde{H}\rangle$ | Trace formula (Born rule) |
| $S=\mathbb{C}^2$ | Spinor module, unique simple module of $\mathbb{B}$ |
| $(\tfrac12,0)=S$, $(0,\tfrac12)=\bar{S}$ | Left- and right-handed Weyl modules |
| $\Delta=S\oplus\bar{S}$ | Dirac spinor module |
| $T=S\oplus\bar{S}$ | Twistor space, $\cong\mathbb{C}^4$ |
| $Z=(\omega^A,\pi_{A'})$ | Twistor: unprimed and primed Weyl spinors |
| $\mathbb{PT}=\mathbb{CP}^3$ | Projective twistor space |
| $h(Z,Z')=\omega^{*}\pi'+\pi^\dagger\omega'$ | Hermitian form of signature $(2,2)$ on $T$ |
| $SU(2,2)$ | Double cover of the conformal group $SO(2,4)$ |
| $x^{AA'}$ | $2\times2$ matrix of a point of complexified Minkowski space |
| $\omega^A=ix^{AA'}\pi_{A'}$ | Twistor incidence relation |
| $L_x\subset\mathbb{PT}$ | Twistor line of the point $x$ |
| $\mathrm{Gr}(2,4)$ | Grassmannian of lines in $\mathbb{CP}^3$ (Klein correspondence) |
| $\mathbf{F}=-E-iH$ | Constant complex-vector structural coefficient of the biwave equation (Alexeyeva); $E,H$ real vectors |
| $\nabla^{\pm}=\partial_\tau\pm i\nabla$ | Mutual bigradients of the biwave equation; $\Box_A=\partial_\tau^2-\Delta$ is minus this series' $\Box$ |
| $\psi^{\pm}_{\boldsymbol{\xi}},\ \Psi^{\pm}_{\boldsymbol{\xi}}$ | Elementary $\boldsymbol{\xi}$-twistor's generating scalar potential and the twistor itself |
| $\Xi=\Psi\circ\Psi^{*}=W+iP$ | Energy–momentum biquaternion of a twistor |
| $\lVert\tilde{Q}\rVert^2$ | Euclidean norm $\sum_\mu \lvert Q_\mu\rvert^2$; the Euclidean difference $\lvert Q_0\rvert^2 - \sum_k \lvert Q_k\rvert^2$; the source's pseudonorm is $i\sqrt{\sum_k \lvert Q_k\rvert^2 - \lvert Q_0\rvert^2}$ |
| $\tilde{\Pi}_\pm(\hat{\mu})=\tfrac12(e_0\pm i\hat{\mu})$ | Rank-one Hermitian idempotents; the $H$-twistor's amplitude is a real multiple of one |
| $Z(\kappa)$, $\kappa\in\mathbb{C}$ | World line of the "virtual" charge generating a shear-free null congruence (Kassandrov) |
| $\{\xi,\tau\}$, $(Z-\hat{Z}(\kappa))\xi=0$, $\tau=Z\xi$ | Twistor field of the congruence; the Penrose incidence relation over complexified Minkowski space |
| $\langle\tilde{P},\tilde{Q}\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{P}\tilde{Q})$ |

## Further Reading

- Roger Penrose, "Twistor algebra," *Journal of Mathematical Physics* **8** (1967) 345–366, for the original construction of twistor space and its algebra.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1: *Two-Spinor Calculus and Relativistic Fields* (Cambridge, 1984), for the two-component spinor calculus and the Weyl spinors.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 2: *Spinor and Twistor Methods in Space-Time Geometry* (Cambridge, 1986), for the twistor correspondence, the conformal group, and the geometry of null lines.
- Roger Penrose, "Solutions of the zero-rest-mass equations," *Journal of Mathematical Physics* **10** (1969) 38–39, for the Penrose transform.
- Roger Penrose, "Nonlinear gravitons and curved twistor theory," *General Relativity and Gravitation* **7** (1976) 31–52, for the half-flat construction.
- Roger Penrose and Malcolm A. H. MacCallum, "Twistor theory: an approach to the quantisation of fields and space-time," *Physics Reports* **6** (1973) 241–315, for the programme as a whole.
- S. A. Huggett and K. P. Tod, *An Introduction to Twistor Theory* (Cambridge, 1985), for a textbook treatment of the Penrose transform and the sheaf-cohomological formulation.
- R. S. Ward, "On self-dual gauge fields," *Physics Letters A* **61** (1977) 81–82, for the Ward correspondence.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the spinor modules and the double cover of the Lorentz group.
- L. A. Alexeyeva, "Differential algebra of biquaternions. 4. Twistors and twistor fields," arXiv:1406.5347 [math-ph] (2014), *Mathematical Journal* **13** (2013), for the algebraic twistors of a biquaternionic biwave equation, their invariants, their generating scalar potentials, and the energy–momentum biquaternions of the travelling, stationary and static families, whose bracket inconsistency is recorded above. The stationary kernel of the same paper is in *The Yang–Mills Equation in Biquaternionic Form*.
- L. A. Alexeyeva, "Generalized Dirac equation with vector structural coefficient and its generalized solutions in biquaternions algebra," *Journal of Mathematics and System Science* **5** (2015) 309–314 (doi:10.17265/2159-5291/2015.08.001), for the journal-published English statement of the same construction: the space of tempered generalized functions in which its solutions are built, the case analysis of the structural coefficient, the standing twistors, and the source's own names for the equation and for the family.
- V. V. Kassandrov, "Algebrodynamics in Complex Space-Time and the Complex-Quaternionic Origin of Minkowski Geometry", arXiv:gr-qc/0602088 (2006), for the shear-free null congruences generated by the complex eikonal equation, the twistor field of the congruence and its incidence relation, the complex null cone equation, the ensemble of its roots (the "duplicons"), and the observable space-time that the programme builds from them. The group-theoretic side — the algebra automorphisms $SO(3,\mathbb{C})$ as the proper Lorentz group on bilinearly induced real coordinates — is in *The Lorentz Group as Biquaternion Norm Automorphisms*.
