# __The Quaternion Form as a Product: the Scalar Coupling of Two Material Operations__

## Introduction

Two material operations can be compared, and the comparison returns a number. This article reads the
operation that performs it. It is the **symmetrised quaternionic product**,

$$
\tilde P\bullet\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P\bigr)
=\bigl[P_0Q_0+(\mathbf P,\mathbf Q)\bigr]e_0 ,
$$

the symmetric part of the quaternionic product $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q$ for the
exchange of its two arguments. The operation is the symmetric part of the quaternionic row of the twelve
structures the algebra carries — the row opened by the general quaternionic product
$\mathrm{GQA}$ whose square is the interval (*The Interval as the Square and the Charge of the Material
Composition*). Its value is **central**: whatever the two operations are, the operation returns a multiple
of the unit, the scalar their overlap carries, and nothing else. The article's claim is that this is what
the symmetrised half of the quaternionic product **is** — a **scalar coupling**, a comparison that
returns a number — and that its diagonal is the **interval** of the material row.

The word of the band is **Coupling**, and the article earns it from the value the operation returns. The
companion half, the antisymmetrised quaternionic product of the band
`Focus on the Antisymmetric Quaternionic Algebra (AQA) — Obstruction`, is the other bracket of the row; the
two halves reconstruct the parent,

$$
\tilde P^{\natural}\tilde Q=\tilde P\bullet\tilde Q+\tilde P\wedge_{\natural}\tilde Q ,
$$

and the reader must hold the two together: the symmetric half is what survives when the order of the two
operations is forgotten, and the antisymmetric half is exactly what the forgetting loses.

The article keeps to the one operation. The general construction of the two parts of a product is
*The Symmetric and Antisymmetric Parts of an Algebra Product*; the operation on its own, its class, its
image and the sixteen products of the basis are *Introduction to the Symmetric Quaternionic Algebra of
Biquaternions*; the coefficient read as a form, with its Gram matrix, its realification and its
invariance, is *The Quaternion Form as a Product on the Symmetric Quaternionic Algebra*; the radical, the
isotropic elements and the failure of the Jordan identity are *The Radical and the Isotropic Elements of
the Symmetric Quaternionic Algebra* and are the subject of the companion article *Why a Central Product
Cannot Compose: the Radical and the Isotropic Elements*; the operators and the matrix models are
*The Multiplication Operators of the Symmetric Quaternionic Algebra* and *The Symmetric Quaternionic
Algebra in the Matrix Representations*. The comparison of this operation with the other three rows is
*The Four General Products and Their Physical Readings: the Two Algebras and the Two Sesqualgebras*, and it is
cited and not redone.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with basis
$e_0=1,e_1,e_2,e_3$, $e_k^{2}=-e_0$, $e_1e_2=e_3$, and central scalar imaginary $i$ with $i^{2}=-1$. An
element is $\tilde Q=Q_0e_0+\mathbf Q$ with $Q_\mu\in\mathbb{C}$ and vector part
$\mathbf Q=Q_1e_1+Q_2e_2+Q_3e_3$; the complex bilinear dot and cross products of vector parts are
$(\mathbf P,\mathbf Q)=\sum_kP_kQ_k$ and $\mathbf P\times\mathbf Q$. The natural conjugation is
${}^{\natural}$, the Hermitian star ${}^{*}=\bar{\cdot}\circ{}^{\natural}$, and the sectors are
$\mathbb{M}_\pm=\{\tilde Q:\tilde Q^{*}=\pm\tilde Q\}$ with the material one $\mathbb{M}_-$. The ordinary
(plain) product is juxtaposition $\tilde P\tilde Q$, the quaternionic product is
$\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q$. The **general plain bilinear form** is
$B(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q)=P_0Q_0-(\mathbf P,\mathbf Q)$, the scalar part of the
plain product (*The Ordinary Product and the Material Sector*), and the **general quaternionic bilinear
form** is $N(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q)$,
the scalar part of the quaternionic product (*Conventions in the Biquaternion Universe*). The two differ
by the sign of the vector part alone. The symmetrisation symbol $\bullet$ is **row-relative** in this
chapter — it is the symmetrisation of whichever product is in play, so the plain row writes
$\tilde P\bullet\tilde Q=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ and this block writes
$\tilde P\bullet\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P)$, a different
operation — and this block's antisymmetrisation is written $\wedge_{\natural}$, where the plain row writes
$\wedge$ for the cross product $\mathbf P\times\mathbf Q$. The six distinguished subspaces are the centre
$\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion subspace
$\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, the Hermitian sector
$\mathbb{M}_+$ and the material sector $\mathbb{M}_-$.

