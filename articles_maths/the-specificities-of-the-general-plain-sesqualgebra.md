# __The Specificities of the General Plain Sesqualgebra__

## Introduction

The general plain sesqualgebra is the operation $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ on the biquaternion space, the general plain sesquilinear product read as a multiplication (*Introduction to the General Plain Sesqualgebra of Biquaternions*). As an element-theoretic object the block is poor: it has a right unit and no left one, no invertible element in the strict sense, no root of $-1$ and no root of $0$, and its only idempotents are the Hermitian ones. As an **operator-theoretic** object it is the opposite, and in a way that no other structure of the twelve reproduces. This article isolates that way and states it as a **criterion** of the block.

The criterion is a **composition law of the right multiplications**, and it is an identity about the product itself:

$$
\text{(C)}\qquad R^{\star}_{\tilde P}R^{\star}_{\tilde Q}=R^{\star}_{\tilde P\tilde Q}\qquad\text{for all }\tilde P,\tilde Q,
$$

where $R^{\star}_{\tilde P}(\tilde X)=\tilde X\star\tilde P$ and the index $\tilde P\tilde Q$ on the right is the **plain** product of the two parameters. The block satisfies C in the **forward** order, and it is the only structure of the twelve that does on the right. The plain product satisfies the **reversed** law, $R_{\tilde P}R_{\tilde Q}=R_{\tilde Q\tilde P}$, so its right multiplications give the **opposite** monoid, and its left multiplications give the monoid, in the forward order; the general quaternionic product carries its one-sided law on the **left**, in the reversed order, so it too gives the opposite monoid (*The Specificities of the General Quaternionic Algebra*); and the remaining nine structures satisfy no one-sided composition law at all. In the whole of the twelve there are therefore exactly three structures with a one-sided law, each on one side and in one order: the plain product, the general quaternionic product and the block. The block is the unique one in which the law is on the **right** and in the **forward** order, and it holds because its right multiplications are the **plain** right multiplications at the conjugated index, an **isotopy** of the plain algebra. Everything peculiar to the block on the operator side follows from this one identity: the projector family is the family of the plain idempotents, the right ideals coincide with the plain right ideals, and the left multiplications, being conjugate-linear, have no projector but the zero operator.

**Placement.** The article is the closing entry of the *Specific Theory* section of the block. It belongs to the family that *The Specificities of the General Plain Algebra* began and that *The Specificities of the General Quaternionic Algebra* and *The Specificities of the Symmetric Quaternionic Algebra* continued, and it is the mirror of the general quaternionic entry: that article reads the **left** multiplications and the left ideals, this one reads the **right**.

**Boundaries.** The product, its class, its table and its placement among the twelve are *Introduction to the General Plain Sesqualgebra of Biquaternions*; the plain right and left multiplications $R_{\tilde C}$, $L_{\tilde B}$, their adjoints, their types and the double centraliser are *One-Sided Operators on the General Plain Sesqualgebra of Biquaternions*, and their double-sided product is *Two-Sided Operators on the General Plain Sesqualgebra of Biquaternions*. The twelve products of the twelve structures are *The 12 Products of the Biquaternion Complex Space*, and the general comparison is *The Specificities of the General Plain Algebra*. The norm, the zero-divisor set, the idempotents and the nilpotents are *Norm and Invertibility in the General Plain Sesqualgebra*, *Zero Divisors of the General Plain Sesqualgebra*, *Square Roots of One and the Idempotents of the General Plain Sesqualgebra* and *Square Roots of Zero and the Nilpotents of the General Plain Sesqualgebra*; the matrix model in which the dictionary below is the identity is *The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*. Nothing topological and nothing metric appears.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ with $e_1e_2=e_3$ and central scalar imaginary $i$. Juxtaposition is the **plain** product $\tilde P\tilde Q$ and $\star$ is the block, $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$. The natural conjugation is $\tilde Q^{\natural}=Q_0-\mathbf Q$, the coefficientwise conjugation is $\overline{\tilde Q}=\overline{Q_0}e_0+\overline{\mathbf Q}$, the Hermitian conjugation is $\tilde Q^{*}=\overline{\tilde Q^{\natural}}$, and $\eta$ is the involution ${}^{*}$ read as an operator, $\eta(\tilde Q)=\tilde Q^{*}$. The **left** and the **right multiplications of the block** by $\tilde P$ are the operators

