# __The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra__

## Introduction

The scalar part of the symmetric quaternionic sesquilinear product is a form in its own right, and this article reads it as the multiplication of the block. The scalar part of

$$
\tilde Q_1\star\tilde Q_2=\bigl[Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})\bigr]-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1
$$

is

$$
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\mathrm{Sc}(\tilde Q_1\star\tilde Q_2)=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*})
=Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})
=\sum_\mu\varepsilon_\mu Q_{1,\mu}\overline{Q_{2,\mu}},
$$

the **Krein form** of the corpus, and the vector part of the block is the mixed term alone. So the block is the form $\langle\cdot,\cdot\rangle_{\natural*}$ enlarged by one vector term: the map $\tilde Q_2\mapsto\tilde Q_2\star\tilde Q_2$ has real scalar part $\langle\tilde Q_2,\tilde Q_2\rangle_{\natural*}$ and vector part $-2\mathrm{Re}(Q_{2t}\overline{\vec Q_2})$, and the block is a product whose *values* carry $\langle\cdot,\cdot\rangle_{\natural*}$ as their scalar part and whose *scalar part* is $\langle\cdot,\cdot\rangle_{\natural*}$. That is the sense in which the form is a product: the form is the scalar component of a multiplication, and the multiplication is the smallest symmetric sesquilinear product whose scalar component is $\langle\cdot,\cdot\rangle_{\natural*}$.

The form $\langle\cdot,\cdot\rangle_{\natural*}$ itself, its Gram matrices, its restrictions and its cone are *The Krein Gram Matrix and the Restrictions of the Form* and *The Isotropic Structure of the General Quaternionic Sesqualgebra*; the four pairings of the algebra are *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*; the indefinite positivity of the algebra is *Indefinite Positivity and the Krein Cone of the Biquaternion Algebra*; the remarkable subspaces are *Remarkable Subspaces under the General Quaternionic Sesqualgebra*; the comparison of the four forms of the row is *Comparison Between the Four General Products*; and the product whose scalar part is read here is *Introduction to the Symmetric Quaternionic Sesqualgebra*. The invariance that does hold, the adjoint relation of the block, is used in *The Multiplication Operators of the Symmetric Quaternionic Sesqualgebra*.

## The Form and Its Two Gram Matrices

**Theorem (the form).** For all biquaternions,

$$ \boxed{\; \langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=Q_{1t}\overline{Q_{2t}}-\sum_{\mu\in\{x,y,z\}}Q_{1,\mu}\overline{Q_{2,\mu}} \;}, $$

and $\langle\cdot,\cdot\rangle_{\natural*}$ is Hermitian: $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\overline{\langle\tilde Q_2,\tilde Q_1\rangle_{\natural*}}$, with $\langle\tilde Q_2,\tilde Q_2\rangle_{\natural*}=|Q_{2t}|^{2}-\sum_k|Q_{2,k}|^{2}$ real.

*Proof.* The first display is the scalar part of the product, computed once. For the Hermitian property, conjugate $\langle\tilde Q_2,\tilde Q_1\rangle_{\natural*}=Q_{2t}\overline{Q_{1t}}-\sum_kQ_{2,k}\overline{Q_{1,k}}$ and use $\overline{Q_{2t}\overline{Q_{1t}}}=Q_{1t}\overline{Q_{2t}}$ and $\overline{Q_{2,k}\overline{Q_{1,k}}}=Q_{1,k}\overline{Q_{2,k}}$. The diagonal value is real because each term is the real square $|Q_{2,\mu}|^{2}$ with its sign.

**Theorem (the two Gram matrices).** In the coefficient basis the Gram matrix of $\langle\cdot,\cdot\rangle_{\natural*}$ is

$$ \boxed{\; E=\mathrm{diag}(1,-1,-1,-1) \;}, $$

In the real basis it is

$$
\mathrm{diag}(1,-1,-1,-1,1,-1,-1,-1),
$$

so $\langle\cdot,\cdot\rangle_{\natural*}$ has inertia $(1,3)$ as a Hermitian form over $\mathbb{C}$, and its real part is the real symmetric bilinear form of signature $(2,6)$; $\langle\cdot,\cdot\rangle_{\natural*}$ is non-degenerate with zero radical, of rank four over $\mathbb{C}$ and eight over $\mathbb{R}$.

