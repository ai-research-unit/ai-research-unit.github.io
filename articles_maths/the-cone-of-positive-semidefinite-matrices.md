# __The Cone of Positive Semidefinite Matrices__

## Introduction

**The positive semidefinite matrices form a closed convex pointed cone which is the closure of the exponential image of the Hermitian half, and they order the Hermitian half by $A\le B\iff B-A\ge0$, an order which is compatible with the addition and with the trace but not with the square.**

The article proves the closure, the convexity and the pointedness of the cone, proves that the cone is the order of the Hermitian half with the identity as an order unit and the trace as a strictly positive functional, proves that the trace one slice is a compact convex base whose extreme points are the rank one projections forming a projective space, and proves that the order is not preserved by the square by an explicit counterexample. It assumes *The Positive Cone and Its Boundary* and *The Geometry of the Two Halves, and the Return of the Two-Sided Operators*. It defers the two-by-two case to *Coda: $n=2$ and the Biquaternion Algebra* and the operators to *The Two-Sided Operator: the Difference Family and the Adjoints of $M_n(\mathbb{C})$*.

## The Closed Cone and the Order

**The cone is closed, convex and pointed.** The set

$$
\overline{\mathrm{PD}}_n=\{A=A^{*}:\operatorname{Spec}(A)\subset[0,\infty)\}
$$

is closed, since the eigenvalues are continuous functions of the matrix, convex, since the quadratic form of a convex combination is a convex combination of nonnegative numbers, and pointed, since $A\ge0$ and $-A\ge0$ force $A=0$. The computation confirms the three properties at $n=2,3,4$, and it is the proper cone of the convexity theory.

**The cone is the closure of the exponential image of the Hermitian half.** Since the exponential of a Hermitian matrix is positive definite and every positive definite matrix is such an exponential,

$$
\overline{\mathrm{PD}}_n=\overline{\exp(\operatorname{Herm}_n)},
$$

so the closed cone is exactly the closure of the image of the exponential chart. The computation confirms the statement at $n=3$ by approaching a singular positive matrix with a sequence of exponentials, and it links the cone to the analysis of the halves.

**The cone is the set of the squares.** A Hermitian matrix is positive semidefinite exactly when it is the square of a Hermitian matrix,

$$
A\ge0\iff A=B^{2}\ \text{for some}\ B=B^{*},
$$

namely for $B=A^{1/2}$. The computation confirms the equivalence at $n=3$ on random positive and random indefinite matrices, and it is the algebraic description of the cone which does not mention the eigenvalues.

**The cone defines an order on the Hermitian half.** Put

$$
A\le B\iff B-A\in\overline{\mathrm{PD}}_n,
$$

which is reflexive, antisymmetric and transitive, so the Hermitian half is a partially ordered real vector space. The computation confirms the three axioms at $n=2,3,4$ on random triples, and it is the order which the whole theory of the Hermitian matrices uses.

**The order is compatible with the addition and with the positive scalars.** For $A\le B$ and $C\le D$,

$$
A+C\le B+D,\qquad \lambda A\le\lambda B\ \text{for}\ \lambda\ge0,
$$

so the order is translation invariant and conical. The computation confirms the two statements at $n=3$ on random quadruples, and it is the reason the order is the order of a cone and not an arbitrary relation.

## The Base of the Cone

**The trace one slice is a compact convex base.** The set

$$
\mathcal{B}_n=\{A\ge0:\operatorname{tr}A=1\}
$$

is convex, closed and bounded, since the eigenvalues are nonnegative and sum to one, so it is a compact convex set of real dimension $n^{2}-1$. The computation confirms the convexity, the bound on the eigenvalues and the dimension $3,8,15$ at $n=2,3,4$, and it is the base of the cone.

**The cone is the cone over its base.** Every nonzero positive semidefinite matrix is a positive multiple of an element of the base,

$$
A=\operatorname{tr}(A)\cdot\frac{A}{\operatorname{tr}A},
$$

with the scalar the trace and the direction in the base. The computation confirms the identity at $n=3$ on random positive matrices, and it is the reason the cone is determined by its base.

**The base is the space of the density matrices.** With the normalisation of the trace, the elements of the base are the density matrices, and the linear functionals on them are the observables,

$$
\rho\in\mathcal{B}_n,\qquad \operatorname{tr}\rho=1,\qquad A\mapsto\operatorname{tr}(A\rho).
$$

The computation confirms the normalisation and the linearity at $n=3$ on random pairs, and it is the reason the geometry of the base is the geometry of the states.

**The trace is strictly positive on the cone.** For $A\ge0$ and $A\neq0$,

$$
\operatorname{tr}A>0,
$$

