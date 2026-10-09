# __Observables as a Jordan Algebra: the Symmetric Plain Product and the Classical Composition__

## Introduction

The Hermitian subspace $\mathbb{M}_+$ is the sector of the observables of the frame, and it carries a
product of its own. Under the symmetrised plain product
$\tilde P\bullet\tilde Q=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ the sector is **closed**: the
symmetrised product of two Hermitian elements is Hermitian. The observables therefore form a commutative
unital algebra with a product defined on them and not merely imported from the full algebra, and the
product satisfies the Jordan identity. That is the algebraic content of the article.

Three readings follow, and each is offered and labelled as a reading rather than proved. The first is
that the symmetrised product is the **classical composition** of two observables, the composition on
which the order does not act; the order-bearing part of the ordinary product leaves the sector altogether
and becomes a generator, in the companion band $\mathrm{APA}$. The second is that the observables are a
**Jordan algebra** in the precise sense: a commutative algebra whose product satisfies the Jordan identity
in place of associativity. The third is that the **trace form** of the operation is invariant, and that
its invariance is the algebraic expression of the fact that the composition has no orientation, the two
slots being indistinguishable.

The algebraic facts are the closure, the Jordan identity, the positive definiteness of the trace form on
the sector and its invariance. The mathematics is *The Symmetric and Antisymmetric Parts of an Algebra
Product* for the splitting, *Introduction to the Symmetric Plain Algebra of Biquaternions* for the
operation, *The Trace Form and the Invariance of the Symmetric Plain Algebra* for the form, and *The Six
Subspaces under the Symmetric Plain Algebra of Biquaternions* for the sector structure. The Jordan
algebra itself is *Jordan Algebras*, and its special class is *Special and Exceptional Jordan Algebras*.

The conventions are those of the companion article. The algebra is
$\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_1e_2=e_3$,
$e_k^{2}=-e_0$, central scalar imaginary $i$, and general element $\tilde Q=Q_0e_0+\mathbf{Q}$. The
material sector is the anti-Hermitian subspace $\mathbb{M}_-$ and the informational sector the Hermitian
subspace $\mathbb{M}_+$, both real and four-dimensional;
$\mathrm{Sc}(\tilde Q)=Q_0$ is the scalar part and ${}^{*}$ is the Hermitian conjugation.

## The Hermitian Sector Is Closed under the Symmetrised Product

**Proposition.** For $\tilde P,\tilde Q\in\mathbb{M}_+$ the symmetrised plain product is Hermitian, so
$\mathbb{M}_+$ is **closed** under $\bullet$.

*Proof.* Hermitian means fixed by ${}^{*}$. Since the star is an anti-automorphism,
$(\tilde P\tilde Q)^{*}=\tilde Q^{*}\tilde P^{*}=\tilde Q\tilde P$, so the symmetric part is fixed,

$$
(\tilde P\bullet\tilde Q)^{*}=\tfrac12\bigl((\tilde P\tilde Q)^{*}+(\tilde Q\tilde P)^{*}\bigr)
=\tfrac12\bigl(\tilde Q\tilde P+\tilde P\tilde Q\bigr)=\tilde P\bullet\tilde Q .
$$

The result holds for every pair, and the operation restricted to the sector is an operation **of** the
sector. Verified on $100$ random pairs. This is the closure cell of *The Six Subspaces under the Symmetric
Plain Algebra of Biquaternions*.

**Proposition.** The material sector $\mathbb{M}_-$ is **not** closed under the symmetrised plain product,
and the informational sector is not closed under the antisymmetric plain product.

*Proof.* On two anti-Hermitian elements the symmetrised product is the Hermitian anticommutator, by the
companion article; the witness is $ie_0\bullet ie_0=(ie_0)^{2}=-e_0\in\mathbb{M}_+$. On two Hermitian
elements the antisymmetric product is the anti-Hermitian commutator, and the witness is
$ie_1\wedge ie_2=\tfrac12[ie_1,ie_2]=(ie_1)\times(ie_2)=-e_3\in\mathbb{M}_-$. Both verified on the basis.

The two propositions place the two bands of the split. **The symmetric half closes the informational
sector and the antisymmetric half closes the material sector**: the symmetric product is the one the
observables admit, and the antisymmetric product is the one the generators admit. A product such as the
ordinary one closes neither.

## The Observables of the Frame

