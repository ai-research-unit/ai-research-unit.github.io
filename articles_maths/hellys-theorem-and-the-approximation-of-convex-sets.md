
# __Helly's Theorem and the Approximation of Convex Sets__

## Introduction

**Helly's theorem** answers a question of pure intersection: if a finite family of convex sets in $\mathbb{R}^n$ is such that every $n+1$ of its members have a common point, then the whole family has a common point. The number $n+1$ is the **Helly number** of the convex sets of $\mathbb{R}^n$, and the theorem is the exact dual of Carathéodory's bound: both express the finite-dimensionality of the convex geometry, one by the number of points needed for a convex combination, the other by the number of conditions needed to force a common point. The theorem is also an algorithm in disguise, since it reduces the consistency of a system of convex inequalities to the consistency of its subsystems of size $n+1$.

The second half of the article is the **approximation of convex sets** by simpler ones, above all by **polytopes**. The instrument is the **Hausdorff distance** between compact convex sets, and the governing facts are that every compact convex set is the limit of inscribed and of circumscribed polytopes, that convergence in the Hausdorff distance is convergence of the support functions, and that the collection of compact convex sets is complete and, modulo translation, locally compact in that distance, by the **Blaschke selection theorem**. Helly's theorem enters the approximation through the outer approximation by finitely many supporting half-spaces, which is where a family of half-spaces is tested for a common point.

The setting is the finite-dimensional convex geometry of *Convex Analysis*, in the *Foundations of Analysis* category of this Part, which owns the convex hull, Carathéodory's theorem, the separation theorems and the polyhedral theory; that material is cited. What this article adds is Helly's theorem with the finite and the compact versions of its proof, the Helly number, the Hausdorff metric on convex bodies, and the polytopal approximation theorems. The metric space background is *Normed and Banach Spaces* and *Real Topology*, the compactness is that of *Topological Modules and Vector Spaces*, and the extreme-point theory invoked in the comparison is *Convex Sets and the Convex Hull*. The order-theoretic and measure-theoretic structures of the corpus are not used.

## Helly's Theorem

### The Finite Theorem

**Theorem (Helly, finite version).** Let $K_1,\dots,K_m$ be convex subsets of $\mathbb{R}^n$ with $m\geq n+1$. If every subfamily of $n+1$ of the $K_i$ has a nonempty intersection, then $\bigcap_{i=1}^{m}K_i$ is nonempty.

*Proof.* It is enough to show that a minimal subfamily with empty intersection has at most $n+1$ members under the hypothesis that every $n+1$ of the sets meet, since then an empty intersection of the whole family would exhibit such a subfamily and contradict the hypothesis. Let $K_1,\dots,K_m$ be minimal with empty intersection, so $\bigcap_{i=1}^{m}K_i = \emptyset$ and $\bigcap_{j\neq i}K_j\neq\emptyset$ for every $i$; pick $x_i\in\bigcap_{j\neq i}K_j$. The hypothesis forces $m\geq n+2$: a subfamily of at most $n+1$ members with empty intersection could be enlarged to $n+1$ members of the family still with empty intersection. Among the points $x_1,\dots,x_m$ choose a minimal affinely dependent subfamily and relabel it $x_1,\dots,x_k$, so $k\leq n+2$ because $n+1$ points of $\mathbb{R}^n$ are always affinely independent. By the Radon lemma the set $\{x_1,\dots,x_k\}$ splits into two nonempty parts $A$ and $B$ with $\operatorname{conv}\{x_i : i\in A\}$ and $\operatorname{conv}\{x_i : i\in B\}$ meeting, and a point $z$ of the intersection lies in $K_j$ for every $j$: for $j\leq k$ the part of the partition not containing $j$ consists of points $x_i$ with $i\leq k$, $i\neq j$, each of which lies in $K_j$, so its convex hull lies in $K_j$; for $j > k$ every index $i\leq k$ satisfies $i\neq j$, so all the points $x_1,\dots,x_k$ lie in $K_j$ and their convex hull does too. Hence $z\in\bigcap_{i=1}^{m}K_i$, a contradiction. Therefore $m\leq n+1$, and the theorem follows.

