# __The Split-Complex Quadratic Family__

## Introduction

The split-complex algebra $\mathbb{D} = \mathbb{R}[j]$, $j^2 = +1$, carries the quadratic family

$$
f_c(z) = z^2 + c, \qquad z, c \in \mathbb{D},
$$

the direct analogue of the family of *The Mandelbrot Set and the Quadratic Family*. The algebra is not a field: it has the two null directions spanned by the idempotents, and it is isomorphic, through the idempotent decomposition, to the product $\mathbb{R} \times \mathbb{R}$ of two real lines. That isomorphism breaks the quadratic map into a **pair of real quadratic maps**, and it is the whole content of the split-complex theory: the critical orbit, the escape and the connectedness locus are read on the pair of real maps, and what the definite complex case distributes over a connected parameter set the split case distributes over a product of two intervals. This article fixes the family, establishes the idempotent decomposition, defines the escape, computes the connectedness locus as a square, and compares it with the Mandelbrot set.

The article is the $\mathbb{D}$ instance of the quadratic family. The algebra and its idempotents are those of *Split-Complex Algebra*, *Split-Complex Idempotents and Projections* and *Split-Complex Zero Divisors*; the norm, its polarisation and the null cone are those of *Split-Complex Norm and Invertibility* and *Split-Complex Null Quadric and Projective Geometry*; the group of units acting by multiplication is that of *Hyperbolic Rotations*. The complex case that the comparison uses is *The Mandelbrot Set and the Quadratic Family*, and the escape radius of a real quadratic map is that article's. The Fatou and Julia sets of the family are the subject of *The Split-Complex Julia Sets* and their geometry of *The Hyperbolic Geometry of the Split-Complex Julia Sets*. No physics is invoked, and every numerical value displayed was recomputed.

## The Family and the Idempotent Decomposition

### The Algebra and the Idempotents

**Definition.** The **split-complex algebra** is $\mathbb{D} = \mathbb{R}[j]$ with $j^2 = +1$. A general element is $z = a + ja'$ with $a, a' \in \mathbb{R}$; the **conjugation** is $\bar z = a - ja'$; the **norm** is $N(z) = z\bar z = a^2 - a'^2$, an indefinite form of signature $(1,1)$; and the **idempotents** are

$$
\Pi_+ = \frac{1+j}{2}, \qquad \Pi_- = \frac{1-j}{2}, \qquad \Pi_\pm^2 = \Pi_\pm, \quad \Pi_+\Pi_- = 0, \quad \Pi_+ + \Pi_- = 1 .
$$

Every element decomposes uniquely as

$$
z = z_+\Pi_+ + z_-\Pi_-, \qquad z_+ = a+a', \quad z_- = a-a' ,
$$

and the **idempotent coordinates** $z_+, z_-$ are the values of $z$ under the two algebra homomorphisms $\mathbb{D} \to \mathbb{R}$ sending $j$ to $+1$ and to $-1$.

**Theorem (the isomorphism $\mathbb{D} \cong \mathbb{R}\times\mathbb{R}$).** The map

$$
\varphi : \mathbb{D} \longrightarrow \mathbb{R}^2, \qquad \varphi(z) = (z_+, z_-) = (a+a',\, a-a') ,
$$

is an isomorphism of real vector spaces and of rings, with the product of $\mathbb{R}^2$ taken componentwise; its inverse is $\varphi^{-1}(u,v) = \frac{u+v}{2} + j\,\frac{u-v}{2}$. The conjugation corresponds to the exchange of the two coordinates, $\varphi(\bar z) = (z_-, z_+)$, and the norm corresponds to the product, $N(z) = z_+z_-$.

