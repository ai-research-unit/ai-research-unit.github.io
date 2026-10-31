# __Matrix Representations : The Eigenbasis and the Diagonalising Matrix__

## Introduction

A spectrally regular biquaternion has two distinct eigenvalues, and its matrix can be put in diagonal form by a change of basis. The change is not the same object in the two displays. In the $2\times2$ model it is one matrix $\mathsf C_Q$, built from two eigenvectors. In the $4\times4$ regular model it is a matrix of four columns, two for each eigenvalue, and the two eigenvalues are repeated. The repetition is the only numerical difference: the $4\times4$ diagonalising matrix is the $2\times2$ one doubled inside each eigenspace.

This article develops the spectral matrix units, the diagonalising matrix in each display, the determinant of the change, its freedom, the normal case and the transitions between two elements. It is the regular counterpart of *Matrix Representations : The Jordan Basis and the Jordanising Matrix*.

**Conventions.** The algebra and the displays are those of *Matrix Representations : The Models and the Change of Frame*. The element is $\tilde Q=Q_te_t+\vec Q$ with $B^2=Q_x^2+Q_y^2+Q_z^2\neq0$, and $B$ is a chosen square root. The spectral direction is $\vec\Xi=-i\vec Q/B$, the spectral idempotents are $\tilde\Pi_\pm=\tfrac12(e_t\pm\vec\Xi)$, and the eigenvalues are
$$
\lambda_\pm=Q_t\pm iB.
$$
The eigenbasis is written in the corner order
$$
\mathcal E=(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-),
$$
where $\vec\Upsilon_-$ and $\vec\Upsilon_+$ are the two spectral nilpotents. This is the order in which the first and last elements are the corners and the two middle elements are mixed. The fixed Peirce basis of the corpus is the transposition of the two middle elements of $\mathcal E$.

**Boundaries.** The construction of the eigenbasis and of the nilpotents is *The Eigenbasis of a Spectrally Regular Biquaternion*; the projectors are *Matrix Representations : The Spectral Projectors*; the Peirce frame is *Matrix Representations : Peirce Coordinates, Matrix Units and the Spinor Planes*; the Jordan case is *Matrix Representations : The Jordan Basis and the Jordanising Matrix*; the normal matrices are *Eigenvalues and Diagonalisation*.

## Common Aspects

A spectrally regular biquaternion has two distinct eigenvalues, and its matrix can be put in diagonal form by a change of basis. The change is not the same object in the two displays: in the entry model it is one matrix $\mathsf C_Q$ built from two eigenvectors, while in the regular model it has four columns, two for each eigenvalue. The repetition is the only numerical difference; the regular change is the entry change doubled inside each eigenspace.

**The eigenbasis.** With $\vec\Xi=-i\vec Q/B$, $\tilde\Pi_\pm=\tfrac12(e_t\pm\vec\Xi)$ and $\lambda_\pm=Q_t\pm iB$, the eigenbasis is written in the corner order
$$
\mathcal E=(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-),
$$
where $\vec\Upsilon_-$ and $\vec\Upsilon_+$ are the two spectral nilpotents. The first and last elements are the corners and the two middle elements are mixed. The fixed Peirce basis of the corpus is the transposition of the two middle elements of $\mathcal E$.

**The spectral matrix units.** Let $E_{ij}$ be the ordinary $2\times2$ matrix units and $P_{ij}=\mathsf C_QE_{ij}\mathsf C_Q^{-1}$. The four matrices are a basis of $M_2(\mathbb{C})$ and multiply as the matrix units:
$$
P_{ij}P_{kl}=\delta_{jk}P_{il}.
$$
The correspondence is $P_{11}=\tilde\Pi_+$, $P_{12}=\vec\Upsilon_-$, $P_{21}=\vec\Upsilon_+$, $P_{22}=\tilde\Pi_-$: the diagonal elements are the spectral projectors and the off-diagonal elements the spectral nilpotents.

