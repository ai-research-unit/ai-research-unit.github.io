# __Decompositions Along the Remarkable Subspaces__

## Introduction

The remarkable subspaces of *Introduction to the Remarkable Subspaces* organise the reduced biquaternion space in three ways, and this article writes the three decompositions and compares them. The first is the **block decomposition along the two involutions**: the bar and the natural sign are two commuting involutions, so the real four-dimensional space splits into the **four common eigenspaces**, each a real line, and each labelled by the pair of its eigenvalues under the two involutions. The second is the **decomposition along a single involution**, the **halving** of the space into the fixed and the anti-fixed space of that involution; there are three halvings, those of the bar, the natural sign and the star, and each is a grouping of the four blocks two by two. The third is the **decomposition along the idempotents**, the splitting $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\Pi_+\oplus\mathbb{C}\Pi_-$ by the two eigenlines of the multiplication by $j$, and it is the only one of the three that is a decomposition of the **algebra** and not only of the space.

**The results.** The four blocks are the four real lines
$$
\mathbb{B}_{\mathrm{r}}=\mathbb{R}\ \oplus\ \mathbb{R}i\ \oplus\ \mathbb{R}j\ \oplus\ \mathbb{R}ij,
$$
the common eigenspaces of the bar and the natural sign, the first two being also the eigenspaces of the star with the signs $+$ and $-$. The three halvings are
$$
\mathbb{C}\oplus\mathbb{C}j,\qquad \mathbb{R}\{1,j\}\oplus\mathbb{R}\{i,ij\},\qquad \mathbb{R}\{1,ij\}\oplus\mathbb{R}\{i,j\}=\mathbb{B}_{\mathrm{r}},
$$
the decompositions of the natural sign, the bar and the star; each is the grouping of the four blocks two by two according to the sign of the involution, and each is a **$\mathbb{Z}_{2}$-grading** of the algebra but not a decomposition of it into two subalgebras, because the homogeneous spaces of degree one are not closed under the product. The idempotent decomposition
$$
\mathbb{B}_{\mathrm{r}}=\mathbb{C}\Pi_+\oplus\mathbb{C}\Pi_-
$$
is of the other kind: it is the product of the two minimal ideals, it is the unique algebra direct-product decomposition, and its two summands are the two simple modules of *Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions*. The two kinds differ in what is closed: in a grading only the products of the same parity are constrained, while in a direct product each summand is a subalgebra and the mixed products vanish.

**Boundaries.** The subspaces and their characters are *Introduction to the Remarkable Subspaces*, above this article in this category; the involutions are *The Two Involutions and the Group of Involutions of the Reduced Biquaternions*; the idempotents are *Square Roots of One and the Idempotents of the Algebra of the Reduced Biquaternions*; and the ideals and the Peirce decomposition are *Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions*. The subspaces at a glance, with the closure of each under the product, are *Comparison of the Remarkable Subspaces*, below this article. The biquaternion counterparts are *Decompositions Along the Remarkable Subspaces* of the biquaternion category and *The Specificities of the Biquaternion Algebra*, §*The $\mathbb{Z}_{2}$-Grading*.

## The Block Decomposition Along the Two Involutions

### The Two Involutions and Their Common Eigenspaces

**The bar and the natural sign commute and are both of square one, so they diagonalise simultaneously, and the common eigenlines are four.**

**Theorem (simultaneous diagonalisation).** The bar $\bar{\cdot}$ and the natural sign ${}^{\natural}$ commute, ${}^{\natural}\bar{\cdot}=\bar{\cdot}{}^{\natural}$, and each has square one; hence the real space decomposes into the four **common eigenspaces**
$$
\mathbb{B}_{\mathrm{r}}=\bigoplus_{(\varepsilon_{1},\varepsilon_{2})\in\{\pm1\}^{2}}\mathbb{B}_{(\varepsilon_{1},\varepsilon_{2})},\qquad
\mathbb{B}_{(\varepsilon_{1},\varepsilon_{2})}=\{Q_\pm:\bar Q_\pm=\varepsilon_{1}Q_\pm,\ Q_\pm^{\natural}=\varepsilon_{2}Q_\pm\},
$$
each of real dimension one.

