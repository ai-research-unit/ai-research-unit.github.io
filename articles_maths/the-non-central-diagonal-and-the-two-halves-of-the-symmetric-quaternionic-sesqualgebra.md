# __The Non-Central Diagonal and the Two Halves of the Symmetric Quaternionic Sesqualgebra__

## Introduction

The symmetric quaternionic sesquilinear product of *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions* is the multiplication of this block, and its diagonal $\tilde Q\star\tilde Q$ is the object that tells the block apart from its companions. Two of the four symmetric parts have central diagonals: the quaternionic bilinear one, $\tilde Q^{\natural}\tilde Q=N(\tilde Q)e_0$, and the plain sesquilinear one, whose diagonal is the positive Hermitian form $(|Q_0|^{2}+\sum_k|Q_k|^{2})$ times $e_0$. The plain square is already non-central in general, $(e_0+e_1)^{2}=2e_1$, and the block's diagonal is non-central too, but with its own shape: it carries a complex scalar part and a vector part side by side, and at $e_0+e_1$ it is $-2e_1$, an element of the vector subspace. The reason is structural: the product is the half-sum of the two orders $\tilde P^{\natural}\tilde Q^{*}$ and $\tilde Q^{*}\tilde P^{\natural}$, and on the diagonal the two orders are the same product read twice, whose scalar parts agree and whose vector parts carry the cross product with opposite signs. The half-sum therefore keeps the scalar part and the *mixed* vector part and loses the cross product, and the mixed vector part does not vanish.

This article reads the diagonal as an element and not as a number. Its scalar part is the Krein form $K(\tilde Q,\tilde Q)$, its vector part is $-Q_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{Q}$, and its vanishing is the criterion of centrality. The article then reads the two halves of the diagonal, the two orders $\tilde Q^{\natural}\tilde Q^{*}$ and $\tilde Q^{*}\tilde Q^{\natural}$, whose sum is twice the diagonal and whose difference is twice the antisymmetric companion; it reads the elements of square zero and the idempotents, both families in full; and it reads the absence of a unit and the two one-sided actions that the diagonal carries. The reconstruction of the general quaternionic sesquilinear product from its two halves is the introduction's and is not repeated here.

The product itself is *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions*; the general quaternionic sesquilinear product and its square are *Introduction to the General Quaternionic Sesqualgebra of Biquaternions*; the antisymmetric companion is Block 8 of the batch and is defined in *The 12 Products of the Biquaternion Complex Space*; the form $K$ is *The Krein Gram Matrix and the Restrictions of the Form*; the isotropic elements of the form are *The Isotropic Structure of the General Quaternionic Sesqualgebra*; the zero divisors of the algebra are *Biquaternion Zero Divisors*; and the norm is *Biquaternion Norm and Invertibility*.

