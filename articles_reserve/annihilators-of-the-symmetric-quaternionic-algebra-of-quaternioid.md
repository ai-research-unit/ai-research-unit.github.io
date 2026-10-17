# __Annihilators of the Symmetric Quaternionic Algebra__

## Introduction

The zero divisor of a product is a property of one element alone: it says that *some* nonzero
partner exists that the element kills. The annihilator says *which* partners those are, and it is
the finer object. It is the set of elements killed by a fixed element,
$$
A_\star(\tilde p)=\{\tilde x:\tilde p\star\tilde x=0\},\qquad
B_\star(\tilde p)=\{\tilde x:\tilde x\star\tilde p=0\},
$$
the left and the right annihilator (*Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*,
§*The Element Vocabulary*). When the product is carried by a multiplication operator the
annihilator is the kernel of that operator, so it is a linear subspace and its computation is one
of linear algebra.

The block of this article is the **symmetric quaternionic multiplication**
$$
\tilde p\star\tilde q=\tfrac12\bigl(\tilde p^{\natural}\tilde q+\tilde q^{\natural}\tilde p\bigr)
=N(\tilde p,\tilde q)\,e_t,\qquad N(\tilde p,\tilde q)=p_0q_t+(\vec p,\vec q),
$$
the quaternion form read as a product (*Introduction to the Symmetric Quaternionic Algebra of
Quaternions*). It is commutative and central valued, so the two annihilators of an element are one
set. The block is the extreme of the six for the annihilator: the set of zero divisors is the whole
punctured space, and yet the annihilator of every nonzero element is a **hyperplane**, the largest
a nonzero annihilator can be. The article owns that reading, the operator with its rank, and the
shape of the annihilator on the remarkable subspaces; the zero-divisor set is the cited article's.

A second article, *Annihilators in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*, asks a different question: it fixes the product and collects the
elements that kill the whole space, the radical of the product, whereas this article fixes the
element and collects the partners it kills.

## The Annihilator of a Product

**Definition (annihilator).** Let $\star$ be a product on $\mathbb{H}$ and let
$\tilde p\in\mathbb{H}$. The **left annihilator** and the **right annihilator** of $\tilde p$ in
$\star$ are
$$
A_\star(\tilde p)=\{\tilde x:\tilde p\star\tilde x=0\},\qquad
B_\star(\tilde p)=\{\tilde x:\tilde x\star\tilde p=0\}.
$$
They are the kernels of the left and the right multiplication, and they are nonzero exactly when
$\tilde p$ is a zero divisor of the corresponding side.

Throughout this article the product is the **symmetric quaternionic multiplication** $\star$, and
unqualified, *annihilator* means the annihilator of $\star$. The left and the right multiplication
are one operator,
$$
L_{\tilde p}\tilde x=\tilde p\star\tilde x=N(\tilde p,\tilde x)e_t,\qquad
R_{\tilde p}=L_{\tilde p},
$$
because the block is commutative.

## The Two Annihilators Coincide

**Proposition (the two annihilators coincide).** For every $\tilde p$,
$$
B_\star(\tilde p)=A_\star(\tilde p)=\ker L_{\tilde p}.
$$

*Proof.* The block is commutative, $\tilde x\star\tilde p=\tilde p\star\tilde x$, so the two
products vanish together; the two annihilators are therefore one set, and it is the kernel of the
one operator of the block.

## The Annihilator of an Element

**Theorem (the annihilator is the orthogonal hyperplane).** For $\tilde p\neq0$,
$$
A_\star(\tilde p)=B_\star(\tilde p)=\{\tilde x:N(\tilde p,\tilde x)=0\}=\tilde p^{\perp},
$$
the orthogonal of $\tilde p$ for the form $N$, a **real hyperplane of dimension three**. For
$\tilde p=0$ both annihilators are all of $\mathbb{H}$. The annihilator of the product,
$$
\{\tilde q:\tilde q\star\tilde x=0\ \text{for every }\tilde x\}=\{0\},
$$
is zero.

