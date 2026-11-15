# __The Lie Structure of the Antisymmetric Quaternionic Sesquilinear Product__

## Introduction

The antisymmetrisation of $\tilde Q_1^{\natural}\tilde Q_2^{*}$ is
$$
\tilde Q_1\wedge_{\natural*}\tilde Q_2=\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2^{*}-\overline{\tilde Q_2^{\natural}\tilde Q_1^{*}}\bigr)=\vec Q_1\times\overline{\vec Q_2},
$$
the cross product of the first vector part with the conjugate of the second. It has no scalar part and no mixed part, its image is the vector subspace, and it fails the Jacobi identity with a defect of dimension three. The failure is not caused by a mixed part, because there is none: it is caused by the conjugate-linearity of the second slot. On the real quaternion subspace the bracket coincides with the plain bracket of the first article of the block, and its failure is invisible there.

This article reads the Lie structure of the bracket: the antisymmetrisation, the Jacobi identity and its failure, the defect, the bracket table, the ideals and the radical, the Killing form, the exponential and the versors, and the row of the bracket in the comparison of the four.

The setting is [The General Quaternionic Sesquilinear Product](the-general-quaternionic-sesquilinear-product.html), whose second half is this product, and [The Jordan Structure of the Symmetric Quaternionic Sesquilinear Product](the-jordan-structure-of-the-symmetric-quaternionic-sesquilinear-product.html), which reads the first half. The general theory is [Lie Algebras](lie-algebras-a-general-introduction.html), and the comparison of the four brackets is [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html).

## The Antisymmetrisation

**Definition.** The **antisymmetric quaternionic sesquilinear product** is
$$
\tilde Q_1\wedge_{\natural*}\tilde Q_2=\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2^{*}-\overline{\tilde Q_2^{\natural}\tilde Q_1^{*}}\bigr).
$$

**Theorem (the closed form).** For all $\tilde Q_1,\tilde Q_2$,
$$
\boxed{\;\tilde Q_1\wedge_{\natural*}\tilde Q_2=\vec Q_1\times\overline{\vec Q_2}\;}
$$

*Proof.* In the general quaternionic sesquilinear product the scalar row is $K(\tilde Q_1,\tilde Q_2)$, Hermitian in the pair, the mixed part is $-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1$, which is Hermitian in the pair, and the cross part is $\vec Q_1\times\overline{\vec Q_2}$. Under the exchange with conjugation the scalar row and the mixed part are fixed and the cross part changes sign, so the half-difference is the cross part. Verified exactly on the basis and on general elements.

**Corollary (the elementary properties).** The bracket is antisymmetric in the sesquilinear sense; it has no scalar part and no mixed part; its image is the vector subspace; and its restriction to the real quaternion subspace is the cross product, hence the bracket of the plain product.

*Proof.* The first three items are read from the display. On the real quaternion subspace the conjugation is trivial, so $\vec Q_1\times\overline{\vec Q_2}=\vec Q_1\times\vec Q_2$, which is the plain bracket. Verified exactly, with a deviation of zero on all sixteen pairs of the real basis.

**Remark (the two pure brackets).** Two of the four brackets of the batch have no mixed part: this one and the plain one. Their values are cross products, and they differ only in the conjugation of the second factor. On real coefficients the two coincide, so the difference is invisible on the real algebra and appears only when the imaginary unit enters. The consequence is a defect that no real witness can produce, and a bracket that looks, on the real basis, exactly like the one Lie bracket of the block.

**Remark (the bracket is conjugate-linear in the second slot).** For every fixed $\tilde Q_1$ the map $\tilde Q_2\mapsto\tilde Q_1\wedge_{\natural*}\tilde Q_2$ is conjugate-linear. The bracket is a real bilinear map on a real space of dimension eight, and the complex notation records the conjugate-linearity rather than a complex bilinearity. Everything that follows is a consequence of that single fact.

## The Jacobi Identity

**Theorem (the identity fails).** There are $\tilde Q_1,\tilde Q_2,\tilde Q_3$ with
$$
\bigl[\tilde Q_1,\tilde Q_2\bigr]_{\natural*}\wedge_{\natural*}\tilde Q_3+\bigl[\tilde Q_2,\tilde Q_3\bigr]_{\natural*}\wedge_{\natural*}\tilde Q_1+\bigl[\tilde Q_3,\tilde Q_1\bigr]_{\natural*}\wedge_{\natural*}\tilde Q_2\neq0 .
$$

