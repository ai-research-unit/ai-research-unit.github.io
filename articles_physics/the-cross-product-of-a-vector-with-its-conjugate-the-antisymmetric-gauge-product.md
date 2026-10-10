# __The Cross Product of a Vector with Its Conjugate: the Antisymmetric Gauge Product__

## Introduction

The antisymmetric half of the fourth product is the simplest of the twelve operations to write down and
the most unusual to read. It is

$$
\tilde P\diamond\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q^{*}-\tilde Q^{*}\tilde P^{\natural}\bigr)
=\mathbf{P}\times\overline{\mathbf{Q}},
$$

the cross product of the vector part of the first argument with the **conjugate** of the vector part of
the second. It is the operation named $\mathrm{AQS}$ in *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* and developed as a multiplication in *Introduction to the Antisymmetric Quaternionic
Sesqualgebra of Biquaternions*. Its value is a **pure vector**, of scalar part zero; it is
**conjugate-alternating**; and its diagonal, unlike the diagonal of every alternating bilinear product, does
**not** vanish: at $\tilde Q=e_1+ie_2$ it is $-2ie_3$. The physics menu files the band under the word
**Polarisation**, and the reading the article earns is the one the menu names: the pure vector of the value
is an **axial vector**, and the axial vector carries a direction — a polarisation or spin direction — for
the gauge side of the frame. The reading is a reading of the *value*, and the article is explicit about
where it stops.

The article owns the antisymmetric half as a product: the rule, the coordinate form, the pure-vector image,
the conjugate-alternation, the non-vanishing diagonal, the reading of the axial vector, and the boundaries
that keep the reading honest. It defers the moment when the bracket fails to close the Jacobi identity —
the second article of the band — to *A Bracket Invisible on the Real Forms: the Complex Witness of the
Jacobi Failure*; the physics of polarisation and of spin to
*Pancharatnam's Phase and the Polarization Sphere in Biquaternionic Form*,
*The Self-Dual and Anti-Self-Dual Split: Spin 1 from the Biquaternion Material Sector* and
*The Bloch Ball as the Trace-One Slice of the Future Light Cone*; the generators of the internal action to
*Observables, Gauge Generators and the Chirality of the Internal Action*; the states to *The States the
Indefinite Metric Cannot Normalise*; and the algebra to the mathematics articles *Introduction to the
Antisymmetric Quaternionic Sesqualgebra of Biquaternions*, *The Conjugate Cross Product and the Jacobi
Failure of the Antisymmetric Quaternionic Sesqualgebra*, *Remarkable Subspaces under the Antisymmetric
Quaternionic Sesqualgebra of Biquaternions*, *The Sesquilinear Pairing of the Antisymmetric Quaternionic
Sesqualgebra* and *The 12 Products of the Biquaternion Complex Space*.

**Conventions.** As in the companion articles of this block:
$\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$, $e_0=1$,
$e_k^{2}=-e_0$, $e_1e_2=e_3$, central $i$; $\tilde Q=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$,
scalar part $\mathrm{Sc}(\tilde Q)=Q_0$ and vector part $\mathbf{Q}=\sum_kQ_ke_k$; the natural conjugation
$\tilde Q^{\natural}=Q_0e_0-\mathbf{Q}$, the coefficientwise one $\bar{\tilde Q}=\sum_\mu\bar Q_\mu e_\mu$,
and the star $\tilde Q^{*}=\overline{\tilde Q^{\natural}}$; $(\mathbf{P},\mathbf{Q})=\sum_kP_kQ_k$ and
$\times$ are the bilinear dot and cross products, and $\overline{\mathbf{Q}}=\sum_k\overline{Q_k}e_k$; the
fourth product is $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q^{*}$; the Krein form is
$K(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$
with $\varepsilon=(1,-1,-1,-1)$; the sectors are $\mathbb{M}_+$ (informational) and $\mathbb{M}_-$
(material). All conventions are those of *Conventions in the Biquaternion Universe*.

**A notation caution.** The fourth product is written $\tilde P\star\tilde Q$ in this block. The
antisymmetric half is written $\diamond$ here, the symbol of *Introduction to the Antisymmetric
Quaternionic Sesqualgebra of Biquaternions*; the menu comment renders it $\wedge$, which the mathematics
article avoids because $\wedge$ names the plain outer product $\mathbf{P}\times\mathbf{Q}$ of the
antisymmetric plain algebra. The stable identifier is the name $\mathrm{AQS}$.

## The Rule and Its Coordinate Form

### The Definition

The antisymmetric half is the half-difference of the two orders of the fourth product. The two orders
differ only in the sign of their cross term, so the half-difference keeps the cross term and cancels the
scalar part and the mixed term:

$$
\tilde P\diamond\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q^{*}-\tilde Q^{*}\tilde P^{\natural}\bigr)
=\mathbf{P}\times\overline{\mathbf{Q}}.
$$

