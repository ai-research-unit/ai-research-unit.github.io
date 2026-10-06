# __The Slices of the Quaternion Julia Sets__

## Introduction

A four-dimensional set is studied through its sections by the two-dimensional subspaces that carry a complex structure, and the quaternion Julia sets are no exception. The **slices** of $J_c$ are the intersections $J_c \cap \mathbb{C}_\nu$, one for each unit imaginary quaternion $\nu$, the plane $\mathbb{C}_\nu=\operatorname{span}\{e_0,\nu\}$ being a copy of $\mathbb{C}$. There are three facts to be kept apart. First, if the parameter lies in the plane, the plane is invariant and the slice is exactly the ordinary complex Julia set of the corresponding complex parameter; this is the one slice that can be computed by the complex theory alone. Second, if the parameter is real, every slice is a rotation of that one, and the whole four-dimensional set is the rotational hull of a single two-dimensional picture. Third, if the parameter is neither real nor in the chosen plane, the slice is a genuine two-dimensional section of a four-dimensional set, and **no slice determines the set**: the reconstruction requires all of them. The purpose of this article is to state and prove exactly these three facts, to record the discipline they impose on every picture, and to warn against the naive generalisation of the second to the third.

The quadratic map, the critical point, the filled Julia set and the complex planes are from *The Quaternion Quadratic Map and Its Julia Sets*; the parametrisation of the locus and the reduction $\kappa$ are from *The Quaternion Mandelbrot Set*; the complex Julia set and its computation are from *The Julia Sets of a Complex Polynomial*; the rotations and the orthogonal group are from *Quaternion Rotations and Reflections* and *Quaternion Automorphisms and Derivations*; and the dimensions and the coverings used below are from *Fractal Geometry*. The escape radius and the Green's function on a slice are the subject of *The Escape Radius and the Green's Function for Quaternions*, and the dimension of the slices and of the hulls is that of *The Dimension of the Quaternion Julia Sets*. No physics is invoked.

Throughout, $\mathbb{C}_\nu=\operatorname{span}\{e_0,\nu\}$ for $\nu \in S^2=\{\nu\in\operatorname{Im}\mathbb{H}:N(\nu)=1\}$, and $\kappa(c)=c_0+i|\mathbf c|$ is the reduction of the parameter to the complex plane. The plane of the parameter $c$ is $\mathbb{C}_c=\operatorname{span}\{e_0,c\}$.

## The Complex Planes Through the Origin

**Proposition (the family of planes).** The assignment $\nu \mapsto \mathbb{C}_\nu$ is a bijection from $S^2$ onto the set of two-dimensional subalgebras of $\mathbb{H}$ that contain $e_0$, and it is equivariant for the orthogonal action: $\operatorname{Ad}_u(\mathbb{C}_\nu)=\mathbb{C}_{\operatorname{Ad}_u\nu}$ for $u \in S^3$, with $\operatorname{Ad}_u$ acting on $S^2$ by the rotation group. Every quaternion lies in at least one plane, and a quaternion with nonzero vector part lies in exactly one, namely $\mathbb{C}_{\hat{\mathbf q}}$ with $\hat{\mathbf q}=\mathbf q/|\mathbf q|$.

*Proof.* Each $\mathbb{C}_\nu$ is a two-dimensional real subalgebra and is a copy of $\mathbb{C}$ with $\nu$ as a square root of $-e_0$; conversely a two-dimensional subalgebra containing $e_0$ is spanned by $e_0$ and an element $\xi$ with $\xi^2=-e_0$, and the elements with square $-e_0$ are exactly the unit imaginary quaternions, which form $S^2$ by *Quaternion Roots of Minus One*. The equivariance is the fact that an automorphism carries the plane of an axis to the plane of the image of the axis. The last statement is proved in *The Quaternion Quadratic Map and Its Julia Sets*. $\square$

