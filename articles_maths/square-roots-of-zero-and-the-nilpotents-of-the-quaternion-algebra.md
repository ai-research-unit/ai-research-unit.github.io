# __Square Roots of Zero and the Nilpotents of the Quaternion Algebra__

## Introduction

The algebra of this article is the quaternion algebra $\mathbb{H}$, the real space $\mathbb{H}$ under the general plain bilinear product $\tilde p\tilde q$ of *Introduction to the Quaternion Algebra*, the multiplication of the algebra and the operation named the algebra in *The Algebraic Structures over the Quaternion $\mathbb{R}$ Space*. That product is the one read throughout this article.

The article treats two subjects, and in this order. The first is the square roots of the central value $0$, the elements $\tilde\xi\in\mathbb{H}$ with

$$
\tilde\xi^2=0 .
$$

The second is the nilpotents of the algebra, the nonzero elements whose square vanishes. The two subjects are one subject: the roots of $0$ are the origin together with the square-zero elements, and the nonzero square-zero elements are exactly the nilpotents. **Over $\mathbb{R}$ both classes collapse** — the roots of $0$ are the origin alone and there is no nilpotent at all — and the collapse is the division property of the algebra, every nonzero element being a unit. The roots of $+e_0$ and the idempotents are the companion article *Square Roots of One and the Idempotents of the Quaternion Algebra*, above this article in this category; the roots of the general quadratic $\tilde\xi^2=\tilde q$ are *Square Roots of a General Element in the Quaternion Algebra*, below this article in this category.

**The results.** The roots of $0$ are the origin alone; there is no nonzero square-zero element. The square-zero set is the singleton $\{0\}$, the nilpotent class is empty, and no element is of nilpotency index two or more, a vanishing power vanishing at the first step. The square of a general element closes in two terms, $\tilde q^2=[q_0^2-|\vec q|^2]e_0+2q_0\vec q$, whose central and vector coefficients cannot vanish together off the origin, and the cube closes as $\tilde q^3=q_0[q_0^2-3|\vec q|^2]e_0+[3q_0^2-|\vec q|^2]\vec q$, vanishing only at the origin as well. No element is both an idempotent and a nonzero nilpotent, and the square-zero class meets the centre and the vector subspace only at the origin.

The article is algebraic. The zero-divisor set, its families and the criterion on the norm are *Zero Divisors of the Quaternion Algebra*; the roots of $+e_0$ and the idempotents are *Square Roots of One and the Idempotents of the Quaternion Algebra*; the general root problem is *Square Roots of a General Element in the Quaternion Algebra*; and the folding of the empty classes, with the isolation of the plain product among the six, is *The Specificities of the Quaternion Algebra*.

**Conventions.** The algebra is $\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$ and $e_1e_2=e_3$, so that $e_k^2=-e_0$ and $e_je_k=-e_ke_j$ for $j\neq k$. An element is $\tilde q=q_0e_0+\vec q$ with $\vec q=\sum_{k=1}^{3}q_ke_k$ and $q_\mu\in\mathbb{R}$; the scalar part is $q_0=\mathrm{Sc}(\tilde q)$ and the vector part is $\vec q$. The natural conjugation is $\tilde q^{\natural}=q_0e_0-\vec q$, and the **norm** is $N(\tilde q)=\tilde q\tilde q^{\natural}=q_0^2+|\vec q|^2$, positive definite over $\mathbb{R}$ by *Norm and Invertibility in the Quaternion Algebra*; every nonzero element is a unit, $\tilde q^{-1}=\tilde q^{\natural}/N(\tilde q)$, so there is no zero divisor. The scalar line $\mathbb{R}e_0$ is the centre and the vector subspace is $\mathrm{Vect}(\mathbb{H})$, of dimension three. A root of a central value is written $\tilde\xi$ (§*The Root Convention* of *Conventions in Mathematics*), a nilpotent $\tilde\nu$ (§*The Nilpotent Convention*), and a generic element $\tilde q$.

The equations name a product, so the roots and the nilpotents are relative to it. The general definition of the power, the square, the root of a central value and the nilpotent, with the index of nilpotency and the square-zero element, is *Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, §*The Element Vocabulary*. Throughout this article the square is the one of the general plain bilinear product, the multiplication of the algebra; the other five structures over the same space carry roots of $0$ and square-zero sets of their own.

## The Roots of Zero

**The roots of $0$ are exactly the origin, $\Sigma_0=\{0\}$; there is no nonzero square-zero element.**

