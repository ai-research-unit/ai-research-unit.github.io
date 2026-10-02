
# __Involutive Profinite Groups__

## Introduction

A profinite group is a compact totally disconnected group, and it is determined by its finite quotients; the natural way for an involution to enter such a group is therefore through the finite quotients, and a continuous involution of a profinite group is exactly a compatible system of involutions of its finite quotients. This makes the fixed subgroup the inverse limit of the fixed subgroups of the finite quotients, reduces the subgroup criterion to the finite case, and connects the theory to the Galois groups of infinite extensions, whose involutions come from the arithmetic of the base field. This article develops the inverse-limit description, the fixed subgroup and its closedness, the finite reduction, and the Galois-theoretic examples.

The article assumes the inverse limit and the topology of a profinite group, the open subgroups and their neighbourhood basis, the Krull topology and the Galois correspondence, and the profinite completion from *Profinite Groups and the Krull Topology*; the continuous involution, the dictionary and the closure properties from *Involutive Topological Groups*; the criterion for the fixed-point set to be a subgroup from *The Fixed-Point Subgroup of a Continuous Involution*; and the compact theory of *Involutive Compact Groups*. The Galois theory that the Krull topology topologises is that of *Galois Theory* and *Splitting Fields and Algebraic Closure* in Part I; the invariant integral of a profinite group is Part III and is not used.

Throughout, $G$ is a profinite group with identity $e$, $\sigma$ is a continuous involution, $\alpha = \sigma\iota$ is the associated continuous involutive automorphism, $G^\sigma$ is the fixed-point set and $I(\sigma) = G^\alpha$ is the inverted subgroup. The open normal subgroups of $G$ are written $N$, and they form an inverse system directed by reverse inclusion.

## Continuous Involutions and Finite Quotients

**Theorem (continuity through the quotients).** A group involution $\sigma$ of a profinite group $G$ is continuous if and only if for every open normal subgroup $N$ there is an open normal subgroup $M \subseteq N$ with $\sigma(M) = M$; equivalently, if and only if the $\sigma$-stable open normal subgroups form a neighbourhood base at $e$. When $\sigma$ is continuous it induces an involution $\sigma_N$ of each finite quotient $G/N$ with $N$ stable, and these involutions form a compatible system.

**Proof.** A continuous map from $G$ to the discrete quotient $G/N$ is locally constant, so $\sigma^{-1}(N)$ is open and contains an open normal subgroup $M$; replacing $M$ by $M \cap \sigma(M)$ gives a $\sigma$-stable open normal subgroup and the compatibility $\sigma(M) = M$, which makes $\sigma$ induce a map of $G/M$ to itself. Conversely, if the stable open normal subgroups form a base, then $\sigma$ is a compatible system of maps of the finite quotients and is therefore continuous, because a map into an inverse limit is continuous when its finite components are. The induced maps are involutions because $\sigma^2 = \mathrm{id}$.

**Theorem (the inverse-limit description).** Let $\sigma$ be a continuous involution of $G$ and let $N$ run over the $\sigma$-stable open normal subgroups. Then the induced maps give isomorphisms of topological groups

$$
G \;\cong\; \varprojlim_N G/N , \qquad G^\sigma \;\cong\; \varprojlim_N (G/N)^\sigma , \qquad G^\alpha \;\cong\; \varprojlim_N (G/N)^\alpha ,
$$

the limits taken over the stable $N$, and the fixed subgroup of the limit is the limit of the fixed subgroups of the finite quotients.

**Proof.** The first isomorphism is the reconstruction of a profinite group from its open normal subgroups. For the second, an element of $G$ is fixed by $\sigma$ exactly when each of its images in the finite quotients is fixed by the induced involution, because the finite components determine the element; the compatible families of fixed points are exactly the fixed points of the limit, and the same argument applies to $\alpha$. Continuity of the maps is the inverse-limit topology.

**Corollary (finite reduction).** Every question about a continuous involution of a profinite group that concerns only its fixed subgroup, the induced involutions of the quotients and the assignment of involutions is a question about finite groups, passed to the limit.

**Proof.** The three isomorphisms above express the profinite data as limits of finite data, and the inverse limit of an inverse system of statements about finite groups is the statement about the limit.

