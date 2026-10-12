# __Square Roots of a General Element__

## Introduction

A root of a central value in a structure is an element whose square in that structure is the value times $e_0$. The quaternion space carries six structures, and this article reads the root equation $\tilde\xi\star\tilde\xi=\lambda e_0$ for every real $\lambda$ and for all six: the two general products exchange a sphere for the empty set, the four structures whose square vanishes only at the origin reduce the roots of $0$ to the origin, and the two cross products alone admit the whole space as roots of $0$. The three values that carry a name, $-1$, $0$ and $+1$, are *Square Roots of Minus One, Zero and Plus One*, which is the companion of this article. The products are *The 6 Products of the Quaternion Real Space* and *The Two General Products of the Quaternion $\mathbb{R}$ Space*, the six structures are *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, and the definitions are *Definitions for the Study of the 6 Algebraic Structures*, all above this article in this category.

## Roots of a Central Value

**Definition.** Let $\star$ be a product on $\mathbb{H}$ and let $\lambda\in\mathbb{R}$. A **root of $\lambda$** in $\star$ is an element $\tilde\xi$ with
$$
\tilde\xi\star\tilde\xi=\lambda e_0 .
$$
The root set is read relative to the product, as the name *root of $-1$ in the general plain product* records, and the value is central, so the equation is an equality of quaternions with a real right-hand side. The value is left general here; the three particular values $-1,0,+1$ and the geometry they carry are the subject of *Square Roots of Minus One, Zero and Plus One*.

## The Two Squares and the Two Forms

The root equation is the square equation, and the six squares of *Idempotents* group the six structures in two:

| structure | square of $\tilde x$ | root equation |
|---|---|---|
| $\mathrm{GPA}$ | $(x_0^2-\lvert\mathbf x\rvert^2)e_0+2x_0\mathbf x$ | $B(\tilde x)=x_0^2-\lvert\mathbf x\rvert^2=\lambda$ and $2x_0\mathbf x=0$ |
| $\mathrm{SPA}$ | $(x_0^2-\lvert\mathbf x\rvert^2)e_0+2x_0\mathbf x$ | $B(\tilde x)=x_0^2-\lvert\mathbf x\rvert^2=\lambda$ and $2x_0\mathbf x=0$ |
| $\mathrm{APA}$ | $0$ | $0=\lambda$ |
| $\mathrm{GQA}$ | $N(\tilde x)e_0$ | $N(\tilde x)=\lambda$ |
| $\mathrm{SQA}$ | $N(\tilde x)e_0$ | $N(\tilde x)=\lambda$ |
| $\mathrm{AQA}$ | $0$ | $0=\lambda$ |

The plain square carries the plain form $B(\tilde x)=x_0^2-|\mathbf x|^2$; the quaternionic square carries the quaternion form $N(\tilde x)=x_0^2+|\mathbf x|^2$. The two forms are definite and opposite on the vector subspace, and this one sign is the whole difference between the two families below.

## The Roots in the Plain Family

**Theorem (the roots of a central value in the plain product).** For the general plain and the symmetric plain structures, the roots of $\lambda$ are
$$
\lambda<0:\quad\{\mathbf u:|\mathbf u|^2=-\lambda\}\ \text{in the vector subspace} ,\qquad
\lambda=0:\quad\{0\} ,\qquad
\lambda>0:\quad\{\pm\sqrt\lambda\,e_0\} .
$$
The root set of a negative value is the sphere of radius $\sqrt{-\lambda}$ in the vector subspace, of real dimension two; the roots of $0$ are the origin alone; and the roots of a positive value are the two central points $\pm\sqrt\lambda\,e_0$.

*Proof.* The square is $\tilde\xi^2=(\xi_0^2-|\boldsymbol\xi|^2)e_0+2\xi_0\boldsymbol\xi$, and the vector part $2\xi_0\boldsymbol\xi$ vanishes when $\xi_0=0$ or $\boldsymbol\xi=0$. If $\boldsymbol\xi=0$ the equation is $\xi_0^2=\lambda$, with no real solution for $\lambda<0$, the single element $0$ for $\lambda=0$, and the two elements $\pm\sqrt\lambda\,e_0$ for $\lambda>0$. If $\xi_0=0$ the equation is $-|\boldsymbol\xi|^2=\lambda$, with no solution for $\lambda>0$, the single element $0$ for $\lambda=0$, and the sphere $|\boldsymbol\xi|^2=-\lambda$ of real dimension two for $\lambda<0$. The two branches are disjoint except at the origin, which they share only in the case $\lambda=0$.

