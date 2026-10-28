# __The General Polar Decomposition, the Amplitude and the Operator-to-State Map__

## Introduction

Every nonzero operator in the algebra defines a state. The definition is one line, $\tilde Q\mapsto\tilde Q\tilde Q^{*}$, normalised by the trace. The state is not added to the operator from outside and the operator is not a state in disguise: the map forgets the unitary phase and the overall scale and keeps the normalised positive amplitude. The **general polar decomposition** is the factorization that makes the forgetting explicit, $\tilde Q=\tilde Q_H\tilde Q_0$, with $\tilde Q_H=\sqrt{\tilde Q\tilde Q^{*}}\ge0$ the amplitude and $\tilde Q_0=\tilde Q_H^{+}\tilde Q$ the phase; the state is the square of the normalised $\tilde Q_H$. It is the **H-norm** statement, defined for every nonzero element, and on the null cone $\tilde Q_0$ is a partial isometry. The N-norm refinement, where $\tilde Q_H$ is positive definite and $\tilde Q_0$ is unitary, is the **Cartan pairing**; it exists only where $\langle\tilde Q\rangle_{\natural}\neq0$. The four-factor word is that refinement read in *The Polar Decomposition and Its Three Pairings*.

The thesis is one sentence. **The map $\tilde Q\mapsto\tilde Q\tilde Q^{*}/2\langle\tilde Q,\tilde Q\rangle_{*}$ sends every nonzero operator to a state, the positive factor $\tilde Q_H=\sqrt{\tilde Q\tilde Q^{*}}$ is that state's unnormalised amplitude, and the stratigraphy of the map is the stratigraphy of the algebra: the punctured null cone goes to the pure states, the unitary group up to scale goes to the maximally mixed state, and the invertible elements in between go to the mixed states.** The last clause is the part that is easy to state and easy to get backwards: the reversible elements produce the most mixed states, and the zero divisors produce the pure ones.

The article is a synthesis of the general polar decomposition with the state space of the informational sector. It proves no new theorem. The general two-factor decomposition, its Moore–Penrose inverse and the partial isometry on the cone are owned by *The Polar Decomposition of a Biquaternion*; its N-regular sharpening, where the second factor is unitary, by *The Cartan Hermitian Pairing of the Polar Decomposition of Biquaternions*; the state space and the Born rule by the quantum-physics articles; and the modular Hamiltonian by the Tomita–Takesaki articles. What is added here is the map as a map: its fibre, its stratigraphy, its covariance, and the boundary of its name.

The name needs a warning at the start. The **operator-to-state map** is not the operator-state correspondence of a conformal field theory. There is no conformal boundary, no radial quantisation, no state–operator isomorphism and no Virasoro algebra in what follows. The map is the elementary algebraic one $\tilde Q\mapsto\tilde Q\tilde Q^{*}$, and the name is used only because it says what the map does.

**The two decompositions.** The general decomposition is not the Cartan pairing. The word $\tilde Q=\tilde Q_H\tilde Q_0$ with $\tilde Q_H\ge0$ and $\tilde Q_0$ a partial isometry is the general H-norm polar decomposition of *The Polar Decomposition of a Biquaternion*, defined on every nonzero element. The **Cartan pairing** is its N-regular restriction, where $\tilde Q_H$ is positive definite and $\tilde Q_0$ is unitary; it is defined only on $\langle\tilde Q\rangle_{\natural}\neq0$ and is owned by *The Cartan Hermitian Pairing of the Polar Decomposition of Biquaternions*. The two coincide off the null cone and differ on it, where the Cartan theorem does not apply. The physics articles that use the general form also call it the **generalized Cartan pairing**; the name is a usage, not a theorem, and this article reserves *Cartan* for the unitary case.

The conventions are those of *Conventions in the Biquaternion Universe*. The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong M_2(\mathbb{C})$, the Hermitian form is $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$, the trace is $\operatorname{Tr}\tilde Q=2\operatorname{Sc}\tilde Q=2Q_t$, and a state is $\tilde{Ϛ}\in\mathbb{M}_+$ with $\operatorname{Tr}\tilde{Ϛ}=1$, that is, $\tilde{Ϛ}=\tfrac12(e_t+i\vec r)$ with $\lvert\vec r\rvert\le1$.

## The Results It Uses

