# __The Complex-Displaced Singularity and the Circle Electron__

## Introduction

In the biquaternion reading of electrodynamics, the vacuum Maxwell equation $\tilde{\nabla}\tilde{F}=0$ is the four-dimensional Cauchy–Riemann condition, and a charged particle is a **singularity** of the field rather than a source (*Maxwell's Equations in the Biquaternionic Formulation*, *Radiation from Accelerated Charges in Biquaternionic Form*). Lanczos, in the doctoral dissertation of 1919, took that reading one step further and asked a question that the source-free equation makes natural: if the field is a function of the biquaternionic position, what fixes the **position of the singularity**? Nothing in the vacuum equation does. The second half of his chapter on the electron as a singularity therefore perturbs the singularity's position off the material slice, into what he calls complexified space, and shows that the perturbation does not destroy the field theory — it replaces the point charge by a **ring**.

This article develops that construction in the corpus conventions. It is the one place in the corpus where a singularity is deliberately displaced off the material subspace $\mathbb{M}_-$, and it is the classical, linear counterpart of the **algebrodynamical ring**, which the corpus records on a nonlinear primary equation (*The Algebrodynamical Programme: Nonlinear Cauchy–Riemann Conditions, Self-Quantized Charge, and Induced Causal Geometry*). The two rings are different objects on different equations, and the contrast is drawn below.

The article is in three steps. It fixes the singular set of the displaced potential, which is a circle rather than a point. It reads the field of the ring, which acquires an intrinsic magnetic-type component that Gsponer and Hurni call **mesomagnetic**. And it records Lanczos's self-energy result, the finite difference of two separately divergent energies, which is the reason he believed the circle electron escaped the divergence of the point model. The result is a source claim of 1919, recorded here with the formula by which Lanczos reached it and with the numerical check of that formula.

## The Displaced Potential and Its Singular Set

### The Coulomb Kernel and the Position of the Singularity

In the stationary sector the field is carried by the scalar potential alone, and the four-potential is a material element with a purely imaginary scalar part,

$$
\tilde{A} = \frac{i\phi}{c}\,e_0 \in \mathbb{M}_-, \qquad \phi(\mathbf{x}) = \frac{q}{4\pi\epsilon}\,\frac{1}{\|\mathbf{x}-\mathbf{r}_0\|},
$$

where $\mathbf{r}_0$ is the position of the point charge, $\epsilon$ is the permittivity of the medium, and $\|\mathbf{x}\|$ is the ordinary Euclidean length of the vector part. The potential is singular on the set $\mathbf{x}=\mathbf{r}_0$, a single point, and it is the kernel $1/\|\mathbf{x}-\mathbf{r}_0\|$ whose geometry the construction uses; the charge and the permittivity enter only as the overall factor $q/4\pi\epsilon$ and are set aside below.

Lanczos introduces potential and field strength as **complex** quantities. If the potential is complex-valued, then in his reading there is no reason for the constants $(\xi,\eta,\zeta)$ that locate the singularity to be real, and the natural generalisation is to let them range over the complex numbers. A rotation and a translation of the coordinates bring the singularity to

$$
\xi = 0, \qquad \eta = 0, \qquad \zeta = -i\varrho, \qquad \varrho \in \mathbb{R}_{>0},
$$

so that the whole displacement of the singularity from the origin is

$$
\Delta\tilde{Q} = \zeta\,e_3 = -i\varrho\,e_3 .
$$

**The displacement is informational.** The element $-i\varrho e_3$ has a purely imaginary vector coefficient, so it is an element of the informational sector $\mathbb{M}_+$, and in that sector's own coordinates it is the displacement $z' = -\varrho$ along the third informational axis. Lanczos's phrase "displacing the electron into complexified space" is, in the corpus's terms, displacing the singularity along an **imaginary direction of the vector coefficient** — that is, along $\mathbb{M}_+$. The field points themselves remain material: they are the real elements $x\,e_1+y\,e_2+z\,e_3$, and the potential is evaluated on them. The construction therefore places the singularity in one sector and reads its field in the other.

### The Square of the Distance and the Ring

With $\mathbf{r}_0 = -i\varrho e_3$ the squared Euclidean separation is

$$
\|\mathbf{x}-\mathbf{r}_0\|^2 = x^2 + y^2 + (z+i\varrho)^2 = \bigl(x^2+y^2+z^2-\varrho^2\bigr) + 2i\,z\varrho ,
$$

a **complex** number, and the potential is the reciprocal square root of it,

$$
\phi(\mathbf{x}) = \frac{1}{\sqrt{\,x^2 + y^2 + (z+i\varrho)^2\,}} .
$$

The singular set is the zero set of the radicand. Writing the radicand as $A+iB$ with $A=x^2+y^2+z^2-\varrho^2$ and $B=2z\varrho$, the zero set is $A=0$ together with $B=0$. The second condition gives $z=0$, and with $z=0$ the first gives $x^2+y^2=\varrho^2$. Hence the singular set of the real coordinates is the **circle**

$$
\Gamma : \qquad z = 0, \qquad x^2 + y^2 = \varrho^2 ,
$$

a ring of radius $\varrho$ in the plane $z=0$, centred on the third axis. This is Lanczos's **circle electron**, *Kreiselektron*. A point singularity of the real potential has been opened into a ring by displacing its position into the informational sector. The radius of the ring is the magnitude of the imaginary part of the displacement, $\varrho=|\zeta|$, and the point electron is recovered in the limit $\varrho\to0$.

## The Branch Disk and the Two Sheets

The circle is not the only distinguished set. Because $\phi$ is built from a square root, the circle bounds a **branch disk** on which the two determinations of the root meet and the function fails to be single-valued:

$$
D : \qquad z=0, \qquad x^2+y^2 < \varrho^2 .
$$

Across the disk the square root reverses sign, so $\phi$ changes sign. On the disk itself the radicand is real and negative, $x^2+y^2-\varrho^2<0$, so the root is purely imaginary and $\phi$ is purely imaginary there; outside the ring, on the same plane, the radicand is real and positive and $\phi$ is real. The potential therefore interpolates, as the plane $z=0$ is crossed, between the real and the purely imaginary determinations, and the whole of the disk, and not only its boundary, is a locus of the multi-valuedness.

This is the point at which the two readings of the displacement differ. **In Lanczos's own reading** the sign change of $\phi$ is harmless for the field theory: the field strength $\tilde{F}$ is built from the potential by differentiation and changes sign in the same way, so the **product** of the potential and the field strength is continuous across the disk, and Lanczos integrates over the disk "above and below" and finds the contribution regular. The disk is thus a defect of the potential's single-valuedness and not of the field's regularity in his sense. **In the corpus's reading** the potential is a function on the biquaternion algebra, the displacement $\Delta\tilde{Q}$ is an element of $\mathbb{M}_+$, and the disk is the locus where the branch of the kernel must be chosen; the single-valued object is the field strength, not the potential, and the choice of branch is what a Cauchy-theoretic treatment would have to fix. In both readings the disk carries the branch structure and the circle carries the singularity.

The single-valued physical statement that survives is this: **the singular locus of the circle electron is the ring $\Gamma$, and the ring is thin — a line in space, not a surface.** The disk is a multi-valuedness of the potential, visible in the sign of the field strength but not a set on which the field strength itself diverges.

## The Field of the Ring: the Mesomagnetic Component

### The Field Strength Is Complex

Because the potential is complex, its gradient is complex, and the field of the configuration

$$
\mathbf{E}_\phi(\mathbf{x}) = -\mathrm{grad}\,\phi(\mathbf{x}) = -\bigl(\partial_x\phi\,e_1 + \partial_y\phi\,e_2 + \partial_z\phi\,e_3\bigr)
$$

has both a real and an imaginary part at every point off the ring and off the disk. Writing $\phi=\phi_R+i\phi_I$, the real part $-\mathrm{grad}\,\phi_R$ is the electric field of the configuration and the imaginary part $-\mathrm{grad}\,\phi_I$ is a second field that survives from the displacement into $\mathbb{M}_+$. The imaginary part is not an artefact of the bookkeeping: it is nonzero at generic points, as it must be whenever $\varrho\neq0$, and it vanishes identically at $\varrho=0$, where the point electron is recovered and the field is purely electric.

Away from the singular set the potential remains harmonic, since it is the analytic continuation of the harmonic Coulomb kernel in the parameter $\zeta$; each of the two parts $\phi_R,\phi_I$ therefore satisfies the three-dimensional Laplace equation separately, and the two fields are divergence- and curl-free where they are defined. The ring is the only singularity of the field. The check is direct: the Laplacian of $\phi$ computed by central differences at a hundred points off the ring is below $10^{-7}$, the level of the finite-difference error.

### Why the Second Field Is Mesomagnetic, Not Magnetic

An electric field that acquires an imaginary component under a displacement of the source looks at first like an electric field accompanied by a magnetic field, and Lanczos's calculation treats it that way: the second field of the displaced configuration is what supplies the compensating energy of the next section. Gsponer and Hurni record a correction that the corpus keeps with the claim. The second component is **not** an ordinary magnetic field. The magnetic field of electromagnetism is an axial vector, the field of a circulation, and it reverses under a space reflection while the electric field — a polar vector — does not. The imaginary component of the displaced field transforms as a **polar** vector, exactly as the electric field does, so it cannot be the magnetic field. Gsponer and Hurni name it a **mesomagnetic** field, and they note that the transformation properties of improper Lorentz transformations such as space reflection were not understood in 1919 and cannot be charged to Lanczos.

The corpus records both statements and keeps them apart. What is certain is the algebra: the displacement into $\mathbb{M}_+$ produces a second field whose transformation character differs from that of the ordinary magnetic field. Whether it is called magnetic, mesomagnetic, or a mere imaginary part of a complexified electric field is a question of physical interpretation that the algebra does not decide.

**The far field is the point field.** The mesomagnetic forces are appreciable only near the ring. At distances large compared with $\varrho$ the displacement is a small perturbation of the position, and the field of the circle electron differs from that of the point electron by a quantity that vanishes with $\varrho/\|\mathbf{x}\|$. The ring is invisible from far away.

## The Self-Energy: the Difference That Vanishes

### The Hamilton Function in the Stationary Field

Lanczos's reason for the construction is the self-energy. In the stationary field the density of the action integrand — his **Hamiltonian function** — is the difference of the electric and the magnetic energy densities. For a point electron the field is purely electric, and the self-energy integral of the Coulomb field diverges at the position of the charge: the energy of a point charge is infinite in the classical theory. For the circle electron the field is complex and carries the second, mesomagnetic component, and Lanczos finds that **the electric energy still diverges, but the mesomagnetic energy diverges in the opposite direction and cancels it**, so that the difference of the two tends to zero. The Hamiltonian function of the circle electron is therefore not necessarily infinite. This is the statement that the divergence of the point-charge self-energy is not forced by the field theory, but is a property of the point idealisation; moving the singularity into $\mathbb{M}_+$ removes it.

The electric and the mesomagnetic energies are each divergent at the ring, and the claim is about their difference. Lanczos computes the difference by a limiting procedure. Because of the symmetry about the third axis he works in the plane $y=0$ and multiplies by $2\pi\varrho$; he integrates over the disk "above and below" from the radius $\varrho-\varepsilon$ inward — that part contributes nothing, the product of the potential and the field strength being regular there — and then over a small torus of radius $\varepsilon$ threaded on the ring,

$$
\rho = \varrho + \varepsilon\cos\varphi, \qquad z = \varepsilon\sin\varphi ,
$$

where $\rho=\sqrt{x^2+y^2}$ and $\varphi$ is the azimuth, and lets $\varepsilon\to0$. The Hamiltonian function of the ring is then

$$
H = \frac{2\pi\varrho}{\varepsilon}\int_0^{2\pi} \frac{\varepsilon+\varrho\,(\cos\varphi+i\sin\varphi)}{\bigl[\varepsilon+2\varrho\,(\cos\varphi+i\sin\varphi)\bigr]^2}\,d\varphi .
$$

### The Vanishing of the Integral

The integral vanishes, and it vanishes for every $\varepsilon$ in the range $0<\varepsilon<2\varrho$ in which it is taken. The reason is elementary and is worth recording because it is the whole content of the self-energy claim. Setting $u=e^{i\varphi}$ turns the integral into a contour integral over the unit circle,

$$
\int_0^{2\pi}\frac{\varepsilon+\varrho e^{i\varphi}}{\bigl[\varepsilon+2\varrho e^{i\varphi}\bigr]^2}\,d\varphi
= \frac{1}{i}\oint \frac{\varepsilon+\varrho u}{u\,(\varepsilon+2\varrho u)^2}\,du ,
$$

whose integrand has a simple pole at $u=0$ and a double pole at $u=-\varepsilon/2\varrho$. For $\varepsilon<2\varrho$ both lie inside the contour. The residues are $+1/\varepsilon$ at $u=0$ and $-1/\varepsilon$ at $u=-\varepsilon/2\varrho$, and they cancel exactly, so the contour integral, and with it $H$, is zero. The cancellation of the two residues is the exact echo, at the level of the integral, of the cancellation of the electric and mesomagnetic energies at the level of the field: one divergent term and one oppositely divergent term, in the ratio that makes their difference finite, and in fact zero. The result has been recomputed here directly from the formula, by summing the integrand over a hundred equally spaced values of $\varphi$ for several $\varepsilon$ and $\varrho$: the integral is zero to machine precision, at the $10^{-16}$ level, in every case tried.

Two qualifications belong with the result. The vanishing is the statement of Lanczos's model at the level of the stationary field; it is not a derivation that the physical electron has zero electromagnetic mass. And the cancellation is exact only because the electric and mesomagnetic contributions are computed from the same complex potential, so that their divergences are tied together; a deformation of the model that breaks the complex structure — for instance a real deformation of the ring — would spoil it. The corpus records the result as the source's, with the formula, and does not promote it into a framework result.

### Relation to the Finite-Mass Programme

The circle electron is the static, singularity-side member of the family of constructions by which the Lanczos line confronts the self-energy divergence. The later programme of Gsponer and Hurni works on the **retarded** singularity and derives the standard action of electrodynamics from Lanczos's, finding a finite electromagnetic mass for a boundary tube of finite retarded radius; that result is recorded in *Radiation from Accelerated Charges in Biquaternionic Form*, together with its own limits. The two share the same structural move — the divergence is not assumed but traced to the idealisation — and differ in what is deformed: the retarded radius there, the position of the singularity here. Neither is the Abraham–Lorentz extended electron, and neither is a result of the corpus's own framework.

## Relation to the Algebrodynamical Ring

The corpus records a second ring-shaped electron, and the two must be kept apart.

| | Circle electron (Lanczos, 1919) | Algebrodynamical ring |
|---|---|---|
| Equation | linear vacuum Maxwell, $\tilde{\nabla}\tilde{F}=0$ | nonlinear primary Cauchy–Riemann system |
| Ring arises from | complex displacement of a point singularity into $\mathbb{M}_+$ | self-dual solution of the nonlinear system |
| Radius | free, equal to the imaginary displacement $\varrho$ | fixed by the equation, the admissible family $R_n$ |
| Charge | arbitrary | self-quantised, minimal value $|q|=\tfrac14$ |
| Gravity | none | Kerr–Newman metric, $g=2$ |

Both are classical models in which the electron is a ring rather than a point, and both are recorded in the corpus as external programmes rather than as results. The difference is the equation. Lanczos's ring lives on the **linear** Cauchy–Riemann equation, where the complex displacement is a symmetry of the equation and the ring is its image; the algebrodynamical ring lives on a **nonlinear, over-determined** primary equation, where the ring, the quantised charge and the induced metric are consequences of the nonlinearity. The linear ring has a free radius and no quantisation; the nonlinear ring has a fixed radius, a quantised charge and a metric. The corpus's linear framework reaches the first and is silent on the second, which is the boundary the algebrodynamical article states.

## Summary

Lanczos's circle electron is the displacement of a point singularity of the vacuum field off the material subspace $\mathbb{M}_-$ and into the informational sector $\mathbb{M}_+$. With the displacement $\Delta\tilde{Q}=-i\varrho e_3$, the singular set of the displaced Coulomb potential $\phi=1/\sqrt{x^2+y^2+(z+i\varrho)^2}$ is the ring $\Gamma: z=0$, $x^2+y^2=\varrho^2$, of radius equal to the magnitude of the imaginary displacement; the disk it bounds is a branch locus, not a second singularity, and the point electron is the limit $\varrho\to0$. The field of the ring is complex, carrying a second component that is polar under space reflection and that Gsponer and Hurni call mesomagnetic; it is appreciable only near the ring, and the far field is the point field.

The construction's purpose is the self-energy. In the stationary field the Hamiltonian function is the difference of the electric and the mesomagnetic energies; each diverges at the ring, and their difference does not. Lanczos's limiting integral over a small torus threaded on the ring vanishes, and the vanishing is the exact cancellation of the two residues of an elementary contour integral, $+1/\varepsilon$ at $u=0$ and $-1/\varepsilon$ at $u=-\varepsilon/2\varrho$. The result is a claim of the source's, checked here by direct quadrature to machine precision and recorded with the later retarded-radii programme of Gsponer and Hurni as the two sides of the same structural move. The corpus's own linear framework reaches the construction and does not endorse its physical reading; the ring on the nonlinear algebrodynamical equation is a different object, on a different equation, with different consequences.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\phi$ | Scalar potential; the displaced Coulomb potential $1/\sqrt{x^2+y^2+(z+i\varrho)^2}$, up to the charge factor |
| $\mathbf{r}_0 = -i\varrho e_3$ | Position of the singularity, displaced into the informational sector |
| $\Delta\tilde{Q} = -i\varrho e_3$ | The displacement itself; an element of $\mathbb{M}_+$ with $z'=-\varrho$ |
| $\varrho$ | Magnitude of the imaginary displacement; radius of the circle electron |
| $\Gamma$ | Singular set: the ring $z=0$, $x^2+y^2=\varrho^2$ |
| $D$ | Branch disk $z=0$, $x^2+y^2<\varrho^2$, where the square root changes sign |
| $\rho=\sqrt{x^2+y^2}$ | Cylindrical radius, used in the torus parametrisation |
| $\varphi$ | Azimuth on the torus threaded on the ring |
| $\rho=\varrho+\varepsilon\cos\varphi,\ z=\varepsilon\sin\varphi$ | Small torus threaded on the ring; the integration surface |
| $\varepsilon$ | Radius of the torus threaded on the ring (Lanczos's $\epsilon$, renamed to avoid the permittivity) |
| $H$ | Hamiltonian function (action density) of the ring; the difference of electric and mesomagnetic energy |
| $\mathbf{E}_\phi = -\mathrm{grad}\,\phi$ | Complexified electric field of the displaced configuration; real part electric, imaginary part mesomagnetic |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | Material and informational sectors |
| $\epsilon$ | Permittivity of the medium (Coulomb factor only) |

## Further Reading

- Cornelius Lanczos, *The Functional Theoretical Relationships of the Maxwell Aether Equations* (doctoral dissertation, Budapest, handwritten 1919; English typescript arXiv:physics/0408079), Chapter 7, *Das Kreiselektron*, for the displaced potential, the ring, the branch disk, and the vanishing Hamiltonian function of the ring.
- A. Gsponer and J.-P. Hurni, "Lanczos's Functional Theory of Electrodynamics: A Commentary on Lanczos's PhD Dissertation" (1998; arXiv:math-ph/0402012v2), for the reading of the complex displacement as a translation into complexified space, the finiteness of the self-energy for an imaginary translation, the mesomagnetic character of the imaginary field component, and the particle-spectrum remark.
- *Radiation from Accelerated Charges in Biquaternionic Form*, and the sources there, for the retarded-radii programme in which the standard action is derived from Lanczos's and the electromagnetic mass is finite for a boundary tube of finite retarded radius.
- *The Algebrodynamical Programme: Nonlinear Cauchy–Riemann Conditions, Self-Quantized Charge, and Induced Causal Geometry*, for the second ring, on a nonlinear primary equation, with its self-quantised charge and its Kerr–Newman metric.
- *Maxwell's Equations in the Biquaternionic Formulation*, for the reading of the vacuum equation as a four-dimensional Cauchy–Riemann condition and for the stationary limit whose Coulomb kernel is the starting point here.
- E. T. Newman, "Maxwell's equations and ideal null coordinates" and the complex-Minkowski-space literature, for the modern use of a complex shift of a real singularity; the construction above is the same displacement read as a map from a point to a ring rather than as a coordinate change.
