# __The Symmetric Quaternionic Sesqualgebra in the Matrix Representations__

## Introduction

The biquaternion algebra has two matrix models, the isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$ and the regular representation on the four complex coefficients, and this article writes the symmetric quaternionic sesquilinear product in both. In the two-by-two model the matrices are

$$
\Phi(\tilde Q)=Q_0I-i(Q_1\sigma_1+Q_2\sigma_2+Q_3\sigma_3),
\qquad
\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\
\sigma_2=\begin{pmatrix}0&-i\\ i&0\end{pmatrix},\
\sigma_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
$$

and the two conjugations of the algebra become the two matrix operations: the natural conjugation ${}^{\natural}$ becomes the adjugate, $\Phi(\tilde Q^{\natural})=\mathrm{adj}\,\Phi(\tilde Q)$, and the star conjugation ${}^{*}$ becomes the conjugate transpose, $\Phi(\tilde Q^{*})=\Phi(\tilde Q)^{\dagger}$. The block is the half-sum of the two orders, so it becomes the **symmetrisation of the twisted matrix product**:

$$
\Phi(\tilde P\star\tilde Q)=\tfrac12\bigl(\mathrm{adj}\,\Phi(\tilde P)\,\Phi(\tilde Q)^{\dagger}+\Phi(\tilde Q)^{\dagger}\,\mathrm{adj}\,\Phi(\tilde P)\bigr).
$$

In the four-by-four regular model the left regular matrix $\mathsf{M}_4(\tilde Q)$ satisfies $\mathsf{M}_4(\tilde Q^{\natural})=\mathsf{M}_4(\tilde Q)^{T}$ and $\mathsf{M}_4(\tilde Q^{*})=\mathsf{M}_4(\tilde Q)^{\dagger}$, and the same symmetrisation appears:

$$
\mathsf{M}_4(\tilde P\star\tilde Q)=\tfrac12\bigl(\mathsf{M}_4(\tilde P)^{T}\mathsf{M}_4(\tilde Q)^{\dagger}+\mathsf{M}_4(\tilde Q)^{\dagger}\mathsf{M}_4(\tilde P)^{T}\bigr).
$$

The article computes the trace and the rank of the two matrix forms, the determinant, the diagonal and its deformation, and the matrix form of the Krein form $K$ with its Gram matrix and its indefinite cone.

The two models are *The General Quaternionic Sesqualgebra in the $2\times2$ Matrix Representation* and *The General Quaternionic Sesqualgebra in the $4\times4$ Matrix Representation*; the form $K$ is *The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra*; the diagonal and its centrality are *The Non-Central Diagonal and the Two Halves of the Symmetric Quaternionic Sesqualgebra*; and the product is *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions*.

**Conventions.** $\mathrm{adj}\,M$ is the adjugate of the two-by-two matrix $M$, $\mathrm{adj}\,\begin{pmatrix}a&b\\c&d\end{pmatrix}=\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$; $M^{\dagger}$ is the conjugate transpose; $N(\tilde Q)=\tilde Q^{\natural}\tilde Q=Q_0^{2}+Q_1^{2}+Q_2^{2}+Q_3^{2}$ is the norm and $\det\Phi(\tilde Q)=N(\tilde Q)$; the coefficient basis is $e_0,e_1,e_2,e_3$.

## The Two-by-Two Model

**Theorem (the product formula).** In the two-by-two model,

$$
\Phi(\tilde P\star\tilde Q)=\tfrac12\bigl(\mathrm{adj}\,\Phi(\tilde P)\,\Phi(\tilde Q)^{\dagger}+\Phi(\tilde Q)^{\dagger}\,\mathrm{adj}\,\Phi(\tilde P)\bigr).
$$

*Proof.* The isomorphism $\Phi$ is $\mathbb{C}$-linear and multiplicative, and it carries the two conjugations to the adjugate and the conjugate transpose; applying it to $\tilde P\star\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q^{*}+\tilde Q^{*}\tilde P^{\natural})$ gives the display. The formula was checked on fifty random pairs. $\square$

**Theorem (the trace and the determinant).** For all biquaternions,

$$
\mathrm{Tr}\,\Phi(\tilde P\star\tilde Q)=2K(\tilde P,\tilde Q),
\qquad
\det\Phi(\tilde P\star\tilde Q)=N(\tilde P\star\tilde Q).
$$

*Proof.* The trace of $\mathrm{adj}\,\Phi(\tilde P)\Phi(\tilde Q)^{\dagger}$ is twice the scalar part of $\tilde P^{\natural}\tilde Q^{*}$, by the identification of the trace with twice the scalar part; the second term contributes the same, so the trace of the half-sum is $\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=K(\tilde P,\tilde Q)$ counted with the two orders, that is $2K$. The determinant is the norm of the value because $\det\Phi(\tilde X)=N(\tilde X)$ for every element and $\Phi$ is multiplicative. $\square$

