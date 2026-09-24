
# __Diffeomorphism Groups__

## Introduction

Let $M$ be a smooth manifold. The **diffeomorphism group** $\mathrm{Diff}(M)$ is the group of the diffeomorphisms of $M$ with the composition as multiplication; when $M$ is compact and without boundary it is the standard example of an infinite-dimensional Lie group that is neither a group of matrices nor a group of loops, and it is the group whose Lie algebra is the Lie algebra $\mathfrak{X}(M)$ of the vector fields with the bracket $[X,Y] = XY-YX$ of the derivations of $C^\infty(M)$. The group is a **Banach** Lie group of class $C^k$ when $k$ is finite and a **Fréchet** Lie group in the smooth case; in the smooth case it is not locally compact, it carries no Haar measure, and its exponential map — the time-one map of a vector field, which is the exponential map of the written *Lie Groups* and *Hilbert's Fifth Problem and Infinite-Dimensional Lie Theory* — is not locally surjective in general, so that the Lie functor is not an equivalence and the group is the classical instance of this failure.

Two structural features make the group a subject of the second Part. The first is **fragmentation**: every diffeomorphism isotopic to the identity is a product of diffeomorphisms each supported in a ball, and it is a bounded product — the **Thurston fragmentation** — so that the group is generated, in a controlled way, by the subgroups supported in small balls; consequently $\mathrm{Diff}_0(M)$ is simple and perfect for $M$ compact and connected (Thurston, Mather), and the subgroups defined by a geometric structure — the group $\mathrm{Symp}(M,\omega)$ of the symplectomorphisms, the group $\mathrm{Diff}(M,\Omega)$ of the volume-preserving diffeomorphisms, and the Hamiltonian group $\mathrm{Ham}(M,\omega)$ — are handled by the same machinery, with Banyaga's theorem that the volume-preserving and the Hamiltonian groups are simple. The second is the presence of **distances**: the identity component has no finite generating set, so its word metric is not the interesting object, and the genuinely metric structure is the **Hofer metric** on the Hamiltonian group, a bi-invariant metric whose nondegeneracy is a theorem of Hofer, together with the **flux homomorphism** and the **Calabi invariant**, which measure the obstruction to a symplectic isotopy being Hamiltonian. The rigidity of the $C^0$-closure — the theorem of Eliashberg and Gromov that the closure of $\mathrm{Ham}(M,\omega)$ in the homeomorphism group is a group — completes the picture of the group as an object of the topological and metric world rather than of the linear one.

The article develops the group $\mathrm{Diff}(M)$ with the $C^k$ and the smooth topologies and the Lie group structure, the Lie algebra of the vector fields and the exponential map, the subgroups defined by the orientation, a volume form and a symplectic form, the fragmentation and the simplicity theorems, the Hofer metric, the flux and the Calabi invariant, the $C^0$-rigidity, and the failure of the finite generation with the bounded generation that replaces it. The input from above is the smooth manifold and vector field theory of *Lie Groups*, the exponential map and the flow of *The Lie Algebra and the Exponential Map*, the infinite-dimensional Lie framework of *Hilbert's Fifth Problem and Infinite-Dimensional Lie Theory*, the symplectic forms and the Poisson brackets of *Symplectic Forms and Poisson Brackets*, the orientation of *The Rotation Group and Orientation*, and the loop groups and their central extensions of *Loop Groups*. The integration of a top form over an oriented manifold, used below for the Virasoro cocycle, for the Calabi invariant and for the Hofer length, is that of *Differential Forms and Stokes' Theorem*, earlier in this Part. The **diffeomorphism group**, the **fragmentation**, the **Hofer metric** and the **flux homomorphism** are defined in line, since no article above introduces them.

The boundary with the Parts is the one fixed for this block. There is **no measure and no limit** in what follows: the volumes, the Calabi invariant and the Hofer norm use the integral of a top form over an oriented manifold, and the last also the integral of a one-form over an oriented interval, both of which are available in Part II; the analysis of the Hofer metric (the analytic estimates behind the energy–capacity inequalities and the $C^0$-symplectic topology as an analytic theory), the $L^p$-theory of the diffeomorphism groups, the completion of the group in the analytic topologies, the probability measures on $\mathrm{Diff}(M)$ and the ergodic theory of the actions are all Part III, where the measure and the limit are available, and they are cited forward rather than developed. No physics is invoked.

