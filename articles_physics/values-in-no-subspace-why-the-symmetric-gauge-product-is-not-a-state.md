# __Values in No Subspace: Why the Symmetric Gauge Product Is Not a State__

## Introduction

A product is read physically through the subspace its values occupy. The plain product of the algebra
returns an element of the algebra; the quaternionic product returns a multiple of the identity; the
sesquilinear product returns a central number; the symmetric plain sesquilinear product, in particular,
returns a **central** element, and its diagonal is the positive Hermitian form that the framework uses as
its probability. The symmetric half of the fourth product, $\tilde P\bullet\tilde Q$ of *The Gauge Metric
as a Product: the Symmetric Quaternionic Sesquilinear Product*, does something else. Its value carries a
complex scalar part and a complex vector part side by side, and it lies in **no one of the remarkable subspaces** of the algebra. That single fact is why the band's product is **not a state**.
This article states it, computes the non-central diagonal that goes with it, and sets it against the plain
symmetric sesquilinear product, which is central-valued and positive and which is the state row.

The article owns the subspace reading of the symmetric half: where its values lie, where its diagonal
lies, and the contrast that follows. It defers the remarkable subspaces themselves and their decompositions to
*Relations Between Subspaces* and *Other Remarkable Subspaces*; the closure of the remarkable subspaces under the
product to the mathematics article *Remarkable Subspaces under the Symmetric Quaternionic Sesqualgebra of
Biquaternions*; the form $K$ and its restrictions to *The Krein Gram Matrix and the Restrictions of the
Form*; the diagonal as an element to *The Non-Central Diagonal and the Two Halves of the Symmetric
Quaternionic Sesqualgebra*; and the state side to *Mass, Rank and the Positivity of the Dagger* and *Why
the Fourth Product Is a Gauge Structure and Not a State Space*.

**Conventions.** As in the companion articles of this block:
$\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$, $e_0=1$,
$e_k^{2}=-e_0$, $e_1e_2=e_3$, central $i$; $\tilde Q=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$,
scalar part $\mathrm{Sc}(\tilde Q)=Q_0$, vector part $\mathbf{Q}=\sum_kQ_ke_k$; the natural conjugation
$\tilde Q^{\natural}=Q_0e_0-\mathbf{Q}$ and the star $\tilde Q^{*}=\overline{\tilde Q^{\natural}}$;
$(\mathbf{P},\mathbf{Q})=\sum_kP_kQ_k$; the block's product is
$\tilde P\bullet\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q^{*}+\tilde Q^{*}\tilde P^{\natural})=[P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})]-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}$;
the Krein form is $K(\tilde P,\tilde Q)=P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})$ with
$\varepsilon=(1,-1,-1,-1)$; the sectors are $\mathbb{M}_+=\{Q^{*}=Q\}$ and
$\mathbb{M}_-=\{Q^{\flat}=Q\}$, with $\flat=-{}^{*}$. All conventions are those of *Conventions in the
Biquaternion Universe*.

## Remarkable Subspaces, Named

The phrase *in no subspace* means nothing until the remarkable subspaces are named. The algebra is eight-dimensional over
$\mathbb{R}$, and it carries remarkable real subspaces, the fixed and anti-fixed spaces of the
three commuting involutions.

| subspace | real dim | defining condition | basis |
|---|---|---|---|
| centre $\mathbb{C}_{\mathbb{B}}$ | $2$ | central | $\{e_0,ie_0\}$ |
| vector subspace $\mathrm{Vect}(\mathbb{B})$ | $6$ | $Q_0=0$ | $\{e_1,e_2,e_3,ie_1,ie_2,ie_3\}$ |
| real quaternion $\mathbb{H}_{\mathbb{B}}$ | $4$ | $Q_\mu$ real | $\{e_0,e_1,e_2,e_3\}$ |
| antiquaternion $i\mathbb{H}_{\mathbb{B}}$ | $4$ | $Q_\mu$ purely imaginary | $\{ie_0,ie_1,ie_2,ie_3\}$ |
| informational $\mathbb{M}_+$ | $4$ | $Q_0$ real, $\mathbf{Q}$ purely imaginary | $\{e_0,ie_1,ie_2,ie_3\}$ |
| material $\mathbb{M}_-$ | $4$ | $Q_0$ purely imaginary, $\mathbf{Q}$ real | $\{ie_0,e_1,e_2,e_3\}$ |

