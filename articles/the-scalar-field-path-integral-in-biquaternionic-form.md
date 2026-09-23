# __The Scalar Field Path Integral in Biquaternionic Form__

## Introduction

A quantum field theory admits three formulations: the equation of motion, the operator algebra, and the functional integral. For the scalar field of this framework the first two are the subjects of the companion articles *The Klein–Gordon Equation in Biquaternionic Form* and *Canonical Quantization of the Biquaternion Klein–Gordon Field*; the third is the subject of this article. The functional integral writes the theory as a sum over field configurations weighted by the central phase $e^{iS/\hbar}$, and in doing so it makes the correlation functions of the quantized field the moments of a distribution on the space of classical configurations.

The division of labour among the path-integral articles of the corpus must be stated at once. The algebraic status of the phase — that the $i$ of $e^{iS/\hbar}$ is the central scalar imaginary, that the exponent lies in the material sector, and that the phase is a central unitary element — is a general statement about the functional integral and belongs to the companion article *The Functional Integral in Biquaternionic Form*, not here; it is taken as established. The functional integral of the **one-particle** Klein–Gordon theory, with its free Gaussian and its lattice regulator, is a statement in the relativistic quantum-theory category, given by the companion article *The Klein–Gordon Path Integral in Biquaternionic Form*, and is likewise not repeated. What is treated here is the complementary object: the functional integral of the **quantized** scalar field, its derivation from the operator formalism of the companion articles, its correlation functions, and its relation to the vacuum persistence amplitude and to pair creation.

Three statements organise the article.

1. **The integration variable is a central-valued c-number field.** The field configurations are functions into the center $\mathbb{C}_{\mathbb{B}}$; the action, the source and the measure are central; and the weight is a central phase. Because the scalar field is bosonic, the sum over configurations is an ordinary (functional) integral over complex functions; it is the fermionic case that would require anticommuting values. This is the path-integral form of the statement that spin $0$ lives in the center.
2. **The functional integral is the operator formalism's generating functional.** Its functional derivatives reproduce the time-ordered correlation functions of the field operator of the companion article *The Quantized Scalar Field in Biquaternionic Form*; the free two-point function is the Feynman propagator; the vacuum functional is the norm of the vacuum-to-vacuum amplitude. The canonical commutator is recovered from the representation $\hat\pi=-i\hbar\,\delta/\delta\phi$.
3. **The algebra contributes the same three things it contributes elsewhere in the scalar sector.** The centrality of the field and the source; the norm-form reading of the quadratic form, whose momentum-space symbol is the norm form of the material four-wavevector shifted by the mass; and the identification of the Wick rotation with a sector relabelling. No new mechanism and no native ladder; the bosonic gap of the companion Fock-space article persists.

The article is organised as follows. The next section derives the functional integral from the field-eigenvalue basis and the time-slicing of the propagator. The following section defines the generating functional and evaluates the free Gaussian. The next section establishes the equivalence with the operator formalism. The section after that treats the vacuum persistence amplitude and its relation to pair creation. A section states the biquaternion reading. The article closes with the standard/open separation.

- Companion article *Canonical Quantization of the Biquaternion Klein–Gordon Field*, for the equal-time commutators, the mode algebra and the Hamiltonian whose matrix elements the path integral reproduces.
- Companion article *The Quantized Scalar Field in Biquaternionic Form*, for the field operator, the Wightman function and the Feynman propagator that the Gaussian produces.
- Companion article *The Scalar Fock Space in Biquaternionic Form*, for the state space on which the functional integral's correlators are defined.
- Companion article *Scalar Pair Creation in Biquaternionic Form*, for the external-background process whose probability is the modulus squared of the vacuum functional.
- Companion article *Noether's Theorem in Biquaternionic Form*, for the central scalar action and the current.
- Companion article *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, for the material four-wavevector and the norm form.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0=1,e_1,e_2,e_3$ with $e_k^2=-e_0$, and $i$ is the central scalar imaginary. The material and informational sectors are $\mathbb{M}_-$ and $\mathbb{M}_+$; the center is $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_0,ie_0\}$. The gradient is $\tilde{\nabla}=e_0\partial_{ict}+e_1\partial_x+e_2\partial_y+e_3\partial_z$ and $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}=\partial_{ict}^2+\Delta$. The scalar field is $\tilde{\Phi}=\phi\,e_0$ with $\phi$ complex, written in real components as $\phi=(\phi_1+i\phi_2)/\sqrt2$, so that $\mathrm{Sc}(\tilde{\Phi}^\dagger\tilde{\Phi})=\frac12(\phi_1^2+\phi_2^2)$ and the kinetic term is $\frac12[(\partial\phi_1)^2+(\partial\phi_2)^2]$ — the component normalization of the companion articles on the quantized field and on symmetry breaking — and the mass parameter is $\mu=mc/\hbar$. Natural units $\hbar=c=1$ are used in the analytical parts. The metric of the $ict$ sector is $\eta=\mathrm{diag}(-1,+1,+1,+1)$; physical components are written $x=(t,\mathbf{x})$ and $p=(\omega,\mathbf{p})$, with $E_{\mathbf{p}}=\sqrt{\mathbf{p}^2+\mu^2}$.

