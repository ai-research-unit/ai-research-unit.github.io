# __Maxwell's Equations in the Biquaternionic Formulation__

## Introduction

Maxwell's equations are the clearest illustration of why the biquaternionic formulation is natural. In their biquaternionic form, they collapse into a single equation relating a biquaternionic field strength to a biquaternionic source. With the $ict$ structure built into the Minkowski subspace, the biquaternionic structure becomes manifest, and the Lorentz invariance of electromagnetism appears as a rotor conjugation in the Minkowski subspace.

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
\tilde{\nabla}^{\natural} = e_0 \partial_{ict} - e_1 \partial_x - e_2 \partial_y - e_3 \partial_z.
$$

The product $\tilde{\nabla} \tilde{\nabla}^{\natural}$ is computed term by term:

- Time-time: $e_0 \partial_{ict} \cdot e_0 \partial_{ict} = \partial_{ict}^2$.
- Time-space cross terms: these vanish because $\partial_{ict}$ commutes with $\partial_k$ and $e_0$ commutes with $e_k$.
- Space-space: $\sum_{j,k=1}^{3} e_j e_k \partial_j \partial_k = -\Delta e_0$, where $\Delta = \partial_x^2 + \partial_y^2 + \partial_z^2$, using $e_j e_k = -\delta_{jk} e_0 + \epsilon_{jkl} e_l$ and the symmetry of $\partial_j \partial_k$.

Therefore

$$
\tilde{\nabla} \tilde{\nabla}^{\natural} = \partial_{ict}^2 + \Delta e_0.
$$

The same result holds in the opposite order, $\tilde{\nabla}^{\natural} \tilde{\nabla} = \partial_{ict}^2 + \Delta e_0$. This is exactly the d'Alembertian:

$$
\Box = \tilde{\nabla} \tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural} \tilde{\nabla} = \partial_{ict}^2 + \Delta.
$$

So the d'Alembertian is the product of the biquaternionic gradient and its quaternion conjugate.

## The Field-Strength Biquaternion

The electromagnetic field is described by a **field-strength biquaternion**

$$
\tilde{F} = \mathbf{F}, \qquad \mathbf{F} = i\sqrt{\epsilon}\,\mathbf{E} - \sqrt{\mu}\,\mathbf{H}.
$$

Here $\mathbf{F}$ is a complex three-vector combining the electric and magnetic fields, with an **imaginary** electric part and a **real** magnetic part: the electric field carries a time index, and in the $ict$ convention it is the time direction that supplies the factor $i$. The tilde signals that $\tilde{F}$ is a biquaternion with vanishing scalar part. The square roots $\sqrt{\epsilon}$ and $\sqrt{\mu}$ are the natural normalization factors that make the biquaternionic product symmetric between electric and magnetic contributions.

The field-strength biquaternion is obtained from the potential biquaternion by differentiation. In the biquaternion algebra, the natural object constructed from $\tilde{A}$ is

$$
\tilde{F} = \tilde{\nabla}^{\natural} \tilde{A} - \mathrm{Sc}\!\left(\tilde{\nabla}^{\natural} \tilde{A}\right),
$$

which is the vector part of $\tilde{\nabla}^{\natural}\tilde{A}$. Equivalently, in tensor language,

$$
F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu,
$$

with components

$$
F^{\mu\nu} =
\begin{pmatrix}
0 & iE_x/c & iE_y/c & iE_z/c \\
-iE_x/c & 0 & B_z & -B_y \\
-iE_y/c & -B_z & 0 & B_x \\
-iE_z/c & B_y & -B_x & 0
\end{pmatrix}.
$$

The tensor is antisymmetric:

$$
F^{\mu\nu} = -F^{\nu\mu}.
$$

**A note on the relation between $\mathbf{F}$ and $\tilde{\nabla}^{\natural}\tilde{A}$.** The precise identification of the biquaternion $\mathbf{F} = i\sqrt{\epsilon}\mathbf{E} - \sqrt{\mu}\mathbf{H}$ with the vector part of $\tilde{\nabla}^{\natural}\tilde{A}$ depends on the normalization of the potential and on the sign conventions for the fields. The tensor formula $F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu$ is unambiguous, and it is the definition of the field strength used in this article. The formula $\tilde{F} = \tilde{\nabla}^{\natural}\tilde{A} - \mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{A})$ reproduces this field strength up to an overall normalization factor; with the convention $A_0 = i\phi/c$ used here the electric part is imaginary, and the choice $A_0 = -i\phi/c$ would reverse it. The reader who wants to verify the exact correspondence should check the components directly against the tensor formula.

The complex combination $\mathbf{F} = i\sqrt{\epsilon}\,\mathbf{E} - \sqrt{\mu}\,\mathbf{H}$ has a long history. It was introduced by **Ludwik Silberstein** in 1907, in his work on the electromagnetic field as a complex three-vector, and is now known as the **Riemann–Silberstein vector**; the biquaternionic field strength is $i\sqrt{\epsilon}$ times that vector, an overall constant factor. The biquaternionic formulation is the natural algebraic home of this object: the complex vector $\mathbf{F}$ is the vector part of a biquaternion with vanishing scalar part, and the operations of the electromagnetic field theory ($\mathrm{rot}$, $\mathrm{div}$, and the wave operator) become biquaternion multiplication and differentiation. The historical construction of Silberstein and its modern biquaternionic formulation are therefore two expressions of the same structure.

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
\mathrm{Sc}\!\left(\tilde{\nabla}^{\natural} \tilde{R}\right) = 0,
$$

i.e., the scalar part of $\tilde{\nabla}^{\natural} \tilde{R}$ vanishes. This is the **integrability condition** for the biquaternionic Maxwell equation $\tilde{\nabla} \tilde{F} = -\tilde{R}$, and it is the biquaternionic expression of the conservation of electric charge.

## Maxwell's Equations in Biquaternionic Form

With these definitions, Maxwell's equations take the single compact form

$$
\tilde{\nabla} \tilde{F} = -\tilde{R}.
$$

One equation replaces the four standard Maxwell equations. There is no explicit factor of $\epsilon$ or $\mu$: the medium is entirely in the definitions of $\tilde{F}$ and $\tilde{R}$.

The counting is visible in the characteristic polynomial. The principal symbol of the vector part $\partial_{ict}\mathbf{F} + \mathrm{rot}\,\mathbf{F}$ is $-({\omega}/{c})I + i\,[\boldsymbol{\xi}]_\times$ in the Fourier variables $({\boldsymbol{\xi}},\omega)$, where $[\boldsymbol{\xi}]_\times$ is the cross-product matrix, and its determinant is $-({\omega}/{c})\bigl(({\omega}/{c})^2 - |\boldsymbol{\xi}|^2\bigr)$. The characteristic set is therefore $\omega = 0$ together with the light cone $|\omega| = c|\boldsymbol{\xi}|$. The four standard Maxwell equations have the same characteristic set with every root doubled; the single complex equation carries the characteristics of the four with half the multiplicity, which is the symbol-level form of "one equation replaces four".

Taking the scalar and vector parts of $\tilde{\nabla} \tilde{F} = -\tilde{R}$ separately, we recover the Hamiltonian form of Maxwell's equations. The scalar part is

$$
-\mathrm{div}\,\mathbf{F} = -R_0,
$$

and the vector part is

$$
\partial_{ict} \mathbf{F} + \mathrm{rot}\,\mathbf{F} = -\mathbf{R}.
$$

These are equivalent to the four standard Maxwell equations. The integrability condition $\mathrm{Sc}(\tilde{\nabla}^{\natural} \tilde{R}) = 0$ is automatically satisfied when the source is expressed in terms of the potentials via $\tilde{R} = -\tilde{\nabla} \tilde{F}$, and it is the consistency condition that must be imposed when the source is specified independently.

## The Retarded Green's Function

The biquaternionic Maxwell equation $\tilde{\nabla} \tilde{F} = -\tilde{R}$ is a linear first-order equation for the field strength $\tilde{F}$ in terms of the source $\tilde{R}$. Its solution can be written as a convolution with a **Green's function** $\tilde{G}(\tilde{Q})$, which is the solution of the equation with a point source:

$$
\tilde{\nabla} \tilde{G}(\tilde{Q}) = \delta(\tilde{Q}) e_0.
$$

The physically relevant Green's function is the **retarded** one, which vanishes for $t < 0$ and has support on the future light cone. It is the first-order kernel of the companion article *The Biquaternion D'Alembertian and Its Green's Functions*,

$$
\tilde{G}_1 = \tilde{\nabla}^{\natural}\,G_\Box
= \frac{1}{c}\frac{1}{4\pi R}\,\delta'\!\left(t - \frac{R}{c}\right)\bigl(-i\,e_0 + \hat{R}\bigr) + \frac{1}{4\pi R^2}\,\delta\!\left(t - \frac{R}{c}\right)\hat{R},
$$

where $G_\Box(R,t) = (4\pi R)^{-1}\delta(t - R/c)$ is the scalar retarded kernel of the wave operator, $R = \sqrt{x^2 + y^2 + z^2}$, $\hat{R} = (x e_1 + y e_2 + z e_3)/R$ is the unit radial biquaternion, and $\delta'$ is the derivative of the delta. It satisfies $\tilde{\nabla}\tilde{G}_1 = \Box G_\Box = -\delta(\tilde{Q})$, and it is supported on the future light cone. The kernel is not a multiple of the delta alone: the $\delta'$ term is a **double layer** on the cone and the $\delta$ term a **single layer**, and it is the $\delta'$ term — absent from any schematic multiple-of-$\delta$ display — that the wave-front and jump conditions of *Shock Electromagnetic Waves* require. The three-component form of the same kernel is the Green tensor $U$ of the next section, and its distributional layer calculus is that of *Distributions on Surfaces, Layers, and Jump Conditions*.

The solution of the inhomogeneous equation is then the retarded convolution

$$
\tilde{F}(\tilde{Q}) = -\int \tilde{G}_1(\tilde{Q} - \tilde{Y})\,\tilde{R}(\tilde{Y})\,d^4 Y,
$$

