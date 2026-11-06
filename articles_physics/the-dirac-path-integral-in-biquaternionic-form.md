# __The Dirac Path Integral in Biquaternionic Form__

## Introduction

The path integral is the third formulation of quantum physics, alongside the operator formulation and the wave-equation formulation. For a particle of spin $\tfrac12$ it presents a difficulty that the scalar case does not: the Dirac operator is first order, and a path integral whose phase is a sum over a Lagrangian is naturally a device for a **second-order** operator. The history of the subject is the history of two complementary resolutions of that difficulty. Feynman's original "checkerboard" builds the first-order structure into a discrete lattice of directed paths. The proper-time and worldline formulation applies the first-order operator to a scalar path integral, or generates it from an additional **odd** degree of freedom on the worldline.

This article develops the biquaternionic interpretation of both. The square of the biquaternionic Dirac operator is the d'Alembertian — the companion article *Klein–Gordon from the Dirac Square in Biquaternionic Form* derives it — so the Dirac propagator is obtained from the scalar path integral by applying the first-order operator. The spin is carried by an integral over an odd variable for a reason the algebra states in one line: a single odd variable is not an element of $\mathbb{B}$ and a pair of them is, because the algebra has no odd part, and the even part of the envelope is the algebra itself. The two statements are the two halves of one algebraic fact. The derivative term is one element of the algebra and the spin weight is another, and the first order of the equation is the pairing of the two.

Three boundaries are respected. The Klein–Gordon **path integral** and the scalar propagator belong to the spin-$0$ subcategory and are cited, not re-derived. The **spin-half path integral** and the **fermionic field path integral** are different objects: the former is the non-relativistic spinning path integral and the latter is the quantised-field integral belonging to *Biquaternion Quantum Fields*; neither is the single-particle Dirac path integral treated here. The general apparatus of the d'Alembertian and its Green's functions belongs to *the generalities*.

**The conventions are the series conventions, and they are cited here and not developed.** The algebra, its four units and the central scalar imaginary are those of *Algebra and Element Conventions*, §*The Algebra and Its Basis* and §*The Base and Its Units*: $e_t$ is the unit of the algebra and $i$ is central. The gradient $\tilde{\nabla}$, its quaternion conjugate $\tilde{\nabla}^{\natural}$, the d'Alembertian $\Box$ and the pair operator $\mathbb{D}$ are those of *Operator and Calculus Conventions*, §*The Gradient*. The pair operator is the chiral pair written once, it satisfies $\mathbb{D}^2=\Box$ on the pair, and it is the pair itself and not an array of generators. The coordinates $x_\mu=(x_0,x_1,x_2,x_3)$, the material sector $\mathbb{M}_-$ and its interval $-c^2{r'_{t}}^2+r_x^2+r_y^2+r_z^2$, whose one minus is the square of the $i$ in $Q_t=i c r'_t$, are those of *Frame and Metric Conventions*, §*The $\mathbb{M}_-$ Frame*, and the four-momentum element $\tilde{P}$ is that of *Algebra and Element Conventions*, §*The Four-Vectors and the Currents*.

**The dynamics is the chiral pair.**

$$
\tilde{\nabla}\tilde{Ξ}^{\mathrm{sp}}_R = \mu\tilde{Ξ}^{\mathrm{sp}}_L, \qquad
\tilde{\nabla}^{\natural}\tilde{Ξ}^{\mathrm{sp}}_L = \mu\tilde{Ξ}^{\mathrm{sp}}_R, \qquad
\mu = \frac{mc}{\hbar},
$$

with massless limit $\tilde{\nabla}\tilde{Ξ}^{\mathrm{sp}} = 0$; in natural units $\mu = m$. Both lines act from the left, the conjugation $\natural$ separates them, and no glyph names a side (*Operator and Calculus Conventions*, §*The Two Sides and the Renaming Theorem*). Every coordinate form of the pair is the standard Dirac equation and is not a second dynamics. The field is one element of $\mathbb{B}$ with two parts, one for each value of the subscript, and the mass is the term that takes one part into the other.

**Two different equations carry the name of Dirac, and this article uses one of them.** The first is the one-sided pair displayed above: both gradients act by left multiplication, and the mass is the off-diagonal pairing of the two values of the subscript. The second is the **two-sided** form of *The Dirac Equation in Biquaternionic Form*, a single equation on $\mathbb{B}$ in which the derivative acts from the left and the mass by right multiplication through the fixed direction $\vec e_z$. The two are the same field read through the dictionary of that article, and they are not the same operator; the difference is exactly the difference between a one-sided and a two-sided action. Every statement below is about the one-sided pair, and the path integral is built for it.

The worldline parameter is $\tau$ and the proper time $T$. The material position is $\tilde R_\varphi = i c r'_t\,e_t + r_x\,\vec e_x + r_y\,\vec e_y + r_z\,\vec e_z \in \mathbb{M}_-$, with real coordinates $x_0 = c r'_{t}$ and $r_k$ on the three spatial directions (*Frame and Metric Conventions*, §*The $\mathbb{M}_-$ Frame*), so that $Q_t = ix_0$.

## The Dirac Propagator and the Square

The object the path integral must compute is the Feynman propagator of the pair. Its two components are the amplitudes for the two values of the subscript, and each component is an element of the algebra: no array enters, and the pair is what the algebra's own product acts on.

**The two symbols.** A plane wave of the pair is $\tilde{Ξ}^{\mathrm{sp}}(x) = \hat{\tilde{Ξ}^{\mathrm{sp}}}\exp(-ip\cdot x)$, with $p\cdot x = p_0x_0 - \vec p\cdot\vec r$ and $p_0 = E/c$ the contraction of the material frame. The momentum element is $\tilde{P}$, and its norm is the mass-shell scalar,

$$
\langle\tilde{P}\rangle_{\natural} = \tilde{P}\tilde{P}^{\natural} = -p^2,
\qquad
p^2 = p_0^2 - p_1^2 - p_2^2 - p_3^2 .
$$

The gradient and its conjugate act on the plane wave by left multiplication by the two symbols,

$$
\tilde{\nabla}\,e^{-ip\cdot x} = i\tilde{P}\,e^{-ip\cdot x},
\qquad
\tilde{\nabla}^{\natural}\,e^{-ip\cdot x} = i\tilde{P}^{\natural}\,e^{-ip\cdot x},
$$

a derived form: the time derivative of the phase is $-ip_0$ and the spatial derivative $+ip_k$, and on the material sector the time derivative of the gradient is read with $\partial/\partial R_t = -i\,\partial/\partial x_0$ (*Operator and Calculus Conventions*, §*The Gradient*). The product of the two symbols is the symbol of the d'Alembertian,

$$
i\tilde{P}\,i\tilde{P}^{\natural} = -\langle\tilde{P}\rangle_{\natural} = p^2 .
$$

The sign bookkeeping is the whole of that line. The two factors of $i$ multiply to $-1$ and the norm is $-p^2$, so the product of the two symbols is the mass-shell scalar itself. Either order gives the same product, because the norm of an element is central: the sign with which the momentum is contracted is a labelling convention and not something the square can see.

