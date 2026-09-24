# __The Neutron in Biquaternionic Form__

## Introduction

The neutron is the electrically neutral, spin-$\tfrac12$ baryon: in the Standard Model a bound colour-singlet composite of one up quark and two down quarks, with mass $m_n c^2 = 939.565$ MeV, magnetic moment $\mu_n = -1.9130427\,\mu_N$, mean lifetime about $880$ s, and baryon number one. All of these are measured facts, and standard physics accounts for them within the colour gauge theory and its bound states. This article asks a narrower question than *what is the neutron*: **which properties of the neutron does the biquaternion framework of this series reach, which does it merely represent, and which does it not reach at all?**

The answer is stated at the outset because the pull toward closure is strong. The framework supplies a spin-$\tfrac12$ module and a Dirac equation, so it can represent a neutral spin-$\tfrac12$ field; it supplies a charge operator on that module, so it can state the neutron's neutrality as a constraint; and there it stops. The framework contains no colour group, no confinement mechanism, no three-dimensional internal module, no quark, and no bound-state construction. The neutron's **composite character is therefore not reached.** Its three-quark content, its colour singlet, its baryon number, its mass, its magnetic moment, and its lifetime are imported from standard physics, not derived here. That is a negative result, and it is the article's finding; it is written as such rather than padded.

A second honest point belongs here. The series takes the standing position that its predictions agree with standard physics because it is a **reformulation**, not a new theory. For the neutron that position is radical: nothing here distinguishes the framework's neutron from the Standard Model's, and the tree-level spin coupling it inherits gives a **zero** magnetic moment for a neutral structureless Dirac field, which is not the neutron. The neutron is exactly the object on which a colourless reformulation has nothing to say about structure, and the article records the boundary rather than crossing it.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$ and $e_1e_2 = e_3$, and $i$ is the scalar imaginary, $i^2 = -1$, commuting with every $e_k$. The fixed-point subspaces are $\mathbb{M}_-$ (anti-Hermitian, the material sector) and $\mathbb{M}_+$ (Hermitian, the informational sector), with $\mathbb{B} = \mathbb{M}_- \oplus \mathbb{M}_+$; $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace and $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ is the center of the algebra. The biquaternionic gradient is $\tilde{\nabla} = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z$, its quaternion conjugate is $\bar{\tilde{\nabla}} = e_0\partial_{ict} - e_1\partial_x - e_2\partial_y - e_3\partial_z$, and $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla}$. The spinor module is $\Delta = S\oplus\bar{S}$, with $S=\mathbb{C}^2$ the unique simple left $\mathbb{B}$-module, the chirality operator is $\gamma_5 = \mathrm{diag}(-I_2, I_2)$, and the chiral projectors are $P_L=\tfrac12(I_4-\gamma_5)$, $P_R=\tfrac12(I_4+\gamma_5)$. The charge operator inherited from the chiral-fermion article is $Q = q_LP_L + q_RP_R$. Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the **speed of light in the medium** and $c_0$ the vacuum speed of light. The trace formula $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ is inherited unchanged. The symbols $SU(3)$, $N_c$, and the word *quark* are **standard-model notation, not framework objects**; they are used only where standard physics is quoted or where an object is named as absent.

## The Neutron as a Spin-$\tfrac12$ Biquaternion Field

The framework's carrier for any spin-$\tfrac12$ fermion is the Dirac module

$$
\Delta \;=\; S\oplus\bar{S}, \qquad S=\mathbb{C}^2=\left(\tfrac12,0\right), \qquad \bar{S}=\left(0,\tfrac12\right), \qquad \dim_{\mathbb{C}}\Delta = 4,
$$

of the companion articles. A neutron field $\tilde{\Psi}$ is placed in this module, and its free propagation is the biquaternion Dirac equation

$$
\tilde{\nabla}\tilde{\Psi}_R \;=\; m_n\,\tilde{\Psi}_L, \qquad \bar{\tilde{\nabla}}\tilde{\Psi}_L \;=\; m_n\,\tilde{\Psi}_R,
$$

with $m_n$ the neutron mass. The Lorentz group acts on the module through $SL(2,\mathbb{C})$, the double cover of the proper orthochronous Lorentz group, and a field in it transforms in the spinor representation $(\tfrac12,0)\oplus(0,\tfrac12)$. The representation-theoretic content of spin-$\tfrac12$ — half-integer spin, the double-valued rotation, Lorentz covariance — is inherited from the algebra, and in this sense the framework **represents** a spin-$\tfrac12$ field. Three qualifications are what the neutron actually tests.

