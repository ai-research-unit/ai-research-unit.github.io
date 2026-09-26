
# __Projective Geometry__

## Introduction

Projective geometry is the geometry of the one-dimensional subspaces of a vector space: the **projective space** $\mathbb{P}(V)$ of a vector space $V$ over a field $K$ has as its points the lines through the origin of $V$, and every linear structure of $V$ — the subspaces, the incidence, the linear maps, the bilinear and quadratic forms — descends to a projective structure. The descent loses the scale and keeps the incidence, and it is exactly the loss that makes the theory a geometry: the affine space embeds in the projective space as the complement of a hyperplane, the parallel lines meet at the points of that hyperplane, the conics and the quadrics are the zero sets of the quadratic forms, and the polarity of a nondegenerate quadric is a duality of the projective space, an incidence-preserving correspondence between the points and the hyperplanes. The present article develops the projective spaces and their coordinates, the collineations and the fundamental theorem, the quadrics and their polarity, and the **Klein correspondence**, the identification of the lines of the projective three-space with the points of a quadric in the projective five-space, which is the projective form of the isomorphism of the groups of the six-dimensional quadratic form with the linear group of the four-dimensional space.

The article belongs to the category of the quadratic forms and the Clifford algebras because the projective geometry of a form is the geometry of its quadric, and because the Klein correspondence is the projective face of the spin groups of this Part: the lines of $\mathbb{P}^3$ are the points of the Klein quadric, the incidence of the lines is the polarity of the quadric, and the group of the quadric is the projective orthogonal group $PO(6)$, whose spin double cover is $\operatorname{Spin}(6) \cong SL(4)$ in the complex case. The specific case of the biquaternion norm form, with its null quadric, its two rulings and its Plücker coordinates, is developed, and the article cites it for the concrete instance of the correspondence. The algebraic topology of the real and complex projective spaces is cited to the topology of this Part, and the article keeps to the projective geometry of the forms.

## Projective Spaces and Homogeneous Coordinates

### The Projective Space of a Vector Space

**Definition.** Let $V$ be a vector space over a field $K$ of dimension $n+1 \geq 2$. The **projective space** $\mathbb{P}(V)$ is the set of the one-dimensional subspaces of $V$,
$$
\mathbb{P}(V) = (V \setminus \{0\})/K^\times ,
$$
the quotient by the action of the multiplicative group by scalar multiplication; its elements are the **points**, and the **projective dimension** of $\mathbb{P}(V)$ is $\dim V - 1 = n$. A point is written $[v]$ for a nonzero vector $v$, and the coordinates of $v$ in a basis of $V$ are the **homogeneous coordinates** of the point, determined up to a common nonzero scalar. The projective space of $K^{n+1}$ is written $\mathbb{P}^n(K)$, or $\mathbb{P}^n$ when the field is understood.

**Proposition.** The projective space $\mathbb{P}(V)$ determines the vector space $V$ up to isomorphism together with its field of scalars: the field is recovered from the incidence geometry of the projective line and the space by the fundamental theorem below, and a semilinear isomorphism $V \to W$ induces a bijection $\mathbb{P}(V) \to \mathbb{P}(W)$ preserving the incidence. A hyperplane of $V$ determines a **projective hyperplane** of $\mathbb{P}(V)$, and the complement of a hyperplane is an **affine chart**
$$
\mathbb{P}(V) \setminus \mathbb{P}(H) \cong \operatorname{Hom}(L, H) \cong K^n ,
$$
where $L$ is a line complementary to $H$, the isomorphism sending a point to its coordinate along $L$; the chart depends on the choice of $H$, and the passage from one chart to another is a projective transformation.

**Proof.** Choose a complement $L$ with $V = H \oplus L$, so that $\dim L = 1$. Every point of $\mathbb{P}(V)$ not contained in $\mathbb{P}(H)$ is the line of a unique vector $l + h$ with $l \in L\setminus\{0\}$, and the assignment of $h/l \in \operatorname{Hom}(L,H) \cong H$ is a bijection onto $H \cong K^n$; a change of the complement or of the hyperplane changes the assignment by a linear fractional expression, which is the projective transformation of the statement. The recovery of the field from the incidence is the fundamental theorem. $\square$

