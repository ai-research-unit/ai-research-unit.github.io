# __The Spin–Charge Hilbert Space and the SU(3) Supermultiplets in Biquaternionic Form__

## Introduction

The framework carries the Lorentz group and its spinor module, and its gauge-principle article reaches the compact group $\mathrm{SU}(2)$ inside the material sector. It does not carry $\mathrm{SU}(3)$: the companion *The Gauge Group Ceiling* shows that the algebra's own compact structure stops at $\mathrm{SU}(2)$, and *The Gluon: An Octet Outside the Biquaternion Algebra* states the cost of embedding beyond it. Yet the Standard Model's particle content is organised by $\mathrm{SU}(3)$ and $\mathrm{SU}(2)$ multiplets, and the spinor-structure programme supplies a way to write that content as vectors of a single Hilbert space built from **spin multiplets** and **charge multiplets**. It is worth recording because it is the bridge the programme builds between the spinor structure and the particle classification, and because it makes explicit which parts of the classification the framework can host and which it can only transcribe.

The construction is the following. Wigner's definition makes an elementary particle an irreducible unitary representation of the Poincaré group, acting in an abstract Hilbert space $\mathcal{H}_\infty$. Pauli's doubling of the wave function — the physics of spin — replaces $\mathcal{H}_\infty$ by $\mathcal{H}_S^{2s+1}\otimes\mathcal{H}_\infty$, the tensor product of a finite-dimensional **spin space** with the infinite-dimensional one. Heisenberg's proton–neutron doubling, and Kemmer's three-charge generalisation, replace it by $\mathcal{H}_Q\otimes\mathcal{H}_\infty$ with a finite-dimensional **charge space**. The two doublings combine into

$$
\mathcal{H}_S\otimes\mathcal{H}_Q\otimes\mathcal{H}_\infty,
$$

and a state vector of this space is a list of the representation labelling the particle in each factor. On this space the internal symmetry groups $\mathrm{SU}(2),\mathrm{SU}(3),\dots$ act by a central extension, and the supermultiplets of the eightfold way are the orbits.

The article is organised as follows. A first section recalls the abstract Hilbert space and its convergence condition. A second builds the spin multiplets and a third the charge multiplets. A fourth assembles the spin–charge space and reads a state vector. A fifth records the superselection rules, and a sixth the ray representation and the central extension that carries the internal symmetry. A closing section separates what the framework hosts from what it transcribes.

**Conventions.** The Lorentz conventions are the corpus's: $\mathrm{Spin}^{+}(1,3)\cong\mathrm{SL}(2,\mathbb{C})$, representations $\tau^{l\dot l}$ with $l,\dot l\in\frac12\mathbb{Z}_{\ge0}$ and spin $s=|l-\dot l|$. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong\mathbb{C}\mathrm{l}_2$, its Clifford form the corpus's *Clifford Structure of the Biquaternion Algebra*. The construction and the particle assignments are transcribed from the spinor-structure programme (V. V. Varlamov, arXiv:1409.1400, §§2.3, 3); the mass formula used to place the charge multiplets is the subject of the companion *The Spin–Mass Formula and the Spectrum of Elementary Particles in Biquaternionic Form*.

- Companion article *The Spin–Mass Formula and the Spectrum of Elementary Particles in Biquaternionic Form*, for the mass formula that fixes the spin-space degrees on the spin lines.
- Companion article *SU(3) Representations and the Gell-Mann–Okubo Mass Formula in Biquaternionic Form*, for the $\mathrm{SU}(3)$ representation theory and the mass splitting within a supermultiplet.
- Companion articles *The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)* and *The Gluon: An Octet Outside the Biquaternion Algebra*, for the framework's own statement of what it cannot contain.
- Companion articles *The Proton in Biquaternionic Form* and *The Neutron in Biquaternionic Form*, for the two states of the charge doublet as biquaternion fields.
- Mathematics article *Projective Representations* and *The Peter–Weyl Theorem*, for the ray representation and the central extension used in the last section.

## The Abstract Hilbert Space

The starting point is von Neumann's abstract Hilbert space. Wave functions are vectors $|\psi\rangle$ of a complex Hilbert space $\mathcal{H}$ on which a representation $U(g)$ of the Lorentz group acts, subject to the **von Neumann condition**

$$
\int_{\mathrm{SL}(2,\mathbb{C})}\bigl|\langle\psi\,|\,U(g)\,|\,\psi\rangle\bigr|\,dg < \infty,
$$

