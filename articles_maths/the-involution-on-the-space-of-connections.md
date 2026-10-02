
# __The Involution on the Space of Connections__

## Introduction

The connections on a principal or vector bundle over a manifold do not form a vector space but an affine space $\mathcal{A}$, modelled on the one-forms with values in the Lie algebra of the structure group, and the bundle automorphisms act on it: the **gauge group** $\mathcal{G}$ of the bundle acts by conjugation, the curvature transforms in the associated representation, and the orbit space $\mathcal{A}/\mathcal{G}$ is the **moduli space** of connections. A structure on the bundle — a real structure, or a conformal structure on the manifold through the Hodge star — induces an **involution** of the affine space, and the fixed connections are the ones compatible with the structure: the **real connections**, fixed by the conjugation, and the **self-dual and anti-self-dual connections**, fixed by the star up to sign. The involution descends to the moduli space, its fixed locus is the moduli of the compatible connections, and the study of that locus is the geometry of the moduli.

The article develops the affine space of connections and the curvature, the action of the gauge group and the moduli space, the involution induced by a real structure and the fixed set of real connections, the descent of the involution to the moduli space, and the self-duality involution of the star on the two-forms and the self-dual connections. The chosen structure — the real structure or the conformal metric that gives the star — is the form that the involution reads, and the whole construction is the geometry of that choice. The connections and their curvature are those of *Fibre Bundles, Connections and Curvature*; the real structures are *Real Structures on a Smooth Manifold*; the star and its eigenspaces are *The Hodge Star and the Real Structure of the Exterior Algebra* and *The Volume Element, Duality and the Hodge Star*; and the action of an involution on a pairing and on the cohomology is *Hermitian Pairings on a Topological Space* and *The Signature Operator and the Involution*.

The prerequisites are *Fibre Bundles, Connections and Curvature* for the bundles, the connections, the curvature and the gauge-theoretic reading; *Differential Forms and Stokes' Theorem* for the forms; *The Hodge Star and the Real Structure of the Exterior Algebra* and *Riemannian Geometry* for the star of a conformal metric; *Real Structures on a Smooth Manifold* and *Hermitian Structures and the Almost Complex Structure* for the real and complex structures; *Matrix Groups and Classical Groups* and the Lie group articles for the structure groups; and *Transformation Groups and the Erlangen Program* for the group actions on the infinite-dimensional space. The analytic topology of the moduli space — the slice theorem, the compactness and the bubbling — belongs to Part III and to the analysis of the elliptic equations, and is cited. The twisted Cauchy–Riemann operator of the gauge theory is *Clifford Modules and the Twisted Cauchy–Riemann Operator*. No physics is invoked.

## Connections and the Affine Space

**Definition.** Let $\pi:P\to M$ be a principal bundle with structure group $G$ and Lie algebra $\mathfrak{g}$, and let $\operatorname{ad}P=P\times_G\mathfrak{g}\to M$ be the adjoint bundle. A **connection** on $P$ is a $\mathfrak{g}$-valued one-form $A$ on $P$ that is equivariant and reproduces the generators of the action; equivalently, it is a horizontal distribution on $P$. The connections form the affine space

$$
\mathcal{A}=\bigl\{A:\ A=A_0+\eta,\ \eta\in\Omega^{1}(M;\operatorname{ad}P)\bigr\},
$$

modelled on the space of one-forms with values in the adjoint bundle, for any fixed reference connection $A_0$; the difference of two connections is a tensor, which is why $\mathcal{A}$ is an affine space and not a vector space, and the **curvature** of $A$ is the two-form

$$
F_A=dA+\tfrac12[A\wedge A]\in\Omega^{2}(M;\operatorname{ad}P),
$$

whose vanishing is the flatness of the connection. The connection, the curvature and the Bianchi identity are those of *Fibre Bundles, Connections and Curvature*.

**Definition.** For a vector bundle $E$ with structure group $G\subset GL(r)$ the same construction is written in a local trivialisation as a matrix of one-forms, $\nabla=d+A$, with the curvature $F=dA+A\wedge A$; the two descriptions agree through the associated bundle, and the adjoint bundle is the bundle of endomorphisms of $E$ of the appropriate type. The choice of the affine space $\mathcal{A}$ is the choice of the bundle, and it depends on the manifold and on the bundle but not on a metric.

