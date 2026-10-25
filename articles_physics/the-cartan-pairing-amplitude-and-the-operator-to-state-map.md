# __The Cartan Pairing, the Amplitude and the Operator-to-State Map__

## Introduction

Every nonzero operator in the algebra defines a state. The definition is one line, $\tilde Q\mapsto\tilde Q\tilde Q^{*}$, normalised by the trace. The state is not added to the operator from outside and the operator is not a state in disguise: the map forgets the unitary phase and keeps the positive amplitude. The Cartan pairing is the factorization that makes the forgetting explicit, $\tilde Q=\tilde H\tilde U$, with $\tilde H$ the amplitude and $\tilde U$ the phase.

The thesis is one sentence. **The map $\tilde Q\mapsto\tilde Q\tilde Q^{*}/2\langle\tilde Q,\tilde Q\rangle_{*}$ sends every nonzero operator to a state, the Cartan factor $\tilde H=\sqrt{\tilde Q\tilde Q^{*}}$ is that state's unnormalised amplitude, and the stratigraphy of the map is the stratigraphy of the algebra: the null cone goes to the pure states, the unitary group goes to the maximally mixed state, and the invertible elements in between go to the mixed states.** The last clause is the part that is easy to state and easy to get backwards: the reversible elements produce the most mixed states, and the zero divisors produce the pure ones.

The article is a synthesis of the Cartan pairing with the state space of the informational sector. It proves no new theorem. The factorisation is owned by *The Cartan Hermitian Pairing of the Polar Decomposition of Biquaternions*, the state space and the Born rule by the quantum-physics articles, and the modular Hamiltonian by the Tomita–Takesaki articles. What is added here is the map as a map: its fibre, its stratigraphy, its covariance, and the boundary of its name.

The name needs a warning at the start. The **operator-to-state map** is not the operator-state correspondence of a conformal field theory. There is no conformal boundary, no radial quantisation, no state–operator isomorphism and no Virasoro algebra in what follows. The map is the elementary algebraic one $\tilde Q\mapsto\tilde Q\tilde Q^{*}$, and the name is used only because it says what the map does.

The conventions are those of *Conventions in the Biquaternion Universe*. The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong M_2(\mathbb{C})$, the Hermitian form is $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$, the trace is $\operatorname{Tr}\tilde Q=2\operatorname{Sc}\tilde Q=2Q_t$, and a state is $\tilde{Ϛ}\in\mathbb{M}_+$ with $\operatorname{Tr}\tilde{Ϛ}=1$, that is, $\tilde{Ϛ}=\tfrac12(e_t+i\vec r)$ with $\lvert\vec r\rvert\le1$.

## The Results It Uses

| result | established in | used here for |
|---|---|---|
| the Cartan pairing, its theorem and its domain | [*The Cartan Hermitian Pairing of the Polar Decomposition of Biquaternions*](../articles_maths/the-cartan-hermitian-pairing-of-the-polar-decomposition-of-biquaternions.html), §*The Statement*, §*The Domain* | $\tilde Q=\tilde H\tilde U$, $\tilde H=\sqrt{\tilde Q\tilde Q^{*}}$ |
| the positive cone and the Hermitian square root | [*Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*](../articles_maths/positivity-and-the-hermitian-cone-of-the-biquaternion-algebra-with-hermitian-adjoint.html), §*The Polar Decomposition* | existence and uniqueness of $\tilde H\ge0$ |
| the generalized pairing on the null cone | [*The Polar Decomposition of an N-Degenerate Biquaternion*](../articles_maths/the-polar-decomposition-of-an-n-degenerate-biquaternion.html), §*The Two-Factor Decomposition* | the rank-one case and the partial isometry |
| the state space, the Bloch ball and the Born rule | [*Quantum Physics in Biquaternionic Form*](quantum-physics-in-biquaternionic-form.html), §*States* | the normalisation and the trace-one condition |
| the trace reading of the Born weight | [*The Born Rule from the Hermitian Form*](the-born-rule-as-a-trace-formula-derivation-and-comparison.html), §*The Trace Reading and Normalisation* | $\operatorname{Tr}(\tilde Q\tilde Q^{*})=2\langle\tilde Q,\tilde Q\rangle_{*}$ |
| the modular Hamiltonian of a faithful state | [*The Modular Hamiltonian in Biquaternionic Form*](the-modular-hamiltonian-in-biquaternionic-form.html), §*Definition from the Modular Operator* | $\tilde K_{\mathrm{mod}}=-\ln\tilde{Ϛ}$ |

