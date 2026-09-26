# __The Yang–Mills Path Integral and the Faddeev–Popov Procedure in Biquaternionic Form__

## Introduction

The companion article *The Gauge Field Path Integral in Biquaternionic Form* specialises the functional integral to a gauge field and develops the Faddeev–Popov procedure for the **abelian** case: the gauge orbit, the compensating determinant, and the Gaussian evaluation that yields the propagator. It records the non-abelian determinant only as a structure, $\Delta=\det(\partial_\mu D^\mu)$ up to the overall sign of a determinant, and leaves its development to the present subcategory. This is that development. The companion article *The Yang–Mills Equation in Biquaternionic Form* writes the classical non-abelian field equation $D_\mu F^{\mu\nu}=J^\nu$ and its covariant conservation $D_\nu J^\nu=0$; the present article places that equation inside the path integral and asks what survives of it as an operator statement.

Three features distinguish the non-abelian procedure from the abelian one, and they organise everything below.

- **The determinant is a functional of the connection.** In the abelian theory the Faddeev–Popov determinant is the field-independent constant $\det\Box^{-1}$, and the ghosts it would introduce decouple. In the non-abelian theory the determinant depends on $\mathcal A$ through the commutator term of the covariant derivative, and it must be represented by anticommuting fields. The ghosts are therefore not an optional device; they are the determinant written as a functional integral.
- **The quantum equation of motion is an expectation value.** The classical equation $D_\mu F^{\mu\nu}=J^\nu$ becomes the Schwinger–Dyson statement $\langle D_\mu F^{\mu\nu}\rangle=\langle J^\nu\rangle$, with contact terms at coincident points, and its gauge-invariance content is carried by the Slavnov–Taylor identities rather than by an operator equation.
- **The gauge slice is not global.** The Faddeev–Popov construction inserts unity only if the gauge condition selects one representative on each orbit. For the non-abelian theory on a non-trivial bundle it does not, and the copies — the Gribov ambiguity — are supplementary data of the non-abelian case, absent in the abelian one.

The algebra contributes at three points, and they are the reason the construction is not merely a transcription. The gauge algebra is realized by the quaternion commutator inside the material sector, so the structure constants $f^{abc}$ are read off from $\varepsilon_{abc}$ and the Jacobi identity that closes the Slavnov–Taylor and BRST algebras is a consequence of the associativity of $\mathbb{B}$. The Faddeev–Popov operator is a material-sector differential operator twisted by the informational adjoint action — the same adjoint action that *Integer-Spin Quantization and the Adjoint Action on the Material Sector in Biquaternionic Form* identifies as the spin-one representation — so the operator that the ghosts invert is, on its internal indices, a spin-one object. And the ghosts themselves lie outside $\mathbb{B}$: the algebra is ungraded, every element of it is even, and no product of two elements of $\mathbb{B}$ is odd, so the determinant lives in the Grassmann envelope $\mathbb{B}\otimes\Lambda$, exactly as the fermionic Gaussian integral requires.

We use the conventions of the companion articles throughout. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, $e_je_k=-\delta_{jk}e_0+\varepsilon_{jkl}e_l$, and central scalar imaginary $i$. The material and informational sectors are
$$
\mathbb{M}_-=\mathrm{span}_\mathbb{R}\{ie_0,e_1,e_2,e_3\},
\qquad
\mathbb{M}_+=\mathrm{span}_\mathbb{R}\{e_0,ie_1,ie_2,ie_3\},
\qquad
\mathbb{B}=\mathbb{M}_-\oplus\mathbb{M}_+ ,
$$
and the center is $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_\mathbb{R}\{e_0,ie_0\}$. The gradient is $\tilde{\nabla}=e_0\partial_{ict}+e_1\partial_x+e_2\partial_y+e_3\partial_z$, with conjugate $\bar{\tilde{\nabla}}$ and $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}=\partial_{ict}^2+\Delta$; the $ict$ metric is $\eta=\mathrm{diag}(-1,+1,+1,+1)$. The non-abelian sector is built on the compact factor
$$
\mathfrak{su}(2)=\mathrm{span}_\mathbb{R}\{e_1,e_2,e_3\}\subset\mathbb{M}_- ,
\qquad
[e_a,e_b]=2\varepsilon_{abc}e_c ,
\qquad
T_a=\tfrac12 e_a ,\ \ [T_a,T_b]=\varepsilon_{abc}T_c ,\ \ \mathrm{Tr}(T_aT_b)=-\tfrac12\delta_{ab},
$$
with the connection $\mathcal{A}_\mu=\mathcal{A}_\mu^a e_a\in\mathfrak{su}(2)$, the coupling $\kappa=q/\hbar$, the covariant derivative $D_\mu=\partial_\mu+i\kappa\mathcal{A}_\mu$, the curvature $F_{\mu\nu}=\partial_\mu\mathcal{A}_\nu-\partial_\nu\mathcal{A}_\mu+i\kappa[\mathcal{A}_\mu,\mathcal{A}_\nu]$, its adjoint law $F'_{\mu\nu}=UF_{\mu\nu}U^{-1}$ for a unit real quaternion $U$, and the adjoint covariant derivative $D_\lambda X=\partial_\lambda X+i\kappa[\mathcal{A}_\lambda,X]$. The connection components are taken in the unnormalized basis $e_a$, in which the structure constants are $f^{abc}=2\varepsilon^{abc}$; in the normalized basis $T_a=\tfrac12 e_a$ the same algebra reads $[T_a,T_b]=\varepsilon_{abc}T_c$, with $f^{abc}=\varepsilon^{abc}$, and in the Hermitian-generator realization $T^a=ie_a\in\mathbb{M}_+$ of the BRST companion it reads $[T^a,T^b]=2i\varepsilon^{abc}T^c=if^{abc}T^c$. The two realizations are related by the central $i$, which exchanges the sectors, and the same structure constants $f^{abc}$ serve both. The matrix trace on the $\mathfrak{su}(2)$ factor is written $\mathrm{Tr}$ and is distinct from the informational trace formula $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$. Natural units $\hbar=c=1$ are used for the integral where no dimensionful quantity is displayed.

