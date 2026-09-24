# __The Klein–Gordon Path Integral in Biquaternionic Form__

## Introduction

The path integral is the third formulation of a quantum theory, alongside the equation of motion and the operator algebra. For a relativistic scalar field it is the **functional integral over field configurations**, weighted by the phase $e^{iS[\phi]/\hbar}$, and it organises the whole of the free and perturbative theory: the generating functional is a Gaussian in the presence of a source, the free two-point function is the inverse of the quadratic form, the classical field is the stationary point, and the loop expansion is the expansion of the determinant about that point. This article derives the Klein–Gordon functional integral in biquaternionic form, evaluates the free Gaussian exactly, identifies its two-point function with the propagator of the companion article *The Klein–Gordon Propagator and Its Green's Functions in Biquaternionic Form*, and states what the algebra contributes.

The division of labour with the companion path-integral article must be stated at once. The companion article *The Path Integral in Biquaternionic Form* analyses the **algebraic status of the phase**: it shows that the $i$ of $e^{iS/\hbar}$ is the central scalar imaginary, that the exponent lies in the material sector $\mathbb{M}_-$, that the phase is a central unitary element, and that a non-central root would produce a spin rotation rather than a global phase. This article does not repeat that analysis; it takes the centrality of the phase as established and addresses the complementary case, the **relativistic field-theoretic** one: a functional integral over a field configuration space, not a single-particle sum over paths, with the Klein–Gordon quadratic form in the exponent. The non-relativistic single-particle scalar case, which is a sum over paths with a central kernel, belongs to the Schrödinger setting and is not treated here.

The biquaternion content of the Klein–Gordon path integral is a statement about the **configuration space and the quadratic form** rather than about the phase. The field is a function into the center $\mathbb{C}_{\mathbb{B}}$, as the companion article *The Scalar Field in the Center: Why Spin 0 Escapes the Biquaternion State Module* establishes; the action is therefore a central scalar functional; the measure is a measure on a space of central-valued functions; and every object built from the Gaussian — the two-point function, the determinant, the effective action — is central and acts on the state module as scalar multiplication. The two structural points that are genuinely the algebra's are the identification of the **mass shell** with a level set of the norm form, so that the quadratic form in the exponent is the norm form read on the material sector, and the identification of the **Wick rotation** with the passage from the material sector to the quaternion subspace, which is exactly the passage that makes the Euclidean quadratic form positive definite. The path integral's convergence, and its failure for a negative mass squared, are properties of the norm form.

The article is organised as follows. The field configuration space and the action are set up first, and the equation of motion is derived from the action by variation. The generating functional is defined and the free Gaussian is evaluated, first on a finite lattice where it is an ordinary finite-dimensional integral and can be checked exactly, and then in the formal continuum limit. The stationary-phase expansion and the classical field are treated next. The Wick rotation and Euclidean functional are then discussed, with the positivity question. A closing section states the biquaternion reading, and open questions are recorded.

Throughout, the conventions are those of the companion articles: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, central $i$; $\mathbb{C}_{\mathbb{B}}=\operatorname{span}_{\mathbb{R}}\{e_0,ie_0\}$ is the center; $\tilde{X}=ict\,e_0+\mathbf{x}\in\mathbb{M}_-$; $\tilde{\nabla}=e_0\partial_{ict}+\sum_k e_k\partial_k$; and $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}=\partial_{ict}^2+\Delta=\Delta-c^{-2}\partial_t^2$. The scalar field is $\tilde{\Phi}=\phi\,e_0$ with $\phi$ complex, and the mass parameter is $\mu=mc/\hbar$. The analytic parts use natural units $\hbar=c=1$, as the companion articles do.

- Companion article *The Klein–Gordon Equation in Biquaternionic Form*, for the scalar equation, its mass-term sign, and the central scalar operator.
- Companion article *The Klein–Gordon Propagator and Its Green's Functions in Biquaternionic Form*, for the free two-point function, the four contour prescriptions, and the Euclidean kernel.
- Companion article *The Scalar Field in the Center: Why Spin 0 Escapes the Biquaternion State Module*, for the field's central value space and the exclusion of the state module.
- Companion article *The Path Integral in Biquaternionic Form*, for the centrality of the phase, the material sector, and the algebra's complex structure.
- Companion article *The Wick Rotation in the Biquaternion Universe*, for the identification of the material sector with the quaternion subspace.
- Companion article *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, for the material sector, the four-wavevector, and the norm form.

