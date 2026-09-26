
# __Topological Dynamics__

## Introduction

A **topological dynamical system** is a topological space $X$ together with a continuous map $T:X\to X$, or a continuous action of a group or semigroup, and topological dynamics is the study of the properties of the action that are invariant under a change of coordinates by a homeomorphism. No differentiability and no measure is assumed: the whole theory is carried by the topology of the phase space and by the continuity of the action, and its basic notions — the orbit and its closure, the limit sets, recurrence, minimality, transitivity, equicontinuity, and the entropy that counts the exponential growth of the number of distinguishable orbits — are topological invariants of the system. When a measure is available and invariant, the same system has a measure-theoretic dynamics, which is the subject of *Ergodic Theory*; the present article keeps the two apart and cites the measure theory rather than mixing it in.

The article begins with the orbit, the $\omega$-limit and $\alpha$-limit sets and the invariant subsets, with the elementary fact that the limit sets of a continuous map on a compact space are compact, invariant and nonempty. It then develops recurrence: periodic points, recurrent and almost periodic points, the non-wandering set, and the **Birkhoff recurrence theorem**, that every homeomorphism of a compact metric space has a recurrent point; the measure-theoretic **Poincaré recurrence theorem** is quoted from *Ergodic Theory*. Minimality follows: the existence of minimal sets by compactness, the equivalence of minimality with the density of every orbit, and the examples of the rotations of the circle and of the torus. Topological transitivity and its relation to dense orbits, the mixing conditions, and the structure theory of minimal flows — equicontinuity, distality, proximality and the **enveloping semigroup** of Ellis — are the next blocks, with the theorem of Auslander and Ellis that a minimal equicontinuous flow is a translation flow on a compact homogeneous space. The article then defines **topological entropy** in the two equivalent forms, of Adler–Konheim–McAndrew by open covers and of Bowen by separated sets, proves its elementary properties and computes it for the rotation and the shift, and it closes with the chain recurrent set and Conley's decomposition.

The topological spaces, the compactness, the metric spaces, the Baire category theorem and the homeomorphism group are those of *Topological Spaces*, *Metric, Uniform and Complete Spaces* and *Topological Groups*; the compact-open topology on the spaces of maps is the standard one and is used only in passing. The measure-theoretic recurrence and ergodicity are those of *Ergodic Theory*; the invariant measures, the Birkhoff and von Neumann ergodic theorems and the variational principle are cited there and are not developed here. Symbolic systems, smooth systems, hyperbolic systems, bifurcations.

No physics is invoked.

## Orbits, Limit Sets and Invariance

### Systems and Orbits

**Definition.** A **topological dynamical system** is a pair $(X,T)$ with $X$ a topological space and $T:X\to X$ continuous; the **orbit** of $x \in X$ is the set $\mathcal O(x)=\{T^nx:n \in \mathbb{N}_0\}$, and the **$\omega$-limit set** is

$$
\omega(x)=\bigcap_{N \in \mathbb{N}}\overline{\{T^nx:n \ge N\}},
$$

the set of points that every orbit of $x$ visits arbitrarily late. When $T$ is a homeomorphism the **$\alpha$-limit set** $\alpha(x)$ is also defined, as the set of points that every backward orbit visits arbitrarily late, that is, the $\omega$-limit set of $x$ for the inverse system $(X,T^{-1})$; the **full orbit** is $\{T^nx:n \in \mathbb{Z}\}$. A subset $A \subseteq X$ is **invariant** if $T(A)\subseteq A$ and **totally invariant** if $T^{-1}(A)=A$; it is **minimal** if it is nonempty, closed and invariant and contains no proper nonempty closed invariant subset.

For a flow $\varphi:\mathbb{R}\times X\to X$, that is, a continuous action of the additive group $\mathbb{R}$ (or of a semigroup), the same notions are defined with the orbit $\varphi(\mathbb{R},x)$ and the limit set $\omega(x)=\bigcap_{t\ge0}\overline{\varphi([t,\infty),x)}$. The discrete and the continuous theory run in parallel, and the statements below are given for a single continuous map, the flow versions being obtained by replacing the sequence $T^n$ by the family $\varphi_t$.

