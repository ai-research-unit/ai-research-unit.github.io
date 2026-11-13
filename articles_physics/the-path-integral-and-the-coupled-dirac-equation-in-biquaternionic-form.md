# __The Path Integral and the Coupled Dirac Equation in Biquaternionic Form__

## Introduction

*The Path Integral and the Dirac Equation in Biquaternionic Form* constructs the sum over worldlines that produces the free Dirac propagator. This article constructs the same sum for the **coupled** pair, with the gradient replaced by the covariant derivative of *The Gauge Principle in Biquaternionic Form*. The weight is $e^{iS/\hbar}$, the output is the propagator, and the question is what the connection does to the sum over histories.

**The coupled pair, and the covariant derivative.**

$$
\tilde\nabla_{\mathrm{gco}}\tilde\Xi_R=k_m\tilde\Xi_L,
\qquad
\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\Xi_L=k_m\tilde\Xi_R,
\qquad
\tilde\nabla_{\mathrm{gco}}=\tilde\nabla_\Phi+\frac{i\,ϙ}{\hbar}\tilde A_\Phi,
$$

with $\tilde A_\Phi$ the potential biquaternion in the material sector $\mathbb{B}_\Phi$, central per component in the abelian case, and $ϙ$ the charge. The action that produces this pair is *The Variational Principle and the Coupled Dirac Equation in Biquaternionic Form*, and the solutions in a constant potential are *The Coupled Dirac Equation in Biquaternionic Form*. Neither is re-derived here. This article takes the action as its input and asks what the exponential does with it.

**The finding, in one sentence.** The worldline integral sorts the connection into two objects and gives each a separate home: the one-form $A_\Phi$ enters the phase, and the curvature $F$ enters the spin factor. That split is the path-integral statement of the type table of *The Coupled Dirac Equation in Biquaternionic Polar Variables*, and it is why the polar reading finds the connection unable to turn the rotor while the spin still precesses in a background.

**Four consequences follow, and each is stated exactly or checked.**

- A potential with zero field strength is a boundary term along every path, so it multiplies every history by the same phase and factors out of the sum. The coupled kernel is then the free kernel times two endpoint phases, and nothing else changes. That is the path-integral form of "a constant potential is pure gauge".
- The factoring holds only for a symmetric discretisation of the gauge term. A left-endpoint rule gives a defect linear in the step, and the defect is the lattice statement that the gauge term must be a coboundary to be removable.
- Two histories with the same endpoints differ by the flux through the loop they enclose. The connection is therefore invisible to one path and visible only between two, and this is the only channel by which the one-form reaches an amplitude.
- The semiclassical evaluation gives the Lorentz path, a van Vleck determinant with no term linear in the field strength, and the spin transport along the Lorentz path.

**What the article does not do.** It does not build a second integral, does not construct a measure over fields, and does not derive fermionic statistics. The companion's limitation carries over unchanged: the worldline integral is over commuting elements of $\mathbb{B}$, and the Grassmann character sits in the odd variables that the spin factor absorbs. It also does not evaluate the kernel for a general constant field strength; that is the Schwinger computation, and §*Open Questions* states what would be needed.

**The same integral in the other coordinates is the polar companion.** *The Path Integral and the Coupled Dirac Equation in Biquaternionic Polar Variables* reads the kernel of this article in the word $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$, and finds where each of the four factors comes from. It constructs no second integral. Nothing below depends on that reading.

## Conventions

The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with $e_t=1$, $\vec e_\mu^{2}=-e_t$, $i$ central, $\mathrm{Sc}$ the coefficient of $e_t$ and $\mathrm{Tr}=2\,\mathrm{Sc}$. The pairing is the Hermitian $\mathrm{Sc}(\cdot^{*}\cdot)$. The material position is $\tilde R_\Phi=ir'_te_t+r_x\vec e_x+r_y\vec e_y+r_z\vec e_z$, with $\langle\tilde R_\Phi\rangle_{\natural}=-{r'_t}^{2}+|\vec r|^{2}$. The mass parameter is $k_m=mc/\hbar$. The worldline parameter is $\tau$ and the proper time $T$.

**The one-form of the connection.** The potential is written $\tilde A_\Phi=A_te_t+\sum_\eta A_\eta\vec e_\eta$ with real coefficients in the abelian case. Its pairing with the worldline tangent is the **real** pairing