## The Map

For $\tilde Q\in\mathbb{B}$ with $\tilde Q\neq0$ define

$$
\boxed{\;\tilde{Ϛ}_Q=\frac{\tilde Q\tilde Q^{*}}{2\langle\tilde Q,\tilde Q\rangle_{*}},
\qquad
\langle\tilde Q,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde Q\tilde Q^{*})=\sum_\mu\lvert Q_\mu\rvert^{2}>0\;}.
$$

The image is Hermitian, positive semidefinite and normalised by $\langle\tilde{Ϛ}_Q,e_t\rangle_{*}=\tfrac12$, so it is a state. The denominator is the Hermitian bracket and not a trace: the star names the form that is positive definite on the whole algebra, and the trace is its $2\times2$ reading, $\operatorname{Tr}=2\,\mathrm{Sc}$. The factor cancels in every probability, because a probability is a ratio of the same bracket.

The map is defined for every nonzero element, including the zero divisors. It is not defined at $\tilde Q=0$, where the numerator and the denominator vanish together. There is no limiting state at the origin: along different directions the limit depends on the direction, and the origin has no state.

Three elementary properties fix the map.

- **Right invariance.** For unitary $\tilde W$, $\tilde Q\tilde W$ has the same image, because $(\tilde Q\tilde W)(\tilde Q\tilde W)^{*}=\tilde Q\tilde W\tilde W^{*}\tilde Q^{*}=\tilde Q\tilde Q^{*}$. The unitary right factor is the phase that the map forgets.
- **Left covariance.** For unitary $\tilde V$, the image of $\tilde V\tilde Q$ is $\tilde V\tilde{Ϛ}_Q\tilde V^{*}$. A left unitary is a change of frame, and it rotates the state rather than leaving it fixed.
- **Normalisation.** $\langle\tilde{Ϛ}_Q,e_t\rangle_{*}=\tfrac12$ and $\tilde{Ϛ}_Q\ge0$, so the image is a state and not merely a positive element.

The distinction between the two sides is the whole content of the Cartan factorization. The right unitary is the fibre; the left unitary is the frame.

## The Amplitude and the State

Write the Cartan factorization of a nonzero element as

$$
\tilde Q=\tilde H\tilde U,\qquad \tilde H=\sqrt{\tilde Q\tilde Q^{*}}\ge0,\qquad \tilde U=\tilde H^{+}\tilde Q .
$$

Then

$$
\boxed{\;\tilde{Ϛ}_Q=\frac{\tilde H^{2}}{2\langle\tilde H,\tilde H\rangle_{*}},
\qquad
\hat H=\frac{\tilde H}{\sqrt{2\langle\tilde H,\tilde H\rangle_{*}}},
\qquad
\tilde{Ϛ}_Q=\hat H^{2}\;}.
$$

The **amplitude** is $\tilde H$; the **normalised amplitude** is $\hat H$; the **state** is the square of the normalised amplitude. The three objects are different. $\tilde H$ carries the scale of the operator; $\hat H$ is normalised in the Hilbert–Schmidt sense, $\langle\hat H,\hat H\rangle_{*}=\tfrac12$, which is $\operatorname{Tr}\hat H^{2}=1$ in the matrix image; $\tilde{Ϛ}_Q$ is the state, with $\langle\tilde{Ϛ}_Q,e_t\rangle_{*}=\tfrac12$.

The eigenvalues of $\tilde H$ are the singular values $\sigma_1\ge\sigma_2\ge0$ of $\tilde Q$. The eigenvalues of the state are their normalised squares,

