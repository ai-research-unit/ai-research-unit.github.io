# __The Physical Interpretation of the 12 Products__

## Introduction

The biquaternion complex space carries twelve products and not four. The four general products are the operations; each splits into a symmetric part, which keeps the value of the parent and loses its order, and an antisymmetric part, which keeps the order and loses the value. The four parents and their eight halves are the twelve structures of the space, and they are twelve operations on one vector space, not twelve algebras.

This article reads the twelve physically in one place. It gives the eight labels and the two classical laws; it compares the value, the form and the unit of the twelve; it reads the degeneracy of each, the kernel of each, and the values each can square to. The three companion readings — the zero divisors, the annihilators and the roots — are gathered here because they answer three questions of the same twelve objects: where each degenerates, what each forgets, and what each can square to.

The article owns no theorem. Each result is stated in a sentence, the mathematics article that proves it is linked, and the reading is given with its boundary. The naming of a structure is a claim about the physical job it can carry, not a theorem of the algebra.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The twelve products, their multiplication tables and their values | [The 12 Products of the Biquaternion $\mathbb{C}$ Space](../articles_maths/the-12-products-of-the-biquaternion-complex-space.html) |
| The twelve structures, their products, values, units and identities | [The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](../articles_maths/the-algebraic-structures-over-the-biquaternion-c-space.html) |
| The Jordan and Jacobi identities, the two that hold and the six witnesses of failure | [The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](../articles_maths/the-algebraic-structures-over-the-biquaternion-c-space.html) |
| The realification, the real dimension, the real operators and the signatures | [The Realification of the Eight Derived Structures](../articles_maths/the-realification-of-the-eight-derived-structures.html) |
| The four forms and their signatures | [The 4 Forms over the Biquaternion $\mathbb{C}$ Space](../articles_maths/the-4-forms-over-the-biquaternion-c-space.html) |
| The four algebraic norms and their definiteness and multiplicativity | [The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space](../articles_maths/the-4-algebraic-norms-over-the-biquaternion-c-space.html) |
| The twelve zero-divisor sets and the cone | [Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](../articles_maths/zero-divisors-in-the-algebraic-structures-over-the-biquaternion-c-space.html) |
| The twelve annihilators, their dimensions and the two sides | [Annihilators in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](../articles_maths/annihilators-in-the-algebraic-structures-over-the-biquaternion-c-space.html) |
| The root equation and the four existence classes | [Square Roots of a General Element in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](../articles_maths/square-roots-of-a-general-element-in-the-algebraic-structures-over-the-biquaternion-c-space.html) |
| The roots of $+1$ and of $0$ | [Square Roots of One and the Idempotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](../articles_maths/square-roots-of-one-and-the-idempotents-in-the-algebraic-structures-over-the-biquaternion-c-space.html), [Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](../articles_maths/square-roots-of-zero-and-the-nilpotents-in-the-algebraic-structures-over-the-biquaternion-c-space.html) |
| The norm, its vanishing, the cone and the unit group | [Norm and Invertibility in the Biquaternion Algebra](../articles_maths/norm-and-invertibility-in-the-biquaternion-algebra.html) |

## The Twelve and Their Two Halves

### One Product, Two Parts

Let $\circ$ be one of the four general products. Its symmetric and antisymmetric parts are

$$
\boxed{\;S(x,y)=\tfrac12\bigl(x\circ y+y\circ x\bigr),
\qquad
A(x,y)=\tfrac12\bigl(x\circ y-y\circ x\bigr)\;},
$$

so that $x\circ y=S(x,y)+A(x,y)$ for every pair. For the two sesquilinear parents the exchange is not the plain one: the second term is the conjugate of the product in the opposite order,

$$
S(x,y)=\tfrac12\bigl(x\circ y^{*}+\overline{y\circ x^{*}}\bigr),
\qquad
A(x,y)=\tfrac12\bigl(x\circ y^{*}-\overline{y\circ x^{*}}\bigr).
$$

In both families the split is a split of the **product map**, not of an algebra. The symmetric part survives the exchange of the two factors; the antisymmetric part changes sign. Neither part is closed under composition in general, and the parent is not the direct sum of the two as an algebra. What is true is that the parent is the sum of the two as products on the same vector space.

