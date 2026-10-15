# __The Two Products of the Complexoid Space__

## Introduction

The complex space carries two products: the **general plain bilinear product** $AC$, which is the multiplication of the field, and the **general plain sesquilinear product** $A\bar C$, the derived operation of the algebra with its conjugate-linear involution. They are the two products on which the whole `## Complex Numbers` chapter is built.

This article defines the two products, writes them in coordinates, states the defining property of each, and names the two structures they define. The full relations between them and their comparison, as a table with witnesses, are *Relations and Comparison Between the Two Products*, below this article in this category; the multiplication of the field is *Complex Algebra*, below this article in this category, which owns it; and the two forms carried by the two products are *The Two Forms and the Two Algebraic Norms of the Complex Space*, also below.

The elements are written $A = a + ia'$ and $C = c + ic'$. The **bar** is complex conjugation and the **Hermitian star** coincides with it, $A^{*} = \bar A$.

## The Two Products

**Definition.** The **general plain bilinear product** is the multiplication of the field,

$$
A \cdot C = AC,
$$

and the **general plain sesquilinear product** is the derived operation

$$
A \cdot C = A\bar C,
$$

the multiplication of the first element by the conjugate of the second.

Both are $\mathbb{R}$-bilinear in the pair. The bilinear product is $\mathbb{C}$-linear in each argument; the sesquilinear product is $\mathbb{C}$-linear in the first argument and conjugate-linear in the second.

**Remark (why exactly two).** The two products are the two ways the involution of the field can enter a multiplication of a pair: it enters not at all, giving $AC$, or it enters in the second argument, giving $A\bar C$. There is no third way, the insertion of the bar in the first argument only reproducing the second product by commutativity, $(\bar A)C = \overline{(\bar C)A}$. The two products are the whole product structure of the complex space.

## The Two Products in Coordinates

With $A = a + ia'$ and $C = c + ic'$,

$$
AC = \bigl(ac - a'c'\bigr) + i\bigl(ac' + a'c\bigr), \qquad
A\bar C = \bigl(ac + a'c'\bigr) + i\bigl(a'c - ac'\bigr) .
$$

**Proof.** The first is the multiplication of complex numbers. For the second, $\bar C = c - ic'$ and

$$
A\bar C = (a + ia')(c - ic') = ac + a'c' + i(a'c - ac') .
$$

Both are single complex numbers, neither has a remainder outside the algebra, and each is $\mathbb{R}$-bilinear in the pair. The two products differ only in the sign of the $a'c'$ term of the real part and in the order of the factors of the imaginary part.

## The Plain Product $AC$

**Proposition.** The product $AC$ has the following properties.

1. It is $\mathbb{C}$-bilinear: $A(\lambda C) = (\lambda A)C = \lambda(AC)$ for every $\lambda \in \mathbb{C}$.
2. It is associative, $(AC)D = A(CD)$, and commutative, $AC = CA$.
3. The unit $1$ is a two-sided unit, $1 \cdot A = A \cdot 1 = A$.
4. It has no zero divisor: $AC = 0$ implies $A = 0$ or $C = 0$, and every nonzero element is invertible.

**Proof.** Items 1 to 3 are the axioms of the field and are owned by *Complex Algebra*. Item 4 holds because $\mathbb{C}$ is a field: if $A \neq 0$ then $C = A^{-1}(AC) = 0$.

The product $AC$ is the multiplication of the field, the left multiplications form a monoid isomorphic to the multiplicative monoid of $\mathbb{C}$, and the product is the operation of the first of the two structures defined below.

## The Plain Sesquilinear Product $A\bar C$

**Proposition.** The product $A\bar C$ has the following properties.

1. It is $\mathbb{C}$-linear in the first argument and conjugate-linear in the second:
   $(\lambda A)\bar C = \lambda (A\bar C)$ and $A\overline{(\lambda C)} = \bar\lambda (A\bar C)$.
2. It is conjugate-commutative, $A\bar C = \overline{C\bar A}$.
3. The unit $1$ is a right unit but not a left unit, $A\bar 1 = A$ and $1\bar C = \bar C$.
4. It is not associative.

