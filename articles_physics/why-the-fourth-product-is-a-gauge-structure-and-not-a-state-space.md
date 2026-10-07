# __Why the Fourth Product Is a Gauge Structure and Not a State Space__

## Introduction

A gauge transformation is not a state. It is an operation that acts on states and on fields and leaves the physical predictions alone; the group of gauge transformations is a group of **transformations**, and asking for its cone of positive elements is a category mistake. What distinguishes a structure of states from a structure of transformations is **positivity**: a state space is a cone, ordered by a positive definite pairing, with a distinguished unit-trace slice whose boundary elements are the pure states; a structure of transformations has a composition and often a bracket, and no cone at all.

This article closes the fourth block by showing which of the two the fourth product supplies, and the answer is the second. The fourth product has no unit and is not associative, so its natural replacement is a **ternary product**, and that ternary product has exactly the parity of a **Jordan triple** — the algebraic gateway through which a cone of states is reconstructed in the standard theory of operator algebras. The gateway is inspected here and the last axiom is missing: the **Jordan triple identity fails** for the fourth product, at an explicit witness of basis elements, and it fails on nearly half of the basis five-tuples. The consequence is a no-go statement. No Jordan structure, no cone, no pure states and no transition probabilities can be reconstructed from the fourth product's ternary structure; the state space of the framework remains the positive cone carried by the sesquilinear product, and the fourth product is read as the **gauge structure** — a composition of transformations with an invariant indefinite metric and no positivity.

The article owns the no-go, the transformation reading, and the closing ledger of the block. It defers the ternary product, the parity theorem and the failure itself to the mathematics articles *The Ternary Product and the Failure of the Jordan Triple Identity*, *The Sesquilinear Associator and the Ternary Product*, *Algebraic J\*-Algebras* and *Jordan Triples with an Involution*; the positivity and the cone to *Mass, Rank and the Positivity of the Dagger*; the gauge metric to *The Fourth Product and Its Indefinite Metric*; and the null states to *The States the Indefinite Metric Cannot Normalise*.

**Conventions.** As in the companion articles of this block: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$, $e_k^{2}=-e_0$, $e_1e_2=e_3$; the fourth product $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q^{*}$; the sesquilinear product $\tilde P\star_s\tilde Q=\tilde P\tilde Q^{*}$; the plain product $\tilde P\tilde Q$; the conjugations ${}^{\natural}$, ${}^{*}$ and the coefficientwise bar; $\mathrm{Sc}$ the scalar part and $\mathrm{Tr}=2\,\mathrm{Sc}$. The sectors are $\mathbb{M}_+$ and $\mathbb{M}_-$, and $H$ and $K$ are the probability form and the gauge metric. All conventions are those of *Conventions in the Biquaternion Universe*.

## Transformations and States

Two structures must be kept apart, and the whole article turns on the distinction.

**A state space is a cone with a unit.** The states of the framework are the positive trace-one elements of the informational sector for the probability form $H$; the pure ones are its rank-one projectors; and the Born rule is a ratio of two $H$-pairings. Everything in that sentence uses positivity: the cone is a cone because $H$ is positive definite, the boundary is a boundary because the form has a sign, and the transition probabilities are ratios of positive numbers. A structure that has a composition and a bracket but no positive form cannot carry any of it.

**A gauge structure is a composition of transformations.** A gauge transformation acts on the algebra by conjugation-like maps and composes with the others; its invariants are the pairings left unchanged, and its natural home is a group or a Lie algebra, not a cone. The framework's internal action is of this kind: the sandwich

$$
\Theta_{\tilde U}(\tilde R)=\tilde U\tilde R\tilde U^{*}
$$

with $\tilde U$ a unitary of the slice is an isometry of the frame and a transformation of the internal field, and the composition of two such sandwiches is again a sandwich. The statement that the internal action is **one-sided** — that only the right multiplication by a unitary is an isometry of the fourth product's form — is *Observables, Gauge Generators and the Chirality of the Internal Action*, and it is the operator face of the same distinction: the algebra has an action structure with a chirality, and its state structure lives in another product.

**The question of the block.** The fourth product is the corner of the four that the framework assigns to gauge. Its metric is indefinite, its states are null, and it has no unit. The natural way to repair a product without a unit is to pass to its **ternary product** — a composition of three rather than two — and the natural question is whether that ternary product carries a state space. The rest of the article answers it.

