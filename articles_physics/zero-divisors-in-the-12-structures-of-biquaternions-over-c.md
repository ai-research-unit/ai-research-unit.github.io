# __Zero Divisors in the 12 Structures of Biquaternions over $\mathbb{C}$__

## Introduction

The comparison section of the physics menu mirrors the comparison group of the mathematics menu: the twelve
structures of the biquaternion complex space read against one subject at a time. The mathematics group opens
with *Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, and this article is its physics companion. The subject is the set of elements that a
product cannot invert, and the physical question is what that set means in each of the twelve structures.

A **zero divisor** of a product is a nonzero element $\tilde Q$ that annihilates some nonzero element: there
is a nonzero $\tilde X$ with $\tilde Q\cdot\tilde X=0$ (a left zero divisor), or with
$\tilde X\cdot\tilde Q=0$ (a right zero divisor). An element is a zero divisor exactly when it has no inverse
in the product. Physically, a zero divisor is an operation that sends a nonzero object to zero: it is not
invertible, nothing can undo it, and it marks a direction in which composition degenerates.

The mathematics companion proves one theorem about the twelve structures, and the theorem is the spine of
this article. Among the twelve structures the zero-divisor set is the **punctured cone**
$\mathcal{C}\setminus\{0\}$, the nonzero elements of vanishing biquaternion norm, exactly for the four
general products $\mathrm{GPA}$, $\mathrm{GQA}$, $\mathrm{GPS}$ and $\mathrm{GQS}$; the two symmetric
structures $\mathrm{SPA}$ and $\mathrm{SQS}$ have the enlarged set $(\{Q_0=0\}\cup\mathcal{C})\setminus\{0\}$;
and the remaining six structures have the whole punctured space $\mathbb{B}\setminus\{0\}$. The cone is
therefore contained in all twelve sets and equals only four of them, and the physical reading of the theorem
is the subject of this article: the four general products degenerate exactly on the light cone, the two
symmetric products of Jordan type degenerate on the lightlike family as well, and the six derived products
are not compositional operations at all, because every nonzero element fails to be invertible in them.

The article reads the theorem structure by structure. It first fixes what a zero divisor is as an operation,
then reads the cone in the algebra and in spacetime, then tabulates the twelve sets with their physical
readings, then separates the common core from the enlarged and the total sets. The other five articles of
the section take up the objects that the zero-divisor set organises: *Annihilators in the 12 Structures
of Biquaternions over $\mathbb{C}$* the annihilator planes, *Square Roots of Minus One, Zero and Plus One in the 12 Structures
of Biquaternions over $\mathbb{C}$* the roots of $0$, *Square Roots of a General Element in the 12 Structures of Biquaternions over $\mathbb{C}$* the general
radicand, *Idempotents in the 12 Structures of Biquaternions over $\mathbb{C}$* the non-pure family, and *Nilpotents in the 12
Structures of Biquaternions over $\mathbb{C}$* the square-zero class. A closing part, §*The Zero-Divisor Set Beyond the Twelve*, gathers six
properties of the set that name no product.

**Conventions.** We use those of the companion articles unchanged. The biquaternion algebra is
$\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$, $e_k^{2}=-e_0$ and
$e_je_k=-\delta_{jk}e_0+\varepsilon_{jkl}e_l$, and $i$ the central scalar imaginary. The conjugations are
the natural conjugation ${}^{\natural}$, the coefficient conjugation $\bar{\cdot}$ and the Hermitian
conjugation ${}^{*}=\bar{\cdot}\circ{}^{\natural}$, with $\tilde Q^{\flat}=-\tilde Q^{*}$. The biquaternion
norm is $N(\tilde Q)=\langle\tilde Q,\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}=\sum_\mu Q_\mu^{2}$,
whose vanishing locus is the cone; the subspaces are the anti-Hermitian material sector $\mathbb{M}_-$ and
the Hermitian informational sector $\mathbb{M}_+$; the material coordinate is $\tilde Q=ict\,e_0+\mathbf x$,
so that $N(\tilde Q)=-c^{2}t^{2}+\mathbf x^{2}$, and $c=1/\sqrt{\epsilon\mu}$. An element is **pure** when
its scalar part vanishes, $Q_0=0$, and **non-pure** when $Q_0\neq0$. The plain product is written
$\tilde P\tilde Q$ and the plain sesquilinear product $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$; the
trace is $\mathrm{Tr}=2\,\mathrm{Sc}$. The twelve structures are those of *The 12 Products of the
Biquaternion Complex Space* and *The Twelve Structures Compared: Product, Law and Form*, and they are cited
throughout by their three-letter names.

## The Zero Divisor as an Operation That Cannot Be Inverted

**The algebra.** In a finite-dimensional associative algebra with a two-sided unit, an element is
invertible if some element multiplies it to the unit on both sides, and a nonzero element that is not
invertible is a zero divisor. The biquaternion algebra is finite dimensional and associative, and it has
zero divisors because its norm form is isotropic: the norm vanishes on a complex cone of dimension three,
and every nonzero element of that cone annihilates its own conjugate,
$\tilde Q\tilde Q^{\natural}=N(\tilde Q)e_0=0$. The criterion is exact. A nonzero $\tilde Q$ is invertible
if and only if $N(\tilde Q)\neq0$, and the inverse is then the two-sided plain inverse
$\tilde Q^{-1}=\tilde Q^{\natural}/N(\tilde Q)$; on the cone the inverse does not exist. This is the
plain-row criterion of *The Group of Units of the General Plain Algebra and the Complement of the Zero-Divisor Cone*, and it is the one criterion of the four
general products: each of them is the plain product read in a different slot, so each has the same
invertibility criterion and the same zero-divisor set.

**The operation.** Read the product as the composition of two operations, as *The Monoid of Acting Maps:
the Process Is the Multiplication, the State Is the Idempotent* does: an element is the map "multiply by
it", $L_{\tilde Q}:\tilde R\mapsto\tilde Q\tilde R$. A unit is an invertible map, a zero divisor is a
non-invertible one, and the cone is the set of elements whose acting map drops rank. A nonzero element of
the cone kills a nonzero argument, so it destroys information and no operation can restore it. Off the
cone, every acting map is invertible and the reversible processes are the units. The light cone is thus
not primarily a surface in spacetime; it is the set of processes that cannot be undone, and it becomes the
light cone of spacetime when the material coordinate is used.

**The state.** The second family of the cone is the set of nonzero multiples of idempotents, and a
rank-one projector is the extreme case. A projector satisfies $\tilde\Pi^{2}=\tilde\Pi$, so it is a
nonzero element of the cone: $N(\tilde\Pi)=0$ and $\tilde\Pi$ has no inverse, as *The Biquaternion Vacuum
as a Minimal Idempotent* states of the vacuum. This is not a defect of a state; it is the algebra's
statement that asking for the inverse of a measurement is a category mistake. The zero-divisor set is
therefore the home of two different physical objects at once, the lightlike propagation and the state, and
the two are separated by the scalar part, as the next section shows.

## The Cone in the Algebra and in Spacetime

### The vanishing set and its two families

The cone is the vanishing set of the biquaternion norm,

$$
\mathcal{C}=\{\tilde Q\neq0:\ N(\tilde Q)=\tilde Q\tilde Q^{\natural}=\sum_\mu Q_\mu^{2}=0\},
$$

a complex cone of complex dimension three with the apex removed, of real dimension six. On the material
sector it is the light cone $|\mathbf x|=c|t|$. The scalar part cuts it into two families, and the physics
of the two is different.

- The **pure** family, $Q_0=0$ and $(\mathbf Q,\mathbf Q)=0$. The square of a pure zero divisor vanishes,
  $\tilde Q^{2}=-(Q_1^{2}+Q_2^{2}+Q_3^{2})e_0=0$: these are the nilpotents, the lightlike displacements. A
  pure lightlike displacement is the translation part of a null direction, and its square being zero is
  the algebra's form of the statement that two successive displacements along a null direction add and
  nothing more. The family is of real dimension four, and the physical reading of the nilpotent square
  belongs to *Nilpotents in the 12 Structures of Biquaternions over $\mathbb{C}$* and to *Square Roots of Minus One, Zero and Plus
  One in the 12 Structures of Biquaternions over $\mathbb{C}$*.
