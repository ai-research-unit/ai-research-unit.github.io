
# __Maxwell's Equations in the Biquaternionic Formulation__

## Introduction

Maxwell's equations are the clearest illustration of why the biquaternionic formulation is natural. In their biquaternionic form, they collapse into a single equation relating a biquaternionic field strength to a biquaternionic source. With the $ict$ structure built into the Minkowski subspace, the biquaternionic structure becomes manifest, and the Lorentz invariance of electromagnetism appears as a rotation in the Minkowski subspace.

This article develops the biquaternionic formulation of Maxwell's equations in a material medium characterized by permittivity $\epsilon$ and permeability $\mu$, then takes the vacuum limit $\epsilon = \epsilon_0$, $\mu = \mu_0$. The presentation proceeds in the natural order: first the standard Maxwell equations in three-vector form, then the potential biquaternion $\tilde{A}$, then the biquaternionic gradient $\tilde{\nabla}$, then the field-strength biquaternion $\tilde{F}$, and finally the single biquaternionic equation that replaces the four standard Maxwell equations. The article closes with the gauge structure, the retarded Green's function, the stationary limit, the energy conservation law, the biquaternionic energy–momentum, the Lorentz transformation of the potential, and the extension to complexified spacetime.

Throughout this article, the symbol $c$ denotes the **speed of light in the medium**: $c = 1/\sqrt{\epsilon\mu}$. In vacuum, $c$ reduces to the constant vacuum speed of light $c_0 = 1/\sqrt{\epsilon_0\mu_0}$. The symbol $v$ (and $\mathbf{v}$, $\mathbf{u}$) is reserved for particle and frame velocities. This convention keeps the notation consistent with relativistic mechanics, where $c$ is the speed of light and $v$ is a velocity.

## Maxwell's Equations in a Material Medium

In a linear, isotropic, non-dispersive medium characterized by permittivity $\epsilon$ and permeability $\mu$, Maxwell's equations in three-vector form are

$$
\mathrm{rot}\,\mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t},
$$

$$
\mathrm{rot}\,\mathbf{H} = \frac{\partial \mathbf{D}}{\partial t} + \mathbf{J},
$$

$$
\mathrm{div}\,\mathbf{D} = \rho,
$$

$$
\mathrm{div}\,\mathbf{B} = 0,
$$

with the constitutive relations

$$
\mathbf{D} = \epsilon\,\mathbf{E}, \qquad \mathbf{B} = \mu\,\mathbf{H}.
$$

Here $\mathbf{E}$ is the electric field, $\mathbf{H}$ the magnetic field, $\mathbf{D}$ the electric displacement, $\mathbf{B}$ the magnetic induction, $\rho$ the free charge density, and $\mathbf{J}$ the free current density. The constants $\epsilon$ and $\mu$ are properties of the medium. In vacuum they take the values $\epsilon_0$ and $\mu_0$.

The speed of electromagnetic waves in the medium is

$$
c = \frac{1}{\sqrt{\epsilon \mu}}.
$$

In vacuum this becomes

$$
c_0 = \frac{1}{\sqrt{\epsilon_0 \mu_0}}.
$$

The local speed of light $c$ is the factor that controls propagation in the medium, and it enters the equations in the same way for all media. In vacuum, $c = c_0$.

The source fields $\rho$ and $\mathbf{J}$ are not independent: they satisfy the **charge conservation law**

$$
\mathrm{div}\,\mathbf{J} + \frac{\partial \rho}{\partial t} = 0,
$$

which follows from taking the divergence of the Ampère–Maxwell law and substituting Gauss's law. This constraint is the integrability condition for the Maxwell system, and it will reappear below as the constraint on the biquaternionic source $\tilde{R}$.

## The Potential Biquaternion

The electromagnetic field is described by a **potential biquaternion**

$$
\tilde{A} = A_0 + \mathbf{A}, \qquad A_0 = \frac{i\phi}{c}, \qquad \mathbf{A} = \mathbf{A},
$$