## The Configuration Space and the Action

### The field as a central-valued function

The field of the theory is a function on spacetime taking values in the center,

$$
\tilde{\Phi}(\tilde{X})=\phi(\tilde{X})\,e_0,
\qquad
\phi:\mathbb{R}^{1,3}\to\mathbb{C},
$$

and the configuration space of the theory is the space of such functions. Because the center is the fixed space of the framework's conjugations and the unique rotationally invariant subspace of the algebra, the field carries no index of any kind; this is the field-theoretic form of spin $0$, and it is the reason the configuration space is a space of *complex-valued* functions rather than a space of module-valued or algebra-valued ones. The real and imaginary parts of $\phi$ are the scalar parts of the two sectors,

$$
\phi=\phi_1+i\phi_2,
\qquad
\tilde{\Phi}=\underbrace{\phi_1\,e_0}_{\in\,\mathbb{M}_+}+\underbrace{\phi_2\,ie_0}_{\in\,\mathbb{M}_-},
$$

so that the complex scalar is equivalent to two real scalars, one in each sector's scalar direction. The configuration space is therefore also the space of pairs of real functions, and the complex structure that makes it a single complex field is the central scalar imaginary.

### The action and its variation

The Klein–Gordon action for the complex scalar field is the standard relativistic scalar action, written with the framework's d'Alembertian. In natural units,

$$
S[\tilde{\Phi}]
=\int d^4x\left[-\frac{1}{2}\partial_\mu\phi^*\,\partial^\mu\phi-\frac{1}{2}\mu^2\,|\phi|^2\right],
$$

with the index contracted by the level-2 $ict$ metric $\eta=\mathrm{diag}(-1,+1,+1,+1)$; in biquaternion form, using $\tilde{\Phi}^\dagger=\phi^*e_0$ and $\mathrm{Sc}(\tilde{\Phi}^\dagger\tilde{\Phi})=|\phi|^2$, this is a central scalar functional,

$$
S[\tilde{\Phi}]=\int d^4x\left[-\frac{1}{2}\mathrm{Sc}\!\left(\partial_\mu\tilde{\Phi}^\dagger\,\partial^\mu\tilde{\Phi}\right)-\frac{1}{2}\mu^2\,\mathrm{Sc}\!\left(\tilde{\Phi}^\dagger\tilde{\Phi}\right)\right]\in\mathbb{C}_{\mathbb{B}} .
$$

The action is central because every ingredient in it is: the field is central, the derivatives act coefficient-wise, the metric contraction is a real number, and the trace is the trace formula's scalar projection. It is also real, since the kinetic and mass terms are Hermitian.

The equation of motion follows by variation. For a variation $\delta\tilde{\Phi}$ vanishing at the boundary,

$$
\delta S
=\frac{1}{2}\int d^4x\left[-\partial_\mu\delta\phi^*\,\partial^\mu\phi-\mu^2\,\delta\phi^*\,\phi\right]
=\frac{1}{2}\int d^4x\;\delta\phi^*\left[\left(\Box-\mu^2\right)\phi\right],
$$

after integrating by parts and discarding the boundary term; the overall factor is immaterial for the stationarity condition, but it is kept so that the displayed variation is the variation of the action written above. With $\partial_\mu\partial^\mu=\Box$, the stationarity of the action is

$$
\frac{\delta S}{\delta\phi^*}=0
\qquad\Longleftrightarrow\qquad
\left(\Box-\mu^2\right)\phi=0,
$$

which is the Klein–Gordon equation of the companion article. The derivation was checked against three independent on-shell modes: for the superposition

$$
\phi(t,x,y,z)=\sum_{n=1}^{3}a_n\cos(\mathbf{k}_n\cdot\mathbf{x}-\Omega_n t),
\qquad
\Omega_n=\sqrt{\mathbf{k}_n^2+\mu^2},
$$

with $|\mathbf{k}_n|=(1.3,2.1,0.8)$ along the directions $(0.2,-0.5,0.7)$, $(-0.9,0.4,0.1)$, $(0.6,0.6,-0.3)$ in turn, amplitudes $(a_1,a_2,a_3)=(1.0,0.7,-0.5)$ and $\mu=1.1$, the finite-difference evaluation of $(\Box-\mu^2)\phi$ at three generic events had a greatest residual of order $10^{-7}$, the residual being the truncation error of the difference stencil rather than a failure of the equation. The linearity of the equation makes the superposition a weak test; the test's content is in the signs, and it confirms that the sign conventions of the action, of $\Box$, and of the mass term are mutually consistent.

