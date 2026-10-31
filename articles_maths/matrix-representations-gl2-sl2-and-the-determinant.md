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

## The Group in the Two Displays

**The theorem.** The map $\mathsf M_2$ is an isomorphism of complex Lie groups
$$
\mathbb{B}^{\times}\longrightarrow GL_2(\mathbb{C}),\qquad
\tilde Q\longmapsto\mathsf M_2(\tilde Q),
$$
and it carries the norm-one subgroup onto $SL_2(\mathbb{C})$. The map $\mathsf M_4^L$ is an injective homomorphism whose image is a closed complex subgroup of $GL_4(\mathbb{C})$ isomorphic to $GL_2(\mathbb{C})$, and
$$
\{\tilde Q:N=1\}\cong SL_2(\mathbb{C})\subset SL_4(\mathbb{C}).
$$

*Proof.* Both maps are injective algebra homomorphisms, so they carry units to invertible matrices and inverses to inverses. They are holomorphic because they are complex linear in the four coefficients. The determinant of the $2\times2$ image is $N$, and the determinant of the $4\times4$ image is $N^2$; the norm-one set therefore has determinant one in both displays.

**The inverse is polynomial.** The inverse matrix is the adjugate divided by the determinant, and both are polynomial in the entries; on the open set where the determinant is nonzero the inverse is holomorphic. Both isomorphisms are therefore biholomorphic onto their images.

**The two readings.** The algebra says: the units are the elements of nonzero norm, and the group law is the biquaternion product. The $2\times2$ matrix says: the units are all invertible matrices, and the group law is the matrix product. The $4\times4$ matrix says: the units are the invertible matrices in the image, and the group law is the block product. The three descriptions are the same group in three notations. The algebra carries the real structure and the two sectors; the $2\times2$ display carries the determinant, the eigenvalues and the Bruhat decomposition; the $4\times4$ display carries the doubling of every multiplicity and the square of the determinant.

**The image is not all of $GL_4$.** The image has complex dimension four, while $GL_4(\mathbb{C})$ has dimension sixteen. The group isomorphism is therefore onto a subgroup, and the twelve missing dimensions are the two identical blocks. Every group statement below is a statement about the image, not about the ambient $GL_4(\mathbb{C})$.

## The Determinant Sequence

**The exact sequence.**
$$
1\longrightarrow SL_2(\mathbb{C})\longrightarrow GL_2(\mathbb{C})\xrightarrow{\ \det\ }\mathbb{C}^{\times}\longrightarrow1.
$$
The kernel of the determinant is $SL_2$ by definition; the determinant is surjective because $\operatorname{diag}(\lambda,1)$ has determinant $\lambda$; and $SL_2$ is normal because the determinant is a homomorphism. In the regular model the same sequence is read on the image, with $\det\mathsf M_4^L(\tilde Q)=N^2$.

**The non-central splitting.** The sequence splits, but not centrally. The map
$$
s:\mathbb{C}^{\times}\to GL_2(\mathbb{C}),\qquad
s(\lambda)=\operatorname{diag}(\lambda,1),
$$
is a homomorphism with $\det s(\lambda)=\lambda$, so $GL_2\cong SL_2\rtimes\mathbb{C}^{\times}$ as a semidirect product, the action of $\lambda$ on $SL_2$ being conjugation by $\operatorname{diag}(\lambda,1)$. In the regular model the same splitting is the image under $\mathsf M_4^L$, with $\mathsf M_4^L(\operatorname{diag}(\lambda,1))$ block diagonal.

**No central splitting.** A central splitting would send $\lambda$ to a scalar matrix $\mu(\lambda)\mathrm I_2$ with $\det(\mu(\lambda)\mathrm I_2)=\mu(\lambda)^2=\lambda$. A homomorphism $\mu$ would give $\mu(1)=1$ and $\mu(-1)^2=-1$, while $\mu((-1)(-1))=\mu(1)=1$; hence $\mu(-1)^2=1$, a contradiction. In the regular model the scalar matrix is $\mu(\lambda)\mathrm I_4$, its determinant is $\mu(\lambda)^4$, and the same argument with the fourth power gives the same contradiction. There is therefore no subgroup of the image isomorphic to $\mathbb{C}^{\times}$, central in the image, and mapping isomorphically to the determinant.

