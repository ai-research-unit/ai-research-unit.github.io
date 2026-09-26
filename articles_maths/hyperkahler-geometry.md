
# __Hyperkähler Geometry__

## Introduction

A **hyperkähler manifold** is a Riemannian manifold carrying three complex structures $J_1, J_2, J_3$ with the quaternionic relations, each of them compatible with the metric in the sense of a Kähler structure. It is the quaternionic analogue of a Kähler manifold, and the passage from one to three complex structures is not a small step: the requirement that the three Kähler forms be closed is a system of equations on the curvature, and its solutions are Ricci-flat. A hyperkähler manifold is at once a quaternionic Kähler manifold with vanishing scalar curvature, a Riemannian manifold with holonomy group contained in $Sp(n)$, and a Calabi–Yau manifold of a special kind. It is the setting for the classical four-dimensional objects — the $K3$ surfaces and the four-torus, the Eguchi–Hanson and Taub–NUT metrics — and for the moduli spaces of the Yang–Mills and Higgs equations in higher dimensions, which are hyperkähler by construction and which are the reason the concept was isolated.

The article is organised around three equivalent descriptions. The first is **complex**: three integrable complex structures with the quaternionic relations, related by a two-sphere of complex structures $\mathbb{I} = aJ_1+bJ_2+cJ_3$ on which the three Kähler forms combine into a two-sphere of Kähler forms. The second is **metric**: the holonomy group is contained in $Sp(n)$, the compact symplectic group, which is one of the entries in Berger's list of irreducible holonomy groups and is the Ricci-flat Kähler case. The third is **algebraic**, through the Bogomolov decomposition of a compact Kähler manifold with $c_1=0$ into tori, Calabi–Yau factors and irreducible hyperkähler factors, and through the hyperkähler quotient, which produces the new examples from old ones.

**The boundaries of the article.** The quaternion algebra is that of Part I'sthe quaternionic structures, the Obata connection and the quaternionic Kähler condition are those of *Quaternionic Geometry*, which is the immediately preceding article of this half, and the Riemannian metric, the Levi-Civita connection, holonomy and Berger's classification are those of *Riemannian Geometry*. The complex structure, the Chern connection and the fundamental form are those of *Hermitian Geometry and Almost Complex Structures*, and the Kähler condition, the Hodge theory and the Ricci form those of *Kähler Geometry*. The Calabi–Yau condition and the Bogomolov decomposition are developed. The hyperkähler quotient and the twistor construction rely on the theory of moment maps for symplectic group actions, which is that of *Symplectic Geometry*, and on the analysis of the Monge–Ampère equation, which belongs to Part III, where the measure and the limit are available; the existence theorems are stated here and their proofs cited. The base field is $\mathbb{R}$ and no physics is invoked.

## Hyperkähler Structures

**Definition.** A **hyperkähler manifold** is a Riemannian manifold $(M,g)$ together with a hypercomplex structure $(J_1,J_2,J_3)$ such that each $J_i$ is an isometry of $g$ and the fundamental form

$$
\Omega_i(X,Y) = g(J_iX,Y)
$$

is closed for $i = 1,2,3$; that is, each $J_i$ is a Kähler structure for the same metric $g$. The four objects $g, \Omega_1, \Omega_2, \Omega_3$ are the **hyperkähler structure**.

Recall from *Quaternionic Geometry* that a hypercomplex structure is a global quaternionic triple of integrable complex structures, equivalently the trivialisation of the rank-three subbundle $\mathcal{Q}$ by three integrable sections $J_1,J_2,J_3$ satisfying $J_1^2=J_2^2=J_3^2=-\mathrm{id}$ and $J_1J_2=J_3$, $J_2J_3=J_1$, $J_3J_1=J_2$, and that the three forms are related to the metric by $\Omega_i(X,Y) = g(J_iX,Y)$.

**Proposition.** Let $(M,g,J_1,J_2,J_3)$ be hyperkähler. Then:

**(a)** each $\Omega_i$ is a symplectic form and each $J_i$ is a compatible almost complex structure in the sense of *Symplectic Geometry*;

**(b)** the three forms $\Omega_1,\Omega_2,\Omega_3$ are the components of a closed two-form with values in the imaginary quaternions, and the combination $\Omega_2+i\Omega_3$ is a holomorphic symplectic form with respect to $J_1$;

