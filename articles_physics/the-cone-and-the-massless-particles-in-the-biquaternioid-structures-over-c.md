# __The Cone and the Massless Particles in the Biquaternioid Structures over $\mathbb{C}$__

## Introduction

The general plain algebra and the general plain sesqualgebra of biquaternions are one space read in two
products: the plain product $\tilde P\tilde Q$, and the plain sesquilinear product
$\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$. Every difference between the two structures traces to one
cause, the Hermitian conjugation in the second slot. One set survives the comparison unchanged, and it is
the set this article is about: the **zero divisors**, the nonzero elements whose biquaternion norm
vanishes. That set is the light cone of the material sector, and it is where the **massless particles**
live in the algebra.

Two questions organise the article, and they are the two the comparison asks of every object.

- **What is the cone in each band?** In the composition it is the boundary of invertibility: a nonzero
  element is invertible if and only if its norm does not vanish, so the cone is exactly the set the plain
  product cannot divide by. In the probability it is the boundary of the state cone: the sesquilinear
  square of a nonzero element is a positive element and is never zero, and it drops from rank two to rank
  one exactly on the cone. The nilpotent index of the cone rises from two in the first band to three in
  the second, and that index shift is the sharpest single contrast of the comparison.
- **Is the cone a property of either product?** It is not. The cone is the null set of the interval form
  $\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)$, whose algebraic norm is the biquaternion norm,
  and of the four forms the corpus uses it is the null set of that one alone. The interval is what puts the
  cone into the algebra; the two products are what give it its two jobs.

The two bands are the general members of the grid of the twelve structures, and that grid is the frame the
title names. The cone is cut out by the interval, which is the form of the quaternionic row and not of the
general plain pair alone, so the shared vanishing set of the two bands is a feature of the frame rather
than of one band. The grid, its twelve operations and their operator rows are *The 12 Products of the
Biquaternioid Complex Space*, *The Four General Products and Their Physical Readings*, *The Twelve
Structures Compared: Product, Law and Form* and *The Operators of the Twelve Structures: Multiplication,
Adjoint and Bracket*; this article uses the grid and does not rebuild it.

The article then applies the two answers to the massless particles. The photon is the case the corpus has
built; the graviton and the chiral fermion sit on the same cone, and what separates the massless particles
from one another is data the cone does not carry.

The article is organised as follows. The second section fixes the cone as one set, names its two jobs,
places it among the subspaces and separates the three sets the corpus calls a cone. The third reads the
cone under each of the twelve structures in turn, with a physical interpretation for each, and is the part
the title names. The fourth computes the nilpotent index in the two bands and records the recomputation.
The fifth shows that the cone is the null set of the interval and of no other form, and computes its
relation to the sector sign and to the gauge metric. The sixth reads the cone in the composition band,
including the absorbing property, the collapsing multiplication and the massless limit as a degeneration of
the symbol; the seventh reads it in the probability band, including the collapse of the sandwich. The
eighth treats the massless particles. The ninth separates what the cone derives from what is imported. The
tenth gathers, across the whole corpus and without regard to the older boundaries, every further reading of
the cone, each cited in place. The closing sections are the ledger, the boundaries, the summary, the
notation table and the literature.

**Conventions.** We use those of the companion articles unchanged. The biquaternion algebra is
$\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$,
$\vec e_\mu^{2}=-e_t$ and $\vec e_\mu \vec e_\nu=-\delta_{\mu\nu}e_t+\varepsilon_{\mu\nu\lambda}\vec e_\lambda$, and $i$ the central scalar imaginary.
The conjugations are the natural conjugation ${}^{\natural}$, the coefficient conjugation $\bar{\cdot}$
and the Hermitian conjugation ${}^{*}=\bar{\cdot}\circ{}^{\natural}$, with
$\tilde Q^{\flat}=-\tilde Q^{*}$. The biquaternion norm is
$\langle\tilde Q\rangle_{\natural}=\langle\tilde Q,\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}=\sum_\mu Q_\mu^{2}$,
which is the determinant of the matrix model $\mathsf{M}_2$ with $\mathsf{M}_2(e_t)=I_2$ and
$\mathsf{M}_2(\vec e_\mu)=-i\sigma_\mu$. The subspaces are the anti-Hermitian material sector $\mathbb{M}_-$,
the Hermitian informational sector $\mathbb{M}_+$, the real-quaternion subspace
$\mathbb{H}_{\mathbb{B}}$ and the centre $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_t,ie_t\}$.
The material coordinate is $\tilde R=ict\,e_t+x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$, so that $\langle\tilde R\rangle_{\natural}=-c^{2}t^{2}+x^2+y^2+z^2$,
and $c=1/\sqrt{\epsilon\mu}$ is the speed of light in the medium. The trace formula is
$\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)=2\langle\tilde P,\tilde H\rangle$. The
plain product is written $\tilde P\tilde Q$ and the plain sesquilinear product
$\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$; a plain idempotent is written $\tilde\Pi$, and the nilpotent
convention for a square-zero element is that of *Conventions in the Biquaternion Universe*.

## One Cone in the Two Bands

### The norm and its vanishing set

The cone is read off one object, the biquaternion norm

$$
\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}=\sum_\mu Q_\mu^{2}=\det\mathsf{M}_2(\tilde Q).
$$

On the material sector the norm is the Minkowski interval, $\langle\tilde R\rangle_{\natural}=-c^{2}t^{2}+x^2+y^2+z^2$ for
$\tilde R=ict\,e_t+x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$, so its zero set is the light cone $|x\,\vec e_x+y\,\vec e_y+z\,\vec e_z|=c|t|$. The algebraic
character of that zero set is the subject of *The Light Cone as the Biquaternion Zero-Divisor Cone*: a
nonzero biquaternion has vanishing norm if and only if it is a zero divisor, that is, if and only if it
annihilates some nonzero element. The same article splits the zero divisors into the **nilpotents**, whose
scalar part vanishes and whose square is zero, and the **idempotent multiples**, whose scalar part does
not and which generate the minimal ideals. Both families sit on the cone.

The cone is therefore not a surface that the algebra imports and then meets; it is the vanishing set of
the algebra's own quadratic form, and its algebraic name is the zero-divisor set.

### The two jobs of one set

The two bands share the norm and share its vanishing set. What they do with the set differs, and each band
does exactly one thing with it.

In the **composition**, the cone is the boundary of invertibility. A nonzero element $\tilde Q$ has a
two-sided plain inverse precisely when $\langle\tilde Q\rangle_{\natural}\neq0$, the inverse being
$\tilde Q^{\natural}/\langle\tilde Q\rangle_{\natural}$, and it has none when $\langle\tilde Q\rangle_{\natural}=0$. The plain product is the
operation that composes transformations and iterates a process (*The Products, Their Forms and Their Norms*), so the cone is the set of elements that cannot be composed further, and the physics of that
failure is propagation, taken up in its own section below.

In the **probability**, the cone is a rank drop. The plain sesquilinear product gives no element a
two-sided inverse at all, and its one-sided inverse exists exactly off the cone, so element invertibility
is not the distinguishing signal here. The operator signal agrees with the composition: the left
multiplication is injective exactly off the cone, so the cone is the boundary of invertibility of the
*operator* as well. What distinguishes the probability band is the second signal, the rank of the
sesquilinear square: the square $\tilde Q_1\star\tilde Q_1$ is a Hermitian positive element of rank two off the
cone and of rank one on it. *The Biquaternioid General Plain Sesqualgebra (GPS) over $\mathbb{C}$* proves the criterion and reads
the rank drop as a mass label, rank two massive and rank one massless.

The same set is thus a locus of non-invertibility for one product and a locus of rank drop for the other.
That is the first concrete form of the comparison: the cone is one object, and each product reports it in
its own vocabulary.

### Where the cone lives among the subspaces

The cone is not spread over the algebra. The centre $\mathbb{C}_{\mathbb{B}}$ and the real-quaternion
subspace $\mathbb{H}_{\mathbb{B}}$ are division algebras and contain no zero divisors at all: on
$\mathbb{H}_{\mathbb{B}}$ the norm is $\sum_\mu Q_\mu^{2}$ with every $Q_\mu$ real, so it is a sum of
squares and vanishes only at the origin. The zero divisors require the complexification, and they live in
the two Hermitian-type sectors:

- in $\mathbb{M}_-$, the anti-Hermitian material sector, the cone is the physical light cone;
- in $\mathbb{M}_+$, the Hermitian informational sector, the cone is the boundary of the future cone of
  the informational sector, which is the state cone of *The Bloch Ball as the Trace-One Slice of the
  Future Light Cone*.

The cone of the material sector and the boundary of the state cone of the informational sector are not two
objects that happen to be similar. They are the two faces of one cone, read in the two sectors, and the
matrix model makes them literally the same set of rank-one conditions.

A third reading of the same set appears on the complexified phase space of *The Symplectic Form and the
Biquaternion Norm Cone*, where a pure-vector phase-space biquaternion $\tilde Z=\vec q+i\vec p$ is
null exactly when $\lvert\vec q\rvert=\lvert\vec p\rvert$ and $\vec q\cdot\vec p=0$: the cone
is the set where the configuration and the momentum magnitudes are equal and the two vectors are
orthogonal, which is the isotropic locus of the sector sign, since $\langle\cdot,\cdot\rangle=-\langle\cdot,\cdot\rangle_{\natural}$ on the pure subspace. There the
cone is a genuinely complex object and not a physical locus: the condition equates two quantities of
different dimension until a symplectic scale is fixed, and the real phase space meets the cone only at the
origin.

### Three sets the corpus calls a cone

The word "cone" is used for three different sets in this corpus, and the comparison is only readable if
they are kept apart.

- **The zero-divisor cone**, $\{\tilde Q\neq0:\langle\tilde Q\rangle_{\natural}=0\}$, the null set of the norm. It is the
  subject of this article, and "the cone" without qualification always means this set here.
- **The state cone** of the informational sector, the future cone of $\mathbb{M}_+$, that is
  $\{\alpha e_t+i\vec w:\alpha\geq\lvert\vec w\rvert\}$, sliced by $\mathrm{Tr}\,\tilde{Ϛ}=1$
  for the states. It is a cone of *positive* elements, and it is the image of the sesquilinear square; the
  zero-divisor cone is its rank-one boundary, as the next sections show.
- **The cone of an operation**, the one-dimensional ray $\mathbb{R}_{\ge0}e_t$ that is the image of the
  symmetric plain sesquilinear product. *Why Probability Values Are Central: the Symmetric Sesquilinear
  Product and Its Cone* warns of exactly this collision: its ray is the **normalisation direction** of a
  probability and "is not the state cone".

The gauge band adds a fourth set that it also calls a null cone, the null set $\{K=0\}$ of the gauge
metric. Its relation to the zero-divisor cone is computed in the section on the four forms, and it is
closer than the name suggests. The operator article uses the word a fifth time, in the frame of the
twelve: *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket* says of the two
indefinite rows that they "keep the classes but lose the cone", and the cone lost there is the positivity
cone of the adjoint classes, that is the state cone and not the zero-divisor cone. The names are
distinguished by what they are cones *of*: a vanishing set, a positivity, a normalisation, and a
definiteness.

## The Cone in the Twelve Structures

This part reads the cone under each of the twelve structures in turn: the product, the rank of its left
multiplication off the cone and on it, what the cone is for that structure, and the physical interpretation
of the reading. The mathematics of each row is owned by the mathematics companion and its block articles;
the reading is this article's. The order is that of *The Twelve Structures Compared: Product, Law and Form*
and of *Zero Divisors in the Biquaternioid Structures over $\mathbb{C}$*: the four general structures first, then
their four symmetric parts, then their four antisymmetric parts, and inside each group the plain algebra,
then the plain sesqualgebra, then the quaternionic algebra, then the quaternionic sesqualgebra.

The companion reads the **zero-divisor set** of each structure, that is the set of elements whose left
multiplication is not injective; this part reads the **cone** in each, that is the rank that multiplication
takes on a lightlike operand. The measure is the same, the real rank of the left multiplication; the two
readings coincide on the four general rows, whose zero-divisor set is exactly the punctured cone, and they
separate on the other eight. In $\mathrm{SPA}$ and $\mathrm{SQS}$ the zero-divisor set is strictly larger
than the cone, the pure family joining it; in the six remaining rows the multiplication is already
degenerate off the cone, so the whole punctured space is the zero-divisor set, while the cone is only a
rank drop for $\mathrm{APS}$ and $\mathrm{AQA}$ and nothing at all for $\mathrm{SPS}$, $\mathrm{SQA}$,
$\mathrm{APA}$ and $\mathrm{AQS}$.

### The twelve rows in one table

The cone is one set, and the twelve rows meet it in different ways. The measurement is the **rank of the
left multiplication**, the map $L_{\tilde P}(\tilde Q_1)=\tilde P\star\tilde Q_1$ read on the eight real
parameters of the algebra. Off the cone a row separates invertible from singular when that rank is eight,
and the table gives the rank for a generic operand off the cone and for an operand on it; the two
algebra-valued symmetric rows take two values on the cone, and their entry carries both.

