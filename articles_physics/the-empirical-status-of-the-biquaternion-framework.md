# __The Empirical Status of the Biquaternion Framework__

## Introduction

This article asks what would count as an **empirical signature** of the biquaternion framework: a measurement whose outcome the framework predicts to differ from the prediction of standard physics. It is a research agenda, and its subject is the criteria a candidate must meet, not a catalogue of confident predictions.

The standing position of the series is stated here plainly. On every domain the companion articles have developed, the framework **agrees** with standard physics: the single-qubit formalism reproduces the Bloch ball, the Born rule, and the projective update exactly; relativistic mechanics reproduces the interval, the mass shell, and the four-force constraints exactly; Maxwell and Dirac are transcriptions; and the hydrogen spectrum, the Casimir force, the Unruh temperature, and the Bell/CHSH bounds are reproduced and not modified, while the CPT theorem is transcribed rather than established. The framework is a reformulation, and on each domain it reformulates it is currently **empirically equivalent** to what it reformulates. That is the starting point of this article, not a disappointment, and the main result below is that it is also, so far, the end point: no distinguishing prediction is made.

The temptation this article exists to resist is the opposite of that conclusion: to take a structure the framework contains — the two-sector decomposition, the local complex structure, the imaginary directions — call it a prediction, and name the experiment that would test it. The method adopted instead is to take each candidate in turn and ask:

1. Which framework-specific quantity does it depend on?
2. Is that quantity derived anywhere in this series, or merely posited?
3. What existing experimental bound already constrains it?

A candidate that traces to an undetermined parameter or an unverified claim is **not a signature**, and is labelled as such below; so is a candidate whose "prediction" is the standard result rewritten. The next section fixes what a signature would have to be and identifies the structural reason none is yet available; the sections after record the standing agreement, explain why it is not evidence for the framework's distinctive content, and examine the candidates individually.

Throughout, the notation is inherited from the read-list articles: the biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, and scalar imaginary $i$; the material sector is the anti-Hermitian subspace $\mathbb{M}_-$ and the informational sector the Hermitian subspace $\mathbb{M}_+$, with $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$; the norm form is $N(\tilde{Q})=\tilde{Q}\bar{\tilde{Q}}$; the trace formula is $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$.

## What Would Count as a Signature

A measurement $M$ is a **signature** of the framework relative to a standard theory $S$ if the framework predicts for $M$ a value that differs from the value $S$ predicts, by an amount the framework itself fixes, and if the measurement can resolve the difference. Four conditions must hold simultaneously:

**(S1) A framework-specific quantity.** There is a quantity $Q$ that the framework determines and $S$ does not. The two-sector reading, the local complex structure, and the imaginary directions are candidates for such quantities; whether any of them *determines* a number is a separate matter.

**(S2) A fixed value or scale.** The framework fixes the value of $Q$, or at least a scale in terms of which the deviation is expressed. A symbol left free is not a prediction. A dimensionless algebra that imports all its dimensional constants from outside fixes no scale.

**(S3) An observable.** There is a measurable quantity $O$ whose value is $O_S+\delta(Q)$, with $\delta$ computed from the framework. If $O=O_S$ identically, the framework is consistent but indistinguishable on this measurement.

**(S4) Resolution.** An existing or feasible experimental bound on $O-O_S$ is tighter than the predicted $\delta$. A deviation smaller than the best bound is not a test; it is an aspiration.

The four conditions fail together for a structural reason. The framework's established content is the algebra $\mathbb{B}$ with its standard representations: $\mathbb{B}\cong M_2(\mathbb{C})$, a theorem of the corpus and not a modelling choice; $\mathbb{M}_-\cong\mathbb{R}^{3,1}$ with the Minkowski form; and $\mathbb{M}_+$, the Hermitian part of $M_2(\mathbb{C})$, the standard operator space of a two-state system. All are shared with the standard formalism, and the algebra is **dimensionless**: $N$, the product, and the conjugations carry no scale, while $c$, $\hbar$, $m$, and $e$ are inserted from outside.

