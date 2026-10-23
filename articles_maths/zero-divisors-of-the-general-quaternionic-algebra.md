# __Zero Divisors of the General Quaternionic Algebra__

## Introduction

This article studies the **zero divisors** of the biquaternion algebra $\mathbb{B}$ read through
the general quaternionic bilinear product, and it complements the algebraic norm of the product by
describing the set on which the algebraic norm vanishes.

A divisor is relative to a product, and the definition is stated once in *Definitions for the Study
of the Algebraic Structures*, §*The Zero Divisor and the Annihilator*; the unqualified "zero
divisor" means the zero divisor of the general quaternionic product throughout, and every other
product is named. The article establishes four things. First, the **criterion**: a nonzero
$\tilde Q$ is a zero divisor of $\star$ exactly when its algebraic norm vanishes, so the zero
divisors of the quaternionic product are the nonzero solutions of $\langle\tilde Q\rangle_{\natural}=0$. Second, the set
is the **zero-divisor cone**, a real cone of dimension six in the eight-dimensional real space that
is not a subspace, and it is the union of the **pure** and the **non-pure** families of the element
theory of the algebra. Third, the two **annihilators** of an element, taken with respect to
$\star$, are each of complex dimension two for a zero divisor and vanish for a unit, and the
element lies in its own annihilators. Fourth, and the sharpest fact of the article, the two
annihilators **coincide for every element**, unit or zero divisor alike, because the natural
conjugation is a $\mathbb{C}$-linear anti-automorphism of order two; the quaternionic product is
the one product of the block whose annihilators are not exchanged by the conjugation.

**The results.** A nonzero biquaternion is a zero divisor of the general quaternionic product exactly when its algebraic norm vanishes, $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2=Q_t^2+(\vec Q,\vec Q)=0$, so the zero divisors are the nonzero points of the **zero-divisor cone** $C=\{N=0\}$, a real cone of real dimension $6$ that is not a subspace and is stable under the product. The cone splits into the **pure** family, the plain nilpotents with $Q_t=0$ and $(\vec Q,\vec Q)=0$ forming an isotropic cone of real dimension $4$, and the **non-pure** family, the complex multiples $\tilde Q=2Q_t\tilde\Pi$ of the nontrivial plain idempotents, on which $\tilde Q\star\tilde Q=0$ while the plain square is the nonzero multiple $2Q_t\tilde Q$. The two annihilators of an element coincide, are $\{0\}$ off the cone and a complex plane on it, and the four general products select one and the same zero-divisor set. Each section below states its result first and then proves it.

$$
\tilde Q_1\star\tilde Q_2=\tilde Q_1^{\natural}\tilde Q_2 ,
$$

with $\natural$ the natural conjugation $\tilde Q^{\natural}=Q_t-\vec Q$. An element is
$\tilde Q=Q_te_t+\vec Q$ with $\vec Q=\sum_{k=1}^{3}Q_k\vec e_k$, the **algebraic norm** is
$\langle\tilde Q\rangle_{\natural}=\tilde Q^{\natural}\tilde Q=\sum_\mu Q_\mu^2$, and
$(\vec Q_1,\vec Q_2)=\sum_kQ_{1,k}Q_{2,k}$ is the complex bilinear form of the vector parts. An element
is **pure** when $Q_t=0$ and **non-pure** when $Q_t\neq0$.

## Definition

The word names a product, so the definition is stated for a general product and then read on
$\star$.

**Definition.** Let $\star$ be a product on $\mathbb{B}$ and let $\tilde Q\in\mathbb{B}$. The
element $\tilde Q$ is a **left zero divisor of $\star$** when $\tilde Q\neq0$ and there is a
nonzero $\tilde{Q}_1$ with $\tilde Q\star\tilde{Q}_1=0$; a **right zero divisor of $\star$** when
$\tilde Q\neq0$ and there is a nonzero $\tilde{Q}_1$ with $\tilde{Q}_1\star\tilde Q=0$; and a **zero
divisor of $\star$** when it is one or the other. It is a **two-sided zero divisor of $\star$**
when it is both. The definition is *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*,
§*The Zero Divisor and the Annihilator*, and the origin is not a zero divisor, both factors being
required to be nonzero.