**The pair on a plane wave.** Substituting the symbols into the two lines gives

$$
i\tilde{P}\,\hat{\tilde{Ξ}^{\mathrm{sp}}}_R = \mu\hat{\tilde{Ξ}^{\mathrm{sp}}}_L,
\qquad
i\tilde{P}^{\natural}\,\hat{\tilde{Ξ}^{\mathrm{sp}}}_L = \mu\hat{\tilde{Ξ}^{\mathrm{sp}}}_R ,
$$

and eliminating one part returns the mass shell, $p^2 = \mu^2$, since $\tilde{P}^{\natural}\tilde{P} = \langle\tilde{P}\rangle_{\natural}$.

**The propagator.** The Green kernel of the pair is the inverse of $\mathbb{D}-\mu$, and on a plane wave its two components are

$$
\hat{\mathcal S}_L = \frac{i\mu - \tilde{P}}{p^2 - \mu^2},
\qquad
\hat{\mathcal S}_R = \frac{i\mu - \tilde{P}^{\natural}}{p^2 - \mu^2} .
$$

The numerator of the $L$ component is the momentum element and the numerator of the $R$ component its conjugate; that assignment is the one that satisfies both lines, since

$$
i\tilde{P}\,\hat{\mathcal S}_R - \mu\hat{\mathcal S}_L = i,
\qquad
i\tilde{P}^{\natural}\,\hat{\mathcal S}_L - \mu\hat{\mathcal S}_R = i .
$$

Two factors of $i$ do different work and neither is redundant. The $i$ of the numerator is the normalisation of the Green's function, fixed by the right-hand side. The $i$ inside each symbol fixes the sign of the squared operator: the symbols are $i\tilde{P}$ and $i\tilde{P}^{\natural}$, their product is $p^2$, and without the two factors of $i$ the product would be the norm $-p^2$ and the denominator would be the negative of the mass-shell scalar.

The propagator satisfies

$$
\left(\mathbb{D} - \mu\right)\mathcal S = i\,\delta^{(4)},
$$

the pair of the two lines above with a source of unit strength. Its square is scalar,

$$
\mathbb{D}^2 = \Box ,
$$

the composition of two left multiplications by the two gradients, whose product is central (*Operator and Calculus Conventions*, §*The Gradient*). In symbols that is the identity $i\tilde{P}\,i\tilde{P}^{\natural} = p^2$; the operator is $\Box=\sum_\mu\partial^2/\partial R_\mu^2$, and on the material reading, $Q_t=i c r'_t$ and $Q_k=r_k$, it is $\Delta - \partial^2/\partial x_0^2$, with $\Delta$ the Laplacian in the three real spatial coordinates. The square is therefore the series' own scalar operator and not a second one, and that is what makes the first-order operator a square root.

This is standard relativistic quantum physics (see the Further Reading); the companion article *The Feynman Propagator in Biquaternionic Form* treats the same object in the biquaternion framework. Two structural facts are needed here.

**The propagator is the scalar kernel acted on by the first-order operator.** Write

$$
\Delta_F(x-x_2) = \int\frac{d^4p}{(2\pi)^4}\,
\frac{i}{p^2 - \mu^2 + i\epsilon}\,
\exp(-ip\cdot(x-x_2)),
\qquad
\left(\Box - \mu^2\right)\Delta_F = i\,\delta^{(4)},
$$

for the scalar (Klein–Gordon) Feynman propagator, the spin-$0$ object of the companion subcategory. It carries the same $i$ as $\mathcal S$, so the two kernels have one and the same Green's-function normalisation and differ by the first-order operator alone. Since $\Box$ acts on the exponential as multiplication by $p^2$, the difference is exactly that operator, and formally

$$
\boxed{\;\mathcal S = \left(\mathbb{D} + \mu\right)\Delta_F\;}
$$

which is the Green kernel of the pair operator as *Operator and Calculus Conventions*, §*The Pair Operator and Its Symbol* states it. The verification is the one-line algebra of the pair,

$$
\left(\mathbb{D} - \mu\right)\left(\mathbb{D} + \mu\right)
= \mathbb{D}^2 - \mu^2 = \Box - \mu^2,
$$

which is the operator that $\Delta_F$ inverts. The Dirac propagator is therefore the Klein–Gordon propagator with the first-order operator applied; if the scalar kernel is available as a path integral, the Dirac propagator is available from it by a differential operation. This is one of the two standard resolutions of the first-order problem, and it is the one the biquaternion algebra states most directly: the inverse of the first-order operator is the conjugate first-order operator times the inverse of its square, and its square is central.

**The propagator is not one path integral with one phase.** The worldline proper-time representation makes the same point in a Lorentz-invariant way. Since

$$
\frac{i}{p^2 - \mu^2 + i\epsilon}
= \int_0^\infty dT\,\exp\left(iT\left(p^2 - \mu^2 + i\epsilon\right)\right),
$$

the scalar propagator is the integral over a proper time $T$ of a kernel $\langle x_2|\exp(iT(\Box - \mu^2))|x\rangle$, and that kernel is a sum over worldlines,

$$
\Delta_F(x,x_2) = \int_0^\infty dT\int_{x(0)=x}^{x(T)=x_2}\mathcal{D}x(\tau)\;
\exp(iS_0[x]),
\qquad
S_0[x] = \int_0^T d\tau\left(\frac{1}{4}\sum_\mu\frac{dR_\mu}{d\tau}\frac{dR_\mu}{d\tau} - \mu^2\right),
$$

up to the standard normalisation of the measure and the einbein gauge choice. The tangent is read in the complex coordinate, $Q_t=i c r'_t$ and $Q_k=r_k$, so that for a straight worldline

$$
\sum_\mu\frac{dR_\mu}{d\tau}\frac{dR_\mu}{d\tau} = -\frac{(x-x_2)^2}{T^2},
\qquad
(x-x_2)^2 = (x_0-x_2^0)^2 - \left|\vec r-\vec r_2\right|^2 ,
$$

writing $\vec r = r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$ for the vector part of the position, and the phase reduces to $\exp\left(-i\left[\frac{(x-x_2)^2}{4T} + \mu^2 T\right]\right)$; this is the sign that the explicit free kernel of the next section displays. The Dirac propagator is then $\left(\mathbb{D} + \mu\right)$ applied to $\Delta_F$. The worldline is a curve in the material sector $\mathbb{M}_-$: its tangent is a material four-velocity, and the phase $S_0$ is central. This is the biquaternion content of the scalar worldline: a central phase over a material curve.

The deficiency of this representation is that the spin is nowhere to be seen until the differential operator is applied at the end. The second resolution supplies the spin directly.

## The Free Kernel, Explicitly

It is worth evaluating the scalar worldline kernel in the free case, because the calculation is the whole content of the proper-time method and fixes the sense in which a first-order object is a square root. The proper-time kernel is the Fourier transform

