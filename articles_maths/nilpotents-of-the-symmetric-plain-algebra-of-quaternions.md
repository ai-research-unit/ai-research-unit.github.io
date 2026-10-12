# __Nilpotents of the Symmetric Plain Algebra__

## Introduction

The symmetric plain algebra $\mathbb{H}^{\bullet}$ is the real space $\mathbb{H}$ under the Jordan product $\tilde p\bullet\tilde q=\tfrac12(\tilde p\tilde q+\tilde q\tilde p)$ of *Introduction to the Symmetric Plain Algebra of Quaternions*. This article determines the **nilpotents** of the block, the non-zero elements of square zero, and reads the separation between the nilpotents and the zero divisors.

The answer is the empty class. The nilpotents of the block are the nilpotents of the algebra: the two squares agree, so the equation $\tilde\Upsilon\bullet\tilde\Upsilon=0$ is the equation $\tilde\Upsilon^2=0$, and the plain product of $\mathbb{H}$ is a division rule, so the only element of square zero is the origin. **The block has no non-zero nilpotent and no element of nilpotency index two or more.** This is the whole of the nilpotent theory of the block, and the article's own subject is the contrast it draws: the block **has** zero divisors, a whole punctured vector subspace of them, and **none** of them is a nilpotent.

The separation is the point. A zero divisor is a non-zero element with a non-zero partner, and a nilpotent is a non-zero element whose own square vanishes; the two notions are distinct, and over $\mathbb{R}$ they are as far apart as the block allows: the zero-divisor set is the plane-filling family of the pure elements, while the nilpotent set is empty. The reason is the definiteness of the norm. A pure element has the negative scalar square $-|\mathbf{p}|^2e_0$, non-zero unless the element is the origin, so it is a zero divisor but never a square-zero element; a general element $\tilde p=p_0e_0+\mathbf{p}$ has the square $(p_0^2-|\mathbf{p}|^2)e_0+2p_0\mathbf{p}$, whose two parts cannot vanish together unless $\tilde p=0$. The complex block separates the two classes differently: its pure square is indefinite, its nilpotents form the pure isotropic cone, and its zero-divisor set is larger still. Over $\mathbb{R}$ the cone is the empty set.

A nilpotent is defined relative to a product, and the definition is stated once for a general product in *Definitions for the Study of the 6 Algebraic Structures*, §*The Element Vocabulary*; throughout this article the product is $\bullet$ and, unqualified, **nilpotent** means nilpotent of $\bullet$. The nilpotents of the plain product are read in *Introduction to the General Plain Algebra of Quaternions* and in *Nilpotents of the General Plain Algebra*, which owns that class, where the division property empties it; the associated zero divisors are *Zero Divisors of the Symmetric Plain Algebra*, above this article in this category, which already remarks that the block has no non-zero nilpotent although it has zero divisors; the roots of $0$ are *Square Roots of Minus One, Zero and Plus One in the Symmetric Plain Algebra*, above this article in this category, where $\Sigma_0=\{0\}$; the specific-theory reading is *The Specificities of the Symmetric Plain Algebra*, §*The Degenerate Classes*, below this article in this category; and the operator theory is *The Multiplication Operators of the Symmetric Plain Algebra*, below this article in this category.

**Conventions.** The algebra is $\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$ and $e_1e_2=e_3$, so that $e_k^2=-e_0$ and $e_je_k=-e_ke_j$ for $j\neq k$. An element is $\tilde q=q_0e_0+\mathbf q$ with $\mathbf q=\sum_{k=1}^{3}q_ke_k$ and $q_\mu\in\mathbb{R}$; $\mathbf p\cdot\mathbf q=\sum_kp_kq_k$ is the Euclidean dot product of the vector parts. The product with the mark is $\tilde p\bullet\tilde q=\tfrac12(\tilde p\tilde q+\tilde q\tilde p)$; the plain square is $\tilde q^2=(q_0^2-|\mathbf q|^2)e_0+2q_0\mathbf q$; the norm is $N(\tilde q)=\tilde q\tilde q^{\natural}=q_0^2+|\mathbf q|^2$. The natural sign ${}^{\natural}$ is the quaternion conjugation, the bar is the identity because $\mathbb{R}$ has no nontrivial involution, and the star coincides with the natural sign. The scalar line is $\mathbb{R}e_0$, which is the centre, and the vector subspace is $\mathrm{Vect}(\mathbb{H})=\operatorname{Im}\mathbb{H}$ (*Introduction to the Remarkable Subspaces of the Quaternions*). The left multiplication is $L^{\bullet}_{\tilde p}\tilde q=\tilde p\bullet\tilde q$.