**(c)** the metric is determined by the triple: $g(X,Y) = -\Omega_i(J_iX,Y)$ for each $i$;

**(d)** the structure is Ricci-flat and has holonomy contained in $Sp(n)$.

**Proof.** (a) $\Omega_i$ is nondegenerate because it is the fundamental form of a Riemannian metric with $J_i$ an isometry, and it is closed by hypothesis; the compatibility conditions $\Omega_i(J_iX,J_iY)=\Omega_i(X,Y)$ and the positivity of $g$ hold by the Hermitian property. (b) The complex combinations $i\Omega_1+\Omega_2$, etc., are of type $(2,0)$ with respect to the appropriate complex structure; with respect to $J_1$, the form $\Omega_2+i\Omega_3$ is holomorphic because $\Omega_2 = g(J_2\,\cdot\,,\,\cdot\,)$ and $J_2J_1 = -J_1J_2$. (c) $\Omega_i(J_iX,Y) = g(J_i^2X,Y) = -g(X,Y)$ because $J_i$ is an isometry. (d) The parallelism of $J_1,J_2,J_3$ under the Levi-Civita connection is equivalent to the closedness of the three Kähler forms by *Kähler Geometry*, so the holonomy preserves the quaternionic triple, hence lies in $Sp(n)$, the common stabiliser of the three complex structures on the tangent space; a holonomy group inside $Sp(n)$ implies the metric is Ricci-flat, as for any holonomy group fixing a nonzero parallel form. $\square$

**Theorem.** For a Riemannian manifold $(M,g)$ of real dimension $4n$ the following are equivalent:

**(a)** $(M,g)$ admits a hyperkähler structure;

**(b)** the holonomy group of $g$ is contained in $Sp(n)$;

**(c)** $M$ carries three integrable complex structures $J_1,J_2,J_3$ with the quaternionic relations, each Kähler for $g$;

**(d)** $(M,g)$ is quaternionic Kähler with vanishing scalar curvature;

**(e)** $(M,g)$ is Kähler with respect to some complex structure and $g$ is Ricci-flat, and the reduced holonomy group is contained in $Sp(n)$.

**Proof sketch.** (a)$\Leftrightarrow$(c) is the definition. (a)$\Leftrightarrow$(b): a hyperkähler structure is a set of three parallel complex structures, and the holonomy group must preserve them, so it lies in their common stabiliser $Sp(n)$; conversely a holonomy group contained in $Sp(n)$ preserves the standard quaternionic triple on each tangent space, and these patch to three parallel complex structures. (b)$\Leftrightarrow$(e): $Sp(n)\subseteq SU(2n)$ and the holonomy group of a $Sp(n)$-manifold is Ricci-flat, while a Ricci-flat Kähler metric with holonomy not in $Sp(n)$ would have holonomy in $SU(2n)$ alone. (a)$\Leftrightarrow$(d): $Sp(n)\subseteq Sp(n)\cdot Sp(1)$ and the nonvanishing scalar curvature of a quaternionic Kähler manifold measures the $Sp(1)$-part of the holonomy connection; it vanishes exactly when the holonomy reduces to $Sp(n)$. $\square$

**Remark.** The equivalence (b) places the hyperkähler manifolds in Berger's list of possible irreducible holonomy groups of a Riemannian metric, which are $SO(n)$, $U(n)$, $SU(n)$, $Sp(n)$, $Sp(n)\cdot Sp(1)$, $G_2$ and $\mathrm{Spin}(7)$. The $Sp(n)$ case is the only one of the two quaternionic entries that has a Ricci-flat metric, and the $Sp(n)\cdot Sp(1)$ entry is the quaternionic Kähler one of *Quaternionic Geometry*; the $SU(n)$ entry gives the Calabi–Yau manifolds, and the last two the exceptional holonomy geometries of $G_2$ and $\mathrm{Spin}(7)$ Manifolds. In real dimension four the possibilities collapse: $Sp(1)=SU(2)$, so a hyperkähler four-manifold is a Ricci-flat Kähler surface with holonomy in $SU(2)$, and the compact examples are the four-torus and the $K3$ surfaces.

## The Sphere of Complex Structures

Even though the hyperkähler structure contains only three complex structures, it contains a whole two-sphere of them.

