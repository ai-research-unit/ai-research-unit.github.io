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

**The second chart.** When $B=Q_z$ the first chart is singular; the second chart has determinant $-2B(B+Q_z)$, which is nonzero there because $B\neq0$. The second chart is

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

## The Eigenbasis in the Fixed Model

**The basis elements are the conjugates of the matrix units.** In the fixed model,

$$
\mathsf M_2(\tilde\Pi_+)=\mathsf C_QE_{11}\mathsf C_Q^{-1},\qquad
\mathsf M_2(\vec\Upsilon_-)=\mathsf C_QE_{12}\mathsf C_Q^{-1},\qquad
\mathsf M_2(\vec\Upsilon_+)=\mathsf C_QE_{21}\mathsf C_Q^{-1},\qquad
\mathsf M_2(\tilde\Pi_-)=\mathsf C_QE_{22}\mathsf C_Q^{-1}.
$$

The two assignments of the four basis elements — to the eigenbasis coordinates and to the fixed matrix units — differ by the change of basis $\mathsf C_Q$. This is the precise sense in which the eigenbasis model is the fixed model conjugated by the diagonalising matrix.

**The trace pairing.** With the ordering $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$, the Gram matrix of the trace pairing $\langle\tilde X,\tilde Y\rangle=\operatorname{Tr}(\tilde X\tilde Y)$ is

$$
G=\begin{pmatrix}
1&0&0&0\\
0&0&1&0\\
0&1&0&0\\
0&0&0&1
\end{pmatrix},
$$

because $\operatorname{Tr}(\tilde\Pi_\pm)=1$, $\operatorname{Tr}(\vec\Upsilon_\pm)=0$, $\operatorname{Tr}(\vec\Upsilon_-\vec\Upsilon_+)=\operatorname{Tr}(\tilde\Pi_+)=1$ and $\operatorname{Tr}(\vec\Upsilon_+\vec\Upsilon_-)=\operatorname{Tr}(\tilde\Pi_-)=1$. The basis is not orthonormal: the idempotents are unit vectors for the pairing, the nilpotents are isotropic, and the two mixed products pair to one.

**The invariants.** For every element $\tilde X$ with eigenbasis coordinates $X_{ij}$,

$$
\operatorname{Tr}\mathsf M_2^{Q}(\tilde X)=X_{11}+X_{22}=2X_t,
\qquad
\det\mathsf M_2^{Q}(\tilde X)=X_{11}X_{22}-X_{12}X_{21}=\langle\tilde X\rangle_{\natural}.
$$

The trace is twice the scalar part and the determinant is the quaternionic norm, as in the fixed model, because the two models differ by a conjugation.

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

## The Normal Case

**The definition.** A matrix is **normal** when it commutes with its Hermitian adjoint:

$$
XX^{\dagger}=X^{\dagger}X .
$$

Every Hermitian matrix, every unitary matrix and every scalar matrix is normal. Normality is the condition that the two Hermitian matrices in the Hermitian decomposition commute.

**The Hermitian decomposition.** Every matrix has a unique decomposition

$$
X=A+iB,
\qquad
A=\tfrac12(X+X^{\dagger}),
\qquad
B=\tfrac{1}{2i}(X-X^{\dagger}),
$$

with $A$ and $B$ Hermitian. Then

$$
XX^{\dagger}-X^{\dagger}X=2i(BA-AB),
$$

so $X$ is normal exactly when $[A,B]=0$. The two Hermitian parts are the real and imaginary parts of the matrix, and normality says that they are simultaneously diagonalisable.

**The spectral theorem.** A $2\times2$ matrix is normal exactly when it is unitarily diagonalisable: there are a unitary $U$ and complex numbers $\lambda_+,\lambda_-$ with

$$
X=U\operatorname{diag}(\lambda_+,\lambda_-)U^{\dagger}.
$$

