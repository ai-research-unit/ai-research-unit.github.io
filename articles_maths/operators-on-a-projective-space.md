
# __Operators on a Projective Space__

## Introduction

A projective space is the geometry of the one-dimensional subspaces of a vector space, and its operators are the invertible transformations of that geometry: the **projectivities**, the maps induced by the invertible linear maps of the vector space up to a scalar, together with the semilinear maps when the field carries an automorphism. The article reads the projective space as an object of this Part and asks what its operators are, how they compose, and what figures of the projective space they act on. The answer to the first question is the quotient $PGL(V) = GL(V)/K^\times$, the group of the operators, and the action of $GL(V)$ on the projective space is the structure from which the quotient is read; the kernel of the action is the scalars, and the exact sequence of the scalars is the one datum that distinguishes the operator group from the linear group it comes from.

The article develops the projective space briefly, to fix the objects the operators act on and to state what it cites; it then defines the operators as the classes of invertible linear maps, proves that the assignment is well defined and that composition descends to the classes, and identifies the operator group with the projective general linear group. It treats the two-sided reading of that group — the left and right translations and the sandwich, which are the two-parameter operators of the structure — the collineations and the fundamental theorem, the action on the projective subspaces and on the frames, the case of the projective line in which the operators are the fractional linear transformations, and the action on the quadrics of a form, where the operators preserving a figure form the projective orthogonal group. The involutions among the operators and the order of a projectivity close the article.

The article assumes *Projective Geometry* for the projective space, its coordinates, its subspaces, the incidence and the duality, and for the fundamental theorem and the cross ratio; the bilinear and quadratic forms, their quadrics and their polarities are Part II objects, and the article names them and reads the figures they cut out, as the boundary test of this Part requires. The group-theoretic structure of the classical groups is cited to *List of Projective Geometric Groups*, and the placement of the projective group among the geometries of a group is *Transformation Groups and the Erlangen Program*, later in this Part. The article introduces no distance and no form of its own, and no physics is invoked.

## The Projective Space and the Operators on It

### The Point Set and Its Subspaces

**Definition.** Let $V$ be a vector space of dimension $n+1 \geq 2$ over a field $K$. The **projective space** is the quotient

$$
\mathbb{P}(V) = (V \setminus \{0\})/K^\times ,
$$

its points are the lines through the origin, and a point is written $[v]$ for a nonzero vector $v$; the **homogeneous coordinates** of $[v]$ are the coordinates of $v$, determined up to a common nonzero scalar. The **projective subspaces** are the projectivisations $\mathbb{P}(W)$ of the linear subspaces $W \subseteq V$, and the incidence, the meet and the join, and the dimension formula are those of *Projective Geometry*. A **frame** is a set of $n+2$ points no $n+1$ of which lie in a hyperplane, and it determines the coordinates of every point up to one scalar.

**Definition.** An **operator on the projective space** is a bijection of $\mathbb{P}(V)$ that preserves the incidence, that is, a map carrying the projective subspaces to the projective subspaces of the same dimension; such a map is a **collineation**. The operators form a group under composition, written $\operatorname{Aut}(\mathbb{P}(V))$, and the article calls its elements the operators of the projective space to match the operator layer of a category.

The name records the intent and not a new structure: the operators of the projective space are the maps that preserve the figure it is, and they are the motions of this geometry in the sense of Klein's programme, in which a geometry is the study of the invariants of its operator group.

### The Action of the General Linear Group

**Proposition.** Every invertible linear map $T \in GL(V)$ induces a collineation of $\mathbb{P}(V)$ by

$$
[T]([v]) = [T(v)] ,
$$

the assignment is well defined on the points, and it is compatible with composition, $[T_1][T_2] = [T_1T_2]$; the induced map depends on $T$ only through its class modulo the scalars, since the scalar maps act trivially on the projective space.

