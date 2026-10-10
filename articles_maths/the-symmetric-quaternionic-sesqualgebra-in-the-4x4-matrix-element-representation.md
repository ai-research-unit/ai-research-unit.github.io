# __The Symmetric Quaternionic Sesqualgebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$__

## Introduction

The biquaternion algebra has two matrix models, the isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$ and the regular representation on the four complex coefficients, and this article writes the symmetric quaternionic sesquilinear product in the second. In the four-by-four regular model the left regular matrix $\mathsf{M}_4(\tilde Q)$ satisfies $\mathsf{M}_4(\tilde Q^{\natural})=\mathsf{M}_4(\tilde Q)^{\mathsf T}$ and $\mathsf{M}_4(\tilde Q^{*})=\mathsf{M}_4(\tilde Q)^{\dagger}$, and the block, being the half-sum of the two orders, becomes the **symmetrisation of the twisted matrix product**:

$$
\mathsf{M}_4(\tilde P\star\tilde Q)=\tfrac12\bigl(\mathsf{M}_4(\tilde P)^{\mathsf T}\mathsf{M}_4(\tilde Q)^{\dagger}+\mathsf{M}_4(\tilde Q)^{\dagger}\mathsf{M}_4(\tilde P)^{\mathsf T}\bigr).
$$

This article is the second of the two representation articles of the block, and its companion *The Symmetric Quaternionic Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* reads the same symmetrisation on the realization. The article computes the trace, the determinant and the rank of the regular matrix form, and the matrix form of the Krein form $K$, whose Gram matrix and indefinite cone live in the $2\times2$ companion.

The model is *The General Quaternionic Sesqualgebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$*; the form $K$ is *The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra*; the diagonal and its centrality are *The Non-Central Diagonal and the Two Halves of the Symmetric Quaternionic Sesqualgebra*; and the product is *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions*.

**Conventions.** $M^{\mathsf T}$ is the transpose and $M^{\dagger}$ the conjugate transpose; $N(\tilde Q)=\tilde Q^{\natural}\tilde Q=Q_0^{2}+Q_1^{2}+Q_2^{2}+Q_3^{2}$ is the norm and $\det\mathsf{M}_4(\tilde Q)=N(\tilde Q)^{2}$; the coefficient basis is $e_0,e_1,e_2,e_3$.

## The Four-by-Four Regular Model

**Theorem (the product formula).** In the regular representation,

$$
\mathsf{M}_4(\tilde P\star\tilde Q)=\tfrac12\bigl(\mathsf{M}_4(\tilde P)^{\mathsf T}\mathsf{M}_4(\tilde Q)^{\dagger}+\mathsf{M}_4(\tilde Q)^{\dagger}\mathsf{M}_4(\tilde P)^{\mathsf T}\bigr).
$$

*Proof.* The left regular matrix is multiplicative, $\mathsf{M}_4(\tilde X\tilde Y)=\mathsf{M}_4(\tilde X)\mathsf{M}_4(\tilde Y)$, and it carries the natural conjugation to the transpose and the star conjugation to the conjugate transpose; applying it to the two orders of $\tilde P\star\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q^{*}+\tilde Q^{*}\tilde P^{\natural})$ gives the display. Verified on random pairs. $\square$

**Theorem (the invariants).** For all biquaternions,

$$
\operatorname{Tr}\mathsf{M}_4(\tilde P\star\tilde Q)=4K(\tilde P,\tilde Q),
\qquad
\det\mathsf{M}_4(\tilde P\star\tilde Q)=N(\tilde P\star\tilde Q)^{2},
$$

and the rank of $\mathsf{M}_4(\tilde P\star\tilde Q)$ is four exactly when $N(\tilde P\star\tilde Q)\neq0$.

*Proof.* The trace of the regular matrix is four times the scalar part, so the trace of the half-sum is $4K$; the determinant of the regular matrix is $N(\tilde X)^{2}$, so the determinant of the value is $N(\tilde P\star\tilde Q)^{2}$; and a four-by-four matrix has rank four exactly when its determinant is nonzero. Verified on the model. $\square$

**Corollary (the trace of the operator in the model).** The trace of the value is the same invariant in the two models up to the factor of the model: it is $2K$ in the two-by-two model and $4K$ in the four-by-four model.

*Proof.* The two displays of the trace theorems, here and in the companion article. $\square$

**Remark (the diagonal in the regular model).** The diagonal is read in the regular model by applying $\mathsf{M}_4$ to the diagonal form $\tilde Q\star\tilde Q=K(\tilde Q,\tilde Q)e_0-Q_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{Q}$ of *The Non-Central Diagonal and the Two Halves of the Symmetric Quaternionic Sesqualgebra*: $\mathsf{M}_4(\tilde Q\star\tilde Q)=K(\tilde Q,\tilde Q)I_4-\mathsf{M}_4(Q_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{Q})$, the scalar matrix of the form value minus the matrix of the mixed term. On the vector witnesses $e_1$ and $e_1+ie_2$ the mixed term vanishes and the value is the scalar matrix $-I_4$ or $-2I_4$; the deformation away from the scalar matrices appears at $e_0+e_1$, as in the companion article.

