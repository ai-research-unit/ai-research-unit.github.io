# __Square Roots of Minus One, Zero and Plus One in the Symmetric Plain Algebra__

## Introduction

The symmetric plain algebra of $\mathbb{H}$ carries the Jordan product $\tilde p\bullet\tilde q=\tfrac12(\tilde p\tilde q+\tilde q\tilde p)$ of *Introduction to the Symmetric Plain Algebra of Quaternions*, and the square of an element in it is the plain square. This article determines the three central root sets

$$
\Sigma_{-}=\{\tilde\xi : \tilde\xi\bullet\tilde\xi=-e_0\},\qquad
\Sigma_{0}=\{\tilde\xi : \tilde\xi\bullet\tilde\xi=0\},\qquad
\Sigma_{+}=\{\tilde\xi : \tilde\xi\bullet\tilde\xi=+e_0\},
$$

**This is not the algebra $\mathbb{H}$.** The two algebras share the space, the addition, the real scalars and the unit, but $\bullet$ is a different multiplication and the projection onto the scalar line is not multiplicative. Throughout, the natural sign ${}^{\natural}$ is the quaternion conjugation, the bar is the identity because $\mathbb{R}$ has no nontrivial involution, and the star coincides with the natural sign and gives nothing new.

**Conventions.** The algebra is $\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$ and $e_1^2=e_2^2=e_3^2=-e_0$. An element is $\tilde q=q_0e_0+\mathbf q$ with $\mathbf q=\sum_{k=1}^{3}q_ke_k$ and $q_\mu\in\mathbb{R}$; the norm is $N(\tilde q)=\tilde q\tilde q^{\natural}=q_0^2+|\mathbf q|^2$, the vector subspace is $\mathrm{Vect}(\mathbb{H})$, the unit sphere is $Sp(1)=S^3=\{N=1\}$, and the unit group is $\mathbb{H}^{\times}=\mathbb{H}\setminus\{0\}$. These are those of *Norm and Invertibility in the General Plain Algebra* and *Introduction to the Remarkable Subspaces of the Quaternions*.

## The Common Reduction

### The Square and the Two Equations

Since the square of the block is the plain square, the equation $\tilde\xi\bullet\tilde\xi=\lambda e_0$ is the plain equation $\tilde\xi^2=\lambda e_0$, and it separates into a scalar and a vector equation.

**Proposition.** For $\tilde\xi=\xi_0e_0+\boldsymbol{\xi}$ and $\lambda\in\mathbb{R}$,

$$
\tilde\xi^2=\lambda e_0\iff
\begin{cases}
2\xi_0\boldsymbol{\xi}=0,\\[2pt]
\xi_0^2-|\boldsymbol{\xi}|^2=\lambda .
\end{cases}
$$

*Proof.* The plain square is $\tilde\xi^2=(\xi_0^2-|\boldsymbol{\xi}|^2)e_0+2\xi_0\boldsymbol{\xi}$, and the element is central exactly when its vector part vanishes, which is the displayed pair.

**Corollary.** Either $\xi_0=0$ or $\boldsymbol{\xi}=0$; in the first case $\lambda=-|\boldsymbol{\xi}|^2$ and the root is pure, in the second $\lambda=\xi_0^2$ and the root is scalar. **Only the scalar equation survives on each branch**, so the three central root sets are read off the sign of $\lambda$.

## The Roots of $-e_0$

**Theorem.** $\tilde\xi\bullet\tilde\xi=-e_0$ if and only if $\tilde\xi$ is a pure element of norm one:

$$
\Sigma_{-}=\mathrm{Vect}(\mathbb{H})\cap Sp(1)=\{\tilde\xi\in\mathrm{Vect}(\mathbb{H}) : N(\tilde\xi)=1\}.
$$

*Proof.* On the pure branch $\xi_0=0$ the scalar equation is $-|\boldsymbol{\xi}|^2=-1$, that is $N(\tilde\xi)=1$; on the scalar branch $\boldsymbol{\xi}=0$ the scalar equation is $\xi_0^2=-1$, which has no real solution, so no scalar root exists.

**Proposition.** The root set $\Sigma_{-}$ is the unit sphere of the three-dimensional vector subspace; it has real dimension two in the four-dimensional algebra, it is contained in the level set $\{N=1\}$, and it is a single conjugacy class of the unit group under the adjoint action.

*Proof.* The vector subspace is three-dimensional and the roots are its elements of norm one, so $\Sigma_{-}$ is a two-sphere. The transitivity of the adjoint action on that sphere, the identification of the orbit with the homogeneous space $Sp(1)/U(1)\cong SO(3)/SO(2)$ and the complex structures $L_{\tilde\xi}$ that the roots define on $\mathbb{H}\cong\mathbb{R}^4$ are those of *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*: **the root set is unchanged by the passage from the plain product to the block**, because the square is unchanged, and the whole classification is quoted and not repeated here.**

## The Roots of $0$

