# __One-Sided Operators on the General Plain Algebra of Biquaternions__

## Introduction

Let $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ be the biquaternion algebra with its natural conjugation ${}^{\natural}$ and the general plain bilinear form

$$
\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q),
$$

whose Gram matrix in the basis $e_{0},e_{1},e_{2},e_{3}$ is $\mathrm{diag}(1,-1,-1,-1)$. The adjoint of a $\mathbb{C}$-linear map of $\mathbb{B}$ for this form is its **associate** $F^{\approx}$, the involution of *Association and the Transpose on the Biquaternion Algebra*.

For $\tilde A,\tilde B\in\mathbb{B}$ define the **left** and the **right multiplication**

$$
L_{\tilde A}(\tilde Y)=\tilde A\,\tilde Y,\qquad R_{\tilde B}(\tilde Y)=\tilde Y\,\tilde B .
$$

These are the two one-sided operators of the algebra, and the products $L_{\tilde A}R_{\tilde B}$ of the companion article are the two-sided operators of the same form (*Two-Sided Operators on the General Plain Algebra of Biquaternions*).

The article is the parallel of that one, section for section, and the parallel is faithful rather than accidental: the plain form is the scalar part of the algebra's own product, so the parameter enters **once**, the assignment is linear and multiplicative, and each question of type or of form preservation has a one-line answer. What separates the pair from the Hermitian and the quaternionic pairs of the corpus is a single fact. **Association swaps the two families:**

$$
\bigl(L_{\tilde A}\bigr)^{\approx}=R_{\tilde A},\qquad \bigl(R_{\tilde B}\bigr)^{\approx}=L_{\tilde B}.
$$

The transpose of the left regular representation is the right regular representation, and the transpose of the right one is the left one. The Hermitian dagger keeps the side, $(L_{\tilde A})^{*}=L_{\tilde A^{*}}$, and the quaternionic adjoint keeps the side, $(L_{\tilde A})^{N}=L_{\tilde A^{\natural}}$, so the swap belongs to the plain form alone. It is the reason the operator pair of this form is not a transliteration of the other three.

The algebra, the four conjugations and the remarkable subspaces are *Biquaternions as a Vector Space over $\mathbb{C}$*, *The Group of Involutions* and *Introduction to the Remarkable Subspaces*; the form, its Gram matrix and its four pairings are *The Four Pairings of the Biquaternion Algebra*; association, with the identity $(FG)^{\approx}=G^{\approx}\circ F^{\approx}$ and the basis rule $(e_n[\,]e_m)^{\approx}=e_m[\,]e_n$, is *Association and the Transpose on the Biquaternion Algebra*; the general transpose of a bilinear form is *Bilinear Forms*; the general one-sided operator of an algebra on itself is *Algebras of Endomorphisms* and *The Left and Right Regular Representations*.

## The One-Sided Operators

**Definition.** For $\tilde A,\tilde B\in\mathbb{B}$ the **left multiplication by $\tilde A$** and the **right multiplication by $\tilde B$** are the $\mathbb{C}$-linear maps

$$
L_{\tilde A},R_{\tilde B}:\mathbb{B}\longrightarrow\mathbb{B},\qquad
L_{\tilde A}(\tilde Y)=\tilde A\,\tilde Y,\qquad R_{\tilde B}(\tilde Y)=\tilde Y\,\tilde B .
$$

**Proposition (linearity and injectivity in the parameter).** The assignments $\tilde A\mapsto L_{\tilde A}$ and $\tilde B\mapsto R_{\tilde B}$ are $\mathbb{C}$-linear and injective:

$$
L_{\alpha\tilde A+\beta\tilde A'}=\alpha L_{\tilde A}+\beta L_{\tilde A'},\qquad
R_{\alpha\tilde B+\beta\tilde B'}=\alpha R_{\tilde B}+\beta R_{\tilde B'},
$$

and $L_{\tilde A}=0$ or $R_{\tilde B}=0$ forces $\tilde A=0$ or $\tilde B=0$.

*Proof.* The two displays are the distributivity of the algebra, and injectivity follows by evaluating on $e_{0}$: $L_{\tilde A}(e_{0})=\tilde A$ and $R_{\tilde B}(e_{0})=\tilde B$.

