# __The Four Products: Composition, Probability, Causality and Gauge__

## Introduction

**This entry reads the sixth section of the mathematical category: the four ways two elements combine, the twelve operations they generate, and the four names the physics puts on them.**

**The question is what a pair of elements can do.** A single element has a spectrum and a module acts on it; a *pair* has a product, and the algebra carries four of them, not one. Each sends a pair $(\tilde Q_1,\tilde Q_2)$ to an element of $\mathbb{B}$, each is written on the same eight real coordinates, and the four differ in one point alone: whether the first argument, the second, both or neither is read through a conjugation before the multiplication.

**The answer is one rule with two dials.**

$$
\boxed{\;\tilde Q_1\star_{K_1K_2}\tilde Q_2=K_1(\tilde Q_1)\,K_2(\tilde Q_2),\qquad K_1\in\{\mathrm{id},{}^{\natural}\},\qquad K_2\in\{\mathrm{id},{}^{*}\}\;}
$$

**The two dials are independent and each is an involution,** so the four settings are the four elements of $\mathbb{Z}_2\times\mathbb{Z}_2$. There is no fifth product, and none of the four is a variant of another: they are four different questions asked of one multiplication.

**Each product then splits in two.** The symmetric half keeps the scalar part and loses the direction; the antisymmetric half keeps the direction and loses the scalar part. Four products with two halves each give twelve operations in all, the four parents and their eight halves, and the twelve are pairwise distinct over $\mathbb{C}$.

**The single idea is that the algebra supplies the products and the corpus supplies the names.** The algebra proves that the four settings exist, that only one of them is associative, that only one has a central square, and that only two of the twelve satisfy a classical identity. It does not prove that a physical theory needs exactly these four jobs. The reading below is offered with that boundary stated each time.

## The Source Table

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| the four products, their coordinate formulas, their scalar–vector forms, the two slots, the property table, the identities and the left multiplications, the hyperbolic basis of the plain product | [The Four General Products and Their Relations over the Biquaternion Algebra](../articles_maths/the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html) |
| the symmetric and antisymmetric decomposition, the twelve products one by one, the table of the twelve, the distinction over $\mathbb{C}$ and the coincidence over $\mathbb{R}$, the counts of the failures | [Symmetric and Antisymmetric Decomposition of the Four General Products](../articles_maths/symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html) |
| the vector part of each product, the table of the twelve vector parts, the nine distinct classes, the diagonals, the component forms | [The Vector Parts of the Products over the Biquaternion Algebra](../articles_maths/the-vector-parts-of-the-products-over-the-biquaternion-algebra.html) |
| the four forms, their Gram matrices, their inertias, their null sets, the four algebraic norms, multiplicativity and definiteness | [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](../articles_maths/the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html) |
| the restrictions of the products and the forms to the six remarkable subspaces, the null sets, the isometry groups, the material interpretation | [Remarkable Subspaces and the Four General Products, Forms and Norms](../articles_maths/remarkable-subspaces-and-the-four-general-products-forms-and-norms.html) |

**The rows are the entry's order.** The four products and their properties; then the split into twelve; then the vector parts, which are what a metric can see; then the forms, which are the scalar parts and the reason the four names exist.

## The Results in Brief

### The One Rule and the Two Dials

**Each slot carries one insertion, and the two insertions commute.** The quaternion conjugation ${}^{\natural}$ fixes the central $i$, negates the three vector units and is a $\mathbb{C}$-linear anti-automorphism; the Hermitian conjugation ${}^{*}=\bar{\cdot}\circ{}^{\natural}$ is the coefficientwise conjugate composed with it, and is conjugate-linear. Each is its own inverse.

**The second dial decides whether the operation can be iterated.**

$$
K_2=\mathrm{id}\iff\text{the product is }\mathbb{C}\text{-bilinear in its second argument}\iff\text{a left unit and a monoid of left multiplications exist}.
$$

**The first dial decides whether the form measures or carries a cone.** With $K_1=\mathrm{id}$ the scalar part is definite on each of the two sectors; with $K_1={}^{\natural}$ it is indefinite on each, and the bilinear one has the zero-divisor cone as its null set.

**The grid is closed.** There is no third insertion: an anti-automorphism of $\mathbb{B}$ that fixes $e_t$ and is $\mathbb{C}$-linear is the identity or the quaternion conjugation, and the two sesquilinear settings are its compositions with the star.

### The Four Products

| product | name | scalar part | vector part |
| --- | --- | --- | --- |
| $\tilde Q_1\tilde Q_2$ | plain bilinear | $Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2)$ | $Q_{1t}\vec Q_2+Q_{2t}\vec Q_1+\vec Q_1\times\vec Q_2$ |
| $\tilde Q_1^{\natural}\tilde Q_2$ | quaternionic bilinear | $Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2)$ | $Q_{1t}\vec Q_2-Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2$ |
| $\tilde Q_1\tilde Q_2^{*}$ | plain sesquilinear | $Q_{1t}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2})$ | $-Q_{1t}\overline{\vec Q_2}+\overline{Q_{2t}}\vec Q_1-\vec Q_1\times\overline{\vec Q_2}$ |
| $\tilde Q_1^{\natural}\tilde Q_2^{*}$ | quaternionic sesquilinear | $Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})$ | $-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1+\vec Q_1\times\overline{\vec Q_2}$ |

**Every one of the four is two mixed terms and a cross term.** The mixed terms carry the scalar parts of the two factors against the vector part of the other; the cross term is the bilinear cross product, with a sign that the first dial fixes and a conjugation that the second fixes.

**The four scalar parts are the four forms.** They are written on the coordinates in the four possible ways,

