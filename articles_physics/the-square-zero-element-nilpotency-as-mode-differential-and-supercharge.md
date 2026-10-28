# __The Square-Zero Element: Nilpotency as Mode, Differential and Supercharge__

## Introduction

The equation $X^2=0$ is one line, and the corpus uses it in five places. The one-mode ladder of $\mathbb{B}$ has $\vec\Upsilon_x^2=\vec\Upsilon_y^2=0$. The BRST transformation has $s^2=0$. The supersymmetric charge has $Q^2=0$. The Grassmann label has $\theta^2=0$. The chiral corner of a Dirac symbol is the Pauli ladder $\sigma_\pm$ with $\sigma_\pm^2=0$. The same line, five objects; and a sixth object, the physical null momentum, is often placed beside them although it does not satisfy the line.

The purpose of this article is to state what separates these objects. The equation does not separate them. **A square-zero object has no physical role until three further structures are named: what it acts on, which grading it is odd under, and what its square is paired with.** The three answers give the three principal roles.

- **The mode.** $X$ is an element of an associative algebra acting on a module; it is odd under an inner parity; it is paired with its adjoint by the canonical anticommutator $\{X,X^*\}=e_t$. Its content is occupation, and its square-zero is Pauli exclusion.
- **The differential.** $X$ is an odd derivation or operator on a graded complex; it is odd under ghost number; it is paired with itself by $X^2=0$. Its content is cohomology, and its square-zero is the statement that the image lies in the kernel.
- **The supercharge.** $X$ is an odd operator on a graded Hilbert space; it is odd under chirality or fermion parity; it is paired with its adjoint by $\{Q,Q^\dagger\}=H$. Its content is the spectrum, the zero modes and the index.

Two further objects complete the list. The **Grassmann label** multiplies rather than acts, and has no module, no vacuum and no cohomology; its square-zero is the truncation of the exterior algebra. The **chiral corner** is the local Pauli ladder of a Dirac symbol at a node, not a global operator; its square-zero is the two-level ladder at the crossing. One object is excluded: the **physical null momentum**, which lies on the same cone as the nilpotent but is a zero divisor with a nonzero square.

The article's new content is not a new physical result. It is the classification, the three distinctions that the separate articles do not state together, and the nine interpretations collected under it. The first distinction is between the two $\mathbb{Z}/2$ gradings in play: the **Clifford parity**, which is trivial on $\mathbb{B}=\mathrm{Cl}^0_{1,3}$, and the **occupation parity**, which is the inner automorphism by $(-1)^F=i\vec e_z$ and is nontrivial on $\mathbb{B}$. The one-mode ladder is even in the first and odd in the second; "fermionic" names the second, not the first. The second is the distinction between the two anticommutators: the mode's is the identity, a number, and the supercharge's is the Hamiltonian, an operator. The same algebra with a different right-hand side has a different physics. The third is the distinction between the three pairings of the square: the mode's anticommutator splits the identity into the two rungs; the supercharge's is the Hamiltonian, whose kernel is the zero-mode space; the differential has no such pairing at all, and its cohomology is the whole content.

The same nilpotent carries the lattice and semiclassical interpretations: the null point of a band symbol, the paired zero of a lattice symbol, the vanishing phase gradient at a turning point, and the cone as the degenerate end of a contraction. Those are not a fourth role. Each uses the mode or the corner, and they are collected in §*The Nine Interpretations*, each with its boundary.

The article is organised as follows. The results it borrows are stated with their sources. The equation and the three questions are then set out, with the nilpotent cone and the two-term complex that every nilpotent defines. The three principal roles follow, one section each; then the two boundary objects, the excluded case and the nine interpretations. The gradings are collected in one table, the taxonomy in a second and the interpretations in a third, and the closing sections state what the classification buys, what it does not claim, and the open questions it inherits.

## The Results It Uses

**The conventions.** The notation, the Clifford dictionary and the sector splitting are those of *Conventions in the Biquaternion Universe*; the algebra and its two sectors are those of *Introduction to the Biquaternion Universe*, *The Material Sector: Four-Vectors, Interval and Lorentz Action* and *The Informational Sector: States, Observables and Probability*.

**The algebra.** The one-mode canonical anticommutation relations in $\mathbb{B}$, the pair $\vec\Upsilon_x,\vec\Upsilon_y$, the rungs $\tilde\Pi_\pm$, the inner parity $(-1)^F=i\vec e_z$, the capacity count and the bosonic obstruction are those of *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*; the roots of $+1$, the idempotents and the halving map are those of *Square Roots of One and the Idempotents of the Biquaternion Algebra*; the vacuum idempotent, its zero-divisor property and the Peirce corner at the vacuum are those of *The Biquaternion Vacuum as a Minimal Idempotent*; the Peirce decomposition, the matrix units and the Peirce coordinates are those of *Ideals, Peirce Decompositions and Spinors in the Biquaternion Algebra* and *$M_2(\mathbb{C})$ Model : Peirce Coordinates, Matrix Units and the Spinor Planes*.

**The cone.** The classification of the nilpotent cone, the pure condition, the index-two property and the distinction from the physical null momentum are those of *Square Roots of Zero and the Nilpotents of the Biquaternion Algebra*; the rank-one matrix model is that of *$M_2(\mathbb{C})$ Representation : Rank-One Matrices and the Determinantal Variety*; the root sets across the twelve products are those of *Square Roots of a General Element in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*; the zero-divisor cone, its topology and its massless interpretation are those of *N-Regularity and N-Degeneracy in the Biquaternion Algebra*, *The Zero-Divisor Cone and the Massless Spectrum*, *The Topology of the Zero-Divisor Cone* and *The Light Cone as the Biquaternion Zero-Divisor Cone*.

**The differential.** The BRST transformation, the ghost fields, the Grassmann envelope, the nilpotency $s^2=0$ inherited from associativity and the Jacobi identity, the ghost-number grading, the cohomological characterization of the physical states and the Kugo–Ojima quartet are those of *BRST Symmetry in Biquaternionic Form*.

**The supercharge.** The algebra $\{Q,Q^\dagger\}=H$, $Q^2=0$, the partner spectra, the zero modes, the Witten index, the biquaternion Dirac operator $\mathcal{D}=Q+Q^\dagger$ with $\mathcal{D}^2=\Box$, chirality as the grading, the mass pair and the superpotential are those of *Supersymmetric Quantum Physics in the Biquaternion Framework*; the statement that an odd supercharge is an element of the ambient graded algebra and never an element of $\mathbb{B}$ is that of *The Superalgebra Reading and the Odd Extension in Biquaternionic Form*; the several gradings and the warning against conflating them are those of *The Grading, Fermion Parity and the Two Sectors in Biquaternionic Form*.

**The label, the corner and the interpretations.** The Grassmann algebra as the minimal odd extension, Berezin integration and the fermionic coherent states are those of *Grassmann Coherent States in Biquaternionic Form*; the exact one-mode Wick theorem is that of *The Wick Theorem in Biquaternionic Form*; the Jordan–Wigner square root and its string are those of *The Jordan–Wigner Transformation in Biquaternionic Form*; the Dirac points, the chiral blocks and the topological nodes are those of *Dirac Matter: Graphene, Dirac Cones and Topological Insulators in Biquaternionic Form* and *Fermion Doubling and the Nielsen–Ninomiya Theorem in Biquaternionic Form*; the index-two ceiling and the qutrit outside the algebra are those of *The Qutrit Problem: Three-Level Systems Outside the Biquaternion Algebra*; the hole-theory interpretation is that of *The Dirac Sea, Hole Theory and Antimatter in Biquaternionic Form*; and the WKB phase gradient and the squeezing contraction are those of *The WKB Approximation and the Hamilton–Jacobi Equation in Biquaternionic Form* and *Squeezing Beyond the Biquaternion Algebra*.

Nothing in this article re-derives those results. The coordinate computation of §*The Nilpotent Cone* is the elementary form of the classification, and the rest of the article adds the comparison and the nine interpretations.

