# __Nilpotents of the General Quaternionic Algebra__

## Introduction

This article studies the **nilpotents** of the quaternion algebra $\mathbb{H}$ read through the
general quaternionic bilinear product, and it is the real member of the general quaternionic family
whose complex sibling is *Nilpotents of the General Quaternionic Algebra*.

A nilpotent is relative to a product, and the definition is stated once in *Definitions for the Study
of the 6 Algebraic Structures*, §*The Element Vocabulary*; throughout this article the product is
the general quaternionic product $\tilde p\star\tilde q=\tilde p^{\natural}\tilde q$, and the
unqualified "nilpotent" means a nilpotent of it. The article rests on one computation: the
quaternionic square of every element is the central element $N(\tilde p)e_0$, and the criterion of
square-zero is the vanishing of the definite norm. The answer is as small as it could be: **the
square-zero set is the origin alone**, hence the product has **no nilpotent at all**, of any index.

The companion article of the complex chapter, *Nilpotents of the General Quaternionic Algebra*, gives
the opposite answer on the same rule: there the square-zero set is the whole zero-divisor cone
$\mathcal{C}=\{N=0\}$, of real dimension six, whose pure part is a cone of real dimension four, and
the square-zero elements are exactly the elements of the cone. Over $\mathbb{R}$ the cone collapses
to its apex and the nilpotent set is empty. The article states the criterion, proves the absence of
nilpotents of every index rather than of index two alone, reads the square-zero set as the root set
of $0$ and on the two remarkable subspaces, and places the result against the six structures of the
real chapter and the twelve of the complex chapter.

**Boundaries.** The norm, its definiteness and the square are *Norm and Invertibility in the General
Quaternionic Algebra* and *Square Roots of Minus One, Zero and Plus One in the General Quaternionic
Algebra*; the element vocabulary is *Definitions for the Study of the 6 Algebraic Structures*; the
zero divisors are *Zero Divisors of the General Quaternionic Algebra* and the idempotents
*Idempotents of the General Quaternionic Algebra*, both above this article in this category; the
structure-level comparison of the six square-zero sets is *Nilpotents*, of the real chapter, and
*Nilpotents* of the complex chapter, whose ordering of the sets is quoted; the definiteness of the
form is *The Isotropic Structure of the General Quaternionic Algebra*; and the complex sibling is
*Nilpotents of the General Quaternionic Algebra*.

## Conventions

$\mathbb{H}$ is the real quaternion algebra with basis $e_0=1,e_1,e_2,e_3$, the rules
$e_k^2=-e_0$ and $e_1e_2=e_3$. Over $\mathbb{R}$ the coefficientwise conjugation is the identity and
the Hermitian star coincides with the natural conjugation, so the block carries the single
involution

$$
\tilde p^{\natural}=p_0-\mathbf p,\qquad \tilde p=p_0e_0+\mathbf p,\quad
\mathbf p=p_1e_1+p_2e_2+p_3e_3 .
$$

Juxtaposition is the plain product and $\star$ is the general quaternionic bilinear product
$\tilde p\star\tilde q=\tilde p^{\natural}\tilde q$. Its **powers** are the left-nested products

$$
\tilde p^{1}=\tilde p,\qquad \tilde p^{k+1}=\tilde p\star\tilde p^{k} ,
$$

and the **plain powers** are the same nestings in the plain product, written $\tilde p^{(k)}$, with
$\tilde p^{(0)}=e_0$. The **algebraic norm** is

$$
N(\tilde p)=\tilde p^{\natural}\tilde p=p_0^2+|\mathbf p|^2=\sum_{\mu=0}^{3}p_\mu^2 ,
$$

positive definite, with polar form $\beta(\tilde p,\tilde q)=p_0q_0+\mathbf p\cdot\mathbf q$. The
centre is the scalar line $\mathbb{R}_{\mathbb{H}}=\mathbb{R}e_0$ and the vector subspace is
$\mathrm{Vect}(\mathbb{H})=\{\mathbf p\}$.

## Definition, and the Square

**Definition.** Let $\star$ be a product on $\mathbb{H}$ and let $\tilde\nu\in\mathbb{H}$. The element
$\tilde\nu$ is **nilpotent of $\star$** when $\tilde\nu\neq0$ and $\tilde\nu^{k}=0$ for some positive
integer $k$; the least such $k$ is the **index**. The case $k=2$ is a **square-zero** element, and
the **square-zero set** of the product is the solution set of $\tilde\nu\star\tilde\nu=0$. The
definition is *Definitions for the Study of the 6 Algebraic Structures*, §*The Element Vocabulary*;
the origin is not a nilpotent, the class containing its nonzero members.

