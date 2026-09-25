
# __Quaternion Geometry__

## Introduction

This article is the geometry slot of the quaternion system. It describes the geometry that the algebra $\mathbb{H}$ carries once a distance is placed on it: the metric geometry of $\mathbb{H}$ as a four-dimensional Euclidean space, the metric and group geometry of the unit sphere $S^3 = Sp(1)$, the fibration of that sphere over the two-sphere, the projective geometry of the quaternionic projective spaces, and the arithmetic geometry of the lattice of integral quaternions. The article is the geometric companion of the algebraic and rotation-theoretic articles of the same system and is the quaternion entry of the ladder that Part V traverses one number system at a time.

The article assumes the quaternion algebra from *Quaternion Algebra*: its basis $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$, its conjugation $\bar q$, its norm form $N(q) = q\bar q$, its imaginary subspace $\operatorname{Im}\mathbb{H}\cong\mathbb{R}^3$ and its decomposition into scalar and vector parts. It assumes the unit sphere $Sp(1)$, the adjoint action $\operatorname{Ad}_q(x) = qxq^{-1}$, the double cover $Sp(1)\to SO(3)$ and the two-sided action $Sp(1)\times Sp(1)\to SO(4)$ from *Quaternion Rotations and Reflections*, and it does not restate them; the rotations of the imaginary subspace are used here as the isotropy of a geometric action and not re-derived. The homogeneous-space language, the phrase *locally compact group* and the quotient topology are those of Part II, and the general theory of the manifolds that carry a quaternionic structure is the subject of *Quaternionic Geometry*, written in parallel in the geometry category of Part II; the present article treats only the geometry of the algebra itself. The lattice of integral quaternions and its arithmetic are introduced in *Lattices and the Quaternion Lattice* in the linear-spaces category of Part I, and are recalled here only for their geometric content. The sphere $S^3$ is the only sphere treated; the octonionic sphere, where the same construction fails, is a different system and is not used.

Throughout, a quaternion is $q = q_0 + \mathbf{q} = \sum_\mu q_\mu e_\mu$ with $\mu$ running over $0,1,2,3$, the conjugation is $\bar q = q_0 - \mathbf{q}$, the norm form is $N(q) = q\bar q = |q|^2$, the real inner product is

$$
\langle p, q\rangle = \operatorname{Sc}(p\bar q) = \sum_{\mu=0}^{3} p_\mu q_\mu,
$$

and $\operatorname{Im}\mathbb{H} = \{x : \bar x = -x\}\cong\mathbb{R}^3$ is the space of vectors, with inner product $\langle x, y\rangle = \operatorname{Sc}(x\bar y)$ and vector product $x\times y = \tfrac{1}{2}(xy - yx)$. The unit sphere is $S^3 = Sp(1) = \{q : N(q) = 1\}$. The quaternion units $e_k$ are identified with the standard basis of $\mathbb{R}^4$ whenever coordinates are needed.

## The Metric Geometry of the Quaternion Space

### The Euclidean Structure

The norm form is positive definite and anisotropic: $N(q) > 0$ for $q \neq 0$, and $N(q) = 0$ only for $q = 0$. It is the square of the Euclidean norm on $\mathbb{R}^4$ under the identification $\mathbb{H}\cong\mathbb{R}^4$ given by the basis $(e_0, e_1, e_2, e_3)$, and the bilinear form $\langle p, q\rangle$ of the introduction is the associated inner product. This is the distance datum of the system: it defines the norm $|q| = \sqrt{N(q)}$, the metric $d(p,q) = |p - q|$, and with them open sets, convergence, completeness and compactness on $\mathbb{H}$.

**Proposition.** $\mathbb{H}$ with this metric is isometric to $\mathbb{R}^4$, hence complete, locally compact, and non-compact. The map $q\mapsto |q|$ is a norm, and the multiplication satisfies $|pq| = |p|\,|q|$; the unit sphere $S^3$ is a compact subgroup, and the multiplication is continuous.

*Proof.* The identification with $\mathbb{R}^4$ is a linear isometry by the definition of $\langle\cdot,\cdot\rangle$. The multiplicativity of the norm form is the multiplicativity of the quaternion norm, established in *Quaternion Algebra*; it gives $|pq| = |p|\,|q|$ and, since $|1| = 1$, it makes $S^3$ closed under multiplication and inversion. Continuity of multiplication is polynomial continuity in the coordinates, and $S^3$ is closed and bounded in $\mathbb{R}^4$. $\square$

