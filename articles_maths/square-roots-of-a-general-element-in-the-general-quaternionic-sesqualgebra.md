# __Square Roots of a General Element in the General Quaternionic Sesqualgebra__

## Introduction

The **square root** of an element $a$ in a product $\star$ is an element $\tilde P$ with $\tilde P\star\tilde P = a$, the definition being *Definitions for the Study of the 12 Algebraic Structures* §6; the roots of a central value are the special case $a = \lambda e_0$ and are treated in *Square Roots of Minus One, Zero and Plus One in the General Quaternionic Sesqualgebra*. This article solves the general problem for the **general quaternionic sesquilinear product**

$$
\tilde P \star \tilde Q = \tilde P^{\natural}\tilde Q^{*}
$$

of *Introduction to the General Quaternionic Sesqualgebra of Biquaternions*, and its content is a **criterion**: a general element $\tilde A$ of the biquaternion space is the square of an element of $\star$ if and only if its scalar part is real, the two vectors obtained from its vector part are orthogonal, and a scalar bound holds; the square map is therefore **not** surjective, its image is a real six-dimensional set of the real eight-dimensional space, and a non-empty set of elements has no square root at all.

The reduction is the central-square identity $\tilde P\star\tilde P = (\overline{\tilde P}\tilde P)^{\natural}$, which turns the equation into the plain equation $\overline{\tilde P}\tilde P = \tilde A^{\natural}$ on the element $\tilde P = a+\mathbf u$; the criterion below is the coordinate form of that equation, and the four cases it produces, the free scalar part, the bounded scalar part, the boundary and the central exception, are the four cases of the plain product's quadratic in a different arrangement.

**Conventions.** $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0 = 1, e_1, e_2, e_3$ with $e_1e_2 = e_3$ and central scalar imaginary $i$. An element is $\tilde Q = Q_0e_0+\mathbf Q$. The conjugations are $\tilde Q^{\natural} = Q_0-\mathbf Q$, $\tilde Q^{*} = \overline{\tilde Q^{\natural}}$ and $\overline{\tilde Q} = \tilde Q^{\natural*} = \tilde Q^{*\natural}$. The **scalar part** of $\tilde Q$ is $Q_0$ and the **vector part** is $\mathbf Q$. The product is $\tilde P\star\tilde Q = \tilde P^{\natural}\tilde Q^{*}$, with the natural conjugation ${}^{\natural}$ in the first slot and the star ${}^{*}$ in the second; juxtaposition is the general plain bilinear product. The **Krein form** is $\mathrm{Sc}(\overline{\tilde P}\tilde P) = \sum_\mu\varepsilon_\mu\lvert P_\mu\rvert^2$ with $\varepsilon = (1,-1,-1,-1)$. For a vector $\mathbf v$ of the complex three-space the **real and imaginary parts** $\operatorname{Re}\mathbf v$, $\operatorname{Im}\mathbf v$ are the real vectors of the coordinates, and $\lvert\mathbf v\rvert$ is the real norm of $\mathbf v$; the dot product of two real vectors is written $(\cdot,\cdot)$.

## The Reduction to the Plain Equation

**Proposition (the square of an element).** For every $\tilde P$,

$$
\tilde P\star\tilde P = \bigl(\overline{\tilde P}\,\tilde P\bigr)^{\natural} ,
$$

so $\tilde P\star\tilde P = \tilde A$ if and only if $\overline{\tilde P}\tilde P = \tilde A^{\natural}$.

**Proof.** The identity is the one of *The Square of the General Quaternionic Sesquilinear Product and the Two Halves*, proved on coordinates; applying the involution ${}^{\natural}$ to both sides gives the second reading.

**Proposition (the coordinate system).** Write $\tilde P = a+\mathbf u$ with $a = x_0+iy_0$, $x_0,y_0\in\mathbb{R}$, and $\mathbf u = \mathbf p+i\mathbf q$, $\mathbf p,\mathbf q\in\mathbb{R}^3$, and write $\tilde A$ with scalar part $A_0$ and vector part $\mathbf v = \mathbf R+i\mathbf S$, $\mathbf R,\mathbf S\in\mathbb{R}^3$. Then $\tilde P\star\tilde P = \tilde A$ if and only if

