# __Decompositions and Comparison of the Remarkable Subspaces of the Split-Complex Numbers__

## Introduction

This article reads the **two involutions** of the split-complex algebra as a group, the decompositions they cut out, and the place of the two resulting subspaces beside the six of the biquaternion algebra and the two of the complex field. The two involutions are the identity and the conjugation $j\mapsto-j$; the conjugation coincides with the idempotent conjugation, so what survives of the four-fold involution group of the biquaternion algebra is the single edge $\{\mathrm{id},\bar{\cdot}\}\cong\mathbb{Z}/2$. The identity cuts out the degenerate decomposition $\mathbb{D}=\mathbb{D}\oplus 0$; the conjugation cuts out the content-bearing decomposition $\mathbb{D}=\mathbb{R}_{\mathbb{D}}\oplus j\mathbb{R}_{\mathbb{D}}$ into a fixed and an anti-fixed line; and beside them the idempotent basis cuts out the finer decomposition $\mathbb{D}=\mathbb{R}\Pi_1\oplus\mathbb{R}\Pi_2$, which is not induced by an involution.

The subspaces themselves — their bases, their intersections, their sums, the action of the involution on each and the restricted norm — are *Split-Complex Subspaces*, which owns the line-by-line theory; this article takes the two subspaces and the two decompositions as its object and compares them. The four-dimensional patterns it compares them with are *Decompositions Along the Remarkable Subspaces* and *Comparison of the Remarkable Subspaces*; the complex two are *Decompositions and Comparison of the Remarkable Subspaces of the Complex Numbers*. The products that decide the closure questions are *The Two Products of the Split-Complex Space*, both products read on the subspaces being *Remarkable Subspaces and the Two Products of the Split-Complex Space*. The norm is *Split-Complex Norm and Invertibility*; the idempotents and the ideals are *Split-Complex Idempotents and Projections* and *Split-Complex Ideals and Peirce Decomposition*.

**Conventions.** The algebra is $\mathbb{D}=\mathbb{R}[x]/(x^2-1)$, basis $1,j$, $j^2=+1$; a general element is $A=a+ja'$; the conjugate is $\bar A=a-ja'$; the idempotents are $\Pi_{1,2}=\tfrac12(1\pm j)$ with $A=A_+\Pi_1+A_-\Pi_2$ and $A_\pm=a\pm a'$. The real subspace is $\mathbb{R}_{\mathbb{D}}=\{a\}$ and the split imaginary subspace is $j\mathbb{R}_{\mathbb{D}}=\{ja'\}$.

## The Two Involutions and Their Group

An **involution** of $\mathbb{D}$ is an $\mathbb{R}$-algebra automorphism $\sigma$ with $\sigma^2=\mathrm{id}$ — an algebra map that is its own inverse. The algebra carries two of them:

$$
\mathrm{id} : A\mapsto A, \qquad \bar{\cdot} : A\mapsto \bar A = a-ja' .
$$

**Proposition.** $\mathbb{D}$ has exactly two involutions, the identity and the conjugation, and they form the two-element group $\{\mathrm{id},\bar{\cdot}\}\cong\mathbb{Z}/2$.

**Proof.** Both are $\mathbb{R}$-algebra automorphisms, and $\overline{\bar A}=A$, so both are involutions and they are distinct. Conversely let $\sigma$ be an involution. It fixes $\mathbb{R}$ and permutes the idempotents, since $\sigma(\Pi)^2=\sigma(\Pi)$ and $\sigma(\Pi_1)+\sigma(\Pi_2)=\sigma(1)=1$; the only idempotents of $\mathbb{D}$ are $0$, $1$, $\Pi_1$ and $\Pi_2$, so $\sigma$ either fixes the pair $\{\Pi_1,\Pi_2\}$ pointwise or swaps it. In the first case $\sigma$ fixes a set that spans $\mathbb{D}$, so $\sigma=\mathrm{id}$. In the second case $\sigma(\Pi_1)=\Pi_2$ and $\sigma(\Pi_2)=\Pi_1$, whence $\sigma(j)=\sigma(\Pi_1-\Pi_2)=\Pi_2-\Pi_1=-j$ and $\sigma=\bar{\cdot}$. So the list is complete, and the group is $\mathbb{Z}/2$.

