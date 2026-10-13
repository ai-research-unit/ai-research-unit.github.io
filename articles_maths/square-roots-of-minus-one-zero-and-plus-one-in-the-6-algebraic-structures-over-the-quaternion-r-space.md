# __Square Roots of Minus One, Zero and Plus One in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space__

## Introduction

Let $\star$ be a product on the quaternion algebra $\mathbb{H}$. An element $\tilde\xi$ is a **root of the central value** $\lambda e_0$ when its square in that product is the value,

$$
\tilde\xi\star\tilde\xi=\lambda e_0 , \qquad \lambda\in\mathbb{R},
$$

and the **root set** of the value is the set of its roots. The value is real because the space is real. Three values carry a name, $-1$, $0$ and $+1$, and they are the values on which the element theory of the algebra is built: the roots of $-1$ of the plain product are the complex structures of the space, the roots of $0$ are the square-zero elements, and the roots of $+1$ are the central units of the plain family and the unit sphere of the quaternionic family.

**The six names.** The space carries six products, so the generic definition poses six questions; this article answers them once for all six. Each product has a three-letter code: the first letter is the operation, $\mathrm G$ the general product and $\mathrm S$, $\mathrm A$ its symmetric and antisymmetric parts; the second is the product of the family, $\mathrm P$ the plain one and $\mathrm Q$ the quaternionic one, whose first factor is read through the natural conjugation. The six are read in the two families of *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*,

| the family | general | symmetric | antisymmetric |
|---|---|---|---|
| the plain algebra | $\mathrm{GPA}$ | $\mathrm{SPA}$ | $\mathrm{APA}$ |
| the quaternionic algebra | $\mathrm{GQA}$ | $\mathrm{SQA}$ | $\mathrm{AQA}$ |

and every table of the article follows this order, family by family and, inside a family, general then symmetric then antisymmetric.

**Scope and owners.** The general value $\lambda$ and the six root sets at a general value are *Square Roots of a General Element in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, the companion of this article, which states the root equation, the six squares and the six-row table once; the article cites them and applies them at the three named values. The root sets of each structure stay owned by their articles, cited one by one in §*The Six Structures and the Three Values*. The products are *The 6 Products of the Quaternion Real Space* and *The Two General Products of the Quaternion $\mathbb{R}$ Space*; the vocabulary, the root, the unit, the inverse, the zero divisor and the square root of a central value stated once for a general product, is *Definitions for the Study of the 6 Algebraic Structures*; the idempotents are *Idempotents in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*; the square-zero sets are *Nilpotents in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*; the zero-divisor sets are *Zero Divisors in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*; and the two forms are *The 2 Forms over the Quaternion $\mathbb{R}$ Space*.

**Conventions.** $\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$, a general element is $\tilde\xi=\xi_0e_0+\boldsymbol\xi$ with $\xi_0\in\mathbb{R}$ and $\boldsymbol\xi=\sum_k\xi_ke_k$, the natural conjugation is $\tilde\xi^{\natural}=\xi_0-\boldsymbol\xi$, the **plain form** is $B(\tilde\xi)=\xi_0^{2}-\lvert\boldsymbol\xi\rvert^{2}=\mathrm{Sc}(\tilde\xi^{2})$, and the **quaternion form** is $N(\tilde\xi)=\xi_0^{2}+\lvert\boldsymbol\xi\rvert^{2}=\mathrm{Sc}(\tilde\xi^{\natural}\tilde\xi)$. The vector subspace $\mathrm{Vect}(\mathbb{H})$ is written $\boldsymbol\xi$ for its element. The **square root of a central value** is defined in *Definitions for the Study of the 6 Algebraic Structures* as an element $\tilde\xi$ with $\tilde\xi^{2}=c$ for a central $c$, the class of them being the set of its solutions; the origin is therefore counted with the roots of $0$ wherever it solves the equation, and the places where an owner counts the non-zero roots alone are read as the origin alone.

## The Three Named Values

**Definition.** The **root set of the value** $\lambda e_0$ in the structure $\star$ is

$$
\mathcal R_\lambda=\{\tilde\xi:\tilde\xi\star\tilde\xi=\lambda e_0\} ,
$$

and the three **named values** are $\lambda=-1$, $\lambda=0$ and $\lambda=+1$.