The value is a **pure vector** and its image is therefore the vector subspace
$\mathrm{Vect}(\mathbb{B})=\{Q_0=0\}$; this is the sharpest difference from its symmetric companion
$\tilde P\bullet\tilde Q$, whose values lie in no one of the remarkable subspaces for a general pair. Verified on
$100$ random pairs.

### The Coordinate Rule

**Proposition.** In the coordinates of the two arguments,

$$
\tilde P\diamond\tilde Q=\bigl(P_2\overline{Q_3}-P_3\overline{Q_2}\bigr)e_1
+\bigl(P_3\overline{Q_1}-P_1\overline{Q_3}\bigr)e_2
+\bigl(P_1\overline{Q_2}-P_2\overline{Q_1}\bigr)e_3.
$$

*Proof.* Read the components of the bilinear cross product and substitute the conjugate coordinates of
$\overline{\mathbf{Q}}$. Verified on the coordinate rule. $\square$

## The Laws of the Operation

**Proposition (the class).** The antisymmetric half is sesquilinear over $(\mathbb{C},\bar{\cdot})$:
$\mathbb{C}$-linear in the first slot and conjugate-linear in the second,

$$
(A\tilde P)\diamond\tilde Q=A\,(\tilde P\diamond\tilde Q),
\qquad
\tilde P\diamond(A\tilde Q)=\overline{A}\,(\tilde P\diamond\tilde Q)
\qquad (A\in\mathbb{C}).
$$

*Proof.* The cross product is $\mathbb{C}$-linear in $\mathbf{P}$ and the conjugate is
$\mathbb{C}$-antilinear in $\mathbf{Q}$, as the coordinate rule shows directly. Verified on the coordinate
rule. $\square$

**Proposition (conjugate-alternation).** The operation is **conjugate-alternating**,

$$
\tilde P\diamond\tilde Q=-\overline{\tilde Q\diamond\tilde P}.
$$

*Proof.* Exchanging the arguments gives $\mathbf{Q}\times\overline{\mathbf{P}}$, and conjugating it gives
$\overline{\mathbf{Q}}\times\mathbf{P}=-\mathbf{P}\times\overline{\mathbf{Q}}$. Verified on $100$ random
pairs. $\square$

The symmetry is the antisymmetry of a sesqualgebra part read through the conjugate of the value, and it is
**not** alternation in the bilinear sense. In the bilinear theory an alternating product vanishes on the
diagonal, because $f(x,x)=-f(x,x)$; here the two sides of the exchange are not the same element but
conjugate-reflection partners, and the vanishing fails. That failure is the next section and it is the
technically distinctive fact of the antisymmetric half.

**Corollary (no unit).** There is no left unit and no right unit, and no element acts as an identity for
the operation. The value is pure vector and the operation takes its arguments through conjugations, so no
element is neutral for both slots. (The absence of a unit is shared with the symmetric half and with the
fourth product, and is stated here only to close the list of laws.)

## The Diagonal That Does Not Vanish

**Theorem (the diagonal).** For every biquaternion,

$$
\tilde Q\diamond\tilde Q=\mathbf{Q}\times\overline{\mathbf{Q}}.
$$

It vanishes exactly when the vector part is a **complex multiple of a real vector**, and in particular on
the whole real quaternion subspace; it does **not** vanish in general. At $\tilde Q=e_1+ie_2$,

$$
(e_1+ie_2)\diamond(e_1+ie_2)=-2ie_3.
$$

*Proof.* Put $\tilde P=\tilde Q$ in the rule. The vector part $\mathbf{Q}=(1,i,0)$ and its conjugate
$\overline{\mathbf{Q}}=(1,-i,0)$ have cross product $(0,0,-2i)$. The vanishing condition is the
parallelism of $\mathbf{Q}$ and $\overline{\mathbf{Q}}$, which holds exactly when $\mathbf{Q}=z\,\mathbf{u}$
with $z\in\mathbb{C}$ and $\mathbf{u}$ real. Verified on the witness and on $100$ random pairs. $\square$

