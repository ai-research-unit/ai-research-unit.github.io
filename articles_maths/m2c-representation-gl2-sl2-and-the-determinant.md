# __$M_2(\mathbb{C})$ Representation : $GL_2(\mathbb{C})$, $SL_2(\mathbb{C})$ and the Determinant__

## Introduction

The units of the biquaternion algebra are the invertible matrices, and the determinant is the quaternionic norm. The two statements together identify the group of units with $GL_2(\mathbb{C})$ and cut out the norm-one subgroup as $SL_2(\mathbb{C})$. The identification is an isomorphism of complex Lie groups, and the determinant is its only numerical invariant.

This article develops the group picture: the isomorphism, the determinant sequence and its splittings, the geometry of the level sets, and the relation to the $*$-unitary group through the polar decomposition. It is the matrix form of *The Biquaternion Unit Group as a Topological Group* and of *The N-Regular Sector*.

**Conventions.** The algebra and the model are those of *$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant*. The norm is $\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2=\det\mathsf{M}_2(\tilde Q)$. The unit group of the algebra is $\mathbb{B}^{\times}=\{\tilde Q:N\neq0\}$, and the norm-one group is $\mathbb{B}^{\times}_1=\{\tilde Q:N=1\}$.

**Boundaries.** The unit group as a topological group, its homotopy and its covering are *The Biquaternion Unit Group as a Topological Group*; the norm-one group and the polar factors are *The Polar Decomposition of a N-Regular Biquaternion*; the $*$-unitary group is *The Unitary Group of the Biquaternion Algebra*; the level sets of the norm and the sector are *The N-Regular Sector*; the polar decomposition of a matrix is *$M_2(\mathbb{C})$ Representation : The Polar Decomposition of a Matrix*.

## The Group Isomorphism

**Theorem.** The map $\mathsf{M}_2$ restricts to an isomorphism of complex Lie groups

$$
\mathbb{B}^{\times}\longrightarrow GL_2(\mathbb{C}),\qquad
\tilde Q\longmapsto\mathsf{M}_2(\tilde Q),
$$

and it carries the norm-one subgroup onto $SL_2(\mathbb{C})$:

$$
\{\tilde Q:\langle\tilde Q\rangle_{\natural}=1\}\cong SL_2(\mathbb{C}).
$$

*Proof.* The map is an algebra isomorphism, so it carries units to invertible matrices and inverses to inverses. It is holomorphic because it is complex linear in the four coefficients. The determinant of the image is the norm, so the image of the norm-one set is the set of matrices of determinant one, which is $SL_2(\mathbb{C})$ by definition.

**The inverse is polynomial.** The inverse matrix is the adjugate divided by the determinant, and both are polynomial in the entries; on the open set where the determinant is nonzero the inverse is holomorphic. The group isomorphism is therefore biholomorphic.

**The two readings of the same group.** The algebra says: the units are the elements of nonzero quaternionic norm, and the group law is the biquaternion product. The matrix says: the units are the invertible matrices, and the group law is the matrix product. The two descriptions are the same group in two notations. The biquaternion description carries the real structure, the two sectors and the conjugations; the matrix description carries the determinant, the eigenvalues and the Bruhat decomposition.

## The Determinant Sequence

**The exact sequence.**

$$
1\longrightarrow SL_2(\mathbb{C})\longrightarrow GL_2(\mathbb{C})\xrightarrow{\ \det\ }\mathbb{C}^{\times}\longrightarrow1.
$$

The kernel of the determinant is $SL_2(\mathbb{C})$ by definition; the determinant is surjective because $\operatorname{diag}(\lambda,1)$ has determinant $\lambda$; and $SL_2$ is normal because the determinant is a homomorphism.

**The non-central splitting.** The sequence splits, but not centrally. The map

$$
s:\mathbb{C}^{\times}\to GL_2(\mathbb{C}),\qquad
s(\lambda)=\operatorname{diag}(\lambda,1),
$$

