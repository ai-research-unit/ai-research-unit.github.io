# __Annihilators of the Symmetric Quaternionic Algebra__

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

The block of this article is the **symmetric quaternionic multiplication**
$$
\tilde P\star\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P\bigr)
=N(\tilde P,\tilde Q)\,e_0,\qquad N(\tilde P,\tilde Q)=P_0Q_0+(\vec P,\vec Q),
$$
the quaternion form read as a product (*Introduction to the Symmetric Quaternionic Algebra of
Biquaternions*). It is commutative and central valued, so the two annihilators of an element are
one set. The block is the extreme of the twelve for the annihilator: the set of zero divisors is
the whole punctured space, and yet the annihilator of every nonzero element is a **hyperplane**,
the largest a nonzero annihilator can be. The article owns that reading, the operator with its
rank, and the shape of the annihilator on the remarkable subspaces; the zero-divisor set is the
cited article's.

**The results.** In the symmetric quaternionic block the two annihilators of an element coincide, because the product is commutative, and both are the kernel of the multiplication operator $L_{\tilde P}$. For $\tilde P\neq0$ the annihilator is the orthogonal hyperplane $\tilde P^{\perp}=\{\tilde X:N(\tilde P,\tilde X)=0\}$, of complex dimension three and real dimension six, while the annihilator of the product is $\{0\}$ because the form is non-degenerate. The element lies in its own annihilator exactly when it is isotropic, $N(\tilde P)=0$. The operator $L_{\tilde P}$ has matrix with the single nonzero row $(P_0,P_1,P_2,P_3)$, trace $P_0$, determinant $0$ and rank one for $\tilde P\neq0$.

## The Annihilator of a Product

**The annihilator of an element is the set of partners that it kills; the left annihilator is the kernel of the left multiplication and the right annihilator is the kernel of the right multiplication, and in the block the two coincide because the product is commutative.**

**Definition (annihilator).** Let $\star$ be a product on $\mathbb{B}$ and let
$\tilde Q\in\mathbb{B}$. The **left annihilator** and the **right annihilator** of $\tilde Q$ in
$\star$ are
$$
A_\star(\tilde Q)=\{\tilde X:\tilde Q\star\tilde X=0\},\qquad
B_\star(\tilde Q)=\{\tilde X:\tilde X\star\tilde Q=0\}.
$$
They are the kernels of the left and the right multiplication, and they are nonzero exactly when
$\tilde Q$ is a zero divisor of the corresponding side.

Throughout this article the product is the **symmetric quaternionic multiplication** $\star$, and
unqualified, *annihilator* means the annihilator of $\star$. The left and the right multiplication
are the operator
$$
L_{\tilde P}\tilde X=\tilde P\star\tilde X=N(\tilde P,\tilde X)e_0,\qquad
R_{\tilde P}=L_{\tilde P},
$$
and the block is its own twin, the **general quaternionic bilinear product**, whose annihilators
are *Annihilators of the General Quaternionic Algebra*.

## The Two Annihilators Coincide

**The two annihilators of an element coincide, $B_\star(\tilde P)=A_\star(\tilde P)=\ker L_{\tilde P}$, because the block is commutative.**

**Proposition (the two annihilators coincide).** For every $\tilde P$,
$$
B_\star(\tilde P)=A_\star(\tilde P)=\ker L_{\tilde P}.
$$

*Proof.* The block is commutative, $\tilde X\star\tilde P=\tilde P\star\tilde X$, so the two
products vanish together; the two annihilators are therefore one set, and it is the kernel of the
one operator of the block.

## The Multiplication Operator and the Rank

**The operator $L_{\tilde P}$ has matrix with the single nonzero row $(P_0,P_1,P_2,P_3)$ in the basis $e_0,e_1,e_2,e_3$, trace $P_0$ and determinant $0$; it has rank one and a hyperplane kernel for $\tilde P\neq0$, and it is the zero operator with kernel all of $\mathbb{B}$ at $\tilde P=0$.**

