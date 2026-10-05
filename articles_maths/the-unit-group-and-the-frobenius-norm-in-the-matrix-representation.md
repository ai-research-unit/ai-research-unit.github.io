# __The Unit Group and the Frobenius Norm in the Matrix Representation__

## Introduction

The Euclidean norm of the biquaternion algebra is the Frobenius norm of its matrix realization, and the two topological objects attached to the algebra — its underlying eight-dimensional real space and its group of units — are therefore read most directly in the matrix picture. This article collects those readings. It is the TOPOLOGY entry of the matrix-representation group. The general topology of the algebra is owned by *Biquaternion Topology* and the general group topology by *The Biquaternion Unit Group as a Topological Group*; nothing of either is reproved here, and the article states only what the realization $\Phi$ adds.

The realization is that of *Biquaternion 2×2 Matrix Element Representation*, with $\Phi(e_0) = I$ and $\Phi(e_k) = -i\sigma_k$; the Euclidean norm and the Frobenius norm are those of *The Forms in the Matrix Representation of the Biquaternion Algebra*.

## The Frobenius Norm and the Isometry

**Proposition (the realization is a similarity of Euclidean spaces).** For every biquaternion $\tilde{Q}$,

$$
\bigl\|\Phi(\tilde{Q})\bigr\|_F = \sqrt 2 \,\bigl\|\tilde{Q}\bigr\|_E ,
$$

so the realization, regarded as a real-linear map

$$
\Phi : \mathbb{B}_{\mathbb{R}} \longrightarrow M_2(\mathbb{C})_{\mathbb{R}} \cong \mathbb{R}^8 ,
$$

is a **linear isometry up to the fixed scale $\sqrt 2$**: it is injective, it is onto, and it multiplies all lengths by the same constant.

**Proof.** The trace identity of the companion FORM article gives $\|\Phi(\tilde{Q})\|_F^2 = \operatorname{Tr}(\tilde{Q}\tilde{Q}^{*}) = 2\|\tilde{Q}\|_E^2$, and the square roots agree. Injectivity and surjectivity are the isomorphism of the realization. $\square$

Two immediate consequences, recorded here because they are read from the realization:

- The **underlying topology of the algebra is the Euclidean topology of $\mathbb{R}^8$**, transported along $\Phi$; the algebra is a complete, contractible real space, and its unit sphere in the Euclidean norm is the $7$-sphere $S^7$. The development of the underlying space and its contractibility is *The Euclidean Topology of the Biquaternion Algebra*, §*The Contractibility of the Algebra*.
- The scale $\sqrt 2$ is the trace normalisation $\operatorname{Tr}\Phi(\tilde{Q}) = 2Q_0$; with the normalised map $\Phi/\sqrt 2$ the realization becomes an exact isometry between $\mathbb{B}$ with the Euclidean norm and $M_2(\mathbb{C})$ with the Frobenius norm.

## The Unit Group

**Proposition (the unit groups in matrix form).** Under $\Phi$,

$$
\mathbb{B}^\times \cong GL_2(\mathbb{C}), \qquad \{\tilde{Q} : \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = 1\} \cong SL_2(\mathbb{C}).
$$

**Proof.** The realization is an algebra isomorphism, so it carries invertible elements to invertible matrices, giving the first statement; and it carries the biquaternion norm to the determinant, $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \det\Phi(\tilde{Q})$, so the locus $N = 1$ is the determinant-one locus, giving the second. $\square$

The unit-norm group is the group that acts on the Hermitian subspace in the two-sided action of *The 4×4 Regular Matrix Representation under the Four Forms*, §*The Topology Induced by the Hermitian Form*; in the matrix picture it is $SL_2(\mathbb{C})$ acting by $*$-congruence on the Hermitian matrices.

## The Maximal Compact Slice

**Proposition (the compact slice).** The maximal compact subgroup of $\mathbb{B}^\times \cong GL_2(\mathbb{C})$ is $U(2)$, and the maximal compact subgroup of the unit-norm group $\cong SL_2(\mathbb{C})$ is $SU(2)$, which is the double cover of $SO(3)$:

$$
SU(2) \cong \mathrm{Spin}(3), \qquad SU(2)/\{\pm I\} \cong SO(3).
$$

**Proof.** The unitary matrices are the compact subgroup of the complex general linear group by the polar decomposition, and the determinant-one unitary matrices are the compact subgroup of the special linear group; the double cover of $SO(3)$ by $SU(2)$ is the standard identification of the unit quaternions. $\square$

The slice is the matrix form of the maximal compact subgroup of the unit group, whose retraction and homotopy are owned by *The Unitary Group of the Biquaternion Algebra*, §*The Structure of the Unitary Group*; here it is recorded only as the unitary slice of the realization.

## The Unit Spheres

The Euclidean unit spheres of the algebra and of its distinguished subspaces have a direct matrix reading.

