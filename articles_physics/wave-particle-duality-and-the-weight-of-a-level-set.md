# __Wave–Particle Duality and the Weight of a Level Set: Coarea, Exponential Type and the Projection That Cannot Be Local__

## Introduction

**The five articles before this one read a zero set. This one reads the measure on it.** *The Fourier Transform* reads where the symbol vanishes, *The Count of Degrees of Freedom* reads the rank of the symbol there, *Charge Conservation* reads the cokernel, *The Galilean Limit* reads the degree that makes the zero set a level set, and *The Three Positions of One Zero* reads the analytic position of that vanishing. Each answers a question of the form *where*. A level set is a set, and a set carries no number: it says where a state may live and nothing about how much of the state lives at each of its points. A field on a surface is integrated against a measure, and that measure is not given by the surface. This article supplies it.

**One object, three questions.** How much weight does a level set carry (the coarea weight, one over the gradient of the dispersion)? How far does a state reach (the exponential type of its transform, which is the radius of its support)? Can a sharp cut be local (the transform of an indicator, which is a sinc with a $1/x$ tail)? The three look unrelated and they are one operation read three times. **Each is the transform of an indicator: of a shell, of a ball, of a band.** A set becomes a function under the transform, and the three sections below read the three numbers that function carries.

**What is standard.** The coarea formula, the density of states as an integral of a delta over a shell, the van Hove singularity as a critical point of a dispersion, the Paley–Wiener theorem, the sinc kernel of an ideal low-pass filter, and the conjugate trade between resolution and range are textbook results, and they are flagged as such throughout. The corpus does not own any of them.

**What the corpus adds is the reading, and it adds it in one place.** The symbol whose gradient appears in the weight is the corpus's own $\sigma_{\mathcal{P}}$, not a generic dispersion, and the shell over which it is integrated is the surface the preceding articles have already located. The weight is therefore not a new object: it is a property of the same zero set, and it is the only property of that set the earlier articles did not read. Every display of the first four sections is a statement about that surface.

**The defect this article repairs has an exact counterpart in the one before it.** *The Fourier Transform* says that a count built on the quaternion norm would count nothing, because the norm vanishes on the state module: the form is the wrong one. Here the object is the wrong one, in the same direction. **A count built on a level set would count nothing, because a set has no measure.** The two statements are one sentence read at a form and at a set, and between them they are the reason the duality needs two arms rather than one.

**The import is marked.** That a weight on a shell is a density of states, that an exponential type is a support radius, and that an indicator is a projection are identifications, not theorems of the algebra. The article proves the three identities and marks the three identifications in §*Limits*. The algebra supplies the surface, the gradient, and the kernel, and nothing here derives a physical density from them.

**The conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_t=1$ and $\vec e_x,\vec e_y,\vec e_z$, so $\vec e_\eta^{2}=-e_t$. The wave-number element is $\tilde K_{\Phi}=i\,k_{t}^{\prime}e_t+\vec k_{\Phi}$, its quaternion conjugate is $\tilde K_{\Phi}^{\natural}=i\,k_{t}^{\prime}e_t-\vec k_{\Phi}$, and the norm $\tilde K_{\Phi}\tilde K_{\Phi}^{\natural}=-k_{t}^{\prime\,2}+k_{\Phi}^{2}$ is written in full throughout and never as a single letter. The transform of a field is written $\mathcal{F}[\tilde F]$, after *Biquaternion Continuous Harmonic Analysis*, and never as a mark on the field: a caret carries a power, a conjugation, a transposition and a construction, and the transform is none of the four. The two symbols are $\sigma_{\mathcal{P}}(k_{t}^{\prime},\vec k_\Phi)=k_{t}^{\prime\,2}-k_{\Phi}^{2}-k_m^{2}$ of *The Galilean Limit* and its affine companion $\sigma_{\mathrm{s}}=k_{\mathrm{s}}-k_{\Phi}^{2}/(2k_m)$ with $k_{t}^{\prime}=k_m+k_{\mathrm{s}}$. The capital $\kappa$ is a value of the energy wave number and not a variable of the field, and it is kept apart from $k_{t}^{\prime}$ for that reason alone.

## The Set and the Measure

**The mass shell is where the symbol vanishes, and a solution lives on it.** *The Fourier Transform* states the gradient form as one equation between numbers, $\tilde K_{\Phi}\tilde K_{\Phi}^{\natural}=-k_m^{2}$, and reads it as a surface in wave-number space on which a field is a superposition of plane waves whose labels lie on the surface. That is the whole of the *where*. A superposition is a sum of labels, and a sum of labels is not yet a weight: it says which labels occur and not how much each contributes.

**A weight is what a function needs to be integrated, and the transform supplies a function before it supplies a measure.** The on-shell field has a transform $\mathcal{F}[\tilde F]$ supported on the shell. To compute how much of the state sits at an energy, one integrates that function over the shell, and the integral needs a measure on the shell. **The measure is inherited from the volume element of wave-number space, and the inheritance is not the identity.** A surface does not carry the measure of the space it sits in; it carries that measure cut down by the surface, and the cutting is a Jacobian.

