# __The Symmetry Group SU(4) of the Primordial Force__

## Introduction

The category *Biquaternion Universe Primordial Force* is the top rung of the series: one compact group, fifteen generators, one coupling, and the quartet of four lines above the restructuring scale $M_C$. The question this article answers is the one the block raises in its first sentence: **which group does the category carry?**

$$
\boxed{\ \mathrm{Sym}=\mathrm{SU}(4),\qquad \dim\mathfrak{su}(4)=15,\qquad \operatorname{rank}=3\ }
$$

Fifteen generators: twelve that move one line into another and three traceless diagonal ones. One group and nothing beside it — no second factor, no strong group made local, no abelian direction of its own. The primordial force is not a group *and* something else; it is the smallest compact simple group large enough to hold the four lines of the carrier as one multiplet, and everything the block states is a count on its fifteen.

**Why this is the rung and not an assumption.** A force, in this series, is a gauged generator; the ladder of the series is nested, and this is its fourth rung. The counts are $0,\,3,\,8,\,15$ for $\mathrm{SU}(1),\mathrm{SU}(2),\mathrm{SU}(3),\mathrm{SU}(4)$, and the increments are $3,\,5,\,7$. The primordial force is the rung at which the count is largest:
$$
\mathrm{SU}(1)\subset\mathrm{SU}(2)\subset\mathrm{SU}(3)\subset\mathrm{SU}(4),
\qquad
\dim\mathfrak{su}(n)=n^{2}-1 .
$$
What the category *gauges* is the fifteen, and the two rungs below it are the residues that survive when the vacuum picks a direction.

**What "given the carrier" means, stated plainly at the outset.** The algebra derives the group *given* a formal copy of the carrier; it does not manufacture the carrier. The corpus's own sentence is that the algebra derives the group given the carrier, and the honesty of the article depends on keeping that qualifier. The group therefore has an **address** — it acts on a formal copy of the four-line carrier — and the algebra is not entered. §*Where the Group Lives* separates the two layers, because a reader who conflates them will find the block's other statements contradictory when they are not.

- Companion article [*The $\mathrm{SU}(4)$ Model: Four Lines, Fifteen Generators, One Declaration of Rank Three*](the-su4-model-four-lines-fifteen-generators-one-declaration.html), for the group, the adjoint and the declaration that the algebra cannot make.
- Companion article [*The Counts of the Fifteen*](the-counts-of-the-fifteen-sixteen-cells-six-pairs-twelve-arrays-fifteen-generators.html), for the four distinct registers — sixteen cells, six pairs, twelve arrays, fifteen generators — and why none is the others.
- Companion article [*Quantum Chromodynamics as the Residual of $\mathrm{SU}(4)$*](quantum-chromodynamics-as-the-residual-of-su4.html), for the rung below this one as a stabiliser.
- Companion article [*Rank Five From Three: The Weak Factors as a Condensate Index*](rank-five-from-three-the-weak-factors-as-a-condensate-index.html), for the rank obstruction that keeps the weak factors out of the fifteen.
- Companion article [*The Symmetry Group SU(3) of the Strong Force*](the-symmetry-group-su3-of-the-strong-force.html) and [*The Symmetry Group SU(2)\_L × U(1)\_Y of the Electroweak Force*](the-symmetry-group-su2l-times-u1y-of-the-electroweak-force.html), for the rungs below.
- Companion article [*The Symmetry Group SU(1) of the Force-Free Case*](the-symmetry-group-su1-of-the-force-free-case.html), for the bottom of the ladder and the ladder's own statement.

## Where the Group Lives

**Definition (the group of the category).** The category's *group* is the internal group whose generators its connection carries,
$$
\tilde A=\tilde A^{a}T^{a},\qquad [T^{a},T^{b}]=i f^{abc}T^{c},\qquad a=1,\dots,15,
$$
with $g_4$ the single coupling. The *count* of the category is $\dim\mathfrak{g}=15$.

**Proposition (the count is fifteen, and it is four cells minus the trace).** The group has fifteen generators: twelve that carry a pair of distinct lines into one another and three traceless diagonal ones.

*Proof.* A basis of $\mathfrak{su}(4)$ is the set of off-diagonal unit matrices $e_{ij}$ with $i\neq j$ and the traceless diagonal combinations. There are $4\cdot3=12$ ordered pairs $i\neq j$, and the diagonal space of $4\times4$ Hermitian matrices is four-dimensional, of which the traceless part is three-dimensional because the trace is removed. Hence $12+3=15=4^{2}-1$. The two counts are the same count under two registers — four diagonal cells, three diagonal generators — and the passage between them is exactly the removal of the trace. Verified by the dimension formula and by enumerating the basis.

**Remark (one group, one grid, one copy).** The corpus's identity $16=1+15$ — sixteen cells, one trace, fifteen generators — is what replaces the older and wrong $24=16+4+4$. With one group there is one grid and one copy of the fifteen; the four that is missing twice in the older arithmetic is the two weak factors, and they are not in the model. This is the arithmetic form of the statement that the category has one group and not three.

