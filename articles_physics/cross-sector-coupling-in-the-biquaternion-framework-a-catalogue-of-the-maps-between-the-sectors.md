# __Cross-Sector Coupling in the Biquaternion Framework: a Catalogue of the Maps Between the Sectors__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ splits into the two
four-real-dimensional eigenspaces of Hermitian conjugation,

$$
\mathbb{B} = \mathbb{M}_- \oplus \mathbb{M}_+, \qquad
\mathbb{M}_\pm = \{\tilde{Q} : \tilde{Q}^{*} = \pm\tilde{Q}\},
$$

the **material** sector $\mathbb{M}_-$ and the **informational** sector $\mathbb{M}_+$. The foundational
articles give each sector its physics; this article asks a question that neither of them owns: which
algebraic operations actually carry an element from one sector to the other, and which do not. The
question is the one the introduction records as its second open question, a coupling between the sectors
beyond the Lorentz conjugation. The answer is a short catalogue and a boundary, and the catalogue is the
whole content of the article.

Two clarifications fix the scope. First, a **coupling** here is an algebraic operation that is not
sector-preserving: a map $\mathbb{M}_-\to\mathbb{M}_+$, a map $\mathbb{M}_+\to\mathbb{M}_-$, or a
pairing that reads an element of each sector and returns a scalar. The list is of operations the algebra
already supplies; no operation is introduced. Second, the article **derives nothing**. Every entry is
owned by an article that proves it, and the entry records the owner and the boundary. This is an index
article in the genre of *Relations Between Subspaces* and *What the Biquaternion Algebra Cannot Do: A
Catalogue of Algebraic Obstructions*.

The division that makes the question sharp is this: the conjugations of the algebra never cross the
split, while three operations of a different kind always do. The conjugations are sector-preserving
because the two sectors are *defined* as their fixed spaces, so a map that crossed the split would have
to be something other than a conjugation; the square, multiplication by $i$ and the state-preparation
map are exactly such operations. The split also carries a superselection reading, whose content is that
no *observable* operation crosses it — a statement about observables and not about maps, and one that
must be held apart from the positive entries of the catalogue.

## What Counts as a Coupling

The split is the eigenspace decomposition of the involution ${}^{*}$, and the first fact about the
crossing question is negative and general.

**Proposition (conjugations preserve the sectors).** Each of the four conjugations of the algebra
— the identity, complex conjugation $\bar{\cdot}$, quaternion conjugation ${}^{\natural}$, and
Hermitian conjugation ${}^{*}$ — maps each sector into itself. The same holds for the anti-Hermitian sign
$\flat = -{}^{*}$.

**Why.** The sector of an element is decided by the sign of its adjoint, and each conjugation $c$ commutes
with ${}^{*}$, so for $c(\tilde{Q})$ with $\tilde{Q}\in\mathbb{M}_-$ one has
$c(\tilde{Q})^{*} = c(\tilde{Q}^{*}) = c(-\tilde{Q}) = -c(\tilde{Q})$, and $c(\tilde{Q})$ is again material;
the argument for $\mathbb{M}_+$ is the same with the opposite sign. The commutativity is the Klein-four
relation of the conjugations: ${}^{*} = {}^{\natural}\circ\bar{\cdot}$, and the group $\{1,\bar{\cdot},{}^{\natural},{}^{*}\}$
is abelian, so every $c$ commutes with ${}^{*}$ and $\flat = -{}^{*}$ inherits it, $\tilde{Q}^{\flat} = \tilde{Q}$
being the defining relation of $\mathbb{M}_-$. The property is verified below.

The proposition is why the superselection article can say that no operation *of the conjugation type*
maps one summand into the other. It is not a statement about all operations, and the entries below are
the operations it does not cover.

## The Maps from Material to Informational

### The Square

The square of a material element is its interval, and the interval is a real scalar.

**Identity (the square is the interval).** For every $\tilde{Q}$,

$$
\tilde{Q}^{\natural}\tilde{Q} = N(\tilde{Q})\,e_0,
$$