Throughout this article the product is the general quaternionic bilinear product
$\tilde Q_1\star\tilde Q_2=\tilde Q_1^{\natural}\tilde Q_2$. On it the two defining equations are

$$
\tilde Q^{\natural}\tilde{Q}_1=0 \quad\text{(left)},\qquad \tilde{Q}_1^{\natural}\tilde Q=0 \quad\text{(right)} ,
$$

which are plain-product equations in the conjugated first factor.

## The Criterion

**A nonzero $\tilde Q$ is a zero divisor of $\star$ if and only if its algebraic norm vanishes, $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2=0$.**

**Theorem (the criterion for the general quaternionic product).** For a nonzero
$\tilde Q\in\mathbb{B}$, $\tilde Q$ is a zero divisor of $\star$ if and only if

$$
\boxed{\; \langle\tilde Q\rangle_{\natural}=\sum_{\mu\in\{t,x,y,z\}}Q_\mu^2=0 \;}.
$$

**Proof.** Suppose $\langle\tilde Q\rangle_{\natural}=0$ and $\tilde Q\neq0$. Then

$$
\tilde Q\star\tilde Q=\tilde Q^{\natural}\tilde Q=\langle\tilde Q\rangle_{\natural}e_t=0 ,
$$

so $\tilde{Q}_1=\tilde Q$ is a nonzero element with $\tilde Q\star\tilde{Q}_1=0$ and $\tilde Q$ is a left
zero divisor; the mirror computation with the factors exchanged gives the right statement.
Conversely, suppose $\tilde Q$ is a zero divisor of $\star$: there is a nonzero $\tilde{Q}_1$ with
$\tilde Q\star\tilde{Q}_1=0$, that is $\tilde Q^{\natural}\tilde{Q}_1=0$. If $\langle\tilde Q\rangle_{\natural}\neq0$ then
$\tilde Q^{\natural}$ is a unit of the plain product by §*The Criterion* of *Norm and Invertibility
in the General Quaternionic Algebra*, and multiplying the equation by its inverse gives
$\tilde{Q}_1=0$, a contradiction. Hence $\langle\tilde Q\rangle_{\natural}=0$.

The criterion is the criterion of the plain product read on this product; the two are the same
equation because the algebraic norm is the same quadratic form, and the two products are
distinguished by the object that turns the equation into a statement — the plain inverse there, the
conjugated one-sided solution here.

## The Three-Way Classification

**Every element of $\mathbb{B}$ is exactly one of three: a unit of the plain product with $\langle\tilde Q\rangle_{\natural}\neq0$, the zero element, or a zero divisor of $\star$ with $\langle\tilde Q\rangle_{\natural}=0$ and $\tilde Q\neq0$.**

Combining the criterion with the invertibility theory of the algebraic norm, the elements of
$\mathbb{B}$ are partitioned into three classes, and the classification is the one of *Zero
Divisors of the General Plain Algebra* with the inverse column read for this product.

| condition on $\langle\tilde Q\rangle_{\natural}$ | condition on $\tilde Q$ | conclusion |
|---|---|---|
| $\langle\tilde Q\rangle_{\natural}\neq0$ | none | a unit of the plain product, not a zero divisor of $\star$ |
| $\langle\tilde Q\rangle_{\natural}=0$ | $\tilde Q=0$ | the zero element, not a zero divisor |
| $\langle\tilde Q\rangle_{\natural}=0$ | $\tilde Q\neq0$ | a zero divisor of $\star$ |

The zero divisors are exactly the nonzero elements on which the algebraic norm vanishes. The
classification is a classification of the elements by their behaviour under $\star$, and it does
not describe them under the other products.

## The Algebra Is Not a Division Algebra

**The biquaternion algebra is not a division algebra, because it has zero divisors; the statement does not depend on the product, the same elements being the zero divisors of both.**

A **division algebra** is an algebra in which every nonzero element is invertible; for a
finite-dimensional algebra this is equivalent to the absence of zero divisors. The biquaternion
algebra contains zero divisors, so it is **not** a division algebra. The statement is the one of
*Zero Divisors of the Biquaternion Algebra*, and it is independent of the product: the same
elements are the zero divisors of both products, by the criterion above and the coincidence quoted
below.