The consequence is a barrier that this article will meet repeatedly. Any quantity the framework fixes **by its algebra alone** is a quantity that the standard theory, using the same algebra, fixes identically. A signature therefore requires an input that is not algebra — a dynamics, a coupling, a scale, or a selection principle. The series has supplied such inputs in the places where a transcription needed them (the Dirac mass term, the gauge fixing of the Maxwell field, the frame field of the curved-spacetime construction), but in no case has it supplied one whose value the algebra forces. That is the central structural reason the framework currently makes no distinguishing prediction.

Two precisions. First, "empirically equivalent" is asserted **case by case**, for the domains actually developed, not as a theorem about a completed theory: the framework does not reformulate the Standard Model, the dynamics of general relativity, or quantum field theory in general. Second, equivalence is a property of a *transcription* — a faithful reformulation makes the same predictions by construction — so agreement with experiment cannot by itself be evidence for whatever the reformulation adds.

## The Standing Agreement, Domain by Domain

The following table collects the quantitative results the series has obtained and the standard results they reproduce. In every row the deviation is zero.

| Domain | Framework result | Standard result reproduced |
|---|---|---|
| Single qubit | Bloch sphere and Bloch ball; $\mathrm{Tr}(\tilde{\rho}\tilde{H})=h_0+\mathbf{r}\cdot\mathbf{h}$; sandwich update | States, observables, Born rule, projective measurement |
| Relativistic point mechanics | $N(d\tilde{X})=-c^2dt^2+d\mathbf{x}^2$; $\tilde{P}\bar{\tilde{P}}=-m^2c^2$; $\tilde{F}\bar{\tilde{P}}+\tilde{P}\bar{\tilde{F}}=0$ | Interval, mass shell, four-force orthogonality |
| Maxwell field | $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}=\partial_{ict}^2+\Delta$; Riemann–Silberstein field; invariants | Maxwell's equations in a medium |
| Dirac field | $\tilde{\nabla}\tilde{\Psi}_R=m\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L=m\tilde{\Psi}_R$; massless case $\tilde{\nabla}\tilde{\Psi}=0$ | Dirac equation, mass term |
| Electron gyromagnetic ratio | $g=2$ at tree level; anomaly **absent** | Dirac's tree-level value; the anomaly is outside the framework |
| Hydrogen, relativistic | Exact Dirac–Coulomb spectrum; fine structure | Standard spectrum, quoted not derived |
| Casimir effect | $-\pi^2\hbar c/(240a^4)$, attractive | Standard Casimir force, reproduced |
| Unruh effect | $T=\hbar a/(2\pi c\,k_B)$ | Standard Unruh temperature, reproduced |
| CPT, Born rule, Bell/CHSH, decoherence | Standard statements | Standard results, reproduced; CPT transcribed, not established |
| Linearized gravity and gravitational waves | Standard wave equation **assumed**; no deviation predicted | No derivation of the field equation |

Not one entry in the table is a difference. The agreement is exact where the algebra is used exactly (the qubit, the four-vector kinematics), and it is a faithful reproduction where the framework transcribes a standard equation (Maxwell, Dirac, hydrogen, Casimir, Unruh). The gravitational-wave row is the weakest: there the framework does not derive the field equation it uses, so even the agreement is carried by standard general relativity rather than produced by the algebra.

It is worth naming what these results are checks *of*. They are checks that the transcription is faithful — that the biquaternion dictionary has been applied consistently, that signs and factors of two and the trace convention are right. That is a real and nontrivial achievement: a reformulation that got these wrong would be wrong. But a faithful transcription is guaranteed to agree, so the agreement tests the transcription, not the framework's distinctive content.

## Why Agreement Is Not Confirmation

A reformulation and its target are not two theories that happen to agree; they are one theory written twice. When the dictionary is exact, agreement is a consistency condition on the dictionary, and it cannot discriminate between the framework and the standard formalism, because on the shared structure the two are the same.

The framework's distinctive content is not what the reproducing calculations use. They use the isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$; the identification of $\mathbb{M}_-$ with $\mathbb{R}^{3,1}$; and the standard wave operators built from the biquaternionic gradient. All three are shared with the standard formalism. The framework-specific additions — the naming of $\mathbb{M}_-$ as *material* and $\mathbb{M}_+$ as *informational*, the claim that the complex structure is local and physically determined, the proposal that the algebra is nature's rather than notation's — enter no formula that produces a number. They are therefore untested by every experiment the series cites, including the ones that agree. A reader who treats the agreement as support for the material/informational reading has read the evidence backwards.

