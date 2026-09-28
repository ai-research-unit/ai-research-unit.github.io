
# __Biquaternion Orders and Finite Groups of Units__

## Introduction

The biquaternion algebra carries integral structures, and the groups of units of those structures are the finite groups attached to the algebra. The real slice $\mathbb{H}_{\mathbb{B}}\cong\mathbb{H}$ contains the classical quaternion orders — the Lipschitz order and the Hurwitz order — whose groups of units are the quaternion group of order eight and the binary tetrahedral group of order twenty-four, the second being the vertex set of the regular $24$-cell. The unit sphere of the real slice has for finite subgroups the cyclic groups, the binary dihedral groups and the three binary polyhedral groups of orders $24$, $48$ and $120$. The complex order, the integral biquaternions, behaves differently: its group of units is infinite, generated along a nilpotent direction, so the finite unit groups are the real ones.

This article is the integral and finite-group entry of the Algebra slot. The lattice-theoretic treatment of the quaternion orders — rank, index, covolume, duality, base change — is *Lattices and the Quaternion Lattice*; the order theory of the quaternion algebra over $\mathbb{Q}$, with maximality and the arithmetic of the norm, is *Division Algebras*; the Clifford lift of the finite reflection groups and the McKay correspondence are *Reflection Groups and Clifford Algebras* and *Root Systems and Classification*. Those results are cited, not re-derived, and the present article owns their biquaternion statement: the orders inside $\mathbb{B}$, their finite unit groups, and the infinite unit group of the complex order.

**Conventions.** The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$, central scalar imaginary $i$, products $e_1e_2=e_3$, $e_2e_3=e_1$, $e_3e_1=e_2$ and $e_k^2=-e_0$, so that $e_1e_2e_3=-e_0$. The quaternion subspace $\mathbb{H}_{\mathbb{B}}=\mathbb{R}\{e_0,e_1,e_2,e_3\}$ is the real slice (*Biquaternion Quaternion Subspace*). The norm is $N(\tilde{Q})=\sum_\mu Q_\mu^2$, and on the real slice it is the positive definite form $\sum_\mu q_\mu^2$.

---

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

**Proof.** The change of basis from $(e_0,e_1,e_2,e_3)$ to $(\omega,e_1,e_2,e_3)$ has determinant $\tfrac12$, so the index is $|\det|^{-1}=2$; equivalently $\mathcal{L}'/\mathcal{L}\cong\mathbb{Z}/2$, of prime order. Maximality of $\mathcal{L}'$ is the classical statement that the Hurwitz order is a maximal order in the rational quaternion algebra, and the half-integral element of $\mathcal{L}'\setminus\mathcal{L}$ witnesses that $\mathcal{L}$ is not maximal (*Division Algebras*); the module-level computations of index and covolume are in *Lattices and the Quaternion Lattice*. $\square$

**Remark.** The orders are orders in the *real* quaternion algebra, inside the quaternion subspace of $\mathbb{B}$. The biquaternion algebra contains them and their complexification, and it is the complexification that changes the nature of the unit group, below.

## The Groups of Units

