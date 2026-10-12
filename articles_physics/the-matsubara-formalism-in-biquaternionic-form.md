# __The Matsubara Formalism in Biquaternionic Form__

## Introduction

The **Matsubara formalism** is the Euclidean formulation of quantum field theory at finite temperature. The thermal partition function $Z=\mathrm{Tr}\,e^{-\beta H}$ is written as a functional integral over fields living on a Euclidean space whose time direction is compactified to a circle of circumference $\beta=\hbar/(k_BT)$; the Fourier modes on that circle are the **Matsubara frequencies**, and the propagator becomes a discrete sum over them rather than a continuous integral. It is the standard machinery of thermal field theory, and it is the analytic continuation of the real-time formalisms.

This article asks what the biquaternion algebra $\mathbb{B}$ contributes. The answer is one structural identification and a set of transcriptions, stated at the outset.

- **Established (framework).** The compactified direction is a **material-sector direction**. The imaginary time that Matsubara's circle winds around is not an auxiliary device introduced for convergence: it is the intrinsic imaginary direction of the material sector $\mathbb{M}_-$, the same direction that appears as $ict$ in the biquaternionic gradient and as the KMS analyticity strip in *The KMS Condition and the Biquaternion Framework*. The KMS strip has width $\beta$ and the Matsubara circle has circumference $\beta$, and these are the same $\beta$ because they are the same complexified material time. Concretely, the analytic strip $0<\mathrm{Im}\,t<\beta$ of the KMS boundary relation
$$
F_{\tilde A\tilde B}(t+i\beta) = F_{\tilde B\tilde A}(-t)
$$
is the strip swept when the material time is complexified, and the periodic identification $t\sim t+i\beta$ that makes it a cylinder is the compactification that defines the Matsubara sum.
- **Established (algebra).** The thermal wave biquaternion stays in the material sector,
$$
\tilde k_E = i\omega_n e_0+\mathbf p \in \mathbb{M}_- ,
\qquad
N(\tilde k_E)=-\omega_n^2+\mathbf p^2 ,
\qquad
\langle\tilde k_E,\tilde k_E\rangle_{*}=\omega_n^2+\mathbf p^2 = k_E^2 \ge 0 ,
$$
with the frequency along the imaginary scalar direction of $\mathbb{M}_-$ and the momentum along its real spatial direction. The standard route reaches the same operator by the Wick rotation, $t\to-i\tau$, which reads the element on the real scalar axis; the material-sector route reaches it without a rotation and names the form. The Euclidean mass-shell operator is the **Hermitian form** of that element,
$$
\mathcal{M}_E(\tilde k_E) = \langle\tilde k_E,\tilde k_E\rangle_{*}+m^2 = \omega_n^2+\mathbf p^2+m^2 = k_E^2+m^2 > 0 ,
$$
positive because the Hermitian form is positive definite of signature $(8,0)$ and not because the axes are rotated: the biquaternion norm of the same element, $N(\tilde k_E)=-\omega_n^2+\mathbf p^2$, is indefinite and cannot serve, being the interval and not the probability. So the Euclidean propagator $1/(k_E^2+m^2)$ has no real pole; the Lorentzian mass shell $\tilde k\tilde k^{\natural}=-m^2$ maps to $k_E^2=-m^2$, which is reached only at complex momentum. This is the framework's statement that the thermal propagator's analytic structure is a statement about the complexification of a material direction.
- **Established (algebra).** The spin–statistics theorem of the companion article fixes the periodicity: bosonic fields are periodic and fermionic fields antiperiodic on the thermal circle, and the Matsubara frequencies are therefore
$$
\omega_n = \frac{2\pi n}{\beta}\ \ (\text{bosons}),
\qquad
\omega_n = \frac{(2n+1)\pi}{\beta}\ \ (\text{fermions}).
$$
In the framework the bosonic/fermionic distinction is the even/odd grading of the algebra, so the two frequency sets are the two gradings' Fourier sets.
- **Standard, and transcribed.** The Matsubara sum and its thermal factors, the contour evaluation, the free energy of a mode, the finite-temperature Feynman rules, and the discrete loop sums. The algebra supplies the identification of the circle and the biquaternion-norm operator; it does not supply the temperature.

The findings are recomputed: the bosonic sum rule $(1/\beta)\sum_n(\omega_n^2+E^2)^{-1}=\coth(\beta E/2)/(2E)$ and its fermionic counterpart with $\tanh$, the geometric sums for the Bose and Fermi occupation numbers, and the single-mode free energies.

The article proceeds as follows. The next section records the standard Wick route and the material-sector alternative, then fixes the compactified material time and the thermal circle. A section gives the Matsubara frequencies and the thermal propagator. A section derives the partition function and the free energy. A section isolates the framework's structural content. A section treats the Matsubara sums and the thermal factors, and a section the finite-temperature Feynman rules. A section separates what is established from what is interpretation.

