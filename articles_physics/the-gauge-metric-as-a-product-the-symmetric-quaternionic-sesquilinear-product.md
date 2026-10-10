# __The Gauge Metric as a Product: the Symmetric Quaternionic Sesquilinear Product__

## Introduction

The fourth of the framework's four general products is the general quaternionic sesquilinear product
$\tilde P^{\natural}\tilde Q^{*}$, the plain product with the natural conjugation in the first slot and
the star in the second. Its scalar form is the **Krein form** $K$, Hermitian, non-degenerate and
**indefinite**, and the physics menu files the row it belongs to under the word **Metric**. The same row
is also the row that is **not a state space**: its states are null, it has no unit, and the ternary
product built from it fails the Jordan triple identity (*Why the Fourth Product Is a Gauge Structure and
Not a State Space*). The two facts are the tension the band has to carry. This article reads the
symmetric half of the fourth product as a **product in its own right**, and shows where the metric word
is earned and where it stops: the operation carries the indefinite pairing as its scalar part, and it is
a pairing and not a norm.

The operation is the **symmetric quaternionic sesquilinear product**

$$
\tilde P\bullet\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q^{*}+\tilde Q^{*}\tilde P^{\natural}\bigr)
=\bigl[P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})\bigr]-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P},
$$

the operation named $\mathrm{SQS}$ in *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* and developed as a multiplication in *Introduction to the Symmetric Quaternionic Sesqualgebra of
Biquaternions*. Its scalar part is the Krein form $K$ and its vector part is the mixed term alone. Its
companion, the **antisymmetric quaternionic sesquilinear product**

$$
\tilde P\diamond\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q^{*}-\tilde Q^{*}\tilde P^{\natural}\bigr)
=\mathbf{P}\times\overline{\mathbf{Q}},
$$

is pure vector, and the two reconstruct the fourth product,

$$
\tilde P^{\natural}\tilde Q^{*}=\tilde P\bullet\tilde Q+\tilde P\diamond\tilde Q.
$$

The antisymmetric half is read in *The Cross Product of a
Vector with Its Conjugate: the Antisymmetric Gauge Product*; this article keeps to the symmetric half,
except where the split itself must be stated.

The article owns the reading of the symmetric half as a product: the rule, the value, the two symmetries,
the absence of a unit, the failure of the Jordan identity, and the sense in which the operation is the
invariant pairing of the gauge side of the frame. It defers the metric itself — its signature, its inertia
$(1,3)$ over the complex coefficients and $(2,6)$ over the real parameters, its fundamental decomposition
and its isometry group $U(1,3)$ — to *The Fourth Product and Its Indefinite Metric*; the states the metric
cannot normalise to *The States the Indefinite Metric Cannot Normalise*; the positivity of the probability
form and the state cone to *Mass, Rank and the Positivity of the Dagger*; the gauge transformations
themselves to *The Gauge Principle in Biquaternionic Form*; and the algebra of the split to the
mathematics articles *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions*, *The
Symmetric and Antisymmetric Parts of a Sesqualgebra Product* and *The 12 Products of the Biquaternion Complex Space*.

