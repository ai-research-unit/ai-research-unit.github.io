# __The Realification of the General Plain Sesqualgebra__

## Introduction

The general plain sesqualgebra is the structure the biquaternion ring $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ carries when the plain product is read with the Hermitian conjugation in the second slot,
$$
\tilde P\star\tilde Q=\tilde P\tilde Q^{*},
$$
the general plain sesquilinear structure of *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*. Its product is additive in each variable, $\mathbb{C}$-linear in the first slot and $\varsigma$-semilinear in the second with $\varsigma(z)=\bar z$, so the structure is a **sesqualgebra over $(\mathbb{C},\varsigma)$**; the involution is the star ${}^{*}=\bar{\cdot}\circ{}^{\natural}$, the product is the derived operation of the algebra $\mathbb{B}$ with that involution, and $e_0$ is a right unit and not a left one (*Introduction to the General Plain Sesqualgebra of Biquaternions*). Read over $\mathbb{R}$ the same product on the same set is an $\mathbb{R}$-algebra on the eight-dimensional real space $\mathbb{R}^8$, and this article owns that real reading.

The general construction is not repeated here. The realification of a vector space, of a linear map and of a form, the two criteria of $\mathbb{C}$-linearity and of conjugate-linearity, the two rules of the realification of a form and the table of the four effects are **The Realification and the Effect of the Change of Scalars**. This article gives what is specific to this product: the product as an $\mathbb{R}$-algebra and its real table, the law of its two slots over the centre with the two parities of its two families of multiplications, the realification of the form it carries with the signature that follows, the classes the reading leaves untouched with their real dimensions, and its real operators.

## The Product Read over $\mathbb{R}$

A $\mathbb{C}$-sesquilinear product is additive in each variable and linear over $\mathbb{R}$ in each, so by §*The Effect on the Twelve Algebraic Structures* of *The Realification and the Effect of the Change of Scalars* the product $\star$ is $\mathbb{R}$-**bilinear**, and $(\mathbb{B},\star)$ is an $\mathbb{R}$-**algebra** on $\mathbb{R}^8$ in the broad sense, the sense of a module with a bilinear multiplication. The involution of the base disappears in the passage, since the only automorphism of $\mathbb{R}$ is the identity and a sesquilinear law with the identity involution is a bilinear law: the block is a sesqualgebra over $\mathbb{C}$ and an algebra over $\mathbb{R}$, and the count of sesqualgebras over $\mathbb{R}$ among the twelve is zero. The distinction survives as a distinction of the centre: the second slot is $\mathbb{C}_{\mathbb{B}}$-conjugate-linear where the second slot of a bilinear structure is $\mathbb{C}_{\mathbb{B}}$-linear, and that is what the two sections after this one read.

The product is determined over $\mathbb{R}$ by its values on the complex basis and by the two scalar rules. On the basis,
$$
e_\mu\star e_\nu=\varepsilon_\nu\,e_\mu e_\nu,\qquad \varepsilon=(1,-1,-1,-1),
$$
and the two rules give the real $8\times8$ table in the eight real coordinates:
$$
(i\tilde X)\star\tilde Y=i(\tilde X\star\tilde Y),\qquad \tilde X\star(i\tilde Y)=-i\,(\tilde X\star\tilde Y).
$$
The first slot is $\mathbb{C}$-linear and the second is $\varsigma$-semilinear, so the two slots carry opposite signs at the central imaginary unit, and the real table is the complex table read with the conjugated scalar in the second factor. No new multiplication appears: restriction of scalars keeps the elements and the products, and it is the field that has moved.

