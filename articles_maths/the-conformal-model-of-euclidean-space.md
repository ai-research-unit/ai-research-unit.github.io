
# __The Conformal Model of Euclidean Space__

## Introduction

A conformal transformation of Euclidean space is not linear, and the group of them is not a subgroup of any matrix group acting on the space. It is nevertheless a classical group, of a space two dimensions larger: the group of conformal transformations of the sphere of dimension $n$ is the orthogonal group of a quadratic space of signature $(n+1,1)$, acting on the null cone of that space. The **conformal model** of Euclidean space is the realisation of this fact in a Clifford algebra, in which a point of the space becomes a null vector of the larger space, a sphere or a plane becomes a vector, incidence becomes orthogonality, and a conformal transformation becomes a versor acting by the sandwich.

The construction is the model of Euclidean geometry in which rotations, translations, dilations, inversions and the special conformal transformations are all of one kind, and in which the objects of sphere geometry are linear objects. It is the reason the conformal group of space-time is a classical group of low rank, and it is the setting of a large part of the applications of geometric algebra to graphics and robotics. It must be distinguished from the theory of conformal manifolds and Möbius structures, which is the development of the same ideas without the embedding; that theory is the subject of *Conformal Geometry* and *Möbius and Lie Sphere Geometry*, and the present entry supplies the linear model.

The Clifford algebra, the geometric product, the grade decomposition and the contraction are from *The Clifford Algebra* and *The Geometric Product and the Grade Decomposition*; the volume element, the multivectors and the basis theorem are from *Clifford Algebras in Finite Dimensions*; the versors, the rotors and the sandwich action are from *Versors, Rotors and the Sandwich Action*; the pin and spin groups and the action of the orthogonal group on the null cone are from *The Clifford, Pin and Spin Groups*; the real forms and the isomorphism $\mathrm{Spin}(4,2)\cong SU(2,2)$ are from *The Low-Dimensional Spin Groups and the Exceptional Isomorphisms*; the sphere geometry and the inversions are from *Conformal Geometry* and *Möbius and Lie Sphere Geometry*. Nothing owned by those entries is re-derived.

## The Space of the Model

### The Two Extra Dimensions

**Definition.** Let $\mathbb{R}^{n+1,1}$ be the space

$$
\mathbb{R}^{n+1,1}=\mathbb{R}^n\oplus\mathbb{R}n\oplus\mathbb{R}n_\infty ,
$$

with the vectors $n$ and $n_\infty$ **null**, orthogonal to $\mathbb{R}^n$ and paired by

$$
n^2=0,\qquad n_\infty^2=0,\qquad B(n,n_\infty)=-1,
$$

and with $n$ and $n_\infty$ orthogonal to $\mathbb{R}^n$, on which the form is the standard positive definite one. The **conformal model** of $\mathbb{R}^n$ is the Clifford algebra $\mathrm{Cl}_{n+1,1}$ of this space, together with the embedding of the next subsection.

**Remark (the two conventions).** Some authors use two vectors of norm $+1$ and $-1$ instead of the two null vectors; the two descriptions are related by a change of basis, $n=\tfrac12(u+\bar u)$, $n_\infty=u-\bar u$ up to normalisation, and the null basis is used here because the two extra directions then have the meaning of the origin and of the point at infinity.

### Points as Null Vectors

**Definition.** The **point vector** of a point $x\in\mathbb{R}^n$ is

$$
X=x+\tfrac12|x|^2 n_\infty+n,
$$

where $x$ on the right is the image of the point in $\mathbb{R}^n\subset\mathbb{R}^{n+1,1}$ and $|x|^2=q(x)$.

**Theorem.** For every point $x$ the point vector is null, $X^2=0$, and for two points

$$
B(X,Y)=-\tfrac12|x-y|^2 .
$$

**Proof.** Expand $X^2=q(x)+2B(x,\tfrac12|x|^2n_\infty)+2B(x,n)+2B(\tfrac12|x|^2n_\infty,n)+0+0$, using $n^2=n_\infty^2=0$: the two cross terms with $x$ vanish because $x$ is orthogonal to $n$ and to $n_\infty$, and the last is $\tfrac12|x|^2\cdot2B(n_\infty,n)=-|x|^2$, so $X^2=|x|^2-|x|^2=0$. For the second statement, expand the bilinear form on $X$ and $Y$ in the same way; the terms degenerate to $B(x,y)-\tfrac12|x|^2-\tfrac12|y|^2$, which is $-\tfrac12|x-y|^2$ by the expansion of the square. $\square$

