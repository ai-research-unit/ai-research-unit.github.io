# __Nilpotents of the General Quaternionic Sesqualgebra__

## Introduction

The biquaternion algebra carries four general products on its complex space, and this article treats the **nilpotents** of the fourth, the **general quaternionic sesquilinear product**

$$
\tilde P \star \tilde Q = \tilde P^{\natural}\tilde Q^{*} ,
$$

whose rule and table are *Introduction to the General Quaternionic Sesqualgebra of Biquaternions*. A nilpotent is defined by a product, so the class belongs to the product; the definition for a general product $\star$, the index and the square-zero element are quoted from *Definitions for the Study of the 12 Algebraic Structures*, and the four-way comparison of the square-zero sets is *Zero Divisors*. What this article owns is the **GQS** square-zero family: the criterion, the parametrization, the real dimension, the non-purity and the contrast with the plain nilpotent cone.

The block is the one of the twelve whose nilpotents are **not** the plain ones and **not** the natural ones. The square-zero set of the plain product is the pure isotropic cone, of real dimension four; that of the natural product is the whole zero-divisor cone, of real dimension six; that of the general plain sesquilinear product is the origin alone. The GQS square-zero set is a fourth object, a real four-dimensional family lying in the **non-pure** part of the cone, incomparable with the plain cone and the proper part of the natural cone. This is the reading of the fourth row of the table of *Zero Divisors*.

**Conventions.** $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0 = 1, e_1, e_2, e_3$ with $e_1e_2 = e_3$ and central scalar imaginary $i$. An element is $\tilde Q = Q_0e_0 + \mathbf Q$, $\mathbf Q = \sum_{k=1}^{3}Q_ke_k$. The natural conjugation is $\tilde Q^{\natural} = Q_0-\mathbf Q$, the star is $\tilde Q^{*} = \overline{\tilde Q^{\natural}}$, and the Hermitian conjugation is $\overline{\tilde Q} = \tilde Q^{\natural*} = \tilde Q^{*\natural}$. The **central square** is $C(\tilde Q) = \sum_\mu Q_\mu^2$, with $C(\tilde Q)e_0 = \tilde Q\tilde Q^{\natural}$. The product is $\tilde P\star\tilde Q = \tilde P^{\natural}\tilde Q^{*}$, with the natural conjugation ${}^{\natural}$ in the first slot and the star ${}^{*}$ in the second; juxtaposition $\tilde P\tilde Q$ is the general plain bilinear product, the multiplication of the algebra. The dot and cross products of vector parts are the general plain bilinear ones, and $\hat\mu$ denotes a real unit vector, $\sum_k\hat\mu_k^2 = 1$.

## The Nilpotent of the Product

**Definition (nilpotent of a product, quoted).** Let $\star$ be a product on $\mathbb{B}$. An element $\tilde\Upsilon$ is a **nilpotent of $\star$** when some power of it vanishes, $\tilde\Upsilon^{\star k} = 0$ for some $k\geq1$, the power being read left-nested, $\tilde\Upsilon^{\star k} = (\cdots((\tilde\Upsilon\star\tilde\Upsilon)\star\tilde\Upsilon)\cdots\star\tilde\Upsilon)$; the least such $k$ is the **index of nilpotency**; and an element of index two, $\tilde\Upsilon\star\tilde\Upsilon = 0$ with $\tilde\Upsilon \neq 0$, is a **square-zero element of $\star$**. The origin is the trivial nilpotent. The definition is *Definitions for the Study of the 12 Algebraic Structures* §5 and §6.

Throughout this article the product is $\tilde P\star\tilde Q = \tilde P^{\natural}\tilde Q^{*}$, and, unqualified, **nilpotent** and **square-zero element** mean nilpotent of $\star$ and square-zero element of $\star$. The index-two family is the class the article classifies, and its relation to the higher index is stated at §*The Index*.

## The Square-Zero Equation

**Proposition (the reduction).** For every $\tilde Q$,

$$
\tilde Q\star\tilde Q = \bigl(\overline{\tilde Q}\,\tilde Q\bigr)^{\natural} ,
$$

so $\tilde Q\star\tilde Q = 0$ if and only if $\overline{\tilde Q}\,\tilde Q = 0$.