**Proposition (limit sets).** Let $X$ be compact and $T:X\to X$ continuous. Then for every $x \in X$ the set $\omega(x)$ is nonempty, compact and invariant, and $T(\omega(x))=\omega(x)$ when $T$ is a homeomorphism; more generally $\omega(x)$ is the smallest closed set that every tail of the orbit accumulates on, and $y \in\omega(x)$ if and only if there are $n_k\to\infty$ with $T^{n_k}x\to y$.

*Proof.* The closures $\overline{\{T^nx:n\ge N\}}$ form a decreasing sequence of nonempty compact sets, so their intersection is nonempty and compact; the pointwise description of the limit is immediate from the definition, and the invariance follows from the continuity of $T$ applied to a convergent subsequence. $\square$

**Example (the elementary systems).** (i) For the rotation $R_\theta(z)=e^{2\pi i\theta}z$ of the circle $S^1$, the orbit of $z$ is dense if $\theta$ is irrational, and finite if $\theta$ is rational; in the irrational case $\omega(z)=X$ for every $z$, and in the rational case $\omega(z)$ is the cycle through $z$.

(ii) For the shift $\sigma$ on the sequence space, a point is recurrent exactly when each of its blocks recurs infinitely often in the appropriate direction; the periodic points and the points of the minimal subshifts are recurrent, an eventually constant sequence is not, its orbit converging to the fixed point $0^\infty$, and the limit sets are the closed invariant subsets of the shift.

(iii) For the map $x\mapsto2x\bmod1$ of the circle, $\omega(x)=X$ for every $x$ that is not eventually periodic, because the binary expansion of $x$ produces an orbit hitting every interval; the dyadic rationals are eventually fixed at the origin.

### Wandering and Non-Wandering Points

**Definition.** A point $x \in X$ is **wandering** if there is a neighbourhood $U$ of $x$ and an integer $N$ with $T^n(U)\cap U=\varnothing$ for all $n \ge N$; the **non-wandering set** $\Omega(T)$ is the set of points that are not wandering. A point is **periodic** if $T^px=x$ for some $p \ge1$, and **eventually periodic** if some iterate of it is periodic.

**Proposition.** On a compact space, $\Omega(T)$ is closed and invariant, it contains the closure of the set of periodic points and the union of the $\omega$-limit sets and $\alpha$-limit sets, and $T(\Omega(T))\subseteq\Omega(T)$.

*Proof.* The complement of $\Omega(T)$ is open by definition; the invariance follows from the continuity of $T$, which carries the neighbourhoods witnessing the wandering of $x$ to neighbourhoods witnessing the wandering of $Tx$ up to the shift; the periodic points are non-wandering because $U$ meets $T^p(U)=U$, and the limit sets are contained in $\Omega(T)$ because a point of $\omega(x)$ is accumulated on by the orbit and hence returns to every neighbourhood infinitely often. $\square$

## Recurrence and Minimality

### Recurrence

**Definition.** A point $x$ is **recurrent** if for every neighbourhood $U$ of $x$ there are arbitrarily large $n$ with $T^nx \in U$; equivalently, $x \in\omega(x)$. It is **almost periodic** if for every neighbourhood $U$ of $x$ the set of return times $\{n:T^nx \in U\}$ is **syndetic** (has bounded gaps). It is **uniformly recurrent** in a subset $A$ if it returns to every neighbourhood with bounded gaps. The point is **proximal to** $y$ if there are $n_k\to\infty$ with $\operatorname{dist}(T^{n_k}x,T^{n_k}y)\to0$ in a metric phase space.

