# __Square Roots of a General Element__

## Introduction

Let $\star$ be a product on the quaternion space $\mathbb{H}$. An element $\tilde\xi$ is a **root of the central value** $\lambda e_0$ when its square in that product is the value,

$$
\tilde\xi\star\tilde\xi=\lambda e_0 , \qquad \lambda\in\mathbb{R},
$$

and the **root set** of the value is the set of its roots. The value is general here, and it is real: the space is the quaternion algebra over $\mathbb{R}$, whose centre is the real line, so a central value is a real multiple of $e_0$. The three values that carry a name, $-1$, $0$ and $+1$, are the values of the element theory of the algebra, and that reading is *Square Roots of Minus One, Zero and Plus One*, the companion of this article. Here the value stays general and the question is the one a general value asks: for which real $\lambda$ does a root exist, and what is the root set.

**The six names.** The space carries six products, so the general value poses six questions; this article answers them once for all six. Each product has a three-letter code: the first letter is the operation, $\mathrm G$ the general product and $\mathrm S$, $\mathrm A$ its symmetric and antisymmetric parts; the second is the product of the family, $\mathrm P$ the plain one and $\mathrm Q$ the quaternionic one, whose first factor is read through the conjugation; and the third letter is the same one for the six, $\mathrm A$ the algebra over $\mathbb{R}$. The six are read in the two families of *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*,

| the family | general | symmetric | antisymmetric |
|---|---|---|---|
| the plain algebra | $\mathrm{GPA}$ | $\mathrm{SPA}$ | $\mathrm{APA}$ |
| the quaternionic algebra | $\mathrm{GQA}$ | $\mathrm{SQA}$ | $\mathrm{AQA}$ |

and every table of the article follows this order, family by family and, inside a family, general then symmetric then antisymmetric.

**Scope and owners.** This article owns the general value for the six structures of the quaternion space: the two squares and their reductions of §*The Two General Products at a General Value*, the six-row table of §*The Six Root Sets at a General Value*, the three existence classes, the roots of $0$ and the scaling. The three named values and the geometry they carry are *Square Roots of Minus One, Zero and Plus One*. The products are *The 6 Products of the Quaternion $\mathbb{R}$ Space* and *The Two General Products of the Quaternion $\mathbb{R}$ Space*; the six structures are *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*; the vocabulary stated once for a general product is *Definitions for the Study of the 6 Algebraic Structures*; the two forms are *The 2 Forms over the Quaternion $\mathbb{R}$ Space*; and the neighbouring classes of elements are *Idempotents*, *Nilpotents*, *Annihilators* and *Zero Divisors*, below this article in this category.

**Conventions.** $\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ with $e_0=1$ and $e_1e_2=e_3$; a general element is $\tilde\xi=\xi_0e_0+\boldsymbol\xi$ with $\xi_0\in\mathbb{R}$ and $\boldsymbol\xi=\sum_k\xi_ke_k$; the conjugation is $\tilde\xi^{\natural}=\xi_0-\boldsymbol\xi$; the **plain form** is $B(\tilde\xi)=\xi_0^{2}-\lvert\boldsymbol\xi\rvert^{2}$ and the **quaternion form** is $N(\tilde\xi)=\xi_0^{2}+\lvert\boldsymbol\xi\rvert^{2}$, with $\lvert\boldsymbol\xi\rvert^{2}=\sum_k\xi_k^{2}$. The root is defined in *Definitions for the Study of the 6 Algebraic Structures* §*The Element Vocabulary* as a **non-zero** element with $\tilde\xi\star\tilde\xi=\lambda e_0$; a root set is read here as a solution set, so the origin is counted with the roots of $0$, and the places where an owner counts the non-zero roots alone are read as the origin alone.

## The Two General Products at a General Value

The quaternion space carries six structures and two general products, the plain product $\tilde\xi\tilde\eta$ and the quaternionic product $\tilde\xi^{\natural}\tilde\eta$; the two squares are the plain square and the quaternion form, and they are the two models of the general value.

### The Plain Product: The Vector–Scalar Reduction

