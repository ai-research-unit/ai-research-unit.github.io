# __The Two Forms and the Two Algebraic Norms of the Split-Complexoid Space__

## Introduction

The two products of *The Two Products of the Split-Complexoid Space* carry two **forms**, and the forms carry two **algebraic norms**. The **general plain bilinear form** is $\langle Q_1,Q_2\rangle=Q_1Q_2$, the product itself read as a form; the **general plain sesquilinear form**, also called the **Hermitian form**, is $\langle Q_1,Q_2\rangle_{*}=Q_1\overline{Q_2}$. Their **algebraic norms** are the two algebraic norms, $\langle Q\rangle=Q^2$ and $\langle Q\rangle_{*}=Q\overline{Q}=q^2-q'^2$. This article reads the two forms and the two norms on the coordinates, gives their Gram matrices and their realified signatures, and isolates the one point that separates the split-complex reading from the complex one: which of the two forms is definite.

The collapse of the four forms and their algebraic norms to the two of this article is carried here. The norm $\langle\cdot\rangle_{*}$, its multiplicativity, the criterion of invertibility, the group of units and the order cone are *Norm and Invertibility in the General Split-Complex Algebra*, below this article in this category, and the isotropic cone and the zero divisors are *Zero Divisors of the Split-Complex Algebra*, below this article in this category. The forms read on the distinguished subspaces are *Remarkable Subspaces of the Split-Complexoid and the Two Forms*, below this article in this category.

**The reading fixed here.** The bar is the conjugation $j\mapsto-j$ and the Hermitian conjugation is ${}^{*}=\bar{\cdot}$; the algebra is commutative. In this article $Q_1=q_1+jq'_1$ and $Q_2=q_2+jq'_2$ are elements, so the letters $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{\natural}$, $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\natural*}$ name forms and norms only.

## The Two Forms

This space carries four general forms, the bilinear and sesquilinear pairings in their two-slot variants, written $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{\natural}$, $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\natural*}$. On $\mathbb{D}$ the conjugation of the coefficient ring is the identity, the algebra being read over itself, and ${}^{*}=\bar{\cdot}$; the first and the second coincide with the product and the third and the fourth with the product with the second slot conjugated. The four collapse pairwise to two:

$$
\langle Q_1,Q_2\rangle=Q_1Q_2,
\qquad
\langle Q_1,Q_2\rangle_{*}=Q_1\overline{Q_2},
$$

with $\langle\cdot,\cdot\rangle$ the form of the ring and $\langle\cdot,\cdot\rangle_{*}$ the form of the sesqualgebra, the collapse of the four general forms to these two being carried out in this article.

**Proposition (the two forms are separated by symmetry alone).** $\langle\cdot,\cdot\rangle$ is symmetric and $\mathbb{D}$-bilinear, $\langle Q_1,Q_2\rangle=\langle Q_2,Q_1\rangle$; $\langle\cdot,\cdot\rangle_{*}$ is conjugate-symmetric and sesquilinear over $(\mathbb{D},\bar{\cdot})$, $\langle Q_1,Q_2\rangle_{*}=\overline{\langle Q_2,Q_1\rangle_{*}}$, linear in the first slot and conjugate-linear in the second. Both have Gram matrix $[1]$ over the one-dimensional $\mathbb{D}$-module $\mathbb{D}$.

**Proof.** $\langle\cdot,\cdot\rangle$ is the multiplication of a commutative ring, so $\langle Q_1,Q_2\rangle=Q_1Q_2=Q_2Q_1=\langle Q_2,Q_1\rangle$, and it is $\mathbb{D}$-bilinear. For $\langle\cdot,\cdot\rangle_{*}$, linearity in the first slot is clear; in the second, $\langle Q_1,\lambda Q_2\rangle_{*}=Q_1\overline{\lambda Q_2}=\bar\lambda\,Q_1\overline{Q_2}=\bar\lambda\,\langle Q_1,Q_2\rangle_{*}$, so it is conjugate-linear; and $\langle Q_2,Q_1\rangle_{*}=Q_2\overline{Q_1}=\overline{Q_1\overline{Q_2}}=\overline{\langle Q_1,Q_2\rangle_{*}}$ by commutativity. The module is free of rank one on the basis $1$, and the Gram matrix of either form is the $1\times 1$ matrix of $\langle 1,1\rangle=1=\langle 1,1\rangle_{*}$, namely $[1]$.

