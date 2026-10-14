# __The General Plain Bilinear Product on the Informational Sector__

## Introduction

The informational sector $\mathbb{M}_+$ is the Hermitian half of the algebra: the observables, the
states, the boosts and the identity. An element is written in its own coordinates as

$$
\tilde Q = q_0\,e_0 + i\vec q', \qquad q_0 = c t' \in \mathbb{R},\quad
\vec q' = (x',y',z') \in \mathbb{R}^{3},
$$

a **real** scalar part and three **imaginary** vector parts. This article reads the restriction to that
sector of the one product by which informational operations compose — the **general plain bilinear
product** $(\mathrm{GPA})$, written $\tilde P\tilde Q$, the multiplication of the algebra itself — and asks
what its scalar part measures there. It is the informational companion of *The General Plain Bilinear Product on the
Material Sector*; the product on the whole algebra is *The General Plain Bilinear Product on the Biquaternion Space*,
and the sector itself, its coordinate dictionary and its operator identification are *The Hermitian
Subspace $\mathbb{M}_+$ as the Informational Sector*.

The answer is the mirror of the material one. The scalar part

$$
B(\tilde P,\tilde Q) = \mathrm{Sc}(\tilde P\tilde Q) = p_0q_0 + \vec p'\!\cdot\!\vec q'
$$

is **positive definite** on the sector, of signature $(4,0)$: in the informational coordinates it is the
plain Euclidean inner product, and it is the same form whose restriction to $\mathbb{M}_-$ is negative
definite, signature $(0,4)$. It is the **sector sign**, and here it is positive. The composite of two
informational operations is informational exactly when the two **commute**, informational in its
order-independent half always, and material in its order-dependent half; the **square** of an element of
**either** sector is informational, so $\mathbb{M}_+$ is the sector that receives the squares. The
nonzero idempotents of the algebra lie in $\mathbb{M}_+$ alone, and they lie **on the zero-divisor cone**
— so on this side of the algebra the cone is not a mass shell but the **purity boundary of the state
space**, the set of the pure states.

**Placement and boundaries.** This article is the informational-sector companion of *The General Plain Bilinear Product
on the Biquaternion Space*, in the band *Focus on the General Plain Algebra (GPA) of Biquaternions —
Composition*, and the second of the two sector companions, the first being *The General Plain Bilinear Product on the
Material Sector*. Here the same product is read on $\mathbb{M}_+$ alone: the sector sign on the
informational side, the sector structure of an informational composite, the square as a map into the
sector, the idempotents and the purity boundary, and the units of the sector. The symmetrised product and
the Jordan identity are *The Symmetrised Material Composition and the Jordan Identity* and *Observables
as a Jordan Algebra: the Symmetric Plain Product and the Classical Composition*; the invertibility
criterion, the group of units and the cone are the mathematics of *The Group of Units of the General Plain
Algebra and the Complement of the Zero-Divisor Cone* and the level data of *Norm and Invertibility in the General Quaternionic Algebra*; the idempotents and the Peirce decomposition are *Idempotents of the General Plain
Algebra* and *Ideals and Peirce Decomposition of the General Plain Algebra*; the operators and the
sandwich are *The Operators of the General Plain Bilinear Product: One-Sided, Two-Sided and the Sandwich*; the exchange
of the two sectors is *Each Sector Is the Other's Clock: the Sector Exchange as Relational Time* and the
maps between them *Cross-Sector Coupling in the Biquaternion Framework: a Catalogue of the Maps Between
the Sectors*. None of those is reproved here.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis
$e_0=1,e_1,e_2,e_3$ with $e_1e_2=e_3$, $e_k^{2}=-e_0$, and central scalar imaginary $i$, $i^{2}=-1$; a
general element is $\tilde Q=Q_0e_0+Q_1e_1+Q_2e_2+Q_3e_3$ with complex coefficients; the scalar part is
$\mathrm{Sc}(\tilde Q)=Q_0$ and the vector part is $\vec Q=Q_1e_1+Q_2e_2+Q_3e_3$. The conjugations are
the complex conjugation $\bar{\cdot}$, the natural (quaternion) conjugation ${\natural}$, and the
Hermitian conjugation ${}^{*}=\bar{\cdot}\circ{\natural}$. The informational sector is the Hermitian half,
$\mathbb{M}_+=\{\tilde Q:\tilde Q^{*}=+\tilde Q\}$, with the real basis $\{e_0,ie_1,ie_2,ie_3\}$; the
material sector is the anti-Hermitian half, $\mathbb{M}_-=\{\tilde Q:\tilde Q^{*}=-\tilde Q\}$, with the
real basis $\{ie_0,e_1,e_2,e_3\}$, and the two are exchanged by the central $i$, $i\mathbb{M}_+=\mathbb{M}_-$.
The identity is $e_0\in\mathbb{M}_+$, the trace is $\mathrm{Tr}=2\,\mathrm{Sc}$, and the zero-divisor cone
of the general plain bilinear product is $\mathcal{C}=\{N(\tilde Q)=0\}$ with
$N(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)$.

