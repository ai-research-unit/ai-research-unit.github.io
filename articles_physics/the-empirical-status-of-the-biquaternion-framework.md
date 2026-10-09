# __The Empirical Status of the Biquaternion Framework__

## Introduction

This article asks what would count as an **empirical signature** of the biquaternion framework: a measurement whose outcome the framework predicts to differ from the prediction of standard physics. It is a research agenda, and its subject is the criteria a candidate must meet, not a catalogue of confident predictions.

The standing position of the series is stated here plainly. On every domain the companion articles have developed, the framework **agrees** with standard physics: the single-qubit formalism reproduces the Bloch ball, the Born rule, and the projective update exactly; relativistic mechanics reproduces the interval, the mass shell, and the four-force constraints exactly; Maxwell and Dirac are transcriptions; and the hydrogen spectrum, the Casimir force, the Unruh temperature, and the Bell/CHSH bounds are reproduced and not modified, while the CPT theorem is transcribed rather than established. The framework is a reformulation, and on each domain it reformulates it is currently **empirically equivalent** to what it reformulates. That is the starting point of this article, not a disappointment, and the main result below is that it is also, so far, the end point: no distinguishing prediction is made.

The temptation this article exists to resist is the opposite of that conclusion: to take a structure the framework contains — the two-sector decomposition, the local complex structure, the imaginary directions — call it a prediction, and name the experiment that would test it. The method adopted instead is to take each candidate in turn and ask:

1. Which framework-specific quantity does it depend on?
2. Is that quantity derived anywhere in this series, or merely posited?
3. What existing experimental bound already constrains it?

A candidate that traces to an undetermined parameter or an unverified claim is **not a signature**, and is labelled as such below; so is a candidate whose "prediction" is the standard result rewritten. The next section fixes what a signature would have to be and identifies the structural reason none is yet available; the sections after record the standing agreement, explain why it is not evidence for the framework's distinctive content, and examine the candidates individually.

Throughout, the notation is inherited from the read-list articles: the biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, and scalar imaginary $i$; the material sector is the anti-Hermitian subspace $\mathbb{M}_-$ and the informational sector the Hermitian subspace $\mathbb{M}_+$, with $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$; the biquaternion norm is $N(\tilde{Q})=\tilde{Q}\tilde{Q}^{\natural}$; the trace formula is $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$.

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
| Relativistic point mechanics | $N(d\tilde{Q})=-c^2dt^2+d\mathbf{x}^2$; $\tilde{P}\tilde{P}^{\natural}=-m^2c^2$; $\tilde{F}\tilde{P}^{\natural}+\tilde{P}\tilde{F}^{\natural}=0$ | Interval, mass shell, four-force orthogonality |
| Maxwell field | $\Box=\tilde{\nabla}\tilde{\nabla}^{\natural}=\partial_{ict}^2+\Delta$; Riemann–Silberstein field; invariants | Maxwell's equations in a medium |
| Dirac field | $\tilde{\nabla}\tilde{\Psi}_R=m\tilde{\Psi}_L$, $\tilde{\nabla}^{\natural}\tilde{\Psi}_L=m\tilde{\Psi}_R$; massless case $\tilde{\nabla}\tilde{\Psi}=0$ | Dirac equation, mass term |
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

**The Lorentz group.** The experiments that fix the kinematics — aberration of starlight, the Fizeau drag and the Michelson–Morley null result — select the group $SO^+(1,3)$, not a representation of it, and they are recorded with their ownership in *The Lorentz Transformation as a Biquaternionic Rotation*. The rotor conjugation reproduces them because it is a faithful representation of that group and cannot do otherwise; here the agreement is not even an achievement of transcription, since the experiments never test which faithful representation is used.

The lesson generalizes. When a reformulation reproduces a number, the question to ask is **which of its structures produced the number**. If the answer is the standard ones — the complex algebra, the Minkowski form, an inserted constant — then the number is not evidence for the framework's addition. This is the criterion applied to every candidate below.

## Candidate Signatures

