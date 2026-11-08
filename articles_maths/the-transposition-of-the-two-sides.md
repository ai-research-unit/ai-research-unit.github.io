# __The Transposition of the Two Sides__

## Introduction

The operators of the physical corpus are written on the left. A right multiplication appears only inside a pair, where it closes the action on the second side. The practice does not rest on a convention of taste. A right multiplication is a left multiplication read through a reversal of the algebra, and the reversal is written down once:

$$
\boxed{\;R_{\tilde Q}=\tau^{-1}\,L_{\tau(\tilde Q)}\,\tau\;},\qquad \tau(xy)=\tau(y)\tau(x).
$$

The whole of the article is that identity, its hypotheses and its consequences. The hypothesis is the reversal $\tau(xy)=\tau(y)\tau(x)$, and nothing else: order two is not used anywhere, and the reversals of the algebra are in general not involutions. With $\tau$ in hand the two families $L(\mathbb{B})$ and $R(\mathbb{B})$ are one family read in two frames and every two-sided operator is a word in left multiplications and $\tau$.

**What the reversal is not.** It is not the operator transpose $\approx$ of *Adjoint Pair of $L$ and $R$ Operators*, which takes an operator of $\mathbb{B}$ to an operator of $\mathbb{B}$ through a form. It is not the swap of *Operator Chirality on the Biquaternion Algebra*, which exchanges the two sides of an operator and leaves the parameters where they are. A reversal acts on the elements of the algebra, it carries the parameters, and it reverses their product. That last property is the entire mechanism, and it is the one property the coefficient conjugation lacks while appearing to have it.

The two families are *Operators Acting on One Side*, their products *Operators Acting on Two Sides*, the ambient space *The Endomorphisms of the Biquaternion Algebra*. Everything below is written in the coefficient frame $e_t,\vec e_x,\vec e_y,\vec e_z$, with the central $i$ and the products $\vec e_x\vec e_y=\vec e_z$, $\vec e_y\vec e_z=\vec e_x$, $\vec e_z\vec e_x=\vec e_y$, $\vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t$. The article is pure algebra; no step uses a topology, a distance or a limit.

## The Reversals of the Algebra

**Definition.** A **reversal** of $\mathbb{B}$ is an additive bijection $\tau$ with

$$
\tau(xy)=\tau(y)\tau(x)\qquad\text{for all }x,y\in\mathbb{B},
$$

which is either $\mathbb{C}$-linear, $\tau(\lambda x)=\lambda\tau(x)$, or $\mathbb{C}$-**antilinear**, $\tau(\lambda x)=\bar\lambda\,\tau(x)$, for central $\lambda$. The two grades are kept apart, because the operators of the corpus are complex-linear and a reversal of the second grade does not act on them. The inverse of a reversal is a reversal of the same grade.

**Theorem ($\natural$ is a complex-linear reversal).** The natural conjugation, $\natural(e_t)=e_t$ and $\natural(\vec e_k)=-\vec e_k$, satisfies $\natural(xy)=\natural(y)\natural(x)$.

*Proof.* Three cases on the basis, in the frame above. First, a product with $e_t$ is unchanged by the reversal of the order, because $e_t$ is the unit and $\natural$ fixes it. Second, $\vec e_k\vec e_k=-e_t$ is a scalar, and two signs cancel: $\natural(\vec e_k\vec e_k)=-e_t=\natural(\vec e_k)\natural(\vec e_k)$. Third, for distinct $k\ne l$ the product $\vec e_k\vec e_l$ is $\pm$ the third unit $\vec e_m$, so $\natural(\vec e_k\vec e_l)=\mp\vec e_m$; and $\natural(\vec e_l)\natural(\vec e_k)=(-\vec e_l)(-\vec e_k)=-\vec e_k\vec e_l=\mp\vec e_m$, the distinct units anticommuting. The two sides agree in the three cases, and both sides are additive and $\mathbb{C}$-linear on the coordinates.

**Remark (why the sign falls on a product).** A map that negates a basis either preserves a product or reverses it, according to which of the two gets the sign. On the products of two distinct units the exchange of the order carries a sign, and the double negation supplies exactly that sign. On the squares the exchange carries none, because a square is central, and the double negation supplies none either. The two cases agree, and they agree for the same reason.

**Theorem (the coefficient conjugation is not a reversal).** The map $\bar{\cdot}$ sending each of the four coefficients to its conjugate is a $\mathbb{C}$-antilinear automorphism, $\overline{xy}=\bar x\,\bar y$.

