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

## The Spectral Matrix Units

**The definition.** Let $E_{ij}$ be the ordinary $2\times2$ matrix units and let
$$
P_{ij}=\mathsf C_Q\,E_{ij}\,\mathsf C_Q^{-1}
$$
be their conjugates by the diagonalising matrix. The four matrices $P_{ij}$ are a basis of $M_2(\mathbb{C})$ and multiply as the matrix units:
$$
P_{ij}P_{kl}=\delta_{jk}P_{il}.
$$
The correspondence with the eigenbasis is
$$
P_{11}=\tilde\Pi_+,\qquad
P_{12}=\vec\Upsilon_-,\qquad
P_{21}=\vec\Upsilon_+,\qquad
P_{22}=\tilde\Pi_-.
$$
The two diagonal elements are the spectral projectors, and the two off-diagonal elements are the spectral nilpotents.

**The coordinate model.** Every element has a unique expansion
$$
\tilde X=\sum_{i,j=1}^{2}X_{ij}P_{ij},
\qquad
\mathsf M_2^{Q}(\tilde X)=\begin{pmatrix}X_{11}&X_{12}\\X_{21}&X_{22}\end{pmatrix}.
$$
The superscript records that the model depends on the element through $Q$. The map $\mathsf M_2^{Q}$ is an isomorphism of algebras, and for the element itself
$$
\mathsf M_2^{Q}(\tilde Q)=\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}.
$$
In the regular model the same coordinates give
$$
\mathsf M_4^{Q}(\tilde Q)=\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-),
$$
because left multiplication preserves each spinor plane and each eigenvalue is repeated once per plane.

**The coordinates by duality.** The four coordinates are the trace pairings with the dual basis. With the corner order, and with the two mixed elements exchanged in the dual,
$$
X_{11}=\operatorname{Tr}(\tilde\Pi_+\tilde X),\qquad
X_{12}=\operatorname{Tr}(\vec\Upsilon_+\tilde X),\qquad
X_{21}=\operatorname{Tr}(\vec\Upsilon_-\tilde X),\qquad
X_{22}=\operatorname{Tr}(\tilde\Pi_-\tilde X).
$$
In the regular model each trace pairing is doubled, because $\operatorname{Tr}(\tilde\Pi_\pm)=2$ and the mixed products have trace $2$; the coordinate is therefore half the $4\times4$ trace. The exchange in the dual basis is $\operatorname{Tr}(\vec\Upsilon_-\vec\Upsilon_+)=1$ in the $2\times2$ model and $2$ in the regular model.

## The $2\times2$ Diagonalising Matrix

**The definition.**
$$
\mathsf C_Q=
\begin{pmatrix}
B-Q_z&Q_x-iQ_y\\
-Q_x-iQ_y&B-Q_z
\end{pmatrix}.
$$
Its first column is the eigenvector for $\lambda_+$ and its second column the eigenvector for $\lambda_-$, both written in the fixed model and both scaled by $2B\rho_\pm$.

**The determinant.**
$$
\det\mathsf C_Q=(B-Q_z)^2-(Q_x^2+Q_y^2)
=2B(B-Q_z),
$$
using $Q_x^2+Q_y^2=B^2-Q_z^2$. The matrix is invertible whenever $B\neq Q_z$.

**The diagonalisation.**
$$
\mathsf C_Q^{-1}\,\mathsf M_2(\tilde Q)\,\mathsf C_Q
=\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}.
$$

*Proof.* The two columns are eigenvectors for distinct eigenvalues, so the matrix of eigenvectors diagonalises $\mathsf M_2(\tilde Q)$ and the diagonal entries are the eigenvalues. The determinant is nonzero exactly when the two eigenvectors are independent.

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
satisfies the same identity whenever $B\neq-Q_z$. The two determinants cannot both vanish: $B\neq0$, and $B=Q_z$ together with $B=-Q_z$ forces $B=0$. One of the two charts therefore always applies. The two charts agree on their overlap up to the freedom of §*The Freedom of the Change*.

**The labels.** The choice of the square root $B$ labels the two eigenvalues. Replacing $B$ by $-B$ exchanges $\lambda_+$ and $\lambda_-$, exchanges the two columns of $\mathsf C_Q$ and exchanges the two diagonal entries. The pair of eigenvalues is unordered; only the labelling is a choice.

