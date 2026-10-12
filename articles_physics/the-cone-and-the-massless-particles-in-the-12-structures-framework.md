# __The Cone and the Massless Particles in the 12 Structures Framework__

## Introduction

The general plain algebra and the general plain sesqualgebra of biquaternions are one space read in two
products: the plain product $\tilde P\tilde Q$, and the plain sesquilinear product
$\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$. The companion article *Composition and Probability: the
General Plain Algebra and the General Plain Sesqualgebra of Biquaternions Compared* walks the two
structures section by section and traces every difference to one cause, the Hermitian conjugation in the
second slot. One set survives that comparison unchanged, and it is the set this article is about: the
**zero divisors**, the nonzero elements whose biquaternion norm vanishes. That set is the light cone of
the material sector, and it is where the **massless particles** live in the algebra.

Two questions organise the article, and they are the two the comparison asks of every object.

- **What is the cone in each band?** In the composition it is the boundary of invertibility: a nonzero
  element is invertible if and only if its norm does not vanish, so the cone is exactly the set the plain
  product cannot divide by. In the probability it is the boundary of the state cone: the sesquilinear
  square of a nonzero element is a positive element and is never zero, and it drops from rank two to rank
  one exactly on the cone. The nilpotent index of the cone rises from two in the first band to three in
  the second, and that index shift is the sharpest single contrast of the comparison.
- **Is the cone a property of either product?** It is not. The cone is the null set of the interval form
  $N(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)$, whose diagonal is the biquaternion norm,
  and of the four forms the corpus uses it is the null set of that one alone. The interval is what puts the
  cone into the algebra; the two products are what give it its two jobs.

The two bands are the general members of the grid of the twelve structures, and that grid is the frame the
title names. The cone is cut out by the interval, which is the form of the quaternionic row and not of the
general plain pair alone, so the shared vanishing set of the two bands is a feature of the frame rather
than of one band. The grid, its twelve operations and their operator rows are *The 12 Products of the
Biquaternion Complex Space*, *The Four General Products and Their Physical Readings*, *The Twelve
Structures Compared: Product, Law and Form* and *The Operators of the Twelve Structures: Multiplication,
Adjoint and Bracket*; this article uses the grid and does not rebuild it.

The article then applies the two answers to the massless particles. The photon is the case the corpus has
built; the graviton and the chiral fermion sit on the same cone, and what separates the massless particles
from one another is data the cone does not carry.

The article is organised as follows. The second section fixes the cone as one set, names its two jobs,
reads the cone in the twelve rows and separates the three sets the corpus calls a cone. The third computes
the nilpotent index in the two bands and records the recomputation. The fourth shows that the cone is the
null set of the interval and of no other form, and computes its relation to the sector sign and to the
gauge metric. The fifth reads the cone in the composition band, including the absorbing property, the
collapsing multiplication and the massless limit as a degeneration of the symbol; the sixth reads it in the
probability band, including the collapse of the sandwich. The seventh treats the massless particles. The
eighth separates what the cone derives from what is imported. The closing sections are the ledger, the
summary, the notation table and the literature.

**Conventions.** We use those of the companion articles unchanged. The biquaternion algebra is
$\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$,
$e_k^{2}=-e_0$ and $e_je_k=-\delta_{jk}e_0+\varepsilon_{jkl}e_l$, and $i$ the central scalar imaginary.
The conjugations are the natural conjugation ${}^{\natural}$, the coefficient conjugation $\bar{\cdot}$
and the Hermitian conjugation ${}^{*}=\bar{\cdot}\circ{}^{\natural}$, with
$\tilde Q^{\flat}=-\tilde Q^{*}$. The biquaternion norm is
$N(\tilde Q)=\langle\tilde Q,\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}=\sum_\mu Q_\mu^{2}$,
which is the determinant of the matrix model $\mathsf{M}_2$ with $\mathsf{M}_2(e_0)=I_2$ and
$\mathsf{M}_2(e_k)=-i\sigma_k$. The subspaces are the anti-Hermitian material sector $\mathbb{M}_-$,
the Hermitian informational sector $\mathbb{M}_+$, the real-quaternion subspace
$\mathbb{H}_{\mathbb{B}}$ and the centre $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_0,ie_0\}$.
The material coordinate is $\tilde Q=ict\,e_0+\mathbf{x}$, so that $N(\tilde Q)=-c^{2}t^{2}+\mathbf{x}^{2}$,
and $c=1/\sqrt{\epsilon\mu}$ is the speed of light in the medium. The trace formula is
$\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)=2\langle\tilde P,\tilde H\rangle$. The
plain product is written $\tilde P\tilde Q$ and the plain sesquilinear product
$\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$; a plain idempotent is written $\tilde\Pi$, and the nilpotent
convention for a square-zero element is that of *Conventions in the Biquaternion Universe*.

## One Cone in the Two Bands

### The norm and its vanishing set

The cone is read off one object, the biquaternion norm

$$
N(\tilde Q)=\tilde Q\tilde Q^{\natural}=\sum_\mu Q_\mu^{2}=\det\mathsf{M}_2(\tilde Q).
$$

On the material sector the norm is the Minkowski interval, $N(\tilde Q)=-c^{2}t^{2}+\mathbf{x}^{2}$ for
$\tilde Q=ict\,e_0+\mathbf{x}$, so its zero set is the light cone $|\mathbf{x}|=c|t|$. The algebraic
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
two-sided plain inverse precisely when $N(\tilde Q)\neq0$, the inverse being
$\tilde Q^{\natural}/N(\tilde Q)$, and it has none when $N(\tilde Q)=0$. The plain product is the
operation that composes transformations and iterates a process (*The Ordinary Product and the Material
Sector*), so the cone is the set of elements that cannot be composed further, and the physics of that
failure is propagation, taken up in its own section below.

