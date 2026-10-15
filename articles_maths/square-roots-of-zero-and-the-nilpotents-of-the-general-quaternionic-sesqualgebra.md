# __Square Roots of Zero and the Nilpotents of the General Quaternionic Sesqualgebra__

## Introduction

The central value $0$ and the nilpotents are the two faces of one subject in the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$: a **root of zero** is a nonzero element $\tilde\Xi$ with $\tilde\Xi\star\tilde\Xi = 0$, a **nilpotent** is an element some power of which vanishes, and on the **general quaternionic sesquilinear product**

$$
\tilde P \star \tilde Q = \tilde P^{\natural}\tilde Q^{*}
$$

the two notions meet at the square-zero elements, since a nonzero root of zero and a nilpotent of index two are the same thing. The rule, scalar–vector form and table of the product are *Introduction to the General Quaternionic Sesqualgebra of Biquaternions*, and its place among the four general products is *The Four General Products of the Biquaternion $\mathbb{C}$ Space*. A root of a central value and a nilpotent are notions of a **product** and not of an algebra: the root of $\lambda$ is defined for a general product in *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* §6, and the nilpotent, its index and the square-zero element there as well, at §5 and §6. The article treats the roots of zero first and the nilpotents after, and it reads both from the square identity $\tilde Q\star\tilde Q = (\overline{\tilde Q}\tilde Q)^{\natural}$ of *The Square of the General Quaternionic Sesquilinear Product and the Two Halves*.

**What the article does not do.** The root set of a **general** central value and the reduction of the root equation are *Square Roots of One and the Idempotents of the General Quaternionic Sesqualgebra*, which classifies the roots of every real central value and proves the reduction; the present article is the value $\lambda = 0$ of that theorem, and it owns the square-zero family, its index and its place in the zero-divisor cone. The roots of a general element are *Square Roots of a General Element in the General Quaternionic Sesqualgebra*; the four-way comparison of the square-zero sets of the twelve general products is *Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*; and the cone and its criterion are *Zero Divisors of the General Quaternionic Sesqualgebra*.

**Conventions.** $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0 = 1, e_1, e_2, e_3$ with $e_1e_2 = e_3$ and central scalar imaginary $i$. An element is $\tilde Q = Q_0e_0 + \vec Q$, $\vec Q = \sum_{k=1}^{3}Q_ke_k$. The natural conjugation is $\tilde Q^{\natural} = Q_0-\vec Q$, the star is $\tilde Q^{*} = \overline{\tilde Q^{\natural}}$, and the Hermitian conjugation is $\overline{\tilde Q} = \tilde Q^{\natural*} = \tilde Q^{*\natural}$. The **central square** is $C(\tilde Q) = \sum_\mu Q_\mu^2$, with $C(\tilde Q)e_0 = \tilde Q\tilde Q^{\natural}$. The product throughout is the general quaternionic sesquilinear product $\tilde P\star\tilde Q = \tilde P^{\natural}\tilde Q^{*}$, with the natural conjugation ${}^{\natural}$ in the first slot and the star ${}^{*}$ in the second; the two **slot involutions** are ${}^{\natural}$ and ${}^{*}$. The juxtaposition $\tilde P\tilde Q$ is the general plain bilinear product, the multiplication of the algebra. The dot and cross products of vector parts are the general plain bilinear ones, and $\hat u$ denotes a real unit vector, $\sum_kn_k^2 = 1$.

**The results.** In the general quaternionic sesquilinear product the square reduces to $\tilde Q\star\tilde Q = (\overline{\tilde Q}\tilde Q)^{\natural}$, so the square-zero equation is $\overline{\tilde Q}\tilde Q = 0$, whose coordinates are $x_0^{2}+y_0^{2} = \lvert\vec p\rvert^{2}+\lvert\vec p'\rvert^{2}$, $x_0\vec p+y_0\vec p' = 0$ and $\vec p\times\vec p' = 0$ for $\tilde Q = x_0+iy_0+\vec p+i\vec p'$. The roots of zero are exactly the square-zero elements, the family $\tilde\Xi = c(\hat u+i)$ over the complex numbers $c$ and the real unit vectors $\hat u$, equivalently $c(1+\tilde\Xi_2)$; the family is real four-dimensional, it is the union of the complex lines based at the real unit directions, and every nonzero member is **non-pure**, with scalar part $ic$. Every square-zero element is a two-sided zero divisor with itself as partner, the family is a proper real four-dimensional subfamily of the real six-dimensional zero-divisor cone, and it is incomparable with the plain nilpotent cone because the plain square-zero elements are pure; the two square-zero sets share only the origin. The index of a nonzero square-zero element is two, and the question of a nilpotent of index three is left unsettled. Each section below states its result first and then proves it.

