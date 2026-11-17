# __The Two Halves and Their Topology__

## Introduction

**Each of the two halves is a real Euclidean space of dimension $n^{2}$, the splitting map is an isometry, and the interesting topology of the halves sits in the strata: the Hermitian half is cut by the inertia into $n+1$ open regions, the positive cone is convex and contractible, and the unitary half is not contractible because its determinant covers the circle.**

The article proves that the Hermitian and the anti-Hermitian matrices are real vector spaces of dimension $n^{2}$, closed in the matrix space and meeting only at zero, proves the Pythagorean identity for the splitting and the isometry of the splitting map, proves that the positive definite cone is convex hence contractible, proves that the sets of fixed inertia are open and that the determinant of a unitary matrix has modulus one. It assumes *The Two Halves as Orthogonal Complements* and *The Topology of $M_n(\mathbb{C})$*. It defers the fundamental group to *The Homotopy of $\mathrm{GL}_n(\mathbb{C})$ and of the Two Halves* and the metric geometry to *The Geometry of the Two Halves, and the Return of the Two-Sided Operators*.

## The Two Halves as Euclidean Spaces

**Each half is a real vector space of dimension $n^{2}$.** A Hermitian matrix is determined by its real diagonal and by the real and imaginary parts of its strict upper triangle, so

$$
\dim_{\mathbb{R}}\operatorname{Herm}_n=n+2\cdot\frac{n(n-1)}{2}=n^{2},
$$

and the same count holds for $\mathfrak{u}(n)$, since multiplication by $i$ carries one half onto the other. The computation confirms the count at $n=2,3,4$: $4,9,16$.

**Each half is closed in the matrix space.** A half is the fixed set of a linear involution, namely $A\mapsto A^{*}$ or $A\mapsto-A^{*}$, and the fixed set of a continuous map is closed; so

$$
\overline{\operatorname{Herm}_n}=\operatorname{Herm}_n,\qquad \overline{\mathfrak{u}(n)}=\mathfrak{u}(n).
$$

The computation confirms the closure at $n=3$ by taking limits of Hermitian matrices and checking the result is Hermitian, and it is the reason each half is a complete metric space in its own right.

**The two halves meet only at zero.** A matrix which is both Hermitian and anti-Hermitian satisfies $A=A^{*}=-A$, so

$$
\operatorname{Herm}_n\cap\mathfrak{u}(n)=\{0\},
$$

which was verified at $n=3$ by solving the two conditions. So the intersection is the apex, and the two halves are the two closed cones of *The Topology of $M_n(\mathbb{C})$*.

**The unit sphere of each half is a sphere.** The set

$$
\{H\in\operatorname{Herm}_n:\|H\|_{\mathrm{HS}}=1\}
$$

is the unit sphere of a real Euclidean space of dimension $n^{2}$, hence the sphere $S^{n^{2}-1}$, and the same holds in the anti-Hermitian half. The computation confirms the dimension at $n=2,3$ by counting the coordinates of a normalised Hermitian matrix, and it is the only non-contractible subset of a half which is not cut by a condition on the spectrum.

## The Splitting Map

**The splitting map is a linear homeomorphism.** The map

$$
\Phi:M_n(\mathbb{C})\to\operatorname{Herm}_n\oplus\mathfrak{u}(n),\qquad \Phi(A)=\Big(\tfrac12(A+A^{*}),\ \tfrac12(A-A^{*})\Big)
$$

is a linear bijection with inverse $(H,K)\mapsto H+K$, and both maps are continuous. The computation confirms the two identities at $n=3$ on random matrices, and it identifies the matrix space with the product of the two halves.

**The splitting is an isometry up to the cross term.** Since

$$
\|A\|_{\mathrm{HS}}^{2}=\|H\|_{\mathrm{HS}}^{2}+\|K\|_{\mathrm{HS}}^{2}+2\operatorname{Re}\operatorname{tr}(H^{*}K),
$$

and the cross term vanishes because the two halves are orthogonal, the splitting is an isometry:

$$
\|A\|_{\mathrm{HS}}^{2}=\|H\|_{\mathrm{HS}}^{2}+\|K\|_{\mathrm{HS}}^{2}.
$$

The computation confirms the identity at $n=2,3,4$ on random matrices, and it is the Pythagorean theorem of the split.

**The isometry makes the two halves orthogonal coordinates.** In the real Euclidean structure of the matrix space the two halves are perpendicular subspaces, so a matrix is a point of the product and its distance to zero is the square root of the sum of the squares of the two coordinates. The computation confirms the orthogonality at $n=3$ by the vanishing of the inner product of a random Hermitian matrix with a random anti-Hermitian one, and it is the topological form of *The Two Halves as Orthogonal Complements*.

**The involution is an isometry of the matrix space.** The map $A\mapsto A^{*}$ preserves the Hilbert–Schmidt norm, since

