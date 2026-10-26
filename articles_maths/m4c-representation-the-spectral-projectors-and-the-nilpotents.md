# __$M_4(\mathbb{C})_L$ Representation : The Spectral Projectors and the Nilpotents__

## Introduction

A spectrally regular biquaternion has two distinct eigenvalues, and its regular matrix has two spectral projectors of rank two. The projectors are polynomials in the matrix, their column spaces are the two eigenspaces, and the mixed Peirce elements are the nilpotents that complete the eigenbasis. Every object is the doubled copy of its $2\times2$ analogue.

This article develops the projectors, the spectral decomposition, the nilpotents and the residue formula. It is the $4\times4$ counterpart of *$M_2(\mathbb{C})$ Representation : The Spectral Projectors and the Nilpotents*, and it absorbs the $4\times4$ spectral material of the former *The Spectrally Regular Sector and Eigenbasis of a Biquaternion in Matrix Element Representations*.

**Conventions.** The algebra and the model are those of *$M_4(\mathbb{C})_L$ Representation : The Matrix Product and the Algebra Structure*. The element is $\tilde Q=Q_te_t+\vec Q$, with $B^2=Q_x^2+Q_y^2+Q_z^2\neq0$ and a chosen square root $B$. The spectral direction is
$$
\vec\Xi=-\frac{i}{B}\vec Q,\qquad
\tilde\Pi_\pm=\tfrac12(e_t\pm\vec\Xi),\qquad
\lambda_\pm=Q_t\pm iB.
$$
The projectors are $\rho_\pm=\mathsf{M}_4(\tilde\Pi_\pm)$.

**Boundaries.** The spectral criterion is *Spectral Regularity and Degeneracy in the Biquaternion Algebra*; the construction of the eigenbasis and of the nilpotents is *The Spectrally Regular Sector and Construction of the Eigenbasis of a Biquaternion*; the diagonalising matrix is *$M_4(\mathbb{C})_L$ Representation : The Eigenbasis and the Diagonalising Matrix*; the degenerate cone is *$M_4(\mathbb{C})_L$ Representation : Rank-One Matrices and the Determinantal Variety*; the $2\times2$ version is *$M_2(\mathbb{C})$ Representation : The Spectral Projectors and the Nilpotents*.

## The Spectral Projectors

**Definition.**

$$
\rho_+=\tfrac12\bigl(\mathrm I_4+\mathsf{M}_4(\vec\Xi)\bigr),
\qquad
\rho_-=\tfrac12\bigl(\mathrm I_4-\mathsf{M}_4(\vec\Xi)\bigr).
$$

**Proposition.** The matrices $\rho_\pm$ are idempotents of rank two and trace two, they are complementary, and they commute with $M=\mathsf{M}_4(\tilde Q)$:
$$
\rho_+^2=\rho_+,\quad
\rho_-^2=\rho_-,\quad
\rho_+\rho_-=0,\quad
\rho_++\rho_-=\mathrm I_4,\quad
\operatorname{Tr}\rho_\pm=2.
$$

*Proof.* The element $\vec\Xi$ has square $e_t$, because $\vec Q^2=-B^2e_t$, so $\tilde\Pi_\pm^2=\tilde\Pi_\pm$ and $\tilde\Pi_+\tilde\Pi_-=0$. Applying the algebra homomorphism gives the four identities. The trace is $\tfrac12(4\pm0)=2$, and an idempotent of trace two has rank two. The commutation follows from
$$
M=Q_t\mathrm I_4+iB\,\mathsf{M}_4(\vec\Xi),
$$
which exhibits $M$ as a polynomial in $\mathsf{M}_4(\vec\Xi)$. $\square$

**Not Hermitian in general.** For a general complex element the projectors are not Hermitian: $\rho_\pm^{\dagger}$ is the projector of the conjugate direction. They are Hermitian exactly when $\vec\Xi$ is Hermitian, in particular when the element lies in the Hermitian or the anti-Hermitian subspace.

**The column spaces.** Since $M\rho_+=\lambda_+\rho_+$ and $M\rho_-=\lambda_-\rho_-$, the column space of $\rho_+$ is the eigenspace of $\lambda_+$, of dimension two, and the column space of $\rho_-$ is the eigenspace of $\lambda_-$, of dimension two. The two eigenspaces are complementary. In the Peirce basis they are the two coordinate planes $E_+$ and $E_-$ of *$M_4(\mathbb{C})_L$ Representation : The Columns, the Rows and the Spinor Module*.

## The Spectral Decomposition

**Theorem.** For $B^2\neq0$,