**The representation is generic.** The algebra $\mathbb{B}\cong M_2(\mathbb{C})$ has one isomorphism class of simple module, so every structureless spin-$\tfrac12$ field is carried by the same objects; the electron article records the same point, that the algebra contains no discriminator. The neutron is distinguished from the electron here only by the two numbers inserted into the equation, $m_n$ and the charge. Nothing in the algebra prefers these values, and nothing in it marks the field as the neutron rather than any other spin-$\tfrac12$ fermion of the same mass and charge.

**Spin-$\tfrac12$ is represented, not built.** In standard physics the neutron's spin-$\tfrac12$ is not fundamental: it is the total angular momentum of three spin-$\tfrac12$ constituents in a bound colour-singlet state, and the composite nature is what makes the spin assignment non-trivial (the naive three-quark spin coupling gives both $\tfrac12$ and $\tfrac32$; the observed ground state is $\tfrac12$). The framework's unique simple module carries spin-$\tfrac12$ as a representation, but the framework contains no constituents and no composition rule, so it does **not** derive that the neutron's bound state has spin-$\tfrac12$. It represents the answer rather than producing it.

**The mass is a parameter, and the near-degeneracy with the proton is unexplained.** The free equation contains $m_n$ exactly once, as the coefficient of the linear mass term $m_n$;

the framework is scale-free until that number is supplied, so the neutron mass is an input rather than a consequence. So is the fact that the neutron and proton masses agree to about $0.14\%$ ($m_n-m_p \approx 1.293$ MeV): in standard physics this near-degeneracy is the isospin symmetry of the strong interaction, an approximate flavour $SU(2)$ acting on the $(p,n)$ doublet. The framework does contain an $SU(2)$ — the real-vector part of $\mathbb{M}_-$ is $\mathfrak{su}(2)$ under the commutator — but that is the rotation/gauge algebra of the material sector, not flavour isospin, and identifying the two would be an import rather than a derivation. The framework supplies no second fermion with a nearly equal mass.

## Neutrality and the Charge Operator

The neutron's charge is zero. Of the neutron's properties, neutrality looks like the one the framework might own, because the framework does have a charge operator. The chiral-fermion article constructs it on the Dirac module as

$$
Q \;=\; q_L\,P_L + q_R\,P_R,
\qquad
D_\mu = \partial_\mu + \frac{i}{\hbar}A_\mu Q,
\qquad
[D_\mu,D_\nu] = \frac{i}{\hbar}F_{\mu\nu}Q,
$$

with independent chirality charges $q_L,q_R$ that the algebra does not fix (they are parameters, and the bare Dirac mass is gauge invariant if and only if $q_L=q_R$). The operator $Q$ is a module endomorphism, not an element of $\mathbb{B}$ multiplying from the left: its chiral part is proportional to $\gamma_5$, which is a central idempotent combination of the complexification $\mathbb{C}\otimes_\mathbb{R}\mathbb{B}$, not of $\mathbb{B}$. Written in the block basis $(\psi_L,\psi_R)$ it is diagonal,

$$
Q \;=\; \mathrm{diag}\big(q_L I_2,\ q_R I_2\big) \;\cong\; \mathrm{diag}\big(q_L,q_L,q_R,q_R\big),
$$

so its spectrum is $\{q_L,q_R\}$, each with multiplicity two. A single-particle state is **neutral** when it is annihilated by the charge operator, $Q\psi=0$. The kernel is elementary and was recomputed exactly:

- If **both** $q_L$ and $q_R$ are nonzero, then $\ker Q = \{0\}$: the module contains no neutral single-particle state at all.
- If $q_L=0$ and $q_R\neq0$, then $\ker Q = S$, the two-complex-dimensional left-handed block.
- If $q_R=0$ and $q_L\neq0$, then $\ker Q = \bar{S}$, the right-handed block.
- If $q_L=q_R=0$ the whole module is neutral (the trivially uncoupled case).