**Theorem (Birkhoff recurrence).** Let $X$ be a compact metric space and $T:X\to X$ a homeomorphism. Then $T$ has a recurrent point: the minimal sets are nonempty, and every point of a minimal set is recurrent, indeed almost periodic; the union of the minimal sets is therefore contained in the set of recurrent points, and the inclusion is proper in general, since a recurrent point of the full shift need not lie in a minimal subset.

*Proof.* The family of nonempty closed invariant subsets of $X$, ordered by inclusion, has a minimal element by Zorn's lemma and the compactness of $X$: the intersection of a chain of such sets is nonempty, closed and invariant. Let $M$ be minimal; then the orbit closure $\overline{\mathcal O(x)}$ is a nonempty closed invariant subset of $M$ for every $x \in M$, hence equals $M$, so every orbit is dense in $M$. If $x \in M$ and $U$ is a neighbourhood of $x$, the density gives some $n$ with $T^nx \in U$; the union $\bigcup_{k\ge0}T^{-k}(U)$ is nonempty, open and invariant, hence equals $M$ by minimality, and compactness turns this cover of the compact set $M$ into a finite subcover: $M=\bigcup_{k=0}^{N-1}T^{-k}(U)$ for some $N$. Applying this to the point $T^nx \in M$ gives $T^nx \in T^{-k}(U)$ for some $0\le k<N$, that is, $T^{n+k}x \in U$ with $k<N$; hence the return times of $x$ to $U$ have gaps bounded by $N$, which is the almost periodicity of $x$, and almost periodicity implies recurrence. $\square$

The theorem is the topological form of recurrence: it needs no measure and no differentiability, only the compactness; the quantitative statement that almost every point is recurrent with respect to an invariant probability measure is the **Poincaré recurrence theorem**, and the mean recurrence times and the ergodic averages are the subject of *Ergodic Theory*.

**Example.** The irrational rotation of the circle is minimal and every point is almost periodic; the return times to an interval are the Sturmian sequences, whose gaps take at most two values, and this bounded-gap property is the definition of almost periodicity. The rational rotation has all points periodic and every finite orbit is a minimal set. The map $x\mapsto2x$ has the dense orbit of a non-periodic point, but the non-wandering set is all of the circle and the periodic points are dense.

### Minimal Sets and Minimal Systems

**Theorem (characterisations of minimality).** Let $X$ be compact and $T:X\to X$ continuous. The following are equivalent:

(i) $X$ is minimal;

(ii) $\overline{\mathcal O(x)}=X$ for every $x \in X$;

(iii) for every nonempty open $U \subseteq X$ the set $\bigcup_{n\ge0}T^{-n}(U)$ is the whole space;

(iv) there is no proper nonempty closed invariant subset of $X$.

For a homeomorphism the same statements hold with the full orbit $\{T^nx:n \in \mathbb{Z}\}$, and in (iii) the sets $T^{-n}(U)$ may be replaced by $T^{n}(U)$.

*Proof.* (iv) is the definition. If $X$ is minimal and $x \in X$, then $\overline{\mathcal O(x)}$ is closed and invariant, hence equals $X$, which is (ii); conversely (ii) gives (i) because a proper closed invariant subset could not contain a dense orbit. (ii) and (iii) are equivalent because $T^{-n}(U)$ is the set of points whose orbit meets $U$ at time $n$. $\square$

**Example (rotations).** (i) The rotation $R_\theta$ of the circle is minimal if and only if $\theta$ is irrational. If $\theta=p/q$ then the $q$-th roots of unity form a finite invariant set; if $\theta$ is irrational, the orbit of every point is dense by the standard equidistribution argument, and minimality follows from the characterisation.

(ii) On the torus $\mathbb{T}^n$ the translation by a vector $\alpha$ is minimal if and only if the coordinates of $\alpha$ together with $1$ are linearly independent over $\mathbb{Q}$; the same argument with the Kronecker theorem in place of the equidistribution of a single irrational rotation gives the result, and it is the **Kronecker flow**.

