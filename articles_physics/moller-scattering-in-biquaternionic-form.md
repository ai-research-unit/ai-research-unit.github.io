# __Møller Scattering in Biquaternionic Form__

## Introduction

**Møller scattering** is electron–electron scattering, $e^-e^-\to e^-e^-$, in quantum electrodynamics. Christian Møller derived it in 1932, in the same paper that treated the passage of fast electrons through matter. It is the paradigmatic two-electron process: the electron repulsion inside the helium atom is its non-relativistic face, and electron–electron colliders were built around it. At the tree level it receives two contributions, the **$t$-channel** and **$u$-channel** diagrams in which the two electrons exchange a photon, and the two interfere with a relative **minus sign** because the two final electrons are identical fermions. By **crossing symmetry** the Møller amplitude and the Bhabha amplitude, $e^+e^-\to e^+e^-$, are the same amplitude read with different particle labels; the companion article *Bhabha Scattering in Biquaternionic Form* uses that correspondence.

This article treats Møller scattering in the biquaternion framework. The framework's contribution is structural. Its minimal-coupling and quantization articles supply the ingredients — a $U(1)$ coupling localised in the centre, a quantized Maxwell field, a Fock space with creation and annihilation operators, and a propagator — and the Møller amplitude is then a product of **two material-sector currents** contracted by the photon propagator. The **relative minus sign** between the two diagrams is the antisymmetry of fermion exchange, which the framework's canonical quantization already carries as the identity $(\hat a^\dagger)^2=0$ on the mode algebra. And **crossing symmetry** is the framework's charge conjugation on the doubled module, read backwards. What the framework does not do is evaluate loops: the corpus's scattering content is tree-level, and the present article stays there.

The article is organised as follows. The next section sets up the two diagrams, the kinematics and the minus sign. The third computes the spin-summed matrix element. The fourth gives the cross section and its two limits. The fifth treats the weak correction and the parity-violating asymmetry. The sixth is the biquaternion reading. The closing sections are the open questions, the summary, the notation table and the literature.

## The Process and Its Two Diagrams

### Kinematics

Let the incoming electrons carry four-momenta $p_1, p_2$ and the outgoing electrons $p_3, p_4$, with the mass shell $p_i^2 = m^2$ and $\not p_i = m$ on shell, $m = m_e$. The **Mandelstam variables** are

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
t = 2p^2(\cos\theta-1),
\qquad
u = -2p^2(\cos\theta+1).
$$

### The two amplitudes and the minus sign

The $t$-channel diagram contributes

$$
i\mathcal M_t = (-ie)^2\,\bar u(p_3)\gamma^\mu u(p_1)\,\frac{-i}{t}\,\bar u(p_4)\gamma_\mu u(p_2),
$$

and the $u$-channel diagram, obtained by exchanging the two final electrons, contributes

$$
i\mathcal M_u = (-ie)^2\,\bar u(p_3)\gamma^\mu u(p_2)\,\frac{-i}{u}\,\bar u(p_4)\gamma_\mu u(p_1).
$$

Because the two final states differ only by the exchange of identical fermions, the amplitudes are combined with a relative minus sign,

$$
i\mathcal M = i(\mathcal M_t - \mathcal M_u),
$$

the **Pauli exchange sign**. This single sign is the whole of the interference structure: it removes the forward-collinear enhancement in channels where the two electrons would be identical, and it is why the $u$-channel is a subtraction rather than an addition.

## The Spin-Summed Matrix Element

Squaring and averaging over the two initial spins and summing over the two final spins — a factor $\tfrac14$ — gives

$$
\frac14\sum_{\mathrm{spins}}|\mathcal M|^2
= \frac{e^4}{4}\Big\{ \frac{1}{t^2}\operatorname{Tr}[\gamma^\mu(\not p_1+m)\gamma^\nu(\not p_3+m)]\operatorname{Tr}[\gamma_\mu(\not p_2+m)\gamma_\nu(\not p_4+m)]
$$
$$
\qquad\qquad + \frac{1}{u^2}\operatorname{Tr}[\gamma^\mu(\not p_2+m)\gamma^\nu(\not p_3+m)]\operatorname{Tr}[\gamma_\mu(\not p_1+m)\gamma_\nu(\not p_4+m)]
$$
$$
\qquad\qquad - \frac{2}{tu}\operatorname{Tr}[(\not p_3+m)\gamma^\mu(\not p_1+m)\gamma^\nu(\not p_4+m)\gamma_\mu(\not p_2+m)\gamma_\nu] \Big\},
$$

