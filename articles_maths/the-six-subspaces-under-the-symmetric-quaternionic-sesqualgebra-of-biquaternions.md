# __The Six Subspaces under the Symmetric Quaternionic Sesqualgebra of Biquaternions__

## Introduction

The symmetric quaternionic sesquilinear product of *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions* is defined on the whole complex space of the biquaternion algebra, and the six distinguished real subspaces of the algebra carry it in six different ways. The six are the **centre** $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$, the **vector subspace** $\mathbf{e}=\mathrm{span}_{\mathbb{R}}\{e_1,e_2,e_3,ie_1,ie_2,ie_3\}$, the **real quaternion subspace** $\mathbb{H}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_0,e_1,e_2,e_3\}$, the **anti-quaternion subspace** $i\mathbb{H}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{ie_0,ie_1,ie_2,ie_3\}$, the **Hermitian subspace** $\mathbb{M}_{+}=\mathrm{span}_{\mathbb{R}}\{e_0,ie_1,ie_2,ie_3\}$ and the **anti-Hermitian subspace** $\mathbb{M}_{-}=\mathrm{span}_{\mathbb{R}}\{ie_0,e_1,e_2,e_3\}$. They are defined and compared in *Introduction to the Six Subspaces*, and the product of the general quaternionic sesquilinear row is read on them in *The Six Subspaces under the General Quaternionic Sesqualgebra of Biquaternions*.

The product of the block is the half-sum of the two orders of the general product, so the cross product vanishes on its diagonal and survives only in the difference between the two orders; the consequence for the six subspaces is a closure pattern different from the one of the general product. The centre is closed; so are the real quaternion subspace and the Hermitian subspace, the two subspaces on which the coefficients are real up to a factor $i$ and the form is a real symmetric form. The other three are not closed, and the images fall in lower subspaces: the vector subspace maps into the centre, the anti-quaternion subspace into the real quaternion subspace, and the anti-Hermitian subspace into the Hermitian subspace. The values of a general pair, by contrast, are not confined to any subspace of the six: their smallest real span is the whole algebra.

The product is *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions*; the diagonal and the elements of square zero are *The Non-Central Diagonal and the Two Halves of the Symmetric Quaternionic Sesqualgebra*; the form $K$ and its restrictions are *The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra* and *The Krein Gram Matrix and the Restrictions of the Form*; the analogous closure table for the general product is *The Six Subspaces under the General Quaternionic Sesqualgebra of Biquaternions*; and the comparison of the closure patterns of the four rows is assembled in *The 12 Products of the Biquaternion Complex Space*.

**Conventions.** $\tilde Q=\sum_\mu Q_\mu e_\mu$; $\mathbb{B}=\mathbb{C}e_0\oplus\mathbf{e}$ is the scalar–vector decomposition; $K(\tilde P,\tilde Q)=P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})$; a real element has real coefficients, a Hermitian element has a real scalar coefficient and purely imaginary vector coefficients, and an anti-Hermitian element the reverse. The product is $\tilde P\star\tilde Q=K(\tilde P,\tilde Q)e_0-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}$.

## The Product Rule on Each Subspace

**Theorem (the scalar–vector form is the common rule).** On each of the six subspaces the product is read from the single rule

$$
\tilde P\star\tilde Q=K(\tilde P,\tilde Q)e_0-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P},
$$

the first summand lying in the centre and the second in the vector subspace.

*Proof.* This is the scalar–vector form of the introduction; every subspace computation below specialises the coefficients in it. $\square$

## The Centre

**Theorem (closure).** For central elements $\lambda e_0$ and $\mu e_0$,

$$
(\lambda e_0)\star(\mu e_0)=\lambda\overline{\mu}\,e_0.
$$

The centre is closed, and with this product it is a conjugate-commutative, non-associative algebra over $\mathbb{R}$ whose multiplication is $(\lambda,\mu)\mapsto\lambda\overline{\mu}$.

*Proof.* $\lambda e_0$ and $\mu e_0$ have scalar coefficients $\lambda,\mu$ and zero vector coefficients, so the rule gives $K=\lambda\overline{\mu}$ and zero vector part; hence the value is $\lambda\overline{\mu}e_0$. The multiplication is conjugate-commutative, $(\lambda,\mu)\mapsto\lambda\overline{\mu}=\overline{\mu\overline{\lambda}}$, and it is neither commutative nor associative: $i\star1=i$ while $1\star i=-i$, and $(1\star i)\star i=-1$ while $1\star(i\star i)=1$. $\square$

