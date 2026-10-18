# __One-Sided Operators on the Biquaternion Algebra__

## Introduction

Let $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ be the biquaternion algebra with its natural conjugation ${}^{\natural}$ and the general plain bilinear form

$$
\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}(\tilde Q_1\tilde Q_2),
$$

whose Gram matrix in the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ is $\mathrm{diag}(1,-1,-1,-1)$. The adjoint of a $\mathbb{C}$-linear map of $\mathbb{B}$ for this form is its **associate** $F^{\approx}$, the involution of *The Four Adjoints of the Two Algebras and the Two Sesqualgebras in Examples*.

For $\tilde Q_5,\tilde Q_3\in\mathbb{B}$ define the **left** and the **right multiplication**

$$
L_{\tilde Q_5}(\tilde Q)=\tilde Q_5\,\tilde Q,\qquad R_{\tilde Q_3}(\tilde Q)=\tilde Q\,\tilde Q_3 .
$$

These are the two one-sided operators of the algebra, and the products $L_{\tilde Q_5}R_{\tilde Q_3}$ of the companion article are the two-sided operators of the same form (*Two-Sided Operators on the Biquaternion Algebra*).

The article is the parallel of that one, section for section, and the parallel is faithful rather than accidental: the plain form is the scalar part of the algebra's own product, so the parameter enters **once**, the assignment is linear and multiplicative, and each question of type or of form preservation has a one-line answer. What separates the pair from the Hermitian and the quaternionic pairs of the corpus is a single fact. **Association swaps the two families:**

$$
\bigl(L_{\tilde Q_5}\bigr)^{\approx}=R_{\tilde Q_5},\qquad \bigl(R_{\tilde Q_3}\bigr)^{\approx}=L_{\tilde Q_3}.
$$

The transpose of the left regular representation is the right regular representation, and the transpose of the right one is the left one. The Hermitian dagger keeps the side, $(L_{\tilde Q_5})^{*}=L_{\tilde Q_5^{*}}$, and the quaternionic adjoint keeps the side, $(L_{\tilde Q_5})^{N}=L_{\tilde Q_5^{\natural}}$, so the swap belongs to the plain form alone. It is the reason the operator pair of this form is not a transliteration of the other three.

The algebra, the four conjugations and the remarkable subspaces are *The Biquaternioid as a Vector Space over $\mathbb{C}$*, *The Group of Involutions* and *Introduction to the Remarkable Subspaces*; the form, its Gram matrix and its four pairings are *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space*; association, with the identity $(FG)^{\approx}=G^{\approx}\circ F^{\approx}$ and the basis rule $(e_\mu[\,]e_\nu)^{\approx}=e_\nu[\,]e_\mu$, is *The Four Adjoints of the Two Algebras and the Two Sesqualgebras in Examples*; the general transpose of a bilinear form is *Bilinear Forms*; the general one-sided operator of an algebra on itself is *Algebras of Endomorphisms* and *The Left and Right Regular Representations*.

## The One-Sided Operators

**Definition.** For $\tilde Q_5,\tilde Q_3\in\mathbb{B}$ the **left multiplication by $\tilde Q_5$** and the **right multiplication by $\tilde Q_3$** are the $\mathbb{C}$-linear maps

$$
L_{\tilde Q_5},R_{\tilde Q_3}:\mathbb{B}\longrightarrow\mathbb{B},\qquad
L_{\tilde Q_5}(\tilde Q)=\tilde Q_5\,\tilde Q,\qquad R_{\tilde Q_3}(\tilde Q)=\tilde Q\,\tilde Q_3 .
$$

**Proposition (linearity and injectivity in the parameter).** The assignments $\tilde Q_5\mapsto L_{\tilde Q_5}$ and $\tilde Q_3\mapsto R_{\tilde Q_3}$ are $\mathbb{C}$-linear and injective:

$$
L_{\alpha\tilde Q_5+\beta\tilde Q_5'}=\alpha L_{\tilde Q_5}+\beta L_{\tilde Q_5'},\qquad
R_{\alpha\tilde Q_3+\beta\tilde Q_3'}=\alpha R_{\tilde Q_3}+\beta R_{\tilde Q_3'},
$$

and $L_{\tilde Q_5}=0$ or $R_{\tilde Q_3}=0$ forces $\tilde Q_5=0$ or $\tilde Q_3=0$.

*Proof.* The two displays are the distributivity of the algebra, and injectivity follows by evaluating on $e_t$: $L_{\tilde Q_5}(e_t)=\tilde Q_5$ and $R_{\tilde Q_3}(e_t)=\tilde Q_3$.

**Remark (the parameter enters once).** This is the property that the twisted two-sided operator of the quaternionic group loses. There the operator carries the parameter twice, $\Theta_{\lambda\tilde Q_5}=\lambda^{2}\Theta_{\tilde Q_5}$, and the assignment is quadratic, so no sector criterion can be read off the parameter linearly. Here the assignment is linear in the parameter and $\mathbb{C}$-linear in the argument at the same time, and every criterion below is an identity between parameters rather than a condition on a quadratic form.

**Proposition (the two assignments recover the algebra).** The left multiplications form a subalgebra of $\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ isomorphic to $\mathbb{B}$, the right multiplications form a subalgebra anti-isomorphic to $\mathbb{B}$, and every element of the first family commutes with every element of the second.

*Proof.* The first two statements are the two composition laws below, read as the multiplicativity of $\tilde Q_5\mapsto L_{\tilde Q_5}$ and the anti-multiplicativity of $\tilde Q_3\mapsto R_{\tilde Q_3}$; injectivity makes them isomorphisms onto their images. The commutation is the associativity identity $\tilde Q_5(\tilde Q\tilde Q_3)=(\tilde Q_5\tilde Q)\tilde Q_3$.

## The Composition Laws

**Theorem (the four composition laws).** For all $\tilde Q_5,\tilde Q_3,\tilde Q_4,\tilde Q_6\in\mathbb{B}$,

$$
L_{\tilde Q_5}L_{\tilde Q_3}=L_{\tilde Q_5\tilde Q_3},\qquad
R_{\tilde Q_5}R_{\tilde Q_3}=R_{\tilde Q_3\tilde Q_5},\qquad
L_{\tilde Q_5}R_{\tilde Q_3}=R_{\tilde Q_3}L_{\tilde Q_5},\qquad
\bigl(L_{\tilde Q_5}R_{\tilde Q_3}\bigr)\circ\bigl(L_{\tilde Q_4}R_{\tilde Q_6}\bigr)=L_{\tilde Q_5\tilde Q_4}R_{\tilde Q_6\tilde Q_3},
$$

and the diagonal product $L_{\tilde Q_5}R_{\tilde Q_5^{-1}}$ for a unit $\tilde Q_5$ is the **inner automorphism** $\mathrm{Ad}_{\tilde Q_5}(\tilde Q)=\tilde Q_5\tilde Q\tilde Q_5^{-1}$.

*Proof.* The first identity is $\tilde Q_5(\tilde Q_3\tilde Q)=(\tilde Q_5\tilde Q_3)\tilde Q$, the second is $(\tilde Q\tilde Q_5)\tilde Q_3=\tilde Q(\tilde Q_5\tilde Q_3)$ with the parameters read in the reverse order, the third is the associativity of the product, and the fourth composes the third with the first two. The last statement is the definition of the inner automorphism.

**Corollary (the regular representations).** The left multiplications are the **left regular representation** of $\mathbb{B}$, the right multiplications are the **right regular representation** of the opposite algebra, and the two families commute inside $\mathrm{End}_{\mathbb{C}}(\mathbb{B})$. Their products $L_{\tilde Q_5}R_{\tilde Q_3}$ span $\mathrm{End}_{\mathbb{C}}(\mathbb{B})$, of complex dimension $16$, because the sixteen operators $e_\mu[\,]e_\nu$, $\mu,\nu\in\{t,x,y,z\}$, are independent: the enveloping algebra $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}$ is the full algebra of endomorphisms (*The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*).