The single non-trivial involution is the conjugation, and the group is the automorphism group of the algebra, developed in *Split-Complex Automorphisms and Derivations*. In the four-dimensional algebra the group has three non-identity commuting involutions $\bar{\cdot}$, ${}^{*}$ and ${}^{\natural}$, forming the Klein four-group $(\mathbb{Z}/2)^2$, with the reversal $\flat$ outside it. One of the three is the conjugation of the coefficient field and one the conjugation of the quaternion factor; $\mathbb{D}$ has a real coefficient field and no quaternion factor, so only the algebra conjugation survives and the group collapses to $\mathbb{Z}/2$.

**Remark (the two conjugations coincide).** The **idempotent conjugation** is the swap of the two idempotent coordinates, the map $\tau$ with

$$
\tau(A) = A_-\Pi_1 + A_+\Pi_2 ,
$$

named after the idempotent basis and treated as a map in *Split-Complex Algebra*, which writes it with a tilde. In the basis $\{1,j\}$ the swap reads $\tau(A)=(a-a')\Pi_1+(a+a')\Pi_2=a-ja'=\bar A$, so it is not a second involution but the same one, $\tau=\bar{\cdot}$. A reader who expects the "conjugate with respect to the idempotent basis" to be a new map finds it identical to the algebra conjugation, and this coincidence is a special feature of the two-dimensional case: with only one non-trivial involution available, the two constructions have no room to differ.

## The Two Decompositions

Each involution splits $\mathbb{D}$ into its fixed space and its anti-fixed space, and the two involutions give two decompositions.

**The degenerate decomposition of the identity.** The identity fixes every element and negates none:

$$
\mathbb{D} = \mathbb{D} \oplus 0, \qquad \text{fixed space } \mathbb{D}, \quad \text{anti-fixed space } 0 .
$$

It carries no content; it is recorded for completeness, as the first row of the four-dimensional table is the whole space.

**The decomposition of the conjugation.** The conjugation cuts $\mathbb{D}$ into the real line and the split imaginary line:

$$
\mathbb{D} = \mathbb{R}_{\mathbb{D}} \oplus j\mathbb{R}_{\mathbb{D}}, \qquad A = A_r + jA_i, \qquad A_r = \tfrac12(A+\bar A), \quad A_i = \tfrac12 j^{-1}(A-\bar A) = a' .
$$

The two **projections** are $\tfrac12(A+\bar A)=a$ onto the real line and $\tfrac12(A-\bar A)=ja'$ onto the split imaginary line, and each is $\mathbb{R}$-linear and idempotent; their sum is the identity. This is the content-bearing decomposition of the elementary conjugation, the two-dimensional shadow of the scalar–vector decomposition of the four-dimensional algebra.

**The finer idempotent decomposition.** The idempotent basis gives a second decomposition of the plane,

$$
\mathbb{D} = \mathbb{R}\Pi_1 \oplus \mathbb{R}\Pi_2, \qquad A = A_+\Pi_1 + A_-\Pi_2, \qquad A_\pm = a\pm a',
$$

whose members are the two finer lines $\mathbb{R}\Pi_1$ and $\mathbb{R}\Pi_2$. It is **not** induced by an involution of the algebra: the two lines are not the fixed and anti-fixed lines of any algebra involution, because the only non-trivial involution interchanges them and has for eigenspaces the two earlier lines. (As a real-linear involution the diagonal map $\mathrm{diag}(1,-1)$ in the idempotent basis does have them for eigenspaces, but it is not an algebra map, since it does not preserve the unit.) The four lines are the four one-dimensional subspaces of the plane, and the two decompositions are the two ways of pairing them:

| decomposition | first member | second member | induced by |
|---|---|---|---|
| degenerate | $\mathbb{D}$ | $0$ | $\mathrm{id}$ |
| conjugation | $\mathbb{R}_{\mathbb{D}}=\{a\}$ | $j\mathbb{R}_{\mathbb{D}}=\{ja'\}$ | $\bar{\cdot}$ |
| idempotent | $\mathbb{R}\Pi_1=\{t\Pi_1\}$ | $\mathbb{R}\Pi_2=\{t\Pi_2\}$ | no involution |

In the four-dimensional algebra there are three decompositions, all induced by involutions; here there are two content-bearing ones, and only the first of them is induced by an involution.

## The Two Subspaces and Their Properties

The two members of the conjugation decomposition are

$$
\mathbb{R}_{\mathbb{D}} = \{A : \bar A = A\} = \{a\}, \qquad j\mathbb{R}_{\mathbb{D}} = \{A : \bar A = -A\} = \{ja'\},
$$

the fixed and the anti-fixed line. Their bases, dimensions, intersections, sums, the action of the involution on each and the restricted norm are *Split-Complex Subspaces*; three properties are needed for the comparison below and are collected here.

**Closure under the products.** The real line is closed under both products, and the split imaginary line is closed under neither. Multiplication by an element of $\mathbb{R}_{\mathbb{D}}$ preserves it, so $\mathbb{R}_{\mathbb{D}}$ is a **subalgebra**, $\mathbb{R}_{\mathbb{D}}\cong\mathbb{R}$; the product of two elements of $j\mathbb{R}_{\mathbb{D}}$ is real, $ja'\cdot jb'=a'b'$, so $j\mathbb{R}_{\mathbb{D}}$ is not closed — it is closed under addition but not under multiplication.

| subspace | $\dim_{\mathbb{R}}$ | closed under $AC$ and $A\bar C$ | units | isotropic elements |
|---|---|---|---|---|
| $\mathbb{R}_{\mathbb{D}}$ | $1$ | yes, a subalgebra $\cong\mathbb{R}$ | every non-zero element | none |
| $j\mathbb{R}_{\mathbb{D}}$ | $1$ | no | every non-zero element | none |
| $\mathbb{R}\Pi_1$ | $1$ | yes, an ideal | none | every element |
| $\mathbb{R}\Pi_2$ | $1$ | yes, an ideal | none | every element |

**Units.** The two eigenlines consist entirely of units apart from the origin, because the norm is definite on each: $N(a)=a^2>0$ on the real line and $N(ja')=-a'^2<0$ on the split imaginary line, so neither line meets the null cone except at $0$. The two idempotent lines are the opposite extreme: the norm vanishes on each, so every element is a zero divisor and none is a unit. The criterion and the group of units are *Split-Complex Norm and Invertibility*.

**Isotropic elements.** The isotropic elements of $\mathbb{D}$ are exactly the elements of the two idempotent lines, $\mathbb{R}\Pi_1\cup\mathbb{R}\Pi_2$, the zero-divisor set; the two eigenlines contain none apart from the origin. This is the statement that the null cone is the union of the two idempotent lines, owned by *Split-Complex Zero Divisors*, and it is the reason the four lines split into the two definite eigenlines and the two isotropic idempotent lines.

## Comparison with the Six Biquaternion Subspaces

The biquaternion algebra has **six** remarkable real subspaces, the fixed and anti-fixed spaces of its three commuting involutions. They are read from four **coordinate blocks**:

$$
A_1=\mathbb{R}e_0, \qquad A_2=\mathbb{R}(ie_0), \qquad B_1=\operatorname{span}_\mathbb{R}\{e_1,e_2,e_3\}, \qquad B_2=\operatorname{span}_\mathbb{R}\{ie_1,ie_2,ie_3\},
$$

two scalar blocks and two vector blocks, and each remarkable subspace is the sum of two of them: the centre is $A_1\oplus A_2$, the vector subspace $B_1\oplus B_2$, the quaternion subspace $A_1\oplus B_1$, the anti-quaternion subspace $A_2\oplus B_2$, the Hermitian subspace $A_1\oplus B_2$ and the anti-Hermitian subspace $A_2\oplus B_1$.

The six subspaces are the fixed and anti-fixed spaces of the three commuting involutions $\bar{\cdot}$, ${}^{\natural}$, ${}^{*}$: the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ and the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$ are the fixed and anti-fixed spaces of the coefficient conjugation, the centre $\mathbb{C}_{\mathbb{B}}$ and the vector subspace $\mathrm{Vect}(\mathbb{B})$ those of the natural conjugation, and the Hermitian and anti-Hermitian subspaces $\mathbb{M}_+$, $\mathbb{M}_-$ those of the Hermitian conjugation.

The same three involutions are read on $\mathbb{D}$ with the reading fixed in this category: the natural conjugation is the identity, since there is no quaternion factor for it to act on, and the Hermitian conjugation coincides with the bar; only the bar is non-trivial. Reading the fixed and anti-fixed spaces involution by involution gives the collapse.

| involution | fixed space in $\mathbb{B}$ | anti-fixed space in $\mathbb{B}$ | fixed space on $\mathbb{D}$ | anti-fixed space on $\mathbb{D}$ |
|---|---|---|---|---|
| coefficient conjugation $\bar{\cdot}$ | $\mathbb{H}_{\mathbb{B}}$ | $i\mathbb{H}_{\mathbb{B}}$ | $\mathbb{R}_{\mathbb{D}}$ | $j\mathbb{R}_{\mathbb{D}}$ |
| natural conjugation ${}^{\natural}=\mathrm{id}$ | $\mathbb{C}_{\mathbb{B}}$ (centre) | $\mathrm{Vect}(\mathbb{B})$ | $\mathbb{D}$ | $0$ |
| Hermitian conjugation ${}^{*}=\bar{\cdot}$ | $\mathbb{M}_+$ | $\mathbb{M}_-$ | $\mathbb{R}_{\mathbb{D}}$ | $j\mathbb{R}_{\mathbb{D}}$ |

So the six subspaces of the four-dimensional algebra collapse to **two** proper non-trivial subspaces and the two trivial ones: the quaternion and Hermitian subspaces both fall on the real line, the anti-quaternion and anti-Hermitian subspaces both fall on the split imaginary line, the centre falls on the whole algebra and the vector subspace on the origin. The two degenerate images are the price of the two facts that have no content on $\mathbb{D}$: the natural conjugation is the identity, so its fixed space is everything and its anti-fixed space nothing; and the Hermitian conjugation adds no second involution to the bar, so it adds no subspace.

**Remark.** The count agrees with the count of involutions. Three distinct commuting involutions give three fixed spaces and three anti-fixed spaces, six in all, and no two coincide; one non-trivial involution gives one fixed space and one anti-fixed space, two in all. The collapse of the group $\{\mathrm{id},\bar{\cdot},{}^{\natural},{}^{*}\}\cong(\mathbb{Z}/2)^2$ to $\{\mathrm{id},\bar{\cdot}\}\cong\mathbb{Z}/2$ is exactly the collapse of the six subspaces to two, and the two that survive are the fixed and the anti-fixed line of the one involution that is left.

## Comparison with the Two Complex Subspaces

The complex field is the definite two-dimensional algebra, and its subspace theory is the simplest of the family: the conjugation is the unique non-trivial involution, with the real line and the pure imaginary line for its fixed and anti-fixed spaces, and there are exactly two distinguished subspaces, both of dimension one.

| feature | $\mathbb{C}$ | $\mathbb{D}$ |
|---|---|---|
| non-trivial involutions | $1$ | $1$ |
| eigenlines | $\mathbb{R}_{\mathbb{C}}$, $i\mathbb{R}_{\mathbb{C}}$ | $\mathbb{R}_{\mathbb{D}}$, $j\mathbb{R}_{\mathbb{D}}$ |
| norm on the anti-fixed line | $+a'^2$, definite | $-a'^2$, definite |
| idempotent lines | none | $\mathbb{R}\Pi_1$, $\mathbb{R}\Pi_2$ |
| isotropic elements | none | the two idempotent lines |

The two algebras have the same pair of involutive lines, the real and the anti-fixed one, and the same single non-trivial involution; the difference is the **sign of the norm on the anti-fixed line**, $+a'^2$ against $-a'^2$, which is the sign of the square of the generator, and the presence in $\mathbb{D}$ of the two idempotent lines, which $\mathbb{C}$ cannot have because a field has no idempotent other than $0$ and $1$. Compared with the biquaternion algebra, whose three involutions cut out six subspaces, the split-complex algebra is the degenerate commutative rung: one involution, two subspaces, and no lattice of intersections and sums beyond the two complementary pairs.

## Summary

The split-complex algebra has two involutions, the identity and the conjugation $j\mapsto-j$, and they form the group $\{\mathrm{id},\bar{\cdot}\}\cong\mathbb{Z}/2$; the idempotent conjugation is the same map as the algebra conjugation, so it adds no second involution. The identity cuts out the degenerate decomposition $\mathbb{D}=\mathbb{D}\oplus0$; the conjugation cuts out the decomposition $\mathbb{D}=\mathbb{R}_{\mathbb{D}}\oplus j\mathbb{R}_{\mathbb{D}}$ with the projections $\tfrac12(A+\bar A)$ and $\tfrac12(A-\bar A)$; and the idempotent basis cuts out the finer decomposition $\mathbb{D}=\mathbb{R}\Pi_1\oplus\mathbb{R}\Pi_2$, not induced by an involution.

The real line is a subalgebra and the split imaginary line is not closed under the products; both eigenlines consist of units apart from the origin, and the isotropic elements are exactly the two idempotent lines. Compared with the six remarkable subspaces of the biquaternion algebra, which are the fixed and anti-fixed spaces of its three commuting involutions, two of those involutions lose their content on $\mathbb{D}$ — the natural conjugation is the identity and the Hermitian conjugation coincides with the bar — so the six collapse to the two eigenlines of the one involution that remains, with the centre and the vector subspace falling on the whole algebra and the origin. Compared with the complex field, the two eigenlines are the same two up to the sign of the norm on the anti-fixed line, and $\mathbb{D}$ has in addition the two idempotent lines the field lacks.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\bar{\cdot}$ | the unique non-trivial involution, $\bar A=a-ja'$ |
| $\tau(A)=A_-\Pi_1+A_+\Pi_2=\bar A$ | the idempotent conjugation, equal to the bar |
| $\{\mathrm{id},\bar{\cdot}\}\cong\mathbb{Z}/2$ | the involution group |
| $\mathbb{R}_{\mathbb{D}}=\{a\}$ | the fixed line, a subalgebra $\cong\mathbb{R}$ |
| $j\mathbb{R}_{\mathbb{D}}=\{ja'\}$ | the anti-fixed line, not closed under products |
| $\mathbb{R}\Pi_1,\mathbb{R}\Pi_2$ | the finer idempotent lines, not induced by an involution |
| $A_r=a$, $A_i=a'$ | the eigenline coordinates |
| $\bar{\cdot}$, ${}^{\natural}=\mathrm{id}$, ${}^{*}=\bar{\cdot}$ | the three involutions of $\mathbb{B}$ read on $\mathbb{D}$ |
| $\mathcal{N}=\mathbb{R}\Pi_1\cup\mathbb{R}\Pi_2$ | the isotropic set, the two idempotent lines |

## Further Reading

- Israel Nathan Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975), for involutions, eigenspaces and the elementary classification of the two-dimensional involutions.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for isotropic lines, definite lines and the signature of a plane form.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the split-complex plane and the two isotropic directions of $\mathrm{Cl}_{1,0}$.
- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the scalar–vector and idempotent decompositions of the split-complex plane.
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for the fixed spaces of the involutions of an algebra and the structure of its idempotents.