where $\phi$ is the scalar potential and $\mathbf{A}$ is the vector potential. The tilde signals that $\tilde{A}$ is an element of the biquaternion algebra $\mathbb{B}$, not a four-vector.

The scalar part $A_0 = i\phi/c$ is purely imaginary, matching the complex time coordinate $ict$. The vector part $\mathbf{A}$ is the ordinary vector potential. The factor of $i$ in $A_0$ is the same factor that appears in the complex time coordinate.

The coordinate representation of $\tilde{A}$ as a four-vector potential is

$$
\tilde{A} = \sum_{\mu=0}^{3} A_\mu e_\mu \;\longleftrightarrow\; A^\mu = (A^0, A^1, A^2, A^3),
$$

with $e_0 = 1$ and $e_1, e_2, e_3$ the quaternion units, and

$$
A^0 = \frac{i\phi}{c}, \qquad (A^1, A^2, A^3) = \mathbf{A}.
$$

The four-vector representation is a coordinate representation of the biquaternion, not the fundamental object.

## The Biquaternionic Gradient

We introduce the operator that makes the biquaternionic structure manifest. Define the **biquaternionic gradient** in the four variables $(ict, x, y, z)$:

$$
\tilde{\nabla} = e_0 \partial_{ict} + e_1 \partial_x + e_2 \partial_y + e_3 \partial_z,
$$

where $\partial_{ict} = \partial/\partial(ict)$, $\partial_x = \partial/\partial x$, and so on. The tilde signals that $\tilde{\nabla}$ is a biquaternion-valued operator. The inclusion of $e_0$ alongside $e_1, e_2, e_3$ makes the four components manifestly symmetric.

The **quaternion conjugate** of $\tilde{\nabla}$ is obtained by negating the vector part:

$$
\bar{\tilde{\nabla}} = e_0 \partial_{ict} - e_1 \partial_x - e_2 \partial_y - e_3 \partial_z.
$$

The product $\tilde{\nabla} \bar{\tilde{\nabla}}$ is computed term by term:

- Time-time: $e_0 \partial_{ict} \cdot e_0 \partial_{ict} = \partial_{ict}^2$.
- Time-space cross terms: these vanish because $\partial_{ict}$ commutes with $\partial_k$ and $e_0$ commutes with $e_k$.
- Space-space: $\sum_{j,k=1}^{3} e_j e_k \partial_j \partial_k = -\Delta e_0$, where $\Delta = \partial_x^2 + \partial_y^2 + \partial_z^2$, using $e_j e_k = -\delta_{jk} e_0 + \epsilon_{jkl} e_l$ and the symmetry of $\partial_j \partial_k$.

Therefore

$$
\tilde{\nabla} \bar{\tilde{\nabla}} = \partial_{ict}^2 + \Delta e_0.
$$

The same result holds in the opposite order, $\bar{\tilde{\nabla}} \tilde{\nabla} = \partial_{ict}^2 + \Delta e_0$. This is exactly the d'Alembertian:

$$
\Box = \tilde{\nabla} \bar{\tilde{\nabla}} = \bar{\tilde{\nabla}} \tilde{\nabla} = \partial_{ict}^2 + \Delta.
$$

So the d'Alembertian is the product of the biquaternionic gradient and its quaternion conjugate.

## The Field-Strength Biquaternion

The electromagnetic field is described by a **field-strength biquaternion**

$$
\tilde{F} = \mathbf{F}, \qquad \mathbf{F} = \sqrt{\epsilon}\,\mathbf{E} + i\sqrt{\mu}\,\mathbf{H}.
$$

Here $\mathbf{F}$ is a complex three-vector combining the electric and magnetic fields. The tilde signals that $\tilde{F}$ is a biquaternion with vanishing scalar part. The square roots $\sqrt{\epsilon}$ and $\sqrt{\mu}$ are the natural normalization factors that make the biquaternionic product symmetric between electric and magnetic contributions.

