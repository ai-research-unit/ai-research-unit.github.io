# __Charge Conjugation and the Division Ring: Charged, Neutral and Truly Neutral Particles in Biquaternionic Form__

## Introduction

Charge conjugation is the discrete operation that exchanges a particle with its antiparticle. In the companion article *The CPT Theorem in Biquaternionic Form* it is built explicitly on the spinor module, $C[\psi]=i\gamma^2\psi^{*}$, and its internal matrix is found to be an **odd** Clifford element with no representative in the biquaternion algebra. The present article asks the question that computation cannot answer: **when is $C$ trivial?** A symmetry that can be the identity on some representations is a symmetry that is not a symmetry of those states, and the class of particles on which charge conjugation acts trivially has a name — the **truly neutral** particles — and a place in physics: the photon, the $\pi^0$, the $\eta$, the $\phi$, the $Z$ boson, and the neutral members of isomultiplets whose charge-conjugation phase is real.

The classification of the algebra literature answers the question with a single algebraic datum. Charge conjugation is the **pseudoautomorphism** $\bar{A}=\Pi A^{*}\Pi^{-1}$ of a real Clifford algebra $\mathrm{Cl}_{p,q}$, and the matrix $\Pi$ that implements it is fixed by the **division ring** $K$ of the algebra: over a real division ring $K\cong\mathbb{R}$ the matrix is proportional to the identity, so the map is trivial; over a quaternionic division ring $K\cong\mathbb{H}$ it is a genuine product of generators, so the map is the particle–antiparticle interchange. The division ring, in other words, is what decides whether a particle can be its own antiparticle.

The article is organised as follows. A first section recalls the pseudoautomorphism and its matrix. A second states the division-ring trichotomy and computes $C^{2}$ in each case. A third reads the trichotomy as the three classes of particles, charged, neutral and truly neutral, and identifies the biquaternion algebra's place in it. A fourth section separates what the framework supplies from what it transcribes, and a closing section lists the open questions.

**Conventions.** We use those of *Conventions in the Biquaternion Universe* and the companion CPT article. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong M_2(\mathbb{C})$, with basis $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, central scalar imaginary $i$, and matrix realization $\Phi(e_0)=I_2$, $\Phi(e_k)=-i\sigma_k$, $\Phi(i)=iI_2$. Its real forms used below are $\mathrm{Cl}_{2,0}\cong M_2(\mathbb{R})$, $\mathrm{Cl}_{1,1}\cong M_2(\mathbb{R})$, and $\mathrm{Cl}_{0,2}\cong\mathbb{H}$; the algebra is the complex Clifford algebra $\mathbb{C}\mathrm{l}_2$, equivalently the complexification $\mathrm{Cl}_{0,2}\otimes_{\mathbb{R}}\mathbb{C}$. The conjugations are ${}^{\natural}$ (quaternion), $\bar{\cdot}$ (complex), ${}^{*}=({}^{\natural})^{\,*}$ (Hermitian); the sectors are $\mathbb{M}_-$ (material, anti-Hermitian) and $\mathbb{M}_+$ (informational, Hermitian); and the spinor module is $S=\mathbb{C}^2$. The discrete operations are written $C$, $P$, $T$ as in the CPT article, and their algebra-level representatives are the fundamental automorphisms of the same article's Clifford section.

- Companion article *The CPT Theorem in Biquaternionic Form*, for the explicit $C[\psi]=i\gamma^2\psi^{*}$ and for the Clifford classification of the operations as the fundamental automorphisms and the charge-conjugation pseudoautomorphism.
- The mathematics articles *Division Rings*, *Central Simple Algebras and the Brauer Group* and *The Brauer Wall Group and the Eightfold Way*, for the division ring as an isomorphism invariant of a real or complex algebra.
- The mathematics article *List of Clifford Algebras and Spin Groups*, for the classification $\mathrm{Cl}_{p,q}$ by $p-q\bmod 8$ that the trichotomy below uses.
- Companion article *Real Spinors and Reality Conditions on the Biquaternion Algebra with Hermitian Adjoint*, for reality conditions and real structures on the algebra.
- Companion articles *The Neutron in Biquaternionic Form* and *The Proton in Biquaternionic Form*, for the two charge states of one isospin doublet.