The associativity of the parent decides which identities survive: the symmetrisation of an associative product is a Jordan product, and its antisymmetrisation is a Lie product. Of the four parents only the general plain algebra is associative. That single fact is why the plain pair, and only the plain pair, carries the two classical nonassociative algebras.

### The Eight Labels

The four parents are stated first, in their four jobs; their two halves are then read one by one.

| the parent | the product | the square | the word | the unit |
| --- | --- | --- | --- | --- |
| $\mathrm{GPA}$ | $\tilde Q_1\tilde Q_2$ | $\tilde Q^{2}$ | composition | $e_t$ on both sides |
| $\mathrm{GPS}$ | $\tilde Q_1\tilde Q_2^{*}$ | $\tilde Q\tilde Q^{*}$, Hermitian and rank-bearing | probability | $e_t$ on the right alone |
| $\mathrm{GQA}$ | $\tilde Q_1^{\natural}\tilde Q_2$ | $\langle\tilde Q\rangle_{\natural}e_t$, central and signed | causality | $e_t$ on the left alone |
| $\mathrm{GQS}$ | $\tilde Q_1^{\natural}\tilde Q_2^{*}$ | the Krein value, indefinite | gauge | none |

The general plain sesqualgebra $\mathrm{GPS}$ has the positive definite Hermitian form as its scalar part, and its square is the rank-bearing operator $\tilde Q\tilde Q^{*}$: it is the band of the state and the observable. The general quaternionic algebra $\mathrm{GQA}$ has the interval as its central square, and its null set is the causal cone: it is the band of the four-vector. The general quaternionic sesqualgebra $\mathrm{GQS}$ has the indefinite Krein form, whose isometry group is $\mathrm{U}(1,3)$ over $\mathbb{C}$ and $O(2,6)$ over $\mathbb{R}$: it is the band of admissible internal frames.

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

The four words of the symmetric half and the four words of the antisymmetric half are the thread of the article. The symmetric half keeps the scalar part of the parent and loses the direction; the antisymmetric half keeps the direction and loses the scalar part. The physical difference between measuring and generating is that loss.

### The Two Laws

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

The last column of the three Jacobi rows is the cyclic sum of the bracket on the triple, and the two sides of the Jordan rows are $(x^{2}\bullet x)\bullet x$ and $x^{2}\bullet(x\bullet x)$.

The three Jordan failures have one algebraic shape: in the non-associative symmetrisations the square of the pure vector $\vec e_x$ is central, so the iteration of the product has already forgotten the direction before the identity can compare the two orders. Physically a coupling with a central square is not an algebra of observables: a number cannot remember the direction it came from, and measuring the coupling twice does not reproduce the coupling of the square.

The three Jacobi failures have three different reasons. For $\mathrm{AQA}$ the culprit is the non-associativity of the quaternionic product it comes from: the natural conjugation in one slot breaks the associativity that the Jacobi identity of a commutator needs. For $\mathrm{APS}$ and $\mathrm{AQS}$ the culprit is the sesquilinear obstruction: the antisymmetrisation of a sesquilinear product is a Lie bracket only after the collapse of the two involutions, and a genuine sesqualgebra forbids that collapse. The failure is a statement about the sesquilinear pairing and not about a real subspace.

The pattern of the table is the pattern of the four words. Composition has an order-free part that is a Jordan algebra and an order-sensitive part that is a Lie algebra, because the plain product is associative. Probability, causality and gauge have neither: their symmetric halves are couplings that forget the direction, and their antisymmetric halves are brackets that do not close.

## The Twelve Compared

### Value, Form and Unit

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

Read by column, the table gives the three divisions of the twelve: the family (four parents, four symmetric parts, four antisymmetric parts), the value (the whole space, the centre, the vector subspace, or no remarkable subspace) and the law (only the plain pair carries a classical algebra). Read by row, it gives the one exact coincidence: a parent and its symmetric part share the form. The unit is shared only for the plain pair, because the symmetrisation of a sesquilinear product replaces the unit by a conjugation. The antisymmetric part shares neither.

That coincidence is why the symmetric half is the half that measures. The form is the scalar part, and the scalar part is the only thing a state can be paired with. A bracket has a direction and no scalar value, so it can generate and cannot be measured.

