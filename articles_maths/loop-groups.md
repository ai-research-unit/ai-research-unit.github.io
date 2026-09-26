
# __Loop Groups__

## Introduction

The loop group of a Lie group $G$ is the group $LG$ of maps from the circle $S^1$ into $G$, with the pointwise multiplication; when $G$ is a compact Lie group the natural object is the group of smooth loops, and when $G$ is a complex algebraic group the natural object is the group of polynomial loops $\Lambda G = G(\mathbb{C}[t,t^{-1}])$, that is, $G$ applied to the Laurent polynomial ring. The loop group is the simplest infinite-dimensional Lie group that is not a group of diffeomorphisms of a finite-dimensional manifold: it is a Fréchet manifold in the smooth case and an ind-variety in the algebraic case, its Lie algebra is the loop algebra $L\mathfrak{g} = \mathfrak{g}\otimes_{\mathbb{C}}\mathbb{C}[t,t^{-1}]$, and it is the standard example in which the Lie functor fails to be an equivalence — the exponential map is not locally surjective, so the Lie algebra does not determine the group, as discussed in *Hilbert's Fifth Problem and Infinite-Dimensional Lie Theory*.

Two structures make the theory: the **central extension** of the loop algebra by the one-dimensional cocycle $\omega(x,y) = \operatorname{Res}\langle x', y\rangle\,dt$, which adds the centre and the derivation to give the **affine Kac–Moody algebra** $\hat{\mathfrak{g}} = L\mathfrak{g}\oplus\mathbb{C} c\oplus\mathbb{C} d$; and the **Bruhat and Birkhoff decompositions** of the loop group, which are the affine analogues of the decompositions of $G$ and which stratify both the group and the **affine Grassmannian** $G(\mathbb{C}[t,t^{-1}])/G(\mathbb{C}[[t]])$ by the affine Weyl group $\widetilde{W} = W\ltimes\Lambda$ where $W$ is the Weyl group of $\mathfrak{g}$ and $\Lambda$ the cocharacter lattice. The affine Grassmannian is the ind-projective variety whose Schubert cells are indexed by the dominant coweights, and it is the geometric home of the representation theory of the affine algebra: the integrable highest weight modules of the Kac–Moody algebra have characters given by the Weyl–Kac formula, and the geometric Satake theory relates the representations of the dual group to the strata of the Grassmannian.

The loop groups are the analytic and algebraic realisation of the Kac–Moody groups of affine type: where the Kac–Moody group is defined by a presentation from a generalised Cartan matrix, the loop group realises the affine case as a group of loops, and the two pictures meet in the decomposition theory and in the central extension. The article develops the loop group and the loop algebra with the residue pairing, the central extension and the affine Kac–Moody algebra, the affine Bruhat and Birkhoff decompositions, the affine Grassmannian and its Schubert cells, the infinite-dimensional manifold structure with the failure of the exponential map, and the Kähler structure of the based loop group. The input from above is the finite-dimensional Lie theory of *Lie Groups*, *The Lie Algebra and the Exponential Map* and *The Lie Correspondence and the Adjoint Representation*, the infinite-dimensional framework of *Hilbert's Fifth Problem and Infinite-Dimensional Lie Theory*, the root systems and Weyl groups of *Root Systems and Classification*, and the buildings and affine Weyl groups of *Bruhat–Tits Theory* and *Buildings and Tits Systems*. The **loop group**, the **loop algebra**, the **affine Kac–Moody algebra** and the **affine Grassmannian** are defined in line; the affine Kac–Moody groups themselves are not covered here.

