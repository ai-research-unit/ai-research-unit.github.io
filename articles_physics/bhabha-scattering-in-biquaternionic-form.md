# __Bhabha Scattering in Biquaternionic Form__

## Introduction

**Bhabha scattering** is electron–positron scattering, $e^+e^-\to e^+e^-$, in quantum electrodynamics. Homi Bhabha derived it in 1936, in *The scattering of positrons by electrons with exchange on Dirac's theory of the positron*. At the tree level it receives two contributions with a **relative sign difference**: the **$t$-channel scattering** diagram, in which the electron and positron exchange a photon, and the **$s$-channel annihilation** diagram, in which the pair annihilates into a photon that recreates the pair. The two diagrams interfere, and the interference term is negative. By **crossing symmetry**, the Bhabha amplitude is the Møller amplitude $e^-e^-\to e^-e^-$ with one particle line crossed from the initial to the final state, and the two describe the same analytic object.

Bhabha scattering is the workhorse of electron–positron colliders: because its small-angle cross section is large, exactly calculable and dominated by the $1/t^2$ photon propagator, it is used as the **luminosity monitor** of the machine. This is the counterpart of the companion article *Møller Scattering in Biquaternionic Form*, and the biquaternion interpretation is largely shared: the amplitude is a product of material-sector currents joined by the framework's photon propagator, and the two structural features the framework owns are the **fermion sign** — here appearing as the relative sign between exchange and annihilation — and **crossing symmetry**, which is the framework's charge conjugation $\mathcal C$, the real structure that pairs an element with its conjugate.

The article is organised as follows. The next section sets up the kinematics, the frame basis operators and the equations of the external states, then the two amplitudes with their relative sign. The section after that gives the spin sum, the traces and the cross section with its small-angle behaviour. Then comes the crossing relation to Møller, with the exact check, followed by the biquaternion interpretation, including the annihilation channel's relation to charge conjugation and to bound-state physics, and then the open questions. A closing dictionary carries the five basis operators into the display of the older literature; nothing before it needs that display. The summary, the notation table and the literature close the article.

## The Process and Its Two Amplitudes

### Kinematics

Let $k$ and $k_2$ be the four-momenta of the incoming and outgoing **positron**, and $p$ and $p_2$ those of the incoming and outgoing **electron**, so that the process is $e^+(k)\,e^-(p)\to e^+(k_2)\,e^-(p_2)$. The Mandelstam variables are

$$
s = (k+p)^2 = (k_2+p_2)^2,
\qquad
t = (k-k_2)^2 = (p-p_2)^2,
\qquad
u = (k-p_2)^2 = (p-k_2)^2,
$$

In the massless limit $k^2=p^2=k_2^2=p_2^2=0$ they reduce to

$$
s \approx 2k\cdot p \approx 2k_2\cdot p_2,
\quad
t \approx -2k\cdot k_2 \approx -2p\cdot p_2,
\quad
u \approx -2k\cdot p_2 \approx -2k_2\cdot p .
$$

Here $s$ is the annihilation-channel invariant, $t$ the momentum-transfer invariant, and $u$ the crossed invariant; the letters are those of Møller scattering, but the particle assignments differ, and $s+t+u=0$ in the massless limit. In the centre-of-momentum frame at energy $E$, with $\theta$ the angle between the incoming and the outgoing positron,

$$
s=4E^2,\qquad
t=-2E^2(1-\cos\theta),\qquad
u=-2E^2(1+\cos\theta),
$$

so that $t\le0$ and, at small angles, $t\to0^-$ and $u\to-s$.

### The frame operators and the momentum operator
The algebra is $\mathbb{B}$, read in the units $e_t,\vec e_x,\vec e_y,\vec e_z$ of *Algebra and Element Conventions*, and the two-sided multiplications are the basis operators of *Operator Family Conventions*, written here by their action $X\mapsto aXb$.

The four **frame basis operators** that the current uses act by

$$
\Gamma_t: X\mapsto iX\vec e_x,\qquad
\Gamma_\eta: X\mapsto i\vec e_\eta X\vec e_y\quad(\eta=1,2,3),
$$

