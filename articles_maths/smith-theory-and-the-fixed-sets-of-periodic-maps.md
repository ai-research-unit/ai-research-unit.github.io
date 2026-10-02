# __Smith Theory and the Fixed Sets of Periodic Maps__

## Introduction

A periodic map of a space is a homeomorphism of finite order, and the Smith theory is the set of theorems describing the fixed set of such a map from the homology of the space. Its central statement is that a periodic map with a prime period $p$ cannot have an arbitrary fixed set: for an action of $\mathbb{Z}/p$ on a finite-dimensional complex the fixed set is again finitely generated in mod $p$ homology, its total mod $p$ Betti number is at most that of the space — the **Smith inequality** — and if the space is a mod $p$ homology sphere then the fixed set is a mod $p$ homology sphere of no larger dimension. The theory is the higher-period counterpart of the mod 2 package of *The Mod 2 Cohomology of an Involution*, it is proved by the **Smith transfer**, the averaging of a chain over the group, and in the modern formulation it is the statement that the equivariant cohomology $H_G^*(X;\mathbb{F}_p)$ is a finitely generated module over $H^*(BG;\mathbb{F}_p)$ whose rank is the total mod $p$ Betti number of the fixed set.

The article develops the theory. It defines the periodic maps and the groups they generate, states the Smith inequalities for $\mathbb{Z}/p$ and for a $p$-group together with the local forms, proves the homology sphere theorem and the parity of the dimension drop for odd primes, describes the Smith transfer and the rank proof through the equivariant cohomology, and closes with the examples of the roots of unity and the linear actions and with the statement of the Smith conjecture. The equivariant cohomology and the Borel construction are those of *Equivariant Cohomology*, and its mod 2 case for an involution, with the fixed set and the module $\mathbb{F}_2[x]$, is *The Mod 2 Cohomology of an Involution*; the transfer of a covering and its composition are those of *The Transfer Map*, and the transfer under an involution is the subject of *The Transfer and the Involution*; the fixed-point functors and the equivariant homotopy groups are those of *Equivariant Homotopy Theory*; the Bredon coefficients, in which the theory is stated functorially on the orbit category, are those of *Equivariant Obstruction Theory*. The Smith conjecture, the topological statement that an orientation-preserving periodic map of the three-sphere with a connected non-empty fixed set is conjugate to a rotation, is named at the end; it is a theorem of the three-dimensional topology of *Three-Manifolds and the Geometrisation*, and is not used here.

Nothing analytic and nothing geometric is used. The article is the homology of the fixed set of a finite-order map, with coefficients in a prime field, and the arguments are the module theory of the equivariant cohomology and the averaging of chains; the smooth theory of periodic maps and the differentiable tools are not used, and no distance, no norm, no measure and no smooth structure is chosen. Throughout, $p$ is a prime, $\mathbb{F}_p = \mathbb{Z}/p$ is the prime field, and a **periodic map** of period $p$ is a homeomorphism $\sigma$ of a space $X$ with $\sigma^p = \mathrm{id}$, equivalently an action of the cyclic group $\mathbb{Z}/p$; a **$p$-group** is a group of order a power of $p$. The fixed set of a group $G$ acting on $X$ is $X^G = \{x : g\cdot x = x \ \forall g \in G\}$. The spaces are finite-dimensional complexes, or compact spaces whose cohomology is finitely generated in each degree and vanishes above a fixed dimension, when the finiteness statements are made. The equivariant cohomology $H_G^*(X;\mathbb{F}_p) = H^*(EG\times_G X;\mathbb{F}_p)$ and the classifying space $BG$ are those of *Equivariant Cohomology* and *Classifying Spaces and Cohomology Operations*.

## Periodic Maps and the Fixed Sets

### Periodic Maps and Their Groups

**Definition.** A **periodic map** of period $n$ on a space $X$ is a homeomorphism $\sigma$ with $\sigma^n = \mathrm{id}$; it generates an action of $\mathbb{Z}/n$ by $\bar k\cdot x = \sigma^k(x)$. A periodic map of prime period $p$ generates an action of $\mathbb{Z}/p$, and a finite group of homeomorphisms all of whose orders are powers of $p$ is a **$p$-group action**.

