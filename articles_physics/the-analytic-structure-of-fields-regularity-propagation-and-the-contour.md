# __The Analytic Structure of Fields: Regularity, Propagation and the Contour__

## Introduction

The biquaternion algebra carries a differential calculus, and the calculus has a physical reading. A field is not an arbitrary function of four variables: it is a function that satisfies a first-order constraint. The constraint is the Cauchy–Riemann system of the algebra, its square is the wave operator, and the solutions are the fields that propagate. The kernel that inverts the constraint is the propagator, and the contour that defines the inverse is the choice of causal boundary condition.

The article reads the analytic structure physically. It states the regularity constraint, the two notions of holomorphy, the Fueter construction, the fundamental solution, the Kirchhoff–Green representation, the residue and the zero-divisor boundary. It does not derive a wave equation, a mass spectrum or a dynamics; it reads the structures the calculus already carries.

The central statement is that **regularity is an on-shell constraint**. The operator

$$
D=\sum_\mu e_\mu\frac{\partial}{\partial Q_\mu}
$$

satisfies $DD^{\natural}=D^{\natural}D=\Box$, so a regular field, $DF=0$, is automatically harmonic, $\Box F=0$. The first-order equation is the field equation; the second-order equation is its consequence. The physical reading is the Dirac-type constraint: not every function is a field, and the fields are the kernel of the constraint.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The Cauchy–Riemann operator, regularity and harmonicity | [Biquaternion Regular Functions](../articles_maths/biquaternion-regular-functions.html) |
| The shifted operator, the boundary-value criterion and the Helmholtz splitting | [Biquaternion Regular Functions](../articles_maths/biquaternion-regular-functions.html), §*The Shifted Operator* |
| The Fueter operator and the axial construction | [Fueter Theory for Biquaternions](../articles_maths/fueter-theory-for-biquaternions.html) |
| The fundamental solution, Green's formulas and the Kirchhoff–Green representation | [Biquaternion Integration](../articles_maths/biquaternion-integration.html) |
| The residue and the residue theorem | [Biquaternion Integration](../articles_maths/biquaternion-integration.html), §*The Residue Theory* |
| The gradient, the d'Alembertian and the symbol | [Derivatives, Fields and Transforms](derivatives-fields-and-transforms.html) |
| The mass shell and the propagation cone | [The Zero-Divisor Cone and the Massless Spectrum](the-zero-divisor-cone-and-the-massless-spectrum.html) |
| The two helicities of a time-harmonic field | [The Time-Harmonic Maxwell Operator and the Quaternionic Cauchy Integral](the-time-harmonic-maxwell-operator-and-the-quaternionic-cauchy-integral.html) |

## Regularity as a Constraint

### The Operator

On a four-dimensional real subspace $V\subset\mathbb{B}$ with complex coordinates $Q_t,\dots,Q_z$, the Cauchy–Riemann operator and its conjugate are

$$
D=\sum_{\mu\in\{t,x,y,z\}}e_\mu\frac{\partial}{\partial Q_\mu},
\qquad
D^{\natural}=e_t\frac{\partial}{\partial Q_t}-\sum_{k=1}^{3}\vec e_k\frac{\partial}{\partial Q_k}.
$$

The units satisfy the Clifford relation $e_\mu e_\nu^{\natural}+e_\nu e_\mu^{\natural}=2\delta_{\mu\nu}e_t$, so the cross terms cancel:

$$
DD^{\natural}=D^{\natural}D=\Box
=\left(\frac{\partial^2}{\partial Q_t^2}+\frac{\partial^2}{\partial Q_x^2}+\frac{\partial^2}{\partial Q_y^2}+\frac{\partial^2}{\partial Q_z^2}\right)e_t.
$$

The d'Alembertian is scalar and acts component-wise. On the Euclidean real form it is the Laplacian of signature $(4,0)$; on the material slice it is $-\partial_{t'}^2+\Delta$ of signature $(3,1)$; on the informational slice it is $\partial_t^2-\Delta$ of signature $(1,3)$.