| row | product | rank off the cone | rank on the cone | what the cone is for the row |
| --- | --- | --- | --- | --- |
| GPA | $\tilde P\tilde Q$ | $8$ | $4$ | the boundary of invertibility |
| GPS | $\tilde P\tilde Q^{*}$ | $8$ | $4$ | the boundary of invertibility |
| GQA | $\tilde P^{\natural}\tilde Q$ | $8$ | $4$ | the boundary of invertibility |
| GQS | $\tilde P^{\natural}\tilde Q^{*}$ | $8$ | $4$ | the boundary of invertibility |
| SPA | $s_{\mathrm{pb}}(\tilde P,\tilde Q)$ | $8$, and $4$ on the pure subspace | $4$ on the pure part, $6$ on the rest | a degeneration locus, not the whole one |
| SPS | $s_{\mathrm{ps}}(\tilde P,\tilde Q)$ | $2$ | $2$ | none: the image is the centre |
| SQA | $s_{\mathrm{qb}}(\tilde P,\tilde Q)$ | $2$ | $2$ | none: the image is the centre |
| SQS | $s_{\mathrm{qs}}(\tilde P,\tilde Q)$ | $8$, and $4$ on the pure subspace | $4$ on the pure part, $6$ on the rest | a degeneration locus, not the whole one |
| APA | $a_{\mathrm{pb}}(\tilde P,\tilde Q)$ | $4$ | $4$ | none: the centre lies in the kernel |
| APS | $a_{\mathrm{ps}}(\tilde P,\tilde Q)$ | $6$ | $4$ | a drop, not the whole locus |
| AQA | $a_{\mathrm{qb}}(\tilde P,\tilde Q)$ | $6$ | $4$ | a drop, not the whole locus |
| AQS | $a_{\mathrm{qs}}(\tilde P,\tilde Q)$ | $4$ | $4$ | none: the centre lies in the kernel |

Three statements follow, and together they are the grid-level answer to the question of whether the cone
belongs to a product.

- **The cone is a degeneration locus of all twelve.** No row has an invertible left multiplication at a
  point of the cone: the rank never reaches eight on it, and it is at most six, the maximum being attained
  by the two algebra-valued symmetric rows SPA and SQS on the non-pure part of the cone. The cone is
  therefore a common boundary of the twelve structures, and in that sense it is one set and not twelve.
- **The cone is the whole degeneration locus of exactly four rows.** For the four general products the
  rank is eight off the cone and four on it, so the cone is exactly the line between invertibility and its
  failure. These are the four rows whose invertibility criterion is the norm, and for them the cone is what
  the companion article calls the boundary of the band. For six of the eight parts the left multiplication
  is already degenerate off the cone, and those six carry no unit; the two exceptions are the
  algebra-valued symmetric rows, SPA carrying the two-sided unit $e_t$ and SQS none, which are invertible
  at a generic element off the cone and off the pure subspace and degenerate only on the pure subspace and
  on the cone.
- **The cone is absorbing for exactly those four rows.** The product of a lightlike element with anything
  is lightlike, $\langle\tilde P\rangle_{\natural}=0\Rightarrow \langle\tilde P\star\tilde Q\rangle_{\natural}=0$, for GPA, GPS, GQA and GQS; it fails
  for the eight parts, where the symmetrisation or the antisymmetrisation mixes a lightlike term with a
  second term that need not be lightlike, and the sum can leave the cone.

The reasons the eight parts degenerate are visible in the table. The four antisymmetric rows have no scalar
part, so the centre lies in their kernel; the two central-valued symmetric rows have the centre for their
whole image, so their operators are of rank two everywhere; and the two algebra-valued symmetric rows SPA
and SQS are singular on the pure subspace $\{Q_t=0\}$ as well. Their symmetrised left multiplication is
the anticommutator of the matrix model, with eigenvalues $\tfrac12(\lambda_i+\lambda_j)$ of the eigenvalues
$\lambda_i$ of $\mathsf M_2(\tilde P)$, whose product carries the factor $\mathrm{Sc}(\tilde P)^{2}$ and so
vanishes on the pure subspace and on the cone alike. The determinant vanishing is not the whole rank
story: on the pure subspace the rank is four, while on the non-pure part of the cone one eigenvalue
survives and the rank is six, which is why the on-cone entry of these two rows carries two values. The
corpus states the one row it tabulates: *The Operators of the Twelve Structures: Multiplication, Adjoint
and Bracket* computes the antisymmetric plain sesquilinear left multiplication as "of real rank six for a
unit and four for a zero divisor", which is the row APS of the table.

### $\mathrm{GPA}$, the general plain algebra — composition

The product is the plain product $\tilde P\tilde Q$. The left multiplication has real rank eight off the
cone and four on it, so the cone is the exact boundary of invertibility, and it is absorbing: a lightlike
factor forces a lightlike composite, $\langle\tilde P\rangle_{\natural}=0\Rightarrow \langle\tilde P\tilde Q\rangle_{\natural}=0$.
**The physical interpretation** is that the composition of operations degenerates exactly on the light cone,
so the cone is at once the locus of lightlike propagation and the line between the reversible and the
irreversible processes. The reading is *The Light Cone as the Biquaternion Zero-Divisor Cone*, *The Biquaternioid General Quaternionic Algebra (GQA) over $\mathbb{C}$* and *Zero Divisors as a Physical Locus in Biquaternionic Form*.

The units are the elements off the cone, forming the group $\mathbb{B}^{\times}\simeq S^{1}\times S^{3}$ (*The Biquaternion Unit Group as a Topological Group*), and the cone is exactly the complement of that group: the boundary of invertibility is a group boundary, the apex included, the origin lying in the complement and being no zero divisor.

### $\mathrm{GPS}$, the general plain sesqualgebra — probability

The product is the pairing $\tilde P\tilde Q^{*}$. The rank is eight off the cone and four on it, so the cone
is the exact boundary of invertibility, and it is absorbing. **The physical interpretation** is the
probability reading of the same boundary: the sesquilinear square drops from rank two to rank one exactly on
the cone, so the cone is the rank-drop locus of the Born weight and the pure-state boundary of the state
cone. The reading is *The Biquaternioid General Plain Sesqualgebra (GPS) over $\mathbb{C}$* and *The Spinor Space as a Module and as a Hilbert Space*.

The element $e_t$ is a right unit alone, and the invertible elements are the elements off the cone, with the solution $(\tilde P^{-1})^{*}$; the cone is the complement of those elements.

### $\mathrm{GQA}$, the general quaternionic algebra — causality

The product is $\tilde P^{\natural}\tilde Q$, the plain product with the natural conjugation in the first
slot, and its square is the central interval. The rank is eight off the cone and four on it, so the cone is
the exact boundary of invertibility, and it is absorbing. **The physical interpretation** is the causality
reading of the same boundary: a lightlike element cannot be composed with, the rank drop is the algebraic
form of that statement, and the orientation of the product makes the band measure a sign rather than a size.
The reading is *The Biquaternioid General Quaternionic Algebra (GQA) over $\mathbb{C}$* and *Why the Material
Composition Is Oriented and Cannot Measure*.

The element $e_t$ is a left unit alone; the invertible elements are the elements off the cone, with the solution $(\tilde P^{-1})^{\natural}$, and the cone is the complement of those elements.

### $\mathrm{GQS}$, the general quaternionic sesqualgebra — gauge

The product is the fourth product $\tilde P^{\natural}\tilde Q^{*}$. The rank is eight off the cone and four
on it, so the cone is the exact boundary of invertibility, and it is absorbing.
**The physical interpretation** is the gauge reading: the cone is the locus where the indefinite gauge
metric degenerates, and the rank drop is the algebraic form of a gauge direction that cannot be normalised.
The reading is *The Biquaternioid General Quaternionic Sesqualgebra (GQS) over $\mathbb{C}$* and *The States the Indefinite Metric Cannot
Normalise*.

There is no unit on either side, and the invertible elements are the elements off the cone, with the solution $(\tilde P^{-1})^{\natural*}$; the cone is the complement of those elements.

### $\mathrm{SPA}$, the symmetric plain algebra — commutativity

The product is the Jordan product $\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$. The left multiplication has
rank eight off the cone, except on the pure subspace where it is four, and on the cone it is four on the pure
part and six on the rest. The cone is a degeneration locus of the row and not the whole one, and the row is
not absorbing: the symmetrisation mixes a lightlike term with a second term that need not be lightlike.
**The physical interpretation** is that a symmetrised material composition is a coupling, and a coupling can
vanish on the pure family even when both factors are non-degenerate, as the witness $\vec e_x\bullet \vec e_y=0$ shows.
The reading is *The Biquaternioid Symmetric Plain Algebra (SPA) over $\mathbb{C}$* and *Square Roots of One and the Idempotents: the Hermitian Observables and the States*.

The unit $e_t$ is two-sided, and the invertible elements of the row are the complement of its zero-divisor set, the smaller set $\{Q_t\neq0,\ \mathrm{Norm}\neq0\}$ (together with $0$, which is in the complement and is no zero divisor). They form no group, the product being non-associative. The pure family is the difference: an element with $Q_t=0$ and $\mathrm{Norm}\neq0$ is a plain unit, invertible in the composition, and a zero divisor of the symmetrised row.

### $\mathrm{SPS}$, the symmetric plain sesqualgebra — positivity

The product is the symmetrisation $\tfrac12(\tilde P\tilde Q^{*}+\overline{\tilde Q\tilde P^{*}})$, which is
scalar-valued, with the non-negative value $\langle\tilde P,\tilde Q\rangle_{*}$. The rank is two off the cone and two on
it: the cone is nothing for the row, because the image is the centre. **The physical interpretation** is that
a symmetrised pairing is a measurement and not an operation: it keeps the real part of the Born weight alone,
and a real number inverts nothing, so the cone is invisible to it. The reading is *The Hermitian Form as a
Product: Positivity and the Real Part of the Born Pairing* and *Why Probability Values Are Central: the
Symmetric Sesquilinear Product and Its Cone*.

The row has no unit, so there is no group of units and the complement of the whole punctured space is the origin alone.

### $\mathrm{SQA}$, the symmetric quaternionic algebra — coupling

The product is the symmetrisation
$\tfrac12(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P)=\langle\tilde P,\tilde Q\rangle_{\natural}e_t$, central and
scalar-valued. The left multiplication has rank two off the cone and two on it: the cone is nothing for the
row, because the image is the centre whatever the operand. **The physical interpretation** is that a scalar
coupling of two operations returns a number, and a number composes with nothing, so the cone leaves no trace
in a band that has no operation to degenerate. The reading is *The Quaternion Form as a Product: the Scalar
Coupling of Two Material Operations* and *Why a Central Product Cannot Compose: the Radical and the Isotropic
Elements*.

The row has no unit, so there is no group of units and the complement of the whole punctured space is the origin alone.

### $\mathrm{SQS}$, the symmetric quaternionic sesqualgebra — metric

The product is the symmetrisation
$\tfrac12(\tilde P^{\natural}\tilde Q^{*}+\overline{\tilde Q^{\natural}\tilde P^{*}})$. The rank is eight off
the cone, except on the pure subspace where it is four, and on the cone it is four on the pure part and six
on the rest: the cone is a degeneration locus of the row and not the whole one, and the row is not
absorbing. **The physical interpretation** is that the symmetric part of the gauge metric is again a
coupling, and the same witness applies: a symmetrised gauge coupling annihilates two operations whose vector
parts are conjugate-orthogonal, $\vec e_x\star \vec e_y=0$, so the pure family and the cone degenerate together. The
reading is *The Biquaternioid Symmetric Quaternionic Sesqualgebra (SQS) over $\mathbb{C}$* and *Values in
No Subspace: Why the Symmetric Gauge Product Is Not a State*.

The row has no unit, so the complement of the enlarged set, $\{Q_t\neq0,\ \mathrm{Norm}\neq0\}\cup\{0\}$, carries no group of units.

### $\mathrm{APA}$, the antisymmetric plain algebra — rotation

The product is the commutator $\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)=\vec P\times\vec Q$, which is
alternating, and the left multiplication has real rank four off the cone and four on it. The cone is nothing
for the row: the multiplication is already singular on the pure subspace, and the centre lies in its kernel.
**The physical interpretation** is that the antisymmetric plain product is the bracket of rotations, a
bracket and not a composition, so it has no inverse to lose and the cone cannot mark a boundary that does not
exist. The reading is *The Biquaternioid Antisymmetric Plain Algebra (APA) over $\mathbb{C}$* and *Angular
Momentum and the Lie Algebra of the Material Sector*.

The row has no unit, so there is no group of units and the complement of the whole punctured space is the origin alone.

### $\mathrm{APS}$, the antisymmetric plain sesqualgebra — phase

The product is the antisymmetrisation
$\tfrac12(\tilde P\tilde Q^{*}-\overline{\tilde Q\tilde P^{*}})$, the vector part of the pairing. The rank is
six off the cone and four on it, a drop and not the whole locus. **The physical interpretation** is the phase
reading: the band keeps the imaginary part of the Born pairing, and an imaginary part is a phase, not an
operation with an inverse, so the cone marks a rank drop in a band that has no invertibility to lose. The
reading is *The Biquaternioid Antisymmetric Plain Sesqualgebra (APS) over $\mathbb{C}$* and *The
Operators of the Antisymmetric Plain Sesquilinear Product and the Phase*.

The row has no unit, so there is no group of units and the complement of the whole punctured space is the origin alone.

### $\mathrm{AQA}$, the antisymmetric quaternionic algebra — obstruction

The product is the antisymmetrisation $\tfrac12(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P)$,
which is alternating. The left multiplication has rank six off the cone and four on it, so the cone lowers
the rank but is not the whole degeneration locus. **The physical interpretation** is that the bracket
obstructs the internal action and does not close; the cone is a rank drop inside a band that is already
singular, and a bracket that does not close is not a composition that a boundary could mark. The reading is
*The Biquaternioid Antisymmetric Quaternionic Algebra (AQA) over $\mathbb{C}$* and *Boosts, Mixed Terms
and the Missing Lie Structure*.

The row has no unit, so there is no group of units and the complement of the whole punctured space is the origin alone.

### $\mathrm{AQS}$, the antisymmetric quaternionic sesqualgebra — polarisation

The product is the antisymmetrisation
$\tfrac12(\tilde P^{\natural}\tilde Q^{*}-\overline{\tilde Q^{\natural}\tilde P^{*}})=\vec P\times\overline{\vec Q}$, the conjugate cross product, which is alternating. The rank is four off the
cone and four on it: the cone is nothing for the row, and the centre lies in the kernel.
**The physical interpretation** is the polarisation of the gauge coupling: a conjugate bracket is not a
composition, so no invertibility is lost on the cone. The reading is *The Cross Product of a Vector with Its
Conjugate: the Antisymmetric Gauge Product* and *The Operators of the Antisymmetric Quaternionic
Sesquilinear Product and the Polarisation*.