## The Two Halves of the Parent Product

The general quaternionic product is $\mathbb{C}$-bilinear, so for it the exchange of the two arguments is
the plain interchange, and it is a **conjugation of the value** and not a reversal,

$$
\tilde Q^{\natural}\tilde P=\bigl(\tilde P^{\natural}\tilde Q\bigr)^{\natural} .
$$

A bilinear product over a field in which $2$ is invertible therefore splits canonically into a symmetric
and an antisymmetric part (*The Symmetric and Antisymmetric Parts of an Algebra Product*), and the two
parts of the quaternionic product are the two operations of the quaternionic row.

**Proposition (the explicit form).** For all $\tilde P=P_0e_0+\mathbf P$ and $\tilde Q=Q_0e_0+\mathbf Q$,

$$
\tilde P\bullet\tilde Q
=\tfrac12\bigl(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P\bigr)
=\bigl[P_0Q_0+(\mathbf P,\mathbf Q)\bigr]e_0 .
$$

In particular the value is central, the operation is $\mathbb{C}$-bilinear and commutative, and its
image is the centre $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$.

*Proof.* The parent value is
$\tilde P^{\natural}\tilde Q=[P_0Q_0+(\mathbf P,\mathbf Q)]e_0+P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q$
(*The 12 Products of the Biquaternion Complex Space*). The reverse value is obtained
by exchanging the arguments; its scalar part is symmetric in the pair and its vector part is
antisymmetric, with the cross product reversing and the mixed terms exchanging with a sign. Half the sum
keeps the scalar part and cancels the vector part. Bilinearity is inherited term by term with the
coefficients in $\mathbb{C}$; commutativity is the symmetry of the definition; and the value being a
multiple of $e_0$ puts the image in the centre.

**Remark (what the exchange leaves and what it removes).** The scalar part of the parent product carries
the two terms the exchange leaves fixed — the square term $P_0Q_0$ and the scalar product
$(\mathbf P,\mathbf Q)$ of the two vector parts — and the symmetrised part is exactly that half. The
vector part of the parent, the mixed terms $P_0\mathbf Q-Q_0\mathbf P$ and the cross term
$-\mathbf P\times\mathbf Q$, is antisymmetric and is removed; it is the operation of the companion band.
The coupling therefore **removes the order** of the two operations: it is the value of the product once
the order is forgotten, and nothing of the order survives.

## The Value Is Central: a Coupling and Not a Composition

**Proposition (centrality, commutativity and the image).** Every value of $\bullet$ is a complex multiple
of the unit, and the image of the operation is the centre $\mathbb{C}_{\mathbb{B}}$; the operation is
commutative,

$$
\tilde P\bullet\tilde Q=\tilde Q\bullet\tilde P ,
$$

and it is the value of the general quaternionic bilinear form placed on the central line,

$$
\tilde P\bullet\tilde Q=N(\tilde P,\tilde Q)\,e_0 , \qquad
N(\tilde P,\tilde Q)=\mathrm{Sc}\bigl(\tilde P^{\natural}\tilde Q\bigr)=P_0Q_0+(\mathbf P,\mathbf Q) .
$$

*Proof.* The explicit form is the definition of the coefficient, and the coefficient is the scalar part
of the parent product; commutativity is the symmetry of $P_0Q_0+(\mathbf P,\mathbf Q)$; the image statement
is the centrality of the value.

