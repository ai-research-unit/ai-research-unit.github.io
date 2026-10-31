# __Matrix Representations : $GL_2(\mathbb{C})$, $SL_2(\mathbb{C})$ and the Determinant__

## Introduction

The units of the biquaternion algebra are the elements of nonzero norm, and the norm-one elements are the spin group. The $2\times2$ model reads the unit group as $GL_2(\mathbb{C})$ and the norm-one group as $SL_2(\mathbb{C})$; the $4\times4$ regular model reads the same groups as a four-dimensional subgroup of $GL_4(\mathbb{C})$ and a three-dimensional subgroup of $SL_4(\mathbb{C})$. The determinant of the regular matrix is the square of the determinant of the $2\times2$ matrix, and that square is the only numerical difference between the two readings.

This article develops the group isomorphism, the determinant sequence and its splittings, the level sets of the norm, the Bruhat decomposition, the centre and the double covers. It is the group-level companion of *Matrix Representations : Trace, Determinant and the Biquaternion Norm*.

**Conventions.** The algebra and the models are those of *Matrix Representations : The Models and the Change of Frame*. The norm is $N=\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2$, and
$$
\det\mathsf M_2(\tilde Q)=\langle\tilde Q\rangle_{\natural},
\qquad
\det\mathsf M_4^L(\tilde Q)=\langle\tilde Q\rangle_{\natural}^2.
$$
The unit group is $\mathbb{B}^{\times}=\{\tilde Q:N\neq0\}$, and the norm-one group is $\mathbb{B}^{\times}_1=\{\tilde Q:N=1\}$. The image is $M_4(\mathbb{C})_{\mathbb{B},L}=\mathsf M_4^L(\mathbb{B})$.

**Boundaries.** The unit group as a topological group is *The Biquaternion Unit Group as a Topological Group*; the norm-one group and the polar factors are *The Polar Decomposition of a N-Regular Biquaternion*; the $*$-unitary group is *The Unitary Group of the Biquaternion Algebra*; the level sets and the sector are *The N-Regular Sector*; the polar decomposition of a matrix is *Matrix Representations : The Polar Decomposition of a Matrix*; the projective line is *Matrix Representations : The Projective Line and the Möbius Action*.

## Common Aspects

The units of the biquaternion algebra are the elements of nonzero norm, and the norm-one elements are the spin group. The entry model reads the unit group as $GL_2(\mathbb{C})$ and the norm-one group as $SL_2(\mathbb{C})$; the regular model reads the same groups as a four-dimensional subgroup of $GL_4(\mathbb{C})$ and a three-dimensional subgroup of $SL_4(\mathbb{C})$. The determinant of the regular matrix is the square of the entry determinant, and that square is the only numerical difference between the two readings.

**The group isomorphism.** The map $\mathsf M_2$ is an isomorphism of complex Lie groups
$$
\mathbb{B}^{\times}\longrightarrow GL_2(\mathbb{C}),\qquad
\tilde Q\longmapsto\mathsf M_2(\tilde Q),
$$
and it carries the norm-one subgroup onto $SL_2(\mathbb{C})$. The map $\mathsf M_4^L$ is an injective homomorphism whose image is a closed complex subgroup of $GL_4(\mathbb{C})$ isomorphic to $GL_2(\mathbb{C})$, and $\{\tilde Q:N=1\}\cong SL_2(\mathbb{C})\subset SL_4(\mathbb{C})$. Both maps are holomorphic and complex linear in the four coefficients; their inverses are polynomial on the open set where the determinant is nonzero. The image of $\mathsf M_4^L$ has complex dimension four, while $GL_4(\mathbb{C})$ has dimension sixteen, so every group statement about the regular model is a statement about the image, not about the ambient group.

**The determinant sequence.**
$$
1\longrightarrow SL_2(\mathbb{C})\longrightarrow GL_2(\mathbb{C})\xrightarrow{\ \det\ }\mathbb{C}^{\times}\longrightarrow1.
$$
The kernel is $SL_2$ by definition; the determinant is surjective because $\operatorname{diag}(\lambda,1)$ has determinant $\lambda$; and $SL_2$ is normal. In the regular model the same sequence is read on the image, with $\det\mathsf M_4^L(\tilde Q)=N^2$.

**The splittings.** The sequence splits, but not centrally. The map $s(\lambda)=\operatorname{diag}(\lambda,1)$ is a homomorphism with determinant $\lambda$, so $GL_2\cong SL_2\rtimes\mathbb{C}^{\times}$, the action being conjugation by $\operatorname{diag}(\lambda,1)$. A central splitting would send $\lambda$ to $\mu(\lambda)\mathrm I_2$ with $\mu(\lambda)^2=\lambda$; a homomorphism $\mu$ would give $\mu(1)=1$ and $\mu(-1)^2=-1$, while $\mu((-1)(-1))=\mu(1)=1$, a contradiction. There is therefore no central subgroup isomorphic to $\mathbb{C}^{\times}$ mapping isomorphically to the determinant. In the regular model the scalar is $\mu(\lambda)\mathrm I_4$, its determinant is $\mu(\lambda)^4$, and the same contradiction appears with the fourth power.

