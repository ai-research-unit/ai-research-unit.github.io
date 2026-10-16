# __Square Roots of a General Element in the General Quaternionic Algebra__

## Introduction

This article solves the square-root equation $\tilde\Xi\star\tilde\Xi=\tilde Q$ in the general quaternionic bilinear product for an arbitrary element $\tilde Q$ of the biquaternion algebra, and it states the absence that the equation forces.

The equation names a product, and throughout this article the square is the one of the general quaternionic product; the plain square of the same element is a different equation, and its solution is *Square Roots of a General Element in the Biquaternion Algebra*. The quaternionic square is the central element $\langle\tilde\Xi\rangle_{\natural}e_0$ for every $\tilde\Xi$, so the equation can be solved only when the right-hand side is a central value, and this is the first statement of the article: **an element which is not a central value has no square root in this product**, and the absence is stated and not filled. For a central radicand $\tilde Q=\lambda e_0$ the equation reduces to the single complex equation $\langle\tilde\Xi\rangle_{\natural}=\lambda$, and the root set is a nondegenerate complex quadric, of complex dimension three when $\lambda\neq0$ and the zero-divisor cone when $\lambda=0$. Every central value has roots, and the root set of $\lambda$ is a scaled copy of the root set of $1$ or of $-1$.

**The results.** The quaternionic square is always central, $\tilde\Xi\star\tilde\Xi=\langle\tilde\Xi\rangle_{\natural}e_0$, so the equation $\tilde\Xi\star\tilde\Xi=\tilde Q$ has a solution if and only if $\tilde Q$ is a central value: **an element with nonzero vector part has no square root** in this product. For a central radicand $\tilde Q=\lambda e_0$ the root set is $R(\lambda)=\{\tilde\Xi:\langle\tilde\Xi\rangle_{\natural}=\lambda\}$, which is a nondegenerate complex quadric of complex dimension $3$ and real dimension $6$ when $\lambda\neq0$, and the zero-divisor cone of real dimension $6$ when $\lambda=0$, and it is never empty. The sets are not new: $R(\lambda)=\alpha R(1)=(i\alpha)R(-1)$ for $\alpha^2=\lambda\neq0$, so the three central values generate every value, and a root of a nonzero value is a unit of the algebra while a nonzero root of $0$ is a zero divisor. Each section below states its result first and then proves it.

**Boundaries.** The plain square-root problem, its vector–scalar reduction and its two branches are *Square Roots of a General Element in the Biquaternion Algebra*; the roots of $+1$ and of $-1$ in the plain product with its idempotents are *Square Roots of One and the Idempotents of the Biquaternion Algebra*, and the roots of $0$ with its nilpotents are *Square Roots of Zero and the Nilpotents of the Biquaternion Algebra*. The four central-value problems of the four general products side by side are *Square Roots of a General Element in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*, which owns the comparison; this article owns the block reading and the existence criterion for an arbitrary radicand. The algebraic norm is *Norm and Invertibility in the General Quaternionic Algebra*, the cone and the zero divisors are *Zero Divisors of the General Quaternionic Algebra*, the roots of $+1$ and of $-1$ with the idempotents of the product are *Square Roots of One and the Idempotents of the General Quaternionic Algebra*, and the roots of $0$ with the nilpotents are *Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$, with $e_1e_2=e_3$ and central scalar imaginary $i$, $i^2=-1$. Juxtaposition is the plain product and $\star$ the general quaternionic bilinear product $\tilde\Xi\star\tilde Q=\tilde\Xi^{\natural}\tilde Q$, with $\natural$ the natural conjugation $\tilde Q^{\natural}=Q_0-\vec Q$. An element is $\tilde\Xi=\Xi_0e_0+\vec\Xi$ with $\vec\Xi=\sum_{k=1}^{3}\Xi_ke_k$, the **algebraic norm** is $\langle\tilde\Xi\rangle_{\natural}=\sum_\mu \Xi_\mu^2=\Xi_0^2+(\vec\Xi,\vec\Xi)$, and a **central value** is an element $\lambda e_0$ with $\lambda\in\mathbb{C}$; the scalar line $\mathbb{C}e_0$ is denoted $\mathbb{C}_{\mathbb{B}}$.

## The Reduction

**Definition.** Let $\tilde Q\in\mathbb{B}$. A **square root of $\tilde Q$** in the general quaternionic product is an element $\tilde\Xi$ with

$$
\tilde\Xi\star\tilde\Xi=\tilde Q .
$$

The root is relative to the product, and this article uses the one of $\star$ throughout; the general definition of the square and of the roots of an element is *Definitions for the Study of the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*, §*Powers, the Square and the Roots*.