### The norm-form reading of the quadratic form

The quadratic part of the action can be written in a form that displays the algebra. Integrating the kinetic term by parts,

$$
S[\tilde{\Phi}]=\frac{1}{2}\int d^4x\;\mathrm{Sc}\!\left(\tilde{\Phi}^\dagger\left(\Box-\mu^2\right)\tilde{\Phi}\right),
$$

so the operator in the exponent is exactly the Klein–Gordon operator whose Green's functions the companion article constructs. The mass shell is where the momentum-space symbol vanishes,

$$
\frac{\omega^2}{c^2}-\mathbf{k}^2-\mu^2=0
\qquad\Longleftrightarrow\qquad
N(\tilde{K})=\tilde{K}\bar{\tilde{K}}=-\mu^2,
$$

a level set of the norm form on the material four-wavevector $\tilde{K}=i\omega/c\,e_0+\mathbf{k}$. The quadratic form of the path integral is thus the norm form of $\mathbb{M}_-$, shifted by the mass: the exponent's saddle is the norm form's level set, and the Gaussian's width is the operator whose symbol is that norm form minus the mass. This is the sense in which the framework's contribution to the scalar path integral is geometry rather than a new mechanism.

## The Generating Functional and the Free Gaussian

### Definitions

The generating functional is

$$
Z[J]=\int\mathcal{D}\tilde{\Phi}\;\exp\left(iS[\tilde{\Phi}]+i\int d^4x\;\mathrm{Sc}\!\left(\tilde{J}^\dagger\tilde{\Phi}\right)\right),
$$

with a central source $\tilde{J}=J\,e_0$ and a measure $\mathcal{D}\tilde{\Phi}$ on the central-valued configuration space. The correlation functions are the functional derivatives with respect to the source; the normalisation $Z[0]$ is fixed by the requirement that the vacuum expectation of the identity be one. The phase factor is the central unitary element analysed in the companion article *The Path Integral in Biquaternionic Form*, and the measure is a measure on a space of complex functions, i.e. on a space of pairs of real functions.

### The finite-dimensional Gaussian, exactly

The rigorous content of the free functional integral is the finite-dimensional Gaussian identity, of which the continuum integral is the formal limit. On a lattice of $N$ sites with a real symmetric positive-definite quadratic form $A$, the integral

$$
Z_N[J]=\int\prod_{i=1}^{N}d\phi_i\;\exp\left(-\frac{1}{2}\phi^{T}A\phi+J^{T}\phi\right)
$$

evaluates to

$$
\boxed{\;Z_N[J]=(2\pi)^{N/2}\left(\det A\right)^{-1/2}
\exp\left(\frac{1}{2}J^{T}A^{-1}J\right)\;}
$$

and the two-point function is the inverse of the quadratic form,

$$
\langle\phi_i\phi_j\rangle=\left(A^{-1}\right)_{ij},
\qquad
\partial_{J_i}\partial_{J_j}\ln Z_N\big|_{J=0}=\left(A^{-1}\right)_{ij}.
$$

Both statements were verified numerically. For $N=2$ with $A=\begin{pmatrix}1.7&0.4\\0.4&1.1\end{pmatrix}$ and $J=(0.3,-0.8)$, direct two-dimensional quadrature of the integral gave $7.191119$, and the closed formula gave $7.191119$, agreeing to a relative error of $4.8\times10^{-13}$. For a four-site lattice Klein–Gordon form with spacing $h=0.25$ and $\mu=0.7$, the product $AA^{-1}$ differed from the identity by at most $5.6\times10^{-16}$. The Gaussian identity is therefore the exact backbone of the free theory, and the lattice version is the regulator that makes the formal continuum statement well defined.

### The lattice Klein–Gordon form and its inverse

On the lattice the Klein–Gordon quadratic form is the discretisation of $-\Delta_E+\mu^2$ in the Euclidean formulation,

$$
A_{ij}=\frac{2}{h^2}+\mu^2\;\;\text{on the diagonal},
\qquad
A_{i,i+1}=A_{i+1,i}=-\frac{1}{h^2},
$$

with Dirichlet endpoints, and its inverse is the lattice propagator. The continuum limit $h\to0$ on a fixed physical volume gives the Euclidean Green's function

