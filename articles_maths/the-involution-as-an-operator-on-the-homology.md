
# __The Involution as an Operator on the Homology__

## Introduction

An **involution** of a manifold is a self-homeomorphism $T$ with $T^2 = \mathrm{id}$. It induces an endomorphism $T_*$ of the homology, and $T_*$ is the simplest operator that a symmetry of the manifold produces. This article studies the involution through that operator alone: the homology becomes a module over the group ring $k[\mathbb{Z}/2] = k[t]/(t^2-1)$, the operator splits it into the part it fixes and the part it moves, its trace is a fixed-point count, and the fixed part is related to the fixed set by the Smith theory.

The coefficient ring is kept general, because the two cases differ: over a field of characteristic not two the group ring is semisimple and every module is the direct sum of its fixed and its moving parts, while over $\mathbb{Z}$ the same module carries $2$-torsion and the splitting fails. The sections below treat the operator and its algebra, the transfer and the invariant part, the Lefschetz trace and the fixed-point count, and the Smith theory that bounds the homology of the fixed set.

**The article assumes** the homology and cohomology of a finite CW complex, the Lefschetz number of a self-map, the cup and cap products, and the transfer of a finite covering, all of *Algebraic Topology*, being written in this Part. It uses nothing beyond the operator: the manifold enters through its homology and through the fixed set of the homeomorphism.

**The boundaries of the article.** The involution as a structure on the manifold itself — its fixed set as a manifold, its equivariant surgery and its bordism — is not treated here; the fixed set appears only through the homology the operator computes. The general periodic map, of order divisible by a prime other than two, is the subject of *Periodic Maps and the Smith Theory*. The induced involution on the cohomology ring and its interaction with the intersection form belong to *The Involution on the Homology*. The operators built from the involution, with the adjoint as their archetype, are the subject of *The Involution on the Homology Operators*; the equivariant signature and the $G$-signature theorem are those of *Hermitian Pairings and the Equivariant Signature*. Smooth structures and the analytic proofs of the fixed-point formulae are Part III, and no physics is invoked.

## The Induced Operator and the Group Ring

**Definition.** Let $M$ be a finite CW complex and let $T : M \to M$ be an involution, $T^2 = \mathrm{id}$. Its **induced operator** is the endomorphism
$$
T_* : H_*(M;k) \longrightarrow H_*(M;k), \qquad T_*^2 = \mathrm{id},
$$
and the same letter $T^{*}$ denotes the induced map $H^{*}(M;k)\to H^{*}(M;k)$ on cohomology. With $\mathbb{Z}/2 = \langle t\rangle$, the group ring $k[\mathbb{Z}/2] = k[t]/(t^2-1)$ acts by $t\cdot x = T_*x$, so that $H_*(M;k)$ is a module over $k[\mathbb{Z}/2]$.

The group ring is the algebra that the operator generates, and its structure decides how the homology decomposes.

**Proposition (the two cases of the group ring).** Let $k$ be a field.

**(a)** If $\operatorname{char}k \neq 2$ then $t^2 - 1 = (t-1)(t+1)$ is a factorisation into coprime polynomials, and the Chinese remainder theorem gives
$$
k[\mathbb{Z}/2] \cong k \times k, \qquad t \longmapsto (1,-1).
$$
The ring is semisimple, every $k[\mathbb{Z}/2]$-module is a direct sum of copies of the two simple modules $k$ with $t$ acting by $+1$ and by $-1$, and the module structure is the pair of eigenspaces.

**(b)** If $\operatorname{char}k = 2$ then $t^2 - 1 = (t-1)^2$, the ring $k[t]/(t-1)^2$ is local, and $t-1$ is nilpotent. Every module is an extension of the module on which $t$ acts trivially by one on which $t$ acts unipotently.

