# __$M_2(\mathbb{C})$ Model : The Spectral Projectors__

## Introduction

A spectrally regular biquaternion has two distinct eigenvalues, and the matrix model turns its spectral decomposition into a pair of complementary rank-one projectors. The projectors are polynomials in the matrix, their columns are the eigenvectors, and the two mixed Peirce elements are the nilpotents that complete the eigenbasis.

This article develops the projectors and the nilpotents in the matrix model. It is the matrix form of *The Spectrally Regular Sector and Eigenbasis of a Biquaternion in Matrix Element Representations*, §*The Eigenprojections in the Model*, and it uses the eigenbasis of *$M_2(\mathbb{C})$ Model : The Eigenbasis and the Diagonalising Matrix*.

**Conventions.** The algebra and the model are those of *$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant*. The element is $\tilde Q=Q_te_t+\vec Q$, $B^2=Q_x^2+Q_y^2+Q_z^2\neq0$, and $B$ is a chosen square root. The eigenvalues are $\lambda_\pm=Q_t\pm iB$. The spectral direction is

$$
\vec\Xi=-\frac{i}{B}\vec Q,\qquad
\tilde\Pi_\pm=\tfrac12(e_t\pm\vec\Xi),
$$

and $\rho_\pm=\mathsf{M}_2(\tilde\Pi_\pm)$.

**Boundaries.** The spectral criterion is *The Spectrum*; the eigenbasis construction is *The Eigenbasis of a Spectrally Regular Biquaternion*; the diagonalising matrix is *$M_2(\mathbb{C})$ Model : The Eigenbasis and the Diagonalising Matrix*; the nilpotent cone is *Nilpotents*; the 4×4 spectral representation remains in *The Spectrally Regular Sector and Eigenbasis of a Biquaternion in Matrix Element Representations*.

## The Spectral Projectors

**Definition.** The two spectral projectors are

$$
\rho_+=\tfrac12\big(\mathrm I_2+\mathsf{M}_2(\vec\Xi)\big),\qquad
\rho_-=\tfrac12\big(\mathrm I_2-\mathsf{M}_2(\vec\Xi)\big).
$$

With $\vec\Xi=-i\vec Q/B$, the matrix of $\vec\Xi$ is

$$
\mathsf{M}_2(\vec\Xi)=\frac1B
\begin{pmatrix}
-Q_z&-Q_x+iQ_y\\
-Q_x-iQ_y&Q_z
\end{pmatrix},
$$

so the projectors are

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

**Proposition.** The matrices $\rho_\pm$ are idempotents of rank one and trace one, they are complementary, and they commute with $M=\mathsf{M}_2(\tilde Q)$:

$$
\rho_+^2=\rho_+,\quad
\rho_-^2=\rho_-,\quad
\rho_+\rho_-=0,\quad
\rho_++\rho_-=\mathrm I_2,\quad
\operatorname{Tr}\rho_\pm=1,\quad
\det\rho_\pm=0.
$$

*Proof.* The element $\vec\Xi$ has square $-\vec Q^2/B^2=e_t$, because $\vec Q^2=-B^2 e_t$; so $\tilde\Pi_\pm^2=\tilde\Pi_\pm$ and $\tilde\Pi_+\tilde\Pi_-=0$. Applying the algebra isomorphism gives the four identities. The trace of $\rho_\pm$ is $\tfrac12(2\pm0)=1$, and an idempotent of trace one has rank one. The commutation follows from

$$
M=Q_t\mathrm I_2+iB\,\mathsf{M}_2(\vec\Xi),
$$

which exhibits $M$ as a polynomial in $\mathsf{M}_2(\vec\Xi)$.

**Not Hermitian in general.** For a general complex element the projectors are not Hermitian: $\rho_\pm^{\dagger}$ is the projector of the conjugate direction. They are Hermitian exactly when $\vec\Xi$ is Hermitian; in particular this holds when the element lies in the Hermitian or the anti-Hermitian subspace. The distinction is the matrix form of the fact that the spectral projectors of a complex element are not orthogonal projectors.

