# __Biquaternion Objects and Their Matrix Correspondences__

## Introduction

The biquaternion algebra carries one distinguished algebra isomorphism $\mathsf{M}_2$ to the $2\times2$ complex matrices and one distinguished complete realization $\mathsf{M}_4$, the left regular map, in the $4\times4$ complex matrices. Every named object of the algebra — the algebra, its unit group, its norm-one group, its centre, its automorphism group — has an image under both, and the two images are related: the regular map is the isomorphism taken twice.

This article collects those images in a table and comments on them row by row. It is an index, not a source: the isomorphism $\mathsf{M}_2$ is owned by *Biquaternion 2×2 Matrix Element Representation $M_2(\mathbb{C})$*, the map $\mathsf{M}_4$ by *Biquaternion 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$*, the objects themselves by their own articles, and the observation that the two agree in the way described below by *Introduction to the 4×4 Matrix Representation $M_4(\mathbb{C})_L$ of Biquaternions*. No new result is claimed and no physical vocabulary is used.

The two maps are written down first, then tabulated, then read one object at a time. The table carries, beside each object and its two images, a column of the other realizations of the same object, and a column of the sets and correspondences attached to it. A closing section collects the classical groups that appear — $Sp(1)=S^3$, $SU(2)$, $SO(3)$, $SO^{+}(1,3)$ and $\mathrm{Spin}(1,3)$ — with the two double covers that relate them.

## The Two Correspondences

### The Isomorphism $\mathsf{M}_2$

The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0,e_1,e_2,e_3$ and central imaginary $i$; a general element is $\tilde{Q}=\sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$, and the norm is $N(\tilde{Q})=\sum_\mu Q_\mu^2$. On the algebra, ${}^{\dagger}$ denotes Hermitian conjugation, the composition of quaternion conjugation with complex conjugation, with fixed space the Hermitian sector $\mathbb{M}_+$ and anti-fixed space the anti-Hermitian sector $\mathbb{M}_-$.

The isomorphism is written $\mathsf{M}_2$. It converts a biquaternion into a $2 \times 2$ complex matrix,

$$
\mathsf{M}_2:\mathbb{B}\longrightarrow M_2(\mathbb{C}),
$$

and it is fixed by its values on the basis, the rest following by $\mathbb{C}$-linearity:

$$
\mathsf{M}_2(e_0)=I,\qquad
\mathsf{M}_2(e_1)=-i\sigma_1,\qquad
\mathsf{M}_2(e_2)=-i\sigma_2,\qquad
\mathsf{M}_2(e_3)=-i\sigma_3,
$$

and extended by $\mathsf{M}_2(ie_\mu)=i\,\mathsf{M}_2(e_\mu)$. On a general element,

$$
\mathsf{M}_2(\tilde{Q})=
\begin{pmatrix}
Q_0-iQ_3 & -iQ_1-Q_2\\
-iQ_1+Q_2 & Q_0+iQ_3
\end{pmatrix}.
$$

It is bijective, and injective in the strong sense: a given $2\times2$ matrix has one preimage, recovered by the same four entries. Two functionals transfer exactly:

$$
\operatorname{tr}\mathsf{M}_2(\tilde{Q})=2Q_0,\qquad
\det\mathsf{M}_2(\tilde{Q})=N(\tilde{Q}).
$$

### The Left Regular Map $\mathsf{M}_4$

The left regular matrix is the isomorphism written $\mathsf{M}_4$. It converts a biquaternion into a $4 \times 4$ complex matrix,

$$
\mathsf{M}_4:\mathbb{B}\longrightarrow M_4(\mathbb{C}),
$$

and it is fixed by its values on the basis, the rest following by $\mathbb{C}$-linearity: in the basis $e_0,e_1,e_2,e_3$ its $m$-th column is the coordinate column of the product $\tilde{Q}e_m$. Its functionals are

$$
\operatorname{tr}\mathsf{M}_4(\tilde{Q})=4Q_0,\qquad
\det\mathsf{M}_4(\tilde{Q})=N(\tilde{Q})^2.
$$

Unlike $\mathsf{M}_2$, the map $\mathsf{M}_4$ is not onto: its image is a four-complex-dimensional family inside the sixteen-dimensional algebra $M_4(\mathbb{C}).$ Concretely, it is the family of matrices of left multiplication by a biquaternion, and nothing else.

### The Relation Between the Two

Because $\mathsf{M}_2$ is multiplicative, $\mathsf{M}_2(\tilde{Q}\tilde{R})=\mathsf{M}_2(\tilde{Q})\mathsf{M}_2(\tilde{R})$, so left multiplication by $\tilde{Q}$ acts on the four entries of $\mathsf{M}_2(\tilde{R})$ by letting $\mathsf{M}_2(\tilde{Q})$ act on each of the two columns. Reading the columns of $\mathsf{M}_2(\tilde{R})$ as the four coordinates therefore block-diagonalizes the regular matrix, and in that basis the two blocks coincide:

$$
\mathsf{M}_4(\tilde{Q})\;=\;
\begin{pmatrix}
\mathsf{M}_2(\tilde{Q}) & 0\\
0 & \mathsf{M}_2(\tilde{Q})
\end{pmatrix}.
$$

The basis that exhibits this form is the column-adapted one: the four elements whose $\mathsf{M}_2$-images are the matrix units, grouped as the first column of $\mathsf{M}_2$, then the second. In that basis the equality above holds exactly, block for block. Equivalently, the left regular module is a direct sum of two copies of the simple module,

$$
\mathbb{B}\cong V\oplus V,\qquad \mathsf{M}_4\cong\mathsf{M}_2\oplus\mathsf{M}_2,
$$