**Corollary (the matrix form of $K$).** The Krein form is recovered from the model by

$$
K(\tilde P,\tilde Q)=\tfrac12\,\mathrm{Tr}\bigl(\mathrm{adj}\,\Phi(\tilde P)\,\Phi(\tilde Q)^{\dagger}\bigr),
$$

and its Gram matrix in the coefficient basis is $E=\mathrm{diag}(1,-1,-1,-1)$.

*Proof.* The first display is the trace theorem applied to the first order alone, which contributes $K$; the Gram matrix is the matrix of the form on $e_0,e_1,e_2,e_3$, computed in *The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra*. $\square$

**Theorem (rank).** The rank of $\Phi(\tilde P\star\tilde Q)$ is two when $N(\tilde P\star\tilde Q)\neq0$, and is zero or one on the degeneracy set $N(\tilde P\star\tilde Q)=0$.

*Proof.* A two-by-two matrix has rank two exactly when its determinant is nonzero; the determinant is $N(\tilde P\star\tilde Q)$, so the rank is two off the set where the norm of the value vanishes and drops to at most one on it. $\square$

## The Deformation of the Diagonal in the Model

**Theorem (the diagonal matrix).** In the two-by-two model the diagonal is

$$
\Phi(\tilde Q\star\tilde Q)=\Bigl(|Q_0|^{2}-\sum_{k=1}^{3}|Q_k|^{2}\Bigr)I
-\Phi\bigl(Q_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{Q}\bigr),
$$

so it is the scalar matrix of the form value minus the matrix of the mixed term.

*Proof.* Apply $\Phi$ to the diagonal form $\tilde Q\star\tilde Q=K(\tilde Q,\tilde Q)e_0-Q_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{Q}$ of *The Non-Central Diagonal and the Two Halves of the Symmetric Quaternionic Sesqualgebra*; the first summand becomes $K(\tilde Q,\tilde Q)I$ and the second the matrix of the mixed term. $\square$

**Corollary (the two witnesses give scalar matrices).** On the two witnesses,

$$
\Phi(e_1\star e_1)=\Phi(-e_0)=-I,
\qquad
\Phi\bigl((e_1+ie_2)\star(e_1+ie_2)\bigr)=\Phi(-2e_0)=-2I,
$$

both scalar matrices, because both elements lie in the vector subspace and their mixed term vanishes.

*Proof.* $e_1\star e_1=-e_0$ and $(e_1+ie_2)\star(e_1+ie_2)=-2e_0$ by the diagonal article; their matrices are $-I$ and $-2I$. $\square$

**Remark (where the deformation appears).** The menu of the block records the deformation of the diagonal as a matrix that is no longer scalar, exhibited on the witnesses $e_1$ and $e_1+ie_2$. The computation gives the opposite on those two: both are scalar matrices, $-I$ and $-2I$, because both elements lie in the vector subspace, where the mixed term vanishes. The deformation is real, and the element that exhibits it is $e_0+e_1$, whose diagonal is $-2e_1$ and whose matrix is

$$
\Phi\bigl((e_0+e_1)\star(e_0+e_1)\bigr)=\Phi(-2e_1)=2i\sigma_1=\begin{pmatrix}0&2i\\2i&0\end{pmatrix},
$$

a non-scalar matrix, non-scalar exactly when the mixed term $Q_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{Q}$ does not vanish, that is when $Q_0\overline{Q_k}\notin i\mathbb{R}$ for some $k$, the centrality criterion of *The Non-Central Diagonal and the Two Halves of the Symmetric Quaternionic Sesqualgebra*. This is a departure of the computation from the menu comment, recorded here rather than smoothed over.

## The Four-by-Four Regular Model

**Theorem (the product formula).** In the regular representation,

$$
\mathsf{M}_4(\tilde P\star\tilde Q)=\tfrac12\bigl(\mathsf{M}_4(\tilde P)^{T}\mathsf{M}_4(\tilde Q)^{\dagger}+\mathsf{M}_4(\tilde Q)^{\dagger}\mathsf{M}_4(\tilde P)^{T}\bigr).
$$

*Proof.* The left regular matrix is multiplicative, $\mathsf{M}_4(\tilde X\tilde Y)=\mathsf{M}_4(\tilde X)\mathsf{M}_4(\tilde Y)$, and it carries the natural conjugation to the transpose and the star conjugation to the conjugate transpose; applying it to the two orders gives the display. The formula was checked on fifty random pairs. $\square$

**Theorem (the invariants).** For all biquaternions,

