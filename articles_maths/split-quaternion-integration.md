
# __Split-Quaternion Integration__

## Introduction

This article treats the integration of split-quaternion-valued functions. It fixes the orientation of the vector subspace, proves integration by parts and the divergence theorem for the algebra, derives Green's formulas for the vector operator, constructs the fundamental solution, and explains what replaces the Cauchy integral formula and what fails in its place, comparing the situation with the quaternion and split-complex cases.

The split-quaternion algebra, its split-quaternion norm, its conjugation and its subspaces are assumed from *Split-Quaternion Algebra*; the Lorentzian geometry of the vector subspace, including the sign convention of the form $q_x^2-q_y^2-q_z^2$ as three-dimensional Minkowski space, from *Split-Quaternion Rotations and the Lorentz Group*, §*The Lorentz Group of Signature $(2,1)$*, and *Split-Quaternion Geometry*; the operators, the metric structure and the failure of the naive derivative from *Split-Quaternion Analysis*, and the operators of the subspaces from *Split-Quaternion Analysis*. The theory of distributions and fundamental solutions is that of *Distributions and Fundamental Solutions*, the quaternion case that of *Quaternion Integration*, and the two-dimensional hyperbolic case that of *Split-Complex Integration*. Nothing physical is invoked.

## Volume Integrals and the Orientation

**Definition.** Let $\Omega \subset \mathbb{H}_{\mathrm{s}} \cong \mathbb{R}^4$ be a domain with piecewise smooth boundary. The **volume integral** of a split-quaternion-valued function $f$ on $\Omega$ is defined componentwise in the basis $1, \vec e_x, \vec e_y, \vec e_z$:

$$
\int_\Omega f = \Big(\int_\Omega f_t\Big) + \Big(\int_\Omega f_x\Big) \vec e_x + \Big(\int_\Omega f_y\Big) \vec e_y + \Big(\int_\Omega f_z\Big) \vec e_z ,
$$

and it is the Bochner integral of a function with values in the finite-dimensional normed space with the Euclidean norm of *Split-Quaternion Analysis*, §*The Metric Structure*.

**Definition (Orientation).** The algebra $\mathbb{H}_{\mathrm{s}} \cong \mathbb{R}^4$ is oriented by the frame $(1, \vec e_x, \vec e_y, \vec e_z)$, so the volume element is $\mathrm{d}q_t\,\mathrm{d}q_x\,\mathrm{d}q_y\,\mathrm{d}q_z$. The vector subspace $V$ with the coordinates $(q_x,q_y,q_z)$ is oriented by $(\vec e_x,\vec e_y,\vec e_z)$; the form restricted to it is $q_x^2-q_y^2-q_z^2$, and this is the three-dimensional Minkowski space whose Lorentz group is $\mathrm{SO}^{+}(2,1)$ by *Split-Quaternion Rotations and the Lorentz Group*, §*The Lorentz Group of Signature $(2,1)$*. Both orientations are fixed once and for all; no factor of $i$ or of any other non-real element is introduced into any integral in this article.

**Theorem (The Boundary and the Normal).** Let $\partial\Omega$ be a piecewise smooth hypersurface with outward unit normal $(n_{q_t},n_{q_x},n_{q_y},n_{q_z})$ in the Euclidean metric of $\mathbb{R}^4$, and let

$$
n = n_{q_t} + n_{q_x} \vec e_x + n_{q_y} \vec e_y + n_{q_z} \vec e_z
$$

be the corresponding split-quaternion; it satisfies $n_{q_t}^2+n_{q_x}^2+n_{q_y}^2+n_{q_z}^2 = 1$. Then for every $f$ with continuous first derivatives on the closure,