$$
G_E(\tilde{X}_E)=\left(-\Delta_E+\mu^2\right)^{-1},
\qquad
\tilde{G}_E(p)=\frac{1}{\mathbf{p}_E^2+\mu^2},
$$

which is the standard massive Euclidean propagator. The free two-point function of the path integral is therefore the Euclidean kernel

$$
\langle\tilde{\Phi}(\tilde{X}_E)\tilde{\Phi}^\dagger(\tilde{Y}_E)\rangle
=G_E(\tilde{X}_E-\tilde{Y}_E)\,e_0,
$$

a central scalar times $e_0$, whose closed Yukawa form is given in the companion article on the propagator. The identity of the Gaussian two-point function with the inverse of the quadratic form, verified exactly on the lattice, is the path-integral proof that the free propagator is the Green's function of the Klein–Gordon operator: the two constructions agree by construction once the quadratic form is identified with the operator.

### The continuum limit, formally

In the continuum the same completion of the square gives

$$
Z[J]=Z[0]\exp\left(\frac{i}{2}\int d^4x\,d^4y\;J(x)\,G(x-y)\,J(y)\right),
$$

where $G$ is the Green's function of $(\Box-\mu^2)$, fixed by the boundary condition ($i\epsilon$ prescription) that the Gaussian's analytic continuation requires. The free two-point function is $G$ up to the overall normalisation convention fixed in the companion article on the propagator, where the same kernel is obtained as the inverse of the differential operator. The two routes agree; the lattice computation is the rigorous version of the statement, and the continuum formula is its formal limit. The determinant $Z[0]$ is the inverse square root of the operator determinant, a central scalar; it is the free vacuum amplitude, and the phase of its analytic continuation is the zero-point phase.

## The Semiclassical Expansion

### The classical field and stationary phase

For a source, the classical field is the stationary point of the exponent,

$$
\frac{\delta}{\delta\phi^*}\left(S[\phi]+\int J^*\phi+\phi^* J\right)=0
\qquad\Longleftrightarrow\qquad
\left(\Box-\mu^2\right)\phi=-J,
$$

which is the Klein–Gordon equation with a source and is solved by the convolution with the retarded kernel of the companion article. Expanding about the classical field $\phi_{\mathrm{cl}}$,

$$
\phi=\phi_{\mathrm{cl}}+\xi,
$$

the exponent separates into the classical action, a linear term that vanishes by stationarity, and the quadratic fluctuation term $\frac{1}{2}\xi(\Box-\mu^2)\xi$. The one-loop approximation is the Gaussian integral over $\xi$, giving

$$
Z[J]\simeq e^{\,iS[\phi_{\mathrm{cl}}]+i\int J^*\phi_{\mathrm{cl}}}\,
\left[\det\left(\Box-\mu^2\right)\right]^{-1/2},
$$

a central scalar phase times a central scalar determinant. The effective action is the Legendre transform of $\ln Z$, and it is central for the same reason. Every object in the semiclassical expansion is a central scalar, and the state module plays no role at any order; the loop expansion of a spin-$0$ field is a scalar loop expansion tensored with the identity.

### The saddle and the norm form

The classical equation's momentum-space form is the vanishing of the symbol of the quadratic form,

$$
\left(\frac{\omega^2}{c^2}-\mathbf{k}^2-\mu^2\right)\tilde{\phi}_{\mathrm{cl}}(\omega,\mathbf{k})=-\tilde{J}(\omega,\mathbf{k}),
$$

so that the propagator is the inverse of the norm form shifted by the mass. In the framework's terms, the saddle condition is that the four-wavevector of a free mode lies on the level set $N(\tilde{K})=-\mu^2$ of the norm form of $\mathbb{M}_-$, and the source moves the field off the shell by an amount measured by the norm form through the kernel. This is the third formulation's version of the same norm-form geometry that the equation and the propagator exhibit.

## The Wick Rotation and the Euclidean Functional

### The transfer to the quaternion subspace

The oscillatory functional integral is converted into a decaying one by the Wick rotation, which the companion article *The Wick Rotation in the Biquaternion Universe* identifies with the passage from the material sector to the quaternion subspace: the imaginary time coefficient $ict$ is relabelled as the real coefficient $c\tau$, and a point of $\mathbb{M}_-$ becomes a point of $\mathbb{H}_{\mathbb{B}}$,

