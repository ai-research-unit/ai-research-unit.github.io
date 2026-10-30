# __The Subspaces of $\mathbb{C}^2$__

## Introduction

This article classifies the subspaces of the complex two-space: the complex subspaces, the real subspaces, the subspaces selected by the three canonical forms, and the Grassmannians that parametrise them. It is the place where the forms of the previous article acquire a geometric meaning: the isotropic lines of $B$ and the Lagrangian planes of $\omega$ and $\Omega$ are subspaces, and their classification is the first geometric statement of the category.

The article treats the subspaces as sets and as points of a Grassmannian. It does not treat the topology of the Grassmannians beyond their dimension and their identification, which are *Grassmannians and Stiefel Manifolds* and *Projective Geometry*; it does not treat the group actions, which are *The Classical Groups of $\mathbb{C}^2$*; and it does not treat the projective compactification, which is *The Compactifications of $\mathbb{C}^2$*.

**The two classifications that matter are the complex one, which has three terms, and the real one, which has five dimensions but only two kinds of plane in the middle.** The article states both, then reads the forms on them.

## The Complex Subspaces

**A complex subspace of $\mathbb{C}^2$ has dimension $0$, $1$ or $2$, and the subspaces of dimension one are the points of the projective line.**

**Definition.** A **complex subspace** is a subset $W\subset\mathbb{C}^2$ closed under addition and under multiplication by complex scalars. A **complex line** is a complex subspace of dimension $1$; a **complex hyperplane** is a complex subspace of dimension $1$ in the dual sense, that is the kernel of a nonzero complex-linear form.

**Proposition (the three dimensions).** The complex subspaces are $\{0\}$, the complex lines $L=\mathbb{C}v$ with $v\neq0$, and $\mathbb{C}^2$.

*Proof.* A subspace of dimension $0$ is $\{0\}$ and one of dimension $2$ is the whole space. In dimension $1$ every nonzero vector spans the space, so the subspace is $\mathbb{C}v$; two nonzero vectors span the same line exactly when each is a complex multiple of the other.

**Definition.** The **projective line** is the set of complex lines,
$$
\mathbb{CP}^1=\{L\subset\mathbb{C}^2:\dim_{\mathbb{C}}L=1\}=\bigl(\mathbb{C}^2\setminus\{0\}\bigr)/\mathbb{C}^{\times},
$$
with homogeneous coordinates $[z_1:z_2]$, the class of $(z_1,z_2)$. The charts $z_2\neq0$ and $z_1\neq0$ identify $\mathbb{CP}^1$ with two copies of $\mathbb{C}$, glued by $t\mapsto 1/t$.

**Proposition (the projective line is a sphere).** The space $\mathbb{CP}^1$ is homeomorphic to $S^2$, and its real dimension is $2$.

*Proof.* The chart $z_2\neq0$ gives $[z_1:z_2]=[t:1]$ with $t=z_1/z_2$, and the chart $z_1\neq0$ gives $[1:s]$ with $s=z_2/z_1=1/t$; the two copies of $\mathbb{C}$ are glued by $t\mapsto 1/t$ on the punctured plane, which is the one-point compactification of $\mathbb{C}$, hence $S^2$. The real dimension is the complex dimension plus one, that is $2$.

**Proposition (two lines span, two hyperplanes meet).** Two distinct complex lines span $\mathbb{C}^2$; two distinct complex hyperplanes meet only at the origin.

*Proof.* Two distinct lines $L_1,L_2$ have $L_1\cap L_2=\{0\}$ and dimensions adding to $2$, so their sum has dimension $2$. Two distinct hyperplanes $H_1=\ker\ell_1$ and $H_2=\ker\ell_2$ have intersection of dimension $1+1-2=0$, since the two forms are independent and $H_1+H_2=\mathbb{C}^2$.

### The Flag and the Lattice of Subspaces

**The complex subspaces form the lattice $\{0\}\subset L\subset\mathbb{C}^2$, and a maximal chain is a flag determined by one line.**