## The Pseudoautomorphism and Its Matrix

The discrete operations $P$, $T$, $PT$ are the three non-trivial **fundamental automorphisms** of a real Clifford algebra $\mathrm{Cl}_{p,q}$ — the grade involution, the reversion and their composite, the Clifford conjugation — and they act on each graded piece by a sign. Charge conjugation is not of this kind. It is the **pseudoautomorphism**

$$
A\;\longmapsto\;\bar{A}=\Pi\,A^{*}\,\Pi^{-1},
$$

the complex conjugation of the algebra element followed by the inner automorphism by a matrix $\Pi$. Two features make it a pseudoautomorphism rather than an automorphism of $\mathrm{Cl}_{p,q}$. First, it is **conjugate-linear**: it contains $A^{*}$, and no automorphism of the real algebra does. Second, the matrix $\Pi$ does not preserve the real subalgebra; it conjugates the generators with a sign,

$$
\Pi\,\gamma_{\hat{a}}\,\Pi^{-1}=-\gamma_{\hat{a}},
$$

which is the property that distinguishes it from the inner automorphisms implementing $P$ and $T$. The map is the algebra-level form of the module operation $C[\psi]=\eta_C\psi^{*}$, with $\Pi$ the algebra-level charge-conjugation matrix and $\eta_C=i\gamma^{2}$ its module representative up to a phase; because $\Pi$ is determined only up to a nonzero scalar, the phase of $\eta_C$ is free, exactly as the CPT article's explicit verification found.

### The Action on Spinors

On spinors the pseudoautomorphism acts by raising and lowering with the antisymmetric symbol. If $\xi^{\alpha}$ is a spinor of the fundamental representation of $\mathrm{Spin}^{+}(1,3)\cong\mathrm{SL}(2,\mathbb{C})$, the conjugated spinor is

$$
\bar{\xi}^{\,\dot{\alpha}}=\Pi^{\dot{\alpha}\alpha}\,\xi_{\alpha},
$$

and conjugating twice returns

$$
\bar{\bar{\xi}}^{\,\alpha}=\Pi^{\alpha\dot{\alpha}}\bigl(\Pi^{\beta\dot{\alpha}}\xi_{\beta}\bigr)^{*}=\pm\,\xi^{\alpha},
$$

the sign being that of $\Pi\dot{\Pi}$ — the product of $\Pi$ with its own conjugate — so that the relation between a particle and its antiparticle is controlled entirely by $\Pi$. This is the first appearance of the division ring in the question: the allowed matrices $\Pi$ are not arbitrary, and which ones occur is fixed by the algebra's division ring.

## The Division-Ring Trichotomy

The classification is a theorem of the Clifford-algebra literature and is transcribed here. Let $\mathbb{C}_n$ be a complex Clifford algebra with $n$ even, and let $\mathrm{Cl}_{p,q}\subset\mathbb{C}_n$, $n=p+q$, be a real subalgebra. Its **division ring** $K$ — the ring of scalars of its irreducible module — is $\mathbb{R}$ when $p-q\equiv 0,2 \pmod 8$ and $\mathbb{H}$ when $p-q\equiv 4,6\pmod 8$; the remaining classes give a sum of two such rings. The form of the charge-conjugation matrix $\Pi$ follows the division ring:

| division ring $K$ | $p-q\bmod 8$ | matrix $\Pi$ | map $C$ |
|---|---|---|---|
| $\mathbb{R}$ | $0,2$ | $\Pi\propto I$ | trivial (identity) |
| $\mathbb{H}$ | $4,6$ | $\Pi$ a product of generators, $\Pi\dot{\Pi}=\pm I$ | particle–antiparticle interchange |
| $\mathbb{C}$ | complex algebra $F=\mathbb{C}$ | $\Pi$ a product of generators | conjugation, non-trivial |
| $\mathbb{R}\oplus\mathbb{R}$, $\mathbb{H}\oplus\mathbb{H}$ | $1$, $5$ | as in the corresponding one-ring case | as above |

