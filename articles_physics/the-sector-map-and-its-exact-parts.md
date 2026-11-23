# __The Sector Map and Its Exact Parts__

## Introduction

The algebra carries two four-dimensional real slices, and they are the two fixed spaces of one involution. This article writes the map between them, states exactly what it preserves and exactly what it does not, and refuses the inference that a map of the elements is a dictionary of the physics.

The map is multiplication by the scalar imaginary. For $\tilde Q \in \mathbb{B}_\Phi$ put $J(\tilde Q) = i\tilde Q$. Since $i$ is central and $\bar i = -i$, the element $i\tilde Q$ is Hermitian whenever $\tilde Q$ is anti-Hermitian, so $J$ carries one slice onto the other. It is a real-linear bijection, and $J^{2} = -e_t$ on both.

Three things are exact, and one is not.

1. The action is carried exactly. For every unit-norm biquaternion $\tilde U$, the congruence commutes with $J$, so a Lorentz transformation on one slice becomes the same Lorentz transformation on the other.
2. The quaternionic norm changes sign, $\langle J\tilde Q\rangle_\natural = -\langle\tilde Q\rangle_\natural$. That one sign is the interval's inertia, and the flip from $(3,1)$ to $(1,3)$ is this identity read on the coordinates.
3. The Hermitian form is preserved, $H(J\tilde Q) = H(\tilde Q)$.
4. The product is not preserved: $J(\tilde Q\tilde Q') = -J(\tilde Q)J(\tilde Q')$. The map is an anti-homomorphism up to a sign, and no rescaling of $J$ repairs it, because the sign is fixed by $i^{2}=-1$.

What follows from the fourth item is the whole reason the two sectors are not interchangeable. A map that carries the group action but reverses the product cannot carry a statement about composition; and composition is what a dynamics is. The sectors are two readings of one algebra, and the map between them is exact enough to compare invariants and too weak to identify theories.

The conventions are those of [The Element: the Six Subspaces and the Two Ledgers](the-algebraic-vocabulary-element-conjugations-six-subspaces-and-two-ledgers.html) for the star and the natural conjugation, [The Four Forms and the Four Norms](the-four-forms-and-the-four-norms.html) for the four measures, and [The Unit Metric in the Biquaternion Universe](the-unit-metric-in-the-biquaternion-universe.html) for the metric that is read off the multiplication rather than postulated.

## The Two Projections

The involution is the star, and its two fixed spaces are the slices. For any element,

$$
P_\Psi(\tilde Q) = \tfrac12\left(\tilde Q+\tilde Q^{*}\right),
\qquad
P_\Phi(\tilde Q) = \tfrac12\left(\tilde Q-\tilde Q^{*}\right),
$$

and the two are idempotent, orthogonal in the sense $P_\Psi P_\Phi = 0$, and sum to the identity. So

$$
\mathbb{B} = \mathbb{B}_\Psi \oplus \mathbb{B}_\Phi,
\qquad
\dim_\mathbb{R}\mathbb{B}_\Psi = \dim_\mathbb{R}\mathbb{B}_\Phi = 4 .
$$

**Neither projection is an algebra homomorphism, and the defect is one commutator.** For two elements,

$$
P_\Psi(\tilde Q\tilde Q') - P_\Psi(\tilde Q)P_\Psi(\tilde Q') = \tfrac14\left(\tilde Q\tilde Q' - \tilde Q'\tilde Q\right)^{*} - \tfrac14\left(\tilde Q\tilde Q' - \tilde Q'\tilde Q\right),
$$

which is the anti-Hermitian part of the commutator. A product of two Hermitian elements is Hermitian exactly when they commute, and that single fact is the source of every non-additivity in the informational sector: the sum of two observables is an observable, the product is an observable only when the two commute. The same statement, read on the material slice, is that the sum of two four-vectors is a four-vector and the product is not.

Why the decomposition is canonical and the choice of slice is not. The decomposition above needs no choice: the star is fixed by the algebra, so the two projections are fixed. What is a choice is which slice is called *material* and which *informational*, and that choice is a naming, not a structure. This article uses the corpus's naming and states every result in a form that does not depend on it.

## Multiplication by the Scalar Imaginary

The map and its square. Define

$$
J:\mathbb{B}_\Phi\longrightarrow\mathbb{B}_\Psi,\qquad J(\tilde Q)=i\tilde Q .
$$

It is real-linear, injective, and onto: a Hermitian element $\tilde H$ has the anti-Hermitian preimage $-i\tilde H$, and $-i\tilde H$ is anti-Hermitian because $(-i\tilde H)^{*}=i\tilde H^{*}=i\tilde H=-(-i\tilde H)$. Applying $J$ twice gives $-e_t$, so $J$ is a complex structure on the pair, and the pair is one complex vector space of complex dimension four — which is the statement $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ read slice by slice.

It commutes with the congruence, and this is the exact part. For $\tilde U$ of unit norm and $\tilde Q\in\mathbb{B}_\Phi$,

