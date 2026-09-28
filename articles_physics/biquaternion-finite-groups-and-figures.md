
# __Biquaternion Finite Groups and Figures__

## Introduction

The real slice of the biquaternion algebra carries the discrete face of the theory: the finite groups of unit quaternions, and the figures they determine in $\mathbb{H}_{\mathbb{B}}\cong\mathbb{R}^4$. This article reads those groups and those figures — the regular $24$-cell, the symmetry groups $F_4$ and $B_4$ of its lattice, the twofold cover $Sp(1)\to SO(3)$ that produces the finite rotation groups, and the realisation of the units as rotations of the algebra.

The abstract unit groups — the quaternion group $Q_8$ and the binary tetrahedral group $2T$ inside the Lipschitz and Hurwitz orders, and the finite subgroups of the unit sphere — are *Biquaternion Orders and Finite Groups of Units*, which supplies the groups; the present article supplies the figures and the discrete motions. The lattice theory and the behaviour of the product and the bracket on the subspaces are *Relations Between Subspaces*; the Clifford reading of the algebra is *The Clifford Structure of the Biquaternion Algebra*; the continuous motions are *Biquaternion Rotations and Lorentz Transformations*. Those results are cited, not re-derived.

Physically these are the crystallographic figures of the material sector. The finite unit groups are the point groups the discrete configurations admit; the $24$-cell is the figure the Hurwitz units draw in the real slice; and the doubling of the preimage is the spin double cover, so a finite unit group is a group of spins and not only of positions. Because the finite groups are the *real* ones, a finite symmetry of a physical configuration is a symmetry of the material sector and not of the informational one.

**Conventions.** The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$ and central scalar imaginary $i$. The quaternion subspace $\mathbb{H}_{\mathbb{B}}=\mathbb{R}\{e_0,e_1,e_2,e_3\}$ is the real slice, on which the norm is the positive definite form $N(q)=\sum_\mu q_\mu^2$. The unit quaternions are $Sp(1)=\{q\in\mathbb{H}_{\mathbb{B}}:N(q)=1\}=S^3$. The material sector is $\mathbb{M}_-$ (*The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*).

---

## The Unit Sphere and the Rotation Quotient

The unit quaternions form the unit sphere
$$
Sp(1)=S^3=\{q\in\mathbb{H}_{\mathbb{B}}:N(q)=1\},
$$
a compact, connected and simply connected group of real dimension three, and the group of units of the real slice. Its centre is $\{\pm e_0\}$.

**The rotation quotient.** The element $q=\cos\theta\,e_0+\sin\theta\,\hat{n}$, with $\hat{n}$ a real unit vector part, acts on the real vector part by conjugation, and it acts as the rotation about the axis $\hat{n}$ through the angle $2\theta$. The elements $q$ and $-q$ define the same map, so the quotient by the centre is the rotation group,
$$
Sp(1)/\{\pm e_0\}\cong SO(3),
$$
and $Sp(1)$ is a twofold cover of $SO(3)$. The kernel of the quotient is the centre: the unit quaternion returns to $e_0$ after $2\pi$, while the rotation it performs returns to the identity after $\pi$, which is the doubling of the angle.

Two consequences organise the rest of the article. A finite rotation group is the one that preserves a figure, so the figures of the three-dimensional space classify them; and the cover is twofold, so the finite subgroups of $Sp(1)$ are exactly the twofold preimages of the finite rotation groups.

**Physical reading.** The unit sphere is the group of the spatial rotations of the material sector, and the twofold cover is the same doubling that the rotor of *Biquaternion Rotations and Lorentz Transformations* carries: a full turn of the figure is a half-turn of the quaternion. This is why the discrete symmetries of a material configuration are read on $Sp(1)$ and not on $SO(3)$: the extra sign is what a spinor carries and a position does not.

## The Finite Rotation Groups and Their Preimages

The finite subgroups of $SO(3)$ are the rotation groups of the plane and the three Platonic figures: the cyclic groups, the rotation groups of a regular pyramid; the dihedral groups, the rotation groups of a regular prism; and the three **polyhedral** groups
$$
T\ (12),\qquad O\ (24),\qquad I\ (60),
$$
the rotation groups of the tetrahedron, the octahedron and the icosahedron.

**Theorem.** The finite subgroups of $Sp(1)$ are the twofold preimages of these: the cyclic groups, the **binary dihedral** groups, and the three **binary polyhedral** groups
$$
2T\ (24),\qquad 2O\ (48),\qquad 2I\ (120),
$$
the binary tetrahedral, octahedral and icosahedral groups.

