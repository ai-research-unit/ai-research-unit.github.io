# __Remarkable Subspaces and the Two Products of the Split-Complexoid Space__

## Introduction

The split-complex algebra $\mathbb{D}=\mathbb{R}[x]/(x^2-1)$ carries two products, the **general plain bilinear product** $AC$ and the **general plain sesquilinear product** $A\overline{C}$, and its distinguished subspaces are four real lines: the real line $\mathbb{R}_{\mathbb{D}}$, the split imaginary line $j\mathbb{R}_{\mathbb{D}}$, and the two idempotent lines $\mathbb{R}\Pi_1$ and $\mathbb{R}\Pi_2$. This article reads the two products on those four lines, one line to a section, and answers for each the same questions: **is the line closed under the product**, **which of its elements are units**, **which are zero divisors**, and **what role the line plays in the ring**.

The products themselves, their laws and their coordinate forms are *The Two Products of the Split-Complex Space*; the four lines, their bases, their dimensions and their restricted norm are *Split-Complex Subspaces*; the two forms the products carry are *The Two Forms and the Two Algebraic Norms of the Split-Complex Space*, below this article in this category; and the norm, the criterion of invertibility, the units, the idempotents and the zero divisors of the algebra are *Split-Complex Norm and Invertibility*, *Split-Complex Idempotents and Projections* and *Split-Complex Zero Divisors*, all below this article in this category. None of those is restated here. What the article adds is the reading of the two products on the four lines and nothing else. The twelve structures, read on $\mathbb{D}$ and collapsed to the two, are *The Collapse of the Twelve Structures on the Split-Complex Numbers*, below this article in this category.

**The reading fixed here.** In the global convention of *Conventions in Mathematics* the conjugation $j\mapsto-j$ is the **bar**, and the Hermitian conjugation ${}^{*}$ coincides with it. The bar is the unique non-trivial involution of $\mathbb{D}$; the split-complex block also calls it "the involution", and the wording is reconciled once here and not repeated. It fixes $\mathbb{R}_{\mathbb{D}}$, negates $j\mathbb{R}_{\mathbb{D}}$, and exchanges the two idempotent lines. In this article $A=a+ja'$ and $C=c+jc'$ are elements, so that the letters $B$, $H$ and $N$ stay free for the forms, which is the convention of *The Two Forms and the Two Algebraic Norms of the Split-Complex Space*, below this article in this category. The idempotents are written $\Pi_{1,2}=\tfrac12(1\pm j)$; the menu of this category writes them $e_\pm$, and the two notations name the same pair.

On the coordinates the two products are

$$
AC=(ac+a'c')+(ac'+a'c)j,
\qquad
A\overline{C}=(ac-a'c')+(a'c-ac')j,
$$

so the bilinear product is the multiplication of the ring and the sesquilinear product is its reflection in the second slot, as in *The Two Products of the Split-Complex Space*.

## The Closure of the Four Lines

A line is **closed** under a product when the product of two of its elements lies in it again. The four lines answer differently, and the answer is the whole of their relation to the ring.

**Proposition.** The real line and the two idempotent lines are closed under both products; the split imaginary line is closed under neither, and the product of two of its elements lies in the real line for both products.

**Proof.** On $\mathbb{R}_{\mathbb{D}}$, write $A=a$ and $C=c$ with $a',c'=0$; then $AC=ac$ and $A\overline{C}=ac$, both real, so the line is closed under both. On $j\mathbb{R}_{\mathbb{D}}$, write $A=ja'$, $C=jc'$; then $AC=j^2a'c'=a'c'\in\mathbb{R}_{\mathbb{D}}$ and $A\overline{C}=ja'\overline{jc'}=ja'(-jc')=-j^2a'c'=-a'c'\in\mathbb{R}_{\mathbb{D}}$, so the line is closed under neither and each product sends it into the real line. On $\mathbb{R}\Pi_1$, write $A=\lambda\Pi_1$, $C=\mu\Pi_1$; then $AC=\lambda\mu\Pi_1^2=\lambda\mu\Pi_1$, and $A\overline{C}=\lambda\Pi_1\overline{\mu\Pi_1}=\lambda\mu\Pi_1\Pi_2=0$, both in the line; the same computation holds on $\mathbb{R}\Pi_2$ with the two idempotents exchanged.