### The Constraint

A continuously differentiable function $F$ is **left-regular** if

$$
DF=0.
$$

The equation is a first-order system of four real equations for four real components. It is not the wave equation; it is the square root of the wave equation. A regular field is harmonic, but a harmonic field need not be regular: the constraint is stronger by one order.

The physical reading is the **on-shell constraint**. The field equation is first order; the second-order equation is a consequence. A field that satisfies the constraint is a field that propagates; a field that satisfies only the second-order equation is a superposition of propagating and non-propagating parts. The regularity condition selects the propagating part.

The two notions of regularity are two physical ansätze:

| notion | condition | physical reading |
| --- | --- | --- |
| single-plane holomorphy | $F$ independent of two coordinates and holomorphic in $A=q_t+\vec e_xq_x$ | a field on a two-dimensional plane: a plane wave, a reduced model |
| hypercomplex regularity | $DF=0$ in all four coordinates | a fully four-dimensional constrained field |

The first is a reduction; the second is the full constraint. The complex analogy holds on the plane and fails in four dimensions, and the failure is the zero divisors.

## The Fueter Construction

The Fueter operator is the same first-order operator read on the quaternionic real form. The **Fueter construction** takes a holomorphic function of one complex variable and extends it axially to a regular function of four variables. The theorem says that the axial extension is regular, and the construction is injective.

The physical reading is the **axial ansatz**. A field that is symmetric about an axis can be generated from a two-dimensional seed; the Fueter theorem says the ansatz is complete for that symmetry class. The reading is a reduction: the four-dimensional constrained field is assembled from a holomorphic seed, and the seed carries the two-dimensional profile.

The construction is not a general solution. A regular field need not be axial, and the Fueter construction does not generate the general kernel. It generates the axially symmetric sector, and the theorem is the statement that the sector is exactly the axial extension of the holomorphic functions. The physical reading is a symmetric ansatz with a completeness theorem, not a general propagator.

## The Fundamental Solution

### The Kernel

The fundamental solution of $D$ on the Euclidean real form is

$$
G(Q)=\frac{Q^{\natural}}{\lVert Q\rVert_E^4},
\qquad
DG=2\pi^2\delta_0 e_t.
$$

It is homogeneous of degree $-3$, and it is regular away from the origin. The constant $2\pi^2$ is the surface area of the unit three-sphere in $\mathbb{R}^4$.

The physical reading is the **propagator**. The kernel is the field of a point source at the origin; the $1/r^3$ falloff is the four-dimensional static field of a point source. The distributional equation is the statement that the source is a delta function at the origin, and the field away from the origin is regular.

### The Representation

The Borel–Pompeiu formula and the Kirchhoff–Green representation express a field in a region in terms of its boundary values and its sources:

$$
F(X)=\int_{\partial\Omega}K(X,Y)F(Y)\,dS_Y
+\int_\Omega G(X-Y)\,DF(Y)\,dV_Y .
$$

For a regular field the volume term vanishes, and the field is determined by its boundary data. The physical reading is the **boundary determination**: a regular field inside a region is fixed by its values on the boundary. The representation is the analytic form of the initial-boundary-value problem.

The Kirchhoff–Green form is the biquaternionic version of the classical representation. It carries the same causal structure: the field at a point is a sum of boundary contributions, and the kernel is singular on the characteristic cone. On the Minkowski slice the cone is the light cone; on the Euclidean form it is the sphere. The reading is the propagation cone, not a signal velocity.

### The Residue

The Cauchy integral formula and the residue theorem hold where the kernel is defined. The residue at a pole is the coefficient of the singular part, and the contour integral picks the poles enclosed.

The physical reading is the **pole prescription**. If the kernel is read as a propagator, the pole is the on-shell mode, and the contour is the choice of boundary condition: retarded, advanced or Feynman. The residue is the on-shell residue; the contour is the causal choice. The algebra supplies the poles and the residues; the contour is an extra choice, and the three choices are the three propagators.