**Definition.** A **flag** of $\mathbb{C}^2$ is a chain
$$
0\subset L\subset\mathbb{C}^2,\qquad \dim_{\mathbb{C}}L=1,
$$
and the **flag variety** $\mathrm{Fl}(1,2;\mathbb{C}^2)$ is the set of such chains.

**Proposition (the flag variety is the projective line).** The map $L\mapsto(0\subset L\subset\mathbb{C}^2)$ is a bijection $\mathbb{CP}^1\to\mathrm{Fl}(1,2;\mathbb{C}^2)$.

*Proof.* The chain is determined by its middle term, and every line occurs in exactly one such chain.

**Remark (a lattice, not a chain).** The set of complex subspaces is $\{0\}\cup\mathbb{CP}^1\cup\{\mathbb{C}^2\}$, ordered by inclusion. **It is a lattice of height two and not a chain**: two distinct lines are incomparable, and their join is the whole space while their meet is the origin. A flag is a maximal chain, and the lattice is the union of all the maximal chains, one for each line.

### The Dual

**The dual space has the same dimension, the annihilator reverses the inclusions, and a complex line corresponds to a hyperplane.**

**Definition.** The **dual space** is $V^{*}=\operatorname{Hom}_{\mathbb{C}}(V,\mathbb{C})$, with dual basis $\ell^{1},\ell^{2}$ defined by $\ell^{k}(z)=z_k$. The **annihilator** of a subspace $W$ is
$$
W^{\circ}=\{\ell\in V^{*}:\ell(w)=0\text{ for all }w\in W\}.
$$

**Proposition (the dimension formula).** For every subspace $W$, $\dim W+\dim W^{\circ}=2$, and $W^{\circ\circ}=W$ under the identification $V^{**}=V$.

*Proof.* Choose a basis of $W$ and extend it to a basis of $V$; the dual basis of the extension has exactly $2-\dim W$ elements that vanish on $W$, and they are a basis of $W^{\circ}$. The double annihilator has the same dimension as $W$ and contains it, hence equals it.

**Corollary (lines against hyperplanes).** The annihilator is a bijection between the complex lines and the complex hyperplanes, and a line $L$ is contained in a hyperplane $H$ exactly when $H^{\circ}\subset L^{\circ}$.

*Proof.* A line has annihilator of dimension $1$, hence a hyperplane, and the correspondence is reversed by the dimension formula and involutive by $W^{\circ\circ}=W$. The inclusion reverses under the annihilator.

**Remark (no canonical isomorphism with the dual).** The space and its dual are isomorphic, both of dimension $2$, but **there is no canonical isomorphism between them**: one is supplied by a nondegenerate bilinear form. The form $B$ supplies a symmetric one, $v\mapsto B(v,\cdot)$; the form $\omega$ supplies an alternating one, $v\mapsto\omega(v,\cdot)$, whose inverse is its negative. The choice is a choice of form, and the two choices give different identifications.

## The Real Subspaces

**A real subspace has dimension $0$ to $4$; in dimension $2$ there are exactly two kinds, the complex lines and the totally real planes, and in dimension $3$ there is only one kind.**

**Definition.** A **real subspace** is a subset closed under addition and under multiplication by real scalars. Its **real dimension** is written $\dim_{\mathbb{R}}W$.

**Proposition (the dimensions).** The real subspaces of $\mathbb{C}^2$ have dimensions $0,1,2,3,4$, and the Grassmannian $\mathrm{Gr}_k(\mathbb{R}^4)$ of $k$-planes has dimension $k(4-k)$.

*Proof.* The dimension formula is the standard one for the Grassmannian of a real vector space: a $k$-plane is the row space of a $k\times4$ matrix of rank $k$, and the parameters are $4k$ minus the $k^2$ parameters of the stabiliser $\mathrm{GL}_k(\mathbb{R})$. The values at $k=0,1,2,3,4$ are $0,3,4,3,0$.

