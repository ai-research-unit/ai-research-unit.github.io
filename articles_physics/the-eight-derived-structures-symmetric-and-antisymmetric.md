# __The Eight Derived Structures: Symmetric and Antisymmetric__

## Introduction

Every one of the four general products of the biquaternion complex space splits into a symmetric and an antisymmetric part. The four general products give four parents, and the four splits give the **eight derived structures**: the symmetric and antisymmetric plain algebra and sesqualgebra, the symmetric and antisymmetric quaternionic algebra and sesqualgebra. The eight are not a formal decoration of the parents. Each is a product in its own right, with its own values, its own form, its own law and its own physical job: commutativity, positivity, coupling and metric on the symmetric side; rotation, phase, obstruction and polarisation on the antisymmetric side.

This article reads the eight one by one, then the two identities that decide which of them are a Jordan or a Lie product, then the reconstruction of each parent from its two halves, and finally the twelve structures side by side. It owns no theorem. The mathematics is *The Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* and *The Realification of the Eight Derived Structures*; the physical interpretations are gathered from the eleven structure drafts of this category. The general plain algebra is read in *The Four General Products: Composition, Probability, Causality, Gauge*, and this article only quotes it as a parent.

The four words of the symmetric half and the four words of the antisymmetric half are the thread of the article. A splitting is not a classification by itself, but here it is: the symmetric half keeps the scalar part of the parent and loses the direction, the antisymmetric half keeps the direction and loses the scalar part, and the physical difference between measuring and generating is that loss.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The twelve products, their multiplication tables and their values | [The 12 Products of the Biquaternioid $\mathbb{C}$ Space](../articles_maths/the-12-products-of-the-biquaternioid-complex-space.html) |
| The twelve structures, their products, values, units and identities | [The Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space](../articles_maths/the-algebraic-structures-over-the-biquaternioid-c-space.html) |
| The Jordan and Jacobi identities, the two that hold and the six witnesses of failure | [The Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space](../articles_maths/the-algebraic-structures-over-the-biquaternioid-c-space.html) |
| The realification, the real dimension, the real operators and the signatures | [The Realification of the Eight Derived Structures](../articles_maths/the-realification-of-the-eight-derived-structures.html) |
| The four forms and their signatures | [The 4 Forms over the Biquaternioid $\mathbb{C}$ Space](../articles_maths/the-4-forms-over-the-biquaternioid-c-space.html) |
| The four algebraic norms and their definiteness and multiplicativity | [The 4 Algebraic Norms over the Biquaternioid $\mathbb{C}$ Space](../articles_maths/the-4-algebraic-norms-over-the-biquaternioid-c-space.html) |

## The Eight and Their Parents

### One Product, Two Parts

Let $\circ$ be one of the four general products. Its symmetric and antisymmetric parts are

$$
S(x,y)=\tfrac12\bigl(x\circ y+y\circ x\bigr),
\qquad
A(x,y)=\tfrac12\bigl(x\circ y-y\circ x\bigr),
$$

so that $x\circ y=S(x,y)+A(x,y)$ for every pair. For the two sesquilinear parents the exchange is not the plain one: the second term is the conjugate of the product in the opposite order,

$$
S(x,y)=\tfrac12\bigl(x\circ y^{*}+\overline{y\circ x^{*}}\bigr),
\qquad
A(x,y)=\tfrac12\bigl(x\circ y^{*}-\overline{y\circ x^{*}}\bigr).
$$

In both families the split is a split of the **product map**, not of an algebra. The symmetric part survives the exchange of the two factors; the antisymmetric part changes sign. Neither part is closed under composition in general, and the parent is not the direct sum of the two as an algebra. What is true is that the parent is the sum of the two as products on the same vector space.

The associativity of the parent decides which identities survive: the symmetrisation of an associative product is a Jordan product, and its antisymmetrisation is a Lie product. Of the four parents only the general plain algebra is associative. That single fact is why the plain pair, and only the plain pair, carries the two classical nonassociative algebras.

### The Three Non-Plain Parents

