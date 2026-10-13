# __Square Roots of Minus One, Zero and Plus One in the General Quaternionic Sesqualgebra__

## Introduction

The three central values the biquaternion algebra singles out are $-1$, $+1$ and $0$, and a **root** of the value $\lambda$ in a product $\star$ is a nonzero element with $\tilde\Xi\star\tilde\Xi = \lambda e_0$, the definition being *Definitions for the Study of the 12 Algebraic Structures* §6. This article gives the roots of $-1$, $0$ and $+1$ in the **general quaternionic sesquilinear product**

$$
\tilde\Xi \star \tilde Q = \tilde\Xi^{\natural}\tilde Q^{*}
$$

of *Introduction to the General Quaternionic Sesqualgebra of Biquaternions*. The value $0$ returns the nilpotents of the block, which are classified in *Nilpotents of the General Quaternionic Sesqualgebra*; the value $-1$ gives the imaginary units and the value $+1$ the involutions, and the three are treated together because one computation produces all three, the central square.

The point of the article is that the three classes are **disjoint readings of one family**. The root set of $\lambda$ is empty unless $\lambda$ is real, and for real $\lambda$ it is the family $\tilde\Xi = c(\hat\mu+it)$, one complex scalar, one real direction and one real slope $t$, tied by the single equation $(t^2-1)\lvert c\rvert^2 = \lambda$, together with the central circle of the pure scalar roots when $\lambda>0$. The value $-1$ selects the slopes with $t^2<1$, the value $+1$ the slopes with $t^2>1$ and the central circle, and the value $0$ the two slopes $t = \pm1$. The comparison with the plain algebra, where the roots of $+1$ are the idempotent parameters $\tfrac12(e_0+\xi)$, is drawn at §*The Three Values and the Plain Product*.

**Conventions.** $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0 = 1, e_1, e_2, e_3$ with $e_1e_2 = e_3$ and central scalar imaginary $i$. An element is $\tilde Q = Q_0e_0+\mathbf Q$. The natural conjugation is $\tilde Q^{\natural} = Q_0-\mathbf Q$, the star is $\tilde Q^{*} = \overline{\tilde Q^{\natural}}$, and $\overline{\tilde Q} = \tilde Q^{\natural*} = \tilde Q^{*\natural}$. The **central square** is $C(\tilde Q) = \sum_\mu Q_\mu^2$, with $C(\tilde Q)e_0 = \tilde Q\tilde Q^{\natural}$. The **scalar part** and the **vector part** of $\tilde Q$ are $Q_0$ and $\mathbf Q$. The product is $\tilde\Xi\star\tilde Q = \tilde\Xi^{\natural}\tilde Q^{*}$, with the natural conjugation ${}^{\natural}$ in the first slot and the star ${}^{*}$ in the second; juxtaposition is the general plain bilinear product. A **root of $\lambda$** is a nonzero $\tilde\Xi$ with $\tilde\Xi\star\tilde\Xi = \lambda e_0$.

## The Reduction of the Root Equation

**Proposition (the central square of a root).** For every $\tilde\Xi$,

$$
\tilde\Xi\star\tilde\Xi = \bigl(\overline{\tilde\Xi}\,\tilde\Xi\bigr)^{\natural} ,
$$

so $\tilde\Xi$ is a root of $\lambda$ if and only if $\overline{\tilde\Xi}\tilde\Xi = \lambda e_0$; in particular the equation $\tilde\Xi\star\tilde\Xi = \lambda e_0$ forces $\lambda\in\mathbb{R}$.

**Proof.** The identity is the one of *The Square of the General Quaternionic Sesquilinear Product and the Two Halves*, proved on the coordinates. Its scalar part is the **Krein form** $\mathrm{Sc}(\overline{\tilde\Xi}\tilde\Xi) = \sum_\mu \varepsilon_\mu\lvert \Xi_\mu\rvert^2$ with $\varepsilon = (1,-1,-1,-1)$, a real number; the scalar part of the left side is therefore real, and the scalar part of $\lambda e_0$ is $\lambda$, whence $\lambda\in\mathbb{R}$.

**Proposition (the coordinate system).** Write $\tilde\Xi = a+\mathbf u$ with $a = \xi_0+i\xi'_0$, $\xi_0,\xi'_0\in\mathbb{R}$, and $\mathbf u = \boldsymbol{\xi}+i\boldsymbol{\xi}'$, $\boldsymbol{\xi},\boldsymbol{\xi}'\in\mathbb{R}^3$. Then $\tilde\Xi\star\tilde\Xi = \lambda e_0$ if and only if