The multiplicativity of the norm is the single feature that distinguishes this metric from a general four-dimensional Euclidean metric, and it is the source of the whole of the geometry below: the unit sphere is not merely a submanifold but a group, and the group structure and the metric interact.

### The Polar Decomposition and the Radial Geometry

**Definition.** For $q \neq 0$ the **polar decomposition** is $q = |q|\,u$ with $|q| > 0$ and $u = q/|q| \in S^3$. The two factors are unique.

**Proposition.** The map $S^3\times\mathbb{R}_{>0}\to\mathbb{H}\setminus\{0\}$, $(u,r)\mapsto ru$, is a homeomorphism and a diffeomorphism. Consequently $\mathbb{H}\setminus\{0\}$ is diffeomorphic to $S^3\times(0,\infty)$, and $\mathbb{H}$ is the metric cone on $S^3$ completed by its apex.

*Proof.* Uniqueness and bijectivity of $u = q/|q|$, $r = |q|$ are immediate from $N(ru) = r^2N(u) = r^2$. The map and its inverse $q\mapsto(q/|q|,|q|)$ are smooth away from the origin. $\square$

The radial geometry is therefore the geometry of the sphere together with the multiplicative radial coordinate; the sphere is the object on which the quaternion-specific geometry lives, and the remaining sections are concerned with it and with the spaces it fibres over.

## The Metric and Group Geometry of the Unit Sphere

### The Restricted Metric

The metric $d$ of $\mathbb{H}$ restricts to $S^3$ and equals the chordal distance. The intrinsic metric of the sphere is different: it is the **geodesic distance**

$$
d_{S^3}(u, v) = \arccos \langle u, v\rangle = \arccos \operatorname{Sc}(u\bar v), \qquad u, v \in S^3,
$$

the angle between the two unit vectors as elements of $\mathbb{R}^4$, with values in $[0,\pi]$.

**Proposition.** The geodesic distance is a metric on $S^3$, it is left- and right-invariant,

$$
d_{S^3}(pu, pv) = d_{S^3}(u, v) = d_{S^3}(up, vp), \qquad p, u, v \in S^3,
$$

and it is invariant under conjugation: $d_{S^3}(\bar u, \bar v) = d_{S^3}(u, v)$.

*Proof.* The angle $\arccos\langle u,v\rangle$ is a metric on the unit sphere of any inner product space, by the Schwarz inequality. Left invariance: $\langle pu, pv\rangle = \operatorname{Sc}(pu\overline{pv}) = \operatorname{Sc}(pu\bar v\bar p) = \operatorname{Sc}(p\,u\bar v\,\bar p)$; conjugation by a unit quaternion is an algebra automorphism preserving the scalar part, so this equals $\operatorname{Sc}(u\bar v) = \langle u,v\rangle$. Right invariance is the same computation with $q\bar p$ in place of $p\bar q$, or follows by conjugation. Invariance under $q\mapsto\bar q$ follows from $\operatorname{Sc}(\bar u v) = \operatorname{Sc}(u\bar v)$. $\square$

So the metric of the sphere is **bi-invariant**: it is invariant under both the left and the right translations of the group $S^3$, and therefore under the two-sided action of $S^3\times S^3$. A bi-invariant metric on a compact Lie group is the metric induced by an invariant inner product on the Lie algebra, here $\operatorname{Im}\mathbb{H}$ with the inner product $\langle x,y\rangle$; this is why the geometric and the algebraic descriptions of the sphere agree exactly, and it is the first instance of the general phenomenon that a compact group carries a canonical geometry.

### Geodesics and the Exponential Map

**Theorem.** The geodesics of $S^3$ through the identity are the curves $t\mapsto\exp(tx)$ for $x\in\operatorname{Im}\mathbb{H}$, where

$$
\exp(tx) = \cos(|x|t) + \frac{x}{|x|}\sin(|x|t)
$$

for $x \neq 0$; they are the great circles, and they are exactly the one-parameter subgroups. The exponential map $\exp : \operatorname{Im}\mathbb{H}\to S^3$ is surjective, its kernel is the union of the spheres $\{x : |x| = 2\pi k\}$ over the integers $k$, and it is a diffeomorphism from the open ball of radius $\pi$ onto $S^3\setminus\{-1\}$.

*Proof.* The formula for $\exp(tx)$ follows from $x^2 = -|x|^2$ and the splitting of the exponential series into even and odd parts, as in *Quaternion Rotations and Reflections*. One-parameter subgroups of a matrix group are the exponentials of Lie-algebra elements, so the geodesics through $1$ are these curves, and the general geodesic is their left translate. The statement on the kernel is the identity $\exp(x) = 1$ iff $|x| \in 2\pi\mathbb{Z}$ and $x/|x|$ arbitrary; the injectivity on the ball of radius $\pi$ is the polar form, and the image omits exactly $-1 = \exp(\pi u)$ for every unit $u$. $\square$