**The covering.** The multiplication map
$$
\mathbb{C}^{\times}\times SL_2(\mathbb{C})\longrightarrow GL_2(\mathbb{C}),\qquad
(\lambda,U)\longmapsto\lambda U,
$$
is surjective, because every $M$ is $\lambda U$ with $\lambda^2=\det M$ and $U=M/\lambda\in SL_2$. Its kernel is $\{(\lambda,\lambda^{-1}\mathrm I_2):\lambda^2=1\}=\{\pm1\}$, of order two, so
$$
GL_2(\mathbb{C})\cong\big(\mathbb{C}^{\times}\times SL_2(\mathbb{C})\big)/\{\pm1\}.
$$
In the regular model the map is $(\lambda,U)\mapsto\lambda\,\mathrm I_2\otimes U$, with the same kernel and determinant $\lambda^4$.

**The level sets.** For $c\neq0$, $\{N=c\}$ is a smooth complex hypersurface of complex dimension three: the gradient of $N$ vanishes only at $\tilde Q=0$, which is not on the level set, and the quadric is connected. In the regular model it is the intersection of the image with $\det=c^2$. The level set $N=1$ is $SL_2(\mathbb{C})$, embedded in $SL_4(\mathbb{C})$; it is not compact, since $\operatorname{diag}(r,r^{-1})$ has determinant one and escapes as $r\to\infty$. Each nonzero level set is homogeneous,
$$
\{N=c\}\cong(SL_2\times SL_2)/SL_2,
$$
under $(A,B)\cdot M=AMB^{-1}$, with the diagonal $SL_2$ as stabiliser. The level set $c=0$ is the null cone, not smooth: it is the cone over the Segre quadric $\mathbb{P}^1\times\mathbb{P}^1$, with the apex at the origin.

**The centre and the projective group.** The centre of $GL_2$ is $\mathbb{C}^{\times}\mathrm I_2$, of complex dimension one, and in the regular model $\mathbb{C}^{\times}\mathrm I_4$. The inner automorphism group is
$$
PGL_2(\mathbb{C})=GL_2(\mathbb{C})/\mathbb{C}^{\times}\mathrm I_2,
$$
of complex dimension three; it is the group of algebra automorphisms of $M_2(\mathbb{C})$ and, by transport, of $\mathbb{B}$. The determinant is not defined on $PGL_2$: under $M\mapsto\lambda M$ it changes by $\lambda^2$ in the entry model and by $\lambda^4$ in the regular model, so only its vanishing locus and its class are defined.

**The double covers.** Three actions of $SL_2(\mathbb{C})$ have kernel $\{\pm\mathrm I_2\}$: conjugation on $M_2(\mathbb{C})$, conjugation on the Hermitian matrices, and the Möbius action on $\mathbb{P}^1$. In the regular model the kernel is $\{\pm\mathrm I_4\}$. The conjugation action of $SU(2)$ on the Hermitian traceless matrices preserves $\det=-|\vec x|^2$ and gives $SU(2)\to SO(3)$, a double cover with $SO(3)\cong\mathbb{RP}^3$. The conjugation action of $SL_2(\mathbb{C})$ on the Hermitian matrices preserves $x_0^2-|\vec x|^2$ and the positive cone and gives $SL_2(\mathbb{C})\to SO^+(1,3)$, a double cover; since $SL_2$ is simply connected, it is the universal cover and $\pi_1(SO^+(1,3))=\mathbb{Z}/2$. The Möbius action gives $SL_2\to PSL_2\cong PGL_2$, also a double cover.

| Cover | Base | Kernel | Fibre |
|---|---|---|---|
| $SU(2)\to SO(3)$ | rotations | $\{\pm\mathrm I_2\}$ | two points |
| $SL_2(\mathbb{C})\to SO^+(1,3)$ | Lorentz | $\{\pm\mathrm I_2\}$ | two points |
| $SL_2(\mathbb{C})\to PSL_2(\mathbb{C})$ | Möbius | $\{\pm\mathrm I_2\}$ | two points |
| $\mathbb{C}^{\times}\times SL_2\to GL_2$ | units | $\{\pm(1,\mathrm I_2)\}$ | two points |
| $SU(2)\to S^2$ (Hopf) | sphere | $U(1)$ | circle |