**Proposition (the operator).** In the basis $e_0,e_1,e_2,e_3$ the operator $L_{\tilde P}$ of an
element $\tilde P=P_0e_0+\vec P$ has matrix
$$
\begin{pmatrix}
P_0 & P_1 & P_2 & P_3 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{pmatrix},
$$
its trace is $P_0$, its determinant is $0$, and its image is the central line $\mathbb{C}e_0$ for
every $\tilde P\neq0$.

*Proof.* The value $\tilde P\star\tilde X$ is the scalar $N(\tilde P,\tilde X)$ times $e_0$, so the
matrix has the single nonzero row $(P_0,P_1,P_2,P_3)$; the trace is $P_0$ and the determinant is
$0$ because the last three rows vanish. The row is nonzero exactly when $\tilde P\neq0$.

**Corollary (the rank and the annihilator).** For $\tilde P\neq0$ the operator has rank one and its
kernel is a hyperplane; at $\tilde P=0$ the operator is zero and the kernel is the whole space.

## The Annihilator of an Element

**For $\tilde P\neq0$ the annihilator is the orthogonal hyperplane $\tilde P^{\perp}=\{\tilde X:N(\tilde P,\tilde X)=0\}$, of complex dimension three and real dimension six, the element lies in it exactly when it is isotropic, and the annihilator of the product is $\{0\}$ because the form is non-degenerate.**

**Theorem (the annihilator is the orthogonal hyperplane).** For $\tilde P\neq0$,
$$
A_\star(\tilde P)=B_\star(\tilde P)=\{\tilde X:N(\tilde P,\tilde X)=0\}=\tilde P^{\perp},
$$
the orthogonal of $\tilde P$ for the form $N$, a complex subspace of dimension three and real
dimension six. For $\tilde P=0$ both annihilators are all of $\mathbb{B}$. The annihilator of the
product,
$$
\{\tilde Q:\tilde Q\star\tilde X=0\ \text{for every }\tilde X\}=\{0\},
$$
is zero.

*Proof.* The annihilator is the kernel of the nonzero functional
$\tilde X\mapsto N(\tilde P,\tilde X)$, a hyperplane. The element lies in the hyperplane exactly
when $N(\tilde P)=N(\tilde P,\tilde P)=0$. The annihilator of the product is the radical of the
form, which is $\{0\}$ because the form is non-degenerate (*The Radical and the Isotropic Elements
of the Symmetric Quaternionic Algebra*).

**Corollary (the element is in its own annihilator exactly on the isotropic locus).** For
$\tilde P\neq0$ the element belongs to its annihilator exactly when $N(\tilde P)=0$,
that is exactly when it is isotropic; and that is exactly when it is a nilpotent of index two
(*Nilpotents of the Symmetric Quaternionic Algebra*).

## The Dichotomy

**The annihilator separates everything: it is never zero for a nonzero element and never a plane, it depends on the element through the form $N$ alone, and the element lies in its own annihilator exactly on the isotropic locus, the exact opposite of the general plain algebra, whose annihilator is a plane on the zero-divisor cone and zero off it.**

The zero-divisor set of the block is the whole punctured space, so it separates nothing. The
annihilator separates everything: it is the orthogonal hyperplane $\tilde P^{\perp}$, and it
depends on the element through the form $N$ alone. The block is the exact opposite of the general
plain algebra, whose annihilator is zero off the zero-divisor cone and a plane on it: here the
annihilator is never zero for a nonzero element and never a plane, and the invariant that the
general products read on the cone is read here on the isotropic locus, where the element lies in
its own annihilator. The reason is that the form is non-degenerate while the product is not unital,
so the orthogonal of a nonzero element is a hyperplane and the radical of the form, which is the
annihilator of the product, is zero.

## The Annihilator on the Remarkable Subspaces

**On the centre a nonzero element has the vector subspace as its annihilator, on the vector subspace a nonzero element has the hyperplane $\{\tilde X:(\vec P,\vec X)=0\}$ as its annihilator, and on the Hermitian subspace the annihilator of a nonzero element meets the subspace in a hyperplane of it.**

