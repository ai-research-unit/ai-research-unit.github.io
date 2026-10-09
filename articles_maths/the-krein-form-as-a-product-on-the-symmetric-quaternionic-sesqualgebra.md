# __The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra__

## Introduction

The scalar part of the symmetric quaternionic sesquilinear product is a form in its own right, and this article reads it as the multiplication of the block. The scalar part of

$$
\tilde P\star\tilde Q=\bigl[P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})\bigr]-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}
$$

is

$$
K(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\star\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})
=P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})
=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu},
$$

the **Krein form** of the corpus, and the vector part of the block is the mixed term alone. So the block is the form $K$ enlarged by one vector term: the map $\tilde Q\mapsto\tilde Q\star\tilde Q$ has real scalar part $K(\tilde Q,\tilde Q)$ and vector part $-2\mathrm{Re}(Q_0\overline{\mathbf{Q}})$, and the block is a product whose *values* carry $K$ as their scalar part and whose *scalar part* is $K$. That is the sense in which the form is a product: the form is the scalar component of a multiplication, and the multiplication is the smallest symmetric sesquilinear product whose scalar component is $K$.

The form $K$ itself, its Gram matrices, its restrictions and its cone are *The Krein Gram Matrix and the Restrictions of the Form* and *The Isotropic Structure of the General Quaternionic Sesqualgebra*; the four pairings of the algebra are *The Four Pairings of the Biquaternion Algebra*; the indefinite positivity of the algebra is *Indefinite Positivity and the Krein Cone of the Biquaternion Algebra*; the six subspaces are *The Six Subspaces under the General Quaternionic Sesqualgebra of Biquaternions*; the comparison of the four forms of the row is *Comparison Between the Four General Products*; and the product whose scalar part is read here is *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions*. The invariance that does hold, the adjoint relation of the block, is used in *The Multiplication Operators of the Symmetric Quaternionic Sesqualgebra*.

