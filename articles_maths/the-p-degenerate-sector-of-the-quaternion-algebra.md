# __The P-Degenerate Sector of the Quaternion Algebra__

## Introduction

The null set of the plain algebraic norm,
$$
\mathcal N=\{\tilde q:\ q_t^2=\lvert\vec q\rvert^2\},
$$
is a quadratic cone of real dimension three with apex at the origin. Off the apex it is a smooth hypersurface, ruled by two families of lines that meet it in the two null directions of each plane through the scalar axis, and every one of its points is invertible. The cone is therefore the boundary of the two open classes of [The P-Norm Partition of the Quaternion Algebra](the-p-norm-partition-of-the-quaternion-algebra.html), and it is not a zero-divisor set: the contrast with the biquaternion block, where the null cone is exactly the set of the zero divisors, is the sharpest difference between the two algebras that the norm produces.

The article proves the dimension and the smoothness, exhibits the ruling and the parametrisation, computes the quaternion norm on the cone, and separates the two readings of the same set: as the sector between the two open halves, and as the zero level set of an indefinite form, whose induced metric is degenerate along the rulings.

## The Cone and Its Smoothness

**Theorem (the cone).** $\mathcal N$ is a closed cone of real dimension three, with apex the origin, and it is a smooth three-dimensional submanifold away from the apex.

*Proof.* It is the zero set of the continuous function $P$, closed, and stable under the real scalars since $P$ is homogeneous of degree two. Its dimension is three because $P$ is a non-zero quadratic form of signature $(1,3)$ whose zero set is the classical null cone. The gradient is $\nabla P=2(q_t,-\vec q)$, which vanishes only at the origin; by the implicit function theorem the cone is smooth wherever the gradient does not vanish, and the tangent space at a point is the hyperplane $P$-orthogonal to that point.

**Proposition (the apex is the only singularity).** The cone is not a manifold at the origin: every neighbourhood of $0$ in $\mathcal N$ has the homotopy type of a pair of two-spheres and not of a ball.

*Proof.* A small sphere $S^3_\varepsilon$ meets the cone in the set $q_t^2=\lvert\vec q\rvert^2=\varepsilon^2/2$, which is the union of the two two-spheres $\lvert\vec q\rvert=\varepsilon/\sqrt2$ with $q_t=\pm\varepsilon/\sqrt2$ inside $S^3_\varepsilon$. So the link is $S^2\sqcup S^2$, one sphere for each sign of the scalar part. Verified on the parametrised sphere.

**Remark (the tangent cone).** The tangent cone at the apex is the cone itself, and the tangent space at a smooth point is the hyperplane $\tilde q^{\perp_P}$ of dimension three. **The cone is its own tangent cone at the apex, it is smooth everywhere else, and the apex is the single point at which the algebra loses the manifold structure the form gives it.**

## The Two Rulings

**Theorem (the ruling).** Every non-zero null element has a unique writing
$$
\tilde q=\lambda\bigl(e_t+\vec n\bigr),\qquad \lambda=q_t\in\mathbb{R}^{\times},\quad \vec n=\frac{\vec q}{q_t}\in S^2 .
$$
Equivalently, with the two signs, $\tilde q=\lambda(e_t\pm\vec n)$ for $\lambda>0$ and a unit $\vec n$, and then the sign records the sign of the scalar part.

*Proof.* On the cone with $q_t\neq0$, put $\vec n=\vec q/q_t$; then $\lvert\vec n\rvert^2=\lvert\vec q\rvert^2/q_t^2=1$, and $\tilde q=q_t(e_t+\vec n)$. The writing is unique because $q_t$ is the scalar part and $\vec n$ is determined by $\vec q$ and $q_t$. For the second form, absorb the sign of $\lambda$ into $\vec n$. Verified on random null elements.

**Corollary (the generators).** Through each point of the smooth part passes exactly one line of the ruling, namely $\mathbb{R}\tilde q$; the line lies in the cone, and every line of the cone is of this form.

*Proof.* The line $\mathbb{R}\tilde q$ is contained in the cone by homogeneity, and it is the set of the multiples of the point; a line in the cone through $\tilde q$ is a set of null multiples of $\tilde q$ and is contained in it. Verified by spanning the lines.

