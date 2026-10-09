# __Interference without a Lie Algebra: the Jacobi Failure in the State Space__

## Introduction

The plain sesquilinear amplitude splits into a central half and a vector half, and the companion article of this band read the vector half as the **phase** of the pairing. There is an algebraic price for a phase that is carried by a vector and not by a central number, and this article states it: the antisymmetric plain sesqualgebra **fails the Jacobi identity**, so the phase structure of the framework carries **no symmetry algebra**.

The failure is exact and small enough to see at a glance. For the antisymmetric plain sesqualgebra $\tilde P\wedge_{*}\tilde Q=\mathrm{Vect}(\tilde P\tilde Q^{*})$, the cyclic sum of the block at the triple $(e_0,e_1,e_2)$ — the outer form $\mathrm{cyc}\,\wedge_{*}$ defined below — is

$$
\mathrm{cyc}\,\wedge_{*}(e_0,e_1,e_2)=e_3\neq0,
$$

so the operation is not a Lie bracket and there is no Lie algebra of generators attached to it. The contrast is with the antisymmetric **plain** product, whose antisymmetrisation is the cross product, alternates, satisfies the Jacobi identity and closes as the algebra of the rotations; the contrast with that closing bracket is the whole reading of this article. The operation still has a **sesquilinear pairing** — the Hermitian form read on its values — and the article states it, because the pairing is what survives where the algebra does not. The bound of the band stands: the phase is **read from** a value, and a failure of an identity is a negative result about the algebra and supplies no dynamics.

**Boundaries.** The Jacobi failure, the witness and the quadric of the diagonal are *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*; the pairing and the invariant forms are *The Sesquilinear Pairing of the Antisymmetric Plain Sesqualgebra*; the general Lie structures of a sesqualgebra, including the failure of the Jacobi identity of an antisymmetrised sesquilinear product and the Lie structure that actually exists, are *Lie Algebras of Sesqualgebras* and *The Sesquilinear Commutator*. The closing bracket is *The Cross Product as a Lie Bracket: Rotations and the Jacobi Identity*, *The Lie Algebra of the Antisymmetric Plain Algebra* and *Angular Momentum and the Lie Algebra of the Material Sector*; the physical angular momentum is *Angular Momentum and Spin in Biquaternionic Form*. The other antisymmetrised sesquilinear-type product and its failure are *The Brackets That Do Not Close: the Jacobi Failure of the Quaternionic Commutator* and *Boosts, Mixed Terms and the Missing Lie Structure*; the state side is *Mass, Rank and the Positivity of the Dagger*. The companion of this band is *The Imaginary Part of the Born Pairing: the Antisymmetric Sesquilinear Product*.

**Conventions.** As in the companion articles and in *Conventions in the Biquaternion Universe*: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$, $e_k^{2}=-e_0$, $e_1e_2=e_3$; $\tilde Q=Q_0e_0+\mathbf Q$, $Q_\mu\in\mathbb{C}$; ${}^{\natural}$ the natural conjugation, $\overline{\cdot}$ the coefficientwise one, ${}^{*}=\overline{\cdot}\circ{}^{\natural}$; $\mathrm{Sc}$ and $\mathrm{Vect}$ the scalar and vector parts, $\mathrm{Tr}=2\,\mathrm{Sc}$; the Hermitian form $H(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q^{*})=\sum_\mu P_\mu\overline{Q_\mu}$; the operations $\tilde P\circledast\tilde Q=H(\tilde P,\tilde Q)e_0$ (symmetric) and $\tilde P\wedge_{*}\tilde Q=\mathrm{Vect}(\tilde P\tilde Q^{*})$ (antisymmetric). The bilinear dot and cross products of vector parts are $(\mathbf P,\mathbf Q)$ and $\mathbf P\times\mathbf Q$, and the sesquilinear triple bracket is $[\mathbf P,\mathbf Q,\mathbf R]=(\mathbf P\times\mathbf Q,\mathbf R)$. The antisymmetric plain product of the algebra row is written $\tilde P\wedge\tilde Q=\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)=\mathbf P\times\mathbf Q$, the quaternionic antisymmetric product $\tilde P\wedge_{Q}\tilde Q$. The sectors are $\mathbb{M}_{\pm}$ and the state side is $\mathbb{M}_{+}$.

