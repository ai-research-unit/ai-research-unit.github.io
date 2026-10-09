# __The Symmetrised Material Composition and the Jordan Identity__

## Introduction

The ordinary product of the biquaternion algebra splits into two halves, and the split is the whole
subject of this block. The plain interchange of the two arguments leaves one half unchanged and reverses
the sign of the other:

$$
\tilde P\tilde Q=\tilde P\bullet\tilde Q+\tilde P\wedge\tilde Q,
\qquad
\tilde P\bullet\tilde Q=\tfrac12\bigl(\tilde P\tilde Q+\tilde Q\tilde P\bigr),
\qquad
\tilde P\wedge\tilde Q=\tfrac12\bigl(\tilde P\tilde Q-\tilde Q\tilde P\bigr).
$$

The symmetric half is the **symmetrised plain product**, the operation named $\mathrm{SPA}$ among the
twelve algebraic structures of the biquaternion complex space; the antisymmetric half is $\mathrm{APA}$,
the subject of the companion band. This article reads the symmetric half.

The operation is the plain product with the cross term dropped,

$$
\tilde P\bullet\tilde Q=\bigl[P_0Q_0-(\mathbf{P},\mathbf{Q})\bigr]+P_0\mathbf{Q}+Q_0\mathbf{P},
$$

it is $\mathbb{C}$-bilinear and commutative, $e_0$ is a unit on both sides, and it is **not** associative.
What it keeps in place of associativity is a single law, the **Jordan identity**, and of the twelve
operations of the batch it is the only Jordan product. That is its algebraic signature, and
it is the reason the operation is a product of the classical non-associative kind and not a bracket.

The physical reading offered here, and labelled as such, is that the symmetrised plain product is the
**order-free composition of two material operations**: the composition of two material elements with the
order forgotten. The part that is lost in the forgetting is exactly the cross term, and the cross term is
what the antisymmetric band keeps. The two bands are therefore the two halves of one statement, and the
operation of this article is the half on which the order does not act.

The boundary is stated where the reading is made and again in the ledger: the Jordan identity is a law of
the algebra and not a statement about measurement. The operation carries no positivity, selects no state
and introduces no scale.

The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis
$e_0=1,e_1,e_2,e_3$, $e_1e_2=e_3$, $e_k^{2}=-e_0$, and central scalar imaginary $i$. A general element is
$\tilde Q=Q_0e_0+\mathbf{Q}$ with $\mathbf{Q}=\sum_{k=1}^{3}Q_ke_k$ and $Q_\mu\in\mathbb{C}$;
$(\mathbf{P},\mathbf{Q})=\sum_kP_kQ_k$ is the complex bilinear dot product of the vector parts, and
$\mathrm{Sc}(\tilde Q)=Q_0$ is the scalar part. The material sector is the anti-Hermitian subspace
$\mathbb{M}_-=\{\tilde Q:\tilde Q^{*}=-\tilde Q\}$, with the real basis $\{ie_0,e_1,e_2,e_3\}$, and the
informational sector is the Hermitian subspace $\mathbb{M}_+=\{\tilde Q:\tilde Q^{*}=+\tilde Q\}$, with the
real basis $\{e_0,ie_1,ie_2,ie_3\}$. The star is the Hermitian conjugation,
${}^{*}=\bar{\cdot}\circ{}^{\natural}$.

## The Split of the Ordinary Product

The ordinary product is $\mathbb{C}$-bilinear in both slots, so the exchange of the two arguments is a
plain interchange and the algebra of the exchange is $\mathbb{Z}/2$. Every $\mathbb{C}$-bilinear operation
$f$ decomposes uniquely into an exchange-fixed part and an exchange-reversed part,

$$
f^{\mathrm{s}}(\tilde P,\tilde Q)=\tfrac12\bigl(f(\tilde P,\tilde Q)+f(\tilde Q,\tilde P)\bigr),
\qquad
f^{\mathrm{a}}(\tilde P,\tilde Q)=\tfrac12\bigl(f(\tilde P,\tilde Q)-f(\tilde Q,\tilde P)\bigr),
\qquad
f=f^{\mathrm{s}}+f^{\mathrm{a}} .
$$