The boundary with Part III is the one fixed for this block. What is developed here is the group-theoretic and algebraic structure: the loop group and its subgroups, the loop algebra, the residue pairing and the central extension, the affine Kac–Moody algebra, the affine Weyl group, the Bruhat and Birkhoff decompositions and the affine Grassmannian as an ind-variety. What is deferred is the **analytic** theory: the smooth and Sobolev completions $H^s(S^1,\mathfrak{g})$ of the loop algebra and the loop group (a completion in the analytic sense), the Fourier analysis of the loops and the corresponding $L^2$-theory, the positive energy representations of the loop group on Hilbert spaces and the semigroup of the disc, the Kac–Moody characters as analytic functions, and the measure-theoretic and probabilistic aspects of the Brownian loops — all of which belong to *Analysis on Groups*,and the infinite-dimensional analysis of Part III. The **residue** used in the cocycle is the algebraic coefficient of $t^{-1}$ in $\mathbb{C}((t))$ and involves no integration. No physics is invoked.

## The Loop Group and the Loop Algebra

### The Algebraic Loop Group

**Definition.** Let $G$ be a connected simply connected simple algebraic group over $\mathbb{C}$ and let $\Lambda G = G(\mathbb{C}[t,t^{-1}])$ be the group of its $\mathbb{C}[t,t^{-1}]$-points: the group of the **Laurent polynomial loops** in $G$. The group $\Lambda G$ contains the **positive loop group** $\Lambda^+G = G(\mathbb{C}[[t]])$, the **negative loop group** $\Lambda^-G = G(\mathbb{C}[t^{-1}])$ of the loops regular at $\infty$, the **polynomial loop group** $G(\mathbb{C}[t])$, and, for each point $z\in\mathbb{C}^\times$ or more generally for the evaluation at $t = 0$, the evaluation map $\Lambda^+G \to G$, $f\mapsto f(0)$; the **Iwahori subgroup** of $\Lambda G$ is the preimage $I$ of a Borel subgroup $B\leq G$ under this evaluation.

**Example.** For $G = SL_2$, the loop group $\Lambda SL_2$ is the group of $2\times2$ matrices with entries in $\mathbb{C}[t,t^{-1}]$ and determinant $1$; the matrix $\mathrm{diag}(t,t^{-1})$ is a loop that is neither in $\Lambda^+G$ nor in $\Lambda^-G$ and generates, together with the constant loops, the "translation" part of the affine Weyl group; for $G = GL_n$ the loop group is the group of invertible matrices over $\mathbb{C}[t,t^{-1}]$ and the determinant is a Laurent polynomial, so that $GL_n(\mathbb{C}[t,t^{-1}])$ is not the direct product of $SL_n$ and the constants but the determinant contributes a factor of the units $\mathbb{C}[t,t^{-1}]^\times = \mathbb{C}^\times t^{\mathbb{Z}}$.

**Definition.** The **smooth loop group** $LG = C^\infty(S^1,G)$ is the group of smooth maps from the circle into a compact Lie group $G$, with the pointwise product and the topology of uniform convergence of all the derivatives; it is a Fréchet Lie group modelled on the Fréchet space $C^\infty(S^1,\mathfrak{g})$ of the smooth loops in the Lie algebra. The **based loop group** $\Omega G$ is the subgroup of the loops $\gamma$ with $\gamma(1) = e$; the splitting $LG \cong G\times\Omega G$ by the evaluation at $1$ is a homeomorphism and a diffeomorphism of Fréchet manifolds, but not a group isomorphism.

### The Loop Algebra and the Residue Pairing

**Definition.** The **loop algebra** of a complex simple Lie algebra $\mathfrak{g}$ is the Lie algebra

$$
L\mathfrak{g} = \mathfrak{g}\otimes_{\mathbb{C}}\mathbb{C}[t,t^{-1}]
$$

with the bracket $[x\otimes t^m, y\otimes t^n] = [x,y]\otimes t^{m+n}$. It is a Lie algebra over $\mathbb{C}$, infinite-dimensional, graded by $\mathbb{Z}$ with the degree of $x\otimes t^m$ equal to $m$, and it is the Lie algebra of the algebraic loop group $\Lambda G$ in the algebraic sense: the derivations of the coordinate ring of $G(\mathbb{C}[t,t^{-1}])$ at the identity form $L\mathfrak{g}$.