## The Jacobi Identity and Its Failure

### The Identity to be Tested

The antisymmetric half of a bilinear product is a Lie bracket exactly when it is alternating and satisfies the Jacobi identity, and the antisymmetric plain product of the algebra row is the model: it is the cross product of the vector parts,

$$
\tilde P\wedge\tilde Q=\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)=\mathbf P\times\mathbf Q,
$$

which alternates and closes, so its values exponentiate to the rotations. The same test asked of the antisymmetric **sesquilinear** half of the plain product gives the negative answer of this article.

### The Witness

**The operation fails the Jacobi identity.** For an operation $b$ additive in each variable, the **cyclic sum** at a triple is the outer form

$$
\mathrm{cyc}\,b(\tilde X,\tilde Y,\tilde Z)=b\bigl(b(\tilde X,\tilde Y),\tilde Z\bigr)+b\bigl(b(\tilde Y,\tilde Z),\tilde X\bigr)+b\bigl(b(\tilde Z,\tilde X),\tilde Y\bigr),
$$

which vanishes for all triples exactly when $b$ satisfies the Jacobi identity (*The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*). At the real triple $(e_0,e_1,e_2)$ the cyclic sum of the block does not vanish. The basis table of the operation reads

$$
e_0\wedge_{*} e_1=-e_1,\qquad e_1\wedge_{*} e_2=-e_3,\qquad e_2\wedge_{*} e_0=e_2,\qquad e_2\wedge_{*} e_1=e_3,
$$

so the three terms are

$$
\wedge_{*}(e_0\wedge_{*} e_1,e_2)=\wedge_{*}(-e_1,e_2)=e_3,
$$

$$
\wedge_{*}(e_1\wedge_{*} e_2,e_0)=\wedge_{*}(-e_3,e_0)=-e_3,
$$

$$
\wedge_{*}(e_2\wedge_{*} e_0,e_1)=\wedge_{*}(e_2,e_1)=e_3,
$$

and the sum is

$$
\mathrm{cyc}\,\wedge_{*}(e_0,e_1,e_2)=e_3\neq0 .
$$

That is the menued witness: the **cyclic sum $e_3$** at $(e_0,e_1,e_2)$.

**Remark (the second, conjugated witness).** The failure has a second face that the real basis does not see. At the triple $(e_1,e_1,ie_2)$, which needs the non-real coefficient $i$ in the third slot, the cyclic sum is $-2ie_2$; the real triple exhibits one failure and the conjugated triple the other, and the mathematics records both (*The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*).

**Remark (verified).** With the definition $\tilde P\wedge_{*}\tilde Q=\mathrm{Vect}(\tilde P\tilde Q^{*})$, the outer cyclic sum at $(e_0,e_1,e_2)$ is $e_3$ and at $(e_1,e_1,ie_2)$ is $-2ie_2$; the failure is generic and not a basis accident, the cyclic sum being nonzero on $100$ of $100$ random triples.

### Why It Fails

The failure is structural and it is the same mechanism as the failure of the Jordan identity in the companion band. The operation is conjugate-linear in its **second** slot, and a double bracket therefore reintroduces a conjugation at the wrong place; a commutator of a **bilinear associative** product closes because the associativity rearranges the two products, while an antisymmetrisation of a **genuine sesquilinear** product does not. The mathematics states the criterion exactly — the antisymmetrisation of a derived sesquilinear product is antisymmetric and satisfies the Jacobi identity only in the collapse case where the two involutions are trivial, that is only when the product is bilinear and the sesqualgebra is an algebra (*Lie Algebras of Sesqualgebras*, *The Sesquilinear Commutator*) — and this article reads the consequence: for the plain sesqualgebra the complex conjugation is nontrivial and the identity fails, so this block supplies no bracket.