where the integral is over the past light cone of $\tilde{Q}$. This is the biquaternionic form of the retarded solution of Maxwell's equations, and it is the physically correct solution for radiation problems: the field at a point depends only on the sources in its past light cone, not on the future sources.

The retarded Green's function is distinct from the **Cauchy kernel** $\tilde{Q}^{\natural}/\|\tilde{Q}\|_E^4$ of the elliptic theory (companion articles on biquaternion integration and biquaternion analysis on subspaces). The Cauchy kernel is the fundamental solution of the elliptic d'Alembertian $\Box = \partial_{ict}^2 + \Delta$ (with the same sign for all four directions), whereas the retarded Green's function is the fundamental solution of the hyperbolic wave operator $\Box = -\partial_t^2/c^2 + \Delta$. The two are related by the **Wick rotation** $t \to -i\tau$, which converts the hyperbolic kernel into the elliptic one. The elliptic kernel is the natural object in the Euclidean (imaginary-time) formulation; the retarded kernel is the natural object in the Lorentzian (real-time) formulation.

## The A-Field and Its Green Tensor

The complex-vector form of the Maxwell system writes the field as a single complex three-vector

$$
\mathcal{A} = \sqrt{\epsilon}\,\mathbf{E} + i\sqrt{\mu}\,\mathbf{H},
$$

which satisfies one complex equation

$$
-c^{-1}\partial_t \mathcal{A} - i\,\mathrm{rot}\,\mathcal{A} = \mathbf{j},
\qquad
\mathbf{j} = \sqrt{\mu}\,\mathbf{J}_{\mathrm{e}} - i\sqrt{\epsilon}\,\mathbf{J}_{\mathrm{m}},
\qquad
c = \frac{1}{\sqrt{\epsilon\mu}} .
$$

This is Alexeyeva's **A-field**, and the equation is what she calls the **Hamiltonian form** of the Maxwell equations — not the scalar/vector split of $\tilde{\nabla}\tilde{F} = -\tilde{R}$ that this article also calls by that name. The symbol $\mathcal{A}$ is used here for the A-field because the plain $\mathbf{A}$ is already the vector part of the potential biquaternion $\tilde{A}$ elsewhere in this article; the two objects are different and must not be conflated. The A-field carries the same content as the single biquaternionic equation in another variable: since the field strength is $\tilde{F} = i\sqrt{\epsilon}\,\mathbf{E} - \sqrt{\mu}\,\mathbf{H}$,

$$
\mathcal{A} = -i\,\tilde{F},
$$

which is exactly the dual field strength $\tilde{F}_\star = -i\tilde{F}$ of *The Magnetic Monopole in Biquaternionic Form*. The A-field is therefore not an independent object but the Hodge-dual field configuration, and it carries the energy and the flux directly:

$$
W = \tfrac{1}{2}\|\mathcal{A}\|^2,
\qquad
\mathbf{P} = \tfrac{1}{2}\,i c\,\mathcal{A}\times\mathcal{A}^* .
$$

The point of the form is symmetry, not economy: the equation is invariant under the interchange of the electric and magnetic halves, which the four standard Maxwell equations possess only once magnetic charges are admitted. Dropping the condition of their absence is what produces the single complex equation.

On the three components of $\mathcal{A}$ the operator of this equation is the matrix $L_{kj}(\partial_x,\partial_t) = -c^{-1}\delta_{kj}\partial_t + i\,e_{kjl}\partial_l$, so its fundamental solution is a **Green tensor**, not a scalar:

$$
U_{jk}(x,t) = c^{-1}\delta_{jk}\,\partial_t\psi - c\,\partial_j\partial_k\chi - i\,e_{jlk}\,\partial_l\psi,
$$

where

$$
\psi(R,t) = \frac{1}{4\pi R}\,\delta(t - R/c),
\qquad
\chi(R,t) = \psi *_t \theta(t) = \frac{1}{4\pi R}\,\theta(t - R/c),
$$