**Corollary (invertibility).** The left multiplication $L_{\tilde Q_5}$ is invertible if and only if $\tilde Q_5$ is a unit, with inverse $L_{\tilde Q_5^{-1}}$; the same holds on the right, with inverse $R_{\tilde Q_3^{-1}}$.

*Proof.* If $\tilde Q_5$ is a unit then $L_{\tilde Q_5}L_{\tilde Q_5^{-1}}=L_{e_t}=\mathrm{id}$ by the composition law. Conversely, if $L_{\tilde Q_5}$ is invertible let $\tilde Q$ be the preimage of $e_t$; then $\tilde Q_5\tilde Q=e_t$, and applying the inverse to $\tilde Q_5$ shows that $\tilde Q$ is also a left inverse, so $\tilde Q_5$ is a unit.

## Association on the One-Sided Operators

**Theorem (association swaps the two families).** For all $\tilde Q_5,\tilde Q_3\in\mathbb{B}$,

$$
\bigl(L_{\tilde Q_5}\bigr)^{\approx}=R_{\tilde Q_5},\qquad
\bigl(R_{\tilde Q_3}\bigr)^{\approx}=L_{\tilde Q_3}.
$$

*Proof.* By the invariance of the scalar part under cyclic permutation of the factors, for all $\tilde Q_1,\tilde Q_2\in\mathbb{B}$,

$$
\bigl\langle L_{\tilde Q_5}\tilde Q_1,\tilde Q_2\bigr\rangle
=\mathrm{Sc}\bigl(\tilde Q_5\tilde Q_1\tilde Q_2\bigr)
=\mathrm{Sc}\bigl(\tilde Q_1\tilde Q_2\tilde Q_5\bigr)
=\bigl\langle\tilde Q_1,R_{\tilde Q_5}\tilde Q_2\bigr\rangle,
$$

and the right case is the same computation with the two parameters in the other order. The form is non-degenerate, so the associate is unique.

**Corollary (the transpose of the regular representations).** Association exchanges the left regular representation and the right one: the transpose of $L_{\tilde Q_5}$ is $R_{\tilde Q_5}$ and the transpose of $R_{\tilde Q_3}$ is $L_{\tilde Q_3}$. In particular the image of the left regular representation under association is the right regular representation, and the left regular representation is not stable under the transpose unless the algebra is commutative.

**Remark (the cross identity holds here and fails for the dagger).** For the plain form the adjoint of a left multiplication may be written with the parameter on the right,

$$
\bigl\langle L_{\tilde Q_5}\tilde Q_1,\tilde Q_2\bigr\rangle=\bigl\langle\tilde Q_1,R_{\tilde Q_5}\tilde Q_2\bigr\rangle,
$$

and this cross identity is **true**, because the form is the scalar part of the product and the scalar part is cyclic. It is false for the Hermitian form of the other pair: there $(L_{\tilde Q_5}\tilde Q_1,\tilde Q_2)=(\tilde Q_1,L_{\tilde Q_5^{*}}\tilde Q_2)$ and the analogous statement with $R_{\tilde Q_5^{*}}$ fails. The reason is the same in both cases: the adjoint of a multiplication carries the parameter of the multiplication, and the plain form reads the parameter on the other side while the Hermitian one does not.

**Corollary (association on the mixed operators).** With the identity $(FG)^{\approx}=G^{\approx}\circ F^{\approx}$ for the transpose of a composite,

$$
\bigl(L_{\tilde Q_5}R_{\tilde Q_3}\bigr)^{\approx}=L_{\tilde Q_3}R_{\tilde Q_5},
$$

