
# __Grassmannians and Stiefel Manifolds__

## Introduction

The **Grassmannian** $\mathrm{Gr}_k(\mathbb{R}^n)$ is the set of $k$-dimensional linear subspaces of $\mathbb{R}^n$, and the **Stiefel manifold** $V_k(\mathbb{R}^n)$ is the set of orthonormal $k$-frames in $\mathbb{R}^n$. Both are smooth manifolds, both are compact, and the second is a principal bundle over the first with structure group $O(k)$: a frame determines the subspace it spans, and the frames spanning a fixed subspace are exactly the orthonormal bases of that subspace, a copy of $O(k)$. The pair is the model example of a homogeneous space and a principal bundle, the simplest nontrivial family of Riemannian symmetric spaces after the spheres, and the ambient space of the Gauss map of a submanifold and of the classifying spaces of vector bundles.

Grassmannians appear whenever a linear-algebraic object is allowed to vary: a subspace of a vector space, a projection, a line in projective space, a plane in space, a linear system of divisors. The real projective space $\mathbb{RP}^{n-1}$ is the Grassmannian $\mathrm{Gr}_1(\mathbb{R}^n)$ of lines, the sphere $S^{n-1}$ is the Stiefel manifold $V_1(\mathbb{R}^n)$ of unit vectors, and the orthogonal group $O(n)$ is $V_n(\mathbb{R}^n)$. The general linear group acts transitively on the Grassmannians, with stabiliser a parabolic subgroup, so the Grassmannian is the homogeneous space $O(n)/(O(k)\times O(n-k))$ — one of the two great families of symmetric spaces, the one of compact type and rank $\min(k, n-k)$.

This article defines both manifolds by three routes — as sets of subspaces, as sets of projections, and as quotients of groups — and shows the three descriptions agree. It proves that they are compact smooth manifolds, computes their dimensions, gives the charts from the Stiefel coordinates, identifies the tautological and universal bundles and the principal bundle $V_k(\mathbb{R}^n) \to \mathrm{Gr}_k(\mathbb{R}^n)$, and constructs the natural Riemannian metric as the one induced from the ambient Euclidean space, with its geodesics, curvature and symmetric-space structure. It treats the complex and quaternionic analogues; the Plücker embedding of the Grassmannian into a projective space, whose image is cut out by the Plücker relations; the Schubert cells, which give a cell decomposition and hence the cohomology; the Euler characteristic; and the relation of the Grassmannians to the classifying space $BO(k)$ and to the Gauss map of a submanifold.

The article assumes *Smooth Manifolds and Differential Geometry* for manifolds, submanifolds and group actions on manifolds; *Fibre Bundles, Connections and Curvature* for principal bundles, associated bundles, classifying spaces and the tautological bundle; *Riemannian Geometry* and *Curvature and Geodesics* for the metric, geodesics and curvature; *Euclidean Geometry*, *Spherical Geometry* and *Hyperbolic Geometry* for the model geometries that the low-dimensional cases are; *Groups*, *Group Actions and Structure* and *Matrix Groups and Classical Groups* for the group theory; *The Exterior Algebra* and *The Determinant and Alternating Forms* for the exterior algebra and the Plücker coordinates; and *The Three Two-Dimensional Algebras and the Three Kinds of Rotation* for the correspondence between the number systems $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$ and the division algebras' Grassmannians. The Schubert calculus, the intersection theory of the Grassmannian, belongs to the algebraic side of the corpus and is cited as standard; the homology theory is quoted from algebraic topology. The article is the prerequisite. No physics is invoked.

## The Grassmannian as a Manifold

### The Set of Subspaces

**Definition.** Let $V$ be an $n$-dimensional real vector space with an inner product. For $0 \leq k \leq n$ the **Grassmannian** is the set

$$
\mathrm{Gr}_k(V) = \{W \subseteq V : W \text{ a linear subspace of dimension } k\},
$$

and $\mathrm{Gr}_k(\mathbb{R}^n)$ is written for the case of $V = \mathbb{R}^n$ with the standard inner product.

**Example.** $\mathrm{Gr}_0(\mathbb{R}^n)$ and $\mathrm{Gr}_n(\mathbb{R}^n)$ are single points; $\mathrm{Gr}_1(\mathbb{R}^n) = \mathbb{RP}^{n-1}$ is the real projective space of *Smooth Manifolds and Differential Geometry*; $\mathrm{Gr}_{n-1}(\mathbb{R}^n) = \mathbb{RP}^{n-1}$ again, by the duality $W \mapsto W^\perp$; and $\mathrm{Gr}_2(\mathbb{R}^3)$ is the set of lines through the origin in $\mathbb{R}^3$, hence also $\mathbb{RP}^2$. The **duality** $\mathrm{Gr}_k(V) \to \mathrm{Gr}_{n-k}(V)$, $W \mapsto W^\perp$, is a diffeomorphism.