**Proof.** $\tilde Q\star\tilde Q = \tilde Q^{\natural}\tilde Q^{*}$, and $\tilde Q^{*} = \overline{\tilde Q^{\natural}}$, so $\tilde Q^{\natural}\tilde Q^{*} = \tilde Q^{\natural}\overline{\tilde Q^{\natural}}$. The map ${}^{\natural}$ is an anti-automorphism of the plain product, so $\tilde Q^{\natural}\overline{\tilde Q^{\natural}} = \bigl(\overline{\tilde Q^{\natural}}\,\tilde Q^{\natural}\bigr)^{\natural}$; and $\overline{\tilde Q^{\natural}} = \tilde Q^{*}$, $\overline{(\tilde Q^{\natural})^{\natural}} = \overline{\tilde Q}$, giving $\bigl(\tilde Q^{*}\tilde Q\bigr)^{\natural}$. The two readings $\tilde Q^{\natural}\overline{\tilde Q^{\natural}}$ and $\overline{\tilde Q}\tilde Q$ are the same element because $\overline{\tilde Q}\tilde Q = \overline{\tilde Q^{\natural}}\tilde Q^{\natural}$ up to the involution $\natural$ of the plain product, and applying $\natural$ to the vanishing equation is an equivalence. The identity is the one of *The Square of the General Quaternionic Sesquilinear Product and the Two Halves*, where it is proved on the coordinates.

**Proposition (the coordinate equations).** Write $\tilde Q = a + \mathbf u$ with $a = x_0+iy_0$ and $\mathbf u = \mathbf p+i\mathbf p'$, where $x_0,y_0\in\mathbb{R}$ and $\mathbf p,\mathbf p'\in\mathbb{R}^3$. Then $\tilde Q\star\tilde Q = 0$ if and only if

$$
x_0^2+y_0^2 = \lvert\mathbf p\rvert^2+\lvert\mathbf p'\rvert^2 , \qquad x_0\mathbf p+y_0\mathbf p' = 0 , \qquad \mathbf p\times\mathbf p' = 0 .
$$

**Proof.** The plain product $\overline{\tilde Q}\tilde Q = (\overline{a}+\overline{\mathbf u})(a+\mathbf u)$ has scalar part $\lvert a\rvert^2-(\overline{\mathbf u},\mathbf u)$ and vector part $\overline{a}\mathbf u+a\overline{\mathbf u}+\overline{\mathbf u}\times\mathbf u$. With $\overline{a} = x_0-iy_0$ and $\overline{\mathbf u} = \mathbf p-i\mathbf p'$ one computes $\overline{a}\mathbf u+a\overline{\mathbf u} = 2(x_0\mathbf p+y_0\mathbf p')$, a real vector, and $\overline{\mathbf u}\times\mathbf u = 2i\,\mathbf p\times\mathbf p'$. The scalar part is $x_0^2+y_0^2-\lvert\mathbf p\rvert^2-\lvert\mathbf p'\rvert^2$, and the vanishing of the scalar part and of the real and imaginary parts of the vector part is the displayed system.

## The Classification

**Theorem (the square-zero elements).** The square-zero elements of $\star$ are exactly the elements

$$
\tilde\Upsilon = c\bigl(\hat\mu + i\bigr) , \qquad c\in\mathbb{C}^{*} , \qquad \hat\mu\in\mathbb{R}^3 , \qquad \sum_{k=1}^{3}\hat\mu_k^2 = 1 ,
$$

together with the origin; equivalently, $\tilde\Upsilon = c\,(1 + i\hat\nu)$ over the complex numbers $c$ and the real unit vectors $\hat\nu$, and the two parametrizations agree under $\hat\nu\mapsto-\hat\mu$ and $c\mapsto ic$.

**Proof.** Let $\tilde Q = a+\mathbf u$ satisfy the coordinate system. The third equation $\mathbf p\times\mathbf p' = 0$ says that the real vectors $\mathbf p$ and $\mathbf p'$ are linearly dependent; when $\mathbf p' = 0$ this is automatic and it holds trivially when $\mathbf p = 0$. If $\mathbf p$ and $\mathbf p'$ are not both zero they are parallel to a common real unit vector $\hat\mu$, so $\mathbf u = c\,\hat\mu$ for a complex number $c$, and the second equation becomes $\operatorname{Re}(\overline{a}c)\,\hat\mu = 0$, that is $\operatorname{Re}(\overline{a}c) = 0$. When $a \neq 0$ this says that $c$ is a real multiple of $ia$, $c = ita$ with $t\in\mathbb{R}$; substituting into the first equation gives $\lvert a\rvert^2 = t^2\lvert a\rvert^2$, so $t^2 = 1$ and $c = \pm ia$; then $\tilde Q = a\pm ia\hat\mu = \pm ia(\hat\mu\mp i)$, of the displayed form. When $a = 0$ the first equation gives $\lvert c\rvert^2 = 0$, that is $c = 0$ and $\tilde Q = 0$, which is excluded for a square-zero element. The two parametrizations are related by $c(\hat\mu+i) = ic\,(1-i\hat\mu) = ic\,(1+i(-\hat\mu))$. Since $\hat\mu+i$ has square zero and the set is stable under the multiplication by a complex scalar (the scalar $c$ is central), every displayed element is square-zero, which proves the equivalence.