**Corollary.** The Euclidean distance of two points is recoverable from the model, $|x-y|^2=-2B(X,Y)$, and the null cone of $\mathbb{R}^{n+1,1}$ is in bijection with the points of $\mathbb{R}^n$, with the ray of the vector corresponding to the point and the two rays $\lambda n$ and $\lambda n_\infty$ corresponding to the origin and to the point at infinity.

**Proof.** The first statement is the theorem; the second identifies the null vectors $x+\tfrac12|x|^2n_\infty+n$ and rescales them, and the maps $x\mapsto X$ and $X\mapsto$ point are inverse on the rays. $\square$

## Spheres and Planes

### The Incidence Relation

**Definition.** A nonzero vector $s$ of the model **represents** the set of points

$$
\{x:X\cdot s=0\},
$$

the point vector of $x$ being orthogonal to $s$.

**Theorem (circles, spheres and planes).**

1. For a point $c$ and a radius $r>0$, the sphere of centre $c$ and radius $r$ is represented by
   
   $$
   s=c+\tfrac12\bigl(|c|^2-r^2\bigr)n_\infty+n ,
   $$

   which is the point vector of the centre displaced by $-\tfrac12r^2n_\infty$.
2. For a hyperplane $\{x:a\cdot x=d\}$ with a unit normal $a$ and an offset $d$, the hyperplane is represented by

   $$
   s=a+dn_\infty .
   $$

**Proof.** For the sphere, compute $B(X,s)$ with $X$ the point vector of $x$ and $s$ as displayed, using the orthogonality of $n$ and $n_\infty$ to $\mathbb{R}^n$ and $B(X,n_\infty)=-1$, $B(X,n)=-\tfrac12|x|^2$: the result is $-\tfrac12|x-c|^2+\tfrac12r^2$, which vanishes exactly on the sphere. For the hyperplane, $B(X,s)=B(x,a)+dB(x,n_\infty)+\tfrac12|x|^2B(n_\infty,a)+dB(n,n_\infty)$, and all the terms but the first and the last vanish because $x$ and $a$ are orthogonal to $n_\infty$, so the expression is $B(x,a)-d$, which vanishes exactly on the hyperplane. $\square$

**Corollary.** The spheres are the vectors $s$ with $B(s,n_\infty)\neq0$ and the hyperplanes are the vectors with $B(s,n_\infty)=0$; accordingly the hyperplanes are the spheres through the point at infinity, and a point is a sphere of radius zero.

**Proof.** For the sphere of the theorem, $B(s,n_\infty)=B(n,n_\infty)=-1$; for the hyperplane, $B(s,n_\infty)=0$. The last statement follows from the null point vector being of the displayed form with $r=0$. $\square$

### Incidence and Duality

**Theorem.** Let $s_1,\ldots,s_k$ be vectors representing spheres or planes. Then their common points are the solutions of $B(X,s_i)=0$ for all $i$, and the set of such $X$ is the set of $X$ orthogonal to the blade $s_1\wedge\cdots\wedge s_k$. In particular:

1. two spheres meet in a sphere of dimension $n-2$, a circle in $\mathbb{R}^3$, the one-parameter family of points orthogonal to the 2-blade;
2. the intersection of a sphere and a plane is a sphere of dimension $n-2$, and of two planes a space of dimension $n-2$;
3. in $\mathbb{R}^3$ a third sphere cuts the circle of two spheres in two points, the two null directions of the orthogonal complement of the 3-blade.

**Proof.** The conditions $B(X,s_i)=0$ for all $i$ are the statement that $X$ is orthogonal to each $s_i$, hence to their wedge, which is the general duality statement. The dimension of the space of solutions is read off from the grade of the blade: the orthogonal complement of a $k$-blade in the space of dimension $n+2$ has dimension $n+2-k$, and its null rays are the common points, a circle for $k=2$ in three dimensions and two points for $k=3$. $\square$

**Remark.** The stated incidence is the reason sphere geometry becomes linear in this model: a statement about the intersection of spheres becomes a statement about the dimension of the orthogonal complement of a blade, and the algebra of blades is the calculus of the geometry. The full development, including the oriented spheres and the hyperbolic geometry of the space of them, is Lie sphere geometry, recorded in the literature cited below.

## The Conformal Group

### The Orthogonal Group of the Model

**Theorem.** The group $O(n+1,1)$ preserves the null cone, hence acts on the points of $\mathbb{R}^n$ and on the point at infinity, and the action on the points is conformal; conversely every conformal transformation of $\mathbb{R}^n\cup\{\infty\}$ arises this way, and the kernel of the action is $\{\pm1\}$. So

$$
\mathrm{Conf}(\mathbb{R}^n)=\mathrm{Conf}(S^n)\cong O(n+1,1)/\{\pm1\}.
$$