$$
\Delta_F(x,x_2) = \int_0^\infty dT\int\frac{d^4p}{(2\pi)^4}\,
\exp\left(iT\left(p^2 - \mu^2 + i\epsilon\right)\right)\,\exp(-ip\cdot(x-x_2)),
$$

where the $i\epsilon$ prescription makes the $T$-integral converge at large $T$. The $p$-integral is a Gaussian: completing the square in each of the four components gives the standard free kernel

$$
\Delta_F(x,x_2) = \int_0^\infty dT\;\mathcal{N}(T)\;
\exp\left(-i\left[\frac{(x-x_2)^2}{4T} + \mu^2 T\right]\right),
$$

with $\mathcal{N}(T)$ the standard Gaussian normalisation $\propto T^{-2}$, whose precise constant depends on the measure convention and is not needed below. Three features of this expression carry the physics.

- The **proper time $T$ is the Schwinger parameter**, and the exponent is the classical action of a relativistic free particle, $\frac{(x-x_2)^2}{4T}$ being the kinetic term and $\mu^2T$ the mass term; the path integral over $x(\tau)$ is the statement that the exponent is extremised by a straight line, with the fluctuations around it producing the prefactor.
- The **mass is a constant in the exponent**. There is no spin and no algebra-valued weight: $\Delta_F$ is a scalar, and it obeys $(\Box - \mu^2)\Delta_F = i\delta^{(4)}$ up to the measure convention.
- The **first-order structure enters only through the differential prefactor**. The Dirac propagator is obtained by applying $\left(\mathbb{D} + \mu\right)$ to $\Delta_F$, which is why the spin is invisible until that operation is performed.

The same proper-time integral is the bridge to the worldline of the next section: replacing the constant mass by a general worldline interaction, and adding the odd variables, converts this scalar kernel into the algebra-valued kernel of the pair.

## The Spinning Worldline and the Spin Factor

The worldline that generates the Dirac propagator itself, rather than the Klein–Gordon kernel it acts on, carries an additional **odd** (Grassmann) degree of freedom $\tilde{Ξ}^{\mathrm{sp}}_\mu(\tau)$ at each point. The standard supersymmetric worldline action is

$$
S[x,\tilde{Ξ}^{\mathrm{sp}}] = \int_0^T d\tau\left[
\frac{1}{4}\sum_\mu\frac{dR_\mu}{d\tau}\frac{dR_\mu}{d\tau}
+ \frac{i}{2}\sum_\mu\tilde{Ξ}^{\mathrm{sp}}_\mu\frac{d\tilde{Ξ}^{\mathrm{sp}}_\mu}{d\tau}
- \mu^2
\right],
$$

with both quadratic terms read on the same four slots and carrying the same signs: the tangent takes its sign from the square of the $i$ in $Q_t=i c r'_t$ and the odd pair from the weight below, and the tangent and the odd pair are the two halves of one supersymmetric pair, which is why the same signs appear twice. Each half contributes its own kinetic term, the bosonic one from the tangent and the fermionic one from the odd variables.

**The odd pair carries the anticommutation of the worldline.** The odd variables are fixed by the symmetric pairing of the worldline action,

$$
\tilde{Ξ}^{\mathrm{sp}}_\mu\tilde{Ξ}^{\mathrm{sp}}_\nu + \tilde{Ξ}^{\mathrm{sp}}_\nu\tilde{Ξ}^{\mathrm{sp}}_\mu = -\tfrac12 \varepsilon_\mu\delta_{\mu\nu}\,e_t ,
$$

with the unit $e_t$ of the algebra in place of the identity of the older display, and this is the whole of their definition: the right-hand side carries the weight and the unit and nothing else. The central $i$ sits in the kinetic term of the worldline action and not in this relation, so the odd sector carries the signs of the bosonic sector, the time slot negative and the three spatial slots positive, written as the negative of the plain weight.

**The odd pair closes on the algebra.** A single odd variable is not an element of $\mathbb{B}$: the algebra has no odd part, and every element of it commutes with the central coefficients. The products of an even number of odd variables are even, and they close under multiplication; they span an algebra of real dimension eight, and that algebra is $\mathbb{B}$ — the even part of the envelope is the algebra, and the odd part is a second copy of it that the algebra does not contain (*Biquaternion Versors and the Orthogonal Group*, §*The Two Slots of the Envelope*). In the algebra itself the closure is visible on the units: a product of two units is a unit up to sign, since $e_te_t$ and $\vec e_k\vec e_k$ are $\pm e_t$, $e_t\vec e_k$ and $\vec e_k e_t$ are $\pm\vec e_k$, and $\vec e_j\vec e_k$ with distinct spatial indices is the third unit. The four units span the algebra, of complex dimension four, and that dimension is the one the older counting reports.

The path integral over the odd variables, with the boundary condition appropriate to the object computed, is a **spin factor** $Ξ[x]$ multiplying the scalar measure:

$$
\boxed{\;\mathcal S(x,x_2) = \int_0^\infty dT\int\mathcal{D}x\;Ξ[x]\,\exp(iS_0[x])\;}
$$

with the spin factor

$$
Ξ[x] = \int_{\text{b.c.}}\mathcal{D}\tilde{Ξ}^{\mathrm{sp}}\;
\exp\left(-\frac{1}{2}\int_0^T d\tau\;\sum_\mu\tilde{Ξ}^{\mathrm{sp}}_\mu\frac{d\tilde{Ξ}^{\mathrm{sp}}_\mu}{d\tau}\right).
$$

The exponent of $Ξ$ carries no $i$, and the reason is the product of two of them: the action contributes $\frac{i}{2}\sum_\mu\tilde{Ξ}^{\mathrm{sp}}_\mu\frac{d\tilde{Ξ}^{\mathrm{sp}}_\mu}{d\tau}$, the weight is the exponential of $i$ times the action, and $i\cdot i = -1$. Written with the two $i$'s kept apart, the spin factor is $\exp\left(i\int_0^T d\tau\,\frac{i}{2}\sum_\mu\tilde{Ξ}^{\mathrm{sp}}_\mu\frac{d\tilde{Ξ}^{\mathrm{sp}}_\mu}{d\tau}\right)$; multiplied out, it is $\exp\left(-\frac{1}{2}\int_0^T d\tau\,\sum_\mu\tilde{Ξ}^{\mathrm{sp}}_\mu\frac{d\tilde{Ξ}^{\mathrm{sp}}_\mu}{d\tau}\right)$, which is real. It is bilinear in the odd variables, so its expansion is a sum of products of pairs, and a pair corresponds to an element of the algebra, a product of two units being a unit up to sign: the weight the odd integral produces is an element of $\mathbb{B}$.

The complete worldline path integral, with the correct measure, reproduces the propagator $\mathcal S$; this is the Berezin–Marinov / Brink–Di Vecchia–Howe construction, and it is standard. The same construction in a background electromagnetic field replaces the free kinetic term by the minimally coupled one and produces the spin factor quoted in the literature, with the sign conventions of the cited works; the trace of the same object is the closed-worldline weight and belongs to the next section.