with $(\vec e_1,\vec e_2,\vec e_3)=(\vec e_x,\vec e_y,\vec e_z)$, and the fifth, the basis operator that carries the split, acts by

$$
\mathsf{V}_{\mathrm{vol}}: X\mapsto -iX\vec e_z .
$$

Each frame basis operator carries exactly one factor of the central $i$, so a square spends $i^2=-1$ once, and the remaining signs come from the squares of the three spatial units:

$$
\Gamma_t^2=1,\qquad
\Gamma_\eta^2=-1,\qquad
\Gamma_\mu\Gamma_\nu+\Gamma_\nu\Gamma_\mu=0\quad(\mu\neq\nu),
$$

the $1$ being the identity action and the $0$ the zero action. The anticommutation comes from the quaternion rule of two different spatial units. The time basis operator is a right multiplication alone, the three spatial basis operators carry a factor on each side, and the fifth is a right multiplication alone; that side is what makes it a chirality, and its anticommutation with the four frame basis operators is a separate property of the list.

The **momentum basis operator** of a four-momentum $p=(p_0,p_1,p_2,p_3)$ is the sum of the four frame basis operators with the components as coefficients,

$$
P(p): X\mapsto p_0\,iX\vec e_x-\sum_{\eta=1}^3 p_\eta\,i\vec e_\eta X\vec e_y,
$$

the minus signs on the three spatial terms being those of the metric. Its square is a multiple of the identity action,

$$
P(p)^2=p_0^2-\vec p^2,
$$

and the mass-shell condition is $P(p)^2=m^{2}c^{2}$, that is $p_0^2-\vec p^{\,2}=m^{2}c^{2}$.

### The two Dirac equations of the external states

The external states satisfy the massive Dirac equation, and in the biquaternion algebra that equation is not a single line. Two forms matter here: the **chiral pair**, which is the equation read one-sidedly, and the **two-sided equation**, which is the same physics read on the whole algebra.

**The chiral pair.** It is the pair of one-sided equations of *Operator and Calculus Conventions*,

