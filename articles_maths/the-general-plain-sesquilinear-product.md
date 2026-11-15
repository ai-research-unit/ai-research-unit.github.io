# __The General Plain Sesquilinear Product__

## Introduction

The third of the four general products leaves the first slot as it stands and conjugates the second by the Hermitian involution. It is written $\tilde Q_1\tilde Q_2^{*}$, it is the derived operation of the sesqualgebra $\mathbb{B}$ with its involution ${}^{*}$, and it is the product the whole sesquilinear half of the corpus is built on. The insertion of ${}^{*}$ in the second slot costs the same three laws as the insertion of ${}^{\natural}$ in the first, keeps a unit on the opposite side, and buys something the other three products do not have: a positive definite scalar part, and a diagonal with no isotropic element.

This article reads the product alone: the coordinate rule, the scalar–vector form, the laws, the units, the image and the diagonal, the two halves, the four composites, the trace form against the halves, and the row of the product in the comparison of the four. The notation is that of [The Four General Products and Their Relations over the Biquaternion Algebra](the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html): $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, coefficient basis $\mathcal{E}=(e_t,\vec e_x,\vec e_y,\vec e_z)$, $\tilde Q=Q_te_t+\vec Q$, the three conjugations, and the two pairings. The sesqualgebra setting is Introduction to the General Plain Sesqualgebra; the forms are [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html); the twelve products are [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html).

The product is $\mathbb{C}$-linear in the first slot and conjugate-linear in the second. Every statement below respects that asymmetry: a right unit and not a left one, an involution on the left rather than on the right, a diagonal that is Hermitian rather than central, and a defect of the symmetrisation of one dimension against a defect of the antisymmetrisation of three.

## The Product and Its Coordinate Rule

**Definition.** The **general plain sesquilinear product** is
$$
\tilde Q_1\tilde Q_2^{*}=\sum_{\mu}\sum_{\nu}Q_{1\mu}\overline{Q_{2\nu}}\,e_\mu e_\nu .
$$

**Proposition (the coordinate rule).** For all $\tilde Q_1,\tilde Q_2$,
$$
\tilde Q_1\tilde Q_2^{*}=\bigl(Q_{1t}\overline{Q_{2t}}+Q_{1x}\overline{Q_{2x}}+Q_{1y}\overline{Q_{2y}}+Q_{1z}\overline{Q_{2z}}\bigr)
+\bigl(Q_{1t}\overline{Q_{2x}}-Q_{1x}\overline{Q_{2t}}+Q_{1y}\overline{Q_{2z}}-Q_{1z}\overline{Q_{2y}}\bigr)\vec e_x
+\bigl(Q_{1t}\overline{Q_{2y}}-Q_{1x}\overline{Q_{2z}}-Q_{1y}\overline{Q_{2t}}+Q_{1z}\overline{Q_{2x}}\bigr)\vec e_y
+\bigl(Q_{1t}\overline{Q_{2z}}+Q_{1x}\overline{Q_{2y}}-Q_{1y}\overline{Q_{2x}}-Q_{1z}\overline{Q_{2t}}\bigr)\vec e_z .
$$

*Proof.* The plain coordinate rule with every coordinate of the second factor conjugated, the conjugation being an automorphism of the structure constants because they are real. Verified exactly on the sixteen pairs of the basis and on general elements with coefficients in $\mathbb{Q}(i)$.

**Remark (the scalar rule).** The product satisfies $\tilde Q_1(\lambda\tilde Q_2)^{*}=\overline{\lambda}\,\tilde Q_1\tilde Q_2^{*}$ and $(\lambda\tilde Q_1)\tilde Q_2^{*}=\lambda\,\tilde Q_1\tilde Q_2^{*}$. The first slot is linear and the second is conjugate-linear, and no conjugation can move from one slot to the other without changing the product. This is the defining asymmetry of every sesquilinear object in the corpus.

## The Scalar–Vector Form