## The Matrix Form of $K$ and Its Cone

**Theorem (the form in the model).** In the regular model the Krein form is read from the trace of the regular matrices,

$$
K(\tilde P,\tilde Q)=\tfrac14\operatorname{Tr}\bigl(\mathsf{M}_4(\tilde P)^{\mathsf T}\mathsf{M}_4(\tilde Q)^{\dagger}\bigr),
$$

the trace of the **one-order** twisted product, the first term of the symmetrised block; equivalently $\operatorname{Tr}\mathsf{M}_4(\tilde P\star\tilde Q)=4K(\tilde P,\tilde Q)$ for the symmetrised block.

*Proof.* The trace of the regular matrix is four times the scalar part, so $\operatorname{Tr}(\mathsf{M}_4(\tilde P)^{\mathsf T}\mathsf{M}_4(\tilde Q)^{\dagger})=\operatorname{Tr}\mathsf{M}_4(\tilde P^{\natural}\tilde Q^{*})=4K(\tilde P,\tilde Q)$. $\square$

**Remark (the indefinite cone in the regular model).** The image of the isotropic cone of $K$ under $\mathsf{M}_4$ is the set of regular matrices $\{\mathsf{M}_4(\tilde P):\ |P_0|^{2}=\sum_{k=1}^{3}|P_k|^{2}\}$, a cone through the origin whose elements are exactly the values $\mathsf{M}_4(\tilde P)$ with $\operatorname{Tr}\mathsf{M}_4(\tilde P^{\natural}\tilde P^{*})=0$; the cone and the Gram matrix $E=\operatorname{diag}(1,-1,-1,-1)$ are read in the $2\times2$ companion and in *The Krein Gram Matrix and the Restrictions of the Form*.

**Remark.** The matrix form of the form is the transpose-twisted trace pairing; the indefinite cone is the cone of the elements of zero form value, mapped into the matrix algebra. The form itself, its Gram matrix and its cone, independently of the models, are in *The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra* and *The Krein Gram Matrix and the Restrictions of the Form*.

## Worked Examples

**A diagonal in the model.** $e_1\star e_1=-e_0$: $\mathsf{M}_4=-I_4$, trace $-4=4K(e_1,e_1)=4(-1)$, determinant $1=N(-e_0)^{2}=1$, rank four.

**A null diagonal.** $(e_1+ie_2)\star(e_1+ie_2)=-2e_0$: $\mathsf{M}_4=-2I_4$, trace $-8=4(-2)$, determinant $16=N(-2e_0)^{2}=16$.

**The non-scalar diagonal.** $(e_0+e_1)\star(e_0+e_1)=-2e_1$: $\mathsf{M}_4=-2\mathsf{M}_4(e_1)$, trace $0=4K(e_0+e_1,e_0+e_1)=4\cdot0$, determinant $4=N(-2e_1)^{2}=4$.

**A vanishing product in the model.** $e_2\star e_1=0$: $\mathsf{M}_4=0$, trace $0$, rank zero.

**The form recovered.** $K(e_0,e_1)=0$: $\tfrac14\operatorname{Tr}(\mathsf{M}_4(e_0)^{\mathsf T}\mathsf{M}_4(e_1)^{\dagger})=\tfrac14\operatorname{Tr}\mathsf{M}_4(-e_1)=0$, $-e_1$ being traceless in the regular model.

**The cone.** $e_0+e_1$ is isotropic: $|1|^{2}=|1|^{2}$, and $\mathsf{M}_4(e_0+e_1)$ lies in the image cone.

## The Matrices

**The generators.** The regular model is fixed on the basis by four matrices:

$$
\mathsf{M}_4(e_0)=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},\qquad
\mathsf{M}_4(e_1)=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},
$$
$$
\mathsf{M}_4(e_2)=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix},\qquad
\mathsf{M}_4(e_3)=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix}.
$$

A general element is the block matrix

$$
\mathsf{M}_4(\tilde Q)=\begin{pmatrix}A&B\\-B&A\end{pmatrix},\qquad
A=\begin{pmatrix}Q_0&-Q_1\\Q_1&Q_0\end{pmatrix},\qquad
B=\begin{pmatrix}-Q_2&-Q_3\\-Q_3&Q_2\end{pmatrix},
$$

The general element has trace $4Q_0$ and determinant $N(\tilde Q)^2$.