- The **non-pure** family, $Q_0\neq0$. Its square is $\tilde Q^{2}=2Q_0\tilde Q-N(\tilde Q)e_0=2Q_0\tilde Q$,
  so the rescaled element $\tilde\Pi=\tilde Q/(2Q_0)$ is a nontrivial idempotent. These are the
  **idempotent multiples**, the multiples of the projectors. The non-pure family fills the cone in real
  dimension six. Physically it is the state family: the rank-one projectors of the informational sector
  are its boundary, the pure states of *Decoherence as Idempotent Projection* and *The Biquaternion Vacuum
  as a Minimal Idempotent*, and the family is read in *Idempotents in the 12 Structures of Biquaternions over $\mathbb{C}$*.

The two families answer the natural objection to reading a state as a zero divisor: the state is on the
cone, but it is not nilpotent, and its square is the projector it is a multiple of and not zero. The
vanishing of the norm is a statement about invertibility, not about the square.

### The cone in the four general products

The four general structures are the plain product $\tilde P\tilde Q$ (GPA, the composition band), the
quaternionic product $\tilde P^{\natural}\tilde Q$ (GQA), the plain sesquilinear product
$\tilde P\tilde Q^{*}$ (GPS, the probability band) and the quaternionic sesquilinear product
$\tilde P^{\natural}\tilde Q^{*}$ (GQS, the gauge band). Each is the plain product in one slot and one
conjugation, so each has the plain norm as its criterion and the cone as its zero-divisor set. The physics
of the cone differs from band to band, and the differences are the subject of *Composition and
Probability: the General Plain Algebra and the General Plain Sesqualgebra of Biquaternions Compared* and
*The Cone and the Massless Particles in the 12 Structures of Biquaternions over $\mathbb{C}$*: in the composition the cone is the
boundary of invertibility and the locus of lightlike propagation; in the probability it is the rank drop
of the sesquilinear square, rank two massive and rank one massless, read in *Mass, Rank and the Positivity
of the Dagger*; in the gauge band the same cone is the locus where the fourth product's metric degenerates,
read in *The States the Indefinite Metric Cannot Normalise*.

What the four share is the set itself. The identity
$N(\tilde P\tilde Q)=N(\tilde P)N(\tilde Q)$ makes the norm a multiplicative label, and the cone is the
set on which the label vanishes; no slot and no conjugation changes it. The physical statement is that
masslessness is a property of the interval alone, and the four products are four things to do with a
massless element, not four different notions of masslessness.

### The cone in the division subalgebras

The cone is not spread over the whole algebra. The centre $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_0,ie_0\}$ and the real-quaternion subspace
$\mathbb{H}_{\mathbb{B}}$ are division algebras: on $\mathbb{H}_{\mathbb{B}}$ the norm is a sum of four
squares of real numbers, which vanishes only at the origin, so neither subspace contains a zero divisor.
The zero divisors require the complexification, and they live in the two Hermitian-type sectors: the
$\mathbb{M}_-$ cone is the physical light cone, and the $\mathbb{M}_+$ cone is the boundary of the future
cone that carries the states. The division subalgebras are read in *The Anti-Hermitian Subspace
$\mathbb{M}_-$ as the Material Sector* and *The Hermitian Subspace $\mathbb{M}_+$ as the Informational
Sector*.

## The Twelve Sets and Their Physical Readings

The twelve products, their zero-divisor sets and the physical interpretation of each set are read here.
The mathematics of each row is proved in the mathematics companion and its block articles; the
interpretation is the contribution of this article. The twelve are read one by one below, each naming its
product, its zero-divisor set and the physical interpretation, and the table that follows collects the
twelve readings in one place.

### $\mathrm{GPA}$, the general plain algebra — composition

The product is the plain product $\tilde P\tilde Q$, and its zero-divisor set is the punctured cone
$\mathcal{C}\setminus\{0\}$. Off the cone the norm does not vanish and the acting map
$L_{\tilde P}:\tilde X\mapsto\tilde P\tilde X$ is invertible, with the two-sided inverse
$\tilde P^{\natural}/N(\tilde P)$; on the cone the map drops rank and destroys its argument. The physical
statement is that the composition of operations degenerates exactly on the light cone, so the cone is at
once the locus of lightlike propagation and the boundary between the reversible and the irreversible
processes. *The Group of Units of the General Plain Algebra and the Complement of the Zero-Divisor Cone* and *Zero Divisors as a Physical Locus in
Biquaternionic Form* own the reading.

The units are the elements off the cone, and they form the group $\mathbb{B}^{\times}\simeq S^{1}\times S^{3}$ with $\pi_1\cong\mathbb{Z}$ (*The Biquaternion Unit Group as a Topological Group*); the cone is the complement of that group, so the reversible operations are exactly the off-cone ones and the light cone is the wall of the reversible region.

### $\mathrm{SPA}$, the symmetric plain algebra — commutativity

The product is the Jordan product $\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$, and its zero-divisor set
enlarges to $(\{Q_0=0\}\cup\mathcal{C})\setminus\{0\}$: a nonzero element is a zero divisor exactly when
it is pure or lies on the cone, and a pure element annihilates the plane of the elements orthogonal to
it. The enlargement is physical and not a curiosity.
The unit $e_1$ has norm $1$ and is invertible in the algebra, yet $e_1\bullet e_2=0$, so a symmetrised
coupling can annihilate two non-degenerate operations. The reading is *The Symmetrised Material
Composition and the Jordan Identity* and *Observables as a Jordan Algebra: the Symmetric Plain Product
and the Classical Composition*.

The invertible elements are again the elements off the cone, with $e_0$ a two-sided unit, but they form no group, the product being non-associative; the complement of the enlarged set, $\{Q_0\neq0,\ \mathrm{Norm}\neq0\}\cup\{0\}$, is not the invertible set: the pure family is the gap, its elements being zero divisors of the coupling and invertible at once, and the origin is a non-zero-divisor that is not invertible.

### $\mathrm{APA}$, the antisymmetric plain algebra — rotation

The product is the commutator $\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)=\mathbf P\times\mathbf Q$, an
alternating product, so every nonzero element is annihilated by itself and the zero-divisor set is the
whole punctured space $\mathbb{B}\setminus\{0\}$. A bracket is not a composition: no element of it has an
inverse. Physically the antisymmetric plain product is the Lie bracket of rotations, and the statement is
that a rotation is an infinitesimal transformation, not an operation to be undone. The reading is *The
Cross Product as a Lie Bracket: Rotations and the Jacobi Identity* and *Angular Momentum and the Lie
Algebra of the Material Sector*.

There is no unit, the bracket taking its values in the vector subspace, so the complement of the whole punctured space is the origin alone: the rotation band has no reversible operation.

### $\mathrm{GQA}$, the general quaternionic algebra — causality

The product is $\tilde P^{\natural}\tilde Q$, the plain product with the natural conjugation in the first
slot, and its square is the central interval; the criterion is again the norm, so the zero-divisor set is
the same punctured cone. The band reads the cone as the shell of vanishing interval: a lightlike element
cannot be composed with, and the rank drop of the multiplication is the algebraic form of that statement.
The reading is *The Interval as the Square and the Charge of the Material Composition* and *Why the
Material Composition Is Oriented and Cannot Measure*.

The element $e_0$ is a left unit alone, and the invertible elements are the elements off the cone, with the solution $(\tilde P^{-1})^{\natural}$ of the inverse equations; the cone is the complement of those elements, and they form no group, the product being non-associative.

### $\mathrm{SQA}$, the symmetric quaternionic algebra — coupling

The product is the symmetrisation $\tilde P\star\tilde Q=N(\tilde P,\tilde Q)e_0$, central and
scalar-valued, and its zero-divisor set is the whole punctured space: the equation "the value is zero" is
one complex linear equation in the components of the partner, and its solutions fill a complex hyperplane.
A scalar coupling of two operations returns a number, and a number has no inverse. The reading is *The
Quaternion Form as a Product: the Scalar Coupling of Two Material Operations* and *Why a Central Product
Cannot Compose: the Radical and the Isotropic Elements*.

There is no unit — the value is a number and a number is not an operation — so there is no group of units and the complement of the whole punctured space is the origin alone: the coupling band has no reversible element.