**Example.** For $K = \mathbb{R}$ and $n = 1$ the projective line is the circle of the directions of the plane, the one-point compactification of the affine line; for $n = 2$ the projective plane is the affine plane with the line at infinity added, whose points are the directions of the affine lines; the projective spaces over $\mathbb{C}$ are the compact complex manifolds of the algebraic geometry, and the spaces $\mathbb{RP}^n$, $\mathbb{CP}^n$ of the topology of this Part are the real and complex projective spaces with their quotient topologies.

### Projective Subspaces, Incidence and Duality

**Definition.** A **projective subspace** of $\mathbb{P}(V)$ is the projectivisation $\mathbb{P}(W)$ of a linear subspace $W \subseteq V$; a point lies in the subspace when the corresponding line is contained in $W$, and the **incidence** relation is this containment. The projective subspaces of dimension $0$, $1$, $2$ and $n-1$ are the points, the **lines**, the **planes** and the **hyperplanes**; two subspaces **meet** when their intersection is nonempty, and the join of two subspaces is the projectivisation of the sum, of dimension $\dim \mathbb{P}(W_1) + \dim \mathbb{P}(W_2) - \dim \mathbb{P}(W_1 \cap W_2)$.

**Theorem (the dimension formula and the duality).** The projective subspaces of $\mathbb{P}(V)$ form a lattice under the containment, with the meet the intersection and the join the sum, and the dimension formula
$$
\dim(\mathbb{P}(W_1) \cap \mathbb{P}(W_2)) = \dim\mathbb{P}(W_1) + \dim\mathbb{P}(W_2) - \dim\mathbb{P}(W_1 \cup W_2)
$$
attained in the complementarity sense; the assignment $W \mapsto W^\perp$ of the orthogonal complement with respect to a nondegenerate bilinear form on $V$ reverses the containment and exchanges the meet and the join, the **duality principle**: every true statement about the incidence of the projective subspaces of a fixed dimension remains true when the dimensions are replaced by their complements and the containment is reversed.

**Proof.** The lattice statements are the linear algebra of the subspaces, with the intersection and the sum replacing the linear meet and join, and the dimension formula is the standard formula $\dim(W_1\cap W_2) = \dim W_1 + \dim W_2 - \dim(W_1+W_2)$; the orthogonal complement of a nondegenerate form reverses the containment, $\dim W^\perp = \dim V - \dim W$, and exchanges the sum with the intersection, which is the duality. $\square$

**Example.** In the projective plane $\mathbb{P}^2$ the duality exchanges the points and the lines: the statement that two distinct points determine a unique line is dual to the statement that two distinct lines meet in a unique point; the theorem of Desargues and its dual, and the theorem of Pascal and its dual of Brianchon, are the standard instances of the principle. In the projective three-space the duality exchanges the points and the planes and fixes the lines, and the lines of the space are self-dual, which is the geometric content of the Klein correspondence.

### Coordinates, Frames and the Cross Ratio

**Definition.** A **projective frame** of $\mathbb{P}(V)$ with $\dim V = n+1$ is a set of $n+2$ points in general position, that is, no $n+1$ of them lying in a hyperplane; a frame determines the coordinates of every point uniquely up to a common scalar: the vectors representing the frame form a basis of $V$ together with one linear relation, and the relation fixes the normalisation. For four distinct points of a projective line $\mathbb{P}^1$ the **cross ratio** is the scalar
$$
[a : b : c : d] = \frac{(a-b)(c-d)}{(a-c)(b-d)} ,
$$
computed from any affine coordinates of the four points, and it is independent of the coordinates chosen.

**Theorem.** The group $PGL(V)$ of the projective transformations acts simply transitively on the projective frames, so that any two frames are carried to each other by a unique projective transformation; consequently the cross ratio is the complete invariant of the ordered quadruples of distinct points of a projective line, the group $PGL(2,K)$ acts triply transitively on the line, and the stabiliser of three points is the parametrisation of the fourth by the cross ratio.

