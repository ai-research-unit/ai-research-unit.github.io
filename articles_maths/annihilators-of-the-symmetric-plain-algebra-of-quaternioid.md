# __Annihilators of the Symmetric Plain Algebra__

## Introduction

The zero divisor of a product is a property of one element alone: it says that *some* nonzero
partner exists that the element kills. The annihilator says *which* partners those are, and it is
the finer object. It is the set of elements killed by a fixed element,
$$
A_\star(\tilde p)=\{\tilde q:\tilde p\star\tilde q=0\},\qquad
B_\star(\tilde p)=\{\tilde q:\tilde q\star\tilde p=0\},
$$
the left and the right annihilator. When the product is carried by a multiplication operator the
annihilator is the kernel of that operator, so it is a linear subspace.

The block of this article is the **symmetric plain multiplication**
$$
\tilde p\bullet\tilde q=\tfrac12\bigl(\tilde p\tilde q+\tilde q\tilde p\bigr)
=(p_0q_0-\vec p\cdot\vec q)e_0+p_0\vec q+q_0\vec p,
$$
the Jordan product (*Introduction to the Symmetric Plain Algebra of Quaternions*). It is
commutative, so the left and the right multiplication by an element are one operator and the two
annihilators of the element are one set. The zero-divisor set of the block is the vector subspace
with the origin removed, the single pure family of the criterion (*Zero Divisors of the Symmetric
Plain Algebra*, above this article in this category). The annihilator reads that family: a nonzero
pure element annihilates a real plane, a nonzero non-pure element annihilates nothing, and the
origin alone annihilates the whole space. The article owns that reading, the operator with its rank
and its determinant, and the shape of the annihilator on the remarkable subspaces; the zero-divisor
set and its criterion are the cited article's.

**The distinction from the structure-level article.** The chapter also carries *Annihilators in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*
(*Comparison of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*), where the
object is the set of elements that kill the whole space for a fixed product, that is the radical;
the present article instead fixes the element and reads the set it kills, which is the finer
question and the one the zero divisors ask.

## The Annihilator of a Product

**Definition (annihilator).** Let $\star$ be a product on $\mathbb{H}$ and let
$\tilde q\in\mathbb{H}$. The **left annihilator** and the **right annihilator** of $\tilde q$ in
$\star$ are
$$
A_\star(\tilde q)=\{\tilde x:\tilde q\star\tilde x=0\},\qquad
B_\star(\tilde q)=\{\tilde x:\tilde x\star\tilde q=0\}.
$$
They are the kernels of the left and the right multiplication, and they are nonzero exactly when
$\tilde q$ is a zero divisor of the corresponding side.

Throughout this article the product is the **symmetric plain multiplication** $\bullet$, and
unqualified, *annihilator* means the annihilator of $\bullet$. The left and the right
multiplication of the block are the operator
$$
L^{\bullet}_{\tilde p}\tilde q=\tilde p\bullet\tilde q,\qquad
R^{\bullet}_{\tilde p}\tilde q=\tilde q\bullet\tilde p,
$$
and the block is the operation $\mathrm{SPA}$ of *The Algebraic Structures over the Quaternion
$\mathbb{R}$ Space*. It is the symmetric half of the plain product,
$\mathrm{GPA}=\mathrm{SPA}+\mathrm{APA}$, and the plain product is a division algebra, where no
nonzero element annihilates anything; the block is where that changes.

**Remark (only the annihilator, not the ideal).** The annihilator of a zero divisor is a subspace,
not a two-sided ideal: the plane of a pure element does not contain $e_0$, and it is not carried
into itself by the product with an arbitrary element. It is the vanishing of the operator, not an
algebraic ideal, that the block carries, and the block has no proper ideal because the ambient
algebra is simple.

## The Two Annihilators Coincide

**Proposition (the two annihilators coincide).** For every $\tilde p$,
$$
B_\bullet(\tilde p)=A_\bullet(\tilde p)=\ker L^{\bullet}_{\tilde p}.
$$

*Proof.* The block is commutative, $\tilde q\bullet\tilde p=\tilde p\bullet\tilde q$, so
$\tilde q\bullet\tilde p=0$ exactly when $\tilde p\bullet\tilde q=0$; the two annihilators are
therefore one set, and it is the kernel of the one operator of the block,
$L^{\bullet}_{\tilde p}=R^{\bullet}_{\tilde p}$ (*The Multiplication Operators of the Symmetric
Plain Algebra*, below this article in this category).

## The Annihilator of an Element

The criterion of the block is the single clause $p_0=0$: a nonzero element is a zero divisor
exactly when it is pure, equivalently when its annihilator is nonzero (*Zero Divisors of the
Symmetric Plain Algebra*, §*The Criterion*). The annihilator of a pure element is the following.

