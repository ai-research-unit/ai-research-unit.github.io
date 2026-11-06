# __The Unit Metric in the Biquaternion Universe__

## Introduction

The series carries one metric. It is the unit metric,

$$
\delta_{\mu\nu}=(1,1,1,1),
$$

diagonal, all four coefficients $+1$, the matrix of the interval $\sum_\mu Q_\mu^2$. It is the same in the $\mathbb{B}$ frame and in the $\mathbb{M}_-$ frame, and neither frame carries a second one.

The claim of this article is that this is the efficient object and not a minimal notation. It is read off the multiplication table instead of being postulated. It leaves no index to raise. And it makes the Lorentzian minus a fact of arithmetic instead of a convention that each article must declare.

The article answers three questions. What is the object? What does it buy? And why is the alternative refused?

The alternative is real, and the article states it in full. On the material sector one takes the real coordinate $x_0=c r'_{t}$ and writes the interval as a contraction with a metric that carries the minus,

$$
g=\mathrm{diag}(-1,1,1,1).
$$

That form gives back the familiar Clifford metric, and it is the language of the textbooks. It is not an error: it is the same geometry with the $i$ moved. The series does not write it, and the decision is stated here once, with its price. **The metric stays $1,1,1,1$, and the $i$ of $i c r'_t$ and of $i r'_{x_k}$ stays in the coordinate, separate and explicit.**

The conventions are those of [Frame and Metric Conventions](frame-and-metric-conventions.html) and [Conventions in the Biquaternion Universe](algebra-and-element-conventions.html): the base is $e_t=1$, $\vec e_x,\vec e_y,\vec e_z$ with $\vec e_k^2=-e_t$ and $\vec e_x\vec e_y=\vec e_z$, the norm is $\langle\tilde Q\rangle_\natural=\tilde Q\tilde Q^\natural$, a frame is named on the coordinate, and $c$ is the speed of light in the medium.

## What the Unit Metric Is

**It is the coefficient tuple of the interval.** For an element $\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ the norm is

$$
\langle\tilde Q\rangle_\natural=\tilde Q\tilde Q^\natural=Q_t^2+Q_x^2+Q_y^2+Q_z^2=\sum_{\mu,\nu}\delta_{\mu\nu}Q_\mu Q_\nu .
$$

The four squares enter with the same sign and there is no cross term, so the coefficient of $Q_\mu Q_\nu$ is one on the diagonal and zero off it. That coefficient is the metric, and that is the whole definition:

$$
\delta_{\mu\nu}=1\ \text{if}\ \mu=\nu,\qquad \delta_{\mu\nu}=0\ \text{otherwise}.
$$

**The four directions are unit directions.** Each basis element has norm one:

$$
\langle e_\mu\rangle_\natural=e_\mu e_\mu^\natural=+1,\qquad \mu\in\{t,x,y,z\}.
$$

The two cases are computed directly: $e_te_t^\natural=e_te_t=1$, and $\vec e_k\vec e_k^\natural=\vec e_k(-\vec e_k)=-\vec e_k^2=+1$. No sign is inserted anywhere, because the natural conjugation supplies the sign and the square supplies it back.

**That one line is the metric.** The Gram matrix of the quaternionic form on the base is

$$
\langle e_\mu,e_\nu\rangle_\natural=\mathrm{Sc}\bigl(e_\mu^\natural e_\nu\bigr)=\delta_{\mu\nu},
$$

and the four units are pairwise orthogonal, since $\mathrm{Sc}(e_x^\natural e_y)=-\mathrm{Sc}(\vec e_x\vec e_y)=-\mathrm{Sc}(\vec e_z)=0$. A base of four unit vectors, mutually orthogonal, has the identity as its Gram matrix. Nothing was chosen here: the base was given, the product was given, and the matrix came out.

**It has no free parameter.** A symmetric $4\times4$ real matrix has ten independent entries. Here four are fixed at $+1$ by the norms of the four units, six at $0$ by their orthogonality, and every one of the ten by the multiplication. There is no signature to pick, no scale to fix and no convention to declare.