| object | Euclidean description | matrix description |
|---|---|---|
| the algebra $\mathbb{B}$ | unit sphere $S^7$ | the Frobenius sphere $\|\Phi(\tilde{Q})\|_F^2 = 2$ |
| the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ | unit sphere $S^3$ | the Frobenius sphere on the complex matrices with real entries |
| the roots of $-1$ in $\mathbb{H}_{\mathbb{B}}$ | $S^2$ | the traceless anti-Hermitian matrices of Frobenius norm $\sqrt 2$ |
| the Hermitian subspace $\mathbb{M}_+$ | the null cone and its link | the Hermitian matrices, of signature $(1,3)$ |

The third row is the matrix form of the root sphere of *The Six Subspaces and the Elements* and of the classification of *Biquaternion Square Roots of Minus One, Zero and Plus One*; the general topology of the unit sphere is *The Euclidean Topology of the Biquaternion Algebra*, §*The Euclidean Unit Sphere*, and that of the link of the null cone is *Biquaternion Topology*, §*The link of the null cone*.

## The Lorentz Group and Its Connectedness

The one topological statement that the realization adds to the units is the connectedness of the Lorentz image.

**Proposition (the image is connected).** The two-sided action of the unit-norm group on $\mathbb{M}_+$,

$$
SL_2(\mathbb{C}) \times \mathbb{M}_+ \longrightarrow \mathbb{M}_+, \qquad (\tilde{A}, \tilde{Q}) \longmapsto \tilde{A}\tilde{Q}\tilde{A}^{*},
$$

has image in the identity component $SO^+(1,3)$ of the orthogonal group of the form, because $SL_2(\mathbb{C})$ is connected and the action is continuous.

**Proof.** The action is continuous in $\tilde{A}$, the group $SL_2(\mathbb{C})$ is connected as a complex algebraic group, and the continuous image of a connected set is connected; the image therefore lies in the identity component of the orthogonal group. The double cover itself, with its central kernel of order two, is *The 4×4 Regular Matrix Representation under the Four Forms*, §*The Topology Induced by the Hermitian Form*; the group and its geometry are *Biquaternion Rotations and Lorentz Transformations*. $\square$

## Summary

The matrix realization is a linear similarity of Euclidean spaces, $\|\Phi(\tilde{Q})\|_F = \sqrt2\|\tilde{Q}\|_E$, so the topology of the algebra is the Euclidean topology of $\mathbb{R}^8$ read on the matrices, with unit sphere $S^7$ and its subspaces carrying $S^3$ and $S^2$ in the familiar places. The unit group is $GL_2(\mathbb{C})$ and the unit-norm group is $SL_2(\mathbb{C})$, because $N = \det$; their maximal compact subgroups are $U(2)$ and $SU(2) = \mathrm{Spin}(3)$. The two-sided action of the unit-norm group on the Hermitian matrices has image in $SO^+(1,3)$, and its connectedness is the connectedness of $SL_2(\mathbb{C})$. The general topology of the algebra and of its unit group is *Biquaternion Topology* and *The Biquaternion Unit Group as a Topological Group*; this article is their matrix reading.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\|\cdot\|_F$ | Frobenius norm; $\|\Phi(\tilde{Q})\|_F = \sqrt2\,\|\tilde{Q}\|_E$ |
| $S^7$ | Euclidean unit sphere of $\mathbb{B}_{\mathbb{R}} \cong \mathbb{R}^8$ |
| $S^3$, $S^2$ | Unit spheres of the quaternion subspace and of its root set |
| $GL_2(\mathbb{C})$ | Group of units of the realization |
| $SL_2(\mathbb{C})$ | Unit-norm group, $\{\tilde{Q} : \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = 1\}$ |
| $U(2)$, $SU(2)$ | Maximal compact subgroups of $GL_2(\mathbb{C})$ and $SL_2(\mathbb{C})$ |
| $\mathrm{Spin}(3) \cong SU(2)$ | Double cover of $SO(3)$ |
| $SO^+(1,3)$ | Identity component of the orthogonal group, image of the two-sided action |

## Further Reading

- *Biquaternion 2×2 Matrix Element Representation* (`articles_maths/biquaternion-2x2-matrix-element-representation.md`), for the realization, the determinant and the group of units
- *The Forms in the Matrix Representation of the Biquaternion Algebra* (`articles_maths/the-forms-in-the-matrix-representation-of-the-biquaternion-algebra.md`), for the Euclidean and Frobenius norms and the trace identity
- *Biquaternion Topology* (`articles_maths/biquaternion-topology.md`), for the underlying space, its contractibility, the unit sphere and the link of the null cone
- *The Biquaternion Unit Group as a Topological Group* (`articles_maths/the-biquaternion-unit-group-as-a-topological-group.md`), for the group topology, the retraction and the homotopy
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the units, the real size function and the invertibility criterion
- *Biquaternion Rotations and Lorentz Transformations* (`articles_maths/biquaternion-rotations-and-lorentz-transformations.md`), for the Lorentz group and its geometry