**That Jacobian is one over the gradient of the dispersion, and nothing else.** The number is fixed by the shape of the symbol and by the shape alone. Two symbols with the same zero set have two different weights whenever their gradients differ, and the corpus has exactly such a pair available: $\sigma_{\mathcal{P}}$ and $k_{t}^{\prime}$ vanish on the same shell, and $\partial\sigma_{\mathcal{P}}/\partial k_{t}^{\prime}=2k_{t}^{\prime}$ at fixed $\vec k_\Phi$. The gradient of $\sigma_{\mathcal{P}}$ in the momentum wave number actually vanishes on the shell, since $\nabla_{\vec k}\sigma_{\mathcal{P}}=2k_{t}^{\prime}\nabla_{\vec k}k_{t}^{\prime}-2\vec k_\Phi$ is zero when $\nabla_{\vec k}k_{t}^{\prime}=\vec k_\Phi/k_{t}^{\prime}$; **that is why the symbol's delta is not the useful one and the dispersion's is.** **The level set is a property of the symbol; the weight is a property of the dispersion, and the two are not the same function.** That distinction is the first thing the next section makes exact.

**The three questions are three indicators.** The weight on a shell is the transform of the indicator of the shell. The reach of a state is read off the growth of its transform, which is the transform of the indicator of a ball. The locality of a cut is decided by the transform of the indicator of a band. **An indicator is a set written as a function, and the transform turns it into a kernel whose two properties — its size and its tail — are the two numbers this article computes.**

**Why the three belong in this series rather than in a mathematics article.** Each of the three is a statement about the corpus's own object: the shell is the mass shell of the five preceding duality articles, the ball is the support of a solution of the corpus's hyperbolic equation, and the band is the spectrum of the corpus's lattice operator. The three are placed here because they are the three properties of the zero set that *where* does not answer.

## The Weight of a Level Set

**The density of states is a delta function on the symbol's zero set.** For a dispersion $k_{t}^{\prime}(\vec k_\Phi)$ the number of labels per unit energy wave number is

$$
\rho(\kappa)=\frac{1}{(2\pi)^{3}}\int_{\mathbb{R}^{3}}\delta\bigl(k_{t}^{\prime}(\vec k_\Phi)-\kappa\bigr)\,d^{3}k_\Phi ,
$$

with $\kappa$ a value of the energy wave number. The delta is the statement that only the labels on the shell contribute, and the integral is the statement that all of them do. **Nothing has been assumed about a state.** The number is a property of the symbol alone, and it is the same for every field that obeys the same equation.

**The delta is evaluated by a change of variable, and the Jacobian is the weight.** Write $k_{t}^{\prime}$ for the coordinate normal to the shell and $S_\kappa$ for the shell at the value $\kappa$. In a neighbourhood of a regular point the substitution $\vec k_\Phi\mapsto\bigl(k_{t}^{\prime},\text{coordinates on }S_\kappa\bigr)$ has Jacobian $\bigl|\nabla_{\vec k}k_{t}^{\prime}\bigr|^{-1}$, so

$$
\delta\bigl(k_{t}^{\prime}(\vec k_\Phi)-\kappa\bigr)\,d^{3}k_\Phi
=\frac{dS}{\bigl|\nabla_{\vec k}k_{t}^{\prime}\bigr|}\,d k_{t}^{\prime},
$$

and integrating over $k_{t}^{\prime}$ against the delta gives the coarea formula,

$$
\boxed{\;\rho(\kappa)=\frac{1}{(2\pi)^{3}}\oint_{k_{t}^{\prime}=\kappa}\frac{dS}{\bigl|\nabla_{\vec k}k_{t}^{\prime}\bigr|}\;}
$$

**That box is the whole of the first result, and it contains no dynamics.** A steep dispersion carries little weight and a flat one carries a great deal, because the same interval of energy spans a thin or a thick slab of wave-number space. The reciprocal gradient is exactly the thickness of that slab per unit energy. **The weight of a label on the shell is the volume of the slab that the label stands for.**

**The relativistic instance, exactly.** For the massive dispersion, obtained from $\sigma_{\mathcal{P}}=0$,

$$
k_{t}^{\prime}(\vec k_\Phi)=\sqrt{k_{\Phi}^{2}+k_m^{2}},
\qquad
\nabla_{\vec k}k_{t}^{\prime}=\frac{\vec k_\Phi}{k_{t}^{\prime}},
\qquad
\bigl|\nabla_{\vec k}k_{t}^{\prime}\bigr|=\frac{k_{\Phi}}{k_{t}^{\prime}} .
$$

The shell at fixed $\kappa$ is a sphere of radius $k_{\Phi}=\sqrt{\kappa^{2}-k_m^{2}}$ and area $4\pi k_{\Phi}^{2}$, so the weight is

$$
\rho(\kappa)=\frac{1}{(2\pi)^{3}}\,4\pi k_{\Phi}^{2}\,\frac{\kappa}{k_{\Phi}}
=\frac{k_{\Phi}\,\kappa}{2\pi^{2}},
$$

**a form with a threshold and no other structure.** At $\kappa=k_m$ the momentum vanishes and the weight vanishes with it; above the threshold it grows without bound. For the massless symbol the same computation with $k_m=0$ gives $\rho(\kappa)=\kappa^{2}/(2\pi^{2})$, **which has no threshold at all**, and that is the analytic statement of the difference between a gap and a cone.

