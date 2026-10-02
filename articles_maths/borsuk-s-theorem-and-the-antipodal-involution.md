# __Borsuk's Theorem and the Antipodal Involution__

## Introduction

The antipodal involution $x \mapsto -x$ of the sphere $S^{n}$ is the standard free involution, and its equivariant maps have a rigidity that no other involution of the sphere shares: a continuous map of the sphere to a lower-dimensional sphere that commutes with the antipodal involutions cannot exist, and a continuous map of the sphere to Euclidean space that is **odd** must vanish somewhere. These are the statements of **Borsuk's theorem**, and they are the first place in the corpus where the equivariant structure of the antipodal involution forces a topological conclusion. The article states the theorem in its several equivalent forms, proves the case of the circle $S^{1}$ completely, and shows how the general case is a computation of the equivariant topology of the quotient: an odd map $S^{n} \to S^{n-1}$ would descend to a map $\mathbb{RP}^{n} \to \mathbb{RP}^{n-1}$ whose effect on the mod-$2$ cohomology is impossible.

The article is the last of the group `- * Theory` and it uses the free involution and the orbit space of *The Orbit Space of a Free Involution*, the equivariant maps of *Equivariant Maps and Equivariant Homotopy*, and the quotient description of *Spaces with an Involution and the Orbit Space*. The computation of the mod-$2$ cohomology of real projective space and the degree of a map of spheres belong to the algebraic topology of this Part, and the general proof of Borsuk's theorem is cited there; the equivariant reduction that this article gives is complete, and only the cohomological input is deferred.

Only the topology and the real numbers are used, together with the intermediate value theorem of the analysis of Part I. No metric is chosen beyond the standard one on the sphere, and the theorem is used later for its equivariant content rather than for any measure or length.

## The Antipodal Involution and Odd Maps

### Odd Maps as Equivariant Maps

**Definition.** The **antipodal involution** of the sphere $S^{n} = \{x \in \mathbb{R}^{n+1} : |x| = 1\}$ is the map $\alpha(x) = -x$. A map $f : S^{n} \to \mathbb{R}^{k}$ is **odd**, or **antipodal**, when

$$
f(-x) = -f(x) \qquad (x \in S^{n}) .
$$

**Proposition.** The antipodal involution is a free continuous involution of $S^{n}$, and the odd maps $S^{n} \to \mathbb{R}^{k}$ are exactly the equivariant maps for the antipodal involution of $S^{n}$ and the antipodal involution of $\mathbb{R}^{k}$. The odd maps $S^{n} \to S^{k}$ are the equivariant maps of the spheres.

**Proof.** Freeness is $x \neq -x$ on the sphere; continuity is that of the restriction of the linear map $x \mapsto -x$. An equivariant map to $\mathbb{R}^{k}$ with the antipodal involution is a continuous $f$ with $f(-x) = -f(x)$, which is the definition of oddness; the restriction to spheres is equivariant when the target is a sphere.

### The Sphere and Its Quotient

**Theorem.** The orbit space of the antipodal involution of $S^{n}$ is real projective space $\mathbb{RP}^{n}$, the orbit map $S^{n} \to \mathbb{RP}^{n}$ is a two-fold covering, and it is the universal two-fold covering of $\mathbb{RP}^{n}$ in the sense that every two-fold covering of $\mathbb{RP}^{n}$ is a pullback of it.

**Proof.** The orbit space is projective space by definition; the covering statement is that of *The Orbit Space of a Free Involution* for the free involution of a Hausdorff space; the universal property is that of the classifying space $\mathbb{RP}^{\infty}$ of *Two-Fold Coverings and the Borel Construction*, restricted to the finite projective space, where every two-fold covering is pulled back from the finite universal covering $S^{n} \to \mathbb{RP}^{n}$.

**Corollary.** An odd map $S^{n} \to S^{n-1}$ descends to a continuous map $\mathbb{RP}^{n} \to \mathbb{RP}^{n-1}$ of the quotients, and conversely a continuous map $\mathbb{RP}^{n} \to \mathbb{RP}^{n-1}$ lifts to an odd map $S^{n} \to S^{n-1}$.