## The Fixed Subgroup

**Theorem (the closedness and the dictionary).** The fixed subgroup $H = G^\alpha = I(\sigma)$ is a closed, hence compact, subgroup of $G$; the fixed-point set $G^\sigma$ is closed and compact; and $G^\sigma$ is a subgroup precisely when it is abelian. The two sets need not be comparable, and $H \subseteq G^\sigma$ exactly when $H$ has exponent two, in which case $H = G^\sigma$.

**Proof.** This is the theorem on the fixed subgroup of a continuous involution, applied to the compact group $G$; the inverse-limit descriptions make the same statements finite at each stage.

**Theorem (openness criteria).** A closed subgroup of a profinite group is open if and only if it has finite index. The fixed subgroup $H = G^\alpha$ is open if and only if the induced involution of $G/N$ has a fixed subgroup of uniformly bounded index for the stable $N$, and $H$ is open when $\alpha$ acts as the inversion on a neighbourhood of $e$.

**Proof.** The first statement is the theorem on open subgroups of a profinite group. For the second, $H$ has finite index exactly when some quotient $G/N$ has $(G/N)^\alpha$ of finite index equal to $[G:H]$, which is the uniform boundedness of the finite indices; the last statement follows because a subgroup containing a neighbourhood of $e$ is open.

**Corollary (the trivial and centralising cases).** If the involution is the identity then $G^\sigma = G$ and $H = G$; if the involution is the inversion of an abelian profinite group then $H = G$ and $G^\sigma$ is the two-torsion subgroup, which is closed and may fail to be open, as for $\hat{\mathbb{Z}}$ with the inversion, where $G^\sigma = \{0\}$.

**Proof.** The first case is immediate. For the abelian inversion, the fixed-point set is the closed subgroup of elements of order dividing two; in $\hat{\mathbb{Z}}$ the only such element is $0$, because a nonzero profinite integer has an infinite cyclic image under some finite quotient.

## Galois-Theoretic Examples

**Example (complex conjugation at a real place).** Let $K$ be a field with an order-two element $\tau$ of its absolute Galois group $G_K = \operatorname{Gal}(\bar K/K)$, the case of complex conjugation at a real place. The inner automorphism $c_\tau$ is a continuous involution of the profinite group $G_K$, and its fixed subgroup is the centraliser $C_{G_K}(\tau)$, which under the Galois correspondence is the decomposition group of the place; the closed subgroup $C_{G_K}(\tau)$ is the Galois group of the corresponding residue extension, and it is open exactly when the place is discrete with finite residue field.

**Proof.** The centraliser of an element of order two is closed because it is the fixed set of the continuous automorphism $c_\tau$; under the Galois correspondence a closed subgroup corresponds to an intermediate extension of $\bar K/K$, and the identification with the decomposition group is the standard dictionary of valuation theory, which Part I's Galois theory supplies.

**Example (the associated anti-involution).** With $\tau$ as above, the composition $\sigma = c_\tau\iota$ is a continuous involution of $G_K$ whose associated involutive automorphism is $\alpha = c_\tau$, so the dictionary is immediate: $G^\sigma = I(c_\tau)$ and $I(\sigma) = C_{G_K}(\tau)$. The anti-involution $\sigma$ inverts the elements of the decomposition group and fixes the elements $g$ satisfying $\tau g^{-1}\tau^{-1} = g$, that is the elements with $g\tau = \tau g^{-1}$.

**Proof.** The dictionary and the computation are those of *Involutive Topological Groups*; the elementwise description follows from $\sigma(g) = \tau g^{-1}\tau^{-1}$.

**Example (the profinite completion of an abstract involution).** Let $\Gamma$ be an abstract group with an involution $\sigma$ and let $\hat\Gamma$ be its profinite completion, the inverse limit of the finite quotients. The involution extends to a continuous involution $\hat\sigma$ of $\hat\Gamma$, and the fixed subgroup of $\hat\sigma$ contains the closure of the image of $\Gamma^\sigma$; it may be strictly larger, by the closedness trap of *Involutive Topological Groups*: a closed subgroup need not be the closure of its intersection with a dense subgroup. The fixed subgroups of the finite quotients compute the fixed subgroup of the completion by the inverse-limit theorem.

