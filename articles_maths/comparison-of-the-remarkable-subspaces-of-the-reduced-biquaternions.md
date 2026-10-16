# __Comparison of the Remarkable Subspaces__

## Introduction

This article puts the remarkable subspaces of the reduced biquaternion algebra side by side. The eight planes of real dimension two — the six coordinate planes of the involutions and the two idempotent lines — are listed with their defining equations, their bases, their dimensions, their norm type and their **closure** under the multiplication, and the comparison shows the three regularities of the list: the closed planes are exactly the fixed spaces of the three involutions, the idempotent lines alone are the ideals, and the invariance under the involutions is the one property all eight share. The article is the reference of the section: it collects in tables the statements proved in *Introduction to the Remarkable Subspaces* and *Decompositions Along the Remarkable Subspaces*, and it places the reduced biquaternion list beside the biquaternion one.

**The results.** The eight spaces are

$$
\mathbb{C},\quad \mathbb{C}j,\quad \mathbb{R}\{1,j\},\quad \mathbb{R}\{i,ij\},\quad \mathbb{R}\{1,ij\},\quad \mathbb{R}\{i,j\},\quad \mathbb{C}\Pi_{1},\quad \mathbb{C}\Pi_{2},
$$

and the comparison is summarised by three statements. **The subalgebras among the coordinate planes are the three fixed planes** $\mathbb{C}=\mathbb{R}\{1,i\}$, $\mathbb{R}\{1,j\}$ and $\mathbb{R}\{1,ij\}$; the three anti-fixed planes $\mathbb{C}j$, $\mathbb{R}\{i,ij\}$, $\mathbb{R}\{i,j\}$ are not closed, because each contains a basis element whose square leaves it. **The ideals are the two idempotent lines alone**, the minimal ideals $\mathbb{C}\Pi_{1}$ and $\mathbb{C}\Pi_{2}$, which are also the two simple modules; no coordinate plane is an ideal, since none is stable under the whole algebra except the whole space. **All eight planes are permuted by the three involutions**, each involution fixing or exchanging them, and this invariance is the reason the space decomposes along them. Among the subalgebras, $\mathbb{C}$, $\mathbb{R}\{1,ij\}$, $\mathbb{C}\Pi_{1}$ and $\mathbb{C}\Pi_{2}$ are copies of the complex field — four copies, with the imaginary units $i$, $ij$, $i\Pi_{1}$ and $i\Pi_{2}$ respectively — and $\mathbb{R}\{1,j\}$ is a copy of the split-complex numbers.

**Boundaries.** The spaces, their characters and their norms are *Introduction to the Remarkable Subspaces*; the decompositions are *Decompositions Along the Remarkable Subspaces*; the involutions are *The Two Involutions and the Group of Involutions of the Reduced Biquaternions*; the idempotents and the ideals are *Square Roots of One and the Idempotents of the General Plain Algebra of the Reduced Biquaternions* and *Ideals and Peirce Decomposition of the General Plain Algebra of the Reduced Biquaternions*. The forms restricted to the planes are *Remarkable Subspaces and the Four Forms of the Reduced Biquaternions* and the norms *Remarkable Subspaces and the Four Algebraic Norms of the Reduced Biquaternions*, of the later subsections of this category. The biquaternion counterpart is *Comparison of the Remarkable Subspaces* of the biquaternion category.

## The Table of the Spaces

**The eight spaces, with their defining equation, their basis, their real dimension and the type of their norm, are the following.**

| space | defining equation | basis | real dim | $\mathbb{C}$-linear | norm $\langle\cdot\rangle$ |
|---|---|---|---|---|---|
| $\mathbb{C}$ | $T^{\natural}=T$ | $1,\ i$ | $2$ | yes | $A^{2}$, complex |
| $\mathbb{C}j$ | $T^{\natural}=-T$ | $j,\ ij$ | $2$ | yes | $-B^{2}$, complex |
| $\mathbb{R}\{1,j\}$ | $\bar T=T$ | $1,\ j$ | $2$ | no | $a^{2}-b^{2}$, split |
| $\mathbb{R}\{i,ij\}$ | $\bar T=-T$ | $i,\ ij$ | $2$ | no | $-(a^{2}-b^{2})$, split |
| $\mathbb{R}\{1,ij\}$ | $T^{*}=T$ | $1,\ ij$ | $2$ | no | $a^{2}+b^{2}$, positive definite |
| $\mathbb{R}\{i,j\}$ | $T^{*}=-T$ | $i,\ j$ | $2$ | no | $-(a^{2}+b^{2})$, negative definite |
| $\mathbb{C}\Pi_{1}$ | $jT=T$ | $\Pi_{1},\ i\Pi_{1}$ | $2$ | yes | $0$ |
| $\mathbb{C}\Pi_{2}$ | $jT=-T$ | $\Pi_{2},\ i\Pi_{2}$ | $2$ | yes | $0$ |

