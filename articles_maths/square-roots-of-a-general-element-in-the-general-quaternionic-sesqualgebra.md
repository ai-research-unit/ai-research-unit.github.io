# __Square Roots of a General Element in the General Quaternionic Sesqualgebra__

## Introduction

The **square root** of an element $a$ in a product $\star$ is an element $\tilde\Xi$ with $\tilde\Xi\star\tilde\Xi = a$, the definition being *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* §6; the roots of a central value are the special case $a = \lambda e_0$ and are treated in *Square Roots of One and the Idempotents of the General Quaternionic Sesqualgebra*, whose central-value theorem gives them, and in *Square Roots of Zero and the Nilpotents of the General Quaternionic Sesqualgebra* for the value $0$. This article solves the general problem for the **general quaternionic sesquilinear product**

$$
\tilde\Xi \star \tilde Q = \tilde\Xi^{\natural}\tilde Q^{*}
$$

of *Introduction to the General Quaternionic Sesqualgebra of Biquaternions*, and its content is a **criterion**: a general element $\tilde A$ of the biquaternion space is the square of an element of $\star$ if and only if its scalar part is real, the two vectors obtained from its vector part are orthogonal, and a scalar bound holds; the square map is therefore **not** surjective, its image is a real six-dimensional set of the real eight-dimensional space, and a non-empty set of elements has no square root at all.

The reduction is the central-square identity $\tilde\Xi\star\tilde\Xi = (\overline{\tilde\Xi}\tilde\Xi)^{\natural}$, which turns the equation into the plain equation $\overline{\tilde\Xi}\tilde\Xi = \tilde A^{\natural}$ on the element $\tilde\Xi = a+\vec u$; the criterion below is the coordinate form of that equation, and the four cases it produces, the free scalar part, the bounded scalar part, the boundary and the central exception, are the four cases of the plain product's quadratic in a different arrangement.

**Conventions.** $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0 = 1, e_1, e_2, e_3$ with $e_1e_2 = e_3$ and central scalar imaginary $i$. An element is $\tilde Q = Q_0e_0+\vec Q$. The conjugations are $\tilde Q^{\natural} = Q_0-\vec Q$, $\tilde Q^{*} = \overline{\tilde Q^{\natural}}$ and $\overline{\tilde Q} = \tilde Q^{\natural*} = \tilde Q^{*\natural}$. The **scalar part** of $\tilde Q$ is $Q_0$ and the **vector part** is $\vec Q$. The product is $\tilde\Xi\star\tilde Q = \tilde\Xi^{\natural}\tilde Q^{*}$, with the natural conjugation ${}^{\natural}$ in the first slot and the star ${}^{*}$ in the second; juxtaposition is the general plain bilinear product. The **Krein form** is $\mathrm{Sc}(\overline{\tilde\Xi}\tilde\Xi) = \sum_\mu\varepsilon_\mu\lvert \Xi_\mu\rvert^2$ with $\varepsilon = (1,-1,-1,-1)$. For a vector $\vec v$ of the complex three-space the **real and imaginary parts** $\operatorname{Re}\vec v$, $\operatorname{Im}\vec v$ are the real vectors of the coordinates, and $\lvert\vec v\rvert$ is the real modulus of $\vec v$; the dot product of two real vectors is written $(\cdot,\cdot)$.

**The results.** A general element $\tilde A$ with scalar part $A_0$ and vector part $\vec R+i\vec S$, with $\vec R,\vec S$ real vectors, is the square of an element of the general quaternionic sesquilinear product $\tilde\Xi\star\tilde Q=\tilde\Xi^{\natural}\tilde Q^{*}$ if and only if $A_0$ is real, the two real vectors $\vec R$ and $\vec S$ are orthogonal, and the scalar bound holds: every real $A_0$ when $\lvert\vec R\rvert>\lvert\vec S\rvert$, $A_0<0$ when $\lvert\vec R\rvert=\lvert\vec S\rvert>0$ or when $\lvert\vec R\rvert<\lvert\vec S\rvert$ with $A_0^{2}\ge\lvert\vec S\rvert^{2}-\lvert\vec R\rvert^{2}$, and every real $A_0$ in the central case $\vec R=\vec S=0$. The image of the square map is therefore a real six-dimensional set of the real eight-dimensional space, and the square map is **not surjective**. At a generic element of the image the roots form a real two-dimensional family, at the central elements a real four-dimensional one, and the nonzero nilpotents such as $e_0+ie_1$ are never squares. Each section below states its result first and then proves it.

