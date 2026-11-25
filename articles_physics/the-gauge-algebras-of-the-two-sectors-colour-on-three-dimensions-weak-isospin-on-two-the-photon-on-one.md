# __The Gauge Algebras of the Two Sectors: Colour on Three Dimensions, Weak Isospin on Two, the Photon on One__

## Introduction

**The question.** The strong sector and the electroweak sector are written in different algebras. Which algebra is each, on which module does it act, and which of the two does the biquaternion algebra actually hand over?

**The answer.**

$$
\boxed{\;
\underbrace{\mathfrak{su}(3)}_{\dim 8}\ \text{on}\ \mathbb C^3,
\qquad
\underbrace{\mathfrak{su}(2)_L\oplus\mathfrak{su}(2)_R}_{\dim 3+3}\ \text{on}\ \mathbb C^2\oplus\mathbb C^2,
\qquad
\underbrace{\mathfrak u(1)_{B-L}}_{\dim 1}\ \text{on the line},
\;}
$$

$$
\boxed{\;
8+1+3+3=15\ \longrightarrow\ 8+3+1=12\ \longrightarrow\ 8+1=9,
\qquad
\mathfrak u(1)_Y=\left\langle T_{3R}+\tfrac12(B-L)\right\rangle,
\quad
\mathfrak u(1)_{\mathrm{em}}=\left\langle T_{3L}+Y\right\rangle .
\;}
$$

**The single idea.** Each sector is a pair: an algebra and a module. The algebra alone does not name the sector, because $\mathfrak{su}(2)_L$ and $\mathfrak{su}(2)_R$ are the same algebra; what distinguishes them is which doublet they act on. And of the two non-abelian factors, only the weak ones come from the biquaternion algebra — the rotors are a copy of $\mathrm{SU}(2)$ — while colour is posited as an algebra on three of the carrier's four dimensions.

**What the article establishes.** The list of residual algebras with their dimensions; the module each acts on; the two derived abelian factors with their derivations; the sense in which the photon's algebra is one-dimensional; the three reductions of dimension and what each costs; and the boundary between what the algebra reaches and what the model posits.

**What the article does not establish.** No coupling, no dynamics, no spectrum. The couplings are [The Gauge Connection Below the Breaking: Three Pieces, Three Couplings, and What Each Multiplies](the-gauge-connection-below-the-breaking-three-pieces-three-couplings-and-what-each-multiplies.html). The states are [The Quantum Numbers Below the Breaking](the-quantum-numbers-below-the-breaking-colour-b-l-weak-isospin-and-the-electric-charge.html).

**Where the ceiling is.** The reason $\mathrm{SU}(3)$ is posited and not derived is [Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)](why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html). That article is the boundary statement this one uses and does not repeat.

## The Two Sectors and the Algebras They Use

**Two sectors, six algebras, three of them at the bottom.** The inventory comes first.

| sector | algebra | dimension | module | where it comes from |
|---|---|---|---|---|
| strong | $\mathfrak{su}(3)$ | $8$ | $\mathbb C^3\subset\mathbb C^4$ | posited on the triplet |
| strong, abelian | $\mathfrak u(1)_{B-L}$ | $1$ | the singlet line | the surviving $\mathrm{SU}(4)$ Cartan |
| electroweak, left | $\mathfrak{su}(2)_L$ | $3$ | $\mathbb C^2_L$ | the rotor algebra |
| electroweak, right | $\mathfrak{su}(2)_R$ | $3$ | $\mathbb C^2_R$ | the rotor algebra |
| electroweak, hypercharge | $\mathfrak u(1)_Y$ | $1$ | the whole generation | derived: $T_{3R}+\tfrac12(B-L)$ |
| electromagnetic | $\mathfrak u(1)_{\mathrm{em}}$ | $1$ | one dimension per charge | derived: $T_{3L}+Y$ |

**The reading of the table.** The strong sector is $\mathfrak{su}(3)\oplus\mathfrak u(1)_{B-L}$ at the intermediate stage and $\mathfrak{su}(3)$ alone at the bottom, because $B-L$ is absorbed into hypercharge. The electroweak sector is $\mathfrak{su}(2)_L\oplus\mathfrak{su}(2)_R\oplus\mathfrak u(1)_{B-L}$ at the intermediate stage and $\mathfrak{su}(2)_L\oplus\mathfrak u(1)_Y$ at the bottom. The electromagnetic sector is one $\mathfrak u(1)$.

## Colour: $\mathfrak{su}(3)$ on Three Dimensions

**Eight generators, one module, and a statement about what they can see.**

