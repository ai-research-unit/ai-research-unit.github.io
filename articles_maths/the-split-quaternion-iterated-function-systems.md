# __The Split-Quaternion Iterated Function Systems__

## Introduction

The iterated function systems of the split-quaternion algebra are the systems of the definite algebra of *The Quaternion Iterated Function Systems* read in an algebra whose norm is indefinite. The similarities are again $S(\tilde q)=\tilde a\tilde q\tilde b+\tilde c$, of Euclidean ratio $|\tilde a||\tilde b|$, and the Hutchinson theory of *Fractal Geometry* again gives a compact attractor and the similarity dimension when the open set condition holds. What changes is the indefinite geometry: the multiplicative part of a similarity preserves the **null cone**, and it scales the form $N$ by the factor $N(\tilde a)N(\tilde b)$, so a multiplicative map with $|N(\tilde a)N(\tilde b)|<1$ contracts the indefinite metric; an attractor lying on the null cone has vanishing form and degenerate indefinite length, while an attractor meeting the hyperboloid carries a genuine hyperbolic Cantor set. The open set condition is the delicate point: in the null cone the pieces can be tangent, because a null displacement puts the two images in contact along the cone, and the condition must be stated with an open set adapted to the null direction; whether it can always be so adapted is recorded as an open point.

The article defines the systems, proves the contraction and the invariance of the null cone, computes the elementary Cantor sets and the null example, identifies the **hyperbolic Cantor sets** with the limit sets of the Schottky groups of *The Limit Sets of the Hyperbolic Lattices* through the inverse branches, states the Bowen pressure formula for their dimension as quoted, presents the hyperbolic gasket, and compares the systems with the definite quaternion and the split-complex ones.

The similarities and the group work as in *The Quaternion Iterated Function Systems*; the algebra, the norm and the zero divisors are from *Split-Quaternion Algebra*, *Split-Quaternion Norm and Invertibility* and *Split-Quaternion Ideals and Peirce Decomposition*; the hyperboloid, the hyperbolic plane and the boundary are from *Split-Quaternions and Hyperbolic Geometry*; the limit sets, the Schottky groups and the critical exponent are from *The Limit Sets of the Hyperbolic Lattices* and *Kleinian and Fuchsian Groups*; the iterated function systems, the attractor, the open set condition and the similarity dimension are *Fractal Geometry*'s; and the comparison with the definite system is *The Quaternion Iterated Function Systems* and *The Split-Complex Iterated Function Systems*. No physics is invoked.

Throughout, $N$ is the indefinite norm of signature $(2,2)$ and $|\cdot|$ the Euclidean norm of $\mathbb{R}^4$; a similarity is $S(\tilde q)=\tilde a\tilde q\tilde b+\tilde c$ with ratio $\lambda=|\tilde a||\tilde b|$; the null cone is $\{N=0\}$; and $\mathbb{H}^{+}$ is the timelike sheet of the hyperboloid of *Split-Quaternions and Hyperbolic Geometry*.

## Contractions in the Indefinite Metric

**Proposition (the multiplicative part preserves the form up to a factor).** For $\tilde a,\tilde b\in\mathbb{H}_{\mathrm{s}}$ and $M(\tilde q)=\tilde a\tilde q\tilde b$, one has $N(M(\tilde q))=N(\tilde a)N(\tilde b)N(\tilde q)$. Hence $M$ preserves the null cone and the two open cones $N>0$ and $N<0$, and it contracts the form when $|N(\tilde a)N(\tilde b)|<1$.

*Proof.* The norm is multiplicative, $N(\tilde a\tilde q\tilde b)=N(\tilde a)N(\tilde q)N(\tilde b)$, by *Split-Quaternion Norm and Invertibility*; the sets on which $N$ is positive, negative or zero are therefore permuted among themselves according as the sign of the factor, and the factor is $N(\tilde a\tilde b)=N(\tilde a)N(\tilde b)$. $\square$