**Proposition.** A periodic map of period $n$ with fixed set $F = X^{\sigma}$ has the fixed set as the fixed set of the cyclic group it generates, and for a composite period $n = p_1^{a_1}\cdots p_r^{a_r}$ the fixed set of the whole group is the intersection of the fixed sets of its Sylow subgroups. The theory therefore reduces to the case of prime period, and the case of a prime period to the case of the group $\mathbb{Z}/p$.

*Proof.* The fixed set of the cyclic group is the set of points fixed by the generator, and a cyclic group is the direct product of its Sylow subgroups; the fixed set of a product is the intersection of the fixed sets. $\square$

### The Fixed Set and Its Invariants

The fixed set $F = X^G$ is a closed subspace when $G$ is finite and $X$ is Hausdorff, and it is the finest of the fixed-point functors of *Equivariant Homotopy Theory*: for $H \leq K$ one has $X^K\subseteq X^H$, so the fixed set of the whole group is the smallest. The Smith theory computes the homology of $F$ from the homology of $X$ and the action, and the two data it uses are the mod $p$ Betti numbers and the dimensions.

## The Smith Inequalities

### The Case of a Prime Period

**Theorem (Smith inequality).** Let $\mathbb{Z}/p$ act on a finite-dimensional complex $X$ with finitely generated mod $p$ homology, and let $F = X^{\mathbb{Z}/p}$. Then the mod $p$ homology of $F$ is finitely generated in each degree and

$$
\sum_i \dim_{\mathbb{F}_p} H_i(F;\mathbb{F}_p) \;\leq\; \sum_i \dim_{\mathbb{F}_p} H_i(X;\mathbb{F}_p),
$$

the total mod $p$ Betti number of the fixed set is at most that of the space. More precisely, the **Smith index** of a class of dimension $k$ is $k$ and each fixed class in degree $k$ accounts for a class in degree at least $k$ downstairs, so that for every $k$,

$$
\sum_{i \leq k} \dim_{\mathbb{F}_p} H_i(F;\mathbb{F}_p) \;\leq\; \sum_{i \leq k} \dim_{\mathbb{F}_p} H_i(X;\mathbb{F}_p) + \sum_{i < k}\dim_{\mathbb{F}_p} H_i(X;\mathbb{F}_p).
$$

*Proof.* The equivariant cohomology $H_{\mathbb{Z}/p}^*(X;\mathbb{F}_p)$ is a finitely generated module over the noetherian ring $H^*(B\mathbb{Z}/p;\mathbb{F}_p)$, by the finiteness of the cohomology of $X$ and the spectral sequence of the Borel fibration; its rank over the polynomial part is the total mod $p$ dimension of the fixed set, by the localization theorem of *Equivariant Cohomology* applied to the prime period; and the rank cannot exceed the total dimension of $H^*(X)$, which is the dimension of the module modulo its $x$-torsion. The degreewise statement follows from the filtration by the degree of the fixed classes. $\square$

### The Case of a $p$-Group

**Theorem (Smith theory of $p$-groups).** Let $P$ be a $p$-group acting on a finite-dimensional complex $X$ and let $F = X^P$. Then the mod $p$ homology of $F$ is finitely generated and the Smith inequality holds, with the fixed set of $P$ equal to the fixed set of its centre and computed by iteration over a central series:

$$
X^P = X^{Z(P)}, \qquad F \text{ a mod } p \text{ finite complex}, \qquad \sum_i\dim_{\mathbb{F}_p}H_i(F)\le\sum_i\dim_{\mathbb{F}_p}H_i(X).
$$

*Proof.* The fixed set of a group is the fixed set of any set of generators, and the centre of a $p$-group is nontrivial; the fixed set of $P$ equals that of $Z(P)$ because a $p$-group acts on $X^{Z(P)}$ and the quotient by the centre has smaller order, so induction on $|P|$ with the prime-period theorem at each stage gives the statement. The finiteness is the finiteness of the equivariant cohomology as a module over the noetherian ring $H^*(BP;\mathbb{F}_p)$, which is polynomial over $\mathbb{F}_p$ on generators of even degree for $p$ odd and a polynomial ring over $\mathbb{F}_2$; the rank is the fixed-set dimension. $\square$

### The Local Forms and the Acyclic Case

