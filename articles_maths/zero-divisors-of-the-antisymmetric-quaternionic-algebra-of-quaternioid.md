# __Zero Divisors of the Antisymmetric Quaternionic Algebra__

## Introduction

The antisymmetric quaternionic algebra of $\mathbb{H}$ carries the operation
$\tilde p\diamond\tilde q=\tfrac12(\tilde p^{\natural}\tilde q-\tilde q^{\natural}\tilde p)=p_0\vec q-q_0\vec p-\vec p\times\vec q$
of *Introduction to the Antisymmetric Quaternionic Algebra of Quaternions*. The parent quaternionic
product has no zero divisor, the ambient algebra $\mathbb{H}$ being a division algebra; the
antisymmetric block is at the opposite extreme. This article determines its zero divisors: the
criterion, the annihilator, the rank of the multiplication,

**This is not the algebra $\mathbb{H}$.** The two share the space, the addition and the real
scalars, but $\diamond$ is a different multiplication, alternating and without a unit. Throughout,
the natural sign ${}^{\natural}$ is the quaternion conjugation, the bar is the identity because
$\mathbb{R}$ has no nontrivial involution, and the star coincides with the natural sign and gives
nothing new. The symbol $\diamond$ is reserved for this block.

The product and its table are *Introduction to the Antisymmetric Quaternionic Algebra of
Quaternions*; the left multiplication operator is read in *The Adjoint Operators of the
Antisymmetric Quaternionic Algebra*, below this article in this category; the comparison with the
parent's divisor theory is

**Conventions.** The algebra is $\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$ and
$e_1^2=e_2^2=e_3^2=-e_0$. A generic element is $\tilde q=q_0e_0+\vec q$ with
$\vec q=\sum_{k=1}^{3}q_ke_k$ and $q_\mu\in\mathbb{R}$; $\vec p\cdot\vec q$ is the
Euclidean dot product, $\vec p\times\vec q$ the vector product, the **centre** is
$\mathbb{R}_{\mathbb{H}}=\mathbb{R}e_0$ and the **vector subspace** is
$\mathrm{Vect}(\mathbb{H})=\{\vec q\}$; the **quaternion form** is
$N(\tilde p,\tilde q)=p_0q_0+\vec p\cdot\vec q$.

## The Notion and the Product

**Definition.** A nonzero element $\tilde p$ is a **zero divisor** of the block when there is a
nonzero element $\tilde q$ with

$$
\tilde p\diamond\tilde q=0 .
$$

Because the operation is alternating, $\tilde p\diamond\tilde p=0$ for every $\tilde p$; hence
**every nonzero element is a zero divisor, with itself as partner on both sides**, and the
zero-divisor set is the punctured space $\mathbb{H}\setminus\{0\}$.

**Theorem (the zero-divisor set is total).** The set of zero-divisor elements is
$\mathbb{H}\setminus\{0\}$, of real dimension four. The block is the opposite of the parent
quaternionic product, whose only zero divisor is $0$, and agrees with its plain companion, the
cross product.

*Proof.* For every $\tilde p\neq0$ the relation $\tilde p\diamond\tilde p=0$ exhibits the partner
$\tilde q=\tilde p$; no nonzero element is excluded.

## The Criterion

**Theorem (the criterion).** For nonzero $\tilde p,\tilde q$,

$$
\tilde p\diamond\tilde q=0\iff p_0\vec q=q_0\vec p+\vec p\times\vec q
\iff \tilde q\ \text{is a multiple of}\ \tilde p,\ \tilde q=\lambda\tilde p .
$$

For a nonzero element the annihilating partners are exactly the multiples of the element.

*Proof.* The equation
$\tilde p\diamond\tilde q=p_0\vec q-q_0\vec p-\vec p\times\vec q=0$ is the displayed
criterion. Let $\vec q=\alpha\vec p+\vec q_\perp$ with $\vec q_\perp\perp\vec p$;
the criterion splits into the parallel part $(p_0\alpha-q_0)\vec p=0$ and the perpendicular part
$p_0\vec q_\perp=\vec p\times\vec q_\perp$. The first gives $\alpha=q_0/p_0$ when
$p_0\neq0$; the second is $p_0\vec q_\perp=|\vec p|R(\vec q_\perp)$ with $R$ a quarter
turn of the plane orthogonal to $\vec p$, so that
$(p_0/|\vec p|)\vec q_\perp=R(\vec q_\perp)$ would make the real number $p_0/|\vec p|$
an eigenvalue of $R$, and a quarter turn has no real eigenvalue; hence $\vec q_\perp=0$, so
$\vec q=\alpha\vec p$ and $\tilde q=\lambda\tilde p$. For a pure $\tilde p$ the parallel part
gives $q_0=0$ and the perpendicular part $\vec p\times\vec q=0$, so again
$\tilde q=\lambda\tilde p$, then pure. The direct verification by the rank of the multiplication
operator is below.

### The Parallel and the Perpendicular Parts