is a homomorphism with $\det s(\lambda)=\lambda$, so $GL_2\cong SL_2\rtimes\mathbb{C}^{\times}$ as a semidirect product, the action of $\lambda$ on $SL_2$ being conjugation by $\operatorname{diag}(\lambda,1)$.

**No central splitting.** A central splitting would send $\lambda$ to a scalar matrix $\mu(\lambda)\mathrm I_2$ with $\det(\mu(\lambda)\mathrm I_2)=\mu(\lambda)^2=\lambda$. A homomorphism $\mu$ would give $\mu(1)=1$ and $\mu(-1)^2=-1$, while $\mu((-1)(-1))=\mu(1)=1$; hence $\mu(-1)^2=1$, a contradiction. There is therefore no subgroup of $GL_2$ isomorphic to $\mathbb{C}^{\times}$, central in $GL_2$, and mapping isomorphically to the determinant. The obstruction is the square in the determinant of a scalar matrix, and it is the group-level form of the fact that the norm of a central element is a square.

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

The quotient is by the diagonal copy of $\{\pm1\}$, and it is the source of the twofold cover of the Lorentz group by $SL_2$.

**The dimensions.** $\dim_{\mathbb{C}}GL_2=4$, $\dim_{\mathbb{C}}SL_2=3$, $\dim_{\mathbb{C}}\mathbb{C}^{\times}=1$, and the sequence is $3+1=4$. Over the reals the dimensions are $8$, $6$ and $2$.

## The Level Sets of the Norm

**The level sets are smooth.** For $c\neq0$,

$$
\{N=c\}=\{\tilde Q:\langle\tilde Q\rangle_{\natural}=c\}
$$

is a smooth complex hypersurface of complex dimension three, because the gradient of $N$ vanishes only at $\tilde Q=0$, and $0$ is not on the level set. It is connected, being a nondegenerate affine quadric of dimension at least two.

**The norm-one slice.** The level set $N=1$ is $SL_2(\mathbb{C})$. It is not compact: the Hermitian matrix $\operatorname{diag}(r,r^{-1})$ has determinant one and eigenvalues $r,r^{-1}$, and it escapes every compact set as $r\to\infty$. Its maximal compact subgroup is $SU(2)$, the fixed points of the Cartan involution $M\mapsto(M^{\dagger})^{-1}$.

**The homogeneous structure.** The group $SL_2(\mathbb{C})\times SL_2(\mathbb{C})$ acts on $GL_2$ by $(A,B)\cdot M=AMB^{-1}$, and the determinant is invariant. The action is transitive on each level set $N=c$ with $c\neq0$, and the stabiliser of the identity is the diagonal $SL_2$. Hence each nonzero level set is a homogeneous space of complex dimension three,

$$
\{N=c\}\cong (SL_2\times SL_2)/SL_2,
$$

with the diagonal embedding. The statement is the matrix form of the transitivity of the conformal group on the elements of fixed norm.

**The cone.** The level set $c=0$ is the null cone, and it is not smooth: it is the cone over the Segre quadric $\mathbb{P}^1\times\mathbb{P}^1$, with the apex at the origin. The apex is the only singular point, and it is the image of the zero element. The cone is the subject of *$M_2(\mathbb{C})$ Representation : Rank-One Matrices and the Determinantal Variety*.

## The Unit Group and the $*$-Unitary Group

**The $*$-unitary subgroup.** The fixed points of the Hermitian adjoint are the Hermitian matrices; the matrices satisfying $M^{\dagger}M=\mathrm I_2$ are the $*$-unitary group $U(2)$. In the algebra, the condition is $\tilde Q^{*}\tilde Q=e_t$, and the subgroup is

$$
\mathrm{U}(\mathbb{B})=\{\tilde Q:\tilde Q^{*}\tilde Q=e_t\}\cong U(2),
$$

of real dimension four. It is the maximal compact subgroup of $\mathbb{B}^{\times}\cong GL_2(\mathbb{C})$.

