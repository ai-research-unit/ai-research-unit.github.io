
# __Kähler Geometry__

## Introduction

A **Kähler manifold** is a complex manifold with a Hermitian metric whose fundamental form $\Omega$ is closed. The condition is a single equation, but it reconciles three structures at once: the complex structure $J$, the Riemannian metric $g$, and the symplectic form $\Omega$. On a Kähler manifold the Levi-Civita connection preserves the complex structure, the Chern connection coincides with it, the complex structure is parallel, and the curvature tensor has the symmetries of a unitary holonomy group. The result is the most rigid and the most computable setting in differential geometry, and it is the ambient category for the algebraic geometry of projective varieties.

This article develops the Kähler condition and its consequences. It states the equivalent formulations of the Kähler condition — the closedness of $\Omega$, the parallelism of $J$ for the Levi-Civita connection, the local existence of a Kähler potential, and the reduction of the holonomy group to $U(n)$ — and treats the standard examples, the complex projective space with its Fubini–Study metric above all. It then develops the two central machines that the condition makes available: the Hodge theory of a compact Kähler manifold, whose analytic proofs are deferred to Part III, and the Lefschetz operators, whose $sl_2$ structure packages the cohomology. It closes with the Ricci form and the Kähler–Einstein condition, which is the doorway.

**The boundaries of the article.** The Riemannian metric, the Levi-Civita connection, the curvature tensor, the Ricci tensor and the holonomy group are those of the companion article *Riemannian Geometry*, and are used without derivation. The almost complex structures, the Nijenhuis tensor, the Hermitian metrics, the fundamental form $\Omega(X,Y) = g(JX,Y)$ and the Chern connection are those, which is the immediately preceding article of this half; they are assumed. The symplectic structure on a Kähler manifold, the Darboux theorem and the compatible almost complex structures are those of *Symplectic Geometry*. The Laplace operator on forms, harmonic forms, Hodge theory and the finiteness of the cohomology of the $\bar\partial$-complex require the measure, the limit and the theory of elliptic operators, which belong to Part III, where the measure and the limit are available; the results are stated here and their proofs deferred there in that explicit form. The Chern classes of a complex manifold and their expression through the curvature of a connection are those of *Characteristic Classes*, earlier in this Part; the article states the identity $[\rho] = 2\pi c_1(M)$ and cites it. The projective and algebraic-geometric consequences — the Kodaira embedding theorem, the structure of algebraic varieties, the Hodge conjecture — belong to algebraic geometry and are only pointed at. The base field is $\mathbb{R}$ and no physics is invoked.

## Kähler Manifolds

**Definition.** A **Kähler manifold** is a Hermitian manifold $(M, J, g)$ — a complex manifold with a Hermitian metric — whose fundamental form

$$
\Omega(X,Y) = g(JX,Y)
$$

is closed: $d\Omega = 0$. The form $\Omega$ is then the **Kähler form**, the metric $g$ is a **Kähler metric**, and the triple $(M,J,g)$ is a **Kähler structure**.

Since $\Omega$ is a real $(1,1)$-form, the closedness has a sharper form on a complex manifold.

**Proposition.** Let $(M,J,g)$ be a Hermitian manifold with fundamental form $\Omega$, of type $(1,1)$. Then

$$
d\Omega = 0 \iff \partial\Omega = 0 \iff \bar\partial\Omega = 0,
$$

and in that case $\Omega$ is locally of the form $i\partial\bar\partial\varphi$ for a real function $\varphi$.

**Proof.** Since $\Omega$ has bidegree $(1,1)$, the exterior derivative splits as $d\Omega = \partial\Omega + \bar\partial\Omega$ with $\partial\Omega$ of bidegree $(2,1)$ and $\bar\partial\Omega$ of bidegree $(1,2)$; the two have different bidegrees, so their sum vanishes exactly when each vanishes. The local form $i\partial\bar\partial\varphi$ is the Poincaré lemma for $\bar\partial$ combined with the reality of $\Omega$: a closed real $(1,1)$-form is locally $\bar\partial$-exact up to the conjugate, which is the content of the $\partial\bar\partial$-lemma on a polydisc. $\square$

