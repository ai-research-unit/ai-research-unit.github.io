# __The Hermitian Form as a Product on the Symmetric Plain Sesqualgebra__

## Introduction

The symmetric plain sesqualgebra is the operation $\tilde P\star\tilde Q = \mathrm{Sc}(\tilde P\tilde Q^{*})e_0 = H(\tilde P,\tilde Q)e_0$, with $H(\tilde P,\tilde Q) = P_0\overline{Q_0} + (\mathbf P,\overline{\mathbf Q})$ (*Introduction to the Symmetric Plain Sesqualgebra of Biquaternions*). Its product and its form are the same data: the block is the Hermitian form of the corpus *read as a multiplication*, and every statement about the product is a statement about the form and conversely. This article develops the block from the side of the form: the identification and the rank-one structure it forces, the Gram matrix and the positivity, the Cauchy and Schwarz inequality with its equality case, the trace functional and the trace form, the failure of the invariance of the form under the product, the restriction of the form to the remarkable subspaces, and the bridge to the form of the quaternionic row.

The result that organises the article is that the form is the **definite** form of the algebra, of signature $(8,0)$ on the real space, while the product it defines is **rank one** and central: the image is the centre $\mathbb{C}_{\mathbb{B}}$, the form is recovered as the trace form $\mathrm{Sc}(\tilde P\star\tilde Q) = H(\tilde P,\tilde Q)$, and the invariance that the trace form of the symmetric plain block enjoys — the invariance of a Jordan product — **fails** here. The two facts are one: a product whose values are central and whose form is definite cannot carry an associative or Jordan invariance, because the invariance is exactly the identity that forces the product to have a vector part.

**Boundaries.** The form $H$, its positivity, its cone, its signature and its Gram matrix are *Biquaternion Norm and Invertibility*, *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint* and *The Canonical Hermitian Form on the Regular Module of the Biquaternion Algebra*; they are cited here and not restated, and this article owns only the reading of $H$ as the product of the block. The trace form and the invariance of the symmetric plain block are *The Trace Form and the Invariance of the Symmetric Plain Algebra*; the quaternion form $B$ and its comparison are *The Quaternion Form as a Product on the Symmetric Quaternionic Algebra* and *Comparison Between the Four General Products*. The remarkable subspaces are *Introduction to the Remarkable Subspaces*, and their reading under the general plain sesquilinear product is *Remarkable Subspaces under the General Plain Sesqualgebra of Biquaternions*. Nothing topological and nothing metric appears; the form is used as an algebraic datum and no length, distance or norm of positive real values is written.

**Conventions.** As in the companion articles: $\mathbb{B}$ with basis $e_0,e_1,e_2,e_3$, natural conjugation ${}^{\natural}$, coefficientwise conjugation $\overline{\cdot}$, Hermitian conjugation ${}^{*} = \overline{\cdot}\circ{}^{\natural}$; the block product is $\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0$ and $H$ is the Hermitian form. The remarkable subspaces are the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, the Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$.

## The Identification and the Rank-One Structure

**Theorem (the block is the form read as a product).** For all $\tilde P,\tilde Q$,

$$
\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0 ,
$$

and the assignment $\tilde P\star\tilde Q \mapsto H(\tilde P,\tilde Q)$ is a bijection between the products of the block and the values of the form; the block carries no information beyond the form.

**Proposition (the image is the centre, the product has rank one).** The image of the multiplication is the centre $\mathbb{C}_{\mathbb{B}}$; as a map $\mathbb{B}\otimes_{\mathbb{C}}\overline{\mathbb{B}} \to \mathbb{B}$ the product has rank one over $\mathbb{C}$, its single non-zero value direction being $e_0$. The kernel is the hyperplane of pairs with $H(\tilde P,\tilde Q) = 0$.

*Proof.* Every value is a complex multiple of $e_0$; the value $e_0$ is attained at $(\tilde P,\tilde Q) = (e_0,e_0)$, and no value has a vector part; the condition for vanishing is the single scalar equation $H(\tilde P,\tilde Q) = 0$. $\square$

**Corollary (the product is not a multiplication with a unit).** Because the rank is one and the image is central, the block cannot have a unit and cannot reproduce an element with a vector part on either side; this is the rank-one reason for the absence of a unit proved in the companion article, and it is the reason the block's idempotents are the two central ones alone.

## The Gram Matrix and the Positivity

**Proposition (the Gram matrix is the identity).** In the basis $e_0,e_1,e_2,e_3$,