which is the module-theoretic content of the display. The two functionals agree with this: $4Q_0$ is twice $2Q_0$, and $N^2$ is the square of $N$.

### The Other Realizations

The two maps above are not the only realizations of the algebra. Beside them the corpus uses:

- the **coefficient four-vector**, writing the element as a column of its four complex coordinates in the space $\mathbb{C}^4$, owned by *Biquaternion Four-Vector Element Representation*;
- the **spinor module** $V=\mathbb{C}^2$, the two-dimensional complex space on which $\mathsf{M}_2(\tilde{Q})$ acts by multiplication, of complex dimension $2$ and real dimension $4$; this is the spin representation of the algebra, and unlike the realizations above it has a layer of owners rather than one: the general theory in *Spin Representations and Clifford Modules with Inner Conjugation*, the spinor realized as an element of the algebra in *Spinors as Minimal Left Ideals with Inner Conjugation*, the reality conditions in *Real Spinors and Reality Conditions with Inner Conjugation*, and the biquaternion case in *Biquaternion Spin Geometry*, whose module theory is *Modules over the General Plain Algebra of Biquaternions*;
- the **even Clifford algebra** $\mathrm{Cl}_{1,3}^{+}$, isomorphic to $\mathbb{B}$ as a real algebra and hence also to $M_2(\mathbb{C})$ as a real algebra, owned by *The Clifford Algebra Representation*;
- the **realification** $\mathsf{M}_4$ over $\mathbb{R}$, writing the operator as an $8\times8$ real matrix, since the algebra is the real space $\mathbb{R}^8$;
- the **real Clifford algebra** $\mathrm{Cl}_{3,1}\cong M_4(\mathbb{R})$, the opposite-sign companion, in which the biquaternions sit as the even part and so are written as $4\times4$ real matrices;
- the **quaternionic matrix algebra** $\mathrm{Cl}_{1,3}\cong M_2(\mathbb{H})$, in which the biquaternions sit as the even part and so are written as $2\times2$ quaternionic matrices.

The coefficient column and the simple module are carriers rather than matrix algebras; the remaining four are matrix realizations, and they are the entries of the fourth column of the table below. They are all one algebra written at different sizes and over different scalars, so a statement about $\mathbb{B}$ is a statement about each of them, and the choice among them is a choice of convenience.

## The Table

Every image below is the image of the object named in the first column; a dash in no cell means the object is empty, only that no separate name was given to the image.

| object | $\dim_{\mathbb{C}}$ | $\dim_{\mathbb{R}}$ | $2\times2$ image under $\mathsf{M}_2$ | $4\times4$ image under $\mathsf{M}_4$ | other realizations | sets and correspondences |
|---|---|---|---|---|---|---|
| $\mathbb{B}$ | $4$ | $8$ | all of $M_2(\mathbb{C})$, an isomorphism | the $4$-dimensional family of left-multiplication matrices, not all of $M_4(\mathbb{C})$; equal blocks $\mathsf{M}_2(\tilde{Q})$ | the $8\times8$ real regular matrices; the $4\times4$ real matrices of $\mathrm{Cl}_{3,1}$; the $2\times2$ quaternionic matrices of $\mathrm{Cl}_{1,3}$; the coefficient column $\mathbb{C}^4$; the spinor module $V=\mathbb{C}^2$, of complex dimension $2$ | the real space $\mathbb{R}^8$; the even Clifford algebra $\mathrm{Cl}_{1,3}^{+}$ |
| $\mathbb{B}^{\times}$ | $4$ | $8$ | $GL(2,\mathbb{C})$ | block-diagonal $\mathrm{diag}(GL(2,\mathbb{C}),GL(2,\mathbb{C}))$ | the invertible $8\times8$ real matrices; the invertible quaternionic $2\times2$ matrices | $(\mathbb{C}^{\times}\times SL(2,\mathbb{C}))/\{\pm1\}$; a real Lie group of real dimension $8$, not simply connected; **only its norm-one part generates Lorentz transformations** |
| $\mathbb{B}^{\times}_1$ | $3$ | $6$ | $SL(2,\mathbb{C})$ | block-diagonal $\mathrm{diag}(SL(2,\mathbb{C}),SL(2,\mathbb{C}))$ | the $8\times8$ real matrices whose blocks are each in $SL(2,\mathbb{C})$; the quaternionic $2\times2$ matrices that are complex with determinant one | the spin group $\mathrm{Spin}(1,3)$; the universal cover of $SO^{+}(1,3)$; real dimension $6$, simply connected; **its elements are the rotors $\tilde{\Lambda}$ of the Lorentz transformations**, acting by the dagger sandwich $\tilde{Q}\mapsto\tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{*}$ |
| $S^3=Sp(1)$ | $3$ | $3$ | $SU(2)$ | block-diagonal $\mathrm{diag}(SU(2),SU(2))$ | the $4\times4$ real matrices of left multiplication on $\mathbb{R}^4$; the unit quaternionic $2\times2$ matrices; the $3\times3$ real rotations of the adjoint action | $Sp(1)=S^3=SU(2)=\mathrm{Spin}(3)$; the unit sphere of the quaternion subspace; the maximal compact subgroup of $\mathbb{B}^{\times}_1$; the double cover of $SO(3)$ |
| $U(2)$ | $4$ | $4$ | the unitary matrices $\{X:X^{\dagger}X=1\}$ | block-diagonal $\mathrm{diag}(U(2),U(2))$ | the unitary $2\times2$ matrices; the unit group of the Hermitian form | the maximal compact subgroup of $\mathbb{B}^{\times}$; $=U(1)\times SU(2)$; the compact part of the Cartan decomposition $GL(2,\mathbb{C})=U(2)\exp(\mathfrak{p})$ |
| the boosts | $3$ | $3$ | the Hermitian positive definite elements of $SL(2,\mathbb{C})$ | the same, block by block | the Hermitian positive elements $B=\exp(\sigma)$ with $\sigma$ traceless Hermitian, of unit norm; the hyperbolic space $H^3$ | the non-compact part of $\mathbb{B}^{\times}_1$; the symmetric space $SL(2,\mathbb{C})/SU(2)$; with the dilatation, the non-compact part of $\mathbb{B}^{\times}$ |
| $\mathbb{C}^{\times}e_0$ | $1$ | $2$ | the scalar matrices $\lambda I$ | the scalar matrices $\lambda I_4$ | the $8\times8$ real scalar matrices | the centre $Z(\mathbb{B})$; the scalars of $M_2(\mathbb{C})$ |
| $\{\pm e_0\}$ | $0$ | $0$ | $\{\pm I\}$ | $\{\pm I_4\}$ | $\{\pm I_8\}$ | the kernel of the two-to-one cover; the torsion of $\mathbb{B}^{\times}_1$; the discrete centre |
| $\operatorname{Aut}_{\mathbb{C}}(\mathbb{B})$ | $3$ | $6$ | conjugation $X\mapsto \mathsf{M}_2(g)X\mathsf{M}_2(g)^{-1}$ for a unit $g$, modulo scalars, that is $PGL(2,\mathbb{C})$ | the same conjugation restricted to the image, block by block | the Möbius maps of the projective line; the $4\times4$ real Lorentz matrices, since $PSL(2,\mathbb{C})\cong SO^{+}(1,3)$ | $PGL(2,\mathbb{C})=PSL(2,\mathbb{C})$; the same abstract group as the row below |
| $\mathbb{B}^{\times}_1/\{\pm e_0\}$ | $3$ | $6$ | the dagger sandwich $X\mapsto \mathsf{M}_2(\tilde{\Lambda})X\mathsf{M}_2(\tilde{\Lambda})^{\dagger}$ with $N(\tilde{\Lambda})=1$, modulo scalars, that is $PSL(2,\mathbb{C})$ | the same sandwich, block by block | the $4\times4$ real Lorentz matrices acting on $\mathbb{R}^{1,3}$ | the proper orthochronous Lorentz group $SO^{+}(1,3)$, of real dimension $6$ |