The row has no unit, so there is no group of units and the complement of the whole punctured space is the origin alone.

## The Nilpotent Index: Two against Three

### The composition: square-zero is pure isotropic

In the composition band the nilpotent structure is elementary: an element squares to zero exactly when it
is pure and isotropic,

$$
\tilde Q_1^{2}=0\quad(\tilde Q_1\neq0)\ \Longleftrightarrow\ \tilde Q_1\ \text{pure and isotropic}.
$$

*Pure* means the scalar part vanishes, $\mathrm{Sc}(\tilde Q_1)=Q_{1,0}=0$. *Isotropic* means the vector part
has vanishing square, $\sum_{k}Q_{1k}^{2}=0$. The two conditions together are the criterion
$\det\mathsf{M}_2(\tilde Q_1)=0$ with $\mathrm{Tr}\,\mathsf{M}_2(\tilde Q_1)=0$, which for a $2\times2$ matrix
is exactly nilpotence, and the recomputation below confirms both directions on random elements and on the
parametrised cone $Q_{1,1}=1$, $Q_{1,2}=i\cos t$, $Q_{1,3}=i\sin t$, which satisfies $\sum_k Q_{1k}^{2}=1-1=0$ for every
$t$. The pure isotropic cone is therefore the square-zero locus, and its nilpotent index is **two**: the
first power is nonzero and the second vanishes.

The square-zero locus is a proper part of the cone. An idempotent multiple, for instance the Hermitian
idempotent $\tilde\Pi=\tfrac12(e_t+i\vec u)$ with
$\tilde\Pi^{2}=\tilde\Pi$, has vanishing norm and a nonzero square, so the cone is the disjoint union of
the square-zero elements and the elements whose square is not zero.

### The pairing: nothing squares to zero, and the cone is nilpotent of index three

In the probability band the situation is opposite at the first step and sharper at the second. The scalar
part of the sesquilinear square is a sum of moduli,

$$
\mathrm{Sc}(\tilde Q_1\star\tilde Q_1)=\mathrm{Sc}(\tilde Q_1\tilde Q_1^{*})=\sum_\mu\lvert Q_{1\mu}\rvert^{2},
$$

so it is positive for every nonzero element and vanishes only at the origin. Hence there is **no nonzero
element whose sesquilinear square vanishes**: the square-zero elements of the composition band have no
counterpart here at all.

What the same pure isotropic cone does carry in this band is a higher index. For $\tilde Q_1$ pure and
isotropic, the first sesquilinear power is nonzero because its scalar part is a sum of moduli, while the
third power vanishes,

$$
\tilde Q_1\star\tilde Q_1\neq0,
\qquad
(\tilde Q_1\star\tilde Q_1)\star\tilde Q_1=0,
$$

so the cone is nilpotent of **index three**. The matrix model shows why in one line:
$\mathsf{M}_2(\tilde Q_1)$ is nilpotent, $\mathsf{M}_2(\tilde Q_1\star\tilde Q_1)$ is
$\mathsf{M}_2(\tilde Q_1)\mathsf{M}_2(\tilde Q_1)^{\dagger}$, and the product
$\mathsf{M}_2(\tilde Q_1)\mathsf{M}_2(\tilde Q_1)^{\dagger}\mathsf{M}_2(\tilde Q_1)^{\dagger}$ vanishes for
every nilpotent $\mathsf{M}_2(\tilde Q_1)$.

One qualification is needed, and it is the same qualification as in the composition band. The index three
belongs to the **pure** part of the cone. An idempotent multiple is Hermitian and idempotent, so its
sesquilinear cube is itself, $\tilde\Pi\star\tilde\Pi\star\tilde\Pi=\tilde\Pi\neq0$, and its index is
infinite. The index shift is therefore a shift of the pure isotropic cone alone, from two to three; the
idempotent multiples are nilpotent in neither band.

The shift is the sharpest single contrast of the comparison. Lightlike propagation is square-zero in the
operation that composes and cubically-zero in the operation that evaluates.

### The recomputation

Every claim of this section was recomputed in the matrix model with $\mathsf{M}_2(\vec e_\mu)=-i\sigma_\mu$, on
$100$ random elements and on the parametrised pure isotropic cone.

| Claim | Recomputation |
| --- | --- |
| $\langle\tilde Q\rangle_{\natural}=\det\mathsf{M}_2(\tilde Q)=\sum_\mu Q_\mu^{2}$ | holds on every element drawn |
| $\tilde Q_1^{2}=0$ exactly for pure isotropic $\tilde Q_1$ | both directions hold, random and parametrised |
| $\mathrm{Sc}(\tilde Q_1\star\tilde Q_1)=\sum_\mu\lvert Q_{1\mu}\rvert^{2}$ | holds on every element drawn |
| $\tilde Q_1\star\tilde Q_1\neq0$ for $\tilde Q_1\neq0$ | holds on every nonzero element drawn |
| $(\tilde Q_1\star\tilde Q_1)\star\tilde Q_1=0$ on the pure isotropic cone | holds for every $t$ tested |
| $\tilde\Pi\star\tilde\Pi\star\tilde\Pi=\tilde\Pi$ for $\tilde\Pi$ idempotent | holds |

## The Cone Is the Null Set of the Interval and of No Other Form

The comparison uses four forms, and the cone is the null set of one of them. Writing them out is what
shows that the cone is a property of the interval rather than of either product.

The four forms are the forms of the four families of the grid, one to a family (*The Twelve Structures
Compared: Product, Law and Form*): $\langle\cdot,\cdot\rangle$ belongs to the plain bilinear family, to GPA and SPA; $\langle\cdot,\cdot\rangle_{*}$ to the
plain sesquilinear family, to GPS and SPS; $\langle\cdot,\cdot\rangle_{\natural}$ to the quaternionic bilinear family, to GQA and SQA; and
$\langle\cdot,\cdot\rangle_{\natural*}$ to the quaternionic sesquilinear family, to GQS and SQS. The cone is the null set of the interval, so
it is the null set of the form of the **quaternionic bilinear** family and not of the general plain pair:
the natural conjugation is what produces the interval, while the plain product carries the sector sign.

The **sector sign** is $\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q)$, of signature $(4,4)$ on the
complex space. Its algebraic norm is

$$
\langle\tilde Q,\tilde Q\rangle=\mathrm{Sc}(\tilde Q^{2})=Q_t^{2}-\sum_k Q_k^{2},
$$

which is not the norm: the vector part enters with the opposite sign. On the material sector, where
$Q_t=ict$ and the $Q_k$ are real, the sector sign is $-c^{2}t^{2}-(x^2+y^2+z^2)$, a negative definite
form, so the material sector contains no real direction on which $\langle\cdot,\cdot\rangle$ vanishes. The light cone is not the
null cone of the sector sign. *The Bilinear Product on the Material Sector* states the same separation
from the other side, that the sector sign is definite on each sector and has no cone there, so that the
causal structure belongs to the interval.

The **probability weight** is the form $\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})$, whose value
is the sum $\sum_\mu P_\mu\overline{Q_\mu}$, of signature $(8,0)$. Its algebraic norm is

$$
\langle\tilde Q,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde Q\tilde Q^{*})=\sum_\mu\lvert Q_\mu\rvert^{2},
$$

which is positive for every nonzero element. A positive definite form has no nonzero null vector, so the
cone is invisible to the probability weight: no element of the cone is null for $\langle\cdot,\cdot\rangle_{*}$, and no element
outside it is null either.

The **interval** is the form $\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)$, whose value is
the sum $\sum_\mu P_\mu Q_\mu$, and whose algebraic norm is the biquaternion norm,
$\langle\tilde Q,\tilde Q\rangle_{\natural}=\langle\tilde Q\rangle_{\natural}$. The light cone is its null set by construction.

The **fourth form** is $\langle\tilde P,\tilde Q\rangle_{\natural*}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})$, the gauge
metric of the quaternionic sesquilinear product, whose algebraic norm is
$\lvert Q_t\rvert^{2}-\sum_k\lvert Q_k\rvert^{2}$; it is indefinite, of realified signature $(2,6)$,
positive on the centre and negative on the vector subspace.

Its null set is not the light cone, and the comparison is sharper than "different". On the two sectors the
interval and the gauge metric are one form up to sign,

$$
\langle\tilde P,\tilde Q\rangle_{\natural*}=\langle\tilde P,\tilde Q\rangle_{\natural}\ \text{on}\ \mathbb{M}_+,
\qquad
\langle\tilde P,\tilde Q\rangle_{\natural*}=-\langle\tilde P,\tilde Q\rangle_{\natural}\ \text{on}\ \mathbb{M}_-,
$$

which is the sector collapse $\langle\cdot,\cdot\rangle_{\natural*}=\pm\langle\cdot,\cdot\rangle_{\natural}$ of *The Four General Products and Their Physical Readings*, with the
sign carried by the sector. Two consequences follow. On the trace-one Hermitian slice the two vanishings
coincide, $\langle\cdot,\cdot\rangle_{\natural*}=0\iff\langle\cdot,\cdot\rangle_{\natural}=0\iff$ rank one, and that coincidence is the intersection statement of *The States the
Indefinite Metric Cannot Normalise*: the pure states are the intersection of the gauge-metric null set, the
zero-divisor cone and the trace-one slice, so the cone is at once the locus of light and the boundary of
the state space. Off the two sectors the null sets separate in both directions, with the witnesses
$\tilde Q=e_t+\vec e_x$, where $\langle\tilde Q,\tilde Q\rangle_{\natural*}=0$ and $\langle\tilde Q,\tilde Q\rangle_{\natural}=2$, and $\tilde Q=e_t+i\sqrt{2}\,\vec e_x+\vec e_y$, where $\langle\tilde Q,\tilde Q\rangle_{\natural}=0$ and
$\langle\tilde Q,\tilde Q\rangle_{\natural*}=-2$. The gauge metric therefore contains the cone as a subset and adds to it; it is not the interval.

Of the four, only the interval has the light cone as its null set. The other two indefinite forms meet the
cone, and each meets it on one remarkable subspace: the sector sign on the pure part, where
$\langle\tilde Q,\tilde Q\rangle=-\langle\tilde Q\rangle_{\natural}$, and on the centre, where $\langle\tilde Q,\tilde Q\rangle=\langle\tilde Q\rangle_{\natural}$, so the two
forms coincide up to sign on the pure subspace and the sector sign vanishes on the pure isotropic elements;
and the gauge metric on the two sectors, where $\langle\cdot,\cdot\rangle_{\natural*}=\pm\langle\cdot,\cdot\rangle_{\natural}$. Neither meeting is the whole cone, and each of the
two forms has its own null set, the quadrics $Q_t^{2}=\sum_kQ_k^{2}$ and $\langle\cdot,\cdot\rangle_{\natural*}=0$, which contain points off
the cone and miss points of it. The witness $\tilde Q=e_t+i \vec e_x+i \vec e_y+\vec e_z$ has $\langle\tilde Q,\tilde Q\rangle_{\natural}=0$, $\langle\tilde Q,\tilde Q\rangle=2$ and $\langle\tilde Q,\tilde Q\rangle_{\natural*}=-2$, so
it lies on the cone and in neither of the other null sets, while $\tilde Q=e_t+\vec e_x$ has $\langle\tilde Q,\tilde Q\rangle=\langle\tilde Q,\tilde Q\rangle_{\natural*}=0$ with
$\langle\tilde Q,\tilde Q\rangle_{\natural}=2$, so it lies in both of them and off the cone. The interval is therefore the only one of the four
whose null set is the cone, and the only one that meets the cone in all of it. The statement matters for
the comparison, because it locates the cause of the cone. The cone is not "where the plain product
vanishes" and it is not "where the sesquilinear product vanishes"; neither product is a quadratic form.
The cone is where the interval vanishes, and the interval is the form whose algebraic norm is the norm. The two
products then take that one set and give it two different jobs, which is what the next two sections read.

## The Cone in the Composition Band: Propagation at the Speed of Light

In the composition the cone is the set of elements that cannot be divided by, and the physics of that
failure is propagation.

The wave operator is the norm of the gradient, $\Box=\tilde\nabla\tilde\nabla^{\natural}$, and a
four-wavevector $\tilde P$ is null exactly when $\langle\tilde P\rangle_{\natural}=0$. For such a $\tilde P$ every function of
the phase $\mathrm{Sc}(\tilde P\tilde Q^{\natural})=\langle\tilde P,\tilde Q\rangle$ solves the wave
equation, so the null directions are the directions in which the algebra propagates without dispersion.
The four consequences of the null shell — the shell's uniqueness as a cone, the speed $c$ and its
frame-independence, the absence of a rest frame, and the motion at $c$ for every momentum — belong to
*The Null Four-Momentum: What the Cone Derives and What It Does Not* and are not re-derived here.

The invariance of the cone under the rotor group is the invariant barrier of *Causality and the Light Cone
as an Information Barrier in Biquaternionic Form*: each of the three classes of separation is a union of
orbits of the rotor group, and their common boundary is the cone, so no rotor carries a point of the cone
off it. The massless shell is therefore not merely a locus of velocities; it is a boundary that the
composition's own symmetry group preserves.

Two facts about the material coordinates are worth separating here. The nilpotent cone of the composition
band, the pure isotropic set of the nilpotent-index section, is the set of elements whose square vanishes;
the roots of $0$ in the equation $\tilde Q_1^{2}=0$ are exactly those nilpotents, and they are the subject of
*Square Roots of Zero and the Nilpotents: the Light Cone*. A general element of the
light cone need not be nilpotent: the idempotent multiples of the cone have nonzero square, and they are
the elements that carry the rank-one structure used in the next section.

### The cone is absorbing, and the operators that collapse it

The multiplicativity of the norm has a second reading that the frame-independence of $c$ does not exhaust.
If one factor of a product lies on the cone then so does the product,

