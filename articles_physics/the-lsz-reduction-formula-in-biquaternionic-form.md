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
\big\langle 0\big|T\,\tilde{Ξ}(x_1)\cdots\tilde{Ξ}(x_{n+m})\big|0\big\rangle\Big|_{\text{on shell}},
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
- **Established (algebra).** For a scalar field, amputation is multiplication by $\mathcal{M}(\tilde P)$, the inverse of the propagator $D_F=1/(\mathcal{M}(\tilde P)-i\epsilon)$. On real momenta $\mathcal{M}$ is a **real** central scalar, so it multiplies all four complex components identically and commutes with the conjugation $\flat$, hence with the two sectors. Relative to the standard wave operator it carries a factor $-1$ per leg, which is a sign convention on the external states and not a physical difference.
- **Established (algebra).** The wave-function renormalization is the residue at the biquaternion-norm pole,
$$
Z=\lim_{p^2\to m^2}\big(m^2-p^2\big)\,D_F(p^2)=\lim_{\mathcal{M}\to0}\mathcal{M}(\tilde P)\,D_F,
$$
and the asymptotic field carries $\sqrt Z$ per leg, which is the factor the formula's $Z^{-1/2}$ removes. Checked on a model propagator with a nonzero residue and a regular part.
- **Established (algebra).** For a **scalar** biquaternion field the amputation is a real central scalar, so the reduction is one scalar reduction repeated on the four coefficients, with no mixing; the two sectors are related by multiplication by the central $i$ rather than being independent field copies. For a field **with spin** the amputation is the action $\mathcal{A}_p-m$ on the element. Its pole is still the central scalar $p^2=m^2$; its residue is the action $\mathcal{A}_p+m$, which the spin sum writes as $\sum_r \tilde W^{(r)}\bar{\tilde W}^{(r)}$. The residue is therefore of rank two, not scalar: a leg of that field is a sum of two spin-state reductions with a common pole, and the momentum action exchanges the two values of the chirality while the mass keeps each of them.
- **One-mode truncation.** Conditional on the one-mode identification of *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*, the LSZ reduction for a single mode closes inside $\mathbb{B}$: the residue is the unit of the algebra times $i$, so $Z=1$ exactly, and the algebra hosts at most that one mode. The field-level reduction is an operation on the Fock space, not an element of $\mathbb{B}$; the same gap that the S-matrix, Fock, Wick, and Bogoliubov articles record.
- **Standard, and transcribed.** The derivation of LSZ from the asymptotic conditions, the adiabatic switching, the $Z$ factors, the free-field limit, and the momentum-conservation delta functions. The algebra supplies the mass-shell symbol and the plane waves, not the reduction theorem.

The article proceeds as follows. The next section states the formula and sketches its derivation from asymptotic fields. A section identifies the amputation with the inverse mass-shell operator. A section fixes the external wavefunctions as biquaternion plane waves. A section treats the wave-function renormalization as a residue, verified numerically. A section treats the scalar case and the spin case, the latter with the two Dirac equations of the corpus and with the two values of the chirality. A section treats the one-mode truncation and the gap. Two sections treat the reduction from the functional integral and the spectral representation. A section separates what is established from what is interpretation, and the closing section states the Pauli and gamma formulation that the body replaces by elements of $\mathbb{B}$.

## The LSZ Formula

The reduction is a statement about the asymptotic behaviour of correlation functions, and it is worth stating the logic before using it.

