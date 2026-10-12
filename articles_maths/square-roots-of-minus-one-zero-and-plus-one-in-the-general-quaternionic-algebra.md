# __Square Roots of Minus One, Zero and Plus One in the General Quaternionic Algebra__

## Introduction

This article classifies the square roots of the three central values $-1$, $0$ and $+1$ in the general quaternionic bilinear product.

The equation $\tilde\Xi\star\tilde\Xi=\lambda e_0$ names a product, and throughout this article the square is the one of the general quaternionic product $\tilde\Xi^{\natural}\tilde Q$; the root is relative to it, and the plain square of the same element is a different object. The whole of the problem is decided by one identity: the square of every element of this product is already the central element $N(\tilde\Xi)e_0$, so the three special values are the three level sets of the algebraic norm,

$$
\tilde\Xi\star\tilde\Xi=-e_0 \iff N(\tilde\Xi)=-1 , \qquad
\tilde\Xi\star\tilde\Xi=0 \iff N(\tilde\Xi)=0 , \qquad
\tilde\Xi\star\tilde\Xi=e_0 \iff N(\tilde\Xi)=1 ,
$$

and each is a nondegenerate complex quadric, of complex dimension three and real dimension six. The article gives the three sets, their dimension, their families and their standard elements, and it reads them against the three sets of the plain product, where the same three values have a different shape because the plain square is scalar only on the vector part.

**Boundaries.** The square, the algebraic norm and the idempotents of the algebra are *Introduction to the General Plain Algebra of Biquaternions*, *Norm and Invertibility in the General Plain Algebra*, *Idempotents of the General Plain Algebra* and *Nilpotents of the General Plain Algebra*; the three special values for the plain product are their own article, *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*, and the plain case is quoted here and not reproved. The four root problems of the four general products side by side, and the criterion by which a root of a non-zero value is a unit, are *Square Roots of a General Element*; this article owns the block reading of the three values and the families inside them. The algebraic norm and the one-sided theory are *Norm and Invertibility in the General Quaternionic Algebra*, and the zero divisors, which are the roots of $0$, are *Zero Divisors of the General Quaternionic Algebra*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$, with $e_1e_2=e_3$ and central scalar imaginary $i$, $i^2=-1$. Juxtaposition is the plain product and $\star$ the general quaternionic bilinear product $\tilde\Xi\star\tilde Q=\tilde\Xi^{\natural}\tilde Q$, with $\natural$ the natural conjugation $\tilde Q^{\natural}=Q_0-\mathbf Q$. An element is $\tilde\Xi=\Xi_0e_0+\mathbf\Xi$ with $\mathbf\Xi=\sum_{k=1}^{3}\Xi_ke_k$, the **algebraic norm** is $N(\tilde\Xi)=\sum_\mu \Xi_\mu^2=\Xi_0^2+(\mathbf\Xi,\mathbf\Xi)$, and $(\mathbf\Xi,\mathbf\Xi)=\sum_k\Xi_k^2$ is the complex bilinear form of the vector part. A **central value** is an element $\lambda e_0$ with $\lambda\in\mathbb{C}$, and $\hat\mu$ denotes a real unit vector of $\mathbb{R}^3$.

## The Problem and Its Reduction

**Definition.** Let $\lambda\in\mathbb{C}$. A **square root of the central value $\lambda$** in the general quaternionic product is an element $\tilde\Xi$ with

$$
\tilde\Xi\star\tilde\Xi=\lambda e_0 .
$$

The root is relative to the product, and this article uses the one of $\star$ throughout; the general definition of the square and of the roots of a central value is *Definitions for the Study of the 12 Algebraic Structures*, §*Powers, the Square and the Roots*.

**Theorem (the reduction).** For every $\tilde\Xi\in\mathbb{B}$,

$$
\tilde\Xi\star\tilde\Xi=\lambda e_0 \iff N(\tilde\Xi)=\lambda .
$$

**Proof.** The square is $N(\tilde\Xi)e_0$ by §*The Square Lies in the Scalar Line* of *Introduction to the General Quaternionic Algebra of Biquaternions*, and $e_0\neq0$.

The reduction is a single complex equation in the four complex coordinates, and it holds for every $\lambda$ at once. It has no case split and no vanishing condition: the plain product reduces the same problem to the pair $\Xi_0^2-(\mathbf\Xi,\mathbf\Xi)=\lambda$, $2\Xi_0\mathbf\Xi=0$, whose second equation forces $\Xi_0=0$ or $\mathbf\Xi=0$ and produces the central pair and the vector family (*Square Roots of a General Element in the General Plain Algebra*); the quaternionic square is central for every element, so the second equation does not arise and the root set is the quadric itself.

