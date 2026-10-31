# __Matrix Representations : The Spectral Projectors__

## Introduction

A spectrally regular biquaternion has two distinct eigenvalues, and its matrix has two complementary spectral projectors. In the $2\times2$ model the projectors have rank one and trace one, and their columns are eigenvectors. In the $4\times4$ regular model the same projectors are inflated, $\rho_\pm^{(4)}=I_2\otimes\rho_\pm^{(2)}$, so they have rank two and trace two, and each eigenspace is a plane. The eigenvalues themselves are the same in the two displays, each repeated twice in the regular one.

This article develops the spectral idempotents, the projectors in the two displays, the spectral decomposition, the eigenspaces, the nilpotents, the residues, the standard axis and the degeneration on the cone.

**Conventions.** The algebra and the models are those of *Matrix Representations : The Models and the Change of Frame*. The element is $\tilde Q=Q_te_t+\vec Q$, with $B^2=Q_x^2+Q_y^2+Q_z^2\neq0$ and a chosen square root $B$. The spectral direction is
$$
\vec\Xi=-\frac{i}{B}\vec Q,
\qquad
\tilde\Pi_\pm=\tfrac12(e_t\pm\vec\Xi),
\qquad
\lambda_\pm=Q_t\pm iB.
$$
The projectors are $\rho_\pm=\mathsf M_2(\tilde\Pi_\pm)$ in the $2\times2$ display and $\rho_\pm^{(4)}=\mathsf M_4^L(\tilde\Pi_\pm)$ in the $4\times4$ display.

**Boundaries.** The spectral criterion is *The Spectrum*; the eigenbasis and the nilpotents are *The Eigenbasis of a Spectrally Regular Biquaternion*; the diagonalising matrix is *Matrix Representations : The Eigenbasis and the Diagonalising Matrix*; the degenerate cone is *Matrix Representations : Rank-One Matrices and the Determinantal Variety*; the Jordan theory of the cone is *Nilpotents*.

## The Spectral Idempotents

**The direction.** The vector part has square $\vec Q^2=-B^2e_t$, so
$$
\vec\Xi^2=-\frac{1}{B^2}\vec Q^2=e_t.
$$
The elements
$$
\tilde\Pi_\pm=\tfrac12(e_t\pm\vec\Xi)
$$
are therefore idempotent, complementary and orthogonal:
$$
\tilde\Pi_+^2=\tilde\Pi_+,\qquad
\tilde\Pi_-^2=\tilde\Pi_-,\qquad
\tilde\Pi_+\tilde\Pi_-=0,\qquad
\tilde\Pi_++\tilde\Pi_-=e_t.
$$
They are not Hermitian unless $\vec\Xi$ is Hermitian, and they are not the standard pair unless $\vec\Xi=\pm i\vec e_z$.

**The spectral form.** The element is
$$
\tilde Q=Q_te_t+iB\vec\Xi=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-,
\qquad
\lambda_\pm=Q_t\pm iB.
$$
The two eigenvalues are exchanged by $B\mapsto-B$, and the two idempotents are exchanged at the same time; the pair is unordered.

## The Projectors in the Two Displays

**The definition.** The projectors are the images of the spectral idempotents:
$$
\rho_\pm=\tfrac12\bigl(\mathrm I_2\pm\mathsf M_2(\vec\Xi)\bigr),
\qquad
\rho_\pm^{(4)}=\tfrac12\bigl(\mathrm I_4\pm\mathsf M_4^L(\vec\Xi)\bigr).
$$
Because $\mathsf M_4^L(\vec\Xi)=I_2\otimes\mathsf M_2(\vec\Xi)$,
$$
\rho_\pm^{(4)}=I_2\otimes\rho_\pm=\operatorname{diag}(\rho_\pm,\rho_\pm).
$$
The regular projectors are the inflation of the $2\times2$ ones.

**The $2\times2$ entries.** With $\vec\Xi=-i\vec Q/B$,
$$
\mathsf M_2(\vec\Xi)=\frac1B
\begin{pmatrix}
-Q_z&-Q_x+iQ_y\\
-Q_x-iQ_y&Q_z
\end{pmatrix},
$$
so
$$
\rho_+=\frac{1}{2B}
\begin{pmatrix}
B-Q_z&-Q_x+iQ_y\\
-Q_x-iQ_y&B+Q_z
\end{pmatrix},
\qquad
\rho_-=\frac{1}{2B}
\begin{pmatrix}
B+Q_z&Q_x-iQ_y\\
Q_x+iQ_y&B-Q_z
\end{pmatrix}.
$$

