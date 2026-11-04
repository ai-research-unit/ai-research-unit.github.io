# __Møller Scattering in Biquaternionic Form__

## Introduction

**Møller scattering** is electron–electron scattering, $e^-e^-\to e^-e^-$, in quantum electrodynamics. Christian Møller derived it in 1932, in the same paper that treated the passage of fast electrons through matter. It is the paradigmatic two-electron process: the electron repulsion inside the helium atom is its non-relativistic face, and electron–electron colliders were built around it. At the tree level it receives two contributions, the **$t$-channel** and **$u$-channel** diagrams in which the two electrons exchange a photon. The two diagrams differ by the exchange of the two final electrons and therefore enter with a relative **minus sign**, the Pauli exchange sign of identical fermions. By **crossing symmetry** the Møller amplitude and the Bhabha amplitude, $e^+e^-\to e^+e^-$, are the same amplitude read with different particle labels; the companion article *Bhabha Scattering in Biquaternionic Form* uses that correspondence.

This article treats Møller scattering in the biquaternion framework. The framework's contribution is structural. Its minimal-coupling and quantization articles supply the ingredients — a $\mathrm{U}(1)$ coupling localised in the centre, a quantized Maxwell field, a Fock space with creation and annihilation operators, and a propagator — and the Møller amplitude is then a product of **two material-sector currents** contracted by the photon propagator. The **relative minus sign** between the two diagrams is the antisymmetry of fermion exchange, which the framework's canonical quantization already carries as the identity $(a^{\mathrm{fop}\dagger})^2=0$ on the mode algebra. And **crossing symmetry** is the framework's charge conjugation on the doubled module, read backwards. What the framework does not do is evaluate loops: the corpus's scattering content is tree-level, and the present article stays there.

Every vertex below is written with the two-sided cells $L_aR_b$, with $L_a\psi=a\psi$ and $R_b\psi=\psi b$. The five Clifford generators appear only in *The Legacy Gamma Formulation*, where they are identified with five of those cells; the body uses only the cells. Throughout, $i^2=-1$ is the central imaginary of $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, so every $i$ in a cell is that one central unit and no separate matrix imaginary enters.

The article is organised as follows. The next section sets up the two diagrams, the kinematics and the minus sign. The third computes the spin-summed matrix element. The fourth gives the cross section and its two limits. The fifth treats the weak correction and the parity-violating asymmetry. The sixth is the biquaternion interpretation. The seventh collects the Clifford dictionary that the traces use. The closing sections are the open questions, the summary, the notation table and the literature.

## The Process and Its Two Diagrams

### Kinematics

Let the incoming electrons carry four-momenta $p_1,p_2$ and the outgoing electrons $p_3,p_4$, with $p_i^2=m^2$ and $m=m_e$. The algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with $e_t=1$, $\vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t$, and central imaginary $i$, $i^2=-1$. A two-sided multiplication is a **cell**,

$$
L_a\psi=a\psi,\qquad R_b\psi=\psi b,\qquad L_aR_b\psi=a\psi b,\qquad L_aR_bL_cR_d=L_{ac}R_{db}.
$$

The four frame cells of the current are

$$
\Gamma_t:=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}=iR_{\vec e_x}^{\mathrm{axf}},\qquad
\Gamma_k:=iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\quad(k=1,2,3),
$$

with $(\vec e_1,\vec e_2,\vec e_3)=(\vec e_x,\vec e_y,\vec e_z)$. Each $\Gamma_\mu$ carries exactly one factor of the central $i$, so each square spends $i^2=-1$ once, and the remaining signs come from $\vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t$:

$$
\Gamma_t^2=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}},\qquad
\Gamma_k^2=-L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}},\qquad
\{\Gamma_\mu,\Gamma_\nu\}=2g_{\mu\nu}L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}},
$$

with $g=\mathrm{diag}(+1,-1,-1,-1)$; the anticommutator is the quaternion rule $\vec e_j\vec e_k=-\vec e_k\vec e_j$ for $j\ne k$. The cells are two-sided: $\Gamma_t$ has the central left multiplier $e_t$ and is therefore a pure right multiplication, while the three spatial cells $\Gamma_k$ have a non-central left multiplier and use both sides. The fifth frame cell, the **chirality cell**, is $-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}=-iR_{\vec e_z}^{\mathrm{axf}}$; it is also a pure right multiplication and anticommutes with the four cells.

The **momentum cell** of a four-momentum $p=(p_0,p_1,p_2,p_3)$ is

$$
P:=p_0\Gamma_t-\sum_{k=1}^3 p_k\Gamma_k
=p_0\,iR_{\vec e_x}^{\mathrm{axf}}-\sum_{k=1}^3 p_k\,iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},
$$

which is the slashed momentum read in these cells, $P=p_\mu\Gamma^\mu$ with $p_\mu=(p_0,p_1,p_2,p_3)$ and $\Gamma^k=-\Gamma_k$. Its square is central,

