# __Roots, Idempotents and Observables__

## Introduction

The plain product of the biquaternion algebra, read at the central value $+1$, gives one equation, $\tilde\Xi\tilde\Xi=e_t$, and two objects. Its solutions are the **roots of $+1$**; the elements with $\tilde\Pi\tilde\Pi=\tilde\Pi$ are the **idempotents**; and the **halving map** $\tilde\Xi\mapsto\tfrac12(e_t+\tilde\Xi)$ is a bijection from the first set onto the second. A root of $+1$ is an operation of square one, and the two idempotents it carries are the projections onto its two eigenspaces.

This article reads the pair physically. The **Hermitian roots of $+1$** are read as the **involutive observables** of the informational sector, the observables whose only values are $\pm1$. The **Hermitian idempotents** are read as the **pure states** of that sector. The root and its pair are then one datum seen twice: the observable and its two eigenstates. The non-Hermitian roots and idempotents are read as neither, and the roots of $-1$ are read as the **local complex structures**, which lie in the material sector.

The article owns no theorem. Every classification, bijection and count is stated in the mathematics article that proves it and linked in the table below. What this article adds is the naming and the boundary of the naming.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The classification of the roots of $+1$: the two central roots, the purely imaginary family and the non-trivial family | [Square Roots of One and the Idempotents of the Biquaternion Algebra](../articles_maths/square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html) |
| The halving map, the pair map and the spectral resolution of a root | [Square Roots of One and the Idempotents of the Biquaternion Algebra](../articles_maths/square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html) |
| The idempotents, orthogonality, completeness, primitivity and the Peirce decomposition | [Ideals and Peirce Decomposition of the Biquaternion Algebra](../articles_maths/ideals-and-peirce-decomposition-of-the-biquaternion-algebra.html) |
| The sectors $\mathbb{M}_\pm$, the Hermitian conjugation and the trace | [The Four Forms and the Four Algebraic Norms](../articles_maths/the-four-forms-and-the-four-algebraic-norms.html) |
| The restrictions of the forms to the remarkable subspaces | [Remarkable Subspaces and the Four Forms](../articles_maths/remarkable-subspaces-and-the-four-forms.html) |
| The roots of $-1$ and their relation to the roots of $+1$ | [Square Roots of One and the Idempotents of the Biquaternion Algebra](../articles_maths/square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html) |
| The root sets and idempotent sets of the twelve structures | [Square Roots of One and the Idempotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](../articles_maths/square-roots-of-one-and-the-idempotents-in-the-algebraic-structures-over-the-biquaternion-c-space.html) |
| The roots of a general element and the failure of the square-root formula off the cone | [Square Roots of a General Element in the Biquaternion Algebra](../articles_maths/square-roots-of-a-general-element-in-the-biquaternion-algebra.html) |

## One Equation, Two Objects

The square of a biquaternion is

$$
\tilde Q^2=\bigl(Q_t^2-(\vec Q,\vec Q)\bigr)e_t+2Q_t\vec Q,
$$

and the equation $\tilde\Xi^2=e_t$ separates into $2\Xi_t\vec\Xi=0$ and $\Xi_t^2-(\vec\Xi,\vec\Xi)=1$. Since $\mathbb{C}$ is a field, a root is either a complex scalar or pure, and the two branches exhaust the solutions. The scalar branch gives the two central roots $\pm e_t$. The pure branch splits again:

| family | elements | real parameters | Hermitian |
| --- | --- | --- | --- |
| trivial | $\pm e_t$ | two isolated | yes, central |
| purely imaginary | $i\tilde\xi$, $\tilde\xi$ a real pure quaternion of square $-e_t$ | two | yes |
| non-trivial | $\vec\xi+i\vec\xi'$, $\vec\xi\neq0$, with $\xi^2-{\xi'}^2=-1$ and $\vec\xi\cdot\vec\xi'=0$ | four | no |

