# __$M_2(\mathbb{C})$ Representation : The Eigenbasis and the Diagonalising Matrix__

## Introduction

A spectrally regular element has a basis of eigenvectors, and in that basis its matrix is diagonal. The basis is not the standard one: it depends on the element, and the matrix that changes from the standard basis to it is the diagonalising matrix. The coordinate model attached to that basis is the one in which the element is diagonal, its two eigenvalues are the diagonal entries, and the two mixed Peirce elements are the off-diagonal units.

This article develops the eigenbasis model and the diagonalising matrix. It is the matrix form of *The Spectrally Regular Sector and Construction of the Eigenbasis of a Biquaternion*, §*The Eigenbasis*, §*The Matrix Model* and §*Change of Basis*.

**Conventions.** The algebra and the model are those of *$M_2(\mathbb{C})$ Representation : The Matrix Product and the Algebra Structure*. The element is $\tilde Q=Q_te_t+\vec Q$ with $B^2=Q_x^2+Q_y^2+Q_z^2\neq0$, and $B$ is a chosen square root. The spectral direction is $\vec\Xi=-i\vec Q/B$, the spectral idempotents are $\tilde\Pi_\pm=\tfrac12(e_t\pm\vec\Xi)$, and the eigenvalues are $\lambda_\pm=Q_t\pm iB$. The two mixed elements are written $\vec\Upsilon_-$ and $\vec\Upsilon_+$, with $\vec\Upsilon_-\mapsto E_{12}$ and $\vec\Upsilon_+\mapsto E_{21}$ in the eigenbasis model.

**Boundaries.** The construction of the basis and of the nilpotents is *The Spectrally Regular Sector and Construction of the Eigenbasis of a Biquaternion*; the spectral projectors are *$M_2(\mathbb{C})$ Representation : The Spectral Projectors and the Nilpotents*; the Peirce coordinates of the standard pair are *$M_2(\mathbb{C})$ Representation : The Peirce Coordinates and the Matrix Units*; the 4×4 model is *The Spectrally Regular Sector and Eigenbasis of a Biquaternion in Matrix Element Representations*.

## The Eigenbasis

**The basis.** The eigenbasis is

$$
\big(\tilde\Pi_+,\ \vec\Upsilon_-,\ \vec\Upsilon_+,\ \tilde\Pi_-\big),
$$

with $\tilde\Pi_\pm$ the spectral idempotents and $\vec\Upsilon_\pm$ the two spectral nilpotents. It is a $\mathbb{C}$-basis of $\mathbb{B}$ for every $B\neq0$. The order is the one adapted to the matrix units: the first and last elements are the two corners, and the two middle elements are the two mixed elements.

**The multiplication table.** The basis multiplies as the matrix units:

| Product | Value |
|---|---|
| $\tilde\Pi_+^2$ | $\tilde\Pi_+$ |
| $\tilde\Pi_-^2$ | $\tilde\Pi_-$ |
| $\tilde\Pi_+\tilde\Pi_-$ | $0$ |
| $\vec\Upsilon_-^2$, $\vec\Upsilon_+^2$ | $0$ |
| $\vec\Upsilon_-\vec\Upsilon_+$ | $\tilde\Pi_+$ |
| $\vec\Upsilon_+\vec\Upsilon_-$ | $\tilde\Pi_-$ |
| $\tilde\Pi_+\vec\Upsilon_-=\vec\Upsilon_-\tilde\Pi_-$ | $\vec\Upsilon_-$ |
| $\tilde\Pi_-\vec\Upsilon_+=\vec\Upsilon_+\tilde\Pi_+$ | $\vec\Upsilon_+$ |

The table is the standard matrix-unit table with the labels of the middle elements chosen so that $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+$. The choice is the opposite of the standard pair's labelling, where $\vec\Upsilon_x\vec\Upsilon_y=\tilde\Pi_+$; the two labels are conventions and the table is the same.

**The expansion.** Every element has a unique expansion

$$
\tilde X=X_{11}\tilde\Pi_++X_{12}\vec\Upsilon_-+X_{21}\vec\Upsilon_++X_{22}\tilde\Pi_-,
$$

and the coordinate matrix is

$$
\mathsf{M}_2^{Q}(\tilde X)=\begin{pmatrix}X_{11}&X_{12}\\X_{21}&X_{22}\end{pmatrix}.
$$

The superscript $Q$ records that the model depends on the element $Q$ through its spectral direction. For the element itself,

$$
\mathsf{M}_2^{Q}(\tilde Q)=\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix},
$$

because $\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-$ and the mixed coefficients vanish.

**The coordinates by duality.** The four coordinates are the trace pairings

$$
X_{11}=\operatorname{Tr}(\tilde\Pi_+\tilde X),\quad
X_{12}=\operatorname{Tr}(\vec\Upsilon_+\tilde X),\quad
X_{21}=\operatorname{Tr}(\vec\Upsilon_-\tilde X),\quad
X_{22}=\operatorname{Tr}(\tilde\Pi_-\tilde X),
$$