### The Three Cases

The load-bearing case is the first. Over a **real** division ring the pseudoautomorphism reduces to the identity, because $\Pi\propto I$ makes $\bar{A}=\Pi A^{*}\Pi^{-1}$ act as the complex conjugation of the coefficients — which on the real algebra is the identity — and the charge-conjugation operation is trivial on every representation carried by that algebra. The particles described by those representations are their own antiparticles in the strongest sense: not merely a neutral particle equal to its conjugate, but a particle on which the conjugation *does nothing*.

## The Meaning of $C^{2}$

The sign in $\bar{\bar{\xi}}=\pm\xi$ is the square of charge conjugation, and it is worth isolating because $C^{2}=1$ versus $C^{2}=-1$ is the difference between an operation of order two and one of order four. The value is read from $\Pi\dot{\Pi}$:

- For a **real** division ring, $\Pi\propto I$, so $\Pi\dot{\Pi}=I$ and $C^{2}=1$; the conjugation is an involution, and trivially so.
- For a **quaternionic** division ring, $\Pi\dot{\Pi}=+I$ when the generator counts $a,b$ are $\equiv0,1\pmod 4$ and $\Pi\dot{\Pi}=-I$ when $a,b\equiv2,3\pmod 4$. For the fundamental representation of $\mathrm{Spin}^{+}(1,3)$, built on $\mathrm{Cl}_{0,2}\cong\mathbb{H}$, the counts give $a-b\equiv0\pmod 4$, so $\Pi\dot{\Pi}=I$ and $C^{2}=1$ once more. That the fundamental representation has $C^{2}=1$ is an invariant fact of the spinor structure, and it is the algebraic expression of the standard requirement that the free Dirac equation admit an involutive charge conjugation.

### The Independence of $C^{2}$

The independence of $C^{2}$ from the representation is the point of the division-ring reading. In ordinary field theory the sign of $C^{2}$ depends on the dimension of the Dirac matrices and is fixed by convention and by the choice of representation; here it is fixed by the algebra, and for the representations the framework actually uses it is $+1$. What is genuinely division-ring-dependent is not the sign but the **triviality** of $C$: a real division ring makes the map the identity, a quaternionic one makes it the interchange, and a complex one makes it a conjugation between conjugate representations.

## The Three Classes of Particles

The trichotomy of the previous section is the algebraic form of the three classes of charge states.

### The Dictionary

**Charged particles.** Described by the **complex** representations of $\mathrm{Spin}^{+}(1,3)$, for which the pseudoautomorphism is non-trivial and maps a representation to its complex conjugate. The charge states $\pm1$ correspond to a representation and to its conjugate, and $C$ exchanges them: $C$ maps the particle to a different state, its antiparticle. The electron, the proton and the charged mesons are of this class.

**Neutral particles.** Described by the **real** representations of $\mathrm{Spin}^{+}(1,3)$ whose algebra has quaternionic division ring $K\cong\mathbb{H}$. The pseudoautomorphism is non-trivial, but it acts *within* the representation and interchanges the particle with its antiparticle: the neutron and the neutrino are of this class, states that are neutral (charge state $0$) yet distinct from their conjugates.

**Truly neutral particles.** Described by the **real** representations whose algebra has real division ring $K\cong\mathbb{R}$. The pseudoautomorphism is trivial, so the particle and its antiparticle are the same state, and the conjugation carries no phase. The photon is the paradigm; the $\pi^{0}$, the $\eta$ and the $\phi$ — the neutral members of isomultiplets in the class — are the hadronic examples. Following the source's notation, this charge state is written $\bar{0}$ to distinguish it from the neutral state $0$.

The three classes are exactly the split of the charge values $\{-1,0,\bar{0}\}$ that the companion article *The Spin–Charge Hilbert Space and the SU(3) Supermultiplets in Biquaternionic Form* uses to organise the charge multiplets. The present article supplies the reason the split is threefold and not twofold: a neutral particle can fail to be truly neutral precisely when its representation is real but not of real type, which is to say when the algebra's division ring is quaternionic rather than real.

