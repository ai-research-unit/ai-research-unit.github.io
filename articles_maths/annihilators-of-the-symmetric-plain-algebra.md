# __Annihilators of the Symmetric Plain Algebra__

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

The block of this article is the **symmetric plain multiplication**
$$
\tilde P\bullet\tilde Q=\tfrac12\bigl(\tilde P\tilde Q+\tilde Q\tilde P\bigr)
=\bigl[P_0Q_0-(\vec P,\vec Q)\bigr]+P_0\vec Q+Q_0\vec P,
$$
the Jordan product (*Introduction to the Symmetric Plain Algebra of Biquaternions*). It is
commutative, so the left and the right multiplication by an element are one operator and the two
annihilators of the element are one set. The zero-divisor set of the block is the union of the
vector subspace and the central-square cone, the two clauses of one criterion (*Zero Divisors of
the Symmetric Plain Algebra*, above this article in this category). The annihilator keeps the two
families apart: a pure element annihilates a plane and an element of the cone with nonzero scalar
part annihilates a line. The article owns that reading, the operator with its rank, and the shape
of the annihilator on the remarkable subspaces; the zero-divisor set and its criterion are the
cited article's.

**The results.** The annihilator of an element is the set of partners that it kills; the block is commutative, so the left and the right annihilator coincide and are the kernel of the one multiplication operator $L_{\tilde P}$. For the block the operator has trace $4P_0$ and determinant $P_0^{2}C(\tilde P)$: the annihilator is trivial off the zero-divisor set, a complex plane $\{\tilde X:X_0=0,\ (\vec P,\vec X)=0\}$ for a non-zero pure element, and the complex line $\mathbb{C}\tilde Q^{\natural}$ for an element with $Q_0\neq0$ and $C(\tilde Q)=0$.

## The Annihilator of a Product

**The annihilator of an element is the set of partners that it kills; the left annihilator and the right annihilator are the kernels of the left and the right multiplication, and they are non-zero exactly when the element is a zero divisor of the corresponding side.**

**Definition (annihilator).** Let $\star$ be a product on $\mathbb{B}$ and let
$\tilde Q\in\mathbb{B}$. The **left annihilator** and the **right annihilator** of $\tilde Q$ in
$\star$ are
$$
A_\star(\tilde Q)=\{\tilde X:\tilde Q\star\tilde X=0\},\qquad
B_\star(\tilde Q)=\{\tilde X:\tilde X\star\tilde Q=0\}.
$$
They are the kernels of the left and the right multiplication, and they are nonzero exactly when
$\tilde Q$ is a zero divisor of the corresponding side.

Throughout this article the product is the **symmetric plain multiplication** $\bullet$, and
unqualified, *annihilator* means the annihilator of $\bullet$. The left and the right
multiplication of the block are the operator
$$
L_{\tilde P}\tilde X=\tilde P\bullet\tilde X,\qquad
R_{\tilde P}\tilde X=\tilde X\bullet\tilde P,
$$
and the block is its own twin, the **general plain bilinear product**, whose annihilators are
*Annihilators of the General Plain Algebra*.

## The Two Annihilators Coincide

**The block is commutative, so the two annihilators of an element coincide: $B_\bullet(\tilde P)=A_\bullet(\tilde P)=\ker L_{\tilde P}$ for every $\tilde P$.**

**Proposition (the two annihilators coincide).** For every $\tilde P$,
$$
B_\bullet(\tilde P)=A_\bullet(\tilde P)=\ker L_{\tilde P}.
$$

*Proof.* The block is commutative, $\tilde X\bullet\tilde P=\tilde P\bullet\tilde X$, so
$\tilde X\bullet\tilde P=0$ exactly when $\tilde P\bullet\tilde X=0$; the two annihilators are
therefore one set, and it is the kernel of the one operator of the block,
$L_{\tilde P}=R_{\tilde P}$.

## The Multiplication Operator and the Rank

**In the basis $e_0,e_1,e_2,e_3$ the operator $L_{\tilde P}$ has trace $4P_0$ and determinant $\det L_{\tilde P}=P_0^{2}C(\tilde P)$: it is invertible off the zero-divisor set, of rank two with a two-dimensional kernel on the pure family, and of rank three with a one-dimensional kernel on the scalar family.**

**Proposition (the operator and its characteristic polynomial).** In the basis $e_0,e_1,e_2,e_3$
the operator $L_{\tilde P}$ of an element $\tilde P=P_0e_0+\vec P$ has matrix
$$
\begin{pmatrix}
P_0 & -P_1 & -P_2 & -P_3 \\
P_1 & P_0 & 0 & 0 \\
P_2 & 0 & P_0 & 0 \\
P_3 & 0 & 0 & P_0
\end{pmatrix},
$$
its trace is $4P_0$ and its determinant is
$$
\det L_{\tilde P}=P_0^{2}\,C(\tilde P),\qquad C(\tilde P)=\sum_{\mu=0}^{3}P_\mu^{2}.
$$