The two dimension columns are read as follows. $\dim_{\mathbb{C}}$ is the complex dimension, the number of complex parameters: the complex dimension of the group when the object is complex, and the complex dimension of the complex group of which it is a real form when it is not. It follows that $\dim_{\mathbb{R}}=2\dim_{\mathbb{C}}$ for a complex object and $\dim_{\mathbb{R}}=\dim_{\mathbb{C}}$ for a real form, so the two columns agree exactly when the object carries no complex structure. A group and its matrix image have the same dimension, so the two columns apply to the second and the third column at once.


## The Objects One by One

### The Algebra $\mathbb{B}$

**Definition.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, of complex dimension $4$ and real dimension $8$, with the product on the basis $e_0,e_1,e_2,e_3$ of the quaternions and the central $i$ commuting with everything.

**$2\times2$.** The image is all of $M_2(\mathbb{C})$, and the correspondence is an isomorphism, not merely an injective map. The inverse of the display above reads an arbitrary matrix back to its biquaternion. The trace sees only the scalar part, and the determinant is the norm, which is why invertibility of the matrix and invertibility of the element are the same condition.

**$4\times4$.** The image is the four-dimensional family of left-multiplication operators, and in the column-adapted basis each one is the block-diagonal doubling of its $2\times2$ image. The trace is $4Q_0$ and the determinant is $N^2$, so the determinant is the square of the $2\times2$ determinant; this is the general fact that the determinant of a direct sum is the product of the determinants of its summands, applied to $\mathsf{M}_4\cong\mathsf{M}_2\oplus\mathsf{M}_2$.

**Other.** The coefficient column is the realization the physics articles write a field in; the Clifford identification is the one in which the spinor module is natural, since the bivectors act on it as the matrices do; the realification is the same algebra read over $\mathbb{R}$, where it is $\mathbb{R}^8$ and the matrices are twice as large.

### The Unit Group $\mathbb{B}^{\times}$

**Definition.** $\mathbb{B}^{\times}=\{\tilde{Q}:N(\tilde{Q})\neq0\}$, the invertible elements, of complex dimension $4$ and real dimension $8$. It is an open dense subset of the algebra, hence a complex Lie group of the same dimension as the algebra, since the condition is the nonvanishing of the determinant.

**$2\times2$.** The image is $GL(2,\mathbb{C})$, by the identity $\det\mathsf{M}_2(\tilde{Q})=N(\tilde{Q})$. This is the cleanest statement of the group of units in the whole corpus: it is reached by applying the isomorphism and then taking the determinant.

**$4\times4$.** The image is block-diagonal with both blocks in $GL(2,\mathbb{C})$, by $\det\mathsf{M}_4=N^2$. The two blocks carry the same information, so no hypothesis is gained or lost by passing to the larger realization.

**Other.** Every unit factors as a central scalar times a norm-one element, $\tilde{Q}=N(\tilde{Q})^{1/2}\,\tilde{U}$ with $N(\tilde{U})=1$, and the central factor is fixed only up to a sign, so the group is the quotient $(\mathbb{C}^{\times}\times SL(2,\mathbb{C}))/\{\pm1\}$ along the diagonal. It is not simply connected: the central circle contributes a copy of $\mathbb{Z}$ to the fundamental group. Only its norm-one subgroup is the spin group.

### The Norm-One Group $\mathbb{B}^{\times}_1$

