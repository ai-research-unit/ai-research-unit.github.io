# __The Dirac Sea, Hole Theory and Antimatter in Biquaternionic Form__

## Introduction

In 1928 Dirac found that his equation has solutions of negative energy as well as positive. The free equation has two branches, and nothing in the classical theory forbids an electron from descending the negative branch without limit, so a stable ground state seemed to be impossible. Dirac's answer, in 1930, was the **hole theory**: the negative-energy states are all occupied by an unobservable **sea** of electrons, and the **holes** left in this sea are the antiparticles — the positrons. The idea predicted antimatter, and it shaped the physics of the vacuum for a decade. It was superseded after 1934, when it was understood that the same results follow from the second-quantized theory without any filled sea, by reinterpreting the negative-frequency modes as positive-energy antiparticles. The modern vacuum is the empty state of a Fock space, and the sea survives as a heuristic and as a real object in condensed matter.

This article is the historical and conceptual companion to the framework's technical treatment of the negative-frequency branch, which is *Canonical Quantization of the Biquaternion Dirac Field*. That article already contains the exact statement of the modern resolution in the framework's variables: it expands the field in positive- and negative-frequency modes, notes that *if the modes commuted the energy would be unbounded below*, and finds that the **anticommutator** renders the negative-frequency modes as positive-energy antiparticles. The present article says where that statement came from, why Dirac's original version had to be abandoned, and what the framework can and cannot say about the sea.

Two readings of the negative branch are therefore distinguished throughout.

- The **hole reading**, in which the vacuum is a filled sea and a hole is the absence of a negative-energy background electron. It is the historical reading.
- The **reinterpretation**, in which the vacuum is empty and the negative-frequency modes are the creation operators of antiparticles. It is the modern reading, and it is the one the framework's canonical quantization already uses.

The article's conclusion is that the biquaternion framework is naturally on the reinterpretation side. Its one-particle structure has the two branches and the charge-conjugation real structure that relabels them, but it has no sea; the sea appears only in the second-quantized extension, where it is removed by normal ordering like any other vacuum constant. The framework's added question — whether its algebra gives the vacuum constant a distinguished meaning — is open and is stated as such.

The article is organised as follows. The next section states the negative-energy problem and the pressure from Klein's paradox. The third gives Dirac's hole theory and the prediction of the positron. The fourth lists the objections that killed the filled sea as a fundamental picture. The fifth gives the modern reinterpretation and the second-quantized vacuum. The sixth treats vacuum polarization, where the sea's response became measurable. The seventh treats the Dirac sea in condensed matter, where a filled sea is a physical object. The eighth is the biquaternion reading. The closing sections are the open questions, the summary, the notation table and the literature.

## The Negative-Energy Problem

Dirac's equation is linear in the time derivative, so its solutions come in two branches. For a plane wave of four-momentum $p$ the equation admits both $p^0 = +\sqrt{\mathbf p^2+m^2}$ and $p^0 = -\sqrt{\mathbf p^2+m^2}$, and the second branch has no lower bound: the energy of a solution on the negative branch can be arbitrarily negative. A charged particle would radiate without limit as it fell, so the classical one-particle theory has no stable ground state. The difficulty is not an artefact of the free theory; it survives coupling to the electromagnetic field.

**Klein's paradox** sharpened the trouble. For a potential step strong enough that $V > E + mc^2$, the transmitted wave in the usual one-particle calculation has a negative group velocity and the reflected current exceeds the incident current. The companion article *The Klein Paradox in Biquaternionic Form* treats the calculation in the framework's variables. Its physical significance here is that a strong potential does not simply confine a Dirac electron: it pulls it onto the negative branch. The one-particle theory therefore cannot describe a step of arbitrary strength, and the missing ingredient is the antiparticle.

## Dirac's Hole Theory

### The filled sea

Dirac's 1930 proposal was to occupy every negative-energy state. Because the electron obeys the Pauli exclusion principle, the filled sea is inert: no positive-energy electron can fall in, because the states are taken, and the sea contributes no observable current. A **hole** — an unoccupied negative-energy state — is observable. Its properties follow by subtraction:

- removing a state of negative charge $-e$ and negative energy leaves a positive charge $+e$ and positive energy;
- removing a state of spin up leaves an object of spin down, and vice versa.

The hole is therefore a positive-energy, positively charged particle of the same mass as the electron: the **positron**.

### The prediction and the discovery

Dirac first identified the hole with the proton, in a 1930 paper on electrons and protons, but the mass was wrong and the identification was criticised by Weyl and by Oppenheimer. In 1931 Dirac predicted a new particle of electron mass and positive charge, and in 1932 Anderson observed it in cosmic-ray cloud-chamber tracks: the positron. The hole theory thus predicted antimatter before antimatter was seen, and for several years the filled sea was the working picture of the vacuum.