**Conventions.** $\tilde Q=\sum_\mu Q_\mu e_\mu$; $\varepsilon=(1,-1,-1,-1)$; $K(\tilde P,\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ is $\mathbb{C}$-linear in the first argument and $\bar{\cdot}$-semilinear in the second. The real basis is $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$, and the coefficient basis is $e_0,e_1,e_2,e_3$ over $\mathbb{C}$.

## The Form and Its Two Gram Matrices

**Theorem (the form).** For all biquaternions,

$$
K(\tilde P,\tilde Q)=P_0\overline{Q_0}-\sum_{k=1}^{3}P_k\overline{Q_k},
$$

and $K$ is Hermitian: $K(\tilde P,\tilde Q)=\overline{K(\tilde Q,\tilde P)}$, with $K(\tilde Q,\tilde Q)=|Q_0|^{2}-\sum_k|Q_k|^{2}$ real.

*Proof.* The first display is the scalar part of the product, computed once. For the Hermitian property, conjugate $K(\tilde Q,\tilde P)=Q_0\overline{P_0}-\sum_kQ_k\overline{P_k}$ and use $\overline{Q_0\overline{P_0}}=P_0\overline{Q_0}$ and $\overline{Q_k\overline{P_k}}=P_k\overline{Q_k}$. The diagonal value is real because each term is the real square $|Q_\mu|^{2}$ with its sign. $\square$

**Theorem (the two Gram matrices).** In the coefficient basis the Gram matrix of $K$ is

$$
E=\mathrm{diag}(1,-1,-1,-1),
$$

In the real basis it is

$$
\mathrm{diag}(1,-1,-1,-1,1,-1,-1,-1),
$$

so $K$ has inertia $(1,3)$ as a Hermitian form over $\mathbb{C}$, and its real part is the real symmetric bilinear form of signature $(2,6)$; $K$ is non-degenerate with zero radical, of rank four over $\mathbb{C}$ and eight over $\mathbb{R}$.

*Proof.* On the coefficient basis, $K(e_\mu,e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$, so the Gram matrix is $E$. The real basis Gram matrix records the real part of $K$, the realification: $\mathrm{Re}\,K(e_\mu,e_\nu)=\mathrm{Re}\,K(ie_\mu,ie_\nu)=\varepsilon_\mu\delta_{\mu\nu}$ and $\mathrm{Re}\,K(e_\mu,ie_\nu)=0$, since $K(e_\mu,ie_\nu)=-i\varepsilon_\mu\delta_{\mu\nu}$ is purely imaginary; the matrix is block diagonal with two copies of $E$, hence the displayed diagonal. The inertia follows from the signs, the non-degeneracy from the nonzero determinant, and the rank from the number of nonzero entries. $\square$

**Remark.** The basis $e_0,e_1,e_2,e_3$ is a Gram-orthogonal basis of $K$ with the signs $+,-,-,-$, so the form is indefinite by one positive direction and three negative ones; on the realification the two copies of the complex direction give the real signature $(2,6)$. The form is non-degenerate, and its condition of invariance is used in *The Multiplication Operators of the Symmetric Quaternionic Sesqualgebra*.

## The Isotropic Elements

**Theorem (the isotropic cone).** The isotropic cone of $K$ is

$$
\{\tilde P:K(\tilde P,\tilde P)=0\}=\{\tilde P:|P_0|^{2}=\textstyle\sum_{k=1}^{3}|P_k|^{2}\},
$$

a real algebraic cone of real dimension seven through the origin, of real codimension one, meeting the real quaternion subspace $\mathbb{H}_{\mathbb{B}}$ in the real cone $\{p_0^{2}=p_1^{2}+p_2^{2}+p_3^{2}\}$ of real dimension three.

*Proof.* $K(\tilde P,\tilde P)=|P_0|^{2}-\sum_k|P_k|^{2}$, which vanishes exactly on the displayed set; the equation is one real equation on the eight real coordinates, so the real dimension is seven, and on the four real coordinates of the real quaternion subspace it is one real equation, of real dimension three. The cone is algebraic and homogeneous of degree two in the real coordinates. $\square$

**Worked examples.** $e_0+e_1$, $e_0+e_2$, $e_0+e_3$ are isotropic; $e_1+ie_2$ is not, since $K(e_1+ie_2,e_1+ie_2)=-1-1=-2$; and the square-zero elements of *The Non-Central Diagonal and the Two Halves of the Symmetric Quaternionic Sesqualgebra*, among them $e_0+i\boldsymbol\mu$ for real unit $\boldsymbol\mu$, are isotropic.

**Remark (isotropy is wider than square zero).** The isotropic set is exactly the set of elements whose square has zero scalar part; the square-zero set also asks for the vanishing of the vector part. So square zero is a condition on the element, isotropy a condition on its scalar part alone, and $e_0+e_1$ separates the two: it is isotropic, and its square is $-2e_1$.

## The Restriction to the Six Subspaces

**Theorem (the six restrictions).** The form $K$ restricts to the six distinguished real subspaces with the following signatures:

| Subspace | $K$ on the subspace | Rank over $\mathbb{R}$ | Signature |
|---|---|---|---|
| centre $\mathbb{C}e_0$ | $\lambda\overline{\mu}$ | $2$ | $(2,0)$ |
| vector $\mathbf{e}$ | $-(\mathbf{P},\overline{\mathbf{Q}})$ | $6$ | $(0,6)$ |
| quaternion $\mathbb{H}_{\mathbb{B}}$ | $p_0q_0-\sum_kp_kq_k$ | $4$ | $(1,3)$ |
| anti-quaternion $i\mathbb{H}_{\mathbb{B}}$ | $p_0q_0-\sum_kp_kq_k$ | $4$ | $(1,3)$ |
| Hermitian $\mathbb{M}_{+}$ | $p_0q_0-\sum_kp_kq_k$ | $4$ | $(1,3)$ |
| anti-Hermitian $\mathbb{M}_{-}$ | $p_0q_0-\sum_kp_kq_k$ | $4$ | $(1,3)$ |

*Proof.* On the centre, $K(\lambda e_0,\mu e_0)=\lambda\overline{\mu}$, positive of rank two over the real coordinates of $\lambda$. On the vector subspace, $P_0=Q_0=0$ leaves $-(\mathbf{P},\overline{\mathbf{Q}})$, negative definite of rank six over the real coordinates of $\mathbf{P}$. On the real quaternion subspace all coefficients are real, so $K$ is the real bilinear form $p_0q_0-\sum_kp_kq_k$ of signature $(1,3)$. On the anti-quaternion subspace $P_k=ip_k$ with $p_k$ real, so $K(\tilde P,\tilde Q)=p_0q_0-\sum_k(ip_k)\overline{(iq_k)}=p_0q_0-\sum_kp_kq_k$, the same form. On $\mathbb{M}_{+}$ the coefficients are $(p_0,ip_1,ip_2,ip_3)$, and $P_k\overline{Q_k}=(ip_k)\overline{(iq_k)}=(ip_k)(-iq_k)=p_kq_k$, so $K=p_0q_0-\sum_kp_kq_k$; on $\mathbb{M}_{-}$ the roles of the scalar and vector coefficients are exchanged and the same computation applies. $\square$

**Corollary (the form is negative on the vector directions and positive on the centre).** On the decomposition $\mathbb{B}=\mathbb{C}e_0\oplus\mathbf{e}$, the form $K$ is the direct sum of a positive rank-two piece on the centre and a negative rank-six piece on the vector subspace.

## The Invariance of $K$ under the Block

**Theorem (the invariance fails).** The form $K$ is not invariant under the block: there are biquaternions with

$$
K(\tilde A\star\tilde P,\tilde A\star\tilde Q)\neq K(\tilde P,\tilde Q).
$$

Explicitly,

$$
K(\tilde A\star\tilde P,\tilde A\star\tilde Q)
=\mathrm{Sc}\bigl(\mathrm{SPA}(\overline{\tilde P},\tilde A)\,\mathrm{SPA}(\tilde Q,\overline{\tilde A})\bigr),
$$

where $\mathrm{SPA}(\tilde X,\tilde Y)=\tfrac12(\tilde X\tilde Y+\tilde Y\tilde X)$ is the symmetric plain product, and the defect is this value minus $K(\tilde P,\tilde Q)$.

*Proof.* The two identities

$$
(\tilde A\star\tilde X)^{\natural}=\mathrm{SPA}(\overline{\tilde X},\tilde A),
\qquad
(\tilde A\star\tilde X)^{*}=\mathrm{SPA}(\tilde X,\overline{\tilde A})
$$

follow from the definition of the block and the two anti-automorphism properties of ${}^{\natural}$ and ${}^{*}$. Then $K(\tilde A\star\tilde P,\tilde A\star\tilde Q)=\mathrm{Sc}\bigl((\tilde A\star\tilde P)^{\natural}(\tilde A\star\tilde Q)^{*}\bigr)$, which is the displayed value. On the pair $\tilde A=\tilde P=e_0+e_1$, $\tilde Q=e_1$ one has $\tilde A\star\tilde P=-2e_1$ and $\tilde A\star\tilde Q=-e_0-e_1$, so $K(\tilde A\star\tilde P,\tilde A\star\tilde Q)=-2$ against $K(\tilde P,\tilde Q)=K(e_0+e_1,e_1)=-1$: the defect is $-1$ and the invariance fails. $\square$

**Theorem (the compatibility that does hold).** The block and the form are tied by the adjoint relation

$$
K(\tilde A\star\tilde X,\tilde Y)=\overline{K(\tilde X,\tilde A^{\natural}\star\tilde Y)}.
$$

*Proof.* Use the two identities of the previous theorem, $(\tilde A\star\tilde X)^{\natural}=\mathrm{SPA}(\overline{\tilde X},\tilde A)$ and $(\tilde A\star\tilde X)^{*}=\mathrm{SPA}(\tilde X,\overline{\tilde A})$, together with $\mathrm{Sc}(U)=\mathrm{Sc}(U^{\natural})$, the value of the natural conjugation on the two scalar products, and the cyclic invariance $\mathrm{Sc}(UV)=\mathrm{Sc}(VU)$. On the one hand

$$
K(\tilde A\star\tilde X,\tilde Y)=\mathrm{Sc}\bigl((\tilde A\star\tilde X)^{\natural}\tilde Y^{*}\bigr)=\tfrac12\,\mathrm{Sc}\bigl((\overline{\tilde X}\tilde A+\tilde A\overline{\tilde X})\tilde Y^{*}\bigr),
$$

and on the other, with the same identity read at the element $\tilde A^{\natural}$,

$$
K(\tilde A^{\natural}\star\tilde Y,\tilde X)=\mathrm{Sc}\bigl((\tilde A^{\natural}\star\tilde Y)^{\natural}\tilde X^{*}\bigr)=\tfrac12\,\mathrm{Sc}\bigl((\overline{\tilde Y}\tilde A^{\natural}+\tilde A^{\natural}\overline{\tilde Y})\tilde X^{*}\bigr).
$$

The two agree term by term: the natural conjugation sends $\overline{\tilde X}\tilde A\tilde Y^{*}$ to $\overline{\tilde Y}\tilde A^{\natural}\tilde X^{*}$ and $\tilde A\overline{\tilde X}\tilde Y^{*}$ to $\overline{\tilde Y}\tilde X^{*}\tilde A^{\natural}$, since $(\overline{\tilde X})^{\natural}=\tilde X^{*}$ and $(\tilde Y^{*})^{\natural}=\overline{\tilde Y}$, and the scalar part is invariant under it; the second pair is then carried one onto the other by the cyclic invariance. Hence $K(\tilde A\star\tilde X,\tilde Y)=K(\tilde A^{\natural}\star\tilde Y,\tilde X)=\overline{K(\tilde X,\tilde A^{\natural}\star\tilde Y)}$ by the Hermitian symmetry of $K$, which is the display. $\square$

**Remark.** The invariance fails, and the compatibility that holds is the adjoint relation rather than the multiplicativity. The distinction is the one of the whole block: the product is conjugate-linear in one slot, so its left multiplications do not preserve $K$ the way a group of linear maps does, and the form records the failure through the two identities of the adjoint theorem.

## The Two Hermitian Subspaces and the Comparison of the Four Forms

**Theorem (the Hermitian and anti-Hermitian restrictions).** On $\mathbb{M}_{+}$ and on $\mathbb{M}_{-}$ the form $K$ restricts to the same real bilinear form of signature $(1,3)$, and on each of them it is the Krein form of a real four-space with one positive and three negative directions.

*Proof.* The two restrictions were computed in the table of §*The Restriction to the Six Subspaces*: on both, the coefficients are real up to the factor $i$ and the form reads $p_0q_0-\sum_kp_kq_k$, of signature $(1,3)$. $\square$

**Theorem (the four scalar parts).** The four symmetric parts of the four general products have the scalar parts

$$
\mathrm{Sc}(\mathrm{SPA}(\tilde P,\tilde Q))=P_0Q_0-(\mathbf{P},\mathbf{Q}),
\qquad
\mathrm{Sc}(\mathrm{SQA}(\tilde P,\tilde Q))=P_0Q_0+(\mathbf{P},\mathbf{Q}),
$$

$$
\mathrm{Sc}(\mathrm{SPS}(\tilde P,\tilde Q))=P_0\overline{Q_0}+(\mathbf{P},\overline{\mathbf{Q}})=H(\tilde P,\tilde Q),
\qquad
\mathrm{Sc}(\mathrm{SQS}(\tilde P,\tilde Q))=P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})=K(\tilde P,\tilde Q).
$$