## The Roots of Zero

**A nonzero root of zero is exactly a square-zero element: it satisfies $\overline{\tilde Q}\tilde Q = 0$, and on coordinates the system $x_0^{2}+y_0^{2} = \lvert\vec p\rvert^{2}+\lvert\vec p'\rvert^{2}$, $x_0\vec p+y_0\vec p' = 0$, $\vec p\times\vec p' = 0$; the roots are exactly the family $c(\hat u+i)$, $c\in\mathbb{C}^{*}$, $\lvert\hat u\rvert = 1$, equivalently $c(1+\tilde\Xi_2)$, of real dimension four and non-pure.**

### The Square-Zero Equation

**Definition (root of a central value, quoted).** A **root of the central value $\lambda$** in a product $\star$ is a nonzero element $\tilde\Xi$ with $\tilde\Xi\star\tilde\Xi = \lambda e_0$; a **root of zero** is a root of $0$. The definition is *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* §6.

**Proposition (the reduction, quoted).** For every $\tilde Q$,

$$
\tilde Q\star\tilde Q = \bigl(\overline{\tilde Q}\,\tilde Q\bigr)^{\natural} ,
$$

so $\tilde Q$ is a root of zero if and only if $\overline{\tilde Q}\,\tilde Q = 0$; the identity is proved on the coordinates in *Square Roots of One and the Idempotents of the General Quaternionic Sesqualgebra* §*The Reduction of the Root Equation*, and the equation $\overline{\tilde Q}\tilde Q = 0$ is the square-zero equation of this article.

**Proposition (the coordinate equations).** Write $\tilde Q = a + \vec u$ with $a = x_0+iy_0$ and $\vec u = \vec p+i\vec p'$, where $x_0,y_0\in\mathbb{R}$ and $\vec p,\vec p'\in\mathbb{R}^3$. Then $\tilde Q\star\tilde Q = 0$ if and only if

$$
x_0^2+y_0^2 = \lvert\vec p\rvert^2+\lvert\vec p'\rvert^2 , \qquad x_0\vec p+y_0\vec p' = 0 , \qquad \vec p\times\vec p' = 0 .
$$

**Proof.** The plain product $\overline{\tilde Q}\tilde Q = (\overline{a}+\overline{\vec u})(a+\vec u)$ has scalar part $\lvert a\rvert^2-(\overline{\vec u},\vec u)$ and vector part $\overline{a}\vec u+a\overline{\vec u}+\overline{\vec u}\times\vec u$. With $\overline{a} = x_0-iy_0$ and $\overline{\vec u} = \vec p-i\vec p'$ one computes $\overline{a}\vec u+a\overline{\vec u} = 2(x_0\vec p+y_0\vec p')$, a real vector, and $\overline{\vec u}\times\vec u = 2i\,\vec p\times\vec p'$. The scalar part is $x_0^2+y_0^2-\lvert\vec p\rvert^2-\lvert\vec p'\rvert^2$, and the vanishing of the scalar part and of the real and imaginary parts of the vector part is the displayed system. The computation is the coordinate proposition of *Square Roots of One and the Idempotents of the General Quaternionic Sesqualgebra*, read at $\lambda = 0$.

### The Classification of the Roots of Zero

**The roots of zero are exactly the elements $\tilde\Xi = c(\hat u+i)$ with $c\in\mathbb{C}^{*}$ and $\hat u$ a real unit vector, equivalently $\tilde\Xi = c(1+\tilde\Xi_2)$, together with the origin; they form a real four-dimensional family, the union of the complex lines based at the real unit directions, and every nonzero member is non-pure with scalar part $i c$.**