$$
\sum_\mu\varepsilon_\mu Q_{1\mu}Q_{2\mu},\qquad
\sum_\mu Q_{1\mu}Q_{2\mu},\qquad
\sum_\mu Q_{1\mu}\overline{Q_{2\mu}},\qquad
\sum_\mu\varepsilon_\mu Q_{1\mu}\overline{Q_{2\mu}},
$$

with $\varepsilon=(1,-1,-1,-1)$, and they are what the next entry of the category treats as the four forms and the four norms.

### The Property Table

| property | $\tilde Q_1\tilde Q_2$ | $\tilde Q_1^{\natural}\tilde Q_2$ | $\tilde Q_1\tilde Q_2^{*}$ | $\tilde Q_1^{\natural}\tilde Q_2^{*}$ |
| --- | --- | --- | --- | --- |
| $\mathbb{C}$-linear in the first argument | yes | yes | yes | yes |
| $\mathbb{C}$-linear in the second argument | yes | yes | no | no |
| associative | yes | no | no | no |
| unit on the left | yes | yes | no | no |
| unit on the right | yes | no | yes | no |
| left multiplications form a monoid | yes | yes | no | no |
| multiplication of an algebra over $\mathbb{C}$ | yes | yes | no | no |
| multiplication of a sesqualgebra over $\mathbb{C}$ | no | no | yes | yes |

**Only the plain product is a multiplication in the strict sense.** It is associative, two-sidedly unital and $\mathbb{C}$-bilinear, and it makes $\mathbb{B}$ an associative algebra over $\mathbb{C}$. The quaternionic product keeps bilinearity and the left unit but loses associativity; the two sesquilinear products keep the right unit and lose bilinearity.

**The associativity row is the one row that the two dials decide jointly.** It holds exactly when both slots are trivial, and the reason is the same in all three failures: the plain product lets the parentheses be dropped, and the twisted operation then conjugates a factor and transposes two of them.

### The Two Squares

**Exactly one setting makes the square of every element central.**

$$
\boxed{\;\tilde Q^{\natural}\tilde Q=\langle\tilde Q\rangle_{\natural}e_t,\qquad \langle\tilde Q\rangle_{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2\;}
$$

**The other three settings do not.** At the plain setting $e_t+\vec e_x$ squares to $2\vec e_x$; at the plain sesquilinear setting $e_t+i\vec e_x$ squares to $2e_t+2i\vec e_x$; at the quaternionic sesquilinear setting $e_t+\vec e_x$ squares to $-2\vec e_x$. In each case the square has a vector part and the scalar part is not the invariant.

**The second square is Hermitian and positive semidefinite.**

$$
\tilde Q\tilde Q^{*}=\Bigl(\sum_\mu\lvert Q_\mu\rvert^{2}\Bigr)e_t+\text{a Hermitian vector part},
$$

of trace $2\sum_\mu\lvert Q_\mu\rvert^{2}$ in the matrix model, of rank two off the zero-divisor cone and of rank at most one on it.

**The two squares are not two computations of one object.** One is central and signed, with values in $\mathbb{C}$ and a null set that is a cone; the other is Hermitian and positive, with values in the centre of the Hermitian sector and a null set that is the origin alone. Everything that follows about causality and probability is a consequence of that difference.

### The Twelve and the Two Halves

**Each product splits into a symmetric and an antisymmetric half, and the exchange that defines the split depends on the family.**

$$
f^{\mathrm{s}}(\tilde Q_1,\tilde Q_2)=\tfrac12\bigl(f(\tilde Q_1,\tilde Q_2)+f(\tilde Q_2,\tilde Q_1)\bigr),\qquad
f^{\mathrm{a}}(\tilde Q_1,\tilde Q_2)=\tfrac12\bigl(f(\tilde Q_1,\tilde Q_2)-f(\tilde Q_2,\tilde Q_1)\bigr)
$$

for the two bilinear families, and

$$
f^{\mathrm{s}}(\tilde Q_1,\tilde Q_2)=\tfrac12\bigl(f(\tilde Q_1,\tilde Q_2)+\overline{f(\tilde Q_2,\tilde Q_1)}\bigr),\qquad
f^{\mathrm{a}}(\tilde Q_1,\tilde Q_2)=\tfrac12\bigl(f(\tilde Q_1,\tilde Q_2)-\overline{f(\tilde Q_2,\tilde Q_1)}\bigr)
$$

for the two sesquilinear ones. **The bare interchange is not the exchange:** in the sesquilinear case the interchange alone returns a product of the other class, and it is the conjugation of the value that repairs it.

**The twelve operations, with the part of the value that each keeps.**

| operation | scalar part | vector part | law |
| --- | --- | --- | --- |
| $\tilde Q_1\tilde Q_2$ | $Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2)$ | $Q_{1t}\vec Q_2+Q_{2t}\vec Q_1+\vec Q_1\times\vec Q_2$ | associative |
| $\tilde Q_1^{\natural}\tilde Q_2$ | $Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2)$ | $Q_{1t}\vec Q_2-Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2$ | not associative |
| $\tilde Q_1\tilde Q_2^{*}$ | $Q_{1t}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2})$ | $-Q_{1t}\overline{\vec Q_2}+\overline{Q_{2t}}\vec Q_1-\vec Q_1\times\overline{\vec Q_2}$ | not associative |
| $\tilde Q_1^{\natural}\tilde Q_2^{*}$ | $Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})$ | $-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1+\vec Q_1\times\overline{\vec Q_2}$ | not associative |
| $\tilde Q_1\bullet\tilde Q_2$ | $Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2)$ | $Q_{1t}\vec Q_2+Q_{2t}\vec Q_1$ | **Jordan** |
| $\tilde Q_1\bullet_{\natural}\tilde Q_2$ | $Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2)$ | $0$ | fails Jordan |
| $\tilde Q_1\bullet_{*}\tilde Q_2$ | $Q_{1t}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2})$ | $0$ | fails Jordan |
| $\tilde Q_1\bullet_{\natural*}\tilde Q_2$ | $Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})$ | $-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1$ | fails Jordan |
| $\tilde Q_1\wedge\tilde Q_2$ | $0$ | $\vec Q_1\times\vec Q_2$ | **Lie** |
| $\tilde Q_1\wedge_{\natural}\tilde Q_2$ | $0$ | $Q_{1t}\vec Q_2-Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2$ | fails Jacobi |
| $\tilde Q_1\wedge_{*}\tilde Q_2$ | $0$ | $-Q_{1t}\overline{\vec Q_2}+\overline{Q_{2t}}\vec Q_1-\vec Q_1\times\overline{\vec Q_2}$ | fails Jacobi |
| $\tilde Q_1\wedge_{\natural*}\tilde Q_2$ | $0$ | $\vec Q_1\times\overline{\vec Q_2}$ | fails Jacobi |