with $N(\tilde{Q}) = \sum_\mu Q_\mu^{2}$. For $\tilde{Q}\in\mathbb{M}_-$, written $\tilde{Q} = ict\,e_0+\mathbf{x}$
with real $t$ and $\mathbf{x}$, the value $N(\tilde{Q}) = -c^{2}t^{2}+\mathbf{x}^{2}$ is **real**, and the
scalar line $\mathbb{R}e_0$ lies in $\mathbb{M}_+$.

**Reading.** Squaring is therefore a map $\mathbb{M}_-\to\mathbb{M}_+$, with image the real scalar line,
and it is the minimal instance of a cross-sector coupling supplied by the product itself. It is
deliberately weak: it is a map and not an evolution, and the product of *two* material elements is not
informational — it carries a rotation part in $\mathbb{M}_-$ and a boost part in $\mathbb{M}_+$, so it
lies in neither sector. The square is the coupling; the product is not. The identity is owned by *The
Interval as the Square and the Charge of the Material Composition*, and the grid-level pointer by *The Four General Products and Their Physical Readings*.
Recomputed on $100$ random material elements: central, real, and equal to $N(\tilde{Q})e_0$ on $100$ of
$100$; on $100$ random pairs of material elements the product lies in neither sector on $100$ of $100$.

### The Preparation Map

The second map is a rotation of the four-vector into an element of the informational sector.

**Map.** On a material element $\tilde{Q} = ict\,e_0+\mathbf{x}$, the central element
$\tilde{H} = -\tfrac{i}{2}\tilde{Q}$ is

$$
\tilde{H} = -\tfrac{i}{2}\bigl(ict\,e_0+\mathbf{x}\bigr) = \tfrac12\bigl(ct\,e_0-i\mathbf{x}\bigr) \in \mathbb{M}_+,
$$

with $\mathrm{Tr}(\tilde{H}) = ct$ and $N(\tilde{H}) = -\tfrac14 N(\tilde{Q})$. On the trace-one slice
$ct = 1$ it is the Hermitian state $\tilde\rho = \tfrac12(e_0+i\mathbf{r})$ with $\mathbf{r} = -\mathbf{x}$,
a point of the Bloch ball.

**Reading.** The map is a dictionary and not a dynamics: it names a **state preparation**, the
correspondence between a future-directed four-vector and a mixed state, and it is the mirror dictionary
of *The Bloch Ball as the Trace-One Slice of the Future Light Cone*, which owns it. Its boundary is that
it carries no equation of motion, and that the trace-one slice is what makes it a state map rather than a
bare vector-space isomorphism.

## The Maps from Informational to Material

### Multiplication by the Central Imaginary

The simplest map is the one the central scalar supplies.

**Proposition.** Multiplication by $i$ exchanges the two sectors, $i\mathbb{M}_+ = \mathbb{M}_-$ and
$i\mathbb{M}_- = \mathbb{M}_+$, reverses the sign of the norm, $N(i\tilde{Q}) = -N(\tilde{Q})$, and is a
bijection of the algebra.

**Why.** The scalar $i$ is central and anti-Hermitian, $i^{*} = -i$, so $(i\tilde{Q})^{*} = \tilde{Q}^{*}i^{*} = -i\tilde{Q}^{*}$:
the sign of the adjoint flips and the sector with it. The norm reverses because $N$ is quadratic in the
coefficients and $i^{2} = -1$.

**Reading.** The exchange is a **relational clock**: because the two sectors are the two time
coordinates, the exchange reads one sector's time against the other's, which is the reading of *Each
Sector Is the Other's Clock: the Sector Exchange as Relational Time*. Its boundary is that the exchange
is invertible and of order four, so it cannot by itself supply an arrow; the arrow needs the non-units of
the acting monoid (see below). Multiplication by the central scalar is developed by *The Central
Rotation: Phase, Duality and the Wick Rotation as One Generator*. Recomputed on $100$ elements of each
sector: $i$ sends $\mathbb{M}_-$ to $\mathbb{M}_+$ and $\mathbb{M}_+$ to $\mathbb{M}_-$ with no exception
on $200$ of $200$.

