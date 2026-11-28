---
title: The Symmetry Group SU(2)_L × U(1)_Y of the Electroweak Force
---

# __The Symmetry Group SU(2)\_L × U(1)\_Y of the Electroweak Force__

## Introduction

The category *Biquaternion Universe Electroweak Force* is the rung below the strong one: the sector built from the group that survives the restructuring. The question this article answers is: **which group does the category carry?**

$$
\boxed{\ \mathrm{Sym}=\mathrm{SU}(2)_L\times\mathrm{U}(1)_Y,\qquad \dim=3+1=4,\qquad \operatorname{rank}=1+1=2\ }
$$

Three generators of weak isospin and one of hypercharge, and the title names the pair because the Standard Model's electroweak group *is* the pair. The two are not one group and they are not independent: they are the two normalisations of a single compact structure, and the relation between them is the parity lock of §*The Two Factors and the Lock*. The block calls this rung the **weak factors** in the plural for the same reason, and the ladder's arithmetic of §*The Two Factors and the Lock* counts only the simple factor, three, because the abelian one is the index the chain above cannot supply.

**The placement on the ladder.** A force is a gauged generator, and the ladder is nested with counts $0,\,3,\,8,\,15$:
$$
\mathrm{SU}(1)\subset\mathrm{SU}(2)\subset\mathrm{SU}(3)\subset\mathrm{SU}(4).
$$
This rung is the second. It is reached from the third by the removal of the five generators that distinguish a line from the two it leaves, and it is not a piece of the fifteen: the rank cannot fall from three to reach it as debris, nor rise from three to reach its endpoint, so the weak factors arrive as an *index* on the condensate that breaks the rung above. That is the sense in which this rung is real and the sense in which it is not a fragment.

**The honest standing, stated at the outset.** The group and the hypercharge assignment are standard theory. Nothing here is derived from the biquaternion algebra, and the block says so in the sharpest form the corpus allows. What the category supplies is the placement of the group on the ladder, the algebra's own compact normalisation $\mathrm{U}(2)$ and the lock that relates the two factors, and the computation of the mixed group in the corpus's notation. The assignment of hypercharges is imported, and §*What the Category Does Not Supply* names that as a boundary rather than a derivation.

- Companion article [*The Electroweak Symmetry Group and the Hypercharge Assignment*](the-electroweak-symmetry-group-and-the-hypercharge-assignment.html), for the group, the anomaly system and its three rays.
- Companion article [*The Electroweak Pair in the Biquaternion Framework: The Quotient and the Parity Lock*](the-electroweak-pair-in-the-biquaternion-framework-the-quotient-and-the-parity-lock.html), for $\mathfrak{u}(2)$ against $\mathrm{SU}(2)\times\mathrm{U}(1)$.
- Companion article [*The Weinberg Angle and the Three Neutral States*](the-weinberg-angle-and-the-three-neutral-states.html), for the mixing.
- Companion article [*The Photon as the Unbroken Mixture*](the-photon-as-the-unbroken-mixture.html), for the unbroken $\mathrm{U}(1)_{\mathrm{em}}$.
- Companion article [*Rank Five From Three: The Weak Factors as a Condensate Index*](rank-five-from-three-the-weak-factors-as-a-condensate-index.html), for why the factors are an index and not debris.
- Companion article [*The Fourth Generator: The Abelian Factor on the Ladder*](the-fourth-generator-the-abelian-factor-on-the-ladder.html), for why this category carries four generators where the ladder carries three.
- Companion article [*The Symmetry Group SU(3) of the Strong Force*](the-symmetry-group-su3-of-the-strong-force.html) and [*The Symmetry Group SU(4) of the Primordial Force*](the-symmetry-group-su4-of-the-primordial-force.html), for the rungs above.

## The Four Generators

**Definition (the group of the category).** The category's *group* is the internal group whose generators its connection carries,
$$
\tilde A=\tilde A^{a}T^{a},\qquad a=1,\dots,4,
\qquad
\mathfrak{g}=\mathfrak{su}(2)_L\oplus\mathfrak{u}(1)_Y ,
$$
with $T^{1},T^{2},T^{3}$ the weak isospin generators and $Y$ the hypercharge. The *count* is $\dim\mathfrak{g}=3+1=4$.

**Proposition (the count is four, and it is three plus one).** The group has three non-abelian generators forming an $\mathfrak{su}(2)$ and one abelian generator.

