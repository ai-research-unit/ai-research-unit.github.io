# __Charge Conjugation and the Division Ring: Charged, Neutral and Truly Neutral Particles in Biquaternionic Form__

## Introduction

Charge conjugation is the discrete operation that exchanges a particle with its antiparticle. In the companion article *The CPT Theorem in Biquaternionic Form* it is built explicitly on the spinor module, $C[\psi]=-L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\psi^{*}$, and its internal factor is found to be an **odd** Clifford element with no representative in the biquaternion algebra. The present article asks the question that computation cannot answer: **when is $C$ trivial?** A symmetry that acts as the identity on a representation exchanges nothing there; the class of particles on which charge conjugation acts trivially has a name — the **truly neutral** particles — and a place in physics: the photon, the $Z$ boson, and the neutral mesons $\pi^0$, $\eta$, $\phi$.

The classification of the algebra literature answers the question with a single algebraic datum. Charge conjugation is the **pseudoautomorphism** of the complex Clifford algebra $\mathbb{C}\mathrm{l}_{n+m}$ induced by a real form $\mathrm{Cl}_{n,m}\subset\mathbb{C}\mathrm{l}_{n+m}$, $A^{\mathrm c}=\Pi\bar A\Pi^{-1}$, where $\bar A$ is the coefficient conjugation and $\Pi$ is a product of generators. The matrix $\Pi$ is fixed by the **division ring** $K$ of the real form: over a real division ring $K\cong\mathbb{R}$ it is proportional to the identity, so the map is trivial; over a quaternionic division ring $K\cong\mathbb{H}$ it is a genuine product of generators, so the map is the particle–antiparticle interchange; over the complex division ring $K\cong\mathbb{C}$ it relates a representation to its conjugate. The division ring, in other words, is what decides whether a particle can be its own antiparticle. (The literature writes the same map with $A^{*}$; here the star is reserved for the Hermitian conjugation of the corpus, and $\bar{\cdot}$ is the coefficient conjugation.)

The article is organised as follows. A first section states the pseudoautomorphism, its matrix and its action on spinors. A second states the division-ring trichotomy and computes $C^{2}$. A third reads the trichotomy as the three classes of particles. A fourth places the three classes in the biquaternion algebra. A fifth separates what the framework supplies from what it transcribes. The article closes with the open questions, a reference section on the frame cells and their identities, and the summary.

- Companion article *The CPT Theorem in Biquaternionic Form*, for the explicit $C[\psi]=-L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\psi^{*}$ and for the Clifford classification of the operations as the fundamental automorphisms and the charge-conjugation pseudoautomorphism.
- The mathematics articles *Division Rings*, *Central Simple Algebras and the Brauer Group* and *The Brauer Wall Group and the Eightfold Way*, for the division ring as an isomorphism invariant of a real or complex algebra.
- The mathematics article *List of Clifford Algebras and Spin Groups*, for the classification of $\mathrm{Cl}_{n,m}$ by $d=n-m\bmod 8$ that the trichotomy below uses.
- Companion article *Real Spinors and Reality Conditions on the Biquaternion Algebra with Hermitian Adjoint*, for reality conditions and real structures on the algebra.
- Companion articles *The Neutron in Biquaternionic Form* and *The Proton in Biquaternionic Form*, for the two charge states of one isospin doublet.

## The Pseudoautomorphism and Its Matrix

The discrete operations $P$, $T$, $PT$ are the three non-trivial **fundamental automorphisms** of a real Clifford algebra $\mathrm{Cl}_{n,m}$ — the grade involution, the reversion and their composite, the Clifford conjugation — and they act on each graded piece by a sign. Charge conjugation is not of this kind. On the complexification $\mathbb{C}\mathrm{l}_{n+m}$ it is the **pseudoautomorphism**

$$
\boxed{\;A\;\longmapsto\;A^{\mathrm c}=\Pi\,\bar A\,\Pi^{-1}\;},
$$

the coefficient conjugation of the algebra element followed by the inner automorphism by a matrix $\Pi$. Two features distinguish it from the fundamental automorphisms. First, it is **conjugate-linear**: it contains $\bar A$, and no complex-linear automorphism does. Second, it is not an automorphism in the category of $\mathbb{C}$-algebras, only a *semilinear* one: it preserves products, $(AB)^{\mathrm c}=A^{\mathrm c}B^{\mathrm c}$, but it reverses the scalar, $(\lambda A)^{\mathrm c}=\bar\lambda\,A^{\mathrm c}$. That reversal is what the prefix records, and it is why $C$ cannot be counted among the three untwisted operations.