The general plain sesqualgebra $\mathrm{GPS}$ is the probability band. Its product is $\tilde Q_1\tilde Q_2^{*}$, its scalar part is the positive definite Hermitian form $\langle\tilde Q_1,\tilde Q_2\rangle_{*}$, and its square has rank two off the zero-divisor cone and at most one on it. Its two slots are a state and an observable: the linear slot is prepared, the conjugate-linear one is measured. It has a right unit alone. Its symmetric part is $\mathrm{SPS}$ and its antisymmetric part $\mathrm{APS}$.

The general quaternionic algebra $\mathrm{GQA}$ is the causality band. Its product is $\tilde Q_1^{\natural}\tilde Q_2$, its square is central for every element, and that central value is the interval $\langle\tilde Q\rangle_{\natural}e_t$. Its null set is the causal cone; its norm-one elements are the Lorentz parameters, and on the material sector they act by the dagger sandwich $\tilde X\mapsto\tilde U\tilde X\tilde U^{*}$. It has a left unit alone and is not associative. Its symmetric part is $\mathrm{SQA}$ and its antisymmetric part $\mathrm{AQA}$.

The general quaternionic sesqualgebra $\mathrm{GQS}$ is the gauge band. Its product is $\tilde Q_1^{\natural}\tilde Q_2^{*}$, its form is the indefinite Krein form of signature $(1,3)$ over $\mathbb{C}$ and $(2,6)$ over $\mathbb{R}$, and its isometry group is $\mathrm{U}(1,3)$ over $\mathbb{C}$ and $O(2,6)$ over $\mathbb{R}$. It has no unit, selects no direction of positivity and supplies no state; it is the structure of admissible transformations. Its symmetric part is $\mathrm{SQS}$ and its antisymmetric part $\mathrm{AQS}$.

The fourth parent, the general plain algebra $\mathrm{GPA}$, is the composition band: associative, with the unit $e_t$ on both sides, and with the zero-divisor cone as the wall of invertibility. Its two parts are $\mathrm{SPA}$ and $\mathrm{APA}$, read here while the parent is left to *The Four General Products: Composition, Probability, Causality, Gauge*.

| the parent | the product | the square | the word | the unit |
| --- | --- | --- | --- | --- |
| $\mathrm{GPA}$ | $\tilde Q_1\tilde Q_2$ | $\tilde Q^{2}$ | composition | $e_t$ on both sides |
| $\mathrm{GPS}$ | $\tilde Q_1\tilde Q_2^{*}$ | $\tilde Q\tilde Q^{*}$, Hermitian and rank-bearing | probability | $e_t$ on the right alone |
| $\mathrm{GQA}$ | $\tilde Q_1^{\natural}\tilde Q_2$ | $\langle\tilde Q\rangle_{\natural}e_t$, central and signed | causality | $e_t$ on the left alone |
| $\mathrm{GQS}$ | $\tilde Q_1^{\natural}\tilde Q_2^{*}$ | the Krein value, indefinite | gauge | none |

### The Eight at a Glance

The eight derived structures carry the product, the values and the word that the rest of the article unfolds.

| the structure | the parent | the product | the values | the word |
| --- | --- | --- | --- | --- |
| $\mathrm{SPA}$ | $\mathrm{GPA}$ | $\tfrac12(\tilde Q_1\tilde Q_2+\tilde Q_2\tilde Q_1)$ | the whole space | commutativity |
| $\mathrm{SPS}$ | $\mathrm{GPS}$ | $\tfrac12(\tilde Q_1\tilde Q_2^{*}+\overline{\tilde Q_2\tilde Q_1^{*}})$ | the centre | positivity |
| $\mathrm{SQA}$ | $\mathrm{GQA}$ | $\tfrac12(\tilde Q_1^{\natural}\tilde Q_2+\tilde Q_2^{\natural}\tilde Q_1)$ | the centre | coupling |
| $\mathrm{SQS}$ | $\mathrm{GQS}$ | $\tfrac12(\tilde Q_1^{\natural}\tilde Q_2^{*}+\overline{\tilde Q_2^{\natural}\tilde Q_1^{*}})$ | no remarkable subspace | metric |
| $\mathrm{APA}$ | $\mathrm{GPA}$ | $\tfrac12(\tilde Q_1\tilde Q_2-\tilde Q_2\tilde Q_1)$ | the vector subspace | rotation |
| $\mathrm{APS}$ | $\mathrm{GPS}$ | $\tfrac12(\tilde Q_1\tilde Q_2^{*}-\overline{\tilde Q_2\tilde Q_1^{*}})$ | the vector subspace | phase |
| $\mathrm{AQA}$ | $\mathrm{GQA}$ | $\tfrac12(\tilde Q_1^{\natural}\tilde Q_2-\tilde Q_2^{\natural}\tilde Q_1)$ | the vector subspace | obstruction |
| $\mathrm{AQS}$ | $\mathrm{GQS}$ | $\tfrac12(\tilde Q_1^{\natural}\tilde Q_2^{*}-\overline{\tilde Q_2^{\natural}\tilde Q_1^{*}})$ | the vector subspace | polarisation |

