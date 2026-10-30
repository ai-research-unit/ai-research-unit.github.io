# __$M_2(\mathbb{C})$ Model : The Jordan Basis and the Jordanising Matrix__

## Introduction

A spectrally degenerate biquaternion has one eigenvalue. Off the scalar line its matrix has a single Jordan block, its eigenspace is two-dimensional while the algebra is four-dimensional, and the two missing vectors are supplied by a chain. The change from the fixed model to a Jordan basis is the Jordanising matrix. It cannot be $*$-unitary, because a non-scalar Jordan block is not normal. The definite Hermitian form nevertheless selects a canonical chain, and the Jordanising matrix becomes the singular-value frame of the nilpotent.

This article develops the Jordan basis and its coordinate model, the canonical and general Jordanising matrices, their determinants and freedom, the trace pairing, the $*$-unitary form and the defect, and the transitions between elements. It is the matrix form of *The Jordan Basis of a Spectrally Degenerate Biquaternion*, §*The Jordan Basis*, §*The Canonical Frame*, §*The Matrix Model* and §*Expansion of Every Biquaternion*, and the degenerate counterpart of *$M_2(\mathbb{C})$ Model : The Eigenbasis and the Diagonalising Matrix*.

**Conventions.** The algebra and the fixed model are those of *$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant*. The element is $\tilde Q=Q_te_t+\vec Q$ with $\vec Q^2=0$ and $\vec Q\neq0$. Put $B^2=\vec Q\cdot\vec Q=0$, $Q=\mathsf M_2(\vec Q)$, and $M=\mathsf M_2(\tilde Q)=Q_t\mathrm I_2+Q$. The nilpotent $Q$ is rank one. The Jordan block is $J_2(Q_t)=\begin{pmatrix}Q_t&1\\0&Q_t\end{pmatrix}$. The corner order is $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$; the chain order is $(\vec\Upsilon_-,\tilde\Pi_-,\tilde\Pi_+,\vec\Upsilon_+)$.

The Hermitian form is $\langle X,Y\rangle_*=\operatorname{Sc}(XY^*)$ of *Conventions of the Twelve Products and the Four Forms*, §*The Form Convention*, with norm $\langle\vec Q\rangle_*=\sum\lvert Q_k\rvert^2>0$. The star is $\tilde Q^*=\bar Q_te_t-\overline{\vec Q}$, and $\mathsf M_2(\tilde Q^*)=M^{\dagger}$. The singular value of the nilpotent is

$$
s=\sqrt{2\langle\vec Q\rangle_*}=\sqrt{\operatorname{Tr}(Q^{\dagger}Q)}.
$$

**Boundaries.** The construction of the flag, the corners and the Jordan pair is *The Jordan Basis of a Spectrally Degenerate Biquaternion*; the canonical pair is there, §*The Canonical Frame*. The spectral projectors of the regular case are *$M_2(\mathbb{C})$ Model : The Spectral Projectors*; the centraliser is *$M_2(\mathbb{C})$ Model : The Centraliser and the Double Centraliser*; the $4\times4$ model is *$M_4(\mathbb{C})_{\mathbb{B}}$ Model : The Jordan Basis and the Jordanising Matrix*; the eigenbasis model is *$M_2(\mathbb{C})$ Model : The Eigenbasis and the Diagonalising Matrix*.

## The Jordan Basis

**The basis.** For a spectrally degenerate $\tilde Q$ with $\vec Q\neq0$, the **Jordan basis** is

$$
\mathcal{J}(\tilde Q)=(\vec\Upsilon_-,\ \tilde\Pi_-,\ \tilde\Pi_+,\ \vec\Upsilon_+),
$$

with $\vec\Upsilon_-=\vec Q$. The first pair and the second pair are the two chains for $Q_t$ under left multiplication. The same four vectors in the corner order $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$ are the coordinate basis. The corner order is the one adapted to the matrix units and to the coordinate model; the chain order is the one adapted to the $4\times4$ Jordan form.

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