### $\mathrm{AQA}$, the antisymmetric quaternionic algebra — obstruction

The product is the antisymmetrisation $\tfrac12(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P)$,
alternating, so the zero-divisor set is the whole punctured space. This is the bracket that obstructs the
internal action, and the physical statement is that a bracket which does not close is not a composition
either. The reading is *The Brackets That Do Not Close: the Jacobi Failure of the Quaternionic
Commutator* and *Boosts, Mixed Terms and the Missing Lie Structure*.

There is no unit, so there is no group of units and the complement of the whole punctured space is the origin alone: an obstruction is never a reversible operation.

### $\mathrm{GPS}$, the general plain sesqualgebra — probability

The product is the pairing $\tilde P\tilde Q^{*}$, and its zero-divisor set is the punctured cone. The
band reads the cone as the rank drop of the sesquilinear square: the square of a nonzero element has rank
two off the cone and rank one on it, so the zero divisors are exactly the amplitudes of vanishing Born
weight. The reading is *Mass, Rank and the Positivity of the Dagger* and *The Spinor Space as a Hilbert
Space of the General Plain Sesqualgebra*.

The element $e_0$ is a right unit alone, and the invertible elements are the elements off the cone, with the solution $(\tilde P^{-1})^{*}$ of the inverse equations; the cone is the complement of those elements, and they form no group.

### $\mathrm{SPS}$, the symmetric plain sesqualgebra — positivity

The product is the symmetrisation $\tfrac12(\tilde P\tilde Q^{*}+\overline{\tilde Q\tilde P^{*}})$,
scalar-valued, with the non-negative value $H(\tilde P,\tilde Q)$; the zero-divisor set is the whole
punctured space. The band keeps the real part of the Born pairing alone, and a real number cannot invert
anything: the value zero is one linear equation, killed by a hyperplane. A symmetrised pairing is a
measurement and not an operation. The reading is *The Hermitian Form as a Product: Positivity and the Real
Part of the Born Pairing* and *Why Probability Values Are Central: the Symmetric Sesquilinear Product and
Its Cone*.

There is no unit, the value being a real number, so there is no group of units and the complement of the whole punctured space is the origin alone.

### $\mathrm{APS}$, the antisymmetric plain sesqualgebra — phase

The product is the antisymmetrisation
$\tfrac12(\tilde P\tilde Q^{*}-\overline{\tilde Q\tilde P^{*}})$, the vector part of the pairing, and its
zero-divisor set is the whole punctured space. The band reads the imaginary part of the Born pairing, and
an imaginary part is a phase, not an operation with an inverse. The reading is *The Imaginary Part of the
Born Pairing: the Antisymmetric Sesquilinear Product* and *The Operators of the Antisymmetric Plain
Sesquilinear Product and the Phase*.

There is no unit, the value lying in the vector subspace, so there is no group of units and the complement of the whole punctured space is the origin alone.

### $\mathrm{GQS}$, the general quaternionic sesqualgebra — gauge

The product is the fourth product $\tilde P^{\natural}\tilde Q^{*}$, and its zero-divisor set is the
punctured cone, the null set of the indefinite metric. Here the cone is the locus where the gauge metric
degenerates, and the rank drop is the algebraic form of a gauge direction that cannot be normalised. The
reading is *The Fourth Product and Its Indefinite Metric* and *The States the Indefinite Metric Cannot
Normalise*.

There is no unit on either side, and the invertible elements are the elements off the cone, with the solution $(\tilde P^{-1})^{\natural*}$ of the inverse equations; the cone is the complement of those elements, and they form no group.

### $\mathrm{SQS}$, the symmetric quaternionic sesqualgebra — metric

The product is the symmetrisation
$\tfrac12(\tilde P^{\natural}\tilde Q^{*}+\overline{\tilde Q^{\natural}\tilde P^{*}})$, and its
zero-divisor set is the enlarged set $(\{Q_0=0\}\cup\mathcal{C})\setminus\{0\}$, as for $\mathrm{SPA}$.
The band reads the symmetric part of the gauge metric, and the same witness applies: a symmetrised gauge
coupling annihilates two operations whose vector parts are conjugate-orthogonal. The reading is *The Gauge
Metric as a Product: the Symmetric Quaternionic Sesquilinear Product* and *Values in No Subspace: Why the
Symmetric Gauge Product Is Not a State*.

There is no unit, both symmetrised terms conjugating a factor, so the complement of the enlarged set, $\{Q_0\neq0,\ \mathrm{Norm}\neq0\}\cup\{0\}$, carries no group of units.

### $\mathrm{AQS}$, the antisymmetric quaternionic sesqualgebra — polarisation

The product is the antisymmetrisation $\tfrac12(\tilde P^{\natural}\tilde Q^{*}-\overline{\tilde Q^{\natural}\tilde P^{*}})=\mathbf P\times\overline{\mathbf Q}$,
the conjugate cross product, and its zero-divisor set is the whole punctured space. The band reads the
polarisation of the gauge coupling, and a conjugate bracket is not a composition. The reading is *The
Cross Product of a Vector with Its Conjugate: the Antisymmetric Gauge Product* and *The Operators of the
Antisymmetric Quaternionic Sesquilinear Product and the Polarisation*.

There is no unit, the value lying in the vector subspace, so there is no group of units and the complement of the whole punctured space is the origin alone.

### The Twelve Sets in One Table

The table collects the twelve products, their zero-divisor sets and the physical interpretation of each
set.

| structure | product | zero-divisor set | physical reading |
|---|---|---|---|
| GPA | $\tilde P\tilde Q$ | $\mathcal{C}\setminus\{0\}$ | the plain composition degenerates on the light cone: lightlike propagation, no inverse |
| GQA | $\tilde P^{\natural}\tilde Q$ | $\mathcal{C}\setminus\{0\}$ | the quaternionic composition degenerates on the same cone |
| GPS | $\tilde P\tilde Q^{*}$ | $\mathcal{C}\setminus\{0\}$ | the probability band degenerates on the cone: the rank drop of the sesquilinear square |
| GQS | $\tilde P^{\natural}\tilde Q^{*}$ | $\mathcal{C}\setminus\{0\}$ | the gauge band degenerates on the cone: the null set of its indefinite metric |
| SPA | $\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ | $(\{Q_0=0\}\cup\mathcal{C})\setminus\{0\}$ | the symmetrised composition also annihilates on the lightlike family |
| SQA | $\tfrac12(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P)$ | $\mathbb{B}\setminus\{0\}$ | a scalar-valued coupling: the value is a number that composes with nothing |
| SPS | $\tfrac12(\tilde P\tilde Q^{*}+\overline{\tilde Q\tilde P^{*}})$ | $\mathbb{B}\setminus\{0\}$ | a scalar-valued pairing: the weight is a number, not an operation |
| SQS | $\tfrac12(\tilde P^{\natural}\tilde Q^{*}+\overline{\tilde Q^{\natural}\tilde P^{*}})$ | $(\{Q_0=0\}\cup\mathcal{C})\setminus\{0\}$ | the symmetrised gauge coupling also annihilates on the lightlike family |
| APA | $\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)$ | $\mathbb{B}\setminus\{0\}$ | the antisymmetrised composition is not invertible anywhere |
| AQA | $\tfrac12(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P)$ | $\mathbb{B}\setminus\{0\}$ | the antisymmetrised quaternionic composition is not invertible anywhere |
| APS | $\tfrac12(\tilde P\tilde Q^{*}-\overline{\tilde Q\tilde P^{*}})$ | $\mathbb{B}\setminus\{0\}$ | the antisymmetrised pairing is not invertible anywhere |
| AQS | $\tfrac12(\tilde P^{\natural}\tilde Q^{*}-\overline{\tilde Q^{\natural}\tilde P^{*}})$ | $\mathbb{B}\setminus\{0\}$ | the antisymmetrised gauge coupling is not invertible anywhere |

Three groups appear in the table, and each group has one physical statement.

- **The four general products.** The set is the cone. These are the structures that compose and pair; each
  composes off the cone and fails on it, so their physics is the physics of the light cone, read in the
  four bands by the four articles cited in the previous section.