$$
P^2=(p_0^2-\vec p^2)\,L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}},
$$

and the mass-shell condition is $P^2=m^2L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$, that is $p_0^2-\vec p^2=m^2$.

The **Mandelstam variables** are

$$
s = (p_1+p_2)^2 = (p_3+p_4)^2,
\qquad
t = (p_1-p_3)^2 = (p_4-p_2)^2,
\qquad
u = (p_1-p_4)^2 = (p_3-p_2)^2,
$$

and for equal masses they satisfy the identity

$$
s + t + u = 4m^2 .
$$

The centre-of-momentum configuration used below is

$$
p_1 = (E,0,0,p),\quad p_2 = (E,0,0,-p),\quad
p_3 = (E,p\sin\theta,0,p\cos\theta),\quad p_4 = (E,-p\sin\theta,0,-p\cos\theta),
$$

with $E^2 = m^2+p^2$ and $E_{\mathrm{CM}} = 2E$, so that

$$
s = 4E^2 = E_{\mathrm{CM}}^2,
\qquad
t = 2p^2(\cos\theta-1) = -4p^2\sin^2\tfrac{\theta}{2},
\qquad
u = -2p^2(\cos\theta+1) = -4p^2\cos^2\tfrac{\theta}{2}.
$$

Both $-t$ and $-u$ are positive and vanish at one end of the angular range, $-t$ at $\theta=0$ and $-u$ at $\theta=\pi$; this is what makes $1/t$ and $1/u$ the two photon propagators and $y:=-t/s$ the inelasticity, equal to $\sin^2(\theta/2)$ up to $m^2/E^2$.

### The two Dirac equations of the external states

The external spinors satisfy the massive Dirac equation, but in the biquaternion algebra that equation is not a single line.

**The chiral pair.** It is first a pair of one-sided equations

$$
\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L,
\qquad
\tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R,
$$

where $\tilde\nabla=e_t\partial/\partial Q_t+\sum_k\vec e_k\partial/\partial Q_k$ is the biquaternionic gradient and $\tilde\nabla^{\natural}$ is its quaternion conjugate. At $m=0$ the two lines decouple into the two Weyl equations $\tilde\nabla\tilde\Psi_R=0$ and $\tilde\nabla^{\natural}\tilde\Psi_L=0$, one for each chirality. The mass is the only term that couples them, and it couples them off the diagonal. Both gradients act from the left, so this pair is **one-sided**.

**The two-sided form.** Read on the whole algebra rather than on the module, the same physics is the single equation

$$
L_{\tilde\nabla^{\natural}}F=m\,L_{e_t}^{\mathrm{axf}}R_{-i\vec e_z}^{\mathrm{axf}}\bar F=m\,\chi\bar F,
\qquad
\chi:=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}=-iR_{\vec e_z}^{\mathrm{axf}},
$$

with $\bar F$ the coefficient conjugate and $\chi$ the **chirality cell**, the two-sided multiplier by $e_t$ on the left and by $-i\vec e_z$ on the right. The derivative acts on the left, the mass acts on the right, and the conjugation supplies the antilinear part; the second field of the pair is the conjugate of the first, $-i\bar F\vec e_z$. The two forms are related by a change of representation but they are different operators: the pair is linear in the field, the two-sided form is antilinear in $F$ because the mass term carries $\bar F$. The pair is what the external spinors below solve; the two-sided form is the algebra's own reading of the same mass.

**The four-component form.** In the frame cells, with $P=p_0\Gamma_t-\sum_kp_k\Gamma_k$ and the mass read as the central cell $m\,L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$, the pair is written as the single four-component equation

$$
\bigl(P-m\,L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}\bigr)w=0,
$$

and the spin sum below is the sum over its two positive-frequency solutions. This is the pair written once; its two lines are the two chiral halves. It is not the two-sided equation: there the mass is a right multiplication by the chirality cell, here it is the central multiplier $m$. The two agree on the module, where the right multiplication by $-i\vec e_z$ separates the two chiralities, as the chiral grading of the four-component spinor does.

### The two amplitudes and the minus sign

The vertex current of an electron of incoming momentum $p_{\mathrm{in}}$ and outgoing momentum $p_{\mathrm{out}}$ is

$$
J_\mu(p_{\mathrm{out}},p_{\mathrm{in}}):=\bar w(p_{\mathrm{out}})\,\Gamma_\mu\,w(p_{\mathrm{in}}),
\qquad
\bar w:=w^\dagger iR_{\vec e_x}^{\mathrm{axf}},
$$

with $\Gamma_\mu$ the cell of the Lorentz index $\mu$ and $\bar w$ the Dirac adjoint, whose factor $iR_{\vec e_x}^{\mathrm{axf}}=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$ is the Clifford-odd cell outside $\mathbb{B}$. The contraction is the Hermitian pairing of two module elements, so every $J_\mu$ is a single complex number and the brackets below are ordinary complex products. With this notation the $t$-channel and $u$-channel brackets are