**Definition.** $\mathbb{B}^{\times}_1=\{\tilde{Q}:N(\tilde{Q})=1\}$, the level set of the norm at $1$, of complex dimension $3$ and real dimension $6$. It is a group under multiplication because the norm is multiplicative; the gradient of the norm is $2\tilde{Q}$, which never vanishes on the level set, so the set is a submanifold; and it is connected, simply connected and non-compact.

**$2\times2$.** The image is $SL(2,\mathbb{C})$, the matrices of determinant one, by $\det\mathsf{M}_2=N$. This is the realization in which the group is normally met, and it is the one in which the double cover of the Lorentz group is computed.

**$4\times4$.** The image is block-diagonal with both blocks in $SL(2,\mathbb{C})$. Each block is one copy of the spinor action, and the two copies carry the same group element.

**Other.** The group is the spin group $\mathrm{Spin}(1,3)$, and as a set it is the complexification of the sphere $S^3$, which is the reason it is non-compact: the complexification of a compact group is compact only in trivial cases. It is the universal cover of $SO^{+}(1,3)$, the covering being two-to-one. **Its elements are exactly the rotors of the Lorentz transformations**: the sandwich $\tilde{Q}\mapsto \tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{*}$ of a norm-one element is an isometry, because $N(\tilde{\Lambda})=1$ gives $N(\tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{*})=N(\tilde{Q})$, and every proper orthochronous Lorentz transformation arises this way, uniquely up to the sign of $\tilde{\Lambda}$.

### The Unit Quaternions $S^3=Sp(1)$

**Definition.** $S^3=\mathbb{H}_{\mathbb{B}}\cap\mathbb{B}^{\times}_1$, the norm-one elements of the quaternion subspace, of real dimension $3$; equivalently the real quaternions $a+be_1+ce_2+de_3$ with $a^2+b^2+c^2+d^2=1$. As the unit sphere of the quaternions it is also written $Sp(1)$, the compact symplectic group of rank one.

**$2\times2$.** The image is $SU(2)$, the unitary matrices of determinant one. The image of a general real quaternion $a+be_1+ce_2+de_3$ is the matrix of the display
$$
\begin{pmatrix}
a-id & -ib-c\\
-ib+c & a+id
\end{pmatrix},
$$
which is unitary exactly because the coefficients are real and their squares sum to one.

**$4\times4$.** The image is block-diagonal with both blocks in $SU(2)$.

**Other.** The three compact groups of real dimension three are one group here, $Sp(1)=S^3=SU(2)=\mathrm{Spin}(3)$, the last identification being the spin group of the definite form. This is the maximal compact subgroup of $\mathbb{B}^{\times}_1$, the unit sphere of the quaternion subspace, and the double cover of the rotation group $SO(3)$; it is also the group that acts by conjugation, since on the unitary slice the dagger sandwich and conjugation coincide. Acting on $\mathbb{R}^4$ by left multiplication it is written as $4\times4$ real rotation matrices, and acting on $\mathbb{R}^3$ through the adjoint action as $3\times3$ real rotation matrices.

### The Central Scalars $\mathbb{C}^{\times}e_0$

**Definition.** The centre $Z(\mathbb{B})=\mathbb{C}e_0$, with its units $\mathbb{C}^{\times}e_0=\{\lambda e_0:\lambda\neq0\}$, of complex dimension $1$ and real dimension $2$.

**$2\times2$.** The image is the scalar matrices $\lambda I$. A scalar matrix commutes with every matrix, and the centre is exactly the preimage of the scalars, since a biquaternion commutes with everything precisely when it is central.

**$4\times4$.** The image is the scalar matrices $\lambda I_4$, by the same argument applied to the doubling.

**Other.** The centre is the whole of the scalars of $M_2(\mathbb{C})$ under $\mathsf{M}_2$, and it is the kernel of the map to the automorphism group below. Its intersection with the norm-one group is only $\{\pm e_0\}$, since $N(\lambda e_0)=\lambda^2$ equals one only for $\lambda=\pm1$, which excludes the phases: $e^{i\theta}e_0$ is central but has norm $e^{2i\theta}$.

### The Centre of the Norm-One Group $\{\pm e_0\}$

**Definition.** $\mathbb{C}_{\mathbb{B}}\cap\mathbb{B}^{\times}_1=\{\pm e_0\}$, a group of order two and real dimension $0$, the torsion of $\mathbb{B}^{\times}_1$ and its full centre.

**$2\times2$.** The image is $\{\pm I\}$, the central element of $SL(2,\mathbb{C})$ of order two, which is the kernel of the map $SL(2,\mathbb{C})\to PSL(2,\mathbb{C})$.

**$4\times4$.** The image is $\{\pm I_4\}$.

**Other.** This is the kernel of the two-to-one cover of the Lorentz group, and it is the algebraic origin of the spinor sign: a rotor turned by a full turn gives $-e_0$, by two turns gives $+e_0$.

### The Automorphism Group $\operatorname{Aut}_{\mathbb{C}}(\mathbb{B})$

**Definition.** The $\mathbb{C}$-algebra automorphisms of $\mathbb{B}$, that is the bijective $\mathbb{C}$-linear maps preserving the product and fixing $e_0$, of complex dimension $3$ and real dimension $6$.

