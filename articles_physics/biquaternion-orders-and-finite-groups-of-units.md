# __Biquaternion Orders and Finite Groups of Units__

## Introduction

The biquaternion algebra carries integral structures, and the groups of units of those structures are the finite groups attached to the algebra. The real slice $\mathbb{H}_{\mathbb{B}}\cong\mathbb{H}$ contains the classical quaternion orders — the Lipschitz order and the Hurwitz order — whose groups of units are the quaternion group of order eight and the binary tetrahedral group of order twenty-four. The unit sphere of the real slice has for finite subgroups the cyclic groups, the binary dihedral groups and the three binary polyhedral groups of orders $24$, $48$ and $120$, and those groups draw the figures of the theory: the regular $24$-cell with the Hurwitz units as its vertices, and the McKay correspondence. The complex order, the integral biquaternions, behaves differently: its group of units is infinite, generated along a nilpotent direction, so the finite unit groups are the real ones.

This article is the integral and finite-group entry of the Topology group. The unit criterion is the biquaternion norm, which is *Biquaternion Norm and Invertibility*, and the topology of the group of units is *The Biquaternion Unit Group as a Topological Group*. Those results are cited, not re-derived, and the present article owns the orders inside $\mathbb{B}$, their finite unit groups as abstract groups, the figures those groups determine in the real sector, and the infinite unit group of the complex order. The quotient $Sp(1)/\{\pm e_0\}\cong SO(3)$, the rotor, the twofold cover and the rotation $\rho_v(\tilde R)=-v\tilde Rv^{-1}$ are *Biquaternion Rotations and Lorentz Transformations*, cited.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$ and units $e_k^2=-e_0$; the real slice is $\mathbb{H}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_0,e_1,e_2,e_3\}$, and the material sector is $\mathbb{M}_-$.

## The Quaternion Orders

**Definition.** A subset $\Lambda\subseteq\mathbb{H}$ is an **order** if it is a subring and a free abelian group of rank four whose $\mathbb{Q}$-span is $\mathbb{H}$; equivalently, it is a lattice that is also closed under multiplication and contains $e_0$.

**Definition.** The **Lipschitz order** is
$$
\mathcal{L}=\mathbb{Z}e_0\oplus\mathbb{Z}e_1\oplus\mathbb{Z}e_2\oplus\mathbb{Z}e_3,
$$
and the **Hurwitz order** is the larger lattice obtained by adjoining the half-integral element $\omega=\tfrac12(e_0+e_1+e_2+e_3)$,
$$
\mathcal{L}'=\mathcal{L}\oplus\mathbb{Z}\omega .
$$

**Theorem.** The Hurwitz order contains the Lipschitz order with index two, and it is a maximal order of $\mathbb{H}$; the Lipschitz order is an order but is not maximal.

*Proof.* The change of basis from $(e_0,e_1,e_2,e_3)$ to $(\omega,e_1,e_2,e_3)$ has determinant $\tfrac12$, so the index is $|\det|^{-1}=2$; equivalently $\mathcal{L}'/\mathcal{L}\cong\mathbb{Z}/2$, of prime order. Maximality of $\mathcal{L}'$ is the classical statement that the Hurwitz order is a maximal order in the rational quaternion algebra, and the half-integral element of $\mathcal{L}'\setminus\mathcal{L}$ witnesses that $\mathcal{L}$ is not maximal.

**Remark.** The orders are orders in the *real* quaternion algebra, inside the quaternion subspace of $\mathbb{B}$. The biquaternion algebra contains them and their complexification, and it is the complexification that changes the nature of the unit group, below.

**Physical reading.** The two orders are the two lattices the real sector admits, and they are the two the physics of the crystalline sector uses. Their relation is the relation between the two ways of assigning half-integer coordinates to a site, and the element $\omega$ is the half-integral shift. The lattices lie in the real sector $\mathbb{H}_{\mathbb{B}}$, the slice on which the material time $ict$ vanishes.

## The Groups of Units

