# __$M_4(\mathbb{C})_L$ Model : The Jordan Basis and the Jordanising Matrix__

## Introduction

A spectrally degenerate biquaternion has a single eigenvalue. In the left regular representation the eigenvalue occurs four times, in two Jordan blocks of size two. The Jordan basis of the algebra gives a basis of $\mathbb{C}^4$ in which the regular matrix is $J_2(Q_t)\otimes\mathrm I_2$, equivalently $\operatorname{diag}(J_2(Q_t),J_2(Q_t))$ in the chain order, and the change to that basis is the $4\times4$ Jordanising matrix. The $2\times2$ similarity that builds the basis has determinant one, so the $4\times4$ determinant is fixed at $\tfrac14$, independent of the element, exactly as in the regular eigenbasis model.

This article constructs the basis, proves the determinant theorem, identifies the freedom and its $*$-unitary subgroup, and describes the defect. It is the $4\times4$ counterpart of *$M_2(\mathbb{C})$ Model : The Jordan Basis and the Jordanising Matrix* and the degenerate counterpart of *$M_4(\mathbb{C})_L$ Model : The Eigenbasis and the Diagonalising Matrix*.

**Conventions.** The algebra and the $4\times4$ model are those of *$M_4(\mathbb{C})_L$ Model : The Product, the Trace and the Determinant*. The element is $\tilde Q=Q_te_t+\vec Q$ with $\vec Q^2=0$ and $\vec Q\neq0$. The $2\times2$ model is $M=\mathsf M_2(\tilde Q)=Q_t\mathrm I_2+Q$, with $Q=\mathsf M_2(\vec Q)$. The nilpotent has singular value

$$
s=\sqrt{2\langle\vec Q\rangle_*},\qquad Q=suv^{\dagger},
$$

with $u,v\in\mathbb{C}^2$ orthonormal. The $2\times2$ Jordanising matrix is $\mathsf S_Q=(u\ s^{-1}v)$. The Jordan basis is $\mathcal{J}=(\vec\Upsilon_-,\tilde\Pi_-,\tilde\Pi_+,\vec\Upsilon_+)$; the corner order is $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$.

**Boundaries.** The flag, the corners, the Jordan pair and the canonical pair are *The Jordan Basis of a Spectrally Degenerate Biquaternion*; the $2\times2$ Jordanising matrix and its determinant are *$M_2(\mathbb{C})$ Model : The Jordan Basis and the Jordanising Matrix*; the projectors are *$M_4(\mathbb{C})_L$ Model : The Spectral Projectors*; the centraliser is *$M_4(\mathbb{C})_L$ Model : The Centraliser and the Double Centraliser*; the eigenbasis model is *$M_4(\mathbb{C})_L$ Model : The Eigenbasis and the Diagonalising Matrix*.

## The Jordan Basis

**The spectral matrix units.** Let

$$
P_{ij}=\mathsf S_Q\,E_{ij}\,\mathsf S_Q^{-1}
$$

be the images of the ordinary $2\times2$ matrix units. The four matrices are a basis of $M_2(\mathbb{C})$ and multiply as the matrix units,

$$
P_{ij}P_{kl}=\delta_{jk}P_{il}.
$$

They are the spectral matrix units: $P_{11}=\tilde\Pi_+$ and $P_{22}=\tilde\Pi_-$ are the canonical idempotents, and $P_{12}=\vec\Upsilon_-$, $P_{21}=\vec\Upsilon_+$ are the generators.

**The $2\times2$ coordinate model.** Every element $\tilde X$ has a unique expansion

$$
\tilde X=\sum_{i,j}X_{ij}P_{ij},\qquad
\mathsf M_2^{\tilde Q}(\tilde X)=\begin{pmatrix}X_{11}&X_{12}\\X_{21}&X_{22}\end{pmatrix}.
$$

The coordinate matrix of the element itself is

$$
\mathsf M_2^{\tilde Q}(\tilde Q)=J_2(Q_t).
$$

**The $4\times4$ basis.** The coordinate columns of $P_{11},P_{12},P_{21},P_{22}$ in the fixed basis $e_t,\vec e_x,\vec e_y,\vec e_z$ form a basis of $\mathbb{C}^4$. It is the **Jordan basis** of the regular model. In the corner order the regular matrix of a general element is

$$
\mathsf M_4^{\tilde Q}(\tilde X)=\mathsf M_2^{\tilde Q}(\tilde X)\otimes\mathrm I_2,
$$

because left multiplication acts on the row index of the matrix units and leaves the copy index untouched. For the element,

