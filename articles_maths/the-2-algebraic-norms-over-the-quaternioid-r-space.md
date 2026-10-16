# __The 2 Algebraic Norms over the Quaternioid $\mathbb{R}$ Space__

## Introduction

The two forms of *The 2 Forms over the Quaternioid $\mathbb{R}$ Space* are the scalar parts of the two general products, and their **algebraic norms** are the **two algebraic norms** of the chapter:

$$
\langle\tilde p\rangle=\langle\tilde p,\tilde p\rangle=p_0^2-\lvert\vec p\rvert^2 , \qquad \langle\tilde p\rangle_{\natural}=\langle\tilde p,\tilde p\rangle_{\natural}=p_0^2+\lvert\vec p\rvert^2 .
$$

The **plain algebraic norm** is the plain form read at its two equal arguments, $\langle\tilde p\rangle=p_0^2-\lvert\vec p\rvert^2$, and the **quaternion algebraic norm** is the quaternion form read at its two equal arguments, $\langle\tilde p\rangle_{\natural}=p_0^2+\lvert\vec p\rvert^2$. The first is **indefinite**: it is $+1$ at $e_0$ and $-1$ at $e_1$, so it is of both signs. The second is **positive definite** and vanishes only at the origin. Read on the products, the two are the coefficients of the two squares, $\tilde p\tilde p=\langle\tilde p\rangle e_0+2p_0\vec p$ and $\tilde p^{\natural}\tilde p=\langle\tilde p\rangle_{\natural}e_0$. The two norms are read off the two forms, the first from the plain form and the second from the quaternion form.

This article gives the two norms, the **multiplicativity** of the second and the failure of the first, the **norm of a product against the product of the norms**, the **level sets** read algebraically, and the **invertibility criteria** the two give. It assumes the two forms from *The 2 Forms over the Quaternioid $\mathbb{R}$ Space* and the two squares from *Comparison Between the Two General Products*, both preceding this one; the norms read on the two remarkable subspaces are *Remarkable Subspaces and the Two Algebraic Norms*, below this article in this category; and the theory of the norm and the invertibility of the plain product is owned by *Norm and Invertibility in the Quaternion Algebra*, in the *Quaternions* category.

**Conventions.** Throughout, $\tilde p=p_0e_0+\vec p$ and $\tilde q=q_0e_0+\vec q$ name elements, $(\vec p,\vec q)$ is the dot product of the vector parts, and $\tilde p^{\natural}=p_0e_0-\vec p$. The two algebraic norms are the two forms read at their two equal arguments, $\langle\tilde p\rangle=p_0^2-\lvert\vec p\rvert^2$ and $\langle\tilde p\rangle_{\natural}=p_0^2+\lvert\vec p\rvert^2$, written with the one bracket and the subscript of the pair, the plain and the quaternionic; read on the products they are the coefficients of the two squares, $\tilde p\tilde p=\langle\tilde p\rangle e_0+2p_0\vec p$ and $\tilde p^{\natural}\tilde p=\langle\tilde p\rangle_{\natural}e_0$.

## The Two Norms

**Definition.** The two algebraic norms are the two forms read at their two equal arguments,

$$
\langle\tilde p\rangle=\langle\tilde p,\tilde p\rangle , \qquad \langle\tilde p\rangle_{\natural}=\langle\tilde p,\tilde p\rangle_{\natural} ,
$$

and on the coordinates

$$
\langle\tilde p\rangle=p_0^2-\lvert\vec p\rvert^2 , \qquad \langle\tilde p\rangle_{\natural}=p_0^2+\lvert\vec p\rvert^2 .
$$

The plain norm is **indefinite**, of both signs, and the quaternion norm is **positive definite**, zero only at the origin. Read on the products, the two squares are $\tilde p\tilde p=\langle\tilde p\rangle e_0+2p_0\vec p$, a general element of $\mathbb{H}$ whose scalar coefficient is the plain norm, and $\tilde p^{\natural}\tilde p=\langle\tilde p\rangle_{\natural}e_0$, a central element whose coefficient is the quaternion norm.

## Multiplicativity

**Theorem (multiplicativity of the quaternion norm; failure of the plain one).** For all $\tilde p,\tilde q$,

$$
\langle\tilde p\tilde q\rangle_{\natural}=\langle\tilde p\rangle_{\natural}\langle\tilde q\rangle_{\natural} , \qquad \text{equivalently}\qquad \bigl(\tilde p\tilde q\bigr)^{\natural}\bigl(\tilde p\tilde q\bigr)=\tilde p^{\natural}\tilde p\,\tilde q^{\natural}\tilde q ,
$$

while the plain norm is not multiplicative:

$$
\langle\tilde p\tilde q\rangle\neq \langle\tilde p\rangle\langle\tilde q\rangle \quad\text{in general} , \qquad \bigl(e_1e_2\bigr)^{2}=-e_0 , \quad e_1^{2}e_2^{2}=e_0 .
$$

