# __Matrix Representations : The Six Subspaces as Matrix Conditions__

## Introduction

**The subject.** The six remarkable subspaces of the biquaternion algebra are the fixed and anti-fixed spaces of the four conjugations and the two halves of the scalar--vector split. This article writes each one as a condition on a matrix, in the $2\times2$ entry model and in the $4\times4$ operator model.

**What changes with the display.** In the $2\times2$ model the image is the whole of $M_2(\mathbb{C})$, so each condition characterises the subspace among all matrices. In the $4\times4$ model the image is a proper subalgebra of complex dimension four inside a sixteen-dimensional algebra, so each condition must be intersected with the image. In the block frame the $4\times4$ condition is a block condition, because $\mathsf M_4^{L}(\tilde Q)=\mathrm I_2\otimes\mathsf M_2(\tilde Q)$.

**The six conditions in one line.** Scalar, traceless, real, purely imaginary, Hermitian, anti-Hermitian: the six words are the same in both sizes, and only their scope changes.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ on $e_t,\vec e_x,\vec e_y,\vec e_z$, with $\vec e_k^2=-e_t$ and $\vec e_x\vec e_y=\vec e_z$. An element is $\tilde Q=Q_te_t+\vec Q$, with $Q_\mu=q_\mu+iq'_\mu$ and $q_\mu,q'_\mu$ real. The four involutions are
$$
\tilde Q^{\natural}=Q_t-\vec Q,\qquad
\overline{\tilde Q}=\overline{Q_t}+\overline{\vec Q},\qquad
\tilde Q^{*}=\overline{\tilde Q^{\natural}},\qquad
\tilde Q^{\flat}=-\tilde Q^{*}.
$$
The models and the frame change $C_{\Pi}$ are those of *Matrix Representations : The Models and the Change of Frame*.

**Boundaries.** The subspaces are defined in *The Six Subspaces*; their intersections are *The Subspaces and Their Relations*; the matrix conditions are the subject of this article.

## Common Aspects

The six remarkable subspaces are the fixed and anti-fixed spaces of the four conjugations and the two halves of the scalar–vector split. Each is a condition on the element, and the same six words survive every display: scalar, traceless, real, purely imaginary, Hermitian, anti-Hermitian. What changes is the scope of the condition. In the $2\times2$ model the image is the whole of $M_2(\mathbb{C})$, so the condition characterises the subspace among all matrices. In the $4\times4$ model the image is a four-complex-dimensional subalgebra of a sixteen-dimensional algebra, so every condition must be intersected with the image.

**The table.** The condition on the element, the image in the entry model, the condition on the regular matrix inside the image, and the real dimension:

| Subspace | Condition on the element | $2\times2$ image | Condition on $M=\mathsf M_4^{L}(\tilde Q)$ | Real dim. |
|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $\tilde Q^{\natural}=\tilde Q$ | scalar matrices | $M=\lambda\mathrm I_4$ | $2$ |
| $\mathrm{Vect}(\mathbb{B})$ | $\tilde Q^{\natural}=-\tilde Q$ | traceless matrices, $\mathfrak{sl}_2(\mathbb{C})$ | $\operatorname{Tr}M=0$ | $6$ |
| $\mathbb{H}_{\mathbb{B}}$ | $\overline{\tilde Q}=\tilde Q$ | $\begin{pmatrix}z&w\\-\bar w&\bar z\end{pmatrix}$ | $M=\overline M$ | $4$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $\overline{\tilde Q}=-\tilde Q$ | $i$ times the quaternion matrices | $M=-\overline M$ | $4$ |
| $\mathbb{M}_+$ | $\tilde Q^{*}=\tilde Q$ | Hermitian matrices | $M=M^{\dagger}$ | $4$ |
| $\mathbb{M}_-$ | $\tilde Q^{\flat}=\tilde Q$ | $i$ times Hermitian matrices | $M=-M^{\dagger}$ | $4$ |

**The determinants.** On the element, $\det\mathsf M_2(\tilde Q)=Q_t^2+B^2$ takes the values $Q_t^2$, $B^2$, $\lvert z\rvert^2+\lvert w\rvert^2$, $-\lvert z'\rvert^2-\lvert w'\rvert^2$, $q_t^2-\lvert\vec q'\rvert^2$ and $-(q'_t)^2+\lvert\vec q\rvert^2$ on the six rows. On the operator the determinant is the square of each value, because $\det\mathsf M_4^{L}=\det(\mathsf M_2)^2$.

