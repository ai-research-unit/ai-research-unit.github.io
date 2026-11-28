# __The Symmetry Group SU(3) of the Strong Force__

## Introduction

The category *Biquaternion Universe Strong Force* is the rung below the primordial one: the strong sector as the residual of the group above $M_C$, and the sector where the algebra meets its wall. The question this article answers is: **which group does the category carry?**

$$
\boxed{\ \mathrm{Sym}=\mathrm{SU}(3),\qquad \dim\mathfrak{su}(3)=8,\qquad \operatorname{rank}=2\ }
$$

Eight generators: six that carry one colour line into another and two Cartan. Rank two, and the two are the two differences of the three diagonal frame. One group, and it is a *stabiliser* — not a new group added to the series, but the part of the rung above that leaves a chosen line alone.

**The placement on the ladder.** A force is a gauged generator, and the ladder is nested with counts $0,\,3,\,8,\,15$. This rung is the third:
$$
\mathrm{SU}(3)=\mathrm{Stab}_{\mathrm{SU}(4)}(\mathbb{C}e_t),
\qquad
\mathrm{SU}(1)\subset\mathrm{SU}(2)\subset\mathrm{SU}(3)\subset\mathrm{SU}(4).
$$
The passage from fifteen to eight is the removal of the seven directions that move a line — six that carry it elsewhere and one that is its phase — and the passage from eight to three is the removal of the five that distinguish a line from the two it leaves.

**The wall, stated at the outset because the article's credibility depends on it.** No generator of this group is an element of $\mathbb{B}$, and none can act $\mathbb{B}$-linearly on a $\mathbb{B}$-module. $\mathrm{SU}(3)$ is reached on a **formal copy** of the carrier, where its generators are endomorphisms of $\mathbb{B}$ and not elements of it — each of the eight is a sum of two or three Conway words $e_{\imath}[\,]e_{\jmath}$, none of them a single product. So the group has an address, and the algebra is not entered. *Contained* means contained in the endomorphism algebra on the copy; it does not mean contained in $\mathbb{B}$.

- Companion article [*Quantum Chromodynamics as the Residual of $\mathrm{SU}(4)$: The $\mathrm{SU}(3)$ Wall, Restated*](quantum-chromodynamics-as-the-residual-of-su4.html), for the stabiliser statement and the two layers.
- Companion article [*The Gluon: An Octet Outside the Biquaternion Algebra*](the-gluon-an-octet-outside-the-biquaternion-algebra.html), for the octet and its carrier.
- Companion article [*The Eight AXF Matrices of the Gluons in Detail*](the-eight-axf-matrices-of-the-gluons-in-detail-every-matrix-every-gluon-its-entries-its-spectrum-and-its-fate.html), for the eight matrices.
- Companion article [*The Three Lines in $\mathrm{SU}(3)$: A Coordinate Label on the Eight, Not a Charge*](the-three-lines-in-su3-a-coordinate-label-on-the-eight-not-a-charge.html), for the colour letters.
- Companion article [*The Symmetry Group SU(4) of the Primordial Force*](the-symmetry-group-su4-of-the-primordial-force.html), for the rung above, of which this is a stabiliser.
- Companion article [*The Symmetry Group SU(2)\_L × U(1)\_Y of the Electroweak Force*](the-symmetry-group-su2l-times-u1y-of-the-electroweak-force.html) and [*The Symmetry Group SU(1) of the Force-Free Case*](the-symmetry-group-su1-of-the-force-free-case.html), for the rungs below.

## The Eight, and Where They Come From

**Definition (the group of the category).** The category's *group* is the internal group whose generators its connection carries,
$$
\tilde A=\tilde A^{a}T^{a},\qquad [T^{a},T^{b}]=i f^{abc}T^{c},\qquad a=1,\dots,8 ,
$$
with $g_3$ the coupling. The *count* is $\dim\mathfrak{su}(3)=8$.

**Proposition (the count is eight, and it is two Cartan plus six roots).** The group has eight generators: two commuting diagonal ones and six that carry one line into another.