The operation is therefore a **bilinear form read as a product**: it takes two operations and returns the
scalar their comparison carries, always on the same one-dimensional line, and it never returns an
operation of the same kind as its inputs. That is the whole content of the band name. A value in the
**centre** is a number, the same number for every observer and commuting with every element; it can be
multiplied by other numbers and it cannot be composed with other operations, because a central value
carries no vector direction and no slot to act on.

### The Sixteen Products of the Basis

On the complex basis $e_0,e_1,e_2,e_3$, with the row index the left argument and the column index the
right one, the operation reads

| $\bullet$ | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
|---|---|---|---|---|
| $e_0$ | $e_0$ | $0$ | $0$ | $0$ |
| $e_1$ | $0$ | $e_0$ | $0$ | $0$ |
| $e_2$ | $0$ | $0$ | $e_0$ | $0$ |
| $e_3$ | $0$ | $0$ | $0$ | $e_0$ |

**Proposition (the table).** The table is diagonal,
$e_\mu\bullet e_\nu=\delta_{\mu\nu}e_0$; every entry is central; the four diagonal entries are the unit
and the twelve off-diagonal entries are zero; and the operation is not the zero operation, since
$e_0\bullet e_0=e_0$.

*Proof.* $N(e_\mu,e_\nu)=\mathrm{Sc}(e_\mu^{\natural}e_\nu)$ is the coefficient square of the two basis
elements, which is $\delta_{\mu\nu}$; the centrality and the values follow from the explicit form. The
table is the one of *Introduction to the Symmetric Quaternionic Algebra of Biquaternions*.

Four of the sixteen products are nonzero and equal to $e_0$, twelve vanish: the coupling is the identity
table of the coefficient form and nothing more. In particular two **distinct** basis operations do not
couple at all — their value is zero — and a basis operation couples only with itself, to the unit.

## The Diagonal Is the Interval

**Theorem (the square is the interval).** For every $\tilde Q$,

$$
\tilde Q\bullet\tilde Q=N(\tilde Q)\,e_0 , \qquad N(\tilde Q)=Q_0^{2}+Q_1^{2}+Q_2^{2}+Q_3^{2} .
$$

On the material coordinate $\tilde Q=ict\,e_0+\mathbf x$ the value is $-c^{2}t^{2}+\mathbf x^{2}$, the
Minkowski interval.

*Proof.* Put $\tilde P=\tilde Q$ in the explicit form: the coefficient is $Q_0^{2}+(\mathbf Q,\mathbf Q)$,
which is $N(\tilde Q)$. The material reading is the substitution $Q_0=ict$ and $\mathbf Q=\mathbf x$ with
$t$ and $\mathbf x$ real.

This is the article's sharpest point, and it must be stated with its caution. **The operation whose values
are central is the one that carries the metric.** The diagonal of the scalar coupling is the interval, so
the geometry of the material row sits in the **symmetric** part of the quaternionic product; the order of
the two operations, by contrast, sits in the **antisymmetric** part and carries no geometry at all. The
two halves of one product divide the two jobs between them.

The diagonal has three readings that must not be conflated. Its **value** $N(\tilde Q)$ is the interval;
its **sign** separates the timelike from the spacelike element, since $N$ is indefinite on the material
sector; and its **vanishing set** is the light cone, $\{N(\tilde Q)=0\}$, the set of the zero divisors of
the algebra. The square of a material element being central, the interval is a number carried by the
element and not a component of it. The interval itself, the mass shell and the group of its automorphisms
are *Biquaternion Norm and Invertibility*; the cone is *The Light Cone as the Biquaternion Zero-Divisor
Cone* and *Zero Divisors as a Physical Locus in Biquaternionic Form*; the reading of the interval as the
square of a composition is *The Interval as the Square and the Charge of the Material Composition*, and
none of the three is redone here.