**Corollary (the real dimension and the two readings).** The square-zero elements form a real four-dimensional family, $c$ of two real parameters and $\hat\mu$ of two; and every square-zero element is **non-pure**,

$$
\Upsilon_0 = ic \neq 0 ,
$$

so the family lies in the non-pure part $Q_0\neq0$ of the zero-divisor cone.

**Proof.** The parametrization has $\mathbb{C}^{*}$ of real dimension two and the unit vectors $\hat\mu$ of real dimension two, and the scalar part of $c(\hat\mu+i)$ is $ic$, which vanishes only for $c = 0$.

**Example.** The elements $e_0+ie_1$, $e_0+ie_2$, $e_0+ie_3$ are square-zero, as are $ie_0\pm e_k$; the general member is $c(\hat\mu+i)$. The element $e_1+ie_2$ is **not** square-zero: its square is $-2e_0-2ie_3$, computed from the criterion $\overline{\tilde Q}\tilde Q = -2e_0+2ie_3$.

The classification answers the two questions that a square-zero theory asks. The **parametrization** is a complex line over each real direction, $c(\hat\mu+i)$ with $\hat\mu$ over the real unit vectors and $c$ over the complex scalars, so the family is the union of the complex lines based at the real unit directions, of real dimension four, and the square of every member of the family is the origin. The non-purity is the striking point: the square-zero elements of the plain product are pure, of vanishing scalar part, while here every one of them has scalar part $ic$, so the two square-zero sets share only the origin.

## The Index

**Proposition (the cube of a square-zero element vanishes).** If $\tilde\Upsilon\star\tilde\Upsilon = 0$ then $\tilde\Upsilon^{\star 3} = 0$ and every higher left-nested power vanishes; the index of a nonzero square-zero element is two.

**Proof.** $\tilde\Upsilon^{\star 3} = (\tilde\Upsilon\star\tilde\Upsilon)\star\tilde\Upsilon = 0\star\tilde\Upsilon = 0$, and the higher powers begin with a factor that already vanishes.

**Remark (the higher index).** The classification above is the classification of the index-two family, the family of the square-zero elements, which is the family of the fourth row of *Zero Divisors*. Whether the block has a nilpotent of index three, an element with $\tilde\Upsilon\star\tilde\Upsilon\neq0$ and $(\tilde\Upsilon\star\tilde\Upsilon)\star\tilde\Upsilon = 0$, is not claimed here: the reduction of the higher equation is the pair $\tilde\Upsilon\star\tilde\Upsilon = \tilde Z\neq0$ with $\tilde Z\star\tilde\Upsilon = 0$, the second equation forcing $C(\tilde\Upsilon) = 0$ by the zero-divisor criterion of the plain algebra; the computations performed do not exhibit a solution, and the question is recorded as unsettled in the companion notes of the article. The definitions article records that the index is not bounded by two in every product of the twelve; for the block the only index settled here is two.

## The Nilpotents and the Zero Divisors

**Theorem (the square-zero elements are two-sided zero divisors).** Every nonzero square-zero element $\tilde\Upsilon$ satisfies $\tilde\Upsilon\star\tilde\Upsilon = 0$, so it is a zero divisor of $\star$ with itself as partner on both sides, and it lies in the zero-divisor cone

$$
C(\tilde\Upsilon) = 0 .
$$

**Proof.** The relation $\tilde\Upsilon\star\tilde\Upsilon = 0$ is the product of the element with itself and exhibits the partner; the cone is the criterion of *Zero Divisors of the General Quaternionic Sesqualgebra*, and $\overline{\tilde\Upsilon}\tilde\Upsilon = 0$ implies $C(\tilde\Upsilon) = 0$.

