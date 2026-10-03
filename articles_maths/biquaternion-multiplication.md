# __Biquaternion Multiplication__

## Introduction

This article defines the **product** of two biquaternions and studies the two halves into which it splits. The product of $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is the complex-linear extension of the quaternion product. It is associative and unital; it is not commutative, and its failure of commutativity is not arbitrary, because the antisymmetric part of the product is the complex cross product of the two vector parts.

The product of two biquaternions always splits into a symmetric and an antisymmetric part, and the two parts are of different kinds, defined and studied in turn below. The antisymmetric part is a **pure vector**. The symmetric part carries all of the scalar and the mixed scalar–vector terms, and it makes the Hermitian subspace a Jordan algebra.

The article assumes the elements, the basis and the conjugations from *Biquaternion Algebra* and *Different Ways to Consider Biquaternions*, and it defines no form. The behaviour of the product and of its two parts on each of the six subspaces is tabulated in *Biquaternion Relations Between Subspaces*; the Lie algebra carried by the antisymmetric part is *Biquaternion Lie Algebra*; the operators $L_{\tilde{P}}$ and $R_{\tilde{P}}$ are *The Enveloping Algebra of the Biquaternion Algebra and the Bi-module Structure*; and the basis products written out one by one are *Worked Examples in the Biquaternion Algebra*.

Throughout, the product of two elements is written by juxtaposition, $\tilde{P}\tilde{Q}$, and $\tilde{P}=P_0+\mathbf{P}$ separates the complex scalar part $P_0$ from the complex vector part $\mathbf{P}=P_1e_1+P_2e_2+P_3e_3$.

## The Product

### Definition

The **biquaternion product** is the $\mathbb{C}$-bilinear extension of the quaternion product of the units:

$$
e_1e_2 = e_3, \qquad e_2e_3 = e_1, \qquad e_3e_1 = e_2, \qquad e_1^2 = e_2^2 = e_3^2 = -e_0,
$$

with central scalar imaginary $i$, $i^2=-1$. In developed form the product of $\tilde{P}=\sum_\mu P_\mu e_\mu$ and $\tilde{Q}=\sum_\nu Q_\nu e_\nu$ is

$$
\tilde{P}\tilde{Q} = \sum_{\mu=0}^{3}\sum_{\nu=0}^{3} P_\mu Q_\nu \, e_\mu e_\nu .
$$

The product is $\mathbb{C}$-bilinear, associative and unital, with unit $e_0$; it is not commutative. The unit relations above are those of *Biquaternion Algebra* and of the quaternion algebra, extended complex-linearly.

### The Scalar–Vector Form

Write $\tilde{P}=P_0+\mathbf{P}$ and $\tilde{Q}=Q_0+\mathbf{Q}$. Expanding the product on the scalar and vector parts of the two factors, the scalar parts contribute scalars, the two mixed products contribute vectors, and the product of the two vector parts is again a sum of a scalar and a vector. The result is

$$
\tilde{P}\tilde{Q} = P_0Q_0 - (\mathbf{P},\mathbf{Q}) + P_0\mathbf{Q} + Q_0\mathbf{P} + \mathbf{P}\times\mathbf{Q} ,
$$

where

$$
(\mathbf{P},\mathbf{Q}) = \sum_{k=1}^{3} P_kQ_k , \qquad
\mathbf{P}\times\mathbf{Q} = (P_2Q_3-P_3Q_2)e_1 + (P_3Q_1-P_1Q_3)e_2 + (P_1Q_2-P_2Q_1)e_3 .
$$

The two pairings are the **complex bilinear dot product** and the **complex bilinear cross product**. They are $\mathbb{C}$-bilinear, and they reduce to the ordinary dot and cross products when the coefficients are real. The formula has the same shape as the quaternion product — a scalar part, a mixed vector part and a cross-product vector part — with the single difference that the coefficients are complex.

## The Symmetric Part

### Definition

The **symmetric part**, also called the **symmetrized product** or the **Jordan product**, of two biquaternions is

$$
\tilde{P}\bullet\tilde{Q} := \tfrac{1}{2}\bigl(\tilde{P}\tilde{Q}+\tilde{Q}\tilde{P}\bigr).
$$

In scalar–vector notation the antisymmetric terms of the product cancel and the mixed terms double:

$$
\tilde{P}\bullet\tilde{Q} = \bigl(P_0Q_0-(\mathbf{P},\mathbf{Q})\bigr) + P_0\mathbf{Q} + Q_0\mathbf{P} .
$$

The symmetrized product is commutative and $\mathbb{C}$-bilinear, and it agrees with the ordinary square on the diagonal:

$$
\tilde{P}\bullet\tilde{Q} = \tilde{Q}\bullet\tilde{P} , \qquad \tilde{P}\bullet\tilde{P} = \tilde{P}^2 .
$$

### It Is the Polarisation of the Square

**Proposition.** The symmetrized product is the polarisation of the square:

$$
\tilde{P}\bullet\tilde{Q} = \tfrac{1}{2}\Bigl((\tilde{P}+\tilde{Q})^2 - \tilde{P}^2 - \tilde{Q}^2\Bigr).
$$

**Proof.** Expand $(\tilde{P}+\tilde{Q})^2=\tilde{P}^2+\tilde{P}\tilde{Q}+\tilde{Q}\tilde{P}+\tilde{Q}^2$ by bilinearity and divide by two.

The identity is the reason the symmetrized product, not the full product, is the product of the square: $\tilde{P}\bullet\tilde{P}=\tilde{P}^2$, and the symmetric part of $\tilde{P}\tilde{Q}$ is exactly the term that a squaring process can see. Directly,

$$
\tilde{P}^2 = \bigl(P_0^2-(\mathbf{P},\mathbf{P})\bigr) + 2P_0\mathbf{P} ,
$$

which is a scalar plus a scalar multiple of $\mathbf{P}$ and contains no cross-product term. Every square-root problem $\xi^2=\tilde{Q}$ is therefore a problem in the symmetric part alone, and the outer product plays no part in *Biquaternion Square Roots of Minus One, Zero and Plus One* and *Biquaternion Square Roots of a General Element*.

### It Is a Jordan Product

**Theorem.** With the product $\bullet$, the algebra $\mathbb{B}$ is a commutative Jordan algebra: $\bullet$ is commutative and bilinear, and the Jordan identity

$$
(\tilde{P}\bullet\tilde{Q})\bullet\tilde{P}^2 = \tilde{P}\bullet\bigl(\tilde{Q}\bullet\tilde{P}^2\bigr)
$$

holds for all $\tilde{P},\tilde{Q}$.

**Proof.** The product of an associative algebra satisfies the Jordan identity for the symmetrized product, by the associativity of the underlying product; commutativity and bilinearity are built into the definition. The general theory is *Jordan Algebras*.

Two consequences follow. First, the Hermitian subspace $\mathbb{M}_+$ is closed under $\bullet$: for $\tilde{P},\tilde{Q}\in\mathbb{M}_+$ the product $\tilde{P}\bullet\tilde{Q}$ is again Hermitian, so $\mathbb{M}_+$ is a Jordan subalgebra of $\mathbb{B}$. Second, the symmetrized product carries the same scalar part as the product itself,

$$
\mathrm{Sc}(\tilde{P}\bullet\tilde{Q}) = \mathrm{Sc}(\tilde{P}\tilde{Q}) = P_0Q_0-(\mathbf{P},\mathbf{Q}),
$$

since the antisymmetric part has no scalar part.

## The Antisymmetric Part

### Definition

The **antisymmetric part** of the product, or **outer product**, is

$$
\tilde{P}\wedge\tilde{Q} := \tfrac{1}{2}\bigl(\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P}\bigr).
$$

In scalar–vector notation the scalar parts cancel and the mixed terms too, leaving the cross product of the vector parts:

$$
\tilde{P}\wedge\tilde{Q} = \mathbf{P}\times\mathbf{Q} .
$$

The outer product is **alternating** and $\mathbb{C}$-bilinear, and it is skew:

$$
\tilde{P}\wedge\tilde{P} = 0 , \qquad \tilde{P}\wedge\tilde{Q} = -\,\tilde{Q}\wedge\tilde{P} .
$$

Its value is a pure vector: the scalar part of $\tilde{P}\wedge\tilde{Q}$ vanishes, for every pair of biquaternions, not only for vector-like ones.

### The Commutativity Criterion