## The Diffeomorphism Group as a Lie Group

### The $C^k$ Topologies and the Smooth Case

**Definition.** Let $M$ be a compact smooth manifold without boundary and let $0\leq k\leq\infty$. The **group of class $C^k$ diffeomorphisms** $\mathrm{Diff}^k(M)$ is the group of the bijections $f : M\to M$ such that $f$ and $f^{-1}$ are of class $C^k$, with the **$C^k$ compact-open topology**: the topology of uniform convergence of the maps and of their derivatives of order at most $k$ in the charts of a finite atlas. For $k$ finite the topological group is a **Banach** Lie group modelled on the Banach space $\mathfrak{X}^k(M)$ of the $C^k$ vector fields with the $C^k$-norm; for $k = \infty$ it is a **Fréchet** Lie group modelled on the Fréchet space $\mathfrak{X}(M) = C^\infty(M,TM)$ of the smooth vector fields with the topology of the uniform convergence of all the derivatives. The **identity component** $\mathrm{Diff}_0(M)$ is the subgroup of the diffeomorphisms isotopic to the identity; in the $C^\infty$ case it is the connected component of the identity.

**Theorem (the Lie group structure).** Let $M$ be compact and without boundary.

**(a)** $\mathrm{Diff}^k(M)$ for finite $k$ is a Banach Lie group: the charts are obtained by the exponential map of a Riemannian metric on $M$, and the group operations are smooth in the Banach sense; the exponential map of the group is a local diffeomorphism near $0$.

**(b)** $\mathrm{Diff}(M) = \mathrm{Diff}^\infty(M)$ is a Fréchet Lie group; the group operations are smooth for the Fréchet structure (Omori), the group is not locally compact, and it does not carry a finite-dimensional Lie algebra of the classical kind: its Lie algebra is the infinite-dimensional $\mathfrak{X}(M)$.

**(c)** The group $\mathrm{Diff}(M)$ is **not** a group of finite dimension: for a connected $M$ of dimension at least $1$, $\mathrm{Diff}(M)$ contains no non-trivial compact open subgroup, is not locally compact, and admits no invariant measure; the compact subgroups of $\mathrm{Diff}(M)$ are the conjugates of the groups of isometries of the invariant metrics, and for a compact $M$ the maximal compact subgroups are the groups of isometries of the Riemannian metrics on $M$.

**Proof sketch.** (a) The chart $X\mapsto \exp_X$ at the identity, defined by the time-one map of the vector field $X$ (which is complete on a compact manifold), is a homeomorphism onto a neighbourhood of the identity with inverse $f\mapsto$ the logarithm of the derivative; the group operations are smooth in the Banach setting by the implicit function theorem for Banach spaces, and the local diffeomorphism property of the exponent is the inverse function theorem. (b) The Fréchet case requires the Nash–Moser-type inverse function theorem instead of the Banach one; the smoothness of the composition and the inversion is the theorem of Omori, and the non-local-compactness is immediate from the infinite-dimensionality of the tangent space. (c) A compact open subgroup would give a neighbourhood of the identity consisting of diffeomorphisms conjugate into a compact group, which fails already for the translations in a chart; there is no invariant measure because the group is not locally compact, a Haar measure on a locally compact group being the only known source of the invariant measure, and this is the statement deferred to the analysis of Part III. $\square$

### The Lie Algebra of Vector Fields and the Exponential Map

**Definition.** The **Lie algebra of the vector fields** $\mathfrak{X}(M) = \Gamma(TM)$ is the space of the smooth sections of the tangent bundle with the bracket $[X,Y] = X\circ Y - Y\circ X$ acting on $C^\infty(M)$: the vector fields are the derivations of the algebra of the smooth functions, and the bracket is their commutator. The **exponential map** of the diffeomorphism group is

$$
\exp : \mathfrak{X}(M)\longrightarrow \mathrm{Diff}_0(M),\qquad \exp(X) = \Phi_X^1 ,
$$

the **time-one map** of the flow $\Phi_X^t$ of the vector field $X$; for $M$ compact every vector field is complete, so the flow is defined for all times, and $\exp$ is smooth with $d\exp_0 = \mathrm{id}$.