A **root of $0$** is an element $\tilde\xi\in\mathbb{H}$ with $\tilde\xi^2=0$, the square being the one of the general plain bilinear product.

### The Reduction

Write the root in scalar and vector parts,

$$
\tilde\xi=\xi_0e_0+\vec\xi,\qquad \vec\xi=\xi_1e_1+\xi_2e_2+\xi_3e_3,\qquad \xi_k\in\mathbb{R}.
$$

**Proposition (the reduction at the value $0$).** For $\tilde\xi=\xi_0e_0+\vec\xi$,

$$
\tilde\xi^2=0\qquad\Longleftrightarrow\qquad
\begin{cases}
2\xi_0\vec\xi=0,\\[2pt]
\xi_0^2-|\vec\xi|^2=0 .
\end{cases}
$$

*Proof.* Specialisation of the central reduction of *Square Roots of One and the Idempotents of the Quaternion Algebra* to $\lambda=0$: the plain square is $\tilde\xi^2=(\xi_0^2-|\vec\xi|^2)e_0+2\xi_0\vec\xi$, and the element vanishes exactly when both its parts do.

Since $\mathbb{R}$ is a field, the vector equation holds exactly when $\xi_0=0$ or $\vec\xi=0$. **Only the scalar equation survives on each branch**: the root is pure, $\xi_0=0$, or it is a real scalar, $\vec\xi=0$.

### The Scalar Case

In the scalar case $\tilde\xi=\xi_0e_0$ and the scalar equation reads $\xi_0^2=0$; since $\mathbb{R}$ is a field, $\xi_0=0$. The root in this case is the single element

$$
\tilde\xi=0,
$$

the origin.

### The Pure Case Is Empty

In the pure case $\tilde\xi=\vec\xi$ and the scalar equation reads

$$
-|\vec\xi|^2=0,
$$

that is $\vec\xi=0$: the pure branch returns the origin and no other element. **There is no nonzero pure root of $0$**, the sum of squares being definite, so a pure element has the non-positive square $-|\vec u|^2e_0$, which vanishes only at the origin.

### Statement of the Theorem

**Theorem.** The roots of $0$ of the algebra are exactly the origin,

$$
\Sigma_0=\{0\}.
$$

*Proof.* By the reduction the root is pure or scalar. The scalar case gives $\xi_0=0$; the pure case gives $\vec\xi=0$; both return the origin, and the origin is a root. The two cases exhaust the equation and the class has one element.

### Verification

The origin is a root, $0\cdot 0=0$, and nothing else is: the pure branch needs $|\vec\xi|^2=0$ and the scalar branch $\xi_0^2=0$, both of which have the origin as their only real solution. The smallest non-central witnesses confirm the emptiness: the pure element $e_1$ has square $e_1^2=-e_0\neq0$, and the element $e_0+e_1$ has square $e_0+2e_1+e_1^2=2e_1\neq0$.

### The Roots of Zero and the Nilpotents

The nonzero roots of $0$ are exactly the **nilpotents** of the algebra. The roots of $0$ here are the origin alone, so the nilpotents are none. A nonzero root of $0$ would be a square-zero element, hence a zero divisor annihilating itself; the algebra has no zero divisor, so no such element exists. The behaviour is the opposite of the roots of $+e_0$, which are units of the algebra (*Square Roots of One and the Idempotents of the Quaternion Algebra*), and it is the degenerate case of the general root problem at the central value $0$ (*Square Roots of a General Element in the Quaternion Algebra*).

## The Nilpotents

**The nilpotents of the algebra are none: there is no nonzero square-zero element, the nilpotent cone is the empty set, and no element is of nilpotency index two or more.**

The **nilpotents** of the algebra are the nonzero elements whose square vanishes. The class is empty, and the reason is one line long: the square of a general element closes in two terms, one central and one along the vector part,

$$
\tilde q^2=\bigl[q_0^2-|\vec q|^2\bigr]e_0+2q_0\vec q ,
$$

and the two coefficients cannot vanish together off the origin — the vector term forces the scalar part to vanish, and the central term then forces the vector part to vanish. The complexified block, where the central coefficient is a difference of *complex* squares, does the opposite, and its nilpotents fill the pure isotropic cone of real dimension four, the *pure* family of its zero divisors, the other family being the multiples of the nontrivial idempotents. Over $\mathbb{R}$ both families are empty.

### The Definition