$$
\mathsf M_4^{\tilde Q}(\tilde Q)=J_2(Q_t)\otimes\mathrm I_2
=\begin{pmatrix}
Q_t&0&1&0\\
0&Q_t&0&1\\
0&0&Q_t&0\\
0&0&0&Q_t
\end{pmatrix}.
$$

In the chain order $(\vec\Upsilon_-,\tilde\Pi_-,\tilde\Pi_+,\vec\Upsilon_+)$ the same matrix is

$$
\operatorname{diag}\bigl(J_2(Q_t),J_2(Q_t)\bigr).
$$

The two forms differ by the permutation that orders the two chains; the corner order is the one attached to the coordinate model, and the chain order is the one attached to the block diagonal.

**The invariants.** For every element $\tilde X$ with scalar part $X_t$,

$$
\operatorname{Tr}\mathsf M_4^{\tilde Q}(\tilde X)=4X_t,
\qquad
\det\mathsf M_4^{\tilde Q}(\tilde X)=\langle\tilde X\rangle_{\natural}^2.
$$

The trace is four times the scalar part and the determinant is the square of the central scalar, because the regular model is two copies of the $2\times2$ model.

## The Jordanising Matrix

**Definition.** The **Jordanising matrix** $\mathsf S_Q^{(4)}$ is the matrix whose columns are the coordinate columns of $P_{11},P_{12},P_{21},P_{22}$ in the fixed basis. By construction,

$$
\bigl(\mathsf S_Q^{(4)}\bigr)^{-1}\mathsf M_4(\tilde Q)\,\mathsf S_Q^{(4)}
=J_2(Q_t)\otimes\mathrm I_2.
$$

**Theorem (the determinant is fixed).**

$$
\det\mathsf S_Q^{(4)}=\tfrac14
$$

for every element of the sector off the scalar line, independently of $Q$.

*Proof.* The map $X\mapsto\mathsf S_QX\mathsf S_Q^{-1}$ is a linear map of $M_2(\mathbb{C})$ with determinant $(\det\mathsf S_Q)^2/(\det\mathsf S_Q)^2=1$. It sends the matrix-unit basis $E_{ij}$ to the spectral basis $P_{ij}$ with determinant one. The change from the matrix-unit basis to the quaternion coefficient basis is the fixed matrix $\mathsf T$ whose columns are the standard pair

$$
\tilde\Pi_+=\tfrac12(e_t+i\vec e_z),\qquad
\vec\Upsilon_-=\tfrac12(i\vec e_x-\vec e_y),\qquad
\vec\Upsilon_+=\tfrac12(i\vec e_x+\vec e_y),\qquad
\tilde\Pi_-=\tfrac12(e_t-i\vec e_z),
$$

that is

$$
\mathsf T=\frac12
\begin{pmatrix}
1&0&0&1\\
0&i&i&0\\
0&-1&1&0\\
i&0&0&-i
\end{pmatrix},
\qquad
\det\mathsf T=\tfrac14.
$$

The two determinants multiply to $\tfrac14$. ∎

The $2\times2$ determinant modulus $s^{-1}=\lvert\det\mathsf S_Q\rvert$ does not appear: the similarity cancels it. The $4\times4$ Jordanising matrix is therefore never singular on the sector, and its determinant is the determinant of the fixed Peirce change.

**The chain order.** In the chain order the Jordanising matrix is the corner-order matrix with the columns permuted to $(P_{12},P_{22},P_{11},P_{21})$. The permutation has determinant $-1$, so the determinant becomes $-\tfrac14$. The value $\tfrac14$ is attached to the corner order, and the two orders differ only by the permutation that separates the two chains.

**No second chart.** The $2\times2$ construction has no exceptional chart: one of the two columns of $Q$ is nonzero, and the normalised column is the eigenvector. The $4\times4$ matrix inherits the same uniformity. The scalar line $\vec Q=0$ is the boundary, not a chart.

## The Freedom of the Change

**The commutant.** The regular matrix in the corner order is

$$
\mathsf N=J_2(Q_t)\otimes\mathrm I_2
=Q_t\mathrm I_4+E_{12}\otimes\mathrm I_2.
$$

A matrix $\mathsf G$ gives the same Jordan form exactly when it commutes with $\mathsf N$. The commutant of $E_{12}\otimes\mathrm I_2$ is

$$
\left\{\begin{pmatrix}A&B\\0&A\end{pmatrix}:\ A,B\in M_2(\mathbb{C})\right\}
=\mathbb{C}[E_{12}]\otimes M_2(\mathbb{C}),
$$