$$
\int_\Omega \partial/\partial q_t f \;=\; \int_{\partial\Omega} f\, n_{q_t} \,\mathrm{d}\sigma, \quad \int_\Omega \partial/\partial q_x f \;=\; \int_{\partial\Omega} f\, n_{q_x} \,\mathrm{d}\sigma, \quad \int_\Omega \partial/\partial q_y f \;=\; \int_{\partial\Omega} f\, n_{q_y} \,\mathrm{d}\sigma, \quad \int_\Omega \partial/\partial q_z f \;=\; \int_{\partial\Omega} f\, n_{q_z} \,\mathrm{d}\sigma,
$$

with $\mathrm{d}\sigma$ the Euclidean surface element, and taking scalar parts and summing,

$$
\int_\Omega \operatorname{Sc}\big(D f\big) \;=\; \int_{\partial\Omega} \operatorname{Sc}\big(f\, n\big) .
$$

The normalisation is the Euclidean one, which exists on every smooth hypersurface. What degenerates on a boundary tangent to the light cone is not the normalisation but the boundary term: if $\langle n\rangle_{\natural} = 0$ at a point, then $n$ is a zero divisor there and the functional $f \mapsto \operatorname{Sc}(fn)$ has a kernel, so the boundary term loses information. The algebra-valued form $\int_\Omega Df = \int_{\partial\Omega} fn$ with the normal on the right is *not* valid as it stands; the componentwise theorem gives $\int_\Omega Df = \int_{\partial\Omega}\sum_\mu (\vec e_\mu\,f)n_\mu$, and only after taking the scalar part does the sum collapse to the single product $fn$.

**Proof.** The four displays are the divergence theorem in the four coordinates, applied to the components of $f$. For the scalar-part form, $\operatorname{Sc}(Df) = \sum_\mu\operatorname{Sc}(\vec e_\mu\,\partial/\partial q_\mu\,f)$ and $\int_\Omega\partial/\partial q_\mu\,f = \int_{\partial\Omega}f\,n_\mu$; since $\vec e_\mu$ is constant and the scalar part is linear and invariant under cyclic permutations,

$$
\int_\Omega\operatorname{Sc}(Df) = \sum_\mu\int_{\partial\Omega}\operatorname{Sc}(\vec e_\mu\,f\,n_\mu) = \sum_\mu\int_{\partial\Omega}\operatorname{Sc}(f\,n_\mu\vec e_\mu) = \int_{\partial\Omega}\operatorname{Sc}\Big(f\sum_\mu n_\mu\vec e_\mu\Big) = \int_{\partial\Omega}\operatorname{Sc}(fn),
$$

because $\sum_in_\mu\vec e_\mu = n$. If $\langle n\rangle_{\natural} = 0$ then $n$ is a zero divisor by *Split-Quaternion Zero Divisors*, §*Definition and Criterion*, so there is a nonzero $\tilde q$ with $n\tilde q = 0$ and $\operatorname{Sc}(\tilde q n) = \operatorname{Sc}(n\tilde q) = 0$; a boundary layer with constant values $\tilde q$ therefore contributes nothing to the boundary term.

## Integration by Parts and Green's Formulas

**Definition.** The **scalar product** of two functions is

$$
\langle f, g\rangle = \int_{\Omega} \operatorname{Sc}\big(f\, g^{\natural}\big),
$$

and the associated pairing is real-valued and non-degenerate in each variable pointwise.

**Theorem (The Adjoint of Left Multiplication).** For $\mu = 1,2,3$, left multiplication by $\vec e_\mu$ has adjoint left multiplication by $-\vec e_\mu$ with respect to the pointwise pairing $\operatorname{Sc}(f g^{\natural})$:

$$
\operatorname{Sc}\big((\vec e_\mu f)g^{\natural}\big) = -\operatorname{Sc}\big(f\,(\vec e_\mu g)^{\natural}\big) , \qquad \mu = 1,2,3,
$$

while for the identity generator $e_t = 1$ the same identity holds with the sign $+$.