## The Two Families of Zero Divisors

**The zero divisors split into the pure ones, $Q_t=0$ with $(\vec Q,\vec Q)=0$, and the non-pure ones, $Q_t\neq0$ with $(\vec Q,\vec Q)=-Q_t^2$, and the split does not depend on the product.**

The zero divisors split into two families according to the value of the scalar part, and the split
does not depend on the product, because $\langle\tilde Q\rangle_{\natural}=Q_t^2+(\vec Q,\vec Q)$ separates the two
cases on the element. A biquaternion is **pure** when $Q_t=0$ and **non-pure** when $Q_t\neq0$; on
a pure element the criterion is $(\vec Q,\vec Q)=0$, and on a non-pure one it is
$(\vec Q,\vec Q)=-Q_t^2$, which can be met by the vector part cancelling the scalar
contribution. The two families are developed in *Zero Divisors of the Biquaternion Algebra*; in
this product they are separated not by the square, which vanishes on both, but by the plain square,
as the two sections below compute.

## Pure Zero Divisors

**A nonzero pure element is a zero divisor of $\star$ exactly when $(\vec Q,\vec Q)=0$, and then it is a nilpotent of the plain product, $\tilde Q\tilde Q=0$; these are the isotropic bivectors $\vec\rho+i\vec\rho'$ with $\vec\rho\perp\vec\rho'$ and $\lvert\vec\rho\rvert=\lvert\vec\rho'\rvert$.**

**Proposition (the square of a pure element).** Let $\tilde Q=\vec Q$ be a pure element. Then

$$
\tilde Q\star\tilde Q=(\vec Q,\vec Q)\,e_t , \qquad \tilde Q\tilde Q=-(\vec Q,\vec Q)\,e_t , \qquad \tilde Q^{\natural}=-\tilde Q .
$$

**Proof.** The scalar–vector form of the product at a pure pair is $(\vec Q,\vec Q)e_t$ for
the quaternionic product and $-(\vec Q,\vec Q)e_t$ for the plain one, and the natural
conjugation negates a pure element.

**Theorem (the criterion in the pure case).** For a nonzero pure $\tilde Q$ the following are
equivalent:

1. $\tilde Q$ is a zero divisor of $\star$; 2. $(\vec Q,\vec Q)=0$; 3.
$\tilde Q\star\tilde Q=0$; 4. $\tilde Q$ is a nilpotent of the plain product, $\tilde Q\tilde Q=0$.

**Proof.** The equivalence of (1) and (2) is the criterion specialised to $Q_t=0$. The equivalence
of (2) with (3) and with (4) is the proposition above, both squares being the same scalar up to
sign.

The pure zero divisors are therefore the **nilpotents of the plain product**: on them the two
products have the same square, up to the sign, and in particular a pure zero divisor vanishes when
squared in either product. In the older vocabulary they are the isotropic **bivectors**
$\vec\rho+i\vec\rho'$ with $\vec\rho\perp\vec\rho'$ and
$|\vec\rho|=|\vec\rho'|$, the parameterisation of *Zero Divisors of the General Plain
Algebra*, §*The Bivector Form*.

## Non-Pure Zero Divisors

**A zero divisor with $Q_t\neq0$ has $\langle\tilde Q\rangle_{\natural}=0$ and $\tilde Q\star\tilde Q=0$ while its plain square is the nonzero element $\tilde Q\tilde Q=2Q_t\tilde Q$, and it is a complex multiple $\tilde Q=2Q_t\tilde\Pi$ of a nontrivial plain idempotent.**

**Proposition (the square of a non-pure element).** Let $\tilde Q=Q_te_t+\vec Q$ with $Q_t\neq0$
and $\langle\tilde Q\rangle_{\natural}=0$. Then

$$
\tilde Q\star\tilde Q=0 , \qquad \tilde Q\tilde Q=2Q_t\tilde Q\neq0 .
$$