*Proof.* The two involutions commute because ${}^{*}=\bar{\cdot}\circ{}^{\natural}$ is an involution (*The Two Involutions and the Group of Involutions of the Reduced Biquaternions*), and two commuting involutions are simultaneously diagonalisable over $\mathbb{R}$; each is $\pm1$ on each common eigenline, and the four eigenvalues give the four spaces. Because the two involutions act on the four basis elements by $\pm$ signs and no two basis elements carry the same sign pair, each common eigenspace is one of the four basis lines and has dimension one.

### The Four Blocks

**The four blocks are the four real coordinate lines, and the star reads them with the signs $+,-,-,+$.**

**Theorem (the blocks).** The four blocks are
$$
\mathbb{B}_{(+,-)}=\mathbb{R}j,\qquad \mathbb{B}_{(-,+)}=\mathbb{R}i,\qquad \mathbb{B}_{(-,-)}=\mathbb{R}ij,\qquad \mathbb{B}_{(+,+)}=\mathbb{R},
$$
and the star acts on them with the eigenvalue $\varepsilon_{3}=\varepsilon_{1}\varepsilon_{2}$, so $\mathbb{R}$ and $\mathbb{R}ij$ are star-fixed and $\mathbb{R}i$ and $\mathbb{R}j$ star-negated.

*Proof.* The characters of the four lines of *Introduction to the Remarkable Subspaces* give the labels: $\mathbb{R}$ is $(+,+)$, $\mathbb{R}i$ is $(-,+)$, $\mathbb{R}j$ is $(+,-)$ and $\mathbb{R}ij$ is $(-,-)$. The star eigenvalue is $\varepsilon_{1}\varepsilon_{2}$ because ${}^{*}=\bar{\cdot}\circ{}^{\natural}$.

**Corollary (the block decomposition is the finest).** The block decomposition is the common refinement of the three halvings: each halving groups the four blocks two by two, and the three halvings are the three pairings
$$
\{++\,,\,{-+}\}\ \text{and}\ \{+-,\,--\},\qquad \{++\,,\,+-\}\ \text{and}\ \{-,+,\,--\},\qquad \{++\,,\,--\}\ \text{and}\ \{+-,-\+\}
$$
for the natural sign, the bar and the star respectively.

## The Decomposition Along Each Involution

### The Three Halvings

**Each involution halves the space, and the three halvings are the three complementary pairs of coordinate planes.**

**Theorem (the halvings).** The three involutions give the three decompositions
$$
\mathbb{B}_{\mathrm{r}}=\mathbb{C}\oplus\mathbb{C}j,\qquad \mathbb{B}_{\mathrm{r}}=\mathbb{R}\{1,j\}\oplus\mathbb{R}\{i,ij\},\qquad \mathbb{B}_{\mathrm{r}}=\mathbb{R}\{1,ij\}\oplus\mathbb{R}\{i,j\},
$$
of the natural sign, the bar and the star, each into a fixed plane and an anti-fixed plane of real dimension two.

*Proof.* This is the computation of the fixed and anti-fixed spaces of *The Two Involutions and the Group of Involutions of the Reduced Biquaternions*, regrouped by the blocks: the natural sign groups the blocks with $\varepsilon_{2}=+$ and those with $\varepsilon_{2}=-$, the bar groups by $\varepsilon_{1}$, and the star, whose eigenvalue is $\varepsilon_{1}\varepsilon_{2}$, groups by that product.

### Each Halving Is a Grading

**Each halving is a $\mathbb{Z}_{2}$-grading of the algebra, and none is a decomposition into two subalgebras.**

**Theorem (the gradings).** For each involution $\sigma$ let $\mathbb{B}_{+}$ be the fixed plane and $\mathbb{B}_{-}$ the anti-fixed plane. Then
$$
\mathbb{B}_{+}\mathbb{B}_{+}\subseteq\mathbb{B}_{+},\qquad \mathbb{B}_{+}\mathbb{B}_{-}\subseteq\mathbb{B}_{-},\qquad \mathbb{B}_{-}\mathbb{B}_{-}\subseteq\mathbb{B}_{+},
$$
so the halving is a $\mathbb{Z}_{2}$-grading; the anti-fixed plane is not closed under the product, so the halving is not a decomposition into two subalgebras.

