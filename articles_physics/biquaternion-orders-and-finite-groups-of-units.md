# __Biquaternion Orders and Finite Groups of Units__

## Introduction

The biquaternion algebra carries integral structures, and the groups of units of those structures are the finite groups attached to the algebra. The real slice $\mathbb{H}_{\mathbb{B}}\cong\mathbb{H}$ contains the classical quaternion orders — the Lipschitz order and the Hurwitz order — whose groups of units are the quaternion group of order eight and the binary tetrahedral group of order twenty-four. The unit sphere of the real slice has for finite subgroups the cyclic groups, the binary dihedral groups and the three binary polyhedral groups of orders $24$, $48$ and $120$. The complex order, the integral biquaternions, behaves differently: its group of units is infinite, generated along a nilpotent direction, so the finite unit groups are the real ones.

This article is the integral and finite-group entry of the Topology group. The unit criterion is the biquaternion norm, which is *Biquaternion Norm and Invertibility*, and the topology of the group of units is *The Biquaternion Unit Group as a Topological Group*. Those results are cited, not re-derived, and the present article owns the orders inside $\mathbb{B}$, their finite unit groups as abstract groups, and the infinite unit group of the complex order.

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

*Proof.* The change of basis from $(e_0,e_1,e_2,e_3)$ to $(\omega,e_1,e_2,e_3)$ has determinant $\tfrac12$, so the index is $|\det|^{-1}=2$; equivalently $\mathcal{L}'/\mathcal{L}\cong\mathbb{Z}/2$, of prime order. Maximality of $\mathcal{L}'$ is the classical statement that the Hurwitz order is a maximal order in the rational quaternion algebra, and the half-integral element of $\mathcal{L}'\setminus\mathcal{L}$ witnesses that $\mathcal{L}$ is not maximal. $\square$

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

**Proof.** On real quaternion coordinates the norm is $N(x)=\sum_\mu q_\mu^2\geq0$, an integer for $x$ in either order; the inverse is $x^{-1}=\bar{x}/N(x)$ with $\bar{x}$ the quaternion conjugate, and $\bar{x}$ lies in the order whenever $x$ does, so $x$ is a unit exactly when $N(x)=1$. The norm-one elements with integer coordinates are the eight signed units $\pm e_\mu$, and with half-integer coordinates they are those together with the sixteen elements $\tfrac12(\pm e_0\pm e_1\pm e_2\pm e_3)$, of norm one. The resulting groups are closed under multiplication, have the stated orders, and are the quaternion group and the binary tetrahedral group respectively. $\square$

**Remark (the two indices).** The lattices have index $2$, but the unit groups have index $24/8=3$: the Lipschitz units are a proper subgroup of index three in the Hurwitz units, so the two notions of index do not agree.

**Physical reading.** The finite unit groups are the **crystallographic point groups** the material sector admits: $Q_8$ is the smallest non-abelian one, and $2T$ is the next. They are the finite groups of symmetry of a discrete configuration of the material sector, and because they lie in the definite real slice no null direction enters them.

## The Finite Subgroups of the Unit Sphere

**Theorem.** The finite subgroups of the unit quaternions $Sp(1)=S^3$ are the cyclic groups, the binary dihedral groups, and the three binary polyhedral groups
$$
2T\ (24),\qquad 2O\ (48),\qquad 2I\ (120),
$$
the binary tetrahedral, octahedral and icosahedral groups.

The binary dihedral groups are the twofold preimages of the dihedral groups, of order four times the dihedral order, and the Hurwitz order realises $2T$ integrally, as above. The classification is the classical classification of the finite subgroups of the unit quaternions.

**Physical reading.** The binary polyhedral groups are the **spin point groups**: they are the double covers of the crystallographic point groups, and the doubling is the spin double cover, so a finite unit group is a group of spins and not only of positions. The orders $24$, $48$, $120$ are the orders of the binary tetrahedral, octahedral and icosahedral groups, and the appearance of the icosahedral case is the algebraic origin of the icosahedral symmetry in the framework's crystallography. Because the finite groups are the **real** ones, a finite symmetry of a physical configuration is a symmetry of the material sector and not of the informational one.

## The Integral Biquaternions

The integral biquaternions are the order $\mathbb{Z}[i]\otimes_{\mathbb{Z}}\mathcal{L}'$, the biquaternions with Gaussian-integer coordinates. Its group of units is **infinite**, and the reason is the nilpotent directions. A pure biquaternion $P$ with $N(P)=0$ satisfies $P^2=-N(P)e_0=0$, so it is nilpotent, and for such a $P$ the element $e_0+P$ is a unit with inverse $e_0-P$ and powers
$$
(e_0+P)^n=e_0+nP ,
$$
so the unit group contains an infinite cyclic subgroup generated along a nilpotent direction. Such a direction exists integrally, for instance $P=e_1+ie_2$, which is null and has Gaussian-integer coefficients.

**Physical reading.** The real orders have finite unit groups; the complex order does not. The difference is the light cone: nilpotent directions are null, and a null direction generates a translation-like one-parameter group without bound. On the material sector, where the four-position is $\tilde{Q}=ict\,e_0+\mathbf{x}$, the null condition is the light cone $c^2t^2=\mathbf{x}^2$: the integral null element $P=e_1+ie_2$ lies on the complex null cone and is the nilpotent direction that generates the infinite cyclic subgroup, while the finite unit groups sit in the real sector $\mathbb{H}_{\mathbb{B}}$, where the norm is definite and no null direction exists. In physics terms the infinite unit group is the algebraic statement that the light cone is present, and the finite unit groups are the groups of the massive, non-null sector.

## Summary

The quaternion orders inside the biquaternion algebra are the Lipschitz order $\mathcal{L}$ and the Hurwitz order $\mathcal{L}'$, the second containing the first with index two and maximal. Their groups of units are the quaternion group of order eight and the binary tetrahedral group of order twenty-four; the unit-group index is three, though the lattice index is two. The finite subgroups of the unit sphere $Sp(1)=S^3$ are the cyclic groups, the binary dihedral groups and the binary polyhedral groups $2T$, $2O$, $2I$ of orders twenty-four, forty-eight and one hundred twenty.

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
| $\mathbb{Z}[i]\otimes\mathcal{L}'$ | Integral biquaternions; infinite unit group |
| $n=e_1+ie_2$, $n^2=0$ | Nilpotent generator of the unipotent family |
| $e_0+kn$, $N=1$ | Unipotent family of norm-one units, $k\in\mathbb{Z}$ |
| $\mathbb{H}_{\mathbb{B}}$ | Real sector, the slice $ict=0$; home of the orders and their finite unit groups |
| $c^2t^2=\mathbf{x}^2$ | Light cone of the material sector; the null condition $N(\tilde{Q})=0$ there |

## Further Reading

- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A. K. Peters, 2003), for the Lipschitz and Hurwitz orders, their unit groups and the $24$-cell.
- John H. Conway and Neil J. A. Sloane, *Sphere Packings, Lattices and Groups* (Springer, 3rd ed. 1999), for the $D_4$ and $F_4$ lattices and the Weyl groups, and for the distinction between the lattice symmetry group and the unit group.
- H. S. M. Coxeter, *Regular Polytopes* (Dover, 3rd ed. 1973), for the $24$-cell and the finite reflection groups.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for orders in a quaternion algebra and maximality.