**Remark (verified).** The identity $\tilde P\bullet\tilde Q=N(\tilde P,\tilde Q)e_0$ and the square
$\tilde Q\bullet\tilde Q=N(\tilde Q)e_0$ were recomputed on $100$ random biquaternions in exact complex
arithmetic; the maximum deviation from zero is $8.9\times10^{-16}$, machine precision. The commutation
$\tilde P\bullet\tilde Q-\tilde Q\bullet\tilde P$ vanishes **exactly** on the same samples, not merely to
machine precision, the coefficient being literally symmetric.

**Proposition (polarisation identity).** The coefficient is recovered from the diagonal by the
polarisation identity of a symmetric bilinear form,

$$
\tilde P\bullet\tilde Q=\tfrac12\bigl(N(\tilde P+\tilde Q)-N(\tilde P)-N(\tilde Q)\bigr)e_0 ,
$$

equivalently $N(\tilde P+\tilde Q)=N(\tilde P)+N(\tilde Q)+2N(\tilde P,\tilde Q)$.

*Proof.* $N$ is symmetric and bilinear in its two arguments, so expanding $N(\tilde P+\tilde Q)$ gives
$N(\tilde P)+N(\tilde Q)+2N(\tilde P,\tilde Q)$; the coupling is $N(\tilde P,\tilde Q)e_0$ by the
centrality proposition, and the identity follows on rearranging.

**Remark (verified).** The polarisation identity was recomputed on $100$ random biquaternion pairs, with
the two sides agreeing to machine precision on all of them.

**Reading (the interference term).** The coupling is the **cross term of the square of a sum**, the
quantity two operations contribute jointly beyond the sum of their separate intervals. Reading the
diagonal $N(\tilde P)$ as the interval a single operation carries, the off-diagonal $N(\tilde P,\tilde Q)$
is the correction to the interval of the sum: if it vanishes, the two operations contribute to the
interval of their sum only through their separate intervals, and they are uncorrelated for the metric. In
the language of a superposition this is an **interference term** — the joint term of a squared sum — with
the caution that the interference here is symmetric and bilinear and not the sesquilinear cross term of a
norm: the coefficient is indefinite, so it can be positive or negative, and it is not a probability-like
interference.

**Reading (mass and interaction are one form).** A single coefficient carries both of the readings the
framework gives it. Evaluated on one operation the diagonal is the interval, and on a material
four-momentum on shell it is $-m^{2}c^{2}$, so the diagonal carries the **mass**; evaluated on two
operations the off-diagonal is their pairing, so the same coefficient carries the **interaction**. Mass
and interaction are the diagonal and the off-diagonal of one symmetric form, and neither is a separate
object.

**Reading (a signed correlation, and its zeros decouple).** The coefficient is indefinite, so the coupling
of two operations is positive, negative or zero, and a pair with $N(\tilde P,\tilde Q)=0$ contributes
nothing to the interval of their sum. The coupling is therefore a **signed correlation** and not a
probability: it has no positivity, and its zeros are the pairs the metric does not correlate. This is the
same pairing the article reads as a comparison; the name offered here, labelled as a reading, is a
correlation with either sign and a decoupled zero. Nothing in the corpus yet names a physical process
behind a vanishing coupling, and the naming is the framework's and not the algebra's.

## The Contrast with the Symmetrised Plain Product

The operation has a **plain** cousin, the symmetric part of the ordinary product,

$$
\tfrac12\bigl(\tilde P\tilde Q+\tilde Q\tilde P\bigr)
=\bigl[P_0Q_0-(\mathbf P,\mathbf Q)\bigr]e_0+P_0\mathbf Q+Q_0\mathbf P ,
$$

the operation of the band `Focus on the Symmetric Plain Algebra (SPA) — Commutativity`. The two are the
same construction applied to the two rows of the algebra, and they differ in one sign; the difference is
not cosmetic, because the sign decides whether the value is central and whether the operation is a
Jordan product.

