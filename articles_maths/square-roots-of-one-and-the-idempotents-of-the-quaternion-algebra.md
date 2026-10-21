# __Square Roots of One and the Idempotents of the Quaternion Algebra__

## Introduction

The algebra of this article is the quaternion algebra $\mathbb{H}$, the real space $\mathbb{H}$ under the quaternion product $\tilde q_1\tilde q_2$ of *Introduction to the Quaternion Algebra*, the multiplication of the quaternion algebra. It is associative with a two-sided unit, and it is a division rule; that product is the one read throughout this article.

The article treats two subjects, and in this order. The first is the square roots of the central value $+e_t$, the elements $\tilde\xi\in\mathbb{H}$ with

$$
\tilde\xi^2=e_t.
$$

The second is the idempotents of the algebra, the elements $\tilde\pi$ with $\tilde\pi^2=\tilde\pi$. The two subjects are one subject, because the **halving map**

$$
\tilde\xi\longmapsto\tilde\pi=\tfrac12(e_t+\tilde\xi),\qquad \tilde\xi^2=e_t,
$$

is a bijection from the roots of $+e_t$ onto the idempotents, with inverse $\tilde\xi=2\tilde\pi-e_t$. The reason is a two-line computation: if $\tilde\xi^2=e_t$ then $\tilde\pi^2=\tfrac14(e_t+2\tilde\xi+e_t)=\tilde\pi$, and if $\tilde\pi^2=\tilde\pi$ then $(2\tilde\pi-e_t)^2=4\tilde\pi^2-4\tilde\pi+e_t=e_t$. Every idempotent of the algebra is read through that map, on the roots of $+e_t$ alone, and the families of idempotents are the families of the roots of $+e_t$ read through it.

**The results.** The roots of $+e_t$ are the two central scalars $\pm e_t$, and there are no others; the class is the two-point set, the central part of the level set $\{N=1\}$ of the algebra. The idempotents are the origin and the unit, $\tilde\pi\in\{0,e_t\}$; the halving map $\tilde\xi\mapsto\tfrac12(e_t+\tilde\xi)$ is a bijection carrying the pair $\{\tilde\xi,-\tilde\xi\}$ to the complementary pair $\{\tilde\pi,e_t-\tilde\pi\}$; and the Peirce decomposition is degenerate, one Peirce space being the whole algebra and the other three $\{0\}$. The roots of $-e_t$ are one paragraph: over $\mathbb{R}$ the centre has no element of square $-e_t$, so the sign cannot be flipped, and the roots of $-e_t$ are read from the same reduction as the level set $\{N=1\}$ of the vector subspace.

The article is algebraic. It does not treat the roots of the general quadratic $\tilde\xi^2=\tilde q$, which is *Square Roots of a General Element in the Quaternion Algebra*; the roots of $0$ and the nilpotents, which are *Square Roots of Zero and the Nilpotents of the Quaternion Algebra*; the structure of the zero-divisor set, which is *Zero Divisors of the Quaternion Algebra*; or the idempotent theory of the complexified block, which is *Square Roots of One and the Idempotents of the Quaternion Algebra*. The last paragraph of §*The Roots of One* records how the roots of $-e_t$ are read; it is a remark, it is used nowhere, and it opens nothing.

**Conventions.** The algebra is $\mathbb{H}$ with basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$ and $\vec e_x \vec e_y=\vec e_z$, so that $\vec e_k^2=-e_t$ and $\vec e_\mu \vec e_\nu=-\vec e_\nu \vec e_\mu$ for $\mu\neq\nu$. An element is $\tilde q=q_te_t+\vec q$ with $\vec q=\sum_{k=1}^{3}q_k\vec e_k$ and $q_\mu\in\mathbb{R}$; the scalar part is $q_t=\mathrm{Sc}(\tilde q)$ and the vector part is $\vec q$. The natural conjugation is $\tilde q^{\natural}=q_te_t-\vec q$, and the **norm** is $\langle\tilde q\rangle_{\natural}=\tilde q\tilde q^{\natural}=q_t^2+|\vec q|^2$, positive definite over $\mathbb{R}$ by *Norm and Invertibility in the Quaternion Algebra*; every nonzero element is a unit, $\tilde q^{-1}=\tilde q^{\natural}/\langle\tilde q\rangle_{\natural}$, so there is no zero divisor. The scalar line $\mathbb{R}e_t$ is the centre and the vector subspace is $\mathrm{Vect}(\mathbb{H})$, of dimension three. A root of a central value is written $\tilde\xi$ (§*The Root Convention* of *Conventions in Mathematics*), an idempotent $\tilde\pi$ (§*The Idempotent Convention*), and a generic element $\tilde q$.