**Two facts are visible in the table without a computation.** The four parents and the four symmetric parts have the same scalar part, because the symmetrisation fixes the scalar part; the four antisymmetric parts have zero scalar part, because the antisymmetrisation kills it. And the two central symmetrisations, $\tilde Q_1\bullet_{\natural}\tilde Q_2$ and $\tilde Q_1\bullet_{*}\tilde Q_2$, have no vector part at all: their image is the centre.

**The two central ones are scalar by construction.**

$$
\tilde Q_1\bullet_{\natural}\tilde Q_2=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t,\qquad
\tilde Q_1\bullet_{*}\tilde Q_2=\langle\tilde Q_1,\tilde Q_2\rangle_{*}e_t .
$$

**Only two of the twelve satisfy a classical identity.** $\tilde Q_1\bullet\tilde Q_2$ is a Jordan product and $\tilde Q_1\wedge\tilde Q_2$ is a Lie bracket, and the reason is one fact about the parents: the symmetrisation of an associative product is a Jordan product, and its antisymmetrisation is a Lie bracket, and the plain product is the only associative parent.

### The Vector Parts and the Nine Classes

**The vector part of a product is what a metric can see, and the twelve products carry nine distinct vector parts.**

$$
V(\tilde Q_1^{\natural}\tilde Q_2)=V(\tilde Q_1\wedge_{\natural}\tilde Q_2),\qquad
V(\tilde Q_1\tilde Q_2^{*})=V(\tilde Q_1\wedge_{*}\tilde Q_2),\qquad
V(\tilde Q_1\bullet_{\natural}\tilde Q_2)=V(\tilde Q_1\bullet_{*}\tilde Q_2)=0,
$$

and these three coincidences are the only ones on the complex space.

**The first two are a consequence of the third.** The symmetric half of each of the two quaternionic families is central, so the antisymmetric half of the same family has the vector part of the parent. A reader who knows only the vector parts therefore cannot tell the parent from its antisymmetric half in those two families.

### The Forms of the Four

**The scalar part of a product is a form on the pair, and the four forms have four different inertias on the two sectors.**

| product | form | inertia on $\mathbb{B}_{\Phi}$ | inertia on $\\mathbb{B}_{\\Psi}$ |
| --- | --- | --- | --- |
| $\tilde Q_1\tilde Q_2$ | $\langle\cdot,\cdot\rangle$ | $(0,4)$ | $(4,0)$ |
| $\tilde Q_1^{\natural}\tilde Q_2$ | $\langle\cdot,\cdot\rangle_{\natural}$ | $(3,1)$ | $(1,3)$ |
| $\tilde Q_1\tilde Q_2^{*}$ | $\langle\cdot,\cdot\rangle_{*}$ | $(4,0)$ | $(4,0)$ |
| $\tilde Q_1^{\natural}\tilde Q_2^{*}$ | $\langle\cdot,\cdot\rangle_{\natural*}$ | $(1,3)$ | $(1,3)$ |

**Two are definite on each sector and two are indefinite on each,** and that is the first dial read at the level of inertias. **One is definite on every subspace and one has inertia $(8,0)$ on the whole space,** and that is the plain sesquilinear form, whose square root is the topological norm.

### The Degeneracy of the Twelve on the Real Part

**The twelve are pairwise distinct over $\mathbb{C}$ and ten over $\mathbb{R}$.**

$$
\tilde Q_1\wedge\tilde Q_2=\tilde Q_1\wedge_{\natural*}\tilde Q_2\quad(\tilde Q_1,\tilde Q_2\ \text{real}),
\qquad
\tilde Q_1\bullet_{\natural}\tilde Q_2=\tilde Q_1\bullet_{*}\tilde Q_2\quad(\tilde Q_1,\tilde Q_2\ \text{real}).
$$

**The fall from twelve to ten is a loss of distinctions, and it is exact.** For real elements the coefficientwise conjugation is the identity, the first dial changes nothing in the sesquilinear families, and two pairs of operations that are different on the complex space become one.

**The consequence is a caution about computations.** A computation restricted to real elements cannot separate the members of either coincident pair, and a property that holds for one member and fails for the other is invisible there. A reader who checks an associativity, a Jacobi identity or a Jordan identity on real elements only therefore risks reporting an obstruction as absent, or a structure as present, when the distinction between the two members has simply been erased by the reality condition.

### The Counts of the Failures

**The failures are far from equally dense, and their counts on the eight-element basis give their shape.**

