# __Annihilators of the Antisymmetric Plain Algebra__

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
the annihilator is the kernel of that operator, so it is a linear subspace and its computation is
one of linear algebra.

The block of this article is the **antisymmetric plain multiplication**
$$
\tilde P\wedge\tilde Q=\tfrac12\bigl(\tilde P\tilde Q-\tilde Q\tilde P\bigr)=\vec P\times\vec Q,
$$
the cross product of the two vector parts; it is $\mathbb{C}$-bilinear, alternating and vector
valued (*Introduction to the Antisymmetric Plain Algebra of Biquaternions*). Its zero-divisor set
is degenerate, the block being alternating: every nonzero element is a two-sided zero divisor with
itself as partner, and the set is the whole punctured space (*Zero Divisors of the Antisymmetric
Plain Algebra*, above this article in this category). The annihilator is where the block is **not**
degenerate, and that is the content of this article. It separates the central line, whose nonzero
elements kill every element of the space, from the non-central elements, whose annihilator is a
plane that depends on the element. The article owns the annihilator of the block: the coincidence
of its two sides, the multiplication operator with its characteristic polynomial, the rank table,
the dichotomy by the vector part, and the shape of the annihilator on the remarkable subspaces. The
zero-divisor set itself and the comparison with the other eleven structures are the cited
article's, and the pairs of elements whose bracket vanishes are *Remarkable Subspaces under the
Antisymmetric Plain Algebra of Biquaternions*.

**The results.** The two annihilators of the antisymmetric plain multiplication coincide, $B_\wedge(\tilde P)=A_\wedge(\tilde P)=\ker L_{\tilde P}$, because the block is alternating. The operator $L_{\tilde P}$ has matrix $\operatorname{diag}(0,C_{\vec P})$, trace $0$, determinant $0$ and characteristic polynomial $t^{2}(t^{2}+(\vec P,\vec P))$; its rank is $2$ off the centre, where the annihilator is the plane $\mathbb{C}_{\mathbb{B}}\oplus\mathbb{C}\vec P$ of complex dimension $2$, and $0$ on the centre, whose nonzero elements annihilate the whole space. The dichotomy is therefore by the vector part, where the parent plain product's is by the scalar part.

## The Annihilator of a Product

**Definition (annihilator).** Let $\star$ be a product on $\mathbb{B}$ and let
$\tilde Q\in\mathbb{B}$. The **left annihilator** and the **right annihilator** of $\tilde Q$ in
$\star$ are
$$
A_\star(\tilde Q)=\{\tilde X:\tilde Q\star\tilde X=0\},\qquad
B_\star(\tilde Q)=\{\tilde X:\tilde X\star\tilde Q=0\}.
$$
The element $\tilde Q$ is a left zero divisor precisely when $A_\star(\tilde Q)\neq\{0\}$ and
$\tilde Q\neq0$, and a right zero divisor precisely when $B_\star(\tilde Q)\neq\{0\}$ and
$\tilde Q\neq0$; the annihilator is thus the object that decides the zero-divisor property, element
by element.

Throughout this article the product is the **antisymmetric plain multiplication** $\wedge$, and
unqualified, *annihilator* means the annihilator of $\wedge$. The multiplication operator of the
block is
$$
L_{\tilde P}\tilde X=\tilde P\wedge\tilde X,
$$
so that $A_\wedge(\tilde P)=\ker L_{\tilde P}$.

## The Two Annihilators Coincide

**For every $\tilde P$ the left and the right annihilator of the block coincide, $B_\wedge(\tilde P)=A_\wedge(\tilde P)=\ker L_{\tilde P}$.**

**Proposition (the two annihilators coincide).** For every $\tilde P$,
$$
B_\wedge(\tilde P)=A_\wedge(\tilde P)=\ker L_{\tilde P}.
$$

*Proof.* The block is alternating, $\tilde X\wedge\tilde P=-\tilde P\wedge\tilde X$, so
$\tilde X\wedge\tilde P=0$ exactly when $\tilde P\wedge\tilde X=0$; the two annihilators are
therefore one set, the kernel of $L_{\tilde P}$.

**Remark (the coincidence fails for the neighbouring products).** The left and the right
annihilator are distinct for the plain product, whose left and right multiplications by $\tilde P$
are different operators, and the plain product's zero divisor therefore comes in a left and a right
version. For the block the distinction is empty, and a zero divisor of the block is two-sided for
the same reason that the two annihilators coincide.