*Proof.* The annihilator is the kernel of the nonzero functional
$\tilde x\mapsto N(\tilde p,\tilde x)$, a hyperplane of dimension $4-1=3$. The annihilator of the
product is the radical of the form, which is $\{0\}$ because the form is non-degenerate (*The
Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*).

**Corollary (the element is never in its own annihilator).** For $\tilde p\neq0$ the element does
not belong to its annihilator, because
$N(\tilde p,\tilde p)=N(\tilde p)=p_0^{2}+|\vec p|^{2}>0$. Only $0$ lies in its own annihilator,
and there the annihilator is the whole space.

## The Multiplication Operator and the Rank

**Proposition (the operator).** In the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ the operator $L_{\tilde p}$ of an
element $\tilde p=p_0e_t+\vec p$ has matrix
$$
\begin{pmatrix}
p_0 & p_1 & p_2 & p_3 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{pmatrix},
$$
its trace is $p_0$, its determinant is $0$, and its image is the central line $\mathbb{R}e_t$ for
every $\tilde p\neq0$.

*Proof.* The value $\tilde p\star\tilde x$ is the scalar $N(\tilde p,\tilde x)$ times $e_t$, so the
matrix has the single nonzero row $(p_0,p_1,p_2,p_3)$; the trace is $p_0$ and the determinant is
$0$ because the last three rows vanish. The row is nonzero exactly when $\tilde p\neq0$.

**Corollary (the rank and the annihilator).** For $\tilde p\neq0$ the operator has rank one, image
the central line $\mathbb{R}e_t$ and kernel the hyperplane $\tilde p^{\perp}$; at $\tilde p=0$ the
operator is zero, of rank zero, and its kernel is the whole space.

## The Dichotomy

The zero-divisor set of the block is the whole punctured space, so it separates nothing. The
annihilator separates everything: it is the orthogonal hyperplane $\tilde p^{\perp}$, and it
depends on the element through the form $N$ alone. The block is the exact opposite of the general
plain algebra, whose annihilator is zero off the zero-divisor cone and a plane on it: here the
annihilator is never zero for a nonzero element and never a plane, and the invariant that the
general products read on the cone is read here on the isotropic locus.

Over $\mathbb{C}$ that locus is a nontrivial cone: the isotropic elements satisfy
$N(\tilde p,\tilde p)=0$, they lie in their own annihilator, and they are exactly the nilpotents of
index two. Over $\mathbb{R}$ the form is positive definite, so
$N(\tilde p,\tilde p)=N(\tilde p)=p_0^{2}+|\vec p|^{2}>0$ for every nonzero element and the
isotropic set is the single point $0$: **no nonzero element is in its own annihilator**. The
hyperplane shape is the same in the two blocks; the definiteness is what removes the
self-annihilating elements, and it is the only difference. The reason the annihilator is never zero
is that the form is non-degenerate, so the orthogonal of a nonzero element is a hyperplane; the
reason it is never the whole space is that the functional $N(\tilde p,\cdot)$ is nonzero; and the
annihilator of the product, the radical of the form, is zero for the same non-degeneracy.

## The Annihilator on the Remarkable Subspaces

The quaternion algebra has two remarkable real subspaces, the scalar line and the vector space
(*Introduction to the Remarkable Subspaces of the Quaternions*), and the annihilator is read on
each.

**The centre.** A nonzero central element $\tilde p=\lambda e_t$ has
$N(\lambda e_t,\tilde x)=\lambda x_0$, so its annihilator is $\{x_0=0\}$, the vector subspace. The
centre is therefore the subspace whose nonzero elements annihilate exactly the vector subspace.

**The vector subspace.** A nonzero pure element $\tilde p=\vec p$ has
$N(\vec p,\tilde x)=(\vec p,\vec x)$, so its annihilator is the hyperplane
$\{\tilde x:(\vec p,\vec x)=0\}$. It contains the centre and, inside the vector subspace, the
real plane orthogonal to $\vec p$; the element $\vec p$ never lies in the annihilator,
because $(\vec p,\vec p)>0$ for $\vec p\neq0$. On the vector subspace the annihilator
meets the subspace in a plane, of dimension two, and the missing dimension is the scalar one.