**Definition.** A real subspace $W$ is **$J$-invariant** when $JW=W$, and **totally real** when $W\cap JW=\{0\}$.

**Proposition ($J$-invariant is complex).** A real subspace is $J$-invariant exactly when it is a complex subspace; in particular its real dimension is even.

*Proof.* If $JW=W$, the multiplication by $i$ preserves $W$, so $W$ is closed under complex scalars. Conversely a complex subspace is closed under $J$. The real dimension of a complex subspace is twice its complex dimension, hence even.

**Theorem (the two kinds of real plane).** Every real $2$-plane of $\mathbb{C}^2$ is either a complex line or a totally real plane, and the two classes are disjoint.

*Proof.* Let $W$ be a real $2$-plane. The intersection $W\cap JW$ is $J$-invariant, hence complex, so its real dimension is $0$ or $2$. If it is $2$, then $W\cap JW=W$ and $W=JW$, so $W$ is a complex line. If it is $0$, then $W$ is totally real. The two cases are mutually exclusive because a complex line has $W\cap JW=W\neq\{0\}$.

**Proposition (the real $3$-planes).** Every real $3$-plane contains a complex line and is not totally real; no real $3$-plane is complex.

*Proof.* For a real $3$-plane $W$, $\dim(W+JW)\le4$ gives $\dim(W\cap JW)\ge2$; the intersection is $J$-invariant, hence contains a complex line. A complex subspace has even real dimension, so $W$ is not complex.

**Corollary (the real lines).** Every real line is totally real.

*Proof.* A real line fixed by $J$ would be a complex subspace of real dimension $1$, which is impossible.

The real subspaces are collected below. The two middle rows are the content of the theorem.

| $k$ | Real $k$-planes | Complex among them | Dimension of $\mathrm{Gr}_k(\mathbb{R}^4)$ |
|---|---|---|---|
| $0$ | the origin | the origin | $0$ |
| $1$ | real lines | none | $3$ |
| $2$ | complex lines and totally real planes | the complex lines, a $2$-parameter family | $4$ |
| $3$ | real hyperplanes | none | $3$ |
| $4$ | the whole space | the whole space | $0$ |

**Remark (the two families of planes).** The complex lines form a $2$-parameter family inside the $4$-parameter family of real $2$-planes; the totally real planes form the complement, an open dense set. **A real $2$-plane is therefore either complex or totally real, with no intermediate case, and the condition is read on the single number $\dim(W\cap JW)$.**

## The Isotropic Lines of $B$

**The isotropic cone of $B$ is the union of two complex lines; the two lines are real $2$-planes whose links in the unit sphere are two linked circles, and the cone has no real point outside the origin.**

**Theorem (the cone is two lines).** The set $\{z:B(z,z)=0\}$ is $L_+\cup L_-$, where
$$
L_+=\{z_1=iz_2\},\qquad L_-=\{z_1=-iz_2\},
$$
and the two lines meet only at the origin.

*Proof.* This is the theorem of *The Three Canonical Forms on $\mathbb{C}^2$*: $B(z,z)=(z_1+iz_2)(z_1-iz_2)$ and $\mathbb{C}$ is a domain.

**Proposition (the real picture).** The complex cone $B=0$ has no real point except the origin. Its two components are real $2$-planes, and each meets the unit sphere $S^3$ in a great circle; the two circles are disjoint.

*Proof.* If $z\in\mathbb{R}^4$ and $B(z,z)=0$, then $z_1^2+z_2^2=0$ with $z_1,z_2$ real, hence $z_1=z_2=0$. Each line $L_\pm$ is a real $2$-plane through the origin, and its intersection with $S^3$ is a great circle. The two lines meet only at the origin, so the two circles are disjoint.

**Remark (the two circles are linked).** The circles $L_+\cap S^3$ and $L_-\cap S^3$ are two fibres of the Hopf fibration, over the two points $[i:1]$ and $[-i:1]$ of $\mathbb{CP}^1$. **Two distinct fibres of the Hopf fibration have linking number $1$**, so the two circles are linked despite being disjoint (*The Unit Sphere and the Hopf Fibration*).