## The Multiplication Operator

**The operator $L_{\tilde P}$ has matrix $\operatorname{diag}(0,C_{\vec P})$, trace $0$, determinant $0$ and characteristic polynomial $\chi_{L_{\tilde P}}(t)=t^{2}(t^{2}+(\vec P,\vec P))$, with eigenvalues $0$ doubled and the two roots of $t^{2}+(\vec P,\vec P)$.**

**Proposition (the operator in the standard basis).** In the basis $e_0,e_1,e_2,e_3$ the operator
$L_{\tilde P}$ of an element $\tilde P=P_0e_0+\vec P$ has matrix
$$
\operatorname{diag}(0,C_{\vec P})=
\begin{pmatrix}
0 & 0 & 0 & 0 \\
0 & 0 & -P_3 & P_2 \\
0 & P_3 & 0 & -P_1 \\
0 & -P_2 & P_1 & 0
\end{pmatrix},
$$
where $C_{\vec P}$ is the $3\times3$ skew matrix of the cross product
$\vec X\mapsto\vec P\times\vec X$.

*Proof.* The first column is zero, because the scalar direction of $\tilde P$ is invisible and
$\tilde P\wedge e_0=\vec P\times\mathbf 0=0$; the remaining three columns are
$\tilde P\wedge e_k=\vec P\times\mathbf e_k$, which are the columns of $C_{\vec P}$.

**Proposition (the characteristic polynomial).** The trace of $L_{\tilde P}$ is $0$, its
determinant is $0$, and its characteristic polynomial is
$$
\chi_{L_{\tilde P}}(t)=t^{2}\bigl(t^{2}+(\vec P,\vec P)\bigr),\qquad
(\vec P,\vec P)=\sum_{k=1}^{3}P_k^{2}.
$$
The eigenvalues are $0$ with multiplicity two and the two roots of $t^{2}+(\vec P,\vec P)$.

*Proof.* The matrix is $\operatorname{diag}(0,C_{\vec P})$. Its trace is that of
$C_{\vec P}$, which is zero because $C_{\vec P}$ is skew; its determinant is zero because the
first row is zero. Its characteristic polynomial is the product of the characteristic polynomial
$t$ of the scalar block and that of the skew matrix $C_{\vec P}$, namely
$t\bigl(t^{2}+(\vec P,\vec P)\bigr)$, since the eigenvalues of $C_{\vec P}$ are $0$ and
$\pm is$ with $s^{2}=(\vec P,\vec P)$. Computed exactly on general elements of
$\mathbb{Q}(i)$ coefficients.

**Remark (the operator vanishes exactly on the centre).** $L_{\tilde P}$ is the zero operator
exactly when $C_{\vec P}=0$, that is when $\vec P=0$: the central elements $P_0e_0$ are
precisely the elements whose multiplication operator is zero. This is the rank drop at the centre,
and the annihilator reads it as follows.

## The Rank and the Annihilator

**The rank of $L_{\tilde P}$ and the annihilator depend only on the vector part: the rank is $0$ at $\vec P=0$, where the annihilator is the whole space $\mathbb{B}$, and $2$ at $\vec P\neq0$, where the annihilator is the plane $\mathbb{C}_{\mathbb{B}}\oplus\mathbb{C}\vec P$ of complex dimension $2$.**

The annihilator of $\tilde P$ is the kernel of $L_{\tilde P}$, so its size is the nullity of a
$4\times4$ matrix, and the rank of that matrix is all that has to be computed.

**Corollary (the rank and the annihilator).** The rank of $L_{\tilde P}$ and the annihilator of
$\tilde P$ depend only on the vector part $\vec P$, and there are two cases,

| $\vec P$ | $\operatorname{rank}L_{\tilde P}$ | $\dim\ker L_{\tilde P}$ | $\ker L_{\tilde P}$ |
|---|---|---|---|
| $0$ | $0$ | $4$ | $\mathbb{B}$ |
| $\neq0$ | $2$ | $2$ | $\mathbb{C}_{\mathbb{B}}\oplus\mathbb{C}\vec P$ |

with $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ the centre of the algebra.