So the two forms have the same single entry and are torn apart by symmetry, exactly as on the complex field: symmetry alone selects the bilinear form against the conjugate-symmetric one. On the coordinates,

$$
\langle Q_1,Q_2\rangle=(q_1q_2+q'_1q'_2)+(q_1q'_2+q'_1q_2)j,
\qquad
\langle Q_1,Q_2\rangle_{*}=(q_1q_2-q'_1q'_2)+(q'_1q_2-q_1q'_2)j .
$$

The two values agree on the real line and differ on the split imaginary line: with $Q_1=Q_2=j$ one has $\langle j,j\rangle=1$ and $\langle j,j\rangle_{*}=-1$. That sign is the whole of the difference, and it is the split sign.

## The Two Realified Signatures

A form has a value in $\mathbb{D}$; its **realification** is its real part, read on $\mathbb{D}$ as a two-dimensional real space. The two forms realify to two real symmetric bilinear forms, and the split sign exchanges their signatures relative to the complex case.

**Proposition (the action of the structure).** With $J$ the multiplication by $j$ on $\mathbb{D}$,

$$
\langle JQ_1,JQ_2\rangle=+\langle Q_1,Q_2\rangle,
\qquad
\langle JQ_1,JQ_2\rangle_{*}=-\langle Q_1,Q_2\rangle_{*}.
$$

**Proof.** $\langle JQ_1,JQ_2\rangle=(jQ_1)(jQ_2)=j^2Q_1Q_2=Q_1Q_2=\langle Q_1,Q_2\rangle$, since $j^2=+1$. For the conjugate-symmetric form, $\langle JQ_1,JQ_2\rangle_{*}=jQ_1\overline{jQ_2}=jQ_1(-\bar j\,\overline{Q_2})=-j^2Q_1\overline{Q_2}=-Q_1\overline{Q_2}=-\langle Q_1,Q_2\rangle_{*}$, because $\bar j=-j$.

The two signs place the two forms in the two realification rules, and **the split sign assigns them to the rule opposite to the complex one**. On $\mathbb{C}$ the bilinear form $\langle A,C\rangle=AC$ satisfies $\langle iA,iC\rangle=-\langle A,C\rangle$, so it realifies to the **split signature** $(n,n)=(1,1)$, and the Hermitian form satisfies $\langle iA,iC\rangle_{*}=+\langle A,C\rangle_{*}$, so it realifies to the doubling $(2,0)$. On $\mathbb{D}$, because $j^2=+1$, the two signs are exchanged: the **Hermitian** form obeys the bilinear rule and the **bilinear** form obeys the Hermitian rule. Reading the two real parts on the basis $1,j$,

$$
\operatorname{Re}B=\;q_1q_2+q'_1q'_2\ \text{with Gram}\ \begin{pmatrix}1&0\\0&1\end{pmatrix},
\qquad
\operatorname{Re}H=\;q_1q_2-q'_1q'_2\ \text{with Gram}\ \begin{pmatrix}1&0\\0&-1\end{pmatrix},
$$

so

| form | on $\mathbb{C}$ | on $\mathbb{D}$ |
|---|---|---|
| bilinear form $\langle\cdot,\cdot\rangle$ | $(1,1)$, indefinite | $(2,0)$, definite |
| Hermitian form $\langle\cdot,\cdot\rangle_{*}$ | $(2,0)$, definite | $(1,1)$, indefinite |

The two forms **exchange their realified signatures** when the sign of the square of the generator is flipped. This is the precise form of the split sign at the level of the forms, and it is stated again in *The Realification and the Effect of the Change of Scalars on the Split-Complexoid*, below this article in this category.