## The Equation and the Three Questions

### What a Nilpotent Is

A nilpotent is a nonzero element $X$ of an algebra with

$$
X^2=0 .
$$

In a finite-dimensional algebra four consequences are immediate and are used throughout. The image of $X$ lies in its kernel, $\mathrm{im}\,X\subseteq\ker X$. The element is a zero divisor: $X^2=0$ exhibits $X$ as a nonzero element annihilated by a nonzero element. It is not invertible. And in a matrix algebra its trace vanishes and its spectrum is $\{0\}$.

The same element supports two readings, and the two readings are the seed of the whole taxonomy. Read on a module $M$, $X$ is a linear map whose image lies in its kernel. Read on the algebra by left multiplication, $L_X(A)=XA$, it is a two-term complex,

$$
0\longrightarrow A\stackrel{L_X}{\longrightarrow}A\longrightarrow0 ,
$$

whose cohomology is the pair $H^0=\ker L_X$, $H^1=A/\mathrm{im}\,L_X$. The module reading asks what $X$ does to states; the complex reading asks what $X$ does to the algebra. The mode is the module reading, the differential is the complex reading, and the supercharge is the graded module reading between them; the fact that they are readings of the same element is why the same equation appears in all three.

The complex is the more general object, and it is worth fixing its two cohomology spaces once. For a nilpotent $X$ acting on a space $M$, the two-term complex

$$
0\longrightarrow M\stackrel{X}{\longrightarrow}M\longrightarrow0
$$

has

$$
H^0=\ker X,\qquad H^1=M/\mathrm{im}\,X .
$$

The dimension of $H^0$ is the number of closed states; the dimension of $H^1$ counts the states modulo the exact ones. Their difference is the index of the complex, the graded count that the roles below use. The mode is this minimal case. A graded complex replaces $M$ by a direct sum of graded pieces and $X$ by maps between adjacent pieces; the supercharge and the BRST differential are graded complexes of this kind, and their cohomology is read degree by degree. The two-term formulas are the local model for each degree. The roles that have a complex are readings of these two spaces, degree by degree, and the differences between the roles are differences in what supplies the splitting of $M$ and in which grading is imposed on the cohomology.

### The Nilpotent Cone

Write a general element as $\tilde Q=Q_te_t+\vec Q$ with $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ and complex coefficients. The square is

$$
\tilde Q^2=\bigl(Q_t^2-(\vec Q,\vec Q)\bigr)e_t+2Q_t\vec Q,
\qquad
(\vec Q,\vec Q)=Q_x^2+Q_y^2+Q_z^2 .
$$

The equation $\tilde Q^2=0$ splits into $2Q_t\vec Q=0$ and $Q_t^2=(\vec Q,\vec Q)$. The scalar branch returns $\tilde Q=0$. The nonzero branch has $Q_t=0$ and $(\vec Q,\vec Q)=0$: the nilpotent is a pure element with an isotropic complex vector part. The set is the **nilpotent cone**, of complex dimension two and real dimension four, inside the six-real-dimensional zero-divisor cone. In this algebra every nilpotent has index two, so $\vec\Upsilon^3=0$ exactly when $\vec\Upsilon^2=0$, and no nilpotent is an idempotent; the two classes meet only at the origin. In the $2\times2$ matrix model the nilpotents are the nonzero trace-free singular matrices.

The pure condition is what separates the nilpotent from the rest of the cone. An element of the cone with a nonzero scalar part is a complex multiple of a non-trivial idempotent; it is a zero divisor but not a nilpotent. The nilpotent is the part of the cone that is also pure. The table places the three nearby objects beside it.

| object | equation | where it lives | physical interpretation |
|---|---|---|---|
| nilpotent | $\vec\Upsilon^2=0$, $\vec\Upsilon\neq0$ | pure vector subspace, complex isotropic | one fermionic mode; null symbol; contraction limit |
| physical null four-momentum | $\langle\tilde P\rangle_{\natural}=0$, $\tilde P^2\neq0$ | material sector $\mathbb{M}_-$ | photon or other massless carrier |
| idempotent | $\tilde\Pi^2=\tilde\Pi$ | all of $\mathbb{B}$; the Hermitian ones in $\mathbb{M}_+$ | state, rung, vacuum |
| Grassmann label | $\theta^2=0$ | outside $\mathbb{B}$ | odd label of a coherent state |

The second row is derived in §*The Excluded Case: The Physical Null Momentum*, the third is the rung of §*The Mode*, and the fourth is the label of §*The Label*. The table is a map of the neighbourhood, not a list of nilpotents: only the first row satisfies $X^2=0$.

### The Three Questions

The equation $X^2=0$ answers none of the following.

1. **What does $X$ act on?** A module with a vacuum and a number operator; a graded complex of fields; a graded Hilbert space; or nothing at all, if $X$ is a label that multiplies.
2. **Which grading is $X$ odd under?** The inner occupation parity; the ghost number; the chirality or fermion parity; the exterior degree; or no grading, if $X$ is the local block of a symbol.
3. **What is $X$ paired with?** Its adjoint by the canonical anticommutator, which is the identity; its adjoint by a Hamiltonian, which is an operator; itself, since its square is zero; or nothing, which is the label.

The three answers are not independent, but none of them is implied by the equation. A nilpotent element of an algebra can be read as a mode, as a differential or as a supercharge, and the same element can be read in more than one way; what fixes the physical role is the structure one chooses to use.

### The Pairing of the Square

The sharpest algebraic difference between the three principal roles is the right-hand side of the anticommutator.

**The mode.** A nilpotent $X$ with a partner $X^*$ such that

$$
XX^*+X^*X=e_t
$$

splits the identity into two orthogonal idempotents,

$$
\Pi_+=XX^*,\qquad \Pi_-=X^*X,\qquad \Pi_++\Pi_-=e_t,\qquad \Pi_+\Pi_-=\Pi_-\Pi_+=0 .
$$

The module is the direct sum of the two images, $M=\Pi_+M\oplus\Pi_-M$, and the two cohomology spaces of the two-term complex are represented by these two images. The index is zero, and the content is the pair of rungs.

**The supercharge.** A nilpotent $Q$ with a partner $Q^\dagger$ such that

$$
QQ^\dagger+Q^\dagger Q=H
$$

has $H$ as the Hodge Laplacian of the graded complex on $\mathcal{H}_+\oplus\mathcal{H}_-$. Where $H$ is invertible the complex is acyclic; in general the cohomology is the kernel of $H$, and the index is the graded dimension of that kernel, the Witten index. The content is the zero-mode space and its grading.

**The differential.** A nilpotent $Q$ with no such partner has no pairing of the square. The cohomology is not the kernel of a Laplacian; it is the quotient $\ker Q/\mathrm{im}\,Q$, and it is the content.

The three cases are one algebra with three right-hand sides: the identity, the Hamiltonian, and nothing. The rest of the article fills in the three rows.

## The Mode

### The Pair and the Rungs

The one-mode algebra is generated by the canonical pair

$$
\vec\Upsilon_x=\tfrac12\bigl(i\vec e_x-\vec e_y\bigr),\qquad
\vec\Upsilon_y=\tfrac12\bigl(i\vec e_x+\vec e_y\bigr),
$$

with $\vec\Upsilon_x^2=\vec\Upsilon_y^2=0$, $\{\vec\Upsilon_x,\vec\Upsilon_y\}=e_t$ and $\vec\Upsilon_x^*=\vec\Upsilon_y$. The products $\tilde\Pi_+=\vec\Upsilon_x\vec\Upsilon_y$ and $\tilde\Pi_-=\vec\Upsilon_y\vec\Upsilon_x$ are orthogonal idempotents summing to $e_t$, and they are the two rungs. In the matrix image $\mathsf{M}_2(\vec e_k)=-i\sigma_k$,