**Remark (the parameter enters once).** This is the property that the twisted two-sided operator of the quaternionic group loses. There the operator carries the parameter twice, $\Theta_{\lambda\tilde A}=\lambda^{2}\Theta_{\tilde A}$, and the assignment is quadratic, so no sector criterion can be read off the parameter linearly. Here the assignment is linear in the parameter and $\mathbb{C}$-linear in the argument at the same time, and every criterion below is an identity between parameters rather than a condition on a quadratic form.

**Proposition (the two assignments recover the algebra).** The left multiplications form a subalgebra of $\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ isomorphic to $\mathbb{B}$, the right multiplications form a subalgebra anti-isomorphic to $\mathbb{B}$, and every element of the first family commutes with every element of the second.

*Proof.* The first two statements are the two composition laws below, read as the multiplicativity of $\tilde A\mapsto L_{\tilde A}$ and the anti-multiplicativity of $\tilde B\mapsto R_{\tilde B}$; injectivity makes them isomorphisms onto their images. The commutation is the associativity identity $\tilde A(\tilde Y\tilde B)=(\tilde A\tilde Y)\tilde B$. Verified on random triples.

## The Composition Laws

**Theorem (the four composition laws).** For all $\tilde A,\tilde B,\tilde C,\tilde D\in\mathbb{B}$,

$$
L_{\tilde A}L_{\tilde B}=L_{\tilde A\tilde B},\qquad
R_{\tilde A}R_{\tilde B}=R_{\tilde B\tilde A},\qquad
L_{\tilde A}R_{\tilde B}=R_{\tilde B}L_{\tilde A},\qquad
\bigl(L_{\tilde A}R_{\tilde B}\bigr)\circ\bigl(L_{\tilde C}R_{\tilde D}\bigr)=L_{\tilde A\tilde C}R_{\tilde D\tilde B},
$$

and the diagonal product $L_{\tilde A}R_{\tilde A^{-1}}$ for a unit $\tilde A$ is the **inner automorphism** $\mathrm{Ad}_{\tilde A}(\tilde Y)=\tilde A\tilde Y\tilde A^{-1}$.

*Proof.* The first identity is $\tilde A(\tilde B\tilde Y)=(\tilde A\tilde B)\tilde Y$, the second is $(\tilde Y\tilde A)\tilde B=\tilde Y(\tilde A\tilde B)$ with the parameters read in the reverse order, the third is the associativity of the product, and the fourth composes the third with the first two. The last statement is the definition of the inner automorphism. All were verified on random triples and on random units.

**Corollary (the regular representations).** The left multiplications are the **left regular representation** of $\mathbb{B}$, the right multiplications are the **right regular representation** of the opposite algebra, and the two families commute inside $\mathrm{End}_{\mathbb{C}}(\mathbb{B})$. Their products $L_{\tilde A}R_{\tilde B}$ span $\mathrm{End}_{\mathbb{C}}(\mathbb{B})$, of complex dimension $16$, because the sixteen operators $e_n[\,]e_m$ are independent: the enveloping algebra $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{op}}$ is the full algebra of endomorphisms (*The Enveloping Algebra of the Biquaternion Algebra and the Bi-module Structure*).

**Corollary (invertibility).** The left multiplication $L_{\tilde A}$ is invertible if and only if $\tilde A$ is a unit, with inverse $L_{\tilde A^{-1}}$; the same holds on the right, with inverse $R_{\tilde B^{-1}}$.

*Proof.* If $\tilde A$ is a unit then $L_{\tilde A}L_{\tilde A^{-1}}=L_{e_{0}}=\mathrm{id}$ by the composition law. Conversely, if $L_{\tilde A}$ is invertible let $\tilde Y$ be the preimage of $e_{0}$; then $\tilde A\tilde Y=e_{0}$, and applying the inverse to $\tilde A$ shows that $\tilde Y$ is also a left inverse, so $\tilde A$ is a unit.

## Association on the One-Sided Operators

**Theorem (association swaps the two families).** For all $\tilde A,\tilde B\in\mathbb{B}$,