Each candidate below is examined under the three questions of the Introduction and the four conditions of the second section. The order runs from the candidate with no home in the framework to the one that is, in the writer's judgement, the most promising, and it closes with a second warning rather than a candidate.

### A Fundamental Scale, and Modified Dispersion

**The candidate.** High-energy quantum-gravity models typically propose a modification of the dispersion relation — an energy-dependent speed of light, or a minimum length — appearing at a fundamental scale, often the Planck scale.

**The framework-specific quantity.** There is none. The algebra $\mathbb{B}$ and its coefficient field are dimensionless; the biquaternion norm, the product, and the conjugations carry no scale. Every dimensional quantity in the series is imported: the corpus records that the electron mass, charge, and $\hbar$ are inserted, and that the framework supplies neither the value of the fine-structure constant nor the magnitude of the Coulomb coupling. No article derives a fundamental length or energy. The companion article on the renormalization group puts the point sharply: the scale, the field content, the gauge group, and the values of the couplings are all inputs, and the algebra fixes none of them.

**Derived or posited.** Neither. This is stronger than "unverified": the candidate has no home in the framework as developed. There is no parameter whose absence could be repaired by more work on the same algebra — a scale must be inserted, and any inserted scale is an addition to the framework rather than a consequence of it.

**The existing bound.** The relevant bounds bound proposals that *do* supply a scale. The Fermi-LAT analysis of GRB 090510 already requires any linear energy dependence of the speed of light to set in above the Planck scale, $E_\mathrm{Pl}\approx1.22\times10^{19}$ GeV; and the gravitational-wave event GW170817 constrains $v_\mathrm{GW}-v_\mathrm{EM}$ to between $-3\times10^{-15}$ and $+7\times10^{-16}$ times $c$. These do not constrain the biquaternion framework, because the framework supplies no scale for them to act on. If a scale were inserted by hand, the bounds are tight enough to exclude most natural choices.

**Verdict.** Not a signature. A dispersion claim here would be the invention the Introduction warns against. A Clifford-algebra programme that *does* supply the missing scale, and is therefore addressable by the bounds just quoted, is recorded under *An External Programme That Supplies a Scale* below; it is a different framework from this one.

### The Local Complex Structure

**The candidate.** The framework's most distinctive physical claim after the two-sector reading is that the complex structure of $\mathbb{B}$ is **local**, its scale set by the local speed of light $c=1/\sqrt{\epsilon\mu}$. One might hope that an observable depends on the complex structure as such, and not merely on the standard electromagnetic properties of the medium.

**The framework-specific quantity.** The local speed $c(\mathbf{x})=1/\sqrt{\epsilon(\mathbf{x})\mu(\mathbf{x})}$, which fixes the embedding of physical time in the imaginary scalar direction, $\partial_{ict}=-(i/c)\,\partial_t$.

**Derived or posited.** The relation $c=1/\sqrt{\epsilon\mu}$ is **standard**, a consequence of the constitutive relations $\mathbf{D}=\epsilon\mathbf{E}$ and $\mathbf{B}=\mu\mathbf{H}$; the framework does not derive it. What is posited is the *identification* of this standard speed with the scale of the complex structure. Crucially, the framework adds no equation for $\epsilon$ or $\mu$: in every calculation of the series they are the standard medium parameters, supplied from outside.

**The existing bound.** None specific to the framework. Bounds on $\epsilon(\omega)$ and $\mu(\omega)$ are bounds on the standard medium response, which the framework takes as input; they do not test the complex-structure reading, because that reading makes no claim about their values.

**Verdict.** Not a signature. The *locality* of the complex structure is inherited entirely from the standard locality of $c(\mathbf{x})$, so any observable sensitive to it is already an observable of standard medium electromagnetism.

### A Second Light Cone, or Vacuum Birefringence

**The candidate.** The framework has two sectors, and the two sectors carry quadratic forms of opposite signature. Perhaps there are two null structures, hence a polarization-dependent propagation speed — birefringence — or a second, "informational" light cone.