**Remark (the real and imaginary parts are two quadrics).** The equation $B(z,z)=0$ is one complex equation and therefore two real equations, $\operatorname{Re}B(z,z)=0$ and $\operatorname{Im}B(z,z)=0$. Each defines a real quadric of signature $(2,2)$, a cone over a torus in $S^3$. **Their intersection is the isotropic cone $B=0$, the union of the two complex lines $L_+\cup L_-$**, which meets $S^3$ in the two linked circles above. The complex cone is not the zero set of a single real quadratic form: it is the intersection of the two real cones, not their union.

**Remark (the image in $\mathbb{CP}^1$).** The projectivisation of the cone is the set of its complex lines, that is the two points
$$
[i:1],\qquad[-i:1]
$$
of $\mathbb{CP}^1$. **The quadric $B=0$ meets the line at infinity in these two points**, and the projective picture of the cone is a pair of points, not a curve.

**Remark (the comparison with the split-complex null quadric).** In the split-complex plane the null quadric $x^2-y^2=0$ is the union of the two real lines $x=\pm y$. **The complex cone is the same phenomenon one complex dimension higher**: the two real lines become two complex lines, each of real dimension $2$, and the real points of the complex cone collapse to the origin because the two lines are not defined over $\mathbb{R}$. The split-complex picture is *Split-Complex Null Quadric and Projective Geometry*.

## The Lagrangian Planes

**The Lagrangian subspaces of the two alternating forms are of two different kinds: the complex lines for the holomorphic form and the $\Omega$-Lagrangian planes, a $3$-parameter family inside the $4$-parameter family of totally real planes, for the Kähler form.**

**Definition.** Let $\sigma$ be a nondegenerate alternating form on a real vector space of dimension $2n$. A subspace $W$ is **isotropic** when $\sigma|_{W}=0$, and **Lagrangian** when it is isotropic of dimension $n$.

**Theorem ($\omega$-Lagrangian lines).** For the holomorphic symplectic form $\omega$, the Lagrangian subspaces are exactly the complex lines, and the space of them is $\mathbb{CP}^1$.

*Proof.* The complex dimension is $2$, so a Lagrangian complex subspace has complex dimension $1$, and every complex line is isotropic because $\omega$ is alternating and $\mathbb{C}$-bilinear. The classification of the isotropic subspaces is the theorem of *The Three Canonical Forms on $\mathbb{C}^2$*.

**Definition.** The **Kähler form** is $\Omega=-\operatorname{Im}H=\sum_k dx_k\wedge dy_k$, a real symplectic form on $\mathbb{R}^4$.

**Theorem ($\Omega$-Lagrangian planes).** A real $2$-plane $W$ is Lagrangian for $\Omega$ exactly when $\Omega|_{W}=0$; every such plane is totally real; and the set of them is a $3$-parameter family, the homogeneous space $\mathrm{U}(2)/\mathrm{O}(2)$.

*Proof.* If $W$ contained a complex line $L$, then $\Omega|_{L}$ would be the area form of $L$, nondegenerate, so $\Omega|_{W}\neq0$; hence $W$ is totally real. The unitary group acts transitively on the Lagrangian planes and the stabiliser of the coordinate plane $\mathbb{R}^2\subset\mathbb{C}^2$ is $\mathrm{O}(2)$, so the family is $\mathrm{U}(2)/\mathrm{O}(2)$ of dimension $4-1=3$.

**Proposition (a totally real plane need not be Lagrangian).** The plane $W=\operatorname{span}_{\mathbb{R}}\{e_1,e_2\}$ is Lagrangian, while the plane $W'=\operatorname{span}_{\mathbb{R}}\{e_1,ie_1+e_2\}$ is totally real and not Lagrangian.