*Proof.* The quaternion norm is the scalar coefficient of the product of the element with its quaternion conjugate, $\langle\tilde p\rangle_{\natural}=\mathrm{Sc}\bigl(\tilde p^{\natural}\tilde p\bigr)$, and the conjugation is an anti-automorphism, so $\bigl(\tilde p\tilde q\bigr)^{\natural}\bigl(\tilde p\tilde q\bigr)=(\tilde p\tilde q)^{\natural}\tilde p\tilde q=\tilde q^{\natural}\tilde p^{\natural}\tilde p\tilde q=\tilde q^{\natural}|\tilde p|^2\tilde q=|\tilde p|^2|\tilde q|^2e_0$, the scalar $|\tilde p|^2$ commuting with every element; reading the scalar coefficient gives the multiplicativity. For the plain norm, the value of $\tilde p\tilde q\tilde p\tilde q$ is the square of the product and the two factors' squares do not determine it: at $\tilde p=e_1,\tilde q=e_2$ the product is $e_3$, of square $-e_0$, while the product of the squares is $(-e_0)(-e_0)=e_0$, so the plain norm of the product differs from the product of the plain norms.

So the quaternion norm is **multiplicative**: the norm of a product is the product of the norms, and the quaternion norm is the reduced norm of the algebra, the square root of the determinant of the regular representation. The plain norm is not multiplicative, and this is the reason it is called a norm rather than the norm of the algebra: the plain product fails associativity in no way, but its *algebraic norm* is not a multiplicative function. The multiplicativity of the quaternion norm is the algebra's composition law for the four-square identity.

## The Norm of a Product Against the Product of the Norms

**Corollary (the two comparisons).** For all $\tilde p,\tilde q$,

$$
\langle\tilde p\tilde q\rangle_{\natural}=\langle\tilde p\rangle_{\natural}\langle\tilde q\rangle_{\natural} , \qquad \text{equivalently}\qquad \bigl(\tilde p\tilde q\bigr)^{\natural}\bigl(\tilde p\tilde q\bigr)=\tilde p^{\natural}\tilde p\,\tilde q^{\natural}\tilde q ,
$$

the quaternion norm of a product being exactly the product of the quaternion norms; and the plain norm of a product is not the product of the plain norms, the two squares differing by the commutator, $(\tilde p\tilde q)^2-\tilde p^2\tilde q^2=\tilde p[\tilde q,\tilde p]\tilde q$. The quaternion norm of the product is the same in the two orders, $\langle\tilde p\tilde q\rangle_{\natural}=\langle\tilde q\tilde p\rangle_{\natural}$, both being the value of the quaternion form on the product.

*Proof.* The first identity is the multiplicativity theorem. For the second, the plain square of the product is $(\tilde p\tilde q)^2$ and the product of the plain squares is $\tilde p^2\tilde q^2$, the two differing by $\tilde p[\tilde q,\tilde p]\tilde q$; at $\tilde p=e_1,\tilde q=e_2$ the two values are $-e_0$ and $+e_0$. For the third, $\langle\tilde p\tilde q\rangle_{\natural}=|\tilde p\tilde q|^2=|\tilde p|^2|\tilde q|^2=|\tilde q|^2|\tilde p|^2=\langle\tilde q\tilde p\rangle_{\natural}$, the coefficient being a real number.

So the quaternion norm is insensitive to the order of the factors and to the nesting of a product, while the plain norm is sensitive to both; the quaternion norm is the one that behaves as a **norm of an algebra**, and it is the one used in the invertibility criterion.

## The Level Sets

**Definition.** A **level set** of a norm is the set of elements on which that norm takes a fixed value, $\langle\tilde p\rangle=c$ or $\langle\tilde p\rangle_{\natural}=c$ for a real $c$; the level sets are read algebraically, each being cut out by the equation on the coordinates.

**Proposition (the level sets of the two norms).**

*The quaternion norm.* For a real value $c$, $\langle\tilde p\rangle_{\natural}=c$ is the **three-sphere** $p_0^2+\lvert\vec p\rvert^2=c$ of radius $\sqrt c$ when $c>0$, the origin alone when $c=0$, and is empty when $c<0$.

*The plain norm.* For a real value $c$, $\langle\tilde p\rangle=c$ reads $p_0^2-\lvert\vec p\rvert^2=c$: a **two-sheeted hyperboloid** about the scalar axis when $c>0$, a **one-sheeted hyperboloid** when $c<0$, and the **isotropic cone** $p_0^2=\lvert\vec p\rvert^2$ when $c=0$.

*Proof.* The two equations are the two forms read at their two equal arguments. The quaternion equation is the sphere of radius $\sqrt c$ in the four coordinates, empty for $c<0$. The plain equation is the level set of the quadratic form $p_0^2-\lvert\vec p\rvert^2$, of signature $(1,3)$: a two-sheeted hyperboloid for a positive value, a one-sheeted hyperboloid for a negative one, and the cone for the vanishing value.

So the level sets of the two norms are of different shapes: the quaternion norm cuts the space into concentric three-spheres, cut by the origin and empty for the negative values; the plain norm cuts it into the hyperboloids of the form of signature $(1,3)$, with the **isotropic cone** as its zero level set. In particular the elements of unit quaternion norm form the **unit three-sphere** of the four coordinates, and the nonzero elements of zero plain norm are the generators of the cone, of the form $e_0\pm\hat u$ with $(\hat u,\hat u)=1$, which are the isotropic elements of the plain form.

