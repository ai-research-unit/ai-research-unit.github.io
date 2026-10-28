# __The Unitary Group: Gauge, Phase and the Double Cover__

## Introduction

The unitary group of the biquaternion algebra is

$$
U(\mathbb{B})=\{\tilde Q\in\mathbb{B}:\tilde Q^{*}\tilde Q=e_t\}\cong U(2),
$$

not $U(4)$. It is the group of the algebra's unitary elements, and it acts on spinors by left multiplication and on states by conjugation. Its centre is the global phase $U(1)$; its quotient by the centre is $SO(3)$; its norm-one slice is $SU(2)\cong S^3$, the double cover of $SO(3)$.

The article reads the group physically. It states the group and its topology, reads the left action as the gauge of the spinor and the conjugation as the gauge of the state, the pure-state orbit as the Bloch sphere, the flag variety as the space of measurement bases, the polar decomposition as the amplitude–frame split, and the double cover as the spinor. It closes with the relation to the Krein isometry group and with the limits of the gauge reading.

The distinction that organises the article is the distinction between three actions:

| action | group | what it preserves | physical reading |
| --- | --- | --- | --- |
| left multiplication on spinors | $U(2)$ | the Hermitian form and the spinor norm | the gauge of the spinor |
| conjugation $\tilde X\mapsto\tilde U\tilde X\tilde U^{*}$ | $U(2)/U(1)\cong SO(3)$ | Hermiticity, trace, positivity and the product | the gauge of the state and the frame |
| dagger sandwich | $SO^{+}(1,3)$ (via the spin cover $\mathbb{B}^{\times}_{1}\cong SL_2(\mathbb{C})$; $SU(2)$ is the compact part) | the norm and the two sectors | the Lorentz group, not a gauge |

The three are often conflated because their compact parts all involve $SU(2)$. They act on different objects and preserve different structures, and the physical reading of each is different.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The unitary group, its normal form and its topology | [The Unitary Group of the Biquaternion Algebra](../articles_maths/the-unitary-group-of-the-biquaternion-algebra.html) |
| The polar decomposition and the retractions | [The Polar Decomposition of a Biquaternion](../articles_maths/the-polar-decomposition-of-a-biquaternion.html) |
| The three actions and the sandwich | [Element and Operator Representations: The Three Actions](the-element-and-operator-representations.html) |
| The minimal left ideals and the spinor spaces | [The Minimal Left Ideals](../articles_maths/the-minimal-left-ideals.html) |
| The Krein isometry group and its Cartan decomposition | [The Krein Isometry Group and Its Cartan Decomposition](../articles_maths/the-krein-isometry-group-and-its-cartan-decomposition.html) |
| The Krein form and the gauge calibration | [The Krein Form and the Indefinite Structure](the-krein-form-and-the-indefinite-structure.html) |
| The state space and the Born form | [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html) |
| The Lorentz action as a sandwich | [Frames, Rotations and the Lorentz Group](frames-rotations-and-the-lorentz-group.html) |

## The Group

### The Normal Form

A unitary biquaternion is a scalar multiple of a unit quaternion:

$$
\tilde U=\lambda\,\hat u,
\qquad
\lvert\lambda\rvert=1,
\qquad
\hat u\in Sp(1)\cong SU(2).
$$

The scalar phase and the rotor commute, and the intersection is $\{\pm e_t\}$, so

$$
U(\mathbb{B})=S^1\cdot S^3
\cong(S^1\times S^3)/\{\pm e_t\}
\cong S^1\times S^3 .
$$

The group is four-dimensional, compact and connected. Its maximal torus is $T^2=S^1\times S^1$, and the flag variety is

$$
U(\mathbb{B})/T^2\cong S^2 .
$$

The homotopy groups are

$$
\pi_1(U(\mathbb{B}))=\mathbb{Z},
\qquad
\pi_3(U(\mathbb{B}))=\mathbb{Z},
$$

and the universal cover is $\mathbb{R}\times S^3$. The norm is the determinant in the matrix model, and it gives the two quotients

$$
U(\mathbb{B})/S^3\cong S^1,
\qquad
U(\mathbb{B})/U(1)\cong SO(3).
$$

The norm-one slice is $SU(2)\cong S^3$; the centre is the global phase $U(1)$; the quotient by the centre is the rotation group.

### The Reading

The group has three layers, and each is a physical statement.

- **The phase.** The centre $U(1)$ is the global phase. It acts trivially on rays and on the algebra's inner automorphisms; it is the redundancy of the description, not a physical degree of freedom.
- **The rotor.** The $S^3$ factor is the spatial rotation. Its quotient by the centre is $SO(3)$; its double cover is the spinor.
- **The norm.** The determinant $N$ is the scale. On the unitary group it is a phase; the norm-one slice is the determinant-one subgroup.