**A frame carries a coordinate, not a metric.** Both frames read the same $\delta_{\mu\nu}$, because both read the same norm. What separates them is the coordinate the norm is read in: $Q_\mu$ in $\mathbb{B}$, the real $x_\mu$ in $\mathbb{M}_-$. A frame that carried a metric of its own would be a second object, and the rest of this article is about why the series keeps one.

## The Metric Is Read Off the Product

### The quaternionic form and the plain form

Two bilinear forms live on the algebra, and they differ in one slot. The **plain** form takes the scalar part of the product, $\mathrm{Sc}(\tilde Q_1\tilde Q_2)$. The **quaternionic** form conjugates the first slot before multiplying, $\mathrm{Sc}(\tilde Q_1^\natural\tilde Q_2)$, and it is the one the natural conjugation supplies. On the base the two read

$$
\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu},\qquad
\mathrm{Sc}(e_\mu^\natural e_\nu)=\delta_{\mu\nu},
$$

with $\varepsilon=(1,-1,-1,-1)$ the plain weight. The two tables are:

| pair | $\mathrm{Sc}(e_\mu e_\nu)$ | $\mathrm{Sc}(e_\mu^\natural e_\nu)$ |
|---|---|---|
| $(e_t,e_t)$ | $+1$ | $+1$ |
| $(\vec e_x,\vec e_x)$, $(\vec e_y,\vec e_y)$, $(\vec e_z,\vec e_z)$ | $-1$ each | $+1$ each |
| every pair with $\mu\neq\nu$ | $0$ | $0$ |

**The weight is what the conjugation does.** For each unit, $e_\mu^\natural=\varepsilon_\mu e_\mu$: the natural conjugation leaves the temporal unit and negates the three space units. So the two forms differ by the weight, applied entrywise, and the weight squares to the identity. **The metric is what is left when the weight has been applied twice.**

**The metric is a theorem of the table.** Solving the first display for the metric gives

$$
\delta_{\mu\nu}=\frac{\mathrm{Sc}(e_\mu e_\nu)}{\mathrm{Sc}(e_\mu e_\mu)} ,
$$

because $\mathrm{Sc}(e_\mu e_\mu)=\varepsilon_\mu$ and $\varepsilon_\mu^2=1$. Nothing on the right is a convention: the scalar part of a product of units is computed from the multiplication. The identity metric is therefore not an axiom, an input or a simplification. It is the multiplication table, read once.

### The order is inverted, and that is the gain

In the textbook order the metric is an input and the interval is defined by it, $s^2=g_{\mu\nu}x_\mu x_\nu$. The object and the invariant are born together, and the invariant cannot be checked without the object: a mis-signed entry of $g$ produces a wrong $s^2$ and nothing in the algebra objects.

Here the interval is the norm, $\langle\tilde Q\rangle_\natural=\tilde Q\tilde Q^\natural$, a product of the element with its own conjugate, and the metric is read off afterwards. **The norm is primitive and the metric is derived.** The inversion removes an input, and it removes with it the freedom to enter a wrong one: there is no array to mistype.

## How the Interval Appears

One formula, every reading. The formula is the same in all of them, because the metric is the same in all of them; what changes is the coordinate the coefficients are read in.

### The material reading

With $Q_t=i c r'_t$ and $Q_k=x_k$, for $r'_t,r_x,r_y,r_z$ real,

$$
\bigl\langle\tilde Q_-\bigr\rangle_\natural=(i c r'_t)^2+r_x^2+r_y^2+r_z^2=-c^2{r'_{t}}^2+r_x^2+r_y^2+r_z^2 .
$$

This is the Minkowski interval. The minus is $i^2=-1$: it appears at the squaring of the temporal coefficient and nowhere else. The real form has three positive directions and one negative, which the series writes $(3,1)$, positive counted first.

### The informational reading

With $Q_t=c r_t$ and $Q_k=i r'_{x_k}$,

