# __Annihilators of the General Plain Algebra__

## Introduction

The zero divisor of a product is a property of one element alone: it says that *some* nonzero
partner exists that the element kills. The annihilator says *which* partners those are, and it is
the finer object. It is the set of elements killed by a fixed element,
$$
A_\star(\tilde q)=\{\tilde x:\tilde q\star\tilde x=0\},\qquad
B_\star(\tilde q)=\{\tilde x:\tilde x\star\tilde q=0\},
$$
the left and the right annihilator (*Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*,
§*The Zero Divisor and the Annihilator*). When the product is carried by a multiplication operator
the annihilator is the kernel of that operator, so it is a linear subspace and its computation is
one of linear algebra.

The block of this article is the **general plain multiplication**, the product $\tilde p\tilde q$
of the quaternion algebra $\mathbb{H}$ (*Introduction to the General Plain Algebra of
Quaternions*). It is associative, it carries the two-sided unit $e_0$, and over $\mathbb{R}$ it is
a division algebra: every nonzero element is invertible, by the norm criterion $N(\tilde q)\neq0$
(*Norm and Invertibility in the General Plain Algebra*). The block therefore has no zero divisors
and no Zero Divisors article, because there is no set to characterise. What is left of the element
theory is the vanishing of the annihilator, and the article is short for that reason. It owns the
annihilator of the block, the two multiplication operators, the rank table and the reading on the
remarkable subspaces.

The chapter carries the structure-level article *Annihilators in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*
(`articles_maths/annihilators-in-the-algebraic-structures-over-the-quaternion-r-space.md`), whose annihilating set asks the other question:
which elements kill the whole space for a fixed product, the radical of that product, where this
article asks which elements a fixed element kills. The two notions are transposed, not equal.

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

Throughout this article the product is the **general plain multiplication** $\star$, and
unqualified, *annihilator* means the annihilator of $\star$. The two one-sided multiplications are
the operators
$$
L_{\tilde p}\tilde x=\tilde p\tilde x,\qquad R_{\tilde p}\tilde x=\tilde x\tilde p,
$$
the left and the right multiplication of the algebra (*One-Sided Operators on the General Plain
Algebra of Quaternions*), and
$$
A_\star(\tilde p)=\ker L_{\tilde p},\qquad B_\star(\tilde p)=\ker R_{\tilde p}.
$$

## The Annihilator Is Zero

**Theorem (the annihilator of a nonzero element is zero).** Let $\tilde q\in\mathbb{H}$.

- If $\tilde q\neq0$ then $A_\star(\tilde q)=B_\star(\tilde q)=\{0\}$.
- If $\tilde q=0$ then $A_\star(\tilde q)=B_\star(\tilde q)=\mathbb{H}$.

*Proof.* If $\tilde q\tilde x=0$ with $\tilde q\neq0$, multiply on the left by the inverse
$\tilde q^{-1}$, which exists by the division property; then $\tilde x=0$. The right side is the
same computation with the inverse on the right. At $\tilde q=0$ both products vanish for every
$\tilde x$, so both annihilators are the whole space.

**Corollary (the two sides coincide).** $A_\star(\tilde q)=B_\star(\tilde q)$ for every $\tilde q$:
off the origin both are $\{0\}$, and at the origin both are $\mathbb{H}$. No nonzero element is a
zero divisor of either side, and the annihilator is never a proper nonzero subspace.

## The Multiplication Operator and the Rank

**Proposition (the operators and their invariants).** In the basis $e_0,e_1,e_2,e_3$ the operators
$L_{\tilde p}$ and $R_{\tilde p}$ of an element $\tilde p=p_0e_0+\vec p$ have trace $4p_0$ each
and determinant
$$
\det L_{\tilde p}=\det R_{\tilde p}=N(\tilde p)^2=(p_0^2+|\vec p|^2)^2,
$$
and the characteristic polynomial
$$
\chi_{L_{\tilde p}}(t)=\chi_{R_{\tilde p}}(t)=(t^2-2p_0t+N(\tilde p))^2.
$$