**Proof.** If $v$ and $\lambda v$ represent the same point then $T(\lambda v) = \lambda T(v)$ represents the same point as $T(v)$, so $[T]$ is well defined; if $T_1$ and $T_2$ agree on every line through the origin then $T_2^{-1}T_1$ fixes every line, and a linear map fixing every line is a scalar, so the induced map depends only on the class of $T$ in $GL(V)/K^\times$. The compatibility with composition is the associativity of the linear composition, and the invertibility of $T$ makes $[T]$ a bijection preserving the subspaces.

**Definition.** The **projective general linear group** is the quotient

$$
PGL(V) = GL(V)/K^\times ,
$$

a group of operators on $\mathbb{P}(V)$; the **projective special linear group** is $PSL(V) = SL(V)/(SL(V)\cap K^\times)$, the image of the determinant-one group, and it is a subgroup of $PGL(V)$ of index the group $K^\times/(K^\times)^{n+1}$ of the power classes.

**Theorem (the central extension).** The projection $GL(V) \to PGL(V)$ has kernel the scalars $K^\times$ acting by the nonzero scalar multiplications, and it sits in the exact sequence

$$
1 \longrightarrow K^\times \longrightarrow GL(V) \longrightarrow PGL(V) \longrightarrow 1 ,
$$

so that $PGL(V)$ is the quotient of $GL(V)$ by its centre $K^\times$; the same sequence with $SL(V)$ in place of $GL(V)$ has kernel the group of scalars of determinant one, which is the group of the $(n+1)$-th roots of unity in $K$.

**Proof.** The kernel is the set of invertible linear maps inducing the identity on every line, which is $K^\times$ by the argument of the proposition; the statement for $SL(V)$ is the restriction of the sequence, whose kernel is the scalar matrices of determinant one.

**Remark.** The centre is the whole kernel, and this is the reason the operator group of a projective space is a quotient and not a subgroup of $GL(V)$: the scalars are operators on the vector space and the identity on the projective space, so they are invisible to the figure and are divided out. The quotient is the first place in this Part where an operator is genuinely a class rather than a map, and every statement about the operators is a statement about the classes.

## The Two-Sided Reading

### The Left and Right Translations

**Definition.** The group $PGL(V)$ acts on itself by the **left translation** $[T] \mapsto [A][T]$ and by the **right translation** $[T] \mapsto [T][B]$, for $[A], [B] \in PGL(V)$, and the two actions commute; the **sandwich** is the two-parameter operator

$$
\Theta_{[A],[B]}([T]) = [A]\,[T]\,[B] .
$$

The order of the two parameters matters, and the sandwich with $[B] = [A]^{-1}$ is the **conjugation** $[T] \mapsto [A][T][A]^{-1}$, the inner automorphism of the projective group.

**Proposition.** The sandwich operators form a group isomorphic to the quotient of $PGL(V)\times PGL(V)$ by the diagonal copy of the centre of $PGL(V)$, and they are exactly the operators on $PGL(V)$ given by the two-sided multiplication; the inner automorphisms are the sandwiches with the second parameter the inverse of the first.

**Proof.** The sandwich depends on the pair $([A],[B])$, and two pairs give the same operator on the group exactly when they differ by a central element in both coordinates, which is the stated quotient; the associative law and the inverses are read from the group law, and the conjugation statement is the substitution $[B] = [A]^{-1}$.

**Remark.** The projective group is the operator group of a flag geometry and not of a symmetric space, so its sandwich has two genuinely independent parameters; the inner automorphisms are the one-parameter part, and the left and right translations are the two one-sided boundary pieces. This is the operator reading of the projective group as the group of the projective space and of the projective lines it contains, where the left translations move the flags and the right translations move the coordinate frames.

### The Action on Frames

**Theorem.** The group $PGL(V)$ acts simply transitively on the projective frames of $\mathbb{P}(V)$: every two frames are carried to each other by a unique element of $PGL(V)$. Consequently the frames are the principal homogeneous space of the operator group, and the coordinates that a frame assigns are unique.

**Proof.** A projective frame is the image of a basis together with one relation; two frames determine an invertible linear map carrying the representative of the first basis to the representative of the second, the common scalar being fixed by the relation, and the map is unique up to a scalar, which is the identity in $PGL(V)$. The classical statement is in *Projective Geometry*, and the operator form is the identification of the frame as the torsor under the operator group.