$$
M=\lambda_+\rho_++\lambda_-\rho_-,
\qquad
\lambda_\pm=Q_t\pm iB.
$$

*Proof.* Expand the right side:
$$
\lambda_+\rho_++\lambda_-\rho_-
=\tfrac12(\lambda_++\lambda_-)\mathrm I_4+\tfrac12(\lambda_+-\lambda_-)\mathsf{M}_4(\vec\Xi)
=Q_t\mathrm I_4+iB\,\mathsf{M}_4(\vec\Xi)=M.
$$
$\square$

**The invariants.** Taking the trace and the determinant,
$$
\operatorname{Tr}M=2(\lambda_++\lambda_-)=4Q_t,
\qquad
\det M=(\lambda_+\lambda_-)^2=\bigl(Q_t^2+B^2\bigr)^2.
$$
The factor two in the trace and the square in the determinant are the multiplicity of the spectrum.

**The Lagrange form.**
$$
\rho_+=\frac{M-\lambda_-\mathrm I_4}{\lambda_+-\lambda_-},
\qquad
\rho_-=\frac{M-\lambda_+\mathrm I_4}{\lambda_--\lambda_+}.
$$
The formulas are the images of the $2\times2$ Lagrange polynomials, and they show that the projectors are polynomials in $M$ of degree one.

**The signed projector.**
$$
\rho_+-\rho_-=\mathsf{M}_4(\vec\Xi)=-\frac{i}{B}\mathsf{M}_4(\vec Q),
\qquad
M=Q_t\mathrm I_4+iB(\rho_+-\rho_-).
$$
The scalar part is carried by the identity and the vector part by the signed projector, exactly as in the $2\times2$ model, with the same coefficients.

## The Nilpotents

**Definition.** Let $\vec\Upsilon_\pm^{\mathrm{spec}}$ be the spectral nilpotents of the algebra, the mixed Peirce elements of the eigenbasis. Their images
$$
N_-=\mathsf{M}_4(\vec\Upsilon_-^{\mathrm{spec}}),\qquad
N_+=\mathsf{M}_4(\vec\Upsilon_+^{\mathrm{spec}})
$$
are the **spectral nilpotents** of the regular model.

**Proposition.** The two matrices are nonzero, square-zero, trace-zero, of rank two, and satisfy the Peirce relations
$$
N_-N_+=\rho_+,\qquad
N_+N_-=\rho_-,\qquad
\rho_+N_-=N_-=N_-\rho_-,\qquad
\rho_-N_+=N_+=N_+\rho_+.
$$

*Proof.* Apply $\mathsf{M}_4$ to the Peirce relations of the algebra. The rank is two because in the Peirce basis the matrix is the doubled off-diagonal unit $\operatorname{diag}(E_{12},E_{12})$ or $\operatorname{diag}(E_{21},E_{21})$. $\square$

**The Jordan form.** A nonzero nilpotent of the regular image is conjugate to the direct sum of two Jordan blocks $\begin{pmatrix}0&1\\0&0\end{pmatrix}$. The two nilpotents $N_\pm$ are conjugate to each other and to the doubled off-diagonal units; the labels record the mixed corner, not a conjugacy class. The nilpotent is the off-diagonal entry that survives when the two eigenvalues coalesce.

**The explicit matrices.** In the fixed Peirce basis the nilpotents are the doubled off-diagonal units:
$$
S^{-1}N_-S=\operatorname{diag}(E_{12},E_{12}),
\qquad
S^{-1}N_+S=\operatorname{diag}(E_{21},E_{21}).
$$
For a general element they are the conjugates of these by the $4\times4$ diagonalising matrix, and their entries are the same as the $2\times2$ entries, repeated in the two blocks.

## The Projectors as Residues

**The partial fractions.** For $z$ outside the spectrum,
$$
(z\mathrm I_4-M)^{-1}=\frac{\rho_+}{z-\lambda_+}+\frac{\rho_-}{z-\lambda_-}.
$$

**The merged pole.** For $M=\lambda\mathrm I_4+N$ with $N^2=0$,
$$
(z\mathrm I_4-M)^{-1}=\frac{\mathrm I_4}{z-\lambda}+\frac{N}{(z-\lambda)^2}.
$$
The coefficient of the double pole is the nilpotent. In the regular model the nilpotent has rank two and the double pole therefore carries a two-dimensional Jordan part in each of the two copies.

**The contour integral.** For a small positively oriented circle $\gamma_\pm$ around $\lambda_\pm$ enclosing no other eigenvalue,
$$
\rho_\pm=\frac{1}{2\pi i}\oint_{\gamma_\pm}(z\mathrm I_4-M)^{-1}\,dz.
$$
The residue of the resolvent at $z=\lambda_\pm$ is $\rho_\pm$, by the partial-fraction decomposition. The Lagrange polynomials and the contour integral are the same projector, read algebraically and analytically.