*Proof.* If $X$ is unitarily diagonalisable, it commutes with its dagger because diagonal matrices do. Conversely, Schur's theorem writes $X=UTU^{\dagger}$ with $T$ upper triangular. Normality of $X$ is normality of $T$. Comparing the $(1,1)$ entries of $TT^{\dagger}$ and $T^{\dagger}T$ gives $|t_{12}|^2=0$, so $T$ is diagonal. $\square$

**The spectral projectors.** For distinct eigenvalues,

$$
\Pi_+=\frac{X-\lambda_-\mathrm I_2}{\lambda_+-\lambda_-},
\qquad
\Pi_-=\mathrm I_2-\Pi_+,
$$

and $X=\lambda_+\Pi_++\lambda_-\Pi_-$. The matrix $X$ is normal exactly when $\Pi_+$ and $\Pi_-$ are Hermitian; then they are orthogonal projectors,

$$
\Pi_\pm^2=\Pi_\pm=\Pi_\pm^{\dagger},
\qquad
\Pi_+\Pi_-=0,
$$

and the eigenspaces are orthogonal. For a non-normal matrix with distinct eigenvalues the same $\Pi_\pm$ are idempotent and satisfy $\Pi_+\Pi_-=0$, but they are not Hermitian: they project onto the eigenspaces along the other eigenspace, and the two eigenspaces are not orthogonal.

**The normal form.** A normal matrix is exactly a matrix of the form

$$
X=a\mathrm I_2+b\,\vec n\cdot\vec\sigma,
\qquad
a,b\in\mathbb{C},
\quad
\vec n\in\mathbb{R}^3,
$$

with $\vec\sigma=(\sigma_1,\sigma_2,\sigma_3)$ and $\vec n$ not necessarily of unit length. The two eigenvalues are $a\pm b|\vec n|$. The form displays the normal locus as the union of the complex planes spanned by $\mathrm I_2$ and a point of the Bloch sphere, that is, the union of the unitary conjugates of the diagonal algebra.

**The algebra reading.** In the model $X=\mathsf{M}_2(\tilde Q)$, the matrix is normal exactly when

$$
[\vec Q,\bar{\vec Q}]=0,
$$

that is, when the vector part and its complex conjugate are linearly dependent. Equivalently,

$$
\vec Q=\zeta\vec p,
\qquad
\zeta\in\mathbb{C},
\quad
\vec p\in\mathbb{R}^3,
$$

with $\vec p=0$ when $\vec Q=0$, so the three components of $\vec Q$ have a common phase. For a non-scalar normal element, the spectral direction is

$$
\vec\Xi=-\frac{i\vec Q}{B}=-\frac{i\vec p}{|\vec p|},
$$

for the square root $B=\pm\zeta|\vec p|$, which is pure imaginary. Hence

$$
\tilde\Pi_\pm=\tfrac12(e_t\pm\vec\Xi)=\tfrac12\Bigl(e_t\mp i\frac{\vec p}{|\vec p|}\Bigr)
$$

are Hermitian idempotents, $\tilde\Pi_\pm^{*}=\tilde\Pi_\pm$, and they are orthogonal for the Hermitian form. Conversely, if the spectral idempotents are Hermitian, $\vec\Xi$ is pure imaginary and $\vec Q=iB\vec\Xi$ is a complex scalar times a real vector. In a unitary eigenbasis the star exchanges the two nilpotents, $\vec\Upsilon_-^{*}=\vec\Upsilon_+$, and the Hermitian form pairs them; the two idempotents are the orthogonal spectral projectors.

**The three normal types.** For a normal matrix with distinct eigenvalues:

- $X$ is Hermitian exactly when $\lambda_\pm\in\mathbb{R}$; then $\vec Q$ is pure imaginary.
- $X$ is unitary exactly when $|\lambda_\pm|=1$.
- $X$ is both exactly when $\lambda_\pm=\pm1$, that is, when $X$ is an involution.

A normal matrix with a repeated eigenvalue is scalar: it is unitarily diagonalisable with equal diagonal entries. The scalar is Hermitian when the scalar is real and unitary when its modulus is one.