The last row is not a covering; it is the Hopf fibration, included for contrast.

## The Coefficient Frame

**The image and the determinant.** In the coefficient frame the regular matrix is $X=\mathsf M_4^L(\tilde Q)=Q_t\mathrm I_4+Q_xL_x+Q_yL_y+Q_zL_z$. The image is a closed four-complex-dimensional subgroup of $GL_4(\mathbb{C})$, and
$$
\det X=\langle\tilde Q\rangle_{\natural}^2,
\qquad
X^{-1}=\frac{\mathsf M_4^L(\tilde Q^{\natural})}{\langle\tilde Q\rangle_{\natural}}
=\frac{X^{\mathsf T}}{\langle\tilde Q\rangle_{\natural}},
$$
so the inverse is polynomial on the invertible set. The determinant sequence on the image is $1\to SL_2\to GL_2\to\mathbb{C}^{\times}\to1$, read through $N^2$.

**The centre and the splitting.** The centre of the image is $\mathbb{C}^{\times}\mathrm I_4$. A central splitting would need $\mu(\lambda)\mathrm I_4$ with $\mu(\lambda)^4=\lambda$, and the same $\mu(-1)$ contradiction applies. The non-central splitting is the image of $\operatorname{diag}(\lambda,1)$, a block-diagonal matrix in the regular image.

**The level sets and the polar decomposition.** The level set $N=c$ is the intersection of the image with $\det=c^2$, a smooth complex hypersurface of dimension three. The $*$-unitary subgroup is the image of $U(2)$, and the polar decomposition is
$$
GL_4(\mathbb{C})_L=Herm^{>0}_L\cdot U(2)_L,
$$
with the positive Hermitian factor and the unitary factor both block diagonal. The regular statement is the entry statement read twice, because $\mathsf M_4^L$ is injective.

**The covers.** The three double covers have kernel $\{\pm\mathrm I_4\}$ in the regular model, since $\mathsf M_4^L(-\mathrm I_2)=-\mathrm I_4$. The Hopf fibration remains $SU(2)\to S^2$ with fibre $S^1$ and is not a covering.

## The Entry Model

**The groups.** The entry model gives $\mathbb{B}^{\times}\cong GL_2(\mathbb{C})$ and $\mathbb{B}^{\times}_1\cong SL_2(\mathbb{C})$, with $\det\mathsf M_2(\tilde Q)=N$. The determinant sequence, the non-central splitting $s(\lambda)=\operatorname{diag}(\lambda,1)$, and the twofold cover $\mathbb{C}^{\times}\times SL_2\to GL_2$ are the entry-model statements of the common section.

**The level sets and the Bruhat decomposition.** Each nonzero level set is a smooth connected complex hypersurface of dimension three, homogeneous under $SL_2\times SL_2$. The Borel subgroup of upper triangular invertible matrices has complex dimension three and gives the two-cell decomposition
$$
GL_2(\mathbb{C})=B\sqcup BwB,
\qquad
w=\begin{pmatrix}0&1\\1&0\end{pmatrix},
$$
with the big cell the nonvanishing locus of the lower-left entry. The two cells are the two orbits of $B$ on the projective line.

**The unitary and projective groups.** The $*$-unitary subgroup is $U(2)$, of real dimension four, with maximal compact $SU(2)$ of real dimension three. The polar decomposition is $GL_2=Herm^{>0}\cdot U(2)$, unique, and on the norm-one group $SL_2=Herm^{>0}_1\cdot SU(2)$. The centre is $\mathbb{C}^{\times}\mathrm I_2$ and the projective group is $PGL_2$, of complex dimension three.

**The covers.** $SU(2)\to SO(3)$, $SL_2(\mathbb{C})\to SO^+(1,3)$ and $SL_2(\mathbb{C})\to PGL_2$ are double covers with kernel $\{\pm\mathrm I_2\}$. The Hopf map $SU(2)\to S^2$ has fibre $S^1$ and is not a covering. The image of $GL_2(\mathbb{C})$ is connected and has the homotopy type of $U(2)$, with fundamental group $\mathbb{Z}$; the norm-one subgroup is simply connected and has the homotopy type of $S^3$.

## The Peirce Frame

**The block group.** In the Peirce frame the image is the set of block-diagonal matrices $\mathrm I_2\otimes B=\operatorname{diag}(B,B)$ with $B\in GL_2(\mathbb{C})$. The group law is blockwise, the inverse is $\operatorname{diag}(B^{-1},B^{-1})$, and the determinant is $\det(B)^2=N^2$. The group is isomorphic to $GL_2(\mathbb{C})$ through the first block.

