
# __Classifying Spaces and Cohomology Operations__

## Introduction

Two constructions organise the cohomology of a space with coefficients in a group or a field. The first linearises the data of a group action: every topological group $G$ has a **classifying space** $BG$, the base of a principal $G$-bundle $EG \to BG$ whose total space is contractible, and the homotopy classes of maps into $BG$ are exactly the principal $G$-bundles over a space. The second linearises the operations available on cohomology itself: the **Steenrod squares** $\mathrm{Sq}^i$ and the **Steenrod powers** $P^i$ are natural transformations that raise degree, they satisfy the **Adem relations**, and they generate the graded algebra $\mathcal{A}_p$ that acts on the mod $p$ cohomology of every space. The two are the same subject seen from two sides: a natural transformation of cohomology functors is a cohomology class of an Eilenberg–MacLane space, and the Eilenberg–MacLane spaces are the classifying spaces of the coefficient groups.

The article develops the principal bundles and the classifying property, the Milnor join and the bar construction of $EG \to BG$, the functoriality and the homotopy characterisation of $BG$ up to weak homotopy equivalence, the standard cases for a discrete group, for a compact Lie group and for the classical groups, the Eilenberg–MacLane spaces $K(\pi,n)$ with the representability of singular cohomology, and the cohomology operations with the Steenrod squares and powers, the Adem relations and the Steenrod algebra. The homotopy-theoretic input is that of *Homotopy Groups and Fibrations*, directly above this article: the higher homotopy groups, the long exact sequence of a fibration and the Hurewicz theorem are used as they stand there and are not re-derived. The cohomological input is that of *Cohomology and the Universal Coefficient Theorem* and of *Cup and Cap Products* of this Part, the principal-bundle input is that of *Fibre Bundles, Connections and Curvature*, and the theory of a group acting on a space, together with group cohomology and the bar resolution, is that of *Group Cohomology* of Part I.

One object of the corpus is named and not used: the **characteristic classes** of a vector bundle are the subject of *Characteristic Classes*, and the relation of the Steenrod operations to them — the Wu formula expresses the Stiefel–Whitney classes of a manifold through the squares of its cohomology classes — is stated here only as the reason the operations matter, without developing the theory. The applications of the classifying space to the differential and to the filtration of a fibration lie outside this article, and so does the stable refinement of the Steenrod algebra.

Throughout, $G$ denotes a topological group, $H$ a discrete group when the context is group cohomology, $X$ and $Y$ are CW complexes unless stated otherwise, $[X,Y]$ is the set of homotopy classes of maps, $\pi_n$ is the $n$-th homotopy group, and $H^n(-;\pi)$ is singular cohomology with coefficients in the abelian group $\pi$. The symbols $BG$, $EG$ and $K(\pi,n)$, fixed in the shared notation of the corpus, mean the classifying space, its contractible total space and the Eilenberg–MacLane space. Coefficients in a field are written $\mathbb{F}_p = \mathbb{Z}/p\mathbb{Z}$.

## Principal Bundles and the Classifying Property

### Principal Bundles

**Definition.** Let $G$ be a topological group. A **principal $G$-bundle** over a space $B$ is a map $p : P \to B$ with a right action of $G$ on $P$ preserving the fibres, such that each fibre is a free orbit of $G$ and $B$ is covered by open sets $U$ for which there is a $G$-equivariant homeomorphism $p^{-1}(U) \cong U \times G$ over $U$, the action on the right being by multiplication on $G$. A **morphism** of principal $G$-bundles is a $G$-equivariant map over $B$; the **pullback** $f^*P$ of $P$ along a map $f : X \to B$ is the bundle whose fibre over $x$ is the fibre of $P$ over $f(x)$, with the evident $G$-action. Two bundles over $B$ are **isomorphic** if a morphism between them is a homeomorphism, and the set of isomorphism classes of principal $G$-bundles over $X$ is written $\operatorname{Prin}_G(X)$.

**Example.** The trivial bundle is $X \times G \to X$ with the action on the second factor. For $G = U(1)$ the associated bundle of a principal $G$-bundle via the standard representation on $\mathbb{C}$ is a complex line bundle, and the passage between the two is the standard dictionary which makes the first Chern class of a line bundle a degree-two class of the base; the differentiable theory of a principal connection on such a bundle is that of *Fibre Bundles, Connections and Curvature*.

### The Classifying Property

**Definition.** Let $G$ be a topological group. A **universal principal $G$-bundle** is a principal $G$-bundle $p : EG \to BG$ with $EG$ weakly contractible, that is, with $\pi_n(EG) = 0$ for all $n \geq 0$. The base $BG$ is the **classifying space** of $G$.

**Theorem (classifying property).** Let $p : EG \to BG$ be a universal principal $G$-bundle and let $X$ be a CW complex. The pullback of $p$ along a map $f : X \to BG$ defines a natural bijection

$$
[X, BG] \xrightarrow{\ \cong\ } \operatorname{Prin}_G(X), \qquad [f] \mapsto f^*EG .
$$

The trivial bundle corresponds to the class of a constant map, so the bijection is between pointed data when a basepoint is fixed.

*Proof sketch.* The map is well defined on homotopy classes because a homotopy $F : X \times I \to BG$ pulls the bundle back to a principal bundle over $X\times I$, whose restrictions to $X \times \{0\}$ and $X \times \{1\}$ are isomorphic by the homotopy invariance of fibre bundles over a product with $I$. For surjectivity, let $P \to X$ be a principal $G$-bundle; the associated bundle $P \times_G EG \to X$ has fibre $EG$ and total space $P\times_G EG$, which strongly deformation retracts onto a copy of $P$ because $EG$ is contractible, so the bundle $P$ is the pullback of $p$ along the classifying map of a section of $P\times_G EG \to X$; the section is constructed by the homotopy lifting property of the fibration $P \times_G EG \to X$, which has contractible fibres. For injectivity, two maps pulling $p$ back to isomorphic bundles differ by a homotopy, constructed again by lifting the isomorphism over $X \times I$ through the fibration with contractible fibre. $\square$

**Remark.** The theorem is the exact sense in which $BG$ classifies the group $G$: it converts the geometric problem of principal bundles into the homotopy problem of maps into one space, and it makes $\operatorname{Prin}_G$ a representable functor on the homotopy category of CW complexes.

## Constructions of the Universal Bundle

### The Milnor Join

**Definition.** The **join** of spaces $X_1,\ldots,X_n$ is the quotient of the set of formal sums $\sum_{i=1}^n t_i x_i$ with $t_i \geq 0$, $\sum_i t_i = 1$, $x_i \in X_i$, by the relation that terms with $t_i = 0$ are omitted; it is written $X_1 * \cdots * X_n$. For a topological group $G$ the $n$-fold join $G^{*n}$ carries the diagonal right action $\left(\sum_i t_i g_i\right)\cdot g = \sum_i t_i (g_i g)$.