*Proof.* $\dim\mathfrak{su}(2)=2^{2}-1=3$ and $\dim\mathfrak{u}(1)=1$, and the algebra is their direct sum, so the count is four and the rank is $1+1=2$. The three close under the commutator, $[T^{a},T^{b}]=i\epsilon^{abc}T^{c}$, and $Y$ commutes with all of them because it generates the abelian factor. Verified by the dimension formula and by the commutator of the two algebras.

**Proposition (the rank, and why the endpoint needs five).** The rank of this rung is two, and the endpoint of the breaking needs rank five.

*Proof.* $\operatorname{rank}\mathfrak{su}(2)+\operatorname{rank}\mathfrak{u}(1)=1+1=2$, and the endpoint algebra is $\mathfrak{su}(3)\oplus\mathfrak{u}(1)_{B-L}\oplus\mathfrak{su}(2)_L\oplus\mathfrak{u}(1)_Y$ of rank $2+1+1+1=5$. Since the rank of a subalgebra never exceeds that of the algebra and $\operatorname{rank}\mathfrak{su}(4)=3$, no chain of breakings reaches five from three; the two units of rank that this rung contributes are part of the five that cannot be produced by breaking, which is why the factors arrive as an index. Verified by the rank lemma applied to $\mathfrak{su}(4)$ and to the endpoint.

## The Two Factors and the Lock