## The Reduction to the Plain Equation

**The square reduces to $\tilde\Xi\star\tilde\Xi=(\overline{\tilde\Xi}\tilde\Xi)^{\natural}$, so $\tilde\Xi\star\tilde\Xi=\tilde A$ holds exactly when $\overline{\tilde\Xi}\tilde\Xi=\tilde A^{\natural}$, which on coordinates is the system $\xi_0^{2}+\xi'^{2}_0-\lvert\vec\xi\rvert^{2}-\lvert\vec\xi'\rvert^{2}=A_0$, $2(\xi_0\vec\xi+\xi'_0\vec\xi')=-\vec R$, $2\vec\xi\times\vec\xi'=-\vec S$ for $\tilde\Xi=a+\vec u$ and $\tilde A=A_0+\vec R+i\vec S$.**

**Proposition (the square of an element).** For every $\tilde\Xi$,

$$
\tilde\Xi\star\tilde\Xi = \bigl(\overline{\tilde\Xi}\,\tilde\Xi\bigr)^{\natural} ,
$$

so $\tilde\Xi\star\tilde\Xi = \tilde A$ if and only if $\overline{\tilde\Xi}\tilde\Xi = \tilde A^{\natural}$.

**Proof.** The identity is the one of *The Square of the General Quaternionic Sesquilinear Product and the Two Halves*, proved on coordinates; applying the involution ${}^{\natural}$ to both sides gives the second reading.

**Proposition (the coordinate system).** Write $\tilde\Xi = a+\vec u$ with $a = \xi_0+i\xi'_0$, $\xi_0,\xi'_0\in\mathbb{R}$, and $\vec u = \vec\xi+i\vec\xi'$, $\vec\xi,\vec\xi'\in\mathbb{R}^3$, and write $\tilde A$ with scalar part $A_0$ and vector part $\vec v = \vec R+i\vec S$, $\vec R,\vec S\in\mathbb{R}^3$. Then $\tilde\Xi\star\tilde\Xi = \tilde A$ if and only if

$$
\xi_0^2+\xi'^2_0-\lvert\vec\xi\rvert^2-\lvert\vec\xi'\rvert^2 = A_0 , \qquad 2(\xi_0\vec\xi+\xi'_0\vec\xi') = -\vec R , \qquad 2\,\vec\xi\times\vec\xi' = -\vec S .
$$

**Proof.** The plain product $\overline{\tilde\Xi}\tilde\Xi = (\overline{a}+\overline{\vec u})(a+\vec u)$ has scalar part $\xi_0^2+\xi'^2_0-\lvert\vec\xi\rvert^2-\lvert\vec\xi'\rvert^2$, real vector part $2(\xi_0\vec\xi+\xi'_0\vec\xi')$ and imaginary vector part $2i\,\vec\xi\times\vec\xi'$, as in §*The Reduction of the Root Equation* of *Square Roots of One and the Idempotents of the General Quaternionic Sesqualgebra*; the equation $\overline{\tilde\Xi}\tilde\Xi = \tilde A^{\natural}$ has scalar part $A_0$ because the natural conjugation fixes the scalar part, and vector part $-\vec v = -\vec R-i\vec S$; the identification of the three parts is the displayed system.

## The Solvability Criterion

