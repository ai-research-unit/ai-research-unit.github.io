
# __Octonion Geometry__

## Introduction

This article is the geometry slot of the octonion system. It sets out the geometry that the octonion algebra carries on $\mathbb{R}^8$ and on its imaginary part, the almost complex and nearly Kähler structures on the imaginary unit sphere, the octonionic projective plane, and the calibrated forms that the algebra defines. The article is the octonion member of the geometry slots that this Part traverses one number system at a time; it is not the general theory of the geometry of Part II, which is that of the companions *Riemannian Geometry*, *Symmetric Spaces* and *Homogeneous Spaces*, all written in parallel. The projective geometries of the associative systems are the companions *Projective Geometry* and *Quaternion Geometry*, and the geometry of the split systems is *Split-Biquaternion Geometry* and *Split-Biquaternions and Hyperbolic Geometry*.

The article takes the multiplication and the associator from *Octonion Algebra*, the norm, the inner product and the unit sphere from *Octonion Norm and Invertibility*, the operator theory from *Octonion Representations*, and the groups $G_2$, $F_4$ and the Cayley plane from *Octonions and the Exceptional Lie Groups*. The differential forms and their integrals are those of *Differential Forms and Stokes' Theorem*, the fibrations those of *Fibre Bundles, Connections and Curvature*, and the projective geometry of Part II is the companion *Projective Geometry*. The exceptional holonomy of Part II is the subject of *G2 and Spin(7) Manifolds* ; the geometry of the other number systems is *Quaternion Geometry* , for the split systems, *Split-Biquaternion Geometry* and *Split-Biquaternions and Hyperbolic Geometry*, written in this batch. The present article supplies the octonionic geometry that these articles use.

**Conventions.** The octonions are $\mathbb{O}$ with basis $e_0,\dots,e_7$, conjugation $\bar x$, norm $\lvert x\rvert^2 = x\bar x = \langle x,x\rangle$ and inner product $\langle x,y\rangle = \operatorname{Sc}(x\bar y)$. The imaginary subspace is $\operatorname{Im}\mathbb{O}\cong\mathbb{R}^7$ with orthonormal basis $e_1,\dots,e_7$, and $S^6$ denotes its unit sphere. For $u,v\in\operatorname{Im}\mathbb{O}$ the **cross product** is

$$
u\times v = \operatorname{Vect}(uv) = \tfrac{1}{2}(uv - vu),
$$

which is again imaginary. The identification $\mathbb{O}\cong\mathbb{R}^8$ is always by the basis $e_0,\dots,e_7$ and always carries the Euclidean metric $\langle\cdot,\cdot\rangle$.

## The Imaginary Space and the Cross Product

### The Cross Product

**Theorem.** The cross product is bilinear and alternating on $\operatorname{Im}\mathbb{O}$ and satisfies

$$
\lvert u\times v\rvert^2 = \lvert u\rvert^2\lvert v\rvert^2 - \langle u,v\rangle^2, \qquad
u\times(u\times w) = \langle u,w\rangle u - \lvert u\rvert^2w
$$

for all imaginary $u,v,w$. Consequently $\operatorname{Im}\mathbb{O}$ with the cross product is the seven-dimensional vector product.

*Proof.* Both identities are the real-part identities of *Octonion Algebra* together with the alternation of the associator: expanding $\operatorname{Vect}(uv) = \tfrac12(uv-vu)$ and using $\langle uv,w\rangle = \operatorname{Sc}(uv\bar w)$ reduces each identity to the Fano multiplication table, checked on the basis; the first is the Lagrange identity of the norm form and the second is its polarised companion. $\square$

The first identity says that the cross product has the length of the area of the parallelogram spanned by $u$ and $v$; the second says that for orthonormal $u,w$ the map $v\mapsto u\times v$ is a complex structure on the orthogonal complement of $u$ and a rotation by a right angle in the plane spanned by $u,w$.

### The Associative Three-Form

**Definition.** The **associative three-form** on $\operatorname{Im}\mathbb{O}$ is

$$
\varphi(u,v,w) = \langle u\times v,w\rangle, \qquad u,v,w\in\operatorname{Im}\mathbb{O}.
$$

**Theorem.** $\varphi$ is an alternating three-form on $\mathbb{R}^7$, nonzero and of norm one in the sense that its stabiliser in $GL_7(\mathbb{R})$ is the group $G_2$; equivalently

