# __Why a Central Product Cannot Compose: the Radical and the Isotropic Elements__

## Introduction

The symmetrised quaternionic product returns a number for every pair of material operations, and a number
composes with nothing. This article reads the two structures that show how far the consequent failure
reaches and where it stops. The failure is *compositive*: the operation has **no unit**, its unit
candidate acting as a projection rather than as an identity, and it **fails the Jordan identity**, so it
does not behave like the symmetrised *plain* product of the plain row. The reach is *discriminating*: the
operation is **non-degenerate**, so its radical — the elements it fails to separate from everything — is
trivial, and the only elements it fails to separate from themselves are the **isotropic** ones, the
lightlike elements of the material row. The article's claim is the pair of these: a product whose values
are **central** cannot compose, and yet the same product still separates, everywhere except on the cone.

The operation is

$$
\tilde P\bullet\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P\bigr)
=\bigl[P_0Q_0+(\mathbf P,\mathbf Q)\bigr]e_0=N(\tilde P,\tilde Q)\,e_0 ,
$$

the symmetrised quaternionic product of the band
`#### Focus on the Symmetric Quaternionic Algebra (SQA) of Biquaternions — Coupling`. Its values lie in
the **centre** $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$, and the whole article turns on the reading that
follows: a product whose image is the centre returns a number, a number has no slot to act in, and the
absence of a slot is the absence of a composition. The two structures that measure the failure and the
reach are the radical and the isotropic set.

The article keeps to the operation and to the coefficient it returns. The operation, its centrality, its
commutativity, the absence of a unit and the diagonal as the interval are the companion article
*The Quaternion Form as a Product: the Scalar Coupling of Two Material Operations*; the class, the image
and the sixteen products are *Introduction to the Symmetric Quaternionic Algebra of Biquaternions*; the
radical, the isotropic elements and the Jordan failure, in their algebraic form, are
*The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*; the six subspaces, with
the restriction of the coefficient to each, are *The Six Subspaces under the Symmetric Quaternionic
Algebra of Biquaternions*; and the two bilinear forms of the algebra, with their Gram matrices and their
signature table, are *Comparison Between the Four General Products* and
*The Four General Products and Their Physical Readings*.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with basis
$e_0=1,e_1,e_2,e_3$, $e_k^{2}=-e_0$, $e_1e_2=e_3$, and central scalar imaginary $i$ with $i^{2}=-1$; an
element is $\tilde Q=Q_0e_0+\mathbf Q$; the natural conjugation is ${}^{\natural}$, the Hermitian star
${}^{*}=\bar{\cdot}\circ{}^{\natural}$, and the sectors are $\mathbb{M}_\pm$. The ordinary product is
$\tilde P\tilde Q$, the quaternionic product is $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q$, and
$\tilde P\bullet\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P)$ is its
symmetrisation. The symmetrisation symbol $\bullet$ is **row-relative** in this chapter: the plain row
writes it for $\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$, a different operation. The **general
quaternionic bilinear form** is
$N(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q)$ and the
**general plain bilinear form** is $B(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q)=P_0Q_0-(\mathbf P,\mathbf Q)$;
the biquaternion norm is $N(\tilde Q)=\langle\tilde Q,\tilde Q\rangle_{\natural}=Q_0^{2}+Q_1^{2}+Q_2^{2}+Q_3^{2}$.

## A Product Whose Values Are All Central

**Proposition (the values lie in the centre).** For all $\tilde P,\tilde Q$ the value
$\tilde P\bullet\tilde Q$ lies in the centre $\mathbb{C}_{\mathbb{B}}$, and for every $\tilde Q$ the value
$\tilde Q\bullet\tilde Q=N(\tilde Q)e_0$ lies in the centre.

*Proof.* The explicit form puts the value on the central line $\mathbb{C}e_0$; the square is the special
case $\tilde P=\tilde Q$. Both are in the companion article.

A value in the centre is a **number**, and the whole service and the whole failure of the operation come
from that. The service is the diagonal: the square of an element is its interval, and a number can be
compared, multiplied and read as a physical invariant. The failure is the rest: a number carries no
vector direction and no first or second slot, so it invites no further product and admits no iteration.
The operation is the identity table of the coefficient $N$, and its image is one-dimensional while its
domain is eight-dimensional over the reals; almost all of the structure of the pair is annihilated by the
product.

## The Radical of the Coupling

