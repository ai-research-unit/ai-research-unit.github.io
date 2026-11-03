# __The LSZ Reduction Formula in Biquaternionic Form__

## Introduction

The **LSZ reduction formula** (Lehmann, Symanzik, Zimmermann) expresses an S-matrix element as the on-shell residue of a time-ordered correlation function. It is the bridge between the vacuum expectation values that the functional integral produces and the scattering amplitudes that experiment measures. Natural units $\hbar=c=1$ are used. The wave biquaternion is $\tilde P=iEe_t+\vec p$, where $E=p_0$ is the energy component, on or off the shell, and $E_{\vec p}=\sqrt{\vec p^{\,2}+m^2}$ is its on-shell value; the mass shell is $\tilde P\tilde P^{\natural}=-m^2$, that is $E=E_{\vec p}$. For $n$ incoming and $m$ outgoing particles the formula is, schematically,

$$
\boxed{\;
\begin{aligned}
&\langle p_{n+1}\cdots p_{n+m}|S|p_1\cdots p_n\rangle\\[2pt]
&\quad=\Big[\prod_{j=n+1}^{n+m}\int d^4x_j\,\exp(ip_j\cdot x_j)\Big]
\Big[\prod_{i=1}^{n}\int d^4x_i\,\exp(-ip_i\cdot x_i)\Big]\\[2pt]
&\quad\qquad\times\Big[\prod_{j=1}^{n+m}\big(\Box_j-m^2\big)\Big]
\big\langle 0\big|T\,\tilde\Phi(x_1)\cdots\tilde\Phi(x_{n+m})\big|0\big\rangle\Big|_{\text{on shell}},
\end{aligned}
\;}
$$

with a factor $Z^{-1/2}$ per external leg. Four operations are at work: Fourier transform each leg with its plane-wave phase, amputate it by the wave operator, put every external momentum on the mass shell, and divide by $\sqrt Z$ per leg. The companion article *The S-Matrix in Biquaternionic Form* uses this reduction and records that it is not rederived there; this article supplies the derivation in the framework's terms.

The findings are these.

- **Established (algebra).** The mass shell is the zero set of the **central mass-shell operator**
$$
\mathcal{M}(\tilde P)=\tilde P\tilde P^{\natural}+m^2=(-E^2+\vec p^{\,2})+m^2=m^2-p^2,
\qquad
\mathcal{M}(\tilde P)=0\iff p^2=m^2\iff E_{\vec p}^2=\vec p^{\,2}+m^2,
$$
with the wave biquaternion $\tilde P=iEe_t+\vec p$ and its quaternion conjugate $\tilde P^{\natural}=iEe_t-\vec p$. The sign comes from the central unit, $(iE)^2=i^2E^2=-E^2$, and $\vec p^{\,2}=p_x^2+p_y^2+p_z^2$ is the Euclidean square: the quaternion square is $\vec p\,\vec p=-\vec p^{\,2}$, which is why the product reads $-E^2+\vec p^{\,2}$ and not $-E^2-\vec p^{\,2}$. The product is central, $\tilde P\tilde P^{\natural}=(-E^2+\vec p^{\,2})e_t=-p^2e_t$, so the mass shell is a **level set of the biquaternion norm**.
- **Established (algebra).** For a scalar field, amputation is multiplication by $\mathcal{M}(\tilde P)$, the inverse of the propagator $D_F=1/(\mathcal{M}(\tilde P)-i\epsilon)$. On real momenta $\mathcal{M}$ is a **real** central scalar, so it multiplies all four complex components identically and commutes with the conjugation $\flat$, hence with the sector projections. Relative to the standard wave operator it carries a factor $-1$ per leg, which is a sign convention on the external states and not a physical difference.
- **Established (algebra).** The wave-function renormalization is the residue at the biquaternion-norm pole,
$$
Z=\lim_{p^2\to m^2}\big(m^2-p^2\big)\,D_F(p^2)=\lim_{\mathcal{M}\to0}\mathcal{M}(\tilde P)\,D_F,
$$
and the asymptotic field carries $\sqrt Z$ per leg, which is the factor the formula's $Z^{-1/2}$ removes. Checked on a model propagator with a nonzero residue and a regular part.
- **Established (algebra).** For a **scalar** biquaternion field the amputation is a real central scalar, so the reduction is one scalar reduction repeated on the four components, with no mixing; the two sectors are related by multiplication by the central $i$ rather than being independent field copies. For a **spinor** field the amputation is the cell $\mathcal{D}(p)-m$. Its pole is still the central scalar $p^2=m^2$; its residue is the cell $\mathcal{D}(p)+m$, which the spin sum writes as $\sum_r w^{(r)}\bar w^{(r)}$. The residue is therefore rank two, not scalar: a spinor leg is a sum of two spin-state reductions with a common pole, and the chirality is the cell that anticommutes with $\mathcal{D}(p)$ and commutes with the mass.
- **One-mode truncation.** Conditional on the one-mode identification of *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*, the LSZ reduction for a single mode is a $2\times2$ matrix statement, and the algebra hosts at most that one mode. The field-level reduction is an operation on the module, not an element of $\mathbb{B}$; the same module gap that the S-matrix, Fock, Wick, and Bogoliubov articles record.
- **Standard, and transcribed.** The derivation of LSZ from the asymptotic conditions, the adiabatic switching, the $Z$ factors, the free-field limit, and the momentum-conservation delta functions. The algebra supplies the mass-shell symbol and the plane waves, not the reduction theorem.

The article proceeds as follows. The next section states the formula and sketches its derivation from asymptotic fields. A section identifies the amputation with the inverse mass-shell operator. A section fixes the external wavefunctions as biquaternion plane waves. A section treats the wave-function renormalization as a residue, verified numerically. A section treats the scalar case and the spinor case, the latter with the two Dirac equations of the corpus and with the chirality split. A section treats the one-mode truncation and the module gap. Two sections treat the reduction from the functional integral and the spectral representation. A section separates what is established from what is interpretation, and the Gamma Formulation names the frame cells used in the body.

## The LSZ Formula

The reduction is a statement about the asymptotic behaviour of correlation functions, and it is worth stating the logic before using it.