## The Definition and the Criterion

**Definition (nilpotent of a product).** Let $\star$ be a product on $\mathbb{H}$; then $\tilde\Upsilon$ is a **nilpotent of $\star$**, or an element of **square zero**, when

$$
\tilde\Upsilon\neq0\qquad\text{and}\qquad\tilde\Upsilon\star\tilde\Upsilon=0 .
$$

The origin is a square-zero element of every product, and it is not a nilpotent.

Throughout this article the product is the symmetric plain product $\bullet$, and the equation is $\tilde\Upsilon\bullet\tilde\Upsilon=0$. It is the equation of the algebra, because the square of the block is the plain square; the criterion is therefore the criterion of the algebra.

**Theorem (the criterion).** An element of the block is a nilpotent of $\bullet$ only if it is non-zero with vanishing square, and no such element exists:

$$
\tilde\Upsilon\ \text{nilpotent of }\bullet\iff\tilde\Upsilon\neq0\ \text{and}\ \tilde\Upsilon^2=0\iff\text{never}.
$$

Equivalently, the square-zero elements of the block are exactly the origin:

$$
\tilde\Upsilon\bullet\tilde\Upsilon=0\iff\tilde\Upsilon=0 .
$$

*Proof.* Write $\tilde p=p_0e_0+\mathbf{p}$; the plain square is $\tilde p^2=(p_0^2-|\mathbf{p}|^2)e_0+2p_0\mathbf{p}$, and it vanishes exactly when $2p_0\mathbf{p}=0$ and $p_0^2-|\mathbf{p}|^2=0$. If $p_0\neq0$ the first equation gives $\mathbf{p}=0$, and then the second gives $p_0^2=0$, a contradiction with $p_0\neq0$; hence $p_0=0$, and the second then reads $-|\mathbf{p}|^2=0$, so $\mathbf{p}=0$ and $\tilde p=0$. **The only square-zero element is the origin, so there is no nilpotent.**

**Corollary (the empty class).** The nilpotent class of the block is empty and the square-zero class is the origin. The nilpotents of the block and the nilpotents of the plain algebra coincide, the two squares being the same and the plain product being a division rule.

## The Empty Nilpotent Cone

**Definition.** The **nilpotent cone** of a block is the set of its nilpotents. For the symmetric plain algebra of $\mathbb{H}$ it is empty:

$$
\mathcal{N}=\{\tilde\Upsilon\in\mathbb{H}:\ \tilde\Upsilon\neq0,\ \tilde\Upsilon\bullet\tilde\Upsilon=0\}=\varnothing .
$$

**Theorem (no cone).** The nilpotent cone of the block is empty.

*Proof.* By the criterion a square-zero element is the origin, and the origin is excluded from the cone by its definition; the cone, the set of non-zero square-zero elements, is therefore empty.

**Remark (why the cone is empty over $\mathbb{R}$).** The nilpotents of the block are the pure isotropic elements, the non-zero pure elements of vanishing square, because the product of two pure elements is the scalar $-\mathbf{u}\cdot\mathbf{v}$ (*Zero Divisors of the Symmetric Plain Algebra*, §*The Pairs That Multiply to Zero*, above this article in this category). Over $\mathbb{R}$ the square of a pure element is $\mathbf{u}\bullet\mathbf{u}=-|\mathbf{u}|^2e_0$, a **non-positive** scalar, and it vanishes only for $\mathbf{u}=0$: the isotropic cone of the Euclidean form is the origin. **The definiteness of the norm closes the cone to the origin**, and with it closes the nilpotent class. In the complex block the same square is indefinite: the nilpotents there are the pure isotropic cone, a complex quadric of complex dimension two, a four-real-parameter family whose projectivisation is a conic of real dimension two. Over $\mathbb{R}$ the quadric degenerates to the single point.

## The Separation from the Zero Divisors

The zero-divisor set of the block is the whole punctured vector subspace, and the nilpotent set is empty; the two are as far apart as a block with a division property allows, and the gap is elementary.

