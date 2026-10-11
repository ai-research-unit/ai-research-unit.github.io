# __The Two Forms and the Two Algebraic Norms of the Complex Space__

## Introduction

The two products of the complex space carry two **forms**, and their diagonals are the two **algebraic norms**. This article defines the two forms, separates them, reads the two norms, and states the one feature that distinguishes the complex reading from the biquaternion one: on $\mathbb{C}$ a single function is both definite and multiplicative.

The two forms are the reading on $\mathbb{C}$ of the four forms $B$, $N$, $H$, $K$ of the biquaternion algebra, which are the four scalar parts of the four general products and are counted and defined in *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*; their diagonals are the four algebraic norms of *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*. The two products whose scalar parts they are, and the collapse of the four products to them, are *The Two Products of the Complex Space*. The topological norm $|\cdot|=\sqrt{H}$, its multiplicativity, the invertibility criterion and the group of units are owned by *Complex Norm and Invertibility*, below this article in this category, and are named here and not developed.

**Conventions.** **Bar** is complex conjugation, the **natural sign** is the identity on the commutative base, and the **Hermitian** mark is the bar, ${}^{*}=\bar{\cdot}$. Elements are written $A$ and $C$, and $B$ is not used for an element: $B$, $N$, $H$, $K$ are the four forms of the biquaternion algebra, of which $B$ and $H$ survive here. The letter $N$ is read with care: in the biquaternion chapter it is the quaternionic bilinear form, which coincides with $B$ on $\mathbb{C}$, while *Complex Norm and Invertibility*, below this article in this category, writes the positive definite norm as $N(A)=A\bar A$, which is the diagonal of $H$. The two readings are told apart by their argument count and by their chapter.

## The Two Forms

The **form** of a product is its scalar part, a function of two elements (*The 4 Forms over the Biquaternion $\mathbb{C}$ Space*). On the complex space, read over itself and as the centre of $\mathbb{B}$, there is no vector direction, so the scalar part of a product is the product, and the two forms are

$$
B(A,C)=AC,\qquad H(A,C)=A\bar C .
$$

The four forms of the biquaternion algebra collapse to these two, and the collapse is the triviality of the natural sign, in the first slot alone:

| the biquaternion form | the pair of slots | value on $\mathbb{C}$ | the complex form |
|---|---|---|---|
| $B$, general plain bilinear | $(\mathrm{id},\mathrm{id})$ | $AC$ | $B$ |
| $N$, general quaternionic bilinear | $(\natural,\mathrm{id})$ | $AC$ | $B$ |
| $H$, general plain sesquilinear | $(\mathrm{id},{}^{*})$ | $A\bar C$ | $H$ |
| $K$, general quaternionic sesquilinear | $(\natural,{}^{*})$ | $A\bar C$ | $H$ |

The two pairs $(\mathrm{id},\mathrm{id})$ and $(\natural,\mathrm{id})$ name the bilinear product, and $(\mathrm{id},{}^{*})$ and $(\natural,{}^{*})$ the sesquilinear one; the two members of each pair give the same product, and hence the same form. The count of the forms on $\mathbb{C}$ is therefore two, and the two are distinct as functions of a pair, since $B(A,C)$ and $H(A,C)$ differ as soon as the second element is not real. The complex space is one-dimensional over itself, so the Gram matrix of a form in the basis $1$ is the $1\times1$ matrix of its value on the unit, and both forms have the Gram matrix $[1]$, since $B(1,1)=H(1,1)=1$. The Gram matrix therefore does not separate the two forms here, and the separation is by their symmetry.

## The Two Forms Are Separated by Their Symmetry

The two forms carry the two symmetries of the biquaternion pair. The form $B$ is **symmetric**,

$$
B(A,C)=AC=CA=B(C,A),
$$

because the field is commutative. The form $H$ is **conjugate-symmetric**,

$$
H(A,C)=A\bar C=\overline{C\bar A}=\overline{H(C,A)},
$$

and it is symmetric exactly on the real subspace, when the bar fixes both arguments. The two forms of the complex space are therefore told apart by their symmetry alone, $B$ symmetric against $H$ conjugate-symmetric, and not by their Gram matrix, which is $[1]$ for both. On $\mathbb{B}$ the same two symmetries occur, but there the Gram matrices separate the forms as well, $\mathrm I_4$ for $N$ and $H$ against the sign matrix $\mathrm E$ for $B$ and $K$ (*The 4 Forms over the Biquaternion $\mathbb{C}$ Space*); the complex reading loses that second separator, since the sign vector $\varepsilon=(1)$ on a one-dimensional space is the identity.

## The Two Algebraic Norms

The **algebraic norm** of a form is its diagonal, the form read at equal arguments (*The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*). The two forms therefore give two algebraic norms,

$$
B(A)=B(A,A)=A^{2},\qquad H(A)=H(A,A)=A\bar A=|A|^{2},
$$

the square and the squared modulus of the element. The four algebraic norms of the biquaternion algebra collapse with the forms, $B=N$ and $H=K$, so the complex space carries two norms and no more.