Throughout, $L_a$ and $R_b$ are the left and right multiplications, $L_a\psi=a\psi$ and $R_b\psi=\psi b$, so that a cell is $L_aR_b\psi=a\psi b$. The four **generator cells**, one for each coordinate $t,x,y,z$, are:

$$
G_0=iR_{\vec e_x}^{\mathrm{axf}},\quad
G_1=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad
G_2=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad
G_3=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}.
$$

The factor $i$ belongs to the cell, and products use $i^2=-1$: $(iR_{\vec e_x}^{\mathrm{axf}})^2=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$, while $(iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}})^2=-L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ because $\vec e_k^{2}=-1$.

The map is the algebra-level form of the module operation $C[\psi]=\eta_C\psi^{*}$. The algebra-level matrix is $\Pi$, and the module representative is the cell

$$
\eta_C=-L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},
$$

determined up to a phase. Because $\Pi$ is fixed only up to a nonzero scalar, the phase of $\eta_C$ is free, exactly as the CPT article's explicit verification found.

### The Action on Spinors

On spinors the pseudoautomorphism acts through the invariant antisymmetric matrix $\Pi$. Let $\xi$ be a two-component spinor of the fundamental representation of $\mathrm{Spin}^{+}(1,3)\cong\mathrm{SL}(2,\mathbb{C})$, and let $\bar\xi$ be its coefficient conjugate. The charge-conjugated spinor is:

$$
\xi^{\mathrm c}=\Pi\,\bar\xi,
\qquad\text{that is,}\qquad
\xi^{\mathrm c}_{\dot\alpha}=\sum_\alpha\Pi_{\dot\alpha\alpha}\bar\xi_\alpha .
$$

Conjugating twice:

$$
(\xi^{\mathrm c})^{\mathrm c}=\Pi\,\overline{\Pi\,\bar\xi}=\Pi\bar\Pi\,\xi,
\qquad\text{that is,}\qquad
(\xi^{\mathrm c})^{\mathrm c}_\alpha=\sum_\beta(\Pi\bar\Pi)_{\alpha\beta}\xi_\beta=\pm\,\xi_\alpha .
$$

The sign is that of $\Pi\bar\Pi$ — the product of $\Pi$ with its coefficient conjugate — so the relation between a particle and its antiparticle is controlled entirely by $\Pi$. This is the first appearance of the division ring: the allowed matrices $\Pi$ are not arbitrary, and which ones occur is fixed by the algebra's division ring.

The module form of the same operation is the cell $\eta_C=-L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$. Its defining property is the intertwining condition:

$$
\eta_C^{-1}G_\mu\,\eta_C=-G_\mu^{*},
$$

where $G_\mu^{*}$ is the module conjugate of the generator cell. In the chiral-basis realization of the CPT article the module conjugation is componentwise complex conjugation of the spinor components, and it gives

$$
G_0^{*}=G_0,\qquad G_1^{*}=G_1,\qquad G_2^{*}=-G_2,\qquad G_3^{*}=G_3 .
$$

In the cell frame the condition reads:

$$
\eta_C^{-1}G_0\eta_C=-G_0,\quad
\eta_C^{-1}G_1\eta_C=-G_1,\quad
\eta_C^{-1}G_2\eta_C=+G_2,\quad
\eta_C^{-1}G_3\eta_C=-G_3 .
$$

The plus sign on $G_2$ is not an exception: it is exactly what $-G_2^{*}=+G_2$ requires, since the module conjugation negates that generator. So $\eta_C$ anticommutes with the three generators that the module conjugation fixes and commutes with the one it negates. It is odd, and it anticommutes with the chirality cell $-iR_{\vec e_z}^{\mathrm{axf}}$. This is the precise form of the statement that charge conjugation flips chirality. The condition is also what makes the operation compatible with the free equation: if $\psi$ solves the free equation then $C[\psi]$ solves it as well, which is the CPT article's explicit verification.

The free equation has two lines, one for each chirality. In the notation of *The Dirac Equation in Biquaternionic Form*,

$$
\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L,
\qquad
\tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R,
$$

On the spinor module the same statement is the single pair equation $(\mathbb{D}-m)\psi=0$, with $\psi=(\psi_L,\psi_R)$. Charge conjugation meets the two readings alike: because $\eta_C$ anticommutes with the chirality cell, $C$ exchanges the two lines, and the intertwining condition is what keeps the pair a solution.

## The Division-Ring Trichotomy

