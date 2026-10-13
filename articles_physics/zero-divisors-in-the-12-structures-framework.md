# __Zero Divisors in the 12 Structures Framework__

## Introduction

The comparison section of the physics menu mirrors the comparison group of the mathematics menu: the twelve
structures of the biquaternion complex space read against one subject at a time. The mathematics group opens
with *Zero Divisors*, and this article is its physics companion. The subject is the set of elements that a
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
Framework* the annihilator planes, *Square Roots of Minus One, Zero and Plus One in the 12 Structures
Framework* the roots of $0$, *Square Roots of a General Element in the 12 Structures Framework* the general
radicand, *Idempotents in the 12 Structures Framework* the non-pure family, and *Nilpotents in the 12
Structures Framework* the square-zero class.

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
plain-row criterion of *Biquaternion Norm and Invertibility*, and it is the one criterion of the four
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
  belongs to *Nilpotents in the 12 Structures Framework* and to *Square Roots of Minus One, Zero and Plus
  One in the 12 Structures Framework*.
- The **non-pure** family, $Q_0\neq0$. Its square is $\tilde Q^{2}=2Q_0\tilde Q-N(\tilde Q)e_0=2Q_0\tilde Q$,
  so the rescaled element $\tilde\Pi=\tilde Q/(2Q_0)$ is a nontrivial idempotent. These are the
  **idempotent multiples**, the multiples of the projectors. The non-pure family fills the cone in real
  dimension six. Physically it is the state family: the rank-one projectors of the informational sector
  are its boundary, the pure states of *Decoherence as Idempotent Projection* and *The Biquaternion Vacuum
  as a Minimal Idempotent*, and the family is read in *Idempotents in the 12 Structures Framework*.

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
*The Cone and the Massless Particles in the 12 Structures Framework*: in the composition the cone is the
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

The twelve products, their zero-divisor sets and the physical reading of each set are collected here. The
mathematics of each row is proved in the mathematics companion and its block articles; the reading is the
contribution of this article.

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
| the norm criterion is $N(\tilde Q)=0$, with inverse $\tilde Q^{\natural}/N(\tilde Q)$ | *Biquaternion Norm and Invertibility* | cited |
| a pure cone element has $\tilde Q^{2}=0$ and a non-pure one gives the idempotent $\tilde Q/(2Q_0)$ | mathematics companion; recomputed | verified |
| $\mathrm{SPA}$ and $\mathrm{SQS}$ have the enlarged set $(\{Q_0=0\}\cup\mathcal{C})\setminus\{0\}$ | mathematics companion; witness $e_1\bullet e_2=0$ with $N(e_1)=1$ recomputed | verified |
| the six derived structures have the whole punctured space | mathematics companion; random annihilators found for $\mathrm{SQA}$ and $\mathrm{SPS}$, alternating squares vanish | verified |
| the cone is contained in all twelve sets and equals four | mathematics companion, theorem | cited |
| the material cone is the light cone $|\mathbf x|=c|t|$ | *The Light Cone as the Biquaternion Zero-Divisor Cone* | cited |
| the rank drop of the sesquilinear square is the mass label | *Mass, Rank and the Positivity of the Dagger* | cited |
| the cone is the information barrier, the elementary erasure and the rank-one mass boundary | *Causality and the Light Cone as an Information Barrier in Biquaternionic Form*; *Landauer's Principle and the Material–Informational Exchange in Biquaternionic Form*; *Mass, Rank and the Positivity of the Dagger* | interpretation |
| the complement of the cone is the invertible region; a spacelike element is a unit | *Biquaternion Norm and Invertibility*; *Subluminal and Superluminal Electromagnetic Waves and the Lepton Mass Spectrum*; recomputed that a random spacelike element has $N>0$ and an inverse | verified |
| the horizon is a null surface of the same cone | *Black Hole Thermodynamics in Biquaternionic Form* | cited |
| the confinement kernel is a destroyed description, not a hidden one | *Confinement and the Loss of Partonic Information in Biquaternionic Form*; *Gauge Redundancy and the Information in the Gauge Orbit in Biquaternionic Form* | cited |

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
$k_BT\log2$ of dissipated heat. The zero divisor is the algebra's elementary erasure — an operation with no
inverse, whose kernel is what it destroys — and the dimension of the kernel is the amount of information
the operation annihilates. The units are the processes that erase nothing, the zero divisors the processes
that erase something, and a rank-dropping zero divisor is the elementary irreversible step whose
thermodynamic price the Landauer article owns.

**The rank and the mass label.** In the probability band the cone is where the sesquilinear square drops
rank, from two to one, and the rank is read as a mass label in *Mass, Rank and the Positivity of the
Dagger*. *The Four Readings of Mass: Norm, Rank, Charge and Scale* separates the senses of the word mass,
and the cone owns one of them cleanly and another only as a value. The cone is exactly the rank-one locus,
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
propagation. The size of the cone is an invariant of the form: *Inertia and the Witt Invariant: What a
Signature Allows a Spectrum to Carry* records the inertia $(p,q,r)$, whose $r$ is the **nullity**, the
number of null directions of the form, and reads the signature $p-q$ as a capacity, the net number of
positive modes a form can bind. How many null directions the cone has is therefore fixed by the form and
not by the frame.

**The complement is the invertible region.** The theorem of *Biquaternion Norm and Invertibility* is an
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
operation, and the algebraic face of "destroyed" is a kernel the operation cannot return from. The
Landauer principle prices that destruction, and confinement is its gauge-theory instance.

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
  Biquaternionic Form*, the elementary erasure whose price *Landauer's Principle and the Material–
  Informational Exchange in Biquaternionic Form* fixes, and the rank-one boundary at which the mass label
  of *Mass, Rank and the Positivity of the Dagger* falls from two to one.