the two parameters exchanging their places. The two-sided family of the companion article therefore carries the **swap** as its adjoint, and it is that swap, not a conjugation of the parameter, that its type criteria read (*Two-Sided Operators on the Biquaternion Algebra*, §*The Adjoint and the Swap*).

## Self-Adjoint and Skew-Adjoint One-Sided Operators

**Theorem (the type criteria).** Let $\tilde Q_5\in\mathbb{B}$ and let $L_{\tilde Q_5}$ be the left multiplication. Then

$$
L_{\tilde Q_5}\ \text{self-adjoint}\iff \tilde Q_5\ \text{central},\qquad
L_{\tilde Q_5}\ \text{skew-adjoint}\iff \tilde Q_5=0,
$$

and the same two criteria hold for the right multiplication with $\tilde Q_3$ in place of $\tilde Q_5$.

*Proof.* By the swap theorem, $L_{\tilde Q_5}$ is self-adjoint exactly when $R_{\tilde Q_5}=L_{\tilde Q_5}$, that is $\tilde Q_5\tilde Q=\tilde Q\tilde Q_5$ for all $\tilde Q$, which is centrality of $\tilde Q_5$; and it is skew-adjoint exactly when $R_{\tilde Q_5}=-L_{\tilde Q_5}$, that is $\tilde Q_5\tilde Q=-\tilde Q\tilde Q_5$ for all $\tilde Q$. Evaluating the last identity at $\tilde Q=e_t$ gives $\tilde Q_5=-\tilde Q_5$, hence $\tilde Q_5=0$, and $\tilde Q_5=0$ indeed gives the zero operator.

**Corollary (the two sectors).** The self-adjoint left multiplications are the multiplications by the centre $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$; the skew-adjoint sector contains the zero operator alone. The two statements are the sharpest contrast with the Hermitian pair, where the Hermitian and the anti-Hermitian parameters give the self-adjoint and the skew-adjoint operators respectively and both sectors are four-dimensional, and with the quaternionic pair, where the pure parameters give nonzero skew-adjoint one-sided operators.

**Remark (why the skew sector collapses).** Association reverses the order of the factors, and the scalar part is cyclic, so the transpose of a left multiplication is a right multiplication with the same parameter. A skew-adjoint left multiplication would therefore have to satisfy $\tilde Q_5\tilde Q=-\tilde Q\tilde Q_5$ for every $\tilde Q$, and the unit of the algebra permits only $\tilde Q_5=0$. The collapse is a property of the plain form and of the unit together; it disappears as soon as the adjoint carries a conjugation of the parameter, as in the quaternionic case.

## Which Multiplications Preserve the Form

**Theorem (the one-sided automorphisms of the form).** The left multiplication $L_{\tilde Q_5}$ preserves the general plain bilinear form,

$$
\bigl\langle L_{\tilde Q_5}\tilde Q_1,L_{\tilde Q_5}\tilde Q_2\bigr\rangle=\langle\tilde Q_1,\tilde Q_2\rangle\qquad\text{for all }\tilde Q_1,\tilde Q_2,
$$

if and only if $\tilde Q_5=\pm e_t$, that is if and only if $L_{\tilde Q_5}=\pm\mathrm{id}$. The same criterion holds for $R_{\tilde Q_3}$.

*Proof.* By the swap theorem and the symmetry of the form,

$$
\bigl\langle L_{\tilde Q_5}\tilde Q_1,L_{\tilde Q_5}\tilde Q_2\bigr\rangle
=\mathrm{Sc}\bigl(\tilde Q_5\tilde Q_1\tilde Q_5\tilde Q_2\bigr)
=\bigl\langle\tilde Q_1,\tilde Q_5\tilde Q_2\tilde Q_5\bigr\rangle,
$$