The plain square is $\tilde\xi^{2}=B(\tilde\xi)e_0+2\xi_0\boldsymbol\xi$, an element with scalar part the plain form $B(\tilde\xi)=\xi_0^{2}-\lvert\boldsymbol\xi\rvert^{2}$ and vector part $2\xi_0\boldsymbol\xi$, and the equation $\tilde\xi^{2}=\lambda e_0$ is the pair

$$
B(\tilde\xi)=\lambda , \qquad 2\xi_0\boldsymbol\xi=0 .
$$

The second equation is the **vector–scalar reduction**: $\xi_0=0$ or $\boldsymbol\xi=0$. The case $\boldsymbol\xi=0$ gives the two central roots $\tilde\xi=\pm\sqrt\lambda\,e_0$, present for $\lambda>0$ and collapsing to the origin at $\lambda=0$, and absent for $\lambda<0$. The case $\xi_0=0$ gives the roots in the vector subspace, the solutions of $-\lvert\boldsymbol\xi\rvert^{2}=\lambda$, which are the sphere $\lvert\boldsymbol\xi\rvert^{2}=-\lambda$ of real dimension two for $\lambda<0$ and nothing for $\lambda>0$. So the plain product reads **every** real value: the negative values with the sphere of the vector subspace, the value $0$ with the origin, and the positive values with the two central points. The sphere of a negative value is the family of the complex structures on the vector subspace scaled by $\sqrt{-\lambda}$: a pure vector of unit length squares to $-e_0$, so the whole sphere is the family that the conversion of the plain product into an algebra over $\mathbb{C}$ uses.

### The Quaternionic Product: One Real Equation

The square of the quaternionic product is already central,

$$
\tilde\xi^{\natural}\tilde\xi=N(\tilde\xi)e_0 , \qquad N(\tilde\xi)=\xi_0^{2}+\lvert\boldsymbol\xi\rvert^{2} ,
$$

so the equation $\tilde\xi^{\natural}\tilde\xi=\lambda e_0$ is the single real equation $N(\tilde\xi)=\lambda$. The quaternion form is a sum of four real squares, hence non-negative, so a root exists exactly for a non-negative value: the origin alone at $\lambda=0$, and the sphere $N(\tilde\xi)=\lambda$ of real dimension three at $\lambda>0$. **Every positive value has a root and no negative value has one.**

The two general products exchange their sets of values, and the exchange is one sign. The plain form is indefinite on the vector subspace and the quaternion form is definite there, so the sphere of the plain product stands at the negative values and the sphere of the quaternionic product at the positive ones; it is the same exchange that separates the roots of $-1$ from the roots of $+1$ in the two general products of *The Two General Products of the Quaternion $\mathbb{R}$ Space*.

**Remark (the roots, the units and the zero divisors).** The space is the quaternion division algebra, so every non-zero element has the two-sided inverse $\tilde\xi^{-1}=\tilde\xi^{\natural}/N(\tilde\xi)$, and the zero-divisor set of the two general products is empty (*Zero Divisors*, below this article in this category). A root of a non-zero value is therefore invertible, and the roots of $0$ of the four structures whose square vanishes only there are the origin alone, no root of theirs being a zero divisor. The two sets are not the same set, though: the symmetric quaternionic structure has the whole punctured space as its zero-divisor set while its root of $0$ is the origin alone. The two sets meet in the two antisymmetric structures, whose square vanishes identically, so that every non-zero element is square-zero, its own annihilating partner, a zero divisor of the structure and a root of $0$.

## The Six Structures and the General Value

The square of a structure is its operation read at the two equal arguments, and each of the six carries a root problem of its own. The two general products are read above; the four derived ones are their symmetrisations and antisymmetrisations, and all six are read here, one by one.

### $\mathrm{GPA}$, the general plain algebra