The table is the standard matrix-unit table with $P_{11}=\tilde\Pi_+$, $P_{12}=\vec\Upsilon_-$, $P_{21}=\vec\Upsilon_+$ and $P_{22}=\tilde\Pi_-$. It is the same table as in the regular case: the basis is always a system of matrix units, and what changes is the element expanded in it.

**The expansion.** Every element has a unique expansion

$$
\tilde X=X_{11}\tilde\Pi_++X_{12}\vec\Upsilon_-+X_{21}\vec\Upsilon_++X_{22}\tilde\Pi_-,
$$

and the coordinate matrix is

$$
\mathsf M_2^{\tilde Q}(\tilde X)=\begin{pmatrix}X_{11}&X_{12}\\X_{21}&X_{22}\end{pmatrix}.
$$

The superscript records that the model depends on the element through its vector part. The map $\mathsf M_2^{\tilde Q}$ is an algebra isomorphism onto $M_2(\mathbb{C})$. For the element itself,

$$
\mathsf M_2^{\tilde Q}(\tilde Q)=J_2(Q_t),
$$

because $\tilde Q=Q_te_t+\vec\Upsilon_-$ and $e_t=\tilde\Pi_++\tilde\Pi_-$.

**The coordinates by duality.** The four coordinates are the trace pairings

$$
X_{11}=\operatorname{Tr}(\tilde\Pi_+\tilde X),\quad
X_{12}=\operatorname{Tr}(\vec\Upsilon_+\tilde X),\quad
X_{21}=\operatorname{Tr}(\vec\Upsilon_-\tilde X),\quad
X_{22}=\operatorname{Tr}(\tilde\Pi_-\tilde X),
$$

with the two mixed elements exchanged in the dual basis, as in the regular case. The exchange is the statement $\operatorname{Tr}(\vec\Upsilon_-\vec\Upsilon_+)=1=\operatorname{Tr}(\vec\Upsilon_+\vec\Upsilon_-)$.

**The centraliser.** The matrices commuting with $J_2(Q_t)$ are the upper triangular Toeplitz matrices

$$
\begin{pmatrix}a&b\\0&a\end{pmatrix},\qquad a,b\in\mathbb{C}.
$$

Hence the centraliser of $\tilde Q$ is $\mathbb{C}[\tilde Q]=\{ae_t+b\vec Q\}$, the dual numbers, of complex dimension two, with maximal ideal $\mathbb{C}\vec Q$ and only the idempotents $0$ and $e_t$. The statement is the matrix form of *The Centraliser*.

## The Jordanising Matrix

**Definition.** A matrix $\mathsf S\in GL_2(\mathbb{C})$ is **Jordanising** for $\tilde Q$ when

$$
\mathsf S^{-1}\,M\,\mathsf S=J_2(Q_t).
$$

Its first column $w_1$ is an eigenvector and its second column $w_2$ satisfies $Qw_2=w_1$. The first column is annihilated by $M-Q_t\mathrm I_2=Q$, and the second is mapped to the first.

**The general solution.** If $\mathsf S$ is one Jordanising matrix, the others are

$$
\mathsf S\,\mathsf G,\qquad
\mathsf G=\begin{pmatrix}\alpha&\beta\\0&\alpha\end{pmatrix},
\quad \alpha\neq0,\quad \beta\in\mathbb{C}.
$$

*Proof.* If $\mathsf S$ and $\mathsf S'$ both Jordanise, then $\mathsf G=\mathsf S^{-1}\mathsf S'$ satisfies $\mathsf GJ_2(Q_t)=J_2(Q_t)\mathsf G$. A direct computation gives $\mathsf G=\begin{pmatrix}\alpha&\beta\\0&\alpha\end{pmatrix}$, and invertibility gives $\alpha\neq0$. Conversely, such a $\mathsf G$ commutes with $J_2(Q_t)$, so $\mathsf S\mathsf G$ Jordanises. ∎