**Corollary (the three special values).** The roots of $-1$, of $0$ and of $+1$ are the level sets of the algebraic norm,

$$
\{\tilde\Xi:N(\tilde\Xi)=-1\} , \qquad \{\tilde\Xi:N(\tilde\Xi)=0\} , \qquad \{\tilde\Xi:N(\tilde\Xi)=1\} .
$$

## The Roots of Minus One

### Statement

**Theorem.** The roots of $-1$ in the general quaternionic product are the solutions of

$$
N(\tilde\Xi)=\Xi_0^2+(\mathbf\Xi,\mathbf\Xi)=-1 .
$$

The set is a nondegenerate complex quadric of complex dimension three, hence of real dimension six. It contains the two central roots $\pm i$ and the elements $i\hat\mu$ over the real unit vectors; writing $\Xi_\mu=\xi_\mu+i\xi'_\mu$ with $\xi_\mu,\xi'_\mu$ real, its two real equations are

$$
\sum_{\mu=0}^{3}\bigl(\xi_\mu^2-\xi'^2_\mu\bigr)=-1 , \qquad \sum_{\mu=0}^{3}\xi_\mu \xi'_\mu=0 ,
$$

a family of real dimension six.

**Proof.** The criterion is the reduction. With $\Xi_\mu=\xi_\mu+i\xi'_\mu$ the equation $N=\sum_\mu(\xi_\mu^2-\xi'^2_\mu)+2i\sum_\mu \xi_\mu \xi'_\mu=-1$ is the pair of real equations displayed, which is two independent real equations on eight real coordinates; the gradient of $N$ does not vanish on the level set, so the quadric is nondegenerate off the origin and has real dimension $8-2=6$. The elements $\pm i$ have $N=(\pm i)^2=-1$; and for a real unit vector $\hat\mu$ the element $i\hat\mu$ has $(\mathbf\Xi,\mathbf\Xi)=(i\hat\mu,i\hat\mu)=-\sum_k\hat\mu_k^2=-1$ and $\Xi_0=0$, so it satisfies the equation.

### The Families

The roots of $-1$ split into three entries according to the vector part, and the split is the one of the plain classification with the two real directions exchanged.

- **The central roots $\pm i$.** These have $\mathbf\Xi=0$ and $\Xi_0=\pm i$, and $\Xi_0^2=-1$. They are the two elements of the root set in the centre $\mathbb{C}_{\mathbb{B}}$.
- **The imaginary vector roots.** These have $\Xi_0=0$ and $\mathbf\Xi$ a pure complex vector with $(\mathbf\Xi,\mathbf\Xi)=-1$. The real solutions are the elements $i\hat\mu$ over the real unit vectors, a quadric of real dimension two in the vector subspace with signature $(3,3)$; the complex solutions form a family of real dimension four, the solutions of $\sum_k\xi_k^2-\sum_k\xi'^2_k=-1$ with $\sum_k\xi_k\xi'_k=0$.
- **The mixed roots.** These have both $\Xi_0$ and the vector part nonzero, and they fill the rest of the quadric.

The contrast with the plain product is a change of sign in the vector direction. The plain square of a pure element is $-(\mathbf\Xi,\mathbf\Xi)e_0$, so there the real unit vectors are roots of $-1$ and the imaginary ones of $+1$; here the sign is removed by the conjugation in the first slot, so the **real** unit vectors are roots of $+1$ and the **imaginary** ones, $i\hat\mu$, are roots of $-1$. The central roots $\pm i$ are common to the two products, the scalar line being fixed by the conjugation.

### Verification

The two central roots and the imaginary vector roots are read from the algebraic norm directly. For the mixed family the equations above are the general pair, and the elements whose vector part has real and imaginary parts $\boldsymbol{\xi},\boldsymbol{\xi}'$ with $|\boldsymbol{\xi}|=r$, $|\boldsymbol{\xi}'|=s$ and $\boldsymbol{\xi}\perp\boldsymbol{\xi}'$ have $N=\xi_0^2+r^2-s^2$ when $\Xi_0=\xi_0$ is real; the value $-1$ is reached for every real $\xi_0$ by choosing $r,s$ with $s^2-r^2=1+\xi_0^2$, so the mixed family is non-empty over every real scalar. The parametrics confirm the real dimension six.

## The Roots of Zero

**Theorem.** The roots of $0$ in the general quaternionic product are the elements of the **zero-divisor cone**,

$$
\{\tilde\Xi:\tilde\Xi\star\tilde\Xi=0\}=\{\tilde\Xi:N(\tilde\Xi)=0\}=C ,
$$