## The Informational Sector and Its Coordinates

An informational element is written in the two dictionaries of the sector,

$$
\tilde Q = q_0\,e_0 + i\vec q' = (ct')\,e_0 + i x'\,e_1 + i y'\,e_2 + i z'\,e_3 \in \mathbb{M}_+,
\qquad c \ \text{the speed of light}.
$$

The real scalar and the imaginary vector are the mark of the sector: an informational element is fixed by
the Hermitian conjugation, $\tilde Q^{*}=+\tilde Q$, so the scalar coefficient is real and the three
vector coefficients are imaginary. The sector is the home of the Hermitian operators on the spinor
module, of the observables, of the states and of the boosts, and its own physics is owned by *The
Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*.

Two forms carry the geometry of the sector, and they are the restrictions of the two forms of the plain
row:

$$
B(\tilde P,\tilde Q)=p_0q_0+\vec p'\!\cdot\!\vec q' \quad\text{of signature }(4,0),
\qquad
N(\tilde P,\tilde Q)=p_0q_0-\vec p'\!\cdot\!\vec q' \quad\text{of signature }(1,3).
$$

The first is the **sector sign** of this article, the scalar part of the general plain bilinear product, definite and
without cone; the second is the **interval**, the general quaternionic bilinear form, indefinite, whose
zero set is the zero-divisor cone. The two differ by twice the coefficient square of the vector part,

$$
B(\tilde P,\tilde Q) = N(\tilde P,\tilde Q) - 2\,\vec Q\!\cdot\!\vec Q,
\qquad \vec Q\!\cdot\!\vec Q = Q_1^{2}+Q_2^{2}+Q_3^{2},
$$

which on the sector is $-2|\vec q'|^{2}$ and therefore of one sign; the two forms agree only on the
scalar line. Keeping $B$ and $N$ apart is the whole of the article: $B$ carries the sign of the sector
and $N$ carries the metric, and on $\mathbb{M}_+$ the sign is positive and the metric is Lorentzian.

## The Product of Two Informational Operations

The general plain bilinear product $\tilde P\tilde Q$ is the multiplication of the algebra. The informational sector is
not closed under it, and the way it fails is the mirror of the material failure. The Hermitian
conjugation is an anti-automorphism, $(\tilde P\tilde Q)^{*}=\tilde Q^{*}\tilde P^{*}$, so for two
informational operations it returns the reversed product,

$$
(\tilde P\tilde Q)^{*} = \tilde Q^{*}\tilde P^{*} = \tilde Q\tilde P,
$$

and the composite therefore splits into its Hermitian and anti-Hermitian parts,

$$
\tilde P\tilde Q
= \underbrace{\tfrac12\bigl(\tilde P\tilde Q+\tilde Q\tilde P\bigr)}_{\text{anticommutator, in }\mathbb{M}_+}
+ \underbrace{\tfrac12\bigl(\tilde P\tilde Q-\tilde Q\tilde P\bigr)}_{\text{commutator, in }\mathbb{M}_-}.
$$