$$
x_0^2+y_0^2-\lvert\mathbf p\rvert^2-\lvert\mathbf q\rvert^2 = A_0 , \qquad 2(x_0\mathbf p+y_0\mathbf q) = -\mathbf R , \qquad 2\,\mathbf p\times\mathbf q = -\mathbf S .
$$

**Proof.** The plain product $\overline{\tilde P}\tilde P = (\overline{a}+\overline{\mathbf u})(a+\mathbf u)$ has scalar part $x_0^2+y_0^2-\lvert\mathbf p\rvert^2-\lvert\mathbf q\rvert^2$, real vector part $2(x_0\mathbf p+y_0\mathbf q)$ and imaginary vector part $2i\,\mathbf p\times\mathbf q$, as in §*The Square-Zero Equation* of *Nilpotents of the General Quaternionic Sesqualgebra*; the equation $\overline{\tilde P}\tilde P = \tilde A^{\natural}$ has scalar part $A_0$ because the natural conjugation fixes the scalar part, and vector part $-\mathbf v = -\mathbf R-i\mathbf S$; the identification of the three parts is the displayed system.

## The Solvability Criterion

**Theorem (the image of the square map).** Let $\tilde A$ have scalar part $A_0$ and vector part $\mathbf v = \mathbf R+i\mathbf S$ with $\mathbf R,\mathbf S$ real vectors. Then $\tilde A$ has a square root in $\star$ if and only if one of the four following holds:

- **the scalar part is real and the two real vectors are orthogonal**, $A_0\in\mathbb{R}$ and $(\mathbf R,\mathbf S) = 0$, and
  - $\lvert\mathbf R\rvert > \lvert\mathbf S\rvert$, in which case **every** real $A_0$ is allowed;
  - $\lvert\mathbf R\rvert = \lvert\mathbf S\rvert > 0$, in which case $A_0 < 0$;
  - $0 \le \lvert\mathbf R\rvert < \lvert\mathbf S\rvert$, in which case $A_0 < 0$ and $A_0^2 \ge \lvert\mathbf S\rvert^2-\lvert\mathbf R\rvert^2$;
  - $\mathbf R = \mathbf S = 0$, the **central case** $\tilde A = A_0e_0$, in which every real $A_0$ is allowed.

**Proof.** *Necessity.* The scalar part of $\overline{\tilde P}\tilde P$ is the Krein form of $\tilde P$, a real number, so $A_0$ is real. The real vector part of $\overline{\tilde P}\tilde P$ is $2(x_0\mathbf p+y_0\mathbf q)$, a combination of $\mathbf p$ and $\mathbf q$, and the imaginary vector part is $2\,\mathbf p\times\mathbf q$, which is orthogonal to both $\mathbf p$ and $\mathbf q$; hence $\mathbf R$ and $\mathbf S$ are orthogonal, with $(\mathbf R,\mathbf S) = -4(x_0\mathbf p+y_0\mathbf q,\mathbf p\times\mathbf q) = 0$.

For the bound, let $G$ be the Gram matrix of the pair $(\mathbf p,\mathbf q)$, with entries $P = \lvert\mathbf p\rvert^2$, $Q = \lvert\mathbf q\rvert^2$ and $C = (\mathbf p,\mathbf q)$, so $\det G = \lvert\mathbf p\times\mathbf q\rvert^2 = \lvert\mathbf S\rvert^2/4$, and let $\mathbf m = x_0\mathbf p+y_0\mathbf q$, so $\lvert\mathbf m\rvert^2 = \mathbf v^{\mathsf T}G\mathbf v = \lvert\mathbf R\rvert^2/4$ for the pair $\mathbf v = (x_0,y_0)$. The pair $(\mathbf p,\mathbf q)$ is independent exactly when $\mathbf S\neq0$, and then $G$ is definite with eigenvalues $\lambda_1,\lambda_2>0$, $\lambda_1\lambda_2 = \det G$ and $\lambda_1+\lambda_2 = \operatorname{tr}G = P+Q$. In an orthonormal eigenbasis of $G$ the two scalars are