$$
p_i=\frac{\sigma_i^{2}}{\sigma_1^{2}+\sigma_2^{2}},
\qquad p_1+p_2=1 .
$$

So the state is the **normalised squared singular-value distribution** of the operator. This is the precise sense in which the state is the positive data of the operator: it keeps the singular values and discards the unitary factor.

### What the Amplitude Is Not

The amplitude is not the state, and the state is not the amplitude. Three distinctions are worth stating because the corpus uses the words loosely.

- $\tilde H$ is not a state: its trace is not one in general, and it is the square root of the unnormalised state.
- $\tilde H^{2}$ is not a state either: it is positive but its bracket with the unit is $2\langle\tilde Q,\tilde Q\rangle_{*}$, which is $\tfrac12$ only after normalisation.
- $\hat H$ is not a state: it is a positive operator of Hilbert–Schmidt norm one, and its square is the state.

The chain is $\tilde Q\rightsquigarrow\tilde H\rightsquigarrow\hat H\rightsquigarrow\tilde{Ϛ}_Q$, and each arrow loses information: the first forgets $\tilde U$, the second forgets the scale, the third squares.

## Purity Is the Spread of the Singular Values

The purity of the state is

$$
\boxed{\;\operatorname{Tr}\tilde{Ϛ}_Q^{2}
=\frac{\sigma_1^{4}+\sigma_2^{4}}{(\sigma_1^{2}+\sigma_2^{2})^{2}}
=\frac{1}{2}+\frac{(\sigma_1^{2}-\sigma_2^{2})^{2}}{2(\sigma_1^{2}+\sigma_2^{2})^{2}}\;}.
$$

The second form shows the range at once: $\tfrac12\le\operatorname{Tr}\tilde{Ϛ}_Q^{2}\le1$, with equality at the two ends.

| case | singular values | purity | state | operator |
|---|---|---|---|---|
| equal | $\sigma_1=\sigma_2>0$ | $\tfrac12$ | maximally mixed | unitary up to scale |
| intermediate | $\sigma_1>\sigma_2>0$ | between | mixed | invertible, not unitary up to scale |
| one vanishing | $\sigma_1>0$, $\sigma_2=0$ | $1$ | pure | rank one, a zero divisor |

The table is the stratigraphy of the map. It is worth reading against the intuition that reversible elements should correspond to pure states.

- **The unitary group goes to the maximally mixed state.** If $\tilde Q=c\tilde U$ with $\tilde U$ unitary, then $\tilde Q\tilde Q^{*}=\lvert c\rvert^{2}e_t$ and $\tilde{Ϛ}_Q=\tfrac12 e_t$. The most reversible elements produce the least information-bearing state.
- **The null cone goes to the pure states.** If $\tilde Q\neq0$ and $N=\langle\tilde Q\rangle_{\natural}=0$, then $\det(\tilde Q\tilde Q^{*})=\lvert N\rvert^{2}=0$, so $\tilde Q\tilde Q^{*}$ has rank one and the state is pure. Conversely, a pure image forces $\operatorname{rank}\tilde Q=1$, hence $N=0$. **The nonzero zero divisors are exactly the operators that define pure states.**
- **The interior goes to the mixed states.** An invertible element that is not a scalar unitary has two distinct singular values and a state strictly between pure and maximally mixed.

The identification of the cone with the pure states is exact and is the strongest statement in the article. It is also the one that connects the map to measurement: a sharp outcome is a zero divisor, and its state is pure; a weak outcome is invertible, and its state is mixed; a unitary evolution is a scalar unitary, and its state is maximally mixed. The three strata of *The Polar Decomposition of a Kraus Operator* are the three rows of this table, read through the map.

## The Phase and the Fibre

The Cartan factorization writes $\tilde Q=\tilde H\tilde U$ with $\tilde U$ unitary. The map keeps $\tilde H$ and discards $\tilde U$. The fibre over a state is therefore the set of operators with the same $\tilde H$, that is,

$$
\{\tilde H\tilde W:\ \tilde W\ \text{unitary}\},
$$