## From the Operator Formalism to the Functional Integral

The functional integral is derived from the operator formalism by inserting a complete set of field eigenstates at each time. The field operator $\hat{\phi}(\mathbf{x})$ has a continuum of eigenstates,

$$
\hat{\phi}(\mathbf{x})|\phi\rangle=\phi(\mathbf{x})|\phi\rangle,
\qquad
\langle\phi'|\phi\rangle=\delta[\phi'-\phi],
\qquad
\int\mathcal{D}\phi\,|\phi\rangle\langle\phi|=\mathbf{1},
$$

with real eigenvalues for the real field and complex eigenvalues for the complex one. The transition amplitude factors into short-time pieces, and inserting the field basis between them gives, for a real field,

$$
\langle\phi_f,t_f|\phi_i,t_i\rangle
=\int_{\phi(t_i)=\phi_i}^{\phi(t_f)=\phi_f}\mathcal{D}\phi\;
\exp\left(\frac{i}{\hbar}\int_{t_i}^{t_f}\!dt\,L[\phi,\dot{\phi}]\right),
$$

with $L=\int d^3x\,\mathcal{L}$; the phase-space form is obtained by inserting also the momentum completeness relation, and integrating out the momentum returns the Lagrangian form above. The boundary values $\phi_i,\phi_f$ are held fixed, and the measure is the formal product of Lebesgue measures at each time slice, $\mathcal{D}\phi=\prod_t d\phi(t)$, made meaningful by a lattice regulator as in the finite-dimensional Gaussian below.

In the framework's notation the field is central-valued and the weight is a central phase,

$$
\tilde{\Phi}(\tilde{X})=\phi(\tilde{X})e_0,
\qquad
S[\tilde{\Phi}]=\int d^4x\left[-\mathrm{Sc}\!\left[(\bar{\tilde{\nabla}}\tilde{\Phi}^\dagger)(\tilde{\nabla}\tilde{\Phi})\right]-\mu^2\,\mathrm{Sc}\!\left(\tilde{\Phi}^\dagger\tilde{\Phi}\right)\right],
$$

$$
Z=\int\mathcal{D}\tilde{\Phi}\;e^{\,iS[\tilde{\Phi}]/\hbar},
\qquad
e^{\,iS/\hbar}\ \text{a central unitary} .
$$

Three features of this rewriting are structural rather than cosmetic. First, the integration variable is a function into the **center**, so the path integral is an ordinary functional integral over complex functions, equivalently over pairs of real functions, and the state module on which spinor fields live is not integrated over at all. Second, the quadratic form in the exponent is the norm form shifted by the mass: the momentum-space symbol of $(\Box-\mu^2)$ on the plane wave $e^{-ip\cdot x}$ is

$$
\frac{\omega^2}{c^2}-\mathbf{k}^2-\mu^2
=-\left(N(\tilde{K})+\mu^2\right),
\qquad
N(\tilde{K})=\tilde{K}\bar{\tilde{K}},
\qquad
\tilde{K}=i\frac{\omega}{c}\,e_0+\mathbf{k},
$$

which vanishes precisely on the mass shell $N(\tilde{K})=-\mu^2$, so the Gaussian's width and the mass shell are one algebraic object; the propagator is the inverse of this symbol, $\Delta_F(\tilde{K})=-i/(N(\tilde{K})+\mu^2-i\epsilon)$, exactly as the companion field article has it. Third, the phase is central, so it commutes with every element of the algebra and multiplies configuration space uniformly; no rotor and no spinor index enters. The three are the same three facts that the one-particle and propagator articles record for their own objects.

## The Phase-Space Form and the Semiclassical Kernel

The time-sliced construction above can be written in either the Lagrangian or the Hamiltonian form, and the passage between them is the path-integral version of the Legendre transform of the companion quantization. Inserting at each slice the momentum completeness relation

$$
\int\mathcal{D}\pi\,|\pi\rangle\langle\pi|=\mathbf{1},
\qquad
\langle\phi|\pi\rangle=e^{\,\frac{i}{\hbar}\int d^3x\,(\pi\phi+\pi^\dagger\phi^\dagger)},
$$

and using $\langle\pi|\hat H|\phi\rangle=\langle\pi|\phi\rangle H(\phi,\pi)$, the kernel becomes