### The Biquaternion Interpretation of the Spin Factor

The spin factor is where the algebra sits, and its structure is the reason the odd variable carries the spin.

**A pair of odd variables is an element, and a single one is not.** The algebra carries no odd part: every element is even in the Grassmann sense, because the central coefficients commute with it. The oddness therefore lives in the variable and not in the algebra, and the weight is where it disappears: the exponent of $Ξ$ is bilinear, so each term of its expansion is a pair, and a pair is an element of the algebra, since a product of two units is a unit up to sign. The weight is an element of $\mathbb{B}$ and acts on the field by left multiplication. The transport of the field along the worldline is a multiplication by that element, and the algebra is not an auxiliary description of the spin: it is the algebra of the pairs.

**The spin factor is the path-ordered product of the elements at the successive points.** Order by order, $Ξ[x]$ is a sum of elements: the unit, then the products of two units, then of four. Each instant of the worldline contributes an element and the product is path ordered, because the elements at different instants do not commute. The exponent therefore grows one factor of the algebra per pair of odd variables, and the whole transport is a product of elements multiplying the field on the left.

**The square of the operator is the scalar path integral.** The worldline action has a bosonic kinetic term and a fermionic one, and integrating out the odd variables returns the weight that the first-order equation adds. The statement that the Dirac propagator is the Dirac operator applied to the scalar kernel, and the statement that a pair of odd variables is an element of the algebra, are two faces of the same relation: the odd variable is the spin and the pair is the algebra, so squaring the first-order operator removes the odd variable and returns the scalar operator whose path integral is $\Delta_F$.

## The Spin Factor in a Background Field

The spin factor earns its name in a background electromagnetic field, and the calculation shows how the algebra organises the result. Minimal coupling adds the gauge term $\sum_\mu qA_\mu(x)\frac{dx_\mu}{d\tau}$ to the worldline action,

$$
S[x] = \int_0^T d\tau\left[\frac{1}{4}\sum_\mu\frac{dR_\mu}{d\tau}\frac{dR_\mu}{d\tau} - \mu^2 + \sum_\mu qA_\mu(x)\frac{dx_\mu}{d\tau}\right],
$$

and the odd kinetic term is unchanged. The coupling is through the pair of two units, contracted with the field strength. The six generators are written once, the three of a time index and a spatial one and the three of two spatial indices:

$$
\tilde\Sigma_{0k} = i\vec e_k,
\qquad
\tilde\Sigma_{jk} = \vec e_j\vec e_k,
\qquad
\tilde\Sigma_{\nu\mu} = -\tilde\Sigma_{\mu\nu} .
$$

**The six generators are the two labels of the Lorentz action.** On the field they act by left multiplication, and the six split by the index: with $\mu=t$ the element $i\vec e_k$ is a boost generator and lies in $\mathbb{M}_+$, and with both indices spatial the element $\vec e_j\vec e_k$ is a rotation generator and lies in the real quaternion sector. The two families are the two labels of *Algebra and Element Conventions*, §*The Remarkable Subspaces of Biquaternions*, so a boost and a rotation are read on the same line with no second structure.

**The six elements are two triples and not six directions.** A boost and a rotation sharing the same direction differ by one factor of $i$: $\vec e_x\vec e_y$ and $i\vec e_z$ are the same direction, and the six elements therefore occupy the three directions twice. This is the coarsest reading of the six, and it is enough for the exponent below, which is linear in the generators. An identity that separates $\vec e_x\vec e_y$ from $i\vec e_z$ — the vanishing of the traced weight at a given order, for instance — is an identity of the two-sided generators and is read where those are written out.

**The weight is the path-ordered exponential of an element.** The path integral over the odd variables produces the path-ordered exponential of the contraction:

$$
\boxed{\;Ξ[x] = \mathcal{P}\exp\left(-\frac{i}{2}\int_0^T d\tau\;\sum_{\mu\neq\nu}\tilde\Sigma_{\mu\nu}F_{\mu\nu}(x(\tau))\right)\;}
$$

for the open worldline that computes the propagator, and for the worldline closed into a loop it is the traced weight

$$
Ξ_{\mathrm{loop}}[x] = \mathrm{Tr}\,\mathcal{P}\exp\left(-\frac{i}{2}\int_0^T d\tau\;\sum_{\mu\neq\nu}\tilde\Sigma_{\mu\nu}F_{\mu\nu}(x(\tau))\right).
$$

Closing the worldline into a loop turns the weight into a trace, and that is the antiperiodic case of the odd integral above: the fermionic variables are antiperiodic around the circle, as every fermionic trace requires. The contractions pair the electric components with the boost generators and the magnetic components with the rotation generators, so the exponent carries both labels at once.

This is the standard Berezin–Marinov spin factor, and the path ordering is required in both cases because the elements at different times do not commute. The same structure is what produces the anomalous magnetic moment in the worldline computation of the electron's form factors, and it is the worldline form of the spin–field coupling that the companion articles *The Electron in Biquaternionic Form* and *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism* treat from the operator side.

**On the closed worldline the weight is traced.** The trace is that of the multiplication, four times the scalar part of the element: the unit contributes four and each vector unit zero, because multiplication by a vector unit permutes the four units up to sign with no fixed point (*Matrix Representations Conventions*, §*The Left Family*). A single generator is pure, so the term linear in the field strength vanishes and the loop weight begins with the quadratic term, built from $F_{\mu\nu}F_{\mu\nu}$. Which invariants of the field strength survive at each order is an identity of the two-sided generators, where the fifth cell is traceless, and it is not restated here. The open weight is an element at each end, and it multiplies the field at the two ends of the worldline. The path-ordered exponential is the worldline image of the algebra's rotor construction: at each instant the field is carried by one generator, and the product of all the carries is the spin factor.

## Feynman's Checkerboard

Before the continuum worldline there was a discrete model, and in 1+1 dimensions it exhibits the algebraic structure with unusual clarity. Feynman's checkerboard (1949) represents the Dirac particle as moving at the speed of light along the two null directions of two-dimensional spacetime, with the amplitude for a path built from two rules: a directed step carries a phase, and each **corner** (reversal of direction) carries a factor $i\epsilon m/\hbar$, with $\epsilon$ the step length and $m$ the mass; the sign of the corner weight is conjugate to the naming of the two directions, and the recurrence below fixes the one used here. The propagator is the sum over all such paths, and in the continuum limit the sum satisfies the two-dimensional Dirac equation.

The reason is the one on which this whole article turns. In 1+1 dimensions the field has two parts, and the two parts are exactly the amplitudes for the two directions of motion. Writing the propagator as the four amplitudes $K_{++}$, $K_{+-}$, $K_{-+}$, $K_{--}$, where the labels record the initial and final directions, the corner weight builds the mass mixing: the amplitudes that exchange the direction require an odd number of corners, so they are the ones proportional to $m$, and the ones that keep it require an even number.