**Proof.** The scalar part is invariant under cyclic permutations, $\operatorname{Sc}(\tilde q_1 \tilde q_2 \tilde q_3) = \operatorname{Sc}(\tilde q_2 \tilde q_3 \tilde q_1)$, since $\operatorname{Sc}$ is the trace form of the algebra; hence $\operatorname{Sc}(\vec e_\mu\,f g^{\natural}) = \operatorname{Sc}(f g^{\natural} \vec e_\mu) = \operatorname{Sc}(f\,\overline{\vec e_\mu^{\natural} g})$ because $\tilde q \mapsto \tilde{q}^{\natural}$ is an anti-automorphism. Now $\vec e_\mu^{\natural} = -\vec e_\mu$ for $\mu = 1,2,3$ and $e_t^{\natural} = e_t$, which gives the two signs; they are confirmed by evaluating both sides on the basis.

**Corollary (The Formal Adjoint of the Vector Operator).** The operator $D = \vec e_x\partial/\partial q_x + \vec e_y\partial/\partial q_y + \vec e_z\partial/\partial q_z$ is formally *self-adjoint* with respect to the scalar product $\langle f,g\rangle = \int\operatorname{Sc}(f g^{\natural})$: the two signs cancel in

$$
(\vec e_\mu\,\partial/\partial q_\mu)^* = \partial/\partial q_\mu^*\,\big(\text{left multiplication by } \vec e_\mu\big)^* = (-\partial/\partial q_\mu)(-\vec e_\mu) = \vec e_\mu\,\partial/\partial q_\mu ,
$$

so that $D^* = D$. With the boundary term retained, integration by parts gives

$$
\langle Df, g\rangle = \langle f, Dg\rangle + \int_{\partial\Omega}\operatorname{Sc}\big(f\,n\,g^{\natural}\big) .
$$

**Proof.** Integration by parts with a vanishing boundary term gives $\partial/\partial q_\mu^* = -\partial/\partial q_\mu$, and the adjoint of left multiplication by $\vec e_\mu$ is left multiplication by $-\vec e_\mu$ by the theorem, for $\mu = 1,2,3$; the product of the two signs is $+1$. The boundary term is the contribution of the boundary term in that integration by parts, its form taken from the divergence theorem of the first section.

