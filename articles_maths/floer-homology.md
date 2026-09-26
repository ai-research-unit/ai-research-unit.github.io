
# __Floer Homology__

## Introduction

Floer homology is the homology of an infinite-dimensional Morse complex, constructed from the critical points of a functional on a space of loops, paths or connections and from the solutions of an elliptic partial differential equation that plays the role of the gradient flow. The functional is defined on a space in which a distance is available — a loop space, a path space, a space of connections modulo gauge — so the construction belongs to Part II; the compactness, the Fredholm theory and the a priori estimates that make the construction work are analytic and belong to Part III, where the measure and the limit are available. What is established here is the algebraic and geometric skeleton: the complexes, the index computations that grade them, the invariance theorems, and the computations that produce consequences, such as the Arnold conjecture.

There are four principal theories, and they share a common template. **Hamiltonian Floer homology** counts the periodic orbits of a Hamiltonian flow on a symplectic manifold, with the differential counting cylinders that solve the Floer equation; it computes the singular homology of the manifold, and its existence proves the Arnold conjecture for nondegenerate Hamiltonian diffeomorphisms. **Lagrangian Floer homology** counts the intersection points of two Lagrangian submanifolds, with the differential counting pseudoholomorphic strips; it is the obstruction to displacing one Lagrangian from another, and it gives the Arnold conjecture for Lagrangians. **Instanton Floer homology** is the same construction applied to the Chern–Simons functional on the space of connections over a three-manifold, with gradient flow lines the anti-self-dual connections on a four-manifold with a cylindrical end; it is the three-dimensional companion of Donaldson's invariants. **Heegaard Floer homology** and **contact homology** are the versions adapted to three-manifolds and to contact structures, and they detect the tight–overtwisted dichotomy of *Symplectic and Contact Topology*.

This article states the construction of each theory, the index formula that grades the complexes, the compactness and gluing statements that give $\partial^2 = 0$ and the invariance, the isomorphism theorems that compute the homologies in the standard cases, and the applications that the invariants yield. The analytic content of the theory — the construction of the moduli spaces, the Fredholm theory, the transversality, the compactness and the gluing — is the analysis of Part III, and its citation is explicit throughout. The Khovanov homology that one obtains by the same template applied to a link diagram is the subject, and the topological applications to three- and four-manifolds are standard.

**The boundaries of the article.** The symplectic form, the Hamiltonian vector fields, the almost complex structures compatible with $\omega$ and the Lagrangian submanifolds are those of *Symplectic Geometry*; the contact form, the Reeb field and the symplectisation are those of *Contact Geometry*; the $h$-principle, the tight–overtwisted dichotomy and the Seiberg–Witten constraints are those of *Symplectic and Contact Topology*. The homology and cohomology of spaces and the algebra of chain complexes are those of *Algebraic Topology*, being written by another agent; the complexes are constructed here and their homological algebra is taken from there. Connections, covariant derivatives, curvature and the Chern–Simons form are those of *Fibre Bundles, Connections and Curvature*, and the characteristic classes those of *Characteristic Classes*, earlier in this Part. Smooth manifolds, transversality, moduli spaces and the compactness of the spaces of maps are those of *Smooth Manifolds and Differential Geometry* and *Differential Topology*, being written in parallel. The existence of the moduli spaces, the Sard–Smale transversality, the elliptic regularity, the compactness theorems of Gromov and Uhlenbeck and the gluing theorems require the measure, the limit and the theory of elliptic operators, and are the subject of Part III; the results are stated here and their proofs cited.

## The Floer Template

**Definition.** Let $X$ be a smooth infinite-dimensional space — a loop space, a path space or a space of connections modulo gauge — let $\mathcal{A} : X\to\mathbb{R}$ be a function, and let $\nabla_{\mathcal{A}}$ be a section of a Banach bundle over $X$ whose zero set is the critical set of $\mathcal{A}$. The **Floer complex** of $\mathcal{A}$ is the free module on the critical points of $\mathcal{A}$ that are of **Floer type**, graded by the **Fredholm index** of the linearised problem, with a differential that counts, with signs, the solutions of the gradient flow equation connecting critical points of index difference one:

$$
\partial x = \sum_{y}\#\mathcal{M}(x,y)\,y .
$$

The **Floer homology** $HF_*(\mathcal{A})$ is the homology of this complex.

