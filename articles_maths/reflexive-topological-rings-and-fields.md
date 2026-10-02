
# __Reflexive Topological Rings and Fields__

## Introduction

A topological module is **reflexive** when the canonical map into its double dual is a topological isomorphism: the module is recovered from the continuous linear forms on it, and the recovery is topological, not merely algebraic. This is the finiteness condition of duality theory, and it fails for the standard analytic spaces — the space $\ell^1$, the algebra $C(K)$ of continuous functions, the non-complete spaces — and holds for the finite-dimensional spaces, for the complete valued fields in dimension one, and for the Hilbert spaces. This article treats reflexivity for topological rings and fields: it fixes the dual of a topological module over a base topological field as the module of continuous linear forms with the topology of uniform convergence, defines the canonical map and reflexivity, proves that reflexivity forces completeness and that the finite-dimensional Hausdorff spaces over a complete base are reflexive, states the criterion of the strong dual and the Mackey–Arens theorem for the strong topology, reads reflexivity for the valued fields and their completions, and shows how an isometric involution of the base transfers to the dual and makes the canonical map equivariant.

The article assumes the topological ring, the topological module and the continuity of the operations from *Topological Rings and Fields* and *Topological Modules and Vector Spaces*; the continuous additive operators, the natural pairing and the topology of pointwise convergence from *Operators on a Topological Ring*; the completion, its universal property and the fact that a complete submodule is closed from *The Completion Operator*; the absolute value, the valuation and the completion of a valued field from *Absolute Values, Valuations and Completions*; the residue operator from *The Residue Operator of a Valued Field*; the involution and its extension to the completion from *The Involution and the Completion of a Ring* and *Involutive Valued Fields*. The theory of locally convex spaces, the Hahn–Banach theorem and the Mackey–Arens theorem are quoted where used; the normed duality of operators is *The Involution on Bounded Operators of a Ring* and the Banach–Alaoglu theorem is quoted as the source of the compactness criterion. No measure beyond the Haar measure of a locally compact field and no form beyond the pairing occurs.

Throughout, $K$ is a topological field, complete, non-discrete and with a nontrivial topology; $M$ is a topological $K$-module (a topological vector space over $K$), Hausdorff; the **dual** is

$$
M^* = \operatorname{Hom}_K^c(M, K) ,
$$

the $K$-module of continuous $K$-linear maps, with the **weak-$\ast$ topology** of pointwise convergence and the **strong topology** of uniform convergence on the bounded subsets of $M$; the **bidual** is $M^{**} = (M^*)^*$; and the **canonical map** is

$$
c_M : M\longrightarrow M^{**}, \qquad c_M(m)(f) = f(m) .
$$

## Duals and the Natural Pairing

**Definition.** The **natural pairing** is the bilinear map $\langle \,\cdot\,,\,\cdot\,\rangle : M^*\times M\to K$, $\langle f, m\rangle = f(m)$. The weak-$\ast$ topology on $M^*$ is the initial topology of the maps $f\mapsto f(m)$ for $m\in M$; the strong topology is that of uniform convergence on the bounded subsets of $M$; the **dual topology** is the strong one unless stated otherwise.

**Proposition (the pairing is separating in both variables).** If $M$ is Hausdorff and $K$ is complete, non-discrete and nontrivial, then for every nonzero $m\in M$ there is $f\in M^*$ with $f(m)\neq 0$, and for every nonzero $f\in M^*$ there is $m\in M$ with $f(m)\neq 0$; the pairing is therefore separating in both variables when $M$ is locally convex.

**Proof.** The first statement is the Hahn–Banach theorem applied to the one-dimensional subspace spanned by $m$: a nonzero continuous linear form on $Km$ extends to $M$ when $M$ is locally convex and $K$ complete and nontrivial, so the dual separates points; the second is the definition of a nonzero linear form. Without local convexity the first statement may fail, and the article states the result under that hypothesis.

**Proposition (the canonical map is $K$-linear and continuous).** For a topological module $M$ the canonical map $c_M$ is $K$-linear, and it is continuous when $M^{**}$ carries the weak-$\ast$ topology.

**Proof.** For $f\in M^*$ the assignment $m\mapsto f(m)$ is $K$-linear and continuous by the definition of the dual; hence $c_M$ is $K$-linear, and it is continuous for the weak-$\ast$ topology because each composite $f\circ c_M$ is the continuous map $f$.

## The Canonical Map and Reflexivity

**Definition.** The module $M$ is **semi-reflexive** if $c_M$ is bijective, and **reflexive** if $c_M$ is a topological isomorphism onto $M^{**}$ with the strong topology. A topological ring $R$ is **reflexive** if it is reflexive as a module over itself or, more precisely, if the canonical map of the underlying topological additive group into its double dual is a topological isomorphism; a topological field $F$ is reflexive if it is reflexive as a one-dimensional topological vector space over itself.

