
# __Symplectic and Contact Topology__

## Introduction

The local theory of symplectic and contact manifolds is rigid to the point of being unique: the Darboux theorem says that every symplectic manifold looks locally like $\mathbb{R}^{2n}$ with its standard form, and the contact Darboux theorem says the same for a contact manifold, so there are no local invariants at all. Everything of interest is therefore **global**, and the subject of this article is the interplay between the differential-geometric existence question — which manifolds carry such a structure — and the topological obstructions to it.

The global theory is governed by a dichotomy between **flexibility** and **rigidity**. In the open case, existence is a matter of homotopy theory: an open manifold carries a symplectic form exactly when it carries a nondegenerate $2$-form, and the same for contact structures, by the $h$-principle of Gromov. In the closed case the $h$-principle fails, and the failure is measured by topological invariants: the cohomology class $[\omega]$ must satisfy $[\omega]^{\wedge n}\neq0$, a symplectic four-manifold is constrained by its Seiberg–Witten invariants, and a contact structure on a three-manifold is either **tight** or **overtwisted**, a dichotomy that is invisible to homotopy theory. Overtwisted contact structures, in every dimension, obey the $h$-principle; tight ones do not, and their classification is the hard part of the subject.

This article states the foundational global theorems — Moser's stability theorem, Gromov's $h$-principle for open manifolds, Gray's theorem, the Lutz–Martinet existence theorem for contact structures on three-manifolds, and Eliashberg's classification of overtwisted structures — and the topological constraints that make the closed case rigid. It treats the symplectic topology of four-manifolds, where the invariants of Seiberg–Witten and Gromov–Witten theory give the sharpest results; the toric picture, where a symplectic manifold with a torus action is encoded in a polytope; and the theory of fillings, in which contact structures appear as boundaries of symplectic manifolds. The invariants defined by counting holomorphic curves — the Gromov–Witten and Floer theories — are treated, and are used here only as statements.

**The boundaries of the article.** The symplectic form, its linear algebra, the Darboux theorem, Hamiltonian vector fields, Lagrangian submanifolds, compatible almost complex structures and symplectic reduction are those of *Symplectic Geometry*; the contact form, the Reeb field, Legendrian submanifolds and symplectisation are those of *Contact Geometry*; the Poisson tensor and its leaves are those of *Poisson Geometry*, and these three articles are the immediately preceding ones of this half. The linear-algebraic theory of alternating forms — the canonical form, the Pfaffian, the symplectic group — is that of *Symplectic Forms and Poisson Brackets*, and is not restated. Smooth manifolds, transversality, handlebodies and the topological machinery of four-manifolds are those of *Smooth Manifolds and Differential Geometry*, *Differential Topology* . The homology and cohomology used are those of *Algebraic Topology*, being written by another agent, and the Seiberg–Witten and instanton invariants are analytic objects whose construction belongs to Part III, where the measure and the limit are available; the results are stated here and cited. Lie groups and torus actions are those of *Lie Groups* and its companions. The base field is $\mathbb{R}$ and no physics is invoked.

## Moser's Stability Theorem and the Space of Structures

**Theorem (Moser, symplectic case).** Let $M$ be a closed manifold and let $\omega_t$, $t\in[0,1]$, be a smooth path of symplectic forms on $M$ with $[\omega_t]$ constant in $H^2(M;\mathbb{R})$. Then there is a smooth isotopy $\phi_t$ of $M$ with $\phi_0 = \mathrm{id}$ and $\phi_t^*\omega_t = \omega_0$.

**Proof sketch.** Write $\sigma_t = \frac{d}{dt}\omega_t$ for the derivative, which is a closed $2$-form because each $\omega_t$ is closed; the hypothesis on the cohomology class makes $\sigma_t$ exact, $\sigma_t = d\alpha_t$ for a $1$-form $\alpha_t$ depending smoothly on $t$. The Moser equation $\iota_{X_t}\omega_t = -\alpha_t$ defines a time-dependent vector field $X_t$ uniquely, because $\omega_t$ is nondegenerate, and the isotopy of $X_t$ has $\frac{d}{dt}\phi_t^*\omega_t = \phi_t^*(d\iota_{X_t}\omega_t + \iota_{X_t}d\omega_t + \sigma_t) = 0$, so $\phi_t^*\omega_t = \phi_0^*\omega_0 = \omega_0$. $\square$