In the **probability**, the cone is a rank drop. The plain sesquilinear product has no two-sided inverse
at all, and its one-sided inverse exists exactly off the cone, so invertibility is not the distinguishing
signal here. The signal is the rank of the sesquilinear square: the square $\tilde X\star\tilde X$ is a
Hermitian positive element of rank two off the cone and of rank one on it. *Mass, Rank and the Positivity
of the Dagger* proves the criterion and reads the rank drop as a mass label, rank two massive and rank one
massless.

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
Biquaternion Norm Cone*, where a pure-vector phase-space biquaternion $\tilde Z=\mathbf q+i\mathbf p$ is
null exactly when $\lvert\mathbf q\rvert=\lvert\mathbf p\rvert$ and $\mathbf q\cdot\mathbf p=0$: the cone
is the set where the configuration and the momentum magnitudes are equal and the two vectors are
orthogonal, which is the isotropic locus of the sector sign, since $B=-N$ on the pure subspace. There the
cone is a genuinely complex object and not a physical locus: the condition equates two quantities of
different dimension until a symplectic scale is fixed, and the real phase space meets the cone only at the
origin.

### The cone in the twelve rows

The cone is one set, and the twelve rows meet it in different ways. The measurement is the **rank of the
left multiplication**, the map $L_{\tilde P}(\tilde X)=\tilde P\star\tilde X$ read on the eight real
parameters of the algebra. Off the cone a row separates invertible from singular when that rank is eight,
and the table gives the rank for a generic operand off the cone and for an operand on it.

| row | product | rank off the cone | rank on the cone | what the cone is for the row |
| --- | --- | --- | --- | --- |
| GPA | $\tilde P\tilde Q$ | $8$ | $4$ | the boundary of invertibility |
| SPA | $s_{\mathrm{pb}}(\tilde P,\tilde Q)$ | $8$, and $4$ on the pure subspace | $4$ | a degeneration locus, not the whole one |
| APA | $a_{\mathrm{pb}}(\tilde P,\tilde Q)$ | $4$ | $4$ | none: the centre lies in the kernel |
| GQA | $\tilde P^{\natural}\tilde Q$ | $8$ | $4$ | the boundary of invertibility |
| SQA | $s_{\mathrm{qb}}(\tilde P,\tilde Q)$ | $2$ | $2$ | none: the image is the centre |
| AQA | $a_{\mathrm{qb}}(\tilde P,\tilde Q)$ | $6$ | $4$ | a drop, not the whole locus |
| GPS | $\tilde P\tilde Q^{*}$ | $8$ | $4$ | the boundary of invertibility |
| SPS | $s_{\mathrm{ps}}(\tilde P,\tilde Q)$ | $2$ | $2$ | none: the image is the centre |
| APS | $a_{\mathrm{ps}}(\tilde P,\tilde Q)$ | $6$ | $4$ | a drop, not the whole locus |
| GQS | $\tilde P^{\natural}\tilde Q^{*}$ | $8$ | $4$ | the boundary of invertibility |
| SQS | $s_{\mathrm{qs}}(\tilde P,\tilde Q)$ | $8$, and $4$ on the pure subspace | $4$ | a degeneration locus, not the whole one |
| AQS | $a_{\mathrm{qs}}(\tilde P,\tilde Q)$ | $4$ | $4$ | none: the centre lies in the kernel |

Three statements follow, and together they are the grid-level answer to the question of whether the cone
belongs to a product.

- **The cone is a degeneration locus of all twelve.** No row has an invertible left multiplication at a
  point of the cone: the rank is four or less everywhere on it, and eight nowhere. The cone is therefore a
  common boundary of the twelve structures, and in that sense it is one set and not twelve.
- **The cone is the whole degeneration locus of exactly four rows.** For the four general products the
  rank is eight off the cone and four on it, so the cone is exactly the line between invertibility and its
  failure. These are the four rows that carry a unit and an inverse, and for them the cone is what the
  companion article calls the boundary of the band. For the eight parts the left multiplication is already
  degenerate off the cone, which is the operator form of the fact that a part has no unit.
- **The cone is absorbing for exactly those four rows.** The product of a lightlike element with anything
  is lightlike, $N(\tilde P)=0\Rightarrow N(\tilde P\star\tilde Q)=0$, for GPA, GQA, GPS and GQS; it fails
  for the eight parts, where the symmetrisation or the antisymmetrisation mixes a lightlike term with a
  second term that need not be lightlike, and the sum can leave the cone.

The reasons the eight parts degenerate are visible in the table. The four antisymmetric rows have no scalar
part, so the centre lies in their kernel; the two central-valued symmetric rows have the centre for their
whole image, so their operators are of rank two everywhere; and the two algebra-valued symmetric rows SPA
and SQS are singular on the pure subspace $\{Q_0=0\}$ as well, because the symmetrised left multiplication
has the eigenvalues $\tfrac12(\lambda_i+\lambda_j)$ of the anticommutator, whose product carries the factor
$\mathrm{Sc}(\tilde P)^{2}$ and so vanishes on the pure subspace and on the cone alike. The corpus states
the one row it tabulates: *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket*
computes the antisymmetric plain sesquilinear left multiplication as "of real rank six for a unit and four
for a zero divisor", which is the row APS of the table.

### Three sets the corpus calls a cone

The word "cone" is used for three different sets in this corpus, and the comparison is only readable if
they are kept apart.

- **The zero-divisor cone**, $\{\tilde Q\neq0:N(\tilde Q)=0\}$, the null set of the norm. It is the
  subject of this article, and "the cone" without qualification always means this set here.
- **The state cone** of the informational sector, the future cone of $\mathbb{M}_+$, that is
  $\{\alpha e_0+i\mathbf{w}:\alpha\geq\lvert\mathbf{w}\rvert\}$, sliced by $\mathrm{Tr}\,\tilde\varrho=1$
  for the states. It is a cone of *positive* elements, and it is the image of the sesquilinear square; the
  zero-divisor cone is its rank-one boundary, as the next sections show.
