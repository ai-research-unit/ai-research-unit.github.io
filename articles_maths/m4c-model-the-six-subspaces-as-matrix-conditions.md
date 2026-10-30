# __$M_4(\mathbb{C})$ Model : The Six Subspaces as Matrix Conditions__

## Introduction

The six remarkable subspaces of the biquaternion algebra are the fixed and anti-fixed spaces of the four conjugations and the two halves of the scalar–vector split. In the regular model each becomes an entrywise matrix condition: scalar, traceless, real, purely imaginary, Hermitian, anti-Hermitian. The conditions are exact only inside the four-dimensional image; the ambient matrix algebra is much larger, and this is the main difference from the $2\times2$ model.

This article collects the six descriptions, their dimensions, traces and determinants. It is the $4\times4$ counterpart of *$M_2(\mathbb{C})$ Model : The Six Subspaces as Matrix Conditions*.

**Conventions.** The algebra and the model are those of *$M_4(\mathbb{C})$ Model : The Product, the Trace and the Determinant*. Write $Q_\mu=q_\mu+iq'_\mu$ with $q_\mu,q'_\mu$ real. The four involutions are
$$
\tilde Q^{\natural}=Q_t-\vec Q,\qquad
\overline{\tilde Q}=\overline{Q_t}+\overline{\vec Q},\qquad
\tilde Q^{*}=\overline{\tilde Q^{\natural}},\qquad
\tilde Q^{\flat}=-\tilde Q^{*}.
$$

**Boundaries.** The subspaces are defined in *The Six Subspaces*; the four forms restricted to them are *Remarkable Subspaces and the Four General Products, Forms and Norms*; the trace and determinant are *$M_4(\mathbb{C})$ Representation : Trace, Determinant and the Biquaternion Norm*; the $2\times2$ version is *$M_2(\mathbb{C})$ Model : The Six Subspaces as Matrix Conditions*.

**Frame.** This article uses the coefficient basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$, because that is the basis in which quaternion conjugation is transposition: $\mathsf M_4^{L}(\tilde Q^{\natural})=M^{\mathsf T}$. The canonical frame of *Conventions in Mathematics*, §*The Matrix Models*, is the Peirce frame, where $\mathsf M_4^{L}(\tilde Q)=I_2\otimes\mathsf M_2(\tilde Q)$; the two displays differ by the change $S$ of *The Product, the Trace and the Determinant*. In the canonical frame the same involution is $M\mapsto C\,M^{\mathsf T}\,C^{-1}$ with $C=R_y=-i\sigma_2\otimes\mathrm I_2$.

## The Table

The table gives the condition on a matrix $M=\mathsf{M}_4^{L}(\tilde Q)$ **inside the image** $M_4(\mathbb{C})_{\mathbb{B},L}$, the real dimension of the subspace, and the determinant of the $2\times2$ image.

| Subspace | Defining condition | Condition on $M$ in the image | Real dim. | Trace | $\det\mathsf{M}_2(\tilde Q)$ |
|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $\tilde Q^{\natural}=\tilde Q$ | $M=\lambda\mathrm I_4$ | $2$ | $4Q_t$ | $Q_t^2$ |
| $\mathrm{Vect}(\mathbb{B})$ | $\tilde Q^{\natural}=-\tilde Q$ | $\operatorname{Tr}M=0$ | $6$ | $0$ | $B^2$ |
| $\mathbb{H}_{\mathbb{B}}$ | $\overline{\tilde Q}=\tilde Q$ | $M=\overline M$ | $4$ | $4q_t$ | $\sum q_\mu^2$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $\overline{\tilde Q}=-\tilde Q$ | $M=-\overline M$ | $4$ | $4iq'_t$ | $-\sum(q'_\mu)^2$ |
| $\mathbb{M}_+$ | $\tilde Q^{*}=\tilde Q$ | $M=M^{\dagger}$ | $4$ | $4q_t$ | $q_t^2-\lvert\vec q'\rvert^2$ |
| $\mathbb{M}_-$ | $\tilde Q^{\flat}=\tilde Q$ | $M=-M^{\dagger}$ | $4$ | $4iq'_t$ | $-(q'_t)^2+\lvert\vec q\rvert^2$ |

