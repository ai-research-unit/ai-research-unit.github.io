# __The Symmetry Group SU(1) of the Force-Free Case__

## Introduction

The category *Biquaternion Universe Force-Free* is the free layer of the series: the four free Lagrangians, the free Proca, Dirac and Klein–Gordon equations, their polar and momentum-space forms, the free fluid of each spin, and the free operator and free kinematics, with every internal coupling set to zero. The question this article answers is the one the block raises by its silence: **which group does the category carry?**

The answer is the trivial group, and the fact that it is trivial is not a defect but a place on a ladder.

$$
\boxed{\ \mathrm{Sym}=\mathrm{SU}(1)=\{e\}=\{\mathbf{1}\}\ }
$$

The category's force group is the group with **one element and no generator**: $\dim\mathfrak{su}(1)=1^{2}-1=0$.

**Why this is the answer and not an evasion.** The neighbouring categories of the series carry the groups $\mathrm{SU}(4)$ and $\mathrm{SU}(3)$ — fifteen generators at the primordial force, eight at the strong force, the second being a stabiliser inside the first. The ladder is nested,
$$
\mathrm{SU}(1)\subset\mathrm{SU}(2)\subset\mathrm{SU}(3)\subset\mathrm{SU}(4),
\qquad
\dim\mathfrak{su}(n)=n^{2}-1=0,\,3,\,8,\,15 ,
$$
and the free layer is its bottom rung. A force, in this series, is a *gauged generator*: the strong force is eight gauged generators and the primordial force is fifteen. The free layer gauges none — its coupling is zero at every vertex — so the number of generators it gauges is zero, and the group at that rung is $\mathrm{SU}(1)$. The category's group is not introduced from outside the ladder; it is the rung at which the ladder's count reaches zero.

**What went wrong in the first drafts, and why the correction matters.** An earlier version of this article answered with $\mathrm{U}(1)\cdot SL(2,\mathbb{C})$, the group of unit-modulus biquaternions, on the ground that it is the group preserving the algebra's norm. That group is real and it does preserve the norm; but it is the *arena*, and it is identical at every rung of the ladder — at the free layer, at the strong force and at the primordial force alike. A group that is the same in all four categories cannot be the group *of one* of them, and quoting it here is what made the free layer look as though it possessed a symmetry drawn from nowhere. The ladder is indexed by the gauged internal group; the norm's unit group is not indexed by the ladder at all. §*Why the Norm's Unit Group Is Not the Rung* states this precisely.

