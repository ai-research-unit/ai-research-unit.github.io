# __Annihilators of the General Quaternionic Algebra__

## Introduction

The zero divisor of a product is a property of one element alone: it says that *some* nonzero
partner exists that the element kills. The annihilator says *which* partners those are, and it is
the finer object. It is the set of elements killed by a fixed element,
$$
A_\star(\tilde Q)=\{\tilde Q_1:\tilde Q\star\tilde Q_1=0\},\qquad
B_\star(\tilde Q)=\{\tilde Q_1:\tilde Q_1\star\tilde Q=0\},
$$
the left and the right annihilator (*Definitions for the Study of the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*,
§*The Zero Divisor and the Annihilator*). When the product is carried by a multiplication operator
the annihilator is the kernel of that operator, so it is a linear subspace.

The block of this article is the **general quaternionic multiplication**
$$
\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q
=\bigl[P_tQ_t+(\vec P,\vec Q)\bigr]+P_t\vec Q-Q_t\vec P-\vec P\times\vec Q,
$$
the product of the natural conjugate of the first factor with the second (*Introduction to the
General Quaternionic Algebra of Biquaternions*). It is neither commutative nor alternating, and yet
a two-sided involution ties the two sides: the natural conjugation is a $\mathbb{C}$-linear
anti-automorphism of order two, so it carries the left annihilator
$\{\tilde Q_1:\tilde Q_1^{\natural}\tilde Q=0\}$ onto the right annihilator
$\{\tilde Q^{\natural}\tilde Q_1=0\}$, and the two annihilators of an element coincide. The
annihilator vanishes off the zero-divisor cone $C(\tilde P)=0$ and is a complex plane on it. The
article owns that reading, the operator with its rank, and the shape of the annihilator on the
remarkable subspaces; the zero-divisor set and its comparison with the other three general products
are the cited article's.

**The results.** The left and the right annihilator of an element coincide for **every** element of $\mathbb{B}$, unit or zero divisor alike, because the natural conjugation is a $\mathbb{C}$-linear anti-automorphism of order two; the quaternionic product is the one general product whose annihilators are not exchanged but equal. The multiplication operator $L_{\tilde P}$ has trace $4P_t$ and determinant $C(\tilde P)^{2}$ with $C(\tilde P)=\sum_\mu P_\mu^{2}$: it is invertible off the zero-divisor cone, while on the cone it has rank two and a kernel of complex dimension two. The common annihilator is therefore $\{0\}$ off the cone and a complex plane on it, and the plane contains the element itself. Each section below states its result first and then proves it.

## The Annihilator of a Product

**The annihilator of an element is the set of partners that it kills; the left annihilator is the kernel of the left multiplication and the right annihilator the kernel of the right multiplication, and both are nonzero exactly when the element is a zero divisor of the corresponding side.**

**Definition (annihilator).** Let $\star$ be a product on $\mathbb{B}$ and let
$\tilde Q\in\mathbb{B}$. The **left annihilator** and the **right annihilator** of $\tilde Q$ in
$\star$ are
$$
A_\star(\tilde Q)=\{\tilde Q_1:\tilde Q\star\tilde Q_1=0\},\qquad
B_\star(\tilde Q)=\{\tilde Q_1:\tilde Q_1\star\tilde Q=0\}.
$$
They are the kernels of the left and the right multiplication, and they are nonzero exactly when
$\tilde Q$ is a zero divisor of the corresponding side.

Throughout this article the product is the **general quaternionic multiplication** $\star$, and
unqualified, *annihilator* means the annihilator of $\star$. The left and the right multiplication
are the operator
$$
L_{\tilde P}\tilde Q_1=\tilde P\star\tilde Q_1=\tilde P^{\natural}\tilde Q_1,\qquad
R_{\tilde P}\tilde Q_1=\tilde Q_1\star\tilde P=\tilde Q_1^{\natural}\tilde P,
$$
a multiplication by the natural conjugate. The block is the sibling of the **general plain
algebra**, whose annihilators are *Annihilators of the Biquaternion Algebra*, and the two share
the cone and its plane but differ in the coincidence of the two sides.

## The Two Annihilators Coincide

**For every $\tilde Q\in\mathbb{B}$, unit or zero divisor alike, the two annihilators coincide, $B_\star(\tilde Q)=A_\star(\tilde Q)$, because the natural conjugation is a $\mathbb{C}$-linear anti-automorphism of order two.**

**Theorem (the coincidence).** For **every** $\tilde Q\in\mathbb{B}$, unit or zero divisor alike,
$$
B_\star(\tilde Q)=A_\star(\tilde Q).
$$