$$
\xi_0^2+\xi'^2_0-\lvert\boldsymbol{\xi}\rvert^2-\lvert\boldsymbol{\xi}'\rvert^2 = \lambda , \qquad \xi_0\boldsymbol{\xi}+\xi'_0\boldsymbol{\xi}' = 0 , \qquad \boldsymbol{\xi}\times\boldsymbol{\xi}' = 0 .
$$

**Proof.** The plain product $\overline{\tilde\Xi}\tilde\Xi = (\overline{a}+\overline{\mathbf u})(a+\mathbf u)$ has scalar part $\xi_0^2+\xi'^2_0-\lvert\boldsymbol{\xi}\rvert^2-\lvert\boldsymbol{\xi}'\rvert^2$, real vector part $2(\xi_0\boldsymbol{\xi}+\xi'_0\boldsymbol{\xi}')$ and imaginary vector part $2i\,\boldsymbol{\xi}\times\boldsymbol{\xi}'$, as the computation of §*The Square-Zero Equation* of *Nilpotents of the General Quaternionic Sesqualgebra* records; setting the three parts equal to those of $\lambda e_0$ gives the system.

## The Root Set of a Central Value

**Theorem (the roots of a central value).** Let $\lambda\in\mathbb{C}$. The value $\lambda$ has a root in $\star$ if and only if $\lambda\in\mathbb{R}$, and then the nonzero roots are exactly

$$
\tilde\Xi = c\bigl(\hat\mu + it\bigr) , \qquad c\in\mathbb{C}^{*} , \quad \hat\mu\in\mathbb{R}^3 , \quad \sum_{k=1}^{3}\hat\mu_k^2 = 1 , \quad t\in\mathbb{R} , \quad (t^2-1)\lvert c\rvert^2 = \lambda ,
$$

together with, when $\lambda>0$, the **central circle** of the scalar roots $\tilde\Xi = ae_0$ with $\lvert a\rvert^2 = \lambda$.

**Proof.** Let $\tilde\Xi = a+\mathbf u$ satisfy the coordinate system. The equation $\boldsymbol{\xi}\times\boldsymbol{\xi}' = 0$ makes the real vectors $\boldsymbol{\xi}$ and $\boldsymbol{\xi}'$ parallel. When $\mathbf u = 0$ the system reduces to $\lvert a\rvert^2 = \lambda$, so $\lambda>0$ and $a$ runs over the circle $\lvert a\rvert^2 = \lambda$; the value $\lambda = 0$ gives $a = 0$, which is not a root because a root is nonzero. When $\mathbf u \neq 0$ one writes $\mathbf u = c\hat\mu$ with $c\in\mathbb{C}^{*}$ and $\hat\mu$ a real unit vector, and the equation $\xi_0\boldsymbol{\xi}+\xi'_0\boldsymbol{\xi}' = 0$ becomes $\operatorname{Re}(\overline{a}c) = 0$; when $a \neq 0$ this says $c = ita$ with $t\in\mathbb{R}$, and when $a = 0$ the same relation holds with the parameter $t = 0$, the first equation giving $\lvert c\rvert^2 = -\lambda$. Substituting $a = itc$ into the first equation gives $(t^2-1)\lvert c\rvert^2 = \lambda$, and the parametrization $a = itc$, $\mathbf u = c\hat\mu$ is $\tilde\Xi = c(\hat\mu+it)$. The family is well parametrized: for $\lambda\neq0$ the modulus $\lvert c\rvert$ is determined by $t$ through the displayed equation, while the argument of $c$ and the direction $\hat\mu$ are free.

**Corollary (the shape of the root set and its dimension).** For $\lambda\neq0$ the root set is a real four-dimensional family, $t$ of one real parameter, the argument of $c$ of one and the direction $\hat\mu$ of two, with $\lvert c\rvert$ determined by $t$; for $\lambda>0$ it carries in addition the real one-dimensional central circle; and for $\lambda = 0$ the family is the square-zero set of *Nilpotents of the General Quaternionic Sesqualgebra*, of real dimension four.

**Proof.** The parameter count is the one stated, and at $\lambda = 0$ the equation $(t^2-1)\lvert c\rvert^2 = 0$ gives $t = \pm1$, so the family is $c(\hat\mu\pm i)$, the square-zero set of the cited article.

## The Three Values

**Theorem (the roots of $-1$).** The roots of $-1$ in $\star$ are exactly

$$
\tilde\Xi = c\bigl(\hat\mu + it\bigr) , \qquad c\in\mathbb{C}^{*} , \quad \lvert t\rvert<1 , \quad \lvert c\rvert^2 = \frac{1}{1-t^2} , \qquad \lvert\hat\mu\rvert = 1 ,
$$

a real four-dimensional family; the three basis vectors $e_1$, $e_2$, $e_3$ are roots, and no root of $-1$ is a pure scalar.