**The framework-specific quantity.** The biquaternion norm $N(\tilde{Q})=\tilde{Q}\tilde{Q}^{\natural}$. It is a **single** quadratic form on $\mathbb{B}$, and its zero set is a single cone. Its restrictions to $\mathbb{M}_-$ and $\mathbb{M}_+$ are the mirror quadratic forms $-q_0^2+\mathbf{q}^2$ and $q_0^2-\mathbf{q}^2$; these are restrictions of the same form to complementary subspaces, not two independent propagation structures. A field propagating in the framework obeys one d'Alembertian $\Box=\partial_{ict}^2+\Delta$, built from one $c$. There is no second cone and no splitting of polarizations.

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

**The framework-specific quantity.** Unspecified. The only operations involving both sectors are multiplication by $i$, which exchanges them, and the rotor conjugation $\tilde{Q}\mapsto\tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{*}$, the standard Lorentz action. The companion article on $\mathbb{M}_+$ states that no dynamics for $\mathbb{M}_+$-valued fields is specified and that there is no coupling beyond the Lorentz one; the introduction lists a coupling between the sectors as an open question.

**Derived or posited.** Posited as a question. There is no field equation, no action, and no coupling constant.

**The existing bound.** If a specific coupling were written down — a Yukawa interaction of range $\lambda$ and strength $\alpha$, say — then torsion-balance, equivalence-principle, and atom-interferometry bounds would apply to it. With no parameter, nothing is constrained. And a coupling that is inserted rather than derived would make any resulting signature a test of the insertion, not of the framework.

**Verdict.** Not a signature, but the framework's largest gap and its best hope. This is the item on the agenda whose completion would most plausibly produce a genuine signature.

### Deviations in Quantum Statistics

**The candidate.** *Quaternionic* quantum physics is a real alternative to the complex theory with distinctive predictions — most notably a modification of two-particle interference. A reader meeting the word "biquaternion" might expect the framework to inherit them.

**The framework-specific quantity.** None, and this is a structural no-go rather than a gap. $\mathbb{B}$ is an **associative** algebra and is isomorphic to $M_2(\mathbb{C})$; it is a complex algebra, not a quaternionic Hilbert space. Its two-state sector is exactly the standard complex two-state theory. The framework therefore sits on the same side as standard quantum physics in every interference test, and it does not inherit the quaternionic programme's deviations.

**Derived or posited.** The exact complex structure is derived. The deviations are absent by algebra, not merely unverified.

**The existing bound.** Precision interference and two-particle tests are consistent with complex quantum physics; the framework shares that agreement exactly. There is no framework-specific number to compare.

**Verdict.** Not a signature, and a warning. This is the candidate on which a careless writer is most likely to claim a signature — or, worse, to claim the quaternionic predictions under a biquaternionic name. The framework is not a quaternionic Hilbert-space theory, and the predictions of that programme are not available to it.

### Derived Dimensionless Relations

**The candidate.** The class of signatures that does not require a new scale: a relation among **standard** parameters — a ratio, a mixing angle, a sum rule — that the algebra forces and the standard theory leaves free. This is the one form a scale-free algebra can take.

**The framework-specific quantity.** None exists in the corpus. No article derives a value for a coupling, a mass ratio, or a mixing angle. The series says so where it matters: the hydrogen article records that the framework does not supply the dimensionless coupling; the electron article records that the mass and charge are inserted; the chiral-fermion article records that the abelian sector is vector-like and offers no charge assignment.

**Derived or posited.** Nothing is derived; this is the empty cell of the framework.

**The existing bound.** Whichever relation were proposed, the standard constants are known to many digits, so a derived relation would be immediately and sharply testable. The absence here is a limit of the framework's derivation, not of experimental precision.