**The covering.** The multiplication map
$$
\mathbb{C}^{\times}\times SL_2(\mathbb{C})\longrightarrow GL_2(\mathbb{C}),\qquad
(\lambda,U)\longmapsto\lambda U,
$$
is surjective, because every $M$ can be written $\lambda U$ with $\lambda^2=\det M$ and $U=M/\lambda\in SL_2$. Its kernel is
$$
\{(\lambda,U):\lambda U=\mathrm I_2\}=\{(\lambda,\lambda^{-1}\mathrm I_2):\lambda^2=1\}=\{\pm1\},
$$
of order two. Hence
$$
GL_2(\mathbb{C})\cong\big(\mathbb{C}^{\times}\times SL_2(\mathbb{C})\big)/\{\pm1\}.
$$
The quotient is by the diagonal copy of $\{\pm1\}$. In the regular model the same map is $(\lambda,U)\mapsto\lambda\,\mathrm I_2\otimes U$, with the same kernel, and the determinant is $\lambda^4$.

**The dimensions.** $\dim_{\mathbb{C}}GL_2=4$, $\dim_{\mathbb{C}}SL_2=3$, $\dim_{\mathbb{C}}\mathbb{C}^{\times}=1$, and the sequence is $3+1=4$. Over the reals the dimensions are $8$, $6$ and $2$. The regular image has the same complex dimension four inside the sixteen of $GL_4(\mathbb{C})$.

## The Level Sets of the Norm

**The level sets are smooth.** For $c\neq0$,
$$
\{N=c\}=\{\tilde Q:\langle\tilde Q\rangle_{\natural}=c\}
$$
is a smooth complex hypersurface of complex dimension three, because the gradient of $N$ vanishes only at $\tilde Q=0$, and $0$ is not on the level set. It is connected, being a nondegenerate affine quadric of dimension at least two. In the regular model it is the intersection of the image with the level set $\det=c^2$ of the determinant, a smooth complex hypersurface of the same dimension.

**The norm-one slice.** The level set $N=1$ is $SL_2(\mathbb{C})$, embedded in $SL_4(\mathbb{C})$ by the regular representation. It is not compact: in the $2\times2$ model the Hermitian matrix $\operatorname{diag}(r,r^{-1})$ has determinant one, and in the regular model its image is the block matrix $\operatorname{diag}(r,r^{-1},r,r^{-1})$, which escapes every compact set as $r\to\infty$. Its maximal compact subgroup is the image of $SU(2)$, the fixed points of the Cartan involution $M\mapsto(M^{\dagger})^{-1}$.

**The homogeneous structure.** The group $SL_2(\mathbb{C})\times SL_2(\mathbb{C})$ acts on $GL_2$ by $(A,B)\cdot M=AMB^{-1}$, and the determinant is invariant. The action is transitive on each level set $N=c$ with $c\neq0$, and the stabiliser of the identity is the diagonal $SL_2$. Hence each nonzero level set is a homogeneous space of complex dimension three,
$$
\{N=c\}\cong (SL_2\times SL_2)/SL_2,
$$
with the diagonal embedding. In the regular model the same action is read blockwise, and the level set is the image of the $2\times2$ one.

**The cone.** The level set $c=0$ is the null cone, and it is not smooth: it is the cone over the Segre quadric $\mathbb{P}^1\times\mathbb{P}^1$, with the apex at the origin. The apex is the only singular point, and it is the image of the zero element. In the regular model the cone is the intersection of the image with the determinant-zero locus, and it is the subject of *Matrix Representations : Rank-One Matrices and the Determinantal Variety*.

## The Unit Group and the $*$-Unitary Group

**The $*$-unitary subgroup.** The matrices in the $2\times2$ image satisfying $M^{\dagger}M=\mathrm I_2$ form $U(2)$, of real dimension four. In the algebra the condition is $\tilde Q^{*}\tilde Q=e_t$, and the subgroup is
$$
\mathrm{U}(\mathbb{B})=\{\tilde Q:\tilde Q^{*}\tilde Q=e_t\}\cong U(2).
$$
In the regular model the same subgroup is the diagonal copy $\operatorname{diag}(U,U)$ inside $U(4)$, of the same real dimension. It is the maximal compact subgroup of the image.

**The special $*$-unitary subgroup.** The intersection with the norm-one group is $SU(2)$, of real dimension three, the group of rotation rotors. In the regular model it is the diagonal copy $\operatorname{diag}(U,U)$ of $SU(2)$ inside $SU(4)$, and it is the maximal compact subgroup of $SL_2$.

