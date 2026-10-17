# __Square Roots of Zero and the Nilpotents of the Symmetric Plain Algebra__

## Introduction

The symmetric plain algebra $\mathbb{H}^{\bullet}$ is the real space $\mathbb{H}$ under the Jordan product

$$
\tilde p\bullet\tilde q=\tfrac12\bigl(\tilde p\tilde q+\tilde q\tilde p\bigr)
$$

of *Introduction to the Symmetric Plain Algebra of Quaternions*, the symmetrisation of the general plain bilinear product of *Introduction to the General Plain Algebra of Quaternions*, and the operation named $\mathrm{SPA}$ in *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*. The square of the block is the **plain square**, $\tilde p\bullet\tilde p=\tilde p^2$: the symmetrisation moves only the antisymmetric part of the product, and that part vanishes on the diagonal (*The Symmetric and Antisymmetric Parts of an Algebra Product*).

The article treats two subjects, and in this order. The first is the square roots of the central value $0$, the elements $\tilde\xi\in\mathbb{H}$ with $\tilde\xi\bullet\tilde\xi=0$. The second is the nilpotents of the block, the nonzero elements whose square vanishes. The two subjects are one subject: the roots of $0$ are the origin together with the square-zero elements, and the nonzero square-zero elements are exactly the nilpotents. **Over $\mathbb{R}$ both classes collapse** — the roots of $0$ are the origin alone and there is no nilpotent at all — and the collapse is the definiteness of the Euclidean form of the vector subspace. The roots of $+e_t$ and the idempotents are the companion article *Square Roots of One and the Idempotents of the Symmetric Plain Algebra*; the roots of the general quadratic $\tilde\xi\bullet\tilde\xi=\tilde q$ are *Square Roots of a General Element in the Symmetric Plain Algebra*.

The roots of $0$ of the block and the roots of $0$ of the general plain product are the same set, the two squares being equal; the plain product is a **division rule** and has no nonzero square-zero element. The block is not a division rule — it has zero divisors, the whole punctured vector subspace — and the question is whether the symmetrisation adds square-zero elements to that set. It does not: the square of a pure element is the definite negative scalar $-|\vec q_a|^2e_t$, and the pure branch of the equation is empty.

**The results.** The roots of $0$ are the origin alone, $\Sigma_0=\{0\}$; there is no nonzero square-zero element. **The nilpotent class of the block is empty**: the nilpotent cone is the empty set, no element is of nilpotency index two or more, and the block carries no operator of a nilpotent and no flag. The zero-divisor set is not empty, but no zero divisor is square-zero; the contrast with the complex block, whose nilpotents fill the pure isotropic cone, is again the definiteness of the norm.

The article is algebraic. The zero-divisor set, its family and the criterion on the norm are *Zero Divisors of the Symmetric Plain Algebra*; the roots of $+e_t$ and the idempotents are *Square Roots of One and the Idempotents of the Symmetric Plain Algebra*; the general root problem is *Square Roots of a General Element in the Symmetric Plain Algebra*; the operator theory of the block is *The Multiplication Operators of the Symmetric Plain Algebra*; and the law that the block fails, and which would carry a nilpotent operator, is *The Specificities of the Symmetric Plain Algebra*. The class is empty, so there is no separate literature of the cone, of the flag or of the ideal–annihilator coincidence to point to: those are the objects of the complex block and of the general plain algebra, and the block has none of them.

**Conventions.** The algebra is $\mathbb{H}$ with basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$ and $\vec e_x\vec e_y=\vec e_z$, so that $\vec e_k^2=-e_t$ and $e_j\vec e_k=-\vec e_ke_j$ for $j\neq k$. An element is $\tilde q=q_te_t+\vec q$ with $\vec q=\sum_{k=1}^{3}q_k\vec e_k$ and $q_\mu\in\mathbb{R}$; $\vec p\cdot\vec q=\sum_kp_kq_k$ is the Euclidean dot product of the vector parts, and the plain square is $\tilde q^2=(q_t^2-|\vec q|^2)e_t+2q_t\vec q$. The **norm** is $N(\tilde q)=\tilde q\tilde q^{\natural}=q_t^2+|\vec q|^2$; the natural sign ${}^{\natural}$ is the quaternion conjugation, the bar is the identity because $\mathbb{R}$ has no nontrivial involution, and the star coincides with the natural sign. The scalar line $\mathbb{R}e_t$ is the centre and the vector subspace is $\mathrm{Vect}(\mathbb{H})=\operatorname{Im}\mathbb{H}$ (*Introduction to the Remarkable Subspaces of the Quaternions*). The left multiplication is $L^{\bullet}_{\tilde p}\tilde q=\tilde p\bullet\tilde q$. A root of a central value is written $\tilde\xi$ (§*The Root Convention* of *Conventions in Mathematics*), a nilpotent $\tilde\nu$ (§*The Nilpotent Convention*), and a generic element $\tilde p$ or $\tilde q$.