The decomposition $U(2)\cong S^1\times S^3$ is therefore the decomposition into the central phase and the rotor. The physical state has a phase and a rotor, not a scale; the scale is the amplitude of the polar decomposition, and it is not unitary.

## The Gauge of the State Space

### The Left Action

The unitary group acts on the algebra by left multiplication:

$$
L_{\tilde U}(\tilde X)=\tilde U\tilde X,
\qquad
\tilde U\in U(\mathbb{B}).
$$

The action preserves the Hermitian form:

$$
\langle\tilde U\tilde X,\tilde U\tilde Y\rangle_{*}
=\mathrm{Sc}\bigl((\tilde U\tilde X)^{*}\tilde U\tilde Y\bigr)
=\mathrm{Sc}(\tilde X^{*}\tilde Y)
=\langle\tilde X,\tilde Y\rangle_{*} .
$$

It is an isometry of the Hilbert space. It does not preserve Hermiticity: $(\tilde U\tilde X)^{*}=\tilde X^{*}\tilde U^{*}\neq\tilde U\tilde X$ in general. The left action is therefore the action on the spinor space, not on the state space; the state space carries the conjugation instead.

The reading is the **gauge of the spinor**. A spinor is an element of a Peirce carrier, which is a minimal left ideal in this algebra; a unitary left multiplication is a change of the basis of the spinor. The Hermitian form on the spinor space is invariant, and the global phase is the kernel of the action on rays.

The state space is not the spinor space. A state is a positive trace-one element, and it transforms by conjugation:

$$
\rho\longmapsto \tilde U\rho\tilde U^{*}.
$$

The conjugation preserves Hermiticity, the trace, the positivity and the algebra product; its kernel is the global phase. It is the action on the state space, and its effective group is $U(2)/U(1)\cong SO(3)$. The left multiplication and the conjugation are different actions on different objects, and the distinction is the first thing the gauge reading must keep.

### The Bloch Sphere

The quotient by the global phase is

$$
U(\mathbb{B})/U(1)\cong SO(3),
$$

the effective group of the conjugation action. The space of pure states of a two-level system is the orbit of a pure state, and the stabiliser of a pure state is the maximal torus $T^2$ of two phases, not the centre:

$$
U(\mathbb{B})/T^2\cong S^2 .
$$

The pure states are the Hermitian idempotents; the unitary group acts transitively on them, and the stabiliser of one is $T^2$. The orbit is the Bloch sphere.

The reading is the **state space**. The unitary group is the group of reversible changes of basis; the quotient by the phase is the effective rotation group $SO(3)$, which acts on the rays; the pure states are the orbit $U(2)/T^2\cong S^2$. The mixed states are the interior of the Bloch ball, and the unitary group acts on them by conjugation.

### The Flag Variety

The quotient by the maximal torus is

$$
U(\mathbb{B})/T^2\cong S^2 .
$$

A maximal torus is a pair of commuting phases, and a point of the flag variety is a **measurement basis**: a pair of orthogonal states, up to the two phases. The reading is the choice of a complete measurement. The torus is the pair of phases of the two outcomes; the flag variety is the basis itself. The same homogeneous space is the pure-state orbit: a pure state is a line, and a complete flag in $\mathbb{C}^{2}$ is determined by its line.

The three quotients are therefore:

| quotient | space | physical reading |
| --- | --- | --- |
| $U(\mathbb{B})/U(1)$ | $SO(3)$ | the effective group of the conjugation action / the rotation group |
| $U(\mathbb{B})/T^2$ | $S^2$ | the pure states and the measurement bases: the same sphere, two readings |
| $U(\mathbb{B})/S^3$ | $S^1$ | the phase / the determinant |

The first quotient is the group $SO(3)$, not a sphere. The second is the Bloch sphere, read once as states and once as bases; for $U(2)$ the two readings are the same homogeneous space.

## The Polar Decomposition

Every invertible element has a polar decomposition

$$
\tilde Q=\tilde A\,\tilde U,
\qquad
\tilde A=\lvert\tilde Q\rvert\text{ positive},
\qquad
\tilde Q\text{ unitary},
$$

and the unitary group is a strong deformation retract of the unit group. The reading is the **amplitude–frame split**: every invertible operator is a positive amplitude times a unitary frame. The amplitude is the state (the positive factor); the frame is the basis (the unitary factor).

The polar decomposition is the operator-to-state map. The positive factor carries the probabilities; the unitary factor carries the phase and the orientation. The map is not unique at the degenerate boundary, where the amplitude is not invertible; the frame is then a partial isometry, not a unitary.

