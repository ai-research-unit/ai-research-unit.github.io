
# __Dual-Numbers Topology__

## Introduction

This article collects the topology of the dual-number algebra $\mathbb{D}' = \mathbb{R}[\varepsilon]/(\varepsilon^2)$ as a space: its contractibility, the Euclidean unit sphere, the norm-one set, the group of units and its homotopy, the maximal ideal as a closed nilpotent direction, and the boundary of the group of units. It uses the algebra and its submodules of *Dual-Numbers Algebra* and *Dual-Number Subspaces*, the norm form and unit criterion of *Dual-Numbers Norm and Invertibility*, the maximal ideal of *Dual-Numbers Ideals and the Maximal Ideal*, the zero-divisor set of *Dual-Numbers Zero Divisors*, and the boundary of the unit group. The structural model is *Biquaternion Topology*, which studies the Euclidean sphere and the null cone of $\mathbb{B}$.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. Throughout the algebra is $\mathbb{D}'$ over $\mathbb{R}$, a general dual number is

$$
Z = a + \varepsilon b, \qquad a, b \in \mathbb{R},
$$

with $a = \operatorname{Re} Z$, $b = \operatorname{Inf} Z$, norm form $N(Z) = Z\bar{Z} = a^2$, Euclidean norm $\|Z\|_E = \sqrt{a^2 + b^2}$, maximal ideal $\mathfrak{m} = (\varepsilon) = \varepsilon\mathbb{R}$, and unit group $(\mathbb{D}')^\times = \{a \neq 0\}$. To keep the two notions apart, the norm form is written $N$ and the Euclidean form $\|\cdot\|_E$; they are distinct, and the whole topology is carried by the second.

## The Dual Plane as a Topological Space

### The Underlying Space

The map

$$
Z = a + \varepsilon b \longmapsto (a, b)
$$

is a linear isometry of $(\mathbb{D}', \|\cdot\|_E)$ onto $\mathbb{R}^2$ with the Euclidean metric. So the topology of $\mathbb{D}'$ is the ordinary Euclidean topology of the plane, and the basis $(1, \varepsilon)$ is an orthonormal basis for $\|\cdot\|_E$.

**Proposition.** The product is bilinear, hence continuous, so $\mathbb{D}'$ is a topological algebra over $\mathbb{R}$. Inversion is continuous on the units, so $(\mathbb{D}')^\times$ is a topological group and the shear subgroup $1 + \mathfrak{m}$ is a closed subgroup.

**Proof.** Bilinearity gives continuity of the product from the continuity of the algebra operations on $\mathbb{R}^2$. The inverse $a + \varepsilon b \mapsto a^{-1} - a^{-2}\varepsilon b$ is continuous where $a \neq 0$; $1 + \mathfrak{m} = \{a = 1\}$ is closed. $\square$

### The Distinction Between the Two Forms

The norm form $N(Z) = a^2$ and the Euclidean form $a^2 + b^2$ induce different geometries on the same space. The Euclidean form gives the distance and hence the topology; the norm form is the multiplicative form and has no metric content. Although $N$ is continuous, its vanishing does not control the Euclidean size: a sequence with $N(Z_n) \to 0$ need not have $Z_n \to 0$, because $Z_n$ may move along the null line $\mathfrak{m}$.

## Contractibility

### The Algebra

**Theorem.** $\mathbb{D}'$ is contractible, hence path-connected and simply connected, with $\pi_n(\mathbb{D}') = 0$ for all $n \geq 1$.

**Proof.** The straight-line homotopy

$$
H(t, Z) = (1 - t)Z, \qquad t \in [0, 1],
$$

is continuous, with $H(0, Z) = Z$ and $H(1, Z) = 0$; so the identity is homotopic to the constant map at $0$. $\square$

So every map into $\mathbb{D}'$ is null-homotopic, and every subset of $\mathbb{D}'$ that is star-shaped with respect to the origin is contractible by the same homotopy.

### The Distinguished Subsets

The two submodules are star-shaped, hence contractible, and homeomorphic to $\mathbb{R}$:

$$
R_{\mathbb{D}'} = \{b = 0\} \cong \mathbb{R}, \qquad \mathfrak{m} = \varepsilon R_{\mathbb{D}'} = \{a = 0\} \cong \mathbb{R}.
$$

So the two eigenspaces of dual conjugation carry no topology beyond that of the line. The entire topological content of the algebra lies in the complement of the maximal ideal and in the interaction of the two lines, not in the lines themselves.

## The Euclidean Unit Sphere

### Definition