$$
\mathsf{M}_2(\vec\Upsilon_x)=|0\rangle\langle1|,\qquad
\mathsf{M}_2(\vec\Upsilon_y)=|1\rangle\langle0|,\qquad
\mathsf{M}_2(i\vec e_z)=\sigma_3,
$$

with $|0\rangle=(1,0)^{\mathsf{T}}$ and $|1\rangle=(0,1)^{\mathsf{T}}$. The rungs act on the module as the ladder: $\vec\Upsilon_x\tilde\Pi_-=\vec\Upsilon_x$ and $\vec\Upsilon_y\tilde\Pi_+=\vec\Upsilon_y$, while $\vec\Upsilon_x\tilde\Pi_+=\vec\Upsilon_y\tilde\Pi_-=0$. The Peirce corners are those of *Ideals, Peirce Decompositions and Spinors in the Biquaternion Algebra*. The rest of this section is the cohomological and grading reading that the taxonomy adds.

Two of the nine interpretations, Jordan–Wigner and the exact one-mode Wick theorem, use the pair without adding a role. Neither is a separate row of the taxonomy; both are in §*The Nine Interpretations*.

### The Two Rungs Are the Cohomology

The two-term complex of the mode is

$$
0\longrightarrow S\stackrel{\vec\Upsilon_x}{\longrightarrow}S\longrightarrow0,
\qquad S=\mathbb{C}^2 .
$$

Its cohomology is

$$
H^0=\ker\vec\Upsilon_x=\mathbb{C}|0\rangle=\tilde\Pi_+S,\qquad
H^1=S/\mathrm{im}\,\vec\Upsilon_x\cong\mathbb{C}|1\rangle=\tilde\Pi_-S .
$$

The index is $1-1=0$. The content of the mode's square-zero is therefore not a cohomological quotient; it is the **splitting of the module into the two rungs**, which the anticommutator supplies. The two rungs are the vacuum and the occupied state, and the two cohomology spaces are represented by these two rungs. The mode is the case in which the square-zero is paired with the identity and the cohomology is balanced.

The same equality holds on the algebra by left multiplication: the kernel and the image of $L_{\vec\Upsilon_x}$ coincide; each is of complex dimension two and consists of the matrices with vanishing second row. The rung structure is therefore visible on the algebra as well, and the module statement is the one the physics uses.

### The Occupation Parity

The mode's grading is the inner automorphism by

$$
(-1)^F=e_t-2\tilde\Pi_-=i\vec e_z,
$$

which is Hermitian, squares to $e_t$, and satisfies

$$
(-1)^F\vec\Upsilon_x(-1)^F=-\vec\Upsilon_x,\qquad
(-1)^F\vec\Upsilon_y(-1)^F=-\vec\Upsilon_y .
$$

Its eigenspaces are

$$
\mathbb{B}_0=\mathbb{C}\{e_t,i\vec e_z\}=\mathbb{C}\{e_t,\tilde\Pi_-\},\qquad
\mathbb{B}_1=\mathbb{C}\{\vec\Upsilon_x,\vec\Upsilon_y\},
$$

and

$$
\mathbb{B}=\mathbb{B}_0\oplus\mathbb{B}_1,\qquad
\mathbb{B}_i\mathbb{B}_j\subseteq\mathbb{B}_{i+j}.
$$

This is a genuine $\mathbb{Z}/2$ grading of $\mathbb{B}$ as an associative algebra, and it is the grading the Fock-space article calls the parity grading. It is **not** the Clifford parity. The Clifford algebra $\mathrm{Cl}_{1,3}$ is graded by the degree of its monomials, $\mathrm{Cl}_{1,3}=\mathrm{Cl}^0\oplus\mathrm{Cl}^1$, and $\mathbb{B}=\mathrm{Cl}^0$; every element of $\mathbb{B}$ is Clifford-even. The odd part $\mathrm{Cl}^1=\mathbb{B}\gamma$ is a rank-one module over $\mathbb{B}$, not a second copy of the algebra. The ladder is therefore **even in the Clifford grading and odd in the occupation grading**. The word "fermionic" names the second, not the first.

The distinction is not a pedantic one. It is the reason the one-mode algebra can be an algebra of fermionic modes while every one of its elements is a bosonic (Clifford-even) element of the ambient algebra. The mode's fermionic character is carried by the inner automorphism, not by the degree. The differential below and the supercharge's odd extension are the cases in which the fermionic character must be carried by an outer grading instead.

### The Mode in a Field

Second quantization is the passage from the one-mode algebra to the many-mode tensor product, and the mode is its elementary unit. In a many-body field theory the labels are supplied by the mode: $a^\dagger_{p,s}$ creates a fermion with momentum $p$ and spin $s$, $a_{p,s}$ annihilates it, $b^\dagger_{p,s}$ creates the corresponding antifermion, and $b_{p,s}$ annihilates it. The algebra supplies the occupation quantum and the exclusion; the field supplies the quantum numbers. The many-mode algebra is $M_{2^m}(\mathbb{C})$, which is outside $\mathbb{B}$ for $m\ge2$; the tensor product is the extra input.

The same mode is the native qubit: the two rungs are the two computational states, and the ladder is the native gate. The matchgate and fermionic-linear-optics circuits are the multi-mode extension, with the tensor product assumed. The qubit is not a separate object from the mode; it is the mode read as a two-state system.

### What the Mode Does Not Supply

The mode supplies the occupation quantum, the two rungs, the exclusion principle and the native qubit. It does not supply a field, a Hamiltonian, a mass, a charge, a coupling, or a lattice. A field is a collection of many modes; the algebra has room for one, because $m$ modes generate $M_{2^m}(\mathbb{C})$, of dimension $4^m$, which exceeds four for $m\ge2$, and no nilpotent of $\mathbb{B}$ has index above two. The mode's square-zero is the algebraic form of "at most one," and that is the whole of its physical content at the level of the algebra.

## The Differential

### The BRST Complex

A differential is an odd operator $Q$ on a graded complex with $Q^2=0$. The BRST complex of a gauge theory is the corpus's principal example. The gauge field, the ghost $c$, the antighost $\bar c$ and the Nakanishi–Lautrup field $B$ carry ghost numbers $0,1,-1,0$, and the BRST transformation is

$$
sA_\mu^a=-D_\mu c^a,\qquad
sc^a=-\tfrac{g}{2}f^{abc}c^bc^c,\qquad
s\bar c^a=B^a,\qquad
sB^a=0 .
$$

The nilpotency $s^2=0$ is the Jacobi identity of the gauge algebra in disguise. In the biquaternion framework the gauge algebra is realized by the commutator inside $\mathbb{B}$, and the Jacobi identity is a rearrangement of the associativity of the product; the nilpotency is therefore inherited from associativity rather than postulated. The ghosts themselves are not elements of $\mathbb{B}$: they are odd generators adjoined in the Grassmann envelope $\mathbb{B}\otimes\Lambda$, and the BRST charge is an operator on the resulting Fock space, not an element of the four-dimensional algebra.

The physical states are the ghost-number-zero cohomology,

$$
\mathcal{H}_{\mathrm{phys}}=\frac{\ker Q_{\mathrm{BRST}}}{\mathrm{im}\,Q_{\mathrm{BRST}}}\Big|_{\mathrm{gh}=0},
$$

and the unphysical content forms the Kugo–Ojima quartet: the timelike and longitudinal components of the gauge field together with the ghost pair, four states in two zero-norm pairs, removed by the cohomology. The physical subspace is two-dimensional at each momentum, the two transverse polarizations.

### The Role of the Differential

The differential is the case in which the square-zero is paired with nothing. There is no adjoint partner whose anticommutator with $Q$ is the identity or a positive Hamiltonian that contracts the complex; the cohomology is not the kernel of a Hodge Laplacian, and it is not balanced by construction. The content is the quotient $\ker Q/\mathrm{im}\,Q$, and the whole apparatus — the ghosts, the gauge fixing, the quartet — exists to make that quotient the physical state space.

