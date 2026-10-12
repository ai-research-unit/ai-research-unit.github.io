# __The Square Roots of a Central Value in the Six Structures__

## Introduction

A root of a central value in a structure is an element whose square in that structure is the value times $e_0$. The quaternion space carries six structures, and the root set is read here for all six and for every real value of the central element. The two general products exchange a sphere for the empty set, the four structures with a definite square reduce the roots of $0$ to the origin, and the two cross products alone admit the whole space as roots of $0$. The products are *The 6 Products of the Quaternion Real Space* and *The Two General Products of the Quaternion $\mathbb{R}$ Space*, the six structures are *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, and the definitions are *Definitions for the Study of the 6 Algebraic Structures*, all above this article in this category.

## Roots of a Central Value

**Definition.** Let $\star$ be a product on $\mathbb{H}$ and let $\lambda\in\mathbb{R}$. A **root of $\lambda$** in $\star$ is an element $\tilde\xi$ with
$$
\tilde\xi\star\tilde\xi=\lambda e_0 .
$$
The root set is read relative to the product, as the name *root of $-1$ in the general plain product* records, and the value is central, so the equation is an equality of quaternions with a real right-hand side. The roots of the three particular values $-1,0,+1$ are the entries of the table below, and the roots of a general central value are the same computation carried to a general $\lambda$.

## The Two Squares and the Two Forms

The root equation is the square equation, and the six squares of *The Idempotents of the Six Structures* group the six structures in two:

| structure | square of $\tilde x$ | root equation |
|---|---|---|
| $\mathrm{GPA}$ | $(x_0^2-\lvert\mathbf x\rvert^2)e_0+2x_0\mathbf x$ | $B(\tilde x)=x_0^2-\lvert\mathbf x\rvert^2=\lambda$ and $2x_0\mathbf x=0$ |
| $\mathrm{SPA}$ | $(x_0^2-\lvert\mathbf x\rvert^2)e_0+2x_0\mathbf x$ | $B(\tilde x)=x_0^2-\lvert\mathbf x\rvert^2=\lambda$ and $2x_0\mathbf x=0$ |
| $\mathrm{GQA}$ | $N(\tilde x)e_0$ | $N(\tilde x)=\lambda$ |
| $\mathrm{SQA}$ | $N(\tilde x)e_0$ | $N(\tilde x)=\lambda$ |
| $\mathrm{APA}$ | $0$ | $0=\lambda$ |
| $\mathrm{AQA}$ | $0$ | $0=\lambda$ |

The plain square carries the plain form $B(\tilde x)=x_0^2-|\mathbf x|^2$; the quaternionic square carries the quaternion form $N(\tilde x)=x_0^2+|\mathbf x|^2$. The two forms are definite and opposite on the vector subspace, and this one sign is the whole difference between the two families below.

## The Roots in the Plain Family

**Theorem (the roots of a central value in the plain product).** For the general plain and the symmetric plain structures, the roots of $\lambda$ are
$$
\lambda<0:\quad\{\mathbf u:|\mathbf u|^2=-\lambda\}\ \text{in the vector subspace} ,\qquad
\lambda=0:\quad\{0\} ,\qquad
\lambda>0:\quad\{\pm\sqrt\lambda\,e_0\} .
$$
For the three values this reads: the roots of $-1$ are the sphere $S^2$ of the pure unit quaternions, of real dimension two; the roots of $0$ reduce to the origin; and the roots of $+1$ are the two units $\pm e_0$.

*Proof.* The square is $\tilde\xi^2=(\xi_0^2-|\boldsymbol\xi|^2)e_0+2\xi_0\boldsymbol\xi$, and the vector part $2\xi_0\boldsymbol\xi$ vanishes when $\xi_0=0$ or $\boldsymbol\xi=0$. If $\boldsymbol\xi=0$ the equation is $\xi_0^2=\lambda$, with no real solution for $\lambda<0$, the single element $0$ for $\lambda=0$, and the two elements $\pm\sqrt\lambda\,e_0$ for $\lambda>0$. If $\xi_0=0$ the equation is $-|\boldsymbol\xi|^2=\lambda$, with no solution for $\lambda>0$, the single element $0$ for $\lambda=0$, and the sphere $|\boldsymbol\xi|^2=-\lambda$ of real dimension two for $\lambda<0$. The two branches are disjoint except at the origin, which they share only in the case $\lambda=0$; for $\lambda=-1$ the sphere is $S^2$ and for $\lambda=+1$ the two points are $\pm e_0$.