$$
\langle\phi_f,t_f|\phi_i,t_i\rangle
=\int\mathcal{D}\phi\,\mathcal{D}\pi\;
\exp\left(\frac{i}{\hbar}\int_{t_i}^{t_f}\!dt\int d^3x\,
\big[\pi\,\dot{\phi}+\pi^\dagger\dot{\phi}^\dagger-\mathcal{H}(\phi,\pi)\big]\right),
$$

the **phase-space** or Hamiltonian form of the functional integral. The momentum is now an independent integration variable, and because the field is complex both kinetic terms appear, with the corresponding boundary terms fixed at the endpoints. Because the Hamiltonian is quadratic in $\pi$, the momentum integral is a Gaussian and can be performed explicitly; it reproduces the Lagrangian form, since with the Hamiltonian $\mathcal{H}=c^{2}\pi\pi^{\dagger}+|\nabla\phi|^{2}+\mu^{2}|\phi|^{2}$ the saddle value of $\pi\dot{\phi}+\pi^{\dagger}\dot{\phi}^{\dagger}-\mathcal{H}$ is $2c^{-2}|\dot{\phi}|^{2}-c^{-2}|\dot{\phi}|^{2}-|\nabla\phi|^{2}-\mu^{2}|\phi|^{2}=\mathcal{L}$. The saddle point of the momentum integral is

$$
\frac{\partial\mathcal{H}}{\partial\pi}=\dot{\phi}
\qquad\Longleftrightarrow\qquad
\pi=\frac{1}{c^2}\dot{\phi}^{\,*},
$$

which is the conjugate momentum of the companion canonical quantization. The regularity of the Legendre transform — no constraint, no gauge redundancy — is what makes the passage between the two forms exact and uncontroversial in the scalar sector; in the Dirac and Maxwell cases the same passage requires the introduction of ghosts and constraints, and the framework supplies no principle that would avoid them.

The path integral is also a semiclassical expansion. Writing $\phi=\phi_{cl}+\eta$ about a solution of the classical equation, the exponent expands as

$$
S[\phi_{cl}+\eta]=S[\phi_{cl}]
+\int d^4x\,\eta^\dagger\!\left(\Box-\mu^2\right)\!\eta+O(\eta^3),
$$

the linear term vanishing by the equation of motion, and the quadratic term carrying no $\tfrac12$ because the central-valued field is complex and its quadratic form is the bilinear $\eta^\dagger(\Box-\mu^2)\eta$ — the same complex-versus-real counting that the finite-dimensional Gaussian below exhibits. For the free theory the fluctuation integral is Gaussian and the dependence on the background drops out of the determinant, so the free kernel is **exact**, not merely semiclassical; the one-dimensional model of this statement is the free-particle kernel $K=\sqrt{m/(2\pi i\hbar T)}\,\exp(im\Delta x^2/2\hbar T)$, which the path integral reproduces exactly, and the standard reference for the construction is the path-integral literature. In the interacting theory the determinant depends on the background and the semiclassical expansion becomes the loop expansion treated below.

## The Generating Functional and the Free Gaussian

A source is added to make the correlation functions the derivatives of a single functional. With a central-valued source $\tilde J=J\,e_0$, and with both source terms present because the complex field and its conjugate are independent,

$$
Z[\tilde J]=\int\mathcal{D}\tilde{\Phi}\;\exp\left(iS[\tilde{\Phi}]
+i\int d^4x\left[\mathrm{Sc}\!\left(\tilde J^\dagger\tilde{\Phi}\right)+\mathrm{Sc}\!\left(\tilde{\Phi}^\dagger\tilde J\right)\right]\right),
$$

and the time-ordered correlation functions of the quantized field are its functional derivatives,

$$
\langle0|T\,\hat{\phi}(x_1)\cdots\hat{\phi}(x_n)\,\hat{\phi}^\dagger(y_1)\cdots\hat{\phi}^\dagger(y_m)|0\rangle
=\frac{1}{Z[0]}\left(\frac{1}{i}\right)^{n+m}
\frac{\delta^{\,n+m}Z[\tilde J]}
{\delta J^*(x_1)\cdots\delta J^*(x_n)\,\delta J(y_1)\cdots\delta J(y_m)}\bigg|_{\tilde J=0}.
$$

This is the equivalence that the next section examines; here the free case is evaluated.

**The free Gaussian.** The free action is quadratic, and the functional integral is the formal limit of the finite-dimensional Gaussian identity. On a lattice of $N$ sites with a real symmetric positive-definite quadratic form $A$,

$$
Z_N(J)=\int\prod_{i=1}^{N}d\phi_i\;
\exp\!\left(-\frac{1}{2}\phi^{T}A\phi+J^{T}\phi\right)
=(2\pi)^{N/2}(\det A)^{-1/2}\exp\!\left(\frac{1}{2}J^{T}A^{-1}J\right),
$$