**Theorem (the separation).** The zero-divisor set of the block is the punctured vector subspace,

$$
\mathcal{Z}=\mathrm{Vect}(\mathbb{H})\setminus\{0\}=\{\mathbf{u}:\ \mathbf{u}\neq0\},
$$

of real dimension three, and the nilpotent set is empty. Every zero divisor is a pure element of non-vanishing square,

$$
\mathbf{u}\in\mathcal{Z}\quad\Longrightarrow\quad \mathbf{u}\bullet\mathbf{u}=-|\mathbf{u}|^2e_0\neq0,
$$

so no zero divisor is a square-zero element, and the two classes meet nowhere.

*Proof.* The criterion is that of *Zero Divisors of the Symmetric Plain Algebra*, above this article in this category: a non-zero element is a zero divisor exactly when it is pure. The square of a non-zero pure element is $-|\mathbf{u}|^2e_0$ with $|\mathbf{u}|^2>0$, so it is non-zero and the element is not square-zero. The intersection is empty, and its only candidate, the origin, is excluded by the definition of a zero divisor.

**Remark (the two subfamilies of the pure elements).** In the complex block the pure elements split by isotropy: the isotropic ones, those with $\mathbf{P}\cdot\mathbf{P}=0$, are the nilpotents, and the non-isotropic ones are the zero divisors that are not nilpotents. Over $\mathbb{R}$ the pure square is the definite form $-|\mathbf{p}|^2e_0$: the isotropic subfamily collapses to the origin, and the non-isotropic subfamily fills the whole punctured vector subspace. **The Euclidean definiteness empties the first subfamily and hands the whole zero-divisor set to the second**, which is why the block separates the two classes so sharply.

## The Nilpotency Index

**Proposition (no element of index two or more).** Every non-zero element of the block is invertible, and no non-zero element has a vanishing power:

$$
\tilde p\neq0\quad\Longrightarrow\quad \tilde p\ \text{is invertible and}\ \tilde p^{k}\neq0\ \text{for every}\ k\geq1 .
$$

In particular there is no element of nilpotency index two, three or more, and the nilpotent class is empty at every index.

*Proof.* The norm $N(\tilde p)=p_0^2+|\mathbf{p}|^2$ is a sum of squares, so it is positive for $\tilde p\neq0$ and the inverse $\tilde p^{-1}=\tilde p^{\natural}/N(\tilde p)$ exists (*Norm and Invertibility in the Symmetric Plain Algebra*, above this article in this category). An invertible element is not a zero divisor, so if $\tilde p^{k}=0$ with $\tilde p\neq0$ and $k\geq2$, then $\tilde p\bullet\tilde p^{k-1}=0$ forces $\tilde p^{k-1}=0$, and descending gives $\tilde p=0$, a contradiction. No power of a non-zero element vanishes.

**Remark (the block has no operator of a nilpotent).** In the complex block a square-zero element produces an operator of index three and the flag calculus that goes with it (*The Multiplication Operators of the Symmetric Plain Algebra*, below this article in this category). The block has no such element, so **there is no operator of a nilpotent and no flag to read**: the operator material of a square-zero element is vacuous here, and the only square-zero element is the origin, whose operator is the zero operator.

## The Relation to the Other Notions

**Nilpotents and the zero divisors.** The nilpotent class is empty and the zero-divisor set is the punctured vector subspace; they are disjoint, and the inclusion of the former in the latter is the inclusion of the empty set. In the complex block the nilpotent cone sits inside the zero-divisor set as a proper subset, the non-isotropic pure elements filling the difference; over $\mathbb{R}$ the difference is the whole set.

**Nilpotents and the idempotents.** A nilpotent would be a non-zero element of square zero, and an idempotent is an element equal to its own square. The two classes have the origin in common and nothing else, since the equations $\tilde p^2=0$ and $\tilde p^2=\tilde p$ together give $\tilde p=0$. The only element that is both square-zero and idempotent is the origin.

**Nilpotents and the roots.** The nilpotents are exactly the roots of $0$ outside the origin, and the block has none: the roots of $0$ are $\Sigma_0=\{0\}$ (*Square Roots of Minus One, Zero and Plus One in the Symmetric Plain Algebra*, §*The Roots of $0$*, above this article in this category), of which the origin is the square-zero element. The degeneracy of the general square-root problem at the central value $0$ is therefore total: the radicand $0$ has the single root $0$.

