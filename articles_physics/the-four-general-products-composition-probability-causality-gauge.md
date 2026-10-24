# __The Four General Products: Composition, Probability, Causality, Gauge__

## Introduction

The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries four general products and not one. Each sends a pair $(\tilde Q_1,\tilde Q_2)$ to an element of $\mathbb{B}$, each is written on the same eight real coordinates, and the four differ in one point alone: whether the first argument, the second, or both are read through a conjugation before the multiplication. This article gives the four a physical job. The general plain bilinear product is **composition**, the general plain sesquilinear product is **probability**, the general quaternionic bilinear product is **causality**, and the general quaternionic sesquilinear product is **gauge**.

The naming is a reading and not a theorem. The algebra proves that the four products exist, that they are the four settings of one construction, and what each of them does; it does not prove that a relativistic quantum theory needs exactly these four jobs, nor that no other assignment of the four is possible. What the naming has in its favour is that the four jobs are independent: a theory needs a rule for combining operations, a rule for assigning probabilities, a rule for deciding which events can influence which, and a rule for handling the redundancy of its description. The four forms supply one candidate for each. The article states that, and it states where the statement stops.

The article owns no new theorem. Each result is stated in a sentence, the mathematics article that proves it is linked, and the reading is given with its boundary.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The four products, their coordinate formulas and their scalar–vector forms | [The Four General Products and Their Relations](../articles_maths/the-four-general-products-and-their-relations.html) |
| The property table, the two slots, the units, associativity and the scalar square | [The Four General Products and Their Relations](../articles_maths/the-four-general-products-and-their-relations.html) |
| The identities linking the four products and the left multiplications | [The Four General Products and Their Relations](../articles_maths/the-four-general-products-and-their-relations.html) |
| The twelve products and the symmetric and antisymmetric halves | [Symmetric and Antisymmetric Decomposition of the Four General Products](../articles_maths/symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html), [The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](../articles_maths/the-algebraic-structures-over-the-biquaternion-c-space.html) |
| The four forms, their Gram matrices, their signatures and their isometry groups | [The Four Forms and the Four Algebraic Norms](../articles_maths/the-four-forms-and-the-four-algebraic-norms.html) |
| The four algebraic norms, multiplicativity, definiteness and the zero divisors | [The Four Forms and the Four Algebraic Norms](../articles_maths/the-four-forms-and-the-four-algebraic-norms.html) |
| The restrictions of the forms to the two sectors and the remarkable subspaces | [Remarkable Subspaces and the Four Forms](../articles_maths/remarkable-subspaces-and-the-four-forms.html) |
| Invertibility, the zero-divisor cone and the unit group | [Norm and Invertibility in the Biquaternion Algebra](../articles_maths/norm-and-invertibility-in-the-biquaternion-algebra.html) |
| The realification and its effect on the twelve products and the four forms | [The Realification and the Effect of the Change of Scalars](../articles_maths/the-realification-and-the-effect-of-the-change-of-scalars.html) |

## The One Mechanism

### The Four Settings of One Rule

The four products are not four independent definitions. Each is the plain product with a conjugation inserted in one or both slots:

$$
\boxed{\;\tilde Q_1\star_{K_1K_2}\tilde Q_2=K_1(\tilde Q_1)\,K_2(\tilde Q_2),
\qquad
K_1\in\{\mathrm{id},{}^{\natural}\},
\qquad
K_2\in\{\mathrm{id},{}^{*}\}\;},
$$

where ${}^{\natural}$ is the natural conjugation, fixing the central $i$ and negating the three vector units, and ${}^{*}=\bar{\cdot}\circ{}^{\natural}$ is the Hermitian conjugation. The two insertions commute, each is its own inverse, and the four settings form a group isomorphic to $\mathbb{Z}_2\times\mathbb{Z}_2$. The four general products are the four settings of that one rule.

| Product | Slots | Scalar Part |
| --- | --- | --- |
| $\tilde Q_1\tilde Q_2$ | $(\mathrm{id},\mathrm{id})$ | $Q_{1,0}Q_{2t}-(\vec Q_1,\vec Q_2)$ |
| $\tilde Q_1\tilde Q_2^{*}$ | $(\mathrm{id},{}^{*})$ | $Q_{1,0}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2})$ |
| $\tilde Q_1^{\natural}\tilde Q_2$ | $({}^{\natural},\mathrm{id})$ | $Q_{1,0}Q_{2t}+(\vec Q_1,\vec Q_2)$ |
| $\tilde Q_1^{\natural}\tilde Q_2^{*}$ | $({}^{\natural},{}^{*})$ | $Q_{1,0}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})$ |