**The factor that is not the weight is worth naming, because it is the one that is easy to miss.** If the delta is written in the symbol instead of in the dispersion, the integral returns $1/(2k_{t}^{\prime})$ times the weight, because $\delta(\sigma_{\mathcal{P}})=\delta(\kappa^{2}-k_{t}^{\prime\,2})=[\delta(k_{t}^{\prime}-\kappa)]/(2\kappa)$ at fixed $\kappa$. **The two integrals are both correct and they answer different questions**: one is the coarea cofactor of the surface, and the other counts labels per unit energy. The coarea cofactor is the geometric object; the density of states is the physical one; and the passage between them is the constant $2\kappa$, which is the Jacobian of the map from the symbol to the energy.

## The Weight Checked

**On a lattice the histogram is the definition, not an approximation to it.** A finite lattice has finitely many labels, so "the number of labels per unit energy" is a count over a bin, and the coarea formula is a claim about what that count converges to. Take the nearest-neighbour square-lattice dispersion $\sigma(k_x,k_y)=-2(\cos k_x+\cos k_y)$ on a grid of $16000^{2}$ points of the zone $[-\pi,\pi]^{2}$, and compare the bin count with the line integral of the box. This is the tight-binding dispersion and not the lattice gradient's own symbol: the latter is $a^{-1}\sum_\mu\sin(p_\mu a)e_\mu$ in *Fermion Doubling*, whose norm $a^{-2}\sum_\mu\sin^{2}(p_\mu a)$ is a different function with its own critical points, and the counting below is about the dispersion on the left:

| energy $E$ | bin count | shell integral | relative difference |
|---|---|---|---|
| $-3.0$ | $0.091547$ | $0.091277$ | $2.9\times10^{-3}$ |
| $-2.5$ | $0.099379$ | $0.099237$ | $1.4\times10^{-3}$ |
| $+1.0$ | $0.141820$ | $0.141773$ | $3.3\times10^{-4}$ |
| $+2.5$ | $0.099379$ | $0.099158$ | $2.2\times10^{-3}$ |
| $+3.0$ | $0.091547$ | $0.091358$ | $2.1\times10^{-3}$ |

**The residual is the bin width and not the formula.** At the finest bin tried the agreement is $3.3\times10^{-4}$, and it degrades on either side of that bin because a narrower bin counts fewer points and a wider one averages the curvature of the shell. The two sides compute one number because one is the coarea formula's left side and the other its right, and no numerical coincidence is available at five energies.

**The symmetry is a check the counting cannot fake.** The symbol satisfies $\sigma(-\vec k)=-\sigma(\vec k)$, so the weight at $+E$ equals the weight at $-E$, and the measured counts are equal to every printed digit at $E=\pm1.0$ and at $E=\pm2.5$. A bin count that carried a systematic error would not preserve the symmetry; a line integral that carried a wrong normalisation would preserve it and miss the value.

**The relativistic identity closes to six digits.** Evaluating the delta integral numerically by a narrow Gaussian on the dispersion, with $k_m=1$ and the normalisation of the box,

| $\kappa$ | numerical | $k_{\Phi}\kappa/(2\pi^{2})$ | relative difference |
|---|---|---|---|
| $1.5$ | $0.084960558$ | $0.084960395$ | $1.9\times10^{-6}$ |
| $2.0$ | $0.175493633$ | $0.175493438$ | $1.1\times10^{-6}$ |
| $3.0$ | $0.429869578$ | $0.429869376$ | $4.7\times10^{-7}$ |

**The error falls as the shell moves away from the threshold**, which is the signature of a Gaussian standing in for a delta: near the threshold the dispersion is flat in the shell's own direction and the stand-in is worst. The exact form is not fitted. It is the value the box gives when the gradient and the area are inserted.

## Three Shapes of Symbol, Three Weights

**The weight is a property of the gradient, so it classifies symbols by their gradients and not by their equations.** There are three cases, and the first two are the corpus's; the third is what a flat band would be.

**A linear symbol has a constant gradient, and that is the whole of the graphene result.** For $k_{t}^{\prime}=v k_{\Phi}$ the gradient has modulus $v$ everywhere, the shell is a sphere of area $4\pi\kappa^{2}/v^{2}$, and

$$
\rho(\kappa)=\frac{1}{(2\pi)^{3}}\,4\pi\frac{\kappa^{2}}{v^{2}}\,\frac{1}{v}=\frac{\kappa^{2}}{2\pi^{2}v^{3}} .
$$

Measured against a numerical delta integral at $v=1,2,4$ and $\kappa=0.2,0.4$, the relative difference is $1.0\times10^{-4}$ and $2.5\times10^{-5}$, the same at every $v$ because the only thing that changes is the constant. **The linear density of states of a Dirac cone is therefore not a property of a material. It is the statement that a linear symbol has a constant gradient, and the constant is the velocity.**