**The coordinate model.** Every element has a unique expansion
$$
\tilde X=\sum_{i,j=1}^{2}X_{ij}P_{ij},
\qquad
\mathsf M_2^{Q}(\tilde X)=\begin{pmatrix}X_{11}&X_{12}\\X_{21}&X_{22}\end{pmatrix}.
$$
The superscript records that the model depends on the element through $Q$. The map $\mathsf M_2^{Q}$ is an isomorphism, and for the element itself
$$
\mathsf M_2^{Q}(\tilde Q)=\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix},
\qquad
\mathsf M_4^{Q}(\tilde Q)=\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-),
$$
because left multiplication preserves each spinor plane and each eigenvalue is repeated once per plane. The coordinates are the trace pairings with the dual basis: in the corner order, with the two mixed elements exchanged in the dual,
$$
X_{11}=\operatorname{Tr}(\tilde\Pi_+\tilde X),\qquad
X_{12}=\operatorname{Tr}(\vec\Upsilon_+\tilde X),\qquad
X_{21}=\operatorname{Tr}(\vec\Upsilon_-\tilde X),\qquad
X_{22}=\operatorname{Tr}(\tilde\Pi_-\tilde X).
$$
In the regular model each trace pairing is doubled and the coordinate is half the $4\times4$ trace; $\operatorname{Tr}(\vec\Upsilon_-\vec\Upsilon_+)=1$ in the entry model and $2$ in the regular model.

**The freedom.** A diagonalising matrix is defined up to right multiplication by an invertible matrix commuting with the diagonal form. In the entry model this is $\operatorname{diag}(\mathbb{C}^{\times},\mathbb{C}^{\times})$, of complex dimension two: the two eigenvectors can be rescaled independently, and a scalar multiplies both. In the regular model with $\lambda_+\neq\lambda_-$, the commutant is
$$
C\bigl(\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-)\bigr)=GL_2(\mathbb{C})\times GL_2(\mathbb{C}),
$$
of complex dimension eight; the extra six parameters mix the two spinor planes inside one eigenspace. The determinant of the change is multiplied by the determinant of the commuting matrix, so only its vanishing and its rank are invariant.

**The normal case.** A matrix is normal when $XX^{\dagger}=X^{\dagger}X$. The element is normal exactly when its entry matrix is normal, because the regular matrix is $\mathrm I_2\otimes\mathsf M_2(\tilde Q)$ in the Peirce frame and the dagger acts on the second factor. In the algebra the condition is $[\vec Q,\bar{\vec Q}]=0$, that is, $\vec Q=\zeta\vec p$ with $\zeta\in\mathbb{C}$ and $\vec p\in\mathbb{R}^3$: the three components have a common phase. For a non-scalar normal element the spectral direction $\vec\Xi=-i\vec p/\lvert\vec p\rvert$ is pure imaginary, the spectral idempotents are Hermitian, and the matrix is unitarily diagonalisable:
$$
\mathsf M_2(\tilde Q)=U\operatorname{diag}(\lambda_+,\lambda_-)U^{\dagger},
\qquad
\mathsf M_4^{L}(\tilde Q)=U_4\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-)U_4^{\dagger},
$$
with $U\in U(2)$ and $U_4$ its inflation. A normal element with distinct eigenvalues is Hermitian exactly when $\lambda_\pm\in\mathbb{R}$, $*$-unitary exactly when $\lvert\lambda_\pm\rvert=1$, and an involution exactly when $\lambda_\pm=\pm1$; with equal eigenvalues it is scalar.

**Transitions.** For two spectrally regular elements $\tilde Q$ and $\tilde Q'$, the change from the $Q'$-coordinates to the $Q$-coordinates is $T_{Q'Q}=\mathsf C_Q^{-1}\mathsf C_{Q'}$, and it satisfies
$$
\mathsf M_2^{Q}(\tilde X)=T_{Q'Q}\,\mathsf M_2^{Q'}(\tilde X)\,T_{Q'Q}^{-1}.
$$
The family satisfies the cocycle identity $T_{Q''Q}T_{Q'Q''}=T_{Q'Q}$. A transition preserves the diagonal form exactly when the two elements commute; then their spectral directions are parallel, the eigenbases agree up to rescaling, and the transition is diagonal. A general pair has no simultaneous eigenbasis.

## The Coefficient Frame

**The change.** In the coefficient frame the diagonalising matrix is the coordinate matrix of the eigenbasis in the coefficient basis:
$$
\mathsf C_{Q,\mathrm{coef}}=C_{\Pi}\mathsf C_Q^{(4)},
\qquad
\det\mathsf C_{Q,\mathrm{coef}}=\bigl(-\tfrac14\bigr)(-1)=\tfrac14,
$$
because $\det C_{\Pi}=-\tfrac14$ for the corpus order of the Peirce basis and $\det\mathsf C_Q^{(4)}=-1$ in the Peirce frame. The value is independent of the element. The two signs, the $-1$ of the corner order and the $-\tfrac14$ of the Peirce change, multiply to $\tfrac14$.

**The diagonal form.** The same change puts the regular matrix in the form
$$
\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-).
$$
The coefficient-frame matrix of the element is not diagonal in this basis until the change is applied; the eigenbasis is a new basis, not the coefficient basis. The four columns are the coefficient coordinates of $\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-$ in that order.