The group is the semidirect product $\mathbb{C}^{\times}\ltimes\mathbb{C}$ of the invertible Toeplitz matrices, of complex dimension two. The parameter $\alpha$ is a global scale and the parameter $\beta$ is a chain shift; the section *The Freedom of the Change* reads them on the frame.

**The canonical matrix.** Let

$$
Q=suv^{\dagger},\qquad s=\sqrt{2\langle\vec Q\rangle_*},
$$

be the singular-value decomposition of the nilpotent, with $u,v\in\mathbb{C}^2$ orthonormal. Define

$$
\mathsf S_Q=\bigl(u\ \ s^{-1}v\bigr).
$$

Equivalently, if $c$ is a nonzero column of $Q$, then

$$
\mathsf S_Q=\left(\frac{c}{\lVert c\rVert}\ \ \frac{Q^{\dagger}c}{2\langle\vec Q\rangle_*\lVert c\rVert}\right).
$$

The formula is uniform: one of the two columns of $Q$ is nonzero, and the two choices give the same first column up to a phase. There is no second chart.

**Theorem (canonical Jordanisation).** The matrix $\mathsf S_Q$ is Jordanising, and the images of the matrix units are the canonical frame:

$$
\mathsf M_2(\tilde\Pi_+)=\mathsf S_QE_{11}\mathsf S_Q^{-1}=uu^{\dagger},\qquad
\mathsf M_2(\vec\Upsilon_-)=\mathsf S_QE_{12}\mathsf S_Q^{-1}=suv^{\dagger}=Q,
$$

$$
\mathsf M_2(\vec\Upsilon_+)=\mathsf S_QE_{21}\mathsf S_Q^{-1}=s^{-1}vu^{\dagger},\qquad
\mathsf M_2(\tilde\Pi_-)=\mathsf S_QE_{22}\mathsf S_Q^{-1}=vv^{\dagger}.
$$

*Proof.* The columns of $\mathsf S_Q$ are a chain: $Qu=0$ and $Q(s^{-1}v)=u$. Hence $Q\mathsf S_Q=\mathsf S_QE_{12}$, and $M\mathsf S_Q=\mathsf S_Q(Q_t\mathrm I_2+E_{12})=\mathsf S_QJ_2(Q_t)$. The conjugates of the matrix units follow from the definition of $\mathsf S_Q$ and the identities $uu^{\dagger}+vv^{\dagger}=\mathrm I_2$ and $uv^{\dagger}=Q/s$. ∎

The four matrices are the canonical frame of *The Jordan Basis of a Spectrally Degenerate Biquaternion*, §*The Canonical Frame*:

$$
\tilde\Pi_+=\frac{\vec Q\vec Q^*}{2\langle\vec Q\rangle_*},\qquad
\tilde\Pi_-=\frac{\vec Q^*\vec Q}{2\langle\vec Q\rangle_*},\qquad
\vec\Upsilon_+=\frac{\vec Q^*}{2\langle\vec Q\rangle_*}.
$$

The two idempotents project onto the column and the row space of $Q$, and the two generators are the mixed matrix units scaled by $s$ and $s^{-1}$.

**Theorem (the determinant).** The determinant of the canonical Jordanising matrix satisfies

$$
\lvert\det\mathsf S_Q\rvert=\frac{1}{s}=\frac{1}{\sqrt{2\langle\vec Q\rangle_*}}.
$$

*Proof.* Since $u$ and $v$ are orthonormal, $\mathsf S_Q^{\dagger}\mathsf S_Q=\operatorname{diag}(1,s^{-2})$. Taking determinants gives $\lvert\det\mathsf S_Q\rvert^2=s^{-2}$. ∎

The phase of the determinant is not canonical: a common phase of $u$ and $v$ multiplies $\mathsf S_Q$ by that phase. The modulus is the invariant.

**The worked example.** Take

$$
\tilde Q=e_t+\vec e_x+i\vec e_y.
$$

Then $Q_t=1$,

$$
Q=\begin{pmatrix}0&-2i\\0&0\end{pmatrix},\qquad
s=2,\qquad
\langle\vec Q\rangle_*=2.
$$

