
# __Real Structures on a Curve__

## Introduction

A smooth projective curve over $\mathbb{R}$ carries the conjugation, whose fixed points are the real points, and the central question about it is older than the general theory: how many connected components does the real locus have, and how are they arranged? The answer is the **inequality of Harnack**, $s\le g+1$ for a curve of genus $g$ with $s$ real components, and its refinement by the **separating invariant**, which records whether the real locus cuts the complex curve in two. This article fixes the real structure of a curve, the topology of the real locus, Harnack's inequality with the separating invariant, and the classification by the genus, and it closes the `- * Theory` group.

The article is the curve member of the group: it uses the real points and the real topology of *Real Algebraic Varieties*, the involution and the fixed locus of *Real Structures on Varieties and Galois Descent*, the involution on the cohomology of *The Galois Action on the Cohomology* and *The Involution as an Operator on the Homology* of the category *Geometric Topology* of this Part, and the genus and the Riemann–Roch theory of the written *Algebraic Curves* and *The Riemann–Roch Theorem for Curves*; the trace form and the norm of *The Weil Restriction and the Trace Form* are used for the descent of a curve and the real points of a genus. The finer topology of the real locus — the arrangement of the components as a subset of the complex curve — is the theory of the real algebraic curves of Part IV, and it is named with a deferral; only the count of the components and the separating invariant, which are invariants of the genus, are proved here.

Throughout $C$ is a smooth projective curve of genus $g$ over $\mathbb{R}$, $C_{\mathbb{C}} = C\times_{\mathbb{R}}\mathbb{C}$ its complexification, $\sigma$ the conjugation of $C_{\mathbb{C}}$, $C(\mathbb{R})$ the real points and $s$ their number of connected components. The genus is $g = \dim_{\mathbb{R}}H^1(C,\mathcal{O}_C)$ for the smooth curve, equal to the topological genus of the compact surface $C(\mathbb{C})$ by *Algebraic Curves*.

## Real Structures on a Curve

### The Conjugation and the Real Locus

**Definition.** A **real curve** is a smooth projective curve $C$ over $\mathbb{R}$. Its **real structure** is the conjugation $\sigma$ of $C_{\mathbb{C}}$ over $\mathbb{C}/\mathbb{R}$ of *Real Structures on Varieties and Galois Descent*, and its **real locus** is the fixed locus
$$
C(\mathbb{R}) = C_{\mathbb{C}}(\mathbb{C})^\sigma ,
$$
the fixed-point set of the involution on the complex points.

**Theorem (the real locus is a compact one-manifold).** For a smooth projective real curve $C$ the real locus $C(\mathbb{R})$ is a compact topological space of dimension one without boundary; it is a finite disjoint union of connected components, each homeomorphic to the circle $S^1$, and their number is the integer $s$ of the article.

*Proof.* On an affine chart the real points are the real solutions of the defining equations, a closed subset of a compact $\mathbb{P}^m(\mathbb{R})$ because $C$ is projective, hence compact; the curve being smooth of dimension one and defined over $\mathbb{R}$, the real points form a real one-dimensional manifold without boundary, by the implicit function theorem in its algebraic form: the Jacobian criterion of *Algebraic Curves* gives that the gradient of the defining equation is nonzero at every real point, so the real points are locally the graph of a function of one variable. A compact connected one-manifold without boundary is homeomorphic to the circle $S^1$ by the classification of the compact one-manifolds, in the category *Geometric Topology* below in this Part, and a compact space has finitely many components.

### The Genus and the Complex Curve

**Definition.** The **genus** of $C$ is $g = \dim_{\mathbb{R}}H^1(C,\mathcal{O}_C) = \dim_{\mathbb{C}}H^1(C_{\mathbb{C}},\mathcal{O})$, the arithmetic genus of the smooth curve, equal to the topological genus of the compact real two-manifold $C(\mathbb{C})$ by the Riemann–Roch theorem of *The Riemann–Roch Theorem for Curves*.

**Proposition (the Euler characteristic and the genus).** The complex curve $C_{\mathbb{C}}$ is a compact connected real two-manifold of Euler characteristic $2-2g$, its first Betti number is $2g$, and the real locus satisfies the congruences of the mod-two intersection form; the genus is the invariant of the complexification, and the real structure is the involution that the genus alone does not determine.

