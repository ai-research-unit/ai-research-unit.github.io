# __The Symmetric Quaternionic Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$__

## Introduction

The biquaternion algebra has two matrix models, the isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$ and the regular representation on the four complex coefficients, and this article writes the symmetric quaternionic sesquilinear product in the first. In the two-by-two model the matrices are

$$
\mathsf{M}_2(\tilde Q)=Q_0I-i(Q_1\sigma_1+Q_2\sigma_2+Q_3\sigma_3),
\qquad
\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\
\sigma_2=\begin{pmatrix}0&-i\\ i&0\end{pmatrix},\
\sigma_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
$$

and the two conjugations of the algebra become the two matrix operations: the natural conjugation ${}^{\natural}$ becomes the adjugate, $\mathsf{M}_2(\tilde Q^{\natural})=\operatorname{adj}\mathsf{M}_2(\tilde Q)$, and the star conjugation ${}^{*}$ becomes the conjugate transpose, $\mathsf{M}_2(\tilde Q^{*})=\mathsf{M}_2(\tilde Q)^{\dagger}$. The block is the half-sum of the two orders, so it becomes the **symmetrisation of the twisted matrix product**:

$$
\mathsf{M}_2(\tilde P\star\tilde Q)=\tfrac12\bigl(\operatorname{adj}\mathsf{M}_2(\tilde P)\,\mathsf{M}_2(\tilde Q)^{\dagger}+\mathsf{M}_2(\tilde Q)^{\dagger}\,\operatorname{adj}\mathsf{M}_2(\tilde P)\bigr).
$$

This article is the first of the two representation articles of the block, and its companion *The Symmetric Quaternionic Sesqualgebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$* reads the same symmetrisation on the regular model. The article computes the trace and the rank of the matrix form, the determinant, the diagonal and its deformation, and the matrix form of the Krein form $K$ with its Gram matrix and its indefinite cone.

The model is *The General Quaternionic Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*; the form $K$ is *The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra*; the diagonal and its centrality are *The Non-Central Diagonal and the Two Halves of the Symmetric Quaternionic Sesqualgebra*; and the product is *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions*.

**Conventions.** $\operatorname{adj}M$ is the adjugate of the two-by-two matrix $M$, $\operatorname{adj}\begin{pmatrix}a&b\\c&d\end{pmatrix}=\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$; $M^{\dagger}$ is the conjugate transpose; $N(\tilde Q)=\tilde Q^{\natural}\tilde Q=Q_0^{2}+Q_1^{2}+Q_2^{2}+Q_3^{2}$ is the norm and $\det\mathsf{M}_2(\tilde Q)=N(\tilde Q)$; the coefficient basis is $e_0,e_1,e_2,e_3$; and $\mathbf Q=(Q_1,Q_2,Q_3)$ is the vector part.

## The Two-by-Two Model

**Theorem (the product formula).** In the two-by-two model,

$$
\mathsf{M}_2(\tilde P\star\tilde Q)=\tfrac12\bigl(\operatorname{adj}\mathsf{M}_2(\tilde P)\,\mathsf{M}_2(\tilde Q)^{\dagger}+\mathsf{M}_2(\tilde Q)^{\dagger}\,\operatorname{adj}\mathsf{M}_2(\tilde P)\bigr).
$$

*Proof.* The isomorphism $\mathsf{M}_2$ is $\mathbb{C}$-linear and multiplicative, and it carries the two conjugations to the adjugate and the conjugate transpose; applying it to $\tilde P\star\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q^{*}+\tilde Q^{*}\tilde P^{\natural})$ gives the display. Verified on random pairs. $\square$

**Theorem (the trace and the determinant).** For all biquaternions,

$$
\operatorname{Tr}\mathsf{M}_2(\tilde P\star\tilde Q)=2K(\tilde P,\tilde Q),
\qquad
\det\mathsf{M}_2(\tilde P\star\tilde Q)=N(\tilde P\star\tilde Q).
$$

*Proof.* The trace of $\operatorname{adj}\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger}$ is twice the scalar part of $\tilde P^{\natural}\tilde Q^{*}$, by the identification of the trace with twice the scalar part; the second term contributes the same, so the trace of the half-sum is $\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=K(\tilde P,\tilde Q)$ counted with the two orders, that is $2K$. The determinant is the norm of the value because $\det\mathsf{M}_2(\tilde X)=N(\tilde X)$ for every element and $\mathsf{M}_2$ is multiplicative. Verified on the model. $\square$