**The nearest external claim, and why it does not fill the cell.** The one programme the corpus knows that claims masses fixed by structure rather than by a fitted potential is the Einstein–Mayer route in Gsponer and Hurni's four-page Lanczos-centenary contribution (1994; arXiv:hep-ph/0112317): the fermion masses there are **eigenvalues of a generalized mass operator** rather than Yukawa outputs, so no Higgs is needed, and the neutrino and u-quark masses come out zero. It is the right *form* for this cell — a mass fixed by the structure rather than inserted — and it is worth naming here for that reason. It does not fill the cell, for two reasons stated in *The Standard Model under the Biquaternion Framework*. First, the observable content of a mass sector is the **pattern** of ratios and mixings, and the source exhibits no ratio and no mixing angle. Second, the couplings are claimed to be the Standard Model's own two free parameters $e$ and $\sin^2\theta$, so what is fixed is the *existence* of masses, not a value. A derived mass relation would be a genuine item for this section; a mechanism that makes masses eigenvalues while leaving every ratio free is a change of bookkeeping. The item is nonetheless the closest thing the corpus holds, and it is recorded as such rather than dismissed.

**Verdict.** The most promising candidate class, and currently empty. What would settle it is stated in the next section.

### Unverified Framework Claims: the Entropy Functional

**The candidate.** The corpus floats a small number of framework-specific proposals that are not yet verified. The clearest is an entropy functional on the states of $\mathbb{M}_+$, written $S(\tilde{\rho})=-2\,\mathrm{Sc}(\tilde{\rho}\log\tilde{\rho})$ and recorded in the companion article as *needing verification*.

**The framework-specific quantity.** The functional $S(\tilde{\rho})$, if it were well defined.

**Derived or posited.** Posited, and not yet verified: the biquaternion logarithm is multivalued, and no article shows that the expression is real, concave, or additive on the states of $\mathbb{M}_+$. Even if all of that were established, it is a transcription of the standard von Neumann entropy $S(\rho)=-\mathrm{Tr}(\rho\log\rho)$ and would agree with the standard theory rather than deviate from it.

**The existing bound.** None applies, because a transcribed entropy functional makes no new prediction.

**Verdict.** Not a signature, and a second warning: an item whose "signature" traces to an unverified claim is not a signature until the claim is verified, and here verification would still leave the standard result in place.

### Empirical Claims of an External Programme

**The candidate.** A programme outside the framework — the electro-gravimagnetic model of L. A. Alexeyeva, recorded in *The Electro-Gravimagnetic Field and the Magnetic-Charge–Mass Hypothesis* — adopts the framework's A-field and adds a hypothesis: magnetic charge density is gravitational mass density. It then claims three consequences: a solenoidal electric field from rotating mass (the Earth's electric axis), an orbital shift from an "electromass" force, and a comparison with the cogravity term used by Matos and Tajmar for the perihelion of Mercury.

**The framework-specific quantity.** None of the framework's. The claims do not use $\mathbb{M}_+$, the rotor action, or any structure of $\mathbb{B}$ beyond the A-field, which the framework itself reads as the dual field strength and not as an independent object. The distinctive input is the magnetic-charge–mass identification, which the algebra does not force.

**Derived or posited.** Posited, and by an external author, not by the framework. The identification is a hypothesis; the corpus's monopole article admits magnetic charge algebraically and derives the Dirac condition but draws no mass identification from it.

**The existing bound.** A field identified with gravity would be constrained by equivalence-principle and torsion-balance tests. The programme states no coupling strength or range, so nothing is yet bounded, and the later revision of the programme (the conservation law of a single open source is not Lorentz invariant under interaction, repaired by a scalar resistance field) shows that its internal consistency was provisional on the conservation side. The author's 2017 paper proves the charges–currents interaction equations invariant under the Poincaré–Lorentz group and derives the transformation formulae for charge, current, power and force. That result is about the *equations*, not about the closedness condition the 2009 paper found non-invariant, so it does not restore the earlier conservation claim; the corpus records both and states the reconciliation in *The Electro-Gravimagnetic Field and the Magnetic-Charge–Mass Hypothesis*. The paper offers the invariance proof itself as "mathematical justifiability" of the model and its "adequacy" to existing physical ideas about matter, space and time. The corpus's criterion is the reverse — covariance and elegance are not evidence (see *Why Agreement Is Not Confirmation*) — so the argument is recorded as the author's and carries no weight here.