**Remark (why this diagonal is different).** In the bilinear theory the diagonal of an antisymmetric part
is zero and the diagonal of the symmetric part carries the square; the two are separated cleanly. For a
sesqualgebra part they are not. The diagonal of the symmetric half is the fixed part of the square,
$\tfrac12(\tilde Q\star\tilde Q+\overline{\tilde Q\star\tilde Q})$, and the diagonal of the antisymmetric
half is its anti-fixed part, $\tfrac12(\tilde Q\star\tilde Q-\overline{\tilde Q\star\tilde Q})$; the
antisymmetric diagonal is the vector part of the square read through the conjugate, and it vanishes only
when the square is fixed by that conjugation. The failure is therefore not an accident of one element: it
is what the adaptation of the exchange costs, and it is stated in the general theory of *The Symmetric and
Antisymmetric Parts of a Sesqualgebra Product*.

**The diagonal read as the self-helicity of one element.** The corpus reads the **off-diagonal** axial
vector as a polarisation direction carried by a pair of elements; the diagonal extends that reading to a
**single** element, and the extension is exact. On a complex vector $\mathbf{Q}=\mathbf{a}+i\mathbf{b}$ with
$\mathbf{a},\mathbf{b}$ real,

$$
\mathbf{Q}\times\overline{\mathbf{Q}}=(\mathbf{a}+i\mathbf{b})\times(\mathbf{a}-i\mathbf{b})=-2i\,\mathbf{a}\times\mathbf{b},
$$

so the diagonal of the antisymmetric gauge product is the imaginary multiple of twice the cross product of
the two real vectors an element carries — $-2ie_3$ at $\mathbf Q=e_1+ie_2$. A single complex vector has an
intrinsic axial direction, perpendicular to the plane of its real and imaginary parts, and the diagonal is
that direction: an element carries a **built-in helicity** before any second element enters, and the
vanishing condition — the vector part a complex multiple of a real vector — is exactly the condition that
its two real parts be collinear, so that there is no plane and no direction. The reading keeps the article's
boundary: the diagonal is a **direction attached to one element**, not a state and not a beam, and the
physical helicity of a field remains *Pancharatnam's Phase and the Polarization Sphere in Biquaternionic
Form* and *The Self-Dual and Anti-Self-Dual Split: Spin 1 from the Biquaternion Material Sector*. What this
article adds is the name **self-helicity** for the diagonal, on top of the corpus's reading of the
off-diagonal axial vector.

## The Polarisation Reading

### The Value Is an Axial Vector

The cross product of two vectors is not a third vector of the same kind: under a reflection it transforms
with the opposite sign, and the object it defines is an **axial vector** or pseudovector. In the algebra
the value $\mathbf{P}\times\overline{\mathbf{Q}}$ is a vector of $\mathrm{Vect}(\mathbb{B})$, so it lives
in the same six-dimensional real space as a vector field strength, and it is an axial object by the
algebra's own rule. That is the object the band reads.

### What the Reading Says

The reading the band offers is this: **the axial vector of the antisymmetric gauge product carries a
direction for the gauge side of the frame**, and the direction is read as a **polarisation or spin
direction**. Two elements of the algebra are paired by the operation's arguments, the pairing produces the
cross product of the first vector part with the conjugate of the second, and the result is a direction
perpendicular to both. The direction is the invariant content: it is what remains of the pair when the
scalar part and the mixed term have cancelled. The reading is a reading of the value, offered as such.

### The Bracket as a Field-Strength Pairing

The value is a cross product, and in three complex dimensions a cross product is the Hodge dual of an
exterior product. Writing $\star$ for the Hodge dual on the three-dimensional complex space,

$$
\mathbf{P}\times\overline{\mathbf{Q}}=\star\bigl(\mathbf{P}\wedge\overline{\mathbf{Q}}\bigr),
$$

so the antisymmetric gauge product is the **field-strength pairing** of the two vector parts: it is an
antisymmetric two-form read through the Hodge dual, exactly the shape of a field strength $F_{\mu\nu}$ read
as a vector, and its arguments are the two vector parts of the elements. Read this way the two halves of
the block have two different geometric characters: the symmetric half is the **metric** reading, a
symmetric pairing, and the antisymmetric half is the **curvature** reading, a two-form — the
metric-and-field-strength pair that a gauge theory of the frame is built from. The diagonal survives in
this reading as the **self-dual part** of the two-form of one element: the element paired with its own
conjugate returns the part of its field strength that is its own Hodge dual, and the off-diagonal is the
mixed (non-self-dual) part. The boundary is the corpus's: the physical self-dual split of the field
strength, its two chiralities and the two helicities of the massless field are *The Self-Dual and
Anti-Self-Dual Split: Spin 1 from the Biquaternion Material Sector* and *Higher Multipoles and the
Field-Strength Decomposition in Biquaternionic Form*. What this article states is the product-level form of
the same identification.

