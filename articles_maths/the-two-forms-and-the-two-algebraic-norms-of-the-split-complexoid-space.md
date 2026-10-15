# __The Two Forms and the Two Algebraic Norms of the Split-Complexoid Space__

## Introduction

The two products of *The Two Products of the Split-Complex Space* carry two **forms**, and the forms carry two **algebraic norms**. The **general plain bilinear form** is $B(A,C)=AC$, the product itself read as a form; the **general plain sesquilinear form**, also called the **Hermitian form**, is $H(A,C)=A\overline{C}$. Their **algebraic norms** are the two algebraic norms, $B(A)=A^2$ and $H(A)=A\overline{A}=a^2-a'^2=N(A)$. This article reads the two forms and the two norms on the coordinates, gives their Gram matrices and their realified signatures, and isolates the one point that separates the split-complex reading from the complex one: which of the two forms is definite.

The collapse of the four forms and their algebraic norms to the two of this article is carried here. The norm $N$, its multiplicativity, the criterion of invertibility, the group of units and the order cone are *Split-Complex Norm and Invertibility*, below this article in this category, and the isotropic cone and the zero divisors are *Split-Complex Zero Divisors*, below this article in this category. The forms read on the distinguished subspaces are *Remarkable Subspaces of the Split-Complex Numbers and the Two Forms*, below this article in this category.

**The reading fixed here.** The bar is the conjugation $j\mapsto-j$ and the Hermitian conjugation is ${}^{*}=\bar{\cdot}$; the algebra is commutative. In this article $A=a+ja'$ and $C=c+jc'$ are elements, so the letters $B$, $H$ and $N$ name forms and norms only.

## The Two Forms

This space carries four general forms, the bilinear and sesquilinear pairings in their two-slot variants, written $B$, $N$, $H$ and $K$. On $\mathbb{D}$ the conjugation of the coefficient ring is the identity, the algebra being read over itself, and ${}^{*}=\bar{\cdot}$; the first and the second coincide with the product and the third and the fourth with the product with the second slot conjugated. The four collapse pairwise to two:

$$
B(A,C)=AC,
\qquad
H(A,C)=A\overline{C},
$$

with $B$ the form of the ring and $H$ the form of the sesqualgebra, the collapse being carried by *The Collapse of the Twelve Structures on the Split-Complex Numbers*, the article preceding this one.

**Proposition (the two forms are separated by symmetry alone).** $B$ is symmetric and $\mathbb{D}$-bilinear, $B(A,C)=B(C,A)$; $H$ is conjugate-symmetric and sesquilinear over $(\mathbb{D},\bar{\cdot})$, $H(A,C)=\overline{H(C,A)}$, linear in the first slot and conjugate-linear in the second. Both have Gram matrix $[1]$ over the one-dimensional $\mathbb{D}$-module $\mathbb{D}$.

**Proof.** $B$ is the multiplication of a commutative ring, so $B(A,C)=AC=CA=B(C,A)$, and it is $\mathbb{D}$-bilinear. For $H$, linearity in the first slot is clear; in the second, $H(A,\lambda C)=A\overline{\lambda C}=\bar\lambda\,A\overline{C}=\bar\lambda\,H(A,C)$, so it is conjugate-linear; and $H(C,A)=C\overline{A}=\overline{A\overline{C}}=\overline{H(A,C)}$ by commutativity. The module is free of rank one on the basis $1$, and the Gram matrix of either form is the $1\times 1$ matrix of $B(1,1)=1=H(1,1)$, namely $[1]$.

So the two forms have the same single entry and are torn apart by symmetry, exactly as on the complex field: symmetry alone selects the bilinear form against the conjugate-symmetric one. On the coordinates,

$$
B(A,C)=(ac+a'c')+(ac'+a'c)j,
\qquad
H(A,C)=(ac-a'c')+(a'c-ac')j .
$$

The two values agree on the real line and differ on the split imaginary line: with $A=C=j$ one has $B(j,j)=1$ and $H(j,j)=-1$. That sign is the whole of the difference, and it is the split sign.

## The Two Realified Signatures

A form has a value in $\mathbb{D}$; its **realification** is its real part, read on $\mathbb{D}$ as a two-dimensional real space. The two forms realify to two real symmetric bilinear forms, and the split sign exchanges their signatures relative to the complex case.

**Proposition (the action of the structure).** With $J$ the multiplication by $j$ on $\mathbb{D}$,