**Definition.** A subset of $\mathbb{H}$ is a **cone** when it contains $\mu\tilde\xi$ for every $\tilde\xi$ it contains and every real $\mu$. Its **apex** is the origin.

**The root set of $0$ is a cone, and the root sets of the two signed values are not.** The six products are bilinear over $\mathbb{R}$, so the square of a scaled element is $\mu^{2}(\tilde\xi\star\tilde\xi)$: a root of $0$ scaled is again a root of $0$, while $\mu\tilde\xi$ is a root of $\mu^{2}\lambda$ and not of $\lambda$ unless $\mu^{2}=1$. The root set of $0$ is therefore the cone of the structure, cut by the vanishing of the square, and the root sets of $-1$ and of $+1$ are the level sets of the square at the two values, carrying no apex.

### The Roots of $\pm1$ Are Units and the Non-Zero Roots of $0$ Are Zero Divisors

The quaternion form decides the nature of every root, because the norm of a square is the square of the norm.

**Theorem (a root of a signed value is a unit; a non-zero root of $0$ is a square-zero element).** Let $\tilde\xi$ be a root of $-1$ or of $+1$ in one of the six structures. Then $N(\tilde\xi)=1$, the element is a unit of the algebra, and its inverse is $\tilde\xi^{-1}=\tilde\xi^{\natural}/N(\tilde\xi)$. A non-zero root of $0$ is a square-zero element, at once a zero divisor of its structure and its own annihilating partner.

*Proof.* The square of the root is $\lambda e_0$ with $\lambda=\pm1$, and the norm is multiplicative, $N(\tilde\xi^{2})=N(\tilde\xi)^{2}$, so $N(\tilde\xi)^{2}=N(\lambda e_0)=1$ and $N(\tilde\xi)=1$. The criterion of invertibility of the algebra is $N\neq0$ and the two-sided inverse is $\tilde\xi^{\natural}/N(\tilde\xi)$ (*Zero Divisors in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*). A root of $0$ has vanishing square, hence is a square-zero element, and a non-zero square-zero element annihilates itself on both sides and is a zero divisor of its structure (*Nilpotents in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, *Annihilators in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*).

The algebra is a division algebra, so it decomposes as

$$
\mathbb{H}=\{0\}\cup\mathbb{H}^{\times} , \qquad \mathcal R_{-1}\cup\mathcal R_{+1}\subseteq\mathbb{H}^{\times} ,
$$

with no zero-divisor term: the plain product has no zero divisor at all, and the root set of $0$ of the four structures whose square vanishes only at the origin is the origin alone. The non-zero roots of $0$ occur in the two antisymmetric structures, whose square vanishes identically and whose zero-divisor set is the whole punctured space. So the two signed values are the values at which the roots are units and the value $0$ is the value at which the roots, when they are not the origin, are the square-zero elements; and the two questions — where is the square zero, and where is it minus the unit — are answered at the two ends of the same norm.

## The Six Structures and the Three Values

The square of a structure is its operation read at the two equal arguments, so each of the six carries a root problem of its own, and the problem is decided by the sweep of that square. The six squares are the table of *Square Roots of a General Element in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* §*The Two Squares and the Two Forms*; at the three named values they read as follows.

**Theorem (the classes of the six structures at the three values; quoted).** Among the six structures of the quaternion real space the value $-1$ has roots in the two plain structures alone and the value $+1$ in the four other structures; the value $0$ has the origin alone as its root set in the four structures whose square vanishes only at the origin, and the whole space in the two antisymmetric structures.

**Corollary (the values that fail).** Only the two antisymmetric structures fail a named value, and they fail both, their square vanishing identically.

*Proof.* The plain family reads the indefinite plain form $B$ on the vector subspace, the quaternionic family the definite form $N$, and the two antisymmetric structures the vanishing square; the witnesses are those of §*The Six Structures and the Three Values* below.

The six are read one by one below; each names the product, the square and the three root sets, and cites the article that owns them.

### $\mathrm{GPA}$, the general plain algebra

The product is $\tilde\xi\tilde\eta$, and its square is the plain square $\tilde\xi^{2}=(\xi_0^{2}-\lvert\boldsymbol\xi\rvert^{2})e_0+2\xi_0\boldsymbol\xi$; the vector part $2\xi_0\boldsymbol\xi$ vanishes when $\xi_0=0$ or $\boldsymbol\xi=0$, and the scalar part then gives the value.