**Theorem (the failure of the Lie correspondence).** For a compact manifold $M$ the map $\exp$ is smooth with derivative the identity at $0$, and its image generates $\mathrm{Diff}_0(M)$ as a group, but $\exp$ is **not locally surjective** in general: there are diffeomorphisms isotopic to the identity and arbitrarily close to it in the $C^\infty$-topology which are not the time-one map of any vector field. Consequently the Lie functor $\mathrm{Diff}\mapsto\mathfrak{X}$ is not an equivalence of categories in the smooth case, and the diffeomorphism groups are the classical counterexamples to the naive infinite-dimensional Lie theory; the discussion of the failure of the correspondence in infinite dimensions is that of *Hilbert's Fifth Problem and Infinite-Dimensional Lie Theory*.

**Proof sketch.** The obstruction is already visible on a non-compact manifold: a diffeomorphism close to the identity whose flow structure is incompatible with a single autonomous field cannot lie in the image of $\exp$, and the same obstruction survives on the compact manifolds for the diffeomorphisms with the appropriate local behaviour; the positive statements for the finite differentiability classes follow from the Banach inverse function theorem, which is unavailable in the Fréchet case. The failure is standard in the infinite-dimensional theory and is quoted from the literature. $\square$

**Remark (the regularity of the group).** Although the exponential map fails, the group $\mathrm{Diff}(M)$ is **regular** in the sense of the infinite-dimensional theory: for every smooth curve $t\mapsto X_t$ of vector fields the evolution equation with the time-dependent field $X_t$ defines a smooth one-parameter family of diffeomorphisms of $M$, the **evolution operator**, and this is the strongest form of the Lie theory that survives for the diffeomorphism groups of compact manifolds. The evolution operator is the exponential of a time-dependent field, and it is the reason the group of diffeomorphisms is a "regular" Fréchet Lie group even though the exponential of a single field does not exhaust a neighbourhood of the identity.

## Subgroups Defined by Structure

### Orientation, Volume and Symplectic Forms

**Definition.** Let $M$ be a compact connected oriented manifold of dimension $n$.

**(a)** The **orientation-preserving diffeomorphism group** $\mathrm{Diff}^+(M)$ is the subgroup of the diffeomorphisms preserving the orientation; it is open and of index $2$ in $\mathrm{Diff}(M)$ when $M$ is connected, and its identity component is $\mathrm{Diff}_0(M)$.

**(b)** Let $\Omega$ be a volume form on $M$. The **volume-preserving group** is $\mathrm{Diff}(M,\Omega) = \{f : f^*\Omega = \Omega\}$; its Lie algebra is the Lie algebra of the **divergence-free** vector fields, where the divergence is the function $\operatorname{div}_\Omega(X)$ defined by the Lie derivative $\mathcal{L}_X\Omega = (\operatorname{div}_\Omega X)\Omega$, a definition that uses only the top form and no measure.

**(c)** Let $\omega$ be a symplectic form on $M$. The **symplectomorphism group** is $\mathrm{Symp}(M,\omega) = \{f : f^*\omega = \omega\}$; its Lie algebra is the Lie algebra of the **symplectic vector fields** $X$ with $\iota_X\omega$ closed, and the **Hamiltonian group** $\mathrm{Ham}(M,\omega)$ is the identity component of the subgroup whose Lie algebra consists of the **Hamiltonian vector fields**, those with $\iota_X\omega$ exact, $\iota_X\omega = -dh$ for a Hamiltonian function $h$; the two agree when $H^1(M;\mathbb{R}) = 0$.

**(d)** The subgroups are closed and Lie subgroups for the finite differentiability classes, and for the smooth classes they are Fréchet Lie subgroups; the Lie algebras in (b) and (c) are the kernels of the natural maps to the cohomology, and the tangent space at the identity of $\mathrm{Diff}(M,\Omega)$ is the space of the divergence-free fields.

**Example ($M = S^1$ and $M = T^2$).** For the circle, $\mathrm{Diff}^+(S^1)$ is the orientation-preserving group whose Lie algebra is the vector fields $X = X(t)\frac{\partial}{\partial t}$ on the circle, with the bracket $[X,Y] = (X'Y - XY')\frac{\partial}{\partial t}$; the Lie algebra has the one-dimensional central extension with the cocycle

