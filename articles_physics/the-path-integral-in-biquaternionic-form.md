# __The Path Integral in Biquaternionic Form__

## Introduction

The Feynman path integral writes the transition amplitude of a quantum system as a sum over histories,

$$
K(x_f,t_f;x_i,t_i)=\int\mathcal{D}x(t)\;e^{iS[x]/\hbar},
\qquad
S[x]=\int_{t_i}^{t_f}L(x,\dot x)\,dt,
$$

in which every path from $(x_i,t_i)$ to $(x_f,t_f)$ contributes the phase $e^{iS[x]/\hbar}$. The sum is formal: it is defined as a limit of finite-dimensional oscillatory integrals, and its convergence is governed by the same $i\epsilon$ prescription that the companion article *The Feynman Propagator in Biquaternionic Form* treats in momentum space.

This article asks of the phase the question that the read-list articles have already asked twice. The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ contains a unique **central** root of $-1$ up to sign — the scalar imaginary $i$ — and it also contains **real non-central** roots: the unit pure real quaternions $\hat{\mu}$ that name spin directions, of which the quaternion units $e_1,e_2,e_3$ are the coordinate cases. The companion article *The Schrödinger Equation in Biquaternionic Form* settled which of these is the $i$ of the state-vector equation, and showed that a non-central root breaks norm preservation. The companion article *The Feynman Propagator in Biquaternionic Form* settled where the $i\epsilon$ lives — along the $ict$ axis of the material sector $\mathbb{M}_-$ — and argued that the algebra names that axis without choosing its orientation. The companion article *The Wick Rotation in the Biquaternion Universe* settled that $t\mapsto-i\tau$ is, in this framework, the identification of the material sector $\mathbb{M}_-$ with the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, obtained by relabeling the imaginary time coefficient as a real one. The path integral's phase is the object on which all three of these results bear at once.

The finding is stated at the outset. **The algebra supplies a canonical complex structure for the phase — the central scalar imaginary — so the phase factors are central unitary elements of $\mathbb{C}_{\mathbb{B}}$ rather than a choice of a preferred spin axis. It locates the phase exponent $iS/\hbar$ in the material sector $\mathbb{M}_-$, along the same $ict$ direction as the propagator's $i\epsilon$ and the thermal analyticity strip. And it exhibits the Wick rotation as the transfer that turns the oscillatory sum over paths into a decaying one.** What it does not supply is the measure, the action, or the space of paths; the last is a gap the algebra cannot close, because $\mathbb{B}$ is finite-dimensional and the space of paths is not. The article reports the contributions and the gap.

## The Sum over Paths

For a non-relativistic particle of mass $m$ in a potential $V$, the path integral is the continuum limit of a product of short-time kernels. Over a time $T=t_f-t_i$ divided into $N$ steps of length $\varepsilon=T/N$,

$$
K(x_f,t_f;x_i,t_i)
=\lim_{N\to\infty}\int\prod_{k=1}^{N-1}dx_k\;\prod_{k=0}^{N-1}K_\varepsilon(x_{k+1},x_k),
$$

with the single-step kernel