**Definition (nilpotent of a product).** Let $\star$ be a product on $\mathbb{H}$; a **square-zero element** of $\star$ is an element $\tilde q$ with $\tilde q^{\star2}=0$, and a **nilpotent of $\star$** is a **nonzero** element $\tilde\nu$ with $\tilde\nu^{\star k}=0$ for some $k\geq1$. The least such $k$ is the **index of nilpotency**, and an element is of **index two** when its square vanishes while it does not. The element $0$ is a square-zero element and is not a nilpotent.

The equation names a product, and the notion is relative to it; throughout this article the product is the general plain bilinear product, the multiplication of the algebra, and the square is the plain square. The general definition, with the index of nilpotency and the square-zero element, is *Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, §*The Element Vocabulary*; the square-zero set and the nilpotent class are kept apart below, and the relation between them is stated in both readings.

The natural conjugation preserves square-zero elements, being multiplicative and carrying a vanishing square to a vanishing square,

$$
(\tilde\nu^{\natural})^2=(\tilde\nu^2)^{\natural}=0 ,
$$

Were the class not empty, it would be a conjugation-stable class; as it is, the statement is vacuous and is recorded for the form of the definition.

### The Criterion

**An element is square-zero exactly when it is the origin: the criterion is $q_0=0$ and $\vec q=0$, that is $\tilde q=0$, and over $\mathbb{R}$ the pure elements with isotropic vector part reduce to the origin alone.**

**Theorem (the criterion for a square-zero element).** For $\tilde q\in\mathbb{H}$ the following are equivalent: $\tilde q^2=0$; the scalar part and the vector part both vanish, $q_0=0$ and $\vec q=0$; and $\tilde q=0$.

*Proof.* The displayed formula expands the square. The two coefficients of the sum, central and vector, must vanish separately. If $q_0\neq0$ then the vector coefficient $2q_0\vec q$ vanishes only for $\vec q=0$, and then the central coefficient is $q_0^2\neq0$, a contradiction; so $q_0=0$. With $q_0=0$ the formula reads $\tilde q^2=-|\vec q|^2e_0$, which vanishes exactly when $|\vec q|^2=q_1^2+q_2^2+q_3^2=0$, a sum of three squares of real numbers, hence exactly when $\vec q=0$. So $\tilde q=0$ is the only square-zero element.

**Corollary.** The square-zero set of the algebra is the singleton $\{0\}$, and the nilpotent class — the nonzero square-zero elements — is the empty set. The algebra therefore carries no nilpotent whatever, of index two or of any higher index.

Over the complexified block the same computation passes through the complex bilinear form $(\vec Q,\vec Q)=Q_1^2+Q_2^2+Q_3^2$: the criterion there is $Q_0=0$ and $(\vec Q,\vec Q)=0$, a complex vector part on the isotropic cone, and the nilpotents are the nonzero elements of that cone, of real dimension four. The difference is exactly the passage from the sum of three real squares, which is positive definite, to the sum of three complex squares, which is isotropic on a cone.

### Index Two

**Theorem (no higher index).** For the algebra, $\tilde q^k=0$ for some $k\geq1$ if and only if $\tilde q=0$; equivalently, a vanishing power vanishes at the first step.

*Proof.* If $\tilde q\neq0$ it is a unit, with inverse $\tilde q^{-1}$. Multiplying $\tilde q^k=0$ on the left by $\tilde q^{-1}$ gives $\tilde q^{k-1}=0$, and iterating gives $\tilde q=0$, a contradiction. So no nonzero element has a vanishing power, of index two or of any higher index.

The direct computation of the cube agrees, and it is worth recording because it mirrors the complexified expansion:

$$
\tilde q^2=\bigl[q_0^2-|\vec q|^2\bigr]e_0+2q_0\vec q,\qquad \tilde q^3=q_0\bigl[q_0^2-3|\vec q|^2\bigr]e_0+\bigl[3q_0^2-|\vec q|^2\bigr]\vec q .
$$

If $\vec q=0$ then $\tilde q^3=q_0^3e_0$ vanishes only for $q_0=0$; if $\vec q\neq0$ the vanishing of the vector coefficient forces $|\vec q|^2=3q_0^2$, and the central coefficient is then $q_0[q_0^2-9q_0^2]=-8q_0^3$, which vanishes only for $q_0=0$, whereupon $|\vec q|^2=0$, a contradiction. So $\tilde q^3=0$ if and only if $\tilde q=0$, and the same conclusion holds for every higher power.

### The Nilpotent Cone Is Empty