**Conventions.** We use those of the companion articles, in particular *The KMS Condition and the Biquaternion Framework*, *The Unruh Effect in Biquaternionic Form*, and *Hawking Radiation in Biquaternionic Form*, whose thermal state this article's formalism must reproduce. The algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, and central scalar imaginary $i$. The material sector is $\mathbb{M}_-$ (anti-Hermitian) and the informational sector is $\mathbb{M}_+$ (Hermitian), with $\mathbb{B}=\mathbb{M}_-\oplus\mathbb{M}_+$ and $i\mathbb{M}_\pm=\mathbb{M}_\mp$. The material coordinate is $\tilde{Q}=ict\,e_0+\mathbf x$, with biquaternion norm $N(\tilde{Q})=-c^2t^2+\mathbf x^2$, indefinite of signature $(3,1)$ on $\mathbb{M}_-$; the Hermitian form (the general plain sesquilinear form, written $H$ in the companion articles) is $\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})=\sum_\mu P_\mu\overline{Q_\mu}$, positive definite of signature $(8,0)$ on $\mathbb{B}$ and equal on the material sector to the Euclidean square, $\langle\tilde Q,\tilde Q\rangle_{*}=c^2t^2+\mathbf x^2$. It is this form that the thermal propagator uses, and it is distinct from the Hamiltonian $H$ of the partition function. The gradient is $\tilde\nabla=e_0\partial_{ict}+e_k\partial_k$ and $\Box=\tilde\nabla\tilde\nabla^{\natural}=\partial_{ict}^2+\Delta$; the $ict$ metric is $\eta=\mathrm{diag}(-1,+1,+1,+1)$. The Lorentzian wave biquaternion is $\tilde k=iEe_0+\mathbf p$ with quaternion conjugate $\tilde k^{\natural}=iEe_0-\mathbf p$ and $\tilde k\tilde k^{\natural}=-p^2$. The inverse temperature is $\beta=\hbar/(k_BT)$; the trace pairing is $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$. Natural units $\hbar=c=k_B=1$ are used in the computations, with $\beta$ and the temperature restored where a physical statement is made.

## Imaginary Time and the Thermal Circle

The Matsubara formalism is usually reached by a Wick rotation, and it is reached here without one. Both routes are recorded, and so is the reason the second is used.

**The standard route: the Wick rotation, quoted.** The usual treatment continues the real time, $\tau=it$ with $t=-i\tau$: the material-time coefficient $ict$ becomes the real $c\tau$, the Minkowski metric $\eta=\mathrm{diag}(-1,+1,+1,+1)$ becomes the Euclidean metric $\delta=\mathrm{diag}(+1,+1,+1,+1)$, and the wave biquaternion is read on the real scalar axis,
$$
\tilde k_E = -\omega_n e_0+\mathbf p ,
\qquad
\tilde k_E\tilde k_E^{\natural} = \omega_n^2+\mathbf p^2 = k_E^2 \ge 0 .
$$
This is the framework's level-2 to level-1 passage and it is standard (*The Wick Rotation in the Biquaternion Universe*; *The Functional Integral in Biquaternionic Form* uses the same identification). The norm of the rotated element is positive there, and the standard route takes the positivity from that rotated metric. It is correct, and it is what the literature does.

**The alternative route: the material sector, no rotation.** The same result is obtained without leaving $\mathbb{M}_-$, by complexifying the material time along its own imaginary direction instead of rotating the axes. The material-time coefficient is $ict$, along the imaginary scalar direction of $\mathbb{M}_-$, and the physical time $t$ is real while the coefficient carries the $i$. Thermal equilibrium complexifies this coordinate, $t\mapsto t+is$ with $0<s<\beta$ the KMS strip of the boundary relation above, and the periodic identification builds the circle out of that imaginary displacement itself. No coordinate leaves $\mathbb{M}_-$, and the thermal frequency is the conjugate variable of the compactified material time, placed along the same imaginary scalar direction,
$$
\tilde k_E = i\omega_n e_0+\mathbf p \in \mathbb{M}_- .
$$
On this element the interval keeps its sign, $N(\tilde k_E)=-\omega_n^2+\mathbf p^2$, indefinite; the norm cannot supply the positivity the rotated route got from the metric. The definite form does, $\langle\tilde k_E,\tilde k_E\rangle_{*}=\omega_n^2+\mathbf p^2=k_E^2$, as the propagator below records. The two routes therefore agree on the propagator, $D_E=1/(k_E^2+m^2)$, and differ in what they change: the standard route rotates the metric and leaves the form implicit, the material-sector route keeps the metric and names the form. The second is used in this article because it needs no change of sector, and because the form it names is the same Hermitian form for which the Bochner theorem of the companion article is stated. Both routes are successful; the alternative is the one taken.

**The thermal circle.** The complexified material time is compactified,
$$
t \sim t+i\beta ,
\qquad
\beta=\hbar/(k_BT),
$$
so the configuration manifold is $S^1_\beta\times\mathbb{R}^3$ with the circle of circumference $\beta$ drawn in the imaginary material direction; write $\tau$ for the real parameter along the circle. The compactification is the statement of thermal equilibrium: the partition function $Z=\mathrm{Tr}\,e^{-\beta H}$ is the functional integral on that manifold, with the circle's circumference playing the role of the inverse temperature. This is standard (Matsubara 1955; Fetter–Walecka; Kapusta–Gale) and is transcribed.