**Theorem (the scalar–vector form).** For all $\tilde Q_1,\tilde Q_2$,
$$
\boxed{\;\tilde Q_1\tilde Q_2^{*}=\bigl(Q_{1t}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2})\bigr)-Q_{1t}\overline{\vec Q_2}+\overline{Q_{2t}}\,\vec Q_1-\vec Q_1\times\overline{\vec Q_2}\;}
$$

*Proof.* The scalar coefficient is the four products with the three vector signs negative and every second coordinate conjugated, that is $Q_{1t}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2})$. The three vector coefficients group into the two mixed terms and the cross term with the conjugation on the second factor. Computed exactly on general elements.

**Proposition (the scalar part is a Hermitian form).** The scalar part of the product is
$$
\mathrm{Sc}\bigl(\tilde Q_1\tilde Q_2^{*}\bigr)=Q_{1t}\overline{Q_{2t}}+Q_{1x}\overline{Q_{2x}}+Q_{1y}\overline{Q_{2y}}+Q_{1z}\overline{Q_{2z}}=H(\tilde Q_1,\tilde Q_2),
$$
a Hermitian form, $\mathbb{C}$-linear in the first slot and conjugate-linear in the second, of Gram matrix the identity, and positive definite:
$$
H(\tilde Q,\tilde Q)=\lvert Q_t\rvert^2+\lvert Q_x\rvert^2+\lvert Q_y\rvert^2+\lvert Q_z\rvert^2>0\qquad(\tilde Q\neq0).
$$

*Proof.* The four signs of the scalar row are positive and each second coordinate carries a bar, which is the definition of $H$. The diagonal value is a sum of four squares of moduli, and it vanishes only when all four coordinates vanish.

**Remark (the definite column).** This is the only one of the four general products whose scalar part is positive definite. The plain product carries the split form, the general quaternionic bilinear product the anisotropic but indefinite norm form of $N$ over $\mathbb{C}$, and the general quaternionic sesquilinear product the indefinite Krein form. The consequence is immediate and it is used in the next sections: the product has no isotropic element, $\tilde Q\tilde Q^{*}=0$ forces $\tilde Q=0$.

## The Laws It Keeps and the Laws It Loses

**Theorem (the four laws of the ladder fail).** The product is not associative, not flexible, not left alternative, not right alternative, and not power associative.

*Proof.* Four witnesses, each computed exactly.

*Not associative.* With $\tilde Q_1=\tilde Q_2=e_t$, $\tilde Q_3=\vec e_x$: $(\tilde Q_1\tilde Q_2^{*})\tilde Q_3^{*}=e_t\vec e_x^{*}=-\vec e_x$ against $\tilde Q_1(\tilde Q_2\tilde Q_3^{*})^{*}=\vec e_x$.

*Not flexible.* With $\tilde Q_1=\vec e_x$, $\tilde Q_2=e_t$: $(\vec e_xe_t^{*})\vec e_x^{*}=\vec e_x\vec e_x^{*}=e_t$ against $\vec e_x(e_t\vec e_x^{*})^{*}=\vec e_x(-\vec e_x)^{*}=-e_t$.

*Not alternative.* Left, with $\tilde Q_1=e_t$, $\tilde Q_2=\vec e_x$: $(e_te_t^{*})\vec e_x^{*}=-\vec e_x$ against $e_t(e_t\vec e_x^{*})^{*}=\vec e_x$. Right, with the same pair: $(e_t\vec e_x^{*})\vec e_x^{*}=-e_t$ against $e_t(\vec e_x\vec e_x^{*})^{*}=e_t$.

*Not power associative.* For $\tilde Q=e_t+\vec e_x$: $\tilde Q(\tilde Q\tilde Q^{*})=2e_t+2\vec e_x$ and $(\tilde Q\tilde Q^{*})\tilde Q^{*}=2e_t-2\vec e_x$.

**Remark (the same reason as the quaternionic case, on the other side).** The product is the plain product composed with an anti-automorphism on the right, and every failure above is the movement of the conjugation into the inner factor at a rebracketing. The two bilinear-conjugation products of the batch, $\tilde Q_1^{\natural}\tilde Q_2$ and $\tilde Q_1\tilde Q_2^{*}$, are mirror images of one another, and their failures are the same failures with the slots exchanged.