*Proof.* Both are totally real: $Je_1=ie_1$ is not in the span of $e_1,e_2$, and $J(ie_1+e_2)=-e_1+ie_2$ is not in the span of $e_1,ie_1+e_2$. On the first, $\Omega(e_1,e_2)=0$; on the second, $\Omega(e_1,ie_1+e_2)=1$.

**Remark (two Lagrangians, two geometries).** The $\omega$-Lagrangian lines are complex and form a compact $2$-parameter family; the $\Omega$-Lagrangian planes are totally real and form a compact $3$-parameter family, the Lagrangian Grassmannian $\mathrm{U}(2)/\mathrm{O}(2)$. **The two words Lagrangian refer to two different forms, and no plane is Lagrangian for both**: a complex line is $\omega$-Lagrangian and $\Omega$-symplectic, and an $\Omega$-Lagrangian plane is totally real and therefore contains no $\omega$-Lagrangian line.

## The Grassmannians

**The complex Grassmannians of $\mathbb{C}^2$ are a point, a sphere and a point; the real ones are a projective space, a quadric hypersurface and a projective space.**

**Definition.** The **Grassmannian** $\mathrm{Gr}_k(F^n)$ is the set of $k$-dimensional subspaces of the vector space $F^n$ over the field $F$.

**Proposition (the complex Grassmannians).** The complex Grassmannians of $\mathbb{C}^2$ are
$$
\mathrm{Gr}_0=\{\{0\}\},\qquad \mathrm{Gr}_1=\mathbb{CP}^1\cong S^2,\qquad \mathrm{Gr}_2=\{\mathbb{C}^2\},
$$
of real dimensions $0,2,0$.

*Proof.* The only subspaces of dimensions $0$ and $2$ are the origin and the whole space, and the one-dimensional ones are the complex lines.

**Proposition (the real Grassmannians).** The real Grassmannians of $\mathbb{R}^4$ are
$$
\mathrm{Gr}_1=\mathbb{RP}^3,\qquad \mathrm{Gr}_2=\text{a quadric hypersurface in }\mathbb{P}^5,\qquad \mathrm{Gr}_3=\mathbb{RP}^3,
$$
of dimensions $3,4,3$.

*Proof.* A real line is a point of $\mathbb{RP}^3$ and a real hyperplane is a point of the dual projective space, again $\mathbb{RP}^3$. A real $2$-plane is the row space of a $2\times4$ matrix of rank $2$, and the Plücker coordinates are the six $2\times2$ minors, subject to the single quadratic Plücker relation; the image is the Klein quadric in $\mathbb{P}^5$, of dimension $4$.

The dimensions are collected below. The complex Grassmannian of complex dimension $k(2-k)$ has real dimension $2k(2-k)$.

| $k$ | $\mathrm{Gr}_k(\mathbb{C}^2)$ | Real dimension | $\mathrm{Gr}_k(\mathbb{R}^4)$ | Real dimension |
|---|---|---|---|---|
| $0$ | a point | $0$ | a point | $0$ |
| $1$ | $\mathbb{CP}^1\cong S^2$ | $2$ | $\mathbb{RP}^3$ | $3$ |
| $2$ | a point | $0$ | the Klein quadric | $4$ |
| $3$ | — | — | $\mathbb{RP}^3$ | $3$ |
| $4$ | — | — | a point | $0$ |

**Remark (incidence).** A complex line and a complex hyperplane are incident when the line is contained in the hyperplane, which under the annihilator is the condition $H^{\circ}\subset L^{\circ}$. **In the projective line the incidence is the equality of a point and its image under the duality**, and the flag variety $\mathrm{Fl}(1,2;\mathbb{C}^2)$ is again $\mathbb{CP}^1$. The general theory is *Grassmannians and Stiefel Manifolds* and *Projective Geometry*.

## Summary

The complex subspaces of $\mathbb{C}^2$ are the origin, the complex lines and the whole space; the lines form $\mathbb{CP}^1\cong S^2$, and a flag $0\subset L\subset\mathbb{C}^2$ is determined by its line. The dual space has dimension $2$, the annihilator satisfies $\dim W+\dim W^{\circ}=2$, and it exchanges lines and hyperplanes; there is no canonical isomorphism $V\cong V^{*}$ without a bilinear form.