$$
\|A^{*}\|_{\mathrm{HS}}^{2}=\operatorname{tr}(AA^{*})=\operatorname{tr}(A^{*}A)=\|A\|_{\mathrm{HS}}^{2},
$$

so it is an isometry of order two whose fixed set is the Hermitian half and whose anti-fixed set is the anti-Hermitian half. The computation confirms the isometry at $n=3$, and it is the metric reason the two halves are the two eigenspaces of a symmetry.

## The Strata of the Hermitian Half

**The inertia is constant on open sets.** The eigenvalues of a Hermitian matrix depend continuously on the entries, so the number of positive and of negative eigenvalues is constant on a neighbourhood of every matrix with no zero eigenvalue; hence

$$
\operatorname{Herm}_n^{(p,q)}=\{H:\text{inertia }(p,q)\}
$$

is open for $p+q=n$. The computation confirms the openness at $n=3$ by perturbing random Hermitian matrices and finding the inertia unchanged, and it gives $n+1$ regions.

**The regions of fixed inertia are separated by the singular set.** A path between two matrices of different inertia must cross the set of singular Hermitian matrices, since the inertia can change only when an eigenvalue passes through zero. The computation confirms the separation at $n=3$ by following a path from a positive to a negative definite matrix and finding a zero eigenvalue, and it is why the singular set is the wall of the half.

**Each region is connected.** Two Hermitian matrices of the same inertia are joined by a path of the same inertia, since the unitary group acts transitively on each region and is connected, and a matrix of inertia $(p,q)$ is $U\operatorname{diag}(1,\dots,-1,\dots)U^{*}$ with $U$ unitary. The computation confirms the transitivity at $n=3$, and it shows that the $n+1$ regions are the connected components of the complement of the singular set.

**The rank strata inside the Hermitian half have real dimension $2nr-r^{2}$.** A Hermitian matrix of rank $r$ is $UV^{*}$ with $U$ of size $n\times r$ and the parameter count gives

$$
\dim_{\mathbb{R}}\{H\in\operatorname{Herm}_n:\operatorname{rank}H=r\}=2nr-r^{2},
$$

which gives $5,8,9$ at $n=3$ and the full dimension $n^{2}$ at $r=n$. The computation confirms the count at $n=3$ against the formula.

## The Positive Cone

**The positive definite cone is convex.** For $P,Q$ positive definite and $0\le t\le1$,

$$
(1-t)P+tQ\ \text{is positive definite},
$$

since the quadratic form of the combination is the combination of the positive quadratic forms. The computation confirms the convexity at $n=3$ on fifty values of $t$ and random positive pairs, and it is the reason the cone is contractible.

**The cone is contractible to the identity.** The homotopy

$$
H(P,t)=(1-t)P+t\,\mathrm{I},\qquad 0\le t\le1,
$$

stays inside the cone because the combination of two positive definite matrices is positive definite, and it joins every positive matrix to the identity. The computation confirms the path at $n=3$ by checking the positivity at every step, and it gives the contractibility of the cone.

**The cone is open in the Hermitian half.** The eigenvalues are continuous and positive on the cone, so a small perturbation stays positive, and the cone is the region of inertia $(n,0)$; hence it is open, convex and therefore homeomorphic to the whole half. The computation confirms the openness at $n=3$, and it is the reason the exponential is a homeomorphism onto the cone.

**The exponential is a homeomorphism onto the cone.** The map $\exp:\operatorname{Herm}_n\to\mathrm{PD}_n$ is continuous, bijective with inverse the logarithm, and both maps are continuous, so

$$
\operatorname{Herm}_n\cong\mathrm{PD}_n
$$

as topological spaces. The computation confirms the two-sided inverse at $n=3$ on random Hermitian matrices and random positive ones, and it is the statement that the noncompact half and the open cone have the same topology.

## The Unitary Group

**The unitary group is closed and bounded.** It is the set of matrices with $A^{*}A=\mathrm{I}$, which is closed since the entries of $A^{*}A$ are continuous functions, and every unitary matrix has Hilbert–Schmidt norm $\sqrt n$, so

$$
\mathrm{U}(n)\ \text{is compact},\qquad \|U\|_{\mathrm{HS}}=\sqrt n.
$$

The computation confirms the norm at $n=2,3,4$, and it is the reason the unitary group is the compact part, in contrast with the two halves.

**The determinant of a unitary matrix has modulus one.** Since $|\det U|^{2}=\det(U^{*}U)=1$,

$$
\det:\mathrm{U}(n)\to S^{1}
$$

is a continuous surjection, and it is surjective because $\operatorname{diag}(e^{i\varphi},1,\dots,1)$ is unitary with determinant $e^{i\varphi}$. The computation confirms the modulus at $n=2,3$ and the surjectivity by the diagonal example, and it is the first sign that the unitary group is not contractible.

**The unitary group is not contractible.** A contractible space has trivial continuous maps into any space up to homotopy, while the determinant is a surjection onto the circle and the circle is not contractible; so