Three consequences separate the differential from the mode.

- **It does not create a particle.** $Q$ shifts ghost number by one; it maps a state to a state of different ghost number, and it changes no particle number. The ghost is not a physical particle; it is a fermionic coordinate whose rung is removed by the cohomology. The BRST charge is a derivation of the field algebra and an operator on the Fock space, not a ladder.
- **It has no vacuum idempotent.** The mode's vacuum is the idempotent $\tilde\Pi_+$; the differential's "vacuum" is the ghost vacuum, but the physical content is not a rung. The cohomology is a quotient, not an image.
- **It does not pair with an identity.** The mode's anticommutator is $e_t$; the differential has no such pairing. The unphysical part of the complex is contractible — the quartet is removed — but the physical part is not, and that is the point.

The ghost is the object that shows why the algebra alone is not enough. Algebraically, the ghost oscillator has a canonical anticommutator, $\{c,\partial_c\}=1$, and therefore looks like a mode. Physically, it is removed by the cohomology: its rung is not a state. The mode's algebra and the mode's physics are not the same thing, and the differential is the structure that separates them.

## The Supercharge

### The Algebra

The supersymmetry algebra of a quantum-mechanical model is generated by an odd charge $Q$ and its adjoint, with

$$
Q^2=(Q^\dagger)^2=0,\qquad
\{Q,Q^\dagger\}=H .
$$

The Hermitian combination $\mathcal{D}=Q+Q^\dagger$ satisfies $\mathcal{D}^2=H$, and the Hamiltonian is the square of the Hermitian part. The harmonic zero modes of $Q$, the states annihilated by both $Q$ and $Q^\dagger$, are the states annihilated by $H$; the partner Hamiltonians $H_+=A^\dagger A$ and $H_-=AA^\dagger$ have the same spectrum except at zero energy; and the Witten index

$$
\Delta=\mathrm{Tr}\,(-1)^F=\dim\ker H_+-\dim\ker H_-
$$

is the graded dimension of the zero-mode space. The index is invariant under continuous deformations, which is why it is a topological quantity.

The normalization is a convention. The corpus writes $\{Q,Q^\dagger\}=H$; the standard supersymmetry literature often writes $\{Q,Q^\dagger\}=2H$. The factor of two changes no physics, but it must be kept fixed when comparing formulas. What matters for the taxonomy is not the factor but the fact that the right-hand side is an **operator**, not the identity.

### The Biquaternion Realization

In the biquaternion framework the Dirac operator is the gradient

$$
\tilde\nabla=e_t\partial/\partial Q_t+\vec e_x\partial/\partial Q_x+\vec e_y\partial/\partial Q_y+\vec e_z\partial/\partial Q_z,
$$

with $\tilde\nabla\tilde\nabla^{\natural}=\tilde\nabla^{\natural}\tilde\nabla=\Box$, the central d'Alembertian. The first-order pair $(\tilde\nabla,\tilde\nabla^{\natural})$ is the supercharge pair, the grading is chirality, and the mass pair

$$
\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L,\qquad
\tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R
$$

is the off-diagonal term that the superalgebra reads as the superpotential. In block form,

$$
\mathcal{D}=\begin{pmatrix}0&\tilde\nabla^{\natural}\\ \tilde\nabla&0\end{pmatrix},
\qquad
\mathcal{D}^2=\Box\,I .
$$

The free theory has $H_+=H_-=\Box$; a position-dependent mass $m\to W(x)$ splits the partners, and the superpotential is the mass. The 1+1-dimensional reduction reproduces the standard partner potentials $V_\pm=W^2\mp dW/dx$, and the Witten index is the chirality imbalance of the Dirac zero modes.

Two senses of "supercharge" are in play in the corpus. The SUSY article calls the first-order gradient $\tilde\nabla$ a supercharge: it is an element of $\mathbb{B}$, it is even in the Clifford grading, and its product with its adjoint is the scalar $\Box$. The superalgebra article calls the odd generator $Q$ a supercharge: it is not an element of $\mathbb{B}$, its graded square is the Hamiltonian, and its anticommutator with itself is $2H$. The two are related by the block decomposition $\mathcal{D}=Q+Q^\dagger$: the Hermitian combination is the Dirac operator, and the odd $Q$ is its off-diagonal block.

The taxonomy uses the second sense, because it is the one in which the square-zero is an odd element. In the biquaternion realization the odd supercharge is the off-diagonal block of $\mathcal{D}$ acting on the graded module, and in the ambient graded algebra it is an element of $\mathrm{Cl}^1=\mathbb{B}\gamma$. The superalgebra-reading article states the point in the sharpest form: a supercharge is an odd element with $\{Q,Q\}=2H$, and it is therefore never an element of the four-dimensional algebra. The odd slot is a rank-one module over $\mathbb{B}$, not a second algebra.

### The Role of the Supercharge

The supercharge is the case in which the square-zero is paired with the Hamiltonian. Three consequences follow.

- **The cohomology is the zero-mode space.** For $H$ positive semidefinite and the complex elliptic, $\ker Q=\ker H\oplus\mathrm{im}\,Q$, so $\ker Q/\mathrm{im}\,Q\cong\ker H$. The cohomology is the space of zero modes, and the index is its graded dimension. The supercharge's content is not the whole spectrum but the part of it that the grading protects.
- **The splitting is by the Hamiltonian.** The mode's anticommutator is the identity and splits the identity into two rungs; the supercharge's anticommutator is $H$, and the splitting is by the spectral projectors of $H$; the zero modes are the corner that survives.
- **The grading is chirality.** The supercharge is odd under $\gamma_5$; the mode is odd under $(-1)^F=i\vec e_z$. In the one-mode truncation the two gradings can be represented by the same element, but they act on different spaces and have different physical meanings. The coincidence of the element is not a coincidence of the role.

## The Label

### The Grassmann Algebra

The Grassmann algebra $\Lambda$ is generated by odd labels $\theta_i$ with

$$
\theta_i\theta_j=-\theta_j\theta_i,\qquad
\theta_i^2=0 .
$$

Its elements multiply; they do not act on a Hilbert space. Berezin integration is the linear functional fixed by

$$
\int d\theta\,\theta=1,\qquad
\int d\theta\,1=0,
$$

and the fermionic coherent states, the path-integral measure and the fermionic Wick theorem are built from it. In the framework the envelope is $\mathbb{B}\otimes\Lambda$; the Grassmann labels are adjoined, not native.

### The Label Is Not a Mode

The label and the mode are different objects, and the difference is the same one the whole article is about.

- **The mode acts.** $\vec\Upsilon_x$ maps the occupied rung to the vacuum and annihilates the vacuum; it has a kernel, an image and a cohomology.
- **The label multiplies.** $\theta$ multiplies a function of the even variables; it has no state space, no vacuum and no cohomology. Its square-zero truncates the Taylor expansion; it does not annihilate a state.
- **The label is the coefficient of a mode, not the mode.** The coherent state $|\theta\rangle=\exp(\theta a^\dagger)|0\rangle$ uses $\theta$ as a label and $a^\dagger$ as the operator. The label carries the sign of the statistics; the operator carries the occupation.

The structural reason the full Grassmann algebra is not inside $\mathbb{B}$ is worth stating. A single Grassmann generator is a nilpotent of $\mathbb{B}$ — $\sigma_+$ is one — but two independent generators with a nonzero product are not. In $M_2(\mathbb{C})$ every nonzero nilpotent has rank one, and a rank-one nilpotent has image equal to its kernel. Two such nilpotents with both products nonzero cannot anticommute: if $N_1N_2\ne0$ and $N_2N_1\ne0$, the two products are proportional, so their one-dimensional images agree, and then one of the products vanishes. The Grassmann algebra on two generators therefore has no faithful representation in $\mathbb{B}$, and the envelope must be adjoined. This is the algebraic form of the statement that the odd coordinates are not elements of the algebra.