**Definition.** For $V = \mathbb{R}^n$ with the standard inner product, a **projection** is an endomorphism $P \in \operatorname{End}(\mathbb{R}^n)$ with $P^2 = P$ and $P^T = P$, that is, an orthogonal projection. The **rank** of $P$ is the dimension of its image.

**Theorem.** The map $W \mapsto P_W$, the orthogonal projection onto $W$, is a bijection from $\mathrm{Gr}_k(\mathbb{R}^n)$ onto the set

$$
\{P \in M_n(\mathbb{R}) : P^2 = P,\ P^T = P,\ \operatorname{rank} P = k\}.
$$

**Proof.** An orthogonal projection has image $W$ of rank $k$, and $W$ is recovered from $P_W$ as its image; conversely a symmetric idempotent of rank $k$ is the orthogonal projection onto its image. The two constructions are inverse. $\square$

### Charts and the Manifold Structure

**Theorem.** The Grassmannian $\mathrm{Gr}_k(\mathbb{R}^n)$ is a compact smooth manifold of dimension $k(n-k)$.

**Proof sketch.** For a partition of $\{1, \ldots, n\}$ into a set $I$ of size $k$ and its complement $J$, let $U_I$ be the set of subspaces $W$ such that the projection $\mathbb{R}^n \to \mathbb{R}^I$ restricts to an isomorphism $W \to \mathbb{R}^I$. Equivalently, $W$ is the graph of a unique linear map $A : \mathbb{R}^I \to \mathbb{R}^J$ given by the matrix with entries $A_{ji}$ such that the columns $\binom{e_i}{A_{\cdot i}}$ span $W$. The assignment $W \mapsto A$ is a bijection $U_I \to M_{J,I}(\mathbb{R}) \cong \mathbb{R}^{k(n-k)}$, and the transition maps between two charts are smooth rational functions of the matrices, so the $U_I$ form a smooth atlas. Compactness is the compactness of the image under the projections: the map $W \mapsto P_W$ has image closed and bounded in the finite-dimensional space $M_n(\mathbb{R})$. $\square$

**Definition.** The coordinates $A$ above are the **Stiefel coordinates** of $W$ in the chart $U_I$, and the chart is the **big cell** when $I = \{1, \ldots, k\}$. The Grassmannian is covered by the $\binom{n}{k}$ charts $U_I$, one for each $k$-element subset of $\{1, \ldots, n\}$.

**Corollary.** $\dim \mathbb{RP}^{n-1} = n - 1$, and $\dim \mathrm{Gr}_2(\mathbb{R}^4) = 4$; in general the dimension $k(n-k)$ is the number of independent entries of the matrix of a projection of rank $k$.

## The Stiefel Manifold

### Frames

**Definition.** The **Stiefel manifold** $V_k(\mathbb{R}^n)$ is the set of ordered orthonormal $k$-tuples $(v_1, \ldots, v_k)$ of vectors in $\mathbb{R}^n$, that is, the set of matrices $X \in M_{n,k}(\mathbb{R})$ with $X^TX = I_k$. Equivalently, $V_k(\mathbb{R}^n)$ is the set of linear isometries $\mathbb{R}^k \hookrightarrow \mathbb{R}^n$.

**Example.** $V_1(\mathbb{R}^n) = S^{n-1}$; $V_n(\mathbb{R}^n) = O(n)$; $V_2(\mathbb{R}^3)$ is the set of ordered orthonormal pairs in $\mathbb{R}^3$, a three-dimensional manifold.

**Theorem.** The Stiefel manifold $V_k(\mathbb{R}^n)$ is a compact smooth manifold of dimension

$$
\dim V_k(\mathbb{R}^n) = nk - \frac{k(k+1)}{2}.
$$