### The Four Columns of Three

Read by product, the twelve fall into four columns of three. Each column is one job, and within it the general product is the operation, the symmetric part the quantity, and the antisymmetric part the order or the phase:

| | composition | probability | causality | gauge |
| --- | --- | --- | --- | --- |
| operation | the product of a boost rotor and a rotation rotor | the Born pairing of a state and an observable | the quaternionic product of two four-vectors | the Krein pairing of two internal frames |
| quantity (symmetric) | the signed Euclidean overlap | the expectation value | the Minkowski inner product, whose diagonal is the interval | the indefinite calibration, i.e. the Krein form |
| order or phase (antisymmetric) | the rotation axis | the interference | the boost obstruction, the bracket that fails | the polarisation direction |

The two classical structures sit in the composition column as the two halves that close: $\mathrm{SPA}$ in the quantity row, where the Jordan product is the observables' product, and $\mathrm{APA}$ in the order row, where the Lie bracket is the rotation. No other cell is a classical algebra, and that scarcity is the table's point: the twelve are not twelve equivalent structures, but four jobs each with a quantity half and an order half, of which only the two halves of the composition column are classical.

**The boundary.** The four-column table is a reading of the same twelve products, not a theorem that the columns are independent or that the assignment of jobs is forced. The operation, quantity and order entries are the framework's names; the products and the identities are the algebra's.

## Degeneracy Across the Twelve

### One Wall, Three Sets

A zero divisor is a nonzero element with a nonzero annihilating partner. It is an operation that cannot be inverted, and the set of such operations is the wall of the reversible region. The twelve products do not give twelve unrelated walls.

| the group | the structures | the zero-divisor set | the reason |
| --- | --- | --- | --- |
| the four general products | $\mathrm{GPA}$, $\mathrm{GPS}$, $\mathrm{GQA}$, $\mathrm{GQS}$ | $\mathcal{C}\setminus\{0\}$ | the conjugation in one or both slots is a bijection and does not move the norm |
| the two symmetric structures | $\mathrm{SPA}$, $\mathrm{SQS}$ | $(\{Q_t=0\}\cup\mathcal{C})\setminus\{0\}$ | the symmetrisation also annihilates the pure elements |
| the six scalar-valued or antisymmetric structures | $\mathrm{SPS}$, $\mathrm{SQA}$, $\mathrm{APA}$, $\mathrm{APS}$, $\mathrm{AQA}$, $\mathrm{AQS}$ | $\mathbb{B}\setminus\{0\}$ | the value is a number or a pure direction, so the map cannot be injective |

The **cone** is the common zero set of the quaternion norm, $\mathcal{C}=\{\tilde Q:\langle\tilde Q\rangle_{\natural}=0\}$, a complex cone of complex dimension three and real dimension six. It lies in every one of the twelve sets, so no band is free of degeneracy. The **nilpotent cone** is its pure part, of real dimension four, and it is strictly smaller than the cone: a zero divisor need not be nilpotent.

The enlargement of $\mathrm{SPA}$ and $\mathrm{SQS}$ is physical. A pure element, one with $Q_t=0$, kills the plane of operations orthogonal to it, and it does so whether or not it is lightlike. The cleanest witness is a unit: $\vec e_x$ has norm $1$ and is invertible in the algebra, yet $\vec e_x\bullet\vec e_y=0$ for the Jordan product. The classical equivalence *zero divisor if and only if not a unit* therefore fails, and an invertible element can fail to compose symmetrically.

The whole space of the other six is the algebraic form of their irreversibility. A scalar coupling returns a number, and a number has no inverse. A bracket returns a direction and not an operation, so it is an infinitesimal transformation and not something to be undone. Neither kind has a unit to invert.

### The Wall and Its Two Families

The cone splits into two families, and the split is physical. The **pure null family**, $Q_t=0$ and $(\vec Q,\vec Q)=0$, is the nilpotent family of lightlike displacements. The **non-pure family** is the multiples of the idempotents, that is, the states. A state is a zero divisor because a measurement cannot be undone, not because its square vanishes. Both lie on the same wall, and only the first is square-zero.