## The Problems with Hole Theory

Four objections made the filled sea untenable as a fundamental description.

- **Infinite charge and energy.** A completely filled sea of negative-energy states has infinite total charge and infinite (negative) energy. Only differences from the sea are observable, so the infinities must be subtracted, but the subtraction is a prescription, not a derivation. In the operator language this prescription becomes **normal ordering**, the removal of the vacuum expectation value of the energy and charge; the framework's canonical-quantization article performs exactly this subtraction and records the constant $E_0=-2V\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}$.
- **It is a fermion-only device.** The exclusion principle is what keeps the sea inert. A boson obeys no exclusion, so a filled bosonic sea would be no obstacle to further occupation, and the negative-frequency problem of the Klein–Gordon equation must be resolved another way — by the second-quantized treatment of the two branches with a different statistics. Hole theory therefore cannot be the general theory of the vacuum.
- **The sea is an infinite many-body state, not a one-particle statement.** Its consistency requires an infinite number of particles and a notion of the vacuum as a state of an operator algebra, which the one-particle equation does not supply.
- **It is not needed.** Once the fields are quantized, the same predictions follow from the anticommutation relations alone, without populating anything.

The last point is the decisive one: the hole theory is a correct but redundant bookkeeping of the second-quantized theory, not an extra physical ingredient.

## The Modern Reinterpretation

### The reinterpretation

The reinterpretation of the negative branch is usually credited to Furry and Oppenheimer (1934), who showed that positron processes follow from the second-quantized electron field without a sea, and to Stückelberg (1941) and Feynman (1948), who made the picture systematic: a negative-frequency solution propagating forward in time is the same as a positive-frequency antiparticle propagating backward in time. The field operator is expanded as

$$
\hat\psi(x) = \sum_r\int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\left[\hat a_r(\mathbf p)\,u^{(r)}(\mathbf p)e^{-ip\cdot x} + \hat b_r^\dagger(\mathbf p)\,v^{(r)}(\mathbf p)e^{+ip\cdot x}\right],
$$

in which the **annihilation** operator multiplies the positive-frequency spinors and the **creation** operator of antiparticles multiplies the negative-frequency spinors. There is no sea; the vacuum $|0\rangle$ is defined by $\hat a|0\rangle = \hat b|0\rangle = 0$. The framework's canonical-quantization article writes precisely this expansion on the spinor module, with each mode function the module representative of a biquaternion plane wave.

### Normal ordering

With the anticommutator the Hamiltonian becomes, after normal ordering,

$$
\hat H = \sum_r\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}\left(\hat a_r^\dagger\hat a_r + \hat b_r^\dagger\hat b_r\right),
$$

a positive sum of particle and antiparticle numbers, with the divergent constant removed. The charge is equally normal-ordered, and particles and antiparticles carry opposite charge. This is the modern replacement of the filled sea, and it is the content the framework already has.

## Vacuum Polarization: Where the Sea's Response Became Measurable

Even though the filled sea is not the fundamental picture, the *response of the vacuum* to an external field is real and measurable, and the hole language captures it well: the vacuum behaves as a polarizable medium because virtual electron–positron pairs can be displaced.

The first calculation is **Uehling's** (1935): the vacuum polarization correction to the Coulomb potential of a point charge. **Euler and Heisenberg** (1936) computed the effective Lagrangian of the electromagnetic field obtained by integrating out the fermions, which is nonlinear in the field strengths; **Weisskopf** (1936) and later **Schwinger** (1951) completed the renormalized treatment. The consequences include the running of the electric charge, the Lamb shift, and — in strong fields — birefringence of the vacuum and the possibility of pair creation. In condensed matter the same vacuum polarization is realized as the dielectric response of the filled valence band, which is why the analogy between the Dirac sea and the filled band is not only formal.

## The Dirac Sea in Condensed Matter

In solids the filled sea is a physical object. The electrons of a crystal fill the bands up to the Fermi level; the filled valence band of a semiconductor or insulator is a **Fermi sea**, and an empty state near the top of the valence band — a **hole** — conducts as a positive charge. The arithmetic is the same as in Dirac's hole theory: remove an electron of charge $-e$ and momentum $\mathbf p$ from the filled band, and the remaining excitation has charge $+e$, momentum $-\mathbf p$ and positive energy. The effective mass of the hole is the negative of the electron's band mass, exactly as the hole's energy in the Dirac sea is positive when the electron energy was negative.

The analogy sharpens in the Dirac materials of the companion article *Dirac Matter: Graphene, Dirac Cones and Topological Insulators in Biquaternionic Form*. Graphene's electrons near the Dirac point obey a massless two-dimensional Dirac equation, and the negative-energy branch is the filled lower cone; its hole excitations are the positive-charge carriers. In a Dirac or Weyl semimetal the filled negative-energy branch is again a real Dirac sea, and its low-energy response — including the anomalous quantum Hall effect and Klein tunnelling — is described by the same equations that Dirac wrote for the vacuum. The condensed-matter realization is therefore the place where the sea is not a bookkeeping device but a measured many-body state.

