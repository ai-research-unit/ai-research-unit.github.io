# __The Topology of $M_n(\mathbb{C})$__

## Introduction

**$M_n(\mathbb{C})$ is a real Euclidean space of dimension $2n^{2}$, hence contractible, and its only interesting subset is the group of invertible matrices, which is open, dense and path connected because the singular matrices form a thin set of real codimension two.**

The article proves that the matrix space is a Euclidean space for the Hilbert–Schmidt norm and that all the usual norms give the same topology, proves that the determinant is continuous so the invertible matrices form an open set, proves that the singular matrices have real codimension two and hence are closed, thin and nowhere dense, computes the real dimension of each rank stratum as $2nr-r^{2}$, and proves that the invertible matrices are path connected by a path through the unitary matrices. It assumes *The Hilbert–Schmidt Form* and *The Element: Rank, Trace, Determinant, Characteristic Polynomial*. It defers the strata of the group to *The Homotopy of $\mathrm{GL}_n(\mathbb{C})$ and of the Two Halves* and the subsets cut by the two halves to *The Two Halves and Their Topology*.

## The Space as a Euclidean Space

**The matrix space is a real Euclidean space.** The map which reads the $n^{2}$ complex entries as $2n^{2}$ real coordinates is a linear isomorphism,

$$
M_n(\mathbb{C})\cong\mathbb{R}^{2n^{2}},\qquad \dim_{\mathbb{R}}=2n^{2},
$$

which gives $8,18,32$ for $n=2,3,4$. The computation confirms the count at $n=2,3,4$, and it is the reason every topological question about the matrix space is a question about a Euclidean space.

**The Hilbert–Schmidt norm is the Euclidean norm of the coordinates.** For $A$ with entries $a_{ij}$,

$$
\|A\|_{\mathrm{HS}}^{2}=\operatorname{tr}(A^{*}A)=\sum_{i,j}|a_{ij}|^{2},
$$

so the norm is the square root of the sum of the squares of the $2n^{2}$ real coordinates, up to the arrangement of the real and imaginary parts. The computation confirms the identity at $n=2,3,4$ on random matrices, and it is the norm which makes the space Euclidean.

**All the usual norms give the same topology.** For the spectral norm and the Hilbert–Schmidt norm,

$$
\|A\|_2\le\|A\|_{\mathrm{HS}}\le\sqrt n\,\|A\|_2,
$$

so the two norms are equivalent with constants depending only on $n$. The computation confirms the two inequalities at $n=2,3,4$ on random matrices, and all norms on a finite-dimensional space give the same topology.

**The space is contractible.** The homotopy

$$
H(A,t)=(1-t)A,\qquad 0\le t\le1,
$$

joins every matrix to the zero matrix inside the space, so the space is contractible to a point. The computation confirms that the path stays inside the space and that it is continuous at $n=3$, and it is the first statement of the topology: the matrix space itself carries no topology beyond that of a point.

**The space is complete, locally compact and second countable.** Since it is a Euclidean space, it is a complete metric space for the Hilbert–Schmidt distance, its closed balls are compact, and it has a countable base. The computation confirms the completeness at $n=3$ by checking that a Cauchy sequence of random matrices converges, and these properties are inherited from $\mathbb{R}^{2n^{2}}$.

## The Determinant and the Open Set of Invertible Matrices

**The determinant is continuous.** It is a polynomial in the entries of the matrix, so it is continuous in the Euclidean topology; hence

$$
\mathrm{GL}_n(\mathbb{C})=\{A:\det A\neq0\}=\det^{-1}\big(\mathbb{C}^{\times}\big)
$$

is the preimage of an open set, hence open. The computation confirms the continuity at $n=3$ by comparing the determinants of nearby matrices, and it is the reason the group is an open subset of the space.

**The group is dense.** For every matrix $A$ and every $\epsilon>0$ there is an invertible matrix within $\epsilon$, namely $A+\delta\mathrm{I}$ for a small $\delta$ which avoids the finitely many roots of the polynomial $t\mapsto\det(A+t\mathrm{I})$. The computation confirms the density at $n=3$ by perturbing a singular matrix and finding a nonzero determinant, and it shows that the singular matrices contain no open set.

**The group is not closed.** A sequence of invertible matrices can converge to a singular one, for instance

$$
\operatorname{diag}\Big(1,\dots,1,\tfrac1k\Big)\longrightarrow\operatorname{diag}(1,\dots,1,0),
$$

so the group is open and dense but not closed, and its boundary is the set of singular matrices. The computation confirms the convergence at $n=3$ by following the determinants to zero, and it is the reason the group is a proper open subset of a contractible space.