where $dg$ is a Haar measure. The condition is what makes the representation integrable on the group and gives the space a group-averaged inner product. An infinite sequence $|\psi_1\rangle,|\psi_2\rangle,\dots$ spans the space in the sense of **convergence in average**,

$$
\bigl\|\psi\rangle - |s_n\rangle\bigr\| = \int_{\mathrm{SL}(2,\mathbb{C})}\bigl|\psi\rangle-|s_n\rangle\bigr|^{2}\,dg \longrightarrow 0 \quad (n\to\infty),
\qquad |s_n\rangle = \sum_{j=1}^{n}c_j\,|\psi_j\rangle,
$$

and the Gram–Schmidt process makes the sequence orthonormal. A space satisfying the von Neumann condition and the convergence condition is the **abstract Hilbert space** $\mathcal{H}_\infty$. It is the arena in which the spin and charge spaces are placed, and the whole construction below is a statement about how finite-dimensional factors tensor onto it.

## Spin Multiplets

### The Doubling of the Wave Function

Pauli's theory of electron spin is a **doubling** of the space of wave functions. If $|\psi_1\rangle$ and $|\psi_2\rangle$ are vectors of $\mathcal{H}_\infty$, the doubled space is the set of formal combinations $c_1|\psi_1\rangle+c_2|\psi_2\rangle$, and it is realised by the tensor product

$$
\mathcal{H}_S^2\otimes\mathcal{H}_\infty,
$$

with basis vectors $|e_1\rangle,|e_2\rangle$ of $\mathcal{H}_S^2$ and general vector $\psi_S=\sum_j|x_j\rangle\otimes|\psi_j\rangle$. The correspondence with the formal sum shows the tensor product is the adequate description of the space of wave functions with spin.

### Spin Doublets and Triplets

The simplest multiplet is the **spin doublet**, with the two spin states $\pm\frac12$ on the spin-$\frac12$ line and its dual:

$$
\tau^{\frac12,0}\ (\text{spin }\tfrac12) \qquad\text{and}\qquad \tau^{0,\frac12}\ (\text{spin }-\tfrac12).
$$

This is the fundamental doublet, and it is the Dirac equation's content. The same construction at the next interlocking place gives the doublet $\tau^{1,\frac12}\oplus\tau^{\frac12,1}$, and so on up the chain; there are infinitely many spin doublets, each a pair of states $\pm\frac12$ on the spin-$\frac12$ line and its dual.

The **spin triplet** is built within $\mathcal{H}_S^3\otimes\mathcal{H}_\infty$, and its fundamental member is

$$
\tau^{1,0}\ (\text{spin }1),\qquad \tau^{\frac12,\frac12}\ (\text{spin }0),\qquad \tau^{0,1}\ (\text{spin }-1),
$$

the two outer states on the spin-$1$ line and its dual, the middle state on the spin-$0$ line. The general **spin multiplet** is

$$
\mathcal{H}_S^{\,2s+1}\otimes\mathcal{H}_\infty,
\qquad s=0,\tfrac12,1,\tfrac32,\dots,
$$

whose $2s+1$ states are the spin projections $-s,-s+1,\dots,s$, distributed over the spin lines of the interlocking diagram. The multiplets are fermionic for $s$ half-integer and bosonic for $s$ integer, and every multiplet has an antiparticle multiplet reached by the dual lines. The spaces $\mathcal{H}_S^{2s+1}\otimes\mathcal{H}_\infty$ are **nonseparable** — the infinite-dimensional factor is the reason — and this is recorded as a property of the construction, not as a defect.

## Charge Multiplets

Heisenberg's proposal that proton and neutron are two states of one particle — the nucleon — is formally the same doubling, with the charge space $\mathcal{H}_Q^2$ in place of the spin space:

$$
\mathcal{H}_Q^2\otimes\mathcal{H}_\infty,
$$

where $\mathcal{H}_Q^2$ is the charge space associated with the **fundamental** representation of $\mathrm{SU}(2)$. Kemmer's generalisation to three charge states $+1,0,-1$ places a three-dimensional charge space,

$$
\mathcal{H}_Q^3\otimes\mathcal{H}_\infty,
$$

with $\mathcal{H}_Q^3$ associated with the triplet (adjoint) representation of $\mathrm{SU}(2)$. The two cases are the charge doublet and the charge triplet; both are ordinary $\mathrm{SU}(2)$ isospin multiplets, assembled in the same way as the spin multiplets. The pattern extends to $\mathcal{H}_Q^{N}\otimes\mathcal{H}_\infty$ for the higher internal groups, and it is in this sense that the particle classification of the Standard Model becomes a statement about tensor factors.

