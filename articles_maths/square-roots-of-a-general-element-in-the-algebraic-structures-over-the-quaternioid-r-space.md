# __Square Roots of a General Element in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space__

## Introduction

Let $\star$ be a product on the quaternion space $\mathbb{H}$. An element $\tilde\xi$ is a **root of the central value** $\lambda e_0$ when its square in that product is the value,

$$
\tilde\xi\star\tilde\xi=\lambda e_0 , \qquad \lambda\in\mathbb{R},
$$

and the **root set** of the value is the set of its roots. The value is general here, and it is real: the space is the quaternion algebra over $\mathbb{R}$, whose centre is the real line, so a central value is a real multiple of $e_0$. The named values are the two signed ones, $+1$ and $-1$, read with the idempotents in *Square Roots of One and the Idempotents in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*, and the value $0$, read with the nilpotents in *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*; the two are the companions of this article. Here the value stays general and the question is the one a general value asks: for which real $\lambda$ does a root exist, and what is the root set.

**The three companion structures.** Beside the algebra product of the *Quaternions* category, the space carries the three companion structures of this category, so the general value poses three questions besides the algebra one; this article answers the three once. The three are named in *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*:

$$
\mathrm{SPA} , \qquad \mathrm{APA} , \qquad \mathrm{GQA} ,
$$

the **symmetric plain algebra** of the Jordan product, the **antisymmetric plain algebra** of the cross product and the **general quaternionic algebra** of the product $\tilde\xi^{\natural}\tilde\eta$. Every table of the article follows this order.

**Scope and owners.** This article owns the general value for the three companion structures of the quaternion space: the two squares and their reductions of §*The Two General Products at a General Value*, the table of §*The Three Root Sets at a General Value*, the three existence classes, the roots of $0$ and the scaling. The two signed values $+1$ and $-1$, with the idempotents, are *Square Roots of One and the Idempotents in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*; the value $0$ and the nilpotents are *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*. The products are *The 6 Products of the Quaternioid Real Space* and *The Two General Products of the Quaternioid $\mathbb{R}$ Space*; the three companion structures are *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*; the vocabulary stated once for a general product is *Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*; the two forms are *The 2 Forms over the Quaternioid $\mathbb{R}$ Space*; and the neighbouring classes of elements are *Annihilators in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* and *Zero Divisors in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*, below this article in this category. The algebra-product root at the general value is owned by *Square Roots of a General Element in the Quaternion Algebra* in the *Quaternions* category.

**Conventions.** $\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ with $e_0=1$ and $e_1e_2=e_3$; a general element is $\tilde\xi=\xi_0e_0+\vec\xi$ with $\xi_0\in\mathbb{R}$ and $\vec\xi=\sum_k\xi_ke_k$; the conjugation is $\tilde\xi^{\natural}=\xi_0-\vec\xi$; the **plain form** is $\langle\tilde\xi\rangle=\xi_0^{2}-\lvert\vec\xi\rvert^{2}$ and the **quaternion form** is $\langle\tilde\xi\rangle_{\natural}=\xi_0^{2}+\lvert\vec\xi\rvert^{2}$, with $\lvert\vec\xi\rvert^{2}=\sum_k\xi_k^{2}$. The algebra product is $\tilde\xi\tilde\eta$, the general quaternionic product is $\tilde\xi^{\natural}\tilde\eta$, the Jordan product is $\tilde\xi\bullet\tilde\eta=\tfrac12(\tilde\xi\tilde\eta+\tilde\eta\tilde\xi)$, and the plain cross product is $\tilde\xi\wedge\tilde\eta=\tfrac12(\tilde\xi\tilde\eta-\tilde\eta\tilde\xi)=\vec\xi\times\vec\eta$. The root is defined in *Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* §*The Element Vocabulary* as a **non-zero** element with $\tilde\xi\star\tilde\xi=\lambda e_0$; a root set is read here as a solution set, so the origin is counted with the roots of $0$, and the places where an owner counts the non-zero roots alone are read as the origin alone.

## The Two General Products at a General Value

The quaternion space carries the algebra product $\tilde\xi\tilde\eta$ and the general quaternionic product $\tilde\xi^{\natural}\tilde\eta$; the two squares are the plain square and the quaternion form, and they are the two models of the general value.

### The Plain Product: The Vector–Scalar Reduction