$$
J\left(\tilde U\tilde Q\tilde U^{*}\right)=i\,\tilde U\tilde Q\tilde U^{*}=\tilde U\left(i\tilde Q\right)\tilde U^{*},
$$

because $i$ is central and is fixed by the star. So a Lorentz transformation acting on one slice is the *same* element acting on the other, and the two actions have the same orbits up to $J$. Every statement about the group — the six generators, the two Casimirs, the Cartan decomposition, the Wigner angle — is therefore a statement about both slices at once, and is proved once.

**It reverses the product, and this is the exact part that costs.** For $\tilde Q,\tilde Q'\in\mathbb{B}_\Phi$,

$$
J(\tilde Q\tilde Q')=i\tilde Q\tilde Q'=-\left(i\tilde Q\right)\left(i\tilde Q'\right)=-J(\tilde Q)J(\tilde Q').
$$

There is no linear rescaling $J_\imath=\digamma_{\mathrm{cfm}}\,\mathrm{id}$ that repairs the sign: multiplicativity would require $\digamma_{\mathrm{cfm}}=\digamma_{\mathrm{cfm}}^{2}$, that is $\digamma_{\mathrm{cfm}}\in\{0,1\}$, and the identity map does not carry one slice to the other. The sign is the arithmetic of $i^{2}=-1$ and it cannot be normalised away. Read as a statement about representations, $J$ is an isomorphism of $\mathbb{B}_\Phi$ with the opposite algebra $\mathbb{B}_\Psi^{\mathrm{op}}$, which is why the two sectors are mirror images rather than copies.

## The Two Forms Under the Map

**The quaternionic norm changes sign.** For $\tilde Q\in\mathbb{B}_\Phi$,

$$
\langle J\tilde Q\rangle_\natural=\left(i\tilde Q\right)\left(i\tilde Q\right)^{\natural}=i^{2}\,\tilde Q\tilde Q^{\natural}=-\langle\tilde Q\rangle_\natural .
$$

Since the norm is a sum of four squares of the coefficients, the identity says that the complexified interval is negated. On the material slice the physical interval is this norm at a negative real value, $\langle\tilde P_\Phi\rangle_\natural=-m^{2}c^{2}$; on the informational slice the same polynomial at a positive value is what the corpus calls an indefinite weight and never a state.

The Hermitian form is preserved. For the same element,

$$
H(J\tilde Q)=\mathrm{Sc}\left((i\tilde Q)(i\tilde Q)^{*}\right)=\mathrm{Sc}\left(i\tilde Q\cdot(-i\tilde Q^{*})\right)=\mathrm{Sc}\left(\tilde Q\tilde Q^{*}\right)=H(\tilde Q),
$$

because $(i\tilde Q)^{*}=-i\tilde Q^{*}$ and the two factors of $i$ multiply to one. So the positive-definite form is the same number on the two sides of the map, and this is the precise sense in which the amplitude of the informational sector and the weight of the material sector are one computation.

The pair of statements is the asymmetry of the corpus in one line. $J$ preserves $H$ and negates $\langle\cdot\rangle_\natural$. On the material side the physical scalar is the negated one; on the informational side the physical scalar is the preserved one. That is why the interval is indefinite and the weight is definite, and it is not a convention: it is the two signs of the same map.

The trace. The trace of the $2\times2$ image is $2\,\mathrm{Sc}$, and $J$ changes the scalar part by $i$: $\mathrm{Sc}(i\tilde Q)=i\,\mathrm{Sc}(\tilde Q)$. So the trace is *not* preserved; it is multiplied by $i$, which is the statement that the material scalar (an energy, an interval coefficient) and the informational scalar (a normalisation, a weight) are different numbers of different dimensions and are not to be compared without the factor.

## The Coordinate Dictionary

What the map does to the corpus coordinates. Write the material element in the corpus's letters, $\tilde R_\Phi=i\,r'_t\,e_t+\vec r$, and apply $J$:

$$
J\left(i\,r'_t\,e_t+r_x\vec e_x+r_y\vec e_y+r_z\vec e_z\right)=-r'_t\,e_t+i\left(r_x\vec e_x+r_y\vec e_y+r_z\vec e_z\right).
$$

This is the informational element $c t'\,e_t+i\left(x'\vec e_x+y'\vec e_y+z'\vec e_z\right)$ with

$$
c t'=-r'_t,\qquad x'=r_x,\qquad y'=r_y,\qquad z'=r_z .
$$

**So the map moves the $i$ and flips the time.** The material coordinate carries the imaginary unit on the temporal coefficient; the image carries it on the three spatial coefficients and carries the temporal coefficient real. This is the corpus's Wick rotation stated as a map of elements rather than as a substitution, and the sign on $c t'$ is the sign of the norm flip computed above, not a separate convention.

The inertias are the two signatures. With $\delta_{\imath\jmath}=(1,1,1,1)$ the interval is a contraction with the unit metric on each side, and the two readings are

$$
\langle\tilde R_\Phi\rangle_\natural=-c^{2}{t'}^{2}+r_x^{2}+r_y^{2}+r_z^{2},
\qquad
\langle J\tilde R_\Phi\rangle_\natural=c^{2}{t'}^{2}-{x'}^{2}-{y'}^{2}-{z'}^{2},
$$

of inertia $(3,1)$ and $(1,3)$. One metric, one tuple of signs, two inertias, and the difference is the minus sign of the map. A reader who wants the two signatures from two matrices has to choose two; a reader who takes them from one map chooses once.

## What the Map Does Not Carry

A four-vector is not a state, and the map does not pretend otherwise. A state is $\tilde{Ϛ}_\Psi=\tfrac12(e_t+i\vec s_\Psi)$, of trace one and radius below one. The image of a four-momentum is $J(\tilde P_\Phi)$, of Hermitian form $H(\tilde P_\Phi)$ and of norm $+m^{2}c^{2}$; normalising it by its trace gives an element of the informational slice, and that element is not the state of the particle. It is the element whose vector part is the spatial momentum scaled by the energy, and the corpus's conventions call it a generator, not a state.

The Born weight is not the interval. The weight of an observable $\tilde A$ in a state is $\mathrm{Sc}(\tilde{Ϛ}_\Psi\tilde A)$, and it is a probability only after the state and the observable are placed in the same slice. $J$ carries one slice to the other, so it carries the *algebra* of the pairing, and it does not carry the interpretation: a probability and an interval are different functionals of the same elements.

**Composition is the casualty.** Because $J$ reverses the product, it cannot carry a statement of the form "the product of these two elements is the evolution". A reader who composes two maps, one on each side, must insert a sign, and the sign is $(-1)$ per factor. The corpus's rule is therefore: compare invariants across the map, never compose across it.

| object | under $J$ |
| --- | --- |
| the congruence $\tilde Q\mapsto\tilde U\tilde Q\tilde U^{*}$ | preserved |
| the quaternionic norm | negated |
| the Hermitian form | preserved |
| the trace $2\,\mathrm{Sc}$ | multiplied by $i$ |
| the product | reversed up to $-1$ |
| the inertia | $(3,1)\leftrightarrow(1,3)$ |
| the coordinate $i\,r'_t e_t+\vec r$ | $-r'_t e_t+i\vec r$ |
| a four-vector | an element, not a state |
| a composition of two maps | requires a sign |

## Summary

The two slices are the fixed spaces of the star, and multiplication by $i$ is the exact map between them. It commutes with the congruence, so every statement about the Lorentz group holds on both slices at once; it negates the quaternionic norm, which is the flip of the inertia from $(3,1)$ to $(1,3)$; it preserves the Hermitian form, which is why one weight serves both sectors; and it reverses the product up to a sign, which is why the two sectors are mirror images and not copies. The map is exact where exactness is useful and broken where it matters.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $P_\Psi$, $P_\Phi$ | the projections onto the Hermitian and anti-Hermitian slices, $\tfrac12(\tilde Q\pm\tilde Q^{*})$ |
| $J(\tilde Q)=i\tilde Q$ | the map from the material to the informational slice |
| $\langle\tilde Q\rangle_\natural=\tilde Q\tilde Q^{\natural}$ | the quaternionic norm, the interval on the material slice |
| $H(\tilde Q)=\mathrm{Sc}(\tilde Q\tilde Q^{*})$ | the Hermitian form, the weight |
| $2\,\mathrm{Sc}$ | the trace of the $2\times2$ image |
| $\tilde R_\Phi=i\,r'_t e_t+\vec r$ | the material coordinate |
| $\delta_{\imath\jmath}=(1,1,1,1)$ | the unit metric, read off the multiplication |

## Further Reading

In this category. [The Element: the Six Subspaces and the Two Ledgers](the-algebraic-vocabulary-element-conjugations-six-subspaces-and-two-ledgers.html) fixes the star and the natural conjugation. [The Four Forms and the Four Norms](the-four-forms-and-the-four-norms.html) proves which form is multiplicative and which is definite. [The Two Sectors: the Hermitian Split and the Four Bridges](the-two-sectors-the-hermitian-split-and-the-four-bridges.html) states the four constructions that carry one slice to the other. [The Unit Metric in the Biquaternion Universe](the-unit-metric-in-the-biquaternion-universe.html) reads the metric off the multiplication. [The Temporal Dimension: Why the Temporal Unit Is the Identity](the-temporal-dimension-why-the-temporal-unit-is-the-identity.html) reads the two temporal coefficients that this article's dictionary relates. [Two Readings of One Transformation: A Comparison](two-readings-of-one-transformation-a-comparison.html) takes the map as the instrument of the comparison.

In the mathematics corpus. [The Four General Products and Their Relations over the Biquaternion Algebra](../articles_maths/the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html) supplies the product laws that the sign reversal violates, and the opposite-algebra statement is there.
