# __The General Plain Sesquilinear Product on the Informational Sector__

## Introduction

The general plain sesquilinear product is $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$, the general plain bilinear
product with its second factor read through the Hermitian conjugation. This article reads that product on
the **informational sector** $\mathbb{M}_+$, the Hermitian half of the algebra, and it is the
informational companion of the probability band; the material companion is *The General Plain Sesquilinear
Product on the Material Sector*.

On the informational sector the Hermitian conjugation is the **identity**,

$$
\tilde Q\in\mathbb{M}_+ \ \Longrightarrow\ \tilde Q^{*}=\tilde Q,
\qquad\text{hence}\qquad
\tilde P\star\tilde Q=\tilde P\tilde Q \qquad (\tilde P,\tilde Q\in\mathbb{M}_+).
$$

The second slot's conjugation, which is the whole difference between the probability row and the
composition row, therefore **does nothing at all inside the informational sector**. The two rows are not
two products there; they are one product, and the whole of the difference between them is carried by the
material sector, where the star is the sign $-1$ (*The General Plain Sesquilinear Product on the Material
Sector*). This article reads what the coincidence means, and it reads the structure that the product
carries on the state side: the probability value is the **sector sign** $B$, positive definite; the
symmetric half of the value is the sector sign times $e_0$ and the antisymmetric half is the vector part
of the general plain bilinear composite; the idempotents of the product are exactly the **Hermitian
projections**, hence
the pure states, and they lie on the **purity boundary** of the state space, which is the zero-divisor cone.

**Placement and boundaries.** This article is the informational-sector companion of the probability band,
*Focus on the General Plain Sesqualgebra (GPS) of Biquaternions — Probability*, and the mirror of *The General
Plain Bilinear Product on the Informational Sector* in the composition band. The product, its two halves and
the form $H$ on the whole algebra are the band's framing articles; the reality of $H$ on the state side is
announced by *The Hermitian Form as a Product: Positivity and the Real Part of the Born Pairing*, whose
section on the state side is the short version of this article, and by *Why Probability Values Are
Central: the Symmetric Sesquilinear Product and Its Cone*, which owns the centrality and the idempotents
of the symmetric operation; here the same side is read as the sector of the parent product and not of its
half. The positivity, the cone and the signature are *Mass, Rank and the Positivity of the Dagger* and
*Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*; the idempotents
of the product are *Idempotents of the General Plain Sesqualgebra*; the adjoint and the operators are *The
Operators of the Plain Sesquilinear Product and the Born Pairing* and *Observables, Gauge Generators and
the Chirality of the Internal Action*; the material sector itself and the interval are *The Anti-Hermitian
Subspace $\mathbb{M}_-$ as the Material Sector* and *Biquaternion Norm and Invertibility*. None of those
is reproved here.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis
$e_0=1,e_1,e_2,e_3$ with $e_1e_2=e_3$, $e_k^{2}=-e_0$, and central scalar imaginary $i$, $i^{2}=-1$; a
general element is $\tilde Q=Q_0e_0+Q_1e_1+Q_2e_2+Q_3e_3$ with complex coefficients; the scalar part is
$\mathrm{Sc}(\tilde Q)=Q_0$ and the trace is $\mathrm{Tr}=2\,\mathrm{Sc}$. The conjugations are the
complex conjugation $\bar{\cdot}$, the natural conjugation ${\natural}$, and the Hermitian conjugation
${}^{*}=\bar{\cdot}\circ{\natural}$. The informational sector is
$\mathbb{M}_+=\{\tilde Q:\tilde Q^{*}=+\tilde Q\}$, with the real basis $\{e_0,ie_1,ie_2,ie_3\}$ and the
coordinates $\tilde Q=(ct')e_0+i\mathbf x'$; the material sector is the anti-Hermitian half,
$\mathbb{M}_-=\{\tilde Q:\tilde Q^{*}=-\tilde Q\}$, and $i\mathbb{M}_+=\mathbb{M}_-$. The four scalar
forms are $B(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q)$ with Gram
$\mathrm{E}=\mathrm{diag}(1,-1,-1,-1)$ in the coefficient basis,
$N(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)$,
$H(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q^{*})$ and
$K(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})$; the zero-divisor cone is
$\mathcal{C}=\{N=0\}$.

## The Star Is the Identity on the Informational Sector