The equations name a product, so the roots and the nilpotents are relative to it. The general definition of the power, the square and the root of a central value, and the general definition of the nilpotent, with the index of nilpotency and the square-zero element, are *Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*, §*The Element Vocabulary*. Throughout this article the square is the one of the symmetric plain product, which is the plain square; the other five structures over the same space carry roots of $0$ and square-zero sets of their own.

## The Roots of Zero

**The roots of $0$ are exactly the origin, $\Sigma_0=\{0\}$; there is no nonzero square-zero element.**

A **root of $0$** is an element $\tilde\xi\in\mathbb{H}$ with $\tilde\xi\bullet\tilde\xi=0$, the square being the one of the symmetric plain product.

### The Reduction

Write the root in scalar and vector parts,

$$
\tilde\xi=\xi_te_t+\vec\xi,\qquad \vec\xi=\xi_x\vec e_x+\xi_y\vec e_y+\xi_z\vec e_z,\qquad \xi_k\in\mathbb{R}.
$$

The square of the block is the plain square, so equating $\tilde\xi^2$ to the central element $\lambda e_t$ splits the equation into a vector part and a scalar part; at $\lambda=0$,

**Proposition (the reduction at the value $0$).** For $\tilde\xi=\xi_te_t+\vec\xi$,

$$
\tilde\xi\bullet\tilde\xi=0\qquad\Longleftrightarrow\qquad
\begin{cases}
2\xi_t\vec\xi=0,\\[2pt]
\xi_t^2-|\vec\xi|^2=0 .
\end{cases}
$$

*Proof.* Specialisation of the central reduction of *Square Roots of One and the Idempotents of the Symmetric Plain Algebra* to $\lambda=0$: the plain square is $\tilde\xi^2=(\xi_t^2-|\vec\xi|^2)e_t+2\xi_t\vec\xi$, and the element vanishes exactly when both its parts do.

Since $\mathbb{R}$ is a field, the vector equation holds exactly when $\xi_t=0$ or $\vec\xi=0$. **Only the scalar equation survives on each branch**: the root is pure, $\xi_t=0$, or it is a real scalar, $\vec\xi=0$.

### The Scalar Case

In the scalar case $\tilde\xi=\xi_te_t$ and the scalar equation reads $\xi_t^2=0$; since $\mathbb{R}$ is a field, $\xi_t=0$. The root in this case is the single element

$$
\tilde\xi=0,
$$

the origin.

### The Pure Case Is Empty

In the pure case $\tilde\xi=\vec\xi$ and the scalar equation reads

$$
-|\vec\xi|^2=0,
$$

that is $\vec\xi=0$: the pure branch returns the origin and no other element. **There is no nonzero pure root of $0$**, the Euclidean form of the vector subspace being definite, so a pure element has a non-positive square, $-|\vec q_a|^2e_t$, which vanishes only at the origin.

### Statement of the Theorem

**Theorem.** The roots of $0$ of the block are exactly the origin,

$$
\Sigma_0=\{0\}.
$$

*Proof.* By the reduction the root is pure or scalar. The scalar case gives $\xi_t=0$; the pure case gives $\vec\xi=0$; both return the origin, and the origin is a root. The two cases exhaust the equation and the class has one element.

### Verification

The origin is a root, $0\bullet0=0$, and nothing else is: the pure branch needs $|\vec\xi|^2=0$ and the scalar branch $\xi_t^2=0$, both of which have the origin as their only real solution. A worked instance outside the block is the general plain product, whose roots of $0$ are the same origin, the two squares agreeing. The smallest non-central witness confirms the emptiness: the pure element $\vec e_x$ has square $\vec e_x^2=-e_t\neq0$, and the element $e_t+\vec e_x$ has square $e_t+2\vec e_x+\vec e_x^2=2\vec e_x\neq0$.

### The Roots of Zero and the Nilpotents