$$
\mathbf v^{\mathsf T}G\mathbf v = \lambda_1v_1^2+\lambda_2v_2^2 , \qquad x_0^2+y_0^2 = v_1^2+v_2^2 .
$$

If $\lvert\mathbf R\rvert\le\lvert\mathbf S\rvert$ and $\mathbf S\neq0$ then $\mathbf v^{\mathsf T}G\mathbf v\le\det G$, so $\lambda_1v_1^2\le\lambda_1\lambda_2$ and $\lambda_2v_2^2\le\lambda_1\lambda_2$, that is $v_1^2\le\lambda_2$ and $v_2^2\le\lambda_1$; hence $x_0^2+y_0^2 \le \lambda_1+\lambda_2 = P+Q$, that is $A_0 \le 0$. The estimate is strict unless $v_1^2 = \lambda_2$ and $v_2^2 = \lambda_1$ together, and such a pair would give $\mathbf v^{\mathsf T}G\mathbf v = 2\lambda_1\lambda_2 > \det G$; so $A_0<0$ whenever $\lvert\mathbf R\rvert\le\lvert\mathbf S\rvert$ and $\mathbf S\neq0$, the equality $A_0 = 0$ being excluded by the same argument. Finally the quantity of the bound is a square. With the rank-one matrix $W = \mathbf v\mathbf v^{\mathsf T}$ the three scalars are $\operatorname{tr}W = x_0^2+y_0^2$, $\operatorname{tr}(WG) = \lvert\mathbf m\rvert^2$ and $\det W = 0$, and the identity $\det(W+G) = \det W+\det G+\operatorname{tr}W\operatorname{tr}G-\operatorname{tr}(WG)$ gives

$$
A_0^2+\lvert\mathbf R\rvert^2-\lvert\mathbf S\rvert^2 = \bigl(\operatorname{tr}W-\operatorname{tr}G\bigr)^2+4\operatorname{tr}(WG)-4\det G = \bigl(\operatorname{tr}(W+G)\bigr)^2-4\det(W+G) .
$$

The matrix $W+G$ is symmetric and positive semi-definite, the sum of the positive semi-definite $W$ and $G$, so its two eigenvalues $\mu_1,\mu_2$ are non-negative and

$$
\bigl(\operatorname{tr}(W+G)\bigr)^2-4\det(W+G) = (\mu_1+\mu_2)^2-4\mu_1\mu_2 = (\mu_1-\mu_2)^2 \ge 0 .
$$

Hence $A_0^2+\lvert\mathbf R\rvert^2\ge\lvert\mathbf S\rvert^2$ always, which is the bound.

*Sufficiency.* When $\mathbf R\neq0$ choose the real unit vectors $\hat u_1 = \mathbf R/\lvert\mathbf R\rvert$ and $\hat u_2 = \hat{\mathbf S}\times\hat u_1$ when $\mathbf S\neq0$, and $\hat u_1 = \mathbf R/\lvert\mathbf R\rvert$ together with any vector orthogonal to it when $\mathbf S = 0$; set $\mathbf p = -\alpha\hat u_1$, $\mathbf q = \beta\hat u_2$ with $\alpha\beta = \lvert\mathbf S\rvert/2$ and $x_0 = \lvert\mathbf R\rvert/(2\alpha)$, $y_0 = 0$. Then $\mathbf p\times\mathbf q = -\alpha\beta\,(\hat u_1\times\hat u_2) = -\mathbf S/2$ and $x_0\mathbf p+y_0\mathbf q = -\alpha x_0\hat u_1 = -\mathbf R/2$ because $\mathbf R$ is parallel to $\hat u_1$, so the second and the third equations of the coordinate system hold. The first equation becomes

$$
\frac{\lvert\mathbf R\rvert^2}{4\alpha^2}-\alpha^2-\frac{\lvert\mathbf S\rvert^2}{4\alpha^2} = A_0 ,
$$