**The roots of $-1$** are the sphere $S^{2}$ of the pure unit quaternions, of real dimension two: the central branch has no real solution, and the pure branch gives $\lvert\boldsymbol\xi\rvert^{2}=1$. The sphere is the sphere of the complex structures on the space, a single conjugacy class of the unit group under the adjoint action, the homogeneous space $\mathbb{H}^{1}/U(1)$.

**The roots of $0$** are the origin alone: the pure branch gives $\lvert\boldsymbol\xi\rvert^{2}=0$ and the central branch $\xi_0^{2}=0$, so the two together force $\tilde\xi=0$, and the isotropic cone of the plain form is real only after complexification.

**The roots of $+1$** are the two central units $\pm e_0$: the central branch gives $\xi_0^{2}=1$, the pure branch is excluded by $-\lvert\boldsymbol\xi\rvert^{2}=1$, and the factorisation $\tilde\xi^{2}-e_0=(\tilde\xi-e_0)(\tilde\xi+e_0)$ with no zero divisor forces the root to be central. The pair is the centre of the unit sphere.

The article is *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*.

### $\mathrm{SPA}$, the symmetric plain algebra

The product is the Jordan product $\tilde\xi\bullet\tilde\eta=\tfrac12(\tilde\xi\tilde\eta+\tilde\eta\tilde\xi)$, and its square is the plain square, $\tilde\xi\bullet\tilde\xi=\tilde\xi^{2}$, so the three root sets are exactly the three of $\mathrm{GPA}$.

**The idempotent reading of the block is its own.** The idempotents of the block correspond to the roots of $+1$ under $\tilde\pi\mapsto2\tilde\pi-e_0$, so they are only $0$ and $e_0$; the sphere $S^{2}$ carries no idempotent here, the plain product over $\mathbb{R}$ being a division algebra.

The article is *Square Roots of Minus One, Zero and Plus One in the Symmetric Plain Algebra*.

### $\mathrm{APA}$, the antisymmetric plain algebra

The product is the commutator $\tilde\xi\wedge\tilde\eta=\tfrac12(\tilde\xi\tilde\eta-\tilde\eta\tilde\xi)=\boldsymbol\xi\times\boldsymbol\eta$, the cross product of the two vector parts. It is alternating, so at the two equal arguments it vanishes, $\tilde\xi\wedge\tilde\xi=0$, and the three equations reduce to $0=-e_0$, $0=0$ and $0=+e_0$.

**There is no root of $-1$ and no root of $+1$**, the value $0$ alone being read by the vanishing square. **The roots of $0$** are every element of the space; the non-zero ones are at once the square-zero set, the nilpotent set and the zero-divisor set of the block, all three being the punctured space.

The article is *Square Roots of Minus One, Zero and Plus One in the Antisymmetric Plain Algebra*.

### $\mathrm{GQA}$, the general quaternionic algebra

The product is $\tilde\xi^{\natural}\tilde\eta$, and its square is the central element $N(\tilde\xi)e_0$, so the root problem is the single real equation $N(\tilde\xi)=\lambda$.

**There is no root of $-1$**, the quaternion form being a sum of four squares and the equation $N=-1$ being empty. **The roots of $0$** are the origin alone, $N$ vanishing only there. **The roots of $+1$** are the level set $N=1$, the unit sphere $S^{3}$ of real dimension three.

This is the exchange of the signs against the plain family: the plain product has its sphere at the negative value and its two points at the positive one, the quaternionic product has nothing at the negative value and its sphere at the positive one, and the exchange is the sign between the two forms on the vector subspace.

The article is *Square Roots of Minus One, Zero and Plus One in the General Quaternionic Algebra*.

### $\mathrm{SQA}$, the symmetric quaternionic algebra

The product is the symmetrisation $\tfrac12(\tilde\xi^{\natural}\tilde\eta+\tilde\eta^{\natural}\tilde\xi)=N(\tilde\xi,\tilde\eta)e_0$, the quaternion form read as a product, and its square is the definite form, $\tilde\xi\star\tilde\xi=N(\tilde\xi)e_0$, non-negative at every element. The three root sets are the three of $\mathrm{GQA}$: no root of $-1$, the origin alone as the root of $0$, and the level set $N=1$ as the roots of $+1$, the group $Sp(1)$ of the unit quaternions, of real dimension three.

