
# __Projective Geometric Algebra and Dual Quaternions__

## Introduction

The rigid motions of space form a group of six parameters, three of rotation and three of translation, and it is not a subgroup of any of the classical groups acting on three-dimensional space: a rigid motion of a body is not determined by a rotation about a fixed point. Two constructions give the group linearly. The first is the algebra of **dual quaternions**, in which a rigid motion is a versor of a four-dimensional algebra over the ring of dual numbers, and in which the interpolation of rigid motions is the interpolation of quaternions. The second is **projective geometric algebra**, the Clifford algebra of a degenerate quadratic form of signature $(3,0,1)$, in which the plane is the primitive object, the line and the point are wedges of planes, incidence is the meet of blades, and a rigid motion is a versor acting by the sandwich on all of them at once.

This article develops the two constructions and their relation. The degeneracy of the form is the point of the second: the ideal element of the projective space is null, so that the translations are rotations about the ideal plane rather than transformations of a non-degenerate algebra, and the algebra is the smallest one that carries the incidence of projective geometry together with the metric of Euclidean geometry. The dual quaternions are the even part of that algebra, and the study of rigid motions in them is the older form of the same theory.

The Clifford algebra, the geometric product, the grade decomposition and the contraction are from *The Clifford Algebra* and *The Geometric Product and the Grade Decomposition*; the degenerate Clifford algebras, the radical and the filtration are from *Degenerate Clifford Algebras and the Radical* and *The Filtration and the Associated Graded Algebra*; the volume element, the duality and the Hodge star are from *The Volume Element, Duality and the Hodge Star*; the versors, the rotors, the sandwich action and the exponentiation of a bivector are from *Versors, Rotors and the Sandwich Action*; the quaternions, the rotation group and the quaternion double cover are from *Quaternion Rotations and Reflections* and *The Rotation and Reflection Groups in the Biquaternion Algebra*; the dual numbers are from *The Number Systems as Clifford Algebras*; the biquaternion algebra and its zero divisors are from *The Biquaternion Algebra as a Clifford Algebra*; the null vectors and the sphere vocabulary of the conformal model are from *The Conformal Model of Euclidean Space*. Nothing owned by those entries is re-derived.

## The Projective Model of Space

### The Degenerate Algebra

**Definition.** Let $V=\mathbb{R}^{3,0,1}=\mathbb{R}^3\oplus\mathbb{R}e_0$ with the form $q$ positive definite on $\mathbb{R}^3$ and $q(e_0)=0$, the vector $e_0$ being orthogonal to $\mathbb{R}^3$ and spanning the radical. The **projective geometric algebra** of the three-dimensional space is the Clifford algebra

$$
\mathrm{Cl}_{3,0,1}=\mathrm{Cl}(V,q),
$$

of dimension $2^4=16$.

**Remark.** The degeneracy is essential and not a defect: the vector $e_0$ is the point at infinity of the projective completion, and the fact that it is null is what lets a translation be a rotation about it. The algebra is filtered and not graded by the length of its products, in the sense of *The Filtration and the Associated Graded Algebra*, and the exterior algebra of $V$ is its associated graded algebra; the elements of the algebra are read as projective objects of grade one, two and three.

### Planes, Lines and Points

**Definition.** The vectors of the algebra are the **planes**: a plane with unit Euclidean normal $a$ and offset $d$, written $a\cdot x=d$, is the vector

$$
\pi=a+de_0 .
$$

Lines are the wedges of two planes, points are the wedges of three planes, and the whole space is the pseudoscalar $e_1e_2e_3e_0$.

**Theorem.** The incidence of projective geometry is the wedge of the representatives:

1. the line of intersection of two planes is the wedge $\pi_1\wedge\pi_2$, and the plane $\pi$ contains the point $P$ exactly when $\pi\wedge P=0$;
2. the point of intersection of three planes is the wedge $\pi_1\wedge\pi_2\wedge\pi_3$, so the plane through three points and the point on three planes are read off from the same wedge;
3. the join of two objects is obtained from the meet of their duals by the duality of the algebra, which pairs the blades of complementary grade, so that the line through two points and the plane through three points are computed from the same products as their meet counterparts.