**The example.** The normal matrix

$$
N=\begin{pmatrix}1&1\\-1&1\end{pmatrix}
$$

has $\tilde Q=e_t-\vec e_y$, $\vec Q=-\vec e_y$, $B=1$ and $\vec\Xi=i\vec e_y$, so $\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_y)$. In the fixed model,

$$
\mathsf M_2(\tilde\Pi_\pm)=\tfrac12(\mathrm I_2\pm\sigma_2)
=\tfrac12\begin{pmatrix}1&\mp i\\\pm i&1\end{pmatrix},
$$

the orthogonal projectors onto the eigenvectors $(1,i)$ and $(1,-i)$ respectively. The eigenvalues are $1\pm i$, neither real nor of modulus one: the matrix is normal, but neither Hermitian nor unitary. The example is computed with the other seven in *$M_2(\mathbb{C})$ Representation : Worked Examples*.

**What the normal case adds to the eigenbasis.** The eigenbasis of a normal matrix can be chosen orthonormal, so the diagonalising matrix can be chosen unitary. The freedom of the change is then the freedom of multiplying by a diagonal unitary, not an arbitrary invertible diagonal matrix. The Lagrange formula for the projectors is the same as in the general case; only the Hermitian property is new. The normal case is the exact intersection of the eigenbasis construction with the spectral theorem.

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

The eigenbasis $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$ multiplies as the matrix units $E_{11},E_{12},E_{21},E_{22}$; in the coordinate model the element is diagonal with entries $\lambda_+,\lambda_-$ and vanishing mixed coordinates. The diagonalising matrix $\mathsf{C}_Q$ has the two eigenvectors as columns, has determinant $2B(B-Q_z)$, and satisfies $\mathsf{C}_Q^{-1}M\mathsf{C}_Q=\operatorname{diag}(\lambda_+,\lambda_-)$; a second chart covers the axis $B=Q_z$. The matrix is defined up to a nonzero scalar and an invertible diagonal right factor, which are the rescalings of the two eigenvectors. Transitions between two spectral elements satisfy the cocycle identity and preserve the diagonal form only when the elements commute. In the normal case the eigenbasis can be chosen orthonormal, the diagonalising matrix unitary, and the spectral projectors Hermitian; the normal elements are exactly those whose vector part is a complex scalar times a real vector.

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
| $XX^{\dagger}=X^{\dagger}X$ | the normality condition |
| $\vec Q=\zeta\vec p$ | the normal coordinates, $\zeta\in\mathbb{C}$, $\vec p\in\mathbb{R}^3$ |
| $X=a\mathrm I_2+b\,\vec n\cdot\vec\sigma$ | the normal form |

## Further Reading

- [The Spectrally Regular Sector and Construction of the Eigenbasis of a Biquaternion](the-spectrally-regular-sector-and-construction-of-the-eigenbasis-of-a-biquaternion.html), for the construction of the basis and the change of basis
- [$M_2(\mathbb{C})$ Representation : The Spectral Projectors and the Nilpotents](m2c-representation-the-spectral-projectors-and-the-nilpotents.html), for the projectors
- [$M_2(\mathbb{C})$ Representation : The Peirce Coordinates and the Matrix Units](m2c-representation-the-peirce-coordinates-and-the-matrix-units.html), for the standard coordinate model
- [$M_2(\mathbb{C})$ Representation : Worked Examples](m2c-representation-worked-examples.html), for the eight worked matrices, including the normal example
- [Spectral Regularity and Degeneracy in the Biquaternion Algebra](spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the spectral criterion
- [The Spectrally Regular Sector and Eigenbasis of a Biquaternion in Matrix Element Representations](m4c-representation-the-eigenbasis-and-the-diagonalising-matrix.html), for the 4×4 model
- [Eigenvalues and Diagonalisation](eigenvalues-and-diagonalisation.html), for the matrix theorem
