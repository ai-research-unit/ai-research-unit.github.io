# __Annihilators of the Antisymmetric Plain Algebra__

## Introduction

The zero divisor of a product is a property of one element alone: it says that *some* nonzero
partner exists that the element kills. The annihilator says *which* partners those are, and it is
the finer object. It is the set of elements killed by a fixed element,
$$
A_\star(\tilde p)=\{\tilde x:\tilde p\star\tilde x=0\},\qquad
B_\star(\tilde p)=\{\tilde x:\tilde x\star\tilde p=0\},
$$
the left and the right annihilator; the zero divisor and the radical are *Definitions for the Study
of the 6 Algebraic Structures*, §*The Element Vocabulary*. When the product is carried by a
multiplication operator the annihilator is the kernel of that operator, so it is a linear subspace
and its computation is one of linear algebra.

The block of this article is the **antisymmetric plain multiplication**
$$
\tilde p\times\tilde q=\tfrac12\bigl(\tilde p\tilde q-\tilde q\tilde p\bigr)=\vec p\times\vec q,
$$
the cross product of the two vector parts; it is $\mathbb{R}$-bilinear, alternating, of zero scalar
part and without a unit (*Introduction to the Antisymmetric Plain Algebra of Quaternions*). Its
zero-divisor set is degenerate, the block being alternating: every nonzero element is a two-sided
zero divisor with itself as partner, and the set is the whole punctured space (*Zero Divisors of
the Antisymmetric Plain Algebra*, above this article in this category). The annihilator is where
the block is **not** degenerate, and that is the content of this article. It separates the central
line, whose nonzero elements kill every element of the space, from the noncentral elements, whose
annihilator is a real plane that depends on the element. The article owns the annihilator of the
block: the coincidence of its two sides, the multiplication operator with its characteristic
polynomial, the rank table, the dichotomy by the vector part, and the shape of the annihilator on
the two remarkable subspaces. The zero-divisor set itself and the comparison with the other five
structures are the cited article's.

The annihilator of this article is not the object of *Annihilators in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, the structure-level article of
the comparison group: that article fixes the product and asks which elements kill the **whole**
space, the radical, and finds the scalar line for the cross product alone; here the element is
fixed and the partners vary.

## The Annihilator of a Product

**Definition (annihilator).** Let $\star$ be a product on $\mathbb{H}$ and let
$\tilde p\in\mathbb{H}$. The **left annihilator** and the **right annihilator** of $\tilde p$ in
$\star$ are
$$
A_\star(\tilde p)=\{\tilde x:\tilde p\star\tilde x=0\},\qquad
B_\star(\tilde p)=\{\tilde x:\tilde x\star\tilde p=0\}.
$$
The element $\tilde p$ is a left zero divisor precisely when $A_\star(\tilde p)\neq\{0\}$ and
$\tilde p\neq0$, and a right zero divisor precisely when $B_\star(\tilde p)\neq\{0\}$ and
$\tilde p\neq0$; the annihilator is thus the object that decides the zero-divisor property, element
by element. The two-sided annihilator of the whole space, the common kernel over all elements, is
the radical of the product.

Throughout this article the product is the **antisymmetric plain multiplication** $\times$, and
unqualified, *annihilator* means the annihilator of $\times$. The multiplication operator of the
block is
$$
L_{\tilde p}\tilde x=\tilde p\times\tilde x,
$$
so that $A_\times(\tilde p)=\ker L_{\tilde p}$.

## The Two Annihilators Coincide

**Proposition (the two annihilators coincide).** For every $\tilde p$,
$$
B_\times(\tilde p)=A_\times(\tilde p)=\ker L_{\tilde p}.
$$

*Proof.* The block is alternating, $\tilde x\times\tilde p=-\tilde p\times\tilde x$, so
$\tilde x\times\tilde p=0$ exactly when $\tilde p\times\tilde x=0$; the two annihilators are
therefore one set, the kernel of $L_{\tilde p}$.

**Remark (why the two sides coincide).** The coincidence is a consequence of the alternation and
not of the symmetry. Over $\mathbb{R}$ the plain product is a division algebra, so for a nonzero
element its two annihilators are $\{0\}$ and the difference of the two sides is invisible; for the
block both sides are nonzero and equal, and a zero divisor of the block is two-sided for the same
reason that the two annihilators coincide.

## The Annihilator of an Element