## The Standard Axis

**The case $\vec Q\parallel\vec e_z$.** Take $\vec Q=Q_z\vec e_z$ and $B=Q_z$. Then
$$
\vec\Xi=-i\vec e_z,\qquad
\tilde\Pi_+=\tfrac12(e_t-i\vec e_z)=\tilde\Pi_-^{(\mathrm{std})},\qquad
\tilde\Pi_-=\tfrac12(e_t+i\vec e_z)=\tilde\Pi_+^{(\mathrm{std})}.
$$
The spectral projectors are the doubled diagonal units,
$$
\rho_+=S\operatorname{diag}(E_{22},E_{22})S^{-1},\qquad
\rho_-=S\operatorname{diag}(E_{11},E_{11})S^{-1},
$$
and the nilpotents are the doubled off-diagonal units with the labels exchanged. The element is diagonal in the fixed model, and the spectral decomposition is the entry-by-entry decomposition.

**The scalar case.** For $\vec Q=0$ the element is scalar, $M=Q_t\mathrm I_4$. The spectral direction is undefined, the four eigenvalues coincide, and the spectral projector of the single eigenvalue is $\mathrm I_4$. The decomposition $M=\lambda P+\lambda(\mathrm I_4-P)$ is not unique, and the construction of this article does not apply.

**The degenerate cone.** For $B=0$ and $\vec Q\neq0$ the two eigenvalues coincide and the matrix is $Q_t\mathrm I_4+N$ with $N$ nilpotent of rank two. There is no pair of complementary rank-two spectral projectors: the only spectral projector is $\mathrm I_4$, and the nilpotent is not a difference of two projectors. The spectral theory of the cone is the Jordan theory of *Square Roots of Zero and the Nilpotents of the Biquaternion Algebra*.

**The directional limit.** If $\vec Q\to0$ along a fixed direction, the projectors $\rho_\pm$ tend to a pair of rank-two projectors depending on that direction, while $M\to Q_t\mathrm I_4$. The limit pair is not the spectral pair of the limit matrix, because the limit matrix is scalar and has no preferred pair. The discontinuity is the matrix form of the fact that the spectral decomposition is not continuous at the vertex.

## Summary

For a spectrally regular element the two spectral projectors are $\rho_\pm=\tfrac12(\mathrm I_4\pm\mathsf{M}_4(\vec\Xi))$ with $\vec\Xi=-i\vec Q/B$. They are complementary rank-two idempotents of trace two, they commute with $M$, and $M=\lambda_+\rho_++\lambda_-\rho_-$ with $\lambda_\pm=Q_t\pm iB$. The two spectral nilpotents are the doubled off-diagonal units; they are square-zero, rank two, and satisfy $N_-N_+=\rho_+$ and $N_+N_-=\rho_-$. On the standard axis the projectors are the doubled diagonal units and the nilpotents the doubled off-diagonal units, with the labels exchanged. On the cone the construction fails.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\vec\Xi=-i\vec Q/B$ | the spectral direction |
| $\tilde\Pi_\pm=\tfrac12(e_t\pm\vec\Xi)$ | the spectral idempotents |
| $\rho_\pm=\mathsf{M}_4(\tilde\Pi_\pm)$ | the rank-two spectral projectors |
| $\lambda_\pm=Q_t\pm iB$ | the eigenvalues, each double |
| $N_\pm$ | the rank-two spectral nilpotents |
| $S$ | the Peirce change |

## Further Reading

- [$M_4(\mathbb{C})_L$ Representation : The Eigenbasis and the Diagonalising Matrix](m4c-representation-the-eigenbasis-and-the-diagonalising-matrix.html), for the eigenbasis
- [$M_4(\mathbb{C})_L$ Representation : Rank-One Matrices and the Determinantal Variety](m4c-representation-rank-one-matrices-and-the-determinantal-variety.html), for the cone
- [$M_2(\mathbb{C})$ Representation : The Spectral Projectors and the Nilpotents](m2c-representation-the-spectral-projectors-and-the-nilpotents.html), for the $2\times2$ version
- [The Spectrally Regular Sector and Construction of the Eigenbasis of a Biquaternion](the-spectrally-regular-sector-and-construction-of-the-eigenbasis-of-a-biquaternion.html), for the construction
- [Square Roots of Zero and the Nilpotents of the Biquaternion Algebra](square-roots-of-zero-and-the-nilpotents-of-the-biquaternion-algebra.html), for the nilpotent cone