**Proof.** The descent is the functoriality of the orbit space for equivariant maps, and the lift is the universal property of the covering $S^{n-1} \to \mathbb{RP}^{n-1}$ applied to the composite $\mathbb{RP}^{n} \to \mathbb{RP}^{n-1}$, using that the two-fold covering of $\mathbb{RP}^{n}$ is the pullback.

## Borsuk's Theorem

### The Statements

**Theorem (Borsuk).** The following are equivalent.

1. There is no continuous odd map $S^{n} \to S^{n-1}$.
2. For every continuous $f : S^{n} \to \mathbb{R}^{n}$ there is $x \in S^{n}$ with $f(x) = f(-x)$.
3. Every continuous odd map $f : S^{n} \to \mathbb{R}^{n}$ has a zero.
4. There is no continuous map $\mathbb{RP}^{n} \to \mathbb{RP}^{n-1}$ that induces an isomorphism on the first cohomology with $\mathbb{Z}/2$ coefficients.

The statement (2) is the **Borsuk–Ulam theorem**, and (1) is its equivariant form.

### The Equivalences

**Theorem.** The statements (1), (2) and (3) are equivalent, and (4) is the quotient form of (1).

**Proof.** (3) $\Rightarrow$ (2): given $f : S^{n} \to \mathbb{R}^{n}$, the map $g(x) = f(x) - f(-x)$ is continuous and odd, and $g(x) = 0$ is $f(x) = f(-x)$. (2) $\Rightarrow$ (3): an odd $g$ with $g(x) = g(-x)$ satisfies $g(x) = -g(x)$, so $g(x) = 0$. (1) $\Leftrightarrow$ (3): if an odd $g : S^{n} \to \mathbb{R}^{n}$ has no zero, then $x \mapsto g(x)/|g(x)|$ is a continuous odd map $S^{n} \to S^{n-1}$, contradicting (1); conversely an odd map $S^{n} \to S^{n-1}$ has no coincidence with itself under the antipodal involution, since $h(x) = h(-x) = -h(x)$ would give $h(x) = 0$, impossible for a map into the sphere, so it witnesses the failure of (2) and (3). Finally (4) is (1) read through the quotient, by the descent and lifting of odd maps to maps of projective spaces.

### The Case of the Circle

**Theorem.** Borsuk's theorem holds for $n = 1$: there is no continuous odd map $S^{1} \to S^{0}$, and every continuous odd $f : S^{1} \to \mathbb{R}$ has a zero.

**Proof.** For the second statement, let $f : S^{1} \to \mathbb{R}$ be continuous and odd. Choose $x_{0} \in S^{1}$; if $f(x_{0}) = 0$ there is nothing to prove, so suppose $f(x_{0}) \neq 0$. Let $\gamma : [0,1] \to S^{1}$ be a continuous path from $\gamma(0) = x_{0}$ to $\gamma(1) = -x_{0}$, for instance the parametrisation of a semicircle. Then $f \circ \gamma$ is continuous, $(f\circ\gamma)(0) = f(x_{0})$ and $(f\circ\gamma)(1) = f(-x_{0}) = -f(x_{0})$; the two values are nonzero with opposite signs, so the intermediate value theorem gives $t$ with $(f\circ\gamma)(t) = 0$, and $f$ has a zero. For the first statement, a continuous map $h : S^{1} \to S^{0} = \{-1,1\}$ has image in a discrete space adjoined to the connected space $S^{1}$, hence is constant, and an odd constant is impossible, since $c = h(x) = -h(-x) = -c$ forces $c = 0$, which is not in $S^{0}$.

**Remark.** The case $n = 1$ is the whole of the theorem that can be proved with the intermediate value theorem; the cases $n \geq 2$ require the degree of a self-map of the sphere or, equivalently, the cohomology of the projective spaces, and they are proved in the algebraic topology of this Part.

## Borsuk's Antipodal Theorem

### The Covering Statement

