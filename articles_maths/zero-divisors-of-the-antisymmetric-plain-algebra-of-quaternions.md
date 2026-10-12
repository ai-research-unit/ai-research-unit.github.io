# __Zero Divisors of the Antisymmetric Plain Algebra__

## Introduction

The antisymmetric plain algebra of $\mathbb{H}$ carries the cross product
$\tilde p\times\tilde q=\tfrac12(\tilde p\tilde q-\tilde q\tilde p)=\mathbf p\times\mathbf q$ of
*Introduction to the Antisymmetric Plain Algebra of Quaternions*. The plain algebra is a division
algebra, with no zero divisor; the antisymmetric block is at the opposite extreme. This article
determines its zero divisors: the criterion, the pairs that multiply to zero and the dimension
count.

**This is not the algebra $\mathbb{H}$.** The two share the space, the addition and the real
scalars, but $\times$ is a different multiplication, alternating and without a unit. Throughout,
the natural sign ${}^{\natural}$ is the quaternion conjugation, the bar is the identity because
$\mathbb{R}$ has no nontrivial involution, and the star coincides with the natural sign and gives
nothing new.

The product, its alternation and its table are *Introduction to the Antisymmetric Plain Algebra of
Quaternions*; the multiplication operators of the block are read in *The Adjoint Operators and the
Derivations of the Antisymmetric Plain Algebra* and its two matrix models, all below this article
in this category.

**Conventions.** The algebra is $\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$ and
$e_1^2=e_2^2=e_3^2=-e_0$. A generic element is $\tilde q=q_0e_0+\mathbf q$ with
$\mathbf q=\sum_{k=1}^{3}q_ke_k$ and $q_\mu\in\mathbb{R}$; $\mathbf p\cdot\mathbf q$ is the
Euclidean dot product and $\mathbf p\times\mathbf q$ the vector product of the vector parts; the
**centre** is $\mathbb{R}_{\mathbb{H}}=\mathbb{R}e_0$ and the **vector subspace** is
$\mathrm{Vect}(\mathbb{H})=\{\mathbf q\}$.

## The Notion and the Product

**Definition.** A nonzero element $\tilde p$ is a **zero divisor** of the block when there is a
nonzero element $\tilde q$ with

$$
\tilde p\times\tilde q=0 .
$$

Because the operation is alternating, $\tilde p\times\tilde p=0$ for every $\tilde p$; hence
**every nonzero element is a zero divisor, with itself as partner on both sides.** The left and the
right zero divisors coincide, and the block's zero-divisor set is total.

**Theorem (the zero-divisor set is total).** The set of zero-divisor elements is the punctured
space

$$
\mathbb{H}\setminus\{0\},
$$

the whole four-dimensional space with the origin removed. The block is the extreme opposite of the
plain one, whose only zero divisor is $0$.

*Proof.* For every $\tilde p$ the relation $\tilde p\times\tilde p=0$ exhibits a nonzero partner
$\tilde q=\tilde p$ when $\tilde p\neq0$. No nonzero element is excluded, and $0$ is excluded by
the definition.

## The Criterion

**Theorem (the criterion).** For nonzero $\tilde p,\tilde q$,

$$
\tilde p\times\tilde q=0\iff \mathbf p\times\mathbf q=0\iff \mathbf p\ \text{and}\ \mathbf q\ \text{are linearly dependent in}\ \mathbb{R}^3 .
$$

The dependence is the **parallelism of the vector parts**: the criterion reads
$\mathbf q=\lambda\mathbf p$, or $\mathbf p=\lambda\mathbf q$, for some real $\lambda$, the zero
vector being proportional to every vector.

*Proof.* The operation is the vector product of the vector parts, which vanishes exactly when the
two vectors are linearly dependent. Two nonzero vectors of $\mathbb{R}^3$ are linearly dependent
exactly when they are proportional.

**Remark (the criterion is blind to the scalars).** The scalar coordinates $p_0,q_0$ do not enter
the criterion at all: a pure and a non-pure element with the same vector part have the same
partners. This is the reason the collapse that the definiteness of the norm forces on the other
blocks does not occur here — the operation never reads a norm.

### The Annihilators

The annihilator of an element is the kernel of its left multiplication, the two sides coinciding
because the block is alternating; it is the plane $\mathbb{R}e_0\oplus\mathbb{R}\mathbf p$ for a
noncentral element and the whole space for a central one. The annihilators, the operator
$\operatorname{diag}(0,C_{\mathbf p})$ with its characteristic polynomial $t^2(t^2+|\mathbf p|^2)$,
the rank table and the dichotomy by the vector part are the companion article *Annihilators of the
Antisymmetric Plain Algebra*, below this article in this category.

## The Pairs That Multiply to Zero

### The Families