The nonzero roots of $0$ are exactly the **nilpotents** of the block. The roots of $0$ here are the origin alone, so the nilpotents are none. A nonzero root of $0$ would be a square-zero element, hence a zero divisor annihilating itself; the block has zero divisors, the whole punctured vector subspace, and none of them is square-zero. The behaviour is the opposite of the roots of $+e_t$, which are units of the block (*Square Roots of One and the Idempotents of the Symmetric Plain Algebra*), and it is the degenerate case of the general root problem at the central value $0$ (*Square Roots of a General Element in the Symmetric Plain Algebra*).

## The Nilpotents

**The nilpotents of the block are none: there is no nonzero square-zero element, the nilpotent cone is the empty set, and no element is of nilpotency index two or more.**

The **nilpotents** of the block are the nonzero elements whose square vanishes. The class is empty, and it is empty over the plain product as well, the two squares being equal; the block does not enlarge it. What separates the two products is the rest of the square-zero question: the plain product is a division rule, while the block has the zero divisors of the vector subspace, and one might expect the symmetrisation to place square-zero elements among them. It places none, because the defining equation reduces to $|\vec P|^2=0$.

### The Definition

**Definition (nilpotent of a product).** Let $\star$ be a product on $\mathbb{H}$; a **nilpotent of $\star$** is a nonzero element $\tilde\nu$ with $\tilde\nu^{\star k}=0$ for some $k\geq1$, and the least such $k$ is the **index of nilpotency**. The case $k=2$ is a **square-zero** element. The element $0$ is a square-zero element and is not a nilpotent.

The equation names a product, and the notion is relative to it; the general definition, with the index of nilpotency and the square-zero element, is *Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*, §*The Element Vocabulary*. Throughout this article the product is the symmetric plain product, which has the plain square.

The natural sign preserves square-zero elements, conjugation being multiplicative and carrying a vanishing square to a vanishing square,

$$
(\tilde\nu^{\natural})^{\bullet2}=(\tilde\nu^{\bullet2})^{\natural}=0 ,
$$

and the star, which coincides with the natural sign over $\mathbb{R}$, does the same. Were the class not empty, it would be a conjugation-stable class; as it is, the statement is vacuous and is recorded for the form of the definition.

### The Criterion

**An element is square-zero exactly when it is the origin: the pure elements with isotropic vector part, $P_0=0$ and $(\vec P,\vec P)=0$, are the solutions of the equation, and over $\mathbb{R}$ the only one is $0$.**

The square of a general element closes in two terms, one central and one along the vector part, because the vector part is a pure quaternion combination and its own square is central:

$$
\tilde q^2=\bigl[q_t^2-(\vec q,\vec q)\bigr]e_t+2q_t\vec q .
$$

**Theorem (the criterion for a square-zero element).** For $\tilde p\in\mathbb{H}$ the following are equivalent: $\tilde p\bullet\tilde p=0$; $\tilde p$ is pure, $p_0=0$, and its vector part is isotropic, $(\vec p,\vec p)=0$; and $\tilde p=0$.

*Proof.* The displayed formula expands the square. If $p_0\neq0$ then the vector part $2p_0\vec p$ vanishes only for $\vec p=0$, and then the scalar part is $p_0^2\neq0$; so a square-zero element is pure. For a pure $\tilde p$ the formula reads $\tilde p^2=-(\vec p,\vec p)e_t$, which vanishes exactly when $(\vec p,\vec p)=|\vec p|^2=0$, and the Euclidean form being definite this holds exactly when $\vec p=0$, that is for $\tilde p=0$.

**Corollary.** The only square-zero element of the block is the origin; the block has no nilpotent, and its nilpotent class is the empty set.

**The criterion for an empty class.** The class of nonzero nilpotents is not recognized as empty from a law of the product alone: a symmetric product carries no law that forbids a square-zero element, and *Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*, §*The Criterion for an Empty Class*, sends the class of the two symmetric structures to the basis for that reason. Read on the basis, the class is empty: the equation $|\vec P|^2=0$ has the origin as its only real solution. The emptiness is thus the definiteness of the Euclidean form, not the emptiness of the zero-divisor set.

### The Empty Nilpotent Cone

The set of square-zero elements is $\{0\}$, so the **nilpotent cone is the empty set**: there is no parametrisation of it, no real dimension to give, and no family of isotropic pure elements, the Euclidean form of the vector subspace being definite. Over the complex block the pure square $-\vec U^2=-(\vec U,\vec U)e_t$ is indefinite, the isotropic pure elements form a cone of complex dimension two, and the nilpotents fill it; the real block has none of them.