**Asymptotic fields.** A renormalized field $\tilde\Phi$ is supposed to approach, at early and late times, a free field of the same mass,
$$
\tilde\Phi(x) \;\xrightarrow{\ t'\to\pm\infty\ }\; \sqrt{Z}\,\tilde\Phi_{\mathrm{in/out}}(x) ,
$$
where $\tilde\Phi_{\mathrm{in/out}}$ is a free field and $Z$ is the wave-function renormalization. The adiabatic switching of the interaction makes the approach weak, and the reduction formula is the statement that the S-matrix element can be written entirely in terms of the interpolating field's correlation functions.

**The formula.** With $G^{(n+m)}(x_1,\dots,x_{n+m})=\langle0|T\,\tilde\Phi(x_1)\cdots\tilde\Phi(x_{n+m})|0\rangle$ the position-space correlator, the content of the display of the Introduction is
$$
\langle f|S|i\rangle
= \Big[\prod_{\text{legs}}\int d^4x_j\,\exp(\pm ip_j\cdot x_j)\Big]
\Big[\prod_{\text{legs}}\big(\Box_j-m^2\big)\Big]
G^{(n+m)}(x_1,\dots,x_{n+m})\Big|_{\text{on shell}} ,
$$
the sign being $+$ on an outgoing leg and $-$ on an incoming one, with one factor $Z^{-1/2}$ per leg. Each external leg is Fourier-transformed with its plane-wave phase and acted on by the wave operator, and the result is evaluated with all external momenta **on the mass shell**. The amputated correlator is defined off the shell as well; what requires the shell is the identification of its residue with an S-matrix element.

**Why amputation works.** The two-point function has a pole at the mass shell,
$$
D_F(p^2) = \frac{Z}{m^2-p^2-i\epsilon} + \text{regular} = -\,\frac{Z}{p^2-m^2+i\epsilon} + \text{regular},
$$
so multiplying by $\mathcal{M}(p^2)=m^2-p^2$, equivalently by $-(p^2-m^2)$, and going on shell extracts the residue $Z$, while the same multiplication on an external leg of a general correlator amputates exactly the propagator that leg carried and leaves the amputated (1PI) amplitude. The residue is the wave-function renormalization. It is $Z=(\sqrt Z)^2$: one factor is the leg's overlap with the one-particle state, the other its coupling to the rest of the diagram. The formula's $Z^{-1/2}$ per leg removes the leg's own factor, so no $Z$ survives in the amplitude; the residue is the object that is measured, and it cancels out of the amplitude. All of this is standard (Lehmann–Symanzik–Zimmermann; see also the textbook derivations cited), and it is transcribed rather than rebuilt.

**The biquaternion form of the amputation.** The wave operator's momentum symbol is the negative of the central mass-shell operator,
$$
\big(\Box-m^2\big) \;\longrightarrow\; p^2-m^2 \;=\; -\big(\tilde P\tilde P^{\natural}+m^2\big) \;=\; -\,\mathcal{M}(\tilde P) ,
$$
so the amputation is multiplication by the inverse propagator $\mathcal{M}(\tilde P)$ in momentum space, equivalently by the negative of the wave operator's symbol. The two conventions differ by a factor $-1$ per leg, which is the same sign convention on the external states; no pole and no residue is affected. The mass-shell operator $\mathcal{M}(\tilde P)=\tilde P\tilde P^{\natural}+m^2=m^2-p^2$ is the object whose vanishing is the shell, $\mathcal{M}(\tilde P)=0$, i.e. $\tilde P\tilde P^{\natural}=-m^2$. The remaining sections spell out the consequence: the amputation *operator* is a real central scalar for a scalar field and a cell for a spinor field, while the pole $\mathcal{M}(\tilde P)=0$ is the same central scalar in both cases.

## Amputation as the Inverse Mass-Shell Operator

The propagator and the mass-shell operator are algebraic inverses, and LSZ is the statement of that inversion.

**The inversion.** In momentum space the Feynman propagator is
$$
D_F(\tilde P) = \frac{1}{\mathcal{M}(\tilde P)-i\epsilon} = -\,\frac{1}{p^2-m^2+i\epsilon} ,
$$
so that, off the shell and with the prescription removed,
$$
\boxed{\;\lim_{\epsilon\to0^{+}}\mathcal{M}(\tilde P)\,D_F(\tilde P) = \lim_{\epsilon\to0^{+}}\frac{m^2-p^2}{m^2-p^2-i\epsilon} = 1 \qquad (\mathcal{M}\neq0)\;}
$$
and with the prescription kept the same product is $1$ up to $O(\epsilon/\mathcal{M})$. Multiplying a correlation function by $\mathcal{M}(\tilde P)$ on a leg is precisely the inverse operation to attaching the propagator to that leg. This is the whole content of "amputation", and in the framework it is the multiplication of an algebra-valued function by the central scalar $\mathcal{M}(\tilde P)$. The normalization is the propagator article's. Its Klein–Gordon Green's function is $G_F=1/(\vec p^{\,2}+m^2-p_0^2-i\epsilon)=1/(\mathcal{M}-i\epsilon)$, which satisfies $(\Box-m^2)G_F=-\delta^{(4)}$ and whose free-field residue is $+1$; the textbook normalization $1/(p^2-m^2+i\epsilon)$ is its negative.

**The centrality is a real centrality.** Because $\mathcal{M}(\tilde P)$ is central, the amputation commutes with the left and right multiplications of the algebra and does not disturb any internal index; it multiplies every component of the field by the same complex number. On real momenta $\mathcal{M}=m^2-p^2$ is also **real**, and a real central scalar commutes with the conjugation $\flat=-{}^{*}$,
$$
\big(\mathcal{M}\tilde\Phi\big)^{\flat} = \bar{\mathcal{M}}\,\tilde\Phi^{\flat} = \mathcal{M}\,\tilde\Phi^{\flat},
$$
the twist of $\flat$ cancelling $\mathcal{M}^{\flat}=-\bar{\mathcal{M}}$ on a central factor, so it maps each sector into itself and commutes with the sector projections, $\big(\mathcal{M}\tilde\Phi\big)_{\pm}=\mathcal{M}\,\tilde\Phi_{\pm}$ with $\tilde\Phi_{\pm}=\tfrac12(\tilde\Phi\pm\tilde\Phi^{\flat})$ (the $+$ part is the one fixed by $\flat$, hence in $\mathbb{M}_-$). A central scalar that is not real does the opposite: the unit $i$ exchanges the two sectors, $i\,\mathbb{M}_{-}=\mathbb{M}_{+}$, because it flips the Hermiticity of an element. The $i\epsilon$ of the prescription is the one complex central factor in the operator: it displaces the pole, and being non-real it exchanges the sectors like the unit $i$ itself, so it does not split the field into two independent copies. This distinction — central for all, real for the split — is the algebraic content of the scalar reduction below.

**The pole set is a biquaternion-norm level set.** The mass shell $\mathcal{M}(\tilde P)=0$ is the statement $\tilde P\tilde P^{\natural}=-m^2$, a level set of the biquaternion norm. For $m=0$ it is the zero set of the biquaternion norm, i.e. the zero-divisor cone, the light cone of *The Material Sector: Four-Vectors, Interval and Lorentz Action*. The reduction formula thus places the external legs on a level set of the same biquaternion norm that determines the algebra's singular elements, the metric, and the zero-divisor cone; the mass shell and the light cone are the $m\ne0$ and $m=0$ members of one family. A numerical check with $m=0.7$ and $\vec p=(0.3,-0.9,1.1)$ gives $\vec p^{\,2}=2.11$ and $E_{\vec p}^2=2.60$, hence
$$
\tilde P\tilde P^{\natural} = (iE)^2+\vec p^{\,2} = -2.60+2.11 = -0.490000 = -m^2 ,
$$
agreeing with $-m^2=-0.49$ to machine precision. The on-shell condition and the biquaternion-norm statement are thus the same equation, checked at the corpus's test point, $m=0.7$ and $\vec p=(0.3,-0.9,1.1)$, which no other result of this article uses.

## The External Wavefunctions

The external legs carry the framework's plane waves, and this is where the reduction meets the algebra's complex structure.

**Central-phase plane waves.** The biquaternion plane wave
$$
\tilde\Phi_{\tilde P}(\tilde{R}) = \tilde Q^{\mathrm{amp}}\,\exp\big(\,i\,\mathrm{Sc}(\tilde P^{\natural}\tilde{R})\big) ,
\qquad
\tilde{R} = ict'\,e_t+x\,\vec e_x+y\,\vec e_y+z\,\vec e_z .
$$
Here $\tilde Q^{\mathrm{amp}}$ is a constant biquaternion amplitude, an element of $\mathbb{B}$ bound here, whose majuscule marks its complex scalar part. The differential operator is central and acts on the exponential as multiplication by its symbol, $\Box\to p^2=-\tilde P\tilde P^{\natural}$, so
$$
\big(\Box-m^2\big)\tilde\Phi_{\tilde P} \;\longrightarrow\; -\big(\tilde P\tilde P^{\natural}+m^2\big)\tilde\Phi_{\tilde P} = -\,\mathcal{M}(\tilde P)\,\tilde\Phi_{\tilde P},
$$
which vanishes for $\tilde P\tilde P^{\natural}=-m^2$. The phase is the central scalar $\mathrm{Sc}(\tilde P^{\natural}\tilde{R})=-p\cdot x$ with $p\cdot x=Et'-\vec p\cdot\vec x$, the corpus's four-vector notation, so $\exp(i\,\mathrm{Sc}(\tilde P^{\natural}\tilde{R}))=\exp(-ip\cdot x)$ is the positive-frequency mode and the wave is a **central-phase** plane wave: its phase is a complex number and not a biquaternion, which is the reason the framework's free modes are the ordinary plane waves of the standard theory. This is the same statement that the path-integral and functional-integral articles make about the phase being central. Being complex, the phase is central but not real: it multiplies every component by the same complex number, and because that number is not real it re-mixes the two sectors instead of preserving them, so the sector split is a split of the field and never of the phase.

**The one-particle states.** The asymptotic states are one-particle states of the Fock module of *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*, labeled by on-shell momenta and by the internal (spinor or helicity) label carried by the module. The external wavefunction is the constant amplitude $\tilde Q^{\mathrm{amp}}$ times the central phase; for a scalar field it is an element of $\mathbb{B}$, while for a spinor field the same slot carries the spinor $w^{(r)}$ of the spinor case below, bare by the rule that a spinor carries no tilde. The LSZ integral projects a correlation function onto that amplitude.

**Momentum conservation.** The integrals over the leg positions produce the momentum-conserving delta function
$$
(2\pi)^4\delta^{(4)}\Big(\sum p_i-\sum p_j\Big),
$$
which is unaffected by the algebra; it is a property of the Fourier transform. In the biquaternion form the conserved object is the wave biquaternion itself: the delta function equates the coefficient vectors of $\sum\tilde P_{\mathrm{in}}$ and $\sum\tilde P_{\mathrm{out}}$, and its four coefficients are the four conserved components, the $e_t$ coefficient being $iE$, so the equality of those coefficients is energy conservation, the central $i$ cancelling from both sides.

## Wave-Function Renormalization as a Residue

The factor $Z$ that LSZ requires is the residue of the propagator at the biquaternion-norm pole, and the framework's account of it is the residue of a central scalar function.

**Definition.** Writing the momentum-space two-point function near the mass shell as
$$
D_F(p^2) = \frac{Z}{m^2-p^2-i\epsilon}+c_0+c_1\,(m^2-p^2)+\cdots ,
$$
the wave-function renormalization is
$$
Z = \lim_{p^2\to m^2}\big(m^2-p^2\big)\,D_F(p^2) = \lim_{\mathcal{M}\to0}\mathcal{M}(\tilde P)\,D_F,
$$
the coefficient of the simple pole. In the framework the pole is at $\mathcal{M}(\tilde P)=0$, i.e. at $p^2=m^2$. For a scalar field the residue is a central scalar, real for real momenta; for a spinor field it is a cell, and the spinor section takes that case. The physical normalization is $\sqrt Z$ per external leg in either case.

**Free field.** For the free field $Z=1$: the two-point function is the free propagator $D_F=1/(\mathcal{M}-i\epsilon)$, and the amputated two-point function is the constant $1$: amputation removes the only propagator there was, so the free S-matrix is the identity. This was checked directly: multiplying the free $D_F$ by $\mathcal{M}=m^2-p^2$ and cancelling gives $1$, with a residual of order $\epsilon/|\mathcal{M}|$.

**Interacting field, checked.** For the model propagator
$$
D(\mathcal{M}) = \frac{Z}{\mathcal{M}}+c_0+c_1\mathcal{M},
\qquad Z=2.3,\ c_0=0.4,\ c_1=-0.7,\ m=0.7,
$$
with $\mathcal{M}=m^2-p^2$, the residue was computed from both sides of the pole. Since $\delta D(\delta)=Z+c_0\delta+c_1\delta^2$, a step $\delta=\pm10^{-6}$ gives
$$
\delta D(\delta)\big|_{\delta=+10^{-6}} = 2.3000004 ,
\qquad
\delta D(\delta)\big|_{\delta=-10^{-6}} = 2.2999996 ,
$$
approaching $Z=2.3$ from both sides as the step is refined, and the second-order term in the step is what the two values differ by. The residue is insensitive to the regular part and to the direction of approach, as it must be; the framework's contribution is that the pole is the biquaternion-norm condition and the residue is central.

**Sector splitting of $Z$.** For a scalar field whose self-energy commutes with $\flat$, the two-point function is block diagonal on the sector split, $D_F=D_{F-}+D_{F+}$, because a $\flat$-commuting operator has no cross part; each block carries its own residue, and the total residue is the sum $Z=Z_-+Z_+$. Each external leg then carries a $\sqrt{Z_\pm}$ from the sector it propagates in, and the amplitude's normalization is the product of those factors along the legs. For a self-energy with a part that does not commute with $\flat$ — one whose internal factor mixes the two chiralities, as a chirality-changing mass does — $Z$ does not split and the residue is a cell in the internal space. The assumption, not the algebra, is what produces the split: the algebra states that $\mathcal{M}$ is real central, and the split follows only for a dynamics that respects $\flat$.

## The Scalar and Spinor Reductions

The two cases differ in exactly one place: whether the amputation operator is a scalar or a cell.

**Scalar case: one scalar factor, four components.** For a scalar biquaternion field the amputation operator is the real central scalar $\mathcal{M}(\tilde P)$. It multiplies each of the four complex components of a correlation function by the same factor, so the reduction is component-wise: one scalar reduction, repeated four times, with no mixing and no preferred basis. The sector parts $\tilde\Phi_\pm$ are amputated by the same scalar, since $\mathcal{M}$ is real; the relation between the sectors remains multiplication by the central $i$, an isomorphism of real four-spaces and not a second, independent field. This is the LSZ counterpart of the central kinetic operator of the functional integral, which is also a single scalar multiplying every component. Its content is a component count: the biquaternion scalar's four complex components enter the reduction separately, and the algebra fixes nothing beyond that. It is **not** a statement that a biquaternion scalar is a multiplicity of complex scalars, for the reason the functional-integral and harmonic-oscillator articles give.

**Spinor case: the cell, and which Dirac equation.** For a spinor field the amputation operator is a cell, and the reduction must name the equation whose cell it is. Write $L_a\psi=a\psi$ and $R_b\psi=\psi b$ for the two multiplications of $\mathbb{B}$, and $L_aR_b$ for the cell $\psi\mapsto a\psi b$. The cells act on $\mathbb{B}$ read as a four-complex-dimensional module, which is the Dirac module $\Delta=S\oplus S^{\mathrm c}$, whose two summands are the two chiralities. The **momentum cell** is
$$
\mathcal{D}(p)=iL_{e_t}R_{\vec e_x}p_0-\sum_{k=x,y,z}iL_{\vec e_k}R_{\vec e_y}p_k ,
\qquad
\mathcal{D}(p)^2=p^2\,\mathbf{1} ,
\qquad
p^2=p_0^2-\vec p^{\,2},
$$
with $\mathbf{1}=L_{e_t}R_{e_t}$ the identity cell. Since $L_{e_t}$ is the identity map, the cell is the propagator article's momentum cell $iR_{\vec e_x}p_0-\sum_k iL_{\vec e_k}R_{\vec e_y}p_k$, with that identity written out. It is the momentum symbol of the pair operator $\mathbb{D}$ of *Conventions of the Operators and the Calculus*, $\mathbb{D}\Psi=(\tilde\nabla\tilde\Psi_R,\tilde\nabla^{\natural}\tilde\Psi_L)$ with $\mathbb{D}^2=\Box\,\mathbf{1}$; the operator $\mathcal{D}(p)-m$ is the symbol of the inverse propagator. The energy enters as the component $p_0=E$ and not as the on-shell value $E_{\vec p}$, because the amputation is an off-shell operation; the two coincide only on the shell. The signs are the frame's. The energy cell squares to $+1$ because $i^2=-1$ is met by $\vec e_x^2=-e_t$, and each spatial cell squares to $-1$ because the two quaternion squares give $(-e_t)(-e_t)=+e_t$ and the sign is the central $i^2$ alone.

**The two Dirac equations.** The corpus carries two, and they are not the same operator (see *The Dirac Equation in Biquaternionic Form*, §*The One-Sided and the Two-Sided Equation*). The **one-sided** form is the chiral pair
$$
\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L ,
\qquad
\tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R ,
$$
in which the gradient acts by left multiplication on the module and the mass is the off-diagonal pairing of the two chiral halves. The **two-sided** form is the single equation
$$
-\tilde\nabla^{\natural}F-m\,i\,\overline{F}\,\vec e_z=0 ,
$$
in which the time derivative and the spatial gradient act by left multiplication, the mass acts by right multiplication through $\vec e_z$, and the componentwise conjugation $\bar F$ supplies an antilinear part. The reduction of this article is the one-sided pair: it is the pair whose Green matrix the propagator article inverts, $(\mathbb{D}-m)\mathcal{S}=\delta I$ (the conventions article's $I$ is the identity cell written $\mathbf 1$ here), and whose momentum symbol is $\mathcal{D}(p)$. The two-sided equation is a change of representation, and its mass is a multiplication together with a conjugation rather than a multiplication alone; a reduction in that form would have to carry the conjugation through every leg, and the corpus does not attempt it.

**The pole is central; the residue is a cell.** On a central-phase plane wave $\tilde\nabla$ acts as left multiplication by $i\tilde P$ and $\tilde\nabla^{\natural}$ by $i\tilde P^{\natural}$, so the pair becomes
$$
i\tilde P\tilde\Psi_0^R=m\tilde\Psi_0^L ,
\qquad
i\tilde P^{\natural}\tilde\Psi_0^L=m\tilde\Psi_0^R .
$$
Eliminating one half, $\tilde P^{\natural}\tilde P\tilde\Psi_0^R=-m^2\tilde\Psi_0^R$, and since $\tilde P^{\natural}\tilde P=\tilde P\tilde P^{\natural}=-p^2$ is central, $(p^2-m^2)\tilde\Psi_0^R=0$. The second-order operator of the pair is therefore the central scalar of the scalar case: the pole of every spinor leg sits on the same biquaternion-norm level set $\mathcal{M}(\tilde P)=0$. What is not scalar is the residue. The inverse of the pair operator in momentum space is
$$
\big(\mathcal{D}(p)-m\big)^{-1}=\frac{\mathcal{D}(p)+m}{p^2-m^2}=\frac{\mathcal{D}(p)+m}{-\,\mathcal{M}(\tilde P)} ,
$$
so the residue of the propagator at $\mathcal{M}=0$ is the cell $\mathcal{D}(p)+m$, up to the overall $-i$, the product of the $-1$ in $\mathcal{M}=-(p^2-m^2)$ and the $i$ of the Feynman normalization. The spin-sum identity of the propagator article, which holds on the shell, writes that cell as a sum of two rank-one terms,
$$
\mathcal{D}(p)+m=\sum_{r=1}^{2}w^{(r)}(\vec p)\,\bar w^{(r)}(\vec p) ,
\qquad
\mathcal{D}(p)-m=\sum_{r=1}^{2}v^{(r)}(\vec p)\,\bar v^{(r)}(\vec p) ,
$$
the second being the numerator for a $\tilde\Psi^{\natural}$ leg. A spinor leg is thus a sum of two spin-state reductions with a common central pole: not one scalar reduction, and not an unfactorizable object either, since the cell factors into the two spin states. That factorization is what lets the reduction put one external spinor on each leg, $w^{(r)}$ on a positive-frequency leg and $v^{(r)}$ on a negative-frequency one, and the reduction reads
$$
\langle f|S|i\rangle_{\text{spinor}}
= \Big[\prod_{\text{legs}}\int d^4x_j\,\exp(\sigma_j ip_j\cdot x_j)\Big]
\Big[\prod_{\text{legs}}\big(\mathcal{D}_j-\varepsilon_j m\big)\Big]
\big\langle 0\big|T\,\tilde\Psi(x_1)\cdots\tilde\Psi^{\natural}(x_{n+m})\big|0\big\rangle\Big|_{\text{on shell}} ,
$$
with two independent signs per leg: $\sigma_j=+1$ on an outgoing leg and $-1$ on an incoming one, from the Fourier phase, and $\varepsilon_j=+1$ on a $\tilde\Psi$ leg and $-1$ on a $\tilde\Psi^{\natural}$ leg, from the numerator the leg carries. The two are unrelated: a $\tilde\Psi^{\natural}$ leg may be incoming or outgoing.

**Chirality.** The chirality is the cell $\chi_{\mathrm{c}}=-iL_{e_t}R_{\vec e_z}$, the representative of the central grading $\chi=i\tilde\Xi_{\mathrm{ad}}$ of *The Dirac Equation in Biquaternionic Form*, and the fifth cell of the frame written in the Gamma Formulation. It squares to the identity cell, and direct computation gives
$$
\{\chi_{\mathrm{c}},\mathcal{D}(p)\}=0 ,
\qquad
[\chi_{\mathrm{c}},m\,\mathbf{1}]=0 .
$$
The momentum cell is therefore chirality-off-diagonal and the mass is chirality-diagonal: with $P_\pm=\tfrac12(\mathbf 1\pm\chi_{\mathrm{c}})$, one has $\mathcal{D}(p)P_+=P_-\mathcal{D}(p)$, and the equation $\mathcal{D}(p)\psi=m\psi$ splits into the two lines
$$
P_-\,\mathcal{D}(p)\,\psi_+=m\,\psi_- ,
\qquad
P_+\,\mathcal{D}(p)\,\psi_-=m\,\psi_+ ,
$$
with $\psi_\pm=P_\pm\psi$. That is the cell form of the chiral pair: the momentum cell carries one chirality into the other, while the mass multiplies each chirality by itself, so each line pairs a chirality-flipping kinetic term with a mass term of one chirality. The two lines are the momentum-space form of the chiral pair displayed above, and they are one equation in the module; they are split because they act on different objects, not because there are two dynamics.

**A consistency check.** The identity behind the amputation is $(\mathcal{D}(p)-m)(\mathcal{D}(p)+m)=(p^2-m^2)\mathbf{1}=-\,\mathcal{M}(\tilde P)\mathbf{1}$. Recomputed on $100$ random real four-momenta, the largest deviation is of order $10^{-15}$ for both $\mathcal{D}(p)^2=p^2\mathbf 1$ and the product identity; the cell anticommutators hold exactly: every entry of $\chi_{\mathrm c}$ is $\pm i$ and every entry of $\mathcal D(p)$ is $\pm i$ times one momentum component, so each entry of the anticommutator is the sum of two cancelling products. The framework adds nothing to the identity; it identifies the module, the mass cell, and the chirality cell on which it acts.

## The One-Mode Truncation and the Module Gap

Conditional on the one-mode identification of the Fock article, the reduction has a finite-dimensional shadow, and the shadow is exact.

**The one-mode statement.** For a single fermionic mode the field is replaced by the pair of ladders $\vec\Upsilon_x,\vec\Upsilon_y$ of *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*, and the correlator by the trace over the mode. Direct computation gives
$$
\vec\Upsilon_x\vec\Upsilon_y=\tilde\Pi_+ ,
\qquad
\vec\Upsilon_y\vec\Upsilon_x=\tilde\Pi_- ,
\qquad
\tilde\Pi_\pm^2=\tilde\Pi_\pm ,
\qquad
\tilde\Pi_++\tilde\Pi_-=e_t ,
\qquad
\tilde\Pi_+\tilde\Pi_-=0 ,
\qquad
\mathrm{Sc}\,\tilde\Pi_\pm=\tfrac12 ,
$$
so the two orderings are the two minimal idempotents: $\tilde\Pi_+=\vec\Upsilon_x\vec\Upsilon_y$ is the vacuum rung and $\tilde\Pi_-=\vec\Upsilon_y\vec\Upsilon_x$ the occupation-number operator, which the Fock article gives as $\tfrac12(e_t-i\vec e_z)$. The time-ordered two-point function is $\theta(t')\tilde\Pi_+-\theta(-t')\tilde\Pi_-$, whose vacuum expectation is $\theta(t')$: the vacuum is the rung $\tilde\Pi_+$, on which the normalized state functional returns one, and the other rung annihilates it. Its Fourier transform is
$$
D(\omega)=\frac{i\,\tilde\Pi_+}{\omega+i\epsilon}+\frac{i\,\tilde\Pi_-}{\omega-i\epsilon} ,
$$
so the residue at $\omega=0$, read by multiplying by $\omega$ with the prescription removed, is $i(\tilde\Pi_++\tilde\Pi_-)=i\,e_t$: the identity cell of the mode algebra, times the overall $i$ that the Feynman normalization carries. The wave-function renormalization, the coefficient of the identity, is therefore $Z=1$ exactly, because the truncated space has no continuum to renormalize into. This is the finite-dimensional instance of LSZ, and it is exact rather than approximate.

**The gap.** The S-matrix of a *field* is an operator on an infinite-dimensional Fock space, and the LSZ reduction is a statement about that operator; neither is an element of $\mathbb{B}$. The algebra provides the mass-shell symbol, the plane waves, and the internal module of the external legs; it does not provide the reduction theorem, which is a statement about the asymptotics of an infinite-dimensional theory. This is the same module gap as in the Fock, S-matrix, Wick, and Bogoliubov articles, here located at the step where the external legs are placed on shell.

## The Reduction from the Functional Integral

The reduction can be read off the source derivative of the generating functional, and in the framework the source is an element of the algebra, not a c-number.

**The source and the correlator.** Add to the action a source term $\int\langle\tilde J,\tilde\Phi\rangle$, with $\tilde J\in\mathbb{B}$ a source paired by the plain bilinear form, $\langle\tilde J,\tilde\Phi\rangle=\mathrm{Sc}(\tilde J\tilde\Phi)$. The first derivative of $W[\tilde J]$ is the classical field $\tilde\Phi_{\mathrm{cl}}=\delta W/\delta\tilde J$ of the effective-action article, and the $(n+m)$-fold derivative at $\tilde J=0$ is the connected $(n+m)$-point function $G^{(n+m)}$.

**The reduction.** LSZ is the statement that the S-matrix element is that correlator with every leg amputated and normalized,
$$
\langle f|S|i\rangle
= \Big[\prod_{\text{legs}}Z_j^{-1/2}\Big]
\Big[\prod_{\text{legs}}\ \lim_{\mathcal{M}(\tilde P_j)\to0}\mathcal{M}(\tilde P_j)\Big]
G^{(n+m)}(p_1,\dots,p_{n+m}) ,
$$
where $G^{(n+m)}(p_1,\dots,p_{n+m})$ is the Fourier transform of the position-space correlator of the earlier section, the argument distinguishing the two writings, the limits are taken on the external momenta and not on the source, and the $Z_j^{-1/2}$ per leg cancels the $\sqrt{Z_j}$ that the leg carries, the residue $Z_j$ being the square of it. Equivalently the poles sit in the correlator and the limits select its residue: for each leg, $G^{(n+m)}$ has a simple pole in $\mathcal{M}(\tilde P_j)$ whose residue is the one-particle projection of that leg.

Reading the formula this way separates what the algebra supplies — the element-valued source, the central mass-shell operator, the residues — from what is the standard LSZ theorem: that the on-shell residue of the source derivative is the physical amplitude, which rests on the asymptotic conditions and is not an algebraic fact.

## The Spectral Representation and the Residue

The residue $Z$ is the one-particle weight in the **Källén–Lehmann spectral representation**, and the framework's spectral function is a sum over the module's states.

Insert a complete set of intermediate states into the two-point function. In the normalization used here, where the $2\pi$ of the spectral density is cancelled by the measure, the result is
$$
D_F(p^2) = \int_0^\infty \frac{d\mu^2}{2\pi}\,\frac{\rho(\mu^2)}{\mu^2-p^2-i\epsilon} = -\int_0^\infty \frac{d\mu^2}{2\pi}\,\frac{\rho(\mu^2)}{p^2-\mu^2+i\epsilon},
\qquad
\rho(\mu^2) = (2\pi)\sum_n \big|\langle n|\tilde\Phi(0)|0\rangle\big|^2\,\delta(\mu^2-m_n^2)\ \ge 0 ,
$$
with the sum over all intermediate states of mass $m_n$. The two writings are the same function, since $\mu^2-p^2-i\epsilon=-(p^2-\mu^2+i\epsilon)$; the first is the one adapted to the propagator's normalization, whose pole at $\mu^2=m^2$ is $1/(m^2-p^2-i\epsilon)$. The two $2\pi$'s, the one in $d\mu^2/2\pi$ and the one in $\rho$, cancel in the one-particle term and give back $Z$ exactly, which is the check that the normalization is consistent. The spectral function is non-negative — a consequence of the positivity of the state space — and the one-particle contribution is a delta function at the physical mass whose coefficient is $Z$:
$$
\rho(\mu^2) = 2\pi\,Z\,\delta(\mu^2-m^2) + \rho_{\mathrm{continuum}}(\mu^2),
$$
so that the one-particle term reproduces $D_F=Z/(m^2-p^2-i\epsilon)$ and the residue of the pole is the one-particle weight. The continuum's threshold is the multiparticle branch point. This is standard (Källén 1952, Lehmann 1954) and is cited.

**Biquaternion content.** The intermediate states are states of the Fock module of *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*, and the matrix element $\langle n|\tilde\Phi(0)|0\rangle$ is a module-valued amplitude whose norm enters. The one-particle contribution is the module vector projected onto the on-shell momentum, i.e. the external wavefunction of the earlier section; the residue $Z$ is its norm squared. For a scalar field with a $\flat$-commuting self-energy the spectral function splits into the two sectors' contributions, $\rho=\rho_-+\rho_+$, consistent with $Z=Z_-+Z_+$. The positivity of $\rho$ is the positivity of the inner product of the state space, which the GNS article constructs; the spectral representation is thus where the LSZ residue and the state-space positivity meet.

## What Is Established and What Is Interpretation

**Established (algebra).**
- The mass shell is the biquaternion-norm level set $\tilde P\tilde P^{\natural}=-m^2$, equivalently $\mathcal{M}(\tilde P)=\tilde P\tilde P^{\natural}+m^2=0$, with $\tilde P\tilde P^{\natural}=(iE)^2+\vec p^{\,2}$ and $(iE)^2=-E^2$; checked numerically ($-0.490000$ versus $-m^2=-0.49$).
- Amputation is multiplication by the inverse propagator: the real central scalar $\mathcal{M}(\tilde P)$ for a scalar field, the cell $\mathcal{D}(p)-m$ for a spinor field, with $D_F=1/(\mathcal{M}-i\epsilon)$ in the scalar case; the two conventions differ by a factor $-1$ per leg.
- The wave-function renormalization is the residue at the biquaternion-norm pole; checked for a model propagator ($Z=2.3$ recovered from both sides) and for the free field ($Z=1$, amputated two-point function $1$).
- For a scalar field the reduction is component-wise, with one real central scalar multiplying all four complex components; the sector split is preserved by that scalar and exchanged by the central $i$.
- For a spinor field the pole is the same central scalar, the residue is the rank-two cell $\mathcal{D}(p)+m=\sum_r w^{(r)}\bar w^{(r)}$, and the chirality cell anticommutes with $\mathcal{D}(p)$ and commutes with the mass; checked on $100$ random four-momenta.
- The one-mode truncation gives the exact free result $Z=1$, the residue being the identity cell of the mode algebra.

**Standard, and transcribed.**
- The LSZ theorem itself: the asymptotic conditions, adiabatic switching, the derivation from the interpolating field, the $\sqrt Z$ factors, the momentum-conservation delta functions, and the spinor reduction formula.

**Interpretation.**
- Reading the mass shell as a level set of the biquaternion norm, so that the massless case is the zero-divisor cone, is the framework's own identification; it is consistent with the material-sector article.
- Reading the spinor residue as a sum over spin states rather than as a scalar factor is the framework's reading of the spin sums; the spin sums themselves are the propagator article's.
- The component-wise scalar reduction is the LSZ counterpart of the functional-integral factorization; stated as such.

**Open.**
- The framework has no independent derivation of the asymptotic conditions; they are assumed as in the standard theory.
- The reduction of the **two-sided** Dirac equation is not written. Its mass is a right multiplication together with the conjugation $\overline{F}$, so the amputation would have to be applied on the right and the conjugation carried through every leg; whether that produces the same residue as the one-sided pair is not settled here.
- Whether the component-wise structure of the scalar reduction has observable consequences lies outside this article, which only identifies it.

## The Gamma Formulation

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a separate algebra; the body writes the cells directly.

Here $L_a\psi=a\psi$ and $R_b\psi=\psi b$ are the left and right multiplications, and $L_aR_b$ is a cell.

$$
\gamma_0=iL_{e_t}R_{\vec e_x},\quad \gamma_1=iL_{\vec e_x}R_{\vec e_y},\quad \gamma_2=iL_{\vec e_y}R_{\vec e_y},\quad \gamma_3=iL_{\vec e_z}R_{\vec e_y},\quad \gamma_5=-iL_{e_t}R_{\vec e_z}.
$$

The frame is the body's cells renamed. The momentum cell is the contraction
$$
\slashed p=\gamma_0p_0-\sum_{k=x,y,z}\gamma_kp_k ,
\qquad
(\slashed p)^2=p^2\,\mathbf 1 ,
$$
the mass-shell operator is minus the product of the two shifted cells,
$$
\mathcal{M}(\tilde P)=-\big(\slashed p-m\big)\big(\slashed p+m\big)=m^2-p^2 ,
$$
a multiple of the identity cell, and the residue of the spinor propagator is the cell $\slashed p+m$ up to the overall $-i$, which is the spin sum $\sum_r w^{(r)}\bar w^{(r)}$. The mass is the identity cell, not a fifth generator. The frame is consistent in the usual sense, $\{\gamma_\mu,\gamma_\nu\}=2g_{\mu\nu}\mathbf 1$ with $g=\mathrm{diag}(+1,-1,-1,-1)$. That $g$ is minus the $ict'$ coordinate metric $\eta=\mathrm{diag}(-1,+1,+1,+1)$, and the overall sign is the one that makes $\slashed p^{\,2}$ equal $p^2$, the d'Alembertian's symbol, rather than $-p^2$. Each square is a cell sign times the central one: $(\gamma_0)^2=\mathbf 1$, and $(\gamma_k)^2=-\mathbf 1$ for the three spatial cells, the two quaternion squares multiplying to $+1$ and the central $i^2=-1$ remaining.

$\gamma_5$ is the reference-frame cell of the chirality; the central grading $\chi=i\tilde\Xi_{\mathrm{ad}}$ is a different object, represented by $\gamma_5$ on the Dirac module. It squares to the identity cell, anticommutes with every $\gamma_\mu$ and hence with $\slashed p$, and commutes with the mass. The two chiralities are its $\pm1$ eigenspaces, projected by $\tfrac12(\mathbf 1\pm\gamma_5)$; the momentum cell is off-diagonal between them and the mass is diagonal, which is the frame's form of the chiral pair of the spinor section.

The dictionary is complex-linear, and the frame carries the central $i$ in each $\gamma_\mu$: the four are $i$ times real cells, so together with $i$ they span the complex Clifford algebra $\mathrm{Cl}_{1,3}(\mathbb{C})\cong M_4(\mathbb{C})$ of the section's first line. The real cells $L_aR_b$ alone, without the $i$, are real matrices and span all of $M_4(\mathbb{R})$; nothing is lost by writing the frame with the $i$ attached.

## Summary

The LSZ reduction in biquaternionic form is the standard reduction with the framework's mass-shell symbol. The mass shell is the biquaternion-norm level set
$$
\tilde P\tilde P^{\natural}=-m^2
\qquad\Longleftrightarrow\qquad
\mathcal{M}(\tilde P)=\tilde P\tilde P^{\natural}+m^2=0 ,
\qquad
\tilde P\tilde P^{\natural}=(iE)^2+\vec p^{\,2}=(-E^2+\vec p^{\,2})e_t=-p^2e_t ,
$$
verified as $-0.490000=-m^2$ for $m=0.7$, $\vec p=(0.3,-0.9,1.1)$, the sign being the central unit's, $(iE)^2=-E^2$. Amputation is multiplication by the real central mass-shell operator $\mathcal{M}(\tilde P)$, the inverse of the propagator $D_F=1/(\mathcal{M}-i\epsilon)$; the wave-function renormalization is the residue at the biquaternion-norm pole, checked to give $Z=2.3$ for a model propagator and $Z=1$ for the free field, where the amputated two-point function is exactly $1$. For a scalar biquaternion field the reduction is one real central scalar multiplying the four complex components, so it is component-wise and preserves the sector split. For a spinor field the amputation is the cell $\mathcal{D}(p)-m$: the pole remains the central scalar $p^2=m^2$, the residue, on the shell, is the rank-two cell $\mathcal{D}(p)+m=\sum_r w^{(r)}\bar w^{(r)}$, so a leg is a sum of two spin-state reductions, and the chirality cell anticommutes with $\mathcal{D}(p)$ and commutes with the mass. The one-mode truncation gives the exact free result $Z=1$.

The reduction theorem itself — the asymptotic conditions, the adiabatic switching, the $\sqrt Z$ normalization — is standard and transcribed. The algebra supplies the mass-shell symbol, the central-phase plane waves, the mass cell and the chirality cell; the field-level S-matrix and its reduction live on the Fock module and not in $\mathbb{B}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $i$, $i^2=-1$ | Central scalar imaginary; the sign of every $E^2$ and of every cell square |
| $\tilde P=iEe_t+\vec p$, $\tilde P^{\natural}=iEe_t-\vec p$ | Wave biquaternion and its quaternion conjugate |
| $\vec p^{\,2}=p_x^2+p_y^2+p_z^2$ | Euclidean square of the vector part; the quaternion square is $\vec p\,\vec p=-\vec p^{\,2}$ |
| $\tilde P\tilde P^{\natural}=(-E^2+\vec p^{\,2})e_t=-p^2e_t$ | Central biquaternion norm; $p^2=p_0^2-\vec p^{\,2}$ |
| $\mathcal{M}(\tilde P)=\tilde P\tilde P^{\natural}+m^2=m^2-p^2$ | Mass-shell operator, the inverse propagator; real central on real momenta |
| $\mathcal{M}(\tilde P)=0\iff E_{\vec p}^2=\vec p^{\,2}+m^2$ | Mass shell, a biquaternion-norm level set |
| $\Box=\mathrm{Sc}(\tilde\nabla\tilde\nabla^{\natural})=\partial^2/\partial Q_t^2+\Delta$ | d'Alembertian, the series convention, with symbol $\Box\to p^2$ on the material sector |
| $\eta=\mathrm{diag}(-1,+1,+1,+1)$ | $ict'$ coordinate metric (level 2); the frame's component metric $g$ is minus it |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | Anti-Hermitian and Hermitian sectors, the fixed spaces of $\flat$ and of ${}^{*}$; $\tilde\Phi_\pm=\tfrac12(\tilde\Phi\pm\tilde\Phi^{\flat})$ |
| $\flat=-{}^{*}$ | The anti-Hermitian conjugation; antilinear, with the twist $(AB)^{\flat}=-B^{\flat}A^{\flat}$ |
| $D_F(\tilde P)=1/(\mathcal{M}(\tilde P)-i\epsilon)=-1/(p^2-m^2+i\epsilon)$ | Feynman propagator (momentum space) |
| $p^2-m^2=-\mathcal{M}(\tilde P)$ | Symbol of the wave operator $(\Box-m^2)$; amputation uses $\mathcal{M}$ |
| $Z=\lim_{p^2\to m^2}(m^2-p^2)D_F(p^2)=\lim_{\mathcal{M}\to0}\mathcal{M}D_F$ | Wave-function renormalization (residue) |
| $\langle f\lvert S\rvert i\rangle$ | S-matrix element from the reduction |
| $\sigma_j$, $\varepsilon_j$ | The two signs of leg $j$: $\sigma_j=\pm1$ from the Fourier phase (out/in), $\varepsilon_j=\pm1$ from the numerator ($\tilde\Psi$/$\tilde\Psi^{\natural}$); independent |
| $\exp(i\,\mathrm{Sc}(\tilde P^{\natural}\tilde R))=\exp(-ip\cdot x)$ | Central-phase plane wave (external leg), the positive-frequency mode; complex central, not real |
| $\tilde Q^{\mathrm{amp}}$ | Constant biquaternion amplitude of the central-phase plane wave; an element of $\mathbb{B}$ bound here, with a complex scalar part, hence the majuscule |
| $L_a$, $R_b$, $L_aR_b$ | Left multiplication $a\psi$, right multiplication $\psi b$, and the cell $\psi\mapsto a\psi b$ |
| $\mathbf{1}=L_{e_t}R_{e_t}$ | Identity cell |
| $\mathcal{D}(p)=iL_{e_t}R_{\vec e_x}p_0-\sum_k iL_{\vec e_k}R_{\vec e_y}p_k$ | Momentum cell, the momentum symbol of $\mathbb{D}$; $\mathcal{D}(p)^2=p^2\mathbf 1$ |
| $\mathbb{D}$ | Pair operator, $\mathbb{D}\Psi=(\tilde\nabla\tilde\Psi_R,\tilde\nabla^{\natural}\tilde\Psi_L)$, $\mathbb{D}^2=\Box\,\mathbf 1$ |
| $\chi_{\mathrm{c}}=-iL_{e_t}R_{\vec e_z}$ | Chirality cell, the module representative of the central grading $\chi=i\tilde\Xi_{\mathrm{ad}}$; $\{\chi_{\mathrm c},\mathcal{D}(p)\}=0$, $\chi_{\mathrm c}^2=\mathbf 1$ |
| $\Delta=S\oplus S^{\mathrm c}$ | Dirac module, the two chiralities |
| $w^{(r)},v^{(r)}$ | External spinors; $\sum_r w^{(r)}\bar w^{(r)}=\mathcal{D}(p)+m$ and $\sum_r v^{(r)}\bar v^{(r)}=\mathcal{D}(p)-m$, evaluated on the shell |
| $\vec\Upsilon_x,\vec\Upsilon_y$, $\tilde\Pi_\pm$ | One-mode ladders and rungs; $\tilde\Pi_+\tilde\Pi_-=0$, $\tilde\Pi_++\tilde\Pi_-=e_t$ |
| $\rho(\mu^2)$, $Z=Z_-+Z_+$ | Spectral weight and the sector splitting of the residue |
| $\tilde J$ | Element-valued source of the generating functional, paired by the plain bilinear form |
| $\langle\tilde Q_1,\tilde Q_2\rangle$ | The plain bilinear form, the scalar part of the plain bilinear product: $\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ |

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
- Companion articles: [The S-Matrix in Biquaternionic Form](the-s-matrix-in-biquaternionic-form.html), for the S-matrix and the external data whose reduction this article supplies; [The Feynman Propagator in Biquaternionic Form](the-feynman-propagator-in-biquaternionic-form.html), for the wave biquaternion, the mass shell, the spin sums and the momentum cell; [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html), for the one-sided and the two-sided equations and the chirality sign; [Fock Space and Creation/Annihilation Operators in Biquaternionic Form](fock-space-and-creation-annihilation-operators-in-biquaternionic-form.html), for the one-particle states and the one-mode truncation; [The Functional Integral in Biquaternionic Form](the-functional-integral-in-biquaternionic-form.html) and [The Generating Functional and the Effective Action in Biquaternionic Form](the-generating-functional-and-the-effective-action-in-biquaternionic-form.html), for the correlation functions being reduced; [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html), for the biquaternion norm and the zero-divisor cone.