**A hyperbolic symbol has a gradient that vanishes at the threshold, and that is the whole of the massive result.** The gradient $k_{\Phi}/k_{t}^{\prime}$ tends to zero as the shell shrinks to a point at $\kappa=k_m$, so the weight tends to zero there and grows above it. **The threshold is the place where the shell has no area and the slab has no thickness**, and both vanish at the same point because the point is the same point.

**A constant symbol has no gradient, and the formula fails at the only place it is used.** If $k_{t}^{\prime}$ is constant on a surface of positive measure, then every label on that surface is on shell, the shell is not a set of measure zero, and the weight is no longer a function of the energy: it is a delta carrying the area of the whole surface. **That is what a flat band is in the transform's language** — a level set of positive measure, and therefore a pole of the propagator on a surface instead of at a point.

| dispersion | gradient | level set | weight |
|---|---|---|---|
| $v k_{\Phi}$, linear | the constant $v$ | a sphere | $\kappa^{2}/(2\pi^{2}v^{3})$ |
| $\sqrt{k_{\Phi}^{2}+k_m^{2}}$, hyperbolic | $k_{\Phi}/k_{t}^{\prime}$, zero at the threshold | a sphere in $\vec k_\Phi$ at each $\kappa$ | $k_{\Phi}\kappa/(2\pi^{2})$ |
| constant | zero | a surface of positive measure | a delta on that surface |

**The table is the classification, and the third row is not a pathology.** A flat band is a symbol with no gradient on a set, and the weight's divergence there is the exact statement that the set has positive measure. **A weight that is infinite on a set is the measure-theoretic name for a degeneracy that no perturbation removes by moving a single label.**

## Where the Weight Becomes Infinite

**The formula fails where the gradient vanishes, and the failure is local.** A regular point of the dispersion has a neighbourhood in which the shell is a graph, and there the box applies. A critical point has none: the shell either does not cross it, or crosses it in a cone, or coincides with it. **The three cases are a minimum, a saddle, and a flat band**, and only the second gives a divergence the article can compute.

**The saddle gives a logarithmic divergence, and its coefficient is exactly $1/(2\pi^{2})$.** On the square lattice the critical points of $\sigma=-2(\cos k_x+\cos k_y)$ are the four points where both sines vanish. At $(0,0)$ the symbol is $-4$ and at $(\pm\pi,\pm\pi)$ it is $+4$, so those are the extrema; at $(0,\pm\pi)$ and $(\pm\pi,0)$ it is $0$ and the second variation has one positive and one negative eigenvalue, so those are the saddles. There are two inequivalent saddles per zone, each contributing $-1/(4\pi^{2})$ to the slope, and $-1/(2\pi^{2})$ together. Approaching $\sigma=0$ along the energy, the shell integral rises as

| $E$ | weight |
|---|---|
| $0.200$ | $0.222027$ |
| $0.100$ | $0.257300$ |
| $0.050$ | $0.292125$ |
| $0.020$ | $0.338476$ |
| $0.010$ | $0.373376$ |
| $0.005$ | $0.408741$ |
| $0.002$ | $0.455032$ |
| $0.001$ | $0.489770$ |

and the seven successive slopes against $\log E$ are $-0.050889$, $-0.050242$, $-0.050585$, $-0.050350$, $-0.051021$, $-0.050520$, $-0.050115$, against the value $-1/(2\pi^{2})=-0.050661$ that the saddle's quadratic form and the zone normalisation give. **The van Hove singularity is a critical point of the symbol, and the strength of the divergence is the constant in front of the logarithm.** That constant is not fitted to the sequence. The second variation at a saddle is $k_x^{2}-k_y^{2}$ up to scale, and a single saddle gives $-1/(4\pi^{2})$ against the box as cutoff. Checked on that quadratic saddle alone, over the zone as box, the slope is $-0.025335$ between $E=10^{-2}$ and $10^{-3}$ and $-0.025330$ between $10^{-4}$ and $10^{-5}$, against $-1/(4\pi^{2})=-0.0253303$. The two inequivalent saddles add to $-1/(2\pi^{2})$, which the seven measured slopes of the lattice bracket.

**A periodic symbol must have critical points, and that is why the weight is a distribution on every lattice.** A continuous function on a compact set attains a maximum and a minimum, and at each the gradient of the symbol vanishes. So on a lattice there is always at least one energy at which the weight diverges, and the divergence is not a defect of a model. **On a lattice the weight has a singularity somewhere by necessity; on the continuum it has one only if the symbol is chosen to have one.** That is the sharpest form of the difference between the circle and the line, and it is the same difference *Fermion Doubling* states as a doubler the circle forces.

**The reading.** The transform gives three properties of a spectrum that the corpus states separately: where the states are (the shell of the previous articles), how much of each (the weight), and where the weight is infinite (the critical points). **The third is where the inversion theorem stops being a theorem**, and it is a statement about the symbol's gradient rather than about any symmetry of the equation.

## The Reach of a State

**A support radius is a growth rate read at imaginary wave number, and the corpus has the theorem.** By Paley–Wiener, a state supported in a ball of radius $R$ has a transform of exponential type $R$, entire and obeying $\bigl|\mathcal{F}[\tilde F](\zeta)\bigr|\le C\exp(R|\zeta|)$, and the type is the limit

