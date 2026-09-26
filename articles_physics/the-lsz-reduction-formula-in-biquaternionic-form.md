# __The LSZ Reduction Formula in Biquaternionic Form__

## Introduction

The **LSZ reduction formula** (Lehmann, Symanzik, Zimmermann) expresses an S-matrix element as the on-shell residue of a time-ordered correlation function. It is the bridge between the vacuum expectation values that the functional integral produces and the scattering amplitudes that experiment measures. Schematically, for $n$ incoming and $m$ outgoing particles,
$$
\langle f|S|i\rangle
= \Big[\prod_{\text{legs}}\int d^4x_j\, e^{\pm ip_j\cdot x_j}\Big]
\Big[\prod_{\text{legs}}\big(\Box_j-m^2\big)\Big]
\big\langle 0\big|T\,\tilde\Phi(x_1)\cdots\tilde\Phi(x_n)\big|0\big\rangle
\Big|_{\text{on shell}},
$$
with a wave-function renormalization factor $Z^{-1/2}$ per leg. The two operations are *Fourier transform* and *amputate*: put each external leg on the mass shell and replace the propagator that carried it by the free plane wave. The companion article *The S-Matrix in Biquaternionic Form* uses this reduction and records that it is not rederived there; this article supplies the derivation in the framework's terms.

The findings are these.

- **Established (algebra).** The mass shell is the zero set of the **central mass-shell operator**
$$
\mathcal{M}(\tilde k) = \tilde k\bar{\tilde k}+m^2 ,
\qquad
\mathcal{M}(\tilde k)=0 \iff \tilde k\bar{\tilde k}=-m^2 \iff E_{\mathbf p}^2=\mathbf p^2+m^2 ,
$$
with the wave biquaternion $\tilde k=iEe_0+\mathbf p$ and its quaternion conjugate $\bar{\tilde k}=iEe_0-\mathbf p$. The product is central, $\tilde k\bar{\tilde k}=(-E^2+\mathbf p^2)e_0=-p^2e_0$, so the mass shell is a **level set of the norm form**. Amputation is multiplication by the inverse propagator, the central mass-shell operator $\mathcal{M}(\tilde k)=\tilde k\bar{\tilde k}+m^2=m^2-p^2$, with $D_F=1/\mathcal{M}(\tilde k)$ up to the $i\epsilon$; it is therefore a central scalar operation for a scalar field, and it commutes with everything.
- **Established (algebra).** The wave-function renormalization is the residue at the norm-form pole,
$$
Z = \lim_{p^2\to m^2}\big(m^2-p^2\big)\,D_F(p^2),
$$
and for a central scalar operator on the biquaternion module the residue is the module residue, so each external leg carries $\sqrt{Z}$ with $Z$ the module value. This was checked on an explicit propagator with a nonzero residue and a regular part.
- **Established (algebra).** For a **scalar** biquaternion field the reduction's kinematics is block diagonal with respect to the sector split, because the mass-shell operator is central and the external wavefunctions are central-phase plane waves; the amputation commutes with the sector projections, and the two sectors are related by multiplication by the central $i$ rather than being independent field copies. For a **spinor** field the amputation operator $\not p-m$ is matrix-valued and non-central, and the external legs are the spinors $u^{(r)},v^{(r)}$ of *The Feynman Propagator in Biquaternionic Form*; the reduction does not factor.
- **One-mode truncation.** Conditional on the one-mode identification of *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*, the LSZ reduction for a single mode is a $2\times2$ matrix statement, and the algebra hosts at most that one mode. The field-level reduction is an operation on the module, not an element of $\mathbb{B}$; the same module gap that the S-matrix, Fock, and Bogoliubov articles record.
- **Standard, and transcribed.** The derivation of LSZ from the asymptotic conditions, the adiabatic switching, the $Z$ factors, the free-field limit, and the momentum-conservation delta functions. The algebra supplies the mass-shell symbol and the plane waves, not the reduction theorem.

The article proceeds as follows. The next section states the LSZ formula and sketches its derivation from asymptotic fields. A section identifies the amputation with the inverse mass-shell operator. A section fixes the external wavefunctions as biquaternion plane waves. A section treats the wave-function renormalization as a residue, verified numerically. A section treats the scalar and spinor cases separately, and a section the one-mode truncation and the module gap. A section separates what is established from what is interpretation.