**Verdict.** Not a signature of the framework, and not the framework's claim. It is recorded because it is the most developed physical reading of the dual field strength that the corpus knows of, and because a reader meeting the A-field should see both readings named and separated. The corpus's own verdict on the framework is untouched by it: the claims are qualitative, attributed, and testable in principle but unpredicted in practice.

### An External Programme That Supplies a Scale

**The candidate.** The one gap this article keeps finding is a scale, and there is a Clifford-algebra programme that fills it. *Extended relativity in Clifford spaces* — the principal review is by Castro and Pavšič (2004) — takes the coordinates of the arena to be Clifford-valued polyvectors rather than points, so that lines, areas and volumes carry coefficients alongside the four vector coordinates. On that arena the programme supplies exactly the missing items: an **invariant length**, whose quantization is said to give a **minimal Planck scale**; a **maximal acceleration**; the invariance of **minimal Planck areas** under acceleration boosts, which is read as a **maximal-tension principle**; and modified dispersion and minimal-length uncertainty relations.

**The framework-specific quantity.** None of the biquaternion framework's. The programme is built on a larger Clifford algebra and takes the invariant length as the parameter that bridges quantities of different grade on its arena. The biquaternion algebra $\mathbb{B}$ is the even part of a four-dimensional Clifford algebra; it has no grade structure to bridge and no parameter to bridge it with.

**Derived or posited.** The scale is **posited**. The construction fixes an invariant length and then exhibits quantities that survive acceleration boosts; it does not derive the value of the length. So the programme is an instance of the pattern this article has been naming, not an exception to it: a scale inserted, and then consequences computed from it.

**The existing bound.** The bounds recorded under *A Fundamental Scale, and Modified Dispersion* act here, because this programme does supply the scale they need. A linear energy dependence of the speed of light is already required to set in above the Planck energy by the Fermi-LAT analysis of GRB 090510, and GW170817 bounds $v_\mathrm{GW}-v_\mathrm{EM}$ to a few parts in $10^{15}$ of $c$. A maximal acceleration is a separate, long-standing conjecture (Caianiello and others); no confirmed signature of it exists.

**Verdict.** Not a signature of the biquaternion framework, and not a claim of this series. It is recorded as the **contrast case**, because it answers the objection a reader will raise — *why not simply add a scale?* — by showing what adding one costs. Castro and Pavšič do not keep the manifold: their coordinates are non-commuting polyvectors, so the arena is not a space of points, and dimension including the signature has to be rebuilt slice by slice (the remark in *The Clifford Algebra Representation* reproduces the Euclidean–Minkowski-generators example behind that idea). A scale in the biquaternion framework would have to come the same way, as an addition to the algebra rather than a consequence of it. The construction of the arena is recorded in *Curved Spacetime and the Biquaternion Framework*, section *The Arena Alternative: Algebra Valued Coordinates*.

### An External Programme That Varies the Speed of Light

**The candidate.** A programme outside the framework — the biquaternion relativity of A. Waser (2011) — takes the framework's complexified four-position and four-velocity and reads gravitation as the effect of a spatially varying speed of light, $c=c_0f(\mathbf{x})$, with the profile fixed by requiring the model's own force $F_g=-mc\,\nabla c$ to reproduce Newton's law. From that one input the paper derives the Schwarzschild line element, the classical equation of motion with perihelion precession, the gravitational redshift, free transverse gravitation waves of velocity $c$, and a screened field of a point charge.

**The framework-specific quantity.** None of the framework's. The programme uses the four-velocity biquaternion, the semi-biquaternion product, and the complexified four-position, which the corpus's companion articles read as a rewriting of standard four-vector kinematics. Its distinctive content is the added hypothesis that $c$ varies with position and that the line element is $ds^2=-f^2c_0^2\,dt^2+(dr^2+r^2d\Omega^2)/f^2$. The algebra does not force either.