**Conventions.** As in the companion articles of this block: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$
with basis $e_0,e_1,e_2,e_3$, $e_0=1$, $e_k^{2}=-e_0$, $e_1e_2=e_3$, and central scalar imaginary $i$;
a general element is $\tilde Q=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$, of scalar part
$\mathrm{Sc}(\tilde Q)=Q_0$ and vector part $\mathbf{Q}=\sum_kQ_ke_k$; the natural conjugation is
$\tilde Q^{\natural}=Q_0e_0-\mathbf{Q}$, the coefficientwise one is $\bar{\tilde Q}=\sum_\mu\bar Q_\mu e_\mu$,
and the star is $\tilde Q^{*}=\overline{\tilde Q^{\natural}}$; $(\mathbf{P},\mathbf{Q})=\sum_kP_kQ_k$ and
$\times$ are the bilinear dot and cross products; the fourth product is
$\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q^{*}$; the Krein form is
$K(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$
with sign vector $\varepsilon=(1,-1,-1,-1)$; the sectors are $\mathbb{M}_+$ (informational) and
$\mathbb{M}_-$ (material), with $\flat=-{}^{*}$. All conventions are those of *Conventions in the
Biquaternion Universe*.

**A notation caution.** The physics block writes the fourth product $\tilde P\star\tilde Q$. The
mathematics article *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions* writes the
symmetric half with the same symbol $\star$, because in that block it is the product; here the symbol
$\star$ stays with the fourth product, the symmetric half is written $\bullet$ and the antisymmetric half
$\diamond$, the symbol the menu comment renders $\wedge$. The reader moving between the two blocks should
carry the names $\mathrm{SQS}$ and $\mathrm{AQS}$ rather than the marks.

## The Exchange and the Two Parts

### Why the Bare Transposition Fails

The fourth product is $\mathbb{C}$-linear in its first slot and conjugate-linear in its second, so it is a
**sesqualgebra** product over the datum $(\mathbb{C},\bar{\cdot})$. Its two parts are not the two halves of
the bare transposition of its arguments. The bare transposition reverses the parity of the scalars — it is
conjugate-linear in the first slot and linear in the second — so its two halves are only
$\mathbb{R}$-bilinear operations and are not products of the class. The exchange has to be **adapted**: the
arguments are exchanged **and the value is conjugated**. With the coefficientwise conjugation
$\bar{\cdot}$ as the adapting conjugation,

$$
f^{\mathrm c}(\tilde P,\tilde Q)=\overline{f(\tilde Q,\tilde P)},
\qquad
f^{\mathrm s}=\tfrac12\bigl(f+f^{\mathrm c}\bigr),
\qquad
f^{\mathrm a}=\tfrac12\bigl(f-f^{\mathrm c}\bigr),
$$

the two parts are sesquilinear of the original parity again, each has the symmetry its name announces, and
the split is unique. The construction is *The Symmetric and Antisymmetric Parts of a Sesqualgebra
Product*, and it needs the exchange and not the transposition: **the split of a sesqualgebra product by the
adapted exchange keeps the sesqualgebra**.

### The Two Parts of the Fourth Product

For $f(\tilde P,\tilde Q)=\tilde P^{\natural}\tilde Q^{*}$ the adapted exchange is not a conjugation of the
value. The value does not determine the pair, and the swapped product read through the exchange gives the
**other order**, not a conjugation of the first. One computes

$$
\overline{\tilde Q^{\natural}\tilde P^{*}}=\tilde Q^{*}\tilde P^{\natural},
$$

so the symmetric and antisymmetric parts are the half-sum and the half-difference of the two orders
$\tilde P^{\natural}\tilde Q^{*}$ and $\tilde Q^{*}\tilde P^{\natural}$. The value of the fourth product
expands, on general elements, as

$$
\tilde P^{\natural}\tilde Q^{*}
=\bigl[P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})\bigr]
-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}+\mathbf{P}\times\overline{\mathbf{Q}},
$$

and the two orders differ by the sign of the cross term alone: the scalar part and the mixed term
$-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}$ are the same in both, and the cross products
$\mathbf{P}\times\overline{\mathbf{Q}}$ and $\overline{\mathbf{Q}}\times\mathbf{P}=-\mathbf{P}\times\overline{\mathbf{Q}}$
are opposite. The half-sum therefore keeps the scalar part and the mixed term and cancels the cross
product, and the half-difference keeps the cross product and nothing else:

$$
\tilde P\bullet\tilde Q=\bigl[P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})\bigr]
-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P},
\qquad
\tilde P\diamond\tilde Q=\mathbf{P}\times\overline{\mathbf{Q}}.
$$

**Remark (the trap of the whole block).** In the **plain** sesquilinear row the split is the
scalar/vector split of the one value: $\mathrm{SPS}=\mathrm{Sc}$ and $\mathrm{APS}=\mathrm{Vect}$
(*The Hermitian Form as a Product: Positivity and the Real Part of the Born Pairing*). **For the fourth
product it is not.** Here the antisymmetric part is one **piece** of the vector part, the cross term
$\mathbf{P}\times\overline{\mathbf{Q}}$, and the symmetric part keeps the rest — the scalar part and the
two mixed vector terms. The naive move, to call the scalar part of $\tilde P^{\natural}\tilde Q^{*}$ the
symmetric part and its vector part the antisymmetric part, is therefore wrong, and it is wrong by exactly
the two mixed terms. That error is the reason the symmetric half has a **non-central diagonal**, the
subject of *Values in No Subspace: Why the Symmetric Gauge Product Is Not a State*.

### The Twelve, and the Split's Place

The split is the quaternionic sesquilinear row of the catalogue of *The 12 Products of the Biquaternion Complex Space*: the symmetric part $\mathrm{SQS}$ and the antisymmetric part
$\mathrm{AQS}$ are two of the twelve operations, and the two are exactly the parts of the fourth product.
The reconstruction $\mathrm{GQS}=\mathrm{SQS}+\mathrm{AQS}$ is the uniqueness of the split read on the
products, and it was checked against the owner article and against the row table before it was written.