The asymmetry between the two eigenlines has one cause: $j$, the generator of the anti-fixed line, squares to $+1$ rather than to $-1$, so the product of two elements of $j\mathbb{R}_{\mathbb{D}}$ cancels the sign change and lands on the fixed line. In the complex field the same computation gives $(ia')(ic')=-a'c'$, again in the fixed line; the two cases agree that an anti-fixed line is not a subring, and differ in the sign, which is the split sign. The real line is thus the only subring among the two eigenlines, and $\mathbb{R}_{\mathbb{D}}\cong\mathbb{R}$ as a ring.

## The Two Products on the Idempotent Lines

The idempotent lines are closed under both products, and this is stronger than the closure of the real line: it is closure under multiplication by an arbitrary element of the algebra, on both sides.

**Proposition.** The lines $\mathbb{R}\Pi_1$ and $\mathbb{R}\Pi_2$ are the two minimal ideals of $\mathbb{D}$ for the bilinear product; for every $A$ in $\mathbb{R}\Pi_1$ and every $C$ in $\mathbb{D}$, both $AC$ and $A\overline{C}$ lie in $\mathbb{R}\Pi_1$, and the same on $\mathbb{R}\Pi_2$.

**Proof.** Since $\Pi_1$ is central and $\Pi_1^2=\Pi_1$, one has $(\lambda\Pi_1)C=\lambda C\Pi_1=\lambda(c+c')\Pi_1\in\mathbb{R}\Pi_1$, so $\mathbb{R}\Pi_1$ is an ideal; and $\overline{C}=C_-\Pi_1+C_+\Pi_2$ has $C_-=c-c'$, so that $\Pi_1\overline{C}=C_-\Pi_1$ and $(\lambda\Pi_1)\overline{C}=\lambda C_-\Pi_1\in\mathbb{R}\Pi_1$. The case of $\Pi_2$ is the same with the roles exchanged. Minimality and the direct decomposition $\mathbb{D}=\mathbb{R}\Pi_1\oplus\mathbb{R}\Pi_2$ are the content of *Split-Complex Idempotents and Projections*, below this article in this category, and they show that the two lines are the finest pieces of the algebra.

So the two idempotent lines are the two minimal ideals of the ring, and each is a field in its own right, isomorphic to $\mathbb{R}$ with the unit $\Pi_i$. Because the algebra is commutative, a left ideal, a right ideal and a two-sided ideal are the same object, so there is no distinction between the two sides and the two lines are the only non-zero proper ideals. On each line the bilinear product is the multiplication of that copy of $\mathbb{R}$, while the sesquilinear product carries the line into itself through the conjugate coordinate $C_-$.

## The Units and the Zero Divisors of Each Line

The algebra splits into the units $N\neq0$ and the non-units $N=0$, the latter being the null cone: the origin together with the zero divisors, which are the non-zero elements supported on a single idempotent (*Split-Complex Norm and Invertibility*; *Split-Complex Zero Divisors*, both below this article in this category). Read on the four lines, this classification is what separates the two eigenlines from the two idempotent lines.

| line | basis | closed under $AC$? | closed under $A\overline{C}$? | units | zero divisors |
|---|---|---|---|---|---|
| $\mathbb{R}_{\mathbb{D}}$ | $1$ | yes | yes | all non-zero | none |
| $j\mathbb{R}_{\mathbb{D}}$ | $j$ | no | no | all non-zero | none |
| $\mathbb{R}\Pi_1$ | $\Pi_1$ | yes | yes | none | all non-zero |
| $\mathbb{R}\Pi_2$ | $\Pi_2$ | yes | yes | none | all non-zero |

The two eigenlines lie entirely in the set of the units: their norm is $N(a)=a^2$ on $\mathbb{R}_{\mathbb{D}}$ and $N(ja')=-a'^2$ on $j\mathbb{R}_{\mathbb{D}}$, both non-zero away from the origin, so every non-zero element of either line is a unit and no element of either line is a zero divisor. The two idempotent lines lie entirely in the complement: their norm is $N(\lambda\Pi_i)=\lambda^2 N(\Pi_i)=0$, so every non-zero element of either line is a zero divisor and none of them is a unit, while $0$ is neither. The classification of the elements by the vanishing of the norm therefore separates the four lines into two units-lines, which are the two eigenlines, and two zero-divisor-lines, which are the two idempotent lines.

**Remark.** The bilinear product of two elements of $j\mathbb{R}_{\mathbb{D}}$ and the sesquilinear product of two of its elements are both real, and they differ by the sign: $AC=a'c'$ and $A\overline{C}=-a'c'$. So the split imaginary line is carried into the real line by each product, and the two images are mirror images of one another. This is the line-level form of the statement that the two products agree on $\mathbb{R}_{\mathbb{D}}$ and differ by a sign on the anti-fixed direction; the form reading is *Remarkable Subspaces of the Split-Complex Numbers and the Two Forms*, below this article in this category.

## Summary

The two products $AC$ and $A\overline{C}$ of the split-complex algebra read on its four distinguished lines. The real line $\mathbb{R}_{\mathbb{D}}$ is closed under both products and is the subring of the fixed points of the conjugation, where the two products agree; the split imaginary line $j\mathbb{R}_{\mathbb{D}}$ is closed under neither, and each product sends it into the real line, the two images differing by the sign because $j^2=+1$; the two idempotent lines $\mathbb{R}\Pi_1$ and $\mathbb{R}\Pi_2$ are closed under both products and are the two minimal ideals of the ring, the finest pieces of the idempotent decomposition.

The classification of the elements by the norm separates the lines: every non-zero element of either eigenline is a unit and no element of either is a zero divisor, while every non-zero element of either idempotent line is a zero divisor and none of them is a unit. This is the line-level form of the split of the algebra into the units and the null cone, the null cone being the two idempotent lines. The discussion reduces to the two eigenlines and the two idempotent lines, because $\mathbb{D}$ has one non-trivial involution instead of three and, in addition, has two non-trivial idempotents, which the complex field does not.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}=\mathbb{R}[x]/(x^2-1)$ | split-complex algebra, basis $1,j$, $j^2=+1$ |
| $A=a+ja'$, $C=c+jc'$ | elements of $\mathbb{D}$ |
| $\bar{A}=a-ja'$ | the bar: the unique non-trivial involution |
| $\Pi_{1,2}=\tfrac12(1\pm j)$ | the two standard idempotents (menu: $e_\pm$) |
| $\mathbb{R}_{\mathbb{D}}$, $j\mathbb{R}_{\mathbb{D}}$ | the fixed and anti-fixed lines of the bar |
| $\mathbb{R}\Pi_1$, $\mathbb{R}\Pi_2$ | the two idempotent lines, the two minimal ideals |
| $AC$, $A\overline{C}$ | the general plain bilinear and sesquilinear products |
| $N(A)=A\bar{A}=a^2-a'^2$ | the norm, owned by *Split-Complex Norm and Invertibility* |

## Further Reading

- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the scalar–vector and idempotent decompositions and the reading of the products on the lines.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the split-complex algebra as the even Clifford algebra $\mathrm{Cl}_{1,0}$ and its isotropic lines.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, Graduate Texts in Mathematics 131, 2nd ed. 2001), for ideals, minimal ideals and the classification of the elements of a commutative ring by its units.
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for the decomposition of an algebra by its idempotents.