**Theorem (Borel; Smith).** Let $\mathbb{Z}/p$ act on a finite-dimensional complex $X$ with the mod $p$ homology of a point, $\tilde H^*(X;\mathbb{F}_p) = 0$. Then the fixed set is mod $p$ acyclic, $\tilde H^*(F;\mathbb{F}_p)=0$; and if $F$ is empty then $X$ is not mod $p$ acyclic, so an acyclic complex admits no free action of $\mathbb{Z}/p$.

*Proof.* For an acyclic complex the equivariant cohomology $H_{\mathbb{Z}/p}^*(X;\mathbb{F}_p)\cong H^*(B\mathbb{Z}/p;\mathbb{F}_p)$ consists of the torsion-free part generated by the base alone, since the fibre contributes nothing; the localization theorem then forces the fixed set to contribute no generic part, which is the acyclicity of $F$. The last statement is the contrapositive. $\square$

The acyclic case is the local computation on which the global theory rests: it says that the fixed set of a periodic map carries the same mod $p$ homology as the space only when the space is a sphere-like object, and it is the source of the restriction on the possible fixed sets.

## The Homology Sphere Theorem

### The Statement

**Theorem (Smith; homology spheres).** Let $\mathbb{Z}/p$ act on a finite-dimensional complex $X$ whose mod $p$ homology is that of an $n$-sphere: $H_i(X;\mathbb{F}_p) = \mathbb{F}_p$ for $i \in \{0,n\}$ and zero otherwise. Then either the fixed set $F$ is empty, or $F$ is a mod $p$ homology $r$-sphere with $-1 \leq r \leq n$; here $r = -1$ is the convention for the empty fixed set, and $F$ is non-empty exactly when $r \geq 0$. For an odd prime $p$ the dimension drop is even,

$$
n - r \equiv 0 \pmod 2 ,
$$

and for $p = 2$ it is unconstrained, the reflection of $S^n$ in an equatorial $S^{n-1}$ realising a drop of one.

*Proof.* The Smith inequality with the hypothesis gives $\sum_i\dim H_i(F)\le2$, so $F$ has the mod $p$ homology of a point or of a sphere; the localization theorem and the action on the top class of $X$, which is either fixed or moved to a class generating the reduced group, exclude the remaining possibilities and identify the degree $r$. For odd $p$ the normal directions to the fixed set carry a complex structure: the action of $\mathbb{Z}/p$ on a linear normal slice is a sum of rotations by $p$-th roots of unity, because the only roots of unity of order dividing $p$ that are real are $\pm1$ and for odd $p$ the eigenvalue $-1$ forces a pair of equal complex eigenvalues, so the normal dimension is even and the drop is even. $\square$

### The Consequences

**Corollary.** A periodic map of odd prime period on a sphere has a fixed set that is a sphere of the same parity of dimension and no larger; a free action of $\mathbb{Z}/p$ on a mod $p$ homology sphere can occur only when the sphere is odd-dimensional for odd $p$, the roots-of-unity action on $S^{2n-1}$ being the model, while for $p=2$ the antipodal action on $S^n$ is free in every dimension. The fixed set of a periodic map is therefore never empty on an even-dimensional sphere for odd $p$, and is never empty on a non-contractible homology sphere that is mod $p$ acyclic.

*Proof.* The parity is the theorem; the root-of-unity action on $S^{2n-1}\subset\mathbb{C}^n$ is free because a scalar $\zeta\neq1$ has no nonzero fixed vector, and it realises the free case in odd dimensions; the antipodal action realises it for $p=2$ in every dimension; the last statements are the contrapositive of the acyclic case. $\square$

**Remark (the Smith conjecture).** For a periodic map of $S^3$ of any period, the Smith theory gives a fixed set that is a mod $p$ homology circle or empty, and the finer statement that an orientation-preserving periodic map of $S^3$ with a connected non-empty fixed set is conjugate to a rotation is the **Smith conjecture**, proved by Thurston and Gordon–Litherland and belonging to the three-dimensional topology of *Three-Manifolds and the Geometrisation* and to the knot theory of *Knot Theory*; the Smith theory of this article is the cohomological input to that theorem and is not sufficient for it.

## The Transfer and the Proof Strategy

### The Smith Transfer

**Definition.** For a finite group $G$ acting on a complex $X$ the **norm operator** is