**Theorem (the annihilator).** For an element $\tilde p=p_0e_0+\vec p$ the annihilator is
$$
A_\times(\tilde p)=\{\tilde x:\tilde p\times\tilde x=0\}
=\begin{cases}
\mathbb{R}e_0\oplus\mathbb{R}\vec p, & \vec p\neq0,\\[2pt]
\mathbb{H}, & \vec p=0 .
\end{cases}
$$
For a noncentral element it is the real plane spanned by the centre and the vector part of the
element, of real dimension two; for a central element every element is annihilated.

*Proof.* If $\vec p\neq0$, the equation $\vec p\times\vec x=0$ holds exactly when
$\vec x$ is parallel to $\vec p$, a line of the vector subspace, and the scalar coordinate
$x_0$ is free and adds the centre; with the centre that is the plane
$\mathbb{R}e_0\oplus\mathbb{R}\vec p$, of real dimension two. If $\tilde p=\lambda e_0$ with
$\lambda\neq0$, then $\tilde p\times\tilde x=\lambda e_0\times\tilde x=0$ for every $\tilde x$. The
criterion for the parallelism is the one of *Zero Divisors of the Antisymmetric Plain Algebra*,
above this article in this category.

## The Multiplication Operator and the Rank

**Proposition (the operator in the standard basis).** In the basis $e_0,e_1,e_2,e_3$ the operator
$L_{\tilde p}$ of an element $\tilde p=p_0e_0+\vec p$ has matrix
$$
\operatorname{diag}(0,C_{\vec p})=
\begin{pmatrix}
0 & 0 & 0 & 0 \\
0 & 0 & -p_3 & p_2 \\
0 & p_3 & 0 & -p_1 \\
0 & -p_2 & p_1 & 0
\end{pmatrix},
$$
where $C_{\vec p}=[\vec p]_\times$ is the $3\times3$ skew matrix of the cross product
$\vec x\mapsto\vec p\times\vec x$.

*Proof.* The first column is zero, because the scalar direction of $\tilde p$ is invisible and
$\tilde p\times e_0=\vec p\times\mathbf 0=0$; the remaining three columns are
$\tilde p\times e_k=\vec p\times\mathbf e_k$, which are the columns of $C_{\vec p}$.

**Proposition (the invariants).** The trace of $L_{\tilde p}$ is $0$, its determinant is $0$, and
its characteristic polynomial is
$$
\chi_{L_{\tilde p}}(t)=t^{2}\bigl(t^{2}+|\vec p|^{2}\bigr),\qquad
|\vec p|^{2}=\sum_{k=1}^{3}p_k^{2}.
$$
The eigenvalues are $0$ with multiplicity two and the two roots of $t^{2}+|\vec p|^{2}$.

*Proof.* The matrix is $\operatorname{diag}(0,C_{\vec p})$. Its trace is that of
$C_{\vec p}$, which is zero because $C_{\vec p}$ is skew; its determinant is zero because the
first row is zero. Its characteristic polynomial is the product of the characteristic polynomial
$t$ of the scalar block and that of the skew matrix $C_{\vec p}$, namely
$t(t^{2}+|\vec p|^{2})$, since the eigenvalues of $C_{\vec p}$ are $0$ and
$\pm i|\vec p|$. Computed exactly on general elements of $\mathbb{Q}$ coefficients.

**Remark (the rank drops on the centre alone).** $L_{\tilde p}$ is the zero operator exactly when
$C_{\vec p}=0$, that is when $\vec p=0$: the central elements $p_0e_0$ are precisely the
elements whose multiplication operator is zero. This is the only rank drop, and the annihilator
reads it at once.

**Corollary (the rank and the annihilator).** The rank of $L_{\tilde p}$ and the annihilator of
$\tilde p$ depend only on the vector part $\vec p$, and there are two cases,

| $\vec p$ | $\operatorname{rank}L_{\tilde p}$ | $\dim\ker L_{\tilde p}$ | $\ker L_{\tilde p}$ |
|---|---|---|---|
| $0$ | $0$ | $4$ | $\mathbb{H}$ |
| $\neq0$ | $2$ | $2$ | $\mathbb{R}e_0\oplus\mathbb{R}\vec p$ |

All dimensions are real dimensions, the space being the real vector space
$\mathbb{H}\cong\mathbb{R}^4$.