**Remark.** The centre is closed but is not the field $\mathbb{C}$: the induced product $\lambda\overline{\mu}$ is the ordinary multiplication followed by conjugation of the second factor, it is conjugate-commutative rather than commutative, and it is not associative, so no isomorphism with $(\mathbb{C},\cdot)$ exists. The conjugate in the product formula, $\lambda\overline{\mu}$, is the trace of the semilinearity of the second slot.

## The Vector Subspace

**Theorem (the product lands in the centre).** For $\tilde P,\tilde Q$ in the vector subspace,

$$
\tilde P\star\tilde Q=K(\tilde P,\tilde Q)\,e_0,
\qquad
K(\tilde P,\tilde Q)=-(\mathbf{P},\overline{\mathbf{Q}}),
$$

a central element. The vector subspace is not closed; the image of the product on it is the centre, of real rank two.

*Proof.* For $\tilde P,\tilde Q$ in the vector subspace the scalar coefficients $P_0,Q_0$ vanish, so the mixed term $-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}$ vanishes and only the centre part remains. The value $K(\tilde P,\tilde Q)=-(\mathbf{P},\overline{\mathbf{Q}})$ ranges over $\mathbb{C}$ as $\mathbf{P},\mathbf{Q}$ range, so the image is the whole centre, of real rank two. $\square$

**Remark.** The product of two vectors is a scalar, as in a Clifford algebra; the difference is that the scalar is the *form value* and not the symmetric bilinear pair, and that the product of a vector with itself is negative, $e_1\star e_1=-e_0$, on every vector direction.

## The Real Quaternion Subspace

**Theorem (closure and the product table).** On real elements the product is

$$
p\star q=\Bigl(p_0q_0-\sum_{k=1}^{3}p_kq_k\Bigr)e_0-p_0\mathbf{q}-q_0\mathbf{p},
$$

with the multiplication table

| $\star$ | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
|---|---|---|---|---|
| $e_0$ | $e_0$ | $-e_1$ | $-e_2$ | $-e_3$ |
| $e_1$ | $-e_1$ | $-e_0$ | $0$ | $0$ |
| $e_2$ | $-e_2$ | $0$ | $-e_0$ | $0$ |
| $e_3$ | $-e_3$ | $0$ | $0$ | $-e_0$ |

The real quaternion subspace is closed under the product and commutative on it, of real image rank four.

*Proof.* For real $p,q$ the bar is the identity, so the rule gives the displayed value, which is real; this is the table of the introduction with real coefficients. The table is symmetric, so the product is commutative on the subspace. The values span the four real directions: $e_0\star e_0=e_0$ and, for each $k$, $e_0\star e_k=-e_k$; so the image is the whole real quaternion subspace, of real rank four. $\square$

**Remark (the commutative algebra).** The table defines a commutative, non-associative algebra on the real quaternion subspace: $e_k\star e_k=-e_0$ on each vector direction and $e_i\star e_j=0$ for distinct vector directions, so it is not the quaternion multiplication. It is the natural conjugate of the plain symmetric product, $p\star q=\bigl(\mathrm{SPA}(p,q)\bigr)^{\natural}$, so its scalar part is the symmetric bilinear form $p_0q_0-\sum_kp_kq_k$ times $e_0$ and its vector part the mixed term $-p_0\mathbf{q}-q_0\mathbf{p}$ alone. The idempotents of the block lie here, with the family $-\tfrac12e_0+\boldsymbol\mu$ of the diagonal article.

## The Anti-Quaternion Subspace

**Theorem (the product lands in the real quaternion subspace).** For $\tilde P=i p$, $\tilde Q=iq$ with $p,q$ real,

$$
\tilde P\star\tilde Q=\Bigl(p_0q_0-\sum_{k=1}^{3}p_kq_k\Bigr)e_0-p_0\mathbf{q}-q_0\mathbf{p},
$$

an element of the real quaternion subspace. The anti-quaternion subspace is not closed; its image is the real quaternion subspace, of real rank four.

*Proof.* For $\tilde P=ip$ the scalar coefficient is $ip_0$ and the vector coefficients are $ip_k$, so $K(\tilde P,\tilde Q)=(ip_0)\overline{(iq_0)}-\sum_k(ip_k)\overline{(iq_k)}=(ip_0)(-iq_0)-\sum_k(ip_k)(-iq_k)=p_0q_0-\sum_kp_kq_k$, real. The vector part is $-ip_0\overline{iq}-\overline{iq_0}\,ip=-ip_0(-i)\mathbf{q}-(-iq_0)ip=-p_0\mathbf{q}-q_0\mathbf{p}$, real. So the value is real, and the image is the whole real quaternion subspace. $\square$