An **observable** of the frame is a Hermitian element, $\tilde Q\in\mathbb{M}_+$, and a **state** is a
Hermitian positive element of trace one; the dictionary is that of *The Hermitian Subspace $\mathbb{M}_+$
as the Informational Sector*. The first consequence of the closure is that two observables compose:

**Proposition.** The symmetrised product of two observables is an observable. The ordinary product is not:
it has one Hermitian and one anti-Hermitian part, and only the Hermitian part stays in the sector.

*Proof.* The closure is the first proposition. For the ordinary product take the Hermitian pair
$\tilde P=ie_1$, $\tilde Q=ie_2$: then
$\tilde P\tilde Q=(ie_1)(ie_2)=-e_1e_2=-e_3$, which is anti-Hermitian and not an observable, while the
two parts of the split read $\tilde P\bullet\tilde Q=\tfrac12(-e_3+e_3)=0$ and
$\tilde P\wedge\tilde Q=\tfrac12(-e_3-e_3)=-e_3$. So the ordinary product of two observables need not be
an observable, and the antisymmetric part is where it leaves the sector. Verified on the basis.

The observables therefore form a commutative unital algebra over $\mathbb{R}$ of real dimension four,
with the unit $e_0$, and it satisfies the Jordan identity because the ambient operation does. The algebra
is **special**, being the symmetrisation of the associative algebra $\mathbb{B}$ restricted to
$\mathbb{M}_+$; the special class is *Special and Exceptional Jordan Algebras*.

**Remark (the observables are not a subalgebra of the ordinary product).** The closure is a statement
about $\bullet$ and not about the ordinary product: $\mathbb{M}_+$ is closed under the order-free
composition and under nothing else. The ordinary product of two observables leaves the sector, which is
the asymmetry that makes the sector "the states" under one product and "the generators" under another.

## The Square of an Observable and Its Positivity

**Proposition.** The square in the block is the ordinary square, $\tilde Q\bullet\tilde Q=\tilde Q^{2}$,
so the square of an observable is an observable; and the square is the **diagonal** of the operation, in
the sense that the polarisation

$$
\tilde P\bullet\tilde Q=\tfrac12\bigl((\tilde P+\tilde Q)^{2}-\tilde P^{2}-\tilde Q^{2}\bigr)
$$

recovers the product from the square alone.

*Proof.* The antisymmetric part vanishes on the diagonal because it is alternating, so the block's square
is the ordinary square, as in the companion article; the polarisation is the polarisation identity of a
commutative bilinear operation and was recomputed on random pairs. The square and the polarisation are
*The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*.

**Proposition.** The square of an observable is a **positive** observable. In coordinates, for
$\tilde Q=h_0e_0+i\mathbf{h}$ with $h_0$ and $\mathbf{h}$ real,

$$
\tilde Q^{2}=\bigl(h_0^{2}+(\mathbf{h},\mathbf{h})\bigr)e_0+2h_0\,i\mathbf{h},
$$

and the positivity condition $h_0^{2}+(\mathbf{h},\mathbf{h})\geq\lvert 2h_0\rvert\,\lvert\mathbf{h}\rvert$
is the identity $(h_0^{2}-(\mathbf{h},\mathbf{h}))^{2}\geq0$.

*Proof.* The spectral form of a Hermitian element is
$\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-$ with $\lambda_\pm=h_0\pm\lvert\mathbf{h}\rvert$ real
and $\tilde\Pi_\pm$ orthogonal idempotents of *The Hermitian Subspace $\mathbb{M}_+$ as the Informational
Sector*; squaring gives $\tilde Q^{2}=\lambda_+^{2}\tilde\Pi_++\lambda_-^{2}\tilde\Pi_-$, a combination of
the same idempotents with non-negative coefficients, hence positive. The coordinate display and the
inequality were recomputed.

Two facts follow, and they are the reason the observables form a Jordan algebra of the strongest kind.
First, the square of every observable is positive, so no observable squares to a negative one. Second,
the positive cone is closed under addition, so a sum of squares vanishes only when every term does:

**Corollary.** The Jordan algebra of observables is **formally real**: $Q_1^{2}+\cdots+Q_n^{2}=0$ implies
$Q_1=\cdots=Q_n=0$.

