# __Zero Divisors of the Antisymmetric Plain Sesqualgebra__

## Introduction

A zero divisor is an element that annihilates a nonzero element, and it is defined by a product. This article determines the zero divisors of the antisymmetric plain sesqualgebra $\mathrm{APS}$,

$$
\tilde P\diamond\tilde Q=\operatorname{Vect}\bigl(\tilde P\tilde Q^{*}\bigr)=-P_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{P}-\mathbf{P}\times\overline{\mathbf{Q}},
$$

the antisymmetric half of the general plain sesquilinear product of *Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions*.

The answer is extreme and it is the point of the article. **Every nonzero element of the block is a zero divisor, on both sides.** The set of the zero divisors of the block is therefore the whole space with the origin removed, and the block is separated from the four general products of the space, whose four zero-divisor sets coincide in the cone $\{c(\tilde Q)=0\}\setminus\{0\}$ of the central square. The block's set is strictly larger, and the enlargement is not a computation left undone but a theorem: the product is the projection of the parent onto the vector subspace, and the projection has a kernel.

The annihilators repay the uniformity of the set. Each nonzero element annihilates a **complex line** of elements, with one exception: the elements that are zero divisors of the plain product annihilate a **complex plane**. So the block distinguishes its elements even though it declares them all zero divisors, and the distinction is the invertibility of the parent.

The zero divisors are defined by a product, and the definition is stated once in *Definitions for the Study of the 12 Algebraic Structures*, §*The Zero Divisor and the Annihilator*; throughout this article the product is $\diamond$ and, unqualified, **zero divisor** means zero divisor of $\diamond$. The plain product's cone, its two families and its criterion $c(\tilde Q)=0$ are *Zero Divisors of the General Plain Algebra*; the four general products' common set is *The Zero Divisors and the Twelve Structures*; the annihilators of one element in the four general products are *The Annihilating Elements of the Twelve Structures*. The classes that the zero divisors of the block are not are its idempotents, *Idempotents of the Antisymmetric Plain Sesqualgebra*, and its nilpotents, *Nilpotents of the Antisymmetric Plain Sesqualgebra*; the square-zero elements and the quadric of the diagonal are *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0=1,e_1,e_2,e_3$, $e_1e_2=e_3$, central scalar imaginary $i$ and coefficients in $\mathbb{C}$; an element is $\tilde Q=Q_0e_0+\mathbf{Q}$, with $\mathbf{Q}=\sum_{k=1}^{3}Q_ke_k$, and $(\mathbf P,\mathbf Q)=\sum_kP_kQ_k$ is the complex bilinear dot product of the vector parts. The conjugations are ${}^{\natural}$, the coefficientwise $\bar{\cdot}$ and the star ${}^{*}=\bar{\cdot}\circ{}^{\natural}$; the plain product is written $\tilde P\tilde Q$ and the parent sesquilinear product $\tilde P\tilde Q^{*}$. The projection $\operatorname{Vect}$ removes the scalar part, its kernel is the centre $\mathbb{C}_{\mathbb{B}}$, and its image is the vector subspace $\operatorname{Vect}(\mathbb{B})$. The central square of the plain product is $c(\tilde Q)e_0=\tilde Q\tilde Q^{\natural}$ with $c(\tilde Q)=\sum_\mu Q_\mu^{2}$, and the element $\tilde Q$ is invertible in the plain product exactly when $c(\tilde Q)\neq0$.

## The Definition

**Definition (zero divisor, annihilator).** Let $\star$ be a product on $\mathbb{B}$ and let $\tilde Q\in\mathbb{B}$. The element $\tilde Q$ is a **left zero divisor of $\star$** when $\tilde Q\neq0$ and there is a nonzero $\tilde R$ with $\tilde Q\star\tilde R=0$; a **right zero divisor of $\star$** when $\tilde Q\neq0$ and there is a nonzero $\tilde R$ with $\tilde R\star\tilde Q=0$; and a **zero divisor of $\star$** when it is one or the other. It is a **two-sided zero divisor** when it is both. The **left** and the **right annihilator** of a zero divisor $\tilde Q$ are

$$
A_\star(\tilde Q)=\{\tilde X:\tilde Q\star\tilde X=0\},\qquad
B_\star(\tilde Q)=\{\tilde X:\tilde X\star\tilde Q=0\},
$$

the kernels of the two one-sided multiplications. The origin is **not** a zero divisor of any product, though $0\star\tilde X=0$ for every $\tilde X$, and both elements of an annihilating pair are required to be nonzero.