The classification is a theorem of the Clifford-algebra literature and is transcribed here. Let $\mathbb{C}\mathrm{l}_{n+m}$ be the complex Clifford algebra of an $(n+m)$-dimensional non-degenerate complex quadratic form, and let $\mathrm{Cl}_{n,m}\subset\mathbb{C}\mathrm{l}_{n+m}$ be a real form, with $n$ positive and $m$ negative squares. Write $d=n-m\bmod 8$.

The **division ring** $K$ of the real form — the ring of scalars of its irreducible module — is fixed by $d$ alone:

| $d=n-m\bmod8$ | $0,2$ | $4,6$ | $3,7$ | $1$ | $5$ |
|---|---|---|---|---|---|
| $K$ | $\mathbb{R}$ | $\mathbb{H}$ | $\mathbb{C}$ | $\mathbb{R}\oplus\mathbb{R}$ | $\mathbb{H}\oplus\mathbb{H}$ |

The form of the charge-conjugation matrix follows $K$:

| division ring $K$ | $d$ | matrix $\Pi$ | map $C$ |
|---|---|---|---|
| $\mathbb{R}$ | $0,2$ | $\Pi\propto I$ | identity at the algebra level |
| $\mathbb{H}$ | $4,6$ | a product of generators, $\Pi\bar\Pi=\pm I$ | particle–antiparticle interchange |
| $\mathbb{C}$ | $3,7$ | a product of generators | conjugation to the conjugate representation |

For even $n+m$ the integer $d$ is even, so only $K\cong\mathbb{R}$ and $K\cong\mathbb{H}$ occur; the complex row needs odd $n+m$, and $\mathrm{Cl}_{3,0}\cong M_2(\mathbb{C})$ at $d=3$ is the standard example. The two sum rows belong to odd $n+m$ and behave on each summand as the corresponding simple case.

This is the first structural fact of the trichotomy: the three cases are not three real forms of one even algebra. Two of them are real forms of real and of quaternionic type, and the third is the complex module itself, taken before any real form is imposed on it.

### The Three Cases

**Real division ring.** $\Pi\propto I$. On the real form the coefficient conjugation $\bar A$ is the identity, so $A^{\mathrm c}=\Pi A\Pi^{-1}=A$: the operation is trivial at the algebra level, and every representation carried by the algebra is its own conjugate. The particles are their own antiparticles in the strongest sense — not a neutral particle equal to its conjugate, but a particle on which the conjugation exchanges nothing. A real representation may still carry the sign $-1$; for a boson that sign is the charge-conjugation parity, $-1$ for the photon and the $\phi$ and $+1$ for the $\pi^0$ and the $\eta$, and it does not make the antiparticle a distinct state.

**Quaternionic division ring.** $\Pi$ is a product of generators with $\Pi\bar\Pi=\pm I$. The coefficient conjugation is not the identity on the complexification, and the pseudoautomorphism acts inside the real representation, exchanging the particle with its antiparticle: the state is its own charge-conjugate only up to a distinct partner. This is the neutral case.

**Complex division ring.** $\Pi$ is a product of generators, and the map relates a representation to its conjugate. The two charge states $\pm1$ are the two members of the conjugate pair, and $C$ maps one to the other. No state of the pair is its own antiparticle. This is the charged case.

## The Meaning of $C^{2}$

The square of charge conjugation is the product $\Pi\bar\Pi$, and both signs occur in practice. The section therefore separates what the division ring fixes from what the representation fixes.

**What the division ring fixes.** Only the form of $\Pi$. A real division ring makes it a scalar, and the map is the identity, so $C^{2}=\mathrm{id}$ trivially; the sign $-1$ that the photon carries is then a phase on the state, not a property of the map. A quaternionic or a complex division ring makes it a product of generators, and the sign of $\Pi\bar\Pi$ is then left open.

**A single chiral half squares to $-1$.** The invariant matrix is $\Pi=\epsilon=i\sigma_2$, which is real. Hence $\bar\Pi=\Pi$ and

$$
\Pi\bar\Pi=\Pi^{2}=-I,
\qquad\text{so}\qquad
(\xi^{\mathrm c})^{\mathrm c}=-\xi .
$$

The transposed form of the same map, $\psi_c=\eta\,\bar\psi^{T}$, is the CPT article's second formula; its cell is $\eta=R_{\vec e_x}^{\mathrm{axf}}$, with $\eta^{2}=R_{\vec e_x^{2}}^{\mathrm{axf}}=-L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$, and the minus sign of $\Pi^{2}$ is carried by $\vec e_x^{2}=-1$. On a two-component spinor, charge conjugation is a map of order four, not an involution.