**$2\times2$.** Every automorphism is inner, because the algebra is a full matrix algebra, so the group is the image of the conjugation action of the units, with kernel the central scalars:
$$
\operatorname{Aut}_{\mathbb{C}}(\mathbb{B})\cong\mathbb{B}^{\times}/\mathbb{C}^{\times}\cong PGL(2,\mathbb{C}).
$$
In the $2\times2$ realization the automorphism attached to a unit $g$ is $X\mapsto \mathsf{M}_2(g)\,X\,\mathsf{M}_2(g)^{-1}$, taken modulo an overall scalar because a central multiple of $g$ gives the same automorphism. Over the complex field the projective general and projective special linear groups coincide, $PGL(2,\mathbb{C})=PSL(2,\mathbb{C})$, because every nonzero complex number is a square and so every projective class has a representative of determinant one.

**$4\times4$.** The same conjugation restricted to the image: conjugating a left-multiplication matrix by the image of a unit gives again a left-multiplication matrix, so the operator realization is stable under the automorphism group. In the adapted basis the conjugation acts on both blocks at once, carrying them to conjugate blocks.

**Other.** Modulo the scalar, this is the group of Möbius transformations of the Riemann sphere, acting on the projective line of the simple module. Two maps that are *not* automorphisms of this group and are often met beside it: quaternion conjugation is an anti-automorphism, since it reverses the order of a product, and complex conjugation is not $\mathbb{C}$-linear. Both are recorded in the owner article.

### The Proper Orthochronous Lorentz Group $\mathbb{B}^{\times}_1/\{\pm e_0\}$

**Definition.** The quotient of the norm-one group by its centre, a Lie group of real dimension $6$, isomorphic to the identity component of the Lorentz group of signature $(1,3)$:
$$
\mathbb{B}^{\times}_1/\{\pm e_0\}\cong SO^{+}(1,3).
$$

**$2\times2$.** The action is not conjugation but the dagger sandwich, $\tilde{Q}\mapsto \tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{*}$ for a rotor $\tilde{\Lambda}\in\mathbb{B}^{\times}_1$, modulo the sign of the rotor because $\pm\tilde{\Lambda}$ give the same transformation; in the image it is $X\mapsto \mathsf{M}_2(\tilde{\Lambda})\,X\,\mathsf{M}_2(\tilde{\Lambda})^{\dagger}$. On the Hermitian matrices of trace zero this is the Lorentz action, and modulo scalars the acting group is $PSL(2,\mathbb{C})$. The distinction from the row above is the whole content: the sandwich replaces the inverse by the conjugate transpose, which is what makes it preserve the two sectors $\mathbb{M}_+$ and $\mathbb{M}_-$ rather than only intertwining them.

**$4\times4$.** The same sandwich block by block, that is the Lorentz action written in the operator realization. Since the sandwich preserves the sectors, it preserves in particular the anti-Hermitian sector $\mathbb{M}_-$; reading an element of that sector as a real four-vector turns the sandwich into a $4\times4$ Lorentz matrix.

**Other.** This is the proper orthochronous Lorentz group: proper, because it is connected and so sits in the identity component, whence the determinant is one; orthochronous, because a connected group cannot exchange the two halves of the light cone. It preserves the norm and both sectors. Its two-to-one cover is the norm-one group, and the obstruction to inverting the cover is the sign group $\{\pm e_0\}$.

## The Bigger Groups of the Twisted Spinor

The norm-one group is not the largest group that acts on the spinor, and the two ways of enlarging it are different in kind.

**Enlarging by the scalings.** Multiplying by the centre is free, since the centre acts on the module by a scalar, and it produces the group of units,

$$
\mathbb{B}^{\times}_1=SL(2,\mathbb{C})\;\subset\;\mathbb{B}^{\times}=GL(2,\mathbb{C}),
$$

of real dimensions $6$ and $8$. This is the enlargement the polar form detects: the scale $r$ and the phase $e^{i\alpha}$ are exactly the central parameters the norm-one group discards, and they are the twist under which the module becomes the **twisted spinor**. The complex dimensions are $3$ and $4$, and the enlargement is one complex dimension, the centre.

**Enlarging by the conformal generators.** A different group acts on the same four-complex-dimensional space. The algebra $\mathbb{B}$ has complex dimension $4$, so it is also the twistor module $\mathbb{T}=\mathbb{C}^4$, and the group of its conformal structure is

$$
SU(2,2)\cong\mathrm{Spin}(4,2),
$$

of real dimension $15$, the double cover of the conformal group $SO^{+}(2,4)$ of the Minkowski space. This group is **not** a subgroup of $\mathbb{B}^{\times}$: it shares the Lorentz subgroup but enlarges it by the translations and the special conformal transformations, which are not multiplications of the algebra. The two enlargements are therefore of different kinds, and only the first is a quotient of the algebra's own group.

**The chain of the spinor groups.** With both dimensions and with the module each group carries, the picture is

| group | $\dim_{\mathbb{C}}$ | $\dim_{\mathbb{R}}$ | module |
|---|---|---|---|
| $SU(2)=\mathrm{Spin}(3)$ | $3$ | $3$ | the definite spinor, of complex dimension $2$ |
| $SL(2,\mathbb{C})=\mathrm{Spin}(1,3)$ | $3$ | $6$ | the spinor, the same module |
| $GL(2,\mathbb{C})=\mathbb{B}^{\times}$ | $4$ | $8$ | the **twisted** spinor, the same module, a non-trivial twist |
| $SU(2,2)=\mathrm{Spin}(4,2)$ | $15$ | $15$ | the twistor, that is the algebra $\mathbb{B}$ itself |

The real form $SL(2,\mathbb{C})$ and the real form $SU(2,2)$ both have $\dim_{\mathbb{R}}=\dim_{\mathbb{C}}$, while the complex group $\mathbb{B}^{\times}$ has $\dim_{\mathbb{R}}=2\dim_{\mathbb{C}}$; the spinor module stays $\mathbb{C}^2$ at every step, since the twist changes the weight and not the module.