an equation in $w = \alpha^2$ with the solution $w = \tfrac12\bigl(-A_0+\sqrt{A_0^2+\lvert\mathbf R\rvert^2-\lvert\mathbf S\rvert^2}\bigr)$; the solution is positive exactly when $\lvert\mathbf R\rvert>\lvert\mathbf S\rvert$, or when $\lvert\mathbf R\rvert\le\lvert\mathbf S\rvert$ with $A_0<0$ and $A_0^2\ge\lvert\mathbf S\rvert^2-\lvert\mathbf R\rvert^2$, which are the three non-central cases of the statement. When $\mathbf R = 0$ and $\mathbf S\neq0$ the same construction with $\lvert\mathbf R\rvert = 0$ gives the bound $A_0\le-\lvert\mathbf S\rvert$, the case $x_0 = y_0 = 0$ of the estimate. When $\mathbf S = 0$ and $\mathbf R\neq0$ the ansatz $\mathbf q = 0$, $\mathbf p = -\alpha\hat u_1$, $y_0 = 0$, $x_0 = \lvert\mathbf R\rvert/(2\alpha)$ gives $A_0 = \lvert\mathbf R\rvert^2/(4\alpha^2)-\alpha^2$, which takes every real value as $\alpha$ runs over the positive numbers. When $\mathbf R = \mathbf S = 0$ the element is central, $\tilde A = A_0e_0$, and the scalar root $\tilde P = ae_0$ with $\lvert a\rvert^2 = A_0$ exists for the positive $A_0$, while *Square Roots of Minus One, Zero and Plus One in the General Quaternionic Sesqualgebra* gives the roots for the non-positive values; this is the central case.

**Corollary (the square map is not surjective).** The image of the square map $\tilde P\mapsto\tilde P\star\tilde P$ is the set of the theorem, a real six-dimensional subset of the real eight-dimensional space; the elements with $\mathbf R$ not orthogonal to $\mathbf S$, and the elements with $\lvert\mathbf R\rvert\le\lvert\mathbf S\rvert$, $\mathbf S\neq0$ and $A_0$ failing the scalar bound ($A_0<0$, and $A_0^2\ge\lvert\mathbf S\rvert^2-\lvert\mathbf R\rvert^2$ when $\lvert\mathbf R\rvert<\lvert\mathbf S\rvert$), have no square root.

**Proof.** The conditions $A_0\in\mathbb{R}$, $(\mathbf R,\mathbf S) = 0$ and the scalar inequality cut a real six-dimensional set, one scalar and one orthogonality relation removing two of the eight real dimensions, and the theorem identifies it with the image.

## The Solution Family

**Proposition (the dimension of the solution set).** For a generic element $\tilde A$ of the image the square roots form a real two-dimensional family; the central elements are the exception, with a fibre of real dimension four. On $\tilde A = \lambda e_0$ the roots are those of the central value: the family $c(\hat\mu+it)$ of *Square Roots of Minus One, Zero and Plus One in the General Quaternionic Sesqualgebra*, of real dimension four, together with the central circle $\lvert a\rvert^2 = \lambda$ when $\lambda>0$.

**Proof.** The unknown is the quadruple $(x_0,y_0,\mathbf p,\mathbf q)$ of real dimension eight, and the differential of the square map has rank six at a generic $\tilde P$, so its fibre is of real dimension two and the generic solution family is two-dimensional. The rank drops to four on the roots of a central value, whose fibre is the family $c(\hat\mu+it)$ with the slope $t$, the argument of $c$ and the direction $\hat\mu$ as its four real parameters; the scalar roots add the one-dimensional circle $\lvert a\rvert^2 = \lambda$ when $\lambda>0$. The central elements are therefore the exception to the generic dimension.

The corollary below records the two extremes.

**Corollary (a nilpotent is not a square).** The nilpotent $e_0+ie_1$ of *Nilpotents of the General Quaternionic Sesqualgebra* has no square root in $\star$: its scalar part is $1$, its vector part is $ie_1$, so $\mathbf R = 0$ and $\lvert\mathbf S\rvert = 1$, and the bound $A_0\le-\lvert\mathbf S\rvert = -1$ fails at $A_0 = 1$.

**Proof.** The values are read on the display; the criterion of the theorem excludes them.