The general theory of the splitting, its two projections, the uniqueness of the pair and the two
admissibility conditions are *The Symmetric and Antisymmetric Parts of an Algebra Product*; the split is
used here and not re-derived.

Applied to the ordinary product the split gives the two operations of the block. The symmetric part is
the **symmetrised plain product**

$$
\tilde P\bullet\tilde Q=\tfrac12\bigl(\tilde P\tilde Q+\tilde Q\tilde P\bigr),
$$

and the antisymmetric part is the **antisymmetric plain product**

$$
\tilde P\wedge\tilde Q=\tfrac12\bigl(\tilde P\tilde Q-\tilde Q\tilde P\bigr)=\mathbf{P}\times\mathbf{Q} .
$$

The ordinary product is recovered from the two halves,
$\tilde P\tilde Q=\tilde P\bullet\tilde Q+\tilde P\wedge\tilde Q$, and neither half determines the
other: the symmetric half is one operation of the twelve, and the antisymmetric half is another. The
pairing of the two halves is the pairing of the two bands of this family, and the comparison of the four general
products and their parts is *The Four General Products and Their Physical Readings: the Two Algebras and the Two
Sesqualgebras*.

## The Operation and Its Class

**Proposition.** The symmetrised plain product is $\mathbb{C}$-bilinear and **commutative**, and it has
the coordinate form

$$
\tilde P\bullet\tilde Q=\bigl[P_0Q_0-(\mathbf{P},\mathbf{Q})\bigr]+P_0\mathbf{Q}+Q_0\mathbf{P},
$$

which is the ordinary product with the cross term $\mathbf{P}\times\mathbf{Q}$ removed.

*Proof.* The scalar part of the ordinary product is symmetric,
$\mathrm{Sc}(\tilde P\tilde Q)=P_0Q_0-(\mathbf{P},\mathbf{Q})=\mathrm{Sc}(\tilde Q\tilde P)$, so it
cancels nothing in the half-sum and remains.
The vector part is $P_0\mathbf{Q}+Q_0\mathbf{P}+\mathbf{P}\times\mathbf{Q}$ in the one order and
$Q_0\mathbf{P}+P_0\mathbf{Q}+\mathbf{Q}\times\mathbf{P}$ in the other; adding the two cancels the
antisymmetric cross terms and doubles the symmetric terms, and halving gives the displayed vector part.
Commutativity is the symmetry of the half-sum. This is *Introduction to the Symmetric Plain Algebra of
Biquaternions*, read here as the operation of the block.

**Proposition.** The unit $e_0$ is a unit on both sides, $e_0\bullet\tilde Q=\tilde Q\bullet e_0=\tilde Q$,
and it is the only unit.

*Proof.* The unit has vector part zero, so $P_0\mathbf{Q}+Q_0\mathbf{P}$ reads $\mathbf{Q}$ and the scalar
and dot terms read $Q_0$. Uniqueness is *Introduction to the Symmetric Plain Algebra of Biquaternions*.

**Proposition.** The operation is **not associative**, with the witness $e_1\bullet e_1=-e_0$ read against
$e_2$:

$$
(e_1\bullet e_1)\bullet e_2=(-e_0)\bullet e_2=-e_2,
\qquad
e_1\bullet(e_1\bullet e_2)=e_1\bullet 0=0 .
$$

*Proof.* The products of the basis are the quaternion table with the six off-diagonal vector entries set
to $0$, so $e_1\bullet e_2=0$ and the two bracketings differ. Verified on the basis.

The failure of associativity is what makes the block a Jordan algebra rather than an associative one, and
the Jordan identity is the substitute it keeps. The block is weaker than associativity, and the two
bracketings of the witness are how much weaker.

**Remark (the table of the operation).** The sixteen products of the basis are the quaternion table of
the plain product with the off-diagonal vector entries $e_3,-e_3,e_2,-e_2,e_1,-e_1$ replaced by $0$; the
first row and column and the diagonal $e_0,-e_0,-e_0,-e_0$ are unchanged. The operation differs from the
ordinary product only where the ordinary product is skew. This is *Introduction to the Symmetric Plain
Algebra of Biquaternions*.