Three facts about the table carry the whole reading. First, **the Hermitian roots are exactly the trivial roots and the purely imaginary family**: a Hermitian element has the form $h_te_t+i\vec h$ with $h_t$ real and $\vec h$ real pure, its square is $(h_t^2+\lvert\vec h\rvert^2)e_t+2h_ti\vec h$, and the vector part vanishes only at $h_t=0$ or $\vec h=0$. Second, **every root is a unit**, with inverse itself, so no root is a zero divisor. Third, **the non-trivial roots are not Hermitian**, so the table already separates the observables from the rest.

The separation is the first physical statement of the article. The physically available involutions are the Hermitian ones. A non-Hermitian root is a perfectly good algebraic involution, but it is not an observable of the informational sector, and it is not a state either, as the next two sections show.

## The Halving Map

The halving map is the bridge between the two objects:

$$
\boxed{\;\tilde\Xi\longmapsto\tilde\Pi_+(\tilde\Xi)=\tfrac12(e_t+\tilde\Xi),\qquad
\tilde\Pi_-(\tilde\Xi)=\tfrac12(e_t-\tilde\Xi)=e_t-\tilde\Pi_+(\tilde\Xi)\;}.
$$

The two computations are two lines: if $\tilde\Xi^2=e_t$ then $\tfrac14(e_t+\tilde\Xi)^2=\tfrac12(e_t+\tilde\Xi)$, and if $\tilde\Pi^2=\tilde\Pi$ then $(2\tilde\Pi-e_t)^2=e_t$. The inverse is $\tilde\Xi=2\tilde\Pi-e_t$.

The pair has four properties, and each is a physical statement in the reading that follows.

- **Orthogonal and complete.** $\tilde\Pi_+\tilde\Pi_-=\tilde\Pi_-\tilde\Pi_+=0$ and $\tilde\Pi_++\tilde\Pi_-=e_t$. The two projections resolve the identity: the two outcomes exhaust the alternatives.
- **The root is the difference.** $\tilde\Xi=\tilde\Pi_+-\tilde\Pi_-$. The observable is the difference of its two states.
- **The root acts by the two signs.** $\tilde\Xi\tilde\Pi_+=\tilde\Pi_+\tilde\Xi=\tilde\Pi_+$ and $\tilde\Xi\tilde\Pi_-=-\tilde\Pi_-$. The pair is the spectral decomposition of the root, with eigenvalues $+1$ and $-1$.
- **Each nontrivial idempotent is a zero divisor.** $\tilde\Pi(e_t-\tilde\Pi)=0$, and a nontrivial idempotent has vanishing norm, $\langle\tilde\Pi\rangle_{\natural}=0$. The states lie on the cone even though the observables do not.

The last property is the sharpest algebraic contrast between the two objects. A root of $+1$ is a unit and never a zero divisor. Its nontrivial idempotents are zero divisors, and they lie on the zero-divisor cone. The nontrivial observable is invertible; its eigenstates are not. The degenerate pair $0,e_t$ is the exception: it is the trivial resolution and carries no state. That is not a defect: a projection is not meant to be invertible, and the non-invertibility is exactly the collapse of information that a projection performs.

The halving map is a bijection onto all idempotents, including $0$ and $e_t$, which are the degenerate cases of the trivial roots. So the algebraic statement is complete: every idempotent of the algebra is half of a root of $+1$, and every root of $+1$ carries a complete orthogonal pair.

## Hermitian Roots as Observables

A Hermitian root is a Hermitian element of square $e_t$. It is an operator with two eigenvalues, $+1$ and $-1$, and with orthogonal eigenspaces. The physical reading is direct:

> **The Hermitian roots of $+1$ are the involutive observables** — the observables of square one, the parities and the signs of the informational sector.

The trivial roots $\pm e_t$ are the observables $+1$ and $-1$; they are central and carry no direction. The family $\pm i\tilde\xi$ is the non-central one: a direction $\tilde\xi$ on the real unit sphere, and the observable $i\tilde\xi$. The two signs do not double the family, since $\xi$ already ranges over the sphere, so the family is one observable for each point of $S^2$. The standard examples are $i\vec e_z$, $i\vec e_x$ and $i\vec e_y$; the non-trivial root $\vec e_x+i(\vec e_y+\vec e_z)$ is a root but not Hermitian, and the table places it outside the observables.

