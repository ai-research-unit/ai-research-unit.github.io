# __Decompositions and Comparison of the Remarkable Subspaces of the Split-Complexoid__

## Introduction

This article reads the **two involutions** of the split-complex algebra as a group, the decompositions they cut out, and the place of the two resulting subspaces beside the two of the complex field. The two involutions are the identity and the conjugation $j\mapsto-j$; the conjugation coincides with the idempotent conjugation, so the involution group reduces to the single edge $\{\mathrm{id},\bar{\cdot}\}\cong\mathbb{Z}/2$. The identity cuts out the degenerate decomposition $\mathbb{D}=\mathbb{D}\oplus 0$; the conjugation cuts out the content-bearing decomposition $\mathbb{D}=\mathbb{R}_{\mathbb{D}}\oplus j\mathbb{R}_{\mathbb{D}}$ into a fixed and an anti-fixed line; and beside them the idempotent basis cuts out the finer decomposition $\mathbb{D}=\mathbb{R}\Pi_1\oplus\mathbb{R}\Pi_2$, which is not induced by an involution.

The subspaces themselves — their bases, their intersections, their sums, the action of the involution on each and the restricted norm — are *Split-Complexoid Subspaces*, which owns the line-by-line theory; this article takes the two subspaces and the two decompositions as its object and compares them. The complex two are *Decompositions and Comparison of the Remarkable Subspaces of the Complex Numbers*. The products that decide the closure questions are *The Two Products of the Split-Complexoid Space*, both products read on the subspaces being *Remarkable Subspaces and the Two Products of the Split-Complexoid Space*. The norm is *Split-Complex Norm and Invertibility*; the idempotents and the ideals are *Split-Complex Idempotents and Projections* and *Split-Complex Ideals and Peirce Decomposition*.