a real cone of real dimension six. It consists of the origin, the **pure** isotropic elements $\boldsymbol\rho+i\boldsymbol\rho'$ with $\boldsymbol\rho\perp\boldsymbol\rho'$ and $|\boldsymbol\rho|=|\boldsymbol\rho'|$, and the **non-pure** elements $\tilde\Xi=2\Xi_0\tilde\Pi$ over the nontrivial idempotents $\tilde\Pi$ of the plain product.

**Proof.** The criterion is the reduction. The shape and the two families are *Zero Divisors of the General Quaternionic Algebra*, §*The Zero Divisor Set* and §*The Two Families of Zero Divisors*.

The root set of $0$ is the whole nilpotent cone of the product, the largest of the four general products, and it contains the root set of $0$ of the plain product, which is the pure isotropic cone of real dimension four (*Nilpotents of the General Plain Algebra*). The two standard roots are $e_1+ie_2$, which is pure, and $e_0+ie_1$, which is not; the second is twice the Hermitian idempotent, whose plain square is itself.

## The Roots of Plus One

**Theorem.** The roots of $+1$ in the general quaternionic product are the solutions of

$$
N(\tilde\Xi)=\Xi_0^2+(\mathbf\Xi,\mathbf\Xi)=1 .
$$

The set is a nondegenerate complex quadric of complex dimension three, hence of real dimension six. It contains the two central roots $\pm e_0$ and the elements $\hat\mu$ over the real unit vectors, and its families are the mirror of the roots of $-1$ under multiplication by $i$.

**Proof.** The criterion is the reduction, and the quadric is nondegenerate by the same argument as for $-1$. The elements $\pm e_0$ have $N=1$; a real unit vector $\hat\mu$ has $(\mathbf\Xi,\mathbf\Xi)=\sum_k\hat\mu_k^2=1$ and $\Xi_0=0$. Multiplication by $i$ acts as $\tilde\Xi\mapsto i\tilde\Xi$ and multiplies the algebraic norm by $i^2=-1$, so it is a bijection of the roots of $-1$ onto the roots of $+1$ and accounts for the displayed families.

**Corollary.** The roots of $+1$ are exactly the products $i\tilde\Xi$ of the roots of $-1$ with $i$, and the roots of $-1$ are exactly the products $i\tilde\Xi$ of the roots of $+1$ with $i$. The two sets are the two halves of the level set $N=\pm1$ under the complex structure.

## The Three Sets Compared

The three special values are the three sign choices of the algebraic norm, and their three sets are read side by side with the plain product's three sets.

| value | the general quaternionic product | the general plain product |
|---|---|---|
| $-1$ | $N=-1$, one quadric of real dimension $6$; contains $\pm i$ and the imaginary vector roots $i\hat\mu$ | the central pair $\pm i$, the real vector roots $\hat\mu$, and a four-parameter family |
| $0$ | $N=0$, the whole zero-divisor cone of real dimension $6$ | the pure isotropic cone of real dimension $4$, together with $0$ |
| $+1$ | $N=1$, one quadric of real dimension $6$; contains $\pm e_0$ and the real vector roots $\hat\mu$ | the products $i\tilde\Xi$ of the roots of $-1$ with $i$ |

The quaternionic column is this article. The plain column is quoted from *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*, and the case-by-case comparison of the four general products, with the criterion by which the roots of a non-zero value are units, is *Square Roots of a General Element*.

Two structural differences are worth naming. The plain root sets are stratified by the vanishing of the scalar part, because the plain square is scalar only on the vector part; the quaternionic root sets are single quadrics, because the quaternionic square is always scalar. And the plain roots of $-1$ carry the idempotents and the plain roots of $0$ carry only the nilpotents, whereas here the roots of $-1$ are a quadric with no element of the algebra attached, the idempotents of the product being the trivial ones alone, and the roots of $0$ carry the whole zero-divisor set, nilpotents and idempotent multiples together.

## The Relation to the Idempotents

The plain classification of the idempotents is a bijection from the plain roots of $-1$ to the idempotents, $\xi\mapsto\tfrac12(e_0+\xi i)$ (*Idempotents of the General Plain Algebra*). In the general quaternionic product that bijection has no analogue: the idempotents of the product are $0$ and $e_0$ alone, and they are the roots of $0$ and of $+1$ respectively, not of $-1$.

Two statements record what happens instead. First, the **roots of $-1$ are not the idempotent parameters**: the idempotent equation of the product is $\tilde Q\star\tilde Q=\tilde Q$, which forces $\tilde Q$ to be central, hence $0$ or $e_0$, and neither is a root of $-1$. Second, the **plain idempotents are roots of $0$ of the product**: for a nontrivial plain idempotent $\tilde\Pi=\tfrac12(e_0+\xi i)$,