**Conventions.** We use those of the companion articles, in particular *The S-Matrix in Biquaternionic Form* and *The Feynman Propagator in Biquaternionic Form*. The algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, and central scalar imaginary $i$. The biquaternionic gradient is $\tilde\nabla=e_0\partial_{ict}+e_1\partial_x+e_2\partial_y+e_3\partial_z$ with $\Box=\tilde\nabla\bar{\tilde\nabla}=\partial_{ict}^2+\Delta$; the $ict$ metric is $\eta=\mathrm{diag}(-1,+1,+1,+1)$. The wave biquaternion is $\tilde k=iEe_0+\mathbf p$ with **quaternion** conjugate $\bar{\tilde k}=iEe_0-\mathbf p$ and $\tilde k\bar{\tilde k}=(-E^2+\mathbf p^2)e_0=-p^2e_0$, where $p^2=E^2-\mathbf p^2$; the mass shell is $\tilde k\bar{\tilde k}=-m^2c^2/\hbar^2$ (in the dynamical expressions we set $\hbar=c=1$). On the spinor module the Dirac operator is $\not p-m$ with $\not p=\gamma^0E-\boldsymbol\gamma\cdot\mathbf p$, the Clifford metric $g=\mathrm{diag}(+1,-1,-1,-1)$, and $\eta=-g$. The mode algebra is $\{\hat a_r(\mathbf p),\hat a_s^\dagger(\mathbf q)\}=(2\pi)^3\delta_{rs}\delta^{(3)}(\mathbf p-\mathbf q)$, with all other anticommutators zero; the matrix isomorphism is $\Phi(e_k)=-i\sigma_k$; the trace pairing is $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$.

## The LSZ Formula

The reduction is a statement about the asymptotic behaviour of correlation functions, and it is worth stating the logic before using it.

**Asymptotic fields.** A renormalized field $\tilde\Phi$ is supposed to approach, at early and late times, a free field of the same mass,
$$
\tilde\Phi(x) \;\xrightarrow{\ t\to\pm\infty\ }\; \sqrt{Z}\,\tilde\Phi_{\mathrm{in/out}}(x) ,
$$
where $\tilde\Phi_{\mathrm{in/out}}$ is a free field and $Z$ is the wave-function renormalization. The adiabatic switching of the interaction makes the approach weak, and the reduction formula is the statement that the S-matrix element can be written entirely in terms of the interpolating field's correlation functions.