$$
\omega(X,Y) = \int_{S^1} X'''(t)Y(t)\,\mathrm{d}t ,
$$

the **Virasoro cocycle**, defined by the integral of the one-form $X'''Y\,\mathrm{d}t$ over the oriented circle — the integration of a top form over an oriented manifold, available here — and the corresponding central extension of the algebra is the **Virasoro algebra**, the infinite-dimensional analogue of the central extension of the loop algebra of *Loop Groups*. For the torus $T^2 = \mathbb{R}^2/\mathbb{Z}^2$ with the area form $\omega = \mathrm{d}x\wedge\mathrm{d}y$, the Hamiltonian vector field of a function $h$ is $X_h = \frac{\partial h}{\partial y}\frac{\partial}{\partial x} - \frac{\partial h}{\partial x}\frac{\partial}{\partial y}$. The restriction to the torus of the constant field $(1,0)$ would be the Hamiltonian field of the function $y$, which is not a well-defined function on $T^2$; accordingly the translation by $(1,0)$ is an area-preserving diffeomorphism whose flux is the nonzero integral class $[\mathrm{d}y]$, so it is not Hamiltonian: the Hamiltonian group $\mathrm{Ham}(T^2,\omega)$ is a proper subgroup of $\mathrm{Symp}_0(T^2,\omega) = \mathrm{Diff}(T^2,\omega)_0$, and the flux detects the difference.

### The Flux Homomorphism and the Calabi Invariant

**Definition.** Let $(M,\omega)$ be a compact symplectic manifold and let $\{\phi_t\}$ be a smooth isotopy in $\mathrm{Symp}_0(M,\omega)$ with $\phi_0 = \mathrm{id}$. Writing $\frac{d}{dt}\phi_t = X_t\circ\phi_t$ with $X_t$ symplectic, the one-form $\iota_{X_t}\omega$ is closed, and the **flux** of the isotopy is the class

$$
\operatorname{Flux}(\{\phi_t\}) = \int_0^1[\iota_{X_t}\omega]\,\mathrm{d}t \;\in H^1(M;\mathbb{R}) ,
$$

the integral over the oriented interval of the curve of cohomology classes; the **Flux group** $\Gamma\subseteq H^1(M;\mathbb{R})$ is the image of the flux map on $\pi_1(\mathrm{Symp}_0(M,\omega))$. The flux is independent of the isotopy within the homotopy class, it vanishes for the isotopies inside $\mathrm{Ham}(M,\omega)$, and the exact sequence

$$
1\longrightarrow \mathrm{Ham}(M,\omega)\longrightarrow \mathrm{Symp}_0(M,\omega)\xrightarrow{\ \operatorname{Flux}\ } H^1(M;\mathbb{R})/\Gamma
$$

expresses the Hamiltonian group as the kernel of the flux.

**Theorem (Banyaga; Ono).** Let $(M,\omega)$ be a compact connected symplectic manifold.

**(a)** (flux conjecture) The flux group $\Gamma$ is a discrete subgroup of $H^1(M;\mathbb{R})$, so the quotient $H^1(M;\mathbb{R})/\Gamma$ is a torus; the discreteness holds for a large class of manifolds — in particular for the Kähler manifolds, by the work of Ono and others — and is open in general.

**(b)** The Hamiltonian group $\mathrm{Ham}(M,\omega)$ is a simple group, and it is the kernel of the flux; the group $\mathrm{Symp}_0(M,\omega)$ is not simple but its commutator subgroup is the kernel of the flux.

**(c)** For a closed symplectic manifold with $H^1(M;\mathbb{R}) = 0$ the group $\mathrm{Symp}_0(M,\omega) = \mathrm{Ham}(M,\omega)$ is simple and perfect.

**Proof sketch.** The flux is well defined and locally constant by the closedness of $\iota_X\omega$ and the homotopy invariance of the period map, the integration of the closed one-forms over the cycles being that of *Differential Forms and Stokes' Theorem*; the discreteness of $\Gamma$ is proved by the analytic estimates of the symplectic topology, and the simplicity of the Hamiltonian group is Banyaga's theorem, proved by the fragmentation of the Hamiltonian diffeomorphisms into the commutators supported in the Darboux balls. The statements are quoted from the literature. $\square$