**Remark (the terminology).** The operation $\tilde P\wedge_{*}\tilde Q$ is the antisymmetric half of the product under the **conjugate** exchange — the interchange of the two arguments twisted by the coefficientwise conjugation — and it is *not* the sesquilinear commutator $[\tilde P,\tilde Q]_{\varsigma}=\tilde P\tilde Q^{*}-\tilde Q\tilde P^{*}$ of *The Sesquilinear Commutator*, which is the antisymmetric half under the bare interchange. The two are the two readings of the antisymmetry of one product, and the mathematics holds the exact relation $[\tilde P,\tilde Q]_{\varsigma}=2\,\tilde P\wedge_{*}\tilde Q+\bigl(\overline{\tilde Q\tilde P^{*}}-\tilde Q\tilde P^{*}\bigr)$, whose defect is the imaginary part of the swapped value and vanishes on the real span, where the commutator is twice the block (*The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*, *The Sesquilinear Commutator*). The failure of the Jacobi identity is a property of this half, and this article does not attribute it to the commutator — nor does it read the commutator's failure, whose witness is a triple of matrix units in the two-by-two model and not a triple of this basis.

## The Absence of a Symmetry Algebra

### No Lie Algebra of the Phase

A bracket that fails the Jacobi identity is not a Lie bracket, and the operation is therefore **not the Lie algebra of any group**. There is no adjoint representation, no exponential of an adjoint action, and no conserved bilinear Killing form read from the operation; the whole layer that a Lie algebra supports is unavailable. The reading is the one the band's title records: **the phase structure of the framework carries no symmetry algebra**. An interference term is assembled from two amplitudes; it is a relational datum and not an infinitesimal transformation, and the operation that assembles it generates nothing.

### The Contrast with the Closing Bracket

The contrast is with the antisymmetric plain product, and it is sharp because the two operations are built by the same recipe from the two sides of the four-product grid.

| feature | antisymmetric plain product $\wedge$ | antisymmetric plain sesquilinear product $\wedge_{*}$ |
|---|---|---|
| value | $\mathbf P\times\mathbf Q$, vector subspace | $\mathrm{Vect}(\tilde P\tilde Q^{*})$, vector subspace |
| diagonal | alternating, $\tilde P\wedge\tilde P=0$ | not zero, $\tilde P\wedge_{*}\tilde P=\mathrm{Vect}(\tilde P\tilde P^{*})$ |
| law | antisymmetric, $\tilde P\wedge\tilde Q=-\tilde Q\wedge\tilde P$ | conjugate-alternating, $-\overline{\tilde Q\wedge_{*}\tilde P}$ |
| Jacobi identity | holds | fails, witness $(e_0,e_1,e_2)$, cyclic sum $e_3$ |
| reading | the algebra of rotations, $SO(3)$ | no symmetry algebra |

The closing bracket is read as the generators of the rotations and as the local algebra of the material sector (*The Cross Product as a Lie Bracket: Rotations and the Jacobi Identity*, *Angular Momentum and the Lie Algebra of the Material Sector*, *The Lie Algebra of the Antisymmetric Plain Algebra*), and the physical angular momentum of the corpus is raised from it (*Angular Momentum and Spin in Biquaternionic Form*). The failing bracket raises nothing of the kind, and the two rows of the table are the exact statement that the symmetry layer belongs to the antisymmetric **plain** product — the cross product — and not to the sesquilinear antisymmetrisations.

**Remark (the neighbours that also fail).** The block is not alone in failing. The antisymmetric quaternionic product fails the Jacobi identity at the same triple with the cyclic sum $-e_3$, read as the associator defect of the quaternionic product (*The Brackets That Do Not Close: the Jacobi Failure of the Quaternionic Commutator*, *Boosts, Mixed Terms and the Missing Lie Structure*); the two failures are different in cause — an associator defect there, a twist defect here — and the mathematics separates them (*The Jacobi Failure and the Associator Defect of the Antisymmetric Quaternionic Algebra*). The reading of the whole grid is that the antisymmetric **plain** product alone closes, while the quaternionic antisymmetrisation and the two sesquilinear ones fail, so the state row of the framework is a row of pairings and not a row of generators.

## The Sesquilinear Pairing of the Bracket

### The Pairing

A bracket that closes carries an invariant bilinear form, the Killing form; the failing bracket carries instead the **Hermitian form read on its values**, because the form is defined on the whole algebra and the operation is algebra-valued. For all biquaternions,