So the square-zero family of the block and the image of its square map are disjoint apart from the origin: a nonzero nilpotent is never a square, which is the sharpest form of the failure of surjectivity.

## Summary

A square root of $\tilde A$ in the general quaternionic sesquilinear product $\tilde P\star\tilde Q = \tilde P^{\natural}\tilde Q^{*}$ is an element with $\tilde P\star\tilde P = \tilde A$, and the square reduces to $\tilde P\star\tilde P = (\overline{\tilde P}\tilde P)^{\natural}$, so the equation is the plain equation $\overline{\tilde P}\tilde P = \tilde A^{\natural}$. On coordinates $\tilde P = x_0+iy_0+\mathbf p+i\mathbf q$ and $\tilde A$ with scalar part $A_0$ and vector part $\mathbf R+i\mathbf S$ the equation is the system $x_0^2+y_0^2-\lvert\mathbf p\rvert^2-\lvert\mathbf q\rvert^2 = A_0$, $2(x_0\mathbf p+y_0\mathbf q) = -\mathbf R$, $2\mathbf p\times\mathbf q = -\mathbf S$.

The element $\tilde A$ is a square if and only if $A_0$ is real, $\mathbf R$ is orthogonal to $\mathbf S$, and the scalar part satisfies the bound $A_0<0$, $A_0^2\ge\lvert\mathbf S\rvert^2-\lvert\mathbf R\rvert^2$ when $\lvert\mathbf R\rvert\le\lvert\mathbf S\rvert$ and $\mathbf S\neq0$, with no further restriction when $\lvert\mathbf R\rvert>\lvert\mathbf S\rvert$ and in the central case $\mathbf R = \mathbf S = 0$ where the roots are the roots of the central value. The image of the square map is a real six-dimensional set, so a non-empty set of elements has no square root; the solution family is of real dimension two at a generic element of the image and of real dimension four at the central elements, and the nonzero nilpotents, in particular $e_0+ie_1$, are never squares.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde P\star\tilde Q = \tilde P^{\natural}\tilde Q^{*}$ | the general quaternionic sesquilinear product |
| square root of $\tilde A$ | an element $\tilde P$ with $\tilde P\star\tilde P = \tilde A$ |
| $\tilde P\star\tilde P = (\overline{\tilde P}\tilde P)^{\natural}$ | the reduction of the square |
| $A_0$, $\mathbf R+i\mathbf S$ | the scalar part and the vector part of $\tilde A$ |
| $(\mathbf R,\mathbf S) = 0$ | the orthogonality of the two real vectors |
| $A_0<0$, $A_0^2\ge\lvert\mathbf S\rvert^2-\lvert\mathbf R\rvert^2$ | the scalar bound when $\lvert\mathbf R\rvert\le\lvert\mathbf S\rvert$ and $\mathbf S\neq0$ |
| $\mathbf R=\mathbf S=0$ | the central case, the roots of a central value |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the square root of an element and the root of a central value.
- *Square Roots of Minus One, Zero and Plus One in the General Quaternionic Sesqualgebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-general-quaternionic-sesqualgebra.md`), for the central case and the family $c(\hat\mu+it)$ used here.
- *Square Roots of a General Element in the General Plain Algebra* (`articles_maths/square-roots-of-a-general-element-in-the-general-plain-algebra.md`), for the plain problem and its quadratic, against which this criterion is set.
- *Nilpotents of the General Quaternionic Sesqualgebra* (`articles_maths/nilpotents-of-the-general-quaternionic-sesqualgebra.md`), for the square-zero family and the element $e_0+ie_1$.
- *The Square of the General Quaternionic Sesquilinear Product and the Two Halves* (`articles_maths/the-square-of-the-quaternionic-sesquilinear-product-and-the-two-halves.md`), for the identity $\tilde P\star\tilde P = (\overline{\tilde P}\tilde P)^{\natural}$ and the Krein form.
- *The Square Roots of a Central Value in the Four General Products* (`articles_maths/the-square-roots-of-a-central-value-in-the-four-general-products.md`), for the four-way comparison of the root sets.
- *Conventions in Mathematics* (`articles_maths/conventions-in-mathematics.md`), for the notation and the article format.