$$
\langle\tilde P\rangle_{\natural}=0\ \Longrightarrow\ \langle\tilde P\tilde Q\rangle_{\natural}=\langle\tilde Q\tilde P\rangle_{\natural}=0,
$$

so the cone is the **absorbing set** of the composition. *The Four Forms, the Four Algebraic Norms and the Change of Scalars* states it as "composition cannot generate mass": a composite with a lightlike factor
is lightlike. The same article gives the family picture that goes with it. The mass shells
$\{N=-m^{2}c^{2}\}$ interpolate between the null cone at $m=0$ and the timelike interior, the product
multiplies the labels, and a lightlike label is therefore absorbing for the whole family. This is a
statement the present article's account of propagation does not contain: it uses the multiplicativity to
freeze the vanishing under a rotor, not to say that the product cannot leave the cone.

The same fact has an operator face, in *The Operators of the Quaternionic Product: the Opposite Monoid and
the Norm*. For a null parameter $\tilde P$ the matrix model has $\det\mathsf{M}_2(\tilde P)=0$, and then
$\det\mathsf{M}_2(\tilde P\tilde Q)=0$ for every $\tilde Q$, so the whole image of the left multiplication
$L_{\tilde P}$ lies in the cone. The left multiplication by a null parameter collapses the form, which is
the operator picture of lightlike propagation and the operator counterpart of the statement that the cone
is the boundary of invertibility. A general element off the cone has $\det\neq0$ and its multiplication is
invertible, so the same determinant separates the two regimes in the operator language.

The absorbing property is also the reason a mass spectrum attached to this product is not a set of
eigenvalues. On the unit group the norm is a homomorphism,
$\langle\tilde P\tilde Q\rangle_{\natural}=\langle\tilde P\rangle_{\natural}\langle\tilde Q\rangle_{\natural}$, which is exactly the statement that the norm $\langle\tilde Q\rangle_{\natural}$ is a **character**,
$\langle\cdot\rangle_{\natural}:(\mathbb{B}^{\times},\cdot)\to(\mathbb{C}^{\times},\cdot)$, and *Why a Central Product Cannot Compose:
the Radical and the Isotropic Elements* draws the consequence: a mass label built out of $\langle\tilde Q\rangle_{\natural}$ on this row is
a character and not an eigenvalue, an eigenvalue needing a unit and a spectral theory. The comparison adds
the form-side counterpart. *The Quaternion Form as a Product: the Scalar Coupling of Two Material
Operations* reads the interval $\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)$ — the form
the cone belongs to — as a comparison that "measures every direction and normalises none": its radical is
trivial, so it separates every nonzero element from some partner, and its algebraic norm vanishes on the cone, so
it separates no lightlike element from itself. That is the exact counterpart in the composition row of the
probability row's statement that the probability weight has no null vector.

The same drop is the algebraic form of the massless limit, and the reading is *Conformal Invariance and the
Massless Limit in Biquaternionic Form*. On shell the four-momentum is a biquaternion $\tilde P$ and the
symbol of the wave operator is its norm: for the massive momentum the norm is $-\mu^{2}\neq0$ and the left
multiplication by $\tilde P$ has complex rank four, while for the massless one the norm vanishes and the
rank is two. In the real count of the table of the twelve rows the drop is eight to four, and it is the
same drop the row GPA shows at every point of the cone. The massless limit is therefore a **degeneration
of the symbol** and not merely the removal of a constant: the symbol acquires a kernel, the propagator
acquires a pole on the light cone, and the equation acquires the gauge-like degeneracy the conformal
symmetry organises. The operator face and the absorbing face are two readings of one rank identity.

## The Cone in the Probability Band: the Boundary of the State Cone

In the probability the cone is the boundary of the state cone, and the passage from the cone to the state
space is one map.

The sesquilinear square lands in the informational sector. For every $\tilde Q_1$ the element
$\tilde Q_1\star\tilde Q_1$ is Hermitian, its scalar part is real and its vector part is imaginary, so it lies
in $\mathbb{M}_+$, and it is positive:

$$
\tilde Q_1\star\tilde Q_1\in\mathbb{M}_+,
\qquad
\langle\tilde Q_1\star\tilde Q_1\rangle_{\natural}=\lvert \langle\tilde Q_1\rangle_{\natural}\rvert^{2},
\qquad
\mathrm{rank}\,\tilde Q_1\star\tilde Q_1=1\ \Longleftrightarrow\ \langle\tilde Q_1\rangle_{\natural}=0.
$$

Writing the image as $\alpha e_t+i\vec w$ with $\alpha$ real and $\vec w$ a real vector, the
positivity is the inequality $\alpha\geq\lvert\vec w\rvert$, and the determinant identity is

$$
\alpha^{2}-\lvert\vec w\rvert^{2}=\lvert \langle\tilde Q_1\rangle_{\natural}\rvert^{2}.
$$

Three statements follow, and together they are the band's reading of the cone.

- **The image is the state cone.** The image of the sesquilinear square is exactly the set of positive
  elements of $\mathbb{M}_+$, that is, the set $\{\alpha e_t+i\vec w:\alpha\geq\lvert\vec w\rvert\}$.
  Every positive element is a sesquilinear square, by taking the positive square root, and the map is onto
  by that construction. This set is the future light cone of the informational sector, and *The Spinor Space as a Module and as a Hilbert Space* identifies it with the state cone.
- **The boundary is the image of the zero divisors.** The rank-one elements are the boundary
  $\alpha=\lvert\vec w\rvert$, and by the rank criterion they are precisely the images of the cone. A
  massless element therefore maps to a rank-one positive element, which is a pure state, and the massless
  slice of the cone is the pure-state boundary of the state cone.
- **The probability of a massless element is not zero.** The weight $\langle\cdot,\cdot\rangle_{*}$ of the four-forms section is
  positive definite, with $\langle\tilde Q,\tilde Q\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}>0$ on every nonzero
  element and in particular on the whole cone. The pairing has no null vector anywhere, so the cone is not
  a locus of vanishing probability, and a massless element carries a well-defined boundary state rather
  than a null state.

The contrast with the composition band is now exact. The same element that the plain product cannot
divide by, and that in the composition band is a signal travelling at $c$, is in the probability band a
pure state on the boundary of the state cone.

The sharper operator reading belongs to the sandwich rather than to the square, and it separates the two
regimes by a rank of four against one. The sandwich
$\Theta_{\tilde Q}(\tilde Q_2)=\tilde Q\tilde Q_2\tilde Q^{*}$ of *The Operators of the Plain Sesquilinear
Product and the Born Pairing* is the operator form of the sesquilinear product; acting on the whole algebra
it has complex rank four off the cone, where it is a bijection of the matrix algebra, and complex rank one
on it, where its image is a single Hermitian line. In the matrix model the sandwich is the congruence
$X\mapsto M X M^{\dagger}$ with $M=\mathsf M_2(\tilde Q)$, and *The 2×2 Matrix Operator Representation
$\mathsf M_2(\mathbb C)$ of Biquaternions* computes the collapse: on the cone the matrix is a product
$M=uv^{\dagger}$ of rank one and every operand is sent to a multiple of $uu^{\dagger}$, the line of a
minimal idempotent. The surviving scalar decides which face of the cone the operand sits on: for the pure
part $Q_t=0$ and the operator is nilpotent, while for an idempotent multiple $Q_t\neq0$ and it is a scaled
projection. Read as a process the collapse is irreversible, a completely positive map with a single Kraus
operator and hence the algebraic shape of a destructive measurement, and it is the geometric form of the
decoherence of *Decoherence as Idempotent Projection*. The division of the cone into the nilpotent part and
the idempotent multiples is thus the same division the composition band reads through the nilpotent index,
seen here as the two possible survivors of the collapse.

## The Massless Particles

### The photon: one momentum in both bands

The photon is the massless case the corpus has built, and it exhibits both jobs of the cone at once. Its
four-momentum is

$$
\tilde P=i\frac{E}{c}e_t+\vec p,
\qquad
\langle\tilde P\rangle_{\natural}=-\frac{E^{2}}{c^{2}}+\vec p^{2},
$$

so the massless condition $\langle\tilde P\rangle_{\natural}=0$ is $\lvert\vec p\rvert=E/c$, and the four-momentum is a zero
divisor. The lightlike momentum has a second face. With
$\vec u=\vec p/\lvert\vec p\rvert$ and
$\tilde\Pi(\vec u)=\tfrac12(e_t+i\vec u)$, it is the imaginary multiple

$$
\tilde P=2i\frac{E}{c}\,\tilde\Pi(-\vec u)
$$

of a rank-one Hermitian idempotent, so it is not merely non-invertible but a scaled projector. That
identity, its verification $\tilde\Pi^{2}=\tilde\Pi$, $\tilde\Pi^{*}=\tilde\Pi$, $\langle\tilde\Pi\rangle_{\natural}=0$, and its
consequences for the shell, the rest frame and the speed are *The Null Four-Momentum: What the Cone Derives
and What It Does Not*; the comparison uses them and does not re-derive them.

The probability band completes the picture. The sesquilinear square of the same momentum is

$$
\tilde P\star\tilde P=4\frac{E^{2}}{c^{2}}\,\tilde\Pi(-\vec u),
$$

a positive multiple of the **same** projector. The **interpretation**, and it is this article's, is that
one element carries one face in each band: in the composition the momentum is an imaginary multiple of the
projector, which is why it is non-invertible and why the propagation is at $c$; in the probability it is a
positive multiple of the same projector, which is why its state is a pure boundary state and not a null
state. Neither band alone shows this; the comparison is the two squares read side by side. The flagpole
form of the identity, in which the null direction and the projector are two faces of one object, is in
*The Boost of an Electromagnetic Plane Wave as a Rotation and a Dilation*, and the polarisation account is
*The Photon in Biquaternionic Form*.

### Every massless particle sits on the same cone

The cone is one set, and every massless particle of the framework sits on it: the massless shell is the
only shell that is a cone, by the dilation invariance of the cone (*The Null Four-Momentum: What the Cone
Derives and What It Does Not*). The massless particles are:

- the photon, of helicity $\pm1$, whose four-momentum is the case just computed;
- the graviton, of helicity $\pm2$, the massless spin-two field of *Canonical Quantization of the
  Biquaternion Graviton Field*;
- the Rarita–Schwinger field, of helicity $\pm\tfrac32$, the massless spin-$\tfrac32$ case of *Canonical
  Quantization of the Biquaternion Rarita–Schwinger Field*;
- the chiral fermion, the massless spin-$\tfrac12$ case of *Chiral Fermions in the Biquaternion
  Framework*, where the masslessness of a lone Weyl field in the unbroken phase is the algebraic statement
  that the mass bilinear vanishes identically on a state of definite chirality.

All four have $\langle\tilde Q,\tilde Q\rangle_{\natural}=0$; the cone sees no difference between them.

### What the cone does not tell the massless particles apart

Two data of a massless particle are fixed by the cone and two are not.

The cone fixes the shell and the rank. The shell is $\langle\tilde Q,\tilde Q\rangle_{\natural}=0$ for every massless particle, and the rank of the
sesquilinear square is one for every massless particle, so rank is a mass label and not a spin label; it
separates massless from massive and does not separate the massless from one another.

The cone does not fix the helicity content. For a massless field the momentum is left invariant by the
Euclidean group $\mathrm{ISO}(2)$ of the plane transverse to it, whose unitary representations are
labelled by the helicity, and a field of a given Lorentz type carries finitely many helicities, of which
the gauge symmetry removes all but the two extreme ones. The count is therefore two for every spin, for
the photon, the graviton and the Rarita–Schwinger field alike, and the value of the spin is what
distinguishes them. The null directions themselves, with their chirality and their phase, are the subject
of *The Celestial Sphere of the Null Cone: Null Directions, Chirality and the Phase*.

The **interpretation** is that the cone is the common floor of the massless spectrum and not its separator. A
massless particle is a point of the cone plus a helicity, and the cone supplies the first factor only.

## What the Cone Derives and What It Does Not

The element-level division — what the cone derives about *one* null four-momentum, and what it does not —
is *The Null Four-Momentum: What the Cone Derives and What It Does Not*'s, and is not repeated here. What
this article adds is the version of the division that only the comparison can state, because it is a
division **between the two bands**.

What the cone derives is the same set in both bands, and its two jobs are two faces of one statement: the
shell is $\langle\tilde Q,\tilde Q\rangle_{\natural}=0$, so it is the boundary of invertibility in the composition and the rank-drop boundary of the
sesquilinear square in the probability. The probability adds one item of its own: the sesquilinear square
of a massless element is a positive rank-one element, so the massless slice of the cone is the pure-state
boundary of the state cone. The one place the two bands disagree is the nilpotent index, two against three,
and that disagreement is the comparison's sharpest single result.

What neither band derives is likewise the same in both. The value $m=0$; any mass scale at all, since the
cone is dilation-invariant; the selection of the massless branch over the massive one; and the reduction
from the four polarisation directions of the material sector to the two transverse ones. The reduction is
the one to state carefully, because the rank-one boundary invites the opposite conclusion: the rank is a
*count* of rank-one summands and the count of polarisations is a reading offered on that count, as *Mass,
Rank and the Positivity of the Dagger* says of itself. The reduction is a subsidiary gauge condition, and
the polarisation space it acts on belongs to *The Photon in Biquaternionic Form*.

The comparison sharpens the reason for the last item. The cone is the null set of the interval, and the
interval is a form of the algebra, so everything the cone says is a statement about the norm and its
vanishing. The polarisation count and the helicity content are statements about a little group, and no
little group lives inside the norm. That is why the cone can be exact about the massless shell and silent
about the massless spectrum.

## The Cone Across the Corpus

The cone is one set, and the framework is young: no band has finished with it. This part therefore does not
close anything. It gathers, from every article of the corpus that has something to say about the vanishing
of the norm, what that article says, and it cites each owner so that the statement stands in its original
place as well as here. The rule of the gathering is the one the twelve structures impose: anything that has
sense under the grid belongs to the cell of the grid it belongs to, and the cone, which is the degeneracy
locus of all twelve, is that cell's meeting point. What follows is grouped by the face of the cone the
corpus reads, not by the article it is read in.