$$
H\bigl(\tilde P\wedge_{*}\tilde Q,\tilde R\bigr)
=-P_0\bigl(\overline{\mathbf Q},\overline{\mathbf R}\bigr)
+\overline{Q_0}\,\bigl(\mathbf P,\overline{\mathbf R}\bigr)
-\bigl[\mathbf P,\overline{\mathbf Q},\overline{\mathbf R}\bigr],
\qquad
[\mathbf P,\mathbf Q,\mathbf R]=(\mathbf P\times\mathbf Q,\mathbf R),
$$

the **sesquilinear pairing of the bracket** (*The Sesquilinear Pairing of the Antisymmetric Plain Sesqualgebra*).

### Its Class

The pairing is **$\mathbb{C}$-linear in the first argument and conjugate-linear in the second and in the third**: the operation is conjugate-linear in its second slot, the form is conjugate-linear in its second slot, and the two conjugations stack without cancelling, which is exactly the algebraic reason the Jacobi identity failed on the same product. A tri-linear object of this class is a **relative** pairing of three amplitudes and not a bracket of an algebra. It is also worth recording the contrast in the second-slot behaviour with the pairing of the closing bracket: a Killing form is symmetric and bilinear, and this pairing is neither.

### Where the Positivity Goes

The form $H$ is positive definite on the algebra, so on the values of the operation it is positive definite as well: $H(\tilde P\wedge_{*}\tilde Q,\tilde P\wedge_{*}\tilde Q)\ge0$, with equality exactly when the value vanishes. Positivity therefore does not fail the block; the order does. The point of the pairing section is that the **form survives where the algebra does not**: the operation has no generators and no Killing form, and it still has the definite form, read on its values, which is what makes the interference term a positive-length vector of the informational sector and not a symmetry generator.

**Remark (the invariant forms are one-dimensional).** A form $\beta$ is invariant under the block in the sense $\beta(\tilde P\wedge_{*}\tilde Q,\tilde R)=-\overline{\beta(\tilde P,\tilde Q\wedge_{*}\tilde R)}$, and the space of such $\beta$ is **one-complex-dimensional**, spanned by the form that reads the scalar slot; so the invariance of $H$ itself — its invariance under the inner action that the algebra rows carry — does not descend to the block. This is the mathematics' statement (*The Sesquilinear Pairing of the Antisymmetric Plain Sesqualgebra*, *Lie Algebras of Sesqualgebras*), cited here and not re-proved. The reading is again negative and exact: the failing block is not the home of an invariant form of a symmetry algebra, only of the definite form of the vector space it lives in.

**Remark (verified).** The identity with the triple bracket holds on $100$ random triples to $<10^{-13}$; the quadratic form of the pairing is strictly positive on every nonzero value tested.

**Remark (the pairing as a tensor).** The three arguments enter with the parities $\mathbb{C}$-linear, conjugate-linear, conjugate-linear, so the pairing is a tensor of the class $(\mathbb{C},\bar{\cdot},\bar{\cdot}\,)$ and not an invariant of a bracket; the maths article states the invariance that remains and its one-dimensionality (*The Sesquilinear Pairing of the Antisymmetric Plain Sesqualgebra*).

**Reading (a three-amplitude invariant).** The pairing takes **three** amplitudes and returns a number; it is a relative invariant of the three, never of one. Read physically it is the algebraic form of a **three-point correlation of phases**: the object an interference term of three amplitudes would be assembled from, conjugate-linear in the last two entries because the phases being correlated are relative. As with the binary term, no process and no measure is derived; what the algebra supplies is the invariant, and the corpus's phase articles supply the processes that use it.

**Where the positivity survives.** Positivity is the one thing the failing block keeps. The form $H$ is definite on the whole algebra, so on the values of the bracket it is definite too, and this is the exact sense in which **the form survives where the algebra does not**: the operation that raises no generators still carries a positive-definite length, and an interference vector therefore has a length even though it names no symmetry.

## Interference without a Lie Algebra

### The Reading

