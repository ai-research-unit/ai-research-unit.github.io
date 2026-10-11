# __The 2 Algebraic Norms over the Quaternion $\mathbb{R}$ Space__

## Introduction

The two forms of *The 2 Forms over the Quaternion $\mathbb{R}$ Space* are the scalar parts of the two general products, and their **diagonals** are the **two algebraic norms** of the chapter:

$$
N_P(\tilde p)=\tilde p^2 , \qquad N_Q(\tilde p)=\tilde p^{\natural}\tilde p=|\tilde p|^2e_0 .
$$

The **plain algebraic norm** $N_P$ is the square of the plain product, $N_P(\tilde p)=B(\tilde p)e_0+2p_0\mathbf p$ with $B(\tilde p)=p_0^2-\lvert\mathbf p\rvert^2$; the **quaternion algebraic norm** $N_Q$ is the diagonal of the quaternionic product, $N_Q(\tilde p)=N(\tilde p)e_0$ with $N(\tilde p)=p_0^2+\lvert\mathbf p\rvert^2$. The first is a general element of $\mathbb{H}$ and is **indefinite**: it takes the value $e_0$ at $e_0$ and $-e_0$ at $e_1$, so its scalar coefficient is of both signs. The second is the central positive element $|\tilde p|^2e_0$, **positive definite**. The two norms are read off the two forms, the first from the plain form and the second from the quaternion form.

This article gives the two norms, the **multiplicativity** of the second and the failure of the first, the **norm of a product against the product of the norms**, the **level sets** read algebraically, and the **invertibility criteria** the two give. It assumes the two forms from *The 2 Forms over the Quaternion $\mathbb{R}$ Space* and the two squares from *Comparison Between the Two General Products*, both preceding this one; the norms read on the two remarkable subspaces are *Remarkable Subspaces and the Two Algebraic Norms*, below this article in this category; and the theory of the norm and the invertibility of the plain product is owned by *Norm and Invertibility in the General Plain Algebra*, in the GPA block below.

**Conventions.** Throughout, $\tilde p=p_0e_0+\mathbf p$ and $\tilde q=q_0e_0+\mathbf q$ name elements, $(\mathbf p,\mathbf q)$ is the dot product of the vector parts, $B(\tilde p)=p_0^2-\lvert\mathbf p\rvert^2$ and $N(\tilde p)=p_0^2+\lvert\mathbf p\rvert^2$ are the two forms read on the diagonal, and $\tilde p^{\natural}=p_0e_0-\mathbf p$. The two algebraic norms are $N_P(\tilde p)=\tilde p^2$ and $N_Q(\tilde p)=\tilde p^{\natural}\tilde p=|\tilde p|^2e_0$; the number $|\tilde p|^2\geq0$ is written $N(\tilde p)$ when the coefficient is meant and $N_Q(\tilde p)$ when the central element is meant.

## The Two Norms

**Definition.** The two algebraic norms are the diagonals of the two products,

$$
N_P(\tilde p)=\tilde p\tilde p=\tilde p^2 , \qquad N_Q(\tilde p)=\tilde p^{\natural}\tilde p=|\tilde p|^2e_0 ,
$$

and on the coordinates

$$
N_P(\tilde p)=\bigl(p_0^2-\lvert\mathbf p\rvert^2\bigr)e_0+2p_0\mathbf p , \qquad N_Q(\tilde p)=\bigl(p_0^2+\lvert\mathbf p\rvert^2\bigr)e_0 .
$$

The plain norm is a general quaternion, its scalar coefficient $B(\tilde p)$ being of any sign and its vector coefficient $2p_0\mathbf p$ being nonzero off the axes; the quaternion norm is a nonnegative real multiple of the unit, and it is zero only at the origin.

## Multiplicativity

**Theorem (multiplicativity of the quaternion norm; failure of the plain one).** For all $\tilde p,\tilde q$,

$$
N_Q(\tilde p\tilde q)=N_Q(\tilde p)N_Q(\tilde q) , \qquad \text{that is}\qquad |\tilde p\tilde q|^2=|\tilde p|^2\,|\tilde q|^2 ,
$$

while the plain norm is not multiplicative:

$$
N_P(\tilde p\tilde q)\neq N_P(\tilde p)N_P(\tilde q) \quad\text{in general} , \qquad N_P(e_1e_2)=-e_0 , \quad N_P(e_1)N_P(e_2)=e_0 .
$$