**The centre.** A nonzero central element $\tilde P=\lambda e_0$ has
$N(\lambda e_0,\tilde X)=\lambda X_0$, so its annihilator is $\{X_0=0\}$, the vector subspace. The
centre is therefore the subspace whose nonzero elements annihilate exactly the vector subspace.

**The vector subspace.** A nonzero pure element $\tilde P=\vec P$ has
$N(\vec P,\tilde X)=(\vec P,\vec X)$, so its annihilator is the hyperplane
$\{\tilde X:(\vec P,\vec X)=0\}$. It contains the centre and, inside the vector subspace, the
complex line through $\vec P$ and the orthogonal plane of the vector form; the element
$\vec P$ lies in the annihilator exactly when it is isotropic.

**The Hermitian and anti-Hermitian subspaces.** On the Hermitian subspace the form $N$ is Hermitian
and its restriction is non-degenerate; the annihilator of a nonzero Hermitian element meets the
subspace in a hyperplane of it, and the real directions among them are self-orthogonal when their
real square is zero.

## Summary

The annihilator of an element in a product is the set of partners the element kills, the left and
the right annihilator being the kernels of the left and the right multiplication. The symmetric
quaternionic multiplication is commutative and central valued,
$\tilde P\star\tilde Q=N(\tilde P,\tilde Q)e_0$ with
$N(\tilde P,\tilde Q)=P_0Q_0+(\vec P,\vec Q)$, so the two annihilators of an element
coincide. Every nonzero element is a zero divisor and every nonzero element has the **hyperplane**
$\tilde P^{\perp}$ as annihilator, of complex dimension three; the element lies in its own
annihilator exactly when it is isotropic, and the annihilator of the product is $\{0\}$ because the
form is non-degenerate. The block reads on the isotropic locus what the general plain algebra reads
on the zero-divisor cone: the two are the two ends of the same dimension count, and the annihilator
is the hyperplane in the one and the plane or the line in the other.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q=N(\tilde P,\tilde Q)e_0$ | the symmetric quaternionic multiplication, the operation $\mathrm{SQA}$ |
| $N(\tilde P,\tilde Q)=P_0Q_0+(\vec P,\vec Q)$ | the quaternion form, the scalar part of the block |
| $A_\star(\tilde P),B_\star(\tilde P)$ | the left and the right annihilator of $\tilde P$ in the block, equal because the block is commutative |
| $L_{\tilde P}$ | the left multiplication operator, $L_{\tilde P}\tilde X=N(\tilde P,\tilde X)e_0$, of rank one for $\tilde P\neq0$ |
| $\tilde P^{\perp}=\{\tilde X:N(\tilde P,\tilde X)=0\}$ | the annihilator of a nonzero element, a complex hyperplane of dimension three |
| $N(\tilde P)=P_0^{2}+(\vec P,\vec P)$ | the algebraic norm, vanishing exactly when the element lies in its own annihilator |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), §*The Zero Divisor and the Annihilator*, for the zero divisor and the annihilator of a general product.
- *Introduction to the Symmetric Quaternionic Algebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-algebra-of-biquaternions.md`), for the product, its commutativity and its table.
- *Zero Divisors of the Symmetric Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-symmetric-quaternionic-algebra.md`), above this article in this category, for the criterion that makes the whole punctured space the zero-divisor set.
- *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra* (`articles_maths/the-radical-and-the-isotropic-elements-of-the-symmetric-quaternionic-algebra.md`), for the non-degeneracy of the form and the isotropic locus.
- *Square Roots of Zero and the Nilpotents of the Symmetric Quaternionic Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-symmetric-quaternionic-algebra.md`), for the isotropic elements, which are the nilpotents of index two and the elements lying in their own annihilator.
- *Annihilators of the General Plain Algebra* (`articles_maths/annihilators-of-the-general-plain-algebra.md`), the parent product, whose annihilator is a plane on the cone and zero off it.