**The trace pairing.** In the corner order the Gram matrix of the trace pairing $\langle\tilde X,\tilde Y\rangle=\operatorname{Tr}(\tilde X\tilde Y)$ on the regular image is
$$
G=2\begin{pmatrix}
1&0&0&0\\
0&0&1&0\\
0&1&0&0\\
0&0&0&1
\end{pmatrix},
$$
because $\operatorname{Tr}(\tilde\Pi_\pm)=2$, $\operatorname{Tr}(\vec\Upsilon_\pm)=0$ and the mixed products are the rank-two idempotents. The factor two is the duplication of the spinor plane.

**The freedom.** The coefficient-frame change has the same freedom as the Peirce one: right multiplication by $GL_2\times GL_2$ when the eigenvalues are distinct, and by $U(2)\times U(2)$ in the normal case. The determinant $\tfrac14$ belongs to one chosen basis, not to the element.

## The Entry Model

**The matrix.**
$$
\mathsf C_Q=
\begin{pmatrix}
B-Q_z&Q_x-iQ_y\\
-Q_x-iQ_y&B-Q_z
\end{pmatrix}.
$$
Its first column is the eigenvector for $\lambda_+$ and its second the eigenvector for $\lambda_-$, both written in the fixed model and scaled by $2B\rho_\pm$. Its determinant is
$$
\det\mathsf C_Q=(B-Q_z)^2-(Q_x^2+Q_y^2)=2B(B-Q_z),
$$
using $Q_x^2+Q_y^2=B^2-Q_z^2$. The matrix is invertible whenever $B\neq Q_z$, and
$$
\mathsf C_Q^{-1}\,\mathsf M_2(\tilde Q)\,\mathsf C_Q
=\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}.
$$
The two columns are eigenvectors for distinct eigenvalues, so the matrix of eigenvectors diagonalises $\mathsf M_2(\tilde Q)$; the determinant is nonzero exactly when they are independent.

**The second chart.** When $B=Q_z$ the first chart is singular. The matrix
$$
\mathsf C_Q'=
\begin{pmatrix}
-Q_x+iQ_y&B+Q_z\\
B+Q_z&Q_x+iQ_y
\end{pmatrix},
\qquad
\det\mathsf C_Q'=-2B(B+Q_z),
$$
satisfies the same identity whenever $B\neq-Q_z$. The two determinants cannot both vanish: $B\neq0$, and $B=Q_z$ together with $B=-Q_z$ forces $B=0$. One of the two charts therefore always applies, and they agree on their overlap up to the freedom of the change.

**The labels.** The choice of the square root $B$ labels the eigenvalues. Replacing $B$ by $-B$ exchanges $\lambda_+$ and $\lambda_-$, the two columns of $\mathsf C_Q$ and the two diagonal entries. The pair of eigenvalues is unordered; only the labelling is a choice.

## The Peirce Frame

**The change.** The regular diagonalising matrix $\mathsf C_Q^{(4)}$ is the matrix whose columns are the coordinate columns of $P_{11},P_{12},P_{21},P_{22}$ in the Peirce frame, in that order. Equivalently, its four columns are the coordinate columns of the eigenbasis $\mathcal E$. It satisfies
$$
\bigl(\mathsf C_Q^{(4)}\bigr)^{-1}\mathsf M_4^{L}(\tilde Q)\,\mathsf C_Q^{(4)}
=\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-).
$$
Each eigenvalue occurs twice, once per spinor plane.

