# __Annihilators of the General Quaternionic Algebra__

## Introduction

The zero divisor of a product is a property of one element alone: it says that *some* nonzero
partner exists that the element kills. The annihilator says *which* partners those are, and it is
the finer object. It is the set of elements killed by a fixed element,
$$
A_\star(\tilde Q)=\{\tilde X:\tilde Q\star\tilde X=0\},\qquad
B_\star(\tilde Q)=\{\tilde X:\tilde X\star\tilde Q=0\},
$$
the left and the right annihilator (*Definitions for the Study of the 12 Algebraic Structures*,
§*The Zero Divisor and the Annihilator*). When the product is carried by a multiplication operator
the annihilator is the kernel of that operator, so it is a linear subspace.

The block of this article is the **general quaternionic multiplication**
$$
\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q
=\bigl[P_0Q_0+(\mathbf P,\mathbf Q)\bigr]+P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q,
$$
the product of the natural conjugate of the first factor with the second (*Introduction to the
General Quaternionic Algebra of Biquaternions*). It is neither commutative nor alternating, and yet
a two-sided involution ties the two sides: the natural conjugation is a $\mathbb{C}$-linear
anti-automorphism of order two, so it carries the left annihilator
$\{\tilde X:\tilde X^{\natural}\tilde Q=0\}$ onto the right annihilator
$\{\tilde Q^{\natural}\tilde X=0\}$, and the two annihilators of an element coincide. The
annihilator vanishes off the zero-divisor cone $C(\tilde P)=0$ and is a complex plane on it. The
article owns that reading, the operator with its rank, and the shape of the annihilator on the
remarkable subspaces; the zero-divisor set and its comparison with the other three general products
are the cited article's.

## The Annihilator of a Product

**Definition (annihilator).** Let $\star$ be a product on $\mathbb{B}$ and let
$\tilde Q\in\mathbb{B}$. The **left annihilator** and the **right annihilator** of $\tilde Q$ in
$\star$ are
$$
A_\star(\tilde Q)=\{\tilde X:\tilde Q\star\tilde X=0\},\qquad
B_\star(\tilde Q)=\{\tilde X:\tilde X\star\tilde Q=0\}.
$$
They are the kernels of the left and the right multiplication, and they are nonzero exactly when
$\tilde Q$ is a zero divisor of the corresponding side.

Throughout this article the product is the **general quaternionic multiplication** $\star$, and
unqualified, *annihilator* means the annihilator of $\star$. The left and the right multiplication
are the operator
$$
L_{\tilde P}\tilde X=\tilde P\star\tilde X=\tilde P^{\natural}\tilde X,\qquad
R_{\tilde P}\tilde X=\tilde X\star\tilde P=\tilde X^{\natural}\tilde P,
$$
a multiplication by the natural conjugate. The block is the sibling of the **general plain
algebra**, whose annihilators are *Annihilators of the General Plain Algebra*, and the two share
the cone and its plane but differ in the coincidence of the two sides.

## The Two Annihilators Coincide

**Theorem (the coincidence).** For **every** $\tilde Q\in\mathbb{B}$, unit or zero divisor alike,
$$
B_\star(\tilde Q)=A_\star(\tilde Q).
$$

*Proof.* Let $\tilde X\in\mathbb{B}$. Applying the natural conjugation ${}^{\natural}$ to the
equation $\tilde Q^{\natural}\tilde X=0$ gives $(\tilde Q^{\natural}\tilde X)^{\natural}=0$, which
is $\tilde X^{\natural}\tilde Q=0$ because ${}^{\natural}$ is an anti-automorphism of order two;
the argument reverses because ${}^{\natural}$ is a bijection of $\mathbb{B}$ onto itself. Hence
$\tilde Q\star\tilde X=0$ exactly when $\tilde X\star\tilde Q=0$, and the two annihilators contain
exactly the same elements.

The coincidence is a property of this product: it holds because ${}^{\natural}$ is a
$\mathbb{C}$-**linear** anti-automorphism of order two, so the first factor can be conjugated away
without changing the annihilation. The general plain algebra has no such involution and its two
annihilators are generally distinct.

## The Multiplication Operator and the Rank

**Proposition (the operator and its determinant).** In the basis $e_0,e_1,e_2,e_3$ the operator
$L_{\tilde P}$ of an element $\tilde P=P_0e_0+\mathbf P$ has the matrix of multiplication by
$\tilde P^{\natural}$, of trace $4P_0$ and determinant
$$
\det L_{\tilde P}=C(\tilde P)^{2},\qquad C(\tilde P)=\sum_{\mu=0}^{3}P_\mu^{2}.
$$

*Proof.* The matrix is the left multiplication matrix of the quaternion $\tilde P^{\natural}$,
whose determinant is the square of the quaternion norm $C(\tilde P^{\natural})=C(\tilde P)$; the
natural conjugation keeps the four squares, so the determinant is $C(\tilde P)^{2}$. The trace is
the sum of the four diagonal entries, $4P_0$.

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
nonzero element of the cone is a matrix of rank one (*Zero Divisors of the General Plain Algebra*),
whence the kernel is of complex dimension two. The origin gives the zero operator.

## The Annihilator of an Element

**Theorem (the dimension of the annihilator).** Let $\tilde Q\in\mathbb{B}$.

- If $\tilde Q$ is a unit of the plain product, $C(\tilde Q)\neq0$, then
$A_\star(\tilde Q)=B_\star(\tilde Q)=\{0\}$.
- If $\tilde Q\neq0$ is a zero divisor, $C(\tilde Q)=0$, then $A_\star(\tilde Q)$ and
$B_\star(\tilde Q)$ are equal, of complex dimension two, and the common annihilator contains
$\tilde Q$.