and the two-point function is the inverse of the quadratic form. For the complex configuration space of the central-valued field the same identity has the source bilinear in $J^*$ and $J$ with no $\tfrac12$,

$$
Z_N\;\propto\;(\det A)^{-1}\exp\!\left(J^*\!A^{-1}J\right),
$$

and the two-point function is again $A^{-1}$; the factor of two in the real-versus-complex counting is exactly the counting that the central-valued field's single complex component supplies. The verification below is performed in the real form, where the closed result is the one quoted. In the continuum the completion of the square gives

$$
Z[\tilde J]=Z[0]\exp\!\left(-\int d^4x\,d^4y\;J^*(x)\,\Delta_F(x-y)\,J(y)\right),
$$

where $\Delta_F$ is the Feynman propagator of the companion article *The Quantized Scalar Field in Biquaternionic Form*, the Green's function of $(\Box-\mu^2)$ with the $i\epsilon$ prescription that makes the Gaussian converge. In material notation $\Delta_F(\tilde{K})=-i/(N(\tilde{K})+\mu^2-i\epsilon)$, so the pole of the free two-point function is the mass-shell level set of the norm form. The exponent carries no explicit $i$ because the complex field's bilinear pairs $J^*$ with $J$ and because $\Delta_F$ itself carries the $i$; in the real-field convention the same identity reads $\exp(\frac{i}{2}\int J\,G\,J)$ with $G=i\Delta_F$, the two forms differing only by the overall normalisation of the field. Two functional derivatives return the propagator itself,

$$
\langle0|T\,\hat{\phi}(x)\hat{\phi}^\dagger(y)|0\rangle
=\left(\frac{1}{i}\right)^{\!2}
\frac{\delta^{2}Z[\tilde J]}{\delta J^*(x)\,\delta J(y)}\bigg|_{\tilde J=0}
=\Delta_F(x-y),
$$

which is the two-point function of the companion field article; the inverse-of-the-quadratic-form statement is the one verified on the lattice below, where $AA^{-1}$ differed from the identity by $5.6\times10^{-16}$.

**Verification.** The Gaussian identity was checked by direct two-dimensional quadrature against the closed form. For $A=\begin{pmatrix}1.7&0.4\\0.4&1.1\end{pmatrix}$ and $J=(0.3,-0.8)$, the quadrature gave $7.191118733737$ and the closed formula gave $7.191118733744$, a relative difference of $9.7\times10^{-13}$, the discretization error of the sum. For a four-site lattice Klein–Gordon form with spacing $h=0.25$ and $\mu=0.7$, the product $AA^{-1}$ differed from the identity by at most $5.6\times10^{-16}$. The identity of the Gaussian two-point function with the inverse of the quadratic form is the path-integral proof that the free propagator is the Green's function of the field operator; on the lattice the two constructions agree by construction once the quadratic form is identified with the operator.

## Equivalence with the Operator Formalism

The path integral and the canonical quantization are two representations of one theory, and the dictionary between them is worth displaying because the framework's central structure appears on both sides.

**The canonical commutator.** On functionals of the configuration, the momentum is represented by

$$
\hat{\pi}(\mathbf{x})=-i\hbar\,\frac{\delta}{\delta\phi(\mathbf{x})},
$$

so that

$$
\big[\hat{\phi}(\mathbf{x}),\hat{\pi}(\mathbf{y})\big]
=-i\hbar\left[\phi(\mathbf{x}),\frac{\delta}{\delta\phi(\mathbf{y})}\right]
=i\hbar\,\delta^{(3)}(\mathbf{x}-\mathbf{y}),
$$

which is the equal-time commutator imposed in the companion quantization. The commutator is thus not extra input: it is the statement $\delta\phi(\mathbf x)/\delta\phi(\mathbf y)=\delta^{(3)}$ in the functional representation. The conjugate momentum is the derivative of the action, $\pi=\delta S/\delta\dot{\phi}$ on shell, matching the classical Legendre transform.

**The mode expansion and the correlators.** The Gaussian integration produces the Wightman and Feynman functions of the companion field article, and the standard free-field Wick expansion recovers the mode algebra from them. The Hamiltonian and the charge are the generators of the time and phase translations, and their matrix elements are reproduced by the functional integral with the appropriate insertions. The equivalence is the standard one and is not re-derived; what the framework changes is the notation.

**Why the paths are c-numbers.** The functional integral integrates over **classical configurations**, not over operators, and this is legitimate for a bosonic field precisely because the field operators commute at spacelike separation: the configuration space is a set of c-number functions, and the weight is a c-number phase. For a fermionic field the same construction requires anticommuting (Grassmann) values, because the field operators anticommute; the scalar sector's functional integral is therefore an ordinary integral over complex functions, and this is the path-integral face of the spin–statistics connection. The central-valuedness of the scalar field is what makes its configuration space the space of complex functions; the state module does not enter the integral.