| result | established in | used here for |
|---|---|---|
| the general two-factor decomposition, the Moore–Penrose inverse and the partial isometry | [*The Polar Decomposition of a Biquaternion*](../articles_maths/the-polar-decomposition-of-a-biquaternion.html), §*The Moore–Penrose Inverse of the Hermitian Factor*, §*The Isometry Factor* | $\tilde Q=\tilde Q_H\tilde Q_0$ for every nonzero element, and the cone case |
| the Cartan pairing on the N-regular set, its theorem and its domain | **The Cartan Hermitian Pairing of the Polar Decomposition of Biquaternions**, §*The Statement*, §*The Domain* | the unitary second factor off the cone |
| the positive cone and the Hermitian square root | [*Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*](../articles_maths/positivity-and-the-hermitian-cone-of-the-biquaternion-algebra-with-hermitian-adjoint.html), §*The Polar Decomposition* | existence and uniqueness of $\tilde Q_H\ge0$ |
| the rank-one case and the partial isometry on the null cone | [*The Polar Decomposition of a Biquaternion*](../articles_maths/the-polar-decomposition-of-a-biquaternion.html), §*The Isometry Factor*, §*Examples* | the cone case of the same general pair |
| the state space, the Bloch ball and the Born rule | [*Quantum Physics in Biquaternionic Form*](quantum-physics-in-biquaternionic-form.html), §*States* | the normalisation and the trace-one condition |
| the trace reading of the Born weight | [*The Born Rule from the Hermitian Form — Derivation and Comparison*](the-born-rule-as-a-trace-formula-derivation-and-comparison.html), §*The Trace Reading and Normalisation* | $\operatorname{Tr}(\tilde Q\tilde Q^{*})=2\langle\tilde Q,\tilde Q\rangle_{*}$ |
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

Four elementary properties fix the map.

- **Right invariance.** For unitary $\tilde W$, $\tilde Q\tilde W$ has the same image, because $(\tilde Q\tilde W)(\tilde Q\tilde W)^{*}=\tilde Q\tilde W\tilde W^{*}\tilde Q^{*}=\tilde Q\tilde Q^{*}$. The unitary right factor is the phase that the map forgets.
- **Scale invariance.** For nonzero complex $\lambda$, $\lambda\tilde Q$ has the same image, because $(\lambda\tilde Q)(\lambda\tilde Q)^{*}=\lvert\lambda\rvert^{2}\tilde Q\tilde Q^{*}$ and the denominator carries the same factor. The overall scale is the second coordinate that the map forgets.
- **Left covariance.** For unitary $\tilde V$, the image of $\tilde V\tilde Q$ is $\tilde V\tilde{Ϛ}_Q\tilde V^{*}$. A left unitary is a change of frame, and it rotates the state rather than leaving it fixed.
- **Normalisation.** $\langle\tilde{Ϛ}_Q,e_t\rangle_{*}=\tfrac12$ and $\tilde{Ϛ}_Q\ge0$, so the image is a state and not merely a positive element.

The distinction between the two sides is the whole content of the general polar factorization. The right unitary and the scale are the fibre; the left unitary is the frame.

## The Amplitude and the State

Write the general polar factorization of a nonzero element as

$$
\tilde Q=\tilde Q_H\tilde Q_0,\qquad \tilde Q_H=\sqrt{\tilde Q\tilde Q^{*}}\ge0,\qquad \tilde Q_0=\tilde Q_H^{+}\tilde Q .
$$

Off the null cone this is the Cartan pairing, with $\tilde Q_H>0$ and $\tilde Q_0=\tilde Q_H^{-1}\tilde Q$ unitary. Then

$$
\boxed{\;\tilde{Ϛ}_Q=\frac{\tilde Q_H^{2}}{2\langle\tilde Q_H,\tilde Q_H\rangle_{*}},
\qquad
\tilde Q_{\mathrm n}=\frac{\tilde Q_H}{\sqrt{2\langle\tilde Q_H,\tilde Q_H\rangle_{*}}},
\qquad
\tilde{Ϛ}_Q=\tilde Q_{\mathrm n}^{2}\;}.
$$