*Proof.* On the coefficient basis, $\langle e_\mu,e_\nu\rangle_{\natural*}=\varepsilon_\mu\delta_{\mu\nu}$, so the Gram matrix is $E$. The real basis Gram matrix records the real part of $\langle\cdot,\cdot\rangle_{\natural*}$, the realification: $\mathrm{Re}\,\langle e_\mu,e_\nu\rangle_{\natural*}=\mathrm{Re}\,\langle ie_\mu,ie_\nu\rangle_{\natural*}=\varepsilon_\mu\delta_{\mu\nu}$ and $\mathrm{Re}\,\langle e_\mu,ie_\nu\rangle_{\natural*}=0$, since $\langle e_\mu,ie_\nu\rangle_{\natural*}=-i\varepsilon_\mu\delta_{\mu\nu}$ is purely imaginary; the matrix is block diagonal with two copies of $E$, hence the displayed diagonal. The inertia follows from the signs, the non-degeneracy from the nonzero determinant, and the rank from the number of nonzero entries.

**Remark.** The basis $e_t,\vec e_x,\vec e_y,\vec e_z$ is a Gram-orthogonal basis of $\langle\cdot,\cdot\rangle_{\natural*}$ with the signs $+,-,-,-$, so the form is indefinite by one positive direction and three negative ones; on the realification the two copies of the complex direction give the real signature $(2,6)$. The form is non-degenerate, and its condition of invariance is used in *The Multiplication Operators of the Symmetric Quaternionic Sesqualgebra*.

## The Isotropic Elements

**Theorem (the isotropic cone).** The isotropic cone of $\langle\cdot,\cdot\rangle_{\natural*}$ is

$$
\{\tilde Q_1:\langle\tilde Q_1,\tilde Q_1\rangle_{\natural*}=0\}=\{\tilde Q_1:|Q_{1t}|^{2}=\textstyle\sum_{\mu\in\{x,y,z\}}|Q_{1,\mu}|^{2}\},
$$

a real algebraic cone of real dimension seven through the origin, of real codimension one, meeting the real quaternion subspace $\mathbb{H}_{\mathbb{B}}$ in the real cone $\{p_t^{2}=p_x^{2}+p_y^{2}+p_z^{2}\}$ of real dimension three.

*Proof.* $\langle\tilde Q_1,\tilde Q_1\rangle_{\natural*}=|Q_{1t}|^{2}-\sum_k|Q_{1,k}|^{2}$, which vanishes exactly on the displayed set; the equation is one real equation on the eight real coordinates, so the real dimension is seven, and on the four real coordinates of the real quaternion subspace it is one real equation, of real dimension three. The cone is algebraic and homogeneous of degree two in the real coordinates.

**Worked examples.** $e_t+\vec e_x$, $e_t+\vec e_y$, $e_t+\vec e_z$ are isotropic; $\vec e_x+i\vec e_y$ is not, since $\langle \vec e_x+i\vec e_y,\vec e_x+i\vec e_y\rangle_{\natural*}=-1-1=-2$; and the square-zero elements of *The Non-Central Algebraic Norm and the Two Halves of the Symmetric Quaternionic Sesqualgebra*, among them $e_t+i\vec u$ for real unit $\vec u$, are isotropic.

**Remark (isotropy is wider than square zero).** The isotropic set is exactly the set of elements whose square has zero scalar part; the square-zero set also asks for the vanishing of the vector part. So square zero is a condition on the element, isotropy a condition on its scalar part alone, and $e_t+\vec e_x$ separates the two: it is isotropic, and its square is $-2\vec e_x$.

## The Restriction to the Remarkable Subspaces

**Theorem (the restrictions).** The form $\langle\cdot,\cdot\rangle_{\natural*}$ restricts to the remarkable real subspaces with the following signatures:

| Subspace | $\langle\cdot,\cdot\rangle_{\natural*}$ on the subspace | Rank over $\mathbb{R}$ | Signature |
|---|---|---|---|
| centre $\mathbb{C}e_t$ | $\lambda\overline{\mu}$ | $2$ | $(2,0)$ |
| vector $\mathbf{e}$ | $-(\vec Q_1,\overline{\vec Q_2})$ | $6$ | $(0,6)$ |
| quaternion $\mathbb{H}_{\mathbb{B}}$ | $p_tq_t-\sum_kp_kq_k$ | $4$ | $(1,3)$ |
| anti-quaternion $i\mathbb{H}_{\mathbb{B}}$ | $p_tq_t-\sum_kp_kq_k$ | $4$ | $(1,3)$ |
| Hermitian $\mathbb{M}_{+}$ | $p_tq_t-\sum_kp_kq_k$ | $4$ | $(1,3)$ |
| anti-Hermitian $\mathbb{M}_{-}$ | $p_tq_t-\sum_kp_kq_k$ | $4$ | $(1,3)$ |