Both norms are **multiplicative**: $B(AC)=(AC)^{2}=A^{2}C^{2}=B(A)B(C)$, and $H(AC)=|AC|^{2}=|A|^{2}|C|^{2}=H(A)H(C)$. The two differ in value and in definiteness. The value of $H$ is real and positive definite, $H(A)=|A|^{2}>0$ for $A\neq0$; the value of $B$ is complex and **anisotropic**, $B(A)=A^{2}=0$ only for $A=0$, so the diagonal of $B$ never vanishes off the origin, and its real part, $a^{2}-a'^{2}$, is indefinite. The anisotropy of $B$ over $\mathbb{C}$ and the indefiniteness of its realification are not in contradiction: the first is read on the complex values, which vanish only together with $A$, and the second on the real part alone, which changes sign.

| form | the diagonal | value | symmetric | conjugate-symmetric | Gram matrix | realified signature |
|---|---|---|---|---|---|---|
| $B$ | $B(A)=A^{2}$ | complex, anisotropic | yes | no | $[1]$ | $(1,1)$ |
| $H$ | $H(A)=|A|^{2}$ | real, positive definite | no | yes | $[1]$ | $(2,0)$ |

The realified signatures are those of the two rules of the passage to the real reading, the split signature $(n,n)$ for a bilinear form and the doubled inertia for a Hermitian one, applied at $n=1$; the construction and its rules are *The Realification and the Effect of the Change of Scalars*, below this article in this category.

## Definite and Multiplicative Together

On the biquaternion algebra no one of the four algebraic norms is both definite and multiplicative: $N$ is multiplicative and vanishes on the zero-divisor cone, and $H$ is definite and fails multiplicativity, and the obstruction is the zero divisor (*The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*). **On the complex space one and the same function is both**: $H(A)=|A|^{2}$ is real, positive definite, and multiplicative. The anisotropy of $H$ is the absence of zero divisors, since $H(A)=0$ forces $A=0$, and its multiplicativity is the multiplicativity of the modulus.

The pair is therefore joined on $\mathbb{C}$ and split on $\mathbb{B}$, and the mechanism is the zero divisor. A definite function is nonzero off the origin, while a multiplicative one takes the value $0$ on a product only if it takes the value $0$ on a factor; a pair of nonzero elements with vanishing product therefore forbids the two properties in one function. $\mathbb{C}$ has no such pair, and exhibits the definite multiplicative $H$; on $\mathbb{B}$ the witness $(e_0+ie_1)(e_0-ie_1)=0$ with $N(e_0\pm ie_1)=0$ is the obstruction, and the impossibility on $\mathbb{B}$ is the phenomenon of its zero divisors. The norm $H$, its multiplicativity, the criterion of invertibility $A\neq0$ and the group of units $\mathbb{C}^{\times}$ are read in *Complex Norm and Invertibility*, below this article in this category.

## Summary

The two products of the complex space carry two forms, $B(A,C)=AC$ and $H(A,C)=A\bar C$, the collapse of the four forms $B$, $N$, $H$, $K$ of the biquaternion algebra by the triviality of the natural sign; the four products and forms become two, $B=N$ and $H=K$. The two forms have the same Gram matrix $[1]$ over $\mathbb{C}$ and are separated by their symmetry alone, $B$ symmetric and $H$ conjugate-symmetric. Their diagonals are the two algebraic norms $B(A)=A^{2}$, complex and anisotropic, and $H(A)=|A|^{2}$, real and positive definite; both are multiplicative. On $\mathbb{C}$, unlike on $\mathbb{B}$, one and the same function $H$ is both definite and multiplicative, and the impossibility on $\mathbb{B}$ is a phenomenon of its zero divisors.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{C}$ | the complex space, read over itself and as the centre of $\mathbb{B}$ |
| $A$, $C$ | elements of the space |
| $B(A,C)=AC$ | the general plain bilinear form, equal to the quaternionic bilinear form $N$ |
| $H(A,C)=A\bar C$ | the general plain sesquilinear or Hermitian form, equal to the Krein form $K$ |
| $B(A)=A^{2}$ | the plain bilinear algebraic norm |
| $H(A)=A\bar A=|A|^{2}$ | the Hermitian algebraic norm, real and positive definite |
| $\bar{\cdot}$ | complex conjugation, the bar; the natural sign is the identity |
| $[1]$ | the Gram matrix of each form in the complex basis $(1)$ |
| $(1,1)$, $(2,0)$ | the realified signatures of $B$ and of $H$ |

## Further Reading

- *The Two Products of the Complex Space*, for the two products whose scalar parts the two forms are.
- *The 4 Forms over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-4-forms-over-the-biquaternion-c-space.md`) and *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-4-algebraic-norms-over-the-biquaternion-c-space.md`), for the four forms and the four norms that collapse here to two.
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the general theory of the pairings of which the forms are the scalar parts.
- *Relations and Comparison Between the Two Products*, for the two products set against each other.
- *Complex Norm and Invertibility* (`articles_maths/complex-norm-and-invertibility.md`), below this article in this category, for the topological norm $|\cdot|=\sqrt{H}$, its multiplicativity, the invertibility criterion and the group of units.
- *The Realification and the Effect of the Change of Scalars*, below this article in this category, for the two rules that give the realified signatures $(1,1)$ and $(2,0)$.
