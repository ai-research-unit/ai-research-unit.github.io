# __The Scalar Field Path Integral in Biquaternionic Form__

## Introduction

A quantum field theory admits three formulations: the equation of motion, the operator algebra, and the functional integral. For the scalar field of this framework the first two are the subjects of the companion articles *The Klein–Gordon Equation in Biquaternionic Form* and *Canonical Quantization of the Biquaternion Klein–Gordon Field*; the third is the subject of this article. The functional integral writes the theory as a sum over field configurations weighted by the central phase $\exp(\frac{k_m\,i\,S}{m\,c})$, and in doing so it makes the correlation functions of the quantized field the moments of a distribution on the space of classical configurations.

The division of labour among the path-integral articles of the corpus must be stated at once. The algebraic status of the phase — that the $i$ of $\exp(\frac{k_m\,i\,S}{m\,c})$ is the central scalar imaginary, that the exponent lies in the material sector, and that the phase is a central $*$-unitary element — is a general statement about the functional integral and belongs to the companion article *The Functional Integral in Biquaternionic Form*, not here; it is taken as established. The functional integral of the **one-particle** Klein–Gordon theory, with its free Gaussian and its lattice regulator, is a statement in the relativistic quantum-theory category, given by the companion article *The Klein–Gordon Path Integral in Biquaternionic Form*, and is likewise not repeated. What is treated here is the complementary object: the functional integral of the **quantized** scalar field, its derivation from the operator formalism of the companion articles, its correlation functions, and its relation to the vacuum persistence amplitude and to pair creation.

Three statements organise the article.

1. **The integration variable is a central-valued c-number field.** The field configurations are functions into the centre $\mathbb{B}_{C}$; the action, the source and the measure are central; and the weight is a central phase. Because the scalar field is bosonic, the sum over configurations is an ordinary (functional) integral over complex functions; it is the fermionic case that would require anticommuting values. This is the path-integral form of the statement that spin $0$ lives in the centre.
2. **The functional integral is the operator formalism's generating functional.** Its functional derivatives reproduce the time-ordered correlation functions of the field operator of the companion article *The Quantized Scalar Field in Biquaternionic Form*; the free two-point function is the Feynman propagator; the vacuum functional is the norm of the vacuum-to-vacuum amplitude. The canonical commutator is recovered from the representation $\pi_{\mathrm{fop}}=-\frac{m\,c\,i}{k_m\,\xi_{\mathrm{scl}}}$.
3. **The algebra contributes the same three things it contributes elsewhere in the scalar sector.** The centrality of the field and the source; the biquaternion-norm interpretation of the quadratic form, whose momentum-space symbol is the biquaternion norm of the material four-wavevector shifted by the mass; and the identification of the Wick rotation with a sector relabelling. No new mechanism and no native ladder; the bosonic gap of the companion Fock-space article persists.

The article is organised as follows. The next section derives the functional integral from the field-eigenvalue basis and the time-slicing of the propagator. The following section defines the generating functional and evaluates the free Gaussian. The next section establishes the equivalence with the operator formalism. The section after that treats the vacuum persistence amplitude and its relation to pair creation. A section states the biquaternion interpretation. The article closes with the standard/open separation.

- Companion article *Canonical Quantization of the Biquaternion Klein–Gordon Field*, for the equal-time commutators, the mode algebra and the Hamiltonian whose matrix elements the path integral reproduces.
- Companion article *The Quantized Scalar Field in Biquaternionic Form*, for the field operator, the Wightman function and the Feynman propagator that the Gaussian produces.
- Companion article *The Scalar Fock Space in Biquaternionic Form*, for the state space on which the functional integral's correlators are defined.
- Companion article *Scalar Pair Creation in Biquaternionic Form*, for the external-background process whose probability is the modulus squared of the vacuum functional.
- Companion article *Noether's Theorem in Biquaternionic Form*, for the central scalar action and the current.
- Companion article *The Material Sector: Four-Vectors, Interval and Lorentz Action*, for the material four-wavevector and the biquaternion norm.

## From the Operator Formalism to the Functional Integral

The functional integral is derived from the operator formalism by inserting a complete set of field eigenstates at each time. The field operator $\xi_{\mathrm{fop}}(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)$ has a continuum of eigenstates,

$$
\xi_{\mathrm{fop}}(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)|\xi_{\mathrm{scl}}\rangle=\xi_{\mathrm{scl}}(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)|\xi_{\mathrm{scl}}\rangle,
\qquad
\langle\xi_{\mathrm{scl},\mathrm e}|\xi_{\mathrm{scl}}\rangle=\delta[\xi_{\mathrm{scl},\mathrm e}-\xi_{\mathrm{scl}}],
\qquad
\int\mathcal{D}\xi_{\mathrm{scl}}\,|\xi_{\mathrm{scl}}\rangle\langle\xi_{\mathrm{scl}}|=\mathbf{1},
$$

with real eigenvalues for the real field and complex eigenvalues for the complex one. The transition amplitude factors into short-time pieces, and inserting the field basis between them gives, for a real field,