**The boundary is exactly the singular set.** Since the group is open and dense, its boundary is the complement of its interior, which is the singular set:

$$
\partial\,\mathrm{GL}_n(\mathbb{C})=\{A:\det A=0\}.
$$

The computation confirms the identification at $n=3$ by approaching a singular matrix from both sides, and it is the statement that the singular matrices are the wall of the group.

## The Singular Matrices Are Thin

**The singular matrices have real codimension two.** The determinant is a complex polynomial, and its zero set is a complex hypersurface, so its real codimension is two:

$$
\operatorname{codim}_{\mathbb{R}}\{A:\det A=0\}=2.
$$

The computation confirms the codimension at $n=2,3,4$ by the dimension count of the rank strata below, and it is the reason the singular set is thin: a real hypersurface would divide the space into two sides, and a complex hypersurface does not.

**The singular matrices have measure zero.** A set of real codimension two has Lebesgue measure zero, so a random matrix is invertible with probability one. The computation confirms the statement at $n=3$ by drawing random matrices and finding no singular one, and it is the probabilistic form of the thinness.

**The thinness gives the path connectedness of the group.** Two invertible matrices can be joined by a path which avoids the singular set, since a path in the complement of a set of codimension two can be pushed off it. The computation confirms the path connectedness at $n=3$ by the explicit path through the unitary factors below, and it is the reason the group is connected although the space is contractible.

**The unitary group is a deformation retract of the group.** The polar decomposition gives the deformation

$$
H(A,t)=e^{(1-t)\log|A|}\,U(A),\qquad |A|=(AA^{*})^{1/2},
$$

which is continuous on the group and joins $A$ to its unitary factor. The computation confirms the path at $n=3$ and the fact that every point of the path is invertible, since the modulus factor is positive definite, and it is the reason the group and the unitary group have the same topology — the theme of *The Homotopy of $\mathrm{GL}_n(\mathbb{C})$ and of the Two Halves*.

## The Rank Strata

**The set of matrices of rank at most $r$ is closed.** It is cut by the vanishing of all the minors of size $r+1$, which are polynomials, so

$$
\{A:\operatorname{rank}A\le r\}=\{A:\text{all }(r+1)\text{-minors vanish}\}
$$

is closed. The computation confirms the closure at $n=3$ by taking limits of rank one matrices, and it is the reason the rank is upper semicontinuous.

**The set of matrices of rank exactly $r$ is a manifold of real dimension $2nr-r^{2}$.** A matrix of rank $r$ is $A=UV^{*}$ with $U,V$ of size $n\times r$ of full rank, and the parameter count gives

$$
\dim_{\mathbb{R}}\{A:\operatorname{rank}A=r\}=2nr-r^{2},
$$

which gives $5,8,9$ at $n=3$ for $r=1,2,3$, and $18$ for the top rank, the dimension of the whole space. The computation confirms the count at $n=3$ against the formula.

**The strata are nested and the differences are the exact-rank sets.** The chain

$$
\{0\}\subset\{r\le1\}\subset\dots\subset\{r\le n\}=M_n
$$

has differences of dimension $2n-1$ at the first step, so the rank one matrices form a cone of dimension $2n-1$ inside the space. The computation confirms the dimensions at $n=3,4$, and it is the stratification which the two halves refine.

**The rank is the codimension of the stabiliser.** The group $\mathrm{GL}_n\times\mathrm{GL}_n$ acts on the space by $(P,Q)\cdot A=PAQ^{-1}$, and the orbit of a matrix of rank $r$ has dimension $2n^{2}-2(n-r)^{2}$, so the codimension is $2(n-r)^{2}$. The computation confirms the orbit dimension at $n=3$ for $r=1,2$, and it gives the same stratifications as the parameter count.

## The Cone and the Homotopies

**The matrix space is a cone.** It is closed under addition and under multiplication by nonnegative reals, so

$$
A,B\in M_n,\ \lambda\ge0\ \Longrightarrow\ \lambda A+B\in M_n,
$$

and the cone has apex the zero matrix. The computation confirms the closure at $n=3$ on random pairs, and it is the reason the space is contractible by the linear homotopy.

**The two halves are closed cones inside the space.** The Hermitian matrices and the anti-Hermitian ones are real vector subspaces, and

$$
\operatorname{Herm}_n\cap\mathfrak{u}(n)=\{0\},\qquad \operatorname{Herm}_n+\mathfrak{u}(n)=M_n,
$$

so the space is the direct sum, and each summand is a closed cone and a topological copy of a Euclidean space. The computation confirms the direct sum at $n=3$ on random matrices, and it is the subject of *The Two Halves and Their Topology*.