| identity | the part that holds it | the parts that fail it |
| --- | --- | --- |
| Jacobi, over the four antisymmetric parts | $\tilde Q_1\wedge\tilde Q_2$ | $\tilde Q_1\wedge_{*}\tilde Q_2$ on $252$ of the $512$ triples; $\tilde Q_1\wedge_{\natural}\tilde Q_2$ on $144$; $\tilde Q_1\wedge_{\natural*}\tilde Q_2$ on $72$ |
| Jordan, over the four symmetric parts | $\tilde Q_1\bullet\tilde Q_2$ | $\tilde Q_1\bullet_{*}\tilde Q_2$ at $7$ of the $8$ basis elements; $\tilde Q_1\bullet_{\natural}\tilde Q_2$ at $6$; $\tilde Q_1\bullet_{\natural*}\tilde Q_2$ at $4$ |

**The sparsest Jacobi failure is the one whose witness needs a complex element.** $\tilde Q_1\wedge_{\natural*}\tilde Q_2$ fails on the triple $(\vec e_x,\vec e_x,i\vec e_y)$, and the cyclic sum is a nonzero multiple of $i\vec e_y$; on real elements that bracket is the Lie bracket, so no real triple can witness the failure. **The densest is the plain sesquilinear bracket, which fails on half the triples.**

**On the Jordan side the two sesquilinear symmetrisations are the denser and they fail at almost every element.** The witnesses have two shapes: a central shift, in $\tilde Q_1\bullet_{\natural*}\tilde Q_2$, whose sides differ by a multiple of $e_t$, and an outright vanishing, in $\tilde Q_1\bullet_{\natural}\tilde Q_2$ and $\tilde Q_1\bullet_{*}\tilde Q_2$, where a side is zero and the other is not. A shift needs a product whose square is not central, and that is the mark of the sesquilinear families; the vanishing needs a product whose square is central, and that is the mark of the quaternionic bilinear one.

## The Interpretations

### I.6.a — Four Products and Not One, Because There Are Two Dials

**Read:** the four products are the four settings of one rule, and the settings are the four elements of $\mathbb{Z}_2\times\mathbb{Z}_2$.

**The physical reading is a claim about what a theory must be able to ask of a pair.** Two questions are independent. *Is this a quantity or an operation?* is the second dial: a bilinear product can be iterated, a sesquilinear one can only be evaluated. *Does this measure, or does it carry a cone?* is the first dial: a definite form counts, an indefinite one constrains.

**Two independent binary questions give four products, and there is no fifth.** The closure is algebraic and not a matter of taste: an anti-automorphism of the algebra that fixes the unit and is complex-linear is the identity or the quaternion conjugation, and nothing else exists.

**The boundary.** The algebra proves the four settings and their independence as settings. It does not prove that a physical theory needs exactly four products. The claim of the corpus is narrower: each of the four jobs below is served by one setting, and no setting serves two.

### I.6.b — Composition: Associativity Is Composability

**Read:** the plain product makes $\mathbb{B}$ an associative algebra over $\mathbb{C}$, with $e_t$ as a two-sided unit.

**The reading is the oldest one in the corpus and the least controversial.** An element is an operation, the product of two operations is their composition, associativity says that a chain of three operations does not need brackets, and $e_t$ is the identity operation. Non-commutativity is the order of the two operations; the left multiplications form a monoid under composition.

**The invertible elements are the reversible operations, and the zero-divisor cone is the wall of the reversible region.**

$$
\mathbb{B}=\mathbb{B}^{\times}\sqcup\mathcal{N},\qquad
\tilde Q\in\mathbb{B}^{\times}\iff\langle\tilde Q\rangle_{\natural}\neq0 .
$$

**The wall is not empty and it is not thin in the physical sense.** $e_t+i\vec e_x$ is a zero divisor of norm zero, and the plane wave of a null field sits on that cone; $e_t+\vec e_x$ is invertible whose plain form is zero, so the composition's own quadratic form does not decide invertibility. The criterion is the norm of the causal product, not the form of this one, and the two must not be exchanged.

**The boundary.** The product is a composition of elements, not a dynamics. No equation of motion, no field and no quantisation is derived here.

### I.6.c — The Plain Form Is a Sector Sign, Not a Metric

**Read:** the plain form is negative definite on the material sector and positive definite on the informational one.

$$
\langle\tilde Q,\tilde Q\rangle<0\ \ (\tilde Q\in\mathbb{B}_{\Phi},\ \tilde Q\neq0),\qquad
\langle\tilde Q,\tilde Q\rangle>0\ \ (\tilde Q\in\mathbb{B}_{\Psi},\ \tilde Q\neq0).
$$

**So the form of the composition says which half an element belongs to and measures neither half.** The metric of the material sector is the quaternionic form, of inertia $(3,1)$; the plain form is its negative on the same sector, of inertia $(0,4)$.

**The physical reading is a warning about an easy mistake.** A reader who takes the form of the product as the metric of spacetime gets a Euclidean four-space with no cone, and then has to import the cone from somewhere else. The algebra supplies both forms at the two settings of the first dial, and the step between them is that dial: a reflection that negates the three vector coordinates and fixes the scalar direction.

**The boundary.** The sector sign is a statement about the two sectors, and on a general complex element the plain form is a complex number with no sign at all.

### I.6.d — Probability: the Only Definite Form, and a Square That Carries Rank

**Read:** the plain sesquilinear product has the Hermitian form as its scalar part, and that form is positive definite of inertia $(8,0)$ on the real algebra, and definite on every subspace.

**Its square is the rank-bearing Hermitian element.**

$$
\tilde Q\tilde Q^{*}=\sum_\mu\lvert Q_\mu\rvert^{2}e_t+\text{Hermitian vector part},\qquad
\operatorname{rank}\mathsf M_2(\tilde Q\tilde Q^{*})=2\ \text{off the cone},\ \le1\ \text{on it}.
$$

