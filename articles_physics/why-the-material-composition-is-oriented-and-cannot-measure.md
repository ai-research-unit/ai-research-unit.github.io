# __Why the Material Composition Is Oriented and Cannot Measure__

## Introduction

Two material operations can be composed, and the composite depends on their order and on which of the two
slots each occupies. This article reads the two facts that fix what the material composition can and
cannot do. **First, the composition is oriented**: the multiplication $\tilde P\star\tilde Q$ reads its
first factor through the natural conjugation and its second factor as it stands, so the two slots are not
interchangeable, and while the algebra has a left identity it has no right identity — multiplying by the
identity from the right returns the conjugate of the element and not the element. **Second, the
composition cannot measure**: the only elements that equal their own square under $\star$ are the zero
element and the identity, so the material multiplication supplies no projection, and a projection is the
algebraic form of a measurement. Where the framework does find its projections is the informational
structure, and the two facts together are read as a division of labour: the material composition carries
the interval, the informational structure carries the measurement.

The article keeps to the one product. It defers the states themselves, their null character and the
decoherence of a measurement to *The States the Indefinite Metric Cannot Normalise*
and to *Decoherence as Idempotent Projection*; the two-sector superselection structure to *The
Material-Informational Split as a Superselection Structure in Biquaternionic Form*; the non-associativity,
the associator and the ternary product to *The Associator and the Ternary Product of the Quaternionic
Product*; the left multiplications and their monoid to the mathematics article *The Left Multiplications of
the Quaternionic Product and the Opposite Monoid*; and the two-sided operators with their Hermitian
adjoints to the mathematics article *Two-Sided Operators on the Biquaternion Algebra with Hermitian
Adjoint*, whose physics reading is *Observables, Gauge Generators and the Chirality of the Internal
Action*.

**Conventions.** As in the companion *The Interval as the Square and the Charge of the Material
Composition*: $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$,
$e_k^{2}=-e_0$, $e_1e_2=e_3$; an element $\tilde Q=Q_0e_0+\mathbf Q$; the natural conjugation
$\tilde Q^{\natural}=Q_0-\mathbf Q$, the Hermitian one $\tilde Q^{*}$, the coefficientwise bar; the
sectors $\mathbb{M}_\pm$; the ordinary product $\tilde P\tilde Q$, the quaternionic product
$\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q$, the biquaternion norm $N(\tilde Q)=\sum_\mu Q_\mu^{2}$;
the real quaternion subspace $\mathbb{H}_{\mathbb{B}}=\mathbb{R}e_0+\mathbb{R}e_1+\mathbb{R}e_2+\mathbb{R}e_3$
and its imaginary multiple $i\mathbb{H}_{\mathbb{B}}$; the material coordinate $ict\,e_0+\mathbf x$.

## The Two Slots Are Not the Same

**Proposition (one-sided identity).** For every $\tilde Q$,

$$
e_0\star\tilde Q=\tilde Q , \qquad \tilde Q\star e_0=\tilde Q^{\natural} .
$$

There is no right identity for $\star$.

**Proof.** The first is $e_0^{\natural}\tilde Q=e_0\tilde Q=\tilde Q$; the second is
$\tilde Q^{\natural}e_0=\tilde Q^{\natural}$. For the last statement, suppose $\tilde U$ satisfies
$\tilde Q\star\tilde U=\tilde Q$ for all $\tilde Q$. At $\tilde Q=e_0$ this reads $\tilde U=e_0$; at
$\tilde Q=e_1$ it reads $e_1\star e_0=e_1$, that is $-e_1=e_1$, which is false. $\square$

The asymmetry is visible on a single element. Multiplying by the identity on the left changes nothing;
multiplying by it on the right conjugates. The framework reads the first slot as the operation whose
interval is read and the second as the one that acts, or the other way round according to the process; the
algebra asserts only that the roles are distinct. The product is also non-commutative, with

$$
\tilde P\star\tilde Q-\tilde Q\star\tilde P=2P_0\mathbf Q-2Q_0\mathbf P-2\,\mathbf P\times\mathbf Q ,
$$