*Proof.* The first clause is the rank table. For the second, the annihilator is the kernel of the
multiplication by $\tilde Q^{\natural}$, of rank two on the cone; and
$\tilde Q^{\natural}\tilde Q=C(\tilde Q)e_0=0$, so $\tilde Q$ lies in the annihilator.

**Example.** For the pure zero divisor $\tilde Q=e_1+ie_2$, whose vector part has
$(\mathbf Q,\mathbf Q)=1-1=0$, the common annihilator is
$$
A_\star(e_1+ie_2)=\mathbb{C}\{e_1+ie_2,\ e_3-ie_0\},
$$
and for the non-pure zero divisor $\tilde Q=e_0+ie_1$, of algebraic norm $1-1=0$,
$$
A_\star(e_0+ie_1)=\mathbb{C}\{e_0+ie_1,\ e_2+ie_3\}.
$$
In both cases the element lies in its own annihilator and the annihilator is a complex plane.

## The Dichotomy by the Cone

The zero-divisor set of the block is the punctured cone $\{\tilde Q\neq0:C(\tilde Q)=0\}$, a single
equation, and the annihilator is the finer reading of the same equation: off the cone the
annihilator is $\{0\}$ and the element is a unit of the plain product, and on the cone the
annihilator is a complex plane and the element is a rank-one matrix. The block is the sibling of
the general plain algebra and the twin of the symmetric quaternionic algebra: the first has the
same cone and the same plane but its two sides are distinct, and the second has the same
coincidence of the two sides but its annihilator is a hyperplane for every nonzero element rather
than a plane on a cone. The annihilator is the invariant that separates the three.

## The Annihilator on the Remarkable Subspaces

**The centre.** A nonzero central element $\tilde P=\lambda e_0$ has
$L_{\lambda e_0}\tilde X=\lambda\tilde X$, the scalar operator, so it is a unit of the plain
product and its annihilator is $\{0\}$.

**The vector subspace.** A nonzero pure element $\tilde P=\mathbf P$ has
$L_{\mathbf P}\tilde X=-\mathbf P\tilde X$ and $C(\tilde P)=(\mathbf P,\mathbf P)$; its annihilator
is $\{0\}$ unless the vector part is isotropic, and on the isotropic locus it is the complex plane
of the elements the pure quaternion $\mathbf P$ kills by left multiplication.

**The Hermitian and anti-Hermitian subspaces.** On the Hermitian subspace the natural conjugation
is the coefficientwise conjugation of the vector part, and the annihilator of a nonzero Hermitian
zero divisor is again a complex plane; the elements of the annihilator are those killed by the
Hermitian quaternion, a left ideal of the plain algebra.

## Summary

The annihilator of an element in a product is the set of partners the element kills, the left and
the right annihilator being the kernels of the left and the right multiplication. The general
quaternionic multiplication $\tilde P\star\tilde X=\tilde P^{\natural}\tilde X$ carries a
$\mathbb{C}$-linear anti-automorphism of order two, so its two annihilators of an element always
coincide. The operator $L_{\tilde P}$ has determinant $C(\tilde P)^{2}$ and trace $4P_0$: it is
invertible off the cone and of rank two and kernel a complex plane on the cone, and the plane
contains the element itself. The block shares the cone and the plane with the general plain algebra
and the coincidence of the two sides with the symmetric quaternionic algebra, and it is the only
one of the three with both properties.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q$ | the general quaternionic multiplication, the operation $\mathrm{GQA}$ |
| $A_\star(\tilde P),B_\star(\tilde P)$ | the left and the right annihilator of $\tilde P$ in the block, equal by the anti-automorphism ${}^{\natural}$ |
| $L_{\tilde P}$ | the left multiplication operator, $L_{\tilde P}\tilde X=\tilde P^{\natural}\tilde X$, whose kernel is the annihilator |
| $\det L_{\tilde P}=C(\tilde P)^{2}$, $\operatorname{tr}L_{\tilde P}=4P_0$ | the determinant and the trace of the operator |
| $\{0\}$ off the cone | the annihilator of an element of nonzero central square, a unit of the plain product |
| the complex plane on the cone | the annihilator of a nonzero zero divisor, containing the element itself |
| $C(\tilde P)=\sum_\mu P_\mu^{2}$ | the central square, the criterion of the cone |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), §*The Zero Divisor and the Annihilator*, for the zero divisor and the annihilator of a general product.
- *Introduction to the General Quaternionic Algebra of Biquaternions* (`articles_maths/introduction-to-the-general-quaternionic-algebra-of-biquaternions.md`), for the operation, its table and its anti-automorphism.
- *Zero Divisors of the General Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-general-quaternionic-algebra.md`), above this article in this category, for the criterion, the two families and the comparison with the other general products.
- *Zero Divisors of the General Plain Algebra* (`articles_maths/zero-divisors-of-the-general-plain-algebra.md`), for the plain algebra, the cone and the rank-one matrix reading.
- *Annihilators of the General Plain Algebra* (`articles_maths/annihilators-of-the-general-plain-algebra.md`), the sibling block, whose two annihilators of an element are distinct.
- *Annihilators of the Symmetric Quaternionic Algebra* (`articles_maths/annihilators-of-the-symmetric-quaternionic-algebra.md`), the block whose annihilator is a hyperplane for every nonzero element.