**Theorem (characterisations of the Kähler condition).** Let $(M, J, g)$ be a Hermitian manifold of complex dimension $n$ with fundamental form $\Omega$ and Levi-Civita connection $\nabla$. The following are equivalent:

**(a)** $d\Omega = 0$;

**(b)** $\nabla J = 0$;

**(c)** the Chern connection of the Hermitian structure coincides with the Levi-Civita connection of $g$;

**(d)** about every point there are holomorphic coordinates and a real function $\varphi$ with $\Omega = i\,\partial\bar\partial\varphi$, equivalently $g_{i\bar j} = \partial_i\partial_{\bar j}\varphi$;

**(e)** the holonomy group of $g$ is contained in $U(n)$;

**(f)** about every point there are holomorphic coordinates in which the Kähler metric has the form $g_{i\bar j} = \delta_{ij} + O(|z|^2)$.

**Proof sketch.** (a) $\Leftrightarrow$ (b): for a Hermitian manifold, the $(0,3)$-tensor field $\nabla J$ and the $3$-form $d\Omega$ are related by the identity of Goldberg, which expresses each component of $\nabla J$ at a point as a linear combination of the components of $d\Omega$ at that point with universal coefficients; since $g$ is positive definite the vanishing of one is therefore equivalent to the vanishing of the other. (b) $\Leftrightarrow$ (c): a connection which preserves $g$ and $J$ and whose torsion has vanishing $(0,2)$-part is by definition the Chern connection, and that connection is unique; the Levi-Civita connection of $g$ is torsion-free, so if it preserves $J$ it satisfies the defining properties of the Chern connection and coincides with it, and conversely the Chern connection preserves $J$. (b) $\Leftrightarrow$ (e): $J$ is a parallel tensor field, so it is preserved by the holonomy representation, and a parallel complex structure on the tangent space is exactly a reduction of the holonomy group to $U(n)$. (a) $\Leftrightarrow$ (d): the closedness gives the local potential as in the previous proposition, and the converse is immediate from $d^2 = 0$; the coordinate statement is $\Omega = i\sum_{i,j}\partial_i\partial_{\bar j}\varphi\,dz^i\wedge d\bar z^j$. (f): the Taylor expansion of a potential normalised at a point; the first-order terms vanish after a holomorphic change of coordinates, and conversely the vanishing of all the first derivatives $\partial_k g_{i\bar j}$ at a point implies $\partial\Omega = 0$ there. $\square$

**Corollary.** A Kähler manifold is symplectic: the Kähler form $\Omega$ is closed and nondegenerate, being the fundamental form of a Riemannian metric, and the almost complex structure $J$ is compatible with it in the sense of *Symplectic Geometry*. In particular every Kähler manifold is orientable, and the volume form $\Omega^{\wedge n}/n!$ is the Riemannian volume.

**Proof.** $\Omega^\flat = g(J\,\cdot\,,\,\cdot\,)$ is an isomorphism because $g$ is positive definite and $J$ invertible, so $\Omega$ is nondegenerate, and it is closed by assumption. The compatibility $\Omega(JX,JY)=\Omega(X,Y)$ and the positivity $g_J(X,Y)=\Omega(X,JY)=g(X,Y)$ hold by the Hermitian property. $\square$

**Remark.** The chain of conditions in the theorem is the reason the Kähler condition sits at the meeting point of three subjects: it is a condition of closedness (symplectic), of integrability (complex) and of parallel transport (Riemannian), and each of the three viewpoints has its own use. The containment of the Kähler manifolds in the symplectic manifolds is strict: the Kodaira–Thurston manifold is a compact symplectic four-manifold with $b_1 = 3$, while a compact Kähler manifold has even first Betti number, so it carries no Kähler metric. The Kähler manifolds are exactly the Hermitian manifolds whose Chern connection is torsion-free, and this is the sense in which they are the integrable case.

## The Kähler Potential and Local Structure

**Definition.** A **Kähler potential** for a Kähler manifold is a real function $\varphi$ on an open set with

$$
\Omega = i\,\partial\bar\partial\varphi .
$$

**Proposition.** A Kähler potential exists locally on every Kähler manifold, and two potentials on a connected open set differ by the real part of a holomorphic function: $\varphi' = \varphi + f + \bar f$ with $f$ holomorphic.

