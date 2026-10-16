# __Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra__

## Introduction

This article classifies the square roots of the central value $0$ in the general quaternionic bilinear
product, and then the **nilpotents** of that product, the elements some power of which vanishes in the same
product.

Both notions name a product, and throughout this article the product is the general quaternionic bilinear
product $\tilde p\star\tilde q=\tilde p^{\natural}\tilde q$ of the general quaternionic algebra, the
$\mathrm{GQA}$ of *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*; the square of the
article is the square of $\star$, and an unqualified *nilpotent* is a nilpotent of $\star$. The general
definition of the square and of the roots of a central value, and the general definition of a nilpotent, are
*Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*, §*The Element Vocabulary*.

The whole article is settled by one computation, the square of every element being the central element
$N(\tilde p)e_0$. The root equation of the value $0$ therefore reads $N(\tilde p)=0$, and the nilpotent
equation is decided by the same scalar. Over $\mathbb{R}$ the norm is a sum of four squares, so it vanishes
only at the origin; the roots of $0$ are the single element $0$, and the product has **no nilpotent at all**,
of index two or of any larger index. The absence is the collapse of the complex sibling, where the root set
of $0$ is the whole zero-divisor cone.

**The results.** The root of $0$ in the general quaternionic product is the origin alone,
$\{\tilde\xi:\tilde\xi\star\tilde\xi=0\}=\{\tilde\xi:N(\tilde\xi)=0\}=\{0\}$, and the root set coincides with
the zero set of the norm and with the square-zero set. The square-zero set is the origin alone, so the
product has no square-zero element and no nilpotent; the absence is proved for every index, through the power
identity $\tilde p^{k}=N(\tilde p)(\tilde p^{\natural})^{(k-2)}$ and the plain division property, and not
for the index two alone. Neither remarkable subspace, the centre nor the vector subspace, carries a
square-zero element. Against the six structures of the real chapter the general quaternionic structure is one
of the four whose square-zero set is the origin, the other two being the whole space; against the twelve
structures of the complex chapter, whose square-zero sets are ordered through the cone, the real block
records the collapse of that cone to its apex.

**Boundaries.** The product, the square and the reduction of the root equation are *Introduction to the
General Quaternionic Algebra of Quaternions* and *Square Roots of One and the Idempotents of the General
Quaternionic Algebra*; the norm, its definiteness and the plain division property are *Norm and Invertibility
in the General Quaternionic Algebra* and *Norm and Invertibility in the General Plain Algebra*; the zero
divisors are *Zero Divisors of the General Quaternionic Algebra*; the idempotents are *Square Roots of One
and the Idempotents of the General Quaternionic Algebra*; the structure-level comparison of the six
square-zero sets is *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the
Quaternioid $\mathbb{R}$ Space*, and the ordering of the twelve complex sets is quoted from *Square Roots of
Zero and the Nilpotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*; the
definiteness of the form is *The Isotropic Structure of the General Quaternionic Algebra*; the
general root problem for an arbitrary radicand is *Square Roots of a General Element in the General
Quaternionic Algebra*.

**Conventions.** $\mathbb{H}$ is the real quaternion algebra with basis $e_0=1,e_1,e_2,e_3$, the rules
$e_k^2=-e_0$ and $e_1e_2=e_3$. Juxtaposition is the plain product and $\star$ the general quaternionic
bilinear product $\tilde p\star\tilde q=\tilde p^{\natural}\tilde q$, with the conjugation
$\tilde p^{\natural}=p_0-\vec p$ and $\tilde p=p_0e_0+\vec p$,
$\vec p=p_1e_1+p_2e_2+p_3e_3$. The **powers** are the left-nested products $\tilde p^{1}=\tilde p$ and
$\tilde p^{k+1}=\tilde p\star\tilde p^{k}$, and the **plain powers** are the same nestings in the plain
product, written $\tilde p^{(k)}$, with $\tilde p^{(0)}=e_0$. The **algebraic norm** is

$$
N(\tilde p)=\tilde p^{\natural}\tilde p=p_0^2+\lvert\vec p\rvert^2=\sum_{\mu=0}^{3}p_\mu^2 ,
$$

positive definite, with polar form $\beta(\tilde p,\tilde q)=p_0q_0+\vec p\cdot\vec q$. The centre is
the scalar line $\mathbb{R}_{\mathbb{H}}=\mathbb{R}e_0$ and the vector subspace is
$\mathrm{Vect}(\mathbb{H})=\{\vec p\}$.