so the order matters, and it matters through the same conjugation that produces the interval.

The operations themselves do not inherit the defect. Writing $L_{\tilde A}$ for the left multiplication
$\tilde X\mapsto\tilde A\star\tilde X$, the composition of two of them is again a left multiplication,

$$
L_{\tilde A}\circ L_{\tilde B}=L_{\tilde B\tilde A} ,
$$

so a **chain of material operations has a well-defined composite as a map**, by the associativity of
composition, while the chain of the corresponding elements has no bracketing-free product. The failure of
associativity therefore lives on the elements and not on the operations.

**Remark (verified).** The two one-sided rules and the composition rule were checked on $100$ random
triples in exact complex arithmetic, with deviations at machine precision. The failure of associativity is
not a rounding effect: the associator is nonzero on $24$ of the $64$ triples of basis elements.

## The Composite Splits into a Number and a Direction

Composing two elements of the material sector, the result need not be material, and the way it fails is
fixed.

**Proposition (the two halves of a composite).** For all $\tilde P,\tilde Q$,

$$
\tfrac12\bigl(\tilde P\star\tilde Q+\tilde Q\star\tilde P\bigr)
=\bigl(P_0Q_0+(\mathbf P,\mathbf Q)\bigr)e_0 , \qquad
\tfrac12\bigl(\tilde P\star\tilde Q-\tilde Q\star\tilde P\bigr)=P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q .
$$

The **first half is a central number** and the second half is a **vector**. The central half is the
order-independent part of the composite, the vector half the order-dependent one.

**Proof.** Add and subtract the two expansions of the product. $\square$

On the material sector this reads concretely. The square of a material element is its interval and lands
on the central line, so the material sector is not closed under the composition: $e_1\star e_1=e_0$
carries a material element to a central Hermitian one. The general statement is the proposition: a
composite of two material operations is a **number plus a direction**, the number being the
order-independent pairing of the two and the direction the order-dependent discrepancy. The numerical
check confirms the first half on $100$ random material pairs and confirms that the second half is a
general vector, with a real and an imaginary part, so it is neither material nor informational in general.

## There Is No Material Projection

A **projection** is an element equal to its own square. In the algebra the equation has two solutions, and
both are trivial.

**Proposition (the idempotents of $\star$).** The equation $\tilde\Pi\star\tilde\Pi=\tilde\Pi$ has for
solutions exactly $\tilde\Pi=0$ and $\tilde\Pi=e_0$.

**Proof.** By the square identity the left side is $N(\tilde\Pi)e_0$, which is central, so
$\tilde\Pi=N(\tilde\Pi)e_0$ is central and its vector part vanishes; writing $\tilde\Pi=\Pi_0e_0$ the
equation becomes $\Pi_0^{2}=\Pi_0$, whence $\Pi_0\in\{0,1\}$. $\square$

No material element is a projection, and no nontrivial element at all is one: the material composition
therefore supplies no resolution of the algebra against a reference. The check on $100$ random unit
elements with complex coefficients gives a least residual $\lvert\tilde Q\star\tilde Q-\tilde Q\rvert$ of
$0.494$, and the exact zeros are exactly the two trivial solutions; the scalar line confirms the same
reduction, with residuals $0$, $0$, $0.25$, $2$ and $\sqrt2$ at the scalars $0$, $1$, $\tfrac12$, $2$ and
$i$.

**Reading.** The material composition has no measurement in it. Composing material operations is not where
a quantum theory resolves a state; the algebra says so by having no projection beyond the two degenerate
ones.

## Where the Projections Are

The projections the framework uses are elements of the informational sector, and they are not idempotent
for $\star$ at all.

**Proposition (the informational projectors).** For every real unit vector $\hat{\boldsymbol\mu}$ the
element

$$
\tilde\Pi=\tfrac12\bigl(e_0+i\hat{\boldsymbol\mu}\bigr)
$$