The rest of the article does four things. It says what the category's group indexes (§*What a Force Group Indexes*). It exhibits the ladder and locates the free layer on it with exact generator counts (§*The Ladder and the Bottom Rung*). It separates the rung from the arena, which is the correction the neighbour's consistency requires (§*Why the Norm's Unit Group Is Not the Rung*). And it states what the trivial rung still asserts, so that "trivial" is not read as "nothing" (§*What the Trivial Rung Still Asserts*).

- Companion article [*The $\mathrm{SU}(4)$ Model: Four Lines, Fifteen Generators, One Declaration*](the-su4-model-four-lines-fifteen-generators-one-declaration.html), for the top rung and its count.
- Companion article [*Quantum Chromodynamics as the Residual of $\mathrm{SU}(4)$: The $\mathrm{SU}(3)$ Wall, Restated*](quantum-chromodynamics-as-the-residual-of-su4.html), for the strong rung as a stabiliser of the rung above it.
- Companion article [*Rank Five From Three: The Weak Factors as a Condensate Index*](rank-five-from-three-the-weak-factors-as-a-condensate-index.html) and [*The Photon as the Unbroken Mixture*](the-photon-as-the-unbroken-mixture.html), for the intermediate rungs.
- Companion article [*The Compact Sector of the Biquaternions Is $\mathfrak{u}(2)$: No $\mathfrak{su}(3)$ Among the Operators*](the-compact-sector-of-the-biquaternions-is-u2.html), for the arena's compact group and the ceiling that keeps the upper rungs outside the algebra.
- Companion article [*The Lorentz Group as Biquaternion Norm Automorphisms*](the-lorentz-group-as-biquaternion-norm-automorphisms.html), for the arena's kinematic group, which is common to all rungs.
- Companion article [*The Minimal Coupling in Biquaternionic Form*](the-minimal-coupling-in-biquaternionic-form.html), for the coupling whose vanishing defines this category.

## What a Force Group Indexes

**Definition (the category's group).** Throughout the series a category's *force group* is the internal group whose generators the category gauges, that is, the group of the connection the category's covariant derivative carries,
$$
\tilde\nabla_{\Phi}\;\longmapsto\;\tilde\nabla_{\Phi}+i\kappa\,\tilde A_{\Phi},
\qquad
\tilde A_{\Phi}=\tilde A_{\Phi}^{a}\,T^{a},
\qquad
[T^{a},T^{b}]=i f^{abc}T^{c},
$$
with $T^{a}$ a basis of the group's Lie algebra and $\kappa$ the coupling. The *count* of the category is the number of these generators that the category gauges, $\dim\mathfrak{g}$.

This is the definition the neighbouring categories use, and it is the only one that puts them on a common scale. The primordial force is fifteen generators because its connection has fifteen components, the strong force is eight because its connection has eight, and the count is what the phrase "the $\mathrm{SU}(4)$ model" and the phrase "the $\mathrm{SU}(3)$ wall" each report. A category is then characterised by its rung, and the rungs are ordered by the count.

**Proposition (the free layer gauges nothing).** The free layer's coupling vanishes at every vertex, so its connection is absent and its count is zero.

*Proof.* The block defines the category by setting every internal coupling to zero, so $\kappa=0$ throughout; at $\kappa=0$ the covariant derivative $\tilde\nabla_{\Phi}+i\kappa\tilde A_{\Phi}$ is the plain gradient, and a connection that appears nowhere in the equations cannot be said to be gauged. The generators $T^{a}$ are then present in no equation of the layer, and the number gauged is zero. Verified by evaluating the covariant derivative at $\kappa=0$ and confirming that no $\tilde A_{\Phi}$ survives in any of the four free equations.

**Corollary (the group at a count of zero is the trivial group).** A group with no generator is the one-element group, $\mathrm{SU}(1)=\{e\}$.

*Proof.* A connected Lie group is generated by the exponentials of its Lie algebra, so a group with $\dim\mathfrak{g}=0$ has $\mathfrak{g}=0$ and is the identity component of itself, a single point. $\mathrm{SU}(1)$ is the group of $1\times1$ unitary matrices of determinant one, which is $\{1\}$; its algebra is the zero space, and $1^{2}-1=0$. Verified by the dimension formula and by the exponential map on the zero algebra.

**Remark (the definition excludes a different question).** A reader may object that the free layer plainly has *some* symmetry — the Lorentz group acts on it, and the algebra's norm is preserved. That is true and it is not denied; it is a statement about the arena, which every category shares, and not about the rung, which is what the ladder indexes. The two questions are separated in §*Why the Norm's Unit Group Is Not the Rung*, and the separation is the whole content of the correction.

## The Ladder and the Bottom Rung

| Rung | Category | Group | Generators | $\dim=n^{2}-1$ |
|---|---|---|---|---|
| 4 | [primordial force](the-symmetry-group-su4-of-the-primordial-force.html) | $\mathrm{SU}(4)$ | $15$ | $16-1$ |
| 3 | [strong force](the-symmetry-group-su3-of-the-strong-force.html) | $\mathrm{SU}(3)=\mathrm{Stab}_{\mathrm{SU}(4)}(e_t)$ | $8$ | $9-1$ |
| 2 | [weak factors](the-symmetry-group-su2l-times-u1y-of-the-electroweak-force.html) | $\mathrm{SU}(2)_L\times\mathrm{U}(1)_Y$ (the simple rung, three, plus one abelian) | $3+1$ | $4$ |
| 1 | Force-Free | $\mathrm{SU}(1)=\{e\}$ | $0$ | $1-1$ |

**The nesting is containment, not analogy.** $\mathrm{SU}(n)\subset\mathrm{SU}(n+1)$ as the maps fixing the last basis vector, and the series uses exactly this relation at the top: the corpus states the strong group as the stabiliser of a line inside the primordial group, $\mathrm{SU}(3)=\mathrm{Stab}_{\mathrm{SU}(4)}(e_t)$, so the descent from fifteen to eight generators is the removal of the seven directions that move that line. The same containment continues one step down, $\mathrm{SU}(1)\subset\mathrm{SU}(2)$, and the free layer is the stabiliser that fixes everything and moves nothing.

**The increments are the rungs.** Between consecutive rungs the count grows by $2n-1$: three generators from $\mathrm{SU}(1)$ to $\mathrm{SU}(2)$, five from $\mathrm{SU}(2)$ to $\mathrm{SU}(3)$, seven from $\mathrm{SU}(3)$ to $\mathrm{SU}(4)$, and $3+5+7=15$. A category that gauges $2n-1$ fewer generators than the one above it is one rung lower, and the free layer is the rung that gauges none.

**The rungs that carry an abelian factor.** The chain is a chain of simple groups — with $\mathrm{SU}(1)=\{e\}$ at the bottom as the trivial minimal element, which is not simple in the strict sense and is there because the chain needs a floor — and its arithmetic sums to the fifteen of the top rung, so the increments count the *simple* generator alone. Two rungs carry an abelian direction beside them, and neither disturbs the count. At the strong rung the kernel is $\mathfrak{u}(3)$ and not $\mathfrak{su}(3)$, the ninth direction being $B-L$; at the electroweak rung the group is $\mathrm{SU}(2)_L\times\mathrm{U}(1)_Y$, four generators, of which three are the rung and one is abelian. The extra direction is not a fragment of the rung above — the rank forbids it — so it arrives beside the chain as an index. Three is the rung; four is the category, and [*The Fourth Generator*](the-fourth-generator-the-abelian-factor-on-the-ladder.html) writes the accounting that reconciles the two without breaking the ladder.

**Proposition (the free layer is the bottom rung and not a rung beside the ladder).** The group of the category is $\mathrm{SU}(1)$, the unique minimal element of the chain, and it is reached from $\mathrm{SU}(2)$ by the same containment that reaches $\mathrm{SU}(2)$ from $\mathrm{SU}(3)$.

*Proof.* The chain $\mathrm{SU}(1)\subset\mathrm{SU}(2)\subset\mathrm{SU}(3)\subset\mathrm{SU}(4)$ is nested and its minimum is $\mathrm{SU}(1)$, since a subgroup of $\mathrm{SU}(1)$ is $\mathrm{SU}(1)$ itself. The free layer gauges no generator by the proposition above, so its group lies at the minimum. The step from $\mathrm{SU}(2)$ to $\mathrm{SU}(1)$ is the vanishing of three generators, which is the same operation as the step from $\mathrm{SU}(3)$ to $\mathrm{SU}(2)$ performed twice more; no new construction is needed and none is introduced. Verified by the dimension count and by the containment of the four groups as matrices.

**Remark (continuity is the requirement, and it is met exactly).** A group "out of nowhere" would be one that does not sit on the chain, or that sits on it at a position inconsistent with the category's generator count. $\mathrm{SU}(1)$ is on the chain at the position the count dictates: zero generators, the bottom. The earlier answer, $\mathrm{U}(1)\cdot SL(2,\mathbb{C})$, was seven-dimensional and sat on no rung of this ladder at all, which is precisely the discontinuity the reader of the neighbouring categories is entitled to object to.

## Why the Norm's Unit Group Is Not the Rung

The group $\mathrm{U}(1)\cdot SL(2,\mathbb{C})=\{\tilde Q:\lvert\langle\tilde Q\rangle_{\natural}\rvert=1\}$ preserves the biquaternion norm, and the corpus says so in as many words. The question is not whether it does but what kind of object it is.

**Proposition (the norm's unit group is rung-independent).** The group preserving $\langle\cdot\rangle_{\natural}$ is the same at every rung of the ladder, so it cannot be the group of any one rung.

*Proof.* The norm is a property of the algebra alone: $\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}=\det\mathsf{M}_2(\tilde Q)$ depends on no coupling, no connection and no category, and an isometry of it is defined without reference to any of them. Hence the isometry group is the same object in the free layer, in the strong category and in the primordial category; a group that does not vary along the ladder cannot index a position on it. Verified by writing the isometry condition, which mentions $\mathbb{B}$ and its conjugate only, and contains no $\kappa$, no $\tilde A_{\Phi}$ and no $T^{a}$.

**Corollary (naming it as the category's group is what produced the discontinuity).** An answer of the form "the free layer's group is $\mathrm{U}(1)\cdot SL(2,\mathbb{C})$" assigns to one rung a group shared by all rungs, and thereby leaves the free rung without a group of its own.

*Proof.* If $\mathrm{Sym}$ is taken to be the norm's unit group, the same expression is the group of every category, since by the proposition the isometry group does not vary; the series' four categories would then be distinguished by nothing, contradicting the ladder of §*The Ladder and the Bottom Rung*, whose rungs differ in generator count. The only assignment consistent with the ladder is the one that varies along it, which is the gauged internal group. Verified by substituting the isometry group for $\mathrm{Sym}$ in the ladder table and observing that all four rows collapse to one.

**Remark (the arena is not deleted, only relocated).** The correction does not assert that $\mathrm{U}(1)\cdot SL(2,\mathbb{C})$ is absent from the free layer. It asserts that it is the *arena*: the kinematic and norm-preserving structure every category carries, the spacetime side of the series rather than its force side. The corpus's own sentence — that the framework has more symmetry than the physics uses — is a statement about the arena and the compact group $\mathrm{U}(2)$ inside it, and it remains true at every rung. What it is not is the answer to *this* question, which asks which rung the category occupies.

**Remark (why the arena is not seven-dimensional in the equations).** The arena's kinematic factor is the Lorentz group, $SO^{+}(1,3)\cong SL(2,\mathbb{C})/\{\pm e_t\}$, acting by the rotor conjugation on the material sector and preserving the sector and the norm. The extra circle in the seven-dimensional group acts on the complexified field and rescales the norm, which is why the arena's group and the arena's *acting* group differ by a redundancy rather than by a symmetry. Either way the object is rung-independent, and the two readings of it are the subject of the companion articles and not of this one.

## What the Trivial Rung Still Asserts

**Proposition (de-gauging has this category as its fixed point).** Setting the coupling to zero in any category of the series lands on this one, and the landing point is $\mathrm{SU}(1)$, independent of which category one starts from.

*Proof.* At $\kappa=0$ the connection decouples and the covariant derivative becomes the plain gradient in every category; the residual group is then the group gauged at $\kappa=0$, which is the group of no generator. The map "set $\kappa$ to zero" therefore sends every rung to the bottom rung, and the bottom rung is a fixed point of it because $\kappa$ is already zero there. Verified by applying the limit to the covariant derivatives of the four categories and checking that the images agree.

**Corollary (the free layer is the series' zero, not its exception).** The category is the common limit of the other three, and its trivial group is what makes the other three's counts meaningful.

*Proof.* By the proposition every category maps to it at $\kappa=0$, so it is the common image; a ladder whose increments are measured from a rung needs that rung, and the count $0$ is what makes $3$, $8$ and $15$ counts rather than labels. Verified by the arithmetic of the increments, $3+5+7=15$ from a base of $0$.

**Remark (what "trivial" does not mean).** It does not mean the category is empty of structure. The four free equations exist, the norm exists, the mass shell exists, and the arena's group acts on all of them. It means that the category gauges no generator — that no force is switched on — which is exactly what the category's name says and exactly what the ladder's bottom rung records. A force-free universe is one in which the count is zero, and a count of zero is a position on the ladder, not an absence from it.

## What the Category Does Not Supply

**Supplied.** The rung and its count, the containment that reaches it from the rung above, the vanishing of the connection at every vertex, the identification of the free layer as the fixed point of de-gauging, and the separation of the rung from the arena.

**Not supplied.** Four boundaries, stated as boundaries.

- *A generator to gauge.* The category has none, and this is the content of the name. A reader looking for a non-abelian structure in the free layer will not find one, and the absence is the answer rather than a gap.
- *A value.* No mass, no coupling, no constant is fixed by the rung; the count is a dimension and not a number.
- *The upper rungs.* The seven generators that take the count from eight to fifteen, and the five that take it from three to eight, are the subject of the articles that own those rungs; stating them here would be restating another category's group.
- *A different arena.* The rung does not supply a new kinematic group. The arena is the same at every rung, and the free layer is where that fact is most visible, because the rung contributes nothing beside it.

## Summary

The category carries the trivial force group, and it is the bottom rung of the series' ladder.

$$
\boxed{\ \mathrm{Sym}=\mathrm{SU}(1)=\{e\},\qquad \dim\mathfrak{su}(1)=0,\qquad \text{generators gauged}:0\ }
$$

The ladder is nested, $\mathrm{SU}(1)\subset\mathrm{SU}(2)\subset\mathrm{SU}(3)\subset\mathrm{SU}(4)$, with counts $0,\,3,\,8,\,15$ and increments $3,\,5,\,7$. The strong rung is a stabiliser inside the primordial rung, and the free rung is the stabiliser that moves nothing; the containment that reaches it is the same containment used at the top. A force is a gauged generator, and this category gauges none, so its group is the one with no generator. The seven-dimensional group of unit-modulus biquaternions preserves the norm, but it does so at every rung and is therefore the arena rather than the rung; naming it as this category's group is what made the answer discontinuous with its neighbours, and the correction is to place it where it belongs. Setting the coupling to zero in any category lands here, so the free layer is the series' fixed point and the base from which the other three counts are measured.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{SU}(n)$ | The rung-$n$ group; $\dim\mathfrak{su}(n)=n^{2}-1$; nested, $\mathrm{SU}(n)\subset\mathrm{SU}(n+1)$ |
| $\mathrm{SU}(1)=\{e\}$ | The trivial group; this category's force group; one element, no generator |
| $\kappa$ | The coupling; zero throughout this category, by its definition |
| $\tilde A_{\Phi}=\tilde A_{\Phi}^{a}T^{a}$ | The connection of a category and its generators; absent here |
| $\mathrm{SU}(3)=\mathrm{Stab}_{\mathrm{SU}(4)}(e_t)$ | The strong rung as a stabiliser of a line in the rung above |
| $\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}$ | The biquaternion norm; a property of the algebra, hence rung-independent |
| $\mathrm{U}(1)\cdot SL(2,\mathbb{C})=\{\tilde Q:\lvert\langle\tilde Q\rangle_{\natural}\rvert=1\}$ | The norm's unit group; the arena, present identically at every rung |
| $SO^{+}(1,3)\cong SL(2,\mathbb{C})/\{\pm e_t\}$ | The arena's kinematic factor; the rotor conjugation on the material sector |
| $\mathrm{U}(2)$ | The compact group of the fields, inside the arena; rung-independent |

## Further Reading

- [*The $\mathrm{SU}(4)$ Model: Four Lines, Fifteen Generators, One Declaration*](the-su4-model-four-lines-fifteen-generators-one-declaration.html), for the top rung.
- [*Quantum Chromodynamics as the Residual of $\mathrm{SU}(4)$*](quantum-chromodynamics-as-the-residual-of-su4.html), for the strong rung as a stabiliser.
- [*Rank Five From Three*](rank-five-from-three-the-weak-factors-as-a-condensate-index.html) and [*The Photon as the Unbroken Mixture*](the-photon-as-the-unbroken-mixture.html), for the intermediate rungs.
- [*The Restructuring of the Primordial Force*](the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.html), for the descent between rungs.
- [*The Compact Sector of the Biquaternions Is $\mathfrak{u}(2)$*](the-compact-sector-of-the-biquaternions-is-u2.html), for the arena's compact group and the ceiling on the upper rungs.
- [*The Lorentz Group as Biquaternion Norm Automorphisms*](the-lorentz-group-as-biquaternion-norm-automorphisms.html), for the arena's kinematic group.
- [*The Minimal Coupling in Biquaternionic Form*](the-minimal-coupling-in-biquaternionic-form.html), for the coupling whose vanishing defines this category.
- [*Algebra and Element Conventions*](../articles_maths/algebra-and-element-conventions.html), for the norm and the conjugation.
