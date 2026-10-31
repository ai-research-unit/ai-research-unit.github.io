# __Matrix Representations : The Jordan Basis and the Jordanising Matrix__

## Introduction

A spectrally degenerate biquaternion has one eigenvalue and no eigenbasis. Off the scalar line its $2\times2$ matrix has a single Jordan block, its eigenspace is one-dimensional, and a second vector is supplied by a chain. The change to the Jordan basis is the Jordanising matrix. In the $4\times4$ regular model the same basis gives two Jordan blocks of size two, one in each spinor plane, and the Jordanising matrix has determinant fixed by the frame, independent of the element.

This article develops the Jordan basis, the canonical Jordanising matrix, the determinant of the change in the two displays, the canonical frame, the freedom, the defect and the transitions. It is the degenerate counterpart of *Matrix Representations : The Eigenbasis and the Diagonalising Matrix*.

**Conventions.** The algebra and the displays are those of *Matrix Representations : The Models and the Change of Frame*. The element is $\tilde Q=Q_te_t+\vec Q$ with
$$
\vec Q^2=0,\qquad \vec Q\neq0.
$$
Put $Q=\mathsf M_2(\vec Q)$, a rank-one nilpotent, and $M=\mathsf M_2(\tilde Q)=Q_t\mathrm I_2+Q$. The Hermitian form is $\langle X,Y\rangle_*=\operatorname{Sc}(XY^{*})$, with norm
$$
\langle\vec Q\rangle_*=\sum_{k=1}^{3}\lvert Q_k\rvert^2>0,
\qquad
s=\sqrt{2\langle\vec Q\rangle_*}=\sqrt{\operatorname{Tr}(Q^{\dagger}Q)}.
$$
The Jordan block is
$$
J_2(Q_t)=\begin{pmatrix}Q_t&1\\0&Q_t\end{pmatrix}.
$$
The Peirce frame is the corpus order $\mathcal P=(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$; the corner order is $\mathcal E=(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$; the chain order is $\mathcal J=(\vec\Upsilon_-,\tilde\Pi_-,\tilde\Pi_+,\vec\Upsilon_+)$. The coefficient frame is $\mathcal B=(e_t,\vec e_x,\vec e_y,\vec e_z)$.

**Boundaries.** The flag, the corners and the canonical pair are *The Jordan Basis of a Spectrally Degenerate Biquaternion*; the spectral case is *Matrix Representations : The Eigenbasis and the Diagonalising Matrix*; the projectors are *Matrix Representations : The Spectral Projectors*; the centraliser is *Matrix Representations : The Centraliser and the Double Centraliser*; the nilpotent cone is *Nilpotents*.

## The Jordan Basis

**The basis.** For a spectrally degenerate element off the scalar line, the Jordan basis is
$$
\mathcal J(\tilde Q)=(\vec\Upsilon_-,\ \tilde\Pi_-,\ \tilde\Pi_+,\ \vec\Upsilon_+),
\qquad
\vec\Upsilon_-=\vec Q.
$$
The first pair and the second pair are the two chains for the eigenvalue $Q_t$ under left multiplication. The same four elements in the corner order are the basis adapted to the coordinate model.

**The multiplication table.**

| Product | Value | Product | Value |
|---|---|---|---|
| $\tilde\Pi_+^2$ | $\tilde\Pi_+$ | $\tilde\Pi_-^2$ | $\tilde\Pi_-$ |
| $\tilde\Pi_+\tilde\Pi_-$ | $0$ | $\vec\Upsilon_\pm^2$ | $0$ |
| $\vec\Upsilon_-\vec\Upsilon_+$ | $\tilde\Pi_+$ | $\vec\Upsilon_+\vec\Upsilon_-$ | $\tilde\Pi_-$ |
| $\tilde\Pi_+\vec\Upsilon_-=\vec\Upsilon_-\tilde\Pi_-$ | $\vec\Upsilon_-$ | $\tilde\Pi_-\vec\Upsilon_+=\vec\Upsilon_+\tilde\Pi_+$ | $\vec\Upsilon_+$ |

The table is the matrix-unit table with $P_{11}=\tilde\Pi_+$, $P_{12}=\vec\Upsilon_-$, $P_{21}=\vec\Upsilon_+$ and $P_{22}=\tilde\Pi_-$.

**The coordinate model.** Every element has a unique expansion
$$
\tilde X=X_{11}\tilde\Pi_++X_{12}\vec\Upsilon_-+X_{21}\vec\Upsilon_++X_{22}\tilde\Pi_-,
\qquad
\mathsf M_2^{\tilde Q}(\tilde X)=\begin{pmatrix}X_{11}&X_{12}\\X_{21}&X_{22}\end{pmatrix}.
$$
The map is an isomorphism of algebras, and for the element itself
$$
\mathsf M_2^{\tilde Q}(\tilde Q)=J_2(Q_t),
$$
because $\tilde Q=Q_te_t+\vec\Upsilon_-$ and $e_t=\tilde\Pi_++\tilde\Pi_-$.

**The centraliser.** The matrices commuting with $J_2(Q_t)$ are the upper triangular Toeplitz matrices
$$
\begin{pmatrix}a&b\\0&a\end{pmatrix}.
$$
The centraliser of $\tilde Q$ is therefore $\mathbb{C}[\tilde Q]=\{ae_t+b\vec Q\}$, the dual numbers, of complex dimension two and with only the idempotents $0$ and $e_t$.

## The $2\times2$ Jordanising Matrix

**The definition.** A matrix $\mathsf S\in GL_2(\mathbb{C})$ is Jordanising when
$$
\mathsf S^{-1}M\mathsf S=J_2(Q_t).
$$
Its first column is an eigenvector, annihilated by $Q$, and its second column is a preimage of the first under $Q$.

**The canonical matrix.** Let
$$
Q=suv^{\dagger},\qquad s=\sqrt{2\langle\vec Q\rangle_*},
$$
be the singular-value decomposition of the nilpotent, with $u,v\in\mathbb{C}^2$ orthonormal. Then
$$
\mathsf S_Q=\bigl(u\ \ s^{-1}v\bigr)
$$
is Jordanising. Equivalently, if $c$ is a nonzero column of $Q$,
$$
\mathsf S_Q=\left(\frac{c}{\lVert c\rVert}\ \ \frac{Q^{\dagger}c}{2\langle\vec Q\rangle_*\lVert c\rVert}\right).
$$
The formula is uniform: one of the two columns of $Q$ is nonzero, and the two choices give the same first column up to a phase. There is no second chart.

**The theorem.** The matrix $\mathsf S_Q$ is Jordanising, and
$$
\mathsf M_2(\tilde\Pi_+)=uu^{\dagger},\qquad
\mathsf M_2(\vec\Upsilon_-)=suv^{\dagger}=Q,
$$
$$
\mathsf M_2(\vec\Upsilon_+)=s^{-1}vu^{\dagger},\qquad
\mathsf M_2(\tilde\Pi_-)=vv^{\dagger}.
$$

*Proof.* The columns of $\mathsf S_Q$ are a chain: $Qu=0$ and $Q(s^{-1}v)=u$. Hence $Q\mathsf S_Q=\mathsf S_QE_{12}$ and $M\mathsf S_Q=\mathsf S_QJ_2(Q_t)$. The conjugates of the matrix units follow from $uu^{\dagger}+vv^{\dagger}=\mathrm I_2$.

**The determinant.** Since $u$ and $v$ are orthonormal,
$$
\mathsf S_Q^{\dagger}\mathsf S_Q=\operatorname{diag}(1,s^{-2}),
\qquad
\lvert\det\mathsf S_Q\rvert=\frac{1}{s}=\frac{1}{\sqrt{2\langle\vec Q\rangle_*}}.
$$
The modulus is invariant; the phase is not, because a common phase of $u$ and $v$ multiplies $\mathsf S_Q$ by that phase.

**The $*$-unitary form.** Put $U=(u\ v)$. Since $U$ is $*$-unitary and $U^{\dagger}QU=sE_{12}$,
$$
U^{\dagger}MU=\begin{pmatrix}Q_t&s\\0&Q_t\end{pmatrix}.
$$
The superdiagonal $s$ is the singular value of the nilpotent. No $*$-unitary change removes it: a $*$-unitary diagonalisation would make $M$ normal, and a normal matrix with the single eigenvalue $Q_t$ is $Q_t\mathrm I_2$.

**The decomposition of the change.** The canonical matrix is
$$
\mathsf S_Q=U\operatorname{diag}(1,s^{-1}),
$$
the product of the $*$-unitary singular-value frame and the real scaling that normalises the superdiagonal to one. Its singular values are $1$ and $s^{-1}$.

## The $4\times4$ Jordanising Matrix

**The definition.** The regular Jordanising matrix $\mathsf S_Q^{(4)}$ is the matrix whose columns are the coordinate columns of $P_{11},P_{12},P_{21},P_{22}$ in the Peirce frame, in that order. By construction,
$$
\bigl(\mathsf S_Q^{(4)}\bigr)^{-1}\mathsf M_4^{L}(\tilde Q)\,\mathsf S_Q^{(4)}
=J_2(Q_t)\otimes\mathrm I_2.
$$

**The explicit form.** In the corner order, the regular matrix is
$$
J_2(Q_t)\otimes\mathrm I_2
=\begin{pmatrix}
Q_t&0&1&0\\
0&Q_t&0&1\\
0&0&Q_t&0\\
0&0&0&Q_t
\end{pmatrix}.
$$
In the chain order the same matrix is
$$
\operatorname{diag}\bigl(J_2(Q_t),J_2(Q_t)\bigr).
$$
The two forms differ by the permutation that orders the two chains. The corner order is the order of the coordinate model; the chain order is the order of the block diagonal.

**The determinant in the coefficient frame.**
$$
\det\mathsf S_Q^{(4)}=\tfrac14
$$
in the corner order, for every element of the sector off the scalar line.

*Proof.* The conjugation $X\mapsto\mathsf S_QX\mathsf S_Q^{-1}$ is a linear map of $M_2(\mathbb{C})$ with determinant one, and it sends the matrix-unit basis to the spectral basis with determinant one. The change from the matrix-unit basis to the coefficient basis is the fixed Peirce matrix $T$, whose columns are the four Peirce elements in the corner order,
$$
T=\frac12
\begin{pmatrix}
1&0&0&1\\
0&i&i&0\\
0&-1&1&0\\
i&0&0&-i
\end{pmatrix},
\qquad
\det T=\tfrac14.
$$
The $2\times2$ scalars cancel between $\mathsf S_Q$ and $\mathsf S_Q^{-1}$.

**The determinant in the Peirce frame.** With the same corner order,
$$
\det\mathsf S_Q^{(4)}=-1
$$
in the Peirce frame, because the coefficient display is the Peirce display changed by $C_{\Pi}$: $\det(C_{\Pi}\mathsf S_Q^{(4)})=(-\tfrac14)(-1)=\tfrac14$.

**The chain order.** In the chain order the columns are permuted from $(P_{11},P_{12},P_{21},P_{22})$ to $(P_{12},P_{22},P_{11},P_{21})$. The permutation has determinant $-1$, so the determinant becomes $-\tfrac14$ in the coefficient frame and $+1$ in the Peirce frame. The value $\tfrac14$ is attached to the corner order, not to the element.

**No second chart.** The $2\times2$ construction has no exceptional chart: one of the two columns of $Q$ is nonzero, and its normalisation is the eigenvector. The regular change inherits the same uniformity. The scalar line $\vec Q=0$ is the boundary, not a chart.

## The Canonical Frame

**The pair.** The definite Hermitian form selects a canonical pair of Hermitian idempotents:
$$
\tilde\Pi_+=\frac{\vec Q\vec Q^{*}}{2\langle\vec Q\rangle_*},\qquad
\tilde\Pi_-=\frac{\vec Q^{*}\vec Q}{2\langle\vec Q\rangle_*},\qquad
\vec\Upsilon_+=\frac{\vec Q^{*}}{2\langle\vec Q\rangle_*}.
$$
The pair is orthogonal and complete, and it satisfies
$$
\tilde\Pi_+\vec Q=\vec Q,\qquad
\vec Q\tilde\Pi_-=\vec Q,\qquad
\vec Q\vec\Upsilon_+=\tilde\Pi_+,\qquad
\vec\Upsilon_+\vec Q=\tilde\Pi_-.
$$

**The singular-value frame.** In the fixed model the pair is
$$
\mathsf M_2(\tilde\Pi_+)=uu^{\dagger},\qquad
\mathsf M_2(\vec\Upsilon_-)=suv^{\dagger},\qquad
\mathsf M_2(\vec\Upsilon_+)=s^{-1}vu^{\dagger},\qquad
\mathsf M_2(\tilde\Pi_-)=vv^{\dagger}.
$$
The two idempotents project onto the column space and the row space of $Q$; the two generators are the mixed matrix units scaled by $s$ and $s^{-1}$.

**The uniqueness.** The pair of Hermitian idempotents is unique. The generator $\vec\Upsilon_-=\vec Q$ is fixed by the element, and the product $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+$ fixes $\vec\Upsilon_+$ in the corner. The frame is therefore a function of the element; the only residual freedom of $\mathsf S_Q$ is a common phase, which leaves the frame fixed.

**The boundary.** At $\vec Q=0$ the formulas divide by zero. The element is scalar, every basis is an eigenbasis, the Jordan type is two blocks $J_1(Q_t)$, and no adapted frame is distinguished.

## The Freedom of the Change

**The $2\times2$ freedom.** If $\mathsf S$ is one Jordanising matrix, the others are
$$
\mathsf S\mathsf G,\qquad
\mathsf G=\begin{pmatrix}\alpha&\beta\\0&\alpha\end{pmatrix},
\quad
\alpha\neq0.
$$
The group is $\mathbb{C}^{\times}\ltimes\mathbb{C}$, of complex dimension two. The parameter $\alpha$ is a global scale and $\beta$ is a chain shift.

**The shift.** Put $b=-\beta/\alpha$. The frame becomes
$$
\tilde\Pi_+(b)=\tilde\Pi_++b\vec Q,\qquad
\tilde\Pi_-(b)=\tilde\Pi_--b\vec Q,\qquad
\vec\Upsilon_-(b)=\vec Q,
$$
with $\vec\Upsilon_+(b)$ determined by $\vec Q\vec\Upsilon_+(b)=\tilde\Pi_+(b)$. This is the affine family of adapted pairs. The canonical Hermitian pair is $b=0$.

**The determinant.** Since $\det\mathsf G=\alpha^2$,
$$
\det(\mathsf S_Q\mathsf G)=\alpha^2\det\mathsf S_Q.
$$
The modulus $s^{-1}$ is attached to the canonical matrix, not to an arbitrary representative. The global scale is the only freedom that changes it; the shift does not.

**The $4\times4$ commutant.** In the corner order the regular matrix is
$$
\mathsf N=J_2(Q_t)\otimes\mathrm I_2=Q_t\mathrm I_4+E_{12}\otimes\mathrm I_2.
$$
A matrix $\mathsf G$ gives the same Jordan form exactly when it commutes with $\mathsf N$. The commutant is
$$
\left\{\begin{pmatrix}A&B\\0&A\end{pmatrix}:\ A,B\in M_2(\mathbb{C})\right\}
=\mathbb{C}[E_{12}]\otimes M_2(\mathbb{C}),
$$
of complex dimension eight. Its invertible part is the semidirect product
$$
GL_2(\mathbb{C})\ltimes M_2(\mathbb{C}).
$$
The $A$ part mixes the two spinor planes and the $B$ part shifts the two chains.

**The $2\times2$ subgroup.** The freedom of the $2\times2$ chain is the image of the Toeplitz group under $G\mapsto G\otimes G^{-\mathsf T}$, isomorphic to $\mathbb{C}^{\times}\ltimes\mathbb{C}$. The remaining six parameters mix the two planes and shift their chains.

**The $*$-unitary subgroup.** A matrix $\begin{pmatrix}A&B\\0&A\end{pmatrix}$ is $*$-unitary exactly when $B=0$ and $A\in U(2)$. The two planes cannot be rotated independently; only their common $*$-unitary mixing survives.

## The Defect

**No normal non-scalar.** A non-scalar element of the sector is never normal.

*Proof.* Normality is $[\vec Q,\overline{\vec Q}]=0$, which for a vector part means $\vec Q=\zeta\vec p$ with $\zeta\in\mathbb{C}$ and $\vec p\in\mathbb{R}^3$. Then $\vec Q^2=\zeta^2(\vec p\cdot\vec p)=0$, so $\zeta=0$ or $\vec p=0$; in both cases $\vec Q=0$.

**The $*$-unitary form.** In a $*$-unitary basis,
$$
U^{\dagger}\mathsf M_4^{L}(\tilde Q)U
=\begin{pmatrix}Q_t&s\\0&Q_t\end{pmatrix}\otimes\mathrm I_2.
$$
This is two copies of the singular Jordan block. The defect is the same $s$ in both blocks, and it is the norm of the nilpotent.

**When the change is $*$-unitary.** The canonical $\mathsf S_Q$ is $*$-unitary exactly when $s=1$, that is when $2\langle\vec Q\rangle_*=1$, or $\lVert Q\rVert_F=1$. This is a normalisation of the element, not a generic property.

**The scalar line.** At $\vec Q=0$ the defect vanishes, $M=Q_t\mathrm I_2$ is normal, and every orthonormal basis is an eigenbasis. The Jordan form is $Q_t\mathrm I_2$, not $J_2(Q_t)$: the defective Jordanising matrix does not exist there.

**The real quaternion case.** For a real quaternion, $\vec Q\in\mathbb{R}^3$ and $\vec Q^2=0$ force $\vec Q=0$. The defective sector has no real points: its real elements are the real scalars, whose regular matrix is $Q_t\mathrm I_4$.

## Change from One Element to Another

**The affine family.** If $\tilde Q'=\tilde Q+b e_t$, the flag and the frame are unchanged, and
$$
\mathsf M_2^{\tilde Q}(\tilde Q')=J_2(Q_t+b).
$$
The Jordanising matrix is the same.

**The scaling.** If $\tilde Q'=a\tilde Q$ with $a\neq0$, the canonical frame transforms by
$$
\tilde\Pi_\pm'=\tilde\Pi_\pm,\qquad
\vec\Upsilon_-'=a\vec\Upsilon_-,\qquad
\vec\Upsilon_+'=a^{-1}\vec\Upsilon_+,
$$
and the coordinate model by $D=\operatorname{diag}(1,a)$:
$$
\mathsf M_2^{\tilde Q'}(\tilde X)=D\,\mathsf M_2^{\tilde Q}(\tilde X)\,D^{-1}.
$$
The Jordanising matrix becomes $\mathsf S_{Q'}=\mathsf S_QD^{-1}$ up to a phase, and its determinant modulus scales by $\lvert a\rvert^{-1}$, as required.

**The general transition.** For two elements with different vector lines, the change from the $Q'$-coordinates to the $Q$-coordinates is
$$
T_{Q'Q}=\mathsf S_Q^{-1}\mathsf S_{Q'}.
$$
It satisfies the cocycle
$$
T_{Q''Q}T_{Q'Q''}=T_{Q'Q}.
$$
It preserves the block structure only when the vector parts are proportional; a general transition mixes the two chains.

**The commuting case.** Two non-scalar elements of the sector commute exactly when their vector parts are proportional, because the centraliser is $\mathbb{C}[\tilde Q]$. If $\tilde Q'=a\tilde Q+b e_t$, the two elements share the flag and the idempotents; the generators are rescaled reciprocally. A single basis puts both in Jordan form with superdiagonal one only when $a=1$, that is when the vector parts are equal.

## Summary

The Jordan basis $\mathcal J=(\vec\Upsilon_-,\tilde\Pi_-,\tilde\Pi_+,\vec\Upsilon_+)$ is a system of matrix units; in the corner order the element is $J_2(Q_t)$. The canonical Jordanising matrix is $\mathsf S_Q=(u\ s^{-1}v)$ from the singular-value decomposition $Q=suv^{\dagger}$, with $s=\sqrt{2\langle\vec Q\rangle_*}$; it satisfies $\mathsf S_Q^{-1}M\mathsf S_Q=J_2(Q_t)$ and $\lvert\det\mathsf S_Q\rvert=s^{-1}$. In the regular model the same basis gives $J_2(Q_t)\otimes\mathrm I_2$ in the corner order and $\operatorname{diag}(J_2,J_2)$ in the chain order. The determinant of the regular change is $\tfrac14$ in the coefficient frame and $-1$ in the Peirce frame, independent of the element, because the $2\times2$ scalars cancel in the similarity; the chain order flips both signs. The freedom is $\mathbb{C}^{\times}\ltimes\mathbb{C}$ in $2\times2$ and $GL_2(\mathbb{C})\ltimes M_2(\mathbb{C})$ in $4\times4$, with $*$-unitary subgroup $U(2)$. No non-scalar element is normal, the best $*$-unitary form is the singular Jordan block doubled, and the defect is the singular value $s$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal J=(\vec\Upsilon_-,\tilde\Pi_-,\tilde\Pi_+,\vec\Upsilon_+)$ | the Jordan basis in chain order |
| $\mathcal E=(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$ | the same basis in corner order |
| $\mathsf M_2^{\tilde Q}$ | the Jordan coordinate model |
| $J_2(Q_t)$ | the Jordan block |
| $s=\sqrt{2\langle\vec Q\rangle_*}$ | the singular value of the nilpotent |
| $Q=suv^{\dagger}$ | its singular-value decomposition |
| $\mathsf S_Q=(u\ s^{-1}v)$ | the canonical Jordanising matrix |
| $s^{-1}$ | the modulus of its determinant |
| $\mathsf S_Q^{(4)}$ | the regular Jordanising matrix |
| $\tfrac14$, $-1$ | its determinant in the coefficient and Peirce frames |
| $-\tfrac14$, $+1$ | the same determinants in the chain order |
| $GL_2(\mathbb{C})\ltimes M_2(\mathbb{C})$ | the freedom of the regular change |
| $U(2)$ | its $*$-unitary subgroup |
| $\begin{pmatrix}Q_t&s\\0&Q_t\end{pmatrix}$ | the $*$-unitary form, doubled in $4\times4$ |

## Further Reading

- [Matrix Representations : The Models and the Change of Frame](matrix-representations-the-models-and-the-change-of-frame.html), for the frames and the change law
- [Matrix Representations : The Eigenbasis and the Diagonalising Matrix](matrix-representations-the-eigenbasis-and-the-diagonalising-matrix.html), for the regular case
- [Matrix Representations : The Spectral Projectors](matrix-representations-the-spectral-projectors.html), for the projectors and the nilpotents
- [Matrix Representations : The Centraliser and the Double Centraliser](matrix-representations-the-centraliser-and-the-double-centraliser.html), for the commutant
- [The Jordan Basis of a Spectrally Degenerate Biquaternion](the-jordan-basis-of-a-spectrally-degenerate-biquaternion.html), for the flag and the canonical pair
- [Nilpotents](nilpotents.html), for the nilpotent cone
- [The Spectrum](the-spectrum.html), for the spectral criterion
- [$M_2(\mathbb{C})$ Representation : The Jordan Basis and the Jordanising Matrix](m2c-model-the-jordan-basis-and-the-jordanising-matrix.html), for the $2\times2$ source
- [$M_4(\mathbb{C})_{\mathbb{B}_L}$ Representation : The Jordan Basis and the Jordanising Matrix](m4c-model-the-jordan-basis-and-the-jordanising-matrix.html), for the $4\times4$ source