- Companion article *The Gauge Field Path Integral in Biquaternionic Form*, for the abelian Faddeev–Popov construction, the gauge-fixing parameter and the propagator.
- Companion article *The Yang–Mills Equation in Biquaternionic Form*, for the non-abelian curvature, the field equation and covariant conservation.
- Companion article *Non-Abelian Gauge Fields in Biquaternionic Form*, for the connection, the adjoint transformation law and the Yang–Mills density.
- Companion article *BRST Symmetry in Biquaternionic Form*, for the nilpotent odd derivation, the gauge-fixing fermion and the cohomological description of physical states.
- Companion article *Gauge Curvature and the Bianchi Identity in Biquaternionic Form*, for the curvature conventions and the Bianchi identity.
- Companion article *Integer-Spin Quantization and the Adjoint Action on the Material Sector in Biquaternionic Form*, for the adjoint action as the spin-one representation.
- Companion article *The Functional Integral in Biquaternionic Form*, for the measure, the Gaussian evaluation and the Euclidean rotation.
- Companion article *The Renormalization Group in Biquaternionic Form*, for the running of the non-abelian coupling.

## The Non-Abelian Action and Its Gauge Orbit

### The Action and the Invariance

The Yang–Mills action of the framework is the gauge-invariant density of the companion articles,
$$
S_{\mathrm{YM}}[\mathcal{A}]=\int d^4x\left(-\tfrac12\mathrm{Tr}\left(F_{\mu\nu}F^{\mu\nu}\right)\right),
\qquad
F_{\mu\nu}=\partial_\mu\mathcal{A}_\nu-\partial_\nu\mathcal{A}_\mu+i\kappa[\mathcal{A}_\mu,\mathcal{A}_\nu] .
$$
The trace is the matrix trace on the $\mathfrak{su}(2)$ factor, taken in the defining two-dimensional representation; the combination is invariant because $F'_{\mu\nu}=UF_{\mu\nu}U^{-1}$ and the trace is cyclic. Under a local gauge transformation $U(\tilde{X})$, the connection shifts by an inhomogeneous term,
$$
\mathcal{A}'_\mu=U\mathcal{A}_\mu U^{-1}+\frac{i}{\kappa}(\partial_\mu U)U^{-1},
$$
and the action is unchanged, $S_{\mathrm{YM}}[\mathcal{A}^U]=S_{\mathrm{YM}}[\mathcal{A}]$. The same holds for the full Yang–Mills action including a matter sector, provided the matter fields transform in the representation the covariant derivative presupposes.

### The Orbit and the Infinite Factor

The integration variable is an $\mathfrak{su}(2)$-valued one-form, and the measure is the product over its components,
$$
\mathcal{D}\mathcal{A}=\prod_{\mu=0}^{3}\prod_{a=1}^{3}\mathcal{D}\mathcal{A}_\mu^a ,
$$
written in components because $\mathfrak{su}(2)$ is real three-dimensional. The gauge transformation is a shift of the connection by $\frac{i}{\kappa}(D_\mu U)U^{-1}$ with $(D_\mu U)=\partial_\mu U+i\kappa[\mathcal{A}_\mu,U]$ the covariant derivative of the group-valued function; the orbit through $\mathcal{A}$ is the set of all $\mathcal{A}^U$. The integrand $e^{iS_{\mathrm{YM}}}$ is constant on the orbit, and the measure is invariant under the shift, so the integral factorizes as in the abelian case,
$$
Z=\int\mathcal{D}\mathcal{A}\,e^{iS_{\mathrm{YM}}[\mathcal{A}]}
=\mathrm{Vol}(\mathcal{G})\int_{\text{orbits}}\mathcal{D}\mathcal{A}_{\text{rep}}\,e^{iS_{\mathrm{YM}}[\mathcal{A}]},
$$
with $\mathrm{Vol}(\mathcal{G})$ the infinite volume of the group of gauge transformations. The factor is an artifact of the parameterization and must be removed; the Faddeev–Popov construction removes it, and in the non-abelian case it does so at the cost of the determinant and the ghosts.

## Gauge Fixing and the Faddeev–Popov Determinant

### Inserting Unity