*Proof.* The cross-product matrix $C_{\vec P}$ of a nonzero vector $\vec P$ has rank two
whatever the value of $(\vec P,\vec P)$: a skew matrix of odd size is singular, its rank is
even, and it is nonzero. The matrix of $L_{\tilde P}$ is $\operatorname{diag}(0,C_{\vec P})$, of
the same rank two, and its kernel is the direct sum of the kernel $\mathbb{C}e_0$ of the scalar
direction and the kernel of $C_{\vec P}$, which is $\mathbb{C}\vec P$ because
$\vec P\times\vec X=0$ exactly when $\vec X$ is parallel to $\vec P$. At $\vec P=0$
the operator is zero and the kernel is the whole space. The kernel equals the displayed span on
every tested non-central element, computed exactly on a grid of $100$ elements of $\mathbb{Q}(i)$.

**Remark (no rank drop on the isotropic locus).** On the non-central elements the rank is two, so
the annihilator is the same two-dimensional plane for all of them. The isotropic locus of the
vector form, $(\vec P,\vec P)=0$, does not change the rank; it only merges the two nonzero
eigenvalues $\pm is$ into the double zero. This is a difference from the antisymmetric quaternionic
sibling of the block, whose rank drops on the zero-divisor cone of its parent (*Zero Divisors of
the Antisymmetric Quaternionic Algebra*).

**Remark (the rank drops on the centre).** The rank does drop, and it drops on the centre alone: an
element $\tilde P=P_0e_0$ has $\vec P=0$, so $L_{\tilde P}=0$, of rank zero, and its annihilator
is the whole space. The nonzero central elements are therefore left and right annihilators of
*every* element of the block, $\tilde P\wedge\tilde X=0$ and $\tilde X\wedge\tilde P=0$ for all
$\tilde X$.

## The Dichotomy by the Vector Part

**The annihilator's dichotomy is by the vector part: an element with $\vec P=0$ has annihilator $\mathbb{B}$, and an element with $\vec P\neq0$ has annihilator the plane $\mathbb{C}_{\mathbb{B}}\oplus\mathbb{C}\vec P$; the block's dichotomy is the parent's, read from the vector part instead of the scalar part.**

The parent plain product classifies its zero divisors into a pure and a non-pure family, split by
the vanishing of the scalar part $Q_0$ (*Zero Divisors of the General Plain Algebra*, §*The Two
Families of Zero Divisors*), and that classification collapses for the block, the criterion being
met by the pure and the non-pure elements alike (*Zero Divisors of the Antisymmetric Plain
Algebra*, §*The Classification Collapses*). What the block retains at this level is a dichotomy,
and it is the annihilator's.