**Proposition (the exact identity).** The involution reverses the product,
$$
\bigl(\tilde Q_1\tilde Q_2^{*}\bigr)^{*}=\tilde Q_2\tilde Q_1^{*}.
$$

*Proof.* ${}^{*}$ is an anti-automorphism of the plain product and an involution, so $(\tilde Q_1\tilde Q_2^{*})^{*}=\tilde Q_2\tilde Q_1^{*}$. Verified on general elements.

**Proposition (the product is not commutative).** $\tilde Q_1\tilde Q_2^{*}\neq\tilde Q_2\tilde Q_1^{*}$ in general; with $\tilde Q_1=\vec e_x$ and $\tilde Q_2=\vec e_y$ the two values are $-\vec e_z$ and $+\vec e_z$.

*Proof.* The coordinate rule at the two orders, with the conjugation moving from the second factor to the first.

**Remark (what is not lost).** The product keeps no law of the ladder, and it keeps the two identities that matter for the sesquilinear theory: the reversal above, and the Hermitian symmetry of the scalar part, $H(\tilde Q_1,\tilde Q_2)=\overline{H(\tilde Q_2,\tilde Q_1)}$. Those two are what makes the product the natural one for the unitary group and for the cone of squares.

## The One-Sided Units

**Theorem (a right unit and no left unit).** The element $e_t$ is a right identity, $\tilde Qe_t^{*}=\tilde Q$ for every $\tilde Q$, and there is no left identity.

*Proof.* $e_t^{*}=e_t$ and $\tilde Qe_t=\tilde Q$ in the algebra. For the left side, $e_t\tilde Q^{*}=\tilde Q^{*}$, which equals $\tilde Q$ only for $\tilde Q\in\mathbb{B}_{H}$, the real quaternion subspace; the left multiplication by $e_t$ is the involution ${}^{*}$, whose eigenvalues $1$ and $-1$ are both present. The linear system for a left unit has no solution; the least-squares residual is $\tfrac32$.

**Corollary (the right unit is unique).** If $\tilde U\tilde Q^{*}=\tilde Q$ for all $\tilde Q$ then $\tilde U=e_t$.

*Proof.* Put $\tilde Q=e_t$: $\tilde Ue_t=e_t$, and $\tilde Ue_t=\tilde U$. Computed as a linear system, the solution is $(1,0,0,0)$ with zero residual.

**Remark (the involution on the left).** The left multiplication by $e_t$ is the involution ${}^{*}$, verified on the coefficient basis. It has the two eigenspaces $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$ of real dimension four each, and it is the operator that appears in every Peirce computation of the sesquilinear block. The right multiplication by $e_t$ is the identity, and that is exactly the statement that $e_t$ is a right unit.

## The Image, the Diagonal and the Scalar Part

**Proposition (the image is the whole space).** The image of the product is $\mathbb{B}$, of complex dimension $4$.

*Proof.* $\tilde Q_1\tilde Q_2^{*}$ with $\tilde Q_2=e_t$ is $\tilde Q_1$, so the image is everything; the span of the sixteen basis products is four-dimensional, computed exactly.

**Theorem (the diagonal is Hermitian).** For every $\tilde Q$,
$$
\tilde Q\tilde Q^{*}=H(\tilde Q,\tilde Q)\,e_t-Q_t\overline{\vec Q}+\overline{Q_t}\,\vec Q-\vec Q\times\overline{\vec Q},
$$
and $\tilde Q\tilde Q^{*}$ lies in the Hermitian subspace $\mathbb{B}_{\Psi}$. Its scalar part is the nonnegative real $H(\tilde Q,\tilde Q)$, which vanishes only at $\tilde Q=0$.

*Proof.* The scalar–vector form at equal arguments. For the Hermiticity, $(\tilde Q\tilde Q^{*})^{*}=\tilde Q\tilde Q^{*}$ by the reversal identity, and the fixed set of ${}^{*}$ is $\mathbb{B}_{\Psi}$. The scalar part is the diagonal of $H$, positive definite by the proposition above. Verified on general elements, with the maximal imaginary part of the four coefficients equal to zero.