## The Biquaternion Reading

### The two branches are the framework's two mass-shell roots

The framework's mass shell $\tilde k\bar{\tilde k} = -m^2c^2/\hbar^2$ has two roots, and the same two branches appear in every component of the Dirac field. The corpus's companion articles use the two branches explicitly: the Klein article shows that a strong step exchanges them, and the canonical-quantization article expands the field in `positive-frequency' and `negative-frequency' plane waves, with the two branches the two roots of the single biquaternion mass-shell condition. Nothing in this is new to the framework; what matters for the Dirac sea is what the framework does *next*.

### The operator content is already the reinterpretation

The framework's canonical-quantization article contains the modern resolution verbatim. It shows that if the modes commuted, the energy $H=\sum E_{\mathbf p}(\hat a^\dagger\hat a-\hat b^\dagger\hat b)$ would be **unbounded below** and no stable vacuum would exist; that the **anticommutator** replaces this by a positive sum plus a c-number; and that "the anticommutator is what makes the negative-frequency modes into positive-energy antiparticles. This is the operator content of the Dirac sea." The framework is therefore explicitly on the reinterpretation side: the vacuum is the state annihilated by the annihilation operators, and the negative branch is the creation operators of antiparticles. Dirac's filled sea is not implemented, and does not need to be.

### The infinite charge is the normal-ordering constant

The framework's one-particle structure has no sea, and therefore no infinite charge of its own. The infinity appears only when the field is quantized, as the normal-ordering constant

$$
E_0 = -2V\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p},
$$

which the canonical-quantization article removes by the standard prescription and describes as "an ultraviolet feature of the free field." The framework's added question is whether the biquaternion structure singles out a distinguished regularization or assigns $E_0$ a geometric meaning; the article records that "nothing in the biquaternion structure as used here changes that," and the question is open. This is the correct place to fix the article's negative conclusion: **the framework inherits the sea's infinity as the ordinary normal-ordering constant and does not, in the corpus as it stands, explain it.**

### Charge conjugation and the two branches

The relabelling that turns a negative-energy electron into a positive-energy positron is the framework's **charge conjugation**. The companion article on the Clifford structure of the biquaternion algebra places the charge-conjugation real structure $\mathcal C$ on the doubled module $\Delta = S\oplus\bar S$, tying the module $S$ to its conjugate $\bar S$; the same article records that the internal spinor has a charge conjugate but no Majorana partner, and that the doubling from $\mathbb B\cong S\oplus S$ to $\Delta$ is the structure that carries $\mathcal C$. The hole-theory relabelling and the framework's $\mathcal C$ are the same operation read in the two pictures: the sea's holes and the second-quantized antiparticles are the $\mathcal C$-conjugates of the particles. This is the cleanest framework-level content of the article.

### The framework-consistent reading

Putting the pieces together, the framework supports the following reading and no more:

- the two mass-shell branches are the framework's positive- and negative-frequency solutions;
- charge conjugation is the real structure $\mathcal C$ on the doubled module, whose existence is established in the corpus;
- the second-quantized field's creation operators on the negative branch are the operator form of the sea, and the anticommutator makes the theory stable;
- the filled sea itself — an infinite one-particle occupation — has no place in the framework's one-particle algebra, and there is no framework-natural reason to adopt it over the reinterpretation;
- the infinite vacuum charge and energy appear as the normal-ordering constant, which the framework does not explain.

## Open Questions

1. **The vacuum constant.** Does the biquaternion structure single out a regularization of $E_0$, or give it a geometric meaning? The canonical-quantization article says no claim is made; this article records the same and adds that the Dirac sea does not supply an alternative.

2. **The vacuum state's algebra.** The corpus treats the vacuum as a minimal idempotent in *The Biquaternion Vacuum as a Minimal Idempotent* and as the Fock vacuum in the canonical quantization. Are these two objects the same, and does the idempotent reading survive second quantization?

3. **$\mathcal C$ versus hole relabelling.** The framework's $\mathcal C$ is a real structure on the doubled module; the hole relabelling is a map of occupation numbers. Are they literally the same map on the Fock space, or two constructions that agree on one-particle states?

4. **Bosons.** Hole theory fails for bosons. The framework quantizes scalar and vector fields in its Klein–Gordon, Maxwell and Proca articles; does the framework's treatment of the negative-frequency branch of a bosonic field differ structurally from the fermionic case, or only in statistics?

