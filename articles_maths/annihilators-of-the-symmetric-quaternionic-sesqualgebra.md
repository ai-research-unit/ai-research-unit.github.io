# __Annihilators of the Symmetric Quaternionic Sesqualgebra__

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

The block of this article is the **symmetric quaternionic sesquimultiplication**
$$
\tilde P\star\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q^{*}+\overline{\tilde Q^{\natural}\tilde P^{*}}\bigr)
=\bigl[P_0\overline{Q_0}-(\vec P,\overline{\vec Q})\bigr]-P_0\overline{\vec Q}-\overline{Q_0}\vec P,
$$
the Hermitian symmetrisation of the sesquilinear product (*Introduction to the Symmetric
Quaternionic Sesqualgebra of Biquaternions*). It is conjugate-commutative, so the two annihilators
of an element are one set, and its zero divisors are the nonzero pure elements together with the
elements of the cone $C(\tilde P)=0$ (*Zero Divisors of the Symmetric Quaternionic Sesqualgebra*, above
this article in this category).
The annihilator is a complex plane in the pure case and a complex line in the non-pure case, so it
separates the two families where the criterion only joins them. The article owns that reading, the
operator with its rank, and the shape of the annihilator on the remarkable subspaces; the
zero-divisor set and the comparison with the four general products are the cited article's.

**The results.** The annihilator of an element is the set of partners it kills, and the block is conjugate-commutative, so its left and right annihilators are one set. Off the cone the annihilator is $\{0\}$; a pure zero divisor annihilates a complex plane, of complex dimension two, and a non-pure zero divisor annihilates the complex line $\mathbb{C}\tilde Q^{\natural}$, of complex dimension one. The left multiplication therefore has complex rank four on the regular elements, three on the non-pure family and two on the pure family, and rank zero at the origin.

## The Annihilator of a Product

**The annihilator of an element in a product is the set of partners that it kills, the left annihilator being the kernel of the left multiplication and the right annihilator the kernel of the right multiplication; both are nonzero exactly when the element is a zero divisor of the corresponding side.**

**Definition (annihilator).** Let $\star$ be a product on $\mathbb{B}$ and let
$\tilde Q\in\mathbb{B}$. The **left annihilator** and the **right annihilator** of $\tilde Q$ in
$\star$ are
$$
A_\star(\tilde Q)=\{\tilde X:\tilde Q\star\tilde X=0\},\qquad
B_\star(\tilde Q)=\{\tilde X:\tilde X\star\tilde Q=0\}.
$$
They are the kernels of the left and the right multiplication, and they are nonzero exactly when
$\tilde Q$ is a zero divisor of the corresponding side.

Throughout this article the product is the **symmetric quaternionic sesquimultiplication** $\star$,
and unqualified, *annihilator* means the annihilator of $\star$. The one-sided multiplications are
the operators
$$
L_{\tilde P}\tilde X=\tilde P\star\tilde X,\qquad R_{\tilde P}=L_{\tilde P},
$$
read in coordinates in *The Multiplication Operators of the Symmetric Quaternionic Sesqualgebra*.
The block is the sesquilinear sibling of the symmetric quaternionic algebra and the quaternionic
sibling of the symmetric plain sesqualgebra, whose annihilators are *Annihilators of the Symmetric
Quaternionic Algebra* and *Annihilators of the Symmetric Plain Sesqualgebra*.

## The Two Annihilators Coincide

**The block is conjugate-commutative, so an element is a left zero divisor exactly when it is a right zero divisor, and the two annihilators of every element coincide, $A_\star(\tilde Q)=B_\star(\tilde Q)$.**

**Theorem (the two sides coincide).** $\tilde Q$ is a left zero divisor of the block if and only if
it is a right zero divisor, and $A_\star(\tilde Q)=B_\star(\tilde Q)$ for every $\tilde Q$.

*Proof.* The block is conjugate-commutative,
$\tilde P\star\tilde Q=\overline{\tilde Q\star\tilde P}$. Applying it,
$\tilde R\star\tilde Q=\overline{\tilde Q\star\tilde R}$, so $\tilde R\star\tilde Q=0$ holds
exactly when $\tilde Q\star\tilde R=0$; the defining sets are equal.

## The Annihilator of an Element

**A pure zero divisor annihilates the complex plane $\{\tilde R:R_0=0,\ \sum_kQ_k\overline{R_k}=0\}$ and a non-pure zero divisor annihilates the complex line $\mathbb{C}\tilde Q^{\natural}$; off the cone the annihilator is $\{0\}$.**

**Theorem (the annihilators).** The annihilator of a zero divisor $\tilde Q$ of the block is
$$
A_\star(\tilde Q)=
\begin{cases}
\{\tilde R:R_0=0,\ \sum_{k}Q_k\overline{R_k}=0\}, & Q_0=0,\\[2mm]
\{\tilde R:R_0=\mu,\ R_k=-\dfrac{\mu}{\overline{Q_0}}\,\overline{Q_k},\ \mu\in\mathbb{C}\}, & Q_0\neq0,
\end{cases}
$$
of complex dimension two in the pure case and complex dimension one in the non-pure case. For an
element off the cone the annihilator is $\{0\}$.

*Proof.* In the pure case the computations of the criterion leave $R_0=0$ and the single complex
condition $\sum_kQ_k\overline{R_k}=0$ on the three unknowns $R_1,R_2,R_3$, whose solutions form a
complex plane. In the non-pure case the same computations express $\tilde R$ through the free
parameter $R_0$, and the assignment $\mu\mapsto\tilde R(\mu)$ is complex-linear and injective.

