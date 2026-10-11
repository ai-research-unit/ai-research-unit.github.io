# __The Idempotents of the Two General Products__

## Introduction

An idempotent of a product is an element equal to its own square in that product. This article determines the idempotents of the two general products and of the six structures they generate, and contrasts the two-point set that survives with the large idempotent sets of the biquaternion chapter. The products are *The Two General Products of the Quaternion $\mathbb{R}$ Space* and the six structures are *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, above this article in this category.

## Idempotents of a Product

**Definition.** Let $\star$ be a product on $\mathbb{H}$. An **idempotent** of $\star$ is an element $\tilde e$ with $\tilde e\star\tilde e=\tilde e$. The idempotent set is read relative to the product, as the phrase *idempotent of the general plain product* records; the element $0$ is idempotent in every product, and $e_0$ is idempotent in every product for which the product of $e_0$ with itself is $e_0$.

## The Two General Products

**Theorem.** The idempotents of the general plain product $\tilde p\tilde q$ and of the general quaternionic product $\tilde p^{\natural}\tilde q$ are exactly $0$ and $e_0$.

**Proof.** For the plain product, $\tilde x\tilde x=\tilde x$ reads $\tilde x(\tilde x-e_0)=0$; if $\tilde x\neq0$ then $\tilde x$ is invertible and $\tilde x=e_0$. For the quaternionic product, $\tilde x^{\natural}\tilde x=\tilde x$ reads $N(\tilde x)e_0=\tilde x$, so $\tilde x$ is a real scalar $s$ and $s^2=s$, giving $s\in\{0,1\}$. In both products the set is the two-point set $\{0,e_0\}$, exactly the two idempotents the scalar field $\mathbb{R}$ has.

## The Six Structures

| structure | product | idempotents | reason |
|---|---|---|---|
| GPA | $\tilde p\tilde q$ | $\{0,e_0\}$ | division |
| GQA | $\tilde p^{\natural}\tilde q$ | $\{0,e_0\}$ | $\tilde x^{\natural}\tilde x=N(\tilde x)e_0$ |
| SPA | $\tilde p\bullet\tilde q$ | $\{0,e_0\}$ | $\tilde x\bullet\tilde x=\tilde x^2$ |
| SQA | $\tfrac12(\tilde p^{\natural}\tilde q+\tilde q^{\natural}\tilde p)$ | $\{0,e_0\}$ | value in the scalar line forces $\tilde x$ real |
| APA | $\tilde p\times\tilde q$ | $\{0\}$ | $\tilde x\times\tilde x=0$ |
| AQA | $\tfrac12(\tilde p^{\natural}\tilde q-\tilde q^{\natural}\tilde p)$ | $\{0\}$ | $\tilde x\star\tilde x=0$ |

The two symmetrisations keep the two-point set of the general products: the Jordan square $\tilde x\bullet\tilde x$ equals the plain square $\tilde x\tilde x$, and the quaternionic symmetrisation is scalar valued, so its idempotent equation reduces to the real equation $s^2=s$. The two antisymmetrisations kill every square, $\tilde x\star\tilde x=0$, so their only idempotent is $0$; the origin is an idempotent in every product and is the sole survivor here.

The idempotents in the plain product are *The Specificities of the General Plain Algebra*, above this article in this category, and those of the Jordan product are folded into *The Specificities of the Symmetric Plain Algebra*; the antisymmetric cases are the two specificities of their blocks. This article owns only the comparison.

## Contrast with the Biquaternion Case

In the biquaternion chapter the idempotents of the four products form a large set: the standard pair $\tilde\Pi_1,\tilde\Pi_2$ and their conjugates, a quadric of Hermitian idempotents in the Hermitian subspace, and the projection calculus built on them. Over $\mathbb{R}$ there is no idempotent beyond $0$ and $e_0$ in the general products, no proper Peirce decomposition, and no minimal left ideal carried by an idempotent: the algebra is a division algebra and its only idempotents are the trivial ones. The collapse from a quadric to a two-point set is the collapse of the four products to two read on this question, and it is the same divisibility that removes the zero divisors.

## Summary

The general plain and general quaternionic products have exactly the idempotents $0$ and $e_0$, the former by division, the latter because its square is the norm times $e_0$. The symmetrised structures keep the same two-point set, the Jordan square being the plain square and the symmetrised quaternionic square being scalar valued; the two antisymmetric structures have the origin alone, since their square is identically zero. In the biquaternion chapter the idempotent set is a large quadric; here it is the two-point set of the field, and the difference is the division property.

## Summary of Notation

| symbol | meaning |
|---|---|
| idempotent of $\star$ | $\tilde e$ with $\tilde e\star\tilde e=\tilde e$ |
| $\{0,e_0\}$ | the idempotent set of GPA, GQA, SPA, SQA |
| $\{0\}$ | the idempotent set of APA and AQA |
| $\tilde x^{\natural}\tilde x=N(\tilde x)e_0$ | the identity forcing a quaternionic idempotent to be real |

## Further Reading

- *The Two General Products of the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-two-general-products-of-the-quaternion-r-space.md`), for the products.
- *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-6-algebraic-structures-over-the-quaternion-r-space.md`), for the six structures.
- *The Specificities of the General Plain Algebra* (`articles_maths/the-specificities-of-the-general-plain-algebra-of-quaternions.md`), above this article in this category, for the idempotents of the plain product.
- *The Square-Zero Elements of the Two General Products* (`articles_maths/the-square-zero-elements-of-the-two-general-products.md`), below this article in this category, for the companion class.