**Proof.** (a) The idempotents $e_+ = (1+t)/2$ and $e_- = (1-t)/2$ are orthogonal, sum to $1$, and $k[\mathbb{Z}/2] = k e_+ \oplus k e_-$ with $t e_+ = e_+$, $t e_- = -e_-$. The decomposition of a module is the image of the corresponding idempotent. (b) $t^2-1 = (t-1)^2$ in characteristic two, and $(t-1)^2 = 0$ exhibits the ring as $k[\varepsilon]/(\varepsilon^2)$ with $\varepsilon = t-1$ nilpotent.

The distinction is a characteristic-two phenomenon and is not an artefact of the group: it is what makes the mod 2 homology of an involution the natural coefficient system of Smith theory, treated in the last section.

## The Fixed and the Moving Parts

**Definition.** Let $k$ be a field of characteristic $\neq 2$. The **fixed part** and the **moving part** of the homology are
$$
H_*(M;k)^{T} = \ker\bigl(T_* - \mathrm{id}\bigr), \qquad H_*(M;k)_{T} = \ker\bigl(T_* + \mathrm{id}\bigr),
$$
the $+1$- and the $-1$-eigenspaces of the operator. Setting $P_\pm = \tfrac12(1 \pm T_*)$ for the two projections, one has $H_*(M;k) = H_*^{T} \oplus H_{*T}$ with $H_*^{T} = \operatorname{im}P_+$ and $H_{*T} = \operatorname{im}P_-$.

**Proposition (the trace and the Betti numbers).** Let $k$ be a field of characteristic $\neq 2$ in which the relevant dimensions are finite. Then the induced operator satisfies
$$
\operatorname{tr}\bigl(T_* \mid H_i(M;k)\bigr) = \dim_k H_i(M;k)^{T} - \dim_k H_i(M;k)_{T},
$$
so that the dimension of the fixed part and of the moving part in degree $i$ are
$$
\dim_k H_i^{T} = \tfrac12\bigl(\dim_k H_i + \operatorname{tr}(T_*\mid H_i)\bigr), \qquad \dim_k H_{i,T} = \tfrac12\bigl(\dim_k H_i - \operatorname{tr}(T_*\mid H_i)\bigr).
$$

**Proof.** In a basis adapted to the eigenspace decomposition the operator is diagonal with $+1$ on a space of dimension $\dim H_i^T$ and $-1$ on one of dimension $\dim H_{iT}$; the trace is the difference, and the rank-nullity theorem gives the two sums.

**Remark (the integral case is not semisimple).** Over $\mathbb{Z}$ the splitting by the idempotents is unavailable, since $\tfrac12$ is not integral. A finitely generated $\mathbb{Z}[\mathbb{Z}/2]$-module admits an elementary-divisor normal form with summands $\mathbb{Z}$, $\mathbb{Z}[t]/(t-1)$, $\mathbb{Z}[t]/(t+1)$ and $\mathbb{Z}[t]/(t^2-1)$; the summands $\mathbb{Z}[t]/(t-1)$ and $\mathbb{Z}[t]/(t+1)$ are the fixed and the moving cyclic parts seen through a single generator, and the summand $\mathbb{Z}[t]/(t^2-1)$ is the one on which the operator is not diagonalisable by an integral change of basis. This **Smith normal form** of the module is the integral refinement of the eigenspace decomposition and is the reason the integral homology of an involution carries information invisible over $\mathbb{Q}$.

**Example (the antipodal map of the sphere).** Let $T$ be the antipodal map of $S^n$, $T(x) = -x$, free of fixed points. Over $\mathbb{Q}$ the nonzero homology is $H_0$ and $H_n$, each of dimension one, and $T_*$ acts by $+1$ on $H_0$ and by $\deg T = (-1)^{n+1}$ on $H_n$. For $n$ even, $\deg T = -1$, so $H_n$ lies in the moving part and the fixed part is one-dimensional, concentrated in degree zero; for $n$ odd, $\deg T = +1$, and the fixed part is two-dimensional. The moving part is the algebraic shadow of the fact that $T$ moves every point.

