# __Remarkable Subspaces under the Symmetric Quaternionic Sesqualgebra__

## Introduction

The symmetric quaternionic sesquilinear product of *Introduction to the Symmetric Quaternionic Sesqualgebra* is defined on the whole complex space of the biquaternion algebra, and the remarkable real subspaces of the algebra carry it in six different ways. The remarkable subspaces are the **centre** $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$, the **vector subspace** $\mathbf{e}=\mathrm{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z,i\vec e_x,i\vec e_y,i\vec e_z\}$, the **real quaternion subspace** $\mathbb{H}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_t,\vec e_x,\vec e_y,\vec e_z\}$, the **anti-quaternion subspace** $i\mathbb{H}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{ie_t,i\vec e_x,i\vec e_y,i\vec e_z\}$, the **Hermitian subspace** $\mathbb{M}_{+}=\mathrm{span}_{\mathbb{R}}\{e_t,i\vec e_x,i\vec e_y,i\vec e_z\}$ and the **anti-Hermitian subspace** $\mathbb{M}_{-}=\mathrm{span}_{\mathbb{R}}\{ie_t,\vec e_x,\vec e_y,\vec e_z\}$. They are defined and compared in *Introduction to the Remarkable Subspaces*, and the product of the general quaternionic sesquilinear row is read on them in *Remarkable Subspaces under the General Quaternionic Sesqualgebra*.

The product of the block is the half-sum of the two orders of the general product, so the cross product vanishes on its diagonal and survives only in the difference between the two orders; the consequence for the remarkable subspaces is a closure pattern different from the one of the general product. The centre is closed; so are the real quaternion subspace and the Hermitian subspace, the only two of the
four four-dimensional subspaces that keep the product inside themselves. The other three are not closed, and
the images fall in lower subspaces: the vector subspace maps into the centre, the anti-quaternion subspace
into the real quaternion subspace, and the anti-Hermitian subspace into the Hermitian subspace. The values of
a general pair, by contrast, are not confined to any subspace of the remarkable subspaces: their smallest
real span is the whole algebra.

The product is *Introduction to the Symmetric Quaternionic Sesqualgebra*; the diagonal and the elements of square zero are *The Non-Central Algebraic Norm and the Two Halves of the Symmetric Quaternionic Sesqualgebra*; the form $K$ and its restrictions are *The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra* and *The Krein Gram Matrix and the Restrictions of the Form*; the analogous closure table for the general product is *Remarkable Subspaces under the General Quaternionic Sesqualgebra*; and the comparison of the closure patterns of the four rows is assembled in *The 12 Products of the Biquaternion Complex Space*.

**Conventions.** $\tilde Q=\sum_\mu Q_\mu e_\mu$; $\mathbb{B}=\mathbb{C}e_t\oplus\mathbf{e}$ is the scalar–vector decomposition; $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})$; a real element has real coefficients, a Hermitian element has a real scalar coefficient and purely imaginary vector coefficients, and an anti-Hermitian element the reverse. The product is $\tilde Q_1\star\tilde Q_2=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}e_t-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1$.

## The Product Rule on Each Subspace

**Theorem (the scalar–vector form is the common rule).** On each of the remarkable subspaces the product is read from the single rule

$$
\tilde Q_1\star\tilde Q_2=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}e_t-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1,
$$

the first summand lying in the centre and the second in the vector subspace.

*Proof.* This is the scalar–vector form of the introduction; every subspace computation below specialises the coefficients in it.

## The Centre

**Theorem (closure).** For central elements $\lambda e_t$ and $\mu e_t$,

$$
(\lambda e_t)\star(\mu e_t)=\lambda\overline{\mu}\,e_t.
$$

The centre is closed, and with this product it is a conjugate-commutative, non-associative algebra over $\mathbb{R}$ whose multiplication is $(\lambda,\mu)\mapsto\lambda\overline{\mu}$.

*Proof.* $\lambda e_t$ and $\mu e_t$ have scalar coefficients $\lambda,\mu$ and zero vector coefficients, so the rule gives $K=\lambda\overline{\mu}$ and zero vector part; hence the value is $\lambda\overline{\mu}e_t$. The multiplication is conjugate-commutative, $(\lambda,\mu)\mapsto\lambda\overline{\mu}=\overline{\mu\overline{\lambda}}$, and it is neither commutative nor associative: $i\star1=i$ while $1\star i=-i$, and $(1\star i)\star i=-1$ while $1\star(i\star i)=1$.