**Corollary.** The operator group is of dimension $n^2 + 2n$ as a group of transformations for $\dim V = n+1$: a projective transformation is determined by the images of $n+2$ points in general position, three of which may be normalised, leaving $n^2 + 2n$ parameters, equal to $\dim GL(V) - 1 = (n+1)^2 - 1$.

**Proof.** A frame has $n+2$ points, each contributing $n$ independent coordinates after the normalisation of a projective point; the free normalisation of three points on the line accounts for the three scalars of the stabiliser of a frame, and the count is the dimension of $GL(V)$ less the dimension of the scalars.

## Collineations and the Fundamental Theorem

**Definition.** A **semilinear** map $T : V \to V$ is an additive bijection for which there is a field automorphism $\sigma$ of $K$ with $T(\lambda v) = \sigma(\lambda)T(v)$, and it induces a collineation, again written $[T]$, of the projective space. The group of the semilinear invertible maps modulo the scalars is

$$
P\Gamma L(V) = PGL(V) \rtimes \operatorname{Gal}(K) ,
$$

the **projective semilinear group**, where the field automorphisms act on the classes of the linear maps by their action on the scalars.

**Theorem (the fundamental theorem of projective geometry).** Let $\dim V \geq 3$ and let $f$ be a collineation of $\mathbb{P}(V)$; then $f$ is induced by a semilinear bijection of $V$, unique up to a scalar, so

$$
\operatorname{Aut}(\mathbb{P}(V)) = P\Gamma L(V) = PGL(V) \rtimes \operatorname{Gal}(K) .
$$

For $\dim V = 2$ the statement that a bijection of the line preserving the collinearity is semilinear is false, and the cross ratio, not the semilinearity, is then the invariant.

**Proof sketch.** A collineation carries lines to lines and preserves the incidence and the dimension, and the value of a coordinate is described by a function on $K$ which is additive and multiplicative because the collineation preserves the projective additions and multiplications; the function is the values of a field automorphism, and the map is semilinear. The classical argument uses the theorem of Desargues in dimension at least two, and it is in *Projective Geometry*.

**Corollary.** Over a field with no nontrivial automorphism the operators of a projective space of dimension at least two are the projectivities, and the operator group is $PGL(V)$; over the prime field $\mathbb{F}_p$ this is the case, and the collineations are exactly the classes of the invertible linear maps.

## Projectivities of the Line

**Theorem.** For $\dim V = 2$ the projective space is the projective line $\mathbb{P}^1(K)$ and every projectivity is induced by a matrix

$$
\begin{pmatrix} a & b \\ c & d \end{pmatrix}, \qquad ad - bc \neq 0,
$$

acting by the **fractional linear transformation**

$$
z \longmapsto \frac{az + b}{cz + d} ,
$$

where $z$ is an affine coordinate on the complement of a point; the operator group is $PGL(2,K) = GL(2,K)/K^\times$, and the assignment is the identification of the operator with the matrix up to a scalar.

**Proof.** A basis of the two-dimensional $V$ gives a coordinate $z = x_1/x_0$ on the affine chart $x_0 \neq 0$; a linear map of coordinates $(x_0,x_1) \mapsto (ax_0 + bx_1, cx_0 + dx_1)$ gives the displayed fractional formula, and the class modulo scalars is the class of the matrix. The point at which $cz + d = 0$ is sent to the point at infinity, and the map is a bijection of $\mathbb{P}^1(K)$.

**Theorem.** The group $PGL(2,K)$ acts sharply triply transitively on the projective line: it acts transitively on the ordered triples of distinct points, and the stabiliser of a triple is trivial; consequently the **cross ratio**

$$
[z_1 : z_2 : z_3 : z_4] = \frac{(z_1 - z_3)(z_2 - z_4)}{(z_1 - z_4)(z_2 - z_3)}
$$

is the complete invariant of the ordered quadruples of distinct points.