**Proof.** The map $F : M_{n,k}(\mathbb{R}) \to \operatorname{Sym}_k(\mathbb{R})$, $F(X) = X^TX - I_k$, has $V_k = F^{-1}(0)$. Its differential at $X$ is $dF_X(H) = X^TH + H^TX$; this is surjective whenever $X^TX = I_k$, because for a symmetric $S$ one takes $H = \frac{1}{2}XS$, giving $X^TH + H^TX = \frac{1}{2}S + \frac{1}{2}S = S$. Hence $0$ is a regular value and $V_k = F^{-1}(0)$ is a submanifold of dimension $nk - \dim\operatorname{Sym}_k = nk - k(k+1)/2$, by the regular value theorem of *Smooth Manifolds and Differential Geometry*. It is closed and bounded in $M_{n,k}$, hence compact. $\square$

**Corollary.** $\dim V_1(\mathbb{R}^n) = n - 1$, recovering the sphere $S^{n-1}$; $\dim V_n(\mathbb{R}^n) = n^2 - n(n+1)/2 = n(n-1)/2$, recovering $\dim O(n)$; $\dim V_2(\mathbb{R}^3) = 6 - 3 = 3$.

### The Frame Bundle

**Theorem.** The map

$$
\pi : V_k(\mathbb{R}^n) \longrightarrow \mathrm{Gr}_k(\mathbb{R}^n), \qquad \pi(v_1, \ldots, v_k) = \operatorname{span}(v_1, \ldots, v_k),
$$

is a smooth surjective submersion whose fibre over $W$ is the set of orthonormal bases of $W$, in bijection with $O(k)$. It is a principal $O(k)$-bundle, the **Stiefel bundle**, with the action of $O(k)$ on a frame by right multiplication; the base is the Grassmannian and the total space the Stiefel manifold.

**Proof sketch.** Surjectivity is the existence of an orthonormal basis; the fibre is $O(k)$ by the definition of orthonormal basis; local trivialisations are obtained from a local section of $\pi$ constructed by the Gram–Schmidt process applied to the columns of a projection. The bundle theory is that of *Fibre Bundles, Connections and Curvature*. $\square$

**Corollary (dimensions).** The dimension count is consistent:

$$
\dim V_k(\mathbb{R}^n) = \dim \mathrm{Gr}_k(\mathbb{R}^n) + \dim O(k) = k(n-k) + \frac{k(k-1)}{2} = nk - \frac{k(k+1)}{2}.
$$

**Definition.** The **tautological bundle** $\gamma_k \to \mathrm{Gr}_k(\mathbb{R}^n)$ has fibre over $W$ the subspace $W$ itself, with total space

$$
E(\gamma_k) = \{(W, v) : W \in \mathrm{Gr}_k(\mathbb{R}^n),\ v \in W\} \subseteq \mathrm{Gr}_k(\mathbb{R}^n) \times \mathbb{R}^n .
$$

The **orthogonal complement bundle** $\gamma_k^\perp$ has fibre $W^\perp$. Both are smooth vector bundles of rank $k$ and $n-k$, associated to the Stiefel bundle by the standard representation of $O(k)$ and its complement.

**Proposition.** The tangent bundle of the Grassmannian is the bundle

$$
T\mathrm{Gr}_k(\mathbb{R}^n) \cong \operatorname{Hom}(\gamma_k, \gamma_k^\perp),
$$

whose fibre at $W$ is the space of linear maps $W \to W^\perp$, of dimension $k(n-k)$.

**Proof sketch.** A curve of subspaces through $W$ has derivative a linear map $W \to \mathbb{R}^n/W \cong W^\perp$; the identification of the tangent space with the graph of such a map uses the projection chart. $\square$

## The Natural Metric and Its Geometry

### The Riemannian Metric

**Definition.** The **standard metric** on $\mathrm{Gr}_k(\mathbb{R}^n)$ is induced by the map $W \mapsto P_W$ into the Euclidean space $M_n(\mathbb{R})$ with the Hilbert–Schmidt inner product $\langle A, B\rangle = \operatorname{tr}(A^TB)$; equivalently, for tangent vectors $X, Y \in \operatorname{Hom}(W, W^\perp)$ at $W$, the metric is $g_W(X, Y) = \operatorname{tr}(X^TY)$.

**Theorem.** The standard metric makes $\mathrm{Gr}_k(\mathbb{R}^n)$ a Riemannian manifold of nonnegative sectional curvature. Its geodesics are the images of the one-parameter subgroups $\exp(tX)$ of $O(n)$ acting on $W$, that is,

$$
\gamma(t) = \exp(tX)\,W, \qquad X \in \mathfrak{so}(n),
$$

and they are closed, since $O(n)$ is compact and the exponential of $\mathfrak{so}(n)$ is periodic.