## The Reading on the Remarkable Subspaces

Over $\mathbb{R}$ the remarkable subspaces are the scalar line, which is the centre, and the vector subspace (*Introduction to the Remarkable Subspaces of the Quaternions*).

**The centre.** A central element is a scalar $\lambda e_0$, and its square is $\lambda^2e_0$, which vanishes only for $\lambda=0$; the centre contains no nilpotent. The two idempotents $0$ and $e_0$ are central and lie on the scalar line, and neither is a nilpotent.

**The vector subspace.** A non-zero pure element $\mathbf{p}$ has the negative scalar square $-|\mathbf{p}|^2e_0$, non-zero because the Euclidean form is definite. In a symmetric block a square-zero element is necessarily pure, the scalar part $p_0^2-|\mathbf{p}|^2$ and the vector part $2p_0\mathbf{p}$ vanishing together; the vector subspace is where the search for a nilpotent takes place, and **it holds only the origin**.

## Summary

The nilpotents of the block, the non-zero elements of square zero, are none: the only square-zero element is the origin, and there is no element of nilpotency index two or more. The square of an element vanishes only at the origin, so the nilpotent class is empty and the nilpotent cone is the empty set. This is the point of the article: the block has a **large** zero-divisor set, the whole punctured vector subspace $\mathrm{Vect}(\mathbb{H})\setminus\{0\}$ of real dimension three, and **no** nilpotent at all. Every zero divisor is a pure element with the negative scalar square $-|\mathbf{u}|^2e_0\neq0$, so no zero divisor is square-zero, and the two classes are disjoint. Over $\mathbb{R}$ the isotropic subfamily of the pure elements collapses to the origin and the non-isotropic subfamily fills the whole vector subspace; in the complex block the two subfamilies are the nilpotent cone and the remainder of the zero-divisor set, and the cone is genuine. The idempotents $0$ and $e_0$ are central and lie on the scalar line, and neither is a nilpotent; the only element that is both square-zero and idempotent is the origin.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde p\bullet\tilde q$ | the symmetric plain product, the multiplication of the block |
| $\tilde\Upsilon$ | a nilpotent, $\tilde\Upsilon\neq0$ and $\tilde\Upsilon^{\bullet2}=0$; there is none |
| $\{\tilde\Upsilon:\tilde\Upsilon^{\bullet2}=0\}=\{0\}$ | the square-zero elements |
| $\mathcal{N}=\varnothing$ | the nilpotent cone of the block |
| $\mathcal{Z}=\mathrm{Vect}(\mathbb{H})\setminus\{0\}$ | the zero-divisor set, the punctured vector subspace, of real dimension three |
| $\mathbf{u}\bullet\mathbf{u}=-|\mathbf{u}|^2e_0$ | the pure square, never zero off the origin |
| $N(\tilde p)=p_0^2+|\mathbf{p}|^2$ | the norm, positive definite, so every non-zero element is invertible |

## Further Reading

- *Definitions for the Study of the 6 Algebraic Structures*, §*The Element Vocabulary*, for the product-relative definition of a nilpotent and of the square-zero element.
- *Introduction to the Symmetric Plain Algebra of Quaternions*, above this article in this category, for the product, the square and the unit.
- *Introduction to the General Plain Algebra of Quaternions*, for the division property of the plain product that empties the nilpotent class.
- *Nilpotents of the General Plain Algebra* (`articles_maths/nilpotents-of-the-general-plain-algebra-of-quaternions.md`), for the same empty class read on the plain product, the twin of this article.
- *Zero Divisors of the Symmetric Plain Algebra*, above this article in this category, for the zero-divisor set against which the empty nilpotent class is read.
- *Square Roots of Minus One, Zero and Plus One in the Symmetric Plain Algebra*, above this article in this category, for the roots of $0$, which are the origin alone.
- *Norm and Invertibility in the Symmetric Plain Algebra*, above this article in this category, for the invertibility of every non-zero element and the existence of the inverse.
- *The Specificities of the Symmetric Plain Algebra*, below this article in this category, for the definiteness of the norm and the degeneracy of the classes.
- *The Multiplication Operators of the Symmetric Plain Algebra*, below this article in this category, for the operator material of a square-zero element, which the block does not have.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the quadratic form and the nilpotents of a Jordan algebra.
