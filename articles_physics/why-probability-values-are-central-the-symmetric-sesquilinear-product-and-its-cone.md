# __Why Probability Values Are Central: the Symmetric Sesquilinear Product and Its Cone__

## Introduction

The companion article *The Hermitian Form as a Product: Positivity and the Real Part of the Born Pairing* introduced the symmetric half of the plain sesquilinear product,

$$
\tilde P\circledast\tilde Q=\mathrm{Sc}\bigl(\tilde P\tilde Q^{*}\bigr)e_0=H(\tilde P,\tilde Q)e_0,\qquad H(\tilde P,\tilde Q)=P_0\overline{Q_0}+(\mathbf P,\overline{\mathbf Q}),
$$

and read its diagonal as a probability. This article asks the question that the title puts forward: **why are the values central?** The answer is not a small technicality but the whole content of the block, and it separates the block from the quaternionic sesquilinear row that is its nearest neighbour.

Three readings are developed. First, **a value of the block is a number and not a direction**: the image is the centre, so a product of two elements is a complex scalar times $e_0$ and carries no vector information at all. Second, **the cone of the operation is one-dimensional**: the squares generate the non-negative central ray, which is the normalisation direction of the state space, and not the state cone. Third, **the operation has only the two trivial idempotents** $0$ and $e_0$, so the projectors that the corpus calls pure states are *not* idempotents of this operation; the operation produces probability values and selects no state. The last section states the contrast with the symmetric quaternionic sesquilinear product, whose values are not central: the two symmetric sesquilinear products do not divide the state side between them, and only this one is positive.

**Boundaries.** The centrality, the conjugate-commutative law and the idempotents are *The Conjugate-Commutative Law and the Idempotents of the Symmetric Plain Sesqualgebra*; the restrictions and the closure of the six subspaces are *The Six Subspaces under the Symmetric Plain Sesqualgebra of Biquaternions*; the positivity of the form, its cone and its signature are *Mass, Rank and the Positivity of the Dagger* and *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*. The state space, the Bloch ball and its cone are *The Bloch Ball as the Trace-One Slice of the Future Light Cone*, *Quantum Physics in Biquaternionic Form* and *The Ontology of the Quantum State under the Biquaternion Framework*; the projections of the algebra and their role in measurement are *Decoherence as Idempotent Projection* and *The Measurement Problem in Algebraic Form*. The quaternionic row and its indefinite form are *The Fourth Product and Its Indefinite Metric*, *The States the Indefinite Metric Cannot Normalise* and *Why the Fourth Product Is a Gauge Structure and Not a State Space*, and the matrix side of the Krein form $K$ is *The Krein Gram Matrix and the Restrictions of the Form*.