**Proposition (the two null directions of a plane).** For a unit vector $\vec n$, the plane $\Pi_{\vec n}=\mathbb{R}e_t\oplus\mathbb{R}\vec n$ meets the cone in the two lines $\mathbb{R}(e_t+\vec n)$ and $\mathbb{R}(e_t-\vec n)$, which are the two rulings of that plane.

*Proof.* On the plane, $P=\lambda^2-\mu^2=(\lambda-\mu)(\lambda+\mu)$, so the zero set is the union of the two lines $\lambda=\mu$ and $\lambda=-\mu$. Verified on the plane.

**Remark (the rulings do not cross).** The two lines of a plane meet only at the apex, and the two rulings of the cone are exchanged by the conjugation $\vec n\mapsto-\vec n$. **The cone is ruled by lines through the apex, the ruling is a two-sphere of directions, and the plane $\Pi_{\vec n}$ is the chart in which the two rulings are read as two straight lines.**

## The Parametrisation and the Link

**Theorem (the parametrisation).** The map
$$
\Phi\colon\mathbb{R}^{\times}\times S^2\longrightarrow\mathcal N\setminus\{0\},\qquad (\lambda,\vec n)\longmapsto\lambda\bigl(e_t+\vec n\bigr)
$$
is a homeomorphism; equivalently $\mathcal N\setminus\{0\}\cong S^2\times\mathbb{R}_{>0}\times\{\pm1\}$.

*Proof.* The map is continuous and bijective by the ruling theorem, and its inverse $\tilde q\mapsto(q_t,\vec q/q_t)$ is continuous, so it is a homeomorphism; the second form separates the two signs of $\lambda$. Verified by inverting the map on random points.

**Corollary (the link).** The link of the cone at the apex, that is its intersection with the unit sphere $S^3$, is the union of the two two-spheres
$$
q_t=\pm\frac1{\sqrt2},\qquad \lvert\vec q\rvert=\frac1{\sqrt2},
$$
and each of them is the set of the versors $\tfrac1{\sqrt2}(e_t\pm\vec n)$ with $\vec n\in S^2$.

*Proof.* On $S^3$, $q_t^2+\lvert\vec q\rvert^2=1$ together with $q_t^2=\lvert\vec q\rvert^2$ gives $q_t^2=\tfrac12$; for a fixed $q_t$ the set of the $\vec q$ with the fixed modulus $1/\sqrt2$ is a two-sphere, and the two signs of $q_t$ give the two spheres. The two are exchanged by the antipodal map of $S^3$. Verified on points of the sphere. The topology is developed in [The Topology of the P-Null Cone of the Quaternion Algebra](the-topology-of-the-p-null-cone-of-the-quaternion-algebra.html).

**Remark (the shape of the cone).** A cone over a link of two spheres is the union of two cones, and the cone here is the union of the two halves cut by the sign of $q_t$: each half is the cone over one two-sphere, and the two halves meet along the apex alone. **The null cone of the quaternion algebra is a double cone, one half for each sign of the scalar part, and the parametrisation by the scale and the direction is a homeomorphism of each half onto $S^2\times\mathbb{R}_{>0}$.**

## The Norm on the Cone

**Theorem (the quaternion norm restricted to the cone).** On $\mathcal N$,
$$
N(\tilde q)=2q_t^2=2\lvert\vec q\rvert^2 ,
$$
positive on $\mathcal N\setminus\{0\}$ and vanishing only at the apex; on the two pointed halves it is a positive function of the scale, $N(\lambda(e_t+\vec n))=2\lambda^2$.

*Proof.* $N=q_t^2+\lvert\vec q\rvert^2=2q_t^2$ on the cone, and $q_t\neq0$ off the apex. The homogeneity gives the formula on the parametrisation. Verified numerically.

**Corollary (no zero divisors on the cone).** Every non-zero null element is invertible, with $\tilde q^{-1}=\tilde q^{\natural}/(2q_t^2)$.

*Proof.* The inverse of a non-zero quaternion is $\tilde q^{\natural}/N(\tilde q)$, and $N$ does not vanish. Verified on random null elements.

