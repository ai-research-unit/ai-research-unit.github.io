# __Square Roots of Minus One, Zero and Plus One in the General Quaternionic Algebra__

## Introduction

The square in the general quaternionic algebra of *Introduction to the General Quaternionic Algebra of Quaternions* is not the plain square: it is the square read in the product of the block,

$$
\tilde\xi \star \tilde\xi = \tilde\xi^{\natural}\tilde\xi = N(\tilde\xi)e_0 ,
$$

where $N$ is the quaternionic bilinear algebraic norm (*Norm and Invertibility in the General Quaternionic Algebra*). This article solves the equation

$$
\tilde\xi \star \tilde\xi = \lambda e_0 , \qquad \lambda \in \{-1, 0, +1\} ,
$$

for the three distinguished central values, and compares the three root sets with those of the plain product on the same space. The general problem, with an arbitrary element on the right, is *Square Roots of a General Element in the General Quaternionic Algebra*, below this article in this category; the three values here are the specialisation of it, and they are read first because they are the ones the chapter compares elsewhere.

The whole article rests on one observation, and it is the observation that makes the block differ from the plain one: for the quaternionic product the square of an element is always the central element $N(\tilde\xi)e_0$. The square map is therefore not a map of $\mathbb{H}$ into itself but a map of $\mathbb{H}$ onto the scalar line, and the equation above is nothing but the norm equation $N(\tilde\xi) = \lambda$.

## The Reduction of the Equation

**Definition.** A **root of the central value** $\lambda$ for the quaternionic product is an element $\tilde\xi$ with $\tilde\xi \star \tilde\xi = \lambda e_0$. The root glyph is the lower-case xi $\tilde\xi$, the one of the quaternion layer.

**Theorem (the reduction).** For $\tilde\xi \in \mathbb{H}$ the square in the quaternionic product is the central element

$$
\tilde\xi \star \tilde\xi = N(\tilde\xi)e_0 = \bigl(\xi_0^2 + \xi_1^2 + \xi_2^2 + \xi_3^2\bigr)e_0 .
$$

Consequently $\tilde\xi$ is a root of $\lambda$ exactly when $N(\tilde\xi) = \lambda$, and the three root sets are the three level sets of the norm:

$$
\{\tilde\xi : \tilde\xi \star \tilde\xi = \lambda e_0\} = \{\tilde\xi : N(\tilde\xi) = \lambda\} .
$$

*Proof.* The square is $\tilde\xi^{\natural}\tilde\xi$ and the conjugate commutes with the element inside this product, so the value is the norm, a real scalar; the scalar equation $N(\tilde\xi)e_0 = \lambda e_0$ is the coordinate equation $N(\tilde\xi) = \lambda$.

**Remark.** The equation is *not* equivalent to a pair of a scalar and a vector equation here, because its left-hand side has no vector part at all. This is the first place where the block separates from the plain algebra, where the same equation splits into the scalar equation $\xi_0^2 - N(\boldsymbol\xi) = \lambda$ and the vector equation $2\xi_0\boldsymbol\xi = 0$ (*Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*).

## The Three Root Sets

**Theorem (the three values).** For the quaternionic product on $\mathbb{H}$:

1. the roots of $-1$ are **absent**: no $\tilde\xi$ satisfies $N(\tilde\xi) = -1$;
2. the root of $0$ is **unique**: $\tilde\xi \star \tilde\xi = 0$ exactly for $\tilde\xi = 0$;
3. the roots of $+1$ are the elements of the norm-one level set, $\{\tilde\xi : N(\tilde\xi) = 1\}$, a set of real dimension three in $\mathbb{H} \cong \mathbb{R}^4$.

*Proof.* Over $\mathbb{R}$ the norm is positive definite (*Norm and Invertibility in the General Quaternionic Algebra*): it takes its values in the non-negative reals, it vanishes only at $0$, and it takes the value $1$ on a level set of a non-degenerate quadratic form in four variables, which has real dimension three.