Every property of the product written with the addition, the product, $e_0$ and quantification over the elements is a statement about the ring, and by the dictionary of *The Realification and the Effect of the Change of Scalars* it has the same truth value in the two readings. The unit is the first example and the sharpest: $e_0$ is a right unit in the two readings, $e_0\star\tilde X=\tilde X^{*}$ on the left side and $\tilde X\star e_0=\tilde X$ on the right side, and there is no left unit in either: the left-unit equations admit at most one solution, $\tilde U=e_0$ forced by $\tilde U\star e_0=e_0$, and the candidate fails at $e_1$, where $e_0\star e_1=-e_1\neq e_1$. Associativity fails, at the triple $(e_0,e_1,e_1)$, and so does the Jordan identity, at $x=y=e_1$, the two sides $-e_0$ and $+e_0$ in the two cases; the only product of the twelve that is a Jordan product is that of the symmetrisation $\mathrm{SPA}$, and the block is neither commutative, which $\mathrm{SPA}$ is, nor conjugate-commutative, which $\mathrm{SPS}$ is (*The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*). Every one of these negatives holds in the two readings at the same witnesses.

| | the complex reading | the real reading |
|---|---|---|
| the space | $\mathbb{C}^4$, of complex dimension $4$ | $\mathbb{R}^8$, of real dimension $8$ |
| the product | $\mathbb{C}$-sesquilinear | $\mathbb{R}$-bilinear |
| the kind | a sesqualgebra over $(\mathbb{C},\varsigma)$ | an $\mathbb{R}$-algebra |
| the second slot | $\varsigma$-semilinear, $\varsigma={}^{*}$ on the centre | $\mathbb{C}_{\mathbb{B}}$-conjugate-linear, hence $\mathbb{R}$-linear |
| the unit | $e_0$, a right unit only | $e_0$, a right unit only |
| the form carried | the Hermitian $H$, complex inertia $(4,0)$ | the realified $H$, signature $(8,0)$ |

## The Two Slots and the Centre

Over $\mathbb{C}$ the second slot is $\varsigma$-semilinear, and over $\mathbb{R}$ the same slot is $\mathbb{C}_{\mathbb{B}}$-conjugate-linear. The criterion of §*The Realification of a Linear Map* applies to it: a $\mathbb{C}_{\mathbb{B}}$-conjugate-linear map on $\mathbb{B}$ is $\mathbb{R}$-linear on $\mathbb{R}^8$ and anticommutes with the complex structure,
$$
\Sigma J=-J\Sigma,\qquad J:\tilde Y\mapsto i\tilde Y .
$$

The two families of multiplications of the block have **opposite parities** (*The Left and Right Multiplications of the Biquaternion Sesqualgebra*):
$$
L_{\tilde A}(\tilde X)=\tilde A\star\tilde X\ \text{ is conjugate-linear},\qquad R_{\tilde A}(\tilde X)=\tilde X\star\tilde A\ \text{ is linear},
$$
because the conjugation sits in the second slot alone. Read over $\mathbb{R}$ the two parities are the two summands of the space of the real operators. Every $\mathbb{R}$-linear endomorphism of $\mathbb{R}^8$ splits as the sum of a commuting and an anticommuting one,
$$
\operatorname{End}_{\mathbb{R}}(\mathbb{R}^8)=\operatorname{End}_{\mathbb{C}}(\mathbb{B})\oplus\operatorname{Ant}_{\mathbb{C}}(\mathbb{B}),
$$
of real dimensions $32$ and $32$, and the two families of the block lie in the two different summands:
$$
L_{\tilde A}J=-J L_{\tilde A},\qquad R_{\tilde A}J=+J R_{\tilde A}.
$$
In the real basis the two criteria are the two block shapes,
$$
R_{\tilde A}\rightsquigarrow\begin{pmatrix}A&-B\\B&A\end{pmatrix},\qquad L_{\tilde A}\rightsquigarrow\begin{pmatrix}A&B\\B&-A\end{pmatrix},
$$
the first commuting with $J$ and the second anticommuting with it.