**Theorem (Green's Formula and the Two-Sided Operator).** Let $\bar D$ be the operator that multiplies on the right,

$$
\bar D g = (\partial/\partial q_x g)\vec e_x + (\partial/\partial q_y g)\vec e_y + (\partial/\partial q_z g)\vec e_z .
$$

For $f, g$ with continuous first derivatives on the closure,

$$
\int_\Omega \Big[\operatorname{Sc}\big((Df)\,g\big) + \operatorname{Sc}\big(f\,(\bar D g)\big)\Big] = \int_{\partial\Omega} \operatorname{Sc}\big(f\, g\, n\big) .
$$

Two features of the algebra are responsible for the form of this formula, and both are statements that are true for scalar-valued functions and false in general.

1. The operators $D$ and $\bar D$ agree on functions with values in a commutative subalgebra, and in particular on scalar-valued functions, but they differ in general:
$$
\bar Dg - Dg = \sum_\mu\big((\partial/\partial q_\mu\,g)\vec e_\mu - \vec e_\mu(\partial/\partial q_\mu\,g)\big) ,
$$
a sum of commutators, which vanishes exactly when the values of $g$ commute with the generators.
2. The two-term Leibniz rule is false. One has
$$
D(fg) = (Df)g + \sum_\mu \vec e_\mu f\,(\partial/\partial q_\mu g), \qquad \sum_\mu \vec e_\mu f\,(\partial/\partial q_\mu\,g) - f(Dg) = \sum_\mu [\vec e_\mu,f]\,\partial/\partial q_\mu\,g ,
$$
so that $D(fg) = (Df)g + f(Dg)$ holds exactly when $f$ is central; the failure is visible on $f = \vec e_x$, $g = \vec e_y$ at $\mu = 2$, where $\vec e_y(\vec e_x \vec e_y) = -\vec e_x$ while $(\vec e_y \vec e_x)\vec e_y + \vec e_x(\vec e_y \vec e_y) = 0$. What does survive without centrality is the scalar-part statement displayed above, because the scalar part is invariant under cyclic permutations: $\operatorname{Sc}(\vec e_\mu\,f\,\partial/\partial q_\mu\,g) = \operatorname{Sc}(f\,\partial/\partial q_\mu\,g\,\vec e_\mu)$.

**Proof.** Apply the scalar-part divergence theorem of the first section to the algebra-valued function $fg$:

$$
\int_\Omega\operatorname{Sc}\big(D(fg)\big) = \int_{\partial\Omega}\operatorname{Sc}\big(fgn\big).
$$

Now $D(fg) = \sum_\mu\vec e_\mu\big[(\partial/\partial q_\mu\,f)g + f(\partial/\partial q_\mu\,g)\big]$, whose scalar part is $\operatorname{Sc}((Df)g) + \sum_\mu\operatorname{Sc}(\vec e_\mu\,f\,\partial/\partial q_\mu\,g)$. By the cyclic invariance of the scalar part, $\operatorname{Sc}(\vec e_\mu\,f\,\partial/\partial q_\mu\,g) = \operatorname{Sc}(f\,\partial/\partial q_\mu\,g \vec e_\mu) = \operatorname{Sc}(f(\bar Dg))$, and the display follows. The failure of the two-term Leibniz rule is the computation on the stated generators, and the sum-of-commutators form of the difference is immediate.

**Corollary (The Classical Green Identities).** If $g$ is scalar-valued then $\bar Dg = Dg$ and

$$
\int_\Omega\big[\operatorname{Sc}((Df)g) + \operatorname{Sc}(f(Dg))\big] = \int_{\partial\Omega}\operatorname{Sc}(fgn) .
$$

In particular, for scalar-valued $u$ and $v$,

$$
\int_\Omega\big(u\,\Box_{(2,1)} v - v\,\Box_{(2,1)} u\big) = \int_{\partial\Omega}\big(u\,\partial/\partial n v - v\,\partial/\partial n u\big), \qquad \partial/\partial n u = -n_{q_x}\partial/\partial q_x\,u + n_{q_y}\partial/\partial q_y\,u + n_{q_z}\partial/\partial q_z\,u = \operatorname{Sc}(nDu),
$$

the classical Green identity for the wave operator, with the normal derivative carrying the signs of the form.

**Proof.** For scalar-valued $g$ each $\partial/\partial q_\mu\,g$ is scalar and commutes with the generators, so the two operators agree and the first display is the theorem. For the second, apply the first display to the pair $(Du, v)$ and to the pair $(Dv, u)$ with scalar $u, v$, and subtract: the mixed terms are $\operatorname{Sc}((Du)(Dv))$ and $\operatorname{Sc}((Dv)(Du))$, which are equal by the symmetry $\operatorname{Sc}(\tilde q_1 \tilde q_2) = \operatorname{Sc}(\tilde q_2\tilde q_1)$ of the scalar part and therefore cancel, while $\operatorname{Sc}((\Box u)v) = v\,\Box u$ because $v$ is scalar. The boundary terms are

$$
\int_{\partial\Omega}\operatorname{Sc}(Du\,v\,n) - \int_{\partial\Omega}\operatorname{Sc}(Dv\,u\,n) = \int_{\partial\Omega}\big(v\operatorname{Sc}(nDu) - u\operatorname{Sc}(nDv)\big),
$$

which is the display because $\operatorname{Sc}(nDu) = -n_{q_x}\partial/\partial q_x\,u + n_{q_y}\partial/\partial q_y\,u + n_{q_z}\partial/\partial q_z\,u = \partial/\partial n\,u$; the scalar part of $nD$ is the conormal operator of the form $-\partial^2/\partial q_x^2+\partial^2/\partial q_y^2+\partial^2/\partial q_z^2$, the signs being those of the form, not of the Euclidean gradient.

## The Divergence Theorem and the Stokes Theorem

**Theorem (Divergence and Stokes for the Algebra).** For a split-quaternion-valued function $F = F_t + F_x\vec e_x + F_y\vec e_y + F_z\vec e_z$ with continuous first derivatives,

$$
\int_\Omega \Big(\frac{\partial F_t}{\partial q_t} + \frac{\partial F_x}{\partial q_x} + \frac{\partial F_y}{\partial q_y} + \frac{\partial F_z}{\partial q_z}\Big) = \int_{\partial\Omega} \big(F_t n_{q_t} + F_x n_{q_x} + F_y n_{q_y} + F_z n_{q_z}\big),
$$

and the Stokes theorem holds for the three-form of the vector subspace with the orientation fixed above.

**Proof.** The divergence theorem is applied to each coordinate component, and the Stokes theorem is the usual one for the oriented three-dimensional vector subspace.

**Corollary (The Role of the Null Boundary).** On a hypersurface containing a characteristic direction, the boundary term of Green's formula degenerates along that direction: the normal vector is a zero divisor, its product with the boundary values annihilates a part of the algebra, and the boundary integral loses information.

**Proof.** If $n$ is null then $n^2 = 0$ and $n$ is a zero divisor by *Split-Quaternion Zero Divisors*, §*Nonzero Nilpotents*; the products $fng$ depend on $f$ and $g$ only through the components that do not annihilate $n$.

## The Fundamental Solution

**Theorem (Fundamental Solution of the Wave Operator).** The operator $\Box_{(2,1)} = -\partial^2/\partial q_x^2 + \partial^2/\partial q_y^2 + \partial^2/\partial q_z^2$ has a fundamental solution $E$ in the vector subspace, a distribution supported in the closed future cone

$$
C = \{(q_x,q_y,q_z) : q_x \geq 0, \ q_x^2 \geq q_y^2 + q_z^2\},
$$

whose singular support is the light cone $\partial C$, and which is homogeneous of degree $-1$. The solution has support in the solid cone, not only on its boundary: the sharp Huygens principle fails, as it does for every wave operator in two spatial dimensions, and the tail is the interior part of the cone.

**Proof.** The construction of the fundamental solution of a wave operator is that of *Distributions and Fundamental Solutions*, where the support and the homogeneity are established; the boundary behaviour is the statement that the fundamental solution is singular precisely on the characteristic cone, and the failure of the sharp Huygens principle in two spatial dimensions is the standard count of dimensions.

**Theorem (Fundamental Solution of the Vector Operator).** The vector operator $D$ has a fundamental solution

$$
E_D = D E ,
$$

the distribution obtained by applying $D$ to the fundamental solution of the wave operator; it satisfies $D E_D = \delta$ because $D^2 = \Box_{(2,1)}$. Its singular support is the light cone, so the propagation governed by $D$ is at speed one, in contrast with the elliptic case, where the singular support of the fundamental solution is a single point. Both $E$ and $E_D$ depend on the vector coordinates $(q_x,q_y,q_z)$ alone and are independent of the scalar coordinate $q_t$; $E$ is homogeneous of degree $-1$ and $E_D = DE$ of degree $-2$ in those three variables, and the $\delta$ in the two equations is the delta distribution of the vector subspace.

**Proof.** $D(D E) = D^2E = \Box_{(2,1)}E = \delta$; the singular support is contained in that of $E$ and is not smaller because $E_D$ is not smooth across the cone. The elliptic comparison is the fundamental solution of the Laplacian in *Clifford Analysis*.

## The Cauchy Integral Formula and Its Failure

### The Kernel of the Vector Operator

**Theorem (The Kernel of the Vector Operator).** The kernel of $D$ is large. For every smooth scalar function $h$ of one variable,

$$
D\big(\tilde\pi_1\, h(q_x-q_z)\big) = 0 \qquad\text{and}\qquad D\big(h(q_x+q_z)\,\tilde\pi_2\big) = 0 ,
$$

with $\tilde\pi_{1,2} = \tfrac12(1\pm \vec e_y)$ the idempotents. Both families contain nonzero compactly supported functions: $\tilde\pi_1\chi(q_x-q_z)$ with $\chi$ a smooth bump vanishes outside a strip and is not zero.

**Proof.** The products of a generator with an idempotent are

$$
\vec e_x\tilde\pi_1 = \vec e_z\tilde\pi_1 = \tfrac12(\vec e_x+\vec e_z), \qquad \vec e_y\tilde\pi_1 = \tilde\pi_1, \qquad \vec e_x\tilde\pi_2 = -\vec e_z\tilde\pi_2 = \tfrac12(\vec e_x-\vec e_z), \qquad \vec e_y\tilde\pi_2 = -\tilde\pi_2 ,
$$

so for a scalar function $h$

$$
D(\tilde\pi_1h) = \tfrac12(\vec e_x+\vec e_z)\big(\partial/\partial q_x\,h+\partial/\partial q_z\,h\big) + \tilde\pi_1\,\partial/\partial q_y\,h, \qquad D(h\tilde\pi_2) = \tfrac12(\vec e_x-\vec e_z)\big(\partial/\partial q_x\,h-\partial/\partial q_z\,h\big) - \tilde\pi_2\,\partial/\partial q_y\,h ,
$$

and both right-hand sides vanish for the stated $h$, since $\partial/\partial q_y\,h = 0$ and $\partial/\partial q_x\,h = \mp\partial/\partial q_z\,h$ for $h = h(q_x\mp q_z)$. The four elements $\tilde\pi_1$, $\tilde\pi_2$, $\tfrac12(\vec e_x+\vec e_z)$, $\tfrac12(\vec e_x-\vec e_z)$ occurring here are a basis of the algebra, so the two identities are read off the multiplication table and are exact.

**Corollary (Consequences of the Kernel).** No unique continuation, no identity theorem, no maximum principle and no Liouville theorem hold for the solutions of $Df = 0$: the function $\tilde\pi_1\chi(q_x-q_z)$ with $\chi$ supported in $[1,2]$ is a nonzero solution vanishing on the open half-space $q_x-q_z<1$, so the zero set of a nonzero solution can have interior points and no rigidity of the elliptic type survives.

**Corollary (No Right Inverse).** There is no identity $f = E_D*(Df)$ valid for all compactly supported smooth $f$, and therefore no Cauchy–Pompeiu formula of the elliptic type: the identity would give $f = E_D*0 = 0$ for the nonzero compactly supported solutions of the kernel theorem.

**Theorem (The Inversion on the Left).** What holds is the inversion on the left,

$$
f = D\,(E_D * f),
$$

for every $f$ with compact support, so that $E_D*f$ is a solution of the inhomogeneous equation $Dg = f$ for every datum $f$, while the homogeneous solutions are as numerous as the kernel theorem says.

**Proof.** $D(E_D*f) = (DE_D)*f = \delta*f = f$, the differentiation passing through the convolution because the coefficients are constant.

**Remark (What Fails in Place of the Cauchy Formula).** Three structural features of the quaternionic Cauchy integral formula are absent here. First the kernel: $(\tilde q_1-\tilde q_2)^{-1}$ has no counterpart, since $\tilde q_1-\tilde q_2$ is a zero divisor exactly when it is null, so its reciprocal does not exist on the light cone and the singular set of the available kernel is a three-dimensional cone through the point rather than the point itself. Second analyticity: the solutions of $Df = 0$ satisfy a first-order system whose characteristic variety is the light cone, and by the kernel theorem they include nonzero compactly supported functions, so they are not analytic and carry no identity theorem. Third inversion: the inversion available is one-sided, by the theorem above, and the boundary formula of Green is valued in the trace pairing, so the boundary data do not pass to the interior values through a single multiplication kernel.

## Principal Values and the Distributional Inverse

The singularities of the inverse on the null cone are treated distributionally, exactly as in the theory of the wave operator.

**Theorem (The Principal Value of the Inverse).** The locally integrable function $1/\langle\tilde q\rangle_{\natural}$ on the algebra, and the distribution $\tilde q^{-1} = \tilde{q}^{\natural}/\langle\tilde q\rangle_{\natural}$ on the vector subspace, have well-defined principal values: for a test function $\varphi$,

$$
\Big\langle \mathrm{pv}\frac{1}{N},\, \varphi\Big\rangle = \lim_{\varepsilon\to0}\int_{|\langle\tilde q\rangle_{\natural}|>\varepsilon}\frac{\varphi(\tilde q)}{\langle\tilde q\rangle_{\natural}}\,\mathrm{d}\tilde q ,
$$

and the limit exists because the level sets of $\langle\cdot\rangle_{\natural}$ have finite area and the singularity is odd with respect to $\tilde q \mapsto -\tilde q$ after symmetrisation. Off the null cone the reciprocal is an ordinary function and $\langle\tilde q\rangle_{\natural}\cdot(1/\langle\tilde q\rangle_{\natural}) = 1$ identically, so the difference

$$
\langle\tilde q\rangle_{\natural}\cdot \mathrm{pv}\frac{1}{\langle\tilde q\rangle_{\natural}} \;-\; 1
$$

is a distribution of degree zero supported on the null cone; in the standard regularisations it is a multiple of $\delta$, with a factor that depends on the normalisation of the cone.

**Proof.** The convergence of the principal value is the homogeneity of $\langle\cdot\rangle_{\natural}$ of degree two and the oddness of the integrand about the origin; the support statement follows because the two sides agree off the null cone, and the identification of the correction with a multiple of $\delta$ in the standard regularisations is the computation of *Distributions and Fundamental Solutions*.

**Corollary (The Transfer to the Fundamental Solution).** The transform of the fundamental solution of the vector operator involves exactly this principal value, by the corollary of *Split-Quaternion Harmonic Analysis*, §*The Algebra-Valued Transform and the Vanishing Determinant*, where the formula $\mathcal F E_D = \xi/(2\pi\mathrm{i}\langle \xi\rangle_{\natural})$ is displayed; the factor $1/\langle \xi\rangle_{\natural}$ must be read as the principal value, and the correction supported on the cone is the distributional content of the cone support of $E_D$.

**Proof.** Combine the displayed transform with the definition of the principal value above.

## Comparison with the Quaternion and Split-Complex Cases

| | $\mathbb{H}$ | $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{D}$ |
|---|---|---|---|
| operator | Cauchy–Riemann, elliptic | wave operator, hyperbolic | wave operator in one variable |
| fundamental solution | Poisson kernel, singular at a point | distribution supported on the cone | supported on the two characteristic lines |
| Cauchy integral formula | holds | fails; replaced by the one-sided inversion $f = D(E_D*f)$ | fails; replaced by d'Alembert |
| Green's formula | holds, with the elliptic boundary term | holds on non-characteristic boundaries | holds |
| compactly supported solutions of the monogenic equation | none, by Liouville | many: the kernel of $D$ is large | many, by the same zero-divisor mechanism |
| singularities of solutions | off a point, removable | on characteristic surfaces | on characteristic lines |

The quaternion column is the content of *Quaternion Integration* and the split-complex column that of *Split-Complex Integration*. The single cause of the difference is again the indefiniteness of the form, equivalently the presence of the zero divisors: the characteristic cone of the operator is the zero divisor set, and the fundamental solution must be singular along it. The eight-dimensional relative $\mathbb{H}_{\mathbb{D}}$ is a later system of Part V, treated under Split-Biquaternions, and nothing of it is used here.

## Summary

The integration of split-quaternion-valued functions is componentwise, with the orientation of the algebra fixed by the frame $(1,\vec e_x,\vec e_y,\vec e_z)$ and the orientation of the vector subspace by $(\vec e_x,\vec e_y,\vec e_z)$, the form $q_x^2-q_y^2-q_z^2$ being the three-dimensional Minkowski form of the system. The divergence theorem holds on every domain with piecewise smooth boundary, with the Euclidean normal; on a boundary tangent to the light cone the normal is a zero divisor and the boundary term degenerates.

The vector operator is formally self-adjoint, $D^* = D$, and Green's formula reads $\int_\Omega[\operatorname{Sc}((Df)g) + \operatorname{Sc}(f(\bar Dg))] = \int_{\partial\Omega}\operatorname{Sc}(fgn)$, with the classical Green identities for the wave operator as corollaries; the two-sided form is forced by the failure of the two-term Leibniz rule in the non-commutative algebra. The wave operator $\Box_{(2,1)} = D^2$ has a fundamental solution supported in the closed future cone with singular support the light cone, and the vector operator has the fundamental solution $D E$; the propagation is at speed one, and the sharp Huygens principle fails, as in every two-spatial-dimensional wave problem.

There is no Cauchy integral formula: the candidate kernel $(\tilde q-\tilde p)^{-1}$ does not exist on the light cone, where the difference of two points is a zero divisor. The inversion that holds is one-sided, $f = D(E_D*f)$; the formula $f = E_D*(Df)$ of the elliptic theory fails, as the large kernel of $D$ shows, and the maximum principle, the mean value property, the identity theorem and the elliptic Liouville and removable-singularity theorems all fail. The quaternion case, with its elliptic operator and its point singularity, is the opposite extreme, and the differences are all traced to the indefiniteness of the form and the presence of the zero divisors. The eight-dimensional relative is a later system of Part V, named only.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\int_\Omega f$ | the componentwise volume integral | this article |
| $(1,\vec e_x,\vec e_y,\vec e_z)$, $(\vec e_x,\vec e_y,\vec e_z)$ | the orientations of the algebra and of the vector subspace | this article |
| $(q_x,q_y,q_z)$ with $q_x^2-q_y^2-q_z^2$ | the three-dimensional Minkowski space of the system | *Split-Quaternion Rotations and the Lorentz Group* |
| $n$ | the Euclidean unit normal, read as a split-quaternion | this article |
| $D^* = D$ | the formal adjoint of the vector operator | this article |
| $\bar D = \partial/\partial q_x \vec e_x + \partial/\partial q_y \vec e_y + \partial/\partial q_z \vec e_z$ | the operator acting on the right | this article |
| $\int[\operatorname{Sc}((Df)g) + \operatorname{Sc}(f(\bar Dg))] = \int\operatorname{Sc}(fgn)$ | Green's formula | this article |
| $E$ | the fundamental solution of $\Box_{(2,1)}$, supported on the cone | *Distributions and Fundamental Solutions* |
| $E_D = DE$ | the fundamental solution of $D$ | this article |
| $f = D(E_D*f)$ | the inversion on the left | this article |
| $\tilde\pi_1h(q_x-q_z)$, $h(q_x+q_z)\tilde\pi_2$ | the two families in the kernel of $D$ | this article |
| $C$, $\partial C$ | the future cone and the light cone | *Split-Quaternion Geometry* |

## Further Reading

- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I* (Springer, 1990), for the characteristic variety of a first-order operator, the propagation of singularities and the absence of a reproducing kernel in the hyperbolic case.
- Fritz John, *Partial Differential Equations*, 4th ed. (Springer, 1991), for the wave equation, its fundamental solution and the failure of the sharp Huygens principle in two spatial dimensions.
- Robert P. Gilbert and James L. Buchanan, *First Order Elliptic Systems: A Function Theoretic Approach* (Academic Press, 1983), for the elliptic comparison and the Cauchy integral formula that the hyperbolic case lacks.
- Ricardo Estrada and Ram P. Kanwal, *A Distributional Approach to Asymptotics* (Birkhäuser, 2002), for the homogeneous distributions supported on cones and their use as fundamental solutions.
