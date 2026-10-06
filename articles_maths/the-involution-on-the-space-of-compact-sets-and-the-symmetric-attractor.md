# __The Involution on the Space of Compact Sets and the Symmetric Attractor__

## Introduction

An isometric involution $\sigma$ of a metric space $X$ acts on the **space of the nonempty compact subsets** $\mathcal{K}(X)$ by the image,

$$
\Sigma(A) = \sigma(A) , \qquad A \in \mathcal{K}(X) ,
$$

and because $\sigma$ is an isometry and $\sigma^2 = \operatorname{id}$, the map $\Sigma$ is again an involutive isometry, now of the Hausdorff metric space $(\mathcal{K}(X), d_H)$. The fixed points of $\Sigma$ are the **compact sets invariant under $\sigma$**, and the closed set $\operatorname{Fix}\Sigma$ of them is the symmetric part of the space of the compact sets. When an iterated function system is reversible by $\sigma$, the Hutchinson operator $F$ commutes with $\Sigma$, and the commutation produces the central statement of the article: the attractor — the unique fixed point of $F$ — is automatically a fixed point of the involution, so the attractor of a reversible system is **symmetric**. The same involution acts on the measures, through the pushforward, and the self-similar measure of the compatible weights is symmetric in the same sense; the pair of the symmetric attractor and the symmetric measure is the operator form of the symmetry.

This article is the operator side of the involution and closes the category. It defines the induced involution $\Sigma$ on $\mathcal{K}(X)$, proves that it is an isometry, identifies its fixed set, proves that the commutation of $\Sigma$ with the Hutchinson operator forces the attractor to be symmetric and gives an alternative existence proof by the restriction to $\operatorname{Fix}\Sigma$, and treats the adjoint action on the measures with the symmetric self-similar measure. The geometry of the symmetric fractals, the fixed set and the quotient is *Symmetric Fractals and the Involution*; the Hutchinson operator and its adjoint on the measures are *The Hutchinson Operator and Its Adjoint*; and the reversible systems and the symmetric measure of *Fractal Analysis* are *Reversible Iterated Function Systems and the Involution* and *The Self-Similar Measure and the Involution*.

The article assumes *Metric Geometry* for the Hausdorff metric, the isometries and the compactness; *Metric, Uniform and Complete Spaces* for the completeness and the theorem of Banach; *Topological Spaces* for the closed sets and the compactness; *Fractal Geometry* for the attractor and the dimension; and the two articles of the category just cited. No physics is invoked.

## The Involution on the Space of Compact Sets

**Definition.** Let $\sigma$ be an isometric involution of a complete metric space $X$. The **induced involution** on $\mathcal{K}(X)$ is

$$
\Sigma : \mathcal{K}(X) \to \mathcal{K}(X), \qquad \Sigma(A) = \sigma(A) = \{\sigma a : a \in A\} .
$$

**Theorem (the induced involution is an isometric involution).** **(a)** $\Sigma$ maps $\mathcal{K}(X)$ into itself, because the image of a compact set under a continuous map is compact. **(b)** $\Sigma^2 = \operatorname{id}_{\mathcal{K}(X)}$, because $\sigma^2 = \operatorname{id}_X$. **(c)** $\Sigma$ is an isometry of the Hausdorff metric:

$$
d_H\bigl(\Sigma(A), \Sigma(B)\bigr) = d_H(A,B) \qquad (A, B \in \mathcal{K}(X)) .
$$

**(d)** The fixed set $\operatorname{Fix}\Sigma = \{A : \sigma(A) = A\}$ is closed in $\mathcal{K}(X)$ and consists exactly of the compact sets invariant under $\sigma$.

**Proof sketch.** (a) is the continuity of $\sigma$ and the compactness. (b) is the functoriality of the image. (c) the identity $d(\sigma a, \sigma b) = d(a,b)$ gives $\sup_{a \in A} d(\sigma a, \sigma B) = \sup_{a\in A} d(a,B)$ for each of the two terms of the Hausdorff distance, and the two supprema are exchanged by the symmetry of the definition. (d) $\Sigma$ is continuous and involutive, so its fixed set is closed, and $\Sigma(A)=A$ is the definition of the invariance. The statements are those of *Metric Geometry*.

**Example (the fixed compact sets of the standard involutions).** For the reflection $\sigma(x) = -x$ of the line, the fixed compact sets are the compact sets symmetric about the origin, among them the singleton $\{0\}$ and the symmetric Cantor sets. For the reflection of the plane in a line, the fixed compact sets are the compact sets invariant under the reflection, among them the sets contained in the axis and the sets symmetric about it. The fixed set of $\Sigma$ is never empty: a singleton $\{p\}$ for a point $p$ of $\operatorname{Fix}\sigma$ is invariant, and when $\operatorname{Fix}\sigma$ is empty, as for the antipodal map, any two-point orbit $\{x,\sigma x\}$ is an invariant compact set.