$$
N = \sum_{g\in G} g_\# : C_*(X;\mathbb{F}_p) \longrightarrow C_*(X;\mathbb{F}_p),
$$

and when the action is free the **Smith transfer** is the chain map $\tau : C_*(X/G;\mathbb{F}_p)\to C_*(X;\mathbb{F}_p)$ of *The Transfer Map*, characterised by $\tau p_* = N$ and $p_*\tau = |G|$, where $p : X \to X/G$ is the quotient.

**Theorem.** The norm operator is $G$-equivariant and satisfies $N^2 = |G|\,N$; its image is the fixed subcomplex $C_*(X;\mathbb{F}_p)^G$, onto which $|G|^{-1}N$ projects when $|G|$ is invertible in $\mathbb{F}_p$. Over $\mathbb{F}_p$ for a $p$-group the scalar $|G|$ vanishes, so the transfer satisfies $p_*\tau = 0$ and $\tau p_* = N$, and the Smith theory is the homological study of the two operators $N$ and $p$ over $\mathbb{F}_p$, in which the averaging has lost its inverse.

*Proof.* The identities are the definitions and the composition of *The Transfer Map*; over $\mathbb{F}_p$ for a $p$-group the scalar $|G|$ vanishes, so $p_*\tau = 0$ and the transfer carries the mod $p$ homology of the quotient into the kernel of $p_*$, which is the source of all the rigidity. The idempotent statement is the computation $N^2 = \sum_{g,h}g_\#h_\# = |G|\,N$. $\square$

### The Rank Proof

**Remark (the modern proof).** The Smith theorems are the statement that for a finite $p$-group $G$ the equivariant cohomology $H_G^*(X;\mathbb{F}_p)$ is a finitely generated module over the noetherian ring $H^*(BG;\mathbb{F}_p)$, and that its rank equals the total mod $p$ Betti number of the fixed set; the localization theorem identifies the generic part with the fixed set, and the finiteness of the module over the polynomial ring gives the bounds. This is the proof strategy of Quillen and of Bredon, and it is the equivariant-cohomological form of the original transfer argument; the module theory over the polynomial ring is the same as that used in the mod 2 case of *The Mod 2 Cohomology of an Involution*.

## The Euler Characteristic and the Lefschetz Trace

### The Trace Formula

**Theorem (Lefschetz–Hopf).** Let $\sigma$ be a periodic map of finite order on a finite complex $X$, and let

$$
L(\sigma) = \sum_k (-1)^k \operatorname{tr}\bigl(\sigma_* \mid H_k(X;\mathbb{Q})\bigr)
$$

be its Lefschetz number. Then $L(\sigma) = \chi(X^{\sigma})$, the Lefschetz number of the map is the Euler characteristic of its fixed set; more generally, for a finite group $G$ acting on $X$ and each $g \in G$, $L(g) = \chi(X^g)$.

*Proof.* On a finite simplicial model on which $\sigma$ acts simplicially the trace of $\sigma$ on the rational chains is the count of the fixed simplices with signs, and the alternating sum of the counts is the Euler characteristic of the fixed subcomplex; the trace formula identifies this alternating sum with the alternating sum of the traces on homology, which is $L(\sigma)$. $\square$

### The Euler Characteristic of the Quotient

**Theorem.** For a finite group $G$ acting on a finite complex $X$,

$$
\sum_{g\in G}\chi(X^g) = |G|\,\chi(X/G),
$$

and for $G=\mathbb{Z}/p$ of prime order it follows that

$$
\chi(X) \equiv \chi(X^G) \pmod p ,
$$

the Euler characteristics of the space and of its fixed set are congruent modulo the prime.

*Proof.* The first identity is the orbit-counting formula applied to the cells: the Euler characteristic of the quotient is the alternating sum of the numbers of the orbits of the cells, and the orbits are counted by $\frac{1}{|G|}\sum_g(\text{the cells fixed by }g)$, whose alternating sum with the Lefschetz formula is $\frac{1}{|G|}\sum_g\chi(X^g)$. For $G=\mathbb{Z}/p$ every non-identity element generates the group and has the fixed set $F$, so the left side is $\chi(X)+(p-1)\chi(F)$ and the identity reads $\chi(X)+(p-1)\chi(F)=p\,\chi(X/\sigma)$, which is the congruence. $\square$

### The Consequences