### The Rotor Action

An informational element can also act on a material one.

**Proposition.** A unit-norm element $\tilde{\Lambda}\in\mathbb{M}_+$ — the carrier of the pure boosts —
acts on the material sector by the sandwich $\tilde{T}\mapsto\tilde{\Lambda}\tilde{T}\tilde{\Lambda}^{*}$,
and the result is again material.

**Why.** $(\tilde{\Lambda}\tilde{T}\tilde{\Lambda}^{*})^{*} = \tilde{\Lambda}\tilde{T}^{*}\tilde{\Lambda}^{*} = -\tilde{\Lambda}\tilde{T}\tilde{\Lambda}^{*}$,
since $\tilde{\Lambda}^{*} = \tilde{\Lambda}$ for a Hermitian rotor and $\tilde{T}^{*} = -\tilde{T}$.

**Reading.** The action is a **frame change**: the informational sector, through its Hermitian rotors,
supplies the transformations of the material sector. It is a coupling of a third kind — not a map
$\mathbb{M}_-\to\mathbb{M}_+$, but an action of one sector on the other, and it preserves the sector it
acts on. Its boundary is that only the unit-norm elements are rotors, and the general action form of the
framework is the one *Biquaternion Rotations and Lorentz Transformations* develops; the operator side is
*The Sandwich Action in Subspaces*. Recomputed on $100$ random boost rotors and $100$ material elements:
the sandwich result is anti-Hermitian on $100$ of $100$.

## The Off-Sector Pairings

A coupling can also be a scalar read from one element of each sector.

**Proposition (the off-sector scalar part).** For $\tilde{P}\in\mathbb{M}_-$ and $\tilde{H}\in\mathbb{M}_+$,
the scalar part of the plain product is purely imaginary,

$$
\mathrm{Sc}(\tilde{P}\tilde{H}) = i\bigl(ct\,h_0-\mathbf{x}\cdot\mathbf{h}\bigr) \quad \text{for }
\tilde{P} = ict\,e_0+\mathbf{x}, \quad \tilde{H} = h_0e_0+i\mathbf{h},
$$

with both factors real.

**Why.** The scalar part of the product is $P_0H_0-(\mathbf{P},\mathbf{H})$, and the two terms are
$ict\cdot h_0$ and $\mathbf{x}\cdot i\mathbf{h}$, each carrying one factor of $i$.

**Reading.** The pairing reads a material operation against an informational state and returns a phase,
which is the off-sector reading of *The Ordinary Product and the Material Sector*. It is a pairing and
not a map, and it produces no element of either sector. The **imaginary part of the norm** is the same
phenomenon from the other side: the cross terms of $N$ couple the material and informational parameters
of one element, and that is the reading the introduction records for the imaginary part of $N$, owned by
*Biquaternion Norm and Invertibility*. Recomputed on $100$ material–informational pairs: the scalar part
is purely imaginary on $100$ of $100$.

## The Couplings of Time and of Thermodynamics

Two further cross-sector readings are already owned and are recorded here because a catalogue of
couplings is incomplete without them.

- **Imaginary (Matsubara) time.** The imaginary-time axis of thermal field theory is the informational
  temporal direction, so the continuation that the KMS condition and the Matsubara formalism use is the
  material–informational exchange read as a temperature. The owners are *The KMS Condition and the
  Biquaternion Framework* and *The Matsubara Formalism in Biquaternionic Form*; the reading is a
  continuation and not a new coupling.
- **The thermodynamic exchange.** A material operation that loses information passes it to the
  informational sector: the Landauer exchange is the thermodynamic face of the same split, and the
  information loss is counted by the algebra's own logarithm. The owners are *Landauer's Principle and
  the Material–Informational Exchange in Biquaternionic Form* and *The Lyapunov Exponent and Information
  Loss in the Biquaternion Framework*; the arrow that orders the exchange is the split of the acting
  monoid into its units and its non-units (*The Monoid of Acting Maps: the Process Is the Multiplication,
  the State Is the Idempotent*).

