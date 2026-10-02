
# __The Projection Operator__

## Introduction

A projection of a projective space is the map that sends a point along the lines through a fixed centre until they meet a fixed figure, and it is the one-sided operator of the projective geometry: the whole map is determined by one datum, the centre, just as a left multiplication of a group is determined by one parameter. The projection is not an operator of the projective group, since it is neither everywhere defined nor injective; it is an **idempotent** of the projective geometry, a map whose square is itself, and the article treats it in that capacity. The linear model is the projection of a vector space onto a complement of a subspace, whose matrix is an idempotent, and the projective projection is its projectivisation.

The article develops the linear projection operator and its decomposition, the central projection of a projective space and its domain, the **perspectivity** between two figures of the same dimension, and the one-sided algebra that the projections form: the order by the inclusion of the kernels, the action of the projective group on the set of the projections, and the matrix of an idempotent. It closes with the harmonic conjugation and the complete quadrangle, in which the projection of the projective line is the classical construction of the fourth harmonic point.

The article assumes *Projective Geometry* for the projective space, its subspaces, the join and the meet, the incidence and the fundamental theorem; *Operators on a Projective Space* for the operator group $PGL(V)$, the two-sided sandwich and the action on the frames; and *Vector Spaces* for the linear projections and the decomposition of a vector space as a direct sum. The projective projection is a rational map, and the general theory of such maps is Part II algebraic geometry; the article names it and defers its treatment. No distance and no form is introduced, and no physics is invoked.

## The Linear Projection Operator

### Definition and the Direct Sum Decomposition

**Definition.** Let $V$ be a vector space over a field $K$ and let $U, W \subseteq V$ be subspaces with

$$
V = U \oplus W .
$$

The **linear projection** onto $W$ along $U$ is the linear map

$$
P : V \longrightarrow V, \qquad P(u + w) = w \quad \text{for } u \in U,\ w \in W ;
$$

equivalently it is the unique linear map with $P|_W = \mathrm{id}_W$ and $\ker P = U$.

**Proposition.** The linear projection $P$ satisfies

$$
P^2 = P , \qquad \operatorname{im} P = W , \qquad \ker P = U , \qquad V = \ker P \oplus \operatorname{im} P ,
$$

and conversely every linear map $P$ with $P^2 = P$ is the projection onto its image along its kernel; the map is idempotent rather than involutive, it is the identity on its image and zero on its kernel, and it is diagonalisable with eigenvalues $0$ and $1$.

**Proof.** For $v = u + w$ the definition gives $P(v) = w$ and hence $P(P(v)) = P(w) = w = P(v)$; the image is $W$ and the kernel is $U$, and the sum is direct by the hypothesis. Conversely, if $P^2 = P$ then every $v$ is written $v = (v - Pv) + Pv$ with $Pv \in \operatorname{im}P$ and $v - Pv \in \ker P$, so $V = \ker P + \operatorname{im}P$, the two meet at $0$ because $P$ is the identity on its image, and $P$ is the projection along its kernel onto its image. The eigenvalues of an idempotent satisfy $\lambda^2 = \lambda$, so they lie in $\{0,1\}$, and the two eigenspaces are the kernel and the image.

**Corollary (the matrix of a projection).** Choose a basis of $V$ adapted to the decomposition $V = U \oplus W$; then the matrix of $P$ is block diagonal,

$$
P = \begin{pmatrix} 0 & 0 \\ 0 & I_r \end{pmatrix} ,
$$

where $r = \dim W$; over a field in which the idempotent equation is reducible every idempotent matrix is conjugate to this form, and the trace of $P$ is the rank, $\operatorname{tr} P = r$.

**Proof.** In the adapted basis the first $\dim U$ coordinates are sent to zero and the last $r$ coordinates are fixed, which is the displayed block matrix; two idempotent matrices are conjugate exactly when they have the same rank, and the trace is invariant and equals $r$ because the eigenvalues of an idempotent are $0$ and $1$.