**Definition.** The **Euclidean unit sphere** is

$$
S^1_E = \{Z \in \mathbb{D}' : \|Z\|_E = 1\} = \{(a,b) : a^2 + b^2 = 1\} \cong S^1.
$$

It is a closed, compact, connected one-manifold.

### Multiplication Does Not Preserve the Euclidean Norm

**Proposition.** The Euclidean norm is not multiplicative, and the Euclidean unit sphere is not closed under multiplication.

**Proof.** For $Z = 1 + \varepsilon$ one has $\|Z\|_E = \sqrt{2}$ and $Z^2 = 1 + 2\varepsilon$ with $\|Z^2\|_E = \sqrt{5} \neq 2 = \|Z\|_E^2$. For closure, $\varepsilon$ lies on $S^1_E$ because $\|\varepsilon\|_E = 1$, but $\varepsilon^2 = 0 \notin S^1_E$. $\square$

So $S^1_E$ is not a subgroup of $(\mathbb{D}')^\times$; indeed $\varepsilon \in S^1_E$ is a zero divisor, so $S^1_E \not\subseteq (\mathbb{D}')^\times$. The sphere that *is* a union of group components is the norm-one set of the next section, not the Euclidean sphere.

## The Norm-One Set and the Group of Units

### The Norm-One Set

**Definition.** The **norm-one set** is

$$
H = \{Z \in \mathbb{D}' : N(Z) = 1\} = \{a + \varepsilon b : a = \pm 1\},
$$

the union of the two parallel lines $a = 1$ and $a = -1$.

**Proposition.** $H$ is a closed subset with two contractible components, each homeomorphic to a line; its identity part is $H_0 = 1 + \mathfrak{m} = \{a = 1\}$. Hence $H$ has the homotopy type of $S^0$.

**Proof.** $N(Z) = a^2 = 1$ gives $a = \pm 1$ with $b$ free; the two lines are closed and contractible, and the line $a = 1$ is $1 + \mathfrak{m}$. $\square$

So the norm-one set of the dual numbers is not a circle, as in the complex case, nor a hyperbola with two branches, as in the split-complex case, but a pair of parallel lines; its homotopy type is that of the two-point space.

### The Group of Units

**Theorem.** The group of units is $(\mathbb{D}')^\times = \{a \neq 0\}$, the complement of the maximal ideal; as a space it is the disjoint union of the two open half-planes $\{a > 0\}$ and $\{a < 0\}$, each contractible. The homotopy type of $(\mathbb{D}')^\times$ is that of $S^0 = \{\pm 1\}$, onto which it deformation retracts by $Z \mapsto \operatorname{sgn}(a)$; hence

$$
\pi_0\bigl((\mathbb{D}')^\times\bigr) = \mathbb{Z}/2, \qquad \pi_n\bigl((\mathbb{D}')^\times\bigr) = 0 \quad (n \geq 1).
$$

**Proof.** $(\mathbb{D}')^\times = \mathbb{D}' \setminus \mathfrak{m}$ is the complement of the closed line $\mathfrak{m}$, hence two open half-planes, each star-shaped with respect to $\pm 1$ and contractible. The map $H(t, Z) = (1-t)Z + t\operatorname{sgn}(a)$ is a continuous deformation retraction onto $\{\pm 1\}$. $\square$

**Corollary.** The maximal compact subgroup of $(\mathbb{D}')^\times$ is $\{\pm 1\} \cong S^0$, and the unit group has trivial fundamental group despite being disconnected: on each contractible component every loop is null-homotopic.

## The Maximal Ideal as a Closed Nilpotent Direction

### The Maximal Ideal

**Theorem.** The maximal ideal $\mathfrak{m} = \varepsilon\mathbb{R}$ is a closed, connected, contractible subset of $\mathbb{D}'$, homeomorphic to the real line. It has empty interior and its complement $(\mathbb{D}')^\times$ is open and dense.

**Proof.** $\mathfrak{m} = \{a = 0\}$ is closed, since $\operatorname{Re}$ is continuous; it is homeomorphic to $\mathbb{R}$ via $\varepsilon b \leftrightarrow b$, hence contractible. A line has empty interior in the plane, and the complement of a line is open and dense. $\square$

### The Null Line

**Definition.** The **null line** (or isotropic line) is $N^{-1}(0) = \mathfrak{m}$, the vanishing locus of the norm form; the **zero-divisor set** $\mathcal{Z} = \mathfrak{m} \setminus \{0\}$ is the null line punctured at the origin.

**Proposition.** The null line is a closed algebraic cone with apex $0$, and it is the radical of the norm form. The zero-divisor set $\mathcal{Z}$ is neither open nor closed; its closure is $\mathfrak{m}$ and its complement is dense.

**Proof.** $N(tZ) = t^2 N(Z)$ makes $N^{-1}(0)$ a cone; $N(Z+W) = N(Z) + 2B(Z,W) + N(W)$ with $B(Z,W) = a c$ shows that the radical, the set $B$-orthogonal to the whole plane, is exactly $\mathfrak{m}$. The punctured line is not open (a line has empty interior) nor closed (its limit points include the origin); its closure is the line and the complement of a punctured line is dense. $\square$

### The Link of the Null Line

**Definition.** The **link** of the null line is

$$
L = \mathfrak{m} \cap S^1_E = \{+\varepsilon,\, -\varepsilon\} \cong S^0.
$$

**Proposition.** Every nonzero element of $\mathfrak{m}$ is uniquely $t\,u$ with $t = \|Z\|_E > 0$ and $u \in L$, so the null line is the cone on its link. The link has two points, reflecting that the isotropic line is the *double* line $a^2 = 0$: its intersection with the unit circle is double-counted.

**Proof.** $\varepsilon b = |b|\operatorname{sgn}(b)\varepsilon$ with $\|\varepsilon b\|_E = |b|$; the two unit points are $\pm\varepsilon$. The equation $a^2 = 0$ is the square of the linear equation $a = 0$, so its projective solution is a single point of multiplicity two, met twice by the circle. $\square$

This is the topological face of the degeneracy. For a non-degenerate indefinite form in two variables the isotropic cone is a pair of lines, of real dimension one, and its link is the four-point set of normalized null directions, as in the split complex case. For the degenerate dual form the cone is a single line, but the form is the square $a^2$ of the linear form $a$, so the line is met with multiplicity two: the link is the two-point space $\{\pm\varepsilon\}$, which counts the one projective null direction twice.

## The Boundary of the Unit Group

### The Domain and Its Boundary

The group of units is $\mathbb{D}' \setminus \mathfrak{m}$, an open dense subset of the plane with two connected components, distinguished by the sign of the real part. Its complement, hence its boundary, is the maximal ideal:

$$
\partial\bigl((\mathbb{D}')^\times\bigr) = \mathfrak{m}.
$$

**Proposition.** The boundary $\mathfrak{m}$ is a closed subset of the plane of empty interior, homeomorphic to $\mathbb{R}$, and it is the closure of the zero-divisor set $\mathcal{Z} = \mathfrak{m} \setminus \{0\}$. Each of the two components of the unit group is homeomorphic to an open half-plane, and the boundary separates them.

**Proof.** The maximal ideal is the line $\{a = 0\}$, closed with empty interior in the plane and homeomorphic to $\mathbb{R}$ through $b \mapsto \varepsilon b$; its points with $b \neq 0$ are exactly the zero divisors. The components $\{a > 0\}$ and $\{a < 0\}$ are open half-planes, and every path between them meets the line $\{a = 0\}$. $\square$

### Comparison with the Biquaternion Boundary

In the biquaternion case the boundary of the unit group is the zero-divisor cone, of real codimension two. In the dual case the boundary is a line, of real codimension one, so it is a topological wall rather than a cone, and it separates the two components of the unit group.

## Comparison with the Topology of the Other Systems

The topology of the dual numbers sits at the degenerate end of the family.

| System | Ambient space | Unit group | Norm-one set | Link of the isotropic set |
|---|---|---|---|---|
| $\mathbb{C}$ | $\mathbb{R}^2$, contractible | $\mathbb{C}^\times \simeq S^1$ | circle $S^1$ | $\varnothing$ (no null directions) |
| $\mathbb{D} = \mathbb{R}[j]$ | $\mathbb{R}^2$, contractible | $4$ contractible components, $\simeq S^0 \times S^0$ | hyperbola, two branches, $\simeq S^0$ | four points (two null lines) |
| $\mathbb{D}'$ | $\mathbb{R}^2$, contractible | $2$ contractible components, $\simeq S^0$ | two parallel lines, $\simeq S^0$ | two points (a doubled pair) |
| $\mathbb{H}$ | $\mathbb{R}^4$, contractible | $\simeq S^3$ | $S^3$ | $\varnothing$ |
| $\mathbb{B} \cong M_2(\mathbb{C})$ | $\mathbb{R}^8$, contractible | $GL_2(\mathbb{C})$ | $SL(2,\mathbb{C})$ | $(S^3\times S^3)/U(1)$, $\pi_2 = \mathbb{Z}$ |

Three features distinguish the dual row. First, the unit group has exactly two components, one fewer than the split complex case, because the norm form has rank one rather than two; in both cases the components are contractible, so all higher homotopy is trivial. Second, the norm-one set is a pair of parallel lines, the degenerate limit of the hyperbola, with the same homotopy type $S^0$. Third, the isotropic set is a line whose link is two points rather than a sphere; the projective isotropic set is a single point of multiplicity two, so the link counts it twice, which is the reason the dual case has no analogue of the connected link $L \cong (S^3\times S^3)/U(1)$ of the biquaternion null cone.

## Summary

The dual-number algebra $\mathbb{D}'$, with its Euclidean topology, is a contractible topological algebra homeomorphic to $\mathbb{R}^2$, with all homotopy groups trivial. The Euclidean unit sphere is the circle $S^1 \cong S^1_E$, on which the zero divisor $\varepsilon$ lies, so the sphere is not contained in the group of units, and the Euclidean form is not multiplicative. The norm-one set is the pair of parallel lines $a = \pm 1$, with identity component the shear line $1 + \mathfrak{m}$; it has the homotopy type of $S^0$. The group of units is the complement of the maximal ideal, two contractible open half-planes, with homotopy type $S^0$, fundamental group trivial, and maximal compact subgroup $\{\pm 1\}$. The maximal ideal is a closed nilpotent direction, homeomorphic to $\mathbb{R}$, contractible, of empty interior, and it is the null line of the norm form; its link in the Euclidean sphere is the two-point space $\{\pm\varepsilon\}$, the double count of the degenerate isotropic line. The maximal ideal is exactly the boundary of the group of units. In the family of the corpus's number systems the dual row is the degenerate member: two contractible unit-group components against the split complex's four, and a doubled point link against the biquaternion cone's connected five-manifold.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}' = \mathbb{R}[\varepsilon]/(\varepsilon^2)$ | Dual-number algebra; $\varepsilon^2 = 0$ |
| $Z = a + \varepsilon b$ | General dual number |
| $a = \operatorname{Re} Z$, $b = \operatorname{Inf} Z$ | Real and infinitesimal parts |
| $N(Z) = a^2$ | Norm form |
| $\|Z\|_E = \sqrt{a^2 + b^2}$ | Euclidean norm, giving the topology |
| $S^1_E = \{\|Z\|_E = 1\}$ | Euclidean unit sphere $\cong S^1$ |
| $H = \{N(Z) = 1\}$ | Norm-one set, lines $a = \pm 1$, $\simeq S^0$ |
| $\mathfrak{m} = (\varepsilon) = \{a = 0\}$ | Maximal ideal, null line, $\cong \mathbb{R}$ |
| $\mathcal{Z} = \mathfrak{m}\setminus\{0\}$ | Zero-divisor set |
| $(\mathbb{D}')^\times = \{a \neq 0\}$ | Group of units, two contractible components |
| $1 + \mathfrak{m} = \{a = 1\}$ | Shear line, identity component of $H$ |
| $L = \mathfrak{m} \cap S^1_E = \{\pm\varepsilon\}$ | Link of the null line, $\cong S^0$ |
| $\pi_0((\mathbb{D}')^\times) = \mathbb{Z}/2$ | Component count of the unit group |
| $\mathbb{D}, \mathbb{H}, \mathbb{B}$ | Split complex, quaternion and biquaternion systems, the comparisons |

## Further Reading

- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, Cambridge, 2002), for homotopy groups, deformation retractions, and the links of cones.
- Glen E. Bredon, *Topology and Geometry* (Graduate Texts in Mathematics 139, Springer, New York, 1993), for the topology of algebraic varieties and the link of a cone.
- John Milnor and James D. Stasheff, *Characteristic Classes* (Annals of Mathematics Studies 76, Princeton University Press, 1974), for the topology of $\mathbb{R}^n \setminus \{0\}$ and sphere bundles, as the comparison objects.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings* (Grundlehren der mathematischen Wissenschaften 294, Springer, Berlin, 1991), for the radical of a degenerate quadratic form and its isotropic part.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, Natick, 2003), for the unit groups and spheres of the number systems of the family.
- Vladimir V. Kisil, *Geometry of Möbius Transformations: Elliptic, Parabolic and Hyperbolic Actions of $SL(2,\mathbb{R})$* (Imperial College Press, London, 2012), for the parabolic case in the elliptic–parabolic–hyperbolic trichotomy of the unit groups.