**The determinant.** In the Peirce frame,
$$
\det\mathsf C_Q^{(4)}=-1
$$
for every spectrally regular element. The value is independent of $Q$; the entry determinant $2B(B-Q_z)$ cancels. The conjugation $X\mapsto\mathsf C_QX\mathsf C_Q^{-1}$ is a linear map of $M_2(\mathbb{C})$ with determinant one, and it sends the standard matrix-unit basis to the spectral basis with determinant one; the coordinate columns are the vectorised conjugates, and the Kronecker factor has determinant one. The remaining factor is the permutation that orders the columns as $(11,12,21,22)$ instead of the column-major order $(11,21,12,22)$, which exchanges two columns and contributes $-1$.

**No degeneracy.** The entry chart can degenerate at $B=Q_z$, but the regular change cannot: its determinant is $-1$ for every element of the sector. The degeneracy is a property of the chosen entry chart, not of the eigenbasis; the second chart replaces $\mathsf C_Q$ in the construction and gives the same determinant.

**The freedom and the normal case.** The freedom is $GL_2(\mathbb{C})\times GL_2(\mathbb{C})$, reduced to $U(2)\times U(2)$ for a normal element. The transition matrix between two elements is $\mathrm I_2\otimes T_{Q'Q}$ up to that freedom, so a relative change is defined only up to it.

## Summary

A spectrally regular element has an eigenbasis $\mathcal E=(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$ that multiplies as the matrix units. In the $2\times2$ model the element is diagonalised by $\mathsf C_Q$, of determinant $2B(B-Q_z)$, with a second chart at $B=Q_z$. In the $4\times4$ regular model the same change has four columns, two per eigenvalue, and puts the matrix in the form $\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-)$; its determinant is $-1$ in the Peirce frame and $\tfrac14$ in the coefficient frame, independent of the element, because the $2\times2$ determinant cancels in the similarity and only the fixed frame change and a column permutation remain. The change is defined up to right multiplication by an invertible diagonal matrix in $2\times2$ and by $GL_2\times GL_2$ in $4\times4$, reduced to $U(2)\times U(2)$ in the normal case. Transitions between two elements satisfy the cocycle identity and preserve the diagonal form exactly when the elements commute.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal E=(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$ | the eigenbasis in corner order |
| $P_{ij}=\mathsf C_QE_{ij}\mathsf C_Q^{-1}$ | the spectral matrix units |
| $\mathsf M_2^{Q}$ | the spectral coordinate model |
| $\mathsf C_Q$ | the $2\times2$ diagonalising matrix |
| $2B(B-Q_z)$ | its determinant |
| $\mathsf C_Q'$ | the second chart, for $B=Q_z$ |
| $\mathsf C_Q^{(4)}$ | the regular diagonalising matrix |
| $-1$, $\tfrac14$ | its determinant in the Peirce and coefficient frames |
| $GL_2\times GL_2$ | the freedom for distinct eigenvalues |
| $U(2)\times U(2)$ | the freedom in the normal case |
| $T_{Q'Q}=\mathsf C_Q^{-1}\mathsf C_{Q'}$ | the transition matrix |
| $\lambda_\pm=Q_t\pm iB$ | the eigenvalues, repeated twice in $4\times4$ |

## Further Reading

- [Matrix Representations : The Models and the Change of Frame](matrix-representations-the-models-and-the-change-of-frame.html), for the frames and the change law
- [Matrix Representations : The Spectral Projectors](matrix-representations-the-spectral-projectors.html), for the projectors and the nilpotents
- [Matrix Representations : Peirce Coordinates, Matrix Units and the Spinor Planes](matrix-representations-peirce-coordinates-matrix-units-and-the-spinor-planes.html), for the planes and the corner order
- [Matrix Representations : The Jordan Basis and the Jordanising Matrix](matrix-representations-the-jordan-basis-and-the-jordanising-matrix.html), for the degenerate case
- [The Eigenbasis of a Spectrally Regular Biquaternion](the-eigenbasis-of-a-spectrally-regular-biquaternion.html), for the construction
- [Eigenvalues and Diagonalisation](eigenvalues-and-diagonalisation.html), for the matrix theorem
- [Nilpotents](nilpotents.html), for the spectral nilpotents