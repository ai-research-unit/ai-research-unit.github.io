# __The Hyperbolic Geometry of the Split-Complex Julia Sets__

## Introduction

The split-complex plane carries the indefinite form $N(z) = a^2-a'^2$ of signature $(1,1)$, and with it a hyperbolic structure: the group $SO(1,1)$ of **hyperbolic rotations**, the hyperbolas $N = $ const as their orbits, the unit hyperbola $\{N = 1\}$, and the **null quadric** of the form, which in the projective compactification consists of two points at infinity. This article reads the Julia sets of *The Split-Complex Julia Sets* with that structure. It states what the hyperbolic rotations do to the family — the scaling $z \mapsto uz$ carries $f_c$ to a map affinely conjugate to $f_c$ and therefore changes neither the parameter nor the affine class of the Julia set, while the affine automorphisms of $f_c$ are trivial and the set-theoretic symmetries coming from the algebra are the even symmetries $z \mapsto uz$ with $u^2 = 1$ — describes the foliation of the plane by the orbits of $SO(1,1)$ and the trace of the Julia set on each hyperbola, computes the Hausdorff dimension of the split Julia set from the product rule, and translates the notion of a hyperbolic component of the Mandelbrot set into the split parameter plane, where the components become rectangles carrying the product of the Poincaré metrics through the pair of real multipliers.

The article depends on *The Split-Complex Quadratic Family* and *The Split-Complex Julia Sets* for the family and the two sets, on *Hyperbolic Rotations* for the group and the unit hyperbola, and on *Split-Complex Null Quadric and Projective Geometry* for the null quadric, the two points at infinity and the cross-ratio distance. The comparison uses *The Mandelbrot Set and the Quadratic Family*, and the relation to the hyperbolic geometry of the corpus is that of the Kleinian limit sets of *Iterated Function Systems in the Complex Plane*. No physics is invoked.

## The Hyperbolic Structure of the Plane

### The Form and the Group

**Definition.** The **Lorentzian form** of $\mathbb{D}$ is the polar form of the norm,

$$
B(z,w) = ab - a'b' , \qquad z = a+ja', \quad w = b+jb' ,
$$

with Gram matrix $\operatorname{diag}(1,-1)$ in the basis $\{1,j\}$; the associated quadratic form is $N(z) = B(z,z) = a^2-a'^2$. The **hyperbolic rotations** are the linear maps preserving $N$, and their group is

$$
O(1,1) = \{M \in GL(2,\mathbb{R}) : M^{\mathsf{T}}\operatorname{diag}(1,-1)M = \operatorname{diag}(1,-1)\} ,
$$

with identity component $SO^+(1,1) = \{z \mapsto e^{js}z : s \in \mathbb{R}\}$, where $e^{js} = \cosh s + j\sinh s$, a group isomorphic to $(\mathbb{R},+)$.

**Proof.** A linear map is an isometry of $N$ exactly when its matrix preserves the bilinear form; the classification of the elements by the sign of $B$ gives the elliptic, parabolic and hyperbolic types, and a determinant-one isometry fixing the time orientation fixes each of the two null lines and is therefore of the form $M_s = \begin{pmatrix}\cosh s & \sinh s\\ \sinh s & \cosh s\end{pmatrix}$, the multiplication by $e^{js}$. The details are those of *Hyperbolic Rotations*, where the exponential, the rapidity $s$ and the classification are developed.

### The Orbits, the Unit Hyperbola and the Null Quadric

**Theorem.** The orbits of the identity component $SO^+(1,1)$ on the units are the branches of the **hyperbolas** $N(z) = t$: for $t > 0$ the two branches meeting the real axis at $\pm\sqrt t$ and asymptotic to the null lines, and for $t < 0$ the two branches meeting the imaginary axis at $\pm\sqrt{|t|}j$. The **unit hyperbola** $\mathcal{H} = \{N = 1\}$ has the two branches $\mathcal{H}^\pm$, and on each branch the rapidity $s$ with $z = \pm e^{js}$ is an additive parametrisation.

**Proof.** Multiplication by $e^{js}$ preserves $N$ and moves along the level set; conversely on $N(z) = 1$ with $z$ on the right branch one has $z = e^{js}$ for the unique $s$ with $\cosh s = a$, $\sinh s = a'$, and $s$ is additive because $e^{js}e^{jt} = e^{j(s+t)}$. The parametrisation of the other branches is the same up to scale.