The reading is conditional. The corpus's residue theory is the mathematical theorem; the identification of the contour with a physical propagator is the interpretive step, and it requires a dynamics and a vacuum state that the algebra does not supply.

## The Zero-Divisor Boundary

The Cauchy integral formula fails on the null cone. The kernel $G(Q)=Q^{\natural}/\lVert Q\rVert_E^4$ is singular at $Q=0$, and the algebra's zero divisors make the inverse and the naive inverse function fail on the cone.

The physical reading is the **boundary of the analytic domain**. The null cone is where the analytic continuation degenerates; the zero divisors are the obstruction. On the material slice the cone is the light cone, and the failure is the massless limit: the kernel is on the cone, the residue is at the pole, and the contour is the prescription.

The zero divisors also make the naive inverse function fail. The inverse function theorem needs a non-zero Jacobian, and on the cone the Jacobian degenerates. The physical reading is the caustic: the image of a regular map folds, and the fold is the cone.

## The Shifted Operator

The shifted operator is

$$
D_\alpha=D+M_\alpha,
\qquad
\alpha\in\mathbb{B},
$$

where $M_\alpha$ is right multiplication by $\alpha$. The equation $D_\alpha F=0$ defines the $\alpha$-hyperholomorphic functions. The parameter is an arbitrary element: it may be a zero divisor, its square need not be scalar, and it need not commute.

The physical reading is the **mass or chemical potential**. The shift is a constant term in the first-order equation; it is the analogue of a mass term in the Dirac equation or a chemical potential in a finite-density system. The parameter's norm is the mass shell: for the pure element $\alpha=-(i\omega\vec e_x+m\vec e_y)$ the norm is $m^2-\omega^2$, and $\alpha$ is a zero divisor exactly at $\omega=m$. The degenerate branch of the shifted theory is the mass shell of the parameter.

The boundary-value criterion,

$$
P_\alpha f=f
\quad\text{on }\Gamma,
\qquad
P_\alpha=\tfrac12(I+S_\alpha),
$$

is the statement that the boundary datum lies in the $+1$ eigenspace of the singular integral operator. The physical reading is the **admissible boundary condition**: not every boundary value is the boundary value of a solution. The criterion selects the admissible data, and the three branches of the theory are the three cases of the parameter: regular, zero divisor with non-zero scalar part, and pure zero divisor.

The Helmholtz splitting is the **two-helicity decomposition**:

$$
\ker(\Delta-\alpha^2)=\ker D_\alpha\oplus\ker D_{-\alpha}
$$

for scalar $\alpha$. The two shifted kernels are the two circular polarizations of a time-harmonic field. The differential projectors $\Pi_{\pm\alpha}$ split the ambient space into the two helicity sectors, and the boundary projectors $P_\alpha,Q_\alpha$ split the boundary data. The physical reading is the decomposition of a time-harmonic field into two chiral components, each satisfying a first-order equation.

## Physical Interpretations

- **Regularity is an on-shell constraint.** $DF=0$ is the first-order field equation; $DD^{\natural}=\Box$ makes every regular field harmonic. The constraint selects the propagating part.
- **The two regularities are two ansätze.** Single-plane holomorphy is a two-dimensional reduction; hypercomplex regularity is the full four-dimensional constraint. The difference is the dimension of the propagation.
- **The Fueter construction is the axial ansatz.** A holomorphic seed generates an axially symmetric regular field, and the theorem says the ansatz is complete for that symmetry class.
- **The fundamental solution is the propagator.** $G=Q^{\natural}/\lVert Q\rVert^4$ is the field of a point source; the $1/r^3$ falloff is the four-dimensional static field.
- **The Kirchhoff–Green formula is boundary determination.** A regular field inside a region is fixed by its boundary values and its sources; the kernel is singular on the propagation cone.
- **The residue is the on-shell mode, and the contour is the causal choice.** The poles are the modes; the contour selects retarded, advanced or Feynman. The algebra supplies the poles; the contour is an extra choice.
- **The zero divisors are the boundary of the analytic domain.** The Cauchy formula, the inverse and the naive inverse function fail on the null cone; the cone is the caustic of the regular map.
- **The shift is a mass or a chemical potential.** The parameter's norm is the mass shell; the degenerate branch is the lightlike parameter; the Helmholtz splitting is the two-helicity decomposition.