$$
B(JA,JC)=+B(A,C),
\qquad
H(JA,JC)=-H(A,C).
$$

**Proof.** $B(JA,JC)=(jA)(jC)=j^2AC=AC=B(A,C)$, since $j^2=+1$. For the conjugate-symmetric form, $H(JA,JC)=jA\overline{jC}=jA(-\bar j\,\overline{C})=-j^2A\overline{C}=-A\overline{C}=-H(A,C)$, because $\bar j=-j$.

The two signs place the two forms in the two realification rules, and **the split sign assigns them to the rule opposite to the complex one**. On $\mathbb{C}$ the bilinear form $B(A,C)=AC$ satisfies $B(iA,iC)=-B(A,C)$, so it realifies to the **split signature** $(n,n)=(1,1)$, and the Hermitian form satisfies $H(iA,iC)=+H(A,C)$, so it realifies to the doubling $(2,0)$. On $\mathbb{D}$, because $j^2=+1$, the two signs are exchanged: the **Hermitian** form obeys the bilinear rule and the **bilinear** form obeys the Hermitian rule. Reading the two real parts on the basis $1,j$,

$$
\operatorname{Re}B=\;ac+a'c'\ \text{with Gram}\ \begin{pmatrix}1&0\\0&1\end{pmatrix},
\qquad
\operatorname{Re}H=\;ac-a'c'\ \text{with Gram}\ \begin{pmatrix}1&0\\0&-1\end{pmatrix},
$$

so

| form | on $\mathbb{C}$ | on $\mathbb{D}$ |
|---|---|---|
| $B(A,C)=AC$ | $(1,1)$, indefinite | $(2,0)$, definite |
| $H(A,C)=A\overline{C}$ | $(2,0)$, definite | $(1,1)$, indefinite |

The two forms **exchange their realified signatures** when the sign of the square of the generator is flipped. This is the precise form of the split sign at the level of the forms, and it is stated again in *The Realification and the Effect of the Change of Scalars on the Split-Complex Numbers*, below this article in this category.

## The Two Algebraic Norms

The **algebraic norm** of a form is its algebraic norm, the form read at $A=C$. The two forms give the two norms