**Asymptotic fields.** A renormalized field $\tilde{Ξ}$ is supposed to approach, at early and late times, a free field of the same mass,
$$
\tilde{Ξ}(x) \;\xrightarrow{\ t'\to\pm\infty\ }\; \sqrt{Z}\,\tilde{Ξ}_{\mathrm{in/out}}(x) ,
$$
where $\tilde{Ξ}_{\mathrm{in/out}}$ is a free field and $Z$ is the wave-function renormalization. The adiabatic switching of the interaction makes the approach weak, and the reduction formula is the statement that the S-matrix element can be written entirely in terms of the interpolating field's correlation functions.

**The formula.** With $G^{(n+m)}(x_1,\dots,x_{n+m})=\langle0|T\,\tilde{Ξ}(x_1)\cdots\tilde{Ξ}(x_{n+m})|0\rangle$ the position-space correlator, the content of the display of the Introduction is
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
so the amputation is multiplication by the inverse propagator $\mathcal{M}(\tilde P)$ in momentum space, equivalently by the negative of the wave operator's symbol. The two conventions differ by a factor $-1$ per leg, which is the same sign convention on the external states; no pole and no residue is affected. The mass-shell operator $\mathcal{M}(\tilde P)=\tilde P\tilde P^{\natural}+m^2=m^2-p^2$ is the object whose vanishing is the shell, $\mathcal{M}(\tilde P)=0$, i.e. $\tilde P\tilde P^{\natural}=-m^2$. The remaining sections spell out the consequence: the amputation is a real central scalar for a scalar field and an action on the element for a field with spin, while the pole $\mathcal{M}(\tilde P)=0$ is the same central scalar in both cases.

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
\big(\mathcal{M}\tilde{Ξ}\big)^{\flat} = \bar{\mathcal{M}}\,\tilde{Ξ}^{\flat} = \mathcal{M}\,\tilde{Ξ}^{\flat},
$$
the twist of $\flat$ cancelling $\mathcal{M}^{\flat}=-\bar{\mathcal{M}}$ on a central factor, so it maps each sector into itself and acts on the two sector parts $\tilde{Ξ}_\pm$ as the same number, the part fixed by $\flat$ lying in $\mathbb{M}_-$ (*Algebra and Element Conventions*). A central scalar that is not real does the opposite: the unit $i$ exchanges the two sectors, $i\,\mathbb{M}_{-}=\mathbb{M}_{+}$, because it flips the Hermiticity of an element. The $i\epsilon$ of the prescription is the one complex central factor in the operator: it displaces the pole, and being non-real it exchanges the sectors like the unit $i$ itself, so it does not split the field into two independent copies. This distinction — central for all, real for the split — is the algebraic content of the scalar reduction below.

**The pole set is a biquaternion-norm level set.** The mass shell $\mathcal{M}(\tilde P)=0$ is the statement $\tilde P\tilde P^{\natural}=-m^2$, a level set of the biquaternion norm. For $m=0$ it is the zero set of the biquaternion norm, i.e. the zero-divisor cone, the light cone of *The Material Sector: Four-Vectors, Interval and Lorentz Action*. The reduction formula thus places the external legs on a level set of the same biquaternion norm that determines the algebra's singular elements, the metric, and the zero-divisor cone; the mass shell and the light cone are the $m\ne0$ and $m=0$ members of one family. A numerical check with $m=0.7$ and $\vec p=(0.3,-0.9,1.1)$ gives $\vec p^{\,2}=2.11$ and $E_{\vec p}^2=2.60$, hence
$$
\tilde P\tilde P^{\natural} = (iE)^2+\vec p^{\,2} = -2.60+2.11 = -0.490000 = -m^2 ,
$$
agreeing with $-m^2=-0.49$ to machine precision. The on-shell condition and the biquaternion-norm statement are thus the same equation, checked at the corpus's test point, $m=0.7$ and $\vec p=(0.3,-0.9,1.1)$, which no other result of this article uses.

## The External Wavefunctions

The external legs carry the framework's plane waves, and this is where the reduction meets the algebra's complex structure.

**Central-phase plane waves.** The biquaternion plane wave
$$
\tilde{Ξ}_{\tilde P}(\tilde R_\varphi) = \tilde Q^{\mathrm{amp}}\,\exp\big(\,i\,\mathrm{Sc}(\tilde P^{\natural}\tilde R_\varphi)\big) ,
\qquad
\tilde R_\varphi = i c r'_t\,e_t+r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z .
$$
Here $\tilde Q^{\mathrm{amp}}$ is a constant biquaternion amplitude, an element of $\mathbb{B}$ bound here, whose majuscule marks its complex scalar part. The differential operator is central and acts on the exponential as multiplication by its symbol, $\Box\to p^2=-\tilde P\tilde P^{\natural}$, so
$$
\big(\Box-m^2\big)\tilde{Ξ}_{\tilde P} \;\longrightarrow\; -\big(\tilde P\tilde P^{\natural}+m^2\big)\tilde{Ξ}_{\tilde P} = -\,\mathcal{M}(\tilde P)\,\tilde{Ξ}_{\tilde P},
$$
which vanishes for $\tilde P\tilde P^{\natural}=-m^2$. The phase is the central scalar $\mathrm{Sc}(\tilde P^{\natural}\tilde R_\varphi)=-p\cdot x$ with $p\cdot x=Et'-\vec p\cdot\vec x$, the corpus's four-vector notation, so $\exp(i\,\mathrm{Sc}(\tilde P^{\natural}\tilde R_\varphi))=\exp(-ip\cdot x)$ is the positive-frequency mode and the wave is a **central-phase** plane wave: its phase is a complex number and not a biquaternion, which is the reason the framework's free modes are the ordinary plane waves of the standard theory. This is the same statement that the path-integral and functional-integral articles make about the phase being central. Being complex, the phase is central but not real: it multiplies every component by the same complex number, and because that number is not real it re-mixes the two sectors instead of preserving them, so the sector split is a split of the field and never of the phase.

**The one-particle states.** The asymptotic states are one-particle states of the Fock space constructed in *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*, labelled by on-shell momenta and by the internal spin label of the one-particle state. The external wavefunction is the constant amplitude $\tilde Q^{\mathrm{amp}}$ times the central phase; for a scalar field it is an element of $\mathbb{B}$, while for a field with spin the same slot carries the spin amplitude $\tilde W^{(r)}$ of the spin case below. The LSZ integral projects a correlation function onto that amplitude.

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
the coefficient of the simple pole. In the framework the pole is at $\mathcal{M}(\tilde P)=0$, i.e. at $p^2=m^2$. For a scalar field the residue is a central scalar, real for real momenta; for a field with spin it is an action on the element, and the spin case below takes that form. The physical normalization is $\sqrt Z$ per external leg in either case.

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

**Sector splitting of $Z$.** For a scalar field whose self-energy commutes with $\flat$, the two-point function is the sum of one part on each sector, $D_F=D_{F-}+D_{F+}$, because an action commuting with $\flat$ has no cross part; each part carries its own residue, and the total residue is the sum $Z=Z_-+Z_+$. Each external leg then carries a $\sqrt{Z_\pm}$ from the sector it propagates in, and the amplitude's normalization is the product of those factors along the legs. For a self-energy with a part that does not commute with $\flat$ — one whose action exchanges the two values of the chirality, as a mass that changes the value does — $Z$ does not split and the residue is an action on the element. The assumption, not the algebra, is what produces the split: the algebra states that $\mathcal{M}$ is real central, and the split follows only for a dynamics that respects $\flat$.

## The Scalar Case and the Spin Case

The two cases differ in exactly one place: whether the amputation is a scalar or an action on the element.

**Scalar case: one scalar factor, four components.** For a scalar biquaternion field the amputation operator is the real central scalar $\mathcal{M}(\tilde P)$. It multiplies each of the four complex components of a correlation function by the same factor, so the reduction is component-wise: one scalar reduction, repeated four times, with no mixing and no axis singled out. The sector parts $\tilde{Ξ}_\pm$ are amputated by the same scalar, since $\mathcal{M}$ is real; the relation between the sectors remains multiplication by the central $i$, a one-to-one map of real four-spaces and not a second, independent field. This is the LSZ counterpart of the central kinetic operator of the functional integral, which is also a single scalar multiplying every component. Its content is a component count: the biquaternion scalar's four complex components enter the reduction separately, and the algebra fixes nothing beyond that. It is **not** a statement that a biquaternion scalar is a multiplicity of complex scalars, for the reason the functional-integral and harmonic-oscillator articles give.

**Spin case: the action, and which Dirac equation.** For a field with spin the amputation is not a scalar: it is an action on the element, and the reduction must name the equation whose action it is. Write the two multiplications of $\mathbb{B}$ out, $a\tilde{Ξ}^{\mathrm{sp}}$ on the left and $\tilde{Ξ}^{\mathrm{sp}} b$ on the right. The **momentum action** $\mathcal{A}_p$ is the element formula
$$
\mathcal{A}_p\,\tilde{Ξ}^{\mathrm{sp}}=i p_0\,\tilde{Ξ}^{\mathrm{sp}}\,\vec e_x-\sum_{k=x,y,z}i p_k\,\vec e_k\,\tilde{Ξ}^{\mathrm{sp}}\,\vec e_y ,
\qquad
\mathcal{A}_p^2\tilde{Ξ}^{\mathrm{sp}}=p^2\,\tilde{Ξ}^{\mathrm{sp}} ,
\qquad
p^2=p_0^2-\vec p^{\,2},
$$
where the left factor of the energy term is $e_t$ and is not written. It is the momentum symbol of the pair operator $\mathbb{D}$ of *Operator and Calculus Conventions*, in the second of the two writings that the propagator article distinguishes: the pair operator reads that symbol on the two parts of the element and the action reads it on the element itself, the two are not the same map, and each squares to multiplication by $p^2$, so the pole set is common. The action $\mathcal{A}_p-m$ is the symbol of the inverse propagator. The energy enters as the coefficient $p_0=E$ and not as the on-shell value $E_{\vec p}$, because the amputation is an off-shell operation; the two coincide only on the shell. The signs are the frame's. The energy term squares to $+p_0^2$ because the central $i^2=-1$ is met by $\vec e_x^2=-e_t$, and each spatial term squares to $-p_k^2$ because the two quaternion squares give $(-e_t)(-e_t)=+e_t$ and the sign is the central $i^2$ alone.

**The two Dirac equations.** The corpus carries two, and they are not the same operator (see *The Dirac Equation in Biquaternionic Form*, §*The One-Sided and the Two-Sided Equation*). The **one-sided** form is the pair
$$
\tilde\nabla\tilde{Ξ}^{\mathrm{sp}}_R=m\tilde{Ξ}^{\mathrm{sp}}_L ,
\qquad
\tilde\nabla^{\natural}\tilde{Ξ}^{\mathrm{sp}}_L=m\tilde{Ξ}^{\mathrm{sp}}_R ,
$$
in which the gradient acts by left multiplication and the mass is the pairing of the two parts. The **two-sided** form is the single equation
$$
-\tilde\nabla^{\natural}F-m\,i\,\overline{F}\,\vec e_z=0 ,
$$
in which the time derivative and the spatial gradient act by left multiplication, the mass acts by right multiplication through $\vec e_z$, and the componentwise conjugation $\bar F$ supplies an antilinear part. The reduction of this article is the one-sided pair: it is the pair whose Green element the propagator article inverts, and whose momentum symbol, in the second writing, is the action $\mathcal{A}_p$. The two-sided equation is another writing of the same one, and its mass is a multiplication together with a conjugation rather than a multiplication alone; a reduction in that form would have to carry the conjugation through every leg, and the corpus does not attempt it.

**The pole is central; the residue is an action.** On a central-phase plane wave the four coefficients $p_\mu$ are constants, so $\mathcal{A}_p$ is a constant action and $\mathcal{A}_p^2$ is multiplication by $p^2$. The equation $\mathcal{A}_p\tilde{Ξ}^{\mathrm{sp}}=m\tilde{Ξ}^{\mathrm{sp}}$ then gives
$$
\big(\mathcal{A}_p^2-m^2\big)\tilde{Ξ}^{\mathrm{sp}}=(p^2-m^2)\tilde{Ξ}^{\mathrm{sp}}=0 ,
$$
so the second-order operator of the pair is the central scalar of the scalar case: the pole of every leg of the field with spin sits on the same biquaternion-norm level set $\mathcal{M}(\tilde P)=0$. What is not scalar is the residue. The inverse of the action $\mathcal{A}_p-m$ is
$$
\big(\mathcal{A}_p-m\big)^{-1}=\frac{\mathcal{A}_p+m}{p^2-m^2}=\frac{\mathcal{A}_p+m}{-\,\mathcal{M}(\tilde P)} ,
$$
so the residue of the propagator at $\mathcal{M}=0$ is the action $\mathcal{A}_p+m$, up to the overall $-i$, the product of the $-1$ in $\mathcal{M}=-(p^2-m^2)$ and the $i$ of the Feynman normalization. The spin-sum identity of the propagator article, which holds on the shell, writes that action as a sum of two terms of rank one,
$$
\mathcal{A}_p+m=\sum_{r=1}^{2}\tilde W^{(r)}(\vec p)\,\bar{\tilde W}^{(r)}(\vec p) ,
\qquad
\mathcal{A}_p-m=\sum_{r=1}^{2}\tilde V^{(r)}(\vec p)\,\bar{\tilde V}^{(r)}(\vec p) ,
$$
each product $\tilde W\bar{\tilde W}$ being read as the action $\tilde{Ξ}^{\mathrm{sp}}\mapsto \tilde W\tilde{Ξ}^{\mathrm{sp}}\bar{\tilde W}$, and the second sum being the numerator for a $\tilde{Ξ}^{\mathrm{sp}\natural}$ leg. A leg of the field with spin is thus a sum of two spin-state reductions with a common central pole: not one scalar reduction, and not an unfactorizable object either, since the action splits into the two spin states. That factorization is what lets the reduction put one external spin amplitude on each leg, $\tilde W^{(r)}$ on a positive-frequency leg and $\tilde V^{(r)}$ on a negative-frequency one, and the reduction reads
$$
\langle f|S|i\rangle_{\text{spin}}
= \Big[\prod_{\text{legs}}\int d^4x_j\,\exp(s_j ip_j\cdot x_j)\Big]
\Big[\prod_{\text{legs}}\big(\mathcal{A}_{p_j}-\varepsilon_j m\big)\Big]
\big\langle 0\big|T\,\tilde{Ξ}^{\mathrm{sp}}(x_1)\cdots\tilde{Ξ}^{\mathrm{sp}\natural}(x_{n+m})\big|0\big\rangle\Big|_{\text{on shell}} ,
$$
with two independent signs per leg: $s_j=+1$ on an outgoing leg and $-1$ on an incoming one, from the Fourier phase, and $\varepsilon_j=+1$ on a $\tilde{Ξ}^{\mathrm{sp}}$ leg and $-1$ on a $\tilde{Ξ}^{\mathrm{sp}\natural}$ leg, from the numerator the leg carries. The two are unrelated: a $\tilde{Ξ}^{\mathrm{sp}\natural}$ leg may be incoming or outgoing.

**Chirality.** The chirality is the value of the subscript, $L$ or $R$: $L$ is the minus value, $R$ the plus one, every element is the sum of one of each, and only $0$ is both. The closing section prints the frame cell whose two values these are. The momentum action exchanges the two values and the mass keeps each of them, so the equation $\mathcal{A}_p\tilde{Ξ}^{\mathrm{sp}}=m\tilde{Ξ}^{\mathrm{sp}}$ splits into the two lines
$$
\mathcal{A}_p\tilde{Ξ}^{\mathrm{sp}}_R=m\tilde{Ξ}^{\mathrm{sp}}_L ,
\qquad
\mathcal{A}_p\tilde{Ξ}^{\mathrm{sp}}_L=m\tilde{Ξ}^{\mathrm{sp}}_R .
$$
Each line pairs a kinetic term that changes the value with a mass term that keeps it, and the two lines are one equation on one element: they are written apart because each holds on a different part. That is the momentum-space form of the one-sided pair displayed above, written by value instead of by the gradient, and it is not two dynamics.

**A consistency check.** The identity behind the amputation is
$$
(\mathcal{A}_p-m)(\mathcal{A}_p+m)\tilde{Ξ}^{\mathrm{sp}}=(p^2-m^2)\tilde{Ξ}^{\mathrm{sp}}=-\,\mathcal{M}(\tilde P)\,\tilde{Ξ}^{\mathrm{sp}} .
$$
Recomputed on $100$ random real four-momenta, the largest deviation is of order $10^{-15}$ for both $\mathcal{A}_p^2\tilde{Ξ}^{\mathrm{sp}}=p^2\tilde{Ξ}^{\mathrm{sp}}$ and this product identity. The value test is exact: right multiplication by $\vec e_z$ passes through the action and reverses its sign, because $\vec e_x\vec e_z=-\vec e_z\vec e_x$ and $\vec e_y\vec e_z=-\vec e_z\vec e_y$, so an $R$ element is carried into an $L$ element and an $L$ element into an $R$ element, on the same $100$ momenta. The framework adds nothing to the identity; it identifies the element the action acts on, the mass that keeps the value, and the two values between which the action moves.

## The One-Mode Truncation and the Gap

Conditional on the one-mode identification of the Fock article, the reduction has a finite-dimensional shadow, and the shadow is exact.

**The one-mode statement.** For a single fermionic mode the field is replaced by the pair of ladders of *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*, which in the frame are $\ell_x=\tfrac12(i\vec e_x-\vec e_y)$ and $\ell_y=\tfrac12(i\vec e_x+\vec e_y)$, and the correlator by the trace over the mode. Direct computation gives
$$
\ell_x\ell_y+\ell_y\ell_x=e_t ,
\qquad
(\ell_x\ell_y)(\ell_y\ell_x)=0 ,
\qquad
\mathrm{Sc}\,\ell_x\ell_y=\mathrm{Sc}\,\ell_y\ell_x=\tfrac12 ,
$$
so the two orderings are the vacuum of the mode and its occupation-number element, each of scalar part one half, which the Fock article writes as $\tfrac12(e_t-i\vec e_z)$ for the second. The time-ordered two-point function is $\theta(t')\ell_x\ell_y-\theta(-t')\ell_y\ell_x$, whose vacuum value is $\theta(t')$: the normalized state functional returns one on the vacuum ordering and zero on the other. Its Fourier transform is
$$
D(\omega)=\frac{i\,\ell_x\ell_y}{\omega+i\epsilon}+\frac{i\,\ell_y\ell_x}{\omega-i\epsilon} ,
$$
so the residue at $\omega=0$, read by multiplying by $\omega$ with the prescription removed, is $i(\ell_x\ell_y+\ell_y\ell_x)=i\,e_t$: the unit of the algebra, times the overall $i$ that the Feynman normalization carries. The wave-function renormalization, the coefficient of the unit, is therefore $Z=1$ exactly, because the truncated space has no continuum to renormalize into. This is the finite-dimensional instance of LSZ, and it is exact rather than approximate.

**The gap.** The S-matrix of a *field* is an operator on an infinite-dimensional Fock space, and the LSZ reduction is a statement about that operator; neither is an element of $\mathbb{B}$. The algebra provides the mass-shell symbol, the plane waves, and the spin amplitudes of the external legs; it does not provide the reduction theorem, which is a statement about the asymptotics of an infinite-dimensional theory. This is the same gap as in the Fock, S-matrix, Wick, and Bogoliubov articles, here located at the step where the external legs are placed on shell.

## The Reduction from the Functional Integral

The reduction can be read off the source derivative of the generating functional, and in the framework the source is an element of the algebra, not a c-number.

**The source and the correlator.** Add to the action a source term $\int\langle\tilde J,\tilde{Ξ}\rangle$, with $\tilde J\in\mathbb{B}$ a source paired by the plain bilinear form, $\langle\tilde J,\tilde{Ξ}\rangle=\mathrm{Sc}(\tilde J\tilde{Ξ})$. The first derivative of $W[\tilde J]$ is the classical field $\tilde{Ξ}_{\mathrm{cl}}=\delta W/\delta\tilde J$ of the effective-action article, and the $(n+m)$-fold derivative at $\tilde J=0$ is the connected $(n+m)$-point function $G^{(n+m)}$.

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

The residue $Z$ is the one-particle weight in the **Källén–Lehmann spectral representation**, and the framework's spectral function is a sum over the states.

Insert a complete set of intermediate states into the two-point function. In the normalization used here, where the $2\pi$ of the spectral density is cancelled by the measure, the result is
$$
D_F(p^2) = \int_0^\infty \frac{d\mu^2}{2\pi}\,\frac{\rho(\mu^2)}{\mu^2-p^2-i\epsilon} = -\int_0^\infty \frac{d\mu^2}{2\pi}\,\frac{\rho(\mu^2)}{p^2-\mu^2+i\epsilon},
\qquad
\rho(\mu^2) = (2\pi)\sum_n \big|\langle n|\tilde{Ξ}(0)|0\rangle\big|^2\,\delta(\mu^2-m_n^2)\ \ge 0 ,
$$
with the sum over all intermediate states of mass $m_n$. The two writings are the same function, since $\mu^2-p^2-i\epsilon=-(p^2-\mu^2+i\epsilon)$; the first is the one adapted to the propagator's normalization, whose pole at $\mu^2=m^2$ is $1/(m^2-p^2-i\epsilon)$. The two $2\pi$'s, the one in $d\mu^2/2\pi$ and the one in $\rho$, cancel in the one-particle term and give back $Z$ exactly, which is the check that the normalization is consistent. The spectral function is non-negative — a consequence of the positivity of the state space — and the one-particle contribution is a delta function at the physical mass whose coefficient is $Z$:
$$
\rho(\mu^2) = 2\pi\,Z\,\delta(\mu^2-m^2) + \rho_{\mathrm{continuum}}(\mu^2),
$$
so that the one-particle term reproduces $D_F=Z/(m^2-p^2-i\epsilon)$ and the residue of the pole is the one-particle weight. The continuum's threshold is the multiparticle branch point. This is standard (Källén 1952, Lehmann 1954) and is cited.

**Biquaternion content.** The intermediate states are states of the Fock space of *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*, and the matrix element $\langle n|\tilde{Ξ}(0)|0\rangle$ is an amplitude valued in $\mathbb{B}$ whose norm enters. The one-particle contribution is the state projected onto the on-shell momentum, i.e. the external wavefunction of the earlier section; the residue $Z$ is its norm squared. For a scalar field with a $\flat$-commuting self-energy the spectral function splits into the two sectors' contributions, $\rho=\rho_-+\rho_+$, consistent with $Z=Z_-+Z_+$. The positivity of $\rho$ is the positivity of the inner product of the state space, which the GNS article constructs; the spectral representation is thus where the LSZ residue and the state-space positivity meet.

## What Is Established and What Is Interpretation

**Established (algebra).**
- The mass shell is the biquaternion-norm level set $\tilde P\tilde P^{\natural}=-m^2$, equivalently $\mathcal{M}(\tilde P)=\tilde P\tilde P^{\natural}+m^2=0$, with $\tilde P\tilde P^{\natural}=(iE)^2+\vec p^{\,2}$ and $(iE)^2=-E^2$; checked numerically ($-0.490000$ versus $-m^2=-0.49$).
- Amputation is multiplication by the inverse propagator: the real central scalar $\mathcal{M}(\tilde P)$ for a scalar field, the action $\mathcal{A}_p-m$ for a field with spin, with $D_F=1/(\mathcal{M}-i\epsilon)$ in the scalar case; the two conventions differ by a factor $-1$ per leg.
- The wave-function renormalization is the residue at the biquaternion-norm pole; checked for a model propagator ($Z=2.3$ recovered from both sides) and for the free field ($Z=1$, amputated two-point function $1$).
- For a scalar field the reduction is component-wise, with one real central scalar multiplying all four complex components; the sector split is preserved by that scalar and exchanged by the central $i$.
- For a field with spin the pole is the same central scalar, the residue is the rank-two action $\mathcal{A}_p+m=\sum_r \tilde W^{(r)}\bar{\tilde W}^{(r)}$, and the momentum action exchanges the two values of the chirality while the mass keeps each of them; checked on $100$ random four-momenta.
- The one-mode truncation gives the exact free result $Z=1$, the residue being the unit of the algebra.

**Standard, and transcribed.**
- The LSZ theorem itself: the asymptotic conditions, adiabatic switching, the derivation from the interpolating field, the $\sqrt Z$ factors, the momentum-conservation delta functions, and the reduction formula of the field with spin.

**Interpretation.**
- Reading the mass shell as a level set of the biquaternion norm, so that the massless case is the zero-divisor cone, is the framework's own identification; it is consistent with the material-sector article.
- Reading the residue of the field with spin as a sum over spin states rather than as a scalar factor is the framework's reading of the spin sums; the spin sums themselves are the propagator article's.
- The component-wise scalar reduction is the LSZ counterpart of the functional-integral factorization; stated as such.

**Open.**
- The framework has no independent derivation of the asymptotic conditions; they are assumed as in the standard theory.
- The reduction of the **two-sided** Dirac equation is not written. Its mass is a right multiplication together with the conjugation $\overline{F}$, so the amputation would have to be applied on the right and the conjugation carried through every leg; whether that produces the same residue as the one-sided pair is not settled here.
- Whether the component-wise structure of the scalar reduction has observable consequences lies outside this article, which only identifies it.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, and the frame is named on the coordinate.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a separate algebra; the body writes the cells directly.

Here $L_a\tilde{Ξ}^{\mathrm{sp}}=a\tilde{Ξ}^{\mathrm{sp}}$ and $R_b\tilde{Ξ}^{\mathrm{sp}}=\tilde{Ξ}^{\mathrm{sp}} b$ are the left and right multiplications, and $L_aR_b$ is a cell.

$$
\gamma_0=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad \gamma_1=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_2=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_3=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_5=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}.
$$

The same in the axis-free display:

$$
\gamma_0=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\quad \gamma_1=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_2=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_3=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_5=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}.
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
a multiple of the identity cell, and the residue of the spinor propagator is the cell $\slashed p+m$ up to the overall $-i$, which is the spin sum $\sum_r \tilde W^{(r)}\bar{\tilde W}^{(r)}$. The mass is the identity cell, not a fifth generator. The frame is consistent in the usual sense, $\{\gamma_\mu,\gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}\mathbf 1$ with $\varepsilon=(1,-1,-1,-1)$. Each square is a cell sign times the central one: $(\gamma_0)^2=\mathbf 1$, and $(\gamma_k)^2=-\mathbf 1$ for the three spatial cells, the two quaternion squares multiplying to $+1$ and the central $i^2=-1$ remaining. Those squares are the weight, $\gamma_\mu^2=\varepsilon_\mu\mathbf 1$, so the contraction gives $\slashed p^{\,2}=\varepsilon_0p_0^2+\sum_{k=x,y,z}\varepsilon_kp_k^2=p_0^2-\vec p^{\,2}$, which is $p^2$, the d'Alembertian's symbol in the $i c r'_t$ coordinate, rather than $-p^2$.