The remarkable subspaces are the fixed spaces of the involutions ${}^{\natural}$, $-{}^{\natural}$, $\bar{\cdot}$,
$-\bar{\cdot}$, ${}^{*}$ and $\flat$ (*Relations Between Subspaces*), and each carries the product in its
own way. The centre, the real quaternion subspace and the informational sector are **closed**; the vector
subspace maps into the centre, the antiquaternion subspace into the real quaternion subspace, and the
material sector into the informational sector; and the image of the product is not confined to any of
them — the real span of its values is the **whole algebra**. The closure table is *Remarkable Subspaces under the
Symmetric Quaternionic Sesqualgebra of Biquaternions* and is cited, not re-derived.

## The Value Lies in No Subspace

**Theorem (the value is in no subspace).** For a general pair the value $\tilde P\bullet\tilde Q$ lies in
none of the remarkable subspaces.

*Proof.* The value is
$[P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})]-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}$.
It is not in the centre unless its vector part vanishes, and it is not in the vector subspace unless its
scalar part vanishes; a general pair has both nonzero. Its coefficients are not all real, so it is not in
$\mathbb{H}_{\mathbb{B}}$; not all purely imaginary, so not in $i\mathbb{H}_{\mathbb{B}}$; it does not have
a real scalar coefficient with a purely imaginary vector part, so it is not in $\mathbb{M}_+$; and it does
not have a purely imaginary scalar coefficient with a real vector part, so it is not in $\mathbb{M}_-$.
Each obstruction is open, so a general pair fails all six. $\square$

**Worked witness.** Take $\tilde P=(1+i)e_0$ and $\tilde Q=e_0+e_1$. Here $P_0=1+i$, $\mathbf{P}=0$,
$Q_0=1$, $Q_1=1$, so

$$
\tilde P\bullet\tilde Q=(1+i)e_0-(1+i)e_1=(1+i)(e_0-e_1).
$$

The scalar part $1+i$ is neither real nor purely imaginary, and the vector part $-(1+i)e_1$ is nonzero, so
the value is in none of the remarkable subspaces. Verified on the witness and on $100$ random pairs with distinct
arguments, all of which gave a value outside all six.

**What the theorem does and does not say.** It says that the image of the product is contained in no one of
the remarkable subspaces. It does **not** say that every value is outside every subspace: at
$\tilde P=e_0$ the value is the star, $\tilde Q^{*}$, which lies in the informational sector; at a pair
of vectors the value can lie in the centre; and every **diagonal** value $\tilde Q\bullet\tilde Q$ is a real
quaternion and so lies in $\mathbb{H}_{\mathbb{B}}$, a fact the next section uses. The datum is about the
operation's image and not about each value, and it is a datum about the algebra: nothing unphysical is
claimed of any value by it.

## The Diagonal Is Not Central

The diagonal carries the same obstruction in a sharper form, and it is the sharpest statement of the band.

**Theorem (the diagonal).** For every biquaternion,

$$
\tilde Q\bullet\tilde Q=K(\tilde Q,\tilde Q)e_0-Q_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{Q},
\qquad
K(\tilde Q,\tilde Q)=\lvert Q_0\rvert^{2}-\sum_{k=1}^{3}\lvert Q_k\rvert^{2},
$$

with real scalar part and real vector part $-2\sum_k\mathrm{Re}(Q_0\overline{Q_k})e_k$.