*Proof.* Let $\tilde Q_1\in\mathbb{B}$. Applying the natural conjugation ${}^{\natural}$ to the
equation $\tilde Q^{\natural}\tilde Q_1=0$ gives $(\tilde Q^{\natural}\tilde Q_1)^{\natural}=0$, which
is $\tilde Q_1^{\natural}\tilde Q=0$ because ${}^{\natural}$ is an anti-automorphism of order two;
the argument reverses because ${}^{\natural}$ is a bijection of $\mathbb{B}$ onto itself. Hence
$\tilde Q\star\tilde Q_1=0$ exactly when $\tilde Q_1\star\tilde Q=0$, and the two annihilators contain
exactly the same elements.

The coincidence is a property of this product: it holds because ${}^{\natural}$ is a
$\mathbb{C}$-**linear** anti-automorphism of order two, so the first factor can be conjugated away
without changing the annihilation. The general plain algebra has no such involution and its two
annihilators are generally distinct.

## The Multiplication Operator and the Rank

**The operator $L_{\tilde P}$ has trace $4P_t$ and determinant $C(\tilde P)^{2}$ with $C(\tilde P)=\sum_\mu P_\mu^{2}$; it is invertible with trivial kernel when $C(\tilde P)\neq0$, and of rank two with kernel of complex dimension two when $\tilde P\neq0$ and $C(\tilde P)=0$.**

**Proposition (the operator and its determinant).** In the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ the operator
$L_{\tilde P}$ of an element $\tilde P=P_te_t+\vec P$ has the matrix of multiplication by
$\tilde P^{\natural}$, of trace $4P_t$ and determinant
$$
\det L_{\tilde P}=C(\tilde P)^{2},\qquad C(\tilde P)=\sum_{\mu\in\{t,x,y,z\}}P_\mu^{2}.
$$

*Proof.* The matrix is the left multiplication matrix of the quaternion $\tilde P^{\natural}$,
whose determinant is the square of the quaternion norm $C(\tilde P^{\natural})=C(\tilde P)$; the
natural conjugation keeps the four squares, so the determinant is $C(\tilde P)^{2}$. The trace is
the sum of the four diagonal entries, $4P_t$.

**Corollary (the rank and the annihilator).** The rank of $L_{\tilde P}$ and the annihilator of
$\tilde P$ are

| $\tilde P$ | $C(\tilde P)$ | $\operatorname{rank}L_{\tilde P}$ | $\dim\ker L_{\tilde P}$ |
|---|---|---|---|
| $0$ | $0$ | $0$ | $4$ |
| $\tilde P\neq0$, $C(\tilde P)\neq0$ | $\neq0$ | $4$ | $0$ |
| $\tilde P\neq0$, $C(\tilde P)=0$ | $0$ | $2$ | $2$ |

*Proof.* The determinant $C(\tilde P)^{2}$ is nonzero exactly when $C(\tilde P)\neq0$, and in that
case the operator is invertible and the annihilator is $\{0\}$. When $C(\tilde P)=0$ the
determinant vanishes; the multiplication by the nonzero $\tilde P^{\natural}$ in the plain algebra
is then of rank two, because the plain algebra is the matrix algebra $M_2(\mathbb{C})$ and a
nonzero element of the cone is a matrix of rank one (*Zero Divisors of the Biquaternion Algebra*),
whence the kernel is of complex dimension two. The origin gives the zero operator.

## The Annihilator of an Element

**A plain unit has trivial annihilator, while a nonzero zero divisor has a common annihilator of complex dimension two that contains the element itself.**

**Theorem (the dimension of the annihilator).** Let $\tilde Q\in\mathbb{B}$.

- If $\tilde Q$ is a unit of the plain product, $C(\tilde Q)\neq0$, then
$A_\star(\tilde Q)=B_\star(\tilde Q)=\{0\}$.
- If $\tilde Q\neq0$ is a zero divisor, $C(\tilde Q)=0$, then $A_\star(\tilde Q)$ and
$B_\star(\tilde Q)$ are equal, of complex dimension two, and the common annihilator contains
$\tilde Q$.

*Proof.* The first clause is the rank table. For the second, the annihilator is the kernel of the
multiplication by $\tilde Q^{\natural}$, of rank two on the cone; and
$\tilde Q^{\natural}\tilde Q=C(\tilde Q)e_t=0$, so $\tilde Q$ lies in the annihilator.

**Example.** For the pure zero divisor $\tilde Q=\vec e_x+i\vec e_y$, whose vector part has
$(\vec Q,\vec Q)=1-1=0$, the common annihilator is
$$
A_\star(\vec e_x+i\vec e_y)=\mathbb{C}\{\vec e_x+i\vec e_y,\ \vec e_z-ie_t\},
$$
and for the non-pure zero divisor $\tilde Q=e_t+i\vec e_x$, of algebraic norm $1-1=0$,
$$
A_\star(e_t+i\vec e_x)=\mathbb{C}\{e_t+i\vec e_x,\ \vec e_y+i\vec e_z\}.
$$
In both cases the element lies in its own annihilator and the annihilator is a complex plane.