**Periodicity and statistics.** The fields on the circle must be single-valued up to the statistics sign. The KMS boundary relation for a thermal two-point function,
$$
F_{\tilde A\tilde B}(t+i\beta) = F_{\tilde B\tilde A}(-t),
$$
is the operator-exchange identity whose resolution is periodicity for the bosonic (commuting) grading and antiperiodicity for the fermionic (anticommuting) grading:
$$
\tilde\Phi_{\text{boson}}(\tau+\beta) = +\tilde\Phi_{\text{boson}}(\tau),
\qquad
\tilde\Psi_{\text{fermion}}(\tau+\beta) = -\tilde\Psi_{\text{fermion}}(\tau).
$$
The framework's grading is the even/odd decomposition of the algebra and of the spinor module, so the two periodicity classes are the two grading classes; this is the finite-temperature face of *The Spin–Statistics Theorem in Biquaternionic Form*, and no new input is needed beyond the grading and the KMS relation.

## The Matsubara Frequencies and the Thermal Propagator

The periodicity fixes the spectrum of the compactified time derivative, and hence the propagator.

**Frequencies.** A function on the circle of circumference $\beta$ has Fourier modes $e^{i\omega_n\tau}$, and the boundary condition selects the frequencies
$$
e^{i\omega_n(\tau+\beta)}=+e^{i\omega_n\tau} \Rightarrow \omega_n=\frac{2\pi n}{\beta},
\qquad
e^{i\omega_n(\tau+\beta)}=-e^{i\omega_n\tau} \Rightarrow \omega_n=\frac{(2n+1)\pi}{\beta},
\qquad n\in\mathbb{Z},
$$
which are the **bosonic** and **fermionic Matsubara frequencies**. The discrete spectrum replaces the continuous $p^0$ integral of the vacuum theory by a sum:
$$
\int\frac{dp^0}{2\pi}\,f(p^0) \;\longrightarrow\; \frac{1}{\beta}\sum_{n\in\mathbb{Z}} f(i\omega_n),
$$
and the corresponding thermal wave biquaternion is the material element $\tilde k_E=i\omega_n e_0+\mathbf p$, whose Hermitian square is $\langle\tilde k_E,\tilde k_E\rangle_{*}=\omega_n^2+\mathbf p^2=k_E^2$.

**The propagator in the material sector.** In the framework the Lorentzian propagator's denominator is the mass-shell operator $\mathcal{M}(\tilde k)=\tilde k\tilde k^{\natural}+m^2=-p^2+m^2$ at the material wave biquaternion $\tilde k=iEe_0+\mathbf p\in\mathbb{M}_-$. On the thermal grid the frequency sits along the imaginary scalar direction, $\tilde k_E=i\omega_n e_0+\mathbf p$, and the denominator is the Hermitian form of that element,
$$
\langle\tilde k_E,\tilde k_E\rangle_{*}=\lvert i\omega_n\rvert^2+\lvert\mathbf p\rvert^2=\omega_n^2+\mathbf p^2=k_E^2 ,
\qquad
\mathcal{M}_E(\tilde k_E)=\langle\tilde k_E,\tilde k_E\rangle_{*}+m^2=k_E^2+m^2 ,
$$
so that
$$
D_E(\tilde k_E) = \frac{1}{\mathcal{M}_E(\tilde k_E)} = \frac{1}{k_E^2+m^2} .
$$
The same element read with the norm gives $N(\tilde k_E)=-\omega_n^2+\mathbf p^2$, indefinite; the interval and the probability are two forms of one element, and it is the definite one that the thermal denominator needs. The operator is central and positive for real frequencies and momenta, $k_E^2+m^2>0$; hence $D_E$ is a bounded, real-analytic function on the Matsubara grid, and it has no pole there. The Lorentzian mass shell $\tilde k\tilde k^{\natural}=-m^2$ becomes $k_E^2=-m^2$, reached only at complex momentum. This is the framework's statement of the standard fact that the propagator's singularities lie off the real axis, and it shows that the analytic structure of the thermal propagator is a statement about the complexified material direction: the circle is a material direction, and the pole is at complex momentum on that axis.

$$
\frac{1}{\beta}\sum_{n\in\mathbb{Z}}\frac{1}{\omega_n^2+E^2} = \frac{1}{2E}\coth\frac{\beta E}{2}
$$
was checked by direct summation over $\omega_n=2\pi n/\beta$ for $|n|\le2\times10^6$, giving $0.4463328$ against the closed form $0.4463329$, and the fermionic sum rule
$$
\frac{1}{\beta}\sum_{n\in\mathbb{Z}}\frac{1}{\bar\omega_n^2+E^2} = \frac{1}{2E}\tanh\frac{\beta E}{2}
$$
with $\bar\omega_n=(2n+1)\pi/\beta$ gave $0.3314319$ against $0.3314320$. The residual is the truncation of the sum; both rules are standard and the check confirms the frequency sets used here.