with the two mixed elements exchanged in the dual basis, as in the standard pair. The exchange is the statement $\operatorname{Tr}(\vec\Upsilon_-\vec\Upsilon_+)=1=\operatorname{Tr}(\vec\Upsilon_+\vec\Upsilon_-)$.

**The diagonal subalgebra.** An element commutes with $\tilde Q$ exactly when its coordinate matrix is diagonal in the eigenbasis. The diagonal subalgebra is therefore $\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\tilde\Pi_-$, of dimension two, and it is the centraliser of $\tilde Q$. The statement is the matrix form of the fact that a spectrally regular element has a two-dimensional commutative centraliser, spanned by its spectral idempotents.

## The Diagonalising Matrix

**Definition.** The diagonalising matrix is

$$
\mathsf{C}_Q=
\begin{pmatrix}
B-Q_z&Q_x-iQ_y\\
-Q_x-iQ_y&B-Q_z
\end{pmatrix}.
$$

Its columns are the first column of $2B\rho_+$ and the second column of $2B\rho_-$. Its determinant is

$$
\det\mathsf{C}_Q=(B-Q_z)^2-(-Q_x-iQ_y)(Q_x-iQ_y)
=(B-Q_z)^2+Q_x^2+Q_y^2
=2B(B-Q_z),
$$

using $Q_x^2+Q_y^2=B^2-Q_z^2$.

**The inverse.** When $B\neq Q_z$,

$$
\mathsf{C}_Q^{-1}=\frac{1}{2B(B-Q_z)}
\begin{pmatrix}
B-Q_z&-(Q_x-iQ_y)\\
Q_x+iQ_y&B-Q_z
\end{pmatrix}.
$$

**Theorem (diagonalisation).**

$$
\mathsf{C}_Q^{-1}\,\mathsf{M}_2(\tilde Q)\,\mathsf{C}_Q
=\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}.
$$

*Proof.* The two columns of $\mathsf{C}_Q$ are eigenvectors: the first is an eigenvector for $\lambda_+$ and the second for $\lambda_-$. A matrix whose two columns are eigenvectors for distinct eigenvalues is diagonalised by the matrix of its eigenvectors, and the diagonal entries are the eigenvalues. The determinant is nonzero when $B\neq Q_z$, so the matrix is invertible.

**The second chart.** When $B=Q_z$ the first chart is singular, and the relation $B^2=Q_z^2+Q_x^2+Q_y^2$ forces $Q_x=Q_y=0$. The second chart is

$$
\mathsf{C}_Q'=
\begin{pmatrix}
-Q_x+iQ_y&B+Q_z\\
B+Q_z&Q_x+iQ_y
\end{pmatrix},
\qquad
\det\mathsf{C}_Q'=-2B(B+Q_z),
$$

and it satisfies the same diagonalisation identity whenever $B\neq-Q_z$. The two determinants cannot both vanish: $B\neq0$, and $B=Q_z$ and $B=-Q_z$ would give $Q_z=0$ and then $B=0$. One of the two charts therefore always applies.

**The exchange of the labels.** On the axis $\vec Q=Q_z\vec e_z$ the second chart is a permutation matrix, and the diagonalisation holds with the eigenvalues in the order $\lambda_+,\lambda_-$. The labels are a choice of the square root $B$; the reversed choice exchanges the two columns and the two diagonal entries.

## The Freedom of the Change

**Right diagonal multiplication.** If $D=\operatorname{diag}(\alpha,\beta)$ is invertible, then

$$
(\mathsf{C}_QD)^{-1}M(\mathsf{C}_QD)=D^{-1}\big(\mathsf{C}_Q^{-1}M\mathsf{C}_Q\big)D
=\mathsf{C}_Q^{-1}M\mathsf{C}_Q,
$$

because a diagonal matrix commutes with a diagonal matrix. The diagonalising matrix is therefore defined up to right multiplication by an invertible diagonal matrix.

**Left scalar multiplication.** A nonzero scalar multiple $\mu\mathsf{C}_Q$ gives the same conjugation, so the matrix is also defined up to a nonzero scalar. The two freedoms together are the freedom of choosing the eigenvectors and their normalisation: each eigenvector can be rescaled independently, and the pair can be multiplied by a common scalar.

**The eigenvector reading.** The first column of $\mathsf{C}_Q$ is the eigenvector for $\lambda_+$, and the second is the eigenvector for $\lambda_-$. The right diagonal freedom rescales the two eigenvectors independently. The reciprocal scaling of the nilpotents is the same freedom read in the Peirce basis: the pair $(\vec\Upsilon_-,\vec\Upsilon_+)$ can be rescaled by $(\alpha,\alpha^{-1})$ without changing the products, and that rescaling is a diagonal similarity of the coordinate model.

**Normalisations.** Two normalisations are useful. The first fixes the first entry of each eigenvector to one when it is nonzero; this is the chart in which $\mathsf{C}_Q$ is written above, up to the common factor $2B$. The second fixes the determinant of $\mathsf{C}_Q$ to one, which is possible because the determinant is nonzero; the normalised matrix is $\mathsf{C}_Q/\sqrt{2B(B-Q_z)}$, with a choice of square root. The first normalisation is algebraic and the second is metric; neither is canonical.