## The Roots of Zero

**The root of $0$ is the origin alone, and the root set is the zero set of the norm and the square-zero set
of the product: the cone of the complex sibling has collapsed to its apex.**

### The Root Set

**Theorem (the root set of $0$).** The roots of $0$ in the general quaternionic product are the solutions of

$$
\tilde\xi\star\tilde\xi=0 \iff N(\tilde\xi)=0 ,
$$

and the solution set is the single element $\tilde\xi=0$.

**Proof.** The reduction of the root equation of a central value is *Square Roots of One and the Idempotents
of the General Quaternionic Algebra*, §*The Root Equation and Its Reduction*, which reads
$\tilde\xi\star\tilde\xi=\lambda e_0$ as the single equation $N(\tilde\xi)=\lambda$; at $\lambda=0$ this is
$N=0$. The norm is a sum of four real squares, so $N(\tilde\xi)=0$ forces every coordinate to vanish, that
is $\tilde\xi=0$; the norm is positive definite (*Norm and Invertibility in the General Quaternionic
Algebra*), and the origin is its only zero.

**Corollary (the coincidence).** The root set of $0$, the zero set of the norm and the square-zero set of the
product coincide, and the common set is the origin:

$$
\{\tilde\xi:\tilde\xi\star\tilde\xi=0\}=\{\tilde\xi:N(\tilde\xi)=0\}=\{0\} .
$$

**Proof.** The first equality is the theorem and the second is the definiteness of the norm; the square-zero
set is by definition the set $\{\tilde\xi:\tilde\xi\star\tilde\xi=0\}$, so it is the same set.

### The Comparison with the Plain Product

The same level set is read side by side with the plain product, and over $\mathbb{R}$ the two agree.

| value $\lambda$ | quaternionic $\tilde\xi\star\tilde\xi$ | plain $\tilde\xi^2$ |
|---|---|---|
| $0$ | $\{0\}$ alone | $\{0\}$ alone |

**Proposition.** Over $\mathbb{R}$ the root set of $0$ is the origin for the quaternionic product and for the
plain product alike; both algebras are division algebras, and neither has a square-zero element.

**Proof.** The quaternionic column is §*The Root Set*. For the plain column the plain square is
$(\xi_0^2-\lvert\vec\xi\rvert^2)e_0+2\xi_0\vec\xi$; the equation $\tilde\xi^2=0$ is the pair
$\xi_0^2=\lvert\vec\xi\rvert^2$ and $\xi_0\vec\xi=0$. If $\xi_0\neq0$ then $\vec\xi=0$
and $\xi_0^2=0$, a contradiction; hence $\xi_0=0$ and then $\lvert\vec\xi\rvert^2=0$, so
$\tilde\xi=0$. The plain column is *Square Roots of Zero and the Nilpotents of the General Plain Algebra*.

**Remark (the collapse of the complex root set).** In the complex chapter the root set of $0$ of the
quaternionic product is the whole zero-divisor cone $\{N=0\}$, of real dimension six, whose pure part is a
cone of real dimension four and whose non-pure part is the family of the plain-idempotent multiples. Over
$\mathbb{R}$ the cone has no nonzero point and shrinks to its apex, the origin; the collapse is the
definiteness of the quaternionic form (*The Isotropic Structure of the General Quaternionic Algebra*), and
it is the same fact that removes the zero divisors (*Zero Divisors of the General Quaternionic Algebra*) and
the isotropic directions. The complex sibling is *Square Roots of Zero and the Nilpotents of the General
Quaternionic Algebra*.

## The Definition and the Criterion

**The square-zero set of the product is the origin alone, so the product has no square-zero element and no
nilpotent of index two.**

**Definition.** Let $\star$ be a product on $\mathbb{H}$ and let $\tilde\nu\in\mathbb{H}$. The element
$\tilde\nu$ is **nilpotent of $\star$** when $\tilde\nu\neq0$ and $\tilde\nu^{k}=0$ for some positive integer
$k$; the least such $k$ is the **index**. The case $k=2$ is a **square-zero** element, and the **square-zero
set** of the product is the solution set of $\tilde\nu\star\tilde\nu=0$. The definition is *Definitions for
the Study of the Algebraic Structures*, §*The Element Vocabulary*; the origin is not a nilpotent, the
class taking its nonzero members. Throughout this article the product is $\star$.

**Lemma (the square is central).** For every $\tilde p\in\mathbb{H}$,