**Theorem (the square is central).** For every $\tilde\Xi\in\mathbb{B}$ the square $\tilde\Xi\star\tilde\Xi$ lies in the scalar line $\mathbb{C}_{\mathbb{B}}$, and

$$
\tilde\Xi\star\tilde\Xi=\langle\tilde\Xi\rangle_{\natural}e_0 .
$$

**Proof.** The scalar–vector form of the product gives $\tilde\Xi^{\natural}\tilde\Xi=(\Xi_0-\vec\Xi)(\Xi_0+\vec\Xi)=\Xi_0^2-\vec\Xi^2=\bigl(\Xi_0^2+(\vec\Xi,\vec\Xi)\bigr)e_0$; the statement is §*The Square Lies in the Scalar Line* of *Introduction to the General Quaternionic Algebra*.

**Theorem (the existence criterion).** The equation $\tilde\Xi\star\tilde\Xi=\tilde Q$ has a solution if and only if $\tilde Q$ is a central value. For $\tilde Q=\lambda e_0$ the equation is equivalent to the single complex equation

$$
\langle\tilde\Xi\rangle_{\natural}=\lambda .
$$

**Proof.** A square is central by the preceding theorem, so a solution forces $\tilde Q\in\mathbb{C}_{\mathbb{B}}$; conversely if $\tilde Q=\lambda e_0$ the equation reads $\langle\tilde\Xi\rangle_{\natural}e_0=\lambda e_0$, which is $\langle\tilde\Xi\rangle_{\natural}=\lambda$ because $e_0\neq0$.

**Absence (the non-central radicands).** An element of $\mathbb{B}$ whose vector part is nonzero **has no square root** in the general quaternionic product. The witness $e_1$ shows it: a root would satisfy $\langle\tilde\Xi\rangle_{\natural}e_0=e_1$, and the two sides differ in the coefficient of $e_1$. This is not a deficiency of a particular element but of the product, whose squaring map has image the scalar line; the plain product has a wider image, and its squaring map reaches every element, which is why the plain problem has a solution for an arbitrary radicand.

## The Roots of a Central Value

**For a central radicand $\tilde Q=\lambda e_0$ the root set is $R(\lambda)=\{\tilde\Xi:\langle\tilde\Xi\rangle_{\natural}=\lambda\}$: a nondegenerate complex quadric of real dimension six when $\lambda\neq0$, the zero-divisor cone of real dimension six when $\lambda=0$, and never empty.**

**Theorem (the root set of a central value).** Let $\lambda\in\mathbb{C}$ and let $\tilde Q=\lambda e_0$. The root set of $\tilde Q$ is

$$
R(\lambda)=\{\tilde\Xi\in\mathbb{B}:\langle\tilde\Xi\rangle_{\natural}=\lambda\} .
$$

- If $\lambda\neq0$, $R(\lambda)$ is a nondegenerate complex quadric of complex dimension three and real dimension six.
- If $\lambda=0$, $R(0)$ is the zero-divisor cone, a real cone of real dimension six.
- The set is never empty: the element $\tilde\Xi=\sqrt\lambda\,e_0$ is a root, where $\sqrt\lambda$ is either square root of $\lambda$ in $\mathbb{C}$.

**Proof.** The identification with the level set is the reduction. With $\Xi_\mu=p_\mu+ip'_\mu$, the equation $N=\sum_\mu(p_\mu^2-(p'_\mu)^2)+2i\sum_\mu p_\mu p'_\mu=\lambda$ is a pair of real equations, the gradient of $N$ does not vanish off the origin, and the level set has real dimension $8-2=6$ in the two cases; for $\lambda=0$ it is a cone because $\langle\cdot\rangle_{\natural}$ is homogeneous. The displayed central element has $\langle \sqrt\lambda\,e_0\rangle_{\natural}=(\sqrt\lambda)^2=\lambda$.

**Corollary (the central roots).** The root set of every central value contains the two central roots $\pm\sqrt\lambda\,e_0$, and they coincide exactly when $\lambda=0$; for $\lambda\neq0$ the two are distinct and lie in the scalar line $\mathbb{C}_{\mathbb{B}}$.

## The Scaling of the Root Set

**For $\lambda\neq0$ and $\alpha^2=\lambda$ the root set of $\lambda$ is the scaled root set of $1$ and equally of $-1$, $R(\lambda)=\alpha R(1)=(i\alpha)R(-1)$.**

**Theorem.** Let $\lambda\neq0$ and let $\alpha\in\mathbb{C}$ satisfy $\alpha^2=\lambda$. Then multiplication by $\alpha$ is a bijection of the roots of $1$ onto the roots of $\lambda$, and multiplication by $i\alpha$ is a bijection of the roots of $-1$ onto the roots of $\lambda$:

$$
R(\lambda)=\alpha\,R(1)=(i\alpha)\,R(-1) .
$$

**Proof.** The algebraic norm is homogeneous of degree two and $\mathbb{C}$-linear in the scaling, $\langle\alpha\tilde E\rangle_{\natural}=\alpha^2\langle\tilde E\rangle_{\natural}$, so $\alpha$ carries the level set $N=1$ onto the level set $N=\alpha^2=\lambda$; the scaling is a bijection of $\mathbb{B}$ because $\alpha\neq0$. For the second display, $(i\alpha)^2=-\alpha^2=-\lambda$, so $i\alpha$ carries the level set $N=-1$ onto the level set $N=(-1)(-\lambda)=\lambda$.

The root set of a general central value is therefore not a new object: it is the root set of $1$, or equivalently that of $-1$, scaled by a square root of the value. The three special values of *Square Roots of One and the Idempotents of the General Quaternionic Algebra* and *Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra* generate every other central value, and the cone is the remaining case.

## The Classification

**Every element falls into exactly one row: a non-central radicand has an empty root set, a nonzero central value has the quadric $N=\lambda$ of real dimension six, and the central value $0$ has the zero-divisor cone of real dimension six.**

| radicand $\tilde Q$ | condition | root set |
|---|---|---|
| $\tilde Q\notin\mathbb{C}_{\mathbb{B}}$ | $\tilde Q$ not central | empty; the absence of §*The Reduction* |
| $\tilde Q=\lambda e_0$, $\lambda\neq0$ | a non-zero central value | the nondegenerate quadric $N=\lambda$, real dimension six, the scaled root set of $1$ |
| $\tilde Q=0$ | the central value $0$ | the zero-divisor cone $N=0$, real dimension six |

The classification covers every element; the two non-empty rows differ in whether the level set is a nondegenerate quadric or a cone, and they agree in real dimension. The plain product's classification is a different shape: there the root set is the central pair $\pm\sqrt\lambda\,e_0$ together with the quadric cut on the vector subspace, the two pieces distinguished by the branch of the vector–scalar reduction (*Square Roots of a General Element in the Biquaternion Algebra*).

## The Three Central Values

**The values $-1$, $0$ and $+1$ are the seeds of the classification: $R(-1)$ is the quadric $N=-1$, $R(+1)$ the quadric $N=1$, and $R(0)$ the zero-divisor cone, and every other central value is a scaling of the first or the third.**

The values $\lambda=-1$, $0$ and $+1$ are the subject of the companion articles *Square Roots of One and the Idempotents of the General Quaternionic Algebra* and *Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra*, and they are the seeds of the classification:

- $R(-1)=\{N=-1\}$, a quadric of real dimension six containing the central roots $\pm i$ and the imaginary vector roots $\tilde\Xi$ over the real unit vectors $\vec u$;
- $R(0)=\{N=0\}=C$, the zero-divisor cone, containing the origin, the pure isotropic elements and the complex multiples of the nontrivial plain idempotents;
- $R(+1)=\{N=1\}$, a quadric of real dimension six containing the central roots $\pm e_0$ and the real vector roots $\vec u$.

By the scaling theorem, $R(\lambda)$ for a general value is the image of one of the first and the third under multiplication by a square root of $\lambda$, and the second is the cone, which is fixed by every non-zero scaling.

## Worked Examples

- **Roots of $1$.** The central roots are $\pm e_0$. The element $e_1$ is a root, since $\langle e_1\rangle_{\natural}=1$; more generally every real unit vector $\vec u$ is a root, and the elements $i\vec q$ with $(\vec q,\vec q)=-1$ are roots as well. The element $e_0+e_1$ is not a root, since $\langle e_0+e_1\rangle_{\natural}=1+1=2$.
- **Roots of $-1$.** The central roots are $\pm i$, and the elements $\tilde\Xi$ over the real unit vectors are roots. The element $e_1$ is not a root of $-1$; it is a root of $+1$. This is the sign that the quaternionic product removes from the pure square.
- **Roots of $0$.** The origin, the pure isotropic element $e_1+ie_2$, and the non-pure element $e_0+ie_1$ are roots; the first is the trivial one, the second is a nilpotent of the plain product, and the third is twice a Hermitian idempotent. The root set is the whole cone, and its members are the zero divisors of the algebra.
- **Roots of a complex value.** For $\lambda=4$ the element $2e_0$ is a root, and so is $2e_1$; for $\lambda=i$ the element $\alpha e_0$ with $\alpha^2=i$, for instance $\alpha=(1+i)/\sqrt2$, is a root, and the whole root set is the image of $R(1)$ under multiplication by $\alpha$.
- **A non-central radicand.** The element $e_1$ has no root: its square-root equation would force the central element $\langle\tilde\Xi\rangle_{\natural}e_0$ to equal $e_1$. The statement is the absence of §*The Reduction*, and it is the sharpest difference from the plain product, where $e_1$ has the four roots $\pm\tfrac{1}{\sqrt2}(e_0+e_1)$ and $\pm\tfrac{i}{\sqrt2}(e_0-e_1)$ (*Square Roots of a General Element in the Biquaternion Algebra*).