## The Symmetric Four

### $\mathrm{SPA}$, Commutativity

The symmetric plain algebra is the Jordan product $\tilde Q_1\bullet\tilde Q_2=\tfrac12(\tilde Q_1\tilde Q_2+\tilde Q_2\tilde Q_1)$. It is commutative, it satisfies the Jordan identity, it has the two-sided unit $e_t$, and its values fill the whole space. On two material four-vectors $\tilde X=ia_1e_t+\vec b_1$ and $\tilde Y=ia_2e_t+\vec b_2$ its scalar part is $-a_1a_2-\vec b_1\cdot\vec b_2$, the negative Euclidean overlap, and not the interval. The interval belongs to the quaternionic symmetric product; the two must not be conflated.

The physical content of commutativity is that the product keeps the order-free part of a composition and discards the part that depends on the order. Two orthogonal displacements have no order-free part: $\vec e_x\bullet\vec e_y=0$, and the whole composition is the rotation $\vec e_z$. Two parallel displacements have the time direction as their order-free part. The symmetrised product of two operations is the common part of the two orders, and that is why it is the product of the observables and not of the generators.

On the Hermitian sector the product is the Jordan product of the observables, and the sector is closed. The material sector is not a Jordan algebra of its own: the symmetrised product of two anti-Hermitian elements is Hermitian, while the product itself need not be, so the sector is not closed, and a spacetime displacement is not an observable in the quantum sense. A four-vector labels an event and generates a translation, but its values are not read off a state. The unit-norm elements act by the dagger sandwich as isometries of the interval; for the rotors the dagger sandwich is the inner automorphism, and for the boosts it is not. The reflections are form-preserving operators that the product does not supply.

The form is the plain bilinear form of signature $(4,4)$ over $\mathbb{R}$. It is indefinite and vanishes on the complex cone, so it fixes no probability and ranks no state. It is the metric side of the frame, not the state side.

### $\mathrm{SPS}$, Positivity

The symmetric plain sesqualgebra is the scalar-valued symmetrisation $\tilde Q_1\star\tilde Q_2=\langle\tilde Q_1,\tilde Q_2\rangle_{*}e_t$, the real part of the Born pairing. It is conjugate-commutative, its values lie in the centre, it has no unit, and it is not a Jordan product. Its form is the positive definite Hermitian form of signature $(8,0)$ over $\mathbb{R}$.

The physical interpretation is direct: **a probability is a number**. The value is central, so it can be added, multiplied and counted like a scalar, and it survives a change of the local complex structure. Positivity makes the number a probability and not a mere scalar. The two slots are a prepared state and a measured effect, the conjugation sitting in one slot and not in the other; that asymmetry distinguishes a state from an effect. The no-cloning obstruction and the in-out structure of the scattering matrix have the same two-slot shape.

The band asks and never moves. The rank-one operators collapse every element to the central line, so they do not carry a generic state to a state; the calculus is a calculus of questions and not of motions, and a transformation of a state is the sandwich of the parent, not a multiplication of this one. That is the operator content of the separation between the positivity band and the composition band.

The absence of a unit is the same fact read algebraically. $e_t$ is not a unit, because $e_t\star\tilde Q=\overline{Q_t}e_t$ and not $\tilde Q$. A value that is a number cannot act on an operation, so a structure whose values are numbers has no reversible element of its own.

### $\mathrm{SQA}$, Coupling