**The eigenvector columns.** Since $M\rho_+=\lambda_+\rho_+$ and $M\rho_-=\lambda_-\rho_-$, every nonzero column of $\rho_+$ is an eigenvector for $\lambda_+$, and every nonzero column of $\rho_-$ is an eigenvector for $\lambda_-$. The first column of $\rho_+$ is

$$
\frac{1}{2B}\begin{pmatrix}B-Q_z\\-Q_x-iQ_y\end{pmatrix},
$$

and the second column of $\rho_-$ is

$$
\frac{1}{2B}\begin{pmatrix}Q_x-iQ_y\\B-Q_z\end{pmatrix}.
$$

When $B=Q_z$ the relation $B^2=Q_z^2+Q_x^2+Q_y^2$ forces $Q_x=Q_y=0$; both displayed columns then vanish, and the first chart of the diagonalising matrix degenerates. The second chart is used on that axis.

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
=\tfrac12(\lambda_++\lambda_-)\mathrm I_2+\tfrac12(\lambda_+-\lambda_-)\mathsf{M}_2(\vec\Xi)
=Q_t\mathrm I_2+iB\,\mathsf{M}_2(\vec\Xi)=M.
$$

**The invariants.** Taking the trace and the determinant,

$$
\operatorname{Tr}M=\lambda_++\lambda_-=2Q_t,\qquad
\det M=\lambda_+\lambda_-=Q_t^2+B^2=N.
$$

The decomposition is the spectral theorem for a matrix with distinct eigenvalues, written in the two projectors. The projectors are the Lagrange interpolating polynomials of the two eigenvalues:

$$
\rho_+=\frac{M-\lambda_-\mathrm I_2}{\lambda_+-\lambda_-},\qquad
\rho_-=\frac{M-\lambda_+\mathrm I_2}{\lambda_--\lambda_+}.
$$

**The spectral idempotents in the algebra.** The projectors are the images of $\tilde\Pi_\pm=\tfrac12(e_t\pm\vec\Xi)$. These are the two idempotents attached to the spectral direction. They satisfy $\tilde\Pi_++\tilde\Pi_-=e_t$ and $\tilde\Pi_\pm^2=\tilde\Pi_\pm$; they are not Hermitian unless $\vec\Xi$ is Hermitian, and they are not the standard pair unless $\vec\Xi=\pm i\vec e_z$.

**The eigenvalues as a pair.** The two eigenvalues are exchanged by $B\mapsto-B$. The projectors are exchanged at the same time, so the decomposition $M=\lambda_+\rho_++\lambda_-\rho_-$ is unchanged by the relabelling. The choice of $B$ is a choice of which projector is called $+$; the pair is unordered.

## The Nilpotents

**Definition.** Let $\mathsf C_Q$ be the diagonalising matrix of *$M_2(\mathbb{C})$ Model : The Eigenbasis and the Diagonalising Matrix*. The two spectral nilpotents are

$$
N_-=\mathsf C_QE_{12}\mathsf C_Q^{-1},\qquad
N_+=\mathsf C_QE_{21}\mathsf C_Q^{-1}.
$$

They are the images of the two mixed Peirce elements $\vec\Upsilon_-$ and $\vec\Upsilon_+$ of the eigenbasis.

**Proposition.** The two matrices are nonzero, square-zero, trace-zero, determinant-zero, of rank one, and they satisfy the Peirce relations

$$
N_-N_+=\rho_+,\qquad
N_+N_-=\rho_-,\qquad
\rho_+N_-=N_-=N_-\rho_-,\qquad
\rho_-N_+=N_+=N_+\rho_+.
$$