**Definition (the null quadric).** The **null cone** is $\mathcal{N} = \{N = 0\} = \mathbb{R}\Pi_+\cup\mathbb{R}\Pi_-$, the two null lines of *Split-Complex Null Quadric and Projective Geometry*; in the projective line $\mathbb{P}(\mathbb{D})\cong\mathbb{RP}^1$ with affine coordinate $t = a'/a$, the **projective null quadric** is the pair of points at infinity $t = \pm1$. The identity component acts on the projective line by the projectivity

$$
t \longmapsto \frac{t+\tanh s}{1+t\tanh s} ,
$$

fixing each of the two points at infinity, and the **hyperbolic distance** between two directions is the cross-ratio distance $d(t_1,t_2) = \tfrac12|\ln(t_1,t_2\,;-1,1)|$ of that article.

**Remark.** The datum of the hyperbolic plane is thus: the two null directions at infinity, the projective line between them, and the cross-ratio distance. The real Julia sets $J_\pm$ of *The Split-Complex Julia Sets* are subsets of two copies of the real line, and the real line is exactly the boundary of the hyperbolic line; the two are related through the idempotent coordinates, and the relation is recorded below.

## The Symmetries of the Family

**Theorem (the affine automorphisms).** The only affine bijection of $\mathbb{D}$ commuting with $f_c(z) = z^2+c$ is the identity, for every $c$.

**Proof.** An affine bijection $h(z) = \alpha z+\beta$ with $h\circ f_c = f_c\circ h$ gives $\alpha(z^2+c)+\beta = (\alpha z+\beta)^2+c$, that is $\alpha z^2+\alpha c+\beta = \alpha^2z^2+2\alpha\beta z+\beta^2+c$. Comparing the coefficients of $z^2$ and of $z$ gives
$$
\alpha = \alpha^2, \qquad 2\alpha\beta = 0 .
$$
The solutions of $\alpha^2 = \alpha$ in $\mathbb{D}$ are $0$, $1$ and the two idempotents $\Pi_\pm$, and only $\alpha = 1$ is a unit; a bijection requires $\alpha$ to be a unit, so $\alpha = 1$, and then $2\beta = 0$ forces $\beta = 0$, because $\mathbb{D}$ has no nonzero element of additive order two. Hence $h$ is the identity.

**Theorem (the even symmetries).** The map $f_c$ is even in the strong sense that $f_c(uz) = f_c(z)$ for every unit with $u^2 = 1$, that is for $u \in \{\pm1,\pm j\}$; hence the Fatou and the Julia sets are invariant under each of the four maps $z \mapsto uz$,
$$
J_c = uJ_c \qquad (u^2 = 1),
$$
although none of the three nontrivial ones commutes with $f_c$. Among the hyperbolic rotations $e^{js}$ only $u = 1$ satisfies $u^2 = 1$, so no nontrivial rotation of $SO^+(1,1)$ preserves $J_c$: the invariance is the even symmetry of the family, not a rotation symmetry.

**Proof.** $f_c(uz) = u^2z^2+c = z^2+c = f_c(z)$ when $u^2 = 1$, and then $f_c^n(uz) = f_c^n(z)$ for every $n$ by induction. Since $z \mapsto uz$ is a bi-Lipschitz bijection of the plane, the family $\{f_c^n\}$ is equicontinuous at $z$ if and only if it is at $uz$, so both sets are invariant. For a hyperbolic rotation $u = e^{js}$ one has $u^2 = e^{2js}$, which is $1$ only for $s = 0$.

**Theorem (the scaling action).** Let $u \in \mathbb{D}$ be a unit and let $h(z) = uz$. Then

$$
h^{-1}\circ f_c\circ h\,(z) = u z^2 + \frac{c}{u} ,
$$

a quadratic polynomial with leading coefficient $u$, and its normalised parameter is $c$: the polynomial $uz^2+c/u$ is affinely conjugate to $f_c$. Consequently the hyperbolic rotations move the family among the affine conjugacy classes of the polynomials with the **same** normalised parameter, and they produce no symmetry of the Julia set of $f_c$ beyond the even symmetries $z \mapsto uz$ with $u^2 = 1$.

