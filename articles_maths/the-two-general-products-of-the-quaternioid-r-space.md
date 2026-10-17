# __The Two General Products of the Quaternioid $\mathbb{R}$ Space__

## Introduction

The quaternion space $\mathbb{H}$ is a four-dimensional real vector space and an associative division algebra, and it carries **two** general products: the **general plain bilinear product** $\tilde q_1\tilde q_2$, the multiplication of the algebra, and the **general quaternionic bilinear product** $\tilde q_1^{\natural}\tilde q_2$, the plain product with the first factor read through the quaternion conjugation ${}^{\natural}$. The base of the quaternion algebra is $\mathbb{R}$, so the only conjugation available is the natural conjugation ${}^{\natural}$ of the element; the pairing that uses it in the second slot returns the two general products read with both arguments conjugated, with the same scalar parts and the same laws, so no new family arises. Exactly two general products are read on $\mathbb{H}$, and this article defines them.

The two products and their two structures are defined here. The identities that link them are *Relations Between the Two General Products*, below this article in this category, and the table of their laws is *Comparison Between the Two General Products*, below this article in this category. The symmetrisation and the antisymmetrisation of the two are *The 6 Products of the Quaternioid Real Space*, and the three companion structures they define are *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*, both below this article in this category. The left and right multiplications of the two are *The Two General Products and Operators*, the reading on the distinguished subspaces is *Remarkable Subspaces and the Two General Products*, and the degree-two reading is *The 2 Forms over the Quaternioid $\mathbb{R}$ Space*, *The 2 Algebraic Norms over the Quaternioid $\mathbb{R}$ Space* and *Remarkable Subspaces and the Two Forms*, all below this article in this category.

**Conventions.** The algebra is $\mathbb{H}$, the real quaternion algebra, with units $e_t=1,\vec e_x,\vec e_y,\vec e_z$, the relations $\vec e_\mu^2=-e_t$ and $\vec e_x \vec e_y=\vec e_z$, $\vec e_y \vec e_z=\vec e_x$, $\vec e_z \vec e_x=\vec e_y$, and the general element $\tilde q=q_te_t+\vec q$, $\vec q=q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$, with real coefficients $q_\mu$. The **dot product** is $\vec q_1\cdot\vec q_2=q_{1x}q_{2x}+q_{1y}q_{2y}+q_{1z}q_{2z}$ and the **cross product** $\vec q_1\times\vec q_2$ is the usual one, $(q_{1y}q_{2z}-q_{1z}q_{2y})\vec e_x+(q_{1z}q_{2x}-q_{1x}q_{2z})\vec e_y+(q_{1x}q_{2y}-q_{1y}q_{2x})\vec e_z$. The **scalar part** is $\mathrm{Sc}(\tilde q)=q_t$ and the **vector part** is $\operatorname{Vect}(\tilde q)=\vec q$. In this article $\tilde q_1$ and $\tilde q_2$ name elements, so that the brackets stay free for the forms.

## The Two Products

**Definition.** The **general plain bilinear product** and the **general quaternionic bilinear product** of the elements $\tilde q_1=q_{1t}e_t+\vec q_1$ and $\tilde q_2=q_{2t}e_t+\vec q_2$ are

$$
\tilde q_1\tilde q_2 = \bigl(q_{1t}q_{2t}-\vec q_1\cdot\vec q_2\bigr) + q_{1t}\vec q_2 + q_{2t}\vec q_1 + \vec q_1\times\vec q_2 ,
$$

$$
\tilde q_1^{\natural}\tilde q_2 = \bigl(q_{1t}q_{2t}+\vec q_1\cdot\vec q_2\bigr) + q_{1t}\vec q_2 - q_{2t}\vec q_1 - \vec q_1\times\vec q_2 .
$$

The first is the product of the algebra, read on the scalar and vector parts of the two elements; the second is the same rule with the first factor read through ${}^{\natural}$, which changes the sign of its vector part alone. The two products are defined on the same pair of coordinates and take their values in the same space, and the two are the **general** products of $\mathbb{H}$ in the sense of the general construction: the plain product with the two slots read as they stand, and the plain product with the first slot conjugated by the only nontrivial involution the element carries.

Both products are $\mathbb{R}$-bilinear, being built from the bilinear operations of the real vector space $\mathbb{H}$: the scalar and vector parts, the dot product and the cross product are all bilinear over $\mathbb{R}$.

**Proposition (the two products separate the scalar and the vector part of the first factor).** For all $\tilde q_1,\tilde q_2$,

$$
\tilde q_1\tilde q_2+\tilde q_1^{\natural}\tilde q_2=2q_{1t}\,\tilde q_2 , \qquad \tilde q_1\tilde q_2-\tilde q_1^{\natural}\tilde q_2=2\,\vec q_1\,\tilde q_2 ,
$$

where $\vec q_1\tilde q_2$ is read as an element multiplying $\tilde q_2$, and the two products agree exactly when the vector part of the first factor annihilates the second,

$$
\tilde q_1^{\natural}\tilde q_2=\tilde q_1\tilde q_2 \quad\Longleftrightarrow\quad \vec q_1\tilde q_2=0 .
$$