## The Value of the Symmetric Gauge Product

### The Scalar–Vector Form

**Theorem (the value).** For all biquaternions,

$$
\tilde P\bullet\tilde Q
=\bigl[P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})\bigr]-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P},
$$

with scalar part the Krein form $K(\tilde P,\tilde Q)=P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})$
and vector part the mixed term $-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}$.

*Proof.* The value of the fourth product is the display of §*The Two Parts of the Fourth Product*; the
swapped order has the same scalar part, because $\mathrm{Sc}(XY)=\mathrm{Sc}(YX)$ for the plain product,
and its cross term opposite, because $\overline{\mathbf{Q}}\times\mathbf{P}=-\mathbf{P}\times\overline{\mathbf{Q}}$;
the half-sum is the display. Verified on $100$ random pairs. $\square$

**Corollary (the two projections sit side by side).** The scalar part of the value is a complex multiple of
$e_0$ and the vector part is a complex vector in
$\mathrm{span}_{\mathbb{C}}\{e_1,e_2,e_3\}$; neither annihilates the other, and the two are read in the
same element. Neither is the whole of the value, and neither was assigned the name of a part by the split.

**The strain reading of the value.** The two projections have the shapes of the two elementary deformations of a frame, and the correspondence is exact. The scalar part is a **trace**, $K=\mathrm{Sc}(\tilde P\bullet\tilde Q)$, and a trace read on a frame is a **conformal factor**: it changes the scale and leaves the directions alone. The vector part is **traceless** — it is $-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}$ and carries no $e_0$ component — and a traceless symmetric part read on a frame is a **shear**: it changes the shape and leaves the volume. The symmetric gauge product is therefore read as a **frame-deformation operator**: its value is one scale and one shape, and the statement that the value lies in no subspace of the six is the statement that a genuine deformation mixes the two grades. The reading is bounded by the same caution as the theorem it dresses: one value has at most a scalar and a vector part, and it is the **image** of the operation, not one of its values, whose real span is the whole algebra.

**The mixed term as the sector-mixing term.** The vector part of the value is where the two sectors meet, and it is worth naming it. The vector part is $-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}$, and its components run over the six real directions of the vector subspace, three of them material ($e_k$) and three informational ($ie_k$); the scalar part $K$ couples only same-grade coefficients, and the mixed term is what couples the **scalar coefficient of one argument to the vector coefficients of the other**. The symmetric gauge product is therefore the algebraic seat of the framework's **matter–information mixing**: the term the corpus reads in the imaginary part of the biquaternion norm as the coupling of the material and informational sectors is carried here by the vector part of the value, and the **centrality criterion** of the band — $Q_0\overline{Q_k}\in i\mathbb{R}$ for every $k$ — is the **no-mixing** condition under which the coupling vanishes and the value returns to the centre. The name is the article's; the algebra of the term is the theorem above.

**The duality rotation is not the split.** A caution, because two operations of the corpus are easy to conflate here. Multiplication by the central imaginary $i$ is the **electric–magnetic duality rotation** of the field strength, and it exchanges the real and the imaginary sectors (*The Four Other Remarkable Subspaces*); it is **not** the symmetric-versus-antisymmetric split of a product, which is the exchange of the two arguments adapted to the class. The duality rotation is an operation on an element of the algebra; the split is an operation on a product of two. The two coincide on nothing in general, and the corpus keeps them apart.

### The Contrast with the Plain Sesquilinear Row

The two rows of sesqualgebra products are read against each other, and the contrast is one line.

| row | symmetric part | antisymmetric part | the symmetric value |
|---|---|---|---|
| plain sesquilinear $\mathrm{GPS}$ | $\mathrm{SPS}=\mathrm{Sc}(\tilde P\tilde Q^{*})=H(\tilde P,\tilde Q)$ | $\mathrm{APS}=\mathrm{Vect}(\tilde P\tilde Q^{*})$ | central, in $\mathbb{C}_{\mathbb{B}}$ |
| quaternionic sesquilinear $\mathrm{GQS}$ | $\mathrm{SQS}=\tilde P\bullet\tilde Q$ | $\mathrm{AQS}=\mathbf{P}\times\overline{\mathbf{Q}}$ | scalar part $K$, vector part the mixed term, in no subspace of the six |