**Lemma (the square is central).** For every $\tilde p\in\mathbb{H}$,

$$
\tilde p\star\tilde p=\tilde p^{\natural}\tilde p=N(\tilde p)\,e_0 , \qquad
N(\tilde p)=p_0^2+p_1^2+p_2^2+p_3^2 .
$$

**Proof.** At equal arguments the vector part of the product is
$p_0\mathbf p-p_0\mathbf p-\mathbf p\times\mathbf p=0$, so the square is the scalar part
$p_0^2+\mathbf p\cdot\mathbf p$ times $e_0$ (*Introduction to the General Quaternionic Algebra of
Quaternions*; *Square Roots of Minus One, Zero and Plus One in the General Quaternionic Algebra*).

## The Square-Zero Criterion

**Theorem (the criterion).** For $\tilde p\in\mathbb{H}$, $\tilde p\star\tilde p=0$ if and only if
$N(\tilde p)=0$, that is if and only if $\tilde p=0$. The square-zero set of the general quaternionic
product is the single point $\{0\}$, and the product has no square-zero element.

**Proof.** By the lemma $\tilde p\star\tilde p=N(\tilde p)e_0$, which vanishes exactly when
$N(\tilde p)=0$. The norm is a sum of four real squares, so it vanishes only at $\tilde p=0$; the
norm is positive definite, and the criterion is met by the origin alone. The origin has vanishing
square but is not a nilpotent, the nilpotent class taking the nonzero members.

The criterion is the criterion of the complex sibling, and it is the norm equation read on the
product whose square is the norm. The difference is the norm: over $\mathbb{C}$ the equation $N=0$ is
the cone and the set is large, over $\mathbb{R}$ it is the apex and the set is a point.

## No Nilpotent of Any Index

The square-zero case does not by itself exclude a nilpotent of larger index, since the definition
asks for some power, not the second. The following computation closes the question.

**Lemma (the powers).** For every $\tilde p\in\mathbb{H}$ and every $k\geq2$,

$$
\tilde p^{k}=N(\tilde p)\,\bigl(\tilde p^{\natural}\bigr)^{(k-2)} ,
$$

where the factor on the right is the plain power of order $k-2$ of $\tilde p^{\natural}$.

**Proof.** By induction on $k$. For $k=2$ the identity is the central square
$\tilde p^{2}=N(\tilde p)e_0=N(\tilde p)(\tilde p^{\natural})^{(0)}$. Assume it for $k$; then, using
the plain associativity inside the power,

$$
\tilde p^{k+1}=\tilde p\star\tilde p^{k}=\tilde p^{\natural}\bigl(N(\tilde p)(\tilde p^{\natural})^{(k-2)}\bigr)
=N(\tilde p)\,(\tilde p^{\natural})^{(k-1)} ,
$$

which is the identity of order $k+1$.

**Theorem (no nilpotent).** Every $\tilde p\in\mathbb{H}$ with $\tilde p^{k}=0$ for some positive
integer $k$ is $\tilde p=0$. The general quaternionic product has no nilpotent of any index, and its
nilpotent class is empty.

**Proof.** For $k=1$ the assertion is the definition. For $k=2$ it is the criterion of
§*The Square-Zero Criterion*. Let $k\geq3$. By the power lemma
$\tilde p^{k}=N(\tilde p)(\tilde p^{\natural})^{(k-2)}=0$, so either $N(\tilde p)=0$ or
$(\tilde p^{\natural})^{(k-2)}=0$. In the first case $\tilde p=0$ by definiteness. In the second, the
plain powers of a nonzero quaternion do not vanish: if $\tilde x^{(m)}=0$ with $m\geq1$ and
$\tilde x\neq0$, left multiplication by the plain inverse $\tilde x^{-1}$ lowers the exponent, and
iteration gives $\tilde x=0$, a contradiction. Hence $\tilde p^{\natural}=0$ and $\tilde p=0$. The
plain division property used here is *Norm and Invertibility in the General Plain Algebra*.

**Corollary (the index).** No element of the block has nilpotency index two or more, and the
square-zero set, the nilpotent class and the class of elements of finite nilpotency index are
$\{0\}$, $\varnothing$ and $\{0\}$ respectively.

## The Square-Zero Set Is the Origin

**Proposition (the zero set of the norm).** The square-zero set of the general quaternionic product,
the zero set of the norm and the root set of the central value $0$ coincide, and the common set is
the origin:

$$
\{\tilde p:\tilde p\star\tilde p=0\}=\{\tilde p:N(\tilde p)=0\}=\{0\} .
$$

