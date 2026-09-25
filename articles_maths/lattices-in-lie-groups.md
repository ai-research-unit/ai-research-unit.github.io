
# __Lattices in Lie Groups__

## Introduction

A **lattice** in a locally compact group $G$ is a discrete subgroup $\Gamma$ whose coset space $G/\Gamma$ carries a finite $G$-invariant measure. The notion sits at the meeting point of three of the corpus's subjects: because $\Gamma$ is discrete it is a group of Part I's kind; because $G$ is a Lie group it carries the differential structure of *Lie Groups*; and because the quotient has finite measure, which is what makes the notion non-trivial, it is the Haar measure of *Locally Compact Groups and Haar Measure* that is used. For $G = \mathbb{R}^n$ a lattice is a full-rank lattice in the elementary sense, and the theory is the geometry of numbers; for $G$ a semisimple Lie group the lattices are the discrete groups of finite covolume, and the theory is one of the central subjects of the corpus: the arithmetic groups of with this one, are the principal source of examples, and the rigidity theorems — Mostow rigidity, strong rigidity, the Borel density theorem, the arithmeticity theorem — are the principal structural results.

The article develops the definition and the first properties, in particular the fact that a group admitting a lattice is unimodular and that the covolume is well defined up to the normalisation of the Haar measure; the examples in the Euclidean, nilpotent and semisimple cases; the existence theorem of Borel and Harish-Chandra and the compactness criterion of Godement; the structure of lattices in nilpotent and solvable groups after Mal'cev; and the rigidity and density theorems. The Lie-theoretic input — the structure theory of semisimple Lie algebras, the Cartan decomposition, the symmetric space — is that of *Lie Groups*, *The Lie Correspondence and the Adjoint Representation* andused at the level of a homogeneous space carrying a $G$-invariant proper distance. The representation-theoretic input — the unitary dual, induced representations, property (T) — is that of the three earlier articles of this batch, and property (T) is used in its own article *Property (T)*, which lies immediately above this one.