## The Commutation and the Symmetric Attractor

**Theorem (the commutation).** Let $f_1,\dots,f_N$ be an iterated function system on $X$ and let $\sigma$ reverse the system, with the involutive permutation $\tau$:

$$
\sigma \circ f_i = f_{\tau(i)} \circ \sigma \qquad (i = 1,\dots,N) .
$$

Then the Hutchinson operator and the induced involution commute,

$$
F \circ \Sigma = \Sigma \circ F ,
$$

and the attractor $K$ is a fixed point of the involution, $\sigma(K) = K$.

**Proof sketch.** The commutation is the computation of *Symmetric Fractals and the Involution*, $\Sigma(F(A)) = \bigcup_i f_{\tau(i)}(\Sigma(A)) = F(\Sigma(A))$. Then $\Sigma(K) = \Sigma(F(K)) = F(\Sigma(K))$, so $\Sigma(K)$ is a fixed point of the Hutchinson operator and, by the uniqueness of the attractor of the lead article *Fractal Geometry*, $\Sigma(K) = K$.

**Theorem (the existence of the symmetric fixed point).** The restriction of $F$ to the closed set $\operatorname{Fix}\Sigma$ maps it into itself and is a contraction of the same ratio $r$; hence $F$ has a unique fixed point in $\operatorname{Fix}\Sigma$, and that fixed point is the attractor $K$.

**Proof sketch.** If $\sigma(A)=A$ then $\sigma(F(A)) = F(\sigma(A)) = F(A)$ by the commutation, so $F$ preserves $\operatorname{Fix}\Sigma$; the fixed set is closed in the complete $\mathcal{K}(X)$, hence complete, and the contraction of *The Hutchinson Operator and Its Adjoint* restricts to it; the Banach theorem gives the unique fixed point in $\operatorname{Fix}\Sigma$, and it is $K$ because $K \in \operatorname{Fix}\Sigma$ by the previous theorem. The statement is the operator form of the symmetry: the symmetric attractor is the fixed point of the operator not only of $F$ but of the restricted operator on the symmetric compact sets, and the two characterisations agree.

**Example (the symmetric Cantor set, on the operator level).** For $f_1(x)=x/3$, $f_2(x)=x/3+2/3$ and $\sigma(x)=1-x$ on $[0,1]$, the induced involution sends a compact set $A$ to $\{1-a : a \in A\}$ and the Hutchinson operator satisfies $F\circ\Sigma=\Sigma\circ F$. The iteration of $F$ from $[0,1]$ gives the approximants $C_n$, each of which is symmetric, and the limit $C$ is symmetric; the fixed set $\operatorname{Fix}\Sigma$ contains the whole sequence $C_n$ and the limit, so the restricted contraction has the same orbit and the same fixed point. The reader sees that the symmetry of the attractor is not an accident of the example but the commutation of the two operators.

## The Adjoint Action on the Measures and the Symmetric Measure

**Definition.** The **Koopman operator** of the involution acts on the functions by $U_\sigma\varphi = \varphi\circ\sigma$; it is an involutive isometry of the bounded continuous functions in the supremum norm, and a unitary involution of $L^2(\mu)$ when $\mu$ is invariant. Its **adjoint** acts on the measures by the pushforward,

$$
\sigma_\# \mu = \mu \circ \sigma^{-1} = \mu\circ\sigma , \qquad \int \varphi\, d(\sigma_\#\mu) = \int (\varphi\circ\sigma)\, d\mu ,
$$

and $\sigma_\#$ is again an involution of the probability measures, and an isometry for the Wasserstein metric because $\sigma$ is an isometry.

**Theorem (the symmetric self-similar measure).** Let the weights satisfy $p_i = p_{\tau(i)}$ for every $i$. Then the pushforward operator $L$ of the self-similar system commutes with the involution,

$$
\sigma_\# \circ L = L \circ \sigma_\# ,
$$

and the self-similar measure $\mu$ is invariant under the involution,

$$
\sigma_\# \mu = \mu .
$$

**Proof sketch.** The computation is a reindexing: $\sigma_\#(L\mu) = \sum_i p_i (\sigma\circ f_i)_\#\mu = \sum_i p_i (f_{\tau(i)}\circ\sigma)_\#\mu = \sum_j p_{\tau(j)}(f_j)_\#(\sigma_\#\mu) = L(\sigma_\#\mu)$, using $p_j = p_{\tau(j)}$ in the last step. Then $\sigma_\#\mu$ is a fixed point of $L$ and, by the uniqueness of the self-similar measure of *The Hutchinson Operator and Its Adjoint*, $\sigma_\#\mu = \mu$. The measure-theoretic construction of the symmetric measure, its invariance and the dimension of its quotient are those of *Fractal Analysis*'s *The Self-Similar Measure and the Involution*; the operator relation is what is stated here.

