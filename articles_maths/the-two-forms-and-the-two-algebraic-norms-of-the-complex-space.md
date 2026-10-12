# __The Two Forms and the Two Algebraic Norms of the Complex Space__

## Introduction

The two products of the complex space carry two **forms**, and their algebraic norms are the two **algebraic norms**. This article defines the two forms, separates them, reads the two norms, and states its one distinctive feature: a single function is both definite and multiplicative.

The two forms are the scalar parts of the two general products, and the two products and their collapse are *The Two Products of the Complex Space*. The topological norm $|\cdot|=\sqrt{H}$, its multiplicativity, the invertibility criterion and the group of units are owned by *Complex Norm and Invertibility*, below this article in this category, and are named here and not developed.

**Conventions.** **Bar** is complex conjugation and the **Hermitian** mark is the bar, ${}^{*}=\bar{\cdot}$. Elements are written $A$ and $C$, and $B$ is not used for an element: $B$, $N$, $H$, $K$ are the four forms, of which $B$ and $H$ survive here. The letter $N$ is read with care: *Complex Norm and Invertibility*, below this article in this category, writes the positive definite norm as $N(A)=A\bar A$, which is the algebraic norm of $H$. The two readings are told apart by their argument count and by their chapter.

## The Two Forms

The **form** of a product is its scalar part, a function of two elements. On the complex space, read over itself, there is no vector direction, so the scalar part of a product is the product, and the two forms are

$$
B(A,C)=AC,\qquad H(A,C)=A\bar C .
$$

The forms collapse to these two in the first slot alone:

The settings with the identity in the second slot name the bilinear product, and those with the Hermitian conjugation the sesquilinear one; the first slot carries the identity here, so each pair gives one product, and hence one form. The count of the forms on $\mathbb{C}$ is therefore two, and the two are distinct as functions of a pair, since $B(A,C)$ and $H(A,C)$ differ as soon as the second element is not real. The complex space is one-dimensional over itself, so the Gram matrix of a form in the basis $1$ is the $1\times1$ matrix of its value on the unit, and both forms have the Gram matrix $[1]$, since $B(1,1)=H(1,1)=1$. The Gram matrix therefore does not separate the two forms here, and the separation is by their symmetry.

## The Two Forms Are Separated by Their Symmetry

The two forms carry two symmetries. The form $B$ is **symmetric**,

$$
B(A,C)=AC=CA=B(C,A),
$$

because the field is commutative. The form $H$ is **conjugate-symmetric**,

$$
H(A,C)=A\bar C=\overline{C\bar A}=\overline{H(C,A)},
$$

and it is symmetric exactly on the real subspace, when the bar fixes both arguments. The two forms of the complex space are therefore told apart by their symmetry alone, $B$ symmetric against $H$ conjugate-symmetric, and not by their Gram matrix, which is $[1]$ for both. The complex reading has no second separator, since the sign vector $\varepsilon=(1)$ on a one-dimensional space is the identity.

## The Two Algebraic Norms

The **algebraic norm** of a form is its algebraic norm, the form read at equal arguments. The two forms therefore give two algebraic norms,

$$
B(A)=B(A,A)=A^{2},\qquad H(A)=H(A,A)=A\bar A=|A|^{2},
$$

the square and the squared modulus of the element. So the complex space carries two norms and no more.

Both norms are **multiplicative**: $B(AC)=(AC)^{2}=A^{2}C^{2}=B(A)B(C)$, and $H(AC)=|AC|^{2}=|A|^{2}|C|^{2}=H(A)H(C)$. The two differ in value and in definiteness. The value of $H$ is real and positive definite, $H(A)=|A|^{2}>0$ for $A\neq0$; the value of $B$ is complex and **anisotropic**, $B(A)=A^{2}=0$ only for $A=0$, so the algebraic norm of $B$ never vanishes off the origin, and its real part, $a^{2}-a'^{2}$, is indefinite. The anisotropy of $B$ over $\mathbb{C}$ and the indefiniteness of its realification are not in contradiction: the first is read on the complex values, which vanish only together with $A$, and the second on the real part alone, which changes sign.

| form | the algebraic norm | value | symmetric | conjugate-symmetric | Gram matrix | realified signature |
|---|---|---|---|---|---|---|
| $B$ | $B(A)=A^{2}$ | complex, anisotropic | yes | no | $[1]$ | $(1,1)$ |
| $H$ | $H(A)=|A|^{2}$ | real, positive definite | no | yes | $[1]$ | $(2,0)$ |

The realified signatures are those of the two rules of the passage to the real reading, the split signature $(n,n)$ for a bilinear form and the doubled inertia for a Hermitian one, applied at $n=1$; the construction and its rules are *The Realification and the Effect of the Change of Scalars*, below this article in this category.

## Definite and Multiplicative Together

**On the complex space one and the same function is both**: $H(A)=|A|^{2}$ is real, positive definite, and multiplicative. The anisotropy of $H$ is the absence of zero divisors, since $H(A)=0$ forces $A=0$, and its multiplicativity is the multiplicativity of the modulus.

The two properties are therefore joined here. A definite function is nonzero off the origin, while a multiplicative one takes the value $0$ on a product only if it takes the value $0$ on a factor; a pair of nonzero elements with vanishing product would forbid the two properties in one function, and $\mathbb{C}$ has no such pair. It therefore exhibits the definite multiplicative $H$. The norm $H$, its multiplicativity, the criterion of invertibility $A\neq0$ and the group of units $\mathbb{C}^{\times}$ are read in *Complex Norm and Invertibility*, below this article in this category.

## Summary

The two products of the complex space carry two forms, $B(A,C)=AC$ and $H(A,C)=A\bar C$, the collapse of the four forms $B$, $N$, $H$, $K$ to the two settings of the second slot; the four products and forms become two, $B=N$ and $H=K$. The two forms have the same Gram matrix $[1]$ over $\mathbb{C}$ and are separated by their symmetry alone, $B$ symmetric and $H$ conjugate-symmetric. Their algebraic norms are $B(A)=A^{2}$, complex and anisotropic, and $H(A)=|A|^{2}$, real and positive definite; both are multiplicative. One and the same function $H$ is both definite and multiplicative.

## Summary of Notation

| symbol | meaning |
|---|---|
| $A$, $C$ | elements of the space |
| $H(A,C)=A\bar C$ | the general plain sesquilinear or Hermitian form, equal to the Krein form $K$ |
| $B(A)=A^{2}$ | the plain bilinear algebraic norm |
| $H(A)=A\bar A=|A|^{2}$ | the Hermitian algebraic norm, real and positive definite |
| $\bar{\cdot}$ | complex conjugation, the bar |
| $[1]$ | the Gram matrix of each form in the complex basis $(1)$ |
| $(1,1)$, $(2,0)$ | the realified signatures of $B$ and of $H$ |

## Further Reading

- *The Two Products of the Complex Space*, for the two products whose scalar parts the two forms are.
- *Relations and Comparison Between the Two Products*, for the two products set against each other.
- *Complex Norm and Invertibility* (`articles_maths/complex-norm-and-invertibility.md`), below this article in this category, for the topological norm $|\cdot|=\sqrt{H}$, its multiplicativity, the invertibility criterion and the group of units.
- *The Realification and the Effect of the Change of Scalars*, below this article in this category, for the two rules that give the realified signatures $(1,1)$ and $(2,0)$.