### The cone as the singular set of the algebra

The cone is not a surface laid inside the algebra; it is the algebra's singular set, and its shape is known.

On the norm alone the cone is the set $\mathcal{C}=\{\tilde Q:\langle\tilde Q\rangle_{\natural}=0\}$. Its **apex is the only
singular point**: the algebraic norm is irreducible over $\mathbb{C}$ and its gradient $(2Q_t,2Q_x,2Q_y,2Q_z)$
vanishes only at the origin, so the punctured cone is a smooth complex three-manifold, of real dimension six
(*The Topology of the Zero-Divisor Cone*). The cone is **contractible**, the straight-line homotopy to the
apex staying inside it because scaling by a complex number preserves the equation. Its **link**, the
intersection with the unit sphere $S^7_E$, is a closed connected real five-manifold, an $S^1$-bundle over
$\mathbb{P}^1\times\mathbb{P}^1\cong S^2\times S^2$, with $\pi_x=0$ and $\pi_y\cong\mathbb{Z}$, so the link
is simply connected and is not a sphere; that homotopy group is the proof that the apex is a genuine
singularity and not a removable point. The projectivised cone, $\mathbb{P}^1\times\mathbb{P}^1$, is the
**Segre quadric**, and its two rulings are the two families of chiral null planes
(*The Null Quadric and Its Projective Geometry*).

The cone is moreover **one of four null sets**, and this locates it among the forms. The two bilinear forms
$\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\natural}$ are indefinite and both have null sets of real dimension six, but the two do not agree: the null
set of $\langle\cdot,\cdot\rangle$ is the complex cone $\sum_\mu\varepsilon_\mu Q_\mu^{2}=0$, which is not the zero-divisor cone,
while the null set of the Hermitian form $\langle\cdot,\cdot\rangle_{*}$ is the origin alone and that of the Krein form $\langle\cdot,\cdot\rangle_{\natural*}$ is the
**Krein cone** of real dimension seven (*The 4 Forms over the Biquaternioid $\mathbb{C}$ Space*,
*The Krein Level Sets and the Hyperbolic Structure*). On the remarkable subspaces the cone drops from real
dimension six to four on the vector subspace and to three on the quaternion subspace and on the two sectors,
carried at every stage by the indefinite forms alone (*Remarkable Subspaces and the Four Forms*). The cone is
also **the complement of the unit group**: the units are the elements off it, forming
$\mathbb{B}^{\times}\simeq S^{1}\times S^{3}$ with $\pi_x\cong\mathbb{Z}$ and $\pi_y=0$, while the cone's
link has $\pi_y\cong\mathbb{Z}$, and the real slice of the cone is the Minkowski light cone of real dimension
three with link $S^{2}\sqcup S^{2}$, one sphere per nappe (*The Biquaternion Unit Group as a Topological
Group*, *Biquaternion Lorentzian and Conformal Geometry*).

**The physical interpretation** is that the cone is where the algebra is not locally trivial: away from the
apex the zero-divisor set is a manifold and the algebra has a smooth local theory, while the apex is the one
place where the two rulings of null directions degenerate to a point. The link is the sphere-like object the
massless directions live on, and its being an $S^1$-bundle over two spheres is the topological form of the
two spinor chiralities. Of the four null sets the cone is the middle one, of dimension six, and it is the
only one that is the degeneracy of the algebra's own product; the Krein cone is one dimension larger, the
complex cone of $\langle\cdot,\cdot\rangle$ is a different six-dimensional set, and the Hermitian form has no cone at all. The
complement of the cone is the units, so the same norm decides whether an element is invertible and which of
the two homotopy groups vanishes.

### The cone as the critical set of the square

The cone is not only a locus of degeneracy; it is where the square itself degenerates, and the corpus reads
it as a critical set. On the cone the square is affine, $\tilde Q^{2}=2Q_t\tilde Q$, so squaring a null
element stays on its own complex line and preserves the cone; the critical set of the
quadratic map $\tilde Q\mapsto\tilde Q^{2}+\tilde Q_2$ is the union of the cone and the vector subspace, and
the cone is the part of it on which the square can collapse, on which no
escape radius is uniform and on which the Julia set is not a complex manifold. For the parameter zero every
idempotent lies on the Julia set of that map, and the singular Julia set contains a complex surface
(*The Zero Divisors and the Singular Julia Sets*, *The Biquaternion Quadratic Map and Its Julia Sets*). The
same set is the **largest nontrivial vanishing set of a square**: the natural square
$\tilde Q\tilde Q^{\natural}$ vanishes exactly on the cone, while the sesquilinear square
$\tilde Q\star\tilde Q=\tilde Q\tilde Q^{*}$ vanishes at the origin alone
(*The Squares and the Positive Cone of the Biquaternioid Sesqualgebra*).

**The physical interpretation** is that the cone is the boundary of the algebra's iteration: the lightlike
elements are exactly the ones whose square can collapse to a multiple of themselves, and the idempotent
projectors — the measurements — sit on the Julia set of the squaring. The two squares separate the two
pairings: the interval's square can vanish, the Born pairing's cannot, which is the algebraic face of the
fact that a probability weight is never sent to zero by an operation alone.

### The cone as the annihilator locus

The cone is where an operation's kernel stops being trivial, and the corpus reads the kernel directly.
The **annihilator** of an element is the set of partners that it kills, so it is the kernel of the
multiplication by it, and for a cone element it is a complex plane. Its elements are themselves cone
elements: when $\tilde P\neq0$ kills $\tilde Q_1\neq0$, the element $\tilde Q_1$ is a zero divisor of the same
product with witness $\tilde P$, and for the four general products, whose zero-divisor set is the cone,
the whole annihilator lies on the cone. The sharp statement is that the killers of a lightlike element are
lightlike: a null direction can be annihilated only along null directions, and a lightlike signal can be
killed only by another lightlike signal.

The plane is not a new object in each of the four general products. The four planes of one cone element are
one plain plane read through the two conjugations,

$$
A_{\natural}(\tilde P)=A_{\mathrm{plain}}(\tilde P^{\natural}),\qquad
A_{*}(\tilde P)=A_{\mathrm{plain}}(\tilde P)^{*},\qquad
A_{\natural*}(\tilde P)=A_{\mathrm{plain}}(\tilde P^{\natural})^{*},
$$

so the composition band determines the kernel of the pairing and of the gauge band, and the four bands
differ only by which conjugation is applied to the kernel.

The left and the right annihilators coincide in ten of the twelve structures and differ in exactly two,
the plain product $\tilde P\tilde Q$ and the general quaternionic sesquilinear product
$\tilde P^{\natural}\tilde Q^{*}$, and only at a cone element. At the non-pure cone element $e_t+i\vec e_x$ the
two plain planes are

$$
A_{\mathrm{plain}}(e_t+i\vec e_x)=\mathbb{C}\{e_t-i\vec e_x,\ \vec e_z+i\vec e_y\},\qquad
B_{\mathrm{plain}}(e_t+i\vec e_x)=\mathbb{C}\{e_t-i\vec e_x,\ \vec e_z-i\vec e_y\},
$$

which share the line of the natural conjugate $\tilde P^{\natural}=e_t-i\vec e_x$ and differ in their second
generator. A lightlike element kills its own conjugate on both sides,
$\tilde P\tilde P^{\natural}=\langle\tilde P\rangle_{\natural}e_t=0$ on the cone, and the two-sided annihilator is that line. The
difference between the two sides is a **chirality**, the annihilator face of the one-sidedness of the
internal action.

**The physical interpretation** is that the cone is the locus where an operation forgets a direction, and
the direction it forgets is again lightlike. Nullity is closed under the operation that produced it: on
the four general rows the annihilator of a cone element is a plane inside the cone. The two-sided case is
the elementary one, and it is the self-annihilation of a pure cone element, $\tilde P^{2}=0$; the non-pure
case is the state, whose conjugate survives on both sides and whose two kernels differ in one further
direction. The reading is *Annihilators in the Biquaternioid Structures over $\mathbb{C}$*, with the
mathematics in its companion *Annihilators in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*.

### The cone as the root set of zero

The cone is the solution set of the equation $\tilde Q_1^{2}=0$ that is not the origin, and reading it as a
**root set** is a face of its own. The root set of $0$ is a cone in every one of the twelve structures, and
in the four general products it is a different part of the same cone, because the square is a different
square while the zero-divisor set is one set:

- $\mathrm{GPA}$: the pure isotropic cone $\{Q_t=0,\ (\vec Q,\vec Q)=0\}$, of real dimension four,
  the lightlike displacements of the composition;
- $\mathrm{GPS}$: the origin alone, because the sesquilinear square has the definite scalar part
  $\sum_\mu\lvert Q_\mu\rvert^{2}$, so the probability band has no lightlike element;
- $\mathrm{GQA}$: the whole cone $\mathcal{C}$, of real dimension six, because the natural square is the
  norm and every lightlike element annihilates itself;
- $\mathrm{GQS}$: the subfamily $\overline{\tilde Q}\tilde Q=0$, of real dimension four, a proper part of
  the cone that contains $e_t+i\vec e_x$ and misses both the pure isotropic element $\vec e_x+i\vec e_y$ and the
  lightlike $ie_t+\vec e_x+\vec e_y+i\vec e_z$.

The four root sets are nested and separated in a fixed way. Writing $Z_1$ for the composition, $Z_2$ for
the interval, $Z_3$ for the probability and $Z_4$ for the gauge, the order is
$\{0\}=Z_3\subsetneq Z_1\subsetneq Z_2$, $Z_3\subsetneq Z_4\subsetneq Z_2$ and $Z_1\cap Z_4=\{0\}$. The
plain and the gauge square-zero sets are therefore incomparable inside the cone, meeting only at the apex.
The same comparison holds at a general value: the composition realises every value, and the interval's
root set at $\lambda$ is the level set $\langle\tilde Q,\tilde Q\rangle_{\natural}=\lambda$, the cone at $\lambda=0$ and the nondegenerate quadric
elsewhere, so the cone is the value zero of the interval's own shell family.

**The physical interpretation** has two halves. The square-zero elements are the **lightlike
displacements**, and the root set of zero is the smallest physical set that carries masslessness: a
translation along a null direction whose iteration adds nothing. And the cone is **larger than its
displacements**. The complement of the square-zero set inside the cone is the non-pure family, the nonzero
multiples of the idempotents, which are the states; a state is a zero divisor that is **not** square-zero,
idempotent rather than nilpotent, $\tilde\Pi^{2}=\tilde\Pi$, and a measurement has no inverse because it
lies on the cone. The set of the non-invertible operations is therefore strictly larger than the set of
the lightlike ones, and the difference is made of the states. In the probability band the gap runs the
other way and is total: the zero-divisor set is the whole punctured space while the square-zero set is the
origin alone, so no amplitude of that band is lightlike, and an amplitude is non-invertible because it is
a probability and not because it is lightlike. The readings are *Square Roots of Zero and the Nilpotents in the Biquaternioid Structures over $\mathbb{C}$*, *Square Roots of a General Element in the Biquaternioid Structures over $\mathbb{C}$* and *Square Roots of a General Element in the Biquaternioid Structures over $\mathbb{C}$*, with the states in *Square Roots of One and the Idempotents in the Biquaternioid Structures over $\mathbb{C}$*; this subsection gathers their tables for the cone.

### The cone in the propagators and the causal kernels

The dynamics has the cone for support, and the corpus computes the support.

The wave operator is the norm of the gradient, $\Box=\tilde\nabla\tilde\nabla^{\natural}$, whose symbol is
the norm of the four-wavevector; the zero set of the symbol, $\omega^{2}=c^{2}\vec k^{2}$, is the light
cone, which in the algebra is the zero-divisor cone, and the mass shell $\langle\tilde Q,\tilde Q\rangle_{\natural}=-\mu^{2}$ is the **shifted cone**
(*The Biquaternion D'Alembertian and Its Green's Functions*). The invariant kernel depends on the cone
variable $\rho^{2}=-c^{2}t^{2}+R^{2}$, so it is **singular on the cone** and is not defined there as a
function; the light-cone delta resolves the quadratic form into its two halves,

$$
\delta(\rho^{2})=\frac{1}{2cR}\Bigl[\delta\Bigl(t-\frac{R}{c}\Bigr)+\delta\Bigl(t+\frac{R}{c}\Bigr)\Bigr],
$$