$$
\bigl\langle\tilde Q_+\bigr\rangle_\natural=c^2 r_t^2-(r'_{x})^2-(r'_{y})^2-(r'_{z})^2 .
$$

One positive direction and three negative, $(1,3)$. The mirror of the material case: the $i$ has moved from the temporal slot to the three spatial ones, and the three minuses have moved with it.

### The general reading

On $\mathbb{B}$ the four coefficients are complex and the value of the norm is complex. On the real-quaternion subspace $\mathbb{H}_{\mathbb{B}}$, where the coefficients are real, it is $q_t^2+q_x^2+q_y^2+q_z^2$, positive definite, signature $(4,0)$: the ordinary Euclidean form.

| reading | coordinate | interval | signature |
|---|---|---|---|
| $\mathbb{B}$ | $Q_\mu\in\mathbb{C}$ | complex in general | none until a sector is imposed |
| $\mathbb{H}_{\mathbb{B}}$ | $q_\mu\in\mathbb{R}$ | $q_t^2+q_x^2+q_y^2+q_z^2$ | $(4,0)$ |
| $\mathbb{M}_-$ | $Q_t=i c r'_t$, $Q_k=x_k$ | $-c^2{r'_{t}}^2+r_x^2+r_y^2+r_z^2$ | $(3,1)$ |
| $\mathbb{M}_+$ | $Q_t=c r_t$, $Q_k=i r'_{x_k}$ | $c^2 r_t^2-(r'_{x})^2-(r'_{y})^2-(r'_{z})^2$ | $(1,3)$ |

**The metric did not move.** In all four rows the coefficient tuple is $\delta_{\mu\nu}=(1,1,1,1)$; the column that changes is the coordinate. So the answer to the question *how does a metric of $1,1,1,1$ give $-c^2{r'_{t}}^2+r_x^2+r_y^2+r_z^2$* is: it gives the four coefficients $+1$, and the sign is delivered by the coordinate. The metric does its work as a coefficient, and the $i$ does the rest.

**The sign is counted once.** Write $Q_t=i c r'_t$ and the time term of the interval is negative. That is one use of the sign, and there is no second slot in the scheme that could hold another: the metric is the identity, so it carries no entry for a minus on the time direction.

## Why the Sign Cannot Be Wrong

The objection is worth stating in its strongest form. *A metric is a convention. Papers use $(+,-,-,-)$ and papers use $(-,+,+,+)$, both are correct, and a series that fixes $1,1,1,1$ has merely picked one.*

The answer has three steps.

**A convention is a choice between writings the algebra cannot tell apart.** The tuple $1,1,1,1$ is not that. It is the Gram matrix of the quaternionic form on the base, and the quaternionic form is fixed by the norm, which is fixed by the product. Given this base, there is no second tuple that the same product would also support: the Gram matrix is computed, not selected.

**The competing writing is distinguishable, and it is distinguishable in a specific place.** It changes the coefficient tuple from $\delta_{\mu\nu}$ to $-\varepsilon_\mu\delta_{\mu\nu}$, and it moves the $i$ from the coordinate into the array. That is a relocation of one symbol, not a value of a free parameter. It is a different notation for the same geometry.

**Therefore the sign is checkable in one and not in the other.** In the unit scheme a reader checks the minus by squaring: $(i c r'_t)^2=-c^2{r'_{t}}^2$, and $i^2=-1$ is arithmetic. In the absorbed scheme the minus is an entry of an array, and the reader can only check it against the author's declaration. One of the two can be audited by a reader who does not trust the author.

**What the signature still is.** The interval on $\mathbb{M}_-$ has signature $(3,1)$ and this is a real statement. It belongs to the form read on a sector, and the series states it there. It does not belong to the metric: read as a real quadratic form, $\delta_{\mu\nu}$ has signature $(4,0)$, and the $(3,1)$ of the material interval is what the complex coordinate does to the four coefficients that form is read on. Confusing the two is the mistake the unit metric exists to prevent.

## What the Choice Buys

Four gains follow, and the table at the end of the section is their summary.

**No index is raised.** With $\delta_{\mu\nu}$ the identity, a raised index would denote the same slot, so every index is written low and the position of an index carries no information. The sign that a raising would carry is carried by the weight instead, and the series writes it where it belongs.

**One substitution changes the frame.** $Q_t=i c r'_t$ in physics, $Q_t=ix_0$ in the algebra. No matrix, no transpose and no congruence: the substitution carries the interval at once, and there is nothing else to get right.

**One formula serves every sector.** The norm is one polynomial in four variables. An author does not select a case, a branch or a sign before computing; the case is a condition on the coefficients, and the formula is blind to it.

**One symbol does two jobs.** The $i$ of $Q_t=i c r'_t$ supplies the minus of the interval, by $i^2=-1$, and it also marks the temporal coefficient as imaginary, which is what the material reading of time stands on. A single symbol carries the geometry and the interpretation together. Absorption separates the two jobs: the minus moves into $g_{00}=-1$, and the $i$ either leaves the coordinate, taking the reading with it, or stays, and then the sign is written twice.

| object the scheme must carry | unit metric | absorbed metric |
|---|---|---|
| metrics named | one, for the whole series | one per frame |
| change of frame | one substitution | a substitution plus a congruence law |
| index machinery | none | raising and lowering |
| Clifford relation | $\{\gamma_\mu,\gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}I_4$ | $+2g$ after $\gamma\mapsto i\gamma$, else $-2g$ |
| second home of the minus | held by the coordinate, where the $i$ also marks time imaginary | held by a matrix entry, where the $i$ has no second job |
| auditable by squaring | yes | no |

The two schemes write the minus in the same number of places, and the count is not the argument in itself: the plain weight $\varepsilon$ is a fact of the multiplication and stays in both. What the table records is which object holds the second copy, and what else that object does.

## The Alternative We Do Not Choose

**The move.** Take the real coordinate and put the minus in a metric:

$$
x_0=c r'_{t},\qquad x_k=r_k,\qquad -c^2{r'_{t}}^2+r_x^2+r_y^2+r_z^2=g_{\mu\nu}x_\mu x_\nu,\qquad g=\mathrm{diag}(-1,1,1,1).
$$