**The element $\tilde A$ has a square root exactly when $A_0$ is real, $\vec R$ is orthogonal to $\vec S$, and the scalar bound holds in the four cases: every real $A_0$ when $\lvert\vec R\rvert>\lvert\vec S\rvert$, $A_0<0$ when $\lvert\vec R\rvert=\lvert\vec S\rvert>0$, $A_0<0$ with $A_0^{2}\ge\lvert\vec S\rvert^{2}-\lvert\vec R\rvert^{2}$ when $\lvert\vec R\rvert<\lvert\vec S\rvert$, and every real $A_0$ in the central case $\vec R=\vec S=0$; the image is a real six-dimensional set, so the square map is not surjective.**

**Theorem (the image of the square map).** Let $\tilde A$ have scalar part $A_0$ and vector part $\vec v = \vec R+i\vec S$ with $\vec R,\vec S$ real vectors. Then $\tilde A$ has a square root in $\star$ if and only if one of the four following holds:

- **the scalar part is real and the two real vectors are orthogonal**, $A_0\in\mathbb{R}$ and $(\vec R,\vec S) = 0$, and
  - $\lvert\vec R\rvert > \lvert\vec S\rvert$, in which case **every** real $A_0$ is allowed;
  - $\lvert\vec R\rvert = \lvert\vec S\rvert > 0$, in which case $A_0 < 0$;
  - $0 \le \lvert\vec R\rvert < \lvert\vec S\rvert$, in which case $A_0 < 0$ and $A_0^2 \ge \lvert\vec S\rvert^2-\lvert\vec R\rvert^2$;
  - $\vec R = \vec S = 0$, the **central case** $\tilde A = A_0e_0$, in which every real $A_0$ is allowed.

**Proof.** *Necessity.* The scalar part of $\overline{\tilde\Xi}\tilde\Xi$ is the Krein form of $\tilde\Xi$, a real number, so $A_0$ is real. The real vector part of $\overline{\tilde\Xi}\tilde\Xi$ is $2(\xi_0\vec\xi+\xi'_0\vec\xi')$, a combination of $\vec\xi$ and $\vec\xi'$, and the imaginary vector part is $2\,\vec\xi\times\vec\xi'$, which is orthogonal to both $\vec\xi$ and $\vec\xi'$; hence $\vec R$ and $\vec S$ are orthogonal, with $(\vec R,\vec S) = -4(\xi_0\vec\xi+\xi'_0\vec\xi',\vec\xi\times\vec\xi') = 0$.