$$
H(e_\mu,e_\nu) = \delta_{\mu\nu} , \qquad e_\mu\star e_\nu = \delta_{\mu\nu}e_0 ,
$$

so the Gram matrix of the form on the algebra basis is the identity matrix, and the multiplication table of the block is that matrix times $e_0$.

*Proof.* $H(e_\mu,e_\nu) = \sum_\rho (e_\mu)_\rho\overline{(e_\nu)_\rho} = \delta_{\mu\nu}$. Verified on the sixteen pairs, deviation $0$. $\square$

**Proposition (the positivity on the real basis).** On the basis $e_0,e_1,e_2,e_3$ the form has $H(e_\mu,e_\nu) = \delta_{\mu\nu}$; on the real basis $e_\mu, ie_\mu$ of the real space $\mathbb{B}\cong\mathbb{R}^{8}$ the associated real symmetric form $\mathrm{Re}\,H$ is the identity form,

$$
\mathrm{Re}\,H(e_\mu,e_\nu) = \delta_{\mu\nu} , \qquad \mathrm{Re}\,H(ie_\mu,ie_\nu) = \delta_{\mu\nu} , \qquad \mathrm{Re}\,H(e_\mu,ie_\nu) = 0 ,
$$

so the quadratic form $\tilde Q\mapsto H(\tilde Q,\tilde Q)$ is **positive definite** of signature $(8,0)$ on the real space and its null set is $\{0\}$ alone.

*Proof.* $H(ie_\mu,ie_\nu) = (ie_\mu)\overline{(ie_\nu)}$ summed $= (-i)(i)\,\delta_{\mu\nu} = \delta_{\mu\nu}$, a real value; and $H(e_\mu,ie_\nu) = -i\,H(e_\mu,e_\nu) = -i\delta_{\mu\nu}$ by the conjugate-linearity in the second slot, whose real part vanishes. The sixteen pairs were checked, with maximal deviation $0$. $\square$

**Proposition (the diagonal and the absence of an isotropic vector).** For every $\tilde Q$,

$$
H(\tilde Q,\tilde Q) = \lvert Q_0\rvert^{2} + (\mathbf Q,\overline{\mathbf Q}) = \sum_{\mu=0}^{3}\lvert Q_\mu\rvert^{2} ,
$$

real and strictly positive for $\tilde Q \neq 0$. Hence the form has **no isotropic vector**, and its isotropic cone is $\{0\}$.

*Proof.* $H(\tilde Q,\tilde Q) = \sum_\mu Q_\mu\overline{Q_\mu} = \sum_\mu\lvert Q_\mu\rvert^{2}$, a sum of non-negative terms, zero only when every coordinate vanishes. $300$ random elements gave no violation. $\square$

## The Cauchy and Schwarz Inequality

**Theorem (the inequality).** For all $\tilde P,\tilde Q$,

$$
H(\tilde P,\tilde Q)\,\overline{H(\tilde P,\tilde Q)} \le H(\tilde P,\tilde P)\,H(\tilde Q,\tilde Q) ,
$$

that is $\lvert H(\tilde P,\tilde Q)\rvert^{2} \le H(\tilde P,\tilde P)H(\tilde Q,\tilde Q)$, with equality if and only if $\tilde P$ and $\tilde Q$ are linearly dependent over $\mathbb{C}$.

*Proof.* If $\tilde Q = 0$ both sides vanish. Let $\tilde Q \neq 0$ and put $\lambda = H(\tilde P,\tilde Q)/H(\tilde Q,\tilde Q)$ and $\tilde R = \tilde P - \lambda\tilde Q$. Developing $H(\tilde R,\tilde R)$ with the linearity in the first argument and the conjugate-linearity in the second gives $H(\tilde R,\tilde R) = H(\tilde P,\tilde P) - \lambda H(\tilde Q,\tilde P) - \overline{\lambda}H(\tilde P,\tilde Q) + \lvert\lambda\rvert^{2}H(\tilde Q,\tilde Q)$, which reduces to $H(\tilde P,\tilde P) - \lvert H(\tilde P,\tilde Q)\rvert^{2}/H(\tilde Q,\tilde Q)$. The left-hand side is non-negative by the positivity of the form, so the inequality follows; equality is $H(\tilde R,\tilde R) = 0$, which by the absence of isotropic vectors is $\tilde R = 0$, that is $\tilde P = \lambda\tilde Q$. $200$ random pairs gave no violation. $\square$