The $i$ has left the coordinate. What it leaves behind in the metric is the minus it produced, and the $i$ itself reappears, if it is kept at all, only in the rescaled generators, $\gamma'_\mu=i\gamma_\mu$. That is what *absorbing* means, and it can be done.

**The absorbed metric is the plain weight, negated.** In one line,

$$
g_{\mu\nu}=-\varepsilon_\mu\delta_{\mu\nu},
$$

because the real-coordinate interval is $-\varepsilon_\mu x_\mu^2$: the time term is $-x_0^2$, and the three space terms are $+x_k^2$. So the object that absorption produces is not new. It is the weight the algebra already has, moved from the product into the metric and given an overall minus so that the interval comes out right.

### What the absorbed form buys

- **The familiar Clifford relation with a plus.** Setting $\gamma'_\mu=i\gamma_\mu$ gives $\{\gamma'_\mu,\gamma'_\nu\}=2g_{\mu\nu}I_4$ with the metric on the right having the textbook signs.
- **The language of the textbooks and of general relativity.** There the metric is the leading object, and a reader arrives expecting it.
- **A one-line translation.** $g=-\varepsilon$ and $\gamma'=i\gamma$ convert between the two schemes.

None of the three is a gain in content. Each is a gain in familiarity, and familiarity is not nothing: it is the reason the alternative is stated here in full rather than dismissed.

### What it costs