$$
R=\lim_{b\to\infty}\frac{1}{b}\log\bigl|\mathcal{F}[\tilde F](ib)\bigr| .
$$

That is proved for $\mathbb{B}$-valued functions in *The Inverse Fourier Transform of a Symbol*, §*Paley–Wiener: Support against Exponential Type*, and quoted in *Inversion of the Biquaternion Fourier Transform*, §*What Is Quoted: Paley–Wiener and Plancherel*. Nothing here re-derives it. What follows uses it and adds the two statements those articles do not carry.

**The limit is approached from below, and how far below is arithmetic.** For the indicator of an interval of half-width $1$ the estimate at finite $b$ is exactly $1+b^{-1}\log\bigl[(1-e^{-2b})/b\bigr]$, which is $0.94522467$ at $b=80$ and $0.96828016$ at $b=160$. On a $C^{\infty}$ bump of the same radius it is $0.39795817$, $0.58025586$, $0.71150692$, $0.80287960$, $0.86541704$ at $b=10,20,40,80,160$. **The smoother the state, the further out the limit is pushed**, because smoothness is the property that makes the transform decay fast on the real axis and therefore grow slowly on the imaginary one. Reading a type off a numerical transform means knowing which of the two lines one is reading.

**The first statement the maths articles do not carry: a front moves the type at exactly the speed of the front.** Take $u(x,t)=f(x-t)$ with $f$ the indicator of an interval of half-width $1$. Its transform is $\exp(i\zeta t)\mathcal{F}[f](\zeta)$, so at $\zeta=ib$ the modulus gains the factor $e^{bt}$ and the type gains exactly $t$. Measured at $b=80$ and at $b=160$, the increments are $0.500000$, $0.500000$ and $1.000000$ for $\Delta t=0.5,0.5,1.0$, **identical at the two values of $b$**. Finite propagation is therefore not an extra axiom about the equation. It is the statement that the exponential type grows at a finite rate, and the rate is the speed of the front.

**The second: the degree of the symbol decides whether that rate is finite at all.** For the heat equation the multiplier is $\exp(-\zeta^{2}t)$, which at $\zeta=ib$ is $e^{b^{2}t}$: the estimate $(1/b)\log e^{b^{2}t}=bt$ grows with $b$ without bound, measured as $0.4000$, $0.8000$, $1.6000$ at $b=20,40,80$ for $t=0.02$ and $2.0000$, $4.0000$, $8.0000$ for $t=0.1$. For the Schrödinger equation the multiplier is $\exp(i\zeta^{2}t)$ and the same happens along the ray $\zeta=b(1-i)$. **The test is the power of $\zeta$ in the exponent and whether it carries an $i$**: linear in $i\zeta$ gives a finite type growing at a constant rate, and quadratic in $\zeta$, with or without the $i$, gives no finite type at all.

## Two Numbers Read in Two Places

**A decay rate and a support radius are numbers read at the two ends of one axis, and the exclusivity is already a corollary in the corpus.** A decay rate is a pole: the Euclidean Green's function has transform $1/(\zeta^{2}+k_m^{2})$, with poles at $\zeta=\pm ik_m$, and the rate is the distance of the pole from the real axis. A support radius is a type: the indicator's transform is entire, and its radius is the growth at $i\infty$. A compactly supported state therefore has no pole and no decay constant, and a state with a pole at a finite distance has no compact support. That is not a trade-off but the corollary of *Inversion of the Biquaternion Fourier Transform*, §*Exponential Type and the Tail*, which states it as the requirement that a solution of compact support carry a vanishing datum at every pole.

**It is why the corpus needs two Green's functions and gets no contradiction from having both.** The retarded one is supported on the cone and has no decay constant; the Euclidean one has the decay constant $k_m$ and infinite reach. They are not two approximations of one object but the two ends of one axis, and which of them is physical is decided by the contour the inverse transform is taken on. **The companion article reads the same axis from the other side.** *The Three Positions of One Zero* places a zero on the real axis, on the imaginary line and off both, and reads the three as a bound state, a decay and a resonance. That article reads the position of the zero; this one reads the height of the pole and the growth at infinity, and a decaying state is a zero that has left the real axis.

## The Cut That Cannot Be Sharp

**An exact projection is an indicator, and the reason is one line.** Let $P$ be a multiplier whose symbol is $\chi(\vec k_\Phi)$, so that $P^{2}$ has symbol $\chi^{2}$ pointwise. Then

$$
P^{2}=P
\quad\Longleftrightarrow\quad
\chi^{2}(\vec k_\Phi)=\chi(\vec k_\Phi)\ \text{at every } \vec k_\Phi
\quad\Longleftrightarrow\quad
\chi(\vec k_\Phi)\in\{0,1\}\ \text{at every } \vec k_\Phi .
$$

**Idempotence is a pointwise condition on the symbol, so a projection selects a set.** Measured, the residual $\max|\chi^{2}-\chi|$ is exactly $0$ for the indicator of an interval, and $0.250000$ for the Gaussian $\exp(-\zeta^{2}/2)$ and for the tent $(1-|\zeta|)_{+}$. The two smooth symbols each sit at $\chi=1/2$ somewhere, and there $\chi^{2}-\chi=-1/4$ exactly, which is why the residual is a quarter and not something smaller. **A projection whose symbol is continuous is locally constant, and a projection that is not locally constant is discontinuous**, and for a symbol that takes values in $[0,1]$ the largest possible violation is one quarter.