5. **Condensed-matter realization.** In a solid the filled sea is finite and measurable. Can the framework exploit this — for instance, does the finite sea of graphene's lower cone give a framework-natural cutoff for $E_0$? This is a speculative direction and is flagged as such.

6. **Empirical contact.** The sea and the reinterpretation make the same predictions; the article therefore carries no framework-specific prediction, and the standing disclaimer applies.

## Summary

The Dirac equation has negative-energy solutions with no lower bound, and Klein's paradox shows that a strong potential drives a one-particle state onto them. Dirac's 1930 hole theory filled the negative-energy states and identified the holes with positive-energy, positively charged particles, predicting the positron (observed by Anderson in 1932) before it was found. The filled sea is untenable as a fundamental picture: it carries infinite charge and energy, it works only for fermions, it is irreducibly many-body, and it is unnecessary. The modern treatment reinterprets the negative-frequency modes as antiparticle creation operators, defines the vacuum as the empty Fock state, and removes the vacuum constant by normal ordering.

The biquaternion framework is naturally on this second side. Its mass shell has the two branches; its canonical quantization expands the field in positive- and negative-frequency modes, exhibits the unbounded energy that would follow from commuting modes, and finds stability in the anticommutator, which is exactly "the operator content of the Dirac sea." Its charge conjugation is the real structure $\mathcal C$ on the doubled module, which relabels particles as antiparticles as the hole picture does. What the framework does not do is fill a sea — its one-particle algebra has none — and it does not explain the vacuum constant, which appears as the ordinary normal-ordering constant $E_0=-2V\int d^3p\,E_{\mathbf p}/(2\pi)^3$. In condensed matter, by contrast, the Dirac sea is a physical filled band, and in the Dirac materials of the companion article the sea and its holes are measured.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $E=\pm\sqrt{\mathbf p^2+m^2}$ | Two branches of the Dirac dispersion |
| $\hat a_r(\mathbf p)$, $\hat b_r(\mathbf p)$ | Particle and antiparticle annihilation operators |
| $u^{(r)}$, $v^{(r)}$ | Positive- and negative-frequency spinors |
| $|0\rangle$, $\hat a|0\rangle=\hat b|0\rangle=0$ | Fock vacuum; no sea |
| $E_0=-2V\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}$ | Normal-ordering constant (vacuum energy) |
| $e$ | Positive unit of charge; the electron carries $-e$ |
| $\mathcal C$ | Framework's charge-conjugation real structure on $\Delta=S\oplus\bar S$ |
| $\Delta=S\oplus\bar S$ | Doubled spinor module carrying $\mathcal C$ |
| Fermi sea | Filled valence band; the sea's condensed-matter realization |

## Further Reading

- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the equation and the negative-energy solutions.
- P. A. M. Dirac, "A theory of electrons and protons," *Proceedings of the Royal Society A* **126** (1930) 360–365, for the hole theory and the initial, incorrect proton identification.
- P. A. M. Dirac, "Quantised singularities in the electromagnetic field," *Proceedings of the Royal Society A* **133** (1931) 60–72, for the prediction of the positron.
- C. D. Anderson, "The apparent existence of easily deflectable positives," *Science* **76** (1932) 238–239, for the discovery of the positron.
- O. Klein, "Die Reflexion von Elektronen an einem Potentialsprung nach der relativistischen Dynamik von Dirac," *Zeitschrift für Physik* **53** (1929) 157–165, for the paradox that pressures the negative branch.
- W. H. Furry and J. R. Oppenheimer, "On the theory of the positron," *Physical Review* **45** (1934) 245–262, for the field-theoretic treatment without a sea.
- E. C. G. Stückelberg, "Remarque à propos de la création de paires de particules en théorie de relativité," *Helvetica Physica Acta* **14** (1941) 588–594, and R. P. Feynman, "The theory of positrons," *Physical Review* **76** (1949) 749–759, for the systematic reinterpretation.
- E. A. Uehling, "Polarization effects in the positron theory," *Physical Review* **48** (1935) 55–63, and W. Heisenberg and H. Euler, "Folgerungen aus der Diracschen Theorie des Positrons," *Zeitschrift für Physik* **98** (1936) 714–732, for vacuum polarization and the effective Lagrangian.
- J. Schwinger, "On gauge invariance and vacuum polarization," *Physical Review* **82** (1951) 664–679, for the renormalized treatment.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Fields* (McGraw-Hill, 1965), for the second-quantized Dirac field and normal ordering.
- The companion articles of this series: *Canonical Quantization of the Biquaternion Dirac Field*, *The Klein Paradox in Biquaternionic Form*, *The Biquaternion Vacuum as a Minimal Idempotent*, *The Vacuum State and the Casimir Effect in Biquaternionic Form*, *Dirac Matter: Graphene, Dirac Cones and Topological Insulators in Biquaternionic Form*, and *The Clifford Structure of the Biquaternion Algebra*.
