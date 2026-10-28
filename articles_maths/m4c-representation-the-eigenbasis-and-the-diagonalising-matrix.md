# __$M_4(\mathbb{C})_L$ Model : The Eigenbasis and the Diagonalising Matrix__

## Introduction

A spectrally regular biquaternion has an eigenbasis of four vectors. In the regular model the basis is built from the two copies of the $2\times2$ eigenbasis: two vectors for each eigenvalue. The diagonalising matrix is the change to that basis, and its determinant is fixed, independent of the element, because the $2\times2$ diagonalisation acts by a similarity of determinant one.

This article constructs the eigenbasis, proves the diagonal form, computes the diagonalising matrix and its determinant, and describes the freedom of the choice. It absorbs the $4\times4$ material of the former *The Spectrally Regular Sector and Eigenbasis of a Biquaternion in Matrix Element Representations* and is the $4\times4$ counterpart of *$M_2(\mathbb{C})$ Representation : The Eigenbasis and the Diagonalising Matrix*.

**Conventions.** The algebra and the model are those of *$M_4(\mathbb{C})_L$ Representation : The Matrix Product and the Algebra Structure*. The element is $\tilde Q=Q_te_t+\vec Q$ with $B^2=Q_x^2+Q_y^2+Q_z^2\neq0$, and $B$ is a chosen square root. The eigenvalues are $\lambda_\pm=Q_t\pm iB$. The $2\times2$ diagonalising matrix is
$$
\mathsf{C}_Q=\begin{pmatrix}B-Q_z&Q_x-iQ_y\\-Q_x-iQ_y&B-Q_z\end{pmatrix},
\qquad
\det\mathsf{C}_Q=2B(B-Q_z).
$$

**Boundaries.** The projectors and nilpotents are *$M_4(\mathbb{C})_L$ Representation : The Spectral Projectors and the Nilpotents*; the centraliser is *$M_4(\mathbb{C})_L$ Representation : The Centraliser and the Double Centraliser*; the $2\times2$ diagonalising matrix is *$M_2(\mathbb{C})$ Representation : The Eigenbasis and the Diagonalising Matrix*; the construction of the spectral basis is *The Eigenbasis of a Spectrally Regular Biquaternion*.

## The Eigenbasis

**The $2\times2$ eigenbasis.** Let $E_{ij}$ be the ordinary $2\times2$ matrix units and put
$$
P_{ij}=\mathsf{C}_Q\,E_{ij}\,\mathsf{C}_Q^{-1}.
$$
The four matrices $P_{ij}$ are a basis of $M_2(\mathbb{C})$ and multiply as the matrix units,
$$
P_{ij}P_{kl}=\delta_{jk}P_{il}.
$$
They are the spectral matrix units: $P_{11}=\rho_+$ and $P_{22}=\rho_-$ are the spectral projectors, and $P_{12},P_{21}$ are the spectral nilpotents.

**The $2\times2$ coordinate matrix.** Every element $\tilde X$ has a unique expansion
$$
\tilde X=\sum_{i,j}X_{ij}P_{ij},
\qquad
\mathsf{M}_2^{Q}(\tilde X)=\begin{pmatrix}X_{11}&X_{12}\\X_{21}&X_{22}\end{pmatrix}.
$$
The coordinate matrix of the element itself is diagonal:
$$
\mathsf{M}_2^{Q}(\tilde Q)=\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix},
$$
because $\tilde Q=\lambda_+P_{11}+\lambda_-P_{22}$.

**The $4\times4$ eigenbasis.** The four coordinate columns of $P_{11},P_{12},P_{21},P_{22}$ in the fixed basis $e_t,\vec e_x,\vec e_y,\vec e_z$ form a basis of $\mathbb{C}^4$. It is the **eigenbasis** of the regular model. In the order $(P_{11},P_{12},P_{21},P_{22})$, the regular matrix of a general element is
$$
\mathsf{M}_4^{Q}(\tilde X)=\mathsf{M}_2^{Q}(\tilde X)\otimes\mathrm I_2,
$$
because left multiplication acts on the row index of the matrix units and the copy index is untouched.

## The Diagonalising Matrix

**Definition.** The **regular diagonalising matrix** $\mathsf{C}_Q^{(4)}$ is the matrix whose columns are the coordinate columns of $P_{11},P_{12},P_{21},P_{22}$ in the fixed basis. By construction,
$$
\bigl(\mathsf{C}_Q^{(4)}\bigr)^{-1}\mathsf{M}_4(\tilde Q)\,\mathsf{C}_Q^{(4)}
=\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-).
$$

**Theorem (the determinant is fixed).**
$$
\det\mathsf{C}_Q^{(4)}=\tfrac14
$$
for every spectrally regular element, independently of $Q$.