The definition is the equation, and for the block the equation is

$$
\tilde Q\diamond\tilde R=0
\qquad\text{or}\qquad
\tilde R\diamond\tilde Q=0 .
$$

Both are statements about the product $\diamond$, and, unqualified in this article, **zero divisor** means a zero divisor of $\diamond$ and **annihilator** means an annihilator in $\diamond$. The zero-divisor sets of the other products are named with their product throughout.

## The Equations of the Block

### The Block Equation in Coordinates

Since the block is the projection of the parent sesquilinear product, its left zero-divisor equation unfolds in one step.

**Proposition (the equation).** For $\tilde Q,\tilde R\in\mathbb{B}$,

$$
\tilde Q\diamond\tilde R=0
\iff
\tilde Q\tilde R^{*}\in\mathbb{C}_{\mathbb{B}}
\iff
\operatorname{Vect}\bigl(\tilde Q\tilde R^{*}\bigr)=0 ,
$$

and dually $\tilde R\diamond\tilde Q=0$ if and only if $\tilde R\tilde Q^{*}$ is central.

*Proof.* By definition $\tilde Q\diamond\tilde R=\operatorname{Vect}(\tilde Q\tilde R^{*})$, and the kernel of the projection $\operatorname{Vect}$ is the centre $\mathbb{C}_{\mathbb{B}}$. The dual statement is the same identity with the two arguments exchanged.

The equation is therefore not the vanishing of a product, as it is for the plain algebra, but the **membership of a product in the centre**: the block annihilates $\tilde R$ on the left exactly when $\tilde Q\tilde R^{*}$ is a central element, that is exactly when the plain product $\tilde Q\tilde R^{*}$ has vanishing vector part. The parent product need not vanish for the block to: the centrality is enough, and the partner of an element invertible in the plain product achieves $\tilde Q\tilde R^{*}=e_0$, so the equation comes from the projection and not from the vanishing of the product.

### The Annihilators

**Proposition (the left annihilator).** For a nonzero $\tilde Q$ the left annihilator is the star of the set of the $\tilde Z$ with $\tilde Q\tilde Z$ central,

$$
A_\diamond(\tilde Q)=\bigl\{\tilde Z^{*}:\tilde Q\tilde Z\in\mathbb{C}_{\mathbb{B}}\bigr\},
$$

a complex subspace; it is a **complex line** when $\tilde Q$ is invertible in the plain product and a **complex plane** when it is not.

*Proof.* The element $\tilde R$ lies in $A_\diamond(\tilde Q)$ exactly when $\tilde Q\tilde R^{*}$ is central, that is exactly when $\tilde R^{*}$ satisfies $\tilde Q(\tilde R^{*})\in\mathbb{C}_{\mathbb{B}}$; the star is a bijection, so the annihilator is the star of the stated set and is a complex subspace. If $\tilde Q$ is invertible in the plain product, the equation $\tilde Q\tilde Z=\lambda e_0$ has the single solution line $\tilde Z\in\mathbb{C}\tilde Q^{-1}$, so the set is a complex line. If $\tilde Q$ is not invertible, it is a plain zero divisor, and $\mathbb{B}\tilde Q$ is a minimal left ideal of complex dimension two, which contains no nonzero central element because $e_0$ generates $\mathbb{B}$; hence $\tilde Q\tilde Z$ is central exactly when $\tilde Q\tilde Z=0$, that is exactly when $\tilde Z$ lies in the kernel of the plain left multiplication by $\tilde Q$, of complex dimension two.

**Corollary (the right annihilator).** By the conjugate-alternation $\tilde R\diamond\tilde Q=-\overline{\tilde Q\diamond\tilde R}$, the right annihilator equals the left one, $B_\diamond(\tilde Q)=A_\diamond(\tilde Q)$: the two sets of the definition coincide, and an element annihilates a given one on the right exactly when it annihilates it on the left. The block has one annihilator per element and not two, and its dimension is the line-or-plane of the proposition.

The annihilator therefore measures the parent invertibility: the block's zero divisors all exist, but the ones that are invertible in the plain product annihilate only a line, and those that are not annihilate a plane.

## The Criterion

For the plain product the zero divisors are selected by the single condition $c(\tilde Q)=0$, and the criterion is a statement of that product (*Zero Divisors of the General Plain Algebra*). The block has a criterion too, and it is empty.

**Theorem (the criterion of the block).** A nonzero element $\tilde Q$ is a zero divisor of the block if and only if $\tilde Q\neq0$. Equivalently, the zero-divisor set of the block is