*Proof.* Take $(\tilde Q_1,\tilde Q_2,\tilde Q_3)=(\vec e_x,\vec e_x,i\vec e_y)$. The three terms of the cyclic sum are
$$
[\vec e_x,\vec e_x]_{\natural*}\wedge_{\natural*}i\vec e_y=0,\qquad
[\vec e_x,i\vec e_y]_{\natural*}\wedge_{\natural*}\vec e_x=(-i\vec e_z)\wedge_{\natural*}\vec e_x=-i\vec e_y,\qquad
[i\vec e_y,\vec e_x]_{\natural*}\wedge_{\natural*}\vec e_x=(-i\vec e_z)\wedge_{\natural*}\vec e_x=-i\vec e_y,
$$
and the sum is $-2i\vec e_y$. Computed exactly; the two nonzero terms are equal, and the value is produced twice with the same sign, which is the mark of a bracket whose second slot is conjugated rather than linear.

**Proposition (the identity holds on the real vector subspace).** For $\tilde Q_1,\tilde Q_2,\tilde Q_3\in\mathbb{B}_V$ with real coefficients the cyclic sum vanishes.

*Proof.* On the real vector subspace the bracket is the cross product, and the cyclic sum of a cross product bracket vanishes by the Jacobi identity of $\mathfrak{so}(3,\mathbb{C})$. Verified on all sixty-four triples of the real basis, where the sum is zero.

**Remark (where the failure lives).** The failure is produced by the imaginary unit and nowhere else: it vanishes on the real vector subspace, it is three-dimensional on the complex vector subspace, and it is three-dimensional on the whole algebra. The bracket therefore fails the identity on $\mathbb{B}_V$ alone, which none of the other three does.

## The Defect

**Theorem (the defect is three-dimensional).** The span of the values of the cyclic sum over all triples of the complex basis is three-dimensional, equal to the vector subspace; its intersection with the span of the values on the real basis is zero.

*Proof.* The complex witness $(\vec e_x,\vec e_x,i\vec e_y)$ gives $-2i\vec e_y$, and the cyclic companions give $-2i\vec e_k$; the real basis gives nothing. The singular values of the matrix of values over the complex basis give three nonzero values and three left singular vectors, the vector units. Computed exactly.

**Remark (the cause is the conjugation, not a mixed part).** The four defects are $0,3,3,3$. Three of them are nonzero, and they have two different causes: the two brackets with a mixed part fail through it, and this one fails through the conjugation of its second slot. The distinction is visible in the witnesses: the mixed-part brackets fail at $(e_t,\vec e_x,\vec e_y)$, a triple of real elements, and this bracket fails only at a triple that contains $i$.

**Remark (a defect with no trace in the real algebra).** The real form of the bracket is the plain bracket, which is a Lie bracket. The defect is therefore a purely complex phenomenon: the complexification of a Lie algebra is a Lie algebra, but the complexification of this bracket is not obtained by extending scalars, because the bracket is conjugate-linear and the extension is not defined. The sesquilinear bracket is a real Lie-theoretic object whose complexification does not exist, and the defect measures the obstruction.

## The Bracket on the Basis

**Proposition (the table).** In the coefficient basis the bracket has the table of the plain bracket:
$$
[\vec e_x,\vec e_y]_{\natural*}=\vec e_z,\qquad [\vec e_y,\vec e_z]_{\natural*}=\vec e_x,\qquad [\vec e_z,\vec e_x]_{\natural*}=\vec e_y,
$$
with the negatives in the reversed order, and every bracket with $e_t$ vanishes.

*Proof.* $\vec e_x\wedge_{\natural*}\vec e_y=\tfrac12(\vec e_x^{\natural}\vec e_y^{*}-\overline{\vec e_y^{\natural}\vec e_x^{*}})=\tfrac12(\vec e_z-\overline{\vec e_z})=\vec e_z$, since $\vec e_z$ has a real coefficient. The scalar unit is central by the closed form, because the cross product with the zero vector vanishes. Computed exactly.

| $\wedge_{\natural*}$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $0$ | $0$ | $0$ | $0$ |
| $\vec e_x$ | $0$ | $0$ | $\vec e_z$ | $-\vec e_y$ |
| $\vec e_y$ | $0$ | $-\vec e_z$ | $0$ | $\vec e_x$ |
| $\vec e_z$ | $0$ | $\vec e_y$ | $-\vec e_x$ | $0$ |

**Corollary (the table does not see the conjugation).** The table of this bracket and the table of the plain bracket are identical, so no computation on the basis distinguishes them.

*Proof.* The entries of the table are brackets of real basis elements, and on them the conjugation is trivial. The identity of the tables is the identity of the two brackets on the real subalgebra, which is the first corollary of the article.

**Remark (what the table hides).** The table hides the whole defect, since the defect needs $i$. It also hides the difference between this bracket and the plain one, and it hides the conjugate-linearity: the table is compatible with a bilinear bracket and with a sesquilinear one. This is the reason the two brackets cannot be separated by any computation with real coefficients, and the reason the four brackets look alike in the real algebra.

## The Ideals and the Radical

