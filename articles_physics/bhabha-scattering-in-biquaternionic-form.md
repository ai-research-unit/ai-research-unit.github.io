# __Bhabha Scattering in Biquaternionic Form__

## Introduction

**Bhabha scattering** is electron–positron scattering, $e^+e^-\to e^+e^-$, in quantum electrodynamics. Homi Bhabha derived it in 1936, in *The scattering of positrons by electrons with exchange on Dirac's theory of the positron*. At the tree level it receives two contributions with a **relative sign difference**: the **$t$-channel scattering** diagram, in which the electron and positron exchange a photon, and the **$s$-channel annihilation** diagram, in which the pair annihilates into a photon that recreates the pair. The two diagrams interfere, and the interference term is negative. By **crossing symmetry**, the Bhabha amplitude is the Møller amplitude $e^-e^-\to e^-e^-$ with one particle line crossed from the initial to the final state, and the two describe the same analytic object.

Bhabha scattering is the workhorse of electron–positron colliders: because its small-angle cross section is large, exactly calculable and dominated by the $1/t^2$ photon propagator, it is used as the **luminosity monitor** of the machine. This is the counterpart of the companion article *Møller Scattering in Biquaternionic Form*, and the biquaternion interpretation is largely shared: the amplitude is a product of material-sector currents joined by the framework's photon propagator, and the two structural features the framework owns are the **fermion sign** — here appearing as the relative sign between exchange and annihilation — and **crossing symmetry**, which is the framework's charge conjugation $\mathcal C$ on the doubled spinor module.

The article is organised as follows. The next section sets up the kinematics, the frame cells and the two Dirac equations of the external states, then the two amplitudes with their relative sign. The section after that gives the spin sum, the traces and the cross section with its small-angle behaviour. Then comes the crossing relation to Møller, with the exact check, followed by the biquaternion interpretation, including the annihilation channel's relation to charge conjugation and to bound-state physics. The open questions come next; *The Gamma Formulation* records the Clifford dictionary that the traces use, and the summary, the notation table and the literature close the article.

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

### The frame cells and the momentum cell

The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with $e_t=1$, $\vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t$, and central imaginary $i$, $i^2=-1$. A two-sided multiplication is a **cell**,

$$
L_a\psi=a\psi,\qquad R_b\psi=\psi b,\qquad L_aR_b\psi=a\psi b,\qquad L_aR_bL_cR_d=L_{ac}R_{db}.
$$

The four **frame cells** of the current are

$$
\Gamma_t:=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}=iR_{\vec e_x}^{\mathrm{axf}},\qquad
\Gamma_k:=iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\quad(k=1,2,3),
$$

with $(\vec e_1,\vec e_2,\vec e_3)=(\vec e_x,\vec e_y,\vec e_z)$, and the fifth, the **chirality cell**, is

$$
\chi:=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}=-iR_{\vec e_z}^{\mathrm{axf}}.
$$

Each $\Gamma_\mu$ carries exactly one factor of the central $i$, so each square spends $i^2=-1$ once, and the remaining signs come from $\vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t$:

$$
\Gamma_t^2=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}},\qquad
\Gamma_k^2=-L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}},\qquad
\{\Gamma_\mu,\Gamma_\nu\}=2g_{\mu\nu}L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}},
$$

with $g=\mathrm{diag}(+1,-1,-1,-1)$; the anticommutator is the quaternion rule $\vec e_j\vec e_k=-\vec e_k\vec e_j$ for $j\ne k$. The cells are two-sided: $\Gamma_t$ has the central left multiplier $e_t$ and is therefore a pure right multiplication, while the three spatial cells $\Gamma_k$ have a non-central left multiplier and use both sides. The chirality cell is also a pure right multiplication and anticommutes with the four frame cells.

The **momentum cell** of a four-momentum $p=(p_0,p_1,p_2,p_3)$ is

$$
P:=p_0\Gamma_t-\sum_{k=1}^3 p_k\Gamma_k
=p_0\,iR_{\vec e_x}^{\mathrm{axf}}-\sum_{k=1}^3 p_k\,iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},
$$

which is the slashed momentum read in these cells, $P=p^\mu\Gamma^\mu$ with $p^\mu=(p_0,\vec p)$ and $\Gamma^\mu=(\Gamma_t,-\Gamma_k)$ the raised cells, the minus signs being those of the metric, $\Gamma_k=-\Gamma^k$. Its square is central,