$$
\mathcal{Z}_\diamond=\mathbb{B}\setminus\{0\},
$$

and every element of it is a two-sided zero divisor.

*Proof.* Let $\tilde Q\neq0$. If $\tilde Q$ is invertible in the plain product, the element $\tilde R=(\tilde Q^{-1})^{*}$ is nonzero and $\tilde R^{*}=\tilde Q^{-1}$, so $\tilde Q\tilde R^{*}=e_0$ is central and $\tilde Q\diamond\tilde R=0$. If $\tilde Q$ is not invertible in the plain product, it is a plain zero divisor, so there is a nonzero $\tilde Z$ with $\tilde Q\tilde Z=0$; the element $\tilde R=\tilde Z^{*}$ is nonzero and $\tilde Q\tilde R^{*}=\tilde Q\tilde Z=0$ is central, so $\tilde Q\diamond\tilde R=0$. In both cases $\tilde Q$ is a left zero divisor. Conjugate-alternation gives $\tilde R\diamond\tilde Q=-\overline{\tilde Q\diamond\tilde R}=0$ with the same nonzero $\tilde R$, so $\tilde Q$ is a right zero divisor as well, and the two-sided statement follows. The origin is excluded by the definition, and no other element exists.

**Remark (the two reasons).** The set is full for two independent reasons, and each alone would not fill it. The first is the **projection**: the block's value is a value, so the equation $\tilde Q\diamond\tilde R=0$ is the membership $\tilde Q\tilde R^{*}\in\mathbb{C}_{\mathbb{B}}$, and every element of the space can be sent into the centre by the plain product. The second is the **lack of a unit**: there is no element at which to test invertibility, so the barrier that in the plain algebra separates the invertible elements from the zero divisors is absent. The plain cone is thin because the plain product can be noncentral for every partner; the block's set is full because the projection discards the central part of any product at all.

## The Zero Divisor Set

### The Set and the Elementary Properties

The set $\mathcal{Z}_\diamond=\mathbb{B}\setminus\{0\}$ is stable under every nonzero complex scaling, because the equation is linear in the value and the projection is $\mathbb{C}$-linear: if $\tilde Q\diamond\tilde R=0$ then $(\alpha\tilde Q)\diamond\tilde R=\alpha(\tilde Q\diamond\tilde R)=0$. It is stable under the star and under the natural conjugation: each is a bijection of the space fixing the origin, and the star of a value is the value of the reversed pair, $(\tilde Q\diamond\tilde R)^{*}=\tilde R\diamond\tilde Q$, so a vanishing pair is carried to a vanishing pair. It is not the complement of a computed set: the block has no invertible elements to remove.

**Remark (the difference from the plain algebra is the point).** For the plain product the zero-divisor set is a complex hypersurface of $\mathbb{C}^{4}$, the cone $c(\tilde Q)=0$ with the origin removed; it has complex dimension three, and the elements outside it are invertible. For the block the set is the complement of the single point, of complex dimension four, and there is nothing outside it. The move is from a hypersurface to the complement of a point, and the reason is the move from an associative unital product to a projected non-unital one.

### The Contrast with the Four General Products

The four general products of the space have **four different definitions and one common set**, and the agreement is a theorem.

**Theorem (the four sets coincide; cited).** For the four general products $\tilde P\tilde Q$, $\tilde P^{\natural}\tilde Q$, $\tilde P\tilde Q^{*}$ and $\tilde P^{\natural}\tilde Q^{*}$ the zero-divisor set is the same, the cone

$$
\{\tilde Q\neq0:\ c(\tilde Q)=0\},\qquad c(\tilde Q)=\sum_{\mu=0}^{3}Q_\mu^{2}.
$$

This is *The Zero Divisors and the Twelve Structures*, §*The Four Zero-Divisor Sets Coincide*, and it is not restated here.

The block is not one of the four general products, and its set does not coincide with theirs: the cone $\{c=0\}\setminus\{0\}$ is a proper subset of $\mathbb{B}\setminus\{0\}$, since the element $e_0$ has $c(e_0)=1\neq0$ and yet is a zero divisor of the block, $e_0\diamond e_0=0$. **The enlargement is exactly the complement of the cone**, and it is the contribution of the projection. The contrast is the expected one for a sesquilinear block: the parent product is not unital, and the projection removes the central part, so the barrier of the criterion cannot survive.

## The Zero Divisors and the Other Classes