$$
L^{\star}_{\tilde P}(\tilde X)=\tilde P\star\tilde X,\qquad R^{\star}_{\tilde P}(\tilde X)=\tilde X\star\tilde P ,
$$

the superscript $\star$ distinguishing them from the plain operators $L_{\tilde P}(\tilde X)=\tilde P\tilde X$ and $R_{\tilde P}(\tilde X)=\tilde X\tilde P$ of *One-Sided Operators on the General Plain Sesqualgebra of Biquaternions*. The subscript is the element and never the operator, so $R^{\star}_{\tilde P}R^{\star}_{\tilde Q}$ is the composite. An element of the twelve is written $\circ$; a **projector** is an idempotent operator, and the zero operator is one.

## The Isotope Identity

**Theorem (the dictionary).** For every $\tilde P$,

$$
R^{\star}_{\tilde P}=R_{\tilde P^{*}},\qquad L^{\star}_{\tilde P}=L_{\tilde P}\,\eta,\qquad R^{\star}_{\tilde P}=\eta\,L^{\star}_{\tilde P},\qquad L^{\star}_{\tilde P}=\eta\,R^{\star}_{\tilde P} .
$$

The right multiplication of the block is the **plain right multiplication at the conjugated index**; the left multiplication of the block is the **plain left multiplication composed with the involution**, hence conjugate-linear; and the involution $\eta$ carries each one-sided family to the other, $R^{\star}_{\tilde P}=\eta\circ L^{\star}_{\tilde P}$ and $L^{\star}_{\tilde P}=\eta\circ R^{\star}_{\tilde P}$.

*Proof.* The first identity is $R^{\star}_{\tilde P}(\tilde X)=\tilde X\star\tilde P=\tilde X\tilde P^{*}=R_{\tilde P^{*}}(\tilde X)$. The second is $L^{\star}_{\tilde P}(\tilde X)=\tilde P\star\tilde X=\tilde P\tilde X^{*}=L_{\tilde P}(\eta(\tilde X))$. For the third, $\eta\bigl(L^{\star}_{\tilde P}(\tilde X)\bigr)=\eta(\tilde P\tilde X^{*})=\bigl(\tilde P\tilde X^{*}\bigr)^{*}=\tilde X\tilde P^{*}=R^{\star}_{\tilde P}(\tilde X)$, using that ${}^{*}$ is an involution; the fourth is the same relation with the two sides exchanged.

**Corollary (linearity, faithfulness, the unit).** The right multiplications $R^{\star}_{\tilde P}$ are $\mathbb{C}$-**linear** and faithful in $\tilde P$; the left multiplications $L^{\star}_{\tilde P}$ are **conjugate-linear** and faithful; $R^{\star}_{e_0}=\mathrm{id}$ is the right unit and $L^{\star}_{e_0}=\eta$ is the involution.

*Proof.* The plain $R$ and $L$ are $\mathbb{C}$-linear and $\eta$ is conjugate-linear; faithfulness is that of the plain operators, since $\eta$ and ${}^{*}$ are bijections. The unit statements are $\tilde X\star e_0=\tilde X e_0^{*}=\tilde X$ and $e_0\star\tilde X=e_0\tilde X^{*}=\tilde X^{*}$.

**Remark (the price of the dictionary).** In the matrix model $\mathsf{M}_2$ the identities read $\mathsf{M}_2(R^{\star}_{\tilde P}\tilde X)=\mathsf{M}_2(\tilde X)\mathsf{M}_2(\tilde P)^{\dagger}$ and $\mathsf{M}_2(L^{\star}_{\tilde P}\tilde X)=\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde X)^{\dagger}$: the right multiplication is right multiplication by the conjugate transpose, and the left multiplication is left multiplication by it. Every statement below is an element statement about the plain algebra with a conjugated index, and the operator is linear on the right and conjugate-linear on the left. The asymmetry between the two sides is the content of the corollary on the projectors.

## The Criterion