The reading is the reason the unitary group is the gauge group: the physical content of an operator is the positive factor, and the unitary factor is the choice of frame. A gauge transformation is a change of the unitary factor that leaves the amplitude invariant.

## The Double Cover

The norm-one slice is

$$
SU(2)\cong S^3,
$$

and the map

$$
SU(2)\longrightarrow SO(3)
$$

is the double cover. A rotation by $2\pi$ is the identity in $SO(3)$ and $-e_t$ in $SU(2)$; a rotation by $4\pi$ is the identity in both. The norm-one slice $SU(2)$ is the spin group, and its two-valued representation is the spinor.

The physical reading is the **spinor**. A state that transforms under $SU(2)$ rather than $SO(3)$ changes sign under a full turn; the sign is unobservable in a single state but observable in an interference experiment. The algebra's Peirce carriers are the spinor spaces, and here they are the minimal left ideals; the unitary group acts on them by left multiplication. The double cover is the algebraic form of half-integer spin.

The reading is not a derivation of the spin-statistics theorem. It is the statement that the algebra's norm-one unitary group $SU(2)$ is the double cover of the rotation group, and that the spinor representation is the fundamental representation. The statistics is an extra input.

## Inside the Krein Group

The Krein isometry group of the indefinite form is

$$
U_J(\mathbb{B})=\{T:T^{*}ET=E\}\cong U(1,3),
$$

of real dimension sixteen, non-compact, with maximal compact subgroup $U(1)\times U(3)$ and centre $U(1)$. The compact subgroup generated by the algebra's own isometries is

$$
U(1)\times PU(2)\cong U(1)\times SO(3),
$$

of dimension four: the central phases and the unitary sandwiches. The norm-one sandwiches form $PSL(2,\mathbb{C})\cong SO^+(1,3)$, the Lorentz group; their non-unitary members are isometries but not automorphisms of the algebra.

The reading is the **split of the gauge from the frame change**. Inside the algebra's own isometries, the compact subgroup $U(1)\times PU(2)$ is the gauge — the central phase and the spatial rotation — and the non-compact norm-one sandwiches are the boosts, a change of frame rather than a redundancy. The full Krein group is larger: its maximal compact subgroup is $U(1)\times U(3)$, and its non-compact directions are the complex hyperbolic boosts.

The Krein involution is not the Cartan involution. It acts on the full operator algebra $\mathfrak{g}=\operatorname{End}_{\mathbb{C}}(\mathbb{B})\cong\mathfrak{gl}_4(\mathbb{C})$, of real dimension $32$, and splits it as

$$
\mathfrak{g}=\mathfrak{k}\oplus\mathfrak{p},
\qquad
\mathfrak{k}=\mathfrak{u}(1,3),
\qquad
\mathfrak{p}=J\cdot\operatorname{Herm}_4,
$$

with $\mathfrak{k}$ the $J$-skew operators and $\mathfrak{p}$ the $J$-self-adjoint operators, each of dimension $16$. This is the Krein decomposition of the operator algebra, not the Cartan decomposition of $\mathfrak{u}(1,3)$: the fixed group of the Krein involution is the non-compact $U(1,3)$.

The Cartan involution $\theta_0(T)=(T^{*})^{-1}$ of $U(1,3)$ has fixed group $U(1)\times U(3)$ and symmetric space

$$
U(1,3)/(U(1)\times U(3))\cong\mathbb{CH}^3 .
$$

The reading is the space of frames: the complex hyperbolic ball is the space of time axes, and the gauge group is the stabiliser of a point. The boosts act transitively on the ball; the gauge group fixes a point.

## Physical Interpretations

- **The gauge group of the state space is $U(2)$.** The unitary elements act on spinors by left multiplication and on states by conjugation; the conjugation preserves the Born form and the trace-one slice. The global phase is the kernel; the physical state is a ray.
- **The quotient by the phase is the effective rotation group.** $U(2)/U(1)\cong SO(3)$; the pure states are the Hermitian idempotents, and their orbit is the Bloch sphere $U(2)/T^2\cong S^2$.
- **The quotient by the maximal torus is the Bloch sphere.** $U(2)/T^2\cong S^2$; it is the space of pure states and, read dually, the space of measurement bases, since a maximal torus is a pair of orthogonal states up to their phases.
- **The polar decomposition is the amplitude–frame split.** Every invertible operator is a positive amplitude times a unitary frame; the amplitude is the state, the frame is the gauge.
- **The double cover is the spinor.** $SU(2)\to SO(3)$; a $2\pi$ rotation is $-e_t$; the spinor changes sign. The algebra's minimal ideals are the spinor spaces.
- **The gauge is the compact algebraic subgroup of the Krein group.** $U(1)\times PU(2)$ is the compact subgroup generated by the algebra's own isometries; the boosts are physical frame changes, not gauge.
- **The norm is the determinant and the scale.** $U(2)/S^3\cong S^1$; the norm-one slice is $SU(2)$; the phase is the $U(1)$ factor.
- **The gauge is not a field.** The group is the group of changes of basis; the article supplies no connection, no curvature and no field strength.