- **The two symmetric structures $\mathrm{SPA}$ and $\mathrm{SQS}$.** The set is the enlarged set: the
  pure family $\{Q_0=0\}$ and the cone. The physics of the enlargement is that the symmetrised coupling of
  two **pure** operations vanishes whenever their vector parts are orthogonal. The cleanest witness is the
  unit itself: $\tilde P=e_1$ has norm $1$ and is invertible in the algebra, yet for the Jordan product
  $\tilde P\bullet\tilde Q=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ one has
  $e_1\bullet e_2=\tfrac12(e_1e_2+e_2e_1)=0$. The same holds for the symmetric quaternionic sesquilinear
  product, $e_1\star e_2=0$. A unit that cannot be composed symmetrically with another unit is the
  physical content of the enlargement: the derived symmetric operations are couplings, and a coupling of
  two lightlike directions can vanish even when both directions are non-degenerate.
- **The six derived structures $\mathrm{SQA}$, $\mathrm{SPS}$, $\mathrm{APA}$, $\mathrm{AQA}$,
  $\mathrm{APS}$ and $\mathrm{AQS}$.** The set is the whole punctured space: every nonzero element has an
  annihilator, so the product has no invertible operation at all. The reason splits in two. The two
  **scalar-valued** structures $\mathrm{SQA}$ and $\mathrm{SPS}$ return a central number,
  $\mathrm{Sc}(\tilde P^{\natural}\tilde Q)e_0$ and $\mathrm{Sc}(\tilde P\tilde Q^{*})e_0$, and the
  equation "the value is zero" is one linear equation in the components of the second factor, whose
  solutions fill a complex hyperplane. The four **antisymmetric** structures are alternating or
  conjugate-alternating, and every nonzero element is annihilated by a partner built from itself. A product
  whose value is a number, or whose value is an antisymmetrisation, is not an operation one can iterate;
  the whole-space zero-divisor set is the algebraic form of that statement.

## The Cone as the Common Core of the Twelve

The mathematics companion states the sharpest consequence of the table: the cone is contained in all twelve
zero-divisor sets, and the four general products are exactly the four for which the containment is an
equality. Two physical statements follow.

The first is a statement of independence. Every lightlike element is annihilated in every one of the twelve
structures. Masslessness, read as the vanishing of the interval, is therefore not an artefact of the
product one chooses; it survives all twelve readings, and the cone is the largest set on which the twelve
agree. The second is a statement of strictness. Off the cone, the derived structures still have zero
divisors, and the extra elements are exactly the ones the derived operations cannot handle. The failure
of the symmetrised operations on the unit $e_1$ is the simplest case, and the failure of the scalar-valued
and antisymmetric operations on every element is the extreme case. The cone is thus the boundary of
invertibility for the four compositional structures, and for the eight derived structures it is only the
intersection of their much larger degeneracy.

The distinction matches an earlier split of the corpus. The four general products carry the units, the
inverses and the operator laws; the eight derived products are the symmetrisations and antisymmetrisations
used as couplings, values and brackets. A coupling that returns a number is the physical content of the
scalar-valued structures, and a bracket that changes sign under exchange is the content of the
antisymmetric ones. Neither is a rule for composing a process with a process, and the zero-divisor set
says so.

## What the Zero-Divisor Set Decides

| claim | source | status |
|---|---|---|
| the zero-divisor set of the four general products is the punctured cone | mathematics companion, theorem; recomputed on 25 random cone points and on the witnesses $e_0+ie_1$, $e_1+ie_2$ | verified |
| the norm criterion is $N(\tilde Q)=0$, with inverse $\tilde Q^{\natural}/N(\tilde Q)$ | *The Group of Units of the General Plain Algebra and the Complement of the Zero-Divisor Cone* | cited |
| a pure cone element has $\tilde Q^{2}=0$ and a non-pure one gives the idempotent $\tilde Q/(2Q_0)$ | mathematics companion; recomputed | verified |
| $\mathrm{SPA}$ and $\mathrm{SQS}$ have the enlarged set $(\{Q_0=0\}\cup\mathcal{C})\setminus\{0\}$ | mathematics companion; witness $e_1\bullet e_2=0$ with $N(e_1)=1$ recomputed | verified |
| the six derived structures have the whole punctured space | mathematics companion; random annihilators found for $\mathrm{SQA}$ and $\mathrm{SPS}$, alternating squares vanish | verified |
| the cone is contained in all twelve sets and equals four | mathematics companion, theorem | cited |
| the material cone is the light cone $|\mathbf x|=c|t|$ | *The Light Cone as the Biquaternion Zero-Divisor Cone* | cited |
| the rank drop of the sesquilinear square is the mass label | *Mass, Rank and the Positivity of the Dagger* | cited |
| the cone is the information barrier, the home of the erasure's target and the rank-one mass boundary | *Causality and the Light Cone as an Information Barrier in Biquaternionic Form*; *Landauer's Principle and the Material–Informational Exchange in Biquaternionic Form*; *Mass, Rank and the Positivity of the Dagger* | interpretation |
| the complement of the cone is the invertible region; a spacelike element is a unit | *The Group of Units of the General Plain Algebra and the Complement of the Zero-Divisor Cone*; *Subluminal and Superluminal Electromagnetic Waves and the Lepton Mass Spectrum*; recomputed that a random spacelike element has $N>0$ and an inverse | verified |
| the horizon is a null surface of the same cone | *Black Hole Thermodynamics in Biquaternionic Form* | cited |
| the cone is pointwise; a curved background replaces it by a field of local cones | *Curved Spacetime and the Biquaternion Framework* | cited |
| the null cone is a cone over its directions; the projectivisation is the celestial sphere, and the complex cone's is the Segre quadric | *The Celestial Sphere of the Null Cone: Null Directions, Chirality and the Phase* | cited |
| the confinement kernel is a destroyed description, not a hidden one | *Confinement and the Loss of Partonic Information in Biquaternionic Form*; *Gauge Redundancy and the Information in the Gauge Orbit in Biquaternionic Form* | cited |

## The Zero-Divisor Set Beyond the Twelve

The theorem above is the zero-divisor set read through the twelve products. Six further properties of the same set are proved in the corpus, and they are gathered here because they read the zero divisor as a physical object rather than as a row of the table.

**The zero-divisor set is where the square collapses.** On the cone the square is affine, $\tilde Q^{2}=2Q_0\tilde Q$ for every $\tilde Q$ with $N(\tilde Q)=0$, so squaring a lightlike element stays on its own complex line and never leaves the cone (*The Zero Divisors and the Singular Julia Sets*). The critical set of the quadratic map $\tilde Q\mapsto\tilde Q^{2}+\tilde C$ is the union of the cone and the vector subspace, and the cone is the part of it on which the square can collapse and on which no escape radius is uniform; for $\tilde C=0$ every idempotent lies on the Julia set of that map, and the singular Julia set contains a complex surface. The physical reading is that a lightlike operation squared does not leave its ray, and that the projectors — the idempotent measurements — sit on the Julia set of the squaring: a measurement squares to itself and cannot be undone, and the algebra's dynamics of the square is the sharpest form of that irreversibility.

**The zero-divisor set is the largest nontrivial vanishing set of a square.** Among the squares of the algebra the natural square $\tilde Q\tilde Q^{\natural}=N(\tilde Q)e_0$ vanishes exactly on the cone, while the sesquilinear square $\tilde Q\star\tilde Q=\tilde Q\tilde Q^{*}$ vanishes at the origin alone (*The Squares and the Positive Cone of the Biquaternion Sesqualgebra*). The reading is a statement about the two pairings: only the square that carries the interval can collapse, and the square that carries the Born pairing never does, which is why a probability weight cannot be sent to zero by an operation alone. The degeneracy is a property of the indefinite form and not of the algebra's multiplication.

**The zero-divisor set is the boundary of the state cone, and the boundary is the image of the cone.** The map $\tilde Q\mapsto\tilde Q^{*}\tilde Q$ sends the units into the interior of the Hermitian cone $P$, $P^{\circ}=\{\tilde Q^{*}\tilde Q:N(\tilde Q)\neq0\}$, and the sector part of the zero-divisor locus is the isotropic cone of $\mathbb{M}_+$ (*Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*). On $\mathbb{M}_+$ the Krein cone is the full light cone of the interval and its future nappe is the Hermitian cone $P$ (*Indefinite Positivity and the Krein Cone of the Biquaternion Algebra*). The reading is that the edge of the state space is the image of the zero-divisor set under the positivity map: a state on the edge is a zero divisor at trace one, and the invertible region is exactly the interior. The measurement formalism's positivity and the algebra's degeneracy are two faces of one boundary.