Neutrality on the module is therefore not a generic property: it requires one chirality to be uncoupled from the abelian charge. And, apart from the trivially uncoupled case $q_L=q_R=0$, the state that achieves it is **chirality-definite**. When $q_L=0$ the neutral space is $S$, on which $\gamma_5=-1$; when $q_R=0$ it is $\bar{S}$, with $\gamma_5=+1$. The Dirac mass bilinear $\bar{\Psi}\Psi=\psi_L^{\dagger}\psi_R+\psi_R^{\dagger}\psi_L$ vanishes on any definite-chirality state, exactly (recomputed); so the neutral single-particle state of the module carries no Dirac mass bilinear. Whether it can carry a mass at all then rests on a Majorana-type coupling built on the algebra's real structure $\flat$, which pairs the field with its conjugate rather than with an opposite-chirality partner, and whether the framework's real structure carries such a physical coupling is the open question inherited from the chiral-fermion article.

The framework therefore does not cleanly supply a **massive neutral spin-$\tfrac12$ single particle**: on the module, neutrality and the massive Dirac reading pull in opposite directions.

**Can a neutral composite be expressed?** The neutron is not a single module element; it is a bound state of three fermions. The framework does have a many-particle construction: the Fock-space article builds the antisymmetric tensor algebra of the spinor module, with creation and annihilation operators, so a three-fermion **state** is expressible in principle. But the three things the neutron needs are absent. First, **colour**: there is no three-dimensional internal space, and the module ceiling forbids a colour triplet, so any three constituents would be three excitations of one colourless species rather than three coloured quarks. Second, **binding**: the framework has no confinement mechanism and no bound-state construction, so nothing makes a three-particle state a neutron rather than a free scattering state, and there is no mass gap to hold it below threshold. Third, a **selection rule** fixing the constituent number three, the baryon number, and the spin-$\tfrac12$ of the bound state: none is supplied. The charge operator is defined on the one-particle module; a total charge on the Fock space would be its second-quantized sum $\sum_i Q_i$, additive by construction, but the corpus does not construct it, and even granting it the condition fixes a relation among unfixed charges rather than a value. If one imposes the additive condition on three constituents, neutrality reads

$$
n_L\,q_L + n_R\,q_R = 0, \qquad n_L+n_R = 3,
$$

which has solutions for special charge ratios (for instance $(n_L,n_R)=(1,2)$ requires $q_R=-\tfrac12 q_L$), but nothing in the framework fixes $q_L$ or $q_R$, and the standard quark charges are not framework objects. Reading the values $\tfrac23$ and $-\tfrac13$ into $q_L$ and $q_R$ would be exactly the manufacture of the neutrality from an imported quark model, and this article does not do it.

**Verdict on the trap.** The framework's charge operator can *state* the neutron's neutrality as the constraint $Q\psi=0$, and it classifies the single-particle solutions of that constraint; a neutral many-particle **state** is not ruled out in principle once a Fock space and an additive total charge are granted. But the neutron as a **bound colour-singlet composite** is not expressible: colour, confinement, and the selection rule that fixes three constituents are all absent. And the neutrality is not *derived*, because the framework contains no constituents whose charges could sum to zero. The honest sentence is: **neutrality is expressible as a constraint on unfixed charges, a neutral bound composite is not expressible, and the neutrality itself is imported from standard physics.** That is a negative result, and it is reported as one.

## Composite Character: No Colour, No Confinement, No Constituents

The reason the bound composite is unavailable is structural, and the QCD research agenda of this series states it precisely. Three of its established findings carry over unchanged.

**No colour group.** The compact algebra available inside $\mathbb{B}$ under the commutator is at most $\mathfrak{u}(2)=\mathfrak{u}(1)\oplus\mathfrak{su}(2)$, of real dimension four: $\mathbb{M}_-$ decomposes as a Lie algebra into $\mathbb{R}(ie_0)\oplus\mathfrak{su}(2)$, and the maximal compact subalgebra of $\mathfrak{gl}(2,\mathbb{C})$ is $\mathfrak{u}(2)$. No $\mathfrak{su}(3)$ subalgebra is available, and the three quaternion units $e_1,e_2,e_3$ span the *adjoint* of $\mathfrak{su}(2)$, not a complex triplet. Counting three basis vectors is not constructing colour.

**No three-dimensional module.** The algebra $\mathbb{B}\cong M_2(\mathbb{C})$ is simple, so every module is a direct sum of copies of the unique simple module $\mathbb{C}^2$: every $\mathbb{B}$-module has complex dimension $2k$. A colour triplet — a complex three-dimensional internal space for a quark — is not a $\mathbb{B}$-module. The ceiling is a statement about the carrier, not about the arithmetic.