The equations name a product, so the roots and the idempotents are relative to it. The general definition of the power, the square and the root of a central value, and the general definition of an idempotent, are *Algebras: A General Introduction*; the orthogonal, complete and primitive families, the projection and the Peirce decomposition are *Unital Algebras*, §*Idempotents and the Peirce Decomposition*. Throughout this article the square is the one of the quaternion product, the multiplication of the algebra.

## The Roots of One

**The roots of $+e_t$ are exactly the two central scalars $\pm e_t$; there are no others, and the class is the two-point set.**

A **root of $+e_t$** is an element $\tilde\xi\in\mathbb{H}$ with $\tilde\xi^2=e_t$, the square being the one of the quaternion product.

### The Reduction

Write the root in scalar and vector parts,

$$
\tilde\xi=\xi_te_t+\vec\xi,\qquad \vec\xi=\xi_x\vec e_x+\xi_y\vec e_y+\xi_z\vec e_z,\qquad \xi_k\in\mathbb{R}.
$$

The square of an element of the algebra closes in two terms, one central and one along the vector part, because the square of a pure element is central:

$$
\vec\xi^2=-|\vec\xi|^2e_t,\qquad \tilde q^2=\bigl[q_t^2-|\vec q|^2\bigr]e_t+2q_t\vec q.
$$

**Proposition (the central reduction).** For $\tilde\xi=\xi_te_t+\vec\xi$ and $\lambda\in\mathbb{R}$,

$$
\tilde\xi^2=\lambda e_t\qquad\Longleftrightarrow\qquad
\begin{cases}
2\xi_t\vec\xi=0,\\[2pt]
\xi_t^2-|\vec\xi|^2=\lambda.
\end{cases}
$$

*Proof.* The square is $\tilde\xi^2=(\xi_t^2-|\vec\xi|^2)e_t+2\xi_t\vec\xi$, and the element equals the central element $\lambda e_t$ exactly when its vector part vanishes and its scalar part is $\lambda$, which is the displayed pair.

Since $\mathbb{R}$ is a field, the vector equation holds exactly when $\xi_t=0$ or $\vec\xi=0$. **Only the scalar equation survives on each branch**: the root is pure, $\xi_t=0$, or it is a real scalar, $\vec\xi=0$. The case $\lambda=0$ is *Square Roots of Zero and the Nilpotents of the Quaternion Algebra*, below this article in this category, and the general radicand $\tilde q$ is *Square Roots of a General Element in the Quaternion Algebra*, below this article in this category.

### The Scalar Case

In the scalar case $\tilde\xi=\xi_te_t$ and the scalar equation reads $\xi_t^2=1$, whose roots are the two central elements

$$
\tilde\xi=+e_t,\qquad \tilde\xi=-e_t.
$$

They are the only roots of $+e_t$ with non-vanishing scalar part and the only ones in the centre $\mathbb{R}e_t$.

### The Pure Case Is Empty

In the pure case $\tilde\xi=\vec\xi$ and the scalar equation reads

$$
-|\vec\xi|^2=1,
$$

a value no real vector attains. **There is no pure root of $+e_t$.** The reason is the definiteness of the sum of squares: the square of a pure element is the negative scalar $\vec\xi^2=-|\vec\xi|^2e_t$, so a pure element is a root of a negative central value and never of a positive one.

### Statement of the Theorem

**Theorem.** The roots of $+e_t$ of the algebra are exactly the two central scalars

$$
\tilde\xi=+e_t,\qquad \tilde\xi=-e_t,
$$

the class being the two-point set $\{+e_t,-e_t\}$.

