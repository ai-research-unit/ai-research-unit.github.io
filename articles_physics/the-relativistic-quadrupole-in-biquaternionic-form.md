# __The Relativistic Quadrupole in Biquaternionic Form__

## Introduction

A bounded distribution of charge has, in general, a **quadrupole moment**: the first moment above the dipole that is not a vector. In the non-relativistic theory it is a static, symmetric traceless rank-two tensor, and it is the leading correction to the field of an extended source once the charge and the dipole have been accounted for. What makes it a subject in its own right in the relativistic series is that none of those properties survives a boost unchanged. The quadrupole is not a four-vector, its components are not frame-independent, it is not a Lorentz scalar, and it is not even an element of the biquaternion algebra.

This article treats the quadrupole relativistically, in the biquaternion framework. Three questions organise the treatment.

First, **how does the quadrupole tensor of a source transform under a Lorentz boost?** The moment is a functional of the lab-frame charge distribution at a fixed time, and a boost changes both the shape of that distribution and the time slice on which it is read. The transformation is worked out below, and it has a non-trivial consequence: a **spherical** charge distribution, which has no quadrupole in its rest frame, acquires one when it is boosted, because the Lorentz contraction makes it oblate.

Second, **how does the quadrupole enter the retarded field and the radiation of a source?** The electric quadrupole is the leading radiation beyond the electric and magnetic dipoles, it falls off as $r^{-1}$ in the far zone with an angular pattern of degree two, and, together with the magnetic dipole, it is the first correction to the electric-dipole approximation. Its radiated power scales as the sixth power of the frequency.

Third, **where does the quadrupole sit in the algebra?** The moment does not sit in the algebra at all: as a representation of the rotation group it is the five-dimensional $D^{(2)}$, while the algebra carries only $D^{(0)}\oplus D^{(1)}$. The **field** it produces, however, is a biquaternion-valued function, and the algebra carries the field value at every point while the angular content of degree two lives in the field's dependence on position. Relativistically the two statements meet: a boost mixes the electric and magnetic multipoles, and at the level of the field the same boost mixes the two sectors of the field-strength biquaternion.

The article is classical throughout, and the scope is the *relativistic* quadrupole: the sources may move at arbitrary speed, retardation is kept, and the Lorentz transformation of the moments is part of the subject. The conventions are those of the foundational articles:

- Companion article *Introduction to the Biquaternion Universe*, for the algebra and its two sectors.
- Companion article *The Material Sector: Four-Vectors, Interval and Lorentz Action*, for the four-vectors and the material sector.
- Companion article *Conventions in the Biquaternion Universe*, for the metric (its three levels are ruled on in *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*), the d'Alembertian, and the conventions of presentation.
- Companion article *Maxwell's Equations in the Biquaternionic Formulation*, for the potential and field-strength biquaternions.
- Companion article *The Field-Strength Biquaternion and Its Invariants*, for $\tilde{F}$, the Riemann–Silberstein vector, and the self-dual decomposition.

Throughout, $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with basis $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ and $\vec e_\mu^2 = -e_t$; the central scalar imaginary is $i$, $i^2 = -1$; the material sector is $\mathbb{M}_-$ and the informational sector $\mathbb{M}_+$; the biquaternionic gradient is $\tilde{\nabla} = e_t\partial/\partial Q_t + \vec\nabla$ with $\vec\nabla = \vec e_x\partial/\partial Q_x + \vec e_y\partial/\partial Q_y + \vec e_z\partial/\partial Q_z$, and $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \partial^2/\partial Q_t^2 + \Delta$. The speed of light in the medium is $c = 1/\sqrt{\epsilon\mu}$. The irreducible rotation representation of dimension $2l+1$ is written $D^{(l)}$, so the monopole is $D^{(0)}$, the dipole and every vector is $D^{(1)}$, and the quadrupole is $D^{(2)}$.

## The Quadrupole as a Higher Multipole

### The Moment and Its Definition

Let a charge distribution of density $\rho(x_2\,\vec e_x+y_2\,\vec e_y+z_2\,\vec e_z)$ be confined to a bounded region. Its **quadrupole tensor** is

$$
\Theta_{ij} = \int \rho(x_2\,\vec e_x+y_2\,\vec e_y+z_2\,\vec e_z)\left(3x_{i,2}x_{j,2} - r_2^{\,2}\delta_{ij}\right)d^3x_2 .
$$

It is symmetric, $\Theta_{ij} = \Theta_{ji}$, and traceless, $\Theta_{ii} = 0$; those two conditions reduce the nine Cartesian entries to five. The tracelessness is not an extra assumption: the trace part is an $l=0$ contribution at the same $r^{-3}$ order, carries no quadrupole information, and is removed by the traceless definition. The five independent components are the representation $D^{(2)}$ of the rotation group, and it is useful to write them in the symmetric-traceless form the definition suggests:

$$
\Theta_{ij} \in \operatorname{Sym}^2_0(D^{(1)}) \cong D^{(2)} ,
\qquad
\dim_{\mathbb{C}} \operatorname{Sym}^2_0(D^{(1)}) = 5 .
$$

The quadrupole contributes to the potential of the source at the order $r^{-3}$,

$$
\Phi(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z) = \frac{1}{4\pi\epsilon_0}\left[\frac{ϙ}{r} + \frac{\vec p\cdot\vec u}{r^2} + \frac{1}{2r^3}\Theta_{ij}\vec u_i\vec u_j + \ldots\right],
$$

with $\vec u = (x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)/r$, $ϙ$ the total charge and $\vec p = \int\rho\,(x_2\,\vec e_x+y_2\,\vec e_y+z_2\,\vec e_z)\,d^3x_2$ the dipole moment. The term displayed is the exact quadrupole term of the Cartesian expansion, and it is a solid harmonic of degree two: it is $r_2^{\,2}P_2(\cos\gamma)$ continued to the field point.

### Why the Moment Is Not an Algebra Element

The biquaternion algebra, regarded as a module for the rotation group acting by rotor conjugation, decomposes as

$$
\mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B}) = D^{(0)} \oplus D^{(1)} ,
$$

the centre being the trivial representation and the vector part the vector representation. The reason is a dimension count: a four-dimensional complex space decomposes into representations of dimensions $1, 3, 5, \ldots$, and the only partitions of $4$ are $4 = 1 + 3$ and $4 = 1 + 1 + 1 + 1$. A $D^{(2)}$ alone would already require dimension five. More than that, the algebra cannot *reach* the quadrupole by multiplication either: the quaternion product of two vectors,

$$
\vec q\vec v = -\vec q\cdot\vec v + \vec q\times\vec v ,
$$

projects the Clebsch–Gordan sum $D^{(1)}\otimes D^{(1)} = D^{(0)}\oplus D^{(1)}\oplus D^{(2)}$ onto $D^{(0)}\oplus D^{(1)}$ and discards the symmetric traceless part, which is precisely what a quadrupole is.

The quadrupole is therefore a tensor over the vector part, not a value of the algebra. It is a functional of the source, an integral of the charge distribution, not a number that a field can take at a point. This is the distinction that organises the whole article: the **moment** is an object of the infinite-dimensional function space, and the **field** it produces is an algebra-valued function of position.

## The Retarded Field of a Localised Source

### The Retarded Potential and the Far Zone

The field of a moving source is obtained from the retarded potentials. For a point charge the Liénard–Wiechert potential is the standard result, and for an extended distribution the four-potential is the retarded integral

$$
\tilde{A}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,t') = \frac{\mu_0}{4\pi}\int \frac{[\tilde{J}(x_2\,\vec e_x+y_2\,\vec e_y+z_2\,\vec e_z,t'_r)]_{ret}}{|x\,\vec e_x+y\,\vec e_y+z\,\vec e_z-(x_2\,\vec e_x+y_2\,\vec e_y+z_2\,\vec e_z)|}\,d^3x_2 ,
\qquad
t'_r = t' - \frac{|x\,\vec e_x+y\,\vec e_y+z\,\vec e_z-(x_2\,\vec e_x+y_2\,\vec e_y+z_2\,\vec e_z)|}{c} ,
$$

with $\tilde{J} = ic\rho\,e_t + \vec J\in\mathbb{M}_-$ the four-current and the subscript *ret* denoting evaluation at the retarded time. This is the standard retarded solution, transcribed into the material sector; no biquaternion input is needed to write it, and none is used.

For a source with a single frequency $\omega$, the current is $\vec J(x_2\,\vec e_x+y_2\,\vec e_y+z_2\,\vec e_z,t') = \vec J(x_2\,\vec e_x+y_2\,\vec e_y+z_2\,\vec e_z)\exp(-i\omega t')$, and in the far zone $r = |x\,\vec e_x+y\,\vec e_y+z\,\vec e_z|\to\infty$ the retarded integral reduces to

$$
\vec A(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,t') = \frac{\mu_0}{4\pi}\,\frac{\exp(i(kr-\omega t'))}{r}\,\vec F(\vec u) ,
\qquad
\vec F(\vec u) = \int \vec J(x_2\,\vec e_x+y_2\,\vec e_y+z_2\,\vec e_z)\,\exp(-ik\vec u\cdot(x_2\,\vec e_x+y_2\,\vec e_y+z_2\,\vec e_z))\,d^3x_2 ,
$$

