# __Annihilators of the Antisymmetric Quaternionic Algebra__

## Introduction

The zero divisor of a product is a property of one element alone: it says that *some* nonzero
partner exists that the element kills. The annihilator says *which* partners those are, and it is
the finer object. It is the set of elements killed by a fixed element,
$$
A_\star(\tilde p)=\{\tilde x:\tilde p\star\tilde x=0\},\qquad
B_\star(\tilde p)=\{\tilde x:\tilde x\star\tilde p=0\},
$$
the left and the right annihilator of the element in the product $\star$; the zero divisor and the
radical are *Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, §*The Element Vocabulary*.
When the product is carried by a multiplication operator the annihilator is the kernel of that
operator, so it is a linear subspace.

The block of this article is the **antisymmetric quaternionic multiplication**
$$
\tilde p\diamond\tilde q=\tfrac12\bigl(\tilde p^{\natural}\tilde q-\tilde q^{\natural}\tilde p\bigr)=p_0\vec q-q_0\vec p-\vec p\times\vec q,
$$
scalar part zero and vector part the mixed term with the cross term subtracted (*Introduction to
the Antisymmetric Quaternionic Algebra of Quaternions*). It is alternating, so every nonzero
element is a two-sided zero divisor with itself as partner and the zero-divisor set is the whole
punctured space (*Zero Divisors of the Antisymmetric Quaternionic Algebra*, above this article in
this category). The annihilator is where the block is not degenerate: it is the **real line**
$\mathbb{R}\tilde p$ for every nonzero element, of real dimension one, and the whole space at $0$.
The article owns that reading, the operator with its characteristic polynomial, and the shape of
the annihilator on the remarkable subspaces; the zero-divisor set and the comparison with the other
five structures are the cited article's.

The word *annihilator* is also used one level up, for the elements that kill the whole space at a
fixed product, which is the radical; that is the structure-level question of *Annihilators in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*
(`articles_maths/annihilators-in-the-algebraic-structures-over-the-quaternion-r-space.md`), not the annihilator of a fixed element read here.

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
$\tilde p\neq0$: the annihilator decides the zero-divisor property element by element.

Throughout this article the product is the **antisymmetric quaternionic multiplication**
$\diamond$, and unqualified, *annihilator* means the annihilator of $\diamond$. The left
multiplication is the operator
$$
L_{\tilde p}\tilde x=\tilde p\diamond\tilde x,
$$
so that $A_\diamond(\tilde p)=\ker L_{\tilde p}$. The block is the twin of the **antisymmetric
plain algebra**, whose annihilator of a noncentral element is the real plane
$\mathbb{R}e_0\oplus\mathbb{R}\vec p$ (*Annihilators of the Antisymmetric Plain Algebra*); the
two are the two antisymmetric blocks of the six, and this one fails the Jacobi identity where the
plain one holds it.

## The Two Annihilators Coincide

**Proposition (the two annihilators coincide).** For every $\tilde p$,
$$
B_\diamond(\tilde p)=A_\diamond(\tilde p)=\ker L_{\tilde p}.
$$

*Proof.* The block is alternating, $\tilde x\diamond\tilde p=-\tilde p\diamond\tilde x$, so
$\tilde x\diamond\tilde p=0$ exactly when $\tilde p\diamond\tilde x=0$; the two annihilators are
therefore one set, the kernel of $L_{\tilde p}$.

## The Annihilator of an Element

**Theorem (the annihilator is the line of the element).** For a nonzero element $\tilde p$,
$$
A_\diamond(\tilde p)=B_\diamond(\tilde p)=\mathbb{R}\tilde p,
$$
the **real line** of the element, of real dimension one; for $\tilde p=0$ both annihilators are the
whole space $\mathbb{H}$, of real dimension four.