The off-cone elements are the invertible elements of the plain product, and they form the group $\mathbb{B}^{\times}\simeq S^{1}\times S^{3}$ with $\pi_1\cong\mathbb{Z}$. The cone is the complement of that group, so the reversible operations are exactly the off-cone ones and the light cone is the wall of the reversible region. The other structures keep the wall and lose the group: an element off the cone is invertible in the four general products, but the products are not associative, so the invertible elements form no group; the symmetrisations and the brackets destroy invertibility or have no unit at all.

On the material sector the cone cuts down to the physical light cone, the locus of lightlike propagation and the boundary between the reversible and the irreversible. The four general products read the same wall with four names: composition degenerates there, the probability square has rank one there, the interval vanishes there, and the gauge multiplication drops rank there. One set, four readings.

The projectivisation of the cone is the **celestial sphere** along which a photon's momentum points. The proper orthochronous Lorentz group acts transitively on its future directions, the past directions are a second copy, and time reversal exchanges the two. Complexified, the projectivisation is the **Segre quadric**, whose two rulings are the two chiral celestial spheres.

The cone is also the **information barrier**. A reset memory lands on a pure state, which is a zero divisor, and the reset costs $k_BT\log2$: that is Landauer's price. A gauge kernel hides a description that a gauge choice can recover; a confinement kernel destroys a description that the observable algebra no longer contains, and that loss is an absent label rather than an erased memory, so it carries no Landauer price.

### The Kernels

The annihilator of an element is the set of partners it kills. It is the kernel of the operation "multiply by it", so it is the kernel of a process: the set of inputs the process merges into nothing. A process is invertible exactly when its kernel is trivial, and the dimension of the kernel is the rank drop.

| the group | the annihilator | the two sides |
| --- | --- | --- |
| the four general products | $\{0\}$ off the cone; a complex plane on it | differ for $\mathrm{GPA}$ and $\mathrm{GQS}$, equal for $\mathrm{GPS}$ and $\mathrm{GQA}$ |
| $\mathrm{SPA}$, $\mathrm{SQS}$ | $\{0\}$ off the cone; the line $\mathbb{C}\tilde Q^{\natural}$ or $\mathbb{C}\tilde Q^{*}$ on it; a plane at a pure element | equal |
| $\mathrm{SPS}$, $\mathrm{SQA}$ | the hyperplane $\langle\tilde Q,\tilde Q_1\rangle_{*}=0$ or $\langle\tilde Q,\tilde Q_1\rangle_{\natural}=0$ | equal |
| $\mathrm{APA}$, $\mathrm{AQS}$ | $\mathbb{C}e_t\oplus\mathbb{C}\vec Q$, or its conjugate; the whole space at a central element | equal |
| $\mathrm{APS}$, $\mathrm{AQA}$ | a line off the cone, a plane on it; the centre at a central element for $\mathrm{AQA}$ | equal |

The two sides differ for exactly two structures, the plain composition and the gauge coupling: that is the **chirality of the internal action**. The sharpest instance is the photon. For the null momentum $\tilde P=2i(E/c)\tilde\Pi_-$, with $\tilde\Pi_-=\tfrac12(e_t-i\vec e_z)$, the left multiplication kills $\tilde\Pi_+=\tfrac12(e_t+i\vec e_z)$, because $\tilde\Pi_-\tilde\Pi_+=0$. A massless momentum of one chirality annihilates the opposite chiral state, which is the algebraic form of the statement that a massless fermion has only one helicity.

For the two scalar-valued structures every nonzero element has a hyperplane as its annihilator: a number destroys one complex dimension. For the two brackets $\mathrm{APA}$ and $\mathrm{AQS}$, a nonzero central element kills the whole algebra: those brackets are blind to the centre. That centre is the framework's **classical sector**, the home of the $c$-number parameters such as $\hbar$, $c$, a mass and a coupling.

The kernel has four physical names for one object. It is the **zero-mode space** of the index theorem, the space of solutions the Dirac operator cannot see; the **GNS null space**, the directions that the state functional sends to zero; the **no-cloning obstruction**, the set of inputs a copying map would have to merge; and the **BRST closed space**, whose quotient by the image is the physical cohomology. The four names are four processes, and the annihilator is the same algebraic set in each.