Two examples show how narrowly the agreement should be read.

**The electron.** The framework forces the tree-level $g=2$, which is Dirac's result; the measured anomalous part $a=(g-2)/2\approx1.1597\times10^{-3}$ is outside the classical equation and is not contained. The framework therefore cannot claim the measured moment at the precision the measurement achieves; its agreement is with tree-level Dirac theory, one part in $10^3$ away from the measured value.

**Hydrogen.** The exact relativistic spectrum is the standard Dirac–Coulomb result, quoted and reproduced; the corpus states that the bound-state solution is not derived anywhere in the series. The framework supplies the spin algebra and the level bookkeeping, but not the radial dynamics or the coupling constant, and the agreement is with an imported result.

The lesson generalizes. When a reformulation reproduces a number, the question to ask is **which of its structures produced the number**. If the answer is the standard ones — the complex algebra, the Minkowski form, an inserted constant — then the number is not evidence for the framework's addition. This is the criterion applied to every candidate below.

## Candidate Signatures

Each candidate below is examined under the three questions of the Introduction and the four conditions of the second section. The order runs from the candidate with no home in the framework to the one that is, in the writer's judgement, the most promising, and it closes with a second warning rather than a candidate.

### A Fundamental Scale, and Modified Dispersion

**The candidate.** High-energy quantum-gravity models typically propose a modification of the dispersion relation — an energy-dependent speed of light, or a minimum length — appearing at a fundamental scale, often the Planck scale.

**The framework-specific quantity.** There is none. The algebra $\mathbb{B}$ and its coefficient field are dimensionless; the norm form, the product, and the conjugations carry no scale. Every dimensional quantity in the series is imported: the corpus records that the electron mass, charge, and $\hbar$ are inserted, and that the framework supplies neither the value of the fine-structure constant nor the magnitude of the Coulomb coupling. No article derives a fundamental length or energy. The companion article on the renormalization group puts the point sharply: the scale, the field content, the gauge group, and the values of the couplings are all inputs, and the algebra fixes none of them.

**Derived or posited.** Neither. This is stronger than "unverified": the candidate has no home in the framework as developed. There is no parameter whose absence could be repaired by more work on the same algebra — a scale must be inserted, and any inserted scale is an addition to the framework rather than a consequence of it.

**The existing bound.** The relevant bounds bound proposals that *do* supply a scale. The Fermi-LAT analysis of GRB 090510 already requires any linear energy dependence of the speed of light to set in above the Planck scale, $E_\mathrm{Pl}\approx1.22\times10^{19}$ GeV; and the gravitational-wave event GW170817 constrains $v_\mathrm{GW}-v_\mathrm{EM}$ to between $-3\times10^{-15}$ and $+7\times10^{-16}$ times $c$. These do not constrain the biquaternion framework, because the framework supplies no scale for them to act on. If a scale were inserted by hand, the bounds are tight enough to exclude most natural choices.

**Verdict.** Not a signature. A dispersion claim here would be the invention the Introduction warns against.

### The Local Complex Structure

**The candidate.** The framework's most distinctive physical claim after the two-sector reading is that the complex structure of $\mathbb{B}$ is **local**, its scale set by the local speed of light $c=1/\sqrt{\epsilon\mu}$. One might hope that an observable depends on the complex structure as such, and not merely on the standard electromagnetic properties of the medium.

**The framework-specific quantity.** The local speed $c(\mathbf{x})=1/\sqrt{\epsilon(\mathbf{x})\mu(\mathbf{x})}$, which fixes the embedding of physical time in the imaginary scalar direction, $\partial_{ict}=-(i/c)\,\partial_t$.

**Derived or posited.** The relation $c=1/\sqrt{\epsilon\mu}$ is **standard**, a consequence of the constitutive relations $\mathbf{D}=\epsilon\mathbf{E}$ and $\mathbf{B}=\mu\mathbf{H}$; the framework does not derive it. What is posited is the *identification* of this standard speed with the scale of the complex structure. Crucially, the framework adds no equation for $\epsilon$ or $\mu$: in every calculation of the series they are the standard medium parameters, supplied from outside.