satisfies $\tilde\Pi^{2}=\tilde\Pi$ for the ordinary product, $\tilde\Pi\tilde\Pi^{*}=\tilde\Pi$ for the
sesquilinear pairing, $\mathrm{Tr}\,\tilde\Pi=1$, and

$$
N(\tilde\Pi)=0 , \qquad \tilde\Pi\star\tilde\Pi=N(\tilde\Pi)e_0=0 .
$$

**Proof.** The first two are the standard projector identities for $\tfrac12(e_0+i\hat{\boldsymbol\mu})$
with $\hat{\boldsymbol\mu}^{2}=-e_0$; the trace is the definition, and the last is the square identity of
the companion article applied to $\tilde\Pi$, whose norm vanishes because
$N(\tilde\Pi)=\tfrac14(1-1)=0$. $\square$

The objects a quantum theory counts as pure states are therefore **null for the material composition**: the
composition sends them to zero rather than holding them fixed. That is the sharpest form of the contrast
between the two structures, and it is the subject of *The States the Indefinite Metric Cannot Normalise*, which owns the isotropy and its reading. The Bloch sphere of states, the trace-one
slice and the decoherence of a measurement are owned by *The Bloch Ball as the Trace-One Slice of the
Future Light Cone* and *Decoherence as Idempotent Projection*, and are cited here, not repeated.

**Reading.** **Composition and measurement are separated by the algebra.** The material multiplication
carries the interval and has no projection; the informational structure supplies all the projections there
are. The two jobs sit in different rows of the framework, and the idempotent count is the algebraic
statement of the separation.

## What Is Closed in the Material Composition

The composition does respect one internal split of the material sector, and the statement must be made
carefully, because the first form of it is false.

**Definition (the real–imaginary split).** Write $\mathbb{H}_{\mathbb{B}}$ for the real quaternion subspace
(spans of the basis with real coefficients) and $i\mathbb{H}_{\mathbb{B}}$ for its imaginary multiple. The
algebra is their direct sum, and each element splits as a real quaternion part plus an imaginary one.

**Proposition (the gradings).** $\mathbb{H}_{\mathbb{B}}\star\mathbb{H}_{\mathbb{B}}\subseteq\mathbb{H}_{\mathbb{B}}$
and $i\mathbb{H}_{\mathbb{B}}\star i\mathbb{H}_{\mathbb{B}}\subseteq\mathbb{H}_{\mathbb{B}}$, while
$\mathbb{H}_{\mathbb{B}}\star i\mathbb{H}_{\mathbb{B}}\subseteq i\mathbb{H}_{\mathbb{B}}$ and
$i\mathbb{H}_{\mathbb{B}}\star\mathbb{H}_{\mathbb{B}}\subseteq i\mathbb{H}_{\mathbb{B}}$.

So the real quaternion subspace is **closed** under the material composition: a real-valued material field
composes to a real-valued one, and a real value composed with an imaginary one stays imaginary. All four
inclusions were checked on $100$ real and imaginary samples.

**The correction.** It does not follow that the even part of the material sector is closed. The material
sector meets the real quaternion subspace in the three-dimensional **spatial** part
$\mathbb{R}e_1+\mathbb{R}e_2+\mathbb{R}e_3$ — the unit $e_0$ is Hermitian and therefore not material — and
that part is **not** closed: $e_1\star e_1=e_0$ leaves it for the central line. So a composition of two
purely spatial material operations is not spatial; it picks up a central, informational part. The subspace
that is genuinely closed is the full real quaternion space, which contains the unit and is **not** contained
in the material sector. A reading of the split as "the spatial part is self-contained" is therefore wrong
as it stands, and the correct statement is the one above.

**Cautions.** The imaginary half is not closed, since a product of two imaginary elements is real. And the
restricted product on $\mathbb{H}_{\mathbb{B}}$ is not the quaternion product: it is the conjugation-inserted
product, which is non-associative, the triple of units $(e_1,e_1,e_2)$ a witness, since
$(e_1\star e_1)\star e_2=e_2$ against $e_1\star(e_1\star e_2)=-e_2$ (*verified*).

