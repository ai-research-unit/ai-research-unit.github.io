# __The Two Products of the Split-Complex Space__

## Introduction

This article defines the **two products** carried by the split-complex space — the **general plain bilinear product** $AC$ and the **general plain sesquilinear product** $A\overline{C}$ — reads them on the coordinates, states the two structures they define, and isolates the one point that tells this pair of products from the pair carried by the complex field. The first is the multiplication of the algebra and makes $\mathbb{D}$ a commutative ring; the second is the product with the second slot conjugated and makes $\mathbb{D}$ a **sesqualgebra** over the algebra with involution $(\mathbb{D},\bar{\cdot})$. The four general products of the biquaternion space collapse to these two, and the collapse is the whole operational content of the split-complex chapter: two operations and two structures where the four-dimensional algebra carries four and twelve.

The two products are defined and their structures asserted here. The **arithmetic of the collapse**, the dictionary of the twelve codes and the count of the surviving structures are *The Collapse of the Twelve Structures on the Split-Complex Numbers*; the associator of the sesquilinear product, its ternary product, its left and right multiplications, its sandwich and its commutator are *The Sesquilinear Product of the Split-Complex Space*, both below this article in this category. The forms and the norms the two products define are *The Two Forms and the Two Algebraic Norms of the Split-Complex Space*, and the products read on the distinguished subspaces are *Remarkable Subspaces and the Two Products of the Split-Complex Space*. The ring multiplication alone, with its zero divisors, its idempotents and its ideals, is *Split-Complex Algebra* and its companions. The **four general products** which collapse here are defined in *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, and their reading on the split space is the subject of this article.

**Conventions.** The algebra is $\mathbb{D}=\mathbb{R}[x]/(x^2-1)$, basis $1,j$, $j^2=+1$; a general element is $A=a+ja'$; the conjugate is $\bar A=a-ja'$; the idempotents are $\Pi_{1,2}=\tfrac12(1\pm j)$, with $A=A_+\Pi_1+A_-\Pi_2$ and $A_\pm=a\pm a'$. The natural sign is the identity and the Hermitian conjugation coincides with the bar. In this article $A=a+ja'$ and $C=c+jc'$ name elements, and the letters $B$, $H$, $N$ are kept for the forms and norms of *The Two Forms and the Two Algebraic Norms of the Split-Complex Space*.

## The Two Products

**Definition.** The **general plain bilinear product** and the **general plain sesquilinear product** of the elements $A=a+ja'$ and $C=c+jc'$ are

$$
AC = (ac+a'c') + (ac'+a'c)\,j, \qquad A\overline{C} = (ac-a'c') + (a'c-ac')\,j .
$$

The two products are defined on the same coordinates and take their values in the same plane; the first is the product of the algebra, the second differs from it by the conjugation of the second slot. They are the two **general plain** products of the four products of the four-dimensional algebra, kept for the plain family and the plain sesquilinear one.

**Proposition (the two products are separated by the second slot).** The product $AC$ is bilinear over $\mathbb{D}$, in both slots. The product $A\overline{C}$ is linear in the first slot and conjugate-linear in the second,

$$
A\overline{\lambda C} = \bar\lambda\,A\overline{C}, \qquad \lambda \in \mathbb{D},
$$

and the two products coincide exactly when the second factor is real or the first factor is zero.

**Proof.** Bilinearity of $AC$ is the distributivity of the algebra. For $A\overline{C}$, linearity in $A$ is clear from the coordinates; in the second slot, $A\overline{\lambda C}=A\,\bar\lambda\,\overline{C}=\bar\lambda\,A\overline{C}$, so the slot is conjugate-linear. The difference is

$$
AC - A\overline{C} = 2c'(a'+aj),
$$

which vanishes if and only if $c'=0$, that is $C\in\mathbb{R}$, or $A=0$.

So the two products differ by the conjugate-linearity in the second slot, and they agree on every pair whose second factor is real. On the pair $A=C=j$ they disagree as much as possible on the second coordinate, $AC=j^2=1$ against $A\overline{C}=j(-j)=-1$; the sign is the split sign $j^2=+1$, and it is the whole of the difference between the two products beyond the conjugation.

## The Ring Product $AC$

**Theorem (the commutative ring).** Under the product $AC$ the plane $\mathbb{D}$ is a commutative, associative ring with the two-sided unit $1$, and $\mathbb{D}$ is the algebra $\mathbb{R}[x]/(x^2-1)$.