**2.1 The algebra.** $\mathfrak{su}(3)$ acts on $\mathbb C^3$, the triplet left by the split $\mathbf4\to\mathbf3\oplus\mathbf1$. Its eight generators are the two diagonal ($\lambda_3$, $\lambda_8$) and six off-diagonal Gell-Mann directions, and they annihilate the singlet line:

$$
\mathfrak{su}(3)=\{X\in\mathfrak{su}(4):\ X e_t=0\}.
$$

**2.2 The module.** The triplet is the module of the sector. Every quark field is a vector in it, every gluon is an endomorphism of it, and no strong-sector object carries an index outside it.

**2.3 What colour cannot see.** $\mathfrak{su}(3)$ is blind to the lepton line and blind to both weak factors. That blindness is not an accident of the embedding: it is the content of $X e_t=0$, which says the algebra annihilates the fourth direction. Every statement about colour blindness in the corpus reduces to that equation.

**2.4 Why the algebra is posited.** The biquaternion algebra has three imaginary units and its rotors form $\mathrm{SU}(2)$. It has no eight-dimensional compact real form, so no amount of reading the algebra produces $\mathfrak{su}(3)$ acting on three complex dimensions. Colour is therefore an input: the model declares a $\mathfrak{su}(3)$ on the triplet, and everything downstream is consistent with that declaration rather than derived from it. The full argument, with the dimension count that rules out the alternatives, is [Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)](why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html).

## Weak Isospin: Two Copies, Two Modules, One Algebra

**The isomorphism is not the physics.** This is the distinction the sector lives or dies by.

**3.1 The algebra.** $\mathfrak{su}(2)$ is spanned by three generators obeying $[T_a,T_b]=i\varepsilon_{abc}T_c$, and the model has two copies of it, one per weak factor. As abstract algebras the two are isomorphic; as subalgebras of $\mathfrak{su}(4)\oplus\mathfrak{su}(2)\oplus\mathfrak{su}(2)$ they are different subspaces.

**3.2 The two modules.** The left copy acts on $\mathbb C^2_L$, the right on $\mathbb C^2_R$, and the carrier sees neither: both weak factors are external to the $\mathbf4$ and act on the two-index structure $(\mathbf2,\mathbf1)$ and $(\mathbf1,\mathbf2)$. So the two copies are told apart by their modules and by nothing else.

**3.3 The rotor identification.** Each copy is the rotor algebra of the biquaternion algebra: a unit quaternion rotates, three imaginary units span the rotation algebra, and the group is $\mathrm{SU}(2)$. This is the one place where the two sectors differ in provenance: the weak algebras are read off the algebra, and the strong one is not.

**3.4 The parity exchange.** The two copies are exchanged by the $L\leftrightarrow R$ swap, which is parity in this frame. A model with one copy has parity violated explicitly; a model with two and a vacuum that treats them unequally has it violated spontaneously. That distinction is what makes the left–right model a different claim from the Standard Model, and it is [$\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$: Two Sides, Six Generators, One Group](su2l-times-su2r-two-sides-six-generators-one-group.html).

## The Abelian Factors

**Two of the three $\mathfrak u(1)$s are derived, and the third is a limit of them.**

**4.1 $B-L$, which is a Cartan direction.** It is not a factor of the top group: it is the diagonal of $\mathfrak{su}(4)$ orthogonal to $\mathfrak{su}(3)$,

$$
\mathfrak u(1)_{B-L}=\left\langle \operatorname{diag}(-1,\tfrac13,\tfrac13,\tfrac13)\right\rangle,
$$

and it becomes a factor only after the first breaking.

**4.2 $Y$, which is a diagonal subgroup of two factors.** Hypercharge is the span of

$$
T_{3R}+\tfrac12(B-L),
$$

so $\mathfrak u(1)_Y$ is a one-dimensional subspace of $\mathfrak{su}(2)_R\oplus\mathfrak u(1)_{B-L}$ and not a factor of anything. **Geometrically it is the diagonal subgroup along which the two phases turn together, with the $B-L$ parameter at half the rate of the $T_{3R}$ one**, and the weight $\tfrac12$ is not a second parameter: it is one number written on two normalisations of one direction. That is why the coupling $g_Y$ is not independent at the breaking scale: it is fixed by $g_R$ and $g_{B-L}$ through the normalisation of the combination, and the relation is in [The Gauge Connection Below the Breaking: Three Pieces, Three Couplings, and What Each Multiplies](the-gauge-connection-below-the-breaking-three-pieces-three-couplings-and-what-each-multiplies.html).

**The counting, which is the sharp form of the same statement.** Four generators survive to the Standard Model, and they draw on five raw directions.