**Theorem (the annihilator of a pure element).** For a nonzero pure element $\tilde p=\vec p$,
$$
A_\bullet(\vec p)=B_\bullet(\vec p)
=\{\tilde q=q_0e_0+\vec q:\ q_0=0,\ \vec p\cdot\vec q=0\},
$$
the plane of the vector subspace orthogonal to $\vec p$, of real dimension two.

*Proof.* For a pure element, $\vec p\bullet\tilde q=-(\vec p\cdot\vec q)e_0+q_0\vec p$,
which vanishes exactly when $q_0=0$ and $\vec p\cdot\vec q=0$. In the three-dimensional
vector subspace the single equation $\vec p\cdot\vec q=0$ has a solution space of real
dimension two.

**Remark (the element is not its own partner).** The square of a pure element is
$\vec p\bullet\vec p=-|\vec p|^2e_0$, which is nonzero for $\vec p\neq0$. The element
is therefore not orthogonal to itself, and a nonzero pure element does not lie in its own
annihilator; the line $\mathbb{R}\vec p$ meets the plane only at the origin.

**Corollary (the annihilator vanishes off the pure elements).** For a nonzero element that is not
pure the annihilator is $\{0\}$: the element is regular, and indeed a unit.

*Proof.* A nonzero element with $p_0\neq0$ has no nonzero partner, by the criterion of the cited
article; equivalently its multiplication operator has determinant $p_0^2N(\tilde p)\neq0$, as the
next section computes.

## The Multiplication Operator and the Rank

**Proposition (the operator and its invariants).** In the basis $e_0,e_1,e_2,e_3$ the operator
$L^{\bullet}_{\tilde p}$ of an element $\tilde p=p_0e_0+\vec p$ has matrix
$$
\begin{pmatrix}
p_0 & -p_1 & -p_2 & -p_3 \\
p_1 & p_0 & 0 & 0 \\
p_2 & 0 & p_0 & 0 \\
p_3 & 0 & 0 & p_0
\end{pmatrix},
$$
its trace is $4p_0$ and its determinant is
$$
\det L^{\bullet}_{\tilde p}=p_0^2\bigl(p_0^2+|\vec p|^2\bigr)=p_0^2N(\tilde p).
$$

*Proof.* The columns are the values $\tilde p\bullet e_j$; the first is $(p_0,p_1,p_2,p_3)$, and
the others are $(-p_1,p_0,0,0)$, $(-p_2,0,p_0,0)$ and $(-p_3,0,0,p_0)$. The trace is the sum of the
diagonal entries, $4p_0$. For $p_0\neq0$ the determinant is the product of the three eigenvalues
$p_0$ of the vector block with the Schur complement $p_0+|\vec p|^2/p_0$, namely
$p_0^3(p_0+|\vec p|^2/p_0)=p_0^2(p_0^2+|\vec p|^2)$; the identity is polynomial in the
coordinates, so it holds at $p_0=0$ as well.

**Corollary (the rank and the annihilator).** The rank of $L^{\bullet}_{\tilde p}$ and the
annihilator of $\tilde p$ are

| $\tilde p$ | $\operatorname{rank}L^{\bullet}_{\tilde p}$ | $\dim\ker L^{\bullet}_{\tilde p}$ | $\ker L^{\bullet}_{\tilde p}$ |
|---|---|---|---|
| $0$ | $0$ | $4$ | $\mathbb{H}$ |
| $\tilde p\neq0$, $p_0=0$ | $2$ | $2$ | $\{\tilde q:q_0=0,\ \vec p\cdot\vec q=0\}$ |
| $p_0\neq0$ | $4$ | $0$ | $\{0\}$ |

*Proof.* A nonzero pure element has $p_0=0$: its first column is $\vec p$ and the other three
columns are the multiples $-p_ke_0$ of the scalar direction, so the columns span
$\mathbb{R}e_0\oplus\mathbb{R}\vec p$, of dimension two, and the rank is two. The kernel is the
plane of the pure elements orthogonal to $\vec p$, of real dimension two. A non-pure element has
$p_0\neq0$: the determinant $p_0^2N(\tilde p)$ is nonzero because the norm
$N(\tilde p)=p_0^2+|\vec p|^2$ is positive definite, so the rank is four and the kernel is
$\{0\}$. At the origin the matrix is zero, of rank zero and kernel the whole space.

## The Dichotomy

The zero-divisor set of the block has one criterion and one family, and the annihilator splits the
space by it: a nonzero pure element annihilates a real plane, every other nonzero element
annihilates nothing, and the origin alone annihilates the whole space. The dimension of the
annihilator reads the pure family where the criterion already does, and the operator reads it
again: the plane is the kernel of a rank-two operator, and a unit has the empty kernel of a
rank-four operator.