**Proof.** Write a point as the wedge of three planes through it. Then a plane contains the point exactly when adjoining it to the wedge does not increase the grade, which is the condition $\pi\wedge P=0$; two planes in general position have a line common to them, which is the join of the two, and the wedge of the two planes is the blade of common points, of grade two, so the wedge is the line; the same argument one step further gives the point of three planes. The join statements are the duality of *The Volume Element, Duality and the Hodge Star*, applied with the care that the degeneracy of the form requires for the ideal elements. $\square$

**Remark.** The correspondence with the conformal model is the reason the plane is taken as primitive here: in the conformal model the point is primitive and the sphere is a vector, while in the projective model the plane is primitive and the point is a wedge of three planes. The two models are dual descriptions of the same incidence, and the projective one is the more economical when the objects of interest are planes and lines and the transformations are rigid motions.

## Rigid Motions as Versors

### The Ideal Plane and the Rotors

**Theorem.** The rotations of the Euclidean part of the algebra are the rotors of $\mathrm{Cl}_{3,0}$, extended to the whole algebra; the translations are the rotors

$$
T_t=1-\tfrac12 te_0 ,
$$

with $t$ a Euclidean vector and $e_0$ the null generator of the radical, so that $t e_0$ has square zero and the exponential terminates.

**Proof.** That the rotations of the Euclidean part are the rotors of $\mathrm{Cl}_{3,0}$ is in *Quaternion Rotations and Reflections*; the extension acts on the whole algebra because the construction is by the sandwich and the extra generator is annihilated. For the translations: $(te_0)^2=q(t)q(e_0)=0$, so $\exp(-\tfrac12te_0)=1-\tfrac12te_0$; the norm is $1$, so it is a rotor, and its sandwich action on the planes is the translation of the planes by $+t$, the computation being the degenerate analogue of the one for the conformal model. $\square$

**Corollary (screw motions).** Every rigid motion of space is a rotor of the algebra, and every rotor is the exponential of a bivector, so every rigid motion is the exponential of a bivector and is therefore a **screw motion**: a rotation about an axis together with a translation along it.

**Proof.** The composition of a rotation and a translation is a rotor, and by the Chasles theorem every rigid motion of space is a screw motion; the exponential statement is the theorem on the exponentiation of bivectors of *Versors, Rotors and the Sandwich Action*, and the two descriptions agree because the exponential of a general bivector of the algebra is a rotation about a line together with a translation along it. $\square$

### The Even Part and the Dual Quaternions

**Definition.** The **dual numbers** are $\mathbb{D}=\mathbb{R}[\varepsilon]/(\varepsilon^2)$, and the **dual quaternions** are the algebra

$$
\mathbb{D}\mathbb{H}=\mathbb{H}\otimes\mathbb{D}=\mathbb{H}[\varepsilon]/(\varepsilon^2),
$$

of dimension eight over $\mathbb{R}$.

**Theorem.** The even part of the projective geometric algebra is isomorphic to the dual quaternions:

$$
\mathrm{Cl}^0_{3,0,1}\cong\mathbb{D}\mathbb{H} .
$$

**Proof.** Both are eight-dimensional, and the even part is generated by the products $e_ie_j$ of the Euclidean generators, which are the quaternion units, and by the products $e_ie_0$, which are those units multiplied by the nilpotent element $\omega=e_1e_2e_3e_0$; the element $\omega$ lies in the even part, is central there and has square zero, so the even part is the quaternions extended by a central nilpotent. $\square$

**Corollary.** A rigid motion is a unit dual quaternion, and the action of a rigid motion on a point is the sandwich action of the unit dual quaternion on the dual quaternion representing the point.

**Proof.** Immediate from the identification and the theorem on the versors. $\square$

## The Dual Quaternions at Work

### The Unit Dual Quaternions

**Theorem.** A dual quaternion is written $q=q_0+\varepsilon q_1$ with $q_0,q_1\in\mathbb{H}$; it is a unit when it satisfies the two conditions

