# __A Bracket Invisible on the Real Forms: the Complex Witness of the Jacobi Failure__

## Introduction

The antisymmetric half of the fourth product is a bracket by parity: it is conjugate-alternating, its
value is a pure vector, and it is the natural candidate for the internal bracket of the gauge side of the
frame. A bracket that is to organise an algebra of transformations must satisfy the **Jacobi identity**;
a bracket that fails it is not a Lie bracket, and the algebra it would generate is not a Lie algebra. The
antisymmetric gauge product **fails the Jacobi identity**, and this article is about the witness and about
one property of the witness that the rest of the band has not yet used: **the failure is invisible on the
real quaternion forms**. At the witness

$$
(x,y,z)=(e_1,\,e_1,\,ie_2),
\qquad
\tilde P\diamond\tilde Q=\mathbf{P}\times\overline{\mathbf{Q}},
$$

the cyclic sum is

$$
(\tilde x\diamond\tilde y)\diamond\tilde z+(\tilde y\diamond\tilde z)\diamond\tilde x+(\tilde z\diamond\tilde x)\diamond\tilde y=-2ie_2,
$$

and it differs from zero. The witness uses the element $ie_2$, which is **not** on the real basis
$\{e_0,e_1,e_2,e_3\}$. On the real quaternion subspace the operation coincides with the **plain**
antisymmetric part $\mathbf{P}\times\mathbf{Q}$, which **is** a Lie bracket — it satisfies the Jacobi
identity — and a check performed on the real basis finds no failure at all. The failure of the complex
bracket is therefore a statement about the algebra as a **complex** space, and a real-form computation,
however extensive, cannot see it.

The article owns the failure's reading: the witness, its value, why the witness needs a complex element,
what a real-form check would report, and the negative reading that no gauge algebra is obtained. It defers
the computation to the mathematics article *The Conjugate Cross Product and the Jacobi Failure of the
Antisymmetric Quaternionic Sesqualgebra*; the comparison of the failing brackets to *The 12 Products of the Biquaternion Complex Space*; the matrix models to *The Antisymmetric Quaternionic
Sesqualgebra in the Matrix Representations*; the subspaces to *The Six Subspaces under the Antisymmetric
Quaternionic Sesqualgebra of Biquaternions*; the negative reading to *The Gauge Group Ceiling: Why the
Biquaternion Algebra Reaches SU(2) but Not SU(3)* and *What the Biquaternion Algebra Cannot Do: A Catalogue of Algebraic Obstructions*; and
the obstruction's place in the map of the four general products to *The Four General Products and Their Physical Readings:
the Two Algebras and the Two Sesqualgebras*.

**Conventions.** As in the companion articles of this block:
$\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$, $e_0=1$,
$e_k^{2}=-e_0$, $e_1e_2=e_3$, central $i$; $\tilde Q=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$,
scalar part $\mathrm{Sc}(\tilde Q)=Q_0$ and vector part $\mathbf{Q}=\sum_kQ_ke_k$; the natural conjugation
$\tilde Q^{\natural}=Q_0e_0-\mathbf{Q}$, the coefficientwise one $\bar{\tilde Q}=\sum_\mu\bar Q_\mu e_\mu$,
and the star $\tilde Q^{*}=\overline{\tilde Q^{\natural}}$; $(\mathbf{P},\mathbf{Q})=\sum_kP_kQ_k$ and
$\times$ are the bilinear dot and cross products; the block's operation is
$\tilde P\diamond\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q^{*}-\tilde Q^{*}\tilde P^{\natural})=\mathbf{P}\times\overline{\mathbf{Q}}$;
the plain antisymmetric part is $\mathrm{APA}$, $\tilde P\wedge\tilde Q=\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)=\mathbf{P}\times\mathbf{Q}$;
the sectors are $\mathbb{M}_+$ and $\mathbb{M}_-$. All conventions are
those of *Conventions in the Biquaternion Universe*.

**A notation caution.** The antisymmetric quaternionic sesquilinear product is written $\diamond$ here, the
symbol of *Introduction to the Antisymmetric Quaternionic Sesqualgebra of Biquaternions*, which the menu
comment renders $\wedge$. The plain antisymmetric product is written $\wedge$ in that article, and it is
written $\wedge$ here to keep the two apart; the stable identifiers are $\mathrm{AQS}$ and $\mathrm{APA}$.