| Standard Model generator | count | drawn from |
|---|---|---|
| $W^{1}_L,W^{2}_L,W^{3}_L$ | $3$ | $\mathrm{SU}(2)_L$, as a factor |
| $Y$ | $1$ | one direction of $\mathrm{SU}(2)_R$ and one of $\mathrm{SU}(4)$, mixed |

The surplus is not an error in the count. The two neutral raw directions span a plane; $Y$ is one direction in it; **the orthogonal direction is a physical state, the $Z_R$, which becomes massive at $M_R$.** The step $5\to4$ is therefore the step in which one gauge boson acquires a mass, and it happens entirely inside that plane.

**And the vacuum is a vector, not a line.** $T_{3R}$ gives $+\tfrac12$ on $v_R e_\uparrow$ and $B-L$ gives $-1$, so neither annihilates it; the kernel is the single combination $Y$. **The line count and the generator count disagree and both are right**: a doublet has one line up to phase, so the line stabiliser is $\mathrm{U}(1)_R$ and the step reads $3\to1$; the generator that survives is one of the four directions of $\mathfrak{su}(2)_R\oplus\mathfrak u(1)_{B-L}$, so the step reads $4\to1$. A stabiliser of a vector is smaller than the stabiliser of its line, and a scalar vacuum is a vector.

**4.3 $Q$, which is a combination of a combination.** The electric charge is the span of

$$
T_{3L}+Y=T_{3L}+T_{3R}+\tfrac12(B-L).
$$

It is the unique direction annihilated by both vacuum lines, which is why it survives: the two conditions $Q\Phi_0=0$ and $QH_0=0$ leave exactly one dimension among the five Cartan directions of $B-L$, $T_{3L}$ and $T_{3R}$.

**4.4 The rank budget, read as an algebra statement.** $3\to5\to4\to3$: the Cartan rank of the residual algebra, computed as the dimension of the maximal torus that survives. **The first step adds two directions**, because the two weak $\mathrm{SU}(2)$ factors arrive with the doublet index at $M_C$ and bring their Cartans with them, while the sextet that leaves is off-diagonal and removes no torus direction. The second removes $T_{3R}$; the third removes $T_{3L}$ and $Y$ and keeps their sum.

## The Photon on One Dimension

**The module of the last algebra is one-dimensional, and that is what "on one" means.**

**5.1 The module.** A $\mathrm{U}(1)$ acts on a one-dimensional complex space by a phase, $e^{i\alpha Q}$. So the module of $\mathfrak u(1)_{\mathrm{em}}$ is one complex dimension for each value of $Q$, and the algebra is a single number times the identity on it.

**5.2 Why this is not a triviality.** It fixes what the photon can and cannot do. It cannot change a charge, so it cannot connect two different species; it cannot change colour, so it commutes with $\mathfrak{su}(3)$; and it cannot change the generation, so it is diagonal in flavour. Every selection rule of electromagnetism is the one-dimensionality of the module written out.

**5.3 The photon as a direction in a three-dimensional space.** The algebra is one-dimensional, but the field that realises it is a particular vector in the three-dimensional neutral space spanned by $W^3_L$, $W^3_R$ and $B$. The one dimension of §*5.1* is the algebra's; the three-dimensional space is the neutral block's; and the map between them is the mixing. That is why "the photon is a mixture" and "the photon's algebra is one-dimensional" are both true and do not contradict: one statement is about the module, the other about the basis.

## What the Reduction Loses

**Six dimensions at the first step, six at the second and third.** The losses are not all of a kind.

**6.1 The first loss: colour-lepton mixing.** The six leptoquark directions of $\mathfrak{su}(4)/\left(\mathfrak{su}(3)\oplus\mathfrak u(1)\right)$ are the endomorphisms that map the lepton line to the triplet and back. They carry colour, they carry $B-L=\pm\tfrac43$, and no residual algebra contains them. Their module structure under the residual group is a coloured pair, which is why they can be integrated out covariantly rather than dropped: they form a module, not a set.

**6.2 The second loss: the right-handed charged pair.** $\mathfrak{su}(2)_R/\mathfrak u(1)_R$ is two-dimensional and carries $T_{3R}=\pm1$ in the adjoint. Below $M_R$ there is no operator that rotates the members of a right doublet into each other, so no mass term can be forbidden by that symmetry, and the observed splitting of the members is allowed.

**6.3 The third loss: the left-handed charged pair and the neutral mixing.** $\left(\mathfrak{su}(2)_L\oplus\mathfrak u(1)_Y\right)/\mathfrak u(1)_{\mathrm{em}}$ is four-dimensional: the two $W^{\pm}$ and the two directions that become $Z$ and the photon. The one that survives is the combination annihilating both vevs.