The symmetric quaternionic algebra is the scalar-valued symmetrisation $\tilde Q_1\star\tilde Q_2=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t$. It is commutative but not a Jordan product, its values lie in the centre, it has no unit, and its form is the quaternion form of signature $(4,4)$ over $\mathbb{R}$.

For two four-vectors its scalar part is $-a_1a_2+\vec b_1\cdot\vec b_2$. On the diagonal it is the interval $-a^{2}+\lvert\vec b\rvert^{2}$, whose zero set is the light cone and whose sign separates timelike from spacelike. The symmetric quaternionic product is therefore the **causal coupling** of two material operations: it answers whether two displacements can be connected by a signal, and its radical is the set of null separations. The band carries the metric and not the probability, and that is why its values are central numbers rather than states.

The comparison is a rank-one functional: its kernel is the hyperplane of operations that the coupling does not see, and its image is the central line. The coupling returns a number and not a direction. Its adjoint is the symmetry of the comparison and not a comparison, and the conjugation of a parameter belongs to the Hermitian form, not to the quaternion form. The spin group is not realised in the band: the symmetrisation destroys invertibility and leaves the double cover to the parent.

### $\mathrm{SQS}$, Metric

The symmetric quaternionic sesqualgebra is the symmetrisation of the fourth product. It is conjugate-commutative and not a Jordan product, it has no unit, and its values lie in no remarkable subspace: the value carries the scalar part $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}$ and the mixed vector part side by side. Its form is the Krein form of signature $(2,6)$ over $\mathbb{R}$.

The physical interpretation is the **symmetric part of the gauge metric**. The signature is indefinite, so the band selects no direction of positivity; a gauge calibration can compare two internal frames and cannot rank them. The value of a general pair lies in no remarkable subspace, and the self-pairing is in general not central. The standard reconstruction of a state space — positivity, a unit, a Jordan structure, a module action — does not reach the band. The metric belongs to the transformation side of the frame, whose invariants are the pairings left unchanged, not to the state side, whose invariants are positive numbers.

The minimal witness is $\tilde Q=e_t+\vec e_x$. Its symmetric square is $-2\vec e_x$, a non-central value, while a pure vector direction has the central square $-e_t$: the slightest mixing of a scale with a direction leaves the class of what can be measured. The operators of the band are a deformation, their scalar part a conformal factor and their traceless vector part a shear. The band deforms an element rather than rotating or translating it.

## The Antisymmetric Four

### $\mathrm{APA}$, Rotation

The antisymmetric plain algebra is the commutator $\tilde Q_1\star\tilde Q_2=\tfrac12(\tilde Q_1\tilde Q_2-\tilde Q_2\tilde Q_1)=\vec Q_1\times\vec Q_2$. It is alternating, it satisfies the Jacobi identity, it has no unit, and its values lie in the vector subspace. Its form vanishes identically.

The physical interpretation is the **Lie bracket of rotations**. The cross product of two material vectors generates a rotation, and the closure of the bracket is why the rotations form a group while the boosts do not. It is a material bracket, its values lying in the vector subspace, so it belongs to the compact half of the Lorentz algebra. The vector subspace with this product is a Lie algebra isomorphic to $\mathfrak{sl}(2,\mathbb{C})$, the quaternion subspace is $\mathbb{R}e_t\oplus\mathfrak{su}(2)$, and the anti-Hermitian subspace is $\mathfrak{u}(2)$.

Angular momentum and the Killing form are the two invariants of the material frame. The adjoint negating the parameter is the generator-observable dictionary: a skew-adjoint operator generates a form-preserving flow, its Hermitian multiple is measured, and angular momentum is $i$ times a generator. The band supplies generators and not observables. The sandwich is self-adjoint for every parameter because the two slots of an alternating product already differ by a sign, and it is the square of the finite rotation. The finite rotations are the multiplicative operators; the reflections are the form-preserving operators that the product cannot use.

### $\mathrm{APS}$, Phase

The antisymmetric plain sesqualgebra is the antisymmetrisation of the plain sesquilinear product. It is conjugate-alternating, it fails the Jacobi identity, it has no unit, and its values lie in the vector subspace. Its form vanishes identically.

