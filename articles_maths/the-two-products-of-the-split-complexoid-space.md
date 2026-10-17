# __The Two Products of the Split-Complexoid Space__

## Introduction

This article defines the **two products** carried by the split-complex space — the **general plain bilinear product** $Q_1Q_2$ and the **general plain sesquilinear product** $Q_1\overline{Q_2}$ — reads them on the coordinates, states the two structures they define, and isolates the one point that tells this pair of products from the pair carried by the complex field. The first is the multiplication of the algebra and makes $\mathbb{D}$ a commutative ring; the second is the product with the second argument conjugated and makes $\mathbb{D}$ a **sesqualgebra** over the algebra with involution $(\mathbb{D},\bar{\cdot})$. Two operations and two structures are the whole operational content of the split-complex space.

The two products are defined and their structures asserted here. The associator of the sesquilinear product, its ternary product, its left and right multiplications, its sandwich and its commutator are *The Sesquilinear Product of the Split-Complexoid Space*, below this article in this category. The forms and the norms the two products define are *The Two Forms and the Two Algebraic Norms of the Split-Complexoid Space*, and the products read on the distinguished subspaces are *Remarkable Subspaces and the Two Products of the Split-Complexoid Space*. The ring multiplication alone, with its zero divisors, its idempotents and its ideals, is *Split-Complex Algebra* and its companions.

**Conventions.** The algebra is $\mathbb{D}=\mathbb{R}[x]/(x^2-1)$, basis $1,j$, $j^2=+1$; a general element is $Q=q+jq'$; the conjugate is $\bar Q=q-jq'$; the idempotents are $\Pi_1=\tfrac12(1+j)$ and $\Pi_2=\tfrac12(1-j)$, with $Q=q_+\Pi_1+q_-\Pi_2$, $q_+=q+q'$ and $q_-=q-q'$. The Hermitian conjugation coincides with the bar. In this article $Q_1=q_1+jq'_1$ and $Q_2=q_2+jq'_2$ name elements, and the letters $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{*}$, $\langle\cdot,\cdot\rangle_{\natural}$ are kept for the forms and norms of *The Two Forms and the Two Algebraic Norms of the Split-Complexoid Space*.

## The Two Products

**Definition.** The **general plain bilinear product** and the **general plain sesquilinear product** of the elements $Q_1=q_1+jq'_1$ and $Q_2=q_2+jq'_2$ are

$$
Q_1Q_2 = (q_1q_2+q'_1q'_2) + (q_1q'_2+q'_1q_2)\,j, \qquad Q_1\overline{Q_2} = (q_1q_2-q'_1q'_2) + (q'_1q_2-q_1q'_2)\,j .
$$

The two products are defined on the same coordinates and take their values in the same plane; the first is the product of the algebra, the second differs from it by the conjugation of the second argument. They are the two products of the split-complex space, the bilinear one and the sesquilinear one.

**Proposition (the two products are separated by the second argument).** The product $Q_1Q_2$ is bilinear over $\mathbb{D}$, in both arguments. The product $Q_1\overline{Q_2}$ is linear in the first argument and conjugate-linear in the second,

$$
Q_1\overline{\lambda Q_2} = \bar\lambda\,Q_1\overline{Q_2}, \qquad \lambda \in \mathbb{D},
$$

and the two products coincide exactly when the second factor is real or the first factor is zero.

**Proof.** Bilinearity of $Q_1Q_2$ is the distributivity of the algebra. For $Q_1\overline{Q_2}$, linearity in $Q_1$ is clear from the coordinates; in the second argument, $Q_1\overline{\lambda Q_2}=Q_1\,\bar\lambda\,\overline{Q_2}=\bar\lambda\,Q_1\overline{Q_2}$, so the argument is conjugate-linear. The difference is

$$
Q_1Q_2 - Q_1\overline{Q_2} = 2q'_2(q'_1+q_1j),
$$

which vanishes if and only if $q'_2=0$, that is $Q_2\in\mathbb{R}$, or $Q_1=0$.

So the two products differ by the conjugate-linearity in the second argument, and they agree on every pair whose second factor is real. On the pair $Q_1=Q_2=j$ they disagree as much as possible on the second coordinate, $Q_1Q_2=j^2=1$ against $Q_1\overline{Q_2}=j(-j)=-1$; the sign is the split sign $j^2=+1$, and it is the whole of the difference between the two products beyond the conjugation.