The star fixes the informational sector pointwise. For $\tilde Q\in\mathbb{M}_+$ the two conjugations
compose to the identity, $\tilde Q^{\natural}=\overline{\tilde Q}$ coefficientwise, and the second slot of
the sesquilinear product is read with no change:

$$
\tilde P\star\tilde Q=\tilde P\tilde Q^{*}=\tilde P\tilde Q .
$$

Three consequences organise the article.

- **The product of two informational elements is the general plain bilinear product.** Its table, its closure rule, its
  non-commutativity and its order dependence are those of the composition row, read on the sector.
- **The probability value is the sector sign.** The scalar part of the value is
  $H(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q)=B(\tilde P,\tilde Q)$, and on $\mathbb{M}_+$ that is
  the positive definite Euclidean form of the informational coordinates.
- **The star is visible only on the mixed pairs and on the material sector.** On $\mathbb{M}_-$ it is the
  sign $-1$, and on a pair with one leg in each sector it is a genuine involution; inside $\mathbb{M}_+$
  it is nothing.

**Remark (verified).** For $100$ random pairs of informational elements,
$\tilde P\tilde Q^{*}=\tilde P\tilde Q$, $H(\tilde P,\tilde Q)=B(\tilde P,\tilde Q)$, and both are real to
machine precision.

**Proposed interpretation, labelled as such.** The star is the **operation that defines the probability
row**, and it is **idempotent on the informational sector**: applying it to a state changes nothing. The
informational sector is therefore the sector on which a product and a pairing are indistinguishable, and
the physical content of the second slot is entirely the choice of the material sector and of the mixed
pairs. This is the sharpest form of the framework's statement that the quantisation datum is the second
slot: on the state side there is no quantisation datum left, because the states are the elements on which
the conjugation is the identity.

## The Product on the Sector Is the General Plain Bilinear Product