$$
\mathrm{U}(n)\ \text{is not contractible},
$$

which was confirmed at $n=2,3$ by the determinant having every phase. So the unitary half carries the topology which the two linear halves do not, and it is the only one of the three sets with a nontrivial homotopy type.

**The unitary group is a real algebraic set of dimension $n^{2}$.** It is cut by the $n^{2}$ real equations $U^{*}U=\mathrm{I}$ and its dimension is $n^{2}$, the dimension of the anti-Hermitian half. The computation confirms the dimension at $n=2,3,4$ by the count of the anti-Hermitian coordinates, and it is the reason the group and the anti-Hermitian half have the same dimension while only one of them is compact.

## The Case $n=2$

**At $n=2$ each half is four-dimensional real.** The values are

$$
\dim_{\mathbb{R}}\operatorname{Herm}_2=4,\qquad \dim_{\mathbb{R}}\mathfrak{u}(2)=4,\qquad \dim_{\mathbb{R}}M_2(\mathbb{C})=8,
$$

which were recomputed at $n=2$. So the two-by-two matrix space is the orthogonal sum of two four-dimensional Euclidean spaces, and the splitting map is an isometry of $\mathbb{R}^{8}$.

**The Hermitian half of the biquaternion algebra has three regions.** The inertias are $(2,0)$, $(1,1)$ and $(0,2)$, so

$$
\operatorname{Herm}_2=\mathrm{PD}_2\ \sqcup\ \{\text{inertia }(1,1)\}\ \sqcup\ (-\mathrm{PD}_2),
$$

with the singular set as the common boundary. The computation confirms the three regions at $n=2$ by drawing random Hermitian matrices and reading the inertia, and it shows that the Peirce idempotents $\tilde\Pi_\pm$ sit at the boundary between the regions of inertia $(1,1)$ and the definite ones.

**The compact half of the two-by-two case fibres over the circle.** Since $\mathrm{SU}(2)\cong S^{3}$ and

$$
\mathrm{U}(2)/\mathrm{SU}(2)\cong S^{1},
$$

the determinant exhibits the group as a bundle of three-spheres over the circle, and the computation confirms the dimension count $1+3=4$ at $n=2$. So the biquaternion unitary group carries a three-sphere as well as the phase of its determinant, and the determinant of *The Polar Decomposition from the Two Halves* supplies the circle factor.

## Summary

Each of the two halves is a real Euclidean space of dimension $n^{2}$, closed in the matrix space and meeting the other only at zero, and the splitting map is a linear homeomorphism which is an isometry by the Pythagorean identity $\|A\|_{\mathrm{HS}}^{2}=\|H\|_{\mathrm{HS}}^{2}+\|K\|_{\mathrm{HS}}^{2}$, the cross term vanishing by orthogonality. The Hermitian half is cut by the inertia into $n+1$ open connected regions separated by the singular set, the rank strata have real dimension $2nr-r^{2}$, and the positive definite cone is convex, open and homeomorphic to the whole half through the exponential. The unitary group is compact of dimension $n^{2}$ and not contractible, since its determinant is a surjection onto the circle, so it is the only one of the three sets with a nontrivial homotopy type; at $n=2$ the halves are four-dimensional and the unitary group is a circle times a three-sphere.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{Herm}_n\cong\mathbb{R}^{n^{2}}$ | the Hermitian half as a Euclidean space |
| $\mathfrak{u}(n)\cong\mathbb{R}^{n^{2}}$ | the anti-Hermitian half as a Euclidean space |
| $\Phi(A)=(H,K)$ | the splitting map |
| $\|A\|_{\mathrm{HS}}^{2}=\|H\|_{\mathrm{HS}}^{2}+\|K\|_{\mathrm{HS}}^{2}$ | the Pythagorean identity |
| $\operatorname{Herm}_n^{(p,q)}$ | the region of inertia $(p,q)$ |
| $2nr-r^{2}$ | the dimension of the Hermitian rank $r$ stratum |
| $\mathrm{PD}_n$ | the convex open cone of positive matrices |
| $\det:\mathrm{U}(n)\to S^{1}$ | the surjection which obstructs contractibility |

## Further Reading

- Rajendra Bhatia, *Matrix Analysis* (Springer, 1997), for the topology of the positive definite cone and the unitary group.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the inertia and the inertia theorems.
- Allen Hatcher, *Algebraic Topology* (Cambridge, 2002), for the homotopy of the classical groups.
- [The Two Halves as Orthogonal Complements](the-two-halves-as-orthogonal-complements.html), for the orthogonality used in the Pythagorean identity.
- [The Topology of $M_n(\mathbb{C})$](the-topology-of-mnc.html), for the ambient space and its strata.
- [The Peirce Decomposition and the Two Halves](the-peirce-decomposition-and-the-two-halves.html), for the idempotents at the boundary of the regions.