Geodesics are the locally distance-minimising curves, and on $S^3$ every geodesic segment of length at most $\pi$ realises the geodesic distance. The **cut locus** of a point is the antipode: for each $u$ there is exactly one point $v$ at distance $\pi$, namely $v = -u$, and beyond that distance the two unit vectors are joined by a one-parameter family of minimising geodesics. This is the geometry of the compact rank-one symmetric space $S^3$, whose curvature is constant and positive.

### The Sphere as a Homogeneous Space

The bi-invariance of the metric says that the isometry group of $S^3$ contains the two-sided action of $S^3\times S^3$. By *Quaternion Rotations and Reflections* that action is a surjective homomorphism $S^3\times S^3\to SO(4)$ with kernel $\{\pm(1,1)\}$; the isometry group of $S^3$ is $O(4) = SO(4)\rtimes\mathbb{Z}/2\mathbb{Z}$, and the piece containing the identity is exactly $SO(4)$. The sphere is therefore the homogeneous space

$$
S^3 \cong SO(4)/SO(3) \cong (S^3\times S^3)/\Delta S^3, \qquad \Delta S^3 = \{(q,q) : q\in S^3\},
$$

the quotient by the diagonal, which is the isotropy of the identity. The **isotropy representation** is the adjoint action $\operatorname{Ad}$ of $S^3$ on the tangent space $\operatorname{Im}\mathbb{H}$ at the identity, so the sphere is a symmetric space of rank one and the stabiliser of a point is the group $SO(3)$ of rotations of the tangent space. The scalar part of the two-sided action is trivial: since $\Phi_{(q_1,q_2)}(x) = q_1xq_2^{-1}$ fixes the scalar line when $q_1 = q_2$, the diagonal $S^3$ fixes the identity and acts on the tangent space by the adjoint action, as required.

## The Hopf Fibration

### Definition of the Map

**Definition.** The **Hopf map** is

$$
\pi : S^3\longrightarrow S^2, \qquad \pi(q) = q\,e_1\,\bar q .
$$

**Proposition.** For $q\in S^3$ the element $\pi(q)$ lies in $\operatorname{Im}\mathbb{H}$ and has norm one, so $\pi$ is a well-defined map $S^3\to S^2$, where $S^2 = \{x\in\operatorname{Im}\mathbb{H} : |x| = 1\}$ is the unit sphere of the imaginary quaternions. The map is invariant under right multiplication by the subgroup

$$
U(1) = \{e^{e_1\theta} = \cos\theta + e_1\sin\theta : \theta\in\mathbb{R}\},
$$

so that $\pi(qp) = \pi(q)$ for $p\in U(1)$, and the assignment $q\mapsto\pi(q)$ is the orbit map of the action of $U(1)$ on $S^3$ by right translation.

*Proof.* Since $|q| = 1$ and the conjugation preserves the scalar part, $\pi(q)$ has scalar part $\operatorname{Sc}(e_1) = 0$ and norm $N(q)N(e_1)N(\bar q) = 1$; hence $\pi(q)\in S^2$. For $p = e^{e_1\theta}$ one has $p e_1\bar p = e_1$ because $p$ commutes with $e_1$; hence $\pi(qp) = qp\,e_1\bar p\bar q = qe_1\bar q = \pi(q)$. Conversely, if $\pi(q) = \pi(r)$ then $q e_1\bar q = re_1\bar r$, so $\bar r q$ commutes with $e_1$; the commutant of $e_1$ in $\mathbb{H}$ is the two-dimensional subalgebra $\mathbb{R}\oplus\mathbb{R}e_1$, and being a unit quaternion it lies in $U(1)$. Hence $r = q p^{-1}$ for some $p\in U(1)$, and the fibres of $\pi$ are exactly the orbits of the right action. $\square$

### The Fibration

**Theorem.** The Hopf map is a locally trivial fibre bundle with fibre $S^1$ and base $S^2$,

$$
S^1 \longrightarrow S^3 \xrightarrow{\ \pi\ } S^2,
$$

and it is the orbit map of the free right action of $U(1)\cong S^1$ on $S^3$. The fibre over any point is a great circle of $S^3$, and the fibres are pairwise linked, each two of them having linking number one.