The family is two-dimensional because a direction on the sphere is. The observable's eigenvalues do not depend on the direction; only its eigenbasis does. The direction is therefore the **axis of the measurement**, and the pair of idempotents is the pair of outcomes. The reading is the algebraic form of a Stern–Gerlach measurement: one direction is chosen, and the two outcomes are the two signs along it. The choice of direction is a choice of observable; the algebra fixes the two possible outcomes once the direction is chosen.

Two further carriers of the same root are worth naming. A traceless Hermitian element $\tilde H=i\vec h$ squares to $\lvert\vec h\rvert^2e_t$, so $\tilde H/\lvert\vec h\rvert$ is an involution whose eigenvalues $\pm\lvert\vec h\rvert$ are the split levels of the Zeeman and Stark articles; the algebra fixes the structure and the isotropy of the splitting, not the gyromagnetic ratio. And the central root $-e_t$ is the rotor of a full turn, $R(2\pi)=-e_t$, the nontrivial element of the double cover: the two central roots are the two signs of the covering.

The boundary is immediate and important. **Not every observable is a root of $+1$.** A general Hermitian element $\tilde H=h_te_t+i\vec h$ has square $(h_t^2+\lvert\vec h\rvert^2)e_t+2h_ti\vec h$, which is $e_t$ only when $h_t^2+\lvert\vec h\rvert^2=1$ and $h_t\vec h=0$ — that is, only for the trivial roots and the family above. A general observable has arbitrary real eigenvalues $h_t\pm\lvert\vec h\rvert$, and it is the affine combination $h_te_t+\lvert\vec h\rvert\tilde\Xi$ of the identity and, for $\vec h\neq0$, the root $\tilde\Xi=i\vec h/\lvert\vec h\rvert$; its spectral projections are the halving pair of that root, but the observable itself is a root only when $h_t^2+\lvert\vec h\rvert^2=1$ and $h_t\vec h=0$. The roots of $+1$ are the **involutive** observables, the two-parameter family above together with the two central signs, inside the four-parameter family of general Hermitian elements. The reading names a subclass and does not exhaust the observables.

## Hermitian Idempotents as States

A Hermitian idempotent is an idempotent with $\tilde\Pi^{*}=\tilde\Pi$. The halving map of the Hermitian roots gives the family

$$
\boxed{\;\tilde\Pi_\pm(i\tilde\xi)=\tfrac12(e_t\pm i\tilde\xi),\qquad \tilde\xi\in S^2\;},
$$

which is the **Bloch sphere** of the pure states. The trace is one, $\operatorname{Tr}\tilde\Pi=2\operatorname{Sc}\tilde\Pi=1$, and the norm vanishes, so the state is on the boundary of the positive cone. The trivial cases $e_t$ and $0$ are the degenerate states of the trivial observables.

The same element carries the other state readings. The von Neumann entropy is a monotone function of the deviation $\operatorname{Sc}(\tilde{Ϛ}^2-\tilde{Ϛ})$, which vanishes exactly on the idempotents, and the Fisher information with respect to the Bloch radius diverges on them. The **pure state**, the **zero-entropy state**, the **zero-divisor state** and the **perfectly resolvable state** are four names for one element.

> **The Hermitian idempotents are the pure states** of the informational sector, and the two idempotents of a Hermitian root are the two eigenstates of the observable.

The spectral resolution makes the identification exact. For $\tilde\Xi=i\tilde\xi$,

$$
\boxed{\;\tilde\Xi\tilde\Pi_+=\tilde\Pi_+,\qquad \tilde\Xi\tilde\Pi_-=-\tilde\Pi_-,\qquad \tilde\Xi=\tilde\Pi_+-\tilde\Pi_-\;}.
$$

