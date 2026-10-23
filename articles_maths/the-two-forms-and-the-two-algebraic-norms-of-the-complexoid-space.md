# __The Two Forms and the Two Algebraic Norms of the Complexoid Space__

## Introduction

The two products of the complex space carry two **forms**, and their algebraic norms are the two **algebraic norms**. This article defines the two forms, separates them, reads the two norms, and states its one distinctive feature: a single function is both definite and multiplicative.

The two forms are the scalar parts of the two general products, and the two products and their collapse are *The Two Products of the Complexoid Space*. The topological norm $\sqrt{\langle\cdot\rangle_{*}}$, its multiplicativity, the invertibility criterion and the group of units are owned by *Complex Norm and Invertibility*, below this article in this category, and are named here and not developed.

## The Two Forms

The **form** of a product is its scalar part, a function of two elements. On the complex space, read over itself, there is no vector direction, so the scalar part of a product is the product, and the two forms are

$$
\langle Q_1,Q_2\rangle=Q_1Q_2,\qquad \langle Q_1,Q_2\rangle_{*}=Q_1\bar Q_2 .
$$

The forms collapse to these two in the first slot alone. The settings with the identity in the second slot name the bilinear product, and those with the Hermitian conjugation the sesquilinear one; the first slot carries the identity here, so each pair gives one product, and hence one form. The count of the forms on $\mathbb{C}$ is therefore two, and the two are distinct as functions of a pair, since $\langle Q_1,Q_2\rangle$ and $\langle Q_1,Q_2\rangle_{*}$ differ as soon as the second element is not real. The complex space is one-dimensional over itself, so the Gram matrix of a form in the basis $1$ is the $1\times1$ matrix of its value on the unit, and both forms have the Gram matrix $[1]$, since $\langle 1,1\rangle=\langle 1,1\rangle_{*}=1$. The Gram matrix therefore does not separate the two forms here, and the separation is by their symmetry.

## The Two Forms Are Separated by Their Symmetry

The two forms carry two symmetries. The form $\langle\cdot,\cdot\rangle$ is **symmetric**,

$$
\boxed{\;\langle Q_1,Q_2\rangle=Q_1Q_2=Q_2Q_1=\langle Q_2,Q_1\rangle\;},
$$

because the field is commutative. The form $\langle\cdot,\cdot\rangle_{*}$ is **conjugate-symmetric**,

$$
\boxed{\;\langle Q_1,Q_2\rangle_{*}=Q_1\bar Q_2=\overline{Q_2\bar Q_1}=\overline{\langle Q_2,Q_1\rangle_{*}}\;},
$$

and it is symmetric exactly on the real subspace, when the bar fixes both arguments. The two forms of the complex space are therefore told apart by their symmetry alone, $\langle\cdot,\cdot\rangle$ symmetric against $\langle\cdot,\cdot\rangle_{*}$ conjugate-symmetric, and not by their Gram matrix, which is $[1]$ for both. The complex reading has no second separator, since the sign vector $\varepsilon=(1)$ on a one-dimensional space is the identity.

## The Two Algebraic Norms

The **algebraic norm** of a form is the form read at equal arguments. The two forms therefore give two algebraic norms,