**Remark (the diagonal against the others).** The diagonal of the plain product fills the whole space; the diagonal of the general quaternionic bilinear product collapses onto the centre; the diagonal here fills a real four-dimensional subspace and carries a scalar part that is a genuine norm. The diagonal is the Hermitian square of the sesqualgebra, and the cone it generates is the algebraic positive cone of [Hermitian Squares and the Algebraic Positive Cone](hermitian-squares-and-the-algebraic-positive-cone.html), restricted to this algebra.

**Proposition (no isotropic element).** $\tilde Q\tilde Q^{*}=0$ if and only if $\tilde Q=0$.

*Proof.* The scalar part of $\tilde Q\tilde Q^{*}$ is $H(\tilde Q,\tilde Q)$, a sum of four moduli, and it must vanish. Conversely $\tilde Q=0$ gives $0$.

**Remark (the two real dimensions).** The image of the diagonal is contained in $\mathbb{B}_{\Psi}$ and it is four-dimensional over $\mathbb{R}$; its complex span is the whole of $\mathbb{B}$, because $i$ times a value of the diagonal is not a value of the diagonal but is in the span. The vector part of the diagonal lies in $i\,\mathrm{Vect}_{\mathbb{R}}(\mathbb{B})$, and the scalar part is real, so the two parts are of different natures, as the table of diagonals in [The Vector Parts of the Products over the Biquaternion Algebra](the-vector-parts-of-the-products-over-the-biquaternion-algebra.html) records.

## The Two Halves of This Product

**Definition.** The **symmetric plain sesquilinear product** and the **antisymmetric plain sesquilinear product** are
$$
\tilde Q_1\bullet_{*}\tilde Q_2=\tfrac12\bigl(\tilde Q_1\tilde Q_2^{*}+\overline{\tilde Q_2\tilde Q_1^{*}}\bigr),\qquad
\tilde Q_1\wedge_{*}\tilde Q_2=\tfrac12\bigl(\tilde Q_1\tilde Q_2^{*}-\overline{\tilde Q_2\tilde Q_1^{*}}\bigr).
$$

**Theorem (the reconstruction and the two forms).** For all $\tilde Q_1,\tilde Q_2$,
$$
\boxed{\;\tilde Q_1\tilde Q_2^{*}=\tilde Q_1\bullet_{*}\tilde Q_2+\tilde Q_1\wedge_{*}\tilde Q_2\;},
$$
$$
\tilde Q_1\bullet_{*}\tilde Q_2=H(\tilde Q_1,\tilde Q_2)\,e_t,\qquad
\tilde Q_1\wedge_{*}\tilde Q_2=-Q_{1t}\overline{\vec Q_2}+\overline{Q_{2t}}\,\vec Q_1-\vec Q_1\times\overline{\vec Q_2}.
$$

*Proof.* The scalar part $H$ is Hermitian, so it is fixed by the exchange-with-conjugation and stays in the symmetrisation; the vector part changes sign under that operation and stays in the antisymmetrisation. Verified on general elements.

**Corollary (the symmetrisation is central and Hermitian).** $\tilde Q_1\bullet_{*}\tilde Q_2$ is a multiple of $e_t$ by the Hermitian form $H$, so the symmetrisation is a commutative product with a one-dimensional image and a positive definite associated form.

**Remark (the degenerate Jordan product, the definite one).** The symmetrisation is the rank-one product of the Hermitian form, and its square is $\tilde Q\bullet_{*}\tilde Q=H(\tilde Q,\tilde Q)e_t$, a nonnegative real multiple of the identity. Its Jordan defect is one-dimensional, with the witness $\tilde Q_1=\tilde Q_2=\vec e_x$ giving $e_t$, so the identity is not automatic even here; the reason is the absence of a left unit. This is [The Jordan Structure of the Symmetric Plain Sesquilinear Product](the-jordan-structure-of-the-symmetric-plain-sesquilinear-product.html).