**Proposition.** Let $(M,g,J_1,J_2,J_3)$ be hyperkähler and let $a,b,c$ be real numbers with $a^2+b^2+c^2=1$. Put

$$
\mathbb{I} = aJ_1 + bJ_2 + cJ_3,
$$

the linear combination in the bundle $\mathcal{Q}$ with constant coefficients $a,b,c$. Then $\mathbb{I}$ is an integrable complex structure and a Kähler structure for $g$, with fundamental form

$$
\Omega_{\mathbb{I}} = a\Omega_1 + b\Omega_2 + c\Omega_3 .
$$

The assignment $(a,b,c)\mapsto \mathbb{I}$ is a bijection from $S^2$ onto the set of complex structures on $M$ that lie in $\mathcal{Q}$ and are Kähler for $g$. It is the **twistor sphere** of the hyperkähler structure.

**Proof.** For real $a,b,c$, the endomorphism $\mathbb{I} = aJ_1+bJ_2+cJ_3$ satisfies $\mathbb{I}^2 = -(a^2+b^2+c^2)\mathrm{id}$ by the anticommutation relations, so on the unit sphere it is an almost complex structure; the form $\Omega_{\mathbb{I}}(X,Y) = g(\mathbb{I}X,Y)$ is closed as a linear combination of closed forms and is nondegenerate, so the metric is Hermitian for $\mathbb{I}$ and $\Omega_{\mathbb{I}}$ is its fundamental form. Finally $\mathbb{I}$ is a parallel section of $\mathcal{Q}$: each $J_i$ is parallel for the Levi-Civita connection because its Kähler form is closed, and the coefficients $a,b,c$ are constants, so $\nabla\mathbb{I}=0$; a parallel almost complex structure is integrable by the Newlander–Nijenhuis theorem. $\square$

**Remark.** The twistor sphere is the fibre of the twistor space $Z(M)$ of *Quaternionic Geometry* over a point, and the collection of Kähler forms $\Omega_{\mathbb{I}}$ is a two-sphere of symplectic forms, all compatible with the same metric. The hyperkähler condition is thus exactly the statement that the two-sphere of complex structures is constant: it is a parallel section of the twistor bundle, and the vanishing of the scalar curvature in the quaternionic Kähler hierarchy is the flatness of this sphere in the twistor connection.

## The Hyperkähler Quotient

The construction that produces most known examples from simpler ones is a quotient by a group action, and it requires a moment map for each of the three symplectic forms.

**Definition.** Let $(M,g,J_1,J_2,J_3)$ be a hyperkähler manifold and let a Lie group $K$ act on $M$ preserving $\mathcal{Q}$ and $g$. A **hyperkähler moment map** for the action is a map

$$
\mu = (\mu_1,\mu_2,\mu_3) : M \longrightarrow \mathfrak{k}^*\otimes\mathbb{R}^3,
$$

where each $\mu_i:M\to\mathfrak{k}^*$ is a moment map for the action on the symplectic manifold $(M,\Omega_i)$, and $\mathfrak{k}$ is the Lie algebra of $K$. Its components satisfy $d\langle\mu_i, \xi\rangle = \iota_{\xi_M}\Omega_i$ for the fundamental vector field $\xi_M$ of $\xi\in\mathfrak{k}$, the sign convention of *Symplectic Geometry*.

**Theorem (hyperkähler quotient).** Let $K$ act on a hyperkähler manifold $M$ with a hyperkähler moment map $\mu$, and let the action be free and proper on the common zero locus $\mu^{-1}(0)$. Then the quotient

$$
M \sslash\!\!/ K = \mu^{-1}(0)/K
$$

is a smooth manifold carrying an induced hyperkähler structure, of dimension $\dim M - 4\dim K$. It is the **hyperkähler quotient**.

**Proof sketch.** The quotient is a manifold by the free proper action and the equivariance of $\mu$, and the restriction of $g$ to $\mu^{-1}(0)$ induces a metric on the quotient by the usual slice argument. The three forms $\Omega_i$ descend because the action is Hamiltonian for each, with the zero level as its moment level; the compatibility of the descended forms with the descended complex structures is the statement that the horizontal distribution is invariant under the three $J_i$, which follows from the equivariance of the moment maps. $\square$