Because the right-hand side of the outer product depends on the vector parts alone, the vanishing of the antisymmetric part is a criterion:

$$
\tilde{P}\tilde{Q} = \tilde{Q}\tilde{P} \quad\Longleftrightarrow\quad \mathbf{P}\times\mathbf{Q} = 0 .
$$

The cross product of two complex vectors vanishes exactly when the vectors are **linearly dependent**, so two biquaternions commute if and only if their vector parts are parallel. In particular a central element $\tilde{P}=P_0e_0$ commutes with every biquaternion, since its vector part is zero; the converse holds, so this recovers the centre $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ as the set of elements that commute with all of $\mathbb{B}$.

### The Closure of the Two Sectors

The two halves of the product behave differently with respect to the Hermitian split, and the pattern is worth recording here because it is the origin of the Lie and Jordan structures of the algebra.

| $\tilde{P},\tilde{Q}$ | $\tilde{P}\wedge\tilde{Q}$ | $\tilde{P}\bullet\tilde{Q}$ |
|---|---|---|
| $\mathbb{M}_+$ (Hermitian) | lies in $\mathbb{M}_-$ | lies in $\mathbb{M}_+$ |
| $\mathbb{M}_-$ (anti-Hermitian) | lies in $\mathbb{M}_-$ | lies in $\mathbb{M}_+$ |

That is, the antisymmetric part closes on the anti-Hermitian subspace and carries the Hermitian one into it, so $\mathbb{M}_-$ is a Lie subalgebra; the symmetric part closes on the Hermitian subspace, so $\mathbb{M}_+$ is a Jordan subalgebra. The full subspace-by-subspace table, with the centre, the vector subspace, the quaternion subspace and the anti-quaternion subspace, is *Biquaternion Relations Between Subspaces*.

## The Two Parts Together

### The Split Is by Symmetry, Not by Grade

The product is the sum of its two halves,

$$
\tilde{P}\tilde{Q} = \tilde{P}\bullet\tilde{Q} + \tilde{P}\wedge\tilde{Q} ,
$$

and the two halves are read in coordinates as

| part | scalar part | vector part | symmetry |
|---|---|---|---|
| $\tilde{P}\bullet\tilde{Q}$ | $P_0Q_0-(\mathbf{P},\mathbf{Q})$ | $P_0\mathbf{Q}+Q_0\mathbf{P}$ | symmetric, $\tilde{P}\bullet\tilde{Q}=\tilde{Q}\bullet\tilde{P}$ |
| $\tilde{P}\wedge\tilde{Q}$ | $0$ | $\mathbf{P}\times\mathbf{Q}$ | antisymmetric, $\tilde{P}\wedge\tilde{Q}=-\tilde{Q}\wedge\tilde{P}$ |

The antisymmetric part is pure vector and the symmetric part carries the scalar plus the mixed terms.

### The Operator Reading

The two halves are the balanced and the unbalanced one-sided multiplications. With $L_{\tilde{P}}(\tilde{Q})=\tilde{P}\tilde{Q}$ and $R_{\tilde{P}}(\tilde{Q})=\tilde{Q}\tilde{P}$ the left and right multiplications by $\tilde{P}$,

$$
\tilde{P}\bullet\tilde{Q} = \tfrac{1}{2}\bigl(L_{\tilde{P}}+R_{\tilde{P}}\bigr)(\tilde{Q}) , \qquad \tilde{P}\wedge\tilde{Q} = \tfrac{1}{2}\bigl(L_{\tilde{P}}-R_{\tilde{P}}\bigr)(\tilde{Q}) .
$$

The antisymmetric combination $L_{\tilde{P}}-R_{\tilde{P}}$ is the inner derivation of the algebra, so the outer product is the derivation up to the factor $\tfrac12$, and the symmetric combination $L_{\tilde{P}}+R_{\tilde{P}}$ is twice the symmetrized multiplication by $\tilde{P}$. The operators themselves are *The Enveloping Algebra of the Biquaternion Algebra and the Bi-module Structure*.

### Worked Example