$$
G_2 = \left\{g\in GL_7(\mathbb{R}) : g^*\varphi = \varphi\right\} = \left\{g\in SO(7) : g^*\varphi = \varphi\right\} .
$$

The value of $\varphi$ on an ordered orthonormal triple of imaginary basis elements is $\pm1$ precisely when the triple is a Fano line, so that the seven associative three-planes of the form $\operatorname{span}(e_i,e_j,e_k)$ are the seven lines of the Fano plane, and it is zero otherwise.

*Proof.* Alternation is the computation of the multiplication table: the structure constants of the cross product in the basis $e_1,\dots,e_7$ are totally antisymmetric, and they are nonzero exactly on the Fano lines, with the orientations carried by the table; the identification of the stabiliser with $G_2$ is the standard theorem quoted in *Octonions and the Exceptional Lie Groups*. $\square$

**Corollary.** The three-form $\varphi$ and the metric determine the cross product by $u\times v = $ the vector dual to $\varphi(u,v,\cdot)$, and hence determine the octonion multiplication. The group $G_2$ is therefore the full symmetry group of the geometry of the imaginary space, and its orbit on the Grassmannian of oriented three-planes separates the associative planes from the rest.

*Proof.* Non-degeneracy of the metric gives the duality, and the stabiliser statement is the theorem. $\square$

## The Unit Spheres

### The Sphere $S^7$

**Proposition.** The unit sphere $S^7\subset\mathbb{O}$ is a compact Riemannian manifold of dimension seven with the round metric inherited from $\mathbb{R}^8$; it is parallelizable, and it is homogeneous under the action of left multiplication, so that $S^7 = \operatorname{Spin}(7)/G_2$ with the isotropy $G_2$ acting irreducibly on the tangent space $\operatorname{Im}\mathbb{O}$.

*Proof.* The round metric is the restriction of the Euclidean metric by definition of a submanifold, the parallelizability is the existence of the seven global fields $x\mapsto xe_k$, and the homogeneous description is the orbit theorem of *Octonion Representations*. $\square$

### The Sphere $S^6$ and the Nearly Kähler Structure

**Theorem.** For a unit imaginary $u$ the map

$$
J_u : u^{\perp}\longrightarrow u^{\perp}, \qquad J_uv = u\times v,
$$

is a linear isometry with $J_u^2 = -\mathrm{id}$, so that it defines an almost complex structure on the imaginary unit sphere $S^6$; the associated Hermitian metric $g$ and two-form $\omega$ satisfy

$$
\nabla_X(JY) + J\nabla_Y(JX) = 0
$$

for the Levi-Civita connection of $S^6$, that is, $(S^6,g,J)$ is a **nearly Kähler** manifold. The almost complex structure is not integrable: the Nijenhuis tensor $N_J$ does not vanish, so $S^6$ is not a complex manifold with this structure.

*Proof.* The identities $J_u^2 = -\mathrm{id}$ and orthogonality are the two displayed identities of the previous section restricted to $u^\perp$; the nearly Kähler equation is the classical theorem of the (nearly Kähler) structure induced by the cross product, and the non-integrability is the classical theorem that the Nijenhuis tensor of this structure is nonzero. The statements are standard and are quoted with the sources cited. $\square$

The almost complex structure on $S^6$ is the reason why the exceptional geometry of $G_2$ has a nearly Kähler rather than a Kähler flavour: the natural candidate for a complex structure defined by the algebra is present but is not integrable, and it degenerates along the imaginary units themselves. The question whether $S^6$ carries some complex structure is a separate and open problem, and the present article does not use it.

### The Fibrations

**Proposition.** The unit sphere carries the following fibre bundles with the indicated fibres and bases.

1. The quaternionic Hopf fibration $S^3\to S^7\to S^4$, whose fibres are the quaternion unit spheres under right multiplication by the unit quaternions of a fixed quaternion subalgebra.
2. The octonionic Hopf fibration $S^7\to S^{15}\to S^8$, with fibres $S^7$ and base $S^8$, in the analogous sense.

Both bundles are non-trivial and their total spaces are the spheres of the quaternionic and octonionic lines; the octonionic bundle is the last of the four Hopf fibrations, whose existence is equivalent to the parallelizability of the spheres $S^1,S^3,S^7$.

*Proof.* The fibres are the orbits of $S^3$ and of $S^7$ acting by right multiplication on the corresponding unit spheres, which are free and proper; the base is the quotient, identified with the projective spaces $\mathbb{HP}^1 = S^4$ and $\mathbb{OP}^1 = S^8$ of lines in $\mathbb{H}^2$ and $\mathbb{O}^2$. Non-triviality and the classification of the Hopf fibrations are standard; the sources are cited. $\square$