## The $4\times4$ Diagonalising Matrix

**The definition.** The regular diagonalising matrix $\mathsf C_Q^{(4)}$ is the matrix whose columns are the coordinate columns of $P_{11},P_{12},P_{21},P_{22}$ in the Peirce frame, in that order. Equivalently, its four columns are the coordinate columns of the eigenbasis $\mathcal E$.

**The theorem.**
$$
\bigl(\mathsf C_Q^{(4)}\bigr)^{-1}\mathsf M_4^{L}(\tilde Q)\,\mathsf C_Q^{(4)}
=\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-).
$$
The two eigenvalues occur twice each. In the $2\times2$ display the same change is $\mathsf C_Q$ and each eigenvalue occurs once.

**The determinant in the Peirce frame.**
$$
\det\mathsf C_Q^{(4)}=-1
$$
for every spectrally regular element. The value is independent of $Q$; the $2\times2$ determinant $2B(B-Q_z)$ cancels.

*Proof.* The conjugation $X\mapsto\mathsf C_QX\mathsf C_Q^{-1}$ is a linear map of $M_2(\mathbb{C})$ with determinant $(\det\mathsf C_Q)^2/(\det\mathsf C_Q)^2=1$. It sends the standard matrix-unit basis to the spectral basis with determinant one. The coordinate columns are the vectorised conjugates, $\operatorname{vec}(P_{ij})=(\mathsf C_Q^{-\mathsf T}\otimes\mathsf C_Q)\operatorname{vec}(E_{ij})$, and the Kronecker factor has determinant one. The remaining factor is the permutation that orders the columns as $(11,12,21,22)$ instead of the column-major order $(11,21,12,22)$; that permutation exchanges two columns and contributes $-1$.

**The determinant in the coefficient frame.** In the coefficient frame the same change is $C_{\Pi}\mathsf C_Q^{(4)}$, of determinant
$$
\det\bigl(C_{\Pi}\mathsf C_Q^{(4)}\bigr)
=\bigl(-\tfrac14\bigr)(-1)=\tfrac14,
$$
because $\det C_{\Pi}=-\tfrac14$ for the corpus order of the Peirce basis. The two signs, the $-1$ of the corner order and the $-\tfrac14$ of the corpus Peirce change, multiply to $\tfrac14$.

**What cancels and what does not.** The $2\times2$ chart can degenerate at $B=Q_z$, but the $4\times4$ change cannot: the determinant is $-1$ for every element of the sector. The degeneracy is a property of the chosen $2\times2$ chart, not of the eigenbasis. The second chart of the $2\times2$ model replaces $\mathsf C_Q$ in the construction and gives the same determinant.

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

## The Freedom of the Change

**The $2\times2$ freedom.** If $D=\operatorname{diag}(\alpha,\beta)$ is invertible, then
$$
(\mathsf C_QD)^{-1}\mathsf M_2(\tilde Q)(\mathsf C_QD)
=D^{-1}\bigl(\mathsf C_Q^{-1}\mathsf M_2(\tilde Q)\mathsf C_Q\bigr)D
=\mathsf C_Q^{-1}\mathsf M_2(\tilde Q)\mathsf C_Q,
$$
because a diagonal matrix commutes with a diagonal matrix. The diagonalising matrix is therefore defined up to right multiplication by an invertible diagonal matrix,
$$
\operatorname{diag}(\mathbb{C}^{\times},\mathbb{C}^{\times}),
$$
of complex dimension two. A scalar multiple is the diagonal matrix with equal entries, so it adds nothing beyond the two independent rescalings.

**The eigenvector reading.** The two entries of $D$ rescale the two eigenvectors independently, and the scalar multiplies both. The freedom is the choice of the eigenvectors and of their normalisation, not a property of the element.

**The $4\times4$ freedom.** Two regular eigenbases differ by an element of the commutant of the diagonal form. When $\lambda_+\neq\lambda_-$,
$$
C\bigl(\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-)\bigr)
=GL_2(\mathbb{C})\times GL_2(\mathbb{C}),
$$
of complex dimension eight. The first factor changes the basis inside the $\lambda_+$-eigenspace and the second inside the $\lambda_-$-eigenspace. The extra six parameters, compared with the $2\times2$ freedom, mix the two spinor planes inside one eigenspace.