**Proof.** Commutativity is the symmetry of the coordinate formulas, $ac+a'c'=ca+c'a$ and $ac'+a'c=ca'+c'a$; associativity is the associativity of the polynomial algebra $\mathbb{R}[x]/(x^2-1)$, or equally the identity $A(CD)=(AC)D$ checked on the three coordinates; and $1\cdot A=A\cdot 1=A$. The ring is the algebra, by definition of the multiplication of $\mathbb{D}$.

The product $AC$ is the **algorithmic product** of the algebra: the bilinear, commutative, associative operation with unit, and in the codes of *The Collapse of the Twelve Structures on the Split-Complex Numbers* it is the common value of the four codes $\mathrm{GPA}=\mathrm{SPA}=\mathrm{GQA}=\mathrm{SQA}$. As a form it is the general plain bilinear form $B(A,C)=AC$ of *The Two Forms and the Two Algebraic Norms of the Split-Complex Space*, whose diagonal is the first algebraic norm $B(A)=A^2$.

**Proposition (the properties of $AC$).**

| property | holds | witness |
|---|---|---|
| bilinear over $\mathbb{D}$ | yes | distributivity |
| commutative | yes | $AC=CA$ |
| associative | yes | $A(CD)=(AC)D$ |
| two-sided unit | yes | $1A=A1=A$ |
| alternative, flexible, power-associative | yes | consequences of associativity |
| zero divisors | yes | $\Pi_1\Pi_2=0$ with both factors non-zero |
| a field | no | the zero divisors are not invertible |

The failure of the field condition is the subject of *Split-Complex Zero Divisors*; as a ring, $\mathbb{D}\cong\mathbb{R}\times\mathbb{R}$ is a product of two fields, and its elements are classified in *The Classes of Element of the Split-Complex Algebra*.

## The Sesquilinear Product $A\overline{C}$

**Theorem (the sesqualgebra).** Over the algebra with involution $(\mathbb{D},\bar{\cdot})$, the product $A\overline{C}$ is conjugate-commutative,

$$
A\overline{C} = \overline{C\overline{A}},
$$

it has the **right** unit $1$ and no left unit, and it is **not** associative.

**Proof.** Conjugate-commutativity: $\overline{C\overline{A}}=\bar C A=A\overline{C}$, by the commutativity of the ring and the definition of the bar. Right unit: $A\overline{1}=A\cdot 1=A$. No left unit: if $E\overline{C}=C$ for every $C$, then taking $C=1$ gives $E=1$, but then $1\overline{j}=\bar j=-j\neq j$, a contradiction. Non-associativity: with $A=1$, $C=1$ and $D=j$ one has

$$
(A\overline{C})\overline{D} = (1\cdot 1)\overline{j} = -j, \qquad A\overline{(C\overline{D})} = 1\overline{(1\cdot\overline{j})} = \overline{-j} = j,
$$

so the two associators differ by $-2j$ and associativity fails.

The structure is therefore not the ring but a **sesqualgebra**: a module over an algebra with involution, with a conjugate-bilinear product. The product is conjugate-commutative and right-unital; the plain exchange of its two slots gives $C\bar A=\overline{A\bar C}$, the conjugate of the value, and its associator is developed in *The Sesquilinear Product of the Split-Complex Space*, below this article in this category. The exchange of the slots and the rest of the relations between the two products are collected in *Relations and Comparison Between the Two Products of the Split-Complex Space*, below this article in this category.

**Proposition (the properties of $A\overline{C}$).**

| property | holds | witness |
|---|---|---|
| linear in the first slot | yes | distributivity |
| conjugate-linear in the second | yes | $A\overline{\lambda C}=\bar\lambda\,A\overline{C}$ |
| commutative | no | $A\overline{C}=\overline{C\overline{A}}\neq C\overline{A}$ in general |
| conjugate-commutative | yes | $A\overline{C}=\overline{C\overline{A}}$ |
| associative | no | $(1\overline{1})\overline{j}=-j$ against $1\overline{(1\overline{j})}=j$ |
| left unit | no | $1\overline{j}=-j$ |
| right unit | yes | $A\overline{1}=A$ |
| alternative, flexible, power-associative | no | the same associator |

The associator, the left and right multiplications, the sandwich and the commutator of the sesquilinear product are *The Sesquilinear Product of the Split-Complex Space*, below this article in this category; as a form the product is the general plain sesquilinear form $H(A,C)=A\overline{C}$ of *The Two Forms and the Two Algebraic Norms of the Split-Complex Space*, whose diagonal is the second algebraic norm $H(A)=A\overline{A}=N(A)=a^2-a'^2$.