## The Three Failing Brackets

Three of the four antisymmetric parts fail the Jacobi identity — $\mathrm{AQA}$, $\mathrm{APS}$ and
$\mathrm{AQS}$ — while the plain one, $\mathrm{APA}$, satisfies it. The table collects
the witnesses and the basis elements they use.

| bracket | definition | witness $(x,y,z)$ | cyclic sum | basis elements used |
|---|---|---|---|---|
| $\mathrm{AQA}$ | $\tfrac12(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P)$ | $(e_0,e_1,e_2)$ | $-e_3$ | all four real |
| $\mathrm{APS}$ | $\tfrac12(\tilde P\tilde Q^{*}-\overline{\tilde Q}\tilde P^{\natural})=\mathrm{Vect}(\tilde P\tilde Q^{*})$ | $(e_0,e_1,e_2)$ | $+e_3$ | all four real |
| $\mathrm{AQS}$ | $\tfrac12(\tilde P^{\natural}\tilde Q^{*}-\tilde Q^{*}\tilde P^{\natural})=\mathbf{P}\times\overline{\mathbf{Q}}$ | $(e_1,e_1,ie_2)$ | $-2ie_2$ | $ie_2$ is complex |

The **plain** antisymmetric part $\mathrm{APA}$, the first row of the four general products, is absent from the
table, and its absence is the reason the table is worth drawing: $\mathrm{APA}=\mathbf{P}\times\mathbf{Q}$
is the ordinary cross product of two real vectors continued to the algebra, it **is** the Lie bracket of
$\mathfrak{so}(3)$ and of the vector representation of $\mathfrak{su}(2)$, and it **satisfies** the Jacobi
identity. The three failing brackets are therefore not the antisymmetric parts as such; they are the three
antisymmetric parts whose arguments pass through a **conjugation** — two through ${}^{\natural}$ in the
first slot, one through ${}^{*}$ in the second — and it is the conjugation that breaks the bracket.

**Remark (the pattern).** Each failing bracket uses one conjugation more than the plain one. The plain
bracket conjugates nothing and closes. The bracket of $\mathrm{AQA}$ inserts ${}^{\natural}$ into the first
slot only; the bracket of $\mathrm{APS}$ inserts ${}^{*}$ into the second slot only; the bracket of
$\mathrm{AQS}$ inserts both. The failure is a failure of the conjugation, and the corpus reads it that way:
the three failures are the three ways of spoiling the plain bracket by a conjugation, and only the plain
bracket is a Lie bracket.

## The Failure at the Witness

**Proposition.** The antisymmetric gauge product fails the Jacobi identity. At the witness
$x=y=e_1$, $z=ie_2$ the cyclic sum is $-2ie_2$.

*Proof.* Compute the three terms. First, $e_1\diamond e_1=e_1\times e_1=0$, so
$(e_1\diamond e_1)\diamond(ie_2)=0$. Second, $e_1\diamond(ie_2)=e_1\times\overline{ie_2}=e_1\times(-ie_2)=-ie_3$,
and $(-ie_3)\diamond e_1=(-ie_3)\times e_1=-i(e_3\times e_1)=-ie_2$. Third, $(ie_2)\diamond e_1=ie_2\times e_1=-ie_3$,
and $(-ie_3)\diamond e_1=-ie_2$ as before. The cyclic sum is $0+(-ie_2)+(-ie_2)=-2ie_2$, which is not
zero. Verified on the witness. $\square$

**Remark (the value is not a numerical accident).** The witness is the smallest one; the failure holds on
an open set around it, because the cyclic sum of a trilinear expression is continuous and is nonzero at the
witness. The identity is therefore not merely undefined somewhere; it is false.

## Why the Witness Needs the Complex Element

### The Coincidence on the Real Forms

Let $\mathbb{H}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_0,e_1,e_2,e_3\}$ be the real quaternion
subspace. On it the coefficientwise conjugation is the identity, $\bar{\tilde Q}=\tilde Q$, and the
conjugate in the second argument of the rule does nothing:

$$
\tilde P,\tilde Q\in\mathbb{H}_{\mathbb{B}}\quad\Longrightarrow\quad
\tilde P\diamond\tilde Q=\mathbf{P}\times\overline{\mathbf{Q}}=\mathbf{P}\times\mathbf{Q}=\tilde P\wedge\tilde Q .
$$