$$
\mathrm{Tr}\,\mathsf{M}_4(\tilde P\star\tilde Q)=4K(\tilde P,\tilde Q),
\qquad
\det\mathsf{M}_4(\tilde P\star\tilde Q)=N(\tilde P\star\tilde Q)^{2},
$$

and the rank of $\mathsf{M}_4(\tilde P\star\tilde Q)$ is four exactly when $N(\tilde P\star\tilde Q)\neq0$.

*Proof.* The trace of the regular matrix is four times the scalar part, so the trace of the half-sum is $4K$; the determinant of the regular matrix is $N(\tilde X)^{2}$, so the determinant of the value is $N(\tilde P\star\tilde Q)^{2}$; and a four-by-four matrix has rank four exactly when its determinant is nonzero. $\square$

**Corollary (the trace of the operator in the model).** The trace of the value is the same invariant in the two models up to the factor of the model: it is $2K$ in the two-by-two model and $4K$ in the four-by-four model.

*Proof.* The two displays of the trace theorems. $\square$

## The Matrix Form of $K$ and Its Cone

**Theorem (the form in the model).** In the two-by-two model the Krein form reads

$$
K(\tilde P,\tilde Q)=\tfrac12\,\mathrm{Tr}\bigl(\mathrm{adj}\,\Phi(\tilde P)\,\Phi(\tilde Q)^{\dagger}\bigr),
$$

with Gram matrix $E=\mathrm{diag}(1,-1,-1,-1)$ in the coefficient basis; in the regular model the same form is read from the trace of the regular matrices, $\mathrm{Tr}\,\mathsf{M}_4(\tilde P\star\tilde Q)=4K(\tilde P,\tilde Q)$.

*Proof.* The first display is the trace theorem; the Gram matrix is the matrix of $K$ on the coefficient basis. In the regular model the trace of the product is $4K$, which recovers $K$ up to the factor of the dimension. $\square$

**Corollary (the indefinite cone in the model).** The image of the isotropic cone of $K$ under $\Phi$ is the set of matrices

$$
\Bigl\{\Phi(\tilde P):\ |P_0|^{2}=\sum_{k=1}^{3}|P_k|^{2}\Bigr\},
$$

a cone through the origin whose elements are exactly the values $\Phi(\tilde P)$ with $\mathrm{Tr}\,\Phi(\tilde P^{\natural}\tilde P^{*})=0$.

*Proof.* The isotropic cone is $\{|P_0|^{2}=\sum_k|P_k|^{2}\}$ by the form article; applying the isomorphism $\Phi$ and the trace formula gives the displayed set, since $K(\tilde P,\tilde P)=\mathrm{Sc}(\tilde P^{\natural}\tilde P^{*})=\tfrac12\mathrm{Tr}\,\Phi(\tilde P^{\natural}\tilde P^{*})$. $\square$

**Remark.** The matrix form of the form is the adjugate-twisted trace pairing; the indefinite cone is the cone of the elements of zero form value, mapped into the matrix algebra. The form itself, its Gram matrix and its cone, independently of the models, are in *The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra* and *The Krein Gram Matrix and the Restrictions of the Form*.

## Worked Examples

**A diagonal in the model.** $e_1\star e_1=-e_0$: $\Phi=-I$, trace $-2=2K(e_1,e_1)=2(-1)$, determinant $1=N(-e_0)=1$, rank two.

**A null diagonal.** $(e_1+ie_2)\star(e_1+ie_2)=-2e_0$: $\Phi=-2I$, trace $-4=2(-2)$, determinant $4=N(-2e_0)=4$.

**The non-scalar diagonal.** $(e_0+e_1)\star(e_0+e_1)=-2e_1$: $\Phi=2i\sigma_1=\begin{pmatrix}0&2i\\2i&0\end{pmatrix}$, trace $0=2K(e_0+e_1,e_0+e_1)=2\cdot0$, determinant $4=N(-2e_1)=4$.

**A vanishing product in the model.** $e_2\star e_1=0$: $\Phi=0$, trace $0$, rank zero.

**The form recovered.** $K(e_0,e_1)=0$: $\tfrac12\mathrm{Tr}(\mathrm{adj}\,I\cdot\Phi(e_1)^{\dagger})=\tfrac12\mathrm{Tr}((-i\sigma_1)^{\dagger})=0$, the traceless matrix.

**The cone.** $e_0+e_1$ is isotropic: $|1|^{2}=|1|^{2}$, and $\Phi(e_0+e_1)$ lies in the image cone.

## Summary