*Proof.* The matrix of $L_{\tilde p}$ is the left multiplication matrix of the quaternion
$\tilde p$: its trace is $4p_0$ and its determinant is the square of the norm, $N(\tilde p)^2$. The
matrix of $R_{\tilde p}$ is the transpose of that of $L_{\tilde p}$ for the plain form,
$R_{\tilde p}=L_{\tilde p}^{\sim}$ in the notation $F^{\sim}=DF^{\mathsf T}D$ with
$D=\operatorname{diag}(1,-1,-1,-1)$ (*Association and the Transpose on the General Plain Algebra*,
and *One-Sided Operators on the General Plain Algebra of Quaternions*,
$L_{\tilde a}^{\sim}=R_{\tilde a}$); a transpose has the same trace and the same characteristic
polynomial, hence the same determinant. The quadratic factor $t^2-2p_0t+N(\tilde p)$ has
discriminant $-4|\vec p|^2$: it is $(t-p_0)^2$ at $\vec p=0$, and it has no real root when
$\vec p\neq0$. The invariants are computed exactly on $e_0$, $(2,-3,5,7)$, $(0,1,2,3)$ and $0$
in the verification of this article.

**Corollary (the rank and the annihilator).** The rank of the two operators and the two
annihilators of $\tilde q$ are

| $\tilde q$ | $N(\tilde q)$ | $\operatorname{rank}L_{\tilde q},\operatorname{rank}R_{\tilde q}$ | $\dim A_\star(\tilde q),\dim B_\star(\tilde q)$ |
|---|---|---|---|
| $0$ | $0$ | $0$ | $4$ |
| $\tilde q\neq0$ | $\neq0$ | $4$ | $0$ |

*Proof.* The determinant $N(\tilde q)^2$ is nonzero exactly when $\tilde q\neq0$, by the positive
definiteness of the norm; then both operators are invertible and both annihilators are $\{0\}$. The
origin gives the zero operator, of kernel the whole space. All dimensions are real dimensions, the
space being the real vector space $\mathbb{H}\cong\mathbb{R}^4$.

## The Dichotomy

The dichotomy of the block is the annihilator's, and it is as short as a dichotomy can be: off the
origin the annihilator is $\{0\}$, at the origin it is the whole space. There is no intermediate
case, and there is no locus on which the rank drops. The zero-divisor cone of the complexified
block is the norm equation $N=0$; over $\mathbb{R}$ the norm is positive definite, so that cone
meets the real space only at the origin. The dichotomy is therefore exactly the split of the space
into the origin and its complement, and it carries no more than the division property itself. Where
the complexified block has a genuine hypersurface of zero divisors and reads a pair of annihilator
planes on it (*Annihilators of the General Plain Algebra*, the biquaternion block), the real block
has a single point and nothing on it but the whole space.

## The Annihilator on the Remarkable Subspaces

**The centre.** A nonzero central element $\tilde p=\lambda e_0$ with $\lambda\neq0$ has
$L_{\tilde p}\tilde x=\lambda\tilde x$, the scalar operator, so it is invertible and its
annihilator is $\{0\}$. The centre is the scalar line $\mathbb{R}e_0$ (*Introduction to the General
Plain Algebra of Quaternions*), and a nonzero central element is invertible as a nonzero scalar is.

**The vector subspace.** A nonzero pure element $\tilde p=\vec p$ has norm $|\vec p|^2>0$, so
it is invertible and its annihilator is $\{0\}$. The vector subspace is as free of annihilators as
the whole space.

**The general reading.** On a remarkable subspace the annihilator of an element of the subspace is
the intersection of the ambient annihilator with the subspace. The ambient annihilator is $\{0\}$
at every nonzero element, so the annihilator of a nonzero element of the centre or of the vector
subspace is again $\{0\}$; the only nonzero annihilator anywhere is the whole space, at the single
origin.

## Summary