**Theorem (Milnor).** Let $G$ be a topological group and let $EG = \operatorname{colim}_n G^{*n}$ be the colimit of the joins along the maps $G^{*n} \to G^{*n+1}$, $x \mapsto x * e$ with $e$ the identity. Then the diagonal action of $G$ on $EG$ is free, $EG$ is weakly contractible, and

$$
BG = EG/G
$$

with $EG \to BG$ a principal $G$-bundle. The bundle so obtained is universal.

*Proof.* The action is free: if $\sum_i t_i g_i g = \sum_i t_i g_i$ as points of the join and the representations are reduced, then $g_i g = g_i$ for every index $i$ with $t_i > 0$, and such an index exists, so $g = 1$. For weak contractibility one uses the standard connectivity of the join. The join of two nonempty spaces is connected, and if $X$ and $Y$ are connected and nonempty then $X*Y$ is simply connected: it is the union of $CX \times Y$ and $X \times CY$, whose intersection is $X \times Y$, and van Kampen's theorem presents $\pi_1(X*Y)$ as the amalgamated product of $\pi_1(Y)$ and $\pi_1(X)$ over $\pi_1(X)\times\pi_1(Y)$, in which the map onto one of the two vertex groups is surjective, so the amalgam is trivial. By the standard formula $\mathrm{conn}(X*Y) = \mathrm{conn}(X) + \mathrm{conn}(Y) + 2$ the join of $r$ nonempty spaces is at least $(r-2)$-connected, so $\pi_k(G^{*n}) = 0$ for $n \geq k+3$, and since every class in $\pi_k(EG)$ is represented at some finite stage of the colimit, every homotopy group of $EG$ is killed at a finite stage and $EG$ has trivial homotopy in every degree. The quotient map $EG \to EG/G$ is a principal $G$-bundle: the action is free, and the reduced representation of a point of a join, in which one coordinate is nonzero at a chosen index, gives a slice on which the action is a product with $G$; the local trivialisations of the colimit are assembled from these. $\square$

**Remark.** The construction is concrete at every stage and the colimit is only used to kill the higher homotopy groups one at a time; this is why $EG$ can be taken to be a CW complex when $G$ is one, a point used in the computations below. For a product of groups the product $EG \times EH$ is contractible and carries a free action of $G\times H$ with quotient $BG\times BH$, so it is a universal principal $(G\times H)$-bundle and $B(G\times H)$ is homotopy equivalent to $BG\times BH$.

### The Bar Construction

**Definition.** Let $G$ be a topological group. The **bar construction** is the simplicial space $B_\bullet G$ with $B_n G = G^n$ and face maps

$$
\partial_i (g_1,\ldots,g_n) = \begin{cases} (g_2,\ldots,g_n), & i = 0,\\ (g_1,\ldots,g_{i}g_{i+1},\ldots,g_n), & 1 \leq i \leq n-1,\\ (g_1,\ldots,g_{n-1}), & i = n,\end{cases}
$$

and degeneracies inserting the identity. Its geometric realisation is written $BG = |B_\bullet G|$; the same construction applied to the free $G$-set $G$ gives the simplicial space $E_\bullet G$ with $E_nG = G^{n+1}$, whose realisation $EG = |E_\bullet G|$ carries a free right action of $G$ with quotient $BG$.

**Theorem.** For every topological group $G$ the realisation $EG$ is weakly contractible, the action of $G$ is free, and $EG \to BG$ is a universal principal $G$-bundle. For a discrete group $H$ the space $BH$ is a CW complex with one $n$-cell for each element of $H^n$, and its homology and cohomology are the group homology and cohomology:

$$
H_n(BH;\mathbb{Z}) \cong H_n(H;\mathbb{Z}), \qquad H^n(BH;M) \cong H^n(H;M),
$$

for every $H$-module $M$. Consequently $BH$ is the Eilenberg–MacLane space $K(H,1)$.

*Proof sketch.* The realisation $E_\bullet G$ has an extra degeneracy, given by inserting the identity in the last coordinate, and a simplicial space with an extra degeneracy has contractible realisation; the freeness is the freeness of the action on each $G^{n+1}$ and the quotient identifies $E_\bullet G/G$ with $B_\bullet G$. For discrete $H$ the realisation is a CW complex whose $n$-cells are the nondegenerate simplices, indexed by $H^n$, and the chain complex of $B_\bullet H$ is the bar resolution; its homology computes $\operatorname{Tor}$ over $\mathbb{Z}H$, and its cohomology computes $\operatorname{Ext}$, which is group cohomology as developed in *Group Cohomology*. The last statement is the characterisation of $K(H,1)$ by its homotopy groups, established below. $\square$

**Remark.** Both constructions produce the same space up to homotopy equivalence; the Milnor join is the geometric model and the bar construction is the algebraic one, and it is the bar construction that exhibits $BH$ as the classifying space of a discrete group in the form in which group cohomology is computed. The description of $H^n(H;M)$ as the cohomology of $BH$ is used aga.

### Functoriality

**Theorem.** A continuous homomorphism $\varphi : G \to H$ induces maps $E\varphi : EG \to EH$ and $B\varphi : BG \to BH$, well defined up to homotopy, and $B\varphi$ classifies the extension of structure group: for a principal $G$-bundle $P$ over $X$, the bundle $P\times_G H$ obtained by the action $g\cdot h = \varphi(g)h$ corresponds under the classifying bijection to the composition $B\varphi \circ f$ with the classifying map $f$ of $P$. A homomorphism homotopic to $\varphi$ induces a homotopic map, so $B$ is a functor on the homotopy category of topological groups and continuous homomorphisms.

*Proof sketch.* The map on the bar construction is induced levelwise, $B_n\varphi(g_1,\ldots,g_n) = (\varphi g_1,\ldots,\varphi g_n)$, on the simplices, and the realisation is functorial; the homotopy invariance follows because a homotopy of homomorphisms gives a simplicial homotopy. The identification of the associated bundle with the composite is the naturality of the classifying bijection, since $P \times_G H$ is the pullback of $EH$ by the same argument that identifies $P$ with the pullback of $EG$. $\square$

**Corollary.** The constructions are products and coproducts in the expected way: $B(G\times H)$ is homotopy equivalent to $BG \times BH$, and for a discrete group $H$ the classifying space of the free product is homotopy equivalent to the wedge, $B(H_1 * H_2) \simeq BH_1 \vee BH_2$. In particular $B\mathbb{Z} = S^1$ up to homotopy equivalence, since $S^1$ has contractible universal cover $\mathbb{R}$, and $B(\mathbb{Z}/n\mathbb{Z})$ is the infinite lens space $L^\infty_n = S^\infty/(\mathbb{Z}/n\mathbb{Z})$.

## The Homotopy Characterisation

### Uniqueness of the Universal Bundle

**Theorem.** Let $G$ be a topological group. Any two universal principal $G$-bundles $EG \to BG$ and $E'G \to B'G$ are isomorphic as bundles after a homotopy equivalence $EG \to E'G$; equivalently, $BG$ and $B'G$ are weakly homotopy equivalent, and homotopy equivalent when both are CW complexes.