The sphere of roots of a negative value is the family of the complex structures on the vector subspace scaled by $\sqrt{-\lambda}$: a pure vector of unit length squares to $-e_0$, so it is a multiplication by a complex structure, and the whole sphere carries the continuous family. This is the family the conversion of the plain product into an algebra over $\mathbb{C}$ uses, and it is the reason the plain family has a continuous root set at the negative values while the quaternionic family has none. The unit case of this sphere, the named value $-1$, is the subject of *Square Roots of Minus One, Zero and Plus One*.

## The Roots in the Quaternionic Family

**Theorem (the roots of a central value in the quaternionic product).** For the general quaternionic and the symmetric quaternionic structures, the roots of $\lambda$ are
$$
\lambda<0:\quad\varnothing ,\qquad
\lambda=0:\quad\{0\} ,\qquad
\lambda>0:\quad\{\tilde\xi:N(\tilde\xi)=\lambda\} ,
$$
the last being the sphere of radius $\sqrt\lambda$ in the four-dimensional space, of real dimension three.

*Proof.* The square of the quaternionic family is $N(\tilde\xi)e_0$, so the root equation is the single real equation $N(\tilde\xi)=\lambda$. The quaternion form is a sum of four real squares, $N(\tilde\xi)=\xi_0^2+|\boldsymbol\xi|^2$, hence nonnegative; the equation is empty for $\lambda<0$, the single element $0$ for $\lambda=0$, and the sphere of radius $\sqrt\lambda$, of real dimension three, for $\lambda>0$.

The two families exchange the signs: the plain family has its sphere at the negative values and two points at the positive values, while the quaternionic family has its sphere at the positive values and nothing at the negative values. The exchange is the sign between the plain form $B$ and the quaternion form $N$ on the vector subspace, and it is the same exchange that separates the roots of $-1$ from the roots of $+1$ in the two general products of *The Two General Products of the Quaternion $\mathbb{R}$ Space*.

## The Roots in the Antisymmetric Structures

**Theorem (the roots in the cross products).** For the plain cross product and the quaternionic cross product the root set of $\lambda$ is the whole space for $\lambda=0$ and is empty for $\lambda\neq0$.

*Proof.* Both products are alternating, so their square vanishes identically; the equation $0=\lambda e_0$ is satisfied by every element when $\lambda=0$ and by none when $\lambda\neq0$.

The antisymmetric structures are the one place of the six where the roots of $0$ are not the origin but the whole space, and they have no root of any other value. The failure is total: the two structures admit no root of a nonzero central value at all, and their roots of $0$ are all of $\mathbb{H}$.

## The Six Root Sets Side by Side

For a general central value $\lambda$ the six root sets are

| structure | $\lambda<0$ | $\lambda=0$ | $\lambda>0$ |
|---|---|---|---|
| $\mathrm{GPA}$ | the sphere of radius $\sqrt{-\lambda}$ in $\mathrm{Vect}(\mathbb{H})$, dimension two | $\{0\}$ | $\{\pm\sqrt\lambda\,e_0\}$ |
| $\mathrm{SPA}$ | the same sphere | $\{0\}$ | $\{\pm\sqrt\lambda\,e_0\}$ |
| $\mathrm{APA}$ | $\varnothing$ | $\mathbb{H}$ | $\varnothing$ |
| $\mathrm{GQA}$ | $\varnothing$ | $\{0\}$ | the sphere of radius $\sqrt\lambda$ in $\mathbb{H}$, dimension three |
| $\mathrm{SQA}$ | $\varnothing$ | $\{0\}$ | the same sphere |
| $\mathrm{AQA}$ | $\varnothing$ | $\mathbb{H}$ | $\varnothing$ |

**Theorem (the six root sets).** The symmetrised structures inherit the root sets of the general products from which they are made, the Jordan square being the plain square and the symmetrised quaternionic square being the norm times $e_0$. The plain family has a two-dimensional sphere of roots at the negative values and two points at the positive values; the quaternionic family has nothing at the negative values and a three-dimensional sphere at the positive values; the two antisymmetric structures have all of $\mathbb{H}$ at the value $0$ and nothing elsewhere.