## The Gauge Group and Its Action

**Definition.** The **gauge group** of a principal bundle $P$ is the group of automorphisms of $P$ covering the identity of $M$,

$$
\mathcal{G}=\operatorname{Aut}(P)\cong\Gamma(M,P\times_G G),
$$

the sections of the bundle associated to $P$ by the conjugation action of $G$ on itself; it is a group of bundle automorphisms, infinite-dimensional, and it is the symmetry group of the connection space.

**Theorem.** The gauge group acts on the connections by the pullback, and on the curvature by the adjoint representation,

$$
u\cdot A=u^{*}A,\qquad
F_{u\cdot A}=u^{-1}F_Au=\operatorname{Ad}(u^{-1})F_A ,
$$

so the action preserves the flatness and the equation $F_A=0$; the action is affine, $u\cdot(A_0+\eta)=u\cdot A_0+\operatorname{Ad}(u^{-1})\eta$ for the correct transformation of $\eta$, and the stabiliser of a connection in the gauge group is the group of parallel automorphisms. The action is free at the **irreducible** connections, those whose holonomy group is the whole structure group, and the orbit space of the irreducible connections is a manifold.

**Proof.** The transformation of the connection form under a bundle automorphism is the standard formula $u^{*}A=\operatorname{Ad}(u^{-1})A+u^{-1}du$, and the curvature is natural for the bundle map, whence the stated transformation; the stabiliser of a connection consists of the automorphisms that are parallel for it, and their group is trivial exactly at the connections with full holonomy, which gives the freeness at the irreducible points. The slice theorem that makes the quotient a manifold near an irreducible orbit belongs to the analysis of the elliptic operators and is quoted. $\square$

**Definition.** The **moduli space** of connections is the orbit space

$$
\mathcal{M}=\mathcal{A}/\mathcal{G},
$$

possibly restricted to the irreducible connections; the **Chern–Weil classes** of the bundle, evaluated on cycles of $M$, give the components and the invariants of the moduli space, and they are independent of the connection because the curvature transforms by conjugation and the invariant polynomials are invariant.

**Remark.** The moduli space is the quotient of an affine space by an infinite-dimensional group, and its geometry is the geometry of the orbits: the tangent space at a connection is the space $\Omega^{1}(M;\operatorname{ad}P)$ modulo the image of the infinitesimal gauge transformations, the **covariant derivative** $d_A:\Omega^{0}\to\Omega^{1}$; the zeros of its cokernel are the reducible connections, and the quotient is singular there. The whole is the infinite-dimensional analogue of a homogeneous space, and the involution below descends to the quotient and acts on the moduli space.

## The Involution on the Connections

**Definition.** A **real structure** on a complex vector bundle $E\to M$ is an antilinear bundle automorphism $\kappa:E\to E$ with $\kappa^{2}=\mathrm{id}$; the fixed points of $\kappa$ form the real subbundle $E_{\mathbb{R}}$, and a connection $\nabla$ on $E$ is **real** (or compatible with the real structure) when it commutes with $\kappa$,

$$
\kappa\nabla_Xs=\nabla_X\kappa s\qquad(X\in\mathrm{X}(M),\ s\in\Gamma(E)),
$$

equivalently when $\kappa$ preserves the space of sections of the real subbundle and the connection restricts to it.

**Theorem.** The real structure induces an involution of the affine space of connections,

$$
\tau:\mathcal{A}\to\mathcal{A},\qquad \tau(A)=\kappa A\kappa^{-1},
$$

an affine map whose linear part is the conjugation of the one-forms, and the fixed points of $\tau$ are the **real connections**. The curvature of a real connection is real, $F_{\tau(A)}=\kappa F_A\kappa^{-1}$, and the involution commutes with the gauge group action in the sense that $\tau(u\cdot A)=\kappa u\kappa^{-1}\cdot\tau(A)$; the real structures on the bundle form a torsor over the real gauge transformations, and the reality condition is an involution on the elements of the connection space.

**Proof.** The map $\tau$ is affine because $\kappa$ is linear and the difference of connections is conjugated linearly; a fixed point satisfies $\kappa A\kappa^{-1}=A$, which is the compatibility with $\kappa$; the curvature is natural for the bundle automorphism, and the reality of $F_A$ follows; the intertwining with the gauge action is the computation of the two sides on a section. $\square$

