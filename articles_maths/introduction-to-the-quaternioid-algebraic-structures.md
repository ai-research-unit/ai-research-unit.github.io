# __Introduction to the Quaternioid Algebraic Structures__

## Introduction

The real quaternions $\mathbb{H}$ are a division algebra, and that algebra is the subject of the *Quaternions* category, entered at *Introduction to the Quaternion Algebra*. This category treats another question about the same carrier. Beyond the algebra product $\tilde q_1\tilde q_2$ the space $\mathbb{R}^4$ carries the products built from it and from the conjugation: the symmetrisation $\tfrac12(\tilde q_1\tilde q_2+\tilde q_2\tilde q_1)$, the antisymmetrisation $\tfrac12(\tilde q_1\tilde q_2-\tilde q_2\tilde q_1)$, and the product $\tilde q_1^{\natural}\tilde q_2$ with the conjugation read in the first slot. Their algebras are the **symmetric plain algebra** ($\mathrm{SPA}$), the **antisymmetric plain algebra** ($\mathrm{APA}$) and the **general quaternionic algebra** ($\mathrm{GQA}$). These three are the structures of the category, and the articles below read their basic properties, their element theory and their operators.

## Conventions

$\tilde q = q_te_t+\vec q = \sum_{\mu\in\{t,x,y,z\}}q_\mu e_\mu$ with $q_\mu\in\mathbb{R}$, and $\vec q = \sum_{k=1}^{3}q_k\vec e_k$ is the vector part; $e_t$ is the unit; ${}^{\natural}$ is the quaternion conjugation, $\vec e_k^{\natural}=-\vec e_k$ on the imaginary units and $e_t^{\natural}=e_t$; $(\vec q_1,\vec q_2)=\sum_kq_{1k}q_{2k}$ and $\vec q_1\times\vec q_2$ are the real dot and cross products. The algebra product $\tilde q_1\tilde q_2$ is owned by the *Quaternions* category and is cited from here, never restated. The tilde and the mark ${}^{\natural}$ are those of *Conventions in Mathematics*.

## The Three Companion Products

**Definition.** The **three companion products** of the quaternion space are the **symmetric plain product**, the **antisymmetric plain product** and the **general quaternionic product**,

$$
\tilde q_1\bullet\tilde q_2 = \tfrac12(\tilde q_1\tilde q_2+\tilde q_2\tilde q_1) = \bigl(q_{1t}q_{2t}-(\vec q_1,\vec q_2)\bigr) + q_{1t}\vec q_2 + q_{2t}\vec q_1,
$$

$$
\tilde q_1\wedge\tilde q_2 = \tfrac12(\tilde q_1\tilde q_2-\tilde q_2\tilde q_1) = \vec q_1\times\vec q_2,
$$

$$
\tilde q_1^{\natural}\tilde q_2 = \bigl(q_{1t}q_{2t}+(\vec q_1,\vec q_2)\bigr) + q_{1t}\vec q_2 - q_{2t}\vec q_1 - \vec q_1\times\vec q_2 .
$$

**Theorem.** The algebra product is the sum of its two halves, and the quaternionic product is separated from it by the scalar and the vector part of the first factor,

$$
\tilde q_1\tilde q_2 = \tilde q_1\bullet\tilde q_2 + \tilde q_1\wedge\tilde q_2, \qquad
\tilde q_1\tilde q_2 + \tilde q_1^{\natural}\tilde q_2 = 2q_{1t}\tilde q_2, \qquad
\tilde q_1\tilde q_2 - \tilde q_1^{\natural}\tilde q_2 = 2\vec q_1\,\tilde q_2 .
$$

**Proof.** The symmetrisation keeps the scalar product and the two linear terms of $\tilde q_1\tilde q_2$ and the antisymmetrisation keeps the cross product, so their sum is the algebra product; the quaternionic product is the algebra product with $\tilde q_1$ replaced by $\tilde q_1^{\natural}=q_{1t}e_t-\vec q_1$, which flips the signs of $(\vec q_1,\vec q_2)$, of $q_{2t}\vec q_1$ and of $\vec q_1\times\vec q_2$, and adding or subtracting the two displays kills the vector terms of the first factor. The algebra product and the general quaternionic product are the **two general products** of the space in the sense of the general theory of a product with an involution; the two halves of the first are the symmetric and antisymmetric plain products. The products and their tables are *The 6 Products of the Quaternioid $\mathbb{R}$ Space* and *The Two General Products of the Quaternioid $\mathbb{R}$ Space*.