The first column of $Q$ vanishes; the second is $c=(-2i,0)$. Hence $u=(-i,0)$, $Q^{\dagger}u=(0,2)$ and

$$
\mathsf S_Q=\begin{pmatrix}-i&0\\0&\tfrac12\end{pmatrix}.
$$

The check is

$$
\mathsf S_Q^{-1}\,\mathsf M_2(\tilde Q)\,\mathsf S_Q
=\begin{pmatrix}1&1\\0&1\end{pmatrix},
$$

and the canonical frame is

$$
\tilde\Pi_+=\tfrac12(e_t+i\vec e_z),\qquad
\tilde\Pi_-=\tfrac12(e_t-i\vec e_z),\qquad
\vec\Upsilon_-=\vec e_x+i\vec e_y,\qquad
\vec\Upsilon_+=\tfrac14(-\vec e_x+i\vec e_y).
$$

The same element is computed in *The Jordan Basis of a Spectrally Degenerate Biquaternion*, §*A Worked Example*.

## The Canonical Frame

**The pair.** The definite Hermitian form selects the value $b=0$ of the affine family of adapted pairs, as proved in *The Jordan Basis of a Spectrally Degenerate Biquaternion*, §*The Canonical Frame*. In the present notation,

$$
\tilde\Pi_+=\frac{\vec Q\vec Q^*}{2\langle\vec Q\rangle_*},\qquad
\tilde\Pi_-=\frac{\vec Q^*\vec Q}{2\langle\vec Q\rangle_*},\qquad
\vec\Upsilon_+=\frac{\vec Q^*}{2\langle\vec Q\rangle_*}.
$$

The pair is Hermitian, orthogonal and complete, and it satisfies

$$
\tilde\Pi_+\vec Q=\vec Q,\qquad
\vec Q\tilde\Pi_-=\vec Q,\qquad
\vec Q\vec\Upsilon_+=\tilde\Pi_+,\qquad
\vec\Upsilon_+\vec Q=\tilde\Pi_-.
$$

**The matrix form.** In the fixed model the pair is the singular-value frame of the nilpotent:

$$
\mathsf M_2(\tilde\Pi_+)=uu^{\dagger},\qquad
\mathsf M_2(\vec\Upsilon_-)=suv^{\dagger},\qquad
\mathsf M_2(\vec\Upsilon_+)=s^{-1}vu^{\dagger},\qquad
\mathsf M_2(\tilde\Pi_-)=vv^{\dagger}.
$$

The two idempotents are the support idempotents: the orthogonal projections onto the column space and the row space of $Q$, and the two generators are the two mixed matrix units scaled by $s$ and $s^{-1}$.

**Uniqueness.** The pair of Hermitian idempotents is unique. The generator $\vec\Upsilon_-=\vec Q$ is fixed by the element, and the product $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+$ fixes $\vec\Upsilon_+$ in the corner. The frame is therefore a function of the element, not of a choice. The only residual freedom of the matrix $\mathsf S_Q$ is a common phase, which leaves the frame fixed.

**The boundary.** At $\vec Q=0$ the formulas divide by zero. The element is scalar, every basis is an eigenbasis, the Jordan type of $M$ is two blocks $J_1(Q_t)$, and no adapted frame is distinguished. The scalar line is the boundary of the construction, not a chart of it.

## The $*$-Unitary Form and the Defect

**No normal non-scalar.** A matrix is normal when $MM^{\dagger}=M^{\dagger}M$. A non-scalar element of the sector is never normal.

*Proof.* Normality of $M$ is $[\vec Q,\overline{\vec Q}]=0$, which for a vector part means $\vec Q=\zeta\vec p$ with $\zeta\in\mathbb{C}$ and $\vec p\in\mathbb{R}^3$. Then $\vec Q^2=\zeta^2(\vec p\cdot\vec p)=0$, so $\zeta=0$ or $\vec p=0$; in both cases $\vec Q=0$. ∎

**The $*$-unitary form.** Put $U=(u\ v)$. Since $U$ is $*$-unitary and $U^{\dagger}QU=sE_{12}$,