## Limits

The unitary group of the algebra is $U(2)$, not $U(4)$. The full isometry group of the definite Hermitian form on $\mathbb{B}\cong\mathbb{C}^4$ is $U(4)$, but it mixes the left and right actions and does not preserve the algebra product. The algebra's unitary group is the subgroup that acts by left multiplication.

The left action is not an automorphism of the algebra. It preserves the Hermitian form, but it does not preserve Hermiticity or the product. The conjugation is the automorphism, and its effective group is $U(2)/U(1)\cong SO(3)$. The two actions must not be conflated.

The dagger sandwich by the norm-one group is the Lorentz action — the norm-one group is its spin cover — not a gauge group. It preserves the norm and the two sectors, and it acts on the four-vectors; it is a change of frame, not a redundancy of the description.

The gauge reading is the state-space action. It is not a derivation of the Standard Model gauge group, and it is not a claim that the physical gauge group is $U(2)$.

The double cover is the spinor, not a derivation of the spin-statistics theorem. The statistics is an extra input.

No dynamics is supplied. The group is the group of reversible changes of basis; the article does not supply a Hamiltonian, a connection or a field.

## Summary

- $U(\mathbb{B})=\{\tilde Q:\tilde Q^{*}\tilde Q=e_t\}\cong U(2)$, with structure $S^1\times S^3$, maximal torus $T^2$, flag variety $S^2$ and universal cover $\mathbb{R}\times S^3$.
- The left action preserves the Hermitian form on spinors; the conjugation preserves the state space. The global phase is the kernel of both; the quotient $U(2)/U(1)\cong SO(3)$ is the effective rotation group, and the Bloch sphere of rays is the orbit $U(2)/T^2\cong S^2$.
- The quotient $U(2)/T^2\cong S^2$ is the Bloch sphere, read as the pure states and as the measurement bases.
- The polar decomposition splits every invertible operator into a positive amplitude and a unitary frame; the amplitude is the state, the frame is the gauge.
- The norm-one slice is $SU(2)\cong S^3$, the double cover of $SO(3)$; the spinor changes sign under a $2\pi$ rotation.
- The compact subgroup generated by the algebra's own isometries is $U(1)\times PU(2)\cong U(1)\times SO(3)$; the boosts are physical frame changes, not gauge.
- The norm is the determinant and the scale; $U(2)/S^3\cong S^1$ and the norm-one slice is $SU(2)$.
- The group supplies no connection, no curvature, no field and no dynamics.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $U(\mathbb{B})=\{\tilde Q:\tilde Q^{*}\tilde Q=e_t\}$ | the unitary group, $\cong U(2)$ |
| $S^1\cdot S^3$ | the phase times the rotor |
| $T^2$ | a maximal torus |
| $U(\mathbb{B})/T^2\cong S^2$ | the flag variety (measurement bases) and the pure-state orbit (Bloch sphere) |
| $U(\mathbb{B})/U(1)\cong SO(3)$ | the effective group of the conjugation action; the rotation group |
| $U(\mathbb{B})/S^3\cong S^1$ | the determinant, the phase |
| $\tilde Q=\tilde A\tilde U$ | the polar decomposition |
| $U(1,3)$ | the Krein isometry group |
| $U(1)\times PU(2)$ | the compact subgroup generated by the algebra's own isometries |

## Further Reading

- [The Unitary Group of the Biquaternion Algebra](../articles_maths/the-unitary-group-of-the-biquaternion-algebra.html), for the group and its topology.
- [The Polar Decomposition and Its Three Pairings](the-polar-decomposition-and-its-three-pairings.html), for the amplitude–frame split.
- [Element and Operator Representations: The Three Actions](the-element-and-operator-representations.html), for the left action, the inner automorphism and the sandwich.
- [The Krein Isometry Group and Its Cartan Decomposition](../articles_maths/the-krein-isometry-group-and-its-cartan-decomposition.html), for $U(1,3)$ and the compact part.
- [Spin and the Two State Spaces](spin-and-the-two-state-spaces.html), for the spinor spaces and the double cover.
- [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html), for the state space and the Born form.