**Corollary.** An involution of a complex of odd Euler characteristic has a non-empty fixed set, because the congruence with $F$ empty would force $\chi(X)\equiv0\pmod2$; a periodic map of odd prime order $p$ has a quotient with the integral Euler characteristic $\frac{1}{p}(\chi(X)+(p-1)\chi(F))$, so the fixed set is constrained by the divisibility of this number, and on a sphere $S^{2n}$ of any odd prime period the fixed set cannot be empty.

*Proof.* The first statement is the congruence with $F=\emptyset$; the second is the identity rearranged and the integrality of the Euler characteristic of a finite complex; the last is the specialisation to $\chi(S^{2n})=2$ and $\chi(\emptyset)=0$. $\square$

## The Behaviour Under the Operations

### The Products and the Subgroups

**Theorem.** For periodic maps $\sigma$ on $X$ and $\tau$ on $Y$ the product $\sigma\times\tau$ on the product $X\times Y$ is periodic of the period dividing the product of the periods, and

$$
(X\times Y)^{\sigma\times\tau} = X^{\sigma}\times Y^{\tau};
$$

for a subgroup $H\leq G$ the fixed set of $H$ contains that of $G$, and the fixed set of $G$ is the fixed set of $H$ acting on the fixed set of $G$. The Smith inequalities of the factors combine by the Künneth formula over $\mathbb{F}_p$ when its sequence degenerates, so the total mod $p$ Betti number of the fixed set of a product is the product of those of the factors.

*Proof.* A pair $(x,y)$ is fixed by the product exactly when $x$ is fixed by $\sigma$ and $y$ by $\tau$; the inclusion $X^G\subseteq X^H$ for $H\leq G$ is immediate and the last statement follows from the functoriality of the fixed-point functors. The Künneth statement is the Künneth theorem of *Cohomology and the Universal Coefficient Theorem*. $\square$

### The Quotient of the Action

**Theorem.** The periodic map descends to the orbit space only when the quotient is by a normal subgroup; for the action of $G$ on $X$ and a normal subgroup $N$, the quotient group $G/N$ acts on $X/N$, and

$$
(X/N)^{G/N} = X^G/N ,
$$

the fixed set of the quotient action is the image of the fixed set; in particular for a periodic map of period $n$ the cyclic group of order $n$ acts on the quotient by a subgroup, and the Smith theory of the quotient is the Smith theory of the smaller group.

*Proof.* The action of $G$ on $X$ induces an action of $G/N$ on the orbit space $X/N$ because $N$ is normal, and a point $Nx$ of the orbit space is fixed by the class of $g$ exactly when $gx \in Nx$, that is when $x$ is fixed by the class up to the action of $N$, which gives the displayed identity on the fixed sets. $\square$

## Examples

**Example (the roots of unity).** Let $\mathbb{Z}/p$ act on $S^{2n-1}\subset\mathbb{C}^n$ by scalar multiplication by a primitive $p$-th root of unity $\zeta$. The action is free, the fixed set is empty, and the quotient is a lens space; the Smith theorem is compatible with the emptiness, and the mod $p$ homology of the quotient is that of $S^{2n-1}$ with the degree shifted, the transfer recording the $p$-fold covering. In even dimensions the sphere $S^{2n}$ with the same scalar action on the first $n$ complex coordinates and the trivial action on the last real coordinate has fixed set $S^0$, the two poles, a mod $p$ homology $0$-sphere, and the drop $2n$ is even, as the parity theorem requires.

**Example (the linear actions and the projective spaces).** Let $\mathbb{Z}/p$ act on $\mathbb{CP}^{n-1}$ by the diagonal scalar action $[z_0:\dots:z_{n-1}]\mapsto[\zeta^{a_0}z_0:\dots:\zeta^{a_{n-1}}z_{n-1}]$ with weights $a_i$ mod $p$. A point is fixed exactly when every coordinate with $p \nmid a_i$ vanishes, so the fixed set is empty when no weight is divisible by $p$, and is the projective subspace $\mathbb{CP}^{m-1}$ on the $m$ coordinates with $p \mid a_i$ when $m \geq 1$; its total mod $p$ Betti number is $m$, at most the total dimension $n$ of $H^*(\mathbb{CP}^{n-1})$, with equality exactly when every weight vanishes and the action is trivial. The Smith inequality reads as this count.