**Theorem.** The group of units of the Lipschitz order is the eight-element quaternion group,
$$
\mathcal{L}^{\times}\cong Q_8=\{\pm e_0,\pm e_1,\pm e_2,\pm e_3\},
$$
and the group of units of the Hurwitz order is the twenty-four-element binary tetrahedral group,
$$
(\mathcal{L}')^{\times}\cong 2T=\{\pm e_0,\pm e_1,\pm e_2,\pm e_3,\tfrac12(\pm e_0\pm e_1\pm e_2\pm e_3)\}.
$$

**Proof.** On real quaternion coordinates the norm is $N(\tilde q)=\sum_\mu q_\mu^2\geq0$, an integer for $\tilde q$ in either order; the inverse is $\tilde q^{-1}=\tilde q^{\natural}/N(\tilde q)$ with $\tilde q^{\natural}$ the quaternion conjugate, and $\tilde q^{\natural}$ lies in the order whenever $\tilde q$ does, so $\tilde q$ is a unit exactly when $N(\tilde q)=1$. The norm-one elements with integer coordinates are the eight signed units $\pm e_\mu$, and with half-integer coordinates they are those together with the sixteen elements $\tfrac12(\pm e_0\pm e_1\pm e_2\pm e_3)$, of norm one. The resulting groups are closed under multiplication, have the stated orders, and are the quaternion group and the binary tetrahedral group respectively.

**Remark (the two indices).** The lattices have index $2$, but the unit groups have index $24/8=3$: the Lipschitz units are a proper subgroup of index three in the Hurwitz units, so the two notions of index do not agree.

**Physical reading.** The finite unit groups are the **spin point groups** the material sector admits: they are the double covers of the crystallographic point groups, so the quaternion group $Q_8$, the double cover of the four-group, is the smallest non-abelian one, and $2T$ is the next. They are the finite groups of symmetry of a discrete configuration of the material sector, and because they lie in the definite real slice no null direction enters them.

## The Finite Subgroups of the Unit Sphere

The unit quaternions $Sp(1)=S^3$ form a group with centre $\{\pm e_0\}$, and the quotient
$$
Sp(1)/\{\pm e_0\}\cong SO(3)
$$
is the rotation group of Euclidean three-space (*Biquaternion Rotations and Lorentz Transformations*). The cover being twofold, a finite rotation group is the one that preserves a figure, so the figures classify the finite rotation groups first.

**Physical reading.** The unit sphere is the group of the spatial rotations of the material sector, and the twofold cover is the same doubling that the rotor of *Biquaternion Rotations and Lorentz Transformations* carries: a full turn of the figure is a half-turn of the quaternion. This is why the discrete symmetries of a material configuration are read on $Sp(1)$ and not on $SO(3)$: the extra sign is what a spinor carries and a position does not.

**Theorem.** The finite subgroups of $SO(3)$ are the rotation groups of the plane and the three Platonic figures: the cyclic groups, the rotation groups of a regular pyramid; the dihedral groups, the rotation groups of a regular prism; and the three polyhedral groups
$$
T\ (12),\qquad O\ (24),\qquad I\ (60),
$$
the rotation groups of the tetrahedron, the octahedron and the icosahedron.

**Theorem.** The finite subgroups of the unit quaternions $Sp(1)=S^3$ are the twofold preimages of these: the cyclic groups, the **binary dihedral** groups, and the three binary polyhedral groups
$$
2T\ (24),\qquad 2O\ (48),\qquad 2I\ (120),
$$
the binary tetrahedral, octahedral and icosahedral groups.

**Proof.** Let $\Gamma\subset Sp(1)$ be finite. Its image under the quotient is a finite subgroup $\bar\Gamma\subset SO(3)$, and the cover being twofold, $|\Gamma|=2|\bar\Gamma|$; conversely the preimage of a finite subgroup of $SO(3)$ is finite, of twice the order. The preimage of a cyclic group of order $n$ is cyclic of order $2n$, since the preimage of a cyclic group is cyclic; the preimage of a dihedral group of order $2n$ is a binary dihedral group of order $4n$; and the preimages of the three polyhedral groups of orders twelve, twenty-four and sixty are $2T$, $2O$ and $2I$, of orders twenty-four, forty-eight and one hundred twenty.

**Physical reading.** The binary polyhedral groups are the **spin point groups**: they are the double covers of the crystallographic point groups, and the doubling is the spin double cover, so a finite unit group is a group of spins and not only of positions. The orders $24$, $48$, $120$ are the orders of the binary tetrahedral, octahedral and icosahedral groups, and the appearance of the icosahedral case is the algebraic origin of the icosahedral symmetry in the framework's crystallography. Because the finite groups are the **real** ones, a finite symmetry of a physical configuration is a symmetry of the material sector and not of the informational one. The Hurwitz order realises $2T$ integrally, as above; the other two are figures of the unit sphere without an integral model of the same kind.

## The 24-Cell and the Twelve Rotations

The twenty-four Hurwitz units are points of the unit sphere $S^3\subset\mathbb{H}_{\mathbb{B}}\cong\mathbb{R}^4$, and they are the vertices of a regular **$24$-cell**, the regular polytope of four-dimensional Euclidean space whose twenty-four cells are octahedra. The unit group is drawn as a figure.

**Theorem (the symmetry group).** The symmetry group of the $24$-cell is larger than the unit group: the signed permutations of the four coordinates form the Weyl group $B_4$ of order $384$, and the full symmetry group is the Weyl group $F_4$ of order $1152$, whereas the unit group is $2T$ of order $24$.

**Proof.** A symmetry of the $24$-cell permutes the vertices, so the symmetry group acts on the twenty-four units; the group generated by sign changes and coordinate permutations is the hyperoctahedral group $B_4$ of order $2^4\cdot 4!=384$, and it preserves the vertex set; the $24$-cell is the $F_4$ root polytope, whose full symmetry group is the Weyl group $F_4$ of order $1152$. Both contain the unit group $2T$, and both are strictly larger.

**Physical reading.** The two Weyl groups are the symmetry groups of the Hurwitz lattice and of the root system $F_4$, and they are symmetries of the **lattice**, not of the unit group. The distinction is the one the framework needs: the twenty-four units do not act as the $1152$ symmetries of $F_4$, because a unit acts by conjugation and conjugation gives only twelve distinct maps, all of them proper rotations. The figure is larger than the group that acts on it, and the two must not be conflated.

The unit group reaches the algebra through the rotations $\rho_v$ of *Biquaternion Rotations and Lorentz Transformations*, §*Reflections*, not through these symmetries: the map
$$
\rho_v(\tilde R) = -v\,\tilde R\,v^{-1}
$$
is a rotation of determinant $+1$ of the real slice and depends on $v$ only up to sign, so the twenty-four Hurwitz units give twelve distinct rotations. Together they generate the conjugation action of $2T$ on the real slice, of kernel $\{\pm e_0\}$, so that $2T/\{\pm e_0\}\cong A_4$ of order twelve, and adjoining the central negation, which is $\rho_{e_0}$, gives a group of order $24$. Read on the vector subspace $\mathrm{Vect}(\mathbb{B})\cong\mathbb{R}^3$ instead of on the real slice, the same map $\rho_{e_1}$ is the reflection in the hyperplane orthogonal to $e_1$, which generates the Weyl group $W(A_1)=\mathbb{Z}/2$ on that three-dimensional space.

**Physical reading.** The twelve proper rotations of the figure are the twelve distinct maps the twenty-four units give, so the discrete motions of the real slice are rotations and not reflections. This is the discrete counterpart of the continuous statement of *Biquaternion Rotations and Lorentz Transformations*, that a norm-one element acts on the Clifford vector subspace by a reflection only where orthogonality and anticommutation coincide, and elsewhere by a rotation.

## The McKay Correspondence

The five families of finite subgroups of $Sp(1)$ are the five families of simply laced Dynkin diagrams: the cyclic groups give the types $\tilde A$, the binary dihedral groups the types $\tilde D$, and the three binary polyhedral groups the exceptional types,
$$
2T \leftrightarrow \tilde E_6,\qquad 2O \leftrightarrow \tilde E_7,\qquad 2I \leftrightarrow \tilde E_8 .
$$
This is the **McKay correspondence**, and its content is that the Platonic solids, their binary preimages in the unit sphere and the exceptional simple Lie algebras are one subject. The Clifford reading of the algebra that underlies the correspondence is *The Clifford Structure of the Biquaternion Algebra*.

## The Integral Biquaternions

The integral biquaternions are the order $\mathbb{Z}[i]\otimes_{\mathbb{Z}}\mathcal{L}'$, the biquaternions with Gaussian-integer coordinates. Its group of units is **infinite**, and the reason is the nilpotent directions. A pure biquaternion $P$ with $N(P)=0$ satisfies $P^2=-N(P)e_0=0$, so it is nilpotent, and for such a $P$ the element $e_0+P$ is a unit with inverse $e_0-P$ and powers
$$
(e_0+P)^n=e_0+nP ,
$$
so the unit group contains an infinite cyclic subgroup generated along a nilpotent direction. Such a direction exists integrally, for instance $P=e_1+ie_2$, which is null and has Gaussian-integer coefficients.

**Physical reading.** The real orders have finite unit groups; the complex order does not. The difference is the light cone: nilpotent directions are null, and a null direction generates a translation-like one-parameter group without bound. On the material sector, where the four-position is $\tilde{Q}=ict\,e_0+\mathbf{x}$, the null condition is the light cone $c^2t^2=\mathbf{x}^2$: the integral null element $P=e_1+ie_2$ lies on the complex null cone and is the nilpotent direction that generates the infinite cyclic subgroup, while the finite unit groups sit in the real sector $\mathbb{H}_{\mathbb{B}}$, where the norm is definite and no null direction exists. In physics terms the infinite unit group is the algebraic statement that the light cone is present, and the finite unit groups are the groups of the massive, non-null sector.

## Summary

The quaternion orders inside the biquaternion algebra are the Lipschitz order $\mathcal{L}$ and the Hurwitz order $\mathcal{L}'$, the second containing the first with index two and maximal. Their groups of units are the quaternion group of order eight and the binary tetrahedral group of order twenty-four; the unit-group index is three, though the lattice index is two.

The unit sphere $Sp(1)=S^3$ has for finite subgroups the twofold preimages of the finite rotation groups of the plane and the three Platonic figures: the cyclic groups, the binary dihedral groups and the binary polyhedral groups $2T$, $2O$, $2I$ of orders twenty-four, forty-eight and one hundred twenty. The twenty-four Hurwitz units are the vertices of the regular $24$-cell in $\mathbb{H}_{\mathbb{B}}\cong\mathbb{R}^4$, whose symmetry group is the Weyl group $F_4$ of order $1152$, containing the hyperoctahedral $B_4$ of order $384$; both are strictly larger than the unit group $2T$. The units act on the real slice by the rotations $\rho_v(\tilde R)=-v\tilde Rv^{-1}$, of determinant $+1$, and the twenty-four units give twelve distinct rotations generating a group of order $24$ with $2T/\{\pm e_0\}\cong A_4$. The five families of finite subgroups are the five families of simply laced Dynkin diagrams, the McKay correspondence. Physically the finite unit groups are the spin point groups of the material sector — the double covers of the crystallographic point groups — and the figure the twenty-four units draw is the discrete symmetry of that sector.

The integral biquaternions over the Gaussian integers have an infinite group of units, generated along a nilpotent direction, so the finite unit groups are the real ones.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{L}=\mathbb{Z}e_0\oplus\cdots\oplus\mathbb{Z}e_3$ | Lipschitz order; index $2$, not maximal |
| $\mathcal{L}'=\mathcal{L}\oplus\mathbb{Z}\omega$ | Hurwitz order; maximal order of $\mathbb{H}$ |
| $\omega=\tfrac12(e_0+e_1+e_2+e_3)$ | Half-integral Hurwitz element |
| $\mathcal{L}^{\times}\cong Q_8$ | Lipschitz units, order $8$ |
| $(\mathcal{L}')^{\times}\cong 2T$ | Hurwitz units, order $24$ |
| $2T,2O,2I$ | Binary polyhedral groups of orders $24$, $48$, $120$ |
| $Sp(1)=S^3$ | Unit quaternions; the unit sphere; finite subgroups cyclic, binary dihedral, binary polyhedral |
| $Sp(1)/\{\pm e_0\}\cong SO(3)$ | Rotation quotient; the rotation group of Euclidean three-space |
| $T,O,I$ | Rotation groups of the tetrahedron, octahedron, icosahedron; orders $12,24,60$ |
| $24$-cell | Regular polytope of $\mathbb{H}_{\mathbb{B}}\cong\mathbb{R}^4$ with the $24$ Hurwitz units as vertices |
| $B_4$, $F_4$ | Weyl groups of orders $384$ and $1152$; symmetries of the $24$-cell and the lattice |
| $\rho_v(\tilde R)=-v\tilde Rv^{-1}$ | Rotation of the real slice defined by a unit $v$; determinant $+1$; the $24$ units give twelve distinct maps |
| $2T/\{\pm e_0\}\cong A_4$ | Conjugation action of the binary tetrahedral group on the real slice |
| $\tilde A,\tilde D,\tilde E_{6,7,8}$ | Simply laced Dynkin types of the five families; the McKay correspondence |
| $\mathbb{Z}[i]\otimes\mathcal{L}'$ | Integral biquaternions; infinite unit group |
| $n=e_1+ie_2$, $n^2=0$ | Nilpotent generator of the unipotent family |
| $e_0+kn$, $N=1$ | Unipotent family of norm-one units, $k\in\mathbb{Z}$ |
| $\mathbb{H}_{\mathbb{B}}$ | Real sector, the slice $ict=0$; home of the orders and their finite unit groups |
| $c^2t^2=\mathbf{x}^2$ | Light cone of the material sector; the null condition $N(\tilde{Q})=0$ there |

## Further Reading

- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A. K. Peters, 2003), for the Lipschitz and Hurwitz orders, their unit groups and the $24$-cell.
- John H. Conway and Neil J. A. Sloane, *Sphere Packings, Lattices and Groups* (Springer, 3rd ed. 1999), for the $D_4$ and $F_4$ lattices and the Weyl groups, and for the distinction between the lattice symmetry group and the unit group.
- H. S. M. Coxeter, *Regular Polytopes* (Dover, 3rd ed. 1973), for the $24$-cell and the finite reflection groups.
- Harold S. M. Coxeter and William O. J. Moser, *Generators and Relations for Discrete Groups* (Springer, 4th ed. 1980), for the finite rotation groups and their binary preimages.
- John McKay, *Graphs, singularities and finite groups* (Proceedings of Symposia in Pure Mathematics 37, 1980), for the correspondence between the finite subgroups of $SU(2)$ and the simply laced root systems.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for orders in a quaternion algebra and maximality.