$$
P^2=(p_0^2-\vec p^2)\,L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}},
$$

and the mass-shell condition is $P^2=m^2L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$, that is $p_0^2-\vec p^2=m^2$.

### The two Dirac equations of the external states

The external spinors satisfy the massive Dirac equation, but in the biquaternion algebra that equation is not a single line. Two forms matter here: the **one-sided chiral pair**, which is the Dirac equation on the spinor module, and the **two-sided equation**, which is the same physics read on the whole algebra. The four-component form is their common reading in the frame cells.

**The chiral pair.** It is first a pair of one-sided equations

$$
\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L,
\qquad
\tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R,
$$

where $\tilde\nabla=e_t\partial/\partial Q_t+\sum_k\vec e_k\partial/\partial Q_k$ is the biquaternionic gradient and $\tilde\nabla^{\natural}$ is its quaternion conjugate. At $m=0$ the two lines decouple into the two Weyl equations $\tilde\nabla\tilde\Psi_R=0$ and $\tilde\nabla^{\natural}\tilde\Psi_L=0$, one for each chirality. The mass is the only term that couples them, and it couples them off the diagonal. Both gradients act from the left, so this pair is **one-sided**. The electron spinor $w$ and the positron spinor $v$ are the two four-component fields of the process; the charge conjugation $\mathcal C$ of the doubled module maps one onto the other.

**The two-sided form.** Read on the whole algebra rather than on the module, the same physics is the single equation

$$
\tilde\nabla^{\natural}F=m\,\chi\bar F=m\,L_{e_t}^{\mathrm{axf}}R_{-i\vec e_z}^{\mathrm{axf}}\bar F,
\qquad
\chi:=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}=-iR_{\vec e_z}^{\mathrm{axf}},
$$

with $\bar F$ the coefficient conjugate and $\chi$ the **chirality cell**, the two-sided multiplier by $e_t$ on the left and by $-i\vec e_z$ on the right. The derivative acts on the left, the mass acts on the right, and the conjugation supplies the antilinear part. The two forms are related by a change of representation but they are different operators: the pair is linear in the field, the two-sided form is antilinear in $F$ because the mass term carries $\bar F$.

The cell $\chi$ is a right multiplication by the unit $-i\vec e_z$, whose square is $e_t$; hence $\chi^2=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ and the eigenvalues of $\chi$ are $\pm1$. The two eigenspaces are the two chirality classes of $F$, and the coefficient conjugate of a field in one class lies in the other, because conjugation sends $-i\vec e_z$ to $+i\vec e_z$. The mass term therefore relates the two classes through $\bar F$: the conjugation plays the part of the second field of the pair, and the multiplier $\chi$ the part of the off-diagonal mass. That is why the two-sided reading is one equation for one biquaternion rather than a pair, and why it is antilinear.

**The four-component form.** In the frame cells, with $P(p)=p_0\Gamma_t-\sum_kp_k\Gamma_k$ and the mass read as the central cell $m\,L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$, the pair is written as

$$
\bigl(P(p)-m\,L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}\bigr)w(p)=0,
\qquad
\bigl(P(k)+m\,L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}\bigr)v(k)=0,
$$

where $w$ is the electron spinor and $v$ the positron spinor. The two lines are distinguished by the sign of the mass term, because $w$ carries the positive-frequency factor $e^{-ip\cdot x}$ and $v$ the negative-frequency factor $e^{+ip\cdot x}$; the opposite sign is the crossing, not a second mass. Each of $w$ and $v$ still carries both chiralities: the chiral halves are the two projections of the spinor, and the mass couples them. This is therefore not the two-sided equation: there the mass is a right multiplication by the chirality cell on the algebra, here it is the central multiplier $m$ on the module, and the conjugation that the two-sided form carries is absorbed in the passage from one carrier to the other.

### The two amplitudes

The vertex current of an electron line with incoming momentum $p$ and outgoing momentum $p'$ is

$$
J_\mu(p',p):=\bar w(p')\,\Gamma_\mu\,w(p),
\qquad
\bar w:=w^\dagger iR_{\vec e_x}^{\mathrm{axf}},
\qquad
\bar v:=v^\dagger iR_{\vec e_x}^{\mathrm{axf}},
$$