**Proof.** The local existence is condition (d) of the theorem. For uniqueness, put $\psi = \varphi'-\varphi$, so that $\psi$ is real and $\partial\bar\partial\psi = 0$; then $\bar\partial(\partial\psi) = 0$, so the $(1,0)$-form $\partial\psi$ is holomorphic, hence closed, hence locally of the form $\partial\psi = df$ with $f$ holomorphic; conjugating the last identity and using that $\psi$ is real gives $\bar\partial\psi = d\bar f$, and therefore $d\psi = \partial\psi + \bar\partial\psi = d(f+\bar f)$, so that $\psi = f+\bar f$ up to an additive constant. $\square$

**Example.** On $\mathbb{C}^n$ with the Euclidean metric the potential $\varphi = \tfrac12\sum_{i=1}^n |z_i|^2$ gives

$$
i\,\partial\bar\partial\varphi = \frac{i}{2}\sum_{i=1}^n dz_i\wedge d\bar z_i = \sum_{i=1}^n dx_i\wedge dy_i = \Omega_0,
$$

using $i\,dz\wedge d\bar z = 2\,dx\wedge dy$; so the flat metric is Kähler. The potential is not unique: $\varphi + f + \bar f$ gives the same form.

**Remark.** The Kähler potential is the local primitive of the Kähler form and is thus the Kähler analogue of the existence of a symplectic potential $\theta$ with $\omega = -d\theta$; the difference is that the potential is a function rather than a $1$-form, because the Kähler form has the extra type. The equality $\Omega = i\partial\bar\partial\varphi$ is the reason the local theory of Kähler metrics is the theory of a single real function, and the reason the global existence of a potential is obstructed by the cohomology class $[\Omega]$.

**Proposition (Kähler normal coordinates).** Let $(M,J,g)$ be Kähler and let $p \in M$. There are holomorphic coordinates $z$ centred at $p$ with

$$
g_{i\bar j}(z) = \delta_{ij} + O(|z|^2), \qquad \text{that is} \quad \Omega = \sum_i dx_i\wedge dy_i \text{ at } p .
$$

**Proof.** Choose holomorphic coordinates and expand the potential about $p$; the terms of first order can be removed by a holomorphic change of coordinates, and the real quadratic part can be brought to the identity by a unitary linear transformation on the coordinates. $\square$

**Remark.** Kähler normal coordinates show that a Kähler manifold has no first-order local invariants: the curvature is genuinely a second-order object, and the curvature is the only local invariant of a Kähler metric. This is the Kähler counterpart of the Darboux theorem of *Symplectic Geometry* and of the existence of normal coordinates for a Riemannian metric, in *Riemannian Geometry*, being written in parallel.

## Examples

**Example (complex Euclidean space and tori).** $\mathbb{C}^n$ with the Euclidean metric is Kähler, as above. A quotient $\mathbb{C}^n/\Lambda$ by a lattice is Kähler with the induced flat metric: the fundamental form has constant coefficients, hence is closed. Complex tori are thus Kähler, and they are the flat Kähler manifolds with infinite fundamental group.

**Example (complex projective space).** On the affine chart $\mathbb{C}^n \subseteq \mathbb{CP}^n$ with coordinates $z_1,\ldots,z_n$, the **Fubini–Study form** is

$$
\Omega_{FS} = i\,\partial\bar\partial\log(1 + |z|^2), \qquad |z|^2 = \sum_{i=1}^n |z_i|^2 .
$$

It is closed because it is $\partial\bar\partial$ of a function, and the associated Hermitian matrix $g_{i\bar j} = \partial_i\partial_{\bar j}\log(1+|z|^2)$ is

$$
g_{i\bar j} = \frac{\delta_{ij}(1+|z|^2) - \bar z_i z_j}{(1+|z|^2)^2},
$$

which is positive definite; so $\Omega_{FS}$ is a Kähler form. On $n = 1$ one computes $\Omega_{FS} = \frac{2\,dx\wedge dy}{(1+x^2+y^2)^2}$ and

$$
\int_{\mathbb{CP}^1}\Omega_{FS} = 2\pi,
$$