$$
\tilde A_\Phi\cdot\mathrm{d}\tilde R_\Phi:=A_t\,\mathrm{d}r'_t+\sum_\eta A_\eta\,\mathrm{d}r_\eta,
$$

and not the algebra product. The distinction is forced by the coordinates: the temporal slot of the position is $ir'_t$, and $\partial/\partial R_t=-i\,\partial/\partial r'_t$, so a product would carry a factor of $i$ that no gauge transformation produces. The one-form is a real number at each point of the worldline.

**The sign of the gauge term.** The covariant derivative carries $+\frac{iϙ}{\hbar}\tilde A_\Phi$. A field redefinition then removes a constant potential only with the phase $e^{-iϙ\tilde A_\Phi\cdot(\tilde R_\Phi-\tilde R_{\Phi,i})/\hbar}$, as §*The Exact Kernel in a Field-Free Potential* shows by one differentiation. The worldline weight therefore carries the gauge term with a minus,

$$
S_{\mathrm{gco}}[x]=-\!ϙ\!\int\tilde A_\Phi\cdot\mathrm{d}\tilde R_\Phi ,
$$

and this is the corpus's sign and not the textbook sign. *The Coupled Dirac Equation in Biquaternionic Form* records the reason: the parent's opposite convention $\partial_\mu-\frac{iϙ}{\hbar}A_\mu$ is the same coupling with the opposite sign of $ϙ$, and this article inherits the gauge principle's sign and does not flip it. A reader who carries $+q\!\int\!A\cdot\mathrm{d}x$ from a textbook has the same physics and the opposite charge, and the free article's §*The Spin Factor in a Background Field* writes exactly that with a generic $q$: it is this article's term with $q=-ϙ$.

**The two kernels.** The propagator is the pair $\mathcal S_L,\mathcal S_R$ of *The Path Integral and the Dirac Equation in Biquaternionic Form*, now satisfying the two lines with the covariant operators,

$$
\tilde\nabla_{\mathrm{gco}}\mathcal S_R-k_m\mathcal S_L=i\delta^{(4)},
\qquad
\tilde\nabla_{\mathrm{gco}}^{\natural}\mathcal S_L-k_m\mathcal S_R=i\delta^{(4)} .
$$

Each is an element of $\mathbb{B}$ and not a scalar, and the two are the conjugates of each other in the sense of the free article. The kernel is B-valued in the coupled case for the same reason as in the free case, and nothing about that changes here.

## The Worldline of the Coupled Pair

**The action.** The worldline action of the free article gains one term,

$$
S[x,\tilde\Xi_{\mu}]=S_0[x]+S_{\mathrm{spin}}[\tilde\Xi_{\mu}]+S_{\mathrm{gco}}[x],
\qquad
S_{\mathrm{gco}}[x]=-\!ϙ\!\int_0^T\tilde A_\Phi\bigl(x(\tau)\bigr)\cdot\mathrm{d}\tilde R_\Phi(\tau),
$$

with $S_0$ the central kinetic and mass term and $S_{\mathrm{spin}}$ the odd part. The propagator is the sum

$$
\mathcal S(x,x_2)=\int_0^\infty\mathrm{d}T\int_{x}^{x_2}\mathcal{D}x\;\mathcal{F}[x]\;\exp\!\Bigl(\frac{i}{\hbar}\bigl(S_0[x]+S_{\mathrm{gco}}[x]\bigr)\Bigr),
$$

with $\mathcal{F}$ the spin factor. The odd variables are integrated at fixed $x(\tau)$, so the gauge term does not reach them: it is a functional of the material trajectory alone.

**The gauge term is central, and that is the whole of its algebraic behaviour.** $S_{\mathrm{gco}}$ is a real number for every path. Its exponential is therefore a central element of modulus one, and multiplying the weight by a central element cannot reorder the path-ordered spin factor, cannot rescale it, and cannot rotate it. The connection multiplies the weight of a history; it does not enter the history's algebra. That one sentence is the worldline form of the polar companion's type table, and every statement below is a consequence of it.

**The two lines of the pair see conjugate gauge terms.** The $L$ line's operator is $\tilde\nabla_{\mathrm{gco}}^{\natural}$, whose connection entry is $\tilde A_\Phi^{\natural}=A_te_t-\sum_\eta A_\eta\vec e_\eta$. The two kernels therefore carry