Two consequences follow, the first of them the block's own. First, the right multiplication of the block is the plain right multiplication at the conjugated index, $\tilde X\star\tilde A=\tilde X\tilde A^{*}$, so the right family closes in the **forward** order,
$$
R_{\tilde A}R_{\tilde B}=R_{\tilde A\tilde B},
$$
and $\tilde A\mapsto R_{\tilde A}$ is an injective $\mathbb{R}$-algebra homomorphism of $\mathbb{B}$ into $\operatorname{End}_{\mathbb{R}}(\mathbb{R}^8)$: over $\mathbb{R}$ the right family is the regular representation of the ring by endomorphisms, which neither family is over $\mathbb{C}$, the left multiplications being $\mathbb{C}$-linear in their parameter and conjugate-linear in their argument, the right multiplications the reverse. Over $\mathbb{C}$ the right regular map is conjugate-linear in its parameter, $R_{\lambda\tilde A}=\overline{\lambda}R_{\tilde A}$, and no nonzero left multiplication is $\mathbb{C}$-linear (*the obstruction*); the two statements are the same parity mismatch read on the two sides. Second, the left family does not close, $L_{\tilde A}L_{\tilde B}=T_{\tilde A,\tilde B^{*}}$, and its nonzero composites are two-sided multiplications, hence $\mathbb{C}$-linear, hence no longer left multiplications. The two sides of the block therefore straddle the two summands of $\operatorname{End}_{\mathbb{R}}(\mathbb{R}^8)$, the left multiplications on the conjugate-linear side and the right multiplications on the $\mathbb{C}$-linear one. The general quaternionic sesqualgebra splits in the same way, its second slot carrying the star as well; what belongs to the block alone is the composition of the right family, $R_{\tilde A}R_{\tilde B}=R_{\tilde A\tilde B}$ in the plain product of the parameters, where the general quaternionic sesqualgebra has a two-sided multiplication and no law, since its right multiplication reads the first slot. The block is the right-handed mirror of that structure, whose twist sits in the first slot (*The Specificities of the General Plain Sesqualgebra*).

## The Realified Form

The product carries the general plain sesquilinear form, the Hermitian $H$, which is its scalar part:
$$
H(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\star\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q^{*})=P_0\overline{Q_0}+(\vec P,\overline{\vec Q})=\sum_{\mu=0}^{3}P_\mu\overline{Q_\mu},
$$
with Gram matrix $\mathrm{I}_4$ on the basis $e_0,e_1,e_2,e_3$ and complex inertia $(4,0)$ (*The 4 Forms over the Biquaternion $\mathbb{C}$ Space*). A Hermitian form realifies by the **second rule** of §*The Realification of a Form* of *The Realification and the Effect of the Change of Scalars*: the realification is the real part of the form, which is already real on the diagonal, its imaginary part is alternating and is no part of the realification, and its complex inertia is doubled rather than split. The realified form is therefore
$$
H_{\mathbb{R}}(\tilde P,\tilde Q)=\operatorname{Re}H(\tilde P,\tilde Q)=\sum_{\mu=0}^{3}\bigl(\operatorname{Re}P_\mu\operatorname{Re}Q_\mu+\operatorname{Im}P_\mu\operatorname{Im}Q_\mu\bigr),
$$
the **ordinary Euclidean form** of the eight real coordinates, of Gram matrix $\mathrm{I}_8$ and signature
$$
(8,0).
$$
It is positive definite, and its null set is the single element $0$: the form the block carries has no cone in the real reading, in contrast with the two bilinear forms of the corpus, whose realifications are split of signature $(4,4)$. The entry is the row *Hermitian* of the table of *The Realification of the Four Forms*, §*The Four Gram Matrices*.

The imaginary part of $H$ is not lost in the passage, it is the second face of the form. On the eight real coordinates it is alternating and non-degenerate,
$$
\sigma(\tilde P,\tilde Q)=\operatorname{Im}H(\tilde P,\tilde Q),\qquad \sigma(\tilde P,\tilde Q)=-\sigma(\tilde Q,\tilde P),
$$
a symplectic form of rank $8$, the sum of the canonical pairs of the four coordinate planes $(e_k,ie_k)$, of rank $2$ on the centre and rank $6$ on the vector subspace, tied to the Euclidean $g=H_{\mathbb{R}}$ by the Kähler identity
$$
\sigma(\tilde P,\tilde Q)=g(\tilde P,J\tilde Q),
$$
so that the complex form the block carries shows in the real reading its two faces, the Euclidean $g=H_{\mathbb{R}}$ and the alternating $\sigma$ (*Remarkable Subspaces and the Four Forms*).