## The Ternary Product: a Gateway to a State Space

### The Ternary Product and Its Parity

With no unit and no associativity, the natural replacement for the binary product is

$$
\{\tilde P,\tilde Q,\tilde R\}=(\tilde P\star\tilde Q)\star\tilde R^{*}=\overline{\tilde Q}\,\tilde P\,\tilde R,
$$

the plain product of the conjugated middle factor with the outer two. It is additive in each variable and its parities are

$$
\{\lambda\tilde P,\tilde Q,\tilde R\}=\lambda\{\tilde P,\tilde Q,\tilde R\},\qquad
\{\tilde P,\lambda\tilde Q,\tilde R\}=\bar\lambda\{\tilde P,\tilde Q,\tilde R\},\qquad
\{\tilde P,\tilde Q,\lambda\tilde R\}=\lambda\{\tilde P,\tilde Q,\tilde R\},
$$

$\mathbb{C}$-linear in the first and the third slots and conjugate-linear in the middle. That is exactly the parity of a **Jordan triple with an involution**: linear in the two outer slots, conjugate-linear in the middle.

### The Left Model

Under the relabelling $\tilde X=\tilde Q^{\natural}$, $\tilde Y=\tilde P$, $\tilde Z=\tilde R$ the ternary product becomes

$$
\{\tilde P,\tilde Q,\tilde R\}=\tilde X^{*}\,\tilde Y\,\tilde Z,
$$

the **left** model of the ternary products of the algebra. The sibling sesquilinear product has the **middle** model $\tilde X\tilde Y^{*}\tilde Z$, and the mathematics' parity theorem is that the identity is a property of the middle model, not of the left one: the two models have the same parity and different theorems.

### Why the Parity Is a Gateway

The parity matters because of the standard reconstruction, and it is worth stating, since the physical reading turns on it. An **algebraic $J^{*}$-algebra** — a ternary product of one of the two models satisfying the Jordan triple identity — is the algebraic form of a **JB\*-triple**, and a JB\*-triple carries a state space: its predual carries the normal states, whose extreme points are the pure states, and the ternary product supplies the Jordan structure from which the cone, the transition probabilities and the dynamics are built. When the identity holds for a model, a ternary product of that model is a state space in the making. The fourth product has the parity, and its ternary product is the left model; the hypothesis that suggests itself is that it too carries a state space. The next section shows that it does not.

## The Identity Fails

### The Witness

The Jordan triple identity is

$$
\{x,y,\{u,v,w\}\}=\{\{x,y,u\},v,w\}-\{u,\{y,x,v\},w\}+\{u,v,\{x,y,w\}\},
$$

and it **fails** for the ternary product of the fourth product. On the basis elements $(x,y,u,v,w)=(e_0,e_1,e_0,e_2,e_0)$ the left-hand side is $e_3$ while the right-hand side is $-3e_3$: the two differ by $4e_3$, and the identity is false.

The computation is short and exact, and it uses only real basis coefficients. For the left-hand side, the inner bracket is $\{e_0,e_2,e_0\}=\bar e_2e_0e_0=e_2$, and then $\{e_0,e_1,e_2\}=\bar e_1e_0e_2=e_3$. For the right-hand side, $\{\{e_0,e_1,e_0\},e_2,e_0\}=\{e_1,e_2,e_0\}=e_2e_1=-e_3$, then $-\{e_0,\{e_1,e_0,e_2\},e_0\}=-\{e_0,e_3,e_0\}=-e_3$, then $\{e_0,e_2,\{e_0,e_1,e_0\}\}=\{e_0,e_2,e_1\}=e_2e_1=-e_3$; the three terms sum to $-3e_3$. The failure is by a factor of four, on basis elements, with real coefficients.

### The Failure Is Not Marginal

Of the $1024$ five-tuples of basis elements, **$480$ make the identity fail** and $544$ make it hold, so the failure is not a small-set phenomenon. The witness has real coordinates and lies in the associative real quaternion subalgebra; the failure survives restriction to every real subspace on which the two conjugations differ, and it is not repaired on the quaternion subspace. The identity holds when all five arguments are central — on the centre the product is commutative and associative — and the passage from the centre to the algebra is the passage from commuting scalars to the non-commuting product: the same passage on which the multiplication first fails to be associative.