*Proof.* By the reduction the root is pure or scalar. The pure case is impossible, $|\vec\xi|^2=-1$ having no real solution. The scalar case gives $\xi_t^2=1$, that is $\pm e_t$. The two cases exhaust the equation and the set has two elements.

### Verification

The two elements are roots, $(\pm e_t)^2=e_t$, and nothing else is, because the reduction yields only the two branches and the pure branch is empty. The class is the **central part of the level set** $\{N=1\}$: the level set is the elements of norm one, and a central element is a real scalar $se_t$ of norm $\langle se_t\rangle_{\natural}=s^2$, so the central elements of the level set are $\pm e_t$.

### The Roots of One Are Units

A root of $+e_t$ is a **unit**: $\tilde\xi^2=e_t$ reads $\tilde\xi\tilde\xi=e_t$, so $\tilde\xi$ is invertible with inverse

$$
\tilde\xi^{-1}=\tilde\xi,
$$

and a unit is not a zero divisor. The single element common to the roots of $+e_t$ and the idempotents is $e_t$: an element that is both a root of $+e_t$ and an idempotent satisfies $\tilde\xi^2=e_t$ and $\tilde\xi^2=\tilde\xi$, hence $\tilde\xi=e_t$. The two classes are different sets, and the halving map of §*The Idempotents* is the bijection between them.

**The roots of minus one.** The roots of $-e_t$ are not the image of the roots of $+e_t$ here, because the mechanism that flips the sign is unavailable. For a product bilinear in its two slots with a **central element of square $-e_t$**, an element $i$ of the centre with $i^2=-e_t$, multiplication by it flips the sign, $(i\tilde\xi)^2=i^2\tilde\xi^2=-\tilde\xi^2$, and the roots of $-e_t$ are read off the roots of $+e_t$ by one map; over $\mathbb{R}$ the centre is the scalar line $\mathbb{R}e_t$ and no central element has square $-e_t$, so the mechanism is unavailable and the two root sets are not carried one to the other. They follow instead from the same reduction, at $\lambda=-1$: the scalar equation of §*The Reduction* reads $-\lvert\vec\xi\rvert^2=-1$ on the pure branch, that is $\lvert\vec\xi\rvert^2=1$, so the roots of $-e_t$ are exactly the elements of the vector subspace $\mathrm{Vect}(\mathbb{H})$ with $\langle \vec\xi\rangle_{\natural}=|\vec\xi|^2=1$, a quadric of real dimension two. The class exists, it is not empty, and it indexes no idempotent; the halving map uses the roots of $+e_t$ alone, and the roots of $-e_t$ are quoted here and used nowhere in this article.

## The Idempotents

**The idempotents of the algebra are exactly the origin and the unit, $\tilde\pi\in\{0,e_t\}$; the class is the two-point set, and there is no non-trivial idempotent.**

The **idempotents** of the algebra are the elements satisfying $\tilde\pi^2=\tilde\pi$, the square being the one of the quaternion product. They correspond to projectors under multiplication, and the algebra has only the two trivial ones; what remains of the theory is the halving map from the roots of $+e_t$, the complementary pairs, and a degenerate Peirce decomposition.

### The Definition

**Definition.** An element $\tilde\pi$ of $\mathbb{H}$ is an **idempotent of the quaternion algebra** when

$$
\tilde\pi^2=\tilde\pi.
$$

The origin is an idempotent, and so is the unit $e_t$; the two are the **trivial idempotents**. The equation names a product, and the notion is relative to it: throughout this article the product is the quaternion product, the multiplication of the algebra, and another product is named where it is meant.

Idempotents encode direct summands of the regular module,

$$
\mathbb{H}=\mathbb{H}\tilde\pi\oplus\mathbb{H}(e_t-\tilde\pi),\qquad \mathbb{H}=\tilde\pi\mathbb{H}\oplus(e_t-\tilde\pi)\mathbb{H},
$$