The kernel can be structural rather than a constraint. The Bianchi identity says that the cyclic covariant derivative annihilates every field strength, and it is the operator Jacobi identity rewritten. An anomaly is a current that is no longer in the kernel of the divergence at one loop, and its cancellation is a condition that keeps the kernel large enough. A Bogoliubov transformation changes the annihilator itself, so the vacuum of one mode expansion is not annihilated by the operators of another, which is the algebraic shape of the Unruh and Hawking effects.

## The Roots Across the Twelve

### The Four Existence Classes

A root of a central value $\lambda$ in one of the twelve structures is an element whose square in that product is the value, $\tilde\Xi\star\tilde\Xi=\lambda e_t$. The root problem asks which elements realise a given value. It is the inverse of the square map, and the square map is the band's way of producing a number from an operation: the plain square produces a polar scale and a direction, the central square produces the interval, the Hermitian square produces a probability weight, and the fourth square produces the indefinite gauge value.

Two squares do most of the grouping. The **plain square** $\tilde\Xi^{2}$ belongs to $\mathrm{GPA}$ and $\mathrm{SPA}$; the **central square** $\tilde\Xi^{\natural}\tilde\Xi=\langle\tilde\Xi\rangle_{\natural}e_t$ belongs to $\mathrm{GQA}$ and $\mathrm{SQA}$. The sesquilinear bands have two squares of their own: the **Hermitian square** $\tilde\Xi\tilde\Xi^{*}$, positive semidefinite and rank-bearing, and the **fourth square** $\tilde\Xi^{\natural}\tilde\Xi^{*}$, the indefinite gauge value. The symmetric quaternionic sesqualgebra is the exception: its square is the Hermitian part of the fourth square, a real element whose root sets are those of a symmetrised coupling. The four antisymmetric structures have no square of their own beyond the zero or pure value: an antisymmetrisation kills the scalar part, so a bracket cannot realise a nonzero central value at all.

For a general complex value $\lambda$ the twelve structures fall into four classes.

| the class | the structures | the values that have a root |
| --- | --- | --- |
| bilateral | $\mathrm{GPA}$, $\mathrm{GQA}$, $\mathrm{SPA}$, $\mathrm{SQA}$ | every complex $\lambda$ |
| indefinite sesquilinear | $\mathrm{GQS}$, $\mathrm{SQS}$ | every real $\lambda$ |
| definite sesquilinear | $\mathrm{GPS}$, $\mathrm{SPS}$ | every real $\lambda\geq0$ |
| antisymmetric | $\mathrm{APA}$, $\mathrm{APS}$, $\mathrm{AQA}$, $\mathrm{AQS}$ | $\lambda=0$ alone |

The classes are physical. The bilateral structures read every value, phase and amplitude together: the composition and causality bands can produce any complex value. The probability band admits only non-negative values, because a probability weight is non-negative, and it has the origin alone at $0$, because no nonzero amplitude squares to nothing. The gauge band produces the Krein interval, which is real by construction. The brackets produce a pure or vanishing object, so only $0$ is readable.

### The Three Named Values

A root of $+1$ is an **involution**: a parity, a reality condition, a discrete symmetry, or, in the probability band, a unitary transformation of the state space. The plain and natural products produce the involutions of the module; the probability band's involution is the unitary group $\mathrm{U}(2)$; the symmetrisation replaces unitarity by normalisation, the root being a normalised amplitude without its phase; and a bracket produces no involution at all. The compactness of $\mathrm{U}(2)$ is what makes the internal labels discrete.

An **idempotent** is an element equal to its own square. In the plain product the two equations are one equation read through the halving map,

$$
\boxed{\;\tilde\Pi=\tfrac12(e_t+\tilde\Xi),
\qquad
\tilde\Xi=2\tilde\Pi-e_t\;},
$$

which is a bijection between the roots of $+1$ and the idempotents. An idempotent is a projection, and a projection is a determinate state: measuring twice gives the same result as measuring once. The idempotent sets are the state sets of the bands. The plain product carries the largest family, one state per root of one; the Hermitian idempotents are the pure states of the probability band, on the boundary of the positive cone; the gauge family is the only nontrivial family of idempotents that are units. The brackets and the interval band carry no nontrivial state: an infinitesimal transformation has no determinate state, and a state is not an interval.