$$
S_{\mathrm{gco}}^{R}[x]=-\!ϙ\!\int\bigl(A_t\,\mathrm{d}r'_t+\textstyle\sum_\eta A_\eta\,\mathrm{d}r_\eta\bigr),
\qquad
S_{\mathrm{gco}}^{L}[x]=-\!ϙ\!\int\bigl(A_t\,\mathrm{d}r'_t-\textstyle\sum_\eta A_\eta\,\mathrm{d}r_\eta\bigr),
$$

by the two definitions and nothing else. For a purely electric potential the two gauge terms are equal, and the two lines accumulate the same phase. For a purely magnetic one they are opposite, and the two lines accumulate conjugate phases. The asymmetry is the conjugate operator's and not a choice, and it is the sum-over-histories reading of the element article's sentence that the conjugate entry is neither the negative of the entry nor a decomposition of it.

**What the sum adds to the free one.** One term in the exponent and nothing in the measure. The free article's §*The Spin Factor in a Background Field* already writes a gauge term and a curvature term; this article's contribution is to fix the gauge term's sign to the covariant derivative's and to work out what the sum then does, and the curvature term's placement on the spin is the free article's and is not redone here. **The sorting of $A$ and $F$ is therefore not a new entry in the sum but a reading of where each of the two pieces already sits.** Everything the one-form can do is decided by its cohomology on the space of paths, which is the subject of the next section.

## The One-Form and the Three Regimes

The gauge term is the integral of a one-form along a curve, so its behaviour is decided by whether that one-form is closed and whether it is exact.

**First regime: exact. The gauge term is a boundary term on every path.** Let $\tilde A_\Phi=-\tilde\nabla_\Phi\Gamma$ for a real function $\Gamma$, so that the field strength vanishes. Then along any path

$$
-\!ϙ\!\int_{x_i}^{x_f}\tilde A_\Phi\cdot\mathrm{d}\tilde R_\Phi
=ϙ\bigl(\Gamma(x_f)-\Gamma(x_i)\bigr),
$$

by the fundamental theorem of calculus, for every path with the same endpoints. The gauge term is constant on the space of paths. **It therefore factors out of the integral exactly**, and the kernel is the free kernel times the two endpoint phases. No approximation enters: the statement is exact for every path.

**The check is a lattice check, and it is where the discretisation matters.** A gauge term is a line integral, and a discretised worldline must choose a point of each segment at which to evaluate the potential. With the symmetric (midpoint) rule the telescoping is exact: over two hundred random eight-step paths with a quadratic $\Gamma$ the gauge term equals the boundary term to $2\times10^{-15}$. With the left-endpoint rule it does not: the defect is $6\times10^{1}$ at worst on the same paths, and on a fixed smooth path it halves as the step halves, $3.3\times10^{-1}$, $1.7\times10^{-1}$, $8.3\times10^{-2}$, $4.1\times10^{-2}$ for eight, sixteen, thirty-two and sixty-four steps.

**The rule is not a detail of the bookkeeping.** The defect of the left-endpoint rule is $O(h)$ and path-dependent, so a lattice sum with that rule is not gauge invariant at finite step and does not converge to a gauge-invariant limit without a counterterm. The symmetric rule makes the gauge term a coboundary exactly, at every step, on every path. That is the worldline version of the lattice-gauge statement that the link variable must sit on the link and not at its foot. **The two rules agree in the continuum and differ on the lattice, and the continuum statement is the one this article uses.**

**Second regime: closed but not exact. The flux between two histories.** Let $F=0$ in a region that is not simply connected. Then the one-form is closed and not exact, and its integral around a non-contractible loop is a nonzero number. On $\mathbb{R}^4$ no such loop exists, and the first regime covers every field-free potential. A region with a hole is a different matter, and the corpus's setting is $\mathbb{R}^4$: the statement below is about the structure of the sum and not about a physical solenoid.

**Third regime: not closed. The flux through the loop a path encloses.** Let the field strength be nonzero. Take two histories with the same endpoints, $\gamma_1$ and $\gamma_2$. Their gauge terms differ by the integral around the closed loop $\gamma_1-\gamma_2$, and Stokes's theorem gives

$$
S_{\mathrm{gco}}[\gamma_1]-S_{\mathrm{gco}}[\gamma_2]
=-ϙ\oint_{\gamma_1-\gamma_2}\tilde A_\Phi\cdot\mathrm{d}\tilde R_\Phi
=-ϙ\int_{\Sigma}F ,
$$

with $\Sigma$ any surface the loop bounds. The relative weight of the two histories is therefore $e^{-iϙ\Phi/\hbar}$ with $\Phi$ the flux. **The connection is invisible to a single history and visible only between two**, and the flux is the only channel by which the one-form reaches an amplitude.

**The check is exact for polygons.** For a constant field strength in a two-dimensional model the gauge term of a polygonal loop equals the field strength times the enclosed area to $2\times10^{-16}$ over five random hexagons, and a two-path model with endpoints $(0,0)$ and $(2,0)$ gives a difference of $-0.480$ against a field-times-area of $-0.480$. Green's theorem is exact for a linear potential on a polygon, so the identity is algebraic and the number is a check on the arithmetic and the orientation.

**What the three regimes say together.** The gauge field has exactly two ways to change a sum over histories: through the endpoints, when the potential is exact, and through the enclosed flux, when it is not. Neither channel touches the spin factor, and neither touches the measure. A field with no flux is a change of variable on the space of paths and not a force.

## The Exact Kernel in a Field-Free Potential

**The identity.** For a constant potential the covariant derivative is removed by a phase,

$$
\Bigl(\frac{\partial}{\partial R_\mu}+\frac{iϙ}{\hbar}A_\mu\Bigr)\Bigl(e^{-iϙ\tilde A_\Phi\cdot\tilde R_\Phi/\hbar}f\Bigr)
=e^{-iϙ\tilde A_\Phi\cdot\tilde R_\Phi/\hbar}\frac{\partial f}{\partial R_\mu},
$$

because each component of the connection is a central scalar and the two connection terms cancel. The identity is checked by finite differences to $2\times10^{-11}$ over the four slots, and it is exact by the centality of $A_\mu$: a central number passes through the field and cannot produce a commutator to cancel.

**The kernel.** Applying the identity to both lines of the pair gives

$$
\boxed{\;\mathcal S^{A}(x_f,x_i)=e^{-iϙ\tilde A_\Phi\cdot(\tilde R_{\Phi,f}-\tilde R_{\Phi,i})/\hbar}\;\mathcal S^{0}(x_f,x_i)\;}
$$

for every constant potential, component by component, exactly. The result agrees with §*The One-Form and the Three Regimes*: a constant potential has zero field strength, its gauge term is a boundary term along every path, and the boundary term is this phase. **The two routes to the statement are independent** — one differentiates the operator, the other sums over paths — and they agree, which is the consistency the two articles owe each other.

**What the phase means.** The exponent is $ϙ(A_t\Delta r'_t+\sum_\eta A_\eta\Delta r_\eta)/\hbar$. Its temporal slot is the energy shift $E\mapsto E+ϙcA_t$ of the coupled equation, written as a phase over the elapsed coordinate time; its spatial slots are the momentum shift $\vec p\mapsto\vec p+ϙ\vec A$, written as a phase over the displacement. **The classical substitution of the element article is one phase in the sum**, and the algebra states it with one sign because the scalar and vector potentials are the two slot types of one element.

**Three consequences, and each is a statement about the amplitude.** The modulus is unchanged, so a constant potential does not change the weight of any single history and leaves the probability of propagation at fixed endpoints alone. The pole structure in momentum space is translated and not deformed, so the mass shell is the translated hyperboloid of unchanged radius. And the spin transport is unchanged, because the phase is central and commutes with the spin factor's path ordering. **A constant potential is a change of variable on the space of histories and not a force**, and the sum over histories shows the change of variable in one line where the operator shows it in a covariance proof.

**The limit of the statement.** It holds for a potential that is constant on the region the worldline explores. For a potential that is exact but not constant the same factoring holds with $\Gamma$ in place of $\tilde A_\Phi\cdot\tilde R_\Phi$, so the kernel is the free kernel times a phase at each endpoint. For a potential with nonzero field strength no such factoring exists, and the sum is a genuinely new object: the flux reaches the relative weights, and the spin factor's curvature term reaches the spin.

## The Semiclassical Form in a Background

**The stationary phase is the Lorentz path.** Stationarity of $S_0+S_{\mathrm{gco}}$ with respect to the trajectory, with the odd variables integrated out, gives

$$
\tfrac12\,\eta_{\mu\nu}\ddot R^{\nu}=-ϙ F_{\mu\nu}\dot R^{\nu},
\qquad
F_{\mu\nu}=\frac{\partial A_\nu}{\partial R_\mu}-\frac{\partial A_\mu}{\partial R_\nu},
$$

which is the Lorentz equation with the metric raised, $\ddot R^{\mu}=-2ϙ F^{\mu}{}_{\nu}\dot R^{\nu}$. The factor two is the normalisation of the kinetic term, $\tfrac14\sum_\mu\dot R_\mu\dot R_\mu$ rather than $\tfrac12$, and it is the same factor that makes a straight line give $-\langle\tilde R_\Phi-\tilde R_{\Phi,2}\rangle_{\natural}/4T$ in the free kernel.

**The check distinguishes the coefficient from its half.** On a two-dimensional model with a constant field strength and a Euclidean metric, where the stationary point is a minimum and the comparison is unambiguous, the Euler–Lagrange residual of the path satisfying $\ddot R=-2ϙF\dot R$ falls as $1.7\times10^{-3}$, $4.3\times10^{-4}$, $1.1\times10^{-4}$, $2.7\times10^{-5}$ for ten, twenty, forty and eighty steps, which is second order. The path satisfying $\ddot R=-ϙF\dot R$ keeps a residual of $4.0\times10^{-1}$ at every resolution. The stationary path is the first and not the second, and the Euclidean signature is used for the check only: the equation displayed above is the same algebra in the corpus's metric, and the coefficient two is signature-independent.

**The phase is the classical action with the gauge term.** At the stationary path

$$
\theta_{\mathrm{act}}=\frac{1}{\hbar}\bigl(S_0[x_{\mathrm{cl}}]+S_{\mathrm{gco}}[x_{\mathrm{cl}}]\bigr),
$$

and the gauge term's contribution is $-ϙ\!\int\!\tilde A_\Phi\cdot\mathrm{d}\tilde R_\Phi$ evaluated on the Lorentz path. For an exact potential it is a boundary term and the phase is the free one plus the endpoint phases. For a field strength it is the flux through the surface between the Lorentz path and the straight line, and it is the part of the phase that the classical motion adds.

**The determinant has no term linear in the field strength.** The Gaussian fluctuations about the Lorentz path give the van Vleck factor, which is the inverse square root of the determinant of the second variation. That operator is the free one plus a term linear in $F$, the term being $-ϙF_{\mu\nu}\dot R^\nu\delta R^\mu$ after integration by parts: a potential term and not a derivative one. Its contribution to the determinant's logarithm is $-\mathrm{tr}(GV)$, with $G$ the free Jacobi kernel, and $G$ is symmetric under the exchange of the two worldline times while $F$ is antisymmetric in its two indices, so the trace vanishes. **The determinant is even in the field strength**, and the amplitude has no first-order response to a weak field.

**The check is the evenness itself.** On the two-dimensional model, at a fixed path, the ratio of the second-variation determinant in field strength $B$ to the free determinant is $-6.0\times10^{-4}$, $-2.4\times10^{-3}$, $-9.6\times10^{-3}$ and $-3.8\times10^{-2}$ for $B=0.05$, $0.10$, $0.20$ and $0.40$, and the same values for $-B$: the ratio of the two determinants is unity to $10^{-8}$ over the four field strengths. Divided by $B^{2}$ the deviation is $-0.240$, $-0.240$, $-0.239$, $-0.237$, constant to one percent, so the leading response is quadratic and the linear one is absent. This agrees with the exact constant-field determinant of the standard theory, which is a product of $\sinh(ϙF\tau)/(ϙF\tau)$ factors and is likewise even.

**The consequence in one sentence.** A weak field bends the path and moves the phase, and it does not change the amplitude to first order; the amplitude's first response is quadratic in the field strength.

**The rotor is the transport along the Lorentz path.** The spin factor's curvature term is the path-ordered exponential of the six generators contracted with $F$, and the semiclassical evaluation of that factor is the parallel transport of the spin frame along the classical path. In the free case the classical path is a straight line and the transport is trivial in the frame that moves with it; in a background the path is the Lorentz path and the transport is not trivial. **This is where the connection reaches the spin**, and only here: through the curvature, along the path's bending, and never through the one-form. The composition with the rotor's own rate, and the ratio two of the resulting precession, are *The Classical Origin of $g=2$ in Biquaternionic Form*, and the polar reading of the same division is the companion's §*The Semiclassical Word*.

## Composition, and Why the Coupling Does Not Obstruct It

**The gauge term is additive over concatenation.** For a path that passes through an intermediate point $y$,

$$
\int_{x_i}^{x_f}\tilde A_\Phi\cdot\mathrm{d}\tilde R_\Phi
=\int_{x_i}^{y}\tilde A_\Phi\cdot\mathrm{d}\tilde R_\Phi
+\int_{y}^{x_f}\tilde A_\Phi\cdot\mathrm{d}\tilde R_\Phi ,
$$

because a line integral along a concatenated curve is the sum of its pieces. The gauge term therefore splits at the intermediate point in exactly the way the free action splits, and the composition law of the proper-time kernels survives the coupling unchanged:

$$
\int\mathrm{d}^4y\;K^{\mathrm{gco}}_{T_1}(x,y)\,K^{\mathrm{gco}}_{T_2}(y,x_2)=K^{\mathrm{gco}}_{T_1+T_2}(x,x_2).
$$

**The composition law is a statement about additivity and not about the algebra.** The free article's composition argument uses the additivity of the kinetic and mass terms and the path ordering of the spin factor; the coupling adds a third additive term and changes neither of the other two. **A coupling that is the integral of a one-form composes**, and a coupling that were not a line integral — an interaction depending on the path's curvature, say — would not. That is the sharp form of the statement, and it is why the worldline formulation of gauge theory needs no special care at the composition step.

**The flux is what composes additively in the amplitude.** For two histories differing by a loop, the relative phase is the flux through the loop, and for two loops sharing an edge the fluxes add with the orientations. A chain of small loops therefore accumulates the phase linearly, and the composition of kernels at successive points is the statement that the phase accumulates along the path rather than at the junctions.

## The Checkerboard With a Connection

**The discrete model takes the coupling without approximation.** In Feynman's checkerboard, described in *The Path Integral and the Dirac Equation in Biquaternionic Form*, a path is a sequence of lightlike steps and corners, with a phase for each step and a factor $i\epsilon k_m$ for each corner. Minimal coupling adds one factor per step,

$$
\exp\Bigl(-\frac{iϙ}{\hbar}\tilde A_\Phi\cdot\Delta\tilde R_\Phi\Bigr)
\ \text{per directed step},
$$

and leaves the corner weight alone. The corner is the mass insertion. **The mass term carries no derivative, so the substitution that dresses the steps cannot reach it**, and it is invariant under the local central phase without help — which is why the coupling is a repair of the kinetic term alone in *The Variational Principle and the Coupled Dirac Equation in Biquaternionic Form*. **The corner is untouched and the step is dressed**, and that is the discrete image of the sorting of the connection into the phase.

**The lattice gauge invariance is exact and needs no limit.** Under $\tilde A_\Phi\mapsto\tilde A_\Phi-\tilde\nabla_\Phi\Gamma$, each step's phase changes by the difference of $ϙ\Gamma/\hbar$ at the step's two ends, and the product over the steps of a path telescopes to the two endpoint factors. The sum over paths is therefore invariant at every step size, with no continuum limit taken and no counterterm added. **The checkerboard is exactly gauge invariant, and the continuum integral is only formally so**, which is the correct order of the two statements and the reason the lattice formulation of gauge theory exists.

**What the discrete model shows that the continuum does not.** The link phase is evaluated on the link, which is the symmetric rule of §*The One-Form and the Three Regimes*; a rule that evaluated the potential at the step's foot would break the telescoping and the lattice invariance with it. The checkerboard therefore exhibits, in a model with finitely many paths, the statement that the gauge term must be a coboundary term to be removable. **The step phase is the coboundary and the corner is the mass**, and the two are the two ingredients of the discrete propagator.

**The two lines in one dimension.** The checkerboard is a two-dimensional model, and its one field-strength component is the electric one. For a purely electric potential the conjugate entry $\tilde A_\Phi^{\natural}$ equals $\tilde A_\Phi$, so the two lines of the pair accumulate the same step phases and the two directions of motion are weighted alike. A potential with a spatial slot reverses the entry and gives the two lines conjugate phases. The one-dimensional model therefore realises the electric case of the conjugate-entry asymmetry and not the magnetic one, and the reason is that a magnetic field needs two spatial directions.

## What the Article Adds and What It Does Not Add

**Adds.**

- The worldline integral of the coupled pair, with the gauge term as one functional of the trajectory and with its sign fixed by the covariant derivative's own sign, checked by one differentiation.
- The sorting of the connection into a one-form in the phase and a curvature in the spin factor, which is the structural statement of the article and the path-integral form of the polar companion's type table.
- The exact factoring for every field-free potential, with the two endpoint phases, and the consequence that the modulus, the pole structure and the spin transport are unchanged by a constant potential.
- The lattice statement that only a symmetric discretisation makes the gauge term a coboundary, with the defect of the left-endpoint rule measured at first order in the step.
- The flux between two histories as the only channel from the one-form to an amplitude, exact for polygons.
- The Lorentz path from stationary phase, the determinant's evenness in the field strength, and the placement of the spin transport at the curvature.

**Does not add.** No new prediction: the coupled propagator is the standard one and the kernel displayed in §*The Exact Kernel in a Field-Free Potential* is the free kernel times a phase. No measure over biquaternion fields, and no Trotter limit for the field integral. No derivation of the fermionic statistics: the worldline variables are Grassmann and the field is not, exactly as in the free article. No evaluation of the kernel for a general constant field strength. No non-abelian connection: the abelian case is the one in which the components are central, and every statement above uses that centality.

## Open Questions

1. **The kernel in a constant field strength.** The Schwinger proper-time result is known, and what is not known here is whether the biquaternion chart organises it better than the matrix chart does. The candidate is the pair's two lines as two orderings of the same proper-time integral, with the curvature term's generator contraction doing the work the gamma-matrix commutator does. The computation is a Gaussian with a path-ordered insert and is not attempted.

2. **The flux and the rotor at a caustic.** The two channels — the phase through the flux, the rotor through the curvature — are independent in the semiclassical order computed here. Where classical paths cross, the van Vleck determinant diverges and the phase is stationary with respect to two paths at once. Whether the interference of the two paths' rotors is then a phase or a genuine rotation is not settled by the free or the constant-potential case.

3. **The non-abelian connection.** Every statement above uses the centality of the components. A connection with coefficients in the algebra does not commute with the field, the gauge term does not factor at a constant potential, and the type table of the polar companion has no analogue. What replaces the sorting of $A$ and $F$ there is open, and the mixed-insertion obstruction of the element article is the place to start.

4. **The measure.** The field version of this integral, over commuting biquaternion fields, has no constructed measure in four dimensions, as in the free article. The worldline integral's Trotter limit is well defined and the field integral's is not, and the coupled case inherits the gap without widening it.

5. **The endpoint phases and the field integral.** The factoring of §*The Exact Kernel in a Field-Free Potential* is a single-particle statement. Whether the same factorization holds for the field integral's generating functional — whether a constant potential drops out of every correlation function — is the question the single-particle result suggests and does not answer.

## Summary

The sum over worldlines for the coupled pair is the free sum with one term added to the exponent, and the added term is the integral of the connection one-form along the history. Because that term is a real number, it multiplies the weight and never enters the algebra: the scale, the boost and the rotor of a history are those of the free history, and only the phase moves.

The one-form's behaviour is decided by cohomology. When the potential is exact its integral depends on the endpoints alone, so it factors out and the coupled kernel is the free kernel times two endpoint phases — exactly, for every field-free potential, and the modulus, the poles and the spin transport are untouched. When the potential is not exact, two histories with the same endpoints differ by the flux through the loop they enclose, and the relative phase $e^{-iϙ\Phi/\hbar}$ is the only way the one-form reaches an amplitude.

The curvature reaches the spin, and the semiclassical evaluation places it there: the stationary path is the Lorentz path, the phase is the classical action with the flux, the van Vleck determinant has no term linear in the field strength because the linear term is an antisymmetric trace against a symmetric kernel, and the rotor is the parallel transport along the bent path. The connection's one-form and its curvature therefore have separate homes, and the polar companion reads them as the angle and the rotor.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$, $\mathbb{B}_\Phi$ | Biquaternion algebra; its material (anti-Hermitian) sector, the home of $\tilde R_\Phi$ and $\tilde A_\Phi$ |
| $\tilde\nabla_{\mathrm{gco}}=\tilde\nabla_\Phi+\frac{iϙ}{\hbar}\tilde A_\Phi$ | Covariant derivative, acting from the left, central per component in the abelian case |
| $\tilde\nabla_{\mathrm{gco}}^{\natural}=(\tilde\nabla_\Phi)^{\natural}+\frac{iϙ}{\hbar}\tilde A_\Phi^{\natural}$ | Its quaternion conjugate, the $L$ line's operator |
| $ϙ$ | Charge; the coupling constant of the prescription |
| $\tilde A_\Phi=A_te_t+\sum_\eta A_\eta\vec e_\eta$ | Potential biquaternion, real coefficients in the abelian case |
| $\tilde A_\Phi^{\natural}=A_te_t-\sum_\eta A_\eta\vec e_\eta$ | Its conjugate; equal for a purely electric potential, opposite for a purely magnetic one |
| $\tilde A_\Phi\cdot\mathrm{d}\tilde R_\Phi=A_t\mathrm{d}r'_t+\sum_\eta A_\eta\mathrm{d}r_\eta$ | The real one-form; the algebra product is not used |
| $S_{\mathrm{gco}}[x]=-ϙ\!\int\tilde A_\Phi\cdot\mathrm{d}\tilde R_\Phi$ | The gauge term of the worldline action; its sign follows the covariant derivative's |
| $F_{\mu\nu}=\partial A_\nu/\partial R_\mu-\partial A_\mu/\partial R_\nu$ | Field strength; the curvature, and the only object that reaches the spin factor |
| $\Phi$ | Flux through the loop two histories enclose |
| $\mathcal S_L,\mathcal S_R$ | The two components of the coupled propagator, elements of $\mathbb{B}$ |
| $\mathcal S^{A},\mathcal S^{0}$ | The kernels in a constant potential and in no potential |
| $\mathcal{F}[x]$ | Spin factor, the path-ordered algebra-valued weight |
| $\Gamma$ | Real gauge function; $\tilde A_\Phi=-\tilde\nabla_\Phi\Gamma$ for an exact potential |
| $\theta_{\mathrm{gau}}=ϙ\Gamma/\hbar$ | Gauge angle |
| $\eta_{\mu\nu}$ | The metric on the four slots, used in the Lorentz equation and in the kinetic normalisation |
| $T$ | Proper time; $x(\tau)$ the worldline |
| $k_m=mc/\hbar$ | Mass parameter |

## Further Reading

- [The Path Integral and the Coupled Dirac Equation in Biquaternionic Polar Variables](the-path-integral-and-the-coupled-dirac-equation-in-biquaternionic-polar-variables.html), the companion, for this kernel read in the polar word.
- [The Path Integral and the Dirac Equation in Biquaternionic Form](the-path-integral-and-the-dirac-equation-in-biquaternionic-form.html), for the free construction this article couples: the pair, the spin factor, the checkerboard and the measure.
- [The Variational Principle and the Coupled Dirac Equation in Biquaternionic Form](the-variational-principle-and-the-coupled-dirac-equation-in-biquaternionic-form.html), for the action used here and for the current that the action produces.
- [The Coupled Dirac Equation in Biquaternionic Form](the-coupled-dirac-equation-in-biquaternionic-form.html), for the equation, the covariance proof, and the constant-potential solutions.
- [The Coupled Dirac Equation in Biquaternionic Polar Variables](the-coupled-dirac-equation-in-biquaternionic-polar-variables.html), for the type table that this article's sorting of $A$ and $F$ reproduces from the worldline side.
- [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html), for the covariant derivative, the gauge law and the sign convention inherited here.
- [The Classical Origin of $g=2$ in Biquaternionic Form](the-classical-origin-of-g-2-in-biquaternionic-form.html), for the composition of the rotor's rate with the frame's transport that gives the Larmor precession.
- J. Schwinger, "On gauge invariance and vacuum polarization," *Physical Review* **82** (1951) 664–679, for the proper-time kernel in a constant field and the even determinant.
- J. Schwinger, "Brownian motion of a quantum oscillator," *Journal of Mathematical Physics* **2** (1961) 407–432, for the proper-time method with a background field.
- M. G. Schmidt and C. Schubert, "The worldline path integral approach to Feynman graphs," in *Loops and Legs in Quantum Field Theory* (2000), and C. Schubert, "Perturbative quantum field theory in the string-inspired formalism," *Physics Reports* **355** (2001) 73–234, for the worldline treatment of the gauge term and the spin factor in a background.
- F. A. Berezin and M. S. Marinov, "Particle spin dynamics as the Grassmann variant of classical mechanics," *Annals of Physics* **104** (1977) 336–362, for the spin factor and its field-strength coupling.
- L. Brink, P. Di Vecchia and P. Howe, "A Lagrangian formulation of the classical and quantum dynamics of spinning particles," *Nuclear Physics B* **118** (1977) 76–94, for the supersymmetric worldline action used here.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the coupled Dirac propagator and the constant-potential solutions.
- H. Kleinert, *Path Integrals in Quantum Mechanics, Statistics, Polymer Physics, and Financial Markets* (World Scientific, 5th edition, 2009), for the discretisation of the gauge term and the difference between the symmetric and the endpoint rules.
