# __Norm and Invertibility in the General Quaternionic Algebra__

## Introduction

The general quaternionic bilinear product $\tilde p \star \tilde q = \tilde p^{\natural}\tilde q$ of *Introduction to the General Quaternionic Algebra of Quaternions* is $\mathbb{R}$-bilinear, has $e_0$ as a left unit and no right one, and is not associative. This article studies the quadratic form that the product carries and the inversion theory that the one-sided unit leaves.

The form is the **quaternionic bilinear algebraic norm** $N(\tilde q) = \tilde q^{\natural}\tilde q$, the second of the two algebraic norms of the quaternion real space (*The 2 Algebraic Norms over the Quaternion $\mathbb{R}$ Space*); the other one belongs to the plain product. Over $\mathbb{R}$ this function is the **Euclidean norm** of the coordinate vector of $\tilde q$: the coincidence is stated and used, not re-derived, and it is the source of the definiteness that decides the whole article. The same function is the reduced norm of the plain algebra (*Norm and Invertibility in the General Plain Algebra*), and the question here is what survives of the plain inversion theory when the unit is only one-sided. Two things survive whole: the multiplicativity $N(\tilde p \star \tilde q) = N(\tilde p)N(\tilde q)$ and the criterion for a one-sided inverse. One thing does not survive at all: the inverse itself, because an inverse is an inverse with respect to a two-sided unit, and the algebra has none.

The article closes with the units, with the three-way classification of an element that the norm produces, and with the comparison against the plain algebra, where the same norm yields a genuine group.

## The Norm of the Quaternionic Product

**Definition.** The **quaternionic bilinear algebraic norm** of $\tilde q \in \mathbb{H}$ is

$$
N(\tilde q) = \tilde q^{\natural}\tilde q = q_0^2 + q_1^2 + q_2^2 + q_3^2 .
$$

It is the second of the two algebraic norms of the space and it is the diagonal of the associated form.

**Proposition.** $N(\tilde q)$ is a real scalar, central in $\mathbb{H}$, and the map $N : \mathbb{H} \to \mathbb{R}$ is a quadratic form with polar form

$$
\beta(\tilde p,\tilde q) = \tfrac12\bigl(N(\tilde p+\tilde q) - N(\tilde p) - N(\tilde q)\bigr) = p_0q_0 + \mathbf p \cdot \mathbf q ,
$$

the quaternionic bilinear form of the space (*The 2 Forms over the Quaternion $\mathbb{R}$ Space*).

*Proof.* The scalar computation is the sum of four squares; a real scalar commutes with every element of $\mathbb{H}$; the polar form of a sum of squares is the Euclidean inner product of the coordinate vectors.

**Theorem (multiplicativity).** The norm is multiplicative for the quaternionic product:

$$
N(\tilde p \star \tilde q) = N(\tilde p)\,N(\tilde q) .
$$

*Proof.* Using $(\tilde p^{\natural}\tilde q)^{\natural} = \tilde q^{\natural}\tilde p$ and the centrality of $N(\tilde p)$,

$$
N(\tilde p \star \tilde q) = (\tilde p^{\natural}\tilde q)^{\natural}(\tilde p^{\natural}\tilde q) = \tilde q^{\natural}\tilde p\,\tilde p^{\natural}\tilde q = \tilde q^{\natural}N(\tilde p)\tilde q = N(\tilde p)\,\tilde q^{\natural}\tilde q = N(\tilde p)N(\tilde q) .
$$

Multiplicativity is the whole reason the product carries an inversion theory at all, and it is a property the norm of the plain algebra also has; the two norms are the same function and both are multiplicative, so the difference between the two blocks lies entirely in the units and not in the forms.

**Theorem (definiteness).** Over $\mathbb{R}$ the norm is positive definite: $N(\tilde q) \geq 0$ for every $\tilde q$, and $N(\tilde q) = 0$ only for $\tilde q = 0$.

*Proof.* $N(\tilde q)$ is a sum of four squares of real numbers. This is the coincidence of the norm with the Euclidean norm, and it is the property that removes every singular element and every isotropic direction from the block.

**Remark (the other norm).** The plain product carries the plain bilinear algebraic norm $\tilde p^2$, whose scalar part is $\mathrm{Sc}(\tilde p^2) = p_0^2 - \mathbf p \cdot \mathbf p$ and whose associated form has signature $(1,3)$ and is indefinite (*The 2 Algebraic Norms over the Quaternion $\mathbb{R}$ Space*). The two norms are equal on the scalar line and differ in sign on the vector subspace, and their definiteness is opposite. The comparison on the two forms of the one space is *The Isotropic Structure of the General Quaternionic Algebra*, below this article in this category.

**Corollary (no zero divisors).** If $\tilde p \star \tilde q = 0$ then $N(\tilde p)N(\tilde q) = 0$, so $\tilde p = 0$ or $\tilde q = 0$ over $\mathbb{R}$. The product has no zero divisors, and no nonzero element is a zero divisor.