*Proof.* On the centre, $\langle \lambda e_t,\mu e_t\rangle_{\natural*}=\lambda\overline{\mu}$, positive of rank two over the real coordinates of $\lambda$. On the vector subspace, $Q_{1t}=Q_{2t}=0$ leaves $-(\vec Q_1,\overline{\vec Q_2})$, negative definite of rank six over the real coordinates of $\vec Q_1$. On the real quaternion subspace all coefficients are real, so $\langle\cdot,\cdot\rangle_{\natural*}$ is the real bilinear form $p_tq_t-\sum_kp_kq_k$ of signature $(1,3)$. On the anti-quaternion subspace $Q_{1,k}=ip_k$ with $p_k$ real, so $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=p_tq_t-\sum_k(ip_k)\overline{(iq_k)}=p_tq_t-\sum_kp_kq_k$, the same form. On $\mathbb{M}_{+}$ the coefficients are $(p_t,ip_x,ip_y,ip_z)$, and $Q_{1,k}\overline{Q_{2,k}}=(ip_k)\overline{(iq_k)}=(ip_k)(-iq_k)=p_kq_k$, so $\langle\cdot,\cdot\rangle_{\natural*}=p_tq_t-\sum_kp_kq_k$; on $\mathbb{M}_{-}$ the roles of the scalar and vector coefficients are exchanged and the same computation applies.

**Corollary (the form is negative on the vector directions and positive on the centre).** On the decomposition $\mathbb{B}=\mathbb{C}e_t\oplus\mathbf{e}$, the form $\langle\cdot,\cdot\rangle_{\natural*}$ is the direct sum of a positive rank-two piece on the centre and a negative rank-six piece on the vector subspace.

## The Invariance of $\langle\cdot,\cdot\rangle_{\natural*}$ under the Block

**Theorem (the invariance fails).** The form $\langle\cdot,\cdot\rangle_{\natural*}$ is not invariant under the block: there are biquaternions with

$$
\langle\tilde Q_3\star\tilde Q_1,\tilde Q_3\star\tilde Q_2\rangle_{\natural*}\neq \langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}.
$$

Explicitly,

$$
\langle\tilde Q_3\star\tilde Q_1,\tilde Q_3\star\tilde Q_2\rangle_{\natural*}
=\mathrm{Sc}\bigl(\mathrm{SPA}(\overline{\tilde Q_1},\tilde Q_3)\,\mathrm{SPA}(\tilde Q_2,\overline{\tilde Q_3})\bigr),
$$

where $\mathrm{SPA}(\tilde Q_1,\tilde Q_2)=\tfrac12(\tilde Q_1\tilde Q_2+\tilde Q_2\tilde Q_1)$ is the symmetric plain product, and the defect is this value minus $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}$.

*Proof.* The two identities

$$
(\tilde Q_3\star\tilde Q_1)^{\natural}=\mathrm{SPA}(\overline{\tilde Q_1},\tilde Q_3),
\qquad
(\tilde Q_3\star\tilde Q_1)^{*}=\mathrm{SPA}(\tilde Q_1,\overline{\tilde Q_3})
$$

follow from the definition of the block and the two anti-automorphism properties of ${}^{\natural}$ and ${}^{*}$. Then $\langle\tilde Q_3\star\tilde Q_1,\tilde Q_3\star\tilde Q_2\rangle_{\natural*}=\mathrm{Sc}\bigl((\tilde Q_3\star\tilde Q_1)^{\natural}(\tilde Q_3\star\tilde Q_2)^{*}\bigr)$, which is the displayed value. On the pair $\tilde Q_3=\tilde Q_1=e_t+\vec e_x$, $\tilde Q_2=\vec e_x$ one has $\tilde Q_3\star\tilde Q_1=-2\vec e_x$ and $\tilde Q_3\star\tilde Q_2=-e_t-\vec e_x$, so $\langle\tilde Q_3\star\tilde Q_1,\tilde Q_3\star\tilde Q_2\rangle_{\natural*}=-2$ against $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\langle e_t+\vec e_x,\vec e_x\rangle_{\natural*}=-1$: the defect is $-1$ and the invariance fails.