**Definition (radical).** The **radical** of the coupling is the set of elements it does not separate
from any element,

$$
\mathrm{Rad}(\bullet)=\bigl\{\tilde Z:\ N(\tilde Z,\tilde X)=0\ \text{for every}\ \tilde X\bigr\}
=\bigl\{\tilde Z:\ \tilde Z\bullet\tilde X=0\ \text{for every}\ \tilde X\bigr\} .
$$

**Proposition (the radical is trivial).** $\mathrm{Rad}(\bullet)=\{0\}$. The coupling is non-degenerate:
for every $\tilde Z\neq0$ there is an $\tilde X$ with $\tilde Z\bullet\tilde X\neq0$, and the coefficient
has Gram matrix $I_4$, of rank $4$ over $\mathbb{C}$.

*Proof.* The coefficient is $N(\tilde Z,\tilde X)=Z_0X_0+(\mathbf Z,\mathbf X)$; taking $\tilde X=e_0$
gives $Z_0$, and taking $\tilde X=e_k$ gives $Z_k$, so an element in the radical has all four coordinates
zero. Its Gram matrix in the basis $e_0,e_1,e_2,e_3$ is the identity, of rank $4$ over $\mathbb{C}$; its
realification is $\operatorname{diag}(I_4,-I_4)$, of signature $(4,4)$ and index $4$.

The radical is the algebraic home of "the pairs the coupling does not separate", and the proposition says
there are no **elements** it fails to separate from everything. This is the exact place where the coupling
is stronger than a degenerate pairing: a degenerate form has a nonzero radical and leaves a whole subspace
unmeasured, while the coupling measures every direction of every element. The failure of the operation is
therefore not a failure of discrimination; the coupling loses none of the input to the radical.

## The Isotropic Elements

**Definition (isotropic element).** An element is **isotropic** for the coupling when it is annihilated by
itself,

$$
\tilde Q\ \text{isotropic}\iff\tilde Q\bullet\tilde Q=0
\iff N(\tilde Q)=0 ,
$$

and two elements $\tilde P,\tilde Q$ are **isotropic as a pair** when $N(\tilde P,\tilde Q)=0$.

**Proposition (the isotropic set is the cone).** The isotropic elements of the coupling are the
**zero divisors** of the algebra and, on the material sector, the **light cone**; they form the complex
cone of real dimension six that is the vanishing set of $N$, and they are closed under the parent product
on either side.

*Proof.* $\tilde Q\bullet\tilde Q=N(\tilde Q)e_0$ vanishes exactly when $N(\tilde Q)=0$; the
identification of the vanishing set of $N$ with the zero divisors and, on the material sector, with the
light cone, and its closure under the parent product, are *Biquaternion Norm and Invertibility* and
*The Light Cone as the Biquaternion Zero-Divisor Cone*.

The isotropic elements are the one set on which the coupling **does** fail to separate an element from
itself, although it still separates the elements pairwise by the preceding section. The reading is exact
and narrow: the coupling is non-degenerate, so an isotropic element is not invisible to the coupling; it
is an element whose **own** value is zero, while its coupling with a suitable other element is not. A
lightlike element is therefore a direction the coupling registers but cannot normalise, the same object
the corpus reads as the kinematic boundary. The cone is owned by *The Light Cone as the Biquaternion
Zero-Divisor Cone* and *Zero Divisors as a Physical Locus in Biquaternionic Form*, and the identification
is cited, not made here.

**Remark (verified).** The radical and the isotropic set were recomputed in exact complex arithmetic. The
Gram matrix of the coefficient is the identity on $100$ random pairs, giving the trivial radical and rank
$4$; the four explicitly lightlike elements $e_0+ie_1$, $e_1+ie_2$, $e_1-ie_2$, $ie_0+e_1$ all have
$N=0$ **exactly**, so their square under the coupling is exactly $0$; and their coupling with $e_0$ is
their scalar coordinate, which is nonzero for $e_0+ie_1$ and for $ie_0+e_1$ and vanishes for $e_1\pm ie_2$,
while those two are separated by other partners, $N(e_1+ie_2,e_1)=1$.

## No Unit, and the Failure of the Jordan Identity

Two failures separate this operation from the symmetrised plain product of the band
`Focus on the Symmetric Plain Algebra (SPA) — Commutativity`, which is a Jordan product with a unit.