$$
U^{\dagger}MU=
\begin{pmatrix}Q_t&s\\0&Q_t\end{pmatrix}.
$$

The superdiagonal $s=\sqrt{2\langle\vec Q\rangle_*}$ is the singular value of the nilpotent. No $*$-unitary change removes it: a $*$-unitary diagonalisation would make $M$ normal, and a normal matrix with the single eigenvalue $Q_t$ is $Q_t\mathrm I_2$, which has no superdiagonal. The canonical Jordanising matrix is

$$
\mathsf S_Q=U\operatorname{diag}(1,s^{-1}),
$$

the product of the $*$-unitary singular-value frame and the real scaling that normalises the superdiagonal to one.

**The polar decomposition.** The decomposition $\mathsf S_Q=U\operatorname{diag}(1,s^{-1})$ is the polar decomposition of $\mathsf S_Q$, with positive factor $\operatorname{diag}(1,s^{-1})$ in the $u,v$ basis. The singular values of $\mathsf S_Q$ are $1$ and $s^{-1}$, and the determinant modulus $s^{-1}$ is the reciprocal of the defect.

**When the matrix is $*$-unitary.** The canonical $\mathsf S_Q$ is $*$-unitary exactly when $s=1$, that is when $2\langle\vec Q\rangle_*=1$, or $\lVert Q\rVert_F=1$. This is a normalisation of the element, not a generic property. In the regular case a normal element always has a $*$-unitary diagonalising matrix; in the degenerate case the best $*$-unitary form is the singular Jordan block above, and the defect is the norm of the nilpotent.

**The scalar line.** At $\vec Q=0$ the defect vanishes, $M=Q_t\mathrm I_2$ is normal, and every orthonormal basis is an eigenbasis. The $*$-unitary form is the scalar matrix and the Jordan form is $Q_t\mathrm I_2$, not $J_2(Q_t)$: the defective Jordanising matrix does not exist there, and any $*$-unitary matrix diagonalises the element.

## The Jordan Basis in the Fixed Model

**The basis elements are the conjugates of the matrix units.** In the fixed model,

$$
\mathsf M_2(\tilde\Pi_+)=\mathsf S_QE_{11}\mathsf S_Q^{-1},\qquad
\mathsf M_2(\vec\Upsilon_-)=\mathsf S_QE_{12}\mathsf S_Q^{-1},
$$

$$
\mathsf M_2(\vec\Upsilon_+)=\mathsf S_QE_{21}\mathsf S_Q^{-1},\qquad
\mathsf M_2(\tilde\Pi_-)=\mathsf S_QE_{22}\mathsf S_Q^{-1}.
$$

The two assignments of the four basis elements — to the Jordan coordinates and to the fixed matrix units — differ by the change of basis $\mathsf S_Q$. This is the precise sense in which the Jordan model is the fixed model conjugated by the Jordanising matrix.

**The trace pairing.** With the corner order, the Gram matrix of the trace pairing $\langle X,Y\rangle=\operatorname{Tr}(XY)$ is

$$
G=\begin{pmatrix}
1&0&0&0\\
0&0&1&0\\
0&1&0&0\\
0&0&0&1
\end{pmatrix},
$$

because $\operatorname{Tr}(\tilde\Pi_\pm)=1$, $\operatorname{Tr}(\vec\Upsilon_\pm)=0$, and $\operatorname{Tr}(\vec\Upsilon_-\vec\Upsilon_+)=\operatorname{Tr}(\tilde\Pi_+)=1$ and $\operatorname{Tr}(\vec\Upsilon_+\vec\Upsilon_-)=\operatorname{Tr}(\tilde\Pi_-)=1$. The trace matrix is not the identity: the idempotents have trace one, the nilpotents trace zero, and the two mixed products trace one.

**The invariants.** For every element $\tilde X$ with Jordan coordinates $X_{ij}$,