1. **The $i$ is relocated, not removed.** With the original generators the relation reads $\{\gamma_\mu,\gamma_\nu\}=-2g_{\mu\nu}I_4$, carrying a stray minus; with the rescaled generators the $i$ sits inside each matrix, $\gamma'=i\gamma$. In both writings the $i$ is inside an object, where a reader cannot see it.
2. **Two metrics instead of one.** The frame carries a metric again, so each frame must be declared with its metric and every display must say which is in force. That is a convention at the head of each article, and a convention can be stated wrongly.
3. **A congruence law in place of a substitution.** The change of frame becomes a matrix statement, $g_{\mathbb{M}_-}=\Lambda^{\mathsf T}g_{\mathbb{B}}\Lambda$, with a matrix, a transpose and a law. The unit scheme writes $Q_t=ix_0$ and stops.
4. **Index machinery returns.** With $g\neq\delta$ raising and lowering are live operations, so every index question acquires two parts: is it up or down, and in which metric.
5. **The sign loses its provenance.** In the unit scheme the minus is checked by squaring. In the absorbed scheme it is a number in an array, checked only against the author's word, so a reader cannot audit it.
6. **The material reading loses its anchor.** The imaginary temporal coefficient is what marks time as measured but not touched; a metric with $g_{00}=-1$ turns the same sign into a property of a matrix, and the reading has nothing algebraic left to stand on.
7. **It opens the door to a mixed text.** A text that keeps $Q_t=i c r'_t$ and also contracts with $g_{00}=-1$ has applied the sign twice, and its time term reads $+c^2{r'_{t}}^2$. The error is silent: every other term is right, the algebra checks pass, and only the sign of the interval is wrong. Absorption done whole is consistent; the mixture is what the literature contains, and it is what a migration has to undo one article at a time.

**The decision.** The series keeps the metric $1,1,1,1$ and keeps the $i$ of $i c r'_t$ and $i r'_{x_k}$ in the coordinate, separate and explicit. The sign is written in the product and in the coordinate, and in nothing else.

**What the decision does not claim.** The absorbed form is not wrong. It is equivalent, and the equivalence is one line: $g=-\varepsilon$. An article that writes it describes the same interval, and a reader who comes from the textbooks should translate once and then work in the coordinate. What the series refuses is not the object but its price, and the price is the seven items above.

## Two Objections

### The objection from gravity

*General relativity needs a metric that varies from point to point, so a constant identity cannot be the metric of spacetime.*

The two objects are different and the series keeps both. The unit metric is the flat form of the algebra at a point: it is the Gram matrix of the norm, it has constant coefficients, and it says nothing about curvature. A curved metric is a field that attaches the algebra to a manifold, and it is carried by a tetrad, not by $\delta_{\mu\nu}$. Curvature cannot reside in the algebra for the reason the curved-space article gives: the algebra is the same at every point and its norm has constant coefficients. So the identity metric is not a rival of the dynamical $g_{\mu\nu}(x)$; it is the local flat form that the dynamical metric reduces to at a point, and the articles that carry a curved metric keep theirs unchanged.

### The objection from invariants

*Without a metric you cannot form an invariant, and without a metric you cannot raise an index.*

The invariant is the norm, and the norm is a product. A boost is a rotor, $B=\cosh\frac{\theta_{\mathrm{rpd}}}{2}+i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\vec u$ for a unit real vector $\vec u$, and it acts by conjugation, $\tilde Q\mapsto B\tilde Q B^{*}$. That action leaves the norm fixed, and the proof uses no metric. A rotor has quaternionic norm one, $BB^\natural=1$, so $B^\natural=B^{-1}$. Because the natural conjugation is an involution and commutes with the bar, $(B^{*})^\natural=\bar B$, so $B^{*}\bar B=\langle B^{*}\rangle_\natural=1$. Then

$$
\bigl\langle B\tilde Q B^{*}\bigr\rangle_\natural=B\tilde Q B^{*}(B^{*})^\natural\tilde Q^\natural B^\natural=B\tilde Q\,\tilde Q^\natural B^{-1}=\langle\tilde Q\rangle_\natural ,
$$

because $B^{*}\bar B=1$ cancels the middle pair and $\tilde Q\tilde Q^\natural$ is a scalar, hence central. So the invariant exists without a metric being introduced, and it is the metric that is read off the invariant rather than the other way round.

As for the index, there is nothing to raise. With $\delta_{\mu\nu}$ the identity, raising with it returns the same slot, so an upper index would denote nothing new; the series writes every index low and lets the weight carry the sign a raising would carry.

## The Plain Weight Is Not the Metric

