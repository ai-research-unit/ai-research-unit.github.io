# __Annihilators of the General Quaternionic Algebra__

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
the annihilator is the kernel of that operator, so it is a real subspace of the four-dimensional
space $\mathbb{H}$.

The block of this article is the **general quaternionic multiplication**
$$
\tilde p\star\tilde q=\tilde p^{\natural}\tilde q
=\bigl[p_0q_t+\vec p\cdot\vec q\bigr]e_t+p_0\vec q-q_t\vec p-\vec p\times\vec q,
$$
the product of the conjugate of the first factor with the second, read over $\mathbb{R}$
(*Introduction to the General Quaternionic Algebra of Quaternions*). It is not associative, and it
has $e_t$ as a left unit only. But over $\mathbb{R}$ the quaternion algebra is a division algebra
and the norm $N(\tilde p)=\tilde p^{\natural}\tilde p=p_0^2+|\vec p|^2$ is a sum of four
squares, hence positive definite; since the norm is multiplicative,
$N(\tilde p\star\tilde q)=N(\tilde p)N(\tilde q)$, the product has **no zero divisors** at all
(*Norm and Invertibility*). The annihilator is the finer
reading of this fact, and over $\mathbb{R}$ its answer is the smallest possible away from the
origin.

The article is short, and it is short for one reason: the block has no zero divisors. There is no
*Zero Divisors* article for it, because there is no zero-divisor set to describe, and the
annihilator is read off the division property in a page. This is the element-level annihilator. It
is not the structure-level *Annihilators in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*, whose object is the annihilating set of an element that kills the
**whole** space for a fixed product, the radical; here the product is fixed and the element varies.

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

Throughout this article the product is the **general quaternionic multiplication** $\star$, and
unqualified, *annihilator* means the annihilator of $\star$. The left multiplication is the plain
left multiplication by the conjugate,
$$
L_{\tilde p}\tilde x=\tilde p\star\tilde x=\tilde p^{\natural}\tilde x,
$$
and the right multiplication is its conjugate,
$\tilde x\star\tilde p=(L_{\tilde p}\tilde x)^{\natural}=\tilde x^{\natural}\tilde p$. Beside
$L_{\tilde p}$ it is convenient to keep the plain right multiplication by the conjugate,
$$
R_{\tilde p}\tilde x=\tilde x\tilde p^{\natural},
$$
the mirror operator, of the same determinant and the same rank as $L_{\tilde p}$. The block is the
real member of the general quaternionic family; its complex sibling is *Annihilators of the General
Quaternionic Algebra*, where the same product has a zero-divisor cone and the annihilator is a
complex plane on it.

## The Two Annihilators Coincide

**Theorem (the coincidence).** For every $\tilde q\in\mathbb{H}$,
$$
B_\star(\tilde q)=A_\star(\tilde q).
$$

*Proof.* By the exchange law of the block,
$\tilde x\star\tilde q=(\tilde q\star\tilde x)^{\natural}$ (*Introduction to the General
Quaternionic Algebra of Quaternions*). The right multiplication is therefore the conjugate of the
left multiplication, and the conjugation is a bijection of $\mathbb{H}$ onto itself fixing $0$
alone, so $\tilde x\star\tilde q=0$ exactly when $\tilde q\star\tilde x=0$. Equivalently,
conjugating the equation $\tilde q^{\natural}\tilde x=0$ gives
$(\tilde q^{\natural}\tilde x)^{\natural}=\tilde x^{\natural}\tilde q=0$, because ${}^{\natural}$
is an anti-automorphism of order two. Hence the two annihilators contain exactly the same elements.

The coincidence is a property of the product, and it holds for the same reason as over
$\mathbb{C}$: the conjugation is a real-linear anti-automorphism of order two, so the first factor
can be conjugated away without changing the annihilation. Over $\mathbb{R}$, however, the
coincidence is **vacuous**: both sides are $\{0\}$ for a nonzero element (next section), so they
agree because both are trivial. The substance of the block is not in the theorem but in the size of
the common set.

## The Annihilator Is Zero

**Theorem (the common annihilator).** Let $\tilde q\in\mathbb{H}$.

- If $\tilde q\neq0$ then $A_\star(\tilde q)=B_\star(\tilde q)=\{0\}$.
- If $\tilde q=0$ then $A_\star(\tilde q)=B_\star(\tilde q)=\mathbb{H}$.