**Proposition (no unit).** There is no element $\tilde E$ with
$\tilde E\bullet\tilde Q=\tilde Q$ for every $\tilde Q$. The candidate $e_0$ acts as
$e_0\bullet\tilde Q=Q_0e_0$, the projection onto the scalar part, and the operation has no right unit
either.

*Proof.* The value $\tilde E\bullet\tilde Q$ is always central, by the explicit form, while a general
$\tilde Q$, such as $\tilde Q=e_1$, is not; so no $\tilde E$ satisfies
$\tilde E\bullet\tilde Q=\tilde Q$ for every $\tilde Q$. The candidate $e_0$ is the projection because
$N(e_0,\tilde Q)=Q_0$. The same argument on the right excludes a right unit.

**Proposition (the Jordan identity fails).** The identity

$$
(\tilde X^{\bullet2}\bullet\tilde Y)\bullet\tilde X=\tilde X^{\bullet2}\bullet(\tilde Y\bullet\tilde X) ,
\qquad \tilde X^{\bullet2}=\tilde X\bullet\tilde X=N(\tilde X)e_0 ,
$$

is **false**, with the witness $\tilde X=\tilde Y=e_1$: the left side is $(e_0\bullet e_1)\bullet e_1=0$
and the right side is $e_0\bullet(e_1\bullet e_1)=e_0$.

*Proof.* $e_1\bullet e_1=N(e_1)e_0=e_0$, because $N(e_1)=1$; then $e_0\bullet e_1=N(e_0,e_1)e_0=0$,
because $N(e_0,e_1)=\mathrm{Sc}(e_0e_1)=0$, so the left side vanishes; the right side is
$e_0\bullet e_0=N(e_0)e_0=e_0$.

The two failures have one cause, and the cause is **non-associativity of the parent**. A symmetrisation
turns an associative product into a Jordan algebra because the associativity of the parent supplies the
Jordan identity; the quaternionic product is not associative, so its symmetrisation inherits no Jordan
identity. The failure is not marginal: it holds at a pair of basis elements, so no weaker variant of the
identity that the plain symmetrisation enjoys can be transferred. The witness is the one of
*The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*. The consequence for the
band is direct: the word **Coupling** in its title is a coupling and not a composition, because an
operation that has no unit and no Jordan identity cannot be iterated as an algebra of a single operation.

## The Centre, the Coupling and the Two Forms

The value of the coupling is central, and that fact has to be held apart from two objects it resembles.
The three are easy to confuse because all three live on the central line or near it.

**The coupling is a form read as a product.** The coefficient $N(\tilde P,\tilde Q)$ is the general
quaternionic bilinear form of *Conventions in the Biquaternion Universe*; the operation
$\tilde P\bullet\tilde Q$ is that form with the value placed in the centre and called a product. The
distinction is not idle: **as a form** $N$ is symmetric, $\mathbb{C}$-bilinear, non-degenerate of
signature $(4,4)$ on the real space, and it is a perfectly good pairing; **as a product** it is a
central-valued operation that cannot compose. The mathematics article *The Quaternion Form as a Product
on the Symmetric Quaternionic Algebra* is exactly the passage between the two readings.

**The coupling is not the plain form.** The coefficient is $N$ and not the general plain bilinear form
$B$. The two differ by the sign of the vector part alone,

$$
N(\tilde P,\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q) , \qquad
B(\tilde P,\tilde Q)=P_0Q_0-(\mathbf P,\mathbf Q) ,
$$

so a value of this band's operation that is written $B$ is wrong, and the natural conjugation in the first
slot of the parent is what fixes the sign. The forms themselves, with their Gram matrices and their
signatures, are *Comparison Between the Four General Products*.

**A cross-chapter warning on the letters.** The letter $B$ is chapter-relative, and it is the one the
mathematics chapter uses for the *other* form: there the quaternion form $B$ is what this chapter calls
$N$, the scalar part of $\tilde P^{\natural}\tilde Q$. A reader who follows the citations into
*The Quaternion Form as a Product on the Symmetric Quaternionic Algebra* will see the coefficient of the
coupling written $B$ there. The object is the same; only the letter changes. In this chapter the
coefficient is $N$ and $B$ is the plain form throughout.

**The two forms read differently on the six subspaces.** Because the difference is the sign of the vector
part, the two forms agree where the vector part vanishes and on the balanced vector subspace, and differ
on the four four-dimensional subspaces, where they exchange their signatures.