and every such decomposition arises from an idempotent. A **primitive** idempotent, one that is not a sum of two nonzero orthogonal idempotents, generates an **indecomposable** left ideal; here that ideal is $\mathbb{H}$ itself, minimal because the algebra is a division algebra. The general statements, with the orthogonal, complete and primitive families, the projection and the Peirce decomposition, are *Unital Algebras*, §*Idempotents and the Peirce Decomposition*. Over $\mathbb{R}$ the possibilities are as small as an algebra permits, and the sections below compute them.

### The Classification

**Theorem (the idempotents).** The idempotents of the algebra are exactly the origin and the unit:

$$
\tilde\pi\in\{0,\ e_t\}.
$$

There is no non-trivial idempotent.

*Proof.* Write the equation as $\tilde\pi^2=\tilde\pi$ and factor it as $\tilde\pi(\tilde\pi-e_t)=0$. The quaternion product is a **division rule**: it has the two-sided unit $e_t$ and no zero divisor, every nonzero element being invertible with $\tilde\pi^{-1}=\tilde\pi^{\natural}/\langle\tilde\pi\rangle_{\natural}$ (*Norm and Invertibility in the Quaternion Algebra*). A vanishing product in a division algebra has a vanishing factor, so either $\tilde\pi=0$ or $\tilde\pi-e_t=0$. The same conclusion in coordinates reads the square $\tilde\pi^2=(\pi_t^2-|\vec\pi|^2)e_t+2\pi_t\vec\pi$ and the pair $2\pi_t\vec\pi=\vec\pi$, $\pi_t^2-|\vec\pi|^2=\pi_t$: the first forces $(2\pi_t-1)\vec\pi=0$, and $\vec\pi\neq0$ with $\pi_t=\tfrac12$ would give $|\vec\pi|^2=-\tfrac14$, which has no real solution, so $\vec\pi=0$ and $\pi_t\in\{0,1\}$. **The two cases exhaust the equation and no non-trivial idempotent occurs.**

**Remark (why the class collapses over $\mathbb{R}$).** The standard construction of a non-trivial idempotent is the element $\tfrac12(e_t+\tilde\xi)$ with $\tilde\xi$ a **non-central root of $+e_t$**: the square $\tfrac14(e_t+2\tilde\xi+\tilde\xi^2)$ equals $\tfrac12(e_t+\tilde\xi)$ exactly when $\tilde\xi^2=e_t$. Over $\mathbb{R}$ the roots of $+e_t$ are the two central scalars $\pm e_t$, so $\tfrac12(e_t+\tilde\xi)$ returns only $e_t$ and $0$; a non-central root of $+e_t$ would need a pure element of square $+e_t$, and the pure square is the non-positive $-|\vec\xi|^2e_t$. In the complexified block the roots of $+e_t$ include non-central elements, the construction closes, and a whole family of idempotents lies between the two trivial ones; that counterpart is *Square Roots of One and the Idempotents of the Quaternion Algebra*.

**Corollary (the class is two-point).** The idempotent class of the algebra is $\{0,e_t\}$, and the two are orthogonal, $0\cdot e_t=0$.

### Orthogonal and Complete Families

An **orthogonal family** is a family of idempotents with $\tilde\pi_i\tilde\pi_j=0$ for $i\neq j$; it is **complete** when the sum of its members is $e_t$. A nonzero idempotent is **primitive** when it is not the sum of two nonzero orthogonal idempotents.

**Theorem (the families).** In the algebra:

- every orthogonal family contains at most one nonzero idempotent;
- the only complete orthogonal family of nonzero idempotents is the singleton $\{e_t\}$;
- the unit $e_t$ is the only primitive idempotent, and $0$ is not primitive.

*Proof.* By the theorem above every idempotent is $0$ or $e_t$. Two distinct nonzero idempotents would both be $e_t$, which is not orthogonal to itself, $e_t e_t=e_t\neq0$; so no orthogonal family contains two nonzero members. A complete orthogonal family of nonzero idempotents sums to $e_t$, and since it contains at most one nonzero idempotent it is either empty, with sum $0\neq e_t$, or the singleton $\{e_t\}$. For primitivity, $e_t$ is not a sum of two nonzero orthogonal idempotents because there are no two distinct nonzero idempotents to sum; and $0$ is not primitive under the convention that a primitive idempotent is nonzero.