*Proof.* A basis of $\mathfrak{su}(3)$ is the six off-diagonal unit matrices $e_{ij}$, $i\neq j$, together with the two traceless diagonal combinations; there are $3\cdot2=6$ ordered pairs and $3-1=2$ traceless diagonal directions, so $6+2=8=3^{2}-1$. The two diagonal generators are a maximal torus, hence the rank is two. Verified by the dimension formula and by enumerating the basis.

**Proposition (the octet is the stabiliser of a line).** The eight are the directions of $\mathrm{SU}(4)$ that leave a chosen line fixed.

*Proof.* $\mathrm{SU}(3)=\mathrm{Stab}_{\mathrm{SU}(4)}(\mathbb{C}e_t)$, of dimension $15-7=8$; the seven removed are the six that move the fixed line into one of the other three plus the phase of the line, and the eight that remain are exactly the root-and-Cartan system of $\mathfrak{su}(3)$ acting on the three lines orthogonal to the fixed one. Verified by the dimension count and by matching the surviving directions to the $3\times3$ block.

**Remark (the two lines of the claim).** Layer A: no strong-generator is an element of $\mathbb{B}$. Layer B: each generator is a sum of two or three Conway words and so is an endomorphism of $\mathbb{B}$ on the formal copy. The group therefore *has an address* — it acts on a copy of the carrier — and the algebra is not entered. Both statements are true and they are true in different layers; a reader who keeps one meaning of *reached* will find "the strong group is a residual" contradictory when it is not.

**Remark (why eight equals eight is a coincidence of counting).** Both $\mathbb{B}$ and $\mathfrak{su}(3)$ are eight real dimensional, and the equality is not an embedding. $\mathbb{B}$'s compact part is $\mathrm{U}(2)$, of dimension four, and its natural module is two-dimensional, whereas $\mathfrak{su}(3)$ needs a complex three-dimensional fundamental. Equality of dimensions is a coincidence of counting, not a containment, and the corpus states it as such.

## What the Group Acts On

**The colour triplet and the octet.** The quarks sit in the complex three-dimensional fundamental $\mathbf{3}$ and the gluons in the eight-dimensional adjoint. The three colour lines are a coordinate label on the eight and not a charge: a sentence that names a line is physics only if it survives a relabelling of the three.

**Proposition (the ninth slot).** What the breaking of the rung above supplies is $\mathfrak{u}(3)$ and not $\mathfrak{su}(3)$, so the strong sector arrives with one abelian direction beside it, $B-L$.

*Proof.* The kernel of the adjoint action of the vacuum on the fifteen is $\mathfrak{u}(3)=\mathfrak{su}(3)\oplus\mathfrak{u}(1)$, of dimension nine; the extra direction is the sum of the three frame diagonals, and it is why the rank does not move from the rung above: $3\to2+1=3$. The strong group is the traceless part, and the abelian part is the $B-L$ direction of the same breaking. Verified by decomposing the fifteen under the surviving algebra and counting nine.

**Remark (the group and the count are not the same object).** Eight is the count of generators; nine is the count of directions the kernel supplies; three is the count of colour lines; and the hadron spectrum's counts are different again. The block's articles keep these registers apart, and the article that mixes them is wrong even when every individual number is right.

## What the Category Does Not Supply

**Supplied.** The group and its count, the octet as a stabiliser of a line, the rank-two torus and its two differences, the triplet and the adjoint, the ninth direction that arrives with the breaking, and the two-layer statement of where the group lives.

**Not supplied.** Five boundaries, stated as boundaries.

- *The group from the algebra alone.* Three colour lines, the beta coefficient and the parton densities are data; the block imports them and says so. Nothing in the series derives the dimension three, the group $\mathrm{SU}(3)$, or the reason the factor should exist at all, and the corpus states plainly that an article which quietly assumes a strong group has fabricated its premise.
- *Confinement.* The mechanism is not derived; the block reads confinement as a loss of partonic information and states that no confinement mechanism is available on the present construction. Above $M_C$ there is no confinement at all.
- *Asymptotic freedom.* The beta coefficient is imported as data, not computed from the framework; the one-loop coefficients are transcribed.
- *A value.* No strong coupling value, no $\Lambda_{\mathrm{QCD}}$. The article fixes the group and its count and no number.
- *A different arena.* The kinematic group is the same at every rung; this category supplies the strong rung and not a new spacetime.