**The zero-divisor set has a topology, and the cone is the complement of the unit group.** The units are the elements off the cone, forming $\mathbb{B}^{\times}\simeq S^{1}\times S^{3}$ with $\pi_1\cong\mathbb{Z}$ and $\pi_2=0$, while the cone — the zero-divisor set together with the apex — is contractible with the apex as its only singular point and link an $S^{1}$-bundle over $S^{2}\times S^{2}$ with $\pi_2\cong\mathbb{Z}$ (*The Biquaternion Unit Group as a Topological Group*, *The Topology of the Zero-Divisor Cone*); the real slice, the material light cone, has real dimension three and link $S^{2}\sqcup S^{2}$ (*Biquaternion Lorentzian and Conformal Geometry*). The reading is that the degeneracy is not a thin set but a six-real-dimensional manifold, and that the invertible and the degenerate regions are complementary, distinguished by the vanishing of one homotopy group. The norm decides at once whether an operation can be undone and which side of the boundary it lies on.

**The quadratic criterion is a feature of the complex signature, not of zero divisors in general.** In the split-biquaternion algebra the zero-divisor criterion is linear in the idempotent basis, $\tilde Q_{+}=0$ or $\tilde Q_{-}=0$, and the zero-divisor set is the union of two four-dimensional linear subspaces meeting at the origin, rather than a quadric cone (*Split-Biquaternion Zero Divisors*); the split-quaternion algebra behaves in the same way, its zero-divisor set being the null cone of an indefinite norm (*Split-Quaternion Zero Divisors*). The reading is a caution: the physical statement that degeneracy is concentrated on the light cone of a quadratic form is a property of the complexified, biquaternion signature. A split world has a degeneracy of a different shape, linear rather than quadratic, and the equation $N=0$ that the corpus reads as the light cone is not available there in the same form.

**The pure family is the nilpotent cone.** The nilpotents of the algebra are exactly the pure zero divisors, the elements with $Q_0=0$ and $N(\tilde Q)=0$, and they form the nilpotent cone of real dimension four; the isotropic elements of the symmetrised products are the zero divisors of the parent plain algebra (*List of Zero Divisors and Nilpotents*, *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*). The reading separates the two halves of the cone: the pure half is the nilpotent lightlike displacement, whose square vanishes, and the non-pure half is the multiples of the projectors, whose square stabilises. The first is the lightlike translation, the second the measurement, and the zero-divisor set holds both.

## The Cone as an Information Barrier and a Mass Label

The cone is one set shared by the four general products, but the corpus reads it in four different roles,
and the zero-divisor article is the natural place where the four readings meet.

**The information barrier.** *Causality and the Light Cone as an Information Barrier in Biquaternionic
Form* reads the material cone as the boundary of causal influence: the cone is the edge of the region a
signal can reach, and the pairs of events outside it can neither signal nor be signalled. The zero-divisor
condition is the algebraic face of the same barrier. A zero divisor sends a nonzero input to zero, so it is
a process that cannot be reversed and cannot return a message; the cone is the locus where an elementary
process loses its invertibility, and the loss of invertibility is what makes the cone a horizon rather than
an ordinary surface. "A signal propagates only within the cone" and "composition degenerates only on the
cone" are the geometric and the algebraic statements of one object.

**The erasure budget.** The loss of invertibility of a map is a loss of information, and the corpus prices
it. *Landauer's Principle and the Material–Informational Exchange in Biquaternionic Form* fixes the
exchange rate between the informational and the material ledgers: the erasure of one bit costs at least
$k_BT\log2$ of dissipated heat. The zero divisor is the algebra's elementary non-invertible step — an
operation with no inverse, whose kernel is what it sends to zero — and the dimension of the kernel is the
size of what the operation merges into zero. The units are the processes that erase nothing, the zero
divisors the processes that erase something, and a rank-dropping zero divisor is the elementary irreversible
step whose thermodynamic price the Landauer article owns.

**The rank and the mass label.** In the probability band the cone is where the sesquilinear square drops
rank, from two to one, and the rank is read as a mass label in *Mass, Rank and the Positivity of the
Dagger*. *The Four Readings of a Biquaternion: Norm, Rank, Charge and Scale* marks which of the four readings
is the mass, and the cone owns that one cleanly and the rank only as a value. The cone is exactly the rank-one locus,
so "on the cone" and "one polarisation" are the same statement; the norm reads the same set as the level
set $N=0$, and a level set is a value and not a count. The cone is therefore not the mass itself. It is
the boundary at which the count of polarisations falls, and the shells $N=-m^2c^2$ around it are what the
norm labels.

**The state family and its irreversibility.** The non-pure family of the cone is the family of multiples of
the positive projectors, and *Decoherence as Idempotent Projection* moves a state from that family into the
interior of the Bloch ball: a pure state is an idempotent and hence a zero divisor, a mixed state is not,
and decoherence is the passage off the cone. *Quantum Channels and the Reversible/Irreversible Dichotomy*
supplies the operator reading of the same passage: a reversible channel is conjugation by a single unit,
and every irreversible channel is a sum of conjugations, so reversibility is unitarity and irreversibility
is the failure of the elementary operation to be a unit. The zero-divisor cone is thus the boundary between
the reversible and the irreversible halves of the state space.

**The cone is the characteristic cone of the wave operator.** The algebra carries two canonical quadratic
structures, and the zero-divisor cone is the isotropy of one of them. *The Symplectic Form and the
Biquaternion Norm Cone* separates them: the **Hermitian** form $\mathrm{Sc}(\tilde Z^{*}\tilde W)$ is
positive definite, so it has no isotropic direction off the origin and defines no cone; the **holomorphic
biquaternion norm** $N(\tilde Z)=\tilde Z\tilde Z^{\natural}$ is a general bilinear form, and its vanishing
set is the cone this article studies. On the material sector that cone is the light cone, and the article
identifies it as the **characteristic cone of the d'Alembertian** — the surface along which a
discontinuous wavefront spreads, the cone of the wave operator rather than of the state space. The same
article shows that one complex structure produces both faces at once: reading a phase-space element
$\tilde Z=\tilde q+i\tilde p$, the Hermitian pairing splits into its real part, a positive-definite metric,
and its imaginary part, a symplectic form, with the algebra's central $i$ as the compatible complex
structure. The zero-divisor cone and the symplectic structure are therefore two faces of one quadratic
geometry, and the cone is where the *holomorphic* face degenerates.

**Where the cone sits: a kinematic boundary.** *Zero Divisors as a Physical Locus in Biquaternionic Form*
asks where the zero-divisor set sits in a non-relativistic spin-0 problem, and it answers with three images
of one object. In momentum space the locus is the massless shell, written $N(\tilde{\mathcal P})=0$ for the
momentum biquaternion; the free non-relativistic dispersion does not lie on it, and it meets the locus only
at the scale $p=2mc$, so the cone is **the boundary of the non-relativistic description** — the theory is
consistent on one side and touches the cone where it is about to fail. In configuration space the locus has
no preimage under a real momentum, and what survives is its shadow: the **WKB turning surface**
$p(x)^2=0$, where the semiclassical amplitude diverges and the eikonal momentum degenerates. In state space
the locus is the boundary of the pure-state manifold, and there it plays a double role, because the state
module is **generated by a null element**: the cone is both the boundary of the state space and its origin.
The unifying statement is that the zero-divisor locus is a **kinematic boundary, not a dynamical
attractor**: a unit and a central phase preserve it, so an invertible element never becomes a zero divisor
under the flow, and the locus bounds where the algebra is a division algebra, where the semiclassical
approximation holds and where the non-relativistic description is self-consistent — and it does not bound
propagation. The algebra's Hermitian forms carry a second invariant, and it should be named without being confused
with the cone. *Hermitian Forms over the Biquaternion Algebra and the Unitary Witt Group with Hermitian
Adjoint* classifies those forms by the inertia $(p,q,r)$ of positive, negative and null directions, fixed in
every basis by Sylvester's law, with the signature $p-q$ the invariant of a non-degenerate form. The unit form
is the algebra's Hilbert form, and its indefinite companion is the Krein form, whose cone is the Krein cone.
That taxonomy belongs to the *Hermitian* forms; the zero-divisor cone of this article is the isotropic cone of
the *bilinear* biquaternion norm, and the two are companion quadratic structures of one complex structure
rather than one object.