**Derived or posited.** Mixed, and the split is the point. The profile is **fitted**, not derived: it comes from setting the model's force law equal to Newton's, so Newton's law is the input. The inverse squaring of the spatial part of the line element is a **second posit**, independent of the profile, and it is what carries the construction to the Schwarzschild form. The consequence is checkable and worth stating: at the profile the paper derives, $f=e^{-r_s/(2r)}$, the metric is **not** Ricci-flat ($R_{11}=-r_s^2/(2r^4)$ in the corpus's curvature convention, recomputed here), so it is not a vacuum solution of Einstein's equations. The Schwarzschild metric is the first-order truncation of that profile, which is why the classical tests come out right at leading order and differ only at order $(r_s/r)^2$.

**The existing bound.** Two, and both are empty by a wide margin. The model's deviation from general relativity is of order $(r_s/r)^2$, which at the solar surface is $1.8\times10^{-11}$ — far below the precision of the classical tests the programme reproduces. The programme's own distinctive prediction is a screening factor $e^{-Gm/(c_0^2r)}$ in the static field of a mass: this is $1-2.1\times10^{-6}$ at the solar surface, $1-7.0\times10^{-10}$ at the Earth's surface, and below $1-10^{-25}$ for any laboratory mass at laboratory separations. No experiment reaches either.

**Verdict.** Not a signature of the framework, and not the framework's claim. It is recorded because it is the one worked-out route by which a varying $c$ reaches the Schwarzschild metric — a route the framework's own local scale factor does not take, as *Curved Spacetime and the Biquaternion Framework*, section *What the Restricted Class Cannot Do*, records — and because it shows the price of the route: two inserted inputs, the fitted profile and the spatial scaling, and a metric that is not itself a vacuum solution. Its provenance is worth noting with the claims: the paper is self-issued, with no journal, DOI or arXiv identifier.

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

1. **A scale.** A fundamental length or energy, whether by deforming the algebra (a quantum group, a non-commutative spacetime) or by adding a dimensionful parameter. This would make the modified-dispersion candidate real, but the bound it must beat is severe: a linear dispersion scale must already lie above the Planck scale, and $v_\mathrm{GW}-v_\mathrm{EM}$ is constrained to a few parts in $10^{15}$ of $c$. **A concrete picture for this route**, which the corpus previously named without exemplifying: the non-commutative arena of *Maxwell's Theory on Non-Commutative Spaces and Quaternions* is a deformation of exactly this kind, and it shows what one delivers — the vacuum becomes a non-linear medium, the dual symmetry is broken, and the propagation velocity acquires a dependence on a background field, so that the speed of light is no longer universal. It also shows the price in its sharpest form: the deformation is **inserted**, not forced — the background $\theta^{\mu\nu}$ is put in by hand, is not a Lorentz scalar, and is precisely the kind of object that every Lorentz-violation bound constrains. Route 1 is therefore not empty; what it delivers is a deformation that tests the insertion and not the algebra, which is this section's general point in a worked case.
2. **A dynamics.** An action coupling $\mathbb{M}_+$ and $\mathbb{M}_-$ beyond the Lorentz rotor. This is the most natural completion of the framework's own hypothesis, and it would make the material–informational candidate real. The task is to write the coupling, quantize it, and compute the leading observable.
3. **A selection principle.** A boundary or quantization condition, or a symmetry, that singles out one structure among the many the algebra permits. The curved-spacetime construction illustrates the need: the frame field is inserted by hand and every Lorentzian metric is representable, so the algebra excludes nothing and predicts nothing there.

In each route the decisive question is whether the new input is **forced** by the algebra or **inserted**. If forced, the signature tests the framework; if inserted, it tests the insertion, and the framework's contribution is the language in which the insertion is written — a real contribution, but not an empirical signature of the algebra.

**Two lower-risk projects.** First, a systematic search for dimensionless consistency relations: any relation among standard parameters that the algebra implies and the standard formalism does not. This needs no new scale and would be immediately testable against constants known to many digits. Second, examine whether the local-complex-structure reading can differ from the standard reading where the standard dielectric response is itself non-local or strongly dispersive; the burden there is to exhibit a difference, not to reinterpret a standard result.