are the **wave function** (the scalar Green's function of the wave equation $\Delta\psi - c^{-2}\partial_t^2\psi = -\delta$) and its time antiderivative, with $R = \|\mathbf{x}\|$ and $\theta$ the Heaviside function. The tensor satisfies the radiation condition $U_{jk} = 0$ whenever $\|\mathbf{x}\| > ct > 0$ or $t < 0$, and the radiated field is the convolution $\mathcal{A} = U * \mathbf{j}$. The biquaternion kernel $\tilde{G}_1$ of the previous section is the same construction for the four-component field; the tensor form is what the three-component equation requires, and the two should not be confused.

Two limits of the equation are worth recording in this complex form, because they replace a pair of split equations by a single complex one. When the sources are static, $\partial_t\mathcal{A} = 0$ and the equation reduces to the complex-vector Poisson equation

$$
\Delta\mathcal{A} = -i\,\mathrm{rot}\,\mathbf{J} + c\,\nabla\rho_{\mathrm{c}},
$$

whose solution combines the Coulomb and Biot–Savart terms into one complex field; and for a monochromatic field $\mathcal{A}(\mathbf{x},t) = \mathcal{A}(\mathbf{x})e^{-i\omega t}$ it becomes the complex-vector Helmholtz equation

$$
\Delta\mathcal{A} + k^2\mathcal{A} = -ik\,\mathbf{J} - i\,\mathrm{rot}\,\mathbf{J} + c\,\nabla\rho_{\mathrm{c}}, \qquad k = \omega/c,
$$

with the same complex source $\mathbf{j} = \sqrt{\mu}\,\mathbf{J}_{\mathrm{e}} - i\sqrt{\epsilon}\,\mathbf{J}_{\mathrm{m}}$ split into its current and charge parts. These are Alexeyeva's static and monochromatic forms; the electric and magnetic halves are solved together, and the interface conditions on a surface of discontinuity are read from the single complex equation rather than from a matched pair.

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

The static solution is given by the **gradient of the Newton kernel**, not by the Newton kernel itself, because the static equation is first order:

$$
\tilde{F}(\mathbf{x}) = \frac{1}{4\pi} \int \frac{(\mathbf{x} - \mathbf{y})\,R_0(\mathbf{y})}{\|\mathbf{x} - \mathbf{y}\|^3}\,d^3 y \;-\; \frac{1}{4\pi} \int \frac{\mathbf{R}(\mathbf{y}) \times (\mathbf{x} - \mathbf{y})}{\|\mathbf{x} - \mathbf{y}\|^3}\,d^3 y,
$$

with $R_0 = \mathrm{Sc}(\tilde{R})$ and $\mathbf{R} = \mathrm{Vect}(\tilde{R})$, and where $\|\mathbf{x} - \mathbf{y}\|$ is the ordinary Euclidean distance in $\mathbb{R}^3$. The first term is the biquaternionic form of the Coulomb law and the second that of the Biot-Savart law. Its imaginary part is $\sqrt{\epsilon}\mathbf{E}$ and its real part is $-\sqrt{\mu}\mathbf{H}$.

For a point charge $q$ at the origin, the source is $\tilde{R} = i q/\sqrt{\epsilon}\,\delta(\mathbf{x}) e_0$, and the solution is

$$
\tilde{F}(\mathbf{x}) = \frac{i q\,\hat{\mathbf{x}}}{4\pi\sqrt{\epsilon}\,\|\mathbf{x}\|^2},
$$

where $\hat{\mathbf{x}} = \mathbf{x}/\|\mathbf{x}\|$, which is the Coulomb field of a point charge at the origin, falling as $1/\|\mathbf{x}\|^2$. In the same way, a steady current loop produces a magnetic dipole field, and the biquaternionic formulation reproduces the standard results of magnetostatics.

## Gauge Structure

The potential biquaternion $\tilde{A}$ is not uniquely determined by the field-strength biquaternion $\tilde{F}$. Two potentials $\tilde{A}$ and $\tilde{A}'$ give the same $\tilde{F}$ if they differ by a **gauge transformation**

$$
\tilde{A}' = \tilde{A} - \tilde{\nabla} \Gamma,
$$

where $\Gamma$ is an arbitrary scalar function. This is the biquaternionic form of the standard gauge transformation $A^\mu \to A^\mu - \partial^\mu \Gamma$.

Under this transformation, the field-strength biquaternion is invariant:

$$
\tilde{F}' = \tilde{\nabla}^{\natural} \tilde{A}' - \mathrm{Sc}\!\left(\tilde{\nabla}^{\natural} \tilde{A}'\right) = \tilde{\nabla}^{\natural} \tilde{A} - \mathrm{Sc}\!\left(\tilde{\nabla}^{\natural} \tilde{A}\right) = \tilde{F}.
$$

The scalar part of the potential is not invariant. Write

$$
S = \mathrm{Sc}\!\left(\tilde{\nabla}^{\natural} \tilde{A}\right).
$$

This is the biquaternionic scalar field, whose components are $\partial_{ict} A_0 + \mathrm{div}\,\mathbf{A}$. Under a gauge transformation, it transforms as

$$
S' = S - \Box \Gamma.
$$

The scalar field $S$ is therefore a **gauge degree of freedom**. It is not a physical field; it can be changed at will by a gauge transformation. The physical content of the theory is entirely in the vector part of $\tilde{\nabla}^{\natural} \tilde{A}$, which is the field-strength biquaternion $\tilde{F}$ and is invariant under the gauge transformation.

The **Lorenz gauge** is the condition

$$
S = 0,
$$

which means

$$
\partial_{ict} A_0 + \mathrm{div}\,\mathbf{A} = 0.
$$

This is the biquaternionic form of the standard Lorenz condition $\partial_\mu A^\mu = 0$. It is a choice of gauge, not a physical condition. (The electro-gravimagnetic programme of *The Electro-Gravimagnetic Field and the Magnetic-Charge–Mass Hypothesis* uses the same condition in a different role, imposing it as a constraint of its representation rather than choosing it as a gauge; see that article, where the difference of logical status is recorded and not resolved.) In the Lorenz gauge, the potential satisfies the wave equation

$$
\Box \tilde{A} = -\mu \tilde{R}',
$$

with

$$
\tilde{R}' = ic\rho + \mathbf{J}.
$$

This is the biquaternionic wave equation for the potential. The factor of $\mu$ is explicit, because the potential equation in the tensor formulation is $\Box A^\mu = -\mu R^\mu$ with $R^\mu = (ic\rho, \mathbf{J})$. Note that the wave equation has a solution if and only if the source $\tilde{R}'$ satisfies the conservation law $\mathrm{Sc}(\tilde{\nabla}^{\natural} \tilde{R}') = 0$, which is equivalent to the charge conservation constraint on $\rho$ and $\mathbf{J}$.

The scalar field $S$ has no independent physical meaning. It is a gauge artifact, and the Lorenz gauge is the physical choice that sets it to zero. In the future, if a physical interpretation of $S$ is found, it would have to arise from a coupling to a sector of the theory that is not gauge-invariant. For the classical electromagnetic field, $S$ is not physical.

**The gauge function as a velocity potential.** There is a reading of the gauge freedom, older than the relativistic one and independent of it, in which the gauge function is a *velocity potential*. Under $\tilde{A} \to \tilde{A} - \tilde{\nabla}\Gamma$ only the gradient of $\Gamma$ matters, exactly as in the hydrodynamic statement that only the gradient of a potential matters for a velocity and its curl. On the hydrodynamic dictionary set out below, the vector potential is the image of the fluid velocity, the field strength is the image of its vorticity, and the gauge transformation is the freedom to add the gradient of a scalar to the velocity — a change that leaves the vorticity and hence the Lamb vector untouched. This is a formal correspondence and not an explanation of gauge invariance, which the algebraic account above settles on its own; it is recorded because the corpus's own gauge discussion stops at "a choice of gauge, not a physical condition", and the hydrodynamic picture supplies a concrete image of why only a gradient is free.

## The Hydrodynamic Form of the Equations

A second reading of the same equations, older than the relativistic one and independent of it, comes from fluid mechanics. It is a formal correspondence with a specific provenance, not an alternative derivation, and its limits are stated with it.

The bridge is the **Lamb vector**. For an incompressible fluid of velocity $\mathbf{u}$, vorticity $\boldsymbol{\omega} = \nabla\times\mathbf{u}$ and pressure $p$, the convective acceleration obeys the identity

$$
(\mathbf{u}\cdot\nabla)\mathbf{u} = \boldsymbol{\omega}\times\mathbf{u} + \nabla\frac{|\mathbf{u}|^2}{2},
$$

so that the Euler equation $\partial_t\mathbf{u} + (\mathbf{u}\cdot\nabla)\mathbf{u} = -\nabla p/\rho$ takes the **Lamb form**

$$
\partial_t\mathbf{u} = -\,\nabla\!\left(\frac{p}{\rho} + \frac{|\mathbf{u}|^2}{2}\right) - \boldsymbol{\ell},
\qquad
\boldsymbol{\ell} = \boldsymbol{\omega}\times\mathbf{u}.
$$

The quantity $\boldsymbol{\ell}$ is the **Lamb vector**. Comparison with the potential relations of the electromagnetic theory, $\mathbf{B} = \nabla\times\mathbf{A}$ and $\mathbf{E} = -\nabla V - \partial_t\mathbf{A}$, suggests the pairing

$$
\mathbf{u}\;\leftrightarrow\;\mathbf{A},
\qquad
\boldsymbol{\omega}\;\leftrightarrow\;\mathbf{B},
\qquad
\boldsymbol{\ell}\;\leftrightarrow\;\mathbf{E},
\qquad
\frac{p}{\rho}+\frac{|\mathbf{u}|^2}{2}\;\leftrightarrow\;V .
$$

With these identifications the Lamb form of the Euler equation *is* the definition of the electric field from the potentials, $\mathbf{E} = -\nabla V - \partial_t\mathbf{A}$, and its curl is the vorticity equation

$$
\partial_t\boldsymbol{\omega} = -\,\nabla\times\boldsymbol{\ell},
$$

which is Faraday's law $\partial_t\mathbf{B} = -\nabla\times\mathbf{E}$ under the dictionary. Both statements are exact given the pairing. The counterpart of Gauss's law is the divergence of the Lamb form,

$$
\nabla\cdot\boldsymbol{\ell} = -\,\nabla^2\!\left(\frac{p}{\rho} + \frac{|\mathbf{u}|^2}{2}\right),
$$

which holds for a divergence-free velocity. The hydrodynamic image of the charge density is therefore a Laplacian of the pressure-and-kinetic term rather than an independent quantity, which is where the analogy's electric sector is thinnest: the fluid has no carrier of "charge" that the flow does not already determine.

The correspondence is attributed to H. Marmanis. It is stated here in three-vector language, as the source states it, and it is not a biquaternion formula; the biquaternionic content of these equations is the one the rest of this article records.

**Limits.** The correspondence is partial, and the corpus does not take it as an explanation of electromagnetism. The full Euler equation is nonlinear while the field equations are not, and the source paper's correspondence is stated for the linearised equations. The magnetic Gauss law has no fluid counterpart, so the analogy has no magnetic monopole sector. The constitutive relations differ, so permittivity and permeability have no single fluid meaning. And the two theories do not share a symmetry group: Maxwell's equations are Lorentz invariant while the fluid equations are Galilean invariant. What the analogy reflects is the precise part of the symmetry structure the two share — of Maxwell's four equations, the two source-free ones are Galilean invariant as well, which is why the potential and field relations carry over and the source laws do not. The two Galilean limits of electrodynamics make this quantitative: sending $c \to \infty$ at fixed vacuum permeability gives the magnetic limit (the regime of the quasi-stationary approximation), and sending $c \to \infty$ at fixed vacuum permittivity with $\mathbf{B} \to c^2\mathbf{B}$ gives the electric limit, used in electrohydrodynamics; the incompressible fluid limit corresponds to the magnetic one, with the vacuum permittivity playing the role of an acoustic compressibility and the vacuum permeability that of a density. The relativistic account of the field remains the standard one. The force-side counterpart of the same correspondence is recorded in *The Lorentz Force in Biquaternion Form*.

## Relationship Between the Two Formulations

The two formulations are related as follows:

- The field-strength biquaternion $\tilde{F}$ is obtained from the potential biquaternion $\tilde{A}$ by differentiation: $\tilde{F} = \tilde{\nabla}^{\natural} \tilde{A} - \mathrm{Sc}(\tilde{\nabla}^{\natural} \tilde{A})$.
- The first-order equation $\tilde{\nabla} \tilde{F} = -\tilde{R}$ is equivalent to the second-order equation $\Box \tilde{A} = -\mu \tilde{R}'$ in the Lorenz gauge.
- The source biquaternions $\tilde{R}$ and $\tilde{R}'$ differ by the normalization factors: $\tilde{R} = i\rho/\sqrt{\epsilon} + \sqrt{\mu}\mathbf{J}$, while $\tilde{R}' = ic\rho + \mathbf{J}$.

The first-order formulation is the most compact: one equation for the field strength. The second-order formulation is the most familiar: the wave equation for the potential. Both are valid, and both are biquaternionic.

**A third route, and where it loses equivalence.** The two formulations above are equivalent to each other, and both are equivalent to the Maxwell system. The classical route to a single equation is a third thing, and it is not equivalent. Eliminating one field — solving the Ampère–Maxwell law for $\mathbf{H}$ and substituting it into $\mathrm{rot}\,\mathbf{E}=-\partial_t\mathbf{B}$ — yields a second-order wave equation for $\mathbf{E}$ alone, and that equation admits solutions the Maxwell system does not. Any $\mathbf{E}=\nabla\psi$ with $\Box\psi=0$ solves it, since $\Box\nabla\psi=\nabla\Box\psi$ vanishes, while $\mathrm{div}\,\mathbf{E}=\Delta\psi$ need not vanish; for $\psi=e^{ik(z-ct)}$ the divergence is $-k^2\psi$, so the elimination has enlarged the solution set by a longitudinal sector that Maxwell forbids. The constraints $\mathrm{div}\,\mathbf{D}=\rho$ and $\mathrm{div}\,\mathbf{B}=0$ are not implied by the wave equation and have to be reimposed by hand, and the boundary data do not transfer either: a Dirichlet or Neumann datum on $\mathbf{E}$ is natural data for the wave equation and not for the first-order system, while the natural Maxwell datum — the tangential components of $\mathbf{E}$ and $\mathbf{H}$ — is not a datum the wave equation is posed with. The reduction is convenient rather than faithful: it is what one wants for propagation, and it is not a statement of the theory.

The biquaternionic formulation pays no such price, because it eliminates nothing. The single equation $\tilde{\nabla}\tilde{F}=-\tilde{R}$ is first order in one field-strength biquaternion, and the constraints are not separate conditions added afterwards: $\mathrm{div}\,\mathbf{F}=R_0$ is the scalar part of that same equation. This is the property Kravchenko calls the **diagonalization** of the Maxwell system, and it can be reproduced in vector calculus by combining the two fields rather than eliminating one of them into the other; *Maxwell's Equations in Chiral Media — The Quaternionic Reformulation* displays the combinations and the first-order equations they satisfy. The two routes are distinct claims and both are wanted: the quaternionic form is preferred because it carries a function theory, and the point here is only that the first-order biquaternionic equation already has the equivalence the wave equation lacks.

**A fourth route: the matrix form, and what makes it work.** Daniel Henry Gottlieb writes the same system as a single **matrix** equation, in which the field is a $4 \times 4$ matrix and the divergence is a column of operators acting on it. In his units and conventions ($c = 1$, Heaviside–Lorentz, metric signature $(-,+,+,+)$, $t$ the time coordinate) the real skew operator of the Lorentz law and its dual are

$$
F = \begin{pmatrix} 0 & \mathbf{E}^{\mathsf T} \\ \mathbf{E} & -[\mathbf{B}]_\times \end{pmatrix}, \qquad
F^* = \begin{pmatrix} 0 & -\mathbf{B}^{\mathsf T} \\ -\mathbf{B} & -[\mathbf{E}]_\times \end{pmatrix},
$$

with $[\mathbf{u}]_\times$ the matrix of $\mathbf{v} \mapsto \mathbf{u} \times \mathbf{v}$; the paper writes the lower-right block of $F$ as $\times\mathbf{B}$, whose action is $\mathbf{v}\mapsto\mathbf{v}\times\mathbf{B} = -[\mathbf{B}]_\times\mathbf{v}$, which is the same object. The complexification $cF := F - iF^*$ is the matrix of a single complex three-vector,

$$
cF = \begin{pmatrix} 0 & \mathbf{A}^{\mathsf T} \\ \mathbf{A} & i[\mathbf{A}]_\times \end{pmatrix}, \qquad \mathbf{A} = \mathbf{E} + i\mathbf{B},
$$

and with the operator column $(-\partial_t, \nabla)^{\mathsf T}$ read entry by entry against the matrix — each operator differentiating the matrix entry beside it — the four equations become the three statements

$$
F\begin{pmatrix} -\partial_t \\ \nabla \end{pmatrix} = \begin{pmatrix} \rho \\ \mathbf{J} \end{pmatrix}, \qquad
F^*\begin{pmatrix} -\partial_t \\ \nabla \end{pmatrix} = \begin{pmatrix} -\mathrm{div}\,\mathbf{B} \\ \partial_t\mathbf{B} + \mathrm{rot}\,\mathbf{E} \end{pmatrix}, \qquad
cF\begin{pmatrix} -\partial_t \\ \nabla \end{pmatrix} = \begin{pmatrix} \rho \\ \mathbf{J} \end{pmatrix}.
$$

The first holds identically, because it is the two definitions $\rho = \mathrm{div}\,\mathbf{E}$ and $\mathbf{J} = \mathrm{rot}\,\mathbf{B} - \partial_t\mathbf{E}$; the second vanishes exactly when the two homogeneous laws hold; so the third, the paper's one equation, holds exactly when the Maxwell system holds. Recomputing the three on fields built from potentials, $\mathbf{B} = \mathrm{rot}\,\mathbf{A}$ and $\mathbf{E} = -\partial_t\mathbf{A} - \nabla\phi$, gives agreement to $6 \times 10^{-17}$ for the first and the third and $1 \times 10^{-17}$ for the vanishing of the second, and on a field that violates the homogeneous laws the discrepancy in the third is exactly $i\left(\mathrm{div}\,\mathbf{B},\; -(\partial_t\mathbf{B} + \mathrm{rot}\,\mathbf{E})\right)$, so the equivalence is exact rather than numerical coincidence. The paper also records the version of the same equation for the four fields $\mathbf{E}, \mathbf{B}, \mathbf{D}, \mathbf{H}$, in which $\mathbf{D} + i\mathbf{B}$ occupies the vector slots: the shape of the matrix is unchanged, but the paper notes that the square of that matrix is no longer a multiple of the identity — as it is for the form above, where $cF^2 = \langle\mathbf{A},\mathbf{A}\rangle I$ — and that this property singles out the first form among all matrices of the second. Both statements were checked: $cF^2 = \langle\mathbf{A},\mathbf{A}\rangle I$ exactly, and the second form's square misses a multiple of the identity by at least $14$ over $100$ random pairs of vectors.

**The dual form, and why it holds.** The equation has a dual in which the matrix carries the operators and the vector carries the field. With

$$
c\nabla := \begin{pmatrix} 0 & \nabla^{\mathsf T} \\ \nabla & i[\nabla]_\times \end{pmatrix},
$$

the system reads $(\partial_t I - c\nabla)\left(0,\; -\overline{\mathbf{E} + i\mathbf{B}}\right)^{\mathsf T} = \left(\rho,\; \mathbf{J}\right)^{\mathsf T}$, again exactly equivalent, and the two forms are one construction seen from two sides: in the first the matrix is the field and the column the operators, in the second the matrix is the operators and the column the field. Recomputing this form on the same fields gives agreement to machine precision, with one caveat of transcription: the conjugate bar in the column is required. Without it the scalar row still gives $\rho$ and the vector rows are wrong, which is how the formula extracts from the source and is why it is not stated here without the bar.

The paper writes two further equations of the same shape, in which the four-potential $(\phi, \mathbf{A})$ replaces the field in the column and the operator matrix acquires the potential in its entries; they are the potential-level counterparts of the two field-level equations, and they are the paper's route to the wave equation and to the covariant gauge condition $\partial_t\phi + \mathrm{div}\,\mathbf{A} = 0$. As printed, both carry a defect in the vector part, and this is recorded rather than reproduced: the first gives $\partial_t\mathbf{A} - i\,\mathrm{rot}\,\mathbf{A}$ where the definition $\mathbf{E} = -\partial_t\mathbf{A} - \nabla\phi$ requires the missing term $-\nabla\phi$, so it holds only in a gauge with $\nabla\phi = 0$, and the second gives $\partial_t\mathbf{A} + \nabla\phi + i\,\mathrm{rot}\,\mathbf{A}$ where $-\mathbf{E} - i\mathbf{B} = \partial_t\mathbf{A} + \nabla\phi - i\,\mathrm{rot}\,\mathbf{A}$ is required, a sign on the magnetic term. Recomputing both against the definitions, the discrepancies are exactly $|\nabla\phi|$ and $|2\mathbf{B}|$ respectively, term for term; the scalar rows and the operator identity $c\nabla^2 = \Delta I$ on which the reduction rests are unaffected, since the scalar row involves only $\partial_t\phi + \mathrm{div}\,\mathbf{A}$ and neither defect touches it. The duality between the two potential equations is therefore a statement about the two operator matrices, not a statement that the printed columns are already correct, and the mechanism below is what carries it.

The reason the dual pairs agree is an algebraic identity, and it is the source of everything else in this route. The matrices of the complex three-vectors satisfy the Clifford relation

$$
cF(\mathbf{A}_1)\,cF(\mathbf{A}_2) + cF(\mathbf{A}_2)\,cF(\mathbf{A}_1) = 2\langle \mathbf{A}_1, \mathbf{A}_2 \rangle I, \qquad \langle \mathbf{A}, \mathbf{A} \rangle = \mathbf{E}^2 - \mathbf{B}^2 + 2i\,\mathbf{E}\cdot\mathbf{B},
$$

in the complex bilinear form — no conjugation, so that $\langle \mathbf{A}, \mathbf{A} \rangle$ is the two field invariants in one — and they **commute with their own complex conjugates**,

$$
cF(\mathbf{A}_1)\,\overline{cF(\mathbf{A}_2)} = \overline{cF(\mathbf{A}_2)}\,cF(\mathbf{A}_1),
$$

for all $\mathbf{A}_1, \mathbf{A}_2$. Both were recomputed over $100$ random pairs, the first to $4 \times 10^{-15}$ and the second exactly. The commutation is the whole mechanism: it is why the matrix of the field times the column of operators equals the matrix of the operators times the column of the field, and it is what the source itself names as the reason, together with the algebra it names as the origin of the commutation — the left and the right regular representations of the biquaternions. In the operator case the Clifford relation becomes

$$
c\nabla^2 = \Delta I, \qquad (\partial_t I - c\nabla)(\partial_t I + c\nabla) = (\partial_t^2 - \Delta) I,
$$

both recomputed at the finite-difference floor, and the second is the paper's decoupling into the wave equation, written as a product of two first-order factors: it is the same factorization as $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural}$ of the biquaternionic gradient, with the operators reorganized and the signs adapted.

**What the matrix route says about the algebra.** The correspondence with the algebra is exact, and it is a change of basis of *Biquaternion 4×4 Regular Matrix Element Representation*: those $4 \times 4$ matrices are the biquaternion algebra in the basis $e_0, x, y, z$ with $x = ie_1$, $y = ie_2$, $z = ie_3$, whose vector units square to $+e_0$; in that basis the left regular matrix of an element is $a I + cF$ with $cF$ the matrix above, the right regular matrix is **exactly its transpose** with no sign matrix, and $c\nabla$ is the same construction with the components of $\nabla$ in place of the field. All of this was recomputed exactly, including the change of basis between the two conventions. The consequence for the question this section is about is not a confirmation but a reversal of direction: the one-equation compactness, with full equivalence and no elimination, is available in a purely matrix setting, so it settles nothing about the algebra; what the algebra supplies here is the *explanation* of the matrix identities, since the commutation that makes the dual pair agree is the commutation of the left and the right regular representations, and the field matrix is the left regular matrix in a basis. An author working in matrices and counting equations is led back to the algebra as the reason his identities are true. That is a stronger statement for the corpus than another confirmation of compactness, and it is consistent with the position taken in the section *The Question of What Is Fundamental* below: the algebra supplies the home in which relations become structural, not a claim that no other language can write the equation once.

Two further items of the paper belong to other articles. The three matrices $cF(\mathbf{e}_i)$ of the coordinate unit vectors anticommute pairwise, square to the identity, and satisfy $cF(\mathbf{e}_1)cF(\mathbf{e}_2) = i\,cF(\mathbf{e}_3)$, while the sixteen matrices $I$, $cF(\mathbf{e}_i)$, their conjugates and their products form a Hermitian basis of $M_4(\mathbb{C})$ of which the four $\{I, cF(\mathbf{e}_i)\}$ span the biquaternions — same matrices, in the same basis, as the sixteen of the second realization recorded in *Biquaternion 4×4 Regular Matrix Element Representation*, where they are listed and where the transposition identity these matrices satisfy is stated. The tensor $\frac{1}{2}cF\,\overline{cF}$ is real, traceless and carries the energy density, the Poynting vector and the Maxwell stress, and its divergence is the four-force density; that balance, and the matrix proof of it from the Leibniz rule, are recorded beside the corpus's own derivation in *Exercise: The Electromagnetic Energy–Momentum Tensor*. The exponential of the real skew $F$ factors as $e^{F} = e^{cF/2}e^{\overline{cF}/2}$ and is a proper Lorentz transformation, recomputed to $1.4 \times 10^{-14}$ over $100$ random fields; the corpus has no separate article for this exponential as an element of the field theory, and it is recorded here only as a property of $cF$ rather than adopted as a route to the Lorentz group, which the two-sided action of *Biquaternion 4×4 Regular Matrix Element Representation* already supplies.

## The Author's Reading: the Objection, the Modification, and Closure

The biquaternionic form is the corpus's own statement of Maxwell's equations, derived above from the four three-vector equations. The author who supplied the A-field, the Green tensor and the shock-inclusive Cauchy theory reads the classical system differently — as **defective** — and the corpus records the reading here, attributed, because it is the stated motive for the modification that defines her programme.

**The objection.** In Alexeyeva's account the classical system has three faults: the two vector equations are not connected to the two scalar equations; the resulting system is "of a mixed hyperbolic–elliptic type", which she holds to contradict the wave nature of electromagnetic propagation; and it does not describe the longitudinal electromagnetic waves she takes to be observed. The first two are precise and reproducible. The vector pair's characteristic equation is

$$
\nu_\tau^2\left(\frac{\nu_\tau^2}{c^2} - \|\boldsymbol{\nu}\|^2\right)^2 = 0,
$$

so the vector system is hyperbolic with the light cone for its characteristics, while the scalar pair $\epsilon\,\mathrm{div}\,\mathbf{E} = \rho_E$, $\mathrm{div}\,\mathbf{H} = 0$ is purely spatial and elliptic; its Coulomb potential solves $\Delta u = \rho_E$, whose solution decays at infinity, which the author reads as incompatible with propagation. The corpus's own reading is the standard one: the vector equations are the **evolution** system and the scalar equations are **constraints** on its initial data, and the two are not meant to be joined by further dynamics. That the constraint sector is elliptic is a feature of the $3+1$ split, not a defect of the four-dimensional equation. The disagreement is one of interpretation, and the corpus records it only because the modification is built on it.

**The modification.** Joining the vector and scalar equations into one connected system is what the scalar $\alpha$-field does. Adding $\alpha$ to the A-field biquaternion, $\tilde{\mathcal{A}} \to \alpha + \tilde{\mathcal{A}}$, turns the Hamiltonian form into the coupled first-order system

$$
\mathrm{rot}\,\mathbf{H} - \epsilon\,\partial_t\mathbf{E} + c^2\,\mathrm{grad}\,\alpha_1 = \mathbf{j}_E,
\qquad
\mathrm{rot}\,\mathbf{E} + \mu\,\partial_t\mathbf{H} - c^2\,\mathrm{grad}\,\alpha_2 = \mathbf{j}_H,
$$

$$
\epsilon\,\mathrm{div}\,\mathbf{E} + \partial_t\alpha_1 = \rho_E,
\qquad
-\mu\,\mathrm{div}\,\mathbf{H} + \partial_t\alpha_2 = \rho_H,
$$

which is hyperbolic and in which each of the eight equations carries the field. The author calls it the **Maxwell–Dirac** system because its differential operator coincides with the differential part of the Dirac operator; the corpus's *The Biquaternion d'Alembertian and Its Green's Functions* records the related shifted-gradient form of the same name, and *The Electro-Gravimagnetic Field and the Magnetic-Charge–Mass Hypothesis* supplies the physical reading of $\alpha$ as the attraction–resistance field, its front conditions, and the static limit in which it gives Poisson's equation. The corpus records the system as a genuine first-order hyperbolic completion of the Maxwell pair and takes no position on whether the modification is needed.

**Closure.** The author's own assessment is that the biquaternionic form is mathematically and physically self-consistent but **unclosed**: the field equations do not determine their own charges and currents, and closure requires the *material equations* for $\rho$ and $\mathbf{j}$, supplied in the companion papers. This is the corpus's own recurring theme — the source biquaternion $\tilde{R}$ must be supplied, not derived — restated in the author's terms, and it is the reason the programme's later papers turn to a law of motion for the charge–current field.

The three-vector form in *Maxwell's Equations in a Material Medium* above is the corpus's derivation; the modified system above and the objection that motivates it are recorded from the author's 2016 paper, and the corpus's own equation is not altered by them.

**A counter-claim, from a formulation arranged differently.** One external formulation claims the opposite outcome, and it belongs beside the modification. E. P. J. de Haas (*Biquaternion Formulation of Relativistic Tensor Dynamics*, arXiv:1401.4470v1, 2013) states that his biquaternion tensor calculus "lacks the extra terms that usually arise in biquaternionic electrodynamics", and he gives the condition in the body: the electromagnetic force biquaternion matches the standard field only if the **Lorenz gauge** holds, $F_0 = \tilde\partial_\nu A^\nu = 0$; off that gauge the usual biquaternion expressions for the Lorentz force and for the two inhomogeneous Maxwell equations carry extra terms which his arrangement does not, the terms arising from rearranging the tensor indices into biquaternion slots, an operation he calls external to his system. So the contrast with the $\alpha$-modification is exact and worth stating plainly: the corpus's own Maxwell equations, and the corpus's *Gauge Structure* section, are reached with no added scalar, and the gauge is fixed by construction; the modification adds a scalar to the A-field because the reduction is held to fail without it; and the counter-claim says the extra terms are an artefact of the mapping and the gauge rather than of the algebra. Both external positions are recorded, attributed, and neither alters the corpus's equation. The full accounting is in *Relativistic Mechanics in Biquaternionic Form* and *Curved Spacetime and the Biquaternion Framework*.

## The Biquaternionic Energy–Momentum

The energy and momentum of the electromagnetic field are encoded in a **biquaternionic energy–momentum**, the halved Hermitian form of the field strength:

$$
\tilde{W} = \frac{1}{2}\tilde{F}\tilde{F}^{*} = W + \frac{i}{c}\vec{S},
$$

where $W$ is the energy density and $\mathbf{S}$ is the energy flow density (the Poynting vector). For the electromagnetic field in a medium, these are

$$
W = \frac{1}{2}\left(\epsilon\,\mathbf{E}\cdot\mathbf{E} + \mu\,\mathbf{H}\cdot\mathbf{H}\right), \qquad \mathbf{S} = \mathbf{E}\times\mathbf{H}.
$$

The scalar part of $\tilde{W}$ is the energy density, real; the vector part is $(i/c)\mathbf{S}$, purely imaginary. The object is therefore an element of the Hermitian subspace $\mathbb{M}_+$, as every Hermitian form is, and the factor $i$ on the Poynting part is required: in the $ict$ convention a temporal component carries an $i$ relative to a spatial one, exactly as the scalar part of the source $\tilde{R}$ above is $i\rho/\sqrt{\epsilon}$ rather than $\rho/\sqrt{\epsilon}$. The form $\tilde{F}\tilde{F}^{*}$ is computed in *The Field-Strength Biquaternion and Its Invariants*; the factor $\tfrac{1}{2}$ is fixed by the requirement that the scalar part be the energy density. The energy–momentum **tensor** $T^{\mu\nu}$ is the source of the gravitational field in any theory that couples gravity to electromagnetism; $\tilde{W}$ carries its energy density and its energy flux.

The conservation of energy and momentum is expressed by the biquaternionic equation

$$
\tilde{\nabla} \tilde{W} = -\tilde{P},
$$

where $\tilde{P}$ is the biquaternionic power–force density, whose scalar part is $-\frac{i}{c}\,\mathbf{J}\cdot\mathbf{E}$ and whose vector part is $-(\rho\mathbf{E} + \mathbf{J}\times\mathbf{B})$. Taking the scalar part of the equation gives the standard energy conservation law

$$
\frac{\partial W}{\partial t} + \mathrm{div}\,\mathbf{S} + \mathbf{J}\cdot\mathbf{E} = 0.
$$

The energy–momentum tensor is the natural bridge between the electromagnetic field and the gravitational field. In the full complexified framework, the same structure appears in the gravitational sector, with the energy–momentum tensor playing the role of the source.

## Energy Conservation and the Cauchy Problem

The biquaternionic energy–momentum $\tilde{W} = \tfrac{1}{2}\tilde{F}\tilde{F}^{*} = W + (i/c)\mathbf{S}$ satisfies the conservation law $\tilde{\nabla} \tilde{W} = -\tilde{P}$, where $\tilde{P}$ is the biquaternionic power–force density. Integrating this law over a spacetime region $D$ with smooth boundary $\partial D$, and using the divergence theorem, gives

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

The argument closes under weaker hypotheses than differentiability. In Alexeyeva's treatment the **classical solution** is continuous and differentiable everywhere except on finitely many wave fronts, on which it satisfies the jump condition. The energy identity then holds with the surface terms included, because the jump of the energy integrand on each front vanishes by the shock article's energy-jump relation, whose electric-energy component is $[W]_{F_t} = c^{-1}(\mathbf{n},[\mathbf{P}]_{F_t})$. The energy integral is still positive-definite and time-independent, so the classical solution — **shock fronts included** — is unique. This is stronger than the finite-energy uniqueness above: the plain energy method presumes enough smoothness to apply the divergence theorem, whereas the distributional statement covers the discontinuous solutions that the shock article needs.

## The Lorentz Transformation of the Potential

The transformation of the four-potential under a Lorentz boost is the **rotor conjugation**

$$
\tilde{A}' = \tilde{\Lambda}\,\tilde{A}\,\tilde{\Lambda}^{*},
$$

where $\tilde{\Lambda}$ is the boost biquaternion. For a pure boost with velocity $\mathbf{u}$, the boost biquaternion is

$$
\tilde{\Lambda} = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\,\hat{\mathbf{u}} = \exp\!\left(\frac{\psi}{2}\,i\hat{\mathbf{u}}\right),
$$

with the rapidity $\psi$ related to the velocity by $\tanh\psi = u/c$, and $\hat{\mathbf{u}} = \mathbf{u}/u$ the unit vector in the direction of the boost. The Lorentz factor is

$$
\gamma = \frac{1}{\sqrt{1 - \mathbf{u}^2/c^2}} = \cosh\psi.
$$

The full development of the boost biquaternion, its relation to the four-velocity, and its action on the four-potential, is the subject of the companion article on the Lorentz transformation. Here we recall the resulting component formulas for the transformation of the scalar and vector potentials:

$$
\phi' = \gamma\left(\phi - \mathbf{u}\cdot\mathbf{A}\right),
$$

$$
\mathbf{A}' = \mathbf{A} + \frac{\gamma - 1}{u^2}(\mathbf{u}\cdot\mathbf{A})\mathbf{u} - \gamma\frac{\phi}{c^2}\mathbf{u}.
$$

These are the standard Lorentz transformation formulas for the four-potential, obtained from the rotor conjugation $\tilde{A}' = \tilde{\Lambda}\tilde{A}\tilde{\Lambda}^{*}$. The same transformation law applies to the biquaternionic source $\tilde{R}$ and to the biquaternionic energy–momentum $\tilde{W}$. This confirms that the biquaternionic formulation is Lorentz-covariant, and it shows how the transformation laws look in biquaternionic form.

**A note on earlier conventions.** An earlier version of this article used the one-sided formula $\tilde{A}' = (\gamma/c)\tilde{U}\tilde{A}$ with $\tilde{U} = c + i\mathbf{u}$. This formula is **incorrect**: it does not reproduce the standard component formulas for a general boost, and it does not match the rotor-conjugation formulation of the Lorentz transformation established in the companion articles. The correct transformation is the rotor conjugation given above.

## The Vacuum Limit

In vacuum, $\epsilon = \epsilon_0$ and $\mu = \mu_0$, and the speed of light becomes

$$
c_0 = \frac{1}{\sqrt{\epsilon_0 \mu_0}}.
$$

All the equations above carry over with the substitution $c \to c_0$, $\epsilon \to \epsilon_0$, $\mu \to \mu_0$. In particular, the field-strength biquaternion becomes

$$
\tilde{F} = i\sqrt{\epsilon_0}\,\mathbf{E} - \sqrt{\mu_0}\,\mathbf{H},
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

## The Field Bivector and the Field Operator

The corpus separates an **element** — a number — from an **operator** — a number with a slot to be filled. The group *Focus on Element Representations* develops the numbers and the group *Focus on Operator Representations* develops the operators, and the separation is not book-keeping: it decides which objects may be added to one another and which must be applied to an argument.

The Maxwell equation of this article is written with an **element**. The field strength $\tilde{F}=i\sqrt{\epsilon}\,\mathbf{E}-\sqrt{\mu}\,\mathbf{H}$ is a bivector, a number, and the equation $\tilde{\nabla}\tilde{F}=-\tilde{R}$ multiplies numbers. The electromagnetic **field tensor** is the associated **operator**: an object that takes a four-vector argument and returns a number, formed from the bivector and its order reverse. Gsponer and Hurni record its explicit form, in their notation, as

$$
F(\;) = \tfrac12\left([\;]\tilde{F} + \tilde{F}^{\sim}[\;]\right),
$$

where $[\;]$ marks the slot and $\tilde{F}^{\sim}$ is the order reverse of the bivector; the source attributes the distinction between the bivector $\tilde{F}$ and the operator $F(\;)$ to Kilmister, who drew it in 1955, and treats the two as objects that must not be confused.

The distinction matters because the field's derived quantities come with slots. The source writes the electromagnetic energy–momentum tensor as $4\pi T(\;)=\tfrac12\tilde{F}^{+}[\;]\tilde{F}$ and the Lorentz force density as a value of the tensor operator at the gradient, again with a slot. In the corpus's vocabulary the point is the element/operator one: the field-strength **number** is the subject of this article and of the companions on the field strength, while the **operator** built from it belongs to *The 4×4 Regular Matrix Operator Representation of Biquaternions*, *The Four-Vector Operator Representation of Biquaternions* and *Bilinear Operators on the Biquaternion Algebra with Hermitian Adjoint*. The corpus writes the Maxwell equation with the element and does not profit from the operator form; the source's warning is that the two must be told apart before either is used.

**One silent assumption.** The compact form also assumes that the potential is its own order reverse, $\tilde{A}=\tilde{A}^{\sim}$ — that is, that it is **ordinal invariant**. Splitting the equation into the parts that are even and odd under reversal, the reversal-even part is the field equation carrying the source and the reversal-odd part is the statement that there are no magnetic monopoles; both belong to the companion article *The Proca Equation: Massive Spin 1 in Biquaternionic Form*, and the second is the subject of *The Magnetic Monopole in Biquaternionic Form*. A reversal-odd potential is the case the same construction reads as a different field rather than as an electromagnetic one.

**The single-term form and spatial reversal.** Gsponer and Hurni record a caveat about the *writing* of the equation rather than about the field. The widely used quaternion form of Maxwell's second set carries a single term — the gradient of the field strength proportional to the current — and the source contrasts it with the two-term form in which the field equation is the reversal-symmetric half of a pair. The two agree only when the reversed term vanishes, and the source identifies that term with the monopole-free relation recorded above; the single-term form is therefore covariant under spatial reversal exactly when the potential and the current are reversion invariant, which is the ordinal-invariance assumption of the paragraph above, and not otherwise.

In the corpus's conventions the split is explicit, and it was checked. For a pure-vector field strength $\tilde{F}=\sum_k F_k e_k$ the two order-parities of $\tilde{\nabla}\tilde{F}$ are

$$
\tfrac12\left(\tilde{\nabla}\tilde{F}+\tilde{F}^{\sim}\tilde{\nabla}\right)=\mathrm{rot}\,\mathbf{F},
\qquad
\tfrac12\left(\tilde{\nabla}\tilde{F}-\tilde{F}^{\sim}\tilde{\nabla}\right)=\partial_{ict}\mathbf{F}-\mathrm{div}\,\mathbf{F}\,e_0,
$$

the first the spatial curl and the second a biquaternion whose scalar part is $-\mathrm{div}\,\mathbf{F}$ and whose vector part is $\partial_{ict}\mathbf{F}$; the second factor of each product is the reversed field strength acted on by the gradient from the right. The one-term equation $\tilde{\nabla}\tilde{F}=-\tilde{R}$ therefore fixes the *sum* of the two halves and neither half separately, and the second — the divergence half — is not identically zero: on a test field of mixed polynomial structure it has both a scalar and a vector part. So the compact equation is a statement about the sum; its spatial-reversal covariance rests on the two halves coinciding, and the source reads that coincidence as the monopole-free condition rather than as a property the writing inherits from the equation.

## Maxwell's Vacuum Equation as a Cauchy–Riemann Condition

The vacuum equation $\tilde{\nabla}\tilde{F}=0$ has a reading that is not a reformulation. Lanczos observed, in his 1919 thesis, that it is the direct **four-dimensional generalisation of the Cauchy–Riemann analyticity condition**: the pair of two-dimensional Cauchy–Riemann equations is replaced by the single biquaternion equation, and classical electrodynamics becomes a biquaternionic field theory of **regular** functions, in which the point singularities are read as electrons. The field at a point is then given by the generalisation of Cauchy's integral formula, an integral over a three-dimensional hypersurface $\Sigma$ surrounding the point,

$$
\tilde{F}(X) = \frac{-1}{2\pi^2}\int_\Sigma \frac{R}{|R|^4}\, d^3\Sigma\, \tilde{F}(Y),
\qquad R = Y-X, \quad |R|^2 = R\bar{R},
$$

in the source's notation. The function theory behind it — Fueter's for real quaternions (1932), later extended to biquaternions and higher-dimensional Clifford algebras — is the corpus's subject in *Fueter Theory for Biquaternions*, *Biquaternion Regular Functions*, *Biquaternion Analysis* and *Biquaternion Integration*, and the elliptic Cauchy kernel $\tilde{Q}^{\natural}/\|\tilde{Q}\|_E^4$ of the retarded-Green's-function section above is the kernel this reading is built on.

**The two kernel normalisations.** The factor $-1/2\pi^2$ here is the normalisation of the **Cauchy** kernel, and it does not conflict with the $1/4\pi^2$ of the fundamental solution of the d'Alembertian recorded in *Biquaternion Integration*, where $\Delta\|\tilde{Q}\|_E^{-2} = -4\pi^2\delta_0$. The two kernels are separated by one application of the Cauchy–Riemann operator, which lowers the degree by one: applied to the degree-$(-2)$ kernel $\|\tilde{Q}\|_E^{-2}$ it produces a degree-$(-3)$ kernel proportional to $\tilde{Q}\|\tilde{Q}\|_E^{-4}$, and the proportionality carries the factor $2$ that converts the $4\pi^2$ of the second-order kernel into the $2\pi^2$ of the first-order one. The Cauchy normalisation is fixed by the surface integral of the kernel, $\int_{S^3_r} n\,G\,dS = 1$ with $G = \tilde{Q}^{\natural}/(2\pi^2\|\tilde{Q}\|_E^4)$ and $n = \tilde{Q}/\|\tilde{Q}\|_E$, which has been checked directly. The two constants therefore belong to two kernels of two different orders, and there is no inconsistency between them.

What the reading adds to the equation is a **regularity** content for the vacuum half: the homogeneous Maxwell pair is the statement that the field is a regular biquaternionic function of the position, so the corpus's analysis machinery — the Cauchy formula, residues, contour deformation — is available for the source-free equations. The source records the reading as Lanczos's and as a reading of the classical theory; it changes no prediction, and it is the framework's most direct contact with the analytic side of the corpus.

**The same equation with the time written out.** The compact equation can be put in a form in which the time derivative stands alone, $i\partial_t\tilde{F} + D\tilde{F} = 0$ with $D$ the spatial part, and in that form it is the equation K. Imaeda formulated in 1976 as a new formulation of classical electrodynamics. The two writings differ only in how the four-gradient is split and in the signature conventions of the biquaternion units; both say that the vacuum field is annihilated by the four-dimensional Cauchy–Riemann operator. The form is worth recording because it is the one on which the separation of the time is performed — the fixed-frequency reduction of the next paragraph is exactly that separation applied to it — and because it is the massless member of the family of shifted equations that the dictionary of *The Dirac Equation in Biquaternionic Form* produces. Imaeda's paper carries the quaternionic vacuum Maxwell equation that the corpus here uses under the names of Conway, Silberstein and Lanczos, and it is recorded in the Further Reading below.

**The same equation at fixed frequency.** The reading above is four-dimensional. In the time-harmonic regime it degenerates to a three-dimensional one, and the object is the same. In the convention $e^{-i\omega t}$ of *Exercise: Plane-Wave Propagation in a Medium*, the temporal derivative $\partial_{ict}$ acts as $-\omega/c$ on a monochromatic field, so the vacuum equation $\tilde{\nabla}\tilde{F}=0$ becomes

$$
\Bigl(D_3-\frac{\omega}{c}\Bigr)\tilde{F}=0,
\qquad
D_3=e_1\partial_x+e_2\partial_y+e_3\partial_z,
\qquad
k=\frac{\omega}{c}=\omega\sqrt{\epsilon\mu},
$$

whose scalar part is the constraint $\mathrm{div}\,\mathbf{F}=0$. The field-strength biquaternion is therefore left regular for the **shifted** three-dimensional Cauchy–Riemann operator $D_3-k$ of *Quaternion Regular Functions*: four-dimensional regularity becomes Helmholtz–Dirac regularity in three dimensions, with the shift supplied by the frequency. The companion combination $\tilde{G}=i\sqrt{\epsilon}\mathbf{E}+\sqrt{\mu}\mathbf{H}$ is annihilated by $D_3+k$ instead, and the A-field $\mathcal{A}=-i\tilde{F}$ satisfies the same equation as $\tilde{F}$, so the electromagnetic field splits into two decoupled first-order equations — the diagonalization again, read from the four-dimensional side. The companion article works this out for a chiral medium, where the two shifts separate and become the two wavenumbers.

## The Internal Freedom of the Vacuum Field

The vacuum equation $\tilde{\nabla}\tilde{F}=0$ is Lorentz covariant: a change of frame acts on $\tilde{F}$ on the left, and left multiplication by the rotor is what the covariance means. Lanczos recorded, in the fourth chapter of the 1919 thesis, a **second** freedom, on the right, which the same equation possesses and which is not a change of frame. His equation (4.8) states that with $\tilde{F}$ the function $\tilde{F}\tilde{q}_0$ is also a solution, for any **constant** quaternion $\tilde{q}_0$ of unit norm:

$$
\tilde{\nabla}(\tilde{F}\tilde{q}_0) = (\tilde{\nabla}\tilde{F})\,\tilde{q}_0 = 0, \qquad N(\tilde{q}_0) = 1 .
$$

The proof is one line — the constant passes through the operator — and it has been checked directly: with $\tilde{q}_0$ a unit quaternion and $\tilde{F}$ a smooth biquaternion field, the residual of the identity is at the level of the finite-difference error. The set of such constants is the unit quaternions, a three-parameter group, which is $\mathrm{SU}(2)\cong\mathbb{H}^\times/\mathbb{R}$. In Lanczos's words the transformation of the versor $\tilde{F}$ is "not uniquely fixed at all" by the field equations: a rotation of the frame, with the two unit-quaternion characteristics $\tilde{p},\tilde{q}$, transforms the field as

$$
\tilde{F}' = \tilde{p}\,\tilde{F}\,\tilde{q}\,\tilde{q}_0 ,
$$

so the equations imply the left ($P$) transformation and leave the right ($Q$) transformation free up to the arbitrary constant factor $\tilde{q}_0$. Equivalently: **the homogeneous equations fix only the left action, and the solution space is a right module over the constants.**

**The Lorentz character of the field is not fixed by the equation.** The choice of $\tilde{q}_0$ decides which Lorentz object the field is, and the homogeneous Maxwell equations do not decide it. Lanczos distinguishes three cases. For the electromagnetic six-vector — the bivector field of the corpus's $\tilde{F}$ — the constant is the one that makes $\tilde{F}'$ transform as a six-vector; for a four-vector the constant is the other element, and Lanczos proposes that the field then be the gradient of a scalar potential, which he associates with gravitation; and the third case, which he did not take, is the one in which the field transforms as the simplest spinor, the massless spin-1/2 field. Gsponer and Hurni note that Lanczos had thus reached, in 1919, the freedom that contains the massless spin-1/2 field, nine years before Dirac, and that he returned to exactly this point after 1928, when he used the quaternion formalism to display the spacetime covariance of the spin-1 and spin-1/2 equations.

The corpus records the invariance and the three readings as the source's and the commentators'. What is structural is the statement of the freedom: the **vacuum Maxwell equation does not determine the spin content of its own solutions**; that is fixed by the constant $\tilde{q}_0$, an extra datum the equation leaves free. The three-parameter group of the freedom is the $\mathrm{SU}(2)$ that *The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)* identifies as the algebra's intrinsic compact group, reached here from the vacuum equation rather than from a gauge construction. The corpus does not adopt Lanczos's assignment of the four-vector case to gravitation; it records that the freedom exists, that its group is $\mathrm{SU}(2)$, and that the electromagnetic reading is the one member of the three that the rest of the corpus uses.

