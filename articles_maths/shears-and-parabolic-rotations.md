
# __Shears and Parabolic Rotations__

## Introduction

This article develops the one-parameter group theory of the infinitesimal extension of the real line, that is, the group theory of the dual numbers. It follows *Dual-Numbers Algebra*, which fixed the ring $\mathbb{D}' = \mathbb{D}'_{\mathbb{R}} = \mathbb{R}[\varepsilon]/(\varepsilon^2)$, the maximal ideal $\mathfrak{m} = (\varepsilon)$ and the group of units $(\mathbb{D}')^\times$, and it follows *Dual-Numbers Representations* for the regular representation and the nilpotent endomorphism $E = \rho_{\mathrm{reg}}(\varepsilon)$. The subject is the geometry of multiplication by a unit, treated, as in *The Three Two-Dimensional Algebras and the Three Kinds of Rotation*, as a one-parameter transformation group and as a Lie group, not as a motion in any physical sense.

The three two-dimensional commutative unital real algebras give three kinds of rotation. For the complex numbers $\mathbb{C}$ the norm-one group is the circle $U(1)$, compact, and its one-parameter group is the elliptic rotation. For the split complex numbers $\mathbb{D} = \mathbb{R}[j]$, $j^2 = +1$, the norm-one group is the hyperbola and its identity component is the hyperbolic rotation group, with the rapidity as additive parameter. For the dual numbers $\mathbb{D}'$ the norm form is degenerate and the norm-one group degenerates to a pair of parallel lines; its identity component is the **shear group**, a one-parameter group whose elements are unipotent linear maps of the dual plane. The purpose of this article is to describe that group, its generator, its Lie algebra, its action, and its relation to the elliptic and hyperbolic cases as the common degenerate limit.

The central objects are these. Multiplication by the unit $u = 1 + s\varepsilon$ is the linear map

$$
S(s) : x + y\varepsilon \longmapsto x + (sx + y)\varepsilon,
$$

the elementary shear matrix $\begin{pmatrix}1&0\\s&1\end{pmatrix}$. The family $\{S(s) : s \in \mathbb{R}\}$ is a one-parameter group, isomorphic to the additive group of the real line, whose infinitesimal generator is the nilpotent endomorphism $E = \rho_{\mathrm{reg}}(\varepsilon)$ with $E^2 = 0$. Because the generator is nilpotent rather than semisimple, the exponential map is polynomial, the group is unipotent, and no orbit other than a fixed point is periodic. The parameter $s$ is the **parabolic angle**; it is additive, and its addition law is the parabolic case of the trichotomy of angle-addition laws.

No physics is invoked anywhere. The word "rotation" is used throughout in the algebraic sense of a one-parameter subgroup of the group of units acting linearly on the algebra, exactly as in *The Three Two-Dimensional Algebras and the Three Kinds of Rotation*.

Notation: $z = x + y\varepsilon$ with $x, y \in \mathbb{R}$; $\operatorname{Re} z = x$, $\operatorname{Inf} z = y$; $\bar z = x - y\varepsilon$; $N(z) = z\bar z = x^2$; $x^2 + y^2$ the Euclidean form; $\mathfrak{m} = \varepsilon\mathbb{R}$ the maximal ideal; $\pi(x + y\varepsilon) = x$ the augmentation.

## The Group of Units

### Units and the Maximal Ideal

**Proposition.** The element $a + b\varepsilon \in \mathbb{D}'$ is a unit if and only if $a \neq 0$, and then

$$
(a + b\varepsilon)^{-1} = \frac{1}{a} - \frac{b}{a^2}\,\varepsilon.
$$

**Proof.** The product $(a+b\varepsilon)(c+d\varepsilon) = ac + (ad+bc)\varepsilon$ equals $1$ exactly when $ac = 1$ and $ad + bc = 0$; the first equation is solvable in $\mathbb{R}$ exactly when $a \neq 0$, and then $c = a^{-1}$ and $d = -a^{-2}b$. $\square$

So the non-units are the elements of the maximal ideal $\mathfrak{m}$, and $(\mathbb{D}')^\times = \mathbb{D}' \setminus \mathfrak{m}$. The subgroup

$$
1 + \mathfrak{m} = \{1 + s\varepsilon : s \in \mathbb{R}\}
$$

consists of the units of real part one; it is the fibre of the augmentation over $1$ inside the unit group, and it will turn out to be exactly the shear group.

### The Unit Group as a Direct Product

**Theorem.** Let $R$ be a commutative ring. The map

$$
\Phi : R^\times \times (R, +) \longrightarrow (\mathbb{D}'_R)^\times, \qquad \Phi(a, s) = a + as\varepsilon = a(1 + s\varepsilon),
$$

is an isomorphism of groups.

**Proof.** $\Phi$ is bijective: given $a + b\varepsilon$ with $a \in R^\times$, the unique preimage is $(a, a^{-1}b)$. It is a homomorphism, because

$$
\Phi(a,s)\Phi(c,t) = a(1+s\varepsilon)\,c(1+t\varepsilon) = ac\bigl(1 + (s+t)\varepsilon\bigr) = \Phi\bigl(ac,\, s+t\bigr),
$$

using $\varepsilon^2 = 0$. $\square$

**Corollary.** For $R = \mathbb{R}$, the group of units is

$$
(\mathbb{D}')^\times \cong \mathbb{R}^\times \times \mathbb{R},
$$

with the two factors the nonzero scalars and the shear group. The unit group is abelian, has exactly two connected components, distinguished by the sign of the real part, and each is contractible.

**Proof.** The isomorphism is the theorem. The sign of the real part is a continuous homomorphism $(\mathbb{D}')^\times \to \{\pm1\}$ and $\mathbb{R}^\times$ has two components, so the two groups have the same component count; the component of the identity is $\{a > 0\} \cong \mathbb{R}_{>0} \times \mathbb{R}$, which is contractible. $\square$

The algebra article records that the unit group is an extension of $R^\times$ by the additive group $R$; for commutative $R$ the extension splits and, the group being abelian, the extension is in fact a direct product, which is the content of the theorem above.

### The Norm-One Group

The norm form $N(z) = z\bar z = x^2$ is multiplicative, $N(uv) = N(u)N(v)$, and its radical is $\mathfrak{m}$: it vanishes on $\mathfrak{m}$ and is nonzero off it. The **norm-one group** is

$$
H = \{z \in \mathbb{D}' : N(z) = 1\}.
$$

**Proposition.** $H = \{x + y\varepsilon : x = \pm 1\}$ is the union of the two parallel lines of real part $\pm1$; its identity component is $H_0 = 1 + \mathfrak{m}$, the shear group.

**Proof.** $N(x + y\varepsilon) = x^2 = 1$ gives $x = \pm1$ and leaves $y$ free; the two lines meet the real axis at $1$ and $-1$, and the component through $1$ is the line $x = 1$, which is $1 + \mathfrak{m}$. $\square$

The three norm-one sets of the three two-dimensional algebras are therefore a circle, a hyperbola and a pair of parallel lines. The degeneration is the visible form of $\varepsilon^2 = 0$: the quadratic form has lost its non-degenerate directions, and its level set is no longer a curve of curvature but a flat pair of lines.

## Multiplication by a Unit as a Shear

### The Regular Representation

By *Dual-Numbers Representations*, the regular representation of $\mathbb{D}'$ is left multiplication on itself,

$$
\rho_{\mathrm{reg}}(u) : \mathbb{D}' \to \mathbb{D}', \qquad \rho_{\mathrm{reg}}(u)(z) = uz,
$$

and it is the case $V = \mathbb{D}'$, $E = \rho_{\mathrm{reg}}(\varepsilon)$ of the general correspondence of that article, in which a representation of $\mathbb{D}'$ on an $R$-module $V$ is a square-zero endomorphism $E \in \operatorname{End}_R(V)$ acting by $a + b\varepsilon \mapsto a\,\mathrm{id}_V + bE$. In particular the $\mathbb{D}'$-linear endomorphisms of the module $\mathbb{D}'$ are exactly the maps $\rho_{\mathrm{reg}}(u)$, and they form an algebra isomorphic to $\mathbb{D}'$. In the basis $(1, \varepsilon)$ the regular representation of the unit $u = a + b\varepsilon$ has the matrix

$$
[u] = \begin{pmatrix} a & 0 \\ b & a \end{pmatrix}.
$$

**Proof.** $\rho_{\mathrm{reg}}(a + b\varepsilon)(1) = a + b\varepsilon$ and $\rho_{\mathrm{reg}}(a+b\varepsilon)(\varepsilon) = a\varepsilon$, which are the columns of $[u]$. $\square$

The matrix is a general element of the commutative subalgebra of $\mathbb{R}^{2\times2}$ generated by the identity and the nilpotent Jordan block $\begin{pmatrix}0&0\\1&0\end{pmatrix}$, which is the endomorphism ring of the regular representation computed in *Dual-Numbers Representations*.

### Shear Matrices

Write a unit as $u = a(1 + s\varepsilon)$ with $a \in \mathbb{R}^\times$ and $s = b/a$. Then

$$
[u] = a\Bigl(I + sE\Bigr), \qquad E = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix},
$$

and $E$ is the matrix of $\rho_{\mathrm{reg}}(\varepsilon)$, the endomorphism sending $x + y\varepsilon$ to $x\varepsilon$.

**Definition.** The **shear** of parameter $s$ is the $\mathbb{D}'$-linear map

$$
S(s) = I + sE = \begin{pmatrix} 1 & 0 \\ s & 1 \end{pmatrix}, \qquad S(s)(x + y\varepsilon) = x + (y + sx)\varepsilon.
$$

It is an elementary shear matrix, or transvection: it fixes the line $\mathfrak{m}$ pointwise, acts as the identity on the quotient $\mathbb{D}'/\mathfrak{m} \cong \mathbb{R}$, and displaces every point by a vector parallel to $\mathfrak{m}$.

Thus multiplication by the unit $u = a(1+s\varepsilon)$ is the composition of the scalar dilation $a$ with the shear $S(s)$: the group of units acts on the dual plane by dilations and shears, and the shear parameter is the coordinate of the quotient $(\mathbb{D}')^\times/\mathbb{R}^\times$.

**Remark (the degenerate perpendicular).** In terms of the Euclidean inner product, the displacement produced by $S(s)$ is

$$
S(s)(v) - v = s\,\langle v, 1\rangle\,\varepsilon, \qquad v = x + y\varepsilon,
$$

since $\langle v, 1\rangle = x$. The displacement is proportional to the component of $v$ along the real axis and points along the nilpotent axis, which is the Euclidean orthogonal complement of the real axis; so $S(s)$ is the elementary shear, or transvection, that displaces each point of the plane along the nilpotent direction by an amount proportional to its real part. In the notation of the other articles on the two-dimensional algebras this is the description of multiplication by a unit as the map $v \mapsto v + s\,v_\perp$, with $v_\perp = \langle v, 1\rangle\,\varepsilon = \operatorname{Re}(v)\,\varepsilon$: the "perpendicular" component is read off by the augmentation and displaced into the maximal ideal. The norm form registers none of this displacement. Its bilinear form is $B(z,w) = \operatorname{Re}(z)\operatorname{Re}(w)$, for which the nilpotent axis is the radical, $B$-orthogonal to the whole plane; the shear leaves $N$ invariant for that reason, and not because the displacement is small.

### Orbits and the Fixed Fibre

**Theorem.** The shear group acts on $\mathbb{D}'$ with the following orbits.

1. The maximal ideal $\mathfrak{m} = \pi^{-1}(0)$ is fixed pointwise.
2. Every fibre $\pi^{-1}(x)$ with $x \neq 0$ is a single orbit, and the action on it is free: the map $s \mapsto S(s)(x + y\varepsilon)$ is a bijection of $\mathbb{R}$ onto the fibre.

**Proof.** $S(s)(x + y\varepsilon) = x + (y + sx)\varepsilon$, so the real part $x$ is invariant and the infinitesimal part is translated by $sx$. If $x = 0$ the point is fixed for every $s$. If $x \neq 0$, the map $y \mapsto y + sx$ is a bijection of $\mathbb{R}$, so the orbit is the whole fibre and the stabiliser is trivial. $\square$

The orbits of the shear group are therefore the fibres of the augmentation, and the fixed set is the fibre over the orig. This is the group-theoretic statement of the fact that the shear moves along the nilpotent direction: the invariant lines of the action are exactly the lines along which the integration theory, integrates.

## The One-Parameter Group of Shears

### The Shear Group and Its Generator

**Theorem.** The set $G = \{S(s) : s \in \mathbb{R}\}$ is a one-parameter subgroup of $GL_2(\mathbb{R})$, and the map $s \mapsto S(s)$ is an isomorphism of groups

$$
(\mathbb{R}, +) \longrightarrow G, \qquad S(s)S(t) = S(s+t), \qquad S(0) = I, \qquad S(s)^{-1} = S(-s).
$$

**Proof.** $S(s) = I + sE$ and $E^2 = 0$, so $(I+sE)(I+tE) = I + (s+t)E + stE^2 = I + (s+t)E$. $\square$

The subgroup $G$ is exactly the image of $1 + \mathfrak{m}$ under the regular representation, and it is a subgroup of the group of $\mathbb{D}'$-linear automorphisms of the module $\mathbb{D}'$. It is **not** a subgroup of the algebra automorphism group: left multiplication by a unit is an algebra homomorphism only when the unit is the identity, since $(uz)(uw) = u^2 zw$ equals $u(zw)$ only when $u^2 = u$, which for a unit forces $u = 1$. The shears are module symmetries, not algebra symmetries.

### The Exponential Map

The generator of the one-parameter group is

$$
E = \frac{d}{ds}\Big|_{s=0} S(s) = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} = \rho_{\mathrm{reg}}(\varepsilon).
$$

**Theorem (exponential).** The exponential map of the shear group is the polynomial map

$$
\exp : \mathbb{R}\varepsilon = \mathfrak{m} \longrightarrow G, \qquad \exp(s\varepsilon) = 1 + s\varepsilon,
$$

which is a group isomorphism and a homeomorphism onto $G$; its inverse is the dual logarithm $\log(1 + s\varepsilon) = s\varepsilon$.

**Proof.** The exponential series $\sum_k (sE)^k/k!$ terminates at $k = 1$ because $E^2 = 0$, so $\exp(sE) = I + sE$. Under the identification of the module with the algebra this is $\exp(s\varepsilon) = 1 + s\varepsilon$. The logarithm is its inverse, and the identities $\exp(s\varepsilon)\exp(t\varepsilon) = \exp((s+t)\varepsilon)$ and $\log(uv) = \log u + \log v$ are the group law. $\square$

So the exponential of the shear generator is algebraic, its image is the whole shear group, and it is injective. This is the sharpest formal contrast with the elliptic case: there the exponential of the rotation generator is periodic, its kernel is $2\pi\mathbb{Z}$, and the group is compact; here the exponential is a homeomorphism from the line onto the group, and the group is a non-compact line.

### The Projective Action and the Translation Coordinate

On the open chart $\{x \neq 0\}$ of the dual plane, use the affine coordinate

$$
t = \frac{y}{x}, \qquad x \neq 0,
$$

which is the coordinate of the line through the origin of slope $t$, i.e. the coordinate of the projective line at points where the first homogeneous coordinate is nonzero. Then

$$
S(s)(x + y\varepsilon) = x + (y+sx)\varepsilon \quad\Longrightarrow\quad t \longmapsto \frac{y + sx}{x} = t + s.
$$

So on the projective line the shear acts by a **translation** of the affine coordinate. A transformation of the projective line with a single fixed point of multiplicity two is called parabolic; the fixed point here is the class of $\varepsilon$, i.e. the fibre over the origin, and the shear group is exactly the one-parameter unipotent subgroup of the parabolic subgroup of $PGL_2(\mathbb{R})$ that fixes that point — the subgroup conjugate to the translations. This is the Lie-theoretic content of the word "parabolic" in the title.

## The Parabolic Angle

### Additivity of the Parameter

The group law $S(s)S(t) = S(s+t)$ says that the parameter $s$ is additive: the composition of two shears is the shear whose parameter is the sum. The parameter is called the **parabolic angle**, and the dual logarithm identifies it with the additive line,

$$
\log : 1 + \mathfrak{m} \longrightarrow (\mathfrak{m}, +), \qquad \log(1 + s\varepsilon) = s\varepsilon.
$$

Two facts about the parabolic angle distinguish it from the elliptic angle, and both are shared with the hyperbolic rapidity. First, it is defined on the whole line and is unbounded, with no period: the shear group is isomorphic to $\mathbb{R}$. Second, the dual logarithm is a homeomorphism onto the whole shear group, because the exponential is injective; the angle is a globally defined coordinate, not a coordinate modulo a period and not restricted to a branch. What separates the parabolic case from the hyperbolic one is therefore not the angle but the group: the generator of the shears is nilpotent and the shear group is unipotent, whereas the generator $j$ of the hyperbolic rotations is semisimple, $j^2 = +1$, and the group of hyperbolic rotations has two components.

### The Group of Units Modulo Scaling

**Theorem.** The quotient of the unit group by the subgroup of nonzero scalars is the shear group, and it is identified with the additive line by the logarithm:

$$
(\mathbb{D}')^\times / \mathbb{R}^\times \cong 1 + \mathfrak{m} \cong (\mathbb{R}, +), \qquad u = a(1+s\varepsilon) \longmapsto 1 + s\varepsilon \longmapsto s.
$$

**Proof.** The subgroup of scalars is $\mathbb{R}^\times = \{a + 0\varepsilon : a \neq 0\}$, and $a(1+s\varepsilon) \equiv 1 + s\varepsilon \pmod{\mathbb{R}^\times}$. The map $u \mapsto a^{-1}u$ is a homomorphism onto $1+\mathfrak{m}$ with kernel $\mathbb{R}^\times$, and $1+\mathfrak{m} \cong (\mathbb{R},+)$ by the group law of the shear group. $\square$

So every unit is a scalar multiple of a unique shear, and the two factors of the direct product $(\mathbb{D}')^\times \cong \mathbb{R}^\times \times \mathbb{R}$ are the scaling part and the parabolic angle. The quotient by scaling is the additive line of angles.

### The Three Angles

The three two-dimensional algebras have three angle parameters; in each case the angle is the coordinate on the connected component of the unit group modulo scaling, and in each case the composition is addition of the coordinate.

| Algebra | Norm-one group | Angle | Addition law | Group topology |
|---|---|---|---|---|
| $\mathbb{C}$, $i^2 = -1$ | circle $U(1)$ | elliptic angle $\theta$ | addition mod $2\pi$ | compact |
| $\mathbb{D}$, $j^2 = +1$ | hyperbola $x^2-y^2=1$ | hyperbolic angle (rapidity) $t$ | additive on $\mathbb{R}$ | non-compact |
| $\mathbb{D}'$, $\varepsilon^2 = 0$ | lines $x = \pm1$ | parabolic angle $s$ | additive on $\mathbb{R}$ | non-compact, unipotent |

In the elliptic and hyperbolic cases the tangent of the angle obeys

$$
\tan(\alpha+\beta) = \frac{\tan\alpha + \tan\beta}{1 - \tan\alpha\tan\beta}, \qquad \tanh(t+u) = \frac{\tanh t + \tanh u}{1 + \tanh t\tanh u},
$$

and it is the product term in the denominator that the degeneracy removes: the parabolic coordinate is the parabolic angle $s$ itself, whose law is bare addition. The composition of two parabolic rotations is the parabolic rotation whose angle is the sum,

$$
s_1 \oplus s_2 = s_1 + s_2,
$$

the parabolic case of the angle-addition laws of the elliptic and hyperbolic cases; this additive composition law for the coordinate is sometimes called Galilean velocity addition. The name records the degenerate character of the law — a translation of the coordinate rather than a Möbius combination of it — and the group-theoretic content is the statement that the shear group is isomorphic to the additive line.

## The Lie Algebra of the Shear Group

### The Generator as the Regular Representation of $\varepsilon$

The Lie algebra of the shear group is the one-dimensional real Lie algebra

$$
\mathfrak{g} = \mathbb{R}E \subset \mathfrak{gl}_2(\mathbb{R}), \qquad E = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} = \rho_{\mathrm{reg}}(\varepsilon).
$$

It is abelian, $[E,E] = 0$, and the generator is nilpotent of index two: $E \neq 0$ and $E^2 = 0$. So $\mathfrak{g}$ is a nilpotent Lie algebra of index two and $G = \exp(\mathfrak{g})$ is a **unipotent** group: every element is unipotent, of the form identity plus a nilpotent endomorphism, and the only eigenvalue of every element is $1$.

Under the identification of the regular representation with the algebra, the Lie algebra of the shear group is the line $\mathbb{R}\varepsilon = \mathfrak{m}$ inside $\mathbb{D}'$, with the trivial bracket; the generator is $\varepsilon$ itself. This is the same square-zero endomorphism that generates the fibre direction, and its nilpotence is the same $\varepsilon^2 = 0$.

### Derivations and Automorphisms

The shear generator must be distinguished from the derivations of the algebra, which generate a different one-parameter group.

**Proposition.** The derivations of $\mathbb{D}'$ are the multiples of the single derivation

$$
\partial_\varepsilon(1) = 0, \qquad \partial_\varepsilon(\varepsilon) = \varepsilon, \qquad \partial_\varepsilon(a + b\varepsilon) = b\varepsilon,
$$

so $\operatorname{Der}(\mathbb{D}')$ is one-dimensional over $\mathbb{R}$, spanned by $\partial_\varepsilon$. This derivation is idempotent, $\partial_\varepsilon^2 = \partial_\varepsilon$, and it is not nilpotent.

**Proof.** Let $\delta$ be a derivation. Then $\delta(1) = \delta(1\cdot 1) = 2\delta(1)$, so $\delta(1) = 0$, and $\delta$ is determined by $\delta(\varepsilon) = a + b\varepsilon$. From $\varepsilon^2 = 0$ and the Leibniz rule, $0 = \delta(\varepsilon^2) = 2\varepsilon\,\delta(\varepsilon) = 2a\varepsilon$, so $a = 0$ and $\delta(\varepsilon) \in \mathbb{R}\varepsilon$. Hence $\delta = c\,\partial_\varepsilon$ with $c$ the coefficient of $\varepsilon$ in $\delta(\varepsilon)$, and $\operatorname{Der}(\mathbb{D}') = \mathbb{R}\partial_\varepsilon$ is one-dimensional. This is the derivation statement of *Dual-Numbers Algebra*, and it settles the general form; finally $\partial_\varepsilon(b\varepsilon) = b\varepsilon$, so $\partial_\varepsilon^2 = \partial_\varepsilon$. $\square$

**Proposition.** Every unital algebra endomorphism of $\mathbb{D}'$ is $\varphi_c(\varepsilon) = c\varepsilon$ for some $c \in \mathbb{R}^\times$, and $\varphi_c$ is an automorphism. Hence $\operatorname{Aut}(\mathbb{D}') \cong \mathbb{R}^\times$, with identity component $\{c > 0\} \cong \mathbb{R}_{>0}$ and Lie algebra $\operatorname{Der}(\mathbb{D}') = \mathbb{R}\partial_\varepsilon$. The exponential of the derivation is $\exp(t\partial_\varepsilon)(\varepsilon) = e^t\varepsilon$.

**Proof.** A unital endomorphism is determined by $\varphi(\varepsilon) = a + b\varepsilon$ and must satisfy $\varphi(\varepsilon)^2 = a^2 + 2ab\varepsilon = 0$, so $a = 0$; then $\varphi(x + y\varepsilon) = x + yb\varepsilon$, which is bijective exactly when $b \neq 0$. Writing $b = c$ gives the stated form. For the last statement, $\partial_\varepsilon^k(\varepsilon) = \varepsilon$ for every $k \geq 1$, so the exponential series of the derivation gives $\exp(t\partial_\varepsilon)(\varepsilon) = \sum_{k \geq 0} t^k \varepsilon/k! = e^t\varepsilon$; the exponential of a derivation of a finite-dimensional real algebra is an automorphism. $\square$

The sharp contrast is now visible. The derivations fix the real axis pointwise and scale the maximal ideal by $\varepsilon \mapsto e^t\varepsilon$, generating the automorphism group $\mathbb{R}^\times$; the shears act on $\mathfrak{m}$ by the identity, fix it pointwise, and are module maps that are not algebra maps. Their generators are the idempotent $\partial_\varepsilon$ and the nilpotent $E$ respectively. The shear group is therefore **not** the exponential of the derivation algebra; it is the exponential of the square-zero direction of the algebra itself.

### The Lie Algebra of the Unit Group

The unit group $(\mathbb{D}')^\times$ is a two-dimensional abelian Lie group, and its Lie algebra at the identity is $\mathbb{D}'$ itself, with the zero bracket, by *Dual-Numbers Algebra*: the commutator on $\mathbb{D}'$ vanishes identically. In the direct-product decomposition $(\mathbb{D}')^\times \cong \mathbb{R}^\times \times \mathbb{R}$ the Lie algebra decomposes as $\mathbb{R} \oplus \mathbb{R}$, with the first factor the infinitesimal dilations and the second factor the infinitesimal shears. The shear group is the one-parameter subgroup generated by the element $\varepsilon \in \mathfrak{m}$, and its Lie algebra is the line $\mathfrak{g} = \mathbb{R}\varepsilon \subset \mathbb{D}'$.

## The Degeneration at $\varepsilon^2 = 0$

### The Degenerate Norm Form and Its Orthogonal Group

The shear is an "orthogonal" transformation of the degenerate norm form, in the following sense.

**Proposition.** A linear map $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ satisfies $N(Az) = N(z)$ for all $z$ if and only if $a = \pm 1$ and $b = 0$; the coefficients $c$ and $d$ are then free. Such an $A$ is invertible, and hence an isometry of the form, exactly when $d \neq 0$.

**Proof.** $N(A(x+y\varepsilon)) = (ax + by)^2$ must equal $x^2$ for all $x, y$; comparing coefficients of $x^2$, $xy$ and $y^2$ gives $a^2 = 1$, $ab = 0$, $b^2 = 0$, hence $a = \pm1$ and $b = 0$. The determinant is then $\det A = ad = \pm d$, so $A$ is invertible exactly when $d \neq 0$. $\square$

The group of isometries of the form is therefore $A = \begin{pmatrix} \pm 1 & 0 \\ c & d \end{pmatrix}$ with $d \neq 0$, and its identity component is $\left\{\begin{pmatrix} 1 & 0 \\ c & d \end{pmatrix} : c \in \mathbb{R},\ d > 0\right\}$, of dimension two; the shear group $S(s) = \begin{pmatrix}1&0\\ s&1\end{pmatrix}$ is its unipotent subgroup with $d = 1$.

So the stabiliser of the form is larger than in the non-degenerate cases, because the radical $\mathfrak{m}$ may be rescaled and sheared without changing $N$: its identity component is two-dimensional, whereas the identity components of the isometry groups in the non-degenerate cases are one-dimensional. The Euclidean orthogonal group $O(2)$ is compact; the group $O(1,1)$ of the split complex form is non-compact with a one-dimensional identity component; the stabiliser here is non-compact and two-dimensional, and the shear group is the distinguished unipotent one-parameter subgroup that preserves the flag $0 \subset \mathfrak{m} \subset \mathbb{D}'$ and acts trivially on both the submodule $\mathfrak{m}$ and the quotient.

### The Norm-One Set

The norm-one set $N(z) = 1$ is the pair of parallel lines $x = \pm1$. The identity component of the group of units, $\{a > 0\}$, meets this set in the single line $x = 1$, which is the shear group $1 + \mathfrak{m}$. So the shear group is exactly the connected "rotation group" of the degenerate form, and the passage from the circle to the hyperbola to the pair of parallel lines is the passage from $U(1)$ to $SO(1,1)_0$ to $G$.

### The Contraction from the Elliptic and Hyperbolic Cases

The degeneracy can be seen as a limit. Consider the family of quadratic forms $N_\sigma(x + y\varepsilon) = x^2 + \sigma y^2$ on the plane, and the generator

$$
J_\sigma = \begin{pmatrix} 0 & -\sigma \\ 1 & 0 \end{pmatrix}, \qquad J_\sigma^2 = -\sigma I.
$$

For $\sigma > 0$ the form is positive definite and $\exp(tJ_\sigma)$ is the elliptic rotation of angle $t\sqrt\sigma$ in the coordinates adapted to the form; for $\sigma < 0$ the form is indefinite and $\exp(tJ_\sigma)$ is the hyperbolic rotation of rapidity $t\sqrt{-\sigma}$ in those coordinates; for $\sigma = 0$ one has $J_0 = E$ and $\exp(tJ_0) = I + tE = S(t)$.

**Theorem (contraction).** For every fixed $t$, $\exp(tJ_\sigma) \to S(t)$ as $\sigma \to 0$.

**Proof.** For $\sigma > 0$,

$$
\exp(tJ_\sigma) = \cos(t\sqrt\sigma)\,I + \frac{\sin(t\sqrt\sigma)}{\sqrt\sigma}\,J_\sigma = \begin{pmatrix} \cos(t\sqrt\sigma) & -\sqrt\sigma\,\sin(t\sqrt\sigma) \\ \dfrac{\sin(t\sqrt\sigma)}{\sqrt\sigma} & \cos(t\sqrt\sigma) \end{pmatrix},
$$

and as $\sigma \to 0$ the entries tend to $1, 0, t, 1$; the case $\sigma < 0$ is the same computation with $\cosh$ and $\sinh$. $\square$

So the shear group is the common contraction of the elliptic and hyperbolic rotation groups, and the mechanism of the contraction is exactly the vanishing of the square of the generator: $J_\sigma^2 = -\sigma I \to 0$, so in the limit the generator becomes nilpotent and the exponential becomes a polynomial. This is a group contraction in the sense of Inönü and Wigner: the one-parameter groups degenerate, and the limit group is the additive line acting by unipotent shears.

### No Compact Rotation Group and No Periodic Orbits

Two consequences make the parabolic case the degenerate end of the trichotomy.

- **No compact rotation group.** The shear group $G \cong \mathbb{R}$ is non-compact and has no nontrivial compact subgroup; the only compact subgroup of the full unit group $(\mathbb{D}')^\times \cong \mathbb{R}^\times \times \mathbb{R}$ is the central $\{\pm 1\}$. There is no analogue of the circle group $U(1)$.
- **No periodic orbits.** The orbit of a point in a fibre $\pi^{-1}(x)$ with $x \neq 0$ is the whole fibre, a non-compact line on which the shear acts by translation, so no orbit other than a fixed point is periodic; in the elliptic case every orbit is a circle and the action is periodic. The shear also does not preserve the Euclidean metric: writing $v = x + y\varepsilon$ one has $S(s)v = x + (y+sx)\varepsilon$, and $x^2+y^2$ is preserved for every $v$ only when $s = 0$. So $S(s)$ is an isometry of the degenerate form $N$ but not of the Euclidean metric of the plane. A compact subgroup of $GL_2(\mathbb{R})$ preserves some positive-definite form, obtained by averaging any form over the group; $G$ is non-compact, so it preserves none, and the computation above is the instance of that failure for the Euclidean form itself.

## Summary

The **group of units** of $\mathbb{D}' = \mathbb{R}[\varepsilon]/(\varepsilon^2)$ is $(\mathbb{D}')^\times = \mathbb{D}' \setminus \mathfrak{m}$, with $(a+b\varepsilon)^{-1} = a^{-1} - a^{-2}b\,\varepsilon$. For commutative $R$ it is the direct product $(\mathbb{D}'_R)^\times \cong R^\times \times (R,+)$ via $a + as\varepsilon \leftrightarrow (a,s)$; over $\mathbb{R}$ this is $\mathbb{R}^\times \times \mathbb{R}$, abelian with two contractible components. The norm form $N(z) = x^2$ is degenerate with radical $\mathfrak{m}$, and its norm-one set is the pair of parallel lines $x = \pm1$, whose identity component is the shear group $1 + \mathfrak{m}$.

Multiplication by a unit is a **dilation composed with a shear**: in the basis $(1, \varepsilon)$ the regular representation is $[a + b\varepsilon] = a(I + (b/a)E)$ with $E = \rho_{\mathrm{reg}}(\varepsilon) = \begin{pmatrix}0&0\\1&0\end{pmatrix}$ and $E^2 = 0$. The **shear** $S(s) = I + sE$ acts by $x + y\varepsilon \mapsto x + (y+sx)\varepsilon$; it fixes $\mathfrak{m}$ pointwise, acts as the identity on the quotient, and its orbits are the fibres of the augmentation, with the fibre over the origin fixed.

The shears form a **one-parameter group** $G = \{S(s)\} \cong (\mathbb{R},+)$ with $S(s)S(t) = S(s+t)$ and generator $E$. The **exponential** is the polynomial map $\exp(s\varepsilon) = 1 + s\varepsilon$, a group isomorphism and homeomorphism onto $G$, inverse to the dual logarithm; on the projective chart $\{x \neq 0\}$ with coordinate $t = y/x$ the shear is the translation $t \mapsto t+s$, so $G$ is the unipotent one-parameter subgroup of the parabolic subgroup of $PGL_2(\mathbb{R})$ that fixes the class of $\varepsilon$, a transformation with a double fixed point. The parameter is the **parabolic angle**; it is additive, globally defined and without period, and $(\mathbb{D}')^\times/\mathbb{R}^\times \cong 1+\mathfrak{m} \cong (\mathbb{R},+)$.

The **Lie algebra** of the shear group is the line $\mathfrak{g} = \mathbb{R}E = \mathbb{R}\varepsilon$ inside $\mathbb{D}'$, abelian, with nilpotent generator $E^2 = 0$; the group is unipotent and every element has the single eigenvalue $1$. The **derivations** $\operatorname{Der}(\mathbb{D}') = \mathbb{R}\partial_\varepsilon$ are spanned by the idempotent $\partial_\varepsilon(\varepsilon) = \varepsilon$, which generates the automorphism group $\operatorname{Aut}(\mathbb{D}') \cong \mathbb{R}^\times$ by $\varepsilon \mapsto e^t\varepsilon$; the shear group is not the exponential of the derivations but of the square-zero direction of the algebra. Finally, the **degeneration** at $\varepsilon^2 = 0$ is visible in the contraction $J_\sigma^2 = -\sigma I \to 0$, whose limit sends the elliptic and hyperbolic rotation groups to the shear group, in the collapse of the norm-one set from a circle and a hyperbola to a pair of parallel lines, and in the absence of any compact rotation group or periodic orbit.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}' = \mathbb{R}[\varepsilon]/(\varepsilon^2)$ | Dual number algebra, $\varepsilon^2 = 0$ |
| $\mathbb{D}$ | Split complex algebra, unit $j$, $j^2 = +1$ |
| $z = x + y\varepsilon$ | General dual number, $x = \operatorname{Re} z$, $y = \operatorname{Inf} z$ |
| $N(z) = z\bar z = x^2$ | Degenerate norm form, radical $\mathfrak{m}$ |
| $H = \{z : N(z) = 1\}$ | Norm-one group, lines $x = \pm1$; $H_0 = 1+\mathfrak{m}$ |
| $\mathfrak{m} = \varepsilon\mathbb{R}$ | Maximal ideal, $\mathfrak{m}^2 = 0$ |
| $\pi(x+y\varepsilon) = x$ | Augmentation, kernel $\mathfrak{m}$ |
| $(\mathbb{D}')^\times = \mathbb{D}' \setminus \mathfrak{m}$ | Group of units |
| $1 + \mathfrak{m}$ | Shear group, units of real part $1$ |
| $\rho_{\mathrm{reg}}(u)(z) = uz$ | Regular representation |
| $[u] = \begin{pmatrix} a & 0 \\ b & a \end{pmatrix}$ | Matrix of $\rho_{\mathrm{reg}}(a + b\varepsilon)$ |
| $E = \rho_{\mathrm{reg}}(\varepsilon) = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$ | Nilpotent generator, $E^2 = 0$ |
| $S(s) = I + sE = \begin{pmatrix} 1 & 0 \\ s & 1 \end{pmatrix}$ | Shear of parameter $s$ |
| $G = \{S(s)\} \cong (\mathbb{R},+)$ | One-parameter shear group |
| $\exp(s\varepsilon) = 1 + s\varepsilon$ | Exponential of the shear generator |
| $t = y/x$ | Translation coordinate on $\{x \neq 0\}$ |
| $s$ | Parabolic angle |
| $\partial_\varepsilon(a + b\varepsilon) = b\varepsilon$, matrix $\begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$ | Generator of $\operatorname{Der}(\mathbb{D}')$, idempotent $\partial_\varepsilon^2 = \partial_\varepsilon$ |
| $\operatorname{Aut}(\mathbb{D}') \cong \mathbb{R}^\times$ | Unital automorphisms, $\varepsilon \mapsto c\varepsilon$ |
| $J_\sigma = \begin{pmatrix} 0 & -\sigma \\ 1 & 0 \end{pmatrix}$, $J_\sigma^2 = -\sigma I$ | Contraction family, $J_0 = E$ |



## Further Reading

- Eduard Study, *Geometrie der Dynamen* (Teubner, 1903), for the dual numbers as an infinitesimal extension and for their linear geometry.
- Wilhelm Blaschke, *Vorlesungen über Differentialgeometrie I* (Springer, 1930), for the classical use of dual numbers in the geometry of ruled surfaces.
- Sophus Lie and Friedrich Engel, *Theorie der Transformationsgruppen* (Teubner, 1888–1893), for one-parameter transformation groups and their infinitesimal generators.
- Erdal Inönü and Eugene P. Wigner, "On the contraction of groups and their representations", *Proceedings of the National Academy of Sciences of the USA* 39 (1953), for the contraction of a one-parameter group to a unipotent limit.
- Vladimir V. Kisil, *Geometry of Möbius Transformations: Elliptic, Parabolic and Hyperbolic Actions of $SL(2,\mathbb{R})$* (Imperial College Press, 2012), for the elliptic–parabolic–hyperbolic trichotomy of one-parameter subgroups.
- Richard W. Sharpe, *Differential Geometry: Cartan's Generalization of Klein's Erlangen Program* (Springer, 1997), for parabolic subgroups, flags and the stabiliser of a degenerate form.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings* (Grundlehren der mathematischen Wissenschaften 294, Springer, 1991), for degenerate and non-degenerate quadratic forms and their isometry groups.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for the classification of forms by their radicals.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Graduate Texts in Mathematics 222, Springer, 2nd ed. 2015), for unipotent groups, the exponential map and the Lie algebra of a matrix group.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of the two-dimensional real algebras and their groups of units.