**Remark.** The fixed set $\mathcal{A}^{\tau}$ of real connections is an affine subspace of the connection space, and the curvature maps it to the real two-forms. The involution is the bundle-theoretic form of the conjugation of *Real Structures on a Smooth Manifold* and of the reality conditions of *Real Spinors and Reality Conditions with Inner Conjugation*; the reality condition on a connection is the compatibility with a real form of the structure group, and the real connections are the connections of the real reduction of the bundle.

## The Involution on the Moduli Space

**Theorem.** The involution $\tau$ of the connection space descends to the moduli space,

$$
\overline{\tau}:\mathcal{M}\to\mathcal{M},\qquad
\overline{\tau}([A])=[\tau(A)],
$$

and it is well defined because $\tau$ intertwines the gauge action; the fixed points of $\overline{\tau}$ are the gauge orbits that meet the fixed set of $\tau$, that is the gauge classes of real connections. The involution is an isometry of the natural metric on the moduli space when the real structure is compatible with the metric on the bundle, and the fixed locus is the moduli space of real connections, the quotient of $\mathcal{A}^{\tau}$ by the subgroup of the gauge group that commutes with $\kappa$.

**Proof.** The descent is the universal property of the quotient by the group action, the intertwining of the preceding theorem giving the well-definedness; a class is fixed exactly when the orbit is invariant, which is the condition that the orbit meets the fixed set of the affine involution, and the last statement is the restriction of the quotient to the fixed subspace. $\square$

**Corollary.** The moduli space carries an involution whose fixed locus is the moduli of real connections, and the pairing with the cohomology of the moduli space gives the **real** structure on the cohomology: the involution acts on $H^{*}(\mathcal{M})$ by an operator $\overline{\tau}^{*}$ whose fixed part is the real cohomology, and the orthogonal decomposition of the pairing under the involution is that of *Hermitian Pairings on a Topological Space*. In the finite-dimensional models — the moduli of flat connections on a surface, which is a finite-dimensional symplectic quotient — the involution is the real structure of the character variety, and its fixed locus is the real character variety.

## Self-Dual Connections

On a four-manifold the metric provides a second involution, that of the Hodge star on the two-forms, and the fixed connections are the instantons.

**Definition.** Let $M$ be an oriented Riemannian four-manifold. The Hodge star acts on the two-forms with square $\star^{2}=1$ and splits them by the chirality into the **self-dual** and **anti-self-dual** parts,

$$
\Omega^{2}=\Omega^{2}_{+}\oplus\Omega^{2}_{-},\qquad \star=+1\ \text{on}\ \Omega^{2}_{+},\ \star=-1\ \text{on}\ \Omega^{2}_{-},
$$

of dimensions three each; the splitting depends on the conformal class of the metric and not on the metric, because the star on the middle degree of a four-manifold is conformally invariant.

**Definition.** A connection $A$ on a bundle over $M$ is **self-dual** when its curvature is self-dual, $F_A\in\Omega^{2}_{+}(\operatorname{ad}P)$, and **anti-self-dual** when $F_A\in\Omega^{2}_{-}$; the equation

$$
F_A=\pm\star F_A
$$

is the **self-duality equation**, and the connections satisfying it are the **instantons** of the bundle.

**Theorem.** The self-duality equation is the equation that the curvature lie in an eigenspace of the involution $\star$ on the two-forms, and it is conformally invariant: it depends on the conformal class of the metric and not on the metric. The solutions are the critical points of the Yang–Mills functional $\int|F_A|^{2}$, and on a bundle whose curvature is square-integrable the self-dual and anti-self-dual connections minimise the functional in their topological class.

**Proof.** The star acts on the curvature component by component; the equation $F_A=\star F_A$ selects the self-dual part, and a conformal change of the metric changes the star on the middle degree by a positive factor on the two halves, so the equation is preserved; the variational statement is the first variation of the Yang–Mills functional, whose critical points satisfy the Yang–Mills equation, and the self-duality equation, being a first-order equation implying the second-order equation by the Bianchi identity, gives the minima. $\square$