$$
\bigl(L_{\tilde A}\bigr)^{\approx}=R_{\tilde A},\qquad
\bigl(R_{\tilde B}\bigr)^{\approx}=L_{\tilde B}.
$$

*Proof.* By the invariance of the scalar part under cyclic permutation of the factors, for all $\tilde X,\tilde Y\in\mathbb{B}$,

$$
\bigl\langle L_{\tilde A}\tilde X,\tilde Y\bigr\rangle
=\mathrm{Sc}\bigl(\tilde A\tilde X\tilde Y\bigr)
=\mathrm{Sc}\bigl(\tilde X\tilde Y\tilde A\bigr)
=\bigl\langle\tilde X,R_{\tilde A}\tilde Y\bigr\rangle,
$$

and the right case is the same computation with the two parameters in the other order. The form is non-degenerate, so the associate is unique. Verified on random parameters.

**Corollary (the transpose of the regular representations).** Association exchanges the left regular representation and the right one: the transpose of $L_{\tilde A}$ is $R_{\tilde A}$ and the transpose of $R_{\tilde B}$ is $L_{\tilde B}$. In particular the image of the left regular representation under association is the right regular representation, and the left regular representation is not stable under the transpose unless the algebra is commutative.

**Remark (the cross identity holds here and fails for the dagger).** For the plain form the adjoint of a left multiplication may be written with the parameter on the right,

$$
\bigl\langle L_{\tilde A}\tilde X,\tilde Y\bigr\rangle=\bigl\langle\tilde X,R_{\tilde A}\tilde Y\bigr\rangle,
$$

and this cross identity is **true**, because the form is the scalar part of the product and the scalar part is cyclic. It is false for the Hermitian form of the other pair: there $(L_{\tilde A}\tilde X,\tilde Y)=(\tilde X,L_{\tilde A^{*}}\tilde Y)$ and the analogous statement with $R_{\tilde A^{*}}$ fails. The reason is the same in both cases: the adjoint of a multiplication carries the parameter of the multiplication, and the plain form reads the parameter on the other side while the Hermitian one does not.

**Corollary (association on the mixed operators).** With the identity $(FG)^{\approx}=G^{\approx}\circ F^{\approx}$ for the transpose of a composite,

$$
\bigl(L_{\tilde A}R_{\tilde B}\bigr)^{\approx}=L_{\tilde B}R_{\tilde A},
$$

the two parameters exchanging their places. The two-sided family of the companion article therefore carries the **swap** as its adjoint, and it is that swap, not a conjugation of the parameter, that its type criteria read (*Two-Sided Operators on the General Plain Algebra of Biquaternions*, §*The Adjoint and the Swap*).

## Self-Adjoint and Skew-Adjoint One-Sided Operators

**Theorem (the type criteria).** Let $\tilde A\in\mathbb{B}$ and let $L_{\tilde A}$ be the left multiplication. Then

$$
L_{\tilde A}\ \text{self-adjoint}\iff \tilde A\ \text{central},\qquad
L_{\tilde A}\ \text{skew-adjoint}\iff \tilde A=0,
$$

and the same two criteria hold for the right multiplication with $\tilde B$ in place of $\tilde A$.

*Proof.* By the swap theorem, $L_{\tilde A}$ is self-adjoint exactly when $R_{\tilde A}=L_{\tilde A}$, that is $\tilde A\tilde Y=\tilde Y\tilde A$ for all $\tilde Y$, which is centrality of $\tilde A$; and it is skew-adjoint exactly when $R_{\tilde A}=-L_{\tilde A}$, that is $\tilde A\tilde Y=-\tilde Y\tilde A$ for all $\tilde Y$. Evaluating the last identity at $\tilde Y=e_{0}$ gives $\tilde A=-\tilde A$, hence $\tilde A=0$, and $\tilde A=0$ indeed gives the zero operator. Verified over random central, random pure and random general parameters.

**Corollary (the two sectors).** The self-adjoint left multiplications are the multiplications by the centre $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_{0}$; the skew-adjoint sector contains the zero operator alone. The two statements are the sharpest contrast with the Hermitian pair, where the Hermitian and the anti-Hermitian parameters give the self-adjoint and the skew-adjoint operators respectively and both sectors are four-dimensional, and with the quaternionic pair, where the pure parameters give nonzero skew-adjoint one-sided operators.