**Theorem (Borsuk's antipodal theorem).** Let $F_{1}, \ldots, F_{n+1}$ be closed subsets of $S^{n}$ with $S^{n} = F_{1} \cup \cdots \cup F_{n+1}$. Then one of the sets contains an antipodal pair $\{x, -x\}$.

**Proof sketch.** Suppose none of the sets contains an antipodal pair, so that $F_{i} \cap (-F_{i}) = \emptyset$ for every $i$, and define

$$
g_{i}(x) = d(x, F_{i}) - d(-x, F_{i}) \qquad (i = 1, \ldots, n), \qquad g(x) = (g_{1}(x), \ldots, g_{n}(x)) \in \mathbb{R}^{n},
$$

with $d$ the distance on the sphere. Each $g_{i}$ is continuous and odd, hence so is $g$, and Borsuk–Ulam in the form (3) gives $x$ with $g(x) = 0$, that is, $d(x, F_{i}) = d(-x, F_{i})$ for every $i \leq n$. Since the sets cover, $x \in F_{j}$ for some $j$ and $-x \in F_{k}$ for some $k$. If $j \leq n$ then $d(x, F_{j}) = 0$, hence $d(-x, F_{j}) = 0$ and $-x \in F_{j}$ because $F_{j}$ is closed, giving an antipodal pair in $F_{j}$. If $k \leq n$ the same argument with $x$ and $-x$ interchanged gives an antipodal pair in $F_{k}$. The only remaining case is $j = k = n+1$, and then both $x$ and $-x$ lie in $F_{n+1}$, again an antipodal pair. Every case contradicts the supposition, so some set contains an antipodal pair.

### The Lusternik–Schnirelmann Form

**Theorem.** Borsuk's antipodal theorem is equivalent to Borsuk–Ulam: each implies the other. Equivalently, the covering statement for $n+1$ closed sets is the same assertion as the non-existence of an odd map $S^{n} \to S^{n-1}$.

**Proof.** The proof of the antipodal theorem from Borsuk–Ulam is the argument above; the reverse implication is the standard reduction: an odd map $h : S^{n} \to S^{n-1}$ composed with the coordinate functions produces $n$ continuous functions on $S^{n}$ that, together with the set where they all vanish, give a cover by $n+1$ sets without an antipodal pair, contradicting the antipodal theorem. The details are the standard ones and are given in the references.

**Remark.** The number $n+1$ is sharp: the sphere $S^{n}$ can be covered by $n+2$ closed sets none of which contains an antipodal pair, and the equivariant computation that proves this is the statement that the Lusternik–Schnirelmann category of $\mathbb{RP}^{n}$ is $n+1$. The category is a homotopy invariant of the quotient, and its computation belongs to the algebraic topology of this Part.

## The Proof by Equivariant Topology

The general form of Borsuk's theorem is proved by passing to the quotient and computing a cohomological invariant, and the article records the shape of that proof so that the reader can see exactly where the deferred input enters.

**Theorem (shape of the proof; the computation deferred).** There is no continuous odd map $S^{n} \to S^{n-1}$ for $n \geq 1$. Suppose there were one; it would descend to a continuous map $\varphi : \mathbb{RP}^{n} \to \mathbb{RP}^{n-1}$. The pullback of the two-fold covering $S^{n-1} \to \mathbb{RP}^{n-1}$ along $\varphi$ is the nontrivial covering $S^{n} \to \mathbb{RP}^{n}$, because the descent comes from the odd map and the odd map lifts it; hence the induced map on the first cohomology with $\mathbb{Z}/2$ coefficients is nonzero, and since both groups have two elements it sends the generator to the generator. The cohomology with $\mathbb{Z}/2$ coefficients of $\mathbb{RP}^{m}$ is a polynomial algebra on one class $\omega$ of degree one, truncated at $\omega^{m+1} = 0$. Naturality of the cup product gives $\varphi^{*}(\omega_{n-1}^{n}) = (\varphi^{*}\omega_{n-1})^{n} = \omega_{n}^{n}$, but $\omega_{n-1}^{n} = 0$ in $H^{n}(\mathbb{RP}^{n-1};\mathbb{Z}/2)$ because the ring is truncated below degree $n$, while $\omega_{n}^{n} \neq 0$ in $H^{n}(\mathbb{RP}^{n};\mathbb{Z}/2)$; the contradiction proves the theorem.

**Proof of the equivariant reduction.** The reduction is the corollary of the descent and lifting of odd maps; the cohomological computation of the projective spaces and the naturality of the cup product are the deferred input, and with them the contradiction is immediate. An alternative proof uses the degree of a self-map of the sphere: an odd map $S^{n} \to S^{n}$ has odd degree, and an odd map $S^{n} \to S^{n-1}$ extended to the ball gives a null-homotopy that the degree forbids; this is the classical route and it uses the same deferred theory.

**Remark.** The theorem is the first genuinely equivariant computation of the corpus, and its content is that the antipodal involution is not a symmetry the sphere can shed: the quotient $\mathbb{RP}^{n}$ remembers the involution through its cohomology, and the remembering forbids the odd maps to lower spheres. The applications of the theorem in this Part and in the applications articles rest on this rigidity.

## Summary

The antipodal involution of the sphere is free, and its orbit space is real projective space; the odd maps, which are the equivariant maps for the antipodal involutions, descend to maps of the projective spaces and lift from them. Borsuk's theorem has four equivalent forms: the non-existence of a continuous odd map $S^{n} \to S^{n-1}$; the Borsuk–Ulam coincidence statement that every continuous $f : S^{n} \to \mathbb{R}^{n}$ has $f(x) = f(-x)$; the vanishing of every continuous odd map into $\mathbb{R}^{n}$; and the non-existence of a map $\mathbb{RP}^{n} \to \mathbb{RP}^{n-1}$ that is an isomorphism on the first $\mathbb{Z}/2$ cohomology. The equivalences are proved, the case $n = 1$ is proved with the intermediate value theorem, and the general case is reduced to the computation of the $\mathbb{Z}/2$ cohomology of the projective spaces, which belongs to the algebraic topology of this Part. Borsuk's antipodal theorem, that $n+1$ closed sets covering $S^{n}$ contain an antipodal pair, is equivalent to Borsuk–Ulam, and the number $n+1$ is the Lusternik–Schnirelmann category of $\mathbb{RP}^{n}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S^{n}$ | The unit sphere in $\mathbb{R}^{n+1}$; $S^{0} = \{-1,1\}$ |
| $\alpha(x) = -x$ | The antipodal involution |
| odd map | $f(-x) = -f(x)$; an equivariant map for the antipodal involutions |
| $\mathbb{RP}^{n}$ | $S^{n}/\alpha$; the orbit space of the antipodal involution |
| $S^{n} \to \mathbb{RP}^{n}$ | The universal two-fold covering of the projective space |
| Borsuk–Ulam | $\forall f : S^{n} \to \mathbb{R}^{n}$ continuous, $\exists x : f(x) = f(-x)$ |
| odd vanishing | Every continuous odd $g : S^{n} \to \mathbb{R}^{n}$ has a zero |
| no odd map | No continuous odd $S^{n} \to S^{n-1}$ |
| antipodal theorem | $n+1$ closed sets covering $S^{n}$ contain an antipodal pair |
| LS category | $\mathrm{cat}(\mathbb{RP}^{n}) = n+1$; the sharpness of $n+1$ |
| $H^{*}(\mathbb{RP}^{m};\mathbb{Z}/2)$ | Truncated polynomial ring $\mathbb{Z}/2[\omega]/(\omega^{m+1})$ |

## Further Reading

- Karol Borsuk, "Drei Sätze über die $n$-dimensionale euklidische Sphäre", *Fundamenta Mathematicae* 20 (1933), 177–190, for the original statements.
- L. Lusternik and L. Schnirelmann, *Méthodes topologiques dans les problèmes variationnels* (Hermann, 1934), for the category and the covering form of the antipodal theorem.
- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002), for the cohomology of projective space, the degree of a map of spheres, and the proof of Borsuk–Ulam.
- James R. Munkres, *Elements of Algebraic Topology* (Addison-Wesley, 1984), for the mod-$2$ cohomology of $\mathbb{RP}^{n}$ and the cup-product proof of Borsuk–Ulam.
- Glen E. Bredon, *Topology and Geometry* (Springer, 1993), for Borsuk–Ulam, the equivariant formulation and the Lusternik–Schnirelmann category.
- Jiří Matoušek, *Using the Borsuk–Ulam Theorem* (Springer, 2nd ed. 2008), for the applications and for several proofs of the theorem.