Collecting the two bands: the plain sesquilinear amplitude splits into a central probability and a vector phase; the phase half is conjugate-alternating, has a non-vanishing diagonal and fails the Jacobi identity; it therefore carries a **pairing** and no **algebra**. Physically, the phase half of the corpus's amplitudes is the **interference term** (*The Double-Slit Experiment in Biquaternionic Form*, the companion article *The Imaginary Part of the Born Pairing: the Antisymmetric Sesquilinear Product*): an interference term is assembled from two amplitudes, it is a relational datum and not a state, and it makes no sense to ask for its generators. The framework here agrees with the physical situation rather than departing from it: interference is a **relational** datum of two amplitudes and not an infinitesimal symmetry. What the algebra adds is the exact statement that the relational datum is the vector half of the pairing and that the operation producing it is not a Lie algebra.

### The Contrast with the Observable Side

The same contrast, seen from the state side. The state side $\mathbb{M}_{+}$ carries the observables, and the two operations of its row are the symmetric half (which fails the Jordan identity, so it is not a Jordan algebra; the companion band) and the antisymmetric half (which fails the Jacobi identity, so it is not a Lie algebra; this article). The symmetry generators of the framework live on the **material** side and on the **bilinear** products, where the brackets close, and the **angular momentum** of the corpus is raised there and not here. The state row therefore supplies probabilities and phases and **no generators**, which is the negative statement that the two bands of the pair have been building to. It is the natural counterpart, on the state side, of the statement that the state row of the framework is a row of pairings and not a row of transformations.

**Remark (the caution).** A failure of the Jacobi identity is a **negative result**: it says the operation is not a Lie algebra, and it does not say that the phase is unphysical, that interference is unreal, or that no group acts on the state space. The physical phases of the corpus remain what the phase articles make them (*The Path Integral in Biquaternionic Form*, *Geometric Phases of Non-Relativistic Spin in Biquaternionic Form*, *The Berry Phase and Geometric Phases in Biquaternionic Form*, *Pancharatnam's Phase and the Polarization Sphere in Biquaternionic Form*), and the groups that act on the state space are the internal action and the compact slice (*Observables, Gauge Generators and the Chirality of the Internal Action*, *Particle Types, Discrete Charge and Three-Particle Couplings*), neither of which is raised from this operation. The failure is an obstruction of one construction and not a statement about the world.

## Ledger

**What the operation does.**
- Supplies the vector half of the sesquilinear amplitude, the phase and interference half of the pairing.
- Carries the sesquilinear pairing $H(\tilde P\wedge_{*}\tilde Q,\tilde R)$, conjugate-linear in the last two slots, a relative invariant of three amplitudes.
- Has positive-definite length on its values, since $H$ is definite on the algebra: the form survives where the algebra does not.

**What the operation does not do.**
- It is not a Lie bracket: the Jacobi identity fails at $(e_0,e_1,e_2)$ with the cyclic sum $e_3$.
- It raises no symmetry algebra: no adjoint action, no exponential, no invariant Killing form.
- Its invariant pairings are one-dimensional and do not include the invariance of $H$.
- It is a pairing and not a generator, and it measures no phase.
- It raises **no group** either: the groups that act on the state space are the internal action and the compact slice, both external to this operation.

## Summary

The antisymmetric plain sesqualgebra **fails the Jacobi identity**: at the witness $(\tilde P,\tilde Q,\tilde R)=(e_0,e_1,e_2)$ the cyclic sum of the outer form is **$e_3$**, at the conjugated witness $(e_1,e_1,ie_2)$ it is $-2ie_2$, and the failure is generic (nonzero on $100$ of $100$ random triples). The reason is structural: the operation is conjugate-linear in its second slot, so a double bracket reintroduces the conjugation at the wrong place, and the antisymmetrised sesquilinear product is a Lie bracket only in the collapse case where the two involutions are trivial, that is only for a bilinear product. The operation is therefore **not the Lie algebra of any group** and raises no symmetry algebra, in exact contrast with the antisymmetric **plain** product $\tilde P\wedge\tilde Q=\mathbf P\times\mathbf Q$, which alternates, closes and gives the algebra of the rotations and the physical angular momentum. What survives is the **sesquilinear pairing** of the bracket, $H(\tilde P\wedge_{*}\tilde Q,\tilde R)=-P_0(\overline{\mathbf Q},\overline{\mathbf R})+\overline{Q_0}(\mathbf P,\overline{\mathbf R})-[\mathbf P,\overline{\mathbf Q},\overline{\mathbf R}]$, $\mathbb{C}$-linear in the first argument and conjugate-linear in the second and third, a **relative invariant of three amplitudes** that reads as a three-point correlation of phases, whose invariant forms are one-complex-dimensional and do not include the invariance of $H$; positivity does not fail, only the algebra does, so the form survives where the algebra does not. The reading is that the phase structure of the framework carries a **pairing and no symmetry algebra**, which is the algebraic form of the physical fact that an interference term is a relational datum of two amplitudes and not an infinitesimal transformation; the state row supplies probabilities and phases and no generators, the groups acting on the state space being external to this operation, and the caution is that a failure of an identity is an obstruction of a construction and not a statement about the world.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\wedge_{*}\tilde Q=\mathrm{Vect}(\tilde P\tilde Q^{*})$ | the antisymmetric plain sesqualgebra; not a Lie bracket |
| $\mathrm{cyc}\,\wedge_{*}(e_0,e_1,e_2)=e_3$ | the failing cyclic sum |
| $\mathrm{cyc}\,\wedge_{*}(e_1,e_1,ie_2)=-2ie_2$ | the conjugated witness |
| $(\tilde P,\tilde Q,\tilde R)=(e_0,e_1,e_2)$ | the witness of the Jacobi failure |
| $\tilde P\wedge\tilde Q=\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)=\mathbf P\times\mathbf Q$ | the closing bracket; alternates, Jacobi holds, gives $SO(3)$ |
| $H(\tilde P\wedge_{*}\tilde Q,\tilde R)$ | the sesquilinear pairing of the bracket; a relative invariant of three amplitudes |
| $[\,\mathbf P,\mathbf Q,\mathbf R\,]=(\mathbf P\times\mathbf Q,\mathbf R)$ | the sesquilinear triple bracket |
| $H(\tilde P\wedge_{*}\tilde Q,\tilde P\wedge_{*}\tilde Q)\ge0$ | the definite length on the values |
| $\mathbb{M}_{+}$ | the state side; no generators raised from the pair |