*Proof.* Choose CW models and argue symmetrically in the two directions. Let $X$ be a CW complex weakly equivalent to $BG$ and let $P$ be the pullback of $EG$ along the weak equivalence $X \to BG$; by the classifying property for $E'G \to B'G$ there is a map $f : X \to B'G$ with $P \cong f^*E'G$, and a bundle map $P \to E'G$ over $f$. That bundle map induces a weak equivalence on the total spaces, because both $EG$ and $E'G$ are weakly contractible, so $f$ induces isomorphisms on all homotopy groups and is a weak equivalence. The construction is symmetric, and the two composites fix the pullback of the universal bundles up to isomorphism, hence are homotopic by the injectivity part of the classifying property. $\square$

**Corollary.** The classifying space $BG$ is determined by $G$ up to weak homotopy equivalence, so any homotopy invariant of $BG$ is an invariant of $G$; a homomorphism inducing a weak equivalence of classifying spaces is a homotopy equivalence when $BG$ and $BH$ are CW complexes.

### The Path–Loop Fibration

**Theorem.** Let $G$ be a topological group and $p : EG \to BG$ its universal bundle. Then

$$
\pi_n(BG) \cong \pi_{n-1}(G) \quad (n \geq 2), \qquad \pi_1(BG) \cong \pi_0(G),
$$

and consequently $BG$ is simply connected whenever $G$ is connected, and $B$ kills one homotopy degree: $\pi_n(BG)$ is the $(n-1)$-st homotopy group of $G$.

*Proof.* The map $p$ is a fibration with fibre $G$, since a principal bundle is locally trivial and a locally trivial map over a paracompact base is a fibration, and the fibre sequence $G \to EG \to BG$ gives the long exact sequence

$$
\cdots \to \pi_n(G) \to \pi_n(EG) \to \pi_n(BG) \to \pi_{n-1}(G) \to \pi_{n-1}(EG) \to \cdots
$$

of *Homotopy Groups and Fibrations*. Every group in the middle vanishes because $EG$ is weakly contractible, so every connecting map is an isomorphism where both neighbouring terms vanish, which gives the displayed identifications; for $n = 1$ the sequence ends $\pi_0(EG) \to \pi_0(BG) \to \pi_0(G) \to \pi_0(EG)$, reading $\pi_1(BG)$ when basepoints are fixed. $\square$

**Example.** For $G = U(1)$ the group is connected with $\pi_1(U(1)) = \mathbb{Z}$ and $\pi_n(U(1)) = 0$ for $n \geq 2$, so $BU(1)$ has $\pi_2 = \mathbb{Z}$ and all other homotopy groups trivial; it is therefore $K(\mathbb{Z},2)$, and indeed $BU(1) = \mathbb{CP}^\infty$. For $G = \mathbb{Z}/2\mathbb{Z}$ discrete one has $\pi_0(G) = \mathbb{Z}/2\mathbb{Z}$, so $B(\mathbb{Z}/2\mathbb{Z})$ has fundamental group $\mathbb{Z}/2\mathbb{Z}$ and no higher homotopy, that is, $B(\mathbb{Z}/2\mathbb{Z}) = K(\mathbb{Z}/2\mathbb{Z},1) = \mathbb{RP}^\infty$.

## The Standard Cases

### Discrete Groups and $K(G,1)$

**Theorem.** Let $H$ be a discrete group. Then $BH$ is a $K(H,1)$: it has fundamental group $H$ and trivial higher homotopy groups, and its universal cover is $EH$, which is contractible. Conversely every $K(H,1)$ is a classifying space for $H$. A connected CW complex $X$ with $\pi_1(X) = H$ and $\pi_n(X) = 0$ for $n \geq 2$ is therefore a $BH$, so it classifies the principal $H$-bundles over every CW complex.

*Proof.* The path–loop theorem gives $\pi_1(BH) \cong \pi_0(H) = H$ and $\pi_n(BH) \cong \pi_{n-1}(H) = 0$ for $n \geq 2$; the universal cover of $BH$ is $EH$ because the fibre of $BH \to K(H,1)$ is discrete and $EH$ is contractible. The converse is the uniqueness of $K(H,1)$. $\square$

**Example.** The following are the standard examples of classifying spaces of discrete groups, all of them aspherical, meaning that the universal cover is contractible:

| Group $H$ | $BH$ | Reason |
|---|---|---|
| $1$ | a point | nothing to classify |
| $\mathbb{Z}$ | $S^1$ | $\mathbb{R}$ is the contractible universal cover |
| $\mathbb{Z}/n\mathbb{Z}$ | $L^\infty_n = S^\infty/(\mathbb{Z}/n)$ | $S^\infty$ is contractible, the action is free |
| $\mathbb{Z}^n$ | $T^n$ | $\mathbb{R}^n$ is the universal cover |
| free group $F_r$ | wedge of $r$ circles | the tree is the contractible universal cover |
| $\pi_1(\Sigma_g)$, $g \geq 2$ | the closed surface $\Sigma_g$ | the hyperbolic plane is the contractible universal cover |

The surfaces of genus $g \geq 1$ and the wedges of circles illustrate the general principle: any connected aspherical $2$-complex with fundamental group $H$ is a model for $BH$, and the bar construction is the universal such model.

### Compact Lie Groups and the Classical Groups

**Definition.** For a Lie group $G$ the classifying space $BG$ is a CW complex, the colimit of the finite-dimensional approximations $G^{*n}$ of the Milnor construction, and for the classical compact groups the universal bundles have the following concrete models, in which $\mathrm{Gr}_n(\mathbb{K}^N)$ is the Grassmannian of $n$-planes:

| $G$ | $BG$ | Universal bundle |
|---|---|---|
| $O(n)$ | $\mathrm{Gr}_n(\mathbb{R}^\infty) = BO(n)$ | tautological $\mathbb{R}^n$-bundle |
| $SO(n)$ | $\mathrm{Gr}_n^+(\mathbb{R}^\infty) = BSO(n)$ | tautological oriented bundle |
| $U(n)$ | $\mathrm{Gr}_n(\mathbb{C}^\infty) = BU(n)$ | tautological $\mathbb{C}^n$-bundle |
| $SU(n)$ | $BSU(n)$ | tautological bundle with trivial determinant |
| $Sp(n)$ | $\mathrm{Gr}_n(\mathbb{H}^\infty) = BSp(n)$ | tautological $\mathbb{H}^n$-bundle |
| $U(1)$ | $\mathbb{CP}^\infty = BU(1)$ | tautological line bundle |

The Grassmannians and the Stiefel manifolds, together with the universal property of the tautological bundle, are treated in *Grassmannians and Stiefel Manifolds*; here they supply the concrete models of the classifying spaces of the classical groups, and the inclusions $\mathrm{Gr}_n(\mathbb{K}^N) \hookrightarrow \mathrm{Gr}_n(\mathbb{K}^{N+1})$ exhibit $BG$ as the colimit of finite-dimensional Grassmannians.