**The proposition.** In the $2\times2$ display the projectors are idempotents of rank one and trace one; in the $4\times4$ display they are idempotents of rank two and trace two. In both,
$$
\rho_\pm^2=\rho_\pm,\qquad
\rho_+\rho_-=0,\qquad
\rho_++\rho_-=\mathrm I,\qquad
\rho_\pm M=M\rho_\pm.
$$
The commutation follows from
$$
M=Q_t\mathrm I+iB\,\mathsf M(\vec\Xi),
$$
which exhibits $M$ as a polynomial in $\mathsf M(\vec\Xi)$.

**Not Hermitian in general.** For a general complex element the projectors are not Hermitian: $\rho_\pm^{\dagger}$ is the projector of the conjugate direction. They are Hermitian exactly when $\vec\Xi$ is Hermitian, in particular when the element lies in the Hermitian or the anti-Hermitian subspace.

## The Spectral Decomposition

**The theorem.** For $B^2\neq0$,
$$
M=\lambda_+\rho_++\lambda_-\rho_-,
\qquad
\lambda_\pm=Q_t\pm iB.
$$

*Proof.* Expand the right side:
$$
\lambda_+\rho_++\lambda_-\rho_-
=\tfrac12(\lambda_++\lambda_-)\mathrm I+\tfrac12(\lambda_+-\lambda_-)\mathsf M(\vec\Xi)
=Q_t\mathrm I+iB\,\mathsf M(\vec\Xi)=M.
$$

**The invariants.** In the $2\times2$ display,
$$
\operatorname{Tr}_2M=2Q_t,
\qquad
\det M=Q_t^2+B^2=N.
$$
In the $4\times4$ display,
$$
\operatorname{Tr}_4M=2(\lambda_++\lambda_-)=4Q_t,
\qquad
\det M=(\lambda_+\lambda_-)^2=N^2.
$$
The factor two in the trace and the square in the determinant are the multiplicity of the spectrum: every eigenvalue is repeated once per spinor plane.

**The Lagrange form.**
$$
\rho_+=\frac{M-\lambda_-\mathrm I}{\lambda_+-\lambda_-},
\qquad
\rho_-=\frac{M-\lambda_+\mathrm I}{\lambda_--\lambda_+}.
$$
The projectors are polynomials in $M$ of degree one, and the formulas are the Lagrange interpolations of the two eigenvalues.

**The signed projector.**
$$
\rho_+-\rho_-=\mathsf M(\vec\Xi)=-\frac{i}{B}\mathsf M(\vec Q),
\qquad
M=Q_t\mathrm I+iB(\rho_+-\rho_-).
$$
The scalar part is carried by the identity and the vector part by the signed projector, with the same coefficients in the two displays.

## The Eigenspaces

**The column spaces.** Since $M\rho_+=\lambda_+\rho_+$, the column space of $\rho_+$ is contained in the eigenspace of $\lambda_+$. The dimension of the column space is the rank of $\rho_+$, which is one in the $2\times2$ display and two in the $4\times4$ display, and the dimension of the eigenspace is the same; the column space is therefore the whole eigenspace. The two eigenspaces are complementary. In the $2\times2$ display every nonzero column of $\rho_+$ is an eigenvector; in the $4\times4$ display the eigenspace is a plane.

**The spectral row.** The column space of $\rho_+$ is the right Peirce row
$$
\tilde\Pi_+^{\mathrm{spec}}\mathbb{B}
=\{\tilde\Pi_+^{\mathrm{spec}}X:X\in\mathbb{B}\},
$$
not the left ideal $\mathbb{B}\tilde\Pi_+^{\mathrm{spec}}$. The two are different planes: the left ideal is one of the two Peirce planes of *Matrix Representations : Peirce Coordinates, Matrix Units and the Spinor Planes*, while the right row meets each of the two blocks in one line. In the standard frame, for example, $\rho_+=\operatorname{diag}(E_{22},E_{22})$ has column space spanned by $\vec\Upsilon_+$ and $\tilde\Pi_-$, not by $\tilde\Pi_+$ and $\vec\Upsilon_+$. The distinction is the column-space caution of the Peirce article.