**Proof.** A triple of distinct points is carried to $0, 1, \infty$ by a unique projectivity, since the images of three points determine a matrix up to scalars and the three conditions determine the three ratios of the entries; the cross ratio of a quadruple with the first three points at $0,1,\infty$ is the fourth point, so it is invariant and complete.

**Remark.** For $K = \mathbb{C}$ the projective line is the Riemann sphere and the fractional linear operators are the Möbius transformations, whose properties as operators on the sphere and on hyperbolic space are the subject of *The Möbius Transformation as an Operator*; for $K = \mathbb{R}$ the real projectivities are the boundary maps of the isometries of the hyperbolic plane, as *Hyperbolic Geometry* records. The two instances are the reason the projective line is the meeting point of the projective, the Möbius and the hyperbolic geometries of this Part.

## Operators and Figures

### The Operators Preserving a Subspace

**Definition.** A projective subspace $\mathbb{P}(W) \subseteq \mathbb{P}(V)$ is **stable** under the operator $[T]$ when $T(W) = W$; the subgroup of $PGL(V)$ stabilising $\mathbb{P}(W)$ is the image of the subgroup of $GL(V)$ preserving the flag ending at $W$, and the operators fixing a point are the image of the stabiliser of a line.

**Proposition.** The stabiliser of a point $[v]$ is the image of the group of the linear maps preserving the line $Kv$, of dimension $n^2$ as a transformation group, and the stabiliser of a hyperplane is the image of the group of the linear maps preserving $\ker\varphi$; the two are the maximal parabolics of the projective group.

**Proof.** A linear map preserves the line $Kv$ exactly when it induces a map of the quotient $V/Kv$, and it preserves the hyperplane $\ker \varphi$ exactly when it preserves the linear form up to a scalar; the dimensions are read from the exact sequences and count the operators fixing the corresponding figure.

### The Operators Preserving a Quadric

**Definition.** Let $q$ be a quadratic form on $V$ with polar form $B$, both Part II objects named here, and let $Q = \{[v] : q(v) = 0\}$ be its **projective quadric**. An operator preserves the quadric when it carries $Q$ to itself, and the operators preserving the quadric form the **projective orthogonal group** $PO(V,q)$, the image of the orthogonal group $O(V,q)$ in $PGL(V)$.

**Theorem.** An operator $[T]$ preserves the quadric $Q$ if and only if the linear map $T$ preserves the polar form up to a scalar,

$$
B(Tv, Tw) = \lambda\, B(v,w) \quad \text{for all } v, w ,
$$

for some $\lambda \in K^\times$; consequently the group of the quadric is the quotient of the similarity group of the form by the scalars, and for a nondegenerate form it is the projective orthogonal group.

**Proof.** A projective transformation preserving $Q$ carries the tangent hyperplane at a point of $Q$ to the tangent hyperplane at the image, and the polarity of the quadric is induced by $B$; the preservation of the polarity is the up-to-scalar preservation of the form, and the converse is immediate. This is the classical statement of *Projective Geometry*, and it is the reason the form-defined groups of this Part are the groups of the quadrics.

**Corollary.** For a nondegenerate form the projective orthogonal group is the quotient of $O(V,q)$ by its centre up to the scalars, of dimension $\frac{n(n+1)}{2}$ as a transformation group, and its subgroup preserving the quadric and the orientation is the projective special orthogonal group; the Hermitian analogue over a field with an involution is *Unitary Geometry over a Field with Involution*, and the polarity so defined is *Orthogonal Geometry and the Involution*.

## Involutions and the Order of an Operator

**Definition.** An operator is an **involution** when its square is the identity, and the **order** of an operator is the least positive $k$ with $[T]^k = 1$; the order is well defined because the class of $T^k$ is the $k$-th power of the class, and it is the order of the class in the projective group.

**Proposition.** The order of a projectivity of $\mathbb{P}^1(K)$ induced by $T \in GL(2,K)$ is the least $k$ with $T^k$ a scalar; over an algebraically closed field of characteristic not two the involutions fall into two families according to the two eigenvalues, which are either distinct and then two points are fixed, or equal and then one point is fixed with a double eigenvalue.