**Theorem (the compatibility that does hold).** The block and the form are tied by the adjoint relation

$$ \boxed{\; \langle\tilde Q_3\star\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\overline{\langle\tilde Q_1,\tilde Q_3^{\natural}\star\tilde Q_2\rangle_{\natural*}} \;}. $$

*Proof.* Use the two identities of the previous theorem, $(\tilde Q_3\star\tilde Q_1)^{\natural}=\mathrm{SPA}(\overline{\tilde Q_1},\tilde Q_3)$ and $(\tilde Q_3\star\tilde Q_1)^{*}=\mathrm{SPA}(\tilde Q_1,\overline{\tilde Q_3})$, together with $\mathrm{Sc}(U)=\mathrm{Sc}(U^{\natural})$, the value of the natural conjugation on the two scalar products, and the cyclic invariance $\mathrm{Sc}(UV)=\mathrm{Sc}(VU)$. On the one hand

$$
\langle\tilde Q_3\star\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\mathrm{Sc}\bigl((\tilde Q_3\star\tilde Q_1)^{\natural}\tilde Q_2^{*}\bigr)=\tfrac12\,\mathrm{Sc}\bigl((\overline{\tilde Q_1}\tilde Q_3+\tilde Q_3\overline{\tilde Q_1})\tilde Q_2^{*}\bigr),
$$

and on the other, with the same identity read at the element $\tilde Q_3^{\natural}$,

$$
\langle\tilde Q_3^{\natural}\star\tilde Q_2,\tilde Q_1\rangle_{\natural*}=\mathrm{Sc}\bigl((\tilde Q_3^{\natural}\star\tilde Q_2)^{\natural}\tilde Q_1^{*}\bigr)=\tfrac12\,\mathrm{Sc}\bigl((\overline{\tilde Q_2}\tilde Q_3^{\natural}+\tilde Q_3^{\natural}\overline{\tilde Q_2})\tilde Q_1^{*}\bigr).
$$

The two agree term by term: the natural conjugation sends $\overline{\tilde Q_1}\tilde Q_3\tilde Q_2^{*}$ to $\overline{\tilde Q_2}\tilde Q_3^{\natural}\tilde Q_1^{*}$ and $\tilde Q_3\overline{\tilde Q_1}\tilde Q_2^{*}$ to $\overline{\tilde Q_2}\tilde Q_1^{*}\tilde Q_3^{\natural}$, since $(\overline{\tilde Q_1})^{\natural}=\tilde Q_1^{*}$ and $(\tilde Q_2^{*})^{\natural}=\overline{\tilde Q_2}$, and the scalar part is invariant under it; the second pair is then carried one onto the other by the cyclic invariance. Hence $\langle\tilde Q_3\star\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\langle\tilde Q_3^{\natural}\star\tilde Q_2,\tilde Q_1\rangle_{\natural*}=\overline{\langle\tilde Q_1,\tilde Q_3^{\natural}\star\tilde Q_2\rangle_{\natural*}}$ by the Hermitian symmetry of $\langle\cdot,\cdot\rangle_{\natural*}$, which is the display.

**Remark.** The invariance fails, and the compatibility that holds is the adjoint relation rather than the multiplicativity. The distinction is the one of the whole block: the product is conjugate-linear in one slot, so its left multiplications do not preserve $\langle\cdot,\cdot\rangle_{\natural*}$ the way a group of linear maps does, and the form records the failure through the two identities of the adjoint theorem.

## The Two Hermitian Subspaces and the Comparison of the Four Forms

**Theorem (the Hermitian and anti-Hermitian restrictions).** On $\mathbb{M}_{+}$ and on $\mathbb{M}_{-}$ the form $\langle\cdot,\cdot\rangle_{\natural*}$ restricts to the same real bilinear form of signature $(1,3)$, and on each of them it is the Krein form of a real four-space with one positive and three negative directions.

*Proof.* The two restrictions were computed in the table of §*The Restriction to the Remarkable Subspaces*: on both, the coefficients are real up to the factor $i$ and the form reads $p_tq_t-\sum_kp_kq_k$, of signature $(1,3)$.