of complex dimension eight. A block matrix of this form is invertible exactly when $A$ is invertible, so the group of the change is the semidirect product

$$
GL_2(\mathbb{C})\ltimes M_2(\mathbb{C}),
$$

also of complex dimension eight. The general Jordanising matrix is $\mathsf S_Q^{(4)}\mathsf G$ with $\mathsf G$ invertible in this commutant. The $A$ part mixes the two copies and the $B$ part shifts the chains.

**The $2\times2$ subgroup.** The freedom of the $2\times2$ chain is the two-dimensional subgroup

$$
\{G\otimes G^{-\mathsf T}:\ G=\begin{pmatrix}\alpha&\beta\\0&\alpha\end{pmatrix},\ \alpha\neq0\}
$$

of the commutant, the image of the Toeplitz group under the representation $G\mapsto G\otimes G^{-\mathsf T}$; it is isomorphic to $\mathbb{C}^{\times}\ltimes\mathbb{C}$. The remaining six parameters mix the two copies and shift their chains.

**The determinant and the freedom.** Under $\mathsf G$ the determinant is multiplied by $\det\mathsf G$. The value $\tfrac14$ is the determinant of the canonical basis; an arbitrary Jordanising matrix multiplies it by $\det\mathsf G$.

**The $*$-unitary subgroup.** The eigenbasis freedom reduces to $U(2)\times U(2)$ in the normal case. Here no non-scalar element is normal, but the $*$-unitary subgroup of the commutant is still defined. A matrix $\begin{pmatrix}A&B\\0&A\end{pmatrix}$ is $*$-unitary exactly when $B=0$ and $A\in U(2)$. The two copies cannot be rotated independently; only their common $*$-unitary mixing survives.

## The Defect

**No normal non-scalar.** The regular matrix is

$$
\mathsf M_4(\tilde Q)=\mathsf M_2(\tilde Q)\otimes\mathrm I_2.
$$

Its conjugate transpose is $\mathsf M_2(\tilde Q)^{\dagger}\otimes\mathrm I_2$, so

$$
\mathsf M_4(\tilde Q)\mathsf M_4(\tilde Q)^{\dagger}
=\bigl(\mathsf M_2(\tilde Q)\mathsf M_2(\tilde Q)^{\dagger}\bigr)\otimes\mathrm I_2,
$$

and similarly for the other order. The regular matrix is normal exactly when the $2\times2$ matrix is normal, that is exactly when $\tilde Q$ is scalar. Off the scalar line the $4\times4$ matrix is not normal, and there is no $*$-unitary diagonalisation.

**The $*$-unitary form.** In a $*$-unitary basis,

$$
U^{\dagger}\mathsf M_4(\tilde Q)U
=\begin{pmatrix}Q_t&s\\0&Q_t\end{pmatrix}\otimes\mathrm I_2,
$$

with $s=\sqrt{2\langle\vec Q\rangle_*}$. This is two copies of the singular Jordan block. The defect is the same $s$, and it occurs in both blocks.

**The scalar line.** At $\vec Q=0$, the matrix is $Q_t\mathrm I_4$, normal and diagonalisable. Its Jordan type is four blocks $J_1(Q_t)$, every basis is an eigenbasis, and the Jordan form is the scalar matrix, not $J_2(Q_t)\otimes\mathrm I_2$: the defective Jordanising matrix does not exist there. The construction is empty there, not singular.

**The real quaternion case.** For a real quaternion, $\vec Q\in\mathbb{R}^3$ and $\vec Q^2=0$ force $\vec Q=0$. The defective sector has no real points: the real elements of the sector are the real scalars, whose regular matrix is $Q_t\mathrm I_4$. The defect is genuinely complex.

## Change from One Element to Another

**The relative change.** If $\tilde Q$ and $\tilde Q'$ are two elements of the sector off the scalar line, the change from the $Q'$-basis to the $Q$-basis is