## The Partition Function and the Free Energy

The partition function is the Gaussian integral of the thermal theory, and its logarithm is the free energy.

**The functional integral.** Under the complexification and the compactification, the thermal partition function is
$$
Z(\beta) = \mathrm{Tr}\,e^{-\beta H} = \int_{\text{periodic}}\mathcal{D}\tilde\Phi\;e^{-S_E[\tilde\Phi]},
$$
the integral taken over field configurations obeying the periodicity appropriate to the grading, on $S^1_\beta\times\mathbb{R}^3$. This is the Euclidean functional integral of the previous articles with the time direction compactified, and everything said there about the module, the central quadratic operator, and the Gaussian determinant applies verbatim; only the mode set changes from $\int dp^0$ to $(1/\beta)\sum_n$.

**One-loop free energy.** For the free biquaternion scalar the Euclidean action is quadratic with operator $\mathcal{M}_E$, and the Gaussian integral gives
$$
\log Z(\beta) = -\frac12\,\mathrm{Tr}\log\mathcal{M}_E
= -\frac{1}{2}\sum_{n}\sum_{\mathbf p}\sum_{j}\log\big(\omega_n^2+\mathbf p^2+m^2\big)
= -\beta\,F(\beta),
$$
the trace being over the module and the last equality defining the free energy $F=E-TS$. The index $j$ runs over the directions the module's traces contribute, this being a component count and not a sum over independent fields: the central eigenvalue is repeated as many times as the trace requires, the sectors being graded parts of one field related by the central $i$ rather than independent copies, as *The Functional Integral in Biquaternionic Form*, *The Partition Function in Biquaternionic Form*, and *The Harmonic Oscillator in Biquaternionic Form* record.

**Single mode.** For a single bosonic mode of energy $E$ the partition function is the geometric sum
$$
Z_{\text{boson}} = \sum_{n\ge0}e^{-\beta En}=\frac{1}{1-e^{-\beta E}},
\qquad
\log Z_{\text{boson}}=-\log\big(1-e^{-\beta E}\big),
$$
and for a single fermionic mode, which can be occupied at most once,
$$
Z_{\text{fermion}} = 1+e^{-\beta E},
\qquad
\log Z_{\text{fermion}}=\log\big(1+e^{-\beta E}\big).
$$
Both were checked numerically against the geometric sums; the occupation numbers
$$
n_{\mathrm B}(E)=\frac{1}{e^{\beta E}-1},
\qquad
n_{\mathrm F}(E)=\frac{1}{e^{\beta E}+1}
$$
follow. The two-state fermionic mode is the finite-temperature face of the one-mode algebra of the Fock and S-matrix articles.

**The thermal state and the companions.** The state whose correlation functions are the KMS functions at inverse temperature $\beta$ is the Gibbs state $\rho=e^{-\beta H}/Z$, with modular Hamiltonian $K=-\log\rho=\beta H+\log Z$, a Hermitian element of the informational sector $\mathbb{M}_+$ as *The KMS Condition and the Biquaternion Framework* records in its finite-dimensional setting. The Matsubara formalism is the Euclidean evaluation of that state's correlation functions, and it reproduces the Unruh and Hawking results when $\beta$ is the appropriate $2\pi c/\kappa$: the temperature is *not* produced by the formalism, it is the input $\beta$, exactly as those articles state. What the formalism supplies is the Euclidean machinery for computing with any $\beta$.

## The Framework's Structural Content

Three statements are the framework's, and they are worth separating from the transcriptions.

**The thermal circle is a material direction.** The imaginary direction of the KMS strip is the imaginary direction of the material sector, $\mathbb{M}_-\oplus i\mathbb{M}_-=\mathbb{B}$ in the sense of the Unruh article's complexified Rindler time; the Matsubara circle is the compactification of that direction. Hence the thermal circle is not an artifact of a convergence trick: it is a circle drawn in a direction the algebra already distinguishes. The framework's statement is that the KMS strip and the thermal circle are the same object read analytically and topologically.

**The Euclidean operator is the Hermitian form on a material element.** $\mathcal{M}_E=\langle\tilde k_E,\tilde k_E\rangle_{*}+m^2$ is the positive form of the material wave biquaternion, central because the value of the form on one element is a real scalar, and identical in form to the Lorentzian operator. So the thermal propagator is the inverse of the probability form evaluated on a discrete momentum set, in the same sector the Lorentzian theory uses. All the algebra's structure — centrality, the module's dimension — passes to the thermal theory unchanged; the temperature enters only through the spacing of the mode set. The norm $N(\tilde k_E)=-\omega_n^2+\mathbf p^2$ is the interval of the same element and is indefinite, so the two forms are not interchangeable and it is that form that the thermal theory needs.