**Proof.** The idempotents are the standard projections onto the two coordinates; linearity of $\varphi$ is clear, and multiplicativity is the computation $\varphi(zw) = (z_+w_+, z_-w_-)$, since $\Pi_+^2 = \Pi_+$, $\Pi_-^2 = \Pi_-$ and $\Pi_+\Pi_- = 0$. The inverse is verified by $z = z_+\Pi_+ + z_-\Pi_-$, and the conjugation is $\bar z = z_-\Pi_+ + z_+\Pi_-$, the exchange of the two coordinates. Finally $N(z) = z\bar z = z_+z_-$, by expanding $(z_+\Pi_+ + z_-\Pi_-)(z_-\Pi_+ + z_+\Pi_-)$ and using $\Pi_+^2 = \Pi_+$, $\Pi_-^2 = \Pi_-$, $\Pi_+\Pi_- = 0$, $\Pi_++\Pi_- = 1$.

### The Quadratic Map on the Pair

**Theorem (the recursion splits).** For $c = \gamma + j\gamma'$ with $c_+ = \gamma+\gamma'$ and $c_- = \gamma-\gamma'$, the iterate of $f_c$ is given componentwise:

$$
\varphi\bigl(f_c(z)\bigr) = \bigl(z_+^2 + c_+,\ z_-^2 + c_-\bigr) .
$$

Consequently, with $g_+(u) = u^2+c_+$ and $g_-(v) = v^2+c_-$ the two real quadratic maps of the pair,

$$
\varphi \circ f_c^n = (g_+^n, g_-^n) \circ \varphi \qquad \text{for every } n \geq 0 ,
$$

and the orbit of $z$ under $f_c$ is bounded if and only if both orbits $g_+^n(z_+)$ and $g_-^n(z_-)$ are bounded.

**Proof.** Since $\varphi$ is a ring isomorphism, $\varphi(f_c(z)) = \varphi(z)^2 + \varphi(c) = (z_+^2+c_+, z_-^2+c_-)$; iterating gives the displayed formula, and boundedness of a sequence in $\mathbb{R}^2$ is boundedness of both coordinates.

**Corollary (the critical set).** The derivative of $f_c$ is the multiplication by $2z$. As an element of the algebra, $2z$ vanishes only at $z = 0$; as a real-linear map of the plane, the multiplication by $2z$ has determinant $N(2z) = 4N(z)$ and is therefore singular exactly on the null cone $\mathcal{N} = \{N = 0\}$, where $2z$ is a zero divisor. So the critical set of $f_c$ as a real dynamical system is the union of the two null lines, and $0$ is its only point at which the derivative vanishes as an algebra element. The orbit of $0$ is the pair $(g_+^n(0), g_-^n(0))$ of the two real critical orbits, and it is this orbit that defines the connectedness locus below.

**Remark (the complex case for comparison).** In $\mathbb{C}$ the algebra is a field, the conjugation is the only nontrivial automorphism, and the pair of "conjugate coordinates" is not independent: the map $z^2+c$ is determined by the single complex parameter $c$, and the critical orbit is a single complex orbit. In $\mathbb{D}$ the two coordinates are independent real numbers and the parameter is genuinely two real parameters, so the family is parameterised by $\mathbb{R}^2$ and not by a field.

## The Escape

### The Norm and the Null Cone

**Definition.** The **null cone** of $\mathbb{D}$ is the zero set of the norm, $\mathcal{N} = \{z : N(z) = 0\} = \mathbb{R}\Pi_+ \cup \mathbb{R}\Pi_-$, the union of the two **null lines** $z_- = 0$ and $z_+ = 0$; its elements other than $0$ are the zero divisors of the algebra.

**Theorem (the failure of the norm as an escape radius).** The norm is indefinite: there are nonzero $z$ with $N(z) = 0$, and along the null lines the norm vanishes while the orbit of $f_c$ may be unbounded. Hence no condition of the form $N(z) > R$ detects the escape, and there is no single radius in the norm that plays the role of the escape radius of the complex case.