**Definition.** Let $(M,\omega)$ be a compact symplectic manifold with $\omega$ exact, $\omega = d\lambda$, or more generally let $M$ be a closed manifold with a volume form; for a Hamiltonian isotopy with the Hamiltonian $H_t$ the **Calabi invariant** is

$$
\operatorname{Cal}(\{\phi_t\}) = \int_0^1\int_M H_t\,\omega^n\,\mathrm{d}t ,
$$

the integral of the top form $H_t\omega^n$ over the oriented manifold $M$ and of the resulting function over the oriented interval; it is a homomorphism on the group of the Hamiltonian diffeomorphisms compactly supported in the exact case, and its vanishing characterises the diffeomorphisms of the group that are the products of the diffeomorphisms supported in the Darboux balls of vanishing Calabi invariant.

## Geometry of the Group: Distances and Rigidity

### The Hofer Metric

**Definition.** Let $(M,\omega)$ be a compact symplectic manifold and let $\mathrm{Ham}(M,\omega)$ be the Hamiltonian group. For a Hamiltonian isotopy $\{\phi_t\}$ generated by the Hamiltonian $H_t$ — normalised so that $\int_M H_t\,\omega^n = 0$ — define the **Hofer length** of the isotopy by

$$
\ell(\{\phi_t\}) = \int_0^1 \bigl(\max_M H_t - \min_M H_t\bigr)\,\mathrm{d}t ,
$$

the integral over the oriented interval of the **oscillation** of $H_t$, and define the **Hofer metric** on $\mathrm{Ham}(M,\omega)$ by

$$
d_H(\phi,\psi) = \inf_{\{\phi_t\} : \phi_1 = \psi^{-1}\phi}\ \ell(\{\phi_t\}) .
$$

The Hofer metric is bi-invariant: it is invariant under the left translations, invariant under the right translations, and invariant under the conjugation by the elements of $\mathrm{Ham}(M,\omega)$; the definition uses only the supremum and the infimum of the Hamiltonian functions and the integral of a one-form over the oriented interval.