using the spin sum $\sum_s u^s(p)\bar u^s(p) = \not p+m$ and the trace identity $\operatorname{Tr}[\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma] = 4(\eta^{\mu\nu}\eta^{\rho\sigma}-\eta^{\mu\rho}\eta^{\nu\sigma}+\eta^{\mu\sigma}\eta^{\nu\rho})$, with odd traces vanishing. Evaluating the three traces gives

$$
\overline{|\mathcal M|^2} = 2e^4\Big\{ \frac{1}{t^2}\left(s^2+u^2-8m^2(s+u)+24m^4\right) + \frac{1}{u^2}\left(s^2+t^2-8m^2(s+t)+24m^4\right) + \frac{2}{tu}\left(s^2-8m^2s+12m^4\right) \Big\}.
$$

Each of the three terms has the same anatomy: the two trace factors are the two electron **currents** contracted with each other through the photon propagator's $1/t$ or $1/u$, and the cross term is the interference, with the minus sign of exchange explicit in the coefficient $-\tfrac{2}{tu}$.

## The Cross Section and Its Limits

The unpolarized differential cross section follows from the standard two-body flux factor,

$$
\frac{d\sigma}{d\Omega} = \frac{1}{64\pi^2 E_{\mathrm{CM}}^2}\,\overline{|\mathcal M|^2},
$$

inserting the centre-of-momentum Mandelstam variables. In the two limits it takes instructive forms.

**Non-relativistic limit** ($m\gg p$, so $E_{\mathrm{CM}} = 2m$):

$$
\frac{d\sigma}{d\Omega} = \frac{m^4\alpha^2}{E_{\mathrm{CM}}^2\,p^4\sin^4\theta}\,(1+3\cos^2\theta),
$$

a Rutherford-like $1/\sin^4\theta$ law modulated by the $(1+3\cos^2\theta)$ factor that is the signature of identical-fermion exchange. It is the relativistic generalisation of the electron–electron repulsion behind the helium atom.

**Ultrarelativistic limit** ($m\ll p$):

$$
\frac{d\sigma}{d\Omega} = \frac{\alpha^2}{E_{\mathrm{CM}}^2\,\sin^4\theta}\,(3+\cos^2\theta)^2 .
$$

The forward and backward singularities are $1/\sin^4\theta$, softened by the exchange factor; the total cross section falls with $s$ like $1/s$, as it must by dimensional analysis for a massless two-body amplitude.

## The Weak Correction and Parity Violation

At energies below the $Z$ mass the process is described by QED, but the full electroweak theory adds two further tree-level diagrams with $Z$-boson exchange. Because the weak interaction is **left-handed** while the electromagnetic one is parity-symmetric, the $Z$ contribution makes the cross section different for left- and right-handed incoming electrons. For a polarized electron beam on an unpolarized target this produces a small parity-violating asymmetry,

$$
A_{\mathrm{PV}} = -\,m_eE\,\frac{G_{\mathrm F}}{\sqrt2\,\pi\alpha}\,\frac{16\sin^2\Theta_{\mathrm{cm}}}{\left(3+\cos^2\Theta_{\mathrm{cm}}\right)^2}\left(\frac14-\sin^2\theta_{\mathrm W}\right),
$$

of a few hundred parts per billion. The asymmetry was measured at SLAC (E158) and provides a determination of the weak mixing angle $\sin^2\theta_{\mathrm W}$; the first discussion is due to Zel'dovich (1959). It is the cleanest experimental reason Møller scattering is still studied, and it is the physical content of the framework's statement that the photon coupling is parity-symmetric while a left-handed coupling is not.

