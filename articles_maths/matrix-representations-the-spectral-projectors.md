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

**Boundaries.** The spectral criterion and the spectral basis are *The Spectrum*; the degenerate cone is the zero-divisor cone of *Zero Divisors and Units*; the nilpotent theory of the cone is *Nilpotents*.

## Common Aspects

A spectrally regular biquaternion has two distinct eigenvalues, and its matrix has two complementary spectral projectors. The construction is the same in every display: choose the spectral direction, build the two idempotents, and map them. The rank and the trace of the projectors change with the display, because the regular model carries each eigenvalue twice.

**The spectral idempotents.** Let $\tilde Q=Q_te_t+\vec Q$ with $B^2=Q_x^2+Q_y^2+Q_z^2\neq0$ and a chosen square root $B$, and set
$$
\vec\Xi=-\frac{i}{B}\vec Q,
\qquad
\tilde\Pi_\pm=\tfrac12(e_t\pm\vec\Xi),
\qquad
\lambda_\pm=Q_t\pm iB.
$$
Since $\vec Q^2=-B^2e_t$, one has $\vec\Xi^2=e_t$, and the two elements are idempotent, complementary and orthogonal:
$$
\tilde\Pi_+^2=\tilde\Pi_+,\qquad
\tilde\Pi_-^2=\tilde\Pi_-,\qquad
\tilde\Pi_+\tilde\Pi_-=0,\qquad
\tilde\Pi_++\tilde\Pi_-=e_t.
$$
They are not Hermitian unless $\vec\Xi$ is Hermitian, and they are not the standard pair unless $\vec\Xi=\pm i\vec e_z$. The element is
$$
\tilde Q=Q_te_t+iB\vec\Xi=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-.
$$
The two eigenvalues are exchanged by $B\mapsto-B$, and the two idempotents are exchanged at the same time; the pair is unordered.

**The spectral decomposition.** For $B^2\neq0$,
$$
M=\lambda_+\rho_++\lambda_-\rho_-,
\qquad
\rho_\pm=\mathsf M(\tilde\Pi_\pm).
$$
The proof is the expansion
$$
\lambda_+\rho_++\lambda_-\rho_-
=\tfrac12(\lambda_++\lambda_-)\mathrm I+\tfrac12(\lambda_+-\lambda_-)\mathsf M(\vec\Xi)
=Q_t\mathrm I+iB\,\mathsf M(\vec\Xi)=M.
$$
The projectors commute with $M$, because $M=Q_t\mathrm I+iB\,\mathsf M(\vec\Xi)$ is a polynomial in $\mathsf M(\vec\Xi)$. In Lagrange form,
$$
\rho_+=\frac{M-\lambda_-\mathrm I}{\lambda_+-\lambda_-},
\qquad
\rho_-=\frac{M-\lambda_+\mathrm I}{\lambda_--\lambda_+},
$$
and the signed projector is
$$
\rho_+-\rho_-=\mathsf M(\vec\Xi)=-\frac{i}{B}\mathsf M(\vec Q),
\qquad
M=Q_t\mathrm I+iB(\rho_+-\rho_-).
$$

**The invariants.** In the entry model $\operatorname{Tr}_2M=2Q_t$ and $\det M=Q_t^2+B^2$; in the regular model $\operatorname{Tr}_4M=4Q_t$ and $\det M=(Q_t^2+B^2)^2$. The factor two in the trace and the square in the determinant are the multiplicity of the spectrum: every eigenvalue is repeated once per spinor plane.

**The residues.** For $z$ outside the spectrum,
$$
(z\mathrm I-M)^{-1}=\frac{\rho_+}{z-\lambda_+}+\frac{\rho_-}{z-\lambda_-},
$$
and for $M=\lambda\mathrm I+N$ with $N^2=0$,
$$
(z\mathrm I-M)^{-1}=\frac{\mathrm I}{z-\lambda}+\frac{N}{(z-\lambda)^2}.
$$
The coefficient of the double pole is the nilpotent. For a small positively oriented circle $\gamma_\pm$ around $\lambda_\pm$ enclosing no other eigenvalue,
$$
\rho_\pm=\frac{1}{2\pi i}\oint_{\gamma_\pm}(z\mathrm I-M)^{-1}\,dz.
$$
The Lagrange polynomials and the contour integral are the same projector, read algebraically and analytically.

**The standard axis and the cone.** On the axis $\vec Q\parallel\vec e_z$ the spectral idempotents are the standard pair, exchanged, and the projectors are the diagonal units. For $\vec Q=0$ the element is scalar, the direction is undefined, and every projector is spectral: the decomposition is not unique. For $B=0$ and $\vec Q\neq0$ the two eigenvalues coincide and the matrix is $Q_t\mathrm I+N$ with $N$ a nonzero nilpotent; there is no pair of complementary spectral projectors, the only spectral projector is $\mathrm I$, and the nilpotent is not a difference of two projectors. If $\vec Q\to0$ along a fixed direction, the projectors tend to a pair of rank-one projectors depending on the direction, while $M\to Q_t\mathrm I$; the limit pair is not the spectral pair of the limit matrix, and the discontinuity is the matrix form of the failure of the spectral decomposition at the vertex.

## The Coefficient Frame