**Theorem (the Floer package).** The Floer complex is well defined and its homology is an invariant of the underlying geometric data, provided:

**(a)** the moduli spaces $\mathcal{M}(x,y)$ of gradient flow lines connecting two critical points of index difference one are finite-dimensional smooth manifolds of dimension $\mathrm{ind}(x) - \mathrm{ind}(y) - 1$;

**(b)** the moduli spaces are compact up to the breaking of flow lines at intermediate critical points, so the differential counts a finite set and $\partial^2 = 0$;

**(c)** the homology is independent of the auxiliary choices — the almost complex structure, the perturbation, the metric on the auxiliary space — up to canonical isomorphism.

**Proof sketch.** Each of the three assertions is an analytic theorem about the elliptic equation defining the flow: (a) is the Fredholm theory of the linearised operator and the Sard–Smale transversality for generic auxiliary data; (b) is the compactness theorem for the relevant elliptic equation together with the gluing construction that identifies the ends of the moduli spaces and gives the identity $\partial\circ\partial = 0$; (c) is proved by a continuation argument in which the auxiliary data are deformed along a path and the resulting cobordism between moduli spaces gives a chain homotopy. The analytic content of (a), (b) and (c) is that of Part III. $\square$

**Remark.** The template is the one already used in finite-dimensional Morse theory, with the Morse–Smale condition, the compactness of the flow lines and the invariance of the Morse homology; the content of Floer's construction is that the same algebra works in infinite dimensions when the flow equation is elliptic, where the finite-dimensional compactness arguments fail and must be replaced by the hard compactness theorems for the corresponding partial differential equations. The grading, which is the dimension of the space of solutions, is the index of an elliptic operator and is computed by the Conley–Zehnder index in the Hamiltonian case and by the Maslov index in the Lagrangian case; in the instanton case it is the spectral flow of a family of self-adjoint operators.

## Hamiltonian Floer Homology and the Arnold Conjecture

**Definition.** Let $(M,\omega)$ be a closed symplectic manifold, let $H : S^1\times M\to\mathbb{R}$ be a periodic Hamiltonian with associated time-dependent vector field $X_H$ and flow $\phi^1_H$, and let $J$ be a compatible almost complex structure. The **Hamiltonian Floer complex** $CF_*(M,H)$ is the free module on the $1$-periodic orbits $x : S^1\to M$ of $X_H$ that are contractible and nondegenerate, graded by the **Conley–Zehnder index** $\mu(x)$. The **Floer equation** for a map $u : \mathbb{R}\times S^1\to M$ is

$$
\partial_s u + J(u)\bigl(\partial_t u - X_H(t,u)\bigr) = 0 ,
$$

and the differential $\partial$ counts, with signs, the solutions that converge at the two ends to prescribed periodic orbits, the count being finite for a generic choice of $J$ and of a time-dependent perturbation of $H$.

**Theorem (Floer).** The Hamiltonian Floer complex is well defined, $\partial^2=0$, and the homology is independent of $H$ and $J$ up to canonical isomorphism. When the symplectic form is aspherical or the manifold is monotone, there is a canonical isomorphism

$$
HF_*(M,H) \cong H_{*+\dim_{\mathbb{C}}M}(M;\mathbb{Z}) ,
$$

with $2\dim_{\mathbb{C}}M = \dim M$ and with the singular homology of $M$, the shift being the one fixed by the normalisation of the Conley–Zehnder index, and the isomorphism respecting the action filtration up to the finite indeterminacy of the Novikov ring. For a general closed symplectic manifold the Floer homology is defined over the Novikov ring, and the isomorphism holds with coefficients there.

**Proof sketch.** The construction is the Floer package applied to the action functional

$$
\mathcal{A}_H(x) = -\int_{D^2} \bar x^*\omega - \int_{S^1} H(t,x(t))\,dt
$$

on the space of contractible loops, whose $L^2$-gradient flow is the Floer equation. The index is the Conley–Zehnder index; the compactness is Gromov's compactness for pseudoholomorphic curves, with the bubbling phenomena controlled by the monotonicity or asphericity hypothesis; the isomorphism with the homology is the PSS (Piunikhin–Salamon–Schwarz) isomorphism, obtained by counting the solutions of a mixed equation interpolating between the closed and the open ends of the theory. $\square$

