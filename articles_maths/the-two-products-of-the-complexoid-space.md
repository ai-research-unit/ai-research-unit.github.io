# __The Two Products of the Complexoid Space__

## Introduction

The complex space carries two products: the **general plain bilinear product** $Q_1Q_2$, which is the multiplication of the field, and the **general plain sesquilinear product** $Q_1\bar Q_2$, the derived operation of the algebra with its conjugate-linear involution. They are the two products on which the whole `## Complex Numbers` chapter is built.

This article defines the two products, writes them in coordinates, states the defining property of each, and names the two structures they define. The full relations between them and their comparison, as a table with witnesses, are *Relations and Comparison Between the Two Products*, below this article in this category; the multiplication of the field is *Complex Algebra*, below this article in this category, which owns it; and the two forms carried by the two products are *The Two Forms and the Two Algebraic Norms of the Complexoid Space*, also below.

The elements are written $Q_1 = q_1 + iq'_1$ and $Q_2 = q_2 + iq'_2$. The **bar** is complex conjugation and the **Hermitian star** coincides with it, $Q_1^{*} = \bar Q_1$.

## The Two Products

**Definition.** The **general plain bilinear product** is the multiplication of the field,

$$
Q_1 \cdot Q_2 = Q_1Q_2,
$$

and the **general plain sesquilinear product** is the derived operation

$$
Q_1 \star Q_2 = Q_1\bar Q_2,
$$

the multiplication of the first element by the conjugate of the second.

Both are $\mathbb{R}$-bilinear in the pair. The bilinear product is $\mathbb{C}$-linear in each argument; the sesquilinear product is $\mathbb{C}$-linear in the first argument and conjugate-linear in the second.

**Remark (why exactly two).** The two products are the two ways the involution of the field can enter a multiplication of a pair: it enters not at all, giving $Q_1Q_2$, or it enters in the second argument, giving $Q_1\bar Q_2$. There is no third way, the insertion of the bar in the first argument only reproducing the second product by commutativity, $(\bar Q_1)Q_2 = \overline{(\bar Q_2)Q_1}$. The two products are the whole product structure of the complex space.

## The Two Products in Coordinates

With $Q_1 = q_1 + iq'_1$ and $Q_2 = q_2 + iq'_2$,

$$
\boxed{\;Q_1Q_2 = \bigl(q_1q_2 - q'_1q'_2\bigr) + i\bigl(q_1q'_2 + q'_1q_2\bigr), \qquad
Q_1\bar Q_2 = \bigl(q_1q_2 + q'_1q'_2\bigr) + i\bigl(q'_1q_2 - q_1q'_2\bigr)\;}.
$$

**Proof.** The first is the multiplication of complex numbers. For the second, $\bar Q_2 = q_2 - iq'_2$ and

$$
Q_1\bar Q_2 = (q_1 + iq'_1)(q_2 - iq'_2) = q_1q_2 + q'_1q'_2 + i(q'_1q_2 - q_1q'_2) .
$$

Both are single complex numbers, neither has a remainder outside the algebra, and each is $\mathbb{R}$-bilinear in the pair. The two products differ only in the sign of the $q'_1q'_2$ term of the real part and in the order of the factors of the imaginary part.

## The Plain Product $Q_1Q_2$

**Proposition.** The product $Q_1Q_2$ has the following properties.

1. It is $\mathbb{C}$-bilinear: $Q_1(\lambda Q_2) = (\lambda Q_1)Q_2 = \lambda(Q_1Q_2)$ for every $\lambda \in \mathbb{C}$.
2. It is associative, $(Q_1Q_2)Q_3 = Q_1(Q_2Q_3)$, and commutative, $Q_1Q_2 = Q_2Q_1$.
3. The unit $1$ is a two-sided unit, $1 \cdot Q_1 = Q_1 \cdot 1 = Q_1$.
4. It has no zero divisor: $Q_1Q_2 = 0$ implies $Q_1 = 0$ or $Q_2 = 0$, and every nonzero element is invertible.

**Proof.** Items 1 to 3 are the axioms of the field and are owned by *Complex Algebra*. Item 4 holds because $\mathbb{C}$ is a field: if $Q_1 \neq 0$ then $Q_2 = Q_1^{-1}(Q_1Q_2) = 0$.

The product $Q_1Q_2$ is the multiplication of the field, the left multiplications form a monoid isomorphic to the multiplicative monoid of $\mathbb{C}$, and the product is the operation of the first of the two structures defined below.

## The Plain Sesquilinear Product $Q_1\bar Q_2$

**Proposition.** The product $Q_1\bar Q_2$ has the following properties.

1. It is $\mathbb{C}$-linear in the first argument and conjugate-linear in the second:
   $(\lambda Q_1)\bar Q_2 = \lambda (Q_1\bar Q_2)$ and $Q_1\overline{(\lambda Q_2)} = \bar\lambda (Q_1\bar Q_2)$.