$$
\tilde p\star\tilde p=\tilde p^{\natural}\tilde p=N(\tilde p)\,e_0 , \qquad
N(\tilde p)=p_0^2+p_1^2+p_2^2+p_3^2 .
$$

**Proof.** At equal arguments the vector part of the product is
$p_0\vec p-p_0\vec p-\vec p\times\vec p=0$, so the square is the scalar part
$p_0^2+\vec p\cdot\vec p$ times $e_0$ (*Introduction to the General Quaternionic Algebra of
Quaternions*, and *Square Roots of One and the Idempotents of the General Quaternionic Algebra*).

**Theorem (the criterion).** For $\tilde p\in\mathbb{H}$, $\tilde p\star\tilde p=0$ if and only if
$N(\tilde p)=0$, that is if and only if $\tilde p=0$. The square-zero set of the general quaternionic
product is the single point $\{0\}$, and the product has no square-zero element.

**Proof.** By the lemma $\tilde p\star\tilde p=N(\tilde p)e_0$, which vanishes exactly when
$N(\tilde p)=0$. The norm is a sum of four real squares, so it vanishes only at $\tilde p=0$; the norm is
positive definite, and the criterion is met by the origin alone. The origin has vanishing square but is not a
nilpotent, the nilpotent class taking the nonzero members.

## No Nilpotent of Any Index

**Every element with a vanishing power is the origin, so the general quaternionic product has no nilpotent of
any index and its nilpotent class is empty.**

The square-zero case does not by itself exclude a nilpotent of larger index, since the definition asks for
some power, not the second. The following computation closes the question.

**Lemma (the powers).** For every $\tilde p\in\mathbb{H}$ and every $k\geq2$,

$$
\tilde p^{k}=N(\tilde p)\,\bigl(\tilde p^{\natural}\bigr)^{(k-2)} ,
$$

where the factor on the right is the plain power of order $k-2$ of $\tilde p^{\natural}$.

**Proof.** By induction on $k$. For $k=2$ the identity is the central square
$\tilde p^{2}=N(\tilde p)e_0=N(\tilde p)(\tilde p^{\natural})^{(0)}$. Assume it for $k$; then, using the
plain associativity inside the power,

$$
\tilde p^{k+1}=\tilde p\star\tilde p^{k}
=\tilde p^{\natural}\bigl(N(\tilde p)(\tilde p^{\natural})^{(k-2)}\bigr)
=N(\tilde p)\,(\tilde p^{\natural})^{(k-1)} ,
$$

which is the identity of order $k+1$.

**Theorem (no nilpotent).** Every $\tilde p\in\mathbb{H}$ with $\tilde p^{k}=0$ for some positive integer $k$
is $\tilde p=0$. The general quaternionic product has no nilpotent of any index, and its nilpotent class is
empty.

**Proof.** For $k=1$ the assertion is the definition. For $k=2$ it is the criterion of §*The Definition and
the Criterion*. Let $k\geq3$. By the power lemma
$\tilde p^{k}=N(\tilde p)(\tilde p^{\natural})^{(k-2)}=0$, so either $N(\tilde p)=0$ or
$(\tilde p^{\natural})^{(k-2)}=0$. In the first case $\tilde p=0$ by definiteness. In the second, the plain
powers of a nonzero quaternion do not vanish: if $\tilde x^{(m)}=0$ with $m\geq1$ and $\tilde x\neq0$, left
multiplication by the plain inverse $\tilde x^{-1}$ lowers the exponent, and iteration gives $\tilde x=0$, a
contradiction. Hence $\tilde p^{\natural}=0$ and $\tilde p=0$. The plain division property used here is
*Norm and Invertibility in the General Plain Algebra*.

**Corollary (the index).** No element of the block has nilpotency index two or more, and the square-zero
set, the nilpotent class and the class of elements of finite nilpotency index are $\{0\}$, $\varnothing$ and
$\{0\}$ respectively.

**Remark (the absence stated).** The class of nilpotents of the block is empty, and the article states the
absence and its reason and stops there. It does not import the nilpotent cone of the complex sibling, whose
square-zero set is the whole cone $\{N=0\}$: over $\mathbb{R}$ the cone has collapsed to a point, and the
class has no content. The empty nilpotent class and the empty zero-divisor set of *Zero Divisors of the
General Quaternionic Algebra* are the same definiteness, read on the equation $N=0$.