**Theorem (Arnold conjecture for Hamiltonian diffeomorphisms).** Let $(M,\omega)$ be a closed symplectic manifold, let $H$ be a periodic Hamiltonian whose time-one flow $\phi^1_H$ is nondegenerate, and let $\sum_i b_i(M)$ be the sum of the Betti numbers. Then

$$
\#\,\mathrm{Fix}(\phi^1_H) \geq \sum_{i=0}^{2n} b_i(M) .
$$

**Proof.** The fixed points of $\phi^1_H$ are the $1$-periodic orbits of $X_H$, hence the generators of the Floer complex. The rank of a chain complex is at least the rank of its homology; applied to the Floer complex, whose homology has total rank $\sum b_i(M)$ by the isomorphism $HF_*\cong H_{*+\dim_{\mathbb{C}}M}(M)$, this gives the inequality. $\square$

**Example.** For $M = \mathbb{CP}^n$ the Betti numbers are $b_{2k}=1$ and $b_{2k+1}=0$, so $\sum b_i = n+1$: every nondegenerate Hamiltonian diffeomorphism of $\mathbb{CP}^n$ has at least $n+1$ fixed points, and the standard linear Hamiltonian has exactly $n+1$. For $M=T^2$ the sum is $4$, matching the four critical points of the height function, and the theorem is sharp in both cases; the Floer-theoretic bound is stronger than the Lefschetz fixed-point bound in general.

**Remark (the Conley conjecture).** A refinement of the Arnold conjecture concerns the periodic points of all periods: the **Conley conjecture** asserts that a Hamiltonian diffeomorphism of a closed symplectic manifold has infinitely many periodic points. Franks proved the conjecture for $S^2$, and Ginzburg and Gürel proved it for the symplectically aspherical and for the negative monotone closed symplectic manifolds; it is known to fail for the complex projective spaces $\mathbb{CP}^n$ with $n\geq2$, so it does not extend to all closed symplectic manifolds. The proof uses the Floer homology of the iterates and the invariance of the action spectrum, and it is a further instance in which the Floer complex sees more than the fixed-point count.

## Lagrangian Floer Homology

**Definition.** Let $(M,\omega)$ be a closed or exact symplectic manifold, let $L_0, L_1\subseteq M$ be closed Lagrangian submanifolds intersecting transversely, and let $J$ be a compatible almost complex structure. The **Lagrangian Floer complex** $CF_*(L_0,L_1)$ is the free module on the intersection points $L_0\cap L_1$, graded by the **Maslov index** $\mu(p)$. The differential counts the pseudoholomorphic strips $u:\mathbb{R}\times[0,1]\to M$ with $u(\cdot,0)\in L_0$, $u(\cdot,1)\in L_1$ and $u(s,\cdot)\to p_\pm$ as $s\to\pm\infty$, which solve the Cauchy–Riemann equation

$$
\partial_s u + J(u)\partial_t u = 0
$$

with Lagrangian boundary conditions; the counts are finite for a generic $J$ and a generic Hamiltonian perturbation of one of the Lagrangians.

**Theorem (Floer).** For a pair of closed Lagrangian submanifolds $L_0,L_1$ of a closed symplectic manifold with $L_0$ and $L_1$ intersecting transversely and with the relevant moduli spaces regular, the Lagrangian Floer complex is well defined, $\partial^2=0$, and the homology $HF_*(L_0,L_1)$ is invariant under Hamiltonian isotopies of the $L_i$ and under the choice of $J$. The construction extends to the case of a single Lagrangian $L$ with $CF_*(L,L)$ computing the Floer homology of $L$ with itself, which is invariant under Hamiltonian isotopies of $L$, vanishes for a displaceable $L$, and is isomorphic to $H_*(L;\mathbb{Z})$, with the grading shifted by the Maslov index, whenever the obstruction to the definition of the complex vanishes.

**Proof sketch.** The analytic content is the same compactness and gluing theory as in the Hamiltonian case, with Gromov's compactness applied to the strips and the boundary conditions controlled by the Lagrangian conditions; the index is the Maslov index of the strip, which computes the dimension of the moduli space; the invariance under Hamiltonian isotopy is a continuation argument along the isotopy. The delicate point absent in the Hamiltonian case is the possibility of discs with boundary on the Lagrangians, which obstructs the definition of the complex in the non-exact case and is handled by the obstruction theory of the Fukaya category. $\square$