*Proof.* The columns are the values $\tilde P\bullet e_j$. The trace is the sum of the diagonal
entries, $4P_0$; the determinant is the product of the three eigenvalues $P_0$ of the vector part
with the Schur complement $P_0-(\vec P,\vec P)/P_0$, namely
$P_0^{3}\bigl(P_0-(\vec P,\vec P)/P_0\bigr)=P_0^{2}\bigl(P_0^{2}-(\vec P,\vec P)\bigr)=P_0^{2}C(\tilde P)$
when $P_0\neq0$; and when $P_0=0$ both sides vanish, the image of $L_{\tilde P}=L_{\vec P}$ being contained in $\mathrm{span}\{e_0\}+\mathbb{C}\vec P$, of dimension at most two. Hence $\det L_{\tilde P}=P_0^{2}C(\tilde P)$ for every $\tilde P$.

**Corollary (the rank and the annihilator).** The rank of $L_{\tilde P}$ and the annihilator of
$\tilde P$ are

| $\tilde P$ | $C(\tilde P)$ | $\operatorname{rank}L_{\tilde P}$ | $\dim\ker L_{\tilde P}$ |
|---|---|---|---|
| $0$ | $0$ | $0$ | $4$ |
| $\tilde P\neq0$, $P_0=0$, $\vec P\neq0$ | $(\vec P,\vec P)\neq0$ | $2$ | $2$ |
| $\tilde P\neq0$, $P_0\neq0$, $C(\tilde P)=0$ | $0$ | $3$ | $1$ |
| $\tilde P\neq0$, $P_0\neq0$, $C(\tilde P)\neq0$ | $\neq0$ | $4$ | $0$ |

*Proof.* A pure element has $P_0=0$, so the matrix is the direct sum of the zero scalar block and
the nonzero vector $\vec P$, of rank two, and the kernel is the plane of the pure elements
orthogonal to $\vec P$, of dimension two. A non-pure element has $P_0\neq0$: the three vector
columns are independent and span a three-dimensional space, and the fourth column raises the rank
to four exactly when $P_0^{2}\neq(\vec P,\vec P)$, that is exactly when $C(\tilde P)\neq0$.
At $C(\tilde P)=0$ the fourth column lies in the span of the three, and the rank is three. The last
case is the origin.

## The Annihilator of an Element

**A non-zero pure element has the pure plane annihilator $\{\tilde X:X_0=0,\ (\vec Q,\vec X)=0\}$, of complex dimension two; a non-zero element with $Q_0\neq0$ and $C(\tilde Q)=0$ has the line annihilator $\mathbb{C}\tilde Q^{\natural}$; and an element that is neither has annihilator $\{0\}$.**

The criterion of the block is the pair of clauses $P_0=0$ or $C(\tilde P)=0$ (*Zero Divisors of the
Symmetric Plain Algebra*, §*The Two Families*). Each clause has its own annihilator.

**Theorem (the annihilator of a pure element).** For a nonzero pure element $\tilde Q=\vec Q$,
$$
A_\bullet(\tilde Q)=B_\bullet(\tilde Q)
=\{\tilde X=X_0e_0+\vec X:\ X_0=0,\ (\vec Q,\vec X)=0\},
$$
the pure plane orthogonal to the vector part, of complex dimension two. The element belongs to its
own annihilator and is a nilpotent of index two.

*Proof.* The product of two pure elements is $\tilde Q\bullet\tilde X=-(\vec Q,\vec X)e_0$;
the kernel is the set above, and in the three-dimensional complex vector subspace the single
equation $(\vec Q,\vec X)=0$ has a two-dimensional solution space.

**Theorem (the annihilator of an element of the cone with nonzero scalar part).** For a nonzero
element $\tilde Q$ with $Q_0\neq0$ and $C(\tilde Q)=0$,
$$
A_\bullet(\tilde Q)=B_\bullet(\tilde Q)=\mathbb{C}\,\tilde Q^{\natural},
$$
the complex line spanned by the natural conjugate.

*Proof.* The natural conjugate gives $\tilde Q\bullet\tilde Q^{\natural}=C(\tilde Q)e_0=0$, so the
line $\mathbb{C}\tilde Q^{\natural}$ lies in the annihilator. Every element of the kernel has
$X_0=0$ and on $\vec X$ the single conjugacy-free equation $Q_0\vec X=X_0\vec Q$ forced by
the vector part of the product, whose determinant vanishes through the factor $C(\tilde Q)$; the
kernel is therefore exactly one-dimensional and equal to that line.

**Corollary (the annihilator vanishes off the zero-divisor set).** For an element that is neither
pure nor of the vanishing central square the annihilator is $\{0\}$: the element is regular.

## The Dichotomy

**The annihilator separates the two families the criterion joins: a pure element annihilates a plane and an element of the cone with non-zero scalar part annihilates a line, the plane being the kernel of a rank-two operator and the line the kernel of a rank-three operator.**