### The Operator Form

The failure is visible in the operators. With $\Theta_{\tilde X,\tilde Y}(\tilde R)=\{\tilde X,\tilde Y,\tilde R\}$, the identity is equivalent to the commutator identity

$$
[\Theta_{\tilde X,\tilde Y},\Theta_{\tilde U,\tilde V}]
=\Theta_{\{\tilde X,\tilde Y,\tilde U\},\tilde V}-\Theta_{\tilde U,\{\tilde Y,\tilde X,\tilde V\}},
$$

and for the fourth product the operator identity fails: at $\tilde X=\tilde U=e_0$, $\tilde Y=e_1$, $\tilde V=e_2$, the two sides applied to a common argument are the left multiplications by $2e_3$ and by $-2e_3$. The operators $\Theta_{\tilde P,\tilde Q}$ are the plain left multiplications by $\overline{\tilde Q}\tilde P$, so the failure says that the left multiplications of the algebra close on a bracket that is not the bracket the identity demands. In a genuine Jordan triple these operators generate a Lie algebra of derivations — the first step of the Tits–Kantor–Koecher construction — and here they do not, so that construction is unavailable.

## What Survives: a Structure of Transformations

The failure has one consequence and it is the article's subject: **no state space can be built from the fourth product**.

**The reconstruction is blocked at the first step.** A state space built from a ternary product requires the identity, because the identity is what makes the ternary product a Jordan structure and what makes the operators derivations. With the identity false, there is no Jordan structure, no cone, no order, no pure states and no transition probabilities. The framework's states remain the positive cone of the probability form $H$, whose positivity is *Mass, Rank and the Positivity of the Dagger*, and the null states of the fourth product remain where they were, on the boundary of the gauge metric, as *The States the Indefinite Metric Cannot Normalise* records.

**What the fourth product does supply.** Three things survive, and they are exactly what a gauge structure needs.

- **A composition of transformations.** The composition of two one-sided actions of the fourth product is the sandwich $L_{\tilde A}\circ L_{\tilde B}(\tilde X)=\tilde A^{\natural}\tilde X\overline{\tilde B}$, and with $\tilde A,\tilde B$ unitaries this is a transformation of the internal frame that composes and has an inverse. It is a group-like structure acting on the algebra.
- **An invariant metric.** The gauge metric $K$ of *The Fourth Product and Its Indefinite Metric*, with its signature $(1,3)$ and its isometry group $U(1,3)$, is the pairing the transformations leave unchanged — the invariant form that a gauge structure has in place of a positive cone.
- **A bracket without a cone.** The operators of the ternary product close under a commutator, and the identity that would make them derivations is false; a bracket is a Lie-algebra-like datum, and positivity is not in it.

The positive result is therefore the division of labour of the block: the fourth product supplies the **transformation side** of the algebra — the indefinite metric, the gauge transformation law and the ternary composition — and the sesquilinear product supplies the **state side** — the cone, the Born pairing and the pure states. The two are read together and are not unifiable into one algebraic triple, because the identity that would unify them is the identity that fails.

## The Block Collected

The fourth block reads one product, and its three articles divide the reading.

| Article | What it owns |
|---|---|
| *The Fourth Product and Its Indefinite Metric* | the product, its scalar form $K$, the signature $(1,3)$, the fundamental decomposition, the gauge metric and the classical–quantum sign reading |
| *The States the Indefinite Metric Cannot Normalise* | the pure states as null for $K$, the three nullities, the state cone against the gauge null cone, the order-three projections |
| *Why the Fourth Product Is a Gauge Structure and Not a State Space* | the ternary product and its parity, the failure of the Jordan triple identity, the no-go, the transformation reading and this ledger |

The block's readings, each labelled: the fourth product is the **gauge** corner of the four products; its metric is the indefinite invariant pairing, read on matter as the Minkowski metric with the time direction positive; the states are **null** for that metric and normalisable for the probability form; the sign of the metric is offered as a **classical–quantum** split; and the product is a structure of **transformations**, not of states. The block's negations: no unit, no associativity, no Jordan identity, no cone, no state space from the fourth product. The division of labour with the sesquilinear block — states there, transformations here — is the block's conclusion and is consistent with the assignment of the four products to composition, causality, probability and gauge in *The Four Products and Their Physical Readings: the Two Algebras and the Two Sesquialgebras*.

