# __Annihilators of the Quaternion Algebra__

## Introduction

The zero divisor of a product is a property of one element alone: it says that *some* nonzero
partner exists that the element kills. The annihilator says *which* partners those are, and it is
the finer object. It is the set of elements killed by a fixed element,
$$
A_\star(\tilde q_1)=\{\tilde q_2:\tilde q_1\star\tilde q_2=0\},\qquad
B_\star(\tilde q_1)=\{\tilde q_2:\tilde q_2\star\tilde q_1=0\},
$$
the left and the right annihilator (*Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*,
§*The Zero Divisor and the Annihilator*). When the product is carried by a multiplication operator
the annihilator is the kernel of that operator, so it is a linear subspace and its computation is
one of linear algebra.

The block of this article is the **quaternion multiplication**, the product $\tilde q_1\tilde q_2$
of the quaternion algebra $\mathbb{H}$ (*Introduction to the Quaternion Algebra of
Quaternions*). It is associative, it carries the two-sided unit $e_t$, and over $\mathbb{R}$ it is
a division algebra: every nonzero element is invertible, by the norm criterion $\langle\tilde q\rangle_{\natural}\neq0$
(*Norm and Invertibility in the Quaternion Algebra*). The block therefore has no zero divisors. The zero-divisor set, empty here, is read in *Zero Divisors of the Quaternion Algebra*, above this article in this category. What is left for this article is the vanishing of the annihilator, and it is short for that reason. It owns the
annihilator of the block, the two multiplication operators, the rank table and the reading on the
remarkable subspaces.


## The Annihilator of a Product

**Definition (annihilator).** Let $\star$ be a product on $\mathbb{H}$ and let
$\tilde q_1\in\mathbb{H}$. The **left annihilator** and the **right annihilator** of $\tilde q_1$ in
$\star$ are
$$
A_\star(\tilde q_1)=\{\tilde q_2:\tilde q_1\star\tilde q_2=0\},\qquad
B_\star(\tilde q_1)=\{\tilde q_2:\tilde q_2\star\tilde q_1=0\}.
$$
They are the kernels of the left and the right multiplication, and they are nonzero exactly when
$\tilde q_1$ is a zero divisor of the corresponding side.

Throughout this article the product is the **quaternion multiplication** $\star$, and
unqualified, *annihilator* means the annihilator of $\star$. The two one-sided multiplications are
the operators
$$
L_{\tilde q_1}\tilde q_2=\tilde q_1\tilde q_2,\qquad R_{\tilde q_1}\tilde q_2=\tilde q_2\tilde q_1,
$$
the left and the right multiplication of the algebra (*One-Sided Operators on the Quaternion Algebra*), and
$$
A_\star(\tilde q_1)=\ker L_{\tilde q_1},\qquad B_\star(\tilde q_1)=\ker R_{\tilde q_1}.
$$

## The Annihilator Is Zero

**Theorem (the annihilator of a nonzero element is zero).** Let $\tilde q_1\in\mathbb{H}$.

- If $\tilde q_1\neq0$ then $A_\star(\tilde q_1)=B_\star(\tilde q_1)=\{0\}$.
- If $\tilde q_1=0$ then $A_\star(\tilde q_1)=B_\star(\tilde q_1)=\mathbb{H}$.

*Proof.* If $\tilde q_1\tilde q_2=0$ with $\tilde q_1\neq0$, multiply on the left by the inverse
$\tilde q_1^{-1}$, which exists by the division property; then $\tilde q_2=0$. The right side is the
same computation with the inverse on the right. At $\tilde q_1=0$ both products vanish for every
$\tilde q_2$, so both annihilators are the whole space.

**Corollary (the two sides coincide).** $A_\star(\tilde q)=B_\star(\tilde q)$ for every $\tilde q$:
off the origin both are $\{0\}$, and at the origin both are $\mathbb{H}$. No nonzero element is a
zero divisor of either side, and the annihilator is never a proper nonzero subspace.

## The Multiplication Operator and the Rank