The plain square is $\tilde\xi^{2}=\langle\tilde\xi\rangle e_0+2\xi_0\vec\xi$, an element with scalar part the plain form $\langle\tilde\xi\rangle=\xi_0^{2}-\lvert\vec\xi\rvert^{2}$ and vector part $2\xi_0\vec\xi$, and the equation $\tilde\xi^{2}=\lambda e_0$ is the pair

$$
\langle\tilde\xi\rangle=\lambda , \qquad 2\xi_0\vec\xi=0 .
$$

The second equation is the **vector–scalar reduction**: $\xi_0=0$ or $\vec\xi=0$. The case $\vec\xi=0$ gives the two central roots $\tilde\xi=\pm\sqrt\lambda\,e_0$, present for $\lambda>0$ and collapsing to the origin at $\lambda=0$, and absent for $\lambda<0$. The case $\xi_0=0$ gives the roots in the vector subspace, the solutions of $-\lvert\vec\xi\rvert^{2}=\lambda$, which are the sphere $\lvert\vec\xi\rvert^{2}=-\lambda$ of real dimension two for $\lambda<0$ and nothing for $\lambda>0$. So the plain product reads **every** real value: the negative values with the sphere of the vector subspace, the value $0$ with the origin, and the positive values with the two central points. The sphere of a negative value is the family of the complex structures on the vector subspace scaled by $\sqrt{-\lambda}$: a pure unit vector squares to $-e_0$, so the whole sphere is the family that the conversion of the plain product into an algebra over $\mathbb{C}$ uses.

### The Quaternionic Product: One Real Equation

The square of the quaternionic product is already central,

$$
\tilde\xi^{\natural}\tilde\xi=\langle\tilde\xi\rangle_{\natural}e_0 , \qquad \langle\tilde\xi\rangle_{\natural}=\xi_0^{2}+\lvert\vec\xi\rvert^{2} ,
$$

so the equation $\tilde\xi^{\natural}\tilde\xi=\lambda e_0$ is the single real equation $\langle\tilde\xi\rangle_{\natural}=\lambda$. The quaternion form is a sum of four real squares, hence non-negative, so a root exists exactly for a non-negative value: the origin alone at $\lambda=0$, and the sphere $\langle\tilde\xi\rangle_{\natural}=\lambda$ of real dimension three at $\lambda>0$. **Every positive value has a root and no negative value has one.**

The two products exchange their sets of values, and the exchange is one sign. The plain form is indefinite on the vector subspace and the quaternion form is definite there, so the sphere of the plain product stands at the negative values and the sphere of the quaternionic product at the positive ones; it is the same exchange that separates the roots of $-1$ from the roots of $+1$ in the two products.

**Remark (the roots, the units and the zero divisors).** The space is the quaternion division algebra, so every non-zero element has the two-sided inverse $\tilde\xi^{-1}=\tilde\xi^{\natural}/\langle\tilde\xi\rangle_{\natural}$, and the zero-divisor set of the two general products is empty (*Zero Divisors in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*, below this article in this category). A root of a non-zero value is therefore invertible, and the roots of $0$ of the two companion structures whose square vanishes only there are the origin alone, no root of theirs being a zero divisor. The two sets are not the same set, though: the symmetric plain structure has the whole punctured vector subspace as its zero-divisor set while its root of $0$ is the origin alone. The two sets meet in the antisymmetric plain structure, whose square vanishes identically, so that every non-zero element is square-zero, its own annihilating partner, a zero divisor of the structure and a root of $0$.

## The Three Companion Structures and the General Value

The square of a structure is its operation read at the two equal arguments, and each of the three carries a root problem of its own. The algebra product is read above; the two other companion structures are its symmetrisation and antisymmetrisation, and all three are read here, one by one.

### $\mathrm{GQA}$, the general quaternionic algebra

The product is $\tilde\xi^{\natural}\tilde\eta$ and its square is the central element $\langle\tilde\xi\rangle_{\natural}e_0$, so the equation is the single real equation $\langle\tilde\xi\rangle_{\natural}=\lambda$. A root exists exactly for a non-negative $\lambda$: the origin alone at $0$ and the sphere of radius $\sqrt\lambda$, of real dimension three, at a positive value; the negative values have none. The product and its class are *Introduction to the General Quaternionic Algebra*.

### $\mathrm{SPA}$, the symmetric plain algebra

The product is the symmetrisation $\tfrac12(\tilde\xi\tilde\eta+\tilde\eta\tilde\xi)$, which is commutative, and its square is the plain square. The root set of every real $\lambda$ is therefore the plain root set, element for element: the two central roots $\pm\sqrt\lambda\,e_0$ at a positive value, the origin at $0$, and the sphere of radius $\sqrt{-\lambda}$ in the vector subspace, of real dimension two, at a negative value. The product and its class are *Introduction to the Symmetric Plain Algebra*.