**Example (the torus and the involution $-I$).** On $T^2 = \mathbb{R}^2/\mathbb{Z}^2$ the involution $-I$ is orientation-preserving. On $H_1(T^2;\mathbb{Q}) = \mathbb{Q}^2$ it acts by $-I$, so the fixed part of $H_1$ vanishes and the moving part is two-dimensional; on $H_0$ and $H_2$ it acts trivially, so the fixed part there is one-dimensional. The fixed set consists of the four points of $\tfrac12\mathbb{Z}^2/\mathbb{Z}^2$.

## The Operator on the Chain Complex

The operator is induced from a chain-level involution, and the chain-level picture carries the fixed set that the homology hides.

**Definition.** Let $T$ act simplicially on a finite simplicial complex $K$. The **equivariant chain complex** is $C_*(K;k)$ with the involution $T_\# : C_i(K;k)\to C_i(K;k)$ induced on the chains, so that $C_*(K;k)$ is a complex of $k[\mathbb{Z}/2]$-modules and $T_\#\partial = \partial T_\#$. The **fixed subcomplex** $C_*^{T} = C_*(K^{T};k)$ consists of the chains supported on the fixed simplices, and the **coinvariant complex** is $C_{*T} = C_*/(1-T_\#)C_*$, the quotient by the subcomplex generated by the chains of the form $c - T_\#c$. Both are sub- or quotient complexes, and there is a short exact sequence of complexes
$$
0 \longrightarrow C_*^{T} \longrightarrow C_* \xrightarrow{\ q\ } C_{*T} \longrightarrow 0 ,
$$
in which the middle map is the projection to the coinvariants.

**Proposition (the operator is a chain map and the sequence is exact).** The map $T_\#$ satisfies $T_\#^2 = \mathrm{id}$ and commutes with the boundary, so it passes to the homology; a chain is fixed by $T_\#$ exactly when it is supported on the fixed simplices, so $C_*^{T}$ is the kernel of $1 - T_\#$, and the sequence above is exact. Consequently there is a long exact sequence
$$
\cdots \longrightarrow H_i(K^{T};k) \longrightarrow H_i(K;k) \xrightarrow{\ q_*\ } H_i(C_{*T}) \longrightarrow H_{i-1}(K^{T};k) \longrightarrow \cdots
$$
relating the homology of the fixed subcomplex, the homology of $K$ and the homology of the coinvariant complex.

**Proof.** $T_\#$ commutes with $\partial$ because it comes from a simplicial map, so it descends to the homology; a chain is fixed iff each simplex it involves is fixed setwise and its coefficients are constant along the orbits, which for a simplicial action means the simplex is pointwise fixed. The exactness in the middle is the definition of $C_{*T}$, and the long exact sequence is the homology sequence of a short exact sequence of complexes.

**Corollary (fixed part, moving part and the fixed set).** Over a field of characteristic not two the long exact sequence splits into the two eigenspace pieces: the fixed part of $H_i(K;k)$ contains the image of $H_i(K^{T};k)$, and the coinvariant homology $H_i(C_{*T})$ is isomorphic to the moving part $H_{i,T}$; for a free action the coinvariant complex is the chain complex of the orbit space, so $H_{i,T}\cong H_i(K/T;k)$. This is the precise sense in which the operator computes the fixed set from the homology.

## The Transfer and the Invariant Part

The fixed part of the homology is computed by the orbit map when the coefficient ring is one in which $2$ is invertible.

**Definition.** Let $T$ act on $M$ and let $p : M \to M/T$ be the orbit map to the quotient. The **transfer** is the homomorphism
$$
p_* : H_*(M/T;k) \longrightarrow H_*(M;k)
$$
defined on the chains of the quotient by lifting a chain of the quotient to the two sheets of the covering over its interior, summing the two lifts and dividing by the number of sheets where this is defined.

**Theorem (the invariant part is the homology of the quotient).** Let $T$ act on the finite CW complex $M$ and let $k$ be a ring in which $2$ is invertible. Then the orbit map induces an isomorphism
$$
H_*(M/T;k) \;\cong\; H_*(M;k)^{T},
$$
and the transfer $p_*$ is a section of the map $p_*$ induced by $p$; the composite $p_* p_*$ is multiplication by $2$ and becomes the identity after inverting $2$.