| amplitude | corners | weight in $m$ | continuum role |
|---|---|---|---|
| $K_{++}$, $K_{--}$ | even number | $m^0$ | free propagation of one value of the subscript |
| $K_{+-}$, $K_{-+}$ | odd number | $m^1$ | mass insertion between the two values |

The continuum limit is the two-part Dirac propagator in 1+1 dimensions, whose small-$\epsilon$ expansion satisfies the two-dimensional Dirac equation with the corner weight as its mass term; the standard derivations of the checkerboard (see the Further Reading) give the explicit form. The two directions are the two parts, and the mass is the corner that exchanges them.

The biquaternion interpretation is then immediate, and it needs no second algebra. In 1+1 dimensions the two retained units are $e_t$ and $\vec e_x$, and their products close on themselves; the two values of the subscript are the two directions, and each corner is one application of the **off-diagonal mass** of the pair $\tilde{\nabla}\tilde{Ξ}^{\mathrm{sp}}_R = \mu\tilde{Ξ}^{\mathrm{sp}}_L$, $\tilde{\nabla}^{\natural}\tilde{Ξ}^{\mathrm{sp}}_L = \mu\tilde{Ξ}^{\mathrm{sp}}_R$. The checkerboard is the discrete, real-time picture of the mass pair: the free propagation is diagonal in the value — each part propagates on its own — and the mass is the reversal that connects them, one application of the second line of the pair per corner. The continuum limit is the statement that the off-diagonal mass pair, iterated on the lattice, reproduces the flat-space propagator of the pair.

### The Recurrence and Its Limit