### $\mathrm{APA}$, the antisymmetric plain algebra

The product is the antisymmetrisation $\tfrac12(\tilde\xi\tilde\eta-\tilde\eta\tilde\xi)$: it is the cross product $\tilde\xi\wedge\tilde\eta=\vec\xi\times\vec\eta$, which is alternating, so its square vanishes identically and the equation reads $0=\lambda e_0$. The root of $0$ is every element of the space, and no other value has a root. The product and its class are *Introduction to the Antisymmetric Plain Algebra*.

## Results

The general value is read in the three companion structures, in the two products and in the coordinates; the table of the existence classes is the one the companion articles quote at the named values.

### The Three Root Sets at a General Value

The three root sets of the central value $\lambda e_0$ are collected below. The columns separate the three kinds of real value: the negative one, the value $0$, and the positive one.

| the structure | the square | $\lambda<0$ | $\lambda=0$ | $\lambda>0$ |
|---|---|---|---|---|
| $\mathrm{GQA}$ | $\langle\tilde\xi\rangle_{\natural}e_0$ | none | the origin alone | the sphere $N=\lambda$, real dimension $3$ |
| $\mathrm{SPA}$ | $\tilde\xi^{2}$ | the sphere $\lvert\vec\xi\rvert^{2}=-\lambda$ in the vector subspace, real dimension $2$ | the origin alone | the pair $\pm\sqrt\lambda\,e_0$ |
| $\mathrm{APA}$ | $0$ | none | the whole space | none |

**Theorem (a root of $0$ exists for all three).** A root of $0$ exists for every one of the three companion structures, and it is the only central value with a root for the antisymmetric plain structure. The root sets of the remaining values are governed by the table: the symmetric plain structure reads every real value and the general quaternionic structure reads the non-negative values alone, and the two put their sphere on opposite sides of $0$, the sphere of the symmetric plain structure at a negative value and that of the general quaternionic structure at a positive one. The algebra product reads every real value as well, as owned by the *Quaternions* category.

*Proof.* The root of $0$ is the vanishing of the square, which every structure has; the rows of the table are the theorems of §*The Three Companion Structures and the General Value*, read in the two reductions of §*The Two General Products at a General Value*.

### The Two Products at a General Value

**Theorem (the two products at a general value).** For every real value $\lambda e_0$ the algebra product and the general quaternionic product have different root sets, and the difference is the exchange of the two spheres. The algebra product answers with the pair $\pm\sqrt\lambda\,e_0$ at a positive value and with the sphere of the vector subspace at a negative value; the general quaternionic product answers with the sphere of the whole space at a positive value and with nothing at a negative value. At $\lambda=0$ the two answer together with the origin.

*Proof.* The two root sets are the two reductions of §*The Two General Products at a General Value*: the plain reduction $\langle\tilde\xi\rangle=\lambda$, $2\xi_0\vec\xi=0$, and the single equation $\langle\tilde\xi\rangle_{\natural}=\lambda$. **The word is *differ*, not *coincide*.** The two squares differ by the sign of the vector part, $\langle\tilde\xi\rangle=\xi_0^{2}-\lvert\vec\xi\rvert^{2}$ against $\langle\tilde\xi\rangle_{\natural}=\xi_0^{2}+\lvert\vec\xi\rvert^{2}$, and that one sign moves the sphere from the negative values to the positive ones.

### The Three Existence Classes

The existence of a root separates the three companion structures into three classes, and the classes are read in the table of §*The Three Root Sets at a General Value*.

**Theorem (the three existence classes).** Among the three companion structures of the quaternion space the central-value root problem has a root of every real $\lambda$ for the **symmetric plain** structure $\mathrm{SPA}$; of every real $\lambda\geq0$ and of no negative one for the **general quaternionic** structure $\mathrm{GQA}$; and of $\lambda=0$ alone for the **antisymmetric plain** structure $\mathrm{APA}$. The algebra product has a root of every real $\lambda$, as owned by the *Quaternions* category.

*Proof.* The plain square is the plain form times $e_0$ on the central line and the negative of the Euclidean square on the vector subspace, so it reaches every real value, at the vector subspace for the negative ones and on the central line for the positive ones; the quaternionic square is the quaternion form, a sum of four squares, so it reaches the non-negative values alone; and the square of the antisymmetric plain structure vanishes identically, so $\lambda=0$ is the only value it can read.