**A standing obligation and the honest outcome.** Because the framework is a reformulation, its equivalence should be re-examined domain by domain as new domains are developed: an article that *derives* rather than transcribes a standard result, or that finds the algebra forcing a number, would change the status of its domain. At present, however, the framework makes no prediction that distinguishes it from standard physics. Every candidate signature examined here traces to a quantity that is absent, undetermined, or posited; the agreements are agreements with the standard structures the framework shares; and the distinctive content enters no computation. The agenda is to derive a framework-specific quantity — most plausibly from a specified sector coupling or a forced dimensionless relation — or to establish that the algebra cannot produce one, a result about the framework as valuable as a signature.

## Physical Readings

The reading that matters for this article is which readings are testable. The frame-independent content — the sesquilinear pair, the zero-divisor cone and the period $2\pi$ of the central phase — is where a signature would have to sit, because the interval and the composition move with the local complex structure and a change of them is not an observable (*Conventions in the Biquaternion Universe*). The clock reading of the sector exchange is on the other side of the line: it reorganises existing structures and adds no prediction, so the article's inventory of candidate signatures is unchanged by it. A further named reading can be added.

- **Selection-rule reading.** The invariance under a change of the local complex structure is read as a selection rule for observable content: only the content the change cannot move — the sesquilinear pair, the zero-divisor cone and the period $2\pi$ — can carry a signature, so the rule excludes a candidate before any experiment is run and is the framework's own filter on its inventory. Boundary: a selection rule is not a prediction, the inventory of candidate signatures is unchanged, and the invariance statement is owned by *The Local Complex Structure and the Speed of Light*.

## Summary

The biquaternion framework is a reformulation of standard physics, and on every domain the companion articles have developed it is currently empirically equivalent to what it reformulates: the single-qubit formalism, relativistic kinematics, Maxwell and Dirac theory, the hydrogen spectrum, the Casimir force, and the Unruh effect are all reproduced, not modified. This equivalence is structural. The framework's established content — the algebra $\mathbb{B}\cong M_2(\mathbb{C})$, the material sector $\mathbb{M}_-\cong\mathbb{R}^{3,1}$, the Hermitian sector $\mathbb{M}_+$ — is shared with the standard formalism, while its distinctive additions are interpretive labels that enter no formula producing a number. Any quantity fixed by the algebra alone is fixed identically by the standard theory, so a signature requires a non-algebraic input: a scale, a coupling, or a selection principle.

The candidates examined here supply none. Modified dispersion has no scale in the framework to act on, and the bounds that would test it (a linear Lorentz-violation scale above the Planck scale; $v_\mathrm{GW}-v_\mathrm{EM}$ within a few parts in $10^{15}$ of $c$) constrain only proposals that supply a scale. The local complex structure is a re-reading of the standard medium speed $c=1/\sqrt{\epsilon\mu}$. Birefringence and a second light cone are foreclosed by the single norm. A material–informational coupling is unspecified — no field, no action, no constant — and is the framework's largest gap. Quaternionic quantum-statistical deviations are unavailable, because the algebra is complex and associative. Derived dimensionless relations, the one class that needs no new scale, are absent. And the celebrated reproductions — $g=2$, the hydrogen spectrum, the Casimir force, the Unruh temperature — are reproductions of standard results.