The product is $\tilde\xi\tilde\eta$ and its square is the plain square, of scalar part $B$ and vector part $2\xi_0\boldsymbol\xi$. A root of $\lambda$ exists for **every** real $\lambda$, and the root set is the two central roots $\pm\sqrt\lambda\,e_0$ at a positive value, the origin at $0$, and the sphere of radius $\sqrt{-\lambda}$ in the vector subspace, of real dimension two, at a negative value. The product and its class are *Introduction to the General Plain Algebra of Quaternions*.

### $\mathrm{SPA}$, the symmetric plain algebra

The product is the symmetrisation $\tfrac12(\tilde\xi\tilde\eta+\tilde\eta\tilde\xi)$, which is commutative, and its square is the plain square. The root set of every real $\lambda$ is therefore the root set of $\mathrm{GPA}$, element for element. The product and its class are *Introduction to the Symmetric Plain Algebra of Quaternions*.

### $\mathrm{APA}$, the antisymmetric plain algebra

The product is the antisymmetrisation $\tfrac12(\tilde\xi\tilde\eta-\tilde\eta\tilde\xi)$, which is alternating, so its square vanishes identically and the equation reads $0=\lambda e_0$. The root of $0$ is every element of the space, and no other value has a root. The product and its class are *Introduction to the Antisymmetric Plain Algebra of Quaternions*.

### $\mathrm{GQA}$, the general quaternionic algebra

The product is $\tilde\xi^{\natural}\tilde\eta$ and its square is the central element $N(\tilde\xi)e_0$, so the equation is the single real equation $N(\tilde\xi)=\lambda$. A root exists exactly for a non-negative $\lambda$: the origin alone at $0$ and the sphere of radius $\sqrt\lambda$, of real dimension three, at a positive value; the negative values have none. The product and its class are *Introduction to the General Quaternionic Algebra of Quaternions*.

### $\mathrm{SQA}$, the symmetric quaternionic algebra

The product is the symmetrisation, and its square is the quaternion form as an element of the centre, $N(\tilde\xi)e_0$. The root set of a non-negative $\lambda$ is the same as for $\mathrm{GQA}$, and the negative values have none. The product and its class are *The Quaternion Form as a Product on the Symmetric Quaternionic Algebra of Quaternions*.

### $\mathrm{AQA}$, the antisymmetric quaternionic algebra

The product is the antisymmetrisation, its square vanishes identically, and the equation reads $0=\lambda e_0$. The root of $0$ is every element of the space, and no other value has a root. The product and its class are *Introduction to the Antisymmetric Quaternionic Algebra of Quaternions*.

## Results

The general value is read in the six structures, in the two general products and in the coordinates; the table of the existence classes is the one the companion article quotes at the three named values.

### The Six Root Sets at a General Value

The six root sets of the central value $\lambda e_0$ are collected below. The columns separate the three kinds of real value: the negative one, the value $0$, and the positive one.

| the structure | the square | $\lambda<0$ | $\lambda=0$ | $\lambda>0$ |
|---|---|---|---|---|
| $\mathrm{GPA}$ | $\tilde\xi^{2}$ | the sphere $\lvert\boldsymbol\xi\rvert^{2}=-\lambda$ in the vector subspace, real dimension $2$ | the origin alone | the pair $\pm\sqrt\lambda\,e_0$ |
| $\mathrm{SPA}$ | $\tilde\xi^{2}$ | the same sphere | the origin alone | the same pair |
| $\mathrm{APA}$ | $0$ | none | the whole space | none |
| $\mathrm{GQA}$ | $N(\tilde\xi)e_0$ | none | the origin alone | the sphere $N=\lambda$, real dimension $3$ |
| $\mathrm{SQA}$ | $N(\tilde\xi)e_0$ | none | the origin alone | the same sphere |
| $\mathrm{AQA}$ | $0$ | none | the whole space | none |

**Theorem (a root of $0$ exists for all six).** A root of $0$ exists for every one of the six structures, and it is the only central value with a root for the two antisymmetric structures. The root sets of the remaining values are governed by the table: the plain family reads every real value, the quaternionic family reads the non-negative values alone, and each family puts its sphere on one side of $0$ and its central roots on the other.