## The Biquaternion Reading

### The amplitude as a product of two material-sector currents

The framework's minimal-coupling article writes the electromagnetic coupling of the biquaternion Dirac field through the four-potential and identifies the conserved current as the material-sector object $\tilde J\in\mathbb M_-$, with the Clifford-odd element that a pure biquaternion product does not supply. The Møller amplitude is the second-quantized version of that same structure: the two factors $\bar u(p)\gamma^\mu u(p')$ are the two electron currents $\tilde J_1^\mu$ and $\tilde J_2^\mu$ in the framework's variables, both material-sector objects, contracted by the photon propagator $1/t$ or $1/u$. The framework's Maxwell field supplies the propagator — its canonical-quantization article constructs the quantized Maxwell field and its two-point function — so the amplitude is the framework's current, twice, joined by the framework's photon. Nothing in this is a new prediction; it is the identification of the components.

### The relative minus sign is the mode algebra's antisymmetry

The single structural feature the framework owns here is the exchange sign. The corpus's canonical-quantization article of the Dirac field obtains **Pauli exclusion as the algebraic identity** $(\hat a_r^\dagger)^2=0$, together with the $\mathbb Z/2$ grading of the mode algebra by fermion parity. That identity is exactly the statement that two fermionic mode operators anticommute, and the relative minus sign between the $t$- and $u$-channel amplitudes is its momentum-space consequence: exchanging two identical external fermions costs a sign. The framework therefore does not merely transcribe the minus sign; the sign is the shadow of the graded structure the corpus establishes on the operator algebra. This is the same $\mathbb Z/2$ grading that the corpus's KMS and fermion-parity articles treat.

### Crossing symmetry is charge conjugation

The Møller and Bhabha amplitudes are related by **crossing symmetry**: moving an incoming electron to an outgoing positron (with reversed four-momentum) changes one process into the other. In the framework this operation is the **charge conjugation** real structure $\mathcal C$ on the doubled module $\Delta = S\oplus\bar S$ of the companion article *The Clifford Structure of the Biquaternion Algebra*; a particle line is replaced by an antiparticle line, and the amplitude's analytic continuation in the Mandelstam variables is the momentum-space face of the same relabelling. The crossing check reported in this article's context file — the Bhabha function minus the Møller function cancelling to numerical accuracy, and the angular identity between the two — is therefore a check of the framework's particle–antiparticle relabelling as much as of the algebra of gamma matrices. The companion Bhabha article states the correspondence from the other side.

### What the framework supplies and what it does not

The framework supplies the two vertex currents, the photon propagator, the Fock space in which the external states live, and the exchange sign as the antisymmetry of its mode algebra. It does **not** supply the numerical evaluation of the traces as a derivation from its own structure — the trace algebra is the Dirac-matrix dictionary of the parent article — nor does it supply the $Z$-exchange diagrams, which belong to the framework's electroweak research agenda rather than to its established content. The parity-violating asymmetry above is quoted as the experimental fact that motivates the left-handed coupling; the corpus's chiral-fermion article discusses the framework's treatment of handedness, and the electroweak article collects the open questions. No framework-specific prediction is claimed.

## Open Questions

1. **The traces as algebra.** Can the four Clifford traces of the spin sum be written directly as biquaternion contractions, without passing through gamma matrices — and does the $\mathbb M_-$ restriction of the currents reproduce the standard results identically?