**Proof.** A projective transformation is induced by an invertible linear map, and it carries a frame to a frame; conversely two frames determine an invertible map taking the representatives of the first to the representatives of the second, the common scalar of the representatives being fixed by the relation, and the map is unique up to a scalar, which does not change the projective transformation. For the line, the action of $PGL(2,K)$ on the ordered triples of distinct points is transitive, and the cross ratio of a quadruple with three fixed points determines the fourth, since the stabiliser of $0, 1, \infty$ is trivial. $\square$

**Remark.** The cross ratio is the projective invariant of the one-dimensional case , where the same invariant is expressed through the pairings of the null vectors of the Möbius model; the two expressions agree, and the general projective frame of $\mathbb{P}(V)$ is the higher-dimensional analogue of the four points of the projective line.

## Collineations and the Fundamental Theorem

### Projective Maps and Their Classification

**Definition.** Let $V$ and $W$ be vector spaces. A map $f : \mathbb{P}(V) \to \mathbb{P}(W)$ is a **collineation** if it carries the collinear triples of points to collinear triples, that is, if the images of the points of a line lie in a line; a **projective map** is the map induced by a semilinear map $T : V \to W$, that is, an additive map which is linear up to an automorphism $\sigma$ of the field, $T(\lambda v) = \sigma(\lambda)T(v)$, and $f([v]) = [T(v)]$. The group of the projective transformations of $\mathbb{P}(V)$ is the quotient $PGL(V) = GL(V)/K^\times$, and the group of the collineations is the semidirect product $P\Gamma L(V) = PGL(V) \rtimes \operatorname{Gal}(K)$ of the projective transformations with the field automorphisms.

**Theorem (the fundamental theorem of projective geometry).** Let $\dim V \geq 3$ and let $f : \mathbb{P}(V) \to \mathbb{P}(W)$ be a collineation onto a projective space of the same dimension; then $f$ is induced by a semilinear bijection $V \to W$, unique up to a scalar, so that every collineation of a projective space of dimension at least two is a projective map; consequently the collineation group of $\mathbb{P}^n(K)$ is $P\Gamma L(n+1,K) = PGL(n+1,K) \rtimes \operatorname{Gal}(K)$ for $n \geq 2$.

**Proof sketch.** The collineation preserves the collinear triples, and it follows that it carries the lines to the lines and the projective subspaces to the projective subspaces, preserving the incidence and the dimension; choosing a frame and the induced coordinates, the map is described by a family of functions on the field which are additive and multiplicative by the preservation of the collinear triples, so that the functions are the values of a field automorphism $\sigma$ on the common coordinate, and the map is the semilinear map of the statement; the uniqueness of the map up to a scalar is the ambiguity of the representatives. The proof for the planes and the spaces of higher dimension uses the theorem of Desargues, which holds automatically in the dimensions at least three, and the classical argument is in the references. $\square$

**Corollary.** The projective transformations of the projective line are the fractional linear transformations, and the semilinear ones are obtained by composing these with the automorphisms of the field; over a field with no nontrivial automorphism the collineations of the projective spaces of dimension at least two are exactly the projective transformations. Dimension one is the exceptional case in which the fundamental theorem fails: every triple of points of $\mathbb{P}^1$ is collinear, so every bijection preserves the collinearity and the cross ratio, not the semilinearity, is the invariant.

### Correlations and Polarities

**Definition.** A **correlation** of $\mathbb{P}(V)$ is a collineation from $\mathbb{P}(V)$ to the dual projective space of the hyperplanes, that is, an incidence-reversing bijection between the points and the hyperplanes; a correlation is a **polarity** if it is an involution, and the polarity is **nondegenerate** if it is induced by a nondegenerate bilinear form $B$ on $V$, the polar hyperplane of a point $[v]$ being the set of the points $[w]$ with $B(v,w) = 0$. The **polarity** of a nondegenerate quadric of the next section is the polarity of its form, and the projective orthogonal group is the subgroup of the projective group preserving the polarity.

**Proposition.** A nondegenerate bilinear form on $V$ induces a polarity of $\mathbb{P}(V)$, and every polarity of a projective space of dimension at least two with the field of characteristic not two is obtained from a nondegenerate bilinear form up to the composition with a field automorphism; the polarity preserves the incidence in the reversed sense, it sends the points of a subspace to the hyperplanes containing the polar of the subspace, and the fixed points of the polarity are the points of the quadric of the symmetric part of the form.

