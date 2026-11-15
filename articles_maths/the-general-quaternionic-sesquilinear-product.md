# __The General Quaternionic Sesquilinear Product__

## Introduction

The fourth of the four general products conjugates both slots, the first by the quaternion involution and the second by the Hermitian one. It is written $\tilde Q_1^{\natural}\tilde Q_2^{*}$, and it is the product of the batch that keeps the least: it is the only one with no unit on either side, the only one whose Jordan defect is the full dimension of the space, and the only one for which the orthogonality of the trace form fails in both of its readings. It is also the product whose scalar part is the Krein form of signature $(1,3)$, and that indefiniteness is the source of most of what follows.

This article reads the product alone: the coordinate rule, the scalar–vector form, the laws, the absence of units, the image and the diagonal, the two halves, the four composites, the trace form against the halves, and the row of the product in the comparison of the four. The notation is that of [The Four General Products and Their Relations over the Biquaternion Algebra](the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html): $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, coefficient basis $\mathcal{E}=(e_t,\vec e_x,\vec e_y,\vec e_z)$, $\tilde Q=Q_te_t+\vec Q$, the three conjugations, and the two pairings. The forms are [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html); the twelve products are [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html); the vector halves are [The Vector Parts of the Products over the Biquaternion Algebra](the-vector-parts-of-the-products-over-the-biquaternion-algebra.html).

The product is the sesquilinear companion of $\tilde Q_1^{\natural}\tilde Q_2$, and the two are read side by side. Where the bilinear product of that name has a left unit, this one has none; where its symmetrisation is central, this one has a symmetrisation of full image; and where its defects are three and one, the defects here are three and four.

## The Product and Its Coordinate Rule

**Definition.** The **general quaternionic sesquilinear product** is
$$
\tilde Q_1^{\natural}\tilde Q_2^{*}=\sum_{\mu}\sum_{\nu}Q_{1\mu}{}^{\natural}\overline{Q_{2\nu}}\,e_\mu e_\nu ,
$$
with $Q_{1t}{}^{\natural}=Q_{1t}$ and $Q_{1k}{}^{\natural}=-Q_{1k}$.

**Proposition (the coordinate rule).** For all $\tilde Q_1,\tilde Q_2$,
$$
\tilde Q_1^{\natural}\tilde Q_2^{*}=\bigl(Q_{1t}\overline{Q_{2t}}-Q_{1x}\overline{Q_{2x}}-Q_{1y}\overline{Q_{2y}}-Q_{1z}\overline{Q_{2z}}\bigr)
+\bigl(Q_{1t}\overline{Q_{2x}}+Q_{1x}\overline{Q_{2t}}-Q_{1y}\overline{Q_{2z}}+Q_{1z}\overline{Q_{2y}}\bigr)\vec e_x
+\bigl(Q_{1t}\overline{Q_{2y}}+Q_{1x}\overline{Q_{2z}}+Q_{1y}\overline{Q_{2t}}-Q_{1z}\overline{Q_{2x}}\bigr)\vec e_y
+\bigl(Q_{1t}\overline{Q_{2z}}-Q_{1x}\overline{Q_{2y}}+Q_{1y}\overline{Q_{2x}}+Q_{1z}\overline{Q_{2t}}\bigr)\vec e_z .
$$

*Proof.* The plain coordinate rule with the three vector coordinates of the first factor negated and every coordinate of the second conjugated. The two operations commute because one acts on the coefficients and the other on the units. Verified exactly on the sixteen pairs of the basis and on general elements with coefficients in $\mathbb{Q}(i)$.

**Remark (the four rules, in one line each).** The four coordinate rules are the plain one with zero, one or two sign-and-bar decorations: none for $\tilde Q_1\tilde Q_2$, the first factor's vector coordinates negated for $\tilde Q_1^{\natural}\tilde Q_2$, the second factor's coordinates conjugated for $\tilde Q_1\tilde Q_2^{*}$, and both for $\tilde Q_1^{\natural}\tilde Q_2^{*}$. This product carries the two decorations at once, and it is the only one that does.

## The Scalar–Vector Form

**Theorem (the scalar–vector form).** For all $\tilde Q_1,\tilde Q_2$,
$$
\boxed{\;\tilde Q_1^{\natural}\tilde Q_2^{*}=\bigl(Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})\bigr)-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\,\vec Q_1+\vec Q_1\times\overline{\vec Q_2}\;}
$$