**Definition.** A Lagrangian $L$ is **displaceable** if there is a Hamiltonian diffeomorphism $\phi$ with $\phi(L)\cap L = \emptyset$. The **Floer homology of $L$ with itself** is the obstruction to displacement: if $HF_*(L,L)\neq0$ then $L$ is not displaceable.

**Theorem (Gromov; Lagrangian non-displacement).** Let $(M,\omega)$ be a closed symplectic manifold and let $L\subseteq M$ be a closed Lagrangian submanifold with $HF_*(L,L)\neq0$. Then $L$ is not displaceable: every Hamiltonian diffeomorphism $\phi$ satisfies $\phi(L)\cap L\neq\emptyset$. Consequently, under the isomorphism $HF_*(L,L)\cong H_*(L;\mathbb{Q})$ for the Lagrangians satisfying the regularity hypotheses,

$$
\#\,(L\cap\phi(L)) \geq \sum_{i=0}^{n} b_i(L)
$$

for a Hamiltonian diffeomorphism $\phi$ in general position: this is the **Arnold conjecture for Lagrangian intersections**. For $M=\mathbb{CP}^n$ the Clifford torus $T^n$ has nonzero Floer homology with itself and is not displaceable.

**Proof sketch.** The nonexistence of a displacement is equivalent to the existence of a Floer trajectory for every Hamiltonian isotopy connecting the two Lagrangians; the compactness of the moduli spaces of strips with fixed ends, together with the nonvanishing of the Floer homology, precludes the isotopy from separating them. The count of intersections is the rank inequality applied to the Lagrangian Floer complex, whose homology has rank $\sum b_i(L)$. Gromov's original proof used the theory of pseudoholomorphic curves in the product $M\times M$ with the diagonal Lagrangian and an adapted almost complex structure. $\square$

**Theorem (Atiyah–Floer conjecture).** Let $Y$ be a closed oriented three-manifold with a Heegaard splitting $Y = Y_1\cup_\Sigma Y_2$ along a surface $\Sigma$, and let $R(Y_i)$ be the moduli space of flat connections on $Y_i$, a Lagrangian submanifold of the moduli space $R(\Sigma)$ of flat connections on $\Sigma$ with respect to the Atiyah–Bott symplectic form. Then the Lagrangian Floer homology of the pair $(R(Y_1),R(Y_2))$ in $R(\Sigma)$ is isomorphic to the instanton Floer homology of $Y$:

$$
HF_*\bigl(R(Y_1),R(Y_2)\bigr) \cong I_*(Y).
$$

**Remark.** The conjecture is the precise form of the statement that the instanton theory of a three-manifold is the Lagrangian Floer theory of the two halves of a Heegaard splitting, and it has been verified in important cases while its general form remains open. It is a relative of the theorem of Donaldson identifying the instanton invariants of a four-manifold with the pairing in the Lagrangian Floer homology of the moduli spaces of flat connections on its boundary components: a four-manifold with boundary $\partial W = Y_0\sqcup Y_1$ gives a Lagrangian correspondence between $R(Y_0)$ and $R(Y_1)$, and the Donaldson invariants are the matrix elements of this correspondence. The structural content is that the instanton and the symplectic Floer theories are two faces of one construction, and it is the reason the instanton theory of the next section belongs to the same family as the symplectic theories.

**Remark (the Fukaya category).** The Lagrangian Floer complex of a pair $(L_0,L_1)$ is the morphism space of a category whose objects are the Lagrangian submanifolds: the composition of morphisms is defined by counting pseudoholomorphic triangles and satisfies the associativity only up to homotopy, so the category is an $A_\infty$-category, the **Fukaya category** of $M$. The obstruction theory of the previous theorem is the statement that the Fukaya category is defined over a Novikov ring, and the theory of the Fukaya category and its relation to the derived category of coherent sheaves by mirror symmetry is the subject of the homological mirror symmetry programme. The construction is the categorical form of the Lagrangian Floer theory presented here.

## Instanton Floer Homology

**Definition.** Let $Y$ be a closed oriented three-manifold, let $P\to Y$ be a principal $\mathrm{SU}(2)$-bundle, and let $\mathcal{B}$ be the space of connections on $P$ modulo gauge transformations. The **Chern–Simons functional** is