The real subspaces have dimensions $0$ to $4$. A real $2$-plane is either a complex line or a totally real plane, according as $\dim(W\cap JW)$ is $2$ or $0$; a real $3$-plane always contains a complex line and is never totally real; a real line is always totally real. The isotropic cone of $B$ is the union of the two complex lines $z_1=\pm iz_2$, which meet only at the origin; it has no real point except the origin, its two components meet $S^3$ in two linked great circles, and its projectivisation is the two points $[i:1]$ and $[-i:1]$ of $\mathbb{CP}^1$. The Lagrangian subspaces are the complex lines for $\omega$, forming $\mathbb{CP}^1$, and the $\Omega$-Lagrangian planes, the $3$-parameter family $\mathrm{U}(2)/\mathrm{O}(2)$ of totally real planes, for $\Omega$; no plane is Lagrangian for both. The Grassmannians are $\mathrm{Gr}_0$ a point, $\mathrm{Gr}_1=\mathbb{CP}^1$, $\mathrm{Gr}_2$ a point in the complex case, and $\mathbb{RP}^3$, the Klein quadric and $\mathbb{RP}^3$ in the real case.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{CP}^1$ | the projective line, the set of complex lines of $\mathbb{C}^2$, homeomorphic to $S^2$ |
| $[z_1:z_2]$ | the homogeneous coordinates of a complex line |
| $\mathrm{Fl}(1,2;\mathbb{C}^2)$ | the flag variety $\{0\subset L\subset\mathbb{C}^2\}$, identified with $\mathbb{CP}^1$ |
| $V^{*}$ | the dual space, with dual basis $\ell^{1},\ell^{2}$ |
| $W^{\circ}$ | the annihilator of $W$, of dimension $2-\dim W$ |
| $JW$ | the image of $W$ under the complex structure |
| totally real | $W\cap JW=\{0\}$ |
| $L_\pm=\{z_1=\pm iz_2\}$ | the two isotropic lines of $B$ |
| $\Omega=\sum_k dx_k\wedge dy_k$ | the Kähler form |
| $\mathrm{Gr}_k(F^n)$ | the Grassmannian of $k$-subspaces of $F^n$ |
| $\Lambda_2=\mathrm{U}(2)/\mathrm{O}(2)$ | the Lagrangian Grassmannian of $\Omega$, of dimension $3$ |

## Further Reading

- [Complex Two-Space](the-complex-two-space.html), for the space, the bases and the complex structure.
- [The Three Canonical Forms on $\mathbb{C}^2$](the-three-canonical-forms-on-the-complex-two-space.html), for the definitions of $B$, $\omega$ and $\Omega$ and the isotropic and Lagrangian computations.
- [The Realification of $\mathbb{C}^2$](the-realification-of-the-complex-two-space.html), for the real reading of the subspaces and the map $J$.
- [The Isotropic Cone of the Bilinear Form on $\mathbb{C}^2$](the-isotropic-cone-of-the-bilinear-form.html), for the cone, its real picture and its projective image.
- [The Unit Sphere and the Hopf Fibration](the-unit-sphere-and-the-hopf-fibration.html), for the two linked circles and the fibration of $S^3$.
- [The Classical Groups of $\mathbb{C}^2$](the-classical-groups-of-the-complex-two-space.html), for the group actions on the lines and on the Lagrangian planes.
- [Grassmannians and Stiefel Manifolds](grassmannians-and-stiefel-manifolds.html), for the general theory of the Grassmannians and the Plücker embedding.
- [Projective Geometry](projective-geometry.html), for the projective line, the duality and the incidence.
- [Split-Complex Null Quadric and Projective Geometry](split-complex-null-quadric-and-projective-geometry.html), for the real two-line cone that this cone complexifies.