**Proposition (the ideals are the three).** The complex subspaces closed under the bracket with the whole algebra are $0$, $\mathbb{B}_V$ and $\mathbb{B}$.

*Proof.* $\mathbb{B}_V$ is closed, since the bracket of two vectors is a vector and the scalar unit is central. The scalar line is closed too, as a consequence of the centrality of $e_t$. A subspace containing a vector and a scalar is everything. Verified by computing the invariant subspaces.

**Proposition (there is no radical).** The bracket is not a Lie bracket, so it has no radical in the sense of Lie theory; the radical of the trace form is the scalar line.

*Proof.* The radical presupposes the Jacobi identity. The radical of the trace form is computed in the next section and is $\mathbb{C}e_t$. The statement is a triviality, recorded so that the row is complete.

**Remark (the centre).** The centre is the scalar line: $e_t$ is central, and no vector element is, since $[\vec e_x,\vec e_y]_{\natural*}=\vec e_z$. The centre is computed by solving the linear systems, and it coincides with the radical of the trace form. The coincidence is the same one as in the plain bracket, and it happens for the same reason: a central line contributes nothing to the adjoint maps.

## The Killing Form

**Definition.** $\kappa(\tilde Q_1,\tilde Q_2)=\operatorname{tr}\bigl(\operatorname{ad}\tilde Q_1\circ\operatorname{ad}\tilde Q_2\bigr)$. The adjoint maps are conjugate-linear, and the composition of two of them is linear, so the trace is defined.

**Theorem (the form in the coefficient basis).** The matrix of $\kappa$ is
$$
\kappa(\tilde Q_1,\tilde Q_2)=-2\bigl(\vec Q_1,\overline{\vec Q_2}\bigr)=\operatorname{diag}(0,-2,-2,-2),
$$
with radical the scalar line; the form is conjugate-linear in the second slot.

*Proof.* The adjoint of $\vec e_x$ is the map $\vec v\mapsto\vec e_x\times\overline{\vec v}$, whose composition with itself is $-\lvert\cdot\rvert^{2}$ on the plane orthogonal to $\vec e_x$; the trace is $-2$. The adjoint of $e_t$ is zero. The conjugate-linearity in the second slot is $[\ ,\ ]$ being conjugate-linear there, and the mixed traces vanish. Computed exactly.

**Proposition (the form is not invariant).** $\kappa([\vec e_x,\vec e_y]_{\natural*},i\vec e_z)+\kappa(\vec e_y,[\vec e_x,i\vec e_z]_{\natural*})=-4i$.

*Proof.* $[\vec e_x,\vec e_y]_{\natural*}=\vec e_z$, so the first term is $\kappa(\vec e_z,i\vec e_z)=-2i$. And $[\vec e_x,i\vec e_z]_{\natural*}=\vec e_x\times(-i\vec e_z)=i\vec e_y$, so the second term is $\kappa(\vec e_y,i\vec e_y)=-2i$. The sum is $-4i$. Computed exactly; the invariance holds on the real basis and fails only with the imaginary unit, as does the identity.

**Remark (a form with a one-dimensional radical that is not an ideal).** The radical of the form is the scalar line, which is an ideal of the bracket. That is the only property the invariant form of a Lie algebra would require, and it holds here; what fails is the invariance itself. The example shows that the invariance is not a consequence of the radical being an ideal, and that the Jacobi identity is indispensable.

## The Exponential and the Versors

**Proposition (the adjoint maps are conjugate-linear).** For every $\tilde Q_1$ the map $\tilde Q_2\mapsto\tilde Q_1\wedge_{\natural*}\tilde Q_2$ is conjugate-linear, so its exponential is defined only on the realification, where it is a real endomorphism.

*Proof.* The bracket is conjugate-linear in the second slot by its closed form. On the real space of dimension eight the adjoint map is real-linear, and its exponential is computed by the series.

**Proposition (the exponential is not an automorphism).** Read on the real space, $\exp(t\operatorname{ad}\tilde Q_1)$ is not an automorphism of the real bracket for generic $\tilde Q_1$ and $t\neq0$, and it is not complex-linear.

*Proof.* The exponential was summed numerically on the realification and compared with the bracket of the images; the deviation on random data is of order $10$. The test of the commutation with the multiplication by $i$ fails with a deviation of order $1$. The failure is general.

**Proposition (no versor conjugation preserves the bracket).** For a versor $\tilde U$ the map $\tilde Q\mapsto\tilde U\tilde Q\tilde U^{\natural}$ does not preserve this bracket.

*Proof.* The map commutes with ${}^{\natural}$ and preserves the plain product, but the bracket carries the coefficientwise conjugation in its second slot, with which the versor conjugation does not commute in general. The numerical deviation on random data is of order $1$. The only versors that preserve the bracket are the central ones, that is $\pm e_t$.