## The Spin–Charge Space

The spin and charge multiplets combine. The **spin–charge Hilbert space** is

$$
\mathcal{H}_S\otimes\mathcal{H}_Q\otimes\mathcal{H}_\infty,
$$

and a state vector of it is written

$$
|A\rangle = \bigl(\tau^{l\dot l},\ \mathrm{Sym}^{(k,r)},\ \mathrm{Cl}_{p,q},\ S_{(p+q)/2},\ C^{a,b,c,d,e,f,g},\ \dots\bigr),
$$

the entries being the Lorentz representation $\tau^{l\dot l}$ that fixes the spin $s=|l-\dot l|$, the symmetric representation space $\mathrm{Sym}^{(k,r)}$ of degree $(k+1)(r+1)=(2l+1)(2\dot l+1)$, the Clifford algebra $\mathrm{Cl}_{p,q}$ associated with the representation, its spin space $S_{(p+q)/2}$, and the $\mathbb{Z}_2\times\mathbb{Z}_2\times\mathbb{Z}_2$ group of the discrete operations of the companion CPT article. The **main object** defining a vector is the representation $\tau^{l\dot l}$; the Clifford algebra, the spin space and the discrete group belong to the spinor structure and are attached to it.

The charge takes the three values $\{-1,0,\bar0\}$: the values $\pm1$ are the charged particles, carried by the complex representations; the value $0$ is the neutral particle with a distinct antiparticle, carried by the real representations of quaternionic division ring; and the value $\bar0$ is the **truly neutral** particle, carried by the real representations of real division ring. This trichotomy is the subject of the companion *Charge Conjugation and the Division Ring*, and the present section takes it as the labelling of the charge factor. A supermultiplet is then a set of vectors of $\mathcal{H}_S\otimes\mathcal{H}_Q\otimes\mathcal{H}_\infty$ sharing a Lorentz representation and a Clifford algebra and differing in the charge projection.

## Superselection Rules

Not every superposition of vectors of $\mathcal{H}_S\otimes\mathcal{H}_Q\otimes\mathcal{H}_\infty$ is realisable. Wigner, Wightman and Wick showed in 1952 that the existence of superselection rules is tied to the unmeasurability of the relative phase of a superposition: certain linear combinations of states are not physical, and the space decomposes into **coherent subspaces** within which superpositions are allowed. The programme reads the spin and the charge as two such superselection rules, so that coherent subspaces are labelled by spin and charge, and it notes that a complete enumeration of the rules is not available. The framework's contribution here is organisational rather than dynamical: the superselection structure is what makes $\mathcal{H}_S\otimes\mathcal{H}_Q\otimes\mathcal{H}_\infty$ a direct sum of sectors rather than a single module, and it is the reason a particle can be labelled by its spin and charge without ambiguity.

## Symmetry as Rays and the Central Extension

### Wigner's Theorem

A second structural point concerns the representation of the symmetry group. A physical state is a **ray** — a unit vector up to phase — and a symmetry maps rays to rays preserving transition probabilities. By Wigner's theorem the map is **unitary or antiunitary**, and the two possibilities are available exactly when the space is defined over $\mathbb{C}$, since the complex field has exactly two absolute-value-preserving automorphisms, the identity and complex conjugation; over $\mathbb{R}$ only unitary maps occur. This is the same dichotomy as the anti-unitary $T$ of the CPT article, and it is the field-theoretic origin of the corpus's observation that the algebra's complex conjugation supplies the anti-linear part of the discrete operations.

### The Ray Representation

Because only rays are physical, the multiplication law of symmetry operators is a **ray (projective) representation**,

$$
T_{gg'} = \omega(g,g')\,T_g\,T_{g'}, \qquad \omega(g,g')\in U(1),
$$

and when $\omega\ne1$ the ordinary theory of group representations does not apply. The remedy is the **central extension**: the group $G$ is enlarged to $E$ whose ordinary representations reproduce all the ray representations of $G$, and a symmetry group of the physical system is represented by the unitary or antiunitary maps of $\mathcal{H}_S\otimes\mathcal{H}_Q\otimes\mathcal{H}_\infty$ that lift the ray representation. The internal symmetry groups $\mathrm{SU}(2),\mathrm{SU}(3),\dots$ act in this way, and the supermultiplet structure of the eightfold way is the orbit structure of their action.

## The Biquaternion Reading