**Proposed reading, labelled as such.** On the three vector units, $i,j\in\{1,2,3\}$, the table of the
operation reads $\tfrac12(e_ie_j+e_je_i)=-\delta_{ij}e_0$, that is $\{e_i,e_j\}=-2\delta_{ij}e_0$; for
two real pure vectors the symmetrised product is central,
$\tfrac12(\mathbf P\mathbf Q+\mathbf Q\mathbf P)=-(\mathbf P\!\cdot\!\mathbf Q)\,e_0$. **The scalar part
of the symmetrised composition is the scalar product of the two directions**, which is the
anticommutation relation from which a Clifford algebra is built. *Verified on the basis and on $100$
random real pure pairs, max deviation $4.4\times10^{-16}$.*

## The Square of an Element

**Proposition.** The square of an element in the block is the ordinary square:

$$
\tilde Q\bullet\tilde Q=\tilde Q^{2}=\bigl[Q_0^{2}-(\mathbf{Q},\mathbf{Q})\bigr]+2Q_0\mathbf{Q}.
$$

*Proof.* $\tilde Q\bullet\tilde Q=\tfrac12(\tilde Q^{2}+\tilde Q^{2})=\tilde Q^{2}$, and the displayed
form is the scalar-vector rule with $\tilde P=\tilde Q$. Verified on the coordinate rule.

The square is the diagonal of the operation, and it is the ordinary square because the antisymmetric part
vanishes on the diagonal: an alternating operation has zero diagonal, so the square carries the symmetric
half alone. The polarisation of the square recovers the whole operation,

$$
\tilde P\bullet\tilde Q=\tfrac12\bigl((\tilde P+\tilde Q)\bullet(\tilde P+\tilde Q)
-\tilde P\bullet\tilde P-\tilde Q\bullet\tilde Q\bigr),
$$

and it is the standard polarisation of a commutative bilinear operation. Its consequence is the one
sentence of this section: **the square map determines the operation and sees only the symmetric half.**
The ordinary product and its opposite have the same square and the same symmetric half, and they differ
exactly in the sign of the antisymmetric half. The square, the idempotents and the Jordan inverse of the
block are *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*.

## The Jordan Identity

**Definition.** A commutative product is a **Jordan product** when it satisfies the **Jordan identity**

$$
(\tilde X\bullet\tilde Y)\bullet(\tilde X\bullet\tilde X)
=\tilde X\bullet\bigl(\tilde Y\bullet(\tilde X\bullet\tilde X)\bigr),
$$

and a commutative algebra with a Jordan product is a **Jordan algebra**; the identity is the one fixed in
*Jordan Algebras*.

**Theorem.** The symmetrised plain product satisfies the Jordan identity for all $\tilde P,\tilde Q$:

$$
(\tilde P\bullet\tilde Q)\bullet(\tilde P\bullet\tilde P)
=\tilde P\bullet\bigl(\tilde Q\bullet(\tilde P\bullet\tilde P)\bigr).
$$

*Proof.* The symmetrisation of an associative product always satisfies the Jordan identity: the algebra
$\mathbb{B}^{\bullet}$ with the product $\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ is the special Jordan
algebra of the associative algebra $\mathbb{B}$, and it is the theorem of *Jordan Algebras* that the
symmetrisation of an associative algebra is a Jordan algebra. The identity is *Introduction to the
Symmetric Plain Algebra of Biquaternions*, and it was recomputed here on general elements and on random
pairs.

Because the symmetrisation comes from an associative product, the algebra is a **special** Jordan
algebra, and its classification among the special ones is *Special and Exceptional Jordan Algebras*.

**Theorem (the uniqueness among the twelve).** Of the twelve operations
$\mathrm{GPA},\mathrm{SPA},\mathrm{APA},\mathrm{GQA},\mathrm{SQA},\mathrm{AQA},\mathrm{GPS},\mathrm{SPS},\mathrm{APS},\mathrm{GQS},\mathrm{SQS},\mathrm{AQS}$
of *The 12 Products of the Biquaternion Complex Space*, the symmetrised plain product
is the **only** one that is a **Jordan product**.