**Remark.** The hyperkähler quotient is the simultaneous version of the symplectic quotient of *Symplectic Geometry* and reduces the dimension by $4\dim K$, one fourfold per generator, exactly as the quaternionic dimension demands. The construction produces the moduli spaces of instantons and of Higgs bundles, and the ALE gravitational instantons as quotients of flat quaternionic space; it is the reason the hyperkähler condition appears naturally in the study of moduli problems, where the three moment maps are the three components of the self-duality equations.

## Examples

**Example (flat quaternionic space).** On $\mathbb{H}^n$ with the Euclidean metric and the constant triple, the three Kähler forms have constant coefficients and are closed; the metric is flat and its holonomy is trivial, contained in $Sp(n)$. Quotients by lattices give compact flat hyperkähler manifolds of any real dimension $4n$, the flat quaternionic tori, which are Kähler with respect to each of the three inherited complex structures and have trivial holonomy.

**Example (four-dimensional hyperkähler manifolds).** A hyperkähler four-manifold is a Ricci-flat Kähler surface, and the compact ones are the four-torus $T^4$ and the $K3$ surfaces. Both are quaternionic Kähler with vanishing scalar curvature; the $K3$ surface with its Yau metric has holonomy exactly $Sp(1)=SU(2)$, while the flat torus has trivial holonomy. In real dimension four the twistor sphere is the sphere of complex structures used in the twistor theory of self-dual Einstein manifolds.

**Example (ALE and the Kleinian singularities).** Let $\Gamma\subseteq SU(2)$ be a finite subgroup. The quotient $\mathbb{C}^2/\Gamma$ is a Kleinian singularity and its minimal resolution carries a hyperkähler metric, the **ALE metric** (asymptotically locally Euclidean), obtained as a hyperkähler quotient of flat quaternionic space by the action of $\Gamma$ or by the Gibbons–Hawking construction. For the cyclic group $\Gamma = \mathbb{Z}/n$ the resulting four-manifold is the $A_{n-1}$ ALE space, whose exceptional divisor is a chain of $n-1$ rational curves with intersection matrix the Cartan matrix of $A_{n-1}$.

**Example (Eguchi–Hanson and Taub–NUT).** The Eguchi–Hanson metric is the $A_1$ ALE metric on the cotangent bundle $T^*\mathbb{CP}^1$, a four-dimensional hyperkähler metric that is asymptotically locally Euclidean; the Taub–NUT metric is a complete four-dimensional hyperkähler metric on $\mathbb{R}^4$ with a circle action and a different asymptotic behaviour. Both are constructed by the Gibbons–Hawking ansatz, in which a hyperkähler metric with a triholomorphic circle action is encoded in a harmonic function on a three-dimensional quotient, and both have complete non-compact ends.

**Example (Hilbert schemes and Kummer varieties).** For a $K3$ surface $S$, the Hilbert scheme $S^{[n]}$ of length-$n$ subschemes is a compact hyperkähler manifold of complex dimension $2n$, the metric being the one induced from the hyperkähler structure on $S$; for an abelian surface $A$, the generalised Kummer variety $K_n(A)$ is the fibre of the sum map on $A^{[n+1]}$, of complex dimension $2n$, and is likewise compact hyperkähler. These manifolds are the two infinite families of irreducible compact hyperkähler manifolds, and the deformation classification of the compact irreducible examples in each dimension is known only in low dimension.

**Example (moduli of Higgs bundles).** Let $\Sigma$ be a compact Riemann surface of genus $g\geq2$ and let $M_H$ be the moduli space of stable Higgs bundles of rank $n$ and degree $d$ on $\Sigma$. The space $M_H$ is a complete hyperkähler manifold of complex dimension $2n^2(g-1)+2$, and the hyperkähler structure is the reason it can be viewed as a complex integrable system; the three Kähler forms come from the three natural complex structures, and the hyperkähler quotient construction produces it from an infinite-dimensional flat space. The metric is the $L^2$-metric on the moduli of solutions of the self-duality equations, and the analysis of its existence uses the Fredholm theory of Part III.

**Example (the Calabi–Yau fourfolds of holonomy $Sp(2)$).** An irreducible hyperkähler manifold of complex dimension four has holonomy $Sp(2)$ and is a Calabi–Yau fourfold that is not a product and carries a holomorphic symplectic form. In this dimension the irreducible examples are constructed from deformations of the Hilbert schemes $S^{[2]}$ of $K3$ surfaces, and their period theory is the higher-dimensional analogue of the period map for $K3$ surfaces.