The observable, its two eigenvalues and its two states are one object and its two projections. The physical reading is that a **two-outcome measurement** is a root of $+1$: the root is the observable, the pair is the two outcomes, and the eigenvalues are the two signs.

The Born pairing completes the sentence. The probability of the outcome $+$ in the state $\tilde\Pi$ is the normalised Hermitian form $\langle\tilde\Pi,\tilde\Pi_+\rangle_{*}/\langle\tilde\Pi,e_t\rangle_{*}=\operatorname{Sc}(\tilde\Pi\tilde\Pi_+^{*})/\operatorname{Sc}(\tilde\Pi)$; in the $2\times2$ image, with $\operatorname{Tr}(\tilde\Pi)=1$, it reads $\operatorname{Tr}(\tilde\Pi\tilde\Pi_+^{*})=\operatorname{Tr}(\tilde\Pi\tilde\Pi_+)=2\operatorname{Sc}(\tilde\Pi\tilde\Pi_+^{*})$, the star being inert and the unstarred trace real and non-negative. The two probabilities sum to one because the pair is complete. The formula is the one of *The Informational Sector: States, Observables and Probability* and *The Born Rule from the Hermitian Form — Derivation and Comparison*; this article only locates it in the root–idempotent pair. The probability is not derived here, and no frequency is identified with it.

The boundary is again immediate. **Not every idempotent is a state.** The non-trivial roots produce a four-real-parameter family of idempotents that lie in no remarkable subspace and are not Hermitian; they are not orthogonal projections and are not states in the sense of the informational sector. The identification of idempotents with states is confined to the Hermitian ones. The mixed states, which are not idempotent at all, are the interior of the Bloch ball and belong to *The Bloch Ball as the Normalised Slice of the Future Light Cone*. The state as an idempotent of the algebra, and the process as the multiplication, are *The Operators: One-Sided, Two-Sided, Sandwich*.

## The Roots of Minus One

The central imaginary carries the roots of $+1$ to the roots of $-1$: if $\tilde\Xi^2=e_t$ then $(i\tilde\Xi)^2=-e_t$, and the map is a bijection because $i$ is central and invertible. The three families are carried to the three families of the roots of $-1$: the central scalars $\pm i$, the family $\pm\tilde\xi$ over the real pure unit quaternions, and the family $-\vec\xi'+i\vec\xi$ with the same two conditions.

> **A root of $-1$ is a local complex structure**: a choice of which element plays the role of $i$ in a local patch.

The central root $i$ is the distinguished choice. It commutes with every element and makes the algebra an algebra over $\mathbb{C}$. The other roots are local: each defines its own complex structure, and passing from one to another is a change of what plays the role of $i$. The physical reading — the local complex structure fixing the propagation of the fields and the speed of light of the patch — is owned by *The Local Complex Structure and the Speed of Light*, and is cited here rather than developed.

One sign statement belongs here. The central $i$ is anti-Hermitian, $i^{*}=-i$, so a Hermitian root of $+1$ is carried to an **anti-Hermitian** root of $-1$. The observables of the article lie in the informational sector $\mathbb{M}_+$; the local complex structures read off them lie in the material sector $\mathbb{M}_-$. The sign of the radicand separates the sectors. That is the algebraic reason a local complex structure is a material object and not an observable.

## The Same Equation Across the Twelve Structures

The equation is relative to the product, so the twelve structures carry twelve root sets. The comparison belongs to *Square Roots of One and the Idempotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* and to *The Physical Interpretation of the 12 Products*; four rows carry the reading.

| structure | roots of $+1$ | idempotents | reading |
| --- | --- | --- | --- |
| GPA, composition | $\pm e_t$ and the pure family | every root gives an idempotent | the involutions and the idempotents |
| GPS, probability | the unitary group $\mathrm{U}(2)$ | the Hermitian states | the reversible symmetries of the pairing |
| GQA, causality | the quadric $C=+1$ | the trivial pair only | the spacelike shell of the interval |
| GQS, gauge | the Krein quadric $\Delta=+1$ | the displaced family $-\tfrac12e_t+\tfrac{\sqrt3}{2}\vec u$ | the gauge band's determinate elements are units, hence reversible |
| the four brackets | none | none | an infinitesimal transformation has no involution and no state |

