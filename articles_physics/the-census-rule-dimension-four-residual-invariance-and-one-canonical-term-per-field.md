# __The Census Rule: Dimension Four, Residual Invariance, and One Canonical Term per Field__

## Introduction

**The claim.** The Lagrangian of the Standard Model, written in the broken phase and in the mass basis, is a list. This article states the rule that generates the list and then counts it. The count is not the point. The point is that the rule is stated before the list, so that a reader with a pencil can add the rows up and get the same number.

**The answer.**

$$
\boxed{\;47=4+8+17+18,\qquad 49=47+2,\qquad 53=47+6,\qquad 20=47-27\;}
$$

**The standing.** Every piece in the list is standard theory. Nothing here is derived from the biquaternion algebra and no coefficient is computed. What the article and its twenty-three companions add is three things: a criterion that says which pieces are possible, a proof that nothing else is possible, and a count with its rule attached to it.

**Why a rule and not a list.** A list of terms is unfalsifiable. Given a Lagrangian, a reader can delete a term and ask why it was there, and the answer "it is in the Standard Model" is circular. A criterion makes every term answerable: it is in the list because it is a dimension-four invariant of the residual group, and every dimension-four invariant of the residual group is in the list.

## The Criterion

**Four conditions, and a piece must satisfy all four.**

A piece is admissible when it is a Lorentz scalar, invariant under the residual group $\mathrm{SU}(3)_c\times\mathrm{U}(1)_{\mathrm{em}}$, of mass dimension at most four, and built from the fields the broken phase contains.

The first two are symmetries. The third is renormalisability. The fourth is what makes this a broken-phase list rather than a symmetric-phase one: the fields are the mass eigenstates, so a piece is built from $G^a_\mu$, $A_\mu$, $Z_\mu$, $W^\pm_\mu$, $h$ and the twelve fermion species, and not from $W_{a,\mu}$, $B_\mu$ and the doublet.

**Why the broken phase.** Because the list is then one list. In the symmetric phase a piece may be built from a doublet, and the number of pieces depends on how the scalar is written, on whether the conjugate doublet is a second object, and on how many components are counted separately. In the broken phase every field has a definite mass, one scalar remains, and the residual group is a product of a colour factor and a phase. The pieces are then exactly the terms a calculator would use.

**The price, stated now.** Residual invariance alone is too weak. A Majorana mass $\tfrac12m_\nu\bar\nu^c_L\nu_L$ is a dimension-three invariant of $\mathrm{SU}(3)_c\times\mathrm{U}(1)_{\mathrm{em}}$ and would be admitted. It is excluded, and the exclusion does not come from this criterion but from a second one: every piece must descend from an invariant of the *unbroken* group, or from its vacuum. That second criterion is stated and used in [The Completeness of the List](the-completeness-of-the-list-why-no-other-dimension-four-piece-exists.html) and [The Unitary-Gauge Image](the-unitary-gauge-image-the-lineage-of-every-piece-and-where-the-three-goldstones-went.html), and the neutrino mass is its one witness.

## The Four Counting Conventions

A count needs a convention as much as a criterion needs a rule. Four are used, and each is stated so that it can be changed without ambiguity.

| Convention | Statement | What it excludes |
|---|---|---|
| one piece per canonical term | a sum over colour, and a sum over the species of one type, is one piece | eighteen quark kinetic terms counted as one |
| $\mathrm{h.c.}$ counted once | a term and its Hermitian conjugate are one piece | doubling the charged current |
| self-interactions inside the curvature | the triple and quartic gauge vertices are sub-structures of the curvatures and are counted as vertices, not pieces | six extra rows in the piece list |
| coefficient-blind | two pieces differing only by a coefficient are one piece | counting $h\bar uu$ and $h\bar dd$ as different kinds |

**The second convention is the one that decides the total.** The charged current has two terms, one with quarks and one with leptons, and they are two rows and not one. Its Hermitian conjugate is a third and a fourth term of the same two pieces.

**The third convention is the one that decides between the two counts.** With the self-interactions folded into the curvatures the count is forty-seven. With them separated the count is fifty-three, and the six added structures are the two triple vertices $\gamma W^+W^-$ and $ZW^+W^-$ and the four quartic vertices $W^+W^-W^+W^-$, $W^+W^-AA$, $W^+W^-ZZ$ and $W^+W^-AZ$. [The Gauge Self-Interactions](the-gauge-self-interactions-two-triple-vertices-and-four-quartic-vertices.html) counts the same six from the tensor structures. The category uses forty-seven for pieces and fifty-three for vertices.

**The fourth convention is what keeps the count finite.** Nine $h\bar ff$ rows differ only by which species carries the coefficient; they are nine and not one, because the coefficients differ, and the convention that makes them nine is the convention that a piece is a monomial with definite field content.

## The Summation

**Four lines, one number.**

$$
\underbrace{4}_{\text{curvatures}}+\underbrace{8}_{\text{scalar}}+\underbrace{17}_{\text{fermion kinetic and interactions}}+\underbrace{18}_{\text{Yukawa}}=47 .
$$

**The blocks behind the four numbers.**