*Proof.* The root of $0$ is the vanishing of the square, which every structure has; the rows of the table are the theorems of §*The Six Structures and the General Value*, read in the two reductions of §*The Two General Products at a General Value*.

### The Two General Products at a General Value

**Theorem (the two general products at a general value).** For every real value $\lambda e_0$ the two general products have different root sets, and the difference is the exchange of the two spheres. The plain product answers with the pair $\pm\sqrt\lambda\,e_0$ at a positive value and with the sphere of the vector subspace at a negative value; the quaternionic product answers with the sphere of the whole space at a positive value and with nothing at a negative value. At $\lambda=0$ the two answer together with the origin.

*Proof.* The two root sets are the two reductions of §*The Two General Products at a General Value*: the plain reduction $B(\tilde\xi)=\lambda$, $2\xi_0\boldsymbol\xi=0$, and the single equation $N(\tilde\xi)=\lambda$. **The word is *differ*, not *coincide*.** The two squares differ by the sign of the vector part, $B(\tilde\xi)=\xi_0^{2}-\lvert\boldsymbol\xi\rvert^{2}$ against $N(\tilde\xi)=\xi_0^{2}+\lvert\boldsymbol\xi\rvert^{2}$, and that one sign moves the sphere from the negative values to the positive ones.

### The Three Existence Classes

The existence of a root separates the six structures into three classes, and the classes are read in the table of §*The Six Root Sets at a General Value*.

**Theorem (the three existence classes).** Among the six structures of the quaternion space the central-value root problem has a root of every real $\lambda$ for the two **plain** structures $\mathrm{GPA}$, $\mathrm{SPA}$; of every real $\lambda\geq0$ and of no negative one for the two **quaternionic** structures $\mathrm{GQA}$, $\mathrm{SQA}$; and of $\lambda=0$ alone for the two **antisymmetric** structures $\mathrm{APA}$, $\mathrm{AQA}$.

*Proof.* The plain square is the plain form times $e_0$ on the central line and the negative of the Euclidean square on the vector subspace, so it reaches every real value, at the vector subspace for the negative ones and on the central line for the positive ones; the quaternionic square is the quaternion form, a sum of four squares, so it reaches the non-negative values alone; and the square of an antisymmetric structure vanishes identically, so $\lambda=0$ is the only value it can read.

The classification is the sharpest of the category over the quaternion space, where the values are real: the plain structures answer every value, the quaternionic structures refuse exactly the negative values, and the antisymmetric structures answer for $0$ alone, with the whole space as the root of $0$.

**Remark (a sibling that keeps the square).** Each general product has a symmetric sibling, $\mathrm{SPA}$ of $\mathrm{GPA}$ and $\mathrm{SQA}$ of $\mathrm{GQA}$, and the sibling keeps the square and therefore the whole root set: the symmetrisation of a product does not change its diagonal, and the two symmetric structures answer with the same sphere and the same pair as their general partners. The coincidence is exact here, and it is the reason the six root sets collapse to four distinct sets and the existence classes to three.

### The Value in Coordinates and the Roots of Zero

Written on the coordinates, the root of $\lambda$ is the equation of the square of the family:

| the family | the equation of the root of $\lambda$ |
|---|---|
| the plain algebra | $\xi_0^{2}-\lvert\boldsymbol\xi\rvert^{2}=\lambda$ and $2\xi_0\boldsymbol\xi=0$ |
| the quaternionic algebra | $\xi_0^{2}+\lvert\boldsymbol\xi\rvert^{2}=\lambda$ |

The value $0$ is the row $\lambda=0$ of each equation, and it is the value every structure of the six reads:

| the structure | the roots of $0$ | real dimension |
|---|---|---|
| $\mathrm{GPA}$, $\mathrm{SPA}$ | the origin alone | $0$ |
| $\mathrm{GQA}$, $\mathrm{SQA}$ | the origin alone | $0$ |
| $\mathrm{APA}$, $\mathrm{AQA}$ | the whole space | $4$ |

The two antisymmetric structures reach the value $0$ by vanishing, and their root of $0$ is the space itself; the four others reach it at the origin alone, because the plain form is isotropic over $\mathbb{R}$ only at the origin and the quaternion form only there as well.