The sector is therefore not closed under composition, and which half survives is decided by which
relation holds: the composite is **informational exactly when the two commute**, $[\tilde P,\tilde Q]=0$,
so that the material half vanishes, and **material exactly when the two anticommute**,
$\{\tilde P,\tilde Q\}=0$, so that the informational half vanishes. A generic pair of informational
operations composes to an element with one part in each sector: the informational part is the
order-independent half $\tfrac12\{\tilde P,\tilde Q\}$, and the order dependence is carried by the
material half $\tfrac12[\tilde P,\tilde Q]$, which changes sign when the two operations are exchanged.
The rule is the same as on $\mathbb{M}_-$: for two elements of **one** sector the anticommutator stays in
that sector and the commutator leaves it, and it is only the sign form that differs.

**Remark (verified).** For $100$ random pairs of Hermitian elements the anticommutator is fixed by the
dagger and the commutator anti-fixed, to machine precision, and the two halves sum to the composite; the
composite is informational in exactly the pairs that commute ($2$ of $100$ random integer pairs, the rest
falling outside the sector).

**Proposed interpretation, labelled as such.** On the informational sector the **order-dependent half is
the half that leaves**: the commutator is material and the anticommutator informational, so
**the commutative part of a composite of two observational operations is an informational operation and
its order dependence is a material one**. The sector is a **special Jordan algebra** under the
symmetrised product, which is the algebraic content of *Observables as a Jordan Algebra: the Symmetric
Plain Product and the Classical Composition*, and the commutator that leaves the sector is the
generator of the internal action, which is *Observables, Gauge Generators and the Chirality of the
Internal Action*.

## The Scalar Part Is the Sector Sign on the Informational Side

The form $B$ is positive on an informational **element** and negative on a material one, that is at the
two equal arguments, and that is the fact this article is built on. On the informational basis
$\{e_0,ie_1,ie_2,ie_3\}$ the diagonal entries are $B(e_0,e_0)=+1$ and $B(ie_k,ie_k)=+1$ with all cross
terms zero, so

$$
B\big|_{\mathbb{M}_+} = +\mathrm{I}_4 \ \text{ of signature }(4,0),
\qquad
B\big|_{\mathbb{M}_-} = -\mathrm{I}_4 \ \text{ of signature }(0,4).
$$

The pair of signs is the **sector sign**: $B$ says which sector an element belongs to, and it says it by
the sign of a number and nothing else. On the informational coordinates the same statement is that $B$ is
the **Euclidean inner product** of the informational coordinate, whereas the interval is Lorentzian in the
same coordinate. The informational sector therefore carries **two metrics of opposite type on the same
four directions**: a Riemannian one, the sector sign, and a Lorentzian one, the interval. The first is
what the general plain bilinear product measures; the second is the metric, and it belongs to the companion
quaternionic block and to *Norm and Invertibility in the General Quaternionic Algebra*, and it is cited here, never re-proved.

**Remark (verified).** On the sector bases $B$ restricts to $\pm\mathrm{I}_4$ with all cross terms $0$;
$B(\tilde Q,\tilde Q)$ is real and strictly positive on $100$ random $\mathbb{M}_+$ elements and real and
strictly negative on $100$ random $\mathbb{M}_-$ elements.

**Proposed interpretation, labelled as such.** Read on the informational coordinate, $B$ is the
**length-squared of an informational configuration**: a positive-definite quantity, additive over
orthogonal directions, and the natural norm of the sector's own space. The interval on the same
directions is indefinite, so the sector carries a definite geometry and an indefinite one at once, and
which one a process sees depends on the product it uses. The positive definite one is the geometry of the
probability and the indefinite one the geometry of the metric; the two are the same four directions read
twice, and the difference between them is the coefficient square of the vector part, $B-N=2|\vec q'|^{2}$.

## The Square: the Sector that Receives

The composite of two informational operations need not be informational, but the **square** always is,
and the square of a **material** element lands here too:

$$
\tilde Q^{2} = \bigl(q_0^{2}+\lvert\vec q'\rvert^{2}\bigr)e_0 + 2iq_0\vec q' \in \mathbb{M}_+
\quad\text{for every } \tilde Q\in\mathbb{M}_+,
\qquad
\tilde Q^{2}\in\mathbb{M}_+ \quad\text{for every } \tilde Q\in\mathbb{M}_-.
$$

The reason is that the two factors of a square are equal and the cross product of a vector with itself
vanishes, so the antisymmetric part of the composite — the part that would leave the sector — is
absent. A square can therefore never witness the failure of closure, and the informational sector is
**closed under squaring** while the material sector is not: the square is a map
$\mathbb{M}_+\to\mathbb{M}_+$ that extends to $\mathbb{M}_-\to\mathbb{M}_+$ and has no value in
$\mathbb{M}_-$ on a nonzero element of either sector. The scalar part of the square is the sector sign,
$\mathrm{Sc}(\tilde Q^{2})=B(\tilde Q,\tilde Q)$, real and of the sign of the sector: positive on
$\mathbb{M}_+$, negative on $\mathbb{M}_-$.

**Remark (verified).** For $100$ random elements of each sector the square is Hermitian; the scalar part
of the square coincides with $B(\tilde Q,\tilde Q)$ to machine precision and is of the sector's sign on
all of them, positive definite on $\mathbb{M}_+$ and negative definite on $\mathbb{M}_-$.

**Proposed interpretation, labelled as such.** The square is the **passage from displacement to
operator**: the square of a material four-vector is an informational element and never a four-vector
again, so composing an operation with itself is not composing two operations but acting on a state. The
squaring of an informational element stays informational, so an observational operation can be iterated
without leaving its sector, which is why the iterations of a measurement are read inside $\mathbb{M}_+$
and the iterations of a displacement are not.

## The Idempotents, the States and the Purity Boundary

The nonzero idempotents of the algebra lie in the informational sector alone. If $\tilde\Pi^{2}=\tilde\Pi$
and $\tilde\Pi\in\mathbb{M}_-$, then $\tilde\Pi^{*}=-\tilde\Pi$ and applying the anti-automorphism to the
idempotent equation gives $-\tilde\Pi=(\tilde\Pi^{*})^{2}=(-\tilde\Pi)^{2}=\tilde\Pi^{2}=\tilde\Pi$,
whence $\tilde\Pi=0$. Every nonzero projection is therefore Hermitian, and the family is

$$
\tilde\Pi_1(\hat u) = \tfrac12\bigl(e_0+i\hat u\bigr),
\qquad
\hat u\in\mathbb{R}^{3},\quad \lvert\hat u\rvert=1,
$$

the **pure states** of the corpus, indexed by the unit sphere and forming the Bloch sphere. The material
sector owns no projection, so the reference state of a material field comes from here — a **state** and
not a material background, which is the companion article's reading and is not repeated. The family is the
corpus's idempotent set (*Idempotents in the 12 Structures of Biquaternions over $\mathbb{C}$*), and its
parametrisation is the corpus's bijection between the roots of $-e_0$ and the states: a pure state is a pure
root of $+e_0$, built from a root of $-e_0$ by the central $i$ (*Square Roots of Minus One, Zero and Plus
One in the 12 Structures of Biquaternions over $\mathbb{C}$*).

The idempotent sits **on the zero-divisor cone**. Its interval vanishes,

$$
N(\tilde\Pi,\tilde\Pi) = \tfrac14\bigl(1-\lvert\hat u\rvert^{2}\bigr) = 0,
$$

so a pure state is a zero divisor of the general plain bilinear product: it is not invertible, it is annihilated by a
nonzero element, and the algebra's other projection at the antipodal direction completes it. The cone
therefore cuts the informational sector, and on the unit-trace slice the cut is exactly the boundary of the
state space: the Bloch ball is the trace-one slice of the future cone and its boundary is the sphere of the
pure states (*The Cone and the Massless Particles in the 12 Structures of Biquaternions over $\mathbb{C}$*
and *The Bloch Ball as the Trace-One Slice of the Future Light Cone*). Inside the sector the cone has two
faces: a cone element with $q_0\neq0$ is a multiple of a pure state,
$\tilde Q=2q_0\tilde\Pi_1(\vec q'/q_0)$, whereas the **nilpotents**, the pure isotropic elements of real
dimension four, meet $\mathbb{M}_+$ at the origin alone, the square of an informational element having
strictly positive scalar part (*Nilpotents in the 12 Structures of Biquaternions over $\mathbb{C}$*). For
the general element of the unit-trace slice,

$$
\tilde\rho = \tfrac12\bigl(e_0+i\vec r\bigr),\qquad \lvert\vec r\rvert\le 1,
$$

the two forms read the Bloch vector as

$$
N(\tilde\rho,\tilde\rho) = \tfrac14\bigl(1-\lvert\vec r\rvert^{2}\bigr),
\qquad
B(\tilde\rho,\tilde\rho) = \tfrac14\bigl(1+\lvert\vec r\rvert^{2}\bigr),
\qquad
\mathrm{Tr}(\tilde\rho^{2}) = \tfrac12\bigl(1+\lvert\vec r\rvert^{2}\bigr),
$$

so the **cone of the norm is the purity boundary of the Bloch ball**: a state is pure exactly when
$\lvert\vec r\rvert=1$, exactly when $N=0$, exactly when it is a zero divisor; a mixed state is
interior, $N>0$, and is a unit. The purity is carried by the difference of the two forms,
$B-N=\lvert\vec r\rvert^{2}/2$ on the slice: **a state is pure when the two forms are furthest apart**,
$B-N=\frac12$, and maximally mixed when they coincide, $B-N=0$.

**Remark (verified).** $N=\frac14(1-\lvert\vec r\rvert^{2})$ and $B=\frac14(1+\lvert\vec r\rvert^{2})$
on $100$ random unit-trace elements; the Hermitian idempotents satisfy $N=0$ and $B=\frac12$ to machine
precision, and $\mathrm{Tr}(\tilde\rho^{2})$ equals $\frac12(1+\lvert\vec r\rvert^{2})$.

**Proposed interpretation, labelled as such.** The same algebraic cone has **two physical roles on the
two sides of the algebra**: on $\mathbb{M}_-$ it is the **light cone**, the wall of the massless and the
boundary of the reversible four-vectors, and on $\mathbb{M}_+$ it is the **purity boundary**, the locus
of the pure states and the boundary of the invertible states of the state space. The object is one and
the readings are two, because the same norm is the interval on one side and the purity on the other. A
pure state is the informational analogue of a lightlike displacement: both are elements of vanishing
norm, both are non-invertible, and neither propagates a proper time of its own.

## The Units and the Cone on the Informational Sector

The invertibility of the general plain bilinear product is decided by the norm and not by the sector sign: an element
is a **unit** exactly when $N(\tilde Q)\neq0$, its inverse is $\tilde Q^{\natural}/N(\tilde Q)$, and the
zero-divisor cone is the complement of the group of units. On the informational sector the criterion is
the interval in the informational coordinate,

$$
N(\tilde Q)=q_0^{2}-\lvert\vec q'\rvert^{2}\neq 0,
$$

so the units of the sector are the off-cone informational elements, the two open families
$q_0^{2}>\lvert\vec q'\rvert^{2}$ and $q_0^{2}<\lvert\vec q'\rvert^{2}$, and the cone is the wall
between them and around them. The identity $e_0$ is a unit; so is every mixed state; no pure state is.

**Proposed interpretation, labelled as such.** On the informational side the cone separates the
**reversible informational operations** from the irreversible ones, exactly as on the material side it
separates the reversible displacements from the lightlike ones. The identification of a state with a
reversible operation is the mixed-state side of the corpus's state theory, and the boundary between the
two is the same cone as the mass shell's wall, read in the informational coordinate. The two sectors
share the cone and not its name.

## A Worked Case

Take two informational elements, one off the cone and one on it,

$$
\tilde P = 3e_0+ie_1\in\mathbb{M}_+,
\qquad
\tilde Q = e_0+ie_2\in\mathbb{M}_+\cap\mathcal{C}.
$$

The two scalar forms and the norm give

$$
B(\tilde P,\tilde P)=+10,\quad B(\tilde Q,\tilde Q)=+2,\quad
B(\tilde P,\tilde Q)=+3,\quad N(\tilde P,\tilde P)=+8,\quad N(\tilde Q,\tilde Q)=0,
$$

so $\tilde P$ is a unit of the sector and $\tilde Q$ is a zero divisor on the cone. The squares are

$$
\tilde P^{2}=10e_0+6ie_1\in\mathbb{M}_+,
\qquad
\tilde Q^{2}=2\tilde Q\in\mathbb{M}_+,
$$

both informational, with the scalar parts $+10$ and $+2$ equal to the sector sign; the element $\tilde Q$
is a zero divisor that is not idempotent, $q^{2}=2q$, and the difference between a projection and a
lightlike displacement is visible in the same computation. The product of the two is neither
informational nor material,

$$
\tilde P\tilde Q=3e_0+ie_1+3ie_2-e_3,
$$

whose scalar part is $B(\tilde P,\tilde Q)=+3$ and whose vector part carries both an imaginary and a real
piece, the real piece $-e_3$ being the order dependence. The pair does not commute, and the split of the
composite displays the rule:

$$
\tfrac12\{\tilde P,\tilde Q\}=3e_0+ie_1+3ie_2\in\mathbb{M}_+,
\qquad
\tfrac12[\tilde P,\tilde Q]=-e_3\in\mathbb{M}_-,
\qquad
\mathrm{Tr}(\tilde P\tilde Q)=6.
$$

Read row by row, the case displays the whole sector at once. The sector sign is positive on both elements
and distinguishes them from material ones by that sign alone. The interval vanishes on the pure direction
and not on the other, so the cone is inside the sector and it is the purity boundary. The square stays,
the product does not, and the order dependence is the material half. And the trace gives the scalar part
of the composite doubled, the algebraic form of an expectation value.

## The Bound

The article states the restriction to the informational sector of the product and its scalar form, and the
boundary of what it must declare is the boundary of the sector.

- **$B$ is not the metric.** It is definite on each sector and has no cone there, so it cannot define the
  causal structure. The metric is the interval, of signature $(1,3)$ on $\mathbb{M}_+$.
- **$B$ is not the interval.** The interval, the mass shell, the four-velocity and invertibility are the
  level data of the general quaternionic bilinear form, owned by *The Interval as the Square and the Charge of the Material Composition*;
  the worked case shows the two forms giving different numbers on the same element.
- **The informational sector is not closed under the product.** A composite of two informational
  elements is informational exactly when the two commute and material exactly when they anticommute; the
  sector is not an algebra, and the anticommutator is the Jordan product of *The Symmetrised Material
  Composition and the Jordan Identity*, not the product itself.
- **The square is not the product.** A square of an element of either sector is informational, so the
  closure of the sector under squaring is not a closure under composition and must not be read as one.
- **The reverse map is not read here.** The square of an element of either sector lands in $\mathbb{M}_+$;
  the roots of a given element are classified by *Square Roots of a General Element in the 12 Structures of
  Biquaternions over $\mathbb{C}$* and are not read here.
- **The cone is not a mass shell here.** The same cone that carries the mass shell on $\mathbb{M}_-$ is
  the purity boundary of the state space on $\mathbb{M}_+$, and the identification of a state with a
  lightlike direction is a reading of the norm and not an identification of the two sectors.

**What the framework does not claim.** The interpretation does not say which physical operation an
informational element represents, does not derive the measurement update from the general plain bilinear product, and
does not claim that every informational process is a composition. The Lorentz action is the sandwich of
*The General Plain Bilinear Product on the Biquaternion Space*, and the measurement update is an idempotent projection;
neither is re-derived here.

## The Ledger

**Proved.** The informational sector is fixed by the dagger, hence $B$ restricts to $+\mathrm{I}_4$ of
signature $(4,0)$ on $\mathbb{M}_+$ and to $-\mathrm{I}_4$ of signature $(0,4)$ on $\mathbb{M}_-$; the
product of two informational elements splits into an informational anticommutator and a material
commutator and is informational exactly when the two commute; the square of an element of either sector
is informational, with scalar part equal to the sector sign; the sector contains the nonzero idempotents
of the algebra and they form the unit sphere $\tilde\Pi_1(\hat u)$, all of them on the
zero-divisor cone; on the unit-trace slice the interval is $\frac14(1-\lvert\vec r\rvert^{2})$ and the
sector sign $\frac14(1+\lvert\vec r\rvert^{2})$, so the cone is the purity boundary and the mixed
states are the interior units; the inverse of an informational unit is informational, and the norm
restricts to a homomorphism $\mathbb{B}^{\times}\to\mathbb{C}^{\times}$.

**Interpretations.** That $B$ carries the **sector sign**, positive on the informational side; that the
informational sector carries a **Riemannian** geometry (the sector sign) and a **Lorentzian** one (the
interval) on the same directions; that the general plain bilinear product is the **composition of informational
operations** and is closed on the commutative pairs alone; that the order-dependent half of a composite
of two observables is the **material generator**; that the square is the **passage from displacement to
state**; that the nonzero projections are informational and their family is the Bloch sphere; that the
cone of the norm is at once the **light cone** of the material side and the **purity boundary** of the
informational side; and that a mixed state is a reversible informational operation while a pure state is
not. Each is the framework's naming of a proved algebraic fact and is labelled as such.

## Physical Readings

The general plain bilinear product reads as the process on the informational sector, and the article's own
interpretation is the composition of two observational operations. Three further readings follow from
the sector's place in the algebra. The matrix side of the sector is the Hermitian matrices, so the
product of two Hermitian matrices is Hermitian exactly when they commute, and the trace formula
$\mathrm{Tr}(\tilde\rho\tilde Q)=2\,\mathrm{Sc}(\tilde\rho\tilde Q)$ is the algebraic form of the
expectation value of an observable in a state. The sector is the receiving end of the square, so every
displacement's square is an operation and the map from the physical four-vectors to the operators is the
square. And the cone, read on the state space, is the boundary of purity: the pure states are the
zero divisors, so **the states the product cannot invert are exactly the states that carry no mixing**,
and a non-invertible informational element is a maximal-information one rather than a degenerate one — the
opposite of the material reading of the same cone. The two sectors remain the two readings of one algebra,
exchanged by the central imaginary and paired as each other's clock (*Each Sector Is the Other's Clock:
the Sector Exchange as Relational Time*), and the product is the one operation they do not share.

## Summary

The informational sector $\mathbb{M}_+$ carries the Hermitian elements, an element being
$\tilde Q=(ct')e_0+i\vec x'$, and this article reads on it the general plain bilinear product $\tilde P\tilde Q$ whose
full theory on the whole algebra is *The General Plain Bilinear Product on the Biquaternion Space*. Its scalar part
$B=p_0q_0+\vec p'\!\cdot\!\vec q'$, the Euclidean inner product of the informational coordinates, is
positive definite on $\mathbb{M}_+$ with signature $(4,0)$ and negative definite on $\mathbb{M}_-$ with
signature $(0,4)$: opposite definite signs on the two sectors, so $B$ carries the **sector sign**. Being
definite, $B$ has no cone and cannot be the metric; the metric is the interval, the general quaternionic
bilinear form, of signature $(1,3)$ on the informational sector, and the two differ by twice the
coefficient square of the vector part. The composition of two informational operations is informational
exactly when the two commute, its material part being the commutator and its order-independent part the
anticommutator; the square of an element of either sector is informational, so the sector receives the
squares and is closed under squaring without being closed under the product. The nonzero idempotents of
the algebra lie in $\mathbb{M}_+$ alone, they form the Bloch sphere of the pure states, and they lie on
the zero-divisor cone; on the unit-trace slice the interval is $\frac14(1-\lvert\vec r\rvert^{2})$ and
the sector sign $\frac14(1+\lvert\vec r\rvert^{2})$, so on this side of the algebra the cone is the
**purity boundary of the state space**: pure states are the zero divisors, mixed states the interior
units, and the purity is the difference of the two metrics. The reversibility of the general plain bilinear product is
carried by the norm $N$ and not by $B$. The distinctions are labelled throughout: what is proved is the
algebra restricted to $\mathbb{M}_+$, what is proposed is the naming.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | The biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^{2}=-e_0$, $e_1e_2=e_3$ |
| $i$ | Central scalar imaginary, $i^{2}=-1$ |
| $\bar{\cdot},{\natural},{}^{*}=\bar{\cdot}\circ{\natural}$ | Complex, natural and Hermitian conjugations |
| $\mathbb{M}_+=\{\tilde Q:\tilde Q^{*}=+\tilde Q\}$ | Informational sector, basis $\{e_0,ie_1,ie_2,ie_3\}$ |
| $\mathbb{M}_-=\{\tilde Q:\tilde Q^{*}=-\tilde Q\}$ | Material sector, basis $\{ie_0,e_1,e_2,e_3\}$ |
| $\tilde Q=q_0e_0+i\vec q'=(ct')e_0+i\vec x'$ | An informational element; real time, imaginary space |
| $\tilde P\tilde Q$ | General plain bilinear product ($\mathrm{GPA}$); associative, unital, non-commutative |
| $B(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q)=p_0q_0+\vec p'\!\cdot\!\vec q'$ | Sector sign; $+\mathrm{I}_4$ on $\mathbb{M}_+$, $-\mathrm{I}_4$ on $\mathbb{M}_-$ |
| $N(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)$ | Interval; $(1,3)$ on $\mathbb{M}_+$, $(3,1)$ on $\mathbb{M}_-$ |
| $B-N=2\,\vec Q\!\cdot\!\vec Q$ | The two forms differ by twice the coefficient square |
| $\tfrac12(\tilde P\tilde Q\pm\tilde Q\tilde P)$ | Anticommutator in $\mathbb{M}_+$; commutator in $\mathbb{M}_-$ |
| $\tilde Q^{2}\in\mathbb{M}_+$ | The square is informational for an element of either sector |
| $\tilde\Pi_1(\hat u)=\tfrac12(e_0+i\hat u)$ | The nonzero idempotents; the Bloch sphere; on the cone |
| $\tilde\rho=\tfrac12(e_0+i\vec r)$, $\lvert\vec r\rvert\le1$ | Unit-trace element; the Bloch ball |
| $N(\tilde\rho,\tilde\rho)=\frac14(1-\lvert\vec r\rvert^{2})$ | The cone as the purity boundary |
| $\mathbb{B}^{\times}=\{N\neq0\}$, $\mathcal{C}=\{N=0\}$ | Group of units; zero-divisor cone |
| $\mathrm{Tr}=2\,\mathrm{Sc}$ | Trace; $\mathrm{Tr}(\tilde\rho\tilde Q)$ an expectation value |
| $(p,q)$ | Signature as (number of $+$, number of $-$) diagonal entries |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the quaternion algebra, its
  scalar part and its relation to $M_2(\mathbb{C})$.
- F. Reese Harvey, *Spinors and Calibrations* (Academic Press, 1990), for the complex and real structures
  on the biquaternion algebra and the sectors of the Hermitian conjugation.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge,
  2000), for the state space, the Bloch ball and the purity of a state.
