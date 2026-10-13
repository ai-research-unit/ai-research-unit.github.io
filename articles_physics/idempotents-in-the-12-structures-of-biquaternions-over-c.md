# __Idempotents in the 12 Structures of Biquaternions over $\mathbb{C}$__

## Introduction

An idempotent of a product is an element equal to its own square, $\tilde\Pi\star\tilde\Pi=\tilde\Pi$.
The equation is the algebraic form of a **projection**, and in this framework a projection is a **state**:
an operation that, performed twice, gives the same result as once. The reading is the corpus's own and it is
stated in *The Monoid of Acting Maps: the Process Is the Multiplication, the State Is the Idempotent*: a
process is a multiplication and a determinate state is an idempotent. The idempotent sets of the twelve
structures are therefore the state sets of the twelve bands, and the twelve answers differ in a way that
matters physically. This article is the fifth physics companion of the mathematics comparison group, and
its mathematics companion is *Idempotents in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/idempotents-in-the-12-algebraic-structures-over-the-biquaternion-c-space.md`).

The mathematics companion proves that only five of the twelve structures carry an idempotent other than
$0$ and $e_0$: the general plain structure $\mathrm{GPA}$, its symmetrisation $\mathrm{SPA}$, the general
plain sesquilinear structure $\mathrm{GPS}$, and the general and symmetric quaternionic sesquilinear
structures $\mathrm{GQS}$ and $\mathrm{SQS}$. It proves further that the idempotents of $\mathrm{GPA}$ are
$\tfrac12(e_0+\tilde\Xi i)$ over the roots $\tilde\Xi$ of $-1$, a four-parameter family; that the
idempotents of $\mathrm{GPS}$ are the Hermitian subfamily $\tfrac12(e_0+i\hat\mu)$ over the real unit
vectors; and that the idempotents of $\mathrm{GQS}$ and $\mathrm{SQS}$ are the family $-\tfrac12e_0+\mu$
over the real vectors $\mu$ with $(\mu,\mu)=\tfrac34$. It proves finally that the central square separates
the families: it vanishes on the plain and the Hermitian idempotents, so those are zero divisors of the
algebra, and it equals $e_0$ on the family of the fourth product, so those are units.

Those three facts are three physical statements, and the article reads them.

- The **plain family** is the state family of the composition: every local complex structure, every phase,
  gives a projector. Its Hermitian subfamily is the family of pure states, and its complementation pairs
  the two outcomes of a complete measurement.
- The **Hermitian family** is the pure-state family of the probability band. Its projectors are exactly
  the density matrices of the Bloch ball, in *The Bloch Ball as the Trace-One Slice of the Future Light
  Cone*, and *The Biquaternion Vacuum as a Minimal Idempotent* reads the vacuum as a minimal member.
- The **fourth family** is the one family of idempotents that are units. The states of the probability
  band are null for the composition, and the states of the gauge band are invertible: the contrast is the
  physical content of the central-square theorem, and the owner is *Why Probability Values Are Central:
  the Symmetric Sesquilinear Product and Its Cone* together with *The Fourth Product and Its Indefinite
  Metric*.

**Conventions.** We use those of the companion articles unchanged. The algebra is
$\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$ and $e_k^{2}=-e_0$;
$i$ is central with $i^{2}=-1$. The conjugations are ${}^{\natural}$, $\bar{\cdot}$ and
${}^{*}=\bar{\cdot}\circ{}^{\natural}$. The **central square** is $C(\tilde\Pi)e_0=\tilde\Pi^{\natural}
\tilde\Pi$ with $C(\tilde\Pi)=\sum_\mu\Pi_\mu^{2}$, and the criterion of invertibility is $C\neq0$. The
remarkable subspaces are the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace
$\mathrm{Vect}(\mathbb{B})$, the quaternion and anti-quaternion subspaces $\mathbb{H}_{\mathbb{B}}$ and
$i\mathbb{H}_{\mathbb{B}}$, and the Hermitian and anti-Hermitian subspaces $\mathbb{M}_+$ (informational
sector) and $\mathbb{M}_-$ (material sector). A **minimal idempotent** is one that is nonzero and cannot
be written as the sum of two nonzero orthogonal idempotents.

## The Idempotent as a State

**The equation and the projection.** An idempotent satisfies $\tilde\Pi^{2}=\tilde\Pi$ in the plain
product, and in a general product the same equation is read in that product. The three invariants of an
idempotent are its central square, which decides whether it is a unit or a zero divisor; its
complement $e_0-\tilde\Pi$, which is idempotent whenever the family is closed under the map and which is
orthogonal to it, $\tilde\Pi(e_0-\tilde\Pi)=0$; and the subspace in which it lies.

**The physical reading.** A projection is a yes-no measurement, and an idempotent is the outcome of that
measurement: performing the measurement twice gives the same outcome as performing it once. The equation
$\tilde\Pi^{2}=\tilde\Pi$ is therefore the algebraic form of a **determinate state**, and the nontrivial
idempotents are the determinate states beside the two trivial ones. The reading is the corpus's, and it is
the reason the idempotents are the objects that connect the algebra to the state space: the processes are
the multiplications and the states are the idempotents, in *The Monoid of Acting Maps: the Process Is the
Multiplication, the State Is the Idempotent*.

**The trivial pair.** The origin is an idempotent of every structure, the product being linear, and the
unit $e_0$ is an idempotent of the eight structures that are not antisymmetric. Physically $0$ is the
impossible outcome and $e_0$ is the trivial measurement, the one that keeps every state; the pair is the
degenerate end of the state set.

## The Plain Family: Every Phase Gives a State

**The bijection.** The idempotents of the plain product are $0$, $e_0$ and the elements
$\tfrac12(e_0+\tilde\Xi i)$ over the roots $\tilde\Xi$ of $-1$, and the map
$\tilde\Xi\mapsto\tfrac12(e_0+\tilde\Xi i)$ is a bijection from the roots of $-1$ onto the idempotents.
The classification of the roots, read in *Square Roots of Minus One, Zero and Plus One in the 12
Structures of Biquaternions over $\mathbb{C}$*, splits the family in three: the trivial pair from $\pm i$, the **Hermitian** family
$\tfrac12(e_0+i\hat\mu)$ over the real unit vectors, and the four-parameter **non-trivial** family from the
complex roots, which lies in none of the four four-dimensional subspaces.

**The physical reading.** A local complex structure is a phase, and the bijection says that every phase
gives a state. The state family of the composition is therefore as large as the family of phases: the four
parameters of the non-trivial idempotents are the four real parameters of the complex root, and the
Hermitian subfamily is the part of the family the probability band keeps. The plain idempotents are the
idempotents of the algebra, and they are the states that the composition can prepare; the owner of the
algebra's idempotents and of their parametrisation is *The Biquaternion Vacuum as a Minimal Idempotent*,
and the corpus reads the associated splitting of the algebra in *Ideals and Peirce Decomposition of the
General Plain Algebra* (mathematics). A Peirce decomposition of the algebra by an idempotent is a splitting
of the states into two orthogonal families, and it requires associativity; this is the algebraic reason the
plain product is the band whose states build the whole algebra.

**The symmetrisation keeps the family.** The symmetric plain algebra has the plain square,
$\tilde\Pi\bullet\tilde\Pi=\tilde\Pi^{2}$, so its idempotent set is the plain one element for element. The
physical reading is that the symmetric composition prepares the same states as the composition; the
symmetrisation changes the process, not the states. The pure members of the family are zero divisors of the
symmetrised block, because the vector subspace is its zero-divisor set, so a state that the symmetrisation
prepares is a state the symmetrisation cannot invert: the owner is *The Cone and the Massless Particles in
the 12 Structures of Biquaternions over $\mathbb{C}$*.

## The Hermitian Family: the Pure States and the Bloch Ball

**The family.** The idempotents of the general plain sesquilinear product are $0$, $e_0$ and the Hermitian
family $\tfrac12(e_0+i\hat\mu)$ over the real unit vectors $\hat\mu$, a two-parameter family lying in the
informational sector $\mathbb{M}_+$. The owner is *Idempotents of the General Plain Sesqualgebra*, and the
physics is *Why Probability Values Are Central: the Symmetric Sesquilinear Product and Its Cone*.

**The physical reading.** The Hermitian idempotents are the **pure states** of the probability band. The
element $\tfrac12(e_0+i\hat\mu)$ has a real scalar part and a purely imaginary vector part, which is the
coefficient condition of the informational sector, and the map $\hat\mu\mapsto\tfrac12(e_0+i\hat\mu)$ sends
the real unit sphere onto the family. The corpus reads the family as the extremal points of the positive
cone of the sesquilgebra: the idempotents sit on the boundary of the cone and are the states the pairing
cannot write as a mixture of two others. The Bloch ball, the trace-one slice of the future light cone, is
the convex body they generate, and its extremal points are exactly this family; the owner is *The Bloch
Ball as the Trace-One Slice of the Future Light Cone*. The vacuum is the minimal member, and a pure state
is minimal because it has no orthogonal part: the complementation $\hat\mu\mapsto-\hat\mu$ pairs it with
the state of the opposite direction, and the pair is a complete two-outcome measurement.

**The symmetry of the band keeps the pair.** The symmetric plain sesquilinear product has a scalar-valued
square, so its only idempotents are $0$ and $e_0$: the symmetrisation of the probability form loses all
the nontrivial pure states. The physical reading is that the symmetrised pairing forgets the direction of
the state and keeps only its normalisation, the reduction the companion article records for the root of
$+1$. The pure state exists in the general pairing and not in its symmetrisation.

## The Gauge Family: the Invertible States

**The family.** The idempotents of the general quaternionic sesquilinear product are $0$, $e_0$ and the
family $-\tfrac12e_0+\mu$ over the real vectors $\mu$ with $(\mu,\mu)=\tfrac34$, a two-parameter family
lying in the quaternion subspace $\mathbb{H}_{\mathbb{B}}$. The symmetric quaternionic sesquilinear
structure has the same family. The owner is *Idempotents of the General Quaternionic Sesqualgebra*.

**The physical reading.** The family is the state family of the gauge band, and it is the only nontrivial
family of the twelve whose members are **units** of the algebra. The element $-\tfrac12e_0+\mu$ has a real
scalar part $-\tfrac12$ and a real vector part of squared length $\tfrac34$, so its central square is
$\tfrac14+\tfrac34=e_0$ and it is invertible: the state can be undone. The contrast with the probability
band is exact and is the physics of the central-square theorem. The pure state $\tfrac12(e_0+i\hat\mu)$ has
central square $0$ and is a zero divisor: the state of the band that measures probability is **null** for
the composition. The gauge state $-\tfrac12e_0+\mu$ has central square $e_0$ and is a unit: the state of
the band whose value is an interval is **invertible**. The reading is that a determinate outcome of a
measurement is not a reversible process, while a determinate state of the gauge band is; the owner of the
indefinite metric is *The Fourth Product and Its Indefinite Metric*, and the null states beside it are
*The States the Indefinite Metric Cannot Normalise*.

**The complementation fails.** For the gauge family the map $\mu\mapsto-\mu$ sends $-\tfrac12e_0+\mu$ to
$\tfrac12e_0-\mu$, which is not a member, so the family is not closed under the complementation
$e_0-\tilde\Pi$ and the two-outcome measurement of the plain family has no analogue there. The
two-parameter family of the gauge band has a centre offset from the origin, while the Hermitian family is
centred at $\tfrac12e_0$: the two families are two spheres of different centre and different radius. The
mathematics companion reads the difference, and the physical reading is that the gauge band's state set is
not a convex mixture body of the probability kind; its members are invertible four-vectors of a fixed
length.

## Which Structures Carry a Nontrivial State

Five of the twelve structures carry an idempotent other than $0$ and $e_0$, and each absence is a physical
statement.

- **The four antisymmetric structures have the origin alone.** The two bilinear brackets have an
  identically vanishing square, and the two sesquilinear brackets have a purely imaginary pure vector for a
  square, which forces the origin. Physically a bracket is an infinitesimal transformation, and an
  infinitesimal transformation has no determinate state: the bracket of an element with itself vanishes,
  so it can never equal the element. The owner is *The Operators of the Twelve Structures: Multiplication,
  Adjoint and Bracket*, and the complex witness of the same absence is *A Bracket Invisible on the Real
  Forms: the Complex Witness of the Jacobi Failure*.
- **The natural product and its symmetrisation have the trivial pair alone.** Their square is the central
  square, so an idempotent is central and the equation leaves $0$ and $e_0$. Physically the band whose
  square is the interval produces no determinate state beyond the trivial ones: a state is not an
  interval.
- **The symmetric quaternionic algebra has the trivial pair alone**, for the same reason, its product
  being central-valued.
- **The five structures with a nontrivial state** are the two plain ones, the general plain sesquilinear
  one, and the two quaternionic sesquilinear ones. Physically the states live in the composition band and
  in the two bands of the pairing, and the band of the interval produces none.

## The Twelve Structures at the Idempotents

The idempotent equation is an equation on the square operator, so the twelve idempotent sets are read from
the twelve squares. The twelve are read one by one below, each naming its product, its square and its
idempotent set, before the table collects the twelve states in one place.

### $\mathrm{GPA}$, the general plain algebra — composition

The product is the plain product and its square is the plain square. The idempotents are $0$, $e_0$ and
the family $\tfrac12(e_0+\tilde\Xi i)$ over the roots $\tilde\Xi$ of $-e_0$; the map is a bijection from
the roots of $-e_0$ onto the states, so every phase gives a state. The nonzero idempotents lie on the cone
and are zero divisors, which is the algebraic form of the statement that a measurement has no inverse. The
reading is *The Monoid of Acting Maps: the Process Is the Multiplication, the State Is the Idempotent* and
*Square Roots: the Local Complex Structure, the Light Cone and the Mass Shell*.

### $\mathrm{SPA}$, the symmetric plain algebra — commutativity

The product is the Jordan product and its square is the plain square, so the idempotent set is that of
$\mathrm{GPA}$ element for element. The symmetrised composition prepares the same states, and the reading
is *Observables as a Jordan Algebra: the Symmetric Plain Product and the Classical Composition*.

### $\mathrm{APA}$, the antisymmetric plain algebra — rotation

The product is the commutator, alternating, so its square vanishes identically and the idempotent equation
forces the origin. An infinitesimal transformation has no state. The reading is *The Cross Product as a
Lie Bracket: Rotations and the Jacobi Identity*.

### $\mathrm{GQA}$, the general quaternionic algebra — causality

The product is the natural product and its square is the central element $C(\tilde\Pi)e_0$, so an
idempotent is central and the equation on the centre leaves only $0$ and $e_0$. The band of the interval
carries no nontrivial state. The reading is *The Interval as the Square and the Charge of the Material
Composition*.

### $\mathrm{SQA}$, the symmetric quaternionic algebra — coupling

The product is the scalar-valued symmetrisation, whose square is $C(\tilde\Pi)e_0$, so the idempotent set
is the trivial pair, as for $\mathrm{GQA}$. A central coupling returns a number that cannot be a state.
The reading is *The Quaternion Form as a Product: the Scalar Coupling of Two Material Operations*.

### $\mathrm{AQA}$, the antisymmetric quaternionic algebra — obstruction

The product is the antisymmetrisation, alternating, so its square vanishes identically and the idempotent
set is the origin alone. The reading is *Boosts, Mixed Terms and the Missing Lie Structure*.

### $\mathrm{GPS}$, the general plain sesqualgebra — probability

The product is the pairing and its square is the Hermitian square. The idempotents are $0$, $e_0$ and the
Hermitian family $\tfrac12(e_0+i\hat\mu)$ over the real unit vectors $\hat\mu$, which lies in the
informational sector $\mathbb{M}_+$. Physically these are the pure states, the boundary of the positive
cone and the extremal points of the Bloch ball, and they are zero divisors because a projector has no
inverse. The reading is *Why Probability Values Are Central: the Symmetric Sesquilinear Product and Its
Cone* and *The Bloch Ball as the Trace-One Slice of the Future Light Cone*.

### $\mathrm{SPS}$, the symmetric plain sesqualgebra — positivity

The product is the scalar-valued symmetrisation, so an idempotent is central and the equation on the
centre, $q=\lvert q\rvert^{2}$, leaves the trivial pair. The symmetrised pairing keeps only the trivial
states. The reading is *The Hermitian Form as a Product: Positivity and the Real Part of the Born
Pairing*.

### $\mathrm{APS}$, the antisymmetric plain sesqualgebra — phase

The product is the antisymmetrisation and its square is a purely imaginary pure vector, so an idempotent
has vanishing scalar part and the cross-product term forces the origin. The idempotent set is the origin
alone. The reading is *The Imaginary Part of the Born Pairing: the Antisymmetric Sesquilinear Product*.

### $\mathrm{GQS}$, the general quaternionic sesqualgebra — gauge

The product is the fourth product. The idempotents are $0$, $e_0$ and the family $-\tfrac12e_0+\mu$ over
the real vectors $\mu$ with $(\mu,\mu)=\tfrac34$, a family of units lying in the real-quaternion subspace.
These are the invertible states of the gauge band, the only nontrivial idempotents of the twelve that are
units, which is the contrast with the null pure state of the composition. The reading is *The Fourth
Product and Its Indefinite Metric* and *The States the Indefinite Metric Cannot Normalise*.

### $\mathrm{SQS}$, the symmetric quaternionic sesqualgebra — metric

The product is the symmetric part of the fourth product, and its square is the coefficientwise real part
of $\tilde\Pi^{\natural}\tilde\Pi^{*}$, a real element; the idempotent equation therefore forces
$\tilde\Pi$ real and reduces to $(\tilde\Pi^{\natural})^{2}=\tilde\Pi$, whose set is the family
$-\tfrac12e_0+\mu$, the same as for $\mathrm{GQS}$. The reading is *The Gauge Metric as a Product: the
Symmetric Quaternionic Sesquilinear Product* and *Values in No Subspace: Why the Symmetric Gauge Product
Is Not a State*.

### $\mathrm{AQS}$, the antisymmetric quaternionic sesqualgebra — polarisation

The product is the antisymmetric part of the fourth product and its square is a purely imaginary pure
vector, so the idempotent set is the origin alone. The reading is *The Cross Product of a Vector with Its
Conjugate: the Antisymmetric Gauge Product*.

### The Twelve Idempotent Sets in One Table

The table collects the square of each structure, its idempotent set, the central square of a nontrivial
idempotent and the physical interpretation.

| structure | square | idempotents | central square of the nontrivial family | physical reading |
|---|---|---|---|---|
| GPA | $\tilde\Pi^{2}$ | $0$, $e_0$, $\tfrac12(e_0+\tilde\Xi i)$ | $0$ (zero divisors) | every phase gives a state; the state family of the composition |
| SPA | $\tilde\Pi^{2}$ | the set of GPA | $0$ | the symmetric composition prepares the same states |
| APA | $0$ | $0$ alone | — | an infinitesimal transformation has no state |
| GQA | $C(\tilde\Pi)e_0$ | $0$, $e_0$ | — | the band of the interval has no nontrivial state |
| SQA | $C(\tilde\Pi)e_0$ | $0$, $e_0$ | — | the same |
| AQA | $0$ | $0$ alone | — | an infinitesimal transformation has no state |
| GPS | $\tilde\Pi\tilde\Pi^{*}$ | $0$, $e_0$, $\tfrac12(e_0+i\hat\mu)$ | $0$ (zero divisors) | the pure states, on the boundary of the positive cone and in the Bloch ball |
| SPS | $\mathrm{Sc}(\tilde\Pi\tilde\Pi^{*})e_0$ | $0$, $e_0$ | — | the symmetrised pairing keeps only the trivial states |
| APS | the pure part | $0$ alone | — | an infinitesimal transformation has no state |
| GQS | $\tilde\Pi^{\natural}\tilde\Pi^{*}$ | $0$, $e_0$, $-\tfrac12e_0+\mu$ | $e_0$ (units) | the invertible states of the gauge band |
| SQS | the real part | $0$, $e_0$, $-\tfrac12e_0+\mu$ | $e_0$ (units) | the same family as the general partner |
| AQS | the pure part | $0$ alone | — | an infinitesimal transformation has no state |

Read by column, the table has three kinds of entry: the origin, present in all twelve rows; the unit,
present in the eight rows that are not antisymmetric; and the families, present in the five rows the
mathematics companion classifies. The four families are the plain one, four parameters and all, the
Hermitian one, and the two rows that share the family $-\tfrac12e_0+\mu$. The physics of the table is the
distribution of the states over the bands: the composition carries the largest family, the probability
band carries the pure states, the gauge band carries the invertible states, the interval band and the
brackets carry none.

## The Complementation and the Complete Measurement

For the plain product the map $\tilde\Pi\mapsto e_0-\tilde\Pi$ is the **complementation**: the complement
is idempotent, the two are orthogonal, $\tilde\Pi(e_0-\tilde\Pi)=0$, and they sum to $e_0$. The map is the
antipode of the parameter set, $\tilde\Xi\mapsto-\tilde\Xi$ for the plain family and
$\hat\mu\mapsto-\hat\mu$ for the Hermitian subfamily. The physical reading is a **complete measurement**:
the pair $\{\tilde\Pi,e_0-\tilde\Pi\}$ is a two-outcome measurement whose outcomes exhaust the identity,
and the orthogonality is the statement that the two outcomes are mutually exclusive. The spectral
decomposition of an idempotent is the Peirce splitting $\mathbb{B}=\mathbb{B}\tilde\Pi\oplus
\mathbb{B}(e_0-\tilde\Pi)$, and the physical reading is the splitting of the state space into the two
outcome eigenspaces. For the plain band the complementation pairs the whole family, the four-parameter
part included; for the probability band it pairs the Hermitian family; it fails for the gauge family,
which is not closed under it, and is the exchange of the trivial pair for the natural product.

The pairing of the Hermitian family under $\hat\mu\mapsto-\hat\mu$ is the corpus's antipodal pure state,
and it is the algebraic form of the two outcomes of a spin measurement along a direction: the two states
$\tfrac12(e_0+i\hat\mu)$ and $\tfrac12(e_0-i\hat\mu)$ are the two eigenstates, and the operator that
separates them is the direction $\hat\mu$ itself, a root of $-1$ read as an observable. The owner of the
observable face is *Observables, Gauge Generators and the Chirality of the Internal Action*, and the
complement is the same statement read on the identity.

## What the Idempotent Decides

| claim | source | status |
|---|---|---|
| only five structures carry a nontrivial idempotent | mathematics companion, theorem; recomputed that the Hermitian projector is idempotent in GPA and not in GQS | cited |
| the plain idempotents are $\tfrac12(e_0+\tilde\Xi i)$ over the roots of $-1$ | mathematics companion; recomputed $\tfrac12(e_0+ie_1)^{2}=\tfrac12(e_0+ie_1)$ | verified |
| the Hermitian idempotents have central square $0$ and are zero divisors | mathematics companion; recomputed $C(\tfrac12(e_0+ie_1))=0$ | verified |
| the fourth family $-\tfrac12e_0+\mu$ has central square $e_0$ and is a family of units | mathematics companion; recomputed with $(\mu,\mu)=\tfrac34$ | verified |
| the complementation $e_0-\tilde\Pi$ is idempotent, orthogonal and sums to the identity | mathematics companion; recomputed for the Hermitian idempotent | verified |
| the families lie in the centre, $\mathbb{M}_+$, $\mathbb{H}_{\mathbb{B}}$ and no remarkable subspace | mathematics companion; the coefficient conditions are read in the text | cited |
| the physical readings (state, pure state, Bloch ball, gauge state, two-outcome measurement, decoherence, Bell basis, vacuum, entropy, coarse-graining, polarisation) | this article; owners cited in the text | interpretation |
| the classical part of a correlation is a convex combination of idempotents; the discord is the rest | *Quantum Discord and Correlations Beyond Entanglement in Biquaternionic Form* | cited |
| the rank-one idempotent makes a minimal left ideal, the algebra's unique spinor carrier | *Higher Spin from Tensor Products: Why the Biquaternion Algebra Admits Only Spin 0 and One-Half* | cited |
| the entangled resource of teleportation is a Bell idempotent, the corrections are unitaries | *Quantum Teleportation in Biquaternionic Form* | cited |

## The States in the Physics Corpus

The idempotents are the states, and the corpus has already written the biography of a state: it is a point
of a ball, it is deformed by decoherence, it is the outcome of a measurement, it is a vector of a GNS
space, and one of its minimal members is the vacuum. The readings below are those articles, restated for
the idempotent table.

**A state is a point of the Bloch ball.** *The Bloch Ball as the Trace-One Slice of the Future Light Cone*
identifies the state space with the trace-one slice of the cone, a ball whose sphere is the pure states,
and the idempotent condition is the boundary condition $\lvert\mathbf r\rvert=1$. *The Generalized Bloch
Ball for Spin 1 in the Biquaternion Framework* extends the picture and marks the ceiling of the framework;
the lesson for the idempotent table is that each structure cuts a convex body of states, and the Hermitian
family is the one whose body has been named.

**Decoherence moves a state off the idempotent family.** *Decoherence as Idempotent Projection* shows that
a pure state is an idempotent and that the dephasing channel deforms it into a positive trace-one element
that is not idempotent, the deviation being the scalar $(\lvert\mathbf r\rvert^{2}-1)/4$. The idempotent
family is therefore the *pure* end of the state family, and an idempotent is a state that has not
decohered. The Jordan idempotent is the algebra's name for the undivided state, and the mixed states of the
ball are exactly the states that are not idempotents.

**A measurement has idempotents for outcomes.** *The Measurement Problem in Algebraic Form* and *Quantum
Channels and the Reversible/Irreversible Dichotomy* read the sandwich
$\tilde\rho\mapsto\tilde P\tilde\rho\tilde P$ as the projective measurement, with the idempotent
$\tilde P$ one outcome and the complement $e_0-\tilde P$ the other. The complementation of this article is
the algebra's two-outcome event: the pair $(\tilde P,e_0-\tilde P)$ is a complete measurement, and the
failure of the complementation for the gauge family says that a gauge idempotent does not by itself define
a two-outcome test. *POVMs and the Positive Cone in Biquaternionic Form* places the idempotents at the
extreme points of the positive cone, so the projective measurement is the sharp end of the general
measurement.

**An idempotent is also a basis vector of a composite.** *The Bell Basis as the Idempotent Basis of
$\mathbb{B}\otimes\mathbb{B}$* uses the idempotents of the tensor square as a basis of the two-qubit space:
the four Bell projectors are idempotent, orthogonal and complete, and they diagonalise the maximally
entangled states. The idempotent therefore does two jobs at once, as a pure state of one system and as a
basis element of the correlations of two, and the tensor-product article is where the two jobs are visibly
the same.

**The vacuum is a minimal idempotent.** *The Biquaternion Vacuum as a Minimal Idempotent* identifies the
one-mode vacuum with the minimal idempotent $\tilde\Pi_1=\tfrac12(e_0+ie_3)$, of trace one, which generates
the minimal left ideal that is the one-particle module. Three properties of the table meet in it: it is a
state, so it is Hermitian; it is minimal, so it is an extreme point of the state set; and it is a zero
divisor, so it is in the non-pure family of the cone. The vacuum-manifold observation of that article —
every unit vector $\hat\mu$ gives a vacuum and the algebra singles none out — is the statement that the
table has a sphere of vacua and no preferred point, which is the framework's standing disclaimer about
selection. *The GNS Construction in the Biquaternion Framework* recovers the same idempotent from the
state's null space, so the minimal idempotent, the vacuum vector and the one-particle module are three
descriptions of one object.

## Entropy, Coarse-Graining and the Vacuum Energy

The idempotents are the pure states, and the corpus has a second, quantitative way of saying what that
means: the idempotents are exactly the states of zero entropy, and every other state lies at a definite
distance from them. The same section collects the further objects the pure states carry: the vacuum energy,
the coarse-graining maps and the polarisation sphere.

**The deviation from idempotency is the entropy coordinate.** *Von Neumann Entropy and the Biquaternion
Norm* and *Coarse-Graining and the Biquaternion Entropy Functional* compute the deviation from idempotency
of a state $\tilde\rho=\tfrac12(e_0+i\mathbf r)$ and find it to be a single scalar,

$$
\mathrm{Sc}\bigl(\tilde\rho^{2}-\tilde\rho\bigr)=\tfrac14\bigl(\lvert\mathbf r\rvert^{2}-1\bigr)
=-N(\tilde\rho),
$$

so that purity, idempotency and the vanishing of the biquaternion norm are three interpretations of one
number. The entropy is a strictly monotone function of that number: it **vanishes on the idempotents**,
is maximal at the centre of the ball, and leaves the idempotent family with infinite slope, because the
logarithm of a state is singular exactly where the state is idempotent. The idempotent family is therefore
the **zero-entropy boundary** of the state space, and the entropy is the coordinate that measures the
distance from it. This is the sharpest statement of what an idempotent is physically: a determinate state
is a state of no missing information, and it is an idempotent because repeating a determinate measurement
changes nothing.

**A coarse-graining is itself an idempotent map.** The coarse-grainings of *Coarse-Graining and the
Biquaternion Entropy Functional* are the trace-preserving, completely positive, **idempotent** maps
$\Phi$ with $\Phi^{2}=\Phi$ onto a commutative subalgebra, of which the fully dephasing channel is the
example. Idempotency therefore appears twice in the framework, at two levels: an idempotent **element** is
a pure state, and an idempotent **map** is a coarse-graining. Both satisfy the same equation $\Pi^{2}=\Pi$,
and the two are related by the fact that a coarse-graining contracts the Bloch ball toward its centre,
moving every state off the idempotent family and increasing the entropy. The second law of the sector is
the statement that the image of a state under a coarse-graining is never closer to the idempotent family
than the state itself.

**The idempotents contain the perfectly distinguishable pairs.** *Relative Entropy and the Biquaternion
Framework* develops the Umegaki quantity $S(\rho\|\sigma)$ and its monotonicity under every physical
process. Two **orthogonal** idempotents are separated with certainty by a single projective measurement,
and their relative entropy diverges, because neither lies in the support of the other; two non-orthogonal
idempotents are separated only probabilistically, and a pair in which at least one member is mixed is
separated no better. The idempotent family therefore contains the pairs a single measurement can tell
apart, and the ball around it is where the distinction is only statistical.

**The idempotents are the perfectly resolvable states.** The entropy says how much information a state
lacks; *Fisher Information and the Biquaternion Norm* says how sharply a state can be told from its
neighbours, and the two readings agree through a **reciprocity**. The classical Fisher information of the
state's spectral family, with respect to the Bloch radius, is the reciprocal of the biquaternion norm,

$$
g_{rr}=\frac{1}{1-|\mathbf{r}|^{2}}=\frac{1}{4\,\mathrm{Sc}\,N(\tilde\rho)} .
$$

It is minimal at the maximally mixed state, where the norm is largest, and it **diverges on the
boundary**, where the norm vanishes. By the Cramér–Rao bound a divergent information means asymptotic
exactness, so the idempotents are exactly the states a displacement of which can be detected with
arbitrarily high precision. The Fisher article names the coincidence: the analytic singularity of the
logarithm, the vanishing of the biquaternion norm and the divergence of the Fisher information are three
descriptions of the same locus. The idempotent is therefore overdetermined in the corpus — the pure state,
the zero-entropy state, the zero-divisor state and the perfectly resolvable state are four names for one
element.

**The vacuum idempotent carries the zero-point energy.** *The Vacuum State and the Casimir Effect in
Biquaternionic Form* identifies the vacuum with the one-mode state of no particles, which is the minimal
idempotent $\tilde\Pi_1=\tfrac12(e_0+ie_3)$ of *The Biquaternion Vacuum as a Minimal Idempotent*, and
records that the state costs half a quantum of energy per mode. The idempotent is the state of the field
when nothing is excited, and the normal-ordering prescription removes the absolute sum while leaving the
**difference** produced by boundary conditions: the Casimir energy. The idempotent therefore carries a
physical energy that is not read off its own algebra — the half-quantum per mode and the cutoff are
standard-theory data — and the framework's role is to house the state and the indefinite metric that fixes
the count of modes.

**Idempotent states are spin-$\tfrac12$, and a scalar escapes them.** The idempotent-as-state reading has a
scope, and *The Scalar Field in the Centre: Why Spin 0 Escapes the Biquaternion State Module* fixes it. The
framework's states are elements of the module $\mathbb{B}\tilde\Pi\cong\mathbb{C}^2$, which carries the
defining two-dimensional representation, so they are **spinor-like by construction**; a spin-$0$ field, being
a single component transforming in the trivial representation, has no place in it. The article gives the
reason and it is a module-theoretic one: the state module is the defining module of the matrix algebra
$M_2(\mathbb{C})$, a simple algebra has only one kind of module, and every finite-dimensional module is a
direct sum of copies of $\mathbb{C}^2$, so no one-dimensional module exists for the trivial representation
to occupy. The scalar lives instead in the **centre** $\mathbb{C}_{\mathbb{B}}=\{Q_0e_0\}$, which is not a
module at all but the rotationally invariant subalgebra, the fixed space of the rotation subgroup. The
idempotents of this article are therefore states of the spin-$\tfrac12$ module only: the Bloch sphere, the
polarisation sphere and the state cone are the same object because the state is spinorial, and a scalar
field is described by the centre's complex line rather than by any idempotent of $\mathbb{M}_+$.

**The sphere of pure states.** The idempotents of the probability band are the boundary sphere of the
Bloch ball, and *Pancharatnam's Phase and the Polarization Sphere in Biquaternionic Form* reads the same
sphere as the polarisation sphere: a fully polarised wave is a point of the sphere, and a partially
polarised one is a point of the ball. *The Bloch Ball as the Trace-One Slice of the Future Light Cone*
completes the pair of readings, so one object — the sphere of idempotents of $\mathbb{M}_+$ — is at once
the sphere of pure qubit states, the sphere of pure polarisations and the boundary of the state cone.
Idempotency is the algebraic name of the sphere.

**The idempotents are the sharp effects, and a general measurement softens them.** *POVMs and the Positive
Cone in Biquaternionic Form* locates the idempotents in measurement theory exactly. The effects — the
elements between $0$ and $e_0$ — form a convex body, the operator interval, and its **extreme points are
exactly the idempotents**, the identity and the rank-one projectors; a projective measurement uses only
these extreme effects, while a general positive-operator-valued measure uses interior, "soft" effects that
are convex combinations $\tilde E=t\tilde\Pi_1+(1-t)\tilde\Pi_2$ of orthogonal idempotents and respond
partially to both alternatives. The idempotent is thus the **sharp** outcome, and every other outcome is a
mixture of sharp ones. The article adds the reason the idempotent picture is not lost: by Naimark's
dilation theorem every POVM is the compression of a projective measurement on a larger module, so the
general effects are replaced by orthogonal idempotents once an ancillary factor is adjoined and traced out.

**The two kinds of time evolution are one bilinear operation.** *The Measurement Problem in Algebraic Form*
states the disciplined version of the collapse. In the framework both a unitary evolution and a measurement
update are the **same bilinear operation** $\tilde Q\mapsto\tilde A\tilde Q\tilde A^{*}$, applied with an
acting element of one of two algebraic types: unitary, $\tilde A\tilde A^{*}=e_0$, or Hermitian idempotent,
$\tilde A^{2}=\tilde A=\tilde A^{*}$. Idempotent and unitary are therefore the two classes of acting element
of one operation form, and the measurement problem becomes the absence of a rule fixing which class applies
when. The article is explicit that this is a restatement and not a solution, and the idempotent's place in
it is exact: it is the class of acting element that produces a definite outcome.

**The idempotent is the algebra's native qubit.** *The Native Qubit and the Defining Module of the
Biquaternion Algebra* identifies the elementary informational carrier as the algebra's own simple module
$S$, and the identification runs through the idempotents. A complex two-dimensional space is not chosen and
then equipped with operators; it is the object an algebra isomorphic to $M_2(\mathbb{C})$ is a matrix algebra
*of*, and the article records the two facts that make "native" precise: the simple module is unique up to
isomorphism, and the algebra's left regular module is two copies of it. On that module the states are placed
by the rank-one idempotents — the article's own statement is that **the rank-one projectors on $S$ are
exactly the idempotents of $\mathbb{M}_+$ that have trace one** — and the trace pairing becomes the
Hilbert-space inner product. The reading sharpens the companion's central claim: the idempotents are not one
convenient representative of the state; they are the rays of the only elementary carrier the algebra
possesses, so the pure states of the framework are native in the same sense in which the qubit is.

**The idempotents are the atoms a context assigns.** *Contextuality and the Kochen–Specker Theorem in
Biquaternionic Form* shows what the idempotents do when several observables are measured together. A
**context** is a maximal commuting set of Hermitian elements, generated by commuting involutions, and its
spectral resolution is a complete family of orthogonal idempotents summing to $e_0$; a noncontextual value
assignment restricts to each context as an algebra homomorphism and takes the values $\{0,1\}$ on the
idempotents, exactly one per context being $1$. The Kochen–Specker theorem is the statement that no such
assignment exists once the defining module has dimension at least three, so the idempotents are not only the
determinate states of a single measurement but the **atoms of every context**, and contextuality is the
failure of a global $\{0,1\}$ labelling of them. The framework's own boundary is stated in the article: the
native module is two-dimensional, the obstruction there is empty, and the smallest arena in which it appears
is the two-qubit algebra $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$, where the Mermin–Peres magic
square forces a noncontextual assignment to make the product of the same nine entries both $+1$ and $-1$.

**A protected subspace is an idempotent's image.** *Quantum Error Correction and the Stabilizer Formalism in
Biquaternionic Form* puts the idempotent to a second job, beyond naming a state. A code is specified by an
abelian group of commuting involutions of $\mathbb{M}_+^{\otimes n}$ — the stabilizer group — and the code
space is the common $+1$ eigenspace, which is the **image of the code projector**
$\tilde\Pi=|S|^{-1}\sum_{\tilde g\in S}\tilde g$, itself an idempotent of the tensor-product algebra. The
article's structural finding is that the whole theory of stabilizer codes is a theory of **commutative
subalgebras and their idempotents**: the code space is a **Peirce component** of a commutative subalgebra,
and the syndrome measurement projects onto its idempotents. The correction is algebraic too: the
Knill–Laflamme condition says an error set is correctable exactly when
$\tilde\Pi\tilde E_a^{*}\tilde E_b\tilde\Pi=c_{ab}\tilde\Pi$ — the errors, sandwiched by the code idempotent,
act on that Peirce component as scalars. The reading is a genuine extension of the companion's picture. The
idempotent is not only the algebra's **native qubit** and the sharp outcome of a single measurement; a
commutative family of idempotents cuts out a **subspace protected from a class of errors**, and the
conditions for protection are conditions on how the idempotent absorbs those errors. Projection, which the
companion reads as the irreversible loss of coherence, is here the constructive move that defines the code
and diagnoses a syndrome.

**A family of idempotent bases is a complete measurement.** *Mutually Unbiased Bases and the Biquaternion
Algebra* turns the idempotent into a tomographic tool. A basis of rays is a complete orthogonal family of
rank-one idempotents, $\tilde\Pi_i\tilde\Pi_j=\delta_{ij}\tilde\Pi_i$ and $\sum_i\tilde\Pi_i=e_0$, and two
bases are **mutually unbiased** when the trace pairing between idempotents of different bases is exactly
$1/d$. For the native qubit the maximal set of $d+1=3$ unbiased bases has a clean algebraic origin: they are
the eigenbases of the three imaginary units $ie_1,ie_2,ie_3$, pairwise anticommuting involutions, and the
three bases are the three coordinate measurements whose outcome probabilities **determine the state**, the
tomographic statement. The companion's picture gains a second dimension: the idempotents of one basis are
the sharp outcomes of one measurement, and the **incompatibility** of two measurements is the size of the
overlap of their idempotents, $1/d$ being maximal ignorance. The article is exact about the ceiling too: on
two qubits the maximum is five bases, the tensor product of qubit bases supplies only three, and the Bell
basis — a natural idempotent basis of $\mathbb{B}\otimes\mathbb{B}$ — is **not** unbiased with respect to
the product basis, so the obstruction to a full set is visible in the idempotents themselves.

**Chirality's projectors are idempotents, and the radicand is dimension-dependent.** *Bosonization in
Biquaternionic Form* records a fact that belongs to this companion's ledger. The chiral projectors
$\tilde\Pi_{L,R}=\tfrac12(1\pm\gamma^5)$ are idempotents that split a spinor into its two chiralities, and
their existence *as projectors* depends on the square of $\gamma^5$: the article records
$(\gamma^5)^2=+I_2$ in two dimensions whereas $(\gamma^5)^2=-I_4$ in four. In two dimensions $\gamma^5$ is
therefore a **real structure** (a root of $+1$), the chiral projectors have real eigenspaces, and an
irreducible two-component
spinor is a sum of two real (Majorana–Weyl) spinors; in four dimensions it is a **complex structure** (a root
of $-1$), and the splitting is complex. The reading is that the idempotent is not a dimension-free object:
the same formal projector has real or complex eigenspaces according to which radicand the chirality operator
realises, and the framework's idempotent-as-state picture inherits that dependence at the level of the
chirality splitting.

## Physical Interpretation

- An idempotent is a projection, and a projection is a determinate state: measuring twice gives the same
  result as measuring once. The idempotent sets are the state sets of the twelve bands.
- The plain product carries the largest family, one state per local complex structure, so every phase
  gives a state. The trivial pair is the impossible outcome and the trivial measurement.
- The Hermitian idempotents are the pure states of the probability band, on the boundary of the positive
  cone, and the Bloch ball is the convex body they generate. The vacuum is a minimal member.
- The gauge family is the only nontrivial family of idempotents that are units. The pure state of the
  probability band is null for the composition; the gauge state is invertible. A determinate outcome of a
  measurement is not a reversible process; a determinate state of the gauge band is.
- The complementation pairs a state with its orthogonal complement, and the pair is a complete
  two-outcome measurement. It pairs the plain family and the Hermitian family and fails for the gauge
  family.
- The brackets and the interval band carry no nontrivial state: an infinitesimal transformation has no
  determinate state, and a state is not an interval.
- The idempotent is the state of *The Bloch Ball as the Trace-One Slice of the Future Light Cone*, the
  outcome of the measurement of *The Measurement Problem in Algebraic Form*, the basis element of *The
  Bell Basis as the Idempotent Basis of B⊗B*, and the minimal vacuum of *The Biquaternion Vacuum as a
  Minimal Idempotent*; decoherence, read in *Decoherence as Idempotent Projection*, is the passage off the
  idempotent family.
- The idempotents are the zero-entropy states: the deviation
  $\mathrm{Sc}(\tilde\rho^{2}-\tilde\rho)=\tfrac14(\lvert\mathbf r\rvert^{2}-1)$ is minus the biquaternion
  norm, and the entropy is a monotone function of it that vanishes exactly on the idempotents. The sphere
  of idempotents of $\mathbb{M}_+$ is at once the pure-qubit sphere, the polarisation sphere and the
  boundary of the state cone.
- Idempotency occurs at two levels. An idempotent element is a pure state; an idempotent map $\Phi^{2}=\Phi$
  is a coarse-graining, and a coarse-graining increases the entropy by moving every state off the
  idempotent family.
- The idempotents are the algebra's **native** states. *The Native Qubit and the Defining Module of the
  Biquaternion Algebra* shows that the elementary carrier is the algebra's unique simple module, and that its
  rays are exactly the trace-one idempotents of $\mathbb{M}_+$; the trace pairing is the Hilbert-space inner
  product. The state is not one convenient representative among many but the only elementary carrier's rays.
- The idempotents are the atoms of a **context**. A maximal commuting set of Hermitian elements resolves into
  a complete family of orthogonal idempotents, and contextuality is the failure of a global $\{0,1\}$
  valuation of them (*Contextuality and the Kochen–Specker Theorem in Biquaternionic Form*). The obstruction
  is empty for the native two-dimensional module and appears first for two qubits, in the Mermin–Peres magic
  square.
- The vacuum idempotent carries the zero-point energy: half a quantum per mode, with the Casimir energy the
  boundary-condition-dependent difference that normal ordering leaves behind.
- The idempotents are also the perfectly resolvable states: the Fisher information of the state with
  respect to the Bloch radius is the reciprocal of the biquaternion norm, so it diverges exactly on the
  idempotents. The pure state, the zero-entropy state, the zero-divisor state and the perfectly resolvable
  state are four names for one element.
- The idempotents are the **sharp** effects, the extreme points of the operator interval $[0,e_0]$, and a
  general POVM uses interior "soft" effects, convex combinations $t\tilde\Pi_1+(1-t)\tilde\Pi_2$ of
  orthogonal idempotents; by Naimark's dilation theorem every such measurement is a projective one on a
  larger module. In *The Measurement Problem in Algebraic Form* the idempotent and the unitary are the two
  classes of acting element of one bilinear operation $\tilde Q\mapsto\tilde A\tilde Q\tilde A^{*}$, the
  idempotent being the class that produces a definite outcome.
- Only the sesquilinear product supplies the cone, and with it the state space. *Why the Fourth Product Is a
  Gauge Structure and Not a State Space* shows that the fourth product's ternary structure fails the
  Jordan triple identity, so no cone and no pure states can be rebuilt from it; the idempotents-as-states
  are the gift of the positive pairing alone.
- The state is spinorial, so the idempotent-as-state reading is a spin-$\tfrac12$ reading: a spin-$0$ scalar
  lives in the centre and escapes the state module, because a simple matrix algebra has no
  one-dimensional module for the trivial representation.
- An idempotent also defines a protected subspace. In *Quantum Error Correction and the Stabilizer Formalism
  in Biquaternionic Form* the code space is the image of an idempotent (the code projector), a Peirce
  component of a commutative subalgebra of involutions; the syndrome measurement projects onto idempotents,
  and the Knill–Laflamme condition says errors are correctable exactly when their products, sandwiched by the
  code idempotent, act as scalars on it.
- Idempotent bases are measurement bases. In *Mutually Unbiased Bases and the Biquaternion Algebra* the three
  maximal unbiased bases of the qubit are the eigenbases of $ie_1,ie_2,ie_3$, the trace pairing between
  idempotents of different bases is $1/d$, the $d+1$ bases reconstruct the state, and the two-qubit Bell
  basis is not unbiased with respect to the product basis.
- Chirality's projectors are idempotents whose eigenspaces' reality is dimension-dependent:
  $(\gamma^5)^2=+I_2$ in two dimensions (a real structure, Majorana–Weyl splitting) and $(\gamma^5)^2=-I_4$
  in four (*Bosonization in Biquaternionic Form*).
- The idempotents separate the classical from the quantum in a correlation. In *Quantum Discord and
  Correlations Beyond Entanglement in Biquaternionic Form* a local projective measurement is a family of
  idempotents, and the classical mutual information is the part of the correlation such a measurement can
  extract; the discord is the rest, zero exactly for the states that are classically correlated. The
  Bell-diagonal states are the convex combinations of the four Bell idempotents, so the classical part of a
  bipartite state is what a convex combination of idempotents carries, and the discord is the correlation
  that no idempotent basis resolves.
- The state's carrier is a **minimal left ideal**, and that is why the algebra carries only spin $0$ and spin
  $\tfrac12$. In *Higher Spin from Tensor Products: Why the Biquaternion Algebra Admits Only Spin 0 and
  One-Half* a rank-one idempotent $e$ makes the left ideal $\mathbb{B}e$ minimal — it contains no smaller
  nonzero left ideal — of complex dimension two, so it is the algebra's unique irreducible carrier, the
  spinor module; the idempotent also decomposes the algebra itself. The module category has a single
  isomorphism class of simple objects, so every module is a sum of copies of that two-dimensional one, and the
  spin content of any module is a finite number of copies of spin $\tfrac12$: spin zero sits in the centre and
  in the invariants of products, and higher spin exists only in tensor powers, to be extracted by constraints.
- An idempotent is a measurement resource and a unitary is a gate; the corpus keeps the two apart. In
  *Quantum Teleportation in Biquaternionic Form* the entangled resource and the Bell measurement are the four
  Bell idempotents of $\mathbb{B}\otimes\mathbb{B}$ — "idempotent and Hermitian, but not unitary" — while the
  corrections are unitary elements, and the protocol is "a controlled collision between two kinds of object
  that the framework elsewhere keeps apart": the idempotents that resolve a measurement and the unitaries
  that generate reversible motion. The same elements $e_k$ enter the resource as $e_k\otimes e_k$ and the
  correction gates as $ie_k$, and the two behave quite differently.

## Summary

An idempotent is an element equal to its own square, the algebraic form of a projection and, in this
framework, of a determinate state. The mathematics companion proves that only five of the twelve
structures carry a nontrivial idempotent: the general plain structure and its symmetrisation, with the
family $\tfrac12(e_0+\tilde\Xi i)$ over the roots of $-1$, one state per phase; the general plain
sesquilinear structure, with the Hermitian family $\tfrac12(e_0+i\hat\mu)$ over the real unit vectors, the
pure states of the probability band, on the boundary of the positive cone and the extremal points of the
Bloch ball; and the two quaternionic sesquilinear structures, with the family $-\tfrac12e_0+\mu$ over the
real vectors of squared length $\tfrac34$, the states of the gauge band. The central square separates the
families: it vanishes on the plain and the Hermitian idempotents, which are therefore zero divisors, and
it equals $e_0$ on the gauge family, which is therefore a family of units. The physics of that separation
is the contrast between the band that measures a probability, whose determinate states are null and cannot
be composed, and the band whose value is an interval, whose determinate states are invertible. The
complementation $\tilde\Pi\mapsto e_0-\tilde\Pi$ pairs a state with its orthogonal complement and makes a
complete two-outcome measurement; it pairs the plain family and the Hermitian family and fails for the
gauge family. The four brackets carry the origin alone, because an infinitesimal transformation has no
determinate state, and the interval band carries only the trivial pair, because a state is not an
interval.

## Summary of Notation

- $\tilde\Pi$ an idempotent, $\tilde\Pi\star\tilde\Pi=\tilde\Pi$; the trivial pair $0$ and $e_0$.
- $C(\tilde\Pi)e_0=\tilde\Pi^{\natural}\tilde\Pi$ the central square; $C\neq0$ is the criterion of invertibility.
- $\tilde\Xi$ a root of $-1$; $\hat\mu$ a real unit vector; the families $\tfrac12(e_0+\tilde\Xi i)$, $\tfrac12(e_0+i\hat\mu)$ and $-\tfrac12e_0+\mu$ with $(\mu,\mu)=\tfrac34$.
- The complementation $\tilde\Pi\mapsto e_0-\tilde\Pi$, with $\tilde\Pi(e_0-\tilde\Pi)=0$; the Peirce splitting $\mathbb{B}=\mathbb{B}\tilde\Pi\oplus\mathbb{B}(e_0-\tilde\Pi)$.
- The remarkable subspaces: the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion and anti-quaternion subspaces $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, and the Hermitian and anti-Hermitian ones $\mathbb{M}_+$, $\mathbb{M}_-$.
- The twelve structures: GPA, GQA, GPS, GQS general; SPA, SQA, SPS, SQS symmetric; APA, AQA, APS, AQS antisymmetric.

## Further Reading

- The mathematics companion: *Idempotents in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/idempotents-in-the-12-algebraic-structures-over-the-biquaternion-c-space.md`), for the twelve sets, the central-square theorem and the complementation.
- The state reading of a process: *The Monoid of Acting Maps: the Process Is the Multiplication, the State Is the Idempotent*; *The Operators of the General Plain Bilinear Product: One-Sided, Two-Sided and the Sandwich*; *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket*.
- The plain family and the algebra's idempotents: *The Biquaternion Vacuum as a Minimal Idempotent*; *Ideals and Peirce Decomposition of the General Plain Algebra* (mathematics).
- The pure states and the Bloch ball: *Why Probability Values Are Central: the Symmetric Sesquilinear Product and Its Cone*; *The Bloch Ball as the Trace-One Slice of the Future Light Cone*; *The Hermitian Subspace M₊ as the Informational Sector*; *The Anti-Hermitian Subspace M₋ as the Material Sector*.
- The gauge family and the indefinite metric: *The Fourth Product and Its Indefinite Metric*; *The States the Indefinite Metric Cannot Normalise*; *Idempotents of the General Quaternionic Sesqualgebra* (mathematics).
- The observable face: *Observables, Gauge Generators and the Chirality of the Internal Action*.
- The states in the physics corpus: *The Bloch Ball as the Trace-One Slice of the Future Light Cone*; *The Generalized Bloch Ball for Spin 1 in the Biquaternion Framework*; *Decoherence as Idempotent Projection*; *The Measurement Problem in Algebraic Form*; *POVMs and the Positive Cone in Biquaternionic Form*; *The Bell Basis as the Idempotent Basis of B⊗B*; *The GNS Construction in the Biquaternion Framework*; *Quantum Channels and the Reversible/Irreversible Dichotomy*; *The Native Qubit and the Defining Module of the Biquaternion Algebra*, for the idempotents as the rays of the algebra's unique simple module; *The Scalar Field in the Centre: Why Spin 0 Escapes the Biquaternion State Module*, for the spinor scope of the state.
- The roots that parametrise the plain family: *Square Roots of Minus One, Zero and Plus One in the 12 Structures of Biquaternions over $\mathbb{C}$*; *Idempotents of the General Plain Algebra* (mathematics).
- The entropy, the coarse-graining and the vacuum energy: *Von Neumann Entropy and the Biquaternion Norm*; *Coarse-Graining and the Biquaternion Entropy Functional*; *Relative Entropy and the Biquaternion Framework*; *Fisher Information and the Biquaternion Norm*, for the resolution floor on the state; *The Vacuum State and the Casimir Effect in Biquaternionic Form*; *Pancharatnam's Phase and the Polarization Sphere in Biquaternionic Form*; *Entanglement Entropy and the Replica Trick in Biquaternionic Form*.
- Why the state space needs the sesquilinear product: *Why the Fourth Product Is a Gauge Structure and Not a State Space*; *Values in No Subspace: Why the Symmetric Gauge Product Is Not a State*.
- The contexts and the obstruction: *Contextuality and the Kochen–Specker Theorem in Biquaternionic Form*, for the idempotent resolution of a context and the $\{0,1\}$ valuation that contextuality forbids.
- The idempotent as a protected subspace: *Quantum Error Correction and the Stabilizer Formalism in Biquaternionic Form*, for the code space as the image of an idempotent Peirce component and the Knill–Laflamme condition on the code idempotent.
- The idempotents and the classical–quantum split of a correlation: *Quantum Discord and Correlations Beyond Entanglement in Biquaternionic Form*, for a projective measurement as a family of idempotents, the Bell idempotent basis, and the discord as the correlation no idempotent basis resolves.
- The idempotent's ideal and its separation from the unitary: *Higher Spin from Tensor Products: Why the Biquaternion Algebra Admits Only Spin 0 and One-Half*, for the minimal left ideal as the algebra's unique spinor carrier and the spin content of its modules; *Quantum Teleportation in Biquaternionic Form*, for the Bell idempotents as the entangled resource and the unitary corrections kept apart from them.
- The idempotent as a measurement basis and a chiral projector: *Mutually Unbiased Bases and the Biquaternion Algebra*, for the idempotent bases, the $1/d$ trace pairing and the $d+1$ tomographic bases; *Bosonization in Biquaternionic Form*, for the chiral projectors and the dimension-dependent square of $\gamma^5$.
- The brackets: *A Bracket Invisible on the Real Forms: the Complex Witness of the Jacobi Failure*; *A Higher Structure for the Jacobi Failure*.
- The grid and the definitions: *The 12 Products of the Biquaternion Complex Space* (mathematics); *The Twelve Structures Compared: Product, Law and Form*; *Definitions for the Study of the 12 Algebraic Structures* (mathematics); *Conventions in the Biquaternion Universe*.