**Corollary (the criterion and the count).** The equation $\tilde\xi \star \tilde\xi = \lambda e_0$ has a root exactly when $\lambda \geq 0$. For $\lambda > 0$ the root set is the level set $N = \lambda$, of real dimension three; for $\lambda = 0$ it is the single element $0$; for $\lambda < 0$ it is empty.

*Proof.* The norm is non-negative and its sublevel sets are the values it takes; the level set of a definite quadratic form at a positive value is three-dimensional, and at zero it is the origin alone.

**Remark.** The count is the extreme case of the general theory: for the quaternionic product on a real division algebra the square map collapses a four-dimensional space onto the half-line, so a positive value has a three-dimensional root set, the value zero has one root, and a negative value has none. Nothing is left of the two-element root set that the commutative degree-two case would suggest.

## Comparison with the Plain Product

The same three values, solved in the plain product $\tilde\xi^2$ of the same space, give the classical answers (*Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*).

| value $\lambda$ | quaternionic $\tilde\xi \star \tilde\xi$ | plain $\tilde\xi^2$ |
|---|---|---|
| $-1$ | no root | the pure elements with $N = 1$, of real dimension two |
| $0$ | $\{0\}$ alone | $\{0\}$ alone |
| $+1$ | the level set $N = 1$, of real dimension three | $\{\pm e_0\}$ alone |

**Proposition.** The two root sets of $-1$ are as different as they can be: the plain equation has a two-dimensional family of roots, the pure elements of norm one, and the quaternionic equation has none. The two root sets of $+1$ are exchanged in the same way: the plain equation has two roots, $\pm e_0$, and the quaternionic equation has the whole three-dimensional norm-one level set.

*Proof.* The plain square forces $2\xi_0\boldsymbol\xi = 0$, hence a pure root, and then $N(\boldsymbol\xi) = 1$ for the value $+1$ and $N(\boldsymbol\xi) = 1$ for the value $-1$; the quaternionic square is the norm by the reduction above, so its root sets are the level sets computed in the preceding section.

**Remark (the root of $+1$ and the units).** The quaternionic root set of $+1$ is exactly the norm-one shell $N = 1$, which is the unit group of the *plain* algebra; so the roots of $+1$ in this block are the units of the other block, and the two readings meet at the norm. The roots of $-1$ in this block are empty for the same reason that the norm is definite, and the emptiness is the algebraic statement that $\mathbb{H}$ has no element whose quaternionic square is $-e_0$, in sharp contrast with the plain square, which has a two-parameter family of such elements.

## Summary

For the quaternionic product the square of an element is always central, $\tilde\xi \star \tilde\xi = N(\tilde\xi)e_0$, so the equation $\tilde\xi \star \tilde\xi = \lambda e_0$ is the norm equation $N(\tilde\xi) = \lambda$. Over $\mathbb{R}$ the norm is definite, so the roots of $-1$ are absent, the root of $0$ is the single element $0$, and the roots of $+1$ are the norm-one level set, a set of real dimension three. The criterion is that a root exists exactly for $\lambda \geq 0$, with a three-dimensional root set for $\lambda > 0$ and the single root $0$ for $\lambda = 0$. The plain product on the same space gives the mirror-image answers: for the plain square the roots of $-1$ fill the pure elements of norm one, a two-dimensional set, and the roots of $+1$ are the two central elements $\pm e_0$; the two equations exchange their behaviour, and the exchange is the difference between the plain and the quaternionic product.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde\xi \star \tilde\xi = \tilde\xi^{\natural}\tilde\xi = N(\tilde\xi)e_0$ | the square in the quaternionic product |
| $N$ | the quaternionic bilinear algebraic norm |
| $\{\tilde\xi : N(\tilde\xi) = \lambda\}$ | the root set of the central value $\lambda$ |
| $\lambda \in \{-1,0,+1\}$ | the three distinguished central values |
| $\tilde\xi^2$ | the plain square, for contrast |

## Further Reading

- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the families of roots of $\pm1$ in the quaternion and octonion algebras.
- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the origin of the sphere of square roots of $-1$.
- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the equation of a square root of a central value in a nonassociative algebra.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the collapse of the square map of a product whose symmetrisation is scalar-valued.