**Example (the acyclic case).** The disk $D^n$ admits no free action of $\mathbb{Z}/p$: it is mod $p$ acyclic, so by the theorem of Borel a free periodic map on it is impossible; this is the homological reason a periodic map of the disk has a fixed point, in the same circle of ideas as the fixed-point theorems of *Degree Theory and the Brouwer Fixed Point Theorem*.

## Summary

The Smith theory of periodic maps describes the fixed set of a finite-order map from the mod $p$ homology of the space. For an action of $\mathbb{Z}/p$ on a finite-dimensional complex the fixed set $F = X^{\mathbb{Z}/p}$ has finitely generated mod $p$ homology and its total mod $p$ Betti number is at most that of $X$ — the Smith inequality — with the degreewise refinement by the Smith index; for a $p$-group the fixed set equals that of the centre and the inequality holds by iteration. If $X$ is mod $p$ acyclic then so is $F$, so a free action of $\mathbb{Z}/p$ on an acyclic complex is impossible, and if $X$ is a mod $p$ homology $n$-sphere then $F$ is a mod $p$ homology $r$-sphere with $r \le n$ or empty, the drop being even for odd $p$ and unconstrained for $p=2$; the roots-of-unity action on the odd spheres is free, while every even-dimensional sphere with an action of odd prime period has a non-empty fixed set of the same parity. The proofs use the Smith transfer $\tau$, whose composite with the projection is the norm operator and which vanishes against the projection over $\mathbb{F}_p$ for a $p$-group, and, in the modern formulation, the finiteness and rank of the equivariant cohomology as a module over the noetherian ring $H^*(BG;\mathbb{F}_p)$. The mod 2 case for an involution is *The Mod 2 Cohomology of an Involution*, the transfer under an involution is *The Transfer and the Involution*, and the Smith conjecture for the three-sphere belongs to the three-dimensional topology and is named only. Nothing analytic and nothing geometric was used.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $p$ | Prime; $\mathbb{F}_p = \mathbb{Z}/p$ the prime field |
| $\sigma^n = \mathrm{id}$ | Periodic map of period $n$ |
| $G$, $P$ | Finite group, and $p$-group, acting on $X$ |
| $F = X^G$ | Fixed set of the group |
| Smith inequality | $\sum_i\dim_{\mathbb{F}_p}H_i(F)\le\sum_i\dim_{\mathbb{F}_p}H_i(X)$ |
| Smith index | The degree of a fixed class; the refinement of the inequality |
| $\tau[c] = \sum_{g\in G}g_\#[c]$ | Smith transfer; $p_*\tau = |G|$ |
| $N = \sum_g g_\#$ | Norm operator; $N^2 = |G|N$, and $\tau p_* = N$ |
| $H_G^*(X;\mathbb{F}_p)$ | Equivariant cohomology; a module over $H^*(BG;\mathbb{F}_p)$ |
| $F$ a mod $p$ homology $r$-sphere, $r\le n$ | Smith theorem for a homology $n$-sphere |
| $n-r$ even for odd $p$ | Parity of the dimension drop |
| Smith conjecture | An orientation-preserving periodic map of $S^3$ with connected non-empty fixed set is a rotation (a theorem of three-dimensional topology) |

## Further Reading

- Paul A. Smith, "Transformations of finite period", *Annals of Mathematics* 39 (1938), 127–164, and the continuation papers, for the original Smith theory.
- Armand Borel, *Seminar on Transformation Groups* (Annals of Mathematics Studies 46, 1960), for the equivariant-cohomological proof and the finiteness of the equivariant module.
- Daniel Quillen, "The spectrum of an equivariant cohomology ring I, II", *Annals of Mathematics* 94 (1971), 549–602, for the rank of the equivariant cohomology and the fixed-set dimension.
- Glen E. Bredon, *Introduction to Compact Transformation Groups* (Academic Press, 1972), for the Smith theory, the transfer and the local statements.
- Wu-yi Hsiang, *Cohomology Theory of Topological Transformation Groups* (Springer, 1975), for the homology sphere theorem and the computations of fixed sets.
- John W. Morgan and Hyman Bass (eds.), *The Smith Conjecture* (Academic Press, 1984), for the topological conjecture and the reduction to knot and three-manifold theory.