**Theorem (Hofer's nondegeneracy).** Let $(M,\omega)$ be a compact symplectic manifold.

**(a)** The Hofer norm is nondegenerate: $d_H(\phi,\psi) = 0$ if and only if $\phi = \psi$; hence $(\mathrm{Ham}(M,\omega),d_H)$ is a metric space with a bi-invariant metric.

**(b)** (energy–capacity inequality) The Hofer norm is bounded below by the symplectic capacities: for every symplectic capacity $c$ of the manifold and every $\phi\in\mathrm{Ham}(M,\omega)$ with $\phi\neq\mathrm{id}$, there is a lower bound for $d_H(\mathrm{id},\phi)$ in terms of the displacement energy of the subsets displaced by $\phi$; this is the **energy–capacity inequality** of Hofer and Zehnder.

**(c)** The metric completion of $\mathrm{Ham}(M,\omega)$ with respect to $d_H$ contains elements that are not in the group; the group is not closed in its own completion, and the study of the completion is the beginning of the $C^0$-symplectic topology, whose analysis belongs to Part III.

**Proof sketch.** The nondegeneracy is the theorem of Hofer: a Hamiltonian diffeomorphism of small Hofer norm is close to the identity in the dynamical sense, established by comparing the Hofer norm with the displacement energy and the symplectic capacities and by the local structure of the Hamiltonian isotopies close to the identity. The energy–capacity inequality is proved by comparing the Hofer length of the isotopy with the capacity of the displaced sets. The statements are quoted from the literature; the analytic machinery is Part III. $\square$

### The $C^0$-Closure and the Rigidity

**Theorem (Eliashberg–Gromov; Oh–Müller).** Let $(M,\omega)$ be a compact symplectic manifold and let $\mathrm{Ham}(M,\omega)$ act on the homeomorphism group $\mathrm{Homeo}(M)$ through the inclusion and the $C^0$-topology, the topology of the uniform convergence of the maps alone.

**(a)** The $C^0$-closure of $\mathrm{Ham}(M,\omega)$ in $\mathrm{Homeo}(M)$ is a group; its elements are the homeomorphisms preserving $\omega$ in the sense of the $C^0$-symplectic structure, and the closure is the group of the **symplectic homeomorphisms**.

**(b)** The $C^0$-closure of the group is strictly larger than the group: there are symplectic homeomorphisms that are not smooth, so the rigidity of the symplectic structure survives the loss of the differentiability but not the loss of the smoothness of the group structure.

**(c)** Consequently the group of the symplectic homeomorphisms is a closed subgroup of $\mathrm{Homeo}(M)$ which is a topological group but not a Lie group; its study belongs to the $C^0$-symplectic topology, an analytic theory of Part III.

**Proof sketch.** The closedness of the group under the composition in the $C^0$-topology is the theorem of Eliashberg and Gromov, proved by the control of the symplectic behaviour of the limit maps through the $h$-principle and the "symplectic squeezing"; the strictness is exhibited by the non-smooth limits of the Hamiltonian isotopies of small Hofer length. The statements are quoted from the literature. $\square$

### Fragmentation, Simplicity and Bounded Generation

**Definition.** Let $M$ be a manifold and let, for a subset $U\subseteq M$, $\mathrm{Diff}(M)_U$ denote the subgroup of the diffeomorphisms supported in $U$, that is, equal to the identity outside $U$. The diffeomorphism group is **fragmented** over a cover $\{U_i\}$ if every element of $\mathrm{Diff}_0(M)$ is a finite product of the elements of the subgroups $\mathrm{Diff}(M)_{U_i}$.

**Theorem (fragmentation; Thurston, Mather, Banyaga).** Let $M$ be a connected manifold and let $\{U_i\}$ be an open cover of $M$.

**(a)** (fragmentation) Every $\phi\in\mathrm{Diff}_0(M)$ is a finite product of the elements of the subgroups $\mathrm{Diff}(M)_{U_i}$; the number of the factors is finite and, in the compact case, bounded by a constant depending only on the manifold and the cover.

**(b)** (simplicity) For $M$ compact and connected, the group $\mathrm{Diff}_0(M)$ is simple and perfect: every element is a product of commutators, and the group has no non-trivial proper normal subgroup. The same holds for the volume-preserving group $\mathrm{Diff}(M,\Omega)_0$ and, by Banyaga's theorem, for the Hamiltonian group $\mathrm{Ham}(M,\omega)$, while for the symplectomorphism group the commutator subgroup is the kernel of the flux.

**(c)** (bounded generation) The group $\mathrm{Diff}_0(M)$ is not finitely generated for a compact connected $M$ of dimension at least $2$, but it is **boundedly generated** by the subgroups supported in the balls: there is a constant $N$ and a finite family of balls such that every element of $\mathrm{Diff}_0(M)$ is a product of at most $N$ elements supported in them.

**Proof sketch.** (a) The fragmentation is proved by writing a diffeomorphism close to the identity as the product of the diffeomorphisms supported in the elements of a partition of unity on the charts, and by reducing the general case to the connectedness by a path of diffeomorphisms; (b) the simplicity uses the fragmentation and the commutator identities inside the Darboux balls, where a diffeomorphism supported in a small ball is a commutator of two diffeomorphisms supported in a slightly larger ball of the same type; (c) the failure of the finite generation is the vanishing of the abelianisation of the group together with the growth of the fragmentation constant, and the bounded generation is the positive statement that replaces it. The statements are the theorems of Thurston, Mather and Banyaga and are quoted from the literature. $\square$

**Remark (the geometric group theory of $\mathrm{Diff}(M)$).** Since the group $\mathrm{Diff}_0(M)$ is not finitely generated and is perfect, the word metric of a finite generating set does not exist and the quasi-isometric invariants of *Geometric Group Theory* and *Hyperbolic Groups* do not apply to the group itself; what remains of the geometric theory is the **bounded generation** of the theorem above, the study of the **distortion** of the finitely generated subgroups — the finitely generated subgroups of the isometry groups, the groups of the isotopy classes of the periodic diffeomorphisms and the finitely generated groups of the Dehn twists — the action on the natural complexes associated with $M$, and the metric geometry of the Hamiltonian group with the Hofer metric, which is a genuine metric space on which the group acts by isometries. The quotient $\pi_0(\mathrm{Diff}^+(M))$ for a surface is the **mapping class group**, whose geometric theory — the classification of the elements, the pseudo-Anosov representatives and the action on the Teichmüller space with its metric — is the subject, earlier in this Part, and the metric geometry of that space is not developed here.

## The Boundary with Analysis

The theory of this article is the group theory and the geometry of the diffeomorphism groups; the analysis is Part III.

- The **measure theory on $\mathrm{Diff}(M)$**: the group is not locally compact and carries no Haar measure; the invariant measures, the Gaussian and the Wiener-type measures on the group, and the probability theory of the random diffeomorphisms are Part III. The volume forms used above enter only through the integral of a top form over the oriented manifold, which is Part II.
- The **$L^p$-theory and the Sobolev completions** of the groups of maps: the completions $\mathrm{Diff}^s(M)$ of the diffeomorphism group in the Sobolev topologies, the Hilbert manifold structures and the corresponding exponential maps are Part III, where the completion in the analytic sense is available.
- The **analysis of the Hofer metric**: the energy–capacity inequalities, the Hofer geometry as a Finsler metric on the Hamiltonian group, the Arnold conjecture for the fixed points of the Hamiltonian diffeomorphisms, the Floer theory and the pseudoholomorphic curves — all Part III.
- The **$C^0$-symplectic topology**: the symplectic homeomorphism groups, the $C^0$-rigidity theorems, the hard analysis of the limits of the Hamiltonian isotopies — Part III; the statements are recorded above at the level of the theorem.
- The **ergodic theory and the dynamics**: the measure-theoretic entropy, the Lyapunov exponents, the central limit theorems for the random products, and the ergodicity of the actions on the moduli spaces are Part III.
- What is *not* deferred: the group $\mathrm{Diff}^k(M)$ and its Banach and Fréchet structures; the Lie algebra $\mathfrak{X}(M)$ and the exponential map with its failure; the subgroups defined by the orientation, the volume form and the symplectic form with their Lie algebras; the flux and the Calabi invariant at the level of the definition and the theorem; the Hofer metric with the nondegeneracy theorem; the fragmentation, the simplicity and the bounded generation.

## Summary

The diffeomorphism group $\mathrm{Diff}(M)$ of a compact manifold is a Banach Lie group of class $C^k$ for finite $k$ and a Fréchet Lie group in the smooth case, modelled on the vector fields $\mathfrak{X}(M)$ with the bracket $[X,Y] = XY-YX$, with the exponential map the time-one map of the flow of a vector field; the exponential map is smooth with derivative the identity at $0$ but is not locally surjective in general, so the Lie functor is not an equivalence, while the group is regular in the sense that the evolution of a curve of vector fields exists. The group is not locally compact, contains no non-trivial compact open subgroup and carries no invariant measure; the maximal compact subgroups are the isometry groups of the Riemannian metrics on $M$.

The subgroups defined by structure are the orientation-preserving, the volume-preserving and the symplectic groups, with the Lie algebras of the divergence-free, the symplectic and the Hamiltonian vector fields respectively; the cycle $\mathrm{Ham}\to\mathrm{Symp}_0\to H^1(M;\mathbb{R})/\Gamma$, with $\Gamma$ the discrete flux group, measures the obstruction to a symplectic isotopy being Hamiltonian, and the Calabi invariant is the integral of the Hamiltonian over the manifold. The Hamiltonian group carries the Hofer metric, bi-invariant, defined by the integral of the oscillation of the Hamiltonian and nondegenerate by Hofer's theorem; the $C^0$-closure of the Hamiltonian group in the homeomorphism group is a group by the theorem of Eliashberg and Gromov, strictly larger than the group. Fragmentation writes every diffeomorphism isotopic to the identity as a bounded product of diffeomorphisms supported in balls, and it implies the simplicity and the perfectness of $\mathrm{Diff}_0(M)$, of the volume-preserving group and of the Hamiltonian group (Thurston, Mather, Banyaga); the group is not finitely generated but is boundedly generated by the ball-supported subgroups, and the Hofer metric is the genuine metric invariant of the identity component. The measure theory, the completions, the $C^0$-symplectic analysis and the ergodic theory of the groups belong to Part III.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M$ | A smooth manifold, compact and without boundary where stated |
| $\mathrm{Diff}(M)$, $\mathrm{Diff}^k(M)$ | Group of smooth, resp. $C^k$, diffeomorphisms |
| $\mathrm{Diff}_0(M)$ | Identity component (isotopic to the identity) |
| $\mathrm{Diff}^+(M)$ | Orientation-preserving diffeomorphisms |
| $\mathfrak{X}(M)$, $\mathfrak{X}^k(M)$ | Smooth, resp. $C^k$, vector fields; Lie algebra |
| $[X,Y] = XY-YX$ | Lie bracket of vector fields |
| $\Phi_X^t$, $\exp$ | Flow of $X$; time-one map $X\mapsto\Phi_X^1$ |
| $\mathrm{Diff}(M,\Omega)$ | Volume-preserving group ($\Omega$ a volume form) |
| $\operatorname{div}_\Omega$ | Divergence defined by $\mathcal{L}_X\Omega = (\operatorname{div}_\Omega X)\Omega$ |
| $\mathrm{Symp}(M,\omega)$ | Symplectomorphism group |
| $\mathrm{Ham}(M,\omega)$ | Hamiltonian group (identity component of the exact case) |
| $\mathrm{Homeo}(M)$ | Homeomorphism group, the $C^0$-ambient group |
| $\operatorname{Flux}$, $\Gamma$ | Flux homomorphism; flux group (discrete in the known cases) |
| $\operatorname{Cal}$ | Calabi invariant |
| $d_H$ | Hofer metric on $\mathrm{Ham}(M,\omega)$ |
| $\ell(\{\phi_t\})$ | Hofer length: $\int_0^1(\max_MH_t-\min_MH_t)\,\mathrm{d}t$ |
| Virasoro cocycle | $\omega(X,Y) = \int_{S^1}X'''Y\,\mathrm{d}t$ on $\mathfrak{X}(S^1)$ |
| Fragmentation | Writing $\phi$ as a finite product of ball-supported diffeomorphisms |
| Bounded generation | Bound on the number of factors, uniform over the group |



## Further Reading

- John Milnor, *Remarks on infinite dimensional Lie groups*, in Relativity, Groups and Topology II (North-Holland, 1984), for the Fréchet Lie group structure and the regularity of the diffeomorphism groups.
- Hideki Omori, *Infinite-Dimensional Lie Groups* (American Mathematical Society, 1997), for the smoothness of the group operations and the exponential map.
- William Thurston, *Foliations and groups of diffeomorphisms*, Bulletin of the American Mathematical Society 80 (1974), 304–307, for the fragmentation and the simplicity of the diffeomorphism groups.
- John N. Mather, *Commutators of diffeomorphisms*, Commentarii Mathematici Helvetici 49 (1974), 512–528, for the perfectness and the simplicity results.
- Augustin Banyaga, *The structure of classical diffeomorphism groups* (Kluwer, 1997), for the volume-preserving and the symplectic cases, the flux and the Calabi invariant.
- Helmut Hofer, *On the topological properties of symplectic maps*, Proceedings of the Royal Society of Edinburgh 115 (1990), 25–38, for the nondegeneracy of the Hofer metric.
- Helmut Hofer and Eduard Zehnder, *Symplectic Invariants and Hamiltonian Dynamics* (Birkhäuser, 1994), for the energy–capacity inequalities.
- Yakov Eliashberg and Mikhael Gromov, *C^0-rigidity of symplectic and contact structures* (lecture notes, 1996), for the closedness of the $C^0$-closure of the Hamiltonian group.
- Yong-Geun Oh and Stefan Müller, *The group of Hamiltonian homeomorphisms and $C^0$-symplectic topology*, Journal of Symplectic Geometry 5 (2007), 167–219, for the symplectic homeomorphism groups.
- Leonid Polterovich, *The Geometry of the Group of Symplectic Diffeomorphisms* (Birkhäuser, 2001), for the Hofer geometry.
- Dusa McDuff and Dietmar Salamon, *Introduction to Symplectic Topology* (Oxford University Press, 3rd ed. 2017), for the background on the symplectic and volume-preserving groups.