$$
K_\varepsilon(x',x)=\Big(\frac{m}{2\pi i\hbar\varepsilon}\Big)^{1/2}
\exp\Big[\frac{i}{\hbar}\Big(\frac{m(x'-x)^2}{2\varepsilon}-\varepsilon\,V(x)\Big)\Big]+O(\varepsilon^2).
$$

Two structural properties follow directly from this definition and are the ones the biquaternion reading has to respect.

**Composition.** The kernel is a semigroup in time:
$$K(x_f,t_f;x_i,t_i)=\int dx\;K(x_f,t_f;x,t)\,K(x,t;x_i,t_i).$$
This is the statement that the sum over paths is a sum over the intermediate point at which a path crosses time $t$; it is the same completeness relation that any representation of the evolution operator must satisfy.

**Interference.** Two classes of paths whose actions differ by $\Delta S$ contribute
$$e^{iS_1/\hbar}+e^{iS_2/\hbar}=2\cos\!\Big(\frac{\Delta S}{2\hbar}\Big)e^{i\bar S/\hbar},
\qquad \bar S=\tfrac12(S_1+S_2),$$
so the intensity has fringes with complete destructive nodes at $\Delta S=(2n+1)\pi\hbar$. More generally, $N$ equal-amplitude paths with successive phase $\delta$ sum to
$$\Big|\sum_{k=0}^{N-1}e^{ik\delta}\Big|=\Big|\frac{\sin(N\delta/2)}{\sin(\delta/2)}\Big|.$$
The phase is therefore the entire dynamical content of the sum: the measure counts paths, and the phase makes them interfere.

**Classical limit.** In the limit $\hbar\to0$ the stationary-phase approximation retains only the paths with $\delta S=0$, i.e. the classical trajectories, and the leading correction is the Gaussian integral over the fluctuations. The biquaternion framework does not change this; it changes only what the symbol $i$ in the exponent denotes, which is the subject of the next section.

## The Biquaternion Phase

### The exponent lies in the material sector

The action $S[x]$ is a real scalar — a Lorentz scalar, in the covariant case. The exponent of the phase is therefore

$$
\frac{iS[x]}{\hbar}=\Big(\frac{S[x]}{\hbar}\Big)\,i\,e_0,
$$

a purely imaginary scalar, with zero vector part. By the defining form of the two sectors — $\mathbb{M}_-$ is the anti-Hermitian subspace, imaginary scalar part and real vector part; $\mathbb{M}_+$ is the Hermitian subspace, real scalar part and imaginary vector part — this exponent is an element of $\mathbb{M}_-$:

$$
\frac{iS}{\hbar}\in\mathbb{C}_{\mathbb{B}}\cap\mathbb{M}_-.
$$

It lies along the imaginary-scalar direction that the framework writes as $ict$. This is the same direction in which the companion article on the Feynman propagator locates the deformation $-i\epsilon\,e_0$, and it is the direction the companion article on the Wick rotation relabels as real. The three are the same algebraic object seen in three problems.

The generator of the phase is thus $i e_0$, the central element that exchanges the two sectors, $i\,\mathbb{M}_\pm=\mathbb{M}_\mp$. This is consistent with the companion article on the harmonic oscillator, which identifies the oscillator's $U(1)$ phase as generated by the sector-exchanging element $ie_0$.

### The phase is central and unitary

Because the exponent is a complex scalar, the phase factor is a **central** element of $\mathbb{B}$:

$$
e^{iS/\hbar}=\cos\!\Big(\frac{S}{\hbar}\Big)e_0+\sin\!\Big(\frac{S}{\hbar}\Big)\,i e_0\;\in\;\mathbb{C}_{\mathbb{B}}=\operatorname{span}_{\mathbb{R}}\{e_0,ie_0\}.
$$

Its Hermitian conjugate is its inverse, $(e^{iS/\hbar})^\dagger=e^{-iS/\hbar}$, so it is **unitary** in the sense of the framework's unitary group $U(2)$:

$$
e^{iS/\hbar}\,\big(e^{iS/\hbar}\big)^\dagger=e_0.
$$

It is **not**, however, a **unit-norm-form** element. The Lorentz rotors are the biquaternions with $\tilde{\Lambda}\bar{\tilde{\Lambda}}=e_0$ (the group $SL(2,\mathbb{C})$), and for a central element $\lambda e_0$ this condition reads $\lambda^2=1$, so $\lambda=\pm1$. For the phase,

$$
e^{iS/\hbar}\,\overline{\big(e^{iS/\hbar}\big)}=e^{2iS/\hbar}\neq e_0
\qquad\text{unless } S/\hbar\in\pi\mathbb{Z}.
$$

So the phase is a unitary element and not a Lorentz rotor. The two notions of "unit" — $\tilde U\tilde U^\dagger=e_0$ for $U(2)$ and $\tilde{\Lambda}\bar{\tilde{\Lambda}}=e_0$ for $SL(2,\mathbb{C})$ — must be kept apart here, and the path-integral phase belongs to the first.

### Consequences of centrality

Because each phase factor is central, it commutes with every element of $\mathbb{B}$. Three consequences are immediate.

1. **The amplitude is a complex scalar.** The integral of central elements is central, so the full kernel is
   $$K(x_f,t_f;x_i,t_i)=\mathcal{K}\,e_0,\qquad \mathcal{K}\in\mathbb{C},$$
   a complex number times the identity. It is not a general biquaternion.

2. **The phase multiplies every spinor component equally.** In the state module $\mathbb{B}\tilde{P}\cong\mathbb{C}^2$ of the Schrödinger article, a central phase acts as the same scalar on both components, $e^{iS/\hbar}\psi$. A non-central phase would mix or relatively phase the components; a central one does not.

3. **The overall phase cancels in the state.** With $\psi\mapsto e^{iS/\hbar}\psi$ and $\tilde{\rho}=\psi\psi^\dagger/\mathrm{Tr}(\psi^\dagger\psi)\in\mathbb{M}_+$, centrality gives
   $$\tilde{\rho}\;\longmapsto\;\frac{e^{iS/\hbar}\psi\,\psi^\dagger e^{-iS/\hbar}}{\mathrm{Tr}(\psi^\dagger\psi)}=\tilde{\rho},$$
   so the global phase of a single path is unobservable, and the Born probabilities $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ are unchanged. Only **relative** phases — differences of actions between paths — are observable, which is exactly what the interference formula of the previous section says.

### The sector chain

The three facts above arrange themselves into a chain that is worth stating separately, and labelling for what it is. The exponent of the phase is an element of the **material sector** $\mathbb{M}_-$; the phase itself is an element of the **center** $\mathbb{C}_{\mathbb{B}}$; the amplitude it produces is central; and the state built from the amplitude, $\tilde{\rho}=\psi\psi^\dagger$, is an element of the **informational sector** $\mathbb{M}_+$. The path integral's phase is thus the point at which a quantity defined along a material-sector trajectory (the action, $\int L\,dt$) is converted, through the central complex structure, into an amplitude that yields an informational-sector state.

That chain is a structural reading of the algebra, not a derivation of anything. The algebra does not say that the action *must* be a real scalar; it says that if the action is a real scalar, its phase is central and its exponent lies in $\mathbb{M}_-$.

## Why the Central Imaginary, and Not a Quaternion Unit

The phase could be written with any root of $-1$ in place of $i$. The alternatives among the real roots are the non-central ones: the unit pure real quaternions $\hat\mu$, of which the quaternion units $e_j$ are the coordinate cases. Writing the phase with such a root $J$ gives, per path, the element $e^{JS/\hbar}$, a unit real quaternion when $J=\hat\mu$; and the three reasons the Schrödinger article gave for rejecting $J$ in the state-vector equation apply here as well.

**The generator need not be anti-Hermitian.** Taking $J\tilde{H}$ in place of $i\tilde{H}$ changes the generator of the flow from $-i\tilde{H}/\hbar$ (anti-Hermitian, hence norm-preserving) to $-J\tilde{H}/\hbar$, which is anti-Hermitian only if $J$ commutes with $\tilde{H}$. With $J=e_3$ and $\tilde{H}=ie_1$ one has, using $e_3e_1=e_2$,
$$J\tilde{H}=e_3(ie_1)=i\,e_2,$$
which is Hermitian, not anti-Hermitian, since $(ie_2)^\dagger=ie_2$. The flow $\exp(-tJ\tilde{H}/\hbar)$ is then not unitary; at $t=\pi\hbar/2$ its exponent is $-\tfrac{i\pi}{2}e_2$ and
$$\tilde U^\dagger\tilde U=e^{-i\pi e_2}=\cosh(\pi)\,e_0-i\sinh(\pi)\,e_2\neq e_0,$$
so the norm is not preserved. A path integral built on this phase would not reproduce a unitary evolution.

**The phase is not a global phase.** Even where a fixed non-central root gives a unitary one-parameter group — as $J=e_3$ does — the phase it produces is not shared by the two spin components. Under the isomorphism $e_k\mapsto-i\sigma_k$ of the companion articles, the phase $e^{e_3\theta}$ maps to
$$e^{e_3\theta}\;\longmapsto\;\cos\theta\,I_2-i\sin\theta\,\sigma_3=\operatorname{diag}\!\big(e^{-i\theta},\,e^{+i\theta}\big),$$
so it multiplies the two components by opposite phases. It is a **relative** phase, that is, a spin rotation, not the single global phase a path is supposed to contribute. A genuinely global phase must be central.

**The choice is extra input.** The central imaginary is supplied by the algebra: $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ contains $\mathbb{C}$ by construction, and within the center the roots of $-1$ are exactly $\pm i$. A real non-central root is a point of the Bloch sphere, and using one fixes a preferred spin axis that the algebra does not supply. The same observation is made by Adler's quaternionic quantum mechanics, where a complex structure must be chosen as additional input.

**An honest qualification.** A *fixed* non-central root $J$ does not destroy interference: two paths with phases $e^{J S_1/\hbar}$ and $e^{J S_2/\hbar}$ still combine to $2\cos(\Delta S/2\hbar)$ times a unit element of the plane $\operatorname{span}\{e_0,J\}$. What fails is not interference but **canonicity and uniformity**: the phase lives in a chosen complex plane rather than the center, the amplitude is a quaternion rather than a complex number, and the plane is an extra input. The Schrödinger article reaches the same verdict for the same reason, and this article inherits it rather than re-deriving it.

## The Propagator and Its Composition

For a free particle the sum over paths can be computed exactly, and the result makes the biquaternion content of the phase visible.

The free kernel is

$$
K_0(x_f,t_f;x_i,t_i)=\Big(\frac{m}{2\pi i\hbar T}\Big)^{1/2}
\exp\!\Big[\frac{i}{\hbar}\frac{m(x_f-x_i)^2}{2T}\Big],\qquad T=t_f-t_i,
$$

which is the stationary-phase result: the phase is the classical action $S_{\mathrm{cl}}=m(x_f-x_i)^2/(2T)$ divided by $\hbar$, and the prefactor is the Gaussian fluctuation determinant. In the biquaternion reading, both factors are central:

- the phase is $\exp(iS_{\mathrm{cl}}/\hbar)\in\mathbb{C}_{\mathbb{B}}$, its exponent in $\mathbb{M}_-$;
- the prefactor $(m/2\pi i\hbar T)^{1/2}$ is a function of the central $i$ and is therefore central as well.

The kernel is thus of the form stated above, $K_0=\mathcal{K}_0\,e_0$ with $\mathcal{K}_0\in\mathbb{C}$, and its squared modulus is the classical spreading density,
$$|K_0|^2=\frac{m}{2\pi\hbar T}.$$

**The measure factor.** The appearance of $\sqrt{i}$ in the prefactor is worth a remark. The square root of the central $i$ is central — it is $\pm e^{i\pi/4}$, one of the two roots of $i$ in the complex line — so the measure factor does not leave the center. It is two-valued, and the composition property below chooses its branch; the algebra itself does not. This is one instance of the general fact that the algebra supplies the phase and not the normalization.

**Composition.** The semigroup property of $K_0$ is a Gaussian (Fresnel) convolution. With $A=im/(2\hbar T_2)$, $B=im/(2\hbar T_1)$, the standard Fresnel integral

$$
\int dy\;e^{A(x-y)^2}e^{By^2}=\sqrt{\frac{-\pi}{A+B}}\;\exp\!\Big(\frac{AB}{A+B}x^2\Big)
$$

gives $A+B=\frac{im}{2\hbar}\frac{T_1+T_2}{T_1T_2}$ and $\frac{AB}{A+B}=\frac{im}{2\hbar(T_1+T_2)}$, so the convolution of $K_0(\cdot,T_2)$ with $K_0(\cdot,T_1)$ is exactly $K_0(\cdot,T_1+T_2)$, prefactor included. The phase that survives is the classical action of the longer free flight, and the branch of every square root is fixed by the requirement that the product reproduce the single kernel. The composition was checked numerically on a case chosen for the purpose: with $m=\hbar=1$, $T_1=0.6$, $T_2=0.9$, $x=1.1$, the convolution and the single kernel agree to a relative $1.8\times10^{-16}$.

**The single-step kernel and the Schrödinger equation.** Expanding $K_\varepsilon$ about $x$ and performing the Gaussian integral over the displacement returns the free Schrödinger equation $i\hbar\,\partial_t\psi=-\frac{\hbar^2}{2m}\partial_x^2\psi$, with the central $i$. The path integral therefore reproduces the state-vector equation of the Schrödinger article, and does not introduce a second imaginary unit: the $i$ of the exponent and the $i$ of the resulting equation are the same central element. The potential term enters through the factor $\exp(-i\varepsilon V/\hbar)$, again central.

The distance between this and a genuinely biquaternionic path integral should be stated plainly. The kernel above is a complex scalar times $e_0$; the paths are real-valued trajectories; and the algebra has entered only through the identification of the phase's imaginary unit and the location of its exponent. No element of $\mathbb{M}_+$ has been used to *define* the sum, and no non-central element appears at all.

## The Wick Rotation as the Bridge

The phase's exponent lies along the $ict$ direction of $\mathbb{M}_-$. The Wick rotation is precisely the operation that turns that direction real, and this is the sense in which it is the bridge between the oscillatory and the decaying forms of the path integral.

Perform the substitution $t\mapsto-i\tau$ in the action. With $dt=-i\,d\tau$ and $\dot x=dx/dt=i\,dx/d\tau$, the kinetic term becomes

$$
\tfrac12 m\dot x^2=\tfrac12 m\Big(i\frac{dx}{d\tau}\Big)^2=-\tfrac12 m\Big(\frac{dx}{d\tau}\Big)^2,
$$

so the Lagrangian becomes $L=-\tfrac12 m(dx/d\tau)^2-V$, and

$$
S=\int dt\,L=\int(-i\,d\tau)\Big[-\tfrac12 m\Big(\frac{dx}{d\tau}\Big)^2-V\Big]
=i\int d\tau\Big[\tfrac12 m\Big(\frac{dx}{d\tau}\Big)^2+V\Big]=i\,S_E,
$$

where $S_E$ is the Euclidean action. The phase therefore becomes

$$
e^{iS/\hbar}=e^{i(iS_E)/\hbar}=e^{-S_E/\hbar},
$$

a decaying real exponential. Checked numerically on a specific trajectory, the identity $e^{iS/\hbar}=e^{-S_E/\hbar}$ holds to machine precision.

In the reading of the Wick-rotation article, the substitution is the identification

$$
\mathbb{M}_-\;\longrightarrow\;\mathbb{H}_{\mathbb{B}},\qquad (ict,x,y,z)\longmapsto(c\tau,x,y,z),
$$

obtained by relabeling the imaginary time coefficient as a real one; it is real-linear, and it is not an isometry, since the quadratic form loses the sign reversal in the time direction. Applied to the path integral, the transfer does exactly one thing: it moves the phase exponent out of the imaginary-scalar direction of $\mathbb{M}_-$ and into the real-scalar direction of $\mathbb{H}_{\mathbb{B}}$. The unit circle of central phases $U(1)\subset\mathbb{C}_{\mathbb{B}}$ is replaced by the positive real axis of decaying weights. The oscillatory sum $\int\mathcal{D}x\,e^{iS/\hbar}$ becomes the positive sum $\int\mathcal{D}x_E\,e^{-S_E/\hbar}$, which is why the latter is the one that can be given a probabilistic (Wiener) reading.

This is where the Wick-rotation article's classification meets the path integral. Its thesis is that the transfer is harmless for problems about equilibrium and correlation and fatal for problems about causality and dynamics, because $\mathbb{H}_{\mathbb{B}}$ is better behaved precisely by having given up the Lorentzian structure. The path integral is the object in which both cases appear: its Euclidean form is the statistical weight of a Euclidean field theory or lattice model, and its Lorentzian form is the amplitude that encodes causal propagation. The transfer to $\mathbb{H}_{\mathbb{B}}$ is what turns amplitudes into weights; it is also what discards the phase relations that carry the causal ordering. And, as the Feynman-propagator article argues for the $i\epsilon$, the direction of the rotation is a choice equivalent to the sign of $\epsilon$: the algebra names the $ict$ axis along which the phase lives, and does not choose the orientation of the continuation.

## The Semiclassical Kernel and Stationary Phase

The classical limit of the sum over paths is obtained by stationary phase, and it is the second place where the algebra of the phase can be read. Expand the action about a classical path $x_{\mathrm{cl}}$ joining the endpoints,

$$
S[x_{\mathrm{cl}}+\delta x]=S_{\mathrm{cl}}+\tfrac12\,\delta^2S+O(\delta^3),
$$

where the linear term vanishes because $x_{\mathrm{cl}}$ is stationary. The leading contribution to the integral is the phase $e^{iS_{\mathrm{cl}}/\hbar}$ times the Gaussian integral over the fluctuations, giving the **van Vleck determinant** formula

$$
K(x_f,t_f;x_i,t_i)\;\approx\;\frac{1}{\sqrt{2\pi i\hbar}}\,
\sqrt{\Big|\det\frac{\partial^2 S_{\mathrm{cl}}}{\partial x_i\,\partial x_f}\Big|}\;
e^{iS_{\mathrm{cl}}/\hbar},
$$

with the Maslov index supplying a phase $e^{-i\pi\nu/2}$ at each conjugate point (caustic), where the determinant vanishes. The next correction comes from the cubic term in the expansion and is of order $\hbar$ relative to the leading term; it is the first term that feels the anharmonicity of the action, and it is not pursued here.

For the free particle $S_{\mathrm{cl}}=m(x_f-x_i)^2/2T$ and $\partial^2S_{\mathrm{cl}}/\partial x_i\partial x_f=-m/T$, so the prefactor is $(m/2\pi i\hbar T)^{1/2}$ and the semiclassical kernel is the exact kernel. Checked by recomputation: composing the semiclassical kernels for $t_1=0.6$ and $t_2=1.1$ reproduces $K(t_1+t_2)$ for the free particle to $8.3\times10^{-17}$, and the van Vleck prefactor matches $(m/2\pi i\hbar T)^{1/2}$ to $2.8\times10^{-17}$. A quadratic action is semiclassically exact; the free particle and the harmonic oscillator are the two elementary cases.

**The phase.** The stationary-phase phase $e^{iS_{\mathrm{cl}}/\hbar}$ is a **central unitary** element of $\mathbb{C}_{\mathbb{B}}$, for the same reason the phase of an individual path is: the classical action is still a real scalar, its exponent is still a purely imaginary scalar in $\mathbb{M}_-$, and the phase is still central. The classical limit changes which paths contribute; it does not change the sector of the phase.

**The prefactor.** The determinant is built from the second variation $\delta^2S$, a real symmetric quadratic form — an ordinary real object, not an element of the algebra. Written out,

$$
\frac{1}{\sqrt{2\pi i\hbar}}\sqrt{\big|\det\nolimits\delta^2S\big|}
=\frac{A_{\mathrm{WKB}}}{\sqrt{2\pi i\hbar}},
\qquad
A_{\mathrm{WKB}}=\sqrt{\big|\det\nolimits\delta^2S\big|},
$$

so the semiclassical prefactor is the **WKB amplitude** divided by the central $\sqrt{2\pi i\hbar}$. This is the amplitude that the companion article *The WKB Approximation and the Hamilton–Jacobi Equation in Biquaternionic Form* writes as the modulus of the wave function; the van Vleck determinant is its multidimensional transport, and the statement that it is the WKB amplitude is the content of that article's continuity equation. Checked for the free particle: $A_{\mathrm{WKB}}=\sqrt{m/T}=0.766965$, and $A_{\mathrm{WKB}}/\sqrt{2\pi i\hbar}$ reproduces the exact free prefactor to $2.8\times10^{-17}$.

Both factors are central — the phase is central, and the prefactor is a real number over the central $\sqrt{2\pi i\hbar}$ — so the semiclassical kernel is central:

$$
K\;\approx\;\mathcal{K}\,e_0,\qquad \mathcal{K}\in\mathbb{C},
$$

with no non-central element anywhere, exactly as for the full kernel. Under the Wick rotation of the previous section, $\sqrt{2\pi i\hbar}$ becomes $\sqrt{2\pi\hbar}$ and the prefactor becomes real and positive, while the unit-circle phase becomes the decaying weight.

**What this adds, and where the gap remains.** The algebra supplies the square root $\sqrt{i}$ inside the center, so the factor $1/\sqrt{2\pi i\hbar}$ — and with it the $\pm\pi/2$ phases of the Maslov index — is an operation performed on the central element rather than on a quantity whose imaginary unit has to be chosen. It also makes the reality of the prefactor structural. It does **not** supply the determinant: the second variation is the Hessian of an ordinary real action, and the fluctuations are real displacements in the material sector's configuration space. The fluctuation operator is therefore the same kind of external object as the measure, and the assessment of the next section applies to it unchanged.

## What the Algebra Adds and What It Does Not

**Standard quantum mechanics, transcribed.** The sum over paths, the composition law, the interference formula, the stationary-phase classical limit, the free and short-time kernels, the Gaussian fluctuation determinant, and the Euclidean reduction by Wick rotation are all standard. None of them is new, and none depends on the biquaternion structure beyond the identification of the phase's imaginary unit.

**What the biquaternion notation provides.**

- A **canonical complex structure**. The phase's $i$ is the central scalar imaginary, fixed by the algebra and not chosen; the phase is therefore a central unitary element of $\mathbb{C}_{\mathbb{B}}$, and the amplitude is a complex number. A quaternionic formulation without a complexifying factor would have to choose a complex structure, as Adler's does.
- A **location for the phase exponent**. The exponent $iS/\hbar$ lies in the material sector $\mathbb{M}_-$, along the same $ict$ direction as the propagator's $i\epsilon$ and the thermal analyticity strip — the same direction the Wick rotation turns real.
- A **name for the phase generator**. The generator $ie_0$ is the central element that exchanges the two sectors, $i\mathbb{M}_\pm=\mathbb{M}_\mp$.
- A **bridge**. The Wick rotation is exhibited as the transfer $\mathbb{M}_-\to\mathbb{H}_{\mathbb{B}}$, which is exactly the operation that converts the oscillatory phase into a decaying weight.
- A **central square root**. The semiclassical prefactor contains $\sqrt{2\pi i\hbar}$; the square root is taken inside the center, so the $\pm\tfrac{\pi}{2}$ phases of the Maslov index are operations on the central $i$ rather than on a quantity whose imaginary unit must first be chosen, and the reality of the prefactor after the Wick rotation is structural.

**What remains open in the framework.**

- **The measure.** The path-integral measure $\mathcal{D}x$ is not supplied by the algebra. The trajectories live in the material sector's configuration space, and the algebra labels points of that sector, but the measure on the space of paths is an analytic construction. The free-kernel normalization is fixed by the composition property, not read off the algebra.
- **The fluctuation operator.** The determinant of the semiclassical kernel is the Hessian of a real action, $\delta^2S$, and the fluctuations are real displacements in the material sector's configuration space. Like the measure, it is an analytic object external to the algebra: the algebra supplies the central $i$ under its square root, not the determinant itself.
- **The space of paths.** This is the sharpest gap. The biquaternion algebra is finite-dimensional ($\mathbb{B}\cong M_2(\mathbb{C})$ as a $\mathbb{C}$-algebra), whereas the space of paths is infinite-dimensional. As the harmonic-oscillator article records for the infinite ladder, $\mathbb{B}$ hosts the two-level truncation and does not contain an infinite-dimensional module. The sum over paths is therefore performed on a function space *outside* $\mathbb{B}$; the algebra acts fiberwise on the values of the field and supplies the phase, but it does not contain the integration domain.
- **A biquaternion-valued action.** If the action were $\mathbb{B}$-valued rather than a real scalar — for instance if a Hermitian Lagrangian density were integrated to an $\mathbb{M}_+$-valued action — then the exponent $iS/\hbar$ would lie in $\mathbb{M}_-$ without being central, and the phase $e^{iS/\hbar}$ would be a general unitary biquaternion rather than a central one. Whether such a theory is admissible in the framework, and what a matrix-valued phase would mean, is not addressed here.

## Open Questions

**1. Is there a biquaternionic measure?** The framework provides the fibers of a field (elements of $\mathbb{B}$ or its modules) and the phase, but not a measure on the space of sections. Whether the algebra admits a distinguished measure — for instance on the zero-divisor cone or the light cone of $\mathbb{M}_-$ — is open.

**2. Spin in the path integral.** The state module is $\mathbb{C}^2$, but the free kernel above is spin-independent: being central, it multiplies both components equally. A path integral that couples to spin would need non-central phases along the path, which would make the phase a spin rotation (a holonomy) rather than a global phase. Whether the framework produces such a coupling from first principles is not known.

**3. The local complex structure.** The series makes the complex structure local, set by the medium through $c=1/\sqrt{\epsilon\mu}$. The scalar imaginary $i$, which the phase uses, is a global central element and cannot vary from point to point. How a local complex structure would enter the phase's exponent is unresolved, and the same question is left open by the Schrödinger article.

**4. The relation to the field-theoretic path integral.** The momentum-space propagator of the companion article is the two-point function of the quantized field; the kernel here is the configuration-space transition amplitude. The passage between them — and the intrinsic $\mathbb{B}$-valued path integral, if one exists — inherits the open status of the companion articles.

**5. Real-time dynamics.** The path integral is where the sign problem lives: the Euclidean form is computable and the Lorentzian form carries the phase that obstructs simulation. The biquaternion reading does not remove this obstruction; it only names the direction (the $ict$ axis of $\mathbb{M}_-$) along which the phase accumulates. Whether that naming has any computational content is open.

**6. Empirical content.** As elsewhere in the framework, whether the present reformulation yields any prediction distinguishing it from standard quantum mechanics is open. Nothing in this article changes that.

## Summary

The path integral $K=\int\mathcal{D}x\,e^{iS[x]/\hbar}$ is a sum over paths weighted by the phase $e^{iS/\hbar}$. In the biquaternion framework the symbol $i$ in that phase is the **central scalar imaginary**, the unique central root of $-1$ in $\mathbb{B}$ up to sign; the phase exponent $iS/\hbar$ is a purely imaginary scalar and therefore lies in the **material sector** $\mathbb{M}_-$, along the $ict$ direction; and the phase factor $e^{iS/\hbar}$ is a **central unitary** element of $\mathbb{C}_{\mathbb{B}}$, satisfying $(e^{iS/\hbar})(e^{iS/\hbar})^\dagger=e_0$ but not the unit-norm-form condition of the Lorentz group, since $e^{iS/\hbar}\overline{e^{iS/\hbar}}=e^{2iS/\hbar}$.

Centrality has three consequences: the amplitude is a complex scalar times $e_0$; the phase multiplies every spinor component of the state module equally; and the global phase cancels in the density matrix $\tilde{\rho}=\psi\psi^\dagger$, so only relative phases — the differences of actions between paths — are observable. These relative phases produce the standard interference, $|e^{iS_1/\hbar}+e^{iS_2/\hbar}|=2|\cos(\Delta S/2\hbar)|$, with nodes at $\Delta S=(2n+1)\pi\hbar$.

A non-central root $J$ fails as the phase's imaginary unit for the same reasons it fails in the Schrödinger equation: the generator $-J\tilde{H}/\hbar$ need not be anti-Hermitian (for $J=e_3$, $\tilde{H}=ie_1$ one has $J\tilde{H}=ie_2$, Hermitian), and even a fixed unitary $J$ gives the two spin components opposite phases, $\exp(e_3\theta)\mapsto\operatorname{diag}(e^{-i\theta},e^{+i\theta})$, so it is a spin rotation rather than a global phase. A fixed non-central root still interferes, but it requires choosing a preferred spin axis, which the algebra does not supply.

The free kernel $K_0=(m/2\pi i\hbar T)^{1/2}\exp(im\Delta x^2/2\hbar T)$ is central, its phase the classical action over $\hbar$ and its prefactor a function of the central $i$; its composition law was verified to machine precision. The Wick rotation $t\mapsto-i\tau$ gives $S=iS_E$ and hence $e^{iS/\hbar}=e^{-S_E/\hbar}$; in the reading of the companion article this is the identification $\mathbb{M}_-\to\mathbb{H}_{\mathbb{B}}$, which turns the unit circle of central phases into the positive real axis of decaying weights. The algebra thus supplies the phase, its sector, and the bridge to the Euclidean form; it does not supply the measure, the action, or the space of paths — the last being a gap it cannot close, because $\mathbb{B}$ is finite-dimensional.

The classical limit by stationary phase is the van Vleck kernel, $K\approx(2\pi i\hbar)^{-1/2}\big|\det\partial^2S_{\mathrm{cl}}/\partial x_i\partial x_f\big|^{1/2}e^{iS_{\mathrm{cl}}/\hbar}$. Its phase is the same central unitary element as before, and its prefactor is the WKB amplitude $A_{\mathrm{WKB}}=\sqrt{|\det\delta^2S|}$ divided by the central $\sqrt{2\pi i\hbar}$, so the semiclassical kernel is central as well. For the free particle it is the exact kernel, with the composition law and the prefactor verified to $8.3\times10^{-17}$ and $2.8\times10^{-17}$ respectively. The algebra supplies the square root of the central $i$ — and with it the Maslov phases — and makes the reality of the prefactor after the Wick rotation structural; the determinant, being the Hessian of an ordinary real action, is not supplied.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Scalar imaginary, central, $i^2=-e_0$ |
| $\mathbb{C}_{\mathbb{B}}=\operatorname{span}_\mathbb{R}\{e_0,ie_0\}$ | Center of $\mathbb{B}$; home of the path-integral phase |
| $\mathbb{M}_-$ | Anti-Hermitian (material) sector; home of the phase exponent $iS/\hbar$ |
| $\mathbb{M}_+$ | Hermitian (informational) sector; home of the state $\tilde\rho=\psi\psi^\dagger$ |
| $\mathbb{H}_{\mathbb{B}}$ | Quaternion subspace; image of the Wick rotation |
| $K(x_f,t_f;x_i,t_i)$ | Transition amplitude (propagator), central: $K=\mathcal{K}e_0$ |
| $S[x]=\int L\,dt$ | Action; real scalar |
| $e^{iS/\hbar}$ | Path phase; central unitary element of $\mathbb{C}_{\mathbb{B}}$ |
| $ie_0$ | Generator of the phase; exchanges the sectors, $i\mathbb{M}_\pm=\mathbb{M}_\mp$ |
| $K_\varepsilon(x',x)$ | Single-step kernel; phase $=\frac{i}{\hbar}\big(\frac{m(x'-x)^2}{2\varepsilon}-\varepsilon V\big)$ |
| $K_0$ | Free kernel; $K_0=\mathcal{K}_0e_0$, $\lvert\mathcal{K}_0\rvert^2=m/2\pi\hbar T$ |
| $S_{\mathrm{cl}}$ | Classical action; stationary point of $S[x]$; phase of the free kernel |
| $\delta^2S$ | Second variation (Hessian) of the action about $x_{\mathrm{cl}}$ |
| $\sqrt{\lvert\det\partial^2S_{\mathrm{cl}}/\partial x_i\partial x_f\rvert}$ | Van Vleck determinant; equals the WKB amplitude $A_{\mathrm{WKB}}$ |
| $e^{-i\pi\nu/2}$ | Maslov phase; $\nu$ the number of conjugate points (caustics) |
| $\tilde\rho=\psi\psi^\dagger/\mathrm{Tr}(\psi^\dagger\psi)$ | State from a spinor; global phase cancels |
| $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace formula (Born rule) |
| $t\mapsto-i\tau$ | Wick rotation |
| $S=iS_E$ | Action under the Wick rotation |
| $e^{iS/\hbar}=e^{-S_E/\hbar}$ | Oscillatory phase becomes decaying weight |
| $\mathbb{M}_-\to\mathbb{H}_{\mathbb{B}}$ | Wick rotation as identification of subspaces |

## Further Reading

- P. A. M. Dirac, "The Lagrangian in Quantum Mechanics," *Physikalische Zeitschrift der Sowjetunion* **3** (1933) 64–72, for the origin of the path-integral formulation.
- R. P. Feynman, "Space-Time Approach to Non-Relativistic Quantum Mechanics," *Reviews of Modern Physics* **20** (1948) 367–387, for the original construction.
- R. P. Feynman and A. R. Hibbs, *Quantum Mechanics and Path Integrals* (McGraw-Hill, 1965), for the standard treatment of the kernel, its composition, and the free-particle case.
- L. S. Schulman, *Techniques and Applications of Path Integration* (Wiley, 1981), for the measure, the semiclassical expansion, and the convergence of the oscillatory integral.
- J. H. Van Vleck, "The Correspondence Principle in the Statistical Interpretation of Quantum Mechanics," *Proceedings of the National Academy of Sciences* **14** (1928) 178–188, for the fluctuation determinant that carries the semiclassical amplitude.
- V. P. Maslov and M. V. Fedoriuk, *Semi-Classical Approximation in Quantum Mechanics* (Reidel, 1981), for the rigorous stationary-phase expansion and the Maslov index at caustics.
- J. Glimm and A. Jaffe, *Quantum Physics: A Functional Integral Point of View* (Springer, 1987), for the Euclidean (Wick-rotated) path integral and its rigorous formulation.
- H. Kleinert, *Path Integrals in Quantum Mechanics, Statistics, Polymer Physics, and Financial Markets* (World Scientific, 2009), for the Euclidean and real-time integrals side by side.
- S. L. Adler, *Quaternionic Quantum Mechanics and Quantum Fields* (Oxford, 1995), for the quaternionic formulation in which a complex structure must be chosen.
- G. C. Wick, "Properties of Bethe-Salpeter Wave Functions," *Physical Review* **96** (1954) 1124–1134, for the Wick rotation and its analytic continuation.
- *The WKB Approximation and the Hamilton–Jacobi Equation in Biquaternionic Form* (`articles_physics/the-wkb-approximation-and-the-hamilton-jacobi-equation-in-biquaternionic-form.md`), for the WKB amplitude, its transport by the continuity equation, and the quantum potential.