**Proof.** Item 1 follows from the multiplication being bilinear and the bar being an involution. For item 2, $\overline{C\bar A} = \bar C A = A\bar C$, the last step by commutativity. For item 3, $\bar 1 = 1$ gives $A\bar 1 = A$, while $1\bar C = \bar C$, which equals $C$ only for real $C$. For item 4 the witness is $A = 1$, $C = 1$, $D = i$:

$$
(A\bar C)\bar D = 1 \cdot \bar i = -i, \qquad A\overline{(C\bar D)} = \overline{1 \cdot \bar i} = \overline{-i} = i .
$$

The two differ, so the product is not associative; it also fails alternation and flexibility and the degree-three identity, the weaker laws of an associative product, with witnesses in *Relations and Comparison Between the Two Products*, below this article in this category, and the failure is the general one for a sesquilinear product, the second slot carrying the conjugate.

The product $A\bar C$ is the derived operation of the algebra with its conjugate-linear involution: it is the sesquilinear form of the algebra read as a multiplication, it is conjugate-commutative, and it has no zero divisor, since $A\bar C = 0$ with $A \neq 0$ forces $\bar C = 0$. Its properties against those of $AC$ are tabulated in *Relations and Comparison Between the Two Products*, below this article in this category.

## The Two Structures the Two Products Define

The two products define two structures on the complex space.

**The field.** The product $AC$ makes $\mathbb{C}$ a field: associative, commutative, with the two-sided unit $1$ and with every nonzero element invertible. This structure is the **general plain algebra** of the complex space, and the multiplication is owned by *Complex Algebra*.

**The sesqualgebra.** The product $A\bar C$, read over the pair $(\mathbb{C}, \bar\cdot)$, makes the complex space a **general plain sesqualgebra**: a left $\mathbb{C}$-module with a product that is conjugate-linear in the second argument, conjugate-commutative, with the right unit $1$ alone and without associativity. It is the structure that carries the Hermitian form.

Together the field and the sesqualgebra are the whole structure block of the complex space: the field carries the products and the inverses, and the sesqualgebra carries the conjugate-linear form.

## Summary

The complex space carries two products: the general plain bilinear product $AC$, the multiplication of the field, and the general plain sesquilinear product $A\bar C$, the derived operation of the algebra with its conjugate-linear involution. The first is the involution-free product of the pair; the second is the product in which the bar enters the second argument.

In coordinates, $AC = (ac - a'c') + i(ac' + a'c)$ and $A\bar C = (ac + a'c') + i(a'c - ac')$. The product $AC$ is $\mathbb{C}$-bilinear, associative, commutative, unital and without zero divisors; the product $A\bar C$ is $\mathbb{C}$-linear in the first argument and conjugate-linear in the second, conjugate-commutative, right-unital but not left-unital, and not associative, with the witness $(1, 1, i)$.

The two products define two structures: the field $\mathbb{C}$ under $AC$, and the general plain sesqualgebra over $(\mathbb{C}, \bar\cdot)$ under $A\bar C$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $AC$ | the general plain bilinear product, the multiplication of the field |
| $A\bar C$ | the general plain sesquilinear product, the derived operation with the bar |
| $A = a + ia'$, $C = c + ic'$ | the elements, with real coordinates |
| $\bar\cdot$ | the bar, complex conjugation, the involution of the field |
| ${}^{*}$ | the Hermitian star, which coincides with the bar |
| $\mathrm{alg}$ | the algebra slot, the field under $AC$ |
| $\mathrm{sesq}$ | the sesqualgebra slot, over $(\mathbb{C}, \bar\cdot)$ under $A\bar C$ |

## Further Reading

- Serge Lang, *Algebra*, 3rd edition (Springer, 2002), for the multiplication of a field, sesquilinear forms and the derived operation of an algebra with an involution.
- Israel Nathan Herstein, *Topics in Algebra*, 2nd edition (Wiley, 1975), for commutative rings, their symmetric and antisymmetric parts and the Jordan and Lie structures of an algebra product.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for algebras with involution and the sesquilinear forms they carry.
- Nathan Jacobson, *Structure of Rings* (American Mathematical Society, 1956), for the general product, its symmetric and antisymmetric parts and the structures they define.