## The Ring Product $Q_1Q_2$

**Theorem (the commutative ring).** Under the product $Q_1Q_2$ the plane $\mathbb{D}$ is a commutative, associative ring with the two-sided unit $1$, and $\mathbb{D}$ is the algebra $\mathbb{R}[x]/(x^2-1)$.

**Proof.** Commutativity is the symmetry of the coordinate formulas, $q_1q_2+q'_1q'_2=q_2q_1+q'_2q'_1$ and $q_1q'_2+q'_1q_2=q_2q'_1+q'_2q_1$; associativity is the associativity of the polynomial algebra $\mathbb{R}[x]/(x^2-1)$, or equally the identity $Q_1(Q_2Q_3)=(Q_1Q_2)Q_3$ checked on the three coordinates; and $1\cdot Q_1=Q_1\cdot 1=Q_1$. The ring is the algebra, by definition of the multiplication of $\mathbb{D}$.

The product $Q_1Q_2$ is the bilinear, commutative, associative operation with unit, the multiplication of the split-complex algebra. As a form it is the general plain bilinear form $\langle Q_1,Q_2\rangle=Q_1Q_2$ of *The Two Forms and the Two Algebraic Norms of the Split-Complexoid Space*, whose algebraic norm is the first algebraic norm $\langle Q_1\rangle=Q_1^2$.

**Proposition (the properties of $Q_1Q_2$).**

| property | holds | witness |
|---|---|---|
| bilinear over $\mathbb{D}$ | yes | distributivity |
| commutative | yes | $Q_1Q_2=Q_2Q_1$ |
| associative | yes | $Q_1(Q_2Q_3)=(Q_1Q_2)Q_3$ |
| two-sided unit | yes | $1Q_1=Q_1 1=Q_1$ |
| alternative, flexible, power-associative | yes | consequences of associativity |
| zero divisors | yes | $\Pi_1\Pi_2=0$ with both factors non-zero |
| a field | no | the zero divisors are not invertible |

The failure of the field condition is the subject of *Split-Complex Zero Divisors*; as a ring, $\mathbb{D}\cong\mathbb{R}\times\mathbb{R}$ is a product of two fields, and its elements are classified in *The Classes of Element of the Split-Complex Algebra*.

## The Sesquilinear Product $Q_1\overline{Q_2}$

**Theorem (the sesqualgebra).** Over the algebra with involution $(\mathbb{D},\bar{\cdot})$, the product $Q_1\overline{Q_2}$ is conjugate-commutative,

$$
Q_1\overline{Q_2} = \overline{Q_2\overline{Q_1}},
$$

it has the **right** unit $1$ and no left unit, and it is **not** associative.

**Proof.** Conjugate-commutativity: $\overline{Q_2\overline{Q_1}}=\bar Q_2 Q_1=Q_1\overline{Q_2}$, by the commutativity of the ring and the definition of the bar. Right unit: $Q_1\overline{1}=Q_1\cdot 1=Q_1$. No left unit: if $E\overline{Q_2}=Q_2$ for every $Q_2$, then taking $Q_2=1$ gives $E=1$, but then $1\overline{j}=\bar j=-j\neq j$, a contradiction. Non-associativity: with $Q_1=1$, $Q_2=1$ and $Q_3=j$ one has

$$
(Q_1\overline{Q_2})\overline{Q_3} = (1\cdot 1)\overline{j} = -j, \qquad Q_1\overline{(Q_2\overline{Q_3})} = 1\overline{(1\cdot\overline{j})} = \overline{-j} = j,
$$

so the two associators differ by $-2j$ and associativity fails.

The structure is therefore not the ring but a **sesqualgebra**: a module over an algebra with involution, with a conjugate-bilinear product. The product is conjugate-commutative and right-unital; the plain exchange of its two arguments gives $Q_2\bar Q_1=\overline{Q_1\bar Q_2}$, the conjugate of the value, and its associator is developed in *The Sesquilinear Product of the Split-Complexoid Space*, below this article in this category. The exchange of the arguments and the rest of the relations between the two products are collected in *Relations and Comparison Between the Two Products of the Split-Complexoid Space*, below this article in this category.

**Proposition (the properties of $Q_1\overline{Q_2}$).**

