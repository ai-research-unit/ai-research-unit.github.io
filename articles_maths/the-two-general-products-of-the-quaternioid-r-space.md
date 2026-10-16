# __The Two General Products of the Quaternioid $\mathbb{R}$ Space__

## Introduction

The quaternion space $\mathbb{H}$ is a four-dimensional real vector space and an associative division algebra, and it carries **two** general products: the **general plain bilinear product** $\tilde p\tilde q$, the multiplication of the algebra, and the **general quaternionic bilinear product** $\tilde p^{\natural}\tilde q$, the plain product with the first factor read through the quaternion conjugation ${}^{\natural}$. The base of the quaternion algebra is $\mathbb{R}$, so the only conjugation available is the natural conjugation ${}^{\natural}$ of the element; the pairing that uses it in the second slot returns the two general products read with both arguments conjugated, with the same scalar parts and the same laws, so no new family arises. Exactly two general products are read on $\mathbb{H}$, and this article defines them.

The two products and their two structures are defined here. The identities that link them are *Relations Between the Two General Products*, below this article in this category, and the table of their laws is *Comparison Between the Two General Products*, below this article in this category. The symmetrisation and the antisymmetrisation of the two are *The 6 Products of the Quaternioid Real Space*, and the three companion structures they define are *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*, both below this article in this category. The left and right multiplications of the two are *The Two General Products and Operators*, the reading on the distinguished subspaces is *Remarkable Subspaces and the Two General Products*, and the degree-two reading is *The 2 Forms over the Quaternioid $\mathbb{R}$ Space*, *The 2 Algebraic Norms over the Quaternioid $\mathbb{R}$ Space* and *Remarkable Subspaces and the Two Forms*, all below this article in this category.

**Conventions.** The algebra is $\mathbb{H}$, the real quaternion algebra, with units $e_0=1,e_1,e_2,e_3$, the relations $e_k^2=-e_0$ and $e_1e_2=e_3$, $e_2e_3=e_1$, $e_3e_1=e_2$, and the general element $\tilde q=q_0e_0+\vec q$, $\vec q=q_1e_1+q_2e_2+q_3e_3$, with real coefficients $q_\mu$. The **dot product** is $\vec p\cdot\vec q=p_1q_1+p_2q_2+p_3q_3$ and the **cross product** $\vec p\times\vec q$ is the usual one, $(p_2q_3-p_3q_2)e_1+(p_3q_1-p_1q_3)e_2+(p_1q_2-p_2q_1)e_3$. The **scalar part** is $\mathrm{Sc}(\tilde q)=q_0$ and the **vector part** is $\operatorname{Vect}(\tilde q)=\vec q$. In this article $\tilde p$ and $\tilde q$ name elements, so that the brackets stay free for the forms.

## The Two Products

**Definition.** The **general plain bilinear product** and the **general quaternionic bilinear product** of the elements $\tilde p=p_0e_0+\vec p$ and $\tilde q=q_0e_0+\vec q$ are

$$
\tilde p\tilde q = \bigl(p_0q_0-\vec p\cdot\vec q\bigr) + p_0\vec q + q_0\vec p + \vec p\times\vec q ,
$$

$$
\tilde p^{\natural}\tilde q = \bigl(p_0q_0+\vec p\cdot\vec q\bigr) + p_0\vec q - q_0\vec p - \vec p\times\vec q .
$$

The first is the product of the algebra, read on the scalar and vector parts of the two elements; the second is the same rule with the first factor read through ${}^{\natural}$, which changes the sign of its vector part alone. The two products are defined on the same pair of coordinates and take their values in the same space, and the two are the **general** products of $\mathbb{H}$ in the sense of the general construction: the plain product with the two slots read as they stand, and the plain product with the first slot conjugated by the only nontrivial involution the element carries.

Both products are $\mathbb{R}$-bilinear, being built from the bilinear operations of the real vector space $\mathbb{H}$: the scalar and vector parts, the dot product and the cross product are all bilinear over $\mathbb{R}$.

**Proposition (the two products separate the scalar and the vector part of the first factor).** For all $\tilde p,\tilde q$,

$$
\tilde p\tilde q+\tilde p^{\natural}\tilde q=2p_0\,\tilde q , \qquad \tilde p\tilde q-\tilde p^{\natural}\tilde q=2\,\vec p\,\tilde q ,
$$

where $\vec p\tilde q$ is read as an element multiplying $\tilde q$, and the two products agree exactly when the vector part of the first factor annihilates the second,

$$
\tilde p^{\natural}\tilde q=\tilde p\tilde q \quad\Longleftrightarrow\quad \vec p\tilde q=0 .
$$