In particular the block has no zero divisor: no nonzero element kills a nonzero partner.

*Proof.* By the multiplicativity and the definiteness of the norm, $\tilde q\star\tilde x=0$ gives
$N(\tilde q)N(\tilde x)=N(0)=0$, hence $N(\tilde q)=0$ or $N(\tilde x)=0$, that is $\tilde q=0$ or
$\tilde x=0$. So for $\tilde q\neq0$ the only solution of $\tilde q\star\tilde x=0$ is
$\tilde x=0$, and $A_\star(\tilde q)=\{0\}$; the right annihilator is the same by the coincidence,
or directly from $\tilde x\star\tilde q=0$. At $\tilde q=0$ the product vanishes for every
$\tilde x$ and both annihilators are the whole space.

**Corollary.** The zero-divisor set of the block is empty away from the origin, and the block
carries no *Zero Divisors* article. The emptiness is the definiteness of the norm, and not a
property of the general quaternionic shape: over $\mathbb{C}$ the same shape has a cone.

## The Multiplication Operator and the Rank

**Proposition (the operator and its determinant).** In the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ the operators
are the plain left and right multiplications by the conjugate $\tilde p^{\natural}$, of determinant
$$
\det L_{\tilde p}=N(\tilde p)^{2}=\bigl(p_0^2+|\vec p|^2\bigr)^{2},\qquad
\det R_{\tilde p}=N(\tilde p)^{2}.
$$

*Proof.* $L_{\tilde p}$ is the left multiplication of the plain algebra by the quaternion
$\tilde p^{\natural}$, whose determinant is the square of the plain norm,
$N(\tilde p^{\natural})^{2}$; the conjugation keeps the sum of four squares, so
$N(\tilde p^{\natural})=N(\tilde p)$. The right multiplication is the plain right multiplication by
the same conjugate, and the left and the right regular representations of the quaternion algebra
have the same determinant.

**Corollary (the rank and the annihilator).** For every $\tilde p$,

| $\tilde p$ | $\operatorname{rank}L_{\tilde p}$ | $\dim\ker L_{\tilde p}$ | $\ker L_{\tilde p}$ |
|---|---|---|---|
| $\neq0$ | $4$ | $0$ | $\{0\}$ |
| $0$ | $0$ | $4$ | $\mathbb{H}$ |

and the same table holds for $R_{\tilde p}$.

*Proof.* The determinant $N(\tilde p)^2$ is a strictly positive real for $\tilde p\neq0$ and
vanishes only at the origin. A $4\times4$ matrix with nonzero determinant has rank four and trivial
kernel; the zero operator at the origin has rank zero and kernel the whole space. The right side is
identical because $\det R_{\tilde p}$ is the same.

**Remark.** The determinant is a square and it is never negative, so over $\mathbb{R}$ it vanishes
at the origin alone. Over $\mathbb{C}$ the same determinant vanishes on the cone $N(\tilde p)=0$,
and there the rank drops to two. The real picture has no intermediate rank: it jumps from four to
zero.

## The Dichotomy

**Theorem (the dichotomy).** The annihilator of an element is $\{0\}$ at every nonzero element and
the whole space $\mathbb{H}$ at the origin alone. Equivalently, the rank of the multiplication
operator is four at every nonzero element and zero at the origin.

*Proof.* This is the rank table of the preceding section.

The dichotomy of the complex block has three rows — rank four off the cone, rank two on it, rank
zero at the origin — and the passage to $\mathbb{R}$ deletes the middle one. The deletion is the
division property: over $\mathbb{R}$ the norm is definite, so its only zero is the origin and the
cone of the complex block shrinks to the single point $\{0\}$. What remains over $\mathbb{R}$ is
the origin against everything else.

## The Annihilator on the Remarkable Subspaces

**The centre.** A nonzero central element $\tilde p=\lambda e_t$ has
$\tilde p^{\natural}=\lambda e_t$ and $L_{\lambda e_t}\tilde x=\lambda\tilde x$; the operator is
the scalar $\lambda$ times the identity, invertible for $\lambda\neq0$, so its annihilator is
$\{0\}$.

**The vector subspace.** A nonzero pure element $\tilde p=\vec p$ has
$N(\tilde p)=|\vec p|^2>0$ and $L_{\vec p}\tilde x=-\vec p\tilde x$, again invertible; its
annihilator is $\{0\}$.