**The boost.** The Lorentz group is not compact, and the table had listed only its compact part: the boosts were the missing entry, and the row has been added. In the Cartan decomposition of the group of units,

$$
GL(2,\mathbb{C})=U(2)\exp(\mathfrak{p}),
\qquad
U(2)=SU(2)\times U(1),
\qquad
\mathfrak{p}=\{\text{Hermitian }2\times2\text{ matrices}\},
$$

the compact part $U(2)$ of real dimension $4$ is the rotor $SU(2)$ together with the phase $U(1)$, and the non-compact part $\exp(\mathfrak{p})$, also of real dimension $4$, is the **boosts** (Hermitian traceless, three parameters) together with the **dilatation** (the scalar, one parameter). The polar form is this decomposition read factor by factor,

$$
\tilde{Q}=r\,e^{i\alpha}\,B\,\hat{q}
=\underbrace{(e^{i\alpha}\hat{q})}_{\text{compact, }U(2)}\;\underbrace{(rB)}_{\text{non-compact, }\exp(\mathfrak{p})},
$$

so the boost is the non-compact factor of the Lorentz group, the symmetric space $SL(2,\mathbb{C})/SU(2)=H^3$ of real dimension $3$, and it sits beside the dilatation as the four non-compact directions of the twisted group. With Lorentz alone the boost is present and the dilatation is not; with the twist the two are the two halves of the non-compact part.


## The Sets and the Double Covers

The groups reached in the table are classical, and two of them sit over another as a two-sheeted cover. They are collected here, with the real dimension and the role of each.

| set | definition or identification | real dimension | role |
|---|---|---|---|
| $Sp(1)$ | the unit quaternions, that is the unit sphere of $\mathbb{H}$ | $3$ | the motions of the definite form; $=S^3=SU(2)=\mathrm{Spin}(3)$ |
| $S^3$ | the unit sphere of the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ | $3$ | the carrier of the definite motions; $=Sp(1)$ |
| $SU(2)$ | the unitary $2\times2$ matrices of determinant one | $3$ | the double cover of $SO(3)$; the compact factor of $SL(2,\mathbb{C})$ |
| $SO(3)$ | the rotations of $\mathbb{R}^3$ | $3$ | the definite motions; $=SU(2)/\{\pm I\}$ |
| $SL(2,\mathbb{C})$ | the $2\times2$ complex matrices of determinant one | $6$ | the complexification of $SU(2)$; the carrier of the indefinite motions; $=\mathbb{B}^{\times}_1$ |
| $SO(1,3)$ | the Lorentz group of the form of signature $(1,3)$, determinant one | $6$ | the indefinite motions; two components, time-preserving and time-reversing |
| $SO^{+}(1,3)$ | the proper orthochronous Lorentz group | $6$ | the identity component; $=\mathbb{B}^{\times}_1/\{\pm e_0\}=PSL(2,\mathbb{C})$ |
| $\mathrm{Spin}(1,3)$ | the spin group of Lorentzian signature | $6$ | the universal cover of $SO^{+}(1,3)$; $=\mathbb{B}^{\times}_1=SL(2,\mathbb{C})$ |
| $\mathrm{B}_0$ | the trace-free part, the elements with $Q_0=0$ | $6$ | the Lie algebra, $\mathrm{B}_0\cong\mathrm{so}(1,3)$, the Lie algebra of $\mathbb{B}^{\times}_1$ and of $SO^{+}(1,3)$ |
| $\{\pm e_0\}$ | the centre of $\mathbb{B}^{\times}_1$ | $0$ | the kernel of both covers; discrete |

**The two double covers.** The definite form and the indefinite form each carry a two-sheeted cover, and the two are the same construction applied to the compact group and to its complexification:

$$
SU(2)\longrightarrow SO(3),\qquad
\mathbb{B}^{\times}_1=\mathrm{Spin}(1,3)\longrightarrow SO^{+}(1,3).
$$

In both, the kernel is the order-two centre, $\{\pm I\}$ in the matrix picture and $\{\pm e_0\}$ in the algebra, and in both a full turn of the covering element gives the negative of the identity cover element while two turns give the identity. The first cover is between compact groups; the second is between non-compact ones, and it is the complexification of the first, the unit quaternions being replaced by $SL(2,\mathbb{C})$.

**Why the quotient is a Lie group.** The centre $\{\pm e_0\}$ is discrete and closed, so the quotient of $\mathbb{B}^{\times}_1$ by it is again a Lie group, and the quotient map is a local diffeomorphism. Since $\mathbb{B}^{\times}_1$ is simply connected, it is the universal cover of that quotient. The same argument in the $2\times2$ picture is the standard one for $SL(2,\mathbb{C})\to PSL(2,\mathbb{C})$.

**The Lie algebra is not the group.** $\mathrm{B}_0$, the trace-free part, has real dimension $6$ and is closed under the bracket, and it is naturally identified with the Lie algebra $\mathrm{so}(1,3)$; it is the Lie algebra of the group $SO^{+}(1,3)$ and of its cover, not a group itself. The distinction matters for the notation: $\mathrm{B}_0\cong\mathrm{so}(1,3)$ and $\mathbb{B}^{\times}_1\cong\mathrm{Spin}(1,3)$ are statements of different kinds, the first about a Lie algebra and the second about a Lie group, and the two objects have the same real dimension.

**The Lorentz group and its components.** The full orthogonal group of the form has four connected components, indexed by the sign of the determinant and by the time orientation. Requiring the determinant to be one leaves $SO(1,3)$, which still has two components; requiring in addition that the time orientation be preserved leaves the identity component $SO^{+}(1,3)$ of the table. The cover $\mathbb{B}^{\times}_1$ is connected, so the two components of $SO(1,3)$ are exchanged by no element of the cover's image, and the two-to-one cover is a cover of the identity component only.

