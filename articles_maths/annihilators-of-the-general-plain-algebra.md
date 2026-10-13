# __Annihilators of the General Plain Algebra__

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

The block of this article is the **general plain multiplication**, the plain product of the
biquaternion algebra,
$$
\tilde P\star\tilde Q=\tilde P\tilde Q
=\bigl[P_0Q_0-(\mathbf P,\mathbf Q)\bigr]+P_0\mathbf Q+Q_0\mathbf P+\mathbf P\times\mathbf Q,
$$
the operation $\mathrm{GPA}$ of the twelve (*Introduction to the General Plain Algebra of
Biquaternions*). It is associative, and the algebra is the complexification of the quaternion
algebra, isomorphic to the matrix algebra $M_2(\mathbb{C})$. Its zero divisors are the elements of
the cone $C(\tilde P)=0$, and a nonzero element of the cone is a rank-one matrix (*Zero Divisors of
the General Plain Algebra*, above this article in this category). The annihilator is the kernel of
the corresponding multiplication: it is $\{0\}$ off the cone and a complex plane on the cone, and
the two sides carry two **distinct** planes. The article owns that reading, the two operators with
their ranks, and the shape of the annihilator on the remarkable subspaces; the zero-divisor set is
the cited article's.

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

Throughout this article the product is the **general plain multiplication** $\star$, and
unqualified, *annihilator* means the annihilator of $\star$. The two one-sided multiplications are
the operators
$$
L_{\tilde P}\tilde X=\tilde P\tilde X,\qquad R_{\tilde P}\tilde X=\tilde X\tilde P,
$$
the left and the right multiplication of the plain algebra, and the block is the parent of the
other eleven: it is the only one that is associative, and its annihilators are the model for the
two-sided reading. The block carries **no** involution that identifies the sides, so the two
annihilators of an element are generally distinct; the sibling blocks *Annihilators of the General
Quaternionic Algebra*, *Annihilators of the General Plain Sesqualgebra* and *Annihilators of the
General Quaternionic Sesqualgebra* each have an involution that modifies the reading.

## The Multiplication Operators and Their Ranks

**Proposition (the operators and their determinants).** In the basis $e_0,e_1,e_2,e_3$ the
operators $L_{\tilde P}$ and $R_{\tilde P}$ of an element $\tilde P=P_0e_0+\mathbf P$ have trace
$4P_0$ each and determinant
$$
\det L_{\tilde P}=\det R_{\tilde P}=C(\tilde P)^{2},\qquad
C(\tilde P)=\sum_{\mu=0}^{3}P_\mu^{2}.
$$

*Proof.* The matrix of $L_{\tilde P}$ is the left multiplication matrix of the quaternion
$\tilde P$, of determinant the square of the quaternion norm $C(\tilde P)$ and trace $4P_0$; the
matrix of $R_{\tilde P}$ is the right multiplication matrix, of the same determinant and trace
because it is the transposed-conjugate of the first on the four quaternion units.

**Corollary (the rank and the annihilator).** The ranks of the two operators and the two
annihilators of $\tilde P$ are

| $\tilde P$ | $C(\tilde P)$ | $\operatorname{rank}L_{\tilde P},\operatorname{rank}R_{\tilde P}$ | $\dim A_\star(\tilde P),\dim B_\star(\tilde P)$ |
|---|---|---|---|
| $0$ | $0$ | $0$ | $4$ |
| $\tilde P\neq0$, $C(\tilde P)\neq0$ | $\neq0$ | $4$ | $0$ |
| $\tilde P\neq0$, $C(\tilde P)=0$ | $0$ | $2$ | $2$ |

*Proof.* The determinant $C(\tilde P)^{2}$ is nonzero exactly when $C(\tilde P)\neq0$, and then
both operators are invertible and both annihilators are $\{0\}$. When $C(\tilde P)=0$ the nonzero
element $\tilde P$ is a rank-one matrix of $M_2(\mathbb{C})$, and the left and the right
multiplication by a rank-one matrix have rank two as operators on the four-dimensional matrix
space; the kernels are therefore of complex dimension two. The origin gives the zero operator.

## The Annihilator of an Element

**Theorem (the dimension of the annihilators).** Let $\tilde Q\in\mathbb{B}$.

- If $\tilde Q$ is a unit of the plain product, $C(\tilde Q)\neq0$, then
$A_\star(\tilde Q)=B_\star(\tilde Q)=\{0\}$.
- If $\tilde Q\neq0$ is a zero divisor, $C(\tilde Q)=0$, then $A_\star(\tilde Q)$ and
$B_\star(\tilde Q)$ are each of complex dimension two, and each contains $\tilde Q^{\natural}$.

*Proof.* The first clause is the rank table. For the second, the plain algebra is isomorphic to
$M_2(\mathbb{C})$ and a nonzero element of the cone is a matrix of rank one; the left
multiplication by a rank-one matrix has rank two and kernel dimension two, and the right
multiplication likewise. Finally $\tilde Q\tilde Q^{\natural}=C(\tilde Q)e_0=0$ and
$\tilde Q^{\natural}\tilde Q=C(\tilde Q)e_0=0$, so $\tilde Q^{\natural}$ lies in both annihilators;
and $\tilde Q$ lies in its own annihilator exactly when $\tilde Q^{2}=0$, which on the cone holds
precisely for the pure zero divisors.

**Theorem (the two annihilators are distinct on the cone).** For a nonzero zero divisor $\tilde Q$
of the cone the two annihilators $A_\star(\tilde Q)$ and $B_\star(\tilde Q)$ are distinct complex
planes, and they share the complex line $\mathbb{C}\tilde Q^{\natural}$.