**Corollary (no nontrivial decomposition).** The only decompositions of the algebra carried by an idempotent are the two trivial ones: for $\tilde\pi=e_t$,

$$
\mathbb{H}=e_t\mathbb{H}\oplus(e_t-e_t)\mathbb{H}=\mathbb{H}\oplus\{0\},
$$

and for $\tilde\pi=0$,

$$
\mathbb{H}=0\cdot\mathbb{H}\oplus(e_t-0)\mathbb{H}=\{0\}\oplus\mathbb{H}.
$$

There is no proper nonzero direct summand of the regular module in the quaternion product.

### The Peirce Decomposition

For an idempotent $\tilde\pi$ the **Peirce decomposition** is the direct sum

$$
\mathbb{H}=\tilde\pi\mathbb{H}\tilde\pi\;\oplus\;\tilde\pi\mathbb{H}(e_t-\tilde\pi)\;\oplus\;(e_t-\tilde\pi)\mathbb{H}\tilde\pi\;\oplus\;(e_t-\tilde\pi)\mathbb{H}(e_t-\tilde\pi),
$$

the four **Peirce spaces** of the idempotent.

**Theorem (the Peirce decomposition is trivial).** For each of the two idempotents of the algebra one Peirce space is the whole algebra and the other three are $\{0\}$:

$$
\tilde\pi=e_t:\quad \mathbb{H}=\mathbb{H}\oplus\{0\}\oplus\{0\}\oplus\{0\},\qquad \tilde\pi=0:\quad \mathbb{H}=\{0\}\oplus\{0\}\oplus\{0\}\oplus\mathbb{H}.
$$

*Proof.* For $\tilde\pi=e_t$ the four spaces are $e_t\mathbb{H}e_t=\mathbb{H}$, $e_t\mathbb{H}(e_t-e_t)=0$, $(e_t-e_t)\mathbb{H}e_t=0$ and $(e_t-e_t)\mathbb{H}(e_t-e_t)=0$. For $\tilde\pi=0$ the same computation exchanges the outer factors.

So the Peirce decomposition of the algebra is the trivial one, with Peirce spaces $\mathbb{H}$ and $\{0\}$ and no off-diagonal space. In particular the two off-diagonal Peirce units, which in the complexified block generate the minimal ideals, do not exist over $\mathbb{R}$: such a unit satisfies $\tilde\nu^2=0$ with $\tilde\nu\neq0$, and there is none (*Square Roots of Zero and the Nilpotents of the Quaternion Algebra*).

### The Halving Map and the Bijection With the Roots of One

**Theorem (the halving bijection).** The map

$$
\tilde\xi\longmapsto\tilde\pi(\tilde\xi),\qquad \tilde\pi(\tilde\xi)=\tfrac12(e_t+\tilde\xi),
$$

is a **bijection** from the set of roots of $+e_t$ onto the set of idempotents of the algebra, with inverse $\tilde\xi=2\tilde\pi-e_t$, and it carries the pair $\{\tilde\xi,-\tilde\xi\}$ to the complementary pair $\{\tilde\pi,e_t-\tilde\pi\}$.

*Proof.* The equivalence $\tilde\pi^2=\tilde\pi\Longleftrightarrow(2\tilde\pi-e_t)^2=e_t$ is the two-line computation of the introduction, read in both directions. *Well defined:* if $\tilde\xi^2=e_t$ then $\tilde\pi(\tilde\xi)^2=\tfrac14(e_t+2\tilde\xi+\tilde\xi^2)=\tfrac12(e_t+\tilde\xi)=\tilde\pi(\tilde\xi)$. *Injective and surjective:* if $\tilde\xi$ is a root of $+e_t$ then $\tilde\pi=\tfrac12(e_t+\tilde\xi)$ is an idempotent, and every idempotent arises so, its inverse image being $\tilde\xi=2\tilde\pi-e_t$; the two maps are inverse to each other. *The pair:* $\tilde\pi(-\tilde\xi)=\tfrac12(e_t-\tilde\xi)=e_t-\tilde\pi(\tilde\xi)$.

**Corollary (the correspondence).** The roots of $+e_t$ being the two points $\pm e_t$, the correspondence is