*Proof.* The annihilator is the kernel of $L_{\tilde p}$. The line $\mathbb{R}\tilde p$ lies in it
by alternation, $\tilde p\diamond\tilde p=0$. Conversely, the criterion of *Zero Divisors of the
Antisymmetric Quaternionic Algebra*, §*The Criterion*, states that $\tilde p\diamond\tilde x=0$
with $\tilde p\neq0$ forces $\tilde x=\lambda\tilde p$: the perpendicular component of the partner
is killed by the quarter-turn comparison of the scalar and cross terms, and only the parallel
component survives. The kernel is therefore exactly the line. At $\tilde p=0$ the operator is zero
and the kernel is all of $\mathbb{H}$.

**Corollary (every element lies in its own annihilator).** For every $\tilde p$ the element itself
is annihilated, $\tilde p\in A_\diamond(\tilde p)$, by alternation; for a nonzero element the
annihilator is exactly the line that $\tilde p$ spans.

**Example.** At the scalar unit $e_0$ the operator is $L_{e_0}\tilde x=\vec x$, which vanishes
exactly on the centre $\mathbb{R}e_0$, of real dimension one. At a nonzero pure element $\vec p$
the annihilator is the line $\mathbb{R}\vec p$, inside the vector subspace. The real block has
no isotropic vector, so the line is the only value the annihilator takes away from the origin.

## The Multiplication Operator and the Rank

**Proposition (the operator and its characteristic polynomial).** In the basis $e_0,e_1,e_2,e_3$
the operator $L_{\tilde p}$ of an element $\tilde p=p_0e_0+\vec p$ has matrix
$$
\begin{pmatrix}
0 & 0 & 0 & 0 \\
-p_1 & p_0 & p_3 & -p_2 \\
-p_2 & -p_3 & p_0 & p_1 \\
-p_3 & p_2 & -p_1 & p_0
\end{pmatrix},
$$
its trace is $3p_0$, its determinant is $0$, and its characteristic polynomial is
$$
\chi_{L_{\tilde p}}(t)=t\,(t-p_0)\bigl((t-p_0)^{2}+|\vec p|^{2}\bigr),\qquad |\vec p|^{2}=p_1^{2}+p_2^{2}+p_3^{2}.
$$

*Proof.* The columns are the values $\tilde p\diamond e_\nu$: at $\nu=0$ the value $-\vec p$, at
$\nu=k$ the value $p_0e_k-\vec p\times e_k$. The lower three-by-three block is
$p_0\mathrm{I}_3-[\vec p]_\times$, whose eigenvalues are $p_0$ and $p_0\pm i|\vec p|$, of
characteristic polynomial $(t-p_0)\bigl((t-p_0)^{2}+|\vec p|^{2}\bigr)$; the first row is zero,
so the eigenvalue $0$ is added and the determinant, the constant term, vanishes. The trace $3p_0$
is the sum of the three diagonal entries $p_0$ of the lower block.

**Corollary (the rank and the annihilator).** The rank of $L_{\tilde p}$ and the annihilator are

| $\tilde p$ | $\operatorname{rank}L_{\tilde p}$ | $\dim\ker L_{\tilde p}$ | $\ker L_{\tilde p}$ |
|---|---|---|---|
| $\tilde p\neq0$ | $3$ | $1$ | $\mathbb{R}\tilde p$ |
| $0$ | $0$ | $4$ | $\mathbb{H}$ |

*Proof.* The lower block $p_0\mathrm{I}_3-[\vec p]_\times$ is invertible when $p_0\neq0$, its
eigenvalues being nonzero, so its three rows already give rank three and the whole matrix, whose
first row is zero, has rank exactly three; when $p_0=0$ and $\tilde p\neq0$ the lower block is
$-[\vec p]_\times$, of rank two and image the plane orthogonal to $\vec p$, and the first
column $-\vec p$ is independent of that image, giving rank three again. The rank is therefore
three for every nonzero element and zero at the origin, and the kernel is the line or the whole
space by the theorem above. The same invariants are computed in *The Adjoint Operators of the
Antisymmetric Quaternionic Algebra*, below this article in this category.