The article is *Square Roots of Minus One, Zero and Plus One in the Symmetric Quaternionic Algebra*.

### $\mathrm{AQA}$, the antisymmetric quaternionic algebra

The product is the commutator $\tilde\xi\wedge^{\natural}\tilde\eta=\tfrac12(\tilde\xi^{\natural}\tilde\eta-\tilde\eta^{\natural}\tilde\xi)$. It is alternating, $\tilde\xi\wedge^{\natural}\tilde\xi=0$, so there is no root of $-1$ and none of $+1$.

**The roots of $0$** are every element of the space; the non-zero ones are at once the square-zero elements, the nilpotents of the block and its zero divisors, the three sets being the punctured space.

The article is *Square Roots of Minus One, Zero and Plus One in the Antisymmetric Quaternionic Algebra*.

## Results

The three named values are the three level sets of the square, tabulated below over the six structures, proved for the two general products, read in coordinates and in the two families of the plain reduction.

### The Six Root Sets at the Three Values

Read against the empty set and against the whole space, the six root sets are

| the family | the structure | the square | the roots of $-1$ | the roots of $0$ | the roots of $+1$ |
|---|---|---|---|---|---|
| the plain algebra | $\mathrm{GPA}$ | $\tilde\xi^{2}$ | the sphere $S^{2}$ of the pure unit quaternions, real dimension $2$ | the origin alone | the pair $\pm e_0$ |
| | $\mathrm{SPA}$ | $\tilde\xi^{2}$ | the sphere $S^{2}$ | the origin alone | the pair $\pm e_0$ |
| | $\mathrm{APA}$ | $0$ | none | the whole space | none |
| the quaternionic algebra | $\mathrm{GQA}$ | $N(\tilde\xi)e_0$ | none | the origin alone | the sphere $S^{3}$ of the unit quaternions, real dimension $3$ |
| | $\mathrm{SQA}$ | $N(\tilde\xi)e_0$ | none | the origin alone | the sphere $S^{3}$ |
| | $\mathrm{AQA}$ | $0$ | none | the whole space | none |

Four structures reduce the root set of $0$ to the origin alone, and the failure of the other two to do so is the vanishing of their square: the two alternating structures have no square to read, so every element is a root of $0$ and no element is a root of a signed value. The two spheres name different values, $S^{2}$ the value $-1$ of the plain family and $S^{3}$ the value $+1$ of the quaternionic family, and the pair $\pm e_0$ is the centre of the quaternionic sphere.

### The Two General Products at the Three Values

**Theorem (the two general products at the three values).** At the value $-1$ the plain product has the sphere $S^{2}$ and the natural product has no root at all. At the value $0$ the two have the origin alone. At the value $+1$ the plain product has the two central units $\pm e_0$ and the natural product the sphere $S^{3}$. The two root sets differ at the two signed values and agree at the value $0$.

*Proof.* The two squares are $B$ read with the vector equation and $N$, and the two forms differ by the sign of the vector part; at the value $0$ the plain pair forces the origin and the equation $N=0$ has the origin for its only solution; at the values $\pm1$ the plain product reads the pure branch, which the plain form reaches at the negative value alone, while the natural product reads the definite level set, which is non-empty at the positive value alone.

**The word is *differ*, not *coincide*.** The zero-divisor sets of *Zero Divisors in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* are one set read twice — the empty set, because the algebra is a division algebra — while the root sets are two different sets at each of the two signed values. The reason is the one on which the whole chapter turns: the two general products read the same norm, and the zero-divisor criterion is the norm, but their squares are $B$ and $N$ on the vector subspace and the two differ by a sign, so the values at which the squares vanish or reach the unit are not the same values.

### The Three Values in Coordinates and the Roots of Zero

Written on the coordinates, the three values are the three equations of the squares, one per family:

| the family | the equation of the root of $\lambda$ |
|---|---|
| the plain family | $\xi_0^{2}-\lvert\boldsymbol\xi\rvert^{2}=\lambda$ with $2\xi_0\boldsymbol\xi=0$ |
| the quaternionic family | $N(\tilde\xi)=\xi_0^{2}+\lvert\boldsymbol\xi\rvert^{2}=\lambda$ |
| the two antisymmetric structures | $0=\lambda e_0$ |

