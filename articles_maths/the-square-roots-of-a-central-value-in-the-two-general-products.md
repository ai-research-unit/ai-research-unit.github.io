# __The Square Roots of a Central Value in the Two General Products__

## Introduction

A root of a central value in a product is an element whose square in that product is the value times $e_0$. This article gathers the three values $-1$, $0$ and $+1$ for the two general products and the six structures they generate, in one table, and reads the passage from the sphere of roots of $-1$ in the plain product to the empty set of the cross products. The products are *The Two General Products of the Quaternion $\mathbb{R}$ Space* and the six structures are *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*; the roots in the plain product are *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*, above this article in this category.

## Roots of a Central Value

**Definition.** Let $\star$ be a product on $\mathbb{H}$ and let $\lambda\in\mathbb{R}$. A **root of $\lambda$** in $\star$ is an element $\tilde\xi$ with
$$
\tilde\xi\star\tilde\xi=\lambda e_0 .
$$
The root set is read relative to the product, as the name *root of $-1$ in the general plain product* records, and the value is central, so the equation is an equality of quaternions with a real right-hand side. The roots of the three values $-1,0,+1$ are the entries of the table below; the roots of a general central value and the roots of a general element are the two other questions of the same family, treated in *Square Roots of a General Element in the General Plain Algebra*.

## The Plain and the Quaternionic Product

The two general products answer the question by the norm and by none:

- **Plain product.** Writing $\tilde\xi=\xi_0+\boldsymbol\xi$, the square is $\tilde\xi^2=(\xi_0^2-|\boldsymbol\xi|^2)+2\xi_0\boldsymbol\xi$. The vanishing of the vector part forces $\xi_0=0$ or $\boldsymbol\xi=0$.
  - $\lambda=-1$: $\boldsymbol\xi=0$ is impossible, so $\xi_0=0$ and $|\boldsymbol\xi|=1$: the roots form the **unit sphere** $S^2$ of the pure unit quaternions, the sphere of the complex structures on $\mathbb{R}^4$.
  - $\lambda=0$: both cases force $\tilde\xi=0$: the roots reduce to the single element $0$.
  - $\lambda=+1$: the vector part vanishes, so $\tilde\xi=\pm e_0$: the roots are the two units.
- **Quaternionic product.** Here $\tilde\xi^{\natural}\tilde\xi=N(\tilde\xi)e_0$, so the equation is the real equation $N(\tilde\xi)=\lambda$.
  - $\lambda=-1$: empty, the norm being a sum of squares.
  - $\lambda=0$: $\tilde\xi=0$ alone.
  - $\lambda=+1$: the **unit sphere** $S^3$ of the unit quaternions.

So the plain product has a sphere of roots of $-1$ and two roots of $+1$, while the quaternionic product has the reverse: empty roots of $-1$ and a sphere of roots of $+1$. The two products exchange the two spheres, and both reduce the roots of $0$ to the origin.

## The Six Structures

| structure | product | roots of $-1$ | roots of $0$ | roots of $+1$ |
|---|---|---|---|---|
| GPA | $\tilde p\tilde q$ | $S^2$, the unit pure sphere | $\{0\}$ | $\{\pm e_0\}$ |
| GQA | $\tilde p^{\natural}\tilde q$ | $\varnothing$ | $\{0\}$ | $S^3$, the unit sphere |
| SPA | $\tilde p\bullet\tilde q$ | $S^2$ | $\{0\}$ | $\{\pm e_0\}$ |
| SQA | $\tfrac12(\tilde p^{\natural}\tilde q+\tilde q^{\natural}\tilde p)$ | $\varnothing$ | $\{0\}$ | $S^3$ |
| APA | $\tilde p\times\tilde q$ | $\varnothing$ | $\mathbb{H}$ | $\varnothing$ |
| AQA | $\tfrac12(\tilde p^{\natural}\tilde q-\tilde q^{\natural}\tilde p)$ | $\varnothing$ | $\mathbb{H}$ | $\varnothing$ |

The symmetrised structures inherit the root sets of the general products from which they are made: the Jordan square is the plain square, and the symmetrised quaternionic square is the norm times $e_0$. The two antisymmetric structures have no root of a nonzero value, since their square is identically zero; their roots of $0$ are **all of** $\mathbb{H}$, not the origin, and this is the one row where the reduction of the roots of $0$ to zero fails. Both antisymmetric products are alternating, hence the empty columns; the plain sphere of roots of $-1$ has no counterpart there.

The roots in the plain product are *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*, above this article in this category; the roots in the symmetric quaternionic product are the companion article of that block. This article owns only the comparison.

## Contrast with the Biquaternion Case

In the biquaternion chapter the roots of a central value form a quadric, the isotropic cone of the complex norm, and the roots of $-1$ are the large family of the split structures; the null set is a hypersurface. Over $\mathbb{R}$ the definiteness of the norm removes the roots of $-1$ of the quaternionic product and leaves the roots of $0$ at the origin alone for the general products. The two spheres $S^2$ and $S^3$ of the plain and the quaternionic product are the only non-trivial root sets of positive dimension; the quadric of the biquaternion chapter is their degeneration at the loss of the division property.

## Summary

The roots of $-1,0,+1$ in the two general products and in the six structures are gathered in one table. The plain product has the sphere $S^2$ of roots of $-1$ and the two roots $\pm e_0$ of $+1$; the quaternionic product has the empty set of roots of $-1$ and the sphere $S^3$ of roots of $+1$; both reduce the roots of $0$ to the origin. The symmetrised structures inherit these sets, and the antisymmetric structures have no roots of a nonzero value and all of $\mathbb{H}$ as roots of $0$. The biquaternion quadric is not reached over $\mathbb{R}$, where the norm is definite.

## Summary of Notation

| symbol | meaning |
|---|---|
| root of $\lambda$ in $\star$ | $\tilde\xi$ with $\tilde\xi\star\tilde\xi=\lambda e_0$ |
| $S^2$ | the unit pure sphere, the roots of $-1$ in the plain product |
| $S^3$ | the unit sphere, the roots of $+1$ in the quaternionic product |
| $\{\pm e_0\}$ | the roots of $+1$ in the plain product |
| $\varnothing$ | the empty root set, for the antisymmetric products off $0$ |

## Further Reading

- *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-general-plain-algebra-of-quaternions.md`), above this article in this category.
- *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-6-algebraic-structures-over-the-quaternion-r-space.md`), for the six products.
- *The Idempotents of the Two General Products* (`articles_maths/the-idempotents-of-the-two-general-products.md`), above this article in this category, for the companion class.
- *The Square-Zero Elements of the Two General Products* (`articles_maths/the-square-zero-elements-of-the-two-general-products.md`), below this article in this category, for the roots of $0$ of the antisymmetric products.