$$
\tilde{X}=ict\,e_0+\mathbf{x}\;\in\;\mathbb{M}_-
\qquad\longmapsto\qquad
\tilde{X}_E=c\tau\,e_0+\mathbf{x}\;\in\;\mathbb{H}_{\mathbb{B}} .
$$

On $\mathbb{H}_{\mathbb{B}}$ the norm form is positive definite, and this is exactly what the Euclidean functional integral needs. The action becomes

$$
S[\tilde{\Phi}]\;\longmapsto\;iS_E[\tilde{\Phi}],
\qquad
S_E[\tilde{\Phi}]=\frac{1}{2}\int d^4x_E\;\mathrm{Sc}\!\left(\tilde{\Phi}^\dagger\left(-\Delta_E+\mu^2\right)\tilde{\Phi}\right),
$$

and the phase factor becomes a decaying weight,

$$
e^{\,iS/\hbar}\;\longmapsto\;e^{-S_E/\hbar},
\qquad
S_E\ge 0 .
$$

The Euclidean quadratic form $-\Delta_E+\mu^2$ is positive definite for $\mu^2\ge0$, which is the statement that the norm form on $\mathbb{H}_{\mathbb{B}}$ is positive definite and the mass adds a positive constant. The Gaussian integral converges, the lattice verification above is a verification of the Euclidean integral, and the continuum object it defines is the Euclidean Green's function whose Yukawa form the propagator article gives. The Wick rotation's phase was checked algebraically: the symbol of the Minkowski operator at $\omega=i p_4$ is $-\left(p_4^2+\mathbf{k}^2+\mu^2\right)$, negative, so its negative is the positive Euclidean symbol.

### The positivity question and the tachyon

The Euclidean quadratic form is positive definite precisely when $\mu^2\ge0$. For a negative mass squared, $\mu^2<0$, the Euclidean operator $-\Delta_E+\mu^2$ has a negative eigenvalue in the long-wavelength mode, the Gaussian weight $e^{-S_E}$ grows in that direction, and the functional integral diverges. In the norm-form reading this is the statement that the level set $N(\tilde{K})=-\mu^2$ becomes spacelike rather than timelike: for $\mu^2<0$ the "mass shell" is a spacelike hyperboloid, the mode with $\mathbf{k}=0$ has $\Omega^2=\mu^2<0$, and the saddle is not a minimum of the Euclidean action. The instability is a property of the norm form's signature, and the framework exhibits it as such rather than as an accident of a potential. The oscillatory Minkowski integral is formally defined in either case, but only for $\mu^2\ge0$ is the analytic continuation to Euclidean space a convergent Gaussian.

### The Euclidean two-point function and its relation to the propagator

The Euclidean two-point function obtained from the Gaussian is $G_E=(-\Delta_E+\mu^2)^{-1}$, and its analytic continuation back to Minkowski time gives the Feynman propagator of the companion article, with the $i\epsilon$ prescription produced by the rotation of the contour. The identification is the standard one and is not repeated here; what the framework adds is that the Euclidean object is a function on $\mathbb{H}_{\mathbb{B}}$, on which the norm form is positive definite, and that the rotation is the sector relabelling of the Wick-rotation article rather than an ad hoc substitution. The causal structure lost in the transfer — the light cone, the ordering — is exactly the Lorentzian structure of $\mathbb{M}_-$ that the Euclidean problem does not retain, which is why the Euclidean functional is well suited to equilibrium and correlation questions and not to causal ones.

## The Biquaternion Reading

Four statements summarise what the framework contributes to the Klein–Gordon path integral.

**The configuration space is the center.** The field is central-valued and the measure is a measure on central-valued functions; the complex scalar is two real scalars, one in each sector's scalar direction. This is the path-integral form of the structural article's verdict that spin $0$ lives in the center, and it is why the theory's functional integral is an ordinary complex scalar functional integral rather than an integral over a module.

**The quadratic form is the norm form.** The momentum-space symbol of the exponent is the norm form of the material four-wavevector shifted by the mass, and the mass shell is the level set $N(\tilde{K})=-\mu^2$. The Gaussian's width and the shell's location are the same algebraic object.

**The Wick rotation is the sector relabelling.** The passage to imaginary time is the identification of $\mathbb{M}_-$ with $\mathbb{H}_{\mathbb{B}}$, and the Euclidean quadratic form is positive definite because the norm form is positive definite on the quaternion subspace. Convergence of the Euclidean functional and the tachyon instability for $\mu^2<0$ are both statements about that signature.