**Proof.** Substituting gives $h^{-1}f_c(h(z)) = u^{-1}((uz)^2+c) = uz^2+c/u$. The normalisation formula of *The Mandelbrot Set and the Quadratic Family*, $c' = ad - b^2/4 + b/2$ for $az^2+bz+d$, gives $c' = u\cdot(c/u) - 0 + 0 = c$. So the scaled map is conjugate to $f_c$, and the conjugacy is the affine normalisation of the scaled map, not an isometry of the split plane. The affine automorphisms of $f_c$ are trivial and the even symmetries of the previous theorem are the only set-theoretic symmetries coming from the algebra.

**Corollary.** The hyperbolic rotations act trivially on the parameter plane: the connectedness locus $M_{\mathbb{D}}$ and the Julia set up to affine conjugacy are $SO(1,1)$-invariant as parameter data, but the plane is not acted on by $SO(1,1)$ in a way that preserves a given $J_c$. The Julia sets are read with the hyperbolic structure through the **foliation** by the level sets of the norm and the coordinates, not through a symmetry.

## The Foliation and the Dimension

**Definition.** The **coordinate foliations** of the split plane are the two families of lines $\{z_+ = \text{const}\}$ and $\{z_- = \text{const}\}$, whose directions are the null directions; the **norm foliation** is the family of hyperbolas $\{N = t\}$ and the two null lines $t = 0$.

**Theorem (the trace on a hyperbola).** For each $t \neq 0$ the level set $N = t$ is an orbit of $SO(1,1)$ and is foliated by the level curves of the two coordinates; the Julia set $J_c$ meets it in the set

$$
J_c \cap \{N = t\} = \left\{z : z_+z_- = t,\ (z_+ \in J_+ \text{ or } z_- \in J_-)\right\} ,
$$

a union of the two coordinate-line families restricted to the hyperbola. On the null lines $t = 0$ the description degenerates: the hyperbola splits into the two null lines, and the two families of coordinate lines coincide with them.

**Proof.** Immediate from the product formula $J_c = \varphi^{-1}((J_+\times\mathbb{R})\cup(\mathbb{R}\times J_-))$ of *The Split-Complex Julia Sets* and from $N = z_+z_-$; the level set $N = t$ in the coordinates is the hyperbola $z_+z_- = t$, which the two coordinate foliations cut into the two families, and its intersections with $J_c$ are exactly those on which a coordinate lies in the corresponding real Julia set.

**Theorem (the dimension).** For every $c \in \mathbb{D}$ the Hausdorff dimension of the split Julia set is

$$
\dim_H J_c = 1 + \max\{\dim_H J_+,\ \dim_H J_-\} ,
$$

whenever the two real Julia sets are nonempty, the product rule $\dim_H(A\times\mathbb{R}) = \dim_H A + 1$ for $A \subseteq \mathbb{R}$ being that of *Fractal Geometry*, and the dimension of a finite union being the maximum. If one of the real Julia sets is empty the corresponding product is absent, and if both are empty the set is empty.

**Proof.** $J_c$ is the union of the two products $\varphi^{-1}(J_+\times\mathbb{R})$ and $\varphi^{-1}(\mathbb{R}\times J_-)$, and $\varphi$ is a linear isomorphism, hence bi-Lipschitz and dimension-preserving; the dimension of a product $A\times\mathbb{R}$ is $\dim_H A + 1$ for a subset of the line, and the dimension of a finite union is the maximum of the dimensions.

**Corollary.** The split Julia set is never of dimension below one, and it is never compact: it contains the product of a nonempty subset of the line with the whole line, which is unbounded, so a nonempty $J_c$ is unbounded and only the empty set is compact. For $c = 0$ the dimension is $1+0 = 1$ and the set is the union of the four lines through the sides of the square $K_0$ — it strictly contains $\partial K_0$ and is not the boundary of the square; for $c = -2$ the dimension is $1+1 = 2$, in agreement with the two crossing strips of *The Split-Complex Julia Sets*. In particular the plane Julia set of a split-complex quadratic map is never the boundary of its filled Julia set, because the boundary is compact and the Julia set is not.