so preservation is equivalent to $\tilde Q_5\tilde Q\tilde Q_5=\tilde Q$ for all $\tilde Q$. At $\tilde Q=e_t$ this gives $\tilde Q_5^{2}=e_t$, so $\tilde Q_5$ is a unit with $\tilde Q_5^{-1}=\tilde Q_5$; the identity then reads $\tilde Q_5\tilde Q=\tilde Q\tilde Q_5$ for all $\tilde Q$, so $\tilde Q_5$ is central, and a central element of square $e_t$ is $\pm e_t$ (it is $\lambda e_t$ with $\lambda^{2}=1$). Conversely $\pm e_t$ preserves the form because the two signs cancel.

**Theorem (the inner automorphisms preserve the form).** For every unit $\tilde Q_5$ the inner automorphism $\mathrm{Ad}_{\tilde Q_5}=L_{\tilde Q_5}R_{\tilde Q_5^{-1}}$ preserves the form:

$$
\bigl\langle \tilde Q_5\tilde Q_1\tilde Q_5^{-1},\tilde Q_5\tilde Q_2\tilde Q_5^{-1}\bigr\rangle=\langle\tilde Q_1,\tilde Q_2\rangle .
$$

*Proof.* $\mathrm{Sc}(\tilde Q_5\tilde Q_1\tilde Q_5^{-1}\tilde Q_5\tilde Q_2\tilde Q_5^{-1})=\mathrm{Sc}(\tilde Q_5\tilde Q_1\tilde Q_2\tilde Q_5^{-1})=\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ by the cyclicity of the scalar part.

**Corollary (preservation is a two-sided property).** The one-sided operators that are automorphisms of the form are the two trivial ones, while the inner automorphisms, which are two-sided, are automorphisms of the form for every unit of the algebra. The isometries of the plain form that the algebra supplies are therefore not one-sided, and the companion article reads them inside the two-sided family.

## The Commutant and the Double Centraliser

**Theorem (the double centraliser).** An operator $S\in\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ commutes with every left multiplication if and only if it is a right multiplication, and conversely:

$$
\{\,S:SL_{\tilde Q_5}=L_{\tilde Q_5}S\ \ \forall\tilde Q_5\,\}=\{\,R_{\tilde Q_3}\,\},\qquad
\{\,S:SR_{\tilde Q_3}=R_{\tilde Q_3}S\ \ \forall\tilde Q_3\,\}=\{\,L_{\tilde Q_5}\,\}.
$$

*Proof.* Let $S$ commute with all $L_{\tilde Q_5}$ and put $\tilde Q_3=S(e_t)$. For every $\tilde Q_5$, using $\tilde Q_5=L_{\tilde Q_5}(e_t)$ and the commutation,

$$
S(\tilde Q_5)=S\bigl(L_{\tilde Q_5}(e_t)\bigr)=L_{\tilde Q_5}\bigl(S(e_t)\bigr)=\tilde Q_5\tilde Q_3=R_{\tilde Q_3}(\tilde Q_5),
$$

so $S=R_{\tilde Q_3}$; the converse is the third composition law. The second identity is the same argument with the two families exchanged.

**Corollary (the bicommutant is the scalars).** An operator commuting with both families is a scalar multiple of the identity:

$$
\{\,S:SL_{\tilde Q_5}=L_{\tilde Q_5}S\ \text{and}\ SR_{\tilde Q_3}=R_{\tilde Q_3}S\ \ \forall \tilde Q_5,\tilde Q_3\,\}=\mathbb{C}\,\mathrm{id}.
$$

*Proof.* By the theorem $S=R_{\tilde Q_4}$ for some $\tilde Q_4$, and commutation with every right multiplication reads $R_{\tilde Q_4}R_{\tilde Q_3}=R_{\tilde Q_3}R_{\tilde Q_4}$, that is $\tilde Q_3\tilde Q_4=\tilde Q_4\tilde Q_3$ for all $\tilde Q_3$, i.e. $\tilde Q_4$ central.

## Worked Examples