The complex structure **preserves** the form,
$$
H_{\mathbb{R}}(J\tilde P,J\tilde Q)=+H_{\mathbb{R}}(\tilde P,\tilde Q),
$$
the opposite of the case of a bilinear form. The map $J$ is therefore an isometry of the Euclidean form, an element of the orthogonal group $O(8)$ in the real basis, and the $\mathbb{C}$-linear endomorphisms that preserve $H$ form the unitary group $U(4)$.

The square of the block is positive for this form. The element $\tilde Q\star\tilde Q=\tilde Q\tilde Q^{*}$ is Hermitian, and its scalar part is the squared Euclidean norm,
$$
\mathrm{Sc}(\tilde Q\star\tilde Q)=H(\tilde Q,\tilde Q)=\sum_{\mu=0}^{3}\lvert Q_\mu\rvert^2 ,
$$
so the diagonal of the realified Hermitian form is the square of the real norm of the element, and the form the block carries is the positive definite one of the four forms of the corpus.

## What the Interpretation Leaves Untouched

Since $i$ lies in $\mathbb{B}$, an additive subgroup closed under left multiplication by every element is closed under multiplication by $i$, and the ideals, the idempotents, the zero divisors, the nilpotents and the units are the same in the two readings. The statement concerns the two readings of the block and not the block against the ring: the classes are cut out of the ring's for the product $\star$. The zero-divisor set of $\star$ is the cone of the norm and the common set of the four general products, and the invertibility criterion is the non-vanishing of $N(\tilde P)=\tilde P\tilde P^{\natural}$ (*Zero Divisors of the General Plain Sesqualgebra*, *Norm and Invertibility in the General Plain Sesqualgebra*); the idempotents of the block are the Hermitian ones, and its nilpotents are those of the ring with the index moved from two to three. The right unit, the right ideals and the multiplicative monoid are the plain ones read at the conjugated index (*The Specificities of the General Plain Sesqualgebra*).

What the real reading adds is the **count**: each of those classes becomes an eight-dimensional real problem with a dimension of its own.

| class | the condition | over $\mathbb{C}$ | over $\mathbb{R}$ |
|---|---|---|---|
| the zero divisors of the block | $N(\tilde Q)=0$, $\tilde Q\neq0$ | complex dimension $3$ | real dimension $6$ |
| the nilpotents of the block | $Q_0=0$, $(\vec Q,\vec Q)=0$, $\tilde Q\neq0$, of index three | complex dimension $2$ | real dimension $4$ |
| the idempotents of the block | $\tilde Q\star\tilde Q=\tilde Q$, hence Hermitian | — | real dimension $2$ |
| the projectors of the right family | $\tilde Q\tilde Q=\tilde Q$ | complex dimension $2$ | real dimension $4$ |