## The Dichotomy by the Cone

**The annihilator reads the cone twice: off the cone it is $\{0\}$ and the element is a plain unit, on the cone it is a complex plane and the element is a rank-one matrix.**

The zero-divisor set of the block is the punctured cone $\{\tilde Q\neq0:C(\tilde Q)=0\}$, a single
equation, and the annihilator is the finer reading of the same equation: off the cone the
annihilator is $\{0\}$ and the element is a unit of the plain product, and on the cone the
annihilator is a complex plane and the element is a rank-one matrix. The block is the sibling of
the general plain algebra and the twin of the symmetric quaternionic algebra: the first has the
same cone and the same plane but its two sides are distinct, and the second has the same
coincidence of the two sides but its annihilator is a hyperplane for every nonzero element rather
than a plane on a cone. The annihilator is the invariant that separates the three.

## The Annihilator on the Remarkable Subspaces

**On a nonzero central element the annihilator is $\{0\}$; on the vector subspace it is $\{0\}$ unless the vector part is isotropic, and a complex plane on the isotropic locus; and on the Hermitian and anti-Hermitian subspaces it is again a complex plane for a nonzero zero divisor.**

**The centre.** A nonzero central element $\tilde P=\lambda e_t$ has
$L_{\lambda e_t}\tilde Q_1=\lambda\tilde Q_1$, the scalar operator, so it is a unit of the plain
product and its annihilator is $\{0\}$.

**The vector subspace.** A nonzero pure element $\tilde P=\vec P$ has
$L_{\vec P}\tilde Q_1=-\vec P\tilde Q_1$ and $C(\tilde P)=(\vec P,\vec P)$; its annihilator
is $\{0\}$ unless the vector part is isotropic, and on the isotropic locus it is the complex plane
of the elements the pure quaternion $\vec P$ kills by left multiplication.

**The Hermitian and anti-Hermitian subspaces.** On the Hermitian subspace the natural conjugation
is the coefficientwise conjugation of the vector part, and the annihilator of a nonzero Hermitian
zero divisor is again a complex plane; the elements of the annihilator are those killed by the
Hermitian quaternion, a left ideal of the plain algebra.

## Summary

The annihilator of an element in a product is the set of partners the element kills, the left and
the right annihilator being the kernels of the left and the right multiplication. The general
quaternionic multiplication $\tilde P\star\tilde Q_1=\tilde P^{\natural}\tilde Q_1$ carries a
$\mathbb{C}$-linear anti-automorphism of order two, so its two annihilators of an element always
coincide. The operator $L_{\tilde P}$ has determinant $C(\tilde P)^{2}$ and trace $4P_t$: it is
invertible off the cone and of rank two and kernel a complex plane on the cone, and the plane
contains the element itself. The block shares the cone and the plane with the general plain algebra
and the coincidence of the two sides with the symmetric quaternionic algebra, and it is the only
one of the three with both properties.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q$ | the general quaternionic multiplication, the operation $\mathrm{GQA}$ |
| $A_\star(\tilde P),B_\star(\tilde P)$ | the left and the right annihilator of $\tilde P$ in the block, equal by the anti-automorphism ${}^{\natural}$ |
| $L_{\tilde P}$ | the left multiplication operator, $L_{\tilde P}\tilde Q_1=\tilde P^{\natural}\tilde Q_1$, whose kernel is the annihilator |
| $\det L_{\tilde P}=C(\tilde P)^{2}$, $\operatorname{tr}L_{\tilde P}=4P_t$ | the determinant and the trace of the operator |
| $\{0\}$ off the cone | the annihilator of an element of nonzero central square, a unit of the plain product |
| the complex plane on the cone | the annihilator of a nonzero zero divisor, containing the element itself |
| $C(\tilde P)=\sum_\mu P_\mu^{2}$ | the central square, the criterion of the cone |

## Further Reading

- *Definitions for the Study of the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternioid-c-space.md`), §*The Zero Divisor and the Annihilator*, for the zero divisor and the annihilator of a general product.
- *Introduction to the General Quaternionic Algebra* (`articles_maths/introduction-to-the-general-quaternionic-algebra.md`), for the operation, its table and its anti-automorphism.
- *Zero Divisors of the General Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-general-quaternionic-algebra.md`), above this article in this category, for the criterion, the two families and the comparison with the other general products.
- *Zero Divisors of the Biquaternion Algebra* (`articles_maths/zero-divisors-of-the-biquaternion-algebra.md`), for the plain algebra, the cone and the rank-one matrix reading.
- *Annihilators of the Biquaternion Algebra* (`articles_maths/annihilators-of-the-biquaternion-algebra.md`), the sibling block, whose two annihilators of an element are distinct.
- *Annihilators in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/annihilators-in-the-algebraic-structures-over-the-biquaternioid-c-space.md`), the block whose annihilator is a hyperplane for every nonzero element.