**Proof.** The first equality is the criterion, the second is the definiteness of the norm; the root
set of $0$ is by definition the set $\{\tilde p:\tilde p\star\tilde p=0\}$, so it is the same set.
The three sets are the apex of the cone of the complex block, and they are a single point.

**Remark (the collapse of the cone).** Over $\mathbb{C}$ the set $\{N=0\}$ is the zero-divisor cone
$\mathcal{C}$, of real dimension six, and the square-zero elements are exactly its nonzero points; the
pure part of the cone, the nilpotents of the plain product, is a cone of real dimension four. Over
$\mathbb{R}$ the equation $N=0$ has no nonzero solution and the cone shrinks to its apex. The
collapse is the definiteness of the quaternionic form (*The Isotropic Structure of the General
Quaternionic Algebra*), and it is the same fact that removes the zero divisors
(*Zero Divisors of the General Quaternionic Algebra*).

## The Nilpotents and the Roots of Zero

The root set of a central value is the solution set of $\tilde p\star\tilde p=c$ with $c$ central;
the square-zero set is the value $0$, and the value $0$ is the only central value whose root set is
degenerate here.

**Theorem (the three central values).** The root sets of the central values $-e_0$, $0$ and $+e_0$
are

$$
\{\tilde p:\tilde p\star\tilde p=-e_0\}=\varnothing,\qquad
\{\tilde p:\tilde p\star\tilde p=0\}=\{0\},\qquad
\{\tilde p:\tilde p\star\tilde p=+e_0\}=\mathrm{Sp}(1) ,
$$

the first empty, the third the unit sphere of real dimension three. The statement and the reduction
are *Square Roots of Minus One, Zero and Plus One in the General Quaternionic Algebra*.

**Proof.** The three equations are $N(\tilde p)=-1$, $N(\tilde p)=0$ and $N(\tilde p)=1$; the norm is
positive definite, so the first has no solution, the second has the origin alone, and the third is
the norm-one level set, the sphere $\mathrm{Sp}(1)$.

**Corollary.** The square-zero set is the root set of $0$ and is strictly smaller than the root set
of $+e_0$, and the nilpotents, which are its nonzero members, do not exist; the element $0$ is at the
same time the only root of $0$ and the only idempotent that is not the left unit.

## The Nilpotents on the Remarkable Subspaces

The square-zero equation is the vanishing of the norm, and the norm is read on the two remarkable
subspaces of $\mathbb{H}$, the scalar line $\mathbb{R}_{\mathbb{H}}=\mathbb{R}e_0$, the centre, and
the vector subspace $\mathrm{Vect}(\mathbb{H})$ (*Introduction to the Remarkable Subspaces of the
Quaternions*).

**Proposition.** On the centre and on the vector subspace the square vanishes only at the origin, so
neither subspace carries a square-zero element and neither carries a nilpotent; in the centre the
square is $A^2e_0$, and in the vector subspace it is the central element $|\mathbf p|^2e_0\neq0$ for
every nonzero pure $\mathbf p$.

| subspace | element | square | nilpotents |
|---|---|---|---|
| $\mathbb{R}_{\mathbb{H}}$, the centre | $Ae_0$ | $A^2e_0$ | none |
| $\mathrm{Vect}(\mathbb{H})$, the vector subspace | $\mathbf p$ | $\lvert\mathbf p\rvert^2e_0$ | none |

**Proof.** The square is the norm on the subspace of each row, by the lemma; $A^2$ vanishes only at
$A=0$ and $|\mathbf p|^2$ only at $\mathbf p=0$. A nonzero pure element has a central nonzero square,
so no pure element is square-zero, and no central element is either.

## The Nilpotents and the Other Structures of the Space

The comparison of the six square-zero sets is *Nilpotents*, the structure-level article of the real
chapter, and its verdict for the block is the origin alone.

**Theorem (the six square-zero sets).** Among the six structures of the quaternion real space the
square-zero set is $\{0\}$ for the general plain algebra, the symmetric plain algebra, the general
quaternionic algebra and the symmetric quaternionic algebra, and it is the whole space
$\mathbb{H}$ for the two antisymmetric structures. Only two square-zero sets occur, and the general
quaternionic structure is one of the four with the origin alone.

**Proof.** The four rows are the theorem of *Nilpotents*, §*The Four Structures with the Origin
Alone*, where the plain square is anisotropic and the quaternionic square is the definite norm; the
two alternating rows are its §*The Two Alternating Structures*, the products being alternating. The
four structures with the origin alone are exactly those whose square is the plain square or the
central element $N(\tilde x)e_0$, neither of which vanishes off the origin over $\mathbb{R}$.