The four complex lines $\mathbb{C}$, $\mathbb{C}j$, $\mathbb{C}\Pi_{1}$, $\mathbb{C}\Pi_{2}$ are one-dimensional over $\mathbb{C}$; the four real planes $\mathbb{R}\{1,j\}$, $\mathbb{R}\{i,ij\}$, $\mathbb{R}\{1,ij\}$, $\mathbb{R}\{i,j\}$ have no complex structure of their own, and the multiplication by $i$ permutes them in pairs, $\mathbb{R}\{1,j\}\leftrightarrow\mathbb{R}\{i,ij\}$ and $\mathbb{R}\{1,ij\}\leftrightarrow\mathbb{R}\{i,j\}$. The two idempotent lines are the null set of the norm, and their nonzero elements are the zero divisors.

*Proof.* The defining equations are the fixed and anti-fixed conditions of *The Two Involutions and the Group of Involutions of the Reduced Biquaternions* and the eigenconditions of the multiplication by $j$; the bases and dimensions are those of *Introduction to the Remarkable Subspaces*; the norms are the table of §*The Norm on the Spaces* of that article.

## The Subalgebras and the Non-Closed Planes

**A coordinate plane is closed under the multiplication exactly when it is the fixed plane of one of the three involutions, and then it is a subalgebra.**

**Theorem (the closure).** Among the eight spaces:

- $\mathbb{C}$, $\mathbb{R}\{1,j\}$, $\mathbb{R}\{1,ij\}$ are **subalgebras**, closed under the multiplication;
- $\mathbb{C}j$, $\mathbb{R}\{i,ij\}$, $\mathbb{R}\{i,j\}$ are **not** closed;
- $\mathbb{C}\Pi_{1}$, $\mathbb{C}\Pi_{2}$ are subalgebras, and in fact ideals.

*Proof.* For a plane spanned by two basis elements it suffices to check the products of the basis elements. For $\mathbb{C}=\mathbb{R}\{1,i\}$: $1\cdot1=1$, $1\cdot i=i$ and $i\cdot i=-1$ lie in the plane. For $\mathbb{R}\{1,j\}$: $j\cdot j=1$. For $\mathbb{R}\{1,ij\}$: $(ij)^{2}=-1$. For $\mathbb{C}j=\mathbb{R}\{j,ij\}$: $j\cdot ij=j^{2}i=i\notin\mathbb{C}j$, so it is not closed. For $\mathbb{R}\{i,ij\}$: $i\cdot ij=i^{2}j=-j\notin$ the plane. For $\mathbb{R}\{i,j\}$: $i\cdot j=ij\notin$ the plane. The idempotent lines are the principal ideals $\mathbb{C}\Pi_{i}=\mathbb{B}_{\mathrm{r}}\Pi_{i}$, hence closed, by *Ideals and Peirce Decomposition of the General Plain Algebra of the Reduced Biquaternions*.

**Corollary (the criterion).** The three closed coordinate planes are the fixed spaces of the three involutions, and the three non-closed ones are the anti-fixed spaces. In a fixed plane every basis element has square in the plane; in an anti-fixed plane the square of a basis element may leave it. The three subalgebras are also the realifiable ones in the sense of the two scalar systems.

**Corollary (the shapes of the subalgebras).** The three coordinate subalgebras and the two idempotent lines are
$$
\mathbb{C}\cong\mathbb{C},\qquad \mathbb{R}\{1,j\}\cong\mathbb{R}[j]/(j^{2}-1)\cong\mathbb{R}\times\mathbb{R},\qquad \mathbb{R}\{1,ij\}\cong\mathbb{C},
$$
$$
\mathbb{C}\Pi_{1}\cong\mathbb{C},\qquad \mathbb{C}\Pi_{2}\cong\mathbb{C},
$$
so the algebra contains **four copies of the complex field** — the scalar line, the Hermitian subspace and the two idempotent lines — and one copy of the split-complex numbers, the real subalgebra.

## The Ideals and the Lattice

**The only ideals among the planes are the two idempotent lines, and they are the two minimal ideals of the algebra.**