**The projectors.** The coefficient frame is real, so the projectors are
$$
\rho_\pm^{(4)}=\tfrac12\bigl(\mathrm I_4\pm\mathsf M_4^L(\vec\Xi)\bigr)
=\tfrac12\Bigl(\mathrm I_4\mp\frac{i}{B}\bigl(Q_xL_x+Q_yL_y+Q_zL_z\bigr)\Bigr).
$$
They are idempotents of rank two and trace two, complementary and orthogonal, and they commute with $M$. The rank is two because the regular representation carries two copies of the defining $2\times2$ space; the trace is two because each copy contributes one.

**The spectral nilpotents.** Let $\vec\Upsilon_\pm^{\mathrm{spec}}$ be the mixed Peirce elements of the spectral basis. Their images
$$
N_\pm=\mathsf M_4^L(\vec\Upsilon_\pm^{\mathrm{spec}})
$$
are the spectral nilpotents. They are nonzero, square-zero and traceless, of rank two, and they satisfy
$$
N_-N_+=\rho_+,\qquad
N_+N_-=\rho_-,\qquad
\rho_+N_-=N_-=N_-\rho_-,\qquad
\rho_-N_+=N_+=N_+\rho_+.
$$
The proof is the application of $\mathsf M_4^L$ to the Peirce relations of the spectral basis. A nonzero nilpotent of the regular image is conjugate to the direct sum of two square-zero blocks $\begin{pmatrix}0&1\\0&0\end{pmatrix}$; the two nilpotents are conjugate to each other, and the labels record the mixed corner, not a conjugacy class.

**The standard axis.** On the axis $\vec Q=Q_z\vec e_z$ and $B=Q_z$, the projectors are
$$
\rho_+^{(4)}=\operatorname{diag}(E_{22},E_{22}),
\qquad
\rho_-^{(4)}=\operatorname{diag}(E_{11},E_{11}),
$$
and the nilpotents are
$$
N_-^{(4)}=\operatorname{diag}(E_{21},E_{21}),
\qquad
N_+^{(4)}=\operatorname{diag}(E_{12},E_{12}),
$$
with the labels exchanged with respect to the standard pair. The element is diagonal in the fixed model, and the spectral decomposition is the entry-by-entry decomposition.

## The Entry Model

**The explicit projectors.** With $\vec\Xi=-i\vec Q/B$,
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

**The rank and the eigenspaces.** The projectors are idempotents of rank one and trace one:
$$
\rho_\pm^2=\rho_\pm,\qquad
\rho_+\rho_-=0,\qquad
\rho_++\rho_-=\mathrm I_2,\qquad
\rho_\pm M=M\rho_\pm.
$$
Since $M\rho_+=\lambda_+\rho_+$, the column space of $\rho_+$ is the whole eigenspace of $\lambda_+$, of dimension one; every nonzero column is an eigenvector. The two eigenspaces are complementary. The projectors are not Hermitian in general: $\rho_\pm^{\dagger}$ is the projector of the conjugate direction, and they are Hermitian exactly when $\vec\Xi$ is Hermitian, in particular on the Hermitian and anti-Hermitian subspaces.

**The nilpotents and the axis.** The spectral nilpotents are $N_\pm^{(2)}=\mathsf M_2(\vec\Upsilon_\pm^{\mathrm{spec}})$, of rank one and square-zero. On the standard axis they are the off-diagonal units $E_{12}$ and $E_{21}$, exchanged; on the cone a nonzero nilpotent is a single square-zero block of rank one.

## The Peirce Frame

**The inflation.** Because $\mathsf M_4^L(\vec\Xi)=\mathrm I_2\otimes\mathsf M_2(\vec\Xi)$,
$$
\rho_\pm^{(4)}=\mathrm I_2\otimes\rho_\pm=\operatorname{diag}(\rho_\pm,\rho_\pm).
$$
The regular projectors are the inflation of the entry projectors: rank two, trace two, and each eigenspace is a plane.

**The spectral row.** The column space of $\rho_+$ is the right Peirce row
$$
\tilde\Pi_+^{\mathrm{spec}}\mathbb{B}
=\{\tilde\Pi_+^{\mathrm{spec}}X:X\in\mathbb{B}\},
$$
not the left ideal $\mathbb{B}\tilde\Pi_+^{\mathrm{spec}}$. The two are different planes: the left ideal is one of the two Peirce planes, while the right row meets each of the two blocks in one line. In the standard frame, for example, $\rho_+=\operatorname{diag}(E_{22},E_{22})$ has column space spanned by $\vec\Upsilon_+$ and $\tilde\Pi_-$, not by $\tilde\Pi_+$ and $\vec\Upsilon_+$. The distinction is the column-space caution of the Peirce article.

**The nilpotents and the blocks.** The nilpotents are $N_\pm=\mathrm I_2\otimes N_\pm^{(2)}$, of rank two, square-zero and traceless, and their products are the projectors:
$$
N_-N_+=\rho_+,\qquad
N_+N_-=\rho_-.
$$
Each block carries one copy of the entry nilpotent, and the two copies are the two spinor planes.

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
- [The Spectrum](the-spectrum.html), for the criterion and the spectral basis
- [Nilpotents](nilpotents.html), for the nilpotent cone