**The existing bound.** None specific to the framework. Bounds on $\epsilon(\omega)$ and $\mu(\omega)$ are bounds on the standard medium response, which the framework takes as input; they do not test the complex-structure reading, because that reading makes no claim about their values.

**Verdict.** Not a signature. The *locality* of the complex structure is inherited entirely from the standard locality of $c(\mathbf{x})$, so any observable sensitive to it is already an observable of standard medium electromagnetism.

### A Second Light Cone, or Vacuum Birefringence

**The candidate.** The framework has two sectors, and the two sectors carry quadratic forms of opposite signature. Perhaps there are two null structures, hence a polarization-dependent propagation speed — birefringence — or a second, "informational" light cone.

**The framework-specific quantity.** The norm form $N(\tilde{Q})=\tilde{Q}\bar{\tilde{Q}}$. It is a **single** quadratic form on $\mathbb{B}$, and its zero set is a single cone. Its restrictions to $\mathbb{M}_-$ and $\mathbb{M}_+$ are the mirror quadratic forms $-q_0^2+\mathbf{q}^2$ and $q_0^2-\mathbf{q}^2$; these are restrictions of the same form to complementary subspaces, not two independent propagation structures. A field propagating in the framework obeys one d'Alembertian $\Box=\partial_{ict}^2+\Delta$, built from one $c$. There is no second cone and no splitting of polarizations.

**Derived or posited.** The single cone is **derived**: it is the zero-divisor set of the algebra, a theorem of the corpus. The absence of birefringence is therefore a consequence of the algebra, not an unverified claim.

**The existing bound.** Had the framework predicted birefringence, astrophysical polarimetry and gravitational-wave timing would constrain it. Since it predicts none, there is nothing to bound — and, once again, its consistency with the null-cone tests is not evidence for the framework, because the null cone it uses is the standard one.

**Verdict.** Not a signature. The algebra here forecloses the candidate rather than realizing it.

### The Imaginary Directions as Extra Space

**The candidate.** The framework complexifies spacetime, so each point carries four real and four imaginary coordinates. A reader might expect the imaginary directions to be observable extra dimensions, with Kaluza–Klein-like consequences.

**The framework-specific quantity.** None. The companion article on $\mathbb{M}_+$ states explicitly that the imaginary directions are **not** claimed to be extra space; the informational sector reinterprets the same four-dimensional arena, and no field is taken to propagate in the imaginary directions. No compactification radius is defined.

**Derived or posited.** The complexification is a property of the algebra; the *observability* of the extra directions is not claimed at all, not even as a hypothesis.

**The existing bound.** If the imaginary directions were compactified at a radius $R$, collider and short-range-gravity tests would bound $R$; with no radius defined, there is nothing to bound.

**Verdict.** Not a signature. This candidate is often imputed to complexified-spacetime proposals from the outside, and the corpus is explicit in disclaiming it.

### A New Material–Informational Coupling

**The candidate.** The framework's central interpretive claim is that $\mathbb{M}_+$ is a physical sector. A coupling between the sectors beyond the standard Lorentz action would be new physics: a fifth force, a new field, a mass mixing.

**The framework-specific quantity.** Unspecified. The only operations involving both sectors are multiplication by $i$, which exchanges them, and the rotor conjugation $\tilde{X}\mapsto\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$, the standard Lorentz action. The companion article on $\mathbb{M}_+$ states that no dynamics for $\mathbb{M}_+$-valued fields is specified and that there is no coupling beyond the Lorentz one; the introduction lists a coupling between the sectors as an open question.

**Derived or posited.** Posited as a question. There is no field equation, no action, and no coupling constant.

**The existing bound.** If a specific coupling were written down — a Yukawa interaction of range $\lambda$ and strength $\alpha$, say — then torsion-balance, equivalence-principle, and atom-interferometry bounds would apply to it. With no parameter, nothing is constrained. And a coupling that is inserted rather than derived would make any resulting signature a test of the insertion, not of the framework.