which is a $\mathrm{U}(2)$ torsor when $\tilde H>0$ and a smaller orbit when $\tilde H$ is rank one. The phase is not a gauge field and not a physical field: it is the coordinate along the fibre. Choosing a representative of each fibre is choosing a section of the map, and the Cartan factorization is the canonical section $\tilde U=\tilde H^{-1}\tilde Q$ when $\tilde H$ is invertible.

This gives a clean statement of what a **gauge choice** is in this language. A gauge transformation acts on the right, $\tilde Q\mapsto\tilde Q\tilde W$, and leaves the state fixed. A change of frame acts on the left, $\tilde Q\mapsto\tilde V\tilde Q$, and rotates the state. The two are not the same operation, and confusing them is the common error. Gauge freedom is the fibre; frame freedom is the base.

The fibre also shows why the map cannot be inverted. A state determines the normalised amplitude $\hat H$ uniquely, because the positive square root is unique, but it determines neither $\tilde U$ nor the scale of $\tilde H$. Two operators with the same singular values and different unitary factors define the same state and the same amplitude, with different Cartan phases: the state is blind to the phase.

### The Reversed Reading

The Cartan factorization of the **adjoint** element is

$$
\tilde Q^{*}=\tilde U^{*}\tilde H,
$$

which is the right polar decomposition, not the left one. Its first factor is $\tilde U^{*}\tilde H\tilde U$, a rotation of $\tilde H$, and its second factor is $\tilde U^{*}$. The state of $\tilde Q^{*}$ is the same as the state of $\tilde Q$, because $\tilde Q^{*}(\tilde Q^{*})^{*}=\tilde Q^{*}\tilde Q$, which is $\tilde U^{*}\tilde H^{2}\tilde U$ and has the same spectrum. The map is blind to the side on which the phase stands; only the singular values survive.

## The Modular Reading

For a faithful state, $\tilde{Ϛ}_Q>0$, the modular Hamiltonian is defined by

$$
\tilde K_{\mathrm{mod}}=-\ln\tilde{Ϛ}_Q=-2\ln\hat H
=-2\ln\tilde H+\ln\!\bigl(2\langle\tilde H,\tilde H\rangle_{*}\bigr)e_t .
$$

The last term is central and is the additive constant that a modular Hamiltonian always carries. The amplitude is therefore the square root of the state, and its logarithm is minus half the modular Hamiltonian up to that constant. This is the exact sense in which the Cartan amplitude is the modular square root.

Two boundaries must be kept.

- The modular **conjugation** is anti-unitary and is not the Cartan factor $\tilde U$. The Tomita–Takesaki conjugation depends on the state and on the algebra; the Cartan factor is the unitary quotient of the operator. They are different objects and the notation must not identify them.
- The modular reading needs $\tilde{Ϛ}_Q>0$, hence $\tilde H>0$, hence $\tilde Q$ invertible. On the null cone the state is pure, the logarithm diverges and the modular Hamiltonian does not exist. The purity table and the modular table have the same boundary.

## Where the Map Appears

The map is not an extra structure added to the theory; it is the common form of four constructions that the corpus already uses.