**Proposition (injectivity of the canonical map).** The canonical map $c_M$ is injective exactly when the dual separates the points of $M$, that is when $M$ is **torsionless**; the kernel of $c_M$ is the intersection of the kernels of the elements of $M^*$, which is closed and is the closure of zero in the weak topology.

**Proof.** $c_M(m) = 0$ means $f(m) = 0$ for all $f\in M^*$, so the kernel is the intersection of the kernels of the continuous linear forms, an intersection of closed sets, hence closed. It is zero exactly when the dual separates points.

**Theorem (reflexivity forces completeness).** If $M$ is reflexive then $M$ is complete for its topology; more generally, a semi-reflexive locally convex space is weakly complete, and a reflexive space is complete for the original topology.

**Proof.** The bidual $M^{**}$ with the weak-$\ast$ topology is a closed subspace of a product of copies of $K$, hence complete; if $c_M$ is a topological isomorphism, the completeness of the bidual transfers to $M$, so $M$ is complete. The semi-reflexive case is the same argument for the weak topology, since a closed subspace of a product is weakly complete.

**Theorem (the finite-dimensional case).** Let $M$ be a finite-dimensional Hausdorff topological vector space over the complete non-discrete field $K$. Then $M$ is reflexive, and the canonical map is a homeomorphism onto the strong bidual.

**Proof.** For $M = K^n$ the dual is $K^n$ and the bidual is $K^n$, and the canonical map is the identity matrix, hence bijective; every Hausdorff vector space topology on a finite-dimensional space over a complete non-discrete field is the product topology, so the canonical map is a homeomorphism. The general finite-dimensional case follows by choosing a basis and transporting the topology, which is uniquely determined by the finite dimension.

**Corollary (complete valued fields are reflexive).** A complete valued field $F$, regarded as a one-dimensional topological vector space over itself, is reflexive; a general valued field is reflexive exactly when it is complete, so a non-complete valued field is not reflexive.

**Proof.** Dimension one over the complete base $F$ is the finite-dimensional case; a non-complete valued field fails to be complete, hence fails to be reflexive by the completeness theorem.

## Topologies on the Dual

**Theorem (the strong dual and the Mackey–Arens theorem, quoted).** On the dual $M^*$ of a locally convex space the strong topology is the topology of uniform convergence on the bounded subsets of $M$, and the Mackey–Arens theorem states that the topologies on $M$ for which the dual is $M^*$ are exactly those of uniform convergence on the weakly bounded sets, the finest being the **Mackey topology**. The strong dual $M^*$ is complete when $M$ is complete and metrisable.

**Proof.** Quoted; the strong topology is by definition the topology of uniform convergence on bounded sets, and the Mackey–Arens theorem characterises the admissible topologies. The completeness of the strong dual for a complete metrisable $M$ is the Banach–Steinhaus theorem.

**Corollary (reflexivity in terms of the strong dual).** A locally convex space $M$ is reflexive exactly when it is semi-reflexive and its strong dual is barrelled; when $M$ is reflexive, the strong dual of $M^*$ is $M$ under the canonical identification, and the strong topology of the bidual is the topology of uniform convergence on the bounded subsets of $M^*$.

**Proof.** Quoted from the standard theory of locally convex spaces: semi-reflexivity plus the barrelled property of the strong dual is the standard criterion, and the identification of the bidual with $M$ follows.

## The Involutive Duality

**Theorem (an isometric involution transfers to the dual and makes the canonical map equivariant).** Let $R$ be a topological ring with a continuous involution $\sigma$, let $M$ be a topological $R$-module, and give the dual $M^* = \operatorname{Hom}_K^c(M,K)$ the module structure twisted by $\sigma$,

$$
(r\cdot f)(m) = f(\sigma(r)\,m) ,
$$

when $\sigma$ is an anti-automorphism of $R$ acting on $M$ by a compatible anti-action, or $(r\cdot f)(m) = f(r\,m)$ in the automorphism case. Then $\sigma$ induces a continuous involution $\sigma^*$ of $M^*$ with $\sigma^*\sigma^* = \mathrm{id}$, the bidual carries the corresponding involution $\sigma^{**}$, and the canonical map is equivariant, $c_M\circ\sigma = \sigma^{**}\circ c_M$ when $\sigma$ acts on $M$, so reflexivity is compatible with the involutive structure.

**Proof.** The twisted module structure is well defined because $\sigma$ is an automorphism or anti-automorphism and preserves the continuity of the forms; $\sigma^*f = f\circ\sigma$ is continuous, additive and involutive, and it is continuous for the weak-$\ast$ and strong topologies because $\sigma$ is a homeomorphism of $M$. The equivariance of $c_M$ is $\langle\sigma^*f, \sigma m\rangle = \langle f, m\rangle$, checked directly from the definition.

