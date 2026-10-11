# __The Zero Divisors and the Two General Products__

## Introduction

A zero divisor of a product is a pair of nonzero elements whose product vanishes. This article puts the two general products side by side on that question, proves that neither has a zero divisor, and reads the same question on the six structures the products generate, where the answer is no longer the same. The products are *The Two General Products of the Quaternion $\mathbb{R}$ Space*; the six structures are *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*; the per-structure sets are *Zero Divisors of the Symmetric Plain Algebra*, *Zero Divisors of the Symmetric Quaternionic Algebra* and the two antisymmetric companions, above this article in this category; the article re-derives none of them.

## Zero Divisors of a Product

**Definition.** Let $\star$ be a product on $\mathbb{H}$. A **zero divisor** of $\star$ is a pair $(\tilde x,\tilde y)$ with $\tilde x\neq0$, $\tilde y\neq0$ and $\tilde x\star\tilde y=0$. The product is **without zero divisors** when no such pair exists. A zero divisor is **left** when the first factor is the fixed one, and the class is read relative to the product, as the name *zero divisor of the general plain product* records.

## The Two General Products Have None

**Theorem.** Neither the general plain product $\tilde p\tilde q$ nor the general quaternionic product $\tilde p^{\natural}\tilde q$ has a zero divisor.

**Proof.** For the plain product, if $\tilde x\tilde y=0$ with $\tilde x\neq0$ then $\tilde x$ is invertible and multiplying on the left by $\tilde x^{-1}$ gives $\tilde y=0$; hence there is no pair of nonzero factors. For the quaternionic product, $\tilde x^{\natural}\tilde y=0$ with $\tilde x\neq0$ gives $\tilde y=0$ in the same way, because $\tilde x^{\natural}$ is invertible with inverse $(\tilde x^{\natural})^{-1}=(\tilde x^{-1})^{\natural}$. The norm supplies the one-line form of both: $N(\tilde x\star\tilde y)=N(\tilde x)N(\tilde y)$ for the plain product and $N(\tilde x^{\natural}\tilde y)=N(\tilde x)N(\tilde y)$ for the quaternionic one, and a product of two positive numbers is not zero, so the left side cannot vanish when both factors are nonzero.

The proof is the **division property** of $\mathbb{H}$: every nonzero quaternion is invertible, equivalently the norm vanishes only at the origin. It is quoted from *Norm and Invertibility in the General Plain Algebra*, above this article in this category, and it is the one fact that separates this chapter from the biquaternion one.

## The Six Structures

The symmetric and antisymmetric parts of the two general products carry the same question and answer it differently:

| structure | product | zero divisors | example |
|---|---|---|---|
| GPA | $\tilde p\tilde q$ | none | — |
| GQA | $\tilde p^{\natural}\tilde q$ | none | — |
| SPA | $\tilde p\bullet\tilde q$ | yes | $e_1\bullet e_2=0$ |
| SQA | $\tfrac12(\tilde p^{\natural}\tilde q+\tilde q^{\natural}\tilde p)$ | yes | $e_1\star e_2=0$ |
| APA | $\tilde p\times\tilde q$ | yes | $e_1\times e_1=0$ |
| AQA | $\tfrac12(\tilde p^{\natural}\tilde q-\tilde q^{\natural}\tilde p)$ | yes | $e_1\star e_1=0$ |

- **SPA.** Writing $\tilde p\bullet\tilde q=\tfrac12(\tilde p\tilde q+\tilde q\tilde p)=\bigl(p_0q_0-\mathbf p\cdot\mathbf q\bigr)e_0+p_0\mathbf q+q_0\mathbf p$, two distinct axis units give $e_j\bullet e_k=\tfrac12(e_je_k+e_ke_j)=0$ for $j\neq k$, so the zero divisors are at least the orthogonal pure pairs. This is *Zero Divisors of the Symmetric Plain Algebra*, above this article in this category.
- **SQA.** The symmetrised quaternionic product is scalar valued, $p_0q_0+\mathbf p\cdot\mathbf q$, so any two elements with $p_0q_0=-\mathbf p\cdot\mathbf q$ are a zero-divisor pair; the pure orthogonal pairs are the simplest. This is *Zero Divisors of the Symmetric Quaternionic Algebra*.
- **APA and AQA.** Both products are alternating, $\tilde x\star\tilde x=0$; every nonzero element is therefore a two-sided zero divisor with itself as partner, so the zero-divisor set is the punctured space, and the pairs are the parallel pairs, with parallel vector parts in the plain case and the two elements scalar multiples of one another in the quaternionic one. These are *Zero Divisors of the Antisymmetric Plain Algebra* and *Zero Divisors of the Antisymmetric Quaternionic Algebra*.

Thus the two **general** products share the division property, and the passage to a symmetric or an antisymmetric part can create a zero divisor where the general product had none: the symmetrisation of two elements that commute with a sign, and the antisymmetrisation of any element with itself.

## Contrast with the Biquaternion Case

In the biquaternion chapter the four products share one large zero-divisor set, the isotropic cone of the complex norm, and a nonzero element of square zero is a zero divisor of every one of them. Over $\mathbb{R}$ there is no isotropic element of the definite norm, so the two general products have no zero divisor at all, and only the derived structures acquire one. The collapse from a cone to the empty set is the collapse of the four products to two read on this question, and it is the same fact as the divisibility of $\mathbb{H}$.

## Summary

The general plain and general quaternionic products have no zero divisor, by the division property of $\mathbb{H}$, which says that the norm vanishes only at zero and that every nonzero element is invertible. Among the six structures the two general ones keep that property, while the symmetric plain and symmetric quaternionic products acquire zero divisors from the orthogonal pure pairs, and the two antisymmetric products acquire all of them from alternation. In the biquaternion chapter the zero-divisor set is a cone shared by the four products; here it is empty for the general products and is created only by symmetrisation or antisymmetrisation.

## Summary of Notation

| symbol | meaning |
|---|---|
| zero divisor of $\star$ | a pair $\tilde x,\tilde y\neq0$ with $\tilde x\star\tilde y=0$ |
| $N$ | the quaternion norm, multiplicative and definite |
| GPA, GQA | the two general products, without zero divisors |
| SPA, SQA | the symmetrised structures, with zero divisors |
| APA, AQA | the alternating structures, total zero divisors |

## Further Reading

- *Norm and Invertibility in the General Plain Algebra* (`articles_maths/norm-and-invertibility-in-the-general-plain-algebra-of-quaternions.md`), for the division property.
- *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-6-algebraic-structures-over-the-quaternion-r-space.md`), for the six products.
- *Zero Divisors of the Symmetric Plain Algebra* (`articles_maths/zero-divisors-of-the-symmetric-plain-algebra-of-quaternions.md`), above this article in this category.
- *Zero Divisors of the Antisymmetric Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-antisymmetric-quaternionic-algebra-of-quaternions.md`), above this article in this category.