The first two are the two symmetric bilinear forms of the algebra and the last two the two Hermitian forms, $H$ and $K$, of opposite sign in the vector term; on the real quaternion subspace $K$ coincides with the first bilinear form and $H$ with the second.

*Proof.* The four scalar parts are the scalar parts of the four symmetric parts, written out product by product in *The Four General Products of the Biquaternion $\mathbb{C}$ Space* and collected in *The 12 Products of the Biquaternion Complex Space*. On a real element the bar is the identity, so $K$ reads $p_0q_0-(p,q)$, the first bilinear form, and $H$ reads $p_0q_0+(p,q)$, the second. $\square$

**Remark (the comparison).** The two bilinear forms differ by the sign of the vector term, and so do the two Hermitian forms; the passage from the bilinear pair to the Hermitian pair is the passage from a symmetric bilinear product to a symmetric sesquilinear one, and $K$ is the Hermitian form whose vector term carries the negative sign. The four forms and their comparison are *Comparison Between the Four General Products*; the two Hermitian forms are the two articles *The Hermitian Form as a Product on the Symmetric Plain Sesqualgebra* and the present one.

## Worked Examples

**A positive value.** $K(e_0,e_0)=1$.

**A negative value.** $K(e_1,e_1)=-1$; on the vector subspace the form is negative definite, so every nonzero vector direction has a negative square.