Take $\tilde{P}=e_0+e_1$ and $\tilde{Q}=e_2$, so that $P_0=1$, $\mathbf{P}=e_1$, $Q_0=0$ and $\mathbf{Q}=e_2$. The dot product vanishes, $(\mathbf{P},\mathbf{Q})=0$, and the cross product is $\mathbf{P}\times\mathbf{Q}=e_1\times e_2=e_3$. Hence

$$
\tilde{P}\bullet\tilde{Q} = (1\cdot 0-0)+1\cdot e_2+0\cdot e_1 = e_2 , \qquad \tilde{P}\wedge\tilde{Q} = e_3 , \qquad \tilde{P}\tilde{Q} = e_2+e_3 .
$$

Interchanging the factors changes the sign of the outer product and leaves the symmetric part unchanged,

$$
\tilde{Q}\tilde{P} = e_2-e_3 , \qquad \tilde{Q}\bullet\tilde{P} = e_2 , \qquad \tilde{Q}\wedge\tilde{P} = -e_3 ,
$$

so $\tilde{P}\tilde{Q}\neq \tilde{Q}\tilde{P}$ while $\tilde{P}\tilde{Q}+\tilde{Q}\tilde{P} = 2e_2 = 2(\tilde{P}\bullet\tilde{Q})$, and the difference is $\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P}=2e_3=2(\tilde{P}\wedge\tilde{Q})$, in agreement with the identities above.

## Summary

The biquaternion product is the complex-linear extension of the quaternion product; it is associative and unital, and not commutative. It always splits into a symmetric and an antisymmetric part,

$$
\tilde{P}\tilde{Q} = \tilde{P}\bullet\tilde{Q} + \tilde{P}\wedge\tilde{Q} , \qquad \tilde{P}\bullet\tilde{Q} = \tfrac{1}{2}(\tilde{P}\tilde{Q}+\tilde{Q}\tilde{P}) , \qquad \tilde{P}\wedge\tilde{Q} = \tfrac{1}{2}(\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P}) .
$$

The **antisymmetric part** is the complex cross product of the vector parts, $\tilde{P}\wedge\tilde{Q}=\mathbf{P}\times\mathbf{Q}$; it is alternating, pure vector, and vanishes exactly when the vector parts are linearly dependent, which is the commutativity criterion.

The **symmetric part** is $\mathbb{C}$-bilinear and commutative, it agrees with the square on the diagonal, $\tilde{P}\bullet\tilde{P}=\tilde{P}^2$, and it is the polarisation of the square, $\tilde{P}\bullet\tilde{Q}=\tfrac{1}{2}((\tilde{P}+\tilde{Q})^2-\tilde{P}^2-\tilde{Q}^2)$. It makes $\mathbb{B}$ a Jordan algebra; it has the same scalar part as the product, $\mathrm{Sc}(\tilde{P}\bullet\tilde{Q})=\mathrm{Sc}(\tilde{P}\tilde{Q})=P_0Q_0-(\mathbf{P},\mathbf{Q})$; it contains all the powers and hence all the square-root problems; and it closes on the Hermitian subspace, which is a Jordan subalgebra. The antisymmetric part closes on the anti-Hermitian subspace, which is a Lie subalgebra.

Read on the operators, the symmetric part is the balanced multiplication $\tfrac{1}{2}(L_{\tilde{P}}+R_{\tilde{P}})$ and the antisymmetric part the derivation $\tfrac{1}{2}(L_{\tilde{P}}-R_{\tilde{P}})$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde{P}\tilde{Q}$ | the biquaternion product |
| $\tilde{P}=P_0+\mathbf{P}$ | scalar part plus vector part |
| $(\mathbf{P},\mathbf{Q})$ | the complex bilinear dot product, $\sum_k P_kQ_k$ |
| $\mathbf{P}\times\mathbf{Q}$ | the complex bilinear cross product |
| $\tilde{P}\bullet\tilde{Q}=\tfrac{1}{2}(\tilde{P}\tilde{Q}+\tilde{Q}\tilde{P})$ | the symmetric or symmetrized (Jordan) product |
| $\tilde{P}\wedge\tilde{Q}=\tfrac{1}{2}(\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P})$ | the antisymmetric part, or outer product |
| $L_{\tilde{P}}$, $R_{\tilde{P}}$ | left and right multiplications by $\tilde{P}$ |
| $\mathrm{Sc}$ | the scalar part of an element |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original product that is extended here.