The physical interpretation is the **imaginary part of the Born pairing**, and therefore the phase of an amplitude. Its values carry a direction, so it is the part of the pairing that the central generator moves; the phase of an amplitude is where the clock of the framework enters a measurement. One amplitude read through the two halves gives one number and one axis: the probability and the direction of the phase. Interference cannot be read off the real part alone, and that is why a pairing is not a metric.

The Jacobi failure is the statement that interference has no symmetry algebra of its own. Read against the clock, the failure is not a loss, because the phase itself is supplied by the central rotation; what is missing is a Lie algebra of phases, not the phase. An interference term is assembled from two amplitudes and is a relational datum, not an infinitesimal transformation. The antisymmetric sesquilinear form is a structure of interference and not a gauge algebra, the gauge algebra being carried by the quaternionic row. The phase operator has one handedness: the right family is the negative mirror of the left, and the antisymmetry ties the two together.

### $\mathrm{AQA}$, Obstruction

The antisymmetric quaternionic algebra is the antisymmetrisation $\tfrac12(\tilde Q_1^{\natural}\tilde Q_2-\tilde Q_2^{\natural}\tilde Q_1)$. It is alternating, it fails the Jacobi identity, it has no unit, and its values lie in the vector subspace. Its form vanishes identically.

The physical interpretation is **obstruction**. The bracket is the mixed term

$$
\tilde Q_1\star\tilde Q_2=Q_{1t}\vec Q_2-Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2,
$$

and the first two terms are the boost. On pure vectors the deviation vanishes, the product is minus the cross product, the operators close and the self-adjoint sandwiches are exactly the pure, rotation-like parameters. On mixed terms the deviation is nonzero and closure fails, and the boost-like parameters make the sandwich non-symmetric. The operator calculus therefore carries the compact rotations and fails on the boosts.

The failure is the algebraic origin of the boost obstruction. The non-compact generators do not close on a Lie algebra, and the gap is the mixed term $Q_{1t}\vec Q_2-Q_{2t}\vec Q_1$. The commutator of two boosts is a rotation, so the bracket closes on the six Lorentz generators where the informational bracket does not: that is the framework's reading of the Cartan decomposition. Read as generators, as symmetries or as forms, the band fails in the same way. The operators generate no Lie algebra and exponentiate to no group; every multiplication is singular, so the band carries no form-preserving operator, no isometry and no inner automorphism; and it has no non-degenerate invariant form, so the adjoint has to be imported and then leaves the family. An obstruction constrains an interpretation without supplying one.

### $\mathrm{AQS}$, Polarisation

The antisymmetric quaternionic sesqualgebra is the antisymmetrisation of the fourth product,

$$
\tilde Q_1\star\tilde Q_2=\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2^{*}-\tilde Q_2^{*}\tilde Q_1^{\natural}\bigr)=\vec Q_1\times\overline{\vec Q_2}.
$$

It is conjugate-alternating, it fails the Jacobi identity, it has no unit, and its values lie in the vector subspace. Its form vanishes identically.

The product returns an **axis**, and its magnitude is the area the pair spans. The axis is the physical content. It pairs a vector with the conjugate of another and returns the axial direction of the pair, the axis about which the two are rotated into one another. For two real vectors it is the ordinary cross product. The product answers "about which axis?", and its magnitude is the area and not a scalar charge. Every value is a pure vector, so the band carries no mass, no energy and no phase: a rotation of the internal frame has no scalar invariant and is invisible to the central clock.

The coefficient conjugation in the second slot is a reality condition. Physically the band is the pairing of a field with its conjugate field, the algebraic form of a charge-conjugation-invariant bilinear. The operators carry a direction and not a state: left multiplication by a parameter sends every element into the plane perpendicular to that parameter, so the operators are polarisers and analysers, they select an axis and cannot prepare a state. The adjoint reverses the parameter, which is the axial character of the cross product: the axis changes sign when the orientation of the pair is reversed, and an axial vector is not a polar vector.

The Jacobi failure is the sesquilinear obstruction. The bracket is a Lie bracket only after the collapse of the two involutions, and a genuine sesqualgebra forbids that collapse. The failure is visible on the real Lorentz generators, so it is a property of the sesquilinear pairing and not of the non-compactness of the boost.

## The Two Laws

### The Witness Table