**Ordering.** The Lagrangian functional integral computes time-ordered correlation functions of the field, with the ordering fixed by the convention that the momentum is inserted to the right of the coordinate at coincident times; different operator orderings differ by contact terms that the measure's regularization controls. This is standard and is the same ambiguity the companion articles record for the normal-ordering constant.

## The Euclidean Formulation and the Lattice Determinant

The functional integral is made convergent by continuing to imaginary time. Writing $t=-i\tau$, so that the material coordinate's time component becomes the real coefficient $c\tau$ and the phase becomes a decaying weight, the action continues to the **Euclidean action**

$$
S_E[\tilde{\Phi}]=\int d^4x_E\left[(\partial_\tau\phi^*)(\partial_\tau\phi)
+\sum_k(\partial_k\phi^*)(\partial_k\phi)+\mu^2\phi^*\phi\right]
=\int d^4x_E\;\mathrm{Sc}\!\left[\tilde{\Phi}^\dagger(-\Delta_E+\mu^2)\tilde{\Phi}\right],
$$

with $\Delta_E=\partial_\tau^2+\Delta$ the Euclidean Laplacian, and the functional integral becomes

$$
Z_E=\int\mathcal{D}\tilde{\Phi}\;e^{-S_E[\tilde{\Phi}]/\hbar},
$$

a sum of positive weights. The step from the material coordinate $\tilde{X}=ict\,e_0+\mathbf{x}\in\mathbb{M}_-$ to its Euclidean form is the replacement of the imaginary time coefficient by a real one, i.e. the passage to the quaternion subspace on which the norm form is positive definite; this is the framework's reading of the Wick rotation, and it is the reason the Euclidean Gaussian converges. The action is central, the weight is positive and central, and the configuration space is unchanged.

**The lattice regulator.** Discretizing the Euclidean direction on a lattice of spacing $h$, the quadratic form of one degree of freedom is a tridiagonal matrix with diagonal $a=2/h^2+\mu^2$ and off-diagonal $b=-1/h^2$, and its determinant obeys the recursion

$$
D_n=a\,D_{n-1}-b^2D_{n-2},
\qquad
D_0=1,\quad D_1=a ,
$$

which follows from expanding along the first row. The inverse $A^{-1}$ is the lattice propagator, and in the continuum limit $h\to0$ the matrix $(-\Delta_E+\mu^2)^{-1}$ becomes the Euclidean two-point function. This is the standard lattice definition of a scalar functional integral, and it is the definition that gives the measure a meaning.

**Verification.** For $\mu=0.7$ and $h=0.25$ the four-site lattice matrix satisfied $AA^{-1}=\mathbf{1}$ to $5.6\times10^{-16}$, and for the lattices $(n,h,\mu)=(4,0.25,0.7)$ and $(6,0.3,0.9)$ the determinant recursion agreed with direct Gaussian elimination to fifteen significant figures. The determinant is positive, as the Euclidean quadratic form's positivity requires, and the finite-dimensional Gaussian identity of the previous section applies with $A$ the lattice form.

**The continuum limit and the free energy.** In the limit the functional integral defines $\ln Z_E$, whose per-volume limit is the free energy density of the Euclidean scalar theory; the determinant $\det(-\Delta_E+\mu^2)$ is central, as every object of the scalar sector is, and its logarithm is the one-loop vacuum energy. The divergent part of that logarithm is the Euclidean form of the vacuum energy that the companion quantization's normal ordering removes, and its finite part is the quantity the Casimir companion computes for boundary conditions. The Euclidean formulation adds no new framework content; it makes the measure and the determinant well defined and puts the vacuum energy on the same footing as the propagator.

## The Vacuum Persistence Amplitude and Pair Creation

The functional integral makes the vacuum amplitude an integral over configurations and connects directly to the external-background process of the companion article *Scalar Pair Creation in Biquaternionic Form*. A background that couples through the invariant produces an effective action in which the mass is spacetime-dependent,

$$
Z[\tilde\sigma]=\int\mathcal{D}\tilde{\Phi}\;\exp\left(iS[\tilde{\Phi}]
-i g\int d^4x\,\mathrm{Sc}\!\left(\tilde{\Phi}^\dagger\tilde{\Phi}\right)\sigma\right),
$$

and the **vacuum persistence amplitude** in the background is

$$
\big|\langle0_{\mathrm{out}}|0_{\mathrm{in}}\rangle\big|^2
=\frac{|Z[\tilde\sigma]|^2}{|Z[0]|^2}.
$$

