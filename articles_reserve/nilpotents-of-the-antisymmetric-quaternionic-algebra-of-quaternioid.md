# __Nilpotents of the Antisymmetric Quaternionic Algebra__

## Introduction

The nilpotent is defined by an equation in which the product occurs, so it is a class of the product and not of the space (*Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*). The block of this article is the antisymmetric quaternionic multiplication

$$
\tilde p\diamond\tilde q=\tfrac12\bigl(\tilde p^{\natural}\tilde q-\tilde q^{\natural}\tilde p\bigr)
=p_0\vec q-q_t\vec p-\vec p\times\vec q ,
$$

which is alternating and without a unit (*Introduction to the Antisymmetric Quaternionic Algebra of Quaternions*). The article determines its nilpotent class and its index.

The answer is total. The block is alternating, so $\tilde\upsilon\diamond\tilde\upsilon=0$ for every element, and therefore the square-zero set of the block is the whole space: **every nonzero element of $\mathbb{H}$ is a nilpotent of the block, of index exactly two**, and no nilpotent has index three or more. The nilpotent class of the block is thus the punctured space, the largest a nilpotent class can be, and it strictly contains the parent quaternionic product's, which over $\mathbb{R}$ is empty. The square-zero set is at once the root set of $0$ and, off the origin, the zero-divisor set of the block, and the two companion articles are cited. The higher powers are read with the left-nested bracketing of the definitions, since the block is not associative.

**Conventions.** Throughout, $\tilde p=p_0e_t+\vec p$, $\tilde q=q_te_t+\vec q$ and $\tilde\upsilon=\upsilon_0e_t+\vec\upsilon$ name elements of $\mathbb{H}$ with real coefficients, $(\vec p,\vec q)$ is the dot product and $\vec p\times\vec q$ the cross product of the vector parts, and $\tilde q^{\natural}=q_te_t-\vec q$ is the quaternion conjugation; the bar is the identity and the star coincides with the natural conjugation, so no bare bar is written on an element of this block. The operation is written $\diamond$ and never $\wedge^{\natural}$ outside a citation, and unqualified, *nilpotent* means a nilpotent of the block. The quaternion form of the space is $N(\tilde p)=p_0^2+\lvert\vec p\rvert^2$, positive definite.

**Boundaries.** The operation and its alternation are *Introduction to the Antisymmetric Quaternionic Algebra of Quaternions*; the definitions of the nilpotent, the index of nilpotency and the square-zero element are *Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*. The nilpotents of the general plain product, to which the block is compared, are *Nilpotents of the General Plain Algebra*; the nilpotent sets of the six structures are *Nilpotents in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*; the zero divisors and the idempotents of the block are *Zero Divisors of the Antisymmetric Quaternionic Algebra* and *Idempotents of the Antisymmetric Quaternionic Algebra*; and the matrix models are *The Antisymmetric Quaternionic Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* and *The Antisymmetric Quaternionic Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{R})_L$*.

## The Notion and Its Product

**Definition (nilpotent of a product).** Let $\star$ be a product on $\mathbb{H}$. A **nilpotent of $\star$** is a nonzero element $\tilde\upsilon$ some power of which vanishes,

$$
\tilde\upsilon^{\star k}=0 \quad\text{for some } k\geq1 ,
$$

the power being the left-nested reading $\tilde\upsilon^{\star k}=\bigl(\cdots\bigl((\tilde\upsilon\star\tilde\upsilon)\star\tilde\upsilon\bigr)\cdots\star\tilde\upsilon\bigr)$ when the product is not associative. The least such $k$ is the **index of nilpotency**, and a nilpotent of index two, $\tilde\upsilon\star\tilde\upsilon=0$ with $\tilde\upsilon\neq0$, is a **square-zero element of $\star$**. The origin satisfies $\tilde\upsilon^{\star1}=0$ but is excluded from the nilpotent class by the nonzero requirement, which the article keeps throughout.

Throughout this article the product is the **antisymmetric quaternionic multiplication** $\diamond$, and unqualified, *nilpotent* means a nilpotent of the block. The nilpotents of the general plain product, to which the block is compared, are *Nilpotents of the General Plain Algebra*; the nilpotent sets of the six structures of the real chapter are *Nilpotents in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*.

## The Criterion

**Theorem (the criterion for the block).** The square-zero set of the antisymmetric quaternionic multiplication is the whole space $\mathbb{H}$; every nonzero element is a nilpotent of the block. Equivalently, the square-zero equation holds at every element and the nilpotent class is the punctured space $\mathbb{H}\setminus\{0\}$.

*Proof.* The block is alternating, $\tilde\upsilon\diamond\tilde\upsilon=0$ for every element $\tilde\upsilon$, by *Introduction to the Antisymmetric Quaternionic Algebra of Quaternions*; the set of the elements whose square vanishes is therefore the whole space. A nilpotent is by definition a nonzero member of that set, so the nilpotent class is the whole space without its origin.