- **The cone of an operation**, the one-dimensional ray $\mathbb{R}_{\ge0}e_0$ that is the image of the
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

## The Nilpotent Index: Two against Three

### The composition: square-zero is pure isotropic

In the composition band the nilpotent structure is elementary: an element squares to zero exactly when it
is pure and isotropic,

$$
\tilde X^{2}=0\quad(\tilde X\neq0)\ \Longleftrightarrow\ \tilde X\ \text{pure and isotropic}.
$$

*Pure* means the scalar part vanishes, $\mathrm{Sc}(\tilde X)=X_0=0$. *Isotropic* means the vector part
has vanishing square, $\sum_{k}X_k^{2}=0$. The two conditions together are the criterion
$\det\mathsf{M}_2(\tilde X)=0$ with $\mathrm{Tr}\,\mathsf{M}_2(\tilde X)=0$, which for a $2\times2$ matrix
is exactly nilpotence, and the recomputation below confirms both directions on random elements and on the
parametrised cone $X_1=1$, $X_2=i\cos t$, $X_3=i\sin t$, which satisfies $\sum_k X_k^{2}=1-1=0$ for every
$t$. The pure isotropic cone is therefore the square-zero locus, and its nilpotent index is **two**: the
first power is nonzero and the second vanishes.

The square-zero locus is a proper part of the cone. An idempotent multiple, for instance the Hermitian
idempotent $\tilde\Pi=\tfrac12(e_0+i\hat{\boldsymbol\mu})$ with
$\tilde\Pi^{2}=\tilde\Pi$, has vanishing norm and a nonzero square, so the cone is the disjoint union of
the square-zero elements and the elements whose square is not zero.

### The pairing: nothing squares to zero, and the cone is nilpotent of index three

In the probability band the situation is opposite at the first step and sharper at the second. The scalar
part of the sesquilinear square is a sum of moduli,

$$
\mathrm{Sc}(\tilde X\star\tilde X)=\mathrm{Sc}(\tilde X\tilde X^{*})=\sum_\mu\lvert X_\mu\rvert^{2},
$$

so it is positive for every nonzero element and vanishes only at the origin. Hence there is **no nonzero
element whose sesquilinear square vanishes**: the square-zero elements of the composition band have no
counterpart here at all.

What the same pure isotropic cone does carry in this band is a higher index. For $\tilde X$ pure and
isotropic, the first sesquilinear power is nonzero because its scalar part is a sum of moduli, while the
third power vanishes,

$$
\tilde X\star\tilde X\neq0,
\qquad
(\tilde X\star\tilde X)\star\tilde X=0,
$$

so the cone is nilpotent of **index three**. The matrix model shows why in one line:
$\mathsf{M}_2(\tilde X)$ is nilpotent, $\mathsf{M}_2(\tilde X\star\tilde X)$ is
$\mathsf{M}_2(\tilde X)\mathsf{M}_2(\tilde X)^{\dagger}$, and the product
$\mathsf{M}_2(\tilde X)\mathsf{M}_2(\tilde X)^{\dagger}\mathsf{M}_2(\tilde X)^{\dagger}$ vanishes for
every nilpotent $\mathsf{M}_2(\tilde X)$.

One qualification is needed, and it is the same qualification as in the composition band. The index three
belongs to the **pure** part of the cone. An idempotent multiple is Hermitian and idempotent, so its
sesquilinear cube is itself, $\tilde\Pi\star\tilde\Pi\star\tilde\Pi=\tilde\Pi\neq0$, and its index is
infinite. The index shift is therefore a shift of the pure isotropic cone alone, from two to three; the
idempotent multiples are nilpotent in neither band.

The shift is the sharpest single contrast of the comparison. Lightlike propagation is square-zero in the
operation that composes and cubically-zero in the operation that evaluates.

### The recomputation

Every claim of this section was recomputed in the matrix model with $\mathsf{M}_2(e_k)=-i\sigma_k$, on
$100$ random elements and on the parametrised pure isotropic cone.

| Claim | Recomputation |
| --- | --- |
| $N(\tilde Q)=\det\mathsf{M}_2(\tilde Q)=\sum_\mu Q_\mu^{2}$ | holds on every element drawn |
| $\tilde X^{2}=0$ exactly for pure isotropic $\tilde X$ | both directions hold, random and parametrised |
| $\mathrm{Sc}(\tilde X\star\tilde X)=\sum_\mu\lvert X_\mu\rvert^{2}$ | holds on every element drawn |
| $\tilde X\star\tilde X\neq0$ for $\tilde X\neq0$ | holds on every nonzero element drawn |
| $(\tilde X\star\tilde X)\star\tilde X=0$ on the pure isotropic cone | holds for every $t$ tested |
| $\tilde\Pi\star\tilde\Pi\star\tilde\Pi=\tilde\Pi$ for $\tilde\Pi$ idempotent | holds |

## The Cone Is the Null Set of the Interval and of No Other Form

The comparison uses four forms, and the cone is the null set of one of them. Writing them out is what
shows that the cone is a property of the interval rather than of either product.

The **interval** is the form $N(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)$, whose value is
the sum $\sum_\mu P_\mu Q_\mu$, and whose diagonal is the biquaternion norm,
$N(\tilde Q,\tilde Q)=N(\tilde Q)$. The light cone is its null set by construction.

The four forms are the forms of the four families of the grid, one to a family (*The Twelve Structures
Compared: Product, Law and Form*): $B$ belongs to the plain bilinear family, to GPA and SPA; $N$ to the
quaternionic bilinear family, to GQA and SQA; $H$ to the plain sesquilinear family, to GPS and SPS; and
$K$ to the quaternionic sesquilinear family, to GQS and SQS. The cone is the null set of the interval, so
it is the null set of the form of the **quaternionic bilinear** family and not of the general plain pair:
the natural conjugation is what produces the interval, while the plain product carries the sector sign.