For the bound, let $G$ be the Gram matrix of the pair $(\vec\xi,\vec\xi')$, with entries $P = \lvert\vec\xi\rvert^2$, $Q = \lvert\vec\xi'\rvert^2$ and $C = (\vec\xi,\vec\xi')$, so $\det G = \lvert\vec\xi\times\vec\xi'\rvert^2 = \lvert\vec S\rvert^2/4$, and let $\vec m = \xi_0\vec\xi+\xi'_0\vec\xi'$, so $\lvert\vec m\rvert^2 = \vec v^{\mathsf T}G\vec v = \lvert\vec R\rvert^2/4$ for the pair $\vec v = (\xi_0,\xi'_0)$. The pair $(\vec\xi,\vec\xi')$ is independent exactly when $\vec S\neq0$, and then $G$ is definite with eigenvalues $\lambda_1,\lambda_2>0$, $\lambda_1\lambda_2 = \det G$ and $\lambda_1+\lambda_2 = \operatorname{tr}G = P+Q$. In an orthonormal eigenbasis of $G$ the two scalars are

$$
\vec v^{\mathsf T}G\vec v = \lambda_1v_1^2+\lambda_2v_2^2 , \qquad \xi_0^2+\xi'^2_0 = v_1^2+v_2^2 .
$$

If $\lvert\vec R\rvert\le\lvert\vec S\rvert$ and $\vec S\neq0$ then $\vec v^{\mathsf T}G\vec v\le\det G$, so $\lambda_1v_1^2\le\lambda_1\lambda_2$ and $\lambda_2v_2^2\le\lambda_1\lambda_2$, that is $v_1^2\le\lambda_2$ and $v_2^2\le\lambda_1$; hence $\xi_0^2+\xi'^2_0 \le \lambda_1+\lambda_2 = P+Q$, that is $A_0 \le 0$. The estimate is strict unless $v_1^2 = \lambda_2$ and $v_2^2 = \lambda_1$ together, and such a pair would give $\vec v^{\mathsf T}G\vec v = 2\lambda_1\lambda_2 > \det G$; so $A_0<0$ whenever $\lvert\vec R\rvert\le\lvert\vec S\rvert$ and $\vec S\neq0$, the equality $A_0 = 0$ being excluded by the same argument. Finally the quantity of the bound is a square. With the rank-one matrix $W = \vec v\vec v^{\mathsf T}$ the three scalars are $\operatorname{tr}W = \xi_0^2+\xi'^2_0$, $\operatorname{tr}(WG) = \lvert\vec m\rvert^2$ and $\det W = 0$, and the identity $\det(W+G) = \det W+\det G+\operatorname{tr}W\operatorname{tr}G-\operatorname{tr}(WG)$ gives

$$
A_0^2+\lvert\vec R\rvert^2-\lvert\vec S\rvert^2 = \bigl(\operatorname{tr}W-\operatorname{tr}G\bigr)^2+4\operatorname{tr}(WG)-4\det G = \bigl(\operatorname{tr}(W+G)\bigr)^2-4\det(W+G) .
$$

The matrix $W+G$ is symmetric and positive semi-definite, the sum of the positive semi-definite $W$ and $G$, so its two eigenvalues $\mu_1,\mu_2$ are non-negative and

$$
\bigl(\operatorname{tr}(W+G)\bigr)^2-4\det(W+G) = (\mu_1+\mu_2)^2-4\mu_1\mu_2 = (\mu_1-\mu_2)^2 \ge 0 .
$$

Hence $A_0^2+\lvert\vec R\rvert^2\ge\lvert\vec S\rvert^2$ always, which is the bound.

*Sufficiency.* When $\vec R\neq0$ choose the real unit vectors $\hat u_1 = \vec R/\lvert\vec R\rvert$ and $\hat u_2 = \hat S\times\hat u_1$ when $\vec S\neq0$, and $\hat u_1 = \vec R/\lvert\vec R\rvert$ together with any vector orthogonal to it when $\vec S = 0$; set $\vec\xi = -\alpha\hat u_1$, $\vec\xi' = \beta\hat u_2$ with $\alpha\beta = \lvert\vec S\rvert/2$ and $\xi_0 = \lvert\vec R\rvert/(2\alpha)$, $\xi'_0 = 0$. Then $\vec\xi\times\vec\xi' = -\alpha\beta\,(\hat u_1\times\hat u_2) = -\vec S/2$ and $\xi_0\vec\xi+\xi'_0\vec\xi' = -\alpha \xi_0\hat u_1 = -\vec R/2$ because $\vec R$ is parallel to $\hat u_1$, so the second and the third equations of the coordinate system hold. The first equation becomes

$$
\frac{\lvert\vec R\rvert^2}{4\alpha^2}-\alpha^2-\frac{\lvert\vec S\rvert^2}{4\alpha^2} = A_0 ,
$$

an equation in $w = \alpha^2$ with the solution $w = \tfrac12\bigl(-A_0+\sqrt{A_0^2+\lvert\vec R\rvert^2-\lvert\vec S\rvert^2}\bigr)$; the solution is positive exactly when $\lvert\vec R\rvert>\lvert\vec S\rvert$, or when $\lvert\vec R\rvert\le\lvert\vec S\rvert$ with $A_0<0$ and $A_0^2\ge\lvert\vec S\rvert^2-\lvert\vec R\rvert^2$, which are the three non-central cases of the statement. When $\vec R = 0$ and $\vec S\neq0$ the same construction with $\lvert\vec R\rvert = 0$ gives the bound $A_0\le-\lvert\vec S\rvert$, the case $\xi_0 = \xi'_0 = 0$ of the estimate. When $\vec S = 0$ and $\vec R\neq0$ the ansatz $\vec\xi' = 0$, $\vec\xi = -\alpha\hat u_1$, $\xi'_0 = 0$, $\xi_0 = \lvert\vec R\rvert/(2\alpha)$ gives $A_0 = \lvert\vec R\rvert^2/(4\alpha^2)-\alpha^2$, which takes every real value as $\alpha$ runs over the positive numbers. When $\vec R = \vec S = 0$ the element is central, $\tilde A = A_0e_0$, and the scalar root $\tilde\Xi = ae_0$ with $\lvert a\rvert^2 = A_0$ exists for the positive $A_0$, while the non-positive values are read from the general root family of *Square Roots of One and the Idempotents of the General Quaternionic Sesqualgebra*, the value $0$ being *Square Roots of Zero and the Nilpotents of the General Quaternionic Sesqualgebra*; this is the central case.

**Corollary (the square map is not surjective).** The image of the square map $\tilde\Xi\mapsto\tilde\Xi\star\tilde\Xi$ is the set of the theorem, a real six-dimensional subset of the real eight-dimensional space; the elements with $\vec R$ not orthogonal to $\vec S$, and the elements with $\lvert\vec R\rvert\le\lvert\vec S\rvert$, $\vec S\neq0$ and $A_0$ failing the scalar bound ($A_0<0$, and $A_0^2\ge\lvert\vec S\rvert^2-\lvert\vec R\rvert^2$ when $\lvert\vec R\rvert<\lvert\vec S\rvert$), have no square root.

**Proof.** The conditions $A_0\in\mathbb{R}$, $(\vec R,\vec S) = 0$ and the scalar inequality cut a real six-dimensional set, one scalar and one orthogonality relation removing two of the eight real dimensions, and the theorem identifies it with the image.

## The Solution Family

**At a generic element of the image the square roots form a real two-dimensional family, while the central elements are the exception with a fibre of real dimension four, which are the roots of the central value $c(\hat u_{\mathrm n}+it)$ together with the central circle when $\lambda>0$; a nonzero nilpotent such as $e_0+ie_1$ has no square root.**

**Proposition (the dimension of the solution set).** For a generic element $\tilde A$ of the image the square roots form a real two-dimensional family; the central elements are the exception, with a fibre of real dimension four. On $\tilde A = \lambda e_0$ the roots are those of the central value: the family $c(\hat u_{\mathrm n}+it)$ of *Square Roots of One and the Idempotents of the General Quaternionic Sesqualgebra*, of real dimension four, together with the central circle $\lvert a\rvert^2 = \lambda$ when $\lambda>0$.

**Proof.** The unknown is the quadruple $(\xi_0,\xi'_0,\vec\xi,\vec\xi')$ of real dimension eight, and the differential of the square map has rank six at a generic $\tilde\Xi$, so its fibre is of real dimension two and the generic solution family is two-dimensional. The rank drops to four on the roots of a central value, whose fibre is the family $c(\hat u_{\mathrm n}+it)$ with the slope $t$, the argument of $c$ and the direction $\hat u_{\mathrm n}$ as its four real parameters; the scalar roots add the one-dimensional circle $\lvert a\rvert^2 = \lambda$ when $\lambda>0$. The central elements are therefore the exception to the generic dimension.

The corollary below records the two extremes.

**Corollary (a nilpotent is not a square).** The nilpotent $e_0+ie_1$ of *Square Roots of Zero and the Nilpotents of the General Quaternionic Sesqualgebra* has no square root in $\star$: its scalar part is $1$, its vector part is $ie_1$, so $\vec R = 0$ and $\lvert\vec S\rvert = 1$, and the bound $A_0\le-\lvert\vec S\rvert = -1$ fails at $A_0 = 1$.

**Proof.** The values are read on the display; the criterion of the theorem excludes them.

So the square-zero family of the block and the image of its square map are disjoint apart from the origin: a nonzero nilpotent is never a square, which is the sharpest form of the failure of surjectivity.

## Summary

A square root of $\tilde A$ in the general quaternionic sesquilinear product $\tilde\Xi\star\tilde Q = \tilde\Xi^{\natural}\tilde Q^{*}$ is an element with $\tilde\Xi\star\tilde\Xi = \tilde A$, and the square reduces to $\tilde\Xi\star\tilde\Xi = (\overline{\tilde\Xi}\tilde\Xi)^{\natural}$, so the equation is the plain equation $\overline{\tilde\Xi}\tilde\Xi = \tilde A^{\natural}$. On coordinates $\tilde\Xi = \xi_0+i\xi'_0+\vec\xi+i\vec\xi'$ and $\tilde A$ with scalar part $A_0$ and vector part $\vec R+i\vec S$ the equation is the system $\xi_0^2+\xi'^2_0-\lvert\vec\xi\rvert^2-\lvert\vec\xi'\rvert^2 = A_0$, $2(\xi_0\vec\xi+\xi'_0\vec\xi') = -\vec R$, $2\vec\xi\times\vec\xi' = -\vec S$.

The element $\tilde A$ is a square if and only if $A_0$ is real, $\vec R$ is orthogonal to $\vec S$, and the scalar part satisfies the bound $A_0<0$, $A_0^2\ge\lvert\vec S\rvert^2-\lvert\vec R\rvert^2$ when $\lvert\vec R\rvert\le\lvert\vec S\rvert$ and $\vec S\neq0$, with no further restriction when $\lvert\vec R\rvert>\lvert\vec S\rvert$ and in the central case $\vec R = \vec S = 0$ where the roots are the roots of the central value. The image of the square map is a real six-dimensional set, so a non-empty set of elements has no square root; the solution family is of real dimension two at a generic element of the image and of real dimension four at the central elements, and the nonzero nilpotents, in particular $e_0+ie_1$, are never squares.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde\Xi\star\tilde Q = \tilde\Xi^{\natural}\tilde Q^{*}$ | the general quaternionic sesquilinear product |
| square root of $\tilde A$ | an element $\tilde\Xi$ with $\tilde\Xi\star\tilde\Xi = \tilde A$ |
| $\tilde\Xi\star\tilde\Xi = (\overline{\tilde\Xi}\tilde\Xi)^{\natural}$ | the reduction of the square |
| $A_0$, $\vec R+i\vec S$ | the scalar part and the vector part of $\tilde A$ |
| $(\vec R,\vec S) = 0$ | the orthogonality of the two real vectors |
| $A_0<0$, $A_0^2\ge\lvert\vec S\rvert^2-\lvert\vec R\rvert^2$ | the scalar bound when $\lvert\vec R\rvert\le\lvert\vec S\rvert$ and $\vec S\neq0$ |
| $\vec R=\vec S=0$ | the central case, the roots of a central value |

## Further Reading

- *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternioid-c-space.md`), for the square root of an element and the root of a central value.
- *Square Roots of One and the Idempotents of the General Quaternionic Sesqualgebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-general-quaternionic-sesqualgebra.md`), for the central case, the family $c(\hat u_{\mathrm n}+it)$ and the reduction identity used here.
- *Square Roots of a General Element in the General Plain Algebra* (`articles_maths/square-roots-of-a-general-element-in-the-biquaternion-algebra.md`), for the plain problem and its quadratic, against which this criterion is set.
- *Square Roots of Zero and the Nilpotents of the General Quaternionic Sesqualgebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-general-quaternionic-sesqualgebra.md`), for the square-zero family and the element $e_0+ie_1$.
- *The Square of the General Quaternionic Sesquilinear Product and the Two Halves* (`articles_maths/the-square-of-the-quaternionic-sesquilinear-product-and-the-two-halves.md`), for the identity $\tilde\Xi\star\tilde\Xi = (\overline{\tilde\Xi}\tilde\Xi)^{\natural}$ and the Krein form.
- *Square Roots of a General Element in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/square-roots-of-a-general-element-in-the-algebraic-structures-over-the-biquaternioid-c-space.md`), for the four-way comparison of the root sets.
- *Conventions in Mathematics* (`articles_maths/conventions-in-mathematics.md`), for the notation and the article format.