The classification is the sharpest of the category over the quaternion space, where the values are real: the symmetric plain structure answers every value, the general quaternionic structure refuses exactly the negative values, and the antisymmetric plain structure answers for $0$ alone, with the whole space as the root of $0$.

### The Value in Coordinates and the Roots of Zero

Written on the coordinates, the root of $\lambda$ is the equation of the family:

| the family | the equation of the root of $\lambda$ |
|---|---|
| the plain square | $\xi_0^{2}-\lvert\vec\xi\rvert^{2}=\lambda$ and $2\xi_0\vec\xi=0$ |
| the quaternion square | $\xi_0^{2}+\lvert\vec\xi\rvert^{2}=\lambda$ |

The value $0$ is the row $\lambda=0$ of each equation, and it is the value every companion structure reads:

| the structure | the roots of $0$ | real dimension |
|---|---|---|
| $\mathrm{GQA}$, $\mathrm{SPA}$ | the origin alone | $0$ |
| $\mathrm{APA}$ | the whole space | $4$ |

The antisymmetric plain structure reaches the value $0$ by vanishing, and its root of $0$ is the space itself; the two others reach it at the origin alone, because the plain square vanishes over $\mathbb{R}$ only at the origin and the quaternion form is positive definite.

### The Two Families

The plain reduction cuts the space into two families, and the root sets of the plain square respect the cut.

**Definition.** An element is **pure** when its scalar part vanishes, $\xi_0=0$, and **central** when its vector part vanishes, $\vec\xi=0$.

The reduction of the plain square is the vanishing of the vector part, $2\xi_0\vec\xi=0$, and the two factors give the two families: the pure one, on which the reduction is satisfied identically, and the central one, on which it forces the vector part to vanish.

| | pure, $\xi_0=0$ | central, $\xi_0\neq0$ |
|---|---|---|
| the reduction $2\xi_0\vec\xi=0$ | satisfied identically | forces $\vec\xi=0$ |
| a root of $\lambda<0$ | the sphere of radius $\sqrt{-\lambda}$ | none |
| a root of $0$ | the origin alone | the origin alone |
| a root of $\lambda>0$ | none | the pair $\pm\sqrt\lambda\,e_0$ |

The two families meet only at the origin, and only in the case $\lambda=0$; for a non-zero $\lambda$ the plain root set has a member in one family alone, the pure one for a negative value and the central one for a positive value.

### The Scaling of the Root Set

**Theorem (the scaling).** Let $\mu\in\mathbb{R}$ and let $\tilde\xi$ be a root of $\lambda$. Then $\mu\tilde\xi$ is a root of $\mu^{2}\lambda$ in all three companion structures, the products being bilinear over $\mathbb{R}$. Consequently, for $\lambda>0$ and for the positive square root $\alpha=\sqrt\lambda$, multiplication by $\alpha$ is a bijection of the root set of $1$ onto the root set of $\lambda$ in the structures that have a root of $1$, and, for $\lambda<0$ in the plain square, multiplication by $\sqrt{-\lambda}$ is a bijection of the pure unit sphere, the root set of $-1$, onto the sphere at $\lambda$. The root set of $0$ is a cone: the origin for the two structures whose square vanishes only there, and the whole space for the one whose square vanishes identically.

*Proof.* The square of a scaled element is $\mu^{2}(\tilde\xi\star\tilde\xi)=\mu^{2}\lambda e_0$ by the bilinearity of the products over $\mathbb{R}$. The two bijections are the reading of that identity at $\lambda=1$ and at $\lambda=-1$, and the cone is the vanishing set of a homogeneous square.

The scaling is the reason the plain sphere at a negative value is one sphere in different sizes, and the reason the two central roots at a positive value are the roots of $1$ in different sizes. It is also the reason the root set of a non-zero value is never a cone here: a scaling by $\mu$ carries $\lambda$ to $\mu^{2}\lambda$, so no non-zero multiple of a root of $\lambda$ is again a root of $\lambda$ unless $\mu^{2}=1$.

## Summary

The root of the central value $\lambda e_0$ in a structure is the element whose square in that structure is the value, and the value is general and real. The two products give two reductions: the algebra product reduces to the pair $\langle\tilde\xi\rangle=\xi_0^{2}-\lvert\vec\xi\rvert^{2}=\lambda$, $2\xi_0\vec\xi=0$, and the general quaternionic product to the single real equation $\langle\tilde\xi\rangle_{\natural}=\xi_0^{2}+\lvert\vec\xi\rvert^{2}=\lambda$.