The pattern is the one the article has used. **The composition band carries the largest family of idempotents**, because every root of its $+1$ gives one; the physical states are the Hermitian members of that family. **The probability band carries the unitary symmetries**, because its root of $+1$ is the unitary group and its idempotents are the pure states. **The interval band and the brackets carry no nontrivial state**, because their square is not the plain square and their $+1$ is a shell or nothing. The gauge band is the exception on the other side: its idempotents are units of the algebra, so a determinate element of that band is reversible, unlike a pure state of the probability band. The complementation $e_t-\tilde\Pi$ also leaves the gauge family, so the complete-pair reading does not carry over to it. A root of $+1$ is therefore a statement about a band; a pure state needs a Hermitian idempotent, and only some bands supply one.

## Physical Readings

- **The observable is the root, the states are its pair.** The interpretation is that a two-outcome observable of the informational sector is a nontrivial Hermitian root of $+1$, and its two eigenstates are the idempotents of the halving map, with eigenvalues the two signs. Boundary: an identification of an algebraic involution with a measurement, and it adds no dynamics and no preferred direction.
- **Measurement is projection onto the pair.** The interpretation is that the spectral resolution $\tilde\Xi=\tilde\Pi_+-\tilde\Pi_-$ is the algebraic form of a measurement with two outcomes, the projection being the idempotent and the outcome being the sign. Boundary: the projection is a projection, not a collapse; the selection of one outcome is not derived.
- **The state is the idempotent, and the pure states are the Bloch sphere.** The interpretation is that the nontrivial Hermitian idempotents are the pure states, with trace one and norm zero, and the family is the Bloch sphere. Boundary: only the nontrivial Hermitian idempotents are states; the mixed states are not idempotent.
- **The direction of the root is the axis of the measurement.** The interpretation is that the two real parameters of the purely imaginary family are the direction on the sphere, so choosing a root is choosing a measurement axis. Boundary: the algebra fixes the two outcomes, not the choice of axis.
- **The invertible observable and the non-invertible state.** The interpretation is that the root is a unit and its nontrivial idempotents are zero divisors, so the nontrivial observable is reversible and the state is not. Boundary: a statement about invertibility, not about information loss in time.
- **The roots of $-1$ are local complex structures.** The interpretation is that a root of $-1$ is a local choice of $i$, the central one being global, and the Hermitian roots of $+1$ give the anti-Hermitian ones in the material sector. Boundary: the reading names a complex structure and does not derive the speed of light; that is *The Local Complex Structure and the Speed of Light*.

## Limits

- **Not every observable is a root of $+1$.** The identification is with the involutive observables. A general Hermitian element has arbitrary eigenvalues; it is not itself an involution, although its spectral projections are the halving pair of the root along its axis.
- **Not every idempotent is a state.** Only the Hermitian idempotents are orthogonal projections and pure states. The four-parameter family of non-Hermitian idempotents is not a state family.
- **The Born rule is not derived here.** The Hermitian form and its trace reading are cited from their owners; the article locates it between the root and the state and adds no derivation.
- **No preferred direction and no preferred state.** The family is the whole sphere, and no algebraic fact selects a point of it. A preferred axis would be an added structure.
- **No dynamics and no collapse.** The root and its pair are a kinematic identification. Nothing here says how a state evolves or how one outcome is selected.
- **Not every involution is an algebraic root.** The real structure $\flat=-{}^{*}$ is an antilinear involution whose eigenspaces are the two sectors; being antilinear it is not an element of the algebra, so it is a superselection structure and not a root of $+1$.
- **The cross-structure table is a summary.** The classification of the twelve root sets is owned by the mathematics article and by *The Physical Interpretation of the 12 Products*; only the rows needed for the reading are quoted.

## Summary