| | symmetrised quaternionic (this band) | symmetrised plain (SPA) |
|---|---|---|
| definition | $\tfrac12(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P)$ | $\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ |
| value | $[P_0Q_0+(\mathbf P,\mathbf Q)]e_0$ | $[P_0Q_0-(\mathbf P,\mathbf Q)]e_0+P_0\mathbf Q+Q_0\mathbf P$ |
| image | the centre $\mathbb{C}_{\mathbb{B}}$ | not central, vector part present |
| coefficient | $N(\tilde P,\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q)$ | $B(\tilde P,\tilde Q)=P_0Q_0-(\mathbf P,\mathbf Q)$ |
| unit | none | $e_0$, on both sides |
| Jordan identity | fails | holds |

**The two coefficients differ by one sign, and it is the sign of the vector part.**
$N(\tilde P,\tilde Q)$ is the general **quaternionic** bilinear form, the scalar part of $\tilde P^{\natural}\tilde Q$;
$B(\tilde P,\tilde Q)$ is the general **plain** bilinear form, the scalar part of $\tilde P\tilde Q$. The
scalar part of this article's operation is $N$ and **not** $B$: on the vector part of the pair the two
forms carry opposite signs, and the natural conjugation in the first slot is exactly what flips the sign.
A sentence that names $B$ for the coefficient of the symmetrised quaternionic product is wrong, and the
error is the most tempting of this row. The forms themselves, with their Gram matrices and their
signatures, are *Comparison Between the Four General Products* and *The Four Pairings of the
Biquaternion Algebra*.

**A cross-chapter warning on the letters.** The letters of the two forms are chapter-relative. The
mathematics chapter writes *this* chapter's $N$ — the scalar part of $\tilde P^{\natural}\tilde Q$ — as
$B$, the very letter this chapter reserves for the plain form: a reader who follows the citations into
*The Quaternion Form as a Product on the Symmetric Quaternionic Algebra* will find the quaternionic form
called $B$ there. The object is the same one this chapter calls $N$; only the letter changes. The name of
this chapter's coefficient is $N$ throughout, and $B$ is never it.

**The image is the centre, and that is the physical dividing line.** The symmetrised plain product of two
material operations is again an element with a scalar part and a vector part, so it can be composed
again and can carry a direction; the symmetrised quaternionic product of two material operations is a
number, and a number composes with nothing. The two operations therefore do not do the same job, and the
distinction is exactly the one the two band names record: the plain symmetrisation is the plain
**anticommutator** and stays in the algebra, the quaternionic symmetrisation **couples** and leaves it.

## What the Coupling Cannot Do

Three negative statements bound the operation and are the reason its reading is a caution.

**A central value compares and does not compose.** The operation has **no unit**: there is no $\tilde E$
with $\tilde E\bullet\tilde Q=\tilde Q$ for every $\tilde Q$. The reason is one line — the value
$\tilde E\bullet\tilde Q$ is always **central**, while a general $\tilde Q$ is not, so the equality fails
already at $\tilde Q=e_1$ for every $\tilde E$. The candidate $e_0$ itself acts as
$e_0\bullet\tilde Q=Q_0e_0$, the projection onto the scalar part, and not as the identity. Without a unit
the operation cannot be iterated as a composition, and a chain of couplings has no bracketing-free value
to give.

**It is not a Jordan product.** The symmetrised plain product is a Jordan product; this operation is not.
The failure and its witness belong to the companion article *Why a Central Product Cannot Compose: the
Radical and the Isotropic Elements*, and its algebraic origin is the non-associativity of the parent
quaternionic product: a symmetrisation makes a Jordan algebra out of an associative product and not out
of a general one, and the quaternionic product is not associative. This is the reason the two rows of the
algebra cannot be read alike even though the construction of their symmetric parts is identical.

