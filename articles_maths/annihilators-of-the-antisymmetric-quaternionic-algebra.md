# __Annihilators of the Antisymmetric Quaternionic Algebra__

## Introduction

The zero divisor of a product is a property of one element alone: it says that *some* nonzero
partner exists that the element kills. The annihilator says *which* partners those are, and it is
the finer object. It is the set of elements killed by a fixed element,
$$
A_\star(\tilde Q)=\{\tilde X:\tilde Q\star\tilde X=0\},\qquad
B_\star(\tilde Q)=\{\tilde X:\tilde X\star\tilde Q=0\},
$$
the left and the right annihilator (*Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*,
§*The Zero Divisor and the Annihilator*). When the product is carried by a multiplication operator
the annihilator is the kernel of that operator, so it is a linear subspace.

The block of this article is the **antisymmetric quaternionic multiplication**
$$
\tilde P\diamond\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde
P\bigr)=P_0\vec Q-Q_0\vec P-\vec P\times\vec Q,
$$
scalar part zero and vector part the mixed term with the cross term subtracted (*Introduction to
the Antisymmetric Quaternionic Algebra of Biquaternions*). It is alternating, so every nonzero
element is a two-sided zero divisor with itself as partner and the zero-divisor set is the whole
punctured space (*Zero Divisors of the Antisymmetric Quaternionic Algebra*, above this article in
this category). The annihilator is where the block is not degenerate: it is the line
$\mathbb{C}\tilde P$ for almost every element and the larger plane only on the zero-divisor cone
$C(\tilde P)=0$ of the parent product. The article owns that reading, the operator with its
characteristic polynomial, and the shape of the annihilator on the remarkable subspaces; the
zero-divisor set and the comparison with the other eleven structures are the cited article's.

**The results.** For the antisymmetric quaternionic multiplication the two annihilators of an element coincide and are the kernel of the left multiplication $L_{\tilde P}$. The operator $L_{\tilde P}$ has trace $3P_0$, determinant $0$ and characteristic polynomial $t(t-P_0)(t^{2}-2P_0t+C(\tilde P))$. Off the zero-divisor cone $C(\tilde P)=0$ of the parent product the annihilator is the line $\mathbb{C}\tilde P$, and on the cone it is the larger plane that contains the line; at $e_0$ the annihilator is the centre $\mathbb{C}e_0$.

## The Annihilator of a Product

**Definition (annihilator).** Let $\star$ be a product on $\mathbb{B}$ and let
$\tilde Q\in\mathbb{B}$. The **left annihilator** and the **right annihilator** of $\tilde Q$ in
$\star$ are
$$
A_\star(\tilde Q)=\{\tilde X:\tilde Q\star\tilde X=0\},\qquad
B_\star(\tilde Q)=\{\tilde X:\tilde X\star\tilde Q=0\}.
$$
They are the kernels of the left and the right multiplication, both nonzero exactly when $\tilde Q$
is a zero divisor of the corresponding side.

Throughout this article the product is the **antisymmetric quaternionic multiplication**
$\diamond$, and unqualified, *annihilator* means the annihilator of $\diamond$. The left
multiplication is the operator
$$
L_{\tilde P}\tilde X=\tilde P\diamond\tilde X,
$$
so that $A_\diamond(\tilde P)=\ker L_{\tilde P}$. The block is the twin of the **antisymmetric
plain algebra**, whose annihilators are *Annihilators of the Antisymmetric Plain Algebra*; the two
twins are the two Lie and near-Lie brackets of the twelve.

## The Two Annihilators Coincide

**For every $\tilde P$ the two annihilators coincide, $B_\diamond(\tilde P)=A_\diamond(\tilde P)=\ker L_{\tilde P}$.**

**Proposition (the two annihilators coincide).** For every $\tilde P$,
$$
B_\diamond(\tilde P)=A_\diamond(\tilde P)=\ker L_{\tilde P}.
$$

*Proof.* The block is alternating, $\tilde X\diamond\tilde P=-\tilde P\diamond\tilde X$, so
$\tilde X\diamond\tilde P=0$ exactly when $\tilde P\diamond\tilde X=0$; the two annihilators are
therefore one set, the kernel of $L_{\tilde P}$.

## The Multiplication Operator and the Characteristic Polynomial

**In the basis $e_0,e_1,e_2,e_3$ the operator $L_{\tilde P}$ of an element $\tilde P=P_0e_0+\vec P$ has trace $3P_0$, determinant $0$ and characteristic polynomial $t(t-P_0)(t^{2}-2P_0t+C(\tilde P))$.**