The **sector sign** is $B(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q)$, of signature $(4,4)$ on the
complex space. Its diagonal is

$$
B(\tilde Q,\tilde Q)=\mathrm{Sc}(\tilde Q^{2})=Q_0^{2}-\sum_k Q_k^{2},
$$

which is not the norm: the vector part enters with the opposite sign. On the material sector, where
$Q_0=ict$ and the $Q_k$ are real, the sector sign is $-c^{2}t^{2}-\mathbf{x}^{2}$, a negative definite
form, so the material sector contains no real direction on which $B$ vanishes. The light cone is not the
null cone of the sector sign. *The Ordinary Product and the Material Sector* states the same separation
from the other side, that the sector sign is definite on each sector and has no cone there, so that the
causal structure belongs to the interval.

The **probability weight** is the form $H(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q^{*})$, whose value
is the sum $\sum_\mu P_\mu\overline{Q_\mu}$, of signature $(8,0)$. Its diagonal is

$$
H(\tilde Q,\tilde Q)=\mathrm{Sc}(\tilde Q\tilde Q^{*})=\sum_\mu\lvert Q_\mu\rvert^{2},
$$

which is positive for every nonzero element. A positive definite form has no nonzero null vector, so the
cone is invisible to the probability weight: no element of the cone is null for $H$, and no element
outside it is null either.

The **fourth form** is $K(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})$, the gauge
metric of the quaternionic sesquilinear product, whose diagonal is
$\lvert Q_0\rvert^{2}-\sum_k\lvert Q_k\rvert^{2}$; it is indefinite, of realified signature $(2,6)$,
positive on the centre and negative on the vector subspace.

Its null set is not the light cone, and the comparison is sharper than "different". On the two sectors the
interval and the gauge metric are one form up to sign,

$$
K(\tilde P,\tilde Q)=N(\tilde P,\tilde Q)\ \text{on}\ \mathbb{M}_+,
\qquad
K(\tilde P,\tilde Q)=-N(\tilde P,\tilde Q)\ \text{on}\ \mathbb{M}_-,
$$

which is the sector collapse $K=\pm N$ of *The Four General Products and Their Physical Readings*, with the
sign carried by the sector. Two consequences follow. On the trace-one Hermitian slice the two vanishings
coincide, $K=0\iff N=0\iff$ rank one, and that coincidence is the intersection statement of *The States the
Indefinite Metric Cannot Normalise*: the pure states are the intersection of the gauge-metric null set, the
zero-divisor cone and the trace-one slice, so the cone is at once the locus of light and the boundary of
the state space. Off the two sectors the null sets separate in both directions, with the witnesses
$\tilde Q=e_0+e_1$, where $K=0$ and $N=2$, and $\tilde Q=e_0+i\sqrt{2}\,e_1+e_2$, where $N=0$ and
$K=-2$. The gauge metric therefore contains the cone as a subset and adds to it; it is not the interval.

Of the four, only the interval has the light cone as its null set. The other two indefinite forms meet the
cone, and each meets it on one remarkable subspace: the sector sign on the pure part, where
$B(\tilde Q,\tilde Q)=-N(\tilde Q)$ and $B(\tilde Q,\tilde Q)=N(\tilde Q)$ on the centre, so the two forms
coincide up to sign on the pure subspace and the sector sign vanishes on the pure isotropic elements; and
the gauge metric on the two sectors, where $K=\pm N$. Neither meeting is the whole cone, and each of the
two forms has its own null set, the quadrics $Q_0^{2}=\sum_kQ_k^{2}$ and $K=0$, which contain points off
the cone and miss points of it. The witness $\tilde Q=e_0+i e_1+i e_2+e_3$ has $N=0$, $B=2$ and $K=-2$, so
it lies on the cone and in neither of the other null sets, while $\tilde Q=e_0+e_1$ has $B=K=0$ with
$N=2$, so it lies in both of them and off the cone. The interval is therefore the only one of the four
whose null set is the cone, and the only one that meets the cone in all of it. The statement matters for
the comparison, because it locates the cause of the cone. The cone is not "where the plain product
vanishes" and it is not "where the sesquilinear product vanishes"; neither product is a quadratic form.
The cone is where the interval vanishes, and the interval is the form whose diagonal is the norm. The two
products then take that one set and give it two different jobs, which is what the next two sections read.

## The Cone in the Composition Band: Propagation at the Speed of Light

In the composition the cone is the set of elements that cannot be divided by, and the physics of that
failure is propagation.

The wave operator is the norm of the gradient, $\Box=\tilde\nabla\tilde\nabla^{\natural}$, and a
four-wavevector $\tilde K$ is null exactly when $N(\tilde K)=0$. For such a $\tilde K$ every function of
the phase $\mathrm{Sc}(\tilde K\tilde Q^{\natural})=\langle\tilde K,\tilde Q\rangle$ solves the wave
equation, so the null directions are the directions in which the algebra propagates without dispersion.
Four consequences are derived rather than imported, and they are collected in *The Photon as a Null
Element: What the Cone Derives and What It Does Not*:

- the massless shell is the zero-divisor cone, and it is the only level set of the norm that is a cone;
- the propagation speed is $c$, and $c$ is the same in every inertial frame, because the norm is
  multiplicative, $N(\tilde P\tilde Q)=N(\tilde P)N(\tilde Q)$, so a rotor cannot change the vanishing of
  the norm;
- a null four-momentum has no rest frame, since a rest frame would require a timelike direction;
- a particle on the null shell moves at $c$ for every momentum, not merely in a limit.

The invariance of the cone under the rotor group is the invariant barrier of *Causality and the Light Cone
as an Information Barrier in Biquaternionic Form*: each of the three classes of separation is a union of
orbits of the rotor group, and their common boundary is the cone, so no rotor carries a point of the cone
off it. The massless shell is therefore not merely a locus of velocities; it is a boundary that the
composition's own symmetry group preserves.