**Theorem (the roots of zero).** The roots of zero of $\star$ are exactly the elements

$$
\tilde\Xi = c\bigl(\hat u + i\bigr) , \qquad c\in\mathbb{C}^{*} , \qquad \hat u\in\mathbb{R}^3 , \qquad \sum_{k=1}^{3}n_k^2 = 1 ,
$$

together with the origin; equivalently, $\tilde\Xi = c\,(1 + \tilde\Xi_2)$ over the complex numbers $c$ and the real unit vectors $\hat m$, and the two parametrizations agree under $\hat m\mapsto-\hat u$ and $c\mapsto ic$.

**Proof.** Let $\tilde Q = a+\vec u$ satisfy the coordinate system. The third equation $\vec p\times\vec p' = 0$ says that the real vectors $\vec p$ and $\vec p'$ are linearly dependent; when $\vec p' = 0$ this is automatic and it holds trivially when $\vec p = 0$. If $\vec p$ and $\vec p'$ are not both zero they are parallel to a common real unit vector $\hat u$, so $\vec u = c\,\hat u$ for a complex number $c$, and the second equation becomes $\operatorname{Re}(\overline{a}c)\,\hat u = 0$, that is $\operatorname{Re}(\overline{a}c) = 0$. When $a \neq 0$ this says that $c$ is a real multiple of $ia$, $c = ita$ with $t\in\mathbb{R}$; substituting into the first equation gives $\lvert a\rvert^2 = t^2\lvert a\rvert^2$, so $t^2 = 1$ and $c = \pm ia$; then $\tilde Q = a\pm ia\hat u = \pm ia(\hat u\mp i)$, of the displayed form. When $a = 0$ the first equation gives $\lvert c\rvert^2 = 0$, that is $c = 0$ and $\tilde Q = 0$, which is excluded for a root of zero. The two parametrizations are related by $c(\hat u+i) = ic\,(1-\tilde\Xi) = ic\,(1+i(-\hat u))$. Since $\hat u+i$ has square zero and the set is stable under the multiplication by a complex scalar (the scalar $c$ is central), every displayed element is square-zero, which proves the equivalence.

**Corollary (the real dimension and the two readings).** The roots of zero form a real four-dimensional family, $c$ of two real parameters and $\hat u$ of two; and every root of zero is **non-pure**,

$$
\Xi_0 = ic \neq 0 ,
$$

so the family lies in the non-pure part $Q_0\neq0$ of the zero-divisor cone.

**Proof.** The parametrization has $\mathbb{C}^{*}$ of real dimension two and the unit vectors $\hat u$ of real dimension two, and the scalar part of $c(\hat u+i)$ is $ic$, which vanishes only for $c = 0$.

**Example.** The elements $e_0+ie_1$, $e_0+ie_2$, $e_0+ie_3$ are square-zero, as are $ie_0\pm e_k$; the general member is $c(\hat u+i)$. The element $e_1+ie_2$ is **not** square-zero: its square is $-2e_0-2ie_3$, computed from the criterion $\overline{\tilde Q}\tilde Q = -2e_0+2ie_3$.

The classification answers the two questions that a root-of-zero theory asks. The **parametrization** is a complex line over each real direction, $c(\hat u+i)$ with $\hat u$ over the real unit vectors and $c$ over the complex scalars, so the family is the union of the complex lines based at the real unit directions, of real dimension four, and the square of every member of the family is the origin. The non-purity is the striking point: the square-zero elements of the plain product are pure, of vanishing scalar part, while here every one of them has scalar part $ic$, so the two square-zero sets share only the origin.

### The Roots of Zero and the Zero Divisors

**Every root of zero is a two-sided zero divisor with itself as partner, lying on the cone $C(\tilde\Xi)=0$, so the family is a proper real four-dimensional subfamily of the real six-dimensional cone, its complement containing the pure zero divisor $e_1+ie_2$.**

**Theorem (the roots of zero are two-sided zero divisors).** Every root of zero $\tilde\Xi$ satisfies $\tilde\Xi\star\tilde\Xi = 0$, so it is a zero divisor of $\star$ with itself as partner on both sides, and it lies in the zero-divisor cone