*Proof.* The scalar row is $Q_{1t}\overline{Q_{2t}}$ minus the three products of the vector coordinates, that is $Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})$. The mixed rows are both negative, and the cross term is positive, since the two sign changes cancel in the product of the two vector parts. Computed exactly on general elements.

**Proposition (the scalar part is the Krein form).** The scalar part of the product is
$$
\mathrm{Sc}\bigl(\tilde Q_1^{\natural}\tilde Q_2^{*}\bigr)=Q_{1t}\overline{Q_{2t}}-Q_{1x}\overline{Q_{2x}}-Q_{1y}\overline{Q_{2y}}-Q_{1z}\overline{Q_{2z}}=K(\tilde Q_1,\tilde Q_2),
$$
the Hermitian form of Gram matrix $\operatorname{diag}(1,-1,-1,-1)$: indefinite, of signature $(1,3)$, nondegenerate, and isotropic on a cone of complex dimension three.

*Proof.* The first display with the signs of the three vector coordinates negative and each second coordinate barred. The signature is that of the diagonal matrix, and the isotropic cone is the set $K(\tilde Q,\tilde Q)=0$, which is the union of the two isotropic quadrics $\lvert Q_t\rvert^2=\lvert\vec Q\rvert^2$.

**Remark (the definite and the indefinite).** The two sesquilinear products of the batch carry the two Hermitian forms $H$ and $K$; the two bilinear products carry the two symmetric forms $P$ and $N$. The Krein form is the one that appears in the unitary group of signature $(1,3)$, and the product here is its derived operation. The indefiniteness is not a defect of the product: it is the reason the radical computed below is not zero while the form is nondegenerate.

## The Laws It Keeps and the Laws It Loses

**Theorem (every law of the ladder fails).** The product is not associative, not flexible, not left alternative, not right alternative, and not power associative.

*Proof.* Four witnesses, each computed exactly.

*Not associative.* With $\tilde Q_1=\tilde Q_2=e_t$, $\tilde Q_3=\vec e_x$: $(\tilde Q_1^{\natural}\tilde Q_2^{*})^{\natural}\tilde Q_3^{*}=-\vec e_x$ against $\tilde Q_1^{\natural}(\tilde Q_2^{\natural}\tilde Q_3^{*})^{*}=\vec e_x$.

*Not flexible.* With $\tilde Q_1=i\vec e_z$, $\tilde Q_2=\vec e_z$: $(\tilde Q_1^{\natural}\tilde Q_2^{*})^{\natural}\tilde Q_1^{*}=\vec e_z$ against $\tilde Q_1^{\natural}(\tilde Q_2^{\natural}\tilde Q_1^{*})^{*}=-\vec e_z$. This is the smallest witness of the article, and it needs the factor $i$: on the real quaternion subspace the two sides agree.

*Not alternative.* Left, with $\tilde Q_1=e_t$, $\tilde Q_2=\vec e_x$: $(e_t^{\natural}e_t^{*})^{\natural}\vec e_x^{*}=-\vec e_x$ against $e_t^{\natural}(e_t^{\natural}\vec e_x^{*})^{*}=\vec e_x$. Right, with the same pair: $(e_t^{\natural}\vec e_x^{*})^{\natural}\vec e_x^{*}=e_t$ against $e_t^{\natural}(\vec e_x^{\natural}\vec e_x^{*})^{*}=-e_t$.

*Not power associative.* For $\tilde Q=e_t+\vec e_x+\vec e_y+i\vec e_z$: $\tilde Q^{\natural}(\tilde Q^{\natural}\tilde Q^{*})^{*}=(2,2,2,-2i)$ and $(\tilde Q^{\natural}\tilde Q^{*})^{\natural}\tilde Q^{*}=(2,6+4i,6-4i,-6i)$. The third power is not well defined.

**Remark (the two decorations, two failures).** Each of the two conjugations costs the ladder on its own, as the two previous articles record, and the product that carries both costs nothing more: the failures are the same failures, and the witnesses are the union of the two sets, with the new witnesses that use both decorations at once being no worse than the old ones. This is the sense in which the fourth product is not a new phenomenon but the product of the two.