**Theorem (the annihilator's dichotomy is by the vector part).** An element with $\vec P=0$ has
annihilator $\mathbb{B}$; an element with $\vec P\neq0$ has annihilator the plane
$\mathbb{C}_{\mathbb{B}}\oplus\mathbb{C}\vec P$. The dichotomy is read from the vector part
where the parent's is read from the scalar part: the block's is the parent's transposed.

*Proof.* Both cases are the rank computation of §*The Rank and the Annihilator*.

**Remark (why the zero-divisor classification dissolves).** The parent's two families come from the
two terms of its square, $\tilde Q^{2}=[Q_0^{2}-(\vec Q,\vec Q)]e_0+2Q_0\vec Q$, the
central term and the vector term, which are read from the scalar part. In the block the square is a
pure vector and vanishes identically, $\tilde Q\wedge\tilde Q=0$, so neither term that separated
the parent's families survives. The classification does not merely merge; it is dissolved, and the
annihilator's dichotomy by the vector part is what the block retains at this level.

## The Annihilator on the Remarkable Subspaces

**On each remarkable subspace the restriction is alternating, with the annihilator collapsing to the whole space on the centre and reading as the plane $\mathbb{C}e_0\oplus\mathbb{C}\vec P$ on the vector subspace.**

**Proposition (the restriction is alternating).** On each of the remarkable subspaces the block
restricts to an operation whose zero-divisor class is the relative class: the nonzero elements of
the subspace are zero divisors, with themselves as partners, because the restriction of an
alternating product is alternating.

*Proof.* The restriction of the block to a subspace is the block read on the elements of the
subspace, and $\tilde X\wedge\tilde X=0$ for every $\tilde X$ of the ambient space, hence for every
element of the subspace (*Introduction to the Antisymmetric Plain Algebra of Biquaternions*).

The subspaces differ in the annihilator, and the difference is the shape of the kernel. On the
centre the operation vanishes identically, so the annihilator of a nonzero central element is the
whole space and the operation is the zero operation. On the vector subspace, where the operation is
the cross product on $\mathbb{C}^{3}$, the annihilator of a nonzero vector $\vec P$ meets the
vector subspace in the line $\mathbb{C}\vec P$ and is the plane
$\mathbb{C}e_0\oplus\mathbb{C}\vec P$ of the ambient space: of its two dimensions, one is the
vector direction of the element itself, the other the scalar direction, which lies outside the
vector subspace. The reading of the operation on the six subspaces, and the elements whose bracket
vanishes, are *Remarkable Subspaces under the Antisymmetric Plain Algebra of Biquaternions*.

## Summary

The annihilator of an element in a product is the set of partners the element kills, the left and
the right annihilator being the kernels of the left and the right multiplication. For the
antisymmetric plain multiplication $\tilde P\wedge\tilde Q=\vec P\times\vec Q$ the two
coincide, $B_\wedge(\tilde P)=A_\wedge(\tilde P)=\ker L_{\tilde P}$, because the product is
alternating. The operator $L_{\tilde P}$ has matrix $\operatorname{diag}(0,C_{\vec P})$ and
characteristic polynomial $t^{2}(t^{2}+(\vec P,\vec P))$: its rank is two on the non-central
elements, where the annihilator is the plane $\mathbb{C}_{\mathbb{B}}\oplus\mathbb{C}\vec P$,
and it is zero on the central line, whose nonzero elements annihilate the whole space. The
annihilator therefore separates the two classes of the block by the vector part, the central
elements and the non-central elements, where the parent plain product separates its zero divisors
by the scalar part; the classification of the zero divisors into two families does not exist for
the block, the criterion being met by the pure and the non-pure elements alike, and the dichotomy
that survives is the annihilator's. On the remarkable subspaces the restriction is alternating,
with the annihilator collapsing to the whole space on the centre and reading as the plane
$\mathbb{C}e_0\oplus\mathbb{C}\vec P$ on the vector subspace.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\wedge\tilde Q=\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)=\vec P\times\vec Q$ | the antisymmetric plain multiplication, the operation $\mathrm{APA}$ |
| $A_\wedge(\tilde P),B_\wedge(\tilde P)$ | the left and the right annihilator of $\tilde P$ in the block, equal because the block is alternating |
| $L_{\tilde P}$ | the left multiplication operator, $L_{\tilde P}\tilde X=\tilde P\wedge\tilde X$, whose kernel is the annihilator |
| $C_{\vec P}$ | the $3\times3$ skew matrix of the cross product $\vec X\mapsto\vec P\times\vec X$, so that the matrix of $L_{\tilde P}$ is $\operatorname{diag}(0,C_{\vec P})$ |
| $\chi_{L_{\tilde P}}(t)=t^{2}(t^{2}+(\vec P,\vec P))$ | the characteristic polynomial of the operator |
| $\mathbb{C}_{\mathbb{B}}\oplus\mathbb{C}\vec P$ | the annihilator of a non-central element $\tilde P$ |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ | the central line, on which the operator vanishes and the annihilator is the whole space |
| $(\vec P,\vec P)=\sum_k P_k^{2}$ | the vector form, whose vanishing does not change the rank |

## Further Reading

- *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternioid-c-space.md`), for the zero divisor and the annihilator of a general product and for the relativity of the definition.
- *Introduction to the Antisymmetric Plain Algebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-plain-algebra.md`), for the operation, its alternation and its table.
- *Zero Divisors of the Antisymmetric Plain Algebra* (`articles_maths/zero-divisors-of-the-antisymmetric-plain-algebra.md`), above this article in this category, for the zero-divisor set, the criterion and the comparison with the other eleven structures.
- *Zero Divisors of the General Plain Algebra* (`articles_maths/zero-divisors-of-the-biquaternion-algebra.md`), for the criterion, the two families and the structure of the zero divisors of the parent plain product.
- *Zero Divisors of the Antisymmetric Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-antisymmetric-quaternionic-algebra.md`), the sibling of the block, whose operator has the central-square cone of its parent as the locus of its rank drop.
- *Remarkable Subspaces under the Antisymmetric Plain Algebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-antisymmetric-plain-algebra.md`), for the elements whose bracket vanishes and for the reading on the subspaces.