**Remark.** The projection is not invertible when both $U$ and $W$ are nonzero, so it is not an operator of the projective group and not a point of $GL(V)$; it lies in the algebra $\operatorname{End}_k(V)$ of all linear operators, of which the projective group is the unit group modulo the scalars. The one-sided name records that the datum is the direct sum decomposition, and that the projection is an element of the algebra of operators rather than a unit of the group.

## The Central Projection of a Projective Space

### Definition by the Join

**Definition.** Let $U \subseteq V$ be a subspace and let $W \subseteq V$ be a complement, $V = U \oplus W$. The **central projection** with centre $U$ onto $W$ is the map

$$
\pi_U : \mathbb{P}(V) \setminus \mathbb{P}(U) \longrightarrow \mathbb{P}(W) , \qquad
\pi_U([v]) = \bigl(\mathbb{P}(U) + [v]\bigr) \cap \mathbb{P}(W) ,
$$

which sends the point $[v]$ to the point where the join of $[v]$ and the centre $\mathbb{P}(U)$ meets the target $\mathbb{P}(W)$; the join meets $\mathbb{P}(W)$ in exactly one point because $V = U \oplus W$.

**Proposition.** The central projection is well defined, and it is the projectivisation of the linear projection $P$ onto $W$ along $U$ in the sense that

$$
\pi_U([v]) = [P(v)] ;
$$

it is defined exactly on the complement of $\mathbb{P}(U)$, it is surjective onto $\mathbb{P}(W)$, and its fibres are the projective subspaces $\mathbb{P}(U + Kv)$ through the centre.

**Proof.** If $v$ and $\lambda v$ represent the same point then $P(\lambda v) = \lambda P(v)$ represents the same point, so $\pi_U$ is well defined; the join of $[v]$ and the centre consists of the points $[\lambda v + u]$, and its intersection with $\mathbb{P}(W)$ is the single point $[P(v)]$, which proves the formula; the fibres are the joins with the centre, and the map is onto because $P$ is onto $W$.

**Remark.** The projection is neither defined on the centre nor injective on the rest, and it is therefore not a collineation of the projective space; it is a **rational map**, regular off the centre. The general theory of the rational maps of projective varieties is Part II algebraic geometry, and the present article keeps the elementary case of the projection of a projective space.

### The Cases of the Plane and the Line

**Example.** Let $\dim V = 3$ and let the centre be a point $c = [u]$ and the target a line $\ell = \mathbb{P}(W)$ not containing $c$, so that $V = Ku \oplus W$. The projection $\pi_c$ sends a point $p \neq c$ to the intersection of the line $cp$ with $\ell$; it is the classical central projection of the projective plane from a point onto a line, it is surjective onto $\ell$, and its fibres are the lines through $c$ other than the centre.

**Example.** In the plane with coordinates $[x_0 : x_1 : x_2]$ let the centre be $c = [0:0:1]$ and let the target be the line $x_2 = 0$; then

$$
\pi_c([x_0 : x_1 : x_2]) = [x_0 : x_1 : 0] ,
$$

so the projection is the rational map that forgets the last coordinate, its indeterminacy locus is the centre, and it is the projectivisation of the coordinate projection of $K^3$ onto the plane $x_2 = 0$ along the $x_2$-axis.

**Proof.** The join of $c$ and $[x_0:x_1:x_2]$ is the line of the points $[s x_0 : s x_1 : t]$, and its intersection with $x_2 = 0$ is the point $[x_0:x_1:0]$ when $(x_0,x_1) \neq (0,0)$; the formula is the projectivisation of the coordinate projection computed in the chosen basis.

## The Perspectivity

### Definition

**Definition.** Let $X = \mathbb{P}(U_1)$ and $Y = \mathbb{P}(U_2)$ be two projective subspaces of the same dimension, and let $C = \mathbb{P}(U)$ be a centre disjoint from both, with

$$
V = U \oplus U_1 = U \oplus U_2 .
$$

The **perspectivity** from $X$ to $Y$ with centre $C$ is the map carrying $p \in X$ to the point in which the join of $p$ and $C$ meets $Y$; it is the restriction of a central projection, and its inverse is the perspectivity from $Y$ to $X$ with the same centre.