**Remark.** The anti-quaternion subspace carries the same product as the real quaternion subspace, transported by $p\mapsto ip$; the two are the two real forms of the same four-real-dimensional product.

## The Hermitian Subspace

**Theorem (closure).** For $\tilde P=a_0+i\boldsymbol{\alpha}$, $\tilde Q=b_0+i\boldsymbol{\beta}$ with real scalar coefficients and real vector parts,

$$
\tilde P\star\tilde Q=\Bigl(a_0b_0-\sum_{k=1}^{3}\alpha_k\beta_k\Bigr)e_0
+i\bigl(a_0\boldsymbol{\beta}-b_0\boldsymbol{\alpha}\bigr),
$$

an element of the Hermitian subspace: a real scalar part and a purely imaginary vector part. The Hermitian subspace is closed under the product, and its image is itself, of real rank four.

*Proof.* A Hermitian element has a real scalar coefficient and purely imaginary vector coefficients; thus $P_0=a_0$, $\mathbf{P}=i\boldsymbol{\alpha}$ with $a_0,\boldsymbol{\alpha}$ real. Then $K=P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})=a_0b_0-\sum_k(i\alpha_k)\overline{(i\beta_k)}=a_0b_0-\sum_k(i\alpha_k)(-i\beta_k)=a_0b_0-\sum_k\alpha_k\beta_k$, real. The vector part is $-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}=-a_0(-i\boldsymbol{\beta})-b_0(i\boldsymbol{\alpha})=i(a_0\boldsymbol{\beta}-b_0\boldsymbol{\alpha})$, purely imaginary. So the value is Hermitian. The image is the whole subspace, since $e_0\star e_0=e_0$ and $e_0\star ie_k=ie_k$ span the four real directions $e_0,ie_1,ie_2,ie_3$. $\square$

**Remark.** With the centre and the real quaternion subspace, the Hermitian subspace is the third closed subspace of the block; the three closed subspaces are exactly the centre, the real quaternion subspace and the Hermitian subspace. On the real quaternion subspace the product is commutative; on the centre it is only conjugate-commutative; and on the Hermitian subspace it is not commutative either, since the imaginary vector part $i(a_0\boldsymbol{\beta}-b_0\boldsymbol{\alpha})$ changes sign under the exchange of the two factors. The Hermitian subspace carries the form of signature $(1,3)$, one of the two real four-dimensional restrictions of $K$ read in *The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra*.

## The Anti-Hermitian Subspace

**Theorem (the product lands in the Hermitian subspace).** For $\tilde P=ia_0+\boldsymbol{\alpha}$, $\tilde Q=ib_0+\boldsymbol{\beta}$ with real coefficients,

$$
\tilde P\star\tilde Q=\Bigl(a_0b_0-\sum_{k=1}^{3}\alpha_k\beta_k\Bigr)e_0
+i\bigl(b_0\boldsymbol{\alpha}-a_0\boldsymbol{\beta}\bigr),
$$

an element of the Hermitian subspace. The anti-Hermitian subspace is not closed; its image is the Hermitian subspace, of real rank four.

*Proof.* Here $P_0=ia_0$ and $\mathbf{P}=\boldsymbol{\alpha}$, so $\overline{Q_0}=-ib_0$ and $\overline{\mathbf{Q}}=\boldsymbol{\beta}$. The scalar part is $K=(ia_0)(-ib_0)-\sum_k\alpha_k\beta_k=a_0b_0-\sum_k\alpha_k\beta_k$, real. The vector part is $-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}=-(ia_0)\boldsymbol{\beta}-(-ib_0)\boldsymbol{\alpha}=i(b_0\boldsymbol{\alpha}-a_0\boldsymbol{\beta})$, purely imaginary. So the value is Hermitian, and the span of the values is the Hermitian subspace. $\square$

**Remark.** The anti-Hermitian subspace carries the product out of itself into the Hermitian subspace, exactly as the anti-quaternion subspace carries it into the real quaternion subspace; the pattern is that the three not-closed subspaces each lose one level, in the chain $\mathbf{e}\to\mathbb{C}e_0$, $i\mathbb{H}_{\mathbb{B}}\to\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_{-}\to\mathbb{M}_{+}$.

## The Table of the Six

**Theorem (the closure table).** The behaviour of the product on the six subspaces is