## The Biquaternion Reading

The biquaternion algebra is the **complex** Clifford algebra $\mathbb{C}\mathrm{l}_{2}$, equivalently the complexification of the quaternionic real algebra $\mathrm{Cl}_{0,2}\cong\mathbb{H}$, and it is the complexification that places the framework's own fields.

### The Three Real Forms

The three cases of the trichotomy are realised by choosing which real form of the algebra carries the field:

- **Charged fields** are carried by the complex algebra $\mathbb{B}$ itself, or by an explicit factor of $\mathbb{C}$: the complexified spinor module, whose charged conjugation is the conjugate-linear $\eta_C$-twisted complex conjugation. This is the framework's default, and it is why the companion articles treat charged fermions and the charged gauge fields directly.
- **Neutral fields** are carried by the real form $\mathrm{Cl}_{0,2}\cong\mathbb{H}\subset\mathbb{B}$, the real-quaternion subspace in which the algebra is a division ring. Its charge conjugation is the non-trivial particle–antiparticle interchange, and the real form is the one the corpus records as the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ and as the division-ring locus where the integral theory is complete.
- **Truly neutral fields** are carried by a real form of real type, $\mathrm{Cl}_{2,0}\cong M_2(\mathbb{R})$ or $\mathrm{Cl}_{1,1}$, both of which occur in $\mathbb{B}$ as the real subspaces on which the quadratic form has definite or split signature. On these the charge conjugation degenerates to the identity, and the field is genuinely its own antiparticle.

The reading is not a derivation, and it does not add a new field content to the framework. Its value is that it locates the three charge classes in the *same* algebra, as three real forms or as the complexification of one of them, and it explains why the framework's material and informational sectors, which are real subspaces of a complex algebra, are the natural carriers of neutral and of charged structure respectively. The photon article's finding that the free photon is a real, self-conjugate field is the case $K\cong\mathbb{R}$; the neutron article's finding that the neutron is neutral but distinguishable from the antineutron is the case $K\cong\mathbb{H}$.

## What the Framework Establishes, Transcribes, and Does Not

**Established, and recomputed.**

- The charge-conjugation pseudoautomorphism is $\bar{A}=\Pi A^{*}\Pi^{-1}$, conjugate-linear, with $\Pi\gamma_{\hat{a}}\Pi^{-1}=-\gamma_{\hat{a}}$; it is not an automorphism of the real form, and this is the algebra-level form of the CPT article's finding that $C$'s internal matrix is odd.
- The twice-conjugated spinor is $\bar{\bar{\xi}}^{\,\alpha}=\pm\xi^{\alpha}$, with the sign the sign of $\Pi\dot{\Pi}$; for the fundamental representation of $\mathrm{Spin}^{+}(1,3)$ on the quaternionic algebra the sign is $+1$, so $C^{2}=1$. This is the spinor-structure expression of the standard requirement.
- Over a real division ring the matrix is $\Pi\propto I$ and the pseudoautomorphism is the identity; the corresponding particles are truly neutral. The three charge classes $+1$, $0$, $\bar{0}$ are respectively the complex representations, the real quaternionic representations, and the real representations of real type.

**Transcribed, not derived.**

- The classification theorem itself: that the form of $\Pi$ is governed by the division ring of the real subalgebra, and the correspondence $p-q\bmod 8\to K\in\{\mathbb{R},\mathbb{C},\mathbb{H}\}$.
- The physical identifications of the three classes — electron and proton charged, neutron and neutrino neutral, photon and $\pi^{0}$ and $\eta$ and $\phi$ truly neutral. These are the standard assignments of particle physics.
- The biquaternion realisation: that the framework's algebra is $\mathbb{C}\mathrm{l}_{2}$ and contains the real forms $\mathrm{Cl}_{2,0}$, $\mathrm{Cl}_{1,1}$ and $\mathrm{Cl}_{0,2}$ is the corpus's own Clifford-structure result; reading the three charge classes through them is the present article's organisation, not a theorem the algebra forces.