**Remark (an inequality of the form, not of a distance).** The statement is an inequality between values of the sesquilinear form and is algebraic: it uses the positivity of the form and the quadratic development, and no length is attached to the elements. It is the Cauchy and Schwarz inequality of any positive definite Hermitian form, read here on the biquaternion space; the companion quaternion row, whose form $B$ is indefinite, has no such inequality.

## The Trace Functional and the Trace Form

**Proposition (the trace form is the form).** For all $\tilde P,\tilde Q$,

$$
\mathrm{Sc}(\tilde P\star\tilde Q) = H(\tilde P,\tilde Q) ,
$$

so the block has **no second form**: the trace form of the multiplication and the form that defines it are one object.

*Proof.* $\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0$ and $\mathrm{Sc}(e_0) = 1$. Verified on $60$ pairs to $1.8\times10^{-15}$. $\square$

**Remark (the trace functional).** The linear functional attached to the block is the scalar part $\mathrm{Sc}: \tilde Q \mapsto Q_0$, and in the $2\times2$ matrix model it is one half of the matrix trace, $\mathrm{Sc}(\tilde Q) = \tfrac12\operatorname{Tr}\Phi(\tilde Q)$ (*The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*). On a value of the product it reads $\mathrm{Sc}(\tilde P\star\tilde Q) = H(\tilde P,\tilde Q)$, and the matrix trace of a value is twice the form,

$$
\operatorname{Tr}\Phi(\tilde P\star\tilde Q) = 2\,H(\tilde P,\tilde Q) ,
$$

the trace identity of the model. There is no fourth form to compare with: the block has only $H$.

## The Invariance under the Product

**Theorem (the invariance fails).** The form $H$ is **not** invariant under the product: there are $\tilde P,\tilde Q,\tilde R$ with

$$
H(\tilde P\star\tilde Q,\tilde R) \neq H(\tilde P,\tilde Q\star\tilde R) .
$$

The witness is $\tilde P = \tilde Q = e_1$, $\tilde R = e_0$, where

$$
H(e_1\star e_1,e_0) = H(e_0,e_0) = 1 , \qquad H(e_1,e_1\star e_0) = H(e_1,0) = 0 .
$$

*Proof.* $e_1\star e_1 = H(e_1,e_1)e_0 = e_0$, so the first quantity is $H(e_0,e_0) = 1$; and $e_1\star e_0 = H(e_1,e_0)e_0 = 0$, so the second vanishes. The two sides $1$ and $0$ were recomputed. $\square$

**Remark (the comparison with the symmetric plain block).** The trace form of the symmetric plain block, $\tau(\tilde P,\tilde Q) = \mathrm{Sc}(\tilde P\bullet\tilde Q) = P_0Q_0 - (\mathbf P,\mathbf Q)$, **is** invariant, $\tau(\tilde P\bullet\tilde Q,\tilde R) = \tau(\tilde P,\tilde Q\bullet\tilde R)$, and the invariance is the associativity of the plain product read on the Jordan product (*The Trace Form and the Invariance of the Symmetric Plain Algebra*). The block of this article fails the same test, and the reason is the rank-one central image: the invariance $\mathrm{Sc}((\tilde P\star\tilde Q)\star\tilde R) = \mathrm{Sc}(\tilde P\star(\tilde Q\star\tilde R))$ reads $H(\tilde P,\tilde Q)\overline{R_0} = \overline{H(\tilde Q,\tilde R)}\,P_0 = H(\tilde R,\tilde Q)P_0$ for all $\tilde P,\tilde Q,\tilde R$, and taking $\tilde P = \tilde Q = e_1$, $\tilde R = e_0$ gives $1$ on the left and $0$ on the right, so the identity fails. The product is conjugate-commutative and central, and its trace form cannot be associative.

## The Restriction to the Remarkable Subspaces

The form $H$ restricts to each of the remarkable subspaces, and on each restriction it is again positive definite; the rank is the real dimension of the subspace and the positivity is inherited from the definite form of the whole space.

| subspace | real dimension | $H$ restricted | rank over $\mathbb{R}$ | positivity |
|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $2$ | $\lambda\overline{\mu}$ on the coordinate | $2$ | positive definite |
| $\mathrm{Vect}(\mathbb{B})$ | $6$ | $\sum_{k} P_k\overline{Q_k}$ | $6$ | positive definite |
| $\mathbb{H}_{\mathbb{B}}$ | $4$ | $\sum_\mu P_\mu Q_\mu$ on real coordinates | $4$ | positive definite |
| $i\mathbb{H}_{\mathbb{B}}$ | $4$ | $\sum_\mu P_\mu\overline{Q_\mu}$ on imaginary coordinates | $4$ | positive definite |
| $\mathbb{M}_+$ | $4$ | $\sum_\mu P_\mu\overline{Q_\mu}$, real-valued | $4$ | positive definite |
| $\mathbb{M}_-$ | $4$ | $\sum_\mu P_\mu\overline{Q_\mu}$, real-valued | $4$ | positive definite |

