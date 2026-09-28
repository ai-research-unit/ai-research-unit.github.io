
# __Dual-Number Subspaces__

## Introduction

This article collects the submodule structure of the dual-number algebra $\mathbb{D}'_R = R[\varepsilon]/(\varepsilon^2)$ and the relations among its distinguished submodules. It follows *Dual-Numbers Algebra* for the two conjugations and the two distinguished submodules, *Dual-Numbers Norm and Invertibility* for the norm, and *Dual-Numbers Ideals and the Maximal Ideal* for the ideal structure. Its structural model is *Biquaternion Relations Between Subspaces*, in which a lattice of six subspaces is organized by the four conjugations; here only one nontrivial conjugation exists, and the lattice is correspondingly small.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. Throughout, $R$ is a commutative ring with identity in which $2$ is invertible; the geometric specialisation is $R = \mathbb{R}$, and then the algebra is written $\mathbb{D}'$. A general dual number is

$$
Z = a + \varepsilon b, \qquad a, b \in R,
$$

with $a = \operatorname{Re} Z$, $b = \operatorname{Inf} Z$, dual conjugation $\bar{Z} = a - \varepsilon b$, norm $N(Z) = Z\bar{Z} = a^2$, and maximal ideal $\mathrm{M} = (\varepsilon)$. The two distinguished submodules are

$$
R_{\mathbb{D}'} = R\cdot 1 = \{Z : \bar{Z} = Z\}, \qquad \varepsilon R_{\mathbb{D}'} = \varepsilon R = \{Z : \bar{Z} = -Z\}.
$$

The scope boundaries are these. This article owns the submodule lattice, the relations among the submodules, and the analysis that the two submodules carry. The ideals and the Peirce-type decomposition belong to *Dual-Numbers Ideals and the Maximal Ideal*; the classification of the zero divisors belongs to *Dual-Numbers Zero Divisors*; limits, continuity and the Cauchy–Riemann system as whole-plane notions belong to *Dual-Numbers Analysis*; the global integration theory belongs to *Dual-Numbers Integration*. The two submodules are treated first as $R$-linear objects and then as the carriers of the differential operators, and the reader is referred elsewhere for their ideal-theoretic role. The second half of the article passes from the algebraic coordinates $a, b$ of the constant coefficients to the analytic coordinates $Z = x + y\varepsilon$ of *Dual-Numbers Analysis*; the change is one of letters only.

## The Decompositions

### The Conjugate Decomposition

Dual conjugation $\bar{\cdot}$ is an involution of $\mathbb{D}'_R$ with eigenvalues $+1$ and $-1$, and its eigenspace decomposition is