The sphere of roots of $-1$ is the sphere of the complex structures on the space: every pure unit quaternion squares to $-e_0$, so it is a multiplication by a complex structure, and the sphere carries the whole continuous family. This is the sphere that the conversion of the plain family into an algebra over $\mathbb{C}$ uses, and it is the reason the plain product has a continuous root set while the quaternionic product has none.

## The Roots in the Quaternionic Family

**Theorem (the roots of a central value in the quaternionic product).** For the general quaternionic and the symmetric quaternionic structures, the roots of $\lambda$ are
$$
\lambda<0:\quad\varnothing ,\qquad
\lambda=0:\quad\{0\} ,\qquad
\lambda>0:\quad\{\tilde\xi:N(\tilde\xi)=\lambda\} ,
$$
the last being the sphere of radius $\sqrt\lambda$ in the four-dimensional space. For the three values: the roots of $-1$ are empty, the roots of $0$ reduce to the origin, and the roots of $+1$ are the unit sphere $S^3$.

*Proof.* The square of the quaternionic family is $N(\tilde\xi)e_0$, so the root equation is the single real equation $N(\tilde\xi)=\lambda$. The quaternion form is a sum of four real squares, $N(\tilde\xi)=\xi_0^2+|\boldsymbol\xi|^2$, hence nonnegative; the equation is empty for $\lambda<0$, the single element $0$ for $\lambda=0$, and the sphere of radius $\sqrt\lambda$, of real dimension three, for $\lambda>0$.

The two families exchange the signs: the plain family has its sphere at the negative values and two points at the positive values, while the quaternionic family has its sphere at the positive values and nothing at the negative values. The exchange is the sign between the plain form $B$ and the quaternion form $N$ on the vector subspace, and it is the same exchange that separates the roots of $-1$ from the roots of $+1$ in the two general products of *The Two General Products of the Quaternion $\mathbb{R}$ Space*.

## The Roots in the Antisymmetric Structures

**Theorem (the roots in the cross products).** For the plain cross product and the quaternionic cross product the root set of $\lambda$ is the whole space for $\lambda=0$ and is empty for $\lambda\neq0$.

*Proof.* Both products are alternating, so their square vanishes identically; the equation $0=\lambda e_0$ is satisfied by every element when $\lambda=0$ and by none when $\lambda\neq0$.

The antisymmetric structures are the one place of the six where the roots of $0$ are not the origin but the whole space, and they have no root of any other value. The failure is total: the two structures admit no root of a nonzero central value at all, and their roots of $0$ are all of $\mathbb{H}$.

## The Six Root Sets Side by Side

| structure | product | roots of $-1$ | roots of $0$ | roots of $+1$ |
|---|---|---|---|---|
| $\mathrm{GPA}$ | $\tilde p\tilde q$ | $S^2$, the unit pure sphere | $\{0\}$ | $\{\pm e_0\}$ |
| $\mathrm{GQA}$ | $\tilde p^{\natural}\tilde q$ | $\varnothing$ | $\{0\}$ | $S^3$, the unit sphere |
| $\mathrm{SPA}$ | $\tilde p\bullet\tilde q$ | $S^2$ | $\{0\}$ | $\{\pm e_0\}$ |
| $\mathrm{SQA}$ | $N(\tilde p,\tilde q)e_0$ | $\varnothing$ | $\{0\}$ | $S^3$ |
| $\mathrm{APA}$ | $\tilde p\wedge\tilde q$ | $\varnothing$ | $\mathbb{H}$ | $\varnothing$ |
| $\mathrm{AQA}$ | $\tilde p\wedge^{\natural}\tilde q$ | $\varnothing$ | $\mathbb{H}$ | $\varnothing$ |

For a general central value $\lambda$ the six root sets are