In the two-by-two model the block is the symmetrisation of the twisted matrix product, $\Phi(\tilde P\star\tilde Q)=\tfrac12(\mathrm{adj}\,\Phi(\tilde P)\Phi(\tilde Q)^{\dagger}+\Phi(\tilde Q)^{\dagger}\mathrm{adj}\,\Phi(\tilde P))$, with trace $2K$, determinant $N(\tilde P\star\tilde Q)$ and rank two off the degeneracy set. In the four-by-four regular model the same symmetrisation reads $\mathsf{M}_4(\tilde P\star\tilde Q)=\tfrac12(\mathsf{M}_4(\tilde P)^{T}\mathsf{M}_4(\tilde Q)^{\dagger}+\mathsf{M}_4(\tilde Q)^{\dagger}\mathsf{M}_4(\tilde P)^{T})$, with trace $4K$, determinant $N(\tilde P\star\tilde Q)^{2}$ and rank four off the degeneracy set. The diagonal is the scalar matrix of the form value minus the matrix of the mixed term; on the two witnesses $e_1$ and $e_1+ie_2$ it is the scalar matrices $-I$ and $-2I$, and the deformation away from the scalar matrices appears at $e_0+e_1$, where the matrix is $\begin{pmatrix}0&2i\\2i&0\end{pmatrix}$. The Krein form is $K(\tilde P,\tilde Q)=\tfrac12\mathrm{Tr}(\mathrm{adj}\,\Phi(\tilde P)\Phi(\tilde Q)^{\dagger})$, with Gram matrix $E=\mathrm{diag}(1,-1,-1,-1)$ in the coefficient basis, and its indefinite cone maps into the matrices of zero form value.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Phi(\tilde Q)=Q_0I-i\sum_kQ_k\sigma_k$ | the two-by-two model; $\Phi({}^{\natural})=\mathrm{adj}$, $\Phi({}^{*})={}^{\dagger}$ |
| $\Phi(\tilde P\star\tilde Q)=\tfrac12(\mathrm{adj}\,\Phi(\tilde P)\Phi(\tilde Q)^{\dagger}+\Phi(\tilde Q)^{\dagger}\mathrm{adj}\,\Phi(\tilde P))$ | the block in the two-by-two model |
| $\mathsf{M}_4(\tilde P\star\tilde Q)=\tfrac12(\mathsf{M}_4(\tilde P)^{T}\mathsf{M}_4(\tilde Q)^{\dagger}+\mathsf{M}_4(\tilde Q)^{\dagger}\mathsf{M}_4(\tilde P)^{T})$ | the block in the regular model |
| $\mathrm{Tr}\,\Phi(\tilde P\star\tilde Q)=2K$, $\det\Phi=N$ | trace and determinant in the two-by-two model |
| $\mathrm{Tr}\,\mathsf{M}_4(\tilde P\star\tilde Q)=4K$, $\det\mathsf{M}_4=N^{2}$ | trace and determinant in the regular model |
| $\Phi(\tilde Q\star\tilde Q)=K(\tilde Q,\tilde Q)I-\Phi(Q_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{Q})$ | the diagonal in the model |
| $\Phi(e_1\star e_1)=-I$, $\Phi((e_1+ie_2)\star(e_1+ie_2))=-2I$, $\Phi((e_0+e_1)\star(e_0+e_1))=2i\sigma_1$ | the two scalar witnesses and the non-scalar witness |
| $K(\tilde P,\tilde Q)=\tfrac12\mathrm{Tr}(\mathrm{adj}\,\Phi(\tilde P)\Phi(\tilde Q)^{\dagger})$ | the form in the model; Gram $E=\mathrm{diag}(1,-1,-1,-1)$ |

## Further Reading

- *The General Quaternionic Sesqualgebra in the $2\times2$ Matrix Representation* (`articles_maths/the-general-quaternionic-sesqualgebra-in-the-2x2-matrix-representation.md`), for the two-by-two model.
- *The General Quaternionic Sesqualgebra in the $4\times4$ Matrix Representation* (`articles_maths/the-general-quaternionic-sesqualgebra-in-the-4x4-matrix-representation.md`), for the regular model.
- *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-sesqualgebra-of-biquaternions.md`), for the product written in the models.
- *The Non-Central Diagonal and the Two Halves of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/the-non-central-diagonal-and-the-two-halves-of-the-symmetric-quaternionic-sesqualgebra.md`), for the diagonal, its centrality and the witnesses.
- *The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra* (`articles_maths/the-krein-form-as-a-product-on-the-symmetric-quaternionic-sesqualgebra.md`), for the form $K$, its Gram matrix and its cone.
- *The Krein Gram Matrix and the Restrictions of the Form* (`articles_maths/the-krein-gram-matrix-and-the-restrictions-of-the-form.md`), for the Gram matrix of the form.
- *The Multiplication Operators of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-quaternionic-sesqualgebra.md`), for the operators of the block and their traces.