**Proposition (the root set of $0$ is the cone, and the root sets of the two signed values carry no apex).** The set $\mathcal R_0$ is a cone whose apex is the origin: a real multiple of a root of $0$ is again a root of $0$. It is the origin alone for the four structures whose square vanishes only there, and the whole space, a cone with the origin as apex, for the two antisymmetric structures. The sets $\mathcal R_{-1}$ and $\mathcal R_{+1}$ carry no apex: a scaling by $\mu$ carries the value $\lambda$ to $\mu^{2}\lambda$, so no non-zero multiple of a root of $\lambda$ is again a root of $\lambda$ unless $\mu^{2}=1$.

*Proof.* The square of a scaled element is $\mu^{2}(\tilde\xi\star\tilde\xi)$, the six products being bilinear; the vanishing of the square is therefore preserved by every $\mu$ and the value is preserved by $\mu=\pm1$ alone. The root set of $0$ of the plain family is the origin and not the isotropic cone of $B$, because the two equations of the pair must hold together: the cone $B=0$ meets the vector subspace at the origin alone, and the other branch is the centre.

The dimension count reads the table of §*The Six Root Sets at the Three Values*: the sphere $S^{2}$ of the plain family is of real dimension two inside the three-dimensional vector subspace, and the sphere $S^{3}$ of the quaternionic family is of real dimension three inside the four-dimensional space.

### The Two Families

The plain reduction cuts the space into two families, and the root sets respect the cut.

**Definition.** An element is **pure** when its scalar part vanishes, $\xi_0=0$, and **central** when its vector part vanishes, $\boldsymbol\xi=0$.

The reduction of the plain square is the vanishing of the vector part, $2\xi_0\boldsymbol\xi=0$, and the two factors give the two families: the pure one, on which the reduction is satisfied identically, and the central one, on which it forces the vector part to vanish.

| | pure, $\xi_0=0$ | central, $\xi_0\neq0$ |
|---|---|---|
| the reduction $2\xi_0\boldsymbol\xi=0$ | satisfied identically | forces $\boldsymbol\xi=0$ |
| the roots of $0$ | the origin alone | the origin alone |
| the roots of $-1$ | the sphere $S^{2}$ of the vector subspace | none |
| the roots of $+1$ | none | the pair $\pm e_0$ |
| the dimension | $3$ | $1$ |

The two signed values are separated by the cut: the sphere of the roots of $-1$ lies in the pure family, where the reduction is free and the plain form is negative definite, and the pair $\pm e_0$ lies in the centre, where the reduction has already forced the vector part to vanish. The value $0$ is read by neither family alone: in the pure family the branch gives $\lvert\boldsymbol\xi\rvert^{2}=0$ and in the central family $\xi_0^{2}=0$, so the origin is the only element of the two, and the isotropic cone of the plain form is real only after complexification.

## The Inverse Equations

At the three values the inverse equations are read on the roots. Of the two general products the plain one has the two-sided unit $e_0$, so the classical equivalence *a root of a signed value if and only if a unit* is available for it; the natural product has no two-sided unit, and the substitute is the one-sided criterion, whose table of solutions is *Zero Divisors in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* §*The One-Sided Inverse Equations*, quoted and not restated.

**Theorem (the inverse equations at the three values).** Let $\star$ be one of the two general products and let $\tilde\xi$ be a root of $-1$ or of $+1$. Then each of the two equations

$$
\tilde\xi\star\tilde\eta=e_0 , \qquad \tilde\eta\star\tilde\xi=e_0
$$

has a solution: the two-sided inverse $\tilde\xi^{-1}=\tilde\xi^{\natural}/N(\tilde\xi)$ for the plain product and the one-sided solution $(\tilde\xi^{-1})^{\natural}$ for the natural product. A non-zero root of $0$ has no solution on either side, and it is its own annihilator.

*Proof.* A root of a signed value has $N=1$ by §*The Roots of $\pm1$ Are Units and the Non-Zero Roots of $0$ Are Zero Divisors*, and the criterion of invertibility is $N\neq0$; the two solutions are those of the table of *Zero Divisors in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*. A non-zero root of $0$ has vanishing square and $N=0$, and an element of vanishing norm annihilates itself on both sides.

The two signed values are therefore the values at which the roots are units, and the value $0$ the value at which the roots are the square-zero elements; and of the two the plain family inverts on both sides, the quaternionic family on one side alone.

## Summary