*Proof.* The two rules differ only in the signs attached to $\vec p\cdot\vec q$, $\vec p\times\vec q$ and $q_0\vec p$, so adding them cancels those terms and leaves $2p_0q_0+2p_0\vec q=2p_0\tilde q$; subtracting them leaves $-2\vec p\cdot\vec q+2q_0\vec p+2\vec p\times\vec q$, which is $2\vec p\tilde q$ by the plain rule read with the vector part alone in the first slot. The agreement condition is the vanishing of the difference.

The identities and the further relations they generate are *Relations Between the Two General Products*, below this article in this category.

## The Multiplication Tables

The two products are determined by their values on the pairs of units, as every bilinear rule is. For the plain product the table is the table of the algebra,

| $\tilde p\backslash\tilde q$ | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
|---|---|---|---|---|
| $e_0$ | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
| $e_1$ | $e_1$ | $-e_0$ | $e_3$ | $-e_2$ |
| $e_2$ | $e_2$ | $-e_3$ | $-e_0$ | $e_1$ |
| $e_3$ | $e_3$ | $e_2$ | $-e_1$ | $-e_0$ |

and for the quaternionic product it is the same table with the entries $e_i^{\natural}e_j$,

| $\tilde p\backslash\tilde q$ | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
|---|---|---|---|---|
| $e_0$ | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
| $e_1$ | $-e_1$ | $e_0$ | $-e_3$ | $e_2$ |
| $e_2$ | $-e_2$ | $e_3$ | $e_0$ | $-e_1$ |
| $e_3$ | $-e_3$ | $-e_2$ | $e_1$ | $e_0$ |

The two tables coincide on the first row and differ by a sign on every entry of the other three rows. The sign is the reflection of the vector part of the first factor, and it is the whole of the difference between the two products beyond the conjugation.

**Proposition (the values of the two products).** The plain product is the multiplication of the associative division algebra, its only nonzero idempotent is $e_0$ and it has no zero divisor. The quaternionic product has the left unit $e_0$ and no right unit, is not associative, and has the same two idempotents $0$ and $e_0$ and no zero divisor.

*Proof.* The plain product is the multiplication of $\mathbb{H}$, an associative division algebra with unit $e_0$; its only idempotents are $0$ and $e_0$ because $p(p-e_0)=0$ forces $p=0$ or $p=e_0$, and there is no zero divisor because every nonzero element is invertible. For the quaternionic product, $e_0^{\natural}\tilde q=e_0\tilde q=\tilde q$ while $\tilde q^{\natural}e_0=\tilde q^{\natural}\neq\tilde q$ for a non-real $\tilde q$, so $e_0$ is a left unit and not a right one; associativity fails on $\tilde p=\tilde q=\tilde r=e_1$, where $(\tilde p^{\natural}\tilde q)^{\natural}\tilde r=(e_1^{\natural}e_1)^{\natural}e_1=e_0^{\natural}e_1=e_1$ while $\tilde p^{\natural}(\tilde q^{\natural}\tilde r)=e_1^{\natural}(e_1^{\natural}e_1)=e_1^{\natural}e_0=-e_1$, and the two sides differ by the sign of $e_1$. The failure is measured by the associator $(\tilde p^{\natural}\tilde q)^{\natural}\tilde r-\tilde p^{\natural}(\tilde q^{\natural}\tilde r)=(\tilde q^{\natural}\tilde p-\tilde p^{\natural}\tilde q^{\natural})\tilde r$ of *The Two General Products and Operators*, below this article in this category. The idempotents of the quaternionic product are computed from $\tilde p^{\natural}\tilde p=|p|^2e_0$, which is real, so $\tilde p^{\natural}\tilde p=\tilde p$ forces $p\in\mathbb{R}$ and $p^2=p$, hence $p=0$ or $p=e_0$. A zero divisor would give $\tilde p^{\natural}\tilde q=0$ with both factors nonzero; taking the norm of $\tilde p^{\natural}\tilde q$ gives $|p|^2|q|^2=0$, so one of the two factors is zero.

The associator of the quaternionic product and the rest of its laws are *Comparison Between the Two General Products* and *The Two General Products and Operators*, both below this article in this category.

## Why Exactly Two Products

The two products are read from one construction: the plain product with the natural conjugation inserted in a slot. The first-slot choice gives the plain and the quaternionic families, $(\mathrm{id},\mathrm{id})$ and $({}^{\natural},\mathrm{id})$; the second-slot choice gives the same two products read with both arguments conjugated, because the base field $\mathbb{R}$ carries no involution other than the identity, so the conjugation in the two slots is the same map ${}^{\natural}$.