**Proof.** The value is negative, so the central circle is absent and $(t^2-1)\lvert c\rvert^2 = -1$ forces $t^2<1$ and $\lvert c\rvert^2 = 1/(1-t^2)$. The element $e_k = 1\cdot(\hat\mu+it)$ with $\hat\mu = e_k$, $t = 0$ has $\lvert c\rvert^2 = 1$ and $(t^2-1)\lvert c\rvert^2 = -1$, so it is a root; the same computation shows $\lvert t\rvert<1$, so the scalar part $itc$ is not the whole element and the roots are not scalars.

**Theorem (the roots of $0$).** The roots of $0$ in $\star$ are exactly the square-zero elements $c(\hat\mu\pm i)$, $c\in\mathbb{C}^{*}$, $\lvert\hat\mu\rvert = 1$; they are the nilpotents of *Nilpotents of the General Quaternionic Sesqualgebra*, they form a real four-dimensional family, and every one of them is a zero divisor.

**Proof.** Set $\lambda = 0$ in the theorem of §*The Root Set of a Central Value*, and quote the classification of the square-zero elements.

**Theorem (the roots of $+1$).** The roots of $+1$ in $\star$ are exactly the central circle $\lvert a\rvert^2 = 1$ together with the family

$$
\tilde\Xi = c\bigl(\hat\mu + it\bigr) , \qquad c\in\mathbb{C}^{*} , \quad \lvert t\rvert>1 , \quad \lvert c\rvert^2 = \frac{1}{t^2-1} , \qquad \lvert\hat\mu\rvert = 1 ,
$$

a real four-dimensional family beside the circle; the elements $e_0$ and $i$ are roots, and no root of $+1$ is square-zero.

**Proof.** The value is positive, so the central circle is present and is read off the case $\mathbf u = 0$; the family is $(t^2-1)\lvert c\rvert^2 = 1$, with $t^2>1$. The elements $e_0$ and $i$ are the scalar roots of modulus one. A square-zero element would give $\lambda = 0$, so it is not a root of $+1$.

## The Units and the Zero Divisors among the Roots

**Theorem (the interleaving).** Let $\tilde\Xi$ be a root of the real value $\lambda$. Then

$$
C(\tilde\Xi) = c^2\,(1-t^2)
$$

in the parametrization $\tilde\Xi = c(\hat\mu+it)$, and for the scalar roots $c(ae_0) = a^2$. Consequently a root of $-1$ or of $+1$ is a **unit of the plain algebra**, $C(\tilde\Xi)\neq0$, while a root of $0$ is a zero divisor, $C(\tilde\Xi) = 0$.

**Proof.** The central square of $c(\hat\mu+it)$ is $c^2$ times the sum of the squares of the four coordinates of $\hat\mu+it$, which is $\sum_k\hat\mu_k^2 + (it)^2 = 1-t^2$; for the scalar root it is $a^2$. The criterion of invertibility of the plain algebra is $C\neq0$ (*Norm and Invertibility in the General Quaternionic Sesqualgebra*), so a root of $-1$ or of $+1$ is a unit of the plain algebra and a root of $0$ is a zero divisor. On the family the value $\lambda = (t^2-1)\lvert c\rvert^2$ has the sign of the real factor $t^2-1$, negative on $\lvert t\rvert<1$ and positive on $\lvert t\rvert>1$, and it vanishes at $t = \pm1$; the scalar circle carries the positive values.

So the three classes are read from one scalar: the roots of $-1$ and of $+1$ are units of the plain algebra, and the roots of $0$ are the zero divisors, in the sharp form of the interleaving of *Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

## The Three Values and the Plain Product

The plain algebra reads the three values as the imaginary units, the involutions and the nilpotent cone: the roots of $-1$ are the elements with $\xi^2 = -e_0$, a family of complex dimension two, the roots of $+1$ the involutions with $\xi^2 = e_0$, and the idempotents are the roots of $+1$ halved, $\tfrac12(e_0+\xi)$ (*Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*, *Idempotents of the General Plain Algebra*). The GQS keeps the names and changes the sets. The roots of $-1$ here are not the pure isotropic family of the plain product; the roots of $+1$ here are **not** the idempotent parameters of $\star$, because the idempotents of the block are the family $-\tfrac12e_0+\mu$ with $\lvert\mu\rvert^2 = \tfrac34$ (*Idempotents of the General Quaternionic Sesqualgebra*), while a root of $+1$ satisfies $\tilde\Xi\star\tilde\Xi = e_0$. The roots of $0$ are the square-zero elements, and in the plain product they are the pure isotropic cone; the block moves them to the non-pure family. The roots of $+1$ and the idempotents of the block meet at $e_0$ alone: an element that is both satisfies $\tilde\Pi\star\tilde\Pi = \tilde\Pi$ and $\tilde\Pi\star\tilde\Pi = e_0$, so $\tilde\Pi = e_0$, and $e_0$ is an idempotent and a root of $+1$; the element $0$ is an idempotent of the block but it is excluded from the roots, which are nonzero by definition. The three values therefore name three classes of the block that are **not** the plain classes of the same name, and the comparison is the one of *Square Roots of a General Element in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