**Proof sketch.** The embedding $W \mapsto P_W$ is equivariant for the action of $O(n)$ by conjugation and is isometric for the standard metrics, so the metric is $O(n)$-invariant; an $O(n)$-invariant metric on a homogeneous space has the geodesics given by the one-parameter subgroups through the identity, and the compactness of $O(n)$ makes them closed. $\square$

### The Symmetric Space Structure

**Theorem.** The Grassmannian is the homogeneous space

$$
\mathrm{Gr}_k(\mathbb{R}^n) = O(n)/(O(k) \times O(n-k)),
$$

and, in the oriented case, $SO(n)/(SO(k) \times SO(n-k))$; the action of $O(n)$ is transitive and the stabiliser of $W_0 = \mathbb{R}^k \times \{0\}$ is $O(k) \times O(n-k)$, acting on $W_0$ and on its orthogonal complement.

**Proof.** The group $O(n)$ acts on subspaces preserving dimension, on the complement, $W \mapsto (AW)$. It is transitive: any $W$ has an orthonormal basis completed to a basis of $\mathbb{R}^n$, giving an orthogonal matrix carrying $W_0$ to $W$. The stabiliser of $W_0$ preserves $W_0$ and its orthogonal complement, hence is $O(k) \times O(n-k)$. $\square$

**Theorem (symmetric space).** The Grassmannian is a Riemannian symmetric space: for each $W$ the **geodesic symmetry** $\sigma_W$ given by reflection in $W$, that is $\sigma_W(v) = v$ for $v \in W$ and $\sigma_W(v) = -v$ for $v \in W^\perp$, is an involutive isometry with isolated fixed point $W$; and $\sigma_W$ reverses every geodesic through $W$.

**Proof.** The reflection $\sigma_W = P_W - P_{W^\perp}$ is an orthogonal transformation, hence an isometry preserving the Grassmannian and acting on the tangent space $T_W\mathrm{Gr} = \operatorname{Hom}(W, W^\perp)$ by $X \mapsto -X$, so its differential at $W$ is $-\mathrm{id}$; an isometry with differential $-\mathrm{id}$ at a fixed point reverses every geodesic through it, which is the defining property of a symmetric space. $\square$

**Corollary (rank and isotropy).** The rank of $\mathrm{Gr}_k(\mathbb{R}^n)$ as a symmetric space is $\min(k, n-k)$, the dimension of a maximal flat totally geodesic submanifold. The space is of **compact type**: the group $O(n)$ is compact, the sectional curvature is nonnegative, and the space has positive curvature.

**Definition.** A maximal flat in $\mathrm{Gr}_k(\mathbb{R}^n)$ is obtained by choosing a decomposition $\mathbb{R}^n = \mathbb{R}^{\min(k,n-k)} \oplus \mathbb{R}^{\min(k,n-k)} \oplus \mathbb{R}^{\text{rest}}$ into mutually orthogonal pieces of the indicated dimensions and varying the graph of a diagonal map between the first two.

**Proof sketch.** The stabiliser $O(k)\times O(n-k)$ acts on the tangent space, and the maximal abelian subalgebra of its action is diagonal of size $\min(k, n-k)$; the corresponding flat is totally geodesic since its tangent directions close under the bracket. $\square$

### Curvature

**Theorem.** For an orthonormal pair $X, Y$ of tangent vectors at $W$, the sectional curvature of the standard metric is

$$
K(X \wedge Y) = \| [X, Y]\|^2 \geq 0,
$$

where the bracket is that of $\mathfrak{so}(n)$, identified with $\bigwedge^2\mathbb{R}^n$, and the norm is the invariant norm (the formula is stated for the normalisation in which the metric is that of the embedding); in particular the curvature of $\mathrm{Gr}_k(\mathbb{R}^n)$ is nonnegative and it vanishes exactly on the two-planes tangent to a maximal flat.

**Proof sketch.** The formula is the general formula $K(X,Y) = \|[X,Y]\|^2$ for the curvature of a symmetric space $G/H$ of compact type with an $\operatorname{Ad}(H)$-invariant metric, applied to $G = O(n)$, $H = O(k)\times O(n-k)$ and the inner product on the complement of $\mathfrak{h}$ in $\mathfrak{so}(n)$; the vanishing of the bracket is exactly the commuting condition that defines a flat, and the nonnegativity is the compact type. $\square$