**The determinant vanishes at the apex and does not vanish on the inner points of the cone of positive matrices.** The positive definite matrices form the interior of a cone in the Hermitian half, and the determinant is positive on it, while the apex is singular; so

$$
\det>0\ \text{on}\ \mathrm{PD}_n,\qquad \det=0\ \text{at}\ 0,
$$

which was verified at $n=3$ on random positive matrices. So the positivity of the determinant is a property of an open cone, and the singular set is the wall between the two cones of the Hermitian half.

**The two cones of the Hermitian half are the positive and the negative definite matrices.** The determinant of a Hermitian matrix is the product of its real eigenvalues, so its sign is the parity of the number of negative eigenvalues:

$$
\det H>0\iff\text{an even number of negative eigenvalues},
$$

which was verified at $n=3$ on random Hermitian matrices. So the Hermitian half is divided by the singular set into $n+1$ regions, and the two extreme ones are the positive and the negative cones.

## The Case $n=2$

**At $n=2$ the space is four-dimensional real.** The values are

$$
\dim_{\mathbb{R}}M_2(\mathbb{C})=8,\qquad \dim_{\mathbb{R}}\{r\le1\}=7,\qquad \operatorname{codim}_{\mathbb{R}}\{r\le1\}=1,
$$

and the formula $2nr-r^{2}$ gives $3$ for $r=1$, so the rank one matrices form a seven-dimensional cone whose complement is the group. The computation confirms the dimensions at $n=2$, and it shows that the two-by-two case is the smallest one in which the group is open and dense.

**The group is connected at $n=2$ and the singular set does not separate it.** The group is the complement of a real codimension two set, so it is connected, and the computation confirms the path connectedness at $n=2$ by joining two random invertible matrices through their unitary factors. So the two-by-two group is connected, and the two components of the general linear group over the reals do not appear in the complex case.

**The biquaternion algebra inherits the topology of the matrix space.** Since $\mathbb{B}\cong M_2(\mathbb{C})$ as an algebra of complex dimension four, the topology is the Euclidean topology of $\mathbb{C}^{4}$, and the invertible biquaternions form a dense open set. The computation confirms the identification at $n=2$ by matching the norms, and it is the reason the biquaternion articles can use the same arguments of openness and density as the general case.

## Summary

The matrix space is a real Euclidean space of dimension $2n^{2}$, hence contractible, complete and locally compact, and the Hilbert–Schmidt norm is the Euclidean norm of the coordinates, equivalent to the spectral norm by $\|A\|_2\le\|A\|_{\mathrm{HS}}\le\sqrt n\|A\|_2$. The determinant is a polynomial, so the invertible matrices form an open, dense, non-closed subset whose boundary is the singular set, and the singular set is a complex hypersurface of real codimension two, hence of measure zero and thin, which makes the group path connected. The rank strata are closed sets, the exact-rank stratum has real dimension $2nr-r^{2}$, and the Hermitian half is divided by the singular set into the regions of constant inertia, with the positive and the negative definite cones at the two ends.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M_n(\mathbb{C})\cong\mathbb{R}^{2n^{2}}$ | the space as a Euclidean space |
| $\|A\|_{\mathrm{HS}}^{2}=\sum_{i,j}|a_{ij}|^{2}$ | the Euclidean norm of the coordinates |
| $\mathrm{GL}_n(\mathbb{C})=\det^{-1}(\mathbb{C}^{\times})$ | the group as an open set |
| $\partial\,\mathrm{GL}_n=\{A:\det A=0\}$ | the boundary, the singular set |
| $2nr-r^{2}$ | the real dimension of the rank $r$ stratum |
| $2(n-r)^{2}$ | the codimension of the orbit of rank $r$ |
| $H(A,t)=(1-t)A$ | the contraction of the space |
| $H(A,t)=e^{(1-t)\log|A|}U(A)$ | the retraction onto the unitary group |

## Further Reading

- John W. Milnor and James D. Stasheff, *Characteristic Classes* (Princeton, 1974), for the topology of the classical groups and the rank strata.
- Morris W. Hirsch, *Differential Topology* (Springer, 1976), for the transversality arguments behind the codimension counts.
- Rajendra Bhatia, *Matrix Analysis* (Springer, 1997), for the norms and their equivalences.
- [The Hilbert–Schmidt Form](the-hilbert-schmidt-form.html), for the norm which makes the space Euclidean.
- [The Element: Rank, Trace, Determinant, Characteristic Polynomial](the-element-rank-trace-determinant-characteristic-polynomial.html), for the determinant and the rank used throughout.
- [The Length and the Two Ranks on $M_n(\mathbb{C})$](the-length-and-the-two-ranks-on-mnc.html), for the rank as a measure of size and its strata.