## What Does Not Couple: the Superselection Boundary

The catalogue has a boundary, and it is the place where the question "is there a coupling?" is answered
*no*.

The material–informational split carries a **superselection reading**: no observable operation carries
one sector to the other, and the relative phase between the two sectors is unobservable. The statement
is exact, and it does not conflict with the positive entries above, for the reason the superselection
article gives. The algebra is central simple, so it has no central-projection superselection structure of
the standard kind, and what survives is a superselection structure of a **real form**, carried by the
real structure $\flat = -{}^{*}$ rather than by the centre. The positive entries of this catalogue are
maps and pairings and not observables: the square is a map, $i$ is central multiplication, the
preparation map is a dictionary, and the off-sector scalar is a pairing. None of them is an observable
that an expectation value could use to prepare or detect a coherence between the sectors.

**Boundary.** The superselection statement is about observables and coherences; this article's positive
entries are about maps. The two must not be collapsed into one another, and the owner of the
superselection statement is *The Material-Informational Split as a Superselection Structure in
Biquaternionic Form*.

## The Catalogue in One Table

| operation | type | source $\to$ target | owner | boundary |
|---|---|---|---|---|
| square $\tilde{Q}\mapsto\tilde{Q}^{\natural}\tilde{Q}$ | map | $\mathbb{M}_-\to\mathbb{M}_+$, image $\mathbb{R}e_0$ | *The Interval as the Square and the Charge of the Material Composition* | a map, not an evolution; the product of two is not informational |
| preparation $\tilde{H} = -\tfrac{i}{2}\tilde{Q}$ | map | $\mathbb{M}_-\to\mathbb{M}_+$ | *The Bloch Ball as the Trace-One Slice of the Future Light Cone* | a dictionary, no dynamics; state only on the trace-one slice |
| central multiplication $\tilde{Q}\mapsto i\tilde{Q}$ | map | $\mathbb{M}_-\leftrightarrow\mathbb{M}_+$ | *The Central Rotation: Phase, Duality and the Wick Rotation as One Generator* | invertible, order four; no arrow by itself |
| rotor action $\tilde{T}\mapsto\tilde{\Lambda}\tilde{T}\tilde{\Lambda}^{*}$ | action | $\mathbb{M}_+$ acts on $\mathbb{M}_-$ | *Biquaternion Rotations and Lorentz Transformations* | preserves the sector it acts on; unit-norm rotors only |
| off-sector scalar $\mathrm{Sc}(\tilde{P}\tilde{H})$ | pairing | $\mathbb{M}_-\times\mathbb{M}_+\to i\mathbb{R}$ | *The Ordinary Product and the Material Sector* | a pairing, produces no element |
| imaginary part of $N$ | pairing | $\mathbb{M}_-\times\mathbb{M}_+$ cross terms | *Biquaternion Norm and Invertibility* | a reading of one element's own cross terms |
| Matsubara continuation | continuation | imaginary time $=$ informational time | *The KMS Condition and the Biquaternion Framework*, *The Matsubara Formalism in Biquaternionic Form* | a continuation, not a new coupling |
| Landauer exchange | process | material $\to$ informational | *Landauer's Principle and the Material–Informational Exchange in Biquaternionic Form* | thermodynamic face; arrow from the acting monoid |
| superselection | **non-coupling** | observables preserve each sector | *The Material-Informational Split as a Superselection Structure in Biquaternionic Form* | about observables, not about maps |

## Physical Readings

The article's own reading is the **two-axis picture** of the split: the sectors are separated by the
involution ${}^{*}$, which the conjugations respect and which a small set of non-conjugation operations
cross. Read one way, the picture says that the split is rigid — nothing built from the conjugations, and
no observable, moves between the sectors. Read the other way, it says that the split is crossed in
exactly the places where the physics needs a bridge: the square takes a process to a probability
argument, $i$ takes a time to the other time, the rotor takes a frame to a frame, and the off-sector
scalar reads a state against an operation. The rigidity and the crossings are not in tension; they are the
two halves of one statement.