$$
N(q_0)=1,\qquad B(q_0,q_1)=0 ,
$$

where $N$ and $B$ are the quaternionic norm and inner product, so that the group of unit dual quaternions is six-dimensional and is the double cover of the group of rigid motions:

$$
\{q:\ N(q)=1\}\longrightarrow SE(3),
$$

with kernel $\{\pm1\}$.

**Proof.** The norm of $q_0+\varepsilon q_1$ is $N(q_0)+\varepsilon\,2B(q_0,q_1)$ in the dual numbers, and it equals $1$ in $\mathbb{D}$ exactly when $N(q_0)=1$ and $B(q_0,q_1)=0$. The first condition is the unit sphere of the quaternions, of dimension three, and the second is a linear condition on $q_1$, cutting the six real dimensions of $q_1$ down to three; the total is six, equal to the dimension of the group of rigid motions, and the map to $SE(3)$ is the sandwich action, which forgets the sign. $\square$

**Corollary (the action on points).** The image of a point $p\in\mathbb{R}^3$ is the sandwich

$$
P\longmapsto q\,P\,q^{-1},\qquad P=1+\varepsilon p ,
$$

where $p$ is identified with the quaternion with zero real part and $q$ is the unit dual quaternion of the motion, and the result is again of the form $1+\varepsilon p'$ with $p'$ the image of the point.

**Proof.** The expression $P=1+\varepsilon p$ represents the point, being the point vector translated to the dual-number form, and the sandwich by a unit dual quaternion is an automorphism of the algebra; taking the $\varepsilon$ part of the result gives the transformed point, the computation being the quaternionic form of the composition of a rotation and a translation. $\square$

**Remark (interpolation).** The reason the dual quaternions are the standard tool for rigid motion interpolation is that they carry the group linearly: a screw motion is a unit dual quaternion, the logarithm of a unit dual quaternion is a bivector of the algebra and hence a screw axis with a pitch, and the interpolation of two unit dual quaternions along the exponential of the difference of the logarithms is the screw interpolation of the motions. The same construction in the quaternions is the interpolation of rotations by the exponential of a bivector, which is in *Versors, Rotors and the Sandwich Action*.

## The Two Constructions Compared

**Theorem.** The following three descriptions of the group of rigid motions of space agree:

1. the rotors of the degenerate Clifford algebra $\mathrm{Cl}_{3,0,1}$, modulo sign;
2. the unit dual quaternions, which are the even part of that algebra, modulo sign;
3. the group $SE(3)$ of orientation-preserving isometries of $\mathbb{R}^3$.

**Proof.** The first two are identified by the theorem on the even part, and the second and third by the theorem on the unit dual quaternions. $\square$

**Remark (the projective model and the conformal model).** The two models of the corpus serve different purposes and are not interchangeable: the projective model has a degenerate form and the plane as primitive, and it describes the rigid motions, the incidence of planes, lines and points, and the screw motions; the conformal model of *The Conformal Model of Euclidean Space* has a non-degenerate form of signature $(n+1,1)$ and the point as primitive, and it describes the conformal transformations and the spheres. The rigid motions form a subgroup of the conformal group, and the passage from the conformal model to the projective one is the passage from the non-degenerate form with the two null vectors to the degenerate form with one.

**Remark (why the degeneracy is the economy).** The conformal model needs two extra dimensions and a non-degenerate form; the projective model needs one extra dimension and a degenerate form, and in exchange it describes the rigid motions and the projective incidence but not the dilations or the inversions. Which model to use is decided by which transformations and which objects are wanted: for planes, lines, points and rigid motions the degenerate algebra is smaller and its duality is the classical duality of projective geometry; for spheres, circles and conformal transformations the non-degenerate algebra of two extra dimensions is the one that has the objects as vectors.

## Summary