The complex bracket restricted to the real quaternion subspace **is** the plain antisymmetric part. Since
the plain antisymmetric part is a Lie bracket, the restriction of the complex bracket to the real forms is
associative in the sense of Jacobi: **the failure does not descend to the real forms**, because on them
there is no failure.

### What Follows

The witness of any failure of a bracket whose restriction to $\mathbb{H}_{\mathbb{B}}$ is $\mathrm{APA}$
must use at least one element with a **complex coefficient** — an element outside
$\mathbb{H}_{\mathbb{B}}$, hence an element of $i\mathbb{H}_{\mathbb{B}}$ or a genuine mixture, in the
sense of the decomposition

$$
\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}=\mathbb{H}_{\mathbb{B}}\oplus i\mathbb{H}_{\mathbb{B}}.
$$

The witness $(e_1,e_1,ie_2)$ uses exactly one such element, and one is the
minimum: two of its three arguments are real basis elements.

## What a Real-Form Check Would Report

The consequence for practice is a caution the article states plainly, because it is the reason the
observation belongs in a physics band and not only in an algebra one.

**A check performed on the real basis elements $e_0,e_1,e_2,e_3$ finds no failure.** Every cyclic sum of
$\mathrm{AQS}$ on a triple of real basis elements vanishes, because on them the bracket is $\mathrm{APA}$
and $\mathrm{APA}$ is a Lie bracket. A computation that samples the real forms — a natural first move,
since the quaternion basis is real and the physical interpretation of the algebra commonly starts from
$\mathbb{H}_{\mathbb{B}}$ — reports the bracket as a Lie bracket, and the report is wrong.

**The failure appears as soon as one imaginary basis element enters.** On the extended basis
$\{e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3\}$ the cyclic sum is nonzero on $72$ of the $512$ triples (a
computed count, reproduced in the ledger), and the smallest witness is $(e_1,e_1,ie_2)$. The count is
given to show the shape of the failure: rare on the basis, common on the space, absent on the real forms.

**The methodological statement.** The Jacobi failure of the antisymmetric gauge product is a property of
the **complex** operation and not of its real restriction. A reader who tests the bracket on real or on
material elements will not see it, and the reason is not a choice of variables but the algebra: the
conjugation that the operation inserts is the identity on the real forms and only there. The failure is
therefore one of the places where the complex structure of $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$
carries content that the real quaternion algebra does not.

**The failure here is one instance of a general fall, and the count measures it.** The blindness of this
article is not peculiar to the gauge bracket. *The 12 Products of the Biquaternion Complex Space* proves
that the twelve operations of the complex space fall to **ten** on the real part: two pairs coincide there,
the antisymmetric plain bilinear product with the antisymmetric quaternionic sesquilinear product, and the
symmetric quaternionic bilinear product with the symmetric plain sesquilinear product. The count $12$
against $10$ is therefore the **total size of what the real forms erase**, and each coincidence is one
place where a real element cannot tell a naturally conjugated operation from a plain one. Offered **as a
reading**, the fall is the algebraic measure of the complex structure of the space: a classical, real
description carries ten operations where the complex space carries twelve, and it follows that **if one
member of a coincident pair satisfies an identity and the other fails it, no real-form computation can
report the difference** — which is exactly this article's caution, one pair of the two. The algebra proves
the two coincidences; the naming of the fall as the algebraic measure of the complex structure is the
framework's, and the count is a count on a basis and not an invariant.

## The Negative Reading: No Gauge Algebra

A bracket that fails the Jacobi identity is not a Lie bracket, and a bracket that is not a Lie bracket
generates no Lie algebra. The negative reading is therefore direct and it is referred, not restated: the
antisymmetric gauge product does not supply the internal Lie algebra of the framework, and no gauge group
is read from it. The ceiling of the framework's gauge reach, and the reason the biquaternion algebra
reaches $SU(2)$ and not $SU(3)$, are *The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2)
but Not SU(3)*; the catalogue of the algebra's obstructions is *What the Biquaternion Algebra Cannot Do: A Catalogue of Algebraic Obstructions*;
and the map that places the three failing brackets among the twelve operations is *The 12 Products of the Biquaternion Complex Space*.