| object | operator | state it defines | article |
|---|---|---|---|
| measurement outcome | Kraus operator $\tilde K_y$ | $\tilde K_y\tilde{Ϛ}\tilde K_y^{*}/p_y$ | [*The Polar Decomposition of a Kraus Operator*](the-polar-decomposition-of-a-kraus-operator-effect-backaction-and-the-measurement-boundary.html) |
| polarization | Jones matrix $\tilde J$ | the normalized $\tilde J\tilde J^{*}$, the output coherency | [*Pancharatnam's Phase and the Polarization Sphere*](pancharatnams-phase-and-the-polarization-sphere-in-biquaternionic-form.html) |
| scattering | S-matrix element $\tilde S$ | the normalized $\tilde S\tilde S^{*}$ | [*The S-Matrix in Biquaternionic Form*](the-s-matrix-in-biquaternionic-form.html) |
| field | field strength $\tilde F$ | the normalized $\tilde F\tilde F^{*}$, an energy–momentum direction | [*The Field Strength Biquaternion and Its Invariants*](the-field-strength-biquaternion-and-its-invariants.html) |

In each row the map is the same and the physical name of the state is different. The measurement row adds a conditioning on the initial state; the polarization row reads the state as a coherency matrix; the scattering row reads it as the state produced by an interaction; the field row reads it as the direction of the energy–momentum element. The unity is algebraic, and the differences are in the interpretation of the operator.

One caution about the measurement row. The map of this article takes an operator to a state without an input. The post-measurement state of an instrument takes an operator and an input state, $\tilde{Ϛ}\mapsto\tilde K\tilde{Ϛ}\tilde K^{*}/p$. The two coincide only when the input is the maximally mixed state, $\tilde{Ϛ}=\tfrac12 e_t$, in which case the output is proportional to $\tilde K\tilde K^{*}$. The operator-to-state map is the input-free shadow of the instrument, not the instrument itself.

## The Name

The phrase "operator-to-state map" is used in two unrelated senses in the literature.

- In **conformal field theory**, the operator-state correspondence is a theorem of radial quantisation: a local operator at the origin defines a state on the boundary sphere, and the map is an isomorphism of Hilbert spaces with a Virasoro action. It needs a conformal boundary, a radial time and a state–operator isomorphism.
- In **this article**, the map is $\tilde Q\mapsto\tilde Q\tilde Q^{*}$, defined on a finite-dimensional algebra, with no boundary, no radial time and no isomorphism. It is a many-to-one map onto the state space, and its fibre is a unitary orbit.

The two share a name and nothing else. The corpus states the disclaimer wherever the name appears, because the CFT phrase would be a false citation. There is no conformal field theory in the biquaternion framework, and this article does not introduce one.

## Physical Interpretation

The map gives the informational sector its ontology in one line: **an operator is an amplitude and a phase, and the state is the squared amplitude.** The amplitude is what the operator does to norms; the phase is what it does to phases; the state is what remains when the phase is forgotten.

The stratigraphy is the physical content.

- A **pure state** comes from a rank-one operator, and rank-one operators are the zero divisors. The sharp measurement, the polarizer and the null field all live on the cone for this reason. Purity is not an idealisation imposed on the state; it is the image of a degenerate operator.
- A **maximally mixed state** comes from a unitary operator up to scale. The reversible evolutions are exactly the operators whose image is the least informative state. This is the algebraic form of the statement that a unitary carries no information about a preferred basis.
- A **mixed state** comes from an invertible operator with two distinct singular values. The mixedness measures the spread of the singular values, hence the anisotropy of the operator.

Read as a whole, the table is a dictionary between the algebra's rank stratication and the state space's purity stratication. It is exact in both directions, and it is the reason the measurement, polarization and scattering articles can share one grammar.

## What This Does Not Claim

- It does not claim the operator-state correspondence of a conformal field theory. There is no boundary, no radial quantisation and no isomorphism.
- It does not claim that every state arises from a unique operator. The map is many-to-one, and the fibre is the unitary right factor.
- It does not claim that the amplitude $\tilde H$ is a state, or that the state $\tilde{Ϛ}_Q$ is an amplitude. The chain is $\tilde Q\rightsquigarrow\tilde H\rightsquigarrow\hat H\rightsquigarrow\tilde{Ϛ}_Q$, and each step loses information.
- It does not claim a modular reading on the null cone. The modular Hamiltonian needs a faithful state and diverges at purity.
- It does not claim that the map is a channel, an instrument or a dynamics. It is a map from operators to states, with no input state and no time.
- It does not claim that the purity table is a classification of physical processes. It is a classification of operators, read through the map.

## Summary

- Every nonzero biquaternion defines a state by $\tilde{Ϛ}_Q=\tilde Q\tilde Q^{*}/2\langle\tilde Q,\tilde Q\rangle_{*}$.
- The Cartan amplitude $\tilde H=\sqrt{\tilde Q\tilde Q^{*}}$ is the unnormalised square root of that state; the state is $\hat H^{2}$ with $\hat H$ the bracket-normalised amplitude.
- The eigenvalues of $\tilde H$ are the singular values of $\tilde Q$, and the state's eigenvalues are their normalised squares.
- The purity is $\tfrac12+(\sigma_1^{2}-\sigma_2^{2})^{2}/2(\sigma_1^{2}+\sigma_2^{2})^{2}$, between $\tfrac12$ and $1$.
- The null cone maps onto the pure states, the unitary group onto the maximally mixed state, and the invertible interior onto the mixed states.
- The map is right-invariant under unitary multiplication (the gauge fibre) and left-covariant (the frame rotation).
- The modular Hamiltonian is $-2\ln\hat H$, with a central additive constant; the modular conjugation is not the Cartan phase.
- The map is the input-free shadow of the instrument and the common form of the Kraus, Jones, S-matrix and field-strength constructions.
- The name is not the CFT operator-state correspondence.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde Q\tilde Q^{*}$ | the positive square whose normalisation is the state |
| $\tilde{Ϛ}_Q$ | the state defined by $\tilde Q$, trace one |
| $\tilde H=\sqrt{\tilde Q\tilde Q^{*}}$ | the Cartan amplitude, Hermitian positive |
| $\hat H=\tilde H/\sqrt{2\langle\tilde H,\tilde H\rangle_{*}}$ | the normalised amplitude, $\langle\hat H,\hat H\rangle_{*}=\tfrac12$ |
| $\sigma_1\ge\sigma_2\ge0$ | the singular values of $\tilde Q$, the eigenvalues of $\tilde H$ |
| $p_i=\sigma_i^{2}/(\sigma_1^{2}+\sigma_2^{2})$ | the state's eigenvalues |
| $\operatorname{Tr}\tilde{Ϛ}_Q^{2}$ | the purity, between $\tfrac12$ and $1$ |
| $\tilde U=\tilde H^{+}\tilde Q$ | the unitary phase, the coordinate along the fibre |
| $\tilde K_{\mathrm{mod}}=-\ln\tilde{Ϛ}_Q$ | the modular Hamiltonian of a faithful state |
| $\operatorname{Tr}\tilde Q=2\operatorname{Sc}\tilde Q=2Q_t$ | the trace |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$ | the Hermitian form |

## Further Reading

- [The Cartan Hermitian Pairing of the Polar Decomposition of Biquaternions](../articles_maths/the-cartan-hermitian-pairing-of-the-polar-decomposition-of-biquaternions.html), for the theorem, the uniqueness and the domain.
- [The Polar Decomposition of an N-Degenerate Biquaternion](../articles_maths/the-polar-decomposition-of-an-n-degenerate-biquaternion.html), for the rank-one case and the partial isometry.
- [Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint](../articles_maths/positivity-and-the-hermitian-cone-of-the-biquaternion-algebra-with-hermitian-adjoint.html), for the positive cone and the square root.
- [The Three Polar Factors of a Biquaternion: Frame, Mass and State](the-three-polar-factors-of-a-biquaternion-frame-mass-and-state.html), for the comparison of the three first factors.
- [The Polar Decomposition of a Kraus Operator](the-polar-decomposition-of-a-kraus-operator-effect-backaction-and-the-measurement-boundary.html), for the measurement reading of the three strata.
- [Quantum Physics in Biquaternionic Form](quantum-physics-in-biquaternionic-form.html), for the state space and the Born rule.
- [The Modular Hamiltonian in Biquaternionic Form](the-modular-hamiltonian-in-biquaternionic-form.html), for the modular operator and the Tomita–Takesaki conjugation.
- [The Ontology of the Quantum State under the Biquaternion Framework](the-ontology-of-the-quantum-state-under-the-biquaternion-framework.html), for the state as the Hermitian square.
- M.-D. Choi, "Completely positive linear maps on complex matrices," *Linear Algebra and its Applications* **10** (1975) 285–290, for the structure of positive maps in two dimensions.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the polar decomposition, the fidelity and the purity.