*Proof.* The map $X\mapsto\mathsf{C}_Q\,X\,\mathsf{C}_Q^{-1}$ is a linear map of $M_2(\mathbb{C})$ with determinant $(\det\mathsf{C}_Q)^2/(\det\mathsf{C}_Q)^2=1$. It sends the standard matrix-unit basis $E_{ij}$ to the spectral basis $P_{ij}$ with determinant one. The change from the standard matrix-unit basis to the quaternion coefficient basis $e_t,\vec e_x,\vec e_y,\vec e_z$ is the fixed matrix with columns
$$
\tilde\Pi_+=\tfrac12(e_t+i\vec e_z),\quad
\vec\Upsilon_-=\tfrac12(i\vec e_x-\vec e_y),\quad
\vec\Upsilon_+=\tfrac12(i\vec e_x+\vec e_y),\quad
\tilde\Pi_-=\tfrac12(e_t-i\vec e_z),
$$
whose determinant is $\tfrac14$. The two determinants multiply to $\tfrac14$. $\square$

The $2\times2$ determinant $2B(B-Q_z)$ cancels in the similarity. The regular diagonalising matrix is therefore never singular on the spectrally regular sector, even when the $2\times2$ chart degenerates. What degenerates is the chart, not the $4\times4$ basis.

**The second chart.** When $B=Q_z$ the first chart is singular. The second chart of the $2\times2$ article,
$$
\mathsf{C}_Q'=\begin{pmatrix}-Q_x+iQ_y&B+Q_z\\B+Q_z&Q_x+iQ_y\end{pmatrix},
\qquad
\det\mathsf{C}_Q'=-2B(B+Q_z),
$$
replaces $\mathsf{C}_Q$ in the construction of the $P_{ij}$; its determinant is nonzero at $B=Q_z$ because $B\neq0$. The determinant of the regular change is again $\tfrac14$, by the same similarity argument. The two determinants cannot both vanish, so one of the two charts always applies, and they agree on their overlap up to the freedom below.

## The Eigenbasis in the Fixed Model

**The basis elements are the conjugates of the matrix units.** In the fixed model,
$$
\mathsf M_4(\tilde\Pi_+)=S\operatorname{diag}(E_{11},E_{11})S^{-1},\qquad
\mathsf M_4(\vec\Upsilon_+)=S\operatorname{diag}(E_{12},E_{12})S^{-1},
$$
$$
\mathsf M_4(\vec\Upsilon_-)=S\operatorname{diag}(E_{21},E_{21})S^{-1},\qquad
\mathsf M_4(\tilde\Pi_-)=S\operatorname{diag}(E_{22},E_{22})S^{-1}.
$$
The two assignments of the four basis elements — to the eigenbasis coordinates and to the fixed matrix units — differ by the change of basis $S$. This is the precise sense in which the eigenbasis model is the fixed model conjugated by the Peirce matrix.

**The diagonal form.** In the eigenbasis the regular matrix of $\tilde Q$ is
$$
\mathsf{M}_4^{Q}(\tilde Q)=\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-),
$$
so each eigenvalue occurs twice. The spectral projectors are the diagonal matrices $\operatorname{diag}(1,1,0,0)$ and $\operatorname{diag}(0,0,1,1)$, each of rank two, and the mixed units are the doubled off-diagonal units.

**The trace pairing.** With the ordering $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$, the Gram matrix of the trace pairing $\langle\tilde X,\tilde Y\rangle=\operatorname{Tr}(\tilde X\tilde Y)$ on the regular image is
$$
G=2\begin{pmatrix}
1&0&0&0\\
0&0&1&0\\
0&1&0&0\\
0&0&0&1
\end{pmatrix},
$$
because $\operatorname{Tr}(\tilde\Pi_\pm)=2$, $\operatorname{Tr}(\vec\Upsilon_\pm)=0$, and the mixed products are the rank-two idempotents. The factor two is the duplication: each $2\times2$ pairing entry is counted twice. The trace matrix of the basis is not the identity: the idempotents have trace $2$, the nilpotents trace $0$, and the two mixed products trace $2$.

**The invariants.** For every element $\tilde X$ with eigenbasis coordinates $X_{ij}$,
$$
\operatorname{Tr}\mathsf M_4^{Q}(\tilde X)=2(X_{11}+X_{22})=4X_t,
\qquad
\det\mathsf M_4^{Q}(\tilde X)=(X_{11}X_{22}-X_{12}X_{21})^2=\langle\tilde X\rangle_{\natural}^2.
$$
The trace is four times the scalar part and the determinant is the square of the central scalar, as in the fixed model, because the two models differ by a conjugation.

## The Freedom of the Change

**Right multiplication.** Two eigenbases differ by an element of the commutant of the diagonal form:
$$
\mathsf{C}'=\mathsf{C}_Q^{(4)}G,
\qquad
G\in C\bigl(\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-)\bigr).
$$

**The group.** When $\lambda_+\neq\lambda_-$, the commutant is
$$
GL_2(\mathbb{C})\times GL_2(\mathbb{C}),
$$
of complex dimension eight. The first factor changes the basis inside the two-dimensional $\lambda_+$ eigenspace and the second inside the two-dimensional $\lambda_-$ eigenspace. In the $2\times2$ model the same eigenvalues have multiplicity one and the freedom is $GL_1\times GL_1$, of dimension two. The extra six parameters are the mixing of the two copies.