### The Bracket as an Anti-Linear Pairing

The law of the operation is **conjugate-alternation**, $\tilde P\diamond\tilde Q=-\overline{\tilde Q\diamond\tilde P}$, and the law can be given a name with more content than the words "not alternating". A bilinear antisymmetric product pairs two elements as they stand; a **conjugate**-antisymmetric product pairs an element with the conjugate of the other, and the shape is the shape of a pairing that a **conjugation** mediates — the form of a particle–antiparticle, or charge, pairing, in which the second argument is inserted through the same involution that would send a field to its conjugate. The non-vanishing diagonal is then the **self-charge** of a single element: the value of the pairing of an element with its own conjugate, which for an alternating product would be forced to vanish and here is not. The reading is bounded, and the boundary is sharp: the algebra supplies the antilinearity of the operation and the non-vanishing of the diagonal, and it does **not** supply a particle identification, a conserved charge or a $\mathcal{C}$-operation; the corpus's charge conjugation and its real structures on the algebra and on the module are *Charge Conjugation and the Division Ring: Charged, Neutral and Truly Neutral Particles in Biquaternionic Form* and *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*. The name **anti-linear pairing** is this article's, and it is offered as a reading of the law above.

### The Boundaries

The reading is bounded on three sides, and the boundaries are the reason it is stated carefully.

1. **The corpus's polarisation is owned elsewhere.** The physical polarisation is the coherence biquaternion
   of a light beam and the points of the Poincaré sphere, in *Pancharatnam's Phase and the Polarization
   Sphere in Biquaternionic Form*; the spin-one representation carried by the material sector is *The
   Self-Dual and Anti-Self-Dual Split: Spin 1 from the Biquaternion Material Sector*; and the state sphere
   is *The Bloch Ball as the Trace-One Slice of the Future Light Cone*. Those articles own the physical
   objects. This article reads a *value of an operation* as a direction; it does not claim to describe a
   beam, a spin state or a point of a sphere, and the value is not a state.

2. **The operation is not a state.** The states of the framework are the positive trace-one elements for
   the form $H$, and they are null for the gauge metric (*The States the Indefinite Metric Cannot
   Normalise*). The antisymmetric half returns a vector, not a positive element and not a trace-one one,
   and the diagonal of the operation at $e_1+ie_2$ is $-2ie_3$, a nonzero vector and not a state. The
   polarisation direction is a direction attached to a pairing; it is not a state vector of the state
   space.

3. **An axial vector is not a generator.** The gauge generators of the framework are the left
   multiplications by the anti-Hermitian elements of $\mathbb{M}_-$, the compact sector whose
   exponentiation gives the internal unitary group (*Observables, Gauge Generators and the Chirality of the
   Internal Action*). The value $\mathbf{P}\times\overline{\mathbf{Q}}$ is a vector of
   $\mathrm{Vect}(\mathbb{B})$; it is not in general an element of $\mathbb{M}_-$ and it is not a left
   multiplication. The passage from an axial vector to a generator is a passage between two different
   constructions, and this article does not make it. The positive form of the same statement is that the
   axial vector is the *carrier* of a direction, and the generator is the *operator* that rotates it.

### Named Readings of the Polarisation

Two further readings of the same value are recorded here, each under a name of its own and each labelled a reading rather than a theorem.

- **Oriented-area reading.** The value $\mathbf{P}\times\overline{\mathbf{Q}}$ is read as an **oriented area**: a cross product is the area of the parallelogram spanned by the two vectors together with its orientation, so the polarisation direction of the band is a plane orientation of the gauge frame rather than a vector along a line. The reading gives the direction a geometric carrier — a plane and a sign — and it is the frame-level counterpart of the polarisation sphere of *Pancharatnam's Phase and the Polarization Sphere in Biquaternionic Form*, which owns the physical polarisation. The boundary is the article's: the value is an element of the algebra and not a point of a sphere.
- **Internal handedness.** That the value is an **axial** (pseudo) vector is read as a **handedness of the internal frame**: the operation carries the orientation of the frame and not only a direction in it. The pseudo character belongs to the cross product as such — it is already present in the real antisymmetric part $\mathbf{P}\times\mathbf{Q}$ of §*The Value Is an Axial Vector* — and what the conjugation of the second slot adds is that the pairing joins a vector to the *conjugate* of another, so that the value is a direction of the frame paired with the conjugate direction of its partner. The name attaches the orientation to the frame; its boundary is that no reflection group, no spin and no parity are claimed here.