**Definition (the residue).** The **residue** of an element $f = \sum_{n\in\mathbb{Z}}f_nt^n \in \mathbb{C}((t))$ is $\operatorname{Res}(f) = f_{-1}$, the coefficient of $t^{-1}$; it is $\mathbb{C}$-linear, vanishes on the Laurent polynomials that are derivatives, $\operatorname{Res}(f') = 0$, and is the algebraic form of the integration of a one-form over the circle. Let $\langle\cdot,\cdot\rangle$ be the normalised invariant bilinear form on $\mathfrak{g}$, the **Killing form** divided by twice the dual Coxeter number, so that the long roots have square length $2$; the form is symmetric, invariant and nondegenerate, and the induced form on $L\mathfrak{g}$ given by

$$
(x\otimes t^m, y\otimes t^n) \longmapsto \langle x,y\rangle\,\delta_{m+n,0}
$$

is invariant and nondegenerate.

**Proposition (the derivative and the residue pairing).** The $\mathbb{C}$-bilinear form

$$
\omega(x,y) = \operatorname{Res}\bigl(\langle x', y\rangle\,dt\bigr) = \sum_{m+n=0} m\,\langle x_m, y_n\rangle = \sum_{m\in\mathbb{Z}} m\,\langle x_m, y_{-m}\rangle
$$

on $L\mathfrak{g}$, where $x = \sum x_mt^m$, $y = \sum y_nt^n$ and $x' = \sum m x_m t^{m-1}$, is a two-cocycle: it is alternating and satisfies the cocycle identity

$$
\omega([x,y],z)+\omega([y,z],x)+\omega([z,x],y) = 0 ,
$$

and it is the unique, up to scalar, invariant two-cocycle on $L\mathfrak{g}$ that is continuous for the grading; it is not a coboundary.

**Proof sketch.** The alternating property is clear from $m\langle x_m,y_{-m}\rangle = -(-m)\langle y_{-m},x_{m}\rangle$; the cocycle identity is checked on the homogeneous components using the invariance of $\langle\cdot,\cdot\rangle$ and the identity $\operatorname{Res}(f') = 0$: the terms combine into the derivative of a product, hence vanish under the residue. The uniqueness is a computation in the invariant theory of the graded Lie algebra $L\mathfrak{g}$, and the class of $\omega$ generates $H^2(L\mathfrak{g},\mathbb{C})$, which is one-dimensional for $\mathfrak{g}$ simple (the spaces $H^2(L\mathfrak{g})$ being computed by the standard spectral sequence and vanishing outside degree $1$). The results are standard and are quoted from the literature. $\square$

## The Central Extension and the Affine Kac–Moody Algebra

### The Affine Kac–Moody Algebra

**Definition.** The **affine Kac–Moody algebra** associated with a simple Lie algebra $\mathfrak{g}$ is

$$
\hat{\mathfrak{g}} = L\mathfrak{g}\oplus\mathbb{C} c\oplus\mathbb{C} d ,
$$

with $c$ central, $[d, x\otimes t^m] = m\,x\otimes t^m$, and

$$
[x\otimes t^m, y\otimes t^n] = [x,y]\otimes t^{m+n} + m\,\langle x,y\rangle\,\delta_{m+n,0}\,c .
$$

The element $c$ is the **canonical central element**, $d$ the **derivation** or energy operator, the **level** of a representation is the scalar by which $c$ acts, and the subalgebra $\hat{\mathfrak{g}}' = L\mathfrak{g}\oplus\mathbb{C} c$ is the **universal central extension** of the loop algebra afforded by the cocycle $\omega$. The algebra $\hat{\mathfrak{g}}$ is the **affine Kac–Moody algebra** of type $\mathfrak{g}^{(1)}$, with a generalised Cartan matrix of affine type obtained from the Cartan matrix of $\mathfrak{g}$ by adjoining the null root; the **affine root system** has the imaginary null root $\delta$ and the real roots $\alpha+n\delta$, and the **affine Weyl group** is

$$
W_{\mathrm{aff}} = W\ltimes\Lambda_{\mathrm{coroot}} ,
$$

generated by the reflections in the affine root hyperplanes, where $W$ is the Weyl group of $\mathfrak{g}$ and $\Lambda_{\mathrm{coroot}}$ the coroot lattice. The **extended affine Weyl group** $\widetilde W = W\ltimes\Lambda$ with the cocharacter lattice $\Lambda$ includes the diagram automorphisms and acts on the affine root system.

**Example (the case $\mathfrak{g} = \mathfrak{sl}_2$).** For $\mathfrak{sl}_2$ the affine algebra $\hat{\mathfrak{sl}}_2$ has the Chevalley generators $e_i, f_i, h_i$ indexed by the two nodes of the affine diagram and the relations of the affine Cartan matrix $\begin{pmatrix}2&-2\\-2&2\end{pmatrix}$; the null root is $\delta = \alpha_0+\alpha_1$, which is not a real root, and the affine Weyl group is the infinite dihedral group $W\ltimes \mathbb{Z}\alpha^\vee$ acting on the line, exactly the group of the apartment of the tree in *Bruhat–Tits Theory*: the affine Weyl group of the loop group is the group that appears as the affine Weyl group of the $p$-adic group of the same root data, and the coincidence is the algebraic form of the fact that both buildings are of the same type.

### The Kac–Moody Group

**Definition.** The **Kac–Moody group** $\widehat{\Lambda G}$ of affine type, also called the **loop group with the central extension**, is the group $(\Lambda G)$-extension defined by the $\mathbb{C}^\times$-extension

$$
1 \longrightarrow \mathbb{C}^\times \longrightarrow \widehat{\Lambda G} \longrightarrow \Lambda G \longrightarrow 1
$$

whose Lie algebra is $\hat{\mathfrak{g}}' = L\mathfrak{g}\oplus\mathbb{C} c$. The cocycle $\omega$ takes integral values on the lattice of the loops, so the extension exists as an extension of the algebraic group $\Lambda G$; the existence and the integrality are the transgression statement of the loop-group theory, and the cohomological language used to state it is that of the section *Algebraic Topology*. The group $\widehat{\Lambda G}$ is the **affine Kac–Moody group** associated with $G$, and it is the central extension whose representation theory at level $k$ is the representation theory of $\hat{\mathfrak{g}}$ with the centre acting by $k$.

**Theorem (the affine Weyl group and the decompositions).** With $I$ an Iwahori subgroup of $\Lambda G$ and $\widetilde W$ the extended affine Weyl group,

**(a)** (affine Bruhat decomposition) $\Lambda G = \bigsqcup_{w\in\widetilde W} I\,w\,I$, the union being disjoint, and each double coset is an affine space of dimension the length of $w$ in the affine Weyl group;

**(b)** (Birkhoff decomposition) $\Lambda G = \bigsqcup_{w\in W_{\mathrm{aff}}}\,\Lambda^-G\, w\, \Lambda^+G$, and the orbits of $\Lambda^+G$ on the "big cell" are the affine cells indexed by $w$; the corresponding decomposition of the loop algebra is the triangular decomposition of the affine algebra;

**(c)** the affine Grassmannian $\mathrm{Gr} = \Lambda G/\Lambda^+G$ is an ind-projective variety over $\mathbb{C}$, and its $\Lambda^+G$-orbits are the **Schubert cells** $\mathrm{Gr}_\lambda$ indexed by the dominant coweights $\lambda$, with $\mathrm{Gr}_\mu \subseteq \overline{\mathrm{Gr}_\lambda}$ when $\mu \leq \lambda$ in the dominance order on the coweights; the closures $\overline{\mathrm{Gr}_\lambda}$ are projective varieties of dimension $\langle\lambda, 2\rho\rangle$ in the standard pairing between the coweights and the weights.

**Proof sketch.** The affine Bruhat decomposition follows from the finite-dimensional Bruhat decomposition applied to the group ind-scheme $\Lambda G$ and the theory of the Iwahori subgroup: the double cosets $I\setminus\Lambda G/I$ form a building which is the affine building of the group over $\mathbb{C}((t))$ (the algebraic model of the Bruhat–Tits building of *Bruhat–Tits Theory*), and the Bruhat cells are indexed by the affine Weyl group. The Birkhoff decomposition is the appendix of the same theory, obtained from the Bruhat decomposition of the "double" loop group; the Grassmannian statement follows because the $G(\mathbb{C}[[t]])$-orbits on $\mathrm{Gr}$ are classified by the coweights and the closures of the orbits are the Schubert varieties of the affine flag variety. The statements are standard and are quoted from the literature. $\square$

## The Infinite-Dimensional Structure

### The Manifold Structure and the Failure of the Exponential Map

**Theorem (the loop group as a Lie group).** Let $G$ be a compact connected Lie group.

**(a)** The smooth loop group $LG = C^\infty(S^1,G)$ is a Fréchet manifold modelled on $C^\infty(S^1,\mathfrak{g})$; it is a topological group with the composition and inversion smooth in the Fréchet sense, hence an infinite-dimensional Lie group, and it is not locally compact.

**(b)** The exponential map $\exp : C^\infty(S^1,\mathfrak{g})\to C^\infty(S^1,G)$, the pointwise exponential, is a smooth map but is **not locally surjective**: the image of a neighbourhood of $0$ is a proper subset of a neighbourhood of the identity, so the inverse function theorem fails and the Lie functor is not an equivalence. The same failure occurs for the algebraic loop group, which is a group ind-scheme.

**(c)** The loop group carries no Haar measure, being infinite-dimensional and not locally compact; the invariant "measure" on it is replaced by the measure on the infinite-dimensional manifold in the sense of the Gaussian or the formal volume, which belongs to the analysis of the infinite-dimensional spaces in Part III.

**Proof sketch.** (a) The Fréchet manifold structure is standard: the loops close to a given loop form a chart via the exponential of the Lie algebra, and the group operations are smooth for the Fréchet structure. (b) The failure of the local surjectivity of the pointwise exponential for a loop is the failure for a single value of the parameter: a loop close to the identity whose value at some point is not in the image of the exponential of the group; since the exponential of a compact connected group is surjective but need not be locally surjective — it fails at the antipode of $SU(2)$, for example — taking loops with values in a neighbourhood not covered by the differential produces a counterexample, and the algebra behaves similarly. The discussion of the failure of the Lie correspondence in infinite dimensions is that of *Hilbert's Fifth Problem and Infinite-Dimensional Lie Theory*. $\square$

### The Kähler Structure of the Based Loop Group

**Theorem (Atiyah–Pressley).** Let $G$ be a compact simply connected simple Lie group and let $\Omega G$ be its based loop group.

**(a)** The based loop group $\Omega G$ is a Kähler manifold of infinite dimension, with a complex structure defined by the **Birkhoff decomposition** and a Kähler form $\omega$ whose value on the tangent vectors $X,Y \in C^\infty(S^1,\mathfrak{g})$ with the loops vanishing at the base point is the pairing

$$
\omega(X,Y) = \int_{S^1}\langle X(\theta), Y'(\theta)\rangle\,\mathrm{d}\theta ,
$$

the **Atiyah–Pressley form**, which is closed, nondegenerate and invariant under $\Omega G$.

**(b)** The **energy functional** $E(\gamma) = \int_{S^1}\langle \gamma^{-1}\gamma', \gamma^{-1}\gamma'\rangle\,\mathrm{d}\theta$ is a Morse–Bott function on $\Omega G$ whose critical points are the geodesic loops $\gamma(\theta) = \exp(\theta\xi)$ for $\xi$ in the Lie algebra, and the critical manifolds are the **integral manifolds**; the energy stratification is the classical Morse theory of the based loop space, whose Lie-algebraic shadow is the affine Weyl group.

**(c)** The complex structure is compatible with the left action of $\Omega G$, and the Birkhoff decomposition identifies the "big cell" of the based loop group with a complex vector space; the intersection of the Birkhoff cells with the based condition gives the Schubert cell decomposition of the affine Grassmannian, and the complexification of the loop group is the loop group of the complexification, on which the Birkhoff decomposition plays the role of the polar decomposition.

**Proof sketch.** The form $\omega$ is the transgression of the invariant three-form on $G$ to the loop space, closed because the three-form is closed; its non-degeneracy and the invariance under the action of $\Omega G$ are the two properties that make the Riemannian metric on $\Omega G$ Kähler. The identification of the critical points of the energy is the calculus of variations for the geodesic loops, and the Morse theory is the classical one. The statements are the theorems of Atiyah and Pressley and are quoted from the literature; the analytic completion of the loops and the Hilbert-space theory of the harmonic analysis on $\Omega G$ are Part III. $\square$

### The Integrable Representations and the Weyl–Kac Formula

**Definition.** An $\hat{\mathfrak{g}}$-module $V$ is a **highest weight module** of **level** $k$ if it is generated by a vector $v$ annihilated by the subalgebra $\mathfrak{g}\otimes\mathbb{C}[t]\oplus\mathbb{C} d$ and by the positive part of $\mathfrak{g}$, with $c$ acting by $k$ and $d$ acting by a scalar; it is **integrable** if the Chevalley generators $e_i, f_i$ act locally nilpotently. The integrable highest weight modules of level $k$ are the **standard modules** $L(\lambda)$ with $\lambda$ a dominant integral weight of level $k$.

**Theorem (Weyl–Kac character formula).** The character of the integrable highest weight module $L(\lambda)$ of the affine algebra $\hat{\mathfrak{g}}$ is

$$
\operatorname{ch}L(\lambda) = \frac{\sum_{w\in\widetilde W}(-1)^{\ell(w)}\,e^{w(\lambda+\rho)-\rho}}{\prod_{\alpha>0}(1-e^{-\alpha})^{\mathrm{mult}\,\alpha}} ,
$$

the sum over the extended affine Weyl group and the product over the positive affine roots, with the multiplicities of the imaginary roots accounted for; the formula specialises to the classical Weyl character formula when the level is zero and gives the **Kac–Weyl denominator identity** for the affine algebra. The representations are the algebraic input into the geometric theory: the **geometric Satake equivalence** identifies the tensor category of the representations of the Langlands dual group with the category of the equivariant perverse sheaves on the affine Grassmannian, so that the Schubert cells of the Grassmannian are the geometric counterpart of the weight spaces; the statement is quoted as a pointer to the geometric theory of the affine Grassmannian, which lies beyond this article.

**Proof sketch.** The character formula is the Weyl character formula in the Kac–Moody setting, proved by the same argument of the Verma modules and the Weyl group inversion, and the denominator identity is the specialisation to the trivial representation; the geometric Satake statement is the theorem of Mirković and Vilonen and is quoted from the literature. The representation theory itself, being finitely generated algebraic representation theory, is the affine case; the analytic realisation of the same modules on Hilbert spaces is Part III. $\square$

**Remark (loop groups and the buildings).** The affine Weyl group $\widetilde W$ of the loop group is the group that acts on the standard apartment of the affine building of the group over the field $\mathbb{C}((t))$, the local field of Laurent series; the affine Bruhat decomposition of the loop group is the Bruhat decomposition of the affine building, and the Iwahori subgroup $I$ is the stabiliser of an alcove. The loop group is thus the "algebraic model" of the affine building of the group over the Laurent series field, and the correspondence between the loop groups and the affine buildings of *Bruhat–Tits Theory* is the correspondence between the "positive" and the "residue" descriptions of the same object. The loop algebra is the Lie algebra of the building's group at the "level" of the Laurent field, and the central extension is the extra structure that the loop group carries and the $p$-adic group does not.

## The Boundary with Analysis

The theory of this article is algebraic and group-theoretic; the analysis of the loop group is Part III.

- The **smooth and Sobolev completions** $H^s(S^1,\mathfrak{g})$ and $H^s(S^1,G)$ of the loop algebra and the loop group, the **Fourier analysis** of the loops, the **$L^2$-spaces** and the **Hilbert space completions** are Part III; the algebraic loop group and the polynomial loop algebra are the objects of this article.
- The **positive energy representations** of the loop group, the **projective representations** of the loop group at level $k$, the **semigroup** of the disc and the **analytic realisation** of the integrable modules are Part III, where the Hilbert space and the operator theory are available; the **Weyl–Kac character** is stated above as a formal identity and its analytic convergence belongs to Part III.
- The **measure-theoretic and probabilistic analysis** of the loop spaces: the Brownian motion on the loop group, the heat kernel, the Wiener measure and the infinite-dimensional Gaussians, are Part III.
- The **Kähler geometry** of $\Omega G$: the Atiyah–Pressley form and the complex structure are stated above as theorems; their deep analytic and geometric development belongs with the infinite-dimensional geometry of Part III.
- What is *not* deferred: the algebraic and smooth loop groups; the loop algebra and the residue pairing; the fundamental two-cocycle and the affine Kac–Moody algebra; the affine and extended affine Weyl groups; the affine Bruhat and Birkhoff decompositions; the affine Grassmannian and its Schubert cells as an ind-variety; the failure of the exponential map; the Atiyah–Pressley form at the level of statement; and the Weyl–Kac character formula.

## Summary

The loop group of a group $G$ is the group of loops $S^1\to G$: in the algebraic setting the polynomial loops $\Lambda G = G(\mathbb{C}[t,t^{-1}])$ and in the smooth setting the Fréchet Lie group $LG = C^\infty(S^1,G)$, with the based loop group $\Omega G$ of the loops with base point fixed. The loop algebra $L\mathfrak{g} = \mathfrak{g}\otimes\mathbb{C}[t,t^{-1}]$ has the invariant two-cocycle $\omega(x,y) = \operatorname{Res}\langle x',y\rangle dt$, which is unique up to scalar and not a coboundary, and its universal central extension adjoined to the derivation gives the affine Kac–Moody algebra $\hat{\mathfrak{g}} = L\mathfrak{g}\oplus\mathbb{C} c\oplus\mathbb{C} d$ with the bracket $[x\otimes t^m,y\otimes t^n] = [x,y]\otimes t^{m+n} + m\langle x,y\rangle\delta_{m+n,0}c$. The affine Weyl group $W_{\mathrm{aff}} = W\ltimes\Lambda_{\mathrm{coroot}}$ and the extended affine Weyl group $\widetilde W$ act on the affine root system and index the decompositions.

The Iwahori subgroup $I$ of $\Lambda G$ gives the affine Bruhat decomposition $\Lambda G = \bigsqcup_{w\in\widetilde W}IwI$, the Birkhoff decomposition $\Lambda G = \bigsqcup\Lambda^-G w\Lambda^+G$ gives the cells of the affine Grassmannian $\mathrm{Gr} = \Lambda G/\Lambda^+G$, an ind-projective variety whose Schubert cells are indexed by the dominant coweights with the closure order the dominance order. The loop group is a Fréchet/ind-variety infinite-dimensional group on which the exponential map is not locally surjective, so the Lie correspondence fails; the based loop group $\Omega G$ is a Kähler manifold with the Atiyah–Pressley form, and the integrable highest weight modules of $\hat{\mathfrak{g}}$ have the Weyl–Kac characters. The central extension is the extra structure that distinguishes the loop group from the $p$-adic group of the same root data, and it is the algebraic model of the affine building. The Sobolev completions, the positive energy representations, the Hilbert-space theory and the probabilistic analysis of the loops belong to Part III.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $LG = C^\infty(S^1,G)$ | Smooth loop group of a compact Lie group |
| $\Omega G$ | Based loop group $\{\gamma : \gamma(1)=e\}$ |
| $\Lambda G = G(\mathbb{C}[t,t^{-1}])$ | Algebraic (Laurent polynomial) loop group |
| $\Lambda^+G = G(\mathbb{C}[[t]])$ | Positive loop group |
| $\Lambda^-G = G(\mathbb{C}[t^{-1}])$ | Negative loop group |
| $I$ | Iwahori subgroup: preimage of a Borel under evaluation at $t=0$ |
| $L\mathfrak{g} = \mathfrak{g}\otimes\mathbb{C}[t,t^{-1}]$ | Loop algebra |
| $\operatorname{Res}$ | Residue: coefficient of $t^{-1}$ in $\mathbb{C}((t))$ |
| $\langle\cdot,\cdot\rangle$ | Normalised invariant form (Killing form / $2h^\vee$) |
| $\omega(x,y)=\operatorname{Res}\langle x',y\rangle dt$ | Fundamental two-cocycle on $L\mathfrak{g}$ |
| $\hat{\mathfrak{g}} = L\mathfrak{g}\oplus\mathbb{C} c\oplus\mathbb{C} d$ | Affine Kac–Moody algebra |
| $c$, $d$ | Central element (level); derivation (energy) |
| $\hat{\mathfrak{g}}' = L\mathfrak{g}\oplus\mathbb{C} c$ | Universal central extension of the loop algebra |
| $\delta$ | Null (imaginary) root of the affine system |
| $W_{\mathrm{aff}} = W\ltimes\Lambda_{\mathrm{coroot}}$, $\widetilde W$ | Affine and extended affine Weyl groups |
| $\widehat{\Lambda G}$ | Kac–Moody group: $\mathbb{C}^\times$-central extension of $\Lambda G$ |
| $\mathrm{Gr} = \Lambda G/\Lambda^+G$ | Affine Grassmannian, an ind-projective variety |
| $\mathrm{Gr}_\lambda$ | Schubert cell of the dominant coweight $\lambda$ |
| affine Bruhat decomposition | $\Lambda G = \bigsqcup_{w\in\widetilde W}IwI$ |
| Birkhoff decomposition | $\Lambda G = \bigsqcup_{w}\Lambda^-G w\Lambda^+G$ |
| $E$, $\omega_{\mathrm{AP}}$ | Energy functional; Atiyah–Pressley Kähler form on $\Omega G$ |
| $\operatorname{ch}L(\lambda)$ | Character of the integrable module; Weyl–Kac formula |
| $H^s(S^1,\mathfrak{g})$ | Sobolev completion (Part III) |





## Further Reading

- Andrew Pressley and Graeme Segal, *Loop Groups* (Oxford University Press, 1986), for the systematic theory of the loop groups, the central extensions and the decompositions.
- Victor G. Kac, *Infinite Dimensional Lie Algebras* (Cambridge University Press, 3rd ed. 1990), for the affine Kac–Moody algebras, the root systems and the Weyl–Kac character formula.
- Michael F. Atiyah and Andrew Pressley, *Convexity and loop groups*, in Arithmetic and Geometry II (Birkhäuser, 1983), 33–63, for the Kähler structure of the based loop group.
- Graeme Segal, *Loop groups and harmonic maps*, in Advances in Homotopy Theory (Cambridge University Press, 1989), for the analytic and geometric applications.
- Ivan Mirković and Kari Vilonen, *Geometric Langlands duality and representations of algebraic groups over commutative rings*, Annals of Mathematics 166 (2007), 95–143, for the geometric Satake equivalence and the perverse sheaves on the affine Grassmannian.
- Shrawan Kumar, *Kac–Moody Groups, their Flag Varieties and Representation Theory* (Birkhäuser, 2002), for the Kac–Moody groups, the affine flag varieties and the representation theory.
- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory* (Springer, 1972), for the finite-dimensional background and the root systems.
- Igor Frenkel and David Ben-Zvi, *Vertex Algebras and Algebraic Curves* (American Mathematical Society, 2nd ed. 2004), for the algebraic realisation of the level-$k$ representations.
- Peter Schneider and Ulrich Stuhler, *Representation theory and sheaves on the Bruhat–Tits building*, Publications Mathématiques de l'IHÉS 85 (1997), 97–191, for the analogue between the loop groups and the $p$-adic groups.