**Proof.** Let $\Gamma\subset Sp(1)$ be finite. Its image under the quotient is a finite subgroup $\bar\Gamma\subset SO(3)$, and the cover being twofold, $|\Gamma|=2|\bar\Gamma|$; conversely the preimage of a finite subgroup of $SO(3)$ is finite, of twice the order. The preimage of a cyclic group of order $n$ is cyclic of order $2n$, since the preimage of a cyclic group is cyclic; the preimage of a dihedral group of order $2n$ is a **binary dihedral** group of order $4n$; and the preimages of the three polyhedral groups of orders twelve, twenty-four and sixty are $2T$, $2O$ and $2I$, of orders twenty-four, forty-eight and one hundred twenty. $\square$

**Physical reading.** The binary polyhedral groups are the **spin point groups**: they are the double covers of the crystallographic point groups, and the doubling is the spin double cover, so a finite unit group is a group of spins and not only of positions. The appearance of the icosahedral case is the algebraic origin of the icosahedral symmetry in the framework's crystallography.

The binary tetrahedral group is not only a figure: it is realised arithmetically, as the group of units of the Hurwitz order in *Biquaternion Orders and Finite Groups of Units*. The other two are figures of the unit sphere without an integral model of the same kind there.

## The 24-Cell and the Hurwitz Units

The twenty-four Hurwitz units of *Biquaternion Orders and Finite Groups of Units* are points of the unit sphere $S^3\subset\mathbb{H}_{\mathbb{B}}\cong\mathbb{R}^4$. They are the vertices of a **regular $24$-cell**, the regular polytope of four-dimensional Euclidean space whose twenty-four cells are octahedra. The unit group is drawn as a figure.

**Theorem (the symmetry group).** The symmetry group of the $24$-cell is larger than the unit group: the signed permutations of the four coordinates form the Weyl group $B_4$ of order $384$, and the full symmetry group is the Weyl group $F_4$ of order $1152$, whereas the unit group is $2T$ of order $24$.

**Proof.** A symmetry of the $24$-cell permutes the vertices, so the symmetry group acts on the twenty-four units; the group generated by sign changes and coordinate permutations is the hyperoctahedral group $B_4$ of order $2^4\cdot 4!=384$, and it preserves the vertex set, and the $24$-cell is the $F_4$ root polytope, whose full symmetry group is the Weyl group $F_4$ of order $1152$. Both contain the unit group $2T$, and both are strictly larger. $\square$

**Physical reading.** The two Weyl groups are the symmetry groups of the Hurwitz lattice and of the root system $F_4$, and they are symmetries of the *lattice*, not of the unit group. The correction is the one the framework needs: the twenty-four units do not act as the $1152$ symmetries of $F_4$, because a unit acts by conjugation and conjugation gives only twelve distinct maps, all of them proper rotations. The figure is larger than the group that acts on it, and the two must not be conflated. The unit group reaches the algebra through the maps $\rho_v$ below, not through these symmetries.

## The Units as Rotations of the Algebra

The units of the real slice act on the algebra by conjugation. For a unit $v$ define
$$
\rho_v(x) = -v\,x\,v^{-1}.
$$

**Theorem.** On the real slice, where the norm is definite, $\rho_v$ is an isometry of determinant $+1$; it depends only on the class of $v$ up to sign; and the twenty-four Hurwitz units give twelve distinct maps, which together generate a group of order $24$, namely the conjugation action of $2T$ on the real slice.

**Proof.** The map $\rho_v$ is the composition of the conjugation $x\mapsto vxv^{-1}$, an algebra automorphism, with the negation $x\mapsto-x$, which is central; conjugation by a unit of the real slice preserves the norm, and on the four-dimensional real slice its determinant is $+1$, as is that of the negation in even dimension, so $\rho_v$ is a rotation. Substituting $-v$ for $v$ leaves $\rho_v$ unchanged, since the two central signs cancel, so the twenty-four units give at most twelve maps; and two units give the same map exactly when they differ by a central element of $Sp(1)$, that central element being $\pm e_0$, so the twelve pairs $\{\pm v\}$ give twelve distinct maps. The conjugation action of $2T$ on the real slice has kernel $\{\pm e_0\}$, so it is $2T/\{\pm e_0\}\cong A_4$ of order twelve, and adjoining the central negation, which is $\rho_{e_0}$, gives a group of order $24$. $\square$

**Physical reading.** The twelve proper rotations of the figure are the twelve distinct maps the twenty-four units give, so the discrete motions of the real slice are rotations and not reflections. This is the discrete counterpart of the continuous statement of *Biquaternion Rotations and Lorentz Transformations*, that a norm-one element acts on the Clifford vector subspace by a reflection only where orthogonality and anticommutation coincide, and elsewhere by a rotation.