## The Nilpotents and the Roots of the Three Central Values

The root set of a central value is the solution set of $\tilde\xi\star\tilde\xi=c$ with $c$ central; the
square-zero set is the value $0$, and the value $0$ is the only central value whose root set degenerates to
the origin.

**Theorem (the three central values).** The root sets of the central values $-e_0$, $0$ and $+e_0$ are

$$
\{\tilde\xi:\tilde\xi\star\tilde\xi=-e_0\}=\varnothing,\qquad
\{\tilde\xi:\tilde\xi\star\tilde\xi=0\}=\{0\},\qquad
\{\tilde\xi:\tilde\xi\star\tilde\xi=+e_0\}=\mathrm{Sp}(1) ,
$$

the first empty, the third the unit sphere of real dimension three. The statement and the reduction are
*Square Roots of One and the Idempotents of the General Quaternionic Algebra*, §*The Roots of Plus One*; the
root set of $0$ is §*The Root Set* of this article.

**Proof.** The three equations are $N(\tilde\xi)=-1$, $N(\tilde\xi)=0$ and $N(\tilde\xi)=1$; the norm is
positive definite, so the first has no solution, the second has the origin alone, and the third is the
norm-one level set, the sphere $\mathrm{Sp}(1)$.

**Corollary.** The square-zero set is the root set of $0$ and is strictly smaller than the root set of
$+e_0$, and the nilpotents, which are its nonzero members, do not exist; the element $0$ is at the same time
the only root of $0$ and the only idempotent that is not the left unit.

## The Nilpotents on the Remarkable Subspaces

The square-zero equation is the vanishing of the norm, and the norm is read on the two remarkable subspaces
of $\mathbb{H}$, the scalar line $\mathbb{R}_{\mathbb{H}}=\mathbb{R}e_0$, the centre, and the vector subspace
$\mathrm{Vect}(\mathbb{H})$.

**Proposition.** On the centre and on the vector subspace the square vanishes only at the origin, so neither
subspace carries a square-zero element and neither carries a nilpotent; in the centre the square is
$A^2e_0$, and in the vector subspace it is the central element $\lvert\vec p\rvert^2e_0\neq0$ for every
nonzero pure $\vec p$.

| subspace | element | square | nilpotents |
|---|---|---|---|
| $\mathbb{R}_{\mathbb{H}}$, the centre | $Ae_0$ | $A^2e_0$ | none |
| $\mathrm{Vect}(\mathbb{H})$, the vector subspace | $\vec p$ | $\lvert\vec p\rvert^2e_0$ | none |

**Proof.** The square is the norm on the subspace of each row, by the lemma; $A^2$ vanishes only at $A=0$
and $\lvert\vec p\rvert^2$ only at $\vec p=0$. A nonzero pure element has a central nonzero square, so
no pure element is square-zero, and no central element is either.

## The Nilpotents and the Other Structures of the Space

The comparison of the six square-zero sets is *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*, the structure-level article of the real chapter, and its
verdict for the block is the origin alone.

**Theorem (the six square-zero sets).** Among the six structures of the quaternion real space the square-zero
set is $\{0\}$ for the general plain algebra, the symmetric plain algebra, the general quaternionic algebra
and the symmetric quaternionic algebra, and it is the whole space $\mathbb{H}$ for the two antisymmetric
structures. Only two square-zero sets occur, and the general quaternionic structure is one of the four with
the origin alone.

**Proof.** The four rows are the theorem of *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*, §*The Six Root Sets of $0$, Which Are the Six
Square-Zero Sets*, where the plain square is anisotropic
and the quaternionic square is the definite norm; the two alternating rows are the same theorem, the
products being alternating. The four structures with the origin alone are exactly those whose square is the
plain square or the central element $N(\tilde x)e_0$, neither of which vanishes off the origin over
$\mathbb{R}$.

**Remark (the complex ordering and the real collapse).** The complex chapter carries twelve structures and
its comparison article orders the square-zero sets through the cone,
$Z_3=\{0\}\subsetneq Z_1\subsetneq Z_2$ and $Z_3\subsetneq Z_4\subsetneq Z_2$ for the four general products
(*Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$
Space*, §*The Order of the Four Sets*), and it places the general quaternionic and the symmetric quaternionic
structures at the whole cone. Over
$\mathbb{R}$ the cone has become a point, so the general quaternionic set drops from the whole cone to the
origin and joins the three real structures whose square vanishes only at the origin; the ordering through the
cone disappears with the cone, and only the two extreme sets, the origin and the whole space, survive. The
collapse is the same definiteness that carries the zero-divisor set of the block from the punctured cone to
the empty set.