The **projective geometric algebra** of space is the Clifford algebra $\mathrm{Cl}_{3,0,1}$ of a degenerate form: the Euclidean space of dimension three together with one orthogonal generator $e_0$ of square zero, spanning the radical. Planes are the vectors, $a\cdot x=d$ being the plane $\pi=a+de_0$; lines are the wedges of two planes, points the wedges of three, the whole space the pseudoscalar. A plane contains a point exactly when the wedge of the two vanishes, the intersection of two planes being the wedge of their vectors and the intersection of three the wedge of all three; the join of two objects is obtained from the meet of their duals by the duality that pairs blades of complementary grade, so that the line through two points and the plane through three are computed from the same products as their meet counterparts. The degeneracy is what makes the model economical: the ideal element of the projective completion is null, and the ordinary Euclidean metric lives on the non-degenerate part.

The **rigid motions** are the rotors of this algebra, the rotations being the rotors of the Euclidean part and the translations being the rotors $T_t=1-\tfrac12te_0=\exp(-\tfrac12te_0)$, whose generator has square zero. Every rigid motion is a rotor, every rotor is the exponential of a bivector, and therefore every rigid motion is a screw motion, a rotation about an axis together with a translation along it. The **even part** of the algebra is the algebra of **dual quaternions** $\mathbb{D}\mathbb{H}=\mathbb{H}[\varepsilon]/(\varepsilon^2)$ of dimension eight, a unit dual quaternion $q_0+\varepsilon q_1$ being characterised by the two conditions $N(q_0)=1$ and $B(q_0,q_1)=0$, which cut the eight dimensions to the six of the group of rigid motions; the group of unit dual quaternions is the double cover of $SE(3)$, and it acts on the point $P=1+\varepsilon p$ by the sandwich $P\mapsto qPq^{-1}$. The three descriptions — the rotors of $\mathrm{Cl}_{3,0,1}$, the unit dual quaternions, and the group $SE(3)$ — agree. The construction is the degenerate and economical counterpart of the conformal model: the projective model takes the plane as primitive, describes the rigid motions and the projective incidence, and carries one extra null dimension, while the conformal model takes the point as primitive, describes the conformal transformations and the spheres, and carries two extra dimensions with a non-degenerate form.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{R}^{3,0,1}$ | Euclidean part plus a radical generator |
| $e_0$, $q(e_0)=0$ | The null generator of the radical, the ideal point |
| $\mathrm{Cl}_{3,0,1}$ | Projective geometric algebra, dimension $16$ |
| $\pi=a+de_0$ | Plane $a\cdot x=d$ |
| $\pi_1\wedge\pi_2$, $\pi_1\wedge\pi_2\wedge\pi_3$ | Line and point, the blades of the planes through them |
| $T_t=1-\tfrac12te_0$ | Translation as a rotor |
| $\mathrm{Cl}^0_{3,0,1}\cong\mathbb{D}\mathbb{H}$ | Dual quaternions, dimension $8$ |
| $\mathbb{D}=\mathbb{R}[\varepsilon]/(\varepsilon^2)$ | Dual numbers |
| $q=q_0+\varepsilon q_1$ | Dual quaternion |
| $N(q_0)=1$, $B(q_0,q_1)=0$ | Unit conditions, six-dimensional |
| $P\mapsto qPq^{-1}$, $P=1+\varepsilon p$ | Action on a point |
| $SE(3)$ | Group of rigid motions |

## Further Reading

- Charles Gunn, *Geometry, Kinematics and Rigid Body Mechanics in Cayley–Klein Geometries* (thesis, Technische Universität Berlin, 2011), for projective geometric algebra, the degenerate form and the rigid motions.
- Leo Dorst, Daniel Fontijne and Stephen Mann, *Geometric Algebra for Computer Science* (Morgan Kaufmann, 2007), for the projective model and its computational use.
- Ken Shoemake, *Animating rotation with quaternion curves* (SIGGRAPH 1985), and Ladislav Kavan, Steven Collins, Ji\v{r}\'i \v{Z}\'ara and Carol O'Sullivan, *Dual quaternions for rigid transformation blending* (2006), for the interpolation of rigid motions by dual quaternions.
- J. Michael McCarthy, *An Introduction to Theoretical Kinematics* (MIT Press, 1990), for the screw theory of rigid motions and its algebraic form.
- John Conway and Derek Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the quaternions and the double covers used throughout.