The block is not a unital product, and the vocabulary that the plain algebra builds on its zero divisors does not transfer. The two families of the plain zero divisors, the pure nilpotents and the complex multiples of the idempotents, organise the **plain** cone by the scalar part of the element; in the block the set is everything, and the operant distinction is not the scalar part but the parent invertibility, which separates the elements whose annihilator is a line from those whose annihilator is a plane.

**Remark (the other classes).** The block has one idempotent, the origin (*Idempotents of the Antisymmetric Plain Sesqualgebra*), and its nilpotents form a proper subcone of the zero-divisor set, the square-zero elements (*Nilpotents of the Antisymmetric Plain Sesqualgebra*); in the plain algebra the zero divisors are the union of the nilpotents and the idempotent multiples, so that a zero divisor is one of the two by construction, while here every element is a zero divisor and almost none is a nilpotent. **The inclusion of an element class in the zero-divisor set carries no information in the block**, and the article records that as the sharpest difference from the algebra.

**Remark (the remarkable subspaces).** Every nonzero element of every remarkable subspace is a zero divisor of the block, the centre included. In the plain algebra the centre contains no zero divisor and the quaternion subspaces contain none; here the centre is annihilated by the block as a whole, since $e_0\diamond e_0=0$. The reading of the classes on the remarkable subspaces is *Remarkable Subspaces under the Antisymmetric Plain Sesqualgebra of Biquaternions*.

## Summary

The zero divisors of the block are defined by the equation $\tilde Q\diamond\tilde R=0$, which unfolds as the membership $\tilde Q\tilde R^{*}\in\mathbb{C}_{\mathbb{B}}$ of a plain product in the centre. The set is **the whole space with the origin removed**, $\mathcal{Z}_\diamond=\mathbb{B}\setminus\{0\}$: every nonzero element is a left and a right zero divisor. The proof separates the two cases of the parent product, the invertible elements, whose partner is $(\tilde Q^{-1})^{*}$, and the non-invertible ones, whose partner is the star of a plain annihilator, and conjugate-alternation turns the left statement into the right one.

The annihilators are a complex line for every element that is invertible in the plain product and a complex plane for every element that is not, and the right annihilator equals the left one, by conjugate-alternation. The set is a complex cone of complex dimension four, the origin removed, against the complex dimension three of the plain cone.

The four general products of the space share the cone $\{c=0\}\setminus\{0\}$ as their zero-divisor set, a theorem of *The Zero Divisors and the Twelve Structures*; the block's set is strictly larger, and the enlargement is exactly the complement of that cone. The zero divisors of the block carry no information about the other classes: the unique idempotent is the origin and the nilpotents are a proper subcone, so an element is a zero divisor unconditionally and a nilpotent only rarely.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\diamond$ | the product of the block, $\tilde P\diamond\tilde Q=\operatorname{Vect}(\tilde P\tilde Q^{*})$ |
| $\tilde Q\diamond\tilde R=0$ | the zero-divisor equation of the block, equivalent to $\tilde Q\tilde R^{*}\in\mathbb{C}_{\mathbb{B}}$ |
| $A_\diamond(\tilde Q)$, $B_\diamond(\tilde Q)$ | the left and the right annihilator, the kernels of the two one-sided multiplications |
| $\mathcal{Z}_\diamond=\mathbb{B}\setminus\{0\}$ | the zero-divisor set of the block, the whole space without the origin |
| $c(\tilde Q)=\sum_\mu Q_\mu^{2}$ | the central square of the plain product, whose vanishing selects the plain zero divisors |
| $(\tilde Q^{-1})^{*}$ | the annihilating partner of an element invertible in the plain product |
| $\operatorname{Vect}$, $\mathbb{C}_{\mathbb{B}}$ | the projection and its kernel, the centre |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), §*The Zero Divisor and the Annihilator*, for the definition and the annihilator.
- *Zero Divisors of the General Plain Algebra* (`articles_maths/zero-divisors-of-the-general-plain-algebra.md`), for the plain cone, its two families and the criterion $c(\tilde Q)=0$.
- *The Zero Divisors and the Twelve Structures* (`articles_maths/the-zero-divisors-and-the-twelve-structures.md`), for the coincidence of the four sets and the one-sided inverse equations.
- *The Annihilating Elements of the Twelve Structures* (`articles_maths/the-annihilating-elements-of-the-twelve-structures.md`), for the annihilators in the four general products.
- *Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-plain-sesqualgebra-of-biquaternions.md`), for the product, its projection and its image.