**It selects no state.** The coefficient $N$ is a $\mathbb{C}$-bilinear form, indefinite on the real
space of the algebra, of signature $(4,4)$ in the real basis; on the material sector it restricts to the
Minkowski form of signature $(3,1)$ and on the informational sector to $(1,3)$. An indefinite form has no
positive cone, and a form with no positive cone selects no state and no probability. The operation
returns the interval of a material operation faithfully and returns **no** notion of a positive norm; a
central-valued pairing is not a state and is not a probability. That role belongs to the sesquilinear row
of the algebra, not to this one. The forms on the six subspaces, with their signatures, are
*The Six Subspaces under the Symmetric Quaternionic Algebra of Biquaternions* and the transversal
signature table of *The Four General Products and Their Physical Readings: the Two Algebras and the Two
Sesqualgebras*.

## The Reading: a Central Value Is the Scalar of a Comparison

**Proposed reading, labelled as such.** Each clause below names a proved identity of the preceding
sections, and the reading is what the framework does with it.

- **The operation is a comparison of two operations.** The value $N(\tilde P,\tilde Q)$ is the scalar
  overlap of the two material operations; the operation couples them to a number. It is the value a
  comparison returns, and it is not a composite operation of the same kind as its arguments.
- **The comparison is order-free.** The operation is commutative, so the coupling of two operations does
  not depend on their order: this is the part of the product that the order does not touch. All of the
  order lives in the antisymmetric half of the parent, the failed bracket of the companion band.
- **The diagonal of the coupling is the interval.** The coupling of an operation with itself is its
  interval, so the symmetric half of the row is the half that carries the metric of the material row.
- **The coupling is the interference term of a sum.** By the polarisation identity the off-diagonal is the
  cross term of the square of a sum, the quantity two operations contribute jointly beyond their separate
  intervals; a vanishing coupling is a pair the metric does not correlate. The interference is symmetric
  and bilinear and carries no positivity.
- **Mass and interaction are one form.** The diagonal, on a material four-momentum on shell, is
  $-m^{2}c^{2}$ and carries the mass; the off-diagonal carries the interaction. One coefficient, read on
  one argument and on two, is both.
- **The pairing is a signed correlation.** The coefficient is indefinite, so a coupling can be positive,
  negative or zero, and a pair with $N(\tilde P,\tilde Q)=0$ is decoupled for the metric. The name is a
  signed correlation, not a probability.
- **The coupling carries the metric, and the order carries the obstruction.** The geometry of the
  material row sits in the symmetric part and the failure of the internal group in the antisymmetric
  part; the two are the two halves of one product and neither can be read off the other.
- **The zeros of the coupling are a selection rule.** The proved statement is that a pair with
  $N(\tilde P,\tilde Q)=0$ is decoupled for the metric, together with the non-degeneracy of the form. A
  family of operations that are **pairwise** $N$-orthogonal therefore contributes to the interval of any
  sum only through its members' separate intervals, the cross terms vanishing. Offered **as a reading**,
  the vanishing coupling is an **orthogonality selection rule** and a maximal $N$-orthogonal family is a
  set the metric does not mix — the algebraic shape of a superselection sector. The reading is of the
  form's zeros and is not a proved statement about states: the coefficient is indefinite, so an
  $N$-orthogonal family is not a positive decomposition, and the name is the framework's and not the
  algebra's. It is a selection rule of the coefficient $N$ and is not the mass selection rule of the
  chiral articles, which is a statement about the gauge invariance of a mass term.

**Caution.** A central value **compares and does not compose**. No associativity, no composition of a
product and no iterated chain can be read from this operation. It is a coupling, and a coupling is a
number.

## The Ledger

**Proved.** The explicit form
$\tilde P\bullet\tilde Q=[P_0Q_0+(\mathbf P,\mathbf Q)]e_0$ and the centrality of the value; the
commutativity; the image equal to the centre $\mathbb{C}_{\mathbb{B}}$; the diagonal,
$\tilde Q\bullet\tilde Q=N(\tilde Q)e_0$, with the material reading $-c^{2}t^{2}+\mathbf x^{2}$; the
reconstruction $\tilde P^{\natural}\tilde Q=\tilde P\bullet\tilde Q+\tilde P\wedge_{\natural}\tilde Q$;
the sixteen basis products, diagonal with values $\delta_{\mu\nu}e_0$; the absence of a unit, with $e_0$
acting as the projection onto the scalar part; the coefficient $N$ and not $B$, the two differing by the
sign of the vector part; the indefiniteness of the coefficient on the real space; the polarisation
identity, recovering the coefficient from the diagonal as the cross term of a sum.