## The Limits

- The article does not claim that the fourth product is a gauge theory; it claims that the fourth product is a structure of transformations with an indefinite invariant metric and no positivity, and it names that structure a gauge structure by analogy with the standard division between transformations and states.
- The failure of the Jordan triple identity is a negative result: it removes a candidate, and it does not by itself supply a physical interpretation. The gauge reading is a reading of what remains.
- The ternary product, the parity theorem and the witness are the mathematics' (*The Ternary Product and the Failure of the Jordan Triple Identity*, *The Sesquilinear Associator and the Ternary Product*), cited here and not re-proved.
- No claim is made about the state space beyond the assignment of the states to the sesquilinear product, and none about a bracket of an internal gauge algebra being the physical one.

## The Ledger

**Proved, and recomputed.** The fourth product has no unit on either side ($e_0\star\tilde Q=\tilde Q^{*}$, $\tilde Q\star e_0=\tilde Q^{\natural}$) and is not associative. Its ternary product $\{\tilde P,\tilde Q,\tilde R\}=\overline{\tilde Q}\tilde P\tilde R$ has the parity of a Jordan triple, linear in the outer slots and conjugate-linear in the middle, and is the left model $\tilde X^{*}\tilde Y\tilde Z$. The Jordan triple identity **fails** at $(e_0,e_1,e_0,e_2,e_0)$, where the two sides are $e_3$ and $-3e_3$; $480$ of the $1024$ basis five-tuples fail; the failure survives on the real subspaces and appears in the operators as the failure of the commutator identity, the operators at $\tilde X=\tilde U=e_0$, $\tilde Y=e_1$, $\tilde V=e_2$ being the left multiplications by $2e_3$ and $-2e_3$. The sandwich $L_{\tilde A}\circ L_{\tilde B}(\tilde X)=\tilde A^{\natural}\tilde X\overline{\tilde B}$ is the composition of two one-sided actions. Recomputed in a companion note and reproduced from *The Ternary Product and the Failure of the Jordan Triple Identity*, *The Sesquilinear Associator and the Ternary Product*, *Algebraic J\*-Algebras* and *Jordan Triples with an Involution*.

**Standard.** That a JB\*-triple carries a state space, and that the Jordan triple identity is the axiom whose failure blocks the reconstruction of a cone, an order and a transition probability.

**Reading, labelled.** That the fourth product is the **gauge structure** of the frame and the sesquilinear product the **state space**, the two not unifiable into one algebraic triple because the identity that would unify them is false.

**Not claimed.** That the fourth product is a gauge theory; that a bracket of the algebra is a physical gauge algebra; that the failure has a physical consequence beyond the removal of a candidate state space.

**Open.** What an actual action of the sandwich transformations on the positive cone would be; whether the order-three projections of the fourth product have physical content; whether the sign split, the sector split and the centre-as-classical reading are one structure or three.

## Summary