**The reading is that this is the product whose value can be a state.** A positive element of rank one is a pure state up to scale; a positive element of rank two is mixed; and the rank itself is the algebraic image of the distinction, which is why the cone is a boundary of the probability reading and not only of the causal one.

**The form is blind to the sector.** On the material sector $\langle\cdot,\cdot\rangle_{*}=-\langle\cdot,\cdot\rangle$, and on the informational sector the two coincide; the Hermitian form therefore measures a material and an informational element on one scale, while the plain form changes sign between them.

**The boundary.** The Born rule is not derived here. That the positive definite form of the sesqualgebra is the probability of a theory is the hypothesis of the informational sector. The product supplies the pairing, the norm and the $*$-unitary group; it does not supply the state space or the measurement postulate.

### I.6.e — The Probability Product Has No Clock

**Read:** in the plain sesquilinear product the central element squares to $+e_t$, not to $-e_t$.

$$
(ie_t)(ie_t)^{*}=ie_t\,\overline{ie_t}=i(-i)e_t=e_t .
$$

**The element that generates the phase in the composition product squares to $+e_t$ here.** It is a $*$-unitary and not a root of $-e_t$, and the central phase $e^{i\theta}e_t$ is likewise a $*$-unitary whose logarithm is a coefficient and not an element with a negative square.

**There is no clock element, and there is no nilpotent of index two.**

$$
\{\tilde Z:\tilde Z\tilde Z^{*}=-e_t\}=\varnothing,\qquad
\{\tilde Z:\tilde Z\tilde Z^{*}=0\}=\{0\}.
$$

**The cone appears one power further out.** For the sesquilinear product the left-nested powers are $\tilde Q^{\star k}=\tilde Q(\tilde Q^{*})^{k-1}$, and the nilpotents are the elements of index three: $\tilde\Upsilon^{\star3}=0$ exactly when $\tilde\Upsilon$ is pure with isotropic vector part, which is the parent's nilpotent cone. The nilpotent squares to nothing in the parent and squares to a **pure state** here:

$$
\tilde\Upsilon=\vec e_x+i\vec e_y,\qquad
\tilde\Upsilon\tilde\Upsilon^{*}=2e_t+2i\vec e_z\ \ (\text{rank one, positive}).
$$

**The physical reading is a division of labour between two products.** The composition product owns the phase, the frequency and the differential calculus; the probability product owns the weight, the state and the rank. A theory that tries to read a phase off the probability product looks for a square root of $-1$ that the product does not possess.

**The boundary.** The phase is not an element of this product: it is the argument of a value of it, and its generator belongs to the composition product. The half-angle and the loop are the owners' results.

### I.6.f — The Argument of the Amplitude Is a Phase, and the Loop Is the Invariant

**Read:** the band's pairing of two spinors is a complex number,

$$
A=\langle\tilde\Xi_1,\tilde\Xi_2\rangle_{*}=\mathrm{Sc}\bigl(\tilde\Xi_1\tilde\Xi_2^{*}\bigr),
$$

whose squared modulus is the transition probability and whose argument is the phase.

**The modulus is invariant under a central phase and the argument shifts by the relative phase.**

$$
\tilde\Xi_k\mapsto e^{i\theta_k}\tilde\Xi_k\quad\Longrightarrow\quad A\mapsto e^{i(\theta_1-\theta_2)}A .
$$

**The axis of the pair is not part of the amplitude.** It is the vector part of the commutator of the two state idempotents, hence the normal to the great circle joining the two directions on the Bloch sphere; the amplitude is a scalar and has no vector part.

**On a closed circuit the phases telescope and the product of the overlaps is invariant.** That product is the Pancharatnam phase, and for a circuit bounding a solid angle $\Omega$ it is half the solid angle, with the half being the mark of the double cover.

**The physical reading is that the algebra owns the pairing and the modulus, and the phase belongs to a loop.** The pair's phase is gauge dependent; only the loop is an invariant. The connection, the curvature and the half-solid-angle rule are not derived here.

**The boundary.** A single overlap has no invariant phase. The statement is about a closed circuit and a chosen representative on each ray.

### I.6.g — Causality: the Square Is the Interval, and the Type Composes While the Operation Does Not

**Read:** the quaternionic bilinear product is the only one whose square is central for every element, and its value is the interval.