Let $G^a[\mathcal{A}]=0$ be a gauge-fixing condition, one equation for each generator, and let $\mathcal{A}^U$ denote the gauge transform of $\mathcal{A}$ by $U$. The Faddeev–Popov identity is
$$
1=\Delta[\mathcal{A}]\int\mathcal{D}U\;\delta\!\left(G[\mathcal{A}^U]\right),
$$
which defines the determinant $\Delta[\mathcal{A}]$: it is the inverse of the volume, in the space of gauge transformations, of the set that satisfies the condition, and it therefore compensates the infinite factor. The determinant is gauge invariant,
$$
\Delta[\mathcal{A}^U]=\Delta[\mathcal{A}],
$$
because the composition of two gauge transformations is a gauge transformation. Shifting the integration variable at fixed $U$ and using the invariance of the measure, of the action and of $\Delta$, the identity turns the integral into
$$
Z=\int\mathcal{D}\mathcal{A}\;\Delta[\mathcal{A}]\,\delta\!\left(G[\mathcal{A}]\right)e^{iS_{\mathrm{YM}}[\mathcal{A}]},
$$
in which the orbit is represented once and the volume factor is gone. The construction is the same as the abelian one in the companion article; what changes is the value of $\Delta$.

### The Determinant of the Non-Abelian Theory

Near a configuration that satisfies $G=0$, the variation of the gauge-fixing functional under an infinitesimal gauge transformation with parameter $\Gamma^a$ is
$$
\delta G^a[\mathcal{A}]=M^{ab}\Gamma^b ,
\qquad
M^{ab}=\frac{\delta G^a}{\delta\Gamma^b},
$$
and the determinant is $\Delta[\mathcal{A}]=\det M$. For the **Lorenz gauge** $G^a=\partial_\mu\mathcal{A}^{a\mu}-\omega^a$, the variation is
$$
\mathcal{A}^{a}_\mu\longmapsto\mathcal{A}^{a}_\mu-(D_\mu\Gamma)^a ,
\qquad
(D_\mu\Gamma)^a=\partial_\mu\Gamma^a+i\kappa f^{abc}\mathcal{A}_\mu^b\Gamma^c ,
$$
so that
$$
M^{ab}=-\partial_\mu D^{\mu\,ab}
=-\Box\,\delta^{ab}+i\kappa f^{abc}\partial_\mu\mathcal{A}^{c\mu}+\cdots ,
$$
with $D_\mu{}^{ab}=\partial_\mu\delta^{ab}-i\kappa f^{abc}\mathcal{A}_\mu^c$ the covariant derivative in the adjoint representation and $f^{abc}$ the structure constants. The identity $D_\mu{}^{ab}=\partial_\mu\delta^{ab}-i\kappa f^{abc}\mathcal{A}_\mu^c$ is fixed by the requirement that it reproduce $(D_\mu X)^a=\partial_\mu X^a+i\kappa[\mathcal{A}_\mu,X]^a$ on an algebra-valued field; it was verified on a generic superposition of the three generators, and the structure constants it uses are read off from the quaternion commutator,
$$
[e_a,e_b]=2\varepsilon_{abc}e_c
\qquad\Longrightarrow\qquad
f^{abc}=2\varepsilon^{abc},
$$
which was verified on the defining representation, $[T_a,T_b]=\varepsilon_{abc}T_c$ with $T_a=\tfrac12 e_a$.

The determinant is field-dependent. In the abelian limit the connection is central, the commutator vanishes, $f^{abc}=0$, and $M=-\Box$ is the field-independent operator of the companion article; in the non-abelian theory the term $i\kappa f^{abc}\partial_\mu\mathcal{A}^{c\mu}$ is present, and $\Delta[\mathcal{A}]$ is a functional of the connection. The overall sign of $M$ is fixed by the direction of the infinitesimal transformation, $M^{ab}=\delta G^a/\delta\Gamma^b$, and a change of that sign multiplies $\Delta$ by a constant and leaves $Z$ unchanged; the companion article's $\det(\partial_\mu D^\mu)$ is this same determinant with the opposite overall sign, not a different operator.

### The Jacobi Identity and Associativity

The algebra that the determinant's locality and the Ward–Slavnov–Taylor identities require is the Jacobi identity of the structure constants,
$$
f^{abe}f^{cde}+f^{bce}f^{ade}+f^{cae}f^{bde}=0 .
$$
In the framework this identity is not an independent axiom. The structure constants are the coefficients of the commutator, the commutator is the antisymmetrization of the associative product of $\mathbb{B}$, and the Jacobi identity is the associativity of that product written in bracket form. The companion article *BRST Symmetry in Biquaternionic Form* isolates this fact for the nilpotency $s^2=0$; the same identity is what makes the Slavnov–Taylor algebra close below.

## The Ghost Fields and the Grassmann Envelope

### The Fermionic Gaussian Integral