*Proof.* The group $U(1)$ acts freely on $S^3$ by right multiplication: $qp = q$ with $p\in U(1)$ gives $p = 1$. The orbit map of a free action of a compact Lie group on a manifold is a principal bundle, so the quotient map $S^3\to S^3/U(1)$ is a locally trivial bundle with structure group $U(1)$; it is $\pi$ by the preceding proposition, and the base is $S^2$ because $\pi$ is surjective and its fibres are the orbits. Surjectivity: every $u\in S^2\subset\operatorname{Im}\mathbb{H}$ is conjugate in $S^3$ to $e_1$, since $S^3$ acts transitively on the unit sphere of the adjoint representation $\operatorname{Im}\mathbb{H}$ by *Quaternion Rotations and Reflections*. Constancy of the fibre: the image of $U(1)$ under right multiplication is the great circle through $1$ and $p$ in the plane $\mathbb{R}\oplus\mathbb{R}e_1$. The linking statement is the classical computation of the Hopf invariant of the generator of $\pi_3(S^2)\cong\mathbb{Z}$; the fibres of the bundle over a latitude circle of the base sweep out a torus in $S^3$ on which they are the two rulings, and the linking number of two fibres is one. $\square$

The fibration is the geometric expression of the identification $S^2 = S^3/U(1)$ and of the homogeneous-space presentation $S^2 = Sp(1)/U(1)$, with isotropy group the circle of quaternions commuting with $e_1$. It also realises the generator of $\pi_3(S^2)$, so the quaternion sphere carries a non-trivial element of homotopy in the lowest dimension where the third homotopy group of a sphere is non-zero.

## Quaternionic Projective Geometry

### The Projective Line

**Definition.** On $\mathbb{H}^2\setminus\{0\}$ define the equivalence relation by $(x,y)\sim(x',y')$ when there is $\lambda\in\mathbb{H}^\times$ with $x' = x\lambda$ and $y' = y\lambda$. The set of classes is the **quaternionic projective line** $\mathbb{H}P^1$.

The relation is defined with the scalar on the right, because $\mathbb{H}$ is non-commutative; it is an equivalence relation, and the right action of $\mathbb{H}^\times$ on $\mathbb{H}^2\setminus\{0\}$ is free. The projective line is the quaternionic analogue of the Riemann sphere, and the next theorem identifies its topology.

**Theorem.** The map

$$
\mathbb{H}P^1\longrightarrow S^4 = \{x\in\mathbb{H}\oplus\mathbb{R} : |x|^2 + t^2 = 1\},
\qquad [x : y]\mapsto \left(2x\bar y,\ |x|^2 - |y|^2\right)\big/\!\left(|x|^2 + |y|^2\right),
$$

is a homeomorphism, so $\mathbb{H}P^1\cong S^4$.

*Proof.* Choosing $\lambda = |y|^{-1}\bar y$ when $y\neq 0$ normalises the representative so that the second coordinate is the real number $|y| \geq 0$, whence every class has a representative $(u, r)$ with $r \geq 0$ real and $|u|^2 + r^2 = 1$; when $r=0$ the class is $[u:0]$ with $|u|=1$. The multiplication $\mathbb{H}^2\times\mathbb{H}\to\mathbb{H}^2$, $((x,y),\lambda)\mapsto(x\lambda,y\lambda)$, is $\mathbb{H}$-linear in the second factor and $\mathbb{R}$-bilinear, and it is continuous; assigning to $(u,r)$ the point $(2u\bar r, |u|^2 - r^2)$ in the unit five-sphere lies in the image. Allowing $u$ to range over the unit sphere $S^3$ and $r$ over $[0,1]$ produces exactly the points of $S^4$, and the identification is compatible with the equivalence relation because the normalisation is unique; the two descriptions are therefore inverse homeomorphisms. $\square$

So the quaternionic projective line is a four-sphere, and it is the base of a second fibration over the quaternion sphere: the assignment $(x,y)\mapsto$ the class of $(x,y)$ restricted to the unit five-sphere of $\mathbb{H}^2$ gives a bundle

$$
S^3 \longrightarrow S^7 \xrightarrow{\ \ } S^4,
$$

the quaternionic Hopf bundle, whose fibre and base are the two spheres that the quaternion algebra supplies.

### The Quaternionic Möbius Group

**Definition.** The group $GL_2(\mathbb{H})$ of invertible quaternionic $2\times2$ matrices with entries in $\mathbb{H}$ acts on $\mathbb{H}P^1$ by

$$
\begin{pmatrix} a & b \\ c & d \end{pmatrix}\cdot[x : y] = [ax + by : cx + dy].
$$

Its centre is $\mathbb{R}^\times$, and the **quaternionic Möbius group** is the quotient