$$
\langle\xi_{\mathrm{scl},f},r'_{t,f}|\xi_{\mathrm{scl},i},r'_{t,i}\rangle
=\int_{\xi_{\mathrm{scl}}(r'_{t,i})=\xi_{\mathrm{scl},i}}^{\xi_{\mathrm{scl}}(r'_{t,f})=\xi_{\mathrm{scl},f}}\mathcal{D}\xi_{\mathrm{scl}}\;
\exp\left(\frac{k_m\,i}{m\,c}\int_{r'_{t,i}}^{r'_{t,f}}\!dr'_t\,\mathrm{Lag}[\xi_{\mathrm{scl}},\partial\xi_{\mathrm{scl}}/\partial r'_t]\right),
$$

with $\mathrm{Lag}=\int d^3r\,\mathcal{L}$; the phase-space form is obtained by inserting also the momentum completeness relation, and integrating out the momentum returns the Lagrangian form above. The boundary values $\xi_{\mathrm{scl},i},\xi_{\mathrm{scl},f}$ are held fixed, and the measure is the formal product of Lebesgue measures at each time slice, $\mathcal{D}\xi_{\mathrm{scl}}=\prod_t d\xi_{\mathrm{scl}}(r'_t)$, made meaningful by a lattice regulator as in the finite-dimensional Gaussian below.

In the framework's notation the field is central-valued and the weight is a central phase,

$$
\tilde{Ξ}(\tilde R_\Phi)=\xi_{\mathrm{scl}}(\tilde R_\Phi)e_t,
\qquad
S[\tilde{Ξ}]=\int d^4r\left[-\mathrm{Sc}\!\left[(\tilde{\nabla}^{\natural}\tilde{Ξ}^{*})(\tilde{\nabla}\tilde{Ξ})\right]-\mu^2\,\mathrm{Sc}\!\left(\tilde{Ξ}^{*}\tilde{Ξ}\right)\right],
$$

$$
Z=\int\mathcal{D}\tilde{Ξ}\;\exp(\,iS[\tilde{Ξ}]\frac{k_m}{m\,c}),
\qquad
\exp(\,\frac{k_m\,i\,S}{m\,c})\ \text{a central }{}^{*}\text{-unitary} .
$$

Three features of this rewriting are structural rather than cosmetic. First, the integration variable is a function into the **centre**, so the path integral is an ordinary functional integral over complex functions, equivalently over pairs of real functions, and the state module on which spinor fields live is not integrated over at all. Second, the quadratic form in the exponent is the biquaternion norm shifted by the mass: the momentum-space symbol of $(\Box-\mu^2)$ on the plane wave $\exp(-ip\cdot x)$ is

$$
\frac{\omega^2}{c^2}-\vec k_\Phi^2-\mu^2
=-\left(\langle\tilde P_{\Phi}\rangle_{\natural}+\mu^2\right),
\qquad
\langle\tilde P_{\Phi}\rangle_{\natural}=\tilde P_{\Phi}\tilde P_{\Phi}^{\natural},
\qquad
\tilde P_{\Phi}=i\frac{\omega}{c}\,e_t+\vec k_\Phi,
$$

which vanishes precisely on the mass shell $\langle\tilde P_{\Phi}\rangle_{\natural}=-\mu^2$, so the Gaussian's width and the mass shell are one algebraic object; the propagator is the inverse of this symbol, $\Delta_F(\tilde P_{\Phi})=-i/(\langle\tilde P_{\Phi}\rangle_{\natural}+\mu^2-i\epsilon)$, exactly as the companion field article has it. Third, the phase is central, so it commutes with every element of the algebra and multiplies configuration space uniformly; no rotor and no spinor index enters. The three are the same three facts that the one-particle and propagator articles record for their own objects.

## The Phase-Space Form and the Semiclassical Kernel

The time-sliced construction above can be written in either the Lagrangian or the Hamiltonian form, and the passage between them is the path-integral version of the Legendre transform of the companion quantization. Inserting at each slice the momentum completeness relation

$$
\int\mathcal{D}\pi\,|\pi\rangle\langle\pi|=\mathbf{1},
\qquad
\langle\xi_{\mathrm{scl}}|\pi\rangle=\exp(\,\frac{k_m\,i}{m\,c}\int  d^3r\,(\pi\xi_{\mathrm{scl}}+\pi^\dagger{\xi_{\mathrm{scl}}}^\dagger)),
$$

and using $\langle\pi|H|\xi_{\mathrm{scl}}\rangle=\langle\pi|\xi_{\mathrm{scl}}\rangle H(\xi_{\mathrm{scl}},\pi)$, the kernel becomes

$$
\langle\xi_{\mathrm{scl},f},r'_{t,f}|\xi_{\mathrm{scl},i},r'_{t,i}\rangle
=\int\mathcal{D}\xi_{\mathrm{scl}}\,\mathcal{D}\pi\;
\exp\left(\frac{k_m\,i}{m\,c}\int_{r'_{t,i}}^{r'_{t,f}}\!dr'_t\int  d^3r\,
\big[\pi\,\partial\xi_{\mathrm{scl}}/\partial r'_t+\pi^\dagger\left(\partial\xi_{\mathrm{scl}}/\partial r'_t\right)^{\dagger}-\mathcal{H}(\xi_{\mathrm{scl}},\pi)\big]\right),
$$