**Example (the real projective space).** For $k = 1$ the Grassmannian is $\mathbb{RP}^{n-1} = O(n)/(O(1)\times O(n-1)) = S^{n-1}/\{\pm 1\}$, of rank one and constant positive sectional curvature: the map $W \mapsto P_W$ sends a unit vector $v$ to $vv^T$ in the unit sphere of $\operatorname{Sym}_n(\mathbb{R})$, and the differential on a unit normal direction $w \perp v$ has squared norm $2$, so the induced metric is twice the round metric of $S^{n-1}$ and the sectional curvature is $1/2$ in this normalisation. The space is the elliptic space $\mathbb{E}^{n-1}$ of *Spherical Geometry*, of diameter $\pi/\sqrt2$ in this normalisation and, with the normalisation that makes the curvature $+1$, exactly the quotient of the round sphere of radius one by the antipodal map. Its geodesics are the projective lines, images of great circles.

## The Plücker Embedding

### Exterior Powers and Plücker Coordinates

**Definition.** Let $W = \operatorname{span}(w_1, \ldots, w_k)$ be a $k$-subspace of $V$ with $\dim V = n$, and let $w_1, \ldots, w_k$ be a basis. The **Plücker vector** of $W$ is the decomposable element

$$
[w_1 \wedge \cdots \wedge w_k] \in \mathbb{P}\left(\textstyle\bigwedge^k V\right) \cong \mathbb{RP}^{\binom{n}{k} - 1},
$$

the class of the wedge product up to scalar; it is independent of the basis chosen, up to the nonzero determinant of the change of basis.

**Theorem (Plücker embedding).** The map

$$
\iota : \mathrm{Gr}_k(V) \longrightarrow \mathbb{P}\left(\textstyle\bigwedge^kV\right), \qquad W \longmapsto [w_1 \wedge \cdots \wedge w_k],
$$

is well defined and injective; its image is a closed smooth submanifold, and the map is an embedding. The image is the set of **decomposable** classes, characterised by the **Plücker relations**: for $1 \leq k \leq n$ and indices $i_1, \ldots, i_{k+1}$ and $j_1, \ldots, j_{k-1}$,

$$
\sum_{r=1}^{k+1}(-1)^r p_{i_1 \ldots \widehat{i_r} \ldots i_{k+1}}\, p_{i_r j_1 \ldots j_{k-1}} = 0,
$$

where $p_{i_1\ldots i_k}$ are the coordinates of the class in the basis $e_{i_1}\wedge\cdots\wedge e_{i_k}$.

**Proof sketch.** Injectivity: $W$ is recovered from $[w_1\wedge\cdots\wedge w_k]$ as the set of $v$ with $v \wedge (w_1\wedge\cdots\wedge w_k) = 0$. Well definedness: a change of basis multiplies the wedge by a nonzero scalar, which is the projectivisation. The map is an injective immersion of the compact Grassmannian into the projective space, hence a closed embedding; the Plücker relations, obtained by expanding the identity $w_{k+1}\wedge w_1\wedge\cdots\wedge w_k = 0$ in coordinates, cut out the decomposable classes. $\square$

**Example (lines in $\mathbb{P}^3$).** For $k = 2$, $n = 4$ the Plücker vector has six coordinates $p_{ij}$, $i<j$, and there is a single Plücker relation

$$
p_{12}p_{34} - p_{13}p_{24} + p_{14}p_{23} = 0,
$$

which is the **Klein quadric**, a smooth quadric hypersurface in $\mathbb{RP}^5$. The Grassmannian $\mathrm{Gr}_2(\mathbb{R}^4)$ is therefore a four-dimensional quadric in $\mathbb{RP}^5$, the Klein quadric, whose two rulings are the two families of lines of $\mathbb{RP}^3$ and realise the Klein correspondence between the points of one projective three-space and the lines of another. The relation is verified by expanding the six minors of a $2 \times 4$ matrix: the identity $p_{12}p_{34} - p_{13}p_{24} + p_{14}p_{23} = 0$ is the Laplace expansion of the determinant of a $2\times 2$ matrix with repeated rows. The projective theory of the quadric and of the correspondence is in the article *Projective Geometry*, written in parallel.