**Proposition (the reading on the subspaces).** On the centre $\mathbb{R}e_t$ and on the vector
subspace $V$ the annihilator of every nonzero element is $\{0\}$; only the origin has the whole
space as annihilator.

*Proof.* Apart from the origin, the elements of the two subspaces have nonzero norm, and the
theorem on the common annihilator applies to each.

The isotropic directions that would enlarge an annihilator, and that the complex block carries on
its cone, do not exist over $\mathbb{R}$: the quaternionic form is definite, so neither subspace
has an isotropic element other than $0$ (*The Isotropic Structure of the General Quaternionic
Algebra*).

## Summary

The annihilator of an element in a product is the set of partners the element kills, the left and
the right annihilator being the kernels of the left and the right multiplication. The general
quaternionic multiplication $\tilde p\star\tilde x=\tilde p^{\natural}\tilde x$ carries the
conjugation, a real-linear anti-automorphism of order two, so its two annihilators of an element
always coincide, exactly as over $\mathbb{C}$. Over $\mathbb{R}$ they coincide **vacuously**: the
two operators are the multiplications by the conjugate $\tilde p^{\natural}$ in the division
algebra, of determinant $N(\tilde p)^2=(p_0^2+|\vec p|^2)^2$, invertible at every nonzero
$\tilde p$. The common annihilator is therefore $\{0\}$ at every nonzero element and the whole
space at the origin, and the dichotomy has these two rows and no more. The block has no zero
divisors and no *Zero Divisors* article, and its element-level annihilator is distinct from the
structure-level annihilating set of *Annihilators in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*, which fixes the product and reads the elements
that kill the whole space. The complex sibling, where the norm becomes isotropic, has a cone and a
plane on it; over $\mathbb{R}$ the division property leaves nothing.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde p\star\tilde q=\tilde p^{\natural}\tilde q$ | the general quaternionic multiplication, the operation $\mathrm{GQA}$ |
| $A_\star(\tilde p),B_\star(\tilde p)$ | the left and the right annihilator of $\tilde p$, equal by the anti-automorphism ${}^{\natural}$ |
| $L_{\tilde p}\tilde x=\tilde p^{\natural}\tilde x$ | the left multiplication, whose kernel is the annihilator |
| $R_{\tilde p}\tilde x=\tilde x\tilde p^{\natural}$ | the plain right multiplication by the conjugate, the mirror of $L_{\tilde p}$ |
| $\det L_{\tilde p}=N(\tilde p)^{2}$ | the determinant, $(p_0^2+|\vec p|^2)^2$, nonzero at every nonzero element |
| $\{0\}$ off the origin | the annihilator of a nonzero element |
| $\mathbb{H}$ at the origin | the annihilator of $0$ |
| $N(\tilde p)=p_0^2+|\vec p|^2$ | the definite norm, the source of the division property |

## Further Reading

- *Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-quaternioid-r-space.md`), §*The Element Vocabulary*, for the zero divisor, the annihilator and the regular element of a general product.
- *Introduction to the General Quaternionic Algebra* (`articles_maths/introduction-to-the-general-quaternionic-algebra-of-quaternioid.md`), for the product, its table and its conjugation.
- *Norm and Invertibility* (`articles_maths/norm-and-invertibility-in-the-general-quaternionic-algebra-of-quaternioid.md`), for the definite norm, its multiplicativity and the absence of zero divisors.
- *The Isotropic Structure of the General Quaternionic Algebra* (`articles_maths/the-isotropic-structure-of-the-general-quaternionic-algebra-of-quaternioid.md`), for the definiteness of the form and the emptiness of the isotropic structure.
- *One-Sided Operators on the General Quaternionic Algebra* (`articles_maths/one-sided-operators-on-the-general-quaternionic-algebra-of-quaternioid.md`), for the left and the right multiplications and their injectivity.
- *Annihilators in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/annihilators-in-the-algebraic-structures-over-the-quaternioid-r-space.md`), for the structure-level annihilating set over the whole space, which is $\{0\}$ for the general quaternionic product.
- *Annihilators of the General Quaternionic Algebra* (`articles_maths/annihilators-of-the-general-quaternionic-algebra.md`), the complex sibling, whose annihilator is a complex plane on the zero-divisor cone that the passage to $\mathbb{R}$ removes.