The family is therefore a real four-dimensional subfamily of the real six-dimensional cone, and it is a **proper** subfamily: the pure zero divisor $e_1+ie_2$ of the cone is not square-zero. This is the difference between the block and the plain algebra. There, nilpotents and zero divisors are related by the criterion of the cone and every nilpotent is pure; here the nilpotents are exactly the square-zero elements, they lie in the non-pure family, and the cone is split into a pure part, where the square-zero condition is never met, and a non-pure part, where it cuts out the proper subfamily $c(\hat\mu+i)$.

## Summary

The nilpotents of the general quaternionic sesquilinear product $\tilde P\star\tilde Q = \tilde P^{\natural}\tilde Q^{*}$ are the elements whose square vanishes. The square reduces to the natural conjugate of the plain product, $\tilde Q\star\tilde Q = (\overline{\tilde Q}\tilde Q)^{\natural}$, so the square-zero equation is $\overline{\tilde Q}\tilde Q = 0$, whose coordinates are $x_0^2+y_0^2 = \lvert\mathbf p\rvert^2+\lvert\mathbf p'\rvert^2$, $x_0\mathbf p+y_0\mathbf p' = 0$ and $\mathbf p\times\mathbf p' = 0$ for $\tilde Q = x_0+iy_0+\mathbf p+i\mathbf p'$.

The square-zero elements are exactly the family $c(\hat\mu+i)$ over the complex numbers $c$ and the real unit vectors $\hat\mu$, equivalently the family $c(1+i\hat\nu)$; the family is real four-dimensional, it is the union of the complex lines based at the real unit directions, and every nonzero member is **non-pure**, with scalar part $ic$. Every square-zero element is a two-sided zero divisor with itself as partner, the family is a proper real four-dimensional subfamily of the real six-dimensional zero-divisor cone, and it is incomparable with the plain nilpotent cone because the plain square-zero elements are pure; the two square-zero sets share only the origin. The index of a nonzero square-zero element is two, and the question of a nilpotent of index three is left unsettled.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde P\star\tilde Q = \tilde P^{\natural}\tilde Q^{*}$ | the general quaternionic sesquilinear product |
| $\tilde\Upsilon$ | a nilpotent, $\tilde\Upsilon\star\tilde\Upsilon = 0$ |
| $\tilde Q\star\tilde Q = (\overline{\tilde Q}\tilde Q)^{\natural}$ | the reduction of the square |
| $C(\tilde Q) = \sum_\mu Q_\mu^2$ | the central square, $C(\tilde Q)e_0 = \tilde Q\tilde Q^{\natural}$ |
| $c(\hat\mu+i)$, $c\in\mathbb{C}^{*}$, $\hat\mu$ real unit | the square-zero family; equivalently $c(1+i\hat\nu)$ |
| $\Upsilon_0 = ic$ | the scalar part of a square-zero element, non-zero |
| $\mathbf p\times\mathbf p' = 0$, $x_0\mathbf p+y_0\mathbf p' = 0$ | the vector equations of the square-zero system |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the definition of the nilpotent, the index, the left-nested power and the square-zero element.
- *Zero Divisors* (`articles_maths/zero-divisors.md`), for the four square-zero sets, the chain and the incomparability this article reads in the fourth row.
- *Nilpotents of the General Plain Algebra* (`articles_maths/nilpotents-of-the-general-plain-algebra.md`), for the plain nilpotent cone, pure and of real dimension four, against which the GQS family is compared.
- *Nilpotents of the General Quaternionic Algebra* (`articles_maths/nilpotents-of-the-general-quaternionic-algebra.md`), for the natural product's square-zero set, the whole zero-divisor cone.
- *Zero Divisors of the General Quaternionic Sesqualgebra* (`articles_maths/zero-divisors-of-the-general-quaternionic-sesqualgebra.md`), for the cone, its two families and the criterion.
- *The Square of the General Quaternionic Sesquilinear Product and the Two Halves* (`articles_maths/the-square-of-the-quaternionic-sesquilinear-product-and-the-two-halves.md`), for the identity $\tilde Q\star\tilde Q = (\overline{\tilde Q}\tilde Q)^{\natural}$.
- *Introduction to the General Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-general-quaternionic-sesqualgebra-of-biquaternions.md`), for the product and its table.
- *Conventions in Mathematics* (`articles_maths/conventions-in-mathematics.md`), for the notation and the article format.