**Corollary (the rank of the left multiplication).** The left multiplication
$L_{\tilde Q}:\tilde R\mapsto\tilde Q\star\tilde R$ has kernel $A_\star(\tilde Q)$, so it is
injective exactly when $\tilde Q$ is regular; as an endomorphism of $\mathbb{B}$ it has complex
rank four on the regular elements, three on the non-pure family, two on the pure family and rank
zero at the origin.

*Proof.* The kernel is the annihilator by definition, of dimension zero, one and two according to
whether $\tilde Q$ is regular, a non-pure zero divisor or a pure zero divisor, and of dimension
four at the origin; the ranks are four minus those dimensions.

**Example.** For the pure zero divisor $\tilde Q=e_1+ie_2$, of central square $1-1=0$, the
annihilator is the complex plane
$$
A_\star(e_1+ie_2)=\mathbb{C}\{e_1-ie_2,\ e_3\}=\mathbb{C}\{\tilde Q^{\natural},\ e_3\},
$$
and for the non-pure zero divisor $\tilde Q=e_0+ie_1$, of central square $1-1=0$, the annihilator
is the complex line
$$
A_\star(e_0+ie_1)=\mathbb{C}\{e_0+ie_1\}=\mathbb{C}\tilde Q.
$$

## The Dichotomy

**The annihilator separates the two families that the criterion joins: it is a complex plane on the pure family and a complex line on the non-pure family, and the left multiplication has complex rank two on the first and three on the second.**

The zero-divisor set of the block is the enlarged set of the pure family $\{\tilde Q\neq0:Q_0=0\}$ and
the punctured cone $\{\tilde Q\neq0:C(\tilde Q)=0\}$, and the annihilator reads its two families
apart: the pure family annihilates a complex plane and the non-pure family a complex line, and the
operator has rank two on the first and three on the second. The block is the conjugation-free twin
of the antisymmetric plain sesqualgebra, whose annihilator is likewise a plane in one case and a line
in the other; the difference is that
the antisymmetric block reads the second case as a plane in the non-degenerate direction, while
here the second case is the line $\mathbb{C}\tilde Q^{\natural}$ of the isotropic element, exactly
as in the symmetric plain algebra. The three blocks carry the same pair of annihilator shapes.

## The Annihilator on the Remarkable Subspaces

**The centre annihilates nothing; a nonzero pure element annihilates a complex plane in the ambient block and a complex line inside the vector subspace; and on the conjugate-changed subspaces the annihilator is again a plane read off the same equation.**

**The centre.** A nonzero central element $\tilde P=\lambda e_0$ has central square
$\lambda^{2}\neq0$, so it is regular and its annihilator is $\{0\}$: the centre annihilates
nothing.

**The vector subspace.** A nonzero pure element $\tilde P=\vec P$ has the plane annihilator
above; inside the vector subspace the annihilator falls to the line through the element, because
the single equation $\sum_kP_k\overline{X_k}=0$ restricted to the vector subspace leaves that line.

**The conjugate-changed subspaces.** The star in the second slot exchanges an element and its
conjugate, so on the Hermitian subspace, where the star fixes the vector part, the annihilator of a
nonzero pure Hermitian element is again a complex plane, and on the anti-Hermitian subspace it is
the conjugate plane read off the same equation.

## Summary

The annihilator of an element in a product is the set of partners the element kills, the left and
the right annihilator being the kernels of the left and the right multiplication. The symmetric
quaternionic sesquimultiplication is conjugate-commutative, so the two annihilators of an element
coincide. The zero divisors of the block are the nonzero pure elements together with the elements of
the cone $C(\tilde Q)=0$: a pure zero divisor annihilates the complex plane
$\{\tilde R:R_0=0,\ \sum_kQ_k\overline{R_k}=0\}$ and a non-pure zero divisor annihilates the complex line
$\mathbb{C}\tilde Q^{\natural}$, and the elements outside the two families are regular. The annihilator
separates the two families that the criterion joins, and the operator has rank two on the pure family
and three on the non-pure family.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q^{*}+\overline{\tilde Q^{\natural}\tilde P^{*}})$ | the symmetric quaternionic sesquimultiplication, the operation $\mathrm{SQS}$ |
| $A_\star(\tilde P),B_\star(\tilde P)$ | the left and the right annihilator, equal because the block is conjugate-commutative |
| $L_{\tilde P}$ | the left multiplication operator, whose kernel is the annihilator |
| $\{\tilde R:R_0=0,\ \sum_kP_k\overline{R_k}=0\}$ | the annihilator of a nonzero pure element, a complex plane |
| $\mathbb{C}\tilde Q^{\natural}$ | the annihilator of a non-pure zero divisor, a complex line |
| $C(\tilde P)=\sum_\mu P_\mu^{2}$ | the central square, the criterion of the cone |

## Further Reading

- *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternioid-c-space.md`), §*The Zero Divisor and the Annihilator*, for the zero divisor and the annihilator of a general product.
- *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-sesqualgebra.md`), for the operation and its conjugate-commutativity.
- *Zero Divisors of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/zero-divisors-of-the-symmetric-quaternionic-sesqualgebra.md`), above this article in this category, for the criterion and the two families.
- *The Multiplication Operators of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-quaternionic-sesqualgebra.md`), for the operator calculus on which the rank is read.
- *Annihilators of the Symmetric Plain Algebra* (`articles_maths/annihilators-of-the-symmetric-plain-algebra.md`), the bilinear twin, with the same pair of annihilator shapes.
- *Annihilators of the Antisymmetric Plain Sesqualgebra* (`articles_maths/annihilators-of-the-antisymmetric-plain-sesqualgebra.md`), the conjugation-free sibling, whose annihilator is a line or a plane.