**Remark.** The centre is closed but is not the field $\mathbb{C}$: the induced product $\lambda\overline{\mu}$ is the ordinary multiplication followed by conjugation of the second factor, it is conjugate-commutative rather than commutative, and it is not associative, so no isomorphism with $(\mathbb{C},\cdot)$ exists. The conjugate in the product formula, $\lambda\overline{\mu}$, is the trace of the semilinearity of the second slot.

## The Vector Subspace

**Theorem (the product lands in the centre).** For $\tilde Q_1,\tilde Q_2$ in the vector subspace,

$$
\tilde Q_1\star\tilde Q_2=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}\,e_t,
\qquad
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=-(\vec Q_1,\overline{\vec Q_2}),
$$

a central element. The vector subspace is not closed; the image of the product on it is the centre, of real rank two.

*Proof.* For $\tilde Q_1,\tilde Q_2$ in the vector subspace the scalar coefficients $Q_{1t},Q_{2t}$ vanish, so the mixed term $-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1$ vanishes and only the centre part remains. The value $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=-(\vec Q_1,\overline{\vec Q_2})$ ranges over $\mathbb{C}$ as $\vec Q_1,\vec Q_2$ range, so the image is the whole centre, of real rank two.

**Remark.** The product of two vectors is a scalar, as in a Clifford algebra; the difference is that the scalar is the *form value* and not the symmetric bilinear pair, and that the product of a vector with itself is negative, $\vec e_x\star \vec e_x=-e_t$, on every vector direction.

## The Real Quaternion Subspace

**Theorem (closure and the product table).** On real elements the product is

$$
p\star q=\Bigl(p_tq_t-\sum_{\mu\in\{x,y,z\}}p_\mu q_\mu\Bigr)e_t-p_t\vec q-q_t\vec p,
$$

with the multiplication table

| $\star$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $e_t$ | $-\vec e_x$ | $-\vec e_y$ | $-\vec e_z$ |
| $\vec e_x$ | $-\vec e_x$ | $-e_t$ | $0$ | $0$ |
| $\vec e_y$ | $-\vec e_y$ | $0$ | $-e_t$ | $0$ |
| $\vec e_z$ | $-\vec e_z$ | $0$ | $0$ | $-e_t$ |

The real quaternion subspace is closed under the product and commutative on it, of real image rank four.

*Proof.* For real $p,q$ the bar is the identity, so the rule gives the displayed value, which is real; this is the table of the introduction with real coefficients. The table is symmetric, so the product is commutative on the subspace. The values span the four real directions: $e_t\star e_t=e_t$ and, for each $k$, $e_t\star \vec e_k=-\vec e_k$; so the image is the whole real quaternion subspace, of real rank four.

**Remark (the commutative algebra).** The table defines a commutative, non-associative algebra on the real quaternion subspace: $\vec e_\mu\star \vec e_\mu=-e_t$ on each vector direction and $\vec e_\mu\star \vec e_\nu=0$ for distinct vector directions, so it is not the quaternion multiplication. It is the natural conjugate of the plain symmetric product, $p\star q=\bigl(\mathrm{SPA}(p,q)\bigr)^{\natural}$, so its scalar part is the symmetric bilinear form $p_tq_t-\sum_kp_kq_k$ times $e_t$ and its vector part the mixed term $-p_t\vec q-q_t\vec p$ alone. The idempotents of the block lie here, with the family $-\tfrac12e_t+\tfrac{\sqrt3}{2}\vec u$ of the diagonal article.

## The Anti-Quaternion Subspace

**Theorem (the product lands in the real quaternion subspace).** For $\tilde Q_1=i p$, $\tilde Q_2=iq$ with $p,q$ real,

$$
\tilde Q_1\star\tilde Q_2=\Bigl(p_tq_t-\sum_{\mu\in\{x,y,z\}}p_\mu q_\mu\Bigr)e_t-p_t\vec q-q_t\vec p,
$$

an element of the real quaternion subspace. The anti-quaternion subspace is not closed; its image is the real quaternion subspace, of real rank four.

*Proof.* For $\tilde Q_1=ip$ the scalar coefficient is $ip_t$ and the vector coefficients are $ip_k$, so $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=(ip_t)\overline{(iq_t)}-\sum_k(ip_k)\overline{(iq_k)}=(ip_t)(-iq_t)-\sum_k(ip_k)(-iq_k)=p_tq_t-\sum_kp_kq_k$, real. The vector part is $-ip_t\overline{iq}-\overline{iq_t}\,ip=-ip_t(-i)\vec q-(-iq_t)ip=-p_t\vec q-q_t\vec p$, real. So the value is real, and the image is the whole real quaternion subspace.