**Gap, left visible.**

- No derivation that a *given* physical particle's real form is the one assigned to it. The classification says which class each algebra's representations fall into; it does not, by itself, say that the neutron is quaternionic and the photon real. That identification is transcribed from the spin and charge assignments and is where a stronger framework would have to act.
- No $\mathbb{B}$-intrinsic form of the pseudoautomorphism, for the same reason the CPT article leaves $C$ external: $\Pi$ is a product of Clifford generators, and the odd generators are outside $\mathbb{B}$. The division-ring classification locates $C$ among the intrinsic maps of $\mathrm{Cl}_{p,q}$; it does not bring $C$ inside $\mathbb{B}$.
- No treatment of the charge-conjugation phase for composite or mixed states, and no statement about $K^{0}$–$\bar{K}^{0}$ mixing, where the truly-neutral reading of a neutral meson requires the superposition language the framework does not yet carry.

## Open Questions

1. **Is the framework's own $\mathbb{B}$ the charged case?** The complex algebra is the $F=\mathbb{C}$ case, so every field valued in $\mathbb{B}$ is charged by construction. Is the neutrality of a field then always the statement that its real form is $\mathrm{Cl}_{0,2}$ or $\mathrm{Cl}_{2,0}$, and can that be read off an equation rather than assigned?

2. **Which real form does the mass term select?** The Dirac mass term is the linear chiral pair, and the Majorana question of the neutrino article is exactly the question of a real form. Does the real structure $\flat=-{}^{*}$ pick out the quaternionic real form $\mathrm{Cl}_{0,2}$, and is the neutrino's neutrality thus the $K\cong\mathbb{H}$ case?

3. **$K^{0}$ and the truly neutral reading.** The source's own example list places $K^{0}$ among the truly neutral particles, which conflicts with the standard reading of $K^{0}$ as neutral but not truly neutral. Is the list to be read as a statement about a specific charge-conjugation phase, or is it a slip? The mixing of $K^{0}$ and $\bar{K}^{0}$ is the test.

4. **The sign of $C^{2}$ in higher-spin fields.** The fundamental representation has $C^{2}=1$; the corpus's higher-spin fields live in tensor powers and in the Rarita–Schwinger construction. Does the division-ring count give $C^{2}=1$ there too, or does the sign change with the spin, as it does in some standard conventions?

5. **Truly neutral composites.** A truly neutral field is one on which $C$ is the identity. Is the same true of a *composite* colour singlet, such as a quark–antiquark state in the framework's gauge-invariant sector, and does the division-ring criterion survive the composition?

## Summary

Charge conjugation is the pseudoautomorphism $\bar{A}=\Pi A^{*}\Pi^{-1}$ of a real Clifford algebra, and the matrix $\Pi$ that implements it is fixed by the algebra's division ring. Over a real division ring $K\cong\mathbb{R}$ it is proportional to the identity and the conjugation is trivial; over a quaternionic ring $K\cong\mathbb{H}$ it is a genuine product of generators and the conjugation interchanges particle and antiparticle; over the complex field it is a conjugation between conjugate representations. The three cases are the three charge classes: charged particles at $Q=+1$, neutral particles with antiparticles at $Q=0$, and truly neutral particles at $Q=\bar{0}$. The twice-conjugated spinor is $\bar{\bar{\xi}}=\pm\xi$, with the sign the sign of $\Pi\dot{\Pi}$; for the fundamental representation of $\mathrm{Spin}^{+}(1,3)$ the sign is $+1$, so $C^{2}=1$, an invariant fact of the spinor structure and the algebraic expression of the standard requirement on charge conjugation.