## The Bogomolov Decomposition and the Place of Hyperkähler Geometry

**Theorem (Bogomolov decomposition, statement).** Let $M$ be a compact Kähler manifold with $c_1(M)=0$ in $H^2(M;\mathbb{R})$. Then $M$ has a finite étale cover

$$
\tilde M = T \times \prod_{i} Y_i \times \prod_{j} Z_j,
$$

where $T$ is a complex torus, each $Y_i$ is a simply connected Calabi–Yau manifold of complex dimension at least $3$ with holonomy $SU(\dim_{\mathbb{C}}Y_i)$, each $Z_j$ is a simply connected irreducible hyperkähler manifold with holonomy $Sp(\dim_{\mathbb{C}}Z_j/2)$, and the decomposition is unique up to order and isometry.

**Proof sketch.** The holonomy group of a compact Ricci-flat Kähler metric is a product of the irreducible pieces of Berger's list, namely $SU(m)$, $Sp(k)$ and the trivial group; the de Rham decomposition turns the product of holonomy groups into a metric product, and the simply connected factors are the Calabi–Yau and hyperkähler ones, while a flat factor of complex dimension $1$ contributes the torus. The uniqueness of the decomposition follows from the uniqueness of the de Rham decomposition and the fact that the Calabi–Yau and hyperkähler factors have distinct holonomy groups. $\square$

**Remark.** The decomposition is the structural result about the hyperkähler world: among the compact Kähler manifolds with vanishing first Chern class, the hyperkähler ones are exactly those whose holonomy group is $Sp(k)$ rather than the larger $SU(2k)$. Every hyperkähler manifold is Calabi–Yau — its holonomy is contained in $SU(2k)$, and the holomorphic symplectic form $\sigma = \Omega_2+i\Omega_3$ has the nowhere vanishing top power $\sigma^{\wedge k}$, a holomorphic volume form — but the converse fails, and the difference is exactly the existence of a second and third complex structure. The Calabi–Yau theory, in which the holonomy $SU(n)$ case and its Hodge theory are developed, is not treated here; the twistor space of the hyperkähler structure is that of *Quaternionic Geometry*.

**Remark.** The hyperkähler manifolds with their holonomy group $Sp(n)$ are the extremal case of the scalar curvature trichotomy of quaternionic Kähler geometry: positive scalar curvature gives the Wolf spaces, negative scalar curvature gives the solvable and symmetric models, and zero scalar curvature gives exactly the hyperkähler manifolds, which are the only ones of the three on which the twistor sphere is parallel rather than merely local.

## Summary

A hyperkähler manifold is a Riemannian manifold with a hypercomplex structure $(J_1,J_2,J_3)$ for which all three fundamental forms $\Omega_i(X,Y)=g(J_iX,Y)$ are closed, so that the metric is simultaneously Kähler for the three complex structures. Equivalently the holonomy group is contained in $Sp(n)$; equivalently the manifold is quaternionic Kähler with vanishing scalar curvature; equivalently it is a Ricci-flat Kähler manifold whose reduced holonomy lies in $Sp(n)$ rather than the larger $SU(2n)$. In real dimension four the condition becomes that of a Ricci-flat Kähler surface, with the four-torus and the $K3$ surfaces as the compact examples.

The hyperkähler structure contains a two-sphere of complex structures $\mathbb{I}=aJ_1+bJ_2+cJ_3$ with $a^2+b^2+c^2=1$, all Kähler for the same metric, with Kähler forms $\Omega_{\mathbb{I}}=a\Omega_1+b\Omega_2+c\Omega_3$; this twistor sphere is the fibre of the twistor space. The hyperkähler quotient of a hyperkähler manifold by a group action with three moment maps is again hyperkähler and reduces the dimension by four times the dimension of the group.

