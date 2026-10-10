# __The States the Indefinite Metric Cannot Normalise__

## Introduction

A state has to be normalisable. That is not a convention: the probability of a measurement outcome is a ratio of two inner products, so the inner product must be positive definite on the states, and the physical state space is the positive cone of that inner product. An indefinite metric, by construction, does not normalise everything: it gives some directions positive, some negative, and some **zero** squared length, and the elements of zero length — the **null** elements — are exactly the ones a norm cannot reach. In the Gupta–Bleuler treatment of the electromagnetic field the unphysical states are the negative-norm ones and the physical state space is recovered after the null states are quotiented out; the null sector is the physical boundary of an indefinite-metric theory.

This article reads that structure on the states of the framework. The states of the informational sector are the rank-one projectors of the algebra, the points of the **Bloch sphere**, and the framework's probability form $H$ normalises them. The fourth product's indefinite metric $K$ — the subject of *The Fourth Product and Its Indefinite Metric* — does not: **every pure state is null for $K$**, and the vanishing is not an accident of one state but an identity satisfied by the whole Bloch sphere. The pure states sit exactly on the **null cone of the gauge metric**. The article owns that computation, its reading, and a second family of projections, the ones belonging to the fourth product itself, which are unitaries of **order three** rather than rank-one projectors, and which — as a labelled speculation — read as an internal three-valued label in place of the two-valued one of an ordinary measurement.

The article defers the positivity of the probability form and the absence of ghosts to *Mass, Rank and the Positivity of the Dagger*; the vacuum to *The Biquaternion Vacuum as a Minimal Idempotent*; the state cone and the Bloch ball to *The Bloch Ball as the Trace-One Slice of the Future Light Cone*; the projection as measurement to *Decoherence as Idempotent Projection*; the gauge reading of the fourth product to *Why the Fourth Product Is a Gauge Structure and Not a State Space*; and the mathematics to the mathematics articles *Idempotents of the General Quaternionic Sesquilinear Product*, *The Square of the General Quaternionic Sesquilinear Product and the Two Halves* and *The Krein Gram Matrix and the Restrictions of the Form*.

**Conventions.** As in the companion articles of this block: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$, $e_k^{2}=-e_0$, $e_1e_2=e_3$; the fourth product $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q^{*}$; the sesquilinear product $\tilde P\star_s\tilde Q=\tilde P\tilde Q^{*}$; the conjugations ${}^{\natural}$, ${}^{*}$ and the coefficientwise bar; $\mathrm{Sc}$ the scalar part and $\mathrm{Tr}=2\,\mathrm{Sc}$. The biquaternion norm is $N(\tilde Q)=\tilde Q\tilde Q^{\natural}=\sum_\mu Q_\mu^{2}$, whose vanishing locus $\mathcal{N}=\{N=0\}$ is the zero-divisor cone, the framework's **light cone**. The sectors are $\mathbb{M}_+=\{\tilde Q^{*}=\tilde Q\}$ and $\mathbb{M}_-=\{\tilde Q^{\flat}=\tilde Q\}$, with $\flat=-{}^{*}$; the sign vector is $\varepsilon=(1,-1,-1,-1)$. All conventions are those of *Conventions in the Biquaternion Universe*.

## Why a State Must Be Normalisable

**The probability form must be positive.** The Born pairing of the framework is the general plain sesquilinear form $H(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q^{*})=\sum_\mu P_\mu\overline{Q_\mu}$, and it is genuinely positive definite: $H(\tilde Q,\tilde Q)=\sum_\mu\lvert Q_\mu\rvert^{2}$ is strictly positive for $\tilde Q\neq0$, with signature $(8,0)$ on the algebra. That positivity is not decorative — it is the reason the framework has no negative-norm states, and it is proved as such in *Mass, Rank and the Positivity of the Dagger*. A state is a positive trace-one element for $H$; a pure state is a rank-one such element; and the set of pure states is the boundary of the state cone, the **Bloch sphere**.