## The Three Structures

**Definition.** The **three structures** of the category are the algebras of the three companion products,

| Structure | Product | Nature |
|---|---|---|
| symmetric plain algebra (SPA) | $\tilde q_1\bullet\tilde q_2$ | commutative Jordan algebra, unital, not associative |
| antisymmetric plain algebra (APA) | $\tilde q_1\wedge\tilde q_2$ | alternating Lie algebra, no unit |
| general quaternionic algebra (GQA) | $\tilde q_1^{\natural}\tilde q_2$ | left-unital, non-associative |

**Theorem (the laws).** The antisymmetric plain algebra is the only one of the three that satisfies the Jacobi identity, and it is a Lie algebra; the symmetric plain algebra is commutative and satisfies the Jordan identity but not associativity; the general quaternionic algebra has the left unit $e_t$ alone and satisfies neither associativity nor the Jordan identity. Only the general quaternionic structure is free of zero divisors: the symmetric plain product vanishes at two anticommuting pure quaternions, such as $\vec e_x$ and $\vec e_y$, and the antisymmetric product vanishes at every element against itself.

**Proof.** The Jordan and Lie laws are computed in *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*; the zero-divisor reading is *Zero Divisors in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*. For the last clause, the left multiplication of the quaternionic product is $\tilde q_2\mapsto\tilde q_1^{\natural}\tilde q_2$, which is the left multiplication of the division algebra $\mathbb{H}$ by $\tilde q_1^{\natural}$, invertible for $\tilde q_1\neq0$, and the right multiplication $\tilde q_2\mapsto\tilde q_2\tilde q_1^{\natural}$ is invertible likewise.

## The Two Forms and the Two Algebraic Norms

**Theorem.** The companion products carry **two bilinear forms**, the plain form and the quaternion form,

$$
\langle\tilde q_1,\tilde q_2\rangle = \mathrm{Sc}(\tilde q_1\tilde q_2) = q_{1t}q_{2t}-(\vec q_1,\vec q_2), \qquad \langle\tilde q_1,\tilde q_2\rangle_{\natural} = \mathrm{Sc}(\tilde q_1^{\natural}\tilde q_2) = q_{1t}q_{2t}+(\vec q_1,\vec q_2),
$$

of Gram matrices $\operatorname{diag}(1,-1,-1,-1)$ and $\mathrm I_4$, hence of signatures $(1,3)$ and $(4,0)$; the first is carried by the algebra product and by the symmetric plain structure, the second by the general quaternionic structure. The forms are *The 2 Forms over the Quaternioid $\mathbb{R}$ Space*.

**Theorem.** The **two algebraic norms** are the two forms read at their two equal arguments, $\langle\tilde q\rangle = q_t^2-\lvert\vec q\rvert^2$ and $\langle\tilde q\rangle_{\natural} = q_t^2+\lvert\vec q\rvert^2$; the first is indefinite and not multiplicative, the second is positive definite, zero only at the origin, and multiplicative. The criterion of invertibility of the algebra product is the second's: $\tilde q$ is invertible exactly when $\langle\tilde q\rangle_{\natural}\neq0$, with $\tilde q^{-1} = \tilde q^{\natural}/\lvert\tilde q\rvert^2$. The two algebraic norms are *The 2 Algebraic Norms over the Quaternioid $\mathbb{R}$ Space*.

## The General and the Higher Structures

**Remark (the $\mathbb{C}$-readings).** The same carrier read over $\mathbb{C}$ is the biquaternions $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$; the passage from the structures over $\mathbb{R}$ to their $\mathbb{C}$-companions is the complexification, and it is *The Realification and the Effect of the Change of Scalars* and the *Biquaternion Algebraic Structures* category. This category keeps the $\mathbb{R}$-base.

**Remark (the ternary product).** The general quaternionic product is non-associative, and its associator is not confined: the ternary product of the quaternionic product has a non-vanishing associator defect, treated in *The Associator and the Ternary Product of the Quaternionic Product*. This is the non-commutative counterpart of the flat ternary product of the complexoid, and it is why the correction terms of the Jordan triple identity are essential here.

## Summary