### The Two Families

The plain reduction cuts the space into two families, and the root sets of the plain product respect the cut.

**Definition.** An element is **pure** when its scalar part vanishes, $\xi_0=0$, and **central** when its vector part vanishes, $\boldsymbol\xi=0$.

The reduction of the plain square is the vanishing of the vector part, $2\xi_0\boldsymbol\xi=0$, and the two factors give the two families: the pure one, on which the reduction is satisfied identically, and the central one, on which it forces the vector part to vanish.

| | pure, $\xi_0=0$ | central, $\xi_0\neq0$ |
|---|---|---|
| the reduction $2\xi_0\boldsymbol\xi=0$ | satisfied identically | forces $\boldsymbol\xi=0$ |
| a root of $\lambda<0$ | the sphere of radius $\sqrt{-\lambda}$ | none |
| a root of $0$ | the origin alone | the origin alone |
| a root of $\lambda>0$ | none | the pair $\pm\sqrt\lambda\,e_0$ |

The two families meet only at the origin, and only in the case $\lambda=0$; for a non-zero $\lambda$ the plain root set has a member in one family alone, the pure one for a negative value and the central one for a positive value.

### The Scaling of the Root Set

**Theorem (the scaling).** Let $\mu\in\mathbb{R}$ and let $\tilde\xi$ be a root of $\lambda$. Then $\mu\tilde\xi$ is a root of $\mu^{2}\lambda$ in all six structures, the products being bilinear over $\mathbb{R}$. Consequently, for $\lambda>0$ and for the positive square root $\alpha=\sqrt\lambda$, multiplication by $\alpha$ is a bijection of the root set of $1$ onto the root set of $\lambda$ in the four bilateral structures, and, for $\lambda<0$ in the plain family, multiplication by $\sqrt{-\lambda}$ is a bijection of the unit sphere, the root set of $-1$, onto the sphere at $\lambda$. The root set of $0$ is a cone: the origin for the four structures whose square vanishes only there, and the whole space for the two whose square vanishes identically.

*Proof.* The square of a scaled element is $\mu^{2}(\tilde\xi\star\tilde\xi)=\mu^{2}\lambda e_0$ by the bilinearity of the products over $\mathbb{R}$. The two bijections are the reading of that identity at $\lambda=1$ and at $\lambda=-1$, and the cone is the vanishing set of a homogeneous square.

The scaling is the reason the plain sphere at a negative value is one sphere in different sizes, and the reason the two central roots at a positive value are the roots of $1$ in different sizes. It is also the reason the root set of a non-zero value is never a cone here: a scaling by $\mu$ carries $\lambda$ to $\mu^{2}\lambda$, so no non-zero multiple of a root of $\lambda$ is again a root of $\lambda$ unless $\mu^{2}=1$.

## Summary

The root of the central value $\lambda e_0$ in a structure is the element whose square in that structure is the value, and the value is general and real. The two general products give two reductions: the plain product reduces to the pair $B(\tilde\xi)=\xi_0^{2}-\lvert\boldsymbol\xi\rvert^{2}=\lambda$, $2\xi_0\boldsymbol\xi=0$, and the quaternionic product to the single real equation $N(\tilde\xi)=\xi_0^{2}+\lvert\boldsymbol\xi\rvert^{2}=\lambda$.

The plain product has a root of every real value: the two central roots $\pm\sqrt\lambda\,e_0$ at a positive value, the origin at $0$, and the sphere of radius $\sqrt{-\lambda}$ in the vector subspace, of real dimension two, at a negative value. The quaternionic product has a root exactly of the non-negative values: the origin at $0$ and the sphere of radius $\sqrt\lambda$, of real dimension three, at a positive value. The two products exchange their spheres through the one sign that separates the plain form $B$ from the quaternion form $N$.