**Proof.** On the null line $z_+ = 0$ the norm is $N(z) = z_+z_- = 0$ for every $z$, while the coordinate $z_-$ evolves by $v \mapsto v^2+c_-$ and may diverge. So the norm cannot bound the orbit, and it also cannot detect divergence: the escape is read on the idempotent coordinates, not on the norm.

**Definition.** A point $z$ **escapes** under $f_c$ if $|f_c^n(z)| \to \infty$ in the Euclidean metric of the plane, equivalently, by the theorem above, if at least one of the two real orbits $g_+^n(z_+)$ or $g_-^n(z_-)$ escapes to infinity.

### The Escape Radii of the Pair

**Theorem.** Let

$$
R_+ = \frac{1+\sqrt{1+4|c_+|}}{2}, \qquad R_- = \frac{1+\sqrt{1+4|c_-|}}{2}
$$

be the least escape radii of the two real quadratic maps $g_+$, $g_-$ of the pair, in the sense of *The Escape Radius and the Green's Function*. Then $|z_+| > R_+$ implies $|g_+^n(z_+)| \to \infty$, and $|z_-| > R_-$ implies $|g_-^n(z_-)| \to \infty$; consequently $z$ escapes as soon as one of its two idempotent coordinates lies beyond the corresponding radius.

**Proof.** Each real map is a real quadratic with real parameter, and the escape radius of the real quadratic $x \mapsto x^2+d$ is the least positive root of $x^2-x-|d|=0$, which is $\frac12(1+\sqrt{1+4|d|})$, exactly as in the complex case. Applying this to $g_+$ and $g_-$ gives the two radii, and the escape of either coordinate is the escape of the point.

**Example (the radii).** For $c = 0$ both radii are $1$; for $c = -1$ (so $c_+ = c_- = -1$) both are $\frac12(1+\sqrt5) = 1.618034\ldots$; for $c = j$ the coordinates are $c_+ = 1$, $c_- = -1$, and both radii are again $\frac12(1+\sqrt5) = 1.618034\ldots$, while the two real maps are $u^2+1$, whose critical orbit escapes, and $v^2-1$, whose critical orbit is the attracting cycle $\{0,-1\}$. The values were recomputed from the formula.

**Remark (the two radii are genuinely needed).** Neither radius controls the other: the parameter $c = 1+j$ has $c_+ = 2$, $c_- = 0$, so $R_+ = 2$ and $R_- = 1$, and the coordinate $z_+$ escapes while $z_-$ converges to $0$. A point of the plane with $z_- = 0$ and $z_+$ between $1$ and $2$ escapes; a point with $z_+ = 0$ and $z_- = 0$ is fixed at $0$. So the escape criterion is a **pair** of one-dimensional criteria, and the region of non-escape is a rectangle in the idempotent coordinates, not a disk.

## The Connectedness Locus

**Definition.** The **connectedness locus** of the split-complex quadratic family is the set of parameters for which the critical orbit is bounded,

$$
M_{\mathbb{D}} = \{c \in \mathbb{D} : (f_c^n(0))_{n \geq 0} \text{ is bounded}\} .
$$

**Theorem.** The connectedness locus is the square