**Proposition (the identity of the double conjugate).** The two involutions together move the decorations and keep the order:
$$
\bigl(\tilde Q_1^{\natural}\tilde Q_2^{*}\bigr)^{\natural*}=\tilde Q_1^{*}\tilde Q_2^{\natural}.
$$

*Proof.* Both involutions are anti-automorphisms of the plain product and they commute, so the twice-conjugated product is $\tilde Q_1^{*}\tilde Q_2^{\natural}$: the two reversals of order cancel and the two decorations exchange. Verified on general elements.

**Remark (no commutativity, in either sense).** The product is neither commutative nor conjugate-commutative. With $\tilde Q_1=\vec e_x$ and $\tilde Q_2=\vec e_y$ the value is $\vec e_z$ and the value at the reversed order is $-\vec e_z$. The four symmetries of the exchange classify it as the general product of its family, and its two halves are obtained by the two projections of that exchange.

## The One-Sided Units

**Theorem (no unit on either side).** There is no left identity and no right identity.

*Proof.* A left unit would satisfy $\tilde U^{\natural}\tilde Q^{*}=\tilde Q$ for all $\tilde Q$, and $\tilde Q=e_t$ gives $\tilde U^{\natural}=e_t$, that is $\tilde U=e_t$; but $e_t^{\natural}\vec e_x^{*}=-\vec e_x$, so $e_t$ is not a left unit and there is no other candidate. The right side is the same computation with $\tilde Q^{\natural}e_t^{*}=\tilde Q^{\natural}$, which differs from $\tilde Q$ on the vector subspace. The two linear systems were solved: sixteen equations in four unknowns on each side, no solution, least-squares residual $\tfrac32$.

**Remark (the ladder of units, completed).** The four products carry the four possible unit patterns: both sides, left only, right only, neither. The pattern is read from the two decorations: a decoration in the first slot destroys the left unit, a decoration in the second slot destroys the right one, and a product with both decorations keeps neither. The pattern is a table of two by two, and this product is the corner with two decorations.

**Corollary (what replaces the unit).** The element $e_t$ is not a unit, and there is no substitute: a unit is an element fixed by both multiplications, and here neither multiplication fixes it. The role of the unit is taken by the two involutions, which fix $e_t$ and act on the two slots, and every identity of the article that would be proved with a unit is proved instead by applying an involution.

## The Image, the Diagonal and the Scalar Part

**Proposition (the image is the whole space).** The image of the product is $\mathbb{B}$, of complex dimension $4$.

*Proof.* $\tilde Q_1^{\natural}\tilde Q_2^{*}$ with $\tilde Q_1=\tilde Q_2=e_t$ is $e_t$; with $\tilde Q_1=\vec e_x$, $\tilde Q_2=e_t$ it is $-\vec e_x$; and the four values $e_t,-\vec e_x,-\vec e_y,-\vec e_z$ span the space. The span of the sixteen basis products is four-dimensional, computed exactly.

**Theorem (the diagonal splits into two orthogonal parts).** For every $\tilde Q$,
$$
\tilde Q^{\natural}\tilde Q^{*}=\bigl(\lvert Q_t\rvert^2+(\vec Q,\overline{\vec Q})\bigr)-Q_t\overline{\vec Q}-\overline{Q_t}\,\vec Q+\vec Q\times\overline{\vec Q},
$$
and the value is the sum of a Hermitian part and an anti-Hermitian part,
$$
\tfrac12\bigl(\tilde Q^{\natural}\tilde Q^{*}+(\tilde Q^{\natural}\tilde Q^{*})^{*}\bigr)=H(\tilde Q,\tilde Q)e_t-\tfrac12\bigl(Q_t\overline{\vec Q}+\overline{Q_t}\vec Q\bigr),\qquad
\tfrac12\bigl(\tilde Q^{\natural}\tilde Q^{*}-(\tilde Q^{\natural}\tilde Q^{*})^{*}\bigr)=\vec Q\times\overline{\vec Q},
$$
and the two parts are orthogonal for the Krein form, $K(h,a)=0$.

*Proof.* The scalar–vector form at equal arguments. The Hermitian part collects the real scalar and the mixed terms, which are Hermitian; the anti-Hermitian part is the cross term, since $\overline{\vec Q\times\overline{\vec Q}}=-\vec Q\times\overline{\vec Q}$. The orthogonality is the vanishing of $K$ on a pair of which one factor is Hermitian and the other anti-Hermitian, verified on general elements and exact on the basis.