with the wavenumber $k = \omega/c$ and $\vec u = (x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)/r$. The whole angular and multipole content of the radiation is carried by the **radiation vector** $\vec F(\vec u)$, and the multipole expansion is the expansion of the phase factor in powers of $k\vec u\cdot(x_2\,\vec e_x+y_2\,\vec e_y+z_2\,\vec e_z)$:

$$
\vec F(\vec u) = \int\vec J - ik\int(\vec u\cdot(x_2\,\vec e_x+y_2\,\vec e_y+z_2\,\vec e_z))\vec J - \frac{k^2}{2}\int(\vec u\cdot(x_2\,\vec e_x+y_2\,\vec e_y+z_2\,\vec e_z))^2\vec J + \ldots
$$

Each successive term adds one order of $kr_2$ and one unit of angular momentum. The four-vector potential $\tilde{A}$ and the field-strength biquaternion $\tilde{F} = \tilde{\nabla}^{\natural}\tilde{A} - \mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{A})$ inherit this expansion term by term.

### The Decomposition of the First-Order Term

The zeroth term is the electric dipole. With the continuity equation $i\omega\rho = \mathrm{div}\,\vec J$, the integral of the current is the time derivative of the dipole moment,

$$
\int\vec J(x_2\,\vec e_x+y_2\,\vec e_y+z_2\,\vec e_z)\,d^3x_2 = -i\omega\,\vec p .
$$

The first-order term is the interesting one, because it carries two different multipoles at once. Write $S_{ij} = \int x_{i,2}J_j\,d^3x_2$. Separating $S$ into its symmetric and antisymmetric parts and using continuity, one finds the exact identities

$$
\tfrac{1}{2}\left(S_{ij}+S_{ji}\right) = -\frac{i\omega}{2}\,D_{ij} ,
\qquad
\tfrac{1}{2}\left(S_{ij}-S_{ji}\right) = \epsilon_{ijk}\,m_k ,
$$

where

$$
D_{ij} = \int\rho\,x_{i,2}x_{j,2}\,d^3x_2 ,
\qquad
\vec m = \frac{1}{2}\int (x_2\,\vec e_x+y_2\,\vec e_y+z_2\,\vec e_z)\times\vec J\,d^3x_2
$$

are the second moment of the charge and the magnetic dipole moment. The first identity follows from $\int\partial/\partial x_{k,2}(x_{i,2}x_{j,2}J_k)\,d^3x_2 = 0$, which gives $\int(x_{i,2}J_j + x_{j,2}J_i) = -i\omega\int x_{i,2}x_{j,2}\rho$, and the second is the definition of $\vec m$. Hence

$$
\int(\vec u\cdot(x_2\,\vec e_x+y_2\,\vec e_y+z_2\,\vec e_z))\vec J\,d^3x_2 = -\vec u\times\vec m - \frac{i\omega}{2}\,\vec D(\vec u) ,
\qquad
[\vec D(\vec u)]_i = D_{ij}n_j .
$$

The antisymmetric part is the **magnetic dipole**; the symmetric part is the **electric quadrupole**. Writing the traceless quadrupole as $\Theta_{ij} = 3D_{ij} - r_2^{\,2}\delta_{ij}\int\rho$ and dropping the trace, which is radial and radiates nothing, the two contributions to the radiation vector at first order are

$$
\vec F_{M1}(\vec u) = ik\,\vec u\times\vec m ,
\qquad
\vec F_{E2}(\vec u) = -\frac{k\omega}{6}\,\vec{\mathcal{Q}}(\vec u) ,
\qquad
[\vec{\mathcal{Q}}(\vec u)]_i = \Theta_{ij}n_j .
$$

The electric quadrupole and the magnetic dipole appear together at the same order in $k$, and this pairing is the reason the quadrupole is a relativistic subject. A boost that converts an electric dipole into a magnetic dipole converts an electric quadrupole into a magnetic quadrupole, so that the electric and magnetic types of a given order are tied together by the boost even though they enter the radiation vector at different orders.

## The Relativistic Transformation of the Quadrupole

### The Lab-Frame Moment of a Moving Source

Consider a source that is static in its rest frame $S_2$, with charge density $\rho_2(x_2\,\vec e_x+y_2\,\vec e_y+z_2\,\vec e_z)$ and quadrupole tensor $\mathcal{Q}_{2,ij}$, and let it move with velocity $\vec v$ in the lab frame $S$. At a fixed lab time, the lab density is the rest density contracted along the motion and scaled by the time-dilation factor,

$$
\rho(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z) = \gamma\,\rho_2\!\left(\gamma\,(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)_\parallel,\ (x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)_\perp\right) ,
\qquad
\gamma = \frac{1}{\sqrt{1-\beta^2}} ,
\qquad
\beta = \frac{|\vec v|}{c} ,
$$