**Everything is central, and the module is a spectator.** The action, the phase, the determinant, the effective action and the two-point function are all central scalars, and the state module on which spinor fields live is not acted upon. This is the same statement that the companion article on the propagator makes for the kernel, here at the level of the whole functional integral.

## Open Questions

1. **The measure.** *Open for the author.* The functional measure $\mathcal{D}\tilde{\Phi}$ is defined here as the formal limit of the lattice measure, and the lattice measure is Lebesgue measure on the central-valued field at each site. Whether the framework supplies a canonical measure from its own structure — from the trace form, or from the norm form, or from the real structure $\flat$ — rather than inheriting the Lebesgue measure, is not settled here.

2. **Interactions.** The article has treated only the free Gaussian and the one-loop expansion about a source. A quartic interaction $\lambda|\phi|^4$ is central and preserves the centrality of every object; whether the framework's trace form suggests a preferred normalisation of the coupling, or a preferred class of interactions, is not considered.

3. **The determinant and its phase.** The free determinant $[\det(\Box-\mu^2)]^{-1/2}$ is central, but its phase requires a regularisation and a choice of branch. Whether the framework's complex structure fixes the branch, or whether the standard $i\epsilon$ prescription is the only input, is not resolved.

4. **The Euclidean functional on $\mathbb{H}_{\mathbb{B}}$.** The Wick rotation identifies Minkowski spacetime $\mathbb{M}_-$ with the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, so the Euclidean functional is an integral over central-valued functions *on $\mathbb{H}_{\mathbb{B}}$*; the field itself remains central, and it is the spacetime point that moves. Whether a non-scalar sector requires a genuinely $\mathbb{H}_{\mathbb{B}}$-valued Euclidean field, and whether that formulation admits configurations with no Minkowski counterpart, is a question about the Wick rotation that the companion article leaves open.

5. **The relation to the non-relativistic path integral.** The Klein–Gordon kernel reduces to the Schrödinger kernel in the non-relativistic limit, but the non-relativistic scalar path integral is a single-particle sum over paths, not a field functional integral. Whether the non-relativistic theory should be read as the one-particle sector of the field functional integral, or as an independent construction, is a question for the non-relativistic articles.

6. **The gravitational and variable-$c$ settings.** On a curved background, or in a medium in which the framework's local complex structure makes $c$ a field, the quadratic form is not the flat norm form and the Euclidean form need not be positive. The convergence argument of this article does not extend to those settings.

## Summary

The Klein–Gordon path integral is the functional integral over central-valued fields, $\tilde{\Phi}=\phi e_0$ with $\phi$ complex, weighted by the central phase $e^{iS}$ with the action

$$
S[\tilde{\Phi}]=\frac{1}{2}\int d^4x\;\mathrm{Sc}\!\left(\tilde{\Phi}^\dagger\left(\Box-\mu^2\right)\tilde{\Phi}\right)
=\int d^4x\left[-\frac{1}{2}\partial_\mu\phi^*\partial^\mu\phi-\frac{1}{2}\mu^2|\phi|^2\right].
$$

Its variation gives the Klein–Gordon equation $(\Box-\mu^2)\phi=0$, verified on a superposition of three on-shell modes to a residual of order $10^{-7}$. The generating functional is defined with a central source, and the free Gaussian is evaluated exactly on a finite lattice,

$$
Z_N[J]=(2\pi)^{N/2}(\det A)^{-1/2}\exp\!\left(\frac{1}{2}J^{T}A^{-1}J\right),
\qquad
\langle\phi_i\phi_j\rangle=(A^{-1})_{ij},
$$

verified by direct quadrature (relative error $4.8\times10^{-13}$) and by the lattice inverse ($A A^{-1}-I$ bounded by $5.6\times10^{-16}$). The free two-point function is the inverse of the Klein–Gordon quadratic form, i.e. the Green's function whose Minkowski continuation is the Feynman propagator of the companion article. In the continuum the same completion of the square gives a Gaussian in the source with the Green's function as its kernel, and the determinant is the free vacuum amplitude.