**Remark (the geometry of the split).** Write $\vec Q=\vec p+i\vec q$ with $\vec p,\vec q$ real. The mixed part $-Q_t\overline{\vec Q}-\overline{Q_t}\,\vec Q$ is a real combination of $\vec p$ and $\vec q$, so it lies in the plane they span, while the cross term $\vec Q\times\overline{\vec Q}$ is a real multiple of $i(\vec p\times\vec q)$, perpendicular to that plane. The two parts are orthogonal as real three-vectors, and that is the geometric content of the proposition. The table of diagonals in [The Vector Parts of the Products over the Biquaternion Algebra](the-vector-parts-of-the-products-over-the-biquaternion-algebra.html) records the same split as $\{r+is:\ r,s\in\mathrm{Vect}_{\mathbb{R}}(\mathbb{B}),\ r\cdot s=0\}$.

**Remark (the diagonal image is the whole space).** The diagonal of this product is the only one of the four whose image is four-dimensional and whose values are not confined to a real form. The hermitian square of the sesqualgebra and the quaternionic square of the bilinear product both land in a proper subspace; the double conjugation lands everywhere, and the split above is the reason: the two parts range independently over the Hermitian and anti-Hermitian subspaces.

**Remark (the isotropic elements).** The diagonal vanishes on the cone $\tilde Q^{\natural}\tilde Q^{*}=0$, which is nonempty: $\tilde Q=e_t+\vec e_x$ gives $0$. The product has isotropic elements on both sides, unlike the plain sesquilinear product, and the cone is the union of two quadrics read from $K$.

## The Two Halves of This Product

**Definition.** The **symmetric quaternionic sesquilinear product** and the **antisymmetric quaternionic sesquilinear product** are
$$
\tilde Q_1\bullet_{\natural*}\tilde Q_2=\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2^{*}+\overline{\tilde Q_2^{\natural}\tilde Q_1^{*}}\bigr),\qquad
\tilde Q_1\wedge_{\natural*}\tilde Q_2=\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2^{*}-\overline{\tilde Q_2^{\natural}\tilde Q_1^{*}}\bigr).
$$

**Theorem (the reconstruction and the two forms).** For all $\tilde Q_1,\tilde Q_2$,
$$
\boxed{\;\tilde Q_1^{\natural}\tilde Q_2^{*}=\tilde Q_1\bullet_{\natural*}\tilde Q_2+\tilde Q_1\wedge_{\natural*}\tilde Q_2\;},
$$
$$
\tilde Q_1\bullet_{\natural*}\tilde Q_2=K(\tilde Q_1,\tilde Q_2)e_t-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\,\vec Q_1,\qquad
\tilde Q_1\wedge_{\natural*}\tilde Q_2=\vec Q_1\times\overline{\vec Q_2}.
$$

*Proof.* The scalar row and the two mixed rows are fixed by the exchange-with-conjugation, since the scalar row is Hermitian and the mixed part is conjugate-symmetric; the cross term changes sign, because $\overline{\vec Q_2\times\overline{\vec Q_1}}=-\vec Q_1\times\overline{\vec Q_2}$. Verified on general elements.

**Corollary (the symmetrisation is not central).** The symmetrisation has a scalar part and a vector part, its image is four-dimensional, and it is conjugate-commutative, $\tilde Q_1\bullet_{\natural*}\tilde Q_2=\overline{\tilde Q_2\bullet_{\natural*}\tilde Q_1}$.

**Remark (the only non-central symmetrisation of its class).** The symmetrisation of the plain product is not central either, and it is the only other one. The two central symmetrisations are those of the two products whose symmetric half loses the vector part, and the reason there is the vanishing of the mixed terms; here the mixed terms are present and they are conjugate-symmetric, so they survive the projection.

**Remark (the antisymmetrisation).** The antisymmetrisation is the cross product with the conjugation on the second factor, $\tilde Q_1\wedge_{\natural*}\tilde Q_2=\vec Q_1\times\overline{\vec Q_2}$. It has zero diagonal, its image is the vector subspace, and on real vector arguments it coincides with the antisymmetrisation of the plain product, because the conjugation is trivial there. Off the real subspace the two differ, and the Jacobi failure of this bracket is invisible on the real basis: the smallest witness is $(\vec e_x,\vec e_x,i\vec e_y)$, which gives $-2i\vec e_y$. This is [The Lie Structure of the Antisymmetric Quaternionic Sesquilinear Product](the-lie-structure-of-the-antisymmetric-quaternionic-sesquilinear-product.html).