$$
PGL_2(\mathbb{H}) = GL_2(\mathbb{H})/\mathbb{R}^\times .
$$

**Theorem.** The action of $PGL_2(\mathbb{H})$ on $\mathbb{H}P^1\cong S^4$ is faithful, transitive, and by homeomorphisms; in the affine chart $y\neq 0$, with $z = xy^{-1}\in\mathbb{H}$, an element acts by the fractional transformation

$$
z \longmapsto (az + b)(cz + d)^{-1}, \qquad \begin{pmatrix} a & b \\ c & d \end{pmatrix}\in GL_2(\mathbb{H}),
$$

and these maps are exactly the orientation-preserving conformal transformations of $S^4$; the full conformal group is $PGL_2(\mathbb{H})\rtimes\mathbb{Z}/2\mathbb{Z}$, the extra factor being an orientation-reversing conformal map.

*Proof.* The action is well defined on classes because right multiplication scales both coordinates by the same unit. Faithfulness of the quotient action: a matrix acting trivially on the projective line is scalar. Transitivity: $GL_2(\mathbb{H})$ sends any non-zero vector to any other, because $\mathbb{H}$ is a division algebra, so the induced action on classes is transitive. The explicit form of the fractional transformation in the chart $y \neq 0$ is a rearrangement of the matrix action. The identification of the resulting group with the conformal group of $S^4$ is the classical computation, of the same kind as the identification of $PGL_2(\mathbb{C})$, acting by Möbius transformations, with the orientation-preserving conformal group of the two-sphere; the general statement is that the conformal group of the round $n$-sphere is the group of Möbius transformations over the corresponding division algebra. $\square$

The conformal structure of $S^4$ is thus quaternionic in the same sense in which the conformal structure of $S^2$ is complex; the algebra appears as the coefficient algebra of the transformations, and the non-commutativity of $\mathbb{H}$ is the reason the matrices are written with a definite side.

### Higher Projective Space and Grassmannians

The construction of $\mathbb{H}P^1$ repeats for any number of coordinates.

**Definition.** On $\mathbb{H}^{n+1}\setminus\{0\}$ define $(x_0,\dots,x_n)\sim(x'_0,\dots,x'_n)$ when there is $\lambda\in\mathbb{H}^\times$ with $x'_i = x_i\lambda$ for all $i$. The quotient is the **quaternionic projective space** $\mathbb{H}P^n$.

**Proposition.** The right action of $\mathbb{H}^\times$ used in the definition is free, so $\mathbb{H}P^n$ is a manifold of real dimension $4n$; the tautological subbundle of the trivial bundle $\mathbb{H}^{n+1}$ is a quaternionic line bundle, and $\mathbb{H}P^n$ is the classifying quotient $S^{4n+3}/S^3$ of the unit sphere of $\mathbb{H}^{n+1}$ by the free right action of $S^3$.

*Proof.* Freedom: $x_i\lambda = x_i$ for all $i$ with some $x_i\neq 0$ forces $\lambda = 1$. Smoothness follows from the transitivity of the action of $GL_{n+1}(\mathbb{H})$ and the existence of affine charts, in which a class with $x_i\neq 0$ is represented uniquely by normalising $x_i = 1$; the charts are copies of $\mathbb{H}^n$, and the changes of chart are smooth because they are one-sided affine maps. The identification with $S^{4n+3}/S^3$ is the orbit-map description of the free action of $S^3$ by right multiplication on the unit sphere. $\square$

Combining the projective space with the flags of subspaces gives the **quaternionic Grassmannians** $Gr_k(\mathbb{H}^n)$, the quotients of the unitary quaternionic group by the block subgroups; they are the compact symmetric spaces of the quaternion family, and their geometry is the manifold part of the subject, treated in *Quaternionic Geometry* in Part II. What belongs to the algebra is the fact that the line bundle over $\mathbb{H}P^n$ is quaternionic and that the projective space is the quotient of the sphere by $S^3$; both follow from the division-algebra property alone.

## The Quaternionic Structure on $\mathbb{R}^{4n}$

The quaternion algebra acts on itself and therefore on any quaternionic vector space, and this action is a geometric structure on the underlying real vector space.

**Definition.** A **quaternionic vector space** is a right module $V$ over $\mathbb{H}$; a **quaternionic structure** on a real vector space $W$ is an injective $\mathbb{R}$-algebra homomorphism $\mathbb{H}\to\operatorname{End}_\mathbb{R}(W)$, equivalently a real representation of $\mathbb{H}$ that extends the scalar action.