**Definition.** A **split-quaternion iterated function system** is a finite family $\{S_1,\dots,S_k\}$ of similarities with Euclidean ratios $\lambda_i=|\tilde a_i||\tilde b_i|<1$; its **attractor** is the unique compact set $\Lambda$ with $\Lambda=\bigcup_iS_i(\Lambda)$. The system is **multiplicative** when every $\tilde c_i=0$, and **null** when its seed lies on the null cone.

**Theorem (existence, and the dimension, quoted).** Every split-quaternion iterated function system has a unique nonempty compact attractor, the limit of the Hutchinson operator from any nonempty compact seed, and it is contained in a ball of the radius $\max_i|\tilde c_i|/(1-\max_i\lambda_i)$ in the Euclidean norm. If the open set condition holds — an open set $U$ with the $S_i(U)$ pairwise disjoint and contained in $U$ — then the Hausdorff and box dimensions of the attractor are the similarity dimension $s$ solving $\sum_i\lambda_i^{\,s}=1$. This is the theory of *Fractal Geometry*, quoted as in *The Quaternion Iterated Function Systems*.

**Corollary (the null attractor).** If the system is multiplicative and the seed lies on the null cone, the attractor lies on the null cone and $N$ vanishes on it.

*Proof.* The multiplicative maps preserve the null cone by the proposition, and the attractor is the closure of the union of the images of the seed. $\square$

## The Elementary Systems

**Example (the Cantor set in a complex plane).** The two maps $S_0(\tilde q)=\tfrac13\tilde q$ and $S_1(\tilde q)=\tfrac13\tilde q+\tfrac23e_1$ form a system of ratio $\tfrac13$; the open set condition holds with the open unit ball; the attractor is a Cantor set of dimension $\log2/\log3$, lying in the plane $\mathbb{C}_{e_1}=\operatorname{span}\{e_0,e_1\}$ because the maps preserve it. The system is the split-quaternion reading of the system of *The Quaternion Iterated Function Systems*, and it is the complex, positive-definite elementary case.

**Example (the null segment and the degeneracy of the metric).** Let $n$ be a null vector of $V$, for instance $n=e_1+e_2$, and let $S_0(\tilde q)=\tfrac12\tilde q$, $S_1(\tilde q)=\tfrac12\tilde q+\tfrac12n$. The attractor is the Euclidean segment $[0,n]$ with the address map $\omega\mapsto\sum_k\epsilon_k2^{-k}n$, and every point of it is null, because $tn$ is null for every real $t$. The Euclidean dimension of the attractor is $1$, the similarity dimension of the two maps of ratio $\tfrac12$; the **indefinite length is zero**, because the form vanishes on every point of it, and the hyperbolic metric of the sheet sees the whole segment as one ideal boundary point. The fixed point of $S_1$ is the endpoint $n$, which is null, and it lies on the cone; the two pieces $S_0(\Lambda)=[0,n/2]$ and $S_1(\Lambda)=[n/2,n]$ meet at the point $n/2$, which is itself null. **This is the null-cone phenomenon of the systems**: the pieces of the attractor touch along the cone, the indefinite metric degenerates on the whole attractor, and a dimension computed with the indefinite form is not the Euclidean one.

**Remark (the open set condition in the null cone).** The elementary null system above still satisfies the open set condition, with the open set $\{tn+\epsilon w:0<t<1,\ |\epsilon|<\eta\}$ and $w$ a direction transverse to the cone: the two images have the $n$-coordinate in $(0,\tfrac12)$ and $(\tfrac12,1)$ and are disjoint, and both lie in the set. **The naive failure of the condition therefore does not occur**, and the honest statement is narrower: the condition holds when the system admits an open set adapted to the null direction, the pieces being tangent along the cone when it does not, and whether every null displacement system admits such a set is recorded as an **open point** in the companion file. The article does not claim that the condition fails in general.

## Hyperbolic Cantor Sets and Gaskets