**The key difference from the complex block.** In the complex symmetric plain algebra the
annihilator had a second value: the scalar family $\{Q_0\neq0,\ C(\tilde Q)=0\}$ annihilated a
complex line. Over $\mathbb{R}$ that family is empty, because the central square
$C(\tilde p)=p_0^2+|\vec p|^2$ vanishes only at $\tilde p=0$. The complex line therefore does
not occur, and over $\mathbb{R}$ the annihilator of an element is either $\{0\}$ or a real plane,
the whole space occurring only at the origin. The definiteness of the norm, which collapses the
criterion to the single clause $p_0=0$, collapses the annihilator to the plane as well.

## The Annihilator on the Remarkable Subspaces

Over $\mathbb{R}$ the remarkable subspaces are the scalar line, which is the centre, and the vector
subspace (*Introduction to the Remarkable Subspaces of the Quaternions*).

**The centre.** A nonzero central element $\tilde p=\lambda e_0$ is not pure, so its annihilator is
$\{0\}$: the centre annihilates nothing, and the unit $e_0$ in particular kills no partner.

**The vector subspace.** A nonzero pure element $\tilde p=\vec p$ has the plane annihilator of
§*The Annihilator of an Element*, and that plane already lies inside the vector subspace: the
product $\vec p\bullet\tilde q=-(\vec p\cdot\vec q)e_0+q_0\vec p$ vanishes exactly on
the pure elements orthogonal to $\vec p$, so the annihilator is the two-plane
$\vec p^{\perp}\cap\mathrm{Vect}(\mathbb{H})$ and it does not leave the subspace. The element
itself is not in it, the line $\mathbb{R}\vec p$ being the orthogonal complement of that plane
in the subspace.

## Summary

The annihilator of an element in a product is the set of partners the element kills, the left and
the right annihilator being the kernels of the left and the right multiplication. The symmetric
plain multiplication is commutative, so the two annihilators of an element coincide and are the
kernel of the one operator
$\tilde p\bullet\tilde q=(p_0q_0-\vec p\cdot\vec q)e_0+p_0\vec q+q_0\vec p$, of trace
$4p_0$ and determinant $p_0^2N(\tilde p)$. A nonzero pure element annihilates the real plane
$\{\tilde q:q_0=0,\ \vec p\cdot\vec q=0\}$ inside the vector subspace, a nonzero non-pure
element annihilates nothing, and the origin annihilates the whole space. Over $\mathbb{R}$ the
second family of the complex block is empty: the annihilator of an element is either $\{0\}$ or a
real plane, and no annihilator is a line. On the remarkable subspaces the centre annihilates
nothing and the annihilator of a pure element is the orthogonal plane inside the vector subspace,
which does not contain the element.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde p\bullet\tilde q=\tfrac12(\tilde p\tilde q+\tilde q\tilde p)$ | the symmetric plain multiplication, the operation $\mathrm{SPA}$ |
| $A_\bullet(\tilde p),B_\bullet(\tilde p)$ | the left and the right annihilator of $\tilde p$ in the block, equal because the block is commutative |
| $L^{\bullet}_{\tilde p}$ | the left multiplication operator, $L^{\bullet}_{\tilde p}\tilde q=\tilde p\bullet\tilde q$, whose kernel is the annihilator |
| $\operatorname{tr}L^{\bullet}_{\tilde p}=4p_0$, $\det L^{\bullet}_{\tilde p}=p_0^2N(\tilde p)$ | the trace and the determinant of the operator |
| $\{\tilde q:q_0=0,\ \vec p\cdot\vec q=0\}$ | the annihilator of a nonzero pure element, a real plane |
| $\mathbb{H}$ | the annihilator of the origin |
| $N(\tilde p)=p_0^2+\lvert\vec p\rvert^2$ | the norm, the central square, positive definite over $\mathbb{R}$ |

## Further Reading

- *Introduction to the Symmetric Plain Algebra of Quaternions* (`articles_maths/introduction-to-the-symmetric-plain-algebra-of-quaternioid.md`), for the Jordan product, its commutativity and its unit.
- *Zero Divisors of the Symmetric Plain Algebra* (`articles_maths/zero-divisors-of-the-symmetric-plain-algebra-of-quaternioid.md`), above this article in this category, for the criterion $p_0=0$, the zero-divisor set and the partner plane.
- *The Multiplication Operators of the Symmetric Plain Algebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-plain-algebra-of-quaternioid.md`), below this article in this category, for the operator, its composition, its kernel and its determinant.
- *Norm and Invertibility in the Symmetric Plain Algebra* (`articles_maths/norm-and-invertibility-in-the-symmetric-plain-algebra-of-quaternioid.md`), for the invertibility criterion and the Jordan inverse of the regular elements.
- *Annihilators in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/annihilators-in-the-algebraic-structures-over-the-quaternioid-r-space.md`), the structure-level article, for the annihilating set of a product, which is the radical and not the annihilator of a fixed element.
- *Introduction to the Remarkable Subspaces of the Quaternions* (`articles_maths/introduction-to-the-remarkable-subspaces-of-the-quaternions.md`), for the scalar line, the vector subspace and the orthogonality.