## The One-Sided Inverse Equations

**Definition.** For $\tilde p$ with $N(\tilde p) \neq 0$ put

$$
\zeta(\tilde p) = \frac{\tilde p}{N(\tilde p)} .
$$

The element $\zeta(\tilde p)$ is the conjugate of the plain inverse: $\zeta(\tilde p) = (\tilde p^{-1})^{\natural}$, since $\tilde p^{-1} = \tilde p^{\natural}/N(\tilde p)$ (*Norm and Invertibility in the General Plain Algebra*).

**Theorem (the two one-sided equations).** Let $\tilde p \in \mathbb{H}$ with $N(\tilde p) \neq 0$. The equation $\tilde p \star \tilde x = e_0$ has the unique solution $\tilde x = \zeta(\tilde p)$, and the equation $\tilde y \star \tilde p = e_0$ has the unique solution $\tilde y = \zeta(\tilde p)$. In particular the two one-sided inverses exist and they coincide:

$$
\tilde p \star \zeta(\tilde p) = e_0 = \zeta(\tilde p) \star \tilde p .
$$

*Proof.* From $\tilde p^{\natural}\tilde x = e_0$, left-multiplying in the plain multiplication by $\tilde p$ gives $\tilde p\tilde p^{\natural}\tilde x = \tilde p$, that is $N(\tilde p)\tilde x = \tilde p$, whence $\tilde x = \tilde p/N(\tilde p)$ because $N(\tilde p)$ is a nonzero real scalar. Conversely $\tilde p^{\natural}\bigl(\tilde p/N(\tilde p)\bigr) = N(\tilde p)/N(\tilde p) = e_0$. Conjugating the second equation gives $(\tilde y^{\natural}\tilde p)^{\natural} = \tilde p^{\natural}\tilde y = e_0$, which is the first equation with $\tilde x = \tilde y$; so its unique solution is again $\tilde y = \zeta(\tilde p)$, and directly $\zeta(\tilde p)^{\natural}\tilde p = \tilde p^{\natural}\tilde p/N(\tilde p) = e_0$.

**Theorem (the criterion).** For $\tilde p \in \mathbb{H}$ the following are equivalent: $\tilde p$ has a left inverse; $\tilde p$ has a right inverse; $N(\tilde p) \neq 0$. Over $\mathbb{R}$ they are equivalent to $\tilde p \neq 0$.

*Proof.* A left inverse is a solution of the first equation and a right inverse a solution of the second; the theorem above solves both exactly when $N(\tilde p) \neq 0$. Over $\mathbb{R}$ the norm is definite, so $N(\tilde p) \neq 0$ is $\tilde p \neq 0$.

**Remark (why this is not invertibility).** In a unital algebra the inverse of $\tilde p$ is defined by $\tilde p \star \tilde x = \tilde x \star \tilde p = e$ for the identity $e$. Here the only candidate for an identity is the left unit $e_0$, and it fails on the right, $\tilde q \star e_0 = \tilde q^{\natural} \neq \tilde q$ for a non-real $\tilde q$; so the phrase "the inverse of $\tilde p$" has no referent, and the two displayed equations are the best the algebra affords. What they compute is an element that inverts $\tilde p$ **against the one-sided unit**, and the content of the theorem is that the left and the right such elements are not merely both present, they are the same. In the plain algebra the inverse is $\tilde p^{-1} = \zeta(\tilde p)^{\natural}$ and the group of units is built on it; here only $\zeta$ survives.

## The Units

**Definition.** The **units** of the algebra are the elements admitting a one-sided inverse,

$$
\mathbb{H}^{\times} = \{\tilde p \in \mathbb{H} : N(\tilde p) \neq 0\} , \qquad \mathbb{H}^{\times} = \mathbb{H} \setminus \{0\} \ \text{ over } \mathbb{R} .
$$

**Theorem.** Under the quaternionic product the set $\mathbb{H}^{\times}$ is closed, contains $e_0$ as a left unit, and every one of its elements has the two-sided inverse $\zeta(\tilde p)$. It is **not a group**: the operation is not associative and $e_0$ is not a right unit. The left multiplications and the right multiplications by a nonzero element are injective linear maps of $\mathbb{H}$, so $\mathbb{H}^{\times}$ is a quasigroup with a left unit and with two-sided inverses.

*Proof.* Closure is the multiplicativity and the definiteness of the norm; the left unit and the failure of the right unit are those of *Introduction to the General Quaternionic Algebra of Quaternions*; the two-sided inverse is the theorem above. The multiplications are injective because the norm multiplies, $N(\tilde p \star \tilde q) = N(\tilde p)N(\tilde q)$, and is definite, so $\tilde p \star \cdot$ and $\cdot \star \tilde p$ have trivial kernel on the finite-dimensional space $\mathbb{H}$; non-associativity on all of $\mathbb{H}$ excludes associativity on $\mathbb{H}^{\times}$, and $e_0 \star \tilde q = \tilde q$ against $\tilde q \star e_0 = \tilde q^{\natural}$ excludes a two-sided identity.