*Proof.* The real two-manifold $C(\mathbb{C})$ has genus $g$ by the definition and the Riemann–Roch theorem, so its Euler characteristic is $2-2g$ and its first Betti number is $2g$ by *CW Complexes and Cellular Approximation* and *Simplicial and Singular Homology*; the mod-two intersection form on $H_1$ is the nondegenerate form of the closed surface of *Poincaré Duality*, preserved by the conjugation, and the real locus represents the fixed part in the sense of the next section.

## The Real Locus and Harnack's Inequality

### The Fixed Part and the Separating Invariant

**Definition.** The real locus is **separating** when $C(\mathbb{C})\setminus C(\mathbb{R})$ has two connected components, and **nonseparating** when it has one; the **separating invariant** is
$$
a = \begin{cases} 0 & \text{when } C(\mathbb{R}) \text{ is separating,} \\ 1 & \text{when } C(\mathbb{R}) \text{ is nonseparating.}\end{cases}
$$
Equivalently, $a=0$ when every component of $C(\mathbb{R})$ has a neighbourhood whose complement has two parts inside $C(\mathbb{C})$, and $a=1$ when some component does not separate the complex curve.

**Proposition (the invariant from the homology).** The conjugation acts on the homology $H_1(C(\mathbb{C}),\mathbb{Z}/2)$ of the compact surface, and the separating invariant records the action on the highest exterior power: $a = 1$ exactly when the conjugation acts as the identity on some nonzero class of the homology.

*Proof.* The conjugation is an orientation-reversing involution of the compact surface $C(\mathbb{C})$, and the mod-two intersection form is preserved by it; a real component is separating exactly when its homology class is orthogonal to its image under the intersection form, and the action on the highest exterior power of the homology is the determinant, which is the identity precisely in the nonseparating case. This is the Smith theory of *The Involution as an Operator on the Homology*, in the category *Geometric Topology* below in this Part.

### Harnack's Inequality

**Theorem (Harnack).** Let $C$ be a smooth projective real curve of genus $g$ with $s$ connected components of the real locus. Then
$$
s\le g+1 ,
$$
and if the real locus is nonseparating, that is $a=1$, then $s\le g$. In particular a real curve of genus $g$ has at most $g+1$ real components, and the bound is attained only in the separating case.

*Proof.* The conjugation is an orientation-reversing involution of the compact surface $C(\mathbb{C})$, its fixed set is the real locus, and the quotient $\Sigma = C(\mathbb{C})/\sigma$ is a compact surface with $s$ boundary components, one over each real component. The Riemann–Hurwitz formula for the quotient by an involution of a surface reads
$$
\chi\bigl(C(\mathbb{C})\bigr) = 2\,\chi(\Sigma) - \chi\bigl(C(\mathbb{R})\bigr) ,
$$
and the Euler characteristics are $\chi(C(\mathbb{C})) = 2-2g$ and $\chi(C(\mathbb{R})) = 0$ because the real locus is a disjoint union of circles, so $\chi(\Sigma) = 1-g$. If $\Sigma$ is orientable of genus $g'$, then $\chi(\Sigma) = 2-2g'-s$ and
$$
g = 2g' + s - 1, \qquad s = g+1-2g'\le g+1 ,
$$
with equality exactly when $g'=0$. If $\Sigma$ is nonorientable, with $k\geq1$ crosscaps, then $\chi(\Sigma) = 2-k-s$ and $s = g+1-k\le g$. The real locus separates $C(\mathbb{C})$ exactly when the quotient is orientable, so the nonseparating case is the nonorientable one and gives $s\le g$. This is the Smith theory of *The Involution as an Operator on the Homology* and of the classification of the involutions on surfaces, both in the category *Geometric Topology* below in this Part.

**Corollary (the extremal case).** A curve with $s = g+1$ is called an **M-curve**; its real locus separates the complex curve, $a=0$, because equality in $s = g+1-2g'$ forces $g'=0$ and an orientable quotient, and it realises the maximum of Harnack. A curve with $s = g$ and nonorientable quotient, that is nonseparating, also occurs, so the two bounds $s\le g+1$ and $s\le g$ of the separating and the nonseparating cases are exact.

*Proof.* The equality in the separating case forces $g'=0$ by the formula $s=g+1-2g'$ of the proof; the nonseparating case gives $s = g+1-k$ with $k\ge1$, so $s=g$ is attained when $k=1$. The examples of the next section exhibit both.