**Definition.** A **slice of the Julia set** $J_c$ is an intersection $J_c \cap \mathbb{C}_\nu$. The slice is **invariant** if $\mathbb{C}_\nu$ is $\mathbb{C}_c$, the plane of the parameter.

## The Invariant Slice

**Theorem (the invariant slice is the complex Julia set).** Let $c \notin \mathbb{R}$ and let $\mathbb{C}_c=\operatorname{span}\{e_0,c\}$ be the plane of the parameter, with the identification $\varphi_c : \mathbb{C}_c \to \mathbb{C}$ sending $c$ to $\kappa(c)=c_0+i|\mathbf c|$; when $c \in \mathbb{R}$ take $\mathbb{C}_c=\mathbb{R}$ and $\varphi_c(c)=c$. Then $\mathbb{C}_c$ is invariant under $f_c$, and

$$
J_c \cap \mathbb{C}_c = \varphi_c^{-1}\bigl(J^{\mathbb{C}}_{\kappa(c)}\bigr) , \qquad K_c \cap \mathbb{C}_c = \varphi_c^{-1}\bigl(K^{\mathbb{C}}_{\kappa(c)}\bigr),
$$

where $J^{\mathbb{C}}_{\kappa}$ and $K^{\mathbb{C}}_{\kappa}$ are the Julia set and the filled Julia set of $z \mapsto z^2+\kappa$. In particular **the slice of the parameter is an honest complex Julia set**.

*Proof.* The invariance of $\mathbb{C}_c$ and the conjugacy of the restriction of $f_c$ to $\mathbb{C}_c$ with $z \mapsto z^2+\kappa(c)$ are the critical slice theorem of *The Quaternion Mandelbrot Set*. A conjugacy of dynamical systems carries bounded orbits to bounded orbits and unbounded orbits to unbounded orbits, so it carries $K_c\cap\mathbb{C}_c$ to $K^{\mathbb{C}}_{\kappa(c)}$; and it is a homeomorphism, so it carries the boundary to the boundary, giving the Julia sets. The real case is the same statement with $\mathbb{R}$ in place of $\mathbb{C}_c$. $\square$

**Remark.** The invariant slice is the only slice that is a complex Julia set in general: for $\nu \neq \pm\hat{\mathbf c}$ the plane is not invariant, the orbit of a point of the slice leaves the slice after one step, and the intersection $J_c\cap\mathbb{C}_\nu$ is a real two-dimensional section and not the Julia set of any complex quadratic map. **A computation of a slice by a complex iteration is legitimate exactly for the invariant slice**; for every other slice the four-dimensional iteration must be used, and it produces a different set.

## The Rotational Hull of a Real Parameter

**Theorem (one slice suffices for a real parameter).** Let $c \in \mathbb{R}$ and let $\nu \in S^2$. Then

$$
K_c = \operatorname{Ad}_{S^3}\bigl(K_c\cap\mathbb{C}_\nu\bigr) , \qquad J_c = \operatorname{Ad}_{S^3}\bigl(J_c\cap\mathbb{C}_\nu\bigr) ,
$$

and for every axis $\nu$ the slice is the same complex Julia set under the identification $\mathbb{C}_\nu \to \mathbb{C}$, $\nu \mapsto i$. Thus **for a real parameter the set is recovered from one slice, and the slices for different axes are congruent**.

*Proof.* This is the hull theorem of *The Quaternion Quadratic Map and Its Julia Sets*, whose proof uses the invariance under the full rotation group $SO(3)$ of a real parameter and the transitivity of the rotations on the spheres of the vector subspace. The congruence of the slices is the invariance together with the same transitivity. $\square$

**Corollary (the profile).** For a real parameter $c$, define the **profile** $\sigma_c \subset \mathbb{R}^2$ by $\sigma_c=\{(q_0,|\mathbf q|) : \tilde q \in J_c\}$, a subset of the closed half-plane. Then $\sigma_c$ determines $J_c$ by