**The complement is the invertible region.** The theorem of *The Group of Units of the General Plain Algebra and the Complement of the Zero-Divisor Cone* is an
equivalence: $\tilde Q$ is invertible if and only if $N(\tilde Q)\neq0$. On the material sector this
partitions the four-vectors exactly as physics does. The **null** four-vectors are the zero divisors, and
the **timelike** and **spacelike** ones are units. The partition has a consequence the word "zero divisor"
invites one to miss: a spacelike four-vector — a superluminal or tachyonic displacement, with $N>0$ — is
**invertible**, so it is not a zero divisor at all. The corpus's superluminal solutions of the free Maxwell
equation are read in *Subluminal and Superluminal Electromagnetic Waves and the Lepton Mass Spectrum* with
the caution that the superluminality is a pattern speed of a localised packet and not a signalling speed;
the algebra adds its own statement, that the spacelike region is the invertible one and the failure of
invertibility sits on the cone alone. The zero-divisor set is therefore the null cone and nothing else, and
the physical claim "this process cannot be undone" means "this process is lightlike" and not "this process
is fast".

**The horizon, and why the cone is not it.** A black-hole event horizon is a **null surface**: it is
generated by a Killing field that is null on it, and *Black Hole Thermodynamics in Biquaternionic Form*
reads its temperature, entropy and first law in the material sector while importing the metric and the
horizon geometry. The temptation is to call the horizon "a piece of the zero-divisor cone", and it should be
resisted, because the two objects are of different kinds. The zero-divisor cone is a **cone in the tangent
space**: at each point it is the set of null *directions*, a fibrewise condition on a single vector, and it
says nothing about which points of spacetime admit such directions. A horizon is a **hypersurface in
spacetime**, a set of *points*, selected by a particular solution of the field equations. What the two
share is the algebra's notion of nullity — a direction is null exactly when its norm vanishes — and the
horizon is where the generating Killing vector is null in that sense. The cone supplies the criterion; the
metric supplies the surface. The two roles must be kept apart: the cone is a property of the algebra and
holds everywhere, and a horizon is a property of one solution and holds on one surface.

**The destroyed description and the hidden one.** *Confinement and the Loss of Partonic Information in
Biquaternionic Form* gives the sharpest information reading of a non-invertible process. Its subject is not
a zero divisor of a product but a loss of labels: the colour of an asymptotic quark is not held in a kernel
that a gauge choice could recover, it is absent from the observable algebra. The contrast with
*Gauge Redundancy and the Information in the Gauge Orbit in Biquaternionic Form* is the point the
zero-divisor article should carry: a non-invertible operation can fail to be invertible for two different
reasons, because the information is **hidden** in a redundancy or because it is **destroyed** in the
operation, and the algebraic face of "destroyed" is a kernel the operation cannot return from. The word
"destroyed" is an informational description, not a thermodynamic one: the confinement loss is a label
absent from the observable algebra, and the corpus's pricing of irreversible erasure belongs to
*Landauer's Principle and the Material–Informational Exchange in Biquaternionic Form*, not to this reading.

**The geometry lives on the cone.** A vanishing quadratic form might be expected to supply no geometry, and
*The Fubini–Study Geometry and the Biquaternion Norm* shows that it supplies all of it. The pure states of
the state space are the rank-one idempotents, which are null elements of the algebra, and on them the
biquaternion norm vanishes; but the article's central identity is that the metric is the norm's **second
variation at the null direction**, $ds^{2}_{\mathrm{FS}}=-N(\delta\tilde P)$, the first variation vanishing
as it does at every null direction of a quadratic form. The line element so obtained is the Fubini–Study
metric of $\mathbb{P}^1(\mathbb{C})$, one quarter of the round metric of the Bloch sphere. The article
states its own limit precisely: the norm "gives the boundary exactly and the flat geometry everywhere, but
not the metrically distinguished interior", the interior metric being the Bures metric, which the algebra
does not supply. The cone is therefore not a geometric dead end. It is the locus on which the algebra's
quadratic form stops measuring length at first order and starts measuring it at second order, and the state
space's geometry is read off the cone's own structure.

**A central shift crosses the mass gap, and the cone is its massless limit.** *The Klein Paradox in
Biquaternionic Form* solves a Dirac electron on an electrostatic step and locates the physics exactly. The
potential term is **central** — a scalar multiple of $e_0$ — so it does not act on the state module and only
shifts the mass shell, while the mass term is the chirality-off-diagonal pair that mixes the two minimal
ideals. The step becomes *more* transparent as it grows, and in the massless limit the transmission is unity
for every step height. The algebraic content of the "paradox" is a statement about the mass gap: a central
shift moves the frequency past it, into the region where the two mass-shell roots exchange their roles, and
the current the algebra conserves is no longer the transport of one particle. The cone enters only as the
limit in which the gap closes: the massless case $m\to0$, in which the two shells meet on the cone, is
exactly the case of unit transmission. The consequence for this article is a caution rather than a
coincidence: the zero-divisor cone is the boundary of invertibility in the algebra, the Klein step is a
boundary of a one-particle *description* set by the mass gap, and the two must not be identified — they meet
only where the mass vanishes and the description is trivially valid at every step height.

**The cone is the boundary at infinity.** *Velocity Space as Hyperbolic Geometry in Biquaternionic Form*
identifies the velocity space of a massive particle as a hyperbolic three-space of curvature $-1/c^{2}$, and
its own finding gives the cone a second geometric role. The light cone is the **boundary at infinity** of
that space: it is at infinite geodesic distance from every velocity while the velocity itself is bounded by
$c$, which is the geometric statement that no finite number of boosts reaches the speed of light. The
article's framework statement is exact: "the boundary at infinity is the zero-divisor cone, which the algebra
carries as the set of non-invertible elements, so the boundary of the geometry and the boundary of
invertibility are the same set". So the cone is not only the set of operations the product cannot invert; it
is also the ideal boundary of the geometry the material sector carries, and the physical unboundedness of
rapidity is the same fact as the algebraic non-invertibility of the null directions.

**A topological obstruction is not the cone.** *The Magnetic Monopole in Biquaternionic Form* supplies the
contrast the zero-divisor reading needs. A point monopole cannot be described by one smooth potential: were
$\tilde F$ the vector part of $\tilde\nabla^{\natural}\tilde A$ for a single everywhere-defined
$\tilde A$, the Bianchi identity would hold and no magnetic source could appear. The monopole forces a
**patchwise** potential, the two patches related on their overlap by a gauge transformation with a
multivalued parameter — the biquaternionic Dirac string — and the magnetic charge is the **winding** of that
parameter, a topological integer fixed by boundary data and not by the local shape of the field. This is a
different kind of obstruction from the one this article studies, and the difference is the point. A zero
divisor is an element the product cannot invert: an **algebraic** failure that holds everywhere and is
detected by the norm. The Dirac string is a **topological** failure of a global potential on one
configuration: the field is invertible wherever it is smooth, and the obstruction is in the patching, not in
the norm. The article's own ledger keeps the two honest — the quantisation condition $eg=2\pi n\hbar c$
emerges as the single-valuedness of the gauge phase around the string, it imports $\hbar$, and it predicts
neither the existence nor the mass of a monopole. One further fact belongs to this companion's sector
language: the static monopole field is a **purely real vector of $\mathbb{M}_-$**, where the electric Coulomb
field is a **purely imaginary vector of $\mathbb{M}_+$**, so that the electric–magnetic split of the field is
the material–informational split of the algebra, and the duality rotation that exchanges them is a central
$U(1)$ symmetry.