**The special $*$-unitary subgroup.** The intersection $U(2)\cap SL_2=SU(2)$, of real dimension three, is the group of rotation rotors. It is the maximal compact subgroup of $SL_2$.

**The polar decomposition.** Every invertible matrix is a product of a positive Hermitian matrix and a $*$-unitary one:

$$
GL_2(\mathbb{C})=Herm^{>0}\cdot U(2),
$$

and the product is unique. Passing to determinants, $\det P=r^2$ and $\det V=\zeta^2$ with $|\zeta|=1$. On $SL_2$ the decomposition restricts to

$$
SL_2(\mathbb{C})=Herm^{>0}_1\cdot SU(2),
$$

with $Herm^{>0}_1$ the positive Hermitian matrices of determinant one. The two factors have real dimensions three and three, and the product is a diffeomorphism. The statement is developed in *$M_2(\mathbb{C})$ Representation : The Polar Decomposition of a Matrix*.

**The topology.** $GL_2(\mathbb{C})$ is connected and has the homotopy type of $U(2)$; its fundamental group is $\mathbb{Z}$, generated by the determinant circle. $SL_2(\mathbb{C})$ is simply connected and has the homotopy type of $SU(2)=S^3$. The determinant sequence is the fibration that exhibits the first statement from the second. The details are *The Biquaternion Unit Group as a Topological Group*, §*The Homotopy Groups*.

## The Bruhat Decomposition

**The Borel subgroup.** The upper triangular invertible matrices

$$
B=\left\{\begin{pmatrix}a&b\\0&d\end{pmatrix}:ad\neq0\right\}
$$

form a closed subgroup of complex dimension three. It is the stabiliser of the first coordinate line, and it is solvable: its commutator subgroup is the unipotent radical of matrices $\begin{pmatrix}1&b\\0&1\end{pmatrix}$, and the quotient is the diagonal torus.

**The two cells.** For $c=0$ the matrix lies in $B$. For $c\neq0$ the elementary identity

$$
\begin{pmatrix}a&b\\c&d\end{pmatrix}
=
\begin{pmatrix}1&a\\0&c\end{pmatrix}
\begin{pmatrix}0&1\\1&0\end{pmatrix}
\begin{pmatrix}1&d/c\\0&b-ad/c\end{pmatrix}
$$

writes the matrix as a product of two upper triangular matrices around the Weyl element $w=\begin{pmatrix}0&1\\1&0\end{pmatrix}$. The decomposition is disjoint, because the lower-left entry of an element of $BwB$ is $\delta p\neq0$, and it is therefore

$$
GL_2(\mathbb{C})=B\sqcup BwB .
$$

The first cell has complex dimension three and the big cell complex dimension four; the big cell is the nonvanishing locus of the entry $c$, hence open and dense. This is the group form of the decomposition of the projective line into the affine line and the point at infinity: $B$ is the stabiliser of the point at infinity, and the big cell is the set of matrices that move it.

## The Centre and the Projective Group

**The centre.** The centre of $GL_2$ is the scalar matrices $\mathbb{C}^{\times}\mathrm I_2$, of complex dimension one. In the algebra it is $\mathbb{C}^{\times}e_t$, the invertible central elements.

**The projective group.** The inner automorphism group is

$$
PGL_2(\mathbb{C})=GL_2(\mathbb{C})/\mathbb{C}^{\times}\mathrm I_2,
$$

of complex dimension three. It is the group of algebra automorphisms of $M_2(\mathbb{C})$, and by transport the group of algebra automorphisms of $\mathbb{B}$. The determinant is not defined on $PGL_2$, because a scalar multiple changes it by a square; the projective group sees the conformal class of the determinant, not its value.

**The determinant on the projective group.** A class $[M]$ has a well-defined determinant only up to squares: $\det(\lambda M)=\lambda^2\det M$. The ambiguity is the same square that obstructs the central splitting. On $PGL_2$ the determinant is therefore not a function; only its vanishing locus and its square class are defined.