**Remark (the intertwining of the two levels).** The support map links the two involutions: $\operatorname{supp}(\sigma_\#\mu) = \sigma(\operatorname{supp}\mu)$, so a symmetric measure has a symmetric support, and the symmetric attractor is the support of the symmetric self-similar measure. The pair $(\Sigma, \sigma_\#)$ — the involution on the compact sets and the adjoint involution on the measures — is the operator form of the geometry of *Symmetric Fractals and the Involution*: the fixed point of $\Sigma$ is the symmetric attractor, the fixed point of $\sigma_\#$ is the symmetric measure, and the two are linked by the support.

**Remark (the decomposition of a measure).** Every finite measure $\mu$ decomposes into its symmetric and antisymmetric parts,

$$
\mu = \tfrac12(\mu + \sigma_\#\mu) + \tfrac12(\mu - \sigma_\#\mu) ,
$$

the first term invariant under the involution and the second changing sign; the self-similar measure of the compatible weights is purely symmetric, and the antisymmetric part vanishes. The decomposition is the measure-theoretic form of the splitting of a function into its even and odd parts, and it is the reason the involution is a symmetry of the system and not merely a symmetry of the attractor.

## Summary

An isometric involution $\sigma$ of $X$ induces an involutive isometry $\Sigma$ of the space of the nonempty compact sets with the Hausdorff metric, and the fixed points of $\Sigma$ are the compact sets invariant under $\sigma$. When an iterated function system is reversible by $\sigma$, the Hutchinson operator commutes with $\Sigma$, so the attractor — the unique fixed point of $F$ — is invariant under the involution; equivalently, the restriction of $F$ to the closed set of the symmetric compact sets is a contraction with the same unique fixed point, the symmetric attractor. On the measures, the adjoint of the Koopman operator is the pushforward $\sigma_\#$, which is an involution of the probability measures and commutes with the pushforward operator $L$ of the self-similar system when the weights are compatible with the permutation of the maps; the self-similar measure is then symmetric, its support is the symmetric attractor, and every measure splits into its symmetric and antisymmetric parts. The geometry of the symmetric fractals is *Symmetric Fractals and the Involution*, the operator and its adjoint on the measures are *The Hutchinson Operator and Its Adjoint*, the reversible systems and the symmetric measure are *Fractal Analysis*'s, the Hausdorff metric and the completeness are *Metric Geometry*'s, and the attractor and the dimension are *Fractal Geometry*'s.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma$, $\Sigma$ | Isometric involution of $X$; the induced involution $\Sigma(A)=\sigma(A)$ on $\mathcal{K}(X)$ |
| $U_\sigma$ | Koopman operator $U_\sigma\varphi=\varphi\circ\sigma$; unitary involution of the functions |
| $\sigma_\#$ | Pushforward, the adjoint of $U_\sigma$; an involution of the measures |
| $\operatorname{Fix}\Sigma$ | The $\sigma$-invariant compact sets, closed in $\mathcal{K}(X)$ |
| $F\circ\Sigma=\Sigma\circ F$ | The commutation, equivalent to the reversibility of the system |
| $\tau$, $p_i=p_{\tau(i)}$ | The permutation of the maps; the compatible weights |
| $K$, $\mu$ | Symmetric attractor and symmetric self-similar measure; $\sigma(K)=K$, $\sigma_\#\mu=\mu$ |
| $\operatorname{supp}\mu=K$ | The support of the symmetric measure is the symmetric attractor |

## Further Reading

- John E. Hutchinson, "Fractals and self-similarity", *Indiana University Mathematics Journal* 30 (1981), 713–747, for the Hutchinson operator, the attractor and the invariant measure.
- Michael F. Barnsley, *Fractals Everywhere* (Academic Press, 2nd edition, 1993), for the operator on the compact sets, the collage theorem and the symmetric constructions.
- Kenneth Falconer, *Fractal Geometry: Mathematical Foundations and Applications* (Wiley, 3rd edition, 2014), for the self-similar sets, the open set condition and the dimension.
- Andrzej Lasota and Michael C. Mackey, *Chaos, Fractals, and Noise: Stochastic Aspects of Dynamics* (Springer, 2nd edition, 1994), for the transfer and Koopman operators, their adjoints and the invariant measures.
- Cédric Villani, *Optimal Transport: Old and New* (Springer, 2009), for the pushforward of the measures, the Wasserstein metric and the contraction.
