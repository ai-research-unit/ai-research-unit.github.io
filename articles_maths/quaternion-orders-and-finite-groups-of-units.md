# __Quaternion Orders and Finite Groups of Units__

## Introduction

The quaternion algebra carries a norm with integer values on certain lattices, and the lattices that are also rings are the **orders**. The two classical orders, the Lipschitz and the Hurwitz orders, have finitely many units, and the unit groups that occur are exactly the finite subgroups of the unit sphere. This article states the orders, their unit groups, the classification of the finite subgroups of the sphere, and the McKay correspondence; the topological group of units of the whole algebra is the article before it, and the finite groups are read here once.

## The Quaternion Orders

**Definition (order).** An **order** of $\mathbb{H}$ is a subring $\mathcal O$ that is a lattice, that is a finitely generated abelian group spanning $\mathbb{H}$ over $\mathbb{R}$, and on which the norm is integral.

**Proposition (the Lipschitz order).** The **Lipschitz order**

$$
\mathcal L=\mathbb{Z}+\mathbb{Z}i+\mathbb{Z}j+\mathbb{Z}k
$$

is a subring of $\mathbb{H}$, a lattice of rank $4$, and the norm of its elements is a nonnegative integer.

*Proof.* The product of two integral quaternions has integral coefficients, so $\mathcal L$ is a subring; the four elements are a $\mathbb{Z}$-basis, so the lattice has rank $4$; the norm of an element with integer coordinates is a sum of four squares, an integer.

**Proposition (the Hurwitz order).** Put $\omega=\tfrac12(1+i+j+k)$. Then $\omega^{2}=\omega-1$, so $\omega$ is an element of order six, and the **Hurwitz order**

$$
\mathcal H=\mathbb{Z}+\mathbb{Z}i+\mathbb{Z}j+\mathbb{Z}\omega
$$

is a subring of $\mathbb{H}$, a lattice of rank $4$, with $\mathcal L\subseteq\mathcal H$ of index $2$; its norm is again integral, and it is a maximal order.

## The Groups of Units

**Theorem (the two unit groups).** The units of the Lipschitz order are the eight elements

$$ \boxed{\; \mathcal L^\times=\{\pm1,\pm i,\pm j,\pm k\}=Q_8 \;} ,$$

the quaternion group of order eight; the units of the Hurwitz order are the twenty-four elements

$$ \boxed{\; \mathcal H^\times=\{\pm1,\pm i,\pm j,\pm k\}\cup\bigl\{\tfrac12(\pm1\pm i\pm j\pm k)\bigr\}=2T \;} ,$$

the binary tetrahedral group of order twenty-four.

*Proof.* An element of an order is a unit exactly when its norm is $1$, the inverse $\tilde q^{\natural}/\langle\tilde q\rangle_{\natural}$ then lying in the order; the elements of norm one in $\mathcal L$ are the eight signed units, forming $Q_8$; the elements of norm one in $\mathcal H$ are those eight together with the sixteen half-integer elements $\tfrac12(\pm1\pm i\pm j\pm k)$, whose norm is $\tfrac14(1+1+1+1)=1$; the set of twenty-four is closed under the product, so it is a group.

**Remark (the unit groups are finite, against the group of units of the algebra).** The group of units of the whole algebra, $\mathbb{H}^\times=\mathbb{H}\setminus\{0\}$, is infinite and is *The Quaternion Unit Group as a Topological Group*, above this article in this category; the orders cut it down to the finite groups of the theorem. The two are different objects, and the group of units of the algebra is stated once, there.

## The Finite Subgroups of the Unit Sphere

**Theorem (the classification).** Every finite subgroup of the unit sphere $S^3=Sp(1)$ is one of

- the cyclic group $C_n$ of order $n$, the rotations about one axis;
- the binary dihedral group $2D_n$ of order $4n$, the preimage of the dihedral group of the plane;
- the binary tetrahedral group $2T$ of order $24$;
- the binary octahedral group $2O$ of order $48$;
- the binary icosahedral group $2I$ of order $120$.