## The Double Cover

**The common kernel.** Three actions of $SL_2(\mathbb{C})$ have the same kernel $\{\pm\mathrm I_2\}$: conjugation on $M_2(\mathbb{C})$, conjugation on the Hermitian matrices, and the Möbius action on $\mathbb{P}^1$. In each case the kernel is the centre of $SL_2$, and the quotient is the image.

**The rotation cover.** The conjugation action of $SU(2)$ on the Hermitian traceless matrices

$$
\vec x\cdot\vec\sigma\longmapsto U(\vec x\cdot\vec\sigma)U^{\dagger}
$$

preserves the determinant $-|\vec x|^2$ and the identity component, so it defines a homomorphism

$$
SU(2)\longrightarrow SO(3),\qquad U\longmapsto R(U),
$$

with kernel $\{\pm\mathrm I_2\}$. It is surjective: every rotation is the conjugation by a rotor, and the two rotors $\pm U$ give the same rotation. Hence $SU(2)$ is the double cover of $SO(3)$, and

$$
SO(3)\cong SU(2)/\{\pm\mathrm I_2\}\cong\mathbb{RP}^3.
$$

**The Lorentz cover.** The conjugation action of $SL_2(\mathbb{C})$ on the Hermitian matrices

$$
H\longmapsto MHM^{\dagger}
$$

preserves the determinant $\det H$, hence the quadratic form $x_0^2-|\vec x|^2$ of signature $(1,3)$, and it preserves the positive cone. It therefore lands in $SO^+(1,3)$, and the kernel is again $\{\pm\mathrm I_2\}$. The map is surjective, so

$$
SL_2(\mathbb{C})\longrightarrow SO^+(1,3)
$$

is a double cover. Since $SL_2(\mathbb{C})$ is simply connected, it is the universal cover of the proper orthochronous Lorentz group, and $\pi_1(SO^+(1,3))=\mathbb{Z}/2$.

**The Möbius cover.** The action on $\mathbb{P}^1$,

$$
\begin{pmatrix}a&b\\c&d\end{pmatrix}\cdot[\xi]=[a\xi+b:c\xi+d],
$$

has kernel $\{\pm\mathrm I_2\}$, so it factors through

$$
PSL_2(\mathbb{C})=SL_2(\mathbb{C})/\{\pm\mathrm I_2\}\cong PGL_2(\mathbb{C}).
$$

The map $SL_2\to PGL_2$ is a double cover, and $PGL_2$ has fundamental group $\mathbb{Z}/2$.

**The determinant cover.** The multiplication map

$$
\mathbb{C}^{\times}\times SL_2(\mathbb{C})\longrightarrow GL_2(\mathbb{C}),\qquad
(\lambda,U)\longmapsto\lambda U,
$$

has kernel $\{(\pm1,\pm\mathrm I_2)\}=\{\pm(1,\mathrm I_2)\}$, of order two, as in §*The Determinant Sequence*. It is the group-level form of the square in the determinant: a scalar matrix $\lambda\mathrm I_2$ has determinant $\lambda^2$, so the determinant cannot distinguish $\lambda$ from $-\lambda$, and the two pairs $(\lambda,U)$ and $(-\lambda,-U)$ have the same product.

**The algebra reading.** In the biquaternion model the kernel of the action on $PGL_2$ is $\{\pm e_t\}$: the two central units of norm one act by the same conjugation. The map to $GL_2$ itself has kernel $\{e_t\}$; the sign is lost only after quotienting by the centre. The norm-one group $\mathbb{B}^{\times}_1\cong SL_2(\mathbb{C})$ is the spin group of the Lorentz form, and the two elements $\pm\tilde Q$ carry the same rotation and the same Möbius transformation but opposite spinors. The sign is not visible in $SO^+(1,3)$ or in $PGL_2$; it is visible in $SL_2$ and in the spinor module.

**The two fibrations.** The Hopf fibration and the covering are different:

$$
S^3\cong SU(2)\longrightarrow S^2,\qquad \text{fibre }S^1,
$$

is the Hopf map, while

$$
S^3\cong SU(2)\longrightarrow \mathbb{RP}^3\cong SO(3)
$$

is the double cover, with fibre $S^0=\{\pm1\}$. The first has a circle as fibre and is not a covering; the second has two points and is. Both come from the same action of $SU(2)$: the Hopf map sends $U$ to the line $U(1,0)^{\mathsf T}$, equivalently to $U\sigma_3U^{\dagger}$, and the covering sends $U$ to the conjugation action on the whole sphere.

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

The units of $\mathbb{B}$ are $GL_2(\mathbb{C})$, and the norm-one elements are $SL_2(\mathbb{C})$. The determinant is the norm and fits the exact sequence $1\to SL_2\to GL_2\to\mathbb{C}^{\times}\to1$, which splits non-centrally but not centrally; the multiplication map $\mathbb{C}^{\times}\times SL_2\to GL_2$ is a twofold cover. Each nonzero level set of the norm is a smooth connected complex hypersurface of dimension three, homogeneous under $SL_2\times SL_2$. The $*$-unitary group $U(2)$ is the maximal compact subgroup, and the polar decomposition is the matrix form of the unit-factor splitting. The centre is $\mathbb{C}^{\times}\mathrm I_2$, and the automorphism group is $PGL_2$. Three double covers have kernel $\{\pm\mathrm I_2\}$: $SU(2)\to SO(3)$, $SL_2(\mathbb{C})\to SO^+(1,3)$ and $SL_2(\mathbb{C})\to PGL_2(\mathbb{C})$; the Hopf fibration $SU(2)\to S^2$ has fibre $S^1$ and is not a covering.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}^{\times}\cong GL_2(\mathbb{C})$ | the unit group |
| $\mathbb{B}^{\times}_1\cong SL_2(\mathbb{C})$ | the norm-one group |
| $\det$ | the determinant, equal to $\langle\cdot\rangle_{\natural}$ |
| $\mathbb{C}^{\times}\mathrm I_2$ | the centre |
| $U(2)$ | the $*$-unitary subgroup, maximal compact |
| $SU(2)$ | the rotation rotors |
| $PGL_2$ | the inner automorphism group |
| $SO^+(1,3)$ | the proper orthochronous Lorentz group |
| $PSL_2(\mathbb{C})\cong PGL_2(\mathbb{C})$ | the Möbius group |
| $\{\pm\mathrm I_2\}$ | the common kernel of the double covers |
| $Herm^{>0}$ | the positive Hermitian matrices |

## Further Reading

- [The Biquaternion Unit Group as a Topological Group](the-biquaternion-unit-group-as-a-topological-group.html), for the topology and the covering
- [The N-Regular Sector](the-n-regular-sector.html), for the sector and its level sets
- [The Polar Decomposition of a N-Regular Biquaternion](the-polar-decomposition-of-an-n-regular-biquaternion.html), for the unit factor
- [The Unitary Group of the Biquaternion Algebra](the-unitary-group-of-the-biquaternion-algebra.html), for $U(2)$
- [$M_2(\mathbb{C})$ Representation : Trace, Determinant and the Biquaternion Norm](m2c-representation-trace-determinant-and-the-biquaternion-norm.html), for the determinant
- [$M_2(\mathbb{C})$ Representation : The Polar Decomposition of a Matrix](m2c-representation-the-polar-decomposition-of-a-matrix.html), for the factorization
- [Biquaternion Rotations and Lorentz Transformations](biquaternion-rotations-and-lorentz-transformations.html), for the double covers of $SO(3)$ and $SO^+(1,3)$
- [$M_2(\mathbb{C})$ Representation : The Projective Line and the Möbius Action](m2c-representation-the-projective-line-and-the-mobius-action.html), for the Möbius cover
- [Lie Groups](lie-groups.html), for $GL_2$ and $SL_2$