**Proposition (the operators and their invariants).** In the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ the operators
$L_{\tilde q}$ and $R_{\tilde q}$ of an element $\tilde q=q_te_t+\vec q$ have trace $4q_t$ each
and determinant
$$
\det L_{\tilde q}=\det R_{\tilde q}=\langle\tilde q\rangle_{\natural}^2=(q_t^2+|\vec q|^2)^2,
$$
and the characteristic polynomial
$$
\chi_{L_{\tilde q}}(t)=\chi_{R_{\tilde q}}(t)=(t^2-2q_tt+\langle\tilde q\rangle_{\natural})^2.
$$

*Proof.* The matrix of $L_{\tilde q}$ is the left multiplication matrix of the quaternion
$\tilde q$: its trace is $4q_t$ and its determinant is the square of the norm, $\langle\tilde q\rangle_{\natural}^2$. The
matrix of $R_{\tilde q}$ is the transpose of that of $L_{\tilde q}$ for the plain form,
$R_{\tilde q}=L_{\tilde q}^{\sim}$ in the notation $F^{\sim}=DF^{\mathsf T}D$ with
$D=\operatorname{diag}(1,-1,-1,-1)$ (*Association and the Transpose on the Quaternion Algebra*,
and *One-Sided Operators on the Quaternion Algebra*,
$L_{\tilde q_3}^{\sim}=R_{\tilde q_3}$); a transpose has the same trace and the same characteristic
polynomial, hence the same determinant. The quadratic factor $t^2-2q_tt+\langle\tilde q\rangle_{\natural}$ has
discriminant $-4|\vec q|^2$: it is $(t-q_t)^2$ at $\vec q=0$, and it has no real root when
$\vec q\neq0$. The invariants are computed exactly on $e_t$, $(2,-3,5,7)$, $(0,1,2,3)$ and $0$
in the verification of this article.

**Corollary (the rank and the annihilator).** The rank of the two operators and the two
annihilators of $\tilde q$ are

| $\tilde q$ | $\langle\tilde q\rangle_{\natural}$ | $\operatorname{rank}L_{\tilde q},\operatorname{rank}R_{\tilde q}$ | $\dim A_\star(\tilde q),\dim B_\star(\tilde q)$ |
|---|---|---|---|
| $0$ | $0$ | $0$ | $4$ |
| $\tilde q\neq0$ | $\neq0$ | $4$ | $0$ |

*Proof.* The determinant $\langle\tilde q\rangle_{\natural}^2$ is nonzero exactly when $\tilde q\neq0$, by the positive
definiteness of the norm; then both operators are invertible and both annihilators are $\{0\}$. The
origin gives the zero operator, of kernel the whole space. All dimensions are real dimensions, the
space being the real vector space $\mathbb{H}\cong\mathbb{R}^4$.

## The Dichotomy

The dichotomy of the block is the annihilator's, and it is as short as a dichotomy can be: off the
origin the annihilator is $\{0\}$, at the origin it is the whole space. There is no intermediate
case, and there is no locus on which the rank drops. The zero-divisor cone of the complexified
block is the norm equation $\langle\cdot\rangle_{\natural}=0$; over $\mathbb{R}$ the norm is positive definite, so that cone
meets the real space only at the origin. The dichotomy is therefore exactly the split of the space
into the origin and its complement, and it carries no more than the division property itself. Where
the complexified block has a genuine hypersurface of zero divisors and reads a pair of annihilator
planes on it (*Annihilators of the Quaternion Algebra*, the biquaternion block), the real block
has a single point and nothing on it but the whole space.

## The Annihilator on the Remarkable Subspaces

**The centre.** A nonzero central element $\tilde q_1=\lambda e_t$ with $\lambda\neq0$ has
$L_{\tilde q_1}\tilde q_2=\lambda\tilde q_2$, the scalar operator, so it is invertible and its
annihilator is $\{0\}$. The centre is the scalar line $\mathbb{R}e_t$ (*Introduction to the General
Plain Algebra of Quaternions*), and a nonzero central element is invertible as a nonzero scalar is.

**The vector subspace.** A nonzero pure element $\tilde q=\vec q$ has norm $|\vec q|^2>0$, so
it is invertible and its annihilator is $\{0\}$. The vector subspace is as free of annihilators as
the whole space.

