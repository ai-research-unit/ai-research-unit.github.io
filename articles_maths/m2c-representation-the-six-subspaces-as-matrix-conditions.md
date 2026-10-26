# __$M_2(\mathbb{C})$ Representation : The Six Subspaces as Matrix Conditions__

## Introduction

The six remarkable subspaces of the biquaternion algebra are defined by the four conjugations and by the scalar–vector split. In the matrix model each definition becomes a matrix condition: the centre is the scalar matrices, the vector subspace is the traceless matrices, the quaternion subspace is a conjugate-linear pattern, the anti-quaternion subspace is $i$ times it, and the two sectors are the Hermitian and the anti-Hermitian matrices.

This article collects the six descriptions, their determinants and their signatures. It is the matrix form of *Introduction to the Remarkable Subspaces*, §*Remarkable Subspaces*, and of *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*, §*The Two Complex Subspaces and the Four Real-Type Subspaces*.

**Conventions.** The algebra and the model are those of *$M_2(\mathbb{C})$ Representation : The Matrix Product and the Algebra Structure*: $\tilde Q=Q_te_t+\vec Q$ with $Q_\mu=q_\mu+iq'_\mu$, the unprimed $q_\mu$ real and the primed $q'_\mu$ real. The conjugations are quaternion conjugation ${}^{\natural}$, complex conjugation $\bar{\cdot}$, Hermitian conjugation ${}^{*}$ and anti-Hermitian conjugation ${}^{\flat}=-{}^{*}$. The four matrix basis images are

$$
\mathsf{M}_2(e_t)=\mathrm I_2,\quad
\mathsf{M}_2(\vec e_x)=\begin{pmatrix}0&-i\\-i&0\end{pmatrix},\quad
\mathsf{M}_2(\vec e_y)=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad
\mathsf{M}_2(\vec e_z)=\begin{pmatrix}-i&0\\0&i\end{pmatrix}.
$$

**Boundaries.** The subspaces and their relations are *Introduction to the Remarkable Subspaces* and *Comparison of the Remarkable Subspaces*; the four forms restricted to them are *Remarkable Subspaces and the Four General Products, Forms and Norms*; the polar action on them is *The Polar Decomposition and Remarkable Subspaces*; the matrix form of that action is *The Sandwich in the $M_2(\mathbb{C})$ Model*.

## The Table

Every subspace is the image of the basis vectors listed in its row, with the real parameters substituted as in the last column.

| Subspace | Defining condition | Basis image | Image | Trace | Determinant | Real signature |
|---|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $\tilde Q^{\natural}=\tilde Q$ | $\mathsf{M}_2(e_t),i\mathsf{M}_2(e_t)$ | scalar matrices | $2Q_t$ | $Q_t^2$ | $(2,0)$ |
| $\mathrm{Vect}(\mathbb{B})$ | $\tilde Q^{\natural}=-\tilde Q$ | $\mathsf{M}_2(\vec e_k),i\mathsf{M}_2(\vec e_k)$ | traceless matrices | $0$ | $B^2$ | $(6,0)$ |
| $\mathbb{H}_{\mathbb{B}}$ | $\overline{\tilde Q}=\tilde Q$ | the four $\mathsf{M}_2(e_\mu)$ | $\begin{pmatrix}z&w\\-\bar w&\bar z\end{pmatrix}$ | $2q_t$ | $\lvert z\rvert^2+\lvert w\rvert^2$ | $(4,0)$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $\overline{\tilde Q}=-\tilde Q$ | $i\mathsf{M}_2(e_\mu)$ | $i$ times the quaternion matrices | $2iq'_t$ | $-\lvert z'\rvert^2-\lvert w'\rvert^2$ | $(0,4)$ |
| $\mathbb{M}_+$ | $\tilde Q^{*}=\tilde Q$ | $\mathsf{M}_2(e_t),i\mathsf{M}_2(\vec e_k)$ | Hermitian matrices | $2q_t$ | $q_t^2-\lvert\vec q'\rvert^2$ | $(1,3)$ |
| $\mathbb{M}_-$ | $\tilde Q^{\flat}=\tilde Q$ | $i\mathsf{M}_2(e_t),\mathsf{M}_2(\vec e_k)$ | $i$ times Hermitian matrices | $2iq'_t$ | $-(q'_t)^2+\lvert\vec q\rvert^2$ | $(3,1)$ |

The table is the matrix form of the six definitions. The two complex subspaces are of real dimension two and six; the four real-type subspaces are of real dimension four. The determinants are the quaternionic norm restricted to each subspace: complex-valued on the centre and the vector subspace, real on the four real-type subspaces. The last column is the signature of the Hermitian norm on the two complex subspaces, where the determinant has no signature, and the signature of the determinant on the four real-type subspaces.