## Beyond the Minkowski Subspace: Complexified Spacetime

Up to this point, all biquaternions have been taken in the **anti-Hermitian subspace** $\mathbb{M}_-$ (the material sector), with $A_\mu = a_\mu + i a'_\mu$ and the constraint that the imaginary parts satisfy the reality conditions $a_0 = 0$, $a'_k = 0$ for the spatial components. In the full biquaternion algebra $\mathbb{B}$, the coefficients $A_\mu$ are arbitrary complex numbers, and the potential and field-strength biquaternions become **fully complexified**

$$
\tilde{A} = A_0 + \mathbf{A}, \qquad \tilde{F} = \mathbf{F},
$$

with complex coefficients that are not restricted to the anti-Hermitian subspace. The projection onto $\mathbb{M}_-$ reproduces the electromagnetic field; the remaining components correspond to the additional directions of the complexified spacetime.

The biquaternionic formulation extends naturally to this setting. The gradient $\tilde{\nabla}$ becomes an operator on the complexified coordinates, and the factorization $\Box = \tilde{\nabla} \tilde{\nabla}^{\natural}$ continues to hold, with $\Box$ now the complexified d'Alembertian. The single equation $\tilde{\nabla} \tilde{F} = -\tilde{R}$ remains valid, but the fields and sources are now fully complex. The integrability condition $\mathrm{Sc}(\tilde{\nabla}^{\natural} \tilde{R}) = 0$ remains the conservation law for the complexified source.