*Proof.* The two rules differ only in the signs attached to $\vec q_1\cdot\vec q_2$, $\vec q_1\times\vec q_2$ and $q_{2t}\vec q_1$, so adding them cancels those terms and leaves $2q_{1t}q_{2t}+2q_{1t}\vec q_2=2q_{1t}\tilde q_2$; subtracting them leaves $-2\vec q_1\cdot\vec q_2+2q_{2t}\vec q_1+2\vec q_1\times\vec q_2$, which is $2\vec q_1\tilde q_2$ by the plain rule read with the vector part alone in the first slot. The agreement condition is the vanishing of the difference.

The identities and the further relations they generate are *Relations Between the Two General Products*, below this article in this category.

## The Multiplication Tables

The two products are determined by their values on the pairs of units, as every bilinear rule is. For the plain product the table is the table of the algebra,

| $\tilde q_1\backslash\tilde q_2$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
| $\vec e_x$ | $\vec e_x$ | $-e_t$ | $\vec e_z$ | $-\vec e_y$ |
| $\vec e_y$ | $\vec e_y$ | $-\vec e_z$ | $-e_t$ | $\vec e_x$ |
| $\vec e_z$ | $\vec e_z$ | $\vec e_y$ | $-\vec e_x$ | $-e_t$ |

and for the quaternionic product it is the same table with the entries $e_\mu^{\natural} e_\nu$,

| $\tilde q_1\backslash\tilde q_2$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
| $\vec e_x$ | $-\vec e_x$ | $e_t$ | $-\vec e_z$ | $\vec e_y$ |
| $\vec e_y$ | $-\vec e_y$ | $\vec e_z$ | $e_t$ | $-\vec e_x$ |
| $\vec e_z$ | $-\vec e_z$ | $-\vec e_y$ | $\vec e_x$ | $e_t$ |

The two tables coincide on the first row and differ by a sign on every entry of the other three rows. The sign is the reflection of the vector part of the first factor, and it is the whole of the difference between the two products beyond the conjugation.

**Proposition (the values of the two products).** The plain product is the multiplication of the associative division algebra, its only nonzero idempotent is $e_t$ and it has no zero divisor. The quaternionic product has the left unit $e_t$ and no right unit, is not associative, and has the same two idempotents $0$ and $e_t$ and no zero divisor.

*Proof.* The plain product is the multiplication of $\mathbb{H}$, an associative division algebra with unit $e_t$; its only idempotents are $0$ and $e_t$ because $p(p-e_t)=0$ forces $p=0$ or $p=e_t$, and there is no zero divisor because every nonzero element is invertible. For the quaternionic product, $e_t^{\natural}\tilde q=e_t\tilde q=\tilde q$ while $\tilde q^{\natural}e_t=\tilde q^{\natural}\neq\tilde q$ for a non-real $\tilde q$, so $e_t$ is a left unit and not a right one; associativity fails on $\tilde q_1=\tilde q_2=\tilde q_3=\vec e_x$, where $(\tilde q_1^{\natural}\tilde q_2)^{\natural}\tilde q_3=(\vec e_x^{\natural}\vec e_x)^{\natural}\vec e_x=e_t^{\natural}\vec e_x=\vec e_x$ while $\tilde q_1^{\natural}(\tilde q_2^{\natural}\tilde q_3)=\vec e_x^{\natural}(\vec e_x^{\natural}\vec e_x)=\vec e_x^{\natural}e_t=-\vec e_x$, and the two sides differ by the sign of $\vec e_x$. The failure is measured by the associator $(\tilde q_1^{\natural}\tilde q_2)^{\natural}\tilde q_3-\tilde q_1^{\natural}(\tilde q_2^{\natural}\tilde q_3)=(\tilde q_2^{\natural}\tilde q_1-\tilde q_1^{\natural}\tilde q_2^{\natural})\tilde q_3$ of *The Two General Products and Operators*, below this article in this category. The idempotents of the quaternionic product are computed from $\tilde q^{\natural}\tilde q=|\tilde q|^2e_t$, which is real, so $\tilde q^{\natural}\tilde q=\tilde q$ forces $\tilde q\in\mathbb{R}$ and $\tilde q^2=\tilde q$, hence $\tilde q=0$ or $\tilde q=e_t$. A zero divisor would give $\tilde q_1^{\natural}\tilde q_2=0$ with both factors nonzero; taking the norm of $\tilde q_1^{\natural}\tilde q_2$ gives $|q_1|^2|q_2|^2=0$, so one of the two factors is zero.

The associator of the quaternionic product and the rest of its laws are *Comparison Between the Two General Products* and *The Two General Products and Operators*, both below this article in this category.

## Why Exactly Two Products

The two products are read from one construction: the plain product with the natural conjugation inserted in a slot. The first-slot choice gives the plain and the quaternionic families, $(\mathrm{id},\mathrm{id})$ and $({}^{\natural},\mathrm{id})$; the second-slot choice gives the same two products read with both arguments conjugated, because the base field $\mathbb{R}$ carries no involution other than the identity, so the conjugation in the two slots is the same map ${}^{\natural}$.