| property | holds | witness |
|---|---|---|
| linear in the first argument | yes | distributivity |
| conjugate-linear in the second | yes | $Q_1\overline{\lambda Q_2}=\bar\lambda\,Q_1\overline{Q_2}$ |
| commutative | no | $Q_1\overline{Q_2}=\overline{Q_2\overline{Q_1}}\neq Q_2\overline{Q_1}$ in general |
| conjugate-commutative | yes | $Q_1\overline{Q_2}=\overline{Q_2\overline{Q_1}}$ |
| associative | no | $(1\overline{1})\overline{j}=-j$ against $1\overline{(1\overline{j})}=j$ |
| left unit | no | $1\overline{j}=-j$ |
| right unit | yes | $Q_1\overline{1}=Q_1$ |
| alternative, flexible, power-associative | no | the same associator |

The associator, the left and right multiplications, the sandwich and the commutator of the sesquilinear product are *The Sesquilinear Product of the Split-Complexoid Space*, below this article in this category; as a form the product is the general plain sesquilinear form $\langle Q_1,Q_2\rangle_{*}=Q_1\overline{Q_2}$ of *The Two Forms and the Two Algebraic Norms of the Split-Complexoid Space*, whose algebraic norm is the second algebraic norm $\langle Q_1\rangle_{*}=Q_1\overline{Q_1}=\langle Q_1\rangle_{\natural}=q_1^2-q'_1^2$.

## The Two Products on the Idempotent Coordinates

The idempotent coordinates separate the two products completely. With $Q_1=q_{1+}\Pi_1+q_{1-}\Pi_2$ and $Q_2=q_{2+}\Pi_1+q_{2-}\Pi_2$, and with the bar exchanging the coordinates, $\overline{Q_2}=q_{2-}\Pi_1+q_{2+}\Pi_2$, one has

$$
Q_1Q_2 = q_{1+}q_{2+}\Pi_1 + q_{1-}q_{2-}\Pi_2, \qquad Q_1\overline{Q_2} = q_{1+}q_{2-}\Pi_1 + q_{1-}q_{2+}\Pi_2 .
$$

So the ring product is the **componentwise** product of the two idempotent coordinates, and the sesquilinear product is the componentwise product with the second factor's coordinates **exchanged**. Writ large on the pairs,

$$
Q_1Q_2 \leftrightarrow (q_{1+}q_{2+},\ q_{1-}q_{2-}), \qquad Q_1\overline{Q_2} \leftrightarrow (q_{1+}q_{2-},\ q_{1-}q_{2+}).
$$

**Corollary (the two vanishing conditions).** $Q_1Q_2=0$ if and only if $q_{1+}q_{2+}=0$ and $q_{1-}q_{2-}=0$; $Q_1\overline{Q_2}=0$ if and only if $q_{1+}q_{2-}=0$ and $q_{1-}q_{2+}=0$. In particular $\Pi_1\overline{\Pi_1}=\Pi_1\Pi_2=0$ while $\Pi_1\Pi_1=\Pi_1$: an idempotent of the ring annihilates itself under the sesquilinear product.

The componentwise form of $Q_1Q_2$ is the reason the ring is the product of two copies of $\mathbb{R}$, $\mathbb{D}\cong\mathbb{R}\times\mathbb{R}$; the exchange of coordinates in $Q_1\overline{Q_2}$ is the reason the sesquilinear product has no left unit and cannot be associative, the exchange being an involution of the coordinates and not the identity. The coordinates and the componentwise multiplication are *Split-Complex Two-Component Element Representation* and *Split-Complex Algebra*.

## The Structures the Two Products Define

The two products define the two structures carried by $\mathbb{D}$.

| product | structure | commutative | associative | unit |
|---|---|---|---|---|
| $Q_1Q_2$ | commutative ring, and algebra over $\mathbb{R}$ | yes | yes | two-sided |
| $Q_1\overline{Q_2}$ | sesqualgebra over $(\mathbb{D},\bar{\cdot})$ | conjugate-commutative | no | right only |

The first is the **algebra** $\mathbb{D}$, the split-complex numbers with their multiplication, and its classes of element — units, zero divisors, idempotents, ideals — are the subject of the Algebra group. The second is the **sesqualgebra**, the product with the second argument conjugated, and its defect, measured by the associator, is the subject of *The Sesquilinear Product of the Split-Complexoid Space*, below this article in this category. The two structures are the two objects the whole operational vocabulary of the chapter describes, and no third structure occurs.

## The Point That Separates the Split Case from the Complex One