The two last rows are read off in one line each, and the two lines use the involution. If $\tilde Q\star\tilde Q=\tilde Q$, that is $\tilde Q\tilde Q^{*}=\tilde Q$, then applying the star to the equation gives $\tilde Q\tilde Q^{*}=\tilde Q^{*}$, since $(XY)^{*}=Y^{*}X^{*}$; comparing the two displays gives $\tilde Q=\tilde Q^{*}$, so the idempotents of the block are the **Hermitian** idempotents of the plain product: the trivial pair $0,e_0$ and the two-sphere of the directions $\tfrac12(e_0+\hat u i)$ over the real unit vectors $\hat u$, a set of real dimension two (*Square Roots of One and the Idempotents of the General Plain Sesqualgebra*). The elements whose right multiplication is a projector are the plain idempotents, a complex two-dimensional family, of real dimension four; so the parameters of the projectors form a family of real dimension four where the idempotents of the block form one of real dimension two, and the factor of two is the one the change of scalars introduces in this article everywhere else. The zero divisor is read the same way: for $\tilde Q$ with $N(\tilde Q)=0$ the partner $\tilde X=(\tilde Q^{\natural})^{*}$ is nonzero and satisfies $\tilde Q\star\tilde X=\tilde Q\tilde Q^{\natural}=0$, so the cone of the norm is a cone of zero divisors in the two readings. The nilpotent row is the sharpest of the four: the square of the block is positive, $\mathrm{Sc}(\tilde Q\star\tilde Q)=\sum_\mu\lvert Q_\mu\rvert^{2}$, so the block has no nonzero square-zero element, and its nilpotents are reached at the third power, where they coincide with the pure zero divisors of the ring (*Square Roots of Zero and the Nilpotents of the General Plain Sesqualgebra*).

## The Real Operators

The left and the right multiplications are $\mathbb{R}$-linear endomorphisms of $\mathbb{R}^8$, by §*The Realification of a Linear Map* of *The Realification and the Effect of the Change of Scalars*, and so are the other two kinds of operator they generate, the sesquilinear sandwich and the ordinary two-sided multiplication,
$$
S_{\tilde P,\tilde Q}(\tilde X)=\tilde P\tilde X^{*}\tilde Q^{*},\qquad T_{\tilde P,\tilde Q}(\tilde X)=\tilde P\tilde X\tilde Q .
$$
The four kinds split by parity in the same way as the two families: $T$ and $R$ are $\mathbb{C}$-linear and commute with $J$, $S$ and $L$ are conjugate-linear and anticommute with $J$. The composition laws are those of *The Left and Right Multiplications of the Biquaternion Sesqualgebra*, and they are laws of the real operators:
$$
L_{\tilde A}L_{\tilde B}=T_{\tilde A,\tilde B^{*}},\qquad R_{\tilde A}R_{\tilde B}=R_{\tilde A\tilde B},\qquad L_{\tilde A}R_{\tilde B}=L_{\tilde A\tilde B},\qquad R_{\tilde A}L_{\tilde B}=S_{\tilde B,\tilde A}.
$$
The right family is a monoid under composition, generated by the right multiplications alone and isomorphic to the multiplicative monoid of $\mathbb{B}$ in the forward order; the left family is not, and its square lands in the two-sided multiplications; the ordinary two-sided multiplication and the sandwich are the two operators of *The Sesquilinear Sandwich on the Biquaternions*, and the two-sided operator $\tilde X\mapsto\tilde Q\tilde X\tilde Q^{*}$ is that of *Two-Sided Operators on the General Plain Sesqualgebra of Biquaternions*. The adjoints of the four kinds for the form $H$ are the one calculus of *The Adjoint of the Sesquilinear Sandwich on the Biquaternions*, which carries the two one-sided families, the ordinary two-sided multiplication and the sandwich, and those for the realified forms are of the real-linear kind, the Euclidean adjoint being the one of the form of this article. The inversion of the operators is a statement about the ring and does not move: $\bigl(R_{\tilde A}\bigr)^{-1}=R_{\tilde A^{-1}}$ on the units, whose criterion is $N(\tilde A)\neq0$ as before.

## Summary