## The Limits

- **A conjugate cross product is an axial vector and not a spin.** The reading of the value as a
  polarisation direction is a reading of the value; it is not a claim that the operation produces a spin
  state or a spin quantum number, and the spin of the framework is owned by the articles named above.
- **The non-vanishing diagonal is an algebraic fact and not a pathology.** It is the anti-fixed part of the
  square, and it is what makes the antisymmetric half a genuine part of the fourth product rather than a
  foreign bracket.
- **The reading is labelled.** That the axial vector should be read as *polarisation* is the framework's
  grouping of the four jobs of the four general products; it is offered as a reading and not as a theorem, and no
  numerical identification with a measured polarisation is claimed.
- **No scale is attached.** No coupling, charge or $\hbar$ enters the operation; the places of entry are
  those the corpus has already fixed, and none is invented here.

## The Ledger

**Proved, and recomputed.** The antisymmetric half is
$\tilde P\diamond\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q^{*}-\tilde Q^{*}\tilde P^{\natural})=\mathbf{P}\times\overline{\mathbf{Q}}$,
pure vector, with the coordinate rule displayed; it is sesquilinear over $(\mathbb{C},\bar{\cdot})$,
$\mathbb{C}$-linear in the first slot and conjugate-linear in the second; it is conjugate-alternating,
$\tilde P\diamond\tilde Q=-\overline{\tilde Q\diamond\tilde P}$; and it has no unit on either side. Its
diagonal is $\mathbf{Q}\times\overline{\mathbf{Q}}$, vanishing exactly when $\mathbf{Q}$ is a complex
multiple of a real vector, and equal to $-2ie_3$ at $\tilde Q=e_1+ie_2$. Recomputed on $100$ random pairs
and on the named witness, and reproduced from *Introduction to the Antisymmetric Quaternionic Sesqualgebra
of Biquaternions*, *The Conjugate Cross Product and the Jacobi Failure of the Antisymmetric Quaternionic
Sesqualgebra* and *The 12 Products of the Biquaternion Complex Space*.

**Reading.** That the axial vector of the value carries a polarisation or spin direction for the gauge side,
and that the value is a direction and not a state. Three further names for the same facts, each a reading:
the diagonal read as the **self-helicity** of one element, $\mathbf{Q}\times\overline{\mathbf{Q}}=-2i\,\mathbf{a}\times\mathbf{b}$
for $\mathbf{Q}=\mathbf{a}+i\mathbf{b}$; the operation read as a **field-strength pairing**, the Hodge dual
of an antisymmetric two-form, so that the symmetric half is the metric reading and the antisymmetric half
the curvature reading of the frame; and the operation read as an **anti-linear pairing**, its
conjugate-alternation the shape of a conjugation-mediated pairing and its non-vanishing diagonal the
**self-charge** of one element. Two further readings, named in §*Named Readings of the Polarisation*: the **oriented-area reading**, the cross product as a plane orientation of the gauge frame rather
than a vector along a line, and **internal handedness**, the pseudo character of the value attached to the
oriented frame.