## The Dichotomy

The zero-divisor set of the block is the whole punctured space, so it separates nothing. The
annihilator separates the elements by the degenerate origin alone: off the origin the annihilator
is the line $\mathbb{R}\tilde p$, on it the whole space. There is no intermediate case, and the
reason is real: the cone of the parent quaternionic product is the locus
$p_0^{2}+|\vec p|^{2}=0$ of its central square, and the quaternion form is definite over
$\mathbb{R}$, so this cone is the origin alone; no nonzero element falls on it and the line never
widens.

**The real-versus-complex difference.** In the complex blocks the annihilator is larger. The
complex twin, the antisymmetric quaternionic algebra over $\mathbb{C}$, has the line
$\mathbb{C}\tilde p$ off the isotropic cone of the central square and the larger plane on it
(*Annihilators of the Antisymmetric Quaternionic Algebra*, the biquaternion article of the same
name); over $\mathbb{R}$ the cone degenerates to the origin and the annihilator is the line at
every nonzero element. The complex antisymmetric quaternionic sesqualgebra, whose product is the
single cross term, has for a noncentral element the plane
$\mathbb{C}e_0\oplus\mathbb{C}\overline{\vec Q}$, of dimension two over $\mathbb{C}$
(*Annihilators of the Antisymmetric Quaternionic Sesqualgebra*); the coupling of the scalar and the
vector parts, which the block here carries and the sesquilinear one does not, is what cuts the
annihilator down to the **real line** $\mathbb{R}\tilde p$.

**The real antisymmetric plain algebra.** The real twin, the antisymmetric plain algebra, has for a
noncentral element the two-dimensional **plane** $\mathbb{R}e_0\oplus\mathbb{R}\vec p$, because
its cross product ignores the scalar coordinate (*Annihilators of the Antisymmetric Plain
Algebra*); the coupling of the scalar and the vector parts in the block here is again what cuts the
annihilator down to the line.

## The Annihilator on the Remarkable Subspaces

The quaternion space has two remarkable real subspaces, the scalar line
$\mathbb{R}_{\mathbb{H}}=\mathbb{R}e_0$ and the vector subspace $\mathrm{Vect}(\mathbb{H})$
(*Introduction to the Remarkable Subspaces of the Quaternions*).

**The restriction is alternating.** On each subspace the block restricts to an alternating
operation, so every element of a subspace is annihilated by itself, $\tilde x\diamond\tilde x=0$,
and the annihilator of an element in the restriction is the ambient annihilator intersected with
the subspace.

*Proof.* The restriction of the block to a subspace is the block read on the elements of the
subspace, and $\tilde x\diamond\tilde x=0$ holds for every $\tilde x$ of the ambient space, hence
for every element of the subspace; the kernel of the restricted operator is the intersection of the
ambient kernel with the subspace.

**The centre.** A nonzero central element $\tilde p=\lambda e_0$ has
$L_{\lambda e_0}\tilde x=\lambda\vec x$, the scalar multiple of the projection onto the vector
subspace, so its annihilator is the centre $\mathbb{R}e_0$: the central elements annihilate the
centre alone.

**The vector subspace.** On the vector subspace, where $p_0=0$ and $\tilde x$ is pure, the
operation is the negative cross product $\tilde p\diamond\tilde x=-\vec p\times\vec x$. The
annihilator of a nonzero pure element meets the vector subspace in the line $\mathbb{R}\vec p$
and is that line in the ambient space; the plane $\mathbb{R}e_0\oplus\mathbb{R}\vec p$ of the
plain twin, which would add the centre, does not occur here.

## Summary