**Remark (complex and quaternionic analogues).** The same construction with $\mathbb{C}$ or $\mathbb{H}$ in place of $\mathbb{R}$ gives the complex Grassmannian $\mathrm{Gr}_k(\mathbb{C}^n)$ and the quaternionic Grassmannian $\mathrm{Gr}_k(\mathbb{H}^n)$, of real dimensions $2k(n-k)$ and $4k(n-k)$, each a complex or quaternionic manifold and a symmetric space of compact type; the complex case carries the natural Kähler structure of the article *Kähler Geometry*, written in parallel, whose fundamental form and complex structure are defined there, and the complex Grassmannians are the simplest Kähler symmetric spaces. The real dimensions are computed from $\dim_{\mathbb{R}}\mathbb{K} = 1, 2, 4$ for $\mathbb{K} = \mathbb{R}, \mathbb{C}, \mathbb{H}$ and are $(\dim_{\mathbb{R}}\mathbb{K})k(n-k)$.

## Schubert Cells and the Cohomology

### The Cell Decomposition

**Definition.** Fix a complete flag

$$
0 = V_0 \subseteq V_1 \subseteq V_2 \subseteq \cdots \subseteq V_n = \mathbb{R}^n, \qquad \dim V_i = i .
$$

For a sequence $\lambda = (\lambda_1, \ldots, \lambda_k)$ with $1 \leq \lambda_1 < \cdots < \lambda_k \leq n$, the **Schubert cell** is

$$
e_\lambda = \{W \in \mathrm{Gr}_k(\mathbb{R}^n) : \dim(W \cap V_{\lambda_i}) = i \text{ and } \dim(W \cap V_{\lambda_i - 1}) = i - 1 \text{ for each } i\}.
$$

Its closure $X_\lambda = \bar e_\lambda$, the **Schubert variety**, consists of the $W$ with $\dim(W \cap V_{\lambda_i}) \geq i$ for all $i$.

**Theorem.** The Schubert cells partition the Grassmannian, each $e_\lambda$ is homeomorphic to $\mathbb{R}^{|\lambda|}$ where

$$
|\lambda| = \sum_{i=1}^{k}(\lambda_i - i),
$$

and the cells are the open cells of a CW decomposition whose closures are the Schubert varieties; there is one cell for each $k$-element subset $\lambda$ of $\{1, \ldots, n\}$, so $\binom{n}{k}$ cells in total.

**Proof sketch.** Choose a complete flag adapted to a fixed $W_0$ and put the chart $U_{\lambda_1}$; the condition on the intersections with the flag gives a chain of nested affine spaces; the dimension count is the number of free entries of the matrix of the corresponding projection, which is $\sum_i(\lambda_i - i)$. $\square$

**Corollary (the Poincaré polynomial).** The cells are indexed by the $k$-element subsets, and the generating function of the cell counts by dimension is the **Gaussian binomial coefficient**

$$
P_t(\mathrm{Gr}_k(\mathbb{R}^n)) = \sum_{\lambda} t^{|\lambda|} = \binom{n}{k}_t ,
$$

so with $\mathbb{F}_2$ coefficients the total dimension of the cohomology is $\binom{n}{k}$, and the mod-$2$ Betti numbers are the numbers of cells of each dimension. The Euler characteristic is the value at $t = -1$,

$$
\chi(\mathrm{Gr}_k(\mathbb{R}^n)) = \binom{n}{k}_{t=-1} = \begin{cases} 0, & n \text{ even and } k \text{ odd}, \\ \displaystyle\binom{\lfloor n/2\rfloor}{\lfloor k/2\rfloor}, & \text{otherwise}, \end{cases}
$$

and in particular $\chi(\mathbb{RP}^{n-1}) = 1$ for $n$ odd and $0$ for $n$ even.

**Proof sketch.** The generating function $\sum_\lambda t^{|\lambda|}$, over the $k$-element subsets $\lambda$ of $\{1,\ldots,n\}$, is by definition the Gaussian binomial coefficient $\binom{n}{k}_t$, the generating function of the partitions fitting in a $k \times (n-k)$ box; the evaluation at $t = -1$ is the standard $q \to -1$ evaluation of the Gaussian binomial, which gives the stated case distinction. The projective-space case $k = 1$ is the alternating sum $1 - 1 + 1 - \cdots$ of $n$ cells of dimensions $0, 1, \ldots, n-1$. $\square$

**Example.** For $k = 2$, $n = 4$ the cells have dimensions $0, 1, 2, 2, 3, 4$ and $\chi = 1 - 1 + 2 - 1 + 1 = 2 = \binom{2}{1}$; the integral cohomology has $2$-torsion in degree $3$, so the integral Betti numbers are not the cell counts while the mod-$2$ Betti numbers are.