**The polar decomposition.** Every invertible matrix in the image is a product of a positive Hermitian matrix and a $*$-unitary one:
$$
GL_2(\mathbb{C})=Herm^{>0}\cdot U(2),
\qquad
GL_4(\mathbb{C})_L=Herm^{>0}_L\cdot U(2)_L,
$$
and the product is unique. The regular statement is the $2\times2$ statement read twice, because $\mathsf M_4^L$ is injective and carries the two factors to $\operatorname{diag}(P,P)$ and $\operatorname{diag}(V,V)$. On the norm-one group the decomposition restricts to
$$
SL_2(\mathbb{C})=Herm^{>0}_1\cdot SU(2),
$$
with $Herm^{>0}_1$ the positive Hermitian matrices of determinant one. The two factors have real dimensions three and three, and the product is a diffeomorphism. The statement is developed in *Matrix Representations : The Polar Decomposition of a Matrix*.

**The topology.** The image of $GL_2(\mathbb{C})$ is connected and has the homotopy type of $U(2)$; its fundamental group is $\mathbb{Z}$, generated by the determinant circle. The norm-one subgroup is simply connected and has the homotopy type of $SU(2)=S^3$. The determinant sequence is the fibration that exhibits the first statement from the second. The details are *The Biquaternion Unit Group as a Topological Group*, §*The Homotopy Groups*.

## The Bruhat Decomposition

**The Borel subgroup.** The image of the upper triangular invertible matrices
$$
B=\left\{\begin{pmatrix}a&b\\0&d\end{pmatrix}:ad\neq0\right\}
$$
is a closed subgroup of $GL_2$ of complex dimension three. It is the stabiliser of the first coordinate line, and it is solvable: its commutator subgroup is the unipotent radical, and the quotient is the diagonal torus. In the regular model it is the set of block upper triangular matrices with two identical $2\times2$ blocks.

**The two cells.** For $c=0$ the matrix lies in $B$. For $c\neq0$ the elementary identity
$$
\begin{pmatrix}a&b\\c&d\end{pmatrix}
=
\begin{pmatrix}1&a\\0&c\end{pmatrix}
\begin{pmatrix}0&1\\1&0\end{pmatrix}
\begin{pmatrix}1&d/c\\0&b-ad/c\end{pmatrix}
$$
writes the matrix as a product of two upper triangular matrices around the Weyl element $w=\begin{pmatrix}0&1\\1&0\end{pmatrix}$. The decomposition is disjoint, because the lower-left entry of an element of $BwB$ is $c\neq0$, and it is therefore
$$
GL_2(\mathbb{C})=B\sqcup BwB.
$$
The first cell has complex dimension three and the big cell complex dimension four; the big cell is the nonvanishing locus of the entry $c$, hence open and dense. In the regular model the same decomposition is read on the two blocks, with the Weyl element doubled.

**The projective reading.** The two cells are the two orbits of the Borel subgroup on the projective line: $B$ is the stabiliser of the point at infinity, and the big cell is the set of matrices that move it. The projective line is *Matrix Representations : The Projective Line and the Möbius Action*.

## The Centre and the Projective Group

**The centre.** The centre of $GL_2$ is the scalar matrices $\mathbb{C}^{\times}\mathrm I_2$, of complex dimension one. In the regular model it is $\mathbb{C}^{\times}\mathrm I_4$. In the algebra it is $\mathbb{C}^{\times}e_t$, the invertible central elements.

**The projective group.** The inner automorphism group is
$$
PGL_2(\mathbb{C})=GL_2(\mathbb{C})/\mathbb{C}^{\times}\mathrm I_2,
$$
of complex dimension three. It is the group of algebra automorphisms of $M_2(\mathbb{C})$, and by transport the group of algebra automorphisms of $\mathbb{B}$. The determinant is not defined on $PGL_2$, because a scalar multiple changes it by a square; the projective group sees the conformal class of the determinant, not its value. In the regular model the same group is the image modulo the scalars $\mathbb{C}^{\times}\mathrm I_4$, and the determinant changes by a fourth power.

**The determinant on the projective group.** A class $[M]$ has a well-defined determinant only up to squares in the $2\times2$ model, and up to fourth powers in the regular model:
$$
\det(\lambda M)=\lambda^2\det M
\quad\text{and}\quad
\det(\lambda M)=\lambda^4\det M.
$$
The ambiguity is the same square that obstructs the central splitting, raised to the second power in the regular model. On $PGL_2$ the determinant is therefore not a function; only its vanishing locus and its class are defined.

## The Double Covers