## The Invertibility Criteria

**Theorem (the criterion).** An element $\tilde p$ is invertible in the plain algebra if and only if $\langle\tilde p\rangle_{\natural}\neq0$, that is $\tilde p\neq0$; and then $\tilde p^{-1}=\tilde p^{\natural}/\lvert\tilde p\rvert^2$. The plain norm $\langle\tilde p\rangle$ gives no criterion of this kind: it is not multiplicative, and it vanishes at the nonzero invertible element $e_0+e_1$, so the invertibility of a product cannot be tested on the plain norm.

*Proof.* The identity $\tilde p^{\natural}\tilde p=\langle\tilde p\rangle_{\natural}e_0$ shows that a nonzero $\tilde p$ has the inverse $\tilde p^{\natural}/\lvert\tilde p\rvert^2$, and a zero divisor would give $\langle\tilde p\rangle_{\natural}\langle\tilde q\rangle_{\natural}=0$ with both factors nonzero, impossible; so $\tilde p$ is invertible exactly when $\langle\tilde p\rangle_{\natural}\neq0$, that is exactly when $\tilde p\neq0$, and the criterion is the quaternion norm's. At $\tilde p=e_0+e_1$ the plain norm is $\langle\tilde p\rangle=0$ while the quaternion norm is $\langle\tilde p\rangle_{\natural}=2$ and the element is invertible, so the vanishing of the plain norm decides nothing; the criterion is therefore the quaternion norm's alone.

So the **quaternion norm is the norm of the algebra**: it is real-valued, definite and multiplicative, and its vanishing gives the invertibility criterion and the division property; the plain norm is the algebraic norm of the plain product and is a norm only in the weak sense of the corpus's vocabulary.

## Summary

The quaternion space carries two algebraic norms, the plain norm $\langle\tilde p\rangle=p_0^2-\lvert\vec p\rvert^2$ and the quaternion norm $\langle\tilde p\rangle_{\natural}=p_0^2+\lvert\vec p\rvert^2$, the two forms read at their two equal arguments, the first from the plain form and the second from the quaternion form. The first is indefinite, taking $+1$ and $-1$ at $e_0$ and $e_1$; the second is positive definite, zero only at the origin. The second is multiplicative, $\langle\tilde p\tilde q\rangle_{\natural}=\langle\tilde p\rangle_{\natural}\langle\tilde q\rangle_{\natural}$, and the first is not, $\langle\tilde p\tilde q\rangle\neq\langle\tilde p\rangle\langle\tilde q\rangle$ in general; read on the squares, the witness is $\bigl(e_1e_2\bigr)^{2}=-e_0$ against $e_1^{2}e_2^{2}=e_0$. The quaternion norm of a product equals the product of the quaternion norms and does not depend on the order, while the plain norm of a product is not the product of the plain norms.

The level sets of the quaternion norm are the three-spheres, cut by the origin and empty for the negative values; those of the plain norm are the hyperboloids of the form of signature $(1,3)$, with the isotropic cone as the zero level set. The invertibility criterion is the quaternion norm's: $\tilde p$ is invertible exactly when $\langle\tilde p\rangle_{\natural}\neq0$, with inverse $\tilde p^{\natural}/\lvert\tilde p\rvert^2$; the plain norm gives no criterion, vanishing at the nonzero element $e_0+e_1$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\tilde p\rangle=\langle\tilde p,\tilde p\rangle=p_0^2-\lvert\vec p\rvert^2$ | the plain algebraic norm, indefinite |
| $\langle\tilde p\rangle_{\natural}=\langle\tilde p,\tilde p\rangle_{\natural}=p_0^2+\lvert\vec p\rvert^2$ | the quaternion algebraic norm, positive definite |
| $\tilde p^{\natural}\tilde p=\langle\tilde p\rangle_{\natural}e_0$ | the quaternion norm read on the product |
| $\langle\tilde p\tilde q\rangle_{\natural}=\langle\tilde p\rangle_{\natural}\langle\tilde q\rangle_{\natural}$ | the multiplicativity of the quaternion norm |
| $\bigl(e_1e_2\bigr)^{2}=-e_0$, $e_1^{2}e_2^{2}=e_0$ | the failure of the plain norm |
| $p_0^2+\lvert\vec p\rvert^2=c$: the three-sphere | the level sets of the quaternion norm |
| $p_0^2-\lvert\vec p\rvert^2=c$: the hyperboloids | the level sets of the plain norm |
| $\tilde p^{-1}=\tilde p^{\natural}/\lvert\tilde p\rvert^2$, $\tilde p\neq0$ | the invertibility criterion |

## Further Reading

- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the quaternion norm, its multiplicativity and the four-square identity.
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for the reduced norm, the regular representation and the invertibility criterion of a division algebra.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the norm form of the quaternion algebra and its level sets.
- Israel Nathan Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975), for the square, the norm and the inverse in a non-commutative ring.