**Remark.** The anti-quaternion subspace carries the same product as the real quaternion subspace, transported by $p\mapsto ip$; the two are the two real forms of the same four-real-dimensional product.

## The Hermitian Subspace

**Theorem (closure).** For $\tilde Q_1=a_t+i\vec\alpha$, $\tilde Q_2=b_t+i\vec\beta$ with real scalar coefficients and real vector parts,

$$
\tilde Q_1\star\tilde Q_2=\Bigl(a_tb_t-\sum_{\mu\in\{x,y,z\}}\alpha_\mu\beta_\mu\Bigr)e_t
+i\bigl(a_t\vec\beta-b_t\vec\alpha\bigr),
$$

an element of the Hermitian subspace: a real scalar part and a purely imaginary vector part. The Hermitian subspace is closed under the product, and its image is itself, of real rank four.

*Proof.* A Hermitian element has a real scalar coefficient and purely imaginary vector coefficients; thus $Q_{1t}=a_t$, $\vec Q_1=i\vec\alpha$ with $a_t,\vec\alpha$ real. Then $K=Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})=a_tb_t-\sum_k(i\alpha_k)\overline{(i\beta_k)}=a_tb_t-\sum_k(i\alpha_k)(-i\beta_k)=a_tb_t-\sum_k\alpha_k\beta_k$, real. The vector part is $-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1=-a_t(-i\vec\beta)-b_t(i\vec\alpha)=i(a_t\vec\beta-b_t\vec\alpha)$, purely imaginary. So the value is Hermitian. The image is the whole subspace, since $e_t\star e_t=e_t$ and $e_t\star i\vec e_k=i\vec e_k$ span the four real directions $e_t,i\vec e_x,i\vec e_y,i\vec e_z$.

**Remark.** With the centre and the real quaternion subspace, the Hermitian subspace is the third closed subspace of the block; the three closed subspaces are exactly the centre, the real quaternion subspace and the Hermitian subspace. On the real quaternion subspace the product is commutative; on the centre it is only conjugate-commutative; and on the Hermitian subspace it is not commutative either, since the imaginary vector part $i(a_t\vec\beta-b_t\vec\alpha)$ changes sign under the exchange of the two factors. The Hermitian subspace carries the form of signature $(1,3)$, one of the two real four-dimensional restrictions of $K$ read in *The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra*.

## The Anti-Hermitian Subspace

**Theorem (the product lands in the Hermitian subspace).** For $\tilde Q_1=ia_t+\vec\alpha$, $\tilde Q_2=ib_t+\vec\beta$ with real coefficients,

$$
\tilde Q_1\star\tilde Q_2=\Bigl(a_tb_t-\sum_{\mu\in\{x,y,z\}}\alpha_\mu\beta_\mu\Bigr)e_t
+i\bigl(b_t\vec\alpha-a_t\vec\beta\bigr),
$$

an element of the Hermitian subspace. The anti-Hermitian subspace is not closed; its image is the Hermitian subspace, of real rank four.

*Proof.* Here $Q_{1t}=ia_t$ and $\vec Q_1=\vec\alpha$, so $\overline{Q_{2t}}=-ib_t$ and $\overline{\vec Q_2}=\vec\beta$. The scalar part is $K=(ia_t)(-ib_t)-\sum_k\alpha_k\beta_k=a_tb_t-\sum_k\alpha_k\beta_k$, real. The vector part is $-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1=-(ia_t)\vec\beta-(-ib_t)\vec\alpha=i(b_t\vec\alpha-a_t\vec\beta)$, purely imaginary. So the value is Hermitian, and the span of the values is the Hermitian subspace.

**Remark.** The anti-Hermitian subspace carries the product out of itself into the Hermitian subspace, exactly as the anti-quaternion subspace carries it into the real quaternion subspace; the pattern is that the three not-closed subspaces each lose one level, in the chain $\mathbf{e}\to\mathbb{C}e_t$, $i\mathbb{H}_{\mathbb{B}}\to\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_{-}\to\mathbb{M}_{+}$.

## The Table of the Remarkable Subspaces

**Theorem (the closure table).** The behaviour of the product on the remarkable subspaces is

| Subspace | Closed? | Image | Real rank of the image |
|---|---|---|---|
| centre $\mathbb{C}e_t$ | yes | centre | $2$ |
| vector $\mathbf{e}$ | no | centre | $2$ |
| real quaternion $\mathbb{H}_{\mathbb{B}}$ | yes | $\mathbb{H}_{\mathbb{B}}$ | $4$ |
| anti-quaternion $i\mathbb{H}_{\mathbb{B}}$ | no | $\mathbb{H}_{\mathbb{B}}$ | $4$ |
| Hermitian $\mathbb{M}_{+}$ | yes | $\mathbb{M}_{+}$ | $4$ |
| anti-Hermitian $\mathbb{M}_{-}$ | no | $\mathbb{M}_{+}$ | $4$ |