**The common kernel.** Three actions of $SL_2(\mathbb{C})$ have the same kernel $\{\pm\mathrm I_2\}$: conjugation on $M_2(\mathbb{C})$, conjugation on the Hermitian matrices, and the Möbius action on $\mathbb{P}^1$. In the regular model the same three actions have kernel $\{\pm\mathrm I_4\}$, because $\mathsf M_4^L(-\mathrm I_2)=-\mathrm I_4$.

**The rotation cover.** The conjugation action of $SU(2)$ on the Hermitian traceless matrices
$$
\vec x\cdot\vec\sigma\longmapsto U(\vec x\cdot\vec\sigma)U^{\dagger}
$$
preserves the determinant $-|\vec x|^2$ and the identity component, so it defines a homomorphism
$$
SU(2)\longrightarrow SO(3),\qquad U\longmapsto R(U),
$$
with kernel $\{\pm\mathrm I_2\}$. In the regular model the same action is $\operatorname{diag}(U,U)$ on the doubled Pauli matrices, with kernel $\{\pm\mathrm I_4\}$. It is surjective, so $SU(2)$ is the double cover of $SO(3)$, and
$$
SO(3)\cong SU(2)/\{\pm\mathrm I_2\}\cong\mathbb{RP}^3.
$$

**The Lorentz cover.** The conjugation action of $SL_2(\mathbb{C})$ on the Hermitian matrices
$$
H\longmapsto MHM^{\dagger}
$$
preserves $\det H$, hence the quadratic form $x_0^2-|\vec x|^2$ of signature $(1,3)$, and it preserves the positive cone. It therefore lands in $SO^+(1,3)$, and the kernel is again $\{\pm\mathrm I_2\}$. In the regular model the action is $X\mapsto MXM^{\dagger}$ on the four-dimensional Hermitian subspace, with kernel $\{\pm\mathrm I_4\}$. The map is surjective, so $SL_2(\mathbb{C})\to SO^+(1,3)$ is a double cover. Since $SL_2(\mathbb{C})$ is simply connected, it is the universal cover, and $\pi_1(SO^+(1,3))=\mathbb{Z}/2$.

**The Möbius cover.** The action on $\mathbb{P}^1$,
$$
\begin{pmatrix}a&b\\c&d\end{pmatrix}\cdot[\xi]=[a\xi+b:c\xi+d],
$$
has kernel $\{\pm\mathrm I_2\}$, so it factors through
$$
PSL_2(\mathbb{C})=SL_2(\mathbb{C})/\{\pm\mathrm I_2\}\cong PGL_2(\mathbb{C}).
$$
The map $SL_2\to PGL_2$ is a double cover, and $PGL_2$ has fundamental group $\mathbb{Z}/2$.

**The two fibrations.** The Hopf fibration and the double cover are different:
$$
S^3\cong SU(2)\longrightarrow S^2,\qquad \text{fibre }S^1,
$$
is the Hopf map, while
$$
S^3\cong SU(2)\longrightarrow \mathbb{RP}^3\cong SO(3)
$$
is the double cover, with fibre $S^0=\{\pm1\}$. The first has a circle as fibre and is not a covering; the second has two points and is. In the regular model the same two maps are read on the doubled Pauli matrices.

**The table.**

| Cover | Base | Kernel | Fibre |
|---|---|---|---|
| $SU(2)\to SO(3)$ | rotations | $\{\pm\mathrm I_2\}$ | two points |
| $SL_2(\mathbb{C})\to SO^+(1,3)$ | Lorentz | $\{\pm\mathrm I_2\}$ | two points |
| $SL_2(\mathbb{C})\to PSL_2(\mathbb{C})$ | Möbius | $\{\pm\mathrm I_2\}$ | two points |
| $\mathbb{C}^{\times}\times SL_2\to GL_2$ | units | $\{\pm(1,\mathrm I_2)\}$ | two points |
| $SU(2)\to S^2$ (Hopf) | sphere | $U(1)$ | circle |

The last row is not a covering; it is the Hopf fibration, included for contrast.

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
- [Matrix Representations : $GL_2(\mathbb{C})$, $SL_2(\mathbb{C})$ and the Determinant](matrix-representations-gl2-sl2-and-the-determinant.html), for the $2\times2$ source
- [Matrix Representations : $GL_2(\mathbb{C})$, $SL_2(\mathbb{C})$ and the Determinant](matrix-representations-gl2-sl2-and-the-determinant.html), for the $4\times4$ source