| Subspace | Closed? | Image | Real rank of the image |
|---|---|---|---|
| centre $\mathbb{C}e_0$ | yes | centre | $2$ |
| vector $\mathbf{e}$ | no | centre | $2$ |
| real quaternion $\mathbb{H}_{\mathbb{B}}$ | yes | $\mathbb{H}_{\mathbb{B}}$ | $4$ |
| anti-quaternion $i\mathbb{H}_{\mathbb{B}}$ | no | $\mathbb{H}_{\mathbb{B}}$ | $4$ |
| Hermitian $\mathbb{M}_{+}$ | yes | $\mathbb{M}_{+}$ | $4$ |
| anti-Hermitian $\mathbb{M}_{-}$ | no | $\mathbb{M}_{+}$ | $4$ |

*Proof.* The six rows are the six theorems above, each of which computes the image and its real dimension; the closed rows are those whose image is the subspace itself. $\square$

**Remark (the comparison with the menu of the six).** The menu of the six subspaces records the closure of the centre and the failure of closure of the other five. The computation gives a finer pattern: the centre, the real quaternion subspace and the Hermitian subspace are closed, and the vector, anti-quaternion and anti-Hermitian subspaces are not. The three closed subspaces are exactly the centre, the real quaternion subspace and the Hermitian subspace; the block has three of them rather than one. The eight-row comparison across the four general products is assembled in *The 12 Products of the Biquaternion Complex Space*; the four rows of the general quaternionic row are in *The Six Subspaces under the General Quaternionic Sesqualgebra of Biquaternions*.

## The Values of a General Pair

**Theorem (the smallest real span of the values).** The smallest real subspace of $\mathbb{B}$ that contains the values $\tilde P\star\tilde Q$ of all pairs is $\mathbb{B}$ itself, of real dimension eight, with basis $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$. The scalar part of a value lies in the centre and the vector part in the vector subspace, and the two parts together generate the whole algebra.

*Proof.* The scalar part $K(\tilde P,\tilde Q)=P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})$ ranges over $\mathbb{C}$: taking $\mathbf{P}=\mathbf{Q}=0$ gives $K=P_0\overline{Q_0}$, which is any complex number. The vector part is $-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}$; taking $\tilde P=e_0$ and $\tilde Q$ arbitrary gives $-\overline{\mathbf{Q}}$, which ranges over the whole vector subspace. Hence the span contains the complex line $\mathbb{C}e_0$ and the vector subspace, whose sum is $\mathbb{B}$ of real dimension eight; no smaller subspace contains all values. $\square$

**Theorem (the span on each subspace).** Restricted to the six subspaces, the values span subspaces of real dimension

$$
2,\ 2,\ 4,\ 4,\ 4,\ 4
$$

for the centre, the vector subspace, the real quaternion, anti-quaternion, Hermitian and anti-Hermitian subspaces respectively.

*Proof.* On the centre the value is $(\lambda e_0)\star(\mu e_0)=\lambda\overline{\mu}\,e_0$, which spans $\mathbb{C}e_0$, of real dimension two as $\lambda\overline{\mu}$ ranges over $\mathbb{C}$; on the vector subspace the value is $K(\tilde P,\tilde Q)e_0$, and $K=-(\mathbf{P},\overline{\mathbf{Q}})$ likewise ranges over $\mathbb{C}$, so the span is again the centre, of real dimension two. On each of the four four-dimensional subspaces the values span a space of real dimension four, read from pairs that lie in the subspace itself: $e_0\star e_0=e_0$ and $e_0\star e_k=-e_k$ span $\mathbb{H}_{\mathbb{B}}$, the image of the real quaternion subspace; $e_0\star e_0=e_0$ and $e_0\star ie_k=ie_k$ span $\mathbb{M}_{+}$, the image of the Hermitian subspace; and $ie_0\star ie_0=e_0$, $ie_0\star ie_k=-e_k$ span $\mathbb{H}_{\mathbb{B}}$ for the anti-quaternion subspace, while $ie_0\star ie_0=e_0$, $ie_0\star e_k=-ie_k$ span $\mathbb{M}_{+}$ for the anti-Hermitian one. $\square$

**Remark (the image is not among the six).** The values of a general pair lie in no subspace of the six, and their span is the whole algebra; this is the content of the first theorem, and it is the reason the block's image is not one of the six subspaces — unlike the image of the sibling sesquilinear symmetrisation $\mathrm{SPS}$, which is the centre. The corresponding statement for the general quaternionic sesquilinear row is in *The Six Subspaces under the General Quaternionic Sesqualgebra of Biquaternions*.

## Worked Examples