$$
B(A)=A^2=(a^2+a'^2)+2aa'j,
\qquad
H(A)=A\overline{A}=a^2-a'^2=N(A).
$$

The algebraic norms of the four forms collapse to the two algebraic norms of this article: the algebraic norms of the first two forms give $A^2$, and the algebraic norms of the last two give $A\overline{A}=N(A)$. The count of four becomes the count of two, exactly as the count of four forms becomes the count of two.

Both norms are multiplicative: $B(AC)=(AC)^2=A^2C^2=B(A)B(C)$ and $N(AC)=N(A)N(C)$ (*Split-Complex Norm and Invertibility*, below this article in this category, owns the second). The two norms differ in their value and in their vanishing set, and neither is a definite real form on $\mathbb{D}$.

**Proposition (value and vanishing set).** $B(A)=A^2$ takes its value in $\mathbb{D}$ and vanishes only at $A=0$; $H(A)=a^2-a'^2$ takes its value in $\mathbb{R}$, is indefinite of signature $(1,1)$, and vanishes on the two null lines $a=\pm a'$, that is on $\mathbb{R}\Pi_1\cup\mathbb{R}\Pi_2$.

**Proof.** $A^2=(a+ja')^2=a^2+a'^2+2aa'j=0$ forces $a^2+a'^2=0$ and $aa'=0$, hence $a=a'=0$ over $\mathbb{R}$; so $B$ is **anisotropic**. The value $a^2-a'^2$ is real and changes sign, so the form is indefinite; it vanishes exactly when $a^2=a'^2$, which is $A\in\mathbb{R}(1+j)\cup\mathbb{R}(1-j)=\mathbb{R}\Pi_1\cup\mathbb{R}\Pi_2$.

The two norms are therefore of two different kinds. The bilinear norm $B$ is $\mathbb{D}$-valued and anisotropic, its only zero the origin; it is not a real form and carries no order. The Hermitian norm $H=N$ is real and indefinite, and its isotropic set is not the origin but two lines, on which the zero divisors lie. This is the statement that the null cone of $\mathbb{D}$ is a pair of lines rather than a point, and it is the algebraic reason the ring is not a field.

## The Point That Separates the Split Case from the Complex One

On the complex field the Hermitian norm is $A\overline{A}=\lvert A\rvert^2$, positive definite, with vanishing set the origin alone; it is the square of the Euclidean modulus and it is multiplicative. The complex field is thus a composition algebra for its definite norm, with no zero divisors and division by every non-zero element.

On $\mathbb{D}$ the same construction gives the indefinite norm $N=a^2-a'^2$, whose vanishing set is the two null lines. **Neither of the two algebraic norms of $\mathbb{D}$ is a definite real norm**: $B(A)=A^2$ is $\mathbb{D}$-valued, so it defines no order and no modulus, and $H(A)=N(A)$ is real but indefinite, its null set the two null lines on which the zero divisors lie rather than the origin. The realification of the form $B$ is definite — it is the Euclidean form $a^2+a'^2$ — but that form is the real part of the square and is not multiplicative.

**Theorem (no definite multiplicative norm).** There is no function $\nu:\mathbb{D}\to\mathbb{R}$ that is a **norm** — definite, $\nu(A)=0$ if and only if $A=0$, and absolutely homogeneous, $\nu(\lambda A)=\lvert\lambda\rvert\nu(A)$ for $\lambda\in\mathbb{R}$ — and **multiplicative**, $\nu(AC)=\nu(A)\nu(C)$.

**Proof.** Homogeneity forces $\nu(0)=0$. If $\nu$ were also multiplicative, the two zero divisors $\Pi_1$ and $\Pi_2$ would give $\nu(\Pi_1)\nu(\Pi_2)=\nu(\Pi_1\Pi_2)=\nu(0)=0$, while definiteness gives $\nu(\Pi_1)>0$ and $\nu(\Pi_2)>0$, a contradiction. So no definite multiplicative norm exists on $\mathbb{D}$.

So the impossibility is exactly the phenomenon of the zero divisors, and it is where the split-complex algebra departs from the complex composition algebra: the definiteness of the Hermitian norm, which gives $\mathbb{C}$ its modulus and its division, is lost on $\mathbb{D}$ because the sign of the square of the generator is reversed, and with it the null cone opens from a point to two lines.

## Summary

The two products of the split-complex space carry two forms, the symmetric bilinear form $B(A,C)=AC$ and the conjugate-symmetric Hermitian form $H(A,C)=A\overline{C}$, both of Gram matrix $[1]$ over the rank-one $\mathbb{D}$-module and separated by symmetry alone. Their realified signatures are $(2,0)$ for $B$ and $(1,1)$ for $H$; the split sign exchanges them with respect to the complex case, where they are $(1,1)$ and $(2,0)$, because the bilinear form is $J$-invariant here and the Hermitian form is $J$-anti-invariant. The four forms and the four algebraic norms collapse to these two forms and their algebraic norms.

The two algebraic norms are $B(A)=A^2$, $\mathbb{D}$-valued and anisotropic, and $H(A)=A\overline{A}=a^2-a'^2=N(A)$, real and indefinite, with isotropic set the two null lines on which the zero divisors lie. Both are multiplicative; neither is a definite real norm. There is no definite multiplicative norm on $\mathbb{D}$: a norm that is definite, absolutely homogeneous and multiplicative would force the zero product $\Pi_1\Pi_2$ of two non-zero elements to have value $\nu(\Pi_1)\nu(\Pi_2)=0$; the impossibility is the zero divisor seen from the side of the form, and it is the point that separates the split-complex algebra from the complex field.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $B(A,C)=AC$ | general plain bilinear form, symmetric, Gram matrix $[1]$ |
| $H(A,C)=A\overline{C}$ | general plain sesquilinear (Hermitian) form |
| $B(A)=A^2$ | the bilinear algebraic norm, $\mathbb{D}$-valued |
| $H(A)=N(A)=a^2-a'^2$ | the Hermitian algebraic norm, real, indefinite |
| $\operatorname{Re}B$ | realification of $B$, signature $(2,0)$ |
| $\operatorname{Re}H$ | realification of $H$, signature $(1,1)$ |
| $J$ | multiplication by $j$, $J^2=+\mathrm{id}$ |
| $\mathbb{R}\Pi_1\cup\mathbb{R}\Pi_2$ | the isotropic set of $N$, the null lines |

## Further Reading

- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for symmetric bilinear and Hermitian forms, signature and inertia in dimension two.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, Colloquium Publications 44, 1998), for forms over an algebra with involution and the realification rules.
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for the algebraic norm of the trace form and algebraic norms in associative rings.