The two slots are the two questions the rest of the article asks of the four. The **second slot** decides whether the operation can be iterated: read without the star, the product is $\mathbb{C}$-bilinear in its second argument and can be iterated; read with the star, it is conjugate-linear there and can only be evaluated. The **first slot** decides the form: read as it stands, the form is definite on each sector; read through ${}^{\natural}$, it is indefinite on each sector and carries a cone. Composition and causality are the settings with $K_2=\mathrm{id}$; probability and gauge are the settings with $K_2={}^{*}$.

### The Property Table

The properties follow the slots, and one of them follows both at once. The table is the one of *The Four General Products and Their Relations*, with the entries that the readings use.

| Property | $\tilde Q_1\tilde Q_2$ | $\tilde Q_1\tilde Q_2^{*}$ | $\tilde Q_1^{\natural}\tilde Q_2$ | $\tilde Q_1^{\natural}\tilde Q_2^{*}$ |
| --- | --- | --- | --- | --- |
| $\mathbb{C}$-linear in the first argument | yes | yes | yes | yes |
| $\mathbb{C}$-linear in the second argument | yes | no | yes | no |
| associative | yes | no | no | no |
| unit on the left | yes | no | yes | no |
| unit on the right | yes | yes | no | no |
| left multiplications form a monoid | yes | no | yes | no |
| multiplication of an algebra over $\mathbb{C}$ (associative or not) | yes | no | yes | no |
| multiplication of a sesqualgebra over $\mathbb{C}$ | no | yes | no | yes |

Only the plain bilinear product is a multiplication in the strict sense: it is associative, two-sidedly unital and $\mathbb{C}$-bilinear, and it makes $\mathbb{B}$ an associative algebra over $\mathbb{C}$. The quaternionic bilinear product is $\mathbb{C}$-bilinear and has the left unit alone; it is not associative, and its left multiplications still form a monoid, isomorphic to the opposite of the multiplicative monoid of $\mathbb{B}$. The two products carrying the star are not bilinear over $\mathbb{C}$ at all: they are the multiplications of a sesqualgebra, and within the pair the plain one is the derived operation $\tilde Q_1\star\tilde Q_2=\tilde Q_1\tilde Q_2^{*}$ with the right unit, while the quaternionic one is not derived and has no unit.

The associativity row is the one row the slots decide only jointly: it holds exactly when both slots are trivial. It is proved in $\mathbb{B}$ by one triple of basis elements for each of the three twisted settings, and the reason is always the same: the plain product lets the parentheses be dropped, and the operation then conjugates a factor and transposes two of them. Associativity of the plain product is therefore not a formal accident of the notation; it is the property that singles the composition out.

### The Square at One Setting

**Exactly one setting makes the square scalar for every element.** For every element,