**Proof sketch.** The orbit map is a quotient by a finite group of order two. The two composites $p^* p_*$ and $p_* p^*$ are computed on chains: the pullback followed by the pushforward multiplies a chain by the number of sheets over its interior, which is two; the averaging projector $\tfrac12(1+T_*)$ is therefore the composite $\tfrac12 p_* p^*$, and its image is the invariant part. The transfer is the "$p_*$" of the pair and is well defined because the quotient map is a branched covering with the branch set the image of the fixed set, over which the two lifts coincide.

**Remark (the free case).** When $T$ is free, the orbit map is an ordinary two-sheeted covering and the transfer is the classical transfer of a covering of *Algebraic Topology*. When $T$ has fixed points the orbit map is not a covering, but the theorem stands with $k$ containing $\tfrac12$, the fixed set contributing to both sides. The statement fails over $\mathbb{Z}$: $H_*(M;\mathbb{Z})^T$ is then generally larger than the image of $H_*(M/T;\mathbb{Z})$, the difference being the $2$-torsion detected by the integral Smith normal form above.

**Corollary (the Euler characteristics).** For a $T$-action on a finite CW complex with $2$ invertible in the coefficients, the Euler characteristic of the fixed part, defined as the alternating sum $\sum_i(-1)^i\dim_k H_i^{T}$, equals the Euler characteristic $\chi(M/T)$ of the quotient.

## The Lefschetz Trace and the Fixed-Point Count

**Definition.** The **Lefschetz number** of the involution is
$$
L(T) = \sum_{i\ge0}(-1)^i \operatorname{tr}\bigl(T_* \mid H_i(M;\mathbb{Q})\bigr) = \sum_{i\ge0}(-1)^i\bigl(\dim_{\mathbb{Q}} H_i^{T} - \dim_{\mathbb{Q}} H_{i,T}\bigr),
$$
the second expression being the one supplied by the eigenspace decomposition.

**Theorem (Hopf trace formula for an involution).** Let $T$ act simplicially on a finite simplicial complex $K$, and suppose the fixed set $K^T$ is a subcomplex. Then
$$
L(T) = \chi(K^T),
$$
the Euler characteristic of the fixed subcomplex.

**Proof.** The Lefschetz number is the alternating sum of the traces on the chain groups, by the standard chain-level computation of the Lefschetz number of *Degree Theory and the Brouwer Fixed Point Theorem*. On $C_i(K;\mathbb{Q})$ the operator $T_*$ permutes the $i$-simplices; a simplex not fixed setwise contributes a trace of zero, a simplex fixed setwise and not pointwise is permuted among its vertices and again contributes zero unless $T$ fixes it pointwise, and a simplex of $K^T$ is fixed pointwise and contributes $1$. The alternating sum of the counts of the fixed simplices is $\chi(K^T)$.

**Corollary (the fixed set is nonempty).** If $L(T) \neq 0$ then $T$ has a fixed point. In particular an involution of a finite CW complex with $\chi(M/T)$ odd, or with $L(T) \neq 0$, has a nonempty fixed set; the antipodal map of $S^n$ has $L(T) = 1 + (-1)^n(-1)^{n+1} = 0$ and is indeed free.

**Remark (the trace is the fixed-part signature).** The Lefschetz number is the alternating sum of the dimensions of the fixed part minus those of the moving part; it is therefore the **equivariant Euler characteristic** of the fixed part. The two extreme cases are $T = \mathrm{id}$, for which $L(T) = \chi(M)$ and the moving part vanishes, and a free involution, for which $L(T) = 0$ and the fixed part and the moving part have equal alternating dimensions.

## The Smith Theory of the Fixed Part

The operator computes the fixed set through the homology, and the Smith theory is the set of constraints that the operator imposes on it. Throughout, $k = \mathbb{F}_p$ for a prime $p$, and the action is that of $\mathbb{Z}/p$.