The determinant of $M$ is the square of the determinant of the $2\times2$ image on every row, so it is a quartic on the subspace. The table records the quadratic determinant $\det\mathsf{M}_2(\tilde Q)=Q_t^2+B^2$ of the $2\times2$ image, whose sign is read directly.

**The warning.** The conditions in the third column are not sufficient in the ambient $M_4(\mathbb{C})$. The Hermitian matrices alone form a real space of dimension $16$, not $4$; the real matrices alone form a real space of dimension $16$, not $4$. The six subspaces are the intersections of those conditions with the image, and the dimensions in the table are the dimensions of the intersections. In the $2\times2$ model the image is all of $M_2(\mathbb{C})$, so no warning is needed; in the regular model it is essential.

## The Centre Subspace

**The scalar matrices.**

$$
\mathsf{M}_4^{L}(Q_te_t)=Q_t\mathrm I_4,
\qquad
\operatorname{Tr}M=4Q_t,
\qquad
\det M=Q_t^4.
$$

The image is the complex line of scalar matrices, of real dimension two. It is the only commutative subspace and the only one of real dimension two. It meets $\mathbb{M}_+$ in the real line $\mathbb{R}\mathrm I_4$ and $\mathbb{M}_-$ in the imaginary line $i\mathbb{R}\mathrm I_4$.

## The Vector Subspace

**The traceless matrices.**

$$
\operatorname{Tr}M=4Q_t=0
\iff
Q_t=0.
$$

The condition is equivalent, inside the image, to skew-symmetry:
$$
\operatorname{Tr}M=0
\iff
M^{\mathsf T}=-M,
$$
because the transpose is quaternion conjugation and $Q^{\natural}=-Q$ exactly when $Q_t=0$. The image is the three-dimensional complex space of regular matrices with zero scalar part, of real dimension six. It is closed under the commutator and not under the product.

**The two chiral halves.** The three matrices $\mathsf{M}_4^{L}(\vec e_k)$ are real and skew-symmetric. They span a three-dimensional subspace of the six-dimensional space of complex skew matrices, one of the two chiral halves of $\mathfrak{so}_4(\mathbb{C})$. The other half is not in the image. This is the regular analogue of the traceless matrices being all of $\mathfrak{sl}_2(\mathbb{C})$: in $M_4(\mathbb{C})$ the traceless condition alone is fifteen-dimensional, and the image selects a three-dimensional subspace.

## The Quaternion Subspace

**The real matrices.**
$$
\mathsf{M}_4^{L}(\tilde Q)=\overline{\mathsf{M}_4^{L}(\tilde Q)}
\iff
Q_\mu\in\mathbb{R}\ \text{for all }\mu.
$$
The image is the space of real matrices of the regular form, of real dimension four. It is closed under multiplication and is a division algebra.

**The trace and the determinant.** On the quaternion subspace the trace is $4q_t$, real, and the determinant of the $2\times2$ image is the sum $\sum q_\mu^2$, non-negative, and zero only at the origin.

**The contrast with $2\times2$.** In the $2\times2$ model the quaternion subspace is the conjugate-linear pattern $\begin{pmatrix}z&w\\-\bar w&\bar z\end{pmatrix}$, not the real matrices. In the regular model complex conjugation is entrywise, so the pattern disappears and the condition becomes realness of all entries. The price is that the image is only four real-dimensional.

## The Anti-Quaternion Subspace

**The purely imaginary matrices.**
$$
\mathsf{M}_4^{L}(\tilde Q)=-\overline{\mathsf{M}_4^{L}(\tilde Q)}
\iff
Q_\mu\in i\mathbb{R}\ \text{for all }\mu.
$$
The image is the space of purely imaginary matrices of the regular form, of real dimension four. It is not closed under multiplication: the product of two purely imaginary matrices is real.