*Proof.* Each plane is the span of two coordinate lines, and the product of two basis elements is, up to sign, a basis element whose character under $\sigma$ is the product of the two characters; the three inclusions are the three products of signs. For the non-closure it is enough to exhibit one anti-fixed product leaving the plane: for the natural sign, $(j)^{2}=1\in\mathbb{C}=\mathbb{B}_{+}$ with $j\in\mathbb{C}j=\mathbb{B}_{-}$; for the bar, $(i)^{2}=-1\in\mathbb{R}\{1,j\}=\mathbb{B}_{+}$ with $i\in\mathbb{R}\{i,ij\}$; for the star, $(i)^{2}=-1\in\mathbb{R}\{1,ij\}$ with $i\in\mathbb{R}\{i,j\}$. In each case $\mathbb{B}_{-}$ is not closed.

**Corollary (the gradings are the same three).** The $\mathbb{Z}_{2}$-grading of the natural sign is the grading $\mathbb{C}\oplus\mathbb{C}j$ of *Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions*, §*The Decomposition as a Grading*; the gradings of the bar and of the star are the other two, and the three are the three ways of writing the block decomposition as two groups of two blocks.

## The Decomposition Along the Idempotents

**The idempotent decomposition is the splitting into the two eigenlines of the multiplication by $j$, and unlike the halvings it is a decomposition of the algebra.**

**Theorem (the idempotent decomposition).** With $\Pi_{\pm}=\tfrac12(1\pm j)$,
$$
\mathbb{B}_{\mathrm{r}}=\mathbb{C}\Pi_+\oplus\mathbb{C}\Pi_-,\qquad \Pi_++\Pi_-=1,\qquad \Pi_+\Pi_-=0,\qquad \Pi_+^{2}=\Pi_+,\ \Pi_-^{2}=\Pi_-,
$$
and the two summands are the two minimal ideals, the images of the two Peirce projections of the family $\{\Pi_+,\Pi_-\}$.

*Proof.* The idempotents and their orthogonality and completeness are *Square Roots of One and the Idempotents of the Algebra of the Reduced Biquaternions*; the two lines are the minimal ideals and the Peirce images by *Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions*.

**Corollary (the diagonal and the coordinate planes).** The idempotent decomposition is the opposite of the block decomposition in a precise sense: the idempotent lines are the **diagonal** planes spanned by $\tfrac12(1+j)$ and $\tfrac12(i+ij)$ and by $\tfrac12(1-j)$ and $\tfrac12(i-ij)$, while the four blocks are the coordinate lines. The idempotent lines are therefore disjoint from the four blocks except at the origin, and the two decompositions are in general position.

## The Two Kinds of Decomposition

**The three halvings are gradings and the idempotent decomposition is a direct product; the distinction is what is closed.**

**Theorem (the two kinds).**

1. A **direct product** decomposition $\mathbb{B}_{\mathrm{r}}=\mathrm A\oplus\mathrm B$ has each summand a subalgebra, $\mathrm A^{2}\subseteq\mathrm A$, $\mathrm B^{2}\subseteq\mathrm B$, and the mixed product zero, $\mathrm A\mathrm B=0$; equivalently the projections are **algebra** homomorphisms.
2. A **grading** $\mathbb{B}_{\mathrm{r}}=\mathbb{B}_{+}\oplus\mathbb{B}_{-}$ has only the three parity inclusions of §*Each Halving Is a Grading*; the projections are not algebra homomorphisms, and the mixed product is not zero.

The idempotent decomposition is a direct product; the three halvings are gradings and not direct products.

*Proof.* For the idempotent decomposition the summands are $\mathbb{C}\Pi_+$ and $\mathbb{C}\Pi_-$, closed under the product, with $\mathbb{C}\Pi_+\cdot\mathbb{C}\Pi_-=\mathbb{C}\Pi_+\Pi_-=0$; the projections are $Q_\pm\mapsto\Pi_{i}Q_\pm$, which satisfy $\Pi_{i}(Q_{\pm,1}Q_{\pm,2})=(\Pi_{i}Q_{\pm,1})(\Pi_{i}Q_{\pm,2})$ because $\Pi_{i}^{2}=\Pi_{i}$ and $\Pi_+\Pi_-=0$, so they are algebra homomorphisms. For the halvings the anti-fixed plane is not closed by §*Each Halving Is a Grading* and the mixed product is the anti-fixed plane, which is nonzero.