## The Involution and the Cohomology of the Curve

### The Action on the Cohomology

**Theorem (the eigenspaces of the conjugation on the curve).** On the cohomology of the structure sheaf the conjugation acts semilinearly, and in degree one
$$
H^1(C_{\mathbb{C}},\mathcal{O}) = H^1_+\oplus H^1_- , \qquad H^1_+\cong H^1(C,\mathcal{O}), \qquad \dim_{\mathbb{C}}H^1 = \dim_{\mathbb{R}}H^1_+ = g ,
$$
the $(+1)$-eigenspace being the cohomology of the real curve and the $(-1)$-eigenspace its conjugate.

*Proof.* This is the eigenspace theorem of *The Galois Action on the Cohomology* applied to the curve, with the $(+1)$-eigenspace identified with the cohomology of the descended real curve and $H^1_-=iH^1_+$; the dimension is the genus $g$ by the definition.

**Remark (the trace form and the function field).** The function field $\mathbb{R}(C)$ of the real curve is the fixed field of the conjugation on $\mathbb{C}(C)$, so it is the descended field of the real structure; the trace form of *The Weil Restriction and the Trace Form* is positive definite on the real part and pairs the cohomology with itself, and the norm of a function is the invariant used to descend the divisors and the functions. The count $s$ and the invariant $a$, however, are read from the homology and the cohomology, as above, and not from the trace form alone.

### The Classification by the Genus

**Theorem (the possible numbers of the components).** For a smooth projective real curve of genus $g$ the number $s$ of the real components takes the values
$$
s\in\{0,1,\ldots,g+1\}
$$
subject to $s\le g$ when the real locus is nonseparating, and every such value is realised: for each $g$ and each admissible pair $(s,a)$ there is a smooth projective real curve of type $(s,a)$.

*Proof.* The bounds are Harnack's inequality and the nonseparating refinement; the realisation is by the construction of the real curves with the prescribed type, part of the classification theory of the real algebraic curves, whose finer invariants (the arrangement of the components in the complex curve) are the object of Part IV. This article records the coarse classification by the genus, the number of the components and the separating invariant, and defers the finer.

**Corollary (the moduli of the real curves).** The real structures of a complex curve of genus $g$ are the involutions of the curve of the antiholomorphic type, and they are classified by the invariants $(s,a)$ together with the finer arrangement; the set of the real forms of the curve is the set of the conjugations modulo the automorphisms, and it is the object of *Real Structures on Varieties and Galois Descent* and of the arithmetic of the curves.

*Proof.* The real forms are the conjugations by the theorem of real forms of *Real Forms and the Descent of an Algebra* applied to the function field; the classification by $(s,a)$ is the coarse classification above, and the remaining invariants are those of the arrangement. The statement is the curve instance of the descent, and its finer version is deferred.

## Examples

### The Genus Zero and One

**Example (the genus zero).** A real curve of genus $g=0$ is a form of the projective line, and Harnack gives $s\le1$. The split form is $\mathbb{P}^1_{\mathbb{R}}$, whose real locus is the copy of $S^1$ and $s=1$, $a=0$; the twisted form is the anisotropic conic $x^2+y^2+z^2=0$, whose real locus is empty, $s=0$, $a=0$. The two real forms of the projective line have been met in *Real Structures on Varieties and Galois Descent*.

**Example (the genus one).** A real curve of genus $g=1$ is a real elliptic curve, a form of a complex torus, and Harnack gives $s\le2$ with the nonseparating refinement $s\le1$ in the nonseparating case. All three values occur: $s=0$ for a curve with no real points, $s=1$ with the real locus a single component and $a=1$, and $s=2$ with two components and $a=0$; the last two are the two topological types of the real elliptic curves, distinguished by the separating invariant. The traces of the Frobenius and the zeta function of the curve over a finite field are the arithmetic of *The Frobenius Operator*.

### A Curve of Higher Genus

**Example (the M-curves).** For every $g$ there are real curves with $s = g+1$ components, the M-curves, whose real locus is a disjoint union of $g+1$ circles separating the complex curve; the Harnack bound is attained. For $g=2$ the bound is $s\le3$, and the curves with $s=3$ are the M-curves of genus two with three components; the curves with $s=2$ have the separating or the nonseparating real locus according to the arrangement.