The semiclassical expansion about a source has the classical Klein–Gordon equation as its saddle, a central scalar classical action as its leading phase, and a central scalar determinant as its one-loop factor; every order of the loop expansion is central and the state module is a spectator. The Wick rotation is the identification of the material sector $\mathbb{M}_-$ with the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, with the imaginary time coefficient relabelled as real; the Euclidean quadratic form $-\Delta_E+\mu^2$ is positive definite for $\mu^2\ge0$, which is the positivity of the norm form on $\mathbb{H}_{\mathbb{B}}$, and for $\mu^2<0$ the Euclidean Gaussian diverges, the tachyon being the statement that the norm-form level set has turned spacelike. The quadratic form's symbol is the norm form of the material four-wavevector shifted by the mass, so the mass shell is the level set $N(\tilde{K})=-\mu^2$; the shell's geometry, the Gaussian's width and the convergence of the Euclidean integral are three readings of one algebraic object, and no part of the algebra beyond the center and the norm form enters.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| $\mathbb{C}_{\mathbb{B}}=\operatorname{span}_{\mathbb{R}}\{e_0,ie_0\}$ | Center of $\mathbb{B}$; the scalar field's value space |
| $\mathbb{M}_-,\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{H}_{\mathbb{B}}$ | Quaternion subspace, target of the Wick rotation |
| $\tilde{X}=ict\,e_0+\mathbf{x}$ | Material coordinate, $\in\mathbb{M}_-$ |
| $\tilde{X}_E=c\tau\,e_0+\mathbf{x}$ | Euclidean coordinate, $\in\mathbb{H}_{\mathbb{B}}$ |
| $\tilde{\Phi}=\phi e_0$ | Scalar (spin-$0$) field, valued in the center |
| $\tilde{K}=i\omega/c\,e_0+\mathbf{k}$ | Material four-wavevector, $\in\mathbb{M}_-$ |
| $N(\tilde{Q})=\tilde{Q}\bar{\tilde{Q}}$ | Norm form; $N(\tilde{K})=-\mu^2$ is the mass shell |
| $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}=\partial_{ict}^2+\Delta$ | d'Alembertian, series convention |
| $\mu=mc/\hbar$ | Mass parameter ($\mu=m$ in natural units) |
| $\Omega_{\mathbf{k}}=\sqrt{\mathbf{k}^2+\mu^2}$ | On-shell frequency, natural units |
| $S[\tilde{\Phi}]$ | Klein–Gordon action, central scalar |
| $S_E[\tilde{\Phi}]$ | Euclidean action, $\ge0$ for $\mu^2\ge0$ |
| $Z[J]$ | Generating functional; $\tilde{J}=Je_0$ a central source |
| $G$, $G_E$ | Two-point kernels, $(\Box-\mu^2)G=-\delta^{(4)}$ and $(-\Delta_E+\mu^2)G_E=\delta^{(4)}$ |
| $A$, $A^{-1}$ | Lattice quadratic form and its inverse (lattice propagator) |
| $\eta=\mathrm{diag}(-1,+1,+1,+1)$ | $ict$-coordinate metric (level 2) |
| $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace formula |

## Further Reading

- R. P. Feynman, "Space-Time Approach to Non-Relativistic Quantum Mechanics", *Reviews of Modern Physics* **20** (1948), 367, for the original path-integral formulation and the sum over histories.
- R. P. Feynman and A. R. Hibbs, *Quantum Mechanics and Path Integrals* (McGraw-Hill, 1965), for the construction of the path integral from short-time kernels and the semiclassical expansion.
- Steven Weinberg, *The Quantum Theory of Fields, Vol. I: Foundations* (Cambridge, 1995), for the functional integral for scalar fields, the generating functional, and the Gaussian evaluation.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the free-field generating functional, the two-point function as the inverse quadratic form, and the Wick rotation.
- Claude Itzykson and Jean-Bernard Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the loop expansion, the effective action, and the determinant of the fluctuation operator.
- J. Glimm and A. Jaffe, *Quantum Physics: A Functional Integral Point of View* (Springer, 1987), for the constructive definition of scalar field functional integrals and the role of the lattice regulator.
- M. Reed and B. Simon, *Methods of Modern Mathematical Physics, Vol. II: Fourier Analysis, Self-Adjointness* (Academic Press, 1975), for Gaussian measures on function spaces and the positive-definiteness conditions for the Euclidean quadratic form.
- I. S. Gradshteyn and I. M. Ryzhik, *Table of Integrals, Series and Products* (Academic Press, 2007), for the finite-dimensional Gaussian integral and its determinant factor.