## The Centre Subspace

**The fixed space of quaternion conjugation.**

$$
\mathsf{M}_2(Q_te_t)=Q_t\mathrm I_2=\begin{pmatrix}Q_t&0\\0&Q_t\end{pmatrix}
=\begin{pmatrix}q_t+iq'_t&0\\0&q_t+iq'_t\end{pmatrix}.
$$

The image is the line of scalar matrices, of complex dimension one. The trace is $2Q_t$ and the determinant is $Q_t^2$; the norm is the square of the scalar, and it vanishes exactly at the origin. The subspace is the only commutative one and the only one of real dimension two. Its two real parameters are the informational scalar $q_t$ and the material scalar $q'_t$.

**The intersection with the sectors.** The centre meets $\mathbb{M}_+$ in the real line $\mathbb{R}e_t$ and $\mathbb{M}_-$ in the imaginary line $\mathbb{R}(ie_t)$. The statement is the matrix form of the split of the centre into its Hermitian and anti-Hermitian parts.

## The Vector Subspace

**The traceless matrices.**

$$
\mathsf{M}_2(\tilde Q)=\begin{pmatrix}-iQ_z&-iQ_x-Q_y\\-iQ_x+Q_y&iQ_z\end{pmatrix},
\qquad \operatorname{Tr}\mathsf{M}_2(\tilde Q)=0.
$$

The image is $\mathfrak{sl}_2(\mathbb{C})$, the traceless matrices, of complex dimension three. Its determinant is

$$
\det\mathsf{M}_2(\tilde Q)=Q_x^2+Q_y^2+Q_z^2=B^2,
$$

the norm with the scalar term dropped. The subspace is the derived subspace $[\mathbb{B},\mathbb{B}]$ and is closed under the commutator; it is not closed under the product, because the product of two traceless matrices need not be traceless: for example $E_{12}E_{21}=E_{11}$ has trace one.

**The two blocks.** Writing $Q_k=q_k+iq'_k$, the real and imaginary parts of the vector subspace are the material and informational spatial blocks, $\mathrm{Vect}(\mathbb{B})=X_{\mathrm{m}}\oplus X_{\mathrm{i}}$. The statement is the matrix form of the split of the traceless matrices into the real and imaginary parts of their entries.

## The Quaternion Subspace

**The real coefficients.**

$$
\mathsf{M}_2(q_te_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z)
=\begin{pmatrix}q_t-iq_z&-iq_x-q_y\\-iq_x+q_y&q_t+iq_z\end{pmatrix}
=\begin{pmatrix}z&w\\-\bar w&\bar z\end{pmatrix},
$$

with $z=q_t-iq_z$ and $w=-iq_x-q_y$. The image is the set of matrices of the form $\begin{pmatrix}z&w\\-\bar w&\bar z\end{pmatrix}$, a complex-linear copy of $\mathbb{H}$ inside $M_2(\mathbb{C})$. The trace is $2q_t$, real, and the determinant is

$$
\det=|z|^2+|w|^2=q_t^2+q_x^2+q_y^2+q_z^2,
$$

positive definite. The subspace is closed under multiplication and is a division algebra: every nonzero element is invertible, with inverse the conjugate divided by the norm. The statement is the matrix form of the reality of the quaternion subspace.

**The conjugate-linear pattern.** The pattern $w\mapsto-\bar w$ is the matrix form of the quaternion conjugation: it is the unique conjugate-linear involution of $\mathbb{C}^2$ commuting with the left action. The quaternion subspace is the fixed space of complex conjugation, and its matrix image is the set of matrices commuting with that involution.

## The Anti-Quaternion Subspace

**The imaginary coefficients.**

$$
\mathsf{M}_2(iq'_te_t+iq'_x\vec e_x+iq'_y\vec e_y+iq'_z\vec e_z)
=i\begin{pmatrix}q'_t-iq'_z&-iq'_x-q'_y\\-iq'_x+q'_y&q'_t+iq'_z\end{pmatrix}.
$$

The image is $i$ times the quaternion matrices, and the determinant is

$$
\det=-\big((q'_t)^2+(q'_x)^2+(q'_y)^2+(q'_z)^2\big),
$$

negative definite. The subspace is not closed under multiplication. Together with the quaternion subspace it exhausts the algebra:

$$
\mathbb{B}=\mathbb{H}_{\mathbb{B}}\oplus i\mathbb{H}_{\mathbb{B}},
$$

the real-and-imaginary split, of two four-dimensional real summands.