The plain symmetric part is **central-valued** and its diagonal is the positive Hermitian form
$H(\tilde Q,\tilde Q)=\lvert Q_0\rvert^{2}+\lvert\mathbf{Q}\rvert^{2}$; the quaternionic symmetric part is
**not central-valued**, its scalar part is the **indefinite** form $K$, and its value lies in no one of the
six subspaces. This is the first appearance of the tension the band carries: the two symmetric
sesquilinear products do not divide the state side between them, because only one of the two has a
positivity to divide. The plain one is the state row; the quaternionic one is not.

## The Laws of the Operation

### Conjugate-Commutativity and Sesquilinearity

**Proposition.** The symmetric quaternionic sesquilinear product is **conjugate-commutative**,

$$
\tilde P\bullet\tilde Q=\overline{\tilde Q\bullet\tilde P},
$$

and it is sesquilinear over $(\mathbb{C},\bar{\cdot})$: $\mathbb{C}$-linear in the first slot and
conjugate-linear in the second.

*Proof.* The coefficientwise conjugation interchanges the two orders, $\overline{\tilde Q^{\natural}\tilde P^{*}}=\tilde Q^{*}\tilde P^{\natural}$
and $\overline{\tilde Q^{*}\tilde P^{\natural}}=\tilde Q^{\natural}\tilde P^{*}$, so it fixes the
half-sum; the scalar rules are those of the two orders read together, and the star in the second slot
supplies the conjugate-linearity. Verified on $100$ random pairs. $\square$

**Remark.** The symmetry is the one the construction announces and it is **not** commutativity. The
operation is neither commutative nor associative: the two-sided symmetry of a sesqualgebra product is
conjugate-commutativity, and associativity is not claimed by any of the twelve operations of the fourth
row.

### The Two One-Sided Actions and the Absence of a Unit

**Proposition (the two one-sided actions of $e_0$).** The identity of the plain product acts through the
two conjugations of the algebra,

$$
e_0\bullet\tilde Q=\tilde Q^{*},
\qquad
\tilde Q\bullet e_0=\tilde Q^{\natural}.
$$

*Proof.* At $\tilde P=e_0$ both orders of the fourth product coincide, $\tilde Q^{*}$, and the half-sum is
$\tilde Q^{*}$; the second display is the conjugate-commutative mirror. Verified on $100$ random elements.
$\square$

**Corollary (no unit).** There is no left unit and no right unit.

*Proof.* A left unit $\tilde E$ forces $\tilde E\bullet e_0=\tilde E^{\natural}=e_0$, hence
$\tilde E=e_0$, but $e_0\bullet e_1=-e_1$; a right unit would need $\tilde Q^{\natural}=\tilde Q$ for every
$\tilde Q$, which fails at $e_1$. $\square$

The absence of a unit is the algebra's statement that the operation is a **pairing** and not a
multiplication of the frame: a unit would supply a preferred element through which one argument could be
resolved against the other, and the two conjugations are exactly what forbids it. The two actions are the
conjugations, and no element of the algebra is neutral for both slots at once.

### The Failure of the Jordan Identity

**Proposition.** The symmetric quaternionic sesquilinear product **fails the Jordan identity**. At the
witness $x=y=e_1$ the two sides of the identity, $(x^{2}\bullet x)\bullet x$ and $x^{2}\bullet(x\bullet x)$,
are $-e_0$ and $e_0$.

*Proof.* The square is $e_1\bullet e_1=-e_0$, because $K(e_1,e_1)=-1$ and the mixed term vanishes at
$e_1$. Then $(-e_0)\bullet e_1=e_1$ and $(-e_0)\bullet(-e_0)=e_0$, so the two sides are
$e_1\bullet e_1=-e_0$ and $(-e_0)\bullet(-e_0)=e_0$. Verified on the witness. $\square$

**Remark (what the failure says and does not say).** The identity fails and the failure is witnessed on
the real basis, so unlike the antisymmetric half it is visible to a real-form computation. What fails is
the identity of a **Jordan product**; what is therefore not available is a Jordan algebra, a cone and a
state space reconstructed from the symmetric half, which is the content of *Why the Fourth Product Is a
Gauge Structure and Not a State Space* and is referred to it. The failure does not say that the operation
is useless: it says that its job is not the job of a state structure.

**The failure given a positive name.** The identity can be read forwards as well, and the reading is worth
the sentence. An operation whose Jordan identity held would be an **observable-like** multiplication: the
multiplication of a Jordan algebra, from which a cone, an order and a spectrum are read. The failure says
that the symmetric gauge pairing is therefore **curvature-like rather than probability-like** — it belongs
to the geometry of the frame and not to the algebra of its observables — so the failure is not only the
removal of a candidate state space but a statement of what the pairing is. The name is this article's; the
identity and its failure are the proposition above.