The framework's relation to all this is precise, and it is a relation of **one** of the three factors. The spin factor $\mathcal{H}_S$ is exactly the framework's own spinor structure: the Lorentz representations $\tau^{l\dot l}$, the spin lines, and the spin spaces $S_{(p+q)/2}$ are the corpus's objects, and the finite-dimensional spin space of a state is the module of the biquaternion algebra or of its tensor powers. The mass formula that fixes the degree on each spin line is the companion article's.

The charge factor $\mathcal{H}_Q$ is a different matter. The internal symmetry groups act there by central extension, and the companion *The Gauge Group Ceiling* establishes that the biquaternion algebra's own compact structure reaches $\mathrm{SU}(2)$ and stops: the $\mathrm{SU}(3)$ of the charge triplet's further generalisation is not an algebra of $\mathbb{B}$. The spin–charge space is therefore something the framework can **state** and lay out, but not something it **contains**; the charge factor is added from outside, and its $\mathrm{SU}(3)$ structure is transcribed.

The infinite-dimensional factor $\mathcal{H}_\infty$ is the third point. It is where the mass-shell orbit lives, and it is the factor that makes the spaces nonseparable. The corpus's fields are functions on spacetime, which is to say sections of a bundle whose fibre is a finite-dimensional module; the programme's $\mathcal{H}_\infty$ is a different object, and the correspondence between the two is not constructed here. This is the honest limit of the identification.

## What the Framework Establishes, Transcribes, and Does Not

**Established, and recomputed.**

- The spin multiplet is $\mathcal{H}_S^{2s+1}\otimes\mathcal{H}_\infty$ and the charge multiplet is $\mathcal{H}_Q^m\otimes\mathcal{H}_\infty$; the spin triplet's fundamental member is $\tau^{1,0}\oplus\tau^{1/2,1/2}\oplus\tau^{0,1}$, with spins $+1,0,-1$, and the spin doublet's is $\tau^{1/2,0}\oplus\tau^{0,1/2}$, with spins $\pm\frac12$. These are the tensor-product decompositions and are checkable in the corpus's representation ring.
- The degree $\dim\mathrm{Sym}^{(k,r)}=(k+1)(r+1)$ equals $(2l+1)(2\dot l+1)$ for $\tau^{l\dot l}$ with $k=2l$, $r=2\dot l$, so the vector label's two entries carry the same number.
- A symmetry of rays is unitary or antiunitary, and the two possibilities exist exactly over $\mathbb{C}$; this is Wigner's theorem and the field-automorphism argument, both standard.

**Transcribed, not derived.**

- The whole construction of $\mathcal{H}_S\otimes\mathcal{H}_Q\otimes\mathcal{H}_\infty$, the von Neumann and convergence conditions, and the superselection reading.
- The central-extension treatment of the internal symmetries and the identification of $\mathrm{SU}(2)$ and $\mathrm{SU}(3)$ as the acting groups.
- The particle content: which supermultiplets exist and which charge multiplets they reduce to.

**Gap, left visible.**

- No derivation of the internal symmetry group. The framework reaches $\mathrm{SU}(2)$ and not $\mathrm{SU}(3)$; the charge factor with its $\mathrm{SU}(3)$ is an addition.
- No derivation of the $\mathcal{H}_\infty$ factor, and no map between the programme's Hilbert space and the corpus's field-valued-in-a-module description.
- No dynamical statement: the spin–charge space classifies states, and the superselection structure constrains superpositions, but neither is derived from a Lagrangian the framework supplies.

## Open Questions

1. **Is there a biquaternion model of $\mathcal{H}_Q$?** The charge doublet and triplet are $\mathrm{SU}(2)$ representations, and the framework does reach $\mathrm{SU}(2)$. Is the charge factor of the fundamental doublet and triplet then *inside* $\mathbb{B}$ after all, with only the passage to $\mathrm{SU}(3)$ crossing the ceiling? The companion gauge-ceiling article separates these, and the question is whether the separation is sharp.

2. **Superselection and the two sectors.** The corpus's material/informational separation is algebraic, not a superselection rule. Is it a coherent-subspace split in the programme's sense, and would that connect the framework's sector structure to the standard superselection rules of charge and spin?

3. **The relation to the field description.** A state vector here is an element of an abstract Hilbert space; a corpus field is a function into a module. Is there a functor between the two pictures, and would the corpus's Fock-space articles supply it?

4. **Mass and the charge factor.** The companion mass formula attaches a mass to the spin representation. Does the charge factor modulate it — the observed charged/neutral mass splittings within an isomultiplet — and if so, is that the $\delta m$ of the Gell-Mann–Okubo machinery?

## Summary