The field-strength biquaternion is obtained from the potential biquaternion by differentiation:

$$
\tilde{F} = \tilde{\nabla} \tilde{A} - \mathrm{Sc}(\tilde{\nabla} \tilde{A}),
$$

or, equivalently, by the tensor relation

$$
F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu,
$$

with components

$$
F^{\mu\nu} =
\begin{pmatrix}
0 & -E_x/c & -E_y/c & -E_z/c \\
E_x/c & 0 & -B_z & B_y \\
E_y/c & B_z & 0 & -B_x \\
E_z/c & -B_y & B_x & 0
\end{pmatrix}.
$$

The tensor is antisymmetric:

$$
F^{\mu\nu} = -F^{\nu\mu}.
$$

The complex combination $\mathbf{F} = \sqrt{\epsilon}\,\mathbf{E} + i\sqrt{\mu}\,\mathbf{H}$ has a long history. It was introduced by **Ludwik Silberstein** in 1907, in his work on the electromagnetic field as a complex three-vector, and is now known as the **Riemann–Silberstein vector**. The biquaternionic formulation is the natural algebraic home of this object: the complex vector $\mathbf{F}$ is the vector part of a biquaternion with vanishing scalar part, and the operations of the electromagnetic field theory ($\mathrm{rot}$, $\mathrm{div}$, and the wave operator) become biquaternion multiplication and differentiation. The historical construction of Silberstein and its modern biquaternionic formulation are therefore two expressions of the same structure.

## The Biquaternionic Source

The sources of the electromagnetic field are described by a **biquaternionic source**

$$
\tilde{R} = R_0 + \mathbf{R},
$$

with

$$
R_0 = \frac{i\rho}{\sqrt{\epsilon}}, \qquad \mathbf{R} = \sqrt{\mu}\,\mathbf{J}.
$$

The scalar part of $\tilde{R}$ carries the charge density, and the vector part carries the current density. The normalizations $1/\sqrt{\epsilon}$ and $\sqrt{\mu}$ are chosen so that the biquaternionic equation below takes a form with no explicit $\epsilon$ or $\mu$.

The source biquaternion is not arbitrary: the charge conservation law $\mathrm{div}\,\mathbf{J} + \partial_t \rho = 0$ becomes, in biquaternionic form,

$$
\mathrm{Sc}\!\left(\bar{\tilde{\nabla}} \tilde{R}\right) = 0,
$$

i.e., the scalar part of $\bar{\tilde{\nabla}} \tilde{R}$ vanishes. This is the **integrability condition** for the biquaternionic Maxwell equation $\tilde{\nabla} \tilde{F} = -\tilde{R}$, and it is the biquaternionic expression of the conservation of electric charge.

## Maxwell's Equations in Biquaternionic Form

With these definitions, Maxwell's equations take the single compact form

$$
\tilde{\nabla} \tilde{F} = -\tilde{R}.
$$

One equation replaces the four standard Maxwell equations. There is no explicit factor of $\epsilon$ or $\mu$: the medium is entirely in the definitions of $\tilde{F}$ and $\tilde{R}$.

Taking the scalar and vector parts of $\tilde{\nabla} \tilde{F} = -\tilde{R}$ separately, we recover the Hamiltonian form of Maxwell's equations. The scalar part is

$$
\mathrm{div}\,\mathbf{F} = -R_0,
$$

and the vector part is

$$
\partial_{ict} \mathbf{F} + \mathrm{rot}\,\mathbf{F} = -\mathbf{R}.
$$

These are equivalent to the four standard Maxwell equations. The integrability condition $\mathrm{Sc}(\bar{\tilde{\nabla}} \tilde{R}) = 0$ is automatically satisfied when the source is expressed in terms of the potentials via $\tilde{R} = -\tilde{\nabla} \tilde{F}$, and it is the consistency condition that must be imposed when the source is specified independently.

## The Retarded Green's Function