*Proof.* Each $Q_i^{2}$ is positive by the proposition, and the sum of positive elements is positive
because the cone $\{h_0\geq\lvert\mathbf{h}\rvert\}$ is convex. Apply the trace form to the sum against
the unit: with $\tilde Q_i=h_{0,i}e_0+i\mathbf{h}_i$ one has
$\tau(\tilde Q_i^{2},e_0)=h_{0,i}^{2}+(\mathbf{h}_i,\mathbf{h}_i)\geq0$ and
$\tau(\sum_i\tilde Q_i^{2},e_0)=\sum_i\bigl(h_{0,i}^{2}+(\mathbf{h}_i,\mathbf{h}_i)\bigr)$; if the sum
vanishes then this trace vanishes, and the vanishing of a sum of non-negative terms forces every
$h_{0,i}=\mathbf{h}_i=0$. The cone and the positive definiteness of the trace form are
*The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* and the section above.

**Remark (the square does not order the sector by the norm).** Positivity of the square is a statement
about the **spectrum**, and it is not the sign of the biquaternion norm: a Hermitian element has
$N(\tilde Q)=h_0^{2}-(\mathbf{h},\mathbf{h})$, which is indefinite, and an element of the positive cone
can have negative norm. The two are kept apart wherever they appear; the norm is *Biquaternion Norm and
Invertibility*.

## The Trace Form and the Invariance

**Definition.** The **trace form** of the block is the scalar part of the symmetrised product,

$$
\tau(\tilde P,\tilde Q)=\mathrm{Sc}\bigl(\tilde P\bullet\tilde Q\bigr)
=\mathrm{Sc}\bigl(\tilde P\tilde Q\bigr)=P_0Q_0-(\mathbf{P},\mathbf{Q}).
$$

It is $\mathbb{C}$-bilinear, symmetric and non-degenerate on $\mathbb{B}$, and on the informational sector
it is **positive definite**. This is the trace form of *The Trace Form and the Invariance of the Symmetric
Plain Algebra*, and it is the same form as the general plain bilinear form $B$ of *The Ordinary Product
and the Material Sector*, read here as the form of the operation.

**Proposition (invariance).** The trace form is **invariant**:

$$
\tau(\tilde P\bullet\tilde Q,\tilde R)=\tau(\tilde P,\tilde Q\bullet\tilde R)
\qquad\text{for all } \tilde P,\tilde Q,\tilde R .
$$

*Proof.* Expanding the symmetrised product in one slot, the left side is
$\tfrac12\bigl(\mathrm{Sc}(\tilde P\tilde Q\tilde R)+\mathrm{Sc}(\tilde Q\tilde P\tilde R)\bigr)$ and
the right side $\tfrac12\bigl(\mathrm{Sc}(\tilde P\tilde Q\tilde R)+\mathrm{Sc}(\tilde P\tilde R\tilde Q)\bigr)$.
The first terms agree, and the second terms agree because the scalar part of the ordinary product is
invariant under a cyclic permutation,
$\mathrm{Sc}(\tilde Q\tilde P\tilde R)=\mathrm{Sc}(\tilde P\tilde R\tilde Q)$. Verified on $100$ random
triples, max deviation $0$. The invariance is *The Trace Form and the Invariance of the Symmetric Plain
Algebra*.

**Proposition (positivity on the observables).** On $\mathbb{M}_+$ the trace form is real and strictly
positive on non-zero elements, $\tau(\tilde Q,\tilde Q)=h_0^{2}+(\mathbf{h},\mathbf{h})>0$ for
$\tilde Q=h_0e_0+i\mathbf{h}\neq0$, and it **coincides with the Hermitian form**
$\mathrm{Sc}(\tilde P\tilde Q^{*})$, the Born pairing of the frame.

*Proof.* For $\tilde Q$ Hermitian, $\tilde Q^{*}=\tilde Q$, so
$\tau(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q^{*})$; the diagonal
is the sum of the squares of the four real coordinates $h_0,\mathbf{h}$. Verified on $100$ random pairs.
The Born pairing and the Hilbert–Schmidt reading are *The Hermitian Subspace $\mathbb{M}_+$ as the
Informational Sector*.

**Proposed reading, labelled as such.** The invariance is read as the **absence of an orientation**.
Because the product is commutative, the left and the right multiplication of the block are the same
operation, and the invariance is the single identity that a symmetric bilinear form can satisfy with
respect to it. There is no "left product" and no "right product" to distinguish, hence no orientation that
the form could detect; a non-commutative product would have two distinct invariance identities and the
asymmetry would be visible. What the algebra proves is the invariance; the word "orientation" is the
reading.

The identity of the two forms on the observables is the reason the block is compatible with the
probability structure of the frame: the classical composition and the Born pairing share their form on
the observables. That coincidence is a statement about $\mathbb{M}_+$ alone; on $\mathbb{M}_-$ the two
differ by sign, and the comparison is *The Four General Products and Their Physical Readings: the Two Algebras and
the Two Sesqualgebras*.