**Reading.** The real–imaginary split is an **internal superselection structure** of the material sector: a
real-valued excitation and an imaginary-valued one are distinguished by the composition, which never mixes
them, though it may carry a real pair to the central line. This is **not** the two-sector
material/informational split of *The Material-Informational Split as a Superselection Structure in
Biquaternionic Form*; that split is by the Hermitian conjugation and separates material from informational,
while this one is by the coefficientwise conjugation and is internal to each sector. The two structures
cross and must not be conflated.

## The Reading: Composition Is Not Measurement

**Proposed reading, labelled as such.** The material composition is **oriented and mute**.

- **The slots are not interchangeable.** The first factor is read through the conjugation, the second is
  not, and the identity acts as the identity from one side only. Composing an interval-one operation on the
  left of an element returns the element; using the identity on the right returns the conjugate.
- **The composite is a number plus a direction.** The order-independent half of a material composite is a
  central number, the pairing of the two operations; the order-dependent half is a direction, with a real
  and an imaginary part.
- **The composition cannot measure.** Its only projections are $0$ and $e_0$; a measurement is supplied by
  the informational structure, whose projectors are null for the composition.
- **Composition and measurement are done by different structures.** The material row carries the interval
  and the composition; the informational row carries the projection and the measurement.

## The Limits

**The orientation is not a time order.** The algebra proves the one-sided identity and the
anti-isomorphism of the left multiplications. It does not prove that the orientation is a
before-and-after order: the product does not say which slot is earlier, and an arrow of time is not an
algebraic datum. Reading the orientation as causal or temporal is a proposal, labelled as one; what would
support it is a physical composition law that singles out a slot, and the framework does not yet have one.

**No material projection of another structure.** The idempotent count is a statement about $\star$ and
nothing else. It says nothing against the ordinary idempotents of the material sector, which are a
different theorem, nor against idempotent **maps** or channels, which are operations on a state space and
not elements of the algebra; that distinction is drawn in *Decoherence as Idempotent Projection*.

**A chain has no intrinsic value.** Because the product is not associative, a word of three material
operations has no bracketing-free value. Whether physical composition supplies a natural bracketing is
recorded as an open question and not resolved.

## The Ledger

**Proved.** $e_0\star\tilde Q=\tilde Q$ and $\tilde Q\star e_0=\tilde Q^{\natural}$, hence a left identity
and no right one; the non-commutativity; the rule $L_{\tilde A}\circ L_{\tilde B}=L_{\tilde B\tilde A}$,
so that the operations compose associatively though the elements do not. The split of a composite into a
central half and a vector half, with the central half the order-independent part. The idempotents of
$\star$ are exactly $0$ and $e_0$. The informational projectors
$\tfrac12(e_0+i\hat{\boldsymbol\mu})$ are idempotent for the ordinary and the sesquilinear products, have
$N=0$, and are **null** for $\star$. The four inclusions of the real–imaginary split, and the non-closure
of the spatial part of the material sector, with the witness $e_1\star e_1=e_0$.

**Readings.** That the material composition is oriented, the first slot read through the interval and the
second as it stands; that the composite is a number plus a direction; that the composition supplies no
measurement; that measurement and composition are done by different structures of the framework; that the
real–imaginary split is an internal superselection structure, distinct from the material/informational one.

**Not claimed.** That the orientation is a time or causal order; that no material projection of some other
structure is possible; that the trivial idempotents carry physical processes; that a chain of three
operations has a natural bracketing.

## Summary