**Proposition (the Schottky limit sets are the attractors of the inverse branches).** Let $\Gamma$ be a Schottky group of $\operatorname{PSL}_2(\mathbb{R})$ with generators $\gamma_1^{\pm1},\dots,\gamma_g^{\pm1}$ pairing the boundary circles of $2g$ disjoint discs, and let $S_i$ be the inverse branches, restricted to the limit set. Then the $S_i$ contract the hyperbolic metric by a factor $\theta_i<1$ on the appropriate region, the limit set $\Lambda(\Gamma)$ is their attractor, and the open set condition holds with the union of the discs as the open set.

*Proof.* The inverse branch of a Möbius pairing of two disjoint discs carries the exterior disc into the interior disc and is a hyperbolic contraction there, with the derivative controlled by the discs; the invariance $\Lambda=\bigcup_iS_i(\Lambda)$ is the defining property of the limit set of a Schottky group, and the disjointness of the discs gives the open set condition. This is the standard dictionary between the Schottky groups and the conformal iterated function systems, and it belongs to *Kleinian and Fuchsian Groups*, cited with *The Limit Sets of the Hyperbolic Lattices*. $\square$

**Theorem (the dimension is the pressure exponent, quoted).** For the conformal system of the inverse branches of a Schottky group the similarity dimension is replaced by the **Bowen pressure exponent**: the Hausdorff dimension of the limit set is the unique $s$ with

$$
P(s)=\lim_{n\to\infty}\frac1n\log\sum_{|\omega|=n}\|DS_\omega\|_\infty^{\,s}=0 ,
$$

where $S_\omega$ is the composition of the branches of the word $\omega$ and $DS_\omega$ its derivative; when the branches have locally constant derivatives this reduces to $\sum_i\theta_i^{\,s}=1$, and the exponent equals the Patterson–Sullivan exponent $\delta(\Gamma)$ of *The Limit Sets of the Hyperbolic Lattices*. The statement is quoted from *Kleinian and Fuchsian Groups*, and it is the reason the hyperbolic Cantor set of this article is the same object as the limit set of the previous one.

**Definition (the hyperbolic gasket).** A **hyperbolic gasket** is the limit set of a discrete group generated by the inversions in the sides of a hyperbolic polygon whose translates are pairwise tangent in the manner of the gasket groups; it is the hyperbolic counterpart of the Euclidean Sierpinski gasket of *The Quaternion Iterated Function Systems*, its pieces meeting along the sides in the pattern of a gasket, and its dimension is the critical exponent of the group. The example of the Euclidean gasket of article 6 is the four-halves system; the hyperbolic gasket is the same combinatorial pattern in which the four pieces are the translates of a hyperbolic polygon and the contractions are the hyperbolic similarities taking the polygon into its sub-polygons.

## Comparison with the Definite and the Split-Complex Systems

**Remark.** The definite quaternion systems of *The Quaternion Iterated Function Systems* are the positive-definite case: the metric is Euclidean, the similarity dimension is available throughout, the Apollonian packing is the Kleinian example, and the null-cone degenerate phenomena do not occur. The split-complex systems are the two-dimensional case: the idempotent decomposition reduces a system in $\mathbb{D}$ to a pair of real systems, the attractor is a product of the two real attractors, and the dimension is the sum, with the same interval structure as in the split-complex Julia sets. The split-quaternion systems sit between the two: they contain the definite systems in the complex planes and the split-complex systems in the split-complex planes, they add the null attractors and the hyperbolic Cantor sets, and they lose the escape radius and the uniformity of the dimension that the definite case has. **The systems of the null cone are the genuinely new ones**, and they are the ones for which the open set condition is delicate.

## Worked Example

**Example (three systems).** The dimensions were recomputed from the ratios.

**(a) The Cantor set of ratio $\tfrac13$.** Two maps: $2(1/3)^s=1$ gives $s=\log2/\log3=0.6309\ldots$; the attractor lies in the plane $\mathbb{C}_{e_1}$ and the open set condition holds.