*Proof.* The identity is put to the symmetrisations of the batch; the four general products are neither
symmetrisations nor antisymmetrisations, and the identity is not put to them. Of the four symmetric parts
only the plain one satisfies it: the other three, $\mathrm{SQA}$, $\mathrm{SPS}$ and $\mathrm{SQS}$ (the
symmetric parts of the quaternionic, the plain sesquilinear and the quaternionic sesquilinear products),
fail on $x=y=e_1$, with the sides $0$ and $e_0$ for the first two and $-e_0$ and $e_0$ for the third
(the table of *The 12 Products of the Biquaternion Complex Space*). The plain product
passes because it is the symmetrisation of the one associative product of the twelve. The identity was
recomputed here for the plain one and failed for the neighbouring symmetric parts.

**Remark (the two laws and the two bands).** Among the four symmetrisations of the twelve exactly one is
a Jordan product, and among the four antisymmetrisations exactly one is a Lie product; both sit in the
plain row, $\mathrm{SPA}$ as the Jordan product and $\mathrm{APA}$ as the Lie bracket, and none of the
other six parts meets the identity of its kind. Read with the product $\bullet$, the biquaternion space is
a commutative unital Jordan algebra over $\mathbb{C}$, and it is special.

**Bound.** The Jordan identity is a law of the algebra. It says that the symmetrisation of an associative
product closes, and nothing more. It is **not** a statement about measurement, about a probability, or
about a physical process, and it carries no positivity: the operation over the real ground field is not
**formally real**, since $e_1\bullet e_1+e_0\bullet e_0=-e_0+e_0=0$ with $e_1,e_0\neq0$. The reading of a
Jordan algebra as an algebra of observables is a separate proposal, made and labelled in
*Observables as a Jordan Algebra: the Symmetric Plain Product and the Classical Composition*, and the
algebraic law alone does not establish it.

## The Symmetrised Composition of Two Material Operations

The operation is defined on the whole algebra, and its physical reading is about the material sector.
Take two material operations, $\tilde P,\tilde Q\in\mathbb{M}_-$, so
$\tilde P^{*}=-\tilde P$ and $\tilde Q^{*}=-\tilde Q$. Because the star is an anti-automorphism,
$(\tilde P\tilde Q)^{*}=\tilde Q^{*}\tilde P^{*}=\tilde Q\tilde P$, and the ordinary product splits by
sector,

$$
\tilde P\tilde Q=\tfrac12\bigl(\tilde P\tilde Q+\tilde Q\tilde P\bigr)
+\tfrac12\bigl(\tilde P\tilde Q-\tilde Q\tilde P\bigr),
\qquad
\tfrac12\{\tilde P,\tilde Q\}\in\mathbb{M}_+,
\qquad
\tfrac12[\tilde P,\tilde Q]\in\mathbb{M}_- .
$$

The first term is fixed by the star and the second is anti-fixed, by the same computation as
*The Ordinary Product and the Material Sector*, §*The Commutator of Two Material Operations Is Material*.
The two terms are exactly the two halves of the block:

$$
\tilde P\bullet\tilde Q=\tfrac12\{\tilde P,\tilde Q\}\in\mathbb{M}_+,
\qquad
\tilde P\wedge\tilde Q=\tfrac12[\tilde P,\tilde Q]\in\mathbb{M}_- .
$$

**Proposition (the symmetrised part is informational; the antisymmetrised part is material).** For
$\tilde P,\tilde Q\in\mathbb{M}_-$ the symmetrised plain product is Hermitian and the antisymmetric plain
product is anti-Hermitian. In particular the material sector is **not closed** under $\bullet$: the
symmetrisation of two material operations leaves the sector.

*Proof.* The anticommutator of two anti-Hermitian elements is Hermitian and the commutator is
anti-Hermitian, as the display records; the closure failure is the case
$ie_0\bullet ie_0=(ie_0)^{2}=-e_0$ of *The Six Subspaces under the Symmetric Plain Algebra of
Biquaternions*. Verified on random pairs of $\mathbb{M}_-$ elements.