**The trace and the determinant.** On the anti-quaternion subspace the trace is $4iq'_t$, purely imaginary, and the determinant of the $2\times2$ image is $-\sum(q'_\mu)^2$, non-positive, and zero only at the origin.

## The Hermitian Subspace

**The Hermitian matrices.**
$$
\mathsf{M}_4^{L}(\tilde Q)^{\dagger}=\mathsf{M}_4^{L}(\tilde Q)
\iff
\tilde Q^{*}=\tilde Q.
$$
The image is the space of Hermitian matrices of the regular form, of real dimension four. The trace is real on it, and the determinant of the $2\times2$ image takes both signs.

## The Anti-Hermitian Subspace

**The anti-Hermitian matrices.**
$$
\mathsf{M}_4^{L}(\tilde Q)^{\dagger}=-\mathsf{M}_4^{L}(\tilde Q)
\iff
\tilde Q^{*}=-\tilde Q.
$$
The image is the space of anti-Hermitian matrices of the regular form, of real dimension four. The trace is purely imaginary on it, and the determinant of the $2\times2$ image takes both signs, opposite to the Hermitian determinant.

**The warning repeated.** The ambient Hermitian matrices are sixteen real-dimensional; the image of $\mathbb{M}_+$ is the four-dimensional subspace of Hermitian matrices of the form $\mathsf{M}_4^{L}(\tilde Q)$ with $\tilde Q^{*}=\tilde Q$. The distinction is the regular analogue of the fact that a general $2\times2$ Hermitian matrix need not be of the form $\mathsf{M}_2(\tilde Q)$; there the image is everything, here it is not.

## How They Fit Together

**The three splits.**

$$
\mathbb{B}=\mathbb{C}_{\mathbb{B}}\oplus\mathrm{Vect}(\mathbb{B})
=\mathbb{H}_{\mathbb{B}}\oplus i\mathbb{H}_{\mathbb{B}}
=\mathbb{M}_+\oplus\mathbb{M}_-.
$$

The first is the trace decomposition, of real dimensions two and six. The second and the third are four-plus-four, and neither refines the other.

**The intersections.** The centre meets $\mathbb{M}_+$ in $\mathbb{R}e_t$ and $\mathbb{M}_-$ in $i\mathbb{R}e_t$. The vector subspace meets $\mathbb{H}_{\mathbb{B}}$ in the pure quaternions, of real dimension three, and $i\mathbb{H}_{\mathbb{B}}$ in the pure anti-quaternions. It meets $\mathbb{M}_+$ in $i$ times the real vector space, and $\mathbb{M}_-$ in the real vector space. The quaternion and anti-quaternion subspaces meet only at the origin, and so do the Hermitian and anti-Hermitian subspaces.

**The subalgebras.** The centre and the quaternion subspace are subalgebras; the vector subspace is a Lie subalgebra; the anti-quaternion subspace and the two Hermitian subspaces are neither. The statements are read from the matrix conditions and from the closure of the corresponding coefficient conditions.

**The real structure.** The regular model is a complex model, and it displays the two as the Hermitian and the anti-Hermitian matrices. They are not isomorphic: their determinants have opposite signs, and multiplication by $i$ exchanges them.

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
- [$M_4(\mathbb{C})$ Representation : The Conjugations and the Adjoints](m4c-representation-the-conjugations-and-the-adjoints.html), for the matrix involutions
- [$M_4(\mathbb{C})$ Representation : Trace, Determinant and the Biquaternion Norm](m4c-representation-trace-determinant-and-the-biquaternion-norm.html), for the determinant
- [$M_2(\mathbb{C})$ Model : The Six Subspaces as Matrix Conditions](m2c-model-the-six-subspaces-as-matrix-conditions.html), for the $2\times2$ version