| subspace | $N$ (the coupling) | $B$ (the plain form) |
|---|---|---|
| centre $\mathbb{C}_{\mathbb{B}}$ | $(1,1)$ | $(1,1)$ |
| vector $\mathrm{Vect}(\mathbb{B})$ | $(3,3)$ | $(3,3)$ |
| quaternion $\mathbb{H}_{\mathbb{B}}$ | $(4,0)$ | $(1,3)$ |
| anti-quaternion $i\mathbb{H}_{\mathbb{B}}$ | $(0,4)$ | $(3,1)$ |
| informational $\mathbb{M}_+$ | $(1,3)$ | $(4,0)$ |
| material $\mathbb{M}_-$ | $(3,1)$ | $(0,4)$ |

The two forms agree on the centre — where the vector part is zero and the two coefficients coincide — and
on the vector subspace, where the two coefficients are opposite but the form is balanced and has the same
signature $(3,3)$; they part company on the four four-dimensional subspaces. There they exchange the
signatures: $N$ has on $\mathbb{H}_{\mathbb{B}}$ the signature $B$ has on $\mathbb{M}_+$, and $N$ has on
$i\mathbb{H}_{\mathbb{B}}$ the signature $B$ has on $\mathbb{M}_-$. On the material sector in particular
$N$ is the indefinite Minkowski form $(3,1)$ and $B$ the definite negative Euclidean form $(0,4)$; the
passage between the two is the passage between the interval and the Euclidean square, and it is the sign
the natural conjugation inserts. The signatures on the six subspaces are *The Six Subspaces under the
Symmetric Quaternionic Algebra of Biquaternions* and the transversal table of
*The Four General Products and Their Physical Readings*. The centre
and vector rows are read as the real part of the coefficient, the two coefficients there being complex.

## The Reading: Why a Central Product Cannot Compose

**Proposed reading, labelled as such.** Each clause names a proved identity of the preceding sections.

- **The radical is the set of pairs the coupling does not separate, and it is trivial.** Nothing in the
  algebra is invisible to the coupling; every direction of every element is measured by some partner. The
  operation does not fail for lack of discrimination.
- **The only elements it fails to separate from themselves are the isotropic ones.** The isotropic set is
  the light cone of the material row: the coupling registers every direction and can normalise none of
  the lightlike ones. So the operation does more than compare; it compares everywhere except on the cone,
  where the comparison returns zero.
- **The failure is exactly compositive.** The values are central, so the operation returns a number; a
  number has no slot, so it cannot act on anything, so the operation has no unit and no Jordan identity
  and no chain. The failure and the reach are the two faces of the single fact that the image is the
  centre.
- **A central product cannot compose, and it also cannot select a state.** The coefficient is indefinite,
  of signature $(4,4)$ on the real space, so it has no positive cone; the coupling carries the interval of
  the material row and carries no positivity. Comparison and composition are different; comparison and
  positivity are different too.
- **No algebra of masses in this row.** A unit and a Jordan identity are what make a symmetrised product
  an algebra one can iterate, with powers, spectra and observables. Neither exists here, so no observable
  algebra of masses — no spectral bookkeeping built on the diagonal — can be assembled from the material
  coupling, and the observable structure must come from the informational, sesquilinear row. The diagonal
  gives the interval, but an interval is not a mass operator without the algebra that would make it one.
- **Mass is a character and not an eigenvalue.** The proved facts are the trivial radical, the centrality
  of the values, the absence of a unit and the failure of the Jordan identity. Read together they say that
  the interval this row attaches to a material operation is a **multiplicative label of the unit group**,
  the group homomorphism — the character $N:(\mathbb{B}^{\times},\cdot)\to(\mathbb{C}^{\times},\cdot)$ of
  the **ordinary** product, its multiplicativity proved in *Biquaternion Norm and Invertibility* — and that
  it **cannot** be read as an eigenvalue of a material operator: an eigenvalue needs an algebra with a
  unit and a spectral theory, and the preceding
  section proves that neither exists in this row. Offered as a reading, a mass spectrum built on this row
  would be a set of **characters**, not a set of eigenvalues; whether any physical spectrum is of that kind
  is not claimed, and the algebra asserts only the multiplicativity of $N$ and the absence of a unit.