*Proof.* The rows of $\mathrm{SPA}$ and $\mathrm{SQA}$ repeat those of $\mathrm{GPA}$ and $\mathrm{GQA}$, the symmetric structures having the same square as their general counterparts, and the rows of $\mathrm{APA}$ and $\mathrm{AQA}$ are the theorem of the cross products. The dimensions are those of a two-sphere in the vector subspace and a three-sphere in the space.

## The Roots of Zero Are the Square-Zero Elements

**Theorem (the reduction of the roots of $0$).** For every one of the six structures the root set of $0$ is the square-zero set of the structure, so a nonzero root of $0$ is at once a square-zero element, a zero divisor of the structure and its own annihilating partner. Four of the six reduce that set to the origin; the two antisymmetric structures have all of $\mathbb{H}$.

*Proof.* The two equations $\tilde\xi\star\tilde\xi=\lambda e_0$ and $\tilde\xi\star\tilde\xi=0$ are the same equation at $\lambda=0$, so the root set of $0$ is the square-zero set; the reading of a nonzero square-zero element as a zero divisor and as its own annihilating partner is the definition of the class (*Nilpotents*, *Annihilators*). The reduction holds for the plain family although the plain form is indefinite on the whole space, because the isotropic cone of the plain form meets the space only at the origin: $x_0^2-|\mathbf x|^2=0$ and $2x_0\mathbf x=0$ together force $\tilde x=0$. So the isotropic cone of the plain form is real only after complexification, and over $\mathbb{R}$ the roots of $0$ are the origin; this is the same absence of an isotropic direction that collapses the idempotents to the two-point set in *Idempotents*, below this article in this category.

## Summary

The root of a central value is an element whose square is the value times $e_0$, and the six squares group the six structures into a plain family, a quaternionic family and the two antisymmetric structures. The plain family, the general plain and the symmetric plain structures, has the sphere of radius $\sqrt{-\lambda}$ of pure elements as roots of a negative value, the origin as roots of $0$, and the two points $\pm\sqrt\lambda\,e_0$ as roots of a positive value. The quaternionic family, the general quaternionic and the symmetric quaternionic structures, has nothing for a negative value, the origin for $0$, and the sphere of radius $\sqrt\lambda$ for a positive value. The two antisymmetric structures have all of $\mathbb{H}$ as roots of $0$ and nothing else. So the two general products exchange the two spheres, and the reduction of the roots of $0$ to the origin fails only in the two cross products, where the roots of $0$ are the square-zero elements of the structure.

## Summary of Notation

| symbol | meaning |
|---|---|
| root of $\lambda$ in $\star$ | $\tilde\xi$ with $\tilde\xi\star\tilde\xi=\lambda e_0$ |
| $B(\tilde x)=x_0^2-\lvert\mathbf x\rvert^2$ | the plain form, the square of the plain family |
| $N(\tilde x)=x_0^2+\lvert\mathbf x\rvert^2$ | the quaternion form, the square of the quaternionic family |
| $\mathrm{Vect}(\mathbb{H})$ | the vector subspace, the home of the roots of a negative value in the plain family |
| $\varnothing$ | the root set of a nonzero value in the two cross products |
| $\mathbb{H}$ | the root set of $0$ in the two cross products |

## Further Reading

- *Square Roots of Minus One, Zero and Plus One* (`articles_maths/quaternion-square-roots-of-minus-one-zero-and-plus-one.md`), the companion of this article, for the three values that carry a name.
- *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-general-plain-algebra-of-quaternions.md`), above this article in this category, for the roots in the plain product.
- *The 2 Forms over the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-2-forms-over-the-quaternion-r-space.md`), for the plain form and the quaternion form.
- *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-6-algebraic-structures-over-the-quaternion-r-space.md`), for the six structures.
- *Idempotents* (`articles_maths/quaternion-idempotents.md`), below this article in this category, for the companion class.
- *Nilpotents* (`articles_maths/quaternion-nilpotents.md`), below this article in this category, for the roots of $0$ of the antisymmetric products.