| Block | Rows | What it contains |
|---|---|---|
| curvatures | $4$ | gluon, photon, $Z$, $W$ |
| scalar | $8$ | kinetic, mass, $hWW$, $hZZ$, $hhWW$, $hhZZ$, $h^3$, $h^4$ |
| fermion kinetic and interactions | $17$ | twelve kinetics, QCD, QED, two charged currents, neutral current |
| Yukawa | $18$ | nine masses, nine $h\bar ff$ |

**The two rows the summation excludes, and why.** The $W$ and $Z$ masses are not invariants of the unbroken group; they exist only after the vacuum is chosen, and they are counted separately. With them the row count is $47+2=49$. The forty-seven is the count of rows with an ancestor term; the forty-nine is the count of rows.

**The three derived counts.** Vertices: $47+6=53$. Blocks: folding the three sums of one type gives $47-11-8-8=20$. Parameters: eighteen constants, and nineteen with the vacuum angle. Each is a different question asked of the same list.

## The Three Counts

**Pieces, vertices, blocks.**

| Count | Value | The question it answers |
|---|---|---|
| pieces | $47$ | how many monomials with distinct field content and coefficient |
| rows | $49$ | how many monomials including the two Proca masses |
| vertices | $53$ | how many Feynman rules at tree level |
| blocks | $20$ | how many structures once the flavour sums are folded |
| constants | $18$ | how many numbers carry the rows |
| parameters | $19$ | how many numbers the theory has |

**Why the three do not contradict each other.** They count different objects: a monomial, a vertex, a structure with a sum inside it. A reader who expects one number is expecting the list to have one purpose, and it has three, because it is used to enumerate terms, to draw diagrams and to count parameters.

**Why the piece count is smaller than the vertex count.** Six structures are vertices and not pieces, and each is a monomial in the field strength rather than in the fields. A vertex is what a diagram uses; a piece is what a Lagrangian writes.

**Why the block count is smaller than the piece count.** A block is a piece with its colour and flavour sums folded. Twelve kinetic rows are one block because they share a coefficient and a tensor structure; the same for nine masses and nine $h\bar ff$.

## What the Count Is Not

**It is not a count of measurements.** The nineteen parameters are nineteen measurements in principle, but several are measured once and determine many rows. A count of rows would be a count of observables only if every row were measured separately, and most are not.

**It is not a derivation.** The rule says which terms are possible; it does not say why the content is the content, why the group is the group, or why the couplings have the values they have. Those are the questions of [The Compact Sector of the Biquaternions Is $\mathfrak{u}(2)$](the-compact-sector-of-the-biquaternions-is-u2.html), and this article does not answer them.

**It is not invariant under a change of convention.** Change the third convention and the piece count moves by six; change the first and it moves by twenty-seven. The invariance is in the rule and not in the number, which is why the rule is printed beside the number in every article of this category.

## Checks

1. The criterion. Four conditions, and each is used at least once.
2. The piece sum. $4+8+17+18=47$.
3. The row count. $47+2=49$ with the two Proca masses.
4. The vertex count. $47+6=53$, the six being two triple and four quartic structures.
5. The block count. $47-11-8-8=20$.
6. The constants. Eighteen, and nineteen with the vacuum angle.
7. The scalar block. $1+1+2+2+2=8$: kinetic, mass, two $hVV$, two $hhVV$, two self-pieces.
8. The fermion block. $12+5=17$: twelve kinetics and five interactions.
9. The Yukawa block. $9+9=18$, in bijection through $m_f=y_fv/\sqrt2$.
10. The conventions. Four stated, and each with the count it changes.

## Summary

The list is generated by a criterion — Lorentz scalar, invariant under $\mathrm{SU}(3)_c\times\mathrm{U}(1)_{\mathrm{em}}$, dimension at most four, built from the broken content — and counted by four stated conventions.

The count is forty-seven pieces: four from the curvatures, eight from the scalar, seventeen from the fermion kinetic term and its interactions, eighteen from the Yukawa term. Two further rows, the Proca masses, are not invariants of the unbroken group and bring the row count to forty-nine. Six further structures are vertices and bring the vertex count to fifty-three. Folding the three flavour sums gives twenty blocks. The constants are eighteen and the parameters nineteen.

The numbers differ because they count different objects, and each article of the category prints the rule beside the number it uses.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| admissible | satisfying the four conditions |
| piece | one monomial with definite field content and coefficient |
| row | a piece, or one of the two Proca masses |
| vertex | a tree-level Feynman rule |
| block | a piece with its colour and flavour sums folded |

## Further Reading

- [The Completeness of the List](the-completeness-of-the-list-why-no-other-dimension-four-piece-exists.html). Why no fiftieth piece exists.
- [The Unitary-Gauge Image](the-unitary-gauge-image-the-lineage-of-every-piece-and-where-the-three-goldstones-went.html). The forty-seven rows against their ancestors.
- [The Complete Lagrangian](the-census-in-one-display-forty-seven-terms-fifty-three-vertices-twenty-blocks-and-nineteen-parameters.html). The numbered table.
- [The Coefficients the List Carries](the-coefficients-the-list-carries-eighteen-constants-and-the-one-that-multiplies-no-piece.html). The eighteen and the nineteenth.
- [The Audit](the-audit-every-constant-against-every-piece.html). The rows against the numbers that fix them.