The **amplitude** is $\tilde Q_H$; the **normalised amplitude** is $\tilde Q_{\mathrm n}$; the **state** is the square of the normalised amplitude. The three objects are different. $\tilde Q_H$ carries the scale of the operator; $\tilde Q_{\mathrm n}$ is normalised in the Hilbert–Schmidt sense, $\langle\tilde Q_{\mathrm n},\tilde Q_{\mathrm n}\rangle_{*}=\tfrac12$, which is $\operatorname{Tr}\tilde Q_{\mathrm n}^{2}=1$ in the matrix image; $\tilde{Ϛ}_Q$ is the state, with $\langle\tilde{Ϛ}_Q,e_t\rangle_{*}=\tfrac12$.

The eigenvalues of $\tilde Q_H$ are the singular values $\sigma_1\ge\sigma_2\ge0$ of $\tilde Q$. The eigenvalues of the state are their normalised squares,

$$
p_i=\frac{\sigma_i^{2}}{\sigma_1^{2}+\sigma_2^{2}},
\qquad p_1+p_2=1 .
$$

So the state is the **normalised squared singular-value distribution** of the operator. This is the precise sense in which the state is the positive data of the operator: it keeps the singular values and discards the unitary factor.

### What the Amplitude Is Not

The amplitude is not the state, and the state is not the amplitude. Three distinctions are worth stating because the corpus uses the words loosely.

- $\tilde Q_H$ is not a state: its trace is not one in general, and it is the square root of the unnormalised state.
- $\tilde Q_H^{2}$ is not a state either: it is positive but its bracket with the unit is $\langle\tilde Q,\tilde Q\rangle_{*}$, which is $\tfrac12$ only after normalisation.
- $\tilde Q_{\mathrm n}$ is not a state: it is a positive operator of Hilbert–Schmidt norm one, and its square is the state.

The chain is $\tilde Q\rightsquigarrow\tilde Q_H\rightsquigarrow\tilde Q_{\mathrm n}\rightsquigarrow\tilde{Ϛ}_Q$, and each arrow loses information: the first forgets $\tilde Q_0$, the second forgets the scale, the third squares.

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

- **The unitary group goes to the maximally mixed state.** If $\tilde Q=c\tilde Q_0$ with $\tilde Q_0$ unitary, then $\tilde Q\tilde Q^{*}=\lvert c\rvert^{2}e_t$ and $\tilde{Ϛ}_Q=\tfrac12 e_t$. The most reversible elements produce the least information-bearing state.
- **The null cone goes to the pure states.** If $\tilde Q\neq0$ and $N=\langle\tilde Q\rangle_{\natural}=0$, then $\det(\tilde Q\tilde Q^{*})=\lvert N\rvert^{2}=0$, so $\tilde Q\tilde Q^{*}$ has rank one and the state is pure. Conversely, a pure image forces $\operatorname{rank}\tilde Q=1$, hence $N=0$. **The nonzero zero divisors are exactly the operators that define pure states.**
- **The interior goes to the mixed states.** An invertible element that is not a scalar unitary has two distinct singular values and a state strictly between pure and maximally mixed.

The identification of the cone with the pure states is exact and is the strongest statement in the article. It is also the one that connects the map to measurement: a sharp outcome is a zero divisor, and its state is pure; a weak outcome is invertible, and its state is mixed; a unitary evolution is a scalar unitary, and its state is maximally mixed. The three strata of *The Polar Decomposition of a Kraus Operator* are the three rows of this table, read through the map.

## The Phase and the Fibre

Off the null cone the general polar factorization writes $\tilde Q=\tilde Q_H\tilde Q_0$ with $\tilde Q_0$ unitary, which is the Cartan pairing; on the cone $\tilde Q_0$ is a partial isometry. The map keeps the normalised amplitude $\tilde Q_{\mathrm n}=\tilde Q_H/\sqrt{2\langle\tilde Q_H,\tilde Q_H\rangle_{*}}$ and discards both $\tilde Q_0$ and the scale of $\tilde Q_H$. The fibre over a state is therefore

$$
\{c\,\tilde Q_{\mathrm n}\tilde W:\ c>0,\ \tilde W\ \text{unitary}\},
$$

off the cone, a $\mathrm{U}(2)$ torsor times a positive scale when $\tilde Q_{\mathrm n}>0$, and on the cone the same set with $\tilde W$ a partial isometry with the same final projection. The phase is not a gauge field and not a physical field: it is one coordinate along the fibre, and the scale is the other. Choosing a representative of each fibre is choosing a section of the map, and the factorization is the canonical section $\tilde Q_0=\tilde Q_H^{-1}\tilde Q$ when $\tilde Q_H$ is invertible.