## The Classical Composition

**Proposed reading, labelled as such.** The symmetrised plain product on the observables is the
**classical composition**: the composition of two observables that does not depend on their order. The
ordinary product of two observables splits into the order-free composition and the order-bearing part,

$$
\tilde P\tilde Q=\underbrace{\tilde P\bullet\tilde Q}_{\text{observable}}+\underbrace{\tilde
P\wedge\tilde Q}_{\text{generator}},
\qquad \tilde P,\tilde Q\in\mathbb{M}_+,
$$

and the second term is anti-Hermitian, an element of $\mathbb{M}_-$ and not an observable. The two bands
of the plain family therefore read as the two faces of one composition: the symmetric band is the face on
which the order does not act, the antisymmetric band the face that carries it.

The reason this is the reading of *classical* is the pair of frames the corpus already holds. The
observables are the Hermitian elements; the states are the positive ones; and the composition on which
the order acts is measured by the commutator, which lives in the generator sector. In the ordinary
quantum formalism the commutator is what makes two observables incompatible, and the anticommutator is
what an order-free product retains. The symmetrised product is exactly the anticommutator half of the
biquaternion composition, so the block names the order-free composition, and it does not name a dynamics.
The Jordan programme, in which the observables of a quantum system are read from the symmetrised product
alone, is *Jordan Algebras*; its origin and the classification of its formally real members are the paper
of Jordan, von Neumann and Wigner.

**Bound, with the mathematics.** The splitting of a bilinear operation into its symmetric and
antisymmetric parts is *The Symmetric and Antisymmetric Parts of an Algebra Product*, and the
corresponding splitting for a sesquilinear operation, which is the one the sesquilinear block uses, is *The
Symmetric and Antisymmetric Parts of a Sesqualgebra Product*. The two are different splittings and must
not be conflated: the bilinear splitting of this block pairs with the plain product, and the sesquilinear
one with the sesquilinear product. The Jordan algebras of a sesqualgebra, where the fixed ring replaces
the base field, are *Jordan Algebras of Sesqualgebras*; the present algebra is the bilinear one and is
over $\mathbb{R}$ on the observables. The invariance of the form is *The Trace Form and the Invariance of
the Symmetric Plain Algebra*, and its positivity as a form is *Positivity and the Hermitian Cone of the
Biquaternion Algebra with Hermitian Adjoint*.

**Proposed reading, speculative and labelled as such.** The symmetric half pairs an observable with
itself and returns a positive observable; the antisymmetric half vanishes on the diagonal, so an
observable is never incompatible with itself. Offered as a speculation, the symmetric half is the
**Bose-like** composition — joint knowability, a symmetric pairing — and the antisymmetric half the
**Fermi-like** one — no self-pairing, alternation. *Not claimed:* that the framework derives the
spin–statistics theorem; the statistics are owned by *Anyons and Braid Statistics in Biquaternionic
Form*.

## The Bound

**What the section does not claim.** The classical composition is a reading. It does not say that the
observables behave classically, that a measurement destroys the order, or that the frame is a classical
system. The algebra proves that the symmetrised product closes the observables and satisfies the Jordan
identity; the words "classical composition" are the framework's name for the order-free product, offered
and labelled.

Three further limits are worth stating. The observables of this article are the Hermitian elements of the
algebra; their reading as operators on the spinor module, and their spectrum as a two-state system, are
*The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* and *Quantum Physics in
Biquaternionic Form*, and are not carried here. The square of an observable is positive, but the Jordan
algebra carries no dynamics: the square is not an evolution and the trace form is not a Hamiltonian. And
the coincidence of the trace form with the Born pairing holds on $\mathbb{M}_+$ alone; off the sector the
two forms differ.

## The Ledger

**Proved.** The Hermitian sector is closed under the symmetrised plain product and the material sector is
not, while the antisymmetric product closes the material sector and not the informational one; the
square of an observable is the ordinary square and is a positive observable, with the polarisation
recovering the product from the square; the observables form a commutative unital **special Jordan
algebra** over $\mathbb{R}$ of real dimension four, and it is formally real; the trace form
$\tau(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\bullet\tilde Q)=P_0Q_0-(\mathbf{P},\mathbf{Q})$ is
symmetric, non-degenerate, invariant,
$\tau(\tilde P\bullet\tilde Q,\tilde R)=\tau(\tilde P,\tilde Q\bullet\tilde R)$, positive definite on
$\mathbb{M}_+$, and equal there to the Hermitian form $\mathrm{Sc}(\tilde P\tilde Q^{*})$.