The biquaternionic Maxwell equation $\tilde{\nabla} \tilde{F} = -\tilde{R}$ is a linear first-order equation for the field strength $\tilde{F}$ in terms of the source $\tilde{R}$. Its solution can be written as a convolution with a **Green's function** $\tilde{G}(\tilde{X})$, which is the solution of the equation with a point source:

$$
\tilde{\nabla} \tilde{G}(\tilde{X}) = \delta(\tilde{X}) e_0.
$$

The physically relevant Green's function is the **retarded** one, which vanishes for $t < 0$ and has support on the future light cone. In the four-vector notation $(x_0, x_1, x_2, x_3) = (ict, x, y, z)$, the retarded Green's function is

$$
\tilde{G}_{\mathrm{ret}}(\tilde{X}) = -\frac{1}{4\pi R}\,\delta(t - R/c)\,e_0 - \frac{i}{4\pi R}\,\delta(t - R/c)\,\hat{R},
$$

where $R = \sqrt{x^2 + y^2 + z^2}$ is the radial distance, $\hat{R} = (x e_1 + y e_2 + z e_3)/R$ is the unit radial biquaternion, and $\delta(t - R/c)$ is the Dirac delta concentrated on the future light cone. The two terms correspond to the scalar and vector parts of the kernel: the scalar part propagates the longitudinal component of the source, and the vector part propagates the transverse component.

The solution of the inhomogeneous equation is then the retarded convolution

$$
\tilde{F}(\tilde{X}) = -\int \tilde{G}_{\mathrm{ret}}(\tilde{X} - \tilde{Y})\,\tilde{R}(\tilde{Y})\,d^4 Y,
$$

where the integral is over the past light cone of $\tilde{X}$. This is the biquaternionic form of the retarded solution of Maxwell's equations, and it is the physically correct solution for radiation problems: the field at a point depends only on the sources in its past light cone, not on the future sources.

The retarded Green's function is distinct from the **Cauchy kernel** $\bar{\tilde{X}}/\|\tilde{X}\|_E^4$ of the elliptic theory (articles 8 and 11). The Cauchy kernel is the fundamental solution of the elliptic d'Alembertian $\Box = \partial_{ict}^2 + \Delta$, whereas the retarded Green's function is the fundamental solution of the hyperbolic wave operator $\Box = -\partial_t^2/c^2 + \Delta$. The two are related by the **Wick rotation** $t \to -i\tau$, which converts the hyperbolic kernel into the elliptic one. The elliptic kernel is the natural object in the Euclidean (imaginary-time) formulation; the retarded kernel is the natural object in the Lorentzian (real-time) formulation.

## The Stationary Limit

When the sources are time-independent, $\partial_t \rho = 0$ and $\partial_t \mathbf{J} = 0$, the biquaternionic Maxwell equation reduces to a **static equation**. The field strength $\tilde{F}$ becomes time-independent, and the equation $\tilde{\nabla} \tilde{F} = -\tilde{R}$ separates into the two standard static equations:

$$
\mathrm{div}\,\mathbf{D} = \rho, \qquad \mathrm{rot}\,\mathbf{H} = \mathbf{J},
$$

where $\mathbf{D} = \epsilon \mathbf{E}$ and $\mathbf{H} = \mathbf{B}/\mu$ are the usual static fields. In biquaternionic form, the static equation is

$$
\tilde{\nabla}_{\mathrm{stat}} \tilde{F} = -\tilde{R}, \qquad \tilde{\nabla}_{\mathrm{stat}} = e_1 \partial_x + e_2 \partial_y + e_3 \partial_z,
$$

where $\tilde{\nabla}_{\mathrm{stat}}$ is the biquaternionic gradient restricted to the spatial directions. The equation is purely spatial, and the time coordinate plays no role.

The static solution is given by the **Newton potential** for the biquaternionic source:

$$
\tilde{F}(\mathbf{x}) = -\frac{1}{4\pi} \int \frac{\tilde{R}(\mathbf{y})}{\|\mathbf{x} - \mathbf{y}\|}\,d^3 y,
$$

where $\|\mathbf{x} - \mathbf{y}\|$ is the ordinary Euclidean distance in $\mathbb{R}^3$. This is the biquaternionic form of the Coulomb and Ampère laws: the scalar part of $\tilde{F}$ is the electric displacement, and the vector part is the magnetic field, both expressed as superpositions of point sources weighted by the inverse distance.

For a point charge $q$ at the origin, the source is $\tilde{R} = i q/\sqrt{\epsilon}\,\delta(\mathbf{x}) e_0$, and the solution is

$$
\tilde{F}(\mathbf{x}) = -\frac{i q}{4\pi\sqrt{\epsilon}\|\mathbf{x}\|}\,e_0,
$$

which is the Coulomb field of a point charge at the origin. In the same way, a steady current loop produces a magnetic dipole field, and the biquaternionic formulation reproduces the standard results of magnetostatics.

## Gauge Structure

The potential biquaternion $\tilde{A}$ is not uniquely determined by the field-strength biquaternion $\tilde{F}$. Two potentials $\tilde{A}$ and $\tilde{A}'$ give the same $\tilde{F}$ if they differ by a **gauge transformation**

$$
\tilde{A}' = \tilde{A} - \tilde{\nabla} \Gamma,
$$

where $\Gamma$ is an arbitrary scalar function. This is the biquaternionic form of the standard gauge transformation $A^\mu \to A^\mu - \partial^\mu \Gamma$.

Under this transformation, the field-strength biquaternion is invariant:

$$
\tilde{F}' = \tilde{\nabla} \tilde{A}' - \mathrm{Sc}(\tilde{\nabla} \tilde{A}') = \tilde{\nabla} \tilde{A} - \mathrm{Sc}(\tilde{\nabla} \tilde{A}) = \tilde{F}.
$$

The scalar part of the potential is not invariant. Write

$$
S = \mathrm{Sc}(\bar{\tilde{\nabla}} \tilde{A}).
$$

This is the biquaternionic scalar field, whose components are $\partial_{ict} A_0 + \mathrm{div}\,\mathbf{A}$. Under a gauge transformation, it transforms as

$$
S' = S + \Box \Gamma.
$$

The scalar field $S$ is therefore a **gauge degree of freedom**. It is not a physical field; it can be changed at will by a gauge transformation. The physical content of the theory is entirely in the gauge-invariant combination $\tilde{\nabla} \tilde{A} + S$ that appears in the field-strength biquaternion.

The **Lorenz gauge** is the condition

$$
S = 0,
$$

which means

$$
\partial_{ict} A_0 + \mathrm{div}\,\mathbf{A} = 0.
$$

This is the biquaternionic form of the standard Lorenz condition $\partial_\mu A^\mu = 0$. It is a choice of gauge, not a physical condition. In the Lorenz gauge, the potential satisfies the wave equation

$$
\Box \tilde{A} = -\mu \tilde{R}',
$$

with

$$
\tilde{R}' = ic\rho + \mathbf{J}.
$$

This is the biquaternionic wave equation for the potential. The factor of $\mu$ is explicit, because the potential equation in the tensor formulation is $\Box A^\mu = -\mu R^\mu$ with $R^\mu = (ic\rho, \mathbf{J})$. Note that the wave equation has a solution if and only if the source $\tilde{R}'$ satisfies the conservation law $\mathrm{Sc}(\bar{\tilde{\nabla}} \tilde{R}') = 0$, which is equivalent to the charge conservation constraint on $\rho$ and $\mathbf{J}$.

The scalar field $S$ has no independent physical meaning. It is a gauge artifact, and the Lorenz gauge is the physical choice that sets it to zero. In the future, if a physical interpretation of $S$ is found, it would have to arise from a coupling to a sector of the theory that is not gauge-invariant. For the classical electromagnetic field, $S$ is not physical.