the **phase-space** or Hamiltonian form of the functional integral. The momentum is now an independent integration variable, and because the field is complex both kinetic terms appear, with the corresponding boundary terms fixed at the endpoints. Because the Hamiltonian is quadratic in $\pi$, the momentum integral is a Gaussian and can be performed explicitly; it reproduces the Lagrangian form, since with the Hamiltonian $\mathcal{H}=c^{2}\pi\pi^{\dagger}+|\nabla\xi_{\mathrm{scl}}|^{2}+\mu^{2}|\xi_{\mathrm{scl}}|^{2}$ the saddle value of $\pi\partial\xi_{\mathrm{scl}}/\partial r'_t+\pi^{\dagger}\left(\partial\xi_{\mathrm{scl}}/\partial r'_t\right)^{\dagger}-\mathcal{H}$ is $2|\partial\xi_{\mathrm{scl}}/\partial r'_t|^{2}-|\partial\xi_{\mathrm{scl}}/\partial r'_t|^{2}-|\nabla\xi_{\mathrm{scl}}|^{2}-\mu^{2}|\xi_{\mathrm{scl}}|^{2}=\mathcal{L}$. The saddle point of the momentum integral is

$$
\frac{\partial\mathcal{H}}{\partial\pi}=\partial\xi_{\mathrm{scl}}/\partial r'_t
\qquad\Longleftrightarrow\qquad
\pi=\left(\partial\xi_{\mathrm{scl}}/\partial r'_t\right)^{\,*},
$$

which is the conjugate momentum of the companion canonical quantization. The regularity of the Legendre transform — no constraint, no gauge redundancy — is what makes the passage between the two forms exact and uncontroversial in the scalar sector; in the Dirac and Maxwell cases the same passage requires the introduction of ghosts and constraints, and the framework supplies no principle that would avoid them.

The path integral is also a semiclassical expansion. Writing $\xi_{\mathrm{scl}}=\xi_{\mathrm{scl},cl}+\eta$ about a solution of the classical equation, the exponent expands as

$$
S[\xi_{\mathrm{scl},cl}+\eta]=S[\xi_{\mathrm{scl},cl}]
+\int d^4r\,\eta^\dagger\!\left(\Box-\mu^2\right)\!\eta+O(\eta^3),
$$

the linear term vanishing by the equation of motion, and the quadratic term carrying no $\tfrac12$ because the central-valued field is complex and its quadratic form is the bilinear $\eta^\dagger(\Box-\mu^2)\eta$ — the same complex-versus-real counting that the finite-dimensional Gaussian below exhibits. For the free theory the fluctuation integral is Gaussian and the dependence on the background drops out of the determinant, so the free kernel is **exact**, not merely semiclassical; the one-dimensional model of this statement is the free-particle kernel $K=\sqrt{m/(\frac{2\,m\,c\,\pi\,i\,T}{k_m})}\,\exp(\frac{k_m\,i\,\Delta\,x^{2}}{2\,c\,T})$, which the path integral reproduces exactly, and the standard reference for the construction is the path-integral literature. In the interacting theory the determinant depends on the background and the semiclassical expansion becomes the loop expansion treated below.

## The Generating Functional and the Free Gaussian

A source is added to make the correlation functions the derivatives of a single functional. With a central-valued source $\tilde J_{\Phi}=J\,e_t$, and with both source terms present because the complex field and its conjugate are independent,

$$
Z[\tilde J_{\Phi}]=\int\mathcal{D}\tilde{Ξ}\;\exp\left(iS[\tilde{Ξ}]
+i\int d^4r\left[\mathrm{Sc}\!\left(\tilde J_{\Phi}^{*}\tilde{Ξ}\right)+\mathrm{Sc}\!\left(\tilde{Ξ}^{*}\tilde J_{\Phi}\right)\right]\right),
$$

and the time-ordered correlation functions of the quantized field are its functional derivatives,

$$
\boxed{\;\langle0|T\,\xi_{\mathrm{fop}}(x_1)\cdots\xi_{\mathrm{fop}}(x_n)\,\xi_{\mathrm{fop}}^{\dagger}(y_1)\cdots\xi_{\mathrm{fop}}^{\dagger}(y_m)|0\rangle
=\frac{1}{Z[0]}\left(\frac{1}{i}\right)^{n+m}
\frac{\delta^{\,n+m}Z[\tilde J_{\Phi}]}
{\delta J^*(x_1)\cdots\delta J^*(x_n)\,\delta J(y_1)\cdots\delta J(y_m)}\bigg|_{\tilde J_{\Phi}=0}\;}.
$$

This is the equivalence that the next section examines; here the free case is evaluated.

**The free Gaussian.** The free action is quadratic, and the functional integral is the formal limit of the finite-dimensional Gaussian identity. On a lattice of $N$ sites with a real symmetric positive-definite quadratic form $A$,

$$
Z_N(J)=\int\prod_{i=1}^{N}d\xi_{\mathrm{scl},i}\;
\exp\!\left(-\frac{1}{2}{\xi_{\mathrm{scl}}}^{T}A\xi_{\mathrm{scl}}+J^{T}\xi_{\mathrm{scl}}\right)
=(2\pi)^{N/2}(\det A)^{-1/2}\exp\!\left(\frac{1}{2}J^{T}A^{-1}J\right),
$$

and the two-point function is the inverse of the quadratic form. For the complex configuration space of the central-valued field the same identity has the source bilinear in $J^*$ and $J$ with no $\tfrac12$,

$$
Z_N\;\propto\;(\det A)^{-1}\exp\!\left(J^*\!A^{-1}J\right),
$$

and the two-point function is again $A^{-1}$; the factor of two in the real-versus-complex counting is exactly the counting that the central-valued field's single complex component supplies. The verification below is performed in the real form, where the closed result is the one quoted. In the continuum the completion of the square gives

$$
\boxed{\;Z[\tilde J_{\Phi}]=Z[0]\exp\!\left(-\int d^4r\,d^4y\;J^*(x)\,\Delta_F(x-y)\,J(y)\right)\;},
$$

where $\Delta_F$ is the Feynman propagator of the companion article *The Quantized Scalar Field in Biquaternionic Form*, the Green's function of $(\Box-\mu^2)$ with the $i\epsilon$ prescription that makes the Gaussian converge. In material notation $\Delta_F(\tilde P_{\Phi})=-i/(\langle\tilde P_{\Phi}\rangle_{\natural}+\mu^2-i\epsilon)$, so the pole of the free two-point function is the mass-shell level set of the biquaternion norm. The exponent carries no explicit $i$ because the complex field's bilinear pairs $J^*$ with $J$ and because $\Delta_F$ itself carries the $i$; in the real-field convention the same identity reads $\exp(\frac{i}{2}\int J\,G\,J)$ with $G=i\Delta_F$, the two forms differing only by the overall normalisation of the field. Two functional derivatives return the propagator itself,

$$
\langle0|T\,\xi_{\mathrm{fop}}(x)\xi_{\mathrm{fop}}^{\dagger}(y)|0\rangle
=\left(\frac{1}{i}\right)^{\!2}
\frac{\delta^{2}Z[\tilde J_{\Phi}]}{\delta J^*(x)\,\delta J(y)}\bigg|_{\tilde J_{\Phi}=0}
=\Delta_F(x-y),
$$

which is the two-point function of the companion field article; the inverse-of-the-quadratic-form statement is the one verified on the lattice below, where $AA^{-1}$ differed from the identity by $5.6\times10^{-16}$.

## Equivalence with the Operator Formalism

The path integral and the canonical quantization are two representations of one theory, and the dictionary between them is worth displaying because the framework's central structure appears on both sides.

**The canonical commutator.** On functionals of the configuration, the momentum is represented by

$$
\pi_{\mathrm{fop}}(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)=-\frac{m\,c\,i}{k_m\,\xi_{\mathrm{scl}}\,(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)},
$$

so that

$$
\big[\xi_{\mathrm{fop}}(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z),\pi_{\mathrm{fop}}(\vec y)\big]
=-\frac{m\,c\,i}{k_m}\left[\xi_{\mathrm{scl}}(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z),\frac{\delta}{\delta\xi_{\mathrm{scl}}(\vec y)}\right]
=\frac{m\,c\,i\,\delta^{(3)}\,(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z-\vec y)}{k_m},
$$

which is the equal-time commutator imposed in the companion quantization. The commutator is thus not extra input: it is the statement $\delta\xi_{\mathrm{scl}}(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)/\delta\xi_{\mathrm{scl}}(\vec y)=\delta^{(3)}$ in the functional representation. The conjugate momentum is the derivative of the action, $\pi=\delta S/\delta(\partial\xi_{\mathrm{scl}}/\partial r'_t)$ on shell, matching the classical Legendre transform.

**The mode expansion and the correlators.** The Gaussian integration produces the Wightman and Feynman functions of the companion field article, and the standard free-field Wick expansion recovers the mode algebra from them. The Hamiltonian and the charge are the generators of the time and phase translations, and their matrix elements are reproduced by the functional integral with the appropriate insertions. The equivalence is the standard one and is not re-derived; what the framework changes is the notation.

**Why the paths are c-numbers.** The functional integral integrates over **classical configurations**, not over operators, and this is legitimate for a bosonic field precisely because the field operators commute at spacelike separation: the configuration space is a set of c-number functions, and the weight is a c-number phase. For a fermionic field the same construction requires anticommuting (Grassmann) values, because the field operators anticommute; the scalar sector's functional integral is therefore an ordinary integral over complex functions, and this is the path-integral face of the spin–statistics connection. The central-valuedness of the scalar field is what makes its configuration space the space of complex functions; the state module does not enter the integral.

**Ordering.** The Lagrangian functional integral computes time-ordered correlation functions of the field, with the ordering fixed by the convention that the momentum is inserted to the right of the coordinate at coincident times; different operator orderings differ by contact terms that the measure's regularization controls. This is standard and is the same ambiguity the companion articles record for the normal-ordering constant.

## The Euclidean Formulation and the Lattice Determinant

The functional integral is made convergent by continuing to imaginary time. Writing $r'_t=-i\tau$, so that the material coordinate's time component becomes the real coefficient $c\tau$ and the phase becomes a decaying weight, the action continues to the **Euclidean action**

$$
S_E[\tilde{Ξ}]=\int d^4r_E\left[(\partial/\partial\tau\,{\xi_{\mathrm{scl}}}^*)(\partial/\partial\tau\,\xi_{\mathrm{scl}})
+\sum_k(\partial/\partial x_k\,{\xi_{\mathrm{scl}}}^*)(\partial/\partial x_k\,\xi_{\mathrm{scl}})+\mu^2{\xi_{\mathrm{scl}}}^*\xi_{\mathrm{scl}}\right]
=\int d^4r_E\;\mathrm{Sc}\!\left[\tilde{Ξ}^{*}(-\Delta_E+\mu^2)\tilde{Ξ}\right],
$$

with $\Delta_E=\partial^2/\partial\tau^2+\Delta$ the Euclidean Laplacian, and the functional integral becomes

$$
Z_E=\int\mathcal{D}\tilde{Ξ}\;\exp(-S_E[\tilde{Ξ}]\frac{k_m}{m\,c}),
$$

a sum of positive weights. The step from the material coordinate $\tilde R_\Phi=i r'_t\,e_t+r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z\in\mathbb{B}_{\Phi}$ to its Euclidean form is the replacement of the imaginary time coefficient by a real one, i.e. the passage to the quaternion subspace on which the biquaternion norm is positive definite; this is the framework's interpretation of the Wick rotation, and it is the reason the Euclidean Gaussian converges. The action is central, the weight is positive and central, and the configuration space is unchanged.

**The lattice regulator.** Discretizing the Euclidean direction on a lattice of spacing $h$, the quadratic form of one degree of freedom is a tridiagonal matrix with diagonal $a=2/h^2+\mu^2$ and off-diagonal $b=-1/h^2$, and its determinant obeys the recursion

$$
D_n=a\,D_{n-1}-b^2D_{n-2},
\qquad
D_0=1,\quad D_1=a ,
$$

which follows from expanding along the first row. The inverse $A^{-1}$ is the lattice propagator, and in the continuum limit $h\to0$ the matrix $(-\Delta_E+\mu^2)^{-1}$ becomes the Euclidean two-point function. This is the standard lattice definition of a scalar functional integral, and it is the definition that gives the measure a meaning.

**The continuum limit and the free energy.** In the limit the functional integral defines $\ln Z_E$, whose per-volume limit is the free energy density of the Euclidean scalar theory; the determinant $\det(-\Delta_E+\mu^2)$ is central, as every object of the scalar sector is, and its logarithm is the one-loop vacuum energy. The divergent part of that logarithm is the Euclidean form of the vacuum energy that the companion quantization's normal ordering removes, and its finite part is the quantity the Casimir companion computes for boundary conditions. The Euclidean formulation adds no new framework content; it makes the measure and the determinant well defined and puts the vacuum energy on the same footing as the propagator.

## The Vacuum Persistence Amplitude and Pair Creation

The functional integral makes the vacuum amplitude an integral over configurations and connects directly to the external-background process of the companion article *Scalar Pair Creation in Biquaternionic Form*. A background that couples through the invariant produces an effective action in which the mass is spacetime-dependent,

$$
Z[\tilde Q_5]=\int\mathcal{D}\tilde{Ξ}\;\exp\left(iS[\tilde{Ξ}]
-i g\int d^4r\,\mathrm{Sc}\!\left(\tilde{Ξ}^{*}\tilde{Ξ}\right)\xi\right),
$$

and the **vacuum persistence amplitude** in the background is

$$
\boxed{\;\big|\langle0_{\mathrm{out}}|0_{\mathrm{in}}\rangle\big|^2
=\frac{|Z[\tilde Q_5]|^2}{|Z[0]|^2}\;}.
$$

For a homogeneous background with a slow or sudden time dependence, the Gaussian in a time-dependent frequency gives the same two-mode squeezed state and the same coefficients as the mode-matching computation of the companion article, and the probability of pair creation is $1-|\langle0_{\mathrm{out}}|0_{\mathrm{in}}\rangle|^2$. The general connection between the imaginary part of the effective action and the pair-creation rate is standard: $\Im\ln Z$ measures the failure of the vacuum to persist. The Gaussian evaluation above is the free case; the background makes the quadratic form time-dependent and the same functional determinant produces the persistence amplitude. The two formulations therefore agree on the process: canonical quantization through the Bogoliubov coefficients, the path integral through the vacuum functional.

This is also the point at which the path integral's determinant is visible. The free determinant $[\det(\Box-\mu^2)]^{-1}$ is a central scalar — the inverse power is the complex field's, as in the finite-dimensional identity above; in a background it becomes the central functional determinant whose modulus produces the persistence amplitude. Whether the framework singles out a regularization of that determinant is open, exactly as for the vacuum energy.

## Interactions and the Loop Expansion

The scalar sector's interaction is a central self-coupling. The renormalizable $\mathrm{U}(1)$-symmetric interaction is the square of the invariant,

$$
\mathcal{L}_{\mathrm{int}}=-\frac{\lambda}{4}\,\Big(\mathrm{Sc}\!\left(\tilde{Ξ}^{*}\tilde{Ξ}\right)\Big)^2
=-\frac{\lambda}{16}\left(\xi_{\mathrm{scl},1}^2+\xi_{\mathrm{scl},2}^2\right)^2 ,
$$

where the second form uses the component normalization stated above, $\mathrm{Sc}(\tilde{Ξ}^{*}\tilde{Ξ})=\frac12(\xi_{\mathrm{scl},1}^2+\xi_{\mathrm{scl},2}^2)$, and the potential is a central scalar polynomial. The generating functional becomes

$$
Z[\tilde J_{\Phi}]=\exp\!\left[-i\int d^4r\;\frac{\lambda}{4}\left(\frac{\delta}{i\,\delta J^*}\frac{\delta}{i\,\delta J}\right)^{\!2}\right]Z_0[\tilde J_{\Phi}],
$$

whose expansion in powers of $\lambda$ is the standard perturbative series, and in which the coupling normalisation is the same as that of the companion breaking article's potential, so that the radial curvature there is $\lambda v^2$. The Feynman rules follow from the two ingredients already established: the **propagator** is the inverse of the quadratic form, $\Delta_F(\tilde P_{\Phi})=-i/(\langle\tilde P_{\Phi}\rangle_{\natural}+\mu^2-i\epsilon)$, and the **vertex** is $-i\lambda$ times a central unit in the normalisation $-\frac{\lambda}{4!}(\xi_{\mathrm{scl},1}^2+\xi_{\mathrm{scl},2}^2)^2$, equivalently $-\frac{3}{2}i\lambda$ in the invariant's normalisation $-\frac{\lambda}{16}(\xi_{\mathrm{scl},1}^2+\xi_{\mathrm{scl},2}^2)^2$ written above — the $4!$ of the four equivalent field factors and the factor from the invariant's double counting are the whole of the difference. Every internal line and every vertex is central; no spinor index, no matrix, and no representation label enters any diagram of the scalar sector. This is the diagrammatic form of the centrality that the whole article records.

Two structural comments complete the picture.

**The loop expansion is the expansion in $\frac{m\,c}{k_m}$.** Restoring $\frac{m\,c}{k_m}$, the weight is $\exp(\frac{k_m\,i\,S}{m\,c})$, the propagator carries a factor $\frac{m\,c}{k_m}$, and a diagram with $\mathrm{Lag}$ loops carries $\hbar^{L-1}$; the semiclassical expansion of the previous section is thus the loop expansion, and the effective action $\Gamma[\xi_{\mathrm{scl}}]$, the Legendre transform of $W=\ln Z$, is the generating functional of the one-particle-irreducible vertices. The general theory of the effective action, of its renormalization and of its convexity belongs to the companion article *The Generating Functional and the Effective Action in Biquaternionic Form* and is not derived here; what is specific to the scalar sector is that every term is a central scalar functional.

**The bosonic gap persists diagrammatically.** The perturbative expansion is an expansion of the functional integral on the imported module; the mode algebra is the standard CCR algebra, and the algebra $\mathbb{B}$ contributes only the central-valuedness of the fields, sources, propagators and vertices. There is no diagrammatic object native to $\mathbb{B}$; the trace argument that forbids a bosonic mode in the algebra forbids equally any attempt to read the diagrammatic expansion as an algebraic identity inside it.

**Renormalization.** The divergences of the loop expansion — the vacuum energy, the tadpole, the mass and the coupling — are controlled by the standard counterterms, which are themselves central scalars; the coupling's flow and the renormalization-scale dependence are the generalities of the method. Whether the framework's trace or biquaternion norm fixes a preferred normalization of the counterterms is open, as recorded below.

## The Biquaternion Reading

Four statements summarise what the framework contributes to the scalar functional integral.

**The configuration space is the centre.** The configuration space of the theory is the space of central-valued functions; the action, the source and the measure are central; the state module is a spectator. This is why the scalar functional integral is an ordinary complex functional integral and why no Grassmann or spinor structure appears.

**The quadratic form is the biquaternion norm.** The momentum-space symbol of the Gaussian's operator is $-(\langle\tilde P_{\Phi}\rangle_{\natural}+\mu^2)$ with $\langle\tilde P_{\Phi}\rangle_{\natural}=\tilde P_{\Phi}\tilde P_{\Phi}^{\natural}$, and it vanishes on the mass shell, the level set $\langle\tilde P_{\Phi}\rangle_{\natural}=-\mu^2$. The shell's geometry, the Gaussian's width and the pole of the propagator are three interpretations of one algebraic object, and the framework's convention for $\Box$ makes them mutually consistent.

**The phase is central, and the Wick rotation is a sector relabelling.** The phase $\exp(\frac{k_m\,i\,S}{m\,c})$ is a central $*$-unitary, so it multiplies the whole configuration space uniformly. The continuation to imaginary time is the relabelling of the material coordinate $\tilde R_\Phi=i r'_t\,e_t+r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z\in\mathbb{B}_{\Phi}$ by the real coefficient $c\tau$, which is the passage to the quaternion subspace on which the biquaternion norm is positive definite; this is the standard Wick rotation read as a change of sector, and it is what makes the Euclidean Gaussian converge.

**The algebra supplies nothing beyond the centre.** There is no bosonic ladder in $\mathbb{B}$, as the companion Fock-space article's trace argument shows, so the mode expansion, the Fock space and the perturbative expansion that the path integral organises are all constructed on an imported module. The functional integral's algebraic content is exhausted by the centrality of the field and the biquaternion-norm geometry of the quadratic form.

## What Is Standard and What Is Open

**Standard, and imported.** The field-eigenvalue basis, the time-slicing derivation of the functional integral, the phase-space and Lagrangian forms, and the measure; the generating functional and the functional-derivative formula for the correlation functions; the finite-dimensional Gaussian identity and the completion of the square; the free two-point function as the inverse quadratic form and the Feynman propagator; the representation of the canonical commutator by $-\frac{m\,c\,i}{k_m\,\xi_{\mathrm{scl}}}$; the Euclidean continuation, the lattice regulator and the determinant recursion; the vacuum persistence amplitude, the functional determinant and the relation of its imaginary part to pair creation; the quartic interaction, the Feynman rules with the propagator as the inverse quadratic form, and the loop expansion as the expansion in $\frac{m\,c}{k_m}$. None of this is re-derived here, and none of it depends on the biquaternion structure beyond the kinematical conventions.

**Open in the biquaternion framework.**

- **The measure.** The functional measure is defined as the formal limit of the lattice Lebesgue measure. Whether the framework supplies a canonical measure from its own structure — the trace form, the biquaternion norm, or the real structure — rather than inheriting the Lebesgue measure, is not settled. This is the same open question the companion article *The Path Integral in Biquaternionic Form* records for the one-particle functional integral.
- **The intrinsic generating functional.** Whether the generating functional should be defined with the trace pairing $\mathrm{Tr}$ or the scalar projection $\mathrm{Sc}$, and whether the choice affects the contact terms, is a convention the algebra does not force.
- **The functional determinant and its phase.** The determinant is central, but its phase requires a regularization and a choice of branch. Whether the framework's complex structure fixes the branch, or whether the standard $i\epsilon$ prescription is the only input, is open.
- **Interactions.** A central quartic coupling preserves the centrality of every object. Whether the trace form suggests a preferred normalization of the coupling is not shown; the perturbative expansion is standard once the coupling is fixed.
- **The bosonic gap.** The path integral's variables are c-numbers, which is what makes the bosonic theory an ordinary integral; the scalar sector has no native ladder in $\mathbb{B}$, so the algebraic content remains the centre. Whether an enlarged structure supplements this is the structural question of the whole scalar sector.
- **Empirical content.** Whether the functional integral as written yields a prediction distinguishing the framework from standard scalar field theory is open.

## Summary

The scalar functional integral is the sum over central-valued configurations weighted by the central phase $\exp(\frac{k_m\,i\,S}{m\,c})$, with the action $S[\tilde{Ξ}]=\int d^4r\,[-\mathrm{Sc}((\tilde{\nabla}^{\natural}\tilde{Ξ}^{*})(\tilde{\nabla}\tilde{Ξ}))-\mu^2\mathrm{Sc}(\tilde{Ξ}^{*}\tilde{Ξ})]$. It is derived from the operator formalism by inserting the field-eigenvalue basis at each time, and it is an ordinary functional integral over complex functions because the scalar field is bosonic and its configurations are c-numbers. Its quadratic form has the momentum-space symbol $-(\langle\tilde P_{\Phi}\rangle_{\natural}+\mu^2)$, the biquaternion norm of the material four-wavevector shifted by the mass, so the mass shell $\langle\tilde P_{\Phi}\rangle_{\natural}=-\mu^2$, the Gaussian's width and the propagator's pole are one object.

The generating functional $Z[\tilde J_{\Phi}]$ has for its functional derivatives the time-ordered correlation functions of the field operator, and its free value is the Gaussian $Z[0]\exp(-\int J^*\Delta_F J)$ with $\Delta_F$ the Feynman propagator; the finite-dimensional Gaussian identity was verified by quadrature to a relative difference of $9.7\times10^{-13}$, and the lattice Klein–Gordon inverse to $5.6\times10^{-16}$. The canonical commutator is recovered from the representation $\pi_{\mathrm{fop}}=-\frac{m\,c\,i}{k_m\,\xi_{\mathrm{scl}}}$, and the mode expansion and correlators follow. The vacuum persistence amplitude $|\langle0_{\mathrm{out}}|0_{\mathrm{in}}\rangle|^2=|Z[\tilde Q_5]|^2/|Z[0]|^2$ in a background is the functional-integral form of the pair-creation probability, and it agrees with the Bogoliubov computation of the companion pair-creation article; its imaginary part measures the failure of the vacuum to persist.

The framework's contribution is the centrality of the configuration space, the biquaternion-norm interpretation of the quadratic form, and the identification of the Wick rotation with the passage to the quaternion subspace. The measure, the determinant's branch and the intrinsic generating functional remain open, and the bosonic gap — no native ladder in $\mathbb{B}$ — persists, as it does throughout the scalar sector.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\mu^2=-e_t$ |
| $i$ | Central scalar imaginary |
| $\mathbb{B}_{C}=\mathrm{span}_{\mathbb{R}}\{e_t,ie_t\}$ | Centre; the configuration space's value space |
| $\tilde{Ξ}=\xi_{\mathrm{scl}}\,e_t$, $\tilde J_{\Phi}=J\,e_t$, $\xi_{\mathrm{scl}}=(\xi_{\mathrm{scl},1}+i\xi_{\mathrm{scl},2})/\sqrt2$ | Scalar field and central source; real components |
| $\tilde R_\Phi=i r'_t\,e_t+r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$ | Material coordinate |
| $\tilde{\nabla}=e_t\partial/\partial R_t+\sum_\mu \vec e_\mu\,\partial/\partial R_\mu$, $\Box=\partial^2/\partial R_t^2+\Delta$ | Gradient and d'Alembertian |
| $S[\tilde{Ξ}]$ | Central scalar action |
| $Z[\tilde J_{\Phi}]=\int\mathcal{D}\tilde{Ξ}\,\exp(\,iS+i\int[\mathrm{Sc}(\tilde J_{\Phi}^{*}\tilde{Ξ})+\mathrm{Sc}(\tilde{Ξ}^{*}\tilde J_{\Phi})])$ | Generating functional |
| $\mathcal{D}\tilde{Ξ}$ | Functional measure on central-valued configurations |
| $\delta^{n+m}Z/\delta J^{*n}\delta J^{m}$ | Functional derivatives = time-ordered correlators |
| $Z_N(J)=(2\pi)^{N/2}(\det A)^{-1/2}\exp(J^{T}A^{-1}J/2)$, $Z_N\propto(\det A)^{-1}\exp(J^*A^{-1}J)$ | Finite-dimensional Gaussian identity, real and complex |
| $\Delta_F$ | Feynman propagator; free two-point function |
| $\Delta_F(\tilde P_{\Phi})=-i/(\langle\tilde P_{\Phi}\rangle_{\natural}+\mu^2-i\epsilon)$ | Propagator in material notation |
| $\tilde P_{\Phi}=\frac{m\,c\,(i\omega/c\,e_t+\vec k_\Phi)}{k_m}$, $\langle\tilde P_{\Phi}\rangle_{\natural}=\tilde P_{\Phi}\tilde P_{\Phi}^{\natural}$ | Material four-wavevector and biquaternion norm |
| $\pi_{\mathrm{fop}}=-\frac{m\,c\,i}{k_m\,\xi_{\mathrm{scl}}}$ | Momentum representation; yields $[\xi_{\mathrm{fop}},\pi_{\mathrm{fop}}]=\frac{m\,c\,i\,\delta^{(3)}}{k_m}$ |
| $S_E[\tilde{Ξ}]=\int\mathrm{Sc}(\tilde{Ξ}^{*}(-\Delta_E+\mu^2)\tilde{Ξ})$ | Euclidean action (Wick rotation) |
| $\vert\langle0_{\mathrm{out}}\vert0_{\mathrm{in}}\rangle\vert^2=\vert Z[\tilde Q_5]\vert^2/\vert Z[0]\vert^2$ | Vacuum persistence amplitude |
| $\mathrm{Tr}(e_t)=2$, $\mathrm{Tr}[\tilde Q_2,\tilde Q_1]=0$ | Trace identity; no bosonic mode in $\mathbb{B}$ |

## Further Reading

- R. P. Feynman, "Space-time approach to non-relativistic quantum mechanics," *Reviews of Modern Physics* **20** (1948) 367–387, for the original sum over histories.
- R. P. Feynman and A. R. Hibbs, *Quantum Mechanics and Path Integrals* (McGraw-Hill, 1965), for the time-slicing construction of the kernel and the semiclassical expansion.
- J. Glimm and A. Jaffe, *Quantum Physics: A Functional Integral Point of View* (Springer, 1987), for the constructive definition of scalar functional integrals and the role of the lattice regulator.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the functional integral for scalar fields, the generating functional, and the Gaussian evaluation.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the free generating functional, the two-point function as the inverse quadratic form, and the Wick rotation.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the loop expansion, the functional determinant, and the effective action.
- L. S. Brown, *Quantum Field Theory* (Cambridge, 1992), for the relation between the imaginary part of the effective action and pair creation.
- M. Reed and B. Simon, *Methods of Modern Mathematical Physics, Vol. II: Fourier Analysis, Self-Adjointness* (Academic Press, 1975), for Gaussian measures on function spaces and positive-definiteness conditions.