**Compare with the hyperbolic geometry of the complex case.** In the complex quadratic family the corresponding computation is that of *The Hausdorff Dimension of the Julia Sets*: the dimension of $J(f_c)$ lies in $[1,2]$, is given by the Bowen equation at the hyperbolic parameters, and is real-analytic there. The split-complex formula is elementary because the map is a product: the dimension is the dimension of one real factor plus the dimension of the line, and the "hyperbolic direction" of the algebra — the direction along the orbits of $SO(1,1)$ — supplies the addend one. In the complex case there is no such addend: the circle fibres and the radial direction are not independent, and the dimension is not a sum.

## The Hyperbolic Components and the Multiplier Metric

**Definition.** A parameter of $M_{\mathbb{D}}$ is **hyperbolic** if both real maps $g_\pm$ have an attracting cycle, that is if both $c_+$ and $c_-$ lie in the union of the real hyperbolic intervals; a **hyperbolic component** of $M_{\mathbb{D}}$ is a connected component of the hyperbolic parameters. Since the condition is a product condition, a hyperbolic component of $M_{\mathbb{D}}$ is $\varphi^{-1}(I_+ \times I_-)$ with $I_\pm$ a real hyperbolic interval.

**Theorem (the multiplier map).** Let $H = \varphi^{-1}(I_+\times I_-)$ be a hyperbolic component, where $I_\pm$ is a real hyperbolic interval of period $p_\pm$. Then the **multiplier map**

$$
\Lambda : H \longrightarrow (-1,1)^2, \qquad \Lambda(c) = \bigl(\lambda_{p_+}(c_+),\, \lambda_{p_-}(c_-)\bigr) ,
$$

sending $c$ to the pair of multipliers of the two attracting real cycles, is a diffeomorphism onto the square $(-1,1)^2$; in particular $H$ is a rectangle.

**Proof.** On a real hyperbolic interval of period $p$ the multiplier of the attracting cycle is a strictly monotone real-analytic function of the parameter, running from $1$ at one endpoint (the period-doubling point) to $-1$ at the other (the next period-doubling point); this is the one-dimensional multiplier theorem in its real form. Applying it to both factors and using that $\varphi$ is an isomorphism gives a diffeomorphism of the product onto $(-1,1)^2$.

**Definition (the hyperbolic metric on a component).** The interval $(-1,1)$ is conformally the unit disk, by $w \mapsto (1+w)/(1-w)$ or by the hyperbolic tangent; transporting the Poincaré metric of the disk gives the **hyperbolic metric** $\rho$ on $(-1,1)$. On a hyperbolic component $H = \varphi^{-1}(I_+\times I_-)$ the pull-back

$$
\rho_H = \Lambda^*(\rho\oplus\rho)
$$

of the product of the two Poincaré metrics is a complete hyperbolic metric of curvature $-1$, in which $H$ is a rectangle of finite area, and the boundary points at which a multiplier reaches $\pm1$ are the cusps.

**Remark (the comparison with the complex case).** In the complex quadratic family the analogue is the theorem that the multiplier map of a hyperbolic component of the Mandelbrot set is a biholomorphism onto the unit disk; the hyperbolic component is then a simply connected Riemann surface carrying the Poincaré metric, and this is the conformal geometry of the parameter plane. In the split-complex family the multiplier map is a diffeomorphism onto a **square** $(-1,1)^2$, and the metric is the product of two Poincaré metrics; the qualitative difference is that the split component is a product of intervals, so its Poincaré-type metric has a product structure and no rotational symmetry. The complex hyperbolic components and their Poincaré metrics are the subject of *The Mandelbrot Set and the Quadratic Family*; the definitions of the multiplier and the hyperbolic parameter are those of *The Fatou Components and the Classification of the Dynamics*, read in the real one-dimensional setting.

## The Relation to the Hyperbolic Geometry of the Corpus

**Remark.** The hyperbolic geometry of the split plane is the two-dimensional Lorentzian geometry of the form $N$ of signature $(1,1)$: one hyperbolic line, its two points at infinity and the cross-ratio distance. It is not the same as the hyperbolic geometry of the corpus in dimension three, which is the geometry of the Kleinian groups and of their limit sets, treated in *Iterated Function Systems in the Complex Plane*; there the limit set is a fractal on the sphere at infinity of hyperbolic three-space, and its dimension is the critical exponent of the group. The split-complex picture is the **two-dimensional** member of the same family: the group is $SO(1,1)$, the boundary of its hyperbolic line is the projective line, and the two points at infinity are the null quadric. The Apollonian gasket and the Schottky limit sets of that article have no two-dimensional split-complex analogue as limit sets of $SO(1,1)$, since $SO(1,1)$ is abelian and one-parameter and its action is transitive on each hyperbola; the fractal content of the split plane is not carried by the group but by the pair of real Julia sets, as the dimension formula shows. The comparison of the two hyperbolic geometries is recorded in *Hyperbolic Geometry* and in *Split-Complex Null Quadric and Projective Geometry*.