**Proposition (the operator and its characteristic polynomial).** In the basis $e_0,e_1,e_2,e_3$
the operator $L_{\tilde P}$ of an element $\tilde P=P_0e_0+\vec P$ has matrix
$$
\begin{pmatrix}
0 & 0 & 0 & 0 \\
-P_1 & P_0 & P_3 & -P_2 \\
-P_2 & -P_3 & P_0 & P_1 \\
-P_3 & P_2 & -P_1 & P_0
\end{pmatrix},
$$
its trace is $3P_0$, its determinant is $0$, and its characteristic polynomial is
$$
\chi_{L_{\tilde P}}(t)=t\,(t-P_0)\bigl(t^{2}-2P_0t+C(\tilde P)\bigr),\qquad
C(\tilde P)=\sum_{\mu=0}^{3}P_\mu^{2}.
$$

*Proof.* The first column is $-\vec P$, because $e_0$ has zero scalar part and the mixed term
$-X_0\vec P$ survives; the remaining three columns are $P_0e_k-\vec P\times e_k$. The lower
three-by-three block is $P_0\mathrm{I}_3-[\vec P]_\times$, whose eigenvalues are $P_0$ and
$P_0\pm is$ with $s^{2}=(\vec P,\vec P)$, of characteristic polynomial
$t^{2}-2P_0t+C(\tilde P)$; the extra eigenvalue $0$ is the first column, and the trace $3P_0$ is
the sum of the four eigenvalues. The determinant is the constant term, which is zero.

## The Rank and the Annihilator

**The rank of $L_{\tilde P}$ is three and the annihilator the line $\mathbb{C}\tilde P$ when $C(\tilde P)\neq0$, and on the cone $C(\tilde P)=0$ the rank drops to two and the annihilator grows to a plane; the line $\mathbb{C}\tilde P$ always lies in the annihilator.**

**Corollary (the rank and the annihilator).** The rank of $L_{\tilde P}$ and the annihilator of
$\tilde P$ are

| $\tilde P$ | $C(\tilde P)$ | $\operatorname{rank}L_{\tilde P}$ | $\dim\ker L_{\tilde P}$ |
|---|---|---|---|
| $0$ | $0$ | $0$ | $4$ |
| $\tilde P\neq0$, $C(\tilde P)\neq0$ | $\neq0$ | $3$ | $1$ |
| $\tilde P\neq0$, $C(\tilde P)=0$ | $0$ | $2$ | $2$ |

*Proof.* Write $N=P_0\mathrm{I}_3-[\vec P]_\times$ for the lower block, so that
$N\vec P=P_0\vec P$. If $C(\tilde P)\neq0$ the eigenvalues of $N$ have no zero among them
when $P_0\neq0$, and when $P_0=0$ the two nonzero eigenvalues $\pm is$ with $s^{2}=C(\tilde P)$
give rank two, whose image is the plane orthogonal to $\vec P$; the first column $-\vec P$ is
not in it because $(\vec P,\vec P)=C(\tilde P)\neq0$, so the rank is three in both cases. If
$C(\tilde P)=0$ and $\tilde P\neq0$ the block $N$ has rank two and the first column adds nothing,
either because $N\vec P=P_0\vec P$ or, when $P_0=0$, because the isotropic $\vec P$ lies
in the image of $[\vec P]_\times$; the rank is two. The annihilator has dimension
$4-\operatorname{rank}L_{\tilde P}$.

**Corollary (the line $\mathbb{C}\tilde P$ is always in the annihilator).** For every $\tilde P$
the element $\tilde P$ annihilates itself, $\tilde P\diamond\tilde P=0$, so
$\mathbb{C}\tilde P\subseteq A_\diamond(\tilde P)$; the annihilator is the line
$\mathbb{C}\tilde P$ exactly off the cone, and on the cone it is the larger plane that contains it.

*Proof.* The alternation gives $\tilde P\diamond\tilde P=0$. Off the cone the annihilator is
one-dimensional by the rank table, so it is the line; on the cone it is two-dimensional and
contains the line.

**Example.** At the element $e_0$, $L_{e_0}\tilde X=\vec X$ vanishes exactly on the pure
scalars, so the annihilator is the centre $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$, of dimension
one, and $C(e_0)=1\neq0$. At the element $e_1+ie_2$, of vector part $\vec P=e_1+ie_2$ with
$(\vec P,\vec P)=1+i^{2}=0$, the annihilator is the plane
$$
A_\diamond(e_1+ie_2)=\mathbb{C}\{e_1+ie_2,\ e_3+ie_0\}.
$$

## The Dichotomy by the Cone

**The annihilator separates the elements by the zero-divisor cone $C(\tilde P)=0$ of the parent product: off the cone it is the line $\mathbb{C}\tilde P$, on the cone the larger plane that contains it.**