Of the eight derived structures exactly two carry the product of a classical nonassociative algebra: $\mathrm{SPA}$ is a Jordan product and $\mathrm{APA}$ is a Lie product. The other six fail the identity of their kind, and each failure is witnessed on a single triple or a single element.

| the structure | the identity | the witness | the failure |
| --- | --- | --- | --- |
| $\mathrm{SPA}$ | Jordan | — | holds |
| $\mathrm{SPS}$ | Jordan | $x=y=\vec e_x$ | the sides are $0$ and $e_t$ |
| $\mathrm{SQA}$ | Jordan | $x=y=\vec e_x$ | the sides are $0$ and $e_t$ |
| $\mathrm{SQS}$ | Jordan | $x=y=\vec e_x$ | the sides are $-e_t$ and $e_t$ |
| $\mathrm{APA}$ | Jacobi | — | holds |
| $\mathrm{APS}$ | Jacobi | $(e_t,\vec e_x,\vec e_y)$ | $\vec e_z$ |
| $\mathrm{AQA}$ | Jacobi | $(e_t,\vec e_x,\vec e_y)$ | $-\vec e_z$ |
| $\mathrm{AQS}$ | Jacobi | $(\vec e_x,\vec e_x,i\vec e_y)$ | $-2i\vec e_y$ |

The last column of the three Jacobi rows is the cyclic sum, and the two sides of the Jordan rows are $(x^{2}\bullet x)\bullet x$ and $x^{2}\bullet(x\bullet x)$.

### Why the Six Fail

The three Jordan failures have one algebraic shape: in the non-associative symmetrisations the square of the pure vector $\vec e_x$ is central, so the iteration of the product has already forgotten the direction before the identity can compare the two orders. For $\mathrm{SPS}$ and $\mathrm{SQA}$ the square is $e_t$ and the two sides differ by $e_t$; for $\mathrm{SQS}$ the square is $-e_t$ and the two sides differ by $2e_t$. Physically the failure says that a coupling with a central square is not an algebra of observables: a number cannot remember the direction it came from, and measuring the coupling twice does not reproduce the coupling of the square.

The three Jacobi failures have three different reasons, and the differences are physical. For $\mathrm{AQA}$ the culprit is the non-associativity of the quaternionic product it comes from: the natural conjugation in one slot breaks the associativity that the Jacobi identity of a commutator needs. For $\mathrm{APS}$ and $\mathrm{AQS}$ the culprit is the sesquilinear obstruction: the antisymmetrisation of a sesquilinear product is a Lie bracket only after the collapse of the two involutions, and a genuine sesqualgebra forbids that collapse. The witness of $\mathrm{AQS}$ is the complex one of the table: the cyclic sum at $(\vec e_x,\vec e_x,i\vec e_y)$ is $-2i\vec e_y$. The failure is therefore a statement about the sesquilinear pairing and not about a real subspace.

The pattern of the table is the pattern of the four words. Composition has an order-free part that is a Jordan algebra and an order-sensitive part that is a Lie algebra, because the plain product is associative. Probability, causality and gauge have neither: their symmetric halves are couplings that forget the direction, and their antisymmetric halves are brackets that do not close. The four words of the symmetric side are the four ways a product can keep a value and lose an order; the four words of the antisymmetric side are the four ways a product can keep an order and lose a value.

## The Reconstruction

### The Split of the Product

The parent is reconstructed from its two parts by addition, $x\circ y=S(x,y)+A(x,y)$, and the reconstruction is exact for every pair in all four families. What the reconstruction does **not** give is a direct sum of algebras. The product of two symmetric elements need not be symmetric, the product of two antisymmetric elements need not be antisymmetric, and the two parts do not close separately in general. The split decomposes the product, not the algebra.

The physical interpretation is the distinction between the two questions a product can answer. The symmetric part answers "what is common to the two orders?" and the antisymmetric part answers "what changes when the orders are exchanged?". A measurement is the first question: two measurements composed symmetrically give an observable, and the order of the two measurements does not matter for their symmetrised composition. A generation is the second: the commutator of two generators is a generator, and the order of two infinitesimal transformations is the rotation between them. The parent carries both, and the two parts are the two readings of one process.