**Theorem (the four scalar parts).** The four symmetric parts of the four general products have the scalar parts

$$
\mathrm{Sc}(\mathrm{SPA}(\tilde Q_1,\tilde Q_2))=Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2),
\qquad
\mathrm{Sc}(\mathrm{SQA}(\tilde Q_1,\tilde Q_2))=Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2),
$$

$$
\mathrm{Sc}(\mathrm{SPS}(\tilde Q_1,\tilde Q_2))=Q_{1t}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2})=\langle\tilde Q_1,\tilde Q_2\rangle_{*},
\qquad
\mathrm{Sc}(\mathrm{SQS}(\tilde Q_1,\tilde Q_2))=Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}.
$$

The first two are the two symmetric bilinear forms of the algebra and the last two the two Hermitian forms, $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\natural*}$, of opposite sign in the vector term; on the real quaternion subspace $\langle\cdot,\cdot\rangle_{\natural*}$ coincides with the first bilinear form and $\langle\cdot,\cdot\rangle_{*}$ with the second.

*Proof.* The four scalar parts are the scalar parts of the four symmetric parts, written out product by product in *The Four General Products of the Biquaternion $\mathbb{C}$ Space* and collected in *The 12 Products of the Biquaternion Complex Space*. On a real element the bar is the identity, so $\langle\cdot,\cdot\rangle_{\natural*}$ reads $p_tq_t-(p,q)$, the first bilinear form, and $\langle\cdot,\cdot\rangle_{*}$ reads $p_tq_t+(p,q)$, the second.

**Remark (the comparison).** The two bilinear forms differ by the sign of the vector term, and so do the two Hermitian forms; the passage from the bilinear pair to the Hermitian pair is the passage from a symmetric bilinear product to a symmetric sesquilinear one, and $\langle\cdot,\cdot\rangle_{\natural*}$ is the Hermitian form whose vector term carries the negative sign. The four forms and their comparison are *Comparison Between the Four General Products*; the two Hermitian forms are the two articles *The Hermitian Form as a Product on the Symmetric Plain Sesqualgebra* and the present one.

## Worked Examples

**A positive value.** $\langle e_t,e_t\rangle_{\natural*}=1$.

**A negative value.** $\langle \vec e_x,\vec e_x\rangle_{\natural*}=-1$; on the vector subspace the form is negative definite, so every nonzero vector direction has a negative square.

**Anisotropic and isotropic.** $\langle e_t+\vec e_x,e_t+\vec e_x\rangle_{\natural*}=1-1=0$ is isotropic; $\langle e_t+2\vec e_x,e_t+2\vec e_x\rangle_{\natural*}=1-4=-3$ is anisotropic.

**A complex isotropic element.** $\tilde Q_1=e_t+i\vec e_x$: $\langle\cdot,\cdot\rangle_{\natural*}=|1|^{2}-|i|^{2}=0$, isotropic; the element is also of square zero by the family of the diagonal article, since $|\vec c|^{2}=1=|\alpha|^{4}$.

**The defect computed.** $\tilde Q_3=e_t$, $\tilde Q_1=\vec e_x$, $\tilde Q_2=\vec e_y$: $\tilde Q_3\star\tilde Q_1=-\vec e_x$ and $\tilde Q_3\star\tilde Q_2=-\vec e_y$, so $\langle -\vec e_x,-\vec e_y\rangle_{\natural*}=\langle \vec e_x,\vec e_y\rangle_{\natural*}=0$ and $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\langle \vec e_x,\vec e_y\rangle_{\natural*}=0$: the defect vanishes on this pair. On $\tilde Q_3=\tilde Q_1=e_t+\vec e_x$, $\tilde Q_2=\vec e_x$ the two values differ, and the defect is the difference of the two displays of the theorem.

## Summary