**Not claimed.** That the operation produces a spin state, a spin quantum number or a point of the Poincaré
or Bloch sphere; that the axial vector is a gauge generator; that the operation is an algebra with a unit
or a Lie structure (the Jacobi failure is the companion article's).

## Physical Readings

The antisymmetric gauge product reads as the rotation-like part of the internal action, and its being pure vector is what keeps it out of the state space. Read against the reality conditions, the conjugation in the first slot is the framework's way of pairing an object with its conjugate, which is the structure a reality condition needs; read on the clock, the product carries no central component, so it is invisible to the exchange and belongs entirely to the vector part of the algebra.

## Summary

The antisymmetric quaternionic sesquilinear product is the half-difference of the two orders of the fourth
product, and it is the cross product of the vector part of the first argument with the conjugate of the
vector part of the second,
$\tilde P\diamond\tilde Q=\mathbf{P}\times\overline{\mathbf{Q}}$. Its value is a **pure vector**, so its
image is the vector subspace; it is sesquilinear over $(\mathbb{C},\bar{\cdot})$ and
**conjugate-alternating**; and it has no unit. Its diagonal $\mathbf{Q}\times\overline{\mathbf{Q}}$ does
**not** vanish in general — it is $-2ie_3$ at $\tilde Q=e_1+ie_2$ — because the antisymmetric half of a
sesqualgebra product is the anti-fixed part of the square and the adaptation of the exchange does not force
the diagonal to zero. The reading of the band is that the **axial vector** of the value carries a
**polarisation or spin direction** for the gauge side of the frame. The reading is bounded: the physical
polarisation, the spin-one representation and the state sphere belong to *Pancharatnam's Phase and the
Polarization Sphere in Biquaternionic Form*, *The Self-Dual and Anti-Self-Dual Split: Spin 1 from the
Biquaternion Material Sector* and *The Bloch Ball as the Trace-One Slice of the Future Light Cone*; the
value is not a state and not a generator, the generators being the left multiplications by the
anti-Hermitian elements of $\mathbb{M}_-$; and the reading is offered as a reading of the value. The
failure of the operation to close under the Jacobi identity, and the complex character of its witness, are
the subject of the companion article of the band.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\diamond\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q^{*}-\tilde Q^{*}\tilde P^{\natural})$ | the antisymmetric quaternionic sesquilinear product, $\mathrm{AQS}$ |
| $\tilde P\diamond\tilde Q=\mathbf{P}\times\overline{\mathbf{Q}}$ | the value; pure vector |
| $P_2\overline{Q_3}-P_3\overline{Q_2},\dots$ | the coordinate rule |
| $\tilde P\diamond\tilde Q=-\overline{\tilde Q\diamond\tilde P}$ | conjugate-alternation |
| $\tilde Q\diamond\tilde Q=\mathbf{Q}\times\overline{\mathbf{Q}}$ | the diagonal; not zero in general |
| $(e_1+ie_2)\diamond(e_1+ie_2)=-2ie_3$ | the witness of the non-vanishing diagonal |
| $\mathrm{Vect}(\mathbb{B})$ | the vector subspace; the image of the operation |
| axial vector | the reading of the value; a direction, not a state and not a generator |
| $\mathbb{M}_-$ | the anti-Hermitian sector; the home of the gauge generators |

## Further Reading

- Mathematics article *Introduction to the Antisymmetric Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-quaternionic-sesqualgebra-of-biquaternions.md`), for the rule, the class, the coordinate form and the conjugate-alternation.
- Mathematics article *The Conjugate Cross Product and the Jacobi Failure of the Antisymmetric Quaternionic Sesqualgebra* (`articles_maths/the-conjugate-cross-product-and-the-jacobi-failure-of-the-antisymmetric-quaternionic-sesqualgebra.md`), for the diagonal and the failure of the Jacobi identity.
- Mathematics article *The 12 Products of the Biquaternion Complex Space* (`articles_maths/the-12-products-of-the-biquaternion-complex-space.md`), for the placement of AQS among the twelve and its laws.
- Mathematics article *Remarkable Subspaces under the Antisymmetric Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-antisymmetric-quaternionic-sesqualgebra-of-biquaternions.md`), for the behaviour of the operation on the remarkable subspaces.
- Mathematics article *The Sesquilinear Pairing of the Antisymmetric Quaternionic Sesqualgebra* (`articles_maths/the-sesquilinear-pairing-of-the-antisymmetric-quaternionic-sesqualgebra.md`), for the pairing of a value with a third element, the Gram matrix of the basis pairs, the forms invariant under the block and the trace form.
- Companion article *The Gauge Metric as a Product: the Symmetric Quaternionic Sesquilinear Product*, for the symmetric half of the same row.
- Companion article *A Bracket Invisible on the Real Forms: the Complex Witness of the Jacobi Failure*, for the failure of the bracket to close.
- Companion article *The States the Indefinite Metric Cannot Normalise*, for the state side that this operation's values are not.
- Companion article *Observables, Gauge Generators and the Chirality of the Internal Action*, for the gauge generators and the boundary between an axial vector and a generator.
- Companion article *Pancharatnam's Phase and the Polarization Sphere in Biquaternionic Form*, for the physical polarisation.
- Companion article *The Self-Dual and Anti-Self-Dual Split: Spin 1 from the Biquaternion Material Sector*, for the spin-one representation of the material sector.