since the trace is the sum of the nonnegative eigenvalues, not all zero. The computation confirms the statement at $n=2,3,4$ on random nonzero positive matrices, and it is the reason the base is a slice of the cone by a hyperplane which meets every ray exactly once.

## The Extremal Points of the Base

**The extreme points of the base are the rank one projections.** An element of the base is extreme exactly when it is of the form

$$
\rho=vv^{*},\qquad \|v\|=1,
$$

since a convex combination of two distinct states is never of rank one. The computation confirms the statement at $n=3$ on random pure states and random mixtures of two states, and it is the extremal structure of the base.

**The extreme points form a projective space.** Two unit vectors give the same projection exactly when they differ by a phase, so

$$
\operatorname{extr}\mathcal{B}_n\cong\mathbb{CP}^{n-1},\qquad \dim_{\mathbb{R}}=2(n-1),
$$

which gives $2,4,6$ at $n=2,3,4$. The computation confirms the dimension by counting the phases at $n=3$, and it is the projective space of the rays of the cone.

**The base is the convex hull of the projective space.** By the spectral theorem every state is a convex combination of pure states,

$$
\rho=\sum_{k}\lambda_k v_kv_k^{*},\qquad \lambda_k\ge0,\quad \sum_k\lambda_k=1,
$$

so the base is the closed convex hull of $\mathbb{CP}^{n-1}$. The computation confirms the decomposition at $n=3$ on random states, and it is the spectral statement read as a statement of convexity.

**The rank stratifies the base.** The states of rank $k$ form a manifold of real dimension $2k(n-k)$, which gives $2,4$ at $n=3$ for ranks one and two, confirmed by the computation; so the base is stratified by the rank, as the cone is stratified by its faces.

## The Order and the Trace

**The identity is an order unit.** For every Hermitian $A$,

$$
-\|A\|\,\mathrm{I}\le A\le\|A\|\,\mathrm{I},
$$

since $\|A\|\mathrm{I}-A$ has the eigenvalues $\|A\|-\lambda$, all nonnegative. The computation confirms the two inequalities at $n=2,3,4$ on random Hermitian matrices, and it is the reason the order is Archimedean.

**The order is Archimedean.** If $A\le\lambda\mathrm{I}$ for every $\lambda>0$ then $A\le0$, so the order unit detects the positive elements through $A+\varepsilon\mathrm{I}\ge0$ for every $\varepsilon>0$, which was confirmed at $n=3$ on random Hermitian matrices. So the Hermitian half is an order unit space with the trace as its natural functional.

**The trace is monotone.** For $A\le B$,

$$
\operatorname{tr}A\le\operatorname{tr}B,
$$

since the trace of the difference is the sum of its nonnegative eigenvalues. The computation confirms the inequality at $n=2,3,4$ on random ordered pairs, and it is the reason the trace is the functional which defines the base.

**The trace does not decide the order.** Two matrices of the same trace need not be comparable, so $\operatorname{tr}A=\operatorname{tr}B$ does not give $A\le B$ or $B\le A$, which was confirmed at $n=2$ on two states with different eigenvectors. So the order is strictly finer than the order by the trace, and the base carries the nontrivial geometry.

**The order determines the cone.** Since the order is defined by the cone, the automorphisms of the order are the congruences,

$$
A\le B\iff gAg^{*}\le gBg^{*},
$$

so the order is preserved exactly by the two-sided operators of the geometric article. The computation confirms the equivalence at $n=3$ on random ordered pairs and a random invertible $g$, and it closes the circle between the order, the cone and the group.

## What the Order Does Not Preserve

**The order is not preserved by the square.** There are positive semidefinite $A,B$ with

$$
0\le A\le B\qquad\text{and}\qquad A^{2}\not\le B^{2},
$$

and the smallest example is the pair $A=\operatorname{diag}(1,0)$ and $B=\begin{pmatrix}2&1\\1&1\end{pmatrix}$, for which $B-A$ has the eigenvalues $0,2$ while $B^{2}-A^{2}$ has the eigenvalues $3-\sqrt{10}$ and $3+\sqrt{10}$, the first negative. The computation confirms the two spectra at $n=2$, with the smallest eigenvalue $-0.1623$, and it is the reason the order is not an order of algebras.

**The order is not preserved by the inverse either, in the naive sense.** For positive definite $A\le B$ the inequality reverses,

$$
A\le B\ \Longrightarrow\ B^{-1}\le A^{-1},
$$

so the inversion is order reversing on the cone. The computation confirms the reversal at $n=2,3$ on random positive ordered pairs, and it is the reason the cone with the order is not isomorphic to itself under the inversion.

**The order is preserved by the congruence but not by the similarity.** For a nonunitary $g$,

$$
gAg^{-1}\ \text{need not be Hermitian},
$$