$$
\tilde\nabla_\Phi\tilde{Ξ}_{R}=k_m\tilde{Ξ}_{L},
\qquad
(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{L}=k_m\tilde{Ξ}_{R},
$$

with $\tilde\nabla_\Phi$ the biquaternionic gradient and $(\tilde\nabla_\Phi)^{\natural}$ its quaternion conjugate. At $m=0$ the two lines decouple into the two Weyl equations $\tilde\nabla_\Phi\tilde{Ξ}_{R}=0$ and $(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{L}=0$, one for each value read by the test. The mass is the only term that relates the two parts. Both gradients act from the left, so this pair is **one-sided**. The electron state is the element $\tilde u(p)$ and the positron state the element $\tilde v(k)$; charge conjugation $\mathcal C$ pairs each with its conjugate. Here $k_m=mc/\hbar$ is the mass wave number, the inverse of the mass length.

**The two-sided form.** Read on the whole algebra rather than one-sidedly, the same physics is the single equation

$$
(\tilde\nabla_\Phi)^{\natural}F=m\,\bar F\,(-i\vec e_z),
$$

with $\bar F$ the coefficient conjugate. The derivative acts on the left, the mass acts on the right by the unit $-i\vec e_z$, and the conjugation supplies the antilinear part. The two forms are different operators: the pair is linear in the field, the two-sided form is antilinear in $F$ because the mass term carries $\bar F$.

The subscript on an element takes the two values $L$ and $R$: the value of $\mathsf{V}_{\mathrm{vol}}$ is $-1$ on the $L$ part and $+1$ on the $R$ part. The conjugation takes each letter to the other, because it sends $-i\vec e_z$ to $+i\vec e_z$. The mass term carries $\bar F$ and is therefore the only term that relates the two parts: the conjugation plays the part of the second field of the pair, and the unit $-i\vec e_z$ the part of the mass. That is why the two-sided reading is one equation for one element rather than a pair, and why it is antilinear.

**The frame-basis operator reading.** In the frame basis operators the two states satisfy

$$
P(p)\,\tilde u(p)=m\,\tilde u(p),
\qquad
P(k)\,\tilde v(k)=-m\,\tilde v(k),
$$

with the momentum basis operator acting on the element as defined. The two lines are distinguished by the sign of the mass term, because $\tilde u$ carries the positive-frequency factor $\exp(-i\theta_{\mathrm{pwp}})$ and $\tilde v$ the negative-frequency factor $\exp(+i\theta_{\mathrm{pwp}})$; the opposite sign is the crossing, not a second mass. This is not the two-sided equation: there the mass acts on the right by a unit and the field is conjugated, here the mass is the central scalar $m$ and the field is not.

Here $\theta_{\mathrm{pwp}}:=p\cdot x/\hbar=\omega_{\vec p}r'_t-\vec p\cdot\vec r$ is the plane-wave angle in momentum notation: $p$ and $x$ are real, so the exponent is $i$ times a real number and the mode factor is a phase of modulus one.

### The two amplitudes

The **current** of a line that enters with momentum $p$ and leaves with momentum $p'$ is the four numbers

$$
J_t(a,b):=\mathrm{Sc}\bigl(a^{*}b\bigr),
\qquad
J_\eta(a,b):=\mathrm{Sc}\bigl(a^{*}\,\vec e_\eta\,b\,\vec e_z\bigr)\quad(\eta=1,2,3),
$$

with $a$ the element of the outgoing line and $b$ that of the incoming one. The time component is the Hermitian form of *Product and Form Conventions* read with its two arguments exchanged, $J_t(a,b)=\langle b,a\rangle_{*}$. The four numbers are the frame-basis operator bilinears reduced to the algebra, a derived form: the central $i$ of the basis operator cancels the central $i$ of the adjoint, and the product $\vec e_y\vec e_x=-\vec e_z$ turns the right multiplier of a spatial basis operator into $\vec e_z$. Every one of the four is a single complex number, and the brackets below are ordinary products.

Two currents contract with the sign vector,

$$
J(a,b)\cdot J(c,d)=\sum_{\mu\in\{t,1,2,3\}}\varepsilon_\mu\,J_\mu(a,b)\,J_\mu(c,d),
\qquad \varepsilon=(1,-1,-1,-1),
$$

the time component entering with $+$ and the three spatial ones with $-$. The positron line uses the same four numbers with the order of the two elements reversed, $J_\mu(k,k_2)$, because there the conjugated element is the incoming one.

With this notation the $t$-channel and $s$-channel amplitudes are

$$
\mathcal M_t:=-\frac{e^2}{t}\,J(p_2,p)\cdot J(k,k_2),
$$

$$
\mathcal M_s:=+\frac{e^2}{s}\,J(k,p)\cdot J(p_2,k_2),
$$

$$
\boxed{\;\mathcal M=\mathcal M_t+\mathcal M_s\;}.
$$

The first term is the **scattering** diagram, with coefficient $-e^2$ and denominator $t=(k-k_2)^2$; the second is the **annihilation** diagram, with coefficient $+e^2$ and denominator $s=(k+p)^2$. **The relative sign between the two diagrams is negative.** It is the sign that the fermion anticommutator supplies when the contractions are ordered: in the exchange channel the electron current is formed first and the positron current second, while in the annihilation channel the two are formed in the opposite order. The electron and positron are not identical, but every fermion field anticommutes with every other, and the antisymmetry of the mode algebra fixes the sign; equivalently, it is the Møller sign carried across by crossing, where it is the exchange sign of two identical electrons. The cross section below shows that the sign is physical: the interference term $2u^2/(st)$ is negative because $st<0$.

## The Spin Sum and the Cross Section

Averaging over the two states of each incoming particle and summing over the two of each outgoing particle costs the factor $\tfrac14$. The sum over the two states of a line is the standard completeness relation, and in the massless limit it is the momentum basis operator that expresses it: $P(p)$ is then nilpotent of rank two, so the two states of the line exhaust it. The squared amplitude is then

$$
\frac14\sum_{\mathrm{states}}|\mathcal M|^2
=\frac{e^4}{4}\left(\frac{T_t}{t^2}+\frac{T_s}{s^2}-\frac{2T_{ts}}{ts}\right),
$$

with the three trace combinations

$$
T_t:=\sum_{\mu,\nu}\varepsilon_\mu\varepsilon_\nu\,
\operatorname{Tr}\bigl[\Gamma_\mu P(p)\Gamma_\nu P(p_2)\bigr]\,
\operatorname{Tr}\bigl[\Gamma_\mu P(k_2)\Gamma_\nu P(k)\bigr],
$$

$$
T_s:=\sum_{\mu,\nu}\varepsilon_\mu\varepsilon_\nu\,
\operatorname{Tr}\bigl[\Gamma_\mu P(p)\Gamma_\nu P(k)\bigr]\,
\operatorname{Tr}\bigl[\Gamma_\mu P(k_2)\Gamma_\nu P(p_2)\bigr],
$$

$$
T_{ts}:=\sum_{\mu,\nu}\varepsilon_\mu\varepsilon_\nu\,
\operatorname{Tr}\bigl[\Gamma_\mu P(p)\Gamma_\nu P(k)\Gamma_\mu P(k_2)\Gamma_\nu P(p_2)\bigr],
$$

where $\varepsilon=(1,-1,-1,-1)$ is the sign vector and $\operatorname{Tr}$ is the trace of the action on the four-dimensional complex space $\mathbb{B}$.

Each factor is a two-sided operator, and a product of two-sided operators is a two-sided operator: the action $X\mapsto aXb$ followed by $X\mapsto cXd$ is $X\mapsto caXbd$, a derived form, so the left multipliers multiply in the order reverse to the order of application and the right multipliers in that order. The trace of a basis operator is four times the product of the scalar parts of its two multipliers,

$$
\operatorname{Tr}\bigl[X\mapsto aXb\bigr]=4\,\mathrm{Sc}(a)\,\mathrm{Sc}(b),
$$

a derived form obtained by expanding $aXb$ on the four units and reading the diagonal. Every one of the three combinations is therefore a finite sum of products of scalar parts, and the massless on-shell conditions $P(p)^2=P(p_2)^2=P(k)^2=P(k_2)^2=0$ reduce each sum to a quadratic in the invariants. The three results are

$$
\frac14 T_t=2(s^2+u^2),\qquad
\frac14 T_s=2(t^2+u^2),\qquad
\frac14 T_{ts}=-2u^2.
$$

Inserting them gives the spin-averaged squared amplitude

$$
\overline{|\mathcal M|^2}
=2e^4\left[\frac{s^2+u^2}{t^2}+\frac{t^2+u^2}{s^2}+\frac{2u^2}{st}\right].
$$

The unpolarized differential cross section follows from the standard two-body flux factor, with equal masses so that the momentum ratio is one,

$$
\frac{d\sigma}{d\Omega}=\frac{1}{64\pi^2s}\,\overline{|\mathcal M|^2},
\qquad
\alpha=\frac{e^2}{4\pi}.
$$

With $d\sigma/d(\cos\theta)=2\pi\,d\sigma/d\Omega$, the result is

$$
\boxed{\;
\frac{d\sigma}{d(\cos\theta)}
=\frac{\pi\alpha^2}{s}\left[\frac{s^2+u^2}{t^2}+\frac{t^2+u^2}{s^2}+\frac{2u^2}{st}\right]\;},
$$

which is equivalently the compact form

$$
\frac{d\sigma}{d(\cos\theta)}
=\frac{\pi\alpha^2}{s}\left[u^2\left(\frac1s+\frac1t\right)^2+\left(\frac{t}{s}\right)^2+\left(\frac{s}{t}\right)^2\right].
$$

The formula is valid at collision energies well below the $Z$ mass scale, around $91\ \mathrm{GeV}$, where photon exchange dominates; above that energy the $Z$-boson contribution must be added, as in the electroweak treatment of the Møller companion. The bracket has the anatomy of the Møller case term for term — a $t$-channel square, an $s$-channel square and the interference — and the interference term $2u^2/(st)$ is negative because $st<0$.

At small angles $t\to0^-$ and the $1/t^2$ term dominates. Its coefficient is $s^2+u^2$, and $u\to-s$, so $s^2+u^2\to2s^2$:

$$
\boxed{\;
\frac{d\sigma}{d(\cos\theta)}
\sim\frac{\pi\alpha^2}{s}\frac{s^2+u^2}{t^2}
\to\frac{2\pi\alpha^2 s}{t^2}\;}.
$$

That limit is large, positive and calculable in perturbation theory to high precision. This domination by the photon propagator at small angles is why Bhabha scattering is the standard **luminosity monitor**: the rate of small-angle $e^+e^-$ events measures the machine's luminosity, given the known cross section.

## Crossing Symmetry with Møller Scattering

**Crossing symmetry** relates the two processes. Moving the incoming electron of Møller scattering to an outgoing positron — reversing the sign of its four-momentum and its charge — turns $e^-e^-\to e^-e^-$ into $e^+e^-\to e^+e^-$; the $u$-channel of one becomes the $s$-channel of the other, and the $t$-channel is common. Consequently, in the massless limit the Møller and Bhabha spin-averaged squared amplitudes are the **same analytic function** of $s,t,u$, evaluated in the physical regions of the two processes. Concretely, exchanging $s\leftrightarrow u$ in the Møller closed form of the companion article turns it term for term into the Bhabha expression above: $(s^2+u^2)/t^2$ is symmetric already, $(s^2+t^2)/u^2$ becomes $(u^2+t^2)/s^2$, and $2s^2/(tu)$ becomes $2u^2/(ts)$. The correspondence is therefore an identity of the two closed forms, not an approximation.

As a check, at $E=1$ and $\theta=\pi/3$ the massless invariants are $s=4$, $t=-1$, $u=-3$. The Bhabha bracket is

$$
\frac{s^2+u^2}{t^2}+\frac{t^2+u^2}{s^2}+\frac{2u^2}{st}
=25+\frac{10}{16}-\frac{18}{4}=\frac{169}{8},
$$

and the Møller bracket at $(s,t,u)=(-3,-1,4)$ is

$$
\frac{s^2+u^2}{t^2}+\frac{s^2+t^2}{u^2}+\frac{2s^2}{tu}
=25+\frac{10}{16}-\frac{18}{4}=\frac{169}{8}.
$$

The two agree exactly, so the check confirms the arithmetic of the two closed forms.

The two processes are therefore not merely analogous; they are one amplitude read twice. The companion Møller article states the correspondence from the other side, and the section on charge conjugation below identifies it with the framework's real structure $\mathcal C$.

## The Biquaternion Reading

### The amplitude as material-sector currents

As in the Møller case, each current is the set of components of the framework's conserved **material-sector current** $\tilde J_{\Phi}\in\mathbb{B}_{\Phi}$ of the minimal-coupling article, and the propagators $1/s$ and $1/t$ come from the framework's quantized Maxwell field. The scattering term contracts two currents through a spacelike photon; the annihilation term contracts a single pair–current through a timelike photon. The full amplitude is again the framework's current, with the framework's photon, in the two possible channels.

### The relative sign is the antisymmetry of the mode algebra

The sign is the framework's **fermion sign**, and its algebraic source is one line. In the exchange channel the four external fermion fields are contracted in one order, in the annihilation channel in the other, and swapping two of them costs a minus. The electron and positron are not identical, but the antisymmetry does not distinguish them: every fermion field anticommutes with every other. The canonical-quantization article obtains this antisymmetry as the identity $(a_{\mathrm{fop},r}^{\dagger})^2=0$ together with the fermion parity of the mode algebra. The Bhabha minus sign is therefore the Møller sign read in the annihilation channel, not a separate input.

### The annihilation channel and charge conjugation

The **annihilation channel** is the framework's charge conjugation made visible. In the $s$-channel the electron and positron form a single timelike current, i.e. a state in which a particle and an antiparticle are paired; and the operation that replaces a particle line by an antiparticle line is exactly the real structure $\mathcal C$ that pairs an element with its conjugate, of the companion article *Real Spinors and Reality Conditions with Inner Conjugation*. Crossing symmetry between Møller and Bhabha — replacing an incoming electron by an outgoing positron — is the momentum-space action of the same $\mathcal C$. This is the cleanest framework-level statement the article has: **the Bhabha annihilation diagram and the Bhabha–Møller crossing relation are two faces of the framework's charge conjugation.**

The $s$-channel also connects the free scattering problem to **bound states**. The same timelike annihilation current that mediates Bhabha scattering resonates in the bound electron–positron system; in quantum electrodynamics this is the positronium spectrum, whose non-relativistic structure is the framework's hydrogen-atom series read with the reduced mass $m_e/2$, and whose relativistic corrections are the Breit–Pauli terms of the companion two-body article. The corpus does not yet contain a dedicated positronium article, so this correspondence is named and not developed.

### What the framework supplies and what it does not

The framework supplies the two currents, the photon propagator, the external Fock states, the fermion sign as the antisymmetry of its mode algebra, and charge conjugation as the real structure $\mathcal C$ that relates the exchange and annihilation channels. The trace evaluation is the basis operator algebra of the frame basis operators, not a new dynamical input. It does **not** supply the $Z$-exchange contribution or the positronium spectrum. As always, the tree-level result is standard electrodynamics expressed in the framework's variables, and no framework-specific prediction is claimed.

## Open Questions

1. **$\mathcal C$ and crossing, precisely.** Is the crossing relation between the Møller and Bhabha amplitudes the literal action of the framework's $\mathcal C$ on the external states, or only the same relabelling of the on-shell elements? The Møller companion asks the same question; a common answer would settle both.

2. **The annihilation current as one object.** In the $s$-channel the particle and antiparticle form a single current, a pair that $\mathcal C$ relates to its conjugate. Can that current be written as one element of $\mathbb{B}$, or does the framework necessarily use the doubling?

3. **Resonance and bound states.** The $s$-channel current has bound-state resonances. Does the framework's machinery produce the positronium spectrum, and does its non-relativistic limit agree with the hydrogen-atom series with the reduced mass $m_e/2$?

4. **Luminosity and precision.** The Bhabha small-angle cross section is known to high order in $\alpha$; can the framework organize the higher-order terms through the Ward–Takahashi and Schwinger–Dyson identities of the corpus, or does it stop at tree level?

5. **Weak corrections.** As in Møller scattering, $Z$ exchange and the parity-violating asymmetry belong to the framework's electroweak agenda; Bhabha scattering at and above the $Z$ pole is an asymmetry-sensitive target.

6. **Empirical contact.** The article carries the standard cross section and no framework-specific prediction; the standing disclaimer applies.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, $\gamma_0^2=I_4$ and $\gamma_\eta^2=-I_4$. The frame belongs to the coordinate, not to the array.

This section fixes the dictionary that the traces above reproduce, and nothing here is needed outside it.

The five basis operators below are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, elements of the same algebra as the body's basis operators, not of a larger one. Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\tilde{Ξ}=a\tilde{Ξ}$ and $R_b\tilde{Ξ}=\tilde{Ξ} b$.

$$
\gamma_0=iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_x},\quad \gamma_1=iL_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},\vec e_y},\quad \gamma_2=iL_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},\vec e_y},\quad \gamma_3=iL_{\mathrm{pau},\vec e_z}R_{\mathrm{pau},\vec e_y},\quad \gamma_5=-iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z} .
$$