## Further Reading

- *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra* (`articles_maths/the-vector-part-of-the-square-and-the-jacobi-failure-of-the-antisymmetric-plain-sesqualgebra.md`), which owns the failure and the witness.
- *The Sesquilinear Pairing of the Antisymmetric Plain Sesqualgebra* (`articles_maths/the-sesquilinear-pairing-of-the-antisymmetric-plain-sesqualgebra.md`), which owns the pairing and the invariant forms.
- *Lie Algebras of Sesqualgebras* (`articles_maths/lie-algebras-of-sesqualgebras.md`), for the general criterion and the Lie structure that actually exists.
- *The Sesquilinear Commutator* (`articles_maths/the-sesquilinear-commutator.md`), for the bracket the operation is not.
- *The Cross Product as a Lie Bracket: Rotations and the Jacobi Identity* (`articles_physics/the-cross-product-as-a-lie-bracket-rotations-and-the-jacobi-identity.md`), the closing bracket.
- *The Lie Algebra of the Antisymmetric Plain Algebra* (`articles_maths/the-lie-algebra-of-the-antisymmetric-plain-algebra.md`), the algebra of the closing bracket.
- *Angular Momentum and Spin in Biquaternionic Form* (`articles_physics/angular-momentum-and-spin-in-biquaternionic-form.md`), the physical angular momentum, raised from the closing bracket.
- *The Brackets That Do Not Close: the Jacobi Failure of the Quaternionic Commutator* (`articles_physics/the-brackets-that-do-not-close-the-jacobi-failure-of-the-quaternionic-commutator.md`), the neighbouring failure.
- *The Imaginary Part of the Born Pairing: the Antisymmetric Sesquilinear Product* (`articles_physics/the-imaginary-part-of-the-born-pairing-the-antisymmetric-sesquilinear-product.md`), the companion article of the band.