**The standard axis.** On the axis $\vec Q\parallel\vec e_z$ the spectral idempotents are the standard pair, exchanged, and the eigenspaces are the standard right Peirce rows, spanned by $(\vec\Upsilon_+,\tilde\Pi_-)$ and by $(\tilde\Pi_+,\vec\Upsilon_-)$. Off the axis the eigenspaces are two new planes, obtained from the standard ones by the diagonalising matrix.

## The Nilpotents

**The definition.** Let $\vec\Upsilon_\pm^{\mathrm{spec}}$ be the mixed Peirce elements of the spectral eigenbasis. Their images
$$
N_\pm=\mathsf M_4^L(\vec\Upsilon_\pm^{\mathrm{spec}})
$$
are the **spectral nilpotents** of the regular model; in the $2\times2$ display the same definition gives $N_\pm^{(2)}=\mathsf M_2(\vec\Upsilon_\pm^{\mathrm{spec}})$, and $N_\pm=I_2\otimes N_\pm^{(2)}$.

**The proposition.** The matrices are nonzero, square-zero and traceless; they have rank one in the $2\times2$ display and rank two in the $4\times4$ display, and they satisfy
$$
N_-N_+=\rho_+,\qquad
N_+N_-=\rho_-,\qquad
\rho_+N_-=N_-=N_-\rho_-,\qquad
\rho_-N_+=N_+=N_+\rho_+.
$$

*Proof.* Apply $\mathsf M$ to the Peirce relations of the spectral basis. The standard nilpotents are the off-diagonal units $E_{12}$ and $E_{21}$, respectively their inflations $I_2\otimes E_{12}$ and $I_2\otimes E_{21}$; the spectral ones are their conjugates by the diagonalising matrix, and rank, square-zero and trace are conjugation-invariant.

**The Jordan form.** A nonzero nilpotent of the regular image is conjugate to the direct sum of two Jordan blocks $\begin{pmatrix}0&1\\0&0\end{pmatrix}$. The two nilpotents are conjugate to each other; the labels record the mixed corner, not a conjugacy class. On the standard axis they are the off-diagonal units, with the labels exchanged.

## The Projectors as Residues

**The partial fractions.** For $z$ outside the spectrum,
$$
(z\mathrm I-M)^{-1}=\frac{\rho_+}{z-\lambda_+}+\frac{\rho_-}{z-\lambda_-}.
$$

**The merged pole.** For $M=\lambda\mathrm I+N$ with $N^2=0$,
$$
(z\mathrm I-M)^{-1}=\frac{\mathrm I}{z-\lambda}+\frac{N}{(z-\lambda)^2}.
$$
The coefficient of the double pole is the nilpotent. In the regular model the nilpotent has rank two, so the double pole carries a two-dimensional Jordan part in each of the two copies.

**The contour integral.** For a small positively oriented circle $\gamma_\pm$ around $\lambda_\pm$ enclosing no other eigenvalue,
$$
\rho_\pm=\frac{1}{2\pi i}\oint_{\gamma_\pm}(z\mathrm I-M)^{-1}\,dz.
$$
The residue of the resolvent at $z=\lambda_\pm$ is $\rho_\pm$, by the partial-fraction decomposition. The Lagrange polynomials and the contour integral are the same projector, read algebraically and analytically.

## The Standard Axis and the Cone

**The standard axis.** Take $\vec Q=Q_z\vec e_z$ and $B=Q_z$. Then
$$
\vec\Xi=-i\vec e_z,\qquad
\tilde\Pi_+=\tfrac12(e_t-i\vec e_z)=\tilde\Pi_-^{(\mathrm{std})},\qquad
\tilde\Pi_-=\tfrac12(e_t+i\vec e_z)=\tilde\Pi_+^{(\mathrm{std})}.
$$
The projectors are the diagonal units, exchanged with respect to the standard labels:
$$
\rho_+=E_{22},\qquad
\rho_-=E_{11},
\qquad
\rho_+^{(4)}=\operatorname{diag}(E_{22},E_{22}),\qquad
\rho_-^{(4)}=\operatorname{diag}(E_{11},E_{11}),
$$
and the nilpotents are the off-diagonal units, exchanged:
$$
N_-=E_{21},\quad N_+=E_{12},
\qquad
N_-^{(4)}=\operatorname{diag}(E_{21},E_{21}),\quad
N_+^{(4)}=\operatorname{diag}(E_{12},E_{12}).
$$
The element is diagonal in the fixed model, and the spectral decomposition is the entry-by-entry decomposition.