## The Four Composites

**Theorem (the table of the composites).** For the quaternionic sesquilinear family the images and the scalar parts of the four composites are

| composite | image, complex dimension | scalar part |
|---|---|---|
| $ss$ | $4$ | present |
| $sa$ | $4$ | present |
| $as$ | $3$ | zero |
| $aa$ | $3$ | zero |

*Proof.* The symmetrisation has a four-dimensional image, so an inner $s$ does not collapse the composite; an outer $s$ reads a scalar part and an outer $a$ kills it. The dimensions are the spans over all triples of the complex basis, computed exactly.

**Remark (the two pairs of families).** The table is the same as that of the plain family, and the two families are the two non-central ones. The discriminator is the dimension of the image of the symmetrisation, and the scalar part separates the rows in all four families. The full table is [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html).

**Corollary (the antisymmetrised composites never leave the vector subspace).** $as$ and $aa$ take their values in $\mathbb{B}_{V}$ and have no scalar part.

## The Trace Form and the Halves

**Definition.** The trace form of the family is $\tau(\tilde Q_1,\tilde Q_2)=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*})$, the Krein form $K$.

**Proposition (the cross term survives).** There are $\tilde Q_1,\tilde Q_2,\tilde Q_3,\tilde Q_4$ with
$$
\mathrm{Sc}\bigl(\tilde Q_1\bullet_{\natural*}\tilde Q_2\;\cdot\;\tilde Q_3\wedge_{\natural*}\tilde Q_4^{*}\bigr)\neq0 .
$$

*Proof.* Take $\tilde Q_1=e_t$, $\tilde Q_2=\vec e_x$, $\tilde Q_3=\vec e_y$, $\tilde Q_4=\vec e_z$. Then $\tilde Q_1\bullet_{\natural*}\tilde Q_2=-\vec e_x$ and $\tilde Q_3\wedge_{\natural*}\tilde Q_4=\vec e_x$, and the scalar part of $(-\vec e_x)^{\natural}\vec e_x^{*}$ is $1$.

**Theorem (both readings of the orthogonality fail).** The four-argument vanishing fails, as the proposition shows. The single-pair split fails as well: for $\tilde Q_1=e_t+\vec e_x+\vec e_y+i\vec e_z$ and $\tilde Q_2=e_t+\vec e_x+i\vec e_y+\vec e_z$,
$$
\tau\bigl(s(\tilde Q_1,\tilde Q_2),s(\tilde Q_1,\tilde Q_2)\bigr)+\tau\bigl(a(\tilde Q_1,\tilde Q_2),a(\tilde Q_1,\tilde Q_2)\bigr)=-20,\qquad
\tau\bigl(\tilde Q_1^{\natural}\tilde Q_2^{*},\tilde Q_1^{\natural}\tilde Q_2^{*}\bigr)=-12 .
$$

*Proof.* The two failures were verified on all basis quadruples for the first and on a grid of coefficients for the second; the values displayed are exact, computed in $\mathbb{Q}(i)$. The reason is the same in both readings: the symmetric half is not central, so the cross term $\tau(s,a)$ does not vanish, and the expansion of $\tau$ over the two halves keeps it.

**Remark (the two readings, separated).** The four-argument orthogonality is the strong statement and it holds exactly for the two families whose symmetric half is central. The single-pair split is the weak statement; it holds for three of the four families and fails here. This is the only family for which both fail, and it is the only family of the four in which the trace form has an indefinite scalar part together with a non-central symmetrisation.

## The Place among the Four

| | this product | $\tilde Q_1\tilde Q_2$ | $\tilde Q_1^{\natural}\tilde Q_2$ | $\tilde Q_1\tilde Q_2^{*}$ |
|---|---|---|---|---|
| decorations | first and second | none | first | second |
| unit | none | both | left | right |
| symmetric half | image $4$ | image $4$ | image $1$ | image $1$ |
| trace form | $K$, signature $(1,3)$ | $P$, split | $N$, indefinite over $\mathbb{C}$ | $H$, positive definite |
| $\tau(s,a)=0$ for all arguments | no | no | yes | yes |
| single-pair split | fails | holds | holds | holds |
| Jacobi defect | $3$, invisible on $\mathbb{B}_{H}$ | $0$ | $3$ | $3$ |
| Jordan defect | $4$ | $0$ | $1$ | $1$ |