**Proposition.** Let $W$ be a real vector space with a quaternionic structure. Then $W$ carries a triple of complex structures $I_1, I_2, I_3$, the images of $e_1, e_2, e_3$, satisfying the quaternion relations

$$
I_1^2 = I_2^2 = I_3^2 = -1, \qquad I_1I_2 = I_3, \quad I_2I_3 = I_1, \quad I_3I_1 = I_2,
$$

and a positive definite inner product invariant under all three, when one is chosen compatible with the quaternionic structure; the dimension of $W$ over $\mathbb{R}$ is a multiple of four.

*Proof.* The relations are the images of the relations $e_k^2 = -e_0$ and $e_1e_2 = e_3$ of the algebra under the homomorphism, which is injective. Since $\mathbb{H}$ is a division algebra, $W$ is free as a module and its real dimension is four times its dimension as a module. An arbitrary inner product is averaged over the compact group $Sp(1)$ of unit quaternions to obtain one invariant under all three structures. $\square$

The triple $(I_1, I_2, I_3)$ is the **quaternionic structure**, and the compatibility condition makes it a hypercomplex structure on $W$; the invariance of the inner product makes it hyperkähler in the linear sense, namely a quaternionic Hermitian space. On the sphere $S^3$ itself, the three complex structures are obtained from the left-invariant fields, and they underlie the description of $S^3$ as a hypercomplex manifold. The manifold theory that this linear structure generates — the hypercomplex and hyperkähler manifolds, and the quaternionic manifolds on which the triple is only locally defined — is exactly the content of *Quaternionic Geometry* and *Hyperkähler Geometry* in Part II, and it is not developed here.

## The Arithmetic Geometry of the Quaternion Lattice

### The Lattice

The quaternion algebra contains a distinguished discrete subgroup, whose geometry is the arithmetic face of the same norm form.

**Definition.** A quaternion is **Lipschitz integral** if all four of its coordinates $q_\mu$ are integers, and **Hurwitz integral** if all four coordinates lie in $\mathbb{Z}$ or all four lie in $\mathbb{Z} + \tfrac{1}{2}$. The sets

$$
\mathcal{L} = \mathbb{Z}e_0 + \mathbb{Z}e_1 + \mathbb{Z}e_2 + \mathbb{Z}e_3, \qquad
\mathcal{H} = \mathcal{L}\cup\left(\tfrac{1}{2}e_0 + \mathcal{L}\right)
= \mathcal{L}\cup\left(\tfrac{1}{2}e_1 + \mathcal{L}\right)\cup\left(\tfrac{1}{2}e_2 + \mathcal{L}\right)\cup\left(\tfrac{1}{2}e_3 + \mathcal{L}\right)
$$

are the **Lipschitz order** and the **Hurwitz order**.

**Proposition.** Both $\mathcal{L}$ and $\mathcal{H}$ are subrings of $\mathbb{H}$ with the same unit $e_0$, they are lattices in $\mathbb{R}^4$, and $\mathcal{H}$ is closed under conjugation; $\mathcal{L}$ is not multiplicatively closed under conjugation and inversion, and $\mathcal{H}$ is the smallest subring containing $\mathcal{L}$ in which every element has an inverse when its norm form is $1$.

*Proof.* The Lipschitz order is the integer span of the basis, and its closure under multiplication is the integrality of the structure constants. For the Hurwitz order, the four cosets listed exhaust the elements with all coordinates in $\mathbb{Z}$ or all in $\mathbb{Z}+\tfrac{1}{2}$, and the product of two elements of any two cosets lies in one of the four; the verification is a finite computation with the structure constants of the quaternion algebra. Closure under conjugation is clear from the coordinate description. The two orders are lattices because they are free abelian groups of rank four spanning $\mathbb{R}^4$. $\square$

### The Units and Their Geometry

The unit groups of the two orders are finite, and their geometry is the arithmetic of the sphere of radius one.

**Theorem.** The groups of units are

$$
\mathcal{L}^\times = \{\pm e_0, \pm e_1, \pm e_2, \pm e_3\}, \qquad |\mathcal{L}^\times| = 8,
$$

the quaternion group of order eight, and $\mathcal{H}^\times$ has order $24$. The Hurwitz units are the $24$ elements of the form

$$
\pm e_0, \quad \pm e_1, \quad \pm e_2, \quad \pm e_3, \quad \tfrac{1}{2}(\pm e_0 \pm e_1 \pm e_2 \pm e_3),
$$