**Theorem (the ideals).** The subspaces of the list that are ideals of the algebra are exactly $\mathbb{C}\Pi_{1}$ and $\mathbb{C}\Pi_{2}$, and they are the two minimal ideals, the two simple modules and the two summands of the direct-product decomposition.

*Proof.* The ideal lattice is $0\subsetneq\mathbb{C}\Pi_{1},\mathbb{C}\Pi_{2}\subsetneq\mathbb{B}_{\mathrm{r}}$ by *Ideals and Peirce Decomposition of the General Plain Algebra of the Reduced Biquaternions*; the coordinate planes are not ideals: an ideal is stable under the multiplication by every element, and each coordinate plane is moved by one — the multiplication by $j$ moves $\mathbb{C}$, $\mathbb{C}j$, $\mathbb{R}\{1,ij\}$ and $\mathbb{R}\{i,j\}$ ($j\cdot1=j$, $j\cdot j=1$, $j\cdot i=ij$), and the multiplication by $i$ moves $\mathbb{R}\{1,j\}$ and $\mathbb{R}\{i,ij\}$ ($i\cdot1=i$, $i\cdot i=-1$) — while stability under the whole algebra holds only for the two idempotent lines and their sums, by the ideal theorem.

**Corollary (the character of the section).** The section's two kinds of plane therefore divide the work: the coordinate planes carry the decompositions into gradings and the invariance under the involutions, and the idempotent lines carry the algebra decomposition into the two ideals. No plane belongs to both kinds: a coordinate plane is never an ideal, and an idempotent line is never a coordinate plane.

## Stability under the Involutions

**The three involutions permute the eight planes, fixing or exchanging them.**

**Theorem (the stability).** Each of the three involutions permutes the eight spaces: it maps each of the six coordinate planes onto itself, and it fixes each idempotent line for the bar and exchanges the two lines for the natural sign and the star; on the coordinate planes the involution is the reflection of the fixed or the anti-fixed character.

*Proof.* A coordinate plane spanned by two basis elements is stable because each involution sends a basis element to $\pm$ that element. The bar fixes $\Pi_{1}$ and $\Pi_{2}$, while ${}^{\natural}$ and ${}^{*}$ exchange them, by *Square Roots of One and the Idempotents of the General Plain Algebra of the Reduced Biquaternions*; since the line $\mathbb{C}\Pi_{i}$ is the complex span of $\Pi_{i}$, the exchange of the idempotents exchanges the lines and the bar fixes each.

**Corollary (why the section exists).** The permutation is the reason the algebra has three splittings: a plane stable under an involution gives a decomposition only when the involution acts on it by a single sign, that is when it is a fixed or an anti-fixed plane. The idempotent lines are permuted but are not eigenspaces of the natural sign or the star (they are eigenspaces of the bar), and this is why the idempotent decomposition is of a different kind from the halvings.

## The Dimensions and the Lattice of the Spaces

**The eight planes are all of real dimension two and complex dimension one; their incidence lattice is the one of the four real lines.**

**Theorem (the incidence).** Each space has real dimension two and is a complex line or a real plane; the four real lines $\mathbb{R}$, $\mathbb{R}i$, $\mathbb{R}j$, $\mathbb{R}ij$ are the atoms, every coordinate plane is the sum of two atoms, and there are exactly three complementary pairs of coordinate planes, the three halvings of *Decompositions Along the Remarkable Subspaces*. The idempotent lines are not sums of atoms.

*Proof.* The atoms are the common eigenspaces of the two involutions, of real dimension one, and the coordinate planes are spanned by pairs of them, by §*The Character of Each Space* of *Introduction to the Remarkable Subspaces*. A plane is the sum of two atoms when it is a coordinate plane; the idempotent lines have basis $\Pi_{i},i\Pi_{i}$ with $\Pi_{i}$ not an atom, since it is not an eigenvector of the bar with a single sign pair... rather $\Pi_{1}$ is bar-fixed and natural-negated, so it is a complex combination of atoms with mixed signs, not a real combination of a single atom and its $i$-multiple.

## Comparison with the Biquaternion Counterparts

**The reduced biquaternion list is the biquaternion list collapsed by the commutativity, and the closure pattern is the visible difference.**