**Proposition.** A perspectivity is a projectivity between the two figures, induced by the restriction of the linear projection from $U_1$ to $U_2$ along $U$; a perspectivity of a hyperplane onto itself with a centre not contained in it is a projectivity with a hyperplane of fixed points, and it is the identity exactly when the centre is disjoint from the hyperplane in the projective sense.

**Proof.** The map is linear in the coordinates and bijective between the two figures, hence a projectivity; the fixed points of a perspectivity of a hyperplane onto itself are the points whose joins with the centre meet the hyperplane at the point itself, and the statement about the identity follows. The classical construction and the fundamental perspectivity theorem are in *Projective Geometry*.

### Desargues and the Generation of the Projective Group

**Theorem (the theorem of Desargues).** Two triangles are in perspective from a point if and only if the three intersections of their corresponding sides are collinear; in the projective plane the theorem is a statement about a central projection and the incidence of the two triangles, and it holds without exception in the projective plane, while in the affine plane it fails for the parallel case.

**Proof.** In homogeneous coordinates two perspective triangles are the images of each other under the central projection from the common vertex, and the intersections of the corresponding sides are the points where the two triangles meet the axis of the projection, hence are collinear; the converse is the construction of the projection from the collinearity. The proof is in *Projective Geometry*.

**Theorem.** Every projectivity of a projective line is the composite of at most three perspectivities, and more generally the projective group is generated by the central projections between figures of the same dimension.

**Proof.** A projectivity of the line is determined by the images of three points, and two pairs of corresponding points may be matched by a perspectivity; composing the perspective maps that match the successive pairs expresses the given projectivity as a composite of three, and the statement for the higher-dimensional figures follows by induction on the dimension and the fundamental theorem.

**Remark.** The perspectivity is thus the one-sided generator of the two-sided projective group: the projections are not themselves projectivities of the whole space, and their composites generate the group. This is the operator-theoretic form of the classical theorem that the projective transformations are products of the perspectives, and it is the reason the projection is placed in the one-sided layer of the category.

## The One-Sided Algebra of the Projections

**Definition.** For a fixed target $W$ of a vector space $V$, the projections onto $W$ along the various complements $U$ are the elements of the set

$$
\mathcal{P}(W) = \{P \in \operatorname{End}_k(V) : P^2 = P,\ \operatorname{im} P = W\} .
$$

The **kernel** and the **image** of a projection are the two figures it determines, and the projections onto $W$ are ordered by the inclusion of their kernels.

**Proposition.** The map sending a projection to its kernel is a bijection from $\mathcal{P}(W)$ onto the set of the complements of $W$ in $V$; two projections with the same image are equal exactly when their kernels are equal, and the set of the projections of $V$ is in bijection with the set of the ordered pairs of complementary subspaces.

**Proof.** The projection with a given kernel $U$ and image $W$ is unique, since it is determined on $U$ and on $W$; conversely a projection determines its kernel and its image, and the direct sum decomposition holds. The statement is the elementary decomposition theorem of a vector space, cited to *Vector Spaces*.

**Proposition.** The projective group acts on the set of the projections by the sandwich

$$
P \longmapsto [A]\,P\,[A]^{-1} ,
$$

the action preserves the rank, the orbit of a projection is the set of the projections with the same rank, and the stabiliser of a projection is the subgroup of $PGL(V)$ preserving its kernel and its image.

**Proof.** Conjugation by an invertible map carries an idempotent to an idempotent, carries the kernel and the image to their images under the conjugation, and preserves the rank; two projections of the same rank are conjugate because their kernels and their images have the same dimension and may be matched by an invertible map. The action is the two-sided action of the projective group restricted to the idempotents.

**Corollary (the trace and the rank).** The rank of a projection is its trace, and the trace is invariant under the sandwich action; for the projectivisation the dimension of the target figure is $\operatorname{tr} P - 1$, so the trace is the numerical invariant of a projection under the projective group.

## Projections and Harmonic Conjugation

**Definition.** Let $a, b \in \mathbb{P}^1(K)$ be two distinct points of the projective line and let $c$ be a third, distinct from both; the **harmonic conjugate** of $c$ with respect to the pair $(a,b)$ is the point $d$ with cross ratio

$$
[a : b : c : d] = -1 ,
$$