**Remark (the antisymmetrisation).** The antisymmetrisation carries the three vector pieces, has zero diagonal, and lands in the vector subspace. Its Jacobi defect is three-dimensional, the image of the failure is the whole vector subspace, and the witness $(\tilde Q_1,\tilde Q_2,\tilde Q_3)=(e_t,\vec e_x,\vec e_y)$ gives $\vec e_z$. On real vector arguments the bracket is minus the cross product and the identity holds there, so the failure is produced by the conjugation in the second slot. This is [The Lie Structure of the Antisymmetric Plain Sesquilinear Product](the-lie-structure-of-the-antisymmetric-plain-sesquilinear-product.html).

## The Four Composites

**Theorem (the table of the composites).** For the plain sesquilinear family the images and the scalar parts of the four composites are

| composite | image, complex dimension | scalar part |
|---|---|---|
| $ss$ | $1$ | present |
| $sa$ | $1$ | present |
| $as$ | $3$ | zero |
| $aa$ | $3$ | zero |

*Proof.* The symmetrisation is central, so an inner $s$ collapses the image to the centre and an outer $s$ produces a scalar part; an outer $a$ is alternating and kills it. The dimensions are the spans over all triples of the complex basis, computed exactly.

**Remark (the same table as the quaternionic bilinear family).** The two central-symmetrisation families share the row $1,1,3,3$, and the two non-central families share $4,4,3,3$. The table of the twelve composites therefore separates the four families into two pairs, and the separator is the dimension of the image of the symmetrisation, not the class of the product. The full table is [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html).

**Corollary (the antisymmetrised composites never leave the vector subspace).** $as$ and $aa$ take their values in $\mathbb{B}_{V}$ and have no scalar part.

## The Trace Form and the Halves

**Definition.** The trace form of the family is $\tau(\tilde Q_1,\tilde Q_2)=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$, the Hermitian form $H$.

**Theorem (the exact split).** For all $\tilde Q_1,\tilde Q_2,\tilde Q_3,\tilde Q_4$,
$$
\mathrm{Sc}\bigl(\tilde Q_1\bullet_{*}\tilde Q_2\;\cdot\;\tilde Q_3\wedge_{*}\tilde Q_4^{*}\bigr)=0 ,
$$
and consequently, for the two halves of a single pair,
$$
\tau(\tilde Q_1,\tilde Q_2)=\tau\bigl(s(\tilde Q_1,\tilde Q_2),s(\tilde Q_1,\tilde Q_2)\bigr)+\tau\bigl(a(\tilde Q_1,\tilde Q_2),a(\tilde Q_1,\tilde Q_2)\bigr).
$$

*Proof.* The symmetric value is a multiple of $e_t$, and the scalar part of a multiple of $e_t$ times anything is that multiple times the scalar part of the other factor, which is zero for an antisymmetric value. The consequence is the expansion of $\tau$ with the cross term removed. Verified on the basis and on random quadruples.

**Remark (the definiteness enters here).** The identity above is the reason the form of this family is the one used to build the positive cone: the split of the Hermitian form over the symmetric and antisymmetric halves is exact, and the symmetric half is a scalar, so the norm of an element is the sum of two nonnegative contributions, one from the scalar product of the pair and one from the antisymmetric part. With an indefinite form the same algebra would give a split with a difference of signs and no cone.

**Remark (the two exclusive families).** The four-argument vanishing holds here and for the general quaternionic bilinear product, and it fails for the plain product and for the general quaternionic sesquilinear product. The split identity at a single pair is weaker and holds for the plain product too, so the discriminator is the four-argument statement. The proof of the general claim is in [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html).

## The Place among the Four

| | this product | $\tilde Q_1\tilde Q_2$ | $\tilde Q_1^{\natural}\tilde Q_2$ | $\tilde Q_1^{\natural}\tilde Q_2^{*}$ |
|---|---|---|---|---|
| class | sesquilinear | $\mathbb{C}$-bilinear | $\mathbb{C}$-bilinear | sesquilinear |
| associative | no | yes | no | no |
| unit | right | both | left | none |
| diagonal | Hermitian, positive scalar part | $\mathbb{B}$ | $\mathbb{B}_{C}$ | $\mathbb{B}$ |
| trace form | $H$, positive definite | $P$, split | $N$, indefinite over $\mathbb{C}$ | $K$, indefinite |
| isotropic elements | none | many | many | many |
| $\tau(s,a)=0$ for all arguments | yes | no | yes | no |
| Jacobi defect | $3$ | $0$ | $3$ | $3$ |
| Jordan defect | $1$ | $0$ | $1$ | $4$ |