The naturality of the envelope is an open question of the corpus, not a result. The BRST article asks for a $\mathbb{Z}_2$-graded extension of $\mathbb{B}$ in which the BRST doublet is an element rather than an adjunction; the Grassmann article asks whether the odd extension is canonical. This article records the question and does not answer it.

## The Corner

A Dirac symbol in chiral form has the block structure

$$
H(k)=\begin{pmatrix}0&h(k)\\ h^\dagger(k)&0\end{pmatrix},
$$

with $h(k)$ the chiral block. At a node $k_0$ the block vanishes, and near it $h(k_0+\delta k)\approx\boldsymbol\sigma\cdot\delta k$. The local ladder is the nilpotent Pauli pair $\sigma_\pm=\tfrac12(\sigma_x\pm i\sigma_y)$, with $\sigma_\pm^2=0$ and $\{\sigma_+,\sigma_-\}=I$. The corner differs from the mode in three ways: the nilpotent is a block on an internal space rather than an element acting on the defining module; the square-zero is a local statement about the symbol and not a dynamics; and the node is a zero of the symbol, not a nilpotent momentum. The graphene and Nielsen–Ninomiya interpretations are §*The Nine Interpretations*; the taxonomy uses the corner only as the case of a local ladder with no cohomology.

## The Excluded Case: The Physical Null Momentum

The object most often confused with the nilpotent is the physical null four-momentum. Write $\tilde P=iP_t e_t+\vec p$ with $P_t^2=\vec p^{\,2}$. Its quaternionic norm vanishes, $\langle\tilde P\rangle_{\natural}=0$, so it lies on the zero-divisor cone; its square does not vanish, $\tilde P^2=2iP_t\tilde P$, and its trace does not vanish, $\mathrm{Tr}\,\tilde P=2iP_t$. It is therefore a nonzero multiple of a rank-one idempotent, not a nilpotent. The nilpotent is pure, traceless and similar to $\begin{pmatrix}0&1\\0&0\end{pmatrix}$; the null momentum is similar to a nonzero multiple of $\begin{pmatrix}1&0\\0&0\end{pmatrix}$. The trace, or equivalently the scalar part, separates the two.

The cone and the norms are §*The Nilpotent Cone*; the photon interpretation is that of *The Zero-Divisor Cone and the Massless Spectrum*. The taxonomy uses the distinction only as its negative boundary: the equation $X^2=0$ selects the nilpotent, and the cone alone does not.

## The Nine Interpretations

The nine interpretations below place the object in a mode, a lattice null point, a limit, or a boundary case where the identification fails. Each names the structure it uses and the boundary it does not cross; the taxonomy of the preceding sections is the frame that keeps them apart.

### Dirac's Hole Is Not a Nilpotent

Hole theory fills the negative-energy sea and reads a missing occupation as a hole. The hole is a **difference** from the sea: it carries the quantum numbers that make it an antiparticle of the missing state, and it disappears when the state is refilled. The nilpotent is not that difference. It is the mode operator itself, the object whose square is zero and whose repeated application is impossible.

The modern interpretation makes the distinction sharper. The vacuum is empty, the negative-frequency modes create antiparticles, and no sea is needed. The nilpotent remains the mode; the antiparticle is a state created by the mode, not a square-zero element. The algebra supplies the anticommutation of the modes, $\{\vec\Upsilon_x,\vec\Upsilon_y\}=e_t$ with $\vec\Upsilon_x^2=\vec\Upsilon_y^2=0$, and the exclusion principle is its square-zero consequence. The hole, if one keeps the language, is a relational object: a missing rung, not a nilpotent.

**Boundary.** The interpretation does not adjudicate between hole theory and the modern one. It says which algebraic object carries which role. The hole has no square-zero representative in $\mathbb{B}$; the nilpotent has no charge label by itself. A reader who identifies the two will look for a nilpotent with the quantum numbers of a positron and will not find one.

### Jordan–Wigner Is a Choice of Square Root

The one-site spin ladder is already fermionic. The raising and lowering operators of a spin one half are nilpotent, and their anticommutator is the identity. The Jordan–Wigner transformation is the choice of that square root and its extension along a chain. At one site the spin algebra and the fermion algebra are the same algebra, and the map is a relabelling of its generators; the nonlocal string appears only when a second site is added, and it is the branch cut that keeps the square root consistent across the chain.

The algebraic content is therefore one sentence: nilpotency is a one-site fact, and the string is the price of a consistent global choice of square root.

**Boundary.** Jordan–Wigner is an equivalence of algebras on a chain, not a derivation of fermions from spins. The string is a nonlocal rewriting; it changes the locality of the operators, not the spectrum. The algebra supplies the one-site nilpotent, not the chain.

### Grassmann Coherent States Are the Minimal Odd Extension

A fermionic coherent state is written with a Grassmann label $\theta$,

$$
|\theta\rangle_{*}=|0\rangle+\theta|1\rangle,
\qquad
\theta^2=0 .
$$

The label is odd, and the algebra $\mathbb{B}$ is even. The Grassmann algebra generated by one odd variable per mode is a minimal extension in which the fermionic grading can be written. The states of the original algebra are even; the odd label is a coordinate on the coherent-state manifold, not a state.

**Boundary.** The odd generator is not an element of $\mathbb{B}$. The extension $\mathbb{B}\otimes\Lambda$ is not unique, and the Berezin integral is an extra structure on it. The algebra supplies the even carrier; the odd label is the minimal addition that makes the grading writable.

### The WKB Phase Gradient Avoids the Cone

In the semiclassical approximation the leading-order momentum is the phase gradient, the real quaternion

$$
\nabla S=\sum_\mu\frac{\partial S}{\partial Q_\mu}\vec e_\mu .
$$

The Hamilton–Jacobi equation fixes its norm to the energy defect,

$$
\boxed{\;\langle\nabla S\rangle_{\natural}=2m(E-V)\;}.
$$

In the classically allowed region this is positive, and the gradient is never a nonzero nilpotent. The cone $\langle\nabla S\rangle_{\natural}=0$ is reached only where $\nabla S=0$, at a turning point: the gradient vanishes, and the origin is not a nilpotent either. A material four-momentum is a different object, since it carries the energy as its imaginary scalar part; its mass shell is not the level set of the phase gradient.

**Boundary.** The statement is about the leading order. Caustics, tunneling and backreaction are outside it. The gradient is not the wavefunction, and the WKB approximation is not exact. The algebra says where the leading-order momentum can live; it does not say that the exact solution stays there.

### The Dirac Point of Graphene Is a Null Momentum

The effective Hamiltonian of graphene near a Dirac point is linear in the momentum, $H=v_F(k_x\sigma_x+k_y\sigma_y)$, and its square is quadratic, $H^2=v_F^2|\vec k|^2I$. The linear branch is the square root of the quadratic symbol. The Dirac point is the apex of the cone, and the gapless excitations around it lie on the null cone $\langle\tilde P\rangle_{\natural}=0$.

In the biquaternion interpretation the physical branch is the **zero-divisor cone**: a null four-momentum is a zero divisor, and the node is its apex. The nilpotent appears in the **chiral block** of the symbol, where the raising and lowering combinations of the Pauli matrices are square-zero; it is the algebraic corner of the branch, not the four-momentum of a particle on it. The Dirac point itself is where the momentum vanishes, and the origin is not a nilpotent.

**Boundary.** The lattice model, the two valleys and the topological protection are input. The algebra supplies the form of the linear branch and the null cone; it does not derive the band structure of graphene. The physical branch is the zero-divisor cone, not the nilpotent cone; the phrase "nilpotent corner" names the algebraic form of the chiral block, not a particle with a nonzero momentum.

### Nielsen–Ninomiya Is a Pairing of Lattice Null Points