**So the algebraic fact and the spatial fact are one fact.** *Decoherence as Idempotent Projection* establishes that full dephasing is a trace-preserving conditional expectation, an exact projection in the operator algebra, and it is careful to say that this is a statement about the algebra of operators and not about space. **The transform supplies the spatial half**: an exact projection has an indicator for a symbol, an indicator is the indicator of a set, and a set has an edge. Whether that edge is sharp is a question about the symbol; whether the projection acts locally is a question about its kernel; and the next section shows that the two questions have one answer.

## The Tail a Sharp Edge Forces

**The transform of an indicator is a sinc, and a sinc has a $1/x$ tail.** For the band $[-B,B]$ the kernel is

$$
K(x)=\frac{1}{2\pi}\int_{-B}^{B}e^{-i\zeta x}\,d\zeta=\frac{\sin(Bx)}{\pi x},
$$

whose envelope is exactly $1/(\pi x)$. Measured at the six points where $\sin(Bx)=\pm1$, with $B=3$, the product $x\,K(x)$ is $0.31830989$ at each of $x=0.523599$, $2.617994$, $4.712389$, $6.806784$, $8.901179$, $10.995574$, **and $1/\pi=0.31830989$.** The envelope is not asymptotic: it is attained at every peak, and the only thing that decays is the peak-to-peak matching.

**The tail's order is the order of the symbol's first broken derivative, and that is the same ladder as the weight.** The indicator jumps, so its kernel decays as $1/x$; a tent has a broken slope and its kernel decays as $1/x^{2}$; a symbol with no jump and no broken slope has no power tail at all. **The order of the tail counts the derivatives the cut fails to have**, and the counting is exact rather than asymptotic.

**So resolution and range are conjugate, and the trade is quantitative.** A projection with a sharp band edge acts in space by convolution with a $1/(\pi x)$ kernel, so its range is infinite. A projection with a graded edge is not a projection at all. **No Fourier multiplier both projects exactly and acts locally**, and the two deficits are one number apart: the width of the edge is the width of the range, reciprocally. An operator that is local and exact exists — multiplication by the indicator of a set in position — but it is not a multiplier, and that is the whole of the distinction.

**The lattice is where the obstruction disappears, and it closes a loop with the weight.** On a circle every symbol is periodic, the band is closed by construction, and an idempotent multiplier is available with no tail: the indicator of a set of sites is a projection with finite range. **A finite band and a continuous space cannot both be had**, and a projection is exactly the object that forces the choice. That is the same obstruction the weight's saddle states as a divergence the circle forces, stated as a tail the line forces.

## The Three Are One Statement

**One operation, three objects.** Each of the three results is the transform of the indicator of a set, and the number each produces is a property of that set's geometry.

| the set | its indicator | the transform | the number |
|---|---|---|---|
| the shell $k_{t}^{\prime}=\kappa$ | $\delta\bigl(k_{t}^{\prime}(\vec k_\Phi)-\kappa\bigr)$ | the weight $1/\bigl|\nabla_{\vec k}k_{t}^{\prime}\bigr|$ | a density of labels per unit energy |
| a ball of radius $R$ | the indicator of the ball | a function of exponential type $R$ | the reach of the state |
| a band $[-B,B]$ | the multiplier's symbol | $\sin(Bx)/(\pi x)$ | the range of the projection |

**The middle row is the one that looks different and is not.** A support is a set in position space, and its indicator is a state. The transform of that state is a function whose growth at infinity is the set's radius, so the radius is read off the transform exactly as the weight is read off the gradient. **In all three rows the set is the input and a number about the set is the output, and in all three the transform is the map between them.**

**The three numbers are one number in one case and not in general.** For a symbol of the form $\sigma=v k_{\Phi}$ the gradient is the velocity, the shell is a sphere, and the weight is a power of the energy; the type of a state supported in a ball of radius $R$ is $R$; and the range of a projection with band edge $B$ is $1/B$. **The weight has the dimension of an inverse energy, the type has the dimension of a length, and the range has the dimension of a length**, so the three are not commensurable as they stand, and the article does not claim they are. What they share is the structure, not the unit.

## The Duality in This Reading

**The wave arm is a level set and the particle arm is a count, and the weight is the only place the two meet.** *The Fourier Transform* states the duality as two forms: the quaternion norm's level set on the wave side and the Hermitian form's conserved number on the particle side. A level set alone cannot produce a count, because a count is an integral and an integral needs a measure. **The weight supplies exactly that measure, and it supplies it from the wave side**: it is computed from the symbol's gradient, and it is what the particle arm's integral runs against.

**That is the precise sense in which the count is the level set plus the weight.** A spectrum is a measure, and a measure is a set and a density. The five preceding articles supply the set; this one supplies the density. **The count of states below an energy is the integral of the weight over the energies below it**, and it is a number the state's own normalisation does not enter.