is the Krein form $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\mathrm{Sc}(\tilde Q_1\star\tilde Q_2)=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*})=Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})=\sum_\mu\varepsilon_\mu Q_{1,\mu}\overline{Q_{2,\mu}}$, Hermitian, with $\langle\tilde Q_2,\tilde Q_2\rangle_{\natural*}=|Q_{2t}|^{2}-\sum_k|Q_{2,k}|^{2}$ real. Its Gram matrix is $E=\mathrm{diag}(1,-1,-1,-1)$ in the coefficient basis and $\mathrm{diag}(1,-1,-1,-1,1,-1,-1,-1)$ in the real basis; its inertia is $(1,3)$, its real signature $(2,6)$, its rank four over $\mathbb{C}$ and eight over $\mathbb{R}$, and its radical is zero. Its isotropic cone is $\{|Q_{1t}|^{2}=\sum_k|Q_{1,k}|^{2}\}$, of real dimension seven and real codimension one, and on the remarkable subspaces it restricts to $(2,0)$ on the centre, $(0,6)$ on the vector subspace, and $(1,3)$ on each of the four real four-dimensional subspaces. It is not invariant under the block; the defect is $\mathrm{Sc}(\mathrm{SPA}(\overline{\tilde Q_1},\tilde Q_3)\mathrm{SPA}(\tilde Q_2,\overline{\tilde Q_3}))-\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}$, and the compatibility that holds is the adjoint relation $\langle\tilde Q_3\star\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\overline{\langle\tilde Q_1,\tilde Q_3^{\natural}\star\tilde Q_2\rangle_{\natural*}}$. Of the four scalar parts of the row, $\langle\cdot,\cdot\rangle_{\natural*}$ and $\langle\cdot,\cdot\rangle_{*}=Q_{1t}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2})$ are the two Hermitian forms, of opposite sign in the vector term, and they collapse onto the two bilinear forms on the real quaternion subspace.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\sum_\mu\varepsilon_\mu Q_{1,\mu}\overline{Q_{2,\mu}}$ | the Krein form, the scalar part of the block |
| $E=\mathrm{diag}(1,-1,-1,-1)$ | the Gram matrix of $\langle\cdot,\cdot\rangle_{\natural*}$ in the coefficient basis |
| $(1,3)$; $(2,6)$ | the inertia over $\mathbb{C}$; the signature over $\mathbb{R}$ |
| $\{\lvert Q_{1t}\rvert^{2}=\sum_k\lvert Q_{1,k}\rvert^{2}\}$ | the isotropic cone |
| $\mathrm{Sc}(\mathrm{SPA})=Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2)$ | the first symmetric bilinear scalar part |
| $\mathrm{Sc}(\mathrm{SQA})=Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2)$ | the second symmetric bilinear scalar part |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=Q_{1t}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2})$ | the other Hermitian form, the scalar part of $\mathrm{SPS}$ |
| $\langle\tilde Q_3\star\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\overline{\langle\tilde Q_1,\tilde Q_3^{\natural}\star\tilde Q_2\rangle_{\natural*}}$ | the adjoint relation, the compatibility that holds |

## Further Reading

- [The Krein Gram Matrix and the Restrictions of the Form](the-krein-gram-matrix-and-the-restrictions-of-the-form.html), for the form $\langle\cdot,\cdot\rangle_{\natural*}$, its Gram matrix and its restrictions.
- [The 4 Forms over the Biquaternion $\mathbb{C}$ Space](the-4-forms-over-the-biquaternion-c-space.html), for the four pairings of which $\langle\cdot,\cdot\rangle_{\natural*}$ is one.
- [The Isotropic Structure of the General Quaternionic Sesqualgebra](the-isotropic-structure-of-the-general-quaternionic-sesqualgebra.html), for the isotropic structure of the form.
- [Indefinite Positivity and the Krein Cone of the Biquaternion Algebra](indefinite-positivity-and-the-krein-cone-of-the-biquaternion-algebra.html), for the indefinite positivity and the cone.
- [Remarkable Subspaces under the General Quaternionic Sesqualgebra](remarkable-subspaces-under-the-general-quaternionic-sesqualgebra.html), for the remarkable subspaces and the restrictions of the forms.
- [Introduction to the Symmetric Quaternionic Sesqualgebra](introduction-to-the-symmetric-quaternionic-sesqualgebra.html), for the product whose scalar part is the form.
- [The Non-Central Algebraic Norm and the Two Halves of the Symmetric Quaternionic Sesqualgebra](the-non-central-algebraic-norm-and-the-two-halves-of-the-symmetric-quaternionic-sesqualgebra.html), for the square-zero family, which lies inside the isotropic cone.
- [Comparison Between the Four General Products](comparison-between-the-four-general-products.html), for the four scalar parts and their comparison.
- [The Multiplication Operators of the Symmetric Quaternionic Sesqualgebra](the-multiplication-operators-of-the-symmetric-quaternionic-sesqualgebra.html), for the adjoint relation in operator form.