**The Dirac module squares to $+1$.** The biquaternion module carries both chiral halves, and there the internal cell satisfies $\eta_C^{2}=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$, the identity operator. The map on the module is therefore an involution, $C^{2}=\mathrm{id}$, and this is the standard statement $(\psi^{\mathrm c})^{\mathrm c}=\psi$ for a Dirac field.

The two computations are not in conflict. The sign $-1$ of a single chiral half is absorbed when the second half is present: the pair, not the half, is what the Dirac field carries. The corpus meets both signs in other places: the Euclidean charge conjugation of *The Spectral Triple of the Biquaternion Algebra* is a cell that squares to $-I_4$, and the real structure of *Bosonization in Biquaternionic Form* is an involution. The moral for the classification is that the sign of $\Pi\bar\Pi$ belongs to the representation and not to the division ring, and that neither sign changes the class of the particle.

## The Three Classes of Particles

The trichotomy of the previous section is the algebraic form of the three classes of charge states, labelled by the charge symbol $Ϙ$.

### The Dictionary

**Charged particles.** The field is valued in a **complex** module, $K\cong\mathbb{C}$; the pseudoautomorphism is non-trivial and maps the module to its conjugate. The charge states $Ϙ=\pm1$ are the module and its conjugate, and $C$ exchanges them, so $C$ maps the particle to a different state, its antiparticle. The electron, the proton and the charged mesons are of this class.

**Neutral particles.** The field is valued in a module over the **quaternionic** division ring, $K\cong\mathbb{H}$; the pseudoautomorphism is non-trivial, but it acts *within* the module and interchanges the particle with a distinct partner. The neutron is of this class, a state that is neutral ($Ϙ=0$) yet distinct from its conjugate. Whether the neutrino belongs here or to the truly neutral class is the Majorana question, open question 2 below.

**Truly neutral particles.** The field is valued in a **real** module, $K\cong\mathbb{R}$; the photon's four-vector is one of them. The pseudoautomorphism is trivial at the algebra level, so the particle and its antiparticle are the same state. The operation may still act as the sign $-1$ on that state — the photon and the $\phi$ both carry $C=-1$ — but the sign is a charge-conjugation parity, not a distinction between two states. The photon is the paradigm; the $\pi^{0}$, the $\eta$ and the $\phi$ — the neutral mesons in the class — are the hadronic examples. Following the companion article's notation, this charge state is written $\bar{0}$ to distinguish it from the neutral state $0$.

The criterion is the division ring of the module and not the reality type of the Lorentz spinor. The Dirac spinor of $\mathrm{Spin}^{+}(1,3)$ is quaternionic for the electron as much as for the neutron, so the spin representation alone does not separate the classes; what separates them is the scalars of the module, that is, the algebra the field is valued in.

The three classes are collected in one table:

| class | module | action of $C$ | examples |
|---|---|---|---|
| charged | complex, $K\cong\mathbb{C}$ | conjugation to the conjugate module; exchanges $Ϙ=\pm1$ | electron, proton, charged mesons |
| neutral | quaternionic, $K\cong\mathbb{H}$ | particle–antiparticle interchange within the module; $Ϙ=0$ | neutron |
| truly neutral | real, $K\cong\mathbb{R}$ | identity at the algebra level, possibly the sign $-1$; $Ϙ=\bar{0}$ | photon, $\pi^{0}$, $\eta$, $\phi$, $Z$ |

A note on the last row. The $Z$ is its own antiparticle, but it couples to vector and axial currents at once, so its interactions are not $C$-invariant and the sign it would carry is not an observable. The class assignment stands; the parity does not.

The three classes are exactly the split of the charge values $\{+1,-1,0,\bar{0}\}$ that the companion article *The Spin–Charge Hilbert Space and the SU(3) Supermultiplets in Biquaternionic Form* uses to organise the charge multiplets. The present article supplies the reason the split is threefold and not twofold: a particle can be neutral and still not truly neutral precisely when the division ring of its module is quaternionic rather than real.

## The Biquaternion Reading