**No confinement.** The framework has no non-perturbative formulation, no Wilson loop, no gauge-invariant regulator, no gauge-fixing principle, and no mass gap; the agenda records confinement as an obstacle with **no mechanism proposed**, not merely an unproven one.

Consequently the neutron's defining structural facts — baryon number one, three constituent quarks, a colour singlet, a bound state with a mass gap above it — lie outside the framework. The framework cannot say what the neutron is made of, and it cannot explain why a colourless composite of charged constituents exists at all. Its own closest apparatus is the zero-divisor cone of $\mathbb{M}_-$ and the non-abelian curvature it does contain, neither of which is a confinement mechanism. On the fermion-number question the framework is also not equipped: the parent's linear mass conserves the vector $U(1)$, while the separate Majorana-type coupling built on the real structure $\flat$ reduces a continuous fermion-number phase to a sign on that reading; neither supplies the quark model's baryon number as a conserved $U(1)$.

The composite character is thus not a gap of the article; it is the framework's boundary. What is left, for the neutron, is a representation of a structureless spin-$\tfrac12$ field with two inserted parameters and a neutrality constraint — and, as the next section shows, even the most basic measured consequence of compositeness falls outside it.

## The Magnetic Moment: A Neutral Field with a Nonzero Moment

The electron article derives, from the $1/2m$ coefficient produced by the Dirac equation under minimal coupling, the tree-level gyromagnetic relation $\boldsymbol{\mu} = (g q/2m)\mathbf{S}$ with $g=2$. Applied to a **neutral** structureless Dirac fermion the same treatment gives

$$
\boldsymbol{\mu} \;=\; \frac{g\,q}{2m}\,\mathbf{S} \;=\; 0 \qquad (q=0),
$$

for any $g$: a neutral point Dirac fermion has no magnetic moment. The measured neutron moment is

$$
\mu_n \;=\; -1.9130427\,\mu_N \;\neq\; 0,
$$

and its sign is negative. The nonzero value is direct evidence that the neutron is not structureless; in standard physics it arises from the charged quarks and their spin and orbital motion inside the colour-singlet bound state. The framework has neither the charged constituents nor the binding, so it cannot supply the moment, and its tree-level spin prediction is not merely incomplete on the neutron — read as a neutral point Dirac field it is **zero, against a measured number of order one in nuclear magnetons**. This is the sharpest place in the article where a framework statement meets a neutron measurement and does not match, and it matches the composite conclusion of the preceding section rather than contradicting it: the neutron is precisely the object for which the framework's structureless Dirac description is quantitatively wrong.

The same boundary shows in the neutron's decay. The free neutron beta-decays with a mean lifetime of about $880$ s; the decay is a weak-interaction process, and the framework contains no weak chiral gauge structure — its center is vector-like, and the chiral-fermion article records that a chiral gauge group is not derived. The lifetime is therefore outside the framework, as is the isospin near-degeneracy with the proton noted above.

## Accounting: Derived, Represented, Outside

The article's finding is best stated as a ledger, in the manner of the electron article. Each row is a property of the neutron, its status in the framework, and where the content actually comes from.

| Neutron property | Status | Object or reason |
|---|---|---|
| Spin-$\tfrac12$ representation content (generic) | Derived (framework), not neutron-specific | unique simple module $\Delta=S\oplus\bar{S}$, spinor representation $(\tfrac12,0)\oplus(0,\tfrac12)$ |
| Free Dirac kinematics, mass-shell relation | Derived (framework) | biquaternion Dirac equation, linear chiral pair $\tilde{\nabla}\tilde{\Psi}_R=m\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L=m\tilde{\Psi}_R$ |
| Neutrality constraint $Q\psi=0$ and its kernel | Derived (framework) | charge operator $Q=q_LP_L+q_RP_R$; kernel trivial unless one chirality charge vanishes |
| Mass value $m_n$ | Represented | parameter of the equation; not derived |
| Charge value $0$ | Represented | a constraint/parameter; not derived from quark charges |
| The identification "*this* field is the neutron" | Represented | the inserted mass and charge |
| Composite character: three quarks, colour singlet | **Outside** | no colour group, no three-dimensional module, no constituents |
| Confinement and the bound-state mass gap | **Outside** | no mechanism, no non-perturbative apparatus |
| Baryon number | **Outside** | not a framework quantum number |
| Magnetic moment $\mu_n\neq0$ | **Outside** | measured; the framework's neutral Dirac value is $0$ |
| Lifetime / beta decay | **Outside** | no weak chiral gauge structure |
| Isospin; $p$–$n$ near-degeneracy | **Outside** | approximate flavour $SU(2)$ not derived; the framework's $SU(2)$ is the sector's rotation algebra |
| Any discriminator from another spin-$\tfrac12$ field | **Outside** | the algebra contains none |

