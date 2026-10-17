# __Annihilators of the Biquaternion Algebra__

## Introduction

The zero divisor of a product is a property of one element alone: it says that *some* nonzero
partner exists that the element kills. The annihilator says *which* partners those are, and it is
the finer object. It is the set of elements killed by a fixed element,
$$
A_\star(\tilde Q_2)=\{\tilde Q_1:\tilde Q_2\star\tilde Q_1=0\},\qquad
B_\star(\tilde Q_2)=\{\tilde Q_1:\tilde Q_1\star\tilde Q_2=0\},
$$
the left and the right annihilator (*Definitions for the Study of the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*,
§*The Zero Divisor and the Annihilator*). When the product is carried by a multiplication operator
the annihilator is the kernel of that operator, so it is a linear subspace.

The block of this article is the **general plain multiplication**, the plain product of the
biquaternion algebra,
$$
\tilde Q_2\star\tilde Q_1=\tilde Q_2\tilde Q_1
=\bigl[Q_{2,0}Q_{1t}-(\vec Q_2,\vec Q_1)\bigr]+Q_{2,0}\vec Q_1+Q_{1t}\vec Q_2+\vec Q_2\times\vec Q_1,
$$
the operation of the twelve (*Introduction to the Biquaternion Algebra of
Biquaternions*). It is associative, and the algebra is the complexification of the quaternion
algebra, isomorphic to the matrix algebra $M_2(\mathbb{C})$. Its zero divisors are the elements of
the cone $C(\tilde Q_2)=0$, and a nonzero element of the cone is a rank-one matrix (*Zero Divisors of
the Biquaternion Algebra*, above this article in this category). The annihilator is the kernel of
the corresponding multiplication: it is $\{0\}$ off the cone and a complex plane on the cone, and
the two sides carry two **distinct** planes. The article owns that reading, the two operators with
their ranks, and the shape of the annihilator on the remarkable subspaces; the zero-divisor set is
the cited article's.

**The results.** The annihilator of an element is the set of partners that it kills. For the general plain product the two multiplication operators have trace $4Q_{2,0}$ and determinant $C(\tilde Q_2)^{2}$; both annihilators are trivial off the cone, and each is a complex plane on the cone. The two planes are distinct, and they share the line $\mathbb{C}\tilde Q_2^{\natural}$.

## The Annihilator of a Product

**The annihilator of an element is the set of partners that it kills; the left annihilator is the kernel of the left multiplication and the right annihilator is the kernel of the right multiplication, and both are nonzero exactly when the element is a zero divisor of the corresponding side.**

**Definition (annihilator).** Let $\star$ be a product on $\mathbb{B}$ and let
$\tilde Q_2\in\mathbb{B}$. The **left annihilator** and the **right annihilator** of $\tilde Q_2$ in
$\star$ are
$$
A_\star(\tilde Q_2)=\{\tilde Q_1:\tilde Q_2\star\tilde Q_1=0\},\qquad
B_\star(\tilde Q_2)=\{\tilde Q_1:\tilde Q_1\star\tilde Q_2=0\}.
$$
They are the kernels of the left and the right multiplication, and they are nonzero exactly when
$\tilde Q_2$ is a zero divisor of the corresponding side.

Throughout this article the product is the **general plain multiplication** $\star$, and
unqualified, *annihilator* means the annihilator of $\star$. The two one-sided multiplications are
the operators
$$
L_{\tilde Q_2}\tilde Q_1=\tilde Q_2\tilde Q_1,\qquad R_{\tilde Q_2}\tilde Q_1=\tilde Q_1\tilde Q_2,
$$
the left and the right multiplication of the plain algebra, and the block is the parent of the
other eleven: it is the only one that is associative, and its annihilators are the model for the
two-sided reading. The block carries **no** involution that identifies the sides, so the two
annihilators of an element are generally distinct; the sibling blocks *Annihilators of the General
Quaternionic Algebra*, *Annihilators of the General Plain Sesqualgebra* and *Annihilators of the
General Quaternionic Sesqualgebra* each have an involution that modifies the reading.

## The Multiplication Operators and Their Ranks

**Both multiplication operators have trace $4Q_{2,0}$ and determinant $C(\tilde Q_2)^{2}$; they are invertible off the cone, and on the cone each is of rank two with a kernel of complex dimension two.**

**Proposition (the operators and their determinants).** In the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ the
operators $L_{\tilde Q_2}$ and $R_{\tilde Q_2}$ of an element $\tilde Q_2=Q_{2,0}e_t+\vec Q_2$ have trace
$4Q_{2,0}$ each and determinant
$$
\det L_{\tilde Q_2}=\det R_{\tilde Q_2}=C(\tilde Q_2)^{2},\qquad
C(\tilde Q_2)=\sum_{\mu\in\{t,x,y,z\}}Q_{2\mu}^{2}.
$$