The same in the axis-free display:

$$
\gamma_0=iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x},\quad \gamma_1=iL_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y},\quad \gamma_2=iL_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y},\quad \gamma_3=iL_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y},\quad \gamma_5=-iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z} .
$$

Each $\gamma_\mu$ carries one factor of $i$, so a square spends $i^2=-1$ once; the signs of the squares are the metric signs. The fifth basis operator is not independent, since

$$
\gamma_5=i\gamma_0\gamma_1\gamma_2\gamma_3 .
$$

These are the body's own basis operators — $\Gamma_t=\gamma_0$, $\Gamma_\eta=\gamma_\eta$ for $\eta=1,2,3$, and $\mathsf{V}_{\mathrm{vol}}=\gamma_5$ — so nothing in the body needs the gammas: the reading is a bookkeeping device for the traces, and $\mathrm{tr}$ is the $4\times4$ matrix trace of this reading, the same number as the body's trace $\operatorname{Tr}$ of the action on $\mathbb{B}$.

**The trace identities.** In the $\gamma$ reading, with $\varepsilon=(1,-1,-1,-1)$ and $\epsilon_{0123}=+1$,

$$
\{\gamma_\mu,\gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,\qquad
(\gamma_\eta)^2=-I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu,\gamma_5\}=0,
$$