The examples are the flat quaternionic spaces and their torus quotients, the compact hyperkähler four-manifolds $T^4$ and $K3$, the ALE gravitational instantons with their Eguchi–Hanson and Taub–NUT metrics, the Hilbert schemes $S^{[n]}$ of $K3$ surfaces and the generalised Kummer varieties $K_n(A)$, and the moduli spaces of Higgs bundles. The Bogomolov decomposition expresses every compact Kähler manifold with $c_1=0$, up to finite étale cover, as a product of a torus, Calabi–Yau factors with holonomy $SU(m)$ and irreducible hyperkähler factors with holonomy $Sp(k)$; the hyperkähler manifolds are the Calabi–Yau manifolds of even complex dimension whose holonomy is the smaller group, and the theory of the $SU(n)$ case is .

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M$, $g$ | Riemannian manifold and its metric (from *Riemannian Geometry*) |
| $J_1, J_2, J_3$ | The hypercomplex triple: $J_i^2=-\mathrm{id}$, $J_1J_2=J_3$, $J_2J_3=J_1$, $J_3J_1=J_2$ |
| $\mathcal{Q}$ | The rank-three subbundle of $\mathrm{End}(TM)$ (from *Quaternionic Geometry*) |
| $\Omega_i(X,Y) = g(J_iX,Y)$ | The three Kähler forms; closed, nondegenerate, $g(X,Y)=-\Omega_i(J_iX,Y)$ |
| $Sp(n)$ | Compact symplectic group, $\dim n(2n+1)$; holonomy group of a hyperkähler manifold |
| $\mathbb{I}=aJ_1+bJ_2+cJ_3$ | The sphere of complex structures, $a^2+b^2+c^2=1$ |
| $\Omega_{\mathbb{I}}=a\Omega_1+b\Omega_2+c\Omega_3$ | Corresponding Kähler form |
| $Z(M)$ | Twistor space of *Quaternionic Geometry*; its fibre at $x$ is the sphere of complex structures |
| $\mu=(\mu_1,\mu_2,\mu_3)$ | Hyperkähler moment map, $\mu_i$ a moment map for $\Omega_i$ |
| $M \sslash\!\!/ K = \mu^{-1}(0)/K$ | Hyperkähler quotient, $\dim = \dim M - 4\dim K$ |
| $\nabla$, $\mathrm{Ric}$ | Levi-Civita connection and Ricci tensor (from *Riemannian Geometry*); $\mathrm{Ric}=0$ here |
| ALE | Asymptotically locally Euclidean; the hyperkähler resolution of $\mathbb{C}^2/\Gamma$ |
| Bogomolov decomposition | $\tilde M = T\times\prod Y_i\times\prod Z_j$ for a compact Kähler $M$ with $c_1=0$ |



## Further Reading

- Marcel Berger, "Sur les groupes d'holonomie homogènes de variétés à connexion affine et des variétés riemanniennes", *Bulletin de la Société Mathématique de France* 83 (1955), 279–330, for the classification of holonomy groups containing $Sp(n)$.
- Fedor A. Bogomolov, "On the Decomposition of Kähler Manifolds with Trivial Canonical Class", *Mathematics of the USSR-Izvestiya* 8 (1974), 55–80, for the decomposition theorem.
- Arnaud Beauville, "Variétés Kähleriennes dont la première classe de Chern est nulle", *Journal of Differential Geometry* 18 (1983), 755–782, for the hyperkähler structure on $S^{[n]}$ and $K_n(A)$ and for the decomposition refined to isometry.
- Nigel Hitchin, Anders Karlhede, Ulf Lindström and Martin Roček, "Hyperkähler Metrics and Supersymmetry", *Communications in Mathematical Physics* 108 (1987), 535–589, for the hyperkähler quotient and the twistor construction.
- Nigel Hitchin, "The Self-Duality Equations on a Riemann Surface", *Proceedings of the London Mathematical Society* 55 (1987), 59–126, for the hyperkähler structure on the moduli space of Higgs bundles.
- Michael Atiyah and Nigel Hitchin, *The Geometry and Dynamics of Magnetic Monopoles* (Princeton University Press, 1988), for the hyperkähler metrics of the ALE and Taub–NUT families.
- Dominic Joyce, *Compact Manifolds with Special Holonomy* (Oxford University Press, 2000), for the place of $Sp(n)$ and $Sp(n)\cdot Sp(1)$ among the holonomy geometries.
- Gang Tian and Shing-Tung Yau, "Compact Kähler Manifolds with Zero First Chern Class", *Journal of the American Mathematical Society* 3 (1990), 579–609, for the existence theory underlying the decomposition.