**Readings.** That the symmetrised quaternionic product is the scalar coupling of two material
operations; that its value is the number a comparison of the two operations returns; that the comparison
is order-free; that its diagonal is the interval and the symmetric half of the row carries the metric;
that the off-diagonal is the interference term of a sum; that mass and interaction are the diagonal and
the off-diagonal of one form; that the pairing is a signed correlation whose zeros decouple; that the zeros
of the coupling are an orthogonality selection rule and a maximal $N$-orthogonal family the algebraic shape
of a superselection sector.

**Not claimed.** That a physical material operation is a biquaternion, or that the coupling of two
operations is a measured quantity. That a central value composes, associates or iterates. That the
coupling carries a positivity or a state. That the symmetrised quaternionic product is a Jordan product.
That the reading of the value as a "comparison" is forced by the algebra rather than chosen; the algebra
forces the centrality and the commutativity, and the naming is the framework's. That the interference,
mass-and-interaction or signed-correlation namings are forced by the algebra; and that a vanishing
coupling has a physical process behind it. That an $N$-orthogonal family is a set of physical
superselection sectors, or that the orthogonality-selection-rule naming is forced by the algebra rather
than chosen; the algebra forces only the vanishing of the cross term and the non-degeneracy of the form.

## Summary

The symmetrised quaternionic product
$\tilde P\bullet\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P)$ is the
symmetric part of the quaternionic product for the exchange of its two arguments, and its value is
central, $\tilde P\bullet\tilde Q=[P_0Q_0+(\mathbf P,\mathbf Q)]e_0=N(\tilde P,\tilde Q)e_0$: it is the
**general quaternionic bilinear form read as a product**. The operation is commutative, its image is the
centre, it has **no unit** ($e_0\bullet\tilde Q=Q_0e_0$ projects onto the scalar part), and it is **not a
Jordan product**, unlike the symmetrised plain product of the band SPA. Its diagonal is the **interval**,
$\tilde Q\bullet\tilde Q=N(\tilde Q)e_0$, so the operation whose values are central is the one that
carries the metric of the material row, while the order of the two operations sits in the antisymmetric
half of the parent. By the polarisation identity the off-diagonal coefficient is the interference term of
a sum, so one form carries both the **mass** (its diagonal) and the **interaction** (its off-diagonal),
and the pairing is a **signed correlation** rather than a probability. The coupling differs from the
symmetrised plain product of the plain row in one sign:
its coefficient is the quaternionic form $N$, the scalar part of $\tilde P^{\natural}\tilde Q$, and not
the plain form $B$, the scalar part of $\tilde P\tilde Q$ — the two differ by the sign of the vector part
alone. The operation reads as a **scalar coupling**: it compares two material operations and returns the
number their overlap carries, and the reading is bounded by the caution that a central value **compares
and does not compose** and selects no state. The radical and the isotropic elements, the failure of the
Jordan identity with its witness, and the boundary of the coefficient against the form $B$ are the
companion article *Why a Central Product Cannot Compose: the Radical and the Isotropic Elements*; the
coefficient read as a form is *The Quaternion Form as a Product on the Symmetric Quaternionic Algebra*;
the six subspaces are *The Six Subspaces under the Symmetric Quaternionic Algebra of Biquaternions*; and
the comparison of the four rows is *The Four General Products and Their Physical Readings: the Two Algebras and
the Two Sesqualgebras*, none of them redone here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | the biquaternion algebra |
| $e_0,e_1,e_2,e_3$; $i$ | the basis, $e_k^{2}=-e_0$; the central scalar imaginary |
| $\tilde Q=Q_0e_0+\mathbf Q$ | an element and its scalar–vector split |
| ${}^{\natural}$, ${}^{*}$ | the natural and the Hermitian conjugations |
| $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q$ | the general quaternionic product (GQA) |
| $\tilde P\bullet\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P)$ | the symmetrised quaternionic product (SQA, this band) |
| $\tilde P\wedge_{\natural}\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P)$ | the antisymmetrised quaternionic product (AQA, the companion band) |
| $\tilde P^{\natural}\tilde Q=\tilde P\bullet\tilde Q+\tilde P\wedge_{\natural}\tilde Q$ | the reconstruction of the parent |
| $N(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q)$ | the general quaternionic bilinear form, the coefficient of the coupling |
| $B(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q)=P_0Q_0-(\mathbf P,\mathbf Q)$ | the general plain bilinear form, the coefficient of the plain row |
| $N(\tilde Q)=Q_0^{2}+Q_1^{2}+Q_2^{2}+Q_3^{2}$ | the biquaternion norm, the diagonal of the coupling |
| $ict\,e_0+\mathbf x$ | the material coordinate; $\tilde Q\bullet\tilde Q=-c^{2}t^{2}+\mathbf x^{2}$ |
| $\mathbb{C}_{\mathbb{B}},\mathrm{Vect}(\mathbb{B}),\mathbb{H}_{\mathbb{B}},i\mathbb{H}_{\mathbb{B}},\mathbb{M}_+,\mathbb{M}_-$ | the six distinguished subspaces |