**Remark (one generator).** At one generator the mechanism is visible. On the line $\mathbb{R}e_1$ the map $\rho_{e_1}$ acts as $-1$, and on the orthogonal complement as the identity, so it is the reflection in the hyperplane orthogonal to $e_1$. The reflection it supplies generates the Weyl group $W(A_1)=\mathbb{Z}/2$ on a one-dimensional Clifford subspace.

## The McKay Correspondence

The five families of finite subgroups of $Sp(1)$ are the five families of simply laced Dynkin diagrams: the cyclic groups give the types $\tilde A$, the binary dihedral groups the types $\tilde D$, and the three binary polyhedral groups the exceptional types,
$$
2T \leftrightarrow \tilde E_6,\qquad 2O \leftrightarrow \tilde E_7,\qquad 2I \leftrightarrow \tilde E_8 .
$$
This is the **McKay correspondence**, and its figure-theoretic content is that the Platonic solids, their binary preimages in the unit sphere and the exceptional simple Lie algebras are one subject. The Clifford reading of the algebra that underlies the correspondence is *The Clifford Structure of the Biquaternion Algebra*.

## Summary

The unit quaternions form the sphere $Sp(1)=S^3$, whose centre is $\{\pm e_0\}$ and whose quotient $Sp(1)/\{\pm e_0\}\cong SO(3)$ is the rotation group of the Euclidean three-space; the cover is twofold, and the angle of the rotation is twice the angle of the quaternion. The finite subgroups of $Sp(1)$ are the twofold preimages of the finite rotation groups of the plane and the three Platonic figures: the cyclic groups, the binary dihedral groups, and the binary polyhedral groups $2T$, $2O$, $2I$ of orders $24$, $48$ and $120$.

The twenty-four Hurwitz units are the vertices of the regular $24$-cell in $\mathbb{H}_{\mathbb{B}}\cong\mathbb{R}^4$; its symmetry group is $F_4$ of order $1152$, containing the hyperoctahedral $B_4$ of order $384$, and both are strictly larger than the unit group $2T$. The units act on the algebra by the maps $\rho_v(x)=-vxv^{-1}$, of determinant $+1$, and the twenty-four units give twelve maps generating a group of order $24$. The five families of finite subgroups are the five families of simply laced Dynkin diagrams, the McKay correspondence.

Physically these are the discrete figures of the material sector: the spin point groups, the $24$-cell and its lattice symmetries, and the discrete rotations of the real slice.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $Sp(1)=S^3=\{N=1\}$ | Unit quaternions; compact, connected, simply connected; the unit sphere of the real slice |
| $\{\pm e_0\}$ | Centre of $Sp(1)$; kernel of the rotation quotient |
| $Sp(1)/\{\pm e_0\}\cong SO(3)$ | Rotation quotient; the rotation group of the Euclidean three-space |
| $T,O,I$ | Rotation groups of the tetrahedron, octahedron, icosahedron; orders $12,24,60$ |
| $2T,2O,2I$ | Binary tetrahedral, octahedral, icosahedral groups; orders $24,48,120$ |
| $24$-cell | Regular polytope of $\mathbb{H}_{\mathbb{B}}\cong\mathbb{R}^4$ with the $24$ Hurwitz units as vertices |
| $B_4$, $F_4$ | Weyl groups of orders $384$ and $1152$; symmetries of the $24$-cell and the lattice |
| $\rho_v(x)=-vxv^{-1}$ | Rotation of the real slice defined by a unit $v$; determinant $+1$ |
| $2T/\{\pm e_0\}\cong A_4$ | Conjugation action of the binary tetrahedral group on the real slice |
| $\tilde A,\tilde D,\tilde E_{6,7,8}$ | Simply laced Dynkin types of the five families; the McKay correspondence |

## Further Reading

- H. S. M. Coxeter, *Regular Polytopes* (Dover, 3rd ed. 1973), for the $24$-cell, its symmetry group and the regular polytopes of four-dimensional space.
- Harold S. M. Coxeter and William O. J. Moser, *Generators and Relations for Discrete Groups* (Springer, 4th ed. 1980), for the finite rotation groups and their binary preimages.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A. K. Peters, 2003), for the finite groups of unit quaternions and the $24$-cell.
- John McKay, *Graphs, singularities and finite groups* (Proceedings of Symposia in Pure Mathematics 37, 1980), for the correspondence between the finite subgroups of $SU(2)$ and the simply laced root systems.