On the complex field the same two identifications hold: $\mathbb{C}$ is commutative, its involution is conjugation, and the two products of the two-dimensional complex space are the field product $AC$ and the sesquilinear product $A\overline{C}$. The difference lies in **what the two products are**.

The bilinear product is the multiplication of a **field** on $\mathbb{C}$: every non-zero element is a unit, there are no zero divisors, and the only idempotents are $0$ and $1$. The same product is the multiplication of a **ring** on $\mathbb{D}$: it has the zero divisors $q^2=q'^2$, the two non-trivial idempotents $\Pi_1$ and $\Pi_2$, and the two non-trivial ideals $\mathbb{R}\Pi_1,\mathbb{R}\Pi_2$. The split sign $j^2=+1$ against $i^2=-1$ is visible not in the number of the products but in the structure of the bilinear one.

**Remark.** The comparison is exact at the level of the products and not at the level of their structures: the products $AC$ and $A\overline{C}$ are defined by the same formulas over any commutative algebra with involution, and it is the sign of the square of the generator, entering only through the conjugation, that decides whether the surviving objects are a field and a division-like sesqualgebra or a ring with zero divisors and a sesqualgebra with a right unit alone.

## Summary

The split-complex space carries two products, defined on the same coordinates: the general plain bilinear product $Q_1Q_2=(q_1q_2+q'_1q'_2)+(q_1q'_2+q'_1q_2)j$, the multiplication of the algebra, and the general plain sesquilinear product $Q_1\overline{Q_2}=(q_1q_2-q'_1q'_2)+(q'_1q_2-q_1q'_2)j$, with the second argument conjugated. They are separated by the second argument — $Q_1Q_2$ is bilinear over $\mathbb{D}$, $Q_1\overline{Q_2}$ is conjugate-linear in the second argument — and they coincide exactly when the second factor is real or the first is zero.

The product $Q_1Q_2$ makes $\mathbb{D}$ a commutative, associative ring with two-sided unit $1$; the product $Q_1\overline{Q_2}$ makes $\mathbb{D}$ a sesqualgebra over $(\mathbb{D},\bar{\cdot})$, conjugate-commutative, with the right unit $1$ and no left unit, and not associative, its associator measured by $(1\overline{1})\overline{j}=-j$ against $1\overline{(1\overline{j})}=j$. In the idempotent coordinates $Q_1Q_2$ is componentwise and $Q_1\overline{Q_2}$ exchanges the coordinates of the second factor. On the complex field the same two values occur, and the difference is not in the count but in the structures: the surviving bilinear product is a field multiplication on $\mathbb{C}$ and a ring multiplication with zero divisors on $\mathbb{D}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $Q_1Q_2=(q_1q_2+q'_1q'_2)+(q_1q'_2+q'_1q_2)j$ | the general plain bilinear product, the ring multiplication |
| $Q_1\overline{Q_2}=(q_1q_2-q'_1q'_2)+(q'_1q_2-q_1q'_2)j$ | the general plain sesquilinear product |
| $Q_1Q_2=Q_1\overline{Q_2} \iff Q_2\in\mathbb{R}$ or $Q_1=0$ | the agreement condition |
| $Q_1Q_2-Q_1\overline{Q_2}=2q'_2(q'_1+q_1j)$ | the difference of the two products |
| $Q_1Q_2\leftrightarrow(q_{1+}q_{2+},q_{1-}q_{2-})$ | the ring product in idempotent coordinates |
| $Q_1\overline{Q_2}\leftrightarrow(q_{1+}q_{2-},q_{1-}q_{2+})$ | the sesquilinear product in idempotent coordinates |
| $\langle Q_1,Q_2\rangle=Q_1Q_2$, $\langle Q_1,Q_2\rangle_{*}=Q_1\overline{Q_2}$ | the two products as the two forms |
| $\langle Q_1\rangle=Q_1^2$, $\langle Q_1\rangle_{*}=\langle Q_1\rangle_{\natural}=Q_1\overline{Q_1}$ | their algebraic norms, the two algebraic norms |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for algebras with involution, sesquilinear products and the sesqualgebra.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, Graduate Texts in Mathematics 131, 2nd ed. 2001), for commutative rings with zero divisors and the failure of the field condition.
- Israel Nathan Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975), for associativity, units and the elementary properties of a ring.
- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the split-complex product and its idempotent coordinates.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the products of the split-complex algebra and its companion algebras.