For a homogeneous background with a slow or sudden time dependence, the Gaussian in a time-dependent frequency gives the same two-mode squeezed state and the same coefficients as the mode-matching computation of the companion article, and the probability of pair creation is $1-|\langle0_{\mathrm{out}}|0_{\mathrm{in}}\rangle|^2$. The general connection between the imaginary part of the effective action and the pair-creation rate is standard: $\Im\ln Z$ measures the failure of the vacuum to persist. The Gaussian evaluation above is the free case; the background makes the quadratic form time-dependent and the same functional determinant produces the persistence amplitude. The three formulations therefore agree on the process: canonical quantization through the Bogoliubov coefficients, the path integral through the vacuum functional.

This is also the point at which the path integral's determinant is visible. The free determinant $[\det(\Box-\mu^2)]^{-1}$ is a central scalar — the inverse power is the complex field's, as in the finite-dimensional identity above; in a background it becomes the central functional determinant whose modulus produces the persistence amplitude. Whether the framework singles out a regularization of that determinant is open, exactly as for the vacuum energy.

## Interactions and the Loop Expansion

The scalar sector's interaction is a central self-coupling. The renormalizable $U(1)$-symmetric interaction is the square of the invariant,

$$
\mathcal{L}_{\mathrm{int}}=-\frac{\lambda}{4}\,\Big(\mathrm{Sc}\!\left(\tilde{\Phi}^\dagger\tilde{\Phi}\right)\Big)^2
=-\frac{\lambda}{16}\left(\phi_1^2+\phi_2^2\right)^2 ,
$$

where the second form uses the component normalization stated above, $\mathrm{Sc}(\tilde{\Phi}^\dagger\tilde{\Phi})=\frac12(\phi_1^2+\phi_2^2)$, and the potential is a central scalar polynomial. The generating functional becomes

$$
Z[\tilde J]=\exp\!\left[-i\int d^4x\;\frac{\lambda}{4}\left(\frac{\delta}{i\,\delta J^*}\frac{\delta}{i\,\delta J}\right)^{\!2}\right]Z_0[\tilde J],
$$

whose expansion in powers of $\lambda$ is the standard perturbative series, and in which the coupling normalisation is the same as that of the companion breaking article's potential, so that the radial curvature there is $\lambda v^2$. The Feynman rules follow from the two ingredients already established: the **propagator** is the inverse of the quadratic form, $\Delta_F(\tilde{K})=-i/(N(\tilde{K})+\mu^2-i\epsilon)$, and the **vertex** is $-i\lambda$ times a central unit in the normalisation $-\frac{\lambda}{4!}(\phi_1^2+\phi_2^2)^2$, equivalently $-\frac{3}{2}i\lambda$ in the invariant's normalisation $-\frac{\lambda}{16}(\phi_1^2+\phi_2^2)^2$ written above — the $4!$ of the four equivalent field factors and the factor from the invariant's double counting are the whole of the difference. Every internal line and every vertex is central; no spinor index, no matrix, and no representation label enters any diagram of the scalar sector. This is the diagrammatic form of the centrality that the whole article records.

Two structural comments complete the picture.

**The loop expansion is the expansion in $\hbar$.** Restoring $\hbar$, the weight is $e^{iS/\hbar}$, the propagator carries a factor $\hbar$, and a diagram with $L$ loops carries $\hbar^{L-1}$; the semiclassical expansion of the previous section is thus the loop expansion, and the effective action $\Gamma[\phi]$, the Legendre transform of $W=\ln Z$, is the generating functional of the one-particle-irreducible vertices. The general theory of the effective action, of its renormalization and of its convexity belongs to the companion article *The Generating Functional and the Effective Action in Biquaternionic Form* and is not derived here; what is specific to the scalar sector is that every term is a central scalar functional.

**The bosonic gap persists diagrammatically.** The perturbative expansion is an expansion of the functional integral on the imported module; the mode algebra is the standard CCR algebra, and the algebra $\mathbb{B}$ contributes only the central-valuedness of the fields, sources, propagators and vertices. There is no diagrammatic object native to $\mathbb{B}$; the trace argument that forbids a bosonic mode in the algebra forbids equally any attempt to read the diagrammatic expansion as an algebraic identity inside it.

**Renormalization.** The divergences of the loop expansion — the vacuum energy, the tadpole, the mass and the coupling — are controlled by the standard counterterms, which are themselves central scalars; the coupling's flow and the renormalization-scale dependence are the generalities of the method. Whether the framework's trace or norm form fixes a preferred normalization of the counterterms is open, as recorded below.

## The Biquaternion Reading

Four statements summarise what the framework contributes to the scalar functional integral.

**The configuration space is the center.** The configuration space of the theory is the space of central-valued functions; the action, the source and the measure are central; the state module is a spectator. This is why the scalar functional integral is an ordinary complex functional integral and why no Grassmann or spinor structure appears.