**Proof.** The quaternionic square is $\langle\tilde Q\rangle_{\natural}e_t$ and the algebraic norm vanishes by the
criterion. The plain square is $(Q_t^2-(\vec Q,\vec Q))e_t+2Q_t\vec Q$, and the criterion
$(\vec Q,\vec Q)=-Q_t^2$ turns it into $2Q_t^2e_t+2Q_t\vec Q=2Q_t\tilde Q$, which is
nonzero because $Q_t\neq0$ and $\tilde Q\neq0$.

**Theorem (the non-pure family is the idempotent family).** A non-pure zero divisor is a complex
multiple of a nontrivial idempotent of the plain product,

$$\boxed{\; \tilde Q=2Q_t\tilde\Pi , \qquad \tilde\Pi=\frac{\tilde Q}{2Q_t} \;},$$

and conversely every complex multiple of a nontrivial plain idempotent is a non-pure zero divisor
of $\star$.

**Proof.** The relation $\tilde Q\tilde Q=2Q_t\tilde Q$ of the proposition makes
$\tilde\Pi=\tilde Q/(2Q_t)$ an idempotent of the plain product, nontrivial because $\tilde Q\neq0$
and $Q_t\neq0$; the converse is the statement of *Idempotents of the General Plain Algebra*,
§*Idempotents and the Non-Pure Zero Divisors*, read with the algebraic norm.

**Remark (the displacement).** The non-pure zero divisor has vanishing quaternionic square, so it
is a **nilpotent of the quaternionic product**, while it is the opposite of a nilpotent in the
plain product: its plain square is the nonzero element $2Q_t\tilde Q$. In particular the Hermitian
idempotents $\tilde\Pi_+(\tilde\Xi)=\tfrac12(e_t+\tilde\Xi)$ over the real unit vectors $\vec u$
satisfy

$$
\tilde\Pi_+(\tilde\Xi)\star\tilde\Pi_+(\tilde\Xi)=\langle\tilde\Pi_+(\tilde\Xi)\rangle_{\natural}e_t=\tfrac14\bigl(1-(\vec u,\vec u)\bigr)e_t=0 , \qquad \tilde\Pi_+(\tilde\Xi)\tilde\Pi_+(\tilde\Xi)=\tilde\Pi_+(\tilde\Xi) ,
$$

so the two products see the same element as an idempotent and as a square-zero element. This
displacement is the subject of *Square Roots of One and the Idempotents of the General Quaternionic Algebra*.

## The Zero Divisor Set

**The zero-divisor cone $C=\{\tilde Q\star\tilde Q=0\}=\{\langle\tilde Q\rangle_{\natural}=0\}$ is a real cone of real dimension $6$ that is not a subspace and is stable under the product; it is the union of the origin, the pure family and the non-pure family.**

**Definition.** The **zero-divisor cone** of the quaternionic product is the vanishing set of the
algebraic norm,

$$
C=\{\tilde Q\in\mathbb{B}:\langle\tilde Q\rangle_{\natural}=0\}=\{\tilde Q:\tilde Q\star\tilde Q=0\}.
$$

**Proposition (shape).** The set $C$ is a real cone of real dimension $6$ in the real
eight-dimensional space $\mathbb{B}$, and it is not a real subspace.