$$
\mathcal M_t=\frac{e^2}{t}\Bigl[J_t(p_3,p_1)J_t(p_4,p_2)-\sum_{k=1}^3 J_k(p_3,p_1)J_k(p_4,p_2)\Bigr],
$$

$$
\mathcal M_u=\frac{e^2}{u}\Bigl[J_t(p_3,p_2)J_t(p_4,p_1)-\sum_{k=1}^3 J_k(p_3,p_2)J_k(p_4,p_1)\Bigr].
$$

The two brackets differ by the exchange of the two electron lines: $\mathcal M_u$ is obtained from $\mathcal M_t$ by swapping the initial momenta, $p_1\leftrightarrow p_2$, or equivalently the final momenta, $p_3\leftrightarrow p_4$. Because the two electrons are identical, the exchange costs a minus sign, and the total amplitude is

$$
\boxed{\;\mathcal M=\mathcal M_t-\mathcal M_u\;},
$$

where the amplitude $\mathcal M$ is the invariant matrix element, normalised so that $i\mathcal M$ times the momentum-conservation delta is the $S$-matrix element. This single sign is the whole of the interference structure: it is why the $u$-channel is a subtraction rather than an addition, and it is the sign that distinguishes the identical-fermion cross section from the distinguishable-particle one.

## The Spin-Summed Matrix Element

Squaring and averaging over the two initial spins and summing over the two final spins — a factor $\tfrac14$ — gives the following. With the spin-sum cell

$$
D(p):=P+m\,L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}
=p_0\,iR_{\vec e_x}^{\mathrm{axf}}-\sum_{k=1}^3 p_k\,iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}+m\,L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}},
$$

the spin sum is

$$
\sum_{r=1}^{2} w^{(r)}(p)\,\bar w^{(r)}(p)=D(p),
$$

and the three trace combinations are

$$
L_t:=\mathrm{Tr}\bigl[\Gamma^\mu D(p_1)\Gamma^\nu D(p_3)\bigr]\,
\mathrm{Tr}\bigl[\Gamma_\mu D(p_2)\Gamma_\nu D(p_4)\bigr],
$$

$$
L_u:=\mathrm{Tr}\bigl[\Gamma^\mu D(p_2)\Gamma^\nu D(p_3)\bigr]\,
\mathrm{Tr}\bigl[\Gamma_\mu D(p_1)\Gamma_\nu D(p_4)\bigr],
$$

$$
L_{tu}:=\mathrm{Tr}\bigl[D(p_3)\Gamma^\mu D(p_1)\Gamma^\nu D(p_4)\Gamma_\mu D(p_2)\Gamma_\nu\bigr],
$$

where $\Gamma^t=\Gamma_t$ and $\Gamma^k=-\Gamma_k$, and $\mathrm{Tr}$ is the trace on the four-dimensional complex module $\mathbb{B}$ that the cells act on, so no gamma enters the body. Then

$$
\frac14\sum_{\mathrm{spins}}|\mathcal M|^2
=\frac{e^4}{4}\left(\frac{L_t}{t^2}+\frac{L_u}{u^2}-\frac{2L_{tu}}{tu}\right).
$$

The traces are evaluated with the standard four-dimensional identities, which follow from the Clifford relations of the frame cells alone,

$$
\mathrm{Tr}(\Gamma_\mu\Gamma_\nu)=4g_{\mu\nu},\qquad
\mathrm{Tr}(\Gamma_\mu\Gamma_\nu\Gamma_\rho\Gamma_\sigma)
=4\bigl(g_{\mu\nu}g_{\rho\sigma}-g_{\mu\rho}g_{\nu\sigma}+g_{\mu\sigma}g_{\nu\rho}\bigr),
$$

with odd traces vanishing; *The Legacy Gamma Formulation* records them with the rest of the dictionary. Evaluating the three traces gives the closed form, in which the factor $\tfrac14$ of the spin average is already included:

$$
\begin{aligned}
\overline{|\mathcal M|^2} = 2e^4\Bigl\{&
\frac{s^2+u^2-8m^2(s+u)+24m^4}{t^2}\\
&+\frac{s^2+t^2-8m^2(s+t)+24m^4}{u^2}
+\frac{2(s^2-8m^2s+12m^4)}{tu}\Bigr\}.
\end{aligned}
$$