**Remark (why the skew sector collapses).** Association reverses the order of the factors, and the scalar part is cyclic, so the transpose of a left multiplication is a right multiplication with the same parameter. A skew-adjoint left multiplication would therefore have to satisfy $\tilde A\tilde Y=-\tilde Y\tilde A$ for every $\tilde Y$, and the unit of the algebra permits only $\tilde A=0$. The collapse is a property of the plain form and of the unit together; it disappears as soon as the adjoint carries a conjugation of the parameter, as in the quaternionic case.

## Which Multiplications Preserve the Form

**Theorem (the one-sided automorphisms of the form).** The left multiplication $L_{\tilde A}$ preserves the general plain bilinear form,

$$
\bigl\langle L_{\tilde A}\tilde X,L_{\tilde A}\tilde Y\bigr\rangle=\langle\tilde X,\tilde Y\rangle\qquad\text{for all }\tilde X,\tilde Y,
$$

if and only if $\tilde A=\pm e_{0}$, that is if and only if $L_{\tilde A}=\pm\mathrm{id}$. The same criterion holds for $R_{\tilde B}$.

*Proof.* By the swap theorem and the symmetry of the form,

$$
\bigl\langle L_{\tilde A}\tilde X,L_{\tilde A}\tilde Y\bigr\rangle
=\mathrm{Sc}\bigl(\tilde A\tilde X\tilde A\tilde Y\bigr)
=\bigl\langle\tilde X,\tilde A\tilde Y\tilde A\bigr\rangle,
$$

so preservation is equivalent to $\tilde A\tilde Y\tilde A=\tilde Y$ for all $\tilde Y$. At $\tilde Y=e_{0}$ this gives $\tilde A^{2}=e_{0}$, so $\tilde A$ is a unit with $\tilde A^{-1}=\tilde A$; the identity then reads $\tilde A\tilde Y=\tilde Y\tilde A$ for all $\tilde Y$, so $\tilde A$ is central, and a central element of square $e_{0}$ is $\pm e_{0}$ (it is $\lambda e_{0}$ with $\lambda^{2}=1$). Conversely $\pm e_{0}$ preserves the form because the two signs cancel. Verified on the generators, on random parameters and on the two parameters $\pm e_{0}$.

**Theorem (the inner automorphisms preserve the form).** For every unit $\tilde A$ the inner automorphism $\mathrm{Ad}_{\tilde A}=L_{\tilde A}R_{\tilde A^{-1}}$ preserves the form:

$$
\bigl\langle \tilde A\tilde X\tilde A^{-1},\tilde A\tilde Y\tilde A^{-1}\bigr\rangle=\langle\tilde X,\tilde Y\rangle .
$$

*Proof.* $\mathrm{Sc}(\tilde A\tilde X\tilde A^{-1}\tilde A\tilde Y\tilde A^{-1})=\mathrm{Sc}(\tilde A\tilde X\tilde Y\tilde A^{-1})=\mathrm{Sc}(\tilde X\tilde Y)$ by the cyclicity of the scalar part. Verified on random units.

**Corollary (preservation is a two-sided property).** The one-sided operators that are automorphisms of the form are the two trivial ones, while the inner automorphisms, which are two-sided, are automorphisms of the form for every unit of the algebra. The isometries of the plain form that the algebra supplies are therefore not one-sided, and the companion article reads them inside the two-sided family.

## The Commutant and the Double Centraliser

**Theorem (the double centraliser).** An operator $S\in\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ commutes with every left multiplication if and only if it is a right multiplication, and conversely:

$$
\{\,S:SL_{\tilde A}=L_{\tilde A}S\ \ \forall\tilde A\,\}=\{\,R_{\tilde B}\,\},\qquad
\{\,S:SR_{\tilde B}=R_{\tilde B}S\ \ \forall\tilde B\,\}=\{\,L_{\tilde A}\,\}.
$$

*Proof.* Let $S$ commute with all $L_{\tilde A}$ and put $\tilde B=S(e_{0})$. For every $\tilde A$, using $\tilde A=L_{\tilde A}(e_{0})$ and the commutation,