The criterion is the alternation of the product read as an element statement, and it is met by every element, the origin included. There is no hypothesis on the element, no scalar part and no vector part to test: the equation $\tilde\upsilon\diamond\tilde\upsilon=0$ is an identity of the block and not a condition on $\tilde\upsilon$. This is the exact opposite of the four structures of the plain and quaternionic families, whose square-zero set is the origin alone and which therefore have no nilpotent, and the contrast is drawn in *Nilpotents in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*.

## The Index

**Proposition (index two, and no higher index).** For every element $\tilde\upsilon$ and every $k\geq2$ the left-nested power vanishes,

$$
\tilde\upsilon^{\diamond k}=0 \quad (k\geq2),
$$

and every nilpotent of the block has index exactly two. The block carries no nilpotent of index three or more.

*Proof.* The left-nested square is $\tilde\upsilon\diamond\tilde\upsilon=0$; the third power is $\bigl(\tilde\upsilon\diamond\tilde\upsilon\bigr)\diamond\tilde\upsilon=0\diamond\tilde\upsilon=0$, and each higher power is formed from a vanishing power and therefore vanishes again. A nonzero element has a nonvanishing first power and a vanishing second power, so its index is exactly two; the origin, whose first power already vanishes, is not a nilpotent, the class being the nonzero elements.

The boundedness of the index is a second sense in which the block is extreme. The general plain and the general quaternionic algebras over $\mathbb{R}$ have no nilpotent at all, their square-zero set being the origin alone; here every nonzero element is a nilpotent of index two, and the membership test is vacuous. The block has the largest nilpotent class and the smallest positive index.

## The Relation to the Zero Divisors

**Proposition (every nonzero nilpotent is a two-sided zero divisor; it is its own partner).** Every nonzero nilpotent $\tilde\upsilon$ of the block satisfies $\tilde\upsilon\diamond\tilde\upsilon=0$, so it lies in its own left annihilator and in its own right annihilator, and it is a two-sided zero divisor with itself as the annihilating partner.

*Proof.* The square is zero by the criterion, so the element is a partner of itself on the left and on the right; the partner is nonzero because the nilpotent is, and the definition of the zero divisor is met. The annihilators of the two sides coincide by the alternation of the block (*Zero Divisors of the Antisymmetric Quaternionic Algebra*), and each contains the line $\mathbb{R}\tilde\upsilon$, to which it is equal for a nonzero element.

The implication *nilpotent implies zero divisor* therefore holds for the block at every nilpotent without exception: the nilpotent class is the punctured space, the zero-divisor class is the same punctured space, and the two coincide, the origin being excluded from both by the common requirement that the element be nonzero. This is a self-annihilation and not a pairing of two distinct elements: the square of an element is zero, so every element is its own annihilating partner, and the square detects no zero divisor here because it vanishes on everything.

## The Relation to the Idempotents

**Remark (the two classes are disjoint).** No element of the block is both an idempotent and a nilpotent. The idempotent class of the block is the origin alone (*Idempotents of the Antisymmetric Quaternionic Algebra*), and the origin is not a nilpotent, the nilpotent class being the nonzero elements; and a nonzero nilpotent has vanishing square while a nonzero idempotent would satisfy $\tilde\Pi\diamond\tilde\Pi=\tilde\Pi\neq0$. The two classes are therefore disjoint.

The statement is the sharp form of a general fact. The idempotent class of the block is the origin alone and the nilpotent class is the whole punctured space, the two extremes that the definitions allow: the smallest idempotent class and the largest nilpotent class. The reason is one and the same, the vanishing square of the block, which collapses the idempotent equation to $0=\tilde\Pi$ and leaves the nilpotent equation an identity.

## The Conjugations and the Matrix Model

**Proposition (the conjugation preserves the nilpotent class).** The natural conjugation ${}^{\natural}$ carries the nilpotent class of the block onto itself, the class being the whole punctured space; and on the values of the block the natural conjugation acts as the negative of the identity,

$$
(\tilde p\diamond\tilde q)^{\natural}=-\tilde p\diamond\tilde q .
$$

*Proof.* The nilpotent class is the whole space apart from the origin, and the natural conjugation is a bijection of $\mathbb{H}$ fixing the origin, so it carries the class onto itself. For the display, the natural conjugation is an anti-automorphism of the plain product, so $(\tilde p^{\natural}\tilde q)^{\natural}=\tilde q^{\natural}\tilde p$; applying it to the two terms of the definition of the block gives $\tfrac12(\tilde q^{\natural}\tilde p-\tilde p^{\natural}\tilde q)=-\tilde p\diamond\tilde q$. The bar is the identity and the star is the natural conjugation, so the other two signs give nothing new here.

**Remark (the matrix model).** In either matrix model of the block the square of an element vanishes, so the matrix of the square is the zero matrix and the nilpotent class is the whole matrix space apart from the zero matrix: $\mathsf{M}(\tilde p\diamond\tilde p)=\mathsf{M}(0)=0$ for every $\tilde p$, in the $2\times2$ model $M_2(\mathbb{C})$ and in the $4\times4$ model $M_4(\mathbb{R})_L$ alike (*The Antisymmetric Quaternionic Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*, *The Antisymmetric Quaternionic Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{R})_L$*). The matrix models therefore carry no nilpotent condition beyond the vanishing of the square.