**Proof sketch.** The polarity of a form is the assignment $[v] \mapsto \ker B(v, \cdot)$, which is well defined because the form is nondegenerate and is a correlation because the assignment is additive and linear on the representatives; the involution property is the symmetry of $B$ up to the transpose, and the fixed points satisfy $B(v,v) = 0$, which is the quadratic condition of the quadric. The converse is the classical theorem that a polarity of a projective space of dimension at least two comes from a bilinear form, with the sesquilinear twist of the field automorphism; the details are in the references. $\square$

## The Projective Geometry of a Quadratic Form

### Quadrics and Their Polarity

**Definition.** Let $q$ be a quadratic form on $V$ with polar form $B$, as in *Quadratic Forms and Polarisation*. The **projective quadric** of $q$ is the zero set
$$
Q = \{[v] \in \mathbb{P}(V) : q(v) = 0\},
$$
the points of the **null cone** of $q$; the quadric is **nondegenerate** if the polar form $B$ is nondegenerate, and its **rank** is the rank of $B$. The **polarity** of the quadric is the polarity of $B$: the polar hyperplane of a point $[p]$ is $[p]^\perp = \{[w] : B(p,w) = 0\}$, the point is on the quadric exactly when it lies in its own polar hyperplane, and the polar hyperplane of a point of the quadric is the **tangent hyperplane** at the point.

**Proposition.** The polarity of a nondegenerate quadric is a bijection between the points and the hyperplanes reversing the incidence; the points of the quadric are the fixed points of the polarity; the tangent hyperplanes at the points of the quadric form the dual quadric; and the subgroup of $PGL(V)$ preserving the quadric is the **projective orthogonal group** $PO(V,q) = O(V,q)/\{\pm 1\}$, which coincides with the subgroup preserving the polarity.

**Proof.** The polarity is a correlation by the previous section, and a point $[p]$ is fixed exactly when $B(p,p) = 0$, which is the condition $q(p) = 0$ in characteristic not two; a projective transformation preserves the quadric exactly when it preserves the form up to a scalar, that is, when its representative lies in the orthogonal group up to the scalars, and the scalars act trivially on the projective space. $\square$

**Theorem (the projective classification).** Over an algebraically closed field every nondegenerate quadric of $\mathbb{P}^n$ is projectively equivalent to the standard one, and every quadric is classified by its rank; over the real field a quadric is classified by the rank and by the signature of the polar form up to the interchange of the positive and the negative parts of the signature, so that the nondegenerate quadrics of $\mathbb{P}^n(\mathbb{R})$ fall into the classes with the signatures $(p,q)$ and $(q,p)$ identified. A nondegenerate quadric of rank $n+1$ is **smooth**, a quadric of lower rank is a cone over a nondegenerate quadric in a smaller projective space with the vertex the projectivised radical, and the quadric is smooth exactly when its polar form is nondegenerate.

**Proof sketch.** Over an algebraically closed field a nondegenerate symmetric form is equivalent to the standard one by the classification of the quadratic forms of *Quadratic Forms and Polarisation*, and a degenerate form is equivalent to a standard form plus zeros, giving the cone structure; over the real field the classification is Sylvester's law of inertia, and the zero set of the form is unchanged by the replacement of $q$ by $-q$, which interchanges the two parts of the signature. The smoothness of the quadric of a nondegenerate form is the regularity of the gradient, and the cone statement is the reduction by the radical. $\square$

**Example (the conics).** For $n = 2$ the projective quadrics are the **conics**. Over $\mathbb{C}$ there is one nondegenerate conic up to the projective transformations; over $\mathbb{R}$ the nondegenerate conics fall into the two classes of the signatures $(3,0)$ and $(2,1)$: the **definite** conics, with no real points, and the **split** conics, with a real oval; a smooth conic in $\mathbb{P}^2$ is a rational curve, parametrised by the pencil of the lines through one of its points, the **rational normal curve** of degree two, and the group preserving the conic is the projective orthogonal group $PO(3)$, which is the split group $PO(2,1) \cong PGL(2,\mathbb{R})$ for the split conic and the compact group $PO(3,\mathbb{R}) \cong SO(3)$ for the definite one. The classical theorems of Pascal and Brianchon are the incidence statements of the conics and their duals.