with the four signs of the last family taken independently; they form the binary tetrahedral group $2T$, the preimage in $S^3$ of the rotation group $T\cong A_4$ of the regular tetrahedron; as a group, $2T$ has one element of order $2$ and $8$ elements of order $6$, and its elements of order $3$ and $6$ number $16$ in all. On the sphere $S^3$ the twenty-four units are the vertices of the regular 24-cell, inscribed in the unit sphere and invariant under right and left multiplication by $2T$.

*Proof.* An element of $\mathcal{L}$ has integer coordinates and norm one, so three of its coordinates vanish and the fourth is $\pm 1$: the eight units are the quaternion group. An element of $\mathcal{H}$ has coordinates in $\mathbb{Z}$ or all in $\mathbb{Z}+\tfrac{1}{2}$; a sum of four squares integer or four squares half-integer equal to one gives exactly the twenty-four listed. Closure under multiplication makes the set a group, and the coincidence of the $24$ vertices with the $24$-cell is the standard combinatorial description of the Hurwitz units. The identification with the binary tetrahedral group is made in *The Rotation and Reflection Groups in the Biquaternion Algebra*, where the finite subgroups of the unit sphere are tabulated. $\square$

The lattice is thus the arithmetic counterpart of the geometry: the unit sphere of the algebra carries a discrete subgroup of finite covolume up to scaling, the norm form is the quadratic form of the lattice, and the unit group of the lattice is the finite symmetry of the densest four-dimensional packing that the quaternion norm defines. The detailed arithmetic is the subject of *Lattices and the Quaternion Lattice* in Part I; the geometric content kept here is that the lattice is a discrete cocompact subset of the sphere of each radius up to the diagonal scaling.

## Comparison with the Complex Case

The geometry above is a strict enrichment of the complex geometry, and the comparison isolates what the quaternions add.

| Feature | $\mathbb{C}$ | $\mathbb{H}$ |
|---|---|---|
| Real dimension | $2$ | $4$ |
| Unit sphere | $S^1$ | $S^3$ |
| Sphere is a group | $U(1)$, abelian | $Sp(1)$, non-abelian |
| Metric | flat plane, circle of unit radius | flat space, round three-sphere |
| Geodesics | lines, great circles | hyperplanes, great three-spheres |
| Group of isometries of the sphere | $O(2) = U(1)\rtimes\mathbb{Z}/2$ | $O(4) = SO(4)\rtimes\mathbb{Z}/2$, $SO(4)\cong (S^3\times S^3)/\{\pm1\}$ |
| Fibration | $S^1\to S^1\to\text{pt}$ | $S^1\to S^3\to S^2$ |
| Projective line | $\mathbb{C}P^1 = S^2$ | $\mathbb{H}P^1 = S^4$ |
| Möbius group | $PGL_2(\mathbb{C})\cong PSL_2(\mathbb{C})$ | $PGL_2(\mathbb{H})$, the conformal group of $S^4$ |
| Complex structures | one, canonical | a two-sphere of them |
| Lattice units | $\{\pm1,\pm i\}$, order $4$ | $\mathcal{L}^\times$ order $8$, $\mathcal{H}^\times$ order $24$ |

Three differences carry the weight. First, the unit sphere of the plane is the whole group of unit complex numbers and the projective line is the two-sphere, whereas the quaternion sphere is three-dimensional, so the fibration over the two-sphere is non-trivial and the projective line is a four-sphere; the quaternion case has a bundle where the complex case has an isomorphism. Second, the isometry group of $S^3$ is the six-dimensional $SO(4)$, and the two-sided action shows it to be a product of two copies of the group, the geometry of a compact group being controlled by two translations rather than one. Third, the complex plane has a single complex structure, whereas the quaternions carry a whole two-sphere of square roots of $-e_0$, so a quaternionic vector space has a two-sphere of complex structures rather than a canonical one.

## Summary

The quaternion algebra $\mathbb{H}$ with its norm form is a four-dimensional Euclidean space whose multiplication is norm-multiplicative. The radial structure is the polar decomposition $q = |q|u$ and identifies $\mathbb{H}\setminus\{0\}$ with $S^3\times\mathbb{R}_{>0}$; the geometry specific to the system lives on the unit sphere $S^3 = Sp(1)$, which is a compact non-abelian Lie group carrying a bi-invariant metric, the geodesic distance $d(u,v) = \arccos\operatorname{Sc}(u\bar v)$. Its geodesics are the one-parameter subgroups $t\mapsto\exp(tx)$, its cut locus is the antipode, and its isometry group is $O(4)$, acting through the two-sided action of $S^3\times S^3$; as a homogeneous space $S^3\cong SO(4)/SO(3)\cong(S^3\times S^3)/\Delta S^3$.