**The warning.** The conditions in the fourth column are not sufficient in the ambient $M_4(\mathbb{C})$. The Hermitian matrices alone form a real space of dimension $16$, and the real matrices alone another; the six subspaces are the intersections of those conditions with the image. The dimensions in the table are the dimensions of the intersections. In the entry model the image is everything, so no warning is needed.

**The three splits.**

$$
\mathbb{B}=\mathbb{C}_{\mathbb{B}}\oplus\mathrm{Vect}(\mathbb{B})
=\mathbb{H}_{\mathbb{B}}\oplus i\mathbb{H}_{\mathbb{B}}
=\mathbb{M}_+\oplus\mathbb{M}_-.
$$

The first is the trace decomposition, of real dimensions two and six. The second and the third are four-plus-four, and neither refines the other. The centre meets $\mathbb{M}_+$ in $\mathbb{R}e_t$ and $\mathbb{M}_-$ in $i\mathbb{R}e_t$. The vector subspace meets $\mathbb{H}_{\mathbb{B}}$ in the pure quaternions, of real dimension three, and $i\mathbb{H}_{\mathbb{B}}$ in the pure anti-quaternions; it meets $\mathbb{M}_+$ in $i$ times the real vector space and $\mathbb{M}_-$ in the real vector space. The quaternion and anti-quaternion subspaces meet only at the origin, and so do the Hermitian and anti-Hermitian subspaces.

**The subalgebras.** The centre and the quaternion subspace are subalgebras; the vector subspace is a Lie subalgebra; the anti-quaternion subspace and the two Hermitian subspaces are neither. The statements are read from the matrix conditions and from the closure of the corresponding coefficient conditions.

## The Coefficient Frame

**The frame.** The coefficient frame is the frame in which ${}^{\natural}$ is transposition. The regular matrix of $\tilde Q$ is $L_{\tilde Q}=Q_t\mathrm I_4+Q_xL_x+Q_yL_y+Q_zL_z$, with $L_t=\mathrm I_4$ and the three real signed permutations of the product rule. The six conditions are therefore entry conditions: transposition, entrywise conjugation, and the adjoint.

**The scalar and the vector.** The centre is the line $M=\lambda\mathrm I_4$, of real dimension two, the only commutative subspace and the only one of real dimension two. The vector subspace is $\operatorname{Tr}M=0$, which inside the image is equivalent to $M^{\mathsf T}=-M$: the transpose is ${}^{\natural}$, and $Q^{\natural}=-Q$ exactly when $Q_t=0$. Its image is the three-complex-dimensional space of regular matrices with zero scalar part, of real dimension six. It is closed under the commutator and not under the product.

**The two halves of $\mathfrak{so}_4(\mathbb{C})$.** The three matrices $L_x,L_y,L_z$ are real and skew-symmetric. They span a three-dimensional subspace of the six-dimensional space of complex skew matrices, one of the two halves. The other half is not in the image. In $M_4(\mathbb{C})$ the traceless condition alone is fifteen-dimensional; the image selects a three-dimensional subspace, the regular analogue of the traceless matrices being all of $\mathfrak{sl}_2(\mathbb{C})$.

**The real and the imaginary.** Complex conjugation is entrywise in the coefficient frame, so $\mathbb{H}_{\mathbb{B}}$ is the set of regular matrices with real entries and $i\mathbb{H}_{\mathbb{B}}$ the set with purely imaginary entries. Both are four-real-dimensional. The first is closed under multiplication and is a division algebra; the second is not closed, because the product of two purely imaginary matrices is real. The trace is $4q_t$ on the first and $4iq'_t$ on the second; the determinant of the entry image is $\sum q_\mu^2$ on the first and $-\sum(q'_\mu)^2$ on the second, non-negative and non-positive respectively and zero only at the origin.

