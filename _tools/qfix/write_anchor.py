content = r'''# __Introduction to the Quaternioid Algebraic Structures__

## Introduction

The real quaternions $\mathbb{H}$ are a division algebra, and that algebra is the subject of the *Quaternions* category, entered at *Introduction to the Quaternion Algebra*. This category treats another question about the same carrier. Beyond the algebra product $\tilde p\tilde q$ the space $\mathbb{R}^4$ carries the products built from it and from the conjugation: the symmetrisation $\tfrac12(\tilde p\tilde q+\tilde q\tilde p)$, the antisymmetrisation $\tfrac12(\tilde p\tilde q-\tilde q\tilde p)$, and the product $\tilde p^{\natural}\tilde q$ with the conjugation read in the first slot. Their algebras are the **symmetric plain algebra** ($\mathrm{SPA}$), the **antisymmetric plain algebra** ($\mathrm{APA}$) and the **general quaternionic algebra** ($\mathrm{GQA}$). These three are the structures of the category, and the articles below read their basic properties, their element theory and their operators.

## Conventions

$\tilde p = p_0e_0+\vec p = \sum_{\mu=0}^{3}p_\mu e_\mu$ with $p_\mu\in\mathbb{R}$, and $\vec p = \sum_{k=1}^{3}p_ke_k$ is the vector part; $e_0$ is the unit; ${}^{\natural}$ is the quaternion conjugation, $e_k^{\natural}=-e_k$ on the imaginary units and $e_0^{\natural}=e_0$; $(\vec p,\vec q)=\sum_kp_kq_k$ and $\vec p\times\vec q$ are the real dot and cross products. The algebra product $\tilde p\tilde q$ is owned by the *Quaternions* category and is cited from here, never restated. The tilde and the mark ${}^{\natural}$ are those of *Conventions in Mathematics*.

## The Three Companion Products

**Definition.** The **three companion products** of the quaternion space are the **symmetric plain product**, the **antisymmetric plain product** and the **general quaternionic product**,

$$
\tilde p\bullet\tilde q = \tfrac12(\tilde p\tilde q+\tilde q\tilde p) = \bigl(p_0q_0-(\vec p,\vec q)\bigr) + p_0\vec q + q_0\vec p,
$$

$$
\tilde p\wedge\tilde q = \tfrac12(\tilde p\tilde q-\tilde q\tilde p) = \vec p\times\vec q,
$$

$$
\tilde p^{\natural}\tilde q = \bigl(p_0q_0+(\vec p,\vec q)\bigr) + p_0\vec q - q_0\vec p - \vec p\times\vec q .
$$

**Theorem.** The algebra product is the sum of its two halves, and the quaternionic product is separated from it by the scalar and the vector part of the first factor,

$$
\tilde p\tilde q = \tilde p\bullet\tilde q + \tilde p\wedge\tilde q, \qquad
\tilde p\tilde q + \tilde p^{\natural}\tilde q = 2p_0\tilde q, \qquad
\tilde p\tilde q - \tilde p^{\natural}\tilde q = 2\vec p\,\tilde q .
$$

**Proof.** The symmetrisation keeps the scalar product and the two linear terms of $\tilde p\tilde q$ and the antisymmetrisation keeps the cross product, so their sum is the algebra product; the quaternionic product is the algebra product with $\tilde p$ replaced by $\tilde p^{\natural}=p_0e_0-\vec p$, which flips the signs of $(\vec p,\vec q)$, of $q_0\vec p$ and of $\vec p\times\vec q$, and adding or subtracting the two displays kills the vector terms of the first factor. The algebra product and the general quaternionic product are the **two general products** of the space in the sense of the general theory of a product with an involution; the two halves of the first are the symmetric and antisymmetric plain products. The products and their tables are *The 6 Products of the Quaternioid $\mathbb{R}$ Space* and *The Two General Products of the Quaternioid $\mathbb{R}$ Space*.

## The Three Structures

**Definition.** The **three structures** of the category are the algebras of the three companion products,

| Structure | Product | Nature |
|---|---|---|
| symmetric plain algebra (SPA) | $\tilde p\bullet\tilde q$ | commutative Jordan algebra, unital, not associative |
| antisymmetric plain algebra (APA) | $\tilde p\wedge\tilde q$ | alternating Lie algebra, no unit |
| general quaternionic algebra (GQA) | $\tilde p^{\natural}\tilde q$ | left-unital, non-associative |

**Theorem (the laws).** The antisymmetric plain algebra is the only one of the three that satisfies the Jacobi identity, and it is a Lie algebra; the symmetric plain algebra is commutative and satisfies the Jordan identity but not associativity; the general quaternionic algebra has the left unit $e_0$ alone and satisfies neither associativity nor the Jordan identity. Only the general quaternionic structure is free of zero divisors: the symmetric plain product vanishes at two anticommuting pure quaternions, such as $e_1$ and $e_2$, and the antisymmetric product vanishes at every element against itself.

**Proof.** The Jordan and Lie laws are computed in *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*; the zero-divisor reading is *Zero Divisors in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*. For the last clause, the left multiplication of the quaternionic product is $\tilde q\mapsto\tilde p^{\natural}\tilde q$, which is the left multiplication of the division algebra $\mathbb{H}$ by $\tilde p^{\natural}$, invertible for $\tilde p\neq0$, and the right multiplication $\tilde q\mapsto\tilde q\tilde p^{\natural}$ is invertible likewise.

## The Two Forms and the Two Algebraic Norms

**Theorem.** The companion products carry **two bilinear forms**, the plain form and the quaternion form,

$$
B(\tilde p,\tilde q) = \mathrm{Sc}(\tilde p\tilde q) = p_0q_0-(\vec p,\vec q), \qquad N(\tilde p,\tilde q) = \mathrm{Sc}(\tilde p^{\natural}\tilde q) = p_0q_0+(\vec p,\vec q),
$$

of Gram matrices $\operatorname{diag}(1,-1,-1,-1)$ and $\mathrm I_4$, hence of signatures $(1,3)$ and $(4,0)$; the first is carried by the algebra product and by the symmetric plain structure, the second by the general quaternionic structure. The forms are *The 2 Forms over the Quaternioid $\mathbb{R}$ Space*.

**Theorem.** The **two algebraic norms** are the values at the two equal arguments, $N_P(\tilde p) = \tilde p^2$ and $N_Q(\tilde p) = \tilde p^{\natural}\tilde p = \lvert\tilde p\rvert^2e_0$; the first is indefinite and not multiplicative, the second is positive definite, zero only at the origin, and multiplicative. The criterion of invertibility of the algebra product is the second's: $\tilde p$ is invertible exactly when $N_Q(\tilde p)\neq0$, with $\tilde p^{-1} = \tilde p^{\natural}/\lvert\tilde p\rvert^2$. The two algebraic norms are *The 2 Algebraic Norms over the Quaternioid $\mathbb{R}$ Space*.

## The General and the Higher Structures

**Remark (the $\mathbb{C}$-readings).** The same carrier read over $\mathbb{C}$ is the biquaternions $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$; the passage from the structures over $\mathbb{R}$ to their $\mathbb{C}$-companions is the complexification, and it is *The Realification and the Effect of the Change of Scalars* and the *Biquaternioid Algebraic Structures* category. This category keeps the $\mathbb{R}$-base.

**Remark (the ternary product).** The general quaternionic product is non-associative, and its associator is not confined: the ternary product of the quaternionic product has a non-vanishing associator defect, treated in *The Associator and the Ternary Product of the Quaternionic Product*. This is the non-commutative counterpart of the flat ternary product of the complexoid, and it is why the correction terms of the Jordan triple identity are essential here.

## Summary

The quaternion space $\mathbb{H}$, of real dimension four and with the single involution ${}^{\natural}$, carries, beyond the algebra product of the *Quaternions* category, three companion products: the symmetric plain product $\tilde p\bullet\tilde q$, the antisymmetric plain product $\tilde p\wedge\tilde q = \vec p\times\vec q$, and the general quaternionic product $\tilde p^{\natural}\tilde q$. Their algebras are the structures of this category. The antisymmetric plain structure is a Lie algebra and the only one of the three satisfying Jacobi; the symmetric plain structure is a commutative Jordan algebra, unital and not associative; the general quaternionic structure is left-unital and non-associative, and faithful on each side.

The companion products carry two forms, $B$ of signature $(1,3)$ and $N$ of signature $(4,0)$, and two algebraic norms, $N_P(\tilde p)=\tilde p^2$, indefinite and not multiplicative, and $N_Q(\tilde p)=\lvert\tilde p\rvert^2e_0$, definite and multiplicative, the latter being the criterion of invertibility of the algebra product.

| Structure | Product | Form | Algebraic norm |
|---|---|---|---|
| SPA | $\tilde p\bullet\tilde q$ | $B(\tilde p,\tilde q) = p_0q_0-(\vec p,\vec q)$ | $N_P(\tilde p) = \tilde p^2$, indefinite |
| APA | $\tilde p\wedge\tilde q$ | vanishing (antisymmetric) | vanishing |
| GQA | $\tilde p^{\natural}\tilde q$ | $N(\tilde p,\tilde q) = p_0q_0+(\vec p,\vec q)$ | $N_Q(\tilde p) = \lvert\tilde p\rvert^2e_0$, definite |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde p = p_0e_0+\vec p$ | general quaternion, $p_\mu\in\mathbb{R}$ |
| $\tilde p^{\natural}$ | quaternion conjugation, $e_k^{\natural} = -e_k$ |
| $\tilde p\tilde q$ | the algebra product, of the *Quaternions* category |
| $\tilde p\bullet\tilde q$, $\tilde p\wedge\tilde q$, $\tilde p^{\natural}\tilde q$ | the three companion products |
| SPA, APA, GQA | the three structures |
| $B(\tilde p,\tilde q)$, $N(\tilde p,\tilde q)$ | the plain form and the quaternion form |
| $N_P(\tilde p)$, $N_Q(\tilde p)$ | the plain and quaternion algebraic norms |
| $\operatorname{diag}(1,-1,-1,-1)$, $\mathrm I_4$ | Gram matrices of $B$ and $N$ |

## Further Reading

- *Introduction to the Quaternion Algebra* (`articles_maths/introduction-to-the-quaternion-algebra.md`), in the *Quaternions* category, for the algebra product, its unit, its norm and its division property.
- *The 6 Products of the Quaternioid $\mathbb{R}$ Space* (`articles_maths/the-6-products-of-the-quaternioid-real-space.md`) and *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/the-algebraic-structures-over-the-quaternioid-r-space.md`), for the products of the carrier and the laws of the structures.
- *The 2 Forms over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/the-2-forms-over-the-quaternioid-r-space.md`) and *The 2 Algebraic Norms over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/the-2-algebraic-norms-over-the-quaternioid-r-space.md`), for the two forms and the two algebraic norms.
- *The Associator and the Ternary Product of the Quaternionic Product* (`articles_maths/the-associator-and-the-ternary-product-of-the-quaternionic-product-of-quaternioid.md`), for the non-commutative ternary product.
- *Introduction to the General Quaternionic Algebra* (`articles_maths/introduction-to-the-general-quaternionic-algebra-of-quaternioid.md`), *Introduction to the Symmetric Plain Algebra* (`articles_maths/introduction-to-the-symmetric-plain-algebra-of-quaternioid.md`) and *Introduction to the Antisymmetric Plain Algebra* (`articles_maths/introduction-to-the-antisymmetric-plain-algebra-of-quaternioid.md`), for the three structures individually.
- *Algebras: A General Introduction*, *Symmetric Algebras*, *Anti-symmetric Algebras* and *Sesqualgebras*, for the general theory of the algebras the three structures instantiate.
'''
p = '/home/hp/Documents/1_Doc/Projects/ai-research/ai-research-unit/articles_maths/introduction-to-the-quaternioid-algebraic-structures.md'
open(p, 'w', encoding='utf-8').write(content)
print('written', len(content.split()), 'words')