*Proof.* Conjugation carries the matrix-unit relations $E_{12}^2=E_{21}^2=0$, $E_{12}E_{21}=E_{11}$, $E_{21}E_{12}=E_{22}$ to the stated relations, and it carries $E_{11},E_{22}$ to $\rho_+,\rho_-$. Trace and determinant are conjugation-invariant; the rank is one because the matrices are nonzero and square-zero in dimension two.

**The explicit matrices.** In the fixed model the nilpotents are the conjugates of the off-diagonal units by $\mathsf C_Q$. The conjugation is the change from the standard eigenbasis to the spectral one, and it is the reason the nilpotents are not simply $E_{12}$ and $E_{21}$: the spectral eigenbasis is not the standard one unless the element points along the $z$-axis. The general closed form in the coefficients is given in *The Eigenbasis of a Spectrally Regular Biquaternion*, §*The Nilpotent Pair*.

**The Jordan form.** A nonzero nilpotent of $M_2(\mathbb{C})$ is conjugate to the Jordan block $\begin{pmatrix}0&1\\0&0\end{pmatrix}$. The two nilpotents $N_\pm$ are therefore conjugate to each other and to the two standard off-diagonal units; the labels $+$ and $-$ record which mixed corner they occupy, not a conjugacy class. The nilpotent is the matrix form of the spectral-degenerate part of the element: it is the off-diagonal entry that appears when the two eigenvalues coalesce.

**The resolvent.** For $z$ outside the spectrum,

$$
(z\mathrm I_2-M)^{-1}=\frac{\rho_+}{z-\lambda_+}+\frac{\rho_-}{z-\lambda_-}.
$$

At a coalescence the two simple poles merge. For $M=\lambda\mathrm I_2+N$ with $N^2=0$ the resolvent is

$$
(z\mathrm I_2-M)^{-1}=\frac{\mathrm I_2}{z-\lambda}+\frac{N}{(z-\lambda)^2},
$$

so the coefficient of the double pole is the nilpotent. The nilpotent is the residue of the merged pole, and the statement is the matrix form of the Jordan decomposition.

## The Projectors as Residues

**The signed projector.** The difference of the two projectors is the image of the spectral direction:

$$
\rho_+-\rho_-=\mathsf M_2(\vec\Xi)=-\frac{i}{B}\mathsf M_2(\vec Q),
$$

because $\rho_\pm=\tfrac12(\mathrm I_2\pm\mathsf M_2(\vec\Xi))$. The spectral resolution is therefore

$$
M=Q_t\mathrm I_2+iB\,(\rho_+-\rho_-),
$$

the scalar part carried by the identity and the vector part by the signed projector.

**The contour integral.** For a small positively oriented circle $\gamma_\pm$ around $\lambda_\pm$ enclosing no other eigenvalue,

$$
\rho_\pm=\frac{1}{2\pi i}\oint_{\gamma_\pm}(z\mathrm I_2-M)^{-1}\,dz .
$$

The residue of the resolvent at $z=\lambda_\pm$ is $\rho_\pm$, by the partial-fraction decomposition of the preceding paragraph. The Lagrange polynomials and the contour integral are the same projector, read algebraically and analytically.

## The Standard Axis

**The case $\vec Q\parallel\vec e_z$.** Take $\vec Q=Q_z\vec e_z$ and $B=Q_z$. Then

$$
\vec\Xi=-i\vec e_z,\qquad
\tilde\Pi_+=\tfrac12(e_t-i\vec e_z)=\tilde\Pi_-^{(\mathrm{std})},\qquad
\tilde\Pi_-=\tfrac12(e_t+i\vec e_z)=\tilde\Pi_+^{(\mathrm{std})},
$$

so the spectral projectors are the two diagonal matrix units, exchanged with respect to the standard labels:

$$
\rho_+=E_{22},\qquad\rho_-=E_{11},
\qquad
N_-=E_{21},\qquad N_+=E_{12}.
$$