**Proposition (the two layers of the claim).** The group acts on a formal copy of the carrier and not inside the algebra: no generator is an element of $\mathbb{B}$, and every generator is an endomorphism of $\mathbb{B}$.

*Proof.* The generators $T^{a}$ are $4\times4$ matrices acting on the four-line carrier $\mathbb{C}^{4}$; $\mathbb{B}\cong M_2(\mathbb{C})$ is four *complex* dimensional and its elements act on a two-dimensional module, so a $4\times4$ generator cannot be an element of $\mathbb{B}$ acting on $\mathbb{B}$ by left multiplication. It is instead an endomorphism of the carrier, built from products of the algebra's units, and the group's containment is that of endomorphism algebras rather than of elements. This is the corpus's *Layer B*: the group has an address, the algebra is not entered. Verified by comparing the module dimensions, two for $\mathbb{B}$ and four for the carrier.

**Remark (why the layer distinction is load-bearing).** The block's claim that the primordial force is "the algebra's own" and the block's claim that "no generator is an element of $\mathbb{B}$" are both true, and they are true in different layers. Layer A is the algebra's elements; Layer B is the endomorphisms of a formal copy of the carrier. A statement that mixes them is wrong even when both halves are right, and the mixing is the single most common error the block's own articles correct.

## What the Fifteen Act On

**The four lines.** The carrier is the quartet $(t,x,y,z)$ — four lines of one multiplet. A line letter is a coordinate on the $4\times4$ table and not a charge: a sentence that names a line is physics only if it survives a relabelling of the four lines. The corpus's rule is to write *four lines* for $(t,x,y,z)$ and *twelve directions and three diagonal directions* for the fifteen.

**The one thing the algebra cannot say.** Which of the four lines is the lepton. That is the whole of the declaration, and it is stated as a declaration because no theorem in the algebra fixes it. It adds no block to the fifteen and moves no eigenvalue; it is the one piece of the model that is a choice, and naming it as a choice is what keeps the rest a derivation.

**Proposition (the unbroken phase, and the split below it).** Above $M_C$ all fifteen directions are massless and the group is $\mathrm{SU}(4)$ acting on the quartet. Below the restructuring the frame is fixed and the fifteen separate.

*Proof.* Above $M_C$ the vacuum is symmetric, so no direction of the adjoint is distinguished and the mass operator is proportional to the identity on the fifteen; hence every direction is massless. Once the frame $D$ is fixed by the vacuum, the adjoint decomposes and the diagonal frame's differences become the Cartan of the surviving octet while the sum becomes the abelian direction $B-L$; the six directions that move the distinguished line acquire mass. The count is then nine massless and six heavy. Verified by the decomposition of the adjoint under the surviving subgroup and by the spectrum of $\operatorname{ad}(iD)$.

## The Rung Below, and the Rank Obstruction

**Proposition (the strong rung is a stabiliser).** The strong group is the stabiliser of a line inside the primordial group,
$$
\mathrm{SU}(3)=\mathrm{Stab}_{\mathrm{SU}(4)}(\mathbb{C}e_t),
\qquad \dim\mathfrak{su}(3)=8 .
$$

*Proof.* The subgroup of $\mathrm{SU}(4)$ fixing a complex line is $\mathrm{U}(3)$, whose traceless part acting on the orthogonal three-space is $\mathrm{SU}(3)$; its dimension is $15-7=8$, the seven removed directions being the six that move the fixed line plus the phase of the line itself. Hence the descent from fifteen to eight is the removal of the directions that move the distinguished line, and it is a containment and not an analogy. Verified by the dimension count and by the stabiliser computation.

**Proposition (the rank obstruction).** The weak factors cannot be debris of the breaking, because the rank cannot rise.

*Proof.* The rank of $\mathfrak{su}(4)$ is three, and a maximal torus of a subalgebra lies in a maximal torus of the algebra, so the rank of every subalgebra is at most three; the endpoint requires rank $2+1+1+1=5$ — the octet's two, the abelian $B-L$ direction, and the two weak factors' own — and no chain of breakings reaches five from three, in any order, at any temperature, with any dynamics. The weak factors therefore arrive as an *index* on the condensate that breaks the group and not as fragments of it. Verified by the rank lemma applied to $\mathfrak{su}(4)$ and to the endpoint algebra.

**Remark (what survives is $\mathfrak{u}(3)$ and not $\mathfrak{su}(3)$).** The kernel of the adjoint action of the vacuum on the fifteen is $\mathfrak{u}(3)$, so the degeneracy is into $\mathrm{SU}(3)_c\times\mathrm{U}(1)_{B-L}$ and not into $\mathrm{SU}(3)$ alone. The extra direction is the sum of the three frame diagonals, and it is why the rank does not move in this step: $3\to2+1=3$. This is stated here because it is the precise sense in which the rung below is adjacent to this one; the abelian factor is a piece of *this* rung's bookkeeping and the strong article's concern.