**Theorem.** The group of units of the Lipschitz order is the eight-element quaternion group,
$$
\mathcal{L}^{\times}=\{\pm e_0,\pm e_1,\pm e_2,\pm e_3\}\cong Q_8 ,
$$
and the group of units of the Hurwitz order is the twenty-four-element binary tetrahedral group,
$$
(\mathcal{L}')^{\times}=\mathcal{L}^{\times}\cup\{\tfrac12(\pm e_0\pm e_1\pm e_2\pm e_3)\}\cong 2T .
$$

**Proof.** On real quaternion coordinates the norm is $N(x)=\sum_\mu q_\mu^2\geq0$, an integer for $x$ in either order; the inverse is $x^{-1}=x^*/N(x)$ with $x^*$ the quaternion conjugate, and $x^*$ lies in the order whenever $x$ does, so $x$ is a unit exactly when $N(x)=1$. The norm-one elements with integer coordinates are the eight signed units $\pm e_\mu$, and with half-integer coordinates they are those together with the sixteen elements $\tfrac12(\pm e_0\pm e_1\pm e_2\pm e_3)$, of norm one. The resulting groups are closed under multiplication, have the stated orders, and are the quaternion group and the binary tetrahedral group respectively. $\square$

**Remark (the two indices).** The lattices have index $2$, but the unit groups have index $24/8=3$: the Lipschitz units are a proper subgroup of index three in the Hurwitz units, so the two notions of index do not agree.

**Remark (the $24$-cell).** The twenty-four Hurwitz units are the vertices of the regular $24$-cell in $\mathbb{H}_{\mathbb{B}}\cong\mathbb{R}^4$. Its full symmetry group is the Weyl group $F_4$ of order $1152$, and the signed permutations of the four coordinates give the Weyl group $B_4$ of order $384$, but these are symmetries of the lattice and are not the unit group (*Root Systems and Classification*, *Lattices and the Quaternion Lattice*). The unit group reaches the lattice only through the maps $\rho_v$ of the rotations article: the twenty-four Hurwitz units give twelve distinct maps $\rho_v(x)=-vxv^{-1}$, each of determinant $+1$ on the algebra and therefore a rotation rather than a reflection, and together they generate the conjugation action of $2T$, namely $2T/\{\pm1\}\cong A_4$ together with the antipodal map, of order $24$ — the unit group is not $F_4$. The root system $A_1$ is present already at one generator: on the line $\mathbb{R}e_1$ the map $\rho_{e_1}$ acts as $-1$ and on the orthogonal complement as the identity, so the Weyl group $W(A_1)=\mathbb{Z}/2$ is realised on a one-dimensional Clifford subspace.

## The Finite Subgroups of the Unit Sphere

**Theorem.** The finite subgroups of the unit sphere $Sp(1)=S^3\subset\mathbb{H}_{\mathbb{B}}$ are the cyclic groups, the binary dihedral groups, and the three binary polyhedral groups
$$
2T\ (24),\qquad 2O\ (48),\qquad 2I\ (120),
$$
the binary tetrahedral, octahedral and icosahedral groups.

**Proof.** The unit quaternions form $Sp(1)\cong SU(2)$, whose centre is $\{\pm e_0\}$; passing to the quotient $SO(3)$ identifies the finite subgroups of $Sp(1)$ with the twofold preimages of the finite rotation groups of $\mathbb{R}^3$, which are the cyclic, dihedral and polyhedral groups. The preimage of a cyclic group is cyclic, of a dihedral group binary dihedral, and of the three polyhedral groups are $2T$, $2O$, $2I$, of twice the orders $12$, $24$ and $60$. The Hurwitz order realises $2T$ integrally, as above. $\square$

**Remark.** The correspondence between these three groups and the simply laced root systems of type $A$, $D$, $E$ is the McKay correspondence, and the Clifford realisation of the same groups as the even parts of the lifts of the finite reflection groups is *Reflection Groups and Clifford Algebras*; the classification of the reflection groups is *Root Systems and Classification*. The binary dihedral groups are the preimages of the dihedral rotation groups, of order four times the dihedral order.

## The Integral Biquaternions

**Definition.** The **integral biquaternions** are the elements whose coefficients lie in the Gaussian integers,
$$
\Lambda=\mathbb{Z}[i]e_0\oplus\mathbb{Z}[i]e_1\oplus\mathbb{Z}[i]e_2\oplus\mathbb{Z}[i]e_3
=\mathcal{L}\otimes_{\mathbb{Z}}\mathbb{Z}[i].
$$
They form an order in $\mathbb{B}$ over $\mathbb{Z}[i]$, and the larger $\Lambda'=\mathcal{L}'\otimes_{\mathbb{Z}}\mathbb{Z}[i]$ contains it with index two.

**Theorem.** The group of units of the integral biquaternions is infinite.

**Proof.** The element $n=e_1+ie_2$ is nilpotent, $n^2=(e_1)^2+i(e_1e_2+e_2e_1)+i^2(e_2)^2=(-e_0)+0+(-1)(-e_0)=0$, so for every integer $k$ the binomial expansion truncates and
$$
(e_0+n)^k=e_0+kn .
$$
Each of these elements has norm $N(e_0+kn)=1+k^2+(ik)^2=1$, since the coefficients of $e_0+kn$ are $Q_0=1$, $Q_1=k$, $Q_2=ik$, $Q_3=0$; a norm-one element has inverse its conjugate and so is a unit. Hence $\Lambda^{\times}$ contains the infinite family $\{e_0+kn:k\in\mathbb{Z}\}$. $\square$

**Remark.** The finite unit groups are therefore those of the *real* order, not of the complex one. The presence of nilpotent directions in the complex order is the same phenomenon as the presence of zero divisors in the algebra at large: $\mathbb{B}\cong M_2(\mathbb{C})$ is not a division algebra, and its integral order inherits unipotent units.

## Summary

The quaternion orders inside the biquaternion algebra are the Lipschitz order $\mathcal{L}$ and the Hurwitz order $\mathcal{L}'$, the second containing the first with index two and maximal. Their groups of units are the quaternion group of order eight and the binary tetrahedral group of order twenty-four, the latter the vertex set of the regular $24$-cell; the unit-group index is three, though the lattice index is two. The finite subgroups of the unit sphere $Sp(1)=SU(2)$ are the cyclic groups, the binary dihedral groups and the binary polyhedral groups $2T$, $2O$, $2I$ of orders twenty-four, forty-eight and one hundred twenty.

The integral biquaternions, with coefficients in the Gaussian integers, form an order in $\mathbb{B}$ whose group of units is infinite: the nilpotent element $e_1+ie_2$ generates the unipotent family $e_0+k(e_1+ie_2)$ of norm one. The finite unit groups of the theory are thus the groups of the real quaternion orders.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{L}=\mathbb{Z}e_0\oplus\cdots\oplus\mathbb{Z}e_3$ | Lipschitz order; index $2$, not maximal |
| $\mathcal{L}'=\mathcal{L}\oplus\mathbb{Z}\omega$ | Hurwitz order; maximal order of $\mathbb{H}$ |
| $\omega=\tfrac12(e_0+e_1+e_2+e_3)$ | Half-integral generator of $\mathcal{L}'$ |
| $\mathcal{L}^{\times}\cong Q_8$ | Lipschitz units, order $8$ |
| $(\mathcal{L}')^{\times}\cong 2T$ | Hurwitz units, order $24$; vertices of the $24$-cell |
| $2T,2O,2I$ | Binary tetrahedral, octahedral, icosahedral groups; orders $24,48,120$ |
| $Sp(1)=S^3$ | Unit quaternions; $SU(2)$; finite subgroups cyclic, binary dihedral, binary polyhedral |
| $\Lambda=\mathcal{L}\otimes_{\mathbb{Z}}\mathbb{Z}[i]$ | Integral biquaternions; infinite group of units |
| $n=e_1+ie_2$, $n^2=0$ | Nilpotent generator of the unipotent family |
| $e_0+kn$, $N=1$ | Unipotent family of norm-one units, $k\in\mathbb{Z}$ |

## Further Reading

- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A. K. Peters, 2003), for the finite groups of unit quaternions, the $24$-cell and the quaternion orders.
- John H. Conway and Neil J. A. Sloane, *Sphere Packings, Lattices and Groups* (Springer, 3rd ed. 1999), for the integral quaternion orders, their unit groups and the root systems realised in them.
- Marie-France Vignéras, *Arithmétique des algèbres de quaternions* (Springer Lecture Notes in Mathematics 800, 1980), for the order theory of the quaternion algebra, maximality and the arithmetic of the norm.
- John McKay, *Graphs, singularities and finite groups* (Proceedings of Symposia in Pure Mathematics 37, 1980), for the correspondence between the finite subgroups of $SU(2)$ and the simply laced root systems.