Two facts about the material coordinates are worth separating here. The nilpotent cone of the composition
band, the pure isotropic set of the preceding section, is the set of elements whose square vanishes; the
roots of $0$ in the equation $\tilde X^{2}=0$ are exactly those nilpotents, and they are the subject of
*Square Roots: the Local Complex Structure, the Light Cone and the Mass Shell*. A general element of the
light cone need not be nilpotent: the idempotent multiples of the cone have nonzero square, and they are
the elements that carry the rank-one structure used in the next section.

### The cone is absorbing, and the operators that collapse it

The multiplicativity of the norm has a second reading that the frame-independence of $c$ does not exhaust.
If one factor of a product lies on the cone then so does the product,

$$
N(\tilde P)=0\ \Longrightarrow\ N(\tilde P\tilde Q)=N(\tilde Q\tilde P)=0,
$$

so the cone is the **absorbing set** of the composition. *The Interval as the Square and the Charge of the
Material Composition* states it as "composition cannot generate mass": a composite with a lightlike factor
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
$N(\tilde P\tilde Q)=N(\tilde P)N(\tilde Q)$, which is exactly the statement that $N$ is a **character**,
$N:(\mathbb{B}^{\times},\cdot)\to(\mathbb{C}^{\times},\cdot)$, and *Why a Central Product Cannot Compose:
the Radical and the Isotropic Elements* draws the consequence: a mass label built out of $N$ on this row is
a character and not an eigenvalue, an eigenvalue needing a unit and a spectral theory. The comparison adds
the form-side counterpart. *The Quaternion Form as a Product: the Scalar Coupling of Two Material
Operations* reads the interval $N(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)$ — the form
the cone belongs to — as a comparison that "measures every direction and normalises none": its radical is
trivial, so it separates every nonzero element from some partner, and its diagonal vanishes on the cone, so
it separates no lightlike element from itself. That is the exact counterpart in the composition row of the
probability row's statement that the probability weight has no null vector.

The same drop is the algebraic form of the massless limit, and the reading is *Conformal Invariance and the
Massless Limit in Biquaternionic Form*. On shell the four-momentum is a biquaternion $\tilde K$ and the
symbol of the wave operator is its norm: for the massive momentum the norm is $-\mu^{2}\neq0$ and the left
multiplication by $\tilde K$ has complex rank four, while for the massless one the norm vanishes and the
rank is two. In the real count of the table of the second section the drop is eight to four, and it is the
same drop the row GPA shows at every point of the cone. The massless limit is therefore a **degeneration
of the symbol** and not merely the removal of a constant: the symbol acquires a kernel, the propagator
acquires a pole on the light cone, and the equation acquires the gauge-like degeneracy the conformal
symmetry organises. The operator face and the absorbing face are two readings of one rank identity.

## The Cone in the Probability Band: the Boundary of the State Cone

In the probability the cone is the boundary of the state cone, and the passage from the cone to the state
space is one map.

The sesquilinear square lands in the informational sector. For every $\tilde X$ the element
$\tilde X\star\tilde X$ is Hermitian, its scalar part is real and its vector part is imaginary, so it lies
in $\mathbb{M}_+$, and it is positive:

$$
\tilde X\star\tilde X\in\mathbb{M}_+,
\qquad
N(\tilde X\star\tilde X)=\lvert N(\tilde X)\rvert^{2},
\qquad
\mathrm{rank}\,\tilde X\star\tilde X=1\ \Longleftrightarrow\ N(\tilde X)=0.
$$

Writing the image as $\alpha e_0+i\mathbf{w}$ with $\alpha$ real and $\mathbf{w}$ a real vector, the
positivity is the inequality $\alpha\geq\lvert\mathbf{w}\rvert$, and the determinant identity is

$$
\alpha^{2}-\lvert\mathbf{w}\rvert^{2}=\lvert N(\tilde X)\rvert^{2}.
$$

Three statements follow, and together they are the band's reading of the cone.

- **The image is the state cone.** The image of the sesquilinear square is exactly the set of positive
  elements of $\mathbb{M}_+$, that is, the set $\{\alpha e_0+i\mathbf{w}:\alpha\geq\lvert\mathbf{w}\rvert\}$.
  Every positive element is a sesquilinear square, by taking the positive square root, and the map is onto
  by that construction. This set is the future light cone of the informational sector, and *The Spinor
  Space as a Hilbert Space of the General Plain Sesqualgebra* identifies it with the state cone.
- **The boundary is the image of the zero divisors.** The rank-one elements are the boundary
  $\alpha=\lvert\mathbf{w}\rvert$, and by the rank criterion they are precisely the images of the cone. A
  massless element therefore maps to a rank-one positive element, which is a pure state, and the massless
  slice of the cone is the pure-state boundary of the state cone.
- **The probability of a massless element is not zero.** The weight $H$ of the preceding section is
  positive definite, with $H(\tilde Q,\tilde Q)=\sum_\mu\lvert Q_\mu\rvert^{2}>0$ on every nonzero
  element and in particular on the whole cone. The pairing has no null vector anywhere, so the cone is not
  a locus of vanishing probability, and a massless element carries a well-defined boundary state rather
  than a null state.

The contrast with the composition band is now exact. The same element that the plain product cannot
divide by, and that in the composition band is a signal travelling at $c$, is in the probability band a
pure state on the boundary of the state cone.