The plain product at $+1$ gives the roots $\tilde\Xi^2=e_t$ and the idempotents $\tilde\Pi^2=\tilde\Pi$, and the halving map $\tilde\Xi\mapsto\tfrac12(e_t+\tilde\Xi)$ is a bijection between them. The roots are the two central scalars, the purely imaginary family $\pm i\tilde\xi$ over the real unit sphere, and the non-trivial four-parameter family; every root is a unit, and only the trivial and purely imaginary roots are Hermitian.

The Hermitian roots are read as the involutive observables, the Hermitian idempotents as the pure states, and, for a nontrivial root, its two idempotents as its two eigenstates. Such a root is the difference of its pair, acts by $+1$ and $-1$ on the two, and its idempotents are zero divisors of trace one and vanishing norm; the trivial roots $\pm e_t$ are the degenerate cases. The non-Hermitian roots and idempotents are neither observables nor states. The roots of $-1$ are the local complex structures, anti-Hermitian when read off the Hermitian roots, and they lie in the material sector. Across the twelve structures the composition band carries the largest idempotent family, the probability band the unitary symmetries, the gauge band the reversible determinate elements, and the interval band and the brackets no nontrivial state.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde\Xi$ | a root of a central value |
| $\tilde\Pi$, $\tilde\Pi_\pm$ | an idempotent and the two members of a complete pair |
| $\tilde\Pi_\pm(\tilde\Xi)=\tfrac12(e_t\pm\tilde\Xi)$ | the halving map and its two branches |
| $\mathbb{M}_\pm$ | the informational (Hermitian) and material (anti-Hermitian) sectors |
| $\operatorname{Sc}$, $\operatorname{Tr}=2\operatorname{Sc}$ | the scalar part and the trace |
| $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2$ | the biquaternion norm |
| $\mathrm{GPA}$, $\mathrm{GPS}$, $\mathrm{GQA}$, $\mathrm{GQS}$ | the plain algebra, the plain sesqualgebra, the quaternionic algebra and the quaternionic sesqualgebra |
| $S^2$ | the real unit sphere of directions of $\tilde\xi$ |

## Further Reading

- [Square Roots of One and the Idempotents of the Biquaternion Algebra](../articles_maths/square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html), for the classification, the halving map and the pair map.
- [Square Roots of Zero and the Nilpotents of the Biquaternion Algebra](../articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-biquaternion-algebra.html), for the other central value and the nilpotent cone.
- [Ideals and Peirce Decomposition of the Biquaternion Algebra](../articles_maths/ideals-and-peirce-decomposition-of-the-biquaternion-algebra.html), for orthogonality, primitivity and the ideals an idempotent generates.
- [The Four Forms and the Four Algebraic Norms](../articles_maths/the-four-forms-and-the-four-algebraic-norms.html), for the sectors, the conjugations and the trace.
- [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html), for the sector, the Bloch ball and the Born pairing.
- [The Roots of a General Element: Mass, Frames and the Mass Shell](the-roots-of-a-general-element-mass-frames-and-the-mass-shell.html), for the general value and the failure of the square-root formula off the cone.
- [The Local Complex Structure and the Speed of Light](the-local-complex-structure-and-the-speed-of-light.html), for the physical reading of the roots of $-1$.
- [The S-Matrix in Biquaternionic Form](the-s-matrix-in-biquaternionic-form.html), for the unitary root $\tilde S\tilde S^{*}=e_t$ of a single mode.
- [The Two-Sheeted Cover and the Topology of Boosts in Biquaternionic Form](the-two-sheeted-cover-and-the-topology-of-boosts-in-biquaternionic-form.html), for $R(2\pi)=-e_t$ and the double cover.
- [Von Neumann Entropy and the Biquaternion Norm](von-neumann-entropy-and-the-biquaternion-norm.html) and [Fisher Information and the Biquaternion Norm](fisher-information-and-the-biquaternion-norm.html), for the zero-entropy and perfectly resolvable readings of the idempotent.
- [The Physical Interpretation of the 12 Products](the-physical-interpretation-of-the-12-products.html), for the full comparison of the twelve root sets.
