# __The Annihilating Elements of the Two General Products__

## Introduction

An element annihilates a product when multiplying by it kills the product on the whole space. This article defines the left, the right and the two-sided annihilating set of each of the two general products, computes them, compares them, and reads the same question on the six structures the products generate. The answer for the two general products is the same in both cases: the scalar line is not special, and only $0$ annihilates. The products are *The Two General Products of the Quaternion $\mathbb{R}$ Space*, the six structures are *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, and the forms are *The 2 Forms over the Quaternion $\mathbb{R}$ Space*, all above this article in this category.

## The Annihilating Sets

**Definition.** For a product $\star$ on $\mathbb{H}$, the **left annihilating set** is
$$
\ell(\star)=\{\tilde x:\tilde x\star\tilde y=0\ \text{for every }\tilde y\} ,
$$
the **right annihilating set** is $r(\star)=\{\tilde x:\tilde y\star\tilde x=0\ \text{for every }\tilde y\}$, and the **two-sided** set is $\ell(\star)\cap r(\star)$.

The left annihilating set is the common kernel of the left multiplication operators $L_{\tilde y}$, and $\tilde x\in\ell(\star)$ exactly when the operator $L_{\tilde x}$ is zero. It is a subspace, and when $\star$ is commutative the two one-sided sets coincide. The **radical of the product** is the two-sided set when the product is read through its form; the radical of the form $\operatorname{Sc}(\tilde x\star\tilde y)$ is generally larger, and it is treated with the pairings in *The Two Pairings of the Quaternion Algebra*, below this article in this category.

## The Two General Products

**Theorem.** For the general plain product $\tilde p\tilde q$ and the general quaternionic product $\tilde p^{\natural}\tilde q$, both one-sided annihilating sets and the two-sided set are $\{0\}$.

**Proof.** For the plain product, $\tilde x\tilde y=0$ for every $\tilde y$ forces $\tilde x=0$, because every nonzero quaternion is invertible: multiply by $\tilde y=\tilde x^{-1}$ on the right. For the quaternionic product, put $\tilde y=e_0$, so that $\tilde x^{\natural}=\tilde x^{\natural}e_0=0$, whence $\tilde x=0$; the right set is empty except for $0$ in the same way. Since the two products agree in giving only $0$, the two-sided sets agree too.

The two computations use the same fact in two guises: the plain product is a division, and ${}^{\natural}$ is a bijection carrying $e_0$ nowhere but $e_0$; the quaternionic product is the plain product composed with an anti-involution of the first slot, so its left annihilating set is the image under ${}^{\natural}$ of the plain one, which is $\{0\}$.

**Consequence for the forms.** The annihilating set of the product is the radical of the product; it is not the radical of the associated form. The plain form $\operatorname{Sc}(\tilde p\tilde q)$ has radical the set of $\tilde x$ with $\operatorname{Sc}(\tilde x\tilde y)=0$ for every $\tilde y$, which is $0$ as well, since $\tilde y=e_0$ gives $\operatorname{Sc}(\tilde x)=x_0$ and $\tilde y=e_k$ gives $\operatorname{Sc}(\tilde x e_k)=-x_k$; the quaternion form $\operatorname{Sc}(\tilde p^{\natural}\tilde q)$ is definite, of radical $0$ by *The 2 Forms over the Quaternion $\mathbb{R}$ Space*. So product and form agree on the two general products, and both are as small as possible.

## The Six Structures

The symmetric and antisymmetric parts of the two general products carry the same question, and the answer is no longer always $\{0\}$. Writing $\bullet$ for the Jordan product $\tfrac12(\tilde p\tilde q+\tilde q\tilde p)$ and $\times$ for the cross product $\tfrac12(\tilde p\tilde q-\tilde q\tilde p)$, and reading *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*:

| structure | product | left annihilating set | reason |
|---|---|---|---|
| GPA | $\tilde p\tilde q$ | $\{0\}$ | division |
| GQA | $\tilde p^{\natural}\tilde q$ | $\{0\}$ | test $\tilde y=e_0$ |
| SPA | $\tilde p\bullet\tilde q$ | $\{0\}$ | test $\tilde y=e_0$ |
| SQA | $\tfrac12(\tilde p^{\natural}\tilde q+\tilde q^{\natural}\tilde p)$ | $\{0\}$ | the diagonal $\tilde y=e_\mu$ reads $x_\mu$ |
| APA | $\tilde p\times\tilde q$ | $\mathbb{R}_{\mathbb{H}}$ | the centre commutes, so scalars annihilate |
| AQA | $\tfrac12(\tilde p^{\natural}\tilde q-\tilde q^{\natural}\tilde p)$ | $\{0\}$ | $\tilde y=e_0$ forces $\tilde x$ real, and then $\tilde y=e_1$ kills it |

The six structures give the annihilating sets their character requires, and the only non-trivial one is that of the cross product, where the set is the scalar line: the **centre** of $\mathbb{H}$ read through the commutator, of dimension one, since a scalar commutes with every element. The centre of the Lie algebra $\mathrm{Vect}(\mathbb{H})$ under the cross product is smaller still, $\{0\}$: no axis line commutes with the whole vector subspace. The antisymmetrised quaternionic product is alternating and its annihilating set is nevertheless $\{0\}$, because its first slot carries the anti-involution: the scalar line, which annihilates the plain cross product, does not annihilate this one, since $e_0\star\tilde q=\tfrac12(\tilde q-\tilde q^{\natural})$ is the vector part of $\tilde q$ and does not vanish identically; the real elements that survive the test $\tilde y=e_0$ are then killed by $\tilde y=e_1$. The failure of the Jacobi identity of *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* and the vanishing of this annihilating set are two faces of the same absence of a central direction.

## Contrast with the Biquaternion Case

In the biquaternion chapter the annihilating sets and the radicals are large: a product there can kill a half of the algebra, because $\mathbb{B}$ has zero divisors and its forms have isotropic cones. Over $\mathbb{R}$ the division property forbids this, and the annihilating sets of the two general products are the two smallest possible, each $\{0\}$. The difference is the difference between a division algebra and a split one, and it is the reason the synthesis of this block is short.

## Summary

The left, right and two-sided annihilating sets of both general products are $\{0\}$, by the division property of the plain product and by the anti-involution of the quaternionic one. The same sets are $\{0\}$ for the two symmetrised structures, and the only exception among the six is the cross product, whose annihilating set is the scalar line, the centre of the algebra. The radicals of the two forms are $\{0\}$ as well, so product and form agree. In the biquaternion chapter the same sets are large, because the split algebra loses the division property; here they are as small as they can be.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\ell(\star)$, $r(\star)$ | left and right annihilating sets of the product $\star$ |
| $\ell\cap r$ | the two-sided annihilating set, the radical of the product |
| $\{0\}$ | the value for the general plain and general quaternionic products |
| $\mathbb{R}_{\mathbb{H}}$ | the annihilating set of the cross product, the centre of the algebra |
| GPA, GQA, SPA, SQA, APA, AQA | the six structures of *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* |

## Further Reading

- *The Two General Products of the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-two-general-products-of-the-quaternion-r-space.md`), for the products.
- *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-6-algebraic-structures-over-the-quaternion-r-space.md`), for the six structures and their names.
- *The Two Pairings of the Quaternion Algebra* (`articles_maths/the-two-pairings-of-the-quaternion-algebra.md`), below this article in this category, for the radicals of the forms.
- *The Zero Divisors and the Two General Products* (`articles_maths/the-zero-divisors-and-the-two-general-products.md`), below this article in this category, for the companion question of the zero divisors.