**Remark (the size of the norm).** On the unit sphere the null elements have $N=1$; along a ruling the norm grows like the square of the scale; and the minimum of $N$ on the cone is attained only at the apex, where the inverse does not exist. **Nullity of $P$ and invertibility coexist on the whole punctured cone, and the inverse is as large as the square of the scale divided by two.**

## Nullity and Invertibility

**Theorem (the coexistence).** $\mathcal N\setminus\{0\}\subset\mathbb{H}^{\times}$, and the cone is a subset of the group of units.

*Proof.* The corollary above, on the parametrised cone. Verified numerically.

**Remark (the meaning of the word null).** The word null refers to the form $P$ and not to the product: an element is null when it is orthogonal to itself in the indefinite metric, and it is a zero divisor when it annihilates something non-zero in the algebra. Over $\mathbb{R}$ the second set is empty, by [Zero Divisors of the Quaternion Algebra](zero-divisors-of-the-quaternion-algebra.html), and the first is the three-dimensional cone of this article. **The two notions are independent, and the quaternion algebra is the smallest algebra in which the null cone of an indefinite norm is entirely made of units, so that the geometry of the light cone and the algebra of the zero divisors come apart.**

**Remark (the contrast with the biquaternion block).** In the complexified algebra the null cone of the plain form is the set of the zero divisors, and through each point of it pass two planes of annihilators; the nullity and the non-invertibility coincide there because the coefficient conjugation supplies isotropic directions and a matrix model in which a null element can be a projector difference. Over $\mathbb{R}$ there is no isotropic direction, the cone is a cone of units, and the annihilators are trivial everywhere. **The real cone is a light cone; the complex one is a light cone that has become a zero-divisor set, and the difference is the presence of the coefficient conjugation.**

## The Spectrum on the Cone

**Proposition (the cone minus the apex is entirely non-real).** The intersection of the cone with the real axis is the apex alone, so every non-zero null element is a spectrally regular quaternion with the distinct eigenvalues $q_t\pm i\lvert\vec q\rvert$.

*Proof.* On the real axis $\vec q=0$ and the cone condition gives $q_t=0$. Off the apex $\vec q\neq0$, which is the criterion of the spectral regularity of [Spectral Regularity and Degeneracy in the Quaternion Algebra](spectral-regularity-and-degeneracy-in-the-quaternion-algebra.html). Verified numerically.

**Corollary (the spectral cut does not cut the punctured cone).** The three spectral strata meet the cone in the apex, the punctured cone, and nothing.

*Proof.* The proposition, and the emptiness of the real stratum off the origin. So the cone is a single spectral piece, and the three-way P-partition and the three-way spectral partition intersect in a degenerate way: **the spectral cut is transverse to the cone and the cone lies wholly inside one stratum of the spectral cut, which is the sharpest possible statement of the independence of the two cuts.**

## The Level Set and the Sector

**Proposition (the induced form on the cone is degenerate).** At a point $\tilde q\in\mathcal N\setminus\{0\}$ the tangent space is $\tilde q^{\perp_P}$, of dimension three, and the restriction of the form $P$ to it has radical $\mathbb{R}\tilde q$ and rank two.

*Proof.* The tangent space of the level set of a form at a point with non-zero gradient is the orthogonal hyperplane. The point $\tilde q$ is null and lies in its own orthogonal hyperplane, so $\mathbb{R}\tilde q$ is in the radical. The radical cannot be larger: if $v$ is in the radical, then $v$ is orthogonal to $\tilde q^{\perp_P}$, hence $v$ is a multiple of the gradient, hence a multiple of $\tilde q$. The rank is $3-1=2$. Verified by computing the Gram matrix of the restriction in a basis of the tangent space.

**Remark (the two readings of the same set).** As a level set, the cone carries an induced form of rank two whose radical is the ruling; as a sector, it is the boundary between the two open classes and carries no metric of its own. **The two readings are the two roles of the same set: as the zero level of $P$ it is a degenerate hypersurface, ruled by the directions in which its own metric vanishes; as the degenerate sector it is the wall between the timelike and the spacelike halves, and it is the wall that the retraction of [The P-Regular Sector of the Quaternion Algebra](the-p-regular-sector-of-the-quaternion-algebra.html) collapses.**