*Proof.* The quaternion norm is the square of the quaternion conjugation applied to the element, $N_Q(\tilde p)=\tilde p^{\natural}\tilde p$, and the conjugation is an anti-automorphism, so $N_Q(\tilde p\tilde q)=(\tilde p\tilde q)^{\natural}\tilde p\tilde q=\tilde q^{\natural}\tilde p^{\natural}\tilde p\tilde q=\tilde q^{\natural}|\tilde p|^2\tilde q=|\tilde p|^2|\tilde q|^2e_0$, the scalar $|\tilde p|^2$ commuting with every element. For the plain norm, the value of $\tilde p\tilde q\tilde p\tilde q$ is the square of the product and the two factors' squares do not determine it: at $\tilde p=e_1,\tilde q=e_2$ the product is $e_3$, of square $-e_0$, while the product of the squares is $(-e_0)(-e_0)=e_0$.

So the quaternion norm is **multiplicative**: the norm of a product is the product of the norms, and the quaternion norm is the reduced norm of the algebra, the square root of the determinant of the regular representation. The plain norm is not multiplicative, and this is the reason it is called a norm rather than the norm of the algebra: the plain product fails associativity in no way, but its *diagonal* is not a multiplicative function. The multiplicativity of the quaternion norm is the algebra's composition law for the four-square identity.

## The Norm of a Product Against the Product of the Norms

**Corollary (the two comparisons).** For all $\tilde p,\tilde q$,

$$
N_Q(\tilde p\tilde q)=N_Q(\tilde p)N_Q(\tilde q) ,
$$

the quaternion norm of a product being exactly the product of the quaternion norms; and the plain norm of a product is not the product of the plain norms, the two differing by the commutator, $(\tilde p\tilde q)^2-\tilde p^2\tilde q^2=\tilde p[\tilde q,\tilde p]\tilde q$. The quaternion norm of the product is the same in the two orders, $N_Q(\tilde p\tilde q)=N_Q(\tilde q\tilde p)$, both being the value of the quaternion form on the product.

*Proof.* The first identity is the multiplicativity theorem. For the second, the plain norm of the product is $(\tilde p\tilde q)^2$ and the product of the plain norms is $\tilde p^2\tilde q^2$, the two differing by $\tilde p[\tilde q,\tilde p]\tilde q$; at $\tilde p=e_1,\tilde q=e_2$ the two values are $-e_0$ and $+e_0$. For the third, $|\tilde p\tilde q|^2=|\tilde p|^2|\tilde q|^2=|\tilde q|^2|\tilde p|^2=|\tilde q\tilde p|^2$, the coefficient being a real number.

So the quaternion norm is insensitive to the order of the factors and to the nesting of a product, while the plain norm is sensitive to both; the quaternion norm is the one that behaves as a **norm of an algebra**, and it is the one used in the invertibility criterion. The statement is the $\mathbb{R}$-reading of the biquaternion table, where the quaternionic norm alone is multiplicative and the plain one is not.

## The Level Sets

**Definition.** A **level set** of a norm $N$ is the set of elements with $N(\tilde p)=ce_0$ for a central value $c\in\mathbb{R}$; the level sets are read algebraically, each being cut out by the scalar and the vector coefficient vanishing together in the right way.

**Proposition (the level sets of the two norms).**

*The quaternion norm.* For a central value $ce_0$, $N_Q(\tilde p)=ce_0$ is the **three-sphere** $|\tilde p|^2=c$ when $c>0$, the origin alone when $c=0$, and is empty when $c<0$.

*The plain norm.* For a central value $ce_0$, the equation $N_P(\tilde p)=ce_0$ forces $\tilde p^2$ to be central, that is $p_0\mathbf p=0$, and the level set is: the **two elements** $\pm\sqrt c\,e_0$ when $c>0$; the **two-sphere** $|\mathbf p|=\sqrt{-c}$ of the vector subspace when $c<0$; and the origin alone when $c=0$.

*Proof.* $N_Q(\tilde p)=ce_0$ reads $p_0^2+\lvert\mathbf p\rvert^2=c$, the equation of the sphere of radius $\sqrt c$ in the four coordinates, empty for $c<0$. For $N_P(\tilde p)=ce_0$ one needs the vector coefficient $2p_0\mathbf p$ to vanish, so $p_0=0$ or $\mathbf p=0$; with $\mathbf p=0$ the equation is $p_0^2=c$, giving the two elements $\pm\sqrt c\,e_0$ for $c>0$ and nothing for $c<0$; with $p_0=0$ the equation is $-\lvert\mathbf p\rvert^2=c$, giving the sphere of radius $\sqrt{-c}$ in the vector subspace for $c<0$ and nothing for $c>0$.

So the level sets of the two norms are of different shapes: the quaternion norm cuts the space into concentric three-spheres, cut by the origin and empty for the negative values; the plain norm cuts the real axis into two points, above the origin, and the vector subspace into two-spheres, below it, the two families meeting only at the origin, which is the level set of the value $0$. In particular the elements of unit quaternion norm form the **unit three-sphere** of the four coordinates, and the elements of square $+e_0$ are the two elements $\pm e_0$ while the elements of square $-e_0$ are the unit two-sphere of the vector subspace; this is the algebraic reading of the roots of $\pm1$, the roots of $1$ being the two scalar units for the plain product and the roots of $-1$ the whole unit sphere of the vectors.