## Limits

The analytic structure is a calculus, not a dynamics. The article does not derive a wave equation, a mass spectrum, a coupling or a scattering amplitude.

The propagator reading needs a choice of real slice and a contour. On the Euclidean form the kernel is the static Green function; on the Minkowski slice the propagator is a boundary value of the same kernel, and the boundary value is the causal choice.

The residue reading is conditional. The residue theorem is mathematical; the identification of the residue with an on-shell mode needs a dynamics.

The Fueter construction is not a general solution. It generates the axial sector, and the theorem is the completeness of that sector, not of the whole kernel.

The shifted operator's parameter is not necessarily a physical mass. It is an element of the algebra; the identification with a mass or a chemical potential is a reading, and the mass shell is the zero-divisor condition of the parameter.

## Summary

- The Cauchy–Riemann operator $D$ satisfies $DD^{\natural}=\Box$; a regular field $DF=0$ is harmonic.
- Regularity is an on-shell constraint: the first-order equation is the field equation, the second-order equation its consequence.
- Single-plane holomorphy is a two-dimensional reduction; hypercomplex regularity is the full four-dimensional constraint.
- The Fueter construction is the axial ansatz: a holomorphic seed generates an axially symmetric regular field, and the ansatz is complete for that class.
- The fundamental solution $G=Q^{\natural}/\lVert Q\rVert^4$ is the propagator; the Kirchhoff–Green formula determines a regular field from its boundary data.
- The residue is the on-shell mode; the contour is the causal choice. The algebra supplies the poles, the contour is an extra choice.
- The zero divisors are the boundary of the analytic domain: the Cauchy formula, the inverse and the naive inverse function fail on the null cone.
- The shifted operator $D_\alpha$ is a mass or chemical potential; its norm is the mass shell; the Helmholtz splitting is the two-helicity decomposition.
- The calculus supplies no dynamics, no mass spectrum and no coupling.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $D=\sum_\mu e_\mu\partial_\mu$ | the Cauchy–Riemann operator |
| $D^{\natural}$ | its quaternion conjugate |
| $\Box=DD^{\natural}$ | the d'Alembertian |
| $G=Q^{\natural}/\lVert Q\rVert_E^4$ | the fundamental solution |
| $D_\alpha=D+M_\alpha$ | the shifted operator |
| $\alpha$ | the shift, a mass or chemical potential |
| $\Pi_{\pm\alpha}$ | the Helmholtz projectors |
| $S_\alpha$ | the singular integral operator |
| $P_\alpha=\tfrac12(I+S_\alpha)$ | the boundary projector |

## Further Reading

- [Derivatives, Fields and Transforms](derivatives-fields-and-transforms.html), for the gradient, the d'Alembertian and the symbol.
- [Biquaternion Regular Functions](../articles_maths/biquaternion-regular-functions.html), for the regularity system and the shifted operator.
- [Fueter Theory for Biquaternions](../articles_maths/fueter-theory-for-biquaternions.html), for the axial construction.
- [Biquaternion Integration](../articles_maths/biquaternion-integration.html), for the fundamental solution, the Kirchhoff–Green formula and the residue.
- [The Zero-Divisor Cone and the Massless Spectrum](the-zero-divisor-cone-and-the-massless-spectrum.html), for the cone and the massless limit.
- [Thermality from the Modular Pair](thermality-from-the-modular-pair-state-clock-and-the-definite-reading.html), for the state and the clock.