$$
C(\tilde\Xi) = 0 .
$$

**Proof.** The relation $\tilde\Xi\star\tilde\Xi = 0$ is the product of the element with itself and exhibits the partner; the cone is the criterion of *Zero Divisors of the General Quaternionic Sesqualgebra*, and $\overline{\tilde\Xi}\tilde\Xi = 0$ implies $C(\tilde\Xi) = 0$.

The family is therefore a real four-dimensional subfamily of the real six-dimensional cone, and it is a **proper** subfamily: the pure zero divisor $e_1+ie_2$ of the cone is not square-zero, its square being $-2e_0-2ie_3$. This is the difference between the block and the plain algebra. There, every square-zero element is pure; here the square-zero elements are exactly the roots of zero, they lie in the non-pure family, and the cone is split into a pure part, where the square-zero condition is never met, and a non-pure part, where it cuts out the proper subfamily $c(\hat u+i)$.

## The Nilpotents of the Product

**The nonzero roots of zero are exactly the nilpotents of index two of the product, and every higher left-nested power of such an element vanishes; whether the product has a nilpotent of index three is left unsettled.**

**Definition (nilpotent of a product, quoted).** Let $\star$ be a product on $\mathbb{B}$. An element $\tilde\Upsilon$ is a **nilpotent of $\star$** when some power of it vanishes, $\tilde\Upsilon^{\star k} = 0$ for some $k\geq1$, the power being read left-nested, $\tilde\Upsilon^{\star k} = (\cdots((\tilde\Upsilon\star\tilde\Upsilon)\star\tilde\Upsilon)\cdots\star\tilde\Upsilon)$; the least such $k$ is the **index of nilpotency**; and an element of index two, $\tilde\Upsilon\star\tilde\Upsilon = 0$ with $\tilde\Upsilon \neq 0$, is a **square-zero element of $\star$**. The origin is the trivial nilpotent. The definition is *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* §5 and §6.

Throughout this article the product is $\tilde P\star\tilde Q = \tilde P^{\natural}\tilde Q^{*}$, and, unqualified, **nilpotent** and **square-zero element** mean nilpotent of $\star$ and square-zero element of $\star$. Every root of zero is a square-zero element and no square-zero element is the origin, so the classification of §*The Classification of the Roots of Zero* is the classification of the nonzero nilpotents of index two.

**Proposition (the cube of a square-zero element vanishes).** If $\tilde\Upsilon\star\tilde\Upsilon = 0$ then $\tilde\Upsilon^{\star 3} = 0$ and every higher left-nested power vanishes; the index of a nonzero square-zero element is two.

**Proof.** $\tilde\Upsilon^{\star 3} = (\tilde\Upsilon\star\tilde\Upsilon)\star\tilde\Upsilon = 0\star\tilde\Upsilon = 0$, and the higher powers begin with a factor that already vanishes.

**Remark (the higher index).** The classification above is the classification of the index-two family, the family of the roots of zero, which is the family of the fourth row of *Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*. Whether the product has a nilpotent of index three, an element with $\tilde\Upsilon\star\tilde\Upsilon\neq0$ and $(\tilde\Upsilon\star\tilde\Upsilon)\star\tilde\Upsilon = 0$, is not claimed here: the reduction of the higher equation is the pair $\tilde\Upsilon\star\tilde\Upsilon = \tilde Z\neq0$ with $\tilde Z\star\tilde\Upsilon = 0$, the second equation forcing $C(\tilde\Upsilon) = 0$ by the zero-divisor criterion of the plain algebra; the computations performed do not exhibit a solution, and the question is recorded as unsettled. The definitions article records that the index is not bounded by two in every product of the twelve; for the block the only index settled here is two.

## Summary