**Statistics is the grading.** The periodic/antiperiodic split of the thermal circle is the even/odd split of the algebra and of the spinor module. This is a consistency, not a derivation: the framework houses the spin–statistics theorem, as the companion article argues, and the Matsubara frequency sets are its Fourier expression.

**What the framework does not supply.** The value of $\beta$. Temperature is a state parameter, fixed by the physical situation (a heat bath, a horizon, an acceleration); the algebra determines neither the existence of a thermal state nor its temperature. This is the same statement the Unruh and Hawking articles make when they insist that they house thermality rather than derive it.

## Matsubara Sums and Thermal Factors

The computational heart of the formalism is the conversion of a frequency sum into a thermal factor, and it is where the circle's winding number appears.

**The contour method.** A sum over Matsubara frequencies is evaluated by a contour integral enclosing the poles of a kernel:
$$
\frac{1}{\beta}\sum_{n}f(i\omega_n)
= \frac{1}{2\pi i}\oint f(z)\,\frac{1}{2}\coth\frac{\beta z}{2}\,dz
\qquad\text{(bosons)},
\qquad
\frac{1}{\beta}\sum_{n}f(i\bar\omega_n)
= \frac{1}{2\pi i}\oint f(z)\,\frac{1}{2}\tanh\frac{\beta z}{2}\,dz
\qquad\text{(fermions)},
$$
the kernels being $\coth$ and $\tanh$ because they have poles exactly at the bosonic and fermionic frequencies, with residue $1/\beta$ after the factor $\tfrac12$, which is the prefactor the sum requires. Evaluating the contour on the physical poles of $f$ gives the thermal factors. This is standard (Fetter–Walecka, Kapusta–Gale) and is cited.

**Checks.** On $f(z)=1/(z^2+E^2)$ the bosonic contour gives $f$'s poles at $z=\pm iE$ with the kernel $\tfrac12\coth(\beta z/2)$, yielding
$$
\frac{1}{\beta}\sum_n\frac{1}{\omega_n^2+E^2} = \frac{1}{2E}\Big(1+2n_{\mathrm B}(E)\Big)=\frac{1}{2E}\coth\frac{\beta E}{2},
$$
and the fermionic one yields $\frac{1}{2E}\tanh(\beta E/2)=\frac{1}{2E}(1-2n_{\mathrm F}(E))$; both were checked numerically in the previous section. The bracket $(1+2n_{\mathrm B})$ is the sum of the vacuum zero-point piece and the thermal excitation, which is the standard interpretation: the $\tfrac12$ is the vacuum energy and the $n$ is the thermal population.

**Biquaternion content.** The kernel is a central scalar, so it commutes with the module structure and multiplies each mode independently; the same thermal factor is therefore repeated once per complex dimension the trace runs over, a component count rather than a sum over independent sectors. Where the framework makes a difference is when the operator is not central — a spinor loop, whose Matsubara sum runs over the fermionic frequencies and whose numerator carries the matrix structure of the spinor module.

## The Matsubara Green's Function and Its Continuation

The discrete sum is not the end of the calculation; the physical response functions are obtained by analytic continuation, and the framework's interpretation of the continuation is the material-direction one.

**Spectral representation.** The thermal Green's function has the spectral representation
$$
G(i\omega_n) = \int_{-\infty}^{\infty}\frac{d\omega}{2\pi}\,\frac{A(\omega)}{i\omega_n-\omega} ,
\qquad
A(\omega)\ \ge 0 ,
$$
in which $A$ is the spectral function and the discrete frequencies $\omega_n$ are the points at which the function is known. This is the finite-temperature form of the Källen–Lehmann representation of the LSZ article, and its positivity has the same origin, the positivity of the inner product of the state space. The analytic structure of $G$ in the complex frequency plane is therefore fixed by $A$: $G$ is analytic off the real axis and its discontinuity across the cut is $A$.

**The positivity is the Bochner theorem at the central root.** The thermal two-point function is a positive-definite function on the compactified time: $F_{\tilde A\tilde A}(t)=\langle\tilde A(t)\tilde A\rangle_\beta$ is positive definite by the positivity of the state-space inner product. That is the hypothesis of Bochner's theorem, and the conclusion is that $F$ is the transform of a positive measure on the circle — the discrete measure with weights $A(\omega_n)\ge0$. So the spectral function's positivity is not an extra assumption of the thermal theory; it is the classical Bochner statement, and in the framework it is the central-root case of the biquaternion Bochner theorem, quoted here in the form the companion article proves it. With the general plain sesquilinear form $\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})$, the quadratic form $Q=\sum_{k,l}A_kG(\omega_k-\omega_l)A_l^{*}$ factorises as the integral $\int ZZ^{*}\,d\mu$ of a positive element, and the transform of a positive measure is positive definite **exactly** for the degenerate roots — the central imaginary $\rho=\pm i$ and the unit pure real quaternions $\rho=\pm\mu$ — while the non-degenerate roots $\rho=b\mu+d\nu i$ fail; at the central root the transform is $G=\varphi e_0$ with $\varphi$ the classical positive-definite function (*The Bochner Theorem for the Biquaternion Transform: the Hermitian Form and the Root*). The Matsubara kernel is the **central-root** character: $e^{i\omega_n\tau}$ is the exponential of $\rho=i$, the central scalar imaginary, and the central root is degenerate. The thermal correlator's positivity is therefore the central-root case of the theorem, found by the same form $\langle\cdot,\cdot\rangle_{*}$ that the propagator uses. No passage to another sector is involved: the kernel is central, the root is degenerate, and the measure is the one the state supplies.