On a periodic lattice the zeros of the Bloch symbol are counted by topology. The signed count is the degree of the symbol on the boundary of the Brillouin zone; on a torus the boundary is empty, so the count vanishes and the zeros come in pairs of opposite chirality. A single null point cannot be removed by a local deformation. The nilpotent is the local square-zero corner, and the pairing is the global statement that the corners cannot be unpaired.

**Boundary.** The theorem assumes a local, periodic, finite-range Hamiltonian with a Hermitian symbol. It is a no-go statement, not a construction. The algebra sees the local null symbol; the signed count is a property of the band bundle over the Brillouin zone, not of the algebra alone. A lattice with defects or a boundary can evade the pairing, and the theorem says nothing about that case.

### The Fermionic Wick Theorem Is Exact

For a single nilpotent mode, a product that contains a repeated mode vanishes, because the repeated pair squares to zero. The only nonzero contractions are the two-point ones, and the graph expansion terminates. This is why the fermionic Wick theorem is an exact operator identity for the mode and not an approximation: there is no infinite series of higher contractions to resum.

**Boundary.** The statement is per mode. For a fermionic field the standard Grassmann Wick theorem is exact, but its exactness is a property of the Grassmann algebra, not of $\mathbb{B}$ alone; the single mode is the smallest instance. The algebra's nilpotency supplies the mode, not the Gaussian state or the measure. The theorem is not a substitute for the path integral, and it does not by itself define the vacuum.

### The Ladder Is Capped at Two Rungs

A nilpotent raising operator climbs one step and stops. A complete family of orthogonal idempotents in $\mathbb{B}$ has at most two members, as the pair $\tilde\Pi_\pm$ shows, and no three-level module exists in $\mathbb{B}$. The qutrit is outside the algebra. The cap is the $2\times2$ matrix model: a complex module has dimension two, and three mutually orthogonal rank-one idempotents cannot fit.

**Boundary.** The cap is on the native module, not on composite systems. Two qubits give four levels, and a qutrit can be embedded in $M_3(\mathbb{C})$, but not in $\mathbb{B}$. The algebra says that its own ladder has two rungs; it does not say that nature has only two levels.

### Squeezing Is a Contraction to the Cone

A contraction of the algebra rescales the structure constants and the norm together. In the corpus's example the bracket and the norm degenerate as

$$
[E_2,E_3]=2\epsilon^2E_1,
\qquad
\langle E_2\rangle_{\natural}=\epsilon^2e_t,
$$

so that at $\epsilon=0$ the elements $E_2$ and $E_3$ are nilpotent and mutually annihilating, the bracket $[E_2,E_3]$ vanishes while $[E_1,E_2]$ and $[E_1,E_3]$ survive, and the basis elements that were invertible are zero divisors. The cone is the limiting locus of the degeneration.

**Boundary.** A contraction is a limit of algebras, not a physical squeezing process. At $\epsilon>0$ the family is a rescaled basis of $\mathbb{B}$; at $\epsilon=0$ the limit algebra is not $\mathbb{B}$, and the cone is a boundary of the family, not a dynamics. No state is squeezed by the algebra; the interpretation explains why the cone is the endpoint, not how a physical system reaches it.

## The Two Gradings

The word "grading" is used in the corpus for several structures, and the taxonomy depends on keeping them apart. The table collects them.

| grading | where it lives | operator | odd part | type |
|---|---|---|---|---|
| Clifford parity | $\mathrm{Cl}_{1,3}=\mathrm{Cl}^0\oplus\mathrm{Cl}^1$ | degree | $\mathrm{Cl}^1=\mathbb{B}\gamma$ | algebra, $\mathbb{Z}/2$; trivial on $\mathbb{B}$ |
| occupation parity | $\mathbb{B}$ | $(-1)^F=i\vec e_z$ | $\mathbb{C}\{\vec\Upsilon_x,\vec\Upsilon_y\}$ | algebra, $\mathbb{Z}/2$, inner |
| chirality | Dirac module | $\gamma_5$ | off-diagonal chiral blocks | module, $\mathbb{Z}/2$ |
| ghost number | $\mathbb{B}\otimes\Lambda$ | $N_{\mathrm{gh}}$ | $Q_{\mathrm{BRST}}$ has degree $+1$ | algebra, $\mathbb{Z}$ |
| number | Fock space | $N$ | — | state space, $\mathbb{N}$ |
| sector splitting | $\mathbb{B}$ | $*$ | — | not a grading |

Three entries deserve comment.

**The Clifford parity is trivial on $\mathbb{B}$.** Every element of $\mathbb{B}=\mathrm{Cl}^0_{1,3}$ is even. The odd part is outside the algebra, a rank-one module $\mathbb{B}\gamma$. This is why an odd supercharge is never an element of $\mathbb{B}$ and why the fermionic mode is not an odd element of the Clifford algebra.

**The occupation parity is inner and nontrivial.** $(-1)^F=i\vec e_z$ is an element of $\mathbb{B}$, and conjugation by it splits $\mathbb{B}$ into the two-dimensional even part $\mathbb{C}\{e_t,i\vec e_z\}$ and the two-dimensional odd part $\mathbb{C}\{\vec\Upsilon_x,\vec\Upsilon_y\}$. This is a genuine $\mathbb{Z}/2$ grading, and it is the one the mode uses. It is not the Clifford parity.

**The sector splitting is not an algebra grading.** $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ is the $\pm1$ eigenspace splitting of the Hermitian conjugation, and the product of two Hermitian elements need not be Hermitian. It grades the symmetrized product and not the associative one. It must not be used as if it were the fermionic parity.

The table of the two $\mathbb{Z}/2$'s of $\mathbb{B}$ is therefore short. The Clifford parity has no odd elements in $\mathbb{B}$; the occupation parity has the ladder as its odd part. An element of $\mathbb{B}$ can be even in both ($e_t$, $\tilde\Pi_\pm$), or even in the Clifford parity and odd in the occupation parity (the ladder). The other two combinations are empty, because there is no Clifford-odd element in $\mathbb{B}$.

| | Clifford even | Clifford odd |
|---|---|---|
| occupation even | $e_t$, $i\vec e_z$, $\tilde\Pi_\pm$ | — |
| occupation odd | $\vec\Upsilon_x$, $\vec\Upsilon_y$ | — |

"Fermionic" is therefore not a property of an element of $\mathbb{B}$ in the Clifford sense. It is a property relative to the occupation grading, and it is carried by the inner automorphism. The field-theoretic fermion parity acts on the many-body Fock space; the one-mode truncation realizes its single-mode shadow as $i\vec e_z$, and that is the content of the Fock-space article's statement that the grading is an element of the algebra for one mode.

## The Taxonomy in One Table

| role | what $X$ is | acts on | odd under | paired with | what the cohomology is |
|---|---|---|---|---|---|
| mode | element of $\mathbb{B}$ | defining module $S$ | occupation parity | $\{X,X^*\}=e_t$ | the two rungs, balanced |
| differential | odd derivation / operator | graded complex | ghost number | nothing | the physical quotient |
| supercharge | odd operator | graded Hilbert space | chirality | $\{Q,Q^\dagger\}=H$ | the zero-mode space |
| label | odd coordinate | — (multiplies) | exterior degree | — | none |
| corner | local block of a symbol | internal space at a node | chiral / sublattice | — | none |
| null momentum | zero divisor with $X^2\ne0$ | — | — | — | none; not a nilpotent |

The table is the article's answer to the question with which it began. The first three rows are the principal roles; the last three are the boundary objects. The mode is the only one whose data are complete inside the four-dimensional algebra. The differential needs a complex and a grading; the supercharge needs an odd extension; the label needs an envelope; the corner needs a symbol and a parameter space; the null momentum is not a nilpotent at all.

The table also explains why the same equation appears five times without the five being the same. $X^2=0$ is the simplest way to have a two-term complex and a two-rung module. The physics chooses which of the two structures to read, and the choice is not in the equation.

## The Interpretations in One Table

The nine interpretations share one algebraic object and divide its roles. The table states the division.