$$
\tilde\Pi\star\tilde\Pi=N(\tilde\Pi)e_0=0 ,
$$

because a nontrivial idempotent is a zero divisor of the plain product and has vanishing algebraic norm; so the bijection of the plain product sends the plain roots of $-1$ to the **roots of $0$** of this product, and not to its roots of $-1$. The displacement is the subject of *Idempotents of the General Quaternionic Algebra*.

## The Relation to the Zero Divisors

The roots of $0$ are the zero divisors together with the origin: for a nonzero $\tilde\Xi$, $\tilde\Xi\star\tilde\Xi=0$ is exactly the condition $N(\tilde\Xi)=0$, which is the criterion for $\tilde\Xi$ to be a zero divisor of the product (*Zero Divisors of the General Quaternionic Algebra*). The roots of $-1$ and of $+1$ have non-vanishing algebraic norm $N=\pm1$, so they are units of the plain product, and they are never zero divisors; in particular the equations $\tilde\Xi\star\tilde X=e_0$ and $\tilde X\star\tilde\Xi=e_0$ are soluble for them and insoluble for the roots of $0$ (*Norm and Invertibility in the General Quaternionic Algebra*). Across the four general products the same statement holds once a root exists: a root of a non-zero central value is a unit and a non-zero root of $0$ is a zero divisor (*Square Roots of a General Element*).

## Summary

In the general quaternionic bilinear product $\tilde\Xi\star\tilde Q=\tilde\Xi^{\natural}\tilde Q$ the square is always central, $\tilde\Xi\star\tilde\Xi=N(\tilde\Xi)e_0$, so the roots of the three special values are the three level sets of the algebraic norm and each is a nondegenerate complex quadric of real dimension six. The roots of $-1$ are the solutions of $N=-1$; they contain the central pair $\pm i$, the imaginary vector roots $i\hat\mu$ over the real unit vectors, and a mixed family, and their real and imaginary vector directions are the ones the plain product assigns to the opposite value. The roots of $0$ are the whole zero-divisor cone, of real dimension six, the union of the pure isotropic elements and the complex multiples of the nontrivial plain idempotents. The roots of $+1$ are the solutions of $N=1$; they contain the central pair $\pm e_0$ and the real vector roots $\hat\mu$, and they are the image of the roots of $-1$ under multiplication by $i$. The plain bijection from the roots of $-1$ to the idempotents has no analogue here: the idempotents of the product are $0$ and $e_0$ alone, and the plain idempotents are roots of $0$ of the product. The roots of $\pm1$ are units of the algebra, and the roots of $0$ are its zero divisors.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde\Xi\star\tilde Q=\tilde\Xi^{\natural}\tilde Q$ | the general quaternionic bilinear product |
| $N(\tilde\Xi)=\sum_\mu \Xi_\mu^2=\Xi_0^2+(\mathbf\Xi,\mathbf\Xi)$ | the algebraic norm |
| $\lambda e_0$ | a central value |
| $N(\tilde\Xi)=\lambda$ | the reduced form of the root equation |
| $\pm i$ | the central roots of $-1$ |
| $i\hat\mu$ | the imaginary vector roots of $-1$ over the real unit vectors $\hat\mu$ |
| $\hat\mu$ | the real vector roots of $+1$ |
| $C=\{N=0\}$ | the zero-divisor cone, the roots of $0$ |
| $\tilde\Pi(\hat\mu)=\tfrac12(e_0+i\hat\mu)$ | the Hermitian idempotent, a root of $0$ of the product |

## Further Reading

- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the square roots of a central value in an algebra with a quadratic form.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the isotropic vectors and the quadratic form $\sum_\mu Q_\mu^2$ of the complex quaternion algebra.
- *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-general-plain-algebra.md`), for the same three values in the plain product, with their stratification by the scalar part.
- *Square Roots of a General Element* (`articles_maths/square-roots-of-a-general-element.md`), for the four root problems side by side and the criterion by which a root of a non-zero value is a unit.
- *Norm and Invertibility in the General Quaternionic Algebra* (`articles_maths/norm-and-invertibility-in-the-general-quaternionic-algebra.md`), for the algebraic norm, the multiplicativity and the one-sided equations.
- *Zero Divisors of the General Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-general-quaternionic-algebra.md`), for the cone, its two families and the annihilators.
- *Idempotents of the General Quaternionic Algebra* (`articles_maths/idempotents-of-the-general-quaternionic-algebra.md`), for the idempotents $0$ and $e_0$ and the displacement of the plain idempotents into the roots of $0$.