*Proof.* The matrix of $L_{\tilde Q_2}$ is the left multiplication matrix of the quaternion
$\tilde Q_2$, of determinant the square of the quaternion norm $C(\tilde Q_2)$ and trace $4Q_{2,0}$; the
matrix of $R_{\tilde Q_2}$ is the right multiplication matrix, of the same determinant and trace
because it is the transposed-conjugate of the first on the four quaternion units.

**Corollary (the rank and the annihilator).** The ranks of the two operators and the two
annihilators of $\tilde Q_2$ are

| $\tilde Q_2$ | $C(\tilde Q_2)$ | $\operatorname{rank}L_{\tilde Q_2},\operatorname{rank}R_{\tilde Q_2}$ | $\dim A_\star(\tilde Q_2),\dim B_\star(\tilde Q_2)$ |
|---|---|---|---|
| $0$ | $0$ | $0$ | $4$ |
| $\tilde Q_2\neq0$, $C(\tilde Q_2)\neq0$ | $\neq0$ | $4$ | $0$ |
| $\tilde Q_2\neq0$, $C(\tilde Q_2)=0$ | $0$ | $2$ | $2$ |

*Proof.* The determinant $C(\tilde Q_2)^{2}$ is nonzero exactly when $C(\tilde Q_2)\neq0$, and then
both operators are invertible and both annihilators are $\{0\}$. When $C(\tilde Q_2)=0$ the nonzero
element $\tilde Q_2$ is a rank-one matrix of $M_2(\mathbb{C})$, and the left and the right
multiplication by a rank-one matrix have rank two as operators on the four-dimensional matrix
space; the kernels are therefore of complex dimension two. The origin gives the zero operator.

## The Annihilator of an Element

**Off the cone both annihilators are $\{0\}$; on the cone each is a complex plane containing $\tilde Q_2^{\natural}$; and on the cone the two planes are distinct, sharing only the line $\mathbb{C}\tilde Q_2^{\natural}$.**

**Theorem (the dimension of the annihilators).** Let $\tilde Q_2\in\mathbb{B}$.

- If $\tilde Q_2$ is a unit of the plain product, $C(\tilde Q_2)\neq0$, then
$A_\star(\tilde Q_2)=B_\star(\tilde Q_2)=\{0\}$.
- If $\tilde Q_2\neq0$ is a zero divisor, $C(\tilde Q_2)=0$, then $A_\star(\tilde Q_2)$ and
$B_\star(\tilde Q_2)$ are each of complex dimension two, and each contains $\tilde Q_2^{\natural}$.

*Proof.* The first clause is the rank table. For the second, the plain algebra is isomorphic to
$M_2(\mathbb{C})$ and a nonzero element of the cone is a matrix of rank one; the left
multiplication by a rank-one matrix has rank two and kernel dimension two, and the right
multiplication likewise. Finally $\tilde Q_2\tilde Q_2^{\natural}=C(\tilde Q_2)e_t=0$ and
$\tilde Q_2^{\natural}\tilde Q_2=C(\tilde Q_2)e_t=0$, so $\tilde Q_2^{\natural}$ lies in both annihilators;
and $\tilde Q_2$ lies in its own annihilator exactly when $\tilde Q_2^{2}=0$, which on the cone holds
precisely for the pure zero divisors.

**Theorem (the two annihilators are distinct on the cone).** For a nonzero zero divisor $\tilde Q_2$
of the cone the two annihilators $A_\star(\tilde Q_2)$ and $B_\star(\tilde Q_2)$ are distinct complex
planes, and they share the complex line $\mathbb{C}\tilde Q_2^{\natural}$.

*Proof.* Both contain $\tilde Q_2^{\natural}$, as the proof of the preceding theorem shows, so the
intersection contains that line. The examples below show two planes whose second generators differ,
so the planes are distinct; two distinct planes in the four-dimensional space meet in a line, and
the line is the shared $\mathbb{C}\tilde Q_2^{\natural}$.

**Example.** For the non-pure zero divisor $\tilde Q_2=e_t+i\vec e_x$, of central square $1-1=0$, the two
annihilators are
$$
A_\star(e_t+i\vec e_x)=\mathbb{C}\{e_t-i\vec e_x,\ \vec e_z+i\vec e_y\},\qquad
B_\star(e_t+i\vec e_x)=\mathbb{C}\{e_t-i\vec e_x,\ \vec e_z-i\vec e_y\},
$$
and for the pure zero divisor $\tilde Q_2=\vec e_x+i\vec e_y$, of central square $1-1=0$,
$$
A_\star(\vec e_x+i\vec e_y)=\mathbb{C}\{\vec e_x+i\vec e_y,\ e_t+i\vec e_z\},\qquad
B_\star(\vec e_x+i\vec e_y)=\mathbb{C}\{\vec e_x+i\vec e_y,\ e_t-i\vec e_z\}.
$$
In both cases the two planes share the line $\mathbb{C}\tilde Q_2^{\natural}$ and differ in the
second generator.

## The Dichotomy by the Cone