so that $[\Omega_{FS}/(2\pi)]$ is a positive generator of $H^2(\mathbb{CP}^n;\mathbb{Z})$; the powers $[\Omega_{FS}]^k/(2\pi)^k$ are the integral generators of $H^{2k}$, and the Hodge numbers are $h^{p,q} = 1$ for $0 \leq p = q \leq n$ and $h^{p,q} = 0$ otherwise. The Fubini–Study metric is the model compact Kähler metric and the quotient of the sphere $S^{2n+1}$ by the Hopf $U(1)$-action of *Contact Geometry*.

**Example (Hermitian symmetric spaces).** A compact Hermitian symmetric space $G/H$ of a semisimple Lie group carries an invariant Kähler structure, and its Kähler form is integral. The Grassmannians, the quadrics and the complex projective spaces are the classical cases, and the classification of the irreducible ones is that of the Cartan domains. The Lie-theoretic input is that of *Lie Groups* and its companions.

**Example (submanifolds and products).** A complex submanifold $N \subseteq M$ of a Kähler manifold is Kähler with the restricted structure: the restriction of $\Omega$ is closed and nondegenerate on $N$ because $TN$ is complex, and the restriction of $g$ is Hermitian. A product of Kähler manifolds is Kähler, the Kähler form being the sum of the pullbacks. A blow-up of a compact Kähler manifold along a complex submanifold is Kähler.

**Example (Riemann surfaces).** A Riemann surface with any Hermitian metric is Kähler, because a $2$-form on a surface is automatically closed. In complex dimension one the Kähler condition is vacuous, and the geometry of Riemann surfaces is the geometry of their conformal structures, which is not developed here.

**Example (Kodaira–Thurston).** The Kodaira–Thurston manifold is the quotient of the Heisenberg group by a lattice, equivalently a $T^2$-bundle over $T^2$; it is compact, symplectic and **not** Kähler, since $b_1 = 3$ is odd whereas a compact Kähler manifold has even first Betti number. The example shows that the Kähler condition is strictly stronger than the symplectic one and that the Hodge-theoretic constraints below are not formal.

## Hodge Theory of a Compact Kähler Manifold

The Kähler condition gives the exterior algebra of forms a second grading and forces the Laplace operators of the three natural complexes to agree.

**Theorem (Kähler identities).** Let $(M,J,g)$ be a Kähler manifold with Lefschetz operator $L\alpha = \Omega\wedge\alpha$ and its formal adjoint $\Lambda = L^*$. Then

$$
[\Lambda, \partial] = i\,\bar\partial^*, \qquad [\Lambda, \bar\partial] = -i\,\partial^*,
$$

and consequently the Laplace operators satisfy

$$
\Delta_d = 2\,\Delta_\partial = 2\,\Delta_{\bar\partial}, \qquad \partial\bar\partial^* + \bar\partial^*\partial = 0, \qquad \partial^*\bar\partial + \bar\partial\partial^* = 0 .
$$

**Proof sketch.** The identities are a computation in local holomorphic normal coordinates, using the Clifford-algebra relation satisfied by the operators of exterior multiplication and contraction and the compatibility of the Kähler form with the frame; the consequence for the Laplacians follows from the Kähler identities together with the definitions $\Delta_d = d d^* + d^*d$ and $\Delta_{\bar\partial} = \bar\partial\bar\partial^* + \bar\partial^*\bar\partial$. $\square$

**Theorem (Hodge decomposition for a compact Kähler manifold).** Let $M$ be a compact Kähler manifold of complex dimension $n$. Then the cohomology of $M$ with complex coefficients decomposes by type,

$$
H^k(M;\mathbb{C}) = \bigoplus_{p+q=k}H^{p,q}(M), \qquad H^{p,q}(M) = \overline{H^{q,p}(M)},
$$

with $H^{p,q}(M) \cong H^{p,q}_{\bar\partial}(M)$, so that $h^{p,q} = h^{q,p}$, and $H^{p,q} = 0$ unless $0 \leq p,q \leq n$. Consequently the Betti numbers satisfy $b_k = \sum_{p+q=k}h^{p,q}$, the odd Betti numbers $b_{2k+1}$ are even, and $b_{2k} \geq 1$ for $0 \leq k \leq n$.