The forms follow the split. The scalar part of the symmetric part is the scalar part of the parent; the scalar part of the antisymmetric part is zero, because an antisymmetrisation kills the scalar part. The whole form of a parent therefore lives in its symmetric half, and the antisymmetric half carries no scalar value at all. That is the algebraic reason why a bracket can be a generator and not an observable, and why a coupling can be a value and not a motion: the form is the scalar value, and only the symmetric half has it.

### The Forms of the Eight

| the structure | the form | the signature over $\mathbb{R}$ | the null set |
| --- | --- | --- | --- |
| $\mathrm{SPA}$ | the plain bilinear form $\langle\cdot,\cdot\rangle$ | $(4,4)$ | the complex cone |
| $\mathrm{SPS}$ | the Hermitian form $\langle\cdot,\cdot\rangle_{*}$ | $(8,0)$ | $\{0\}$ |
| $\mathrm{SQA}$ | the quaternion form $\langle\cdot,\cdot\rangle_{\natural}$ | $(4,4)$ | the zero-divisor cone |
| $\mathrm{SQS}$ | the Krein form $\langle\cdot,\cdot\rangle_{\natural*}$ | $(2,6)$ | the Krein cone |
| $\mathrm{APA}$, $\mathrm{APS}$, $\mathrm{AQA}$, $\mathrm{AQS}$ | the zero form | $(0,0)$ | the whole space |

The four symmetric structures carry the four forms, one each, and the four antisymmetric structures carry none. The three indefinite forms are those of $\mathrm{SPA}$, $\mathrm{SQA}$ and $\mathrm{SQS}$; the definite one is that of $\mathrm{SPS}$. The zero form of the four brackets is the form-level statement of the word *generator*: a bracket has a direction and no scalar value.

### The Twelve Compared

| the structure | the parent | the values | the form | the identity | the unit |
| --- | --- | --- | --- | --- | --- |
| $\mathrm{GPA}$ | — | the whole space | $\langle\cdot,\cdot\rangle$ | associative | $e_t$ on both sides |
| $\mathrm{GPS}$ | — | the whole space | $\langle\cdot,\cdot\rangle_{*}$ | none, sesquilinear | $e_t$ on the right alone |
| $\mathrm{GQA}$ | — | the whole space | $\langle\cdot,\cdot\rangle_{\natural}$ | none, non-associative | $e_t$ on the left alone |
| $\mathrm{GQS}$ | — | the whole space | $\langle\cdot,\cdot\rangle_{\natural*}$ | none, sesquilinear | none |
| $\mathrm{SPA}$ | $\mathrm{GPA}$ | the whole space | $\langle\cdot,\cdot\rangle$ | Jordan | $e_t$ on both sides |
| $\mathrm{SPS}$ | $\mathrm{GPS}$ | the centre | $\langle\cdot,\cdot\rangle_{*}$ | fails Jordan | none |
| $\mathrm{SQA}$ | $\mathrm{GQA}$ | the centre | $\langle\cdot,\cdot\rangle_{\natural}$ | fails Jordan | none |
| $\mathrm{SQS}$ | $\mathrm{GQS}$ | no remarkable subspace | $\langle\cdot,\cdot\rangle_{\natural*}$ | fails Jordan | none |
| $\mathrm{APA}$ | $\mathrm{GPA}$ | the vector subspace | $0$ | Lie | none |
| $\mathrm{APS}$ | $\mathrm{GPS}$ | the vector subspace | $0$ | fails Jacobi | none |
| $\mathrm{AQA}$ | $\mathrm{GQA}$ | the vector subspace | $0$ | fails Jacobi | none |
| $\mathrm{AQS}$ | $\mathrm{GQS}$ | the vector subspace | $0$ | fails Jacobi | none |

Read by column, the table gives the three divisions of the twelve: the family (four parents, four symmetric parts, four antisymmetric parts), the value (the whole space, the centre, the vector subspace, or no remarkable subspace) and the law (only the plain pair carries a classical algebra). Read by row, it gives the one exact coincidence: a parent and its symmetric part share the form. The unit is shared only for the plain pair, because the symmetrisation of a sesquilinear product replaces the unit by a conjugation. The antisymmetric part shares neither. That coincidence is why the symmetric half is the half that measures: the form is the scalar part, and the scalar part is the only thing a state can be paired with.

## The Boundary