**Verdict.** Not a signature, but the framework's largest gap and its best hope. This is the item on the agenda whose completion would most plausibly produce a genuine signature.

### Deviations in Quantum Statistics

**The candidate.** *Quaternionic* quantum mechanics is a real alternative to the complex theory with distinctive predictions — most notably a modification of two-particle interference. A reader meeting the word "biquaternion" might expect the framework to inherit them.

**The framework-specific quantity.** None, and this is a structural no-go rather than a gap. $\mathbb{B}$ is an **associative** algebra and is isomorphic to $M_2(\mathbb{C})$; it is a complex algebra, not a quaternionic Hilbert space. Its two-state sector is exactly the standard complex two-state theory. The framework therefore sits on the same side as standard quantum mechanics in every interference test, and it does not inherit the quaternionic programme's deviations.

**Derived or posited.** The exact complex structure is derived. The deviations are absent by algebra, not merely unverified.

**The existing bound.** Precision interference and two-particle tests are consistent with complex quantum mechanics; the framework shares that agreement exactly. There is no framework-specific number to compare.

**Verdict.** Not a signature, and a warning. This is the candidate on which a careless writer is most likely to claim a signature — or, worse, to claim the quaternionic predictions under a biquaternionic name. The framework is not a quaternionic Hilbert-space theory, and the predictions of that programme are not available to it.

### Derived Dimensionless Relations

**The candidate.** The class of signatures that does not require a new scale: a relation among **standard** parameters — a ratio, a mixing angle, a sum rule — that the algebra forces and the standard theory leaves free. This is the one form a scale-free algebra can take.

**The framework-specific quantity.** None exists in the corpus. No article derives a value for a coupling, a mass ratio, or a mixing angle. The series says so where it matters: the hydrogen article records that the framework does not supply the dimensionless coupling; the electron article records that the mass and charge are inserted; the chiral-fermion article records that the abelian sector is vector-like and offers no charge assignment.

**Derived or posited.** Nothing is derived; this is the empty cell of the framework.

**The existing bound.** Whichever relation were proposed, the standard constants are known to many digits, so a derived relation would be immediately and sharply testable. The absence here is a limit of the framework's derivation, not of experimental precision.

**Verdict.** The most promising candidate class, and currently empty. What would settle it is stated in the next section.

### Unverified Framework Claims: the Entropy Functional

**The candidate.** The corpus floats a small number of framework-specific proposals that are not yet verified. The clearest is an entropy functional on the states of $\mathbb{M}_+$, written $S(\tilde{\rho})=-2\,\mathrm{Sc}(\tilde{\rho}\log\tilde{\rho})$ and recorded in the companion article as *needing verification*.

**The framework-specific quantity.** The functional $S(\tilde{\rho})$, if it were well defined.

**Derived or posited.** Posited, and not yet verified: the biquaternion logarithm is multivalued, and no article shows that the expression is real, concave, or additive on the states of $\mathbb{M}_+$. Even if all of that were established, it is a transcription of the standard von Neumann entropy $S(\rho)=-\mathrm{Tr}(\rho\log\rho)$ and would agree with the standard theory rather than deviate from it.

**The existing bound.** None applies, because a transcribed entropy functional makes no new prediction.

**Verdict.** Not a signature, and a second warning: an item whose "signature" traces to an unverified claim is not a signature until the claim is verified, and here verification would still leave the standard result in place.

### Reproductions That Are Not Signatures

Several results are sometimes presented as if they were successes of the framework, and they are worth separating from signatures explicitly, because each is a reproduction of a standard result.

- **The tree-level gyromagnetic ratio $g=2$.** This is Dirac's tree-level value; the anomaly is outside the framework. The framework can claim agreement with tree-level Dirac theory, not with the measured moment.
- **The relativistic hydrogen spectrum.** It is the standard Dirac–Coulomb spectrum, quoted and reproduced; the exact bound-state solution is not derived in the series.
- **The Casimir force $-\pi^2\hbar c/(240a^4)$.** Reproduced, not modified; the corpus states that the framework supplies no modification.
- **The Unruh temperature $T=\hbar a/(2\pi c\,k_B)$.** Reproduced by a reformulation; the corpus states that it yields no discriminating prediction.
- **The Born rule, the CPT theorem, and the Bell/CHSH bounds.** Standard statements; the Born rule and the Bell/CHSH bounds are reproduced, and the CPT theorem is transcribed rather than established.