with $\Gamma_\mu$ the cell of the Lorentz index $\mu$ and $\bar w,\bar v$ the Dirac adjoints, whose factor $iR_{\vec e_x}^{\mathrm{axf}}=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$ is the Clifford-odd cell outside $\mathbb{B}$. The positron line uses the same bilinear with the order reversed, $\bar v(k)\Gamma_\mu v(k_2)$. The contraction is the Hermitian pairing of two module elements, so every bilinear is a single complex number and the brackets below are ordinary complex products.

Every vertex carries two factors of the central $i$, one in the adjoint and one in the cell, so each vertex carries $i^2=-1$ and never a double $i$. For the time component the reduction is the density,

$$
\bar w\,\Gamma_t\,w
=w^\dagger(iR_{\vec e_x}^{\mathrm{axf}})(iR_{\vec e_x}^{\mathrm{axf}})w
=-\,w^\dagger R_{\vec e_x^2}^{\mathrm{axf}}\,w
=w^\dagger w,
$$

and for a spatial component, with $k=1,2,3$,

$$
\bar w\,\Gamma_k\,w
=w^\dagger(iR_{\vec e_x}^{\mathrm{axf}})(iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}})w
=-\,w^\dagger L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y\vec e_x}^{\mathrm{axf}}\,w
=w^\dagger L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}\,w,
$$

where the last step uses $\vec e_y\vec e_x=-\vec e_z$ and $R_{ab}=R_bR_a$. The same reduction holds with $v$ in place of $w$, and no double $i$ is left in a reduced vertex.

With this notation the $t$-channel and $s$-channel amplitudes are

$$
\mathcal M_t:=-\frac{e^2}{t}\bigl[\bar w(p_2)\Gamma_\mu w(p)\bigr]\bigl[\bar v(k)\Gamma^\mu v(k_2)\bigr],
$$

$$
\mathcal M_s:=+\frac{e^2}{s}\bigl[\bar v(k)\Gamma_\mu w(p)\bigr]\bigl[\bar w(p_2)\Gamma^\mu v(k_2)\bigr],
$$

$$
\boxed{\;\mathcal M=\mathcal M_t+\mathcal M_s\;}.
$$

The first term is the **scattering** diagram, with coefficient $-e^2$ and denominator $t=(k-k_2)^2$; the second is the **annihilation** diagram, with coefficient $+e^2$ and denominator $s=(k+p)^2$. **The relative sign between the two diagrams is negative.** It is the sign that the fermion anticommutator supplies when the contractions are ordered: in the exchange channel the electron bilinear is formed first and the positron bilinear second, while in the annihilation channel the two are formed in the opposite order. The electron and positron are not identical, but every fermion field anticommutes with every other, and the same $\mathbb Z/2$ grading fixes the sign; equivalently, it is the Møller sign carried across by crossing, where it is the exchange sign of two identical electrons. The cross section below shows that the sign is physical: the interference term $2u^2/(st)$ is negative because $st<0$.

## The Spin Sum and the Cross Section

The spin sum is the four-component reading of the same pair. With the spin-sum cell

$$
D(p):=P(p)+m\,L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}
=p_0\,iR_{\vec e_x}^{\mathrm{axf}}-\sum_{k=1}^3 p_k\,iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}+m\,L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}},
$$

the electron and positron sums are

$$
\sum_{r=1}^{2} w^{(r)}(p)\,\bar w^{(r)}(p)=D(p),
\qquad
\sum_{r=1}^{2} v^{(r)}(k)\,\bar v^{(r)}(k)=P(k)-m\,L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}.
$$

At leading order the mass is dropped, $m=0$, and both sums are the momentum cell; the cross section below is the massless one.

Squaring the amplitude and averaging over the two incoming spins and summing over the two final spins — a factor $\tfrac14$ — gives, with the three trace combinations

$$
T_t:=\mathrm{Tr}\bigl[\Gamma^\mu P(p)\Gamma^\nu P(p_2)\bigr]\,
\mathrm{Tr}\bigl[\Gamma_\mu P(k_2)\Gamma_\nu P(k)\bigr],
$$

$$
T_s:=\mathrm{Tr}\bigl[\Gamma^\mu P(p)\Gamma^\nu P(k)\bigr]\,
\mathrm{Tr}\bigl[\Gamma_\mu P(k_2)\Gamma_\nu P(p_2)\bigr],
$$