The biquaternion algebra has two readings, and the trichotomy uses both. As a **complex** algebra it is $\mathbb{C}\mathrm{l}_{2}$, the complexification of the quaternionic real algebra $\mathrm{Cl}_{0,2}\cong\mathbb{H}$, and its real forms are $\mathrm{Cl}_{0,2}\cong\mathbb{H}$ and $\mathrm{Cl}_{2,0}\cong\mathrm{Cl}_{1,1}\cong M_2(\mathbb{R})$. As a **real** algebra it is $\mathbb{C}\otimes_\mathbb{R}\mathbb{H}\cong M_2(\mathbb{C})\cong\mathrm{Cl}_{3,0}$, the identification the corpus records in *The Number Systems as Clifford Algebras*, and there $d=3$, so the division ring is $\mathbb{C}$: the framework's own algebra is the charged case, by the table itself. 

### Choosing the Algebra

The three cases of the trichotomy are realised by choosing whether the field is valued in the complex algebra or in one of its two real forms:

- **Charged fields** are carried by the complex algebra $\mathbb{B}$ itself, or by a complex module built on it. Their charge conjugation is the conjugate-linear $\eta_C$-twisted complex conjugation, and it maps the field to the conjugate representation. This is the framework's default, and it is why the companion articles treat charged fermions and the charged gauge fields directly.
- **Neutral fields** are carried by the real form $\mathrm{Cl}_{0,2}\cong\mathbb{H}\subset\mathbb{B}$, the real-quaternion subspace $\mathbb{H}_{\mathbb{B}}$, which is a division ring. Its charge conjugation is the non-trivial particle–antiparticle interchange.
- **Truly neutral fields** are carried by a real form of real type, isomorphic to $\mathrm{Cl}_{2,0}\cong\mathrm{Cl}_{1,1}\cong M_2(\mathbb{R})$, which occurs in $\mathbb{B}$ as a real subalgebra. On it the charge conjugation is trivial at the algebra level, and the field is its own antiparticle; the sign $-1$ may remain as a parity.

The interpretation is not a derivation, and it does not add a new field content to the framework. Its value is that it locates the three charge classes in the *same* algebra: the complexification carries the charged case, and its real forms carry the two neutral cases. The photon article's finding that the free photon is a real, self-conjugate field is the case $K\cong\mathbb{R}$; the neutron article's finding that the neutron is neutral but distinguishable from the antineutron is the case $K\cong\mathbb{H}$.

## What the Framework Establishes, Transcribes, and Does Not

**Established, and recomputed.**

- The algebra-level pseudoautomorphism is $A^{\mathrm c}=\Pi\bar A\Pi^{-1}$; it is conjugate-linear on the complexification and is not one of the three fundamental automorphisms. On the module its representative is the odd cell $\eta_C=-L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$, and the intertwining condition is $\eta_C^{-1}G_\mu\eta_C=-G_\mu^{*}$, which reads $-,-,+,-$ for $\mu=0,1,2,3$. This is the algebra-level form of the CPT article's finding that $C$'s internal factor is odd.
- The twice-conjugated spinor is $(\xi^{\mathrm c})^{\mathrm c}=\Pi\bar\Pi\,\xi$. For the invariant matrix $\Pi=\epsilon=i\sigma_2$ the product is $-I$, so a chiral half squares to $-1$; the module cell satisfies $\eta_C^{2}=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$, so the Dirac module squares to the identity. Both signs are recomputed, and the pair of them is the statement that charge conjugation is a map of order four on a chiral half and an involution on the module.
- Over a real division ring $\Pi\propto I$ and the pseudoautomorphism is the identity at the algebra level; the corresponding particles are truly neutral. The three charge classes are the modules over $\mathbb{C}$, over $\mathbb{H}$ and over $\mathbb{R}$.

**Transcribed, not derived.**

- The classification theorem itself: that the form of $\Pi$ is governed by the division ring of the real form, and the Bott correspondence $d=n-m\bmod 8\to K$, with $\mathbb{R}$ at $0,2$, $\mathbb{H}$ at $4,6$ and $\mathbb{C}$ at $3,7$.
- The physical identifications of the three classes — electron and proton charged, neutron neutral, photon and $\pi^{0}$ and $\eta$ and $\phi$ truly neutral. These are the standard assignments of particle physics.
- The biquaternion realisation: that the framework's algebra is $\mathbb{C}\mathrm{l}_{2}$ as a complex algebra and $\mathrm{Cl}_{3,0}$ as a real one, and that it contains the real forms $\mathrm{Cl}_{2,0}$, $\mathrm{Cl}_{1,1}$ and $\mathrm{Cl}_{0,2}$, is the corpus's own Clifford-structure result; reading the three charge classes through them is the present article's organisation, not a theorem the algebra forces.

**Gap, left visible.**