Each of these is a check that a transcription is faithful. None is evidence for the material/informational reading, because none of those computations uses it.

## What Would Settle It

The question would be settled affirmatively by a single candidate meeting all four conditions of the second section. The discussion above shows what such a candidate would look like and where the framework would have to acquire it.

**The barrier restated.** To break empirical equivalence the framework must deploy a structure not already contained in the pair $(M_2(\mathbb{C}),\ \text{Minkowski space})$. Three routes are available, and the series has touched all three without deriving any of them:

1. **A scale.** A fundamental length or energy, whether by deforming the algebra (a quantum group, a non-commutative spacetime) or by adding a dimensionful parameter. This would make the modified-dispersion candidate real, but the bound it must beat is severe: a linear dispersion scale must already lie above the Planck scale, and $v_\mathrm{GW}-v_\mathrm{EM}$ is constrained to a few parts in $10^{15}$ of $c$.
2. **A dynamics.** An action coupling $\mathbb{M}_+$ and $\mathbb{M}_-$ beyond the Lorentz rotor. This is the most natural completion of the framework's own hypothesis, and it would make the material–informational candidate real. The task is to write the coupling, quantize it, and compute the leading observable.
3. **A selection principle.** A boundary or quantization condition, or a symmetry, that singles out one structure among the many the algebra permits. The curved-spacetime construction illustrates the need: the frame field is inserted by hand and every Lorentzian metric is representable, so the algebra excludes nothing and predicts nothing there.

In each route the decisive question is whether the new input is **forced** by the algebra or **inserted**. If forced, the signature tests the framework; if inserted, it tests the insertion, and the framework's contribution is the language in which the insertion is written — a real contribution, but not an empirical signature of the algebra.

**Two lower-risk projects.** First, a systematic search for dimensionless consistency relations: any relation among standard parameters that the algebra implies and the standard formalism does not. This needs no new scale and would be immediately testable against constants known to many digits. Second, examine whether the local-complex-structure reading can differ from the standard reading where the standard dielectric response is itself non-local or strongly dispersive; the burden there is to exhibit a difference, not to reinterpret a standard result.

**A standing obligation and the honest outcome.** Because the framework is a reformulation, its equivalence should be re-examined domain by domain as new domains are developed: an article that *derives* rather than transcribes a standard result, or that finds the algebra forcing a number, would change the status of its domain. At present, however, the framework makes no prediction that distinguishes it from standard physics. Every candidate signature examined here traces to a quantity that is absent, undetermined, or posited; the agreements are agreements with the standard structures the framework shares; and the distinctive content enters no computation. The agenda is to derive a framework-specific quantity — most plausibly from a specified sector coupling or a forced dimensionless relation — or to establish that the algebra cannot produce one, a result about the framework as valuable as a signature.

## Summary

The biquaternion framework is a reformulation of standard physics, and on every domain the companion articles have developed it is currently empirically equivalent to what it reformulates: the single-qubit formalism, relativistic kinematics, Maxwell and Dirac theory, the hydrogen spectrum, the Casimir force, and the Unruh effect are all reproduced, not modified. This equivalence is structural. The framework's established content — the algebra $\mathbb{B}\cong M_2(\mathbb{C})$, the material sector $\mathbb{M}_-\cong\mathbb{R}^{3,1}$, the Hermitian sector $\mathbb{M}_+$ — is shared with the standard formalism, while its distinctive additions are interpretive labels that enter no formula producing a number. Any quantity fixed by the algebra alone is fixed identically by the standard theory, so a signature requires a non-algebraic input: a scale, a coupling, or a selection principle.

