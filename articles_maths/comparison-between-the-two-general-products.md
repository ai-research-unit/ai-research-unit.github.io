# __Comparison Between the Two General Products__

## Introduction

The two general products of the quaternion space are defined independently in *The Two General Products of the Quaternioid $\mathbb{R}$ Space*, and it is natural to ask which of them deserves the name of multiplication and how the two are told apart. In the strict sense, of an associative multiplication with a two-sided unit over the field of scalars, only the general plain product does: the quaternionic product is $\mathbb{R}$-bilinear but neither associative nor two-sidedly unital.

This article tabulates the properties that separate the two products — bilinearity, associativity, the unit, commutativity, the square, the values and the radical — and gives the short computation that decides each entry where it is not immediate.

The article assumes the two products and their coordinate rules from *The Two General Products of the Quaternioid $\mathbb{R}$ Space*, the article preceding this one, and it uses the linking identities of *Relations Between the Two General Products*, the article preceding this one, for the unit and the square rows. The left and right multiplications and the associator are *The Two General Products and Operators*, below this article in this category.

## The Property Table

| property | $\tilde q_1\tilde q_2$ | $\tilde q_1^{\natural}\tilde q_2$ |
|---|---|---|
| $\mathbb{R}$-linear in the first argument | yes | yes |
| $\mathbb{R}$-linear in the second argument | yes | yes |
| associative | yes | no |
| commutative | no | no |
| $e_t$ is a left identity | yes | yes |
| $e_t$ is a right identity | yes | no |
| the square $\tilde q^2$ | $\langle\tilde q\rangle e_t+2q_t\vec q$ | $\langle\tilde q\rangle_{\natural} e_t$, scalar |
| the values on the units | $\vec e_x \vec e_y=\vec e_z$, $\vec e_x^2=-e_t$ | $\vec e_x^{\natural} \vec e_y=-\vec e_z$, $\vec e_x^{\natural} \vec e_x=e_t$ |
| the radical | $\{0\}$ | $\{0\}$ |

The last row is the **radical** of the product, the set of elements annihilating the whole space on both sides, $\{x:f(x,y)=0=f(y,x)\ \text{for every}\ y\}$; it is the same for the two products and it is the zero subspace, the algebra being a division algebra and the quaternionic product having no zero divisor. The rows for the square read $\langle\tilde q\rangle=q_t^2-\lvert\vec q\rvert^2$ and $\langle\tilde q\rangle_{\natural}=\lvert\tilde q\rvert^2$; the two algebraic norms are *The 2 Algebraic Norms over the Quaternioid $\mathbb{R}$ Space*, below this article in this category.

## Bilinearity

The first four rows are read off the definitions. Each product is $\mathbb{R}$-linear in each argument: the rule is built from the scalar and vector parts of the two factors, the dot product and the cross product, and each of these is bilinear over $\mathbb{R}$; the conjugation ${}^{\natural}$ acts on the first factor alone and is itself $\mathbb{R}$-linear, and it changes the sign of the vector part and of nothing else.

## Associativity and the Two-Sided Unit

**Theorem (the classification).** Among the two general products, the general plain bilinear product is the only associative one and the only one with a two-sided unit; the general quaternionic bilinear product is neither.

*Proof.* The plain product is the multiplication of $\mathbb{H}$, an associative algebra with two-sided unit $e_t$. For the quaternionic product, $e_t^{\natural}\tilde q=e_t\tilde q=\tilde q$ shows that $e_t$ is a left identity, while $\tilde q^{\natural} e_t=\tilde q^{\natural}$, which equals $\tilde q$ only for a real $\tilde q$, shows that $e_t$ is not a right identity; and a right identity $E$ would give $\tilde q^{\natural}E=\tilde q$ for every $\tilde q$, hence $E=e_t$ on taking $\tilde q=e_t$ and then $\tilde q^{\natural}=\tilde q$ for every $\tilde q$, which is false. Associativity fails on the triple $\tilde q_1=\tilde q_2=\tilde q_3=\vec e_x$, where

$$
(\tilde q_1^{\natural}\tilde q_2)^{\natural}\tilde q_3=(\vec e_x^{\natural} \vec e_x)^{\natural} \vec e_x=e_t^{\natural} \vec e_x=\vec e_x , \qquad \tilde q_1^{\natural}(\tilde q_2^{\natural}\tilde q_3)=\vec e_x^{\natural}(\vec e_x^{\natural} \vec e_x)=\vec e_x^{\natural} e_t=-\vec e_x ,
$$