## The Metric Word, Earned

### The Krein Form as the Scalar Part

The scalar part of the value is the Krein form, and the physics of the row is the indefiniteness of that
form. On the diagonal,

$$
K(\tilde Q,\tilde Q)=\lvert Q_0\rvert^{2}-\sum_{k=1}^{3}\lvert Q_k\rvert^{2},
$$

positive on the centre and negative on the vector subspace, with the fundamental decomposition
$\mathbb{B}=\mathbb{C}_{\mathbb{B}}\oplus\mathrm{Vect}(\mathbb{B})$, the inertia $(1,3)$ over the complex
coefficients and $(2,6)$ over the real parameters, the isometry group $U(1,3)$, and the fundamental
symmetry $J={}^{\natural}$, the natural conjugation, that turns the indefinite form into the definite one.
The metric itself, its signature and its Klein–Gupta–Bleuler reading are *The Fourth Product and Its
Indefinite Metric*; the form read as the multiplication of the block, with its two Gram matrices, its
isotropic elements, its restriction to the six subspaces and its invariance under the block, is *The Krein
Form as a Product on the Symmetric Quaternionic Sesqualgebra*; and here the point is only that the pairing
is **a product**, and that the product's scalar part is where the metric lives.

**The reading of the operation.** The corpus reads the symmetric half as the **invariant indefinite
pairing of the gauge structure**: the pairing that belongs to the transformation side of the frame, the
side whose invariants are the pairings left unchanged, as opposed to the state side whose invariants are
positive numbers. That the pairing is the invariant one, and which transformations leave it alone, are
*The Gauge Principle in Biquaternionic Form*, *Gauge Transformations of the First and Second Kind in
Biquaternionic Form* and *Gauge Redundancy and the Information in the Gauge Orbit in Biquaternionic
Form*; the algebraic statement that the block leaves $K$ invariant is *The Krein Form as a Product on the
Symmetric Quaternionic Sesqualgebra*; the operator face of the same invariance is *Observables, Gauge
Generators and the Chirality of the Internal Action*. This article states the reading and defers the
transformation theory to those articles.

### What the Word Metric Does Not Mean

Four cautions bound the reading, and they are the ledger's own.

1. **An indefinite pairing is a metric in the algebraic sense and not a norm.** There is no positivity, no
   distance and no length: $K(e_1,e_1)=-1$ and $K(e_0,e_0)=+1$, and a negative squared length is a datum
   and not an error.

2. **The vanishing of the form is not a pathology.** The null set $\{K=0\}$ is a real cone of dimension
   seven, it contains $e_0+e_1$, and it contains the pure states (*The States the Indefinite Metric Cannot
   Normalise*). A null element is a fact about one form.

3. **The metric is not the state-space inner product.** The states are normalised by the positive definite
   form $H$, not by $K$; the positivity of $H$ and the absence of ghosts are *Mass, Rank and the
   Positivity of the Dagger*, and the two forms are not interchangeable.

4. **No scale is attached here.** The algebra has no scale; the coupling, the charge and $\hbar$ enter at
   the physical reading, in the places the corpus has already fixed (*Action, Units, and the Constants of
   the Biquaternion Universe*). The Krein form is a structure, not a dimensionful metric.

## One Insertion, Read Twice

The fourth product is the product whose **first slot carries the natural conjugation**, and the
first-slot insertion is the single mechanism behind the two facts of this block. Inserting ${}^{\natural}$
into the first slot of the plain sesquilinear row replaces the definite form $H$ by the **indefinite** form
$K$ — that is the metric — and inserting it into the first slot of the plain product spoils the closure of
the bracket, since the plain antisymmetric part $\mathrm{APA}$ is a Lie bracket and its first-slot
conjugation $\mathrm{AQA}$ is not. The **metric and the obstruction are one insertion read twice**, in the
precise sense that the first-slot insertion produces the metric outright and spoils the closure of the
*plain* bracket; the reading is offered as the framework's grouping and labelled as such, and it does not
claim that the closure failure is the first slot's alone — the paragraph below records that the second slot
spoils it a second time, so the metric is the first slot's work and the non-closure is shared.

The statement is bounded on two sides. An **indefinite** metric is not an unphysical metric: the pairing
is the object the gauge side needs, and the states of the framework live on the plain row and not here.
And a **failure to close** is not a failure of the gauge theory: the theory is carried by the pairing and
by the gauge articles cited above, not by the bracket. The second-slot star spoils the closure a second
time — the plain sesquilinear antisymmetric part $\mathrm{APS}$ fails the identity as well — so the full
fourth product is spoiled on both slots, while the metric is the work of the first.