**The quadratic form is the norm form.** The momentum-space symbol of the Gaussian's operator is $-(N(\tilde{K})+\mu^2)$ with $N(\tilde{K})=\tilde{K}\bar{\tilde{K}}$, and it vanishes on the mass shell, the level set $N(\tilde{K})=-\mu^2$. The shell's geometry, the Gaussian's width and the pole of the propagator are three readings of one algebraic object, and the framework's convention for $\Box$ makes them mutually consistent.

**The phase is central, and the Wick rotation is a sector relabelling.** The phase $e^{iS/\hbar}$ is a central unitary, so it multiplies the whole configuration space uniformly. The continuation to imaginary time is the relabelling of the material coordinate $\tilde{X}=ict\,e_0+\mathbf{x}\in\mathbb{M}_-$ by the real coefficient $c\tau$, which is the passage to the quaternion subspace on which the norm form is positive definite; this is the standard Wick rotation read as a change of sector, and it is what makes the Euclidean Gaussian converge.

**The algebra supplies nothing beyond the center.** There is no bosonic ladder in $\mathbb{B}$, as the companion Fock-space article's trace argument shows, so the mode expansion, the Fock space and the perturbative expansion that the path integral organises are all constructed on an imported module. The functional integral's algebraic content is exhausted by the centrality of the field and the norm-form geometry of the quadratic form.

## What Is Standard and What Is Open

**Standard, and imported.** The field-eigenvalue basis, the time-slicing derivation of the functional integral, the phase-space and Lagrangian forms, and the measure; the generating functional and the functional-derivative formula for the correlation functions; the finite-dimensional Gaussian identity and the completion of the square; the free two-point function as the inverse quadratic form and the Feynman propagator; the representation of the canonical commutator by $-i\hbar\delta/\delta\phi$; the Euclidean continuation, the lattice regulator and the determinant recursion; the vacuum persistence amplitude, the functional determinant and the relation of its imaginary part to pair creation; the quartic interaction, the Feynman rules with the propagator as the inverse quadratic form, and the loop expansion as the expansion in $\hbar$. None of this is re-derived here, and none of it depends on the biquaternion structure beyond the kinematical conventions.

**Open in the biquaternion framework.**

- **The measure.** The functional measure is defined as the formal limit of the lattice Lebesgue measure. Whether the framework supplies a canonical measure from its own structure — the trace form, the norm form, or the real structure — rather than inheriting the Lebesgue measure, is not settled. This is the same open question the companion article *The Path Integral in Biquaternionic Form* records for the one-particle functional integral.
- **The intrinsic generating functional.** Whether the generating functional should be defined with the trace pairing $\mathrm{Tr}$ or the scalar projection $\mathrm{Sc}$, and whether the choice affects the contact terms, is a convention the algebra does not force.
- **The functional determinant and its phase.** The determinant is central, but its phase requires a regularization and a choice of branch. Whether the framework's complex structure fixes the branch, or whether the standard $i\epsilon$ prescription is the only input, is open.
- **Interactions.** A central quartic coupling preserves the centrality of every object. Whether the trace form suggests a preferred normalization of the coupling is not shown; the perturbative expansion is standard once the coupling is fixed.
- **The bosonic gap.** The path integral's variables are c-numbers, which is what makes the bosonic theory an ordinary integral; the scalar sector has no native ladder in $\mathbb{B}$, so the algebraic content remains the center. Whether an enlarged structure supplements this is the structural question of the whole scalar sector.
- **Empirical content.** Whether the functional integral as written yields a prediction distinguishing the framework from standard scalar field theory is open.

## Summary

The scalar functional integral is the sum over central-valued configurations weighted by the central phase $e^{iS/\hbar}$, with the action $S[\tilde{\Phi}]=\int d^4x\,[-\mathrm{Sc}((\bar{\tilde{\nabla}}\tilde{\Phi}^\dagger)(\tilde{\nabla}\tilde{\Phi}))-\mu^2\mathrm{Sc}(\tilde{\Phi}^\dagger\tilde{\Phi})]$. It is derived from the operator formalism by inserting the field-eigenvalue basis at each time, and it is an ordinary functional integral over complex functions because the scalar field is bosonic and its configurations are c-numbers. Its quadratic form has the momentum-space symbol $-(N(\tilde{K})+\mu^2)$, the norm form of the material four-wavevector shifted by the mass, so the mass shell $N(\tilde{K})=-\mu^2$, the Gaussian's width and the propagator's pole are one object.