## Summary

The split plane carries the Lorentzian form $N(z) = a^2-a'^2$ of signature $(1,1)$; the group $SO(1,1)$ of hyperbolic rotations is the one-parameter group $z \mapsto e^{js}z$, its orbits are the hyperbolas $N = $ const, and its projective action fixes the two points at infinity $t = \pm1$ of the null quadric, the hyperbolic distance being the cross-ratio. The scaling $z \mapsto uz$ carries $f_c$ to $uz^2+c/u$, which is affinely conjugate to $f_c$ with the same normalised parameter, so the hyperbolic rotations produce no symmetry of a given Julia set; the affine automorphisms of $f_c$ are trivial, and the symmetries coming from the algebra are the four even symmetries $z \mapsto uz$ with $u^2 = 1$. The Julia sets are instead read through the foliation: on each hyperbola $N = t$ the Julia set is cut out by the two coordinate foliations and a coordinate lying in the corresponding real Julia set, and the two null lines are the degenerate members. The Hausdorff dimension of the split Julia set is $1 + \max\{\dim_H J_+, \dim_H J_-\}$, one plus the larger dimension of the two real factors, by the product rule; the addend one is the dimension of the hyperbolic direction. The hyperbolic components of the connectedness locus are the rectangles $\varphi^{-1}(I_+\times I_-)$, and the pair of real multipliers maps each diffeomorphically onto $(-1,1)^2$, carrying the product of the two Poincaré metrics; this is the split analogue of the biholomorphic multiplier map on a hyperbolic component of the Mandelbrot set. The group theory of the hyperbolic rotations is that of *Hyperbolic Rotations*, the null quadric that of *Split-Complex Null Quadric and Projective Geometry*, the dimension rule that of *Fractal Geometry*, and the three-dimensional hyperbolic limit sets of the corpus are those of *Iterated Function Systems in the Complex Plane*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $B(z,w) = ab-a'b'$ | Polar form of the norm, Lorentzian |
| $N(z) = a^2-a'^2$ | Quadratic form, signature $(1,1)$ |
| $O(1,1)$, $SO^+(1,1)$ | Isometry group of $N$ and its identity component |
| $e^{js} = \cosh s+j\sinh s$ | Hyperbolic rotation of rapidity $s$ |
| $\mathcal{H} = \{N=1\}$, $\mathcal{H}^\pm$ | Unit hyperbola and its two branches |
| $\mathcal{N}$, $t = \pm1$ | Null cone and the two points at infinity |
| $d(t_1,t_2)$ | Cross-ratio distance on the hyperbolic line |
| $z_\pm = a\pm a'$ | Coordinate foliations along the null directions |
| $J_\pm$, $J_c$ | Real Julia sets, and the split Julia set |
| $\dim_H J_c = 1+\max\{\dim_H J_+,\dim_H J_-\}$ | Dimension formula for the split Julia set |
| $H = \varphi^{-1}(I_+\times I_-)$ | Hyperbolic component, a rectangle |
| $\Lambda(c) = (\lambda_{p_+}(c_+),\lambda_{p_-}(c_-))$ | Multiplier map onto $(-1,1)^2$ |
| $\rho_H = \Lambda^*(\rho\oplus\rho)$ | Product Poincaré metric on a component |

## Further Reading

- I. M. Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the split-complex (hyperbolic) plane and its Lorentzian structure.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the two-dimensional real algebras and their forms.
- Kenneth Falconer, *Fractal Geometry: Mathematical Foundations and Applications*, 3rd edition (Wiley, 2014), for the product rule for the Hausdorff dimension.
- John Milnor, *Dynamics in One Complex Variable*, 3rd edition (Princeton University Press, 2006), for the multiplier map and the hyperbolic components of the Mandelbrot set.
- Michael F. Barnsley, *Fractals Everywhere*, 2nd edition (Academic Press, 1993), for the product self-similarity and the dimension of a product.