## What the Table Does Not Say

**The $4\times4$ map is not an isomorphism.** $\mathsf{M}_2$ is onto $M_2(\mathbb{C})$, but $\mathsf{M}_4$ is not onto $M_4(\mathbb{C})$: its image is four-complex-dimensional, against sixteen. The table's entries in that column are faithful images, not the whole matrix algebra, and the phrase "the $4\times4$ matrix representation" names a representation, not an isomorphism.

**The determinants are not the same function.** $\det\mathsf{M}_2=N$ and $\det\mathsf{M}_4=N^2$, and the traces are $2Q_0$ and $4Q_0$. Only the criterion is common, since $N\neq0$ and $N^2\neq0$ are the same condition. A determinant computed in the wrong realization is off by a square.

**The sector structure lives in $\mathsf{M}_2$, not in $\mathsf{M}_4$.** Hermitian against anti-Hermitian, the signatures $(1,3)$ and $(3,1)$, the compact subalgebra and the boosts — all of these are read cleanly from the single $2\times2$ matrix, because ${}^{\dagger}$ on the image is the conjugate transpose. In the $4\times4$ realization each is doubled, and the statement becomes one about both blocks at once. The sector theorems are therefore stated in the $2\times2$ realization for a reason and not by accident.

**The two actions in the last two rows are different.** The automorphism group acts by conjugation $X\mapsto \mathsf{M}_2(g)X\mathsf{M}_2(g)^{-1}$ for a unit $g$; the Lorentz quotient acts by the dagger sandwich $X\mapsto \mathsf{M}_2(\tilde{\Lambda})X\mathsf{M}_2(\tilde{\Lambda})^{\dagger}$ for a rotor $\tilde{\Lambda}$ of norm one. They agree exactly on the unitary slice, by the identity $\tilde{\Lambda}^{*}=\tilde{\Lambda}^{-1}$ for a unitary $\tilde{\Lambda}$; off it they differ, and the sandwich is not multiplicative in the acting rotor across a central rescaling, while the conjugation is insensitive to it.

**The Lorentz transformations correspond to the norm-one group.** The rotors are the elements of $N=1$, that is of the norm-one group $\mathbb{B}^{\times}_1$ of row three: its $2\times2$ image is $SL(2,\mathbb{C})$, its $4\times4$ image is the diagonal copy of $SL(2,\mathbb{C})$, and it is the spin group $\mathrm{Spin}(1,3)$. A rotor $\tilde{\Lambda}$ acts on a biquaternion by the sandwich $\tilde{Q}\mapsto \tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{*}$, and the map from the group onto the transformations is two-to-one, with kernel the sign group $\{\pm e_0\}$ of row six, so that the transformations are the quotient of row eight, $\mathbb{B}^{\times}_1/\{\pm e_0\}\cong SO^{+}(1,3)$. The condition is exactly $N=1$: the sandwich multiplies the norm by $|N(\tilde{\Lambda})|^2$, because the norm is multiplicative and $N(\tilde{\Lambda}^{*})=\overline{N(\tilde{\Lambda})}$, so $N=1$ is what makes it an isometry, and a zero divisor generates nothing at all, having no inverse.

**The two groups in the last two rows are the same abstract group.** Both are $PSL(2,\mathbb{C})$, which is also $SO^{+}(1,3)$, so the two rows are not distinguished by their group but by the action and by the carrier the action is applied to. The conjugation is an automorphism of the algebra; the sandwich is an isometry of the sectors. This is why the same group appears twice in the table with two different descriptions, and it is not a duplication.

**The last two columns are neither exclusive nor exhaustive.** The four-vector, Clifford, spinor and real realizations are different ways of writing the same algebra, and an object corresponds to all of them at once. The Clifford realization is singled out only because the spinor module is natural there.

**The doubling is not the chiral splitting.** $\mathsf{M}_4\cong\mathsf{M}_2\oplus\mathsf{M}_2$ is one spinor taken twice, not the left-handed and the right-handed spinor. Chirality sits inside each copy: the spin module splits into its two chiral spaces over $\mathbb{C}$, and the regular representation doubles that splitting rather than being it. The two ideals that realize the module inside the algebra are therefore not the chiral halves, and the identification is owned by *Biquaternion Spin Geometry*, §*Spinors as the Minimal Left Ideals*.

**The spinor is a module, not a matrix.** The word spinor names the space that a realization acts on, not any one of its matrix forms: the $2\times2$ matrix is a coordinate realization of the algebra, while the spinor is the $V$ on which it acts. The corpus gives that space its own articles rather than folding it into the matrix ones — *Spin Representations and Clifford Modules with Inner Conjugation* for the general spin representations, *Spinors as Minimal Left Ideals with Inner Conjugation* for a spinor realized as an element of the algebra, *Real Spinors and Reality Conditions with Inner Conjugation* for the real structures, and *Biquaternion Spin Geometry* for the biquaternion case. Reading the module off the matrix is exactly what produces the chiral-splitting error recorded above.

**The Lorentz group has no two-dimensional module.** Only the cover acts on the spinor: $\mathbb{B}^{\times}_1=SL(2,\mathbb{C})$ acts on $V=\mathbb{C}^2$ by multiplication, while its quotient $SO^{+}(1,3)$ acts only up to sign, because $\{\pm e_0\}$ acts as $\pm I$. This is the module-theoretic face of the cover, and it is the correct sense in which the algebra has a spinor representation: the representation is of the algebra and of its norm-one group, not of the Lorentz group.