The discrete structure can be written as a pair of coupled recurrences and taken to the continuum, and doing so exhibits the mass pair explicitly. Let $A_+(r_x,r'_t)$ and $A_-(r_x,r'_t)$ be the amplitudes to arrive at the lattice point $(r_x,r'_t)$ having last moved in the $+x$ and $-x$ directions respectively, with the lattice spacing and time step both equal to $\epsilon$ (units $c = 1$). A step carries the particle one site in its direction of motion, and a corner contributes the weight $i\epsilon m/\hbar$; the recurrences are therefore

$$
A_+(r_x,r'_t+\epsilon) = A_+(r_x-\epsilon,r'_t) + \frac{i\epsilon m}{\hbar}\,A_-(r_x-\epsilon,r'_t),
$$

$$
A_-(r_x,r'_t+\epsilon) = A_-(r_x+\epsilon,r'_t) + \frac{i\epsilon m}{\hbar}\,A_+(r_x+\epsilon,r'_t),
$$

where the first term on each right-hand side is the straight continuation and the second is the corner. Two features are visible by inspection. The **free propagation is diagonal**: the term that carries $A_+$ to $A_+$ and $A_-$ to $A_-$ involves no mixing, and each direction propagates independently. The **mass is off-diagonal**: the corner terms couple the two amplitudes with the weight $i\epsilon m/\hbar$, i.e. with an explicit factor of the mass and an explicit factor of $i$.

Taylor-expanding and taking $\epsilon \to 0$ with the lightlike constraint $|dr_x/dr'_t| = 1$ — the particle moves at the speed of light along the null directions, one lattice site per time step — turns the pair into

$$
\frac{\partial A_+}{\partial r'_t} = -\frac{\partial A_+}{\partial r_x} + \frac{im}{\hbar}A_-,
\qquad
\frac{\partial A_-}{\partial r'_t} = +\frac{\partial A_-}{\partial r_x} + \frac{im}{\hbar}A_+,
$$

the two-part Dirac equation in 1+1 dimensions. The corner weight $i\epsilon m/\hbar$ becomes the mass term $i\mu$, with $\mu=m/\hbar$ at $c=1$, and the two directions become the two values of the subscript. Squaring either line with the other substituted gives $\partial^2 A_+/\partial r'_t^2-\partial^2 A_+/\partial r_x^2 = -m^2A_+/\hbar^2$: the cross terms cancel and the two corner factors meet as $i\cdot i=-1$, which is why the mass enters the squared equation with a minus sign. The $i$ of the corner is a relative phase of the two parts, since the rotation $A_+\mapsto e^{i\pi/4}A_+$, $A_-\mapsto e^{-i\pi/4}A_-$ turns the mass term $i\mu$ into the real $-\mu$; that is why the biquaternion pair can carry the real $\mu$, and why the corner weight is a convention rather than a sign. This is the Klein–Gordon equation of the series' d'Alembertian, so the discrete model carries the Dirac square as well as the Dirac equation. This is the discrete origin of the off-diagonal mass pair that the biquaternion algebra writes as $\tilde{\nabla}\tilde{Ξ}^{\mathrm{sp}}_R = \mu\tilde{Ξ}^{\mathrm{sp}}_L$, $\tilde{\nabla}^{\natural}\tilde{Ξ}^{\mathrm{sp}}_L = \mu\tilde{Ξ}^{\mathrm{sp}}_R$: the checkerboard is that pair before the continuum limit has identified the directions with the two values of the subscript. The order of the two factors in a corner is the path ordering that survives as the ordering of the operators $\tilde{\nabla}$ and $\tilde{\nabla}^{\natural}$ in the continuum.

## Composition, the Propagator Equation, and the Scalar Reduction

The path integral must carry the composition law of a kernel and the Green's-function equation, and both are transparent in the biquaternion framework.

**Composition belongs to the proper-time kernel, not to $\mathcal S$.** Write $K_T(x,x_2)$ for the kernel of $\exp\left(iT\left(\Box-\mu^2\right)\right)$. Then

$$
\int d^4y\;K_{T_1}(x,y)\,K_{T_2}(y,x_2) = K_{T_1+T_2}(x,x_2),
$$

a sum over paths being a sum over intermediate points, and $\mathcal S$ is the transform $\int_0^\infty dT$ of the family. The law stops there: $\int d^4y\,\mathcal S(x,y)\mathcal S(y,x_2)$ is the convolution of two propagators — in momentum space the square of the two components of $\hat{\mathcal S}$, not the propagator itself — so $\mathcal S$ does not compose to itself and the composition law is not one of its properties. That is why the worldline keeps the proper time explicit instead of integrating it away at the start. In the biquaternion algebra the composition is the multiplication of algebra-valued amplitudes, with the central phase composing additively; the algebra's non-commutativity means that the order of the intermediate points matters, and the path-ordered spin factor is the price of that non-commutativity.

**The propagator equation.** The kernel satisfies $\left(\mathbb{D} - \mu\right)\mathcal S = i\delta^{(4)}$. This is the statement that the propagator is the Green's function of the first-order pair. Applying $\mathbb{D} + \mu$ and using $\mathbb{D}^2 = \Box$ gives

$$
\left(\Box - \mu^2\right)\mathcal S
= \left(\mathbb{D} + \mu\right)i\,\delta^{(4)} ,
$$

so the first-order propagator, acted on by its conjugate, obeys the Klein–Gordon equation, with the spin structure carried entirely by the source. This is the path-integral form of the Dirac square: the first-order propagator, acted on by its conjugate, obeys the second-order equation. The path integral for the first-order object is therefore not an independent construction; applying the conjugate operator to it returns the scalar path integral of the companion subcategory, and the spin factor is what distinguishes them.

It is worth stating what the square does **not** do in this setting. It does not remove the spin: the squared propagator is an element and not a scalar, so the spin survives in the algebra-valued weight even though its differential operator is central. The spin-0 theory is recovered only when the weight is reduced to its scalar part. In the algebra this is the statement that the algebra-valued weight is what survives squaring, while the odd variable has been absorbed into the two ends of the worldline.

## The Measure and the Einbein

The worldline integrals above are written with a proper-time parameter $T$ that has already been gauge-fixed, and the fixing is worth stating because it is the reason the four-dimensional propagator carries a proper-time integral at all. A relativistic worldline is **reparametrisation invariant**: the action

$$
S[x,e] = \int_0^1 d\tau\left[\frac{1}{4e(\tau)}\sum_\mu\frac{dR_\mu}{d\tau}\frac{dR_\mu}{d\tau} - e(\tau)\,\mu^2\right]
$$

depends on the worldline only through its image, the auxiliary field $e(\tau)$ (the **einbein**) transforming as a density; the parameter $\tau$ has no physical meaning. In the path integral one does not fix $e$ but integrates over it, and the integral over the constant modes of $e$ is precisely the proper-time integral: writing $e(\tau) = T$ for the constant mode, the other modes can be gauged to zero and divide out the volume of the reparametrisation group, and the action becomes

$$
S = \frac{1}{4T}\int_0^1 \sum_\mu\frac{dR_\mu}{d\tau}\frac{dR_\mu}{d\tau}\,d\tau - \mu^2 T ,
$$

which is the proper-time exponent of the previous sections, with $T$ identified as the total proper time. The fluctuations of the material trajectory about the straight line — equivalently, in the Fourier form used above, the four-dimensional Gaussian integral over $p$ — produce the $T^{-2}$ prefactor $\mathcal{N}(T)$ of the free kernel.

The algebraic interpretation is a statement about the two sectors. The einbein is a **central scalar**: it commutes with the odd variables and carries no odd degree of freedom, so its integral only reorganises the material part of the worldline. It is the same for every spin, and it is the reason the spin-0 and spin-$\tfrac12$ theories share the proper-time structure. The spin enters entirely through the odd variables and the spin factor, not through the measure. In the biquaternion framework the einbein is a central element of the worldline's phase, and the spin factor is the algebra-valued remainder; the split of the worldline integral into a central measure and an algebra-valued weight is the path-integral image of the distinction between the centre of the algebra and the rest of it.

## The Chiral Pair on the Worldline

The two constructions of the Dirac path integral can be expressed in one biquaternionic statement, and it is worth writing it explicitly because it is the point at which this article meets the rest of the subcategory.

A worldline carries two structures at once: a **material** trajectory $x_\mu(\tau)$, whose tangent is a four-velocity in $\mathbb{M}_-$, and a **spin** transport, whose generator is the odd variable $\tilde{Ξ}^{\mathrm{sp}}_\mu$. The material trajectory is the object the scalar path integral sums over; the spin transport is the object the spin factor sums over. Squaring the first-order operator pairs them: the square of the Dirac operator is central and acts only on the material trajectory, while the spin is carried along by the element that multiplies the field. The chiral pair

$$
\tilde{\nabla}\tilde{Ξ}^{\mathrm{sp}}_R = \mu\tilde{Ξ}^{\mathrm{sp}}_L, \qquad
\tilde{\nabla}^{\natural}\tilde{Ξ}^{\mathrm{sp}}_L = \mu\tilde{Ξ}^{\mathrm{sp}}_R
$$

is the operator statement of the same split: the two gradients act on the two parts, the material trajectory is common to both, and the mass is the off-diagonal corner that turns one into the other. In the worldline language the two parts are the two ways the transport can hand the field at the boundary to the mass term, and the mass term is the reversal; in the checkerboard the same reversal is the lattice corner. The three descriptions — the operator pair, the discretised checkerboard, and the continuous spinning worldline — are the same off-diagonal mass structure in three registers.

There is a further consistency check that ties this article to *Klein–Gordon from the Dirac Square in Biquaternionic Form*. The scalar kernel $\Delta_F$ is the path integral of the **squared** theory; the spin factor is what the first-order theory adds. In the free case the spin factor is the unit, with no generator inserted, and the worldline path integral reduces to the scalar $\Delta_F$; this is why the square of the propagator's equation is the Klein–Gordon equation with a delta source, as computed above. The higher terms of the spin factor are the spin–field couplings, and they have no spin-0 counterpart. The spin-0 path integral of the companion subcategory is therefore not a separate construction with an analogous appearance; it is the trivial-spin-factor case of the worldline integral, and the full Dirac path integral is what the spin degrees of freedom add to it.

## What Is Standard and What the Algebra Adds

The Feynman propagator, the proper-time representation, the worldline supersymmetric action, the spin factor and the checkerboard limit are all standard results, transcribed here and cited. The biquaternion interpretation contributes three placements:

- The **spin variable is the odd variable** $\tilde{Ξ}^{\mathrm{sp}}_\mu$, whose pairs are elements of $\mathbb{B}$: the even products of odd variables span an algebra of real dimension eight, and that algebra is the biquaternion algebra. The biquaternion algebra is not an auxiliary description of spin; it is the algebra the pairs generate.
- The **Dirac propagator is the Dirac operator applied to the scalar propagator**, and the reason is the Dirac square: the first-order operator's square is the central Klein–Gordon operator, whose path integral is the spin-0 object of the companion subcategory. The first-order path integral is thus a "square root" of the scalar one, in the same sense as the Dirac equation itself.
- The **checkerboard is the chiral pair on a lattice**. Its two directions are the two values of the subscript, and its corners are the off-diagonal mass insertions; the continuum limit is the biquaternion mass pair.

The worldline and the checkerboard are complementary descriptions of the same object, and the algebra shows why both work: a first-order operator can be realised as a sum over directed paths, the checkerboard, which builds in the two values, or as a second-order path integral dressed by an algebra-valued spin factor, the worldline, which builds in the square. The two agree because the odd variable and the mass term are the two faces of the same off-diagonal structure.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, and the frame is named on the coordinate.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C}) = M_4(\mathbb{C})$, not a different algebra; here $L_aR_b$ is the two-sided multiplication $\tilde{Ξ}^{\mathrm{sp}}\mapsto a\tilde{Ξ}^{\mathrm{sp}} b$. The five are the frame cells under the gammas' own letters, so that the dictionary between the two writings is the identity on the operators:

$$
\gamma_0 = iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad
\gamma_1 = iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad
\gamma_2 = iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad
\gamma_3 = iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad
\gamma_5 = -iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}} .
$$

The same in the axis-free display:

$$
\gamma_0 = iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\quad
\gamma_1 = iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad
\gamma_2 = iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad
\gamma_3 = iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad
\gamma_5 = -iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}} .
$$