**Proof sketch.** The analysis: the Hodge theorem for the Laplace operator on a compact manifold identifies de Rham cohomology with the space of harmonic forms, and the equality $\Delta_d = 2\Delta_{\bar\partial}$ of the Kähler identities identifies the harmonic forms with those harmonic for $\Delta_{\bar\partial}$, which are exactly the $\bar\partial$-harmonic representatives of the Dolbeault groups. This identification is the content of the elliptic theory of $\Delta_{\bar\partial}$, and its proof — existence of a parametrix, compactness of the resolvent, the finiteness of the cohomology of an elliptic complex — belongs to Part III, where the measure and the limit are available. The type decomposition follows from $\Delta_d = 2\Delta_{\bar\partial}$ and the fact that $\Delta_{\bar\partial}$ preserves bidegree; conjugation follows from the reality of the Laplace operator; $b_{2k}\geq1$ because $[\Omega]^k \neq 0$, its top power being a nonzero multiple of the volume. $\square$

**Corollary.** A compact Kähler manifold has even first Betti number and satisfies $b_2 \geq 1$; more generally all odd Betti numbers are even and $b_{2k}\geq1$ for $k$ in the range above. A compact complex manifold that fails any of these conditions, the Hopf manifold among them, admits no Kähler metric.

**Remark.** The decomposition is the deepest consequence of the Kähler condition and the origin of Hodge theory. The analytic input is genuinely needed: the finiteness of the Dolbeault cohomology is a theorem of elliptic analysis, and the equality of the three Laplacians is what makes the grading topological. Part III supplies the analysis; this article supplies the algebra and the geometry that make the analysis applicable. The Hodge–Riemann bilinear relations, which put a definite signature on the cohomology of a projective manifold, are stated and proved within the same analytic framework.

## The Lefschetz Operators and Hard Lefschetz

**Definition.** For a compact Kähler manifold $(M,\Omega)$ of complex dimension $n$ and real dimension $2n$, the **Lefschetz operator** is

$$
L : \Omega^\bullet(M) \longrightarrow \Omega^{\bullet+2}(M), \qquad L\alpha = \Omega\wedge\alpha,
$$

and its adjoint is $\Lambda = L^*$. The **degree operator** is $H = \sum_k (k-n)\,\Pi_k$, where $\Pi_k$ is the projection onto the $k$-forms; equivalently $H\alpha = (k-n)\alpha$ for $\alpha$ of degree $k$.

**Theorem.** On a compact Kähler manifold the operators $L, \Lambda, H$ satisfy

$$
[H, L] = 2L, \qquad [H, \Lambda] = -2\Lambda, \qquad [L, \Lambda] = H,
$$

so that they define a representation of the Lie algebra $\mathfrak{sl}_2(\mathbb{R})$ on the cohomology $H^\bullet(M;\mathbb{R})$, with $L$ raising, $\Lambda$ lowering and $H$ measuring the degree.

**Proof sketch.** The relation $[L,\Lambda]=H$ is the algebraic Kähler identity: $L$ and $\Lambda$ are the operators of exterior multiplication and of contraction by the Kähler form, and their commutator acts on a $k$-form as multiplication by $n-k$, a pointwise statement about the compatible pair $(g,J)$. The other two relations are the bidegree behaviour of $L$ and $\Lambda$. The relations pass to cohomology because $dL = Ld$, which is the closedness of $\Omega$, and because $\Lambda$ is the adjoint of $L$. $\square$

**Definition.** A cohomology class $\alpha \in H^k(M;\mathbb{R})$ is **primitive** if $\Lambda\alpha = 0$. The **Lefschetz decomposition** is

$$
H^k(M;\mathbb{R}) = \bigoplus_{j\geq0} L^j\,P^{k-2j}(M), \qquad P^\bullet(M) = \ker\Lambda .
$$

**Theorem (hard Lefschetz).** Let $M$ be a compact Kähler manifold of real dimension $2n$. Then for every $k \leq n$ the map

$$
L^{n-k} : H^k(M;\mathbb{R}) \longrightarrow H^{2n-k}(M;\mathbb{R})
$$