**Example (the nonseparating curves).** For every $g\geq1$ there are real curves with $s=g$ and nonseparating real locus, the simplest being the genus one with $s=1$: a single circle that does not separate the complex torus. The bound $s\le g$ of the nonseparating case is thus the exact one, and it is strictly smaller than Harnack's bound by one, which is the contribution of the separating invariant.

## Summary

A **real curve** is a smooth projective curve $C$ over $\mathbb{R}$ with the conjugation $\sigma$ of $C_{\mathbb{C}}$; its real locus $C(\mathbb{R}) = C_{\mathbb{C}}(\mathbb{C})^\sigma$ is a compact one-dimensional manifold without boundary, a finite disjoint union of $s$ components each homeomorphic to the circle, and the **genus** is $g = \dim_{\mathbb{R}}H^1(C,\mathcal{O})$, the topological genus of the compact surface $C(\mathbb{C})$. The real locus is **separating** or **nonseparating** according to the number of the components of its complement in $C(\mathbb{C})$, with the invariant $a\in\{0,1\}$. **Harnack's inequality** is
$$
s\le g+1 ,
$$
with $s\le g$ in the nonseparating case; the extreme curves with $s = g+1$ are the M-curves and separate. The conjugation acts semilinearly on the cohomology, splitting $H^1(C_{\mathbb{C}},\mathcal{O}) = H^1_+\oplus H^1_-$ with $H^1_+\cong H^1(C,\mathcal{O})$ and $\dim_{\mathbb{C}}H^1 = \dim_{\mathbb{R}}H^1_+ = g$, so the cohomology of the real curve is the fixed part; the trace form detects the real points and the sign conditions. The classification by the genus gives the count $s\in\{0,\ldots,g+1\}$ with the nonseparating refinement, every admissible value realised; the finer arrangement of the components is the theory of the real algebraic curves of Part IV and is deferred.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $C$, $C_{\mathbb{C}}$ | smooth projective real curve of genus $g$; its complexification |
| $\sigma$, $C(\mathbb{R})=C_{\mathbb{C}}(\mathbb{C})^\sigma$ | the conjugation; the real locus |
| $s$ | the number of the connected components of $C(\mathbb{R})$ |
| $g=\dim_{\mathbb{R}}H^1(C,\mathcal{O})$ | the genus; the topological genus of $C(\mathbb{C})$ |
| each component $\cong S^1$ | the real locus is a compact one-manifold |
| $a\in\{0,1\}$ | the separating invariant: separating or nonseparating |
| $s\le g+1$ | Harnack's inequality |
| $s\le g$ if $a=1$ | the refinement for the nonseparating case |
| M-curve, $s=g+1$, $a=0$ | the maximal curve; the bound attained |
| $H^1(C_{\mathbb{C}},\mathcal{O})=H^1_+\oplus H^1_-$, $H^1_+\cong H^1(C,\mathcal{O})$ | the eigenspaces of the conjugation; $\dim H^1_+=g$ |
| $s\in\{0,\ldots,g+1\}$ | the possible numbers of the real components |
| arrangement | the finer topology of the real locus; deferred to Part IV |

## Further Reading

- Axel Harnack, *Über die Vielfaltigkeit der ebenen algebraischen Kurven* (Mathematische Annalen 10, 1876), for the inequality $s\le g+1$ and the first classification of the real curves.
- David Hilbert, *Über die Theorie der algebraischen Formen* (Mathematische Annalen 36, 1890), for the sixteenth problem and the place of the real curves.
- George Wilson, *Hilbert's sixteenth problem* (Topology 17, 1978), for the modern treatment of the real curves and the arrangement of the components.
- Nikolaĭ V. Viro, *Real algebraic plane curves: constructions with controlled topology* (Leningrad Mathematical Journal 1, 1990), for the construction of the real curves with the prescribed topology.
- Alexander I. Khovanskii, *Fewnomials* (American Mathematical Society, Translations of Mathematical Monographs 88, 1991), for the real points of a real curve and the fewnomial bounds.
- Eberhard Becker, *On the real spectrum of a ring and its application to semialgebraic geometry* (Bulletin of the American Mathematical Society 83, 1977), for the real spectrum and the real points of a curve.