$$
T_{ts}:=\mathrm{Tr}\bigl[\Gamma^\mu P(p)\Gamma^\nu P(k)\Gamma_\mu P(k_2)\Gamma_\nu P(p_2)\bigr],
$$

where $\Gamma^t=\Gamma_t$ and $\Gamma^k=-\Gamma_k$, and $\mathrm{Tr}$ is the trace on the four-dimensional complex module $\mathbb{B}$ that the cells act on. Then

$$
\frac14\sum_{\mathrm{spins}}|\mathcal M|^2
=\frac{e^4}{4}\left(\frac{T_t}{t^2}+\frac{T_s}{s^2}-\frac{2T_{ts}}{ts}\right).
$$

The traces are evaluated from the frame-cell Clifford relations together with the massless on-shell conditions; *The Gamma Formulation* records the identities and the dictionary. The three results are

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

As in the Møller case, the two spinor bilinears are the components of the framework's conserved **material-sector current** $\tilde J\in\mathbb M_-$ of the minimal-coupling article, and the propagators $1/s$ and $1/t$ come from the framework's quantized Maxwell field. The scattering term contracts two currents through a spacelike photon; the annihilation term contracts a single pair–current through a timelike photon. The full amplitude is again the framework's current, with the framework's photon, in the two possible channels.

### The relative sign is the graded mode algebra

The sign is the framework's **fermion sign**, and its algebraic source is one line. In the exchange channel the four external fermion fields are contracted in one order, in the annihilation channel in the other, and swapping two of them costs a minus. The electron and positron are not identical, but the grading does not distinguish them: every fermion field anticommutes with every other. The canonical-quantization article obtains this antisymmetry as the identity $(a^{\mathrm{fop}\dagger}_r)^2=0$ together with the $\mathbb Z/2$ grading of the mode algebra by fermion parity. The Bhabha minus sign is therefore the Møller sign read in the annihilation channel, not a separate input.

### The annihilation channel and charge conjugation

The **annihilation channel** is the framework's charge conjugation made visible. In the $s$-channel the electron and positron form a single timelike current, i.e. a state in which a particle and an antiparticle are paired; and the operation that replaces a particle line by an antiparticle line is exactly the real structure $\mathcal C$ on the doubled module $\Delta = S\oplus\bar S$ of the companion article *Real Spinors and Reality Conditions with Inner Conjugation*. Crossing symmetry between Møller and Bhabha — replacing an incoming electron by an outgoing positron — is the momentum-space action of the same $\mathcal C$. This is the cleanest framework-level statement the article has: **the Bhabha annihilation diagram and the Bhabha–Møller crossing relation are two faces of the framework's charge conjugation.**

The $s$-channel also connects the free scattering problem to **bound states**. The same timelike annihilation current that mediates Bhabha scattering resonates in the bound electron–positron system; in quantum electrodynamics this is the positronium spectrum, whose non-relativistic structure is the framework's hydrogen-atom series read with the reduced mass $m_e/2$, and whose relativistic corrections are the Breit–Pauli terms of the companion two-body article. The corpus does not yet contain a dedicated positronium article, so this correspondence is named and not developed.

### What the framework supplies and what it does not

The framework supplies the two vertex currents, the photon propagator, the external Fock states, the fermion sign as the antisymmetry of its mode algebra, and charge conjugation as the real structure $\mathcal C$ that relates the exchange and annihilation channels. The trace evaluation is the cell algebra recorded in *The Gamma Formulation*, not a new dynamical input. It does **not** supply the $Z$-exchange contribution or the positronium spectrum. As always, the tree-level result is standard electrodynamics expressed in the framework's variables, and no framework-specific prediction is claimed.

## Open Questions

1. **$\mathcal C$ and crossing, precisely.** Is the crossing relation between the Møller and Bhabha amplitudes the literal action of the framework's $\mathcal C$ on the external states, or only the same relabelling of on-shell spinors? The Møller companion asks the same question; a common answer would settle both.

2. **The annihilation current as one object.** In the $s$-channel the particle and antiparticle form a single current on $\Delta=S\oplus\bar S$. Can that current be written as one biquaternion object, or does the framework necessarily use the doubled module?

3. **Resonance and bound states.** The $s$-channel current has bound-state resonances. Does the framework's machinery produce the positronium spectrum, and does its non-relativistic limit agree with the hydrogen-atom series with the reduced mass $m_e/2$?