**The defect and its repair are one sentence apart.** A count built on the quaternion norm would count nothing, because the norm vanishes on the state module: that is the defect *The Fourier Transform* names. A count built on a level set would count nothing, because a set has no measure: that is the defect this article names. **The two are the same sentence read at a form and at a set**, and together they are the reason the duality cannot be reduced to one arm.

**What this article does not do to the duality.** It adds no form, no arm and no equation. It reads one property of the zero set the earlier articles located, and it reads that property with the transform the first article of the series introduced. **The table of arms in *Where the Duality Lands* is unchanged.** A row for this article would read *the gradient arm, as a measure on its level set*, which is a property of a row already in the table and not a new arm; and that is the sense in which the article is a footnote to the table rather than an entry in it.

## Limits

**The weight is a distribution and not always a function.** At a critical point of the symbol the box diverges, and at a flat band it is a delta on a surface. Both are correct statements about a measure and both are unusable as a density. The article states the divergence and its coefficient and does not attempt to regularise it, because the regularisation is a property of the state and not of the symbol.

**Coarea needs a symbol with a non-vanishing gradient on the shell.** The change of variable is a local diffeomorphism, and at a critical point it is not one. Everything in §*The Weight of a Level Set* is therefore a statement about regular points, and §*Where the Weight Becomes Infinite* is the statement about the rest.

**The density of states is a property of a spectrum and not of a system.** It counts labels. That a label is a state, and that the count is what a detector measures, are identifications imported from the corpus's quantum articles and not derived here. **The number $\rho$ is not an observable**; it is a bookkeeping device for labels, and every measurement statement about it is an import.

**Paley–Wiener is stated in one variable and used here on a four-dimensional transform.** In one variable the formula $\lim(1/b)\log\lvert\mathcal{F}[\tilde F](ib)\rvert$ returns the one-sided reach, and the type is the larger of the two sides, which is why the front in §*The Reach of a State* is the far edge and not the near one. In four variables the type is a function of direction, the support is a convex body, and its support function is the type. The one-dimensional statements above are the sections of that function, and the article does not claim the multivariate theorem.

**The reach is a property of the state and not of the algebra.** A support is a support of a particular solution. Two solutions of one equation have two different types, and nothing in the algebra fixes either. **What the algebra fixes is the equation's symbol, and the symbol's degree decides whether a finite type is possible at all**, as the heat and Schrödinger entries of §*The Reach of a State* state.

**The sinc tail is not a statement that measurement is impossible.** It is the statement that an exact projection and a finite range cannot both hold. An approximate projection with a finite range exists for every pair of tolerances, and the trade is quantitative rather than absolute. **Nothing here contradicts *Decoherence as Idempotent Projection***, which proves the algebraic statement at full strength; the two statements are about different objects.

**No claim of novelty in physics.** The coarea formula, the density of states, the van Hove singularity, the Paley–Wiener theorem, the sinc kernel and the resolution–range trade are standard. The organisation of them as three readings of the transform of an indicator, and the location of the weight on this corpus's own shell, are the corpus's, and they are an organisation of identities rather than a new identity.

## Summary

**A level set is a set, and a set carries no measure.** The five preceding articles of this series read the zero set; none of them reads how much of a state sits on it, because a set does not say.

**The weight of a label on the shell is one over the gradient of the dispersion.** The delta function's change of variable gives the coarea formula, and the Jacobian is the thickness of the slab of wave-number space that the label stands for. Steep symbols carry little weight, flat ones carry a great deal.

**The relativistic weight is $k_{\Phi}\kappa/(2\pi^{2})$, exact.** It vanishes at the threshold $\kappa=k_m$ and grows without bound above it, the massless case is $\kappa^{2}/(2\pi^{2})$ with no threshold, and a linear symbol gives the constant-gradient result $\kappa^{2}/(2\pi^{2}v^{3})$.

**The checks, in one place.**

| what is checked | how | residual |
|---|---|---|
| the coarea formula, five energies | bin count against line integral, $16000^{2}$ | $3.3\times10^{-4}$ at the finest bin |
| the weight's symmetry | $\rho(+E)=\rho(-E)$ to every printed digit | exact |
| the relativistic weight | delta integral against $k_{\Phi}\kappa/(2\pi^{2})$ | $4.7\times10^{-7}$ at $\kappa=3$ |
| the linear weight | delta integral against $\kappa^{2}/(2\pi^{2}v^{3})$ | $2.5\times10^{-5}$ |
| the van Hove coefficient | slope against $\log E$, seven intervals | $-0.0501$ to $-0.0510$ against $-0.050661$ |
| the exponential type | indicator at $b=80,160$ | $0.94522467$, $0.96828016$ |
| the front's speed | increments of the type at $t=0,0.5,1,2$ | $0.5$, $0.5$, $1.0$ at two values of $b$ |
| the idempotence residual | indicator, Gaussian, tent | $0$, $0.25$, $0.25$ |
| the sinc envelope | $x\,K(x)$ at six peaks, $B=3$ | $0.31830989$ against $1/\pi$ |

**The weight diverges at a critical point of the symbol, and the divergence is the van Hove singularity.** Its coefficient is $1/(2\pi^{2})$ on the square lattice and the measured slopes sit within $2\%$ of it. A flat band is the case where the level set has positive measure, and the weight is then a delta on a surface.