The spinor-structure programme assembles the particle content of the Standard Model into a single Hilbert space $\mathcal{H}_S\otimes\mathcal{H}_Q\otimes\mathcal{H}_\infty$: the spin factor from Pauli's doubling of the wave function, the charge factor from Heisenberg's and Kemmer's doublings for the nucleon and the three-charge particle, and the infinite-dimensional factor from Wigner's definition of an elementary particle. A state vector is a list of a Lorentz representation $\tau^{l\dot l}$ (fixing the spin), its symmetric representation space, its Clifford algebra and spin space, and the discrete-operation group; the charge takes the three values $\pm1,0,\bar0$ that the companion division-ring article separates. Superpositions are restricted by superselection rules into coherent subspaces labelled by spin and charge, and the internal symmetry groups act through a central extension of their ray representations, over $\mathbb{C}$ admitting both unitary and antiunitary maps.

The framework's relation to this is a relation of one factor. The spin factor is its own spinor structure, with the companion mass formula fixing degrees on the spin lines. The charge factor lies beyond the gauge-group ceiling, so the $\mathrm{SU}(3)$ structure is transcribed, not contained. The infinite-dimensional factor has no constructed counterpart in the corpus's field description. Recorded as a scheme, the spin–charge space is a clean bridge between the spinor structure and the particle classification, and a clear statement of exactly where the framework stops.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{H}_\infty$ | Abstract Hilbert space of the Lorentz group representation, von Neumann condition |
| $\mathcal{H}_S^{\,2s+1}$, $\mathcal{H}_Q^{m}$ | Finite-dimensional spin and charge spaces |
| $\mathcal{H}_S\otimes\mathcal{H}_Q\otimes\mathcal{H}_\infty$ | Spin–charge Hilbert space |
| $s=\lvert l-\dot l\rvert$ | Spin of the Lorentz representation |
| $\mathrm{Sym}^{(k,r)}$, degree $(k+1)(r+1)$ | Symmetric representation space of $\tau^{l\dot l}$, $k=2l$, $r=2\dot l$ |
| $\mathrm{Cl}_{p,q}$, $S_{(p+q)/2}$ | Associated Clifford algebra and spin space |
| $Q=+1,0,\bar0$ | Charged, neutral, truly neutral charge states |
| $T_{gg'}=\omega(g,g')T_gT_{g'}$ | Ray (projective) representation of the symmetry group |
| $E=\{(\omega,x)\}$ | Central extension whose representations lift the ray representations |
| Coherent subspace | Maximal domain of allowed superposition under superselection |

## Further Reading

- E. P. Wigner, "On unitary representations of the inhomogeneous Lorentz group," *Annals of Mathematics* **40** (1939) 149–204, for the definition of an elementary particle and the unitary/antiunitary dichotomy.
- J. von Neumann, *Mathematical Foundations of Quantum Mechanics* (Springer, 1932), for the abstract Hilbert space and the convergence conditions.
- W. Pauli, "Zur Quantenmechanik des magnetischen Elektrons," *Zeitschrift für Physik* **43** (1927) 601–623, for the spin doubling of the wave function.
- W. Heisenberg, "Über den Bau der Atomkerne I," *Zeitschrift für Physik* **77** (1932) 1–11, for the proton–neutron charge doublet.
- N. Kemmer, "The charge-dependence of nuclear forces," *Proceedings of the Cambridge Philosophical Society* **34** (1938) 354–364, for the three-charge multiplet.
- E. P. Wigner, G. C. Wick and A. S. Wightman, "The intrinsic parity of elementary particles," *Physical Review* **88** (1952) 101–105, for the relation between superselection rules and the unmeasurability of relative phases.
- M. Gell-Mann and Y. Ne'eman, *The Eightfold Way* (Benjamin, 1964), for the $\mathrm{SU}(3)$ supermultiplets and their reductions.
- V. V. Varlamov, "Spinor Structure and Internal Symmetries," *International Journal of Theoretical Physics* **54** (2015) 3533–3576 (arXiv:1409.1400), for the spin–charge Hilbert space, the superselection reading and the central-extension treatment recorded here.
- Companion articles: *The Spin–Mass Formula and the Spectrum of Elementary Particles in Biquaternionic Form*; *SU(3) Representations and the Gell-Mann–Okubo Mass Formula in Biquaternionic Form*; *Charge Conjugation and the Division Ring*; *The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)*; *The Gluon: An Octet Outside the Biquaternion Algebra*; *The Proton in Biquaternionic Form*; *The Neutron in Biquaternionic Form*.