This is the natural generalization of the $ict$ structure. The electromagnetic field is the real projection of a complex field, just as the material sector $\mathbb{M}_-$ is a real slice of the complexified biquaternion algebra. The structure of Maxwell's equations is preserved, but the arena is larger.

## Summary

Maxwell's equations in a linear, isotropic, non-dispersive medium collapse into the single biquaternionic equation $\tilde{\nabla}\tilde{F} = -\tilde{R}$, where $\tilde{\nabla} = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z$ is the biquaternionic gradient, $\tilde{F} = i\sqrt{\epsilon}\,\mathbf{E} - \sqrt{\mu}\,\mathbf{H}$ is the field-strength biquaternion (the Riemann–Silberstein vector of Silberstein's 1907 construction, up to an overall factor), and $\tilde{R} = i\rho/\sqrt{\epsilon} + \sqrt{\mu}\,\mathbf{J}$ is the source biquaternion. One equation replaces the four standard Maxwell equations, and no explicit $\epsilon$ or $\mu$ appears, because the medium is carried entirely by the definitions of $\tilde{F}$ and $\tilde{R}$. The scalar and vector parts of the single equation reproduce the Hamiltonian form, $\mathrm{div}\,\mathbf{F} = R_0$ and $\partial_{ict}\mathbf{F} + \mathrm{rot}\,\mathbf{F} = -\mathbf{R}$. The d'Alembertian factors as $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \partial_{ict}^2 + \Delta$, and the conservation of electric charge is exactly the integrability condition $\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{R}) = 0$. The single equation is first order and eliminates no field, and that is the property the classical reduction to a second-order wave equation lacks: the reduced equation admits solutions, among them longitudinal ones, that violate the divergence constraints. At fixed frequency the same equation reduces to the shifted Cauchy–Riemann condition $(D_3-k)\tilde{F}=0$ together with its companion, and in a chiral medium the two shifts separate into the two wavenumbers and the two circular polarizations. The vacuum equation also carries an internal freedom beyond its Lorentz covariance: right multiplication by any constant unit quaternion leaves it invariant, a three-parameter $\mathrm{SU}(2)$ that the equation does not fix and that Lanczos read as the freedom selecting the Lorentz character of the field — the electromagnetic six-vector, a four-vector, or the massless spin-1/2 that he did not take.