## Summary

The category carries $\mathrm{SU}(3)$, the third rung, with eight generators and rank two.

$$
\boxed{\ \mathrm{Sym}=\mathrm{SU}(3),\quad \dim=8=2+6,\quad \operatorname{rank}=2,\quad \mathrm{SU}(3)=\mathrm{Stab}_{\mathrm{SU}(4)}(\mathbb{C}e_t)\ }
$$

The eight are two Cartan differences and six roots; the two are the nonzero differences of the three diagonal frame. The group is the stabiliser of a line in the rung above, so the descent from fifteen to eight removes seven directions and is a containment and not an analogy. It is reached on a formal copy of the carrier: its generators are endomorphisms of $\mathbb{B}$, each a sum of two or three Conway words, and no generator is an element of $\mathbb{B}$ — the group has an address, and the algebra is not entered. The breaking that produces it supplies $\mathfrak{u}(3)$ rather than $\mathfrak{su}(3)$, the ninth direction being $B-L$, and the rank stays at three. What the block imports rather than derives — three colour lines, the beta coefficient, the parton densities — is stated as imported, and confinement is read as information loss rather than derived as a mechanism.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{SU}(3)$ | The category's group; dimension $8$, rank $2$ |
| $T^{a}$, $a=1,\dots,8$ | Two Cartan and six root generators |
| $\mathrm{SU}(3)=\mathrm{Stab}_{\mathrm{SU}(4)}(\mathbb{C}e_t)$ | The group as the stabiliser of a line in the rung above |
| $g_3$ | The strong coupling |
| $\mathbf{3}$, $\mathbf{8}$ | The quark triplet and the gluon octet |
| $e_{\imath}[\,]e_{\jmath}$ | Conway words; the generators are sums of two or three, hence endomorphisms of $\mathbb{B}$ |
| $\mathfrak{u}(3)=\mathfrak{su}(3)\oplus\mathfrak{u}(1)_{B-L}$ | What the breaking supplies; dimension nine |
| Layer A / Layer B | Element of $\mathbb{B}$ / endomorphism of a formal copy of the carrier |

## Further Reading

- [*Quantum Chromodynamics as the Residual of $\mathrm{SU}(4)$*](quantum-chromodynamics-as-the-residual-of-su4.html), for the wall and the stabiliser.
- [*The Gluon: An Octet Outside the Biquaternion Algebra*](the-gluon-an-octet-outside-the-biquaternion-algebra.html), for the octet.
- [*The Eight AXF Matrices of the Gluons in Detail*](the-eight-axf-matrices-of-the-gluons-in-detail-every-matrix-every-gluon-its-entries-its-spectrum-and-its-fate.html), for the matrices.
- [*The Three Lines in $\mathrm{SU}(3)$*](the-three-lines-in-su3-a-coordinate-label-on-the-eight-not-a-charge.html), for the colour letters.
- [*The Lagrangian and Quantum Chromodynamics: The Triplet, the Octet and the Feynman Rules*](the-lagrangian-and-quantum-chromodynamics-the-triplet-the-octet-and-the-feynman-rules.html), for the action.
- [*Asymptotic Freedom and the Running of the Strong Coupling*](asymptotic-freedom-and-the-running-of-the-strong-coupling.html), for the imported beta coefficient.
- [*Confinement and the Loss of Partonic Information*](confinement-and-the-loss-of-partonic-information-in-biquaternionic-form.html), for confinement as an information channel.
- [*The Symmetry Group SU(4) of the Primordial Force*](the-symmetry-group-su4-of-the-primordial-force.html), for the rung above.
- [*The Symmetry Group SU(2)\_L × U(1)\_Y of the Electroweak Force*](the-symmetry-group-su2l-times-u1y-of-the-electroweak-force.html), [*The Symmetry Group SU(1) of the Force-Free Case*](the-symmetry-group-su1-of-the-force-free-case.html), for the rungs below.