**Proposition (the algebra's own compact group is $\mathrm{U}(2)$, not $\mathrm{SU}(2)\times\mathrm{U}(1)$).** The biquaternion algebra's intrinsic compact group is $\mathrm{U}(2)$, and the electroweak pair is its two normalisations; the relation between them is the kernel of the exponential.

*Proof.* The $*$-unitary elements of $\mathbb{B}$ form $\mathrm{U}(2)$ by the compact-sector computation, and $\mathrm{U}(2)$ is the quotient of $\mathrm{SU}(2)\times\mathrm{U}(1)$ by the diagonal central element that is simultaneously a half-turn on the rotor and a full turn on the phase. The identification is exactly the relation between the two labels, and it is what the corpus calls the **parity lock**: the label $q$ of a field is congruent to twice its spin, $q\equiv2j\pmod 2$. Verified by intersecting the two normalisations and computing the kernel of the exponential on each factor.

**Remark (what the lock is and is not).** The lock is a relation between two labels and not a claim that the two factors are one group. The group of the category is the pair; the compact group of the algebra is $\mathrm{U}(2)$; and the passage between them is the identification of a central element. A reader who treats the lock as an equality of groups will misread every charge in the block.

**Remark (why the ladder counts three where the group has four).** The chain $\mathrm{SU}(1)\subset\mathrm{SU}(2)\subset\mathrm{SU}(3)\subset\mathrm{SU}(4)$ is a chain of simple groups, and its increments $3,5,7$ sum to the fifteen of the top rung. The electroweak group has four generators because it carries, besides the $\mathrm{SU}(2)$ rung, one abelian factor; that factor is not in the chain and is not a fragment of the rung above, since the rank obstruction forbids it. So the arithmetic of the ladder and the count of the group differ by exactly the index, and the difference is a statement and not a slip: three is the rung, four is the category, and one abelian direction is what the breaking hands over beside the chain.

## What the Group Acts On

**The doublet and the hypercharge.** The left-handed fields sit in $\mathrm{SU}(2)_L$ doublets and the right-handed in singlets; the hypercharge $Y$ is the abelian label, and the electric charge is the mixture $Q=Y+T_3$.

**Proposition (the photon is the unbroken mixture).** The mixing angle is fixed by the single condition $g\sin\theta_W=g_{\mathrm Y}\cos\theta_W$, and the unbroken direction is the electric charge.

*Proof.* Before mixing the two neutral currents are $J^{3}$ and $J^{Y}$; the rotation by $\theta_W$ that makes one combination couple to a massless field is the one satisfying $g\sin\theta_W=g_{\mathrm Y}\cos\theta_W$, and the orthogonal combination is the $Z$. The unbroken generator is $Q=Y+T_3$, and the field that carries it is the photon. Verified by diagonalising the neutral mass matrix and checking that one eigenvalue vanishes exactly at the stated angle.

**Proposition (the three neutral states have three denominators).** The three neutral states of the weak spectrum are not degenerate, and their couplings differ by the three denominators that the two factors and their mixture supply.

*Proof.* The currents are normalised on the two factors separately and on the mixture, and the three normalisations are the three denominators of the block's statement; the condition above fixes which mixture is massless and the other two inherit their denominators from their factors. Verified on the three neutral states by computing each coupling in the two-factor basis.

## What the Category Does Not Supply

**Supplied.** The group and its count, the pair as the two normalisations of the algebra's $\mathrm{U}(2)$, the parity lock relating them, the rank arithmetic that places the rung on the ladder, the mixing condition and the unbroken electric charge, and the three neutral states.

**Not supplied.** Five boundaries, stated as boundaries.

- *The hypercharge assignment.* Four anomaly conditions constrain five numbers and leave exactly three rays; one ray is the observed assignment and one is excluded, and the discrete choice among them is made by the measured electric charges. The assignment is a choice of which circle inside the compact group carries which charge, and it is imported. The framework does not derive it, and the block says so.
- *A value for the mixing angle.* No $\sin^{2}\theta_W$ is computed from the group; the angle is fixed by the measured couplings. The article fixes the relation and not the number.
- *Chirality where the symmetry acts.* This is the rung where the wall is sharpest: the group is chiral as a Standard Model statement, but the algebra's own left action is vector-like by construction and cannot give the two chiral letters independent charges. The one-sided chiral action remains the open problem and is not solved by this rung.
- *The weak factors as debris.* They are an index on the condensate and not fragments of the fifteen; a reader who looks for them inside $\mathfrak{su}(4)$ will not find them, because the rank forbids it.
- *A different arena.* The kinematic group is the same at every rung; this category supplies the electroweak rung and not a new spacetime.

## Summary

The category carries the electroweak pair, $\mathrm{SU}(2)_L\times\mathrm{U}(1)_Y$.

$$
\boxed{\ \mathrm{Sym}=\mathrm{SU}(2)_L\times\mathrm{U}(1)_Y,\quad \dim=3+1=4,\quad \operatorname{rank}=1+1=2,\quad Q=Y+T_3\ }
$$

The three non-abelian generators are the weak isospin and the one abelian generator is the hypercharge; the algebra is their direct sum and its rank is two. The algebra's own compact group is $\mathrm{U}(2)$, and the two factors are its two normalisations, related by the parity lock $q\equiv2j\pmod 2$, which is the kernel of the exponential and not an equality of groups. The mixing angle is fixed by $g\sin\theta_W=g_{\mathrm Y}\cos\theta_W$ and the unbroken direction is the electric charge. The rung is real and not a fragment: the rank cannot reach the endpoint's five from the primordial three, so the abelian factor arrives as an index on the condensate that breaks the rung above, and the ladder's arithmetic counts the simple three while the group counts four. What the category imports — the hypercharge assignment, the value of the mixing angle, the chiral action at the wall — is stated as imported, and the group and its count are what it supplies.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{SU}(2)_L\times\mathrm{U}(1)_Y$ | The category's group; dimension $4$, rank $2$ |
| $T^{1},T^{2},T^{3}$; $Y$ | Weak isospin generators; hypercharge |
| $\mathfrak{su}(2)\oplus\mathfrak{u}(1)$ | The algebra; the direct sum of the two factors |
| $\mathrm{U}(2)$ | The algebra's own compact group; the two factors are its normalisations |
| $q\equiv2j\pmod 2$ | The parity lock; the kernel of the exponential on the two factors |
| $Q=Y+T_3$ | The electric charge; the unbroken generator |
| $g\sin\theta_W=g_{\mathrm Y}\cos\theta_W$ | The condition fixing the mixing angle |
| $\mathbf{2}$, $\mathbf{1}$ | The left doublet and the right singlet |

## Further Reading

- [*The Electroweak Symmetry Group and the Hypercharge Assignment*](the-electroweak-symmetry-group-and-the-hypercharge-assignment.html), for the group and the three rays.
- [*The Electroweak Pair in the Biquaternion Framework*](the-electroweak-pair-in-the-biquaternion-framework-the-quotient-and-the-parity-lock.html), for the quotient and the lock.
- [*The Weinberg Angle and the Three Neutral States*](the-weinberg-angle-and-the-three-neutral-states.html), for the mixing.
- [*The Photon as the Unbroken Mixture*](the-photon-as-the-unbroken-mixture.html), for $\mathrm{U}(1)_{\mathrm{em}}$.
- [*Rank Five From Three*](rank-five-from-three-the-weak-factors-as-a-condensate-index.html), for the factors as an index.
- [*Chiral Fermions in the Biquaternion Framework*](chiral-fermions-in-the-biquaternion-framework.html), for the chiral wall.
- [*The Symmetry Group SU(3) of the Strong Force*](the-symmetry-group-su3-of-the-strong-force.html), [*The Symmetry Group SU(4) of the Primordial Force*](the-symmetry-group-su4-of-the-primordial-force.html), for the rungs above.
- [*The Symmetry Group SU(1) of the Force-Free Case*](the-symmetry-group-su1-of-the-force-free-case.html), for the bottom of the ladder.