The weight $\varepsilon=(1,-1,-1,-1)$ is the square of the units, $\mathrm{Sc}(e_\mu^2)=\varepsilon_\mu$, and it is the same in both frames. It is not a metric, and the difference matters because one formula merges the two:

$$
\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}.
$$

The right-hand side is a product of two objects. The metric is the second factor, the weight is the first, and reading the product as a single object is the error this article exists to prevent.

**The weight looks like a metric, and that is the trap.** Since $g=-\varepsilon$, contracting the real coordinate with $\varepsilon$ rather than with $g$ gives $+c^2{r'_{t}}^2-x^2-y^2-z^2$: the overall negative of the interval. Both objects are diagonal with entries $\pm1$, so the algebra does not catch the substitution, and only the sign of the interval records it.

**A repeated label is a sum, never a contraction.** No index is raised or lowered, so the pairing of two elements is a quaternionic form and not an index operation. The weight does the sign work in a product; the metric does none, because it is the identity.

## Physical Readings

The choice of metric reads in three ways, each with the boundary that keeps it honest.

- **The geometry is in the algebra.** The interval is a norm, the norm is a product, and the metric is the Gram matrix of the product. The framework therefore does not need a metric field to say what a distance is; it needs one only to say how the algebra is attached to a curved manifold, and that is the tetrad's job. Boundary: this is a statement about the flat pointwise geometry, and it says nothing about dynamics.
- **The minus is arithmetic, not convention.** The Lorentzian minus is $i^2=-1$, so it is a fact about numbers and a reader can audit it. Boundary: the assertion that the *world* is Lorentzian is a physical premise; what the algebra supplies is that the premise costs nothing to state and one line to check.
- **Time is measured and not touched.** The imaginary temporal coefficient is what distinguishes time from the three spatial coefficients, and it is also the source of the minus. Boundary: the reading of the placement as the difference between time and space is an interpretation, made in *The Temporal Dimension*; the mathematics fixes only the placement.

## Summary

There is one metric in the series, the unit metric $\delta_{\mu\nu}=(1,1,1,1)$, and it is the identity matrix. It is not postulated. The four basis units have norm one, $\langle e_\mu\rangle_\natural=+1$, so the Gram matrix of the quaternionic form on the base is the identity, and the same computation solves for the identity from the scalar part of the products, $\delta_{\mu\nu}=\mathrm{Sc}(e_\mu e_\nu)/\mathrm{Sc}(e_\mu e_\mu)$. The metric is a theorem of the multiplication table.

The order of the two objects is inverted with respect to the textbook. The interval is a norm, a product of the element with its own conjugate, and the metric is read off afterwards. That removes an input and, with it, the freedom to mistype one.

The Lorentzian interval follows from the same metric, with the sign delivered by the coordinate rather than by the metric. With $Q_t=i c r'_t$ the norm is $(i c r'_t)^2+r_x^2+r_y^2+r_z^2=-c^2{r'_{t}}^2+r_x^2+r_y^2+r_z^2$: the minus is the square of the $i$ in the coordinate, the real form has signature $(3,1)$, and the coefficient tuple is still $\delta_{\mu\nu}$. The informational reading gives the mirror, $c^2 r_t^2-(r'_{x})^2-(r'_{y})^2-(r'_{z})^2$, with signature $(1,3)$, from the same metric and a different coordinate.

The alternative is stated and refused. Absorbing the $i$ into a metric on the material sector gives $g=\mathrm{diag}(-1,1,1,1)$, which is $-\varepsilon$, and it recovers the Clifford metric after $\gamma\mapsto i\gamma$. It is equivalent, and it is the textbooks' language. It is refused because it relocates the $i$ into an object instead of removing it, because it makes a frame carry a metric again, because it replaces one substitution by a congruence law, because it brings back the index machinery, because it makes the minus un-auditable, because it removes the anchor of the material reading, and because it opens the door to a mixed text whose symptom is a time term of $+c^2{r'_{t}}^2$.