The sharper operator reading belongs to the sandwich rather than to the square, and it separates the two
regimes by a rank of four against one. The sandwich
$\Theta_{\tilde Q}(\tilde R)=\tilde Q\tilde R\tilde Q^{*}$ of *The Operators of the Plain Sesquilinear
Product and the Born Pairing* is the operator form of the sesquilinear product; acting on the whole algebra
it has complex rank four off the cone, where it is a bijection of the matrix algebra, and complex rank one
on it, where its image is a single Hermitian line. In the matrix model the sandwich is the congruence
$X\mapsto M X M^{\dagger}$ with $M=\mathsf M_2(\tilde Q)$, and *The 2×2 Matrix Operator Representation
$\mathsf M_2(\mathbb C)$ of Biquaternions* computes the collapse: on the cone the matrix is a product
$M=uv^{\dagger}$ of rank one and every operand is sent to a multiple of $uu^{\dagger}$, the line of a
minimal idempotent. The surviving scalar decides which face of the cone the operand sits on: for the pure
part $Q_0=0$ and the operator is nilpotent, while for an idempotent multiple $Q_0\neq0$ and it is a scaled
projection. Read as a process the collapse is irreversible, a completely positive map with a single Kraus
operator and hence the algebraic shape of a destructive measurement, and it is the geometric form of the
decoherence of *Decoherence as Idempotent Projection*. The division of the cone into the nilpotent part and
the idempotent multiples is thus the same division the composition band reads through the nilpotent index,
seen here as the two possible survivors of the collapse.

## The Massless Particles

### The photon: one element read in two sectors

The photon is the massless case the corpus has built, and it exhibits both jobs of the cone at once. Its
four-momentum is

$$
\tilde P=i\frac{E}{c}e_0+\mathbf{p},
\qquad
N(\tilde P)=-\frac{E^{2}}{c^{2}}+\mathbf{p}^{2},
$$

so the massless condition $N(\tilde P)=0$ is $\lvert\mathbf{p}\rvert=E/c$, and the photon's four-momentum
is a zero divisor. The lightlike momentum has a second face. With
$\hat{\mathbf{n}}=\mathbf{p}/\lvert\mathbf{p}\rvert$ and
$\tilde\Pi(\hat{\boldsymbol\mu})=\tfrac12(e_0+i\hat{\boldsymbol\mu})$,

$$
\tilde P=2i\frac{E}{c}\,\tilde\Pi(-\hat{\mathbf{n}}),
\qquad
\tilde\Pi^{2}=\tilde\Pi,
\qquad
\tilde\Pi^{*}=\tilde\Pi,
\qquad
N(\tilde\Pi)=0,
$$

an imaginary multiple of a rank-one Hermitian idempotent. So the massless momentum is not merely
non-invertible; it is a scaled projector, and the projector is a pure state of the informational sector.

The probability band completes the picture. The sesquilinear square of the same momentum is

$$
\tilde P\star\tilde P=4\frac{E^{2}}{c^{2}}\,\tilde\Pi(-\hat{\mathbf{n}}),
$$

a positive multiple of the **same** projector. The **interpretation** is that one element carries two faces:
in the composition the momentum is an imaginary multiple of the projector, which is why it is
non-invertible and why the propagation is at $c$; in the probability it is a positive multiple of the
same projector, which is why its state is a pure boundary state and not a null state. *The Photon as a
Null Element: What the Cone Derives and What It Does Not* owns both readings, and *The Photon in
Biquaternionic Form* owns the polarisation account; the flagpole form of the identity, in which the null
direction and the projector are two faces of one object, is in *The Boost of an Electromagnetic Plane
Wave as a Rotation and a Dilation*.

### Every massless particle sits on the same cone

The cone is one set, and it is degenerate as a shell in one specific way: it is the only level set of the
norm that is a cone, because $N(\tilde Q)=0$ is invariant under dilation while $N(\tilde Q)=m^{2}$ is not
for $m\neq0$. The massless shell is therefore shared, and every massless particle of the framework sits on
it:

- the photon, of helicity $\pm1$, whose four-momentum is the case just computed;
- the graviton, of helicity $\pm2$, the massless spin-two field of *Canonical Quantization of the
  Biquaternion Graviton Field*;
- the Rarita–Schwinger field, of helicity $\pm\tfrac32$, the massless spin-$\tfrac32$ case of *Canonical
  Quantization of the Biquaternion Rarita–Schwinger Field*;
- the chiral fermion, the massless spin-$\tfrac12$ case of *Chiral Fermions in the Biquaternion
  Framework*, where the masslessness of a lone Weyl field in the unbroken phase is the algebraic statement
  that the mass bilinear vanishes identically on a state of definite chirality.

All four have $N=0$; the cone sees no difference between them.

### What the cone does not tell the massless particles apart

Two data of a massless particle are fixed by the cone and two are not.

The cone fixes the shell and the rank. The shell is $N=0$ for every massless particle, and the rank of the
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

The division between the derived and the imported is the same in this article as in the cone literature,
and it is worth stating once in the comparative form.

What the cone derives, with no further input: the massless shell is the zero-divisor cone and it is the
only level set that is a cone; the propagation speed is $c$ and is the same in every frame; a null
four-momentum has no rest frame; a particle on the null shell moves at $c$ for every momentum; and the
null four-momentum is a scalar multiple of an idempotent of the informational sector. To that list the
comparison adds the probability statement: the sesquilinear square of a massless element is a positive
rank-one element, so the massless slice is the pure-state boundary of the state cone.

What the cone does not derive: the value $m=0$ itself, since the algebra treats every value of $m$ on the
same footing; the existence of a mass scale at all, since the cone is dilation invariant; the physical
selection of the massless branch over the massive one; and the reduction from the four polarisation
directions of the material sector to the two transverse ones. The last of these is the one to state
carefully, because the rank-one boundary invites the opposite conclusion. The rank is a count of the
rank-one summands of the sesquilinear square, and the count of polarisations is a reading offered on that
count, as *Mass, Rank and the Positivity of the Dagger* says of itself. The reduction to two transverse
polarisations is a subsidiary gauge condition, imported and not performed by any power of the cone.

The comparison sharpens the reason. The cone is the null set of the interval, and the interval is a form
of the algebra, so everything the cone says is a statement about the norm and its vanishing. The polarisation
count and the helicity content are statements about a little group, and no little group lives inside the
norm. That is why the cone can be exact about the massless shell and silent about the massless spectrum.