The annihilator of an element in a product is the set of partners the element kills, the left and
the right annihilator being the kernels of the left and the right multiplication. The general plain
multiplication is the associative product of the quaternion algebra $\mathbb{H}$, which over
$\mathbb{R}$ is a division algebra. Its operators $L_{\tilde p}$ and $R_{\tilde p}$ have trace
$4p_0$ and determinant $N(\tilde p)^2=(p_0^2+|\vec p|^2)^2$, and characteristic polynomial
$(t^2-2p_0t+N(\tilde p))^2$. The annihilator of every nonzero element is $\{0\}$ on both sides, and
the two sides coincide trivially; the annihilator of the origin is the whole space. The dichotomy
is therefore the split of the space into the origin and its complement, with no intermediate case
and no rank drop, because the zero-divisor cone of the complexified block meets the real space only
at the origin. On the remarkable subspaces, the centre $\mathbb{R}e_0$ and the vector subspace, the
annihilator of a nonzero element is again $\{0\}$, a nonzero central element being an invertible
scalar. The block has no Zero Divisors article, and this one is short, because there is nothing for
it to characterise.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde p\tilde q$ | the general plain multiplication, the product of the quaternion algebra $\mathbb{H}$ |
| $A_\star(\tilde q)=\{\tilde x:\tilde q\tilde x=0\}$ | the left annihilator of $\tilde q$, the kernel of the left multiplication |
| $B_\star(\tilde q)=\{\tilde x:\tilde x\tilde q=0\}$ | the right annihilator of $\tilde q$, the kernel of the right multiplication |
| $L_{\tilde p},R_{\tilde p}$ | the left and the right multiplication operators, of determinant $N(\tilde p)^2$ and trace $4p_0$ |
| $\chi_{L_{\tilde p}}(t)=(t^2-2p_0t+N(\tilde p))^2$ | the characteristic polynomial of the operator |
| $N(\tilde p)=p_0^2+|\vec p|^2$ | the quaternion norm, positive definite over $\mathbb{R}$ |
| $A_\star(\tilde q)=B_\star(\tilde q)$ | the two sides coincide, being $\{0\}$ off the origin and $\mathbb{H}$ at the origin |

## Further Reading

- *Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-quaternion-r-space.md`), §*The Element Vocabulary*, for the zero divisor, the annihilator and the regular element of a general product.
- *Annihilators in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/annihilators-in-the-algebraic-structures-over-the-quaternion-r-space.md`), the structure-level article of the chapter, for the other question: which elements kill the whole space for a fixed product, the radical, where this article fixes the element and reads the partners it kills.
- *Introduction to the General Plain Algebra of Quaternions* (`articles_maths/introduction-to-the-general-plain-algebra-of-quaternions.md`), for the product, its associativity and its table.
- *Norm and Invertibility in the General Plain Algebra* (`articles_maths/norm-and-invertibility-in-the-general-plain-algebra-of-quaternions.md`), for the norm and the division property that make every nonzero element a unit.
- *One-Sided Operators on the General Plain Algebra of Quaternions* (`articles_maths/one-sided-operators-on-the-general-plain-algebra-of-quaternions.md`), for the operators $L_{\tilde p}$ and $R_{\tilde p}$ and their invertibility.
- *Association and the Transpose on the General Plain Algebra* (`articles_maths/association-and-the-transpose-on-the-general-plain-algebra-of-quaternions.md`), for the transpose $F^{\sim}=DF^{\mathsf T}D$ of the plain form, under which the right multiplication is the transpose of the left.
- *Annihilators of the General Plain Algebra* (`articles_maths/annihilators-of-the-general-plain-algebra.md`), the complexified counterpart in the biquaternion chapter, where the cone is a hypersurface and the annihilator of a nonzero cone element is a pair of planes.
- *The Specificities of the General Plain Algebra* (`articles_maths/the-specificities-of-the-general-plain-algebra-of-quaternions.md`), for why the empty classes of the block are folded into a single article.