**An indefinite metric cannot do that job.** The fourth product's form is the opposite kind of object: $K(\tilde P,\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ with $\varepsilon=(1,-1,-1,-1)$, Hermitian, non-degenerate and **indefinite**, of signature $(1,3)$ over the complex coefficients. Its diagonal is positive on the centre and negative on the six vector directions, and it has a large **null set**, the elements of zero $K$-length. An element of the null set has no normalised representative for $K$: multiplying it by a scalar cannot change zero into one. Normalisation is a property of the pair (form, state), and the states of this framework are normalisable for $H$ and, as the next section shows, exactly null for $K$.

**The physical precedent.** In an indefinite-metric gauge theory the physical states are typically recovered as a quotient by the null states, and the null sector is part of the physical description rather than a defect. The reading of this article is that the framework exhibits the same structure internally: two forms, one definite and one indefinite, and a distinguished family of states that is normalisable for the first and null for the second.

## The Pure States Are Null for the Gauge Metric

### The Pure States

The informational sector $\mathbb{M}_+$ is the Hermitian subspace, of basis $\{e_0,ie_1,ie_2,ie_3\}$; its elements are the observables of the qubit, its positive trace-one elements are the states, and its rank-one projectors are the **pure** states. A pure state is written

$$
\tilde\Pi=\tfrac12\bigl(e_0+i\hat\mu\bigr),\qquad
\hat\mu=\mu_1e_1+\mu_2e_2+\mu_3e_3,\qquad
(\hat\mu,\hat\mu)=\mu_1^{2}+\mu_2^{2}+\mu_3^{2}=1,
$$