**Definition (the right-composition law).** The right multiplications of a product $\circ$ on $\mathbb{B}$ are the operators $R^{\circ}_{\tilde P}(\tilde X)=\tilde X\circ\tilde P$. They satisfy the **right-composition law** when they compose in the **forward** order and are indexed by the **plain** product of the two parameters, juxtaposition being the plain product,

$$
R^{\circ}_{\tilde P}R^{\circ}_{\tilde Q}=R^{\circ}_{\tilde P\tilde Q}\qquad\text{for all }\tilde P,\tilde Q,
$$

and they satisfy the **reversed** law when $R^{\circ}_{\tilde P}R^{\circ}_{\tilde Q}=R^{\circ}_{\tilde Q\tilde P}$.

**Theorem (the criterion).** The block satisfies the right-composition law, with the index read in the plain product of the two parameters:

$$
R^{\star}_{\tilde P}R^{\star}_{\tilde Q}=R^{\star}_{\tilde P\tilde Q}\qquad\text{for all }\tilde P,\tilde Q .
$$

*Proof.* By the dictionary $R^{\star}_{\tilde P}R^{\star}_{\tilde Q}=R_{\tilde P^{*}}R_{\tilde Q^{*}}=R_{\tilde Q^{*}\tilde P^{*}}$, the plain composition law being the reversed one. And $\tilde Q^{*}\tilde P^{*}=(\tilde P\tilde Q)^{*}$, because ${}^{*}$ is an anti-automorphism; so the composite is $R_{(\tilde P\tilde Q)^{*}}=R^{\star}_{\tilde P\tilde Q}$, which is the display.

**Corollary (the right multiplications form a monoid).** The family $\{R^{\star}_{\tilde P}:\tilde P\in\mathbb{B}\}$ is stable under composition, and the assignment $\tilde P\mapsto R^{\star}_{\tilde P}$ is a **monoid isomorphism** from the multiplicative monoid $(\mathbb{B},\cdot)$ onto it, in the **forward** order. Consequently the block's right multiplications are a copy of the plain multiplicative monoid, and not of its opposite.

*Proof.* The law gives closure and the multiplicativity of the assignment; it is injective by the faithfulness of the dictionary, and it is onto its image by construction. The forward order is the law itself, as opposed to the plain law $R_{\tilde P}R_{\tilde Q}=R_{\tilde Q\tilde P}$.

**Remark (why the block and no other).** Exactly three of the twelve structures carry a one-sided composition law, and the table of §*The Isolation among the Twelve* records which. The plain product carries it on both sides, forward on the left and reversed on the right; the general quaternionic product carries it on the left and reversed; the block carries it on the right and forward. The block is the structure in which the forward order is carried by the **right** multiplications, and this is exactly the statement that the twist sits in the second slot and is an anti-automorphism: the conjugation in $\tilde P\tilde Q^{*}$ reverses the order of the plain product, and the reversal, read on the right multiplications, undoes the reversal of the composition. In the nine remaining structures neither side closes, and the reason is the same in every case: a derived part mixes the two slots, and the two products that are not the plain one conjugate a slot, which turns a one-sided multiplication into an operator carrying two independent parameters. The left multiplications of the block do not form a monoid, because the twist is in the slot a left multiplication reads: $L^{\star}_{\tilde P}L^{\star}_{\tilde Q}=L_{\tilde P}\eta L_{\tilde Q}\eta=L_{\tilde P}R_{\tilde Q^{*}}$, a **mixed** operator of the two independent parameters $\tilde P,\tilde Q$, which is a two-sided operator only in the diagonal case $\tilde Q=\lambda\tilde P^{*}$ (*Mixed Inner Conjugation on the General Plain Sesqualgebra of Biquaternions*), and is not the left multiplication of the block at any single element in general.

## The Isolation among the Twelve

**Theorem (the specificity).** Of the twelve structures of *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, the general plain sesqualgebra is the only one whose right multiplications satisfy the right-composition law in the **forward** order.