## Physical Interpretation

The ledger of the article, in the comparative form of the pair of bands.

| Statement | Status | Owner |
| --- | --- | --- |
| The cone is one set, shared by the two bands | Theorem | *The Light Cone as the Biquaternion Zero-Divisor Cone* |
| The cone is the boundary of invertibility of the composition | Theorem | *Composition and Probability: the General Plain Algebra and the General Plain Sesqualgebra of Biquaternions Compared* |
| The cone is the rank-drop locus of the probability | Theorem | *Mass, Rank and the Positivity of the Dagger* |
| The nilpotent index is two in the composition and three in the probability | Theorem | this article, recomputed |
| The cone is the null set of the interval and of no other of the four forms | Theorem | this article, recomputed |
| The cone is a degeneration locus of all twelve rows, and the exact invertibility boundary of the four general products | Theorem | this article, recomputed; *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket* |
| The cone is absorbing for exactly the four general products | Theorem | this article, recomputed |
| The sector sign meets the cone on the pure part, the gauge metric on the two sectors | Theorem | this article, recomputed; *The Symplectic Form and the Biquaternion Norm Cone* |
| The four forms are the forms of the four families of the grid, one to a family | Theorem | *The Twelve Structures Compared: Product, Law and Form* |
| The massless limit is a degeneration of the symbol, of complex rank four to two | Theorem | *Conformal Invariance and the Massless Limit in Biquaternionic Form* |
| The sandwich collapses from complex rank four to rank one on the cone | Theorem | *The 2×2 Matrix Operator Representation $\mathsf M_2(\mathbb C)$ of Biquaternions* |
| The cone is the absorbing set of the composition | Theorem | *The Interval as the Square and the Charge of the Material Composition* |
| A left multiplication by a null parameter collapses the form, its image inside the cone | Theorem | *The Operators of the Quaternionic Product: the Opposite Monoid and the Norm* |
| The norm is a character of the unit group, so $N$ labels masses as characters, not eigenvalues | Interpretation | *Why a Central Product Cannot Compose: the Radical and the Isotropic Elements* |
| The interval measures every direction and normalises none on the cone | Interpretation | *The Quaternion Form as a Product: the Scalar Coupling of Two Material Operations* |
| The gauge metric equals the interval up to sign on the two sectors, $K=\pm N$ | Theorem | *The Four General Products and Their Physical Readings* |
| The pure states are the intersection of the gauge-metric null set, the cone and the trace-one slice | Theorem | *The States the Indefinite Metric Cannot Normalise* |
| The image of the sesquilinear square is the state cone, its boundary the pure states | Theorem | *The Spinor Space as a Hilbert Space of the General Plain Sesqualgebra* |
| A massless element carries a boundary state, not a null state | Interpretation | this article |
| The massless momentum and a pure state are one element read in two sectors | Interpretation | *The Photon as a Null Element: What the Cone Derives and What It Does Not* |
| The cone is the common floor of the massless spectrum, not its separator | Interpretation | this article |
| $m=0$, the mass scale, and the transverse reduction | Imported | *The Photon as a Null Element: What the Cone Derives and What It Does Not* |

## Summary

The zero-divisor cone is the one set that the general plain algebra and the general plain sesqualgebra of
biquaternions share unchanged, and it is the physical locus of the massless particles. In the composition
band it is the boundary of invertibility, and the physics of the boundary is propagation at $c$: the
massless shell is the only level set of the norm that is a cone, the speed is frame independent by
multiplicativity of the norm, a null momentum has no rest frame, and its direction is preserved by the
rotor group. In the probability band it is the boundary of the state cone: the sesquilinear square is
positive for every nonzero element and never vanishes, so the cone is not a locus of vanishing
probability, and the square drops from rank two to rank one exactly on the cone, which makes the massless
slice the pure-state boundary of the state cone. The nilpotent index of the cone rises from two in the
first band to three in the second, and the shift is a shift of the pure isotropic part alone, the
idempotent multiples being nilpotent in neither band. The cone itself is the null set of the interval
$N(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)$ and of no other of the four forms, so the
cone belongs to the interval and the two products give it its two jobs. Read across the grid, the cone is a
degeneration locus of all twelve rows and the exact boundary of invertibility and the absorbing set of
exactly the four general products, and the other two indefinite forms meet it on one remarkable subspace
each, the sector sign on the pure part and the gauge metric on the two sectors. The corpus reads the interval
sharply in two ways that this article recorded only late: it is the comparison that measures every
direction and normalises none, and its gauge cousin $K$ coincides with it up to sign on the two sectors, so
the pure states are the intersection of the gauge-metric null set, the cone and the trace-one slice. In the
composition the cone is also the absorbing set of the product, since one lightlike factor forces a
lightlike composite, and the left multiplication by a null parameter collapses the form and maps every
element into the cone; the same multiplicativity makes the norm a character of the unit group, so a mass
label on that row is a character and not an eigenvalue. The massless particles are the
case list: the photon is one element read in two sectors, an imaginary multiple of a projector in the
composition and a positive multiple of the same projector in the probability, and the graviton, the
Rarita–Schwinger field and the chiral fermion sit on the same cone, distinguished from one another by a
helicity that the cone does not carry. What the cone derives is the shell, the speed, the absence of a
rest frame and the rank-one boundary; what it does not derive is the value $m=0$, a mass scale, the
selection of the massless branch, and the reduction to two transverse polarisations. Finally, the word
"cone" is used for three sets in the corpus — the zero-divisor cone of this article, the state cone of the
informational sector and the one-dimensional ray that normalises a probability — and keeping them apart is
what makes the comparison readable.

## Summary of Notation