$$
(\mathrm{id},{}^{\natural})\ \text{is}\ (\mathrm{id},\mathrm{id})\ \text{read at}\ (\tilde q_1^{\natural},\tilde q_2^{\natural}) , \qquad
({}^{\natural},{}^{\natural})\ \text{is}\ ({}^{\natural},\mathrm{id})\ \text{read at}\ (\tilde q_1^{\natural},\tilde q_2^{\natural}) .
$$

The count is developed in *The Two General Products and the Reason There Are Only Two*, below this article in this category.

## The Structures the Two Products Define

The two products define the two structures that the whole operational vocabulary of the chapter describes, and no third structure is carried by a general product of $\mathbb{H}$.

| product | structure | commutative | associative | unit |
|---|---|---|---|---|
| $\tilde q_1\tilde q_2$ | associative division algebra over $\mathbb{R}$ | no | yes | two-sided, $e_t$ |
| $\tilde q_1^{\natural}\tilde q_2$ | quaternionic algebra over $\mathbb{R}$ | no | no | left only, $e_t$ |

The first is the **algebra** $\mathbb{H}$ itself, the quaternion algebra with its multiplication: associative, with the two-sided unit $e_t$, non-commutative, and a division algebra, every nonzero element being invertible. The second is the **quaternionic algebra**, the space with the product of the first slot conjugated: non-associative, non-commutative, with the unit on the left alone. The two have the same underlying real vector space, the same two idempotents and the same absence of zero divisors, and they are told apart by associativity and by the side on which the unit acts. The two structures are read again, with the four structures of the two halves of each, in *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*, below this article in this category.

## Summary

The quaternion space carries two general products, defined on the same coordinates: the general plain bilinear product $\tilde q_1\tilde q_2=(q_{1t}q_{2t}-\vec q_1\cdot\vec q_2)+q_{1t}\vec q_2+q_{2t}\vec q_1+\vec q_1\times\vec q_2$, the multiplication of the algebra, and the general quaternionic bilinear product $\tilde q_1^{\natural}\tilde q_2=(q_{1t}q_{2t}+\vec q_1\cdot\vec q_2)+q_{1t}\vec q_2-q_{2t}\vec q_1-\vec q_1\times\vec q_2$, the same rule with the first factor conjugated by ${}^{\natural}$. Both are $\mathbb{R}$-bilinear, and their sum and difference separate the scalar part of the first factor from its vector part, $\tilde q_1\tilde q_2+\tilde q_1^{\natural}\tilde q_2=2q_{1t}\tilde q_2$ and $\tilde q_1\tilde q_2-\tilde q_1^{\natural}\tilde q_2=2\vec q_1\tilde q_2$. The two multiplication tables coincide on the first row alone and differ by a sign on every entry of the other three rows.

The plain product makes $\mathbb{H}$ an associative division algebra with the two-sided unit $e_t$; the quaternionic product makes $\mathbb{H}$ a left-unital, non-associative quaternionic algebra. The two have the same two idempotents $0$ and $e_t$ and no zero divisor.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | the real quaternion algebra, basis $e_t,\vec e_x,\vec e_y,\vec e_z$ |
| $\tilde q=q_te_t+\vec q$ | an element, scalar part $q_t$, vector part $\vec q$ |
| $\tilde q^{\natural}=q_te_t-\vec q$ | the quaternion conjugation |
| $\tilde q_1\tilde q_2=(q_{1t}q_{2t}-\vec q_1\cdot\vec q_2)+q_{1t}\vec q_2+q_{2t}\vec q_1+\vec q_1\times\vec q_2$ | the general plain bilinear product |
| $\tilde q_1^{\natural}\tilde q_2=(q_{1t}q_{2t}+\vec q_1\cdot\vec q_2)+q_{1t}\vec q_2-q_{2t}\vec q_1-\vec q_1\times\vec q_2$ | the general quaternionic bilinear product |
| $\tilde q_1\tilde q_2+\tilde q_1^{\natural}\tilde q_2=2q_{1t}\tilde q_2$ | the separation of the scalar part |
| $\tilde q_1\tilde q_2-\tilde q_1^{\natural}\tilde q_2=2\vec q_1\tilde q_2$ | the separation of the vector part |
| $\tilde q_1^{\natural}\tilde q_2=\tilde q_1\tilde q_2 \iff \vec q_1\tilde q_2=0$ | the agreement condition |
| $e_t$ | the two-sided unit of the plain product, the left unit of the quaternionic one |

## Further Reading

- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the quaternion product, its vector reading and the products of the companion real algebras.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the bilinear products of the division algebra $\mathbb{H}$ and the place of the quaternions among the Clifford algebras.
- Israel Nathan Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975), for associativity, units and the division property in a non-commutative ring.
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for algebras over a field, their general products and the laws they may carry.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, Graduate Texts in Mathematics 131, 2nd ed. 2001), for the reading of the quaternions as a division ring and the collapse of the general products over a base with a trivial involution.