*Proof.* The block satisfies it by §*The Criterion*. The other eleven are the three remaining general products together with the eight parts got by symmetrising or antisymmetrising the four. The three general products are disposed of by the table below: $\tilde P\tilde Q$ carries the forward law on the left and the reversed law on the right, $\tilde P^{\natural}\tilde Q$ carries the reversed law on the left, $\tilde P\tilde Q^{*}$ is the block, and $\tilde P^{\natural}\tilde Q^{*}$ conjugates both slots and closes on neither side. Each of the eight derived parts mixes the two slots in its multiplication, $R^{\circ}_{\tilde P}(\tilde X)=\tfrac12(\tilde X\circ\tilde P\pm\tilde P\circ\tilde X)$, so the composite of two of them is a sum of four products and is not a single multiplication at any element in general.

| family | members | right law | left law |
|---|---|---|---|
| general | GPA, GQA, **GPS**, GQS | reversed, none, **forward**, none | forward, reversed, none, none |
| symmetric | SPA, SQA, SPS, SQS | none | none |
| antisymmetric | APA, AQA, APS, AQS | none | none |

Only three of the twelve carry a one-sided law, each on one side: the plain product (forward on the left, reversed on the right), the general quaternionic product (reversed, on the left) and the block (forward, on the right). The block is the unique one whose law is on the right and in the forward order, and the reason is that its twist sits in the second slot alone and is an anti-automorphism: the conjugation reverses the order of the plain product, and that reversal, read on the right multiplications, undoes the reversal of the plain composition. In the nine others neither side closes, because a derived part mixes the two slots or because a product conjugates a slot. The left multiplications of the block close nowhere either, because the twist is in the slot a left multiplication reads: $L^{\star}_{\tilde P}L^{\star}_{\tilde Q}=L_{\tilde P}\eta L_{\tilde Q}\eta=L_{\tilde P}R_{\tilde Q^{*}}$, a **mixed** operator of the two independent parameters $\tilde P,\tilde Q$, a two-sided operator only in the diagonal case $\tilde Q=\lambda\tilde P^{*}$ (*Mixed Inner Conjugation on the General Plain Sesqualgebra of Biquaternions*).

## The Projectors

**Theorem (the projector criterion).** The operator $R^{\star}_{\tilde P}$ is a projector if and only if $\tilde P$ is an idempotent of the plain product, and the operator $L^{\star}_{\tilde P}$ is a projector if and only if $\tilde P=0$.

*Proof.* By the composition law $R^{\star}_{\tilde P}{}^{2}=R^{\star}_{\tilde P\tilde P}$, and by faithfulness the equality $R^{\star}_{\tilde P}{}^{2}=R^{\star}_{\tilde P}$ is $\tilde P\tilde P=\tilde P$. For the left side, $L^{\star}_{\tilde P}$ is conjugate-linear, and its composite with itself is $\mathbb{C}$-linear; a conjugate-linear operator equal to a $\mathbb{C}$-linear one is zero, so $L^{\star}_{\tilde P}{}^{2}=L^{\star}_{\tilde P}$ forces $L^{\star}_{\tilde P}=0$, that is $\tilde P=0$ by faithfulness.

**Corollary (the family of projectors, and the disowning).** The elements whose right multiplication is a projector are the plain idempotents: $0$, $e_0$ and the family $\tfrac12(e_0+\tilde\Xi)$ over the pure roots $\tilde\Xi$ of $+1$, of complex dimension two. The idempotents of the block itself are only the **Hermitian** ones, $0$, $e_0$ and the $\tfrac12(e_0+i\hat\mu)$ over the real unit vectors $\hat\mu$, a family of real dimension two.

*Proof.* By the criterion and by *Idempotents of the General Plain Algebra*, whose idempotents are $0$, $e_0$ and the $\tfrac12(e_0+\tilde\Xi)$ with $\tilde\Xi^{2}=e_0$. The idempotents of the block are computed in *Square Roots of One and the Idempotents of the General Plain Sesqualgebra*: they are the Hermitian idempotents of the algebra, $0$, $e_0$ and the $\tfrac12(e_0+i\hat\mu)$.