**Lemma (Radon).** Any finite affinely dependent set of points of a real vector space splits into two disjoint parts whose convex hulls meet. *Proof.* An affine dependence $\sum_{i=1}^{k}\lambda_i x_i = 0$ with $\sum_i\lambda_i = 0$ and not all $\lambda_i$ zero exists. Split the index set into $P = \{i : \lambda_i>0\}$ and $N = \{i : \lambda_i<0\}$, both nonempty because the coefficients sum to zero. Then $\sum_{i\in P}\lambda_i x_i = \sum_{i\in N}(-\lambda_i)x_i$, and dividing both sides by the common positive value $\sum_{i\in P}\lambda_i = \sum_{i\in N}(-\lambda_i)$ exhibits a point lying in the two convex hulls.

**Theorem (Helly, compact version).** Let $\{K_\alpha\}_{\alpha\in A}$ be a family of compact convex subsets of $\mathbb{R}^n$. If every $n+1$ of them meet, then the whole family meets.

*Proof.* A finite subfamily meets by the finite version, so by the finite intersection property of the compact sets the whole family meets. If the sets are closed convex and one of them is compact, the same conclusion holds by intersecting each with the compact member.

**Remark (the sharpness of $n+1$).** In $\mathbb{R}^n$ the number $n+1$ cannot be lowered: the $n+1$ facets of a simplex meet $n$ at a time and not all together, and the edges of a complete graph exhibit the same failure. The **Helly number** of a class $\mathcal{F}$ of sets is the least integer $h$ such that $h$-wise intersection implies total intersection for every finite subfamily; Helly's theorem is the statement that the convex sets of $\mathbb{R}^n$ have Helly number $n+1$, that the translates of a convex set have Helly number $2$, that the axis-parallel boxes of $\mathbb{R}^n$ have Helly number $2$, and that the complements of convex sets have Helly number $n+1$ as well.

### The Duality with Carathéodory

**Proposition.** Helly's theorem is equivalent to the separation theorem for a finite family of convex sets, and it is dual to Carathéodory's theorem in the following sense: Carathéodory bounds the size of a subfamily of *points* whose convex hull contains a point, and Helly bounds the size of a subfamily of *sets* whose intersection is forced; each is obtained from the other by polarity.

*Proof.* Carathéodory's theorem gives that a point lies in $\operatorname{conv}(a_1,\dots,a_k)$ using at most $n+1$ of the $a_i$; Helly's theorem gives that $\bigcap K_i\neq\emptyset$ from the intersections of $n+1$ at a time. Passing to the polar dual of a set of half-spaces exchanges a convex hull of points with an intersection of half-spaces, and the two bounds interchange; *Convex Analysis* carries the statement of the duality, and it is restated here only in words.

**Corollary (the consistency test).** A system of convex inequalities $f_i(x)\leq0$, $i = 1,\dots,m$, with each $f_i$ convex and each sublevel set $L_i = \{x : f_i(x)\leq0\}$ closed, is consistent when each subsystem of $n+1$ of the inequalities is consistent; when one sublevel set is compact, the test extends to an infinite system. This is the form in which Helly's theorem is used in optimisation and in the theory of linear programming, of which the finite-dimensional case of *Convex Analysis* treats the polyhedral theory.

### Approximation by Polytopes

**Definition.** Let $\mathcal{K}^n$ be the set of nonempty compact convex subsets of $\mathbb{R}^n$ equipped with the **Hausdorff distance**

$$
d_H(K,L) = \max\Bigl(\sup_{x\in K}\operatorname{dist}(x,L),\ \sup_{y\in L}\operatorname{dist}(y,K)\Bigr) = \inf\{\epsilon : K\subseteq L + \epsilon B,\ L\subseteq K + \epsilon B\},
$$

