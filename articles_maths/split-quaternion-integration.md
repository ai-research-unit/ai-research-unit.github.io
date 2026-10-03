
# __Split-Quaternion Integration__

## Introduction

This article treats the integration of split-quaternion-valued functions. It fixes the orientation of the vector subspace, proves integration by parts and the divergence theorem for the algebra, derives Green's formulas for the vector operator, constructs the fundamental solution, and explains what replaces the Cauchy integral formula and what fails in its place, comparing the situation with the quaternion and split-complex cases.

The split-quaternion algebra, its split-quaternion norm, its conjugation and its subspaces are assumed from *Split-Quaternion Algebra*; the Lorentzian geometry of the vector subspace, including the sign convention of the form $q_1^2-q_2^2-q_3^2$ as three-dimensional Minkowski space, from *Split-Quaternion Rotations and the Lorentz Group*, §*The Lorentz Group of Signature $(2,1)$*, and *Split-Quaternion Geometry*; the operators, the metric structure and the failure of the naive derivative from *Split-Quaternion Analysis*, and the operators of the subspaces from *Split-Quaternion Analysis*. The theory of distributions and fundamental solutions is that of *Distributions and Fundamental Solutions*, the quaternion case that of *Quaternion Integration*, and the two-dimensional hyperbolic case that of *Split-Complex Integration*. Nothing physical is invoked.

## Volume Integrals and the Orientation

**Definition.** Let $\Omega \subset \mathbb{H}_{\mathrm{s}} \cong \mathbb{R}^4$ be a domain with piecewise smooth boundary. The **volume integral** of a split-quaternion-valued function $f$ on $\Omega$ is defined componentwise in the basis $1, e_1, e_2, e_3$:

$$
\int_\Omega f = \Big(\int_\Omega f_0\Big) + \Big(\int_\Omega f_1\Big) e_1 + \Big(\int_\Omega f_2\Big) e_2 + \Big(\int_\Omega f_3\Big) e_3 ,
$$

and it is the Bochner integral of a function with values in the finite-dimensional normed space with the Euclidean norm of *Split-Quaternion Analysis*, §*The Metric Structure*.

**Definition (Orientation).** The algebra $\mathbb{H}_{\mathrm{s}} \cong \mathbb{R}^4$ is oriented by the frame $(1, e_1, e_2, e_3)$, so the volume element is $\mathrm{d}q_0\,\mathrm{d}q_1\,\mathrm{d}q_2\,\mathrm{d}q_3$. The vector subspace $V$ with the coordinates $(q_1,q_2,q_3)$ is oriented by $(e_1,e_2,e_3)$; the form restricted to it is $q_1^2-q_2^2-q_3^2$, and this is the three-dimensional Minkowski space whose Lorentz group is $\mathrm{SO}^{+}(2,1)$ by *Split-Quaternion Rotations and the Lorentz Group*, §*The Lorentz Group of Signature $(2,1)$*. Both orientations are fixed once and for all; no factor of $i$ or of any other non-real element is introduced into any integral in this article.

**Theorem (The Boundary and the Normal).** Let $\partial\Omega$ be a piecewise smooth hypersurface with outward unit normal $(n_{q_0},n_{q_1},n_{q_2},n_{q_3})$ in the Euclidean metric of $\mathbb{R}^4$, and let

$$
n = n_{q_0} + n_{q_1} e_1 + n_{q_2} e_2 + n_{q_3} e_3
$$

be the corresponding split-quaternion; it satisfies $n_{q_0}^2+n_{q_1}^2+n_{q_2}^2+n_{q_3}^2 = 1$. Then for every $f$ with continuous first derivatives on the closure,

$$
\int_\Omega \partial_{q_0} f \;=\; \int_{\partial\Omega} f\, n_{q_0} \,\mathrm{d}\sigma, \quad \int_\Omega \partial_{q_1} f \;=\; \int_{\partial\Omega} f\, n_{q_1} \,\mathrm{d}\sigma, \quad \int_\Omega \partial_{q_2} f \;=\; \int_{\partial\Omega} f\, n_{q_2} \,\mathrm{d}\sigma, \quad \int_\Omega \partial_{q_3} f \;=\; \int_{\partial\Omega} f\, n_{q_3} \,\mathrm{d}\sigma,
$$