2. It is conjugate-commutative, $Q_1\bar Q_2 = \overline{Q_2\bar Q_1}$.
3. The unit $1$ is a right unit but not a left unit, $Q_1\bar 1 = Q_1$ and $1\bar Q_2 = \bar Q_2$.
4. It is not associative.

**Proof.** Item 1 follows from the multiplication being bilinear and the bar being an involution. For item 2, $\overline{Q_2\bar Q_1} = \bar Q_2 Q_1 = Q_1\bar Q_2$, the last step by commutativity. For item 3, $\bar 1 = 1$ gives $Q_1\bar 1 = Q_1$, while $1\bar Q_2 = \bar Q_2$, which equals $Q_2$ only for real $Q_2$. For item 4 the witness is $Q_1 = 1$, $Q_2 = 1$, $Q_3 = i$:

$$
\boxed{\;(Q_1\bar Q_2)\bar Q_3 = 1 \cdot \bar i = -i, \qquad Q_1\overline{(Q_2\bar Q_3)} = \overline{1 \cdot \bar i} = \overline{-i} = i\;}.
$$

The two differ, so the product is not associative; it also fails alternation and flexibility and the degree-three identity, the weaker laws of an associative product, with witnesses in *Relations and Comparison Between the Two Products*, below this article in this category, and the failure is the general one for a sesquilinear product, the second slot carrying the conjugate.

The product $Q_1\bar Q_2$ is the derived operation of the algebra with its conjugate-linear involution: it is the sesquilinear form of the algebra read as a multiplication, it is conjugate-commutative, and it has no zero divisor, since $Q_1\bar Q_2 = 0$ with $Q_1 \neq 0$ forces $\bar Q_2 = 0$. Its properties against those of $Q_1Q_2$ are tabulated in *Relations and Comparison Between the Two Products*, below this article in this category.

## The Two Structures the Two Products Define

The two products define two structures on the complex space.

**The field.** The product $Q_1Q_2$ makes $\mathbb{C}$ a field: associative, commutative, with the two-sided unit $1$ and with every nonzero element invertible. This structure is the **general plain algebra** of the complex space, and the multiplication is owned by *Complex Algebra*.

**The sesqualgebra.** The product $Q_1\bar Q_2$, read over the pair $(\mathbb{C}, \bar\cdot)$, makes the complex space a **general plain sesqualgebra**: a left $\mathbb{C}$-module with a product that is conjugate-linear in the second argument, conjugate-commutative, with the right unit $1$ alone and without associativity. It is the structure that carries the Hermitian form.

Together the field and the sesqualgebra are the whole structure block of the complex space: the field carries the products and the inverses, and the sesqualgebra carries the conjugate-linear form.

## Summary

The complex space carries two products: the general plain bilinear product $Q_1Q_2$, the multiplication of the field, and the general plain sesquilinear product $Q_1\bar Q_2$, the derived operation of the algebra with its conjugate-linear involution. The first is the involution-free product of the pair; the second is the product in which the bar enters the second argument.

In coordinates, $Q_1Q_2 = (q_1q_2 - q'_1q'_2) + i(q_1q'_2 + q'_1q_2)$ and $Q_1\bar Q_2 = (q_1q_2 + q'_1q'_2) + i(q'_1q_2 - q_1q'_2)$. The product $Q_1Q_2$ is $\mathbb{C}$-bilinear, associative, commutative, unital and without zero divisors; the product $Q_1\bar Q_2$ is $\mathbb{C}$-linear in the first argument and conjugate-linear in the second, conjugate-commutative, right-unital but not left-unital, and not associative, with the witness $(1, 1, i)$.

The two products define two structures: the field $\mathbb{C}$ under $Q_1Q_2$, and the general plain sesqualgebra over $(\mathbb{C}, \bar\cdot)$ under $Q_1\bar Q_2$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $Q_1Q_2$ | the general plain bilinear product, the multiplication of the field |
| $Q_1\bar Q_2 = Q_1\star Q_2$ | the general plain sesquilinear product, the derived operation with the bar |
| $Q_1 = q_1 + iq'_1$, $Q_2 = q_2 + iq'_2$ | the elements, with real coordinates |
| $\bar\cdot$ | the bar, complex conjugation, the involution of the field |
| ${}^{*}$ | the Hermitian star, which coincides with the bar |
| $\mathrm{alg}$ | the algebra slot, the field under $Q_1Q_2$ |
| $\mathrm{sesq}$ | the sesqualgebra slot, over $(\mathbb{C}, \bar\cdot)$ under $Q_1\bar Q_2$ |

## Further Reading

- Serge Lang, *Algebra*, 3rd edition (Springer, 2002), for the multiplication of a field, sesquilinear forms and the derived operation of an algebra with an involution.
- Israel Nathan Herstein, *Topics in Algebra*, 2nd edition (Wiley, 1975), for commutative rings, their symmetric and antisymmetric parts and the Jordan and Lie structures of an algebra product.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for algebras with involution and the sesquilinear forms they carry.
- Nathan Jacobson, *Structure of Rings* (American Mathematical Society, 1956), for the general product, its symmetric and antisymmetric parts and the structures they define.