*Proof.* The structure constants of the algebra in the coefficient frame are real, the products of the basis being $0$, $\pm e_\mu$ or $-e_t$, so conjugating the coordinates of a product conjugates nothing beyond the coordinates of the two factors.

$\bar{\cdot}$ preserves the product instead of reversing it, and it is antilinear, so it fails both the reversal and the linearity grade. **It is the standing trap of the subject**: it looks like a transposition, it exchanges nothing, and an identity built on it is false for every noncentral parameter.

**Corollary ($\ast$ is an antilinear reversal).** The Hermitian conjugation $\ast=\natural\circ\bar{\cdot}$ satisfies $\ast(xy)=\ast(y)\ast(x)$ and $\ast(\lambda x)=\bar\lambda\,\ast(x)$.

*Proof.* $\ast(xy)=\natural(\bar x\bar y)=\natural(\bar y)\natural(\bar x)=\ast(y)\ast(x)$, the second equality being the theorem on $\natural$ and the reversal of the two conjugated factors.

| $\tau$ | linearity | reverses the product | fixed space |
|---|---|---|---|
| $\natural$ | $\mathbb{C}$-linear | yes | $\mathbb{C}e_t$ |
| $\ast$ | $\mathbb{C}$-antilinear | yes | $\mathbb{B}_{\Psi}$ |
| $\bar{\cdot}$ | $\mathbb{C}$-antilinear | **no**, preserves it | — |

**Remark (all the complex-linear reversals).** For any invertible $U$ the map $\tau_U(x)=U\natural(x)U^{-1}$ is a complex-linear reversal, and each of them arises this way, because every $\mathbb{C}$-linear automorphism of a central simple algebra is inner (*Biquaternion Automorphisms and Derivations*, §*Skolem–Noether*) and the composite of two reversals is an automorphism. The reversal is therefore a choice of $U$, and the choice the corpus makes is $U=e_t$, which is $\natural$ itself. For a complex $U$ the map $\tau_U$ is in general **not** an involution: it is a reversal all the same, and the identity of the next section uses $\tau^{-1}$ and never $\tau$ alone.

## Conjugation by a Reversal

**Theorem (the two families are conjugate).** For a reversal $\tau$ and every $\tilde Q$,

$$
\tau L_{\tilde Q}\tau^{-1}=R_{\tau(\tilde Q)},\qquad
\tau R_{\tilde Q}\tau^{-1}=L_{\tau(\tilde Q)} .
$$

*Proof.* $\tau\bigl(L_{\tilde Q}\tau^{-1}y\bigr)=\tau\bigl(\tilde Q\,\tau^{-1}y\bigr)=\tau(\tau^{-1}y)\,\tau(\tilde Q)=y\,\tau(\tilde Q)=R_{\tau(\tilde Q)}y$ for every $y$, and $\tau$ is bijective. The second line is the same computation with the two factors of the product exchanged, and $\tau^{-1}$ is a reversal of the same linearity grade.

**Corollary (one family in two frames).** The map $\mathcal T(T)=\tau T\tau^{-1}$ on $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ is multiplicative, $\mathcal T(ST)=\mathcal T(S)\mathcal T(T)$; it is $\mathbb{C}$-linear in $T$ when $\tau$ is $\mathbb{C}$-linear and conjugate-linear in $T$ when $\tau$ is antilinear; and it exchanges the two images,

$$
\mathcal T\bigl(L(\mathbb{B})\bigr)=R(\mathbb{B}),\qquad \mathcal T\bigl(R(\mathbb{B})\bigr)=L(\mathbb{B}).
$$

**Corollary (a two-sided operator stays two-sided).** $\mathcal T\bigl(L_{\tilde Q_1}R_{\tilde Q_2}\bigr)=L_{\tau(\tilde Q_2)}R_{\tau(\tilde Q_1)}$. The two sides exchange and the two parameters are carried. The corpus already records the case $\tau=\natural$ in one line, $\natural L_{\tilde Q}\natural=R_{\natural(\tilde Q)}$ (*Operator Chirality on the Biquaternion Algebra*); what the theorem adds is that the property is a property of the reversal and not of that one map.

## The Factoring

**Theorem (a right multiplication is a left one).** $R_{\tilde Q}=\tau^{-1}L_{\tau(\tilde Q)}\tau$, and therefore