with $\mathrm{d}\sigma$ the Euclidean surface element, and taking scalar parts and summing,

$$
\int_\Omega \operatorname{Sc}\big(D f\big) \;=\; \int_{\partial\Omega} \operatorname{Sc}\big(f\, n\big) .
$$

The normalisation is the Euclidean one, which exists on every smooth hypersurface. What degenerates on a boundary tangent to the light cone is not the normalisation but the boundary term: if $N(n) = 0$ at a point, then $n$ is a zero divisor there and the functional $f \mapsto \operatorname{Sc}(fn)$ has a kernel, so the boundary term loses information. The algebra-valued form $\int_\Omega Df = \int_{\partial\Omega} fn$ with the normal on the right is *not* valid as it stands; the componentwise theorem gives $\int_\Omega Df = \int_{\partial\Omega}\sum_i (e_if)n_i$, and only after taking the scalar part does the sum collapse to the single product $fn$.

**Proof.** The four displays are the divergence theorem in the four coordinates, applied to the components of $f$. For the scalar-part form, $\operatorname{Sc}(Df) = \sum_i\operatorname{Sc}(e_i\partial_if)$ and $\int_\Omega\partial_if = \int_{\partial\Omega}fn_i$; since $e_i$ is constant and the scalar part is linear and invariant under cyclic permutations,

$$
\int_\Omega\operatorname{Sc}(Df) = \sum_i\int_{\partial\Omega}\operatorname{Sc}(e_ifn_i) = \sum_i\int_{\partial\Omega}\operatorname{Sc}(fn_ie_i) = \int_{\partial\Omega}\operatorname{Sc}\Big(f\sum_i n_ie_i\Big) = \int_{\partial\Omega}\operatorname{Sc}(fn),
$$

because $\sum_in_ie_i = n$. If $N(n) = 0$ then $n$ is a zero divisor by *Split-Quaternion Zero Divisors*, §*The Null Cone and the Maximal Isotropic Subspaces*, so there is a nonzero $\tilde p$ with $n\tilde p = 0$ and $\operatorname{Sc}(\tilde p n) = \operatorname{Sc}(n\tilde p) = 0$; a boundary layer with constant values $\tilde p$ therefore contributes nothing to the boundary term.

## Integration by Parts and Green's Formulas

**Definition.** The **scalar product** of two functions is

$$
\langle f, g\rangle = \int_{\Omega} \operatorname{Sc}\big(f\, g^{\natural}\big),
$$

and the associated pairing is real-valued and non-degenerate in each variable pointwise.

**Theorem (The Adjoint of Left Multiplication).** For $i = 1,2,3$, left multiplication by $e_i$ has adjoint left multiplication by $-e_i$ with respect to the pointwise pairing $\operatorname{Sc}(f g^{\natural})$:

$$
\operatorname{Sc}\big((e_i f)g^{\natural}\big) = -\operatorname{Sc}\big(f\,(e_i g)^{\natural}\big) , \qquad i = 1,2,3,
$$

while for the identity generator $e_0 = 1$ the same identity holds with the sign $+$.

**Proof.** The scalar part is invariant under cyclic permutations, $\operatorname{Sc}(\tilde q \tilde p \tilde r) = \operatorname{Sc}(\tilde p \tilde r \tilde q)$, since $\operatorname{Sc}$ is the trace form of the algebra; hence $\operatorname{Sc}(e_if g^{\natural}) = \operatorname{Sc}(f g^{\natural} e_i) = \operatorname{Sc}(f\,\overline{e_i^{\natural} g})$ because $\tilde q \mapsto \tilde{q}^{\natural}$ is an anti-automorphism. Now $e_i^{\natural} = -e_i$ for $i = 1,2,3$ and $e_0^{\natural} = e_0$, which gives the two signs; they are confirmed by evaluating both sides on the basis.