$$
\mathrm{tr}(\gamma_\mu\gamma_\nu)=4\varepsilon_\mu\delta_{\mu\nu},\qquad
\mathrm{tr}(\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)
=4\bigl(\varepsilon_\mu\delta_{\mu\nu}\varepsilon_\rho\delta_{\rho\sigma}-\varepsilon_\mu\delta_{\mu\rho}\varepsilon_\nu\delta_{\nu\sigma}+\varepsilon_\mu\delta_{\mu\sigma}\varepsilon_\nu\delta_{\nu\rho}\bigr),
$$

$$
\mathrm{tr}(\gamma_5\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)=-4i\,\epsilon_{\mu\nu\rho\sigma}.
$$

The traces of an odd number of $\gamma_\mu$'s vanish. The three trace combinations of the body are then

$$
\frac14 T_t=2(s^2+u^2),\qquad
\frac14 T_s=2(t^2+u^2),\qquad
\frac14 T_{ts}=-2u^2,
$$

which is the algebra behind the cross section.

The central grading $\xi_{\mathrm{ad}}:=i\tilde{Ζ}_{\mathrm{ad}}$ is a different object from the basis operator $\mathsf{V}_{\mathrm{vol}}$, and the two must not be read as one. Here $\tilde{Ζ}_{\mathrm{ad}}$ is a central root of $-e_t$, so $\tilde{Ζ}_{\mathrm{ad}}^2=-e_t$ and $\xi_{\mathrm{ad}}^2=i^2\tilde{Ζ}_{\mathrm{ad}}^2=(-1)(-e_t)=e_t$; equivalently, $\xi_{\mathrm{ad}}$ is the difference of the two central idempotents of the complexified algebra. Being central, it acts on the Dirac module as a sign, and its representative there is $\gamma_5$. The fifth basis operator $\mathsf{V}_{\mathrm{vol}}$ acts on that same module exactly as $\gamma_5$ acts; what the two-sided reading adds is not a second operator but the frame in which the mass can act by right multiplication.