The annihilator of an element in a product is the set of partners the element kills, the left and
the right annihilator being the kernels of the left and the right multiplication. The antisymmetric
quaternionic multiplication is alternating, so the two annihilators of an element coincide and
contain the element itself. The operator $L_{\tilde p}$ has trace $3p_0$, determinant $0$ and
characteristic polynomial $t(t-p_0)\bigl((t-p_0)^{2}+|\vec p|^{2}\bigr)$: its rank is three for
every nonzero element and its kernel the real line $\mathbb{R}\tilde p$, of real dimension one,
while at the origin the operator is zero and the annihilator is the whole space, of real dimension
four. At $e_0$ the annihilator is the centre, and on the vector subspace it is the line of the
element inside the subspace. The zero-divisor set of the block is the whole punctured space and
gives none of this, and the annihilator reads the block's single exceptional element, the origin.
Over $\mathbb{C}$ the annihilator widens on the isotropic cone of the parent; over $\mathbb{R}$ the
form is definite, the cone degenerates to the origin, and the annihilator is the line at every
nonzero element.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde p\diamond\tilde q=\tfrac12(\tilde p^{\natural}\tilde q-\tilde q^{\natural}\tilde p)$ | the antisymmetric quaternionic multiplication, the operation $\mathrm{AQA}$ |
| $A_\diamond(\tilde p),B_\diamond(\tilde p)$ | the left and the right annihilator of $\tilde p$ in the block, equal because the block is alternating |
| $L_{\tilde p}$ | the left multiplication operator, $L_{\tilde p}\tilde x=\tilde p\diamond\tilde x$, whose kernel is the annihilator |
| $\chi_{L_{\tilde p}}(t)=t(t-p_0)\bigl((t-p_0)^{2}+|\vec p|^{2}\bigr)$ | the characteristic polynomial of the operator |
| $\mathbb{R}\tilde p$ | the annihilator of a nonzero element, a real line of real dimension one |
| $\mathbb{H}$ | the annihilator of $0$, the whole space of real dimension four |
| $\mathbb{R}_{\mathbb{H}}=\mathbb{R}e_0$ | the centre, the annihilator of the nonzero central elements |
| $|\vec p|^{2}=p_1^{2}+p_2^{2}+p_3^{2}$ | the vector form, positive definite over $\mathbb{R}$ |

## Further Reading

- *Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-quaternion-r-space.md`), §*The Element Vocabulary*, for the zero divisor and the radical of a general product.
- *Introduction to the Antisymmetric Quaternionic Algebra of Quaternions* (`articles_maths/introduction-to-the-antisymmetric-quaternionic-algebra-of-quaternions.md`), for the operation, its alternation and its table.
- *Zero Divisors of the Antisymmetric Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-antisymmetric-quaternionic-algebra-of-quaternions.md`), above this article in this category, for the punctured space, the criterion and the comparison with the other five structures.
- *The Adjoint Operators of the Antisymmetric Quaternionic Algebra* (`articles_maths/the-adjoint-operators-of-the-antisymmetric-quaternionic-algebra-of-quaternions.md`), below this article in this category, for the multiplication operator and its invariants.
- *Annihilators in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/annihilators-in-the-algebraic-structures-over-the-quaternion-r-space.md`), for the structure-level annihilating set, the elements that kill the whole space for a fixed product.
- *Introduction to the Remarkable Subspaces of the Quaternions* (`articles_maths/introduction-to-the-remarkable-subspaces-of-the-quaternions.md`), for the scalar line and the vector subspace on which the restriction is read.
- *Annihilators of the Antisymmetric Plain Algebra* (`articles_maths/annihilators-of-the-antisymmetric-plain-algebra-of-quaternions.md`), the real twin block, whose annihilator of a noncentral element is the plane $\mathbb{R}e_0\oplus\mathbb{R}\vec p$.
- *Annihilators of the Antisymmetric Quaternionic Sesqualgebra* (`articles_maths/annihilators-of-the-antisymmetric-quaternionic-sesqualgebra.md`), the complex sibling whose annihilator of a noncentral element is the plane $\mathbb{C}e_0\oplus\mathbb{C}\overline{\vec Q}$.