## A Worked Pair

The symmetric half is read on the two witness pairs of the block, chosen so that the two orders of the
fourth product are respectively coincident and opposite.

| $(\tilde P,\tilde Q)$ | $\tilde P^{\natural}\tilde Q^{*}$ | $\tilde Q^{*}\tilde P^{\natural}$ | $\tilde P\bullet\tilde Q$ | $\tilde P\diamond\tilde Q$ |
|---|---|---|---|---|
| $(-ie_3,\,-ie_0)$ | $-e_3$ | $-e_3$ | $-e_3$ | $0$ |
| $(e_2,\,e_1)$ | $-e_3$ | $+e_3$ | $0$ | $-e_3$ |

At the first pair the two orders coincide, the antisymmetric half vanishes, and the symmetric half is the
order alone. At the second the two orders are opposite, the symmetric half vanishes, and the value of the
fourth product is the antisymmetric half alone. The same two pairs are read in *The Non-Central Diagonal
and the Two Halves of the Symmetric Quaternionic Sesqualgebra*, and they show that neither half is a
function of the other.

A third value stays in the reader's eye for the band that follows. On the element $e_0+e_1$ the diagonal
of the symmetric half is

$$
(e_0+e_1)\bullet(e_0+e_1)=-2e_1,
$$

because $K(e_0+e_1,e_0+e_1)=0$ and the mixed term is $-2e_1$. The value is a vector, it is not a complex
multiple of $e_0$, and it is therefore **not central**: the diagonal of the symmetric gauge product leaves
the centre, and that fact is the whole of the second article of the band.

## Named Readings of the Symmetric Half

Four further readings of the symmetric gauge product are recorded here, each under a name of its own and each labelled a reading rather than a theorem; the identities they rest on are the body's.

- **Swap-conjugation symmetry.** The product is conjugate-commutative rather than commutative, so its values pair an element with the conjugate of the other; read physically, the pairing defines a **frame read in the conjugate**, and the ordering of the two arguments is immaterial while the conjugation is not. The name is the symmetric-half counterpart of §*The Bracket as an Anti-Linear Pairing* of *The Cross Product of a Vector with Its Conjugate: the Antisymmetric Gauge Product*: there the conjugation makes the pairing antisymmetric, here it makes the pairing symmetric. The name is not **conjugate frame**, which the corpus already uses for the anti-holomorphic frame of a complex manifold.
- **Lightlike pairing.** The scalar part of the value is $K(\tilde P,\tilde Q)$, and a pair with vanishing scalar part, $K(\tilde P,\tilde Q)=0$, is read as a **lightlike (null) pair** of the gauge frame: the pairing-level shadow of the zero-divisor condition, since the scalar part of the value is exactly $K$ and the cone of the interval is $\{N=0\}$. The name is chosen to avoid the corpus's word **eikonal**, which is reserved for the short-wavelength equation on a phase, $(\nabla\varphi)^{2}=\alpha^{2}$, of *The WKB Approximation and the Hamilton–Jacobi Equation in Biquaternionic Form* and of *Maxwell's Equations in Chiral Media — The Quaternionic Reformulation*; the relation between the two is that both express the zero-divisor (light-cone) condition, there on a gradient and here on a pair. The reading is the pairing-level counterpart of the null states, and its boundary is the article's: the algebra supplies the vanishing of the scalar part and no wave, no front and no propagation.
- **Frame strain.** The value is read as a **deformation of the frame**, its scalar part a conformal factor and its traceless vector part a shear, so that the symmetric half is the product that deforms an element rather than rotating it. The reading is stated in §*The Metric Word, Earned* in the language of the frame-deformation operator and is repeated here as a named reading so that it can be cited; the boundary is that no elastic or continuum model stands behind the name.
- **Internal volume form.** The trace pairing of the row, $\mathrm{Tr}(\tilde P\bullet\tilde Q)=2\,\mathrm{Sc}(\tilde P\bullet\tilde Q)=2K(\tilde P,\tilde Q)$, is read as an **internal volume** of the gauge frame: an isometry of $K$ preserves the pairing, and the volume-preserving subgroup in the matrix model is $SU(1,3)\subset SL(4,\mathbb{C})$, while a general isometry of $U(1,3)$ has determinant of modulus one and need not preserve the determinant. The name separates the volume reading from the metric reading of the same form, and the boundary is that the algebra supplies the trace and the two groups and no measured volume.

## The Limits