**Remark (the mirror of the general quaternionic case).** The block has a full complex two-dimensional family of projectors and recognizes as its own idempotents only the real two-dimensional Hermitian subfamily; the general quaternionic product has the same full family of projectors on the **left** and the same two idempotents. The two articles are the two sides of one phenomenon, the isotope with a conjugated index: the projectors come from the plain idempotents, and the idempotents of the structure are the elements whose own square is themselves, which the conjugation generally destroys. The count of the projectors is that of *One-Sided Operators on the General Plain Sesqualgebra of Biquaternions*, read through the dictionary.

## The One-Sided Ideals

**Theorem (the right ideals coincide and the left ones do not).** Let $I$ be a subspace of $\mathbb{B}$. Then

$$
I\ \text{is a right ideal of }\star\iff I\ \text{is a right ideal of the plain product},
$$

and

$$
I\ \text{is a left ideal of }\star\iff I\ \text{is a left ideal of the plain product and }I^{*}=I .
$$

*Proof.* $I$ is a right ideal of $\star$ when $I\star\mathbb{B}\subseteq I$, and $I\star\tilde P=I\tilde P^{*}$, so $I\star\mathbb{B}=I\mathbb{B}$ because $\tilde P\mapsto\tilde P^{*}$ is a bijection; hence the first equivalence. For the second, $I$ is a left ideal of $\star$ when $\mathbb{B}\star I\subseteq I$, that is $\mathbb{B}I^{*}\subseteq I$. Taking the parameter $e_0$, whose left action is the involution, gives $I^{*}\subseteq I$, and the two spaces have the same dimension, so $I^{*}=I$; with that, $\mathbb{B}I^{*}=\mathbb{B}I\subseteq I$ is exactly the plain left-ideal condition, and the converse is immediate.

**Corollary (the asymmetry).** The right ideals of the block are exactly those of the plain product, with no further condition, and they are as many as in the matrix algebra: the minimal ones are the $\tilde\Pi\mathbb{B}$ over the primitive plain idempotents. The left ideals are only the two trivial ones, $0$ and $\mathbb{B}$, and the block has no proper nonzero left ideal.

*Proof.* The two displays are the theorem, and a subspace stable under the involution is not a further condition but a strong one. For the sharpening, let $I$ be a left ideal of $\star$, so $I^{*}=I$ and $\mathbb{B}I\subseteq I$. For $x\in I$ and $y\in\mathbb{B}$ the element $y^{*}x^{*}$ lies in $\mathbb{B}I\subseteq I$, hence $xy=(y^{*}x^{*})^{*}$ lies in $I^{*}=I$; therefore $I\mathbb{B}\subseteq I$ and $I$ is two-sided. By the simplicity of $\mathbb{B}$ (*The Biquaternion Sesqualgebra Is Simple*) a two-sided ideal is $0$ or $\mathbb{B}$. The strictness on the left is witnessed by a primitive plain idempotent $\tilde\Pi$: the space $\mathbb{B}\tilde\Pi$ is a minimal **left** ideal of the plain product, and $(\mathbb{B}\tilde\Pi)^{*}=\tilde\Pi^{*}\mathbb{B}\neq\mathbb{B}\tilde\Pi$, so it is not stable and not a left ideal of the block, while the space $\tilde\Pi\mathbb{B}$ is a minimal **right** ideal of the plain product and is a right ideal of the block.

**Remark (the right is the faithful side).** The block is **right-faithful**: its right ideals, its projectors and its multiplicative monoid are the plain ones, read at the conjugated index, and the right side carries the associative theory without loss. The left side does not: it carries the involution, which is conjugate-linear, and its one-sided theory collapses to the two trivial ideals. The general quaternionic product is the mirror image, left-faithful and right-blind; the two articles are read together, and the pair is the element-level statement that the twist of the two sesquilinear products sits in the two different slots.

## The Involution and the Inversion

**Corollary (the involution exchanges the two families).** For every $\tilde P$,

$$
R^{\star}_{\tilde P}=\eta\,L^{\star}_{\tilde P},\qquad L^{\star}_{\tilde P}=\eta\,R^{\star}_{\tilde P},\qquad \eta\,R^{\star}_{\tilde P}\,\eta=L_{\tilde P},\qquad (R^{\star}_{\tilde P})^{-1}=R^{\star}_{\tilde P^{-1}} ,
$$

the last on the invertible elements, where $\tilde P^{-1}$ is the plain inverse and the inverse is the operator inverse.