the two sides differing by the sign of $\vec e_x$.

So the two products are separated by associativity and by the unit at once, and the two failures have one cause: the quaternionic product conjugates its first factor, the conjugation transposes the two factors when a product is conjugated, and the transposition is what the parenthesis cannot absorb. The associator of the quaternionic product is computed in full in *The Two General Products and Operators*, below this article in this category, where it is shown to be $(\tilde q_2^{\natural}\tilde q_1-\tilde q_1^{\natural}\tilde q_2^{\natural})\tilde q_3$.

## Commutativity

Neither product is commutative. For the plain product the failure is the failure of the quaternion algebra to be commutative, witnessed on $(\tilde q_1,\tilde q_2)=(\vec e_x,\vec e_y)$, where $\vec e_x \vec e_y=\vec e_z$ and $\vec e_y \vec e_x=-\vec e_z$. For the quaternionic product the two values on the same pair are $\tilde q_1^{\natural}\tilde q_2=-\vec e_z$ and $\tilde q_2^{\natural}\tilde q_1=\vec e_z$, again opposite; the two products are related by the exchange relation $\tilde q_2^{\natural}\tilde q_1=(\tilde q_1^{\natural}\tilde q_2)^{\natural}$ of *Relations Between the Two General Products*, the article preceding this one, and the exchange is not the identity, so neither is commutative. The anticommutation of the units $\vec e_x,\vec e_y$ is thus common to the two products, the sign of the disagreement coming from the conjugation and not from the order alone.

## The Square

The square of the plain product is a general quaternion and the square of the quaternionic product is always a scalar, and this is the sharpest single difference between the two products at the two equal arguments.

**Proposition (the two squares).** For every $\tilde q=q_te_t+\vec q$,

$$
\boxed{\;\tilde q^2=\langle\tilde q\rangle e_t+2q_t\vec q , \qquad \tilde q^{\natural}\tilde q=\langle\tilde q\rangle_{\natural} e_t=|\tilde q|^2e_t\;},
$$

with $\langle\tilde q\rangle=q_t^2-\lvert\vec q\rvert^2$ and $\langle\tilde q\rangle_{\natural}=q_t^2+\lvert\vec q\rvert^2$. The square of the plain product is scalar exactly when $\tilde q$ is real or $\tilde q$ is purely imaginary with $q_t=0$; the square of the quaternionic product is scalar for every $\tilde q$.

*Proof.* Expanding the plain product on a single element, $(\vec q)^2=-\lvert\vec q\rvert^2e_t$ and $\vec q\times\vec q=0$, so $\tilde q^2=q_t^2e_t+2q_t\vec q+\vec q^2=(q_t^2-\lvert\vec q\rvert^2)e_t+2q_t\vec q$. The quaternionic square is $\tilde q^{\natural}\tilde q$, which is the product of the conjugate with the element, equal to $\lvert\tilde q\rvert^2e_t$ by the multiplicativity of the norm; and the vector part $2q_t\vec q$ of the plain square vanishes exactly when $q_t=0$ or $\vec q=0$.

The two squares are the two algebraic norms of the chapter read at the two equal arguments, and the fact that one is scalar and the other is not is the reason the plain product has no invertibility criterion in the norm while the quaternionic product does; the norms, their multiplicativity and their invertibility criteria are *The 2 Algebraic Norms over the Quaternioid $\mathbb{R}$ Space*, below this article in this category.

## The Values

The two products take all values in $\mathbb{H}$, each being surjective: for a fixed nonzero second factor $\tilde q_2$ the rule $\tilde q_1\mapsto\tilde q_1\tilde q_2$ is a bijection of $\mathbb{H}$, the algebra being a division algebra, and the same holds for the quaternionic rule. The two differ in their **values on the units**, and the difference is a sign on every pair except those of the first row. On the basis pairs,

$$
\boxed{\;\vec e_x \vec e_y=\vec e_z \quad\text{against}\quad \vec e_x^{\natural} \vec e_y=-\vec e_z , \qquad \vec e_x^2=-e_t \quad\text{against}\quad \vec e_x^{\natural} \vec e_x=e_t\;},
$$