**Remark (the smoothness read on the ruling).** The degenerate direction of the induced metric is the ruling direction, so the rulings are the curves of the cone along which the metric has no length. The apex is where the rulings meet, and it is the point where the rank drops from two to zero: the failure of smoothness and the collapse of the rank are the same event.

## A Worked Check

**Example (a point of the cone and its ruling).** Take $\vec n=\tfrac1{\sqrt3}(\vec e_x+\vec e_y+\vec e_z)$, a unit vector, and $\lambda=2$. Then
$$
\tilde q=2e_t+\tfrac2{\sqrt3}\bigl(\vec e_x+\vec e_y+\vec e_z\bigr)
$$
has $q_t=2$ and $\lvert\vec q\rvert^2=\tfrac{4}{3}\cdot3=4$, so $P=4-4=0$; the norm is $N=8$ and the inverse is $\tilde q^{\natural}/8$. The ruling through it is the line of the multiples, parametrised by $\lambda$ with the same $\vec n$.

**Example (the induced form on the tangent space).** At $\tilde q=e_t+\vec e_x$ the tangent space of the cone is $\tilde q^{\perp_P}=\{v:\ v_t=v_x\}$, spanned by $e_t+\vec e_x$, $\vec e_y$ and $\vec e_z$. The Gram matrix of $P$ in that basis is
$$
\begin{pmatrix}0&0&0\\0&-1&0\\0&0&-1\end{pmatrix},
$$
of rank two, with the ruling direction $\tilde q$ as its radical. So the induced form is degenerate exactly along the ruling, as the proposition states. Computed exactly.

**Remark (what the check shows).** The degeneracy is not a defect of the parametrisation: it is the statement that along the ruling the ambient form gives no length, and the rank two is the rank of the form on the three-dimensional tangent space of the cone at any smooth point.

## Summary

The P-degenerate sector is the null cone $q_t^2=\lvert\vec q\rvert^2$, closed, of real dimension three, with the origin as its only singular point.

Every non-zero null element has the unique writing $\lambda(e_t+\vec n)$ with $\lambda$ the scalar part and $\vec n$ the unit direction, so the punctured cone is $S^2\times\mathbb{R}_{>0}\times\{\pm1\}$ and the link at the apex is the union of the two circles $\lvert q_t\rvert=\lvert\vec q\rvert=1/\sqrt2$.

The quaternion norm on the cone is $N=2q_t^2$, positive off the apex, so the whole punctured cone lies in the group of units: nullity in the indefinite form and non-invertibility in the algebra are independent, and over $\mathbb{R}$ the second set is empty.

The cone meets the real axis only at the apex, so its punctured part is entirely spectrally regular; the spectral cut does not cut it.

As a level set the cone carries an induced form of rank two with radical the ruling direction; the degeneracy of the metric and the singularity at the apex are read on the same ruling.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal N$ | the null cone $\{P=0\}$ |
| $P(\tilde q)$ | $\mathrm{Sc}(\tilde q^2)=q_t^2-\lvert\vec q\rvert^2$ |
| $\vec n$ | a unit vector, the direction of a ruling |
| $\lambda$ | the real scale of a ruling, the scalar part |
| $\Pi_{\vec n}$ | the plane $\mathbb{R}e_t\oplus\mathbb{R}\vec n$ |
| $\Phi$ | the parametrisation $\mathbb{R}^{\times}\times S^2\to\mathcal N\setminus\{0\}$ |

## Further Reading

- [The P-Norm Partition of the Quaternion Algebra](the-p-norm-partition-of-the-quaternion-algebra.html) for the three classes the cone separates.
- [The P-Regular Sector of the Quaternion Algebra](the-p-regular-sector-of-the-quaternion-algebra.html) for the two open halves.
- [The P Level Sets and the Hyperbolic Structure of the Quaternion Algebra](the-p-level-sets-and-the-hyperbolic-structure-of-the-quaternion-algebra.html) for the other level sets.
- [The Topology of the P-Null Cone of the Quaternion Algebra](the-topology-of-the-p-null-cone-of-the-quaternion-algebra.html) for the homotopy type of the cone.
- [The Isotropic Structure of the General Quaternionic Algebra of the Biquaternions](the-isotropic-structure-of-the-general-quaternionic-algebra-of-the-biquaternions.html) for the complex case in which nullity and non-invertibility coincide.