Each of the three terms has the same anatomy: the two trace factors are the two electron **currents** contracted with each other through the photon propagator's $1/t$ or $1/u$, and the cross term is the interference. The interference carries the exchange sign squared, so its sign is not fixed by the amplitude but by the kinematics: since $tu>0$, the cross term has the sign of $s^2-8m^2s+12m^4$, whose roots are $s=2m^2$ and $s=6m^2$, so on the physical range it is negative for $4m^2\le s<6m^2$ and positive above, that is, negative while $p^2<m^2/2$ and positive for $p^2>m^2/2$. The interference is therefore **destructive** in the non-relativistic region and **constructive** in the ultrarelativistic one, and the change of sign is one reason the two limits below have such different angular shapes. In Bhabha scattering the cross term, in the same normalisation $\overline{|\mathcal M|^2}=2e^4\{\ldots\}$, is $+\,2u^2/(st)$ with $u$ the crossed invariant of the companion article; once the overall $2e^4$ is distributed it reads $4u^2/(st)$, and since $st<0$ it is negative at every energy, so there the annihilation interference is destructive throughout.

## The Cross Section and Its Limits

The unpolarized differential cross section follows from the standard two-body flux factor, with equal masses so that the momentum ratio is one,

$$
\frac{d\sigma}{d\Omega} = \frac{1}{64\pi^2 E_{\mathrm{CM}}^2}\,\overline{|\mathcal M|^2},
\qquad
\alpha=\frac{e^2}{4\pi},
$$

inserting the centre-of-momentum Mandelstam variables. In the two limits it takes instructive forms.

**Non-relativistic limit** ($m\gg p$, to leading order in $p^2/m^2$, with $E_{\mathrm{CM}}\simeq2m$):

$$
\boxed{\;
\frac{d\sigma}{d\Omega} = \frac{m^4\alpha^2}{E_{\mathrm{CM}}^2\,p^4\sin^4\theta}\,(1+3\cos^2\theta)\;},
$$

a Rutherford-like $1/\sin^4\theta$ law modulated by the $(1+3\cos^2\theta)$ factor. That factor is the spin average of two Rutherford amplitudes. Write $f(\theta)\propto\sin^{-2}(\theta/2)$ for the direct one and $f(\pi-\theta)\propto\cos^{-2}(\theta/2)$ for the exchanged one; the three triplet spin states go with the antisymmetric spatial combination and the singlet with the symmetric one, so

$$
\tfrac34\bigl|f(\theta)-f(\pi-\theta)\bigr|^2+\tfrac14\bigl|f(\theta)+f(\pi-\theta)\bigr|^2
=|f|^2\left[\frac{1}{\sin^4\tfrac\theta2}+\frac{1}{\cos^4\tfrac\theta2}-\frac{1}{\sin^2\tfrac\theta2\cos^2\tfrac\theta2}\right]
=\frac{4\,|f|^2\,(1+3\cos^2\theta)}{\sin^4\theta},
$$

which is the $(1+3\cos^2\theta)$ of the box. A spinless electron would instead give the antisymmetric combination alone, and its cross section would vanish at $\theta=\pi/2$. It is the quantum-mechanical electron–electron repulsion behind the helium atom, with the exchange factor.

**Ultrarelativistic limit** ($m\ll p$, to leading order in $m^2/p^2$):

$$
\frac{d\sigma}{d\Omega} = \frac{\alpha^2}{E_{\mathrm{CM}}^2\,\sin^4\theta}\,(3+\cos^2\theta)^2 .
$$

Both ends of the angular range carry a $1/\sin^4\theta$ factor under the exchange factor $(3+\cos^2\theta)^2$, and both ends are genuine Coulomb singularities: $t=0$ at $\theta=0$ is the direct photon, $u=0$ at $\theta=\pi$ is the exchanged one, since backward scattering of one electron is forward scattering of the other. The electron mass regulates neither — $u=-4p^2\cos^2(\theta/2)$ vanishes at $\theta=\pi$ for every $p$ — so only a detector's angular acceptance makes the cross section finite, and with a fixed cut the total cross section falls as $\alpha^2/s$ up to logarithms from the interference.

## The Weak Correction and Parity Violation

At energies below the $Z$ mass the process is described by QED, but the full electroweak theory adds two further tree-level diagrams with $Z$-boson exchange. Because the weak interaction is **left-handed** while the electromagnetic one is parity-symmetric, the $Z$ contribution makes the cross section different for left- and right-handed incoming electrons. For a polarized electron beam on an unpolarized target the **parity-violating asymmetry** is

$$
A_{\mathrm{PV}}\equiv\frac{\sigma_L-\sigma_R}{\sigma_L+\sigma_R},
$$

where $\sigma_L$ and $\sigma_R$ are the cross sections for left- and right-handed incident electrons.