### Quadrics, Rank One and the Segre Embedding

**Remark.** The rank-one quadrics are the cones over the points and the products of the linear forms: over an algebraically closed field the quadric of rank one in $\mathbb{P}^n$ is a **hyperplane taken with multiplicity two** (the square of a linear form), and the rank-two quadrics are the unions of two hyperplanes. The product of the projective spaces, the **Segre embedding**
$$
\mathbb{P}^{m} \times \mathbb{P}^{n} \longrightarrow \mathbb{P}^{(m+1)(n+1)-1}, \qquad ([u],[v]) \longmapsto [u \otimes v],
$$
has as its image the variety defined by the rank-one condition on the matrices, the **Segre variety**, which for $m = n = 1$ is the quadric surface $\mathbb{P}^1 \times \mathbb{P}^1$ in $\mathbb{P}^3$ with its two rulings; the surface is the model of the Klein quadric in the low-dimensional case and the concrete instance of the rank-one description of the quadrics. The biquaternion case of this construction, with the Segre embedding of $\mathbb{P}^1 \times \mathbb{P}^1$ onto the projective null quadric $Q^2$ of the norm form, the two rulings and the spinor coordinates, is developed, and the general rank-one theory is the content of the present remark.

## The Klein Correspondence

### The Plücker Embedding

**Definition.** Let $V$ be a vector space of dimension four and let $\mathbb{P}(V) = \mathbb{P}^3$ be the projective three-space. For a line $l = \mathbb{P}(U)$ of $\mathbb{P}^3$, with $U$ a two-dimensional subspace of $V$, the **Plücker vector** of $l$ is the decomposable two-vector $p \wedge r \in \Lambda^2V$ determined by a basis $(p,r)$ of $U$, up to a nonzero scalar; the **Plücker embedding** is the map
$$
G(2,V) \longrightarrow \mathbb{P}(\Lambda^2V) = \mathbb{P}^5, \qquad l = [p\wedge r] ,
$$
from the lines of $\mathbb{P}^3$ to the points of the projective five-space, with the **Plücker coordinates** $p_{ij} = x_iy_j - x_jy_i$ the coordinates of the two-vector in the basis $e_i \wedge e_j$ of $\Lambda^2V$.