**The centre and the scalar action.** The centre is $\mathbb{C}^{\times}\mathrm I_4=\operatorname{diag}(\lambda\mathrm I_2,\lambda\mathrm I_2)$. A scalar $\lambda\mathrm I_4$ changes the determinant by $\lambda^4$, which is the fourth-power ambiguity of the projective determinant. There is no central splitting, for the same reason as in the entry model.

**The block Bruhat and the polar decomposition.** The Borel subgroup is the set of block upper triangular matrices with two identical $2\times2$ blocks, and the Bruhat decomposition is the block form of $GL_2=B\sqcup BwB$, with the Weyl element doubled. The polar decomposition is
$$
\operatorname{diag}(B,B)=\operatorname{diag}(P,P)\operatorname{diag}(V,V),
$$
with $P$ positive Hermitian and $V$ unitary. The $*$-unitary subgroup is the diagonal copy $\operatorname{diag}(U,U)$ of $U(2)$ inside $U(4)$, of real dimension four, and the special one is $\operatorname{diag}(U,U)$ with $U\in SU(2)$.

**The covers and the spectrum.** The double covers have kernel $\{\pm\mathrm I_4\}$, and the conjugation actions are read on the doubled Pauli matrices. The regular image has the homotopy type of $U(2)$, and the norm-one subgroup has the homotopy type of $S^3$. The block display adds no topology: it doubles every matrix and every eigenvalue, and the determinant squares.

## Summary

The units of $\mathbb{B}$ are $GL_2(\mathbb{C})$, and the norm-one elements are $SL_2(\mathbb{C})$; in the regular model they are a four-dimensional subgroup of $GL_4(\mathbb{C})$ and a three-dimensional subgroup of $SL_4(\mathbb{C})$, both isomorphic to the $2\times2$ groups. The determinant is the norm in the $2\times2$ display and its square in the $4\times4$ display, and it fits the exact sequence $1\to SL_2\to GL_2\to\mathbb{C}^{\times}\to1$, which splits non-centrally but not centrally; the multiplication map $\mathbb{C}^{\times}\times SL_2\to GL_2$ is a twofold cover. Each nonzero level set of the norm is a smooth connected complex hypersurface of dimension three, homogeneous under $SL_2\times SL_2$. The $*$-unitary group $U(2)$ is the maximal compact subgroup, and the polar decomposition is the matrix form of the unit-factor splitting. The centre is $\mathbb{C}^{\times}\mathrm I$, and the automorphism group is $PGL_2$. Three double covers have kernel $\{\pm\mathrm I\}$: $SU(2)\to SO(3)$, $SL_2(\mathbb{C})\to SO^+(1,3)$ and $SL_2(\mathbb{C})\to PGL_2(\mathbb{C})$; the Hopf fibration $SU(2)\to S^2$ has fibre $S^1$ and is not a covering.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}^{\times}\cong GL_2(\mathbb{C})$ | the unit group |
| $\mathbb{B}^{\times}_1\cong SL_2(\mathbb{C})$ | the norm-one group |
| $\mathsf M_2$, $\mathsf M_4^L$ | the two displays, $\det\mathsf M_2=N$ and $\det\mathsf M_4^L=N^2$ |
| $\mathbb{C}^{\times}\mathrm I_2$, $\mathbb{C}^{\times}\mathrm I_4$ | the centre of each display |
| $U(2)$, $\operatorname{diag}(U,U)$ | the $*$-unitary subgroup, maximal compact |
| $SU(2)$, $\operatorname{diag}(U,U)$ | the rotation rotors |
| $PGL_2$ | the inner automorphism group |
| $SO^+(1,3)$ | the proper orthochronous Lorentz group |
| $PSL_2(\mathbb{C})\cong PGL_2(\mathbb{C})$ | the Möbius group |
| $Herm^{>0}$ | the positive Hermitian matrices |

## Further Reading

- [Matrix Representations : The Models and the Change of Frame](matrix-representations-the-models-and-the-change-of-frame.html), for the models
- [Matrix Representations : Trace, Determinant and the Biquaternion Norm](matrix-representations-trace-determinant-and-the-biquaternion-norm.html), for the determinant and the norm
- *Matrix Representations : The Polar Decomposition of a Matrix*, for the factorization
- *Matrix Representations : The Projective Line and the Möbius Action*, for the Möbius cover
- [The Biquaternion Unit Group as a Topological Group](the-biquaternion-unit-group-as-a-topological-group.html), for the topology
- [The N-Regular Sector](the-n-regular-sector.html), for the level sets
- [The Unitary Group of the Biquaternion Algebra](the-unitary-group-of-the-biquaternion-algebra.html), for $U(2)$
- [Biquaternion Rotations and Lorentz Transformations](biquaternion-rotations-and-lorentz-transformations.html), for the double covers