Read over $\mathbb{R}$ rather than $\mathbb{C}$, the basis operators generate a real Clifford algebra of sixteen dimensions, and its complexification is the whole of $M_4(\mathbb{C})$. The algebra $\mathbb{B}$ itself is the eight-dimensional real algebra $M_2(\mathbb{C})$, the complexified quaternions. That complexification is what lets the basis operators and the gammas be the same objects, and it is why no larger algebra is needed.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{\mathrm{axf},e_\mu}=C_{\Pi}L_{\mathrm{pau},e_\mu}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a basis operator named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

Bhabha scattering, $e^+e^-\to e^+e^-$, is the tree-level electron–positron process with two diagrams, $t$-channel scattering and $s$-channel annihilation, contributing with a relative negative sign. Its spin-averaged cross section is $(\pi\alpha^2/s)[u^2(1/s+1/t)^2+(t/s)^2+(s/t)^2]$ below the $Z$ scale, equal to $(\pi\alpha^2/s)[(s^2+u^2)/t^2+(t^2+u^2)/s^2+2u^2/(st)]$; the interference term is negative because $st<0$. At small angles the $1/t^2$ term dominates, $d\sigma/d(\cos\theta)\sim2\pi\alpha^2s/t^2$, which is why the process is the luminosity monitor of electron–positron colliders. By crossing symmetry it is the same amplitude as Møller scattering in the permuted Mandelstam variables, term for term.