and the assignment $c \mapsto d$ is the **harmonic involution** of the line with respect to the pair, the projective involution fixing $a$ and $b$.

**Proposition.** The harmonic involution is realised by the projection of the complete quadrangle: for a complete quadrangle whose two diagonal points are $a$ and $b$ and whose remaining two diagonal points are joined by the diagonal line, the projections of the two remaining vertices from the third diagonal point give the pair $(c,d)$ harmonic with respect to $(a,b)$, and the construction depends only on the incidence and not on a form.

**Proof.** Set $a = 0$ and $b = \infty$ by a projectivity, so that the complete quadrangle in these coordinates has the four vertices $0, \infty, 1, \lambda$; the fourth harmonic point of $1$ with respect to $0, \infty$ is $-1$, and the computation of the cross ratio gives the value $-1$. The incidence construction and the invariance of the cross ratio are in *Projective Geometry*.

**Remark.** The harmonic involution is the boundary form of the reflection of the projective line, and it is the operator that *The Möbius Transformation as an Operator* classifies among the involutions; the projection construction that produces it is the one-sided operator of the present article composed with itself, and the composite is the involution. This is the point at which the one-sided projective operators and the two-sided Möbius operators meet.

## Summary

A projection is the idempotent operator of a vector space or of a projective space determined by a centre and a complement: the linear projection onto $W$ along $U$ satisfies $P^2 = P$, has image $W$ and kernel $U$, and its matrix in an adapted basis is the block idempotent $\operatorname{diag}(0,I_r)$ with trace the rank $r$. Its projectivisation is the central projection $\pi_U([v]) = [P(v)]$, defined off the centre, surjective onto $\mathbb{P}(W)$, with the joins through the centre as fibres; it is a rational map and not a collineation. The restriction of a central projection to a pair of complementary figures is a **perspectivity**, a projectivity between them, and the perspectivities generate the projective group, with the theorem of Desargues as the incidence statement. The projections onto a fixed target form the set $\mathcal{P}(W)$ of the idempotents of $\operatorname{End}_k(V)$ with that image, in bijection with the complements of $W$, and the projective group acts on them by the sandwich $P \mapsto [A]P[A]^{-1}$ preserving the rank; the trace is the invariant of the action. On the projective line the projection of the complete quadrangle gives the harmonic conjugation, the involution with cross ratio $-1$, which is the boundary form of the reflection.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $V = U \oplus W$ | Direct sum decomposition of the vector space |
| $P(u+w) = w$ | Linear projection onto $W$ along $U$ |
| $P^2 = P$, $\ker P = U$, $\operatorname{im}P = W$ | Idempotent, kernel and image of the projection |
| $\operatorname{diag}(0,I_r)$ | Matrix of a projection in an adapted basis, rank $r$ |
| $\operatorname{tr} P = r$ | Trace equals rank |
| $\pi_U([v]) = [P(v)]$ | Central projection with centre $\mathbb{P}(U)$ |
| $\mathcal{P}(W)$ | Projections with image $W$ |
| perspectivity | Projectivity between two figures from a common centre |
| $[a:b:c:d] = -1$ | Harmonic conjugation, cross ratio minus one |
| harmonic involution | Projective involution fixing the pair and exchanging the conjugates |
| $P \mapsto [A]P[A]^{-1}$ | Sandwich action of the projective group on the projections |

## Further Reading

- H. S. M. Coxeter, *Projective Geometry*, 2nd ed. (Springer, 2003), for the central projection, the perspectivity and the complete quadrangle.
- Reinhold Baer, *Linear Algebra and Projective Geometry* (Academic Press, 1952), for the projections and the perspectivities of a projective space.
- Robin Hartshorne, *Foundations of Projective Geometry* (Benjamin, 1967), for the incidence theorems and the generation of the projective group.
- Paul R. Halmos, *Finite-Dimensional Vector Spaces*, 2nd ed. (Van Nostrand, 1958), for the idempotent operators and the direct sum decompositions.
- Joseph J. Rotman, *Advanced Modern Algebra*, 3rd ed. (American Mathematical Society, 2015), for the projections, the idempotents and the module decompositions.