**Continuation.** The retarded and advanced functions are the boundary values
$$
G^{R/A}(\omega) = G(\omega\pm i\epsilon),
$$
and the passage from the discrete grid to the real axis is the **analytic continuation** $i\omega_n\to\omega+i\epsilon$. The KMS relation is what makes the continuation well posed: it is the statement that $G(z)$ is analytic in the strip $0<\mathrm{Im}\,z<\beta$ up to the physical cut, and the strip's width is the thermal-circle circumference. In the framework the strip is a strip in the complexified material time, as in *The Unruh Effect in Biquaternionic Form*, and the continuation from the grid to the real axis is a movement within the material-sector complexification; the algebra supplies the direction, the standard theory supplies the theorem that the boundary value is the response function.

**A caution.** The continuation is unique only given the spectral function's decay and the analyticity; the Matsubara formalism determines $G$ on the grid and the real-time response follows from the spectral representation, not from the grid alone. This is the same point that *The Feynman Propagator in Biquaternionic Form* makes about the $i\epsilon$ orientation not being algebraic data, here in the thermal setting.

## Finite-Temperature Feynman Rules

The interaction theory is the vacuum perturbation theory with the discrete sums and the modified propagator, and the framework's conventions pass through unchanged.

**The rules.** Each internal line is the Euclidean propagator $D_E(\tilde k_E)=1/(k_E^2+m^2)$ with $k_E^0$ drawn from the appropriate frequency set; each internal frequency is summed as $(1/\beta)\sum_n$; each vertex is $-S_{\mathrm{int}}$ as in the vacuum theory, with the conservation of the discrete frequency imposed by the vertex; and the external legs are on the Matsubara grid, or continued to real frequency for a real-time response. The Euclidean theory is the analytic continuation of the real-time ones, and the retarded and advanced propagators are recovered by continuation from the discrete grid, as the propagator article notes for the thermal case.

**The zero mode.** The $n=0$ bosonic mode, $\omega_0=0$, is special: it is static, its Euclidean propagator is $1/(\mathbf p^2+m^2)$, and for a massless field it contributes a non-analytic zero mode that is the origin of the infrared problems of thermal field theory and of the dimensional reduction of the high-temperature limit. In the framework the zero mode is the mode whose phase is independent of the material time, i.e. constant along the thermal circle; it is the material-sector analogue of a topological sector, and it is where the thermal circle's compactification is most visible.

**The high-temperature limit.** As $\beta\to0$ the frequency spacing diverges and the discrete sum approaches the continuous integral; the leading thermal corrections are the standard $T^4$ (radiation) and $T^2$ (mass) terms of the high-temperature expansion. The framework adds the module's counting to these, through the multiplicity of the trace, and nothing else; the algebra is not a theory of the equation of state.

## What Is Established and What Is Interpretation

**Established (framework).**
- The Matsubara circle is a compactified material-sector direction; its circumference is the KMS width $\beta$, and the KMS strip and the circle are the same complexified material time.
- The Euclidean mass-shell operator is the Hermitian form of the material wave biquaternion, $\mathcal{M}_E=\langle\tilde k_E,\tilde k_E\rangle_{*}+m^2=k_E^2+m^2$ with $\tilde k_E=i\omega_n e_0+\mathbf p\in\mathbb{M}_-$, central and positive, with no real pole; the norm $N(\tilde k_E)=-\omega_n^2+\mathbf p^2$ is indefinite; the Lorentzian mass shell maps to complex momentum.
- The thermal correlator's positivity is the Bochner theorem at the central root, $\rho=i$, the root of the kernel $e^{i\omega_n\tau}$.
- The two frequency sets are the two grading classes' Fourier spectra; the periodic/antiperiodic split is the even/odd split.
- The free energy carries the multiplicity of the module trace; the one-loop free energy is $\log Z=-\tfrac12\mathrm{Tr}\log\mathcal{M}_E$.

**Standard, and transcribed.**
- The Wick rotation (quoted above as the standard route, not used in the body) and the compactification of the time direction; the Matsubara frequencies; the contour evaluation of the sums and the thermal factors; the occupation numbers; the finite-temperature Feynman rules; the zero mode and the high-temperature expansion; the Gibbs state and its modular Hamiltonian.

**Interpretation.**
- Reading the thermal circle as drawn in the material sector, and the Euclidean pole structure as a statement about the complexified material direction, are the framework's structural interpretations. They are consistent with the KMS and Unruh articles and do not by themselves force a thermal interpretation.

