
# __Split-Quaternion Integration__

## Introduction

This article treats the integration of split-quaternion-valued functions. It fixes the orientation of the vector subspace, proves integration by parts and the divergence theorem for the algebra, derives Green's formulas for the vector operator, constructs the fundamental solution, and explains why there is no Cauchy integral formula, comparing the situation with the quaternion and split-complex cases.

The split-quaternion algebra, its norm form, its conjugation and its subspaces are assumed from *Split-Quaternion Algebra*; the Lorentzian geometry of the vector subspace, including the sign convention of the form $b^2-c^2-d^2$ as three-dimensional Minkowski space, from *Split-Quaternion Rotations and the Lorentz Group*, §*The Lorentz Group of Signature $(2,1)$*, and *Split-Quaternion Geometry*; the operators, the metric structure and the failure of the naive derivative from *Split-Quaternion Analysis*, and the operators of the subspaces from *Split-Quaternion Analysis on Subspaces*. The theory of distributions and fundamental solutions is that of *Distributions and Fundamental Solutions*, the quaternion case that of *Quaternion Integration*, and the two-dimensional hyperbolic case that of *Split-Complex Integration*. Nothing physical is invoked.

## Volume Integrals and the Orientation

**Definition.** Let $\Omega \subset \mathbb{H}_{\mathrm{s}} \cong \mathbb{R}^4$ be a domain with piecewise smooth boundary. The **volume integral** of a split-quaternion-valued function $f$ on $\Omega$ is defined componentwise in the basis $1, e_1, e_2, e_3$:

$$
\int_\Omega f = \Big(\int_\Omega f_0\Big) + \Big(\int_\Omega f_1\Big) e_1 + \Big(\int_\Omega f_2\Big) e_2 + \Big(\int_\Omega f_3\Big) e_3 ,
$$

and it is the Bochner integral of a function with values in the finite-dimensional normed space with the Euclidean norm of *Split-Quaternion Analysis*, §*The Metric Structure*.

**Definition (Orientation).** The algebra $\mathbb{H}_{\mathrm{s}} \cong \mathbb{R}^4$ is oriented by the frame $(1, e_1, e_2, e_3)$, so the volume element is $\mathrm{d}a\,\mathrm{d}b\,\mathrm{d}c\,\mathrm{d}d$. The vector subspace $V$ with the coordinates $(b,c,d)$ is oriented by $(e_1,e_2,e_3)$; the form restricted to it is $b^2-c^2-d^2$, and this is the three-dimensional Minkowski space whose Lorentz group is $\mathrm{SO}^{+}(2,1)$ by *Split-Quaternion Rotations and the Lorentz Group*, §*The Lorentz Group of Signature $(2,1)$*. Both orientations are fixed once and for all; no factor of $i$ or of any other non-real element is introduced into any integral in this article.

**Theorem (The Boundary and the Normal).** Let $\partial\Omega$ be a smooth hypersurface with a **non-characteristic** normal, that is a normal vector $n$ with $N(n) \neq 0$, scaled so that $N(n) = \pm 1$. Then the boundary carries the Riemannian or Lorentzian area element induced by the Euclidean metric of $\mathbb{R}^4$ restricted to the hypersurface, the outward normal $n$ is a split-quaternion vector field, and the divergence theorem holds:

$$
\int_\Omega \partial_a f \;=\; \int_{\partial\Omega} f\, n_a, \qquad \int_\Omega \partial_b f \;=\; \int_{\partial\Omega} f\, n_b, \qquad \int_\Omega \partial_c f \;=\; \int_{\partial\Omega} f\, n_c, \qquad \int_\Omega \partial_d f \;=\; \int_{\partial\Omega} f\, n_d ,
$$

for every $f$ with continuous first derivatives on the closure, where $(n_a,n_b,n_c,n_d)$ are the coordinates of the outward unit Euclidean normal. If the normal is characteristic, that is if $N(n) = 0$, then $n$ cannot be normalised and the induced form on the boundary is degenerate.