$$
S(\tilde A)=S\bigl(L_{\tilde A}(e_{0})\bigr)=L_{\tilde A}\bigl(S(e_{0})\bigr)=\tilde A\tilde B=R_{\tilde B}(\tilde A),
$$

so $S=R_{\tilde B}$; the converse is the third composition law. The second identity is the same argument with the two families exchanged. Verified on the generators.

**Corollary (the bicommutant is the scalars).** An operator commuting with both families is a scalar multiple of the identity:

$$
\{\,S:SL_{\tilde A}=L_{\tilde A}S\ \text{and}\ SR_{\tilde B}=R_{\tilde B}S\ \ \forall \tilde A,\tilde B\,\}=\mathbb{C}\,\mathrm{id}.
$$

*Proof.* By the theorem $S=R_{\tilde C}$ for some $\tilde C$, and commutation with every right multiplication reads $R_{\tilde C}R_{\tilde B}=R_{\tilde B}R_{\tilde C}$, that is $\tilde B\tilde C=\tilde C\tilde B$ for all $\tilde B$, i.e. $\tilde C$ central. Verified on the generators and on random parameters.

## Worked Examples

**The identity and the central scalars.** $L_{e_{0}}=R_{e_{0}}=\mathrm{id}$, and for a central scalar $\lambda e_{0}$ the two one-sided operators agree, $L_{\lambda e_{0}}=R_{\lambda e_{0}}=\lambda\,\mathrm{id}$. Both are self-adjoint, neither is skew-adjoint unless $\lambda=0$, and neither preserves the form unless $\lambda=\pm1$: a central scalar acts on the form by the square of the scalar.

**The vector generators.** For $\tilde A=e_{k}$, $k=1,2,3$, the parameter is neither central nor zero, so $L_{e_{k}}$ is neither self-adjoint nor skew-adjoint, and it is not an automorphism of the form either, since $e_{k}^{2}=-e_{0}\neq e_{0}$. The transpose of $L_{e_{k}}$ is $R_{e_{k}}$, and the two operators differ on every element with a nonzero vector part: $L_{e_{k}}(e_{1})=e_{k}e_{1}$ and $R_{e_{k}}(e_{1})=e_{1}e_{k}=-e_{k}e_{1}$ for $k\neq1$. This is the swap in its least degenerate instance, and it is the example that shows the transpose is not a conjugation of the algebra: association carries $L_{e_{k}}$ outside the image of $L$.

**A parameter of mixed type.** For $\tilde A=e_{0}+e_{1}$ the operator is $L_{\tilde A}=\mathrm{id}+L_{e_{1}}$, the sum of a self-adjoint and a non-self-adjoint operator, and the theorem says the type is decided by the parameter: $L_{\tilde A}$ is self-adjoint exactly when the vector part of the parameter vanishes. The parameter carries the criterion, not the operator.

**A null parameter.** For the zero divisor $\tilde A=e_{1}+ie_{2}$, whose square is $0$, the operator $L_{\tilde A}$ is neither self-adjoint nor skew-adjoint, and $L_{\tilde A}^{2}=L_{\tilde A^{2}}=0$: the powers of a null-parameter multiplication vanish. The example records that the type criteria read the parameter and not the invertibility of the parameter. The companion case $\tilde B=e_{0}$ of the two-sided article shows the same for a parameter that is not a unit, and the two-sided article records it (*Two-Sided Operators on the General Plain Algebra of Biquaternions*, §*Worked Examples*).

**A numerical check of the swap.** For random $\tilde A,\tilde B,\tilde X,\tilde Y$, the identities $L_{\tilde A}L_{\tilde B}=L_{\tilde A\tilde B}$, $R_{\tilde A}R_{\tilde B}=R_{\tilde B\tilde A}$, $L_{\tilde A}R_{\tilde B}=R_{\tilde B}L_{\tilde A}$, $\langle L_{\tilde A}\tilde X,\tilde Y\rangle=\langle\tilde X,R_{\tilde A}\tilde Y\rangle$ and $\langle L_{\tilde A}\tilde X,L_{\tilde A}\tilde Y\rangle=\langle\tilde X,\tilde A\tilde Y\tilde A\rangle$ hold to machine precision, and the last one is the identity on which the automorphism criterion rests.