*Proof.* The first two are the dictionary. For the third, $\eta R^{\star}_{\tilde P}\eta(\tilde X)=\eta\bigl(\eta(\tilde X)\star\tilde P\bigr)=\eta\bigl(\tilde X^{*}\tilde P^{*}\bigr)=\bigl(\tilde X^{*}\tilde P^{*}\bigr)^{*}=\tilde P\tilde X=L_{\tilde P}(\tilde X)$. For the fourth, $R^{\star}_{\tilde P}=R_{\tilde P^{*}}$ is invertible exactly when $\tilde P^{*}$ is a plain unit, that is exactly when $\tilde P$ is, and $(R_{\tilde P^{*}})^{-1}=R_{(\tilde P^{*})^{-1}}=R_{(\tilde P^{-1})^{*}}=R^{\star}_{\tilde P^{-1}}$.

**Remark (the inverse of the block at the operator level).** The invertibility criterion of the block is the non-vanishing of the norm $N(\tilde P)=\tilde P\tilde P^{\natural}$ (*Norm and Invertibility in the General Plain Sesqualgebra*), and the operator family carries the plain group of units $\mathbb{B}^{\times}$ faithfully; the operator inverse is indexed by the **plain** inverse, $(R^{\star}_{\tilde P})^{-1}=R^{\star}_{\tilde P^{-1}}$, and the block's own inverse, $\tilde P^{-1\star}=(\tilde P^{-1})^{*}$, is the star-conjugate of the plain one. The right multiplication is the side that carries the plain inverse, and the involution ${}^{*}$ moves between the two, which is the operator form of the fact that the two slots of the block are not symmetric. The involution $P\mapsto P^{-1\star}$ of the block is treated with the two-sided operators in *Mixed Inner Conjugation on the General Plain Sesqualgebra of Biquaternions*.

## The Consequence

**Corollary (what belongs to the block alone).** The block is the only one of the twelve whose right multiplications satisfy the forward composition law $R^{\star}_{\tilde P}R^{\star}_{\tilde Q}=R^{\star}_{\tilde P\tilde Q}$, and it is for this reason the only one whose **right** side carries the plain theory: the right projector criterion is read on the plain idempotents, the right ideals coincide with the plain right ideals, and the right multiplications are a faithful copy of the multiplicative monoid in the forward order. Its **left** side does not: the left multiplications are conjugate-linear, their only projector is the zero operator, and the left ideals collapse to $0$ and $\mathbb{B}$. The general quaternionic product is the mirror image on the left, in the reversed order, and the general plain product is the associative case in which the left order is forward and the right order is reversed.

**Remark (the criterion and the family of the specificities).** The specificities of the general plain algebra read the left-alternativity identity $L_{\tilde X}^{2}=L_{\tilde X\circ\tilde X}$; the specificities of the general quaternionic algebra read the isotope identity $L_{\tilde P}=L_{\tilde P^{\natural}}$ with its projector criterion on the left; the specificities of the symmetric quaternionic algebra read the identity $L_{\tilde X}^{2}=X_0L_{\tilde X}$; and the specificities of the symmetric plain sesqualgebra read the two clauses conjugate-commutativity and centrality. The present article reads the **right-composition law**, which is the forward-order identity of the right multiplications, and it is the only one of the family stated on that side. The four criteria are independent, and each identifies the block for which it is stated against the other eleven.

## Summary