- No derivation that a *given* physical particle's real form is the one assigned to it. The classification says which class each algebra's representations fall into; it does not, by itself, say that the neutron is quaternionic and the photon real. That identification is transcribed from the spin and charge assignments and is where a stronger framework would have to act.
- No $\mathbb{B}$-intrinsic form of the pseudoautomorphism, for the same reason the CPT article leaves $C$ external: $\Pi$ is a product of generators, and the generators needed for it include odd ones outside $\mathbb{B}$; in the module realization $\eta_C$ is odd. The division-ring classification locates $C$ among the intrinsic maps of $\mathbb{C}\mathrm{l}_{n+m}$; it does not bring $C$ inside $\mathbb{B}$.
- No treatment of the charge-conjugation phase for composite or mixed states, and no statement about $K^{0}$–$\bar{K}^{0}$ mixing, where the truly-neutral interpretation of a neutral meson requires the superposition language the framework does not yet carry.

## Open Questions

1. **Is the framework's own $\mathbb{B}$ the charged case?** The charged case is the complex module, so a field that uses the full complex structure of $\mathbb{B}$ sits in it by default. Is the neutrality of a field then always the statement that its real form is $\mathrm{Cl}_{0,2}$ or $\mathrm{Cl}_{2,0}$, and can that be read off an equation rather than assigned?

2. **Which real form does the mass term select?** The Dirac mass term is the linear chiral pair, and the Majorana question of the neutrino article is exactly the question of a real form. Does the anti-Hermitian map $\flat=-{}^{*}$ pick out the quaternionic real form $\mathrm{Cl}_{0,2}$, and is the neutrino's neutrality thus the $K\cong\mathbb{H}$ case?

3. **Neutral mesons and the truly neutral class.** $K^{0}$ has charge $0$ but is not truly neutral: $K^{0}\ne\bar{K}^{0}$, and the two mix. The classification must therefore place it in the quaternionic class. Does the corpus's assignment of the neutral pseudoscalars follow the same rule, and at which charge-conjugation phase?

4. **The sign of $C^{2}$ in higher-spin fields.** A chiral half has $\Pi\bar\Pi=-I$ and the Dirac module has $C^{2}=\mathrm{id}$; the corpus's higher-spin fields live in tensor powers and in the Rarita–Schwinger construction. Does the module sign stay $+1$ there, or does it change with the spin, as it does in some standard conventions?

5. **Truly neutral composites.** A truly neutral field is one on which $C$ acts without exchanging two states. Is the same true of a *composite* colour singlet, such as a quark–antiquark state in the framework's gauge-invariant sector, and does the division-ring criterion survive the composition?

## The Gamma Formulation

This section is the only place in the article where the gamma matrices appear. They are not a different algebra and no formula above needs them: they are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, and each gamma *is* one of the five frame cells, the factor $i$ included, so the dictionary below carries no extra phase.

With $L_a\psi=a\psi$ and $R_b\psi=\psi b$, the dictionary is:

$$
\gamma_0=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad
\gamma_1=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad
\gamma_2=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad
\gamma_3=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad
\gamma_5=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}.
$$

The same in the axis-free display:

$$
\gamma_0=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\quad
\gamma_1=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad
\gamma_2=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad
\gamma_3=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad
\gamma_5=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}.
$$

The first and the last collapse to one-sided multipliers, $\gamma_0=iR_{\vec e_x}^{\mathrm{pau}}$ and $\gamma_5=-iR_{\vec e_z}^{\mathrm{pau}}$, because $L_{e_t}^{\mathrm{pau}}$ is the identity. The charge-conjugation cell of the article is the same frame read in the spatial direction:

$$
\eta_C=-L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}=i\gamma_2,
$$

In the axis-free display:

$$
\eta_C=-L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}=i\gamma_2,
$$

and the chirality cell is:

$$
\Gamma=-iR_{\vec e_z}^{\mathrm{pau}}=\gamma_5.
$$

The same identities in the axis-free display:

$$
\Gamma=-iR_{\vec e_z}^{\mathrm{axf}}=\gamma_5.
$$

The dictionary is complex-linear. Over $\mathbb{R}$ it splits into two real forms: the products of $\gamma_0,\dots,\gamma_3$ satisfy the $\mathrm{Cl}_{1,3}$ relations and span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$, while the sixteen two-sided cells $L_aR_b$ span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

The central grading $\chi$ is a different object from $\gamma_5$. It is $\chi=i\tilde\Xi_{\mathrm{ad}}$, where $\tilde\Xi_{\mathrm{ad}}$ is the adjoined central root of $-1$, with $\tilde\Xi_{\mathrm{ad}}^{2}=-e_t$, so that $\chi^{2}=e_t$; it is also the difference $e_+-e_-$ of the two central idempotents. On the Dirac module it is represented by $\gamma_5$, and it is not $\Gamma$.