**Corollary (The Formal Adjoint of the Vector Operator).** The operator $D = e_1\partial_{q_1} + e_2\partial_{q_2} + e_3\partial_{q_3}$ is formally *self-adjoint* with respect to the scalar product $\langle f,g\rangle = \int\operatorname{Sc}(f g^{\natural})$: the two signs cancel in

$$
(e_i\partial_i)^* = \partial_i^*\,\big(\text{left multiplication by } e_i\big)^* = (-\partial_i)(-e_i) = e_i\partial_i ,
$$

so that $D^* = D$. With the boundary term retained, integration by parts gives

$$
\langle Df, g\rangle = \langle f, Dg\rangle + \int_{\partial\Omega}\operatorname{Sc}\big(f\,n\,g^{\natural}\big) .
$$

**Proof.** Integration by parts with a vanishing boundary term gives $\partial_i^* = -\partial_i$, and the adjoint of left multiplication by $e_i$ is left multiplication by $-e_i$ by the theorem, for $i = 1,2,3$; the product of the two signs is $+1$. The boundary term is the contribution of the boundary term in that integration by parts, its form taken from the divergence theorem of the first section.

**Theorem (Green's Formula and the Two-Sided Operator).** Let $\bar D$ be the operator that multiplies on the right,

$$
\bar D g = (\partial_{q_1} g)e_1 + (\partial_{q_2} g)e_2 + (\partial_{q_3} g)e_3 .
$$

For $f, g$ with continuous first derivatives on the closure,

$$
\int_\Omega \Big[\operatorname{Sc}\big((Df)\,g\big) + \operatorname{Sc}\big(f\,(\bar D g)\big)\Big] = \int_{\partial\Omega} \operatorname{Sc}\big(f\, g\, n\big) .
$$

Two features of the algebra are responsible for the form of this formula, and both are statements that are true for scalar-valued functions and false in general.

1. The operators $D$ and $\bar D$ agree on functions with values in a commutative subalgebra, and in particular on scalar-valued functions, but they differ in general:
$$
\bar Dg - Dg = \sum_i\big((\partial_ig)e_i - e_i(\partial_ig)\big) ,
$$
a sum of commutators, which vanishes exactly when the values of $g$ commute with the generators.
2. The two-term Leibniz rule is false. One has
$$
D(fg) = (Df)g + \sum_i e_i f\,(\partial_i g), \qquad \sum_i e_i f\,(\partial_ig) - f(Dg) = \sum_i [e_i,f]\,\partial_ig ,
$$
so that $D(fg) = (Df)g + f(Dg)$ holds exactly when $f$ is central; the failure is visible on $f = e_1$, $g = e_2$ at $i = 2$, where $e_2(e_1e_2) = -e_1$ while $(e_2e_1)e_2 + e_1(e_2e_2) = 0$. What does survive without centrality is the scalar-part statement displayed above, because the scalar part is invariant under cyclic permutations: $\operatorname{Sc}(e_if\,\partial_ig) = \operatorname{Sc}(f\,\partial_ig\,e_i)$.

**Proof.** Apply the scalar-part divergence theorem of the first section to the algebra-valued function $fg$:

$$
\int_\Omega\operatorname{Sc}\big(D(fg)\big) = \int_{\partial\Omega}\operatorname{Sc}\big(fgn\big).
$$

Now $D(fg) = \sum_ie_i\big[(\partial_if)g + f(\partial_ig)\big]$, whose scalar part is $\operatorname{Sc}((Df)g) + \sum_i\operatorname{Sc}(e_if\partial_ig)$. By the cyclic invariance of the scalar part, $\operatorname{Sc}(e_if\partial_ig) = \operatorname{Sc}(f\partial_ig e_i) = \operatorname{Sc}(f(\bar Dg))$, and the display follows. The failure of the two-term Leibniz rule is the computation on the stated generators, and the sum-of-commutators form of the difference is immediate.

**Corollary (The Classical Green Identities).** If $g$ is scalar-valued then $\bar Dg = Dg$ and

$$
\int_\Omega\big[\operatorname{Sc}((Df)g) + \operatorname{Sc}(f(Dg))\big] = \int_{\partial\Omega}\operatorname{Sc}(fgn) .
$$

In particular, for scalar-valued $u$ and $v$,

$$
\int_\Omega\big(u\,\Box_{(2,1)} v - v\,\Box_{(2,1)} u\big) = \int_{\partial\Omega}\big(u\,\partial_n v - v\,\partial_n u\big), \qquad \partial_n u = -n_{q_1}\partial_{q_1}u + n_{q_2}\partial_{q_2}u + n_{q_3}\partial_{q_3}u = \operatorname{Sc}(nDu),
$$

the classical Green identity for the wave operator, with the normal derivative carrying the signs of the form.

**Proof.** For scalar-valued $g$ each $\partial_ig$ is scalar and commutes with the generators, so the two operators agree and the first display is the theorem. For the second, apply the first display to the pair $(Du, v)$ and to the pair $(Dv, u)$ with scalar $u, v$, and subtract: the mixed terms are $\operatorname{Sc}((Du)(Dv))$ and $\operatorname{Sc}((Dv)(Du))$, which are equal by the symmetry $\operatorname{Sc}(\tilde q \tilde p) = \operatorname{Sc}(\tilde p\tilde q)$ of the scalar part and therefore cancel, while $\operatorname{Sc}((\Box u)v) = v\,\Box u$ because $v$ is scalar. The boundary terms are

$$
\int_{\partial\Omega}\operatorname{Sc}(Du\,v\,n) - \int_{\partial\Omega}\operatorname{Sc}(Dv\,u\,n) = \int_{\partial\Omega}\big(v\operatorname{Sc}(nDu) - u\operatorname{Sc}(nDv)\big),
$$

which is the display because $\operatorname{Sc}(nDu) = -n_{q_1}\partial_{q_1}u + n_{q_2}\partial_{q_2}u + n_{q_3}\partial_{q_3}u = \partial_nu$; the scalar part of $nD$ is the conormal operator of the form $-\partial_{q_1}^2+\partial_{q_2}^2+\partial_{q_3}^2$, the signs being those of the form, not of the Euclidean gradient.

## The Divergence Theorem and the Stokes Theorem

**Theorem (Divergence and Stokes for the Algebra).** For a split-quaternion-valued function $F = F_0 + F_1e_1 + F_2e_2 + F_3e_3$ with continuous first derivatives,

$$
\int_\Omega \Big(\frac{\partial F_0}{\partial q_0} + \frac{\partial F_1}{\partial q_1} + \frac{\partial F_2}{\partial q_2} + \frac{\partial F_3}{\partial q_3}\Big) = \int_{\partial\Omega} \big(F_0 n_{q_0} + F_1 n_{q_1} + F_2 n_{q_2} + F_3 n_{q_3}\big),
$$

and the Stokes theorem holds for the three-form of the vector subspace with the orientation fixed above.

**Proof.** The divergence theorem is applied to each coordinate component, and the Stokes theorem is the usual one for the oriented three-dimensional vector subspace.

**Corollary (The Role of the Null Boundary).** On a hypersurface containing a characteristic direction, the boundary term of Green's formula degenerates along that direction: the normal vector is a zero divisor, its product with the boundary values annihilates a part of the algebra, and the boundary integral loses information.

**Proof.** If $n$ is null then $n^2 = 0$ and $n$ is a zero divisor by *Split-Quaternion Zero Divisors*, §*The Null Cone and the Maximal Isotropic Subspaces*; the products $fng$ depend on $f$ and $g$ only through the components that do not annihilate $n$.

## The Fundamental Solution

**Theorem (Fundamental Solution of the Wave Operator).** The operator $\Box_{(2,1)} = -\partial_{q_1}^2 + \partial_{q_2}^2 + \partial_{q_3}^2$ has a fundamental solution $E$ in the vector subspace, a distribution supported in the closed future cone

$$
C = \{(q_1,q_2,q_3) : q_1 \geq 0, \ q_1^2 \geq q_2^2 + q_3^2\},
$$

whose singular support is the light cone $\partial C$, and which is homogeneous of degree $-1$. The solution has support in the solid cone, not only on its boundary: the sharp Huygens principle fails, as it does for every wave operator in two spatial dimensions, and the tail is the interior part of the cone.

**Proof.** The construction of the fundamental solution of a wave operator is that of *Distributions and Fundamental Solutions*, where the support and the homogeneity are established; the boundary behaviour is the statement that the fundamental solution is singular precisely on the characteristic cone, and the failure of the sharp Huygens principle in two spatial dimensions is the standard count of dimensions.

**Theorem (Fundamental Solution of the Vector Operator).** The vector operator $D$ has a fundamental solution

$$
E_D = D E ,
$$

the distribution obtained by applying $D$ to the fundamental solution of the wave operator; it satisfies $D E_D = \delta$ because $D^2 = \Box_{(2,1)}$. Its singular support is the light cone, so the propagation governed by $D$ is at speed one, in contrast with the elliptic case, where the singular support of the fundamental solution is a single point. Both $E$ and $E_D$ depend on the vector coordinates $(q_1,q_2,q_3)$ alone and are independent of the scalar coordinate $q_0$; $E$ is homogeneous of degree $-1$ and $E_D = DE$ of degree $-2$ in those three variables, and the $\delta$ in the two equations is the delta distribution of the vector subspace.

**Proof.** $D(D E) = D^2E = \Box_{(2,1)}E = \delta$; the singular support is contained in that of $E$ and is not smaller because $E_D$ is not smooth across the cone. The elliptic comparison is the fundamental solution of the Laplacian in *Clifford Analysis*.

## The Cauchy Integral Formula and Its Failure

### The Kernel of the Vector Operator

**Theorem (The Kernel of the Vector Operator).** The kernel of $D$ is large. For every smooth scalar function $h$ of one variable,

$$
D\big(\tilde\pi_+\, h(q_1-q_3)\big) = 0 \qquad\text{and}\qquad D\big(h(q_1+q_3)\,\tilde\pi_-\big) = 0 ,
$$

with $\tilde\pi_\pm = \tfrac12(1\pm e_2)$ the idempotents. Both families contain nonzero compactly supported functions: $\tilde\pi_+\chi(q_1-q_3)$ with $\chi$ a smooth bump vanishes outside a strip and is not zero.

**Proof.** The products of a generator with an idempotent are

$$
e_1\tilde\pi_+ = e_3\tilde\pi_+ = \tfrac12(e_1+e_3), \qquad e_2\tilde\pi_+ = \tilde\pi_+, \qquad e_1\tilde\pi_- = -e_3\tilde\pi_- = \tfrac12(e_1-e_3), \qquad e_2\tilde\pi_- = -\tilde\pi_- ,
$$

so for a scalar function $h$

$$
D(\tilde\pi_+h) = \tfrac12(e_1+e_3)\big(\partial_{q_1}h+\partial_{q_3}h\big) + \tilde\pi_+\,\partial_{q_2}h, \qquad D(h\tilde\pi_-) = \tfrac12(e_1-e_3)\big(\partial_{q_1}h-\partial_{q_3}h\big) - \tilde\pi_-\,\partial_{q_2}h ,
$$

and both right-hand sides vanish for the stated $h$, since $\partial_{q_2}h = 0$ and $\partial_{q_1}h = \mp\partial_{q_3}h$ for $h = h(q_1\mp q_3)$. The four elements $\tilde\pi_+$, $\tilde\pi_-$, $\tfrac12(e_1+e_3)$, $\tfrac12(e_1-e_3)$ occurring here are a basis of the algebra, so the two identities are read off the multiplication table and are exact.

**Corollary (Consequences of the Kernel).** No unique continuation, no identity theorem, no maximum principle and no Liouville theorem hold for the solutions of $Df = 0$: the function $\tilde\pi_+\chi(q_1-q_3)$ with $\chi$ supported in $[1,2]$ is a nonzero solution vanishing on the open half-space $q_1-q_3<1$, so the zero set of a nonzero solution can have interior points and no rigidity of the elliptic type survives.

**Corollary (No Right Inverse).** There is no identity $f = E_D*(Df)$ valid for all compactly supported smooth $f$, and therefore no Cauchy–Pompeiu formula of the elliptic type: the identity would give $f = E_D*0 = 0$ for the nonzero compactly supported solutions of the kernel theorem.

**Theorem (The Inversion on the Left).** What holds is the inversion on the left,

$$
f = D\,(E_D * f),
$$

for every $f$ with compact support, so that $E_D*f$ is a solution of the inhomogeneous equation $Dg = f$ for every datum $f$, while the homogeneous solutions are as numerous as the kernel theorem says.

**Proof.** $D(E_D*f) = (DE_D)*f = \delta*f = f$, the differentiation passing through the convolution because the coefficients are constant.

**Remark (What Fails in Place of the Cauchy Formula).** Three structural features of the quaternionic Cauchy integral formula are absent here. First the kernel: $(\tilde q-\tilde p)^{-1}$ has no counterpart, since $\tilde q-\tilde p$ is a zero divisor exactly when it is null, so its reciprocal does not exist on the light cone and the singular set of the available kernel is a three-dimensional cone through the point rather than the point itself. Second analyticity: the solutions of $Df = 0$ satisfy a first-order system whose characteristic variety is the light cone, and by the kernel theorem they include nonzero compactly supported functions, so they are not analytic and carry no identity theorem. Third inversion: the inversion available is one-sided, by the theorem above, and the boundary formula of Green is valued in the trace pairing, so the boundary data do not pass to the interior values through a single multiplication kernel.

## Principal Values and the Distributional Inverse

The singularities of the inverse on the null cone are treated distributionally, exactly as in the theory of the wave operator.

**Theorem (The Principal Value of the Inverse).** The locally integrable function $1/N(\tilde q)$ on the algebra, and the distribution $\tilde q^{-1} = \tilde{q}^{\natural}/N(\tilde q)$ on the vector subspace, have well-defined principal values: for a test function $\varphi$,

$$
\Big\langle \mathrm{pv}\frac{1}{N},\, \varphi\Big\rangle = \lim_{\varepsilon\to0}\int_{|N(\tilde q)|>\varepsilon}\frac{\varphi(\tilde q)}{N(\tilde q)}\,\mathrm{d}\tilde q ,
$$

and the limit exists because the level sets of $N$ have finite area and the singularity is odd with respect to $\tilde q \mapsto -\tilde q$ after symmetrisation. Off the null cone the reciprocal is an ordinary function and $N(\tilde q)\cdot(1/N(\tilde q)) = 1$ identically, so the difference

$$
N(\tilde q)\cdot \mathrm{pv}\frac{1}{N(\tilde q)} \;-\; 1
$$

is a distribution of degree zero supported on the null cone; in the standard regularisations it is a multiple of $\delta$, with a factor that depends on the normalisation of the cone.

**Proof.** The convergence of the principal value is the homogeneity of $N$ of degree two and the oddness of the integrand about the origin; the support statement follows because the two sides agree off the null cone, and the identification of the correction with a multiple of $\delta$ in the standard regularisations is the computation of *Distributions and Fundamental Solutions*.

**Corollary (The Transfer to the Fundamental Solution).** The transform of the fundamental solution of the vector operator involves exactly this principal value, by the corollary of *Split-Quaternion Harmonic Analysis*, §*The Algebra-Valued Transform and the Vanishing Determinant*, where the formula $\hat E_D = \xi/(2\pi\mathrm{i}N(\xi))$ is displayed; the factor $1/N(\xi)$ must be read as the principal value, and the correction supported on the cone is the distributional content of the cone support of $E_D$.

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

The integration of split-quaternion-valued functions is componentwise, with the orientation of the algebra fixed by the frame $(1,e_1,e_2,e_3)$ and the orientation of the vector subspace by $(e_1,e_2,e_3)$, the form $q_1^2-q_2^2-q_3^2$ being the three-dimensional Minkowski form of the system. The divergence theorem holds on every domain with piecewise smooth boundary, with the Euclidean normal; on a boundary tangent to the light cone the normal is a zero divisor and the boundary term degenerates.

The vector operator is formally self-adjoint, $D^* = D$, and Green's formula reads $\int_\Omega[\operatorname{Sc}((Df)g) + \operatorname{Sc}(f(\bar Dg))] = \int_{\partial\Omega}\operatorname{Sc}(fgn)$, with the classical Green identities for the wave operator as corollaries; the two-sided form is forced by the failure of the two-term Leibniz rule in the non-commutative algebra. The wave operator $\Box_{(2,1)} = D^2$ has a fundamental solution supported in the closed future cone with singular support the light cone, and the vector operator has the fundamental solution $D E$; the propagation is at speed one, and the sharp Huygens principle fails, as in every two-spatial-dimensional wave problem.

There is no Cauchy integral formula: the candidate kernel $(\tilde q-\tilde p)^{-1}$ does not exist on the light cone, where the difference of two points is a zero divisor. The inversion that holds is one-sided, $f = D(E_D*f)$; the formula $f = E_D*(Df)$ of the elliptic theory fails, as the large kernel of $D$ shows, and the maximum principle, the mean value property, the identity theorem and the elliptic Liouville and removable-singularity theorems all fail. The quaternion case, with its elliptic operator and its point singularity, is the opposite extreme, and the differences are all traced to the indefiniteness of the form and the presence of the zero divisors. The eight-dimensional relative is a later system of Part V, named only.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\int_\Omega f$ | the componentwise volume integral | this article |
| $(1,e_1,e_2,e_3)$, $(e_1,e_2,e_3)$ | the orientations of the algebra and of the vector subspace | this article |
| $(q_1,q_2,q_3)$ with $q_1^2-q_2^2-q_3^2$ | the three-dimensional Minkowski space of the system | *Split-Quaternion Rotations and the Lorentz Group* |
| $n$ | the Euclidean unit normal, read as a split-quaternion | this article |
| $D^* = D$ | the formal adjoint of the vector operator | this article |
| $\bar D = \partial_{q_1} e_1 + \partial_{q_2} e_2 + \partial_{q_3} e_3$ | the operator acting on the right | this article |
| $\int[\operatorname{Sc}((Df)g) + \operatorname{Sc}(f(\bar Dg))] = \int\operatorname{Sc}(fgn)$ | Green's formula | this article |
| $E$ | the fundamental solution of $\Box_{(2,1)}$, supported on the cone | *Distributions and Fundamental Solutions* |
| $E_D = DE$ | the fundamental solution of $D$ | this article |
| $f = D(E_D*f)$ | the inversion on the left | this article |
| $\tilde\pi_+h(q_1-q_3)$, $h(q_1+q_3)\tilde\pi_-$ | the two families in the kernel of $D$ | this article |
| $C$, $\partial C$ | the future cone and the light cone | *Split-Quaternion Geometry* |

## Further Reading

- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I* (Springer, 1990), for the characteristic variety of a first-order operator, the propagation of singularities and the absence of a reproducing kernel in the hyperbolic case.
- Fritz John, *Partial Differential Equations*, 4th ed. (Springer, 1991), for the wave equation, its fundamental solution and the failure of the sharp Huygens principle in two spatial dimensions.
- Robert P. Gilbert and James L. Buchanan, *First Order Elliptic Systems: A Function Theoretic Approach* (Academic Press, 1983), for the elliptic comparison and the Cauchy integral formula that the hyperbolic case lacks.
- Ricardo Estrada and Ram P. Kanwal, *A Distributional Approach to Asymptotics* (Birkhäuser, 2002), for the homogeneous distributions supported on cones and their use as fundamental solutions.