**(b) The null segment.** Two maps of ratio $\tfrac12$ with the null displacement $\tfrac12(e_1+e_2)$: the similarity dimension is the solution of $2(1/2)^s=1$, that is $s=1$, and it is the Euclidean dimension of the segment $[0,e_1+e_2]$; every point is null, so the indefinite length is zero and the hyperbolic dimension of the attractor as a hyperbolic set is zero. The two pieces meet at the null midpoint $n/2$.

**(c) The hyperbolic Cantor set.** The limit set of a two-generator Schottky group is the attractor of the two inverse branches; its dimension is the pressure exponent, strictly between $0$ and $1$ by *The Limit Sets of the Hyperbolic Lattices*, and no numerical value is asserted here, since none is recomputed in this pass.

## Summary

A split-quaternion iterated function system is a finite family of similarities $S(\tilde q)=\tilde a\tilde q\tilde b+\tilde c$ of Euclidean ratio $|\tilde a||\tilde b|<1$; it has a compact attractor, and when the open set condition holds its dimension is the similarity dimension $\sum\lambda_i^s=1$, quoted from *Fractal Geometry* as in the definite article. The indefinite geometry adds three features. The multiplicative part preserves the null cone and scales the form by $N(\tilde a)N(\tilde b)$, so an attractor on the null cone has vanishing indefinite length: the null segment generated by a null displacement has Euclidean dimension $1$ and indefinite length zero, and its pieces touch at the null midpoint. The hyperbolic Cantor sets are the limit sets of the Schottky groups, realised as the attractors of the inverse branches, with the Bowen pressure dimension equal to the Patterson–Sullivan exponent of *The Limit Sets of the Hyperbolic Lattices*; the hyperbolic gasket is the analogous gasket pattern in the hyperbolic plane. The open set condition in the null cone holds when an open set adapted to the null direction exists, and whether it always does is recorded as an open point rather than asserted. The comparison with the definite systems is *The Quaternion Iterated Function Systems*'s and with the two-dimensional systems *The Split-Complex Iterated Function Systems*'s.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S(\tilde q)=\tilde a\tilde q\tilde b+\tilde c$ | Split-quaternion similarity |
| $\lambda=\lvert\tilde a\rvert\lvert\tilde b\rvert$ | Euclidean ratio |
| $N(\tilde a)N(\tilde b)$ | Factor by which the multiplicative part scales the form |
| Null cone $\{N=0\}$ | Invariant cone of the multiplicative maps; the degenerate metric locus |
| $[0,n]$ with $n$ null | The null segment attractor |
| $\Lambda$ | Attractor; limit set of a Schottky group |
| $\theta_i$, $s$, $\delta$ | Contraction factors; dimension; Patterson–Sullivan exponent |
| $\mathbb{H}^{+}$ | The hyperbolic plane of *Split-Quaternions and Hyperbolic Geometry* |

## Further Reading

- John E. Hutchinson, "Fractals and self-similarity", *Indiana University Mathematics Journal* 30 (1981), 713–747. The attractor and the open set condition, cited to *Fractal Geometry*.
- Kenneth Falconer, *Fractal Geometry: Mathematical Foundations and Applications*, 3rd ed. (Wiley, 2014). The similarity dimension and the box dimension, cited to *Fractal Geometry*.
- Rufus Bowen, "Hausdorff dimension of quasi-circles", *Publications Mathématiques de l'IHÉS* 50 (1979), 11–25. The pressure formula for the dimension of the limit set of a quasi-Fuchsian group, cited to *Kleinian and Fuchsian Groups*.
- David Mumford, Caroline Series and David Wright, *Indra's Pearls: The Vision of Felix Klein* (Cambridge, 2002). The Schottky groups, the gasket groups and their limit sets.
- Garret Sobczyk, "The hyperbolic number plane", *The College Mathematics Journal* 26 (1995), 268–280. The split-complex systems and the idempotent decomposition.