The general plain sesqualgebra read over $\mathbb{R}$ is the same product on the same elements, an $\mathbb{R}$-algebra on $\mathbb{R}^8$ in the broad sense whose second slot stays $\mathbb{C}_{\mathbb{B}}$-conjugate-linear, with $e_0$ a right unit and no left unit. The two sides of the product have opposite parities, and over $\mathbb{R}$ they fall into the two summands of $\operatorname{End}_{\mathbb{R}}(\mathbb{R}^8)$, the left multiplications into the conjugate-linear summand and the right multiplications into the $\mathbb{C}$-linear one, where they form a monoid in the forward order and give an honest representation of the algebra. The product carries the Hermitian form $H$, whose realification is the Euclidean form of the eight real coordinates, of signature $(8,0)$ and empty null set, with the alternating companion $\sigma=\operatorname{Im}H$ of rank $8$, preserved by the complex structure; the square of the block is Hermitian and $H$-positive. The ideals, the idempotents, the zero divisors, the nilpotents and the units are the same as over $\mathbb{C}$, and the real reading adds their real dimensions — six for the zero-divisor cone, four for the nilpotents and for the parameters of the projectors, two for the idempotents the block recognises as its own. Nothing new is multiplied; the field, the dimension and the linear structure have changed, and with them the form the product carries and the shape of its operators.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ | the product of the general plain sesqualgebra |
| $\mathbb{R}^8$ | the realification of $\mathbb{B}$, the eight real basis elements $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$ |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ | the centre of the ring, read as the field of scalars |
| $J$ | the complex structure, multiplication by $i$, of square $-1$ |
| $L_{\tilde A}J=-JL_{\tilde A}$ | the left multiplications, conjugate-linear, the anticommuting summand |
| $R_{\tilde A}J=+JR_{\tilde A}$, $R_{\tilde A}(\tilde X)=\tilde X\tilde A^{*}$ | the right multiplications, $\mathbb{C}$-linear, the commuting summand; the plain right multiplication at the conjugated index |
| $H(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\star\tilde Q)=\sum_\mu P_\mu\overline{Q_\mu}$ | the Hermitian form the product carries |
| $(8,0)$ | the signature of its realification, the Euclidean form of the eight real coordinates |
| $g=H_{\mathbb{R}}$, $\sigma=\operatorname{Im}H$ | the Euclidean form and its companion, $\sigma(\tilde P,\tilde Q)=g(\tilde P,J\tilde Q)$, of rank $8$ |
| $N(\tilde P)=\tilde P\tilde P^{\natural}$ | the biquaternion norm, whose vanishing cuts the zero divisors and whose non-vanishing is the criterion of the units of the block |
| $S_{\tilde P,\tilde Q}$, $T_{\tilde P,\tilde Q}$ | the sesquilinear sandwich and the ordinary two-sided multiplication |

## Further Reading

- *The Realification and the Effect of the Change of Scalars* (`articles_maths/the-realification-and-the-effect-of-the-change-of-scalars.md`), for the general construction, the two criteria of linearity, the two rules of the realification of a form and the table of the four effects.
- *The Realification of the Four Forms* (`articles_maths/the-realification-of-the-four-forms.md`), for the general case applied to the four forms of the corpus, of which the row *Hermitian* is the form of this article.
- *The Realification of the General Plain Algebra* (`articles_maths/the-realification-and-the-effect-of-the-change-of-scalars.md`), the entry of the neighbouring block over $\mathbb{R}$, for the ring itself: the eight real coordinates, the multiplication table of the plain product and the real regular module.
- *The Left and Right Multiplications of the Biquaternion Sesqualgebra* (`articles_maths/the-left-and-right-multiplications-of-the-biquaternioid-sesqualgebra.md`) and *The Specificities of the General Plain Sesqualgebra* (`articles_maths/the-specificities-of-the-general-plain-sesqualgebra.md`), for the two parities, the composition laws, the projector criterion and the right-composition law of the block.
- *Zero Divisors of the General Plain Sesqualgebra* (`articles_maths/zero-divisors-of-the-general-plain-sesqualgebra.md`), *Norm and Invertibility in the General Plain Sesqualgebra* (`articles_maths/norm-and-invertibility-in-the-general-plain-sesqualgebra.md`), *Square Roots of One and the Idempotents of the General Plain Sesqualgebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-general-plain-sesqualgebra.md`) and *Square Roots of Zero and the Nilpotents of the General Plain Sesqualgebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-general-plain-sesqualgebra.md`), for the classes of the block whose real dimensions this article counts.