The element is diagonal in the fixed model, and the spectral decomposition is the entry-by-entry decomposition. The exchange of the labels is the choice $B=Q_z$; the choice $B=-Q_z$ gives the same pair exchanged back.

**The case $\vec Q=0$.** The element is scalar, $M=Q_t\mathrm I_2$. The spectral direction is undefined, the two eigenvalues coincide, and every projector is a spectral projector. The decomposition is not unique, and the article's construction does not apply. The scalar element is the centre of the algebra, and its spectral theory is trivial.

**The degenerate cone.** For $B=0$ and $\vec Q\neq0$ the two eigenvalues coincide and the matrix is $Q_t\mathrm I_2+N$ with $N$ nilpotent. There is no pair of complementary rank-one spectral projectors: the only spectral projector is $\mathrm I_2$, and the nilpotent is not a difference of two projectors. The construction of this article therefore stops on the cone, and the spectral theory of the cone is the Jordan theory of *Nilpotents*.

**The directional limit.** If $\vec Q\to0$ along a fixed direction, the projectors $\rho_\pm$ tend to a pair of rank-one projectors depending on that direction, while $M\to Q_t\mathrm I_2$. The limit pair is not the spectral pair of the limit matrix, because the limit matrix is scalar and has no preferred pair. The discontinuity is the matrix form of the fact that the spectral decomposition is not continuous at the vertex.

## Summary

For a spectrally regular element the two spectral projectors are $\rho_\pm=\tfrac12(\mathrm I_2\pm\mathsf{M}_2(\vec\Xi))$ with $\vec\Xi=-i\vec Q/B$. They are complementary rank-one idempotents of trace one, they commute with $M$, and $M=\lambda_+\rho_++\lambda_-\rho_-$ with $\lambda_\pm=Q_t\pm iB$. The two spectral nilpotents are the conjugates of the off-diagonal matrix units; they are square-zero, rank one, and satisfy $N_-N_+=\rho_+$ and $N_+N_-=\rho_-$. On the standard axis the projectors are the diagonal units and the nilpotents the off-diagonal units, with the labels exchanged. On the cone the construction fails: the eigenvalues coalesce and the spectral projectors do not exist.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\vec\Xi=-i\vec Q/B$ | the spectral direction |
| $\tilde\Pi_\pm=\tfrac12(e_t\pm\vec\Xi)$ | the spectral idempotents |
| $\rho_\pm=\tfrac12(\mathrm I_2\pm\mathsf{M}_2(\vec\Xi))$ | the spectral projectors |
| $\lambda_\pm=Q_t\pm iB$ | the eigenvalues |
| $N_-=\mathsf C_QE_{12}\mathsf C_Q^{-1}$ | the image of $\vec\Upsilon_-$ |
| $N_+=\mathsf C_QE_{21}\mathsf C_Q^{-1}$ | the image of $\vec\Upsilon_+$ |
| $\mathsf C_Q$ | the diagonalising matrix |

## Further Reading

- [The Eigenbasis of a Spectrally Regular Biquaternion](the-eigenbasis-of-a-spectrally-regular-biquaternion.html), for the construction of the eigenbasis and the nilpotents
- [The Spectrum](the-spectrum.html), for the criterion
- [$M_2(\mathbb{C})$ Model : The Eigenbasis and the Diagonalising Matrix](m2c-model-the-eigenbasis-and-the-diagonalising-matrix.html), for the matrix $\mathsf C_Q$
- [Nilpotents](nilpotents.html), for the nilpotent cone
- [$M_2(\mathbb{C})$ Representation : Trace, Determinant and the Biquaternion Norm](m2c-representation-trace-determinant-and-the-biquaternion-norm.html), for the characteristic polynomial
- [$M_4(\mathbb{C})$ Model : The Eigenbasis and the Diagonalising Matrix](m4c-model-the-eigenbasis-and-the-diagonalising-matrix.html), for the 4×4 spectral representation