$\gamma_5$ is the reference-frame cell of the chirality; the central grading $\chi=i\tilde{Ζ}_{\mathrm{ad}}$ is a different object, represented by $\gamma_5$ on the Dirac module. It squares to the identity cell, anticommutes with every $\gamma_\mu$ and hence with $\slashed p$, and commutes with the mass. The two chiralities are its $\pm1$ eigenspaces, projected by $\tfrac12(\mathbf 1\pm\gamma_5)$; the momentum cell is off-diagonal between them and the mass is diagonal, which is the frame's form of the chiral pair of the spinor section.

The dictionary is complex-linear, and the frame carries the central $i$ in each $\gamma_\mu$: the four are $i$ times real cells, so together with $i$ they span the complex Clifford algebra $\mathrm{Cl}_{1,3}(\mathbb{C})\cong M_4(\mathbb{C})$ of the section's first line. The real cells $L_aR_b$ alone, without the $i$, are real matrices and span all of $M_4(\mathbb{R})$; nothing is lost by writing the frame with the $i$ attached.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

The LSZ reduction in biquaternionic form is the standard reduction with the framework's mass-shell symbol. The mass shell is the biquaternion-norm level set
$$
\tilde P\tilde P^{\natural}=-m^2
\qquad\Longleftrightarrow\qquad
\mathcal{M}(\tilde P)=\tilde P\tilde P^{\natural}+m^2=0 ,
\qquad
\tilde P\tilde P^{\natural}=(iE)^2+\vec p^{\,2}=(-E^2+\vec p^{\,2})e_t=-p^2e_t ,
$$
verified as $-0.490000=-m^2$ for $m=0.7$, $\vec p=(0.3,-0.9,1.1)$, the sign being the central unit's, $(iE)^2=-E^2$. Amputation is multiplication by the real central mass-shell operator $\mathcal{M}(\tilde P)$, the inverse of the propagator $D_F=1/(\mathcal{M}-i\epsilon)$; the wave-function renormalization is the residue at the biquaternion-norm pole, checked to give $Z=2.3$ for a model propagator and $Z=1$ for the free field, where the amputated two-point function is exactly $1$. For a scalar biquaternion field the reduction is one real central scalar multiplying the four complex components, so it is component-wise and preserves each sector. For a field with spin the amputation is the action $\mathcal{A}_p-m$ on the element: the pole remains the central scalar $p^2=m^2$, the residue, on the shell, is the rank-two action $\mathcal{A}_p+m=\sum_r \tilde W^{(r)}\bar{\tilde W}^{(r)}$, so a leg is a sum of two spin-state reductions, and the momentum action exchanges the two values of the chirality while the mass keeps each of them. The one-mode truncation gives the exact free result $Z=1$.