**Theorem.** The zero-divisor pairs $(\tilde p,\tilde q)$ with $\tilde p,\tilde q\neq0$ and
$\tilde p\times\tilde q=0$ form two disjoint families:

$$
\text{(i) the pure pairs: } \tilde p=\mathbf u,\ \tilde q=\mathbf v
\ \text{with}\ \mathbf u,\mathbf v\neq0\ \text{and parallel};
\qquad
\text{(ii) the pairs with a scalar part: } \tilde p\ \text{or}\ \tilde q\ \text{non-pure},
$$

the vector parts being parallel in the second family too, or one of them zero.

*Proof.* By the criterion the vector parts are parallel. Two pure elements with nonzero vector
parts give the first family; a non-pure element gives the second, its partner having a parallel
vector part by the criterion. If one vector part is zero the corresponding element is the pure
scalar $\lambda e_0$ with $\lambda\neq0$, a case of the second family with the partner free; if
both vector parts are nonzero and parallel, the pair is in the first family exactly when both
elements are pure. The two families are disjoint and cover every pair.

**Remark (the two families and the annihilator).** For a noncentral element the annihilator is the
plane $\mathbb{R}e_0\oplus\mathbb{R}\mathbf p$: its vector line $\mathbb{R}\mathbf p$ carries the
pure partners and the rest of the plane the non-pure ones, so the pure pairs are the vector-line
stratum and the pairs with a scalar part the complementary stratum. For a central element the
annihilator is the whole space and the partner is arbitrary.

### The Dimension Count

**Proposition.** The zero-divisor set has real dimension four. The zero-divisor pairs form a set of
real dimension six, and the annihilator of a noncentral element is a plane of real dimension two.

*Proof.* The zero-divisor set is $\mathbb{H}\setminus\{0\}$, of dimension four. For a pair, choose
the first element: if it is noncentral, four parameters, then the partner ranges over the
annihilator plane $\mathbb{R}e_0\oplus\mathbb{R}\mathbf p$, of dimension two, giving a family of
dimension six, which dominates the central stratum
$\{\lambda e_0\}\times(\mathbb{H}\setminus\{0\})$, of dimension five. So the pairs have dimension
six.

## Summary

The antisymmetric plain block has no nontrivial zero divisor theory to discover: the operation is
alternating, so $\tilde p\times\tilde p=0$ and every nonzero element is a zero divisor with itself
as partner, the zero-divisor set being the punctured four-dimensional space. The criterion for a
pair is the parallelism of the vector parts,
$\mathbf p\times\mathbf q=0\iff\mathbf q=\lambda\mathbf p$ or $\mathbf p=\lambda\mathbf q$, and the
annihilator of a noncentral element is the two-dimensional plane
$\mathbb{R}e_0\oplus\mathbb{R}\mathbf p$, of the left multiplication operator
$\operatorname{diag}(0,C_{\mathbf p})$, of vanishing trace and determinant and rank two off the
centre. The zero-divisor pairs form two families, the pure parallel pairs and the pairs with a
scalar part, of total real dimension six. Over $\mathbb{C}$ the criterion is identical and the only
difference is the possible degeneracy of the operator's quadratic factor on the isotropic cone.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde p\times\tilde q=0$, $\tilde p,\tilde q\neq0$ | a zero-divisor pair |
| $\mathbb{H}\setminus\{0\}$ | the zero-divisor set, total |
| $\mathbf p,\mathbf q$ proportional | the criterion |
| $\operatorname{Ann}(\tilde p)=\mathbb{R}e_0\oplus\mathbb{R}\mathbf p$ | the annihilator of a noncentral element |
| $L^{\times}_{\tilde p}=\operatorname{diag}(0,C_{\mathbf p})$ | the left multiplication operator |
| $t^2(t^2+\lvert\mathbf p\rvert^2)$ | its characteristic polynomial |
| rank $2$ / $0$ | on the noncentral elements / on the centre |

## Further Reading

- *Introduction to the Antisymmetric Plain Algebra of Quaternions*, for the product, its alternation and the basis table.
- *Annihilators of the Antisymmetric Plain Algebra* (`articles_maths/annihilators-of-the-antisymmetric-plain-algebra-of-quaternions.md`), below this article in this category, the companion article, for the annihilator of an element, the rank of the multiplication operator and the dichotomy by the vector part.
- *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra*, below this article in this category, for the operator and the adjoint representation.
- *The Lie Algebra of the Antisymmetric Plain Algebra*, below this article in this category, for the centre and the derived algebra.
- *The Specificities of the Antisymmetric Plain Algebra*, below this article in this category, for the total zero-divisor set as one of the criteria of the block.
- *Introduction to the General Plain Algebra of Quaternions*, for the division property of the plain algebra, the contrast of the block.