The root of $0$ exists for all six structures, and it is the origin for the four whose square vanishes only there and the whole space for the two antisymmetric structures, whose square vanishes identically. Read among the six structures the existence question has three answers: a root of every real $\lambda$ for the two plain structures $\mathrm{GPA}$, $\mathrm{SPA}$; a root of every real $\lambda\geq0$ and of no negative one for the two quaternionic structures $\mathrm{GQA}$, $\mathrm{SQA}$; and a root of $0$ alone for the two antisymmetric structures $\mathrm{APA}$, $\mathrm{AQA}$. The symmetrisation keeps the square of its general partner and therefore the whole root set, and the scaling by $\mu$ carries the root set of $\lambda$ to the root set of $\mu^{2}\lambda$, the plain sphere at the negative values being one sphere in different sizes and the roots of $1$ being the pair $\pm e_0$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\lambda e_0$ | a central value, $\lambda\in\mathbb{R}$ |
| $\tilde\xi\star\tilde\xi$ | the square in the product at hand |
| $B(\tilde\xi)=\xi_0^{2}-\lvert\boldsymbol\xi\rvert^{2}$ | the plain form, the scalar part of the plain square |
| $N(\tilde\xi)=\xi_0^{2}+\lvert\boldsymbol\xi\rvert^{2}$ | the quaternion form, the square of the quaternionic product |
| $\boldsymbol\xi=\sum_k\xi_ke_k$ | the vector part, the home of the sphere of the plain product |
| $\mathrm{GPA},\dots,\mathrm{AQA}$ | the six structures of the space, the two families of three |

## Further Reading

- *Square Roots of Minus One, Zero and Plus One* (`articles_maths/quaternion-square-roots-of-minus-one-zero-and-plus-one.md`), the companion of this article, for the three values that carry a name.
- *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-general-plain-algebra-of-quaternions.md`), for the roots in the plain product.
- *The 6 Products of the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-6-products-of-the-quaternion-real-space.md`), for the six products and their operations.
- *The Two General Products of the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-two-general-products-of-the-quaternion-r-space.md`), for the plain product and the quaternionic product.
- *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-6-algebraic-structures-over-the-quaternion-r-space.md`), for the six names and the class of each.
- *Definitions for the Study of the 6 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-6-algebraic-structures.md`), for the root, the central value and the general vocabulary.
- *The 2 Forms over the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-2-forms-over-the-quaternion-r-space.md`), for the plain form and the quaternion form.
- *Introduction to the General Plain Algebra of Quaternions* (`articles_maths/introduction-to-the-general-plain-algebra-of-quaternions.md`), *Introduction to the Symmetric Plain Algebra of Quaternions* (`articles_maths/introduction-to-the-symmetric-plain-algebra-of-quaternions.md`) and *Introduction to the Antisymmetric Plain Algebra of Quaternions* (`articles_maths/introduction-to-the-antisymmetric-plain-algebra-of-quaternions.md`), for the three plain products.
- *Introduction to the General Quaternionic Algebra of Quaternions* (`articles_maths/introduction-to-the-general-quaternionic-algebra-of-quaternions.md`) and *The Quaternion Form as a Product on the Symmetric Quaternionic Algebra of Quaternions* (`articles_maths/the-quaternion-form-as-a-product-on-the-symmetric-quaternionic-algebra-of-quaternions.md`), for the quaternionic product and its symmetrisation.
- *Introduction to the Antisymmetric Quaternionic Algebra of Quaternions* (`articles_maths/introduction-to-the-antisymmetric-quaternionic-algebra-of-quaternions.md`), for the vanishing square.
- *Norm and Invertibility in the General Plain Algebra of Quaternions* (`articles_maths/norm-and-invertibility-in-the-general-plain-algebra-of-quaternions.md`) and *Zero Divisors* (`articles_maths/quaternion-zero-divisors.md`), for the unit that every non-zero root is and the absence of zero divisors.
- *Idempotents* (`articles_maths/quaternion-idempotents.md`), *Nilpotents* (`articles_maths/quaternion-nilpotents.md`), *Annihilators* (`articles_maths/quaternion-annihilators.md`), below this article in this category, for the roots of $-1$, of $0$ and the annihilating partners.