## The Two Products on the Idempotent Coordinates

The idempotent coordinates separate the two products completely. With $A=A_+\Pi_1+A_-\Pi_2$ and $C=C_+\Pi_1+C_-\Pi_2$, and with the bar exchanging the coordinates, $\overline{C}=C_-\Pi_1+C_+\Pi_2$, one has

$$
AC = A_+C_+\Pi_1 + A_-C_-\Pi_2, \qquad A\overline{C} = A_+C_-\Pi_1 + A_-C_+\Pi_2 .
$$

So the ring product is the **componentwise** product of the two idempotent coordinates, and the sesquilinear product is the componentwise product with the second factor's coordinates **exchanged**. Writ large on the pairs,

$$
AC \leftrightarrow (A_+C_+,\ A_-C_-), \qquad A\overline{C} \leftrightarrow (A_+C_-,\ A_-C_+).
$$

**Corollary (the two vanishing conditions).** $AC=0$ if and only if $A_+C_+=0$ and $A_-C_-=0$; $A\overline{C}=0$ if and only if $A_+C_-=0$ and $A_-C_+=0$. In particular $\Pi_1\overline{\Pi_1}=\Pi_1\Pi_2=0$ while $\Pi_1\Pi_1=\Pi_1$: an idempotent of the ring annihilates itself under the sesquilinear product.

The componentwise form of $AC$ is the reason the ring is the product of two copies of $\mathbb{R}$, $\mathbb{D}\cong\mathbb{R}\times\mathbb{R}$; the exchange of coordinates in $A\overline{C}$ is the reason the sesquilinear product has no left unit and cannot be associative, the exchange being an involution of the coordinates and not the identity. The coordinates and the componentwise multiplication are *Split-Complex Two-Component Element Representation* and *Split-Complex Algebra*.

## The Collapse of the Four General Products

The biquaternion space carries four general products: $\mathrm{GPA}(P,Q)=PQ$, $\mathrm{GQA}(P,Q)=P^{\natural}Q$, $\mathrm{GPS}(P,Q)=P\overline{Q}$ and $\mathrm{GQS}(P,Q)=P^{\natural}\overline{Q}$, the plain and the quaternionic family, each in its algebra and sesqualgebra version, in the codes of *The 12 Products of the Biquaternion Complex Space*. Read on $\mathbb{D}$ they take two values: the natural sign is the identity, so the quaternionic family coincides with the plain one, and two products of each pair of slots remain,

$$
\mathrm{GPA} = \mathrm{GQA} = AC, \qquad \mathrm{GPS} = \mathrm{GQS} = A\overline{C}.
$$

**Theorem (the four general products collapse to two).** On the split-complex space the four general products take the two values $AC$ and $A\overline{C}$.

**Proof.** The natural conjugation is the identity on $\mathbb{D}$, so $P^{\natural}=P$ and $\mathrm{GQA}(P,Q)=PQ=\mathrm{GPA}(P,Q)$ and $\mathrm{GQS}(P,Q)=P\overline{Q}=\mathrm{GPS}(P,Q)$. The algebra and the sesqualgebra values differ because the bar is not the identity: $AC$ and $A\overline{C}$ are different functions.

The four general products are *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, and their collapse on the split space with the symmetrisation and antisymmetrisation of the general products, the dictionary of the twelve codes and the count of the surviving structures are *The Collapse of the Twelve Structures on the Split-Complex Numbers*, below this article in this category.

## The Structures the Two Products Define

The two products define the two structures that survive on $\mathbb{D}$.

| product | structure | commutative | associative | unit |
|---|---|---|---|---|
| $AC$ | commutative ring, and algebra over $\mathbb{R}$ | yes | yes | two-sided |
| $A\overline{C}$ | sesqualgebra over $(\mathbb{D},\bar{\cdot})$ | conjugate-commutative | no | right only |

The first is the **algebra** $\mathbb{D}$, the split-complex numbers with their multiplication, and its classes of element — units, zero divisors, idempotents, ideals — are the subject of the Algebra group. The second is the **sesqualgebra**, the product with the second slot conjugated, and its defect, measured by the associator, is the subject of *The Sesquilinear Product of the Split-Complex Space*, below this article in this category. The two structures are the two objects the whole operational vocabulary of the chapter describes, and no third structure survives.