where $(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)_\parallel$ and $(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)_\perp$ are the components of $x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ along and across $\vec v$. This is the Lorentz contraction read as a statement about the density at a fixed lab time, and it preserves the total charge, $\int\rho\,d^3x = \int\rho_2\,d^3x_2$.

The lab-frame quadrupole is the same functional of the lab density,

$$
\Theta_{ij} = \int\rho(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)\left(3x_ix_j - r^2\delta_{ij}\right)d^3x ,
$$

and it is automatically traceless. For a boost along the $z$-axis it evaluates, in terms of the rest-frame second moments $D_{2,ij} = \int\rho_2x_{i,2}x_{j,2}\,d^3x_2$, to

$$
\boxed{\;\Theta_{xx} = 2D_{2,xx} - D_{2,yy} - \frac{D_{2,zz}}{\gamma^2} ,
\qquad
\Theta_{yy} = 2D_{2,yy} - D_{2,xx} - \frac{D_{2,zz}}{\gamma^2} ,
\qquad
\Theta_{zz} = \frac{2D_{2,zz}}{\gamma^2} - D_{2,xx} - D_{2,yy}\;},
$$

$$
\Theta_{xy} = 3D_{2,xy} ,
\qquad
\Theta_{xz} = \frac{3D_{2,xz}}{\gamma} ,
\qquad
\Theta_{yz} = \frac{3D_{2,yz}}{\gamma} .
$$

The trace vanishes identically, as it must. The transformation is a linear map on the symmetric traceless tensors, and it is not a rotation: it rescales the longitudinal direction by $\gamma^{-1}$, which is exactly the statement that the moment is not a four-vector.

### The Lorentz-Contraction Quadrupole

The transformation has a consequence worth isolating. A rest-frame **sphere** has $D_{2,ij} = \tfrac{1}{3}T_2\delta_{ij}$ with $T_2 = \int\rho_2r_2^{\,2}d^3x_2$, and therefore $\mathcal{Q}_{2,ij} = 0$: it is a pure monopole. Under the boost it acquires

$$
\boxed{\;\Theta_{zz} = -\frac{2\beta^2}{3}\,T_2 ,
\qquad
\Theta_{xx} = \Theta_{yy} = +\frac{\beta^2}{3}\,T_2\;}
$$

an oblate quadrupole proportional to the square of the speed and to the source's mean-square radius. The result is purely kinematic and follows from the contraction of the slice on which the moment is measured; it is the tensor expression of the fact that a moving sphere is seen as an oblate spheroid. For a general rest-frame quadrupole the two effects add, and the longitudinal component reads

$$
\Theta_{zz} = \frac{2+\gamma^2}{3\gamma^2}\,\mathcal{Q}_{2,zz} - \frac{2\beta^2}{3}\,T_2 ,
$$

a boosted piece plus a contraction piece. The second piece is the reason the trace $T_2$ of the rest-frame second moment enters a formula for the quadrupole: it is not a multipole moment but the source's size, and the contraction converts size into quadrupole.

### The Covariant Reading

The transformation above shows that the electric quadrupole of one frame is a mixture of the electric and magnetic quadrupoles of another, and the same holds at every order: a boost mixes $E_l$ with $M_l$. The reason is structural. At the level of the field this is the mixing of the two sectors of the field strength, since a boost mixes $\vec E$ and $\vec B$, that is, the Hermitian and anti-Hermitian halves of $\tilde{F}$:

$$
\tilde{F}_2 = \tilde{U}^{\natural}\,\tilde{F}\,\tilde{U} ,
$$

with $\tilde{U}$ the boost biquaternion of $\mathbb{M}_+$. The two multipole types are parity classes — an electric $l$-pole has parity $(-1)^l$, a magnetic $l$-pole parity $(-1)^{l+1}$ — and a boost does not preserve parity, so it rotates the two types into one another. What it does leave alone is the chiral splitting: the two halves of the self-dual field strength are the two helicities, and they transform independently.

The **order** $l$ is a different matter, and here the boost does not behave simply. The order is a label of the angular decomposition in a fixed frame; the rotation subgroup preserves it, but a boost does not. The reason is that a boost acts on the field in two ways at once — it mixes the field components **and** it transforms the argument, so the field is read on another time slice and at an aberrated direction — and a pure multipole of one frame therefore acquires other orders in another. The quadrupole is its own illustration. Its rest-frame potential is the degree-two solid harmonic $\Phi \propto (3z^2-r^2)/r^5$, and a boost along $z$ turns it into

$$
\Phi_2(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)\big|_{r=1}\ \propto\ \frac{(2\gamma^2+1)u^2-1}{\left(1+(\gamma^2-1)u^2\right)^{5/2}} ,
\qquad
u = \cos\theta_2 ,
$$