## The Roots Which Are Units, and the Roots Which Are Zero Divisors

**A root of a nonzero central value has $N\neq0$ and is a unit of the plain product satisfying the two one-sided equations of $\star$, while a nonzero root of $0$ has $N=0$ and is a zero divisor with neither equation soluble.**

The algebraic norm decides the nature of every root, and it decides it the same way as in the other products. A root of a non-zero central value has $\langle\tilde\Xi\rangle_{\natural}=\lambda\neq0$, so it is a unit of the plain product and satisfies the two one-sided equations of $\star$; a non-zero root of $0$ has $\langle\tilde\Xi\rangle_{\natural}=0$, so it is a zero divisor of the algebra, and neither one-sided equation is soluble for it (*Norm and Invertibility in the General Quaternionic Algebra*). The statement is the block reading of the general theorem of *Square Roots of a General Element in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*, §*The Roots Are Units, or Zero Divisors*. In particular the roots of $-1$ and of $+1$ are never zero divisors, and the roots of $0$ other than the origin are always zero divisors; the origin is neither.

## Summary

The square-root equation $\tilde\Xi\star\tilde\Xi=\tilde Q$ of the general quaternionic product has a solution exactly when $\tilde Q$ is a central value; an element with non-zero vector part has no root, because the quaternionic square is always central. For a central radicand the equation reduces to the single complex equation $\langle\tilde\Xi\rangle_{\natural}=\lambda$, the square of the equation being the algebraic norm, and the root set is the nondegenerate complex quadric $N=\lambda$ of real dimension six when $\lambda\neq0$, and the zero-divisor cone of real dimension six when $\lambda=0$. Every central value has roots, among them the central root $\sqrt\lambda\,e_0$, and the root set of $\lambda$ is the root set of $1$, or of $-1$, scaled by a square root of the value. The three special values generate the classification: $R(-1)$ contains the imaginary vector roots $\tilde\Xi$, $R(+1)$ the real vector roots $\vec u$, and $R(0)$ the whole nilpotent cone of the product. The roots of a non-zero value are units of the algebra, the non-zero roots of $0$ are its zero divisors, and the absence of a root for a non-central radicand is stated and not filled.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde\Xi\star\tilde Q=\tilde\Xi^{\natural}\tilde Q$ | the general quaternionic bilinear product |
| $\langle\tilde\Xi\rangle_{\natural}=\sum_\mu \Xi_\mu^2=\Xi_0^2+(\vec\Xi,\vec\Xi)$ | the algebraic norm |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ | the scalar line, the set of the central values |
| $\lambda e_0$ | a central value, $\lambda=\lambda_1+i\lambda_2$ |
| $\tilde\Xi\star\tilde\Xi=\langle\tilde\Xi\rangle_{\natural}e_0$ | the central square |
| $R(\lambda)=\{N=\lambda\}$ | the root set of the central value $\lambda$ |
| $C=R(0)$ | the zero-divisor cone |
| $\alpha$, $\sqrt\lambda$ | the square roots of the value, with $\alpha^2=\lambda$ |
| $R(\lambda)=\alpha R(1)=(i\alpha)R(-1)$ | the scaling of the root set |

## Further Reading

- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the square roots of an element in an algebra with a multiplicative quadratic form.
- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the squaring map of a non-associative algebra and its image.
- *Square Roots of a General Element in the Biquaternion Algebra* (`articles_maths/square-roots-of-a-general-element-in-the-biquaternion-algebra.md`), for the plain problem, its vector–scalar reduction and its two branches.
- *Square Roots of One and the Idempotents of the General Quaternionic Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-general-quaternionic-algebra.md`), for the roots of $+1$ and of $-1$, the idempotents and the displaced plain idempotents.
- *Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-general-quaternionic-algebra.md`), for the roots of $0$ and the nilpotent cone.
- *Square Roots of a General Element in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/square-roots-of-a-general-element-in-the-algebraic-structures-over-the-biquaternioid-c-space.md`), for the four root problems side by side.
- *Norm and Invertibility in the General Quaternionic Algebra* (`articles_maths/norm-and-invertibility-in-the-general-quaternionic-algebra.md`), for the algebraic norm, the one-sided equations and the set $\mathbb{B}^{\times}$.
- *Zero Divisors of the General Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-general-quaternionic-algebra.md`), for the cone and its two families.