The quaternion space $\mathbb{H}$, of real dimension four and with the single involution ${}^{\natural}$, carries, beyond the algebra product of the *Quaternions* category, three companion products: the symmetric plain product $\tilde q_1\bullet\tilde q_2$, the antisymmetric plain product $\tilde q_1\wedge\tilde q_2 = \vec q_1\times\vec q_2$, and the general quaternionic product $\tilde q_1^{\natural}\tilde q_2$. Their algebras are the structures of this category. The antisymmetric plain structure is a Lie algebra and the only one of the three satisfying Jacobi; the symmetric plain structure is a commutative Jordan algebra, unital and not associative; the general quaternionic structure is left-unital and non-associative, and faithful on each side.

The companion products carry two forms, $\langle\cdot,\cdot\rangle$ of signature $(1,3)$ and $\langle\cdot,\cdot\rangle_{\natural}$ of signature $(4,0)$, and two algebraic norms, $\langle\tilde q\rangle = q_t^2-\lvert\vec q\rvert^2$, indefinite and not multiplicative, and $\langle\tilde q\rangle_{\natural} = q_t^2+\lvert\vec q\rvert^2$, definite and multiplicative, the latter being the criterion of invertibility of the algebra product.

| Structure | Product | Form | Algebraic norm |
|---|---|---|---|
| SPA | $\tilde q_1\bullet\tilde q_2$ | $\langle\tilde q_1,\tilde q_2\rangle = q_{1t}q_{2t}-(\vec q_1,\vec q_2)$ | $\langle\tilde q\rangle = q_t^2-\lvert\vec q\rvert^2$, indefinite |
| APA | $\tilde q_1\wedge\tilde q_2$ | vanishing (antisymmetric) | vanishing |
| GQA | $\tilde q_1^{\natural}\tilde q_2$ | $\langle\tilde q_1,\tilde q_2\rangle_{\natural} = q_{1t}q_{2t}+(\vec q_1,\vec q_2)$ | $\langle\tilde q\rangle_{\natural} = q_t^2+\lvert\vec q\rvert^2$, definite |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde q = q_te_t+\vec q$ | general quaternion, $q_\mu\in\mathbb{R}$ |
| $\tilde q^{\natural}$ | quaternion conjugation, $\vec e_k^{\natural} = -\vec e_k$ |
| $\tilde q_1\tilde q_2$ | the algebra product, of the *Quaternions* category |
| $\tilde q_1\bullet\tilde q_2$, $\tilde q_1\wedge\tilde q_2$, $\tilde q_1^{\natural}\tilde q_2$ | the three companion products |
| SPA, APA, GQA | the three structures |
| $\langle\tilde q_1,\tilde q_2\rangle$, $\langle\tilde q_1,\tilde q_2\rangle_{\natural}$ | the plain form and the quaternion form |
| $\langle\tilde q\rangle$, $\langle\tilde q\rangle_{\natural}$ | the plain and quaternion algebraic norms |
| $\operatorname{diag}(1,-1,-1,-1)$, $\mathrm I_4$ | Gram matrices of $\langle\cdot\rangle$ and $\langle\cdot\rangle_{\natural}$ |

## Further Reading

- [Introduction to the Quaternion Algebra](introduction-to-the-quaternion-algebra.html), in the *Quaternions* category, for the algebra product, its unit, its norm and its division property.
- [The 6 Products of the Quaternioid Real Space](the-6-products-of-the-quaternioid-real-space.html) and [The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space](the-algebraic-structures-over-the-quaternioid-r-space.html), for the products of the carrier and the laws of the structures.
- [The 2 Forms over the Quaternioid $\mathbb{R}$ Space](the-2-forms-over-the-quaternioid-r-space.html) and [The 2 Algebraic Norms over the Quaternioid $\mathbb{R}$ Space](the-2-algebraic-norms-over-the-quaternioid-r-space.html), for the two forms and the two algebraic norms.
- [The Associator and the Ternary Product of the Quaternionic Product](the-associator-and-the-ternary-product-of-the-quaternionic-product-of-quaternioid.html), for the non-commutative ternary product.
- [Introduction to the General Quaternionic Algebra](introduction-to-the-general-quaternionic-algebra-of-quaternioid.html), [Introduction to the Symmetric Plain Algebra](introduction-to-the-symmetric-plain-algebra-of-quaternioid.html) and [Introduction to the Antisymmetric Plain Algebra](introduction-to-the-antisymmetric-plain-algebra-of-quaternioid.html), for the three structures individually.
- [Algebras: A General Introduction](algebras-a-general-introduction.html), *Symmetric Algebras*, *Anti-symmetric Algebras* and [Sesqualgebras](sesqualgebras.html), for the general theory of the algebras the three structures instantiate.