## The Octonionic Projective Plane

### The Plane of Lines

**Definition.** Let $\mathbb{O}^3$ be the free right $\mathbb{O}$-module of triples, with the equivalence relation on nonzero triples

$$
(x_0,x_1,x_2)\sim(x_0u,x_1u,x_2u), \qquad u\in\mathbb{O}^{\times},
$$

of right multiplication by a unit octonion. The set of classes is the **octonionic projective plane** $\mathbb{OP}^2$; the class of $(x_0,x_1,x_2)$ is written $[x_0:x_1:x_2]$ and is a **point** of the plane. A **line** is the set of points satisfying a right-linear equation $x_0a_0 + x_1a_1 + x_2a_2 = 0$ with a triple of octonions not all zero.

**Proposition.** The relation $\sim$ is an equivalence relation; the map assigning to a unit octonion the line through a fixed point is well defined; and $\mathbb{OP}^2$ is a compact topological space of real dimension $16$. Two distinct points determine a unique line, and two lines in general position meet in a unique point, so that $\mathbb{OP}^2$ satisfies the incidence axioms of a projective plane; the duality between points and lines is the map sending the point $[x]$ to the line $\{y : \langle x,y\rangle = 0\}$ up to the appropriate side.

*Proof.* The equivalence relation is the action of the group $\mathbb{O}^{\times}$ on $\mathbb{O}^3\setminus\{0\}$ by right multiplication, which is free; the quotient is compact because the sphere $S^{23}$ is compact and the action restricts to it. Incidence is proved by solving the right-linear systems, which are solvable because $\mathbb{O}$ is a division algebra; the uniqueness statements use the cancellation property of *Octonion Norm and Invertibility*. The detailed verification of the incidence axioms is standard and is cited. $\square$

### The Jordan Model and the Cayley Plane

**Theorem.** The octonionic projective plane is isomorphic to the space of rank-one idempotents of trace one in the exceptional Jordan algebra $\mathfrak{h}_3(\mathbb{O})$,

$$
\mathbb{OP}^2\cong\left\{A\in\mathfrak{h}_3(\mathbb{O}) : A\circ A = A,\ \operatorname{tr}A = 1\right\},
$$

and as a homogeneous space it is

$$
\mathbb{OP}^2 = F_4/\operatorname{Spin}(9), \qquad \dim_{\mathbb{R}}\mathbb{OP}^2 = 52 - 36 = 16 ,
$$

the **Cayley plane**. It is a compact connected simply connected rank-one symmetric space with a metric of sectional curvature between $\tfrac14$ and $1$ when normalised so that the maximum is $1$; with this metric it has diameter $\pi/2$, and its cohomology is $\mathbb{Z}[x]/(x^3)$ with $\deg x = 8$, so that it has the rational cohomology of a projective plane with the degrees $1$, $8$, $16$.

*Proof.* The identification with the rank-one idempotents is the standard Veronese model of the plane; the homogeneous description and the cell decomposition are those of *Octonions and the Exceptional Lie Groups*; the curvature, diameter and cohomology statements are the standard properties of the rank-one symmetric space $F_4/\operatorname{Spin}(9)$ and are quoted with the sources cited. $\square$

**Theorem.** The projective plane $\mathbb{OP}^2$ is a **Moufang plane**, that is, its collineation group is transitive on incident point–line pairs and the little projective group is transitive on the flags and satisfies the Moufang condition; but it is not **Desarguesian**. Consequently the plane has no coordinate field, and the failure of the Desargues axiom is an incidence-theoretic form of the non-associativity of $\mathbb{O}$: a quaternion subalgebra of $\mathbb{O}$ coordinatises the subplanes whose lines lie in a common $\mathbb{H}^3\subset\mathbb{O}^3$, and no single such subalgebra coordinatises the whole plane.

*Proof.* The Moufang condition is the transitivity statement for $F_4$ refined to the little projective group; the failure of Desargues is the classical theorem that a projective plane coordinatised by a division ring satisfies Desargues, whereas $\mathbb{OP}^2$ admits no division ring of coordinates because the multiplication is not associative. Both statements are standard, with the sources cited. $\square$

The plane $\mathbb{OP}^2$ is thus the exact geometric analogue of the real, complex and quaternionic projective planes $\mathbb{RP}^2,\mathbb{CP}^2,\mathbb{HP}^2$, and it is the largest of them; the sequence stops with the octonions for the same reason as the Hopf fibrations and the normed division algebras stop.