**The scalar case.** For $\vec Q=0$ the element is scalar, $M=Q_t\mathrm I$. The spectral direction is undefined, the eigenvalues coincide, and every projector is a spectral projector. The decomposition is not unique, and the construction of this article does not apply.

**The cone.** For $B=0$ and $\vec Q\neq0$ the two eigenvalues coincide and the matrix is $Q_t\mathrm I+N$ with $N$ a nonzero nilpotent, of rank one in the $2\times2$ display and rank two in the $4\times4$ display. There is no pair of complementary spectral projectors: the only spectral projector is $\mathrm I$, and the nilpotent is not a difference of two projectors. The spectral theory of the cone is the Jordan theory of *Nilpotents*.

**The directional limit.** If $\vec Q\to0$ along a fixed direction, the projectors $\rho_\pm$ tend to a pair of rank-one projectors depending on that direction, while $M\to Q_t\mathrm I$. The limit pair is not the spectral pair of the limit matrix, because the limit matrix is scalar and has no preferred pair. The discontinuity is the matrix form of the fact that the spectral decomposition is not continuous at the vertex.

## Summary

For a spectrally regular element the spectral projectors are $\rho_\pm=\tfrac12(\mathrm I\pm\mathsf M(\vec\Xi))$ with $\vec\Xi=-i\vec Q/B$. They are complementary idempotents of rank one and trace one in the $2\times2$ display, and their inflations $I_2\otimes\rho_\pm$ have rank two and trace two in the $4\times4$ display. They commute with $M$, and $M=\lambda_+\rho_++\lambda_-\rho_-$ with $\lambda_\pm=Q_t\pm iB$. The eigenspace of $\lambda_\pm$ is the right Peirce row of the spectral idempotent, not its left ideal. The spectral nilpotents are the inflations of the $2\times2$ ones; they are square-zero, of rank one or two, and satisfy $N_-N_+=\rho_+$ and $N_+N_-=\rho_-$. On the standard axis the projectors are the diagonal units and the nilpotents the off-diagonal units, with the labels exchanged. On the cone the construction fails.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\vec\Xi=-i\vec Q/B$ | the spectral direction |
| $\tilde\Pi_\pm=\tfrac12(e_t\pm\vec\Xi)$ | the spectral idempotents |
| $\rho_\pm=\mathsf M_2(\tilde\Pi_\pm)$ | the rank-one spectral projectors |
| $\rho_\pm^{(4)}=I_2\otimes\rho_\pm$ | the rank-two regular projectors |
| $\lambda_\pm=Q_t\pm iB$ | the eigenvalues, repeated twice in $4\times4$ |
| $N_\pm$, $N_\pm^{(4)}$ | the spectral nilpotents, of rank one or two |

## Further Reading

- [Matrix Representations : The Models and the Change of Frame](matrix-representations-the-models-and-the-change-of-frame.html), for the models and the inflation
- [Matrix Representations : Peirce Coordinates, Matrix Units and the Spinor Planes](matrix-representations-peirce-coordinates-matrix-units-and-the-spinor-planes.html), for the planes and the column-space caution
- *Matrix Representations : The Eigenbasis and the Diagonalising Matrix*, for the eigenbasis
- *Matrix Representations : Rank-One Matrices and the Determinantal Variety*, for the cone
- [The Eigenbasis of a Spectrally Regular Biquaternion](the-eigenbasis-of-a-spectrally-regular-biquaternion.html), for the construction
- [The Spectrum](the-spectrum.html), for the criterion
- [Nilpotents](nilpotents.html), for the nilpotent cone
- [$M_2(\mathbb{C})$ Representation : The Spectral Projectors](m2c-model-the-spectral-projectors.html), for the $2\times2$ source
- [$M_4(\mathbb{C})_{\mathbb{B}_L}$ Representation : The Spectral Projectors](m4c-model-the-spectral-projectors.html), for the $4\times4$ source