The series therefore keeps the metric $1,1,1,1$ and keeps the $i$ of $i c r'_t$ and $i r'_{x_k}$ in the coordinate, separate and explicit.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\delta_{\mu\nu}=(1,1,1,1)$ | The unit metric: the identity matrix, the coefficient tuple of $\sum_\mu Q_\mu^2$, the Gram matrix of the quaternionic form on the base |
| $\langle\tilde Q\rangle_\natural=\tilde Q\tilde Q^\natural$ | The norm; $Q_t^2+Q_x^2+Q_y^2+Q_z^2$, all four coefficients $+1$ |
| $\langle e_\mu\rangle_\natural=+1$ | Every basis unit has norm one: the reason the metric is the identity |
| $\langle\tilde Q_1,\tilde Q_2\rangle_\natural=\mathrm{Sc}\bigl(\tilde Q_1^\natural\tilde Q_2\bigr)$ | The quaternionic form; Gram matrix $\delta_{\mu\nu}$ on the base |
| $\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ | The plain form; $\varepsilon_\mu\delta_{\mu\nu}$ on the base |
| $\varepsilon=(1,-1,-1,-1)$ | The plain weight, the square of the units; not a metric |
| $Q_t=i c r'_t$, $Q_k=x_k$ | The material coordinate; the source of the minus of the interval |
| $Q_t=c r_t$, $Q_k=i r'_{x_k}$ | The informational coordinate; the $i$ on the three space slots |
| $-c^2{r'_{t}}^2+r_x^2+r_y^2+r_z^2$ | The material interval, signature $(3,1)$ |
| $c^2 r_t^2-(r'_{x})^2-(r'_{y})^2-(r'_{z})^2$ | The informational interval, signature $(1,3)$ |
| $g=\mathrm{diag}(-1,1,1,1)$ | The absorbed metric of the rejected alternative; equal to $-\varepsilon_\mu\delta_{\mu\nu}$ |
| $\gamma_\mu$, $\{\gamma_\mu,\gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}I_4$ | The Clifford map of the series; $\gamma_0^2=I_4$ and $\gamma_k^2=-I_4$ |
| $\gamma'_\mu=i\gamma_\mu$ | The generators that give $+2g_{\mu\nu}$; the $i$ inside the array |
| $B=\cosh\frac{\theta_{\mathrm{rpd}}}{2}+i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\vec u$ | Boost rotor; it preserves the norm with no metric entering |

## Further Reading

- Hermann Minkowski, "Space and Time" (1908), reprinted in *The Principle of Relativity* (Dover), for the interval and the union of space and time.
- Paul A. M. Dirac, *The Principles of Quantum Mechanics*, 4th edition (Oxford, 1958), for the gamma algebra in the form the textbooks inherited.
- Charles W. Misner, Kip S. Thorne, John A. Wheeler, *Gravitation* (Freeman, 1973), §2.3 and §3.1, for the metric as the leading object and for the fate of the $i c r_t$ convention.
- David Hestenes, *Space-Time Algebra*, 2nd edition (Birkhäuser, 2015), for the school that puts the signature into the frame and the generators rather than into a coefficient, the nearest systematic contrast to the choice made here.
- Roger Penrose, *The Road to Reality* (Knopf, 2004), Chapters 11 and 18, for the complex structure of spacetime and the place of the metric among the structures.
- The corpus articles cited above: [Frame and Metric Conventions](frame-and-metric-conventions.html), [Conventions in the Biquaternion Universe](algebra-and-element-conventions.html), [The Temporal Dimension: Why the Temporal Unit Is the Identity](the-temporal-dimension-why-the-temporal-unit-is-the-identity.html), [Why Complexify Spacetime?](why-complexify-spacetime.html), [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html), [Product and Form Conventions](product-and-form-conventions.html), [Unit, Index and Notation Conventions](unit-index-and-notation-conventions.html), [Matrix Representations Conventions](matrix-representations-conventions.html), and [Curved Spacetime and the Biquaternion Framework](curved-spacetime-and-the-biquaternion-framework.html), for the conventions, the frames, the sector readings and the curved case.