**The formula.** For $n$ incoming particles of momenta $p_1,\dots,p_n$ and $m$ outgoing of momenta $p'_1,\dots,p'_m$,
$$
\langle \mathbf p'_1\cdots\mathbf p'_m|S|\mathbf p_1\cdots\mathbf p_n\rangle
= \Big[\prod_{j=1}^{m}\int d^4x'_j\,e^{ip'_j\cdot x'_j}\Big]
\Big[\prod_{i=1}^{n}\int d^4x_i\,e^{-ip_i\cdot x_i}\Big]
\Big[\prod_{\text{all legs}}\big(\Box-m^2\big)\Big]
\big\langle 0\big|T\,\tilde\Phi(x'_1)\cdots\tilde\Phi(x_1)\cdots\big|0\big\rangle ,
$$
up to the factors of $\sqrt Z$ and the normalization of the asymptotic states. Each external leg is Fourier-transformed with its plane-wave phase and acted on by the wave operator, and the result is evaluated with all external momenta **on the mass shell**; off-shell the amplitude is defined by the un-amputated correlation function, and the two agree at the pole.

**Why amputation works.** The reason the formula holds is that the two-point function has a pole at the mass shell,
$$
D_F(p^2) = \frac{Z}{m^2-p^2-i\epsilon} + \text{regular} = -\,\frac{Z}{p^2-m^2+i\epsilon} + \text{regular},
$$
so multiplying by $\mathcal{M}(p^2)=m^2-p^2$, equivalently by $-(p^2-m^2)$, and going on shell extracts the residue $Z$, while the same multiplication on an external leg of a general correlator amputates exactly the propagator that leg carried and leaves the amputated (1PI) amplitude. The residue is the wave-function renormalization, and the $\sqrt Z$ per leg combines with the residue to give the physical normalization. All of this is standard (Lehmann–Symanzik–Zimmermann; see also the textbook derivations cited), and it is transcribed rather than rebuilt.

**The biquaternion form of the amputation.** In the framework the wave operator is the series one, $\Box-m^2$, and its momentum symbol is the negative of the central mass-shell operator,
$$
\big(\Box-m^2\big) \;\longrightarrow\; -\,\mathcal{M}(\tilde k)=-\big(\tilde k\bar{\tilde k}+m^2\big)=p^2-m^2 ,
$$
so the amputation is multiplication by the inverse propagator $\mathcal{M}(\tilde k)$ in momentum space, equivalently by the negative of the wave operator's symbol. The mass-shell operator $\mathcal{M}(\tilde k)=\tilde k\bar{\tilde k}+m^2=m^2-p^2$ is the object whose vanishing is the shell, $\mathcal{M}(\tilde k)=0$, i.e. $\tilde k\bar{\tilde k}=-m^2$. The remaining sections spell out the consequences of the fact that $\mathcal{M}$ is a *central* scalar for a scalar field and a *matrix* for a spinor field.

<!-- CONVENTION — LSZ wave operator: the wave operator is written $(\Box-m^2)$ with the series d'Alembertian $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}=\partial_{ict}^2+\Delta$, so its momentum symbol is $p^2-m^2=-\mathcal{M}(\tilde k)$ with $\mathcal{M}(\tilde k)=\tilde k\bar{\tilde k}+m^2$; the textbook $(\Box+m^2)$ of the mostly-minus convention is the same operator up to the overall sign, $\Box_{\mathrm{textbook}}=-\Box_{\mathrm{series}}$, as *Conventions in the Biquaternion Universe* records. Do not "correct" $(\Box-m^2)$ to $(\Box+m^2)$ without changing the definition of $\Box$ with it. -->

## Amputation as the Inverse Mass-Shell Operator

The propagator and the mass-shell operator are algebraic inverses, and LSZ is the statement of that inversion.

**The inversion.** In momentum space the Feynman propagator is
$$
D_F(\tilde k) = \frac{1}{\mathcal{M}(\tilde k)-i\epsilon} = -\,\frac{1}{p^2-m^2+i\epsilon} ,
\qquad
\mathcal{M}(\tilde k) = \tilde k\bar{\tilde k}+m^2 = m^2-p^2 ,
$$
so that
$$
\mathcal{M}(\tilde k)\,D_F(\tilde k) = -\,\big(p^2-m^2\big)\,D_F(\tilde k) = 1 \qquad ({\epsilon\to0,\ \text{off shell}}).
$$
Multiplying a correlation function by $\mathcal{M}(\tilde k)$ on a leg is precisely the inverse operation to attaching the propagator to that leg. This is the whole content of "amputation", and in the framework it is the multiplication of a module-valued function by the central scalar $\mathcal{M}(\tilde k)$. This is the normalization of the propagator article, whose Klein–Gordon Green's function is $G_F=1/(\mathbf p^2+m^2-\omega^2-i\epsilon)=1/(\mathcal{M}-i\epsilon)$ with $(\Box-m^2)G_F=-\delta^{(4)}$, and in which the free-field residue is $+1$; the textbook normalization $1/(p^2-m^2+i\epsilon)$ is its negative.

**Centrality and commutation.** Because $\mathcal{M}(\tilde k)$ is central — it is a complex number times $e_0$ — the amputation commutes with the algebra's left and right multiplications and does not disturb any internal index. For a scalar field this means the amputation acts identically on both sectors and on all components; the operator can be moved freely past vertex factors, and the reduction is commutative with the internal symmetry structure. This is the algebraic statement behind the factorized kinematics of the next-but-one section.

**The pole set is a norm-form level set.** The mass shell $\mathcal{M}(\tilde k)=0$ is the statement $\tilde k\bar{\tilde k}=-m^2$, a level set of the norm form. For $m=0$ it is the zero set of the norm form, i.e. the zero-divisor cone, the light cone of *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*. The reduction formula thus places the external legs on a level set of the same norm form that determines the algebra's singular elements, the metric, and the zero-divisor cone; the mass shell and the light cone are the $m\ne0$ and $m=0$ members of one family.

**Verification.** With $m=0.7$, $\mathbf p=(0.3,-0.9,1.1)$ and $E_{\mathbf p}=\sqrt{\mathbf p^2+m^2}=1.6124515497$, the wave biquaternion gives
$$
\tilde k\bar{\tilde k} = -E^2+\mathbf p^2 = -0.490000
= -m^2 ,
$$
agreeing with $-m^2=-0.49$ to machine precision. The on-shell condition and the norm-form statement are thus the same equation, checked on a momentum not used to construct any other result.

## The External Wavefunctions

The external legs carry the framework's plane waves, and this is where the reduction meets the algebra's complex structure.

**Central-phase plane waves.** The biquaternion plane wave
$$
\tilde\Phi_{\tilde k}(\tilde X) = \tilde w\,e^{\,i\,\mathrm{Sc}(\bar{\tilde k}\tilde X)} ,
\qquad
\tilde X = ict\,e_0+\mathbf x ,
$$
with $\tilde w$ a constant biquaternion amplitude, satisfies $(\Box-m^2)\tilde\Phi_{\tilde k}=0$ for $\tilde k\bar{\tilde k}=-m^2$, because the differential operator is central and acts on the exponential as multiplication by $-(\tilde k\bar{\tilde k}+m^2)=-\mathcal{M}(\tilde k)$. The phase is the central scalar $\mathrm{Sc}(\bar{\tilde k}\tilde X)=p\cdot x$, so the wave is a **central-phase** plane wave: its phase is a complex number and not a biquaternion, which is the reason the framework's free modes are the ordinary plane waves of the standard theory. This is the same statement that the path-integral and functional-integral articles make about the phase being central.

**The one-particle states.** The asymptotic states are one-particle states of the Fock module of *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*, labeled by on-shell momenta and by the internal (spinor or helicity) label carried by the module. The external wavefunction is the module vector $\tilde w$ times the central phase, and the LSZ integral projects a correlation function onto that module vector.

**Momentum conservation.** The integrals over the leg positions produce the momentum-conserving delta function
$$
(2\pi)^4\delta^{(4)}\Big(\sum p_i-\sum p'_j\Big),
$$
which is unaffected by the algebra; it is a property of the Fourier transform. In the biquaternion form the conserved quantity is the central scalar four-momentum, i.e. the $e_0$-coefficient pairing of $\tilde k$ with its conjugate, which is the same as the standard four-momentum.

## Wave-Function Renormalization as a Residue

The factor $Z$ that LSZ requires is the residue of the propagator at the norm-form pole, and the framework's account of it is the residue of a central scalar function.

**Definition.** Writing the momentum-space two-point function near the mass shell as
$$
D_F(p^2) = \frac{Z}{m^2-p^2-i\epsilon}+c_0+c_1\,(m^2-p^2)+\cdots ,
$$
the wave-function renormalization is
$$
Z = \lim_{p^2\to m^2}\big(m^2-p^2\big)\,D_F(p^2) = \lim_{\mathcal{M}\to0}\mathcal{M}(\tilde k)\,D_F ,
$$
the coefficient of the simple pole. In the framework the pole is at $\mathcal{M}(\tilde k)=0$, i.e. at $p^2=m^2$; the residue is a central scalar, and the physical normalization is $\sqrt Z$ per external leg.

**Free field.** For the free field $Z=1$: the two-point function is the free propagator $D_F=1/(\mathcal{M}-i\epsilon)$, and the amputated two-point function is the constant $1$, which is LSZ's statement that the free S-matrix is the identity. This was checked directly: multiplying the free $D_F$ by $\mathcal{M}=m^2-p^2$ and cancelling gives $1$ exactly.

**Interacting field, checked.** For the model propagator
$$
D(\mathcal{M}) = \frac{Z}{\mathcal{M}}+c_0+c_1\mathcal{M},
\qquad Z=2.3,\ c_0=0.4,\ c_1=-0.7,\ m=0.7,
$$
with $\mathcal{M}=m^2-p^2$, the residue was computed from both sides of the pole,
$$
\lim_{\delta\to0^\pm}\big(\delta\big)\,D(\delta) = 2.3000004, \quad 2.2999996 ,
$$
approaching $Z=2.3$ as the step is refined. The residue is insensitive to the regular part and to the direction of approach, as it must be; the framework's contribution is that the pole is the norm-form condition and the residue is central.

**Sector splitting of $Z$.** For a scalar field whose self-energy is sector-diagonal, the two-point function is the sum of the sector two-point functions, $D_F=D_{F-}+D_{F+}$, since the cross terms vanish by the sector orthogonality of the real form; each sector carries its own residue, and the total residue is the sum $Z=Z_-+Z_+$. Each external leg then carries a $\sqrt{Z_\pm}$ from the sector it propagates in, and the amplitude's normalization is the product of those factors along the legs. For a non-central self-energy — a fermion loop coupling the chiralities — $Z$ does not split and the residue is a matrix in the internal space.

## The Scalar and Spinor Reductions

The two cases differ in exactly one place: whether the amputation operator is central.

**Scalar case: block diagonality.** For a scalar biquaternion field the mass-shell operator $\mathcal{M}(\tilde k)$ is central, the external wavefunctions are central-phase plane waves with module-valued amplitudes, and the amputation commutes with the sector projections. The reduction's kinematics is therefore block diagonal with respect to the sector split: the amputation acts on each sector's part of a correlation function independently, and the sector parts are related by the central $i$ rather than being independent fields. This is the LSZ counterpart of the block-diagonal quadratic form of the functional integral and the effective action. Its content is a component count: the biquaternion scalar's four real components per sector enter the reduction separately, and the algebra fixes the split. It is **not** a statement that a biquaternion scalar is a multiplicity of complex scalars, for the reason the functional-integral and harmonic-oscillator articles give.

**Spinor case: no factorization.** For a spinor field the amputation operator is the matrix $\not p-m$, which is not central; it acts on the spinor module and mixes the two chiralities through the mass. The external legs are the spinors $u^{(r)}(\mathbf p)$ and $v^{(r)}(\mathbf p)$ of the propagator article, with the spin sums $\sum_r u^{(r)}\bar u^{(r)}=\not p+m$ and $\sum_r v^{(r)}\bar v^{(r)}=\not p-m$; the reduction reads
$$
\langle f|S|i\rangle_{\text{spinor}}
= \Big[\prod_{\text{legs}}\int d^4x_j\,e^{\pm ip_j\cdot x_j}\Big]
\Big[\prod_{\text{legs}}\big(i\not\partial_j-m\big)\Big]
\big\langle 0\big|T\,\tilde\Psi(x_1)\cdots\bar{\tilde\Psi}(x_n)\big|0\big\rangle\Big|_{\text{on shell}} ,
$$
with the $\bar{\tilde\Psi}$ legs amputated by $i\not\partial+m$. The operator is now a matrix and the reduction does not factorize; the internal indices of the module are contracted with the external spinors. This is the standard spinor LSZ formula, and the framework's contribution is the module on which the spinors live and the chirality-off-diagonal form of the mass.

**A consistency check.** The spin sums and the relation $(\not p-m)(\not p+m)=(p^2-m^2)I_4$, which the propagator article verifies, are exactly what makes the spinor amputation extract the residue: the matrix $(i\not\partial-m)$ inverts the spinor propagator's numerator structure. The framework adds nothing to this identity; it identifies the module and the mass operator.

## The One-Mode Truncation and the Module Gap

Conditional on the one-mode identification of the Fock article, the reduction has a finite-dimensional shadow.

**The one-mode statement.** For a single fermionic mode the field $\tilde\Phi$ is replaced by the ladder $\tilde a_{\mathrm{tr}}$ and its conjugate, the correlation functions by traces over the module, and the reduction becomes the matrix statement that the on-shell residue of the one-mode propagator is the identity of the mode algebra. Concretely, the one-mode two-point operators and their vacuum expectations are
$$
\tilde a_{\mathrm{tr}}\tilde a_{\mathrm{tr}}^\dagger = P_+(e_3),
\qquad
\tilde a_{\mathrm{tr}}^\dagger\tilde a_{\mathrm{tr}} = P_-(e_3),
\qquad
\big\langle \tilde a_{\mathrm{tr}}\tilde a_{\mathrm{tr}}^\dagger\big\rangle_0 = 1,
\qquad
\big\langle \tilde a_{\mathrm{tr}}^\dagger\tilde a_{\mathrm{tr}}\big\rangle_0 = 0 ,
$$
so the two operators are the pair of minimal idempotents — the empty and the occupied projector — their vacuum expectations are the free one-mode two-point functions, and the amputation is the algebra's identity $e_0$; the one-mode reduction therefore reproduces the free result $Z=1$. This is the finite-dimensional instance of LSZ, and it is exact rather than approximate.

**The gap.** The S-matrix of a *field* is an operator on an infinite-dimensional Fock space, and the LSZ reduction is a statement about that operator; neither is an element of $\mathbb{B}$. The algebra provides the mass-shell symbol, the plane waves, and the internal module of the external legs; it does not provide the reduction theorem, which is a statement about the asymptotics of an infinite-dimensional theory. This is the same module gap as in the Fock, S-matrix, Wick, and Bogoliubov articles, here located at the step where the external legs are placed on shell.

## The Reduction from the Functional Integral

The reduction can be read off the source derivative of the generating functional, and in the framework the source is module-valued.

Add to the action a source term $\int\langle\tilde J,\tilde\Phi\rangle$ whose Fourier transform has a pole at the mass shell,
$$
\tilde J_{\tilde k} = \frac{\sqrt Z\,\tilde j_{\tilde k}}{\mathcal{M}(\tilde k)-i\epsilon} = \frac{\sqrt Z\,\tilde j_{\tilde k}}{m^2-p^2-i\epsilon} ,
\qquad
\tilde j_{\tilde k}\ \text{regular on shell},
$$
and take the source-derivative of $W[\tilde J]$. The derivative $\delta W/\delta\tilde J_{\tilde k}$ is the classical field of the effective-action article; its one-particle part is extracted by the residue of the source's pole, and the residue is exactly the wave-function renormalization $\sqrt Z$. The reduction formula is the statement that this extraction commutes with the Fourier transform of the leg positions:
$$
\langle f|S|i\rangle
= \Big[\prod_{\text{legs}}\Big(\lim_{\mathcal{M}(\tilde k_j)\to0}\mathcal{M}(\tilde k_j)\Big)\Big]
\frac{\delta^{\,n}W}{\delta\tilde J_1\cdots\delta\tilde J_n}\Big|_{\tilde J=0},
$$
where the on-shell limit is the biquaternion mass-shell condition and the residues are the $\sqrt Z$ factors. Reading the formula this way separates what the algebra supplies — the module-valued source, the central mass-shell operator, the residues — from what is the standard LSZ theorem: that the on-shell residue of the source derivative is the physical amplitude, which rests on the asymptotic conditions and is not an algebraic fact.

## The Spectral Representation and the Residue

The residue $Z$ is the one-particle weight in the **Källen–Lehmann spectral representation**, and the framework's spectral function is a sum over the module's states.

Insert a complete set of intermediate states into the two-point function; the standard result is
$$
D_F(p^2) = \int_0^\infty \frac{d\mu^2}{2\pi}\,\frac{\rho(\mu^2)}{\mu^2-p^2-i\epsilon} = -\int_0^\infty \frac{d\mu^2}{2\pi}\,\frac{\rho(\mu^2)}{p^2-\mu^2+i\epsilon},
\qquad
\rho(\mu^2) = (2\pi)\sum_n \big|\langle n|\tilde\Phi(0)|0\rangle\big|^2\,\delta(\mu^2-m_n^2)\ \ge 0 ,
$$
with the sum over all intermediate states of mass $m_n$. The spectral function is non-negative — a consequence of the positivity of the state space — and the one-particle contribution is a delta function at the physical mass whose coefficient is $Z$:
$$
\rho(\mu^2) = 2\pi\,Z\,\delta(\mu^2-m^2) + \rho_{\mathrm{continuum}}(\mu^2).
$$
The residue of the pole is thus the one-particle weight, and the continuum's threshold is the multiparticle branch point. This is standard (Källen 1952, Lehmann 1954) and is cited.

**Biquaternion content.** The intermediate states are states of the Fock module of *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*, and the matrix element $\langle n|\tilde\Phi(0)|0\rangle$ is a module-valued amplitude whose norm enters. The one-particle contribution is the module vector projected onto the on-shell momentum, i.e. the external wavefunction of the previous section; the residue $Z$ is its norm squared. For a scalar field with sector-diagonal self-energy the spectral function splits into the two sectors' contributions, $\rho=\rho_-+\rho_+$, consistent with $Z=Z_-+Z_+$. The positivity of $\rho$ is the positivity of the inner product of the state space, which the GNS article constructs; the spectral representation is thus where the LSZ residue and the state-space positivity meet.

## What Is Established and What Is Interpretation

**Established (algebra).**
- The mass shell is the norm-form level set $\tilde k\bar{\tilde k}=-m^2$, equivalently $\mathcal{M}(\tilde k)=\tilde k\bar{\tilde k}+m^2=0$; checked numerically ($-0.490000$ versus $-m^2=-0.49$).
- Amputation is multiplication by the central mass-shell operator $\mathcal{M}(\tilde k)$, the inverse of the propagator; on shell it vanishes.
- The wave-function renormalization is the residue at the norm-form pole; checked for a model propagator ($Z=2.3$ recovered from both sides) and for the free field ($Z=1$, amputated two-point function $1$).
- For a scalar field the reduction's kinematics is block diagonal with respect to the sector split; for a spinor field it is not, because the amputation operator is not central.
- The one-mode truncation gives the exact free result $Z=1$ with the correlation functions the minimal idempotents.

**Standard, and transcribed.**
- The LSZ theorem itself: the asymptotic conditions, adiabatic switching, the derivation from the interpolating field, the $\sqrt Z$ factors, the momentum-conservation delta functions, and the spinor reduction formula.

**Interpretation.**
- Reading the mass shell as a level set of the norm form, so that the massless case is the zero-divisor cone, is the framework's own identification; it is consistent with the material-sector article.
- The factorization in the scalar case is the LSZ counterpart of the functional-integral factorization; stated as such.

**Open.**
- The framework has no independent derivation of the asymptotic conditions; they are assumed as in the standard theory.
- Whether the sector block structure of the scalar reduction has observable consequences is a spin-0-article question; this article only identifies the block structure.

## Summary

The LSZ reduction in biquaternionic form is the standard reduction with the framework's mass-shell symbol. The mass shell is the norm-form level set
$$
\tilde k\bar{\tilde k}=-m^2
\qquad\Longleftrightarrow\qquad
\mathcal{M}(\tilde k)=\tilde k\bar{\tilde k}+m^2=0 ,
\qquad
\tilde k\bar{\tilde k}=(-E^2+\mathbf p^2)e_0=-p^2e_0 ,
$$
verified as $-0.490000=-m^2$ for $m=0.7$, $\mathbf p=(0.3,-0.9,1.1)$. Amputation is multiplication by the central mass-shell operator $\mathcal{M}(\tilde k)$, the inverse of the propagator $D_F=1/(\mathcal{M}-i\epsilon)$; the wave-function renormalization is the residue at the norm-form pole, checked to give $Z=2.3$ for a model propagator and $Z=1$ for the free field, where the amputated two-point function is exactly $1$. For a scalar biquaternion field the reduction's kinematics is block diagonal with respect to the sector split; for a spinor field the matrix amputation $\not p-m$ is non-central, the legs are the spinors $u^{(r)},v^{(r)}$ with $\sum_r u^{(r)}\bar u^{(r)}=\not p+m$, and the reduction does not factor.

The reduction theorem itself — the asymptotic conditions, the adiabatic switching, the $\sqrt Z$ normalization — is standard and transcribed. The algebra supplies the mass-shell symbol, the central-phase plane waves, and the internal module; the field-level S-matrix and its reduction live on the Fock module and not in $\mathbb{B}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $\tilde k=iEe_0+\mathbf p$, $\bar{\tilde k}=iEe_0-\mathbf p$ | Wave biquaternion and its quaternion conjugate |
| $\tilde k\bar{\tilde k}=(-E^2+\mathbf p^2)e_0=-p^2e_0$ | Central norm form; $p^2=E^2-\mathbf p^2$ |
| $\mathcal{M}(\tilde k)=\tilde k\bar{\tilde k}+m^2=m^2-p^2$ | Mass-shell operator (vanishing defines the shell) |
| $\mathcal{M}(\tilde k)=0\iff E_{\mathbf p}^2=\mathbf p^2+m^2$ | Mass shell |
| $\Box=\tilde\nabla\bar{\tilde\nabla}=\partial_{ict}^2+\Delta$ | d'Alembertian, series convention |
| $\eta=\mathrm{diag}(-1,+1,+1,+1)$ | $ict$ metric (level 2) |
| $D_F(\tilde k)=1/(\mathcal{M}(\tilde k)-i\epsilon)=-1/(p^2-m^2+i\epsilon)$ | Feynman propagator (momentum space) |
| $p^2-m^2=-\mathcal{M}(\tilde k)$ | Symbol of the wave operator $(\Box-m^2)$; amputation uses $\mathcal{M}$ |
| $Z=\lim_{p^2\to m^2}(m^2-p^2)D_F(p^2)=\lim_{\mathcal{M}\to0}\mathcal{M}D_F$ | Wave-function renormalization (residue) |
| $\langle f|S|i\rangle$ | S-matrix element from the reduction |
| $e^{\,i\,\mathrm{Sc}(\bar{\tilde k}\tilde X)}=e^{\,ip\cdot x}$ | Central-phase plane wave (external leg) |
| $\not p=\gamma^0E-\boldsymbol\gamma\cdot\mathbf p$ | Spinor mass-shell operator |
| $u^{(r)},v^{(r)}$ | External spinors; $\sum_r u^{(r)}\bar u^{(r)}=\not p+m$ |
| $Z=Z_-+Z_+$ | Scalar-sector splitting of the residue (sum) |

## Further Reading

- H. Lehmann, K. Symanzik, and W. Zimmermann, "Zur Formulierung quantisierter Feldtheorien," *Il Nuovo Cimento* **1** (1955) 205–225, for the original reduction formula.
- H. Lehmann, K. Symanzik, and W. Zimmermann, "On the formulation of quantized field theories. II," *Il Nuovo Cimento* **6** (1957) 319–333, for the extension and the renormalization constants.
- G. Källén, "On the definition of the renormalization constants in quantum electrodynamics," *Helvetica Physica Acta* **25** (1952) 417–434, for the spectral representation of the propagator.
- H. Lehmann, "Über Eigenschaften von Ausbreitungsfunktionen und Renormierungskonstanten quantisierter Felder," *Il Nuovo Cimento* **11** (1954) 342–357, for the positivity of the spectral function and the one-particle weight.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Fields* (McGraw-Hill, 1965), for the derivation of the reduction formula and the spinor case.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the reduction formula in the convention used here.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the asymptotic conditions and the derivation of the reduction theorem.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the reduction formula, the wave-function renormalization, and the spinor amplitudes.
- R. Haag, *Local Quantum Physics* (Springer, 1996), for the field-theoretic setting in which the asymptotic conditions are formulated.
- J. Zinn-Justin, *Quantum Field Theory and Critical Phenomena* (Oxford, 2002), for the reduction and the residue of the propagator.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the spinor module on which the matrix amputation acts.
- Companion articles: *The S-Matrix in Biquaternionic Form*, for the S-matrix and the external data whose reduction this article supplies; *The Feynman Propagator in Biquaternionic Form*, for the wave biquaternion, the mass shell, and the spinors; *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*, for the one-particle states and the one-mode truncation; *The Functional Integral in Biquaternionic Form* and *The Generating Functional and the Effective Action in Biquaternionic Form*, for the correlation functions being reduced; *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, for the norm form and the zero-divisor cone.