The zero-divisor set of the block is the whole punctured space, so it separates nothing. The
annihilator separates the elements by the **zero-divisor cone of the parent product**, the locus
$C(\tilde P)=0$: off the cone the annihilator is the line $\mathbb{C}\tilde P$, on the cone it is
the larger plane. The cone is also the criterion of the zero divisor of the sibling general algebra
(*Zero Divisors of the General Quaternionic Algebra*), and the block reads it through the
annihilator alone: the zero-divisor set is blind to it, and the operator is where it appears. The
reading is the twin of the antisymmetric plain algebra, with one difference: there the generic
annihilator is a plane, of complex dimension two, and the jump is to the whole space on the centre,
whereas here the generic annihilator is the line $\mathbb{C}\tilde P$ and the jump is to the plane
on the cone.

## The Annihilator on the Remarkable Subspaces

**On every remarkable subspace the annihilator is the intersection of the ambient annihilator with the subspace: at a nonzero central element it is the centre $\mathbb{C}e_0$, on the vector subspace it meets the subspace in the line $\mathbb{C}\vec P$, the ambient annihilator being the plane $\mathbb{C}e_0\oplus\mathbb{C}\vec P$ when the pure element is isotropic and the line $\mathbb{C}\vec P$ alone when it is not, and every nonzero element of a Hermitian or anti-Hermitian subspace has the nonzero partner it has in the ambient block.**

**The centre.** A nonzero central element $\tilde P=\lambda e_0$ has
$L_{\lambda e_0}\tilde X=\lambda\vec X$, the scalar multiple of the projection onto the vector
subspace, so its annihilator is the centre $\mathbb{C}e_0$: the central elements annihilate the
centre alone.

**The vector subspace.** On the vector subspace, where $P_0=0$ and $\tilde X$ is pure, the
operation is the negative cross product $\tilde P\diamond\tilde X=-\vec P\times\vec X$. The
annihilator of a nonzero pure element meets the vector subspace in the line $\mathbb{C}\vec P$
and is the plane $\mathbb{C}e_0\oplus\mathbb{C}\vec P$ of the ambient space when $\vec P$ is
isotropic, the line $\mathbb{C}\vec P$ alone when it is not.

**The Hermitian and anti-Hermitian subspaces.** The restriction of the block to a subspace
annihilates the same elements as the ambient block intersected with the subspace, so every nonzero
element of every remarkable subspace has a nonzero annihilating partner, the one it has in the
ambient block.

## Summary

The annihilator of an element in a product is the set of partners the element kills, the left and
the right annihilator being the kernels of the left and the right multiplication. The antisymmetric
quaternionic multiplication is alternating, so the two annihilators of an element coincide and
contain the element itself. The operator $L_{\tilde P}$ has trace $3P_0$, determinant $0$ and
characteristic polynomial $t(t-P_0)(t^{2}-2P_0t+C(\tilde P))$: its rank is three and its kernel the
line $\mathbb{C}\tilde P$ off the cone $C(\tilde P)=0$, and on the cone the rank drops to two and
the annihilator grows to the plane that contains the line. At $e_0$ the annihilator is the centre;
the zero-divisor set of the block is the whole punctured space and gives none of this, and the
annihilator is the only invariant of the block that reads the cone.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\diamond\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P)$ | the antisymmetric quaternionic multiplication, the operation $\mathrm{AQA}$ |
| $A_\diamond(\tilde P),B_\diamond(\tilde P)$ | the left and the right annihilator of $\tilde P$ in the block, equal because the block is alternating |
| $L_{\tilde P}$ | the left multiplication operator, $L_{\tilde P}\tilde X=\tilde P\diamond\tilde X$, whose kernel is the annihilator |
| $\chi_{L_{\tilde P}}(t)=t(t-P_0)(t^{2}-2P_0t+C(\tilde P))$ | the characteristic polynomial of the operator |
| $\mathbb{C}\tilde P$ | the annihilator of an element off the cone, a complex line |
| $C(\tilde P)=\sum_\mu P_\mu^{2}$ | the central square, the criterion of the cone on which the annihilator grows |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ | the centre, the annihilator of the nonzero central elements |

## Further Reading

- *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternioid-c-space.md`), §*The Zero Divisor and the Annihilator*, for the zero divisor and the annihilator of a general product.
- *Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-quaternionic-algebra.md`), for the operation and its table.
- *Zero Divisors of the Antisymmetric Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-antisymmetric-quaternionic-algebra.md`), above this article in this category, for the punctured space and the comparison with the other eleven structures.
- *Zero Divisors of the General Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-general-quaternionic-algebra.md`), for the cone $C(\tilde P)=0$, which is the criterion of the parent and the locus of the rank drop.
- *Annihilators of the Antisymmetric Plain Algebra* (`articles_maths/annihilators-of-the-antisymmetric-plain-algebra.md`), the twin block, whose generic annihilator is a plane rather than a line.
- *Remarkable Subspaces under the Antisymmetric Quaternionic Algebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-antisymmetric-quaternionic-algebra.md`), for the elements whose bracket vanishes and for the reading on the subspaces.