$$
\mathrm{CS}(A) = -\frac{1}{8\pi^2}\int_Y \mathrm{tr}\Bigl(A\wedge dA + \frac{2}{3}A\wedge A\wedge A\Bigr),
$$

a real-valued function on $\mathcal{B}$ whose critical points are the flat connections, and the **instanton Floer complex** $CI_*(Y)$ is the Floer complex of $\mathrm{CS}$.

**Theorem (Floer).** The critical points of the Chern–Simons functional are the gauge classes of flat connections, and the gradient flow equation is the anti-self-duality equation for a connection on the four-manifold $Y\times\mathbb{R}$ equipped with a product metric. The homology of the complex, $I_*(Y)$, is the **instanton Floer homology** — an invariant of the three-manifold $Y$, functorial under the cobordisms of four-manifolds, and one whose Euler characteristic recovers the Casson invariant: with the Casson invariant normalised as half the signed count of the irreducible flat connections, the identity is

$$
\chi\bigl(I_*(Y)\bigr) = 2\lambda(Y) .
$$

**Proof sketch.** The gradient flow of the Chern–Simons functional on the space of connections is the equation for an anti-self-dual connection on the cylinder; the compactness of the moduli spaces is Uhlenbeck's compactness theorem for anti-self-dual connections with bounded energy, with the bubbling analysis at the ends, and the gluing gives $\partial^2=0$. The index is the spectral flow of the family of Dirac operators along the path of connections, and the Euler characteristic computation is the observation that the signed count of the generators of the complex is twice the Casson invariant in the normalisation above. The analysis is that of the Yang–Mills theory of Part III. $\square$

**Example.** For the Poincaré homology sphere $\Sigma(2,3,5)$, the flat connections on the trivial $\mathrm{SU}(2)$-bundle are isolated and the instanton homology is concentrated in finitely many degrees, with Casson invariant $\lambda(\Sigma(2,3,5)) = -1$ for the standard orientation and normalisation, computed from the representation variety of the fundamental group in $\mathrm{SU}(2)$, which consists of the trivial representation and the two irreducible ones corresponding to the two embeddings of the binary icosahedral group; the Euler characteristic of the instanton homology is then $2\lambda = -2$, and the trivial connection contributes a pair of generators with opposite signs. The example is the computation that launched the theory, and the Casson invariant is the first of the modern invariants of homology three-spheres.

**Remark.** Floer's exact triangle relates the instanton homology of the three-manifolds obtained by surgery along a knot, and the triangle is the structural result from which the multiplicativity and the surgery formulae of the invariants are derived. The instanton homology is the three-dimensional shadow of the Donaldson invariants of four-manifolds, in the same way that the Hamiltonian Floer homology is the loop-space shadow of the symplectic form: the gradient flow of the Chern–Simons functional on the three-manifold is the four-dimensional equation on the cylinder, and the four-manifold invariants are computed by the pairing of the Floer groups of the boundary components.

## Heegaard Floer Homology and Contact Homology

**Definition.** Let $Y$ be a closed oriented three-manifold with a Heegaard splitting $Y = H_0\cup_\Sigma H_1$ along a surface $\Sigma$ of genus $g$, and let $\mathrm{Sym}^g(\Sigma)$ be the $g$-fold symmetric product with its symplectic form. The **Heegaard Floer complex** $\widehat{CF}(Y)$ is the Lagrangian Floer complex of the two tori $\mathbb{T}_\alpha,\mathbb{T}_\beta\subseteq\mathrm{Sym}^g(\Sigma)$ determined by the two handlebodies, with the holomorphic curves counted in the symmetric product; its homology $\widehat{HF}(Y)$ — and the refined versions $HF^+$, $HF^-$, $HF^\infty$ — are invariants of $Y$.

**Theorem (Ozsváth–Szabó).** The Heegaard Floer homology $\widehat{HF}(Y)$ is an invariant of the closed oriented three-manifold $Y$, independent of the Heegaard splitting and of the auxiliary almost complex structure; it is isomorphic to the Seiberg–Witten Floer homology of $Y$, and it satisfies the surgery exact triangle

$$
\cdots \to \widehat{HF}(Y_0(K)) \to \widehat{HF}(Y_1(K)) \to \widehat{HF}(Y_\infty(K)) \to \cdots
$$