**Corollary (the matrix form of $K$).** The Krein form is recovered from the model by

$$
K(\tilde P,\tilde Q)=\tfrac12\operatorname{Tr}\bigl(\operatorname{adj}\mathsf{M}_2(\tilde P)\,\mathsf{M}_2(\tilde Q)^{\dagger}\bigr),
$$

and its Gram matrix in the coefficient basis is $E=\operatorname{diag}(1,-1,-1,-1)$.

*Proof.* The first display is the trace theorem applied to the first order alone, which contributes $K$; the Gram matrix is the matrix of the form on $e_0,e_1,e_2,e_3$, computed in *The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra*. $\square$

**Theorem (rank).** The rank of $\mathsf{M}_2(\tilde P\star\tilde Q)$ is two when $N(\tilde P\star\tilde Q)\neq0$, and is zero or one on the degeneracy set $N(\tilde P\star\tilde Q)=0$.

*Proof.* A two-by-two matrix has rank two exactly when its determinant is nonzero; the determinant is $N(\tilde P\star\tilde Q)$, so the rank is two off the set where the norm of the value vanishes and drops to at most one on it. Verified on the model. $\square$

## The Deformation of the Diagonal in the Model

**Theorem (the diagonal matrix).** In the two-by-two model the diagonal is

$$
\mathsf{M}_2(\tilde Q\star\tilde Q)=\Bigl(|Q_0|^{2}-\sum_{k=1}^{3}|Q_k|^{2}\Bigr)I
-\mathsf{M}_2\bigl(Q_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{Q}\bigr),
$$

so it is the scalar matrix of the form value minus the matrix of the mixed term.

*Proof.* Apply $\mathsf{M}_2$ to the diagonal form $\tilde Q\star\tilde Q=K(\tilde Q,\tilde Q)e_0-Q_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{Q}$ of *The Non-Central Diagonal and the Two Halves of the Symmetric Quaternionic Sesqualgebra*; the first summand becomes $K(\tilde Q,\tilde Q)I$ and the second the matrix of the mixed term. $\square$

**Corollary (the two witnesses give scalar matrices).** On the two witnesses,

$$
\mathsf{M}_2(e_1\star e_1)=\mathsf{M}_2(-e_0)=-I,
\qquad
\mathsf{M}_2\bigl((e_1+ie_2)\star(e_1+ie_2)\bigr)=\mathsf{M}_2(-2e_0)=-2I,
$$

both scalar matrices, because both elements lie in the vector subspace and their mixed term vanishes.

*Proof.* $e_1\star e_1=-e_0$ and $(e_1+ie_2)\star(e_1+ie_2)=-2e_0$ by the diagonal article; their matrices are $-I$ and $-2I$. $\square$

**Remark (where the deformation appears).** The menu of the block records the deformation of the diagonal as a matrix that is no longer scalar, exhibited on the witnesses $e_1$ and $e_1+ie_2$. The computation gives the opposite on those two: both are scalar matrices, $-I$ and $-2I$, because both elements lie in the vector subspace, where the mixed term vanishes. The deformation is real, and the element that exhibits it is $e_0+e_1$, whose diagonal is $-2e_1$ and whose matrix is

$$
\mathsf{M}_2\bigl((e_0+e_1)\star(e_0+e_1)\bigr)=\mathsf{M}_2(-2e_1)=2i\sigma_1=\begin{pmatrix}0&2i\\2i&0\end{pmatrix},
$$

a non-scalar matrix, non-scalar exactly when the mixed term $Q_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{Q}$ does not vanish, that is when $Q_0\overline{Q_k}\notin i\mathbb{R}$ for some $k$, the centrality criterion of *The Non-Central Diagonal and the Two Halves of the Symmetric Quaternionic Sesqualgebra*. This is a departure of the computation from the menu comment, recorded here rather than smoothed over.

## The Matrix Form of $K$ and Its Cone

**Theorem (the form in the model).** In the two-by-two model the Krein form reads

$$
K(\tilde P,\tilde Q)=\tfrac12\operatorname{Tr}\bigl(\operatorname{adj}\mathsf{M}_2(\tilde P)\,\mathsf{M}_2(\tilde Q)^{\dagger}\bigr),
$$

with Gram matrix $E=\operatorname{diag}(1,-1,-1,-1)$ in the coefficient basis.

*Proof.* The display is the trace theorem; the Gram matrix is the matrix of $K$ on the coefficient basis. $\square$