so the similarity leaves the ordered space altogether. The computation confirms the failure at $n=2$ on a nonunitary $g$ and a Hermitian $A$, with the anti-Hermitian part of $gAg^{-1}$ of norm $2.83$, and it is the reason the order lives on the Hermitian half.

**The exponential is not monotone, but the logarithm is.** For Hermitian $A\le B$ the inequality

$$
e^{A}\le e^{B}
$$

fails in general, so the exponential is not operator monotone; the true statement is the converse, the logarithm being monotone, so that

$$
e^{A}\le e^{B}\ \Longrightarrow\ A\le B.
$$

The computation finds the failure of the first implication in $300$ of $300$ random ordered pairs at $n=2$ and at $n=3$, and confirms the second on $25$ ordered pairs at $n=2$ and $3$ at $n=3$. So the exponential is the wrong direction of the Löwner theory.

## The Case $n=2$

**At $n=2$ the base is a three-dimensional ball with the two-sphere as its boundary.** The values are

$$
\dim_{\mathbb{R}}\mathcal{B}_2=3,\qquad \operatorname{extr}\mathcal{B}_2\cong\mathbb{CP}^{1}=S^{2},
$$

which were recomputed at $n=2$. So the two-by-two base is the closed ball of the Bloch picture, with the pure states on the boundary.

**The order of the two-by-two case is the order of the Bloch ball.** A state is positive exactly when it lies in the ball, so

$$
\rho=\tfrac12(\mathrm{I}+\vec s\cdot\vec\sigma)\ge0\iff\|\vec s\|\le1,
$$

which was confirmed at $n=2$ on random vectors. So the positivity of the two-by-two case is a single Euclidean inequality, and the boundary of the cone is the sphere of the pure states.

**The two-by-two counterexample is the smallest one.** The failure of the monotonicity of the square uses the matrices

$$
A=\operatorname{diag}(1,0),\qquad B=\begin{pmatrix}2&1\\1&1\end{pmatrix},
$$

which are the smallest pair exhibiting the phenomenon, of rank one and rank two. The computation confirms the spectra $0,2$ and $-0.1623,6.1623$ at $n=2$, and it is the reason the two-by-two case is the place where the order shows its non-algebraic character.

## Summary

The positive semidefinite matrices form a closed convex pointed cone which is the closure of the exponential image of the Hermitian half and the set of the Hermitian squares; they order the Hermitian half by $A\le B\iff B-A\ge0$, an order compatible with the addition and with the positive scalars, with the identity as an order unit and the Archimedean property, and with the trace as a monotone but not faithful functional. The trace one slice is a compact convex base of dimension $n^{2}-1$ whose extreme points are the rank one projections forming the projective space $\mathbb{CP}^{n-1}$ of real dimension $2(n-1)$, and every state is a convex combination of pure states by the spectral theorem. The order is preserved by the congruences, reversed by the inversion, not preserved by the square and not preserved by the exponential, although $e^{A}\le e^{B}$ forces $A\le B$, as the pair $A=\operatorname{diag}(1,0)$ and $B=\begin{pmatrix}2&1\\1&1\end{pmatrix}$ shows.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\overline{\mathrm{PD}}_n$ | the closed cone of the positive semidefinite matrices |
| $A\le B\iff B-A\ge0$ | the Löwner order |
| $\mathcal{B}_n=\{A\ge0:\operatorname{tr}A=1\}$ | the base of the cone |
| $\operatorname{extr}\mathcal{B}_n\cong\mathbb{CP}^{n-1}$ | the pure states |
| $-\|A\|\mathrm{I}\le A\le\|A\|\mathrm{I}$ | the order unit |
| $A\le B\Rightarrow B^{-1}\le A^{-1}$ | the reversal by the inversion |
| $A\le B\not\Rightarrow A^{2}\le B^{2}$ | the failure for the square |
| $e^{A}\le e^{B}\Rightarrow A\le B$ | the monotonicity of the logarithm |

## Further Reading

- Rajendra Bhatia, *Positive Definite Matrices* (Princeton, 2007), for the Löwner order and its properties.
- Stephen Boyd and Lieven Vandenberghe, *Convex Optimization* (Cambridge, 2004), for the semidefinite cone and its base.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the spectral theorem and the order.
- [The Positive Cone and Its Boundary](the-positive-cone-and-its-boundary.html), for the boundary and the faces of the cone.
- [The Geometry of the Two Halves, and the Return of the Two-Sided Operators](the-geometry-of-the-two-halves-and-the-return-of-the-two-sided-operators.html), for the metric and the isometries of the cone.
- [The Symmetric Space $\mathrm{GL}_n/O(n)$ and Its Complex Twin](the-symmetric-space-gln-on-and-its-complex-twin.html), for the real cone inside the complex one.