The right factor $\vec e_y$ of the three spatial gammas is the frame's common direction and the left factor is the direction of the coordinate, so the four vectors $L_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}$, $L_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$, $L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$, $L_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$ climb a staircase through the two-sided index pairs — a row in neither factor, and not a diagonal. That staircase is the choice of frame, not a feature of the gammas: the repetition of $\vec e_y$ is in the frame. A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le 1$, and a general element is a sum of at most four, with $\ell(M) = \operatorname{rank}c(M)$.

$\gamma_5$ is the reference-frame cell of the chirality $\Gamma$; the central grading $\chi=i\tilde{Ζ}_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The identities the bodies cite.** In the $\gamma$ reading, with $\varepsilon=(1,-1,-1,-1)$ the sign vector of the cells,
$$
\{\gamma_\mu,\gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,\qquad
(\gamma_k)^2=-I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu,\gamma_5\}=0,
$$
$$
[\gamma_\mu,\gamma_\nu]=2\gamma_\mu\gamma_\nu\quad(\mu\ne\nu),\qquad
[\gamma_a,S_{cd}]=\varepsilon_a\delta_{ac}\gamma_d-\varepsilon_a\delta_{ad}\gamma_c,\qquad
S_{cd}=\tfrac14[\gamma_c,\gamma_d],
$$
$$
\mathrm{tr}(\gamma_\mu\gamma_\nu)=4\varepsilon_\mu\delta_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$
$$
\mathrm{tr}(\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)
=4\bigl(\varepsilon_\mu\delta_{\mu\nu}\varepsilon_\rho\delta_{\rho\sigma}
-\varepsilon_\mu\delta_{\mu\rho}\varepsilon_\nu\delta_{\nu\sigma}
+\varepsilon_\mu\delta_{\mu\sigma}\varepsilon_\nu\delta_{\nu\rho}\bigr).
$$
The contraction sums follow from the squares. With one index raised, $\gamma^\mu=-\varepsilon_\mu\gamma_\mu$, so that $\sum_\mu\gamma^\mu\gamma_\mu=-4I_4$, $\sum_\mu\gamma^\mu\gamma_\alpha\gamma_\mu=2\gamma_\alpha$, $\sum_\mu\gamma^\mu\gamma_\alpha\gamma_\beta\gamma_\mu=-4\varepsilon_\alpha\delta_{\alpha\beta}I_4$ and $\sum_\mu\gamma^\mu\gamma_\gamma\gamma_\beta\gamma_\alpha\gamma_\mu=-2\gamma_\gamma\gamma_\beta\gamma_\alpha$.

The volume cell is $\gamma_0\gamma_1\gamma_2\gamma_3=-i\gamma_5=-R_{\vec e_z}^{\mathrm{pau}}=-L_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$, the same cell written in the two displays.

**The four contraction sums** are the sums in which one gamma is contracted against a fixed string of $n$ gammas,

$$
\sum_\mu\gamma^\mu\gamma_\mu,\qquad
\sum_\mu\gamma^\mu\gamma_\alpha\gamma_\mu,\qquad
\sum_\mu\gamma^\mu\gamma_\alpha\gamma_\beta\gamma_\mu,\qquad
\sum_\mu\gamma^\mu\gamma_\alpha\gamma_\beta\gamma_\gamma\gamma_\mu ,
$$

and one rule produces all four: for a string of distinct indices,

$$
\sum_\mu\gamma^\mu\gamma_{\alpha_1}\cdots\gamma_{\alpha_n}\gamma_\mu = (-1)^{n+1}(4-2n)\,\gamma_{\alpha_1}\cdots\gamma_{\alpha_n},
$$

so that the four values are $-4I_4$, $+2\gamma_\alpha$, $0$ and $-2\gamma_\alpha\gamma_\beta\gamma_\gamma$. The two-gamma entry is the one that vanishes, and it is where the dimension enters: the two contracted gammas are moved past the $n$ fixed ones, which gives the $(-1)^n$, and what is left is the contraction of the string with itself, which counts $4-2n$. With the summed index raised, $\gamma^\mu=-\varepsilon_\mu\gamma_\mu$, the four are $-4I_4$, $+2\gamma_\alpha$, $-4\varepsilon_\alpha\delta_{\alpha\beta}I_4$ and $-2\gamma_\gamma\gamma_\beta\gamma_\alpha$: the two-gamma entry is diagonal and carries the weight, $+4I_4$ on the time direction and $-4I_4$ on the three spatial ones, and the last is the rule with the three indices reversed. With every index low the rule changes, because then the square of a generator carries the weight: $\sum_\mu\gamma_\mu\gamma_\mu=-2I_4$ and $\sum_\mu\gamma_\mu\gamma_\alpha\gamma_\mu=2(1+\varepsilon_\alpha)\gamma_\alpha$, which is $4\gamma_0$ for the time direction and vanishes for the three spatial ones. The one-gamma sum is uniform in the index when the index is raised and weight-dependent when it is low.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

The Dirac path integral is the sum over worldlines that computes the propagator $\mathcal S$, the pair of element-valued kernels satisfying $\left(\mathbb{D} - \mu\right)\mathcal S = i\delta^{(4)}$ with $\mu = mc/\hbar$. Because the Dirac operator is first order, the path integral is organised in one of two standard ways. In the **proper-time** way, the scalar Klein–Gordon kernel is written as a worldline sum over material curves in $\mathbb{M}_-$ with central phase $S_0$, and the Dirac propagator is obtained by applying the conjugate first-order operator: $\mathcal S = \left(\mathbb{D} + \mu\right)\Delta_F$, the identity following from $\mathbb{D}^2 = \Box$. In the **spinning-worldline** way, an odd Grassmann variable $\tilde{Ξ}^{\mathrm{sp}}_\mu$ is added at each point with kinetic term $\frac{i}{2}\sum_\mu\tilde{Ξ}^{\mathrm{sp}}_\mu\frac{d\tilde{Ξ}^{\mathrm{sp}}_\mu}{d\tau}$; a pair of odd variables is an element of the algebra with $\tilde{Ξ}^{\mathrm{sp}}_\mu\tilde{Ξ}^{\mathrm{sp}}_\nu + \tilde{Ξ}^{\mathrm{sp}}_\nu\tilde{Ξ}^{\mathrm{sp}}_\mu = -\frac12\varepsilon_\mu\delta_{\mu\nu}e_t$; the path integral over $\tilde{Ξ}^{\mathrm{sp}}$ is the algebra-valued spin factor $Ξ[x]$; and the full worldline integral reproduces the propagator (Berezin–Marinov, Brink–Di Vecchia–Howe).