| interpretation | the object it uses | what the algebra supplies | what it does not supply |
| --- | --- | --- | --- |
| Dirac's hole | nilpotent mode against the vacuum | exclusion as square-zero composition | the sea, the hole's quantum numbers |
| Jordan–Wigner | one-site nilpotent | the local square root | the chain and the string |
| Grassmann coherent states | odd label $\theta$ | the even carrier to be extended | the odd generator, the Berezin integral |
| WKB | phase gradient | the energy defect as a norm | the approximation, the caustics |
| graphene | null momentum | the linear branch as a square root | the lattice and the valleys |
| Nielsen–Ninomiya | null points of the symbol | the local square-zero corner | the global index and its pairing |
| Wick theorem | one nilpotent mode | termination of the expansion | the Gaussian state |
| qutrit | two-rung ladder | the cap at two idempotents | composite level counting |
| squeezing | contraction parameter | the cone as a limit | the physical process |

## What the Classification Buys

**Three errors it prevents.**

1. *Every nilpotent is a fermion.* False. The BRST charge is a differential, the Grassmann label is a coordinate, the chiral corner is a block, and the null momentum is not a nilpotent. The mode requires a module, a vacuum, a rung pair and a canonical anticommutator.
2. *The BRST charge creates a fermion.* False. It shifts ghost number; it does not change particle number. The ghost is removed by the cohomology, and its rung is not a physical state.
3. *The photon is a nilpotent.* False. The null momentum is a zero divisor with a nonzero square and a nonzero trace; it is a multiple of an idempotent, not a square-zero element.

**Three facts it explains.**

- *Why $\mathbb{B}$ hosts one mode and no field.* The mode is the only role whose data are the algebra and its defining module, with no further structure. Every other role needs something the algebra does not carry: a complex, an odd generator, an envelope, or a parameter space.
- *Why the normalization matters.* The mode's anticommutator is the identity and the supercharge's is the Hamiltonian. The same algebra with a different right-hand side has a different cohomology: the mode's is the rung pair, the supercharge's is the zero-mode space, and the differential's is the physical quotient.
- *Why the cohomology is the content in one case and the splitting in another.* The mode's square-zero is balanced by the identity; the differential's is not balanced at all; the supercharge's is governed by the Hamiltonian. The index — the graded dimension of the cohomology — is zero for the mode, the Witten index for the supercharge, and the ghost-number Euler characteristic for the differential.

**Four questions it leaves open.**

- *The Grassmann envelope.* Is there a natural $\mathbb{Z}_2$-graded extension of $\mathbb{B}$ in which the BRST doublet and the odd coordinates are elements rather than adjunctions?
- *The BRST charge as an algebraic object.* Is there a finite-dimensional object built from $\mathbb{B}$ — a derivation, a supertrace, a cocycle — that computes the cohomology without passing through the mode algebra?
- *The supercharge as an element.* Is there a natural odd extension of $\mathbb{B}$ in which the supercharge is an element, rather than an off-diagonal block of an operator on a module?
- *The many-mode structure.* Is the tensor product $\mathbb{B}^{\otimes N}$ natural in the framework, or is it an extra input? The dimension count says that the algebra itself stops at one mode; the field theory needs the tensor product, and the tensor product is assumed rather than derived.

The first three are the open questions of the BRST and superalgebra articles; the fourth is the open question of the Fock-space article. This article does not answer them. It states where they sit in the classification.

## Limits

The article is a taxonomy, not a derivation. It does not derive the BRST transformation, the supersymmetry algebra or the fermionic statistics from the biquaternion algebra; it states where each structure lives and what each square-zero element does. The mode's identification with a physical fermion remains a realization, not a derivation, and the dimension count $4=4$ remains a coincidence of dimensions until something more is said.

The taxonomy covers the corpus's uses of $X^2=0$; it does not claim to exhaust the mathematical uses of square-zero elements. The de Rham differential, the boundary operator of a chain complex and the Koszul differential are further differentials; they fall under the differential row and add nothing to the classification beyond a further example. The article does not treat them.

The article adds no dynamics, no mass, no coupling and no empirical prediction. It gives the nilpotent, the ladder and the pairing, but no field content: a field is a collection of modes, and the qutrit is outside $\mathbb{B}$. The lattice interpretations are topological and model-dependent; the algebra is not a lattice. The WKB interpretation is leading order; the exact solution, the caustics and the tunneling lie outside it. The contraction is a limit, not a process. The physical interpretations it compares are the corpus's, and the comparison does not make them more or less empirical. The sharpest limit is the distinction of §*The Excluded Case: The Physical Null Momentum*: the physical null momentum is a zero divisor with a nonzero square, and the nilpotent is a pure displacement with a zero square.

## Summary

A nilpotent is a nonzero element with $X^2=0$. The equation is one, and the corpus's uses of it are five: the one-mode ladder of $\mathbb{B}$, the BRST differential, the supersymmetric supercharge, the Grassmann label and the chiral corner. A sixth object, the physical null momentum, is a zero divisor with a nonzero square and is not a nilpotent.

The classification is fixed by three questions. What does $X$ act on? A module, a complex, a Hilbert space, or nothing. Which grading is $X$ odd under? The occupation parity, the ghost number, the chirality, the exterior degree, or none. What is $X$ paired with? The identity, the Hamiltonian, nothing, or nothing at all.

The nilpotent itself is necessarily pure with an isotropic complex vector part: the nilpotent cone is of complex dimension two and real dimension four, inside the six-real-dimensional zero-divisor cone, and every nilpotent has index two. In the matrix model it is a nonzero trace-free singular matrix. The pure condition separates it from the other zero divisors, which are nonzero multiples of idempotents.

The mode is an element of $\mathbb{B}$ acting on the defining module, odd under the inner parity $(-1)^F=i\vec e_z$, and paired with its adjoint by $\{X,X^*\}=e_t$. Its two rungs represent the two cohomology spaces of the two-term complex, its index is zero, and its content is the splitting of the identity into $\tilde\Pi_+$ and $\tilde\Pi_-$. The algebra carries exactly one mode: $m$ modes generate $M_{2^m}(\mathbb{C})$, dimension $4^m$, which exceeds four for $m\ge2$; every nonzero nilpotent of $\mathbb{B}$ has index two, so no three-level ladder exists inside it.

The differential is an odd derivation of ghost number $+1$ on $\mathbb{B}\otimes\Lambda$, with $s^2=0$ inherited from associativity and the Jacobi identity. It has no vacuum idempotent and no such pairing; its content is the cohomology $\ker Q/\mathrm{im}\,Q$ at ghost number zero, and the unphysical content is the Kugo–Ojima quartet.

The supercharge is an odd operator on a graded Hilbert space, with $Q^2=0$ and $\{Q,Q^\dagger\}=H$. Its cohomology is the zero-mode space, its index is the Witten index, and its grading is chirality. In the framework it is the off-diagonal block of the Dirac operator $\mathcal{D}=Q+Q^\dagger$ with $\mathcal{D}^2=\Box$, and the odd supercharge is never an element of $\mathbb{B}$: the Clifford parity is trivial on $\mathbb{B}$, and the odd slot is the rank-one module $\mathrm{Cl}^1=\mathbb{B}\gamma$.

The Grassmann label multiplies rather than acts; it is an odd extension, adjoined in $\mathbb{B}\otimes\Lambda$, and two independent generators with a nonzero product have no faithful representation in $\mathbb{B}$. The chiral corner is the local ladder $\sigma_\pm$ of a chiral symbol at a node; the node is a null point of the symbol, not a nilpotent momentum.

The physical null momentum, $\tilde P=iP_t e_t+\vec p$ with $P_t^2=\vec p^{\,2}$, has $\langle\tilde P\rangle_{\natural}=0$ but $\tilde P^2=2iP_t\tilde P\ne0$ and trace $2iP_t\ne0$; it is a multiple of a rank-one idempotent. The trace separates it from the nilpotent.