**Remark (why no perpendicular partner).** The criterion couples the scalar direction and the
vector part. The cross product contributes the perpendicular component alone, and the scalar part
times the perpendicular part is compared with a quarter turn of it, a rotation of the plane
orthogonal to $\vec p$; a quarter turn has no real eigenvector, so the perpendicular component
of the partner is **forced to vanish**. Only the parallel component survives, and it fixes the
ratio of the scalar parts. The partners are therefore the parallel pairs, and the perpendicular
pairs are exactly the pairs that are **not** partners.

## The Annihilator and the Rank

The annihilator of an element is the kernel of the left multiplication, the two sides coinciding
because the block is alternating, and it is the line $\mathbb{R}\tilde p$ for a nonzero element.
The annihilator, the operator with its characteristic polynomial, the rank table and the contrast
with the cross product are the companion article *Annihilators of the Antisymmetric Quaternionic
Algebra*, below this article in this category.

## The Families and the Dimension Count

**Theorem (the families).** The zero-divisor pairs $(\tilde p,\tilde q)$ with
$\tilde p,\tilde q\neq0$ and $\tilde p\diamond\tilde q=0$ form two families:

$$
\text{(i) the pure pairs: } \tilde p=\vec u,\ \tilde q=\lambda\vec u\ \text{with}\ \vec u\neq0,\ \lambda\neq0 ;
\qquad
\text{(ii) the non-pure pairs: } \tilde q=\lambda\tilde p\ \text{with}\ \tilde p\ \text{non-pure},\ \lambda\neq0 .
$$

No pair mixes a pure and a non-pure element.

*Proof.* By the criterion $\tilde q=\lambda\tilde p$. If $\tilde p$ is pure, $\tilde q$ is pure; if
$\tilde p$ is non-pure, $\tilde q$ is non-pure for $\lambda\neq0$. The two families meet at no
pair, the pure and the non-pure being exclusive.

**Proposition (the dimension count).** The zero-divisor set has real dimension four; the set of
zero-divisor pairs has real dimension five; and the annihilator of a nonzero element is a line, of
real dimension one.

*Proof.* The zero-divisor set is $\mathbb{H}\setminus\{0\}$, of dimension four. A pair is an
element $\tilde p\neq0$, four parameters, together with its partner $\lambda\tilde p$, one
parameter, giving a five-dimensional family; the second argument is not free, the annihilator being
a line.

## Summary

The antisymmetrised quaternionic block has no nontrivial divisor theory: the operation is
alternating, so every nonzero element is a zero divisor with itself as partner and the zero-divisor
set is the punctured four-dimensional space. The criterion for a pair is
$p_0\vec q=q_0\vec p+\vec p\times\vec q$, which forces the partner to be a **multiple
of the element**, $\tilde q=\lambda\tilde p$: the perpendicular component is killed by the
quarter-turn comparison of the scalar and cross terms, and the annihilator is the **line**
$\mathbb{R}\tilde p$ for a nonzero element, cutting the multiplication operator down to rank three,
with trace $3p_0$, vanishing determinant and characteristic polynomial
$t(t-p_0)\bigl((t-p_0)^2+|\vec p|^2\bigr)$. The zero-divisor pairs split into the pure parallel
pairs and the non-pure proportional pairs, of real dimension five. Over $\mathbb{C}$ the same
criterion holds and the annihilator widens on the isotropic cone of the central square; over
$\mathbb{R}$ the cone is empty and the annihilator is always the line.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde p\diamond\tilde q=0$, $\tilde p,\tilde q\neq0$ | a zero-divisor pair |
| $\mathbb{H}\setminus\{0\}$ | the zero-divisor set, total |
| $p_0\vec q=q_0\vec p+\vec p\times\vec q$ | the criterion |
| $\tilde q=\lambda\tilde p$ | the partner, a multiple of the element |
| $\operatorname{Ann}(\tilde p)=\mathbb{R}\tilde p$ | the annihilator, a line |
| $\operatorname{Tr}L^{\diamond}_{\tilde p}=3p_0$, $\det=0$, rank $3$ | the invariants of the operator |
| $t(t-p_0)\bigl((t-p_0)^2+\lvert\vec p\rvert^2\bigr)$ | the characteristic polynomial |

## Further Reading

- *Introduction to the Antisymmetric Quaternionic Algebra of Quaternions*, for the product, its alternation and the basis table.
- *The Adjoint Operators of the Antisymmetric Quaternionic Algebra*, below this article in this category, for the left multiplication operator and its invariants.
- *Zero Divisors of the Antisymmetric Plain Algebra*, above this article in this category, for the companion block whose annihilator is a plane.
- *Zero Divisors of the General Quaternionic Algebra*, for the parent product's divisor theory, which is trivial.
- *The Specificities of the Antisymmetric Quaternionic Algebra*, below this article in this category, for the total zero-divisor set among the criteria of the block.
- *Annihilators of the Antisymmetric Quaternionic Algebra* (`articles_maths/annihilators-of-the-antisymmetric-quaternionic-algebra-of-quaternioid.md`), below this article in this category, the companion article, for the annihilator of an element, the operator with its characteristic polynomial and the rank table.