**Anisotropic and isotropic.** $K(e_0+e_1,e_0+e_1)=1-1=0$ is isotropic; $K(e_0+2e_1,e_0+2e_1)=1-4=-3$ is anisotropic.

**A complex isotropic element.** $\tilde P=e_0+ie_1$: $K=|1|^{2}-|i|^{2}=0$, isotropic; the element is also of square zero by the family of the diagonal article, since $|\mathbf{c}|^{2}=1=|\alpha|^{4}$.

**The defect computed.** $\tilde A=e_0$, $\tilde P=e_1$, $\tilde Q=e_2$: $\tilde A\star\tilde P=-e_1$ and $\tilde A\star\tilde Q=-e_2$, so $K(-e_1,-e_2)=K(e_1,e_2)=0$ and $K(\tilde P,\tilde Q)=K(e_1,e_2)=0$: the defect vanishes on this pair. On $\tilde A=\tilde P=e_0+e_1$, $\tilde Q=e_1$ the two values differ, and the defect is the difference of the two displays of the theorem.

## Summary

The scalar part of the block is the Krein form $K(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\star\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$, Hermitian, with $K(\tilde Q,\tilde Q)=|Q_0|^{2}-\sum_k|Q_k|^{2}$ real. Its Gram matrix is $E=\mathrm{diag}(1,-1,-1,-1)$ in the coefficient basis and $\mathrm{diag}(1,-1,-1,-1,1,-1,-1,-1)$ in the real basis; its inertia is $(1,3)$, its real signature $(2,6)$, its rank four over $\mathbb{C}$ and eight over $\mathbb{R}$, and its radical is zero. Its isotropic cone is $\{|P_0|^{2}=\sum_k|P_k|^{2}\}$, of real dimension seven and real codimension one, and on the six subspaces it restricts to $(2,0)$ on the centre, $(0,6)$ on the vector subspace, and $(1,3)$ on each of the four real four-dimensional subspaces. It is not invariant under the block; the defect is $\mathrm{Sc}(\mathrm{SPA}(\overline{\tilde P},\tilde A)\mathrm{SPA}(\tilde Q,\overline{\tilde A}))-K(\tilde P,\tilde Q)$, and the compatibility that holds is the adjoint relation $K(\tilde A\star\tilde X,\tilde Y)=\overline{K(\tilde X,\tilde A^{\natural}\star\tilde Y)}$. Of the four scalar parts of the row, $K$ and $H=P_0\overline{Q_0}+(\mathbf{P},\overline{\mathbf{Q}})$ are the two Hermitian forms, of opposite sign in the vector term, and they collapse onto the two bilinear forms on the real quaternion subspace.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K(\tilde P,\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ | the Krein form, the scalar part of the block |
| $E=\mathrm{diag}(1,-1,-1,-1)$ | the Gram matrix of $K$ in the coefficient basis |
| $(1,3)$; $(2,6)$ | the inertia over $\mathbb{C}$; the signature over $\mathbb{R}$ |
| $\{|P_0|^{2}=\sum_k|P_k|^{2}\}$ | the isotropic cone |
| $\mathrm{Sc}(\mathrm{SPA})=P_0Q_0-(\mathbf{P},\mathbf{Q})$ | the first symmetric bilinear scalar part |
| $\mathrm{Sc}(\mathrm{SQA})=P_0Q_0+(\mathbf{P},\mathbf{Q})$ | the second symmetric bilinear scalar part |
| $H(\tilde P,\tilde Q)=P_0\overline{Q_0}+(\mathbf{P},\overline{\mathbf{Q}})$ | the other Hermitian form, the scalar part of $\mathrm{SPS}$ |
| $K(\tilde A\star\tilde X,\tilde Y)=\overline{K(\tilde X,\tilde A^{\natural}\star\tilde Y)}$ | the adjoint relation, the compatibility that holds |

## Further Reading

- *The Krein Gram Matrix and the Restrictions of the Form* (`articles_maths/the-krein-gram-matrix-and-the-restrictions-of-the-form.md`), for the form $K$, its Gram matrix and its restrictions.
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the four pairings of which $K$ is one.
- *The Isotropic Structure of the General Quaternionic Sesqualgebra* (`articles_maths/the-isotropic-structure-of-the-general-quaternionic-sesqualgebra.md`), for the isotropic structure of the form.
- *Indefinite Positivity and the Krein Cone of the Biquaternion Algebra* (`articles_maths/indefinite-positivity-and-the-krein-cone-of-the-biquaternion-algebra.md`), for the indefinite positivity and the cone.
- *The Six Subspaces under the General Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/the-six-subspaces-under-the-general-quaternionic-sesqualgebra-of-biquaternions.md`), for the six subspaces and the restrictions of the forms.
- *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-sesqualgebra-of-biquaternions.md`), for the product whose scalar part is the form.
- *The Non-Central Diagonal and the Two Halves of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/the-non-central-diagonal-and-the-two-halves-of-the-symmetric-quaternionic-sesqualgebra.md`), for the square-zero family, which lies inside the isotropic cone.
- *Comparison Between the Four General Products* (`articles_maths/comparison-between-the-four-general-products.md`), for the four scalar parts and their comparison.
- *The Multiplication Operators of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-quaternionic-sesqualgebra.md`), for the adjoint relation in operator form.