$$
\operatorname{Tr}\mathsf M_2^{\tilde Q}(\tilde X)=X_{11}+X_{22}=2X_t,
\qquad
\det\mathsf M_2^{\tilde Q}(\tilde X)=X_{11}X_{22}-X_{12}X_{21}=\langle\tilde X\rangle_{\natural}.
$$

The trace is twice the scalar part and the determinant is the central scalar, as in the fixed model.

## The Freedom of the Change

**The Toeplitz group.** The general Jordanising matrix is $\mathsf S_Q\mathsf G$ with

$$
\mathsf G=\begin{pmatrix}\alpha&\beta\\0&\alpha\end{pmatrix},\qquad \alpha\neq0.
$$

The group is $\mathbb{C}^{\times}\ltimes\mathbb{C}$, of complex dimension two.

**The global scale.** The matrix $\alpha\mathrm I_2$ leaves every conjugate $\mathsf S_QE_{ij}\mathsf S_Q^{-1}$ fixed. It is the redundancy of the matrix relative to the frame, and it is the only parameter that changes the determinant.

**The chain shift.** Put $b=-\beta/\alpha$. The frame becomes

$$
\tilde\Pi_+(b)=\tilde\Pi_++b\vec Q,\qquad
\tilde\Pi_-(b)=\tilde\Pi_- -b\vec Q,\qquad
\vec\Upsilon_-(b)=\vec Q,
$$

with $\vec\Upsilon_+(b)$ determined by $\vec Q\vec\Upsilon_+(b)=\tilde\Pi_+(b)$. This is the affine family of adapted pairs of *The Jordan Basis of a Spectrally Degenerate Biquaternion*, §*The Chosen Frame*. The canonical Hermitian pair is $b=0$. The shift $\beta$ does not change the determinant.

**The determinant.** Since $\det\mathsf G=\alpha^2$,

$$
\det(\mathsf S_Q\mathsf G)=\alpha^2\det\mathsf S_Q.
$$

The modulus $s^{-1}$ is attached to the canonical matrix, not to an arbitrary matrix representative. The global scale is the only freedom that changes it.

**The canonical representative.** Among the canonical matrices, only a common phase remains. The modulus of the determinant is fixed, and a chart fixes the phase by requiring the first nonzero entry of $u$ to be positive real.

**The eigenbasis comparison.** In the regular case the freedom is $GL_1\times GL_1$, two independent rescalings of the two eigenvectors. Here the repeated eigenvalue identifies the two scales and adds a shift; the group is the two-dimensional solvable group, not the torus. The shift is the choice of complement in the kernel, and the global scale is the normalisation of the chain.

## Change from One Element to Another

**The affine family.** If $\tilde Q'=\tilde Q+b e_t$, the flag and the frame are unchanged, and