*Proof.* Put $\tilde P=\tilde Q$ in the value: the scalar part is $\lvert Q_0\rvert^{2}-\sum_k\lvert Q_k\rvert^{2}$,
real, and the vector part is $-Q_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{Q}=-2\mathrm{Re}(Q_0\overline{\mathbf{Q}})$,
real. $\square$

**Theorem (criterion of centrality).** The diagonal lies in the centre exactly when
$Q_0\overline{Q_k}\in i\mathbb{R}$ for every $k$, that is, when the vector $Q_0\overline{\mathbf{Q}}$ is
purely imaginary; in particular on the whole vector subspace, where $Q_0=0$.

*Proof.* The centre is $\mathbb{C}e_0$, so the diagonal is central exactly when its vector part vanishes,
and its $k$-th component is $-2\mathrm{Re}(Q_0\overline{Q_k})$. $\square$

The criterion is the reason the naive reading of the witnesses fails, and the point deserves to be stated
plainly. On the **real vector directions** the diagonal is central: at $e_1$ the form is
$K(e_1,e_1)=-1$ and the mixed term vanishes, so

$$
e_1\bullet e_1=-e_0,
$$

a central value. The same holds at $e_1+ie_2$, where the diagonal is $-2e_0$, again central. Those
directions are **not** witnesses of non-centrality, because the whole vector subspace carries a central
diagonal; they are witnesses of the indefiniteness of the form. The element that exhibits the block's own
obstruction is a sum of a scalar and a vector direction,

$$
(e_0+e_1)\bullet(e_0+e_1)=-2e_1,
$$

because there $K=0$ and $Q_0\overline{Q_1}=1$ is real and not purely imaginary, so the mixed term
$-2e_1$ survives. **That** is the value that leaves the centre, and it is the diagonal of the block that is
not central.

**The criterion read as a no-mixing condition.** The criterion of centrality has an immediate physical name, and the name is the point of this paragraph. The diagonal of an element is central exactly when the pairing of the element with itself returns a **pure scale** and no direction, and the criterion is therefore a **no-mixing condition**: it says that the element's own self-pairing mixes no grade. The reading is exact on the two named elements. On the vector directions — $e_1$, and $e_1+ie_2$ — the diagonal is central, $-e_0$ and $-2e_0$, so the self-pairing of those elements is a pure scale (the form there is still indefinite: $K(e_1,e_1)=-1$, $K(e_2,e_2)=-1$), which is why they witness the *indefiniteness* of the form and not its non-centrality. On $e_0+e_1$, the smallest element that is neither a pure scalar nor a pure vector, the diagonal is $-2e_1$, off the centre, and the self-pairing **mixes** the scalar grade into the vector grade: the pairing rotates its diagonal into a spatial direction. Read on a medium, a no-mixing pairing responds by a pure scale, and a non-central diagonal is the algebraic trace of a **birefringent** response, in which a direction is produced rather than merely scaled. The algebra is the criterion above; the no-mixing and birefringence names are this article's reading, and they are offered as such. The name is *not* the word isotropic: an isotropic element in the sense of a form is a null element, and the vector directions here have $K(e_k,e_k)=-1$, not $0$.

## The Contrast with the Plain Sesquilinear Row

The contrast is one table, and it is the whole difference between a state row and a gauge row.