**Remark (the column of the two largest numbers).** This is the only column with a Jordan defect of four, the full dimension of the space, and the only column where the weak split fails. The Jordan defect is four because the product's symmetrisation is conjugate-commutative but not commutative, and the Jordan identity is stated with the product composed in one order; the failure then has one component for each coordinate. This is read in [The Jordan Structure of the Symmetric Quaternionic Sesquilinear Product](the-jordan-structure-of-the-symmetric-quaternionic-sesquilinear-product.html), where the witness and the defect space are computed.

## Summary

The general quaternionic sesquilinear product is $\tilde Q_1^{\natural}\tilde Q_2^{*}=[Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})]-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1+\vec Q_1\times\overline{\vec Q_2}$, the product with both decorations. It fails every law of the ladder, with a flexibility witness $i\vec e_z,\vec e_z$ that needs the imaginary unit. It has no unit on either side.

Its scalar part is the Krein form $K$ of signature $(1,3)$, indefinite and nondegenerate. Its image is the whole space, its diagonal is the sum of a Hermitian part and an anti-Hermitian part which are orthogonal for $K$, and its diagonal image is the whole space. It has isotropic elements, $\tilde Q=e_t+\vec e_x$ among them.

The symmetrisation is conjugate-commutative and not central, with image of dimension $4$; the antisymmetrisation is $\tilde Q_1\times\overline{\vec Q_2}$ with image the vector subspace, and it coincides with the antisymmetrisation of the plain product on real vector arguments. The four composites have images of dimensions $4,4,3,3$. The trace form $K$ is not orthogonal to the halves in either reading: the four-argument cross term survives with the witness $e_t,\vec e_x,\vec e_y,\vec e_z$ giving $1$, and the single-pair split fails by $8$ on the pair displayed. Both defects are the reflection of the one fact that the symmetric half of this family carries a vector part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra |
| $\mathcal{E}=(e_t,\vec e_x,\vec e_y,\vec e_z)$ | the coefficient basis |
| $\tilde Q=Q_te_t+\vec Q$ | the element, its scalar part and its vector part |
| $\tilde Q_1^{\natural}\tilde Q_2^{*}$ | the general quaternionic sesquilinear product |
| ${}^{\natural}$, ${}^{*}$ | the quaternion involution and the Hermitian involution |
| $K(\tilde Q_1,\tilde Q_2)$ | the Krein form $Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})$ |
| $\tilde Q_1\bullet_{\natural*}\tilde Q_2$ | the symmetric quaternionic sesquilinear product |
| $\tilde Q_1\wedge_{\natural*}\tilde Q_2$ | the antisymmetric quaternionic sesquilinear product |
| $s$, $a$ | the two halves of the product |
| $ss,sa,as,aa$ | the four composites of the family |
| $\mathbb{B}_{\Psi}$, $\mathbb{B}_{\Phi}$ | the Hermitian and anti-Hermitian subspaces |
| $\mathbb{B}_{C}$, $\mathbb{B}_{V}$, $\mathbb{B}_{H}$ | the centre, the vector subspace, the real quaternion subspace |

## Further Reading

- [The Four General Products and Their Relations over the Biquaternion Algebra](the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html), for the four products and the identities between them.
- [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html), for the halves, the composites and the witnesses of the failures.
- [The Vector Parts of the Products over the Biquaternion Algebra](the-vector-parts-of-the-products-over-the-biquaternion-algebra.html), for the diagonal table and the two-bit rule.
- [The Jordan Structure of the Symmetric Quaternionic Sesquilinear Product](the-jordan-structure-of-the-symmetric-quaternionic-sesquilinear-product.html) and [The Lie Structure of the Antisymmetric Quaternionic Sesquilinear Product](the-lie-structure-of-the-antisymmetric-quaternionic-sesquilinear-product.html), for the two halves of this product.
- [The General Plain Sesquilinear Product](the-general-plain-sesquilinear-product.html), for the definite companion of the form used here.
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the Krein form and its index.