### The Nilpotency Index

**Proposition (there is no nilpotent, hence no index).** For every nonzero $\tilde p\in\mathbb{H}$ and every $k\geq1$ the power $\tilde p^{\bullet k}$ is nonzero, so no element has a vanishing power and the index of nilpotency is undefined.

*Proof.* The block's powers are the plain powers, since the plain product is associative and the powers of a single element commute: $\tilde p^{\bullet k}=\tilde p^k$. The plain product of $\mathbb{H}$ is a division rule, so no power of a nonzero element vanishes, and the conclusion follows at every $k$.

The clause is the strict form of the emptiness: it is not merely that no square vanishes, but that no power of any order vanishes. The block therefore carries no element of index two, none of index three, and no higher index either, and the two clauses of the definition of a nilpotent are never satisfied.

### The Absence of the Operator of a Nilpotent

**Proposition (no operator of the block is nilpotent).** For every nonzero $\tilde p$ and every $k\geq1$ the left multiplication satisfies $(L^{\bullet}_{\tilde p})^k\neq0$.

*Proof.* The operator evaluated on the unit gives the power, $(L^{\bullet}_{\tilde p})^k e_t=\tilde p^{\bullet k}=\tilde p^k$, which is nonzero by the proposition above; so the operator is not nilpotent.

Since the nilpotent class is empty, the whole operator reading of a nilpotent is empty with it: there is **no square-zero operator of an element**, no index-three operator, no image $\mathrm{span}\{e_t,\tilde\nu\}$, no failure of the image to lie in the kernel, no intersection line and no splitting of the space in place of a flag. Those objects belong to the complex block, where $L^{\bullet}_{\tilde\Upsilon}$ has index three and the flag calculus fails (*The Specificities of the Symmetric Plain Algebra*); over $\mathbb{R}$ the class that would carry them does not exist, and the absence is stated and not filled.

### The Separation from the Zero Divisors

**Proposition (the zero divisors are not square-zero).** The zero-divisor set of the block is the punctured vector subspace, of real dimension three, and no element of it is square-zero.

*Proof.* For a nonzero pure element $\vec q_a$ and an arbitrary $\tilde y=y_0e_t+\vec y$ the product is $\vec q_a\bullet\tilde y=-( \vec q_a\cdot\vec y)e_t$; it vanishes for the nonzero solutions $\vec y$ orthogonal to $\vec q_a$, so every nonzero pure element is a zero divisor, with annihilator the orthogonal plane of dimension two. Conversely, for a non-pure $\tilde q=q_te_t+\vec q$ with $q_t\neq0$, the equation $\tilde q\bullet\tilde y=0$ reads $(q_ty_0-\vec q\cdot\vec y)e_t+q_t\vec y+y_0\vec q=0$, which forces $y_0=0$ and $\vec y=0$, so $\tilde q$ is not a zero divisor. The zero-divisor set is therefore the punctured vector subspace (*Zero Divisors of the Symmetric Plain Algebra*), and its elements are nonzero and pure, with square $-|\vec q_a|^2e_t\neq0$.

**Corollary (the empty class inside a nonempty one).** The block's zero-divisor set is large — every nonzero pure element — and its square-zero set is $\{0\}$; the two are disjoint away from the origin. A nilpotent would be a zero divisor annihilating itself, and the block has no such element.

### The Relation to the Other Notions

**Nilpotents and the zero divisors.** The class is empty, so no nilpotent is a zero divisor: the zero-divisor set of the block is the punctured vector subspace and none of its elements has a vanishing square. This is the sharpest form of the separation between the two classes.

**Nilpotents and the idempotents.** The only square-zero element is the origin, and the origin is an idempotent; so the square-zero class and the idempotent class meet exactly at $0$. The block has no nilpotent and no non-trivial idempotent, and the two absences have the same source, the definiteness of the norm (*Square Roots of One and the Idempotents of the Symmetric Plain Algebra*).

**Nilpotents and the roots.** The nilpotents are exactly the nonzero roots of $0$ of the block, and the roots of $0$ are the origin alone, so the nilpotent class is the empty part of the root set. This is the degeneracy of the general square-root problem at the central value $0$ (*Square Roots of a General Element in the Symmetric Plain Algebra*).

### The Reading on the Remarkable Subspaces