The determinant that the gauge-fixing identity produces can be written as a functional integral over anticommuting fields, by the finite-dimensional identity
$$
\det M=\int\prod_a d\bar c_a\,dc_a\;e^{-\bar c_a M^{ab}c_b},
$$
with $c_a,\bar c_a$ odd, $c_ac_b=-c_bc_a$, and the Gaussian integral evaluated by the same pairing that the bosonic integral uses. This is the standard device that converts a determinant into a local action, and it is the origin of the Faddeev–Popov ghosts. Applied to $\Delta[\mathcal{A}]=\det(-\partial_\mu D^{\mu\,ab})$, it gives
$$
\Delta[\mathcal{A}]=\int\mathcal{D}c\,\mathcal{D}\bar c\;\exp\!\left(i\int d^4x\,\bar c_a\,M^{ab}c_b\right)
=\int\mathcal{D}c\,\mathcal{D}\bar c\;\exp\!\left(iS_{\mathrm{gh}}\right),
$$
$$
S_{\mathrm{gh}}=-\int d^4x\;\bar c_a\,\partial_\mu(D^\mu c)^a ,
\qquad
(D^\mu c)^a=\partial^\mu c^a+i\kappa f^{abc}\mathcal{A}^{b\mu}c^c .
$$
The ghost $c^a$ and the antighost $\bar c_a$ are Lorentz scalars of opposite ghost number; the antighost is the conjugate field, and the action is the standard one. Its form is exactly the ghost term that *BRST Symmetry in Biquaternionic Form* takes as given; here it has been derived from the measure.

### Where the Ghosts Live

The ghosts are anticommuting, and $\mathbb{B}$ contains no such element: it is not a division algebra — $\mathbb{B}\cong M_2(\mathbb{C})$ contains nonzero nilpotents, among them $(e_1+ie_2)/2$, whose square vanishes — but nilpotency is not oddness, and the algebra is ungraded, so every element of $\mathbb{B}$ is even and no element anticommutes with its fellows. The ghosts therefore cannot be elements of $\mathbb{B}$. They are elements of the Grassmann envelope
$$
\mathbb{B}\otimes\Lambda,
\qquad
\Lambda=\Lambda^0\oplus\Lambda^1,
$$
with $\Lambda^1$ generated by anticommuting $\theta_i$, and a ghost is written $c=c^aT^a\otimes\theta$. The algebra supplies the generators $T^a$, the structure constants and the module; the odd coordinates are adjoined. This is the same statement the Fock companion makes for the ladder operators and the BRST companion makes for the doublet: the framework's algebra is even, and the odd sector is tensored on.

### The Gauge-Fixed Action

Collecting the pieces, the gauge-fixed Yang–Mills action is
$$
S=S_{\mathrm{YM}}+S_{\mathrm{gf}}+S_{\mathrm{gh}},
\qquad
S_{\mathrm{gf}}=-\frac{1}{2\xi}\int d^4x\,\left(\partial_\mu\mathcal{A}^{a\mu}\right)^2 ,
$$
where $\xi$ is the gauge parameter. The gauge-fixing term is the elimination of the Nakanishi–Lautrup field $B^a$ of the BRST companion, whose equation of motion is $B^a=-\xi^{-1}\partial_\mu\mathcal{A}^{a\mu}$; the three terms together are no longer gauge invariant but are invariant under the nilpotent odd derivation $s$, a statement developed in the BRST companion and not repeated here. The partition function that the ghosts define,
$$
Z=\int\mathcal{D}\mathcal{A}\,\mathcal{D}c\,\mathcal{D}\bar c\;e^{iS},
$$
is the Yang–Mills path integral of the framework.

## The Propagator and Gauge-Parameter Independence

### The Quadratic Form