The $Z$ couples to the electron with $g_V^e=-\tfrac12Q_W^e$ and $g_A^e=-\tfrac12$. At $Q^2\ll M_Z^2$ its propagator collapses to $-1/M_Z^2$, so the $Z$ amplitude is $-\sqrt2G_{\mathrm F}$ times the same two currents with $\Gamma_\mu\to\Gamma_\mu(g_V^e-g_A^e\chi)$, the axial part being the vector current with the chirality cell $\chi$ inserted. The asymmetry is twice the interference of the $Z$ amplitude with the photon amplitude, divided by the photon amplitude squared. Three facts follow at once, and they are the anatomy of the boxed result below: the interference carries exactly one power of $G_{\mathrm F}$ and one factor $1/\alpha$ from the two photon vertices; it is proportional to the product $g_V^eg_A^e=\tfrac14Q_W^e$, so a parity-symmetric $Z$ coupling would give nothing; and the kinematic factor is $Q^2$, which in a fixed-target experiment is $Q^2=2m_eE_{\mathrm{beam}}y$, hence the $m_eE_{\mathrm{beam}}$ in front and the $y$-dependence behind.

At tree level the asymmetry is therefore

$$
\boxed{\;
A_{\mathrm{PV}} = -\,m_eE_{\mathrm{beam}}\,\frac{G_{\mathrm F}}{\sqrt2\,\pi\alpha}\,
\frac{4\sin^2\theta}{\left(3+\cos^2\theta\right)^2}\,
Q_W^e\;},
\qquad
Q_W^e=1-4\sin^2\theta_{\mathrm W},
$$

with $Q_W^e$ the weak charge of the electron, $E_{\mathrm{beam}}$ the beam energy in the laboratory — not the centre-of-mass energy $E$ of the kinematics above, since $m_eE_{\mathrm{beam}}=Q^2/(2y)$ in a fixed-target experiment — and $\theta$ the centre-of-mass scattering angle. The same formula in terms of the inelasticity $y=-t/s$, equal to $\sin^2(\theta/2)$ up to $m^2/E^2$, is

$$
A_{\mathrm{PV}} = -\,m_eE_{\mathrm{beam}}\,\frac{G_{\mathrm F}}{\sqrt2\,\pi\alpha}\,
\frac{2y(1-y)}{1+y^4+(1-y)^4}\,Q_W^e,
$$

and the two forms agree by $4\sin^2\theta/(3+\cos^2\theta)^2=2y(1-y)/(1+y^4+(1-y)^4)$. With the definition adopted here, $A_{\mathrm{PV}}$ is negative for $Q_W^e>0$; MOLLER quotes the same number with the opposite convention $(\sigma_R-\sigma_L)/(\sigma_R+\sigma_L)$ and the opposite overall sign. The asymmetry is of order $10^{-7}$, a hundred parts per billion, because $m_eE_{\mathrm{beam}}\sim10^{-2}$ GeV$^2$ and $G_{\mathrm F}/(\sqrt2\pi\alpha)\sim4\times10^{-4}$ GeV$^{-2}$.

It was measured at SLAC (E158), which finds $A_{\mathrm{PV}}=-131\pm14\pm10$ parts per billion and determines $\sin^2\theta_{\mathrm W}$; the approved MOLLER experiment at Jefferson Laboratory is designed for $E_{\mathrm{beam}}=11$ GeV, where the same formula gives $A_{\mathrm{PV}}\approx-4\times10^{-8}$, forty parts per billion. The first discussion is due to Zel'dovich (1959). It is the cleanest experimental reason Møller scattering is still studied, and it is the physical content of the framework's statement that the photon coupling is parity-symmetric while a left-handed coupling is not.

## The Biquaternion Reading

### The amplitude as a product of two material-sector currents

The framework's minimal-coupling article writes the electromagnetic coupling of the biquaternion Dirac field through the four-potential and identifies the conserved current as the spinor-module bilinear

$$
j_\mu=\bar\psi\,\Gamma_\mu\,\psi,
\qquad
\bar\psi=\psi^\dagger iR_{\vec e_x}^{\mathrm{axf}},
$$

where $\Gamma_\mu$ are the four frame cells of the Kinematics, $\Gamma_t=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$ and $\Gamma_k=iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$. The current is a material-sector object, $\tilde J=ic\,j_0e_t+\vec j\in\mathbb M_-$, but its Dirac adjoint uses the Clifford-odd cell $iR_{\vec e_x}^{\mathrm{axf}}$, which lies outside $\mathbb{B}$; the naive product $i\tilde\Psi\tilde\Psi^{*}$ is in $\mathbb M_-$ and is not conserved. The Møller amplitude is the second-quantized version of that structure. Each vertex $\bar w(p_{\mathrm{out}})\Gamma_\mu w(p_{\mathrm{in}})$ is one electron current, and the two currents are contracted by the photon propagator $1/t$ or $1/u$. The framework's Maxwell field supplies the photon line: its canonical-quantization article constructs the quantized Maxwell field, and the photon propagator $1/t$ or $1/u$ is the standard two-point function of that field. The amplitude is the framework's current, twice, joined by the framework's photon. Nothing in this is a new prediction; it is the identification of the components.

### The relative minus sign is the mode algebra's antisymmetry