$$
0\longleftrightarrow-e_t,\qquad e_t\longleftrightarrow+e_t,
$$

so the two-point idempotent class is the image of the two-point root class, and the count of the idempotents of the algebra equals the count of the roots of $+e_t$, two on each side. Consequently the **complementary pairs** $\{\tilde\pi,e_t-\tilde\pi\}$ of idempotents are in bijection with the roots of $+e_t$ modulo the sign identification $\tilde\xi\sim-\tilde\xi$.

### The Complementary Idempotent

**Proposition (the complementary idempotent).** If $\tilde\pi$ is an idempotent of the algebra, then so is $e_t-\tilde\pi$, and the two are **orthogonal**:

$$
(e_t-\tilde\pi)^2=e_t-\tilde\pi,\qquad \tilde\pi(e_t-\tilde\pi)=0.
$$

*Proof.* $(e_t-\tilde\pi)^2=e_t-2\tilde\pi+\tilde\pi^2=e_t-\tilde\pi$, using $\tilde\pi^2=\tilde\pi$; and $\tilde\pi(e_t-\tilde\pi)=\tilde\pi-\tilde\pi^2=0$.

**Corollary (the complement swaps the two idempotents).** For the two idempotents of the algebra the map $\tilde\pi\mapsto e_t-\tilde\pi$ is the exchange $0\leftrightarrow e_t$, and $0\cdot e_t=0$. The complement is available because $e_t$ is the unit, and it is the reason the two-point class is closed under it.

### Idempotents, the Zero Divisors and the Units

**Proposition (no idempotent is a zero divisor).** No idempotent of the algebra is a zero divisor, and every idempotent is either the origin or a unit.

*Proof.* The idempotents are $0$ and $e_t$. The element $0$ is not a zero divisor by the requirement that a divisor be nonzero, and $e_t$ is the unit and a nonzero element, hence invertible with $e_t^{-1}=e_t$. This is a reading of the division property: an idempotent that is neither $0$ nor a unit would be a non-invertible nonzero element, and there is none.

A non-trivial idempotent would be a zero divisor, since $\tilde\pi(e_t-\tilde\pi)=0$ with both factors nonzero; over $\mathbb{R}$ the statement is vacuous, because there is no non-trivial idempotent and no zero divisor at all. The zero-divisor set is empty (*Zero Divisors of the Quaternion Algebra*), and the idempotent reading of it has nothing to describe. In the complexified block the non-trivial idempotents sit inside the zero-divisor cone as its non-pure family, which is what disappears here.

### The Reading on the Centre and the Vector Subspace

Both idempotents are **central**: $0$ and $e_t$ lie in the centre $\mathbb{R}e_t$. The vector subspace $\mathrm{Vect}(\mathbb{H})$ therefore contains no idempotent but the origin, a nonzero pure element $\vec q$ having square $\vec q^2=-|\vec q|^2e_t$, which equals $\vec q$ only for $\vec q=0$. **Of the two remarkable subspaces over $\mathbb{R}$ the centre carries the two idempotents and the vector subspace carries the origin alone**, the origin belonging to both.

## Summary

The quaternion product is the multiplication of the quaternion algebra, and the roots of $+e_t$ in that product are, by the reduction $\tilde\xi^2=\lambda e_t\Longleftrightarrow\{2\xi_t\vec\xi=0,\ \xi_t^2-|\vec\xi|^2=\lambda\}$, the two central scalars $\pm e_t$ alone: the pure branch needs $|\vec\xi|^2=-1$, which has no real solution, and the scalar branch gives $\xi_t^2=1$. The class is the two-point set, the central part of the level set $\{N=1\}$, and every root of $+e_t$ is a unit with $\tilde\xi^{-1}=\tilde\xi$.

The roots of $-e_t$ are read from the same reduction at $\lambda=-1$: they are the elements of the vector subspace with $N=1$, a quadric of real dimension two. The sign cannot be flipped, the centre $\mathbb{R}e_t$ having no element of square $-e_t$, so the roots of $-e_t$ are not the image of the roots of $+e_t$; the paragraph is a remark, and the roots of $-e_t$ index no idempotent.