| value | plain family, GPA and SPA | quaternionic family, GQA and SQA | antisymmetric, APA and AQA |
|---|---|---|---|
| $\lambda<0$ | the sphere of radius $\sqrt{-\lambda}$, dimension two | $\varnothing$ | $\varnothing$ |
| $\lambda=0$ | $\{0\}$ | $\{0\}$ | $\mathbb{H}$ |
| $\lambda>0$ | $\{\pm\sqrt\lambda\,e_0\}$ | the sphere of radius $\sqrt\lambda$, dimension three | $\varnothing$ |

**Theorem (the six root sets).** The symmetrised structures inherit the root sets of the general products from which they are made, the Jordan square being the plain square and the symmetrised quaternionic square being the norm times $e_0$. The plain family has a two-dimensional sphere of roots at the negative values and two points at the positive values; the quaternionic family has nothing at the negative values and a three-dimensional sphere at the positive values; the two antisymmetric structures have all of $\mathbb{H}$ at the value $0$ and nothing elsewhere.

*Proof.* The four rows of the first group are the two theorems of the plain and the quaternionic family, the symmetric structures having the same square as their general counterparts; the two rows of the second group are the theorem of the cross products. The dimensions are those of the spheres $S^2\subset\mathrm{Vect}(\mathbb{H})$ and $S^3\subset\mathbb{H}$.

**Remark (the reduction of the roots of $0$).** Five of the six structures reduce the roots of $0$ to the origin, and the failure of the reduction is confined to the two antisymmetric structures, whose square vanishes identically. The reduction holds for the plain family although the plain form is indefinite on the whole space, because the isotropic cone of the plain form meets the space only at the origin: $x_0^2-|\mathbf x|^2=0$ and $2x_0\mathbf x=0$ together force $\tilde x=0$. So the isotropic cone of the plain form is real only after complexification, and over $\mathbb{R}$ the roots of $0$ are the origin; this is the same definiteness that collapses the idempotents to the two-point set in *The Idempotents of the Six Structures*, above this article in this category.

## Summary

The root of a central value is an element whose square is the value times $e_0$, and the six squares group the six structures into a plain family, a quaternionic family and the two antisymmetric structures. The plain family, the general plain and the symmetric plain structures, has the sphere of radius $\sqrt{-\lambda}$ of pure elements as roots of a negative value, the origin as roots of $0$, and the two points $\pm\sqrt\lambda\,e_0$ as roots of a positive value; for the three values this is the sphere $S^2$ of roots of $-1$, the origin, and the two units. The quaternionic family, the general quaternionic and the symmetric quaternionic structures, has nothing for a negative value, the origin for $0$, and the sphere of radius $\sqrt\lambda$ for a positive value; for the three values this is the empty set, the origin, and the unit sphere $S^3$. The two antisymmetric structures have all of $\mathbb{H}$ as roots of $0$ and nothing else. So the two general products exchange the two spheres, and the reduction of the roots of $0$ to the origin fails only in the two cross products.

## Summary of Notation

| symbol | meaning |
|---|---|
| root of $\lambda$ in $\star$ | $\tilde\xi$ with $\tilde\xi\star\tilde\xi=\lambda e_0$ |
| $B(\tilde x)=x_0^2-\lvert\mathbf x\rvert^2$ | the plain form, the square of the plain family |
| $N(\tilde x)=x_0^2+\lvert\mathbf x\rvert^2$ | the quaternion form, the square of the quaternionic family |
| $S^2$ | the unit pure sphere, the roots of $-1$ in the plain family |
| $S^3$ | the unit sphere, the roots of $+1$ in the quaternionic family |
| $\{\pm e_0\}$ | the roots of $+1$ in the plain family |
| $\varnothing$, $\mathbb{H}$ | the root sets of the cross products, empty off $0$ and all of the space at $0$ |

## Further Reading

- *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-general-plain-algebra-of-quaternions.md`), above this article in this category, for the roots in the plain product.
- *The 2 Forms over the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-2-forms-over-the-quaternion-r-space.md`), for the plain form and the quaternion form.
- *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-6-algebraic-structures-over-the-quaternion-r-space.md`), for the six structures.
- *The Idempotents of the Six Structures* (`articles_maths/the-idempotents-of-the-six-structures.md`), above this article in this category, for the companion class.
- *The Square-Zero Elements of the Six Structures* (`articles_maths/the-square-zero-elements-of-the-six-structures.md`), below this article in this category, for the roots of $0$ of the antisymmetric products.