4. **Luminosity and precision.** The Bhabha small-angle cross section is known to high order in $\alpha$; can the framework organize the higher-order terms through the Ward–Takahashi and Schwinger–Dyson identities of the corpus, or does it stop at tree level?

5. **Weak corrections.** As in Møller scattering, $Z$ exchange and the parity-violating asymmetry belong to the framework's electroweak agenda; Bhabha scattering at and above the $Z$ pole is an asymmetry-sensitive target.

6. **Empirical contact.** The article carries the standard cross section and no framework-specific prediction; the standing disclaimer applies.

## The Gamma Formulation

This section fixes the dictionary that the traces above use, and nothing here is needed outside it.

The five cells below are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, elements of the same algebra as the body's cells, not of a larger one. Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\psi=a\psi$ and $R_b\psi=\psi b$.

$$
\gamma_0=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad \gamma_1=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_2=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_3=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_5=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}} .
$$

The same in the axis-free display:

$$
\gamma_0=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\quad \gamma_1=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_2=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_3=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_5=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}} .
$$

Each $\gamma_\mu$ carries one factor of $i$, so a square spends $i^2=-1$ once; the signs of the squares are the metric signs. The fifth cell is not independent, since

$$
\gamma_5=i\gamma_0\gamma_1\gamma_2\gamma_3 .
$$

These are the body's own cells — $\Gamma_t=\gamma_0$, $\Gamma_k=\gamma_k$ for $k=1,2,3$, and $\chi=\gamma_5$ — so nothing in the body needs the gammas: the reading is a bookkeeping device for the traces, and $\mathrm{tr}$ is the $4\times4$ matrix trace of this reading, the same number as the body's module trace $\mathrm{Tr}$.

**The trace identities.** In the $\gamma$ reading, with $g=\mathrm{diag}(+1,-1,-1,-1)$ and $\epsilon_{0123}=+1$,

$$
\{\gamma_\mu,\gamma_\nu\}=2g_{\mu\nu}I_4,\qquad
(\gamma_k)^2=-I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu,\gamma_5\}=0,
$$

$$
\mathrm{tr}(\gamma_\mu\gamma_\nu)=4g_{\mu\nu},\qquad
\mathrm{tr}(\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)
=4\bigl(g_{\mu\nu}g_{\rho\sigma}-g_{\mu\rho}g_{\nu\sigma}+g_{\mu\sigma}g_{\nu\rho}\bigr),
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

The central grading $\chi_{\mathrm{ad}}:=i\tilde\Xi_{\mathrm{ad}}$ is a different object from the chirality cell $\chi$, and the two must not be read as one. Here $\tilde\Xi_{\mathrm{ad}}$ is a central root of $-e_t$, so $\tilde\Xi_{\mathrm{ad}}^2=-e_t$ and $\chi_{\mathrm{ad}}^2=i^2\tilde\Xi_{\mathrm{ad}}^2=(-1)(-e_t)=e_t$; equivalently, $\chi_{\mathrm{ad}}$ is the difference of the two central idempotents of the complexified algebra. Being central, it acts on the Dirac module as a sign, and its representative there is $\gamma_5$. The chirality cell $\chi$ acts on that same module exactly as $\gamma_5$ acts; what the two-sided reading adds is not a second operator but the frame in which the mass can act by right multiplication.

Read over $\mathbb{R}$ rather than $\mathbb{C}$, the cells generate a real Clifford algebra of sixteen dimensions, and its complexification is the whole of $M_4(\mathbb{C})$. The algebra $\mathbb{B}$ itself is the eight-dimensional real algebra $M_2(\mathbb{C})$, the complexified quaternions. That complexification is what lets the cells and the gammas be the same objects, and it is why no larger algebra is needed.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

Bhabha scattering, $e^+e^-\to e^+e^-$, is the tree-level electron–positron process with two diagrams, $t$-channel scattering and $s$-channel annihilation, contributing with a relative negative sign. Its spin-averaged cross section is $(\pi\alpha^2/s)[u^2(1/s+1/t)^2+(t/s)^2+(s/t)^2]$ below the $Z$ scale, equal to $(\pi\alpha^2/s)[(s^2+u^2)/t^2+(t^2+u^2)/s^2+2u^2/(st)]$; the interference term is negative because $st<0$. At small angles the $1/t^2$ term dominates, $d\sigma/d(\cos\theta)\sim2\pi\alpha^2s/t^2$, which is why the process is the luminosity monitor of electron–positron colliders. By crossing symmetry it is the same amplitude as Møller scattering in the permuted Mandelstam variables, term for term.