is an isomorphism. Consequently the Betti numbers satisfy $b_k = b_{2n-k}$, and the Poincaré duality of $M$ is compatible with the Lefschetz decomposition.

**Proof sketch.** The $\mathfrak{sl}_2$-representation theory of the previous theorem decomposes $H^\bullet$ into finite-dimensional irreducible summands, and the operator $L^{n-k}$ acts invertibly on the summands contributing to degree $k$: on a highest-weight module the powers of the raising operator are isomorphisms in the range where the degree does not exceed the middle dimension. $\square$

**Remark.** The Lefschetz decomposition and the hard Lefschetz theorem are the algebraic shadow of the Kähler class: the class $[\Omega]$ endows the cohomology ring with the structure of a Lefschetz module. Together with the Hodge–Riemann bilinear relations they constitute the **Hodge–Riemann package**, which is the input to the Hodge index theorem and to the theory of polarised Hodge structures. For a complex projective manifold the package holds as well, and the converse question — which integral $(p,p)$-classes are algebraic — is the Hodge conjecture, which lies outside this corpus.

## Ricci Curvature and the Kähler–Einstein Condition

**Definition.** Let $(M,J,g)$ be a Kähler manifold. The **Ricci form** is

$$
\rho(X,Y) = \mathrm{Ric}(JX,Y),
$$

where $\mathrm{Ric}$ is the Ricci tensor of $g$, from *Riemannian Geometry*. It is a real $(1,1)$-form, closed, and its cohomology class is the first Chern class: $[\rho] = 2\pi c_1(M)$.

**Proposition.** In local holomorphic coordinates the Ricci form is

$$
\rho = -i\,\partial\bar\partial\log\det(g_{i\bar j}),
$$

so it is closed and of type $(1,1)$.

**Proof.** The Ricci tensor of a Kähler metric has the local expression $R_{i\bar j} = -\partial_i\partial_{\bar j}\log\det(g_{k\bar l})$, which is the statement that the Ricci form is minus the $\partial\bar\partial$-logarithm of the volume density of the metric; $\rho$ of type $(1,1)$, and $\partial\bar\partial$ of a function is closed. $\square$

**Definition.** A Kähler metric is **Kähler–Einstein** if

$$
\rho = \lambda\,\Omega
$$

for a constant $\lambda$, in which case the scalar curvature is constant. A Kähler manifold whose Ricci form vanishes, $\rho = 0$, is **Calabi–Yau**.

**Theorem (Yau, on the Calabi conjecture).** Let $M$ be a compact Kähler manifold with $c_1(M) = 0$ in $H^2(M;\mathbb{R})$. Then for every Kähler class there is a unique Ricci-flat Kähler metric in that class.

**Proof sketch.** In a fixed Kähler class, the Kähler metrics are parametrised by their potentials: $g' = g + i\partial\bar\partial\varphi$. The Ricci forms change by $-i\,\partial\bar\partial\log(\det(g'_{i\bar j})/\det(g_{i\bar j}))$, so the condition $\rho'=0$ becomes the complex Monge–Ampère equation

$$
\det\Bigl(g_{i\bar j} + \partial_i\partial_{\bar j}\varphi\Bigr) = e^{F}\,\det(g_{i\bar j}),
$$

for a function $F$ determined by the difference of the Ricci forms. Yau's theorem is the solution of this equation by the continuity method: the a priori estimates $C^0$, $C^1$, $C^2$ and $C^{2,\alpha}$ for the solution give openness and closedness of the set of solvable classes. $\square$

**Theorem (Aubin–Yau).** Let $M$ be a compact Kähler manifold with $c_1(M) < 0$, that is, with $c_1$ represented by a negative $(1,1)$-form. Then $M$ admits a unique Kähler–Einstein metric with $\lambda<0$, normalised by the Kähler class.

**Proof sketch.** The same Monge–Ampère equation with the sign of the right-hand side reversed; the a priori estimates are those of Aubin and Yau. $\square$

**Theorem.** A Fano manifold — a compact Kähler manifold with $c_1(M) > 0$, equivalently with $-K_M$ positive — admits a Kähler metric with positive Ricci form, and the existence of a Kähler–Einstein metric with $\lambda>0$ is obstructed by the vanishing of the Futaki invariant; beyond that, it is equivalent to the $K$-stability of the manifold.