**Remark (what this column owns).** This is the only column with a positive definite trace form, the only one with no isotropic element, and the only one whose diagonal is confined to the Hermitian subspace by an involution rather than by the collapse of the image. Those three facts are one fact: the product is the derived operation of a sesqualgebra whose involution is definite on the algebra, and the biquaternion algebra with ${}^{*}$ is the only one of the four readings of $\mathbb{H}$ with that property.

## Summary

The general plain sesquilinear product is $\tilde Q_1\tilde Q_2^{*}=[Q_{1t}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2})]-Q_{1t}\overline{\vec Q_2}+\overline{Q_{2t}}\vec Q_1-\vec Q_1\times\overline{\vec Q_2}$, linear in the first slot and conjugate-linear in the second. It fails associativity, flexibility, alternation, power associativity and commutativity, and it satisfies the reversal identity $(\tilde Q_1\tilde Q_2^{*})^{*}=\tilde Q_2\tilde Q_1^{*}$.

The element $e_t$ is a right unit and not a left one, and the right unit is unique; the left multiplication by $e_t$ is the Hermitian involution. The image is the whole space, the diagonal lies in the Hermitian subspace with the positive definite scalar part $H(\tilde Q,\tilde Q)$, and the product has no isotropic element.

The symmetrisation is central, $\tilde Q_1\bullet_{*}\tilde Q_2=H(\tilde Q_1,\tilde Q_2)e_t$; the antisymmetrisation carries the three vector pieces and lands in the vector subspace. The four composites have images of dimensions $1,1,3,3$. The trace form $H$ is positive definite and orthogonal to the halves in the four-argument sense, so the Hermitian norm of a product splits exactly over the symmetric and antisymmetric parts.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra |
| $\mathcal{E}=(e_t,\vec e_x,\vec e_y,\vec e_z)$ | the coefficient basis |
| $\tilde Q=Q_te_t+\vec Q$ | the element, its scalar part and its vector part |
| $\tilde Q_1\tilde Q_2^{*}$ | the general plain sesquilinear product |
| ${}^{*}={}^{\natural}\circ\overline{\phantom{x}}$ | the Hermitian involution |
| $H(\tilde Q_1,\tilde Q_2)$ | the Hermitian form $\sum_\mu Q_{1\mu}\overline{Q_{2\mu}}$ |
| $(\vec Q_1,\overline{\vec Q_2})$, $\vec Q_1\times\overline{\vec Q_2}$ | the sesquilinear dot and cross products |
| $\tilde Q_1\bullet_{*}\tilde Q_2$ | the symmetric plain sesquilinear product |
| $\tilde Q_1\wedge_{*}\tilde Q_2$ | the antisymmetric plain sesquilinear product |
| $s$, $a$ | the two halves of the product |
| $ss,sa,as,aa$ | the four composites of the family |
| $\mathbb{B}_{\Psi}$, $\mathbb{B}_{\Phi}$ | the Hermitian and anti-Hermitian subspaces |
| $\mathbb{B}_{C}$, $\mathbb{B}_{V}$ | the centre and the vector subspace |

## Further Reading

- [The Four General Products and Their Relations over the Biquaternion Algebra](the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html), for the four products and the identities between them.
- [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html), for the halves and the twelve composites.
- [The Vector Parts of the Products over the Biquaternion Algebra](the-vector-parts-of-the-products-over-the-biquaternion-algebra.html), for the vector half and the diagonal table.
- [The Jordan Structure of the Symmetric Plain Sesquilinear Product](the-jordan-structure-of-the-symmetric-plain-sesquilinear-product.html) and [The Lie Structure of the Antisymmetric Plain Sesquilinear Product](the-lie-structure-of-the-antisymmetric-plain-sesquilinear-product.html), for the two halves of this product.
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for $H$ and its three companions.