**The positive reading, stated briefly.** The failure is not a defect to be repaired; it is a
**characteristic** of the operation, and it is one of the two facts that fix the reading of the fourth
block. The block's product has no unit and no associativity on the symmetric side and no Lie bracket on the
antisymmetric side; what it has is an indefinite pairing and a bracket that carries a direction without
organising a Lie algebra. The corpus reads the block as gauge **because** its invariants are pairings and
its bracket is not a gauge algebra, and the negative reading is the boundary that keeps the word from
being over-read. The pairing's indefiniteness is the work of the natural conjugation of the first slot, and
the bracket's failure to close is **shared by both slots**: the plain antisymmetric part $\mathrm{APA}$ is
a Lie bracket, the first-slot conjugation $\mathrm{AQA}$ is not, and the second-slot star spoils the
closure a second time, since the plain sesquilinear antisymmetric part $\mathrm{APS}$ fails the identity as
well. The metric is the first slot's; the non-closure is not, and *The Gauge Metric as a Product: the
Symmetric Quaternionic Sesquilinear Product* states both with the boundary. An indefinite metric is not an
unphysical metric, and the bracket's failure does not touch the gauge theory, which is carried by the
pairing.

**The defect is not repaired by a real-form check.** The caution above says that a real-form computation is
blind to the failure. The sharper statement, and the reason the negative reading is a statement about the
**complex** operation, is that the blindness is not **repairable by linear combination**. The defect lives
in the complexified algebra: it vanishes on the real span of the basis and reappears as soon as a complex
coefficient enters, and no real-linear combination of the real-form values can conjure it back. Read on the
algebra rather than on a computation, the operation is therefore not the bracket of a real Lie algebra of
matrices over the real form, and the negative reading — *no gauge algebra* — is a statement about
$\mathrm{AQS}$ and not about a particular choice of basis or of variables. The methodological companion of
this paragraph is a positive rule: a bracket of the algebra must be tested on **complex** elements, because
the real form is exactly the place where the complex structure of $\mathbb{B}$ is invisible.

**The defect does not close.** A non-associative law can fail in two ways: the bracket of the prescribed
elements can leave the span, or it can stay inside a span that is nevertheless not a Lie algebra. The
second is what happens here. The real span of the values of $\mathrm{AQS}$ over $100$ random complex triples is
the **whole** six-dimensional vector subspace of $\mathbf{P}$ and $\mathbf{Q}$, so the operation is far from
being too small; what it fails to be is a Lie bracket, because its cyclic sum is not zero on any of those
triples. The closure one can form from the operation is therefore a **vector space and not an algebra**: the
defect does not shrink under closure, it is inherited by the generated span. The name is the article's; the
dimension count and the vanishing of the cyclic sum are recomputed. The upshot for the framework is that the
antisymmetric half generates a **direction space** — the axial vectors it returns — and not a gauge algebra,
which is the negative reading stated in its sharpest algebraic form.

### Named Readings of the Invisibility

Four further readings of the same invisibility are recorded here, each under a name of its own and each labelled a reading rather than a theorem; the invisibility they rest on is the body's.

- **Complex-structure obstruction.** The invisibility of the failure on the real form is read as a statement about the **complex structure** of the algebra: the obstruction lives in the complexification, and a computation restricted to the real span cannot see it because the real form is the locus where the complex structure is erased. The reading turns the methodological rule into a physical one — the obstruction is a complex (chiral) effect, and a purely real description is blind to it — and its boundary is that the algebra supplies the blindness and not a measured chirality.
- **Non-closure as anomaly.** The inheritance of the defect under closure — the generated span is a vector space and not an algebra — is read as an **anomaly-shaped** statement: a consistency condition that holds on the classical (real) description fails on the full (complex) one, and the failure does not cancel as the structure is closed up. The name is offered by analogy with the anomaly of a classical symmetry that fails at the quantum level; the boundary is sharp, since the algebra supplies the inherited failure and no quantisation.
- **Classical blindness.** The fact that a real-form check reports the obstruction as absent is read as a **methodological** statement with physical content: a classical, real description of the frame cannot separate the member of a coincident pair that satisfies the Jacobi identity from the member that fails it. The name is the physical reading of the twelve-to-ten fall of *The 12 Products of the Biquaternion Complex Space*, and it is stated there as a caution about computations and here as a reading about descriptions.
- **Complex engagement as a $\mathbf{T}$-odd seat.** The failure is carried by the central imaginary alone: the operation coincides with the closing real bracket exactly where the coefficients are real, and fails only where the complex structure is engaged. Offered as a **labelled speculation**, one may read that engagement as a $\mathbf{T}$-odd seat: the description in which the bracket fails is the one that carries the central imaginary, and the framework's map between the real description and that one is the **Wick rotation**, the analytic continuation to imaginary time $t \to -i\tau$ (*The Wick Rotation in the Biquaternion Universe*, *The Four Other Remarkable Subspaces*); the seat is therefore the complexification of the time coordinate and not a reversal $t \to -t$. The boundary is sharp and is the reason the reading is labelled: the algebra supplies the complex engagement and no arrow of time, and it supplies no $CP$-violating phase — the framework's EDM article records that the framework has no $CP$-violating phase of its own (*The Electric Dipole Moment and the Biquaternion Anti-Hermitian Structure*) — so the name $\mathbf{T}$-odd here denotes the engagement of the complex time coordinate and not a measured asymmetry.