**Corollary (the indefinite cone in the model).** The image of the isotropic cone of $K$ under $\mathsf{M}_2$ is the set of matrices

$$
\Bigl\{\mathsf{M}_2(\tilde P):\ |P_0|^{2}=\sum_{k=1}^{3}|P_k|^{2}\Bigr\},
$$

a cone through the origin whose elements are exactly the values $\mathsf{M}_2(\tilde P)$ with $\operatorname{Tr}\mathsf{M}_2(\tilde P^{\natural}\tilde P^{*})=0$.

*Proof.* The isotropic cone is $\{|P_0|^{2}=\sum_k|P_k|^{2}\}$ by the form article; applying the isomorphism $\mathsf{M}_2$ and the trace formula gives the displayed set, since $K(\tilde P,\tilde P)=\mathrm{Sc}(\tilde P^{\natural}\tilde P^{*})=\tfrac12\operatorname{Tr}\mathsf{M}_2(\tilde P^{\natural}\tilde P^{*})$. $\square$

**Remark.** The matrix form of the form is the adjugate-twisted trace pairing; the indefinite cone is the cone of the elements of zero form value, mapped into the matrix algebra. The form itself, its Gram matrix and its cone, independently of the models, are in *The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra* and *The Krein Gram Matrix and the Restrictions of the Form*.

## Worked Examples

**A diagonal in the model.** $e_1\star e_1=-e_0$: $\mathsf{M}_2=-I$, trace $-2=2K(e_1,e_1)=2(-1)$, determinant $1=N(-e_0)=1$, rank two.

**A null diagonal.** $(e_1+ie_2)\star(e_1+ie_2)=-2e_0$: $\mathsf{M}_2=-2I$, trace $-4=2(-2)$, determinant $4=N(-2e_0)=4$.

**The non-scalar diagonal.** $(e_0+e_1)\star(e_0+e_1)=-2e_1$: $\mathsf{M}_2=2i\sigma_1=\begin{pmatrix}0&2i\\2i&0\end{pmatrix}$, trace $0=2K(e_0+e_1,e_0+e_1)=2\cdot0$, determinant $4=N(-2e_1)=4$.

**A vanishing product in the model.** $e_2\star e_1=0$: $\mathsf{M}_2=0$, trace $0$, rank zero.

**The form recovered.** $K(e_0,e_1)=0$: $\tfrac12\operatorname{Tr}(\operatorname{adj}I\cdot\mathsf{M}_2(e_1)^{\dagger})=\tfrac12\operatorname{Tr}((-i\sigma_1)^{\dagger})=0$, the traceless matrix.

**The cone.** $e_0+e_1$ is isotropic: $|1|^{2}=|1|^{2}$, and $\mathsf{M}_2(e_0+e_1)$ lies in the image cone.

## The Matrices

**The generators.** The realization is fixed on the basis by four matrices:

$$
\mathsf{M}_2(e_0)=\begin{pmatrix}1&0\\0&1\end{pmatrix},\qquad
\mathsf{M}_2(e_1)=\begin{pmatrix}0&-i\\-i&0\end{pmatrix},\qquad
\mathsf{M}_2(e_2)=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
\mathsf{M}_2(e_3)=\begin{pmatrix}-i&0\\0&i\end{pmatrix}.
$$

The general element has the matrix $\mathsf{M}_2(\tilde Q)=\begin{pmatrix}Q_0-iQ_3&-iQ_1-Q_2\\-iQ_1+Q_2&Q_0+iQ_3\end{pmatrix}$ of trace $2Q_0$ and determinant $N(\tilde Q)$.

**The twisted product, entry by entry.** The block is the symmetrisation of the twisted product, and at the pair $e_1,e_1$ the adjugated conjugate-transposed product is the negative identity,

$$
\operatorname{adj}\mathsf{M}_2(e_1)\mathsf{M}_2(e_1)^{\dagger}
=\begin{pmatrix}0&i\\i&0\end{pmatrix}\begin{pmatrix}0&i\\i&0\end{pmatrix}
=\begin{pmatrix}-1&0\\0&-1\end{pmatrix}=-I=\mathsf{M}_2(e_1\star e_1),
$$

since $e_1\star e_1=-e_0$. At the pair $e_1+ie_2,\,e_1+ie_2$, where $N(e_1+ie_2)=1+i^{2}=0$, the two orders of the twisted product are the two matrices