$$
\bigl(\mathsf S_Q^{(4)}\bigr)^{-1}\mathsf S_{Q'}^{(4)}.
$$

It is defined up to the freedoms of the two bases, and it satisfies the cocycle

$$
T_{Q''Q}T_{Q'Q''}=T_{Q'Q}.
$$

**The affine family.** If $\tilde Q'=\tilde Q+b e_t$, the same basis works, and

$$
\mathsf M_4^{\tilde Q}(\tilde Q')=\mathsf M_4^{\tilde Q}(\tilde Q)+b\mathrm I_4.
$$

The determinant of the Jordanising matrix is unchanged.

**The scaling.** If $\tilde Q'=a\tilde Q$ with $a\neq0$, the basis changes by

$$
T_4=\operatorname{diag}(1,a,a^{-1},1)
$$

in the corner order, and the $2\times2$ coordinate model by $D=\operatorname{diag}(1,a)$, that is $\mathsf M_2^{\tilde Q'}(\tilde X)=D\mathsf M_2^{\tilde Q}(\tilde X)D^{-1}$. The $4\times4$ determinant is unchanged, because $\det T_4=1$. The $2\times2$ determinant scales by $a^{-1}$ up to a phase, as in the $2\times2$ article; the reciprocal scalings of the two generators cancel in the $4\times4$ change.

**The commuting case.** Two non-scalar elements commute exactly when their vector parts are proportional. Then they share the flag and the idempotents; the two generators are rescaled reciprocally, and each element is put in Jordan form by its own normalisation. A single basis puts both in Jordan form with superdiagonal one only when the vector parts are equal. A general pair has no simultaneous Jordan basis.

## Summary

The Jordan basis is the basis of $\mathbb{C}^4$ formed by the coordinate columns of the spectral matrix units $P_{ij}=\mathsf S_QE_{ij}\mathsf S_Q^{-1}$. In the corner order the regular matrix is $J_2(Q_t)\otimes\mathrm I_2$; in the chain order it is $\operatorname{diag}(J_2(Q_t),J_2(Q_t))$. The canonical Jordanising matrix has determinant $\tfrac14$ for every element of the sector off the scalar line, because the $2\times2$ similarity has determinant one and the fixed Peirce change has determinant $\tfrac14$. In the chain order the determinant is $-\tfrac14$. The freedom is the invertible commutant $GL_2(\mathbb{C})\ltimes M_2(\mathbb{C})$, of complex dimension eight, with $*$-unitary subgroup $U(2)$. No non-scalar element is normal; the best $*$-unitary form is the singular Jordan block doubled, and the defect is the singular value $s=\sqrt{2\langle\vec Q\rangle_*}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P_{ij}=\mathsf S_QE_{ij}\mathsf S_Q^{-1}$ | the spectral matrix units |
| $\mathsf M_2^{\tilde Q}$ | the $2\times2$ Jordan coordinate model |
| $\mathsf M_4^{\tilde Q}$ | the $4\times4$ Jordan coordinate model |
| $\mathsf S_Q^{(4)}$ | the $4\times4$ Jordanising matrix |
| $\tfrac14$ | its determinant in the corner order |
| $-\tfrac14$ | its determinant in the chain order |
| $J_2(Q_t)\otimes\mathrm I_2$ | the regular matrix in the corner order |
| $\operatorname{diag}(J_2,J_2)$ | the regular matrix in the chain order |
| $GL_2(\mathbb{C})\ltimes M_2(\mathbb{C})$ | the freedom of the change |
| $U(2)$ | its $*$-unitary subgroup |
| $s=\sqrt{2\langle\vec Q\rangle_*}$ | the defect |

## Further Reading

- [$M_2(\mathbb{C})$ Model : The Jordan Basis and the Jordanising Matrix](m2c-representation-the-jordan-basis-and-the-jordanising-matrix.html), for the $2\times2$ model
- [The Jordan Basis of a Spectrally Degenerate Biquaternion](the-spectrally-degenerate-sector-and-construction-of-the-jordan-basis-of-a-biquaternion.html), for the flag, the corners and the canonical pair
- [$M_4(\mathbb{C})_L$ Model : The Eigenbasis and the Diagonalising Matrix](m4c-representation-the-eigenbasis-and-the-diagonalising-matrix.html), for the regular counterpart
- [$M_4(\mathbb{C})_L$ Model : The Spectral Projectors](m4c-representation-the-spectral-projectors-and-the-nilpotents.html), for the projectors
- [$M_4(\mathbb{C})_L$ Model : The Centraliser and the Double Centraliser](m4c-representation-the-centraliser-and-the-double-centraliser.html), for the commutant
- [$M_4(\mathbb{C})_L$ Model : The Product, the Trace and the Determinant](m4c-representation-the-matrix-product-and-the-algebra-structure.html), for the fixed model
- [$M_2(\mathbb{C})$ Model : Peirce Coordinates, Matrix Units and the Spinor Planes](m2c-representation-the-peirce-coordinates-matrix-units-and-the-spinor-planes.html), for the fixed Peirce change and its determinant
- [The Spectrum](spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the spectral criterion