$$
(\mathrm{id},{}^{\natural})\ \text{is}\ (\mathrm{id},\mathrm{id})\ \text{read at}\ (\tilde p^{\natural},\tilde q^{\natural}) , \qquad
({}^{\natural},{}^{\natural})\ \text{is}\ ({}^{\natural},\mathrm{id})\ \text{read at}\ (\tilde p^{\natural},\tilde q^{\natural}) .
$$

The count is developed in *The Two General Products and the Reason There Are Only Two*, below this article in this category.

## The Structures the Two Products Define

The two products define the two structures that the whole operational vocabulary of the chapter describes, and no third structure is carried by a general product of $\mathbb{H}$.

| product | structure | commutative | associative | unit |
|---|---|---|---|---|
| $\tilde p\tilde q$ | associative division algebra over $\mathbb{R}$ | no | yes | two-sided, $e_0$ |
| $\tilde p^{\natural}\tilde q$ | quaternionic algebra over $\mathbb{R}$ | no | no | left only, $e_0$ |

The first is the **algebra** $\mathbb{H}$ itself, the quaternion algebra with its multiplication: associative, with the two-sided unit $e_0$, non-commutative, and a division algebra, every nonzero element being invertible. The second is the **quaternionic algebra**, the space with the product of the first slot conjugated: non-associative, non-commutative, with the unit on the left alone. The two have the same underlying real vector space, the same two idempotents and the same absence of zero divisors, and they are told apart by associativity and by the side on which the unit acts. The two structures are read again, with the four structures of the two halves of each, in *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*, below this article in this category.

## Summary

The quaternion space carries two general products, defined on the same coordinates: the general plain bilinear product $\tilde p\tilde q=(p_0q_0-\vec p\cdot\vec q)+p_0\vec q+q_0\vec p+\vec p\times\vec q$, the multiplication of the algebra, and the general quaternionic bilinear product $\tilde p^{\natural}\tilde q=(p_0q_0+\vec p\cdot\vec q)+p_0\vec q-q_0\vec p-\vec p\times\vec q$, the same rule with the first factor conjugated by ${}^{\natural}$. Both are $\mathbb{R}$-bilinear, and their sum and difference separate the scalar part of the first factor from its vector part, $\tilde p\tilde q+\tilde p^{\natural}\tilde q=2p_0\tilde q$ and $\tilde p\tilde q-\tilde p^{\natural}\tilde q=2\vec p\tilde q$. The two multiplication tables coincide on the first row alone and differ by a sign on every entry of the other three rows.

The plain product makes $\mathbb{H}$ an associative division algebra with the two-sided unit $e_0$; the quaternionic product makes $\mathbb{H}$ a left-unital, non-associative quaternionic algebra. The two have the same two idempotents $0$ and $e_0$ and no zero divisor.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | the real quaternion algebra, basis $e_0,e_1,e_2,e_3$ |
| $\tilde q=q_0e_0+\vec q$ | an element, scalar part $q_0$, vector part $\vec q$ |
| $\tilde q^{\natural}=q_0e_0-\vec q$ | the quaternion conjugation |
| $\tilde p\tilde q=(p_0q_0-\vec p\cdot\vec q)+p_0\vec q+q_0\vec p+\vec p\times\vec q$ | the general plain bilinear product |
| $\tilde p^{\natural}\tilde q=(p_0q_0+\vec p\cdot\vec q)+p_0\vec q-q_0\vec p-\vec p\times\vec q$ | the general quaternionic bilinear product |
| $\tilde p\tilde q+\tilde p^{\natural}\tilde q=2p_0\tilde q$ | the separation of the scalar part |
| $\tilde p\tilde q-\tilde p^{\natural}\tilde q=2\vec p\tilde q$ | the separation of the vector part |
| $\tilde p^{\natural}\tilde q=\tilde p\tilde q \iff \vec p\tilde q=0$ | the agreement condition |
| $e_0$ | the two-sided unit of the plain product, the left unit of the quaternionic one |

## Further Reading

- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the quaternion product, its vector reading and the products of the companion real algebras.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the bilinear products of the division algebra $\mathbb{H}$ and the place of the quaternions among the Clifford algebras.
- Israel Nathan Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975), for associativity, units and the division property in a non-commutative ring.
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for algebras over a field, their general products and the laws they may carry.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, Graduate Texts in Mathematics 131, 2nd ed. 2001), for the reading of the quaternions as a division ring and the collapse of the general products over a base with a trivial involution.