The algebra proves the split, the eight products, the two identities and the six witnesses. It does not prove that the eight words are the only interpretations of the eight structures. The words *commutativity*, *positivity*, *coupling*, *metric*, *rotation*, *phase*, *obstruction* and *polarisation* are the framework's naming of a proved structure, and each naming is a claim about which physical job the structure can carry, not a theorem of the algebra.

Three boundaries follow. The symmetric parts are not, in general, Jordan algebras: only $\mathrm{SPA}$ is one, and calling $\mathrm{SPS}$ or $\mathrm{SQS}$ a Jordan algebra would erase the witnesses. The antisymmetric parts are not, in general, Lie algebras: only $\mathrm{APA}$ is one, and the Jacobi failures are the content of the words *phase*, *obstruction* and *polarisation*. The reconstruction $G=S+A$ is exact as a decomposition of the product and does not make the parent a direct sum of two algebras.

The general plain algebra is owned by *The Four General Products: Composition, Probability, Causality, Gauge*. The eight structures are read over $\mathbb{R}$ in *The Realification of the Eight Derived Structures*, which owns the real dimension, the real operators and the signatures quoted here.

## Summary

The four general products split into eight derived structures, and the split is a split of each product into an order-free half and an order-sensitive half. The symmetric half keeps the value of the parent and carries the four forms; the antisymmetric half keeps the direction and carries the zero form. Of the eight, only $\mathrm{SPA}$ is a Jordan product and only $\mathrm{APA}$ is a Lie product, because only the plain parent is associative. The other six fail the identity of their kind, with the witnesses $\vec e_x$ for the three Jordan failures and the triples $(e_t,\vec e_x,\vec e_y)$ and $(\vec e_x,\vec e_x,i\vec e_y)$ for the three Jacobi failures. The parent is reconstructed from its two parts by addition, and the reconstruction is exact as a decomposition of the product, not as a direct sum of algebras. The twelve structures compared give three divisions: the family, the values and the law.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathrm{GPA}$, $\mathrm{GPS}$, $\mathrm{GQA}$, $\mathrm{GQS}$ | the four general parents: composition, probability, causality, gauge |
| $\mathrm{SPA}$, $\mathrm{SPS}$, $\mathrm{SQA}$, $\mathrm{SQS}$ | their symmetric parts: commutativity, positivity, coupling, metric |
| $\mathrm{APA}$, $\mathrm{APS}$, $\mathrm{AQA}$, $\mathrm{AQS}$ | their antisymmetric parts: rotation, phase, obstruction, polarisation |
| $S(x,y)$, $A(x,y)$ | the symmetric and antisymmetric parts of a product |
| $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{*}$, $\langle\cdot,\cdot\rangle_{\natural}$, $\langle\cdot,\cdot\rangle_{\natural*}$ | the plain, Hermitian, quaternion and Krein forms |
| $e_t$, $\vec e_x,\vec e_y,\vec e_z$ | the unit and the three quaternion directions, with $\vec e_x^{2}=-e_t$ |
| the centre $\mathbb{C}_{\mathbb{B}}$ | the scalars $\mathbb{C}e_t$, the values of the two couplings |
| the vector subspace | the values of the four brackets |

## Further Reading

- [The Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space](../articles_maths/the-algebraic-structures-over-the-biquaternioid-c-space.html), for the twelve products, the identities and the witnesses.
- [The Realification of the Eight Derived Structures](../articles_maths/the-realification-of-the-eight-derived-structures.html), for the real dimension, the real operators and the signatures.
- *The Twelve Structures Compared: Product, Law and Form*, for the same comparison read by product, law and form rather than by family, value and law.
- *The 12 Products of the Biquaternioid Complex Space*, for the multiplication tables and the coordinates of the twelve.
- [The 4 Forms over the Biquaternioid $\mathbb{C}$ Space](../articles_maths/the-4-forms-over-the-biquaternioid-c-space.html), for the four forms and their Gram matrices.
- *The Four General Products: Composition, Probability, Causality, Gauge*, for the four parents.
- *The Four Forms and the Four Algebraic Norms*, for the forms read physically.
- *Zero Divisors Across the Twelve Structures*, *Annihilators Across the Twelve Structures* and *Roots Across the Twelve Structures*, the three companions of this block.