2. **The exchange sign from first principles.** The corpus obtains Pauli exclusion on the mode algebra. Is there a corresponding statement on the **classical** biquaternion field (a graded-commutativity of the field's components) from which the momentum-space minus sign follows without quantizing?

3. **Crossing and $\mathcal C$.** Is the Mandelstam analytic continuation of the framework's amplitude literally the action of $\mathcal C$ on the external states, or only the same relabelling at the level of the on-shell spinors?

4. **The weak asymmetry.** The corpus's electroweak agenda lists the framework's internal $SU(2)\times U(1)$ questions; the Møller $A_{\mathrm{PV}}$ is a concrete target. Does the framework's left-handed coupling reproduce the $(1/4-\sin^2\theta_{\mathrm W})$ coefficient, or only the general form?

5. **Loops.** The corpus's Ward–Takahashi and Schwinger–Dyson articles treat the identities a loop computation must satisfy, but no loop amplitude is evaluated. Whether Møller scattering at one loop can be organised in the framework without new structure is open.

6. **Empirical contact.** The tree-level result is standard electrodynamics in the framework's variables; the parity-violating asymmetry is the one place the framework meets a measured number, and it is not a framework-specific prediction.

## Summary

Møller scattering, $e^-e^-\to e^-e^-$, is the tree-level exchange of a photon between two electrons, contributing through $t$-channel and $u$-channel diagrams that combine with the relative minus sign of identical-fermion exchange. The Mandelstam variables satisfy $s+t+u=4m^2$; the spin-summed matrix element is three terms, two of them products of traces over the photon propagators and one the interference; the unpolarized cross section reduces to the Rutherford-like $(1+3\cos^2\theta)/\sin^4\theta$ law at low energy and to $(3+\cos^2\theta)^2/\sin^4\theta$ at high energy. The electroweak $Z$-exchange adds a parity-violating asymmetry of a few hundred parts per billion, measured at SLAC and used to extract the weak mixing angle.

In the biquaternion framework the amplitude is the contraction of two material-sector currents — the same current the minimal-coupling article identifies — by the framework's quantized photon propagator. The two structures the framework genuinely owns are the exchange sign, which is the antisymmetry of the mode algebra established by the canonical-quantization article as $(\hat a^\dagger)^2=0$ and the $\mathbb Z/2$ grading, and crossing symmetry, which is the charge-conjugation real structure $\mathcal C$ on the doubled module. The framework does not evaluate loops, does not supply $Z$ exchange, and makes no framework-specific prediction; the parity-violating asymmetry is quoted as the experimental target that the framework's left-handed coupling must ultimately meet.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $e^-e^-\to e^-e^-$ | Møller scattering |
| $p_1,p_2,p_3,p_4$ | Incoming and outgoing electron four-momenta |
| $s,t,u$ | Mandelstam variables; $s+t+u=4m^2$ |
| $E_{\mathrm{CM}}=2E$ | Centre-of-momentum energy |
| $\mathcal M_t,\mathcal M_u$ | $t$- and $u$-channel amplitudes |
| $\mathcal M = \mathcal M_t-\mathcal M_u$ | Total amplitude with the exchange sign |
| $\overline{|\mathcal M|^2}$ | Spin-averaged squared matrix element |
| $\alpha = e^2/4\pi$ | Fine-structure constant |
| $A_{\mathrm{PV}}$ | Parity-violating asymmetry; $\theta_{\mathrm W}$ the weak mixing angle |
| $G_{\mathrm F}$ | Fermi constant |
| $\tilde J\in\mathbb M_-$ | Framework's conserved material-sector current |
| $\mathcal C$ | Charge-conjugation real structure on $\Delta=S\oplus\bar S$ |

## Further Reading

- C. Møller, "Zur Theorie des Durchgangs schneller Elektronen durch Materie," *Annalen der Physik* **406** (1932) 531–585, for the original derivation.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the trace technology and the electron–electron cross section.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the tree-level amplitude, the Mandelstam variables and the cross section.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the trace identities and the identical-fermion exchange sign.
- P. L. Anthony *et al.*, "Precision measurement of the weak mixing angle in Møller scattering," *Physical Review Letters* **95** (2005) 081601, for the SLAC E158 measurement of the parity-violating asymmetry.
- Ya. B. Zel'dovich, "Electron and positron scattering and the weak interaction" (1959), for the first discussion of the parity-violating asymmetry in Møller scattering.
- The companion articles of this series: *Bhabha Scattering in Biquaternionic Form*, *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism*, *Canonical Quantization of the Biquaternion Dirac Field*, *The Feynman Propagator in Biquaternionic Form*, *Canonical Quantization of the Biquaternion Maxwell Field*, *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*, and *Chiral Fermions in the Biquaternion Framework*.