for the three surgeries on a knot $K\subseteq Y$ with framings $0,1,\infty$. It is computable combinatorially in large classes of examples, and it gives a complete algorithm for the genus and the unknotting problem in the knot Floer theory.

**Proof sketch.** The invariance is proved by showing that the Heegaard Floer groups are isomorphic to the Seiberg–Witten Floer homology, which is manifestly an invariant; the isomorphism is the theorem of Taubes and, in full generality, of Kutluhan–Lee–Taubes. The surgery exact triangle is proved by counting holomorphic triangles in the symmetric product. $\square$

**Definition.** Let $(Y,\xi)$ be a contact three-manifold with contact form $\alpha$ and Reeb vector field $R$. The **contact homology** $HC_*(\xi)$ is the homology of a complex generated by the closed Reeb orbits, graded by the Conley–Zehnder index, with a differential counting the pseudoholomorphic cylinders in the symplectisation $Y\times\mathbb{R}$ that converge to pairs of orbits at the two ends; it is the first ingredient of the **symplectic field theory** of Eliashberg–Givental–Hofer, which extends the construction to curves of arbitrary genus and to the full contact homology algebra.

**Theorem (Eliashberg–Givental–Hofer; tautness and the dichotomy).** The symplectic field theory of the symplectisation of a contact manifold is invariant under deformations of the contact form and of the almost complex structure, and under contact isotopy; the contact homology of an overtwisted contact structure on a closed three-manifold vanishes, by a theorem of Yau, and it is nontrivial for the standard tight structure. Consequently the contact homology detects the tight–overtwisted dichotomy of *Symplectic and Contact Topology*, and the Floer-theoretic invariants of a contact structure are the obstruction to its containing an overtwisted disc.

**Proof sketch.** The count of the rigid pseudoholomorphic curves in the symplectisation is invariant by the same compactness and gluing analysis as in the closed case, with the additional care required by the non-compactness of the ends; the vanishing for the overtwisted structures is proved by an explicit reduction of the generating orbits, and the nonvanishing for the tight ones by the computation of the cylindrical contact homology of the standard contact sphere, which is that of a free loop space with the Reeb orbits of the Hopf fibration. $\square$

**Remark.** The four theories are one construction seen from four geometries: the Floer complex of a functional, with the differential counting the gradient flow lines, the grading the index of an elliptic operator, and the invariance the compactness and gluing of the corresponding moduli spaces. The theories differ in the functional — action, symplectic action, Chern–Simons, contact action — and in the equation — Floer, Cauchy–Riemann, anti-self-duality, punctured pseudoholomorphic — and they agree in the algebra of the complex and in the nature of the invariance proofs. The analytic half of each construction is the same circle of ideas: Fredholm theory, transversality, compactness, gluing, all of them belonging to Part III.

## Summary

Floer homology is the homology of a complex built from the critical points of a functional on an infinite-dimensional space, graded by the index of an elliptic operator, with a differential counting the gradient flow lines. The template requires three analytic theorems — the finite-dimensionality and regularity of the moduli spaces, the compactness up to breaking, and the invariance under the auxiliary choices — and these belong to Part III.