The reduction theorem itself — the asymptotic conditions, the adiabatic switching, the $\sqrt Z$ normalization — is standard and transcribed. The algebra supplies the mass-shell symbol, the central-phase plane waves, the mass and the two values of the chirality; the field-level S-matrix and its reduction live on the Fock space and not in $\mathbb{B}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | The biquaternion algebra (*Algebra and Element Conventions*) |
| $e_t$ | The unit of the algebra |
| $i$ | The central scalar imaginary unit; it carries the sign of every $E^2$ and of every term of the momentum action |
| $\tilde P=iEe_t+\vec p$, $\tilde P^{\natural}=iEe_t-\vec p$ | Wave biquaternion and its quaternion conjugate |
| $\vec p^{\,2}$ | Euclidean square of the vector part |
| $\tilde P\tilde P^{\natural}=(-E^2+\vec p^{\,2})e_t=-p^2e_t$ | Central biquaternion norm; $p^2=p_0^2-\vec p^{\,2}$ |
| $\mathcal{M}(\tilde P)=\tilde P\tilde P^{\natural}+m^2=m^2-p^2$ | Mass-shell operator, the inverse propagator; real central on real momenta |
| $\mathcal{M}(\tilde P)=0\iff E_{\vec p}^2=\vec p^{\,2}+m^2$ | Mass shell, a biquaternion-norm level set |
| $\Box$ | The d'Alembertian (*Operator and Calculus Conventions*), with symbol $p^2$ on the material sector |
| $i c r'_t$ | The time coefficient of the material reading; its square, $(i c r'_t)^2=-c^2{r'_{t}}^2$, supplies the one minus of the d'Alembertian on the time direction |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | The anti-Hermitian and Hermitian sectors (*Algebra and Element Conventions*); $\tilde{Ξ}_\pm$ are the two sector parts |
| $\flat$ | The anti-Hermitian conjugation (*Algebra and Element Conventions*), antilinear |
| $D_F(\tilde P)=1/(\mathcal{M}(\tilde P)-i\epsilon)=-1/(p^2-m^2+i\epsilon)$ | Feynman propagator (momentum space) |
| $p^2-m^2=-\mathcal{M}(\tilde P)$ | Symbol of the wave operator $(\Box-m^2)$; amputation uses $\mathcal{M}$ |
| $Z=\lim_{p^2\to m^2}(m^2-p^2)D_F(p^2)=\lim_{\mathcal{M}\to0}\mathcal{M}D_F$ | Wave-function renormalization (residue) |
| $\langle f\lvert S\rvert i\rangle$ | S-matrix element from the reduction |
| $s_j$, $\varepsilon_j$ | The two signs of leg $j$: $s_j=\pm1$ from the Fourier phase (out/in), $\varepsilon_j=\pm1$ from the numerator ($\tilde{Ξ}^{\mathrm{sp}}$/$\tilde{Ξ}^{\mathrm{sp}\natural}$); independent |
| $\exp(i\,\mathrm{Sc}(\tilde P^{\natural}\tilde R_\varphi))=\exp(-ip\cdot x)$ | Central-phase plane wave (external leg), the positive-frequency mode; complex central, not real |
| $\tilde Q^{\mathrm{amp}}$ | Constant biquaternion amplitude of the central-phase plane wave; an element of $\mathbb{B}$ bound here, with a complex scalar part, hence the majuscule |
| $L_a$, $R_b$, $L_aR_b$ | Left multiplication, right multiplication and the cell (closing section only) |
| $\mathcal{A}_p\tilde{Ξ}^{\mathrm{sp}}=i p_0\tilde{Ξ}^{\mathrm{sp}}\vec e_x-\sum_k i p_k\vec e_k\tilde{Ξ}^{\mathrm{sp}}\vec e_y$ | Momentum action, the second writing of the momentum symbol of $\mathbb{D}$; $\mathcal{A}_p^2\tilde{Ξ}^{\mathrm{sp}}=p^2\tilde{Ξ}^{\mathrm{sp}}$ |
| $\mathbb{D}$ | The pair operator of *Operator and Calculus Conventions*, whose square is $\Box$ |
| $L$, $R$ | The two values of the chirality subscript; $L$ the minus value, $R$ the plus one |
| $\tilde W^{(r)},\tilde V^{(r)}$ | External spin amplitudes, elements of $\mathbb{B}$; $\sum_r \tilde W^{(r)}\bar{\tilde W}^{(r)}=\mathcal{A}_p+m$ and $\sum_r \tilde V^{(r)}\bar{\tilde V}^{(r)}=\mathcal{A}_p-m$ on the shell, each product read as the action $\tilde{Ξ}^{\mathrm{sp}}\mapsto \tilde W\tilde{Ξ}^{\mathrm{sp}}\bar{\tilde W}$ |
| $\ell_x,\ell_y$ | The two ladders of *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*, $\ell_x=\tfrac12(i\vec e_x-\vec e_y)$ and $\ell_y=\tfrac12(i\vec e_x+\vec e_y)$; $\ell_x\ell_y+\ell_y\ell_x=e_t$, and the two orderings multiply to $0$ |
| $\rho(\mu^2)$, $Z=Z_-+Z_+$ | Spectral weight and the sector splitting of the residue |
| $\tilde J$ | Element-valued source of the generating functional, paired by the plain bilinear form |
| $\langle\tilde Q_1,\tilde Q_2\rangle$ | The plain bilinear form (*Product and Form Conventions*) |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
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