| | symmetric plain sesquilinear $\mathrm{SPS}$ | symmetric quaternionic sesquilinear $\mathrm{SQS}$ |
|---|---|---|
| rule | $\tfrac12(\tilde P\tilde Q^{*}+\overline{\tilde Q}\tilde P^{\natural})=\mathrm{Sc}(\tilde P\tilde Q^{*})$ | $\tfrac12(\tilde P^{\natural}\tilde Q^{*}+\tilde Q^{*}\tilde P^{\natural})$ |
| value | central, $H(\tilde P,\tilde Q)=P_0\overline{Q_0}+(\mathbf{P},\overline{\mathbf{Q}})$ | scalar part $K$, vector part the mixed term; in no subspace |
| diagonal | $H(\tilde Q,\tilde Q)=\lvert Q_0\rvert^{2}+\lvert\mathbf{Q}\rvert^{2}$, positive off zero | $K(\tilde Q,\tilde Q)e_0-Q_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{Q}$, indefinite, not central in general |
| diagonal subspace | the centre | the centre only when $Q_0\overline{Q_k}\in i\mathbb{R}$ for each $k$ |
| reading | the probability form $H$; the state side | the indefinite pairing of the gauge side |

The plain symmetric part **compares two elements and returns a positive number**: its value is central
precisely so that it can be read as a probability, and its diagonal is strictly positive off the origin.
The quaternionic symmetric part returns an element that is not central and whose scalar part is indefinite:
it can be read as a **pairing**, and it cannot be read as a probability. The two are not two halves of one
state structure — one carries the positivity and the other carries the signature — and the corpus states
this as the reason the **two symmetric sesquilinear products do not divide the state side between them**.

## Why That Is *Not a State*

The words have exact content in the framework, and they are worth spelling out because the negative form
of the statement is easy to over-read.

**A state is a positive trace-one element of the informational sector for the form $H$.** The cone of
states is a cone because $H$ is positive definite; the pure states are its rank-one projectors, the Bloch
sphere; and the Born rule is a ratio of two positive numbers. Everything in that description uses the
positivity of $H$, and none of it uses the block's product. The positivity itself is *Mass, Rank and the
Positivity of the Dagger*.

**The block's product supplies none of the four ingredients.** Its scalar part is indefinite, so its
diagonal orders nothing; its values lie in no subspace, so there is no fixed space over which a cone could
be defined; it has no unit, so there is no trace slice of the kind a state space uses; and the ternary
product built from the fourth product fails the Jordan triple identity, so the standard reconstruction of a
state space from a ternary product does not reach it. The last statement is the no-go of *Why the Fourth
Product Is a Gauge Structure and Not a State Space*, and it is the reason the negative reading is not a
defect of this article's product alone but of the whole fourth corner.

**What the block is instead.** It is the **gauge** side of the frame: a pairing that the transformations of
the gauge structure leave alone, carried by a product whose two halves are a symmetric pairing and a
bracket. The reading is the framework's and is offered as such; the transformation theory is *The Gauge
Principle in Biquaternionic Form* and the companion gauge articles, and the antisymmetric half of the
products of the same row is *The Cross Product of a Vector with Its Conjugate: the Antisymmetric Gauge
Product*.

### Named Readings of the Value

Three further readings of the same theorem are recorded here, each under a name of its own and each labelled a reading rather than a theorem; the theorem they name is the body's.

- **Sector correlation.** That the value leaves all remarkable subspaces is read positively as a **correlation between sectors**: an element outside every remarkable subspace is one that no single sector can hold, so the symmetric gauge product couples the sectors rather than staying inside one. The name is the positive face of the theorem, and its boundary is the article's: the algebra supplies the escape, and it supplies no measure of the correlation.
- **Mixing generator.** The element $e_0+e_1$ is the **minimal mixing element**, and its non-central diagonal $-2e_1$ witnesses the mixing; the centrality criterion $Q_0\overline{Q_k}\in i\mathbb{R}$ is the no-mixing condition. The reading is the value-side counterpart of the sector-mixing term of *The Gauge Metric as a Product: the Symmetric Quaternionic Sesquilinear Product*, named here because it is the element that carries it.
- **No state by locality.** The absence of the value from every subspace is read as an obstruction of a **local** kind to the state reading: a state is localised in a sector — the informational sector — and a value that is in no sector cannot be localised there, so it is not a state. The name keeps the negative reading attached to a locality condition on the value rather than to a defect of the product, and it is the sharpest form of the article's *not a state* conclusion.