with $\hat\mu$ a **real** unit vector. Its four real parameters are $(q_0,q'_1,q'_2,q'_3)=(\tfrac12,\tfrac12\mu_1,\tfrac12\mu_2,\tfrac12\mu_3)$: a real scalar part and an imaginary vector part. The condition $(\hat\mu,\hat\mu)=1$ makes the family a **two-sphere**, the Bloch sphere of the state space; every element of the family is a rank-one projection, $\tilde\Pi^{2}=\tilde\Pi$ and $\tilde\Pi\star_s\tilde\Pi=\tilde\Pi$, the complementary element $\tfrac12(e_0-i\hat\mu)$ is the antipodal pure state, and the two resolve the identity.

### One Computation, Three Nullities

The content of the article is a two-line computation on the coefficients $(\tfrac12,\tfrac i2\mu_1,\tfrac i2\mu_2,\tfrac i2\mu_3)$, and it is exact.

**The gauge metric vanishes.** With $Q_0=\tfrac12$ and $Q_k=\tfrac i2\mu_k$ real-multiplied, the Krein invariant is

$$
K(\tilde\Pi,\tilde\Pi)=\lvert Q_0\rvert^{2}-\sum_{k=1}^{3}\lvert Q_k\rvert^{2}
=\tfrac14-\tfrac14\sum_{k=1}^{3}\mu_k^{2}
=\tfrac14-\tfrac14\cdot1=0,
$$

because $\hat\mu$ is a unit vector. **Every pure state is null for the gauge metric.**

**The interval vanishes.** The same coefficients give the biquaternion norm

$$
N(\tilde\Pi)=\sum_{\mu=0}^{3}Q_\mu^{2}
=\tfrac14+\sum_{k=1}^{3}\Bigl(\tfrac i2\mu_k\Bigr)^{2}
=\tfrac14-\tfrac14\sum_{k=1}^{3}\mu_k^{2}=0,
$$

so every pure state is a **zero divisor**, $\det\Phi(\tilde\Pi)=0$, and lies on the light cone $\mathcal{N}=\{N=0\}$ of the framework.

**The fourth product vanishes.** The square of the state in the fourth product is

$$
\tilde\Pi\star\tilde\Pi=\tilde\Pi^{\natural}\tilde\Pi^{*}
=\tfrac12\bigl(e_0-i\hat\mu\bigr)\cdot\tfrac12\bigl(e_0+i\hat\mu\bigr)
=\tfrac14\bigl(e_0-e_0\bigr)=0,
$$

using $\tilde\Pi^{*}=\tilde\Pi$, $\tilde\Pi^{\natural}=\tfrac12(e_0-i\hat\mu)$ and $\hat\mu^{2}=-e_0$ for a real unit vector. In the matrix model the same statement is immediate: a rank-one projector has $\operatorname{adj}\Phi(\tilde\Pi)\,\Phi(\tilde\Pi)=\det\Phi(\tilde\Pi)\,I=0$ and $\Phi(\tilde\Pi)^{\dagger}=\Phi(\tilde\Pi)$, so $\Phi(\tilde\Pi\star\tilde\Pi)=0$.

**One computation, three statements.** The pure state of the quantum theory is at once isotropic for the gauge metric, a zero divisor of the interval, and a square-zero element of the fourth product. The three are one computation read three ways, and their coincidence is the structural point: the states are precisely the elements that the indefinite metric cannot normalise, and they are so on the light cone of the framework, at the intersection of the $K$-null set, the zero-divisor cone and the trace-one slice.

### The Two Meters Agree Where a State Lives

The two nullities above hold for the pure states; on the state cone the two forms are in fact the **same meter**, and this is worth separating from the double vanishing, which is a different statement.

On the informational sector the two forms coincide as forms, not only on the diagonal. The corollary of the Lagrange identity of *The Fourth Product and Its Indefinite Metric*,

$$
K(\tilde\varrho,\tilde H)=N(\tilde\varrho,\tilde H)\quad\text{for }\tilde\varrho,\tilde H\in\mathbb{M}_+,
$$

is a statement off the diagonal as well, since both forms are Hermitian there; verifying it on the density matrices confirms it. A **density matrix** $\tilde\varrho=\tfrac12(e_0+i\mathbf r)$ with $\lvert\mathbf r\rvert\le1$ is **self-conjugate**, $\tilde\varrho^{*}=\tilde\varrho$, and for a self-conjugate element the gauge invariant is the squared norm,

$$
K(\tilde\varrho,\tilde\varrho)=\mathrm{Sc}\bigl(\tilde\varrho^{\natural}\tilde\varrho^{*}\bigr)=\mathrm{Sc}\bigl(\tilde\varrho^{\natural}\tilde\varrho\bigr)=N(\tilde\varrho)=\tfrac14\bigl(1-\lvert\mathbf r\rvert^{2}\bigr),
$$

so the gauge invariant of a state measures its **mixedness** — one half of the linear entropy, $\tfrac14\bigl(1-\lvert\mathbf r\rvert^{2}\bigr)=\tfrac12\bigl(1-\mathrm{Tr}\,\tilde\varrho^{2}\bigr)$, since $\mathrm{Tr}\,\tilde\varrho^{2}=\tfrac12(1+\lvert\mathbf r\rvert^{2})$: it vanishes exactly on the pure boundary, where the interval vanishes too, and it is $\tfrac14$ at the maximally mixed state. The indefinite metric and the interval are therefore two readings of one number wherever a state lives, and they part only off the informational sector, where $K=-N$. The reading is worth a name: **the two meters agree where a state lives**, and the gauge metric separates a state from the identity by the same number that the interval does. The identity is the corollary of the Lagrange identity; the mixedness interpretation and the "two meters" name are this article's reading.

### What Is Measured with Which Form

The distinction that keeps the reading honest is the distinction between the two forms.

| Quantity | Form | Value at a pure state | Meaning |
|---|---|---|---|
| probability of the state | $H(\tilde\Pi,\tilde\Pi)=\mathrm{Sc}\,\tilde\Pi$ | $\tfrac12$ | positive, normalisable |
| trace | $\mathrm{Tr}\,\tilde\Pi=2\,\mathrm{Sc}\,\tilde\Pi$ | $1$ | a normalised state |
| gauge invariant | $K(\tilde\Pi,\tilde\Pi)$ | $0$ | null; not normalisable |
| interval | $N(\tilde\Pi)$ | $0$ | lightlike; a zero divisor |
| fourth-product square | $\tilde\Pi\star\tilde\Pi$ | $0$ | null element of the gauge product |

The states are normalised by $H$, counted by the trace, and annihilated by $K$ and by $N$. There is no contradiction: the same element can be positive for one form and null for another, and the framework's states are the positive ones for the form that carries the Born rule.

## The Other Projections: Three Values Instead of Two

The fourth product has projections of its own, and they are **not** the states. Solving $\tilde\Pi\star\tilde\Pi=\tilde\Pi$ gives, beyond the degenerate pair $0$ and $e_0$, the elements

$$
\tilde\Pi(\mu)=-\tfrac12 e_0+\mu,\qquad \mu\in\mathrm{Vect}(\mathbb{B})_{\mathbb{R}},\qquad (\mu,\mu)=\tfrac34,
$$

with $\mu$ a **real** vector of squared length $\tfrac34$: again a two-sphere, but a sphere in the real quaternion subalgebra rather than in the informational sector. Every one of them is a **unit** of the algebra, $N(\tilde\Pi(\mu))=\tfrac14+\tfrac34=1$, with inverse its own natural conjugate, $\tilde\Pi(\mu)^{-1}=\tilde\Pi(\mu)^{\natural}=-\tfrac12e_0-\mu$; its trace is $-1$; and its gauge invariant is $K=-\tfrac12$, negative rather than null. Most tellingly it is of **order three** in the plain product,

$$
\tilde\Pi(\mu)^{3}=e_0,
$$

so in the $2\times2$ model its matrix is the unitary conjugate of $\operatorname{diag}(\omega,\omega^{2})$ with $\omega=e^{2\pi i/3}$, a unitary of determinant one and order three whose two eigenvalues are the nontrivial cube roots of unity, the identity supplying the third.

**The reading, labelled a speculation.** A projection of the probability product is a rank-one projector with the two Boolean values $\{0,1\}$ — a **two-valued** measurement. A projection of the fourth product is an invertible unitary whose powers run through the three cube-root values $\{1,\omega,\omega^{2}\}$ — a **three-valued** internal label. The contrast is structural and exact, and it is offered as a speculation about measurement: the framework supplies the two families, but no rule that selects the fourth product for a measurement and no three-valued process, and the caution that $\mathbb{Z}/3$ is ubiquitous is stated with the speculation. The mathematics of the criterion and the classification is *Idempotents of the General Quaternionic Sesquilinear Product*, and the unitary-orbit form is *The General Quaternionic Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*; both are cited, not re-derived.

## A Worked Case: The Qubit on the Bloch Sphere

Take the pure state with Bloch vector $\hat\mu=e_1$, that is $\tilde\Pi=\tfrac12(e_0+ie_1)$, so that the coefficients are $Q_0=\tfrac12$, $Q_1=\tfrac i2$, $Q_2=Q_3=0$.

| quantity | value |
|---|---|
| $\mathrm{Tr}\,\tilde\Pi$ | $1$ |
| $H(\tilde\Pi,\tilde\Pi)$ | $\tfrac14+\tfrac14=\tfrac12$ |
| $K(\tilde\Pi,\tilde\Pi)$ | $\tfrac14-\tfrac14=0$ |
| $N(\tilde\Pi)$ | $\tfrac14-\tfrac14=0$ |
| $\tilde\Pi\star\tilde\Pi$ | $0$ |
| $\tilde\Pi\star_s\tilde\Pi-\tilde\Pi$ | $0$ |

The state is normalised for the probability form, trace one, and null for the gauge metric, the interval and the fourth product. The antipodal state $\tfrac12(e_0-ie_1)$ behaves identically, and the two resolve the identity, so the whole Bloch sphere — not one point of it — is the null set of the gauge metric intersected with the states. The pure states are therefore the boundary of the state cone in two senses at once: the boundary of the Bloch ball for the probability form, and the null cone of the gauge metric.

## Named Readings of the Null States

Four further readings of the same computation are recorded here, each under a name of its own and each labelled a reading rather than a theorem; the identities they rest on are the body's.

- **Null-state bridge.** The pure states are the **intersection** of the gauge-metric null set, the zero-divisor cone and the trace-one slice, and the intersection is read as the bridge between the two forms of the row: it is where the definite form $H$ and the indefinite form $K$ describe the same elements. The reading is a statement about the state side of the gauge corner, and it is the positive counterpart of the no-go statement of *Why the Fourth Product Is a Gauge Structure and Not a State Space*.
- **Gauge length of a state.** The gauge invariant $K(\tilde\varrho,\tilde\varrho)=\tfrac14(1-\lvert\mathbf r\rvert^{2})$ is read as the **signed gauge length** of the state, a length for the gauge form in the sense in which $K$ is a ruler: it is zero on the pure boundary, $\tfrac14$ at the maximally mixed state, and it is the same number as the interval there. The name separates the length reading of the invariant from the mixedness reading, which the article already gives: mixedness is what the length measures.
- **Physical-sector boundary.** The null states are the boundary between what the framework treats as physical and what it treats as gauge, and the reading is offered in the Gupta–Bleuler shape — a physical space recovered after the null sector is quotiented out. The boundary is sharp and stated: the algebra supplies the null set and the two forms, and it supplies no rule that selects the quotient, so the name is a reading of the precedent and not a construction.
- **Three-valued label of the fourth product.** The order-three projections $\tilde\Pi(\mu)$, $(\mu,\mu)=\tfrac34$, are read as a three-valued internal label **carried by the fourth product**, to be set beside the two-valued label of a measurement; they are units of order three in the plain product, $\tilde\Pi(\mu)^{3}=e_0$, and not elements of a third product. The reading is already stated in §*The Other Projections: Three Values Instead of Two* and is repeated here only to give the name its place among the readings of the article; it remains a **speculation**, labelled, and the caution that $\mathbb{Z}/3$ is ubiquitous is unchanged.

## The Limits

- The article does not claim that the pure states are unphysical. A null element for $K$ is a fact about one form; the ghost question lives in the positivity of the probability form $H$, which *Mass, Rank and the Positivity of the Dagger* settles.
- The gauge metric is not the state-space inner product: the states are normalised by $H$, and $K$ is the indefinite pairing of the gauge corner.
- Isotropy is not special to the states: the $K$-null set is a cone of real dimension seven and contains elements that are not zero divisors, such as $e_0+e_1$, as well as elements that are, such as $e_0+ie_1$. What is special to the pure states is the triple coincidence of the $K$-null set, the zero-divisor cone and the trace-one slice.
- The reading of the order-three projections as an internal three-valued label is a **speculation**, labelled; it is not a claim that a measurement in the framework is three-valued.
- Whether the fundamental pairing of the framework is the trace at the informational sector with $H$ or a pairing at the material sector with $K$ is **open**; this article's position is that the states are normalised by $H$ and that $K$ is the metric of the gauge corner, and that position is stated rather than derived (*The Born Rule as a Trace Formula — Derivation and Comparison*).

## The Ledger

**Proved, and recomputed.** Every pure state $\tilde\Pi=\tfrac12(e_0+i\hat\mu)$, $\hat\mu$ a real unit vector, satisfies $K(\tilde\Pi,\tilde\Pi)=0$, $N(\tilde\Pi)=0$ and $\tilde\Pi\star\tilde\Pi=0$; the three are one computation on the coefficients $(\tfrac12,\tfrac i2\mu_1,\tfrac i2\mu_2,\tfrac i2\mu_3)$, and the last is also the matrix identity $\operatorname{adj}\Phi(\tilde\Pi)\Phi(\tilde\Pi)^{\dagger}=0$. The pure states are trace one, $\mathrm{Tr}\,\tilde\Pi=1$; they are positive for the probability form, $H(\tilde\Pi,\tilde\Pi)=\tfrac12$; and they are the projectors of the sesquilinear product, $\tilde\Pi\star_s\tilde\Pi=\tilde\Pi$. The family is the two-sphere of Bloch vectors. The projections of the fourth product are $0$, $e_0$ and the two-sphere $\tilde\Pi(\mu)=-\tfrac12e_0+\mu$ with $\mu$ real and $(\mu,\mu)=\tfrac34$; each satisfies $N(\tilde\Pi(\mu))=1$, $\tilde\Pi(\mu)^{3}=e_0$, $\mathrm{Tr}\,\tilde\Pi(\mu)=-1$, $\tilde\Pi(\mu)^{-1}=\tilde\Pi(\mu)^{\natural}=-\tfrac12e_0-\mu$ and $K=-\tfrac12$. Recomputed in a companion note and reproduced from *Idempotents of the General Quaternionic Sesquilinear Product*, *The Square of the General Quaternionic Sesquilinear Product and the Two Halves*, *The Krein Gram Matrix and the Restrictions of the Form* and *The General Quaternionic Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*.

**Reading.** That the states are the elements the indefinite metric cannot normalise; that they sit on the light cone of the framework; that the two projections — normalisable for $H$, null for $K$ — are the state side and the metric side of the same row; and that the two meters $K$ and $N$ agree on the informational sector, where the gauge invariant of a state is its mixedness, $K(\tilde\varrho,\tilde\varrho)=N(\tilde\varrho)=\tfrac14(1-\lvert\mathbf r\rvert^{2})$, so that the two forms part only off the state cone. Four further readings, named in §*Named Readings of the Null States*: **null-state bridge**, **gauge length of a state**, **physical-sector boundary**, and the **three-valued label of the fourth product**.

**Speculation, labelled.** That the order-three projections of the fourth product read as an internal three-valued label, in contrast with the two-valued projection of a measurement.

**Not claimed.** That a null state is unphysical; that the gauge metric's null set is the state space; that isotropy implies unphysicality; that a measurement in the framework is three-valued.

## Physical Readings

The article's reading is the boundary of the state space: a state must be normalisable, and the indefinite metric cannot normalise an element of zero length. Read against the cone, the elements a gauge metric cannot normalise are exactly the null elements of the algebra, so the zero-divisor cone is at once the locus of light and the boundary of the state space, which is the framework's sharpest statement about where a state can live. Read on the split, the article is the reason the gauge side and the state side are two structures rather than one, positivity being what makes the difference.

## Summary

A state must be normalisable, and normalisation is the work of the positive definite probability form $H$, whose positivity is what keeps the framework free of ghosts. The indefinite metric of the fourth product cannot do that work: **every pure state of the informational sector is null for it**. The pure states are the rank-one projectors $\tilde\Pi=\tfrac12(e_0+i\hat\mu)$ with $\hat\mu$ a real unit vector, the two-sphere of Bloch vectors; on the coefficients $(\tfrac12,\tfrac i2\mu_1,\tfrac i2\mu_2,\tfrac i2\mu_3)$ one computation gives three statements at once, the gauge invariant $K(\tilde\Pi,\tilde\Pi)=\tfrac14-\tfrac14=0$, the biquaternion norm $N(\tilde\Pi)=0$ and the fourth-product square $\tilde\Pi\star\tilde\Pi=0$. The states are therefore simultaneously **isotropic** for the gauge metric, **lightlike** on the zero-divisor cone, and **null** for the gauge product, while remaining positive and trace one for the probability form and its Born pairing: normalised by $H$, annihilated by $K$. The fourth product has projections of its own, the two-sphere $\tilde\Pi(\mu)=-\tfrac12e_0+\mu$ with $(\mu,\mu)=\tfrac34$, each a unit of the algebra of order three in the plain product, $N=1$ and $\tilde\Pi^{3}=e_0$, whose matrix is the unitary conjugate of $\operatorname{diag}(\omega,\omega^{2})$; they are not states, and the reading of them as an internal three-valued label is offered as a **speculation** and labelled, with the caution that $\mathbb{Z}/3$ is ubiquitous and that the framework supplies no three-valued process. The reading of the null states as the boundary between a physical and an unphysical sector is a hypothesis, and the caution is that isotropy is a statement about one form and does not by itself make a state unphysical. The positivity of the probability form is *Mass, Rank and the Positivity of the Dagger*; the gauge metric is *The Fourth Product and Its Indefinite Metric*; the vacuum is *The Biquaternion Vacuum as a Minimal Idempotent*; the state cone is *The Bloch Ball as the Trace-One Slice of the Future Light Cone*; the two-valued measurement is *Decoherence as Idempotent Projection*; and the gauge reading of the fourth product is *Why the Fourth Product Is a Gauge Structure and Not a State Space*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Pi=\tfrac12(e_0+i\hat\mu)$ | a pure state; $\hat\mu$ a real unit vector |
| $\hat\mu$ on $S^{2}$ | the Bloch vector; the Bloch sphere |
| $H(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q^{*})$ | the positive definite probability form; $\mathrm{Tr}\,\tilde\Pi=1$ |
| $K(\tilde P,\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ | the indefinite gauge metric; $K(\tilde\Pi,\tilde\Pi)=0$ |
| $N(\tilde Q)=\tilde Q\tilde Q^{\natural}=\sum_\mu Q_\mu^{2}$ | the biquaternion norm; $N(\tilde\Pi)=0$ |
| $\mathcal{N}=\{N=0\}$ | the zero-divisor cone; the light cone |
| $\{K=0\}$ | the gauge-metric null set; real cone of real dimension seven |
| $\tilde P\star_s\tilde Q=\tilde P\tilde Q^{*}$ | the sesquilinear product; the pure states are its projectors |
| $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q^{*}$ | the fourth product; the pure states are its null elements |
| $\tilde\Pi(\mu)=-\tfrac12e_0+\mu$, $(\mu,\mu)=\tfrac34$ | a projection of the fourth product; the two-sphere |
| $\tilde\Pi(\mu)^{3}=e_0$, $N=1$ | order three and norm one; a unit |
| $\omega=e^{2\pi i/3}$, $\{1,\omega,\omega^{2}\}$ | the cube roots of unity; the three-valued label |
| $\mathbb{M}_+,\mathbb{M}_-$ | the informational and material sectors |

## Further Reading

- Mathematics article *Idempotents of the General Quaternionic Sesquilinear Product* (`articles_maths/idempotents-of-the-quaternionic-sesquilinear-product.md`), for the criterion and the classification of the projections of the fourth product.
- Mathematics article *The Square of the General Quaternionic Sesquilinear Product and the Two Halves* (`articles_maths/the-square-of-the-quaternionic-sesquilinear-product-and-the-two-halves.md`), for the square, the gauge metric and the two halves of the algebra.
- Mathematics article *The Krein Gram Matrix and the Restrictions of the Form* (`articles_maths/the-krein-gram-matrix-and-the-restrictions-of-the-form.md`), for the null set of the gauge metric and the elements on which the two notions of nullity coincide.
- Mathematics article *The General Quaternionic Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-general-quaternionic-sesqualgebra-in-the-2x2-matrix-element-representation.md`), for the unitary-orbit theorem and the order-three matrices.
- Companion article *The Fourth Product and Its Indefinite Metric*, for the gauge metric on which these states are null.
- Companion article *Mass, Rank and the Positivity of the Dagger*, for the positivity of the probability form and the absence of ghosts.
- Companion article *The Biquaternion Vacuum as a Minimal Idempotent*, for the vacuum as the minimal projection and the zero-divisor property of the states.
- Companion article *The Bloch Ball as the Trace-One Slice of the Future Light Cone*, for the state cone and the pure states as its boundary.
- Companion article *Decoherence as Idempotent Projection*, for the two-valued measurement structure of the sesquilinear product.
- Companion article *Why the Fourth Product Is a Gauge Structure and Not a State Space*, which shows what the fourth product is instead of a state space.