**Conventions.** The algebra is $\mathbb{D}=\mathbb{R}[x]/(x^2-1)$, basis $1,j$, $j^2=+1$; a general element is $Q=q+jq'$; the conjugate is $\bar Q=q-jq'$; the idempotents are $\Pi_1=\tfrac12(1+j)$ and $\Pi_2=\tfrac12(1-j)$ with $Q=q_+\Pi_1+q_-\Pi_2$, $q_+=q+q'$ and $q_-=q-q'$. The real subspace is $\mathbb{R}_{\mathbb{D}}=\{q\}$ and the split imaginary subspace is $j\mathbb{R}_{\mathbb{D}}=\{jq'\}$.

## The Two Involutions and Their Group

An **involution** of $\mathbb{D}$ is an $\mathbb{R}$-algebra automorphism $\sigma$ with $\sigma^2=\mathrm{id}$ — an algebra map that is its own inverse. The algebra carries two of them:

$$
\mathrm{id} : Q\mapsto Q, \qquad \bar{\cdot} : Q\mapsto \bar Q = q-jq' .
$$

**Proposition.** $\mathbb{D}$ has exactly two involutions, the identity and the conjugation, and they form the two-element group $\{\mathrm{id},\bar{\cdot}\}\cong\mathbb{Z}/2$.

**Proof.** Both are $\mathbb{R}$-algebra automorphisms, and $\overline{\bar Q}=Q$, so both are involutions and they are distinct. Conversely let $\sigma$ be an involution. It fixes $\mathbb{R}$ and permutes the idempotents, since $\sigma(\Pi)^2=\sigma(\Pi)$ and $\sigma(\Pi_1)+\sigma(\Pi_2)=\sigma(1)=1$; the only idempotents of $\mathbb{D}$ are $0$, $1$, $\Pi_1$ and $\Pi_2$, so $\sigma$ either fixes the pair $\{\Pi_1,\Pi_2\}$ pointwise or swaps it. In the first case $\sigma$ fixes a set that spans $\mathbb{D}$, so $\sigma=\mathrm{id}$. In the second case $\sigma(\Pi_1)=\Pi_2$ and $\sigma(\Pi_2)=\Pi_1$, whence $\sigma(j)=\sigma(\Pi_1-\Pi_2)=\Pi_2-\Pi_1=-j$ and $\sigma=\bar{\cdot}$. So the list is complete, and the group is $\mathbb{Z}/2$.

The single non-trivial involution is the conjugation, and the group is the automorphism group of the algebra, developed in *Split-Complex Automorphisms and Derivations*. $\mathbb{D}$ has a real coefficient field, so only the algebra conjugation survives and the group collapses to $\mathbb{Z}/2$.

**Remark (the two conjugations coincide).** The **idempotent conjugation** is the swap of the two idempotent coordinates, the map $\tau$ with

$$
\tau(Q) = q_-\Pi_1 + q_+\Pi_2 ,
$$

named after the idempotent basis and treated as a map in *Split-Complex Algebra*, which writes it with a tilde. In the basis $\{1,j\}$ the swap reads $\tau(Q)=(q-q')\Pi_1+(q+q')\Pi_2=q-jq'=\bar Q$, so it is not a second involution but the same one, $\tau=\bar{\cdot}$. A reader who expects the "conjugate with respect to the idempotent basis" to be a new map finds it identical to the algebra conjugation, and this coincidence is a special feature of the two-dimensional case: with only one non-trivial involution available, the two constructions have no room to differ.

## The Two Decompositions

Each involution splits $\mathbb{D}$ into its fixed space and its anti-fixed space, and the two involutions give two decompositions.

**The degenerate decomposition of the identity.** The identity fixes every element and negates none:

$$
\mathbb{D} = \mathbb{D} \oplus 0, \qquad \text{fixed space } \mathbb{D}, \quad \text{anti-fixed space } 0 .
$$

It carries no content; it is recorded for completeness, as the first row of the four-dimensional table is the whole space.

**The decomposition of the conjugation.** The conjugation cuts $\mathbb{D}$ into the real line and the split imaginary line:

$$
\mathbb{D} = \mathbb{R}_{\mathbb{D}} \oplus j\mathbb{R}_{\mathbb{D}}, \qquad Q = q_r + jq_i, \qquad q_r = \tfrac12(Q+\bar Q), \quad q_i = \tfrac12 j^{-1}(Q-\bar Q) = q' .
$$

The two **projections** are $\tfrac12(Q+\bar Q)=q$ onto the real line and $\tfrac12(Q-\bar Q)=jq'$ onto the split imaginary line, and each is $\mathbb{R}$-linear and idempotent; their sum is the identity. This is the content-bearing decomposition of the elementary conjugation, the two-dimensional shadow of the scalar–vector decomposition of the four-dimensional algebra.

**The finer idempotent decomposition.** The idempotent basis gives a second decomposition of the plane,

$$
\mathbb{D} = \mathbb{R}\Pi_1 \oplus \mathbb{R}\Pi_2, \qquad Q = q_+\Pi_1 + q_-\Pi_2, \qquad q_+ = q+q', \quad q_- = q-q',
$$

whose members are the two finer lines $\mathbb{R}\Pi_1$ and $\mathbb{R}\Pi_2$. It is **not** induced by an involution of the algebra: the two lines are not the fixed and anti-fixed lines of any algebra involution, because the only non-trivial involution interchanges them and has for eigenspaces the two earlier lines. (As a real-linear involution the diagonal map $\mathrm{diag}(1,-1)$ in the idempotent basis does have them for eigenspaces, but it is not an algebra map, since it does not preserve the unit.) The four lines are the four one-dimensional subspaces of the plane, and the two decompositions are the two ways of pairing them:

| decomposition | first member | second member | induced by |
|---|---|---|---|
| degenerate | $\mathbb{D}$ | $0$ | $\mathrm{id}$ |
| conjugation | $\mathbb{R}_{\mathbb{D}}=\{q\}$ | $j\mathbb{R}_{\mathbb{D}}=\{jq'\}$ | $\bar{\cdot}$ |
| idempotent | $\mathbb{R}\Pi_1=\{t\Pi_1\}$ | $\mathbb{R}\Pi_2=\{t\Pi_2\}$ | no involution |

In the four-dimensional algebra there are three decompositions, all induced by involutions; here there are two content-bearing ones, and only the first of them is induced by an involution.

## The Two Subspaces and Their Properties

The two members of the conjugation decomposition are

$$
\mathbb{R}_{\mathbb{D}} = \{Q : \bar Q = Q\} = \{q\}, \qquad j\mathbb{R}_{\mathbb{D}} = \{Q : \bar Q = -Q\} = \{jq'\},
$$

the fixed and the anti-fixed line. Their bases, dimensions, intersections, sums, the action of the involution on each and the restricted norm are *Split-Complexoid Subspaces*; three properties are needed for the comparison below and are collected here.

**Closure under the products.** The real line is closed under both products, and the split imaginary line is closed under neither. Multiplication by an element of $\mathbb{R}_{\mathbb{D}}$ preserves it, so $\mathbb{R}_{\mathbb{D}}$ is a **subalgebra**, $\mathbb{R}_{\mathbb{D}}\cong\mathbb{R}$; the product of two elements of $j\mathbb{R}_{\mathbb{D}}$ is real, $jq'_1\cdot jq'_2=q'_1q'_2$, so $j\mathbb{R}_{\mathbb{D}}$ is not closed — it is closed under addition but not under multiplication.

| subspace | $\dim_{\mathbb{R}}$ | closed under $Q_1Q_2$ and $Q_1\bar Q_2$ | units | isotropic elements |
|---|---|---|---|---|
| $\mathbb{R}_{\mathbb{D}}$ | $1$ | yes, a subalgebra $\cong\mathbb{R}$ | every non-zero element | none |
| $j\mathbb{R}_{\mathbb{D}}$ | $1$ | no | every non-zero element | none |
| $\mathbb{R}\Pi_1$ | $1$ | yes, an ideal | none | every element |
| $\mathbb{R}\Pi_2$ | $1$ | yes, an ideal | none | every element |

**Units.** The two eigenlines consist entirely of units apart from the origin, because the norm is definite on each: $\langle q\rangle=q^2>0$ on the real line and $\langle jq'\rangle=-q'^2<0$ on the split imaginary line, so neither line meets the null cone except at $0$. The two idempotent lines are the opposite extreme: the norm vanishes on each, so every element is a zero divisor and none is a unit. The criterion and the group of units are *Split-Complex Norm and Invertibility*.

**Isotropic elements.** The isotropic elements of $\mathbb{D}$ are exactly the elements of the two idempotent lines, $\mathbb{R}\Pi_1\cup\mathbb{R}\Pi_2$, the zero-divisor set; the two eigenlines contain none apart from the origin. This is the statement that the null cone is the union of the two idempotent lines, owned by *Split-Complex Zero Divisors*, and it is the reason the four lines split into the two definite eigenlines and the two isotropic idempotent lines.

## Comparison with the Two Complex Subspaces

The complex field is the definite two-dimensional algebra, and its subspace theory is the simplest of the family: the conjugation is the unique non-trivial involution, with the real line and the pure imaginary line for its fixed and anti-fixed spaces, and there are exactly two distinguished subspaces, both of dimension one.

| feature | $\mathbb{C}$ | $\mathbb{D}$ |
|---|---|---|
| non-trivial involutions | $1$ | $1$ |
| eigenlines | $\mathbb{R}_{\mathbb{C}}$, $i\mathbb{R}_{\mathbb{C}}$ | $\mathbb{R}_{\mathbb{D}}$, $j\mathbb{R}_{\mathbb{D}}$ |
| norm on the anti-fixed line | $+a'^2$, definite | $-q'^2$, definite |
| idempotent lines | none | $\mathbb{R}\Pi_1$, $\mathbb{R}\Pi_2$ |
| isotropic elements | none | the two idempotent lines |

The two algebras have the same pair of involutive lines, the real and the anti-fixed one, and the same single non-trivial involution; the difference is the **sign of the norm on the anti-fixed line**, $+a'^2$ against $-q'^2$, which is the sign of the square of the generator, and the presence in $\mathbb{D}$ of the two idempotent lines, which $\mathbb{C}$ cannot have because a field has no idempotent other than $0$ and $1$.

## Summary

The split-complex algebra has two involutions, the identity and the conjugation $j\mapsto-j$, and they form the group $\{\mathrm{id},\bar{\cdot}\}\cong\mathbb{Z}/2$; the idempotent conjugation is the same map as the algebra conjugation, so it adds no second involution. The identity cuts out the degenerate decomposition $\mathbb{D}=\mathbb{D}\oplus0$; the conjugation cuts out the decomposition $\mathbb{D}=\mathbb{R}_{\mathbb{D}}\oplus j\mathbb{R}_{\mathbb{D}}$ with the projections $\tfrac12(Q+\bar Q)$ and $\tfrac12(Q-\bar Q)$; and the idempotent basis cuts out the finer decomposition $\mathbb{D}=\mathbb{R}\Pi_1\oplus\mathbb{R}\Pi_2$, not induced by an involution.

The real line is a subalgebra and the split imaginary line is not closed under the products; both eigenlines consist of units apart from the origin, and the isotropic elements are exactly the two idempotent lines. Only one involution remains on $\mathbb{D}$ — the Hermitian conjugation coincides with the bar — so the discussion reduces to the two eigenlines of that one involution, with the centre and the vector subspace falling on the whole algebra and the origin. Compared with the complex field, the two eigenlines are the same two up to the sign of the norm on the anti-fixed line, and $\mathbb{D}$ has in addition the two idempotent lines the field lacks.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\bar{\cdot}$ | the unique non-trivial involution, $\bar Q=q-jq'$ |
| $\tau(Q)=q_-\Pi_1+q_+\Pi_2=\bar Q$ | the idempotent conjugation, equal to the bar |
| $\{\mathrm{id},\bar{\cdot}\}\cong\mathbb{Z}/2$ | the involution group |
| $\mathbb{R}_{\mathbb{D}}=\{q\}$ | the fixed line, a subalgebra $\cong\mathbb{R}$ |
| $j\mathbb{R}_{\mathbb{D}}=\{jq'\}$ | the anti-fixed line, not closed under products |
| $\mathbb{R}\Pi_1,\mathbb{R}\Pi_2$ | the finer idempotent lines, not induced by an involution |
| $q_r=q$, $q_i=q'$ | the eigenline coordinates |
| $\mathcal{N}=\mathbb{R}\Pi_1\cup\mathbb{R}\Pi_2$ | the isotropic set, the two idempotent lines |

## Further Reading

- Israel Nathan Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975), for involutions, eigenspaces and the elementary classification of the two-dimensional involutions.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for isotropic lines, definite lines and the signature of a plane form.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the split-complex plane and the two isotropic directions of $\mathrm{Cl}_{1,0}$.
- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the scalar–vector and idempotent decompositions of the split-complex plane.
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for the fixed spaces of the involutions of an algebra and the structure of its idempotents.