**Theorem.** The Plücker embedding is injective, its image is the **Klein quadric**
$$
Q_K = \{[\omega] \in \mathbb{P}(\Lambda^2V) : \omega \wedge \omega = 0\},
$$
the set of the decomposable two-vectors up to scale, and in the Plücker coordinates the image is defined by the single relation
$$
p_{01}p_{23} - p_{02}p_{13} + p_{03}p_{12} = 0 .
$$
The Klein quadric is nondegenerate with respect to the form $(\omega, \omega') \mapsto \omega \wedge \omega'$ on $\Lambda^2V$, the form has the Witt index $3$ (the signature $(3,3)$ over the real field), and the group of the quadric is the projective orthogonal group $PO(6)$ of this split form, which is isomorphic to $PGL(V) = PGL(4)$ by the identification of the linear transformations of $V$ with the orthogonal transformations of $\Lambda^2V$.

**Proof sketch.** The linear map $\Lambda^2 V \to K$ given by $\omega \wedge \omega'$ paired with the volume form of $V$ is a nondegenerate symmetric bilinear form of Witt index $3$, and a two-vector is decomposable if and only if it is isotropic for the form, which is the relation $\omega \wedge \omega = 0$; the single Plücker relation is the expansion of the decomposability condition in the coordinates. The group $GL(V)$ acts on $\Lambda^2V$ preserving the form, and the induced map $PGL(V) \to PO(6)$ is an isomorphism because the two groups have the same dimension and the same centre up to the scalars; the details are in the references. $\square$

### The Lines of $\mathbb{P}^3$ and the Incidence

**Theorem (the Klein correspondence).** The Klein quadric is the projective geometry of the lines of $\mathbb{P}^3$: the points of the quadric are the lines, and the two families of the maximal projective subspaces of the quadric (the **generators**, of dimension two, the planes of the quadric) correspond respectively to the points and to the planes of $\mathbb{P}^3$; through a point of $\mathbb{P}^3$ there passes the plane of the quadric consisting of the lines through the point (a generator of the first family), and inside a plane of $\mathbb{P}^3$ there lies the plane of the quadric consisting of the lines in the plane (a generator of the second family). Two lines of $\mathbb{P}^3$ meet if and only if the corresponding points of the Klein quadric are **polar**,
$$
\omega \wedge \omega' = 0 ,
$$
and the incidence geometry of the lines of $\mathbb{P}^3$ is therefore the polarity of the Klein quadric.

**Proof sketch.** The lines through a point of $\mathbb{P}^3$ are parametrised by the lines of the quotient space $V/\mathbb{R}v$, a projective plane, and the corresponding two-vectors form a totally isotropic plane of the quadric because they share the factor $v$; the lines in a plane of $\mathbb{P}^3$ are the lines of a two-dimensional quotient, also a projective plane, and they form the other family. For the polarity, two decomposable two-vectors $\omega = p\wedge r$ and $\omega' = s\wedge t$ satisfy $\omega \wedge \omega' = \det(p,r,s,t)$ up to a constant, which vanishes exactly when the four vectors are linearly dependent, that is, when the two lines span at most a three-dimensional subspace and therefore meet. The identification is verified by explicit computation; the details and the classical statements are in the references. $\square$

**Example.** For $V = \mathbb{R}^4$ the Plücker form of the Klein quadric has signature $(3,3)$, and the quadric is a smooth four-dimensional quadric in the five-dimensional projective space; the maximal isotropic subspaces of the form are three-dimensional in $\Lambda^2V$, so the generators of the quadric are projective planes, and each family is parametrised by the projective three-space of the points, respectively of the planes, of $\mathbb{P}^3$. The spin isomorphism of the quadric is $\operatorname{Spin}(6) \cong SL(4,\mathbb{C})$ in the complex case, the double cover of $PO(6) \cong PGL(4)$, and the two families of the generators are the two **half-spin** representations of $\operatorname{Spin}(6)$, which are the defining representation of $SL(4)$ and its dual; the triality of the spin representations of $\operatorname{Spin}(8)$ is the higher analogue of the same correspondence, and the Klein quadric is the basic case of the projective realisation of the spinors.

**Example (the finite field).** Over the field $\mathbb{F}_2$ the geometry is degenerate but the counts remain and they verify the correspondence: the projective space $\mathbb{P}^3(\mathbb{F}_2)$ has $15$ points and
$$
\binom{4}{2}_2 = \frac{(2^4-1)(2^3-1)}{(2^2-1)(2-1)} = 35
$$
lines, each line with $q+1 = 3$ points; the Plücker embedding sends the $35$ lines to the $35$ points of the Klein quadric in $\mathbb{P}^5(\mathbb{F}_2)$, and the computation of the quadric points by the Plücker relation reproduces the number $35 = (q^2+1)(q^2+q+1)$ of the lines; the incidence of the lines is the polarity of the quadric, verified by the explicit computation over a field of odd characteristic, where the pairing $\omega\wedge\omega'$ distinguishes the dependent from the independent quadruples.

## Summary

A **projective space** $\mathbb{P}(V)$ of dimension $n$ over a field $K$ is the set of the one-dimensional subspaces of a vector space $V$ of dimension $n+1$, with the **homogeneous coordinates** determined up to a common scalar; the **projective subspaces** are the projectivisations of the linear subspaces, with the incidence, the meet and the join, and the dimension formula; the complement of a hyperplane is the **affine chart**, and the **duality** exchanges the meet and the join through the orthogonal complement with respect to a nondegenerate form. The **cross ratio** of four points of a projective line is the complete invariant of the quadruples, the group $PGL(V)$ acts simply transitively on the **projective frames** and the group of the collineations of a projective space of dimension at least two is $P\Gamma L(V) = PGL(V) \rtimes \operatorname{Gal}(K)$ by the **fundamental theorem of projective geometry**, every collineation being induced by a semilinear map. The **projective quadric** of a quadratic form is its null cone in $\mathbb{P}(V)$; the **polarity** of a nondegenerate quadric is the polarity of its polar form, a bijection between the points and the hyperplanes with the points of the quadric as the fixed points and the tangent hyperplanes as the polars, the group of the quadric is the **projective orthogonal group** $PO(V,q)$, and the projective classification of the quadrics is by the rank over an algebraically closed field and by the rank and the signature up to interchange over the real field. The **Klein correspondence** identifies the lines of $\mathbb{P}^3$ with the points of the **Klein quadric** $\{[\omega] : \omega\wedge\omega = 0\}$ in $\mathbb{P}^5$, a nondegenerate quadric of the form $\omega\wedge\omega'$ and signature $(3,3)$ over $\mathbb{R}$, defined in the **Plücker coordinates** by $p_{01}p_{23}-p_{02}p_{13}+p_{03}p_{12} = 0$; the points and the planes of $\mathbb{P}^3$ correspond to the two families of the generators of the quadric, two lines of $\mathbb{P}^3$ meet exactly when the corresponding points are polar, and the isomorphism $PO(6) \cong PGL(4)$ has the spin double cover $\operatorname{Spin}(6) \cong SL(4,\mathbb{C})$, with the two families of the generators as the two half-spin representations.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$ | Coefficient field of $V$ |
| $\mathbb{F}_q$ | Finite field of $q$ elements; $q = p^k$ |
| $\mathbb{P}(V)$, $\mathbb{P}^n$ | Projective space; points are the lines through $0$ |
| $[v]$ | Point of $\mathbb{P}(V)$; homogeneous coordinates up to scale |
| $\mathbb{P}(W)$ | Projective subspace; $W$ a linear subspace |
| $PGL(V)$, $P\Gamma L(V)$ | Projective and collineation groups |
| $[a:b:c:d]$ | Cross ratio of four points of a projective line |
| polarity | Correlation from the points to the hyperplanes; $[v] \mapsto \ker B(v,\cdot)$ |
| $Q = \{[v] : q(v)=0\}$, $PO(V,q)$ | Projective quadric and its projective orthogonal group |
| $(p,q)$ signature | Projective classification over $\mathbb{R}$ up to interchange |
| Segre embedding | $\mathbb{P}^m \times \mathbb{P}^n \to \mathbb{P}^{(m+1)(n+1)-1}$, $([u],[v]) \mapsto [u\otimes v]$ |
| $p_{ij} = x_iy_j - x_jy_i$ | Plücker coordinates of a line of $\mathbb{P}^3$ |
| $Q_K$, $\omega\wedge\omega=0$ | Klein quadric in $\mathbb{P}^5$; lines of $\mathbb{P}^3$ |
| $\omega\wedge\omega' = 0$ | Polarity of the Klein quadric; incidence of the lines |
| $PO(6) \cong PGL(4)$, $\operatorname{Spin}(6)\cong SL(4,\mathbb{C})$ | Group of the split Klein quadric and its spin cover; the split real form is $\operatorname{Spin}(3,3)\cong SL(4,\mathbb{R})$ |
| $\binom{n}{k}_q$ | Gaussian binomial; number of $k$-subspaces of $\mathbb{F}_q^n$ |



## Further Reading

- Reinhold Baer, *Linear Algebra and Projective Geometry* (Academic Press, 1952), for the fundamental theorem of projective geometry and the correlations.
- Jean Dieudonné, *La géométrie des groupes classiques* (Springer, 1955), for the projective orthogonal groups and the classification of the forms.
- H. S. M. Coxeter, *Projective Geometry* (Springer, second edition, 2003), for the projective spaces, the coordinates, the conics and the classical theorems.
- Phillip Griffiths and Joseph Harris, *Principles of Algebraic Geometry* (Wiley, 1978), for the quadrics, the Segre embeddings and the Klein correspondence.
- Felix Klein, "Zur Theorie der Liniencomplexe des ersten und zweiten Grades", *Mathematische Annalen* 2 (1870), 198–226, for the Klein correspondence and the lines of the projective three-space.
- Joe Harris, *Algebraic Geometry: A First Course* (Springer, 1992), for the quadrics, the generators and the spin representations in the projective language.