which is no longer a polynomial of degree two in $u$: its angular content is $l = 2,4,6,\ldots$ rather than $l=2$ alone, with the $l=2,4,6$ weights $1.13$, $0.78$ and $0.33$ at $\gamma = 1.5$. The multipole order is therefore not a Lorentz-invariant label. It is defined in the source's rest frame, and the covariant packaging of the moments is the covariant multipole tensor; on the field side the covariant object is the self-dual field strength, whose two chiral halves are the two helicities.

For the dipole the mixing is classical and explicit. A charge distribution translating with velocity $\vec v$ has current $\vec J = \rho\vec v$, so its magnetic moment is

$$
\vec m = \frac{1}{2}\int(x_2\,\vec e_x+y_2\,\vec e_y+z_2\,\vec e_z)\times\vec J\,d^3x_2 = \frac{1}{2}\,\vec p\times\vec v ,
$$

a magnetic dipole proportional to the electric dipole and the velocity: the moving electric dipole is a magnetic dipole. The quadrupole analogue is that a moving electric quadrupole carries a magnetic quadrupole moment, and a static magnetic quadrupole in turn contributes to the electric quadrupole of the moving frame. In the algebra this is the statement that a boost rotates the Hermitian and anti-Hermitian halves of the field-strength biquaternion into one another: the electric half of $\tilde{F}$ is Hermitian and the magnetic half anti-Hermitian, and the conjugation that implements a boost does not preserve the split.

## The Quadrupole Field and Its Radiation

### The Near Zone

In the near zone the quadrupole field is the gradient of the quadrupole potential, and it falls off as $r^{-4}$:

$$
\vec E_{quad}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z) = -\vec\nabla\Phi_{quad} ,
\qquad
\Phi_{quad}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z) = \frac{1}{4\pi\epsilon_0}\,\frac{1}{2r^3}\Theta_{ij}\vec u_i\vec u_j .
$$

This field is not a radiation field: it has no $r^{-1}$ part, and its Poynting flux integrates to zero over a large sphere. It is the static, or quasi-static, quadrupole field, the relativistic correction to the near field of a slowly moving source.

### The Electric Quadrupole Radiation

In the far zone the electric quadrupole produces a genuine radiation field. From the radiation vector computed above, $\vec F_{E2} = -\tfrac{k\omega}{6}\vec{\mathcal{Q}}(\vec u)$, and $\vec B = ik\,\vec u\times\vec A$ in the radiation zone, one obtains

$$
\vec B_{E2}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,t') = -\frac{\mu_0}{4\pi}\,\frac{\exp(i(kr-\omega t'))}{r}\,\frac{ik^2\omega}{6}\,\vec u\times\vec{\mathcal{Q}}(\vec u) .
$$

The field is transverse, falls off as $r^{-1}$, and carries the angular dependence of degree two through the vector $\vec{\mathcal{Q}}(\vec u)$. The time-averaged angular distribution follows from the Poynting vector $\langle\vec S\rangle = \tfrac{r^2c}{2\mu_0}|\vec B|^2\vec u$:

$$
\frac{dP_{E2}}{d\Omega} = \frac{\mu_0\,\omega^6}{1152\,\pi^2c^3}\,\left|\vec u\times\vec{\mathcal{Q}}(\vec u)\right|^2 .
$$

The angular integral of the numerator is a fixed multiple of the invariant $\Theta_{ij}\Theta_{ij}$,

$$
\oint\left|\vec u\times\vec{\mathcal{Q}}(\vec u)\right|^2d\Omega = \frac{4\pi}{5}\,\Theta_{ij}\Theta_{ij} ,
$$

a consequence of the tracelessness of $\mathcal{Q}$ and of the elementary angular averages $\oint n_in_j\,d\Omega = \tfrac{4\pi}{3}\delta_{ij}$ and $\oint n_in_jn_kn_l\,d\Omega = \tfrac{4\pi}{15}(\delta_{ij}\delta_{kl}+\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk})$. The total radiated power is therefore

$$
\boxed{\;P_{E2} = \frac{\mu_0\,\omega^6}{1440\,\pi\,c^3}\,\Theta_{ij}\Theta_{ij}
= \frac{1}{4\pi\epsilon_0}\,\frac{1}{180\,c^5}\,\langle \,d^3Q_{ij}/d{t'}^3 d^3Q_{ij}/d{t'}^3\rangle\;}
$$