- **Comparison without a normalisation.** The proved facts are the trivial radical together with the
  isotropic set equal to the light cone. Read together they describe a **comparison that measures every
  direction and normalises none**: every nonzero element is separated from some partner, so no direction is
  invisible, and a lightlike element is not separated from itself, so no direction on the cone is
  normalised. Offered as a reading, the coupling is a **comparison that normalises none** — it registers
  directions and supplies no eigenstate on the cone. The name is the framework's and not the algebra's,
  which asserts only the radical and the cone.

**Caution.** An obstruction is a negative result, and a negative result bounds a reading without
supplying one. This article says where the operation **cannot** be read (as a composition, as an algebra
with a unit, as a state) and does not say where the composition the framework does use comes from. The
unit, the associativity and the Jordan identity all live in the **plain** product and in the sesquilinear
rows, not in the quaternionic symmetrisation.

**Open question.** Whether the "separation" reading of the radical and the isotropic set is more than a
naming is recorded and not settled. The algebra proves the trivial radical and the cone; it does not
prove that "separation" is the right physical word for the coefficient.

## The Ledger

**Proved.** That every value of $\bullet$ is central and that the image is $\mathbb{C}_{\mathbb{B}}$; the
trivial radical, $\mathrm{Rad}(\bullet)=\{0\}$, with the Gram matrix $I_4$; the isotropic elements as the
vanishing set of $N$, the zero divisors and the material light cone; the absence of a unit, with $e_0$ as
the projection onto the scalar part; the failure of the Jordan identity at the witness
$(\tilde X,\tilde Y)=(e_1,e_1)$, the two sides $0$ and $e_0$; the coefficient $N$ and not $B$; the
signatures $(1,1),(3,3),(4,0),(0,4),(1,3),(3,1)$ of $N$ on the six subspaces and the same list with
$(4,0)$ and $(0,4)$ at the two sectors for $B$.

**Readings.** That the radical is the set of pairs the coupling does not separate and is trivial; that
the isotropic set is the one place the coupling fails to separate an element from itself; that a central
product cannot compose; that the coupling, being indefinite, selects no state; that no observable algebra
of masses can be assembled from the material coupling, the observable structure coming from the
informational row; that mass in this row is a character of the unit group and not an eigenvalue, so a mass
spectrum here would be a set of characters; that the coupling is a comparison that measures every
direction and normalises none.

**Not claimed.** That a physical operation is a biquaternion. That "separation" is a forced reading of
the radical. That the coupling carries a positivity, a state or a probability. That the failure of the
Jordan identity has a physical process behind it. That a lightlike element is a measured zero of some
physical comparison. That the informational row in fact supplies a mass spectrum, or that the interval
is a mass operator: only that no observable algebra of masses is available in this row. That a physical
mass spectrum is a set of characters, or that "a comparison that normalises none" is forced by the
algebra: only the multiplicativity of $N$, the trivial radical and the cone are asserted.

## Physical Readings

The isotropic elements read as the null cone, so the radical of the central product is the cone read as a degeneration of a product, and the article's reading is that a central product cannot compose because composing needs a value that can be multiplied rather than only added. Read against the states, the absence of a unit and the failure of the Jordan identity say that this product cannot define an observable; read for invariance, its central values are of the class that no change of the local complex structure touches.

## Summary