- **The article does not supply the metric.** The signature, the inertia, the fundamental symmetry and the
  isometry group are *The Fourth Product and Its Indefinite Metric*; the restrictions to the six subspaces
  are *The Krein Gram Matrix and the Restrictions of the Form*. This article reads the symmetric half as a
  product and locates the metric in its scalar part.
- **The article does not claim positivity.** The operation has an indefinite scalar part, and the
  positivity of the framework lives on the plain sesquilinear row and not here. The two symmetric
  sesquilinear products are not two halves of one state structure.
- **The article does not claim a gauge algebra.** The symmetric half is not a Lie structure, and the
  antisymmetric half fails the Jacobi identity, so no gauge algebra is read from either; the negative
  reading is referred to *The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2) but Not
  SU(3)* and to *The Cross Product of a Vector with Its Conjugate: the Antisymmetric Gauge Product*.
- **The invariance reading is a reading.** That the pairing is *the* invariant pairing of the gauge side is
  the framework's grouping, stated as such and not proved here; the transformation theory that makes it
  precise is cited and not restated.

## The Ledger

**Proved, and recomputed.** The fourth product expands as
$\tilde P^{\natural}\tilde Q^{*}=[P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})]-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}+\mathbf{P}\times\overline{\mathbf{Q}}$;
its two orders differ only in the sign of the cross term; the half-sum is
$\tilde P\bullet\tilde Q=[P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})]-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}$
and the half-difference is $\mathbf{P}\times\overline{\mathbf{Q}}$; the two parts reconstruct the fourth
product. The symmetric half is conjugate-commutative, sesquilinear over $(\mathbb{C},\bar{\cdot})$ and
neither commutative nor associative; $e_0\bullet\tilde Q=\tilde Q^{*}$ and
$\tilde Q\bullet e_0=\tilde Q^{\natural}$, so there is no unit on either side; it fails the Jordan identity
at $x=y=e_1$, with the two sides $-e_0$ and $e_0$; its diagonal at $e_0+e_1$ is $-2e_1$, not central; its
value lies in no one of the six subspaces for a general pair and the real span of its values is the whole algebra. Recomputed on $100$
random pairs and on the named witnesses, and reproduced from *Introduction to the Symmetric Quaternionic
Sesqualgebra of Biquaternions*, *The Non-Central Diagonal and the Two Halves of the Symmetric Quaternionic
Sesqualgebra*, *The Six Subspaces under the Symmetric Quaternionic Sesqualgebra of Biquaternions* and *The 12 Products of the Biquaternion Complex Space*.

**Reading.** That the symmetric half is the invariant indefinite pairing of the gauge structure, that its
scalar part is the Krein form and its vector part the mixed term, and that the two projections of its
value sit side by side in one element. Three further names for the same facts, each a reading: the value
read as a **frame-deformation operator**, the scalar part a conformal factor and the traceless vector part
a shear; the mixed term read as the **sector-mixing term**, so that the centrality criterion of the band
is the no-mixing condition; and the failure of the Jordan identity read forwards, so that the pairing is
**curvature-like rather than probability-like**. The same ledger carries the caution that the duality
rotation by the central imaginary is not the symmetric–antisymmetric split of a product. Four further
readings, named in §*Named Readings of the Symmetric Half*: **swap-conjugation symmetry**, **lightlike
pairing**, **frame strain** and **internal volume form**.

**Not claimed.** That the metric is a norm or a distance; that the form's vanishing makes an element
unphysical; that the operation supplies a state space, a Jordan structure or a gauge algebra; that a
particular transformation group beyond the cited articles leaves the pairing invariant.

## Physical Readings

The gauge metric reads as the pairing of the transformations rather than of the states, and its signature is the reading of the gauge side: it is indefinite, so it selects no direction of positivity, which is why a gauge calibration can compare two internal frames and cannot rank them. Read for invariance, this is the second member of the invariant pair: the sesquilinear row of the grid is what a change of the local complex structure does not move, so the gauge metric and the probability form travel together while the interval and the composition do not.

## Summary