The general plain sesqualgebra satisfies the **right-composition law** $R^{\star}_{\tilde P}R^{\star}_{\tilde Q}=R^{\star}_{\tilde P\tilde Q}$ in the **forward** order, and it is the **only** one of the twelve structures that does. The law is the operator form of the isotope identity $R^{\star}_{\tilde P}=R_{\tilde P^{*}}$, the right multiplication of the block being the plain right multiplication at the **conjugated** index; because the conjugation is an anti-automorphism, the reversal it introduces cancels the reversal of the plain composition law, and the right multiplications of the block form a monoid **isomorphic** (not anti-isomorphic) to the multiplicative monoid of the algebra. Exactly three of the twelve structures carry a one-sided law: the plain product (forward on the left, reversed on the right), the general quaternionic product (reversed, on the left), and the block (forward, on the right); the general quaternionic sesquilinear product and the eight derived parts satisfy none. The consequences are the operator face of the block: the **projector criterion** is that $R^{\star}_{\tilde P}$ is a projector exactly when $\tilde P$ is a plain idempotent, a family of complex dimension two, while the block's own idempotents are only the Hermitian ones, of real dimension two; the left multiplications are conjugate-linear with no projector but the zero operator; the **right ideals** of the block are exactly the plain right ideals, and the **left ideals** collapse to the two trivial ones, $0$ and $\mathbb{B}$, so the block is right-faithful and left-blind; and the involution exchanges the two families, $\eta R^{\star}_{\tilde P}\eta=L_{\tilde P}$, with $(R^{\star}_{\tilde P})^{-1}=R^{\star}_{\tilde P^{-1}}$ on the units. The block is the right-handed mirror of the general quaternionic product, and the pair of criteria is the element-level statement that the twist of the two sesquilinear products sits in the two different slots.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ | the product of the block |
| $R^{\star}_{\tilde P}(\tilde X)=\tilde X\star\tilde P$ | the right multiplication of the block |
| $L^{\star}_{\tilde P}(\tilde X)=\tilde P\star\tilde X$ | the left multiplication of the block, conjugate-linear |
| $R^{\circ}_{\tilde P}R^{\circ}_{\tilde Q}=R^{\circ}_{\tilde P\tilde Q}$ | the right-composition law, the criterion, the index in the plain product |
| $R^{\star}_{\tilde P}=R_{\tilde P^{*}}$ | the isotope identity, the dictionary |
| $L^{\star}_{\tilde P}=L_{\tilde P}\eta$ | the left multiplication is plain-composed-with-the-involution |
| $\eta\,R^{\star}_{\tilde P}\,\eta=L_{\tilde P}$ | the involution conjugated reads the plain left multiplication |
| $R^{\star}_{\tilde P}=\eta L^{\star}_{\tilde P}$ | the involution exchanges left and right |
| $R^{\star}_{\tilde P}$ a projector $\iff\tilde P$ a plain idempotent | the projector criterion |
| $L^{\star}_{\tilde P}$ a projector $\iff\tilde P=0$ | the collapse on the left |
| $I\star\mathbb{B}\subseteq I\iff I$ plain right ideal | the right ideals coincide |
| $\mathbb{B}\star I\subseteq I\iff I$ plain left ideal with $I^{*}=I$ | the left ideals are the two trivial ones, $0$ and $\mathbb{B}$ |
| $(R^{\star}_{\tilde P})^{-1}=R^{\star}_{\tilde P^{-1}}$ | the operator inverse, indexed by the plain inverse |

## Further Reading

- *The Specificities of the General Plain Algebra* (`articles_maths/the-specificities-of-the-general-plain-algebra.md`), for the criterion of left alternativity and the family of criteria this article closes.
- *The Specificities of the General Quaternionic Algebra* (`articles_maths/the-specificities-of-the-general-quaternionic-algebra.md`), for the mirror criterion on the left multiplications and the left-ideal coincidence.
- *Introduction to the General Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-general-plain-sesqualgebra-of-biquaternions.md`), for the product, its class, its table and its placement among the twelve.
- *One-Sided Operators on the General Plain Sesqualgebra of Biquaternions* (`articles_maths/one-sided-operators-on-the-general-plain-sesqualgebra-of-biquaternions.md`), for the plain operators $L_{\tilde B}$, $R_{\tilde C}$, their composition laws, their adjoints and their types, which the dictionary reads on the block.
- *Norm and Invertibility in the General Plain Sesqualgebra* (`articles_maths/norm-and-invertibility-in-the-general-plain-sesqualgebra.md`), for the norm, the one-sided inverse and the criterion of invertibility.
- *Square Roots of One and the Idempotents of the General Plain Sesqualgebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-general-plain-sesqualgebra.md`), for the Hermitian idempotents that the projector family meets.
- *The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-general-plain-sesqualgebra-in-the-2x2-matrix-element-representation.md`), for the model in which the dictionary is the conjugate transpose.