**Proof.** An involution of $\Gamma$ acts on the set of finite-index normal subgroups, permutes them and induces involutions of the finite quotients; the compatible system gives a continuous involution of the limit. The inclusion of the closures is clear, and the strictness is the cited warning, witnessed by $\sqrt2\,\mathbb{Z}\subseteq\mathbb{R}$ in the topological form.

**Example (the $p$-adic integers).** On $\mathbb{Z}_p = \varprojlim_k\mathbb{Z}/p^k\mathbb{Z}$ the inversion $x\mapsto -x$ is a continuous involution; its fixed subgroup is $\{0\}$ because $2x = 0$ has only the solution $x = 0$ in $\mathbb{Z}_p$ for odd $p$, and the same holds on $\hat{\mathbb{Z}} = \prod_p\mathbb{Z}_p$. The finite quotients have fixed sets $\{0\}$ for $p$ odd and the whole of $\mathbb{Z}/2^k\mathbb{Z}$ for $p = 2$, so the inverse limit of the fixed sets is again $\{0\}$, consistently with the inverse-limit theorem.

## Summary

A continuous involution of a profinite group is exactly a compatible system of involutions of its finite quotients, equivalently an involution that stabilises a neighbourhood base of open normal subgroups; the group and its fixed and inverted subgroups are the inverse limits of the corresponding finite objects, so the whole theory reduces to finite groups. The fixed subgroup $H = G^\alpha = I(\sigma)$ and the fixed-point set $G^\sigma$ are closed and compact; $G^\sigma$ is a subgroup exactly when it is abelian, $H \subseteq G^\sigma$ exactly when $H$ has exponent two, and then the two coincide. A closed subgroup is open exactly when it has finite index, which for the fixed subgroup is the uniform boundedness of the indices of the fixed subgroups of the finite quotients. The Galois-theoretic examples are the inner involution of an absolute Galois group given by an order-two element, whose fixed subgroup is the centraliser and the decomposition group of the corresponding place; the associated anti-involution $c_\tau\iota$, whose fixed and inverted sets are swapped by the dictionary; and the profinite completion of an abstract involution, whose fixed subgroup contains the closure of the abstract one and may be strictly larger. The integral of a profinite group is Part III and is not used.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G$, $N$ | the profinite group, and an open normal subgroup |
| $\sigma$-stable $N$ | an open normal subgroup with $\sigma(N)=N$; these form a base |
| $\sigma_N$ | the involution induced on the finite quotient $G/N$ |
| $G \cong \varprojlim_N G/N$ | reconstruction from the stable quotients |
| $G^\sigma \cong \varprojlim_N (G/N)^\sigma$ | the fixed set as the limit of the finite fixed sets |
| $H = G^\alpha = I(\sigma)$ | the closed fixed subgroup |
| $[G:H]$ | the index; $H$ is open iff the index is finite |
| $G_K = \operatorname{Gal}(\bar K/K)$ | an absolute Galois group, profinite |
| $C_{G_K}(\tau)$ | the centraliser of an order-two element, the decomposition group |
| $c_\tau\iota$ | the anti-involution attached to complex conjugation |
| $\hat\Gamma$ | the profinite completion of an abstract group $\Gamma$ |

## Further Reading

- John S. Wilson, *Profinite Groups* (Oxford University Press, 1998), for the structure of profinite groups, the open subgroups and the automorphisms of inverse limits.
- Luis Ribes and Pavel Zalesskii, *Profinite Groups* (Springer, second edition, 2010), for the inverse-limit topology, the open normal subgroups and the Galois applications.
- Jürgen Neukirch, Alexander Schmidt and Kay Wingberg, *Cohomology of Number Fields* (Springer, second edition, 2008), for the Galois groups of local and global fields, the decomposition groups and complex conjugation.
- Falko Lorenz, *Algebra II: Fields with Structure, Algebras and Advanced Topics* (Springer, 2008), for the Galois theory of infinite extensions and the fixed fields of closed subgroups.
- Lev S. Pontryagin, *Topological Groups* (Gordon and Breach, second edition, 1966), for the compactness and closedness results used throughout.