## Summary

In the general quaternionic bilinear product the square of every element is the central element
$N(\tilde p)e_0$, and the square vanishes exactly when the norm does. Over $\mathbb{R}$ the norm is a sum of
four squares, hence positive definite, so the root set of $0$ is the origin alone, the square-zero set is the
origin alone, and the product has **no nilpotent**, of index two or of any larger index. The absence is not a
consequence of the square-zero case alone: the powers satisfy
$\tilde p^{k}=N(\tilde p)(\tilde p^{\natural})^{(k-2)}$ for $k\geq2$, so a vanishing power forces either a
vanishing norm or a vanishing plain power, and neither occurs off the origin because the plain algebra is a
division algebra. The root set of $0$ coincides with the zero set of the norm and is strictly smaller than
the root set of $+e_0$, the sphere $\mathrm{Sp}(1)$; the root set of $-e_0$ is empty. Neither remarkable
subspace, the centre nor the vector subspace, carries a square-zero element. Against the six structures of
the real chapter the general quaternionic structure is one of the four whose square-zero set is the origin,
the other two being the whole space; against the twelve structures of the complex chapter, whose square-zero
sets are ordered through the cone, the real block records the collapse of that cone to a point, the same
definiteness that removes the zero divisors.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde p\star\tilde q=\tilde p^{\natural}\tilde q$ | the general quaternionic bilinear product |
| $\tilde\nu$ | a nilpotent of the product; the class is empty |
| $\tilde p^{k}$ | the left-nested power, $\tilde p^{k+1}=\tilde p\star\tilde p^{k}$ |
| $\tilde p^{(k)}$ | the plain power of order $k$ |
| $\tilde p\star\tilde p=N(\tilde p)e_0$ | the square, always central |
| $N(\tilde p)=\sum_\mu p_\mu^2$ | the quaternionic bilinear algebraic norm, positive definite |
| $\{0\}$ | the root set of $0$, the zero set of the norm, the square-zero set |
| $\varnothing$ | the nilpotent class of the block, and the root set of $-e_0$ |
| $\mathrm{Sp}(1)$ | the root set of $+e_0$, the unit sphere of dimension three |
| $\tilde p^{k}=N(\tilde p)(\tilde p^{\natural})^{(k-2)}$, $k\geq2$ | the power identity that excludes nilpotents of every index |
| $\mathbb{R}_{\mathbb{H}},\mathrm{Vect}(\mathbb{H})$ | the centre and the vector subspace, neither carrying a square-zero element |

## Further Reading

- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for nilpotents, powers and the division property in a non-associative algebra.
- *Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-quaternioid-r-space.md`), §*The Element Vocabulary*, for the general definition of a nilpotent, of a square-zero element and of the powers.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the powers of a non-associative product and the isotopes that preserve the division property.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the division property of the quaternion algebra and the multiplicative norm.
- *Norm and Invertibility in the General Quaternionic Algebra* (`articles_maths/norm-and-invertibility-in-the-general-quaternionic-algebra-of-quaternioid.md`), for the definite norm and the one-sided equations.
- *Square Roots of One and the Idempotents of the General Quaternionic Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-general-quaternionic-algebra-of-quaternioid.md`), for the reduction of the root equation, the roots of $+1$ and the roots of $-1$.
- *Square Roots of a General Element in the General Quaternionic Algebra* (`articles_maths/square-roots-of-a-general-element-in-the-general-quaternionic-algebra-of-quaternioid.md`), for the root problem of an arbitrary radicand.
- *Square Roots of Zero and the Nilpotents of the Quaternion Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-quaternion-algebra.md`), for the plain root set of $0$ of the same space and the plain nilpotents.
- *Zero Divisors of the General Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-general-quaternionic-algebra-of-quaternioid.md`), for the empty zero-divisor set.
- *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/square-roots-of-zero-and-the-nilpotents-in-the-algebraic-structures-over-the-quaternioid-r-space.md`), the comparison of the six square-zero sets of the real chapter, whose general quaternionic row is the origin.
- *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/square-roots-of-zero-and-the-nilpotents-in-the-algebraic-structures-over-the-biquaternioid-c-space.md`), §*The Order of the Four Sets*, for the ordering of the four complex root sets of $0$ against which the real collapse is read.