$$
\tilde Q^{\natural}\tilde Q=\langle\tilde Q\rangle_{\natural}e_t,\qquad
\langle\tilde R_{\Phi}\rangle_{\natural}=-{r'_t}^{2}+x^{2}+y^{2}+z^{2}.
$$

**On the material sector the inertia is $(3,1)$ and the zero set is the light cone.** The level set $\{\langle\tilde Q\rangle_{\natural}=-m^{2}c^{2}\}$ is the mass shell; the value is multiplicative,

$$
\langle\tilde Q_1^{\natural}\tilde Q_2\rangle_{\natural}=\langle\tilde Q_1\rangle_{\natural}\langle\tilde Q_2\rangle_{\natural},
$$

so the causal type of a composite is the product of the causal types. The invertibles, the zero divisors and the null set are each closed under multiplication.

**The product is not associative, and the norm does not notice.** The composite of three causal operations depends on the bracket, while its interval is the product of the three intervals whatever the bracket. **The causal type composes even though the causal operation does not associate,** and that separation is the reason the interval can be an invariant of a theory whose operations do not compose.

**One qualification belongs to the sector.** The product of two material elements is material exactly when the two anticommute:

$$
\tilde Q_1\tilde Q_2\in\mathbb{B}_{\Phi}\ (\tilde Q_1,\tilde Q_2\in\mathbb{B}_{\Phi})\iff \tilde Q_1\tilde Q_2=-\tilde Q_2\tilde Q_1 .
$$

**So the light cone is not closed under composition inside the sector:** the sum of the two null directions $\vec e_x+i\vec e_y$ and $\vec e_x-i\vec e_y$ is a spacelike element, and the product of two null fields need not be a null field. What is closed is the causal *value*, not the causal *element*.

**The boundary.** The metric is the quaternionic form, not the plain one, and the causal structure lives on $\mathbb{B}_{\Phi}$; on the whole algebra the zero set is the zero-divisor cone, which is larger than the light cone. No propagation equation and no speed is derived here.

### I.6.h — Gauge: an Indefinite Form Is a Constraint, Not a State

**Read:** the quaternionic sesquilinear product has the Krein form as its scalar part, Hermitian and indefinite, of inertia $(2,6)$ on the real algebra and $(1,3)$ on each four-dimensional real-type subspace.

$$
\langle\tilde Q\rangle_{\natural*}=\lvert Q_t\rvert^{2}-\lvert\vec Q\rvert^{2}.
$$

**Two facts make the reading.** First, an indefinite form normalises nothing: there is no positive unit sphere, so its level sets are hyperboloids and not spheres. Second, its bridge to the definite form is one involution,

$$
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\langle\tilde Q_1^{\natural},\tilde Q_2\rangle_{*},\qquad
\langle\tilde Q^{\natural},\tilde Q\rangle_{\natural*}=\lVert\tilde Q\rVert^{2}>0,
$$

so the quaternion conjugation is the **fundamental symmetry** of the indefinite structure: its eigenspaces are the centre and the vector subspace, of complex dimensions one and three, of the two opposite signs and mutually orthogonal.

**The physical reading is that a constraint is not a state.** A definite form counts states: it is positive, it normalises, and its rank-one elements are pure states. An indefinite form fixes a redundancy: it distinguishes the two signs and leaves the normalisation to a gauge choice. On the material sector the Krein form is minus the interval, so the gauge form and the causal form are one form read with a sign, and on the informational sector they coincide.

**The boundary.** The Krein form is a form, not a gauge theory. No group, no coupling and no field content is derived. What the algebra supplies is the inertia, the fundamental symmetry and the resulting orthogonality.

### I.6.i — The Obstruction Needs a Complex Witness

**Read:** the antisymmetric part of the gauge product, $\tilde Q_1\wedge_{\natural*}\tilde Q_2$, is not a Lie bracket, and its failure of the Jacobi identity is the sparsest of the three.

**The witness is necessarily complex.** On real elements that bracket is the plain Lie bracket, which satisfies the identity; on the triple $(\vec e_x,\vec e_x,i\vec e_y)$ the cyclic sum is a nonzero multiple of $i\vec e_y$.

**The physical reading is that a real description cannot see this obstruction.** The failure lives in the complex structure: it needs an element whose vector part is imaginary relative to the real form, and it vanishes the moment the coefficients are taken real. A theory formulated on real coefficients therefore reports the bracket as closed and misses the obstruction.

**The count makes the statement sharp.** Of the $512$ triples of the basis, $252$ witness the failure of the plain sesquilinear bracket, $144$ that of the quaternionic bilinear one, and $72$ that of the quaternionic sesquilinear one. The sparsest failure is the one that carries the complex structure, and the densest is the one whose witness is real.

**The boundary.** A non-vanishing Jacobi sum is an algebraic fact about a bracket. Whether a physical symmetry algebra is expected to close is a separate hypothesis, and the entry does not derive a gauge algebra from a bracket that fails to be one.

### I.6.j — Only the Plain Column Closes

**Read:** of the twelve operations exactly two satisfy the identity of their kind, the Jordan product $\tilde Q_1\bullet\tilde Q_2$ and the Lie bracket $\tilde Q_1\wedge\tilde Q_2$, and both belong to the plain product.

**The reason is one fact about the parent.** The symmetrisation of an associative product is a Jordan product and its antisymmetrisation is a Lie bracket; the plain product is the only associative parent, so it is the only column that supplies both.

**The six failures are not six accidents.** The three Jordan failures have one shape: in the non-associative symmetrisations the square of a pure vector is central, so the iteration of the product has already forgotten the direction before the identity can compare the two orders. The three Jacobi failures have three reasons: the quaternionic bilinear bracket inherits the non-associativity of its parent; the plain sesquilinear bracket fails on the densest set; and the quaternionic sesquilinear one fails only on complex witnesses.

**The physical reading is that the corpus's two classical structures are not a matter of luck.** An algebra of observables needs a Jordan product, and a symmetry needs a Lie bracket, and both exist here in one column because one product is associative. Every other job in the grid is a pairing and not an algebra, and a pairing does not need an identity to be useful.

**The boundary.** Failing the Jordan identity does not make a symmetrisation useless; it makes it a coupling and not an algebra of observables. The distinction is between a product that can be iterated as an observable and one that can only be evaluated.

### I.6.k — The Symmetric Half Measures and the Antisymmetric Half Generates

**Read:** for every one of the four parents, the symmetric part keeps the scalar part and the antisymmetric part kills it.

$$
\mathrm{Sc}\,f^{\mathrm{s}}=\mathrm{Sc}\,f,\qquad \mathrm{Sc}\,f^{\mathrm{a}}=0 .
$$

**The consequence is a division of the twelve into the measurable and the generative.** A measurement returns a scalar; only the symmetric half carries one. A transformation needs a direction; only the antisymmetric half carries one, and its value lies in the vector subspace.

**So each of the four jobs comes with a quantity and an order.** Composition has a signed overlap and a rotation axis; probability has an expectation value and an interference term; causality has the interval and the boost obstruction; gauge has the indefinite calibration and the polarisation direction.

**The vector part makes the same point from the other side.** Nine distinct vector parts exist among the twelve, and the three coincidences are exactly the cases where the symmetric half is central: where the quantity is a pure scalar, the parent and its antisymmetric half have the same direction, and a vector-only probe cannot distinguish them.

**The boundary.** The words are the corpus's and the division is the algebra's. The entry does not claim that every measurement is a symmetric half, only that the scalar part is what a form can pair with.

### I.6.l — The Twelve Are Ten in a Real Description

**Read:** on the real part of the space two pairs of the twelve coincide, and the count falls from twelve to ten.

**The two coincidences are not accidents of notation.** For real elements the coefficientwise conjugation is the identity, so the two sesquilinear families collapse onto the two bilinear ones in the pairs that differ only by that conjugation: the antisymmetric plain bilinear product equals the antisymmetric quaternionic sesquilinear one, and the symmetric quaternionic bilinear product equals the symmetric plain sesquilinear one.

**The physical reading is a limit on what a classical description can distinguish.** A real-valued formulation sees ten operations, and the two it cannot separate are separated only by the complex structure. A property that holds for one member of a coincident pair and fails for the other is therefore invisible in the real formulation: the identity survives in one member and is lost in the other, and the real description reports both as the same object.

**The sharpest case is the Jacobi failure of the gauge bracket.** It is invisible on real elements, so a real formulation reports the bracket as a Lie bracket. The complex structure is the carrier of the obstruction and not a convenience of the calculation.

**The boundary.** The twelve are the operations of the complex space. A real form carries ten of them, and every statement of the source articles is a statement about the complex space unless it says otherwise.

### I.6.m — In the Gauge Band an Idempotent Is Invertible

**Read:** the equation $\tilde\Pi\star\tilde\Pi=\tilde\Pi$ is relative to the product, so the word *idempotent* names a different set in each band; and in one of them the elements of that set are invertible.

**The family is displaced, and the displacement is the reason.** For the quaternionic sesquilinear product the idempotents beyond the trivial pair are not the Hermitian ones at all. They are

$$
\tilde\Pi_d=-\tfrac12e_t+\tfrac{\sqrt3}{2}\vec u,\qquad(\vec u,\vec u)=1,
$$

which is $\tilde\Pi_d^{\natural}\tilde\Pi_d^{*}=\tilde\Pi_d$: its two conjugates coincide, $\tilde\Pi_d^{\natural}=\tilde\Pi_d^{*}=-\tfrac12e_t-\tfrac{\sqrt3}{2}\vec u$, and the square of that element is $\tilde\Pi_d$ itself. The family is written about the point $-\tfrac12e_t$ and not about $\tfrac12e_t$, and it lies in the real quaternion layer $\mathbb{B}_{H}$.

**Its elements are invertible in the algebra.** The plain square is the conjugate, not the element itself,

$$
\tilde\Pi_d^{2}=-\tfrac12e_t-\tfrac{\sqrt3}{2}\vec u=\tilde\Pi_d^{\natural},
\qquad
\tilde\Pi_d\tilde\Pi_d^{\natural}=e_t,
$$

so $\tilde\Pi_d$ has inverse $\tilde\Pi_d^{\natural}$ and is not a zero divisor. The physical reading is the one this entry is built to give: an idempotent is an outcome only in the plain band, and the implication *idempotent, therefore irreversible* is a statement about that band and not about the algebra. In the gauge band the projection is reversible, and a reader who carries the vocabulary across the bands carries a falsehood with it.

**The pair reading fails in the same band.** The complement $e_t-\tilde\Pi_d=\tfrac32e_t-\tfrac{\sqrt3}{2}\vec u$ is not an idempotent of that product, so there is no complete orthogonal pair and no resolution of the unit into two outcomes. Only the plain band and the general plain sesquilinear band carry a complementation that preserves their family, which is why the two-outcome reading is made in I.6.b and I.6.d and nowhere else.

**The boundary.** The statement is a statement about solution sets, and it is why the twelve rows of the root table cannot be read by one vocabulary. It derives no gauge theory and says nothing about whether a physical projection may be reversible; it says that in this band the algebra does not force the question.

## The Limits

**The naming is a reading and not a theorem.** The algebra proves the four settings, the property table, the two slots, the central square, the positive square and the twelve operations. It does not prove that a physical theory needs exactly four products, that the four jobs are these four, or that no other assignment is possible.

**The four jobs are form-level statements.** For a general element the four forms are four different complex numbers and do not agree; an identity on a real-type subspace does not make two products equal there. The readings are made on the sectors, and a statement about the material sector is not a statement about the algebra.

**The sector dictionary is a convention.** That $\mathbb{B}_{\Phi}$ is spacetime and $\mathbb{B}_{\Psi}$ is the state side is the corpus's hypothesis, stated elsewhere. The sector structure is proved; its physical naming is not.

**The counts are basis-dependent.** $252$, $144$ and $72$ are counts on the eight-element basis, given as the shape of each failure; they are not invariants of the bracket, and they change with the basis.

**No product is derived from its job, and no job from its product.** The products are the algebra's; the jobs are the readings. The entry derives no dynamics, no state space, no mass spectrum, no gauge group and no measurement postulate.

**The grid is a grid of products on $\mathbb{B}$, and that is why entanglement is not a row.** Each of the twelve operations is a map $\mathbb{B}\times\mathbb{B}\to\mathbb{B}$: a pair of elements in, one element out. A correlation between two systems is not of that type. It is a property of one element of the tensor square $\mathbb{B}\otimes\mathbb{B}$, and the operation that extracts it, the partial trace, is a map $\mathbb{B}\otimes\mathbb{B}\to\mathbb{B}$ with one factor already traced against the scalar pairing. So entanglement was never a candidate for a fifth row: a fifth row would need a fifth setting of the two dials, and there is none, while a shared state needs a second factor, and the grid has one factor by construction. The argument is the reason I.6.a can say there is no fifth product and mean it.

**The collapse on the real part is a loss of information, not a simplification.** A real computation is not a cheaper route to the same answer about the twelve; it is a computation about ten operations, two of which stand for two each.

## Summary

- The algebra carries four general products, and they are the four settings of one rule: the plain product with a conjugation inserted in the first slot, the second, both or neither.
- The settings form the group $\mathbb{Z}_2\times\mathbb{Z}_2$; there is no fifth setting, because an anti-automorphism fixing the unit is the identity or the quaternion conjugation.
- The second dial decides iterability: a bilinear product has a left unit and a monoid of left multiplications, a sesquilinear one has neither.
- The first dial decides definiteness: the plain first slot gives a form definite on each sector, the quaternionic one gives an indefinite form whose null set is the zero-divisor cone.
- Only the plain product is associative and two-sidedly unital, and only it is the multiplication of an algebra over $\mathbb{C}$.
- The quaternionic bilinear product is the only one whose square is central, and the central value is the interval; the plain sesquilinear square is Hermitian, positive semidefinite and rank-bearing.
- Each product splits into a symmetric and an antisymmetric half, and the twelve operations are the four parents with their halves; the symmetric half keeps the scalar part, the antisymmetric half kills it.
- The two central symmetrisations have no vector part, which is why the parent and its antisymmetric half share a vector part in those two families; the twelve vector parts fall into nine classes.
- Exactly two of the twelve satisfy a classical identity, the Jordan product and the Lie bracket of the plain product, and they exist because the plain product is the only associative parent.
- The Jacobi failures count $252$, $144$ and $72$ triples; the Jordan failures count $7$, $6$ and $4$ elements; the sparsest Jacobi failure needs a complex witness.
- An idempotent belongs to a band: the gauge band's idempotents are $- \tfrac12e_t+\tfrac{\sqrt3}{2}\vec u$, they are invertible in the algebra, and their complement is not one of them, so the pair reading does not reach that band.
- The grid is a grid of products on $\mathbb{B}$, so entanglement is not a fifth row: a shared state is an element of $\mathbb{B}\otimes\mathbb{B}$ and the partial trace is a map on the tensor square.
- The four forms have inertias $(0,4)$ or $(4,0)$, $(3,1)$ or $(1,3)$, $(4,0)$, $(1,3)$ on the two sectors, which is the algebraic content of the four names.
- Probability is the only definite form, and its product has no clock: the central element squares to $+e_t$, there is no nilpotent of index two, and the cone appears at the third power.
- Causality is the only multiplicative norm, and the causal type composes while the causal operation does not associate.
- Gauge is the only indefinite Hermitian form, and its fundamental symmetry is the quaternion conjugation.
- On the real part two pairs of the twelve coincide and the count falls to ten, which is why a real computation cannot see the complex obstruction.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde Q^{\natural}$ | the quaternion conjugation: central coordinate fixed, vector coordinates negated |
| $\tilde Q^{*}$ | the Hermitian conjugation $\bar{\cdot}\circ{}^{\natural}$ |
| $\bar{\tilde Q}$ | the coefficientwise conjugation |
| $\langle\cdot,\cdot\rangle$ | the plain form, $\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ |
| $\langle\cdot,\cdot\rangle_{\natural}$ | the quaternionic form, $\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2)$ |
| $\langle\cdot,\cdot\rangle_{*}$ | the Hermitian form, $\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$ |
| $\langle\cdot,\cdot\rangle_{\natural*}$ | the Krein form, $\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*})$ |
| $\tilde Q_1\bullet\tilde Q_2$ | the symmetric part of the plain bilinear product |
| $\tilde Q_1\wedge\tilde Q_2$ | the antisymmetric part of the plain bilinear product |
| $\bullet_{\natural},\bullet_{*},\bullet_{\natural*}$ | the symmetric parts of the other three products |
| $\wedge_{\natural},\wedge_{*},\wedge_{\natural*}$ | the antisymmetric parts of the other three products |
| $\mathbb{B}_{\Phi},\mathbb{B}_{\Psi}$ | the anti-Hermitian and Hermitian sectors |
| $\mathcal{N}$ | the zero-divisor cone, the null set of the quaternionic form |
| $V_f$ | the vector part of the product $f$ |
| $J={}^{\natural}$ | the fundamental symmetry of the Krein form |

## Further Reading

**In the mathematics corpus.** The five articles of the source table, and inside them *The Property Table*, which is the algebraic content of the four names, and *The Counts of the Failures*, which is the density of each obstruction.

**In this category.** *The Spectrum and the Two Modes* supplies the two squares as spectral objects: the interval is the discriminant of the quaternionic square, and the mass shell is a level set of the causal value. *The Modules: What the Algebra Acts On* supplies the left multiplications that are the monoid of the composition reading. *Idempotents, Ideals and Observables* supplies the minimal Hermitian idempotents that are the pure states of the probability reading.

**The sources of this entry.** [The Partition: Two Invariants and Four Regimes](the-partition-two-invariants-and-four-regimes.html) is the no-clock theorem, the third-power cone and the geometric phase. [Pancharatnam's Phase and the Polarization Sphere in Biquaternionic Form](pancharatnams-phase-and-the-polarization-sphere-in-biquaternionic-form.html) is the loop phase of the probability reading. The four labels with the $4\times3$ mnemonic table, and the eight labels with the four columns of three, are stated here.