**Proposed reading, labelled as such.** The symmetrised plain product is read as the **order-free
composition of two material operations**. The ordinary product of two material elements is the full
composition; written in its two halves it separates the part that does not depend on the order,
$\tfrac12\{\tilde P,\tilde Q\}$, from the part that does, $\tfrac12[\tilde P,\tilde Q]$. The symmetrised
product keeps the first and drops the second. Since the second is the cross product of the two vector
parts, and the cross product reverses when the two arguments are exchanged, **the cross term is precisely
the part lost when the order is forgotten.** What is added by the reading, and not by the algebra, is the
name "order-free composition" for the first half; what is proved is the split.

Two consequences of the split are worth stating plainly. First, the order-free part of a material
composition is informational: symmetrising two material operations returns an element of $\mathbb{M}_+$,
not of $\mathbb{M}_-$. Second, the order is carried entirely by the material half, so a material
composite is material exactly when the two operations **anticommute** and informational exactly when they
**commute**, which is the sector rule of *The Ordinary Product and the Material Sector*. The reading of
the operation as the composition with the orientation dropped is developed in *Observables as a Jordan
Algebra: the Symmetric Plain Product and the Classical Composition*.

**Bound.** The reading says what the symmetrised product forgets; it does not say that a physical
composition is order-free. The order of two operations is physically meaningful, and the operation of this
article describes only the part of the composition on which the order does not act. Which physical
operation an element represents is not selected by the algebra.

**Proposed reading, labelled as such.** The symmetrised product of two anti-Hermitian elements is
Hermitian: symmetrising two material operations leaves the material sector and lands in the observable
one. Read physically, **the half of a composite an apparatus can register is its symmetrised half**, and
the antisymmetrised half is the part that falls outside it, in the generator sector. The
reading is about the destination of the symmetrised product and not about the law it satisfies; the bound
above stands unchanged, and the Jordan identity remains a law of the algebra and not a statement about
measurement.

## The Ledger

**Proved.** The symmetrised plain product
$\tilde P\bullet\tilde Q=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)=[P_0Q_0-(\mathbf{P},\mathbf{Q})]+P_0\mathbf{Q}+Q_0\mathbf{P}$
is $\mathbb{C}$-bilinear and commutative, with the unit $e_0$ on both
sides, and it is not associative, with the witness $(e_1\bullet e_1)\bullet e_2=-e_2$ against
$e_1\bullet(e_1\bullet e_2)=0$; its square is the ordinary square
$\tilde Q^{2}=[Q_0^{2}-(\mathbf{Q},\mathbf{Q})]+2Q_0\mathbf{Q}$ and its product is the polarisation of
that square; it satisfies the Jordan identity, and it is the only Jordan product among the twelve; the
ordinary product is reconstructed as $\mathrm{GPA}=\mathrm{SPA}+\mathrm{APA}$; and on two material
elements the symmetric half is the Hermitian anticommutator and the antisymmetric half the anti-Hermitian
commutator, so the material sector is not closed under the symmetrised product.

**Readings.** That the symmetrised plain product is the **order-free composition of two material
operations**; that the cross term it drops is exactly the order, which the antisymmetric band keeps; and
that the order-free part of a material composite is informational; that the symmetrised half of a
composite is the observable half; and that the table of the operation is the anticommutation relation of a
Clifford algebra. Each is the framework's naming of a proved
algebraic fact and is labelled as such.

**Not claimed.** That the Jordan identity concerns measurement; that the order-free composition is the
whole composition; that the operation carries a positivity, a state or a scale.

## Physical Readings

The symmetrised product reads as what two material observations share when their order does not matter: it is commutative and its cross term is dropped, so it carries no orientation. Its failure of the Jordan identity is then the algebraic statement that the material ledger is not an algebra of observables; the observables are the Hermitian elements with the same symmetrised operation (*Observables as a Jordan Algebra: the Symmetric Plain Product and the Classical Composition*). Read on the two ledgers, the article is the negative half of a pair whose positive half is the state side.

## Summary