**The diagonalising matrix is not a unit of the algebra.** $\mathsf{C}_Q$ is a matrix, not necessarily the image of a biquaternion of unit norm. It is an element of $GL_2(\mathbb{C})$, and it acts by conjugation on the matrix algebra. Its columns are eigenvectors, not elements of the algebra in the biquaternion product. The distinction is the distinction between the algebra and its defining module.

## Change from One Element to Another

**The transition matrix.** Let $\tilde Q$ and $\tilde Q'$ be two spectrally regular elements, with diagonalising matrices $\mathsf{C}_Q$ and $\mathsf{C}_{Q'}$. The matrix

$$
T_{Q'Q}=\mathsf{C}_Q^{-1}\mathsf{C}_{Q'}
$$

changes the $Q'$-coordinates to the $Q$-coordinates:

$$
\mathsf{M}_2^{Q}(\tilde X)=T_{Q'Q}\,\mathsf{M}_2^{Q'}(\tilde X)\,T_{Q'Q}^{-1}.
$$

*Proof.* Substitute the two definitions:

$$
\mathsf{C}_Q^{-1}M\mathsf{C}_Q
=\mathsf{C}_Q^{-1}\mathsf{C}_{Q'}\big(\mathsf{C}_{Q'}^{-1}M\mathsf{C}_{Q'}\big)\mathsf{C}_{Q'}^{-1}\mathsf{C}_Q.
$$

**The cocycle.** For three elements,

$$
T_{Q''Q}T_{Q'Q''}=T_{Q'Q},
$$

with the obvious convention on the order of the labels. The transition matrices satisfy the cocycle identity of a change of trivialisation, and the family of eigenbasis models is a trivialisation of the bundle of spectral frames over the spectrally regular set.

**The diagonal form is not preserved by a general change.** A transition matrix between two different spectral elements does not preserve the diagonal subalgebra unless the two elements have the same eigenbasis. The diagonal form is attached to one element, and the change to another element mixes the two eigenvalues. The statement is the matrix form of the fact that two spectrally regular elements are simultaneously diagonalisable exactly when they commute.

**The commuting case.** If $\tilde Q$ and $\tilde Q'$ commute, their spectral directions are parallel or the elements are scalar on the same two lines, and the transition matrix is diagonal. Then the two eigenbases coincide up to rescaling, and the two elements are simultaneously diagonal. The statement is the spectral theorem for a commuting family, read in the matrix model.

## Summary

The eigenbasis $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$ multiplies as the matrix units $E_{11},E_{12},E_{21},E_{22}$; in the coordinate model the element is diagonal with entries $\lambda_+,\lambda_-$, while left multiplication on the four-dimensional algebra has the doubled entries $\lambda_+,\lambda_+,\lambda_-,\lambda_-$. The diagonalising matrix $\mathsf{C}_Q$ has the two eigenvectors as columns, has determinant $2B(B-Q_z)$, and satisfies $\mathsf{C}_Q^{-1}M\mathsf{C}_Q=\operatorname{diag}(\lambda_+,\lambda_-)$; a second chart covers the axis $B=Q_z$. The matrix is defined up to a nonzero scalar and an invertible diagonal right factor, which are the rescalings of the two eigenvectors. Transitions between two spectral elements satisfy the cocycle identity and preserve the diagonal form only when the elements commute.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$ | the eigenbasis |
| $\mathsf{M}_2^{Q}$ | the coordinate model attached to $\tilde Q$ |
| $X_{ij}$ | the eigenbasis coordinates |
| $\mathsf{C}_Q$ | the diagonalising matrix |
| $2B(B-Q_z)$ | its determinant |
| $\mathsf{C}_Q'$ | the second chart, for $B=Q_z$ |
| $T_{Q'Q}=\mathsf{C}_Q^{-1}\mathsf{C}_{Q'}$ | the transition matrix |
| $\lambda_\pm=Q_t\pm iB$ | the eigenvalues |

## Further Reading

- [The Spectrally Regular Sector and Construction of the Eigenbasis of a Biquaternion](the-spectrally-regular-sector-and-construction-of-the-eigenbasis-of-a-biquaternion.html), for the construction of the basis and the change of basis
- [$M_2(\mathbb{C})$ Representation : The Spectral Projectors and the Nilpotents](m2c-representation-the-spectral-projectors-and-the-nilpotents.html), for the projectors
- [$M_2(\mathbb{C})$ Representation : The Peirce Coordinates and the Matrix Units](m2c-representation-the-peirce-coordinates-and-the-matrix-units.html), for the standard coordinate model
- [Spectral Regularity and Degeneracy in the Biquaternion Algebra](spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the spectral criterion
- [The Spectrally Regular Sector and Eigenbasis of a Biquaternion in Matrix Element Representations](the-spectrally-regular-sector-and-eigenbasis-of-a-biquaternion-in-matrix-element-representations.html), for the 4×4 model
- [Eigenvalues and Diagonalisation](eigenvalues-and-diagonalisation.html), for the matrix theorem