where $B$ is the closed unit ball. A **polytope** is a compact convex set that is the convex hull of finitely many points, equivalently the bounded intersection of finitely many half-spaces, by the Minkowski–Weyl theorem of *Convex Analysis*.

**Theorem (approximation by inscribed and circumscribed polytopes).** Every $K\in\mathcal{K}^n$ is the limit in the Hausdorff distance of a sequence of inscribed polytopes and of a sequence of circumscribed polytopes: there are polytopes $P_j\subseteq K\subseteq Q_j$ with $d_H(P_j,K)\to0$ and $d_H(Q_j,K)\to0$.

*Proof.* Inscribe in $K$ the convex hull $P_j$ of a $\delta_j$-net of its boundary with $\delta_j\to0$: every point of $K$ is within $\delta_j$ of a point of $P_j$, by the convexity of $K$ and the choice of the net, so $d_H(P_j,K)\leq\delta_j$. Circumscribe about $K$ the intersection $Q_j$ of the finitely many supporting half-spaces whose boundary hyperplanes support $K$ in a finite $\delta_j$-net of the unit sphere; the distance between two parallel supporting hyperplanes whose normals differ by at most $\delta_j$ is bounded by the diameter of $K$ times $\delta_j$, so $d_H(Q_j,K)\to0$. Both nets are finite because the sphere and the boundary of a compact set are totally bounded.

**Theorem (the Hausdorff metric).** The Hausdorff distance is a metric on $\mathcal{K}^n$; the map $K\mapsto\sigma_K$ to the support functions of *The Support Function Operator* is an isometric embedding of $(\mathcal{K}^n,d_H)$ into the Banach space of continuous functions on the sphere with the supremum norm; and a sequence converges in $d_H$ exactly when the support functions converge uniformly.

*Proof.* The triangle inequality for $d_H$ is the triangle inequality for the distance to a set; symmetry is by definition; the identification $d_H(K,L) = \sup_{\lVert u\rVert = 1}\lvert\sigma_K(u) - \sigma_L(u)\rvert$ is the polar form of the two inclusion conditions, using that a compact convex set is the intersection of its supporting half-spaces, which is the support-function reconstruction of *Convex Analysis*.

**Theorem (Blaschke selection).** The set $\mathcal{K}^n$ is complete for the Hausdorff metric, and it is **locally compact** up to translation: every bounded sequence of compact convex sets contains a subsequence converging in the Hausdorff distance.

*Proof.* Completeness: a Cauchy sequence of compact convex sets has a limit that is closed and bounded, and it is convex because it is the limit of convex sets and the Hausdorff distance controls the segments; boundedness and closedness give compactness. Local compactness: rescale the sequence to lie in a fixed ball, extract from an $\epsilon$-net of the union a convergent subsequence by the compactness of the finite-dimensional ball, and the limit is the closed convex hull of the partial limits; this is the Blaschke selection theorem.

## Worked Cases

### Linear Programming

The feasible set of a linear program is a polyhedron $P = \{x : Ax\leq b\}$, the intersection of finitely many half-spaces of $\mathbb{R}^n$. Helly's theorem states that $P$ is empty exactly when some subfamily of $n+1$ of the half-spaces has empty intersection; the finite version of Farkas' lemma is the corresponding statement of the form, one alternative of which is the separation of the convex sets. The number $n+1$ is the number of constraints needed to certify infeasibility, and it is the sense in which the certificate of infeasibility of a linear program is short.

### The Unit Balls of a Norm