**Readings.** That the symmetrised product is the **classical composition** of two observables, the
composition on which the order does not act; that the observables are a **Jordan algebra**; and that the
invariance of the trace form is the **absence of an orientation**; and, speculatively, that the two
halves of the composition are the two statistics. Each is the framework's naming of a proved algebraic
fact and is labelled as such.

**Not claimed.** That the observables compose classically in a physical sense; that the trace form is the
metric, the interval or a Hamiltonian; that the coincidence with the Born pairing extends off
$\mathbb{M}_+$; that the Jordan identity concerns measurement.

## Summary

The symmetrised plain product
$\tilde P\bullet\tilde Q=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ closes the Hermitian sector: the
product of two observables is an observable, whereas the ordinary product splits into an observable part
and a generator part. The observables form a commutative unital **special Jordan algebra** over
$\mathbb{R}$ of real dimension four, with the unit $e_0$, the Jordan identity in place of associativity,
and the square as the diagonal of the operation. The square of an observable is a positive observable,
and the algebra is formally real. Its trace form
$\tau(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\bullet\tilde Q)=P_0Q_0-(\mathbf{P},\mathbf{Q})$ is
symmetric, invariant, positive definite on $\mathbb{M}_+$, and equal there to the Hermitian Born pairing
$\mathrm{Sc}(\tilde P\tilde Q^{*})$. The readings offered and labelled here are that the symmetrised
product is the **classical composition** of two observables, that the observables are a **Jordan
algebra**, and that the invariance of the form is the **absence of an orientation**; the algebraic facts
are the closure, the positivity and the invariance, and none of the three readings is proved.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\bullet\tilde Q=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ | Symmetrised plain product, the operation of the block |
| $\mathbb{M}_+$ | Hermitian (informational) subspace; the observables |
| $\mathbb{M}_-$ | Anti-Hermitian (material) subspace; the generators |
| $\tilde P\tilde Q=\tilde P\bullet\tilde Q+\tilde P\wedge\tilde Q$ | Observables split into observable part and generator part |
| $\tilde Q^{2}$ | Square, equal to the ordinary square; the diagonal of the operation |
| $(\tilde P+\tilde Q)^{2}-\tilde P^{2}-\tilde Q^{2}=2\tilde P\bullet\tilde Q$ | Polarisation of the square |
| $\tau(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\bullet\tilde Q)=P_0Q_0-(\mathbf{P},\mathbf{Q})$ | Trace form of the block |
| $\tau(\tilde P\bullet\tilde Q,\tilde R)=\tau(\tilde P,\tilde Q\bullet\tilde R)$ | Invariance, the trace identity |
| $\mathrm{Sc}(\tilde P\tilde Q^{*})$ | The Hermitian (Born) form, equal to $\tau$ on $\mathbb{M}_+$ |
| $(p,q)$ | Signature written as (number of $+$, number of $-$) |

## Further Reading

- Pascual Jordan, John von Neumann and Eugene Wigner, "On an Algebraic Generalization of the Quantum
  Mechanical Formalism" (1934), for the Jordan programme and the classification of the formally real
  Jordan algebras.
- Mathematics article *The Symmetric and Antisymmetric Parts of an Algebra Product*, for the bilinear
  splitting, and *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*, for the sesquilinear
  one.
- Mathematics article *The Trace Form and the Invariance of the Symmetric Plain Algebra*, for the form,
  its symmetry, its non-degeneracy and its invariance.
- Mathematics article *The Six Subspaces under the Symmetric Plain Algebra of Biquaternions*, for the
  closure of the sector and the failure of closure of the others.
- Mathematics article *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain
  Algebra*, for the square, the polarisation and the Jordan inverse.
- Mathematics article *Jordan Algebras*, *Special and Exceptional Jordan Algebras* and *Jordan Algebras
  of Sesqualgebras*, for the Jordan identity, the special class and the sesquilinear counterpart.
- Companion article *The Symmetrised Material Composition and the Jordan Identity*, for the operation and
  its reading on the material sector.
- Companion article *The Cross Product as a Lie Bracket: Rotations and the Jacobi Identity*, for the
  antisymmetric half and its reading on the generators.
- Companion article *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, for the
  observables, the states, the cone and the Born pairing.