**Corollary (why the idempotents are central).** The two projections of the idempotent decomposition are the algebra homomorphisms $\mathbb{B}_{\mathrm{r}}\to\mathbb{C}\Pi_{i}$ and the decomposition is the one of the direct product $\mathbb{C}\times\mathbb{C}$; the halving projections are only linear. The central idempotents are exactly the ones for which the split is a decomposition of the algebra, and this is the content of *The Specificities of the Algebra of the Reduced Biquaternions*, §*The Associative Interpretation*.

## The Projections and the Changes of Basis

**The projections of the three halvings and of the block decomposition are the averaging formulas, and the change from the real basis to the idempotent basis is the matrix of the two idempotents.**

**Theorem (the projections).** The projections onto the planes of the halvings and the blocks are
$$
P_{\mathbb{C}}=\tfrac12(\mathrm{id}+{}^{\natural}),\qquad P_{\mathbb{C}j}=\tfrac12(\mathrm{id}-{}^{\natural}),
$$
$$
P_{\mathbb{R}\{1,j\}}=\tfrac12(\mathrm{id}+\bar{\cdot}),\qquad P_{\mathbb{R}\{i,ij\}}=\tfrac12(\mathrm{id}-\bar{\cdot}),
$$
$$
P_{\mathbb{R}\{1,ij\}}=\tfrac12(\mathrm{id}+{}^{*}),\qquad P_{\mathbb{R}\{i,j\}}=\tfrac12(\mathrm{id}-{}^{*}),
$$
and the block projections are the four products
$$
P_{(\varepsilon_{1},\varepsilon_{2})}=\tfrac14(\mathrm{id}+\varepsilon_{1}\bar{\cdot})\circ(\mathrm{id}+\varepsilon_{2}{}^{\natural}).
$$

*Proof.* This is the projection formula of *Introduction to the Remarkable Subspaces*, §*The Fixed and Anti-Fixed Space of an Involution*, and the block projections are the products of the two commuting eigenspace projections for the pair $(\varepsilon_{1},\varepsilon_{2})$.

**Theorem (the change of basis).** The real basis $\{1,i,j,ij\}$ and the real basis $\{\Pi_+,i\Pi_+,\Pi_-,i\Pi_-\}$ are related by
$$
\Pi_+=\tfrac12+\tfrac12 j,\quad i\Pi_+=\tfrac12 i+\tfrac12 ij,\quad \Pi_-=\tfrac12-\tfrac12 j,\quad i\Pi_-=\tfrac12 i-\tfrac12 ij,
$$
a real change of basis of determinant $\tfrac14$, so the idempotent decomposition and the block decomposition are two bases of the same real space and the change between them is invertible.

*Proof.* The displays are the definitions and the multiplication by $i$; the determinant is computed from the matrix whose rows are the four coordinate quadruples, $\tfrac12(1,0,1,0)$, $\tfrac12(0,1,0,1)$, $\tfrac12(1,0,-1,0)$, $\tfrac12(0,1,0,-1)$, which has determinant $\tfrac14$.

## Worked Example

**A generic element in the two decompositions.** For $Q_\pm=2+i+3j+4ij$ the four blocks carry the coordinates $2,1,3,4$, and the three halvings read
$$
P_{\mathbb{C}}Q_\pm=2+i,\quad P_{\mathbb{C}j}Q_\pm=3j+4ij,\qquad P_{\mathbb{R}\{1,j\}}Q_\pm=2+3j,\quad P_{\mathbb{R}\{i,ij\}}Q_\pm=i+4ij,
$$
$$
P_{\mathbb{R}\{1,ij\}}Q_\pm=2+4ij,\quad P_{\mathbb{R}\{i,j\}}Q_\pm=i+3j,
$$
while the idempotent decomposition reads
$$
Q_{++}=Q_++Q_-=(2+i)+(3+4i)=5+5i,\qquad Q_{--}=Q_+-Q_-=(2+i)-(3+4i)=-1-3i,
$$
so $Q_\pm=(5+5i)\Pi_++(-1-3i)\Pi_-$. The element is a unit because $Q_{++}$ and $Q_{--}$ are nonzero, and the two decompositions display it as four real coordinates and as two complex idempotent coordinates respectively.