## The Relation to the Parent Product

**Remark (the parent has no nilpotent over $\mathbb{R}$).** The parent quaternionic product $\tilde p^{\natural}\tilde q$ has the square $\tilde p^{\natural}\tilde p=N(\tilde p)e_t$, so its square-zero set is the zero set of the quaternion form, $N(\tilde p)=0$. Over $\mathbb{R}$ the form is a sum of four squares, hence positive definite, and its zero set is the origin alone: the parent has **no nilpotent** at all, and its zero-divisor class is empty as well (*Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra*, *Zero Divisors of the General Quaternionic Algebra*). The block is the parent with the scalar part removed, and with the scalar part removed the square of the parent, which was a positive definite central value, becomes the zero of the block: the parent's one-point square-zero set widens to the whole space, and its single point of vanishing becomes the whole punctured nilpotent class. The block's nilpotent class strictly contains the parent's empty one, and the difference is the whole punctured space, on which the parent's square is a nonzero central value and the block's square is zero.

The contrast with the biquaternion chapter is exactly the definiteness of the form. There the quaternion form has nonzero isotropic vectors, its zero set is a proper cone, and the parent's square-zero set is that cone, a proper subfamily of the space; over $\mathbb{R}$ the definite form has no nonzero isotropic vector, the parent's square-zero set degenerates to the origin, and the removal of the scalar part widens the origin to the whole space. The block's nilpotent class is the largest in both chapters, but the class it strictly contains is the punctured isotropic cone of the complex parent in one and the empty class of the real parent in the other.

## Summary

For the antisymmetric quaternionic multiplication $\tilde p\diamond\tilde q=p_0\vec q-q_t\vec p-\vec p\times\vec q$ every nonzero element is a nilpotent: the square $\tilde\upsilon\diamond\tilde\upsilon$ vanishes identically, so the square-zero set is the whole space and every nilpotent has index exactly two, and no nilpotent has index three or more. The nilpotent class is therefore the punctured space, and it strictly contains the parent quaternionic product's, which over $\mathbb{R}$ is empty, the quaternion form being positive definite. Every nilpotent is a two-sided zero divisor with itself as the annihilating partner, and the implication *nilpotent implies zero divisor* holds for the block at every nilpotent without exception; the square detects no zero divisor here because it vanishes on everything. The nilpotent class and the idempotent class are disjoint, the idempotent class being the origin alone. The natural conjugation carries the class onto itself and acts as the negative of the identity on the values of the block; in either matrix model the square is the zero matrix.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde p\diamond\tilde q=\tfrac12(\tilde p^{\natural}\tilde q-\tilde q^{\natural}\tilde p)=p_0\vec q-q_t\vec p-\vec p\times\vec q$ | the antisymmetric quaternionic multiplication, the operation $\mathrm{AQA}$ |
| $\tilde\upsilon\diamond\tilde\upsilon=0$ | the criterion, the vanishing square of every element |
| $\mathbb{H}$ | the square-zero set of the block, the whole space |
| $\mathbb{H}\setminus\{0\}$ | the nilpotent class of the block, the punctured space |
| $2$ | the index of nilpotency of every nilpotent |
| $(\tilde p\diamond\tilde q)^{\natural}=-\tilde p\diamond\tilde q$ | the natural conjugation acts as minus the identity on the values |
| $N(\tilde\upsilon)=\upsilon_0^2+\lvert\vec\upsilon\rvert^2$ | the quaternion form, positive definite, whose zero set is the parent's square-zero set |

## Further Reading

- *Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-quaternioid-r-space.md`), for the nilpotent, the index of nilpotency, the square-zero element and the relativity of the definitions to the product.
- *Introduction to the Antisymmetric Quaternionic Algebra* (`articles_maths/introduction-to-the-antisymmetric-quaternionic-algebra-of-quaternioid.md`), for the operation, its alternation and its table.
- *Nilpotents in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/nilpotents-in-the-algebraic-structures-over-the-quaternion-r-space.md`), for the nilpotent sets of the six structures of the real chapter.
- *Zero Divisors of the Antisymmetric Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-antisymmetric-quaternionic-algebra-of-quaternioid.md`), for the coincidence of the square-zero set with the zero-divisor set and for the annihilators.
- *Idempotents of the Antisymmetric Quaternionic Algebra* (`articles_maths/idempotents-of-the-antisymmetric-quaternionic-algebra-of-quaternioid.md`), for the idempotent class, the origin alone, which is disjoint from the nilpotent class.
- *Square Roots of Minus One, Zero and Plus One in the Antisymmetric Quaternionic Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-antisymmetric-quaternionic-algebra-of-quaternioid.md`), for the root set of $0$, which is the square-zero set.
- *Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-general-quaternionic-algebra-of-quaternioid.md`), for the parent product, which over $\mathbb{R}$ has no nilpotent.
- *Zero Divisors of the General Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-general-quaternionic-algebra-of-quaternioid.md`), for the parent product, whose square-zero set over $\mathbb{R}$ is the origin alone.
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for nilpotents, the index of nilpotency and the radical of an algebra.
- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for the alternating bilinear rule and the vanishing of its square.