**Remark (Schubert calculus).** The intersection ring of the Grassmannian is the ring of symmetric polynomials modulo an ideal; the classes of the Schubert varieties form a basis, and the structure constants are the Littlewood–Richardson coefficients. This is the Schubert calculus, the intersection theory of the Grassmannian, and it belongs to the algebraic-geometric side of the corpus and is quoted here as standard; it is the reason the Grassmannian is the universal home of the enumerative problems of linear geometry.

## The Classifying Space

**Theorem.** The Grassmannian is the classifying space of the orthogonal group in the following sense: the tautological bundle $\gamma_k$ over $\mathrm{Gr}_k(\mathbb{R}^n)$ is a rank-$k$ bundle whose associated Stiefel bundle is universal in the limit

$$
\mathrm{Gr}_k(\mathbb{R}^\infty) = \varinjlim_n \mathrm{Gr}_k(\mathbb{R}^n) = BO(k),
$$

the classifying space of rank-$k$ real vector bundles, and for a suitable topology every rank-$k$ real vector bundle over a paracompact base is the pullback of $\gamma_k$ along a classifying map unique up to homotopy.

**Proof sketch.** The tautological bundle over the limit Grassmannian is the universal bundle because the space of $k$-frames in $\mathbb{R}^\infty$ is contractible, a fact of the stable linear algebra; the classification theorem is the bundle theory of *Fibre Bundles, Connections and Curvature*. $\square$

**Corollary.** The characteristic classes of a real vector bundle are the pullbacks of the classes of the universal bundle on $BO(k)$; the Stiefel–Whitney and Pontryagin classes are computed by the cohomology of the Grassmannian, which is why the Schubert cells of the previous section are the computational device for the characteristic classes.

**Theorem (Gauss map).** Let $M \subseteq \mathbb{R}^n$ be a submanifold of dimension $k$. The **Gauss map** $\nu : M \to \mathrm{Gr}_{n-k}(\mathbb{R}^n)$ sending a point to its normal subspace, $\nu(p) = (T_pM)^\perp$, is smooth, and the pullback of the tautological bundle along $\nu$ is the normal bundle of $M$ in $\mathbb{R}^n$, while the pullback of the complement bundle is the tangent bundle.

**Proof.** The tangent space varies smoothly with the point, so the normal subspace does too; the two pullback identifications are the definitions of the bundles involved. $\square$

**Corollary.** The Gauss map is the reason the Grassmannian is the natural home of the extrinsic geometry of submanifolds: the second fundamental form of *Riemannian Geometry* is the derivative of the Gauss map, and the curvature of a submanifold is computed from its Gauss image in the Grassmannian.

## Summary

The Grassmannian $\mathrm{Gr}_k(\mathbb{R}^n)$ is the set of $k$-dimensional subspaces of $\mathbb{R}^n$, and the Stiefel manifold $V_k(\mathbb{R}^n)$ is the set of orthonormal $k$-frames; both are compact smooth manifolds, of dimensions $k(n-k)$ and $nk - k(k+1)/2$. The Grassmannian has the chart description by $k(n-k)$ independent matrix entries of a subspace, the Stiefel manifold is the regular level set $X^TX = I_k$, and the projection from a frame to the subspace it spans is a principal $O(k)$-bundle, whose dimension count gives $\dim V_k = \dim \mathrm{Gr}_k + \dim O(k)$.

The tautological bundle has fibre $W$ over $W$, the complement bundle has fibre $W^\perp$, and the tangent bundle of the Grassmannian is $\operatorname{Hom}(\gamma_k, \gamma_k^\perp)$. The group $O(n)$ acts transitively, so $\mathrm{Gr}_k(\mathbb{R}^n) = O(n)/(O(k)\times O(n-k))$, and the standard metric is the $O(n)$-invariant metric induced from the Euclidean structure of matrices; its geodesics are the orbits of one-parameter subgroups of $O(n)$, its curvature is nonnegative, and the reflection in a subspace is an involutive isometry making the Grassmannian a Riemannian symmetric space of compact type and rank $\min(k, n-k)$. The extreme cases are the projective space at $k = 1$, of constant curvature $+1$, and the orthogonal group at $k = n$.