$$
\mathsf M_2^{\tilde Q}(\tilde Q')=J_2(Q_t+b).
$$

The Jordanising matrix is the same. The scalar part shifts the eigenvalue and leaves the basis alone.

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

For $a>0$ the Jordanising matrix is $\mathsf S_{Q'}=\mathsf S_QD^{-1}$; for complex $a$ the identity holds up to a global phase. Its determinant modulus scales by $\lvert a\rvert^{-1}$, so it becomes $s^{-1}/\lvert a\rvert=s'^{-1}$, as required.

**The general transition.** For two elements with different vector lines, the change from the $Q'$-coordinates to the $Q$-coordinates is

$$
T_{Q'Q}=\mathsf S_Q^{-1}\mathsf S_{Q'}.
$$

It satisfies the cocycle

$$
T_{Q''Q}T_{Q'Q''}=T_{Q'Q}.
$$

It preserves the block structure only when the vector parts are proportional; the superdiagonal is then rescaled by the ratio, and a general transition mixes the two blocks.

**The commuting case.** Two non-scalar elements of the sector commute exactly when their vector parts are proportional, because the centraliser is $\mathbb{C}[\tilde Q]$. If $\tilde Q'=a\tilde Q+b e_t$, the two elements share the flag and the idempotents; the two generators are rescaled reciprocally, and each element is put in Jordan form by its own normalisation. A single basis puts both in Jordan form with superdiagonal one only when $a=1$, that is when the vector parts are equal. A general pair has neither a common flag nor a simultaneous Jordan basis, just as a general pair of regular elements has no simultaneous eigenbasis.

## Summary

The Jordan basis $(\vec\Upsilon_-,\tilde\Pi_-,\tilde\Pi_+,\vec\Upsilon_+)$ is a system of matrix units; in the corner order the element is $J_2(Q_t)$. The Jordanising matrix has the canonical representative $\mathsf S_Q=(u\ s^{-1}v)$ from the singular-value decomposition $Q=suv^{\dagger}$ of the nilpotent, with $s=\sqrt{2\langle\vec Q\rangle_*}$. It satisfies $\mathsf S_Q^{-1}M\mathsf S_Q=J_2(Q_t)$, and its determinant has modulus $s^{-1}$. The general representative is $\mathsf S_Q\mathsf G$ with $\mathsf G$ upper triangular Toeplitz; the shift is the affine family of adapted pairs and the scale is the normalisation of the chain. A non-scalar element of the sector is never normal; the best $*$-unitary form is $\begin{pmatrix}Q_t&s\\0&Q_t\end{pmatrix}$, and the defect $s$ is the norm of the nilpotent. Within a fixed vector line the frame is fixed and the two generators are rescaled reciprocally; a shift of the scalar part leaves the basis unchanged.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$ | the Jordan basis in corner order |
| $(\vec\Upsilon_-,\tilde\Pi_-,\tilde\Pi_+,\vec\Upsilon_+)$ | the Jordan basis in chain order |
| $\mathsf M_2^{\tilde Q}$ | the Jordan coordinate model |
| $J_2(Q_t)$ | the Jordan block |
| $s=\sqrt{2\langle\vec Q\rangle_*}$ | the singular value of the nilpotent |
| $Q=suv^{\dagger}$ | the singular-value decomposition |
| $\mathsf S_Q=(u\ s^{-1}v)$ | the canonical Jordanising matrix |
| $\lvert\det\mathsf S_Q\rvert=s^{-1}$ | its determinant modulus |
| $\mathsf G=\begin{pmatrix}\alpha&\beta\\0&\alpha\end{pmatrix}$ | the freedom of the change |
| $b=-\beta/\alpha$ | the affine parameter of the frame |
| $U=(u\ v)$ | the $*$-unitary singular-value frame |
| $U^{\dagger}MU=\begin{pmatrix}Q_t&s\\0&Q_t\end{pmatrix}$ | the $*$-unitary form |
| $T_{Q'Q}=\mathsf S_Q^{-1}\mathsf S_{Q'}$ | the transition matrix |

## Further Reading

- [The Jordan Basis of a Spectrally Degenerate Biquaternion](the-jordan-basis-of-a-spectrally-degenerate-biquaternion.html), for the flag, the corners, the Jordan pair and the canonical frame
- [$M_4(\mathbb{C})_{\mathbb{B}}$ Model : The Jordan Basis and the Jordanising Matrix](m4c-model-the-jordan-basis-and-the-jordanising-matrix.html), for the $4\times4$ model
- [$M_2(\mathbb{C})$ Model : The Eigenbasis and the Diagonalising Matrix](m2c-model-the-eigenbasis-and-the-diagonalising-matrix.html), for the regular counterpart
- [$M_2(\mathbb{C})$ Model : Peirce Coordinates, Matrix Units and the Spinor Planes](m2c-model-the-peirce-coordinates-matrix-units-and-the-spinor-planes.html), for the fixed matrix units
- [$M_2(\mathbb{C})$ Model : The Centraliser and the Double Centraliser](m2c-model-the-centraliser-and-the-double-centraliser.html), for the dual numbers
- [$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant](m2c-model-the-product-the-trace-and-the-determinant.html), for the fixed model
- [The Spectrum](the-spectrum.html), for the spectral criterion
- [Conventions in Mathematics](conventions-in-mathematics.html), for the Hermitian form and norm