For translation from the gamma literature, with $\epsilon_{0123}=+1$ and $g=\mathrm{diag}(1,-1,-1,-1)$:

$$
\{\gamma_\mu,\gamma_\nu\}=2g_{\mu\nu}I_4,\qquad
(\gamma_k)^2=-I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu,\gamma_5\}=0,
$$

$$
[\gamma_\mu,\gamma_\nu]=2\gamma_\mu\gamma_\nu\quad(\mu\ne\nu),\qquad
[\gamma_a,S_{cd}]=g_{ac}\gamma_d-g_{ad}\gamma_c,\qquad
S_{cd}=\tfrac14[\gamma_c,\gamma_d],
$$

$$
\mathrm{tr}(\gamma_\mu\gamma_\nu)=4g_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$

$$
\mathrm{tr}(\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)
=4\bigl(g_{\mu\nu}g_{\rho\sigma}-g_{\mu\rho}g_{\nu\sigma}+g_{\mu\sigma}g_{\nu\rho}\bigr).
$$

No identity in this list is used in the body of the article. They are recorded so that a formula written in the gamma frame can be translated into the cells, and they are the only place in the article where gamma symbols occur.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

Charge conjugation is the pseudoautomorphism $A^{\mathrm c}=\Pi\bar A\Pi^{-1}$ of the complex Clifford algebra $\mathbb{C}\mathrm{l}_{n+m}$ induced by a real form $\mathrm{Cl}_{n,m}\subset\mathbb{C}\mathrm{l}_{n+m}$, and the matrix $\Pi$ that implements it is fixed by the algebra's division ring. Over a real division ring $K\cong\mathbb{R}$ it is proportional to the identity and the conjugation is trivial at the algebra level; over a quaternionic ring $K\cong\mathbb{H}$ it is a genuine product of generators and the conjugation interchanges particle and antiparticle; over the complex division ring $K\cong\mathbb{C}$ it is a conjugation between conjugate representations. The three cases are the three charge classes: charged states at $Ϙ=\pm1$, neutral particles with antiparticles at $Ϙ=0$, and truly neutral particles at $Ϙ=\bar{0}$. The twice-conjugated spinor is $(\xi^{\mathrm c})^{\mathrm c}=\Pi\bar\Pi\,\xi$. The sign of the product belongs to the representation and not to the division ring: for the invariant matrix $\Pi=\epsilon=i\sigma_2$ it is $-I$, so a single chiral half obeys $\xi^{\mathrm{cc}}=-\xi$, while the Dirac module, where $\eta_C^{2}=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$, obeys $C^{2}=\mathrm{id}$.