The set of square-zero elements is $\{0\}$, so the **nilpotent cone is the empty set**: there is no parametrisation of it, no real dimension to give, and no family of isotropic pure elements, the sum of squares of the vector subspace being definite. The emptiness is also the **criterion for an empty class**: a nonzero square-zero element would be a zero divisor, and the general plain structure has none (*Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, §*The Criterion for an Empty Class*). Over the complexified block the pure square $\vec Q^2=-(\vec Q,\vec Q)e_0$ is indefinite, the isotropic pure elements form a cone of complex dimension two, and the nilpotents fill it; the real block has none of them.

### The Nilpotents and the Zero Divisors

**Proposition (a square-zero element is a zero divisor with itself).** If $\tilde\nu$ is a nonzero square-zero element then

$$
\tilde\nu\tilde\nu=0
$$

on both sides, so $\tilde\nu$ is a two-sided zero divisor, with itself as annihilating partner.

*Proof.* The relation $\tilde\nu^2=0$ is the product of $\tilde\nu$ with itself, on either side.

Over $\mathbb{R}$ the proposition has no instance, because there is no nonzero square-zero element, and it is stated to locate the class against the empty zero-divisor set: a nonzero nilpotent would be a zero divisor, the zero-divisor set is empty (*Zero Divisors of the Quaternion Algebra*), and the nilpotent class is therefore empty. The two emptinesses are the same emptiness seen from two sides. In the complexified block the relation runs the other way, and the nonzero nilpotents are exactly the pure family of the zero-divisor cone.

### The Nilpotents and the Idempotents

**Theorem (the two classes are disjoint).** No element of $\mathbb{H}$ is both an idempotent and a nonzero nilpotent.

*Proof.* An idempotent is $0$ or $e_0$ (*Square Roots of One and the Idempotents of the Quaternion Algebra*). The element $e_0$ is not square-zero, $e_0^2=e_0\neq0$, and no nonzero element is square-zero by the criterion; so no idempotent is a nilpotent.

Over $\mathbb{R}$ the disjointness is total: the idempotents are $0$ and $e_0$, the nilpotent class is empty, and the square-zero set is the single point $0$, whose only member is the idempotent $0$ and not a nilpotent. The complexified block draws the same disjointness between two populated classes, the nilpotent cone and the idempotent family, which meet only at the origin; the difference is that both of its classes have points.

### The Square-Zero Set and the Remarkable Subspaces

A square-zero element of the complexified block is pure, and its vector part is isotropic. Over $\mathbb{R}$ the square-zero set is the origin, and the statement is that neither remarkable subspace contributes anything beyond it.

| Remarkable subspace | Square-zero elements |
|---|---|
| $\mathbb{R}e_0$, the centre | $0$ alone; a nonzero scalar has $s^2>0$ |
| $\mathrm{Vect}(\mathbb{H})$, the vector subspace | $0$ alone; a nonzero pure element has $\vec q^2=-\lvert\vec q\rvert^2e_0\neq0$ |

The entries are forced by the two restrictions of the norm: on the centre $N(se_0)=s^2$, positive for $s\neq0$, and on the vector subspace $N(\vec q)=|\vec q|^2$, positive for $\vec q\neq0$. A zero of the plain square is thus nowhere but the origin, and both remarkable subspaces carry the same square-zero set as the whole space; the two restrictions of the norm are *The 2 Algebraic Norms over the Quaternion $\mathbb{R}$ Space*.

### The Nilpotents and the Central Values

The equation $\tilde q^2=0$ is the third of the three central power equations $\tilde q^2=c\,e_0$ for $c=-1,0,+1$ of *Square Roots of a General Element in the Quaternion Algebra*, and it is the one whose root set contains no nonzero element. The value $+1$ is the companion, its two central roots being the subject of *Square Roots of One and the Idempotents of the Quaternion Algebra*.

**Proposition.** The solutions of $\tilde q^2=0$ are exactly the origin, and the origin is not a nilpotent.

*Proof.* The criterion of §*The Criterion*, equivalently the theorem of §*The Roots of Zero*.

**Corollary.** The root set of $0$ is $\{0\}$ and the root set of $+1$ is $\{\pm e_0\}$, both central; among the three central values it is $c=0$ whose root set is empty of nonzero elements, and the nilpotent class, the class of the nonzero roots of $0$, is empty.

## Summary