**The Hermitian pair.** $\mathbb{M}_+$ is $M=M^{\dagger}$ and $\mathbb{M}_-$ is $M=-M^{\dagger}$. Both are four-real-dimensional inside the image. The trace is real on the first and purely imaginary on the second. The determinants of the entry images take both signs, with opposite signs on the two subspaces. The ambient Hermitian matrices are sixteen-real-dimensional; the image is the four-dimensional subspace of those of the regular form, which is why the qualifier "inside the image" is part of the statement.

## The Entry Model

**The six sets.** In the entry model, whose standard basis is the matrix-unit basis, the six subspaces are:

$$
\begin{aligned}
\mathbb{C}_{\mathbb{B}} &: && M=\lambda\mathrm I_2,\\
\mathrm{Vect}(\mathbb{B}) &: && \operatorname{tr}M=0,\\
\mathbb{H}_{\mathbb{B}} &: && M=\begin{pmatrix}z&w\\-\bar w&\bar z\end{pmatrix},\\
i\mathbb{H}_{\mathbb{B}} &: && M=i\begin{pmatrix}z&w\\-\bar w&\bar z\end{pmatrix},\\
\mathbb{M}_+ &: && M=M^{\dagger},\\
\mathbb{M}_- &: && M=-M^{\dagger}.
\end{aligned}
$$

The entry model is an isomorphism onto $M_2(\mathbb{C})$, so each condition is exact among all matrices: the scalar matrices are the centre, the traceless matrices are $\mathfrak{sl}_2(\mathbb{C})$, and the quaternion pattern is the conjugate-linear form of the real quaternions. The two Hermitian halves are the usual Hermitian and anti-Hermitian matrices.

**The determinants.** On the six rows the determinant $Q_t^2+B^2$ takes the values $Q_t^2$, $B^2$, $\lvert z\rvert^2+\lvert w\rvert^2$, $-\lvert z'\rvert^2-\lvert w'\rvert^2$, $q_t^2-\lvert\vec q'\rvert^2$ and $-(q'_t)^2+\lvert\vec q\rvert^2$. The signs separate the four subspaces: the quaternion subspace has a non-negative determinant, the anti-quaternion subspace a non-positive one, and the two Hermitian subspaces take both signs.

## The Block Frame

**The block form.** In the block frame the regular matrix is $\mathrm I_2\otimes\mathsf M_2(\tilde Q)=\operatorname{diag}(B,B)$ with $B=\mathsf M_2(\tilde Q)$. Every condition of the entry model is imposed on $B$ and repeated twice: $B=\lambda\mathrm I_2$, $\operatorname{tr}B=0$, $B=\bar B$, $B=-\bar B$, $B=B^{\dagger}$, $B=-B^{\dagger}$. The carrier is two copies of the $2\times2$ space, and the two planes carry the same condition.

**The invariants.** The trace is twice the entry trace, $4Q_t$, and the determinant is the square of the entry determinant, $\langle\tilde Q\rangle_{\natural}^2$. The real dimensions are those of the entry model, because the block is repeated and adds no parameter: $2,6,4,4,4,4$.

**The two halves of $\mathfrak{so}_4(\mathbb{C})$.** The three matrices $\mathsf M_4^{L}(\vec e_k)$ act on each plane by the corresponding Pauli matrix and are block-diagonal. Their span is the diagonal copy of that half, and the other half of $\mathfrak{so}_4(\mathbb{C})$ is the off-diagonal copy, which is not in the left image. This is the block form of the statement that the image selects one half.

## Summary

The six subspaces are the scalar, traceless, real, purely imaginary, Hermitian and anti-Hermitian matrices of the regular image. Their real dimensions are $2,6,4,4,4,4$. The conditions are exact only inside the four-dimensional image; the ambient matrix algebra satisfies them on much larger sets.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $q_\mu,q'_\mu$ | real and imaginary parts of $Q_\mu$ |
| $\mathbb{C}_{\mathbb{B}},\mathrm{Vect}(\mathbb{B})$ | the centre and the vector subspace |
| $\mathbb{H}_{\mathbb{B}},i\mathbb{H}_{\mathbb{B}}$ | the quaternion and anti-quaternion subspaces |
| $\mathbb{M}_+,\mathbb{M}_-$ | the Hermitian and anti-Hermitian subspaces |

## Further Reading

- [The Six Subspaces](the-six-subspaces.html), for the definitions
- [The Subspaces and Their Relations](the-subspaces-and-their-relations.html), for the intersections