**Proof.** An orthogonal map preserves the form, so it carries null vectors to null vectors, and the induced map on the rays is a bijection of the sphere of directions, hence a transformation of $S^n$; the metric statement of the theorem above, $|x-y|^2=-2B(X,Y)$, shows that the transformation is conformal with respect to the round metric, because it preserves the bilinear form up to a scalar factor on the cone. The converse, that every conformal transformation arises from an orthogonal map, is the classical theorem of Liouville for $n\ge3$ and is verified by enumeration in low dimensions; the kernel is $\{\pm1\}$ because a linear map fixing every point of the cone fixes the whole space. $\square$

**Corollary (dimension check).** The dimension of the conformal group is

$$
\dim O(n+1,1)=\frac{(n+2)(n+1)}{2}=\frac{n(n-1)}{2}+2n+1,
$$

the three terms being the dimensions of the rotations, of the translations and the special conformal transformations together, and of the dilations.

**Proof.** The first expression is the dimension of the orthogonal group of a space of dimension $n+2$; the second collects the rotations of $\mathbb{R}^n$, the two $n$-dimensional families of translations and special conformal transformations, and the one-parameter family of dilations. The equality is immediate. $\square$

### The Transformations as Versors

**Theorem.** The conformal transformations are restrictions of versors of the model acting by the sandwich action; in particular the translation by a vector $t$ is given by

$$
T_t=1-\tfrac12tn_\infty=\exp\bigl(-\tfrac12tn_\infty\bigr),
$$

which is a rotor, with $\widetilde{\mathrm{Ad}}_{T_t}(X)$ the point vector of $x+t$.

**Proof.** The element $tn_\infty$ is the product of two orthogonal vectors, so its square is $q(t)\,q(n_\infty)=0$, and the exponential series terminates: $\exp(-\tfrac12tn_\infty)=1-\tfrac12tn_\infty$. Its norm is $T_t\bar T_t=(1-\tfrac12tn_\infty)(1+\tfrac12tn_\infty)=1$, because $n_\infty t=-tn_\infty$ and $n_\infty^2=0$; so it is a rotor, and its twisted adjoint is the plain one. The computation of $\widetilde{\mathrm{Ad}}_{T_t}(X)$ in the model, using $n_\infty x=-xn_\infty$ and $n_\infty n=-nn_\infty-2$, gives the point vector of $x+t$, the sign of the generator being the one for which the rotation acts as a translation by $+t$ rather than by $-t$. $\square$

**Remark (the four generators).** The rotations are the rotors of the Euclidean part of the model, the translations are the rotors displayed, the dilations are the rotors $\exp\bigl(\tfrac12\ln\lambda\;(n_\infty\wedge n)\bigr)$, whose generator has square one, since $(n_\infty\wedge n)^2=1$, and the special conformal transformations are obtained by conjugating a translation by an inversion. The group generated is the whole of $O(n+1,1)$, and the inversions themselves correspond to the reflections of the model, so the classical statement that the conformal group is generated by inversions is the statement that the orthogonal group is generated by reflections. The development of the versors and of their exponentiation is in *Versors, Rotors and the Sandwich Action*.

## The Lorentzian Case and the Applications

**Example (the conformal group of space-time).** For the Lorentzian four-dimensional space the model is the quadratic space of signature $(4,2)$, and the spin group of the model is

$$
\mathrm{Spin}(4,2)\cong SU(2,2),
$$

by *The Low-Dimensional Spin Groups and the Exceptional Isomorphisms*; the conformal group of Minkowski space is therefore $\mathrm{Spin}(4,2)/\{\pm1\}\cong SU(2,2)/\{\pm1\}$, a classical group of low rank. The special feature of four dimensions is that the group of conformal transformations is of the same size as the group of unitary transformations of a four-dimensional complex space, which is the fact behind the twistor description of the conformal group.

**Remark (the applications).** The model is used wherever spheres and circles are the objects of interest and the transformations are rigid motions or similarities: in the synthesis of rigid and conformal motions in graphics, in the interpolation of rotations and displacements, and in the description of the kinematic chains of robotics. It is also the linear model of the sphere geometry on which the geometry of the sphere and the inversive geometry of the plane are built, and the reference for those subjects is *Conformal Geometry* and *Möbius and Lie Sphere Geometry*.

**Remark (what the model does not do).** The model is a linearisation of the sphere $S^n$ with its conformal structure, not a Riemannian theory: it does not supply a curvature, a connection or a holonomy, and the conformal manifolds of *Conformal Geometry* are not obtained from it by any change of the quadratic space. The distinction is worth keeping: the model is an incidence and transformation theory, and the differential geometry of conformal structures is a different subject.