The Hopf map $\pi(q) = qe_1\bar q$ is the orbit map of the free right action of $U(1)$ and gives the locally trivial bundle $S^1\to S^3\to S^2$, whose fibres are linked great circles. Its higher analogue is the bundle $S^3\to S^7\to S^4$ over the quaternionic projective line, and $\mathbb{H}P^n$ is the quotient of the unit sphere of $\mathbb{H}^{n+1}$ by the free right action of $S^3$, a manifold of real dimension $4n$ with a tautological quaternionic line bundle. The quaternionic Möbius group $PGL_2(\mathbb{H})$ acts on $\mathbb{H}P^1\cong S^4$ by fractional transformations and is the orientation-preserving conformal group of the four-sphere.

A quaternionic structure on a real vector space is a triple of complex structures satisfying the quaternion relations; over $\mathbb{R}$ its dimension is a multiple of four, and it carries a compatible inner product, the linear model of the hypercomplex and hyperkähler geometry developed in Part II. Finally the norm form defines the Lipschitz and Hurwitz orders, whose unit groups have order eight and twenty-four; the twenty-four Hurwitz units form the binary tetrahedral group and are the vertices of the regular 24-cell inscribed in the unit sphere.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | The quaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $q = q_0 + \mathbf{q} = \sum_{\mu=0}^{3} q_\mu e_\mu$ | General quaternion, scalar part $q_0$, vector part $\mathbf{q}$ |
| $\bar q = q_0 - \mathbf{q}$ | Quaternion conjugate |
| $N(q) = q\bar q = \lvert q\rvert^2$ | Norm form and modulus |
| $\langle p, q\rangle = \operatorname{Sc}(p\bar q)$ | Real inner product on $\mathbb{H}$ |
| $\operatorname{Im}\mathbb{H}\cong\mathbb{R}^3$ | Imaginary quaternions, the space of vectors |
| $x\times y = \tfrac{1}{2}(xy - yx)$ | Vector product on $\operatorname{Im}\mathbb{H}$ |
| $S^3 = Sp(1) = \{q : N(q) = 1\}$ | Unit sphere, group of unit quaternions |
| $d_{S^3}(u,v) = \arccos\operatorname{Sc}(u\bar v)$ | Geodesic distance on $S^3$ |
| $\exp(x) = \cos\lvert x\rvert + \frac{x}{\lvert x\rvert}\sin\lvert x\rvert$ | Exponential of a vector, the geodesics |
| $\Delta S^3 = \{(q,q)\}$ | Diagonal subgroup of $S^3\times S^3$ |
| $\pi(q) = qe_1\bar q$ | Hopf map $S^3\to S^2$ |
| $U(1) = \{e^{e_1\theta}\}$ | Circle subgroup, the fibre of the Hopf map |
| $\mathbb{H}P^n$ | Quaternionic projective space, real dimension $4n$ |
| $PGL_2(\mathbb{H}) = GL_2(\mathbb{H})/\mathbb{R}^\times$ | Quaternionic Möbius group |
| $Gr_k(\mathbb{H}^n)$ | Quaternionic Grassmannian |
| $I_1, I_2, I_3$ | Images of $e_1, e_2, e_3$: the quaternionic structure |
| $\mathcal{L}$ | Lipschitz order, integer coordinates |
| $\mathcal{H}$ | Hurwitz order, integer or half-integer coordinates |
| $\mathcal{L}^\times$, $\mathcal{H}^\times$ | Unit groups of order $8$ and $24$ |
| $2T$ | Binary tetrahedral group, the Hurwitz units |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the origin of the quaternion algebra and its geometry.
- Heinz Hopf, "Über die Abbildungen der dreidimensionalen Sphäre auf die Kugelfläche", *Mathematische Annalen* **104** (1931), 637–665, for the fibration $S^1\to S^3\to S^2$ and the Hopf invariant.
- Norman Steenrod, *The Topology of Fibre Bundles* (Princeton University Press, 1951), for the principal bundle structure of the Hopf maps and the quaternionic projective spaces.
- Marcel Berger, *A Panoramic View of Riemannian Geometry* (Springer, 2003), for the bi-invariant metric on a compact Lie group and the geometry of the round spheres.
- Ahlfors, Lars V., *Möbius Transformations in Several Dimensions* (University of Minnesota, 1981), for the conformal group of the four-sphere and the quaternionic Möbius transformations.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the Hurwitz order, the quaternion unit groups and the 24-cell.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for the sphere as a Lie group and the two-sided action giving $SO(4)$.