$$
\boxed{\;\tilde Q^{\natural}\tilde Q=\langle\tilde Q\rangle_{\natural}e_t,
\qquad
\langle\tilde Q\rangle_{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2\;}.
$$

At the other three settings the square is not scalar in general: at $(\mathrm{id},\mathrm{id})$ the element $e_t+\vec e_x$ has the square $2\vec e_x$, at $(\mathrm{id},{}^{*})$ the element $e_t+i\vec e_x$ has the square $2e_t+2i\vec e_x$, and at $({}^{\natural},{}^{*})$ the element $e_t+\vec e_x$ has the square $-2\vec e_x$. This theorem is the algebraic root of the causal reading. The quaternionic bilinear product is the only one of the four whose square is central for every element, and the central value is the interval.

**The other square.** The Hermitian square $\tilde Q\tilde Q^{*}$ has the real scalar part $\sum_\mu\lvert Q_\mu\rvert^{2}$ and is positive semidefinite; the rank of its $2\times2$ matrix representation is two off the zero-divisor cone and at most one on it. This is the algebraic root of the probability reading. The two squares are not two computations of one object: one is central and signed, the other is positive and rank-bearing, and the two jobs are separated by that difference.

### The Twelve Products and the Two Halves of a Job

Each general product splits into a symmetric and an antisymmetric half, and the twelve products of the space are the four general products together with their eight halves. The symmetrisation keeps the scalar part, so the symmetric half carries the form; the antisymmetrisation kills it, so the antisymmetric half carries the order. Of the twelve, only two satisfy a classical identity: the symmetric plain bilinear product is a Jordan product, and the antisymmetric plain bilinear product is a Lie bracket.

Read physically, a job has a **magnitude** and an **order**. The magnitude is the symmetric half: it carries the pairing, the interval and the metric. The order is the antisymmetric half: it carries the bracket and the obstruction. The two halves are not two jobs, and no single product carries both a metric and a closed symmetry. This is the grid-level form of the corpus's rule that the coupling carries the metric and the order carries the obstruction.

## The Four Forms and the Four Jobs

The four forms are read on the material sector $\mathbb{M}_-$, the anti-Hermitian subspace, where the physical dictionary places the spacetime element $\tilde R=ict'\,e_t+x\vec e_x+y\vec e_y+z\vec e_z$. Their signatures there, and on the informational sector $\mathbb{M}_+$, are the algebra's own statement of which form is which; the last column is the reading that attaches a job to each.

| Product | Slots | Form | Signature on $\mathbb{M}_-$ | Signature on $\mathbb{M}_+$ | Job |
| --- | --- | --- | --- | --- | --- |
| $\tilde Q_1\tilde Q_2$ | $(\mathrm{id},\mathrm{id})$ | $\langle\cdot,\cdot\rangle$ | $(0,4)$ | $(4,0)$ | composition |
| $\tilde Q_1\tilde Q_2^{*}$ | $(\mathrm{id},{}^{*})$ | $\langle\cdot,\cdot\rangle_{*}$ | $(4,0)$ | $(4,0)$ | probability |
| $\tilde Q_1^{\natural}\tilde Q_2$ | $({}^{\natural},\mathrm{id})$ | $\langle\cdot,\cdot\rangle_{\natural}$ | $(3,1)$ | $(1,3)$ | causality |
| $\tilde Q_1^{\natural}\tilde Q_2^{*}$ | $({}^{\natural},{}^{*})$ | $\langle\cdot,\cdot\rangle_{\natural*}$ | $(1,3)$ | $(1,3)$ | gauge |

## Interpretations

### Composition

The plain product is the composition of two operations. Associativity is read as composability: the bracket of three factors may be moved without changing the result. The unit $e_t$ is the identity operation, and non-commutativity is the order of the two operations. The left multiplications $L_{\tilde Q_1}:\tilde Q_2\mapsto\tilde Q_1\tilde Q_2$ form a monoid under composition, with $L_{e_t}$ as identity; it is a monoid and not a group, because only the units are invertible. The process is the multiplication, and the state is the idempotent, not the element.

The invertible elements are the reversible operations. The zero-divisor cone is the wall of the reversible region, and the algebra is the disjoint union of the two. The criterion of invertibility is the multiplicative norm of the causal row, not the scalar form of this one: $e_t+\vec e_x$ is a unit with $\langle e_t+\vec e_x,e_t+\vec e_x\rangle=0$, and $e_t+i\vec e_x$ is a zero divisor with $\langle e_t+i\vec e_x,e_t+i\vec e_x\rangle=2$. The scalar form of composition decides no inverse.

The form of the composition is the **sector sign**, not the metric. It is negative definite on $\mathbb{M}_-$ and positive definite on $\mathbb{M}_+$; it says which half an element belongs to and measures neither. The metric of the material sector is the quaternionic form of the causal row, and the two must not be exchanged. The step from one to the other is the first slot's dial: it changes the product with the form, so the metric is not a second structure added to the composition but the same rule at the other setting.

Composition is associative, but the twisted products are not. A non-vanishing associator is the algebraic image of an irreducible term in three operations: a three-way interaction that cannot be assembled from two-body pieces. The reading pairs with the corpus's ternary-product articles, and its boundary is that what fails to associate is the twist, not the elements.

**The boundary.** The product is a composition of elements, not a dynamics. No equation of motion, no field and no quantisation is derived here. The reading does not say that every physical process is a multiplication, and it does not derive the Lorentz action or the measurement update from the plain product; those belong to their own articles.

### Probability

The plain sesquilinear product carries the **Born pairing**. Its form $\langle\cdot,\cdot\rangle_{*}$ is positive definite of signature $(8,0)$ on the real algebra, and it is the only one of the four that is definite on every subspace. Its square root is the unique topological norm of the space, $\lVert\tilde Q\rVert_E^{2}=\langle\tilde Q\rangle_{*}$. A probability can be built from this form and from no other of the four.

On the material sector the Born form is the negative of the sector sign, $\langle\cdot,\cdot\rangle_{*}=-\langle\cdot,\cdot\rangle$; on the informational sector the two coincide. The Born form is therefore blind to the sector: it measures a material and an informational element on the same scale.

The symmetric sesquilinear part lands in the centre, so it supplies a weight and no state. The pure states are the minimal Hermitian idempotents of the algebra, $\tfrac12(e_t+i\vec u)$ with $\vec u$ a real unit vector, and they are not the values of the product. The Born weight is the pairing of a state with an observable, not the product of two weights. The state carries the axis $\vec u$ and no phase; the phase belongs to the spinor, not to the form.

**The boundary.** The Born rule is not derived here. That the positive definite form of the sesqualgebra is the probability of a physical theory is the hypothesis of the informational sector, stated and bounded in its own article. The product supplies the pairing, the norm and the unitary group; it does not supply the state space, the measurement postulate or the identification of an element with a physical state.

### Causality

The quaternionic bilinear product is the causal product. Its square is the interval,

$$
\tilde Q^{\natural}\tilde Q=\langle\tilde Q\rangle_{\natural}e_t,
$$

and on the material sector the central value is the Minkowski interval,

$$
\langle\tilde R\rangle_{\natural}=-c^{2}{t'}^{2}+x^{2}+y^{2}+z^{2},
$$

of signature $(3,1)$. The zero set is the zero-divisor cone; its cut by $\mathbb{M}_-$ is the light cone; and the level set $\{\langle\tilde Q\rangle_{\natural}=-m^{2}c^{2}\}$ is the mass shell.

The form is **multiplicative**,

$$
\boxed{\;\langle\tilde Q_1^{\natural}\tilde Q_2\rangle_{\natural}
=
\langle\tilde Q_1\rangle_{\natural}\,\langle\tilde Q_2\rangle_{\natural}\;},
$$

so the causal type of a composite is the product of the causal types. The null set $\{\langle\tilde Q\rangle_{\natural}=0\}$ is closed under multiplication, and so are the units and the zero divisors; on the material sector this null set is the light cone. The product of two material elements is material exactly when they anticommute, so the light cone is not closed under composition within the sector; the closure is a statement about the algebra and not about the sector. For units, the logarithm $\log\lvert\langle\tilde Q\rangle_{\natural}\rvert$ is additive over the composition and is read as a dilation potential; the rapidity is the length of the pure part of the polar angle, not the potential.

The product is not associative, and the norm does not notice. The composite of three causal operations depends on the bracket, while its interval is the product of the three intervals whatever the bracket. That is the precise sense in which the causal **type** composes even though the causal **operation** does not associate. The reading is not a defect of the algebra; it separates the invariant, which is multiplicative, from the element, which is not.

On the informational sector the same form has signature $(1,3)$: one sign and three of the other, with the inertia reversed by the sector. The interval and the informational metric are one form, and the sign of the inertia is what the sector decides.

**The boundary.** The metric is $\langle\cdot,\cdot\rangle_{\natural}$, not $\langle\cdot,\cdot\rangle$; the causal structure lives on $\mathbb{M}_-$, not on the whole algebra. On the whole algebra the zero set is the zero-divisor cone, which is larger than the light cone, and the form is complex on the centre and the vector subspace. The reading does not derive a propagation equation, a speed or a mass spectrum; it identifies the level sets that such an equation would use.

### Gauge

The quaternionic sesquilinear product carries the **Krein form**. Its form is Hermitian, real at the two equal arguments, and indefinite: of signature $(2,6)$ on the real algebra, and of signature $(1,3)$ on each of the four four-dimensional real-type subspaces. It normalises nothing, because an indefinite form has no positive unit sphere.

On the material sector the Krein form is minus the interval, $\langle\cdot,\cdot\rangle_{\natural*}=-\langle\cdot,\cdot\rangle_{\natural}$; on the informational sector the two coincide, $\langle\cdot,\cdot\rangle_{\natural*}=\langle\cdot,\cdot\rangle_{\natural}$. The interval and the gauge form are therefore one form read with a sign, and on the informational sector they are the same form. This is the algebraic reason the two readings are easy to conflate, and the reason the sign of the sector must be named whenever the two are compared.

The indefinite form is read as a **constraint** and not as a state. A gauge calibration fixes a redundancy; it does not prepare a state, and its form cannot supply a probability. The signature is what an object is: a definite Hermitian form counts states, an indefinite one counts a constraint.

The antisymmetric half of the gauge product is the gauge bracket, the conjugate cross product. It fails the Jacobi identity, and the failure needs a complex witness: on the real forms the bracket coincides with the antisymmetric plain bilinear product, which is a Lie bracket, so no real form can diagnose the failure. The complex structure is the carrier of the obstruction, not a convenience. The failure is structural — the low operation of a higher structure — and the strict group that remains is $\mathrm{U}(2)$. The gauge bracket is valued in the vector subspace: a pure vector, an axial direction read as a polarisation direction, with no central component and no state. The discrete charge is the label of the compact part, and it is discrete because that part is compact.

**The boundary.** The Krein form is a form, not a gauge theory. No gauge group, no coupling constant and no field content is derived here; the indefinite structure — the Krein space, its fundamental symmetry and its signatures — is the subject of the entry *The Krein Form and the Indefinite Structure*. The gauge bracket does not close and supplies no internal symmetry algebra; the closure that exists is the cross-product closure of the real quaternion forms, and the failure of the gauge bracket is invisible to a computation with real coefficients. The ceiling of the internal group is its own question, and the biquaternion algebra reaches $\mathrm{SU}(2)$ and not $\mathrm{SU}(3)$.

### The $4\times3$ Table as a Mnemonic

The four products and the three involutions can be read as a $4\times3$ table of questions. The four rows are the jobs; the three columns are the product read as it stands, read through the natural conjugation, and read through the star.

| product | as it stands | through ${}^{\natural}$ | through ${}^{*}$ |
| --- | --- | --- | --- |
| composition | composition | commutation | rotation |
| causality | causality | coupling | obstruction |
| probability | decision | weight | phase |
| gauge | gauge | measurement | polarisation |

The table is a mnemonic. The row words are the four jobs; the column words are the question each involution puts to the product. Read across a row, the three words are the operation, the quantity and the order or phase of one job: composition, commutation and rotation are the operation, the reversed order and the bracket; causality, coupling and obstruction are the interval, its scalar pairing and its cone; decision, weight and phase are the outcome, the expectation and the interference; gauge, measurement and polarisation are the constraint, the calibration and the axial direction.

The natural conjugation reverses the order of a product, and the star is the Hermitian adjoint; those are the threads of the two outer columns. The assignment is a mnemonic and not a derivation: the four products and the three involutions are algebraic, and the twelve words are the framework's names for the questions they can be asked.

The table does not add a product, a theorem or a completeness claim. It is the four-by-three shape of the twelve questions, and it is offered as a mnemonic because the names are easier to remember in the table than in the list. The algebra's own caution stands: no single product carries both a metric and a closed symmetry, and the twelve are four jobs with two halves, not twelve equivalent structures.

**The boundary.** The assignment of the twelve words to the twelve cells is a reading, not a derivation. The table does not assert that the twelve questions are independent or exhaustive, and it does not replace the property table or the classification of the twelve structures.

## The Two Slots Behind the Names

The four names are not attached to four unrelated structures. They are attached to the four cells of one grid, and each cell is a pair of answers to two questions.

| Question | Slot | Rule |
| --- | --- | --- |
| Can the operation be iterated? | the second | $\mathbb{C}$-bilinear in the second argument if and only if $K_2=\mathrm{id}$; left unit and monoid then follow |
| Is the square of an element central? | neither | only at $({}^{\natural},\mathrm{id})$ |
| Is the product associative? | both | only at $(\mathrm{id},\mathrm{id})$, in $\mathbb{B}$ |
| Does the form measure or carry a metric? | the first | definite on each sector if and only if $K_1=\mathrm{id}$; the right unit has the same rule |
| Which unit does the product have? | both | left unit from the second slot, right unit from the first |

**The second slot separates a dynamics from a pairing.** Read without the star, the form is bilinear and symmetric, and the operation can be iterated; read with the star, it is sesquilinear and conjugate-symmetric, and the operation can only be evaluated. Composition and causality are on the first side; probability and gauge on the second. This is the algebra's own distinction between an operation and a measurement, and it is prior to the physical naming.

**The first slot separates a measure from a metric.** Read as it stands, the form is definite on each sector and carries no cone; read through ${}^{\natural}$, it is indefinite on each sector and carries a cone. The dial is a reflection: it negates the three vector coordinates and fixes the scalar direction. It is an involutive anti-automorphism of the algebra. It is not the central Wick rotation, which is an automorphism of order four and exchanges the two sectors; the dial is an involution, the rotation is a quarter turn, and only the dial is a slot of a product.

**The sector sign is visible in the bilinear layer and invisible in the sesquilinear one.** On $\mathbb{M}_-$ one has $\langle\cdot,\cdot\rangle_{*}=-\langle\cdot,\cdot\rangle$, and on $\mathbb{M}_+$ the two forms coincide. The bilinear form is negative definite on the material sector and the sesquilinear form positive definite there; the difference of sign is exactly the sector. The corpus's rule that the material sector is visible in the bilinear layer and invisible in the sesquilinear one is this identity, and it is why the naming must say which form it means.

**The four readings are one group.** The two insertions are commuting involutions, so the four settings are the four elements of $\mathbb{Z}_2\times\mathbb{Z}_2$. The grid is not a list of four constructions but one construction with two dials. The four products are the four elements of the group read on one rule, and the four jobs are the four readings of that group.

**The collapse on the real part, and the ten-to-twelve distinction.** For real elements the coefficientwise conjugation is the identity, so $\langle\cdot,\cdot\rangle_{\natural*}=\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{*}=\langle\cdot,\cdot\rangle_{\natural}$: the four forms become two. On the realification the twelve products become ten, the pairs $\mathrm{SPS}=\mathrm{SQA}$ and $\mathrm{APA}=\mathrm{AQS}$ having collapsed, and the complex witness of the Jacobi failure of $\mathrm{AQS}$ disappears. The count of twelve is the count over $\mathbb{C}$. A real implementation must use the complex space, or must remember which of its ten operations stands for two. The difference of count is the algebraic size of the complex structure the grid carries, and it is a count of operations, not a measure of a physical complexification.

## Limits

The naming is a reading of a proved algebra. The algebra proves the four settings, the property table, the two slots, the scalar square and the two squares; it does not prove that the four jobs are these four, and it does not prove that no other assignment of the four is possible. The claim is that the four jobs are independent and that the four forms supply one candidate for each; it is offered as a claim about the framework, not as a consequence of the algebra.

The four jobs are form-level statements and are read on the sectors. For a general element the four forms are four and do not agree; an identity on a real-type subspace does not make two products equal. In particular, $\langle\cdot,\cdot\rangle_{\natural*}=\langle\cdot,\cdot\rangle_{\natural}$ on $\mathbb{M}_+$ does not make the quaternionic sesquilinear product a bilinear one there, and $\langle\cdot,\cdot\rangle_{*}=-\langle\cdot,\cdot\rangle$ on $\mathbb{M}_-$ does not make the plain product a pairing.

No product is derived from its job. The products are the algebra's; the jobs are the readings. The article does not derive a dynamics, a state space, a mass spectrum, a gauge group or a measurement postulate. Those are the subjects of the articles named at the end, and each of them states its own hypothesis and its own boundary.

The physical identification of the material sector with spacetime and of the informational sector with the state side is the dictionary of the corpus. It is a convention with a hypothesis, not a theorem of the algebra; the sector structure is proved, the physical naming of the sectors is not.

## Summary

- The algebra carries four general products, and they are the four settings of one rule: the plain product with a conjugation inserted in the first slot, the second, both or neither.
- The settings form a group $\mathbb{Z}_2\times\mathbb{Z}_2$; the four products are its four settings, and the four jobs are its four readings.
- Only the plain bilinear product is associative and two-sidedly unital; only it is the multiplication of an associative algebra over $\mathbb{C}$.
- The quaternionic bilinear product is the only one whose square is central for every element, and the central value is the interval.
- The Hermitian square is positive semidefinite, and the rank of its $2\times2$ matrix representation is two off the cone and at most one on it; this is the algebraic root of the probability reading.
- The second slot separates a dynamics from a pairing; the first slot separates a measure from a metric.
- Composition is the plain product, with the sector sign as its form; the metric is the quaternionic form, not the sector sign.
- Probability is the plain sesquilinear product, with the positive definite Born form; it is the only form definite on every subspace.
- Causality is the quaternionic bilinear product; its square is the interval, its zero set the light cone on the sector, its level sets the mass shells, and its norm is multiplicative.
- Gauge is the quaternionic sesquilinear product, with the indefinite Krein form; it is minus the interval on the material sector and the interval itself on the informational one.
- The four products and the three involutions form a $4\times3$ table of twelve questions, offered as a mnemonic and not as a completeness claim.
- On the real part the four forms collapse to two and the twelve products to ten; the count of twelve is a count over $\mathbb{C}$.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde Q_1\star_{K_1K_2}\tilde Q_2=K_1(\tilde Q_1)K_2(\tilde Q_2)$ | the one rule; $K_1\in\{\mathrm{id},{}^{\natural}\}$ and $K_2\in\{\mathrm{id},{}^{*}\}$ are the two slots |
| $\tilde Q_1\tilde Q_2$ | the general plain bilinear product, composition |
| $\tilde Q_1\tilde Q_2^{*}$ | the general plain sesquilinear product, probability |
| $\tilde Q_1^{\natural}\tilde Q_2$ | the general quaternionic bilinear product, causality |
| $\tilde Q_1^{\natural}\tilde Q_2^{*}$ | the general quaternionic sesquilinear product, gauge |
| $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{*}$, $\langle\cdot,\cdot\rangle_{\natural}$, $\langle\cdot,\cdot\rangle_{\natural*}$ | the sector sign, the Born form, the interval and the Krein form |
| $\langle\tilde Q\rangle_{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2$ | the quaternionic algebraic norm, the interval on $\mathbb{M}_-$ |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | the anti-Hermitian (material) and Hermitian (informational) sectors |
| $\tilde R=ict'\,e_t+x\vec e_x+y\vec e_y+z\vec e_z$ | the material coordinate |
| $\mathrm{SPS}$, $\mathrm{SQA}$, $\mathrm{APA}$, $\mathrm{AQS}$ | the symmetric plain sesquilinear, symmetric quaternionic bilinear, antisymmetric plain bilinear and antisymmetric quaternionic sesquilinear products |

## Further Reading

- [The Four General Products and Their Relations](../articles_maths/the-four-general-products-and-their-relations.html), for the four definitions and their scalar–vector forms.
- [The Four General Products and Their Relations](../articles_maths/the-four-general-products-and-their-relations.html), for the property table, the two slots, the units, the scalar square and the failure of associativity.
- [Symmetric and Antisymmetric Decomposition of the Four General Products](../articles_maths/symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html), for the symmetric and antisymmetric halves and the Jordan and Lie structures.
- [The Four Forms and the Four Algebraic Norms](../articles_maths/the-four-forms-and-the-four-algebraic-norms.html) and [Remarkable Subspaces and the Four Forms](../articles_maths/remarkable-subspaces-and-the-four-forms.html), for the four forms and their restrictions.
- [The Four Forms and the Four Algebraic Norms](../articles_maths/the-four-forms-and-the-four-algebraic-norms.html) and [Norm and Invertibility in the Biquaternion Algebra](../articles_maths/norm-and-invertibility-in-the-biquaternion-algebra.html), for multiplicativity, definiteness, invertibility and the zero-divisor cone.
- [The Realification and the Effect of the Change of Scalars](../articles_maths/the-realification-and-the-effect-of-the-change-of-scalars.html), for the ten-to-twelve distinction.
- [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html) and [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html), for the two sectors and the two jobs that live there.
- [The Krein Form and the Indefinite Structure](the-krein-form-and-the-indefinite-structure.html), for the corresponding entry of this category.