The root of the central value $\lambda e_0$ in a structure is the solution of the equation $\tilde\xi\star\tilde\xi=\lambda e_0$, and the three values that carry a name are $-1$, $0$ and $+1$. The root set of $0$ is a cone with the origin as its apex, the root sets of $-1$ and of $+1$ are the level sets of the square and carry no apex, and the quaternion form places every root: a root of a signed value has $N=1$ and is a unit of the algebra, and a non-zero root of $0$ is a square-zero element and a zero divisor of its structure.

The plain family, the general plain and the symmetric plain structures, has the sphere $S^{2}$ of the pure unit quaternions as its roots of $-1$, of real dimension two, the origin alone as its roots of $0$, and the two central units $\pm e_0$ as its roots of $+1$: the sphere is the family of the complex structures on the space and carries no idempotent, the idempotents of the division algebra being $0$ and $e_0$, read from the roots of $+1$. The quaternionic family, the general quaternionic and the symmetric quaternionic structures, has no root of $-1$, the origin alone as its roots of $0$ and the unit sphere $S^{3}$ as its roots of $+1$, of real dimension three. The two antisymmetric structures have no root of either signed value and read the value $0$ alone, the whole space.

The two general products therefore give two different answers at the two signed values and the same answer at the value $0$: the plain product reads the indefinite plain form and the natural product the definite quaternion form, and the sign between the two forms is the whole difference. The inverse equations follow the same split: the root of a signed value is invertible, on both sides for the plain product and on one side for the natural one, and the non-zero root of $0$ is the element that annihilates itself.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\lambda e_0$, $\lambda\in\mathbb{R}$ | a central value of the real space |
| $-1$, $0$, $+1$ | the three named central values |
| $\mathcal R_\lambda$ | the root set of the value $\lambda$, the solutions of $\tilde\xi\star\tilde\xi=\lambda e_0$ |
| $B(\tilde\xi)=\xi_0^{2}-\lvert\boldsymbol\xi\rvert^{2}$ | the plain form, the scalar part of the plain square |
| $N(\tilde\xi)=\xi_0^{2}+\lvert\boldsymbol\xi\rvert^{2}$ | the quaternion form, the square of the quaternionic family, and the norm |
| $S^{2}$, $S^{3}$ | the unit sphere of the vector subspace, real dimension two, and the unit sphere of the space, real dimension three |
| $\varnothing$, $\mathbb{H}$ | the root sets of a signed value and of $0$ in the two antisymmetric structures |
| $\mathrm{GPA},\dots,\mathrm{AQA}$ | the six structures of the space, the two general products and their four parts |

## Further Reading

- *Square Roots of a General Element in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/square-roots-of-a-general-element-in-the-6-algebraic-structures-over-the-quaternion-r-space.md`), the companion of this article, for the root equation at a general central value, the six squares and the six-row table.
- *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-6-algebraic-structures-over-the-quaternion-r-space.md`), for the six names, the class of each and the two laws of the table.
- *The 6 Products of the Quaternion Real Space* (`articles_maths/the-6-products-of-the-quaternion-real-space.md`), for the six products and their coordinates.
- *The Two General Products of the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-two-general-products-of-the-quaternion-r-space.md`), for the plain product and the natural product, whose signs the three values read.
- *The 2 Forms over the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-2-forms-over-the-quaternion-r-space.md`), for the plain form $B$ of signature $(1,3)$ and the definite quaternion form $N$.
- *Zero Divisors in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/zero-divisors-in-the-6-algebraic-structures-over-the-quaternion-r-space.md`), for the empty zero-divisor set of the two general products, the inverse criterion $N\neq0$, and the table of the one-sided inverse equations.
- *Nilpotents in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/nilpotents-in-the-6-algebraic-structures-over-the-quaternion-r-space.md`), for the square-zero sets, which are the roots of $0$.
- *Idempotents in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/idempotents-in-the-6-algebraic-structures-over-the-quaternion-r-space.md`), for the two idempotents $0$ and $e_0$ and the reading of the roots of $+1$.
- *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-general-plain-algebra-of-quaternions.md`), for the sphere of the roots of $-1$ and the two roots of $+1$.
- *Square Roots of Minus One, Zero and Plus One in the General Quaternionic Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-general-quaternionic-algebra-of-quaternions.md`), for the empty root set of $-1$ and the sphere of the roots of $+1$.