This gives a clean statement of what a **gauge choice** is in this language. A gauge transformation acts on the right by a unitary, $\tilde Q\mapsto\tilde Q\tilde W$, and leaves the state fixed. A change of frame acts on the left by a unitary, $\tilde Q\mapsto\tilde V\tilde Q$, and rotates the state. The two are not the same operation, and confusing them is the common error. Gauge freedom is the unitary part of the fibre; the scale is the other fibre coordinate; frame freedom is the base.

The fibre also shows why the map cannot be inverted. A state determines the normalised amplitude $\tilde Q_{\mathrm n}$ uniquely, because the positive square root is unique, but it determines neither $\tilde Q_0$ nor the scale of $\tilde Q_H$. Two operators whose singular values are proportional and whose unitary factors differ, or whose partial isometries on the cone differ, define the same state and the same normalised amplitude, with phases and scales that need not agree: the state is blind to the phase and to the overall scale.

### The Reversed Reading

The general polar factorization of the **adjoint** element is

$$
\tilde Q^{*}=\tilde Q_0^{*}\tilde Q_H,
$$

which is the right polar decomposition. Written in the same left form as $\tilde Q$, it is $\tilde Q^{*}=(\tilde Q_0^{*}\tilde Q_H\tilde Q_0)\tilde Q_0^{*}$, with first factor $\tilde Q_0^{*}\tilde Q_H\tilde Q_0$, a rotation of $\tilde Q_H$, and second factor $\tilde Q_0^{*}$. The state of $\tilde Q^{*}$ is $\tilde Q_0^{*}\tilde{Ϛ}_Q\tilde Q_0$, a unitary rotation of the state of $\tilde Q$, because $\tilde Q^{*}(\tilde Q^{*})^{*}=\tilde Q^{*}\tilde Q=\tilde Q_0^{*}\tilde Q_H^{2}\tilde Q_0$, which has the same spectrum. The map is blind to the side on which the phase stands in the sense that the singular values and the purity survive; the state itself rotates with the phase.

## The Modular Reading

For a faithful state, $\tilde{Ϛ}_Q>0$, the modular Hamiltonian is defined by

$$
\tilde K_{\mathrm{mod}}=-\ln\tilde{Ϛ}_Q=-2\ln\tilde Q_{\mathrm n}
=-2\ln\tilde Q_H+\ln\!\bigl(2\langle\tilde Q_H,\tilde Q_H\rangle_{*}\bigr)e_t .
$$

The last term is central and is the additive constant that a modular Hamiltonian always carries. The amplitude is therefore the square root of the state, and its logarithm is minus half the modular Hamiltonian up to that constant. This is the exact sense in which the amplitude is the modular square root.

Two boundaries must be kept.

- The modular **conjugation** is anti-unitary and is not the polar phase $\tilde Q_0$. The Tomita–Takesaki conjugation depends on the state and on the algebra; the phase factor is the unitary quotient of the operator off the cone and the partial-isometry quotient on it. They are different objects and the notation must not identify them.
- The modular reading needs $\tilde{Ϛ}_Q>0$, hence $\tilde Q_H>0$, hence $\tilde Q$ invertible. On the null cone the state is pure, the logarithm diverges and the modular Hamiltonian does not exist. The purity table and the modular table have the same boundary.

## Where the Map Appears

The map is not an extra structure added to the theory; it is the common form of four constructions that the corpus already uses.