**Proposition.** For a compact connected Lie group $G$ the classifying space satisfies $\pi_1(BG) = 0$ and $\pi_2(BG) \cong \pi_1(G)$; for a general topological group $\pi_n(BG) \cong \pi_{n-1}(G)$ for $n \geq 2$ and $\pi_1(BG) \cong \pi_0(G)$. In particular $B$ of a compact connected Lie group is simply connected, and $B$ of a finite group is a $K(G,1)$.

*Proof.* Immediate from the path–loop theorem: a connected group has $\pi_0(G) = 0$, so $\pi_1(BG) = 0$, and the remaining statements are the degree shift already established. $\square$

**Example.** $BU(1) = \mathbb{CP}^\infty$ has $\pi_2 = \mathbb{Z}$ and higher homotopy trivial, so it is $K(\mathbb{Z},2)$; $BO(1) = \mathbb{RP}^\infty$ is $K(\mathbb{Z}/2\mathbb{Z},1)$; $BSO(2) = BU(1)$ because $SO(2) \cong U(1)$. The descriptions of these groups as matrix groups with their real, complex and quaternionic forms are those of *Matrix Groups and Classical Groups*.

### Products and Abelian Groups

**Theorem.** Let $G$ and $H$ be topological groups. Then $B(G \times H)$ is homotopy equivalent to $BG \times BH$, the classifying space of the trivial group is a point, and for a discrete abelian group $A$ the space $BA$ is again an abelian group in the homotopy category, with a homotopy equivalence $\Omega BA \simeq A$ when $A$ is discrete.

*Proof.* The product $EG \times EH$ is weakly contractible and carries the free action of $G \times H$ with quotient $BG \times BH$, so it is a universal principal $(G\times H)$-bundle by the defining property; the classifying space is therefore $BG \times BH$ up to weak homotopy equivalence, and up to homotopy equivalence when the spaces are CW complexes. For the last statement the path–loop theorem gives $\Omega BA \simeq A$ because the loop space of a classifying space is the group itself in the discrete case, the loops at the basepoint being the group elements. $\square$

**Corollary.** $B\mathbb{Z}^n$ is homotopy equivalent to the $n$-torus $T^n$, and for a finitely generated abelian group the classifying space is a product of circles and infinite lens spaces, so its cohomology is computed from the Künneth formula of *Cup and Cap Products*.

## Eilenberg–MacLane Spaces

### Existence and Uniqueness

**Definition.** Let $\pi$ be a group, abelian when $n \geq 2$, and let $n \geq 1$. An **Eilenberg–MacLane space** of type $(\pi,n)$ is a CW complex $K(\pi,n)$ with

$$
\pi_n(K(\pi,n)) \cong \pi, \qquad \pi_i(K(\pi,n)) = 0 \text{ for } i \neq n .
$$

For $n = 1$ the group $\pi$ is arbitrary; for $n \geq 2$ it is abelian because the higher homotopy groups are abelian.

**Theorem (existence).** For every group $\pi$ and every $n \geq 1$ there is a CW complex $K(\pi,n)$, of finite type when $\pi$ is finitely presented and $n \geq 1$.

*Proof sketch.* For $n = 1$ take a presentation of $\pi$ and the associated $2$-dimensional CW complex $X$ with $\pi_1(X) = \pi$; attach cells of dimension at least three to kill the higher homotopy groups, which is possible because a map from a sphere to the relevant skeleton can be killed by attaching a cell along it, and the attachments do not change $\pi_1$. For $n \geq 2$ one may either repeat the same argument with a wedge of $n$-spheres in place of the $2$-complex, realising $\pi$ as the degree-$n$ part and then killing all other homotopy, or use the loop-space shift below inductively from the case $n = 1$. The finiteness statement follows because a finitely presented group has a finite $2$-complex model and the killing cells may be chosen finitely many in each degree when the homotopy groups are finitely generated, which holds for a finite type space. $\square$

**Theorem (uniqueness).** Any two CW complexes of type $(\pi,n)$ are homotopy equivalent; more generally any two such spaces are weakly homotopy equivalent, and the homotopy equivalence is unique up to homotopy.

*Proof.* A map between two $K(\pi,n)$'s can be constructed cell by cell: the obstruction to extending a map over the $(k+1)$-skeleton of the source lies in the cohomology of the source with coefficients in the homotopy of the target, and the only nonzero homotopy of the target is $\pi$ in degree $n$; inductively a map is built that induces an isomorphism on $\pi_n$, hence is a weak equivalence by the Whitehead theorem, quoted from *Homotopy Groups and Fibrations*. Uniqueness up to homotopy is the standard consequence of the Whitehead theorem for CW complexes. $\square$

### The Loop-Space Shift

**Theorem.** For $n \geq 1$ there is a weak homotopy equivalence

$$
K(\pi,n) \xrightarrow{\ \simeq\ } \Omega K(\pi,n+1)
$$

between the Eilenberg–MacLane space of type $(\pi,n)$ and the loop space of the Eilenberg–MacLane space of type $(\pi,n+1)$; consequently the sequence of Eilenberg–MacLane spaces with fixed $\pi$ forms a spectrum, and $\Omega^k K(\pi,n+k) \simeq K(\pi,n)$ for every $k \geq 0$.

*Proof.* By the path–loop theorem applied to the fibrations $\Omega K(\pi,n+1) \to PK(\pi,n+1) \to K(\pi,n+1)$, the loop space has $\pi_i(\Omega K(\pi,n+1)) \cong \pi_{i+1}(K(\pi,n+1))$, which is $\pi$ for $i = n$ and zero otherwise; the space $\Omega K(\pi,n+1)$ is therefore a CW type of type $(\pi,n)$, and the uniqueness above identifies it with $K(\pi,n)$. $\square$

**Corollary.** The Eilenberg–MacLane spaces are the building blocks of the Postnikov tower: every connected CW complex $X$ has a tower

$$
\cdots \to X_2 \to X_1 \to X_0 = *
$$

with $X_n$ having the same $n$-type as $X$, the fibre of $X_n \to X_{n-1}$ being a $K(\pi_n(X),n)$, and the successive fibrations classified by cohomology classes $k_n \in H^{n+1}(X_{n-1};\pi_n(X))$, the **$k$-invariants** of $X$. The tower is the standard way of assembling a space from its homotopy groups, and it is the reason the obstruction theory used in the uniqueness theorem above takes values in cohomology with coefficients in homotopy.

### Representability of Cohomology

**Theorem (representability).** Let $\pi$ be an abelian group and $n \geq 1$. For every CW complex $X$ there is a natural bijection

$$
H^n(X;\pi) \xrightarrow{\ \cong\ } [X, K(\pi,n)],
$$

where the right-hand side is the set of homotopy classes of maps; for a based connected CW complex the reduced cohomology corresponds to based homotopy classes. The bijection sends a class to its classifying map and is induced by the **fundamental class** $\iota_n \in H^n(K(\pi,n);\pi)$ that corresponds to the identity of $\pi$ under $H^n(K(\pi,n);\pi) \cong \operatorname{Hom}(\pi,\pi)$.