and in general $\vec e_\mu^{\natural} e_\nu=-\vec e_\mu e_\nu$ for every pair with $\mu\neq t$, the sign being that of the reflection of the vector part of the first factor. The values on the pairs with a real first factor coincide, $e_t\tilde q=e_t^{\natural}\tilde q=\tilde q$, and the values on the pairs with a real second factor disagree unless the first factor is real as well, by the annihilation identity of *Relations Between the Two General Products*, the article preceding this one.

## The Radical

**Proposition (the radical of each product is zero).** For each of the two products the set of elements annihilating the whole space on the left and on the right is $\{0\}$.

*Proof.* For the plain product, $\tilde q_1\tilde q_2=0$ for every $\tilde q_2$ forces $\tilde q_1=0$ on taking $\tilde q_2=e_t$ and using that $\mathbb{H}$ is a division algebra; the same for $\tilde q_2\tilde q_1=0$. For the quaternionic product, $\tilde q_1^{\natural}\tilde q_2=0$ for every $\tilde q_2$ forces $\tilde q_1^{\natural}=0$ on taking $\tilde q_2=e_t$, hence $\tilde q_1=0$, and $\tilde q_2^{\natural}\tilde q_1=0$ for every $\tilde q_2$ forces $\tilde q_1=0$ on taking $\tilde q_2=e_t$.

So neither product has a nonzero annihilator, and both are **nondegenerate** in the sense of the radical. This is the same statement as the absence of zero divisors of the two products, and it separates the two from the antisymmetric plain product of *The 6 Products of the Quaternioid Real Space*, below this article in this category, which alone among the six has a nonzero radical: the cross product $\tilde q_1\wedge\tilde q_2$ annihilates the whole scalar line on both sides, so its radical is the line of the scalars, while the other five products, the two general ones and the four halves other than the cross product, have radical $\{0\}$.

## Summary

The comparison of the two general products of $\mathbb{H}$ is the table with the rows bilinearity, associativity, the unit, commutativity, the square, the values and the radical. The general plain product is $\mathbb{R}$-bilinear in each slot, associative, non-commutative, with the two-sided unit $e_t$, with the square $\tilde q^2=(q_t^2-\lvert\vec q\rvert^2)e_t+2q_t\vec q$, and the radical $\{0\}$. The general quaternionic product is $\mathbb{R}$-bilinear in each slot, non-associative, non-commutative, with the left unit $e_t$ and no right one, with the scalar square $\tilde q^{\natural}\tilde q=\lvert\tilde q\rvert^2e_t$, and the radical $\{0\}$.

The classification isolates the general plain product as the only associative and two-sidedly unital one of the two, and hence as the only multiplication of an associative unital algebra over $\mathbb{R}$. The two products agree on the pairs with a real first factor and disagree elsewhere, and on the units they differ by a sign on every pair except those.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde q_1\tilde q_2$ | the general plain bilinear product |
| $\tilde q_1^{\natural}\tilde q_2$ | the general quaternionic bilinear product |
| $\langle\tilde q\rangle=q_t^2-\lvert\vec q\rvert^2$ | the value on the square of the plain product |
| $\langle\tilde q\rangle_{\natural}=q_t^2+\lvert\vec q\rvert^2$ | the value on the square of the quaternionic product |
| $\{x:f(x,y)=0=f(y,x)\ \forall y\}=\{0\}$ | the radical of each product |
| $e_t$ | two-sided unit for the plain product, left unit for the quaternionic one |
| $(\tilde q_1^{\natural}\tilde q_2)^{\natural}\tilde q_3-\tilde q_1^{\natural}(\tilde q_2^{\natural}\tilde q_3)=(\tilde q_2^{\natural}\tilde q_1-\tilde q_1^{\natural}\tilde q_2^{\natural})\tilde q_3$ | the associator of the quaternionic product |

## Further Reading

- Israel Nathan Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975), for associativity, units and commutativity in a non-commutative ring.
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for the classification of a bilinear rule by its laws and for the multiplication of an algebra over a field.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, Graduate Texts in Mathematics 131, 2nd ed. 2001), for the radical of an algebra and the absence of a nonzero annihilator.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the quaternion product and its companion products on the same space.