## Summary

A root of the central value $\lambda$ in the general quaternionic sesquilinear product $\tilde\Xi\star\tilde Q = \tilde\Xi^{\natural}\tilde Q^{*}$ is a nonzero element with $\tilde\Xi\star\tilde\Xi = \lambda e_0$, and the square reduces to $\tilde\Xi\star\tilde\Xi = (\overline{\tilde\Xi}\tilde\Xi)^{\natural}$. The scalar part of the square is the Krein form $\sum_\mu\varepsilon_\mu\lvert \Xi_\mu\rvert^2$ with $\varepsilon = (1,-1,-1,-1)$, so no root exists unless $\lambda$ is real.

For real $\lambda$ the roots are the family $\tilde\Xi = c(\hat\mu+it)$ with $(t^2-1)\lvert c\rvert^2 = \lambda$, of real dimension four, together with the central circle $\lvert a\rvert^2 = \lambda$ when $\lambda>0$. The value $-1$ takes the slopes $\lvert t\rvert<1$, with $\lvert c\rvert^2 = 1/(1-t^2)$, and contains $e_1,e_2,e_3$; the value $0$ takes the slopes $t = \pm1$ and is the square-zero family $c(\hat\mu\pm i)$; the value $+1$ takes the slopes $\lvert t\rvert>1$, with $\lvert c\rvert^2 = 1/(t^2-1)$, beside the central circle, and contains $e_0$ and $i$. The central square of a root is $C(\tilde\Xi) = c^2(1-t^2)$, so the roots of $-1$ and of $+1$ are units of the plain algebra and the roots of $0$ are zero divisors, and the three classes are not the plain classes of the same name.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde\Xi\star\tilde Q = \tilde\Xi^{\natural}\tilde Q^{*}$ | the general quaternionic sesquilinear product |
| root of $\lambda$ | a nonzero $\tilde\Xi$ with $\tilde\Xi\star\tilde\Xi = \lambda e_0$ |
| $\tilde\Xi\star\tilde\Xi = (\overline{\tilde\Xi}\tilde\Xi)^{\natural}$ | the reduction of the square |
| $\sum_\mu\varepsilon_\mu\lvert \Xi_\mu\rvert^2$, $\varepsilon = (1,-1,-1,-1)$ | the Krein form, the scalar part of $\overline{\tilde\Xi}\tilde\Xi$ |
| $c(\hat\mu+it)$, $(t^2-1)\lvert c\rvert^2 = \lambda$ | the root family, $\lvert\hat\mu\rvert = 1$ |
| central circle, $\lvert a\rvert^2 = \lambda$ | the scalar roots, present only for $\lambda>0$ |
| $C(\tilde\Xi) = c^2(1-t^2)$ | the central square of a root |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the root of a central value and the three values of the biquaternion algebra.
- *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-general-plain-algebra.md`), for the plain reading of the three values, against which this article's sets are compared.
- *Nilpotents of the General Quaternionic Sesqualgebra* (`articles_maths/nilpotents-of-the-general-quaternionic-sesqualgebra.md`), for the roots of $0$, the square-zero family $c(\hat\mu+i)$.
- *Square Roots of a General Element in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/square-roots-of-a-general-element-in-the-12-algebraic-structures-over-the-biquaternion-c-space.md`), for the four-way comparison of the root sets.
- *Idempotents of the General Quaternionic Sesqualgebra* (`articles_maths/idempotents-of-the-general-quaternionic-sesqualgebra.md`), for the idempotent family $-\tfrac12e_0+\mu$, which is not the halved root family of $+1$.
- *The Square of the General Quaternionic Sesquilinear Product and the Two Halves* (`articles_maths/the-square-of-the-quaternionic-sesquilinear-product-and-the-two-halves.md`), for the identity $\tilde\Xi\star\tilde\Xi = (\overline{\tilde\Xi}\tilde\Xi)^{\natural}$ and the Krein scalar part.
- *Norm and Invertibility in the General Quaternionic Sesqualgebra* (`articles_maths/norm-and-invertibility-in-the-general-quaternionic-sesqualgebra.md`), for the criterion of invertibility of the plain algebra used in §*The Units and the Zero Divisors among the Roots*.
- *Conventions in Mathematics* (`articles_maths/conventions-in-mathematics.md`), for the notation and the article format.