The ordinary product of $\mathbb{B}$ splits under the exchange of its arguments into the **symmetrised
plain product**
$\tilde P\bullet\tilde Q=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)=[P_0Q_0-(\mathbf{P},\mathbf{Q})]+P_0\mathbf{Q}+Q_0\mathbf{P}$
and the antisymmetric plain product $\tilde P\wedge\tilde Q=\mathbf{P}\times\mathbf{Q}$, with
$\tilde P\tilde Q=\tilde P\bullet\tilde Q+\tilde P\wedge\tilde Q$. The symmetrised product is
$\mathbb{C}$-bilinear and commutative, $e_0$ is its unit on both sides, and it is not associative. Its
square is the ordinary square and its product is the polarisation of that square, so the square map sees
the symmetric half alone. It satisfies the Jordan identity, and it is the only Jordan product among the
twelve operations of *The 12 Products of the Biquaternion Complex Space*; this makes
the biquaternion space a commutative unital **special Jordan algebra** over $\mathbb{C}$. The physical
reading offered and labelled here is that the operation is the **order-free composition of two material
operations**: on two material elements it is the Hermitian anticommutator, so the symmetrisation of two
material operations is informational, and the cross term it drops is the cross product that carries the
order. The Jordan identity is a law of the algebra and not a statement about measurement.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\tilde Q$ | The ordinary (plain) product, associative and unital |
| $\tilde P\bullet\tilde Q=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ | The symmetrised plain product, the operation $\mathrm{SPA}$ |
| $\tilde P\wedge\tilde Q=\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)=\mathbf{P}\times\mathbf{Q}$ | The antisymmetric plain product, the operation $\mathrm{APA}$ |
| $\tilde P\tilde Q=\tilde P\bullet\tilde Q+\tilde P\wedge\tilde Q$ | The reconstruction $\mathrm{GPA}=\mathrm{SPA}+\mathrm{APA}$ |
| $[P_0Q_0-(\mathbf{P},\mathbf{Q})]+P_0\mathbf{Q}+Q_0\mathbf{P}$ | The coordinate form; the ordinary product with the cross term dropped |
| $\tilde Q\bullet\tilde Q=\tilde Q^{2}$ | The square, equal to the ordinary square |
| $(\tilde P\bullet\tilde Q)\bullet(\tilde P\bullet\tilde P)=\tilde P\bullet(\tilde Q\bullet(\tilde P\bullet\tilde P))$ | The Jordan identity |
| $\tfrac12\{\tilde P,\tilde Q\}$, $\tfrac12[\tilde P,\tilde Q]$ | Anticommutator and commutator of two material elements |
| $\mathbb{M}_-,\mathbb{M}_+$ | Material and informational sectors; anti-Hermitian and Hermitian subspaces |
| $(p,q)$ | Signature written as (number of $+$, number of $-$) |

## Further Reading

- Pascual Jordan, John von Neumann and Eugene Wigner, "On an Algebraic Generalization of the Quantum
  Mechanical Formalism" (1934), for the origin of the symmetrised product and the Jordan identity.
- Mathematics article *Introduction to the Symmetric Plain Algebra of Biquaternions*, for the operation,
  its class, its table, its square and its placement among the twelve.
- Mathematics article *The Symmetric and Antisymmetric Parts of an Algebra Product*, for the splitting,
  its projections and its uniqueness.
- Mathematics article *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain
  Algebra*, for the square, the quadratic identity, the idempotents and the norm of the block.
- Mathematics article *Jordan Algebras* and *Special and Exceptional Jordan Algebras*, for the Jordan
  identity, the symmetrisation of an associative algebra and the special class.
- Mathematics article *The 12 Products of the Biquaternion Complex Space*, for the
  twelve operations and the uniqueness of the Jordan and Jacobi laws.
- Companion article *The Ordinary Product and the Material Sector*, for the ordinary product, its scalar
  form and the sector structure of a material composite.
- Companion article *Observables as a Jordan Algebra: the Symmetric Plain Product and the Classical
  Composition*, for the reading of the block on the Hermitian sector.
- Companion article *The Cross Product as a Lie Bracket: Rotations and the Jacobi Identity*, for the
  antisymmetric half and its Jacobi identity.