**The determinant and the freedom.** The determinant of the diagonalising matrix is multiplied by $\det G$ under the freedom. The value $\tfrac14$ is the determinant of one chosen basis, not an invariant of the element.

**The degenerate case.** When $\lambda_+=\lambda_-$, a diagonalisable $M$ is scalar and its commutant is all of $GL_4(\mathbb{C})$; a non-scalar $M$ with repeated eigenvalue is a Jordan block, has no eigenbasis, and is handled by the Jordan decomposition.

## The Normal Case

**Theorem.** The regular matrix is normal,
$$
MM^{\dagger}=M^{\dagger}M,
$$
if and only if $\tilde Q$ is normal in the algebra. In that case the two eigenspaces are orthogonal, the spectral projectors are Hermitian, and the diagonalising matrix can be chosen $*$-unitary. The diagonal form becomes
$$
M=U\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-)U^{\dagger},
\qquad
U\in U(4).
$$

*Proof.* The map $\mathsf{M}_4$ is injective and satisfies $\mathsf{M}_4(\tilde Q^{*})=M^{\dagger}$, so $MM^{\dagger}=M^{\dagger}M$ is equivalent to $\tilde Q\tilde Q^{*}=\tilde Q^{*}\tilde Q$. For a normal element the spectral projectors are Hermitian, and the distinct eigenspaces are orthogonal. $\square$

**The $*$-unitary ambiguity.** In the normal case the freedom is reduced to
$$
U(2)\times U(2),
$$
the $*$-unitary changes inside the two eigenspaces. The determinant of the $*$-unitary diagonalising matrix has modulus one.

**The real quaternion case.** For a real quaternion $h=q_te_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$, the matrix $M=\mathsf{M}_4(h)$ is real and satisfies $M^{\mathsf T}M=(q_t^2+q_x^2+q_y^2+q_z^2)\mathrm I_4$. The eigenbasis can be chosen real. The two copies of the defining representation are then two copies of the same real matrix.

## Change from One Element to Another

**The relative change.** If $\tilde Q$ and $\tilde Q'$ are two spectrally regular elements, the change from the eigenbasis of $\tilde Q$ to that of $\tilde Q'$ is
$$
\bigl(\mathsf{C}_Q^{(4)}\bigr)^{-1}\mathsf{C}_{Q'}^{(4)}.
$$
It is the matrix of the change of spectral coordinates, and it is defined up to the freedoms of the two bases.

**The algebra form.** On the algebra side the same change is the matrix of the linear map that sends the spectral basis $P_{ij}$ of $\tilde Q$ to the spectral basis $P'_{ij}$ of $\tilde Q'$. In the regular model it acts on the two copies by the same $2\times2$ change, so every relative change is doubled.

**The invariant part.** The eigenvalues are the invariants of the element; the eigenbasis is not. Two elements with the same eigenvalues can have different eigenbases, and the relative change measures the difference. In the regular model the relative change has the extra freedom of mixing the two copies, so it is defined only up to $GL_2\times GL_2$.

## Summary

The eigenbasis is the basis of $\mathbb{C}^4$ formed by the coordinate columns of the spectral matrix units $P_{ij}=\mathsf{C}_QE_{ij}\mathsf{C}_Q^{-1}$. In it the regular matrix is $\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-)$, with each eigenvalue twice. The diagonalising matrix has determinant $\tfrac14$ for every spectrally regular element, because the $2\times2$ similarity has determinant one and the $2\times2$ factor cancels. The freedom is $GL_2\times GL_2$ for distinct eigenvalues, reduced to $U(2)\times U(2)$ in the normal case. The fixed Peirce change $S$ is not a diagonalisation; it is the reduction to the two copies that makes the diagonalisation a doubled $2\times2$ problem.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P_{ij}=\mathsf{C}_QE_{ij}\mathsf{C}_Q^{-1}$ | the spectral matrix units |
| $\mathsf{M}_2^{Q}$ | the spectral coordinate model |
| $\mathsf{C}_Q$ | the $2\times2$ diagonalising matrix |
| $\mathsf{C}_Q^{(4)}$ | the regular diagonalising matrix |
| $GL_2\times GL_2$ | the ambiguity for distinct eigenvalues |

## Further Reading

- [$M_4(\mathbb{C})_L$ Representation : The Spectral Projectors and the Nilpotents](m4c-representation-the-spectral-projectors-and-the-nilpotents.html), for the projectors
- [$M_4(\mathbb{C})_L$ Representation : The Centraliser and the Double Centraliser](m4c-representation-the-centraliser-and-the-double-centraliser.html), for the ambiguity
- [$M_2(\mathbb{C})$ Representation : The Eigenbasis and the Diagonalising Matrix](m2c-representation-the-eigenbasis-and-the-diagonalising-matrix.html), for the $2\times2$ matrix
- [The Eigenbasis of a Spectrally Regular Biquaternion](the-spectrally-regular-sector-and-construction-of-the-eigenbasis-of-a-biquaternion.html), for the construction