**Comparison with the plain algebra.** In the plain algebra the same set $\mathbb{H}^{\times}$, under the same norm, is a group: the identity is the two-sided $e_0$, the inverse is $\tilde p^{-1} = \zeta(\tilde p)^{\natural}$, and the inverse map $\tilde p \mapsto \tilde p^{-1}$ is an anti-automorphism of the group. The quaternionic block keeps the set, the norm, the multiplicativity and the inverse formula read backwards, and loses exactly the group — to the non-associativity and to the one-sidedness of the unit.

## The Three-Way Classification

**Theorem.** Every element of the general quaternionic algebra lies in exactly one of the three classes:

1. $\tilde p = 0$;
2. $\tilde p \neq 0$ with $N(\tilde p) \neq 0$: an element with a one-sided inverse, with the two-sided inverse $\zeta(\tilde p)$;
3. $\tilde p \neq 0$ with $N(\tilde p) = 0$: an element whose square vanishes, $\tilde p \star \tilde p = N(\tilde p)e_0 = 0$, hence a zero divisor and a nilpotent of index two.

Over $\mathbb{R}$ the third class is empty and the classification is two-valued: the zero element and the nonzero elements, all of which have a one-sided inverse.

*Proof.* The three classes are exclusive and exhaustive by the criterion of the preceding section, since the criterion splits the nonzero elements by the vanishing of $N$. In the third class $\tilde p \star \tilde p = \tilde p^{\natural}\tilde p = N(\tilde p)e_0 = 0$ with $\tilde p \neq 0$, so $\tilde p$ is a zero divisor and its square vanishes.

**Remark.** The classification has the same shape as the one the plain algebra carries, and the terms differ in one place only: the middle class is a class of units in the plain algebra and only a class of one-sided invertible elements here. Over a base field in which the norm is isotropic the third class is nonempty and the algebra has nilpotents; over $\mathbb{R}$ the definiteness of the norm removes the class, and this block has no zero divisors and no nonzero nilpotent at all.

## Summary

The quaternionic product carries the norm $N(\tilde q) = \tilde q^{\natural}\tilde q = q_0^2 + q_1^2 + q_2^2 + q_3^2$, which over $\mathbb{R}$ is the Euclidean norm of the coordinate vector, a positive definite quadratic form with polar form $\beta(\tilde p,\tilde q) = p_0q_0 + \mathbf p \cdot \mathbf q$, central-valued and multiplicative, $N(\tilde p \star \tilde q) = N(\tilde p)N(\tilde q)$. Since the algebra has a left unit and no right one, the inverse of the unital theory does not exist; the two one-sided equations $\tilde p \star \tilde x = e_0$ and $\tilde y \star \tilde p = e_0$ both have the unique solution $\zeta(\tilde p) = \tilde p/N(\tilde p) = (\tilde p^{-1})^{\natural}$ exactly when $N(\tilde p) \neq 0$, so the left and the right one-sided inverses coincide. The units are $\mathbb{H}^{\times} = \mathbb{H} \setminus \{0\}$ over $\mathbb{R}$ and they do not form a group, only a quasigroup with a left unit and with two-sided inverses. An element is either zero, or $N$-nonzero and one-sided invertible, or $N$-zero and nilpotent of index two; over $\mathbb{R}$ the last class is empty. The plain algebra carries the same norm and a genuine group of units, and the whole difference between the two blocks is there.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde p \star \tilde q = \tilde p^{\natural}\tilde q$ | the general quaternionic bilinear product |
| $N(\tilde q) = \tilde q^{\natural}\tilde q = \sum_\mu q_\mu^2$ | the quaternionic bilinear algebraic norm |
| $\beta(\tilde p,\tilde q) = p_0q_0 + \mathbf p \cdot \mathbf q$ | the quaternionic bilinear form, the polar form of $N$ |
| $\zeta(\tilde p) = \tilde p/N(\tilde p)$ | the one-sided inverse of $\tilde p$ |
| $\mathbb{H}^{\times} = \{\tilde p : N(\tilde p) \neq 0\}$ | the units, $\mathbb{H} \setminus \{0\}$ over $\mathbb{R}$ |
| $\tilde q^{-1} = \tilde q^{\natural}/N(\tilde q)$ | the plain inverse, from the general plain algebra |
| $\mathrm{Sc}(\tilde q^2) = q_0^2 - \mathbf q \cdot \mathbf q$ | the scalar part of the plain bilinear algebraic norm, for contrast |

## Further Reading

- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the norm of a nonassociative algebra and the one-sided inverse equations.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for inverses against a one-sided unit and the quasigroup attached to a nonassociative product.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the multiplicative norm of the quaternion algebra and the unit sphere.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the norm of an algebra with involution and the norm form of a quaternion algebra.