**Proof.** With $Q_\mu=q_\mu+iq'_\mu$ the real and the imaginary parts, the equation
$N=\sum_\mu(q_\mu^2-q'_\mu{}^2)+2i\sum_\mu q_\mu q'_\mu=0$ is one complex equation, hence two real
equations, and the set is a cone because $\langle\cdot\rangle_{\natural}$ is homogeneous of degree two; the two equations are
independent off the origin, so the real dimension is $8-2=6$. For the failure of linearity, the
elements $\vec e_x+i\vec e_y$ and $\vec e_x-i\vec e_y$ have algebraic norm $1-1=0$, while their sum $2\vec e_x$ has
algebraic norm $4$.

**Corollary.** The cone is a multiplicative set: for every $\tilde Q_1$ and every $\tilde Q_2$ with
$\langle\tilde Q_2\rangle_{\natural}=0$,

$$
\langle\tilde Q_1\star\tilde Q_2\rangle_{\natural}=\langle\tilde Q_1\rangle_{\natural}\langle\tilde Q_2\rangle_{\natural}=0 ,
$$

so the product of a cone point with any element is again in the cone, on either side.

**Proof.** The multiplicativity of the algebraic norm of *Norm and Invertibility in the General
Quaternionic Algebra*, §*Multiplicativity*, evaluated at $\langle\tilde Q_2\rangle_{\natural}=0$.

**The two families and the cone.** The cone is the union of the two families and of the origin: the
pure family is the isotropic cone of the vector subspace, of real dimension four, and the non-pure
family is the rest, of real dimension six. On a pure element the quaternionic and the plain squares
vanish together; on a non-pure one only the quaternionic square vanishes, and the plain square is
the nonzero multiple $2Q_t\tilde Q$. The distinction is invisible at the level of the quaternionic
square, which is blind to it, and it is read from the scalar part of the element.

## The Annihilators

The annihilator of an element is the kernel of the left or the right multiplication, the two
coinciding because the natural conjugation is an anti-automorphism of order two: off the cone both
vanish, and on the cone each is a complex plane. The annihilators, the coincidence theorem, the
operator and the reading on the remarkable subspaces are the companion article *Annihilators of the
General Quaternionic Algebra*, below this article in this category.

## The Zero Divisors and the Four General Products

**The four general products give four zero-divisor equations but one and the same zero-divisor set, $\{\tilde Q\neq0:\langle\tilde Q\rangle_{\natural}=0\}$; what the product changes is the equation and the annihilator, not the set.**

The four general products of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*
give four definitions of a zero divisor, hence four zero-divisor sets. For the biquaternion algebra
the four sets are one and the same set,

$$
\boxed{\; \{\tilde Q\neq0:\langle\tilde Q\rangle_{\natural}=0\} \;},
$$

and this is a theorem of *Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*The Four General Products Coincide*,
which this article quotes and does not reprove. What the product changes is the **equation** and
the **annihilator**: the four left zero-divisor equations are $\tilde Q\tilde{Q}_1=0$,
$\tilde Q^{\natural}\tilde{Q}_1=0$, $\tilde Q\tilde{Q}_1^{*}=0$ and $\tilde Q^{\natural}\tilde{Q}_1^{*}=0$,
four different equations with the same solution set, and the annihilators of one element depend on
the product, as the coincidence theorem above shows for this one. The one-sided inverse equations
and their solutions for the four products are the same article's §*The One-Sided Inverse
Equations*, and the plain reading of the criterion is *Zero Divisors of the Biquaternion Algebra*.

## The Zero Divisors and the Remarkable Subspaces

**The centre, the quaternion subspace and the anti-quaternion subspace carry no zero divisor; the vector subspace carries the whole pure family as an isotropic cone of real dimension $4$, the two Hermitian subspaces carry the non-pure family in the star-fixed form, and a general non-pure zero divisor lies in neither.**

Since the zero divisors are the nonzero elements of algebraic norm zero, their distribution among
the remarkable subspaces is the distribution of the zeros of the quadratic form $\langle\cdot,\cdot\rangle_{\natural}$, and the
signatures are *Remarkable Subspaces under the General Quaternionic Algebra*.

| remarkable subspace | zero divisors |
|---|---|
| $\mathbb{C}_{\mathbb{B}}$, the centre | none |
| $\mathbb{H}_{\mathbb{B}}$, the quaternion subspace | none |
| $i\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace | none |
| $\mathrm{Vect}(\mathbb{B})$, the vector subspace | the pure family, an isotropic cone of real dimension four |
| $\mathbb{M}_{+}$, the Hermitian subspace | the non-pure Hermitian elements with $Q_t^2=-(\vec Q,\vec Q)$ |
| $\mathbb{M}_{-}$, the anti-Hermitian subspace | the non-pure anti-Hermitian elements with the same condition |

The centre, the quaternion subspace and the anti-quaternion subspace carry no zero divisor: the
algebraic norm is definite on the last two and vanishes on the first only at the origin. The vector
subspace carries the whole pure family. The two Hermitian subspaces carry the non-pure family in
the form in which its elements are fixed by the star; a general non-pure zero divisor lies in
neither, and the elements $\vec e_x+i\vec e_y$, of the vector subspace, and $e_t+i\vec e_x$, of the Hermitian
subspace, are the two standard witnesses.

## Summary

For the general quaternionic bilinear product $\tilde Q_1\star\tilde Q_2=\tilde Q_1^{\natural}\tilde Q_2$,
a nonzero element is a zero divisor exactly when its algebraic norm vanishes,
$\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2=0$, and the zero divisors are the nonzero points of the zero-divisor
cone, a real cone of dimension six that is not a subspace and is stable under the product. The cone
is the union of the **pure** family, the plain nilpotents $\vec\rho+i\vec\rho'$ with
$\vec\rho\perp\vec\rho'$ and equal lengths, on which the quaternionic and the plain
squares vanish together, and the **non-pure** family, the complex multiples of the nontrivial plain
idempotents, on which the quaternionic square vanishes while the plain square is the nonzero
multiple $2Q_t\tilde Q$. The left and the right annihilator of a zero divisor are each a complex
plane containing the element, and both are $0$ for a unit; the two annihilators **coincide for
every element**, because the natural conjugation is a $\mathbb{C}$-linear anti-automorphism of
order two that turns the one equation into the other. The zero-divisor set is the same set as for
the plain product, a coincidence of the algebra proved in *Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*; what
this product changes is the equation, the cone-shaped square, and the annihilator, which is
symmetric here where the sesquilinear products make it conjugate-symmetric.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the basis, $e_t$ the identity, $\vec e_k^2=-e_t$ |
| $\tilde Q=Q_te_t+\vec Q$ | an element and its scalar–vector split |
| $\tilde Q_1\star\tilde Q_2=\tilde Q_1^{\natural}\tilde Q_2$ | the general quaternionic bilinear product |
| $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2$ | the algebraic norm, vanishing exactly on the zero-divisor cone |
| $C=\{N=0\}$ | the zero-divisor cone, the square-zero set of the product |
| pure, non-pure | $Q_t=0$; $Q_t\neq0$ |
| $\tilde\Pi_+(\tilde\Xi)=\tfrac12(e_t+\tilde\Xi)$ | the Hermitian idempotent over a real unit vector $\vec u$ |
| $\mathrm{Ann}_\ell(\tilde Q),\mathrm{Ann}_r(\tilde Q)$ | the left and the right annihilator of $\tilde Q$ for $\star$ |
| $\mathrm{Ann}(\tilde Q)$ | their common value, of complex dimension two for a zero divisor |

## Further Reading

- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for zero divisors and annihilators in a non-associative algebra.
- [Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternion-c-space.html), §*The Zero Divisor and the Annihilator*, for the product-relative definition of the zero divisor and of the annihilator.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for isotopes and the way a change of product moves the zero divisors.
- Sterling K. Berberian, *Baer \*-Rings* (Springer, 1972), for annihilators in a ring with an involution and the symmetry that an anti-automorphism imposes on them.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the isotropic vectors of the complex quaternion algebra and the quadratic form $\sum_\mu Q_\mu^2$.
- [Zero Divisors of the Biquaternion Algebra](zero-divisors-of-the-biquaternion-algebra.html), for the two families, the criterion in the plain product and the structure of the cone.
- [Norm and Invertibility in the General Quaternionic Algebra](norm-and-invertibility-in-the-general-quaternionic-algebra.html), for the algebraic norm, its multiplicativity and the one-sided equations.
- [Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](zero-divisors-in-the-algebraic-structures-over-the-biquaternion-c-space.html), for the coincidence of the four zero-divisor sets and the dependence of the annihilators on the product.
- [Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra](square-roots-of-zero-and-the-nilpotents-of-the-general-quaternionic-algebra.html), for the square-zero elements of the product and the index of nilpotency.
- [Square Roots of One and the Idempotents of the General Quaternionic Algebra](square-roots-of-one-and-the-idempotents-of-the-general-quaternionic-algebra.html), for the displacement of the plain idempotents into the nilpotents of the product.
- [Remarkable Subspaces under the General Quaternionic Algebra](remarkable-subspaces-under-the-general-quaternionic-algebra.html), for the signatures of the algebraic norm on the six subspaces.
- [Annihilators of the General Quaternionic Algebra](annihilators-of-the-general-quaternionic-algebra.html), below this article in this category, the companion article, for the coincident annihilators, the operator and the rank table