The symmetric quaternionic sesquilinear product is the symmetric half of the fourth product under the
class-preserving exchange, and it is the half that keeps the scalar part and the mixed vector term while
the antisymmetric half takes the cross term alone. Its value is
$[P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})]-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}$,
of scalar part the Krein form $K$ and vector part the mixed term; the two projections sit side by side and
neither annihilates the other. The operation is **conjugate-commutative** and sesquilinear over
$(\mathbb{C},\bar{\cdot})$, it is neither commutative nor associative, it has **no unit** — the two
one-sided actions of $e_0$ are the two conjugations — and it **fails the Jordan identity** at
$x=y=e_1$, where the two sides are $-e_0$ and $e_0$. Its diagonal at $e_0+e_1$ is $-2e_1$, off the centre,
and its values lie in no one of the six subspaces for a general pair. The **metric word is earned** as the indefiniteness of
the scalar part: $K$ has the signature $(1,3)$ over the complex coefficients, positive on the centre and
negative on the vector subspace, with fundamental symmetry ${}^{\natural}$ and isometry group $U(1,3)$. It
is **not** earned as a norm: the pairing has no positivity, no distance and no length, and the metric is
not the state-space inner product. The corpus reads the operation as the **invariant indefinite pairing
of the gauge structure**, on the transformation side of a frame whose state side is the plain sesquilinear
row; the contrast with the plain symmetric part, which is central-valued and positive on its diagonal, is
the reason the two symmetric sesquilinear products do not divide the state side between them.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\bullet\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q^{*}+\tilde Q^{*}\tilde P^{\natural})$ | the symmetric quaternionic sesquilinear product, $\mathrm{SQS}$ |
| $\tilde P\diamond\tilde Q=\mathbf{P}\times\overline{\mathbf{Q}}$ | the antisymmetric part, $\mathrm{AQS}$, read in the companion article |
| $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q^{*}$ | the fourth product, whose parts the two are |
| $\tilde P\bullet\tilde Q=[P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})]-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}$ | the value; scalar part $K$, vector part the mixed term |
| $K(\tilde P,\tilde Q)=P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})$ | the Krein form; $\varepsilon=(1,-1,-1,-1)$ |
| $e_0\bullet\tilde Q=\tilde Q^{*}$, $\tilde Q\bullet e_0=\tilde Q^{\natural}$ | the two one-sided actions; no unit |
| $x=y=e_1$; the sides $-e_0$, $e_0$ | the witness of the Jordan failure |
| $(e_0+e_1)\bullet(e_0+e_1)=-2e_1$ | the non-central diagonal |
| $(-ie_3,-ie_0)$; $(e_2,e_1)$ | the coincident and the opposite orders |
| $H$ and $K$ | the definite probability form and the indefinite gauge pairing |

## Further Reading

- Mathematics article *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-sesqualgebra-of-biquaternions.md`), for the product, its class and its scalar–vector form.
- Mathematics article *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product* (`articles_maths/the-symmetric-and-antisymmetric-parts-of-a-sesqualgebra-product.md`), for the adapted exchange, the two parts and the reconstruction.
- Mathematics article *The 12 Products of the Biquaternion Complex Space* (`articles_maths/the-12-products-of-the-biquaternion-complex-space.md`), for the names SQS and AQS, their laws and the witnesses.
- Mathematics article *The Non-Central Diagonal and the Two Halves of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/the-non-central-diagonal-and-the-two-halves-of-the-symmetric-quaternionic-sesqualgebra.md`), for the diagonal, the two orders and the absence of a unit.
- Mathematics article *The Krein Gram Matrix and the Restrictions of the Form* (`articles_maths/the-krein-gram-matrix-and-the-restrictions-of-the-form.md`), for the form $K$ and its restrictions.
- Mathematics article *The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra* (`articles_maths/the-krein-form-as-a-product-on-the-symmetric-quaternionic-sesqualgebra.md`), for the form read as the multiplication of the block, its two Gram matrices, its isotropic elements and its invariance under the block.
- Companion article *The Fourth Product and Its Indefinite Metric*, for the metric whose scalar part this product carries.
- Companion article *The States the Indefinite Metric Cannot Normalise*, for the states that are null for that metric.
- Companion article *The Four General Products and Their Physical Readings*, for the map of the four general products and the four jobs.
- Companion article *Mass, Rank and the Positivity of the Dagger*, for the positivity of the probability form and the state cone.
- Companion article *The Cross Product of a Vector with Its Conjugate: the Antisymmetric Gauge Product*, for the antisymmetric half of the same row.
- Companion article *The WKB Approximation and the Hamilton–Jacobi Equation in Biquaternionic Form* (`articles_physics/the-wkb-approximation-and-the-hamilton-jacobi-equation-in-biquaternionic-form.md`), named for the eikonal equation that the **lightlike pairing** reading does not claim.
- Companion article *Maxwell's Equations in Chiral Media — The Quaternionic Reformulation* (`articles_physics/maxwells-equations-in-chiral-media-the-quaternionic-reformulation.md`), named for the same word.