The square-zero elements are pure, so a square-zero element would lie in the vector subspace $\mathrm{Vect}(\mathbb{H})$, the three-dimensional space of pure elements; the only one is the origin, which lies there. The centre $\mathbb{R}e_t$ contains none but the origin as well, a central element $\lambda e_t$ having the square $\lambda^2e_t$, which vanishes only for $\lambda=0$. **Of the two remarkable subspaces over $\mathbb{R}$ neither contains a nilpotent**, the origin being the only square-zero element of the space.

## Summary

The square of the block is the plain square, so the roots of $0$ of the block are exactly the roots of $0$ of the general plain algebra. Over $\mathbb{R}$ the class is small: the equation reads $\xi_t^2-|\vec\xi|^2=0$ with $2\xi_t\vec\xi=0$, the scalar branch gives $\xi_t=0$ and the pure branch gives $\vec\xi=0$, and the only solution is the origin, $\Sigma_0=\{0\}$. The block has no nonzero square-zero element, and it has no element with a vanishing power of any order, the block's powers being the plain powers of a division rule; the index of nilpotency is therefore undefined.

The nilpotent class of the block is empty: there is no nilpotent cone, the set of square-zero elements is $\{0\}$, and the class is not recognized as empty by a law of the product — a symmetric product carries none that forbids a square-zero element — but by the definiteness of the Euclidean form, read on the basis. The block carries no operator of a nilpotent, no index-three operator, no flag and no failure of the ideal–annihilator coincidence, those being the objects of the complex block; and no operator of the block is nilpotent, $(L^{\bullet}_{\tilde p})^k\neq0$ for every nonzero $\tilde p$. The zero-divisor set is the punctured vector subspace, of real dimension three, with the orthogonal plane as annihilator, and it is disjoint from the square-zero class away from the origin. The square-zero class and the idempotent class meet only at the origin, and the nilpotents are the empty part of the roots of $0$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde p\bullet\tilde q$ | the symmetric plain product, the multiplication of the block |
| $\tilde\xi$ | a root of $0$, $\tilde\xi\bullet\tilde\xi=0$ |
| $\tilde\xi=\xi_te_t+\vec\xi$ | scalar and vector parts of a root |
| $\Sigma_0=\{0\}$ | the roots of $0$, the origin alone |
| $\tilde\nu$ | a nilpotent, $\tilde\nu\neq0$ and $\tilde\nu^{\bullet k}=0$ for some $k$ |
| $(\vec p,\vec p)=|\vec p|^2=0$ | the square-zero equation, satisfied only by the origin |
| $\varnothing$ | the nilpotent class of the block |
| $\mathrm{Vect}(\mathbb{H})\setminus\{0\}$ | the zero-divisor set, none of its elements square-zero |
| $(L^{\bullet}_{\tilde p})^k\neq0$ | no operator of the block is nilpotent |
| $\tilde p^{2}=(p_0^2-|\vec p|^2)e_t+2p_0\vec p$ | the square that decides the criterion |

## Further Reading

- *Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*, §*The Element Vocabulary* and §*The Criterion for an Empty Class*, for the product-relative definition of a nilpotent and the rule by which the class is recognized as empty.
- *Introduction to the Symmetric Plain Algebra of Quaternions*, for the product, the unit and the square.
- *Introduction to the General Plain Algebra of Quaternions*, for the division property of the plain product that empties the square-zero class.
- *Square Roots of One and the Idempotents of the Symmetric Plain Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-symmetric-plain-algebra-of-quaternioid.md`), for the roots of $+e_t$ and the idempotents, the companion central element class.
- *Square Roots of a General Element in the Symmetric Plain Algebra* (`articles_maths/square-roots-of-a-general-element-in-the-symmetric-plain-algebra-of-quaternioid.md`), for the roots of the general quadratic $\tilde\xi\bullet\tilde\xi=\tilde q$, of which the roots of $0$ here are the degenerate case.
- *Zero Divisors of the Symmetric Plain Algebra*, for the zero-divisor set, the punctured vector subspace disjoint from the square-zero class.
- *Norm and Invertibility in the Symmetric Plain Algebra*, for the norm whose definiteness empties the nilpotent class.
- *The Specificities of the Symmetric Plain Algebra*, for the algebra that carries the index-three operator of a nilpotent on the complex block, and the block's absence of it.
- *The Multiplication Operators of the Symmetric Plain Algebra*, for the operator theory, in which no operator of the block is nilpotent.
- *Square Roots of Zero and the Nilpotents of the General Plain Algebra*, for the square-zero class of the plain product, which the block shares.
