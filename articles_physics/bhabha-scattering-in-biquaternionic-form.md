# __Bhabha Scattering in Biquaternionic Form__

## Introduction

**Bhabha scattering** is electron–positron scattering, $e^+e^-\to e^+e^-$, in quantum electrodynamics. Homi Bhabha derived it in 1936 in a paper on the scattering of positrons by electrons with exchange, on Dirac's theory of the positron. At the tree level it receives two contributions with a **relative sign difference**: the **$t$-channel scattering** diagram, in which the electron and positron exchange a photon, and the **$s$-channel annihilation** diagram, in which the pair annihilates into a photon that recreates the pair. The two interference terms carry the opposite sign. By **crossing symmetry**, the Bhabha amplitude is the Møller amplitude $e^-e^-\to e^-e^-$ with one particle line crossed from the initial to the final state, and the two describe the same analytic object.

Bhabha scattering is the workhorse of electron–positron colliders: because its small-angle cross section is large, exactly calculable and dominated by the $1/t^2$ photon propagator, it is used as the **luminosity monitor** of the machine. This is the counterpart of the companion article *Møller Scattering in Biquaternionic Form*, and the biquaternion reading is largely shared: the amplitude is a product of material-sector currents joined by the framework's photon propagator, and the two structural features the framework owns are the **exchange sign** — here appearing as the relative sign between exchange and annihilation — and **crossing symmetry**, which is the framework's charge conjugation $\mathcal C$ on the doubled spinor module.

The article is organised as follows. The next section sets up the kinematics and the two amplitudes with their relative sign. The third gives the cross section and its small-angle behaviour. The fourth states the crossing relation to Møller, with the verification recorded in the context file. The fifth is the biquaternion reading, including the annihilation channel's relation to the framework's charge conjugation and to bound-state physics. The closing sections are the open questions, the summary, the notation table and the literature.

## The Process and Its Two Amplitudes

### Kinematics

Let $k$ and $k'$ be the four-momenta of the incoming and outgoing **positron**, and $p$ and $p'$ those of the incoming and outgoing **electron**, so that the process is $e^+(k)\,e^-(p)\to e^+(k')\,e^-(p')$. The Mandelstam variables are

$$
s = (k+p)^2 = (k'+p')^2,
\qquad
t = (k-k')^2 = (p-p')^2,
\qquad
u = (k-p')^2 = (p-k')^2 ,
$$

with the high-energy approximations