A nonzero root of $0$ is a **nilpotent of index two**, written $\tilde\Upsilon$: a square-zero element. It kills itself, so it is an element of its own annihilator, and physically it is an infinitesimal object of which two successive applications give nothing. The lightlike displacement is the pure member. Nilpotency is also Pauli exclusion: the one-mode fermionic ladder is a pair of nilpotents $a,a^{\dagger}$ with $a^{2}=(a^{\dagger})^{2}=0$ and $\{a,a^{\dagger}\}=e_t$, whose product is the vacuum idempotent. The BRST charge and the supercharge are the odd members, and the supercharge is nilpotent only on the massless shell.

A root of $-1$ is a **local complex structure**: a phase, a clock, a half-turn, the Kramers sign. It is deduced from a root of $+1$ by multiplication by the central imaginary in the six bilinear structures, and the mechanism is not universal. The two definite sesquilinear structures and the four brackets have no root of $-1$; the two indefinite sesquilinear structures have one, and in $\mathrm{SQS}$ the witness $\tfrac{1}{\sqrt2}(\vec e_x+i\vec e_y)$ lies on the cone. The physical interpretations of $-1$ belong to the articles on the phase and the clock.

The root sets of $0$ are the sharpest contrast with the zero-divisor sets. The four general products share one zero-divisor set, the cone, but their root sets are different: the plain band has the origin together with the pure null cone, the probability band has the origin alone, the interval band has the whole cone, and the gauge band has the slopes $\lvert t\rvert=1$ of its causal classes. Degeneracy is common across the bands, while factorisation is band-specific.

### The Shells

A shell of a given sign is generated from the unit shell by scaling. The interval is quadratic in the scale, so the mass shell is the unit shell scaled by $mc$, and the cone is the scale-free limit of the family. The magnitude of the value sets the size of the shell and its sign sets the causal class: negative for the timelike shell of a massive particle, zero for the cone, positive for the spacelike or tachyonic shell. For the interval structures the root of a nonzero value is a unit whatever the sign, so a tachyon is invertible and only the value zero has non-invertible roots.

The plain structures have the richest sets: two central roots $\pm\sqrt\lambda\,e_t$ and a pure quadric of real dimension four. The probability band has a family of real dimension four at a positive value and the origin alone at zero; its symmetrisation has a sphere of real dimension seven there, because it forgets the vector part of the square and the equation loses its rigidity. The natural and symmetric-quaternionic structures have a quadric of real dimension six at a value, which is the mass shell. The gauge band has a family of real dimension four at each real value, with the slope separating the causal classes.

The sign is also why the retired single-field mass equation fails. Its solutions lie on the spacelike shell, while a physical mass term must place them on the timelike one, and the conjugation rather than a number is what makes the choice. A complex value has no causal class: the unstable state is a complex central pole whose real part is the energy and whose imaginary part is half the width, so a decaying state has a lifetime instead of a shell. Only the plain band realises such a value as a pole, by the scalar process $\sqrt\lambda\,e_t$; the interval bands read a real interval, so a complex pole is never one of their shells.

## Limits

The algebra proves the split, the eight products, the two identities, the six witnesses, the twelve degeneracy sets, the twelve kernels and the four root classes. It does not prove that the eight words are the only interpretations of the structures, nor that the four jobs are the only assignment of the four parents.

Three boundaries follow. The symmetric parts are not, in general, Jordan algebras: only $\mathrm{SPA}$ is one, and calling $\mathrm{SPS}$ or $\mathrm{SQS}$ a Jordan algebra would erase the witnesses. The antisymmetric parts are not, in general, Lie algebras: only $\mathrm{APA}$ is one, and the Jacobi failures are the content of the words *phase*, *obstruction* and *polarisation*. The reconstruction $G=S+A$ is exact as a decomposition of the product and does not make the parent a direct sum of two algebras.

The degeneracy, the kernel and the root are sets of the algebra. Their identification with a light cone, a loss of information or a mass shell is a reading, and the reading names the band and the process. The algebra supplies the set, its dimension and its shape; the physics supplies the object.