(iii) The two-sided shift on a finite alphabet is not minimal, since a constant sequence is a fixed point; the minimal subshifts are the strictly ergodic ones, and their theory lies outside this article.

**Remark.** A minimal translation of a compact abelian group carries a unique invariant probability measure, the Haar measure; a general minimal system need not be uniquely ergodic, and the uniqueness and ergodicity of the invariant measure belong to *Ergodic Theory*.

## Transitivity and Mixing

### Topological Transitivity

**Definition.** Let $X$ be a topological space and $T:X\to X$ continuous. The system is **topologically transitive** if for all nonempty open $U,V \subseteq X$ there is $n \in \mathbb{N}$ with $T^n(U)\cap V\neq\varnothing$; it is **pointwise transitive** if some point has a dense orbit. It is **topologically mixing** if for all nonempty open $U,V$ there is $N$ with $T^n(U)\cap V\neq\varnothing$ for all $n \ge N$, and **weakly mixing** if $T\times T$ is transitive on $X\times X$.

**Theorem (transitivity and dense orbits).** Let $X$ be a compact metric space and $T:X\to X$ continuous. Then $T$ is topologically transitive if and only if the set of points with dense orbit is a dense $G_\delta$ subset of $X$; in particular for a transitive system the generic point has a dense orbit.

*Proof.* If $x$ has dense orbit and $U,V$ are nonempty open, choose $n$ with $T^nx \in U$ and $m>n$ with $T^mx \in V$; then $T^{m-n}(T^nx)=T^mx \in V$ with $T^nx \in U$, so $T^{m-n}(U)\cap V\neq\varnothing$. Conversely, let $\{U_k\}$ be a countable base and put $E_k=\bigcup_{n\ge0}T^{-n}(U_k)$; each $E_k$ is open, and it is dense because for a nonempty open $W$ the transitivity gives $n$ with $T^{-n}U_k\cap W\neq\varnothing$. The intersection $\bigcap_kE_k$ is a dense $G_\delta$ by Baire, and its points are exactly those whose orbit meets every $U_k$, that is, the points with dense orbit. $\square$

**Example.** (i) The irrational rotation is transitive, and indeed minimal, so every point has a dense orbit and the whole circle as its orbit closure; minimality is the stronger condition that every orbit is dense, which for the rotation is the same statement.

(ii) The doubling map $x\mapsto2x\bmod1$ is transitive and has dense periodic points; it is not minimal, and its non-wandering set is the whole circle.

(iii) The full shift on $d$ symbols is transitive when $d \ge2$ and is mixing; its subshifts of finite type are the model examples, developed.

### The Structure of Minimal Flows

**Definition.** A system $(X,T)$ is **equicontinuous** if the family $\{T^n:n \in \mathbb{N}_0\}$ is equicontinuous at every point, that is, for every $\epsilon>0$ there is $\delta>0$ with $d(T^nx,T^ny)<\epsilon$ for all $n$ whenever $d(x,y)<\delta$; on a compact space this is the same as uniform equicontinuity of the family. It is **distal** if no two distinct points are proximal, and **proximal** if some pair of distinct points is. The **enveloping semigroup** $E(X,T)$ is the closure in $X^X$ with the product topology of the set $\{T^n:n \in \mathbb{N}_0\}$ of iterates of $T$.

**Theorem (Auslander–Ellis).** Let $X$ be a compact metric space and $T$ a homeomorphism.

(i) The enveloping semigroup $E(X,T)$ is a compact semigroup under composition, and its elements are the limits of convergent nets of iterates; the system is equicontinuous if and only if $E(X,T)$ consists of continuous maps, and then $E(X,T)$ is a group of homeomorphisms.

(ii) The system is distal if and only if $E(X,T)$ is a group of homeomorphisms; distal systems are the class closed under the operations of the structure theory of minimal flows.