$$
\boxed{\;\langle Q\rangle=\langle Q,Q\rangle=Q^{2},\qquad \langle Q\rangle_{*}=\langle Q,Q\rangle_{*}=Q\bar Q=q^{2}+q'^{2}\;},
$$

the square and the squared Euclidean norm of the element. So the complex space carries two norms and no more.

Both norms are **multiplicative**: $\langle Q_1Q_2\rangle=(Q_1Q_2)^{2}=Q_1^{2}Q_2^{2}=\langle Q_1\rangle\langle Q_2\rangle$, and $\langle Q_1Q_2\rangle_{*}=Q_1Q_2\overline{Q_1Q_2}=(Q_1\bar Q_1)(Q_2\bar Q_2)=\langle Q_1\rangle_{*}\langle Q_2\rangle_{*}$. The two differ in value and in definiteness. The value of $\langle\cdot,\cdot\rangle_{*}$ is real and positive definite, $\langle Q\rangle_{*}=q^{2}+q'^{2}>0$ for $Q\neq0$; the value of $\langle\cdot,\cdot\rangle$ is complex and **anisotropic**, $\langle Q\rangle=Q^{2}=0$ only for $Q=0$, so the algebraic norm of $\langle\cdot\rangle$ never vanishes off the origin, and its real part, $q^{2}-q'^{2}$, is indefinite. The anisotropy of $\langle\cdot\rangle$ over $\mathbb{C}$ and the indefiniteness of its realification are not in contradiction: the first is read on the complex values, which vanish only together with $Q$, and the second on the real part alone, which changes sign.

| form | the algebraic norm | value | symmetric | conjugate-symmetric | Gram matrix | realified signature |
|---|---|---|---|---|---|---|
| $\langle\cdot\rangle$ | $\langle Q\rangle=Q^{2}$ | complex, anisotropic | yes | no | $[1]$ | $(1,1)$ |
| $\langle\cdot,\cdot\rangle_{*}$ | $\langle Q\rangle_{*}=q^{2}+q'^{2}$ | real, positive definite | no | yes | $[1]$ | $(2,0)$ |

The realified signatures are those of the two rules of the passage to the real reading, the split signature $(n,n)$ for a bilinear form and the doubled inertia for a Hermitian one, applied at $n=1$; the construction and its rules are *The Realification and the Effect of the Change of Scalars*, below this article in this category.

## Definite and Multiplicative Together

**On the complex space one and the same function is both**: $\langle Q\rangle_{*}=q^{2}+q'^{2}$ is real, positive definite, and multiplicative. The anisotropy of $\langle\cdot,\cdot\rangle_{*}$ is the absence of zero divisors, since $\langle Q\rangle_{*}=0$ forces $Q=0$, and its multiplicativity is the multiplicativity of the norm.

The two properties are therefore joined here. A definite function is nonzero off the origin, while a multiplicative one takes the value $0$ on a product only if it takes the value $0$ on a factor; a pair of nonzero elements with vanishing product would forbid the two properties in one function, and $\mathbb{C}$ has no such pair. It therefore exhibits the definite multiplicative $\langle\cdot\rangle_{*}$. The norm $\langle\cdot\rangle_{*}$, its multiplicativity, the criterion of invertibility $Q\neq0$ and the group of units $\mathbb{C}^{\times}$ are read in *Complex Norm and Invertibility*, below this article in this category.

## Summary

The two products of the complex space carry two forms, $\langle Q_1,Q_2\rangle=Q_1Q_2$ and $\langle Q_1,Q_2\rangle_{*}=Q_1\bar Q_2$, the collapse of the four forms $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{\natural}$, $\langle\cdot,\cdot\rangle_{*}$, $\langle\cdot,\cdot\rangle_{\natural*}$ to the two settings of the second slot; the four products and forms become two, $\langle\cdot,\cdot\rangle=\langle\cdot,\cdot\rangle_{\natural}$ and $\langle\cdot,\cdot\rangle_{*}=\langle\cdot,\cdot\rangle_{\natural*}$. The two forms have the same Gram matrix $[1]$ over $\mathbb{C}$ and are separated by their symmetry alone, $\langle\cdot,\cdot\rangle$ symmetric and $\langle\cdot,\cdot\rangle_{*}$ conjugate-symmetric. Their algebraic norms are $\langle Q\rangle=Q^{2}$, complex and anisotropic, and $\langle Q\rangle_{*}=q^{2}+q'^{2}$, real and positive definite; both are multiplicative. One and the same function $\langle\cdot,\cdot\rangle_{*}$ is both definite and multiplicative.

## Summary of Notation

| symbol | meaning |
|---|---|
| $Q_1$, $Q_2$ | elements of the space |
| $\langle Q_1,Q_2\rangle_{*}=Q_1\bar Q_2$ | the general plain sesquilinear or Hermitian form, equal to the Krein form $\langle\cdot,\cdot\rangle_{\natural*}$ |
| $\langle Q\rangle=Q^{2}$ | the plain bilinear algebraic norm |
| $\langle Q\rangle_{*}=Q\bar Q=q^{2}+q'^{2}$ | the Hermitian algebraic norm, real and positive definite |
| $\bar{\cdot}$ | complex conjugation, the bar |
| $[1]$ | the Gram matrix of each form in the complex basis $(1)$ |
| $(1,1)$, $(2,0)$ | the realified signatures of $\langle\cdot,\cdot\rangle$ and of $\langle\cdot,\cdot\rangle_{*}$ |

## Further Reading

- [The Two Products of the Complexoid Space](the-two-products-of-the-complexoid-space.html), for the two products whose scalar parts the two forms are.
- [Relations and Comparison Between the Two Products](relations-and-comparison-between-the-two-products.html), for the two products set against each other.
- [Complex Norm and Invertibility](complex-norm-and-invertibility.html), below this article in this category, for the topological norm $|\cdot|=\sqrt{\langle\cdot\rangle_{*}}$, its multiplicativity, the invertibility criterion and the group of units.
- [The Realification and the Effect of the Change of Scalars](the-realification-and-the-effect-of-the-change-of-scalars-on-the-complexoid.html), below this article in this category, for the two rules that give the realified signatures $(1,1)$ and $(2,0)$.