$$
J_c = \{\tilde q \in \mathbb{H} : (q_0,|\mathbf q|) \in \sigma_c\} ,
$$

and $\sigma_c$ is the image of the complex Julia set $J^{\mathbb{C}}_c \subset \mathbb{C}$ under $z=x+iy \mapsto (x,|y|)$. The set is the union of the spheres of radius $|\mathbf q|$ centred at $q_0e_0$ over the points of the profile; **every picture of $J_c$ for a real parameter is the revolution about the real axis of a picture of the complex Julia set.**

*Proof.* The profile determines the point set because a quaternion is determined by its scalar part, the modulus of its vector part and the axis of its vector part, and the invariance under $SO(3)$ makes the axis irrelevant. The identification of the profile is the theorem. $\square$

## General Parameters: Equivariance Instead of a Hull

**Definition.** The **reduction** of a quaternion $\tilde q$ to the plane of the parameter $c$ is

$$
\rho_c(\tilde q) = q_0 + |\mathbf q|\,\hat{\mathbf c} \quad (\mathbf c\neq0,\ \mathbf q\neq0), \qquad \rho_c(\tilde q) = q_0+|\mathbf q|\,e_1 \quad (\mathbf c=0), \qquad \rho_c(q_0)=q_0 ,
$$

the unique point of $\mathbb{C}_c$ (with $\mathbb{C}_0$ interpreted as the plane $\mathbb{C}_{e_1}$) with the same scalar part and the same modulus of the vector part as $\tilde q$; it is the representative of the orbit of $\tilde q$ under the rotation group that can lie in the plane of the parameter, and it is the point of the plane whose rotational hull contains $\tilde q$.

**Proposition (the rotational hull, and the failure of the naive recovery).** For a real parameter $c$ and every axis $\nu$, the saturation $\operatorname{Ad}_{S^3}(K_c\cap\mathbb{C}_\nu)$ is $K_c$, and $\tilde q \in K_c$ if and only if $\rho_c(\tilde q) \in K_c$. For a general non-real parameter the statement is false: with $c=\tfrac12 e_2$ the point $\tilde q$ with coordinates $(0.25,\,0.90,\,0.15,\,-0.21)$ has a bounded orbit, while its reduction $\rho_c(\tilde q)=(0.25,\,0,\,0.9363,\,0)$ — which lies in the plane $\mathbb{C}_{e_2}$ of the parameter — escapes at the third iterate. Hence $\tilde q$ belongs to $K_c$ but to no rotation of $K_c\cap\mathbb{C}_{e_2}$, and the saturation of the slice is a proper subset of the set.

*Proof.* The positive statement for a real parameter is the rotational hull theorem above. For the failure, any rotation preserves the scalar part and the modulus of the vector part, so the rotations of the slice $\mathbb{C}_{e_2}$ are exactly the points whose reduction to $\mathbb{C}_{e_2}$ lies in the slice; if the reduction of $\tilde q$ is not in $K_c$, then no rotation of a point of $K_c\cap\mathbb{C}_{e_2}$ equals $\tilde q$. The two membership facts are the direct iteration of the quaternion product, recorded in the companion file. $\square$

**Remark (why the invariant slice is still the right object).** The failure above does not weaken the invariant slice: it is the only slice that is computable by the complex theory, it carries the critical orbit, and it is the slice whose dimension is compared with the dimension of the whole set in *The Dimension of the Quaternion Julia Sets*. What fails is only the hope that the other slices are rotations of it. **The correct general statement is equivariance and not a hull:**

$$
J_{\operatorname{Ad}_u(c)} = \operatorname{Ad}_u(J_c) , \qquad K_{\operatorname{Ad}_u(c)} = \operatorname{Ad}_u(K_c) ,
$$