**Proof sketch.** The positive case is the hardest, because the Monge–Ampère equation is not coercive; the necessary conditions are given by the automorphism group and by the Futaki invariant, and the sufficiency is the content of the Chen–Donaldson–Sun theorem, whose statement is the equivalence of the existence of the Kähler–Einstein metric with the $K$-stability of the polarised manifold. $\square$

**Remark.** The Kähler–Einstein condition is the meeting point of the complex structure, the metric and the canonical bundle. Since $[\rho] = 2\pi c_1(M) = -2\pi c_1(K_M)$, where $K_M = \Lambda^n(T^{1,0}M)^*$ is the canonical bundle, the trichotomy $c_1 < 0$, $c_1 = 0$, $c_1 > 0$ is the trichotomy of the curvature of the canonical bundle, and it organises the classification of compact complex manifolds by their Kodaira dimension. The case $c_1(M)=0$ is the subject, where the Ricci-flat metrics produced by Yau's theorem and their holonomy are developed; the Fano case belongs to the algebraic-geometric theory of the anticanonical embedding, and the negative case to the theory of the canonical model.

**Remark (Kodaira embedding).** A compact complex manifold is **projective**, that is, embeds in some $\mathbb{CP}^N$, if and only if it carries a Kähler form whose cohomology class lies in $H^2(M;\mathbb{Z})$ — such a manifold is called a **Hodge manifold**. The theorem of Kodaira is the bridge between the differential geometry of this article and algebraic geometry: the integrality of the Kähler class is the hypothesis that makes the Kähler metric the curvature of a positive line bundle, and the embedding is produced by the holomorphic sections of its powers. The pointwise positivity of the curvature and the vanishing of the higher cohomology of a sufficiently positive line bundle are the analytic input, and the vanishing theorem belongs to the same analytic circle, with the details deferred to Part III.

## Summary

A Kähler manifold is a Hermitian manifold whose fundamental form $\Omega(X,Y)=g(JX,Y)$ is closed. The condition is equivalent to the parallelism of $J$ for the Levi-Civita connection, to the coincidence of the Chern connection with the Levi-Civita connection, to the local existence of a Kähler potential with $\Omega = i\partial\bar\partial\varphi$, and to the reduction of the holonomy group to $U(n)$; a Kähler manifold is in particular symplectic, and the inclusion of the Kähler manifolds in the symplectic ones is strict, the Kodaira–Thurston manifold being symplectic and not Kähler.

The examples are $\mathbb{C}^n$ and its quotients by lattices, the complex projective space with the Fubini–Study form $\Omega_{FS} = i\partial\bar\partial\log(1+|z|^2)$ and $\int_{\mathbb{CP}^1}\Omega_{FS} = 2\pi$, the Hermitian symmetric spaces, the complex submanifolds and products, and the Riemann surfaces, where the condition is vacuous. Kähler normal coordinates make the metric flat to first order, so the curvature is the only local invariant.

On a compact Kähler manifold the Kähler identities give $\Delta_d = 2\Delta_\partial = 2\Delta_{\bar\partial}$, and the Hodge decomposition $H^k(M;\mathbb{C}) = \bigoplus_{p+q=k}H^{p,q}$ with $H^{p,q}=\overline{H^{q,p}}$, so the odd Betti numbers are even and $b_{2k}\geq1$; the analytic proofs are deferred to Part III. The Lefschetz operators $L$, $\Lambda$, $H$ form an $\mathfrak{sl}_2$-representation on cohomology, giving the Lefschetz decomposition into primitive classes and the hard Lefschetz isomorphism $L^{n-k}:H^k\to H^{2n-k}$.