**Corollary.** On a closed manifold the symplectic forms in a fixed cohomology class form a connected space modulo diffeomorphism: any two such forms are related by an isotopy of the manifold. Consequently the symplectic structures on a closed manifold are classified, to first order, by their cohomology classes, and the differential-topological invariants of a symplectic manifold are invariants of the pair $(M,[\omega])$.

**Theorem (Moser, contact case; Gray's theorem).** Let $\alpha_t$, $t\in[0,1]$, be a smooth path of contact forms on a closed manifold. Then there is a diffeomorphism $\phi$ and a positive function $f$ with $\phi^*\alpha_1 = f\alpha_0$; that is, the contact structures $\ker\alpha_t$ are all isotopic.

**Proof sketch.** The argument is the Moser argument as above with the contact forms in place of the symplectic ones: with $\sigma_t = \dot\alpha_t$ one solves $L_{X_t}\alpha_t = \rho_t\alpha_t - \sigma_t$ for a time-dependent vector field $X_t$ and a function $\rho_t$. The equation splits: the equation $\iota_{X_t}\alpha_t = -f_t$ determines the component of $X_t$ along the Reeb field, and the equation $\iota_{X_t}d\alpha_t = -\sigma_t + \rho_t\alpha_t - df_t$, restricted to the contact planes, determines the component in $\xi$, because $d\alpha_t$ is nondegenerate there; the free function $\rho_t$ is then fixed by the component along the Reeb field. The point is that the contact condition is open and the linear equation is solvable at each stage. $\square$

**Remark.** Gray's theorem is the statement that a contact structure on a closed odd-dimensional manifold has no continuous invariants of a one-parameter family: the homotopy classes of contact structures are discrete. The theorem is the reason contact topology is a discrete subject and the reason the tight–overtwisted dichotomy is the central invariant, whereas the symplectic case, by contrast, has the continuous invariants of the cohomology class. In this sense the contact theory is the more rigid of the two.

## The $h$-Principle and Its Failure

**Definition.** A **symplectic form** on a manifold $M$ of dimension $2n$ is a closed nondegenerate $2$-form $\omega$. An **almost symplectic form** is a nondegenerate $2$-form, with no closedness condition; a manifold carrying one is **almost symplectic**. Thus an almost symplectic structure is a reduction of the structure group of $TM$ from $GL(2n,\mathbb{R})$ to $Sp(2n,\mathbb{R})$, equivalently, since $Sp(2n,\mathbb{R})$ deformation retracts to $U(n)$, an almost complex structure together with a Hermitian metric.

**Theorem (Gromov's $h$-principle for open manifolds).** Let $M$ be an open manifold of dimension $2n$ with an almost symplectic form $\omega_0$. Then there is a path of nondegenerate $2$-forms from $\omega_0$ to a symplectic form, and more precisely the space of symplectic forms on $M$ is homotopy equivalent to the space of almost symplectic forms. In particular an open almost symplectic manifold is symplectic.

**Proof sketch.** The proof is the $h$-principle for open $Diff$-invariant differential relations: the relation "$\omega$ is nondegenerate" is open and $Diff$-invariant, and Gromov's convex integration technique solves it after the closedness condition is imposed by induction on a handle decomposition of the open manifold, the closedness being arranged skeleton by skeleton. The relevant homotopy statement is that the inclusion of symplectic forms into almost symplectic forms is a weak homotopy equivalence for an open manifold. $\square$

**Theorem (failure of the $h$-principle on closed manifolds).** The $h$-principle fails for closed manifolds: there are closed almost symplectic manifolds carrying no symplectic structure. For instance $S^1\times S^3$ is parallelisable, hence almost symplectic, and has $H^2(S^1\times S^3;\mathbb{R}) = 0$, so it admits no symplectic form.

**Proof.** A symplectic form on a closed manifold is closed, so it defines a nonzero class in $H^2$: indeed $[\omega]^{\wedge n}$ pairs with the fundamental class to give $\int_M\omega^n/n! > 0$, so $[\omega]\neq0$. On $S^1\times S^3$ the second cohomology vanishes by the Künneth formula, while the triviality of the tangent bundle gives a nondegenerate $2$-form. $\square$

**Remark.** The obstruction used above is the cohomological one, $[\omega]\neq0$ and $[\omega]^{\wedge n}\neq0$, and it is only the first of a hierarchy. In dimension four the deeper obstructions come from gauge theory: a closed symplectic four-manifold has $b_2^+ \geq 1$ and its Seiberg–Witten invariants are severely constrained, and there are simply connected almost symplectic four-manifolds — for instance certain connected sums — that violate these constraints and hence admit no symplectic structure. The general principle is that the $h$-principle for a closed manifold holds exactly when there is no topology left for the closedness condition to detect, and in dimensions two and four there is a great deal.

**Definition.** A **contact structure** on a manifold $M$ of dimension $2n+1$ is a maximally nonintegrable hyperplane field $\xi = \ker\alpha$, where $\alpha$ is a contact form: $\alpha\wedge(d\alpha)^{\wedge n}$ is nowhere zero. A formal contact structure is the homotopy-theoretic datum of a hyperplane field with a nondegenerate skew form on it, with no integrability condition.

**Theorem (Gromov; the $h$-principle for open contact manifolds).** On an open manifold of dimension $2n+1$, the inclusion of contact structures into formal contact structures is a weak homotopy equivalence: every formal contact structure is homotopic to a genuine contact structure.

**Theorem (Eliashberg; the $h$-principle for overtwisted contact structures).** On a closed oriented three-manifold, the overtwisted contact structures are exactly the contact structures that satisfy the $h$-principle: two overtwisted contact structures are isotopic if and only if they are homotopic as formal contact structures, and every formal contact structure is homotopic to an overtwisted one. Consequently the classification of overtwisted contact structures on a closed oriented three-manifold is a problem of algebraic topology, and it was solved by Eliashberg in 1989.

**Proof sketch.** The overtwisted disc is a fixed local model of a contact structure on a neighbourhood of a disc, and the theorem states that the presence of one overtwisted disc leaves enough room for the standard $h$-principle techniques — the removal of singularities and the induction on a handle decomposition — to run. The direction that requires care is the isotopy extension from a neighbourhood of the disc; the argument is a relative version of Gromov's convex integration for contact structures. $\square$

**Theorem (Borman–Eliashberg–Murphy; overtwisted in higher dimensions).** The overtwisted contact structures on a closed manifold of dimension $2n+1 \geq 5$ satisfy the $h$-principle: the classification of overtwisted contact structures is the classification of formal contact structures, and every formal contact structure on a closed manifold of dimension at least five is homotopic to an overtwisted one.

**Proof sketch.** The higher-dimensional overtwisted disc is a model plastic contact structure on a neighbourhood of a $(2n)$-disc, and the flexibility that the model provides makes the $h$-principle techniques available in the same way as in dimension three; the argument differs from the three-dimensional case in the topology of the disc and the use of the $h$-principle for open contact manifolds away from the disc. $\square$

**Remark.** The contrast between the symplectic and the contact cases is instructive. For symplectic structures the flexibility holds in the open case and fails in the closed case, with no intermediate notion corresponding to overtwistedness: the closed case is rigid throughout, and the invariants are those of gauge theory and of holomorphic curves. For contact structures the flexibility holds in the open case, fails for tight structures in the closed case, and holds again for overtwisted ones in the closed case; the dichotomy between tight and overtwisted is exactly the dichotomy between rigidity and flexibility, and it is the source of the difficulty and the richness of contact topology in dimension three.

## Existence Theorems for Contact Structures

**Theorem (Lutz–Martinet).** Every closed oriented three-manifold carries a contact structure; moreover, every homotopy class of oriented $2$-plane fields on a closed oriented three-manifold contains a contact structure that is homotopic to it.

**Proof sketch.** The construction proceeds by a surgery description: a contact structure is built on a handlebody by taking the standard contact structure on the three-ball and gluing along the boundary spheres with a controlled twisting, using the Lutz twist to adjust the homotopy class of the resulting plane field. Surgery along the components of a link presenting the manifold, and the modification of the contact structure at each surgery, produce a global contact structure of the required homotopy type. $\square$

**Theorem (Boothby–Wang).** Let $V$ be a $(2n)$-dimensional symplectic manifold with an integral symplectic form $[\omega]\in H^2(V;\mathbb{Z})$ and let $\pi : M\to V$ be the circle bundle with Euler class $[\omega]$. Then $M$ carries a contact form $\alpha$ with $d\alpha = \pi^*\omega$, and the Reeb vector field of $\alpha$ generates the circle action. Such a contact manifold is **regular**, and its quotient is the symplectic manifold $V$.

**Proof sketch.** Choose a connection $1$-form $\alpha$ on the circle bundle with curvature $d\alpha = \pi^*\omega$; the form is contact because $\alpha\wedge(d\alpha)^{\wedge n} = \alpha\wedge(\pi^*\omega)^{\wedge n}$ is a volume form, the restriction of $\omega^n$ to the horizontal distribution being nonzero and $\alpha$ being transverse. $\square$

**Example.** The Hopf fibration $S^3\to S^2$ with the area form on $S^2$ gives the standard contact structure on $S^3$, and more generally the circle bundle of a prequantisable Kähler manifold gives a regular contact manifold. The Boothby–Wang construction is the source of the standard contact structures on the Brieskorn manifolds, and it is the reason the contact theory of *Contact Geometry* is the odd-dimensional companion of the symplectic theory.

## Symplectic Toric Manifolds

**Definition.** A **symplectic toric manifold** is a compact connected symplectic manifold $(M^{2n},\omega)$ with an effective action of the torus $T^n = (S^1)^n$ preserving $\omega$ and admitting a moment map $\mu : M\to \mathfrak{t}^* = (\mathbb{R}^n)^*$. The image $\Delta = \mu(M)$ is the **moment polytope**.

**Definition.** A **Delzant polytope** in $(\mathbb{R}^n)^*$ is a simple rational polytope with a primitive outward normal vector at each facet such that the normal vectors of the facets meeting at each vertex form a basis of the lattice $\mathbb{Z}^n$.

**Theorem (Delzant).** The assignment $M\mapsto \Delta = \mu(M)$ is a bijection between symplectic toric manifolds of dimension $2n$ up to equivariant symplectomorphism and Delzant polytopes in $(\mathbb{R}^n)^*$ up to translation. The manifold is recovered as the quotient of $\mathbb{C}^d$ by the kernel of a linear torus action determined by the facet normals, where $d$ is the number of facets.

**Proof sketch.** The moment map is a Lagrangian fibration over the polytope, with the fibres the orbits of the torus; the local normal form over the interior of a face is the standard $T^k\times\mathbb{C}^{n-k}$ model, and the Delzant condition is exactly the condition for gluing these local models by symplectomorphisms. Conversely, a Delzant polytope determines a fan and a smooth toric variety with a Kähler form, and the construction of the quotient gives a compact symplectic manifold with moment polytope $\Delta$. $\square$

**Example.** The projective space $\mathbb{CP}^n$ with the Fubini–Study form, in the sense of *Kähler Geometry*, is toric with moment polytope the standard simplex

$$
\Delta = \{(x_1,\ldots,x_n)\in(\mathbb{R}^n)^* : x_i\geq0,\ x_1+\cdots+x_n\leq1 \},
$$

which has $n+1$ facets; the projective space is the quotient of $\mathbb{C}^{n+1}$ by the kernel of the diagonal action of $T^1$ scaled by the facet normals.

**Remark.** Delzant's theorem is the sharpest classification statement in symplectic topology: the symplectic geometry of a toric manifold is combinatorics. It has no analogue in the general case, where the classification of symplectic four-manifolds remains open, and it therefore marks the boundary between the tractable and the intractable parts of the subject.

## Symplectic Four-Manifolds

In dimension four the gauge-theoretic invariants enter, and the constraints they impose make the symplectic topology of four-manifolds a genuinely rigid subject.

**Theorem (Taubes; constraints on symplectic four-manifolds).** Let $M$ be a closed symplectic four-manifold. Then $b_2^+(M)\geq1$, and the Seiberg–Witten invariants of $M$ are nontrivial: the class of the canonical bundle of a compatible almost complex structure is a basic class, with Seiberg–Witten invariant $\pm1$ in the chamber determined by the symplectic form; when $b_2^+(M)>1$ there is no chamber dependence and $M$ is minimal in the sense of the classification of complex surfaces under the natural extension of the Kodaira classification. In particular $M$ does not split as a connected sum $M_1\# M_2$ with both $b_2^+\geq1$.

**Proof sketch.** The Seiberg–Witten equations of Part III depend on a metric and a perturbing form; Taubes takes the perturbation to be a large multiple of the symplectic form $\omega$, and the limiting behaviour of the solutions is governed by the pseudoholomorphic curves of the compatible almost complex structure. The invariants are computed in terms of the symplectic form, and their nonvanishing gives the stated constraint. The analysis is that of the Seiberg–Witten moduli space. $\square$

**Theorem (Gompf; the fundamental group).** Every finitely presented group occurs as the fundamental group of a closed symplectic four-manifold.

**Proof sketch.** The construction is a symplectic generalisation of the standard handlebody realisation of a presentation: symplectic $1$-handles and $2$-handles are glued to a symplectic base along Legendrian and contact boundary pieces, and the effect of each handle on the fundamental group is exactly that of the topological handle. The resulting manifold is symplectic by a gluing theorem for symplectic structures across contact-type boundaries. $\square$

**Theorem (Gompf; symplectic sums).** Let $M_1, M_2$ be closed symplectic four-manifolds containing symplectic surfaces $\Sigma_1, \Sigma_2$ of the same genus and opposite self-intersection number; then the symplectic sum $M_1\#_\Sigma M_2$ is symplectic. The construction produces symplectic manifolds with prescribed fundamental group, Euler characteristic and signature, and it is the source of most known non-Kähler symplectic four-manifolds.

**Proof sketch.** Remove tubular neighbourhoods of the surfaces and glue the resulting boundary three-manifolds, which are circle bundles over the surfaces with contact structures by Boothby–Wang; the gluing is carried out so that the symplectic forms agree along the boundary by the symplectic neighbourhood theorem. $\square$

**Remark.** The contrast with the Kähler case is sharp: a compact Kähler manifold has even first Betti number, as the Hodge decomposition of *Kähler Geometry* shows, so every finitely presented group with odd abelianisation arises only from a non-Kähler symplectic manifold. The Kodaira–Thurston manifold of *Kähler Geometry* is the first example, and Gompf's construction produces them in abundance.

## Tight and Overtwisted Contact Structures

**Definition.** Let $(M,\xi)$ be a contact three-manifold and let $\Sigma\subseteq M$ be an embedded disc with Legendrian boundary. Then $\Sigma$ is an **overtwisted disc** if the Thurston–Bennequin invariant of $\partial\Sigma$, computed with respect to the framing that the disc induces on the boundary, is zero. A contact structure is **overtwisted** if it contains an overtwisted disc, and **tight** otherwise.

**Theorem (Eliashberg).** The standard contact structure $\xi_{\mathrm{std}}$ on $S^3$ and on $\mathbb{R}^3$ is tight, and tightness is equivalent to the non-existence of an overtwisted disc. A contact structure that admits a symplectic filling is tight, and an overtwisted structure admits no filling.

**Proof sketch.** The standard structure on $\mathbb{R}^3$ is tight by the theorem of Eliashberg; a second proof uses the Bennequin inequality, which bounds the Thurston–Bennequin invariant of a Legendrian knot by the genus of a surface that it bounds, and which fails for the boundary of an overtwisted disc. The filling statement follows because a filling supplies the holomorphic curves and the corresponding adjunction inequalities that the overtwisted disc would violate. $\square$

**Remark.** The converse of the filling statement fails in general: there are tight contact structures on closed three-manifolds that admit no symplectic filling, so tightness is strictly weaker than fillability. The distinction is detected by the Floer-theoretic invariants, and it is one of the reasons the classification of tight contact structures is a hard and still incomplete problem.

**Theorem (Bennequin inequality).** Let $K\subseteq(\mathbb{R}^3,\xi_{\mathrm{std}})$ be a Legendrian knot with Thurston–Bennequin invariant $\mathrm{tb}(K)$ and rotation number $\mathrm{rot}(K)$, and let $g$ be the genus of a Seifert surface for $K$ placed in general position with respect to $\xi$. Then

$$
\mathrm{tb}(K) + |\mathrm{rot}(K)| \leq 2g - 1 .
$$

**Proof sketch.** The inequality is proved by putting the Seifert surface into a standard form with respect to the contact structure and computing the Thurston–Bennequin invariant of the boundary in terms of the Euler characteristic of the surface; the modern proofs derive it from the adjunction inequality for pseudoholomorphic curves in the symplectisation, or from the Heegaard Floer theory of the knot, and the analytic input is the same compactness theory that underlies. $\square$

**Example.** The standard contact structure on $S^3$ is tight; the standard Legendrian unknot in it has $\mathrm{tb} = -1$, $\mathrm{rot}=0$ and genus $0$, so the Bennequin inequality is an equality in this case. The overtwisted contact structures on $S^3$ are classified by a single integer, in agreement with the homotopy classification of formal contact structures, and they are the structures that the overtwisted $h$-principle controls.

**Remark.** The tight–overtwisted dichotomy is the central structural result of three-dimensional contact topology. It is a genuine invariant of the contact structure, invisible to the homotopy type of the plane field: a symplectically fillable contact structure is tight, and an overtwisted one is never fillable, while tightness is strictly weaker than fillability. The invariants that detect tightness — the contact homology and the Heegaard Floer groups — are the subject, being another article of this half.

## Fillings and the Symplectic Boundary Problem

**Definition.** A closed contact manifold $(M^{2n+1},\xi)$ is **symplectically fillable** if there is a compact symplectic manifold $(W,\omega)$ with $\partial W = M$ and $\omega|_\xi$ positive and nondegenerate, and the boundary is **convex** in the sense of admitting a Liouville vector field pointing outward. A **Stein filling** is a filling in which the symplectic form is exact with a plurisubharmonic primitive, and a **Weinstein filling** is a filling whose handle decomposition is compatible with the symplectic structure.

**Theorem (Gromov, Eliashberg).** Every symplectically fillable contact structure is tight. In dimension three, every contact structure that bounds a Stein filling is tight, and the overtwisted structures are exactly the contact structures that admit neither a Stein nor a Weinstein filling.

**Proof sketch.** A filling provides the holomorphic curves — the fibres of the filling fibration or the pseudoholomorphic discs with boundary on the binding — that the Bennequin-type inequalities require; the non-existence of an overtwisted disc follows. Conversely, the neighbourhood of an overtwisted disc is a symplectic cobordism that obstructs fillability. $\square$

**Remark.** The filling problem is the contact analogue of the existence problem for symplectic structures: given a contact boundary, does a symplectic manifold exist inside it? The answer is governed by the dichotomy aga, and in dimension three it can be decided by the Floer-theoretic invariants and by the Heegaard Floer theory. The higher-dimensional case is open in general; the flexible side is governed by the overtwisted $h$-principle of Borman–Eliashberg–Murphy, and the rigid side by the symplectic field theory introduced by Eliashberg–Givental–Hofer, whose invariants are built from the pseudoholomorphic curves of the symplectisation.

## Summary

The local theory of symplectic and contact manifolds is unique up to diffeomorphism, by the Darboux theorems; all invariants are global. Moser's theorem makes a compact symplectic structure a property of its cohomology class, and Gray's theorem makes a contact structure on a closed manifold a discrete object with no continuous invariants along isotopies. Gromov's $h$-principle gives the existence of symplectic and contact structures on open manifolds in terms of the formal homotopy data — an almost symplectic form or a formal contact structure — and it fails on closed manifolds, where the constraints begin with $[\omega]^{\wedge n}\neq0$ and, in dimension four, continue with the Seiberg–Witten invariants of Taubes.

Contact topology has a finer structure: contact structures on a closed manifold are either tight or overtwisted, the overtwisted ones satisfy the $h$-principle and are classified by algebraic topology (Eliashberg in dimension three, Borman–Eliashberg–Murphy in higher dimensions), and the tight ones are rigid and are the ones that can fill. Every closed oriented three-manifold carries contact structures, by Lutz–Martinet, and the regular ones are the circle bundles over integral symplectic manifolds, by Boothby–Wang.

In the presence of a torus action the symplectic structure reduces to a Delzant polytope, giving a complete classification of symplectic toric manifolds; without one, the four-dimensional theory is governed by Taubes' constraints, Gompf's symplectic sums and the realisation of arbitrary finitely presented fundamental groups, which together separate the symplectic four-manifolds sharply from the Kähler ones. The invariants behind these statements — the Gromov–Witten and Floer theories and their contact analogues — are constructed.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\omega$ | Symplectic form: closed, nondegenerate $2$-form (fixed for this category) |
| $\alpha$ | Contact form: $\alpha\wedge(d\alpha)^{\wedge n}\neq0$; $\xi=\ker\alpha$ |
| $\xi$ | Contact structure, a maximally nonintegrable hyperplane field |
| $[\omega]$ | Cohomology class; symplectic requires $[\omega]^{\wedge n}\neq0$ |
| Almost symplectic | Nondegenerate $2$-form without closedness; reduction to $Sp(2n,\mathbb{R})\sim U(n)$ |
| Formal contact structure | Homotopy-theoretic hyperplane field with a nondegenerate skew form; no integrability |
| Moser equation | $\iota_{X_t}\omega_t = -\alpha_t$ along a path with constant cohomology class |
| $h$-principle | Existence/classification of structures by their formal homotopy data |
| Overtwisted disc, tight | Local model of flexibility; a contact structure is overtwisted if it contains one, tight otherwise |
| $\mathrm{tb}(K)$, $\mathrm{rot}(K)$ | Thurston–Bennequin invariant and rotation number of a Legendrian knot |
| $T^n$, $\mu$, $\Delta=\mu(M)$ | Torus action, moment map and moment polytope of a symplectic toric manifold |
| Delzant polytope | Simple rational polytope with primitive facet normals forming a lattice basis at each vertex |
| $b_2^\pm$ | Dimensions of the positive and negative eigenspaces of the intersection form on $H^2$ of a four-manifold |
| Symplectic sum | $M_1\#_\Sigma M_2$ along symplectic surfaces of opposite self-intersection |
| Symplectic filling | $(W,\omega)$ with $\partial W=M$ and $\omega|_\xi$ positive; Stein and Weinstein variants |







## Further Reading

- Jürgen Moser, "On the Volume Elements on a Manifold", *Transactions of the American Mathematical Society* 120 (1965), 286–294, for the stability theorem in the symplectic and volume cases.
- Mikhail Gromov, *Partial Differential Relations* (Springer, 1986), for the $h$-principle for open manifolds and the convex integration method.
- Yakov Eliashberg, "Classification of Overtwisted Contact Structures on 3-Manifolds", *Inventiones Mathematicae* 98 (1989), 623–637, for the overtwisted classification in dimension three.
- Matthew Borman, Yakov Eliashberg and Emmy Murphy, "Existence and Classification of Overtwisted Contact Structures in All Dimensions", *Acta Mathematica* 215 (2015), 281–361, for higher-dimensional overtwistedness.
- Robert Lutz, "Structures de contact sur les fibrés principaux en cercles de dimension trois", *Annales de l'Institut Fourier* 27 (1977), 1–15, and Jean Martinet, "Formes de contact sur les variétés de dimension 3", *Springer Lecture Notes in Mathematics* 209 (1971), 142–163, for the existence of contact structures on three-manifolds.
- Thomas Delzant, "Hamiltoniens périodiques et images convexes de l'application moment", *Bulletin de la Société Mathématique de France* 116 (1988), 315–339, for the classification of symplectic toric manifolds by their moment polytopes.
- Clifford Taubes, "The Seiberg–Witten Invariants and Symplectic Forms", *Mathematical Research Letters* 1 (1994), 809–822, for the constraints on symplectic four-manifolds.
- Robert Gompf, "A New Construction of Symplectic Manifolds", *Annals of Mathematics* 142 (1995), 527–595, for the symplectic sum and the realisation of arbitrary fundamental groups.
- Yakov Eliashberg, Alexander Givental and Helmut Hofer, "Introduction to Symplectic Field Theory", *Geometric and Functional Analysis* 2000, Special Volume, 560–673, for the invariants of the symplectisation and the filling obstructions.