The fourth product has no unit and is not associative, so its natural replacement is the ternary product $\{\tilde P,\tilde Q,\tilde R\}=\overline{\tilde Q}\tilde P\tilde R$, which has the parity of a Jordan triple — linear in the outer slots, conjugate-linear in the middle — and is the left model $\tilde X^{*}\tilde Y\tilde Z$ of the algebra's ternary products. The Jordan triple identity, the axiom through which a JB\*-triple reconstructs a state space, nevertheless **fails**: at the basis elements $(e_0,e_1,e_0,e_2,e_0)$ the left-hand side is $e_3$ and the right-hand side is $-3e_3$, $480$ of the $1024$ basis five-tuples are witnesses, the failure survives restriction to the real quaternion subalgebra, and it appears in the operators as the failure of the commutator identity by which the operators of the ternary product would generate a Lie algebra of derivations. The consequence is a no-go statement: no Jordan structure, no cone, no pure states and no transition probabilities can be reconstructed from the fourth product, and the state space of the framework remains the positive cone carried by the sesquilinear product with its Born pairing $H$. What the fourth product does supply is the **transformation side** of the algebra: the composition of the one-sided actions as the sandwich $\tilde A^{\natural}\tilde X\overline{\tilde B}$, the invariant indefinite metric $K$ with its isometry group $U(1,3)$, and a bracket with no cone. The reading — the fourth product as the **gauge structure**, the sesquilinear product as the **state space**, the two not unifiable because the identity that would unify them is false — is proposed and labelled, and it closes the block, whose other two articles are *The Fourth Product and Its Indefinite Metric* and *The States the Indefinite Metric Cannot Normalise*. The ternary product, the parity and the failure are *The Ternary Product and the Failure of the Jordan Triple Identity*, *The Sesquilinear Associator and the Ternary Product*, *Algebraic J\*-Algebras* and *Jordan Triples with an Involution*; the positive cone is *Mass, Rank and the Positivity of the Dagger*; and the map of the four products is *The Four Products and Their Physical Readings: the Two Algebras and the Two Sesquialgebras*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q^{*}$ | the fourth product; no unit, not associative |
| $\{\tilde P,\tilde Q,\tilde R\}=(\tilde P\star\tilde Q)\star\tilde R^{*}=\overline{\tilde Q}\tilde P\tilde R$ | the ternary product of the fourth product |
| $\tilde X^{*}\tilde Y\tilde Z$ | the left model; the fourth product's ternary product |
| $\tilde X\tilde Y^{*}\tilde Z$ | the middle model; the sesquilinear product's ternary product |
| $\Theta_{\tilde X,\tilde Y}(\tilde R)=\{\tilde X,\tilde Y,\tilde R\}$ | the operator of a pair; the plain left multiplication by $\overline{\tilde Y}\tilde X$ |
| $(e_0,e_1,e_0,e_2,e_0)$ | the witness: left side $e_3$, right side $-3e_3$ |
| $480/1024$ | the fraction of basis five-tuples failing the identity |
| $L_{\tilde A}\circ L_{\tilde B}(\tilde X)=\tilde A^{\natural}\tilde X\overline{\tilde B}$ | the sandwich; the composition of two one-sided actions |
| $K(\tilde P,\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ | the gauge metric; indefinite, inertia $(1,3)$ |
| $H(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q^{*})$ | the probability form; the Born pairing; positive definite |
| $\mathbb{M}_+,\mathbb{M}_-$ | the informational and material sectors |

## Further Reading

- Mathematics article *The Ternary Product and the Failure of the Jordan Triple Identity* (`articles_maths/the-ternary-product-and-the-failure-of-the-jordan-triple-identity.md`), for the ternary product, its parity, the left model, the witness and the operator form of the failure.
- Mathematics article *The Sesquilinear Associator and the Ternary Product* (`articles_maths/the-sesquilinear-associator-and-the-ternary-product.md`), for the general ternary product and the parity theorem.
- Mathematics articles *Algebraic J\*-Algebras* (`articles_maths/algebraic-j-star-algebras.md`) and *Jordan Triples with an Involution* (`articles_maths/jordan-triples-with-an-involution.md`), for the two models, the identity, the reconstruction of the state space and the theorem that the identity belongs to the middle model.
- Mathematics article *The Ternary Product as an Operator* (`articles_maths/the-ternary-product-as-an-operator.md`), for the commutator identity and the Lie triple system.
- Mathematics article *Biquaternions as a Quaternionic Sesquialgebra over $\mathbb{C}$* (`articles_maths/biquaternions-as-a-quaternionic-sesquialgebra-over-c.md`), for the product, its failure to be the derived operation and its ternary reading.
- Companion article *The Fourth Product and Its Indefinite Metric*, for the metric the block installs and the division of labour it implies.
- Companion article *The States the Indefinite Metric Cannot Normalise*, for the states on the gauge-metric null cone.
- Companion article *Mass, Rank and the Positivity of the Dagger*, for the positive cone and the no-ghost statement — the state side of the division of labour.
- Companion article *Observables, Gauge Generators and the Chirality of the Internal Action*, for the one-sidedness of the internal action on which the transformation reading rests.
- Companion article *The Four Products and Their Physical Readings: the Two Algebras and the Two Sesquialgebras*, for the map of the four products and the assignment of the fourth to gauge.