**Theorem.** $\tilde\xi\bullet\tilde\xi=0$ if and only if $\tilde\xi=0$:

$$
\Sigma_{0}=\{0\}.
$$

*Proof.* On the pure branch the scalar equation is $-|\boldsymbol{\xi}|^2=0$, so $\boldsymbol{\xi}=0$ and $\tilde\xi=0$; on the scalar branch the equation is $\xi_0^2=0$, so $\xi_0=0$ and again $\tilde\xi=0$.

**Corollary.** The block has **no nonzero square-zero element** — no nonzero nilpotent — although it has zero divisors. A zero divisor is a nonzero element with a nonzero partner, not a nonzero element whose own square vanishes, and the two notions separate in the block, where in an algebra with nilpotents they would not.

## The Roots of $+e_0$

**Theorem.** $\tilde\xi\bullet\tilde\xi=+e_0$ if and only if $\tilde\xi=\pm e_0$:

$$
\Sigma_{+}=\{e_0,-e_0\}.
$$

*Proof.* On the pure branch the equation is $-|\boldsymbol{\xi}|^2=+1$, that is $|\boldsymbol{\xi}|^2=-1$, which has no real solution; on the scalar branch it is $\xi_0^2=1$, whose roots are $\xi_0=\pm1$. Both are roots, and the set has two elements.

**Remark (the two-point class).** Of the three root sets, $\Sigma_{-}$ is a two-dimensional sphere, $\Sigma_{0}$ is one point and $\Sigma_{+}$ is a two-point set. **The two-point class of the outline is the root set of $+e_0$**, and it realises the centre $\{\pm e_0\}$ of the unit sphere; there is no empty class among the three, and the empty root set of $-e_0$ belongs to the symmetric quaternionic block, whose square of a pure element is $+|\mathbf u|^2e_0$ and is positive.

## The Relation to the Idempotents

**Proposition.** The idempotents of the block and the roots of $+e_0$ correspond under the affine map $\tilde\pi\mapsto2\tilde\pi-e_0$:

$$
\tilde\pi\bullet\tilde\pi=\tilde\pi\iff (2\tilde\pi-e_0)\bullet(2\tilde\pi-e_0)=e_0 .
$$

*Proof.* Expand with the quadratic identity or directly in the plain product: $\tilde\pi^2=\tilde\pi$ is equivalent to $4\tilde\pi^2-4\tilde\pi+e_0=e_0$, that is to $(2\tilde\pi-e_0)^2=e_0$.

**Corollary.** Since $\Sigma_{+}=\{\pm e_0\}$, the idempotents are $\tilde\pi=\tfrac12(e_0+e_0)=e_0$ and $\tilde\pi=\tfrac12(e_0-e_0)=0$: the two trivial idempotents. The idempotents and their degeneracy are *The Specificities of the Symmetric Plain Algebra*, below this article in this category and *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*, below this article in this category.

## Summary

The square of the block is the plain square, so the equation $\tilde\xi\bullet\tilde\xi=\lambda e_0$ reduces to the pair $2\xi_0\boldsymbol{\xi}=0$, $\xi_0^2-|\boldsymbol{\xi}|^2=\lambda$, and the three central root sets are: $\Sigma_{-}=\{\tilde\xi\in\mathrm{Vect}(\mathbb{H}):N(\tilde\xi)=1\}$, the unit sphere of the vector subspace, of real dimension two and a single conjugacy class of the unit group; $\Sigma_{0}=\{0\}$, so the block has no nonzero nilpotent although it has zero divisors; and $\Sigma_{+}=\{\pm e_0\}$, the two-point class that realises the centre of the unit sphere. The idempotents correspond to the roots of $+e_0$ under $\tilde\pi\mapsto2\tilde\pi-e_0$, so they are only $0$ and $e_0$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\xi\bullet\tilde\xi=\tilde\xi^2$ | the square of the block is the plain square |
| $\Sigma_{-}=\mathrm{Vect}(\mathbb{H})\cap Sp(1)$ | the roots of $-e_0$, the unit sphere of the vector subspace |
| $\Sigma_{0}=\{0\}$ | the roots of $0$ |
| $\Sigma_{+}=\{\pm e_0\}$ | the roots of $+e_0$ |
| $\tilde\pi\mapsto2\tilde\pi-e_0$ | the correspondence between idempotents and roots of $+e_0$ |
| $Sp(1)=S^3$ | the unit sphere of the algebra |

## Further Reading

- *Introduction to the Symmetric Plain Algebra of Quaternions*, for the product and the square.
- *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*, for the same three sets on the plain product, with the conjugacy-class and homogeneous-space structure.
- *Square Roots of a General Element in the Symmetric Plain Algebra*, below this article in this category, for the equation with a general right-hand side.
- *The Specificities of the Symmetric Plain Algebra*, below this article in this category and *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*, below this article in this category, for the idempotents and their degeneracy.
- *Norm and Invertibility in the Symmetric Plain Algebra*, for the norm, the unit sphere and the unit group.