The nine interpretations use the object as a mode, a lattice null point and a limit: the Dirac hole as a difference and not a nilpotent, Jordan–Wigner as a one-site square root with the string as its branch cut, the Grassmann coherent state as the minimal odd extension, the WKB phase gradient off the cone, the graphene Dirac point as a null momentum with the nilpotent as its chiral corner, Nielsen–Ninomiya as the topological pairing of lattice zeros, the exact one-mode Wick theorem, the two-rung cap that puts the qutrit outside the algebra, and squeezing as a contraction to the cone.

The two $\mathbb{Z}/2$ gradings in play are the Clifford parity, trivial on the algebra, and the occupation parity, the inner automorphism by $i\vec e_z$. The ladder is even in the first and odd in the second; "fermionic" names the second. The sector splitting $\mathbb{M}_+\oplus\mathbb{M}_-$ is not an algebra grading; the number grading lives on the Fock space; the chirality grading lives on the Dirac module.

The classification is a map, not a derivation. It adds no physics, and it leaves open the Grassmann envelope, the BRST charge as an algebraic object, the supercharge as an element, and the naturality of the tensor product.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}\cong M_2(\mathbb{C})$ | biquaternion algebra |
| $e_t=1$, $\vec e_x,\vec e_y,\vec e_z$ | quaternion basis, $\vec e_k^2=-e_t$ |
| $\mathbb{M}_\pm$ | Hermitian (informational) and anti-Hermitian (material) sectors |
| $\vec\Upsilon$ | a pure nilpotent, $\vec\Upsilon^2=0$, $\vec\Upsilon\neq0$ |
| $\tilde\Pi$ | an idempotent, $\tilde\Pi^2=\tilde\Pi$ |
| $\langle\tilde Q\rangle_{\natural}$ | the natural norm $\sum_\mu Q_\mu^2$ |
| $a,a^\dagger$ | the abstract one-mode annihilation and creation operators; $a=\vec\Upsilon_x$, $a^\dagger=\vec\Upsilon_y$ |
| $\vec\Upsilon_x,\vec\Upsilon_y$ | the canonical nilpotent pair, $\tfrac12(i\vec e_x-\vec e_y)$ and $\tfrac12(i\vec e_x+\vec e_y)$ |
| $\tilde\Pi_\pm$ | the two rungs, $\tfrac12(e_t\pm i\vec e_z)$ |
| $(-1)^F=i\vec e_z$ | occupation parity, an element of $\mathbb{B}$ |
| $X^2=0$ | the square-zero equation |
| $0\to M\xrightarrow{X}M\to0$ | the two-term complex of a nilpotent |
| $H^0=\ker X$, $H^1=M/\mathrm{im}\,X$ | its cohomology |
| $\mathrm{Cl}_{1,3}=\mathrm{Cl}^0\oplus\mathrm{Cl}^1$ | Clifford algebra and its degree grading |
| $\mathbb{B}=\mathrm{Cl}^0_{1,3}$ | the biquaternion algebra as the even part |
| $\mathrm{Cl}^1=\mathbb{B}\gamma$ | the odd slot, a rank-one module |
| $Q_{\mathrm{BRST}}$ | the BRST charge, an operator on the Fock space |
| $s$ | the BRST derivation, $s^2=0$ |
| $\Lambda$ | the Grassmann algebra of odd labels |
| $\theta_i$ | a Grassmann label, $\theta_i^2=0$ |
| $Q$, $Q^\dagger$ | the supersymmetric supercharge pair |
| $\mathcal{D}=Q+Q^\dagger$ | the Hermitian supercharge (the Dirac operator) |
| $H=\{Q,Q^\dagger\}$ | the supersymmetric Hamiltonian |
| $\gamma_5$ | chirality, the supersymmetric grading |
| $\tilde P=iP_t e_t+\vec p$ | the physical four-momentum |
| $\langle\tilde P\rangle_{\natural}$ | the quaternionic norm, the interval |
| $H(k)$, $h(k)$ | the chiral symbol and its block |
| $\sigma_\pm$ | the local Pauli ladder, $\sigma_\pm^2=0$ |

## Further Reading

- F. A. Berezin, *The Method of Second Quantization* (Academic Press, 1966), for the Grassmann algebra, Berezin integration and the fermionic coherent states.
- Marc Henneaux and Claudio Teitelboim, *Quantization of Gauge Systems* (Princeton University Press, 1992), for the BRST construction, the ghost-number grading and the cohomological characterization of the physical states.
- Edward Witten, "Dynamical breaking of supersymmetry," *Nuclear Physics B* **188** (1981) 513–554, for the supersymmetry algebra, the partner spectra and the Witten index.
- Julius Wess and Jonathan Bagger, *Supersymmetry and Supergravity* (Princeton University Press, 2nd ed. 1992), for the super-Poincaré algebra and the supercharge conventions.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the Clifford algebra, its even part and the degree grading.
- Alexander Altland and Ben Simons, *Condensed Matter Field Theory* (Cambridge University Press, 2nd ed. 2010), for the two-band models, the Dirac points and the Nielsen–Ninomiya pairing.
- Mikio Nakahara, *Geometry, Topology and Physics* (IOP, 2nd ed. 2003), for the de Rham and Koszul differentials and the cohomological reading of square-zero operators.
- Steven Weinberg, *The Quantum Theory of Fields*, Vol. II (Cambridge University Press, 1996), for the BRST quantization of gauge theories and the physical-state cohomology.
- Companion articles: [The Zero-Divisor Cone and the Massless Spectrum](the-zero-divisor-cone-and-the-massless-spectrum.html); [The Light Cone as the Biquaternion Zero-Divisor Cone](the-light-cone-as-the-biquaternion-zero-divisor-cone.html); [The Physical Interpretation of the 12 Products](the-physical-interpretation-of-the-12-products.html); [Roots, Idempotents and Observables](roots-idempotents-and-observables.html); [Roots, Idempotents and Quantum Information](roots-idempotents-and-quantum-information.html); [Spin and the Two State Spaces](spin-and-the-two-state-spaces.html); [Fock Space and Creation/Annihilation Operators in Biquaternionic Form](fock-space-and-creation-annihilation-operators-in-biquaternionic-form.html); [The Biquaternion Vacuum as a Minimal Idempotent](the-biquaternion-vacuum-as-a-minimal-idempotent.html); [The Dirac Sea, Hole Theory and Antimatter in Biquaternionic Form](the-dirac-sea-hole-theory-and-antimatter-in-biquaternionic-form.html); [The Jordan–Wigner Transformation in Biquaternionic Form](the-jordan-wigner-transformation-in-biquaternionic-form.html); [Grassmann Coherent States in Biquaternionic Form](grassmann-coherent-states-in-biquaternionic-form.html); [The WKB Approximation and the Hamilton–Jacobi Equation in Biquaternionic Form](the-wkb-approximation-and-the-hamilton-jacobi-equation-in-biquaternionic-form.html); [Dirac Matter: Graphene, Dirac Cones and Topological Insulators in Biquaternionic Form](dirac-matter-graphene-dirac-cones-and-topological-insulators-in-biquaternionic-form.html); [Fermion Doubling and the Nielsen–Ninomiya Theorem in Biquaternionic Form](fermion-doubling-and-the-nielsen-ninomiya-theorem-in-biquaternionic-form.html); [The Wick Theorem in Biquaternionic Form](the-wick-theorem-in-biquaternionic-form.html); [The Qutrit Problem: Three-Level Systems Outside the Biquaternion Algebra](the-qutrit-problem-three-level-systems-outside-the-biquaternion-algebra.html); [Squeezing Beyond the Biquaternion Algebra](squeezing-beyond-the-biquaternion-algebra.html); [BRST Symmetry in Biquaternionic Form](brst-symmetry-in-biquaternionic-form.html); [Supersymmetric Quantum Physics in the Biquaternion Framework](supersymmetric-quantum-physics-in-the-biquaternion-framework.html).