**A support radius is a growth rate at imaginary wave number, and a decay rate is a distance from the real axis.** The two are read at the ends of one axis and are mutually exclusive in one variable, which is the corollary *Inversion of the Biquaternion Fourier Transform* states as the vanishing datum a compactly supported solution needs at every pole.

**An exact projection is an indicator, and an indicator is a sinc.** A continuous $0$–$1$ symbol is locally constant, the largest violation among symbols valued in $[0,1]$ is one quarter, and an exactly idempotent multiplier is never local. The lattice closes the band and removes the tail, which is the same obstruction as a divergence the circle forces, stated as a tail the line forces.

**The count is the level set plus the weight, and that is where the two arms meet.** The preceding articles supply the set and this one supplies the density, so a spectrum is a measure rather than a set. With *The Fourier Transform*'s statement that the quaternion norm would count nothing, this is the second half of one sentence.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathcal{F}[\tilde F]$ | the transform of a field, written without a mark on the field |
| $\tilde K_{\Phi}$ | the wave-number element $i\,k_{t}^{\prime}e_t+\vec k_{\Phi}$ |
| $\tilde K_{\Phi}\tilde K_{\Phi}^{\natural}$ | its norm, $-k_{t}^{\prime\,2}+k_{\Phi}^{2}$, and $-k_m^{2}$ on shell |
| $k_{t}^{\prime}$ | the energy wave number, $E/(\hbar c)$ |
| $\vec k_{\Phi}$, $k_{\Phi}$ | the momentum wave number and its modulus |
| $k_m$ | the mass wave number, $mc/\hbar$ |
| $\kappa$ | a value of the energy wave number; a constant, not a variable |
| $\sigma_{\mathcal{P}}$ | the second-order symbol, $k_{t}^{\prime\,2}-k_{\Phi}^{2}-k_m^{2}$ |
| $\sigma_{\mathrm{s}}$ | the affine symbol, $k_{\mathrm{s}}-k_{\Phi}^{2}/(2k_m)$ |
| $k_{\mathrm{s}}$ | the energy above rest, $k_{t}^{\prime}-k_m$ |
| $\rho(\kappa)$ | the weight on the shell, the density of labels per unit energy |
| $\bigl|\nabla_{\vec k}k_{t}^{\prime}\bigr|$ | the modulus of the gradient of the dispersion in wave-number space |
| $R$ | the radius of a support, equal to the exponential type of the transform |
| $b$ | the imaginary wave number $i\zeta=ib$ at which the type is estimated |
| $\chi$ | the symbol of a multiplier, whose idempotence is $P^{2}=P$ |
| $B$ | the half-width of a band, whose kernel is $\sin(Bx)/(\pi x)$ |

## Further Reading

- [Wave–Particle Duality and the Fourier Transform](../articles_physics/wave-particle-duality-and-the-fourier-transform.html), for the two arms, the boxed symbol identity, and the statement that a count built on the quaternion norm would count nothing.
- [Wave–Particle Duality and the Count of Degrees of Freedom](../articles_physics/wave-particle-duality-and-the-count-of-degrees-of-freedom.html), for the rank of the symbol on and off the cone, which is the *where* this article's *how much* follows.
- [Wave–Particle Duality and the Three Positions of One Zero](../articles_physics/wave-particle-duality-and-the-three-positions-of-one-zero.html), for the zero set whose analytic position is read as a bound state, a decay and a resonance.
- [Wave–Particle Duality and the Galilean Limit](../articles_physics/wave-particle-duality-and-the-galilean-limit.html), for $\sigma_{\mathcal{P}}$, $\sigma_{\mathrm{s}}$ and the degree of the symbol that decides whether a finite exponential type is possible.
- [Fermion Doubling and the Nielsen–Ninomiya Theorem in Biquaternionic Form](../articles_physics/fermion-doubling-and-the-nielsen-ninomiya-theorem-in-biquaternionic-form.html), for the square-lattice symbol of §*The Weight Checked* and for the circle that closes the band.
- [Decoherence as Idempotent Projection](../articles_physics/decoherence-as-idempotent-projection.html), for the algebraic projection whose spatial half is §*The Cut That Cannot Be Sharp*.
- [The Biquaternion d'Alembertian and Its Green's Functions](../articles_physics/the-biquaternion-dalembertian-and-its-greens-functions.html), for the retarded and Euclidean Green's functions whose two tails are the two numbers of §*Two Numbers Read in Two Places*.
- [The Inverse Fourier Transform of a Symbol](../articles_maths/the-inverse-fourier-transform-of-a-symbol.html), for the Paley–Wiener pair proved in the corpus, the definition of exponential type used here, and the remark that a polynomial symbol never has finite reach.
- [Inversion of the Biquaternion Fourier Transform: Poles, Tails and the Degenerate Set](../articles_maths/inversion-of-the-biquaternion-fourier-transform-poles-tails-and-the-degenerate-set.html), for the corollary that a solution of compact support needs a vanishing datum at every pole, which is the exclusivity of §*Two Numbers Read in Two Places*.