The single structural feature the framework owns here is the exchange sign. The corpus's canonical-quantization article of the Dirac field obtains **Pauli exclusion as the algebraic identity** $(a^{\mathrm{fop}\dagger}_r)^2=0$, together with the $\mathbb Z/2$ grading of the mode algebra by fermion parity. That identity is exactly the statement that two fermionic mode operators anticommute, and the relative minus sign between the $t$- and $u$-channel amplitudes is its momentum-space consequence: exchanging two identical external fermions costs a sign. The framework therefore does not merely transcribe the minus sign; the sign is the shadow of the graded structure the corpus establishes on the operator algebra. This is the same $\mathbb Z/2$ grading that the corpus's KMS and fermion-parity articles treat.

### Crossing symmetry is charge conjugation

The Møller and Bhabha amplitudes are related by **crossing symmetry**: moving an incoming electron to an outgoing positron, with reversed four-momentum, changes one process into the other. In the framework this operation is the **charge conjugation** real structure $\mathcal C$ on the doubled module $\Delta = S\oplus\bar S$ of the companion article *Real Spinors and Reality Conditions with Inner Conjugation*; a particle line is replaced by an antiparticle line, and the amplitude's analytic continuation in the Mandelstam variables is the momentum-space face of the same relabelling. The numerical check reported in the companion Bhabha article — the two amplitudes agreeing once the Mandelstam roles are permuted — is therefore a check of the framework's particle–antiparticle relabelling as much as of the algebra of the frame cells. The companion Bhabha article states the correspondence from the other side.

### What the framework supplies and what it does not

The framework supplies the two vertex currents, the photon propagator, the Fock space in which the external states live, and the exchange sign as the antisymmetry of its mode algebra. It does **not** supply the numerical evaluation of the traces as a derivation from its own structure — the trace algebra is the cell dictionary of *The Legacy Gamma Formulation* — nor does it supply the $Z$-exchange diagrams, which belong to the framework's electroweak research agenda rather than to its established content. The parity-violating asymmetry above is quoted as the experimental fact that motivates the left-handed coupling; the corpus's chiral-fermion article discusses the framework's treatment of handedness, and the electroweak article collects the open questions. No framework-specific prediction is claimed.

## Open Questions

1. **The traces as algebra.** Can the three trace combinations be reorganised as products of the framework's own currents in $\mathbb M_-$, so that neither the frame cells nor the module trace appear — and does the $\mathbb M_-$ restriction of the currents reproduce the standard results identically?

2. **The exchange sign from first principles.** The corpus obtains Pauli exclusion on the mode algebra. Is there a corresponding statement on the **classical** biquaternion field (a graded-commutativity of the field's components) from which the momentum-space minus sign follows without quantizing?

3. **Crossing and $\mathcal C$.** Is the Mandelstam analytic continuation of the framework's amplitude literally the action of $\mathcal C$ on the external states, or only the same relabelling at the level of the on-shell spinors?

4. **The weak asymmetry.** The corpus's electroweak agenda lists the framework's internal $SU(2)\times \mathrm{U}(1)$ questions; the Møller $A_{\mathrm{PV}}$ is a concrete target. Does the framework's left-handed coupling reproduce the $(1/4-\sin^2\theta_{\mathrm W})$ coefficient, or only the general form?

5. **Loops.** The corpus's Ward–Takahashi and Schwinger–Dyson articles treat the identities a loop computation must satisfy, but no loop amplitude is evaluated. Whether Møller scattering at one loop can be organised in the framework without new structure is open.

6. **The two chiral sums.** The spin sum $D(p)=P+m\,L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ is the four-component reading of the chiral pair. Can the positive- and negative-frequency sums be written as two separate cell sums, one for each chiral half, without passing through the four-component spinor?

7. **Empirical contact.** The tree-level result is standard electrodynamics in the framework's variables; the parity-violating asymmetry is the one place the framework meets a measured number, and it is not a framework-specific prediction.

## The Legacy Gamma Formulation

This section fixes the dictionary that the traces above use, and nothing here is needed outside it.

The five $\gamma$'s are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, so they are elements of the same algebra as the cells, not of a larger one. Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\psi=a\psi$ and $R_b\psi=\psi b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products.

$$
\gamma_0=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad \gamma_1=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_2=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_3=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_5=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}} .
$$

The same in the axis-free display:

$$
\gamma_0=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\quad \gamma_1=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_2=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_3=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_5=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}} .
$$

The body's cells are the same objects: $\Gamma_t=\gamma_0$, $\Gamma_k=\gamma_k$ for $k=1,2,3$, and the chirality cell is $\gamma_5$.

A single product is a pure tensor; in the sixteen-dimensional coefficient space the products form the seven-dimensional cone of coefficient rank at most one. A general element is a sum of at most four products; its **length** $\ell(M)$ is the least number of products in such a sum. The **matrix rank** of $M$ on the regular module is a different number: for a single cell $L_QR_P$ it is $\operatorname{rank}\mathsf M_2(Q)\operatorname{rank}\mathsf M_2(P)$, and it lies in $\{0,1,2,4\}$. The two numbers are independent.