## Summary

The four general products split into eight derived structures, and the split is a split of each product into an order-free half and an order-sensitive half. The symmetric half keeps the value of the parent and carries the four forms; the antisymmetric half keeps the direction and carries the zero form. Of the eight, only $\mathrm{SPA}$ is a Jordan product and only $\mathrm{APA}$ is a Lie product, because only the plain parent is associative. The other six fail the identity of their kind, with the witnesses $\vec e_x$ for the three Jordan failures and the triples $(e_t,\vec e_x,\vec e_y)$ and $(\vec e_x,\vec e_x,i\vec e_y)$ for the three Jacobi failures.

The twelve compared give three divisions: the family, the values and the law. Read by product, they fall into four columns of three, one column for each job, with the operation, the quantity and the order or phase in the three rows. The degeneracy has one wall and three sets: the cone for the four general products, the cone together with the pure elements for $\mathrm{SPA}$ and $\mathrm{SQS}$, and the whole punctured space for the other six. The kernel is trivial off the cone and grows on it; it is a hyperplane for the scalar-valued structures, a centraliser for the rotation bracket, and it differs on its two sides only for the plain product and the gauge coupling. The root problem separates the twelve into four existence classes: every value for the four bilateral structures, every real value for the two indefinite sesquilinear structures, every non-negative real value for the two definite sesquilinear structures, and $0$ alone for the four brackets.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathrm{GPA}$, $\mathrm{GPS}$, $\mathrm{GQA}$, $\mathrm{GQS}$ | the four general parents: composition, probability, causality, gauge |
| $\mathrm{SPA}$, $\mathrm{SPS}$, $\mathrm{SQA}$, $\mathrm{SQS}$ | their symmetric parts: commutativity, positivity, coupling, metric |
| $\mathrm{APA}$, $\mathrm{APS}$, $\mathrm{AQA}$, $\mathrm{AQS}$ | their antisymmetric parts: rotation, phase, obstruction, polarisation |
| $S(x,y)$, $A(x,y)$ | the symmetric and antisymmetric parts of a product |
| $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{*}$, $\langle\cdot,\cdot\rangle_{\natural}$, $\langle\cdot,\cdot\rangle_{\natural*}$ | the plain, Hermitian, quaternion and Krein forms |
| $\mathcal{C}$ | the zero-divisor cone $\{\langle\tilde Q\rangle_{\natural}=0\}$ |
| $\mathbb{B}^{\times}$ | the unit group of the plain product, $\{\langle\tilde Q\rangle_{\natural}\neq0\}$ |
| $\tilde\Pi$, $\tilde\Upsilon$ | an idempotent and a nilpotent |
| $\mathbb{C}_{\mathbb{B}}$ | the centre $\mathbb{C}e_t$, the classical sector |
| the vector subspace | the values of the four brackets |

## Further Reading

- [The 12 Products of the Biquaternion $\mathbb{C}$ Space](../articles_maths/the-12-products-of-the-biquaternion-complex-space.html), for the multiplication tables and the coordinates of the twelve.
- [The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](../articles_maths/the-algebraic-structures-over-the-biquaternion-c-space.html), for the twelve products, the identities and the witnesses.
- [The Realification of the Eight Derived Structures](../articles_maths/the-realification-of-the-eight-derived-structures.html), for the real dimension, the real operators and the signatures.
- [The 4 Forms over the Biquaternion $\mathbb{C}$ Space](../articles_maths/the-4-forms-over-the-biquaternion-c-space.html), for the four forms and their Gram matrices.
- [The Four General Products: Composition, Probability, Causality, Gauge](the-four-general-products-composition-probability-causality-gauge.html), for the four parents read one by one.
- [The Four Forms and the Four Algebraic Norms](the-four-forms-and-the-four-algebraic-norms.html), for the forms and the norms read physically.
- [Roots, Idempotents and Observables](roots-idempotents-and-observables.html), [The Zero-Divisor Cone and the Massless Spectrum](the-zero-divisor-cone-and-the-massless-spectrum.html) and [The Roots of a General Element: Mass, Frames and the Mass Shell](the-roots-of-a-general-element-mass-frames-and-the-mass-shell.html), for the three named values read on their own.