| object | operator | state it defines | article |
|---|---|---|---|
| measurement outcome | Kraus operator $\tilde K_y$ | $\tilde K_y\tilde{Ϛ}\tilde K_y^{*}/p_y$ | [*The Polar Decomposition of a Kraus Operator: Effect, Backaction and the Measurement Boundary*](the-polar-decomposition-of-a-kraus-operator-effect-backaction-and-the-measurement-boundary.html) |
| polarization | Jones matrix $\tilde J$ | the normalized $\tilde J\tilde J^{*}$, the output coherency | [*Pancharatnam's Phase and the Polarization Sphere in Biquaternionic Form*](pancharatnams-phase-and-the-polarization-sphere-in-biquaternionic-form.html) |
| scattering | S-matrix element $\tilde S$ | the normalized $\tilde S\tilde S^{*}$ | [*The S-Matrix in Biquaternionic Form*](the-s-matrix-in-biquaternionic-form.html) |
| field | field strength $\tilde F$ | the normalized $\tilde F\tilde F^{*}$; for a null field, an energy–momentum direction | [*The Field-Strength Biquaternion and Its Invariants*](the-field-strength-biquaternion-and-its-invariants.html) |

In each row the map is the same and the physical name of the state is different. The measurement row adds a conditioning on the initial state; the polarization row reads the state as a coherency matrix; the scattering row reads it as the state produced by an interaction; the field row reads it as the field's state, which for a null field is an energy–momentum direction. The unity is algebraic, and the differences are in the interpretation of the operator.

One caution about the measurement row. The map of this article takes an operator to a state without an input. The post-measurement state of an instrument takes an operator and an input state, $\tilde{Ϛ}\mapsto\tilde K\tilde{Ϛ}\tilde K^{*}/p$. The two coincide only when the input is the maximally mixed state, $\tilde{Ϛ}=\tfrac12 e_t$, in which case the output is proportional to $\tilde K\tilde K^{*}$. The operator-to-state map is the input-free shadow of the instrument, not the instrument itself.

## The Name of the Map

The phrase "operator-to-state map" is used in two unrelated senses in the literature.

- In **conformal field theory**, the operator-state correspondence is a theorem of radial quantisation: a local operator at the origin defines a state on the boundary sphere, and the map is an isomorphism of Hilbert spaces with a Virasoro action. It needs a conformal boundary, a radial time and a state–operator isomorphism.
- In **this article**, the map is $\tilde Q\mapsto\tilde Q\tilde Q^{*}$, defined on a finite-dimensional algebra, with no boundary, no radial time and no isomorphism. It is a many-to-one map onto the state space, and its fibre is a unitary orbit times a positive scale off the cone and a partial-isometry orbit times a positive scale on it.

The two share a name and nothing else. The corpus states the disclaimer wherever the name appears, because the CFT phrase would be a false citation. There is no conformal field theory in the biquaternion framework, and this article does not introduce one.

## Physical Interpretation

The map gives the informational sector its ontology in one line: **an operator is an amplitude, a scale and a phase, and the state is the square of the normalised amplitude.** The amplitude is what the operator does to norms; the phase is what it does to phases; the scale is its overall size; the state is what remains when the phase and the scale are forgotten.

The stratigraphy is the physical content.

- A **pure state** comes from a rank-one operator, and rank-one operators are the zero divisors. The sharp measurement, the polarizer and the null field all live on the cone for this reason. Purity is not an idealisation imposed on the state; it is the image of a degenerate operator.
- A **maximally mixed state** comes from a unitary operator up to scale. The reversible evolutions are exactly the operators whose image is the least informative state. This is the algebraic form of the statement that a unitary carries no information about a preferred basis.
- A **mixed state** comes from an invertible operator with two distinct singular values. The mixedness measures the spread of the singular values, hence the anisotropy of the operator.

Read as a whole, the table is a dictionary between the algebra's rank stratigraphy and the state space's purity stratigraphy. It is exact in both directions, and it is the reason the measurement, polarization and scattering articles can share one grammar.

## What This Does Not Claim

- It does not claim the operator-state correspondence of a conformal field theory. There is no boundary, no radial quantisation and no isomorphism.
- It does not claim that every state arises from a unique operator. The map is many-to-one; off the cone the fibre is the unitary right factor and the positive scale, and on the cone it is the partial isometry and the positive scale.
- It does not claim that the amplitude $\tilde Q_H$ is a state, or that the state $\tilde{Ϛ}_Q$ is an amplitude. The chain is $\tilde Q\rightsquigarrow\tilde Q_H\rightsquigarrow\tilde Q_{\mathrm n}\rightsquigarrow\tilde{Ϛ}_Q$, and each step loses information.
- It does not claim a modular reading on the null cone. The modular Hamiltonian needs a faithful state and diverges at purity.
- It does not claim that the map is a channel, an instrument or a dynamics. It is a map from operators to states, with no input state and no time.
- It does not claim that the purity table is a classification of physical processes. It is a classification of operators, read through the map.

## Summary

- Every nonzero biquaternion defines a state by $\tilde{Ϛ}_Q=\tilde Q\tilde Q^{*}/2\langle\tilde Q,\tilde Q\rangle_{*}$.
- The amplitude $\tilde Q_H=\sqrt{\tilde Q\tilde Q^{*}}$ is the unnormalised square root of that state; the state is $\tilde Q_{\mathrm n}^{2}$ with $\tilde Q_{\mathrm n}$ the bracket-normalised amplitude.
- The eigenvalues of $\tilde Q_H$ are the singular values of $\tilde Q$, and the state's eigenvalues are their normalised squares.
- The purity is $\tfrac12+(\sigma_1^{2}-\sigma_2^{2})^{2}/2(\sigma_1^{2}+\sigma_2^{2})^{2}$, between $\tfrac12$ and $1$.
- The punctured null cone maps onto the pure states, the unitary group up to scale onto the maximally mixed state, and the invertible interior onto the mixed states.
- The map is invariant under scaling, right-invariant under unitary multiplication (the gauge fibre), and left-covariant (the frame rotation).
- The modular Hamiltonian is $-2\ln\tilde Q_{\mathrm n}$, with a central additive constant; the modular conjugation is not the polar phase.
- The map is the input-free shadow of the instrument and the common form of the Kraus, Jones, S-matrix and field-strength constructions.
- The name is not the CFT operator-state correspondence.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde Q\tilde Q^{*}$ | the positive square whose normalisation is the state |
| $\tilde{Ϛ}_Q$ | the state defined by $\tilde Q$, trace one |
| $\tilde Q_H=\sqrt{\tilde Q\tilde Q^{*}}$ | the amplitude, Hermitian positive; the Cartan amplitude off the cone |
| $\tilde Q_{\mathrm n}=\tilde Q_H/\sqrt{2\langle\tilde Q_H,\tilde Q_H\rangle_{*}}$ | the normalised amplitude, $\langle\tilde Q_{\mathrm n},\tilde Q_{\mathrm n}\rangle_{*}=\tfrac12$ |
| $\sigma_1\ge\sigma_2\ge0$ | the singular values of $\tilde Q$, the eigenvalues of $\tilde Q_H$ |
| $p_i=\sigma_i^{2}/(\sigma_1^{2}+\sigma_2^{2})$ | the state's eigenvalues |
| $\operatorname{Tr}\tilde{Ϛ}_Q^{2}$ | the purity, between $\tfrac12$ and $1$ |
| $\tilde Q_0=\tilde Q_H^{+}\tilde Q$ | the unitary phase off the cone, the partial isometry on it; the phase coordinate along the fibre |
| $\tilde K_{\mathrm{mod}}=-\ln\tilde{Ϛ}_Q$ | the modular Hamiltonian of a faithful state |
| $\operatorname{Tr}\tilde Q=2\operatorname{Sc}\tilde Q=2Q_t$ | the trace |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$ | the Hermitian form |

## Further Reading

- [The Polar Decomposition of a Biquaternion](../articles_maths/the-polar-decomposition-of-a-biquaternion.html), for the general two-factor decomposition, the Moore–Penrose inverse and the partial isometry on the cone.
- *The Cartan Hermitian Pairing of the Polar Decomposition of Biquaternions*, for the N-regular sharpening, the uniqueness and the domain.
- [Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint](../articles_maths/positivity-and-the-hermitian-cone-of-the-biquaternion-algebra-with-hermitian-adjoint.html), for the positive cone and the square root.
- [The Polar Decomposition and Its Three Pairings](the-polar-decomposition-and-its-three-pairings.html), for the comparison of the three first factors.
- [The Polar Decomposition of a Kraus Operator: Effect, Backaction and the Measurement Boundary](the-polar-decomposition-of-a-kraus-operator-effect-backaction-and-the-measurement-boundary.html), for the measurement reading of the three strata.
- [Quantum Physics in Biquaternionic Form](quantum-physics-in-biquaternionic-form.html), for the state space and the Born rule.
- [The Modular Hamiltonian in Biquaternionic Form](the-modular-hamiltonian-in-biquaternionic-form.html), for the modular operator and the Tomita–Takesaki conjugation.
- [The Ontology of the Quantum State under the Biquaternion Framework](the-ontology-of-the-quantum-state-under-the-biquaternion-framework.html), for the state as the Hermitian square.
- M.-D. Choi, "Completely positive linear maps on complex matrices," *Linear Algebra and its Applications* **10** (1975) 285–290, for the structure of positive maps in two dimensions.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the polar decomposition, the fidelity and the purity.