## Relationship Between the Two Formulations

The two formulations are related as follows:

- The field-strength biquaternion $\tilde{F}$ is obtained from the potential biquaternion $\tilde{A}$ by differentiation: $\tilde{F} = \tilde{\nabla} \tilde{A} - \mathrm{Sc}(\tilde{\nabla} \tilde{A})$.
- The first-order equation $\tilde{\nabla} \tilde{F} = -\tilde{R}$ is equivalent to the second-order equation $\Box \tilde{A} = -\mu \tilde{R}'$ in the Lorenz gauge.
- The source biquaternions $\tilde{R}$ and $\tilde{R}'$ differ by the normalization factors: $\tilde{R} = i\rho/\sqrt{\epsilon} + \sqrt{\mu}\mathbf{J}$, while $\tilde{R}' = ic\rho + \mathbf{J}$.

The first-order formulation is the most compact: one equation for the field strength. The second-order formulation is the most familiar: the wave equation for the potential. Both are valid, and both are biquaternionic.

## The Biquaternionic Energy–Momentum

The energy and momentum of the electromagnetic field are encoded in a **biquaternionic energy–momentum**

$$
\tilde{W} = W + \frac{1}{c}\vec{S},
$$

where $W$ is the energy density and $\mathbf{S}$ is the energy flow density (the Poynting vector). For the electromagnetic field in a medium, these are

$$
W = \frac{1}{2}\left(\epsilon\,\mathbf{E}\cdot\mathbf{E} + \mu\,\mathbf{H}\cdot\mathbf{H}\right), \qquad \mathbf{S} = \mathbf{E}\times\mathbf{H}.
$$

The scalar part of $\tilde{W}$ is the energy density, and the vector part is the energy flow density. The biquaternionic energy–momentum is the natural source for the gravitational field in any theory that couples gravity to the electromagnetic field.

The conservation of energy and momentum is expressed by the biquaternionic equation

$$
\tilde{\nabla} \tilde{W} = -\tilde{P},
$$

where $\tilde{P}$ is the biquaternionic power–force density, whose scalar part is the power density and whose vector part is the force density. This is the biquaternionic form of the Poynting theorem. When expanded, it gives the standard energy conservation law

$$
\frac{\partial W}{\partial t} + \mathrm{div}\,\mathbf{S} + \mathbf{J}\cdot\mathbf{E} = 0.
$$

The biquaternionic energy–momentum is the natural bridge between the electromagnetic field and the gravitational field. In the full complexified framework, the same structure appears in the gravitational sector, with the energy–momentum biquaternion playing the role of the source.

## Energy Conservation and the Cauchy Problem

The biquaternionic energy–momentum $\tilde{W} = W + (1/c)\mathbf{S}$ satisfies the conservation law $\tilde{\nabla} \tilde{W} = -\tilde{P}$, where $\tilde{P}$ is the biquaternionic power–force density. Integrating this law over a spacetime region $D$ with smooth boundary $\partial D$, and using the divergence theorem, gives

$$
\int_{\partial D} \tilde{n} \tilde{W}\,dS = -\int_D \tilde{P}\,dV,
$$

where $\tilde{n}$ is the biquaternion-valued outward normal on $\partial D$. This is the biquaternionic form of the **Poynting theorem**: the flux of energy–momentum through the boundary equals the work done by the sources inside.

The conservation law implies the **uniqueness** of solutions of the Cauchy problem. Suppose two solutions $\tilde{F}_1$ and $\tilde{F}_2$ satisfy the same initial data at $t = 0$ and the same source $\tilde{R}$. Their difference $\tilde{F} = \tilde{F}_1 - \tilde{F}_2$ satisfies the homogeneous equation $\tilde{\nabla}\tilde{F} = 0$ with zero initial data. The energy integral