$$
\operatorname{adj}\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde P)^{\dagger}=\begin{pmatrix}-4&0\\0&0\end{pmatrix},
\qquad
\mathsf{M}_2(\tilde P)^{\dagger}\operatorname{adj}\mathsf{M}_2(\tilde P)=\begin{pmatrix}0&0\\0&-4\end{pmatrix},
$$

of trace $-4$ and determinant $0$, and the symmetrised value is the scalar matrix $-2I=K(e_1+ie_2,e_1+ie_2)I$: **the two orders differ only in which diagonal entry carries the $-4$**, so the symmetrisation is the scalar matrix and the half-difference, the antisymmetric companion, is the diagonal matrix $\operatorname{diag}(-2,2)$, the value of the antisymmetric quaternionic sesqualgebra at the same pair.

## Summary

In the two-by-two model the block is the symmetrisation of the twisted matrix product, $\mathsf{M}_2(\tilde P\star\tilde Q)=\tfrac12(\operatorname{adj}\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger}+\mathsf{M}_2(\tilde Q)^{\dagger}\operatorname{adj}\mathsf{M}_2(\tilde P))$, with trace $2K$, determinant $N(\tilde P\star\tilde Q)$ and rank two off the degeneracy set. The diagonal is the scalar matrix of the form value minus the matrix of the mixed term; on the two witnesses $e_1$ and $e_1+ie_2$ it is the scalar matrices $-I$ and $-2I$, and the deformation away from the scalar matrices appears at $e_0+e_1$, where the matrix is $\begin{pmatrix}0&2i\\2i&0\end{pmatrix}$. The Krein form is $K(\tilde P,\tilde Q)=\tfrac12\operatorname{Tr}(\operatorname{adj}\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger})$, with Gram matrix $E=\operatorname{diag}(1,-1,-1,-1)$ in the coefficient basis, and its indefinite cone maps into the matrices of zero form value.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_2(\tilde Q)=Q_0I-i\sum_kQ_k\sigma_k$ | the two-by-two model; $\mathsf{M}_2({}^{\natural})=\operatorname{adj}$, $\mathsf{M}_2({}^{*})={}^{\dagger}$ |
| $\mathsf{M}_2(\tilde P\star\tilde Q)=\tfrac12(\operatorname{adj}\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger}+\mathsf{M}_2(\tilde Q)^{\dagger}\operatorname{adj}\mathsf{M}_2(\tilde P))$ | the block in the two-by-two model |
| $\operatorname{Tr}\mathsf{M}_2(\tilde P\star\tilde Q)=2K$, $\det\mathsf{M}_2=N$ | trace and determinant in the two-by-two model |
| $\mathsf{M}_2(\tilde Q\star\tilde Q)=K(\tilde Q,\tilde Q)I-\mathsf{M}_2(Q_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{Q})$ | the diagonal in the model |
| $\mathsf{M}_2(e_1\star e_1)=-I$, $\mathsf{M}_2((e_1+ie_2)\star(e_1+ie_2))=-2I$, $\mathsf{M}_2((e_0+e_1)\star(e_0+e_1))=2i\sigma_1$ | the two scalar witnesses and the non-scalar witness |
| $K(\tilde P,\tilde Q)=\tfrac12\operatorname{Tr}(\operatorname{adj}\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger})$ | the form in the model; Gram $E=\operatorname{diag}(1,-1,-1,-1)$ |

## Further Reading

- *The General Quaternionic Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-general-quaternionic-sesqualgebra-in-the-2x2-matrix-element-representation.md`), for the two-by-two model.
- *The Symmetric Quaternionic Sesqualgebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$* (`articles_maths/the-symmetric-quaternionic-sesqualgebra-in-the-4x4-matrix-element-representation.md`), for the reading on the regular model.
- *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-sesqualgebra-of-biquaternions.md`), for the product written in the models.
- *The Non-Central Diagonal and the Two Halves of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/the-non-central-diagonal-and-the-two-halves-of-the-symmetric-quaternionic-sesqualgebra.md`), for the diagonal, its centrality and the witnesses.
- *The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra* (`articles_maths/the-krein-form-as-a-product-on-the-symmetric-quaternionic-sesqualgebra.md`), for the form $K$, its Gram matrix and its cone.
- *The Krein Gram Matrix and the Restrictions of the Form* (`articles_maths/the-krein-gram-matrix-and-the-restrictions-of-the-form.md`), for the Gram matrix of the form.
- *The Multiplication Operators of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-quaternionic-sesqualgebra.md`), for the operators of the block and their traces.