$$
s = (k+p)^2 \approx 2k\cdot p \approx 2k'\cdot p',
\quad
t = (k-k')^2 \approx -2k\cdot k' \approx -2p\cdot p',
\quad
u = (k-p')^2 \approx -2k\cdot p' \approx -2k'\cdot p .
$$

Here $s$ is the annihilation-channel invariant, $t$ the momentum-transfer invariant, and $u$ the crossed invariant; the variable names are the same as in Møller scattering, but the particle assignments differ.

### The two amplitudes

The two tree-level diagrams contribute

$$
\mathcal M = -e^2\left(\bar v_k\gamma^\mu v_{k'}\right)\frac{1}{(k-k')^2}\left(\bar u_{p'}\gamma_\mu u_p\right)
\;+\; e^2\left(\bar v_k\gamma^\nu u_p\right)\frac{1}{(k+p)^2}\left(\bar u_{p'}\gamma_\nu v_{k'}\right),
$$

the first (scattering) with coefficient $-e^2$ and denominator $t = (k-k')^2$, and the second (annihilation) with coefficient $+e^2$ and denominator $s = (k+p)^2$. The two spinor contractions have different structures: the scattering term pairs a positron current with an electron current through a spacelike photon, while the annihilation term pairs the electron–positron pair into a single current through a timelike photon. **The relative sign between the two diagrams is negative**, exactly as in Møller scattering, and for the same reason: it is the sign of the exchange of identical fermions between the two diagrams.

## The Cross Section

Squaring the amplitude, averaging over the incoming spins and summing over the outgoing ones gives, at leading order and neglecting the electron mass, the spin-averaged differential cross section

$$
\frac{d\sigma}{d(\cos\theta)} = \frac{\pi\alpha^2}{s}\left[\,u^2\left(\frac1s+\frac1t\right)^2 + \left(\frac{t}{s}\right)^2 + \left(\frac{s}{t}\right)^2\,\right],
$$

where $\theta$ is the scattering angle and $s,t,u$ are as above. The formula is valid at collision energies well below the $Z$ mass scale, around $91\ \mathrm{GeV}$, where photon exchange dominates; above that energy the $Z$-boson contribution must be added, as in the electroweak treatment of the Møller companion.

The structure of the three terms is the same as in Møller scattering, term for term: a $t$-channel square, an $s$-channel square, and the interference, which is here written inside the bracket $u^2(1/s+1/t)^2$ with the cross term carrying its sign. Because $t\to0$ at small angles and the term proportional to $1/t^2$ dominates, the small-angle cross section is

$$
\frac{d\sigma}{d(\cos\theta)} \;\sim\; \frac{\pi\alpha^2}{s}\cdot\frac{u^2}{t^2},
$$

large, positive and calculable in perturbation theory to high precision. This domination by the photon propagator at small angles is why Bhabha scattering is the standard **luminosity monitor**: the rate of small-angle $e^+e^-$ events measures the machine's luminosity, given the known cross section.

## Crossing Symmetry with Møller Scattering

**Crossing symmetry** relates the two processes. Moving the incoming electron of Møller scattering to an outgoing positron — reversing the sign of its four-momentum and its charge — turns $e^-e^-\to e^-e^-$ into $e^+e^-\to e^+e^-$; the $u$-channel of one becomes the $s$-channel of the other, and the $t$-channel is common. Consequently the Møller and Bhabha spin-averaged squared amplitudes are the **same analytic function** of $s,t,u$, evaluated in the physical regions of the two processes.

The check recorded in this article's context file verifies the statement numerically in the framework's Mandelstam variables: the Bhabha cross-section function minus the Møller cross-section function cancels to numerical accuracy once the Mandelstam roles are permuted, and the angular identity between the two functions holds at the sampled angles. The two processes are therefore not merely analogous; they are one amplitude read twice. The companion Møller article states the correspondence from the other side, and the fourth section below identifies it with the framework's charge conjugation.

## The Biquaternion Reading

### The amplitude as two material-sector currents

As in the Møller case, the two spinor bilinears are the framework's conserved **material-sector currents** $\tilde J\in\mathbb M_-$ of the minimal-coupling article, and the propagators $1/s$ and $1/t$ come from the framework's quantized Maxwell field. The scattering term contracts two currents through a spacelike photon; the annihilation term contracts a single pair–current through a timelike photon. The full amplitude is again the framework's current, with the framework's photon, in the two possible channels.

### The relative sign is the graded mode algebra

The relative minus sign between the exchange and annihilation diagrams follows, as in Møller scattering, from the antisymmetry of fermion exchange: the two diagrams are related by the exchange of two identical external fermions and so differ by a sign. The framework's canonical-quantization article obtains this antisymmetry as the algebraic identity $(\hat a_r^\dagger)^2=0$ and the $\mathbb Z/2$ grading of the mode algebra by fermion parity. The Bhabha minus sign is therefore the same algebraic fact as the Møller one, seen in a different channel.

### The annihilation channel and charge conjugation

The **annihilation channel** is the framework's charge conjugation made visible. In the $s$-channel the electron and positron form a single timelike current, i.e. a state in which a particle and an antiparticle are paired; and the operation that replaces a particle line by an antiparticle line is exactly the real structure $\mathcal C$ on the doubled module $\Delta = S\oplus\bar S$ of the companion article *The Clifford Structure of the Biquaternion Algebra*. Crossing symmetry between Møller and Bhabha — replacing an incoming electron by an outgoing positron — is the momentum-space action of the same $\mathcal C$. This is the cleanest framework-level statement the article has: **the Bhabha annihilation diagram and the Bhabha–Møller crossing relation are two faces of the framework's charge conjugation.**

The $s$-channel also connects the free scattering problem to **bound states**. The same timelike annihilation current that mediates Bhabha scattering resonates in the bound electron–positron system; in quantum electrodynamics this is the positronium spectrum, whose non-relativistic structure is the framework's hydrogen-atom series read with the positron mass, and whose relativistic corrections are the Breit–Pauli terms of the companion two-body article. The corpus does not yet contain a dedicated positronium article, so this correspondence is named and not developed.

### What the framework supplies and what it does not

The framework supplies the two vertex currents, the photon propagator, the external Fock states, the exchange sign as the antisymmetry of its mode algebra, and charge conjugation as the real structure $\mathcal C$ that relates the exchange and annihilation channels. It does **not** supply the numerical evaluation of the traces from its own structure, the $Z$-exchange contribution, or the positronium spectrum. As always, the tree-level result is standard electrodynamics expressed in the framework's variables, and no framework-specific prediction is claimed.

## Open Questions

1. **$\mathcal C$ and crossing, precisely.** Is the crossing relation between the Møller and Bhabha amplitudes the literal action of the framework's $\mathcal C$ on the external states, or only the same relabelling of on-shell spinors? The Møller companion asks the same question; a common answer would settle both.

2. **The annihilation current as one object.** In the $s$-channel the particle and antiparticle form a single current on $\Delta=S\oplus\bar S$. Can that current be written as one biquaternion object, or does the framework necessarily use the doubled module?

3. **Resonance and bound states.** The $s$-channel current has bound-state resonances. Does the framework's machinery produce the positronium spectrum, and does its non-relativistic limit agree with the hydrogen-atom series with the reduced mass $m_e/2$?

4. **Luminosity and precision.** The Bhabha small-angle cross section is known to high order in $\alpha$; can the framework organize the higher-order terms through the Ward–Takahashi and Schwinger–Dyson identities of the corpus, or does it stop at tree level?

5. **Weak corrections.** As in Møller scattering, $Z$ exchange and the parity-violating asymmetry belong to the framework's electroweak agenda; Bhabha scattering at and above the $Z$ pole is an asymmetry-sensitive target.

6. **Empirical contact.** The article carries the standard cross section and no framework-specific prediction; the standing disclaimer applies.

## Summary

Bhabha scattering, $e^+e^-\to e^+e^-$, is the tree-level electron–positron process with two diagrams, $t$-channel scattering and $s$-channel annihilation, contributing with a relative negative sign. Its spin-averaged cross section is $(\pi\alpha^2/s)[u^2(1/s+1/t)^2+(t/s)^2+(s/t)^2]$ below the $Z$ scale; it is dominated by $1/t^2$ at small angles and is used as the luminosity monitor of electron–positron colliders. By crossing symmetry it is the same amplitude as Møller scattering in the permuted Mandelstam variables, as the context file's numerical check confirms.

In the biquaternion framework the amplitude is the contraction of material-sector currents by the quantized photon propagator, in the exchange and annihilation channels. The two structures the framework owns are the **relative sign**, which is the antisymmetry of the mode algebra established by the canonical-quantization article, and **charge conjugation**, the real structure $\mathcal C$ on the doubled module that relates the annihilation channel to the exchange channel and the Bhabha process to the Møller process. The $s$-channel annihilation current is the doorway to positronium, which the corpus does not yet treat. The framework supplies the components and the symmetries; the trace evaluation, the $Z$ exchange and the bound-state spectrum remain outside its established content, and no framework-specific prediction is claimed.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $e^+e^-\to e^+e^-$ | Bhabha scattering |
| $k,k'$ | Incoming, outgoing positron four-momenta |
| $p,p'$ | Incoming, outgoing electron four-momenta |
| $s,t,u$ | Mandelstam variables; $s$ annihilation, $t$ transfer, $u$ crossed |
| $t$-channel | Scattering diagram, coefficient $-e^2$ |
| $s$-channel | Annihilation diagram, coefficient $+e^2$ |
| $\theta$ | Scattering angle |
| $d\sigma/d(\cos\theta)$ | Leading-order spin-averaged cross section |
| $\alpha$ | Fine-structure constant |
| $\tilde J\in\mathbb M_-$ | Framework's material-sector current |
| $\mathcal C$ | Charge-conjugation real structure on $\Delta=S\oplus\bar S$ |

## Further Reading

- H. J. Bhabha, "The scattering of positrons by electrons with exchange on Dirac's theory of the positron," *Proceedings of the Royal Society A* **154** (1936) 195–206, for the original derivation.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the spinor algebra of electron–positron scattering.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the cross section, crossing symmetry and the annihilation channel.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the trace identities and the relative sign of the exchange and annihilation diagrams.
- The companion articles of this series: *Møller Scattering in Biquaternionic Form*, *The Relativistic Two-Body Problem in Biquaternionic Form*, *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism*, *Canonical Quantization of the Biquaternion Dirac Field*, *Canonical Quantization of the Biquaternion Maxwell Field*, *The Feynman Propagator in Biquaternionic Form*, and *The Clifford Structure of the Biquaternion Algebra*.