*Proof.* The cross-product matrix $C_{\vec p}$ of a nonzero vector $\vec p$ has rank two: a
skew matrix of odd size is singular, its rank is even, and it is nonzero. The matrix of
$L_{\tilde p}$ is $\operatorname{diag}(0,C_{\vec p})$, of the same rank two, and its kernel is
the direct sum of the kernel $\mathbb{R}e_0$ of the scalar direction and the kernel of
$C_{\vec p}$, which is $\mathbb{R}\vec p$ because $\vec p\times\vec x=0$ exactly when
$\vec x$ is parallel to $\vec p$. At $\vec p=0$ the operator is zero and the kernel is the
whole space. The kernel equals the displayed span on every tested noncentral element, computed
exactly on a grid of $100$ elements of $\mathbb{Q}$.

**Remark (no rank drop on an isotropic locus).** Over $\mathbb{R}$ the vector form
$|\vec p|^{2}$ is positive definite, so its only zero is $\vec p=0$: there is no isotropic
locus besides the centre, and the rank drops on the centre alone. The complex sibling has a vector
form that can vanish at a nonzero $\vec P$, but its rank is two there as well, and the vanishing
only merges the two nonzero eigenvalues $\pm i|\vec P|$ into a double zero (*Annihilators of the
Antisymmetric Plain Algebra*, the biquaternion article of the same name).

## The Dichotomy