$$
E(t) = \int_{\mathbb{R}^3} W(\mathbf{x}, t)\,d^3 x = \frac{1}{2}\int_{\mathbb{R}^3} \|\tilde{F}(\mathbf{x}, t)\|_E^2\,d^3 x
$$

is positive-definite and, by the conservation law, time-independent. Since $E(0) = 0$, it follows that $E(t) = 0$ for all $t$, and hence $\tilde{F} = 0$ everywhere. So the Cauchy problem for the biquaternionic Maxwell equation has at most one solution with finite energy. This is the biquaternionic version of the standard uniqueness theorem for Maxwell's equations.

The energy method also provides a stability statement: small perturbations of the initial data lead to small perturbations of the solution, in the $L^2$ norm. The biquaternionic formulation preserves the standard well-posedness of the Maxwell Cauchy problem.

## The Lorentz Transformation of the Potential

The potential biquaternion transforms under a Lorentz boost in a compact form. Let the relative velocity between two inertial frames be $\mathbf{u}$ (the ordinary relative velocity, with $|\mathbf{u}| < c$). Define the **four-velocity biquaternion**

$$
\tilde{U} = c + i\,\mathbf{u},
$$

where the scalar part is the speed of light in the medium and the vector part is the relative velocity. The Lorentz factor is

$$
\gamma = \frac{1}{\sqrt{1 - \mathbf{u}^2/c^2}}.
$$

The potential biquaternion transforms as

$$
\tilde{A}' = \frac{\gamma}{c}\,\tilde{U}\,\tilde{A}.
$$

Expanding this in scalar and vector parts gives the standard Lorentz transformation of the scalar and vector potentials:

$$
\phi' = \gamma\left(\phi - \mathbf{A}\cdot\mathbf{u}\right),
$$

$$
\mathbf{A}' = \gamma\left(\mathbf{A} - \frac{\phi}{c^2}\mathbf{u}\right).
$$

The same transformation law applies to the biquaternionic source $\tilde{R}$ and to the biquaternionic energy–momentum $\tilde{W}$. This confirms that the biquaternionic formulation is Lorentz-covariant, and it shows how the transformation laws look in biquaternionic form. The biquaternionic four-velocity $\tilde{U}$ is the operator that implements the boost.

## The Vacuum Limit

In vacuum, $\epsilon = \epsilon_0$ and $\mu = \mu_0$, and the speed of light becomes

$$
c_0 = \frac{1}{\sqrt{\epsilon_0 \mu_0}}.
$$

All the equations above carry over with the substitution $c \to c_0$, $\epsilon \to \epsilon_0$, $\mu \to \mu_0$. In particular, the field-strength biquaternion becomes

$$
\tilde{F} = \sqrt{\epsilon_0}\,\mathbf{E} + i\sqrt{\mu_0}\,\mathbf{H},
$$

and the potential biquaternion becomes

$$
\tilde{A} = \frac{i\phi}{c_0} + \mathbf{A}.
$$

The complex time coordinate becomes $ic_0 t$, recovering the familiar $ict$ form with the vacuum speed of light. The structure of the equations is unchanged. This is the content of the statement that the vacuum is a special case of a medium: the same equations describe both, with different values of $\epsilon$ and $\mu$.

## The Question of What Is Fundamental

In the standard view, $c_0$ is a fundamental constant of spacetime, and $\epsilon_0$ and $\mu_0$ are properties of the vacuum that are related to $c_0$ by

$$
c_0 = \frac{1}{\sqrt{\epsilon_0 \mu_0}}.
$$

In the material-medium view, $c$ is a derived quantity: it is determined by the properties $\epsilon$ and $\mu$ of the medium. In a fluid, the speed of sound is determined by the density and compressibility. By analogy, one may ask whether the speed of light in vacuum is determined by the electromagnetic properties $\epsilon_0$ and $\mu_0$ of the vacuum, rather than the other way around.