## What the Category Does Not Supply

**Supplied.** The group and its count, the adjoint and its decomposition, the single coupling $g_4$, the unbroken phase above $M_C$, the descent to the strong rung as a stabiliser, and the rank obstruction that places the weak factors outside the fifteen.

**Not supplied.** Four boundaries, stated as boundaries.

- *Which line is the lepton.* The algebra fixes the group and the multiplet and not the labelling; that is the declaration, and it is the one choice in the model.
- *Chirality where the symmetry acts.* The model is not chiral where the group acts, and the corpus now states this as a theorem about the model rather than a caveat about a representation. The one-sided action of the algebra on a chiral spinor module remains the open problem, and it is not solved by enlarging the group.
- *An instanton inside the algebra.* The $\mathrm{SU}(4)$ instanton is a matrix transcription outside the algebra; the group's topological sectors are reached on the formal copy and not on $\mathbb{B}$.
- *A value.* No mass, no coupling value, no mixing angle. The article is a statement of the group and its count, and it fixes no number.

## Summary

The category carries $\mathrm{SU}(4)$, the top rung of the ladder, with fifteen generators and rank three.

$$
\boxed{\ \mathrm{Sym}=\mathrm{SU}(4),\quad \dim=15=12+3,\quad \operatorname{rank}=3,\quad \text{one coupling } g_4\ }
$$

The fifteen are twelve line-mixing directions and three traceless diagonals, which is four diagonal cells minus the trace; one group, one grid, one copy. The group acts on a formal copy of the four-line carrier and not inside the algebra, so its generators are endomorphisms of $\mathbb{B}$ and the algebra is not entered. Above $M_C$ all fifteen are massless; below it the frame splits them nine and six. The rung below is the stabiliser of a line, $\mathrm{SU}(3)=\mathrm{Stab}_{\mathrm{SU}(4)}(\mathbb{C}e_t)$, and the descent removes the seven directions that move it. The rank cannot rise from three, so the weak factors of the rung below arrive as an index and not as debris — the obstruction that makes the ladder a ladder and not a tree.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{SU}(4)$ | The category's group; dimension $15$, rank $3$ |
| $T^{a}$, $a=1,\dots,15$ | The generators; twelve off-diagonal, three traceless diagonal |
| $g_4$ | The single coupling of the category |
| $(t,x,y,z)$ | The four lines of the carrier; coordinates on the table, not charges |
| $16=1+15$ | Sixteen cells, one trace, fifteen generators |
| $M_C$ | The restructuring scale; above it the phase is unbroken |
| $\operatorname{ad}(iD)$ | The adjoint action of the vacuum frame; its kernel is the surviving algebra |
| $\mathrm{SU}(3)=\mathrm{Stab}_{\mathrm{SU}(4)}(\mathbb{C}e_t)$ | The rung below, as a stabiliser of a line |
| $\mathfrak{u}(3)=\mathfrak{su}(3)\oplus\mathfrak{u}(1)_{B-L}$ | What the kernel supplies; the ninth direction is the frame-diagonal sum |

## Further Reading

- [*The $\mathrm{SU}(4)$ Model: Four Lines, Fifteen Generators, One Declaration*](the-su4-model-four-lines-fifteen-generators-one-declaration.html), for the group and the declaration.
- [*The Counts of the Fifteen*](the-counts-of-the-fifteen-sixteen-cells-six-pairs-twelve-arrays-fifteen-generators.html), for the four registers.
- [*Construction of the AXF Matrices of the Fifteen Generators*](construction-of-the-axf-matrices-of-the-fifteen-generators.html), for the arrays themselves.
- [*Classification of the Bosons*](classification-of-the-bosons-in-the-su4-model-one-grid-fifteen-generators-nine-massless-six-heavy.html), for the nine-and-six split.
- [*The Primordial Coupling*](the-primordial-coupling.html), for the one coupling.
- [*Quantum Chromodynamics as the Residual of $\mathrm{SU}(4)$*](quantum-chromodynamics-as-the-residual-of-su4.html), for the rung below.
- [*Rank Five From Three*](rank-five-from-three-the-weak-factors-as-a-condensate-index.html), for the rank obstruction.
- [*The Restructuring of the Primordial Force*](the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.html), for the descent itself.
- [*The Symmetry Group SU(3) of the Strong Force*](the-symmetry-group-su3-of-the-strong-force.html), [*The Symmetry Group SU(2)\_L × U(1)\_Y of the Electroweak Force*](the-symmetry-group-su2l-times-u1y-of-the-electroweak-force.html), [*The Symmetry Group SU(1) of the Force-Free Case*](the-symmetry-group-su1-of-the-force-free-case.html), for the rungs below.