## Calibrated Geometry

### The Calibrations

**Definition.** Let $\varphi$ be the associative three-form on $\operatorname{Im}\mathbb{O}\cong\mathbb{R}^7$ and let $\psi = *\varphi$ be its Hodge dual, a four-form on $\mathbb{R}^7$; on $\mathbb{R}^8\cong\mathbb{O}$ the **Cayley four-form** is

$$
\Phi = e^0\wedge\varphi + \psi ,
$$

where $e^0$ is the covector dual to $e_0$.

**Theorem.** A differential form $\alpha$ of degree $k$ on a Riemannian manifold is a **calibration** if $\alpha|_\xi\leq\operatorname{vol}_\xi$ for every oriented $k$-plane $\xi$, with the orientation and the volume form of the metric. With this definition:

1. $\varphi$ is a calibration on $\mathbb{R}^7$, and an oriented three-plane on which $\varphi|_\xi = \operatorname{vol}_\xi$ is exactly an **associative** three-plane, that is, an oriented subspace spanned by an orthonormal triple whose span is closed under the cross product;
2. $\psi$ is a calibration on $\mathbb{R}^7$, and the corresponding equality planes are the **coassociative** four-planes, the orthogonal complements of the associative three-planes;
3. $\Phi$ is a calibration on $\mathbb{R}^8$, and the corresponding equality planes are the **Cayley** four-planes.

*Proof.* The calibration inequality for $\varphi$ follows from $\lvert u\times v\rvert^2 = \lvert u\rvert^2\lvert v\rvert^2 - \langle u,v\rangle^2$: for an orthonormal pair the cross product is a unit vector, and the value $\varphi(u,v,w) = \langle u\times v,w\rangle$ is at most one in absolute value, with equality exactly when the triple is closed. The dual statements follow from the duality and the corresponding computations for $\Phi$, and are the standard theory of the exceptional calibrations, quoted with the sources cited. $\square$

**Corollary.** An oriented submanifold of $\mathbb{R}^7$ all of whose tangent planes are associative is a calibrated submanifold which minimises volume in its homology class, and the same holds for coassociative four-folds in $\mathbb{R}^7$ and Cayley four-folds in $\mathbb{R}^8$. The exceptional calibrations are therefore the variational face of the octonion algebra, and they pass to the manifolds of holonomy $G_2$ and $\operatorname{Spin}(7)$, whose tangent spaces are modelled on $\operatorname{Im}\mathbb{O}$ with the form $\varphi$ and on $\mathbb{O}$ with the form $\Phi$; the global theory is that of *G2 and Spin(7) Manifolds* .

*Proof.* The calibration inequality gives the volume bound for a submanifold tangent to the equality planes, and the bound is attained by the submanifold itself, proving minimality in its homology class; the passage to the holonomy manifolds is the definition of the exceptional holonomy groups. $\square$

### The Rational Forms and the Lattices

**Proposition.** The forms $\varphi$, $\psi$ and $\Phi$ have integral coefficients in the orthonormal basis $e_0,\dots,e_7$, and so do the structure constants of the cross product and of the octonion multiplication. Consequently the groups $G_2$ and $\operatorname{Spin}(7)$ have integral forms defined over $\mathbb{Z}$, and the lattice

$$
\mathbb{O}_{\mathbb{Z}} = \mathbb{Z}e_0\oplus\cdots\oplus\mathbb{Z}e_7
$$

is closed under multiplication and of rank eight over $\mathbb{Z}$. It is not associative, so it is a non-associative order rather than a ring; it is the integral structure underlying the arithmetic of the Cayley numbers.

*Proof.* The coefficients are the structure constants of the multiplication table of *Octonion Algebra*, which are $0$ or $\pm1$, and the calibration forms are their alternating combinations. The integrality of the groups follows by stabilisation of the integral forms. $\square$

## Summary

The octonion algebra defines geometry on the imaginary space $\operatorname{Im}\mathbb{O}\cong\mathbb{R}^7$ and on $\mathbb{O}\cong\mathbb{R}^8$. On the imaginary space the cross product $u\times v = \operatorname{Vect}(uv)$ satisfies $\lvert u\times v\rvert^2 = \lvert u\rvert^2\lvert v\rvert^2 - \langle u,v\rangle^2$ and $u\times(u\times w) = \langle u,w\rangle u - \lvert u\rvert^2w$; it gives the alternating three-form $\varphi(u,v,w) = \langle u\times v,w\rangle$, whose stabiliser in $GL_7(\mathbb{R})$ is $G_2$ and whose nonzero values on basis triples are exactly the seven Fano lines.