**Proposition (the restrictions).** On each of the remarkable subspaces the restriction of $H$ is positive definite, of rank equal to the real dimension of the subspace, and it is real-valued with the identity form in the natural real basis on $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ and $\mathbb{M}_-$.

*Proof.* $H$ is positive definite on the whole real space, so its restriction to every real subspace is positive definite, hence non-degenerate of rank the real dimension; on the four real subspaces $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ and $\mathbb{M}_-$ the natural real bases give the identity form, and on the two complex subspaces $\mathbb{C}_{\mathbb{B}}$ and $\mathrm{Vect}(\mathbb{B})$ the real bases $e_0,ie_0$ and $e_k,ie_k$ do the same. The form was recomputed on elements of each subspace. $\square$

**Corollary (the block and the remarkable subspaces).** Because the values of the product are central, the product of two elements of any one of the remarkable subspaces is a scalar multiple of $e_0$, real precisely on the four subspaces on which $H$ is real-valued; and the subspace is closed under the product exactly when it contains the idempotent $e_0$: the centre, the quaternion subspace and the Hermitian subspace are closed, and the vector subspace, the anti-quaternion subspace and the anti-Hermitian subspace are not. The restriction of the form is positive definite in every case; only the closure of the product separates the remarkable subspaces. This is the reading of the remarkable subspaces of *Remarkable Subspaces under the Symmetric Plain Sesqualgebra of Biquaternions*, and the flatness of the table — every restriction positive, only the closure differing — is the mark of the central image.

## The Bridge to the Quaternion Form

**Theorem (the coincidence on the real subspace).** On the real elements, $\tilde P,\tilde Q \in \mathbb{H}_{\mathbb{B}}$,

$$
H(\tilde P,\tilde Q) = B(\tilde P,\tilde Q) = P_0Q_0 + (\mathbf P,\mathbf Q) ,
$$

the quaternion form of the symmetric quaternionic block; off the real subspace the two forms part company.

*Proof.* For real coordinates $\overline{Q_\mu} = Q_\mu$, so $H(\tilde P,\tilde Q) = \sum_\mu P_\mu Q_\mu = P_0Q_0 + (\mathbf P,\mathbf Q) = B(\tilde P,\tilde Q)$; the form $B$ is *The Quaternion Form as a Product on the Symmetric Quaternionic Algebra*. For $\tilde P = \tilde Q = ie_0$ one has $H = 1$ and $B = -1$, so the two differ off the real subspace. Verified on $60$ real pairs to $4.4\times10^{-16}$. $\square$

**Corollary (the shared real part).** The two central blocks, the symmetric quaternionic and the symmetric plain sesquilinear, agree on the real elements and differ on the imaginary ones; in the table of the twelve the coincidence is recorded as $\mathrm{SQA} = \mathrm{SPS}$ on the real part. The bridge is the visible form of the two forms being the real and the complex reading of one pairing, the bilinear $B$ and the sesquilinear $H$.

## Worked Examples

**The basis and the Gram matrix.** $H(e_\mu,e_\nu) = \delta_{\mu\nu}$, so the Gram matrix is the identity and the table of the block is the identity times $e_0$. On $e_0 + ie_1$ the diagonal is $H = 2$ and the value of the square is $2e_0$.

**A non-real pairing.** $H(e_0,ie_0) = \overline{i} = -i$, while $H(ie_0,e_0) = i$; the two are conjugate, the Hermitian symmetry of the form.

**The invariance witness.** $H(e_1\star e_1,e_0) = 1$ and $H(e_1,e_1\star e_0) = 0$; the failure of the invariance is measured by the element $e_0$, on which the product vanishes.

**A Cauchy and Schwarz equality.** For $\tilde P = \lambda\tilde Q$ the two sides of the inequality are equal; for $\tilde P = e_0$, $\tilde Q = e_1$ they are $0 \le 1$. The form was checked on $200$ random pairs with no violation.

## Summary