The biquaternion framework's algebra is the complex Clifford algebra $\mathbb{C}\mathrm{l}_{2}$, the charged case, and it contains the real forms $\mathrm{Cl}_{0,2}\cong\mathbb{H}$ and $\mathrm{Cl}_{2,0}\cong M_2(\mathbb{R})$ that carry the neutral and truly neutral cases. The division ring therefore places the three charge classes in one algebra: the photon's real self-conjugacy is the case $K\cong\mathbb{R}$, the neutron's neutrality is the case $K\cong\mathbb{H}$, and the charged fields are the complexification. What is transcribed is the classification and the physical assignments; what is established is the algebra-level form of the pseudoautomorphism, the identity case over a real division ring, and the sign of $C^{2}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}\cong\mathbb{C}\mathrm{l}_2$ | Biquaternion algebra, the complex Clifford algebra of dimension two |
| $\mathrm{Cl}_{p,q}$, $n=p+q$ | Real Clifford algebra; $\mathrm{Cl}_{0,2}\cong\mathbb{H}$, $\mathrm{Cl}_{2,0}\cong M_2(\mathbb{R})$, $\mathrm{Cl}_{1,1}\cong M_2(\mathbb{R})$ |
| $K$ | Division ring of $\mathrm{Cl}_{p,q}$: $\mathbb{R}$ if $p-q\equiv0,2$, $\mathbb{H}$ if $p-q\equiv4,6\pmod 8$ |
| $A\mapsto\bar{A}=\Pi A^{*}\Pi^{-1}$ | Charge-conjugation pseudoautomorphism; conjugate-linear |
| $\Pi$ | Charge-conjugation matrix; $\Pi\gamma_{\hat a}\Pi^{-1}=-\gamma_{\hat a}$, fixed only up to a scalar |
| $\bar{\xi}^{\,\dot\alpha}=\Pi^{\dot\alpha\alpha}\xi_\alpha$ | Conjugated spinor of the fundamental representation |
| $\Pi\dot{\Pi}=\pm I$ | Determines $C^{2}$: $+I\Rightarrow C^{2}=1$, $-I\Rightarrow C^{2}=-1$ |
| $C[\psi]=i\gamma^{2}\psi^{*}$ | Module form of charge conjugation (CPT article) |
| $Q=+1,0,\bar{0}$ | Charged, neutral, truly neutral charge states |
| $\mathbb{H}_{\mathbb{B}}\subset\mathbb{B}$ | Real-quaternion subspace, $\cong\mathrm{Cl}_{0,2}$, the quaternionic real form |
| $\mathbb{M}_-,\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |

## Further Reading

- B. L. van der Waerden, *Group Theory and Quantum Mechanics* (Springer, 1974), and R. Brauer and H. Weyl, "Spinors in $n$ dimensions," *American Journal of Mathematics* **57** (1935) 425–449, for spinors over the division rings $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$.
- M. F. Atiyah, R. Bott and A. Shapiro, "Clifford modules," *Topology* **3** (1964) 3–38, for the classification of real and complex Clifford algebras and their division rings.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the intrinsic order-two maps and the pseudoautomorphism of a Clifford algebra.
- P. K. Rashevskii, "The theory of spinors," *Uspekhi Matematicheskikh Nauk* **10** (1955) 3–110 (*American Mathematical Society Translations* (2) **6** (1957) 1–110), for the classification of the fundamental automorphisms.
- V. V. Varlamov, "Spinor Structure and Internal Symmetries," *International Journal of Theoretical Physics* **54** (2015) 3533–3576 (arXiv:1409.1400), for the division-ring trichotomy of the charge-conjugation pseudoautomorphism and the charged, neutral and truly neutral classes.
- Yu. P. Stepanovsky and V. V. Varlamov, on the interpretation of the discrete symmetries through the automorphism groups of Clifford algebras, for the extension of the classification used here.
- Companion articles: *The CPT Theorem in Biquaternionic Form*; *The Spin–Charge Hilbert Space and the SU(3) Supermultiplets in Biquaternionic Form*; *The Photon in Biquaternionic Form*; *The Neutron in Biquaternionic Form*; *The Neutrino and Majorana Fermions in Biquaternionic Form*; *Real Spinors and Reality Conditions on the Biquaternion Algebra with Hermitian Adjoint*; *Clifford Structure of the Biquaternion Algebra*; *The Brauer Wall Group and the Eightfold Way*.