**Open.**
- The temperature is an input; the framework does not derive it. The Unruh and Hawking articles' gaps — that the modular flow is imported and that the algebra does not produce thermality — are inherited unchanged.
- The finite-dimensional modular Hamiltonian of the KMS article is not extended here to the field algebra; the thermal state is used as the standard Gibbs state of the standard field theory.

## The Euclidean and Thermal Splits in the Algebra

The identifying statement of the article is that the compactified direction is the material time $ict$, a direction of the material sector $\mathbb{M}_-$. The Euclidean-versus-thermal distinction is therefore read **inside** $\mathbb{M}_-$ and does not move the element to another sector. Two forms live on that one sector: the indefinite interval $N$, whose one negative direction is the time $ict$, and the positive Hermitian form $\langle\cdot,\cdot\rangle_{*}$, definite there and equal to the Euclidean square, $\langle\tilde Q,\tilde Q\rangle_{*}=c^2t^2+\mathbf x^2$. The Euclidean reading of the thermal theory is the reading of the material sector through the form: the direction $N$ makes negative is the direction that was compactified, and the form is positive on it and on the rest. What is called the Euclidean section is, on the standard route, the rotated copy reached by $t\to-i\tau$; on the route taken here it is the same material elements read with the definite form. The circle is the compactification of the one direction $N$ makes negative, and the form is what makes the corresponding frequencies positive.

This is why the article's computations are done in $\mathbb{M}_-$ and not in a real-quaternion slice. The material sector already carries both forms, the interval that fixes the causal cone and the probability form that fixes the weights, and it is the second that the thermal propagator needs. The block structure $\mathbb{B}=\mathbb{H}_{\mathbb{B}}\oplus i\mathbb{H}_{\mathbb{B}}$ reads the same object through the central $i$, and its owner is *Other Remarkable Subspaces*; it is a place to put the result, whereas the result itself is a statement about $\mathbb{M}_-$.

## Summary

The Matsubara formalism in biquaternionic form is thermal field theory with the compactified direction identified as the material direction $ict$. The standard route to it is the Wick rotation $t\to-i\tau$, which reads the wave biquaternion as $-\omega_n e_0+\mathbf p$ on the real scalar axis with a definite norm; this article uses instead the material-sector route, in which the computation never leaves $\mathbb{M}_-$ and the positivity is carried by the Hermitian form rather than by the rotated metric. The two routes give the same propagator and the same frequencies. The thermal circle $t\sim t+i\beta$ has circumference $\beta=\hbar/(k_BT)$, which is the KMS strip width, because both are the complexification of that same material time; the wave biquaternion of the grid is material,
$$
\tilde k_E = i\omega_n e_0+\mathbf p \in \mathbb{M}_- ,
\qquad
N(\tilde k_E)=-\omega_n^2+\mathbf p^2 ,
\qquad
\langle\tilde k_E,\tilde k_E\rangle_{*}=\omega_n^2+\mathbf p^2=k_E^2 ,
$$
and the Euclidean mass-shell operator is the Hermitian form of that element,
$$
\mathcal{M}_E(\tilde k_E)=\langle\tilde k_E,\tilde k_E\rangle_{*}+m^2=\omega_n^2+\mathbf p^2+m^2=k_E^2+m^2>0 ,
$$
positive because the Hermitian form is positive definite and not because the axes are rotated, so the propagator has no real pole and the Lorentzian mass shell maps to complex momentum. The positivity of the thermal correlator is the Bochner theorem at the central root, $\rho=i$, the root of the kernel $e^{i\omega_n\tau}$. The frequencies are $\omega_n=2\pi n/\beta$ (bosonic) and $\omega_n=(2n+1)\pi/\beta$ (fermionic), the two grading classes' Fourier spectra. The sum rules
$$
\frac{1}{\beta}\sum_n\frac{1}{\omega_n^2+E^2}=\frac{\coth(\beta E/2)}{2E},
\qquad
\frac{1}{\beta}\sum_n\frac{1}{\bar\omega_n^2+E^2}=\frac{\tanh(\beta E/2)}{2E}
$$
were checked numerically ($0.4463328$ and $0.3314319$ against $0.4463329$ and $0.3314320$ at $\beta=2$, $E=1.3$), and the single-mode free energies $\log Z_{\text{boson}}=-\log(1-e^{-\beta E})$ and $\log Z_{\text{fermion}}=\log(1+e^{-\beta E})$ follow from the geometric sums. The partition function is the Euclidean functional integral on $S^1_\beta\times\mathbb{R}^3$, its one-loop value carries the multiplicity of the module trace, and the finite-temperature rules are the vacuum rules with a discrete frequency sum. The temperature itself is an input, and the framework houses rather than derives thermality, consistently with *The KMS Condition and the Biquaternion Framework*, *The Unruh Effect in Biquaternionic Form*, and *Hawking Radiation in Biquaternionic Form*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $\mathbb{M}_-,\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\tilde{Q}=ict\,e_0+\mathbf x$ | Material coordinate |
| $t\sim t+i\beta$ | Thermal circle $S^1_\beta$: the complexified material time, compactified |
| $\beta=\hbar/(k_BT)$ | Inverse temperature; circle circumference; KMS width |
| $\tau$ | real parameter along the thermal circle |
| $F_{\tilde A\tilde B}(t+i\beta)=F_{\tilde B\tilde A}(-t)$ | KMS boundary relation |
| $\tilde\Phi(\tau+\beta)=\pm\tilde\Phi(\tau)$ | Periodic (boson) / antiperiodic (fermion) |
| $\omega_n=2\pi n/\beta$ | Bosonic Matsubara frequencies |
| $\bar\omega_n=(2n+1)\pi/\beta$ | Fermionic Matsubara frequencies |
| $\tilde k_E=i\omega_ne_0+\mathbf p\in\mathbb{M}_-$ | material wave biquaternion of the thermal grid |
| $N(\tilde k_E)=-\omega_n^2+\mathbf p^2$, $\langle\tilde k_E,\tilde k_E\rangle_{*}=k_E^2=\omega_n^2+\mathbf p^2$ | the interval (indefinite) and the probability form (positive) of the same element |
| $\mathcal{M}_E=\langle\tilde k_E,\tilde k_E\rangle_{*}+m^2=k_E^2+m^2$ | Euclidean mass-shell operator (Hermitian form of the material element) |
| $D_E=1/(k_E^2+m^2)$ | Euclidean (thermal) propagator |
| $(1/\beta)\sum_n$ | Matsubara sum replacing $\int dp^0/2\pi$ |
| $Z=\mathrm{Tr}\,e^{-\beta H}=\int_{\text{per}}\mathcal{D}\tilde\Phi\,e^{-S_E}$ | Thermal partition function |
| $\log Z=-\beta F=-\tfrac12\mathrm{Tr}\log\mathcal{M}_E$ | Free energy (one loop) |
| $n_{\mathrm B}=1/(e^{\beta E}-1)$, $n_{\mathrm F}=1/(e^{\beta E}+1)$ | Bose / Fermi occupation numbers |