- Claude Itzykson and Jean-Bernard Zuber, *Quantum Field Theory* (McGraw–Hill, 1980), for the role of
  the indefinite metric and its separation from the positive probability form.
- Companion article *The General Plain Bilinear Product on the Biquaternion Space*, for the product and the form $B$ on
  the whole algebra and the restriction table over the remarkable subspaces.
- Companion article *The General Plain Bilinear Product on the Material Sector*, for the mirror reading on
  $\mathbb{M}_-$.
- Companion article *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, for the sector,
  its coordinate dictionary and its operator identification.
- Companion article *Observables as a Jordan Algebra: the Symmetric Plain Product and the Classical
  Composition*, for the symmetrised product and the closure of the observables.
- Mathematics article *The Group of Units of the General Plain Algebra and the Complement of the
  Zero-Divisor Cone*
  (`articles_maths/the-group-of-units-of-the-general-plain-algebra-and-the-complement-of-the-zero-divisor-cone.md`),
  for the group of units, the multiplicativity of the norm and the cone as the boundary of invertibility.
- Mathematics article *Idempotents of the General Plain Algebra*
  (`articles_maths/idempotents-of-the-general-plain-algebra.md`), for the classification of the
  idempotents and the projections.
- Companion article *Zero Divisors in the 12 Structures of Biquaternions over $\mathbb{C}$*, for the cone
  as the zero-divisor set of the composition band.
- Companion article *Annihilators in the 12 Structures of Biquaternions over $\mathbb{C}$*, for the
  annihilator planes of a lightlike element and the line they share.
- Companion article *Composition and Probability: the General Plain Algebra and the General Plain
  Sesqualgebra of Biquaternions Compared*, for the twelve structures read side by side.