The table separates two kinds of statement that are easily run together. The framework *does* derive a spin-$\tfrac12$ module and a charge operator; the neutron *does* occupy that module and *does* satisfy the neutrality constraint for a suitable, unfixed charge assignment. But none of that is specific to the neutron, and none of it reaches the properties that make the neutron a neutron. The derived rows are generic fermion structure; the neutron-specific rows are either inserted or outside.

## The Gaps, Named

Three gaps are structural and cannot be closed by better notation. First, **colour**: nothing in the series derives $SU(3)$ or any three-valued internal structure, and the module ceiling makes a colour triplet impossible within the present carrier. Second, **confinement**: no mechanism has been proposed, so the existence of the neutron as a bound colour singlet is not accounted for. Third, **the composite**: the framework has no multi-fermion bound-state construction, so even granting colour it could not assemble the neutron. These are the framework's boundary, and the QCD agenda's three-way classification places them there.

Two further gaps are the article's own, and they are narrower. The **neutrality is a constraint, not a derivation**: the charge operator can be set to zero, but the framework supplies neither the charge values nor the constituents whose charges must cancel, and the standard quark charges are an input the framework does not contain. And the **magnetic moment is a counterexample, not a confirmation**: a neutral structureless Dirac field has zero moment, while the neutron's is nonzero, so the framework's one quantitative spin statement does not describe the neutron at all.

Finally, the standing **empirical-contact** gap applies with full force. Nothing here distinguishes the framework's neutron from the Standard Model's, because the framework reaches only the generic fermion structure they share; the neutron-specific content is imported. The article therefore makes no prediction, claims no prediction, and leaves the neutron's structure exactly where standard physics found it.

## Summary

The neutron is an electrically neutral spin-$\tfrac12$ baryon, and in the biquaternion framework of this series it is represented as a field in the Dirac module $\Delta=S\oplus\bar{S}$ satisfying the linear chiral mass pair $\tilde{\nabla}\tilde{\Psi}_R=m_n\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L=m_n\tilde{\Psi}_R$.

That representation is generic: the algebra carries any structureless spin-$\tfrac12$ field by the same objects, and the spin-$\tfrac12$ it supplies is a representation, not a construction from constituents.

The framework's charge operator $Q=q_LP_L+q_RP_R$ acts on the module with spectrum $\{q_L,q_R\}$. The neutrality constraint $Q\psi=0$ has a nonzero solution only if one chirality is uncoupled ($q_L=0$ or $q_R=0$), and, apart from the trivially uncoupled case $q_L=q_R=0$, the neutral solution is then chirality-definite, so it carries no Dirac mass bilinear; whether it is massive depends on a Majorana-type coupling on the algebra's real structure $\flat$, whose reading is open.

The framework does have a Fock space, so a neutral many-particle **state** is not ruled out in principle. But no neutral **bound composite** is expressible: there is no colour, no confinement, no binding, and no selection rule fixing three constituents. The neutrality is therefore stateable as a constraint on unfixed charges but not derived, and manufacturing it from the standard quark charges would be an import.