**Only the norm-one group is the spin group.** The full unit group $\mathbb{B}^{\times}$ is not simply connected and is not $\mathrm{Spin}(1,3)$; it contains the nonvanishing central scalars, whose circle contributes a copy of $\mathbb{Z}$.

## Summary

The algebra $\mathbb{B}$ has one algebra isomorphism $\mathsf{M}_2$ onto $M_2(\mathbb{C})$ and one faithful regular map $\mathsf{M}_4$ into $M_4(\mathbb{C})$, and the second is the first taken twice: in the column-adapted basis the regular matrix is block-diagonal with two equal blocks $\mathsf{M}_2(\tilde{Q})$. Every named object has an image under both, and the images interlock: the determinant of the element is $N$ in the small picture and $N^2$ in the large one, so the group of units becomes $GL(2,\mathbb{C})$ and then a doubled copy of it, the norm-one group becomes $SL(2,\mathbb{C})$, the unit quaternions become $SU(2)$, the centre becomes the scalars, and the sign group becomes its kernel. The automorphism group is the units modulo the centre, acting by conjugation; the Lorentz quotient is the norm-one group modulo the sign group, acting by the dagger sandwich. The classical groups reached are the compact $Sp(1)=S^3=SU(2)=\mathrm{Spin}(3)$, its complexification $\mathbb{B}^{\times}_1=SL(2,\mathbb{C})=\mathrm{Spin}(1,3)$, and the common quotient $SO^{+}(1,3)=\mathbb{B}^{\times}_1/\{\pm e_0\}=PSL(2,\mathbb{C})$, which is also the automorphism group; the two covers $SU(2)\to SO(3)$ and $\mathbb{B}^{\times}_1\to SO^{+}(1,3)$ have the same discrete kernel, and the Lie algebra $\mathrm{B}_0\cong\mathrm{so}(1,3)$ is the infinitesimal form of the second. The table is an index, and each row is owned by the article named beside it.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $\tilde{Q}$ | a general biquaternion $\sum_\mu Q_\mu e_\mu$, the element acted on |
| $\tilde{\Lambda}$ | a rotor, an element of the norm-one group $\mathbb{B}^{\times}_1$, acting by $\tilde{Q}\mapsto\tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{*}$ |
| $g$ | a unit, an element of $\mathbb{B}^{\times}$, acting on the algebra by conjugation |
| $\mathsf{M}_2$ | the algebra isomorphism $\mathbb{B}\to M_2(\mathbb{C})$ |
| $\mathsf{M}_4$ | the left regular matrix, $\mathsf{M}_4(\tilde{Q})\operatorname{col}(\tilde{R})=\operatorname{col}(\tilde{Q}\tilde{R})$ |
| $N$ | the biquaternion norm $\sum_\mu Q_\mu^2$ |
| ${}^{\dagger}$ | Hermitian conjugation; fixed space $\mathbb{M}_+$, anti-fixed space $\mathbb{M}_-$ |
| $\mathbb{B}^{\times}$ | the invertible elements, $N\neq0$ |
| $\mathbb{B}^{\times}_1$ | the norm-one elements, $N=1$ |
| $\mathrm{B}_0$ | the trace-free part, the elements with $Q_0=0$, isomorphic to the Lie algebra $\mathrm{so}(1,3)$ |
| $S^3=Sp(1)$ | the unit quaternions, the unit sphere of the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ |
| $SU(2)$, $SO(3)$ | the unitary $2\times2$ matrices of determinant one, and the rotations of $\mathbb{R}^3$ |
| $\mathrm{Spin}(1,3)$ | the spin group of Lorentzian signature, $=\mathbb{B}^{\times}_1$ |
| $SO^{+}(1,3)$ | the proper orthochronous Lorentz group, $=\mathbb{B}^{\times}_1/\{\pm e_0\}$ |
| $GL$, $SL$, $SU$, $Sp$, $PGL$, $PSL$ | the general, special, special unitary, symplectic, projective general and projective special linear groups |
| $\dim_{\mathbb{C}}$, $\dim_{\mathbb{R}}$ | the complex and the real dimension; equal for a real form, the real one being the double for a complex group |
| $U(2)$ | the unitary $2\times2$ matrices, the maximal compact subgroup of $\mathbb{B}^{\times}$ |
| $H^3$ | the hyperbolic three-space, the boosts, $=SL(2,\mathbb{C})/SU(2)$ |
| $\mathfrak{p}$ | the Hermitian matrices, the non-compact summand of the Cartan decomposition |
| $SU(2,2)=\mathrm{Spin}(4,2)$ | the conformal group of the Minkowski space, of real dimension $15$; the twistor group |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors*, second edition, Cambridge University Press, 2001, for the isomorphism of a central simple algebra with a full matrix algebra and for the spin groups.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge University Press, 1995, for the identification of the biquaternions with the even part of $\mathrm{Cl}_{1,3}$ and with $M_2(\mathbb{C})$.
- William Fulton and Joe Harris, *Representation Theory: A First Course*, Springer, 1991, for the decomposition of the regular representation into two copies of the simple module.
- Within the corpus, the owner articles *Biquaternion 2×2 Matrix Element Representation $M_2(\mathbb{C})$*, *Biquaternion 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$*, *Biquaternion Four-Vector Element Representation*, *The Clifford Algebra Representation*, *Biquaternion Norm and Invertibility*, *Biquaternion Lie Group and Exponential Structure*, *The 12 Products of the Biquaternion Complex Space*, *The Biquaternion Unit Group as a Topological Group*, *Comparison of the Six Subspaces*, *Biquaternion Automorphisms and Derivations*, *Biquaternion Rotations and Lorentz Transformations*, *Biquaternion Spin Geometry* and *Matrix Groups and Classical Groups*.