where the second form is the standard one, and the two agree because a harmonic quadrupole $\Theta_{ij}\cos\omega t'$ has $\langle\,d^3Q_{ij}/d{t'}^3 d^3Q_{ij}/d{t'}^3\rangle = \tfrac{1}{2}\omega^6\Theta_{ij}\Theta_{ij}$. This is the standard long-wavelength electric-quadrupole result, reconstructed here from the radiation vector; the sixth power of the frequency is the reason each successive multipole is harder to excite.

For an axisymmetric source, $\Theta_{ij} = \mathrm{diag}(-\tfrac{1}{2}ϙ,-\tfrac{1}{2}ϙ,ϙ)$ with $ϙ = \Theta_{zz}$, the angular distribution is the degree-two pattern

$$
\frac{dP_{E2}}{d\Omega} = \frac{\mu_0\,\omega^6}{1152\,\pi^2c^3}\cdot\frac{9}{4}\,ϙ^2\sin^2\!\theta\cos^2\!\theta ,
$$

proportional to $\sin^2 2\theta$, with the nulls on the axis and in the equatorial plane and maxima at $\theta = \pi/4$ and $3\pi/4$. The pattern is the field-space image of the corresponding solid harmonic.

### The Magnetic Quadrupole

The magnetic quadrupole is the companion of the electric quadrupole at the same angular order $l=2$, and it is built from the antisymmetric current structure one order higher in $k$. Its far field has the same $r^{-1}$ fall-off and the same power law, with the magnetic quadrupole moment in place of the electric one, and its parity is opposite: an electric $l$-pole has parity $(-1)^l$, a magnetic $l$-pole parity $(-1)^{l+1}$. The magnetic quadrupole therefore contributes to the same $D^{(2)}$ angular structure with the opposite behaviour under parity, and the two types are mixed by a boost, as the transformation derived above shows.

### Angular Momentum and the Spin-1+ Origin

Each multipole order carries a definite angular momentum. The electric and magnetic $l$-poles radiate quanta of total angular momentum $j = l$, with the multipole moment transforming as a rank-$l$ tensor operator; a quadrupole transition therefore emits a quantum of $j = 2$. This is what places the effect in the sector of **spin-one-and-above origin**. The lowest multipole is the electric dipole, a rank-one object; the quadrupole is rank two; and at each order the rank-$l$ moment is built from $l$ vector (spin-one) ingredients, so the quadrupole is the first multipole that requires the coupling of two spin-one objects. In the framework the same ceiling appears algebraically: the algebra's own tensor operators reach rank one, because $\mathbb{B}$ contains only $D^{(0)}$ and $D^{(1)}$, and the rank-two operator is built in a tensor power — by the Clebsch–Gordan coupling $1\otimes1\to2$ — rather than inside a single factor.

For radiation the angular momentum is carried jointly by the multipole order and the vector character of the field. The field strength is a vector, hence a spin-one object, and the radiated quantum of an $l$-pole has $j = l$, one unit of which reflects the spin-one character of the field in which the multipole is written. This is why the electric quadrupole is often described as a two-unit angular-momentum transition, in which one unit is the vector character of the field and the other the multipole order itself.

## The Quadrupole in the Algebra

### The Field Value and the Angular Content

The resolution of the apparent paradox — that the quadrupole is not an algebra element yet its field is biquaternion-valued — is the separation of two spaces. At each point of space–time the field strength takes a value in the algebra,

$$
\tilde{F}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,t') = i\sqrt{\epsilon}\,\vec E(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,t') - \sqrt{\mu}\,\vec H(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,t') \in \mathrm{Vect}(\mathbb{B}) ,
$$

a pure-vector biquaternion, and the **value** is an element of the six-real-dimensional vector part, which as a rotation module is $D^{(1)}$. The **angular content** of the field, however, is a property of the function $\tilde{F}(\cdot,t')$, living in the infinite-dimensional space of functions on the sphere, and it is that space which contains the $D^{(2)}$ of the quadrupole. The quadrupole field is a vector-valued function whose components depend on the angles through degree-two harmonics; the value at a point is spin one, while the angular map is spin two. There is no contradiction, because the two belong to different spaces: the value algebra is finite, the function space is not.

The same separation explains the fate of the quadrupole under the algebra's own operations. The product of two field values, or the composition of two gradients, discards the symmetric traceless part — the quaternion product keeps only $D^{(0)}\oplus D^{(1)}$, and $\vec\nabla\vec\nabla = -\Delta\,e_t$ keeps only the trace — so no local algebraic operation performed on the field at a point can manufacture a quadrupole. What produces the quadrupole is the integration against the source, that is, the *retarded solution*, which is a non-local operation; and the angular degree two is produced by the source's angular structure, not by the multiplication of values.

### The Two Decompositions

Two algebraic decompositions of $\tilde{F}$ organise the multipole series, and both are visible already at the quadrupole.

The **Hermitian decomposition** separates the electric and magnetic halves,

$$
\tfrac{1}{2}\left(\tilde{F}+\tilde{F}^{*}\right) = i\sqrt{\epsilon}\,\vec E\in\mathbb{M}_+ ,
\qquad
\tfrac{1}{2}\left(\tilde{F}-\tilde{F}^{*}\right) = -\sqrt{\mu}\,\vec H\in\mathbb{M}_- .
$$

The electric and magnetic quadrupole **fields** are the two summands. For a static source the correspondence with the quadrupole types is exact — a static charge distribution gives a purely Hermitian field strength, so the electric quadrupole field is Hermitian, and a stationary current gives a purely anti-Hermitian one, so the magnetic quadrupole field is anti-Hermitian. A radiating quadrupole of either type has both a Hermitian and an anti-Hermitian part. A boost does not preserve this split: it mixes the electric and magnetic fields. The same boost mixes the multipole types, and that is a statement about parity rather than about the two fields: $E_2$ and $\mathsf{M}_2$ have opposite parity, and a boost does not preserve parity.

The **self-dual decomposition** combines the two halves into the two chiralities,

$$
\tilde{F} = i\sqrt{\epsilon}\,\vec N ,
\qquad
\tilde{F}^{*} = i\sqrt{\epsilon}\,\vec N^* ,
\qquad
\vec N = \vec E+ic\vec B ,
\qquad
\vec N^* = \vec E-ic\vec B ,
$$

with $\vec N$ the self-dual and $\vec N^*$ the anti-self-dual combination; for the real field the dagger produces the second from the first, since $\tilde{F}^{*} = i\sqrt{\epsilon}\,\vec E+\sqrt{\mu}\,\vec H = i\sqrt{\epsilon}\,\vec N^*$. The self-dual half transforms independently under the Lorentz group, in one of its two complex three-dimensional representations; this is the object that a boost rotates as a whole, and the two chiral halves it defines are the two helicities of the radiation. The decomposition of the full multipole series along these two halves is the general problem of higher multipoles.

### The Radiation Field as a Zero Divisor

A quadrupole radiation field has one further algebraic property that is worth recording. In the far zone the field is transverse and electric–magnetic balanced, $\vec E\cdot\vec B = 0$ and $|\vec E| = c|\vec B|$, so both Lorentz invariants vanish,

$$
I_1 = \vec E^2 - c^2\vec B^2 = 0 ,
\qquad
I_2 = \vec E\cdot\vec B = 0 ,
\qquad
\langle\tilde{F}\rangle_{\natural} = \tilde{F}\tilde{F}^{\natural} = 0 .
$$

The field-strength biquaternion of a radiation field is therefore a **zero divisor** of $\mathbb{B}$: the quadrupole radiation field, like every radiation field, is null. The near-zone quadrupole field is not, and the transition between the two is the transition from the non-null field of a bound source to the null field of its radiation.

## Summary

The relativistic quadrupole is the first multipole above the dipole, and it differs from the dipole in every way that a boost can reveal.

Its tensor is symmetric and traceless, $\Theta_{ij} = \int\rho(3x_{i,2}x_{j,2}-r_2^2\delta_{ij})d^3x_2$, five components transforming as $D^{(2)}$. Under a boost along the motion, the lab-frame tensor of a source that is static in its rest frame is

$$
\boxed{\;\Theta_{xx} = 2D_{2,xx}-D_{2,yy}-\frac{D_{2,zz}}{\gamma^2} ,
\quad
\Theta_{zz} = \frac{2D_{2,zz}}{\gamma^2}-D_{2,xx}-D_{2,yy} ,
\quad
\Theta_{xy} = 3D_{2,xy} ,
\quad
\Theta_{xz} = \frac{3D_{2,xz}}{\gamma}\;},
$$

with $\Theta_{yy}$ following from the trace condition. A rest-frame sphere acquires the oblate contraction quadrupole $\Theta_{zz} = -\tfrac{2}{3}\beta^2T_2$, $\Theta_{xx} = \Theta_{yy} = +\tfrac{1}{3}\beta^2T_2$, proportional to the mean-square radius $T_2 = \int\rho_2r_2^{\,2}d^3x_2$.

In the radiation problem the electric quadrupole appears at first order in $k$ together with the magnetic dipole, and the two are the symmetric and antisymmetric parts of one current moment. The quadrupole radiation vector is $\vec F_{E2} = -\tfrac{k\omega}{6}\vec{\mathcal{Q}}(\vec u)$; the far field is transverse and falls off as $r^{-1}$; the angular distribution is

$$
\frac{dP_{E2}}{d\Omega} = \frac{\mu_0\omega^6}{1152\pi^2c^3}\left|\vec u\times\vec{\mathcal{Q}}(\vec u)\right|^2 ,
$$

and the total power is $P_{E2} = \tfrac{\mu_0\omega^6}{1440\pi c^3}\Theta_{ij}\Theta_{ij} = \tfrac{1}{4\pi\epsilon_0}\tfrac{1}{180c^5}\langle\,d^3Q_{ij}/d{t'}^3 d^3Q_{ij}/d{t'}^3\rangle$, the standard result, scaling as the sixth power of the frequency.

The quadrupole moment is not an algebra element: it is a rank-two tensor, outside the algebra's rotation content $\mathbb{B} = D^{(0)}\oplus D^{(1)}$. The field it produces is nonetheless a biquaternion-valued function; the value is spin one and the angular content lives in the function space, so the finite algebra carries the field at each point while the function space carries the multipole order. Relativistically the electric quadrupole and the magnetic quadrupole mix under boosts: a boost mixes the electric and magnetic fields, that is, the Hermitian and anti-Hermitian halves of $\tilde{F}$, and — for a separate reason, the failure of parity conservation — it rotates the two quadrupole types into one another, while the two chiral halves of the self-dual combination, the two helicities, are left alone. Finally, a quadrupole radiation field is null, so its field-strength biquaternion is a zero divisor.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_\mu^2 = -e_t$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{C}_{\mathbb{B}}, \mathrm{Vect}(\mathbb{B})$ | Centre and complex vector part of $\mathbb{B}$ |
| $\tilde{\nabla} = e_t\partial/\partial Q_t+\vec\nabla$ | Biquaternionic gradient |
| $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \partial^2/\partial Q_t^2+\Delta$ | d'Alembertian (series convention) |
| $\tilde{A} = i\phi/c\,e_t+\vec A$ | Four-potential, an element of $\mathbb{M}_-$ |
| $\tilde{F} = i\sqrt{\epsilon}\,\vec E-\sqrt{\mu}\,\vec H$ | Field-strength biquaternion (pure vector) |
| $\vec N = \vec E+ic\vec B$ | Riemann–Silberstein vector, $\tilde{F} = i\sqrt{\epsilon}\,\vec N$ |
| $\vec N^* = \vec E-ic\vec B$ | Anti-self-dual combination, $\tilde{F}^{*} = i\sqrt{\epsilon}\,\vec N^*$ for the real field |
| $\rho$, $\vec J$ | Charge and current densities |
| $ϙ$, $\vec p$, $\vec m$ | Monopole, dipole and magnetic dipole moments |
| $D_{ij} = \int\rho\,x_ix_j\,d^3x$ | Second moment of the charge |
| $\Theta_{ij} = \int\rho(3x_{i,2}x_{j,2}-r_2^2\delta_{ij})d^3x_2$ | Quadrupole tensor (symmetric traceless) |
| $T_2 = \int\rho_2\,r_2^{\,2}d^3x_2$ | Trace of the rest-frame second moment |
| $\vec D(\vec u)$, $\vec{\mathcal{Q}}(\vec u)$ | $D_{ij}n_j$, $\Theta_{ij}n_j$ |
| $\Phi_{quad}$ | Quadrupole potential |
| $\vec F(\vec u) = \int\vec J\,\exp(-ik\vec u\cdot(x_2\,\vec e_x+y_2\,\vec e_y+z_2\,\vec e_z))d^3x_2$ | Radiation vector |
| $E_l$, $M_l$ | Electric and magnetic multipoles of order $l$ |
| $D^{(l)}$ | Irreducible rotation representation of dimension $2l+1$ |
| $k = \omega/c$ | Wavenumber |
| $\vec u = (x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)/r$ | Unit radial vector |
| $\gamma$, $\beta = |\vec v|/c$ | Lorentz factor and speed ratio |
| $\tilde{U}\in\mathbb{M}_+$ | Boost biquaternion, $\tilde{F}_2 = \tilde{U}^{\natural}\tilde{F}\tilde{U}$ |
| $\star$ | Hodge dual, $\star(\vec E,\vec B) = (c\vec B,-\vec E/c)$ |
| $\langle\tilde{F}\rangle_{\natural} = \tilde{F}\tilde{F}^{\natural}$ | Biquaternion norm; vanishes for a radiation field |

## Further Reading

- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for the Liénard–Wiechert potentials, the multipole expansion of the radiation field, and the electric-quadrupole power formula.
- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the retarded potentials and the long-wavelength radiation of an oscillating multipole.
- S. R. de Groot and L. G. Suttorp, *Foundations of Electrodynamics* (North-Holland, 1972), for the covariant multipole expansion of the charge-current distribution.
- M. E. Rose, *Elementary Theory of Angular Momentum* (Wiley, 1957), for the irreducible representations $D^{(l)}$ and the multipole moments as tensor operators.
- A. R. Edmonds, *Angular Momentum in Quantum Mechanics* (Princeton, 1957), for the Clebsch–Gordan coupling and the classification of multipole radiation.
- W. Heitler, *The Quantum Theory of Radiation* (Oxford, 1954), for the electric and magnetic multipoles of a radiating source and their angular momentum.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time* (Cambridge, 1984), for the self-dual and anti-self-dual decomposition of the field tensor.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the quaternion product rule and the representation content of the algebras used here.