The square of the algebra is the plain square, and the criterion is $\tilde q^2=0$ if and only if $q_0=0$ and $\vec q=0$, which is $\tilde q=0$; so the **square-zero set is the singleton $\{0\}$ and the nilpotent class is empty**. There is no nonzero square-zero element and no element of index two or more: a vanishing power vanishes at the first step, and the direct computation of the square and the cube confirms it, the central coefficient $q_0^2-|\vec q|^2$ and the vector coefficient $2q_0\vec q$ being unable to vanish together off the origin. The algebra has no element with a vanishing power of any order, its powers being the powers of a division rule, and the index of nilpotency is therefore undefined.

The roots of $0$ are the origin alone, and they are the degeneracy of the general square-root problem at the central value $0$: the scalar branch gives $\xi_0=0$ and the pure branch gives $\vec\xi=0$, both returning the origin. This is the opposite of the roots of $+e_0$, which are units; a nonzero root of $0$ would be a nilpotent and a zero divisor.

The nilpotent class is empty: there is no nilpotent cone, the set of square-zero elements is $\{0\}$, and the emptiness is the definiteness of the sum of squares, a nonzero pure element having the non-positive square $-|\vec q|^2e_0$ and a nonzero scalar the positive square $s^2e_0$. A nonzero nilpotent would be a zero divisor with itself, and the zero-divisor set of the algebra is empty; the two emptinesses are the same seen from two sides; no element is both an idempotent and a nonzero nilpotent, the two classes meeting only at the origin. The square-zero set meets neither the centre nor the vector subspace except at the origin. This is the opposite of the complexified block, whose nilpotents form the pure isotropic cone of real dimension four, and it is the folding recorded in *The Specificities of the Quaternion Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | Quaternion algebra, real dimension four |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$, $e_1e_2=e_3$ |
| $\tilde q=q_0e_0+\vec q$ | General element, scalar part $q_0$, vector part $\vec q$ |
| $N(\tilde q)=q_0^2+\lvert\vec q\rvert^2$ | Quaternion norm, positive definite |
| $\tilde\nu$ | A nilpotent, a nonzero element of vanishing square |
| $\tilde q^2=0$ | The square-zero equation |
| $\Sigma_0=\{0\}$ | The roots of $0$, the origin alone |
| $\{0\}$ | The square-zero set of the algebra |
| $\varnothing$ | The nilpotent class |
| $\tilde q^2=[q_0^2-\lvert\vec q\rvert^2]e_0+2q_0\vec q$ | The square of a general element |
| $\tilde q^3=q_0[q_0^2-3\lvert\vec q\rvert^2]e_0+[3q_0^2-\lvert\vec q\rvert^2]\vec q$ | The cube of a general element |
| $\mathbb{R}e_0$, $\mathrm{Vect}(\mathbb{H})$ | Centre and vector subspace |

## Further Reading

- *Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-quaternioid-r-space.md`), §*The Element Vocabulary*, for the general definition of a root of a central value and of the nilpotent, with the index of nilpotency and the square-zero element; §*The Criterion for an Empty Class*, for the criterion that empties the nonzero nilpotent class.
- *Introduction to the Quaternion Algebra* (`articles_maths/introduction-to-the-quaternion-algebra.md`), for the product, the unit and the square.
- *Square Roots of One and the Idempotents of the Quaternion Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-quaternion-algebra.md`), for the central reduction specialised here, the roots of $+e_0$, the idempotents and their disjointness from the square-zero class.
- *Square Roots of a General Element in the Quaternion Algebra* (`articles_maths/square-roots-of-a-general-element-in-the-quaternion-algebra.md`), for the roots of the general quadratic $\tilde\xi^2=\tilde q$, of which the roots of $0$ here are the degenerate case.
- *Zero Divisors of the Quaternion Algebra* (`articles_maths/zero-divisors-of-the-quaternion-algebra.md`), for the empty zero-divisor set and the two families of the complexified block.
- *The Specificities of the Quaternion Algebra* (`articles_maths/the-specificities-of-the-quaternion-algebra.md`), for the folding of the empty classes and the isolation of the plain product among the six.
- *The 2 Algebraic Norms over the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-2-algebraic-norms-over-the-quaternioid-r-space.md`), for the two restrictions of the norm to the centre and the vector subspace.
- *Square Roots of Zero and the Nilpotents of the Quaternion Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-biquaternion-algebra.md`), the complexified counterpart, for the pure isotropic cone, its real dimension four and the index-two theorem.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for nilpotents and their place in the structure of a finite-dimensional algebra.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for nilpotents, units and the division property.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the square of a quaternion and the behaviour of its vector part.