Finally, the Ricci form $\rho(X,Y)=\mathrm{Ric}(JX,Y)$ is a closed real $(1,1)$-form with $[\rho]=2\pi c_1(M)$, locally $\rho = -i\partial\bar\partial\log\det(g_{i\bar j})$. Kähler–Einstein metrics satisfy $\rho=\lambda\Omega$; Yau's theorem gives a unique Ricci-flat Kähler metric in each Kähler class when $c_1(M)=0$, the Aubin–Yau theorem gives the negative case, and the positive case is governed by $K$-stability. The Ricci-flat case is the doorway.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M$ | Complex manifold of complex dimension $n$, real dimension $2n$ |
| $J$ | Complex structure; $\nabla J = 0$ on a Kähler manifold |
| $g$, $g_{i\bar j}$ | Kähler metric and its coefficients in holomorphic coordinates |
| $\nabla$ | Levi-Civita connection (from *Riemannian Geometry*); equals the Chern connection here |
| $\Omega(X,Y) = g(JX,Y)$ | Kähler form; closed, nondegenerate, of type $(1,1)$ |
| $d\Omega=0$ | The Kähler condition |
| $\varphi$, $\Omega = i\partial\bar\partial\varphi$ | Kähler potential; unique up to $\varphi\mapsto\varphi+f+\bar f$ |
| $\Omega_0 = \sum_i dx_i\wedge dy_i$ | Euclidean Kähler form on $\mathbb{C}^n$ |
| $\Omega_{FS} = i\partial\bar\partial\log(1+|z|^2)$ | Fubini–Study form; $\int_{\mathbb{CP}^1}\Omega_{FS}=2\pi$, $h^{p,p}(\mathbb{CP}^n)=1$ |
| $g_{i\bar j}=\delta_{ij}+O(|z|^2)$ | Kähler normal coordinates |
| $H^{p,q}(M)$, $h^{p,q}$ | Hodge decomposition and Hodge numbers of a compact Kähler manifold |
| $L\alpha=\Omega\wedge\alpha$, $\Lambda=L^*$, $H$ | Lefschetz operators, $H\alpha=(k-n)\alpha$ on $k$-forms; $[L,\Lambda]=H$, $\mathfrak{sl}_2$-relations |
| $P^\bullet=\ker\Lambda$ | Primitive classes; Lefschetz decomposition |
| $L^{n-k}:H^k\to H^{2n-k}$ | Hard Lefschetz isomorphism |
| $\rho(X,Y)=\mathrm{Ric}(JX,Y)$ | Ricci form; $\rho=-i\partial\bar\partial\log\det(g_{i\bar j})$, $[\rho]=2\pi c_1(M)$ |
| Kähler–Einstein | $\rho = \lambda\Omega$; $\lambda=0$ is Calabi–Yau |
| $K_M = \Lambda^n(T^{1,0}M)^*$ | Canonical bundle; $c_1(M) = -c_1(K_M)$ |



## Further Reading

- Phillip Griffiths and Joseph Harris, *Principles of Algebraic Geometry* (Wiley, 1978), for Kähler metrics, the Hodge decomposition, the Lefschetz theorems and the Hodge–Riemann relations.
- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry, Volume II* (Interscience, 1969), for the equivalence of the Kähler conditions, the Kähler potential and the Chern connection.
- Jean-Pierre Demailly, *Complex Analytic and Differential Geometry* (Open Access, 2012), for the Kähler identities, the Hodge theory and the Monge–Ampère equation.
- Kunihiko Kodaira, *Complex Manifolds and Deformation of Complex Structures* (Springer, 1986), for the Hodge theory of compact complex manifolds and the embedding theorem.
- Shing-Tung Yau, "On the Ricci Curvature of a Compact Kähler Manifold and the Complex Monge–Ampère Equation, I", *Communications on Pure and Applied Mathematics* 31 (1978), 339–411, for the solution of the Calabi conjecture.
- Thierry Aubin, "Équations du type Monge–Ampère sur les variétés kählériennes compactes", *Bulletin de la Société Mathématique de France* 102 (1978), 63–95, for the negative Einstein case.
- Xiuxiong Chen, Simon Donaldson and Song Sun, "Kähler–Einstein Metrics on Fano Manifolds, I–III", *Journal of the American Mathematical Society* 28 (2015), 183–278, for the equivalence of the Kähler–Einstein condition with $K$-stability.
- Alan Weinstein, "Symplectic Manifolds and Their Lagrangian Submanifolds", *Advances in Mathematics* 6 (1971), 329–346, for the comparison of the symplectic and Kähler structures and the Kodaira–Thurston example.