**Remark (the complex ordering and the real collapse).** The complex chapter carries twelve
structures and its comparison article *Nilpotents* orders the square-zero sets through the cone,
$Z_3=\{0\}\subsetneq Z_1\subsetneq Z_2$ and $Z_3\subsetneq Z_4\subsetneq Z_2$ for the four general
products, and it places the general quaternionic and the symmetric quaternionic structures at the
whole cone. Over $\mathbb{R}$ the cone has become a point, so the general quaternionic set drops from
the whole cone to the origin and joins the three real structures whose square vanishes only at the
origin; the ordering through the cone disappears with the cone, and only the two extreme sets, the
origin and the whole space, survive. The collapse is the same definiteness that carries the
zero-divisor set of the block from the punctured cone to the empty set.

## Summary

In the general quaternionic bilinear product the square of every element is the central element
$N(\tilde p)e_0$, and the square vanishes exactly when the norm does. Over $\mathbb{R}$ the norm is a
sum of four squares, hence positive definite, so the square-zero set is the origin alone and the
product has **no nilpotent**, of index two or of any larger index. The absence of higher nilpotents
is not a consequence of the square-zero case alone: the powers satisfy
$\tilde p^{k}=N(\tilde p)(\tilde p^{\natural})^{(k-2)}$ for $k\geq2$, so a vanishing power forces
either a vanishing norm or a vanishing plain power, and neither occurs off the origin because the
plain algebra is a division algebra. The square-zero set coincides with the zero set of the norm and
with the root set of the central value $0$, and it is strictly smaller than the root set of $+e_0$,
the sphere $\mathrm{Sp}(1)$; the root set of $-e_0$ is empty. Neither remarkable subspace, the centre
nor the vector subspace, carries a square-zero element. Against the six structures of the real
chapter the general quaternionic structure is one of the four whose square-zero set is the origin,
the other two being the whole space; against the twelve structures of the complex chapter, whose
square-zero sets are ordered through the cone, the real block records the collapse of that cone to a
point.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde p\star\tilde q=\tilde p^{\natural}\tilde q$ | the general quaternionic bilinear product |
| $\tilde p^{k}$ | the left-nested power, $\tilde p^{k+1}=\tilde p\star\tilde p^{k}$ |
| $\tilde p^{(k)}$ | the plain power of order $k$ |
| $\tilde p\star\tilde p=N(\tilde p)e_0$ | the square, always central |
| $N(\tilde p)=\sum_\mu p_\mu^2$ | the quaternionic bilinear algebraic norm, positive definite |
| $\{0\}$ | the square-zero set, the zero set of the norm, the root set of $0$ |
| $\varnothing$ | the nilpotent class of the block |
| $\mathrm{Sp}(1)$ | the root set of $+e_0$, the unit sphere of dimension three |
| $\tilde p^{k}=N(\tilde p)(\tilde p^{\natural})^{(k-2)}$, $k\geq2$ | the power identity that excludes nilpotents of every index |
| $\mathbb{R}_{\mathbb{H}},\mathrm{Vect}(\mathbb{H})$ | the centre and the vector subspace, neither carrying a square-zero element |

## Further Reading

- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for nilpotents, powers and the division property in a non-associative algebra.
- *Definitions for the Study of the 6 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-6-algebraic-structures.md`), §*The Element Vocabulary*, for the general definition of a nilpotent, of a square-zero element and of the powers.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the powers of a non-associative product and the isotopes that preserve the division property.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the division property of the quaternion algebra and the multiplicative norm.
- *Norm and Invertibility in the General Quaternionic Algebra* (`articles_maths/norm-and-invertibility-in-the-general-quaternionic-algebra-of-quaternions.md`), for the definite norm and the one-sided equations.
- *Square Roots of Minus One, Zero and Plus One in the General Quaternionic Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-general-quaternionic-algebra-of-quaternions.md`), for the three root sets and the norm-one sphere.
- *Zero Divisors of the General Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-general-quaternionic-algebra-of-quaternions.md`) and *Idempotents of the General Quaternionic Algebra* (`articles_maths/idempotents-of-the-general-quaternionic-algebra-of-quaternions.md`), for the empty zero-divisor set and the two trivial idempotents.
- *Nilpotents* (`articles_maths/quaternion-nilpotents.md`), the comparison of the six square-zero sets of the real chapter, whose general quaternionic row is the origin.
- *Nilpotents of the General Quaternionic Algebra* (`articles_maths/nilpotents-of-the-general-quaternionic-algebra.md`), the complex sibling, whose square-zero set is the whole cone that the passage to $\mathbb{R}$ collapses.