**The identity and the central scalars.** $L_{e_t}=R_{e_t}=\mathrm{id}$, and for a central scalar $\lambda e_t$ the two one-sided operators agree, $L_{\lambda e_t}=R_{\lambda e_t}=\lambda\,\mathrm{id}$. Both are self-adjoint, neither is skew-adjoint unless $\lambda=0$, and neither preserves the form unless $\lambda=\pm1$: a central scalar acts on the form by the square of the scalar.

**The vector generators.** For $\tilde Q_5=\vec e_k$, $k=x,y,z$, the parameter is neither central nor zero, so $L_{\vec e_k}$ is neither self-adjoint nor skew-adjoint, and it is not an automorphism of the form either, since $\vec e_k^{2}=-e_t\neq e_t$. The transpose of $L_{\vec e_k}$ is $R_{\vec e_k}$, and the two operators differ on every element with a nonzero vector part: $L_{\vec e_k}(\vec e_x)=\vec e_k\vec e_x$ and $R_{\vec e_k}(\vec e_x)=\vec e_x\vec e_k=-\vec e_k\vec e_x$ for $k\neq x$. This is the swap in its least degenerate instance, and it is the example that shows the transpose is not a conjugation of the algebra: association carries $L_{\vec e_k}$ outside the image of $L$.

**A parameter of mixed type.** For $\tilde Q_5=e_t+\vec e_x$ the operator is $L_{\tilde Q_5}=\mathrm{id}+L_{\vec e_x}$, the sum of a self-adjoint and a non-self-adjoint operator, and the theorem says the type is decided by the parameter: $L_{\tilde Q_5}$ is self-adjoint exactly when the vector part of the parameter vanishes. The parameter carries the criterion, not the operator.

**A null parameter.** For the zero divisor $\tilde Q_5=\vec e_x+i\vec e_y$, whose square is $0$, the operator $L_{\tilde Q_5}$ is neither self-adjoint nor skew-adjoint, and $L_{\tilde Q_5}^{2}=L_{\tilde Q_5^{2}}=0$: the powers of a null-parameter multiplication vanish. The example records that the type criteria read the parameter and not the invertibility of the parameter. The companion case $\tilde Q_3=e_t$ of the two-sided article shows the same for a parameter that is not a unit, and the two-sided article records it (*Two-Sided Operators on the Biquaternion Algebra*, §*Worked Examples*).

**A numerical check of the swap.** For random $\tilde Q_5,\tilde Q_3,\tilde Q_1,\tilde Q_2$, the identities $L_{\tilde Q_5}L_{\tilde Q_3}=L_{\tilde Q_5\tilde Q_3}$, $R_{\tilde Q_5}R_{\tilde Q_3}=R_{\tilde Q_3\tilde Q_5}$, $L_{\tilde Q_5}R_{\tilde Q_3}=R_{\tilde Q_3}L_{\tilde Q_5}$, $\langle L_{\tilde Q_5}\tilde Q_1,\tilde Q_2\rangle=\langle\tilde Q_1,R_{\tilde Q_5}\tilde Q_2\rangle$ and $\langle L_{\tilde Q_5}\tilde Q_1,L_{\tilde Q_5}\tilde Q_2\rangle=\langle\tilde Q_1,\tilde Q_5\tilde Q_2\tilde Q_5\rangle$ hold to machine precision, and the last one is the identity on which the automorphism criterion rests.

## Summary