## Summary

The conformal model embeds Euclidean space in the quadratic space $\mathbb{R}^{n+1,1}=\mathbb{R}^n\oplus\mathbb{R}n\oplus\mathbb{R}n_\infty$ with two orthogonal null vectors $n,n_\infty$ satisfying $B(n,n_\infty)=-1$. A point $x$ is represented by the null vector

$$
X=x+\tfrac12|x|^2n_\infty+n ,\qquad X^2=0,\qquad B(X,Y)=-\tfrac12|x-y|^2 ,
$$

so that the Euclidean distance is recovered from the bilinear form and the null cone is the space together with the point at infinity. A sphere of centre $c$ and radius $r$ is the vector $s=c+\tfrac12(|c|^2-r^2)n_\infty+n$ and a hyperplane $a\cdot x=d$ is the vector $s=a+dn_\infty$; a point lies on the sphere or plane exactly when its point vector is orthogonal to $s$, spheres being the vectors with $B(s,n_\infty)\neq0$ and planes those with $B(s,n_\infty)=0$. Incidence of several spheres and planes becomes the orthogonality of their point vectors to the wedge of the corresponding vectors, so that the intersection of spheres and planes is read off from the grade of a blade, and the classical theorems on the intersections of circles, spheres and planes become statements about that grade.

The group of the model acts on the null cone, hence on the space and its point at infinity, and the action is conformal; conversely every conformal transformation arises from an orthogonal map, so that

$$
\mathrm{Conf}(\mathbb{R}^n)\cong O(n+1,1)/\{\pm1\},\qquad \dim O(n+1,1)=\frac{(n+2)(n+1)}{2},
$$

the dimension splitting into the rotations, the translations and special conformal transformations, and the dilations. Each transformation is a versor of the model acting by the sandwich action: the translation by $t$ is the rotor $1-\tfrac12tn_\infty=\exp(-\tfrac12tn_\infty)$, the dilations are the rotors of the plane of $n$ and $n_\infty$, and the inversions are the reflections, so that the generation of the conformal group by inversions is the generation of the orthogonal group by reflections. In Lorentzian signature the model is the space of signature $(4,2)$ and its spin group is $SU(2,2)$, which is the group-theoretic content of the twistor description of the conformal group. The model is an incidence and transformation theory of the sphere and not a theory of conformal manifolds: it carries no curvature and no connection, and the differential geometry of conformal structures remains the subject of *Conformal Geometry* and *Möbius and Lie Sphere Geometry*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{R}^{n+1,1}$ | The space of the model |
| $n$, $n_\infty$ | Null vectors, $n^2=n_\infty^2=0$, $B(n,n_\infty)=-1$ |
| $X=x+\tfrac12\|x\|^2n_\infty+n$ | Point vector of a point |
| $X^2=0$, $B(X,Y)=-\tfrac12\|x-y\|^2$ | Null cone and the distance |
| $s=c+\tfrac12(\|c\|^2-r^2)n_\infty+n$ | Sphere of centre $c$ and radius $r$ |
| $s=a+dn_\infty$ | Hyperplane $a\cdot x=d$ |
| $B(X,s)=0$ | Incidence |
| $B(s,n_\infty)\neq0$ or $=0$ | Sphere or hyperplane |
| $O(n+1,1)/\{\pm1\}$ | The conformal group |
| $\tfrac{(n+2)(n+1)}{2}$ | Its dimension |
| $T_t=1-\tfrac12tn_\infty$ | Translation as a rotor |
| $\mathrm{Spin}(4,2)\cong SU(2,2)$ | The Lorentzian case |

## Further Reading

- Hongbo Li, David Hestenes and Alyn Rockwood, *Generalized homogeneous coordinates for computational geometry*, in *Geometric Computing with Clifford Algebras* (Springer, 2001), for the conformal model, the null vectors and the representation of spheres.
- David Hestenes, *The design of linear algebra and geometry* (Acta Applicandae Mathematicae 23, 1991), for the conformal model and its relation to the classical groups.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge University Press, 2003), for the conformal model of space-time and the identification of the conformal group with $SU(2,2)$.
- Werner Blaschke and Kurt Reidemeister, *Vorlesungen über Differentialgeometrie III* (Springer, 1923), for Lie sphere geometry and the space of oriented spheres.
- Leo Dorst, Daniel Fontijne and Stephen Mann, *Geometric Algebra for Computer Science* (Morgan Kaufmann, 2007), for the conformal model and its use in graphics and robotics.
- David Hestenes and Garret Sobczyk, *Clifford Algebra to Geometric Calculus* (Reidel, 1984), for the versor action and the sandwich on which the transformations of the model are built.