The main result is therefore negative, and meant to be: the framework currently makes no distinguishing prediction. The agenda is to specify and quantize the sector coupling and compute its leading observable, to search for a dimensionless relation the algebra forces, and to test whether the local complex structure can differ from the standard dielectric response in a regime the standard theory does not cover. In each case the decisive question is whether the input is forced by the algebra or inserted; only the first yields a signature of the framework, and only such a signature could settle the hypothesis.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_-$ | Anti-Hermitian subspace (material sector) |
| $\mathbb{M}_+$ | Hermitian subspace (informational sector) |
| $N(\tilde{Q})=\tilde{Q}\tilde{Q}^{\natural}$ | Biquaternion norm (single quadratic form on $\mathbb{B}$) |
| $c=1/\sqrt{\epsilon\mu}$ | Local speed of light in the medium |
| $c_0=1/\sqrt{\epsilon_0\mu_0}$ | Vacuum speed of light |
| $\tilde{\nabla}$, $\Box=\tilde{\nabla}\tilde{\nabla}^{\natural}$ | Biquaternionic gradient, d'Alembertian |
| $\tilde\Pi_\pm=\tfrac12(e_0\pm i\hat{\mu})$ | Idempotent (pure state) |
| $\tilde{H}=h_0e_0+i\mathbf{h}$ | Hermitian element (observable) |
| $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace formula (Born rule) |
| $\mathbb{B}\cong M_2(\mathbb{C})$ | The algebra is the standard complex $2\times2$ algebra |
| $SL(2,\mathbb{C})$ | Unit-norm biquaternions (Lorentz double cover) |

## Further Reading

- *Introduction to the Biquaternion Universe*, for the framework hypothesis and its list of open questions.
- *Why Complexify Spacetime?*, for the motivation of the complex structure and its explicit disclaimer of empirical predictions.
- *The Anti-Hermitian Subspace M- as the Material Sector*, for the identification of the four-vector sector and its signature.
- *The Hermitian Subspace M+ as the Informational Sector*, for the informational hypothesis, the disclaimer that the imaginary directions are not extra space, and the admission that it makes no distinguishing prediction.
- *Quantum Physics in Biquaternionic Form*, for the exact reproduction of the single-qubit formalism.
- *Relativistic Mechanics in Biquaternionic Form*, for the transcription of the ten mechanical formulas.
- *The Electron in Biquaternionic Form*, for the tree-level $g=2$ and the absence of the anomaly.
- *The Hydrogen Atom in Biquaternionic Form — The Relativistic Case*, for the quoted spectrum and the missing derivation.
- *The Vacuum State and the Casimir Effect in Biquaternionic Form*, for a standard result reproduced and explicitly not modified.
- *The Unruh Effect in Biquaternionic Form*, for a reformulation with no discriminator.
- *Gravitational Waves in Biquaternionic Form*, for the explicit statement that no deviation is predicted.
- *Canonical Quantization of the Biquaternion Maxwell Field*, for what the algebra does and does not supply in quantization.
- *Chiral Fermions in the Biquaternion Framework*, for the framework's vector-like abelian sector and its absent prediction.
- *The Electro-Gravimagnetic Field and the Magnetic-Charge–Mass Hypothesis*, for the external programme that reads the A-field as an electro-gravimagnetic field and claims solenoidal-electric, electromass and cogravity effects; recorded there, attributed, and not endorsed here.
- *Electromagnetism in Media — The Local Complex Structure at Work*, for the local complex structure as a reading of the standard medium parameter $c$.
- *The Renormalization Group in Biquaternionic Form*, for the explicit statement that the scale and the couplings are inputs the algebra does not fix.
- *The CPT Theorem in Biquaternionic Form*, for a standard theorem transcribed rather than established.
- *Entangled Subsystems in the Biquaternion Framework*, for the reproduced correlation function and the standard Tsirelson bound.
- *A Brief History of Biquaternions in Physics*, for the distinction between an algebra containing a structure and a physics using it.
- *Curved Spacetime and the Biquaternion Framework*, section *The Arena Alternative: Algebra Valued Coordinates*, for the Clifford-valued-coordinate arena in which the scale of the external programme recorded under *An External Programme That Supplies a Scale* is natural.
- A. Waser, "Biquaternion Relativity — Gravitation as an Effect of Spatial Varying Speed of Light" (self-issued, issued 1 January 2011, 8 pp.), for the external programme recorded under *An External Programme That Varies the Speed of Light*: the varying-$c$ hypothesis, the profile fitted to Newton's law, the Schwarzschild line element obtained from its first-order truncation, the screened static field of a point charge, and the claim of free transverse gravitation waves. A self-issued preprint with no journal, DOI or arXiv identifier; cited for the construction and its own claims, with its curvature and its screening sizes recomputed here.