**Conventions.** As in the introduction of the block: $\tilde Q=\sum_\mu Q_\mu e_\mu$, $K(\tilde P,\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$, $\mathbf{Q}=\sum_kQ_ke_k$, and $\tilde Q\star\tilde Q=K(\tilde Q,\tilde Q)e_0-Q_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{Q}$.

## The Diagonal as an Element

**Theorem (the diagonal).** For every biquaternion,

$$
\tilde Q\star\tilde Q=K(\tilde Q,\tilde Q)e_0-Q_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{Q},
\qquad
K(\tilde Q,\tilde Q)=|Q_0|^{2}-\sum_{k=1}^{3}|Q_k|^{2}.
$$

The scalar part is real and the vector part is $-2\mathrm{Re}(Q_0\overline{\mathbf{Q}})=-2\sum_{k=1}^{3}\mathrm{Re}(Q_0\overline{Q_k})e_k$, a real vector.

*Proof.* Put $\tilde P=\tilde Q$ in the scalar–vector form of *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions*: the scalar part becomes $Q_0\overline{Q_0}-(\mathbf{Q},\overline{\mathbf{Q}})=|Q_0|^{2}-\sum_k|Q_k|^{2}$, a real number, and the vector part becomes $-Q_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{Q}=-2\mathrm{Re}(Q_0\overline{\mathbf{Q}})$, a real vector. $\square$

**Remark (the diagonal is a real element).** Both the scalar and the vector part of the diagonal are real, so the diagonal always lies in the real quaternion subspace $\mathbb{H}_{\mathbb{B}}$, whatever element one starts from. A general element of the block has two complex components in each slot, but its square has only real ones. The reason is the conjugate-commutativity: the diagonal is its own conjugate, $\tilde Q\star\tilde Q=\overline{\tilde Q\star\tilde Q}$, and the fixed elements of the coefficientwise conjugation are exactly the real quaternions.

## The Criterion of Centrality

**Theorem (centrality of the diagonal).** $\tilde Q\star\tilde Q$ lies in the centre exactly when

$$
Q_0\overline{Q_k}\in i\mathbb{R}\quad\text{for every }k=1,2,3,
$$

that is, when $Q_0\overline{\mathbf{Q}}$ is a purely imaginary vector, and in particular when $Q_0=0$.

*Proof.* The centre is $\mathbb{C}e_0$, so the diagonal is central exactly when its vector part vanishes. The $k$-th component of the vector part is $-Q_0\overline{Q_k}-\overline{Q_0}Q_k=-2\mathrm{Re}(Q_0\overline{Q_k})$, which vanishes exactly when $\mathrm{Re}(Q_0\overline{Q_k})=0$, that is when $Q_0\overline{Q_k}$ is purely imaginary. If $Q_0=0$ the three conditions hold. $\square$

**Corollary (the two witnesses).** On the two elements

$$
e_1,
\qquad
e_1+ie_2
$$

the diagonal is central, and the values are $-e_0$ and $-2e_0$ respectively: $K(e_1,e_1)=-1$, $K(e_1+ie_2,e_1+ie_2)=-1-1=-2$, and in both cases $Q_0=0$, so the mixed term vanishes. On the element

$$
e_0+e_1
$$

the diagonal is not central: $K(e_0+e_1,e_0+e_1)=1-1=0$ and the vector part is $-1\cdot e_1-1\cdot e_1=-2e_1$, so $(e_0+e_1)\star(e_0+e_1)=-2e_1$.

**Remark (what the two witnesses show).** The two witnesses named in the menu comment are the vector directions $e_1$ and $e_1+ie_2$, and on both the diagonal is the *complex scalar multiple* of $e_0$ given by the form: $-e_0$ and $-2e_0$. Both are central, so the choice of these two as the witnesses of non-centrality is itself the departure: they lie in the vector subspace $\mathbf{e}$, on which the block's diagonal is central, and not only on $\mathbb{C}e_1$ and the line through $e_1+ie_2$. The element that shows the block's own obstruction is $e_0+e_1$, whose scalar coefficient is nonzero and whose $Q_0\overline{Q_1}=1$ is real and not purely imaginary; the general criterion is the display above.

## The Two Halves of the Diagonal

**Theorem (the two orders).** The two orders whose half-sum is the diagonal are

$$
\tilde Q^{\natural}\tilde Q^{*}
\quad\text{and}\quad
\tilde Q^{*}\tilde Q^{\natural},
$$

their sum is $2\,\tilde Q\star\tilde Q$, their difference is $2\mathbf{Q}\times\overline{\mathbf{Q}}$, and their scalar parts are equal to $K(\tilde Q,\tilde Q)$.

*Proof.* The definitions give $\tilde Q^{\natural}\tilde Q^{*}+\tilde Q^{*}\tilde Q^{\natural}=2\,\tilde Q\star\tilde Q$ and $\tilde Q^{\natural}\tilde Q^{*}-\tilde Q^{*}\tilde Q^{\natural}=2\,\mathbf{Q}\times\overline{\mathbf{Q}}$, the second by the identification of the antisymmetric part with the cross product. The scalar parts are equal because $\mathrm{Sc}(XY)=\mathrm{Sc}(YX)$ for the plain product. $\square$

**Corollary (when one half vanishes).** The two orders are equal exactly when $\mathbf{Q}\times\overline{\mathbf{Q}}=0$, and their sum vanishes exactly when the two are opposite, $\tilde Q^{\natural}\tilde Q^{*}=-\tilde Q^{*}\tilde Q^{\natural}$.

**Worked witness pairs.** The two named pairs separate the halves.

- On $\tilde P=-ie_3$, $\tilde Q=-ie_0$: both orders equal $-e_3$, so the difference vanishes and $\tilde P\star\tilde Q=-e_3$ is the first half alone.
- On $\tilde P=e_2$, $\tilde Q=e_1$: the first order is $-e_3$ and the second is $e_3$, so the sum vanishes and $\tilde P\star\tilde Q=0$, while the antisymmetric companion $\tilde P^{\natural}\tilde Q^{*}-\tilde Q^{*}\tilde P^{\natural}=-2e_3$.

The two pairs show the two extreme cases of the split: the two orders coincident, and the two orders opposite.

**Remark.** The half-difference is the diagonal of Block 8, $\mathrm{AQS}(\tilde Q,\tilde Q)=\mathbf{Q}\times\overline{\mathbf{Q}}$; the reconstruction $\tilde P^{\natural}\tilde Q^{*}=\tilde P\star\tilde Q+\mathbf{P}\times\overline{\mathbf{Q}}$ is the introduction's, and here only the diagonal case is read.

## The Elements of Square Zero

**Theorem (the square-zero family).** $\tilde Q\star\tilde Q=0$ holds exactly for

$$
\tilde Q=0
\quad\text{and for}\quad
\tilde Q=\alpha\,e_0-\frac{i\alpha}{|\alpha|^{2}}\,\mathbf{c},
\qquad
\alpha\in\mathbb{C}^{\times},\ \ \mathbf{c}\in\mathbb{R}^{3},\ \ |\mathbf{c}|^{2}=|\alpha|^{4},
$$

the second family being a real four-dimensional cone through the origin. In particular $e_0+i\boldsymbol\mu$ has square zero for every real unit vector $\boldsymbol\mu$.

*Proof.* By the diagonal form, $\tilde Q\star\tilde Q=0$ asks for $K(\tilde Q,\tilde Q)=0$ and $Q_0\overline{Q_k}\in i\mathbb{R}$ for each $k$. If $Q_0=0$ the second condition is void, but the first reads $-\sum_k|Q_k|^{2}=0$, so $\tilde Q=0$. If $Q_0=\alpha\neq0$, write $Q_0\overline{Q_k}=ic_k$ with $c_k\in\mathbb{R}$; then $Q_k=-ic_k/\overline{\alpha}=-i\alpha c_k/|\alpha|^{2}$ and $|Q_k|^{2}=c_k^{2}/|\alpha|^{2}$, so $K=0$ reads $|\alpha|^{2}=\sum_kc_k^{2}/|\alpha|^{2}$, that is $|\mathbf{c}|^{2}=|\alpha|^{4}$. Conversely the displayed family satisfies both conditions. The family has $\alpha$ of real dimension two and $\mathbf{c}$ on a sphere of real dimension two, hence real dimension four. $\square$

**Remark (square zero is not isotropy).** The square-zero elements are strictly inside the isotropic set of $K$, which is $\{K(\tilde Q,\tilde Q)=0\}$ and also contains the elements with a nonzero mixed vector part, for instance $e_0+e_1$. The isotropic structure is *The Isotropic Structure of the General Quaternionic Sesqualgebra*, and the zero divisors of the plain product, which the square-zero family touches but does not coincide with, are *Biquaternion Zero Divisors*.

## The Idempotents

**Theorem (the idempotent family).** $\tilde Q\star\tilde Q=\tilde Q$ holds exactly for

$$
0,
\qquad
e_0,
\qquad\text{and}\qquad
-\tfrac12e_0+\boldsymbol\mu,
\qquad
\boldsymbol\mu\in\mathbb{R}^{3},\ \ |\boldsymbol\mu|^{2}=\tfrac34.
$$

Every nonzero idempotent has norm $N(\tilde Q)=\tilde Q^{\natural}\tilde Q=1$, and all of them lie in the real quaternion subspace.

*Proof.* Let $Q_0=\alpha$ and $\mathbf{Q}=\mathbf{x}$. The equation splits into the scalar part $K(\tilde Q,\tilde Q)=\alpha$ and the vector part $-2\mathrm{Re}(\alpha\overline{\mathbf{x}})=\mathbf{x}$. If $\alpha=0$ the vector equation gives $\mathbf{x}=0$, hence $\tilde Q=0$. If $\alpha\neq0$ and $\mathbf{x}\neq0$, write the vector equation and its conjugate as the two equations $\alpha\overline{\mathbf{x}}+(\overline{\alpha}+1)\mathbf{x}=0$ and $\overline{\alpha}\mathbf{x}+(\alpha+1)\overline{\mathbf{x}}=0$; eliminating $\overline{\mathbf{x}}$ leaves $\bigl[(1+\alpha)(1+\overline{\alpha})-\alpha\overline{\alpha}\bigr]\mathbf{x}=0$, which with $\mathbf{x}\neq0$ forces $(1+\alpha)(1+\overline{\alpha})=\alpha\overline{\alpha}$, that is $2\mathrm{Re}\,\alpha=-1$, so $\alpha=-\tfrac12+ib$. Substituting back, $(1+\overline{\alpha})(\overline{\mathbf{x}}-\mathbf{x})=0$; if $b\neq0$ this gives $\mathbf{x}$ real, and the scalar equation $\alpha=| \alpha|^{2}-|\mathbf{x}|^{2}$ has a real left side and a real right side, so $b=0$, a contradiction; hence $b=0$, $\alpha=-\tfrac12$, and $\mathbf{x}$ real with $|\mathbf{x}|^{2}=\tfrac34$. The remaining case $\mathbf{x}=0$ leaves the scalar equation $\alpha^{2}=\alpha$, so $\alpha\in\{0,1\}$. Finally $\tilde Q=\alpha e_0+\mathbf{x}$ with real $\alpha,\mathbf{x}$ has $N=\alpha^{2}+|\mathbf{x}|^{2}$, which is $1$ on each of the nonzero families. $\square$

**Remark.** The two isolated idempotents are the origin and the unit candidate $e_0$, and the third family is a two-sphere in the real quaternion subspace, of radius $\sqrt{3}/2$ around $-\tfrac12e_0$. The block has more idempotents than a division algebra and fewer than a matrix algebra; they are the fixed points of a quadratic map on a real four-space, and the family appears because the diagonal is real-valued on the real quaternions.

## The Absence of a Unit Carried by the Diagonal

**Theorem (the two one-sided actions).** The two conjugations appear as the two one-sided actions of $e_0$:

$$
e_0\star\tilde Q=\tilde Q^{*},
\qquad
\tilde Q\star e_0=\tilde Q^{\natural}.
$$

On a diagonal element the two actions give the two conjugations of the element, $\tilde Q^{*}$ and $\tilde Q^{\natural}$, which agree exactly when $\tilde Q$ is real.

*Proof.* $e_0$ is the identity of the plain product, so $e_0\star\tilde Q=\tfrac12(\tilde Q^{*}+\tilde Q^{*})=\tilde Q^{*}$, and the right action is the conjugate-commutative mirror, or the same computation with the factors exchanged. The two conjugations agree exactly when $\overline{\tilde Q}=\tilde Q$, that is when $\tilde Q$ is real. $\square$

**Corollary (no unit).** There is no left unit and no right unit.

*Proof.* A left unit forces $\tilde E^{\natural}=e_0$ and hence $\tilde E=e_0$, but $e_0\star e_1=-e_1$; a right unit forces $\tilde Q^{\natural}=\tilde Q$ for all $\tilde Q$, which fails at $e_1$. $\square$

**Remark.** The diagonal carries the two actions in the following sense: the two orders of the diagonal are the two conjugations of the element read at the two slots, and the unit candidate is the only element whose two actions are conjugations. The one-sided actions of the general quaternionic sesquilinear product are *The Two One-Sided Actions and the Absence of a Unit*, and on the block they are the two displays above.

## Worked Examples

**A central diagonal off the centre.** $\tilde Q=2e_0+ie_1$: $K=4-1=3$ and the mixed term is $-Q_0\overline{Q_1}-\overline{Q_0}Q_1=-(2)(-i)-(2)(i)=2i-2i=0$; its vanishing makes the vector part $0$, so $\tilde Q\star\tilde Q=3e_0$, central with $Q_0\neq0$. The criterion is read on $Q_0\overline{Q_1}=2(-i)=-2i$, purely imaginary, and it is the imaginary character of $Q_0\overline{Q_k}$ — not its reality — that kills the mixed term.

**A square-zero element.** $\tilde Q=e_0+ie_1$: $K=1-1=0$ and the mixed term $-e_0\overline{(ie_1)}-\overline{e_0}(ie_1)=-(-i)e_1-(i)e_1=ie_1-ie_1=0$, so $\tilde Q\star\tilde Q=0$; here $\alpha=1$ and $\mathbf{c}=-e_1$ with $|\mathbf{c}|^{2}=1=|\alpha|^{4}$.

**An idempotent.** $\tilde Q=-\tfrac12e_0+\tfrac{\sqrt3}{2}e_1$: $|\boldsymbol\mu|^{2}=\tfrac34$ and $\tilde Q\star\tilde Q=\tilde Q$; the norm is $N(\tilde Q)=\tfrac14+\tfrac34=1$.

**The two halves at a vector.** $\tilde Q=e_1$: $\tilde Q^{\natural}\tilde Q^{*}=(-e_1)(-e_1)=-e_0$ and $\tilde Q^{*}\tilde Q^{\natural}=(-e_1)(-e_1)=-e_0$; the two orders coincide, the difference vanishes, and the diagonal is $-e_0$.

**Coincident and opposite orders.** $\tilde Q=2e_0+ie_1$: $\tilde Q^{\natural}=2e_0-ie_1$ and $\tilde Q^{*}=2e_0+ie_1$ (the coefficientwise conjugation sends $Q_0$ to $2$ and $Q_1$ to $-i$, and the natural conjugation restores the vector coefficient to $+i$), so the first order is $(2e_0-ie_1)(2e_0+ie_1)=3e_0$ and the second is $(2e_0+ie_1)(2e_0-ie_1)=3e_0$; the two orders coincide, and the diagonal is the central value $3e_0$ read in the earlier example. For the pair $\tilde P=e_2$, $\tilde Q=e_1$ the two orders are opposite, $-e_3$ and $e_3$, and their sum vanishes.

## Summary

The diagonal of the block is the real element $\tilde Q\star\tilde Q=K(\tilde Q,\tilde Q)e_0-Q_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{Q}$, with real scalar part $|Q_0|^{2}-\sum_k|Q_k|^{2}$ and real vector part $-2\sum_k\mathrm{Re}(Q_0\overline{Q_k})e_k$. It is central exactly when $Q_0\overline{Q_k}\in i\mathbb{R}$ for each $k$, and in particular on the whole vector subspace; the two witnesses $e_1$ and $e_1+ie_2$ carry the central values $-e_0$ and $-2e_0$, and $e_0+e_1$ carries the non-central value $-2e_1$. The two halves of the diagonal are the two orders $\tilde Q^{\natural}\tilde Q^{*}$ and $\tilde Q^{*}\tilde Q^{\natural}$, with sum $2\,\tilde Q\star\tilde Q$, difference $2\mathbf{Q}\times\overline{\mathbf{Q}}$, and equal scalar parts; the witness pairs $(-ie_3,-ie_0)$ and $(e_2,e_1)$ exhibit the coincident case and the opposite case. The square-zero elements are $0$ and the real four-dimensional family $\alpha e_0-(i\alpha/|\alpha|^{2})\mathbf{c}$ with $|\mathbf{c}|^{2}=|\alpha|^{4}$, among them $e_0+i\boldsymbol\mu$ for real unit $\boldsymbol\mu$. The idempotents are $0$, $e_0$ and the two-sphere $-\tfrac12e_0+\boldsymbol\mu$ with $|\boldsymbol\mu|^{2}=\tfrac34$, all of norm one. The two one-sided actions of $e_0$ are the two conjugations, $\tilde Q^{*}$ and $\tilde Q^{\natural}$, and the block has no unit.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Q\star\tilde Q=K(\tilde Q,\tilde Q)e_0-Q_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{Q}$ | the diagonal, a real element |
| $Q_0\overline{Q_k}\in i\mathbb{R}$ for all $k$ | the criterion of centrality of the diagonal |
| $e_1$, $e_1+ie_2$; $e_0+e_1$ | the two central witnesses; the non-central witness |
| $\tilde Q^{\natural}\tilde Q^{*}$, $\tilde Q^{*}\tilde Q^{\natural}$ | the two halves of the diagonal, sum $2\tilde Q\star\tilde Q$, difference $2\mathbf{Q}\times\overline{\mathbf{Q}}$ |
| $\alpha e_0-(i\alpha/|\alpha|^{2})\mathbf{c}$, $|\mathbf{c}|^{2}=|\alpha|^{4}$ | the square-zero elements |
| $-\tfrac12e_0+\boldsymbol\mu$, $|\boldsymbol\mu|^{2}=\tfrac34$ | the idempotents off $0$ and $e_0$ |
| $e_0\star\tilde Q=\tilde Q^{*}$, $\tilde Q\star e_0=\tilde Q^{\natural}$ | the two one-sided actions; no unit |

## Further Reading

- *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-sesqualgebra-of-biquaternions.md`), for the product and the reconstruction of the general quaternionic sesquilinear product from its two halves.
- *Introduction to the General Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-general-quaternionic-sesqualgebra-of-biquaternions.md`), for the unsplit product and its square.
- *The 12 Products of the Biquaternion Complex Space* (`articles_maths/the-12-products-of-the-biquaternion-complex-space.md`), for the antisymmetric companion and the table of the twelve operations.
- *The Two One-Sided Actions and the Absence of a Unit* (`articles_maths/the-two-one-sided-actions-and-the-absence-of-a-unit.md`), for the one-sided actions of the general quaternionic sesquilinear product.
- *The Krein Gram Matrix and the Restrictions of the Form* (`articles_maths/the-krein-gram-matrix-and-the-restrictions-of-the-form.md`), for the form $K$ appearing as the scalar part of the diagonal.
- *The Isotropic Structure of the General Quaternionic Sesqualgebra* (`articles_maths/the-isotropic-structure-of-the-general-quaternionic-sesqualgebra.md`), for the isotropic elements, of which the square-zero family is a part.
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the norm $N$.
- *The Six Subspaces under the Symmetric Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/the-six-subspaces-under-the-symmetric-quaternionic-sesqualgebra-of-biquaternions.md`), for the closure of the six subspaces under the product.
