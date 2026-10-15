# __Annihilators of the Symmetric Plain Sesqualgebra__

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

The block of this article is the **symmetric plain sesquimultiplication**
$$
\tilde P\star\tilde Q=H(\tilde P,\tilde Q)e_0,\qquad
H(\tilde P,\tilde Q)=P_0\overline{Q_0}+(\vec P,\overline{\vec Q}),
$$
the Hermitian form read as a product (*Introduction to the Symmetric Plain Sesqualgebra of
Biquaternions*). It is conjugate-commutative and central valued, so the two annihilators of an
element are one set. The block is the Hermitian twin of the symmetric quaternionic algebra: the
zero-divisor set is the whole punctured space and the annihilator of every nonzero element is a
**hyperplane**, the orthogonal of the element for the Hermitian form. The article owns that
reading, the operator with its rank, and the shape of the annihilator on the remarkable subspaces;
the zero-divisor set is the cited article's.

**The results.** The block is conjugate-commutative and central valued, so the left and the right annihilators of every element coincide, $A_\star(\tilde P) = B_\star(\tilde P) = \ker L_{\tilde P}$. For every nonzero $\tilde P$ this common annihilator is the Hermitian orthogonal hyperplane $\tilde P^{\perp} = \{\tilde X : H(\tilde P,\tilde X) = 0\}$, of complex dimension three and real dimension six, and the multiplication operator $L_{\tilde P}$ has image the central line $\mathbb{C}e_0$ and rank one. The element lies in its own annihilator exactly on the isotropic locus, which for the definite form $H$ is the origin alone, and the annihilator of the product is $\{0\}$.

## The Annihilator of a Product

**The annihilator of an element is the set of partners it kills, the left and the right annihilator being the kernels of the left and the right multiplication, and here the two multiplications coincide, $R_{\tilde P} = L_{\tilde P}$, with image the central line and kernel a complex subspace.**

**Definition (annihilator).** Let $\star$ be a product on $\mathbb{B}$ and let
$\tilde Q\in\mathbb{B}$. The **left annihilator** and the **right annihilator** of $\tilde Q$ in
$\star$ are
$$
A_\star(\tilde Q)=\{\tilde X:\tilde Q\star\tilde X=0\},\qquad
B_\star(\tilde Q)=\{\tilde X:\tilde X\star\tilde Q=0\}.
$$
They are the kernels of the left and the right multiplication, and they are nonzero exactly when
$\tilde Q$ is a zero divisor of the corresponding side.

Throughout this article the product is the **symmetric plain sesquimultiplication** $\star$, and
unqualified, *annihilator* means the annihilator of $\star$. The one-sided multiplications are the
operators
$$
L_{\tilde P}\tilde X=H(\tilde P,\tilde X)e_0,\qquad R_{\tilde P}=L_{\tilde P},
$$
conjugate-linear in $\tilde X$ because the form is, with image the central line and kernel a
complex subspace. The block is the sibling of the symmetric quaternionic algebra, whose
annihilators are *Annihilators of the Symmetric Quaternionic Algebra*.

## The Two Annihilators Coincide

**The block is conjugate-commutative, so the two annihilators of every element are one set, $B_\star(\tilde P) = A_\star(\tilde P) = \ker L_{\tilde P}$.**

**Proposition (the two annihilators coincide).** For every $\tilde P$,
$$
B_\star(\tilde P)=A_\star(\tilde P)=\ker L_{\tilde P}.
$$

*Proof.* The block is conjugate-commutative,
$\tilde X\star\tilde P=\overline{\tilde P\star\tilde X}$; a scalar is zero exactly when its
conjugate is, so the two products vanish together and the two annihilators are one set, the kernel
of the one operator of the block.

## The Annihilator of an Element

**For every nonzero $\tilde P$ the common annihilator is the Hermitian orthogonal hyperplane $\tilde P^{\perp}$, of complex dimension three, while at $\tilde P = 0$ it is all of $\mathbb{B}$ and the annihilator of the product is $\{0\}$.**

**Theorem (the annihilator is the orthogonal hyperplane).** For $\tilde P\neq0$,
$$
A_\star(\tilde P)=B_\star(\tilde P)=\{\tilde X:H(\tilde P,\tilde X)=0\}=\tilde P^{\perp},
$$
the orthogonal of $\tilde P$ for the Hermitian form, a complex subspace of dimension three and real
dimension six. For $\tilde P=0$ both annihilators are all of $\mathbb{B}$. The annihilator of the
product,
$$
\{\tilde Q:H(\tilde Q,\tilde X)=0\ \text{for every }\tilde X\}=\{0\},
$$
is zero.

*Proof.* The annihilator is the kernel of the nonzero functional
$\tilde X\mapsto H(\tilde P,\tilde X)$, a hyperplane. The element lies in its own annihilator
exactly when $H(\tilde P,\tilde P)=0$, the isotropic locus. The annihilator of the
product is the radical of the form, which is $\{0\}$ because $H$ is non-degenerate.

**Corollary (the operator and its rank).** The operator $L_{\tilde P}$ has image the central line
$\mathbb{C}e_0$ for every $\tilde P\neq0$, and kernel $\tilde P^{\perp}$, of complex dimension
three. At $\tilde P=0$ the operator is zero and the kernel is the whole space.