and that Jacobian is what turns the invariant kernel into the causal ones. The **retarded and advanced
kernels are supported on the cone**, $G_{\mathrm{ret}}=\delta(t-R/c)/(4\pi R)$ and
$G_{\mathrm{adv}}=\delta(t+R/c)/(4\pi R)$, and the pole prescription chooses the half: the retarded kernel
lives on the future cone, the advanced on the past, while the Feynman prescription treats the two poles
asymmetrically and is therefore a boundary value rather than a solution selected by a cone support
(*The Klein–Gordon Propagator and Its Green's Functions in Biquaternionic Form*,
*Exercise: The Retarded Potentials and the Green's Function*). With a mass the support leaves the cone: the
kernels *acquire support inside the cone rather than on it*, the sharp light-cone delta acquiring a tail in
the Bessel functions, and the closed form
$J_0(\mu\sqrt{t^{2}-r^{2}})$ is valid precisely in the interior of the future cone
(*Bispinor Fields and the Fundamental Solution of the Generalized Maxwell–Dirac Equation*).

**The physical interpretation** is that the cone is not only the boundary of the dynamics but its carrier:
the propagator is singular exactly on the cone, the causal kernels are distributions supported on it, and
the passage from massless to massive is the passage from a support on the cone to a support inside it. The
cone is where a signal is, not merely where it may not exceed.

### The cone as the boundary of the positive and the state cone

In the informational sector the same set is the boundary of positivity, and the corpus reads three faces of
that boundary.

The **positive cone** of the Hermitian sector is the future light cone of the norm: for
$\tilde H=h_0e_t+i\vec h$, positivity is $\langle\tilde H\rangle_{\natural}=h_0^{2}-\lvert\vec h\rvert^{2}\geq0$ together
with $h_0\geq0$, that is $h_0\geq\lvert\vec h\rvert$, and this cone is **self-dual** with respect to the
trace pairing, which is the algebraic reason the pairing serves at once as the Born rule and as the duality
that makes the measurement formalism work (*POVMs and the Positive Cone in Biquaternionic Form*). The
**states** are its trace-one slice: $\tilde{Ϛ}=\tfrac12(e_t+i\vec r)$ with
$\lvert\vec r\rvert\leq1$, the closed unit ball whose boundary — the pure states — is at once the
idempotents, the extreme rays of the cone and the zero divisors at trace one
(*The Bloch Ball as the Trace-One Slice of the Future Light Cone*). The **entropy** is written in the
biquaternion-norm coordinate and leaves the pure states, which are the cone, with **infinite slope**
(*Von Neumann Entropy and the Biquaternion Norm*). Two further readings attach to the same boundary: the
fringe visibility of the double-slit experiment obeys $V^{2}+P^{2}=\lvert\vec r\rvert^{2}\leq1$ with
equality exactly on the cone, so maximal contrast is the statement that the which-path state is a zero
divisor (*The Double-Slit Experiment in Biquaternionic Form*); and the fully polarised states of light,
which are the points of the Poincaré sphere, are exactly the norm cone of the Hermitian sector, the
Pancharatnam phase being the **holonomy of the natural connection on the cone**, with curvature half the
area form of the sphere (*Pancharatnam's Phase and the Polarization Sphere in Biquaternionic Form*).

The boundary is also **the image of the cone under the positivity map**. The map
$\tilde Q\mapsto\tilde Q^{*}\tilde Q$ sends the units into the interior of the Hermitian cone,
$P^{\circ}=\{\tilde Q^{*}\tilde Q:\langle\tilde Q\rangle_{\natural}\neq0\}$, and the sector part of the zero-divisor locus is the
isotropic cone of $\mathbb{M}_+$; on $\mathbb{M}_+$ the Krein cone is the full light cone of the interval,
with the Hermitian cone as its future nappe (*Positivity and the Hermitian Cone of the Biquaternioid Algebra with Hermitian Adjoint*, *Indefinite Positivity and the Krein Cone of the Biquaternioid Algebra*). The edge
of the state space is therefore the image of the cone and its interior the image of the invertible region, so
the positivity of the dagger and the degeneracy of the norm meet on the same boundary.

The same reading fixes the reach of the whole cone picture. The Bloch ball is canonical *because the algebra
supplies the cone*; for a three-level system the state space is eight-dimensional while the positive cone of
$\mathbb{M}_+$ is four-dimensional, so **no cone of a quadratic form carves out the qutrit state space**
(*The Generalized Bloch Ball for Spin 1 in the Biquaternion Framework*). The cone is the state boundary of
the two-level system and of the photon, and its sufficiency stops there.

**The physical interpretation** is that the probability band reads the cone as the edge of what can be
measured: inside it lies the ball of mixed states, on it the pure states and the fully polarised light, and
the map from the algebra's norm to the space of states is exactly the map from the cone to that edge. The
qutrit is the witness that the edge is a feature of the quadratic form and not of statehood as such.

### The cone as the causal and informational boundary

The material band reads the cone as the line between the possible and the impossible, and the corpus states
that reading in several physical settings.

An **exchange of information between two events along a light signal is possible exactly when their
displacement is null**, and because a null displacement is a zero divisor the channel through which signals
pass is the cone itself; the cone forbids the spacelike separations and carries the null ones
(*The Relativistic Exchange of Information and Clock Synchronisation in Biquaternionic Form*,
*Causality and the Light Cone as an Information Barrier in Biquaternionic Form*). The **Rindler horizon is
the zero-divisor cone** of the material sector, and the modular flow of the Unruh construction is read as the
biquaternionic boost flow and its horizon as the algebraic null cone; the identification of the flow with the
boost is the imported Bisognano–Wichmann theorem, not a consequence of the horizon being the cone
(*The Unruh Effect in Biquaternionic Form*). At a **black-hole horizon** the local light cone at each point
is the zero-divisor cone of that point's copy of $\mathbb{M}_-$ — the local statement — while the horizon as
a whole is a global object the pointwise algebra does not see (*Hawking Radiation in Biquaternionic Form*).
The **characteristic surfaces of the wave operator are the light cones**, and a discontinuity on the cone is
not a shock: it stays on the cone and does not steepen (*Shock Electromagnetic Waves*). In **velocity space**
the cone is the absolute of the hyperbolic geometry and the boundary at infinity: it is at infinite geodesic
distance from every velocity, and its ideal points are exactly the lightlike elements, the ones the algebra
cannot invert (*Velocity Space as Hyperbolic Geometry in Biquaternionic Form*). Under the **conformal group**
the inversion is undefined precisely on the cone, and all four families of the group preserve it, so the cone
is the invariant object of conformal geometry and is native to the algebra
(*The Conformal Group in Biquaternionic Form*). In a **medium** the algebraic null cone is the optical
metric's cone: the framework's cone has aperture $c$ and the optical cone aperture $1/n$, so the light cone
of the corpus's zero-divisor reading is the light cone of the medium's optical geometry, and there is no real
null cone below cutoff (*The Effective Optical Metric of the Local Complex Structure*,
*The Local Complex Structure and the Speed of Light*).

**The physical interpretation** is that every causal notion of the corpus — signal, horizon, characteristic,
absolute, inversion, medium — is the one cone, read in the vocabulary of the situation. The global object
that sits on it, the horizon, is the object the pointwise algebra cannot itself carry.

### The cone in the rest of the physics

Several further physical readings have sense under the twelve structures, and they are gathered here.

**Mass has four readings, and two of them detect the cone.** The norm vanishes on it and the rank of the
Hermitian square drops there, while the charge and the scale are defined only off it — the compact label
because the unitary slice is the complement of the cone, the polar scale because its representation requires
a nonzero norm; only the massless elements are detected by the norm and the rank together (*The Four
Readings of a Biquaternion: Norm, Rank, Charge and Scale*). The **Krein form** is the indefinite partner of the Born pairing and carries the
**Krein cone**, the set of elements of non-negative Krein norm with respect to which the framework's
indefinite-sector positivity is stated; its inertia is $(1,3,0)$ on the complexified Hermitian subspace and
$(2,6,0)$ over $\mathbb{R}$ (*Indefinite Positivity and the Krein Cone of the Biquaternioid Algebra*).
The **vacuum** lies on the cone: the minimal idempotent $\tilde\Pi(\vec u)$ is null for every
unit $\vec u$, so $e_t=\tilde\Pi(\vec u)+\tilde\Pi(-\vec u)$
decomposes the unit along two null directions — the algebraic shape of a light-cone frame — and the cone is
the union of the rays that the projectors single out (*The Biquaternion Vacuum as a Minimal Idempotent*).
The **Lorentz group is the group of norm automorphisms** whose nonzero null vectors are the zero divisors,
and the construction realises the closed forward cone only, with no spacelike region and no past cone
(*The Lorentz Group as Biquaternion Norm Automorphisms*). Under **twistors** the null cone of $\mathbb{B}$ is
a cone over the Segre quadric $\mathbb{P}^1\times\mathbb{P}^1$, its two rulings the two families of chiral
spinor lines, and the comparison is sharp: the biquaternion norm is a general plain bilinear form whose null
cone is a complex quadric, while the twistor form is Hermitian of signature $(2,2)$ whose null set is the
real cone that defines the conformal structure (*Twistor Theory and Biquaternions*). In **Dirac matter** the
emergent cones of condensed matter — the Dirac cones of graphene at the Fermi level, the surface Dirac cone
of a topological insulator protected by time-reversal symmetry — are the same shape in a different
substrate, the massless linear dispersion appearing where a lattice symmetry forbids a gap
(*Dirac Matter: Graphene, Dirac Cones and Topological Insulators in Biquaternionic Form*).

**The physical interpretation** is that the cone is an attractor for the framework's physical vocabulary:
mass, positivity, the vacuum, the symmetry group, the projective geometry and the emergent cones of matter
all find their statement in it, and the framework predicts nothing by this, but it collects. The
Ginzburg–Landau-style caution belongs here: the Dirac cone of graphene is an ally of the algebraic cone and
not the same object, and the corpus keeps the two apart.

### The cone in the twelve-structure mathematics

The grid itself has a theorem about the cone, and it is the mathematical form of the part above.

**The cone is the mark of the four general products.** Among the twelve structures the zero-divisor set is
the punctured cone exactly for $\mathrm{GPA}$, $\mathrm{GPS}$, $\mathrm{GQA}$ and $\mathrm{GQS}$, and for no
other; the eight derived sets are strictly larger, the six antisymmetric and scalar-valued symmetric
structures covering the whole punctured space and the two remaining symmetric structures
$\mathrm{SPA}$ and $\mathrm{SQS}$ carrying the enlarged set
$(\{Q_t=0\}\cup\mathcal{C})\setminus\{0\}$. Hence the **corollary** that the punctured cone is contained in
the zero-divisor set of each of the twelve and is equal to the set of exactly four: the cone is the largest
subset on which the twelve agree, and an element of vanishing norm admits an annihilating factor in all
twelve products. The corollary also breaks the ring-theoretic picture on the derived structures, since
$\vec e_x$, of norm $1$, is a zero divisor of $\mathrm{SPA}$ and of $\mathrm{SQS}$ — a zero divisor need not be a
non-unit unless the product has a two-sided unit (*Zero Divisors in the Algebraic Structures over the
Biquaternioid $\mathbb{C}$ Space*).

The four **forms** are the grid's second statement about the cone. The form of each family is one of $\langle\cdot,\cdot\rangle$,
$\langle\cdot,\cdot\rangle_{*}$, $\langle\cdot,\cdot\rangle_{\natural}$, $\langle\cdot,\cdot\rangle_{\natural*}$; $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{*}$ are definite on each sector and **carry no cone there**, while $\langle\cdot,\cdot\rangle_{\natural}$ and $\langle\cdot,\cdot\rangle_{\natural*}$ are
indefinite and carry the light cone. The interval $\langle\cdot,\cdot\rangle_{\natural}$ has signature $(3,1)$ on the material sector and
$(1,3)$ on the informational one, the same form with its inertia reversed by the sector; $\langle\cdot,\cdot\rangle_{\natural*}$ has realified
signature $(2,6)$ and coincides with $\pm\langle\cdot,\cdot\rangle_{\natural}$ on the two sectors. The interval is **multiplicative** on the general
quaternionic bilinear product, so the units and the zero divisors of that product are closed and the light
cone is closed under composition. On the whole algebra the null set of $\langle\cdot,\cdot\rangle$ is not the light cone at all but a
complex quadric of real dimension six (*The Four Forms, the Four Algebraic Norms and the Change of Scalars*,
*The Twelve Structures Compared: Product, Law and Form*). The indefinite-sector positivity statements are
made with the **Krein cone** of the negative of the interval
(*Indefinite Positivity and the Krein Cone of the Biquaternioid Algebra*).

Two further grid statements belong here. The cone's **isotropic lines are its Peirce lines**: the doubly null
lines, the isotropic lines that lie in the norm cone as well, are exactly the Peirce lines
$\mathbb{C}(e_t\pm i\vec u)$ spanned by the rank-one Hermitian idempotents, each generating a
minimal left and a minimal right ideal of complex dimension two all of whose elements are zero divisors, and
the intersection of the cone with the Krein null set is the union of those lines, a cone of real dimension
four (*The Isotropic Structure of the General Quaternionic Sesqualgebra*, *Ideals and Peirce Decomposition of the Biquaternion Algebra*). And the cone is the **boundary of the Hermitian level sets**: the level sets of
the Hermitian form are the real hyperboloids — the hyperboloid model of hyperbolic space — against the
complex hypersurfaces of $\langle\cdot,\cdot\rangle_{\natural}$, and on a Minkowski slice the intersection degenerates to the two nappes of the
light cone, whose future nappe is the Hermitian cone (*The Krein Level Sets and the Hyperbolic Structure*).

**The physical interpretation** is that the cone is the fixed point of the grid: it survives every change of
product as a degeneration locus, it is the exact locus of four of the twelve, and it is carried by exactly
two of the four forms. If the framework is an attractor, the cone is the first thing it attracts, because
the norm is the one quadratic form every band inherits.

## Physical Interpretation

The ledger of the article, in the comparative form of the pair of bands.

| Statement | Status | Owner |
| --- | --- | --- |
| The cone is one set, shared by the two bands | Theorem | *The Light Cone as the Biquaternion Zero-Divisor Cone* |
| The cone is the boundary of invertibility of the composition | Theorem | *The Four General Products and Their Physical Readings* |
| The cone is the rank-drop locus of the probability | Theorem | *The Biquaternioid General Plain Sesqualgebra (GPS) over $\mathbb{C}$* |
| The nilpotent index is two in the composition and three in the probability | Theorem | this article, recomputed |
| The cone is the null set of the interval and of no other of the four forms | Theorem | this article, recomputed |
| The cone is a degeneration locus of all twelve rows, and the exact invertibility boundary of the four general products | Theorem | this article, recomputed; *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket* |
| The cone is absorbing for exactly the four general products | Theorem | this article, recomputed |
| The sector sign meets the cone on the pure part, the gauge metric on the two sectors | Theorem | this article, recomputed; *The Symplectic Form and the Biquaternion Norm Cone* |
| The four forms are the forms of the four families of the grid, one to a family | Theorem | *The Twelve Structures Compared: Product, Law and Form* |
| The massless limit is a degeneration of the symbol, of complex rank four to two | Theorem | *Conformal Invariance and the Massless Limit in Biquaternionic Form* |
| The sandwich collapses from complex rank four to rank one on the cone | Theorem | *The 2×2 Matrix Operator Representation $M_2(\mathbb{C})\otimes M_2(\mathbb{C})$ of Biquaternions* |
| The cone is the absorbing set of the composition | Theorem | *The Biquaternioid General Quaternionic Algebra (GQA) over $\mathbb{C}$* |
| A left multiplication by a null parameter collapses the form, its image inside the cone | Theorem | *The Biquaternioid General Quaternionic Algebra (GQA) over $\mathbb{C}$* |
| The norm is a character of the unit group, so $\langle\tilde Q\rangle_{\natural}$ labels masses as characters, not eigenvalues | Interpretation | *The Biquaternioid Symmetric Quaternionic Algebra (SQA) over $\mathbb{C}$* |
| The interval measures every direction and normalises none on the cone | Interpretation | *The Biquaternioid Symmetric Quaternionic Algebra (SQA) over $\mathbb{C}$* |
| The gauge metric equals the interval up to sign on the two sectors, $\langle\cdot,\cdot\rangle_{\natural*}=\pm\langle\cdot,\cdot\rangle_{\natural}$ | Theorem | *The Four General Products and Their Physical Readings* |
| The pure states are the intersection of the gauge-metric null set, the cone and the trace-one slice | Theorem | *The Biquaternioid General Quaternionic Sesqualgebra (GQS) over $\mathbb{C}$* |
| The image of the sesquilinear square is the state cone, its boundary the pure states | Theorem | *The Biquaternioid General Plain Sesqualgebra (GPS) over $\mathbb{C}$* |
| A massless element carries a boundary state, not a null state | Interpretation | this article |
| The massless momentum and a pure state are one element read in two sectors | Interpretation | *The Null Four-Momentum: What the Cone Derives and What It Does Not* |
| One momentum carries one face in each band, imaginary in the composition and positive in the probability | Interpretation | this article |
| The cone is the common floor of the massless spectrum, not its separator | Interpretation | this article |
| The two vocabularies projectivise the cone to the same sphere | Interpretation | this article |
| The punctured cone is a smooth complex three-manifold and its apex is its only singular point | Theorem | *The Topology of the Zero-Divisor Cone* |
| The link of the cone is an $S^1$-bundle over $S^2\times S^2$, with $\pi_y\cong\mathbb{Z}$, so the apex is a genuine singularity | Theorem | *The Topology of the Zero-Divisor Cone* |
| The projectivised cone is the Segre quadric, its two rulings the chiral null planes | Theorem | *The Null Quadric and Its Projective Geometry* |
| The retarded and advanced kernels are supported on the cone, where the invariant kernel is singular | Theorem | *The Biquaternion D'Alembertian and Its Green's Functions* |
| A mass moves the kernel's support inside the cone, the light-cone delta acquiring a Bessel tail | Theorem | *The Klein–Gordon Propagator and Its Green's Functions in Biquaternionic Form* |
| The positive cone of the Hermitian sector is the future light cone of the norm, self-dual under the trace pairing | Theorem | *POVMs and the Positive Cone in Biquaternionic Form* |
| The entropy has infinite slope at the cone | Theorem | *Von Neumann Entropy and the Biquaternion Norm* |
| The fully polarised states are the norm cone of the Hermitian sector, and the Pancharatnam phase is the holonomy on the cone | Theorem | *Pancharatnam's Phase and the Polarization Sphere in Biquaternionic Form* |
| Maximal double-slit contrast is the which-path state lying on the cone | Theorem | *The Double-Slit Experiment in Biquaternionic Form* |
| The qutrit state space is not a cone slice of the framework's form | Theorem | *The Generalized Bloch Ball for Spin 1 in the Biquaternion Framework* |
| A signal passes between two events exactly when the displacement is null | Theorem | *The Relativistic Exchange of Information and Clock Synchronisation in Biquaternionic Form* |
| The Rindler horizon is the zero-divisor cone and the modular flow is the boost flow | Interpretation | *The Unruh Effect in Biquaternionic Form* |
| At each point of a horizon the local light cone is that point's zero-divisor cone, the horizon itself being global | Interpretation | *Hawking Radiation in Biquaternionic Form* |
| The cone is the absolute of velocity space and the boundary at infinity | Theorem | *Velocity Space as Hyperbolic Geometry in Biquaternionic Form* |
| Conformal inversion is undefined on the cone, and the four conformal families preserve it | Theorem | *The Conformal Group in Biquaternionic Form* |
| In a medium the algebraic null cone is the optical cone, aperture $c$ against $1/n$ | Theorem | *The Effective Optical Metric of the Local Complex Structure* |
| The norm and the rank readings of mass detect the cone, and only the massless elements are detected by both at once | Interpretation | *The Four Readings of a Biquaternion: Norm, Rank, Charge and Scale* |
| The vacuum is a minimal idempotent on the cone, the unit decomposing along two null directions | Interpretation | *The Biquaternion Vacuum as a Minimal Idempotent* |
| The projective null cone is a cone over the Segre quadric, while the twistor form's null set is the real conformal cone | Theorem | *Twistor Theory and Biquaternions* |
| The cone is the mark of the four general products and is contained in the zero-divisor set of all twelve | Theorem | *Zero Divisors in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* |
| $\langle\cdot,\cdot\rangle_{\natural}$ and $\langle\cdot,\cdot\rangle_{\natural*}$ carry the cone while $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{*}$ carry none, and the null set of $\langle\cdot,\cdot\rangle$ is a complex quadric of real dimension six | Theorem | *The Four Forms, the Four Algebraic Norms and the Change of Scalars* |
| Indefinite-sector positivity is stated with the Krein cone of the negative interval | Theorem | *Indefinite Positivity and the Krein Cone of the Biquaternioid Algebra* |
| In the four forms the cone is one of four null sets: the plain form's is a different complex cone of real dimension six, the Hermitian form's is the origin alone and the Krein form's is the Krein cone of real dimension seven | Theorem | *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space* |
| The cone's real dimension drops to four on the vector subspace and to three on the quaternion subspace and on the sectors | Theorem | *Remarkable Subspaces and the Four Forms* |
| The units are the complement of the cone, and the real slice's link is $S^2\sqcup S^2$ against the complex link's $S^1$-bundle over $S^2\times S^2$ | Theorem | *The Biquaternion Unit Group as a Topological Group*; *Biquaternion Lorentzian and Conformal Geometry* |
| The cone is where squaring is affine and preserves the cone, the part of the square's critical set on which the square can collapse | Theorem | *The Zero Divisors and the Singular Julia Sets* |
| For the parameter zero the idempotents lie on the Julia set of the squaring, and the singular Julia set contains a complex surface | Theorem | *The Zero Divisors and the Singular Julia Sets* |
| The natural square vanishes exactly on the cone and the sesquilinear square only at the origin | Theorem | *The Squares and the Positive Cone of the Biquaternioid Sesqualgebra* |
| The positivity map sends the units into the interior of the Hermitian cone and the cone onto its boundary | Theorem | *Positivity and the Hermitian Cone of the Biquaternioid Algebra with Hermitian Adjoint* |
| The cone's isotropic lines are the Peirce lines, the doubly null lines, and the cone meets the Krein null set in their union, a cone of real dimension four | Theorem | *The Isotropic Structure of the General Quaternionic Sesqualgebra* |
| The level sets of the Hermitian form are the real hyperboloids, whose future nappe on a Minkowski slice is the Hermitian cone | Theorem | *The Krein Level Sets and the Hyperbolic Structure* |
| The annihilator of a cone element is a plane inside the cone, and the killers of a lightlike element are lightlike | Theorem | *Annihilators in the Biquaternioid Structures over $\mathbb{C}$* |
| The four planes of a cone element are one plain plane read through the two conjugations | Theorem | *Annihilators in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* |
| The left and right annihilators differ exactly in $\mathrm{GPA}$ and $\mathrm{GQS}$, and only at a cone element | Theorem | *Annihilators in the Biquaternioid Structures over $\mathbb{C}$* |
| The four general products have one zero-divisor set and four root sets of zero: pure cone, whole cone, origin, $\overline{\tilde Q}\tilde Q=0$ | Theorem | *Square Roots of Zero and the Nilpotents in the Biquaternioid Structures over $\mathbb{C}$*; *Square Roots of a General Element in the Biquaternioid Structures over $\mathbb{C}$* |
| The root-set order $\{0\}=Z_3\subsetneq Z_1\subsetneq Z_2$, $Z_3\subsetneq Z_4\subsetneq Z_2$, $Z_1\cap Z_4=\{0\}$ | Theorem | *Square Roots of Zero and the Nilpotents in the Biquaternioid Structures over $\mathbb{C}$* |
| A state is a zero divisor that is not square-zero, so the non-invertible set is larger than the lightlike one | Interpretation | *Square Roots of Zero and the Nilpotents in the Biquaternioid Structures over $\mathbb{C}$*; *Square Roots of One and the Idempotents in the Biquaternioid Structures over $\mathbb{C}$* |
| $m=0$, the mass scale, and the transverse reduction | Imported | *The Null Four-Momentum: What the Cone Derives and What It Does Not* |

The two vocabularies are the same cone read twice, and the reading is what the comparison adds. The
composition reads a null element as an **operation that cannot be inverted**: the norm forgets the scale,
so what a non-invertible element still carries is a direction, and the projectivised cone is the
**celestial sphere** of the material sector, the sphere of lightlike directions with its chirality and its
little-group phase (*The Celestial Sphere of the Null Cone: Null Directions, Chirality and the Phase*). The
probability reads the same element as a **boundary state**: the sesquilinear square of a null element is a
positive rank-one element, and the projectivised boundary of the state cone is the sphere of the pure
states (*The Bloch Ball as the Trace-One Slice of the Future Light Cone*). That the two spheres are one
sphere, the celestial sphere of the momentum and the sphere of the pure states, is the sharpest
comparative form of the article's thesis, and it is the photon's own identity, since the same null
four-momentum whose direction is a point of the sky is the pure state a detector reports (*The Null Four-Momentum: What the
Cone Derives and What It Does Not*). The comparison owns the contrast of the two
vocabularies and the coincidence of the two spheres; the sphere itself, with its metric, its bundle and
its little group, is owned elsewhere.

## Boundaries

The boundaries of this article are drawn to be crossed. The framework is at its beginning, not its end, and
the twelve structures act as an attractor: anything that has sense under the grid about the vanishing of the
norm is quoted here, and this article is expected to grow as the corpus grows. A statement quoted here also
stays in its own article, and the owner is cited; ownership is not a prohibition on restating.

- **What this article originated.** The two jobs of the cone in the two bands; the rank of the left
  multiplication across the twelve rows; the nilpotent index two against three; the cone as the null set of
  the interval and of no other of the four forms; the absorbing property for the four general products; the
  sector-sign and gauge-metric readings; the roster of massless particles and what separates them; and the
  reading that the two vocabularies projectivise the cone to one sphere. These are this article's to define,
  and the other articles cite it for them.
- **The earlier fencing is withdrawn.** The first version drew four boundaries — the single element elsewhere,
  the grid and the zero-divisor sets of the twelve elsewhere, the cone criterion and its topology elsewhere,
  and no dynamics with the photon's polarisation elsewhere. All four were wrong, for the reason above: the
  framework is at its beginning, and a boundary that forbids an article from stating what has sense under the
  grid works against the grid. They are withdrawn, and the statements they fenced are now gathered in the
  tenth part.
- **What is cited and not yet restated.** The operator rows of the twelve structures (*The Operators of the
  Twelve Structures: Multiplication, Adjoint and Bracket*), the full element-level derived/imported list of
  the null momentum (*The Null Four-Momentum: What the Cone Derives and What It Does Not*), the polarisation
  metric and the helicity operator of the photon (*The Photon in Biquaternionic Form*), and the
  reconstruction of a state space from a ternary product (*Why the Fourth Product Is a Gauge Structure and
  Not a State Space*). These are the next boundaries to cross, and the crossing is a matter of the corpus's
  need and not of a rule.

## Summary

The zero-divisor cone is the one set that the general plain algebra and the general plain sesqualgebra of
biquaternions share unchanged, and it is the physical locus of the massless particles. In the composition
band it is the boundary of invertibility, and the physics of the boundary is propagation at $c$: the
element-level consequences of the null shell are *The Null Four-Momentum: What the Cone Derives and What It
Does Not*'s, and the direction of a null momentum is preserved by the rotor group. In the probability band
it is the boundary of the state cone: the sesquilinear square is positive for every nonzero element and
never vanishes, so the cone is not a locus of vanishing probability, and the square drops from rank two to
rank one exactly on the cone, which makes the massless slice the pure-state boundary of the state cone.
The nilpotent index of the cone rises from two in the first band to three in the second, and the shift is
a shift of the pure isotropic part alone, the idempotent multiples being nilpotent in neither band. The
cone itself is the null set of the interval
$\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)$ and of no other of the four forms, so the
cone belongs to the interval and the two products give it its two jobs. Read across the grid, the cone is a
degeneration locus of all twelve rows and the exact boundary of invertibility and the absorbing set of
exactly the four general products, and the other two indefinite forms meet it on one remarkable subspace
each, the sector sign on the pure part and the gauge metric on the two sectors. The twelve readings are
given one by one in the third part, each with its physical interpretation: the four general products
degenerate exactly on the cone, the two algebra-valued symmetric rows on the pure family and the cone
together, the two central-valued symmetric rows not at all, and the four antisymmetric rows nowhere in
particular because they are already singular off the cone. The corpus reads the interval
sharply in two ways that this article recorded only late: it is the comparison that measures every
direction and normalises none, and its gauge cousin $\langle\cdot,\cdot\rangle_{\natural*}$ coincides with it up to sign on the two sectors, so
the pure states are the intersection of the gauge-metric null set, the cone and the trace-one slice. In the
composition the cone is also the absorbing set of the product, since one lightlike factor forces a
lightlike composite, and the left multiplication by a null parameter collapses the form and maps every
element into the cone; the same multiplicativity makes the norm a character of the unit group, so a mass
label on that row is a character and not an eigenvalue. The massless particles are the
case list: the photon is one element read in two sectors, an imaginary multiple of a projector in the
composition and a positive multiple of the same projector in the probability, and the graviton, the
Rarita–Schwinger field and the chiral fermion sit on the same cone, distinguished from one another by a
helicity that the cone does not carry. The element-level division between what the cone derives and what it
does not is *The Null Four-Momentum: What the Cone Derives and What It Does Not*'s; what the comparison adds
is the rank-one boundary in the probability band and the two jobs of the one set. Finally, the word
"cone" is used for three sets in the corpus — the zero-divisor cone of this article, the state cone of the
informational sector and the one-dimensional ray that normalises a probability — and keeping them apart is
what makes the comparison readable.

The tenth part gathers the rest, and it is deliberately open. The cone is read there as the singular set of
the algebra and its link, as the support of the causal kernels, as the boundary of the positive cone whose
entropy has infinite slope there, as the Rindler horizon and the medium's optical cone, as the absolute of
velocity space and the invariant of the conformal group, as the vacuum's own locus, as the projective Segre
quadric and the twistor form's real cone, and as the mark of the four general products, contained in the
zero-divisor set of all twelve. The gathering is not finished: the cone is the framework's attractor, and
the parts of the corpus that have not yet been read for it are expected to be read for it next. The
gathering was extended by the mathematics of the cone that names no product: the cone is one of four null
sets — the Krein cone one dimension larger, the complex cone of $\langle\cdot,\cdot\rangle$ a different six-dimensional set, the
Hermitian form with no cone — and its dimension drops to four on the vector subspace and to three on the
quaternion subspace and the sectors; it is the complement of the unit group, with the link $S^{1}$-bundle
over $S^{2}\times S^{2}$ against the real slice's $S^{2}\sqcup S^{2}$; it is where squaring is affine, the
part of the square's critical set on which the square can collapse, and for the parameter zero the projectors
lie on the Julia set of the squaring; it is the largest nontrivial vanishing
set of a square, the natural square vanishing on it while the Born square vanishes only at the origin; it
is the image of the positivity map and the boundary it puts on the state cone; its isotropic lines are the
Peirce lines, the doubly null lines in which the cone meets the Krein null set; and its Hermitian level-set
companion is the real hyperboloid of hyperbolic space. It is also the annihilator locus, the plane in
which a null direction kills only null directions, and the root set of zero, the largest square-zero set
of the composition, the whole cone of the interval, the origin of the probability and the subfamily
$\overline{\tilde Q}\tilde Q=0$ of the gauge, with the states as the remainder of the cone that is
non-invertible without being lightlike.

## Summary of Notation

- $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$, $\vec e_\mu^{2}=-e_t$, $\vec e_x\vec e_y=\vec e_z$.
- ${}^{\natural}$ natural conjugation; $\bar{\cdot}$ coefficient conjugation; ${}^{*}=\bar{\cdot}\circ{}^{\natural}$ Hermitian conjugation; $\tilde Q^{\flat}=-\tilde Q^{*}$.
- $\mathrm{Sc}$ scalar part, $\mathrm{Tr}=2\,\mathrm{Sc}$; $\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}=\sum_\mu Q_\mu^{2}$ the biquaternion norm, $\langle\tilde Q\rangle_{\natural}=\det\mathsf{M}_2(\tilde Q)$.
- $\tilde P\tilde Q$ the plain product (composition, GPA); $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ the plain sesquilinear product (probability, GPS).
- $\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q)$ the sector sign; $\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})$ the probability weight; $\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)$ the interval; $\langle\tilde P,\tilde Q\rangle_{\natural*}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})$ the fourth form.
- The cone is $\{\tilde Q\neq0:\langle\tilde Q\rangle_{\natural}=0\}$, the zero-divisor set; pure means $\mathrm{Sc}\,\tilde Q_1=0$, isotropic means $\sum_k Q_{1k}^{2}=0$.
- "The cone" without qualification is the zero-divisor cone; the state cone is the future cone of $\mathbb{M}_+$, and the cone of an operation is the ray $\mathbb{R}_{\ge0}e_t$. The gauge metric has its own null set $\{\langle\cdot,\cdot\rangle_{\natural*}=0\}$.
- The twelve rows: GPA, GPS, GQA, GQS the four general products; SPA, SPS, SQA, SQS the symmetric parts; APA, APS, AQA, AQS the antisymmetric parts; $L_{\tilde P}$ the left multiplication of the row, of rank read on the eight real parameters; $\Theta_{\tilde Q}$ the sandwich $\Theta_{\tilde Q}(\tilde Q_2)=\tilde Q\tilde Q_2\tilde Q^{*}$.
- $\mathbb{M}_\pm$ the anti-Hermitian and Hermitian sectors; $\mathbb{H}_{\mathbb{B}}$ the real-quaternion subspace; $\mathbb{C}_{\mathbb{B}}$ the centre.
- $\tilde\Pi$ a plain idempotent, $\tilde\Pi^{2}=\tilde\Pi$; $\tilde\Pi(\vec u)=\tfrac12(e_t+i\vec u)$; $\Box=\tilde\nabla\tilde\nabla^{\natural}$.
- $\mathsf{M}_2$ the $2\times2$ matrix model, $\mathsf{M}_2(e_t)=I_2$, $\mathsf{M}_2(\vec e_\mu)=-i\sigma_\mu$; $\mathrm{ISO}(2)$ the massless little group.