(iii) A minimal equicontinuous system is a translation flow on a compact homogeneous space of a compact group: there is a compact group $G$, a closed subgroup $H$ and a topological generator $g$ of the acting group such that $(X,T)$ is isomorphic to $(G/H,gH)$ acting by left translation. In the case in which $X$ is a compact abelian group, $T$ is a rotation $x\mapsto gx$ with $g$ topologically generating.

*Proof (sketch).* The compactness of $E(X,T)$ is the Tychonoff theorem applied to $X^X$; the closure under composition and the continuity statements are the standard ones. The equivalence of distality with the group property is Ellis's theorem, proved by showing that a distal minimal system is the action of the enveloping semigroup and that a compact semigroup of homeomorphisms with a dense subgroup acting transitively is a group. The representation of an equicontinuous minimal system as a homogeneous space is the theorem of Auslander, obtained by identifying $X$ with the orbit of the identity in the enveloping group. The full proofs are cited below. $\square$

**Corollary (equicontinuous minimal systems are rotations).** An equicontinuous minimal homeomorphism of a compact metric space is topologically conjugate to a minimal rotation on a compact abelian group when the phase space is a group, and in general to a translation on a compact homogeneous space; consequently such a system is rigid, the powers of the acting element accumulating at the identity of the compact group. Every minimal system is a factor of a proximal extension of an equicontinuous minimal system, by the structure theory of minimal flows; this is the **equicontinuous structure relation**, and it is the starting point of the classification of minimal flows by their Ellis groups, which belongs to the topological theory of group actions.

## Topological Entropy

### The Definition by Covers

**Definition.** Let $X$ be compact and $T:X\to X$ continuous. For a finite open cover $\mathcal U$ of $X$ let $N(\mathcal U)$ be the least cardinality of a subcover, put $H(\mathcal U)=\log N(\mathcal U)$, and for $\mathcal U,\mathcal V$ let $\mathcal U\vee\mathcal V=\{U\cap V:U \in\mathcal U,\ V \in\mathcal V\}$; define $\mathcal U^n=\bigvee_{i=0}^{n-1}T^{-i}\mathcal U$. Then

$$
h(T,\mathcal U)=\lim_{n\to\infty}\frac1nH(\mathcal U^n)=\inf_{n\ge1}\frac1nH(\mathcal U^n),
\qquad
h_{\mathrm{top}}(T)=\sup_{\mathcal U}h(T,\mathcal U),
$$

the **topological entropy** of $T$; the limit exists because $H(\mathcal U^{m+n})\le H(\mathcal U^m)+H(\mathcal U^n)$, so the sequence is subadditive.