The neutron's composite character is not reached. The framework has no colour group (the compact algebra is at most $\mathfrak{u}(2)$, of dimension four), no three-dimensional module (every $\mathbb{B}$-module has even complex dimension), no confinement mechanism, and no bound-state construction; its baryon number, mass, lifetime, and isospin are not derived here. Its magnetic moment is the sharp quantitative case: a neutral structureless Dirac field has $\mu=0$, while $\mu_n=-1.9130427\,\mu_N$, so the framework's tree-level spin statement does not describe the neutron. The honest summary is that the framework reaches the neutron's neutrality as a constraint and its spin as a generic representation, and reaches nothing of what makes it a composite baryon.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H} \cong M_2(\mathbb{C})$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2=-e_0$, $e_1e_2=e_3$ |
| $i$ | Scalar imaginary, $i^2=-1$, central |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors; $\mathbb{B}=\mathbb{M}_-\oplus\mathbb{M}_+$ |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace |
| $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ | Center of the algebra |
| $\tilde{\nabla} = e_0\partial_{ict}+e_k\partial_k$ | Biquaternionic gradient (Dirac operator) |
| $\Box = \tilde{\nabla}\bar{\tilde{\nabla}}$ | d'Alembertian |
| $\tilde{\Psi}$, $\tilde{\Psi}^{\flat} = -\tilde{\Psi}^{\dagger}$ | Biquaternion Dirac field; anti-Hermitian conjugate |
| $\Delta = S\oplus\bar{S}$, $S=\mathbb{C}^2$ | Dirac module; unique simple left module |
| $\gamma_5 = \mathrm{diag}(-I_2,I_2)$ | Chirality operator, $\gamma_5^2=I_4$ |
| $P_L = \tfrac12(I_4-\gamma_5)$, $P_R = \tfrac12(I_4+\gamma_5)$ | Chiral projectors |
| $Q = q_LP_L+q_RP_R = \mathrm{diag}(q_L,q_L,q_R,q_R)$ | Charge operator on the module; $q_L,q_R$ unfixed parameters |
| $Q\psi=0$ | Neutrality constraint; kernel trivial unless $q_L=0$ or $q_R=0$ |
| $\bar{\Psi}\Psi = \psi_L^{\dagger}\psi_R+\psi_R^{\dagger}\psi_L$ | Dirac bilinear, chirality-odd |
| $\mathfrak{u}(2)=\mathfrak{u}(1)\oplus\mathfrak{su}(2)$ | Maximal compact algebra in $\mathbb{B}$; dimension $4$ |
| $m_n$, $\mu_n = -1.9130427\,\mu_N$ | Neutron mass (input) and measured magnetic moment (outside) |
| $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Inherited informational trace formula |
| $c = 1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |
| $SU(3)$, $N_c$, quark | Standard-model notation, not framework objects |

## Further Reading

- *The Electron in Biquaternionic Form* — the sibling accounting for a fundamental spin-$\tfrac12$ fermion, and the source of the tree-level $g=2$ relation used here to show that a neutral structureless Dirac field has zero magnetic moment.
- *The Dirac Equation in Biquaternionic Form* — the biquaternion Dirac equation, its mass term, plane-wave solutions, and the mass-shell relation used throughout.
- *Chiral Fermions in the Biquaternion Framework* — the Dirac module, the projectors, the charge operator $Q=q_LP_L+q_RP_R$, the mass selection rule, and the real structure whose reading is left open here.

- *Fock Space and Creation/Annihilation Operators in Biquaternionic Form* — the many-particle space (the antisymmetric tensor algebra of the spinor module) and its operators, the construction that lets a three-fermion *state* be written while supplying no binding.
- *Quantum Chromodynamics under the Biquaternion Framework — A Research Agenda* — the established ceiling on the colour group, the absent confinement mechanism, and the three-way classification the composite section inherits.
- *Non-Abelian Gauge Fields in Biquaternionic Form* — the compact gauge algebra inside $\mathbb{M}_-$ and the non-abelian machinery that stops short of colour.
- *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* — the sector decomposition, the four-vectors, and the $ict$ convention.
- *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* — the Hermitian sector, the rotor action, and the trace formula.
- *Introduction to the Biquaternion Universe* — the algebra, the two sectors, the frame constants, and the open many-particle extension on which a composite construction would depend.
- *The Spinor Module in Biquaternionic Form and Its Lorentz Action* — the module's Lorentz action and the spinor representation on which the spin-$\tfrac12$ representation rests.
- *Spin-$\tfrac12$ Quantum Mechanics in Biquaternionic Form* — the qubit/operator dictionary and the trace formula applied to spin states.
- *Angular Momentum and Spin in Biquaternionic Form* — the spin observables and their algebra, used here only as the generic spin structure the neutron inherits.
- *The Spin–Statistics Theorem in Biquaternionic Form* — why the neutron, as a spin-$\tfrac12$ fermion, obeys Fermi–Dirac statistics, another generic rather than neutron-specific consequence.
- *Canonical Quantization of the Biquaternion Dirac Field* — the equal-time anticommutators, the mode expansion, and the field's quantization, the fermionic setting in which the neutron would have to be a state.