## The Limits

- **The failure is a property of $\mathrm{AQS}$ and not of every antisymmetric part.** The plain
  antisymmetric part is a Lie bracket, and the negative reading concerns the three brackets spoiled by a
  conjugation.
- **The witness count is a computation on the basis and not an invariant.** The number $72$ of failing
  triples on the eight-element basis is reported as the shape of the failure; it is not a theorem and it
  changes with the basis.
- **The failure is not a failure of the block's physics.** The block's job is the gauge pairing and the
  direction it carries, not the generation of a gauge algebra; the negative reading closes the second job
  and does not touch the first.
- **The matrix-model statement is cited, not derived.** That the failure reappears in the two matrix
  models of the block, where the operation is the nested commutator with the adjugate, is *The
  Antisymmetric Quaternionic Sesqualgebra in the Matrix Representations*; no matrix computation is
  repeated here.

## The Ledger

**Proved, and recomputed.** The antisymmetric gauge product fails the Jacobi identity at the witness
$(x,y,z)=(e_1,e_1,ie_2)$, with cyclic sum $-2ie_2$, and the failure holds on an open neighbourhood. The
plain antisymmetric part $\mathrm{APA}=\mathbf{P}\times\mathbf{Q}$ satisfies the Jacobi identity, and it is
the restriction of the gauge bracket to the real quaternion subspace: on $\mathbb{H}_{\mathbb{B}}$, where
$\overline{\mathbf{Q}}=\mathbf{Q}$, the two coincide. Consequently every cyclic sum on a triple of real
basis elements vanishes (all $64$ triples checked), and the smallest witness needs the complex element
$ie_2$; on the eight-element basis $\{e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3\}$ exactly $72$ of the $512$
triples fail. The comparison of the three failing brackets is reproduced from *The 12 Products of the Biquaternion Complex Space*, and the computation from *The Conjugate Cross Product and the
Jacobi Failure of the Antisymmetric Quaternionic Sesqualgebra*.

**Reading.** That the Jacobi failure is a property of the complex operation and invisible on the real
forms, and that a real-form check of the bracket is therefore blind to it; that the blindness is not
repairable by linear combination, so the negative reading is a statement about the complex operation; that
the operation does not close to a Lie algebra even though its values span the whole vector subspace, so it
generates a direction space and not an algebra; and that the blindness is one instance of the general fall
of the twelve operations to ten on the real part, so that the count $12$ against $10$ is read as the
algebraic measure of the complex structure. Three further readings, named in §*Named Readings of the Invisibility*: **complex-structure obstruction**, **non-closure as anomaly** and **classical
blindness**.

**Not claimed.** That the failure can be removed by a change of variables; that the gauged bracket or every
antisymmetric part fails; that the witness count is an invariant; that the matrix-model form of the failure
is re-derived here; that the count $12$ against $10$ is an invariant, or that the naming of the fall as the
measure of the complex structure is forced by the algebra rather than chosen.

## Physical Readings

The complex witness reads as a statement about where a failure can be seen: a bracket whose Jacobi failure needs an element off the real forms is a bracket that no real form can diagnose, so the complex structure is not a convenience but the carrier of the obstruction. Read against the local complex structure, the choice of which real form a point of the algebra uses is a choice of embedding, so the failure this article finds is a failure of the complex object that each of its real sectors hides. Read on the grid, the witness is the reason the quaternionic sesquilinear row is classified as a gauge structure and not as a state space.