from *The Quaternion Quadratic Map and Its Julia Sets*; the whole family over the orbit $SO(3)c$ is one dynamical object read in rotating frames, and a statement about the slices of one member is a statement about the corresponding planes of the whole orbit. The reduction $\rho_c$ intertwines the dynamics for a real parameter, where it generates the symmetry; for a general non-real parameter it does not, and the purely imaginary parameter $c=\tfrac12 e_2$ exhibits the failure; whether it also occurs for a non-real parameter with a nonzero scalar part was not decided by the numerical search recorded in the companion file.

## Reconstruction from All the Slices

**Theorem (the slices determine the set).** For every parameter $c$,

$$
J_c = \bigcup_{\nu \in S^2} \bigl(J_c \cap \mathbb{C}_\nu\bigr) , \qquad K_c = \bigcup_{\nu \in S^2} \bigl(K_c \cap \mathbb{C}_\nu\bigr) .
$$

*Proof.* Every quaternion lies in at least one plane $\mathbb{C}_\nu$ by the first proposition of the article, and the union is therefore the whole set; the reverse inclusion is trivial. $\square$

**Remark (what the union costs).** The theorem is a tautology with content only in what it forbids: because the union is over the whole sphere $S^2$, the reconstruction of a four-dimensional set from slices is not the reconstruction from *finitely many* or from *one*; a numerical picture of a quaternion Julia set is a picture of a slice, and a finite collection of slices is a finite collection of sections and not the set. The computational content of the article is therefore the invariant slice of the theorem above, its congruence with the other slices for a real parameter, and the equivariance as the tool that moves a computation from one parameter to a rotated one.

## The Slice Discipline

**Remark (naming the slice).** Every picture of a quaternion Julia set in the corpus is a picture of a slice, and the slice is named with the picture; a picture with no slice named is a picture of an unspecified set. The reason is the third fact of the introduction: the slice is the whole specification of what is drawn. This is the form the rule takes in this subcategory, and it is stated again wherever a picture occurs.

**Remark (what is seen in a slice).** On the invariant slice the picture is the classical complex Julia set, drawn by the escape-time algorithm of *The Julia Sets of a Complex Polynomial*; on any other slice the picture is a real two-dimensional section of a four-dimensional set and is drawn by the quaternion escape-time algorithm of *The Quaternion Mandelbrot Set*, with the same escape radius $R(c)=1+|c|$. The two pictures are not to be confused: the first is a complex Julia set, and the second is not. In particular a symmetry visible in the first need not be visible in the second, and a feature off the invariant slice is not a feature of the complex parameter.

**Remark (the Jordan curve and the quasi-circle, confined to the slice).** A complex Julia set that is a Jordan curve — the circle for $c=0$, and the quasi-circles of the small parameters — is a Jordan curve *inside its plane*; in $\mathbb{H}$ the same locus of parameters is a two-dimensional surface of revolution for a real parameter (the unit sphere for $c=0$), and it is a Jordan curve only in the slice. The distinction between the complex and the quaternion object is the reason the word *slice* is used at all.

## Worked Example

**Example (a slice of three parameters).** The computations are recorded in the companion file.

**(a) Real parameter, $c=0$.** The invariant slice is the unit circle $|z|=1$; the profile is the semicircle $\{(x,y):x^2+y^2=1,y\geq0\}$; and the quaternion set is the unit sphere $S^3$, the surface of revolution of the semicircle by the two-sphere. The slice by any plane is a congruent circle, and one computation gives all of them.

**(b) Real parameter, $c=-1$.** The invariant slice is the basilica Julia set of $z^2-1$, a connected dendrite meeting the real axis in a Cantor set of points; the quaternion set is its revolution about the real axis. The slice by any plane is a rotation of it, by the theorem.

**(c) Non-real parameter, $c=e_1$.** The parameter $e_1$ lies in $K_c$, its orbit being the two-cycle of the critical orbit; the point $0.5e_2$ does not, its orbit being unbounded by direct computation, and the point $0.5e_1$ also does not. The slice $\mathbb{C}_{e_1}$ contains the bounded part and the plane $\mathbb{C}_{e_2}$ does not see it.