**Theorem (the annihilator's dichotomy is by the vector part).** An element with $\vec p=0$ has
annihilator $\mathbb{H}$; an element with $\vec p\neq0$ has annihilator the plane
$\mathbb{R}e_0\oplus\mathbb{R}\vec p$. The dichotomy is read from the vector part.

*Proof.* Both cases are the rank computation of §*The Multiplication Operator and the Rank*.

**Remark (the dichotomy is the annihilator's alone).** Every nonzero element of the block is a zero
divisor, so the zero-divisor class does not separate the elements and carries no dichotomy here
(*Zero Divisors of the Antisymmetric Plain Algebra*, above this article in this category). The
dichotomy is the annihilator's: it separates the central elements, which kill the whole space, from
the noncentral ones, which kill a plane. The central line $\mathbb{R}e_0$ is contained in every
annihilator: it is the scalar direction of the plane, and it is the annihilator of the central
elements themselves.

**Remark (no cone, and the complex sibling).** The separation is by the vanishing of the vector
part and not by a quadratic condition; the block carries no cone, and the whole space consists of
zero divisors. Over $\mathbb{R}$ the vector form is definite, so its only zero is the centre and
there is no isotropic locus to complicate the picture. The complex sibling *Annihilators of the
Antisymmetric Plain Algebra* (`articles_maths/annihilators-of-the-antisymmetric-plain-algebra.md`)
reads the same plane over $\mathbb{C}$, of complex dimension two; there the dichotomy is the
transpose of its parent's classification of the zero divisors by the scalar part, and the vanishing
of the vector form there does not change the annihilator.

## The Annihilator on the Remarkable Subspaces

The quaternion space has two remarkable real subspaces, the scalar line
$\mathbb{R}_{\mathbb{H}}=\mathbb{R}e_0$ and the vector subspace $\mathrm{Vect}(\mathbb{H})$
(*Introduction to the Remarkable Subspaces of the Quaternions*).

**Proposition (the restriction is alternating).** On each of the two subspaces the block restricts
to an operation whose zero-divisor class is the relative class: the nonzero elements of the
subspace are zero divisors, with themselves as partners, because the restriction of an alternating
product is alternating.

*Proof.* The restriction of the block to a subspace is the block read on the elements of the
subspace, and $\tilde x\times\tilde x=0$ for every $\tilde x$ of the ambient space, hence for every
element of the subspace (*Introduction to the Antisymmetric Plain Algebra of Quaternions*).

The two subspaces differ in the annihilator, and the difference is the shape of the kernel. On the
centre the operation vanishes identically, so the annihilator of a nonzero central element is the
whole space and the operation is the zero operation. On the vector subspace, where the operation is
the cross product on $\mathbb{R}^{3}$, the annihilator of a nonzero vector $\vec p$ meets the
vector subspace in the line $\mathbb{R}\vec p$ and is the plane
$\mathbb{R}e_0\oplus\mathbb{R}\vec p$ of the ambient space: of its two real dimensions, one is
the vector direction of the element itself, the other the scalar direction, which lies outside the
vector subspace.

## Summary

The annihilator of an element in a product is the set of partners the element kills, the left and
the right annihilator being the kernels of the left and the right multiplication. For the
antisymmetric plain multiplication $\tilde p\times\tilde q=\vec p\times\vec q$ the two
coincide, $B_\times(\tilde p)=A_\times(\tilde p)=\ker L_{\tilde p}$, because the product is
alternating. The operator $L_{\tilde p}$ has matrix $\operatorname{diag}(0,C_{\vec p})$ and
characteristic polynomial $t^{2}(t^{2}+|\vec p|^{2})$: its rank is two on the noncentral
elements, where the annihilator is the real plane $\mathbb{R}e_0\oplus\mathbb{R}\vec p$, and it
is zero on the central line, whose nonzero elements annihilate the whole space. The annihilator
therefore separates the two classes of the block by the vector part, the central elements and the
noncentral elements; every nonzero element is already a zero divisor, so the separation is the
annihilator's alone, and no cone cuts it. On the two remarkable subspaces the restriction is
alternating, with the annihilator collapsing to the whole space on the centre and reading as the
plane $\mathbb{R}e_0\oplus\mathbb{R}\vec p$ on the vector subspace. Over $\mathbb{C}$ the
sibling article reads the same plane, of complex dimension two.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde p\times\tilde q=\tfrac12(\tilde p\tilde q-\tilde q\tilde p)=\vec p\times\vec q$ | the antisymmetric plain multiplication, the operation $\mathrm{APA}$ |
| $A_\times(\tilde p),B_\times(\tilde p)$ | the left and the right annihilator of $\tilde p$ in the block, equal because the block is alternating |
| $L_{\tilde p}$ | the left multiplication operator, $L_{\tilde p}\tilde x=\tilde p\times\tilde x$, whose kernel is the annihilator |
| $C_{\vec p}=[\vec p]_\times$ | the $3\times3$ skew matrix of the cross product $\vec x\mapsto\vec p\times\vec x$, so that the matrix of $L_{\tilde p}$ is $\operatorname{diag}(0,C_{\vec p})$ |
| $\chi_{L_{\tilde p}}(t)=t^{2}(t^{2}+|\vec p|^{2})$ | the characteristic polynomial of the operator |
| $\mathbb{R}e_0\oplus\mathbb{R}\vec p$ | the annihilator of a noncentral element $\tilde p$, a real plane of dimension two |
| $\mathbb{R}_{\mathbb{H}}=\mathbb{R}e_0$ | the centre, on which the operator vanishes and the annihilator is the whole space |
| $|\vec p|^{2}=\sum_k p_k^{2}$ | the vector form, positive definite over $\mathbb{R}$, whose only zero is the centre |

## Further Reading

- *Definitions for the Study of the 6 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-6-algebraic-structures.md`), §*The Element Vocabulary*, for the zero divisor, the radical and the regular element of a general product.
- *Introduction to the Antisymmetric Plain Algebra of Quaternions* (`articles_maths/introduction-to-the-antisymmetric-plain-algebra-of-quaternions.md`), for the operation, its alternation and its table.
- *Zero Divisors of the Antisymmetric Plain Algebra* (`articles_maths/zero-divisors-of-the-antisymmetric-plain-algebra-of-quaternions.md`), above this article in this category, the companion article, for the zero-divisor set, the criterion and the parallelism of the vector parts.
- *Annihilators in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/annihilators-in-the-6-algebraic-structures-over-the-quaternion-r-space.md`), for the structure-level annihilating set, the elements that kill the whole space for a fixed product.
- *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra* (`articles_maths/the-adjoint-operators-and-the-derivations-of-the-antisymmetric-plain-algebra-of-quaternions.md`), below this article in this category, for the operator's kernel and image and the derivations.
- *Introduction to the Remarkable Subspaces of the Quaternions* (`articles_maths/introduction-to-the-remarkable-subspaces-of-the-quaternions.md`), for the scalar line and the vector subspace.
- *Zero Divisors of the Antisymmetric Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-antisymmetric-quaternionic-algebra-of-quaternions.md`), the sibling alternating block, whose zero-divisor set is the same punctured space.
- *Annihilators of the Antisymmetric Plain Algebra* (`articles_maths/annihilators-of-the-antisymmetric-plain-algebra.md`), the biquaternion twin over $\mathbb{C}$, which reads the same plane, of complex dimension two.