The generating functional $Z[\tilde J]$ has for its functional derivatives the time-ordered correlation functions of the field operator, and its free value is the Gaussian $Z[0]\exp(-\int J^*\Delta_F J)$ with $\Delta_F$ the Feynman propagator; the finite-dimensional Gaussian identity was verified by quadrature to a relative difference of $9.7\times10^{-13}$, and the lattice Klein–Gordon inverse to $5.6\times10^{-16}$. The canonical commutator is recovered from the representation $\hat\pi=-i\hbar\delta/\delta\phi$, and the mode expansion and correlators follow. The vacuum persistence amplitude $|\langle0_{\mathrm{out}}|0_{\mathrm{in}}\rangle|^2=|Z[\tilde\sigma]|^2/|Z[0]|^2$ in a background is the functional-integral form of the pair-creation probability, and it agrees with the Bogoliubov computation of the companion pair-creation article; its imaginary part measures the failure of the vacuum to persist.

The framework's contribution is the centrality of the configuration space, the norm-form reading of the quadratic form, and the identification of the Wick rotation with the passage to the quaternion subspace. The measure, the determinant's branch and the intrinsic generating functional remain open, and the bosonic gap — no native ladder in $\mathbb{B}$ — persists, as it does throughout the scalar sector.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Central scalar imaginary |
| $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_0,ie_0\}$ | Center; the configuration space's value space |
| $\tilde{\Phi}=\phi\,e_0$, $\tilde J=J\,e_0$, $\phi=(\phi_1+i\phi_2)/\sqrt2$ | Scalar field and central source; real components |
| $\tilde{X}=ict\,e_0+\mathbf{x}$ | Material coordinate |
| $\tilde{\nabla}=e_0\partial_{ict}+\sum_k e_k\partial_k$, $\Box=\partial_{ict}^2+\Delta$ | Gradient and d'Alembertian |
| $S[\tilde{\Phi}]$ | Central scalar action |
| $Z[\tilde J]=\int\mathcal{D}\tilde{\Phi}\,e^{\,iS+i\int[\mathrm{Sc}(\tilde J^\dagger\tilde{\Phi})+\mathrm{Sc}(\tilde{\Phi}^\dagger\tilde J)]}$ | Generating functional |
| $\mathcal{D}\tilde{\Phi}$ | Functional measure on central-valued configurations |
| $\delta^{n+m}Z/\delta J^{*n}\delta J^{m}$ | Functional derivatives = time-ordered correlators |
| $Z_N(J)=(2\pi)^{N/2}(\det A)^{-1/2}e^{J^{T}A^{-1}J/2}$, $Z_N\propto(\det A)^{-1}e^{J^*A^{-1}J}$ | Finite-dimensional Gaussian identity, real and complex |
| $\Delta_F$ | Feynman propagator; free two-point function |
| $\Delta_F(\tilde{K})=-i/(N(\tilde{K})+\mu^2-i\epsilon)$ | Propagator in material notation |
| $\tilde{K}=i\omega/c\,e_0+\mathbf{k}$, $N(\tilde{K})=\tilde{K}\bar{\tilde{K}}$ | Material four-wavevector and norm form |
| $\hat\pi=-i\hbar\,\delta/\delta\phi$ | Momentum representation; yields $[\hat\phi,\hat\pi]=i\hbar\delta^{(3)}$ |
| $S_E[\tilde\Phi]=\int\mathrm{Sc}(\tilde\Phi^\dagger(-\Delta_E+\mu^2)\tilde\Phi)$ | Euclidean action (Wick rotation) |
| $\vert\langle0_{\mathrm{out}}\vert0_{\mathrm{in}}\rangle\vert^2=\vert Z[\tilde\sigma]\vert^2/\vert Z[0]\vert^2$ | Vacuum persistence amplitude |
| $\mathrm{Tr}(e_0)=2$, $\mathrm{Tr}[\tilde A,\tilde B]=0$ | Trace identity; no bosonic mode in $\mathbb{B}$ |

## Further Reading

- R. P. Feynman, "Space-time approach to non-relativistic quantum mechanics," *Reviews of Modern Physics* **20** (1948) 367–387, for the original sum over histories.
- R. P. Feynman and A. R. Hibbs, *Quantum Mechanics and Path Integrals* (McGraw-Hill, 1965), for the time-slicing construction of the kernel and the semiclassical expansion.
- J. Glimm and A. Jaffe, *Quantum Physics: A Functional Integral Point of View* (Springer, 1987), for the constructive definition of scalar functional integrals and the role of the lattice regulator.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the functional integral for scalar fields, the generating functional, and the Gaussian evaluation.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the free generating functional, the two-point function as the inverse quadratic form, and the Wick rotation.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the loop expansion, the functional determinant, and the effective action.
- L. S. Brown, *Quantum Field Theory* (Cambridge, 1992), for the relation between the imaginary part of the effective action and pair creation.
- M. Reed and B. Simon, *Methods of Modern Mathematical Physics, Vol. II: Fourier Analysis, Self-Adjointness* (Academic Press, 1975), for Gaussian measures on function spaces and positive-definiteness conditions.