$$
\boxed{\;L_{\tilde Q_1}R_{\tilde Q_2}=L_{\tilde Q_1}\,\tau^{-1}\,L_{\tau(\tilde Q_2)}\,\tau\;}.
$$

*Proof.* The theorem of the preceding section reads $\tau R_{\tilde Q}=L_{\tau(\tilde Q)}\tau$; composing with $\tau^{-1}$ on the left gives the first identity, and substituting it into the product gives the second.

**Reading.** Both multiplications act on the left. The right factor becomes a left factor at the price of one application of $\tau$ before it and one of $\tau^{-1}$ after. A computation that appears to need a right multiplication needs two left multiplications and one reversal.

**Corollary (the anti-representation explains itself).** The right family is an anti-representation, $R_{\tilde Q_1}R_{\tilde Q_2}=R_{\tilde Q_2\tilde Q_1}$, while the assignment $\tilde Q\mapsto L_{\tau(\tilde Q)}$ is a representation. The first is the second conjugated by $\tau$:

$$
\tau^{-1}L_{\tau(\tilde Q_1)}\tau\;\tau^{-1}L_{\tau(\tilde Q_2)}\tau
=\tau^{-1}L_{\tau(\tilde Q_2\tilde Q_1)}\tau .
$$

The reversal inside the right family and the reversal inside $\tau$ are the same reversal, read on the parameters and on the products respectively. Nothing is added to the algebra to get an anti-representation; one conjugation removes it.

**Corollary (generation).** The operators of $\mathbb{B}$ are generated by the left multiplications together with $\tau$ and $\tau^{-1}$; the right family adds no generator.

*Proof.* The left and the right families together generate $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, by $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}_{\mathrm{opp}}\cong\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ (*The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*). And every right multiplication is $\tau^{-1}L\tau$ by the theorem above, so it lies in the algebra generated by $L(\mathbb{B})$ and $\tau,\tau^{-1}$.

## The Parameter

**Proposition.** $R_{\tilde Q}=L_{\tilde Q}$ exactly when $\tilde Q$ is central.

*Proof.* The identity $x\tilde Q=\tilde Qx$ for every $x$ is the definition of the centre, which is $\mathbb{C}e_t$.

The two operators agree only on the scalars. Elsewhere they are compared by the reversal, which transports the parameter: the right multiplication by $\tilde Q$ is a left multiplication by $\tau(\tilde Q)$.

**Proposition (the fixed-space shortcut).** If $\tau(\tilde Q)=\tilde Q$, then $\tau(x\tilde Q)=\tilde Q\,\tau(x)$ for every $x$: on the fixed space of the reversal, the right multiplication by $\tilde Q$ is the left multiplication by $\tilde Q$ on the reversed element.

*Proof.* $\tau(x\tilde Q)=\tau(\tilde Q)\tau(x)=\tilde Q\tau(x)$.

The fixed spaces are the last column of the table: the centre for $\natural$, where the shortcut is the triviality $R=L$, and the sector $\mathbb{B}_{\Psi}$ for $\ast$, where it is a genuine transfer, since $R_{\tilde Q}\ne L_{\tilde Q}$ off the centre.

**Remark (the two errors, which are distinct).** The first is to take the coefficient conjugation for a reversal: it preserves the product, so the family it is expected to exchange is not exchanged, and the identity it is expected to give fails for every noncentral parameter. The second is to drop the transport of the parameter: the identity $\tau(x\tilde Q)=\tilde Q\tau(x)$ holds on the fixed space and nowhere else, so an equation written with the same parameter on both sides is a statement about a fixed point of $\tau$ and not a general one.

## Summary

A reversal of the biquaternion algebra is a bijection that sends a product to the product of the factors in the other order, and it is either complex-linear or conjugation-linear. The natural conjugation $\natural$ is a complex-linear reversal, and the reason is one line: the double negation supplies the sign that the exchange of the order supplies on the products of two distinct vector units, and supplies none on the squares, where the exchange supplies none either. The Hermitian conjugation $\ast$ is a conjugation-linear reversal. The coefficient conjugation is neither: it preserves the product and conjugates the scalars, so it exchanges nothing and is the standing trap of the subject. All the complex-linear reversals are the maps $U\natural(\cdot)U^{-1}$, which are in general not involutions; the identity below uses only the reversal, never the order.

Conjugation by a reversal exchanges the two regular families, $\tau L\tau^{-1}=R_{\tau(\cdot)}$ and $\tau R\tau^{-1}=L_{\tau(\cdot)}$, so the two families are one family in two frames, and a two-sided operator stays two-sided under the conjugation with its sides exchanged and its parameters carried. Solving the same identity for the right factor gives the statement of the practice:

$$
R_{\tilde Q}=\tau^{-1}L_{\tau(\tilde Q)}\tau,\qquad
L_{\tilde Q_1}R_{\tilde Q_2}=L_{\tilde Q_1}\,\tau^{-1}\,L_{\tau(\tilde Q_2)}\,\tau .
$$

A two-sided operator is two left multiplications separated by one reversal. The anti-representation of the right family is the representation of the left family conjugated by $\tau$, and the left family together with $\tau$ generates every operator of the algebra.

The parameter is carried by the reversal, so the shortcut that drops it is exact on the fixed space and false off it, the fixed spaces being the centre for $\natural$ and the sector $\mathbb{B}_{\Psi}$ for $\ast$. Nothing else is needed: the article never leaves the algebra of operators.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tau$, $\tau(xy)=\tau(y)\tau(x)$ | a reversal, complex-linear or conjugation-linear; order two is **not** required |
| $\natural$ | the natural conjugation, $\mathrm{id}$ on the centre and $-\mathrm{id}$ on the span of $\vec e_x,\vec e_y,\vec e_z$; a complex-linear reversal |
| $\ast=\natural\bar{\cdot}$ | the Hermitian conjugation; a conjugation-linear reversal |
| $\bar{\cdot}$ | the coefficient conjugation; a conjugation-linear **automorphism**, not a reversal |
| fixed space: $\mathbb{C}e_t$ for $\natural$, $\mathbb{B}_{\Psi}$ for $\ast$ | the parameters the reversal does not carry |
| $\tau L_{\tilde Q}\tau^{-1}=R_{\tau(\tilde Q)}$, $\tau R_{\tilde Q}\tau^{-1}=L_{\tau(\tilde Q)}$ | conjugation by a reversal exchanges the two families |
| $\mathcal T(T)=\tau T\tau^{-1}$ | the conjugation on $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$; linear in $T$ for $\tau$ linear, conjugate-linear for $\tau$ antilinear |
| $R_{\tilde Q}=\tau^{-1}L_{\tau(\tilde Q)}\tau$ | the right multiplication as a left multiplication |
| $L_{\tilde Q_1}R_{\tilde Q_2}=L_{\tilde Q_1}\tau^{-1}L_{\tau(\tilde Q_2)}\tau$ | a two-sided operator as two left multiplications |
| $\tau_U(x)=U\natural(x)U^{-1}$ | the general complex-linear reversal, in general not an involution |

## Further Reading

- [Operators Acting on One Side](operators-acting-on-one-side.html), for the two families $L(\mathbb{B})$ and $R(\mathbb{B})$, their injectivity and their composition laws, which are the two laws the reversal exchanges
- [The Endomorphisms of the Biquaternion Algebra](the-endomorphisms-of-the-biquaternion-algebra.html), for the operator space on which the conjugation $\mathcal T$ acts and for the real-linear effects of the conjugations
- [Operators Acting on Two Sides](operators-acting-on-two-sides.html), for the family that this article rewrites as two left multiplications
- [The Hermitian Pair of Operators Acting on One Side](the-hermitian-pair-of-operators-acting-on-one-side.html), for the use of the factoring $R_{\tilde Q^{\ast}}=\ast^{-1}L_{\tilde Q}\ast$ on a pair of equations, where the transported parameter is the first parameter itself
- [Operator Chirality on the Biquaternion Algebra](operator-chirality-on-the-biquaternion-algebra.html), for the case $\tau=\natural$ of the conjugation theorem and for the swap, which is the operator-level comparison and not the element-level one
- [Adjoint Pair of $L$ and $R$ Operators](adjoint-pair-of-l-and-r-operators.html), for the operator transpose $\approx$ and the four adjoints, which act on operators and take their input from a form
- [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure](the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.html), for $\mathbb{B}^{\mathrm e}=\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}_{\mathrm{opp}}\cong\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, on which the generation statement rests
- [Biquaternion Automorphisms and Derivations](biquaternion-automorphisms-and-derivations.html), for the inner automorphisms and Skolem–Noether, which give the reading of the general reversal $\tau_U$ as a choice of $U$
- [Anti-Automorphisms Twisted by the Base Involution](anti-automorphisms-twisted-by-the-base-involution.html), for the coset of the reversals and the place of $\bar{\cdot}$ among the semilinear maps