**Definition.** A space $X$ is a **mod $p$ homology $n$-sphere** if $H_i(X;\mathbb{F}_p) = 0$ for $i \neq n$ and $H_n(X;\mathbb{F}_p) \cong \mathbb{F}_p$; it is **mod $p$ acyclic** if all its reduced mod $p$ homology vanishes. The fixed set of an action is written $X^{G}$.

**Theorem (Smith; the fixed set is of the same homology type).** Let $G = \mathbb{Z}/p$ act on a finite-dimensional paracompact space $X$ of finite mod $p$ cohomological dimension.

**(a)** If $X$ is mod $p$ acyclic, then $X^{G}$ is mod $p$ acyclic and nonempty; in particular a free $\mathbb{Z}/p$-action is possible on a mod $p$ acyclic space only if the space is empty.

**(b)** If $X$ is a mod $p$ homology $n$-sphere, then $X^{G}$ is a mod $p$ homology $r$-sphere for some $-1 \leq r \leq n$, the value $r = -1$ meaning that $X^{G}$ is empty; in particular a free $\mathbb{Z}/p$-action on a mod $p$ homology $n$-sphere is possible only if $p = 2$ or $n$ is odd.

**(c)** If $X$ is a mod $p$ homology $n$-manifold, then every component of $X^{G}$ has dimension at most $n$, and the action is trivial if a component has dimension $n$.

**Theorem (the Smith inequality).** Let $G = \mathbb{Z}/p$ act as above. Then the mod $p$ cohomology of the fixed set is finitely generated and satisfies
$$
\sum_i \dim_{\mathbb{F}_p} H^i(X^{G};\mathbb{F}_p) \;\le\; \sum_i \dim_{\mathbb{F}_p} H^i(X;\mathbb{F}_p).
$$
If equality holds, then the action has the same cohomological dimension as $X$ and the fixed set is a mod $p$ homology manifold of the same dimension; for a homology sphere this happens exactly when the fixed set has the dimension of $X$ and the action is trivial.

**Theorem (Floyd; the Euler characteristic congruence).** Let $G = \mathbb{Z}/p$ act on a compact space with finitely generated mod $p$ homology and finitely generated fixed set. Then
$$
\chi(X^{G}) \equiv \chi(X) \pmod p .
$$
For $p = 2$ this is the statement that the fixed set of an involution has the parity of the Euler characteristic of the ambient space, which agrees with the Hopf trace formula $L(T) = \chi(X^{T})$ read modulo two.

**Proof sketch of the Smith theory.** The action of $\mathbb{Z}/p$ on the chain complex is filtered by the **Smith special homology**, the homology of the subcomplex of chains fixed by the group; the connecting maps in the long exact sequence relating the ordinary and the special homology are supplied by the transfer, and the analysis of the resulting exact sequences gives (a) and (b). The inequality (c) and the Euler characteristic congruence follow from the same sequences by counting the ranks of the terms of total cohomological dimension at most that of $X$, using that the total dimension is additive on the sequence. The arguments are for finite complexes; the general case is obtained by an exhaustion. The full proofs, with the transfer of the group action and the exact sequences, are in *Algebraic Topology* and in the literature cited below; the article states the results and uses them.

**Example (the fixed set of an involution on the sphere).** The antipodal map of $S^n$ is free, so $X^{G}$ is empty and $r = -1$; the reflection of $S^n$ in a hyperplane has fixed set a mod $2$ homology $(n-1)$-sphere, namely the equatorial $S^{n-1}$, so $r = n-1$; and a non-free involution of $S^2$ has a fixed set a mod $2$ homology sphere of dimension $0$ or $1$, that is, an even number of points or a circle, the two classical cases.

**Example (the torus and the Euler characteristic congruence).** On the torus with $\chi = 0$, the involution $-I$ has four fixed points, of Euler characteristic $4 \equiv 0 \pmod 2$, and a free involution has the empty fixed set of Euler characteristic $0$; both satisfy Floyd's congruence.

## Summary