*Proof.* The rows are the six theorems above, each of which computes the image and its real dimension; the closed rows are those whose image is the subspace itself.

**Remark (the comparison with the menu of the remarkable subspaces).** The menu of the remarkable subspaces records, for the plain product, exactly two closed subspaces, the centre and the real quaternion subspace, and the failure of closure of the other four. The computation gives a finer pattern for the block: the centre, the real quaternion subspace and the Hermitian subspace are closed, and the vector, anti-quaternion and anti-Hermitian subspaces are not. The three closed subspaces are exactly the centre, the real quaternion subspace and the Hermitian subspace; the block has three of them, where the plain product has two. The eight-row comparison across the four general products is assembled in *The 12 Products of the Biquaternion Complex Space*; the four rows of the general quaternionic row are in *Remarkable Subspaces under the General Quaternionic Sesqualgebra*.

## The Values of a General Pair

**Theorem (the smallest real span of the values).** The smallest real subspace of $\mathbb{B}$ that contains the values $\tilde Q_1\star\tilde Q_2$ of all pairs is $\mathbb{B}$ itself, of real dimension eight, with basis $e_t,\vec e_x,\vec e_y,\vec e_z,ie_t,i\vec e_x,i\vec e_y,i\vec e_z$. The scalar part of a value lies in the centre and the vector part in the vector subspace, and the two parts together generate the whole algebra.

*Proof.* The scalar part $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})$ ranges over $\mathbb{C}$: taking $\vec Q_1=\vec Q_2=0$ gives $K=Q_{1t}\overline{Q_{2t}}$, which is any complex number. The vector part is $-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1$; taking $\tilde Q_1=e_t$ and $\tilde Q_2$ arbitrary gives $-\overline{\vec Q_2}$, which ranges over the whole vector subspace. Hence the span contains the complex line $\mathbb{C}e_t$ and the vector subspace, whose sum is $\mathbb{B}$ of real dimension eight; no smaller subspace contains all values.

**Theorem (the span on each subspace).** Restricted to the remarkable subspaces, the values span subspaces of real dimension

$$
2,\ 2,\ 4,\ 4,\ 4,\ 4
$$

for the centre, the vector subspace, the real quaternion, anti-quaternion, Hermitian and anti-Hermitian subspaces respectively.

*Proof.* On the centre the value is $(\lambda e_t)\star(\mu e_t)=\lambda\overline{\mu}\,e_t$, which spans $\mathbb{C}e_t$, of real dimension two as $\lambda\overline{\mu}$ ranges over $\mathbb{C}$; on the vector subspace the value is $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}e_t$, and $K=-(\vec Q_1,\overline{\vec Q_2})$ likewise ranges over $\mathbb{C}$, so the span is again the centre, of real dimension two. On each of the four four-dimensional subspaces the values span a space of real dimension four, read from pairs that lie in the subspace itself: $e_t\star e_t=e_t$ and $e_t\star \vec e_k=-\vec e_k$ span $\mathbb{H}_{\mathbb{B}}$, the image of the real quaternion subspace; $e_t\star e_t=e_t$ and $e_t\star i\vec e_k=i\vec e_k$ span $\mathbb{M}_{+}$, the image of the Hermitian subspace; and $ie_t\star ie_t=e_t$, $ie_t\star i\vec e_k=-\vec e_k$ span $\mathbb{H}_{\mathbb{B}}$ for the anti-quaternion subspace, while $ie_t\star ie_t=e_t$, $ie_t\star \vec e_k=-i\vec e_k$ span $\mathbb{M}_{+}$ for the anti-Hermitian one.

**Remark (the image is not among the remarkable subspaces).** The values of a general pair lie in no subspace of the remarkable subspaces, and their span is the whole algebra; this is the content of the first theorem, and it is the reason the block's image is not one of the remarkable subspaces — unlike the image of the sibling sesquilinear symmetrisation $\mathrm{SPS}$, which is the centre. The corresponding statement for the general quaternionic sesquilinear row is in *Remarkable Subspaces under the General Quaternionic Sesqualgebra*.

## Worked Examples

**A central product.** $(2e_t)\star(3ie_t)=2\,\overline{3i}\,e_t=-6ie_t$; the conjugate of the second coefficient in the product formula is visible.

**A vector product.** $\vec e_x\star \vec e_y=0$: $K(\vec e_x,\vec e_y)=0$ and both scalar coefficients vanish.