- The complement of the cone is the invertible region. The null four-vectors are the zero divisors; the
  timelike and the spacelike ones are units, so a superluminal displacement is invertible and the failure
  of invertibility sits on the cone alone.
- A non-invertible operation can hide information or destroy it. A gauge kernel hides a description that a
  gauge choice can recover; the confinement kernel of an asymptotic colour label has destroyed a
  description the observable algebra no longer contains, and Landauer prices the destruction.
- A black-hole event horizon is a null surface, so it shares the algebra's notion of nullity with the cone.
  It is not a piece of the cone: the cone is a fibrewise set of null directions, the horizon a hypersurface
  selected by one solution and its metric. The cone supplies the criterion, the metric supplies the surface.
- The cone is a **kinematic boundary** with three images: the massless shell in momentum space, the WKB
  turning surface in configuration space, and the boundary *and* origin of the state space, because the
  module is generated by a null element. It bounds where the algebra divides, where the semiclassical
  approximation holds and where the non-relativistic description is consistent; it does not bound
  propagation. The number of its directions is the nullity $r$ of the form's inertia.

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

## Summary of Notation

- $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, basis $e_0=1,e_1,e_2,e_3$, $e_k^{2}=-e_0$, $e_1e_2=e_3$.
- $N(\tilde Q)=\tilde Q\tilde Q^{\natural}=\sum_\mu Q_\mu^{2}$ the biquaternion norm; $\mathcal{C}=\{N=0\}$ the cone, $\mathcal{C}\setminus\{0\}$ the punctured cone.
- ${}^{\natural}$ natural conjugation; $\bar{\cdot}$ coefficient conjugation; ${}^{*}=\bar{\cdot}\circ{}^{\natural}$; $\tilde Q^{\flat}=-\tilde Q^{*}$; $\mathrm{Tr}=2\,\mathrm{Sc}$.
- pure means $Q_0=0$; non-pure means $Q_0\neq0$; a nilpotent is a nonzero element with $\tilde\Upsilon^{2}=0$; an idempotent satisfies $\tilde\Pi^{2}=\tilde\Pi$.
- The twelve structures: GPA, GQA, GPS, GQS the four general products; SPA, SQA, SPS, SQS the symmetric parts; APA, AQA, APS, AQS the antisymmetric parts.
- $\mathbb{M}_\pm$ the anti-Hermitian and Hermitian sectors; $\mathbb{H}_{\mathbb{B}}$ the real-quaternion subspace; $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ the centre.
- $c=1/\sqrt{\epsilon\mu}$ the speed of light in the medium; $\tilde Q=ict\,e_0+\mathbf x$ the material coordinate.

## Further Reading

- The mathematics companion: *Zero Divisors* (`articles_maths/zero-divisors.md`), for the theorem on the twelve sets, the two families and the twelve block criteria.
- The cone in the algebra: *The Light Cone as the Biquaternion Zero-Divisor Cone*; *Zero Divisors as a Physical Locus in Biquaternionic Form*; *Biquaternion Norm and Invertibility*.
- The comparison of the four general products: *Composition and Probability: the General Plain Algebra and the General Plain Sesqualgebra of Biquaternions Compared*; *The Cone and the Massless Particles in the 12 Structures Framework*.
- The two families: *Square Roots: the Local Complex Structure, the Light Cone and the Mass Shell*; *Idempotents in the 12 Structures Framework*; *Nilpotents in the 12 Structures Framework*; *The Biquaternion Vacuum as a Minimal Idempotent*; *Decoherence as Idempotent Projection*.
- The state and the rank drop: *Mass, Rank and the Positivity of the Dagger*; *The States the Indefinite Metric Cannot Normalise*; *The Bloch Ball as the Trace-One Slice of the Future Light Cone*.
- The information and thermodynamics of the cone: *Causality and the Light Cone as an Information Barrier in Biquaternionic Form*; *Landauer's Principle and the Material–Informational Exchange in Biquaternionic Form*; *Quantum Channels and the Reversible/Irreversible Dichotomy*; *Decoherence as Idempotent Projection*.
- Where the cone sits: *Zero Divisors as a Physical Locus in Biquaternionic Form*, for the momentum-space, configuration-space and state-space images; *Inertia and the Witt Invariant: What a Signature Allows a Spectrum to Carry*, for the nullity and the signature as a capacity; *The Symplectic Form and the Biquaternion Norm Cone*, for the cone as the isotropy of the holomorphic norm and the characteristic cone of the d'Alembertian.
- The complement, the horizon and the destroyed description: *Biquaternion Norm and Invertibility*; *Subluminal and Superluminal Electromagnetic Waves and the Lepton Mass Spectrum*; *Black Hole Thermodynamics in Biquaternionic Form*; *Confinement and the Loss of Partonic Information in Biquaternionic Form*; *Gauge Redundancy and the Information in the Gauge Orbit in Biquaternionic Form*.
- The operators and the units: *The Monoid of Acting Maps: the Process Is the Multiplication, the State Is the Idempotent*; *The Operators of the Ordinary Product: One-Sided, Two-Sided and the Sandwich*; *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket*.
- The grid: *The 12 Products of the Biquaternion Complex Space*; *The Twelve Structures Compared: Product, Law and Form*; *The Four General Products and Their Physical Readings*.
- The conventions of the series: *Conventions in the Biquaternion Universe*.