**Corollary (reflexive involutive topological rings).** A reflexive topological ring with a continuous involution has a continuous involution on its bidual, and when the ring is reflexive the involution of the ring identifies with the involution of the bidual under the canonical isomorphism; in particular the fixed and skew parts of the involution are preserved by reflexivity, and the completion of an involutive topological ring of *The Involution and the Completion of a Ring* is reflexive exactly when the ring is complete.

**Proof.** Combine the equivariance with the identification of $R$ and $R^{**}$ under reflexivity; the fixed and skew parts are the eigenspaces of the involution, preserved under a topological isomorphism, and the completion statement is the completeness theorem applied to the involutive ring.

## Examples

**Example (the complete valued fields).** A complete valued field $F$ is reflexive as a one-dimensional space over itself; a non-complete valued field, such as $\mathbb{Q}$ with the $p$-adic absolute value or $\mathbb{R}$ with the usual topology embedded in $k(x)$, is not reflexive. The completion of a valued field is its reflexive hull in dimension one.

**Example (the finite-dimensional spaces over a complete field).** Every finite-dimensional Hausdorff space over $\mathbb{C}$ or $\mathbb{Q}_p$ is reflexive; the double dual is the original space and the canonical map is the identity in a basis.

**Example (the Hilbert spaces).** A Hilbert space $H$ is reflexive; the Riesz representation theorem identifies $H^*$ with $H$ and the canonical map with the identity under the conjugate-linear identification, and the involution of the scalar field transfers to the antilinear structure. The spaces $\ell^1$ and $c_0$ are mutually dual and neither is reflexive, which is the standard failure of reflexivity in the normed setting.

**Example (the field of formal Laurent series).** The field $k((t))$ with the $t$-adic topology is complete, hence reflexive as a one-dimensional space over itself; the involution $t\mapsto t^{-1}$ of *Involutive Valued Fields* is not continuous, so it does not transfer to the dual, which shows that the isometry hypothesis in the involutive duality theorem is genuine.

## Summary

For a topological module $M$ over a complete non-discrete topological field $K$, the dual $M^*$ is the module of continuous linear forms with the weak-$\ast$ and strong topologies, and the canonical map $c_M : M\to M^{**}$, $c_M(m)(f) = f(m)$, is $K$-linear and continuous; $M$ is semi-reflexive when $c_M$ is bijective and reflexive when it is a topological isomorphism. The map is injective exactly when the dual separates points; its kernel is a closed subspace; reflexivity forces completeness; and every finite-dimensional Hausdorff space over a complete non-discrete field is reflexive, so the complete valued fields are reflexive in dimension one and the non-complete ones are not. The strong topology is the topology of uniform convergence on bounded sets, and the Mackey–Arens theorem describes the admissible topologies; a reflexive space is identified with the strong dual of its strong dual.

An isometric involution of the acting ring transfers to the dual and to the bidual, and the canonical map is equivariant, so reflexivity is compatible with an involutive structure; the reflexive hull of an involutive valued field is its completion, and the involution extends to it. The standard failures — $\ell^1$, $c_0$, the non-complete valued fields, the non-continuous involution $t\mapsto t^{-1}$ — mark the boundary of the theory, and the normed duality of operators is the neighbouring subject.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$ | Complete non-discrete topological field |
| $M$, $M^*$, $M^{**}$ | Module, dual, bidual |
| $\langle f, m\rangle = f(m)$ | The natural pairing |
| Weak-$\ast$ topology | Pointwise convergence on $M$ |
| Strong topology | Uniform convergence on bounded subsets |
| $c_M(m)(f) = f(m)$ | The canonical map |
| Semi-reflexive | $c_M$ bijective |
| Reflexive | $c_M$ a topological isomorphism |
| Bounded subsets | The sets defining the strong topology |
| $\sigma, \sigma^*, \sigma^{**}$ | The involution and its transfers to the duals |
| $\ell^1$, $c_0$ | The standard non-reflexive pair |

## Further Reading

- Nicolas Bourbaki, *Topological Vector Spaces, Chapters 1–5* (Springer, 1987), for duality, the strong topology, the Mackey–Arens theorem and reflexivity.
- John B. Conway, *A Course in Functional Analysis*, Graduate Texts in Mathematics 96 (Springer, 2nd ed. 1990), for reflexivity of Banach and Hilbert spaces and the examples $\ell^1$ and $c_0$.
- Helmut H. Schaefer, *Topological Vector Spaces*, Graduate Texts in Mathematics 3 (Springer, 2nd ed. 1999), for the strong dual, barrel spaces and the reflexivity criterion.
- Seth Warner, *Topological Fields* (North-Holland, 1989), for the topology of a valued field and its completion.
- Jean-Pierre Serre, *Local Fields* (Springer, 1979), for the locally compact fields and their duality.