$$
\mathbb{D}'_R = R_{\mathbb{D}'} \oplus \varepsilon R_{\mathbb{D}'}, \qquad Z = \underbrace{a}_{+1} + \underbrace{\varepsilon b}_{-1}.
$$

The two projections are $Z \mapsto \tfrac{1}{2}(Z + \bar{Z}) = \operatorname{Re}(Z)$ and $Z \mapsto \tfrac{1}{2}(Z - \bar{Z}) = \operatorname{Inf}(Z)\varepsilon$.

### The Real–Infinitesimal Decomposition

The same decomposition is the **real–infinitesimal decomposition**, written in the coordinates of the basis:

$$
Z = a + \varepsilon b, \qquad a \in R_{\mathbb{D}'}, \quad \varepsilon b \in \varepsilon R_{\mathbb{D}'}.
$$

It is not a second decomposition but the same one: the two names record the two ways of describing the same pair of eigenspaces.

### There Is No Third Decomposition

The biquaternion algebra carries four conjugations, and their eigenspaces generate six distinct subspaces, which is why *Biquaternion Relations Between Subspaces* has a lattice to organize. Over a field $k$, $\mathbb{D}'_k$ has exactly one nontrivial involution, namely dual conjugation, and hence exactly one pairing of eigenspaces. There is no analogue of the quaternion conjugation $\bar{\cdot}$, of the complex conjugation ${}^{*}$ distinct from it, or of the Hermitian and anti-Hermitian subspaces. So the single decomposition above is the whole of the submodule structure.

## The Two Submodules at a Glance

| Submodule | Description | $R$-rank | Generator | Square in itself | Closed under $Z \mapsto \varepsilon Z$ |
|---|---|---|---|---|---|
| $R_{\mathbb{D}'}$ | $+1$-eigenspace of $\bar{\cdot}$ | $1$ | $1$ | yes (it is a subalgebra) | no ($\varepsilon \notin R_{\mathbb{D}'}$) |
| $\varepsilon R_{\mathbb{D}'}$ | $-1$-eigenspace of $\bar{\cdot}$ | $1$ | $\varepsilon$ | yes (it squares to $0$) | yes (it is an ideal) |

The two submodules have the same rank, and they differ in every structural respect that matters: one contains the identity and is a subalgebra, the other is nilpotent and is an ideal.

### The Basis and the Dimension

**Proposition.** $\{1, \varepsilon\}$ is an $R$-basis of $\mathbb{D}'_R$, and $\{1\}$, $\{\varepsilon\}$ are $R$-bases of $R_{\mathbb{D}'}$ and $\varepsilon R_{\mathbb{D}'}$ respectively. Hence $\dim_R R_{\mathbb{D}'} = \dim_R \varepsilon R_{\mathbb{D}'} = 1$ and $\dim_R \mathbb{D}'_R = 2$.

**Proof.** $R[\varepsilon]/(\varepsilon^2)$ has $\{1, \varepsilon\}$ as a free basis by construction, and the two eigenspaces are spanned by the two basis vectors.

## The Coordinate Blocks

With respect to the basis $(1, \varepsilon)$, the group $\mathbb{D}'_R$ is the free module $R \oplus R$, and a general element is the coordinate pair $(a, b)$:

$$
Z = a + \varepsilon b \;\longleftrightarrow\; (a, b) \in R \oplus R.
$$

The two submodules are the coordinate axes: $R_{\mathbb{D}'} = \{b = 0\}$ and $\varepsilon R_{\mathbb{D}'} = \{a = 0\}$. Multiplication in coordinates is

$$
(a, b)(c, d) = (a c,\; a d + b c),
$$

the truncated polynomial product. The conjugation is the coordinatewise sign change $(a, b) \mapsto (a, -b)$, and the norm is $N(a, b) = a^2$, the square of the first coordinate. So the submodule structure is the coordinate structure of the free module $R^2$ together with the diagonal sign action of the involution.

## The Intersections

**Proposition.** $R_{\mathbb{D}'} \cap \varepsilon R_{\mathbb{D}'} = \{0\}$; this is the only intersection of distinct positive-dimensional submodules, and it is the intersection of the two eigenspaces of an involution.

**Proof.** An element of the intersection has $b = 0$ and $a = 0$, hence is $0$.

**Proposition.** The intersections with the maximal ideal are

$$
R_{\mathbb{D}'} \cap \mathrm{M} = \{0\}, \qquad \varepsilon R_{\mathbb{D}'} \cap \mathrm{M} = \varepsilon R_{\mathbb{D}'}.
$$

**Proof.** $\mathrm{M} = \varepsilon R_{\mathbb{D}'}$, so the second identity is immediate; the first is the preceding proposition.

So the maximal ideal coincides with one of the two submodules and meets the other only at the origin.

## The Sums

**Proposition.** $R_{\mathbb{D}'} + \varepsilon R_{\mathbb{D}'} = \mathbb{D}'_R$, and the sum is direct. The maximal ideal satisfies $\mathrm{M} + R_{\mathbb{D}'} = \mathbb{D}'_R$.

**Proof.** Direct from the basis $\{1, \varepsilon\}$ and the identity $\mathrm{M} = \varepsilon R_{\mathbb{D}'}$.

**Corollary.** Every element of $\mathbb{D}'_R$ is uniquely a sum of an element of $R_{\mathbb{D}'}$ and an element of $\varepsilon R_{\mathbb{D}'}$; the uniqueness is the statement that the sum is direct, and it is equivalent to the intersection being zero.

## The Involutions as Sign Patterns

An $R$-linear involution $s$ that is also an algebra automorphism fixes $1$ and, by the automorphism theorem of *Dual-Numbers Automorphisms and Derivations*, is $\varphi_c$ with $\varphi_c(\varepsilon) = \varepsilon c$ for some $c \in R^\times$; it is an involution exactly when $c^2 = 1$. Over a field (or, more generally, an integral domain) this gives $c = \pm 1$, so the involutions are the sign patterns

$$
(+,+) : (a, b) \mapsto (a, b) \qquad \text{(identity)}, \qquad (+,-) : (a, b) \mapsto (a, -b) \qquad \text{(dual conjugation)}.
$$

There are exactly two over a field, and the second is the unique nontrivial one; over a general commutative ring there may be further involutions, one for every unit $c$ with $c^2 = 1$. The biquaternion algebra has four conjugations, whose sign patterns on the six subspaces fill a richer table; the reason for the difference is that $\mathbb{D}'_R$ has only one unit $\varepsilon$ of square zero up to scaling, whereas $\mathbb{B}$ has the two independent quaternion units and the scalar imaginary, giving four independent sign choices.

**Remark.** The sign pattern $(+,+)$ fixes both submodules pointwise, and $(+,-)$ fixes $R_{\mathbb{D}'}$ pointwise while negating $\varepsilon R_{\mathbb{D}'}$. Only the diagonal entries are free; an automorphism of $\mathbb{D}'_R$ cannot exchange the two submodules, because $1$ must be fixed and $\varepsilon$ must go to a multiple of $\varepsilon$. This is the submodule-theoretic content of the automorphism group $\operatorname{Aut}(\mathbb{D}'_R) \cong R^\times$ computed in *Dual-Numbers Automorphisms and Derivations*.

## How the Operations Act on the Splits

### Multiplication by $\varepsilon$

The operator $E = \varepsilon\cdot$ acts on the two submodules as

$$
E : R_{\mathbb{D}'} \longrightarrow \varepsilon R_{\mathbb{D}'}, \qquad a \mapsto \varepsilon a, \qquad E : \varepsilon R_{\mathbb{D}'} \longrightarrow 0, \qquad \varepsilon b \mapsto 0.
$$

So $E$ has $\ker E = \varepsilon R_{\mathbb{D}'}$ and $\operatorname{im}E = \varepsilon R_{\mathbb{D}'}$: the kernel and the image coincide. This is the submodule form of the nilpotence $\mathrm{M}^2 = 0$.

### The Norm on the Splits

The norm is additive on the direct sum and depends only on the first summand:

$$
N(a + \varepsilon b) = N(a) + N(\varepsilon b) = a^2 + 0 = a^2.
$$

On the two submodules,

$$
N(R_{\mathbb{D}'}) \subseteq R_{\mathbb{D}'}, \qquad N(\varepsilon R_{\mathbb{D}'}) = 0.
$$

So the norm restricts to a multiplicative form on the real submodule and vanishes identically on the infinitesimal submodule; this is the submodule statement of the degeneracy of $N$.

### The Product and the Bracket

Since $\mathbb{D}'_R$ is commutative, the commutator bracket vanishes: $[Z, W] = ZW - WZ = 0$ for all $Z, W$. The product respects the splits in the sense that

$$
R_{\mathbb{D}'} \cdot R_{\mathbb{D}'} \subseteq R_{\mathbb{D}'}, \qquad R_{\mathbb{D}'} \cdot \varepsilon R_{\mathbb{D}'} \subseteq \varepsilon R_{\mathbb{D}'}, \qquad \varepsilon R_{\mathbb{D}'} \cdot \varepsilon R_{\mathbb{D}'} = 0.
$$

So the real submodule is a subalgebra, the infinitesimal submodule is an ideal, and the product of two infinitesimal elements vanishes.

## Worked Verifications

### The Decomposition

For $Z = 2 + 3\varepsilon$ the conjugate decomposition is $Z = 2 + 3\varepsilon$ with $2 \in R_{\mathbb{D}'}$ and $3\varepsilon \in \varepsilon R_{\mathbb{D}'}$; the projections are $\tfrac{1}{2}(Z + \bar{Z}) = 2$ and $\tfrac{1}{2}(Z - \bar{Z}) = 3\varepsilon$.

### An Intersection

$R_{\mathbb{D}'} \cap \varepsilon R_{\mathbb{D}'} = \{0\}$: the element $a + \varepsilon b$ lies in both submodules only if $b = 0$ and $a = 0$.

### A Pair That Spans the Algebra

$1 \in R_{\mathbb{D}'}$ and $\varepsilon \in \varepsilon R_{\mathbb{D}'}$ are linearly independent and span $\mathbb{D}'$.

### A Mixed Element and Its Blocks

For $Z = -4 + \varepsilon$ the blocks are $\operatorname{Re}(Z) = -4$ and $\operatorname{Inf}(Z)\varepsilon = \varepsilon$; the norm is $N(Z) = (-4)^2 = 16$, read from the real block alone.

## The Analytic Coordinates

The remainder of the article reads the two submodules as the carriers of the differential operators, and for that it uses the analytic coordinates of *Dual-Numbers Analysis* in place of the algebraic pair $a, b$: a variable dual number is written

$$
Z = x + y\varepsilon, \qquad x, y \in \mathbb{R},
$$

with $x = \operatorname{Re} Z$, $y = \operatorname{Inf} Z$; the algebraic articles keep $a, b$ for the constant coefficients. The augmentation is $\pi(Z) = x$, the maximal ideal is $\mathrm{M} = \varepsilon\mathbb{R} = \{x = 0\}$, and the two distinguished submodules are $R_{\mathbb{D}'} = \{y = 0\}$ and $\varepsilon R_{\mathbb{D}'} = \mathrm{M} = \{x = 0\}$. A function is written

$$
f = u + v\varepsilon, \qquad u, v : U \to \mathbb{R},
$$

on an open set $U \subseteq \mathbb{D}'$, its two components real-valued.

## The Coordinate Operators

### The Two Partial Derivatives

The algebra $\mathbb{D}'$ is $\mathbb{R}^2$ with the coordinates $(x, y)$ of $Z = x + y\varepsilon$. On smooth functions the **coordinate operators** are

$$
\partial_x = \frac{\partial}{\partial x}, \qquad \partial_y = \frac{\partial}{\partial y},
$$

acting componentwise: for $f = u + v\varepsilon$,

$$
\partial_x f = u_x + v_x \varepsilon, \qquad \partial_y f = u_y + v_y \varepsilon.
$$

Both are $\mathbb{R}$-linear derivations of the algebra of smooth functions, and they commute, $[\partial_x, \partial_y] = 0$. They are the coordinate form of the derivations of the algebra: every $\mathbb{R}$-linear derivation of $\mathbb{D}'$ is a multiple of $\partial_\varepsilon$ by *Dual-Numbers Automorphisms and Derivations*, whereas $\partial_x$ and $\partial_y$ are the derivations of the algebra of functions on the plane and are the two coordinate directions of that derivation.

### Restriction to the Submodules

The two submodules carry the two coordinate directions, and the operators restrict to them as follows.

- Along $R_{\mathbb{D}'} = \{y = 0\}$ the operator $\partial_x$ acts as the ordinary derivative $d/dx$; the restriction of $f$ to $R_{\mathbb{D}'}$ is the function $u(x, 0)$.
- Along $\varepsilon R_{\mathbb{D}'} = \{x = 0\}$ the operator $\partial_y$ acts as the ordinary derivative $d/dy$; the restriction of $f$ to $\varepsilon R_{\mathbb{D}'}$ is the function $v(0, y)\varepsilon$.
- Both coordinate operators preserve the summands, each sending the real part into the real part and the infinitesimal part into the infinitesimal part; neither mixes the two submodules, because the coordinates separate them.

The two restrictions of a function are therefore independent, and a function on the dual plane is the same datum as a pair of functions on the two lines together with the off-line values.

### The Nilpotent Component

Multiplication by $\varepsilon$ is the nilpotent endomorphism $E$ introduced above, and it commutes with every coordinate operator. Hence the operator

$$
E\,\partial_x = \varepsilon\,\partial_x
$$

is **nilpotent of index two**:

$$
(\varepsilon\,\partial_x)^2 = \varepsilon^2\,\partial_x^2 = 0,
$$

as an operator on smooth functions, because the scalar $\varepsilon^2 = 0$. The operator $\varepsilon\,\partial_x$ annihilates the real part of a function and differentiates its infinitesimal part, and it is the nilpotent component of every operator below.

## The Cauchy–Riemann Operator

### Definition and Decomposition

**Definition.** The **Cauchy–Riemann operator** of the dual algebra is

$$
\bar{\partial} = \partial_y - \varepsilon\,\partial_x.
$$

It is the sum of the real operator $\partial_y$ and the nilpotent operator $-\varepsilon\,\partial_x$:

$$
\bar{\partial} = \underbrace{\partial_y}_{\text{real part}} \;-\; \underbrace{\varepsilon\,\partial_x}_{\text{nilpotent component}}.
$$

**Proposition.** Applied to $f = u + v\varepsilon$,

$$
\bar{\partial} f = u_y + \bigl(v_y - u_x\bigr)\varepsilon.
$$

**Proof.** $\partial_y f = u_y + v_y \varepsilon$ and $\varepsilon\partial_x f = \varepsilon u_x$.

### The Regularity Equations

**Theorem.** $f = u + v\varepsilon$ is dual differentiable, that is $\bar{\partial} f = 0$, if and only if $u$ and $v$ satisfy

$$
u_y = 0, \qquad v_y = u_x.
$$

**Proof.** Both components of $\bar{\partial} f = u_y + (v_y - u_x)\varepsilon$ must vanish.

These are the dual Cauchy–Riemann equations of *Dual-Numbers Analysis*, and the theorem above is their operator form. The equation $u_y = 0$ is the vanishing of the real part of the operator, and the equation $v_y = u_x$ is the vanishing of its nilpotent component; the nilpotent component of $\bar{\partial}$ couples the two submodules, since it differentiates the real part and places the result in the infinitesimal part.

### The Nilpotent Component Is the Only Coupling

Since $\partial_y$ preserves the submodule decomposition and $\varepsilon\,\partial_x$ is the only term that moves the real part into the infinitesimal part, the equation $v_y = u_x$ is exactly the statement that the infinitesimal part of a regular function is generated from the real part. A regular function is therefore determined by its restriction to the real submodule together with one further function of one variable:

$$
f(x + y\varepsilon) = u(x) + \bigl(y\,u'(x) + c(x)\bigr)\varepsilon,
$$

where $u$ and $c$ are ordinary differentiable functions of $x$. The formula is that of *Dual-Numbers Analysis*, restated as a statement about the two submodules: the restriction of $f$ to $R_{\mathbb{D}'}$ is $u$, and the slope of its restriction to the fibre $\pi^{-1}(x)$ along the infinitesimal direction is $u'(x)$.

## The Reduction to the Real Line

### The First-Order Neighbourhood

The infinitesimal submodule $\varepsilon R_{\mathbb{D}'}$ is the **first-order neighbourhood** of the origin: it is the radical of the norm and it is square-zero, $\mathrm{M}^2 = 0$. The dual plane is the trivial square-zero extension

$$
\mathbb{D}' = \mathbb{R} \oplus \eta\,\mathbb{R}, \qquad \eta^2 = 0,
$$

in the variable $\eta = \varepsilon$, and the first-order neighbourhood of a point $x \in R_{\mathbb{D}'}$ is the fibre $x + \mathrm{M} = \{x + y\varepsilon : y \in \mathbb{R}\}$.

### The Taylor Truncation Is Exact

For a smooth function $g : \mathbb{R} \to \mathbb{R}$ the extension to the first-order neighbourhood is

$$
g(x + y\varepsilon) = g(x) + y\,g'(x)\,\varepsilon,
$$

exact because $\varepsilon^2 = 0$: the Taylor series of $g$ terminates at its first-order term. The same statement for the whole dual algebra is that the differential of $g$ is recovered from the first-order part,

$$
g'(x) = \operatorname{Inf}\bigl(g(x + \varepsilon)\bigr),
$$

so that the first-order neighbourhood of $\mathbb{R}$ is the algebraic model of the derivative.

### The Reduction

**Theorem.** A regular function $f$ on an open set $U \subseteq \mathbb{D}'$ is determined by its restriction to $U \cap R_{\mathbb{D}'}$ and the restriction of its infinitesimal part to one transversal to the infinitesimal direction, that is by two ordinary functions of one real variable.

**Proof.** By the structure formula $f(x + y\varepsilon) = u(x) + (y\,u'(x) + c(x))\varepsilon$, the pair $(u, c)$ of functions of $x$ determines $f$, and $f$ restricts to $u$ on $R_{\mathbb{D}'}$ and to $c(x)\varepsilon$ on the section $y = 0$ of the infinitesimal direction.

So the analysis of the dual algebra reduces to the analysis of the real line together with its first-order neighbourhood, and it never reduces to a pair of independent real analyses as in the split complex case below.

## Second-Order Operators and the Failure of Factorisation

### The Dual Laplacian

Define the **dual Laplacian**

$$
\Delta = \partial_x^2 + \partial_y^2, \qquad \Delta f = u_{xx} + u_{yy} + \bigl(v_{xx} + v_{yy}\bigr)\varepsilon.
$$

**Proposition.** For a regular function $f(x + y\varepsilon) = u(x) + (y\,u'(x) + c(x))\varepsilon$,

$$
\Delta f = u''(x) + \bigl(u'''(x) y + c''(x)\bigr)\varepsilon,
$$

which is not zero unless $u$ and $c$ are affine in $x$.

**Proof.** $u_{yy} = 0$ and $v = y u' + c$ has $v_{xx} = y u''' + c''$ and $v_{yy} = 0$; collecting gives the display.

So regularity does not imply harmonicity: a regular function is not harmonic unless $u$ and $c$ are affine, in contrast with the complex case, where holomorphic functions are harmonic.

### The Failure of Factorisation

In complex analysis the Laplacian factors through the two Wirtinger operators,

$$
\Delta = 4\,\frac{\partial}{\partial z}\,\frac{\partial}{\partial \bar{z}},
$$

and this factorisation is the reason holomorphic functions are harmonic. In the dual algebra the corresponding operators are $\partial_x$ and $\bar{\partial} = \partial_y - \varepsilon\partial_x$, and

$$
\partial_x \bar{\partial} = \partial_x \partial_y - \varepsilon\,\partial_x^2 = \partial_{xy} - \varepsilon\,\partial_x^2,
$$

which is not $\Delta$ in any sign, and cannot be brought into the form $\partial_{xx} + \partial_{yy}$ by any choice of the two first-order factors. The reason is the degeneracy: the two complex Wirtinger operators $\partial_z$, $\partial_{\bar z}$ are conjugates of one another and their product recovers a positive form, whereas here the conjugate of $\bar{\partial}$ in the sense of dual conjugation changes the sign of the nilpotent term only,

$$
\overline{\bar{\partial}} = \partial_y + \varepsilon\,\partial_x,
$$

and the product $\bar{\partial}\,\overline{\bar{\partial}} = \partial_y^2 - \varepsilon^2 \partial_x^2 = \partial_y^2$ has lost the real direction entirely, because $\varepsilon^2 = 0$. So there is no factorisation of $\Delta$ into dual-conjugate first-order operators and no harmonicity theorem.

### The Ellipticity Failure

The principal symbol of $\bar{\partial}$ is $\xi_y - \varepsilon\xi_x$; it vanishes on the covectors with $\xi_y = 0$ and $\varepsilon\xi_x = 0$, that is, on the whole co-normal direction of the infinitesimal line. The operator is therefore not elliptic, and it has no fundamental solution with the decay properties of the complex case. This is the operator form of the fact that the norm is degenerate: the direction of the radical is exactly the direction on which the principal symbol vanishes.

## The Role of the Maximal Ideal

The maximal ideal is the nilpotent direction of the whole analysis.

- It is the **kernel of the augmentation** $\pi(x + y\varepsilon) = x$, so it measures the failure of a dual number to be real.
- It is the **image of the nilpotent component** $\varepsilon\,\partial_x$: differentiating the real part and multiplying by $\varepsilon$ lands in the infinitesimal submodule, and the operator is nilpotent only because $\mathrm{M}^2 = 0$.
- It is the **radical of the norm**, and hence the direction on which the principal symbol of $\bar{\partial}$ vanishes and ellipticity is lost.
- It is the **first-order neighbourhood** of the origin, and hence the direction in which the Taylor series terminates at first order.

So the maximal ideal controls the operator theory, the harmonicity theory and the reduction to the real line at once, and every degeneracy of the analysis is the same algebra fact $\mathrm{M}^2 = 0$ read in a different language.

## Integration on the Submodules

### Along the Real Line

The restriction of the analysis to the real submodule is the ordinary real analysis: for $f$ with restriction $u$ to $R_{\mathbb{D}'}$,

$$
\int_a^b f(x)\,\mathrm{d}x = \int_a^b u(x)\,\mathrm{d}x,
$$

and the fundamental theorem of calculus holds on the real line. This is the ordinary real analysis carried by the subalgebra $R_{\mathbb{D}'}$.

### Along the Fibre

On a fibre $x + \mathrm{M} = \{x + y\varepsilon : y \in [0, 1]\}$ of the augmentation, the restriction of $f = u + v\varepsilon$ to the fibre is affine in $y$ when $f$ is regular, and the fibre integral is the average

$$
\int_0^1 f(x + y\varepsilon)\,\mathrm{d}y = u(x) + \Bigl(\tfrac{1}{2}u'(x) + c(x)\Bigr)\varepsilon,
$$

obtained by integrating the two summands of $f$ separately. The real part of the fibre integral is the value of $u$, and the infinitesimal part is the value of the primitive, so the two submodule restrictions integrate independently.

### The Two Submodule Integrals

The integration on the submodules is therefore the following pair: the ordinary integral on the real line, and the fibre average on the first-order neighbourhood. There is no contour integral and no area integral, because the dual plane has no non-degenerate pairing between its directions; the general integration theory, with the nilpotent direction and the relation between integration and differentiation, is in *Dual-Numbers Integration*.

## Comparison with the Split Complex Case

The split complex algebra $\mathbb{D} = \mathbb{R}[j]$, $j^2 = +1$, has the two idempotents $\pi_\pm = \tfrac{1}{2}(1 \pm j)$ and the decomposition $\mathbb{D} \cong \mathbb{R} \oplus \mathbb{R}$. Its analysis correspondingly splits into a pair of independent real analyses: the Wirtinger-type operators $\partial_{\pi_+}$ and $\partial_{\pi_-}$ act on the two components separately and the Cauchy–Riemann equation is equivalent to a pair of ordinary differential equations on two independent lines.

The dual algebra has only the idempotent $1$, so the two-component splitting is unavailable. What replaces the second component is the *first-order neighbourhood* of the first: the real submodule $R_{\mathbb{D}'}$ is the retract on which the augmentation is a ring homomorphism, and $\varepsilon R_{\mathbb{D}'}$ is the square-zero direction over it. The analysis reduces to the real line and one nilpotent direction rather than to two lines, and the Cauchy–Riemann operator couples the direction to the line through its nilpotent component instead of separating the two. The two degeneracies that follow are the ones established above: no factorisation of the Laplacian, and no ellipticity.

| | Split complex $\mathbb{D}$ | Dual $\mathbb{D}'$ |
|---|---|---|
| Idempotents | two, $\pi_\pm$ | one, $1$ |
| Decomposition | $\mathbb{R} \oplus \mathbb{R}$, two lines | $\mathbb{R} \oplus \varepsilon\mathbb{R}$, line plus first-order neighbourhood |
| First-order operators | two, one per component | $\partial_x$, $\partial_y$, coupled by $\varepsilon\partial_x$ |
| Cauchy–Riemann system | two independent real equations | $u_y = 0$, $v_y = u_x$ |
| Laplacian factorisation | yes, componentwise | no |
| Reduction of the analysis | two independent real analyses | real line plus its first-order neighbourhood |

## Summary

The dual-number algebra $\mathbb{D}'_R = R[\varepsilon]/(\varepsilon^2)$ carries exactly one nontrivial involution, dual conjugation, and hence exactly one decomposition into eigenspaces,

$$
\mathbb{D}'_R = R_{\mathbb{D}'} \oplus \varepsilon R_{\mathbb{D}'},
$$

the real and infinitesimal submodules, of $R$-rank one each. The only intersection of the two positive-dimensional submodules is $R_{\mathbb{D}'} \cap \varepsilon R_{\mathbb{D}'} = 0$, and their sum is the whole algebra; the maximal ideal $\mathrm{M} = \varepsilon R_{\mathbb{D}'}$ coincides with the infinitesimal submodule and meets the real submodule only at the origin. Multiplication by $\varepsilon$ has kernel and image both equal to $\varepsilon R_{\mathbb{D}'}$, the submodule form of $\mathrm{M}^2 = 0$; the norm restricts multiplicatively to $R_{\mathbb{D}'}$ and vanishes on $\varepsilon R_{\mathbb{D}'}$. The lattice of six subspaces that organizes the biquaternion article has no analogue here: with a single nontrivial involution there are only two submodules and the two sign patterns $(+,+)$ and $(+,-)$, so a six-subspace lattice is unavailable for structural reasons and not for lack of interest.

The differential operators of the dual algebra act on the two submodules $R_{\mathbb{D}'}$ and $\varepsilon R_{\mathbb{D}'}$ as the coordinate operators $\partial_x$ and $\partial_y$, and the Cauchy–Riemann operator $\bar{\partial} = \partial_y - \varepsilon\partial_x$ is the sum of the real operator $\partial_y$ and the nilpotent component $\varepsilon\partial_x$, nilpotent of index two because $\varepsilon^2 = 0$. Regularity is the pair of equations $u_y = 0$, $v_y = u_x$, and a regular function is determined by two ordinary functions of one variable, $f(x + y\varepsilon) = u(x) + (y\,u'(x) + c(x))\varepsilon$. The reduction of the analysis is to the real line and its first-order neighbourhood: the infinitesimal submodule is the first-order neighbourhood of the origin, and the extension of a function of one variable to it is the exact first-order Taylor truncation $g(x + y\varepsilon) = g(x) + y\,g'(x)\varepsilon$. The maximal ideal controls everything at once — it is the kernel of the augmentation, the image of the nilpotent component, the radical of the norm and the first-order neighbourhood — and every degeneracy is the single fact $\mathrm{M}^2 = 0$. Two consequences are established: the dual Laplacian does not imply harmonicity of regular functions, and it admits no factorisation into dual-conjugate first-order operators, in contrast with the complex case; and the principal symbol of $\bar{\partial}$ vanishes on the co-normal of the infinitesimal line, so the operator is not elliptic. Integration on the submodules is the ordinary integral on the real line together with the fibre average on the first-order neighbourhood. Compared with the split complex case, where the analysis splits into two independent real analyses, the dual analysis reduces to one real line and one nilpotent direction, the two components being coupled through the nilpotent component rather than separated.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}'_R = R[\varepsilon]/(\varepsilon^2)$ | Dual-number algebra over $R$; $\varepsilon^2 = 0$ |
| $\mathbb{D}' = \mathbb{D}'_{\mathbb{R}}$ | Dual-number algebra over $\mathbb{R}$ |
| $Z = a + \varepsilon b$ | General dual number, algebraic coordinates |
| $a = \operatorname{Re} Z$, $b = \operatorname{Inf} Z$ | Real and infinitesimal parts |
| $\bar{Z} = a - \varepsilon b$ | Dual conjugation, the unique nontrivial involution |
| $R_{\mathbb{D}'} = R\cdot 1$ | Real submodule, $+1$-eigenspace of $\bar{\cdot}$ |
| $\varepsilon R_{\mathbb{D}'} = \varepsilon R$ | Infinitesimal submodule, $-1$-eigenspace of $\bar{\cdot}$ |
| $\mathrm{M} = (\varepsilon)$ | Maximal ideal, equal to $\varepsilon R_{\mathbb{D}'}$ and to the first-order neighbourhood |
| $N(Z) = a^2$ | Norm, vanishes on $\varepsilon R_{\mathbb{D}'}$, radical $\mathrm{M}$ |
| $E = \varepsilon\cdot$ | Nilpotent operator, $\ker E = \operatorname{im}E = \varepsilon R_{\mathbb{D}'}$ |
| $Z = x + y\varepsilon$ | The dual variable in the analytic coordinates, $x = \operatorname{Re} Z$, $y = \operatorname{Inf} Z$ |
| $\pi(Z) = x$ | Augmentation, kernel $\mathrm{M}$ |
| $f = u + v\varepsilon$ | Function of the dual variable, $u, v$ real-valued |
| $\partial_x$, $\partial_y$ | Coordinate operators, $[\partial_x, \partial_y] = 0$ |
| $\varepsilon\,\partial_x$ | Nilpotent component, $(\varepsilon\,\partial_x)^2 = 0$ |
| $\bar{\partial} = \partial_y - \varepsilon\,\partial_x$ | Cauchy–Riemann operator |
| $\overline{\bar{\partial}} = \partial_y + \varepsilon\,\partial_x$ | Its dual conjugate |
| $\Delta = \partial_x^2 + \partial_y^2$ | Dual Laplacian, no factorisation |
| $g(x + y\varepsilon) = g(x) + y\,g'(x)\varepsilon$ | First-order Taylor truncation, exact |
| $\mathbb{D} = \mathbb{R}[j]$, $j^2 = +1$ | Split complex algebra, the comparison case |

## Further Reading

- Eduard Study, *Geometrie der Dynamen* (Teubner, Leipzig, 1903), for the decomposition of the dual-number algebra into its real and infinitesimal parts.
- I. M. Yaglom, *Complex Numbers in Geometry* (Academic Press, New York, 1968), for the submodule structure of the two-dimensional real algebras.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, Natick, 2003), for the subalgebra and ideal lattices of the low-dimensional real algebras.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, New York, 2001), for eigenspace decompositions of involutions and their relation to Peirce decompositions.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings* (Springer, Berlin, 1991), for the restriction of a quadratic form to a subspace and to its radical.
- Lars V. Ahlfors, *Complex Analysis* (McGraw-Hill, New York, 1979), for the Wirtinger operators and the factorisation of the Laplacian in the complex case.
- R. S. Hamilton, "The inverse function theorem of Nash and Moser", *Bulletin of the American Mathematical Society* **7** (1982) 65–222, for the calculus of nilpotent extensions and the first-order neighbourhood.
- Andreas Griewank and Andrea Walther, *Evaluating Derivatives* (SIAM, Philadelphia, 2008), for the operator algebra of the first-order neighbourhood over a real line.
- F. Brackx, R. Delanghe and F. Sommen, *Clifford Analysis* (Pitman, Boston, 1982), for the Cauchy–Riemann operator, regularity and the failure of harmonicity in degenerate settings.