**Proof.** The identities are the divergence theorem in the four coordinates, valid for each component; the normalisation uses the non-degeneracy of the Euclidean metric, and the last statement is *Split-Quaternion Norm and Invertibility*, §*Isotropy*. $\square$

## Integration by Parts and Green's Formulas

**Definition.** The **scalar product** of two functions is

$$
\langle f, g\rangle = \int_{\Omega} \operatorname{Sc}\big(f\, \bar{g}\big),
$$

and the associated pairing is real-valued and non-degenerate in each variable pointwise.

**Theorem (The Adjoint of the Vector Operator).** Left multiplication by $e_i$ has adjoint left multiplication by $-e_i$ with respect to the pointwise pairing $\operatorname{Sc}(f\bar g)$:

$$
\operatorname{Sc}\big((e_i f)\bar g\big) = -\operatorname{Sc}\big(f\,\overline{e_i g}\big) .
$$

Consequently the vector operator $D = e_1\partial_b + e_2\partial_c + e_3\partial_d$ is formally skew-adjoint on functions vanishing on the boundary: $D^* = -D$.

**Proof.** The scalar part is invariant under cyclic permutations, $\operatorname{Sc}(xyz) = \operatorname{Sc}(yzx)$, since it is a multiple of the trace in the matrix model; hence $\operatorname{Sc}(e_if\bar g) = \operatorname{Sc}(f\bar g e_i) = \operatorname{Sc}(f\,\overline{\bar e_i g})$ because $x \mapsto \bar{x}$ is an anti-automorphism, and $\bar e_i = -e_i$. The last statement is the integration by parts of the divergence theorem with vanishing boundary term. $\square$