Write an informational element in its own coordinates, $\tilde Q=(ct')e_0+i\mathbf x'$. The product of two
informational elements is the general plain bilinear one, and its scalar and vector parts are

$$
\tilde P\tilde Q = \bigl(c^{2}t'\tau'+\mathbf x'\!\cdot\!\mathbf y'\bigr)
+ i\bigl(ct'\mathbf y'+c\tau'\mathbf x'\bigr) - \mathbf x'\!\times\!\mathbf y',
$$

so the scalar part is the sector sign $B$ and the vector part carries both an imaginary piece, the
symmetric combination of the two directions, and the real piece $-\mathbf x'\!\times\!\mathbf y'$, the
antisymmetric combination. The composite is informational exactly when the two commute,
$\mathbf x'\!\times\!\mathbf y'=0$, and it carries a material part exactly when they anticommute. For the
sesquilinear product the same computation holds with the star absent, and the failure of closure is the
same failure:

$$
\tilde P\star\tilde Q\in\mathbb{M}_+ \iff [\tilde P,\tilde Q]=0,
\qquad
\tfrac12\bigl(\tilde P\star\tilde Q-(\tilde P\star\tilde Q)^{\natural}\bigr)
=\mathrm{Vect}\bigl(\tilde P\tilde Q\bigr).
$$

**Remark (verified).** On $100$ random informational pairs the sesquilinear composite equals the general plain bilinear
one, and it is informational exactly in the pairs that commute; on $100$ random pairs with one leg in each
sector the star is a genuine involution and the composite is neither informational nor material in
general.

**Proposed interpretation, labelled as such.** On the state side the **probability product is the
composition of observables**, and the sector's failure of closure *is* the non-commutativity of the
observations. A measurement that commutes with what it measures composes inside the sector; a measurement
that does not leaves a material residue, which is the generator and not the probability. The quantum and
the algebraic statements are the same sentence: **the observables close under composition exactly when
they commute**.

## The Two Halves on the State Side

The value of the product splits into its symmetric and antisymmetric halves under the class-preserving
exchange, and on the informational sector the two halves are the central and the vector part of the
general plain bilinear composite:

$$
\tilde P\star\tilde Q
= \underbrace{B(\tilde P,\tilde Q)\,e_0}_{\text{symmetric half, central}}
+ \underbrace{\mathrm{Vect}\bigl(\tilde P\tilde Q\bigr)}_{\text{antisymmetric half, vector}} .
$$

The **symmetric half is the probability value**, the sector sign times $e_0$, real and positive definite;
the **antisymmetric half is the phase**, the vector part of the composite. The two halves of the
probability band are therefore, on the state side, the two halves of the composition: the scalar part of
the product where the block reads a probability and its vector part where the block reads a phase. The
symmetric half is the operation of *The Hermitian Form as a Product: Positivity and the Real Part of the
Born Pairing* and the antisymmetric half the operation of *The Imaginary Part of the Born Pairing: the
Antisymmetric Sesquilinear Product*; what this article adds is that on $\mathbb{M}_+$ both are read from
the one general plain bilinear product and not from a conjugation.

**Remark (the two idempotent sets are not the same).** The idempotents of the **product** are the
Hermitian projections (next section); the idempotents of its **symmetric half** are $0$ and $e_0$ alone,
as *Why Probability Values Are Central: the Symmetric Sesquilinear Product and Its Cone* states. A pure
state $\tilde\Pi$ satisfies $\tilde\Pi\star\tilde\Pi=\tilde\Pi$ and
$\tilde\Pi\circledast\tilde\Pi=\frac12e_0\neq\tilde\Pi$: it is a projection of the product and not of the
probability value. The distinction is exact and is the reason the measurement projection is read from the
product and the probability from its half.

## Positivity and the Purity Boundary

The Born pairing on the informational sector is the sector sign,

$$
H\big|_{\mathbb{M}_+} = B\big|_{\mathbb{M}_+} = +\mathrm{I}_4 \ \text{ of signature }(4,0),
\qquad
H(\tilde Q,\tilde Q)=c^{2}t'^{2}+\lvert\mathbf x'\rvert^{2}>0 \ \text{ for } \tilde Q\neq0,
$$

the Euclidean length-squared of the informational coordinate; it has **no null vector**, so its isotropic
cone is $\{0\}$ and no nonzero informational element has zero probability. The interval restricts to the
Lorentzian form of signature $(1,3)$ in the same coordinate,

$$
N\big|_{\mathbb{M}_+}=\mathrm{diag}(1,-1,-1,-1),
\qquad
N(\tilde Q,\tilde Q)=c^{2}t'^{2}-\lvert\mathbf x'\rvert^{2},
$$

and the two forms differ by the vector square, $B-N=2\lvert\mathbf x'\rvert^{2}$. The interval's cone is
therefore **inside** the sector and is not a cone of the probability: it is the **purity boundary of the
state space**. On the unit-trace slice $\tilde\rho=\frac12(e_0+i\mathbf r)$,

$$
N(\tilde\rho,\tilde\rho)=\tfrac14\bigl(1-\lvert\mathbf r\rvert^{2}\bigr),
\qquad
B(\tilde\rho,\tilde\rho)=H(\tilde\rho,\tilde\rho)=\tfrac14\bigl(1+\lvert\mathbf r\rvert^{2}\bigr),
\qquad
\mathrm{Tr}(\tilde\rho^{2})=\tfrac12\bigl(1+\lvert\mathbf r\rvert^{2}\bigr),
$$

so a state is pure exactly when the probability is $\frac12$, exactly when the interval vanishes, exactly
when it is on the cone; the mixed states are the interior and the probability grows with the mixing. The
information-theoretic reading is exact on the same numbers: the purity is $B-N$ doubled on the slice, and
the cone is the locus of maximal information. The square of the **whole** algebra lands here and fills the
future cone: for every element $\tilde X\star\tilde X$ is positive,
$N(\tilde X\star\tilde X)=\lvert N(\tilde X)\rvert^{2}$, and it is a pure state exactly when $\tilde X$ is
on the cone. The sector's positivity is therefore the image of the sesquilinear square, and the map is *The
Cone and the Massless Particles in the 12 Structures of Biquaternions over $\mathbb{C}$*, while the state
cone and the Bloch ball as its trace-one slice are *The Spinor Space as a Hilbert Space of the General Plain
Sesqualgebra* and *The Bloch Ball as the Trace-One Slice of the Future Light Cone*.

**Remark (verified).** The two restrictions are the displayed matrices with all cross terms $0$;
$H(\tilde\rho,\tilde\rho)=\frac14(1+\lvert\mathbf r\rvert^{2})$ and
$\mathrm{Tr}(\tilde\rho^{2})=\frac12(1+\lvert\mathbf r\rvert^{2})$ on $100$ random unit-trace elements, and
$H$ is strictly positive on $100$ random informational elements.

**Proposed interpretation, labelled as such.** On the informational sector the **probability and the
interval are the two ends of one Euclidean statement**: the probability is the sum of squares and the
interval their signed difference, and their half-difference is the purity. The light cone that the
material sector reads as the wall of the massless is read here as the **wall of the pure**: the same
algebraic object, two physical names, and the sector decides which. The probability itself is never zero
on the state side; it is the *interval* that vanishes on the pure states, so **a pure state is a null
direction of the metric and not of the probability**.

## The Idempotents of the Product Are the Pure States

Every idempotent of the sesquilinear product is Hermitian, by *Idempotents of the General Plain
Sesqualgebra*: the equation $\tilde Q\star\tilde Q=\tilde Q$ reads $\tilde Q\tilde Q^{*}=\tilde Q$, the
square is Hermitian for every element, and applying the involution forces $\tilde Q^{*}=\tilde Q$. The
idempotents are therefore exactly the Hermitian projections of the algebra,

$$
0, \qquad e_0, \qquad \tilde\Pi_1(\hat{\boldsymbol\mu})=\tfrac12\bigl(e_0+i\hat{\boldsymbol\mu}\bigr),
\qquad \hat{\boldsymbol\mu}\in\mathbb{R}^{3},\ \lvert\hat{\boldsymbol\mu}\rvert=1,
$$

and **all of them lie in the informational sector**: the product has no material idempotent, and its
nontrivial idempotents are the pure states, indexed by the unit sphere. Each of them is on the cone,
$N(\tilde\Pi,\tilde\Pi)=0$, and has probability $\frac12$, $H(\tilde\Pi,\tilde\Pi)=\frac12$.

**Proposed interpretation, labelled as such.** On the state side **the idempotents of the product and
the pure states are the same set**, so the projection of a measurement is a projection of the probability
product, and the cone of the norm is at once the purity boundary and the set of the product's
projections. The probability value of a pure state is $\frac12$, the minimal positive value on the
unit-trace slice, so **a pure state is a projection whose probability is the smallest** and a mixed state
is an interior element whose probability is larger. The two readings — an idempotent and a maximal-
information state — are the same element read by the product and by the norm.

## The Adjoint and the Observables on the State Side

The operator layer of the band is *The Operators of the Plain Sesquilinear Product and the Born Pairing*,
and on the informational sector it reads one parameter at a time. The adjoint is taken for the positive
definite form $H$, and the type of a parameter is decided by the sector:

$$
\bigl(L_{\tilde A}\bigr)^{\dagger}=L_{\tilde A^{*}}=L_{\tilde A}
\ \text{ for }\ \tilde A\in\mathbb{M}_+,
\qquad
\bigl(L_{\tilde A}\bigr)^{\dagger}=L_{\tilde A^{*}}=-L_{\tilde A}
\ \text{ for }\ \tilde A\in\mathbb{M}_-,
$$

so on a Hermitian parameter the left multiplication is **self-adjoint** and on an anti-Hermitian one it is
**skew-adjoint**: the observables are the informational parameters and the generators are the material
ones, which is the framework's adjointness dictionary, and the full interpretation is *Observables, Gauge
Generators and the Chirality of the Internal Action*. The one-sidedness that the operator article owns —
the right multiplication is the isometry and the left one is not — is the same statement on the sector:
the unitary slice is not contained in either sector, and the isometries of the probability that lie in
$\mathbb{M}_+$ are $S^{2}$ in the imaginary directions together with $\pm e_0$.

**Remark (verified).** On the sector the left multiplication by a Hermitian parameter is self-adjoint for
$H$ and by an anti-Hermitian one skew-adjoint, to machine precision; the only informational elements
$\tilde A$ with $\tilde A\tilde A^{*}=e_0$ are $\pm e_0$ and the unit imaginary directions $i\hat{\boldsymbol\mu}$.

## The Two Rows Agree on the State Side

The comparison of the two rows is now a single sentence. On the informational sector the sesquilinear
product and the general plain bilinear product are **the same operation**, so

$$
\tilde P\star\tilde Q=\tilde P\tilde Q \ \text{ on } \mathbb{M}_+\times\mathbb{M}_+,
\qquad
\tilde P\star\tilde Q=-\tilde P\tilde Q \ \text{ on } \mathbb{M}_-\times\mathbb{M}_-,
$$

and the difference between the probability row and the composition row is **entirely the sector sign**:
$+1$ on the state side, $-1$ on the displacement side, and the genuine conjugation only on the mixed
pairs. The probability band and the composition band are therefore not two algebras on the same space but
one product whose second slot is the map that separates the two sectors.

**Proposed interpretation, labelled as such.** The framework's two jobs of the plain row — **composition**
and **probability** — are one operation and two sectors. A composition of two displacements is a
displacement read with a minus sign and a probability value; a composition of two observables is a
probability value and a phase. The pair of jobs is the pair of signs of the second slot, and the sector is
what the sign measures. This is the grid-level reading that the two sector companions exist to state, and
it is offered as the framework's grouping and labelled as a reading.

## A Worked Case

Take two informational elements, one off the cone and one on it, the same elements as the composition
companion,

$$
\tilde P = 3e_0+ie_1\in\mathbb{M}_+,
\qquad
\tilde Q = e_0+ie_2\in\mathbb{M}_+\cap\mathcal{C}.
$$

Since both are Hermitian, the sesquilinear product is the general plain bilinear one, and the four numbers of the case
are

$$
H(\tilde P,\tilde P)=B(\tilde P,\tilde P)=+10,\qquad
H(\tilde Q,\tilde Q)=B(\tilde Q,\tilde Q)=+2,\qquad
H(\tilde P,\tilde Q)=B(\tilde P,\tilde Q)=+3,
$$

$$
\tilde P\star\tilde Q=\tilde P\tilde Q=3e_0+ie_1+3ie_2-e_3,
\qquad
N(\tilde P,\tilde P)=+8,\qquad N(\tilde Q,\tilde Q)=0 .
$$

Read row by row, the case displays the whole sector at once. The probability of the lightlike element
$\tilde Q$ is $+2$, strictly positive: **the cone is the purity boundary and not a locus of zero
probability**. The symmetric half of the product is $3e_0$, the value of the Born pairing, and the
antisymmetric half is $ie_1+3ie_2-e_3$, the phase; the two are the two halves of the one general
plain bilinear composite. The pair does not commute, so the composite is not informational, and the material part of the
composite is the commutator $-e_3$ of the composition companion. And the probability $-1$ times the sector
sign holds on the material side, where the same elements would be read with the opposite sign; here it is
the identity.

## The Bound

The article states the restriction to the informational sector of the sesquilinear product and of its
form, and the boundary of what it must declare is the boundary of the sector.

- **The product is not central on the sector.** Its value has a vector part, so it is not a form; only its
  symmetric half is a form, and the pure states are idempotents of the product and not of the half.
- **The probability is not the interval.** $H=B$ is Euclidean and definite on the sector, with no cone;
  the interval is $N$, of signature $(1,3)$, and the two differ by $2\lvert\mathbf x'\rvert^{2}$.
- **The cone is not a probability cone.** The interval's cone is the purity boundary of the state space;
  the probability has no null and no element of zero weight.
- **The sector is not closed under the product.** Two informational elements compose to an informational
  element exactly when they commute, and the residue is material.
- **The sector does not contain the isometry group.** The unitary slice is not contained in either sector;
  inside $\mathbb{M}_+$ the isometries are the unit imaginary directions and $\pm e_0$ alone.
- **The state side has no root of $-1$ and no nilpotent.** The product has no element of vanishing square and
  no square root of $-e_0$; its roots of $+e_0$ are the unitary family $U(2)$, of which the isometries inside
  $\mathbb{M}_+$ are the part read above (*Square Roots of Minus One, Zero and Plus One in the 12 Structures
  of Biquaternions over $\mathbb{C}$*).
- **The mixed pairs are not read here.** The genuine conjugation of the second slot is visible on the
  pairs with one leg in each sector, and the example $e_0+ie_1$ with $ie_0+e_1$, both on the cone,
  composes to zero, $(e_0+ie_1)(ie_0+e_1)^{*}=0$; the mixed pairs are the operator articles' business.

**What the framework does not claim.** The interpretation does not identify the probability with a
measured frequency, does not derive the Born rule from the algebra, and does not claim that the
informational sector is physically realised as a separate world. The Born rule as a trace formula is *The
Born Rule as a Trace Formula — Derivation and Comparison*; the state space and its complement are *The
Spinor Space as a Hilbert Space of the General Plain Sesqualgebra* and *The Complementary Space of the
Spinor Space in the General Plain Sesqualgebra*.

## The Ledger

**Proved.** On $\mathbb{M}_+$ the Hermitian conjugation is the identity, hence
$\tilde P\star\tilde Q=\tilde P\tilde Q$, $H=B$ and the symmetric half of the value is $B e_0$; the Born
pairing restricts to $+\mathrm{I}_4$ of signature $(4,0)$ on each sector and the interval to
$\mathrm{diag}(1,-1,-1,-1)$ on $\mathbb{M}_+$; on the unit-trace slice the interval is
$\frac14(1-\lvert\mathbf r\rvert^{2})$ and the probability $\frac14(1+\lvert\mathbf r\rvert^{2})$, so the
cone is the purity boundary; the idempotents of the product are the Hermitian projections, all
informational, all on the cone, with probability $\frac12$; the left multiplication is self-adjoint for a
Hermitian parameter and skew-adjoint for an anti-Hermitian one; and the worked elements
$3e_0+ie_1$ and $e_0+ie_2$ give $+10$ and $+2$ with the phase $ie_1+3ie_2-e_3$.

**Interpretations.** That the star is **idempotent on the state side** and the probability row and the
composition row coincide there; that the two jobs of the plain row are **one operation and two sectors**,
separated by the sign of the second slot; that the probability on the state side is the **sector sign**
and the measurement projection is a **projection of the product and not of its half**; that a pure state
is a **null direction of the metric and not of the probability**; and that the cone is the wall of the
massless on one side and the wall of the pure on the other. Each is the framework's naming of a proved
algebraic fact and is labelled as such.

## Physical Readings

The general plain sesquilinear product reads as the probability structure of the framework, and on the
informational sector that reading is the reading of the composition: **the probability of a state is the
composition of the state with itself**, the scalar part of an observable's square. Four consequences stand
out. The measurement projection is an idempotent of the product, so a measurement is a statement about the
probability product and not about the probability value, which is the algebraic reason the value alone
cannot select a state. The phase is the vector part of the composite, so the interference of two states is
their failure to commute. The purity is the half-difference of the two metrics, so **the information
content of a state is the gap between the probability and the interval**, a gap that is maximal for the
pure states and vanishes at the maximally mixed element. And the sector exchange is the sign of the second slot, so the passage
from the informational to the material reading of a product is the passage from $+$ to $-$, which is the
clock reading of the two sectors (*Each Sector Is the Other's Clock: the Sector Exchange as Relational
Time*). The probability itself never vanishes on the state side; the wall of the state space is the wall
of the metric.

## Summary

The informational sector $\mathbb{M}_+$ carries the Hermitian elements, an element being
$\tilde Q=(ct')e_0+i\mathbf x'$, and this article reads on it the general plain sesquilinear product
$\tilde P\tilde Q^{*}$ of the probability band. On $\mathbb{M}_+$ the Hermitian conjugation is the
identity, so the sesquilinear product **is** the general plain bilinear product: the probability row and the composition
row coincide on the state side, and the whole difference between them is the sector sign, $-1$ on the
material sector and a genuine conjugation only on the mixed pairs. The scalar part of the value is the
sector sign $B=H$, positive definite of signature $(4,0)$, the Euclidean inner product of the
informational coordinates; the interval is the Lorentzian $N$ of signature $(1,3)$, the two differing by
twice the vector square, and on the unit-trace slice they read $\frac14(1+\lvert\mathbf r\rvert^{2})$ and
$\frac14(1-\lvert\mathbf r\rvert^{2})$, so the cone of the norm is the **purity boundary of the state
space** and the purity is the half-difference of the two metrics. The probability form has no null vector, so no
state has zero probability; the cone is the locus of the pure states, which are exactly the nonzero
idempotents of the product, all informational, all of probability $\frac12$. The symmetric half of the
value is the probability and the antisymmetric half the phase, and on the sector both are read from the
one general plain bilinear product. The left multiplication is self-adjoint for an observable and skew-adjoint for a
generator, and the isometries of the probability lying in the sector are the unit imaginary directions and
$\pm e_0$. The distinctions are labelled throughout: what is proved is the algebra restricted to
$\mathbb{M}_+$, what is proposed is the naming.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | The biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^{2}=-e_0$, $e_1e_2=e_3$ |
| $i$ | Central scalar imaginary, $i^{2}=-1$ |
| $\bar{\cdot},{\natural},{}^{*}=\bar{\cdot}\circ{\natural}$ | Complex, natural and Hermitian conjugations |
| $\mathbb{M}_+=\{\tilde Q^{*}=+\tilde Q\}$ | Informational sector, basis $\{e_0,ie_1,ie_2,ie_3\}$ |
| $\tilde Q=(ct')e_0+i\mathbf x'$ | An informational element; real time, imaginary space |
| $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ | General plain sesquilinear product |
| $\tilde P\star\tilde Q=\tilde P\tilde Q$ on $\mathbb{M}_+$ | The star is the identity on the sector |
| $H=B=\mathrm{Sc}(\tilde P\tilde Q)=+\mathrm{I}_4$ | The probability on the sector is the sector sign |
| $N=\mathrm{diag}(1,-1,-1,-1)$ | The interval, signature $(1,3)$ on $\mathbb{M}_+$ |
| $B-N=2\lvert\mathbf x'\rvert^{2}$ | The probability as the sum of squares against their difference |
| $\tilde\rho=\frac12(e_0+i\mathbf r)$, $\lvert\mathbf r\rvert\le1$ | Unit-trace element; the Bloch ball |
| $N=\frac14(1-\lvert\mathbf r\rvert^{2})$, $H=\frac14(1+\lvert\mathbf r\rvert^{2})$ | The cone as the purity boundary; the purity as the gap |
| $\tilde\Pi_1(\hat{\boldsymbol\mu})=\frac12(e_0+i\hat{\boldsymbol\mu})$ | The idempotents of the product; the pure states; on the cone |
| $B e_0$, $\mathrm{Vect}(\tilde P\tilde Q)$ | The symmetric and antisymmetric halves of the value |
| $(L_{\tilde A})^{\dagger}=L_{\tilde A^{*}}$ | Self-adjoint for $\tilde A\in\mathbb{M}_+$, skew-adjoint for $\tilde A\in\mathbb{M}_-$ |
| $\{i\hat{\boldsymbol\mu}\}\cup\{\pm e_0\}$ | The isometries of $H$ inside the informational sector |
| $(p,q)$ | Signature as (number of $+$, number of $-$) diagonal entries |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the quaternion algebra, the
  conjugate transpose and the matrix model of the biquaternions.
- F. Reese Harvey, *Spinors and Calibrations* (Academic Press, 1990), for the Hermitian forms on the
  biquaternion algebra and the two sectors of the involution.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge,
  2000), for the state space, the Bloch ball, the purity of a state and the projections of a measurement.
- Gérard Emch, *Algebraic Methods in Statistical Mechanics and Quantum Field Theory* (Wiley, 1972), for
  the Hermitian projections as the observables of a state algebra.
- Companion article *The Hermitian Form as a Product: Positivity and the Real Part of the Born Pairing*,
  for the symmetric half of the product and the state side on the whole algebra.
- Companion article *The General Plain Sesquilinear Product on the Material Sector*, for the mirror
  reading on $\mathbb{M}_-$.
- Companion article *The General Plain Bilinear Product on the Informational Sector*, for the composition product on the
  same sector.
- Companion article *Why Probability Values Are Central: the Symmetric Sesquilinear Product and Its Cone*,
  for the symmetric half and its own idempotents.
- Mathematics article *Idempotents of the General Plain Sesqualgebra*
  (`articles_maths/idempotents-of-the-general-plain-sesqualgebra.md`), for the idempotents of the
  product and their classification.
- Mathematics article *The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation*
  (`articles_maths/the-general-plain-sesqualgebra-in-the-2x2-matrix-element-representation.md`), for the
  Hermitian projections, the centre and the positivity in the matrix model.
- Companion article *The Cone and the Massless Particles in the 12 Structures of Biquaternions over
  $\mathbb{C}$*, for the state cone as the image of the sesquilinear square and the two faces of the cone.
- Companion article *Zero Divisors in the 12 Structures of Biquaternions over $\mathbb{C}$*, for the cone
  as the zero-divisor set of the probability band.
- Companion article *Composition and Probability: the General Plain Algebra and the General Plain
  Sesqualgebra of Biquaternions Compared*, for the twelve structures read side by side.