## Further Reading

- The cone in the algebra: *The Light Cone as the Biquaternion Zero-Divisor Cone*; *Zero Divisors as a Physical Locus in Biquaternionic Form*; *Square Roots of Zero and the Nilpotents: the Light Cone*.
- The cone in the material sector: *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*; *Causality and the Light Cone as an Information Barrier in Biquaternionic Form*; *The Boost of an Electromagnetic Plane Wave as a Rotation and a Dilation*.
- The cone in the informational sector: *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*; *The Bloch Ball as the Trace-One Slice of the Future Light Cone*; *The Biquaternioid General Plain Sesqualgebra (GPS) over $\mathbb{C}$*; *The Biquaternioid General Plain Sesqualgebra (GPS) over $\mathbb{C}$*.
- The massless particles: *The Null Four-Momentum: What the Cone Derives and What It Does Not*; *The Photon in Biquaternionic Form*; *Canonical Quantization of the Biquaternion Graviton Field*; *Canonical Quantization of the Biquaternion Rarita–Schwinger Field*; *Chiral Fermions in the Biquaternion Framework*; *Conformal Invariance and the Massless Limit in Biquaternionic Form*; *The Celestial Sphere of the Null Cone: Null Directions, Chirality and the Phase*.
- The map of the four products and their forms: *The Four General Products and Their Physical Readings* (which owns the sector collapse $\langle\cdot,\cdot\rangle_{\natural*}=\pm\langle\cdot,\cdot\rangle_{\natural}$).
- The other bands of the grid, for the cone's other faces: *The Biquaternioid General Quaternionic Algebra (GQA) over $\mathbb{C}$* and *The Biquaternioid General Quaternionic Algebra (GQA) over $\mathbb{C}$* (causality, the absorbing set and the collapsing multiplication); *The Biquaternioid Symmetric Quaternionic Algebra (SQA) over $\mathbb{C}$* and *The Biquaternioid Symmetric Quaternionic Algebra (SQA) over $\mathbb{C}$* (coupling, the character and the comparison that normalises none); *The Biquaternioid General Quaternionic Sesqualgebra (GQS) over $\mathbb{C}$* and *The Biquaternioid General Quaternionic Sesqualgebra (GQS) over $\mathbb{C}$* (gauge, the null set and the intersection with the cone); *The Biquaternioid Symmetric Plain Sesqualgebra (SPS) over $\mathbb{C}$* (positivity, the ray that is not the state cone).
- The zero-divisor set of each structure: *Zero Divisors in the Biquaternioid Structures over $\mathbb{C}$* (the twelve readings this article's third part is the cone counterpart of), and the algebraic background in *The Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*, *The 12 Products of the Biquaternioid Complex Space* and *Centre, Units, Zero Divisors and Division Algebras*.
- The other faces of the same cone in the comparison family: *Annihilators in the Biquaternioid Structures over $\mathbb{C}$* (the annihilator plane of a lightlike element and the chirality of the two sides); *Square Roots of Zero and the Nilpotents in the Biquaternioid Structures over $\mathbb{C}$*, *Square Roots of a General Element in the Biquaternioid Structures over $\mathbb{C}$* and *Square Roots of a General Element in the Biquaternioid Structures over $\mathbb{C}$* (the four root sets of zero and the gap between the lightlike displacements and the states); *Square Roots of One and the Idempotents in the Biquaternioid Structures over $\mathbb{C}$* (the states on the cone and the measurement that has no inverse).
- The grid of the twelve structures: *The 12 Products of the Biquaternioid Complex Space*; *The Twelve Structures Compared: Product, Law and Form*; *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket*.
- The cone in the other realisations of the grid: *The Symplectic Form and the Biquaternion Norm Cone* (the cone as the isotropic locus of the sector sign on the phase space, and as the characteristic cone of the d'Alembertian); *The 2×2 Matrix Operator Representation $M_2(\mathbb{C})\otimes M_2(\mathbb{C})$ of Biquaternions* (the collapse of the congruence, from rank four to rank one); *Conformal Invariance and the Massless Limit in Biquaternionic Form* (the massless limit as a degeneration of the symbol); *Decoherence as Idempotent Projection* (the rank-one collapse read as information loss); *Biquaternion Rotations and Lorentz Transformations* (the rank-one stratum under the rotor group).
- The cone as a topological object: *The Topology of the Zero-Divisor Cone* (the singular set, the contractibility, the link); *The Null Quadric and Its Projective Geometry* (the Segre quadric, the two rulings, the polarity).
- The cone in the propagators: *The Biquaternion D'Alembertian and Its Green's Functions*; *The Klein–Gordon Propagator and Its Green's Functions in Biquaternionic Form*; *Exercise: The Retarded Potentials and the Green's Function*; *Bispinor Fields and the Fundamental Solution of the Generalized Maxwell–Dirac Equation* (the support of the causal kernels, the light-cone delta and its Jacobian, the Bessel tail inside the cone).
- The cone as the boundary of the positive cone and of the state cone: *POVMs and the Positive Cone in Biquaternionic Form*; *Von Neumann Entropy and the Biquaternion Norm*; *The Double-Slit Experiment in Biquaternionic Form*; *Pancharatnam's Phase and the Polarization Sphere in Biquaternionic Form*; *The Generalized Bloch Ball for Spin 1 in the Biquaternion Framework* (the future light cone of the norm, self-duality, the infinite-slope entropy, the contrast bound and the Poincaré sphere, and the qutrit as the limit of the cone picture).
- The cone as the causal and informational boundary: *The Relativistic Exchange of Information and Clock Synchronisation in Biquaternionic Form*; *The Unruh Effect in Biquaternionic Form*; *Hawking Radiation in Biquaternionic Form*; *Shock Electromagnetic Waves*; *Velocity Space as Hyperbolic Geometry in Biquaternionic Form*; *The Conformal Group in Biquaternionic Form*; *The Effective Optical Metric of the Local Complex Structure*; *The Local Complex Structure and the Speed of Light* (the null channel, the Rindler horizon, the pointwise horizon cone, the characteristic cone, the absolute, the conformal invariant, the optical aperture).
- The cone in the rest of the physics: *The Four Readings of a Biquaternion: Norm, Rank, Charge and Scale* (the norm and the rank detect the cone); *The Biquaternioid General Quaternionic Sesqualgebra (GQS) over $\mathbb{C}$* (the indefinite metric and the Krein form); *The Biquaternion Vacuum as a Minimal Idempotent*; *The Lorentz Group as Biquaternion Norm Automorphisms*; *Twistor Theory and Biquaternions*; *Dirac Matter: Graphene, Dirac Cones and Topological Insulators in Biquaternionic Form* (the vacuum on the cone, the norm automorphisms, the projective quadric, the emergent cones).
- The cone in the twelve-structure mathematics: *Zero Divisors in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* (the theorem and its corollary); *The Four Forms, the Four Algebraic Norms and the Change of Scalars* (which forms carry the cone); *Indefinite Positivity and the Krein Cone of the Biquaternioid Algebra* (the Krein cone).
- The cone among the four null sets: *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space*; *Remarkable Subspaces and the Four Forms*; *The Krein Level Sets and the Hyperbolic Structure* (the four null sets and the dimensions they drop to on the remarkable subspaces, the Krein cone and the real hyperboloids whose boundary the cone is).
- The cone as the critical set of the square: *The Zero Divisors and the Singular Julia Sets*; *The Biquaternion Quadratic Map and Its Julia Sets* (the affine action of the square on the cone, the critical set and the idempotents on the Julia set of the parameter zero); *The Squares and the Positive Cone of the Biquaternioid Sesqualgebra* (the natural square as the largest nontrivial vanishing set, against the sesquilinear square that vanishes only at the origin).
- The cone as the complement of the units: *The Biquaternion Unit Group as a Topological Group* (the units off the cone, the covering and the homotopy groups); *Biquaternion Lorentzian and Conformal Geometry* (the Minkowski slice, its real light cone and the link $S^{2}\sqcup S^{2}$).
- The cone's isotropic lines and the positivity map: *The Isotropic Structure of the General Quaternionic Sesqualgebra*; *Ideals and Peirce Decomposition of the Biquaternion Algebra* (the Peirce lines, the doubly null lines, the minimal ideals and the cone's intersection with the Krein null set); *Positivity and the Hermitian Cone of the Biquaternioid Algebra with Hermitian Adjoint* (the units mapped into the interior, the cone onto the boundary).
- The conventions of the series: *Conventions in the Biquaternion Universe*.