**Theorem (Green's Formulas).** For $f, g$ with continuous first derivatives on the closure of a domain with non-characteristic boundary,

$$
\int_\Omega \big[(Df)\,g + f\,(Dg)\big] = \int_{\partial\Omega} f\, n\, g ,
$$

where $n$ is the vector normal of the boundary and the products are the products of the algebra. In particular, if $f$ and $g$ vanish on the boundary, $\int_\Omega (Df)g = -\int_\Omega f(Dg)$; if $Df = 0$ and $g$ vanishes on the boundary, then $\int_\Omega f(Dg) = 0$; and if both $Df = 0$ and $Dg = 0$ and one of them vanishes on the boundary, then $\int_{\partial\Omega} fng = 0$.

**Proof.** Expand $D(fg) = (Df)g + f(Dg)$ using the Leibniz rule and the anticommutation of the generators with the gradient in the vector direction; integrate over $\Omega$ with the divergence theorem of the first section, using that $\int_\Omega D(fg)$ is the boundary integral of $fng$ componentwise. $\square$

**Corollary (The Classical Green Identities).** Applying the formulas to the scalar and vector parts separately gives the classical Green identities for the wave operator $\Box_{(2,1)} = D^2$: for scalar functions,

$$
\int_\Omega \big(u\,\Box v - v\,\Box u\big) = \int_{\partial\Omega} \big(u\,\partial_n v - v\,\partial_n u\big),
$$

with the sign of $\partial_n$ taken from the normal vector of the Minkowski form.

**Proof.** Apply the formula to $Du$ and $v$, to $u$ and $Dv$, subtract, and use $D^* = -D$. $\square$

## The Divergence Theorem and the Stokes Theorem

**Theorem (Divergence and Stokes for the Algebra).** For a split-quaternion-valued function $F = F_0 + F_1e_1 + F_2e_2 + F_3e_3$ with continuous first derivatives,

$$
\int_\Omega \Big(\frac{\partial F_0}{\partial a} + \frac{\partial F_1}{\partial b} + \frac{\partial F_2}{\partial c} + \frac{\partial F_3}{\partial d}\Big) = \int_{\partial\Omega} \big(F_0 n_a + F_1 n_b + F_2 n_c + F_3 n_d\big),
$$

and the Stokes theorem holds for the three-form of the vector subspace with the orientation fixed above.

**Proof.** The divergence theorem is applied to each coordinate component, and the Stokes theorem is the usual one for the oriented three-dimensional vector subspace. $\square$

**Corollary (The Role of the Null Boundary).** On a hypersurface containing a characteristic direction, the boundary term of Green's formula degenerates along that direction: the normal vector is a zero divisor, its product with the boundary values annihilates a part of the algebra, and the boundary integral loses information.

**Proof.** If $n$ is null then $n^2 = 0$ and $n$ is a zero divisor by *Split-Quaternion Zero Divisors*, §*The Zero Divisor Set as the Null Cone*; the products $fng$ depend on $f$ and $g$ only through the components that do not annihilate $n$, exactly as in the matrix model. $\square$

## The Fundamental Solution

**Theorem (Fundamental Solution of the Wave Operator).** The operator $\Box_{(2,1)} = -\partial_b^2 + \partial_c^2 + \partial_d^2$ has a fundamental solution $E$ in the vector subspace, a distribution supported in the closed future cone

$$
C = \{(b,c,d) : b \geq 0, \ b^2 \geq c^2 + d^2\},
$$

whose singular support is the light cone $\partial C$, and which is homogeneous of degree $-1$. The solution has support in the solid cone, not only on its boundary: the sharp Huygens principle fails, as it does for every wave operator in two spatial dimensions, and the tail is the interior part of the cone.

**Proof.** The construction of the fundamental solution of a wave operator is that of *Distributions and Fundamental Solutions*, where the support and the homogeneity are established; the boundary behaviour is the statement that the fundamental solution is singular precisely on the characteristic cone, and the failure of the sharp Huygens principle in two spatial dimensions is the standard count of dimensions. $\square$

**Theorem (Fundamental Solution of the Vector Operator).** The vector operator $D$ has a fundamental solution

$$
E_D = D E ,
$$

the distribution obtained by applying $D$ to the fundamental solution of the wave operator; it satisfies $D E_D = \delta$ because $D^2 = \Box_{(2,1)}$. Its singular support is the light cone, so the propagation governed by $D$ is at speed one, in contrast with the elliptic case, where the singular support of the fundamental solution is a single point.

**Proof.** $D(D E) = D^2E = \Box_{(2,1)}E = \delta$; the singular support is contained in that of $E$ and is not smaller because $E_D$ is not smooth across the cone. The elliptic comparison is the fundamental solution of the Laplacian in *Clifford Analysis*. $\square$

## The Cauchy Integral Formula and Its Failure

**Theorem (No Cauchy Integral Formula).** There is no formula of the form

$$
f(y) = \frac{1}{\omega}\int_{\partial\Omega} K(x-y)\, f(x)
$$

reproducing every solution of $Df = 0$ with a kernel $K$ that is smooth off the light cone and homogeneous of degree $-2$ in the four-dimensional sense; the natural candidate $K(x-y) = (x-y)^{-1}$ fails because $x-y$ is a zero divisor whenever $x-y$ is null, so the kernel has a singular set of dimension three, not of codimension four, and the boundary integral cannot reproduce interior values.

**Proof.** A reproducing kernel of the stated homogeneity must be a fundamental solution of $D$ whose singular support is the boundary of the domain; but every fundamental solution of $D$ has singular support the light cone, by the preceding theorem, so its singular set has codimension one and the boundary integral cannot isolate a point. Against the candidate kernel: the inverse is defined only off the zero divisor set and blows up along it, by *Split-Quaternion Analysis*, §*Singularities*. $\square$

**Theorem (The Cauchy–Pompeiu Replacement).** For every test function $f$ with compact support,

$$
f = E_D * (Df),
$$

the convolution with the fundamental solution of the vector operator, and consequently a solution of $Df = 0$ with compact support is zero. The formula is the replacement of the Cauchy integral formula: the interior values of $f$ are recovered from the values of $Df$ in the interior, not from the boundary values of $f$.

**Proof.** Convolution by a fundamental solution inverts the operator: $D(E_D * f) = (D E_D)*f = \delta * f = f$, and the commutation of $D$ with the convolution is the constancy of the coefficients; interchanging the roles of $f$ and $Df$ gives the display. For the second statement, $Df = 0$ gives $f = 0$. $\square$

**Corollary (Consequences and the Contrast).** There is no maximum principle, no mean value property, no Liouville theorem in the elliptic form and no removable singularity theorem of the elliptic type for the solutions of $Df = 0$; the local behaviour of the solutions is governed by the propagation along the light cone, and the singularities of the solutions are concentrated on characteristic surfaces. In the quaternion case all of these theorems hold, because the Dirac operator there is elliptic and its fundamental solution is singular only at a point.

**Proof.** Each failed property is a consequence of the representation of the solutions by a kernel with singular support on the cone, and the elliptic properties in the quaternion case are those of *Quaternion Integration* and *Clifford Analysis*. $\square$

## Principal Values and the Distributional Inverse

The singularities of the inverse on the null cone are treated distributionally, exactly as in the theory of the wave operator.

**Theorem (The Principal Value of the Inverse).** The locally integrable function $1/N(x)$ on the algebra, and the distribution $x^{-1} = \bar{x}/N(x)$ on the vector subspace, have well-defined principal values: for a test function $\varphi$,

$$
\Big\langle \mathrm{pv}\frac{1}{N},\, \varphi\Big\rangle = \lim_{\varepsilon\to0}\int_{|N(x)|>\varepsilon}\frac{\varphi(x)}{N(x)}\,\mathrm{d}x ,
$$

and the limit exists because the level sets of $N$ have finite area and the singularity is odd with respect to $x \mapsto -x$ after symmetrisation. The distribution $\mathrm{pv}(1/N)$ satisfies the identity

$$
N(x)\cdot \mathrm{pv}\frac{1}{N(x)} = 1 + c\,\delta ,
$$

for a constant $c$ determined by the normalisation of the cone, the correction being supported on the null cone.

**Proof.** The convergence of the principal value is the homogeneity of $N$ of degree two and the oddness of the integrand about the origin; the displayed product is the standard computation of the product of a homogeneous quadratic form with the principal value of its reciprocal, as in *Distributions and Fundamental Solutions*, and the constant depends on the measure of the link of the cone. $\square$

**Corollary (The Transfer to the Fundamental Solution).** The transform of the fundamental solution of the vector operator involves exactly this principal value, by the corollary of *Split-Quaternion Harmonic Analysis*, §*The Algebra-Valued Transform and the Vanishing Determinant*, where the formula $\hat E_D = -\xi/(2\pi\mathrm{i}N(\xi))$ is displayed; the factor $1/N(\xi)$ must be read as the principal value, and the correction supported on the cone is the distributional content of the cone support of $E_D$.

**Proof.** Combine the displayed transform with the definition of the principal value above. $\square$

## Comparison with the Quaternion and Split-Complex Cases

| | $\mathbb{H}$ | $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{D}$ |
|---|---|---|---|
| operator | Dirac, elliptic | wave operator, hyperbolic | wave operator in one variable |
| fundamental solution | Poisson kernel, singular at a point | distribution supported on the cone | supported on the two characteristic lines |
| Cauchy integral formula | holds | fails; replaced by Cauchy–Pompeiu | fails; replaced by d'Alembert |
| Green's formula | holds, with the elliptic boundary term | holds on non-characteristic boundaries | holds |
| compactly supported solutions | none, by Liouville | only zero | only zero |
| singularities of solutions | off a point, removable | on characteristic surfaces | on characteristic lines |

The quaternion column is the content of *Quaternion Integration* and the split-complex column that of *Split-Complex Integration*. The single cause of the difference is again the indefiniteness of the form, equivalently the presence of the zero divisors: the characteristic cone of the operator is the zero divisor set, and the fundamental solution must be singular along it. The eight-dimensional relative $\mathbb{H}_{\mathbb{D}}$ is a later system of Part V, treated under Split-Biquaternions, and nothing of it is used here.

## Summary

The integration of split-quaternion-valued functions is componentwise, with the orientation of the algebra fixed by the frame $(1,e_1,e_2,e_3)$ and the orientation of the vector subspace by $(e_1,e_2,e_3)$, the form $b^2-c^2-d^2$ being the three-dimensional Minkowski form of the system. The divergence theorem holds on domains with non-characteristic boundary; on a characteristic boundary the normal is a zero divisor, cannot be normalised and the boundary term degenerates.

The vector operator has formal adjoint $-D$, and Green's formulas read $\int_\Omega[(Df)g + f(Dg)] = \int_{\partial\Omega} fng$, with the classical Green identities for the wave operator as corollaries. The wave operator $\Box_{(2,1)} = D^2$ has a fundamental solution supported in the closed future cone with singular support the light cone, and the vector operator has the fundamental solution $D E$; the propagation is at speed one, and the sharp Huygens principle fails, as in every two-spatial-dimensional wave problem.

There is no Cauchy integral formula: the candidate kernel $(x-y)^{-1}$ has its singular set on the light cone, of codimension one, and cannot reproduce interior values from a boundary integral. The replacement is the Cauchy–Pompeiu formula $f = E_D * (Df)$, from which it follows that a compactly supported solution of $Df = 0$ vanishes; the maximum principle, the mean value property and the elliptic Liouville and removable-singularity theorems all fail. The quaternion case, with its elliptic operator and its point singularity, is the opposite extreme, and the differences are all traced to the indefiniteness of the form and the presence of the zero divisors. The eight-dimensional relative is a later system of Part V, named only.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\int_\Omega f$ | the componentwise volume integral | this article |
| $(1,e_1,e_2,e_3)$, $(e_1,e_2,e_3)$ | the orientations of the algebra and of the vector subspace | this article |
| $(b,c,d)$ with $b^2-c^2-d^2$ | the three-dimensional Minkowski space of the system | *Split-Quaternion Rotations and the Lorentz Group* |
| $n$, non-characteristic boundary | the normal vector with $N(n) \neq 0$ | this article |
| $D^* = -D$ | the formal adjoint of the vector operator | this article |
| $\int[(Df)g + f(Dg)] = \int fng$ | Green's formula | this article |
| $E$ | the fundamental solution of $\Box_{(2,1)}$, supported on the cone | *Distributions and Fundamental Solutions* |
| $E_D = DE$ | the fundamental solution of $D$ | this article |
| $f = E_D*(Df)$ | the Cauchy–Pompeiu replacement | this article |
| $C$, $\partial C$ | the future cone and the light cone | *Split-Quaternion Geometry* |

## Further Reading

- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I* (Springer, 1990), for the characteristic variety of a first-order operator, the propagation of singularities and the absence of a reproducing kernel in the hyperbolic case.
- Fritz John, *Partial Differential Equations*, 4th ed. (Springer, 1991), for the wave equation, its fundamental solution and the failure of the sharp Huygens principle in two spatial dimensions.
- Robert P. Gilbert and James L. Buchanan, *First Order Elliptic Systems: A Function Theoretic Approach* (Academic Press, 1983), for the elliptic comparison and the Cauchy integral formula that the hyperbolic case lacks.
- Ricardo Estrada and Ram P. Kanwal, *A Distributional Approach to Asymptotics* (Birkhäuser, 2002), for the homogeneous distributions supported on cones and their use as fundamental solutions.