In the biquaternion framework, a single odd variable is not an element of the algebra and a pair is, because every product of two units is a unit up to sign; the spin factor is the path-ordered product of those elements, and squaring the first-order operator returns the central Klein–Gordon operator. In momentum space the two components of the propagator are $\hat{\mathcal S}_L = (i\mu-\tilde{P})/(p^2-\mu^2)$ and $\hat{\mathcal S}_R = (i\mu-\tilde{P}^{\natural})/(p^2-\mu^2)$, and the identity $\left(\mathbb{D}-\mu\right)\left(\mathbb{D}+\mu\right) = \mathbb{D}^2-\mu^2$ is the whole of the square. The scalar path integral of the companion subcategory is the kernel that the first-order factor acts on, a consequence of this identity rather than an independent construction. Feynman's checkerboard is the discrete realisation of the same structure in 1+1 dimensions: the two directions are the two values of the subscript, the corners carry the weight $i\epsilon m/\hbar$ and are the off-diagonal mass insertions, and the continuum limit is the two-dimensional propagator.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra; $e_t$ its unit, $\vec e_x, \vec e_y, \vec e_z$ the three vector units |
| $\mathbb{M}_-$ | Anti-Hermitian (material) sector; the worldline position $\tilde R_\varphi$ |
| $i$ | Central scalar imaginary |
| $\mathbb{D}$ | The pair operator, $\mathbb{D}\tilde{Ξ}^{\mathrm{sp}} = (\tilde{\nabla}\tilde{Ξ}^{\mathrm{sp}}_R,\ \tilde{\nabla}^{\natural}\tilde{Ξ}^{\mathrm{sp}}_L)$, with $\mathbb{D}^2 = \Box$ |
| $\Box$ | Series d'Alembertian, $\sum_\mu\partial^2/\partial R_\mu^2$; $\Delta-\partial^2/\partial x_0^2$ on the material reading |
| $\Delta$ | Laplacian in the three real spatial coordinates |
| $\delta_{\mu\nu}=(1,1,1,1)$ | The unit metric on the four slots, the one metric of the series; the interval is $\sum_\mu Q_\mu^2$ |
| $\varepsilon=(1,-1,-1,-1)$ | Plain weight, the sign of each squared unit: positive on the time slot, negative on the three spatial ones |
| $x_\mu$ | Real coordinates of the material sector, $x_0 = c r'_{t}$ |
| $\tilde{P} = ip_0e_t+\vec p$ | Four-momentum element, $\langle\tilde{P}\rangle_{\natural} = \tilde{P}\tilde{P}^{\natural} = -p^2$ |
| $p^2 = p_0^2-p_1^2-p_2^2-p_3^2$ | Mass-shell scalar of the momentum, with $p_0 = E/c$ |
| $i\tilde{P}$, $i\tilde{P}^{\natural}$ | Symbols of $\tilde{\nabla}$ and $\tilde{\nabla}^{\natural}$ on a plane wave |
| $\mu = mc/\hbar$ | Mass parameter |
| $\tilde{Ξ}^{\mathrm{sp}}$, $\tilde{Ξ}^{\mathrm{sp}}_L$, $\tilde{Ξ}^{\mathrm{sp}}_R$ | The field and its two parts, one per value of the subscript |
| $\mathcal S$, $\mathcal S_L$, $\mathcal S_R$ | Dirac propagator and its two components, $\left(\mathbb{D}-\mu\right)\mathcal S = i\delta^{(4)}$ |
| $\Delta_F(x-x_2)$ | Scalar (Klein–Gordon) Feynman propagator, $\left(\Box-\mu^2\right)\Delta_F = i\delta^{(4)}$ |
| $\mathcal S = \left(\mathbb{D}+\mu\right)\Delta_F$ | Dirac propagator as the scalar kernel acted on |
| $T$ | Proper time (Schwinger parameter) |
| $x(\tau)$, $dR_\mu/d\tau$ | Worldline and its tangent, summed over the four slots |
| $S_0[x]$ | Scalar worldline action |
| $\tilde{Ξ}^{\mathrm{sp}}_\mu(\tau)$ | Odd (Grassmann) worldline variable; a single one is not an element of the algebra |
| $\tilde{Ξ}^{\mathrm{sp}}_\mu\tilde{Ξ}^{\mathrm{sp}}_\nu+\tilde{Ξ}^{\mathrm{sp}}_\nu\tilde{Ξ}^{\mathrm{sp}}_\mu = -\tfrac12\varepsilon_\mu\delta_{\mu\nu}e_t$ | The pair of odd variables, an element of the algebra |
| $Ξ[x]$ | Spin factor, the algebra-valued path-ordered weight |
| $\tilde\Sigma_{0k}=i\vec e_k$, $\tilde\Sigma_{jk}=\vec e_j\vec e_k$ | The six Lorentz generators, boosts in $\mathbb{M}_+$ and rotations in the real quaternion sector |
| $K_{++}$, $K_{+-}$, $K_{-+}$, $K_{--}$ | Checkerboard propagator amplitudes |
| $i\epsilon m/\hbar$ per corner | Checkerboard corner weight |
| $A_+$, $A_-$ | Checkerboard amplitudes by direction of motion |
| $\tilde{\nabla}\tilde{Ξ}^{\mathrm{sp}}_R = \mu\tilde{Ξ}^{\mathrm{sp}}_L$, $\tilde{\nabla}^{\natural}\tilde{Ξ}^{\mathrm{sp}}_L = \mu\tilde{Ξ}^{\mathrm{sp}}_R$ | The chiral mass pair, the one-sided Dirac dynamics |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- R. P. Feynman, "Space-time approach to non-relativistic quantum mechanics," *Reviews of Modern Physics* **20** (1948) 367–387, for the path integral.
- R. P. Feynman, "The theory of positrons," *Physical Review* **76** (1949) 749–759, and "Mathematical formulation of the quantum theory of electromagnetic interaction," *Physical Review* **80** (1950) 440–457, for the first-order propagator and its proper-time structure.
- H. A. Gersch, "Feynman's relativistic chessboard as an Ising model," *International Journal of Theoretical Physics* **20** (1981) 491–501, for the checkerboard model and its continuum limit.
- F. A. Berezin and M. S. Marinov, "Particle spin dynamics as the Grassmann variant of classical mechanics," *Annals of Physics* **104** (1977) 336–362, for the Grassmann worldline and the spin factor.
- L. Brink, P. Di Vecchia and P. Howe, "A Lagrangian formulation of the classical and quantum dynamics of spinning particles," *Nuclear Physics B* **118** (1977) 76–94, for the supersymmetric worldline action.
- J. Schwinger, "On gauge invariance and vacuum polarization," *Physical Review* **82** (1951) 664–679, for the proper-time representation.
- M. G. Schmidt and C. Schubert, "The worldline path integral approach to Feynman graphs," in *Loops and Legs in Quantum Field Theory* (2000), and C. Schubert, "Perturbative quantum field theory in the string-inspired formalism," *Physics Reports* **355** (2001) 73–234, for the modern worldline formulation.
- T. Jacobson and L. S. Schulman, "Quantum stochastics: the passage from a relativistic to a non-relativistic path integral," *Journal of Physics A: Mathematical and General* **17** (1984) 375–383, for the checkerboard continuum limit.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the Dirac propagator, its momentum-space form, and the propagator equation.