**A central product.** $(2e_0)\star(3ie_0)=2\,\overline{3i}\,e_0=-6ie_0$; the conjugate of the second coefficient in the product formula is visible.

**A vector product.** $e_1\star e_2=0$: $K(e_1,e_2)=0$ and both scalar coefficients vanish.

**A vector square.** $e_1\star e_1=-e_0$: the value is the form value times the identity.

**A real quaternion product.** $(e_0+e_1)\star(e_0+e_1)=-2e_1$: the product is real, and it is not central, so the real quaternion subspace is closed but not central.

**A Hermitian product.** $(e_0+ie_1)\star(e_0+ie_1)$: $K=1-1=0$ and the mixed term, computed from the displayed formula with $a_0=1,\boldsymbol{\alpha}=e_1$ and $b_0=1,\boldsymbol{\beta}=e_1$, is $i(e_1-e_1)=0$; the square is zero, an element of the isotropic cone.

**An anti-Hermitian product.** $(ie_0+e_1)\star(ie_0+e_2)=e_0+i(e_1-e_2)$: the scalar coefficient $a_0=b_0=1$ and the vector parts $\boldsymbol{\alpha}=e_1$, $\boldsymbol{\beta}=e_2$ give $K=1$ and the imaginary vector $i(e_1-e_2)$, an element of the Hermitian subspace; the diagonal case $\tilde Q=ie_0+e_1$ has square $K(\tilde Q,\tilde Q)e_0+i(1\cdot e_1-1\cdot e_1)=0$, an isotropic element.

## Summary

The product of the block is read on the six subspaces by the single rule $\tilde P\star\tilde Q=K(\tilde P,\tilde Q)e_0-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}$. The centre is closed, with $(\lambda e_0)\star(\mu e_0)=\lambda\overline{\mu}\,e_0$; the vector subspace is not closed and maps into the centre, of real rank two; the real quaternion subspace is closed and commutative, of real rank four; the anti-quaternion subspace is not closed and maps onto the real quaternion subspace; the Hermitian subspace is closed, of real rank four; and the anti-Hermitian subspace is not closed and maps onto the Hermitian subspace. Three subspaces are closed — the centre, the real quaternion subspace and the Hermitian subspace — and three are not, with images one level down. The values of a general pair are not confined to a subspace of the six: their smallest real span is the whole algebra, of real dimension eight, with the scalar part in the centre and the vector part in the vector subspace.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ | the centre; closed, image rank $2$ |
| $\mathbf{e}$ | the vector subspace; image the centre, rank $2$ |
| $\mathbb{H}_{\mathbb{B}}$ | the real quaternion subspace; closed, image rank $4$ |
| $i\mathbb{H}_{\mathbb{B}}$ | the anti-quaternion subspace; image $\mathbb{H}_{\mathbb{B}}$, rank $4$ |
| $\mathbb{M}_{+}$ | the Hermitian subspace; closed, image rank $4$ |
| $\mathbb{M}_{-}$ | the anti-Hermitian subspace; image $\mathbb{M}_{+}$, rank $4$ |
| $\mathrm{span}_{\mathbb{R}}\{\tilde P\star\tilde Q:\tilde P,\tilde Q\in\mathbb{B}\}=\mathbb{B}$ | the smallest real span, of the values of all pairs, of real dimension eight |

## Further Reading

- *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-sesqualgebra-of-biquaternions.md`), for the product and its scalar–vector form.
- *The Non-Central Diagonal and the Two Halves of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/the-non-central-diagonal-and-the-two-halves-of-the-symmetric-quaternionic-sesqualgebra.md`), for the diagonal, the idempotents and the square-zero elements on the closed subspaces.
- *The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra* (`articles_maths/the-krein-form-as-a-product-on-the-symmetric-quaternionic-sesqualgebra.md`), for the form and its restriction to the six subspaces.
- *The Krein Gram Matrix and the Restrictions of the Form* (`articles_maths/the-krein-gram-matrix-and-the-restrictions-of-the-form.md`), for the form $K$ and its Gram matrices.
- *Introduction to the Six Subspaces* (`articles_maths/introduction-to-the-six-subspaces.md`), for the definition and the comparison of the six subspaces.
- *The Six Subspaces under the General Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/the-six-subspaces-under-the-general-quaternionic-sesqualgebra-of-biquaternions.md`), for the same six subspaces under the general product.
- *The 12 Products of the Biquaternion Complex Space* (`articles_maths/the-12-products-of-the-biquaternion-complex-space.md`), for the comparison of the closure patterns of the twelve operations.