Let $B$ and $B'$ be the closed unit balls of two norms on $\mathbb{R}^n$, both compact convex and symmetric. Their Hausdorff distance is the smallest $\epsilon$ with $B\subseteq(1+\epsilon)B'$ and $B'\subseteq(1+\epsilon)B$, so it measures the relative distortion of the two norms: $d_H$ small means the norms are uniformly equivalent with constant close to one. The approximation of $B$ by the inscribed polytopes is the approximation of the norm by the $\ell_\infty$-type norms with finitely many linear form constraints, and the circumscribed polytopes give the approximation by finitely many supporting hyperplanes.

### A Helly Number of Two

For a family of translates $x_\alpha + C$ of a fixed compact convex $C$ in $\mathbb{R}^n$, the Helly number is two when $C$ is centrally symmetric and $2$ as well in general for translates of a convex set: a subfamily of translates meets whenever each pair meets, by the subadditivity of the support function, $2\sigma_C\leq\sigma_C+\sigma_C$. For axis-parallel boxes the Helly number is two: boxes meet pairwise exactly when the intervals of each coordinate meet pairwise, and a coordinate family of intervals has Helly number two.

## Summary

**Helly's theorem** states that a finite family of convex subsets of $\mathbb{R}^n$ has a common point when every $n+1$ of its members do; the compact version states the same for an arbitrary family of compact convex sets, by the finite intersection property. The number $n+1$ is the **Helly number** of the convex sets of $\mathbb{R}^n$, it is sharp, and the theorem is dual to Carathéodory's bound through polarity. It is used to certify the consistency of a convex system, and in particular the feasibility of a linear program, from subsystems of size $n+1$. The **Hausdorff distance** $d_H(K,L) = \inf\{\epsilon : K\subseteq L+\epsilon B,\ L\subseteq K+\epsilon B\}$ is a metric on compact convex sets, it is the supremum distance of the support functions, and every compact convex set is the limit in it of inscribed and of circumscribed **polytopes**. The space of compact convex sets is complete and locally compact up to translation, by the **Blaschke selection theorem**. The polyhedral theory, the separation theorems and Carathéodory's theorem are *Convex Analysis*; the support function is *The Support Function Operator* in this category; the compactness is *Topological Modules and Vector Spaces* and *Real Topology*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K_1,\dots,K_m$ | Convex sets whose intersection is tested |
| $n+1$ | Helly number of the convex sets of $\mathbb{R}^n$ |
| $h(\mathcal{F})$ | Helly number of a class of sets |
| $L_i = \{x : f_i(x)\leq0\}$ | Sublevel set of a convex function |
| $\mathcal{K}^n$ | Nonempty compact convex subsets of $\mathbb{R}^n$ |
| $d_H(K,L)$ | Hausdorff distance |
| $P\subseteq K\subseteq Q$ | Inscribed and circumscribed polytopes |
| $\sigma_K$ | Support function, $u\mapsto\sup_{x\in K}\langle u,x\rangle$ |

## Further Reading

- Eduard Helly, "Über Mengen konvexer Körper mit gemeinschaftlichen Punkten", *Jahresbericht der Deutschen Mathematiker-Vereinigung* **32** (1923), 175–176, for the original theorem.
- Ludwig Danzer, Branko Grünbaum and Victor Klee, "Helly's theorem and its relatives", in *Convexity*, Proceedings of Symposia in Pure Mathematics 7 (American Mathematical Society, 1963), 101–180, for the Helly number and the relatives of the theorem.
- Wilhelm Blaschke, *Kreis und Kugel* (Veit, 1916), for the selection theorem and the approximation of convex bodies.
- Peter M. Gruber, *Convex and Discrete Geometry*, Grundlehren der mathematischen Wissenschaften 336 (Springer, 2007), for the polytopal approximation and the Hausdorff metric in full.
- R. Tyrrell Rockafellar, *Convex Analysis* (Princeton University Press, 1970), for the finite-dimensional convex geometry in which the theorem sits.
- Branko Grünbaum, *Convex Polytopes*, Graduate Texts in Mathematics 221 (Springer, 2nd ed. 2003), for the polyhedral theory and the sharpness of the Helly number.