**A vector square.** $\vec e_x\star \vec e_x=-e_t$: the value is the form value times the identity.

**A real quaternion product.** $(e_t+\vec e_x)\star(e_t+\vec e_x)=-2\vec e_x$: the product is real, and it is not central, so the real quaternion subspace is closed but not central.

**A Hermitian product.** $(e_t+i\vec e_x)\star(e_t+i\vec e_x)$: $K=1-1=0$ and the mixed term, computed from the displayed formula with $a_t=1,\vec\alpha=\vec e_x$ and $b_t=1,\vec\beta=\vec e_x$, is $i(\vec e_x-\vec e_x)=0$; the square is zero, an element of the isotropic cone.

**An anti-Hermitian product.** $(ie_t+\vec e_x)\star(ie_t+\vec e_y)=e_t+i(\vec e_x-\vec e_y)$: the scalar coefficient $a_t=b_t=1$ and the vector parts $\vec\alpha=\vec e_x$, $\vec\beta=\vec e_y$ give $K=1$ and the imaginary vector $i(\vec e_x-\vec e_y)$, an element of the Hermitian subspace; the diagonal case $\tilde Q=ie_t+\vec e_x$ has square $\langle\tilde Q,\tilde Q\rangle_{\natural*}e_t+i(1\cdot \vec e_x-1\cdot \vec e_x)=0$, an isotropic element.

## Summary

The product of the block is read on the remarkable subspaces by the single rule $\tilde Q_1\star\tilde Q_2=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}e_t-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1$. The centre is closed, with $(\lambda e_t)\star(\mu e_t)=\lambda\overline{\mu}\,e_t$; the vector subspace is not closed and maps into the centre, of real rank two; the real quaternion subspace is closed and commutative, of real rank four; the anti-quaternion subspace is not closed and maps onto the real quaternion subspace; the Hermitian subspace is closed, of real rank four; and the anti-Hermitian subspace is not closed and maps onto the Hermitian subspace. Three subspaces are closed — the centre, the real quaternion subspace and the Hermitian subspace — and three are not, with images one level down. The values of a general pair are not confined to a subspace of the remarkable subspaces: their smallest real span is the whole algebra, of real dimension eight, with the scalar part in the centre and the vector part in the vector subspace.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$ | the centre; closed, image rank $2$ |
| $\mathbf{e}$ | the vector subspace; image the centre, rank $2$ |
| $\mathbb{H}_{\mathbb{B}}$ | the real quaternion subspace; closed, image rank $4$ |
| $i\mathbb{H}_{\mathbb{B}}$ | the anti-quaternion subspace; image $\mathbb{H}_{\mathbb{B}}$, rank $4$ |
| $\mathbb{M}_{+}$ | the Hermitian subspace; closed, image rank $4$ |
| $\mathbb{M}_{-}$ | the anti-Hermitian subspace; image $\mathbb{M}_{+}$, rank $4$ |
| $\mathrm{span}_{\mathbb{R}}\{\tilde Q_1\star\tilde Q_2:\tilde Q_1,\tilde Q_2\in\mathbb{B}\}=\mathbb{B}$ | the smallest real span, of the values of all pairs, of real dimension eight |

## Further Reading

- [Introduction to the Symmetric Quaternionic Sesqualgebra](introduction-to-the-symmetric-quaternionic-sesqualgebra.html), for the product and its scalar–vector form.
- [The Non-Central Algebraic Norm and the Two Halves of the Symmetric Quaternionic Sesqualgebra](the-non-central-algebraic-norm-and-the-two-halves-of-the-symmetric-quaternionic-sesqualgebra.html), for the diagonal, the idempotents and the square-zero elements on the closed subspaces.
- [The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra](the-krein-form-as-a-product-on-the-symmetric-quaternionic-sesqualgebra.html), for the form and its restriction to the remarkable subspaces.
- [The Krein Gram Matrix and the Restrictions of the Form](the-krein-gram-matrix-and-the-restrictions-of-the-form.html), for the form $K$ and its Gram matrices.
- [Introduction to the Remarkable Subspaces](introduction-to-the-remarkable-subspaces.html), for the definition and the comparison of the remarkable subspaces.
- [Remarkable Subspaces under the General Quaternionic Sesqualgebra](remarkable-subspaces-under-the-general-quaternionic-sesqualgebra.html), for the same remarkable subspaces under the general product.
- [The 12 Products of the Biquaternion Complex Space](the-12-products-of-the-biquaternion-complex-space.html), for the comparison of the closure patterns of the twelve operations.