**The twisted product, entry by entry.** The block is the symmetrisation of the transposed conjugate-transposed product, and at the pair $e_1,e_1$ the product is the negative identity,

$$
\mathsf{M}_4(e_1)^{\mathsf T}\mathsf{M}_4(e_1)^{\dagger}
=(-\mathsf{M}_4(e_1))(-\mathsf{M}_4(e_1))=\mathsf{M}_4(e_1)^2=-I_4=\mathsf{M}_4(e_1\star e_1),
$$

since $e_1\star e_1=-e_0$; and at the pair $e_1+ie_2,\,e_1+ie_2$ the symmetrised value is the scalar matrix $-2I_4=K(e_1+ie_2,e_1+ie_2)I_4$, the same scalar $-2$ as in the realization, the two models differing only in the size of the matrix.

**The two models.** At the vector witnesses, where the mixed term $Q_0\overline{\mathbf Q}+\overline{Q_0}\mathbf Q$ vanishes, the symmetrised value is the scalar matrix of the Krein form in both models, with the adjugate in the first slot of the realization and the transpose in the first slot of the regular model; away from those witnesses the value is the scalar matrix of the form minus the matrix of the mixed term, the deformation of *The Non-Central Diagonal and the Two Halves of the Symmetric Quaternionic Sesqualgebra*. The entrywise value $-I_4$ at the vector unit $e_1$ is the same statement in the regular model as the value $-I$ in the realization.

## Summary

In the four-by-four regular model the block is the symmetrisation of the twisted matrix product, $\mathsf{M}_4(\tilde P\star\tilde Q)=\tfrac12(\mathsf{M}_4(\tilde P)^{\mathsf T}\mathsf{M}_4(\tilde Q)^{\dagger}+\mathsf{M}_4(\tilde Q)^{\dagger}\mathsf{M}_4(\tilde P)^{\mathsf T})$, with trace $4K$, determinant $N(\tilde P\star\tilde Q)^{2}$ and rank four off the degeneracy set. The diagonal is the scalar matrix of the form value minus the matrix of the mixed term; on the two witnesses $e_1$ and $e_1+ie_2$ it is the scalar matrices $-I_4$ and $-2I_4$, and the deformation away from the scalar matrices appears at $e_0+e_1$. The Krein form is read from the trace of the regular matrices, $\operatorname{Tr}\mathsf{M}_4(\tilde P\star\tilde Q)=4K(\tilde P,\tilde Q)$, and its indefinite cone maps into the regular matrices of zero form value; the Gram matrix $E=\operatorname{diag}(1,-1,-1,-1)$ is read in the $2\times2$ companion.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_4(\tilde Q)$ | the left regular representation; $\mathsf{M}_4({}^{\natural})={}^{\mathsf T}$, $\mathsf{M}_4({}^{*})={}^{\dagger}$ |
| $\mathsf{M}_4(\tilde P\star\tilde Q)=\tfrac12(\mathsf{M}_4(\tilde P)^{\mathsf T}\mathsf{M}_4(\tilde Q)^{\dagger}+\mathsf{M}_4(\tilde Q)^{\dagger}\mathsf{M}_4(\tilde P)^{\mathsf T})$ | the block in the regular model |
| $\operatorname{Tr}\mathsf{M}_4(\tilde P\star\tilde Q)=4K$, $\det\mathsf{M}_4=N^{2}$ | trace and determinant in the regular model |
| $K(\tilde P,\tilde Q)=\tfrac14\operatorname{Tr}(\mathsf{M}_4(\tilde P)^{\mathsf T}\mathsf{M}_4(\tilde Q)^{\dagger})$ | the form read from the regular trace |

## Further Reading

- *The General Quaternionic Sesqualgebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$* (`articles_maths/the-general-quaternionic-sesqualgebra-in-the-4x4-matrix-element-representation.md`), for the regular model.
- *The Symmetric Quaternionic Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-symmetric-quaternionic-sesqualgebra-in-the-2x2-matrix-element-representation.md`), for the reading on the realization, the diagonal and the Gram matrix.
- *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-sesqualgebra-of-biquaternions.md`), for the product written in the models.
- *The Non-Central Diagonal and the Two Halves of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/the-non-central-diagonal-and-the-two-halves-of-the-symmetric-quaternionic-sesqualgebra.md`), for the diagonal, its centrality and the witnesses.
- *The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra* (`articles_maths/the-krein-form-as-a-product-on-the-symmetric-quaternionic-sesqualgebra.md`), for the form $K$, its Gram matrix and its cone.
- *The Krein Gram Matrix and the Restrictions of the Form* (`articles_maths/the-krein-gram-matrix-and-the-restrictions-of-the-form.md`), for the Gram matrix of the form.
- *The Multiplication Operators of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-quaternionic-sesqualgebra.md`), for the operators of the block and their traces.