**Proof.** The class of $T$ is trivial exactly when $T$ is a scalar, so the order is the least such $k$; the eigenvector decomposition of $T$ over an algebraically closed field describes the fixed points, and an involution has eigenvalues $\pm 1$ up to a common scalar, giving either two fixed points or the unipotent case.

**Remark (the harmonic involution).** On the projective line the involution with two fixed points is the **harmonic homology**, and the involution $z \mapsto 1/z$ fixes $\pm 1$ and exchanges $0$ and $\infty$; the cross ratio of the four points $a, b, z, z'$ at a fixed value characterises the involution. The involutions of the projective line are the boundary form of the reflections of the hyperbolic plane and the inversions of the Möbius geometry, and they are treated as operators in *The Möbius Transformation as an Operator*.

## Summary

The operators of a projective space $\mathbb{P}(V)$ are the collineations, and by the fundamental theorem they are the semilinear maps up to scalars, so the operator group is $P\Gamma L(V) = PGL(V) \rtimes \operatorname{Gal}(K)$ in dimension at least two, and its linear part is the projective general linear group $PGL(V) = GL(V)/K^\times$, the quotient of the invertible linear maps by the scalars, with the central extension $1 \to K^\times \to GL(V) \to PGL(V) \to 1$. The projective special linear group $PSL(V)$ is the image of the determinant-one group, of index the power classes. The two-sided reading of the operator group is the left and right translation and the sandwich $\Theta_{[A],[B]}([T]) = [A][T][B]$, whose one-parameter part is the inner automorphism group; the group acts simply transitively on the projective frames, so a transformation is determined by $n^2+2n$ parameters. In dimension one the operators are the fractional linear transformations, $PGL(2,K)$ acts sharply triply transitively, and the cross ratio is the complete invariant of the quadruples. An operator preserves a projective quadric exactly when it preserves the polar form up to a scalar, so the group of a nondegenerate quadric is the projective orthogonal group $PO(V,q)$, and the involutions and the order of a projectivity are read from the powers of the class in the projective group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $V$ | Vector space of dimension $n+1 \geq 2$ |
| $K$ | Coefficient field |
| $\mathbb{P}(V)$ | Projective space of the lines through $0$ |
| $[v]$ | Point of $\mathbb{P}(V)$; homogeneous coordinates up to scale |
| $GL(V)$, $SL(V)$ | Invertible and determinant-one linear maps |
| $PGL(V) = GL(V)/K^\times$ | Projective general linear group, the operator group |
| $PSL(V)$ | Projective special linear group, the image of $SL(V)$ |
| $P\Gamma L(V) = PGL(V)\rtimes\operatorname{Gal}(K)$ | Collineation group; the operators in dimension at least two |
| $\Theta_{[A],[B]}([T]) = [A][T][B]$ | Two-sided sandwich operator |
| $[z_1:z_2:z_3:z_4]$ | Cross ratio of four points of the projective line |
| $PGL(2,K)$ | Operator group of the projective line; fractional linear maps |
| $Q = \{[v] : q(v)=0\}$ | Projective quadric of a quadratic form $q$ |
| $PO(V,q)$ | Projective orthogonal group, the operators preserving $Q$ |
| order, involution | Least $k$ with $[T]^k=1$; operator with square the identity |

## Further Reading

- Reinhold Baer, *Linear Algebra and Projective Geometry* (Academic Press, 1952), for the fundamental theorem and the collineations.
- Jean Dieudonné, *La géométrie des groupes classiques* (Springer, 1955), for the projective groups and the forms they preserve.
- H. S. M. Coxeter, *Projective Geometry*, 2nd ed. (Springer, 2003), for the projective spaces, the frames, the cross ratio and the classical figures.
- Pierre Samuel, *Projective Geometry* (Springer, 1988), for the algebraic treatment of the collineations and the fundamental theorem.
- Armand Borel, *Linear Algebraic Groups*, 2nd ed. (Springer, 1991), for the parabolic subgroups and the stabilisers of the flags.