The symmetrised quaternionic product has all its values in the centre $\mathbb{C}_{\mathbb{B}}$, and the
whole article is the consequence of that one fact. Its **radical is trivial** — for every nonzero
$\tilde Z$ there is an $\tilde X$ with $\tilde Z\bullet\tilde X\neq0$, the coefficient $N$ having Gram
matrix $I_4$ and rank $4$ — so the coupling fails to separate no element from everything; the only
elements it fails to separate from **themselves** are the **isotropic** ones, $\tilde Q\bullet\tilde Q=0$,
which are the zero divisors and, on the material sector, the light cone. The operation has **no unit**,
its unit candidate $e_0$ acting as the projection $\tilde Q\mapsto Q_0e_0$ onto the scalar part, and it
**fails the Jordan identity**, with the witness $\tilde X=\tilde Y=e_1$: the two sides
$(e_0\bullet e_1)\bullet e_1$ and $e_0\bullet(e_1\bullet e_1)$ are $0$ and $e_0$. Both failures have one
cause: the parent quaternionic product is not associative, and a symmetrisation inherits a Jordan identity
from an associative product and from no other. The coefficient is the general **quaternionic** bilinear
form $N(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)$, **not** the general plain bilinear
form $B(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q)$, the two differing by the sign of the vector
part alone; the two read $(1,1),(3,3),(4,0),(0,4),(1,3),(3,1)$ and
$(1,1),(3,3),(1,3),(3,1),(4,0),(0,4)$ on the six subspaces, agreeing on the centre and the vector
subspace and exchanging signatures on the other four. The reading is that a product whose image is
the **centre** returns a number, and a number **compares and does not compose**: the operation is the
scalar coupling of the material row, non-degenerate, and it is not an algebra with a unit, not a Jordan
algebra and not a state. Because no unit and no Jordan identity is available, no observable algebra of
masses can be assembled from this row — the diagonal gives the interval, but not an interval *operator* —
and the observable structure must come from the informational, sesquilinear row. The algebraic radical,
isotropic elements and Jordan witness are
*The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*; the six-subspace
restrictions are *The Six Subspaces under the Symmetric Quaternionic Algebra of Biquaternions*; the
operation itself is the companion *The Quaternion Form as a Product: the Scalar Coupling of Two Material
Operations*; and the two forms are *Comparison Between the Four General Products* and
*The Four General Products and Their Physical Readings*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\bullet\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P)$ | the symmetrised quaternionic product (SQA) |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ | the centre, the image of the coupling |
| $\mathrm{Rad}(\bullet)=\{\tilde Z:\tilde Z\bullet\tilde X=0\ \forall\tilde X\}$ | the radical; equal to $\{0\}$ |
| $\tilde Q\bullet\tilde Q=N(\tilde Q)e_0$ | the square; the diagonal of the coupling |
| $\{N(\tilde Q)=0\}$ | the isotropic elements; the zero divisors and the light cone |
| $\bigl(\tilde X^{\bullet2}\bullet\tilde Y\bigr)\bullet\tilde X=\tilde X^{\bullet2}\bullet(\tilde Y\bullet\tilde X)$ | the Jordan identity; false, witness $(e_1,e_1)$ |
| $e_0\bullet\tilde Q=Q_0e_0$ | the projection onto the scalar part; there is no unit |
| $N(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q)$ | the general quaternionic bilinear form, the coefficient |
| $B(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q)=P_0Q_0-(\mathbf P,\mathbf Q)$ | the general plain bilinear form; not the coefficient |
| $(1,1),(3,3),(4,0),(0,4),(1,3),(3,1)$ | the signatures of $N$ on the six subspaces |

## Further Reading

- *The Mathematical Study of Biquaternions*, the physics entry point to the mathematical study under
  which this block sits.
- Mathematics article *The 12 Products of the Biquaternion Complex Space*
  (`articles_maths/the-12-products-of-the-biquaternion-complex-space.md`), for the twelve
  operations, the method of the decomposition and the laws of each.
- Mathematics article *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*
  (`articles_maths/the-radical-and-the-isotropic-elements-of-the-symmetric-quaternionic-algebra.md`), for
  the radical, the isotropic elements and the Jordan witness.
- Mathematics article *The Six Subspaces under the Symmetric Quaternionic Algebra of Biquaternions*
  (`articles_maths/the-six-subspaces-under-the-symmetric-quaternionic-algebra-of-biquaternions.md`), for
  the restriction of the coefficient to the six subspaces.
- Mathematics article *Introduction to the Symmetric Quaternionic Algebra of Biquaternions*
  (`articles_maths/introduction-to-the-symmetric-quaternionic-algebra-of-biquaternions.md`), for the class
  and the image.
- Mathematics article *The Quaternion Form as a Product on the Symmetric Quaternionic Algebra*
  (`articles_maths/the-quaternion-form-as-a-product-on-the-symmetric-quaternionic-algebra.md`), for the
  passage from the form to the product.
- Companion article *The Quaternion Form as a Product: the Scalar Coupling of Two Material Operations*,
  for the operation, the centrality, the commutativity and the interval.
- Companion article *The Ordinary Product and the Material Sector*, for the form $B$ and the plain row.
- Companion article *The Symmetrised Material Composition and the Jordan Identity*, for the symmetrised
  plain product (SPA), the Jordan-product contrast of this operation.
- Companion article *Conventions in the Biquaternion Universe*, for the general quaternionic bilinear form
  and the four forms.
- Companion article *The Light Cone as the Biquaternion Zero-Divisor Cone* and *Zero Divisors as a
  Physical Locus in Biquaternionic Form*, for the cone.
- Companion article *The Four General Products and Their Physical Readings*, for the signature table.