The zero-divisor set of the block is the union of the two families, and the criterion is a single
union that does not separate them. The annihilator does: a pure element annihilates a plane and an
element of the cone annihilates a line, so the dimension of the annihilator reads the family where
the criterion does not. The two families are also the two ends of the operator: the plane is the
kernel of a rank-two operator and the line is the kernel of a rank-three operator, and the jump
from $2$ to $3$ in the rank is the jump from the rank-two family to the rank-three family. The line
is the sharpest case: it is $\mathbb{C}\tilde Q^{\natural}$, and up to the scalar it is the set of
the idempotents of the block (*Square Roots of One and the Idempotents of the Symmetric Plain Algebra*).

## The Annihilator on the Remarkable Subspaces

**A non-zero central element annihilates nothing; a non-zero pure element, whose annihilator in the ambient space is a plane, has it fall to the line $\mathbb{C}\vec P$ inside the vector subspace; and on the Hermitian subspace the annihilator of a non-zero pure Hermitian element is again a pure plane containing the real line of the element.**

**The centre.** A nonzero central element $\tilde P=\lambda e_0$ has $C(\lambda e_0)=\lambda^{2}$
and $\vec P=0$, so it is regular and its annihilator is $\{0\}$: the centre annihilates nothing.

**The vector subspace.** A nonzero pure element $\tilde P=\vec P$ has the plane annihilator
above. Inside the vector subspace the annihilator falls to the line $\mathbb{C}\vec P$: the
single equation $(\vec P,\vec X)=0$ is the orthogonal plane of the ambient space, and its
intersection with the vector subspace is the line through $\vec P$.

**The Hermitian and anti-Hermitian subspaces.** On the Hermitian subspace the coefficients satisfy
$\overline{Q_k}=Q_k$ and the bilinear form $(\vec Q,\vec X)$ is Hermitian; the annihilator of
a nonzero pure Hermitian element is again a pure plane, and it contains the real line of the
element.

## Summary

The annihilator of an element in a product is the set of partners the element kills, the left and
the right annihilator being the kernels of the left and the right multiplication. The symmetric
plain multiplication is commutative, so the two annihilators of an element coincide and are the
kernel of the one operator
$\tilde P\bullet\tilde X=[P_0X_0-(\vec P,\vec X)]+P_0\vec X+X_0\vec P$, whose
determinant is $P_0^{2}C(\tilde P)$. The annihilator keeps apart the two families that the
zero-divisor criterion joins: a pure element annihilates the complex plane
$\{\tilde X:X_0=0,\ (\vec P,\vec X)=0\}$ and an element with $Q_0\neq0$ and $C(\tilde Q)=0$
annihilates the complex line $\mathbb{C}\tilde Q^{\natural}$, and every other element is regular.
On the remarkable subspaces the annihilator of a pure element collapses from the ambient plane to
the line through the element inside the vector subspace, and the centre annihilates nothing.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\bullet\tilde Q=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ | the symmetric plain multiplication, the operation $\mathrm{SPA}$ |
| $A_\bullet(\tilde P),B_\bullet(\tilde P)$ | the left and the right annihilator of $\tilde P$ in the block, equal because the block is commutative |
| $L_{\tilde P}$ | the left multiplication operator, $L_{\tilde P}\tilde X=\tilde P\bullet\tilde X$, whose kernel is the annihilator |
| $\det L_{\tilde P}=P_0^{2}C(\tilde P)$, $\operatorname{tr}L_{\tilde P}=4P_0$ | the determinant and the trace of the operator |
| $\{\tilde X:X_0=0,\ (\vec P,\vec X)=0\}$ | the annihilator of a nonzero pure element, a complex plane |
| $\mathbb{C}\tilde Q^{\natural}$ | the annihilator of an element with $Q_0\neq0$ and $C(\tilde Q)=0$, a complex line |
| $C(\tilde P)=\sum_\mu P_\mu^{2}$ | the central square, the criterion of the second family |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), §*The Zero Divisor and the Annihilator*, for the zero divisor and the annihilator of a general product.
- *Introduction to the Symmetric Plain Algebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-plain-algebra-of-biquaternions.md`), for the Jordan product, its commutativity and its table.
- *Zero Divisors of the Symmetric Plain Algebra* (`articles_maths/zero-divisors-of-the-symmetric-plain-algebra.md`), above this article in this category, for the criterion and the two families of the zero-divisor set.
- *Zero Divisors of the General Plain Algebra* (`articles_maths/zero-divisors-of-the-general-plain-algebra.md`), the parent product, whose annihilator is a plane of the cone and vanishes off the cone.
- *Square Roots of One and the Idempotents of the Symmetric Plain Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-symmetric-plain-algebra.md`), for the identification of the line $\mathbb{C}\tilde Q^{\natural}$ with the idempotents of the block.
- *Square Roots of Zero and the Nilpotents of the Symmetric Plain Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-symmetric-plain-algebra.md`), for the square-zero elements, the pure isotropic cone of the block.