The symmetric plain sesqualgebra is the Hermitian form $H(\tilde P,\tilde Q) = P_0\overline{Q_0} + (\mathbf P,\overline{\mathbf Q})$ read as a multiplication, $\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0$; the product and the form are the same data, the image of the product is the centre and its rank is one. The Gram matrix of $H$ on the algebra basis is the **identity**, the sixteen products are $e_\mu\star e_\nu = \delta_{\mu\nu}e_0$, and the form is **positive definite** of signature $(8,0)$ on the real space, with diagonal $H(\tilde Q,\tilde Q) = \sum_\mu\lvert Q_\mu\rvert^{2}$ strictly positive off the origin and no isotropic vector. The **Cauchy and Schwarz inequality** $\lvert H(\tilde P,\tilde Q)\rvert^{2} \le H(\tilde P,\tilde P)H(\tilde Q,\tilde Q)$ holds, with equality exactly for linearly dependent $\tilde P,\tilde Q$; it is an inequality of the form and not of a distance. The **trace form is the form itself**, $\mathrm{Sc}(\tilde P\star\tilde Q) = H(\tilde P,\tilde Q)$, and the trace functional is the scalar part; in the $2\times2$ model $\operatorname{Tr}\Phi(\tilde P\star\tilde Q) = 2H(\tilde P,\tilde Q)$. The **invariance under the product fails**, with the witness $H(e_1\star e_1,e_0) = 1$ against $H(e_1,e_1\star e_0) = 0$, in contrast with the symmetric plain block whose trace form is invariant; the failure is the rank-one central image. On each of the **remarkable subspaces** the restriction is positive definite of rank the real dimension, and only the closure of the product separates the remarkable subspaces, the centre, the quaternion subspace and the Hermitian subspace being the closed ones. Finally $H$ coincides with the quaternion form $B$ on the real subspace, so the two central blocks agree there and differ on the imaginary elements.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0$ | the block, the form read as a product |
| $H(\tilde P,\tilde Q) = \sum_\mu P_\mu\overline{Q_\mu}$ | the Hermitian form of the block |
| $H(e_\mu,e_\nu) = \delta_{\mu\nu}$ | the Gram matrix is the identity |
| $H(\tilde Q,\tilde Q) = \sum_\mu\lvert Q_\mu\rvert^{2} > 0$ | the diagonal; no isotropic vector |
| $\lvert H(\tilde P,\tilde Q)\rvert^{2} \le H(\tilde P,\tilde P)H(\tilde Q,\tilde Q)$ | the Cauchy and Schwarz inequality; equality iff dependent |
| $\mathrm{Sc}(\tilde P\star\tilde Q) = H(\tilde P,\tilde Q)$ | the trace form is the form |
| $\operatorname{Tr}\Phi(\tilde P\star\tilde Q) = 2H(\tilde P,\tilde Q)$ | the matrix trace of a value |
| $H(e_1\star e_1,e_0) = 1 \neq 0 = H(e_1,e_1\star e_0)$ | the failure of the invariance |
| $H = B$ on $\mathbb{H}_{\mathbb{B}}$ | the bridge to the quaternion form |

## Further Reading

- *Introduction to the Symmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-plain-sesqualgebra-of-biquaternions.md`), for the product, its central image and its table.
- *The Conjugate-Commutative Law and the Idempotents of the Symmetric Plain Sesqualgebra* (`articles_maths/the-conjugate-commutative-law-and-the-idempotents-of-the-symmetric-plain-sesqualgebra.md`), for the law, the idempotents and the vanishing annihilator.
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the form $H$, its positivity and its signature on the six real forms.
- *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/positivity-and-the-hermitian-cone-of-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the cone generated by the diagonal of the form.
- *The Canonical Hermitian Form on the Regular Module of the Biquaternion Algebra* (`articles_maths/the-canonical-hermitian-form-on-the-regular-module-of-the-biquaternion-algebra.md`), for the module-theoretic reading of the same form.
- *The Trace Form and the Invariance of the Symmetric Plain Algebra* (`articles_maths/the-trace-form-and-the-invariance-of-the-symmetric-plain-algebra.md`), the sibling whose trace form is invariant, for the comparison.
- *The Quaternion Form as a Product on the Symmetric Quaternionic Algebra* (`articles_maths/the-quaternion-form-as-a-product-on-the-symmetric-quaternionic-algebra.md`), for the form $B$ and the bridge.
- *Comparison Between the Four General Products* (`articles_maths/comparison-between-the-four-general-products.md`), for the four forms of the space and the coincidence $\mathrm{SQA} = \mathrm{SPS}$ on the real part.
- *Remarkable Subspaces under the Symmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-symmetric-plain-sesqualgebra-of-biquaternions.md`), for the remarkable subspaces under the product.