An involution $T$ of a finite CW complex induces an operator $T_*$ on the homology with $T_*^2 = \mathrm{id}$, and the homology becomes a module over the group ring $k[\mathbb{Z}/2] = k[t]/(t^2-1)$. Over a field of characteristic not two the ring is $k\times k$ and the module is the direct sum of the fixed part $\ker(T_*-\mathrm{id})$ and the moving part $\ker(T_*+\mathrm{id})$, the two projections being $\tfrac12(1\pm T_*)$; the trace of the operator is the difference of their dimensions, and the Lefschetz number of the involution is the alternating sum of those differences. Over $\mathbb{Z}$ the splitting fails and the module has an elementary-divisor (Smith) normal form with a summand $\mathbb{Z}[t]/(t^2-1)$ on which the operator is not diagonalisable; the fixed part is then computed over coefficients in which two is invertible, where the orbit map induces the isomorphism $H_*(M/T;k)\cong H_*(M;k)^T$ and the transfer exhibits the fixed part as a direct summand. The Hopf trace formula identifies the Lefschetz number with the Euler characteristic of the fixed subcomplex, so the operator counts the fixed points, and the Smith theory bounds the fixed set by the manifold: on a mod $p$ homology sphere the fixed set of a $\mathbb{Z}/p$-action is a mod $p$ homology sphere of dimension no larger, on a mod $p$ homology manifold it is of dimension no larger, the total mod $p$ cohomological dimension does not increase, and Floyd's congruence $\chi(X^{G})\equiv\chi(X)\pmod p$ holds.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T$, $T^2 = \mathrm{id}$ | an involution of the manifold or complex, and its induced operator on homology |
| $T_*$, $T^{*}$ | the induced endomorphisms on homology and on cohomology |
| $k[\mathbb{Z}/2] = k[t]/(t^2-1)$ | the group ring that makes the homology a module over the operator |
| $H_*(M;k)^{T}$, $H_{*T}$ | the fixed part $\ker(T_*-\mathrm{id})$ and the moving part $\ker(T_*+\mathrm{id})$ |
| $P_\pm = \tfrac12(1\pm T_*)$ | the projections onto the fixed and the moving parts, over a field of characteristic not two |
| $p : M \to M/T$ | the orbit map to the quotient; $p_*$ the transfer |
| $L(T) = \sum_i(-1)^i\operatorname{tr}(T_*\mid H_i(M;\mathbb{Q}))$ | the Lefschetz number of the involution; $L(T) = \chi(M^{T})$ |
| $X^{G}$ | the fixed set of the group action |
| mod $p$ homology $n$-sphere, acyclic | the homology types that the Smith theory propagates to the fixed set |
| Smith inequality | $\sum_i\dim H^i(X^{G};\mathbb{F}_p)\le\sum_i\dim H^i(X;\mathbb{F}_p)$ |
| Floyd's congruence | $\chi(X^{G})\equiv\chi(X)\pmod p$ |
| Smith normal form | the elementary-divisor decomposition of the integral $\mathbb{Z}[\mathbb{Z}/2]$-module $H_*(M;\mathbb{Z})$ |

## Further Reading

- Paul A. Smith, "Transformations of Finite Period", *Annals of Mathematics* 39 (1938), 127–164, for the fixed-point theory of periodic maps and the special homology.
- Paul A. Smith, "Fixed-Point Theorems for Periodic Transformations", *American Journal of Mathematics* 63 (1941), 1–8, for the period-two statements.
- Edwin E. Floyd, "On Periodic Maps and the Euler Characteristics of Associated Spaces", *Transactions of the American Mathematical Society* 72 (1952), 138–147, for the Euler characteristic congruence.
- Glen E. Bredon, *Introduction to Compact Transformation Groups* (Academic Press, 1972), for the Smith theory, the transfer and the equivariant homology developed in full.
- Tammo tom Dieck, *Transformation Groups* (de Gruyter, 1987), for the equivariant homology, the localization theorems and the fixed-point data.
- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002), for the homology, the transfer and the Lefschetz number used as the input.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the group ring $k[\mathbb{Z}/2]$, its idempotents and its module theory over a general coefficient ring.