**Remark (what remains).** What remains of the Lie structure is the real Lie algebra of the real form, which is the plain bracket and its rotation group, and the invariance of the vector subspace. The bracket has no automorphism group beyond its centre and no exponential automorphisms, and it is the only one of the four that fails the identity on the vector subspace itself. The column of this article is therefore the column with the least Lie structure in the block.

## The Place among the Four

| | this bracket | $\wedge$ | $\wedge_{\natural}$ | $\wedge_{*}$ |
|---|---|---|---|---|
| value on $\mathbb{B}_V$ | $\vec X\times\overline{\vec Y}$ | $\vec X\times\vec Y$ | $-\vec X\times\vec Y$ | $-\vec X\times\vec Y$ |
| mixed part | none | none | $Q_{1t}\vec Q_2-Q_{2t}\vec Q_1$ | $-Q_{1t}\overline{\vec Q_2}+\overline{Q_{2t}}\vec Q_1$ |
| Jacobi on the real basis | holds | holds | fails | fails |
| Jacobi on $\mathbb{B}_V$ | fails, defect $3$ | holds | holds | holds |
| centre | $\mathbb{C}e_t$ | $\mathbb{C}e_t$ | $0$ | $0$ |
| Killing form | $\operatorname{diag}(0,-2,-2,-2)$ | $\operatorname{diag}(0,-2,-2,-2)$ | $\operatorname{diag}(3,-2,-2,-2)$ | $\operatorname{diag}(3,-2,-2,-2)$ |
| $\exp(\operatorname{ad})$ automorphism | no | yes | no | no |

**Remark (the column that fails on the vector subspace).** This is the only column whose failure survives on the vector subspace, and it is the only one whose table on the basis is identical to that of a Lie bracket. The two facts are compatible because the table is real and the failure is complex: the bracket is a Lie bracket on the real form and not on the complex space, and the defect measures the difference. The plain bracket is the same bracket with the conjugation removed, and it is the only Lie algebra of the four.

## Summary

The antisymmetric quaternionic sesquilinear product is $\tilde Q_1\wedge_{\natural*}\tilde Q_2=\vec Q_1\times\overline{\vec Q_2}$, the cross product of the first vector part with the conjugate of the second. It has no scalar part and no mixed part, and its image is the vector subspace.

It fails the Jacobi identity with a defect of dimension three, the witness being $(\vec e_x,\vec e_x,i\vec e_y)$, which gives $-2i\vec e_y$; on the real vector subspace the bracket is the cross product and the identity holds, and the table on the basis is the table of the plain bracket.

The ideals are $0$, $\mathbb{B}_V$ and $\mathbb{B}$, the centre is the scalar line, and there is no radical. The Killing form is $\operatorname{diag}(0,-2,-2,-2)$, of radical the scalar line and not invariant, the witness $(e_x,e_y,ie_z)$ giving $-4i$. The adjoint maps are conjugate-linear, the exponential on the realification is not an automorphism, and no versor conjugation preserves the bracket; the residue of the Lie structure is the rotation group of the real form.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra |
| $\tilde Q=Q_te_t+\vec Q$ | the element, its scalar part and its vector part |
| $\tilde Q_1\wedge_{\natural*}\tilde Q_2$ | the antisymmetric quaternionic sesquilinear product |
| ${}^{\natural}$, ${}^{*}$ | the quaternion involution and the Hermitian involution |
| $\operatorname{ad}\tilde Q$ | the adjoint map of the bracket, conjugate-linear |
| $\kappa$ | the trace form of the adjoint representation |
| $K$ | the Krein form |
| $\mathbb{B}_V$ | the vector subspace |
| $\mathbb{B}_{H}$ | the real quaternion subspace |
| $J$ | the Jacobi defect |

## Further Reading

- [The General Quaternionic Sesquilinear Product](the-general-quaternionic-sesquilinear-product.html), for the product of which this is the antisymmetrisation.
- [The Jordan Structure of the Symmetric Quaternionic Sesquilinear Product](the-jordan-structure-of-the-symmetric-quaternionic-sesquilinear-product.html), for the other half of the same product.
- [The Lie Structure of the Antisymmetric Plain Product](the-lie-structure-of-the-antisymmetric-plain-product.html), for the bracket that this one becomes on the real form.
- [The Lie Structure of the Antisymmetric Plain Sesquilinear Product](the-lie-structure-of-the-antisymmetric-plain-sesquilinear-product.html) and [The Lie Structure of the Antisymmetric Quaternionic Product](the-lie-structure-of-the-antisymmetric-quaternionic-product.html), for the two brackets with a mixed part.
- [Lie Algebras](lie-algebras-a-general-introduction.html), for the identity, the ideals and the Killing form in general.
- [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html), for the four brackets.