*Proof.* Both contain $\tilde Q^{\natural}$, as the proof of the preceding theorem shows, so the
intersection contains that line. The examples below show two planes whose second generators differ,
so the planes are distinct; two distinct planes in the four-dimensional space meet in a line, and
the line is the shared $\mathbb{C}\tilde Q^{\natural}$.

**Example.** For the non-pure zero divisor $\tilde Q=e_0+ie_1$, of central square $1-1=0$, the two
annihilators are
$$
A_\star(e_0+ie_1)=\mathbb{C}\{e_0-ie_1,\ e_3+ie_2\},\qquad
B_\star(e_0+ie_1)=\mathbb{C}\{e_0-ie_1,\ e_3-ie_2\},
$$
and for the pure zero divisor $\tilde Q=e_1+ie_2$, of central square $1-1=0$,
$$
A_\star(e_1+ie_2)=\mathbb{C}\{e_1+ie_2,\ e_0+ie_3\},\qquad
B_\star(e_1+ie_2)=\mathbb{C}\{e_1+ie_2,\ e_0-ie_3\}.
$$
In both cases the two planes share the line $\mathbb{C}\tilde Q^{\natural}$ and differ in the
second generator.

## The Dichotomy by the Cone

The zero-divisor set of the block is the punctured cone $\{\tilde Q\neq0:C(\tilde Q)=0\}$, a single
equation. The annihilator reads the cone twice: off the cone both annihilators are $\{0\}$ and the
element is invertible, and on the cone each annihilator is a complex plane. The block is the parent
of the twelve, and the two readings of the cone are its gift: the sibling general products
*Annihilators of the General Quaternionic Algebra*, *Annihilators of the General Plain
Sesqualgebra* and *Annihilators of the General Quaternionic Sesqualgebra* each keep the cone and
the plane and modify the coincidence of the two sides by their involution. The general plain
algebra is the one for which the two sides are genuinely two.

## The Annihilator on the Remarkable Subspaces

**The centre.** A nonzero central element $\tilde P=\lambda e_0$ has
$L_{\lambda e_0}\tilde X=\lambda\tilde X$, the scalar operator, so it is a unit of the plain
product and its annihilator is $\{0\}$.

**The vector subspace.** A nonzero pure element $\tilde P=\mathbf P$ has central square
$(\mathbf P,\mathbf P)$, so it is a zero divisor of the cone exactly when its vector part is
isotropic; then the two annihilators are the complex planes of the elements that the pure
quaternion $\mathbf P$ kills, read off the multiplication table, and for the isotropic
$\mathbf P=e_1+ie_2$ they are the planes of the example above.

**The Hermitian and anti-Hermitian subspaces.** On a remarkable subspace the annihilator of an
element of the subspace is the intersection of the ambient plane with the subspace, so the
annihilator of a nonzero element of a remarkable subspace is again a complex plane inside the
subspace, cut out by the same multiplication table.

## Summary

The annihilator of an element in a product is the set of partners the element kills, the left and
the right annihilator being the kernels of the left and the right multiplication. The general plain
multiplication is the associative product of the biquaternion algebra, isomorphic to
$M_2(\mathbb{C})$, and its operator $L_{\tilde P}$ and its transpose $R_{\tilde P}$ have
determinant $C(\tilde P)^{2}$ and trace $4P_0$: both are invertible off the cone and of rank two
with a two-dimensional kernel on the cone. Off the cone both annihilators vanish; on the cone each
is a complex plane, and the two planes are **distinct**, sharing the line
$\mathbb{C}\tilde Q^{\natural}$. The block is the parent of the other general products, which keep
the cone and the plane and modify the coincidence of the two sides by an involution.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q=\tilde P\tilde Q$ | the general plain multiplication, the operation $\mathrm{GPA}$, the associative product of the biquaternion algebra |
| $A_\star(\tilde P)=\{\tilde X:\tilde P\tilde X=0\}$ | the left annihilator of $\tilde P$, the kernel of the left multiplication |
| $B_\star(\tilde P)=\{\tilde X:\tilde X\tilde P=0\}$ | the right annihilator of $\tilde P$, the kernel of the right multiplication |
| $L_{\tilde P},R_{\tilde P}$ | the left and the right multiplication operators, of determinant $C(\tilde P)^{2}$ and trace $4P_0$ |
| $C(\tilde P)=\sum_\mu P_\mu^{2}$ | the central square, the criterion of the cone |
| the complex planes on the cone | the two annihilators of a nonzero zero divisor, distinct and sharing the line $\mathbb{C}\tilde P^{\natural}$ |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), §*The Zero Divisor and the Annihilator*, for the zero divisor and the annihilator of a general product.
- *Introduction to the General Plain Algebra of Biquaternions* (`articles_maths/introduction-to-the-general-plain-algebra-of-biquaternions.md`), for the operation, its associativity and its table.
- *Zero Divisors of the General Plain Algebra* (`articles_maths/zero-divisors-of-the-general-plain-algebra.md`), above this article in this category, for the cone, the two families and the rank-one matrix reading.
- *Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/zero-divisors-in-the-12-algebraic-structures-over-the-biquaternion-c-space.md`), for the coincidence of the four zero-divisor sets on the cone and the one-sided inverse equations.
- *Annihilators of the General Quaternionic Algebra* (`articles_maths/annihilators-of-the-general-quaternionic-algebra.md`), the sibling whose anti-automorphism makes the two annihilators coincide.
- *Annihilators of the General Plain Sesqualgebra* (`articles_maths/annihilators-of-the-general-plain-sesqualgebra.md`), the sibling whose conjugate-linear star identifies the two sides.