**Conventions.** As in the companion article and in *Conventions in the Biquaternion Universe*: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$, $e_k^{2}=-e_0$, $e_1e_2=e_3$; $\tilde Q=Q_0e_0+\mathbf Q$, $Q_\mu\in\mathbb{C}$; ${}^{\natural}$ the natural conjugation, $\overline{\cdot}$ the coefficientwise one, ${}^{*}=\overline{\cdot}\circ{}^{\natural}$; $\mathrm{Sc}$ the scalar part, $\mathrm{Tr}=2\,\mathrm{Sc}$; the centre $\mathbb{C}_{\mathbb{B}}=\{\lambda e_0\}$; the sectors $\mathbb{M}_{+}$ (Hermitian, informational) and $\mathbb{M}_{-}$ (anti-Hermitian, material). The operation of the block is written $\tilde P\circledast\tilde Q$; the fourth product is $\tilde P^{\natural}\tilde Q^{*}$ and its symmetric part is written $\mathrm{SQS}(\tilde P,\tilde Q)=\tfrac12(\tilde P^{\natural}\tilde Q^{*}+\tilde Q^{*}\tilde P^{\natural})$, whose scalar form is the **Krein form** $K(\tilde P,\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ with $\varepsilon=(1,-1,-1,-1)$; the general quaternionic bilinear form is $N$. The Hermitian form is $H=\langle\cdot,\cdot\rangle_{*}$, its diagonal is $H(\tilde Q,\tilde Q)=\sum_\mu\lvert Q_\mu\rvert^{2}$, and the biquaternion norm is $N(\tilde Q)=\tilde Q\tilde Q^{\natural}$.

## The Values Are Central

### The Image Is the Centre

Every value of the operation is a scalar multiple of $e_0$, because the symmetric half of an element and its natural conjugate has no vector part:

$$
\tilde P\circledast\tilde Q=\mathrm{Sc}\bigl(\tilde P\tilde Q^{*}\bigr)e_0\in\mathbb{C}_{\mathbb{B}} .
$$

The image of the multiplication is therefore the **centre** of the algebra, $\mathbb{C}_{\mathbb{B}}=\{\lambda e_0\}$, and the operation has **rank one** over $\mathbb{C}$: it is a form, not a genuine multiplication, and it cannot reproduce a vector part on either side (*The Hermitian Form as a Product on the Symmetric Plain Sesqualgebra*).

**Remark (verified).** For $100$ random pairs the vector part of the half-sum vanished identically, the central coefficient reproducing $H(\tilde P,\tilde Q)$ to $<10^{-13}$.

### The Law

The centrality has one immediate consequence for the law. Because the value is central, the transposition of the arguments is read through the coefficientwise conjugation of a scalar,

$$
\tilde P\circledast\tilde Q=\overline{\tilde Q\circledast\tilde P},
$$

the **conjugate-commutative law**, and the law is the Hermitian symmetry $H(\tilde Q,\tilde P)=\overline{H(\tilde P,\tilde Q)}$ of the form written on the product (*The Conjugate-Commutative Law and the Idempotents of the Symmetric Plain Sesqualgebra*). The two involutions of the block act differently and record the conjugation in its two roles: the natural conjugation is an automorphism, $\tilde P^{\natural}\circledast\tilde Q^{\natural}=\tilde P\circledast\tilde Q$, and the Hermitian conjugation is the reversal, $\tilde P^{*}\circledast\tilde Q^{*}=\overline{\tilde P\circledast\tilde Q}$.

**Remark (none of the laws of the algebra rows).** The operation is neither commutative nor associative and has no unit. It is the exact opposite of the symmetric plain algebra $\mathrm{SPA}$, which is commutative, unital and Jordan. The law and the unit, not the mere sign of the second slot, are what place the block in the sesqualgebra row.

## Why Centrality Matters

### A Number and Not a Direction

A central value is a complex **number**. It carries no vector direction, and this is exactly what a probability value is: a number, not a state and not a direction. The parent value $\tilde P\tilde Q^{*}$ is an element of the algebra and can carry a vector part; the symmetric half is its scalar part, what remains when the vector part is set aside, and what remains is the number that the corpus reads as a probability (the companion band reads the set-aside vector part as a phase). The centrality is therefore the algebraic reason a probability is a scalar.

**Remark (the reading, offered and labelled).** The centre of the algebra is the fixed set of its automorphisms, and the internal action of the framework — the sandwich $\tilde R\mapsto\tilde U\tilde R\tilde U^{*}$ of *Observables, Gauge Generators and the Chirality of the Internal Action* — fixes every central element. **Read this way, a central probability is a number invariant under the internal action**, and the direction that the operation discards is the datum that the internal action moves. This is a reading of the two algebraic facts and is labelled as such; the algebra establishes only that the value is central and that the automorphisms fix the centre.

### The Diagonal on the State Side

The centrality also organises the **square** of a state. For $\tilde\rho=\tfrac12(e_0+i\mathbf r)$ one has

$$
\tilde\rho\circledast\tilde\rho=H(\tilde\rho,\tilde\rho)e_0=\tfrac14\bigl(1+\lvert\mathbf r\rvert^{2}\bigr)e_0=\tfrac12\,\mathrm{Tr}\bigl(\tilde\rho^{2}\bigr)e_0,
$$

so the diagonal of a state is one half of its **purity**, a central number. The state's Bloch vector $\mathbf r$ enters this value through its length alone: the square of an element sees the magnitude of the coherence and not its orientation. The orientation is carried by the antisymmetric half of the same square, where $\tilde\rho\wedge_{*}\tilde\rho=\tfrac12 i\mathbf r$. The two halves of the **square** therefore split the state into its purity, a central number, and its coherence direction, a vector, and this block owns the number. The operation is not blind to orientation when it is given two elements — on $\mathbb{M}_{+}$ the form is positive definite of rank four, so the pairing of two different states does depend on their relative direction — but the value of the square of one element carries none.

**Remark (verified).** $\tilde\rho\circledast\tilde\rho=\tfrac12\mathrm{Tr}(\tilde\rho^{2})e_0$ to $<10^{-13}$ over $100$ random states.

## The Cone of the Operation

### The Squares Generate a Ray

The values of the operation are the whole centre, but the values that are **squares** are not. Since

$$
\tilde Q\circledast\tilde Q=H(\tilde Q,\tilde Q)e_0=\Bigl(\sum_{\mu=0}^{3}\lvert Q_\mu\rvert^{2}\Bigr)e_0,
$$

the square of an element is a **non-negative real** multiple of $e_0$, and every non-negative real multiple is attained (take $\tilde Q=\sqrt t\,e_0$). The square map therefore has image the closed ray

$$
\{\tilde Q\circledast\tilde Q\}=\mathbb{R}_{\ge0}\,e_0 ,
$$

a **one-dimensional cone** in the two-dimensional centre. The cone of the operation is the positive central ray, and nothing more.

### It Is Not the State Cone

The ray is the **normalisation direction** of the state space, not the state space. The states of the framework are the positive trace-one elements of $\mathbb{M}_{+}$, and their cone is the future light cone of the biquaternion norm with its trace-one slice, the Bloch ball (*The Bloch Ball as the Trace-One Slice of the Future Light Cone*, *Mass, Rank and the Positivity of the Dagger*). That cone is four-dimensional in the real reading of $\mathbb{M}_{+}$ and is **not** generated by the squares of this operation: the operation's cone lies inside the centre, along the trace direction, and the state cone lies in $\mathbb{M}_{+}$ and is carved by the biquaternion norm.

| object | side | what generates it | dimension |
|---|---|---|---|
| cone of the operation | $\mathbb{C}_{\mathbb{B}}$ | squares $\tilde Q\circledast\tilde Q$ | $1$ over $\mathbb{R}$ |
| state cone of the corpus | $\mathbb{M}_{+}$ | the future cone $N\ge0$ on the Hermitian side, sliced by $\mathrm{Tr}\tilde\rho=1$ | $4$ over $\mathbb{R}$ |

**Remark (the reading).** The operation supplies the **scale of a probability** and not the **set of states**. Its positivity is a positivity of numbers, and the state cone is supplied by the biquaternion norm and by the trace normalisation, both of which are owned elsewhere. The word "central" in the title is therefore exact in both senses: the values are central in the algebra, and they are central to the reading because they are the normalisation the state space needs and does not itself produce.

## The Idempotents and the Projections

### Only Two Idempotents

The idempotents of the operation are the elements $\tilde Q$ with $\tilde Q\circledast\tilde Q=\tilde Q$. Since the value is central, the equation forces $\tilde Q$ into the centre, where the operation is the field rule $(\lambda e_0)\circledast(\mu e_0)=\lambda\overline{\mu}\,e_0$; the equation becomes $\lvert\lambda\rvert^{2}=\lambda$, whose roots are $0$ and $1$. The idempotents are therefore exactly

$$
0\quad\text{and}\quad e_0 ,
$$

the two trivial ones (*The Conjugate-Commutative Law and the Idempotents of the Symmetric Plain Sesqualgebra*). There is no idempotent of the operation attached to a direction.

### A Projector Is Not an Idempotent of the Operation

The corpus's pure states are the idempotents of the algebra, $\tilde\Pi_{\pm}(\hat{\boldsymbol{\mu}})=\tfrac12(e_0\pm i\hat{\boldsymbol{\mu}})$ with $\lvert\hat{\boldsymbol{\mu}}\rvert=1$; they are the rank-one projections and the boundary of the Bloch ball (*The Born Rule as a Trace Formula — Derivation and Comparison*, *Decoherence as Idempotent Projection*). Under the operation of this block,

$$
\tilde\Pi_{\pm}\circledast\tilde\Pi_{\pm}=H(\tilde\Pi_{\pm},\tilde\Pi_{\pm})e_0=\tfrac12\,e_0 ,
$$

for **every** unit direction $\hat{\boldsymbol{\mu}}$. A pure state is therefore **not an idempotent** of the operation, and, sharper still, all pure states have the same **self-pairing** $\tfrac12 e_0$: the diagonal of the block on the pure states is constant and carries no orientation, which is why the operation's idempotent equation finds only $0$ and $e_0$. What the operation does see is the **relative** direction of two elements, because on $\mathbb{M}_{+}$ the form is positive definite of rank four and

$$
H\bigl(\tilde\Pi_{\pm}(\hat{\boldsymbol{\mu}}),\tilde\Pi_{\pm}(\hat{\boldsymbol{\nu}})\bigr)=\tfrac12\cos^{2}\frac{\theta}{2},\qquad \hat{\boldsymbol{\mu}}\cdot\hat{\boldsymbol{\nu}}=\cos\theta,
$$

so two states of different direction are separated by the pairing even though each has the same diagonal. The value $\tfrac12 e_0$ is one half of the trace pairing of a projector with itself — the halved certainty $\mathrm{Tr}(\tilde\Pi^{2})=1$ — and it is the diagonal of a state and not a measurement of one.

**Reading (the overlap, and where the factor of two sits).** The value $H(\tilde\Pi(\hat{\boldsymbol{\mu}}),\tilde\Pi(\hat{\boldsymbol{\nu}}))=\tfrac12\cos^{2}(\theta/2)$ is **one half of the Born overlap** of the two states; twice it, $\cos^{2}(\theta/2)$, is the **transition probability** that a state prepared in the direction $\hat{\boldsymbol{\mu}}$ passes a test prepared in the direction $\hat{\boldsymbol{\nu}}$, maximal at $\theta=0$ and vanishing at $\theta=\pi$. The constant self-pairing $\tfrac12 e_0$ and the varying relative pairing are the two faces of one fact: a state has no orientation against itself and a full one against another, so the **diagonal of the operation is uninformative and its off-diagonal carries the relative amplitude**. The one half is the same one half that makes the operation one half of the Born trace pairing, and it must be carried in the comparison, not dropped.

**Remark (verified).** $H(\tilde\Pi_{\pm},\tilde\Pi_{\pm})=\tfrac12$ for every projector of the corpus, so $\tilde\Pi_{\pm}\circledast\tilde\Pi_{\pm}=\tfrac12e_0$, and $H(\tilde\Pi(\hat{\boldsymbol{\mu}}),\tilde\Pi(\hat{\boldsymbol{\nu}}))=\tfrac12\cos^{2}(\theta/2)$; the two directions are separated by the pairing, showing that the block is not blind to orientation even though its diagonal is constant. No nontrivial idempotent of the operation exists, the idempotent equation reducing on the centre to $\lvert\lambda\rvert^{2}=\lambda$.

### The Operation Selects No State

The two facts combine into the reading that this article and its companion share. A projection is an idempotent of the algebra; the operation's idempotents are $0$ and $e_0$; hence the operation contains **no projector of the corpus** and **selects no state**. The operation compares two elements and returns a number; the state is a separate, normalised element of $\mathbb{M}_{+}$ with a direction, supplied by the state side and by the trace normalisation, and the operation's *diagonal* on the states is the same for all of them. The boundary with the idempotent-and-projection articles is exact: those articles own the idempotents of the algebra and their role in measurement; this article owns the idempotents of the *operation*, which are the two trivial ones, and records that they do not coincide with the algebra's.

**Remark (no measurement is read from the operation).** The measurement structure of the framework is the sandwich $\tilde Q\mapsto\tilde A\tilde Q\tilde A^{*}$ applied with a unitary or a Hermitian idempotent acting element (*The Measurement Problem in Algebraic Form*, *Decoherence as Idempotent Projection*), and this block is none of it. A probability value read from the operation is not a measurement outcome; the operation is a pairing.

## The Contrast with the Quaternionic Row

The other symmetric part of the sesquilinear side of the twelve is the **symmetric quaternionic sesquilinear product**, the symmetric half of the fourth product $\tilde P^{\natural}\tilde Q^{*}$,

$$
\mathrm{SQS}(\tilde P,\tilde Q)=\tfrac12\bigl(\tilde P^{\natural}\tilde Q^{*}+\tilde Q^{*}\tilde P^{\natural}\bigr)=\bigl[P_0\overline{Q_0}-(\mathbf P,\overline{\mathbf Q})\bigr]e_0-P_0\overline{\mathbf Q}-\overline{Q_0}\,\mathbf P,
$$

whose scalar part is the **indefinite** Krein form $K(\tilde P,\tilde Q)=P_0\overline{Q_0}-(\mathbf P,\overline{\mathbf Q})$ and whose vector part is the mixed term alone (*Introduction to the General Quaternionic Sesqualgebra of Biquaternions*, *The Krein Gram Matrix and the Restrictions of the Form*). The comparison is exact and instructive, and it does not go in the direction a reader might expect.

**The value is not central.** The value of the quaternionic block is $K(\tilde P,\tilde Q)e_0-P_0\overline{\mathbf Q}-\overline{Q_0}\mathbf P$, a general element with a complex scalar part and a vector part; it lies in **no subspace of the six**, and the block is therefore not a form read on the centre but a genuine element-valued operation.

**The diagonal is not central and not definite.** For $\tilde P=\tilde Q$,

$$
\mathrm{SQS}(\tilde Q,\tilde Q)=\bigl[\lvert Q_0\rvert^{2}-\lvert\mathbf Q\rvert^{2}\bigr]e_0-2\,\mathrm{Re}\bigl(Q_0\overline{\mathbf Q}\bigr),
$$

an indefinite scalar part together with a real vector part; the restriction of the scalar form to the vector subspace is negative definite, and over the complex coefficients the form has inertia $(1,3)$, over the real parameters $(2,6)$, with a large isotropic set (the pure states of the corpus are *null* for it, *The States the Indefinite Metric Cannot Normalise*, *The Fourth Product and Its Indefinite Metric*).

| feature | SPS, this block | SQS, the quaternionic block |
|---|---|---|
| value | central, $\mathbb{C}_{\mathbb{B}}$ | non-central, in no subspace of the six |
| law | conjugate-commutative | conjugate-commutative |
| scalar form | $H$, positive definite | $K$, indefinite, inertia $(1,3)$ over $\mathbb{C}$ |
| diagonal | $\sum_\mu\lvert Q_\mu\rvert^{2}$, real, $>0$ off $0$ | indefinite scalar $+$ real vector |
| reading | probability | gauge structure |

**The two products do not divide the state side.** This is the point of the comparison. The two symmetric sesquilinear products share the law — both are conjugate-commutative and sesquilinear over $(\mathbb{C},\bar{\cdot}\,)$ — and the law does not separate them. They are separated by the **positivity of the scalar form**, and the separation is total: the plain block is positive and reads as probability; the quaternionic block is indefinite, has no positivity and reads as the **gauge structure** of the frame and not as a state structure (*Why the Fourth Product Is a Gauge Structure and Not a State Space*, *The Fourth Product and Its Indefinite Metric*). The state side of the corpus is therefore **not split** between the two; it is carried by the plain row, and the quaternionic row carries the invariant indefinite metric of the transformations. A reader who expects one positive product per side will find instead one positive product and one indefinite product, on one side.

**Remark (the exact wording of the boundary).** The last sentence must not be over-read: the quaternionic form is not "the same probability with a minus sign". It is indefinite and its pure states are null for it; the plain form is definite and its value is the probability. The contrast is stated at the level of the forms and does not compare the two operations' values term by term.

## Ledger

**What centrality gives.**
- A probability value is a **central number**, unpacked from the algebra and not chosen.
- The law is conjugate-commutative, and the natural conjugation is an automorphism while the star is the reversal.
- The diagonal of a state is its **purity**, one half of $\mathrm{Tr}(\tilde\rho^{2})$.
- The relative pairing is **one half of the Born overlap**: $2H(\tilde\Pi(\hat{\boldsymbol{\mu}}),\tilde\Pi(\hat{\boldsymbol{\nu}}))=\cos^{2}(\theta/2)$ is the transition probability, the diagonal being uninformative and the off-diagonal carrying the relative amplitude.

**What it does not give.**
- It gives no orientation: every pure state has the same self-pairing $\tfrac12 e_0$, and its idempotents are only $0$ and $e_0$. The orientation is carried by the antisymmetric diagonal and by the relative pairing of two distinct elements.
- Its cone is the one-dimensional positive central ray, the normalisation direction, not the state cone.
- It is not a state, not a measurement, and not a symmetry algebra.

## Summary

The values of the symmetric plain sesquilinear product are the **centre** of the algebra, $\tilde P\circledast\tilde Q=H(\tilde P,\tilde Q)e_0\in\mathbb{C}_{\mathbb{B}}$, and the operation is a one-dimensional form: a value is a number and not a direction, which is the algebraic sense in which a probability is a scalar. The law is **conjugate-commutative**, the natural conjugation acts as an automorphism and the Hermitian conjugation as the reversal, and on the state side the diagonal of a state is its **purity**, $\tilde\rho\circledast\tilde\rho=\tfrac12\mathrm{Tr}(\tilde\rho^{2})e_0$, while the **relative** pairing of two states is one half of the Born overlap, $2H=\cos^{2}(\theta/2)$, so the diagonal of the operation is uninformative and its off-diagonal carries the transition amplitude. The **cone of the operation** is the closed positive central ray generated by the squares, a one-dimensional cone which is the normalisation direction of the state space and **not** the state cone, the latter being the future light cone of the biquaternion norm with its trace-one Bloch-ball slice. The **idempotents** of the operation are exactly $0$ and $e_0$, so the corpus's pure states, the rank-one projectors $\tilde\Pi_{\pm}$, are **not idempotent** under it: $\tilde\Pi_{\pm}\circledast\tilde\Pi_{\pm}=\tfrac12 e_0$ for every unit direction. The operation therefore creates probability values and **selects no state**, and the boundary with the idempotent-and-projection articles is drawn there. Finally the contrast with the **symmetric quaternionic sesquilinear product**: the two blocks share the law but not the form, since the quaternionic value is non-central, lies in no subspace of the six, and carries the indefinite form $K$; the two symmetric sesquilinear products therefore do not divide the state side between them, and the state side is carried by the plain row alone.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\circledast\tilde Q=H(\tilde P,\tilde Q)e_0$ | the operation of the block; the values are central |
| $\mathbb{C}_{\mathbb{B}}=\{\lambda e_0\}$ | the centre; the image of the operation |
| $\tilde P\circledast\tilde Q=\overline{\tilde Q\circledast\tilde P}$ | the conjugate-commutative law |
| $\tilde\rho\circledast\tilde\rho=\tfrac12\mathrm{Tr}(\tilde\rho^{2})e_0$ | the diagonal of a state is its purity |
| $\{\tilde Q\circledast\tilde Q\}=\mathbb{R}_{\ge0}e_0$ | the one-dimensional cone of the operation |
| $\{0,e_0\}$ | the idempotents of the operation |
| $\tilde\Pi_{\pm}\circledast\tilde\Pi_{\pm}=\tfrac12 e_0$ | a projector is not an idempotent of the operation; $H(\tilde\Pi(\hat{\boldsymbol{\mu}}),\tilde\Pi(\hat{\boldsymbol{\nu}}))=\tfrac12\cos^{2}(\theta/2)$ |
| $\mathrm{SQS}(\tilde P,\tilde Q)=\tfrac12(\tilde P^{\natural}\tilde Q^{*}+\tilde Q^{*}\tilde P^{\natural})$ | the symmetric quaternionic sesquilinear product |
| $K(\tilde P,\tilde Q)=P_0\overline{Q_0}-(\mathbf P,\overline{\mathbf Q})$ | the indefinite Krein form of the quaternionic row |
| $\mathbb{M}_{+}$ | the state side, carried by the plain row alone |

## Further Reading

- *The Conjugate-Commutative Law and the Idempotents of the Symmetric Plain Sesqualgebra* (`articles_maths/the-conjugate-commutative-law-and-the-idempotents-of-the-symmetric-plain-sesqualgebra.md`), for the law and the idempotents.
- *The Six Subspaces under the Symmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/the-six-subspaces-under-the-symmetric-plain-sesqualgebra-of-biquaternions.md`), for the closure of the six.
- *The Hermitian Form as a Product: Positivity and the Real Part of the Born Pairing* (`articles_physics/the-hermitian-form-as-a-product-positivity-and-the-real-part-of-the-born-pairing.md`), the companion article of the band.
- *The Bloch Ball as the Trace-One Slice of the Future Light Cone* (`articles_physics/the-bloch-ball-as-the-trace-one-slice-of-the-future-light-cone.md`), which owns the state cone.
- *Decoherence as Idempotent Projection* (`articles_physics/decoherence-as-idempotent-projection.md`), which owns the idempotents of the algebra and the projections.
- *The Measurement Problem in Algebraic Form* (`articles_physics/the-measurement-problem-in-algebraic-form.md`), where the corpus puts measurement.
- *The Fourth Product and Its Indefinite Metric* (`articles_physics/the-fourth-product-and-its-indefinite-metric.md`), for the quaternionic row and its indefinite form.
- *The States the Indefinite Metric Cannot Normalise* (`articles_physics/the-states-the-indefinite-metric-cannot-normalise.md`), for the states that the quaternionic form makes null.
- *The Krein Gram Matrix and the Restrictions of the Form* (`articles_maths/the-krein-gram-matrix-and-the-restrictions-of-the-form.md`), for the Krein form $K$, its Gram matrix and its inertia.