## Summary

The reduced biquaternion space decomposes in three ways along its remarkable subspaces. The bar and the natural sign are commuting involutions, and their **block decomposition** splits the real space into the four common eigenlines $\mathbb{R}\oplus\mathbb{R}i\oplus\mathbb{R}j\oplus\mathbb{R}ij$, labelled by the two signs $(\varepsilon_{\bar{}},\varepsilon_{\natural})$ with the star reading the product sign. Each involution gives a **halving** into its fixed and anti-fixed plane — the natural sign giving $\mathbb{C}\oplus\mathbb{C}j$, the bar giving $\mathbb{R}\{1,j\}\oplus\mathbb{R}\{i,ij\}$ and the star giving $\mathbb{R}\{1,ij\}\oplus\mathbb{R}\{i,j\}$ — and each halving is the grouping of the four blocks two by two. The **idempotent decomposition** splits the algebra into the two eigenlines of the multiplication by $j$, $\mathbb{C}\Pi_+\oplus\mathbb{C}\Pi_-$, and it is a decomposition of the algebra and not only of the space. The distinction is what is closed under the product: each halving is a $\mathbb{Z}_{2}$-grading, with the anti-fixed plane not a subalgebra, whereas the idempotent decomposition is a direct product, with each summand a minimal ideal and the mixed product zero, and its two projections are the algebra homomorphisms onto the two factors of $\mathbb{C}\times\mathbb{C}$. The projections of the halvings and of the blocks are the averaging formulas built on the involutions, $\tfrac12(\mathrm{id}\pm\sigma)$ and $\tfrac14(\mathrm{id}\pm\bar{\cdot})(\mathrm{id}\pm{}^{\natural})$, and the change between the real basis and the idempotent basis is the invertible real matrix of the two idempotents.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}_{(\varepsilon_{1},\varepsilon_{2})}$ | a block, the common eigenspace of $(\bar{\cdot},{}^{\natural})$ with those signs |
| $\mathbb{R},\mathbb{R}i,\mathbb{R}j,\mathbb{R}ij$ | the four blocks |
| $\mathbb{C}\oplus\mathbb{C}j$ | the halving of the natural sign, the grading |
| $\mathbb{R}\{1,j\}\oplus\mathbb{R}\{i,ij\}$ | the halving of the bar |
| $\mathbb{R}\{1,ij\}\oplus\mathbb{R}\{i,j\}$ | the halving of the star |
| $\mathbb{C}\Pi_+\oplus\mathbb{C}\Pi_-$ | the idempotent decomposition, a direct product of ideals |
| $P_{(\varepsilon_{1},\varepsilon_{2})}=\tfrac14(\mathrm{id}+\varepsilon_{1}\bar{\cdot})(\mathrm{id}+\varepsilon_{2}{}^{\natural})$ | the block projection |
| $\{1,i,j,ij\}\leftrightarrow\{\Pi_+,i\Pi_+,\Pi_-,i\Pi_-\}$ | the change of basis |

## Further Reading

- *Introduction to the Remarkable Subspaces* (`articles_maths/introduction-to-the-remarkable-subspaces-of-the-reduced-biquaternions.md`), for the spaces and their characters.
- *The Two Involutions and the Group of Involutions of the Reduced Biquaternions* (`articles_maths/the-two-involutions-and-the-group-of-involutions-of-the-reduced-biquaternions.md`), for the involutions, their commutativity and their fixed spaces.
- *Square Roots of One and the Idempotents of the Algebra of the Reduced Biquaternions* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the idempotents and the two lines.
- *Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions* (`articles_maths/ideals-and-peirce-decomposition-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the Peirce decomposition and the $\mathbb{Z}_{2}$-grading.
- *Comparison of the Remarkable Subspaces* (`articles_maths/comparison-of-the-remarkable-subspaces-of-the-reduced-biquaternions.md`), for the spaces at a glance and their closure.
- *Decompositions Along the Remarkable Subspaces* (`articles_maths/decompositions-along-the-remarkable-subspaces.md`), for the non-commutative companion.