$\gamma_5$ is the chirality cell itself, $-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$, so the fifth cell and the fifth gamma are one object seen in two readings. The central grading $\chi_{\mathrm{ad}}:=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi_{\mathrm{ad}}^2=e_t$ — is a different object; it merely has the same representative $\gamma_5$ on the Dirac module, so that the two central idempotents correspond to the two chiral projectors and $\chi$ is the module representative of $\chi_{\mathrm{ad}}$.

The dictionary $M\mapsto c(M)$ is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The identities the body cites.** In the $\gamma$ reading, with $g=\mathrm{diag}(+1,-1,-1,-1)$ and $\epsilon_{0123}=+1$,

$$
\{\gamma_\mu,\gamma_\nu\}=2g_{\mu\nu}I_4,\qquad
(\gamma_k)^2=-I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu,\gamma_5\}=0,
$$

$$
[\gamma_\mu,\gamma_\nu]=2\gamma_\mu\gamma_\nu\quad(\mu\ne\nu),\qquad
[\gamma_a,S_{cd}]=g_{ac}\gamma_d-g_{ad}\gamma_c,\qquad
S_{cd}=\tfrac14[\gamma_c,\gamma_d],
$$

$$
\mathrm{tr}(\gamma_\mu\gamma_\nu)=4g_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$

$$
\mathrm{tr}(\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)
=4\bigl(g_{\mu\nu}g_{\rho\sigma}-g_{\mu\rho}g_{\nu\sigma}+g_{\mu\sigma}g_{\nu\rho}\bigr).
$$

Each $\gamma$ is a cell with one factor of $i$; the squares use $i^2=-1$.

The four contraction sums depend on the frame, because the sign of a cell's square depends on the frame. In the Euclidean frame, where every generator squares to $+I_4$,

$$
\sum_\mu\gamma_\mu\gamma_\mu=4I_4,\qquad
\sum_\mu\gamma_\mu\gamma_\alpha\gamma_\mu=-2\gamma_\alpha,
$$

$$
\sum_\mu\gamma_\mu\gamma_\alpha\gamma_\beta\gamma_\mu=4\delta_{\alpha\beta}I_4,\qquad
\sum_\mu\gamma_\mu\gamma_\alpha\gamma_\beta\gamma_\gamma\gamma_\mu=-2\gamma_\gamma\gamma_\beta\gamma_\alpha .
$$

In the Lorentzian frame the metric enters, and the first sum is $\sum_\mu\gamma_\mu\gamma_\mu=-2I_4$.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

Møller scattering, $e^-e^-\to e^-e^-$, is the tree-level exchange of a photon between two electrons, contributing through $t$-channel and $u$-channel diagrams that combine with the relative minus sign of identical-fermion exchange. The Mandelstam variables satisfy $s+t+u=4m^2$; the spin-summed matrix element is three terms, two of them products of traces over the photon propagators and one the interference, whose sign flips from destructive to constructive at $p^2=m^2/2$; the unpolarized cross section reduces to the Rutherford-like $(1+3\cos^2\theta)/\sin^4\theta$ law at low energy and to $(3+\cos^2\theta)^2/\sin^4\theta$ at high energy. The electroweak $Z$-exchange adds a parity-violating asymmetry of order one hundred parts per billion, measured at SLAC and used to extract the weak mixing angle.