The Grassmannian embeds in the projective space of the $k$-th exterior power by the Plücker map, whose image is cut out by the Plücker relations; for $k = 2$, $n = 4$ the image is the Klein quadric in $\mathbb{RP}^5$, a single quadratic relation. The Schubert cells defined by a complete flag give a CW decomposition into $\binom{n}{k}$ cells, whose dimension generating function is the Gaussian binomial coefficient $\binom{n}{k}_t$; the mod-$2$ cohomology has total dimension $\binom{n}{k}$, the integral cohomology carries $2$-torsion in odd degrees, and the Euler characteristic is the evaluation $\binom{n}{k}_{t=-1}$, equal to $0$ for $n$ even and $k$ odd and to $\binom{\lfloor n/2\rfloor}{\lfloor k/2\rfloor}$ otherwise. The intersection theory of the Schubert varieties is the Schubert calculus. In the limit the Grassmannian is the classifying space $BO(k)$, so the characteristic classes of real vector bundles are its cohomology classes, and the Gauss map of a submanifold into a Grassmannian identifies the normal and tangent bundles with pullbacks of the tautological and complement bundles. The complex and quaternionic analogues double and quadruple the dimensions and carry the Kähler structure of the sibling article.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{Gr}_k(V)$, $\mathrm{Gr}_k(\mathbb{R}^n)$ | Grassmannian of $k$-subspaces; a compact manifold of dimension $k(n-k)$ |
| $V_k(\mathbb{R}^n)$ | Stiefel manifold of orthonormal $k$-frames; dimension $nk - k(k+1)/2$ |
| $P_W$ | Orthogonal projection onto $W$; $P_W^2 = P_W$, $P_W^T = P_W$ |
| $\pi : V_k(\mathbb{R}^n) \to \mathrm{Gr}_k(\mathbb{R}^n)$ | Stiefel bundle; principal $O(k)$-bundle |
| $\gamma_k$, $\gamma_k^\perp$ | Tautological bundle and orthogonal complement bundle |
| $T\mathrm{Gr}_k \cong \operatorname{Hom}(\gamma_k, \gamma_k^\perp)$ | Tangent bundle |
| $O(n)/(O(k)\times O(n-k))$ | Grassmannian as a homogeneous space |
| $\sigma_W = P_W - P_{W^\perp}$ | Geodesic symmetry; the symmetric space involution |
| rank $\min(k, n-k)$ | Rank of the symmetric space; dimension of a maximal flat |
| $\iota : \mathrm{Gr}_k \to \mathbb{P}(\bigwedge^kV)$ | Plücker embedding; image cut out by the Plücker relations |
| $p_{i_1\ldots i_k}$ | Plücker coordinates in the basis of exterior monomials |
| $p_{12}p_{34} - p_{13}p_{24} + p_{14}p_{23} = 0$ | The Klein quadric, for $k=2$, $n=4$ |
| $e_\lambda$, $X_\lambda$, $|\lambda| = \sum(\lambda_i - i)$ | Schubert cell, Schubert variety, dimension of a cell |
| $\binom{n}{k}_t$, $\chi = \binom{n}{k}_{t=-1}$ | Gaussian binomial; cell-count generating function; Euler characteristic |
| $BO(k) = \mathrm{Gr}_k(\mathbb{R}^\infty)$ | Classifying space of rank-$k$ real bundles |
| $\nu : M \to \mathrm{Gr}_{n-k}(\mathbb{R}^n)$ | Gauss map; $\nu^*\gamma = NM$, $\nu^*\gamma^\perp = TM$ |
| $\mathrm{Gr}_k(\mathbb{K}^n)$ | Complex ($\mathbb{K}=\mathbb{C}$) and quaternionic ($\mathbb{K}=\mathbb{H}$) Grassmannians |



## Further Reading

- John W. Milnor and James D. Stasheff, *Characteristic Classes* (Princeton University Press, 1974), for the Grassmannian as a classifying space and the universal bundles.
- Phillip Griffiths and Joseph Harris, *Principles of Algebraic Geometry* (Wiley, 1978), for the Plücker embedding, Schubert varieties and Schubert calculus.
- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry, Volume II* (Interscience, 1969), for the curvature of homogeneous spaces and the symmetric space structure.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (Academic Press, 1978), for the Grassmannians as symmetric spaces and the rank theory.
- Sigurdur Helgason, *Groups and Geometric Analysis* (Academic Press, 1984), for the invariant metric, the geodesics and the spherical functions on the Grassmannians.
- Sheldon Katz, *Enumerative Geometry and String Theory* (American Mathematical Society, 2006), for the Schubert calculus and its enumerative applications.
- Armand Borel, "Sur la cohomologie des espaces fibrés principaux et des espaces homogènes de groupes de Lie compacts", *Annals of Mathematics* 57 (1953), 115–207, for the cohomology of the Grassmannians and the flag manifolds.