**The determinant is not invariant.** Under the freedom the determinant of the change is multiplied by the determinant of the commuting matrix. The values $-1$ and $\tfrac14$ belong to one chosen basis, not to the element. Only the vanishing and the rank of the change are invariant.

**The normal case.** When the element is normal, the eigenbasis can be chosen orthonormal and the freedom reduces to
$$
U(2)\times U(2)
$$
in the regular model, and to the diagonal $*$-unitary group in the $2\times2$ model. The determinant of the $*$-unitary change has modulus one.

## The Normal Case

**The definition.** A matrix is normal when $XX^{\dagger}=X^{\dagger}X$. The element is normal exactly when its $2\times2$ matrix is normal, because the regular matrix is $I_2\otimes\mathsf M_2(\tilde Q)$ in the Peirce frame and the dagger acts on the second factor.

**The criterion.** In the algebra the condition is $[\vec Q,\bar{\vec Q}]=0$, that is,
$$
\vec Q=\zeta\vec p,
\qquad
\zeta\in\mathbb{C},
\quad
\vec p\in\mathbb{R}^3.
$$
The three components of the vector part have a common phase. For a non-scalar normal element the spectral direction is $\vec\Xi=-i\vec p/\lvert\vec p\rvert$, which is pure imaginary, and the spectral idempotents are Hermitian.

**The spectral theorem.** A normal $2\times2$ matrix is unitarily diagonalisable:
$$
\mathsf M_2(\tilde Q)=U\operatorname{diag}(\lambda_+,\lambda_-)U^{\dagger},
\qquad
U\in U(2).
$$
In the regular model the same statement is
$$
\mathsf M_4^{L}(\tilde Q)=U_4\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-)U_4^{\dagger},
\qquad
U_4\in U(4),
$$
with $U_4$ the inflation of $U$. The two eigenspaces are orthogonal, and the spectral projectors are Hermitian.

**The three normal types.** A normal element with distinct eigenvalues is Hermitian exactly when $\lambda_\pm\in\mathbb{R}$, $*$-unitary exactly when $\lvert\lambda_\pm\rvert=1$, and an involution exactly when $\lambda_\pm=\pm1$. A normal element with equal eigenvalues is scalar.

## Change from One Element to Another

**The transition matrix.** For two spectrally regular elements $\tilde Q$ and $\tilde Q'$, the change from the $Q'$-coordinates to the $Q$-coordinates is
$$
T_{Q'Q}=\mathsf C_Q^{-1}\mathsf C_{Q'}.
$$
It satisfies
$$
\mathsf M_2^{Q}(\tilde X)=T_{Q'Q}\,\mathsf M_2^{Q'}(\tilde X)\,T_{Q'Q}^{-1}.
$$

**The cocycle.** For three elements,
$$
T_{Q''Q}T_{Q'Q''}=T_{Q'Q},
$$
with the order of the labels read as composition of changes. The family of eigenbasis models is a trivialisation of the bundle of spectral frames over the spectrally regular set.

**The commuting case.** A transition matrix preserves the diagonal form exactly when the two elements commute. In that case their spectral directions are parallel, the two eigenbases agree up to rescaling, and the transition matrix is diagonal. A general pair has no simultaneous eigenbasis.

**The relative change in the regular model.** The same transition is doubled inside each spinor plane:
$$
T^{(4)}_{Q'Q}=I_2\otimes T_{Q'Q}
$$
in the Peirce frame, up to the freedom that mixes the two copies. The extra freedom is the $GL_2\times GL_2$ of §*The Freedom of the Change*, and a relative change is defined only up to it.

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
- [Matrix Representations : The Eigenbasis and the Diagonalising Matrix](matrix-representations-the-eigenbasis-and-the-diagonalising-matrix.html), for the $2\times2$ source
- [Matrix Representations : The Eigenbasis and the Diagonalising Matrix](matrix-representations-the-eigenbasis-and-the-diagonalising-matrix.html), for the $4\times4$ source