The candidates examined here supply none. Modified dispersion has no scale in the framework to act on, and the bounds that would test it (a linear Lorentz-violation scale above the Planck scale; $v_\mathrm{GW}-v_\mathrm{EM}$ within a few parts in $10^{15}$ of $c$) constrain only proposals that supply a scale. The local complex structure is a re-reading of the standard medium speed $c=1/\sqrt{\epsilon\mu}$. Birefringence and a second light cone are foreclosed by the single norm form. A material–informational coupling is unspecified — no field, no action, no constant — and is the framework's largest gap. Quaternionic quantum-statistical deviations are unavailable, because the algebra is complex and associative. Derived dimensionless relations, the one class that needs no new scale, are absent. And the celebrated reproductions — $g=2$, the hydrogen spectrum, the Casimir force, the Unruh temperature — are reproductions of standard results.

The main result is therefore negative, and meant to be: the framework currently makes no distinguishing prediction. The agenda is to specify and quantize the sector coupling and compute its leading observable, to search for a dimensionless relation the algebra forces, and to test whether the local complex structure can differ from the standard dielectric response in a regime the standard theory does not cover. In each case the decisive question is whether the input is forced by the algebra or inserted; only the first yields a signature of the framework, and only such a signature could settle the hypothesis.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_-$ | Anti-Hermitian subspace (material sector) |
| $\mathbb{M}_+$ | Hermitian subspace (informational sector) |
| $N(\tilde{Q})=\tilde{Q}\bar{\tilde{Q}}$ | Norm form (single quadratic form on $\mathbb{B}$) |
| $c=1/\sqrt{\epsilon\mu}$ | Local speed of light in the medium |
| $c_0=1/\sqrt{\epsilon_0\mu_0}$ | Vacuum speed of light |
| $\tilde{\nabla}$, $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}$ | Biquaternionic gradient, d'Alembertian |
| $\tilde{P}_\pm=\tfrac12(e_0\pm i\hat{\mu})$ | Idempotent (pure state) |
| $\tilde{H}=h_0e_0+i\mathbf{h}$ | Hermitian element (observable) |
| $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace formula (Born rule) |
| $\mathbb{B}\cong M_2(\mathbb{C})$ | The algebra is the standard complex $2\times2$ algebra |
| $SL(2,\mathbb{C})$ | Unit-norm-form biquaternions (Lorentz double cover) |

## Further Reading

- *Introduction to the Biquaternion Universe*, for the framework hypothesis and its list of open questions.
- *Why Complexify Spacetime?*, for the motivation of the complex structure and its explicit disclaimer of empirical predictions.
- *The Anti-Hermitian Subspace M- as the Material Sector*, for the identification of the four-vector sector and its signature.
- *The Hermitian Subspace M+ as the Informational Sector*, for the informational hypothesis, the disclaimer that the imaginary directions are not extra space, and the admission that it makes no distinguishing prediction.
- *Quantum Mechanics in Biquaternionic Form*, for the exact reproduction of the single-qubit formalism.
- *Relativistic Mechanics in Biquaternionic Form*, for the transcription of the ten mechanical formulas.
- *The Electron in Biquaternionic Form*, for the tree-level $g=2$ and the absence of the anomaly.
- *The Hydrogen Atom in Biquaternionic Form — The Relativistic Case*, for the quoted spectrum and the missing derivation.
- *The Vacuum State and the Casimir Effect in Biquaternionic Form*, for a standard result reproduced and explicitly not modified.
- *The Unruh Effect in Biquaternionic Form*, for a reformulation with no discriminator.
- *Gravitational Waves in Biquaternionic Form*, for the explicit statement that no deviation is predicted.
- *Canonical Quantization of the Biquaternion Maxwell Field*, for what the algebra does and does not supply in quantization.
- *Chiral Fermions in the Biquaternion Framework*, for the framework's vector-like abelian sector and its absent prediction.
- *Electromagnetism in Media — The Local Complex Structure at Work*, for the local complex structure as a reading of the standard medium parameter $c$.
- *The Renormalization Group in Biquaternionic Form*, for the explicit statement that the scale and the couplings are inputs the algebra does not fix.
- *The CPT Theorem in Biquaternionic Form*, for a standard theorem transcribed rather than established.
- *Entangled Subsystems in the Biquaternion Framework*, for the reproduced correlation function and the standard Tsirelson bound.
- *A Brief History of Biquaternions in Physics*, for the distinction between an algebra containing a structure and a physics using it.