The idempotents are the trivial elements $0$ and $e_t$ and nothing else, the equation $\tilde\pi(\tilde\pi-e_t)=0$ and the absence of zero divisors leaving the two; there is no orthogonal family of two nonzero idempotents, no complete orthogonal family but the singleton $\{e_t\}$, no primitive idempotent but $e_t$, and no nontrivial direct sum decomposition of the algebra. The Peirce decomposition is the trivial one, with Peirce spaces $\mathbb{H}$ and $\{0\}$ and no off-diagonal unit. The halving map $\tilde\xi\mapsto\tfrac12(e_t+\tilde\xi)$ is a bijection from the roots of $+e_t$ onto the idempotents, with inverse $\tilde\xi=2\tilde\pi-e_t$, and it carries the pair $\{\tilde\xi,-\tilde\xi\}$ to the complementary pair $\{\tilde\pi,e_t-\tilde\pi\}$; the complement $e_t-\tilde\pi$ exchanges the two idempotents. No idempotent is a zero divisor, and every idempotent is the origin or a unit; both idempotents are central, so the vector subspace carries the origin alone.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | Quaternion algebra, real dimension four |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_k^2=-e_t$, $\vec e_x \vec e_y=\vec e_z$ |
| $\tilde q=q_te_t+\vec q$ | General element, scalar part $q_t$, vector part $\vec q$ |
| $\langle\tilde q\rangle_{\natural}=q_t^2+\lvert\vec q\rvert^2$ | Quaternion norm, positive definite |
| $\mathbb{R}e_t$, $\mathrm{Vect}(\mathbb{H})$ | Centre and vector subspace |
| $\tilde\xi$ | A root of a central value; of $+e_t$ through the body, of $-e_t$ in the closing remark |
| $\tilde\xi=\xi_te_t+\vec\xi$ | Scalar and vector parts of a root |
| $\{+e_t,-e_t\}$ | The two roots of $+e_t$, the central part of $\{N=1\}$ |
| $\tilde\pi$ | An idempotent, $\tilde\pi^2=\tilde\pi$ |
| $\tilde\pi(\tilde\xi)=\tfrac12(e_t+\tilde\xi)$ | The idempotent of the root $\tilde\xi$; $\tilde\xi\mapsto\tilde\pi(\tilde\xi)$ is a bijection |
| $0$, $e_t$ | The two idempotents, orthogonal: $0\cdot e_t=0$ |
| $e_t-\tilde\pi$ | The complementary idempotent |
| $\tilde\pi\mathbb{H}\tilde\pi$ etc. | The four Peirce spaces |

## Further Reading

- [Introduction to the Quaternion Algebra](introduction-to-the-quaternion-algebra.html), for the product, the unit and the square.
- [Unital Algebras](unital-algebras.html), §*Idempotents and the Peirce Decomposition*, for the orthogonal, complete and primitive families and the four Peirce spaces of an associative unital algebra.
- [Norm and Invertibility in the Quaternion Algebra](norm-and-invertibility-in-the-quaternion-algebra.html), for the division property on which the classification rests.
- [Zero Divisors of the Quaternion Algebra](zero-divisors-of-the-quaternion-algebra.html), for the empty zero-divisor set and the two families of the complexified block.
- [Square Roots of Zero and the Nilpotents of the Quaternion Algebra](square-roots-of-zero-and-the-nilpotents-of-the-quaternion-algebra.html), for the roots of $0$, the square-zero class and the off-diagonal Peirce units.
- [Square Roots of a General Element in the Quaternion Algebra](square-roots-of-a-general-element-in-the-quaternion-algebra.html), for the roots of the general quadratic $\tilde\xi^2=\tilde q$, of which the roots of $+e_t$ here are one case.
- [Square Roots of One and the Idempotents of the Biquaternion Algebra](square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html), the complexified counterpart, for the idempotent family, the bijection with the roots of one and the minimal left ideals.
- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the origin of the imaginary units and the roots of $-1$.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the square of a quaternion and its classes of element.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the structure of a Clifford algebra and its idempotents.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for idempotents, the Peirce decomposition and the structure of the regular module.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for idempotents, projections and their lifting in rings.