## The Two Algebraic Norms

The **algebraic norm** of a form is its algebraic norm, the form read at $Q$. The two forms give the two norms

$$
\langle Q\rangle=Q^2=(q^2+q'^2)+2qq'j,
\qquad
\langle Q\rangle_{*}=Q\overline{Q}=q^2-q'^2 .
$$

The algebraic norms of the four forms collapse to the two algebraic norms of this article: the algebraic norms of the first two forms give $Q^2$, and the algebraic norms of the last two give $Q\overline{Q}=\langle Q\rangle_{*}$. The count of four becomes the count of two, exactly as the count of four forms becomes the count of two.

Both norms are multiplicative: $\langle Q_1Q_2\rangle=(Q_1Q_2)^2=Q_1^2Q_2^2=\langle Q_1\rangle\langle Q_2\rangle$ and $\langle Q_1Q_2\rangle_{*}=\langle Q_1\rangle_{*}\langle Q_2\rangle_{*}$ (*Norm and Invertibility in the General Split-Complex Algebra*, below this article in this category, owns the second). The two norms differ in their value and in their vanishing set, and neither is a definite real form on $\mathbb{D}$.

**Proposition (value and vanishing set).** $\langle Q\rangle=Q^2$ takes its value in $\mathbb{D}$ and vanishes only at $Q=0$; $\langle Q\rangle_{*}=q^2-q'^2$ takes its value in $\mathbb{R}$, is indefinite of signature $(1,1)$, and vanishes on the two null lines $q=q'$ and $q=-q'$, that is on $\mathbb{R}\Pi_1\cup\mathbb{R}\Pi_2$.

**Proof.** $Q^2=(q+jq')^2=q^2+q'^2+2qq'j=0$ forces $q^2+q'^2=0$ and $qq'=0$, hence $q=q'=0$ over $\mathbb{R}$; so $\langle\cdot,\cdot\rangle$ is **anisotropic**. The value $q^2-q'^2$ is real and changes sign, so the form is indefinite; it vanishes exactly when $q^2=q'^2$, which is $Q\in\mathbb{R}(1+j)\cup\mathbb{R}(1-j)=\mathbb{R}\Pi_1\cup\mathbb{R}\Pi_2$.

The two norms are therefore of two different kinds. The bilinear norm $\langle\cdot\rangle$ is $\mathbb{D}$-valued and anisotropic, its only zero the origin; it is not a real form and carries no order. The Hermitian norm $\langle\cdot\rangle_{*}=q^2-q'^2$ is real and indefinite, and its isotropic set is not the origin but two lines, on which the zero divisors lie. This is the statement that the null cone of $\mathbb{D}$ is a pair of lines rather than a point, and it is the algebraic reason the ring is not a field.

## The Point That Separates the Split Case from the Complex One

On the complex field the Hermitian norm is $A\overline{A}=\lvert A\rvert^2$, positive definite, with vanishing set the origin alone; it is the square of the Euclidean modulus and it is multiplicative. The complex field is thus a composition algebra for its definite norm, with no zero divisors and division by every non-zero element.

On $\mathbb{D}$ the same construction gives the indefinite norm $\langle\cdot\rangle_{*}=q^2-q'^2$, whose vanishing set is the two null lines. **Neither of the two algebraic norms of $\mathbb{D}$ is a definite real norm**: $\langle Q\rangle=Q^2$ is $\mathbb{D}$-valued, so it defines no order and no modulus, and $\langle Q\rangle_{*}=q^2-q'^2$ is real but indefinite, its null set the two null lines on which the zero divisors lie rather than the origin. The realification of the form $\langle\cdot,\cdot\rangle$ is definite — it is the Euclidean form $q^2+q'^2$ — but that form is the real part of the square and is not multiplicative.

**Theorem (no definite multiplicative norm).** There is no function $\nu:\mathbb{D}\to\mathbb{R}$ that is a **norm** — definite, $\nu(Q)=0$ if and only if $Q=0$, and absolutely homogeneous, $\nu(\lambda Q)=\lvert\lambda\rvert\nu(Q)$ for $\lambda\in\mathbb{R}$ — and **multiplicative**, $\nu(Q_1Q_2)=\nu(Q_1)\nu(Q_2)$.

**Proof.** Homogeneity forces $\nu(0)=0$. If $\nu$ were also multiplicative, the two zero divisors $\Pi_1$ and $\Pi_2$ would give $\nu(\Pi_1)\nu(\Pi_2)=\nu(\Pi_1\Pi_2)=\nu(0)=0$, while definiteness gives $\nu(\Pi_1)>0$ and $\nu(\Pi_2)>0$, a contradiction. So no definite multiplicative norm exists on $\mathbb{D}$.

So the impossibility is exactly the phenomenon of the zero divisors, and it is where the split-complex algebra departs from the complex composition algebra: the definiteness of the Hermitian norm, which gives $\mathbb{C}$ its modulus and its division, is lost on $\mathbb{D}$ because the sign of the square of the generator is reversed, and with it the null cone opens from a point to two lines.

## Summary

The two products of the split-complex space carry two forms, the symmetric bilinear form $\langle Q_1,Q_2\rangle=Q_1Q_2$ and the conjugate-symmetric Hermitian form $\langle Q_1,Q_2\rangle_{*}=Q_1\overline{Q_2}$, both of Gram matrix $[1]$ over the rank-one $\mathbb{D}$-module and separated by symmetry alone. Their realified signatures are $(2,0)$ for $\langle\cdot,\cdot\rangle$ and $(1,1)$ for $\langle\cdot,\cdot\rangle_{*}$; the split sign exchanges them with respect to the complex case, where they are $(1,1)$ and $(2,0)$, because the bilinear form is $J$-invariant here and the Hermitian form is $J$-anti-invariant. The four forms and the four algebraic norms collapse to these two forms and their algebraic norms.

The two algebraic norms are $\langle Q\rangle=Q^2$, $\mathbb{D}$-valued and anisotropic, and $\langle Q\rangle_{*}=Q\overline{Q}=q^2-q'^2$, real and indefinite, with isotropic set the two null lines on which the zero divisors lie. Both are multiplicative; neither is a definite real norm. There is no definite multiplicative norm on $\mathbb{D}$: a norm that is definite, absolutely homogeneous and multiplicative would force the zero product $\Pi_1\Pi_2$ of two non-zero elements to have value $\nu(\Pi_1)\nu(\Pi_2)=0$; the impossibility is the zero divisor seen from the side of the form, and it is the point that separates the split-complex algebra from the complex field.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle Q_1,Q_2\rangle=Q_1Q_2$ | general plain bilinear form, symmetric, Gram matrix $[1]$ |
| $\langle Q_1,Q_2\rangle_{*}=Q_1\overline{Q_2}$ | general plain sesquilinear (Hermitian) form |
| $\langle Q\rangle=Q^2$ | the bilinear algebraic norm, $\mathbb{D}$-valued |
| $\langle Q\rangle_{*}=q^2-q'^2$ | the Hermitian algebraic norm, real, indefinite |
| $\operatorname{Re}B$ | realification of $\langle\cdot\rangle$, signature $(2,0)$ |
| $\operatorname{Re}H$ | realification of $\langle\cdot\rangle_{*}$, signature $(1,1)$ |
| $J$ | multiplication by $j$, $J^2=+\mathrm{id}$ |
| $\mathbb{R}\Pi_1\cup\mathbb{R}\Pi_2$ | the isotropic set of $\langle\cdot\rangle_{*}$, the null lines |

## Further Reading

- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for symmetric bilinear and Hermitian forms, signature and inertia in dimension two.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, Colloquium Publications 44, 1998), for forms over an algebra with involution and the realification rules.
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for the algebraic norm of the trace form and algebraic norms in associative rings.