## The Limits

- **A value in no subspace is a datum about the algebra and not a claim that the object is unphysical.**
  The theorem has no physical negative content: it says that the value is not confined to a remarkable subspace, and it does not say that the value is not a perfectly good element of the algebra.
- **An indefinite scalar part is a signature and not a failure.** The Krein form is the object the gauge
  side needs; its indefiniteness is the metric and not a defect of the product that carries it.
- **The diagonal that is not central is not a pathology.** The non-centrality is the algebraic trace of the
  two mixed terms that the split of the fourth product leaves in the symmetric half; the antisymmetric
  half has taken the cross term, and the rest remains.
- **The article does not superpose the two symmetric products.** The plain one is the state row and the
  quaternionic one is not; neither is a correction of the other, and the corpus keeps the names apart.

## The Ledger

**Proved, and recomputed.** The value of the symmetric quaternionic sesquilinear product lies in no one of
the remarkable subspaces for a pair of distinct generic arguments, and the real span of its values is the whole algebra; the
witness $\tilde P=(1+i)e_0$, $\tilde Q=e_0+e_1$ gives $(1+i)(e_0-e_1)$ outside all six, and $100$ random
pairs with distinct arguments gave $100$ values outside all six. The diagonal is an exception of a definite
kind: it is always a real quaternion, hence always in $\mathbb{H}_{\mathbb{B}}$, and never leaves it. The
diagonal is
$K(\tilde Q,\tilde Q)e_0-Q_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{Q}$, central exactly when
$Q_0\overline{Q_k}\in i\mathbb{R}$ for each $k$; at $e_1$ it is $-e_0$ and at $e_1+ie_2$ it is $-2e_0$,
both central, and at $e_0+e_1$ it is $-2e_1$, not central. The plain symmetric sesquilinear product is
central-valued and its diagonal is $H(\tilde Q,\tilde Q)=\lvert Q_0\rvert^{2}+\lvert\mathbf{Q}\rvert^{2}$,
positive off the origin. Recomputed on the named witnesses and on $100$ random pairs, and reproduced from
*Remarkable Subspaces under the Symmetric Quaternionic Sesqualgebra of Biquaternions*, *The Non-Central
Diagonal and the Two Halves of the Symmetric Quaternionic Sesqualgebra* and *The Krein Gram Matrix and the
Restrictions of the Form*.

**Reading.** That the gauge pairing separates no state, and that the two symmetric sesquilinear products do
not divide the state side between them; and, on the criterion of centrality, that the criterion is a
**no-mixing condition**, so that the self-pairing of the vector directions returns a pure scale while the
element $e_0+e_1$ is the minimal **mixing** element, its non-central diagonal the algebraic trace of a
birefringent response. The word isotropic is avoided here: an isotropic element of a form is a null
element, and the vector directions have $K(e_k,e_k)=-1$. Three further readings, named in §*Named Readings of the Value*: **sector correlation**, **mixing generator** and **no state by locality**.

**Not claimed.** That a value in no subspace is unphysical; that the indefinite form makes an element
unphysical; that the block's product is a correction of the plain one; that a state space can be
reconstructed from the block.

## Physical Readings

The values lying in no subspace read as the framework's criterion for what can be an observable: an object whose diagonal is not central cannot be counted, so a symmetric gauge product is a structure and not a quantity. The article's examples are the reading in one line: the minimal mixing element $\tilde Q = e_0 + e_1$ has the non-central diagonal $-2e_1$, while a pure vector direction has a central one, so the slightest mixing is enough to leave the class of what can be measured. Read on the split, the criterion is the same one that separates the gauge side from the state side.

## Summary