The left and the right multiplications $L_{\tilde Q_5}(\tilde Q)=\tilde Q_5\tilde Q$ and $R_{\tilde Q_3}(\tilde Q)=\tilde Q\tilde Q_3$ are the one-sided operators of the biquaternion algebra, and the products $L_{\tilde Q_5}R_{\tilde Q_3}$ of the companion article are the two-sided ones. The parameter enters once, so the assignment is linear, multiplicative in the first slot and anti-multiplicative in the second, and the two families commute. Association, the adjoint for the general plain bilinear form, **swaps the two families**, $(L_{\tilde Q_5})^{\approx}=R_{\tilde Q_5}$ and $(R_{\tilde Q_3})^{\approx}=L_{\tilde Q_3}$: the transpose of the left regular representation is the right one. The type criteria are read off the parameter: self-adjoint exactly for a central parameter, skew-adjoint for the zero parameter alone. The one-sided operators that preserve the form are the two trivial ones, $\pm\mathrm{id}$, while the inner automorphisms, which are two-sided, preserve it for every unit. The commutant of the left family is the right family, and the bicommutant is the scalars.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | The biquaternion algebra; basis $e_t,\vec e_x,\vec e_y,\vec e_z$ |
| $\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ | The general plain bilinear form; Gram matrix $\mathrm{diag}(1,-1,-1,-1)$ |
| $F^{\approx}$ | The associate, or transpose, of $F$ for this form |
| $L_{\tilde Q_5}(\tilde Q)=\tilde Q_5\tilde Q$ | Left multiplication; linear and injective in $\tilde Q_5$ |
| $R_{\tilde Q_3}(\tilde Q)=\tilde Q\tilde Q_3$ | Right multiplication; the anti-multiplicative family |
| $L_{\tilde Q_5}L_{\tilde Q_3}=L_{\tilde Q_5\tilde Q_3}$, $R_{\tilde Q_5}R_{\tilde Q_3}=R_{\tilde Q_3\tilde Q_5}$ | Composition laws |
| $L_{\tilde Q_5}R_{\tilde Q_3}=R_{\tilde Q_3}L_{\tilde Q_5}$ | The two families commute |
| $(L_{\tilde Q_5})^{\approx}=R_{\tilde Q_5}$, $(R_{\tilde Q_3})^{\approx}=L_{\tilde Q_3}$ | Association swaps the two families |
| $L_{\tilde Q_5}R_{\tilde Q_5^{-1}}=\mathrm{Ad}_{\tilde Q_5}$ | The inner automorphism of a unit |
| Self-adjoint $\iff \tilde Q_5$ central | Type criterion; the skew sector is $\{0\}$ |
| $L_{\tilde Q_5}$ preserves the form $\iff \tilde Q_5=\pm e_t$ | The one-sided automorphisms of the form |
| $\{S:SL_{\tilde Q_5}=L_{\tilde Q_5}S\}=R(\mathbb{B})$ | The double centraliser |

## Further Reading

- *The Four Adjoints of the Two Algebras and the Two Sesqualgebras in Examples* (`articles_maths/the-four-adjoints-of-the-two-algebras-and-the-two-sesqualgebras-in-examples.md`), for the associate $F^{\approx}$, the basis rule $(e_\mu[\,]e_\nu)^{\approx}=e_\nu[\,]e_\mu$, and the identity $(FG)^{\approx}=G^{\approx}F^{\approx}$ used throughout.
- *Two-Sided Operators on the Biquaternion Algebra* (`articles_maths/two-sided-operators-on-the-biquaternion-algebra.md`), the companion article, for the products $L_{\tilde Q_5}R_{\tilde Q_3}$, their swap adjoint, and the type, automorphism and isometry criteria of the family.
- *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/the-4-forms-over-the-biquaternioid-c-space.md`), for the two bilinear and the two sesquilinear pairings of the algebra and the place of $\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ among them, and the polarisation of the form and its quadratic companion.
- *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure* (`articles_maths/the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.md`), for the enveloping algebra $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}$ and the two-sided operators as its elements.
- *Modules over the Biquaternion Algebra* (`articles_maths/modules-over-the-biquaternion-algebra.md`), for the left regular representation as two copies of the standard module $\mathbb{C}^{2}$.
- *Zero Divisors of the Biquaternion Algebra* (`articles_maths/zero-divisors-of-the-biquaternion-algebra.md`), for the null elements and the pairs of complementary zero divisors used in the examples.