The spheres carry structure from the algebra: $S^7$ is parallelizable and homogeneous, $S^7 = \operatorname{Spin}(7)/G_2$, and it is the total space of the Hopf fibrations $S^3\to S^7\to S^4$ and $S^7\to S^{15}\to S^8$; $S^6$ carries the almost complex structure $J_uv = u\times v$, which is nearly Kähler but not integrable. The octonionic projective plane, equivalently the Cayley plane $\mathbb{OP}^2 = F_4/\operatorname{Spin}(9)$ of real dimension $16$, is a Moufang plane that is not Desarguesian, with sectional curvature in $[\tfrac14,1]$ and cohomology $\mathbb{Z}[x]/(x^3)$ in degree $8$; its lack of coordinates is the incidence-theoretic form of the non-associativity of $\mathbb{O}$.

Finally the forms $\varphi$, its dual $\psi$ and the Cayley form $\Phi = e^0\wedge\varphi + \psi$ are calibrations on $\mathbb{R}^7$ and $\mathbb{R}^8$ whose equality planes are the associative, coassociative and Cayley planes; they are the variational face of the algebra and the point of contact with the manifolds of exceptional holonomy.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{O}$, $e_0,\dots,e_7$ | Octonion algebra, basis with $e_k^2 = -e_0$ for $k\geq1$ |
| $\operatorname{Im}\mathbb{O}\cong\mathbb{R}^7$ | Imaginary subspace, orthonormal basis $e_1,\dots,e_7$ |
| $\langle x,y\rangle = \operatorname{Sc}(x\bar y)$ | Inner product, Euclidean metric |
| $u\times v = \operatorname{Vect}(uv)$ | Cross product on $\operatorname{Im}\mathbb{O}$ |
| $\varphi(u,v,w) = \langle u\times v,w\rangle$ | Associative three-form, $G_2 = \operatorname{Stab}\varphi$ |
| $\psi = *\varphi$, $\Phi = e^0\wedge\varphi+\psi$ | Coassociative four-form, Cayley four-form on $\mathbb{O}$ |
| $S^6$, $S^7$ | Unit spheres of $\operatorname{Im}\mathbb{O}$ and of $\mathbb{O}$ |
| $J_uv = u\times v$ | Nearly Kähler almost complex structure on $S^6$ |
| $\mathbb{OP}^2 = F_4/\operatorname{Spin}(9)$ | Cayley plane, $\dim_{\mathbb{R}} = 16$, Moufang, not Desarguesian |
| $[x_0:x_1:x_2]$ | Octonionic homogeneous coordinates on $\mathbb{OP}^2$ |
| $\mathfrak{h}_3(\mathbb{O})$ | Exceptional Jordan algebra of Hermitian $3\times3$ matrices |
| $F_4$, $G_2$, $\operatorname{Spin}(7)$ | Structure groups of the plane, the imaginary space and the sphere |



## Further Reading

- John C. Baez, "The octonions", *Bulletin of the American Mathematical Society* **39** (2002), 145–205, for the cross product, the projective plane and the Hopf fibrations.
- F. Reese Harvey and H. Blaine Lawson, "Calibrated geometries", *Acta Mathematica* **148** (1982), 47–157, for the calibration inequality and the associative, coassociative and Cayley calibrations.
- F. Reese Harvey, *Spinors and Calibrations* (Academic Press, 1990), for the octonionic forms, the cross product and the exceptional calibrations.
- Tonny A. Springer and Ferdinand D. Veldkamp, *Octonions, Jordan Algebras and Exceptional Groups* (Springer, 2000), for the Cayley plane, its incidence structure and the Jordan model.
- Ruth Moufang, "Alternativkörper und der Satz vom vollständigen Vierseit", *Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg* **9** (1933), 207–222, for the Moufang planes and the failure of Desargues.
- Alfred Gray, "Nearly Kähler manifolds", *Journal of Differential Geometry* **4** (1970), 283–309, for the nearly Kähler structure on $S^6$ and the non-integrability of its almost complex structure.
- Arthur L. Besse, *Manifolds all of whose Geodesics are Closed* (Springer, 1978), for the rank-one symmetric spaces, their curvatures and their cohomology.