**The annihilator reads the cone twice: off the cone it is trivial and the element is invertible, on the cone it is a complex plane; the block is the one of the general products for which the two sides are genuinely two.**

The zero-divisor set of the block is the punctured cone $\{\tilde Q_2\neq0:C(\tilde Q_2)=0\}$, a single
equation. The annihilator reads the cone twice: off the cone both annihilators are $\{0\}$ and the
element is invertible, and on the cone each annihilator is a complex plane. The block is the parent
of the twelve, and the two readings of the cone are its gift: the sibling general products
*Annihilators of the General Quaternionic Algebra*, *Annihilators of the General Plain
Sesqualgebra* and *Annihilators of the General Quaternionic Sesqualgebra* each keep the cone and
the plane and modify the coincidence of the two sides by their involution. The general plain
algebra is the one for which the two sides are genuinely two.

## The Annihilator on the Remarkable Subspaces

**On every remarkable subspace the annihilator is the intersection of the ambient annihilator with the subspace: trivial off the cone, and a complex plane inside the subspace on the cone.**

**The centre.** A nonzero central element $\tilde Q_2=\lambda e_t$ has
$L_{\lambda e_t}\tilde Q_1=\lambda\tilde Q_1$, the scalar operator, so it is a unit of the plain
product and its annihilator is $\{0\}$.

**The vector subspace.** A nonzero pure element $\tilde Q_2=\vec Q_2$ has central square
$(\vec Q_2,\vec Q_2)$, so it is a zero divisor of the cone exactly when its vector part is
isotropic; then the two annihilators are the complex planes of the elements that the pure
quaternion $\vec Q_2$ kills, read off the multiplication table, and for the isotropic
$\vec Q_2=\vec e_x+i\vec e_y$ they are the planes of the example above.

**The Hermitian and anti-Hermitian subspaces.** On a remarkable subspace the annihilator of an
element of the subspace is the intersection of the ambient plane with the subspace, so the
annihilator of a nonzero element of a remarkable subspace is again a complex plane inside the
subspace, cut out by the same multiplication table.

## Summary

The annihilator of an element in a product is the set of partners the element kills, the left and
the right annihilator being the kernels of the left and the right multiplication. The general plain
multiplication is the associative product of the biquaternion algebra, isomorphic to
$M_2(\mathbb{C})$, and its operator $L_{\tilde Q_2}$ and its transpose $R_{\tilde Q_2}$ have
determinant $C(\tilde Q_2)^{2}$ and trace $4Q_{2,0}$: both are invertible off the cone and of rank two
with a two-dimensional kernel on the cone. Off the cone both annihilators vanish; on the cone each
is a complex plane, and the two planes are **distinct**, sharing the line
$\mathbb{C}\tilde Q_2^{\natural}$. The block is the parent of the other general products, which keep
the cone and the plane and modify the coincidence of the two sides by an involution.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Q_2\star\tilde Q_1=\tilde Q_2\tilde Q_1$ | the general plain multiplication, the operation, the associative product of the biquaternion algebra |
| $A_\star(\tilde Q_2)=\{\tilde Q_1:\tilde Q_2\tilde Q_1=0\}$ | the left annihilator of $\tilde Q_2$, the kernel of the left multiplication |
| $B_\star(\tilde Q_2)=\{\tilde Q_1:\tilde Q_1\tilde Q_2=0\}$ | the right annihilator of $\tilde Q_2$, the kernel of the right multiplication |
| $L_{\tilde Q_2},R_{\tilde Q_2}$ | the left and the right multiplication operators, of determinant $C(\tilde Q_2)^{2}$ and trace $4Q_{2,0}$ |
| $C(\tilde Q_2)=\sum_\mu Q_{2\mu}^{2}$ | the central square, the criterion of the cone |
| the complex planes on the cone | the two annihilators of a nonzero zero divisor, distinct and sharing the line $\mathbb{C}\tilde Q_2^{\natural}$ |

## Further Reading

- *Definitions for the Study of the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternioid-c-space.md`), §*The Zero Divisor and the Annihilator*, for the zero divisor and the annihilator of a general product.
- *Introduction to the Biquaternion Algebra* (`articles_maths/introduction-to-the-biquaternion-algebra.md`), for the operation, its associativity and its table.
- *Zero Divisors of the Biquaternion Algebra* (`articles_maths/zero-divisors-of-the-biquaternion-algebra.md`), above this article in this category, for the cone, the two families and the rank-one matrix reading.
- *Zero Divisors in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/zero-divisors-in-the-algebraic-structures-over-the-biquaternioid-c-space.md`), for the coincidence of the four zero-divisor sets on the cone and the one-sided inverse equations.
- *Annihilators of the General Quaternionic Algebra* (`articles_maths/annihilators-of-the-general-quaternionic-algebra.md`), the sibling whose anti-automorphism makes the two annihilators coincide.
- *Annihilators of the General Plain Sesqualgebra* (`articles_maths/annihilators-of-the-general-plain-sesqualgebra.md`), the sibling whose conjugate-linear star identifies the two sides.