The retarded Green's function supplies the causal solution, the field at a point depending only on the sources in its past light cone; it is the fundamental solution of the hyperbolic wave operator and is related by the Wick rotation to the elliptic Cauchy kernel $\tilde{Q}^{\natural}/\|\tilde{Q}\|_E^4$ used in biquaternion analysis. In the stationary limit the equation becomes purely spatial and the solution is the gradient of the Newton kernel, whose first term is Coulomb's law for a point charge and whose second is the Biot–Savart law. The same content in the complex-vector variable $\mathcal{A} = -i\tilde{F}$ — the dual field strength — has a **Green tensor** $U_{jk}$ rather than a scalar kernel, built from the wave function $\psi = (4\pi R)^{-1}\delta(t - R/c)$ and its time antiderivative; with it the Cauchy problem is unique even when the solution carries shock fronts. The potential $\tilde{A}$ is subject to the gauge transformation $\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma$, under which $\tilde{F}$ is invariant while the scalar $S = \mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{A})$ shifts by $S' = S - \Box\Gamma$; the Lorenz gauge $S = 0$ reduces the first-order equation to the wave equation $\Box\tilde{A} = -\mu\tilde{R}'$.

The energy and momentum of the field are carried by the halved Hermitian form $\tilde{W} = \tfrac{1}{2}\tilde{F}\tilde{F}^{*} = W + (i/c)\mathbf{S}$, an element of the Hermitian subspace $\mathbb{M}_+$ whose scalar part is the energy density $W$ and whose vector part is $(i/c)\mathbf{S}$, carrying the Poynting flux. It obeys the conservation law $\tilde{\nabla}\tilde{W} = -\tilde{P}$, which integrates to the biquaternionic Poynting theorem and gives uniqueness and stability of the Cauchy problem with finite energy. The four-potential transforms by rotor conjugation, $\tilde{A}' = \tilde{\Lambda}\tilde{A}\tilde{\Lambda}^{*}$, which reproduces the standard boost formulas for $\phi$ and $\mathbf{A}$ and exhibits the Lorentz covariance of the formulation. The vacuum limit is the substitution $\epsilon \to \epsilon_0$, $\mu \to \mu_0$, $c \to c_0$, leaving the structure of the equations unchanged; whether $c_0$ or the pair $(\epsilon_0,\mu_0)$ is fundamental is a structural question, not a settled one. Finally, the formulation extends to fully complexified coefficients, in which the electromagnetic field is the real projection of a complex field on the larger arena of complexified spacetime.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis |
| $i$ | Scalar imaginary, $i^2 = -1$, commutes with $e_k$ |
| $\mathbb{M}_-$ | Anti-Hermitian subspace (material sector) |
| $\mathbb{M}_+$ | Hermitian subspace (informational sector) |
| $\tilde{A}$ | Potential biquaternion |
| $\tilde{F}$ | Field-strength biquaternion |
| $\tilde{F}_\star = -i\tilde{F}$ | Dual field strength |
| $\mathcal{A} = -i\tilde{F} = \sqrt{\epsilon}\,\mathbf{E} + i\sqrt{\mu}\,\mathbf{H}$ | A-field (complex three-vector; not the potential) |
| $U_{jk}$ | Green tensor of the A-field equation |
| $\psi, \chi$ | Wave function $(4\pi R)^{-1}\delta(t - R/c)$ and its time antiderivative |
| $\tilde{R}, \tilde{R}'$ | Source biquaternions |
| $\tilde{W} = \tfrac{1}{2}\tilde{F}\tilde{F}^{*}$ | Energy–momentum biquaternion, in $\mathbb{M}_+$ |
| $\tilde{\Lambda}$ | Boost biquaternion (unit-norm biquaternion) |
| $\tilde{q}_0$ | Constant unit quaternion; the internal (right-multiplication) freedom of the vacuum equation, in $\mathrm{SU}(2)$ |
| $\tilde{\nabla}$ | Biquaternionic gradient |
| $\tilde{\nabla}^{\natural}$ | Quaternion conjugate gradient |
| $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural}$ | d'Alembertian |
| $\epsilon, \mu$ | Permittivity and permeability of the medium |
| $\epsilon_0, \mu_0$ | Permittivity and permeability of vacuum |
| $c = 1/\sqrt{\epsilon\mu}$ | **Speed of light in the medium** |
| $c_0 = 1/\sqrt{\epsilon_0\mu_0}$ | **Speed of light in vacuum** |
| $D_3 = e_1\partial_x+e_2\partial_y+e_3\partial_z$ | Three-dimensional Cauchy–Riemann operator (time-harmonic reading) |
| $F, F^*, cF$ | Real field matrices of the matrix formulation and their complexification, $cF := F - iF^*$ |
| $c\nabla$ | The operator matrix of the same formulation |
| $k = \omega\sqrt{\epsilon\mu}$ | Wavenumber in the medium at fixed frequency; shift of $D_3-k$ |
| $\mathbf{u}$ | Particle or frame velocity |
| $\langle\tilde{P},\tilde{Q}\rangle_{\natural}$ | the quaternion bilinear form, $\mathrm{Sc}(\tilde{P}^{\natural}\tilde{Q})$; on the diagonal $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=N(\tilde{Q})$ |
| $\langle\tilde{P},\tilde{Q}\rangle_{*}$ | the complex sesquilinear form, $\mathrm{Sc}(\tilde{P}\tilde{Q}^{*})$; on the diagonal $\langle\tilde{Q},\tilde{Q}\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$ |
| $\langle\tilde{P},\tilde{Q}\rangle$ | the complex bilinear form, the scalar part of the complex bilinear product, $\mathrm{Sc}(\tilde{P}\tilde{Q})$ |