**Theorem (Bowen's definition).** Let $X$ be a compact metric space and $T:X\to X$ continuous. For $n \in \mathbb{N}$ and $\epsilon>0$ call a set $E \subseteq X$ **$(n,\epsilon)$-separated** if for all distinct $x,y \in E$ there is $0\le k<n$ with $d(T^kx,T^ky)>\epsilon$, and let $s_n(\epsilon)$ be the largest cardinality of such a set; call $F$ **$(n,\epsilon)$-spanning** if the balls $B_{n,\epsilon}(x)=\{y:\max_{0\le k<n}d(T^kx,T^ky)<\epsilon\}$ with $x \in F$ cover $X$, and let $r_n(\epsilon)$ be the least cardinality of such a set. Then

$$
h_{\mathrm{top}}(T)=\lim_{\epsilon\to0}\limsup_{n\to\infty}\frac1n\log s_n(\epsilon)=\lim_{\epsilon\to0}\limsup_{n\to\infty}\frac1n\log r_n(\epsilon),
$$

and the two limits agree with the definition by covers.

*Proof (sketch).* The Bowen balls are the atoms of the cover $\mathcal U^n$ for a cover by $\epsilon$-balls, so a subcover of the latter of least cardinality is an $(n,\epsilon)$-spanning set and a separated set injects into a subcover; this gives the comparison of $N(\mathcal U^n)$ with $r_n(\epsilon)$ and $s_n(\epsilon)$ up to the constants that disappear under $\frac1n\log$ and the limit $\epsilon\to0$. $\square$

### Properties and Computations

**Theorem (properties of entropy).** Let $X,Y$ be compact metric spaces and $T,S$ continuous maps.

(i) If $(X,T)$ and $(Y,S)$ are topologically conjugate, then $h_{\mathrm{top}}(T)=h_{\mathrm{top}}(S)$; the entropy is a conjugacy invariant.

(ii) $h_{\mathrm{top}}(T^k)=k\,h_{\mathrm{top}}(T)$ for $k \ge1$, and $h_{\mathrm{top}}(T^{-1})=h_{\mathrm{top}}(T)$ for a homeomorphism.

(iii) $h_{\mathrm{top}}(T\times S)=h_{\mathrm{top}}(T)+h_{\mathrm{top}}(S)$ for the product system; for a factor map the entropy does not increase, $h_{\mathrm{top}}(S)\le h_{\mathrm{top}}(T)$.

(iv) $h_{\mathrm{top}}$ is neither continuous nor upper semicontinuous in the $C^0$ topology: a horseshoe supported in a disc of radius $\epsilon$ and extended by the identity outside that disc is a homeomorphism whose entropy is at least $\log2$, and as $\epsilon\to0$ these converge uniformly to the identity, whose entropy is $0$. Upper semicontinuity does hold on the space of $C^\infty$ maps, by the theorems of Yomdin and Newhouse. An expansive system has finite entropy: a finite cover by balls of radius less than the expansivity constant is a generator, the atoms of its unlimited refinement are single points, and $h_{\mathrm{top}}(T)=h(T,\mathcal U)\le\log N(\mathcal U)$.

*Proof (sketch).* (i) and (ii) are immediate from the definition by covers, using $T^{k}$ and the natural covers; (iii) follows from the multiplicativity of the number of subcovers in the product, with the logarithm converting the product into a sum; (iv) the failure of upper semicontinuity is exhibited by the horseshoe in a disc of radius $\epsilon$, whose entropy $\log2$ does not depend on $\epsilon$, while the limit is the identity of entropy $0$; the finiteness for an expansive system is the generator argument above. $\square$

**Example (rotation and shift).** (i) If $T$ is an isometry of a compact metric space, then $h_{\mathrm{top}}(T)=0$: a cover by balls of radius $\epsilon/2$ is carried to covers by balls of the same radius, and $H(\mathcal U^n)\le H(\mathcal U)$, so the entropy vanishes. In particular every rotation of the circle and every translation of the torus has entropy zero.

(ii) The full shift on $d$ symbols has $h_{\mathrm{top}}(\sigma)=\log d$; the counting of the $n$-blocks gives $d^n$ and the logarithm divided by $n$ tends to $\log d$. The entropy of a subshift is computed by the growth of its language, and the entropy of a subshift of finite type is the logarithm of the spectral radius of its transition matrix; these computations belong.

(iii) The doubling map $x\mapsto2x\bmod1$ has entropy $\log2$, by the conjugacy with the full two-shift modulo the countable set of dyadic rationals; the entropy is finite and positive, and it is the topological measure of the exponential growth of the number of orbits distinguishable at resolution $\epsilon$.

**Theorem (variational principle).** Let $X$ be a compact metric space and $T:X\to X$ continuous. Then

$$
h_{\mathrm{top}}(T)=\sup_{\mu}h_\mu(T),
$$

the supremum being over the $T$-invariant Borel probability measures and $h_\mu$ the measure-theoretic entropy; the supremum is attained for every expansive system. The measure-theoretic entropy, the ergodic decomposition and the existence of measures of maximal entropy are the subject of *Ergodic Theory*, and the variational principle is quoted there from the standard theory.

## Chain Recurrence and Conley's Decomposition

**Definition.** Let $X$ be a compact metric space and $T$ a homeomorphism. For $\epsilon>0$ an **$\epsilon$-chain** from $x$ to $y$ is a finite sequence $x=x_0,x_1,\dots,x_n=y$ with $d(Tx_i,x_{i+1})<\epsilon$ for $0\le i<n$. The **chain recurrent set** $\mathrm{CR}(T)$ is the set of points $x$ such that for every $\epsilon>0$ there is an $\epsilon$-chain from $x$ to $x$. A **chain transitive component** is an equivalence class of the relation "$x\sim y$ if for every $\epsilon>0$ there are $\epsilon$-chains from $x$ to $y$ and from $y$ to $x$".

**Theorem (Conley).** Let $T$ be a homeomorphism of a compact metric space. Then $\mathrm{CR}(T)$ is a nonempty compact invariant subset of $X$, it contains the non-wandering set, and it is the disjoint union of its chain transitive components, which are compact and invariant. The complement of $\mathrm{CR}(T)$ is exhausted by the basins of the attractors of $T$: each attractor has an open invariant basin containing it, and every point outside $\mathrm{CR}(T)$ lies in the basin of some attractor. If $T$ has no attractor other than $X$ itself, then $\mathrm{CR}(T)=X$ and $T$ is chain transitive.

*Proof (sketch).* The chain recurrent set is closed because the property of being the base of an $\epsilon$-chain is open in $\epsilon$ and the points can be perturbed; it is invariant because a chain can be shifted by one step; the decomposition into components is the decomposition of an equivalence relation into classes, and the compactness of the classes follows from the compactness of $X$ and the uniform continuity of $T$. Conley's theorem that the complement is exhausted by the basins of attractors is proved by a Lyapunov function that decreases along orbits off the chain recurrent set. $\square$

**Example.** For the irrational rotation the chain recurrent set is the whole circle and the system is chain transitive; for a gradient flow the chain recurrent set consists of the rest points, each a chain transitive component; for a Morse–Smale flow it consists of the rest points and the periodic orbits, and the basins are the stable and unstable manifolds. The attractors, their basins and the Lyapunov functions are the tools by which the theory, describes the asymptotic behaviour of a flow.

## Summary

A topological dynamical system is a continuous map $T$ of a topological space $X$, and its invariants are the orbit $\mathcal O(x)$, the $\omega$-limit set $\omega(x)=\bigcap_N\overline{\{T^nx:n\ge N\}}$, which on a compact space is nonempty, compact and invariant, and the non-wandering set $\Omega(T)$, which contains the periodic points and all the limit sets. A point is recurrent if $x \in\omega(x)$ and almost periodic if the return times to every neighbourhood are syndetic; the **Birkhoff recurrence theorem** states that a homeomorphism of a compact metric space has a recurrent point, and the proof passes through the existence of a minimal set and the almost periodicity of its points. The **Poincaré recurrence theorem** and the mean recurrence times are measure-theoretic and belong to *Ergodic Theory*. Minimality — no proper nonempty closed invariant subset — is equivalent to the density of every orbit and to the density of $\bigcup_nT^{-n}(U)$ for every nonempty open $U$; the irrational rotations of the circle and the Kronecker translations of the torus are minimal, the rotations by rational angles are not, and the existence of minimal sets always holds on a compact space.

Topological transitivity — $T^n(U)\cap V\neq\varnothing$ for all nonempty open $U,V$ and some $n$ — is equivalent, on a compact metric space, to the set of points with dense orbit being a dense $G_\delta$, by the Baire category theorem; mixing and weak mixing strengthen the property to the eventual and the product form. A minimal system that is **equicontinuous** is a translation on a compact homogeneous space (Auslander), and the **enveloping semigroup** $E(X,T)$ of Ellis encodes the recurrence and the distality: the system is equicontinuous exactly when $E(X,T)$ consists of continuous maps, and distal exactly when $E(X,T)$ is a group. **Topological entropy** $h_{\mathrm{top}}(T)=\sup_{\mathcal U}\lim_n\frac1nH(\mathcal U^n)$ measures the exponential growth of the number of orbit segments distinguishable at resolution $\epsilon$, in the equivalent form of Bowen by $(n,\epsilon)$-separated and spanning sets; it is a conjugacy invariant, satisfies $h_{\mathrm{top}}(T^k)=kh_{\mathrm{top}}(T)$ and $h_{\mathrm{top}}(T\times S)=h_{\mathrm{top}}(T)+h_{\mathrm{top}}(S)$, vanishes for isometries, equals $\log d$ for the full $d$-shift and $\log2$ for the doubling map, and satisfies the **variational principle** $h_{\mathrm{top}}(T)=\sup_\mu h_\mu(T)$ over the invariant measures, quoted from *Ergodic Theory*. The **chain recurrent set** of a homeomorphism is the compact invariant set on which the orbits are indistinguishable by coarse finite-time approximation, it contains the non-wandering set, it decomposes into chain transitive components, and its complement is the union of the basins of the attractors, by Conley's theorem.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(X,T)$ | topological dynamical system |
| $T^n$ | iterate of $T$ |
| $\varphi_t$ | flow, continuous action of $\mathbb{R}$ |
| $\mathcal O(x)$ | orbit of $x$ |
| $\omega(x)$, $\alpha(x)$ | limit sets of the forward and backward orbit |
| $\Omega(T)$ | non-wandering set |
| $\mathrm{CR}(T)$ | chain recurrent set |
| $E(X,T)$ | enveloping semigroup |
| $\mathcal U$, $\mathcal U^n$ | open cover, join of the first $n$ iterated covers |
| $H(\mathcal U)$, $N(\mathcal U)$ | entropy and covering number of a cover |
| $s_n(\epsilon)$, $r_n(\epsilon)$ | separated and spanning numbers |
| $h_{\mathrm{top}}(T)$ | topological entropy |
| $h_\mu(T)$ | measure-theoretic entropy |
| $R_\theta$ | rotation of the circle by angle $\theta$ |
| $\mathbb{T}^n$ | torus |







## Further Reading

- George D. Birkhoff, "Dynamical systems with two degrees of freedom", *Transactions of the American Mathematical Society* 18 (1917), 199–300, for the recurrence and minimal-set theorems in the topological setting.
- George D. Birkhoff, *Dynamical Systems* (American Mathematical Society Colloquium Publications, 1927), for the foundations of the topological theory.
- Robert Ellis, *Lectures on Topological Dynamics* (Benjamin, 1969), for the enveloping semigroup, distality and the structure theory of minimal flows.
- Joseph Auslander, *Minimal Flows and Their Extensions* (North-Holland, 1988), for the equicontinuous structure relation, the Ellis group and the classification of minimal flows.
- Roy L. Adler, Alan G. Konheim and M. H. McAndrew, "Topological entropy", *Transactions of the American Mathematical Society* 114 (1965), 309–319, for the definition of topological entropy by open covers and its properties.
- Rufus Bowen, "Entropy for group endomorphisms and homogeneous spaces", *Transactions of the American Mathematical Society* 153 (1971), 401–414, for the definition by separated sets and its equivalence with the covering definition.
- Charles Conley, *Isolated Invariant Sets and the Morse Index* (American Mathematical Society, 1978), for the chain recurrent set, the attractors and the fundamental theorem of dynamical systems.
- Yakov Yomdin, "Volume growth and entropy", *Israel Journal of Mathematics* 57 (1987), 285–300, and Sheldon E. Newhouse, "Continuity properties of entropy", *Annals of Mathematics* 129 (1989), 215–235, for the upper semicontinuity of the entropy on the space of $C^\infty$ maps and its failure in the $C^0$ topology.
- Peter Walters, *An Introduction to Ergodic Theory* (Springer, 1982), for the variational principle and the interaction of the topological and measure-theoretic entropy.