## Summary

The annihilator of an element in a product is the set of partners the element kills, the left and
the right annihilator being the kernels of the left and the right multiplication. The symmetric
quaternionic multiplication is commutative and central valued,
$\tilde p\star\tilde q=N(\tilde p,\tilde q)e_t$ with
$N(\tilde p,\tilde q)=p_0q_t+(\vec p,\vec q)$, so the two annihilators of an element
coincide. Every nonzero element is a zero divisor and every nonzero element has the **hyperplane**
$\tilde p^{\perp}$ as annihilator, of real dimension three; the operator $L_{\tilde p}$ has rank
one, image the centre $\mathbb{R}e_t$, trace $p_0$ and determinant $0$; and the annihilator of the
product is $\{0\}$ because the form is non-degenerate. No nonzero element lies in its own
annihilator, because the form is positive definite: this is where the block differs from its
complex twin, whose isotropic cone is nontrivial and whose isotropic elements annihilate
themselves.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde p\star\tilde q=N(\tilde p,\tilde q)e_t$ | the symmetric quaternionic multiplication, the operation $\mathrm{SQA}$ |
| $N(\tilde p,\tilde q)=p_0q_t+(\vec p,\vec q)$ | the quaternion form, the scalar part of the block, positive definite |
| $A_\star(\tilde p),B_\star(\tilde p)$ | the left and the right annihilator of $\tilde p$ in the block, equal because the block is commutative |
| $L_{\tilde p}$ | the left multiplication operator, $L_{\tilde p}\tilde x=N(\tilde p,\tilde x)e_t$, of rank one for $\tilde p\neq0$ |
| $\tilde p^{\perp}=\{\tilde x:N(\tilde p,\tilde x)=0\}$ | the annihilator of a nonzero element, a real hyperplane of dimension three |
| $N(\tilde p)=p_0^{2}+|\vec p|^{2}=N(\tilde p,\tilde p)>0$ | the definite norm, never zero at a nonzero element |

## Further Reading

- *Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-quaternioid-r-space.md`), §*The Element Vocabulary*, for the zero divisor, the radical and the regular element of a general product.
- *Introduction to the Symmetric Quaternionic Algebra* (`articles_maths/introduction-to-the-symmetric-quaternionic-algebra-of-quaternioid.md`), for the product, its commutativity and its table.
- *Zero Divisors of the Symmetric Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-symmetric-quaternionic-algebra-of-quaternioid.md`), above this article in this category, for the criterion that makes the whole punctured space the zero-divisor set.
- *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra* (`articles_maths/the-radical-and-the-isotropic-elements-of-the-symmetric-quaternionic-algebra-of-quaternioid.md`), for the non-degeneracy of the form and the trivial isotropic set.
- *The Multiplication Operators of the Symmetric Quaternionic Algebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-quaternionic-algebra-of-quaternioid.md`), for the operator, its rank and its composition law.
- *The Quaternioid Form as a Product on the Symmetric Quaternionic Algebra* (`articles_maths/the-quaternioid-form-as-a-product-on-the-symmetric-quaternionic-algebra-of-quaternioid.md`), for the form, its Gram matrix and its positive definiteness.
- *Introduction to the Remarkable Subspaces of the Quaternions* (`articles_maths/introduction-to-the-remarkable-subspaces-of-the-quaternions.md`), for the scalar line and the vector subspace on which the annihilator is read.
- *Annihilators in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/annihilators-in-the-algebraic-structures-over-the-quaternioid-r-space.md`), for the structure-level annihilating set of an element that kills the whole space for a fixed product, which is the radical and not the annihilator of a fixed element.
- *Annihilators of the Symmetric Quaternionic Algebra* (`articles_maths/annihilators-of-the-symmetric-quaternionic-algebra.md`), the biquaternion twin, whose isotropic cone is nontrivial and whose isotropic elements lie in their own annihilator.