## The Point That Separates the Split Collapse from the Complex One

On the complex field the same identifications hold: $\mathbb{C}$ is commutative, its natural conjugation is the identity, and the four general products of the two-dimensional complex space collapse to the same two, the field product $AC$ and the sesquilinear product $A\overline{C}$. The count of the collapse is therefore identical on the two algebras, and the difference lies in **what the two surviving values are**.

The bilinear product is the multiplication of a **field** on $\mathbb{C}$: every non-zero element is a unit, there are no zero divisors, and the only idempotents are $0$ and $1$. The same product is the multiplication of a **ring** on $\mathbb{D}$: it has the zero divisors $a^2=a'^2$, the two non-trivial idempotents $\Pi_{1,2}$, and the two non-trivial ideals $\mathbb{R}\Pi_1,\mathbb{R}\Pi_2$. The split sign $j^2=+1$ against $i^2=-1$ is visible in the collapse not in the number of the surviving products but in the structure of the surviving bilinear one. This is stated and proved in *The Collapse of the Twelve Structures on the Split-Complex Numbers*, below this article in this category.

**Remark.** The comparison is exact at the level of the products and not at the level of their structures: the products $AC$ and $A\overline{C}$ are defined by the same formulas over any commutative algebra with involution, and it is the sign of the square of the generator, entering only through the conjugation, that decides whether the surviving objects are a field and a division-like sesqualgebra or a ring with zero divisors and a sesqualgebra with a right unit alone.

## Summary

The split-complex space carries two products, defined on the same coordinates: the general plain bilinear product $AC=(ac+a'c')+(ac'+a'c)j$, the multiplication of the algebra, and the general plain sesquilinear product $A\overline{C}=(ac-a'c')+(a'c-ac')j$, with the second slot conjugated. They are separated by the second slot — $AC$ is bilinear over $\mathbb{D}$, $A\overline{C}$ is conjugate-linear in the second slot — and they coincide exactly when the second factor is real or the first is zero.

The product $AC$ makes $\mathbb{D}$ a commutative, associative ring with two-sided unit $1$, and it is the common value of the four codes $\mathrm{GPA}=\mathrm{SPA}=\mathrm{GQA}=\mathrm{SQA}$; the product $A\overline{C}$ makes $\mathbb{D}$ a sesqualgebra over $(\mathbb{D},\bar{\cdot})$, conjugate-commutative, with the right unit $1$ and no left unit, and not associative, its associator measured by $(1\overline{1})\overline{j}=-j$ against $1\overline{(1\overline{j})}=j$. In the idempotent coordinates $AC$ is componentwise and $A\overline{C}$ exchanges the coordinates of the second factor. The four general products of the biquaternion space collapse to the two. On the complex field the same two values survive, and the difference is not in the count but in the structures: the surviving bilinear product is a field multiplication on $\mathbb{C}$ and a ring multiplication with zero divisors on $\mathbb{D}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $AC=(ac+a'c')+(ac'+a'c)j$ | the general plain bilinear product, the ring multiplication |
| $A\overline{C}=(ac-a'c')+(a'c-ac')j$ | the general plain sesquilinear product |
| $AC=A\overline{C} \iff C\in\mathbb{R}$ or $A=0$ | the agreement condition |
| $AC-A\overline{C}=2c'(a'+aj)$ | the difference of the two products |
| $\mathrm{GPA},\mathrm{GQA}$ | the general products of the plain and quaternionic algebra, both $AC$ |
| $\mathrm{GPS},\mathrm{GQS}$ | the general products of the plain and quaternionic sesqualgebra, both $A\overline{C}$ |
| $AC\leftrightarrow(A_+C_+,A_-C_-)$ | the ring product in idempotent coordinates |
| $A\overline{C}\leftrightarrow(A_+C_-,A_-C_+)$ | the sesquilinear product in idempotent coordinates |
| $B(A,C)=AC$, $H(A,C)=A\overline{C}$ | the two products as the two forms |
| $B(A)=A^2$, $H(A)=N(A)=A\overline{A}$ | their diagonals, the two algebraic norms |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for algebras with involution, sesquilinear products and the sesqualgebra.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, Graduate Texts in Mathematics 131, 2nd ed. 2001), for commutative rings with zero divisors and the failure of the field condition.
- Israel Nathan Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975), for associativity, units and the elementary properties of a ring.
- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the split-complex product and its idempotent coordinates.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the products of the split-complex algebra and its companion algebras.