At quadratic order in the fields the gauge-fixed action is
$$
S^{(2)}=\tfrac12\int d^4x\;\mathcal{A}^{a\mu}\left(\eta_{\mu\nu}\Box-(1-\tfrac1\xi)\partial_\mu\partial_\nu\right)\mathcal{A}^{a\nu},
$$
whose inversion gives the gauge-field propagator, in momentum space,
$$
D_{\mu\nu}(p)=\frac{1}{p^2}\left(\eta_{\mu\nu}+\frac{p_\mu p_\nu}{p^2}\right)-\frac{\xi}{p^2}\frac{p_\mu p_\nu}{p^2}
=\frac{1}{p^2}\left(\eta_{\mu\nu}+(1-\xi)\frac{p_\mu p_\nu}{p^2}\right).
$$
The projector algebra is that of the companion article, and the series convention $p_\mu p^\mu=-p^2$ fixes its signs: writing $P_{\mu\nu}=\eta_{\mu\nu}+p_\mu p_\nu/p^2=\eta_{\mu\nu}-p_\mu p_\nu/(p_\mu p^\mu)$ and $L_{\mu\nu}=-p_\mu p_\nu/p^2=p_\mu p_\nu/(p_\mu p^\mu)$, one has $P^2=P$, $L^2=L$, $PL=LP=0$, $P+L=\eta$, $\mathrm{tr}\,P=3$, $\mathrm{tr}\,L=1$, and $p^\mu P_{\mu\nu}=0$. Here $p^2$ is the momentum-space eigenvalue of the central $\Box$ in the series convention, so that the invariant $p_\mu p^\mu$ equals $-p^2$ and the transverse projector is $\eta_{\mu\nu}+p_\mu p_\nu/p^2$. The signs of $P$ and $L$ are tied to the momentum convention, and it is the invariant $p_\mu p^\mu=-p^2$, not the variable $p^2$, that fixes them: replacing the invariant by $p^2$ in the projector gives a matrix that is neither transverse nor idempotent. This is the same invariant object the Proca companion writes as the completeness relation $\eta_{\mu\nu}+p_\mu p_\nu/\mu^2$ on shell, and it is the form the gauge-field path-integral companion uses: with $D=p^{-2}(P+\xi L)$ the two agree term by term. The gauge parameter multiplies the longitudinal projector alone, and for a conserved external current, $p_\nu j^\nu=0$, the difference between two propagators with different $\xi$ annihilates the current,
$$
\big(D(\xi)-D(\xi')\big)_{\mu\nu}j^\nu=0 ,
$$
so that physical amplitudes are gauge-parameter independent. This is the content the companion article verifies in the abelian theory; it is unchanged in the non-abelian theory, because the statement is about the quadratic form and the conservation of the external current.

### What the Non-Abelian Theory Adds

Two additions are specific to the non-abelian case. The first is that the external current of the gauge field is itself charged, $J'_\nu=UJ_\nu U^{-1}$, and is covariantly conserved, $D_\nu J^\nu=0$, so the identity $p_\nu j^\nu=0$ holds only after the commutator terms are included: ordinary conservation fails, $\partial_\nu J^\nu=-i\kappa[\mathcal{A}_\nu,J^\nu]$, as the Yang–Mills companion records. The Ward identity of the abelian theory therefore becomes a family of **Slavnov–Taylor identities**, one for each external leg, relating amplitudes with different numbers of ghosts and longitudinal gauge fields. The second addition is that the propagator is not the whole of the quadratic theory: the gauge-fixed action contains the cubic and quartic self-interactions of $\mathcal{A}$, and the ghost action contains the ghost–gauge coupling $i\kappa f^{abc}\bar c_a\partial_\mu(\mathcal{A}^{b\mu}c^c)$. The one-loop two-point function therefore receives, in addition to the gauge-field loop, the ghost loop and the gauge-field tadpole; their contributions are what make the non-abelian beta function differ from the abelian one. For the pure $\mathfrak{su}(2)$ theory the one-loop coefficient is
$$
\beta_\kappa=-\frac{\kappa^3}{16\pi^2}b_0 ,
\qquad
b_0=\frac{11}{3}C_2(G)=\frac{11}{3}\cdot 2=\frac{22}{3},
$$
with $C_2(G)=N=2$ the adjoint quadratic Casimir of $SU(2)$; the coefficient is positive, so the coupling is asymptotically free. This is the standard one-loop result, read in the framework's normalization; the companion article *The Renormalization Group in Biquaternionic Form* records it and the two-loop extension.

## The Quantum Yang–Mills Equation

The classical equation of the companion article is $D_\mu F^{\mu\nu}=J^\nu$, with $D_\nu J^\nu=0$. Inside the path integral it becomes an expectation value, and the derivation is the Schwinger–Dyson argument. For any functional $\mathcal{O}[\mathcal{A}]$ of the connection,
$$
0=\int\mathcal{D}\mathcal{A}\,\frac{\delta}{\delta\mathcal{A}_\mu^a(x)}\Big(\mathcal{O}[\mathcal{A}]\,e^{iS}\Big),
$$
because the integral of a total derivative in field space vanishes. Performing the derivative,
$$
\left\langle\frac{\delta\mathcal{O}}{\delta\mathcal{A}_\mu^a(x)}\right\rangle
+i\left\langle\mathcal{O}\,\frac{\delta S}{\delta\mathcal{A}_\mu^a(x)}\right\rangle=0 .
$$
Taking $\mathcal{O}=1$ gives the **quantum equation of motion**,
$$
\left\langle\frac{\delta S}{\delta\mathcal{A}_\mu^a(x)}\right\rangle=0 ,
$$
and taking $\mathcal{O}$ to be a product of fields gives the hierarchy of contact terms that the equation of motion generates at coincident points. The variation of the Yang–Mills action is the covariant divergence of the field strength,
$$
\frac{\delta S_{\mathrm{YM}}}{\delta\mathcal{A}_\mu^a(x)}=\big(D_\nu F^{\nu\mu}\big)^a(x),
$$
so that, separating the source terms that the gauge-fixing and ghost actions contribute,
$$
\left\langle\big(D_\mu F^{\mu\nu}\big)^a\right\rangle
=\left\langle J^{\nu a}_{\mathrm{gf}}\right\rangle+\left\langle J^{\nu a}_{\mathrm{gh}}\right\rangle ,
$$
where $J_{\mathrm{gf}}$ and $J_{\mathrm{gh}}$ are the sources generated by $-\frac{1}{2\xi}(\partial\cdot\mathcal{A})^2$ and by the ghost action. Two comments make the statement precise.

- **The equation holds inside correlators, up to contact terms.** The classical equation is the statement that the integrand of the path integral is stationary; the quantum statement is that the expectation value of the variation vanishes, and additional operators inserted at the same point produce the contact terms. This is general and standard, not special to the gauge field.
- **The gauge-invariance content is in the identities, not in the equation.** Gauge invariance of the action does not survive gauge fixing as invariance of $S$; it survives as the Slavnov–Taylor identities relating Green functions, which are the quantum transcription of the statement that physical amplitudes are independent of the gauge parameter and that longitudinal gauge fields decouple from physical states. The equation of motion and the identities together replace the classical equation $D_\mu F^{\mu\nu}=J^\nu$.

What the algebra adds here is a reading rather than a formula. The covariant divergence that the quantum equation averages is built from the commutator $[\mathcal{A}_\mu,F^{\mu\nu}]$, and the commutator is the adjoint action of the material sector on itself; the current, being the covariant divergence of the curvature, transforms in the adjoint too, $J'_\nu=UJ_\nu U^{-1}$; and the source is therefore a spin-one object of the material sector, exactly as the curvature is. The quantum equation is the stationarity of a functional whose internal index is the spin-one index of the adjoint action.

## Gauge Slicing and the Gribov Ambiguity

The Faddeev–Popov identity presupposes that the gauge condition $G=0$ intersects each orbit exactly once: the insertion of unity is an identity for each orbit, and the argument that the determinant cancels the volume requires the set of solutions to be a single point per orbit. In the abelian theory on a topologically trivial background this holds for the Lorenz gauge, and the determinant is field-independent. In the non-abelian theory it fails, and the failure is structural.

The obstruction has two parts, one analytic and one topological. Analytically, for a generic non-abelian configuration the equation $G[\mathcal{A}^U]=0$, that is $\partial_\mu\mathcal{A}^{U\mu}=0$, has more than one solution $U$; the extra solutions are the **Gribov copies**. The Faddeev–Popov operator $M^{ab}=-\partial\cdot D^{ab}$ is the Hessian of the gauge-fixing functional, and the copies appear where it develops a zero eigenvalue; the set of configurations where this happens is the **Gribov horizon**. Topologically, the space of connections modulo gauge transformations is not covered by a single gauge slice: a continuous global gauge-fixing condition would be a section of a non-trivial bundle, and the standard argument of Singer shows that no such section exists for the non-abelian theory on the sphere or on any non-trivial bundle.

Two consequences follow, and both are properties of the non-abelian path integral as such.

- **The Faddeev–Popov integral overcounts.** A slice that meets an orbit $k$ times is counted $k$ times, and the determinant alone does not correct for it. The corrected integral restricts the configuration space to a **fundamental domain** in which the gauge condition has a unique solution, the interior of the Gribov region; the boundary is the horizon.
- **The horizon is dynamical.** Because the horizon is a statement about the Faddeev–Popov operator, it is affected by the gauge field, and the low-momentum behaviour of the gauge field's propagator is modified by the restriction. This is the analytic setting in which the confining behaviour of the non-abelian theory is studied in the continuum; the non-perturbative construction in which the area law is established is the lattice regularization, cited below.

In the framework's terms the ambiguity is a statement about the adjoint action, and it is worth stating why the two cases differ. In the abelian theory the gauge group is the center, which is one-dimensional and abelian, the orbit direction is the gradient $\tilde{\nabla}\Gamma$, and the gauge-fixing equation is linear in $\Gamma$ with a field-independent operator. In the non-abelian theory the group is the unit quaternions, the orbit direction is $D_\mu\Gamma$ with a connection-dependent covariant derivative, and the equation is no longer linear in the field: the determinant's dependence on $\mathcal{A}$ and the non-uniqueness of the slice are the same fact seen from two sides. The algebra does not remove the ambiguity; it identifies the operator whose kernel creates it as the adjoint twisting of a central differential operator, and it records that the ambiguity is a property of the non-abelian orbit, exactly as the non-abelian equation of motion is.

## What the Algebra Supplies and What It Imports

**Supplied by the algebra, and recomputed here.** The gauge algebra as the compact factor $\mathfrak{su}(2)=\mathrm{span}_\mathbb{R}\{e_1,e_2,e_3\}\subset\mathbb{M}_-$, with structure constants $f^{abc}=2\varepsilon^{abc}$ read from the quaternion commutator; the Jacobi identity, hence the closure of the Slavnov–Taylor and BRST algebras, from associativity; the adjoint covariant derivative $D_\mu{}^{ab}=\partial_\mu\delta^{ab}-i\kappa f^{abc}\mathcal{A}_\mu^c$, verified against $(D_\mu X)^a=\partial_\mu X^a+i\kappa[\mathcal{A}_\mu,X]^a$ on a generic superposition; the Faddeev–Popov operator $M=-\partial\cdot D$, whose derivative part is the central d'Alembertian and whose internal part is the adjoint action; the gauge-parameter-independence of amplitudes built from conserved currents, from the projector algebra; and the observation that the ghosts require the Grassmann envelope because $\mathbb{B}$ has no odd elements.

**Imported, and left visible.** The Faddeev–Popov trick itself and the insertion of unity; the representation of a determinant by a fermionic Gaussian integral; the gauge-fixing condition and the gauge parameter; the Nakanishi–Lautrup field; the Slavnov–Taylor identities and the standard renormalization of the coupling; the one-loop beta coefficient; the Gribov ambiguity and Singer's obstruction; and the non-perturbative construction of confinement. The algebra supplies the carrier and the structure constants; the analytic apparatus of the path integral is standard.

**Not supplied.** The gauge group is fixed to the compact factor the algebra contains, so the construction is the $SU(2)$ theory (with the abelian factor available separately); the hypercharge, the chiral matter representation and the colour octet are outside it. No gauge-fixing principle is native to the algebra, and the choice of $\xi$ remains external. The reality class of the connection is inherited unchanged from the companion articles, where no single Hermitian-conjugation eigenspace survives the transformation law: the inhomogeneous term $\frac{i}{\kappa}(\partial_\mu U)U^{-1}$ is Hermitian in the spatial directions and anti-Hermitian in the $ict$ direction, so that a uniform assignment of all four components to $\mathbb{M}_-$ is preserved in the time direction and obstructed in the space directions, and the only assignment the companion verifies as consistent is the mixed one, $\mathcal{A}_0$ in $\mathbb{M}_-$ and $\mathcal{A}_k$ in $\mathbb{M}_+$. Nothing in the path integral or the Faddeev–Popov procedure relieves that obstruction. As everywhere in the series, no empirical content is added.

## Summary

The Yang–Mills path integral is the functional integral of the companion article specialised to the non-abelian connection, and the Faddeev–Popov procedure is what makes it finite. The gauge-fixing identity $1=\Delta[\mathcal{A}]\int\mathcal{D}U\,\delta(G[\mathcal{A}^U])$ defines a determinant that is gauge invariant, and in the non-abelian theory the determinant depends on the connection through the commutator term of the adjoint covariant derivative,
$$
\Delta[\mathcal{A}]=\det\big(-\partial_\mu D^{\mu\,ab}\big),
\qquad
D_\mu{}^{ab}=\partial_\mu\delta^{ab}-i\kappa f^{abc}\mathcal{A}_\mu^c ,
$$
whereas in the abelian limit $f^{abc}=0$, $M=-\Box$, and the determinant is field-independent. The determinant is written as a functional integral over anticommuting ghosts in the Grassmann envelope $\mathbb{B}\otimes\Lambda$, because $\mathbb{B}$ has no odd elements, and the resulting ghost action $S_{\mathrm{gh}}=-\int\bar c_a\partial_\mu(D^\mu c)^a$ is the one the BRST companion takes as given.

The gauge-fixed action $S=S_{\mathrm{YM}}+S_{\mathrm{gf}}+S_{\mathrm{gh}}$ has a quadratic part whose inversion gives the propagator
$$
D_{\mu\nu}(p)=\frac{1}{p^2}\left(\eta_{\mu\nu}+(1-\xi)\frac{p_\mu p_\nu}{p^2}\right),
$$
with the gauge parameter in the longitudinal projector alone, so that amplitudes built from conserved currents are gauge-parameter independent. The non-abelian additions are the charged, covariantly conserved current; the Slavnov–Taylor identities in place of the abelian Ward identity; and the ghost and self-interaction loops that give the pure $SU(2)$ one-loop coefficient $b_0=22/3$.

The classical equation $D_\mu F^{\mu\nu}=J^\nu$ becomes the Schwinger–Dyson statement
$$
\left\langle\big(D_\mu F^{\mu\nu}\big)^a\right\rangle=\left\langle J^{\nu a}_{\mathrm{gf}}\right\rangle+\left\langle J^{\nu a}_{\mathrm{gh}}\right\rangle ,
$$
valid inside correlators up to contact terms, with the gauge content carried by the Slavnov–Taylor identities. The Faddeev–Popov procedure requires a unique representative per orbit; for the non-abelian theory this fails, and the Gribov copies and the Gribov horizon are the supplementary structure of the non-abelian case, the operator whose kernel produces them being the adjoint twisting of the central d'Alembertian.

The algebra's contribution is therefore specific and limited: it supplies the compact gauge algebra inside the material sector, the structure constants, the Jacobi identity from associativity, and the adjoint action that twists the Faddeev–Popov operator; it does not supply the gauge-fixing condition, the odd coordinates, the loop integrals, the Gribov analysis, or any empirical content.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$, $e_je_k=-\delta_{jk}e_0+\varepsilon_{jkl}e_l$ |
| $i$ | Central scalar imaginary |
| $\mathbb{M}_-,\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_\mathbb{R}\{e_0,ie_0\}$ | Center of the algebra; abelian factor |
| $\tilde{\nabla},\bar{\tilde{\nabla}}$, $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}=\partial_{ict}^2+\Delta$ | Biquaternionic gradient, conjugate, d'Alembertian |
| $\eta=\mathrm{diag}(-1,+1,+1,+1)$ | $ict$ metric (level 2) |
| $\mathfrak{su}(2)=\mathrm{span}_\mathbb{R}\{e_1,e_2,e_3\}\subset\mathbb{M}_-$ | Compact gauge algebra |
| $[e_a,e_b]=2\varepsilon_{abc}e_c$, $T_a=\tfrac12 e_a$, $\mathrm{Tr}(T_aT_b)=-\tfrac12\delta_{ab}$ | Generators and matrix trace |
| $f^{abc}=2\varepsilon^{abc}$ | Structure constants from the quaternion commutator, in the unnormalized basis $e_a$ ($f^{abc}=\varepsilon^{abc}$ in the normalized basis $T_a=\tfrac12e_a$) |
| $\mathcal{A}_\mu=\mathcal{A}_\mu^a e_a\in\mathfrak{su}(2)$, $\kappa=q/\hbar$ | Connection and coupling |
| $D_\mu=\partial_\mu+i\kappa\mathcal{A}_\mu$, $D_\lambda X=\partial_\lambda X+i\kappa[\mathcal{A}_\lambda,X]$ | Covariant derivative; adjoint action |
| $F_{\mu\nu}=\partial_\mu\mathcal{A}_\nu-\partial_\nu\mathcal{A}_\mu+i\kappa[\mathcal{A}_\mu,\mathcal{A}_\nu]$ | Non-abelian curvature |
| $S_{\mathrm{YM}}=-\tfrac12\int\mathrm{Tr}(F_{\mu\nu}F^{\mu\nu})$ | Yang–Mills action (matrix trace) |
| $\mathcal{D}\mathcal{A}=\prod_\mu\prod_a\mathcal{D}\mathcal{A}_\mu^a$ | Measure on $\mathfrak{su}(2)$-valued configurations |
| $G^a[\mathcal{A}]=\partial_\mu\mathcal{A}^{a\mu}-\omega^a$ | Lorenz gauge-fixing condition |
| $1=\Delta[\mathcal{A}]\int\mathcal{D}U\,\delta(G[\mathcal{A}^U])$ | Faddeev–Popov identity |
| $M^{ab}=-\partial_\mu D^{\mu\,ab}$ | Faddeev–Popov operator (field-dependent) |
| $D_\mu{}^{ab}=\partial_\mu\delta^{ab}-i\kappa f^{abc}\mathcal{A}_\mu^c$ | Covariant derivative in the adjoint representation |
| $c^a,\bar c_a$ | Faddeev–Popov ghost and antighost, Grassmann-odd |
| $\mathbb{B}\otimes\Lambda$ | Grassmann envelope; adjoined odd coordinates |
| $S_{\mathrm{gh}}=-\int\bar c_a\partial_\mu(D^\mu c)^a$ | Ghost action from the determinant |
| $S_{\mathrm{gf}}=-\tfrac{1}{2\xi}\int(\partial_\mu\mathcal{A}^{a\mu})^2$ | Gauge-fixing term; $\xi$ the gauge parameter |
| $D_{\mu\nu}(p)=p^{-2}(\eta_{\mu\nu}+(1-\xi)p_\mu p_\nu/p^2)$ | Gauge-field propagator |
| $P_{\mu\nu}=\eta_{\mu\nu}+p_\mu p_\nu/p^2$, $L_{\mu\nu}=-p_\mu p_\nu/p^2$ | Transverse and longitudinal projectors, $P+L=\eta$ |
| $\langle D_\mu F^{\mu\nu}\rangle=\langle J^\nu\rangle$ | Quantum Yang–Mills equation (Schwinger–Dyson) |
| Slavnov–Taylor identities | Quantum content of gauge invariance in the non-abelian theory |
| Gribov copies, Gribov horizon | Multiple solutions of the gauge condition; zeros of $M$ |
| $b_0=\tfrac{11}{3}C_2(G)$ | One-loop coefficient; $C_2(G)=2$ for $SU(2)$ |
| $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Informational trace formula, distinct from the matrix trace |

## Further Reading

- L. D. Faddeev and V. N. Popov, "Feynman diagrams for the Yang–Mills field," *Physics Letters B* **25** (1967) 29–30, for the gauge-fixing determinant and the ghost fields.
- G. 't Hooft, "Renormalizable Lagrangians for massive Yang–Mills fields," *Nuclear Physics B* **35** (1971) 167–188, for the gauge-fixing and ghost structure in renormalizable form.
- B. S. DeWitt, "Quantum theory of gravity. II. The manifestly covariant theory," *Physical Review* **162** (1967) 1195–1239, for the covariant background-field treatment of gauge fixing.
- L. D. Faddeev and A. A. Slavnov, *Gauge Fields: An Introduction to Quantum Theory* (Benjamin/Cummings, 1980), for the Faddeev–Popov procedure, the Slavnov–Taylor identities and the quantum equations of motion.
- S. Weinberg, *The Quantum Theory of Fields, Vol. II: Modern Applications* (Cambridge, 1996), for the non-abelian path integral, the ghosts, the one-loop beta function and the asymptotically free sign.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the Schwinger–Dyson equations, the Ward and Slavnov–Taylor identities and the gauge-parameter-independence argument.
- V. N. Gribov, "Quantization of non-Abelian gauge theories," *Nuclear Physics B* **139** (1978) 1–19, for the copies and the horizon of the gauge-fixing condition.
- I. M. Singer, "Some remarks on the Gribov ambiguity," *Communications in Mathematical Physics* **60** (1978) 7–12, for the topological obstruction to a global gauge slice.
- N. Vandersickel and D. Zwanziger, "The Gribov problem and QCD dynamics," *Physics Reports* **520** (2012) 175–251, for the fundamental domain, the horizon condition and the continuum confinement setting.
- J. B. Kogut and L. Susskind, "Hamiltonian formulation of Wilson's lattice gauge theories," *Physical Review D* **11** (1975) 395–408, for the non-perturbative regulator in which the confining behaviour is established.
- M. F. Atiyah and I. M. Singer, "Dirac operators coupled to vector potentials," *Proceedings of the National Academy of Sciences* **81** (1984) 2597–2600, for the index theory of the covariant derivative in the adjoint representation.