Each is the preimage of a finite rotation group of three-dimensional space; the covering is two-to-one exactly when the group contains the centre $\{\pm e_t\}$, which holds in every family except the cyclic groups of odd order.

The centre of $S^3$ is $\{\pm e_t\}$ by *The Quaternion Unit Group as a Topological Group*, and the cover of the rotation group is two-to-one exactly when $\pm e_t$ lies in the group.

| family | order | generators | rotation group |
|---|---|---|---|
| $C_n$ | $n$ | one element of order $n$ | cyclic $C_n$ |
| $2D_n$ | $4n$ | two elements | dihedral $D_n$ |
| $2T$ | $24$ | $\mathcal H^\times$ | tetrahedral $A_4$ |
| $2O$ | $48$ | $2T$ and one more | octahedral $S_4$ |
| $2I$ | $120$ | the binary icosahedral | icosahedral $A_5$ |

**Remark (the orders give the first two families).** The Lipschitz units $Q_8$ are the binary dihedral group $2D_2$ of order eight, and the Hurwitz units $2T$ are the binary tetrahedral group; the binary octahedral and binary icosahedral groups are finite subgroups of $S^3$ that are not the unit group of an order of the simple form above, and they are the remaining two Platonic cases.

## The McKay Correspondence

**Theorem (the correspondence).** The five families of the classification correspond to the five simply laced Dynkin diagrams:

| family | $C_n$ | $2D_n$ | $2T$ | $2O$ | $2I$ |
|---|---|---|---|---|---|
| diagram | $A_{{n-1}}^{(1)}$ | $D_{{n+2}}^{(1)}$ | $E_{6}^{(1)}$ | $E_{7}^{(1)}$ | $E_{8}^{(1)}$ |

the correspondence assigning to a finite subgroup the affine Dynkin diagram of the components of the representation of its double by the fundamental representation.

## Summary

The Lipschitz order $\mathcal L=\mathbb{Z}+\mathbb{Z}i+\mathbb{Z}j+\mathbb{Z}k$ is a lattice subring with integral norm and unit group the quaternion group $Q_8$ of order eight; the Hurwitz order $\mathcal H=\mathbb{Z}+\mathbb{Z}i+\mathbb{Z}j+\mathbb{Z}\omega$ with $\omega=\tfrac12(1+i+j+k)$, $\omega^{2}=\omega-1$, contains $\mathcal L$ with index two, is maximal, and has unit group the binary tetrahedral group $2T$ of order twenty-four. The finite subgroups of the unit sphere $S^3$ are the cyclic groups, the binary dihedral groups, and the binary tetrahedral, octahedral and icosahedral groups of orders $24$, $48$ and $120$; under the McKay correspondence they are the simply laced Dynkin diagrams.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathcal L=\mathbb{Z}+\mathbb{Z}i+\mathbb{Z}j+\mathbb{Z}k$ | the Lipschitz order |
| $\mathcal H=\mathbb{Z}+\mathbb{Z}i+\mathbb{Z}j+\mathbb{Z}\omega$ | the Hurwitz order, maximal, $[\mathcal H:\mathcal L]=2$ |
| $\omega=\tfrac12(1+i+j+k)$, $\omega^{2}=\omega-1$ | the order-six element of $\mathcal H$ |
| $Q_8$, $2T$ | the unit groups, of orders $8$ and $24$ |
| $C_n$, $2D_n$, $2T$, $2O$, $2I$ | the finite subgroups of $S^3$ |
| $A_{{n-1}}^{(1)}$, $D_{{n+2}}^{(1)}$, $E_{6}^{(1)}$, $E_{7}^{(1)}$, $E_{8}^{(1)}$ | the McKay diagrams |

## Further Reading

- [Norm and Invertibility in the Quaternion Algebra](norm-and-invertibility-in-the-quaternion-algebra.html), for the norm and the inverse
- [The Quaternion Unit Group as a Topological Group](the-quaternion-unit-group-as-a-topological-group.html), for the group of units of the algebra and the sphere
- [Quaternion Rotations and Reflections](quaternion-rotations-and-reflections.html), for the rotation groups of the quotients