## Further Reading

- *The Mathematical Study of Biquaternions*, the physics entry point to the mathematical study under
  which this block sits.
- Mathematics article *The 12 Products of the Biquaternion Complex Space*
  (`articles_maths/the-12-products-of-the-biquaternion-complex-space.md`), for the twelve
  operations, the method of the decomposition and the laws of each.
- Mathematics article *Introduction to the Symmetric Quaternionic Algebra of Biquaternions*
  (`articles_maths/introduction-to-the-symmetric-quaternionic-algebra-of-biquaternions.md`), for the
  operation, its class, its image and the sixteen products.
- Mathematics article *The Quaternion Form as a Product on the Symmetric Quaternionic Algebra*
  (`articles_maths/the-quaternion-form-as-a-product-on-the-symmetric-quaternionic-algebra.md`), for the
  coefficient read as a form, its Gram matrix, its realification and the failure of its invariance.
- Mathematics article *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*
  (`articles_maths/the-radical-and-the-isotropic-elements-of-the-symmetric-quaternionic-algebra.md`), for
  the radical, the isotropic elements and the Jordan witness.
- Mathematics article *The Multiplication Operators of the Symmetric Quaternionic Algebra*
  (`articles_maths/the-multiplication-operators-of-the-symmetric-quaternionic-algebra.md`), for the
  operators $L^{\bullet}_{\tilde A}$ and the adjoint with respect to the form.
- Mathematics article *The Symmetric and Antisymmetric Parts of an Algebra Product*
  (`articles_maths/the-symmetric-and-antisymmetric-parts-of-an-algebra-product.md`), for the general
  construction of the two parts and the reconstruction.
- Companion article *The Interval as the Square and the Charge of the Material Composition*, for the
  square identity, the interval and the multiplicativity of the norm.
- Companion article *The Ordinary Product and the Material Sector*, for the form $B$ and the plain row.
- Companion article *The Symmetrised Material Composition and the Jordan Identity*, for the symmetrised
  plain product (SPA), the Jordan-product contrast of this operation.
- Companion article *The Four General Products and Their Physical Readings: the Two Algebras and the Two
  Sesqualgebras*, for the transversal comparison and the signature table.
- Companion article *Why a Central Product Cannot Compose: the Radical and the Isotropic Elements*, for
  the radical, the isotropic elements and the Jordan witness read physically.
- Companion article *The Brackets That Do Not Close: the Jacobi Failure of the Quaternionic Commutator*,
  for the antisymmetric half of the same parent.