*Proof sketch.* The universal coefficient theorem of *Cohomology and the Universal Coefficient Theorem* gives $H^n(K(\pi,n);\pi) \cong \operatorname{Hom}(\pi,\pi)$, so there is a class $\iota_n$ corresponding to the identity; by naturality the assignment $f \mapsto f^*\iota_n$ gives a map $[X,K(\pi,n)] \to H^n(X;\pi)$. It is surjective because for any class $u \in H^n(X;\pi)$ the obstruction to building a map $f : X \to K(\pi,n)$ with $f^*\iota_n = u$ lies in groups $H^{k+1}(X;\pi_{k}(K(\pi,n)))$ that vanish for $k \geq n$ on the cells of degree at least $n$ and are handled dimension by dimension below that; it is injective because two maps agreeing on $\iota_n$ are homotopic by the same cell-by-cell argument applied to $X \times I$. Equivalently, the functor $H^n(-;\pi)$ is representable and the representing object is unique up to homotopy by the Yoneda lemma, which recovers the uniqueness of $K(\pi,n)$. $\square$

**Corollary.** The cohomology operations of the next section are the cohomology classes of Eilenberg–MacLane spaces: from the Yoneda correspondence,

$$
\operatorname{Nat}\big(H^n(-;\pi),\, H^m(-;\pi')\big) \cong H^m(K(\pi,n);\pi'),
$$

the natural transformations corresponding to the classes on the right.

## Cohomology Operations

### Operations and the Yoneda Correspondence

**Definition.** A **cohomology operation** of type $(n,m;\pi,\pi')$ is a natural transformation

$$
\theta : H^n(-;\pi) \longrightarrow H^m(-;\pi')
$$

between the contravariant functors on the category of CW complexes and continuous maps, natural with respect to the pullback maps $f^*$. The set of such operations is written $\operatorname{Op}(n,m;\pi,\pi')$; it is a set, and it is an abelian group when $\pi'$ is abelian.

**Theorem (Yoneda).** For abelian $\pi$ and $\pi'$ and $n,m \geq 1$ there is a natural isomorphism

$$
\operatorname{Op}(n,m;\pi,\pi') \cong H^m(K(\pi,n);\pi')
$$

of sets, and this is an isomorphism of abelian groups when the operations are added pointwise.

*Proof.* Represent $H^n(-;\pi)$ by $K(\pi,n)$ as above and $H^m(-;\pi')$ by $K(\pi',m)$. A natural transformation between representable functors $[-,A] \to [-,B]$ corresponds, by the Yoneda lemma, to a homotopy class of maps $A \to B$, that is, to an element of $[K(\pi,n),K(\pi',m)]$, which is identified with $H^m(K(\pi,n);\pi')$ by representability again. Naturality in all the variables is the standard statement of the Yoneda lemma for the homotopy category. $\square$

**Definition.** A **stable cohomology operation** of degree $m$ is a sequence of operations $\theta_n \in \operatorname{Op}(n,n+m;\pi,\pi')$ for all $n$ which are compatible with the suspension isomorphisms, so that $\theta_{n+1}$ applied to a suspension is the suspension of $\theta_n$ applied to the class. For $\pi = \pi' = \mathbb{F}_p$ the stable operations of all degrees form a graded algebra $\mathcal{A}_p$ under composition, the **Steenrod algebra**, whose multiplication is the composition of operations and whose grading is the degree shift.

**Remark.** The term "stable" refers to the suspension compatibility, and it is what makes the operations form an algebra rather than a set of unrelated transformations; the algebra acts on the $\mathbb{F}_p$-cohomology of every space, and the axioms below are the axioms of this action.

### The Steenrod Squares

**Theorem (Steenrod; existence and uniqueness).** For every $i \geq 0$ there is a cohomology operation

$$
\mathrm{Sq}^i : H^n(X;\mathbb{F}_2) \longrightarrow H^{n+i}(X;\mathbb{F}_2),
$$

natural in $X$, and the system is uniquely determined by the following axioms:

| Axiom | Statement |
|---|---|
| normalisation | $\mathrm{Sq}^0 = \operatorname{id}$ |
| instability | $\mathrm{Sq}^i x = 0$ for $i > |x|$, and $\mathrm{Sq}^{|x|} x = x^2$ |
| additivity | $\mathrm{Sq}^i(x+y) = \mathrm{Sq}^i x + \mathrm{Sq}^i y$ |
| Cartan formula | $\mathrm{Sq}^k(xy) = \sum_{i+j=k} \mathrm{Sq}^i x \cdot \mathrm{Sq}^j y$ |
| Bockstein | $\mathrm{Sq}^1$ is the Bockstein homomorphism of $0 \to \mathbb{Z}/2 \to \mathbb{Z}/4 \to \mathbb{Z}/2 \to 0$ |

Here $|x|$ is the degree of a homogeneous class $x$. The squares are constructed by Steenrod's method of acyclic models, or by the action of the group of permutations on the cochain level with the formula $\mathrm{Sq}^i = \cup_i$ on the symmetric representatives of cocycles; the Bockstein of *Cohomology and the Universal Coefficient Theorem* identifies $\mathrm{Sq}^1$.

**Proposition (values on powers).** Let $x$ be a class of degree one and $j, k \geq 0$. Then

$$
\mathrm{Sq}^k(x^j) = \binom{j}{k} x^{j+k} \quad \text{in } \mathbb{F}_2,
$$

so that $\mathrm{Sq}^1(x^j)$ is $0$ for $j$ even and $x^{j+1}$ for $j$ odd. More generally, if $x$ is a generator of even degree $m$ with $\mathrm{Sq}^i x = 0$ for $0 < i < m$, then $\mathrm{Sq}^{mk}(x^j) = \binom{j}{k}x^{j+k}$ and $\mathrm{Sq}^i(x^j) = 0$ for $i$ not divisible by $m$.

*Derivation.* The total square $\mathrm{Sq} = \sum_i \mathrm{Sq}^i$ is multiplicative by the Cartan formula, so $\mathrm{Sq}(x^j) = \mathrm{Sq}(x)^j$; for a generator of even degree $m$ the instability axiom gives $\mathrm{Sq}(x) = x + x^2$, since $\mathrm{Sq}^0x = x$, $\mathrm{Sq}^m x = x^2$ and the remaining squares vanish, and expanding $(x + x^2)^j$ over $\mathbb{F}_2$ collects the terms with the binomial coefficients displayed. The cases $m = 1$ and $m = 2$ are the ones used below; for $m = 1$ the formula specialises to the statement for the generator of $H^*(\mathbb{RP}^\infty;\mathbb{F}_2)$.

**Example.** In $H^*(\mathbb{RP}^n;\mathbb{F}_2) = \mathbb{F}_2[x]/(x^{n+1})$ with $|x| = 1$ the squares act by $\mathrm{Sq}^i(x^j) = \binom{j}{i}x^{i+j}$; in particular $\mathrm{Sq}^1 x = x^2$, $\mathrm{Sq}^1(x^2) = 0$, and the pattern is the mod $2$ Pascal triangle read along the powers. Since $\mathrm{Sq}^1$ is the Bockstein, the square computes the integral cohomology of $\mathbb{RP}^n$: a mod $2$ class is the reduction of an integral class exactly when $\mathrm{Sq}^1$ annihilates it, which happens for the even-degree classes and fails in the odd degrees, and the reduced classes together with the top class recover $H^*(\mathbb{RP}^n;\mathbb{Z})$, with $\mathbb{Z}/2$ in the even degrees $0 < i < n$, nothing in the odd degrees below $n$, and $\mathbb{Z}$ at the top when $n$ is odd.

### The Adem Relations

**Theorem (Adem).** For $a < 2b$ the squares satisfy the relations

$$
\mathrm{Sq}^a \mathrm{Sq}^b = \sum_{c=0}^{\lfloor a/2 \rfloor} \binom{b-c-1}{a-2c}\, \mathrm{Sq}^{a+b-c}\, \mathrm{Sq}^{c},
$$

a finite sum because the binomial coefficient vanishes for $c > \lfloor a/2 \rfloor$ under the usual convention. For $a \geq 2b$ the composite $\mathrm{Sq}^a \mathrm{Sq}^b$ is **admissible**, meaning that no relation is needed. The relations hold in every cohomology ring and define the Steenrod algebra as the quotient of the free associative algebra on the $\mathrm{Sq}^i$ by them.

*Proof sketch.* Both sides of a relation are natural operations of the same degree, so it suffices to check the relation on a class that generates all classes of its degree under pullback; the fundamental class $\iota_n \in H^n(K(\mathbb{Z}/2,n);\mathbb{F}_2)$ does this, since every class of degree $n$ on a CW complex is the pullback of $\iota_n$ along its classifying map. The check for all $n$ is the computation of the cohomology of the Eilenberg–MacLane spaces below, in which the Cartan formula and the instability $\mathrm{Sq}^n\iota_n = \iota_n^2$ determine the action; it cannot be made on a class of degree one, where the examples below show that the relations are invisible. $\square$

**Example.** The low-degree relations, obtained by evaluating the binomial coefficients in the formula, are

$$
\mathrm{Sq}^1\mathrm{Sq}^1 = 0, \qquad
\mathrm{Sq}^1\mathrm{Sq}^2 = \mathrm{Sq}^3, \qquad
\mathrm{Sq}^2\mathrm{Sq}^2 = \mathrm{Sq}^3\mathrm{Sq}^1, \qquad
\mathrm{Sq}^3\mathrm{Sq}^3 = \mathrm{Sq}^5\mathrm{Sq}^1 .
$$

The first says that $\mathrm{Sq}^1$ is a differential; the second shows that $\mathrm{Sq}^3$ is not a new generator but already a composite, and the third and fourth show the same for their leading composites. On the generator $x$ of $H^*(\mathbb{RP}^\infty;\mathbb{F}_2)$ of degree one every one of these composites vanishes: $\mathrm{Sq}^1x = x^2$ and $\mathrm{Sq}^1(x^2) = 0$, so $\mathrm{Sq}^1\mathrm{Sq}^1 x = 0$; $\mathrm{Sq}^2x = 0$ because $\binom{1}{2} = 0$, so $\mathrm{Sq}^2\mathrm{Sq}^2x = 0$ while $\mathrm{Sq}^3\mathrm{Sq}^1x = \mathrm{Sq}^3(x^2) = \binom{2}{3}x^5 = 0$. The relations are therefore invisible on a class of degree one and are genuine relations between operations; verifying one requires a class of higher degree, or the model computation in the cohomology of the Eilenberg–MacLane spaces below.

### The Steenrod Powers

**Theorem (Steenrod; odd primary).** Let $p$ be an odd prime. For $i \geq 0$ there are cohomology operations

$$
P^i : H^n(X;\mathbb{F}_p) \to H^{n+2i(p-1)}(X;\mathbb{F}_p), \qquad \beta : H^n(X;\mathbb{F}_p) \to H^{n+1}(X;\mathbb{F}_p),
$$

natural in $X$, uniquely determined by

| Axiom | Statement |
|---|---|
| normalisation | $P^0 = \operatorname{id}$ |
| instability | $P^i x = 0$ for $2i > |x|$, and $P^i x = x^p$ for $2i = |x|$ |
| additivity | $P^i(x+y) = P^i x + P^i y$, and $\beta$ is additive |
| Cartan formula | $P^k(xy) = \sum_{i+j=k} P^i x \cdot P^j y$ |
| derivation | $\beta(xy) = \beta x \cdot y + (-1)^{|x|} x \cdot \beta y$, and $\beta^2 = 0$ |

The operation $\beta$ is the Bockstein of $0 \to \mathbb{Z}/p \to \mathbb{Z}/p^2 \to \mathbb{Z}/p \to 0$, and it is the odd-primary analogue of $\mathrm{Sq}^1$; the degree formula $|P^i| = 2i(p-1)$ is forced by the requirement that $P^i x = x^p$ when $2i = |x|$, since $x^p$ has degree $p|x| = |x| + 2i(p-1)$.

**Theorem (Adem; odd primary).** For $a < pb$,

$$
P^a P^b = \sum_{c=0}^{\lfloor a/p \rfloor} (-1)^{a+c} \binom{(p-1)(b-c)-1}{a-pc}\, P^{a+b-c} P^{c},
$$

and there are further relations involving $\beta$ and $P$ of the same shape, quoted from the literature, which together with the displayed family define the Steenrod algebra $\mathcal{A}_p$.

**Example.** For $p = 3$ and $a = b = 1$ the formula has the single term $c = 0$ with sign $-1$ and binomial coefficient $\binom{(3-1)\cdot 1 - 1}{1} = \binom{1}{1} = 1$, so that

$$
P^1P^1 = -P^2 \quad \text{in } \mathcal{A}_3 .
$$

This is consistent with the Cartan formula: in $H^*(\mathbb{F}_3[x];\mathbb{F}_3)$ with $|x| = 2$ one has $P^k(x^j) = \binom{j}{k} x^{\,j + k(p-1)}$ for $x$ of even degree, so $P^1(x^2) = \binom{2}{1}x^{4} = 2x^4$, $P^1(x^4) = \binom{4}{1}x^{6} = 4x^6 = x^6$ and $P^2(x^2) = \binom{2}{2}x^6 = x^6$; hence $P^1P^1(x^2) = 2P^1(x^4) = 2x^6 = -x^6 = -P^2(x^2)$ in $\mathbb{F}_3$, as the relation requires. The instability axiom is used here only through $P^1x = x^3$, and the computation is a verification of the sign in the Adem relation, not a derivation of it.

### The Steenrod Algebra

**Definition.** The **Steenrod algebra** $\mathcal{A}_p$ is the graded $\mathbb{F}_p$-algebra of stable cohomology operations on mod $p$ cohomology; it is generated by the $\mathrm{Sq}^i$ when $p = 2$ and by the $\beta$ and $P^i$ when $p$ is odd, subject to the Adem relations. The **excess** of a monomial $\mathrm{Sq}^I = \mathrm{Sq}^{i_1}\mathrm{Sq}^{i_2}\cdots\mathrm{Sq}^{i_k}$ is

$$
e(I) = \sum_{j=1}^{k}\left(i_j - 2i_{j+1}\right) = i_1 - i_2 - \cdots - i_k, \qquad i_{k+1} = 0,
$$

and $\mathrm{Sq}^I$ is **admissible** if $i_j \geq 2i_{j+1}$ for all $j$, the last index being at least one. Every monomial is congruent modulo the Adem relations to a sum of admissible ones.

**Theorem (Serre).** The admissible monomials form a basis of $\mathcal{A}_2$ as an $\mathbb{F}_2$-vector space, and the Poincaré series of $\mathcal{A}_2$ is

$$
\sum_{d \geq 0} \dim_{\mathbb{F}_2}(\mathcal{A}_2)^d\, t^d = \prod_{k \geq 1} \frac{1}{1 - t^{2^k-1}} ,
$$

so that the dimensions in degrees $0$ to $12$ are $1, 1, 1, 2, 2, 2, 3, 4, 4, 5, 6, 6, 7$. For odd $p$ the admissible monomials of the form $\beta^{\epsilon_1}P^{i_1}\beta^{\epsilon_2}\cdots P^{i_k}\beta^{\epsilon_{k+1}}$ with $i_j \geq p\,i_{j+1} + \epsilon_{j+1}$ form a basis of $\mathcal{A}_p$.

*Proof sketch.* Admissibility is the normal form statement: the Adem relations rewrite every composite of two squares of the wrong shape into a sum of composites whose indices satisfy the inequality, and the rewriting terminates because the leading index decreases, so the admissible monomials span. Linear independence is proved by evaluating the monomials on the fundamental classes of the Eilenberg–MacLane spaces, or through Milnor's description of $\mathcal{A}_2$ as the dual of a polynomial algebra. The count of admissible monomials of degree $d$ is the coefficient of $t^d$ in the displayed product: the two counts agree through degree $24$, where both are $1, 1, 1, 2, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 9, 11, 12, 13, 15, 16, 17, 20, 22, 23, 26$ in degrees $0$ to $24$. $\square$

**Example (the unstable condition).** For an admissible $I$, telescoping the excess gives $e(I) = i_k + \sum_{j<k}(i_j - 2i_{j+1}) \geq i_k$, so $e(I) \geq 1$ whenever $I$ is nonempty, and the destabilisation axiom reads

$$
\mathrm{Sq}^I x = 0 \qquad \text{whenever } e(I) > |x| .
$$

On the fundamental class $\iota_1$ of $K(\mathbb{Z}/2,1) = \mathbb{RP}^\infty$ of degree one this leaves only $\mathrm{Sq}^1$ free to act, since $e(I) > 1$ for every nonempty admissible $I$ other than $(1)$; and $\mathrm{Sq}^1\iota_1 = \iota_1^2$ by instability. In the Serre theorem below the generators are the monomials of excess less than $n$, so for $n = 1$ only the empty monomial survives, giving $H^*(\mathbb{RP}^\infty;\mathbb{F}_2) = \mathbb{F}_2[\iota_1]$ with $\mathrm{Sq}^1\iota_1 = \iota_1^2$, which is exactly the cohomology of $\mathbb{RP}^\infty$.

## Computations

### Projective Spaces

**Example.** $H^*(\mathbb{RP}^\infty;\mathbb{F}_2) = \mathbb{F}_2[x]$ with $|x| = 1$, and $H^*(\mathbb{CP}^\infty;\mathbb{F}_2) = \mathbb{F}_2[y]$ with $|y| = 2$. The squares act on the powers by the binomial formula, and the total square of a class is the sum of its squares; the total Steenrod square is multiplicative by the Cartan formula, so $\mathrm{Sq}(x^j) = x^j(1+x)^j$ and

$$
\mathrm{Sq}(x^{j}) = \sum_{i} \binom{j}{i} x^{j+i}.
$$

For $\mathbb{CP}^\infty = K(\mathbb{Z},2)$ the class $y$ is the fundamental class, $P^1 y = y^p$ in $\mathbb{F}_p$-cohomology by instability, and $\mathrm{Sq}^2 y = y^2$, which is the lowest-dimensional nontrivial square.

**Remark (the relation to characteristic classes).** The operations are the algebraic content of the characteristic classes: for a closed smooth manifold $M$ the Wu formula determines the Stiefel–Whitney classes $w_i$ from the squares of its cohomology classes, and for $\mathbb{RP}^n$ the total class is $w = (1+x)^{n+1}$, which is exactly the total square of the generator computed above. The characteristic classes themselves, and their theory over the classifying spaces $BO(n)$ and $BU(n)$, are the subject of *Characteristic Classes*; nothing further is used here.

### The Cohomology of Eilenberg–MacLane Spaces

**Theorem (Serre).** Let $n \geq 1$. The mod $2$ cohomology of the Eilenberg–MacLane space is a polynomial algebra,

$$
H^*(K(\mathbb{Z}/2\mathbb{Z},n);\mathbb{F}_2) = \mathbb{F}_2\big[\,\mathrm{Sq}^I \iota_n \ :\ I \text{ admissible},\ e(I) < n\,\big],
$$

the monomial $I$ empty contributing the fundamental class $\iota_n$; and for $n \geq 2$,

$$
H^*(K(\mathbb{Z},n);\mathbb{F}_2) = \mathbb{F}_2\big[\,\mathrm{Sq}^I \iota_n \ :\ I \text{ admissible},\ e(I) < n,\ i_k \neq 1\,\big].
$$

*Proof sketch.* The classes $\mathrm{Sq}^I\iota_n$ with $I$ admissible are the candidates for polynomial generators, and the proof of the theorem is that they are algebraically independent and generate; the two statements are proved together with the analogous statements for the other coefficient groups and are quoted from the literature. The conditions on the excess are exactly the unstable conditions, and the additional condition $i_k \neq 1$ in the integral case reflects the presence of the Bockstein. $\square$

**Example.** For $n = 1$ the admissible monomials of excess less than one are only the empty one, since $e(I) \geq i_k \geq 1$ for nonempty $I$; hence $H^*(K(\mathbb{Z}/2,1);\mathbb{F}_2) = \mathbb{F}_2[\iota_1]$, which is $H^*(\mathbb{RP}^\infty;\mathbb{F}_2)$, as it must be. For $n = 2$ the admissible monomials of excess one are exactly $(1)$, $(2,1)$, $(4,2,1)$, $(8,4,2,1),\ldots$, so the polynomial generators of $H^*(K(\mathbb{Z}/2,2);\mathbb{F}_2)$ have degrees $2,3,5,9,17,33,\ldots$, that is $2^k+1$ for $k \geq 0$; and in the integral case the condition $i_k \neq 1$ removes them all, leaving $H^*(K(\mathbb{Z},2);\mathbb{F}_2) = \mathbb{F}_2[\iota_2]$, which is $H^*(\mathbb{CP}^\infty;\mathbb{F}_2)$, as it must be. For $n = 3$ the integral generators that survive have degrees $3,5,9,17,33,\ldots$, related to the fundamental class by $\iota_3$, $\mathrm{Sq}^2\iota_3$, $\mathrm{Sq}^4\mathrm{Sq}^2\iota_3$, and so on.

**Corollary.** The Eilenberg–MacLane spaces are the coefficients of the obstruction theory: the successive quotients of a Postnikov tower are the spaces $K(\pi_n(X),n)$, and the cohomology operations are exactly the classes of their cohomology. The applications of this to a fibration, namely the filtration of the cohomology of the total space and the transgression in the spectral sequence, belong.

## Summary

A principal $G$-bundle over $X$ is classified by a map $X \to BG$, where $BG$ is the base of the universal bundle $EG \to BG$ with $EG$ weakly contractible, and pullback of the universal bundle gives the natural bijection $[X,BG] \cong \operatorname{Prin}_G(X)$; a homomorphism $G \to H$ induces $BG \to BH$, and $B$ preserves products and coproducts up to homotopy. The universal bundle is constructed either as the colimit of the Milnor joins $G^{*n}$, free and weakly contractible because the join of $n$ nonempty spaces is at least $(n-2)$-connected, or as the realisation of the bar construction, whose chain complex is the bar resolution and which computes group homology and cohomology: $H_n(BH) \cong H_n(H)$ and $H^n(BH;M) \cong H^n(H;M)$ for a discrete group $H$. The path–loop theorem applied to the fibre sequence $G \to EG \to BG$ gives $\pi_n(BG) \cong \pi_{n-1}(G)$ for $n \geq 2$ and $\pi_1(BG) \cong \pi_0(G)$, so a discrete group has $BH = K(H,1)$, a connected group has a simply connected $BG$, and the classical groups have the Grassmannian models $BO(n)$, $BU(n)$, $BSp(n)$ and so on.

An Eilenberg–MacLane space $K(\pi,n)$ has homotopy concentrated in degree $n$; it exists, is unique up to weak homotopy equivalence, satisfies $\Omega K(\pi,n+1) \simeq K(\pi,n)$, and represents singular cohomology, $H^n(X;\pi) \cong [X,K(\pi,n)]$. The cohomology operations are the natural transformations between these functors, and by the Yoneda lemma they are the cohomology classes of the $K(\pi,n)$: $\operatorname{Op}(n,m;\pi,\pi') \cong H^m(K(\pi,n);\pi')$. The stable operations for $\mathbb{F}_p$ coefficients generate the Steenrod algebra $\mathcal{A}_p$, with generators $\mathrm{Sq}^i$ for $p = 2$ and $\beta, P^i$ for odd $p$; the squares are characterised by normalisation, instability, additivity, the Cartan formula and the identification of $\mathrm{Sq}^1$ with the Bockstein, they satisfy the Adem relations, and the admissible monomials form a basis of $\mathcal{A}_2$ with Poincaré series $\prod_{k\geq1}(1-t^{2^k-1})^{-1}$. The mod $2$ cohomology of the Eilenberg–MacLane spaces is the polynomial algebra on the monomials of excess less than $n$, which recovers $H^*(\mathbb{RP}^\infty;\mathbb{F}_2)$ from $K(\mathbb{Z}/2,1)$ and $H^*(\mathbb{CP}^\infty;\mathbb{F}_2)$ from $K(\mathbb{Z},2)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G$, $H$ | Topological group; discrete group |
| $P \to B$ | Principal $G$-bundle over the base $B$ |
| $\operatorname{Prin}_G(X)$ | Isomorphism classes of principal $G$-bundles over $X$ |
| $[X,Y]$ | Homotopy classes of maps $X \to Y$ |
| $EG \to BG$ | Universal principal $G$-bundle; classifying space |
| $G^{*n}$, $\operatorname{colim}$ | $n$-fold join; the colimit forming $EG$ |
| $B_\bullet G$, $E_\bullet G$ | Bar construction; the free simplicial model of $EG$ |
| $K(\pi,n)$ | Eilenberg–MacLane space, $\pi_i = 0$ for $i \neq n$ and $\pi_n = \pi$ |
| $\iota_n$ | Fundamental class of $K(\pi,n)$ |
| $k_n$ | $k$-invariant of a Postnikov tower |
| $H^n(X;\pi)$ | Singular cohomology with coefficients in $\pi$ |
| $\Omega X$ | Loop space of a based space $X$ |
| $\mathrm{Sq}^i$ | Steenrod square, $H^n(-;\mathbb{F}_2) \to H^{n+i}(-;\mathbb{F}_2)$ |
| $P^i$, $\beta$ | Steenrod power and odd-primary Bockstein |
| $\mathcal{A}_p$ | Steenrod algebra of stable operations mod $p$ |
| $\mathrm{Sq}^I$, $e(I)$ | Admissible monomial, $\mathrm{Sq}^{i_1}\cdots\mathrm{Sq}^{i_k}$; its excess |
| $\mathbb{F}_p$ | The field $\mathbb{Z}/p\mathbb{Z}$ |
| $|x|$ | Degree of a homogeneous cohomology class |





## Further Reading

- Norman Steenrod and David B. A. Epstein, *Cohomology Operations* (Princeton University Press, 1962), for the construction, the axioms and the Adem relations of the squares and powers.
- John Milnor and James D. Stasheff, *Characteristic Classes* (Princeton University Press, 1974), for the classifying spaces of the classical groups, the universal bundles and the Grassmannian models.
- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002), for the classifying spaces of groups, the bar construction, Eilenberg–MacLane spaces and the Steenrod squares.
- Jean-Pierre Serre, *Cohomologie modulo $2$ des complexes d'Eilenberg–MacLane*, Commentarii Mathematici Helvetici 27 (1953), 198–232, for the cohomology of the Eilenberg–MacLane spaces and the admissible basis.
- José Adem, *The relations on Steenrod powers of cohomology classes*, in Algebraic Geometry and Topology: A Symposium in Honor of S. Lefschetz (Princeton University Press, 1957), for the Adem relations at all primes.
- Paul G. Goerss and John F. Jardine, *Simplicial Homotopy Theory* (Birkhäuser, 2009), for the bar construction, the classifying space of a simplicial group and the homotopy theory of the classifying spaces.
- Saunders Mac Lane, *Homology* (Springer, 1975), for the bar resolution, group cohomology and the interpretation of $H^n(H;M)$ as the cohomology of $BH$.