This is a structural question, not a settled one. In SI units, $\mu_0$ and $c_0$ are defined, and $\epsilon_0$ is derived. But the choice of which constants are defined and which are derived is a matter of convention, not physics. The physical question is whether the vacuum has electromagnetic properties in the same sense that a material medium does, or whether $\epsilon_0$ and $\mu_0$ are merely conversion factors between unit systems.

## Beyond the Minkowski Subspace: Complexified Spacetime

Up to this point, all biquaternions have been taken in the Minkowski subspace $\mathbb{M}$, with $A_\mu = a_\mu + i a'_\mu$ and the constraint that the imaginary parts satisfy the reality conditions $a_0 = 0$, $a'_k = 0$ for the spatial components. In the full biquaternion algebra $\mathbb{B}$, the coefficients $A_\mu$ are arbitrary complex numbers, and the potential and field-strength biquaternions become **fully complexified**

$$
\tilde{A} = A_0 + \mathbf{A}, \qquad \tilde{F} = \mathbf{F},
$$

with complex coefficients that are not restricted to the Minkowski subspace. The projection onto the Minkowski subspace reproduces the electromagnetic field; the remaining components correspond to the additional directions of the complexified spacetime.

The biquaternionic formulation extends naturally to this setting. The gradient $\tilde{\nabla}$ becomes an operator on the complexified coordinates, and the factorization $\Box = \tilde{\nabla} \bar{\tilde{\nabla}}$ continues to hold, with $\Box$ now the complexified d'Alembertian. The single equation $\tilde{\nabla} \tilde{F} = -\tilde{R}$ remains valid, but the fields and sources are now fully complex. The integrability condition $\mathrm{Sc}(\bar{\tilde{\nabla}} \tilde{R}) = 0$ remains the conservation law for the complexified source.

This is the natural generalization of the $ict$ structure. The electromagnetic field is the real projection of a complex field, just as the Minkowski subspace is a real slice of the complexified biquaternion algebra. The structure of Maxwell's equations is preserved, but the arena is larger.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis |
| $i$ | Scalar imaginary, $i^2 = -1$, commutes with $e_k$ |
| $\tilde{A}$ | Potential biquaternion |
| $\tilde{F}$ | Field-strength biquaternion |
| $\tilde{R}, \tilde{R}'$ | Source biquaternions |
| $\tilde{W}$ | Energy–momentum biquaternion |
| $\tilde{U}$ | Four-velocity biquaternion |
| $\tilde{\nabla}$ | Biquaternionic gradient |
| $\bar{\tilde{\nabla}}$ | Quaternion conjugate gradient |
| $\Box = \tilde{\nabla}\bar{\tilde{\nabla}}$ | d'Alembertian |
| $\epsilon, \mu$ | Permittivity and permeability of the medium |
| $\epsilon_0, \mu_0$ | Permittivity and permeability of vacuum |
| $c = 1/\sqrt{\epsilon\mu}$ | **Speed of light in the medium** |
| $c_0 = 1/\sqrt{\epsilon_0\mu_0}$ | **Speed of light in vacuum** |
| $\mathbf{u}$ | Particle or frame velocity |

## Further Reading

- Hermann Minkowski, "Space and Time" (1908), reprinted in *The Principle of Relativity* (Dover).
- Albert Einstein, *The Meaning of Relativity* (Princeton, 1922), for the $ict$ formulation of special relativity.
- James Clerk Maxwell, *A Treatise on Electricity and Magnetism* (Dover, 1954), for the original formulation.
- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the four-dimensional formulation.
- L. A. Alexeyeva, "Hamiltonian Form of the Maxwell Equations and Its Generalized Solutions" (2001), for the complex-vector formulation and the retarded Green tensor.
- L. A. Alexeyeva, "Maxwell Equations, Their Hamiltonian and Biquaternionic Forms and Properties of Their Solutions" (2016), for the biquaternionic formulation and the operator factorization.
- A. Waser, "Application of Bi-Quaternions in Physics" (2000, updated 2007), for the biquaternionic energy–momentum and the Lorentz transformation of the potential.