## Summary

The antisymmetric gauge product $\tilde P\diamond\tilde Q=\mathbf{P}\times\overline{\mathbf{Q}}$ **fails
the Jacobi identity**, at the witness $(e_1,e_1,ie_2)$ where the cyclic sum is $-2ie_2$. It is one of the
**three failing brackets** of the twelve — $\mathrm{AQA}$, $\mathrm{APS}$, $\mathrm{AQS}$ — while the
plain antisymmetric part $\mathrm{APA}=\mathbf{P}\times\mathbf{Q}$ **satisfies** the identity; the
difference is the conjugation, and each failing bracket inserts one conjugation more than the plain one.
The distinctive property of the $\mathrm{AQS}$ failure is that **it is invisible on the real forms**: on
the real quaternion subspace the conjugate in the second slot is the identity, the gauge bracket
*coincides* with the plain Lie bracket $\mathrm{APA}$, and every real-basis triple has cyclic sum zero. The
failure therefore lives on the **complex** elements: the smallest witness uses $ie_2$, and a real-form
check of the bracket — the natural first move in a quaternion setting — reports it as a Lie bracket and is
wrong. The negative reading is that a bracket failing Jacobi generates no Lie algebra, so the
antisymmetric gauge product does not supply the internal gauge algebra; the ceiling and the obstruction are
*The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)* and *What the
Biquaternion Algebra Cannot Do: A Catalogue of Algebraic Obstructions*. The block's product carries an
invariant indefinite pairing and a bracket that carries a direction without organising a Lie algebra, and
that is the reading the band closes with.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\diamond\tilde Q=\mathbf{P}\times\overline{\mathbf{Q}}$ | the antisymmetric gauge product, $\mathrm{AQS}$ |
| $\tilde P\wedge\tilde Q=\mathbf{P}\times\mathbf{Q}$ | the plain antisymmetric part, $\mathrm{APA}$ |
| $\mathrm{AQA}=\tfrac12(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P)$ | the quaternionic antisymmetric part |
| $\mathrm{APS}=\mathrm{Vect}(\tilde P\tilde Q^{*})$ | the plain sesquilinear antisymmetric part |
| $(e_1,e_1,ie_2)$ | the witness of the Jacobi failure |
| $-2ie_2$ | the cyclic sum at the witness |
| $(e_0,e_1,e_2)\to-e_3$, $(e_0,e_1,e_2)\to+e_3$ | the real-basis witnesses of $\mathrm{AQA}$ and $\mathrm{APS}$ |
| $\mathbb{H}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_0,e_1,e_2,e_3\}$ | the real quaternion subspace; there the bracket is $\mathrm{APA}$ |
| $ie_2$ | the essential complex element; no real-basis witness exists |
| $72/512$ | the failing triples on the eight-element basis; the shape of the failure |

## Further Reading

- Mathematics article *The Conjugate Cross Product and the Jacobi Failure of the Antisymmetric Quaternionic Sesqualgebra* (`articles_maths/the-conjugate-cross-product-and-the-jacobi-failure-of-the-antisymmetric-quaternionic-sesqualgebra.md`), for the computation of the cyclic sum and the witness.
- Mathematics article *The 12 Products of the Biquaternion Complex Space* (`articles_maths/the-12-products-of-the-biquaternion-complex-space.md`), for the three failing brackets and the witnesses.
- Mathematics article *The Antisymmetric Quaternionic Sesqualgebra in the Matrix Representations* (`articles_maths/the-antisymmetric-quaternionic-sesqualgebra-in-the-matrix-representations.md`), for the nested commutator with the adjugate.
- Mathematics article *The Six Subspaces under the Antisymmetric Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/the-six-subspaces-under-the-antisymmetric-quaternionic-sesqualgebra-of-biquaternions.md`), for the behaviour of the bracket on the distinguished subspaces.
- Companion article *The Cross Product of a Vector with Its Conjugate: the Antisymmetric Gauge Product*, for the product whose failure this is.
- Companion article *The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)*, for the negative reading and the reach of the internal action.
- Companion article *What the Biquaternion Algebra Cannot Do: A Catalogue of Algebraic Obstructions*, for the catalogue of the algebra's obstructions.
- Companion article *The Four General Products and Their Physical Readings: the Two Algebras and the Two Sesqualgebras*, for the map that places the failing brackets among the twelve operations.