## Summary

The left and the right multiplications $L_{\tilde A}(\tilde Y)=\tilde A\tilde Y$ and $R_{\tilde B}(\tilde Y)=\tilde Y\tilde B$ are the one-sided operators of the biquaternion algebra, and the products $L_{\tilde A}R_{\tilde B}$ of the companion article are the two-sided ones. The parameter enters once, so the assignment is linear, multiplicative in the first slot and anti-multiplicative in the second, and the two families commute. Association, the adjoint for the general plain bilinear form, **swaps the two families**, $(L_{\tilde A})^{\approx}=R_{\tilde A}$ and $(R_{\tilde B})^{\approx}=L_{\tilde B}$: the transpose of the left regular representation is the right one. The type criteria are read off the parameter: self-adjoint exactly for a central parameter, skew-adjoint for the zero parameter alone. The one-sided operators that preserve the form are the two trivial ones, $\pm\mathrm{id}$, while the inner automorphisms, which are two-sided, preserve it for every unit. The commutant of the left family is the right family, and the bicommutant is the scalars.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | The biquaternion algebra; basis $e_{0},e_{1},e_{2},e_{3}$ |
| $\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q)$ | The general plain bilinear form; Gram matrix $\mathrm{diag}(1,-1,-1,-1)$ |
| $F^{\approx}$ | The associate, or transpose, of $F$ for this form |
| $L_{\tilde A}(\tilde Y)=\tilde A\tilde Y$ | Left multiplication; linear and injective in $\tilde A$ |
| $R_{\tilde B}(\tilde Y)=\tilde Y\tilde B$ | Right multiplication; the anti-multiplicative family |
| $L_{\tilde A}L_{\tilde B}=L_{\tilde A\tilde B}$, $R_{\tilde A}R_{\tilde B}=R_{\tilde B\tilde A}$ | Composition laws |
| $L_{\tilde A}R_{\tilde B}=R_{\tilde B}L_{\tilde A}$ | The two families commute |
| $(L_{\tilde A})^{\approx}=R_{\tilde A}$, $(R_{\tilde B})^{\approx}=L_{\tilde B}$ | Association swaps the two families |
| $L_{\tilde A}R_{\tilde A^{-1}}=\mathrm{Ad}_{\tilde A}$ | The inner automorphism of a unit |
| Self-adjoint $\iff \tilde A$ central | Type criterion; the skew sector is $\{0\}$ |
| $L_{\tilde A}$ preserves the form $\iff \tilde A=\pm e_{0}$ | The one-sided automorphisms of the form |
| $\{S:SL_{\tilde A}=L_{\tilde A}S\}=R(\mathbb{B})$ | The double centraliser |

## Further Reading

- *Association and the Transpose on the Biquaternion Algebra* (`articles_maths/association-and-the-transpose-on-the-biquaternion-algebra.md`), for the associate $F^{\approx}$, the basis rule $(e_n[\,]e_m)^{\approx}=e_m[\,]e_n$, and the identity $(FG)^{\approx}=G^{\approx}F^{\approx}$ used throughout.
- *Two-Sided Operators on the General Plain Algebra of Biquaternions* (`articles_maths/two-sided-operators-on-the-general-plain-algebra-of-biquaternions.md`), the companion article, for the products $L_{\tilde A}R_{\tilde B}$, their swap adjoint, and the type, automorphism and isometry criteria of the family.
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the two bilinear and the two sesquilinear pairings of the algebra and the place of $\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q)$ among them, and the polarisation of the form and its quadratic companion.
- *The Enveloping Algebra of the Biquaternion Algebra and the Bi-module Structure* (`articles_maths/the-enveloping-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.md`), for the enveloping algebra $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{op}}$ and the two-sided operators as its elements.
- *Modules over the General Plain Algebra of Biquaternions* (`articles_maths/modules-over-the-general-plain-algebra-of-biquaternions.md`), for the left regular representation as two copies of the standard module $\mathbb{C}^{2}$.
- *Zero Divisors of the General Plain Algebra* (`articles_maths/zero-divisors-of-the-general-plain-algebra.md`), for the null elements and the pairs of complementary zero divisors used in the examples.