**The mirror.** The two subspaces are exchanged by multiplication by the central $i$, and their determinants are opposite. The pair is the matrix form of the two real forms of the complex quaternion algebra: the division algebra and its imaginary multiple.

## The Informational Subspace

**The Hermitian matrices.**

$$
\mathsf{M}_2(q_te_t+iq'_x\vec e_x+iq'_y\vec e_y+iq'_z\vec e_z)
=\begin{pmatrix}q_t+q'_z&q'_x-iq'_y\\q'_x+iq'_y&q_t-q'_z\end{pmatrix}.
$$

The image is the set of Hermitian matrices, of real dimension four. The trace is $2q_t$, real, and the determinant is

$$
\det=q_t^2-(q'_x)^2-(q'_y)^2-(q'_z)^2,
$$

of signature $(1,3)$. The subspace is not closed under multiplication; it is closed under the anticommutator, and it is the operator space of a two-state system. The three non-identity basis images are the Pauli matrices:

$$
i\mathsf{M}_2(\vec e_x)=\sigma_1,\qquad
i\mathsf{M}_2(\vec e_y)=\sigma_2,\qquad
i\mathsf{M}_2(\vec e_z)=\sigma_3.
$$

**The positivity cone.** Inside the Hermitian subspace the positive semidefinite matrices are the observables with non-negative spectrum; the positive definite ones are the invertible observables; the rank-one ones are the pure states. The determinant is positive on the two positive cones and negative on the two negative cones, and the boundary is the null cone of the Minkowski form.

## The Material Subspace

**The anti-Hermitian matrices.**

$$
\mathsf{M}_2(iq'_te_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z)
=i\begin{pmatrix}q'_t-q_z&-q_x+iq_y\\-q_x-iq_y&q'_t+q_z\end{pmatrix}.
$$

The image is $i$ times the Hermitian matrices, of real dimension four. The trace is $2iq'_t$, purely imaginary, and the determinant is

$$
\det=-(q'_t)^2+q_x^2+q_y^2+q_z^2,
$$

of signature $(3,1)$. The subspace is not closed under multiplication; it is the Lie algebra of the unitary group under the commutator, and it is the carrier of the material sector.

**Why the material subspace is anti-Hermitian.** The determinant on a Hermitian matrix has signature $(1,3)$; on an anti-Hermitian matrix it has the opposite signature $(3,1)$. The material form is the one with the positive spatial part, and it is obtained by multiplying the Hermitian matrices by $i$. The factor $i$ is the matrix form of the statement that the material sector is the anti-Hermitian one.

## The Roots of Plus One and the Idempotents

**The roots of $+1$.** A matrix $X$ with $X^2=\mathrm I_2$ is diagonalisable with eigenvalues $\pm1$: it is a scalar involution $\pm\mathrm I_2$ when the eigenvalues agree, and a traceless involution when they differ. The six subspaces carry the following roots.

| Subspace | Roots of $+1$ |
|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $\pm\mathrm I_2$ |
| $\mathrm{Vect}(\mathbb{B})$ | the traceless involutions, $\operatorname{Tr}X=0$, $X^2=\mathrm I_2$ |
| $\mathbb{H}_{\mathbb{B}}$ | $\pm\mathrm I_2$ |
| $i\mathbb{H}_{\mathbb{B}}$ | the Hermitian traceless involutions $\vec u\cdot\vec\sigma$, $\lvert\vec u\rvert=1$ |
| $\mathbb{M}_+$ | $\pm\mathrm I_2$ and $\vec u\cdot\vec\sigma$, $\lvert\vec u\rvert=1$ |
| $\mathbb{M}_-$ | none |

The last row is immediate: an anti-Hermitian matrix has purely imaginary eigenvalues, so it cannot have the real eigenvalues $\pm1$. The table is the matrix form of the table of *Introduction to the Remarkable Subspaces*, §*The Roots of Zero and Plus One*.

**The idempotents.** A matrix $\Pi$ with $\Pi^2=\Pi$ is a projector; if it is not $0$ or $\mathrm I_2$, its rank is one. In the six subspaces the only nontrivial idempotents are

$$
\Pi(\vec u)=\tfrac12\bigl(\mathrm I_2+\vec u\cdot\vec\sigma\bigr),
\qquad \vec u\in\mathbb{R}^3,\quad\lvert\vec u\rvert=1,
$$

and they all lie in the Hermitian subspace $\mathbb{M}_+$. The centre and the quaternion subspace contain only $0$ and $\mathrm I_2$; the vector subspace, the anti-quaternion subspace and $\mathbb{M}_-$ contain only $0$. The family is the matrix form of the Hermitian idempotents $\tfrac12(e_t+i\vec u)$ of *Introduction to the Remarkable Subspaces*, §*The Idempotents and the Ideals in the Remarkable Subspaces*.

**The nilpotents.** The roots of $0$ are the nilpotents, and a nonzero nilpotent has trace zero and rank one. It lies in the vector subspace and on the null cone, and it lies in none of the other five subspaces except through the common origin. The idempotent and the nilpotent are the two ends of the rank-one variety: $\Pi^2=\Pi$ and $N^2=0$.

## How They Fit Together

**The three splits.**

$$
\mathbb{B}=\mathbb{C}_{\mathbb{B}}\oplus\mathrm{Vect}(\mathbb{B})
=\mathbb{H}_{\mathbb{B}}\oplus i\mathbb{H}_{\mathbb{B}}
=\mathbb{M}_+\oplus\mathbb{M}_-.
$$

The first is the trace decomposition, of dimensions two and six; the second and third are four-plus-four and neither refines the other. Each sector takes its scalar from one half and its vectors from the other: the prime pattern of $\mathbb{M}_+$ is one real scalar and three imaginary vectors, and that of $\mathbb{M}_-$ is one imaginary scalar and three real vectors.

**The subalgebras.** The centre is closed under multiplication; the vector subspace is closed under the commutator but not under the product; the quaternion subspace is closed under multiplication; the anti-quaternion subspace and the two sectors are closed under neither. The statements are the matrix forms of the corresponding algebra statements, and they are read off the images above.

**The involutions.** The six subspaces are the fixed and anti-fixed spaces of the four involutions: the centre and the vector subspace for ${}^{\natural}$; the quaternion and anti-quaternion subspaces for $\bar{\cdot}$; the two sectors for ${}^{*}$ and ${}^{\flat}$. The matrix images are the scalar, traceless, conjugate-linear-pattern, $i$-pattern, Hermitian and anti-Hermitian conditions. The table at the head of the article is the complete list.

**The real structure.** The matrix model is a complex model, and it does not by itself distinguish $\mathbb{M}_+$ from $\mathbb{M}_-$. The distinction is the choice of the real form ${}^{\flat}$, and the matrix model displays it as the choice between the Hermitian and the anti-Hermitian matrices. The statement is the matrix form of the fact that the two sectors are anti-isometric and not isomorphic.

## Summary

The six remarkable subspaces are the scalar matrices, the traceless matrices, the matrices of the form $\begin{pmatrix}z&w\\-\bar w&\bar z\end{pmatrix}$, $i$ times them, the Hermitian matrices and $i$ times the Hermitian matrices. Their determinants are $Q_t^2$, $B^2$, the positive definite quaternion norm, its negative, the form of signature $(1,3)$ and the form of signature $(3,1)$. The three splits are the trace decomposition and the two four-plus-four decompositions; the centre and the quaternion subspace are subalgebras, the vector subspace is a Lie subalgebra, and the sectors are neither.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $Q_\mu=q_\mu+iq'_\mu$ | complex coefficient and its two real parts |
| $\mathbb{C}_{\mathbb{B}}$ | the centre, the scalar matrices |
| $\mathrm{Vect}(\mathbb{B})$ | the vector subspace, the traceless matrices |
| $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$ | the quaternion and anti-quaternion subspaces |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | the Hermitian and anti-Hermitian subspaces |
| $\mathfrak{sl}_2(\mathbb{C})$ | the traceless matrices |
| $(1,3)$, $(3,1)$ | the signatures of the two sector determinants |

## Further Reading

- [Introduction to the Remarkable Subspaces](introduction-to-the-remarkable-subspaces.html), for the six subspaces and their definitions
- [Comparison of the Remarkable Subspaces](comparison-of-the-remarkable-subspaces.html), for the three splits and the intersections
- [Remarkable Subspaces and the Four General Products, Forms and Norms](remarkable-subspaces-and-the-four-general-products-forms-and-norms.html), for the forms restricted to the subspaces
- [The Polar Decomposition and Remarkable Subspaces](the-polar-decomposition-and-remarkable-subspaces.html), for the action on the subspaces
- [The Sandwich in the $M_2(\mathbb{C})$ Model](the-sandwich-in-the-m2c-model.html), for the matrix action on the two sectors
- [$M_2(\mathbb{C})$ Representation : Trace, Determinant and the Biquaternion Norm](m2c-representation-trace-determinant-and-the-biquaternion-norm.html), for the determinant
- [Comparison of the Remarkable Subspaces](comparison-of-the-remarkable-subspaces.html), for the material reading