In the biquaternion framework the amplitude is the contraction of two material-sector currents — the same current the minimal-coupling article identifies — by the framework's quantized photon propagator. The two structures the framework genuinely owns are the exchange sign, which is the antisymmetry of the mode algebra established by the canonical-quantization article as $(a^{\mathrm{fop}\dagger})^2=0$ and the $\mathbb Z/2$ grading, and crossing symmetry, which is the charge-conjugation real structure $\mathcal C$ on the doubled module. The body uses no gamma: every vertex is a two-sided cell, and the massive external states satisfy a chiral pair of one-sided equations — the same physics whose two-sided reading is a single equation with the mass as a right multiplication by the chirality cell, and whose four-component reading is the ordinary Dirac equation solved by the spinors below. The framework does not evaluate loops, does not supply $Z$ exchange, and makes no framework-specific prediction; the parity-violating asymmetry is quoted as the experimental target that the framework's left-handed coupling must ultimately meet.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $e^-e^-\to e^-e^-$ | Møller scattering |
| $p_1,p_2,p_3,p_4$ | Incoming and outgoing electron four-momenta |
| $s,t,u$ | Mandelstam variables; $s+t+u=4m^2$ |
| $E_{\mathrm{CM}}=2E$ | Centre-of-momentum energy |
| $\theta$ | Centre-of-mass scattering angle |
| $\Gamma_t=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}=iR_{\vec e_x}^{\mathrm{axf}}$, $\Gamma_k=iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ | Four frame cells of the current |
| $\Gamma^t=\Gamma_t$, $\Gamma^k=-\Gamma_k$ | Raised-index cells |
| $L_aR_b$ | Two-sided multiplication, $L_aR_b\psi=a\psi b$ |
| $P=p_0\Gamma_t-\sum_kp_k\Gamma_k$ | Momentum cell; $P^2=(p_0^2-\vec p^2)L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ |
| $D(p)=P+m\,L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ | Spin-sum cell of the momentum shell |
| $w^{(r)}(p)$, $\bar w=w^\dagger iR_{\vec e_x}^{\mathrm{axf}}$ | Positive-frequency spinor and its Dirac adjoint |
| $\mathcal M_t,\mathcal M_u$ | $t$- and $u$-channel amplitudes |
| $\mathcal M=\mathcal M_t-\mathcal M_u$ | Total amplitude with the exchange sign |
| $\overline{|\mathcal M|^2}$ | Spin-averaged squared matrix element, factor $\tfrac14$ included |
| $\mathrm{Tr}$ | Trace on the four-dimensional complex module of the cells |
| $L_t,L_u,L_{tu}$ | Trace combinations of the spin sum |
| $\alpha=e^2/4\pi$ | Fine-structure constant |
| $A_{\mathrm{PV}}$ | Parity-violating asymmetry; $\theta_{\mathrm W}$ the weak mixing angle |
| $E_{\mathrm{beam}}$ | Beam energy in the laboratory, as in $m_eE_{\mathrm{beam}}$ |
| $y=Q^2/s=-t/s$ | Inelasticity; equals $\sin^2(\theta/2)$ up to $m^2/E^2$ |
| $\chi=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ | Chirality cell of the two-sided Dirac equation; $\chi^2=e_t$ |
| $G_{\mathrm F}$ | Fermi constant |
| $g_V^e=-\tfrac12Q_W^e$, $g_A^e=-\tfrac12$ | Vector and axial $Z$ couplings of the electron |
| $Q_W^e=1-4\sin^2\theta_{\mathrm W}$ | Weak charge of the electron |
| $\tilde J\in\mathbb M_-$ | Framework's conserved material-sector current |
| $\mathcal C$ | Charge-conjugation real structure on $\Delta=S\oplus\bar S$ |
| $g=\mathrm{diag}(+1,-1,-1,-1)$ | Clifford metric of the frame cells |

## Further Reading

- C. Møller, "Zur Theorie des Durchgangs schneller Elektronen durch Materie," *Annalen der Physik* **406** (1932) 531–585, for the original derivation.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the trace technology and the electron–electron cross section.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the tree-level amplitude, the Mandelstam variables and the cross section.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the trace identities and the identical-fermion exchange sign.
- P. L. Anthony *et al.*, "Precision measurement of the weak mixing angle in Møller scattering," *Physical Review Letters* **95** (2005) 081601, for the SLAC E158 measurement of the parity-violating asymmetry.
- E. Derman and W. J. Marciano, "Parity-violating asymmetries in polarized electron scattering," *Annals of Physics* **121** (1979) 147, for the tree-level asymmetry formula quoted above, with its $m_eE_{\mathrm{beam}}$, its angular factor and its weak charge.
- J. Benesch *et al.* (MOLLER Collaboration), "The MOLLER Experiment: An Ultra-Precise Measurement of the Weak Mixing Angle Using Møller Scattering," arXiv:1411.4088, for the modern statement of the asymmetry, eq. (1), and its electroweak corrections.
- Ya. B. Zel'dovich (1959), for the earliest discussion of the parity-violating asymmetry in electron–electron scattering, as E158 cites it.
- [Real Spinors and Reality Conditions with Inner Conjugation](../articles_maths/real-spinors-and-reality-conditions-with-inner-conjugation.html), for the charge-conjugation real structure $\mathcal C$ on the doubled module.
- The companion articles of this series: [Bhabha Scattering in Biquaternionic Form](bhabha-scattering-in-biquaternionic-form.html), [The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism](the-minimal-coupling-of-the-biquaternion-dirac-field-to-electromagnetism.html), [Canonical Quantization of the Biquaternion Dirac Field](canonical-quantization-of-the-biquaternion-dirac-field.html), [The Feynman Propagator in Biquaternionic Form](the-feynman-propagator-in-biquaternionic-form.html), [Canonical Quantization of the Biquaternion Maxwell Field](canonical-quantization-of-the-biquaternion-maxwell-field.html), [Fock Space and Creation/Annihilation Operators in Biquaternionic Form](fock-space-and-creation-annihilation-operators-in-biquaternionic-form.html), and [Chiral Fermions in the Biquaternion Framework](chiral-fermions-in-the-biquaternion-framework.html).