The boundary with Part III is the one fixed for this block: the **measure-theoretic and dynamical** theory — the ergodicity of the action of a lattice on the quotient, the mixing and equidistribution of the geodesic flow, the classification of invariant measures (Ratner's theorems), the computation of covolumes by integration, and the counting of rational points — belongs and its companions in Part III, where the measure and the limit are available. What is developed here is the structure of the lattice as a discrete subgroup and as a geometric object, with the Haar measure used only to *define* covolume and to state the standard results. The number theory used at the level of statements is that of *Algebraic Number Theory* in Part I, and the arithmetic subgroups are defined in line, their theory being . No physics is invoked.

## Definitions and First Properties

### Covolume

**Definition.** Let $G$ be a locally compact group with left Haar measure $\mu$ and let $\Gamma \leq G$ be a discrete subgroup. The group $\Gamma$ is a **lattice** in $G$ if

$$
\mu(G/\Gamma) < \infty ,
$$

where the quotient is taken with the quotient measure induced by $\mu$, that is, the measure for which

$$
\int_G f(g)\,d\mu(g) = \int_{G/\Gamma}\Bigl(\sum_{\gamma\in\Gamma} f(g\gamma)\Bigr)\,d\mu_{G/\Gamma}(g\Gamma)
$$

for every $f \in C_c(G)$. The number $\operatorname{covol}(\Gamma) = \mu(G/\Gamma)$ is the **covolume** of $\Gamma$; it depends on the normalisation of $\mu$, and the ratio of the covolumes of two lattices in $G$ is well defined. A lattice is **uniform** or **cocompact** if $G/\Gamma$ is compact, and **non-uniform** otherwise.

**Proposition (elementary properties).** Let $\Gamma$ be a lattice in $G$ and let $g \in G$, $H \leq G$.

**(a)** The conjugate $g\Gamma g^{-1}$ is a lattice with the same covolume.

**(b)** A finite-index subgroup of a lattice is a lattice, and a subgroup containing a lattice is a lattice; if $\Gamma' \leq \Gamma$ has index $[\Gamma:\Gamma'] = m$ then $\operatorname{covol}(\Gamma') = m\cdot\operatorname{covol}(\Gamma)$.

**(c)** If $\Gamma$ is uniform then $\Gamma$ is finitely generated, and $G/\Gamma$ is a compact space on which $G$ acts transitively.

**(d)** The **commensurator** $\operatorname{Comm}_G(\Gamma)$, the set of the $g \in G$ for which $g\Gamma g^{-1}$ is commensurable with $\Gamma$, is a subgroup of $G$ containing the normaliser $N_G(\Gamma)$, and if $\Gamma_1, \Gamma_2$ are lattices in $G$ then $\Gamma_1 \cap \Gamma_2$ is a lattice and has finite index in each.

**Proof.** (a) The conjugation restricts to the identity on the quotient: $G/g\Gamma g^{-1} \to G/\Gamma$, $x\,g\Gamma g^{-1} \mapsto xg\Gamma$, is a $G$-equivariant homeomorphism, so the covolumes agree. (b) For a finite-index subgroup the quotient map $G/\Gamma' \to G/\Gamma$ is finite-to-one with fibres of cardinality $m$, and the quotient measure decomposes accordingly, giving $\operatorname{covol}(\Gamma') = m\operatorname{covol}(\Gamma)$; a subgroup containing a lattice contains it with finite index because $G/\Gamma' \to G/\Gamma$ is surjective and $[\Gamma:\Gamma'] = \operatorname{covol}(\Gamma')/\operatorname{covol}(\Gamma)$ by the same formula read in the other direction. (c) In the uniform case $G/\Gamma$ is compact and carries a discrete transitive action with discrete stabilisers; choosing a compact set containing a fundamental domain and using the compactness of the set of relations between the elements meeting it proves finite generation, the standard argument. (d) If $\Gamma_1, \Gamma_2$ are lattices then $\Gamma_1\cap\Gamma_2$ is a lattice — the intersection of two discrete subgroups is discrete, and the finite-measure property follows from the finite measure of $G/\Gamma_1$ together with the fact that the projection $G/(\Gamma_1\cap\Gamma_2) \to G/\Gamma_1$ is finite-to-one on the complement of a null set — and then $[\Gamma_i : \Gamma_1\cap\Gamma_2] = \operatorname{covol}(\Gamma_1\cap\Gamma_2)/\operatorname{covol}(\Gamma_i) < \infty$ by (b). $\square$

### Unimodularity

**Proposition.** If $G$ admits a lattice then $G$ is unimodular.

**Proof.** Let $\Delta_G$ be the modular function of *Locally Compact Groups and Haar Measure*. The measure on $G/\Gamma$ is $G$-invariant, so the left and right Haar measures of $G$ push forward to the same measure on $G/\Gamma$; this forces $\Delta_G(\gamma) = 1$ for $\gamma \in \Gamma$ by the invariance computation, hence $\Delta_G(\Gamma) = 1$. Now $\ker\Delta_G$ is a closed normal subgroup containing $\Gamma$; if it were proper, the fibre bundle $G/\Gamma \to G/\ker\Delta_G$ would have base the non-compact group $G/\ker\Delta_G$ (a closed subgroup of $\mathbb{R}_{>0}$ under the modular function, hence a copy of $\mathbb{R}$ or of $\mathbb{Z}$) and finite-measure fibres, and the base would carry an invariant measure which is infinite for a non-compact group of this kind; then $G/\Gamma$ would have infinite measure. Hence $\Delta_G = 1$ and $G$ is unimodular. $\square$

**Remark.** The proposition is the reason the theory of lattices is developed almost entirely in the unimodular setting, and the reason the covolume is unambiguously defined once a normalisation of the Haar measure is fixed. It also explains why the affine group of *Locally Compact Groups and Haar Measure*, which is not unimodular, admits no lattice: its discrete subgroups of finite covolume would have to lie in the kernel of the modular function, which is the abelian normal subgroup, and there is no discrete subgroup of the required covolume there.

### Uniform and Non-Uniform Lattices

**Theorem (the quotient).** Let $\Gamma$ be a lattice in a unimodular group $G$. Then $G/\Gamma$ is a space of finite measure on which $G$ acts transitively with discrete stabilisers; it is compact exactly when $\Gamma$ is uniform. If $G$ is a Lie group then $G/\Gamma$ is a compact or non-compact **orbifold** of finite volume according as $\Gamma$ is uniform or not, and it is a manifold of dimension $\dim G$ when $\Gamma$ is torsion-free; in the non-uniform case the non-compactness is accounted for by the presence of cusps.

**Proof sketch.** The quotient is homogeneous with stabiliser $\Gamma$ at the identity coset, so the orbit map $G \to G/\Gamma$ factors as a locally trivial fibration with discrete fibres; when $G$ is a Lie group the quotient inherits a manifold structure of dimension $\dim G$ because $\Gamma$ acts properly discontinuously and freely when it is torsion-free, and the finite-volume statement is the definition of the lattice. Non-compactness of finite volume requires a description of the ends; the ends are the cusps, and the description is the reduction theory of the arithmetic case below. The general statement is standard. $\square$

**Example (the elementary case).** The subgroup $\mathbb{Z}^n \leq \mathbb{R}^n$ is a uniform lattice: $\mathbb{R}^n/\mathbb{Z}^n$ is the $n$-torus, compact, with covolume $1$ for the normalised Lebesgue measure. Every lattice in $\mathbb{R}^n$ is of the form $A\mathbb{Z}^n$ for an invertible matrix $A$, and its covolume is $|\det A|$; this is the elementary geometry of numbers, and the finite generation statement is immediate.

## Examples

### Lattices in Nilpotent Groups

**Theorem (Mal'cev).** Let $N$ be a connected simply connected nilpotent Lie group with Lie algebra $\mathfrak{n}$.

**(a)** $N$ admits a lattice if and only if $\mathfrak{n}$ has a rational structure, that is, a basis with respect to which the structure constants are rational.

**(b)** Every lattice in $N$ is uniform, and is finitely generated; $N/\Gamma$ is a compact nilmanifold.

**(c)** a subgroup is a lattice if and only if it is commensurable with the group generated by the exponentials of a $\mathbb{Z}$-form of a rational structure of $\mathfrak{n}$.

**Proof sketch.** (a) A rational structure gives a subgroup $\Gamma$ generated by the exponentials of a lattice in the rational span, and the Baker–Campbell–Hausdorff formula of *The Lie Algebra and the Exponential Map*, whose terms are rational in the structure constants, shows that $\Gamma$ is a subgroup; the quotient is compact by the cocompactness argument below. Conversely a lattice in a nilpotent group determines a rational structure by taking the images of the lattice in the successive quotients of the lower central series, each a lattice in a vector group, and the structure constants are rational with respect to the basis of logarithms. (b) If $\Gamma$ were non-uniform, the ends of $N/\Gamma$ would be cusps, but the lower central series exhaustion shows that a nilpotent group has no non-trivial cusps: the quotient map to the abelianisation is proper on the complement of a compact set, and a finite-covolume subgroup of a vector group is cocompact, so the induction up the central series terminates with compactness. Hence $\Gamma$ is uniform. (c) is the Mal'cev correspondence: it identifies a rational nilpotent Lie algebra with a Lie algebra over $\mathbb{Q}$ and the commensurability class of the lattice with the $\mathbb{Z}$-form. The theorem is Mal'cev's and is quoted as standard. $\square$

**Example (the Heisenberg lattice).** Let $N$ be the Heisenberg group with the presentation of *Topological Groups* or of *Locally Compact Groups and Haar Measure*: $N = \mathbb{R}^3$ with the group law of the Heisenberg group, generated by $X, Y, Z$ with $[X,Y] = Z$ central. The subgroup $\Gamma$ consisting of the elements whose coordinates lie in $\mathbb{Z}$ is a lattice, and $N/\Gamma$ is a compact three-dimensional nilmanifold; the structure constants are rational with respect to the basis $X, Y, Z$, so Mal'cev's theorem applies. The lattice is not abelian (its commutator subgroup is generated by $Z$), and its abelianisation is $\mathbb{Z}^2$.

### Arithmetic Lattices

**Definition.** Let $\mathbf{G}$ be a linear algebraic group defined over $\mathbb{Q}$ and let $G = \mathbf{G}(\mathbb{R})$ be the group of real points, a Lie group when $\mathbf{G}$ is defined over $\mathbb{R}$ and reductive. An **arithmetic subgroup** is a subgroup of $G$ commensurable with the group of integral points $\mathbf{G}(\mathbb{Z}) = \mathbf{G}(\mathbb{Q})\cap GL_n(\mathbb{Z})$ of a faithful representation $\mathbf{G} \hookrightarrow GL_n$ defined over $\mathbb{Q}$.

**Theorem (Borel–Harish-Chandra).** Let $\mathbf{G}$ be a linear algebraic group defined over $\mathbb{Q}$ and let $G = \mathbf{G}(\mathbb{R})$ be the group of real points, with $\mathbf{G}^0$ reductive. Then the arithmetic subgroup $\mathbf{G}(\mathbb{Z})$ is a lattice in $G$. It is uniform if and only if $\mathbf{G}$ has no nontrivial split torus over $\mathbb{Q}$; equivalently, when $G$ is semisimple, if and only if $G$ has no proper parabolic subgroup defined over $\mathbb{Q}$.

**Proof sketch.** The proof is the reduction theory initiated by Hermite, Minkowski and Siegel and completed by Borel and Harish-Chandra. One exhibits a finite set of **Siegel sets** — subsets of $G$ defined by inequalities on the coordinates in a representation, of the form "the first $k$ coefficients bounded below and the remaining ones bounded above" — whose translates by $\Gamma = \mathbf{G}(\mathbb{Z})$ cover $G$, and one shows that each Siegel set has finite Haar measure. The finiteness of the measure uses the growth of the coefficients in the two directions measured by the determinant, which is the arithmetic content of the Hermite–Minkowski theory of *Algebraic Number Theory*; the compactness criterion is that a Siegel set whose parameters are bounded away from the cusp is compact, which happens exactly when there is no rational parabolic subgroup and hence no cusp. The details are the theorem of Borel and Harish-Chandra and are quoted from the literature. $\square$

**Example ($SL_n(\mathbb{Z})$).** The group $SL_n(\mathbb{Z})$ is a lattice in $SL_n(\mathbb{R})$ for every $n \geq 2$. For $n \geq 3$ it is non-uniform: the quotient $SL_n(\mathbb{R})/SL_n(\mathbb{Z})$ is non-compact, with one cusp described by the rational points of the projective space, and its finite volume is the content of the Siegel set estimate. The group $SL_2(\mathbb{Z})$ is also a non-uniform lattice in $SL_2(\mathbb{R})$; the quotient is the modular surface, of finite volume, with one cusp, and it is the classical example of the modular curve as a quotient of the upper half-plane by the modular group. For the symplectic groups, $Sp_{2n}(\mathbb{Z})$ is a lattice in $Sp_{2n}(\mathbb{R})$, non-uniform for $n \geq 1$; for the orthogonal groups the arithmetic subgroups of the associated quadratic forms give lattices in $SO(p,q)$, and supplies the classical groups themselves.

**Example ($S$-arithmetic lattices and Dedekind domains).** The construction generalises: for a number field $k$ with ring of integers $\mathcal{O}_k$ and a finite set $S$ of places containing the archimedean ones, the group $\mathbf{G}(\mathcal{O}_k[S^{-1}])$ is a lattice in $\prod_{v\in S} \mathbf{G}(k_v)$. The product is a locally compact group, and the lattice is arithmetic in the wider sense; the theory uses the adelic and local fields of *Algebraic Number Theory* in Part I, and the lattices obtained are the **$S$-arithmetic** lattices. For $k=\mathbb{Q}(\sqrt{-d})$ imaginary quadratic with ring of integers $\mathcal{O}_d$ and $S$ the set of archimedean places, the group $PSL_2(\mathcal{O}_d)$ is the **Bianchi group**, a non-uniform arithmetic lattice in $PSL_2(\mathbb{C})$, and these are the standard non-uniform lattices in a rank-one group.

### Rank-One Lattices

**Example (the modular group and hyperbolic surfaces).** The group $PSL_2(\mathbb{R})$ acts on the upper half-plane $\mathbf{H}^2 = \{z \in \mathbb{C}: \operatorname{Im}z > 0\}$ by $z \mapsto (az+b)/(cz+d)$, and the action is transitive with stabiliser $SO(2)$ at $i$. The quotient $PSL_2(\mathbb{R})/PSL_2(\mathbb{Z})$ is the modular surface, of finite volume, non-compact, and the lattice $PSL_2(\mathbb{Z})$ is non-uniform. Every lattice in $PSL_2(\mathbb{R})$ gives a hyperbolic surface of finite area, and a uniform lattice gives a compact hyperbolic surface, that is, a closed surface of genus $g \geq 2$ with a hyperbolic metric; this is the beginning of the relation between lattices and hyperbolic manifolds which develops from the geometric side.

**Example (lattices in $SO(n,1)$ and hyperbolic manifolds).** Let $G = SO(n,1)$ and let $\mathbf{H}^n$ be the hyperbolic $n$-space, the symmetric space of $G$: it is the homogeneous space $SO(n,1)/SO(n)$, and it carries a $G$-invariant proper distance. A uniform lattice in $SO(n,1)$ acts properly discontinuously and cocompactly on $\mathbf{H}^n$ with compact quotient, so it is the fundamental group of a closed hyperbolic $n$-manifold; a non-uniform lattice gives a finite-volume hyperbolic manifold with cusps. For $n = 3$ the two families are the closed and the cusped hyperbolic three-manifolds. The construction identifies the lattices in $SO(n,1)$ up to conjugacy with the hyperbolic structures of finite volume on a manifold of dimension $n$, and Mostow rigidity below then says that the structure is unique.

**Example (lattices in $SU(n,1)$ and complex hyperbolic space).** The same construction applies to $G = SU(n,1)$ acting on the complex hyperbolic space $SU(n,1)/S(U(n)\times U(1))$, a negatively curved symmetric space; the lattices give complex hyperbolic manifolds of finite volume. The rank-one groups $SO(n,1)$, $SU(n,1)$, $Sp(n,1)$ and $F_4^{-20}$ exhaust the simple real Lie groups of real rank one with finite centre, and the lattices in them are the rank-one lattices; they do not have property (T), as recorded in *Property (T)*, and the rigidity phenomena in this case are those of Mostow rather than those of Margulis.

## Rigidity

### Mostow Rigidity

**Theorem (Mostow–Prasad).** Let $G$ and $G'$ be connected semisimple Lie groups with trivial centre and no compact factors, with $G$ not locally isomorphic to $SL_2(\mathbb{R})$, and let $\Gamma \leq G$, $\Gamma' \leq G'$ be **irreducible** lattices. Then every isomorphism $\Gamma \to \Gamma'$ extends to an isomorphism $G \to G'$; in particular an irreducible lattice in such a $G$ determines $G$ and the embedding up to isomorphism. For a reducible lattice the same conclusion holds factor by factor, an isomorphism of lattices extending after a permutation of the factors of $G$; consequently:

**(a)** a closed hyperbolic manifold of dimension $n \geq 3$ has a unique hyperbolic structure up to isometry, and its fundamental group determines it up to isometry;

**(b)** the deformation space of a lattice in a higher-rank semisimple Lie group is a single point.

**Proof sketch.** The proof compares the two actions of the lattices on the symmetric spaces. The isomorphism $\Gamma \to \Gamma'$ gives a quasi-isometry of the symmetric spaces and hence an equivariant map of the boundaries at infinity — the boundary is the Furstenberg boundary, a flag manifold of the group; the boundary map is shown to be a homeomorphism preserving the flag structure, and then the fundamental theorem of projective geometry — a bijection of flag manifolds preserving incidence is induced by a linear map — produces an isomorphism of the algebraic groups defined over $\mathbb{R}$ which restricts to the given isomorphism. The ergodicity of the boundary action, which is the step that uses the measure theory, is treated in Part III. The theorem is Mostow's, extended by Prasad to the semisimple case; it is quoted as standard. $\square$

**Remark.** The hypothesis $G \not\cong SL_2(\mathbb{R})$ up to local isomorphism is essential: lattices in $PSL_2(\mathbb{R})$ have a deformation space of dimension $6g-6$ for a uniform lattice of genus $g$, the Teichmüller space, and the rigidity fails. The rank-one groups $SO(n,1)$ for $n \geq 3$ do satisfy the hypotheses of the theorem for $n \geq 3$ — this is Mostow's original case, since $SO(n,1)$ is not locally isomorphic to $SL_2(\mathbb{R})$ for $n \geq 3$ — and this is why hyperbolic manifolds of dimension at least three have unique structures while surfaces do not. The result is often stated as: rigidity holds in dimensions $\geq 3$ and fails in dimension $2$.

### The Borel Density Theorem

**Theorem (Borel density).** Let $G$ be a connected semisimple Lie group with no compact factors and let $\Gamma \leq G$ be a lattice. Then $\Gamma$ is **Zariski dense** in $G$: in a faithful representation $G \hookrightarrow GL_n(\mathbb{R})$, the Zariski closure of $\Gamma$ — its closure for the topology whose closed sets are the zero sets of polynomials, a linear algebraic group being a subgroup of $GL_n$ defined by polynomial equations — is the whole of $G$, that is, $\Gamma$ is contained in no proper algebraic subgroup of $G$.

**Proof sketch.** The proof uses the dynamics of the action of $\Gamma$ on the flag manifolds of $G$. A lattice is **ergodic** on $G/P$ for every parabolic subgroup $P$, which follows from the finite measure of $G/\Gamma$ and the fact that $G$ acts transitively on $G/P \times G/\Gamma$ (the point is that the orbit of a pair is the whole product space, by a transitivity computation in the semisimple group); the ergodicity of the action is the measure-theoretic input, treated in Part III. If $\Gamma$ were contained in a proper algebraic subgroup, the orbit structure of $\Gamma$ on a suitable flag manifold would be confined to an orbit of the algebraic subgroup, contradicting ergodicity. The theorem is Borel's and is quoted as standard. $\square$

**Corollary.** A lattice in a connected semisimple Lie group $G$ with trivial centre and no compact factors has trivial centre; and if $G$ is simple, every closed subgroup $H$ with $\Gamma \leq H \leq G$ is either discrete or equal to $G$. In particular a lattice is infinite and is contained in no proper closed subgroup of positive dimension when $G$ is simple.

**Proof.** If $z$ is central in $\Gamma$ then $z$ commutes with $\Gamma$, hence lies in the centraliser of $\Gamma$ in $GL_n(\mathbb{R})$; that centraliser is an algebraic subgroup containing $\Gamma$, so by Zariski density it contains $G$, and $z \in G$ commutes with $G$: hence $z \in Z(G) = \{1\}$ and the centre of $\Gamma$ is trivial. For the second statement, $H$ has finite covolume in $G$ because it contains the lattice, and a closed subgroup of finite covolume in a simple group is either discrete or all of $G$; the standard argument shows that a non-discrete closed subgroup of finite covolume in a simple Lie group contains a one-parameter subgroup, and the finite-covolume condition then forces $H$ to be normal and hence all of $G$. $\square$

### Finiteness of Lattices of Bounded Covolume

**Theorem (Kazhdan–Margulis).** Let $G$ be a connected semisimple Lie group with no compact factors and with all simple factors of real rank at least two, and let $V > 0$. Then there are only finitely many conjugacy classes of lattices in $G$ of covolume at most $V$. For a group of real rank one the analogous statement is false, and it fails even for a fixed covolume: in $PSL_2(\mathbb{R})$ the uniform lattices of a given covolume correspond to the hyperbolic structures on a closed surface of genus $g \geq 2$, which form the $(6g-6)$-dimensional Teichmüller space, a continuum of pairwise non-conjugate lattices; in $SO(3,1)$ there are in addition infinitely many conjugacy classes of bounded covolume, given by the hyperbolic three-manifolds obtained by Dehn surgery on a fixed cusped manifold.

**Proof sketch.** For the higher-rank case the proof uses property (T): the covolume of a lattice controls the size of its generating set by the Kazhdan constant, and the arithmeticity theorem of Margulis identifies the higher-rank lattices with the arithmetic ones, so the finiteness reduces to a finiteness for arithmetic data, which is the theorem of Borel and Harish-Chandra on the finiteness of arithmetic subgroups with bounded covolume. The rank-one counterexamples come from the deformation and surgery constructions. The theorem is quoted as standard; the identification of the higher-rank lattices with arithmetic ones is not covered here. $\square$

**Theorem (Margulis arithmeticity).** Let $G$ be a connected semisimple Lie group with no compact factors, all of whose simple factors have real rank at least two, and let $\Gamma \leq G$ be an irreducible lattice. Then $\Gamma$ is **arithmetic**: there are a number field $k$, a linear algebraic $k$-group $\mathbf{H}$ and a finite set $S$ of places of $k$ containing the archimedean ones such that $\prod_{v\in S}\mathbf{H}(k_v)$ is isomorphic to $G$ up to a compact central factor and $\Gamma$ is commensurable with $\mathbf{H}(\mathcal{O}_k[S^{-1}])$. This is the arithmeticity theorem of Margulis, proved from the superrigidity theorem; the finiteness theorem of Wang, that a semisimple group with no rank-one factors has only finitely many conjugacy classes of lattices of covolume at most $V$, is proved by the same circle of ideas, and the arithmetic description of the lattices is the input .

**Example (deformation in rank one).** In $PSL_2(\mathbb{R})$ the lattices are the fundamental groups of hyperbolic surfaces of finite area, and the deformation space of the structure is the Teichmüller space, of dimension $6g-6$ for a closed surface of genus $g$; this is why the finiteness of lattices of bounded covolume fails in rank one and why Mostow rigidity is the best possible statement. The example is the boundary case of the rigidity theory, and develops the geometric side.

## Lattices and Property (T)

**Theorem.** Let $G$ be a locally compact group with property (T) and let $\Gamma \leq G$ be a lattice. Then $\Gamma$ has property (T).

**Proof.** This is the heredity of property (T) from a group to its finite-covolume subgroups, proved in *Property (T)*: the induced representation of a representation with almost invariant vectors has almost invariant vectors, hence an invariant vector, and a $G$-invariant vector of the induced representation is a constant function whose value is $\Gamma$-invariant. $\square$

**Corollary (Kazhdan's original application).** Every lattice in a connected semisimple Lie group with all simple factors of real rank at least two is finitely generated; in particular $SL_n(\mathbb{Z})$ is finitely generated for $n \geq 3$, and the same holds for the arithmetic lattices in the higher-rank groups. The finite generation is used in the proof of the arithmeticity theorem and in the construction of expanders from a lattice by reduction modulo $p$.

**Remark.** The two heredity results about lattices — from $G$ to $\Gamma$ for property (T), and the finiteness of the abelianisation that follows — are the structural form of the intuition that a lattice in a higher-rank group is a rigid object: it has no homomorphism onto $\mathbb{Z}$, its finite quotients are controlled, and its geometry is that of the ambient group.

## The Boundary with Analysis

- The **ergodicity** of a lattice acting on $G/\Gamma$ and on the flag manifolds $G/P$, the **mixing and equidistribution** of the geodesic flow, the classification of invariant measures by Ratner's theorems and the **counting of rational points** are.
- The **computation of covolumes** by integration against the Haar measure, the explicit volume formulas for arithmetic quotients (the Tamagawa number), the **trace formula** and the spectral theory of the Laplacian on $G/\Gamma$ are Part III.
- The **symmetric spaces** and the Riemannian geometry of the quotients are developed ; the article uses only a $G$-invariant proper distance on a homogeneous space.
- The **arithmetic and adelic** constructions are the subject with this one; the number theory used at the level of statements is that of *Algebraic Number Theory* in Part I.
- What is *not* deferred: the definition and elementary properties of lattices, unimodularity and covolume, Mal'cev's theorem for nilpotent groups, the Borel–Harish-Chandra existence theorem at the level of statement, Mostow rigidity, the Borel density theorem and the Kazhdan–Margulis finiteness.

## Summary

A lattice in a locally compact group $G$ is a discrete subgroup $\Gamma$ with $G/\Gamma$ of finite invariant measure; it is uniform when the quotient is compact. The covolume is the quotient measure, defined up to the normalisation of the Haar measure; conjugates have the same covolume, finite-index subgroups have covolume multiplied by the index, and a group admitting a lattice is unimodular. Lattices in a connected simply connected nilpotent Lie group exist exactly when the Lie algebra has a rational structure and are always uniform: this is Mal'cev's theorem, and the Heisenberg group with its integer points is the model example. Arithmetic subgroups of reductive groups over $\mathbb{Q}$ are lattices by the theorem of Borel and Harish-Chandra, and they are uniform exactly when the group has no proper parabolic subgroup over $\mathbb{Q}$, so that there are no cusps.

The rigidity theory is the structural heart of the subject. Mostow–Prasad rigidity says that an isomorphism of lattices in semisimple groups with trivial centre, no compact factors and not locally isomorphic to $SL_2(\mathbb{R})$ extends to an isomorphism of the groups; so a closed hyperbolic manifold of dimension at least three has a unique hyperbolic structure, while in dimension two the Teichmüller deformation space is non-trivial. The Borel density theorem says that a lattice in a semisimple group without compact factors is Zariski dense. The Kazhdan–Margulis theorem and the arithmeticity theorem of Margulis say that in real rank at least two the lattices of bounded covolume fall into finitely many conjugacy classes and are arithmetic; both use property (T), which a lattice inherits from its ambient group, and which gives Kazhdan's original finite-generation theorem for higher-rank lattices. The ergodic, spectral and dynamical consequences belong to Part III, and the arithmetic theory .

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G$, $\Gamma$ | Locally compact group; lattice (discrete subgroup of finite covolume) |
| $\mu$, $\mu_{G/\Gamma}$ | Left Haar measure on $G$; quotient measure on $G/\Gamma$ |
| $\operatorname{covol}(\Gamma) = \mu(G/\Gamma)$ | Covolume, defined up to normalisation of $\mu$ |
| uniform (cocompact) lattice | $G/\Gamma$ compact |
| non-uniform lattice | $G/\Gamma$ non-compact but of finite measure; cusps |
| $\Delta_G$ | Modular function; $G$ admitting a lattice is unimodular |
| $N_G(\Gamma)$ | Normaliser; lattices are commensurated by their normalisers |
| $\mathbb{Z}^n \leq \mathbb{R}^n$ | The elementary uniform lattice; covolume $|\det A|$ for $A\mathbb{Z}^n$ |
| nilmanifold | $N/\Gamma$ for a lattice in a nilpotent Lie group |
| $\mathbf{G}(\mathbb{Z})$ | Arithmetic subgroup of a $\mathbb{Q}$-group; a lattice by Borel–Harish-Chandra |
| $SL_n(\mathbb{Z}) \leq SL_n(\mathbb{R})$ | Standard non-uniform lattice for $n \geq 2$ |
| Siegel set | Subset of $G$ with finite Haar measure used in reduction theory |
| $SO(n,1)/SO(n) = \mathbf{H}^n$ | Hyperbolic $n$-space as a homogeneous space with a proper distance |
| rank-one lattice | Lattice in $SO(n,1)$, $SU(n,1)$, $Sp(n,1)$ or $F_4^{-20}$ |
| Mostow–Prasad rigidity | Isomorphisms of lattices extend to isomorphisms of the ambient groups |
| Zariski density | Borel density theorem: a lattice is Zariski dense |
| Kazhdan–Margulis | Finitely many lattices of bounded covolume in real rank $\geq 2$ |
| $\operatorname{covol}$ scaling | $\operatorname{covol}(\Gamma') = [\Gamma:\Gamma']\operatorname{covol}(\Gamma)$ for $\Gamma' \leq \Gamma$ |
| $S$-arithmetic lattice | Lattice of the form $\mathbf{G}(\mathcal{O}_k[S^{-1}])$ in a product of local groups |





## Further Reading

- Armand Borel, *Introduction aux groupes arithmétiques* (Hermann, 1969), for the Borel–Harish-Chandra theorem and reduction theory.
- Armand Borel and Harish-Chandra, *Arithmetic subgroups of algebraic groups*, Annals of Mathematics 75 (1962), 485–535, for the existence theorem and the compactness criterion.
- G. D. Mostow, *Strong Rigidity of Locally Symmetric Spaces* (Princeton University Press, 1973), for Mostow rigidity and its proof.
- Gopal Prasad, *Strong rigidity of $\mathbb{Q}$-rank 1 lattices*, Inventiones Mathematicae 21 (1973), 255–286, for the extension of Mostow rigidity to the semisimple case.
- Gregory Margulis, *Discrete Subgroups of Semisimple Lie Groups* (Springer, 1991), for superrigidity, arithmeticity and the finiteness theorems.
- Armand Borel, *Density properties for certain subgroups of semi-simple groups without compact components*, Annals of Mathematics 72 (1960), 179–188, for the Borel density theorem.
- David A. Kazhdan and Gregory A. Margulis, *A proof of Selberg's hypothesis*, Matematicheskii Sbornik 75 (1968), 163–168, for the finiteness of lattices of bounded covolume.
- A. I. Mal'cev, *On a class of homogeneous spaces*, American Mathematical Society Translations 39 (1951), for the nilpotent case and rational structures.
- M. S. Raghunathan, *Discrete Subgroups of Lie Groups* (Springer, 1972), for the systematic account of lattices, covolumes and reduction theory.
- Yves Benoist, *Five lectures on lattices in semisimple Lie groups*, in Géométries à courbure négative ou nulle (Soc. Math. France, 2009), for a modern survey of the rigidity theory.