The symmetric quaternionic sesquilinear product has values in **no one of the remarkable subspaces** of the
algebra: its value carries the scalar part $K$ and the vector part $-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}$
side by side, and the real span of its values is the whole algebra. Its diagonal
$\tilde Q\bullet\tilde Q=K(\tilde Q,\tilde Q)e_0-Q_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{Q}$ is
central exactly when $Q_0\overline{Q_k}\in i\mathbb{R}$ for each $k$, in particular on the whole real
vector subspace: at $e_1$ and at $e_1+ie_2$ it is the central value $-e_0$ and $-2e_0$, and the non-central
witness is $e_0+e_1$, whose diagonal is $-2e_1$. The **contrast with the plain symmetric sesquilinear
product**, which is central-valued with a strictly positive diagonal $H(\tilde Q,\tilde Q)$, is what makes
the block's product **not a state**: it has no positivity, no fixed subspace, no unit and no Jordan triple,
and the standard reconstruction of a state space therefore does not reach it. It is instead the
**invariant indefinite pairing of the gauge side** of the frame, and the reading is the framework's, with
the plain row keeping the state cone. The caution is that a value in no subspace is a **datum about the
algebra** and not a claim that the object is unphysical, and that an indefinite pairing is a metric and
never a norm.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\bullet\tilde Q$ | the symmetric quaternionic sesquilinear product, $\mathrm{SQS}$ |
| $\mathbb{C}_{\mathbb{B}},\mathrm{Vect}(\mathbb{B}),\mathbb{H}_{\mathbb{B}},i\mathbb{H}_{\mathbb{B}},\mathbb{M}_+,\mathbb{M}_-$ | the remarkable subspaces |
| $\tilde P\bullet\tilde Q=[P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})]-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}$ | the value; in no subspace |
| $K(\tilde P,\tilde Q)=P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})$ | the Krein form; the scalar part of the value |
| $\tilde Q\bullet\tilde Q=K(\tilde Q,\tilde Q)e_0-Q_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{Q}$ | the diagonal; real element |
| $Q_0\overline{Q_k}\in i\mathbb{R}$ for all $k$ | the criterion that the diagonal be central |
| $e_1$, $e_1+ie_2$ | central diagonals $-e_0$, $-2e_0$; not witnesses of non-centrality |
| $e_0+e_1$ | the non-central witness; diagonal $-2e_1$ |
| $H(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q^{*})$ | the plain symmetric sesquilinear product; central and positive |
| $H(\tilde Q,\tilde Q)=\lvert Q_0\rvert^{2}+\lvert\mathbf{Q}\rvert^{2}$ | the positive diagonal of the state row |

## Further Reading

- Mathematics article *Remarkable Subspaces under the Symmetric Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-symmetric-quaternionic-sesqualgebra-of-biquaternions.md`), for the closure pattern of the remarkable subspaces and the fact that a general value spans the algebra.
- Mathematics article *The Krein Gram Matrix and the Restrictions of the Form* (`articles_maths/the-krein-gram-matrix-and-the-restrictions-of-the-form.md`), for the form $K$ and its restrictions to the remarkable subspaces.
- Mathematics article *The Non-Central Diagonal and the Two Halves of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/the-non-central-diagonal-and-the-two-halves-of-the-symmetric-quaternionic-sesqualgebra.md`), for the diagonal, the criterion of centrality and the witnesses.
- Companion article *The Gauge Metric as a Product: the Symmetric Quaternionic Sesquilinear Product*, for the product whose values these are.
- Companion article *Relations Between Subspaces*, for the remarkable subspaces, their bases and their intersections.
- Companion article *Other Remarkable Subspaces*, for the subspaces treated on their own terms.
- Companion article *Mass, Rank and the Positivity of the Dagger*, for the state cone and the positivity that this product does not supply.
- Companion article *Why the Fourth Product Is a Gauge Structure and Not a State Space*, for the no-go that closes the block.
- Companion article *The Cross Product of a Vector with Its Conjugate: the Antisymmetric Gauge Product*, for the antisymmetric half of the same row.