**The general reading.** On a remarkable subspace the annihilator of an element of the subspace is
the intersection of the ambient annihilator with the subspace. The ambient annihilator is $\{0\}$
at every nonzero element, so the annihilator of a nonzero element of the centre or of the vector
subspace is again $\{0\}$; the only nonzero annihilator anywhere is the whole space, at the single
origin.

## Summary

The annihilator of an element in a product is the set of partners the element kills, the left and
the right annihilator being the kernels of the left and the right multiplication. The quaternion
multiplication is the associative product of the quaternion algebra $\mathbb{H}$, which over
$\mathbb{R}$ is a division algebra. Its operators $L_{\tilde q}$ and $R_{\tilde q}$ have trace
$4q_t$ and determinant $\langle\tilde q\rangle_{\natural}^2=(q_t^2+|\vec q|^2)^2$, and characteristic polynomial
$(t^2-2q_tt+\langle\tilde q\rangle_{\natural})^2$. The annihilator of every nonzero element is $\{0\}$ on both sides, and
the two sides coincide trivially; the annihilator of the origin is the whole space. The dichotomy
is therefore the split of the space into the origin and its complement, with no intermediate case
and no rank drop, because the zero-divisor cone of the complexified block meets the real space only
at the origin. On the remarkable subspaces, the centre $\mathbb{R}e_t$ and the vector subspace, the
annihilator of a nonzero element is again $\{0\}$, a nonzero central element being an invertible
scalar. The zero divisors are the empty set, read in *Zero Divisors of the Quaternion Algebra*, above this article in this category, and this article is short because there is nothing beyond the division property for the annihilator to characterise.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde q_1\tilde q_2$ | the quaternion multiplication, the product of the quaternion algebra $\mathbb{H}$ |
| $A_\star(\tilde q_1)=\{\tilde q_2:\tilde q_1\tilde q_2=0\}$ | the left annihilator of $\tilde q_1$, the kernel of the left multiplication |
| $B_\star(\tilde q_1)=\{\tilde q_2:\tilde q_2\tilde q_1=0\}$ | the right annihilator of $\tilde q_1$, the kernel of the right multiplication |
| $L_{\tilde q},R_{\tilde q}$ | the left and the right multiplication operators, of determinant $\langle\tilde q\rangle_{\natural}^2$ and trace $4q_t$ |
| $\chi_{L_{\tilde q}}(t)=(t^2-2q_tt+\langle\tilde q\rangle_{\natural})^2$ | the characteristic polynomial of the operator |
| $\langle\tilde q\rangle_{\natural}=q_t^2+|\vec q|^2$ | the quaternion norm, positive definite over $\mathbb{R}$ |
| $A_\star(\tilde q)=B_\star(\tilde q)$ | the two sides coincide, being $\{0\}$ off the origin and $\mathbb{H}$ at the origin |

## Further Reading

- *Introduction to the Quaternion Algebra* (`articles_maths/introduction-to-the-quaternion-algebra.md`), for the product, its associativity and its table.
- *Norm and Invertibility in the Quaternion Algebra* (`articles_maths/norm-and-invertibility-in-the-quaternion-algebra.md`), for the norm and the division property that make every nonzero element a unit.
- *One-Sided Operators on the Quaternion Algebra* (`articles_maths/one-sided-operators-on-the-quaternion-algebra.md`), for the operators $L_{\tilde q}$ and $R_{\tilde q}$ and their invertibility.
- *Association and the Transpose on the Quaternion Algebra* (`articles_maths/association-and-the-transpose-on-the-quaternion-algebra.md`), for the transpose $F^{\sim}=DF^{\mathsf T}D$ of the plain form, under which the right multiplication is the transpose of the left.
- *Annihilators of the Biquaternion Algebra* (`articles_maths/annihilators-of-the-biquaternion-algebra.md`), the complexified counterpart in the biquaternion chapter, where the cone is a hypersurface and the annihilator of a nonzero cone element is a pair of planes.
- *The Specificities of the Quaternion Algebra* (`articles_maths/the-specificities-of-the-quaternion-algebra.md`), for why the empty classes of the block are folded into a single article.