## Further Reading

- T. Matsubara, "A new approach to quantum-statistical mechanics," *Progress of Theoretical Physics* **14** (1955) 351–378, for the imaginary-time formulation and the frequency sums.
- A. L. Fetter and J. D. Walecka, *Quantum Theory of Many-Particle Systems* (McGraw-Hill, 1971), for the Matsubara Green's functions, the contour evaluation of the sums, and the thermal factors.
- J. I. Kapusta and C. Gale, *Finite-Temperature Field Theory: Principles and Applications* (Cambridge, 2006), for the finite-temperature Feynman rules, the zero mode, and the high-temperature expansion.
- M. Le Bellac, *Thermal Field Theory* (Cambridge, 1996), for the comparison of the imaginary-time and real-time formalisms and the analytic continuation.
- N. P. Landsman and C. G. van Weert, "Real- and imaginary-time field theory at finite temperature and density," *Physics Reports* **145** (1987) 141–249, for the relation between the Matsubara and Schwinger–Keldysh formalisms.
- R. Kubo, "Statistical-mechanical theory of irreversible processes. I," *Journal of the Physical Society of Japan* **12** (1957) 570–586, for the KMS condition and the analytic properties of thermal correlation functions.
- P. C. Martin and J. Schwinger, "Theory of many-particle systems. I," *Physical Review* **115** (1959) 1342–1373, for the original derivation of the thermal Green's-function formalism.
- G. W. Gibbons and S. W. Hawking, "Action integrals and partition functions in quantum gravity," *Physical Review D* **15** (1977) 2752–2756, for the Euclidean period that fixes a temperature from the geometry of a compactified direction.
- N. D. Birrell and P. C. W. Davies, *Quantum Fields in Curved Space* (Cambridge, 1982), for the Euclidean and thermal propagators and the periodicity in imaginary time.
- J. Zinn-Justin, *Quantum Field Theory and Critical Phenomena* (Oxford, 2002), for the Euclidean functional integral at finite temperature.
- Companion articles: *The KMS Condition and the Biquaternion Framework*, for the modular Hamiltonian and the analytic strip; *The Unruh Effect in Biquaternionic Form* and *Hawking Radiation in Biquaternionic Form*, for the thermal states and the temperatures this formalism reproduces; *The Spin–Statistics Theorem in Biquaternionic Form*, for the periodic/antiperiodic split; *The Functional Integral in Biquaternionic Form* and *The Generating Functional and the Effective Action in Biquaternionic Form*, for the Euclidean integral and its one-loop value; *The Feynman Propagator in Biquaternionic Form*, for the wave biquaternion and the analytic continuation; *The Bochner Theorem for the Biquaternion Transform: the Hermitian Form and the Root*, for the positivity of the thermal correlator at the central root; *The Wick Rotation in the Biquaternion Universe*, for the standard rotation kept in view in the first section and not used in the body.