## The Invertibility Criteria

**Theorem (the criterion).** An element $\tilde p$ is invertible in the plain algebra if and only if $N_Q(\tilde p)\neq0$, that is $\tilde p\neq0$; and then $\tilde p^{-1}=\tilde p^{\natural}/|\tilde p|^2$. The plain norm $N_P$ gives no criterion of this kind: it takes its values in $\mathbb{H}$ rather than in $\mathbb{R}$, and it is not multiplicative, so the invertibility of a product cannot be tested on the plain norm.

*Proof.* The identity $\tilde p^{\natural}\tilde p=|\tilde p|^2e_0$ shows that a nonzero $\tilde p$ has the inverse $\tilde p^{\natural}/|\tilde p|^2$, and a zero divisor would give $|\tilde p|^2|\tilde q|^2=0$ with both factors nonzero, impossible; so $\tilde p$ is invertible exactly when $|\tilde p|^2\neq0$, that is exactly when $\tilde p\neq0$, and the criterion is the quaternion norm's. For the plain norm, a value of $N_P$ is an element of $\mathbb{H}$ and $N_P$ is not multiplicative, so the nonzero-ness of $N_P(\tilde p)$ is not decided by any law of the norm, unlike the quaternion norm; the criterion is therefore the quaternion norm's alone.

So the **quaternion norm is the norm of the algebra**: it is real-valued, definite and multiplicative, and its vanishing gives the invertibility criterion and the division property; the plain norm is the diagonal of the plain product and is a norm only in the weak sense of the corpus's vocabulary. The group of units is the nonzero elements, the unit sphere and the positive scalars giving the three-way classification of the invertible elements, of *Norm and Invertibility in the General Plain Algebra*, in the GPA block below; the biquaternion reading, where the two norms are complex-valued and the definiteness of the quaternionic norm fails, is *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*.

## Summary

The quaternion space carries two algebraic norms, the diagonal of the plain product $N_P(\tilde p)=\tilde p^2=(p_0^2-\lvert\mathbf p\rvert^2)e_0+2p_0\mathbf p$ and the diagonal of the quaternionic product $N_Q(\tilde p)=\tilde p^{\natural}\tilde p=(p_0^2+\lvert\mathbf p\rvert^2)e_0$, read off the plain form and the quaternion form. The first is indefinite, taking $e_0$ and $-e_0$ at $e_0$ and $e_1$; the second is positive definite, zero only at the origin. The second is multiplicative, $N_Q(\tilde p\tilde q)=N_Q(\tilde p)N_Q(\tilde q)$, and the first is not, $N_P(e_1e_2)=-e_0$ against $N_P(e_1)N_P(e_2)=e_0$; the quaternion norm of a product equals the product of the quaternion norms and does not depend on the order, while the plain norm of a product is not the product of the plain norms.

The level sets of the quaternion norm at a central value are the three-spheres, cut by the origin and empty for negative values; those of the plain norm are two points on the real axis for a positive value and a two-sphere of the vector subspace for a negative one. The invertibility criterion is the quaternion norm's: $\tilde p$ is invertible exactly when $N_Q(\tilde p)\neq0$, with inverse $\tilde p^{\natural}/|\tilde p|^2$; the plain norm gives no criterion, being neither real-valued nor multiplicative.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $N_P(\tilde p)=\tilde p^2=(p_0^2-\lvert\mathbf p\rvert^2)e_0+2p_0\mathbf p$ | the plain algebraic norm, indefinite |
| $N_Q(\tilde p)=\tilde p^{\natural}\tilde p=(p_0^2+\lvert\mathbf p\rvert^2)e_0$ | the quaternion algebraic norm, positive definite |
| $N_Q(\tilde p\tilde q)=N_Q(\tilde p)N_Q(\tilde q)$ | the multiplicativity of the quaternion norm |
| $N_P(e_1e_2)=-e_0$, $N_P(e_1)N_P(e_2)=e_0$ | the failure of the plain norm |
| $\lvert\tilde p\rvert^2=c$: the three-sphere | the level sets of $N_Q$ |
| $\pm\sqrt c\,e_0$; $\lvert\mathbf p\rvert=\sqrt{-c}$ | the level sets of $N_P$ |
| $\tilde p^{-1}=\tilde p^{\natural}/\lvert\tilde p\rvert^2$, $\tilde p\neq0$ | the invertibility criterion |

## Further Reading

- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the quaternion norm, its multiplicativity and the four-square identity.
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for the reduced norm, the regular representation and the invertibility criterion of a division algebra.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the norm form of the quaternion algebra and its level sets.
- Israel Nathan Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975), for the square, the norm and the inverse in a non-commutative ring.