**The cone is the degenerate orbit of the symplectic structure.** *The Symplectic Form and the Biquaternion
Norm Cone* gives the cone a dynamical identity, and the identification is exact. Writing a phase-space point
as the biquaternion $\tilde Z=\tilde q+i\tilde p$, the **Hermitian pairing** has real part the Euclidean
metric $g$ and imaginary part the **symplectic form** $\omega$, and the algebra's central $i$ is the
compatible complex structure $J$ of the Kähler triple — the root of $-1$ is the $J$. The coadjoint orbit is
a **level set of the biquaternion norm**, and the article's own phrase is that "the cone is the degenerate
orbit at zero level". So the cone is not only where the quadratic form stops being a metric: it is the
**degenerate orbit** of the symplectic structure whose complex structure is the root of $-1$ the corpus uses
everywhere. Three faces meet in one set — the zero-divisor set, the zero level set of the norm, and the
orbit on which the symplectic form degenerates — and the reading is purely classical: no measurement
postulate and no commutator enter.

## Physical Interpretation

- A zero divisor is an operation that annihilates a nonzero input. It cannot be inverted, and the cone is
  the set of such operations.
- For the four general products the zero-divisor set is the light cone. Composition and pairing degenerate
  exactly where the interval vanishes, which is the algebraic form of lightlike propagation and of the
  rank-one massless boundary of the state cone.
- The cone splits by the scalar part. The pure family is the nilpotent lightlike displacements; the
  non-pure family is the multiples of the projectors, that is, the states. A state is a zero divisor
  because a measurement cannot be undone, not because its square vanishes.
- For the two symmetric structures $\mathrm{SPA}$ and $\mathrm{SQS}$ the degeneracy is larger: the
  symmetrised coupling also annihilates on the lightlike family, and an invertible unit can fail to
  compose symmetrically.
- For the six derived structures the degeneracy is total: a scalar-valued coupling or an antisymmetrised
  bracket is not an operation to be iterated, and no nonzero element of it is invertible.
- The cone is the common core of the twelve sets, so masslessness does not depend on the product. The
  products differ in what they can do with a non-lightlike element, not in where they degenerate.
- The cone is the information barrier of *Causality and the Light Cone as an Information Barrier in
  Biquaternionic Form*, the home of the erasure's target state — a reset memory lands on a pure state, which
  is a zero divisor, and the reset costs $k_BT\log2$, the price *Landauer's Principle and the
  Material–Informational Exchange in Biquaternionic Form* fixes — and the rank-one boundary at which the
  mass label of *Mass, Rank and the Positivity of the Dagger* falls from two to one.
- The complement of the cone is the invertible region. The null four-vectors are the zero divisors; the
  timelike and the spacelike ones are units, so a superluminal displacement is invertible and the failure
  of invertibility sits on the cone alone.
- A non-invertible operation can hide information or destroy it. A gauge kernel hides a description that a
  gauge choice can recover; the confinement kernel of an asymptotic colour label has destroyed a description
  the observable algebra no longer contains; that loss is an absent label rather than an erased memory, so it
  is not an erasure and carries no Landauer price.
- A black-hole event horizon is a null surface, so it shares the algebra's notion of nullity with the cone.
  It is not a piece of the cone: the cone is a fibrewise set of null directions, the horizon a hypersurface
  selected by one solution and its metric. The cone supplies the criterion, the metric supplies the surface.
- The cone is pointwise, and a curved background replaces it by a **field of cones**. Every cone statement
  in the corpus is a statement about one fixed algebra $\mathbb{B}$ evaluated at one point: the norm, the
  rotor action and the light cone as the zero-divisor set are all flat and pointwise (*Curved Spacetime and
  the Biquaternion Framework*). In a curved spacetime a cone attaches to each point, its null directions are
  read off the local metric, and the single global cone becomes a field of local cones. This is the general
  form of the horizon reading above: the algebra supplies the pointwise criterion of nullity, and the metric,
  now a field, selects the directions and the surfaces, the horizon being one such surface. The source is
  explicit about the limit: curvature enters only through a tetrad, and the algebra "supplies nothing that
  determines" the metric and has no representation of $\mathrm{Diff}(M)$.
- The cone is a **kinematic boundary** with three images: the massless shell in momentum space, the WKB
  turning surface in configuration space, and the boundary *and* origin of the state space, because the
  module is generated by a null element. It bounds where the algebra divides, where the semiclassical
  approximation holds and where the non-relativistic description is consistent; it does not bound
  propagation. It is not to be confused with the inertia $(p,q,r)$ of the Hermitian forms: the signature is a
  capacity of modes, the cone is the isotropic set of the bilinear norm, and they are companion structures.
- The cone is the boundary of the algebra's invertibility, and the mass gap is a different boundary. The
  Klein step of *The Klein Paradox in Biquaternionic Form* is a boundary of a one-particle *description*,
  set by the mass gap: a central potential shift moves the frequency past it, the two mass-shell roots
  exchange their roles, and the conserved current is no longer the transport of one particle. The cone
  enters only in the massless limit, where the gap closes and the step is transparent at every height. The
  algebra records the conservation and leaves the particle interpretation to the field theory.
- The cone carries the state-space metric. The biquaternion norm vanishes on the pure states, and the
  Fubini–Study metric is its second variation at a null direction, $ds^{2}_{\mathrm{FS}}=-N(\delta\tilde P)$:
  the cone is where the algebra's quadratic form stops measuring length at first order and measures it at
  second order, so the state space's geometry is read off the cone rather than blocked by it.
- The cone is also a **geometric boundary at infinity**. In *Velocity Space as Hyperbolic Geometry in
  Biquaternionic Form* the velocity space is a hyperbolic space whose ideal points are exactly the lightlike
  elements, the ones the algebra cannot invert. The metric's cross-ratio is built from them, and the
  unboundedness of rapidity is the geometric form of the cone's non-invertibility.
- The cone is a **cone over its own directions**, and those directions are a sphere. In *The Celestial Sphere
  of the Null Cone: Null Directions, Chirality and the Phase* two nonzero null elements define the same
  direction when they differ by a scale, the set of directions is the projectivisation of the null cone, and
  on the material sector that projectivisation is a two-dimensional sphere — the **celestial sphere**, the
  sphere a photon's momentum points along. The Lorentz group acts transitively: the future null directions
  are one orbit, the past directions the other, and time reversal exchanges them, so the sphere, not the
  cone, is the Lorentz-homogeneous object. Complexified, the projectivisation is the **Segre quadric**, whose
  two rulings are the two chiral celestial spheres, and the real sphere is their diagonal, the fixed set of
  the conjugation.
- The cone is algebraic, and a topological obstruction is a different thing. *The Magnetic Monopole in
  Biquaternionic Form* is a configuration where no single global potential exists and the charge is a
  winding, but the field is invertible wherever it is smooth: the failure is in the patching, not in the
  norm. The monopole also sorts the field by sector — magnetic a real vector of $\mathbb{M}_-$, electric an
  imaginary vector of $\mathbb{M}_+$ — and its quantisation condition imports $\hbar$ without predicting
  existence or mass.
- The cone is also a **degenerate orbit of the symplectic structure**. On the phase-space biquaternion
  $\tilde Z=\tilde q+i\tilde p$ the Hermitian pairing has real part the Euclidean metric and imaginary part
  the symplectic form, its complex structure is the central $i$, and the cone is the zero-level (degenerate)
  coadjoint orbit (*The Symplectic Form and the Biquaternion Norm Cone*).

## Summary

The zero-divisor article of the twelve structures is the physics of the set of operations a product cannot
invert. The mathematics companion proves that the set is the punctured cone exactly for the four general
products $\mathrm{GPA}$, $\mathrm{GQA}$, $\mathrm{GPS}$ and $\mathrm{GQS}$, that it is the enlarged set
$(\{Q_0=0\}\cup\mathcal{C})\setminus\{0\}$ for the two symmetric structures $\mathrm{SPA}$ and
$\mathrm{SQS}$, and that it is the whole punctured space for the remaining six. Read physically, the four
general products degenerate exactly on the light cone, so their physics is the physics of the cone: the
boundary of invertibility in the composition, the rank drop of the sesquilinear square in the probability,
and the null set of the indefinite metric in the gauge band. The cone splits by the scalar part into the
pure nilpotent displacements and the non-pure multiples of the projectors, the two objects the later
articles of the section own. The two symmetric structures add the pure family to the cone, because a
symmetrised coupling can annihilate two invertible lightlike directions, and the unit $e_1$ is the witness.
The six derived structures have the whole punctured space, because a scalar-valued coupling returns a
number and an antisymmetrised bracket is not a composition. Finally the cone is contained in all twelve
sets and equals four, so masslessness is independent of the product while the ability to compose a
non-lightlike element is not.