In the biquaternion framework the amplitude is the contraction of material-sector currents by the quantized photon propagator, in the exchange and annihilation channels. The external states solve the one-sided chiral pair; the two-sided reading replaces the mass by a right multiplication by $-i\vec e_z$, and the frame-basis operator reading is the momentum-basis operator equation. The two structures the framework owns are the **fermion sign**, which is the antisymmetry of the mode algebra established by the canonical-quantization article, and **charge conjugation**, the real structure $\mathcal C$ that pairs an element with its conjugate and that relates the annihilation channel to the exchange channel and the Bhabha process to the Møller process. The $s$-channel annihilation current is the doorway to positronium, which the corpus does not yet treat. The framework supplies the components and the symmetries; the trace evaluation is the basis operator algebra of the frame basis operators, while the $Z$ exchange and the bound-state spectrum remain outside its established content, and no framework-specific prediction is claimed.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $e^+e^-\to e^+e^-$ | Bhabha scattering |
| $k,k_2$ | Incoming, outgoing positron four-momenta |
| $p,p_2$ | Incoming, outgoing electron four-momenta |
| $s,t,u$ | Mandelstam variables; $s$ annihilation, $t$ transfer, $u$ crossed |
| $t$-channel | Scattering diagram, coefficient $-e^2$ |
| $s$-channel | Annihilation diagram, coefficient $+e^2$ |
| $\theta$ | Angle between the incoming and the outgoing positron |
| $d\sigma/d(\cos\theta)$ | Leading-order spin-averaged cross section |
| $\alpha=e^2/4\pi$ | Fine-structure constant |
| $\Gamma_t: X\mapsto iX\vec e_x$, $\Gamma_\eta: X\mapsto i\vec e_\eta X\vec e_y$ | Four frame basis operators |
| $\mathsf{V}_{\mathrm{vol}}: X\mapsto -iX\vec e_z$ | Volume basis operator of the frame |
| $P(p): X\mapsto p_0iX\vec e_x-\sum_\eta p_ki\vec e_\eta X\vec e_y$ | Momentum basis operator; $P(p)^2=p_0^2-\vec p^2$ |
| $J_\mu(a,b)$ | Current of a line, $J_t=\mathrm{Sc}(a^*b)$, $J_\eta=\mathrm{Sc}(a^*\vec e_\eta b\vec e_z)$ |
| $J(a,b)\cdot J(c,d)$ | Contraction with the sign vector, $\sum_\mu\varepsilon_\mu J_\mu(a,b)J_\mu(c,d)$ |
| $\tilde u(p)$, $\tilde v(k)$ | Electron and positron state elements |
| $\mathcal M_t,\mathcal M_s$ | Exchange and annihilation amplitudes |
| $\mathcal M=\mathcal M_t+\mathcal M_s$ | Total amplitude with the relative sign |
| $\overline{|\mathcal M|^2}$ | Spin-averaged squared matrix element, factor $\tfrac14$ included |
| $T_t,T_s,T_{ts}$ | Trace combinations of the spin sum |
| $\mathrm{Tr}$ | Trace of the action on the four-dimensional complex space $\mathbb{B}$ |
| $\tilde J_{\Phi}\in\mathbb{B}_{\Phi}$ | Framework's material-sector current |
| $\mathcal C$ | Charge-conjugation real structure, pairing an element with its conjugate |
| $\varepsilon=(1,-1,-1,-1)$ | Sign vector of the frame |
| $i^2=-1$ | Central imaginary of $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- H. J. Bhabha, "The scattering of positrons by electrons with exchange on Dirac's theory of the positron," *Proceedings of the Royal Society A* **154** (1936) 195–206, for the original derivation.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the standard treatment of electron–positron scattering.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the cross section, crossing symmetry and the annihilation channel.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the trace identities and the relative sign of the exchange and annihilation diagrams.
- The companion articles of this series: [Møller Scattering in Biquaternionic Form](moller-scattering-in-biquaternionic-form.html), [The Relativistic Two-Body Problem in Biquaternionic Form](the-relativistic-two-body-problem-in-biquaternionic-form.html), [The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism](the-minimal-coupling-of-the-biquaternion-dirac-field-to-electromagnetism.html), [Canonical Quantization of the Biquaternion Dirac Field](canonical-quantization-of-the-biquaternion-dirac-field.html), [Canonical Quantization of the Biquaternion Maxwell Field](canonical-quantization-of-the-biquaternion-maxwell-field.html), [The Feynman Propagator in Biquaternionic Form](the-feynman-propagator-in-biquaternionic-form.html), and [Real Spinors and Reality Conditions with Inner Conjugation](../articles_maths/real-spinors-and-reality-conditions-with-inner-conjugation.html).