In the biquaternion framework the amplitude is the contraction of material-sector currents by the quantized photon propagator, in the exchange and annihilation channels. The external states solve the one-sided chiral pair; the two-sided reading replaces the mass by the chirality cell, and the four-component reading is the momentum-cell equation. The two structures the framework owns are the **fermion sign**, which is the antisymmetry of the mode algebra established by the canonical-quantization article, and **charge conjugation**, the real structure $\mathcal C$ on the doubled module that relates the annihilation channel to the exchange channel and the Bhabha process to the Møller process. The $s$-channel annihilation current is the doorway to positronium, which the corpus does not yet treat. The framework supplies the components and the symmetries; the trace evaluation is the cell algebra of *The Gamma Formulation*, while the $Z$ exchange and the bound-state spectrum remain outside its established content, and no framework-specific prediction is claimed.

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
| $L_aR_b$ | Two-sided cell, $L_aR_b\psi=a\psi b$ |
| $\Gamma_t=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}=iR_{\vec e_x}^{\mathrm{axf}}$, $\Gamma_k=iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ | Four frame cells |
| $\Gamma^t=\Gamma_t$, $\Gamma^k=-\Gamma_k$ | Raised-index cells |
| $\chi=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}=-iR_{\vec e_z}^{\mathrm{axf}}$ | Chirality cell; $\chi^2=e_t$ |
| $P=p_0\Gamma_t-\sum_kp_k\Gamma_k$ | Momentum cell; $P^2=(p_0^2-\vec p^2)L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ |
| $D(p)=P(p)+m\,L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ | Spin-sum cell, $D(p)=\sum_r w^{(r)}(p)\bar w^{(r)}(p)$ |
| $w^{(r)}(p)$, $\bar w=w^\dagger iR_{\vec e_x}^{\mathrm{axf}}$ | Electron spinor and Dirac adjoint |
| $v^{(r)}(k)$, $\bar v=v^\dagger iR_{\vec e_x}^{\mathrm{axf}}$ | Positron spinor and Dirac adjoint |
| $\mathcal M_t,\mathcal M_s$ | Exchange and annihilation amplitudes |
| $\mathcal M=\mathcal M_t+\mathcal M_s$ | Total amplitude with the relative sign |
| $\overline{|\mathcal M|^2}$ | Spin-averaged squared matrix element, factor $\tfrac14$ included |
| $T_t,T_s,T_{ts}$ | Trace combinations of the spin sum |
| $\mathrm{Tr}$ | Trace on the four-dimensional complex module of the cells |
| $\tilde J\in\mathbb M_-$ | Framework's material-sector current |
| $\mathcal C$ | Charge-conjugation real structure on $\Delta=S\oplus\bar S$ |
| $g=\mathrm{diag}(+1,-1,-1,-1)$ | Clifford metric of the frame cells |
| $i^2=-1$ | Central imaginary of $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |

## Further Reading

- H. J. Bhabha, "The scattering of positrons by electrons with exchange on Dirac's theory of the positron," *Proceedings of the Royal Society A* **154** (1936) 195–206, for the original derivation.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the spinor algebra of electron–positron scattering.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the cross section, crossing symmetry and the annihilation channel.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the trace identities and the relative sign of the exchange and annihilation diagrams.
- The companion articles of this series: [Møller Scattering in Biquaternionic Form](moller-scattering-in-biquaternionic-form.html), [The Relativistic Two-Body Problem in Biquaternionic Form](the-relativistic-two-body-problem-in-biquaternionic-form.html), [The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism](the-minimal-coupling-of-the-biquaternion-dirac-field-to-electromagnetism.html), [Canonical Quantization of the Biquaternion Dirac Field](canonical-quantization-of-the-biquaternion-dirac-field.html), [Canonical Quantization of the Biquaternion Maxwell Field](canonical-quantization-of-the-biquaternion-maxwell-field.html), [The Feynman Propagator in Biquaternionic Form](the-feynman-propagator-in-biquaternionic-form.html), and [Real Spinors and Reality Conditions with Inner Conjugation](../articles_maths/real-spinors-and-reality-conditions-with-inner-conjugation.html).