- $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, basis $e_0=1,e_1,e_2,e_3$, $e_k^{2}=-e_0$, $e_1e_2=e_3$.
- ${}^{\natural}$ natural conjugation; $\bar{\cdot}$ coefficient conjugation; ${}^{*}=\bar{\cdot}\circ{}^{\natural}$ Hermitian conjugation; $\tilde Q^{\flat}=-\tilde Q^{*}$.
- $\mathrm{Sc}$ scalar part, $\mathrm{Tr}=2\,\mathrm{Sc}$; $N(\tilde Q)=\tilde Q\tilde Q^{\natural}=\sum_\mu Q_\mu^{2}$ the biquaternion norm, $N(\tilde Q)=\det\mathsf{M}_2(\tilde Q)$.
- $\tilde P\tilde Q$ the plain product (composition, GPA); $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ the plain sesquilinear product (probability, GPS).
- $N(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)$ the interval; $B=\mathrm{Sc}(\tilde P\tilde Q)$ the sector sign; $H=\mathrm{Sc}(\tilde P\tilde Q^{*})$ the probability weight; $K=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})$ the fourth form.
- The cone is $\{\tilde Q\neq0:N(\tilde Q)=0\}$, the zero-divisor set; pure means $\mathrm{Sc}\,\tilde X=0$, isotropic means $\sum_k X_k^{2}=0$.
- "The cone" without qualification is the zero-divisor cone; the state cone is the future cone of $\mathbb{M}_+$, and the cone of an operation is the ray $\mathbb{R}_{\ge0}e_0$. The gauge metric has its own null set $\{K=0\}$.
- The twelve rows: GPA, GQA, GPS, GQS the four general products; SPA, SQA, SPS, SQS the symmetric parts; APA, AQA, APS, AQS the antisymmetric parts; $L_{\tilde P}$ the left multiplication of the row, of rank read on the eight real parameters; $\Theta_{\tilde Q}$ the sandwich $\Theta_{\tilde Q}(\tilde R)=\tilde Q\tilde R\tilde Q^{*}$; $\mathbb{C}_{\mathbb{B}}e_0$ the centre.
- $\mathbb{M}_\pm$ the anti-Hermitian and Hermitian sectors; $\mathbb{H}_{\mathbb{B}}$ the real-quaternion subspace; $\mathbb{C}_{\mathbb{B}}$ the centre.
- $\tilde\Pi$ a plain idempotent, $\tilde\Pi^{2}=\tilde\Pi$; $\tilde\Pi(\hat{\boldsymbol\mu})=\tfrac12(e_0+i\hat{\boldsymbol\mu})$; $\Box=\tilde\nabla\tilde\nabla^{\natural}$.
- $\mathsf{M}_2$ the $2\times2$ matrix model, $\mathsf{M}_2(e_0)=I_2$, $\mathsf{M}_2(e_k)=-i\sigma_k$; $\mathrm{ISO}(2)$ the massless little group.

## Further Reading

- The physics companion, same section of the menu: *Composition and Probability: the General Plain Algebra and the General Plain Sesqualgebra of Biquaternions Compared*.
- The mathematics companion: *The General Plain Algebra and the General Plain Sesqualgebra of Biquaternions Compared*.
- The cone in the algebra: *The Light Cone as the Biquaternion Zero-Divisor Cone*; *Zero Divisors as a Physical Locus in Biquaternionic Form*; *Square Roots: the Local Complex Structure, the Light Cone and the Mass Shell*.
- The cone in the material sector: *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*; *Causality and the Light Cone as an Information Barrier in Biquaternionic Form*; *The Boost of an Electromagnetic Plane Wave as a Rotation and a Dilation*.
- The cone in the informational sector: *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*; *The Bloch Ball as the Trace-One Slice of the Future Light Cone*; *The Spinor Space as a Hilbert Space of the General Plain Sesqualgebra*; *Mass, Rank and the Positivity of the Dagger*.
- The massless particles: *The Photon as a Null Element: What the Cone Derives and What It Does Not*; *The Photon in Biquaternionic Form*; *Canonical Quantization of the Biquaternion Graviton Field*; *Canonical Quantization of the Biquaternion Rarita–Schwinger Field*; *Chiral Fermions in the Biquaternion Framework*; *Conformal Invariance and the Massless Limit in Biquaternionic Form*; *The Celestial Sphere of the Null Cone: Null Directions, Chirality and the Phase*.
- The map of the four products and their forms: *The Four General Products and Their Physical Readings* (which owns the sector collapse $K=\pm N$).
- The other bands of the grid, for the cone's other faces: *The Interval as the Square and the Charge of the Material Composition* and *The Operators of the Quaternionic Product: the Opposite Monoid and the Norm* (causality, the absorbing set and the collapsing multiplication); *Why a Central Product Cannot Compose: the Radical and the Isotropic Elements* and *The Quaternion Form as a Product: the Scalar Coupling of Two Material Operations* (coupling, the character and the comparison that normalises none); *The States the Indefinite Metric Cannot Normalise* and *The Fourth Product and Its Indefinite Metric* (gauge, the null set and the intersection with the cone); *Why Probability Values Are Central: the Symmetric Sesquilinear Product and Its Cone* (positivity, the ray that is not the state cone).
- The grid of the twelve structures: *The 12 Products of the Biquaternion Complex Space*; *The Twelve Structures Compared: Product, Law and Form*; *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket*.
- The cone in the other realisations of the grid: *The Symplectic Form and the Biquaternion Norm Cone* (the cone as the isotropic locus of the sector sign on the phase space, and as the characteristic cone of the d'Alembertian); *The 2×2 Matrix Operator Representation $\mathsf M_2(\mathbb C)$ of Biquaternions* (the collapse of the congruence, from rank four to rank one); *Conformal Invariance and the Massless Limit in Biquaternionic Form* (the massless limit as a degeneration of the symbol); *Decoherence as Idempotent Projection* (the rank-one collapse read as information loss); *Biquaternion Rotations and Lorentz Transformations* (the rank-one stratum under the rotor group).
- The conventions of the series: *Conventions in the Biquaternion Universe*.