The plain square has a root of every real value: the two central roots $\pm\sqrt\lambda\,e_0$ at a positive value, the origin at $0$, and the sphere of radius $\sqrt{-\lambda}$ in the vector subspace, of real dimension two, at a negative value. The quaternion square has a root exactly of the non-negative values: the origin at $0$ and the sphere of radius $\sqrt\lambda$, of real dimension three, at a positive value. The two squares exchange their spheres through the one sign that separates the plain form $\langle\cdot,\cdot\rangle$ from the quaternion form $\langle\cdot,\cdot\rangle_{\natural}$.

The root of $0$ exists for all three companion structures, and it is the origin for the two whose square vanishes only there and the whole space for the antisymmetric plain structure, whose square vanishes identically. Read among the three companion structures the existence question has three answers: a root of every real $\lambda$ for the symmetric plain structure $\mathrm{SPA}$; a root of every real $\lambda\geq0$ and of no negative one for the general quaternionic structure $\mathrm{GQA}$; and a root of $0$ alone for the antisymmetric plain structure $\mathrm{APA}$. The algebra product has a root of every real $\lambda$, as owned by the *Quaternions* category. The scaling by $\mu$ carries the root set of $\lambda$ to the root set of $\mu^{2}\lambda$, the plain sphere at the negative values being one sphere in different sizes and the roots of $1$ being the pair $\pm e_0$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\lambda e_0$ | a central value, $\lambda\in\mathbb{R}$ |
| $\tilde\xi\star\tilde\xi$ | the square in the product at hand |
| $\langle\tilde\xi\rangle=\xi_0^{2}-\lvert\vec\xi\rvert^{2}$ | the plain form, the scalar part of the plain square |
| $\langle\tilde\xi\rangle_{\natural}=\xi_0^{2}+\lvert\vec\xi\rvert^{2}$ | the quaternion form, the square of the general quaternionic product |
| $\vec\xi=\sum_k\xi_ke_k$ | the vector part, the home of the sphere of the plain square |
| $\mathrm{SPA},\mathrm{APA},\mathrm{GQA}$ | the three companion structures of the space |

## Further Reading

- *Square Roots of One and the Idempotents in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/square-roots-of-one-and-the-idempotents-in-the-algebraic-structures-over-the-quaternioid-r-space.md`), the companion of this article, for the two signed values $+1$ and $-1$ and the idempotents.
- *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/square-roots-of-zero-and-the-nilpotents-in-the-algebraic-structures-over-the-quaternioid-r-space.md`), the companion of this article, for the value $0$ and the nilpotents.
- *The 6 Products of the Quaternioid Real Space* (`articles_maths/the-6-products-of-the-quaternioid-real-space.md`), for the companion products and their operations.
- *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/the-algebraic-structures-over-the-quaternioid-r-space.md`), for the three companion names and the class of each.
- *Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-quaternioid-r-space.md`), for the root, the central value and the general vocabulary.
- *The 2 Forms over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/the-2-forms-over-the-quaternioid-r-space.md`), for the plain form and the quaternion form.
- *Introduction to the General Quaternionic Algebra* (`articles_maths/introduction-to-the-general-quaternionic-algebra-of-quaternioid.md`), for the general quaternionic product and its class.
- *Introduction to the Symmetric Plain Algebra* (`articles_maths/introduction-to-the-symmetric-plain-algebra-of-quaternioid.md`), for the Jordan product and its class.
- *Introduction to the Antisymmetric Plain Algebra* (`articles_maths/introduction-to-the-antisymmetric-plain-algebra-of-quaternioid.md`), for the cross product and the vanishing square.
- *Square Roots of a General Element in the Quaternion Algebra* (`articles_maths/square-roots-of-a-general-element-in-the-quaternion-algebra.md`), in the *Quaternions* category, for the algebra-product root at the general value.
- *Norm and Invertibility in the Quaternion Algebra* (`articles_maths/norm-and-invertibility-in-the-quaternion-algebra.md`) and *Zero Divisors in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/zero-divisors-in-the-algebraic-structures-over-the-quaternioid-r-space.md`), for the unit that every non-zero root is and the absence of zero divisors.
- *Annihilators in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/annihilators-in-the-algebraic-structures-over-the-quaternioid-r-space.md`), below this article in this category, for the roots of $0$ and the annihilating partners.