## Further Reading

- Hermann Minkowski, "Space and Time" (1908), reprinted in *The Principle of Relativity* (Dover).
- Albert Einstein, *The Meaning of Relativity* (Princeton, 1922), for the $ict$ formulation of special relativity.
- James Clerk Maxwell, *A Treatise on Electricity and Magnetism* (Dover, 1954), for the original formulation.
- G. Rousseaux and É. Guyon, "À propos d'une analogie entre la mécanique des fluides et l'électromagnétisme", *Bulletin de l'Union des Physiciens* **96** (2002), no. 841 (2), 125–134, for the fluid–electromagnetism correspondence of *The Hydrodynamic Form of the Equations* — the Lamb vector, the Marmanis dictionary, the two Galilean limits and their fluid readings — and for the historical claim, recorded in *A Brief History of Biquaternions in Physics*, that the mechanical model of the field was the origin of the equations rather than an interpretation of them. An expository article in a teachers' journal, in French; cited for the analogy's content and its historical claims, not as primary literature.
- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the four-dimensional formulation.
- L. A. Alexeyeva, "Hamiltonian Form of the Maxwell Equations and Its Generalized Solutions", *Differential Equations* **39**(6) (2003) 807–816 (arXiv:0705.3153 is the Russian original), for the A-field, the Green tensor, and the shock-inclusive Cauchy theory.
- L. A. Alexeyeva, "Maxwell Equations, Their Hamiltonian and Biquaternionic Forms and Properties of Their Solutions", *Mathematical Journal* **16**(2) (2016) 90–103, ISSN 1682-0525, for the objection to the classical system, the $\alpha$-coupled Maxwell–Dirac system, the unclosed diagnosis, and the operator factorization.
- A. Waser, "Application of Bi-Quaternions in Physics" (2000, updated 2007), for the biquaternionic energy–momentum and the Lorentz transformation of the potential.
- A. W. Conway, "On the applications of quaternions to some recent developments of electrical theory", *Proceedings of the Royal Irish Academy* **29** (1911) 1–9, and L. Silberstein, "Quaternionic form of relativity", *Philosophical Magazine* **23** (1912) 790–809, for the compact biquaternionic Maxwell equation $\nabla\tilde{F}=-4\pi J$ used here.
- C. W. Kilmister, "The application of certain linear quaternion functions to tensor analysis", *Proceedings of the Royal Irish Academy* **57** (1955) 37–99, for the distinction between the electromagnetic field **bivector** and the field **operator** (tensor).
- D. H. Gottlieb, "Maxwell's equations" (1 August 2004, 12 pp.), for the matrix formulation compared in *A fourth route* above: the single complex matrix equation $cF(-\partial_t,\nabla)^{\mathsf T} = (\rho,\mathbf{J})^{\mathsf T}$, the dual form with the operator matrix $c\nabla$, the operator identities $c\nabla^2 = \Delta I$ and $(\partial_t I - c\nabla)(\partial_t I + c\nabla) = (\partial_t^2 - \Delta)I$, and the commutation of the field matrices with their conjugates. The paper's equations (13) and (14) are not reproduced here: their vector parts carry the term and sign defects recorded in *A fourth route*. The paper's $4 \times 4$ matrices are those of the second realization of *Biquaternion 4×4 Regular Matrix Element Representation*, where the transposition identity they satisfy is stated.
- C. Lanczos, "Die funktionentheoretischen Beziehungen der Maxwellschen Aethergleichungen — Ein Beitrag zur Relativitäts- und Elektronentheorie" (Budapest, 1919; reprinted in the *Collected Published Papers*, Vol. VI, A-1–A-82; English typescript arXiv:physics/0408079), for the reading of the vacuum Maxwell equation as the four-dimensional Cauchy–Riemann condition and the generalised Cauchy formula.
- K. Imaeda, "A new formulation of classical electrodynamics", *Il Nuovo Cimento B* **32** (1976) 138–162, for the quaternionic vacuum Maxwell equation $i\partial_tF+DF=0$, the form the compact equation takes when the time derivative is left explicit; the source of the time-harmonic dictionary of *The Dirac Equation in Biquaternionic Form* cites it in the massless case.
- R. Fueter, "Analytische Funktionen einer Quaternionenvariablen", *Commentarii Mathematici Helvetici* **4** (1932) 9–20, for the analytic function theory of regular quaternion functions.
- A. Gsponer and J.-P. Hurni, "The physical heritage of Sir W. R. Hamilton", arXiv:math-ph/0201058, §§6–7, for the operator/bivector distinction, the ordinal-invariance assumption, and the analytic reading of the vacuum equation.
- V. V. Kravchenko, "Quaternionic Diagonalization of Maxwell's Equations" (expository article, National Polytechnic Institute, Mexico City), for the objection to the wave-equation reduction, the diagonalization of the time-harmonic Maxwell system into first-order quaternionic equations, and the extendability problem.
- E. P. J. de Haas, "Biquaternion Formulation of Relativistic Tensor Dynamics," arXiv:1401.4470v1 [physics.gen-ph] (2013), for the counter-claim recorded after *The Author's Reading*: a biquaternion tensor calculus that reports no extra terms relative to the standard relativistic language, the condition being the Lorenz gauge. Cited for the negative claim and for the tensor-index rearrangement it identifies as the source of the extra terms.
- C. Castro and M. Pavšič, *The Extended Relativity Theory in Clifford Spaces* (review, 8 July 2004), for the extension of Maxwell theory to an arena whose coordinates are Clifford-valued polyvectors, where the potential is itself a polyvector, $A = \varphi + A_\mu\gamma^\mu + A_{\mu\nu}\gamma^\mu\wedge\gamma^\nu + \dots$, and the field strength $F = dA$ carries a symmetric and an antisymmetric part of every rank, so that an extended charge couples to antisymmetric tensor fields of arbitrary rank. The **formalism is standard** — $p$-form gauge fields and the coupling of extended objects to them are ordinary exterior calculus — while the reading of its scalar and pseudoscalar components as a dilaton and an axion is the review's suggestion ("one could attempt to identify"), and the arena is not this article's $\mathbb{B}$. It is listed because it is the widest generalization of the single equation recorded here.