The roots of zero of the general quaternionic sesquilinear product $\tilde P\star\tilde Q = \tilde P^{\natural}\tilde Q^{*}$ are the nonzero elements whose square vanishes, and the square reduces to the natural conjugate of the plain product, $\tilde Q\star\tilde Q = (\overline{\tilde Q}\tilde Q)^{\natural}$, so the square-zero equation is $\overline{\tilde Q}\tilde Q = 0$, whose coordinates are $x_0^2+y_0^2 = \lvert\vec p\rvert^2+\lvert\vec p'\rvert^2$, $x_0\vec p+y_0\vec p' = 0$ and $\vec p\times\vec p' = 0$ for $\tilde Q = x_0+iy_0+\vec p+i\vec p'$.

The roots of zero are exactly the family $c(\hat u+i)$ over the complex numbers $c$ and the real unit vectors $\hat u$, equivalently the family $c(1+\tilde\Xi_2)$; the family is real four-dimensional, it is the union of the complex lines based at the real unit directions, and every nonzero member is **non-pure**, with scalar part $ic$. The nonzero roots of zero are exactly the nilpotents of index two, and every higher left-nested power of such an element vanishes. Every root of zero is a two-sided zero divisor with itself as partner, the family is a proper real four-dimensional subfamily of the real six-dimensional zero-divisor cone, and it is incomparable with the plain nilpotent cone because the plain square-zero elements are pure; the two square-zero sets share only the origin. The index of a nonzero square-zero element is two, and the question of a nilpotent of index three is left unsettled.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde P\star\tilde Q = \tilde P^{\natural}\tilde Q^{*}$ | the general quaternionic sesquilinear product |
| root of zero | a nonzero $\tilde\Xi$ with $\tilde\Xi\star\tilde\Xi = 0$ |
| $\tilde\Upsilon$ | a nilpotent, $\tilde\Upsilon^{\star k} = 0$ for some $k\geq1$ |
| $\tilde Q\star\tilde Q = (\overline{\tilde Q}\tilde Q)^{\natural}$ | the reduction of the square |
| $C(\tilde Q) = \sum_\mu Q_\mu^2$ | the central square, $C(\tilde Q)e_0 = \tilde Q\tilde Q^{\natural}$ |
| $c(\hat u+i)$, $c\in\mathbb{C}^{*}$, $\hat u$ real unit | the square-zero family; equivalently $c(1+\tilde\Xi_2)$ |
| $\Xi_0 = ic$ | the scalar part of a square-zero element, non-zero |
| $\vec p\times\vec p' = 0$, $x_0\vec p+y_0\vec p' = 0$ | the vector equations of the square-zero system |

## Further Reading

- *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternion-c-space.md`), for the root of a central value, the nilpotent, the index, the left-nested power and the square-zero element.
- *Square Roots of One and the Idempotents of the General Quaternionic Sesqualgebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-general-quaternionic-sesqualgebra.md`), for the reduction of the root equation and the classification of the roots of a real central value, of which this article is the value $0$.
- *Square Roots of a General Element in the General Quaternionic Sesqualgebra* (`articles_maths/square-roots-of-a-general-element-in-the-general-quaternionic-sesqualgebra.md`), for the general square-root problem and the statement that a nonzero root of zero is never a square.
- *Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/zero-divisors-in-the-algebraic-structures-over-the-biquaternion-c-space.md`), for the four square-zero sets, the chain and the incomparability this article reads in the fourth row.
- *Nilpotents of the General Plain Algebra* (`articles_maths/nilpotents-of-the-general-plain-algebra-of-quaternions.md`), for the plain nilpotent cone, pure and of real dimension four, against which the family is compared.
- *Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-general-quaternionic-algebra-of-quaternions.md`), for the natural product's square-zero set, the whole zero-divisor cone.
- *Zero Divisors of the General Quaternionic Sesqualgebra* (`articles_maths/zero-divisors-of-the-general-quaternionic-sesqualgebra.md`), for the cone, its two families and the criterion.
- *The Square of the General Quaternionic Sesquilinear Product and the Two Halves* (`articles_maths/the-square-of-the-quaternionic-sesquilinear-product-and-the-two-halves.md`), for the identity $\tilde Q\star\tilde Q = (\overline{\tilde Q}\tilde Q)^{\natural}$.
- *Conventions in Mathematics* (`articles_maths/conventions-in-mathematics.md`), for the notation and the article format.