Six properties of the set name no product and are gathered in §*The Zero-Divisor Set Beyond the Twelve*.
The cone is where the square is affine and preserves it, the part of the square's critical set on which it
can collapse, and for the parameter zero the idempotents lie on the Julia set of the squaring; the natural
square is the one whose vanishing set is the cone, the largest nontrivial one, while the Born square vanishes only at the origin; the
positivity map $\tilde Q\mapsto\tilde Q^{*}\tilde Q$ sends the units into the interior of the Hermitian cone
and the cone onto its boundary; the cone is a contractible six-real-dimensional manifold whose link is an
$S^{1}$-bundle over $S^{2}\times S^{2}$ with $\pi_2\cong\mathbb{Z}$, complementary to the unit group
$\mathbb{B}^{\times}\simeq S^{1}\times S^{3}$; the quadratic criterion is a feature of the complex signature,
since the split siblings have a linear criterion and a set of two planes; and the pure half of the cone is
the nilpotent cone of real dimension four. The zero-divisor set is therefore at once the light cone, the
edge of the state space, the critical set of the square and the complement of the units.

## Summary of Notation

- $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, basis $e_0=1,e_1,e_2,e_3$, $e_k^{2}=-e_0$, $e_1e_2=e_3$.
- $N(\tilde Q)=\tilde Q\tilde Q^{\natural}=\sum_\mu Q_\mu^{2}$ the biquaternion norm; $\mathcal{C}=\{N=0\}$ the cone, $\mathcal{C}\setminus\{0\}$ the punctured cone.
- ${}^{\natural}$ natural conjugation; $\bar{\cdot}$ coefficient conjugation; ${}^{*}=\bar{\cdot}\circ{}^{\natural}$; $\tilde Q^{\flat}=-\tilde Q^{*}$; $\mathrm{Tr}=2\,\mathrm{Sc}$.
- pure means $Q_0=0$; non-pure means $Q_0\neq0$; a nilpotent is a nonzero element with $\tilde\Upsilon^{2}=0$; an idempotent satisfies $\tilde\Pi^{2}=\tilde\Pi$.
- The twelve structures: GPA, GQA, GPS, GQS the four general products; SPA, SQA, SPS, SQS the symmetric parts; APA, AQA, APS, AQS the antisymmetric parts.
- $\mathbb{M}_\pm$ the anti-Hermitian and Hermitian sectors; $\mathbb{H}_{\mathbb{B}}$ the real-quaternion subspace; $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ the centre.
- $c=1/\sqrt{\epsilon\mu}$ the speed of light in the medium; $\tilde Q=ict\,e_0+\mathbf x$ the material coordinate.

## Further Reading

- The mathematics companion: *Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/zero-divisors-in-the-12-algebraic-structures-over-the-biquaternion-c-space.md`), for the theorem on the twelve sets, the two families and the twelve block criteria.
- The cone in the algebra: *The Light Cone as the Biquaternion Zero-Divisor Cone*; *Zero Divisors as a Physical Locus in Biquaternionic Form*; *The Group of Units of the General Plain Algebra and the Complement of the Zero-Divisor Cone*.
- The boundary of a description: *The Klein Paradox in Biquaternionic Form*, for the central potential shift, the mass gap and the exchange of the two mass-shell roots past it.
- The obstruction that is topological rather than algebraic: *The Magnetic Monopole in Biquaternionic Form*, for the patchwise potential and the Dirac string, the winding as the magnetic charge, the sector split of the electric and magnetic fields, and the quantisation condition that imports $\hbar$.
- The cone as a geometric boundary: *Velocity Space as Hyperbolic Geometry in Biquaternionic Form*, for the light cone as the ideal boundary of hyperbolic velocity space and the ideal points as the non-invertible lightlike elements.
- The comparison of the four general products: *Composition and Probability: the General Plain Algebra and the General Plain Sesqualgebra of Biquaternions Compared*; *The Cone and the Massless Particles in the 12 Structures of Biquaternions over $\mathbb{C}$*.
- The two families: *Square Roots: the Local Complex Structure, the Light Cone and the Mass Shell*; *Idempotents in the 12 Structures of Biquaternions over $\mathbb{C}$*; *Nilpotents in the 12 Structures of Biquaternions over $\mathbb{C}$*; *The Biquaternion Vacuum as a Minimal Idempotent*; *Decoherence as Idempotent Projection*.
- The state and the rank drop: *Mass, Rank and the Positivity of the Dagger*; *The States the Indefinite Metric Cannot Normalise*; *The Bloch Ball as the Trace-One Slice of the Future Light Cone*.
- The metric on the cone: *The Fubini–Study Geometry and the Biquaternion Norm*, for the Fubini–Study metric as the second variation of the biquaternion norm on the null boundary, and the limit that the interior metric is the Bures metric, which the algebra does not supply.
- The information and thermodynamics of the cone: *Causality and the Light Cone as an Information Barrier in Biquaternionic Form*; *Landauer's Principle and the Material–Informational Exchange in Biquaternionic Form*; *Quantum Channels and the Reversible/Irreversible Dichotomy*; *Decoherence as Idempotent Projection*.
- Where the cone sits: *Zero Divisors as a Physical Locus in Biquaternionic Form*, for the momentum-space, configuration-space and state-space images; *Hermitian Forms over the Biquaternion Algebra and the Unitary Witt Group with Hermitian Adjoint*, for the inertia of the Hermitian forms; *The Symplectic Form and the Biquaternion Norm Cone*, for the cone as the isotropy of the holomorphic norm and the characteristic cone of the d'Alembertian, and for the cone as the degenerate zero-level coadjoint orbit whose complex structure is the central $i$.
- The complement, the horizon and the destroyed description: *The Group of Units of the General Plain Algebra and the Complement of the Zero-Divisor Cone*; *Subluminal and Superluminal Electromagnetic Waves and the Lepton Mass Spectrum*; *Black Hole Thermodynamics in Biquaternionic Form*; *Confinement and the Loss of Partonic Information in Biquaternionic Form*; *Gauge Redundancy and the Information in the Gauge Orbit in Biquaternionic Form*.
- The pointwise cone on a curved background: *Curved Spacetime and the Biquaternion Framework*, for the flat, pointwise character of the norm, the rotor action and the light cone, and the field of local cones a curved metric puts in place of the single global one.
- The cone over its directions: *The Celestial Sphere of the Null Cone: Null Directions, Chirality and the Phase*, for the projectivisation of the null cone as the celestial sphere, the transitive Lorentz action, and the Segre quadric of the complexified cone with its two chiral rulings.
- The operators and the units: *The Monoid of Acting Maps: the Process Is the Multiplication, the State Is the Idempotent*; *The Operators of the General Plain Bilinear Product: One-Sided, Two-Sided and the Sandwich*; *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket*.
- The grid: *The 12 Products of the Biquaternion Complex Space*; *The Twelve Structures Compared: Product, Law and Form*; *The Four General Products and Their Physical Readings*.
- The set beyond the twelve: *The Zero Divisors and the Singular Julia Sets* and *The Biquaternion Quadratic Map and Its Julia Sets*, for the square's affine action on the cone, the critical set and the idempotents on the Julia set of the parameter zero; *The Squares and the Positive Cone of the Biquaternion Sesqualgebra*, for the natural square as the largest nontrivial vanishing set; *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint* and *Indefinite Positivity and the Krein Cone of the Biquaternion Algebra*, for the positivity map and the state cone's boundary; *The Topology of the Zero-Divisor Cone*, *Biquaternion Lorentzian and Conformal Geometry* and *The Biquaternion Unit Group as a Topological Group*, for the cone's link and its complementarity with the units; *Split-Biquaternion Zero Divisors* and *Split-Quaternion Zero Divisors*, for the linear criterion and the two planes of the split signature; *List of Zero Divisors and Nilpotents* and *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*, for the nilpotent cone of real dimension four.
- The conventions of the series: *Conventions in the Biquaternion Universe*.