The material composition $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q$ is **oriented**: its first
slot is read through the natural conjugation and its second is not, the identity acts as the identity only
from the left, $\tilde Q\star e_0=\tilde Q^{\natural}\neq\tilde Q$, so there is no right identity, and the
order matters with commutator $2P_0\mathbf Q-2Q_0\mathbf P-2\mathbf P\times\mathbf Q$. The operations
themselves still compose associatively, $L_{\tilde A}\circ L_{\tilde B}=L_{\tilde B\tilde A}$, so a chain
of material operations is a well-defined map even though a chain of the corresponding elements is not. The
composition **cannot measure**: its only idempotents are $0$ and $e_0$, since a projection must be central
and satisfy $Q_0^{2}=Q_0$, so the material multiplication resolves no state against a reference. Every
composite of two material operations splits into a central number — the order-independent pairing — and a
direction; on the material sector the square is a number, so the sector is not closed, the witness being
$e_1\star e_1=e_0$. The projections the framework uses belong to the informational sector, where
$\tilde\Pi=\tfrac12(e_0+i\hat{\boldsymbol\mu})$ is idempotent for the ordinary and the sesquilinear products
and is **null** for the material composition. The material composition therefore respects one internal
split — the real quaternion subspace is closed, and a real value composes to a real value — but the even
part of the material sector is not closed, since a product of two spatial elements may land on the unit.
The reading is that the material composition carries the interval and the informational structure carries
the measurement, and that the two jobs are separated by the algebra. The orientation is not proved to be a
time order; the states and their isotropy are owned by *The States the Indefinite Metric Cannot Normalise*, the decoherence
of a measurement by *Decoherence as Idempotent Projection*, the non-associativity and the ternary product
by *The Associator and the Ternary Product of the Quaternionic Product*, and the left multiplications and
their monoid by *The Left Multiplications of the Quaternionic Product and the Opposite Monoid*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q$ | the quaternionic product |
| $\tilde Q^{\natural}$ | the natural conjugation; the operation inserted in the first slot |
| $e_0$; $0$ | the two idempotents of $\star$; the left identity and the zero element |
| $L_{\tilde A}$ | the left multiplication $\tilde X\mapsto\tilde A\star\tilde X$ |
| $2P_0\mathbf Q-2Q_0\mathbf P-2\mathbf P\times\mathbf Q$ | the commutator of $\star$ |
| $P_0Q_0+(\mathbf P,\mathbf Q)$ | the central, order-independent half of a composite |
| $\tilde\Pi=\tfrac12(e_0+i\hat{\boldsymbol\mu})$ | the informational projector; null for $\star$ |
| $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$ | the real quaternion subspace and its imaginary multiple |
| $\mathbb{R}e_1+\mathbb{R}e_2+\mathbb{R}e_3$ | the spatial part of the material sector; not closed under $\star$ |
| $\mathbb{M}_\pm$ | the material and informational sectors |

## Further Reading

- *The Mathematical Study of Biquaternions*, the physics entry point to the mathematical study under
  which this block sits.
- Companion article *The Interval as the Square and the Charge of the Material Composition*, for the square
  identity, the interval and the multiplicativity used throughout.
- Mathematics article *The Left Multiplications of the Quaternionic Product and the Opposite Monoid*
  (`articles_maths/the-left-multiplications-of-the-quaternionic-product-and-the-opposite-monoid.md`), for
  the left multiplications and their anti-isomorphism.
- Mathematics article *Idempotents of the Quaternionic Product*
  (`articles_maths/idempotents-of-the-quaternionic-product.md`), for the idempotent reduction.
- Mathematics article *The Associator and the Ternary Product of the Quaternionic Product*
  (`articles_maths/the-associator-and-the-ternary-product-of-the-quaternionic-product.md`), for the
  associator and the failure of the weaker identities.
- Mathematics article *Introduction to the General Quaternionic Algebra of Biquaternions*
  (`articles_maths/introduction-to-the-general-quaternionic-algebra-of-biquaternions.md`), for the product and its table.
- Mathematics article *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*
  (`articles_maths/two-sided-operators-on-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the
  two-sided operators of the sandwich and their Hermitian adjoints.
- Companion article *The States the Indefinite Metric Cannot Normalise* and
  *Decoherence as Idempotent Projection*, for the states and for the measurement.
- Companion article *The Material-Informational Split as a Superselection Structure in Biquaternionic
  Form*, for the two-sector split by the Hermitian conjugation.
- Companion article *Relations Between Subspaces*, for the six subspaces and the real–imaginary split.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the one-sided units and the
  non-associativity of the conjugating products on a quaternion algebra.