- **Bridge reading.** Each positive entry is a bridge of a different kind — a map, a bijection, an
  action, a pairing — and no two entries are the same bridge. Boundary: the reading names the shape of
  each bridge and supplies no dynamics; the grid-level comparison is *The Four General Products and Their Physical Readings*.
- **Boundary reading.** The superselection entry is the statement that the bridges are not observables.
  Read with the positive entries, it says that a coupling can be algebraic and unobservable at once: the
  square exists and no measurement uses it to prepare a coherence between the sectors. Boundary: the
  reading is the superselection article's, restated here only to mark the edge of the catalogue.

## Summary

The algebra's two sectors $\mathbb{M}_-$ and $\mathbb{M}_+$ are the eigenspaces of Hermitian
conjugation, and the conjugations $\bar{\cdot}$, ${}^{\natural}$, ${}^{*}$, $\flat$ preserve each sector,
because a sector is defined as a fixed space. The couplings are the operations that are not
conjugations, and they are few. The square carries a material element to its real interval, a scalar in
$\mathbb{M}_+$, and is the minimal cross-sector map the product supplies. The preparation map
$\tilde{H} = -\tfrac{i}{2}\tilde{Q}$ carries a four-vector to a state on the trace-one slice. Central
multiplication by $i$ exchanges the sectors and reverses the norm, reading one time against the other. A
unit-norm Hermitian rotor acts on the material sector by the sandwich and preserves it, so the
informational sector supplies the frame changes of the material one. The off-sector scalar part
$\mathrm{Sc}(\tilde{P}\tilde{H})$ is purely imaginary and pairs an operation with a state; the imaginary
part of the norm is the same cross-term phenomenon. The Matsubara continuation and the Landauer exchange
are the thermal readings of the same split, and the arrow that orders them is the split of the acting
monoid. Against all of this stands one exact negative statement: the split is a superselection structure
of a real form, so no observable operation and no conjugation crosses it. The catalogue's conclusion is
that the coupling the introduction asks for exists, is algebraic, is minimal, and is not observable —
each of its instances owned by an article that proves it.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $\mathbb{M}_\pm = \{\tilde{Q} : \tilde{Q}^{*} = \pm\tilde{Q}\}$ | Material ($-$) and informational ($+$) sectors |
| ${}^{*}$ | Hermitian conjugation, $e_k^{*} = -e_k$, $i^{*} = -i$ |
| ${}^{\natural}$, $\bar{\cdot}$, $\flat = -{}^{*}$ | Quaternion conjugation, coefficient conjugation, the real structure |
| $\tilde{Q} = ict\,e_0+\mathbf{x}$ | Material element, $t$ and $\mathbf{x}$ real |
| $\tilde{H} = h_0e_0+i\mathbf{h}$ | Informational element, $h_0$ and $\mathbf{h}$ real |
| $N(\tilde{Q}) = \tilde{Q}^{\natural}\tilde{Q} = \sum_\mu Q_\mu^{2}$ | Biquaternion norm; equal to the interval on $\mathbb{M}_-$ |
| $\tilde{H} = -\tfrac{i}{2}\tilde{Q}$ | The preparation map, $\mathbb{M}_-\to\mathbb{M}_+$ |
| $\tilde{T}\mapsto\tilde{\Lambda}\tilde{T}\tilde{\Lambda}^{*}$ | The rotor action, $\tilde{\Lambda}\in\mathbb{M}_+$ of unit norm |
| $\mathrm{Sc}(\tilde{P}\tilde{H})$ | Off-sector scalar pairing, purely imaginary |

## Further Reading

- *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, companion article, for the
  material sector, its four-vectors and the interval.
- *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, companion article, for the
  informational sector, the trace pairing and the state space.
- *The Interval as the Square and the Charge of the Material Composition*, companion article, for the
  square map and its real-scalar image.
- *The Material-Informational Split as a Superselection Structure in Biquaternionic Form*, companion
  article, for the negative statement and its real-form reading.
- *The Four General Products and Their Physical Readings*,
  companion article, for the grid-level comparison of the four products.