Hamiltonian Floer homology counts the periodic orbits of a Hamiltonian flow; its differential solves the Floer equation, its grading is the Conley–Zehnder index, and for a monotone or aspherical closed symplectic manifold it computes the singular homology of the manifold, whence the Arnold conjecture $\#\mathrm{Fix}(\phi^1_H)\geq\sum b_i(M)$ and its sharp form for $\mathbb{CP}^n$ and $T^2$. Lagrangian Floer homology counts the transverse intersections of two Lagrangians, with grading the Maslov index and differential counting pseudoholomorphic strips; it obstructs the displacement of a Lagrangian, proves the Arnold conjecture for Lagrangians, organises itself into the $A_\infty$-category called the Fukaya category, and is related by the Atiyah–Floer conjecture to the instanton theory. Instanton Floer homology is the Floer theory of the Chern–Simons functional, whose gradient flow is the anti-self-duality equation on a four-manifold with cylindrical ends; it is an invariant of a three-manifold whose Euler characteristic is twice the Casson invariant, and it is linked to the Donaldson invariants by exact triangles and by the Atiyah–Floer picture. Heegaard Floer homology is the Lagrangian Floer theory of the symmetric product of a Heegaard surface, isomorphic to the Seiberg–Witten Floer homology, with a surgery exact triangle and effective computations; contact homology is the Floer theory of the symplectisation, and it detects the tight–overtwisted dichotomy of contact topology.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $X$, $\mathcal{A}$, $\nabla_{\mathcal{A}}$ | Infinite-dimensional space, functional, gradient section of the Floer template |
| $\partial x = \sum_y \#\mathcal{M}(x,y)y$ | Floer differential, counting flow lines of index difference one |
| $CF_*, HF_*$ | Floer complex and Floer homology |
| $\mu(x)$ | Conley–Zehnder index of a periodic orbit; Maslov index of a Lagrangian intersection |
| $X_H$, $\phi^1_H$ | Hamiltonian vector field and its time-one flow |
| Floer equation | $\partial_s u + J(u)(\partial_t u - X_H(t,u))=0$, a pseudoholomorphic cylinder with a Hamiltonian term |
| $CF_*(M,H)$ | Hamiltonian Floer complex on the contractible periodic orbits |
| $L_0, L_1$ | Lagrangian submanifolds; $CF_*(L_0,L_1)$ on $L_0\cap L_1$ |
| Pseudoholomorphic strip | $\partial_s u + J(u)\partial_t u = 0$, $u(\cdot,0)\in L_0$, $u(\cdot,1)\in L_1$ |
| $\mathrm{CS}(A)$ | Chern–Simons functional on connections over a three-manifold |
| $I_*(Y)$, $\lambda(Y)$ | Instanton Floer homology of a three-manifold; Casson invariant, with $\chi(I_*(Y)) = 2\lambda(Y)$ |
| $\widehat{HF}(Y)$ | Heegaard Floer homology; isomorphic to Seiberg–Witten Floer homology |
| $HC_*(\xi)$, SFT | Contact homology and symplectic field theory of the symplectisation |
| Fukaya category | $A_\infty$-category with objects Lagrangians and morphism spaces Lagrangian Floer complexes |



## Further Reading

- Andreas Floer, "Morse Theory for Lagrangian Intersections", *Journal of Differential Geometry* 28 (1988), 513–547, for Lagrangian Floer homology and the Arnold conjecture for Lagrangians.
- Andreas Floer, "Symplectic Fixed Points and Holomorphic Spheres", *Communications in Mathematical Physics* 120 (1989), 575–611, for Hamiltonian Floer homology and the Arnold conjecture.
- Andreas Floer, "An Instanton Invariant for 3-Manifolds", *Communications in Mathematical Physics* 118 (1988), 215–240, for instanton Floer homology and the Casson invariant.
- Sergei Piunikhin, Dietmar Salamon and Matthias Schwarz, "Symplectic Floer–Donaldson Theory and Quantum Cohomology", *Contact and Symplectic Geometry* (Cambridge University Press, 1996), 171–200, for the PSS isomorphism between Floer and singular homology.
- Kenji Fukaya, Yong-Geun Oh, Hiroshi Ohta and Kaoru Ono, *Lagrangian Intersection Floer Theory: Anomaly and Obstruction* (American Mathematical Society, 2009), for the Fukaya category and the obstruction theory in the non-exact case.
- Peter Ozsváth and Zoltán Szabó, "Holomorphic Disks and Three-Manifold Invariants: Properties", *Annals of Mathematics* 159 (2004), 1159–1245, for Heegaard Floer homology, the surgery exact triangle and the relation to Seiberg–Witten theory.
- Yakov Eliashberg, Alexander Givental and Helmut Hofer, "Introduction to Symplectic Field Theory", *Geometric and Functional Analysis* 2000, Special Volume, 560–673, for contact homology and the invariants of the symplectisation.
- Michael Atiyah, "New Invariants of 3- and 4-Dimensional Manifolds", *Proceedings of the Symposium on the Mathematical Heritage of Hermann Weyl* (American Mathematical Society, 1988), 285–299, for the Atiyah–Floer conjecture and the relation between instanton and Lagrangian Floer theory.
- Nikolai Saveliev, *Lectures on the Homology of 3-Manifolds* (Springer, 1999), for the Casson invariant, the homology cobordism invariants and the computations for the Poincaré sphere.