**(d) The failure of the naive recovery, $c=\tfrac12 e_2$.** The point $\tilde q$ with coordinates $(0.25,\,0.90,\,0.15,\,-0.21)$ has a bounded orbit, while its reduction $\rho_c(\tilde q)=(0.25,\,0,\,0.9363,\,0)$, a point of the parameter's own plane, escapes at the third iterate. Hence the set is not the saturation of its invariant slice, and the reduction is not a symmetry for this parameter. The failure is not rare: in a random sample of the ball of radius $2$ it occurs at about $2$ per cent of the points, and in the unit ball at about one point in five.

**(e) Equivariance in action.** With $u=(e_1+e_2)/\sqrt2$ one has $\operatorname{Ad}_u(e_1)=e_2$, so $J_{e_2}=\operatorname{Ad}_u(J_{e_1})$ and $K_{e_2}=\operatorname{Ad}_u(K_{e_1})$; the numerical membership of a rotated point in $K_{e_2}$ equals that of its preimage in $K_{e_1}$, verified for random rotations to machine accuracy.

## Summary

The slices of a quaternion Julia set are its intersections with the complex planes $\mathbb{C}_\nu$ through the origin. If the parameter lies in the plane, the plane is invariant and the slice is the complex Julia set of the conjugate complex parameter $\kappa(c)=c_0+i|\mathbf c|$; this is the only slice that a complex iteration computes. If the parameter is real, every slice is a rotation of that one and the whole set is the rotational hull of a single slice, described by its profile in the half-plane; this is the case in which one two-dimensional picture is the whole four-dimensional set. If the parameter is non-real, no slice determines the set: the recovery by the reduction $\rho_c$ fails, as it does at $c=\tfrac12 e_2$, where a point off the parameter's plane has a bounded orbit while its reduction in the plane escapes. The correct general tool is the equivariance $J_{\operatorname{Ad}_u c}=\operatorname{Ad}_u J_c$, and the reconstruction of the set requires the whole sphere of slices. The rule that every picture names its slice is therefore not a stylistic preference but the specification of the object drawn. The escape radius and the potential on a slice are the subject of *The Escape Radius and the Green's Function for Quaternions*, and the dimensions are those of *The Dimension of the Quaternion Julia Sets*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{C}_\nu=\operatorname{span}\{e_0,\nu\}$ | Complex plane of the axis $\nu$, $\nu\in S^2$, $\cong\mathbb{C}$ |
| $\mathbb{C}_c$ | The plane of the parameter, the invariant slice |
| $\kappa(c)=c_0+i\lvert\mathbf c\rvert$ | The complex parameter of the invariant slice |
| $\varphi_c$ | The isomorphism $\mathbb{C}_c\to\mathbb{C}$, $e_0\mapsto1$, $c\mapsto\kappa(c)$ |
| $J_c\cap\mathbb{C}_\nu$ | The slice of the Julia set by the axis $\nu$ |
| $\operatorname{Ad}_{S^3}(X)$ | The rotational hull of $X$ |
| $\sigma_c$ | The profile of $J_c$ in the half-plane, for real $c$ |
| $O(3)$, $O(2)$ | Symmetry of a real member; of a non-real member |

## Further Reading

- John Milnor, *Dynamics in One Complex Variable*, 3rd ed. (Princeton, 2006). The complex Julia sets that are the invariant slices.
- Robert P. Munafo, "Quaternion Julia and Mandelbrot sets" and the associated visualisation literature. The observational slices and the discipline of naming them.
- Paul J. Gomatam and others, "Generalized Mandelbrot set in quaternion space", *Advances in Applied Clifford Algebras* (2006). The critical slice and the reduction of the parameter.
- Kenneth Falconer, *Fractal Geometry: Mathematical Foundations and Applications*, 3rd ed. (Wiley, 2014). The coverings and dimensions, cited to *Fractal Geometry*.