## The Dichotomy

**The zero-divisor set of the block separates nothing, being the whole punctured space, while the annihilator separates everything: it is the hyperplane $\tilde P^{\perp}$ for every nonzero element, and the isotropic locus is the set where the element lies in its own annihilator.**

The zero-divisor set of the block is the whole punctured space, so it separates nothing. The
annihilator separates everything: it is the Hermitian orthogonal $\tilde P^{\perp}$, a hyperplane,
and it is nonzero for every nonzero element. The block is the Hermitian twin of the symmetric
quaternionic algebra; both have the hyperplane annihilator, and they differ in the form, the
bilinear $N=P_0Q_0+(\vec P,\vec Q)$ in the one and the Hermitian
$H=P_0\overline{Q_0}+(\vec P,\overline{\vec Q})$ in the other. The isotropic locus is the set
where the element lies in its own annihilator, and the block has no other separation.

## The Annihilator on the Remarkable Subspaces

**On the remarkable subspaces the annihilator is read as follows: a nonzero central element has the vector subspace as its annihilator, a nonzero pure element has a hyperplane as its annihilator, and on the Hermitian and anti-Hermitian subspaces the annihilator of a nonzero element meets the subspace in a hyperplane of it.**

**The centre.** A nonzero central element $\tilde P=\lambda e_0$ has
$H(\lambda e_0,\tilde X)=\lambda\overline{X_0}$, so its annihilator is $\{X_0=0\}$, the vector
subspace. The centre is the subspace whose nonzero elements annihilate exactly the vector subspace.

**The vector subspace.** A nonzero pure element $\tilde P=\vec P$ has
$H(\vec P,\tilde X)=(\vec P,\overline{\vec X})$, so its annihilator is the hyperplane
$\{\tilde X:(\vec P,\overline{\vec X})=0\}$. It contains the centre and, inside the vector
subspace, the Hermitian orthogonal plane of $\vec P$; the element $\vec P$ lies in its own
annihilator exactly when it is isotropic for $H$.

**The Hermitian and anti-Hermitian subspaces.** On the Hermitian subspace the form $H$ is the
squared norm and the restriction is non-degenerate; the annihilator of a nonzero Hermitian element
meets the subspace in a hyperplane of it, and the isotropic directions of the subspace are the
elements lying in their own annihilators.

## Summary

The annihilator of an element in a product is the set of partners the element kills, the left and
the right annihilator being the kernels of the left and the right multiplication. The symmetric
plain sesquimultiplication is conjugate-commutative and central valued,
$\tilde P\star\tilde X=H(\tilde P,\tilde X)e_0$ with
$H(\tilde P,\tilde X)=P_0\overline{X_0}+(\vec P,\overline{\vec X})$, so the two annihilators
of an element coincide. Every nonzero element is a zero divisor and every nonzero element has the
**hyperplane** $\tilde P^{\perp}$ as annihilator, of complex dimension three; the element lies in
its own annihilator exactly when it is isotropic, and the annihilator of the product is $\{0\}$
because the Hermitian form is non-degenerate. The block is the Hermitian twin of the symmetric
quaternionic algebra, and the two differ only in the form.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q=H(\tilde P,\tilde Q)e_0$ | the symmetric plain sesquimultiplication, the operation $\mathrm{SPS}$ |
| $H(\tilde P,\tilde Q)=P_0\overline{Q_0}+(\vec P,\overline{\vec Q})$ | the Hermitian form, the scalar part of the block |
| $A_\star(\tilde P),B_\star(\tilde P)$ | the left and the right annihilator, equal because the block is conjugate-commutative |
| $L_{\tilde P}$ | the left multiplication operator, $L_{\tilde P}\tilde X=H(\tilde P,\tilde X)e_0$, of rank one for $\tilde P\neq0$ |
| $\tilde P^{\perp}=\{\tilde X:H(\tilde P,\tilde X)=0\}$ | the annihilator of a nonzero element, a complex hyperplane of dimension three |
| $H(\tilde P,\tilde P)$ | the norm, vanishing exactly when the element lies in its own annihilator |

## Further Reading

- *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternion-c-space.md`), §*The Zero Divisor and the Annihilator*, for the zero divisor and the annihilator of a general product.
- *Introduction to the Symmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-plain-sesqualgebra-of-biquaternions.md`), for the Hermitian form and its product.
- *Zero Divisors of the Symmetric Plain Sesqualgebra* (`articles_maths/zero-divisors-of-the-symmetric-plain-sesqualgebra.md`), above this article in this category, for the criterion that makes the whole punctured space the zero-divisor set.
- *Norm and Invertibility in the Symmetric Plain Sesqualgebra* (`articles_maths/norm-and-invertibility-in-the-symmetric-plain-sesqualgebra.md`), for the Hermitian form and its radical.
- *Annihilators of the Symmetric Quaternionic Algebra* (`articles_maths/annihilators-of-the-symmetric-quaternionic-algebra.md`), the bilinear twin, whose hyperplane is read for the quaternion form.
- *Introduction to the Remarkable Subspaces* (`articles_maths/introduction-to-the-remarkable-subspaces.md`), for the subspaces on which the annihilator is read.