$$
M_{\mathbb{D}} = \varphi^{-1}\Bigl([-2,\tfrac14] \times [-2,\tfrac14]\Bigr) = \left\{c = \gamma+j\gamma' : -2 \leq \gamma+\gamma' \leq \tfrac14, \ -2 \leq \gamma-\gamma' \leq \tfrac14 \right\} ,
$$

the product of two real Mandelbrot intervals, with vertices $\frac14$, $-\frac78 \pm j\frac98$ and $-2$ in the coordinates $c = \gamma+j\gamma'$, centre $-\frac78$, diagonal $\frac94$ along the real axis and side length $\frac{9\sqrt2}{8}$.

**Proof.** The critical orbit is the pair of the two real critical orbits, and a real quadratic orbit is bounded exactly when the parameter lies in the interval $[-2,\tfrac14]$, which is the real slice of the Mandelbrot set. So $c \in M_{\mathbb{D}}$ if and only if both $c_+$ and $c_-$ lie in $[-2,\tfrac14]$. Translating by $\gamma = (c_++c_-)/2$ and $\gamma' = (c_+-c_-)/2$ gives the four vertices

$$
(c_+,c_-) = (\tfrac14,\tfrac14) \mapsto \tfrac14, \qquad (\tfrac14,-2) \mapsto -\tfrac78+j\tfrac98, \qquad (-2,\tfrac14) \mapsto -\tfrac78-j\tfrac98, \qquad (-2,-2) \mapsto -2 ,
$$

and the region is the square with these vertices; the centre is the average of the four vertices, $-\tfrac78$, the diagonal is the difference of the real vertices, $\tfrac14-(-2) = \tfrac94$, and the side is $\tfrac94/\sqrt2 = \tfrac{9\sqrt2}{8} = 1.5909902\ldots$.

**Example (the boundary values).** The parameter $c = \frac14$ gives $c_+ = c_- = \frac14$, the parabolic cusp of the real interval in both coordinates; $c = -2$ gives the tip in both; the parameter $-\frac78+j\frac98$ gives $c_+ = \frac14$ (the cusp) and $c_- = -2$ (the tip). At the four vertices the critical orbit is bounded and the parameter is on the boundary of $M_{\mathbb{D}}$, and the numerical orbits confirm the values.

**Remark (the contrast with the Mandelbrot set).** In the complex case the connectedness locus is the Mandelbrot set, a connected compact set of fractal boundary. Here it is a **square**, convex and of empty interior boundary: the two real parameters are independent, and the subdivision of the parameter space into the hyperbolic components of the complex case is replaced by the subdivision of each factor into the real hyperbolic intervals. The fractal content of the complex parameter plane has no analogue in the split parameter plane; the fractal content of the split family lies in the Julia sets of the individual parameters, which are the subject of *The Split-Complex Julia Sets*.

**Remark (the real slice).** For real parameters, $c = \gamma$ and $\gamma' = 0$, both coordinates equal $\gamma$, and $M_{\mathbb{D}} \cap \mathbb{R} = [-2,\tfrac14]$, the real slice of the complex Mandelbrot set. So the split-complex family restricts on the real axis to the real quadratic family, and the two-coordinate structure degenerates to a single interval.

**Theorem (the norm along the critical orbit).** Along the critical orbit the norm is the product of the two real orbits,

$$
N(f_c^n(0)) = g_+^n(0)\, g_-^n(0) ,
$$

so $N$ vanishes at the $n$-th step exactly when one of the two real orbits passes through $0$. In particular $N$ is not a Lyapunov function and the vanishing of $N$ at some step does not decide the boundedness of the orbit.

**Proof.** The norm is multiplicative for the ring isomorphism, $N(z) = z_+z_-$, and the coordinates of $f_c^n(0)$ are $g_+^n(0)$ and $g_-^n(0)$.

**Example.** For $c = j$ the critical orbit in the idempotent coordinates is $(g_+^n(0), g_-^n(0)) = (0,1,2,5,\ldots;\ 0,-1,0,-1,\ldots)$, and the norm along it is $(0\cdot0,\ 1\cdot(-1),\ 2\cdot0,\ 5\cdot(-1),\ \ldots) = (0,-1,0,-5,0,-677,\ldots)$, which alternates between $0$ and nonzero values and is bounded in neither sign; the first coordinate escapes while the second cycles.

## Summary

The split-complex quadratic family $f_c(z) = z^2+c$ on $\mathbb{D} = \mathbb{R}[j]$ is, through the idempotent decomposition $\varphi(z) = (z_+,z_-) = (a+a',a-a')$, the pair of real quadratic maps $u \mapsto u^2+c_+$ and $v \mapsto v^2+c_-$ acting on the two coordinates. The critical set is the null cone $\mathcal{N}$ — the derivative is the multiplication by $2z$, singular exactly where $2z$ is a zero divisor — and the critical value of the point $0$ is $c$; the other critical points $t\Pi_\pm$ have the images $t^2\Pi_\pm+c$, and the orbit of $0$ is the pair of the two real critical orbits and is the orbit that defines the connectedness locus. The orbit of a point is bounded exactly when both coordinate orbits are bounded. The norm $N = a^2-a'^2 = z_+z_-$ is indefinite and vanishes on the two null lines; it cannot serve as an escape radius, and the escape is decided by the two real radii $R_\pm = \frac12(1+\sqrt{1+4|c_\pm|})$ separately, not by a single radius.

The connectedness locus is the square $\varphi^{-1}([-2,\frac14]\times[-2,\frac14])$, the product of the two real Mandelbrot intervals, with vertices $\frac14$, $-\frac78\pm j\frac98$, $-2$, centre $-\frac78$ and side $\frac{9\sqrt2}{8}$; on the real axis it is the interval $[-2,\frac14]$ of the real quadratic family. The fractal content of the complex parameter plane — the Mandelbrot set and its hyperbolic components — is replaced here by the convex square, and the fractal content of the split family is carried by the Julia sets of the individual parameters, treated in *The Split-Complex Julia Sets*. The algebra, the idempotents and the null cone are those of *Split-Complex Algebra*, *Split-Complex Idempotents and Projections* and *Split-Complex Null Quadric and Projective Geometry*; the real quadratic theory that the pair inherits is that of *The Mandelbrot Set and the Quadratic Family* and *The Escape Radius and the Green's Function*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D} = \mathbb{R}[j]$, $j^2=+1$ | Split-complex algebra |
| $z = a + ja'$ | General element, $a, a'\in\mathbb{R}$ |
| $\bar z = a-ja'$ | Conjugation |
| $N(z) = a^2-a'^2 = z_+z_-$ | Norm, signature $(1,1)$ |
| $\Pi_\pm = \tfrac12(1\pm j)$ | Idempotents |
| $z_\pm = a\pm a'$ | Idempotent coordinates |
| $\varphi(z) = (z_+,z_-)$ | Isomorphism $\mathbb{D}\to\mathbb{R}^2$ |
| $f_c(z) = z^2+c$ | The split-complex quadratic family |
| $c_\pm = \gamma\pm\gamma'$ | Idempotent coordinates of $c = \gamma+j\gamma'$ |
| $g_\pm$ | The two real quadratic maps $u\mapsto u^2+c_\pm$ |
| $\mathcal{N} = \mathbb{R}\Pi_+\cup\mathbb{R}\Pi_-$ | Null cone, the two null lines |
| $R_\pm = \tfrac12(1+\sqrt{1+4\lvert c_\pm\rvert})$ | The two real escape radii |
| $M_{\mathbb{D}}$ | Connectedness locus, the square $\varphi^{-1}([-2,\tfrac14]^2)$ |

## Further Reading

- I. M. Yaglom, *Complex Numbers in Geometry* (Academic Press, New York, 1968), for the split-complex (hyperbolic) numbers and their idempotent decomposition.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, Natick, 2003), for the classification of the two-dimensional real algebras.
- Benoit B. Mandelbrot, "On the quadratic mapping $z \mapsto z^2-\mu$", *Physica D* 7 (1983), 224–239, for the quadratic family in the complex case.
- Robert L. Devaney, *An Introduction to Chaotic Dynamical Systems*, 2nd edition (Addison-Wesley, 1989), for the real quadratic family and its interval of bounded orbits.
- Paul Blanchard, Robert L. Devaney and Linda Keen, *Complex Dynamics and Related Topics* (Prentice Hall, 2004), for the quadratic family and its parameter space.