**Remark.** The self-dual connections are the fixed points, up to the sign of the star, of the involution of the star on the curvatures, and the moduli of instantons is the quotient of the solution space by the gauge group; it is the fixed locus of the star involution on the moduli of all connections, refined by the topological charge. The theory of the instanton moduli — the elliptic analysis, the compactness and the invariants they define — belongs to the analysis of the elliptic equations and to *Clifford Modules and the Twisted Cauchy–Riemann Operator*; here the involution is the star, and the self-dual connections are its fixed curvatures.

## Summary

The connections on a bundle form an **affine space** $\mathcal{A}$ modelled on the one-forms with values in the adjoint bundle, with the curvature $F_A=dA+\tfrac12[A\wedge A]$, and the **gauge group** $\mathcal{G}=\operatorname{Aut}(P)$ acts on it by the pullback, $F_{u\cdot A}=\operatorname{Ad}(u^{-1})F_A$, freely at the irreducible connections; the orbit space is the **moduli space** $\mathcal{A}/\mathcal{G}$. A **real structure** $\kappa$ on the bundle induces an affine **involution** $\tau(A)=\kappa A\kappa^{-1}$ of the connection space whose fixed points are the **real connections**; the involution intertwines the gauge action and descends to the moduli space, where its fixed locus is the moduli of real connections, and its induced action on the cohomology of the moduli space gives the real structure on that cohomology, with the orthogonal decomposition of *Hermitian Pairings on a Topological Space*. On a four-manifold the Hodge star provides a second involution, splitting the two-forms into the self-dual and anti-self-dual parts of dimension three each; the connections with $F_A=\pm\star F_A$ are the **instantons**, the fixed curvatures of the star involution, the solutions of a conformally invariant first-order equation and the minima of the Yang–Mills functional in their topological class. The two involutions — the real structure and the star — are the two structures that the connection space reads, and the moduli of connections is the geometry of their fixed loci.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P\to M$, $G$, $\mathfrak{g}$, $\operatorname{ad}P$ | Principal bundle, structure group, Lie algebra, adjoint bundle |
| $\mathcal{A}=\{A_0+\eta:\eta\in\Omega^{1}(\operatorname{ad}P)\}$ | Affine space of connections |
| $F_A=dA+\tfrac12[A\wedge A]$ | Curvature |
| $\mathcal{G}=\operatorname{Aut}(P)$ | Gauge group |
| $u\cdot A$, $F_{u\cdot A}=\operatorname{Ad}(u^{-1})F_A$ | Gauge action on connections and curvature |
| $\mathcal{M}=\mathcal{A}/\mathcal{G}$ | Moduli space of connections |
| $\kappa$, $\kappa^{2}=\mathrm{id}$ | Real structure on the bundle |
| $\tau(A)=\kappa A\kappa^{-1}$ | Involution of the connection space; fixed points = real connections |
| $\Omega^{2}=\Omega^{2}_{+}\oplus\Omega^{2}_{-}$ | Self-dual and anti-self-dual two-forms, $\star=\pm1$ |
| $F_A=\pm\star F_A$ | Self-duality equation; instantons |

## Further Reading

- Michael F. Atiyah, *Geometry of Yang–Mills Fields* (Accademia Nazionale dei Lincei, 1979), for the space of connections, the gauge group, the moduli space and the self-duality equations.
- Simon K. Donaldson and Peter B. Kronheimer, *The Geometry of Four-Manifolds* (Oxford University Press, 1990), for the moduli of connections, the instantons and the invariants of four-manifolds.
- Michael F. Atiyah, Nigel J. Hitchin and Isadore M. Singer, "Self-duality in four-dimensional Riemannian geometry," *Proceedings of the Royal Society A* **362** (1978), 425–461, for the self-duality equations and their reduction.
- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry*, Vol. I (Wiley, 1963), for connections, curvature, the gauge transformations and the Chern–Weil theory.
- Simon K. Donaldson, "Anti self-dual Yang–Mills connections over complex algebraic surfaces and stable vector bundles," *Proceedings of the London Mathematical Society* **50** (1985), 1–26, for the moduli of instantons and the algebraic description.
- Clifford Henry Taubes, "Self-dual connections on 4-manifolds with indefinite intersection matrix," *Journal of Differential Geometry* **19** (1984), 517–560, for the existence theory of the self-dual connections.
- Robert C. Gunning, *On Uniformization of Complex Manifolds: The Role of Connections* (Princeton University Press, 1978), for connections, their moduli and the flat case.