The biquaternion framework's algebra is the complex Clifford algebra $\mathbb{C}\mathrm{l}_{2}$, and read as a real algebra it is $\mathrm{Cl}_{3,0}$, whose division ring is $\mathbb{C}$: the charged case, by the table itself. Its real forms $\mathrm{Cl}_{0,2}\cong\mathbb{H}$ and $\mathrm{Cl}_{2,0}\cong M_2(\mathbb{R})$ carry the neutral and the truly neutral cases. The division ring therefore places the three charge classes in one algebra: the photon's real self-conjugacy is the case $K\cong\mathbb{R}$, the neutron's neutrality is the case $K\cong\mathbb{H}$, and the charged fields are the complexification. What is transcribed is the classification and the physical assignments; what is recomputed here is the algebra-level form of the pseudoautomorphism, the identity case over a real division ring, and the involution property $\eta_C^{2}=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}\cong\mathbb{C}\mathrm{l}_{2}\cong\mathrm{Cl}_{3,0}$ | Biquaternion algebra; complex Clifford algebra generated by two elements (complex dimension four), and $\mathrm{Cl}_{3,0}$ as a real algebra, so $d=3$ |
| $\mathrm{Cl}_{n,m}$, $d=n-m$ | Real Clifford algebra with $n$ positive and $m$ negative squares, a real form of $\mathbb{C}\mathrm{l}_{n+m}$; $\mathrm{Cl}_{0,2}\cong\mathbb{H}$, $\mathrm{Cl}_{2,0}\cong M_2(\mathbb{R})$, $\mathrm{Cl}_{1,1}\cong M_2(\mathbb{R})$ |
| $K$, $d=n-m\bmod8$ | Division ring of the real form: $\mathbb{R}$ at $d\equiv0,2$, $\mathbb{H}$ at $d\equiv4,6$, $\mathbb{C}$ at $d\equiv3,7$, $\mathbb{R}\oplus\mathbb{R}$ at $d\equiv1$, $\mathbb{H}\oplus\mathbb{H}$ at $d\equiv5$ |
| $A^{\mathrm c}=\Pi\bar A\Pi^{-1}$ | Charge-conjugation pseudoautomorphism; $\bar{\cdot}$ is coefficient conjugation |
| $\Pi$ | Charge-conjugation matrix; a product of frame cells, fixed only up to a scalar |
| $G_0=iR_{\vec e_x}^{\mathrm{axf}}$, $G_k=iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ | Four generator cells, one per coordinate, $k=x,y,z$; $(iR_{\vec e_x}^{\mathrm{axf}})^2=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ and $(iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}})^2=-L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ |
| $L_a\psi=a\psi$, $R_b\psi=\psi b$, $L_{a}R_{b}$ | One-sided multipliers and two-sided cells; $L_{a}R_{b}\psi=a\psi b$; $i^2=-1$ |
| $\xi^{\mathrm c}=\Pi\bar\xi$ | Conjugated spinor of the fundamental representation; $(\xi^{\mathrm c})^{\mathrm c}=\Pi\bar\Pi\,\xi$ |
| $\Pi\bar\Pi=\pm I$ | The square on a chiral half: $-I$ for $\Pi=\epsilon=i\sigma_2$, so $\xi^{\mathrm{cc}}=-\xi$; the Dirac module obeys $C^{2}=\mathrm{id}$ |
| $\eta_C=-L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ | Module representative of charge conjugation; odd, $\eta_C^2=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ |
| $C[\psi]=-L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\psi^{*}$ | Module form of charge conjugation (CPT article) |
| $\gamma_\mu$, $\Gamma=\gamma_5=-iR_{\vec e_z}^{\mathrm{axf}}$ | Frame cells of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$; they appear only in *The Gamma Formulation* |
| $\eta=R_{\vec e_x}^{\mathrm{axf}}$ | Cell of the transposed (CPT) form of the map; $\eta^{2}=R_{\vec e_x^{2}}^{\mathrm{axf}}=-L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ |
| $Ϙ=\pm1,0,\bar{0}$ | Charged (either sign), neutral, truly neutral charge states |
| $\mathbb{H}_{\mathbb{B}}\subset\mathbb{B}$ | Real-quaternion subspace, $\cong\mathrm{Cl}_{0,2}$, the quaternionic real form |

## Further Reading

- B. L. van der Waerden, *Group Theory and Quantum Mechanics* (Springer, 1974), and R. Brauer and H. Weyl, "Spinors in $n$ dimensions," *American Journal of Mathematics* **57** (1935) 425–449, for spinors over the division rings $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$.
- M. F. Atiyah, R. Bott and A. Shapiro, "Clifford modules," *Topology* **3** (1964) 3–38, for the classification of real and complex Clifford algebras and their division rings.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the intrinsic order-two maps and the pseudoautomorphism of a Clifford algebra.
- P. K. Rashevskii, "The theory of spinors," *Uspekhi Matematicheskikh Nauk* **10** (1955) 3–110 (*American Mathematical Society Translations* (2) **6** (1957) 1–110), for the classification of the fundamental automorphisms.
- V. V. Varlamov, "Spinor Structure and Internal Symmetries," *International Journal of Theoretical Physics* **54** (2015) 3533–3576 (arXiv:1409.1400), for the division-ring trichotomy of the charge-conjugation pseudoautomorphism and the charged, neutral and truly neutral classes.
- Companion articles: [The CPT Theorem in Biquaternionic Form](the-cpt-theorem-in-biquaternionic-form.html); [The Spin–Charge Hilbert Space and the SU(3) Supermultiplets in Biquaternionic Form](the-spin-charge-hilbert-space-and-the-su3-supermultiplets-in-biquaternionic-form.html); [The Photon in Biquaternionic Form](the-photon-in-biquaternionic-form.html); [The Neutron in Biquaternionic Form](the-neutron-in-biquaternionic-form.html); [The Neutrino and Majorana Fermions in Biquaternionic Form](the-neutrino-and-majorana-fermions-in-biquaternionic-form.html); *Real Spinors and Reality Conditions on the Biquaternion Algebra with Hermitian Adjoint*; *Clifford Algebra Representation*; *The Brauer Wall Group and the Eightfold Way*.