In the biquaternion category the remarkable subspaces are also the fixed and anti-fixed spaces of the involutions and the idempotent lines, but the algebra is not commutative, the vector subspace has real dimension three, and the fixed spaces of the two involutions are richer: the natural sign fixes only the scalar line, the bar fixes a four-dimensional split-quaternion subspace, and the star fixes a real plane of the Hermitian elements. In the reduced biquaternion case the two involutions are two generators of $\mathbb{Z}_{2}\times\mathbb{Z}_{2}$ acting on a four-dimensional space, so their fixed spaces are two-dimensional planes, and the three involutions with their three fixed planes exhaust the list. The closure comparison is the sharp one: the biquaternion has the same subalgebra and ideal structure on fewer spaces, and the reduced biquaternion shows the closure of a coordinate plane as a purely combinatorial fact about the signs of its two basis elements, read from the character table. The comparison is *Comparison of the Remarkable Subspaces* of the biquaternion category.

## Summary

The eight remarkable subspaces of the reduced biquaternion algebra are the six coordinate planes $\mathbb{C}$, $\mathbb{C}j$, $\mathbb{R}\{1,j\}$, $\mathbb{R}\{i,ij\}$, $\mathbb{R}\{1,ij\}$, $\mathbb{R}\{i,j\}$ and the two idempotent lines $\mathbb{C}\Pi_{1}$, $\mathbb{C}\Pi_{2}$, all of real dimension two. They are listed with their defining equations, bases, dimensions, complex-linearity character and norm type; the norm is positive definite on the Hermitian plane, negative definite on the anti-Hermitian plane, split on the real subalgebra and its $i$-multiple, complex on the two complex lines, and zero on the idempotent lines. Under the multiplication, the subalgebras among the coordinate planes are exactly the three **fixed** planes $\mathbb{C}$, $\mathbb{R}\{1,j\}$, $\mathbb{R}\{1,ij\}$, while the three **anti-fixed** planes $\mathbb{C}j$, $\mathbb{R}\{i,ij\}$, $\mathbb{R}\{i,j\}$ are not closed, each containing a basis element whose square leaves it; the four coordinate subalgebras and lines comprise four copies of $\mathbb{C}$ and one copy of the split-complex numbers. The only ideals among the eight are the two idempotent lines, the two minimal ideals and simple modules, and no coordinate plane is an ideal; no plane is both a coordinate plane and an idempotent line. All eight planes are permuted by the three involutions, which fix or exchange them, and that invariance is why the space has the three halvings and the block decomposition; the idempotent lines are permuted but are not eigenspaces of the natural sign or the star, which is why the idempotent decomposition is a direct product and not a grading. The list is the commutativity-collapsed image of the biquaternion list.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{C}=\mathbb{R}\{1,i\}$ | scalar line, fixed space of the natural sign, subalgebra $\cong\mathbb{C}$ |
| $\mathbb{C}j=\mathbb{R}\{j,ij\}$ | $j$-line, anti-fixed space of the natural sign, not closed |
| $\mathbb{R}\{1,j\}$ | real subalgebra, fixed space of the bar, $\cong\mathbb{R}\times\mathbb{R}$ |
| $\mathbb{R}\{i,ij\}$ | anti-fixed space of the bar, not closed |
| $\mathbb{R}\{1,ij\}$ | Hermitian subspace, fixed space of the star, subalgebra $\cong\mathbb{C}$ |
| $\mathbb{R}\{i,j\}$ | anti-Hermitian subspace, anti-fixed space of the star, not closed |
| $\mathbb{C}\Pi_{1},\ \mathbb{C}\Pi_{2}$ | idempotent lines, the two minimal ideals and simple modules |
| closure | the property of being a subalgebra of the multiplication |
| $\mathbb{R},\mathbb{R}i,\mathbb{R}j,\mathbb{R}ij$ | the four atoms, the common eigenspaces of the bar and the natural sign |

## Further Reading

- *Introduction to the Remarkable Subspaces* (`articles_maths/introduction-to-the-remarkable-subspaces-of-the-reduced-biquaternions.md`), for the defining equations, bases and norms.
- *Decompositions Along the Remarkable Subspaces* (`articles_maths/decompositions-along-the-remarkable-subspaces-of-the-reduced-biquaternions.md`), for the block decomposition, the halvings and the idempotent decomposition.
- *The Two Involutions and the Group of Involutions of the Reduced Biquaternions* (`articles_maths/the-two-involutions-and-the-group-of-involutions-of-the-reduced-biquaternions.md`), for the fixed and anti-fixed spaces.
- *Ideals and Peirce Decomposition of the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/ideals-and-peirce-decomposition-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the two minimal ideals and the Peirce decomposition.
- *Square Roots of One and the Idempotents of the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the idempotents and the two lines.
- *Comparison of the Remarkable Subspaces* (`articles_maths/comparison-of-the-remarkable-subspaces.md`), for the non-commutative companion.