**6.4 What is not lost.** $\mathfrak{su}(3)$ and $\mathfrak u(1)_{\mathrm{em}}$ are subalgebras at every stage, and $B-L$ survives the first two steps. The corpus's claim that colour is a stabiliser at every scale is exactly the statement that $\mathfrak{su}(3)\subset\mathfrak h_i$ for all three $\mathfrak h_i$.

## The Checks

**Six checks.**

| check | computation | result |
|---|---|---|
| the dimensions | $8+1+3+3$ | $15$ |
| the second step | $15-3$ | $12$ |
| the third step | $12-3$ | $9$ |
| the rank | $\dim$ maximal torus | $3\to5\to4\to3$ |
| the annihilation | $Xe_t=0$ for $X\in\mathfrak{su}(3)$ | holds for all eight |
| the surviving direction | $Q\Phi_0=QH_0=0$ | one dimension among five |

## Distinctions That Are Easy to Lose

**Three pairs.**

**7.1 The algebra and the module.** $\mathfrak{su}(2)_L$ and $\mathfrak{su}(2)_R$ are isomorphic; the sectors are not. Every statement that treats the two as interchangeable is a statement about the algebra alone and is silent about the physics.

**7.2 Posited and derived.** Colour is posited, the weak factors are read off the rotors, hypercharge and charge are derived from the two. Mixing these three provenances is the commonest error in reading the model, and the corpus's own summary of it is [The $\mathrm{SU}(4)$ Model: Four Colours, Fifteen Generators, One Declaration](the-su4-model-four-colours-fifteen-generators-one-declaration.html).

**7.3 $\mathfrak u(1)$ as a factor and $\mathfrak u(1)$ as a direction.** $B-L$ is a factor between $M_C$ and $M_R$. $Y$ and $Q$ are never factors: they are directions in a product. A coupling can be assigned to a factor; a direction's coupling is a combination of the factors'.

## Summary

**The algebras.** $\mathfrak{su}(3)$ on $\mathbb C^3$, two $\mathfrak{su}(2)$ on the two doublets, and three $\mathfrak u(1)$ of which one is a factor and two are directions.

**The dimensions.** $15$ before and after the first step, then $12$, then $9$, with the rank $3\to5\to4\to3$: six leptoquarks leave as six weak generators arrive.

**The two derived charges.** $Y=T_{3R}+\tfrac12(B-L)$ and $Q=T_{3L}+Y$, each a one-dimensional subspace of the algebra above it.

**The photon.** A one-dimensional algebra acting on a one-dimensional module, realised by a particular direction in the three-dimensional neutral block.

**The provenance.** Weak algebras read off the rotors; colour posited; the two charges derived.

**What the reduction loses.** Six leptoquark directions, then the right charged pair, then the left charged pair and the neutral mixing.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathfrak{su}(3)$, $\mathfrak{su}(2)_L$, $\mathfrak{su}(2)_R$ | the non-abelian residual algebras |
| $\mathfrak u(1)_{B-L}$, $\mathfrak u(1)_Y$, $\mathfrak u(1)_{\mathrm{em}}$ | the three abelian directions |
| $\mathbb C^3$, $\mathbb C^2_L$, $\mathbb C^2_R$ | the modules the algebras act on |
| $T_{3L}$, $T_{3R}$, $B-L$ | the Cartan directions the charges are built from |
| $\mathfrak h_i$ | the unbroken algebra at each stage |
| $\mathrm{End}_{\mathbb C}(\mathbb B)$ | the frame the generators live in |

## Further Reading

- [Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)](why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html). The ceiling, with the dimension count that produces it.
- [$\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$: Two Sides, Six Generators, One Group](su2l-times-su2r-two-sides-six-generators-one-group.html). The two weak copies and the parity exchange.
- [The Electroweak Gauge Group and the Hypercharge Assignment in the Four Colours Left–Right Model: The Group and the Derived $Y$](the-electroweak-gauge-group-and-the-hypercharge-assignment.html). Hypercharge as an anomaly problem rather than a combination.
- [The Gauge Connection Below the Breaking: Three Pieces, Three Couplings, and What Each Multiplies](the-gauge-connection-below-the-breaking-three-pieces-three-couplings-and-what-each-multiplies.html). The couplings these algebras carry.
- [Quantum Chromodynamics as the Residual of $\mathrm{SU}(4)$: The Colour Wall, Restated](quantum-chromodynamics-as-the-residual-of-su4.html). The strong sector as the stabiliser's algebra.
- [The Death of the Primordial Force](the-death-of-the-primordial-force-the-id-condensate-and-the-six-carriers-it-eats.html). The dimension of the last residual algebra, counted as the massless spectrum.
