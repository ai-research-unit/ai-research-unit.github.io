# __Reading an Extra Component: The Gürsey Default, the Reversion Test, and the Prior-Art Warning__

## Introduction

**Every biquaternion reformulation of a standard equation doubles something.** Replace the two-component spinor by a single element of the algebra and the element has more components than the field it replaced; promote the mass from a scalar to an element and the count rises again. The extra components have to be *read*, and the reading is not neutral: the same doubling can be presented as a discovery or as a bookkeeping artefact, and the two presentations differ by nothing in the algebra.

**Three criteria, from one short source.** A four-page comment by Gsponer and Hurni (2001) on biquaternion and Clifford formulations of the Dirac, Proca and Maxwell equations supplies all three, and nothing in it is a new equation. It lists the difficulties that a noncommutative formulation creates; it gives the **isospin reading**, attributed there to Gürsey, as the default interpretation of an extra component; it states a **legitimacy test** — irreducible under the full Poincaré group and covariant under reversion; and it closes with a **prior-art warning**, that most, if not all, apparently new results in the genre can be read with standard concepts and no new physics. Its value is criterial, and this article records the criteria in one place.

**Why one place, and why here.** The criteria are used across the corpus and derived nowhere in it. Every article that replaces a multicomponent object by one element of the algebra reads the surplus by them: the Dirac and Klein–Gordon and Proca articles read a doubling, the coupled-equation articles read a pair of masses, and any article that promotes a parameter to an element reads an eigenvalue. Filing them under one heading means an article can cite a criterion instead of restating it, and means the criteria can be revised once instead of a dozen times.

**What this article is not.** It is not a defence of the genre and not a verdict on the framework. The source is sympathetic to the programme and states the warning against it in the same four pages, and both halves are recorded here, because a corpus that can cite an external statement of its own discipline is in a stronger position than one that asserts that discipline about itself.

## The Difficulties a Noncommutative Formulation Creates

**Information is lost, and the loss has a shape.** Compared with a matrix or tensor formulation, one written in numbers that do not commute suffers losses of three kinds: the numbers carry no index, so an index that a tensor made explicit is now positional or implicit; noncommutativity introduces ambiguities of ordering; and residual definitional freedom remains wherever a product can be bracketed differently. None of the three is fatal, and all three are the reason a biquaternion result needs a dictionary before it needs an interpretation.

**The component count rises twice.** A vector or a two-part field replaced by one number of the algebra becomes a single object with more components than the object it replaces, and an ordinary scalar such as the mass, promoted to an element, does it a second time. This is the difficulty the corpus meets most often, and it is the one the default reading below is designed to absorb.

**The quantum imaginary, and the one place where the algebra is not a matter of taste.** The fifth difficulty in the source's list is the one the corpus's own algebra is exempt from. With a **real** algebra of this kind in place of a complexified one, the quantum-mechanical imaginary is left implicit, and the source records the well known fact that if "$i$" is not explicit in a quantum theory it must be replaced by special rules or by an equivalent antiunitary operator. The comment chooses the biquaternions precisely because they are the complexified algebra, $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, in which the quantum interpretation raises no such difficulty; the corpus's central scalar imaginary is the explicit $i$ that the condition demands. That is the one place in the list where the framework's *choice of algebra* is a matter of argument and not of taste, and it is the positive side of the fact recorded in [The Empirical Status of the Biquaternion Framework](the-empirical-status-of-the-biquaternion-framework.html): quaternionic quantum-statistical deviations are unavailable here because the algebra is complex and associative, so the same complexification that forecloses the deviations leaves the quantum interpretation unrestricted.

**What the list is for.** It is a checklist, not an objection. Each difficulty names a place where a biquaternion reformulation can manufacture a result that is really a change of bookkeeping, and the three criteria below answer the first two of them: the default reading absorbs the surplus components, the legitimacy test rules out the formulations that cannot be made covariant, and the warning tells the reader what to expect when neither has been applied.

## The Default Reading: An Extra Component Is a Multiplicity

**The rule.** The source records that the difficulties were met long ago — by Lanczos, by Proca, by Einstein — and that in the interpretation **Gürsey** initiated they are resolved by recognising that **most such generalisations describe superpositions of particles of different intrinsic spin and isospin**. The corpus adopts that as its default: an extra component in a biquaternion reformulation is read as a spin or isospin multiplicity unless something forces a different reading, and the burden of proof lies with the different reading.

**The worked instance is the simplest generalisation of the Dirac equation.** Replacing the two two-component objects of the older Dirac theory by two biquaternions $A$ and $B$ gives Lanczos's fundamental system

$$
\vec\nabla_\Phi A = mB, \qquad \vec\nabla_\Phi B = mA,
$$

invariant under $A\to AG$, $B\to BG$ with $G$ $*$-unitary, and the doubled solution count is the **isospin doublet** of two spin-$\tfrac12$ superpositions. The source assembles the two superpositions $D_+$ and $D_-$ from the solutions and their conjugates: each takes one value of the chirality from $A$ and the other from the conjugate of $B$, and the two differ by the exchange of those two values and by a right multiplication by $i\vec e_1$, the unit perpendicular to the axis $\vec e_3$. Both satisfy the Klein–Gordon equation, and the combined form

$$
\vec\nabla_\Phi D = mD^{*}i\vec e_z
$$

is strictly equivalent to Dirac's equation of the older literature. The isospin reading is the source's resolution of the doubling: the interpretation of $D_+$ and $D_-$ as an isospin doublet, attributed there for the first time to Gürsey, is what "solves the 'doubling' problem that puzzled Lanczos", and the same authors' Hamilton review draws out the particle content — $D_+$ the proton, $D_-$ the neutron, so that Lanczos's doubling is isospin.

**The reading's status.** It is an interpretation and not a theorem, and it is the corpus's default rather than its conclusion. What it does is give the surplus a physical slot — a multiplicity of existing particles — instead of leaving it as an unnamed extra degree of freedom that a reader may mistake for new physics. It is the interpretive companion of the framework's repeated structural finding that the algebra contains more than the physics selects, recorded as an obstruction in [What the Biquaternion Algebra Cannot Do: A Catalogue of Algebraic Obstructions](what-the-biquaternion-algebra-cannot-do-a-catalogue-of-algebraic-obstructions.html).

**Where it is used.** The Dirac article works the doubling on its own carrier; the Klein–Gordon and Proca articles meet the same surplus when the field is promoted from a two-part object to one element; and the coupled-equation articles read their two masses by exactly this rule. None of them re-derives it, and each cites this article for it.

## A Worked Instance: The Einstein–Mayer Equation

**Promoting the mass.** The same source records the general form, which it attributes to Einstein and Mayer: promote the mass $m$ to a biquaternion $E$, the "hypercomplex mass", and the pair becomes

$$
\vec\nabla_\Phi A = B E^{\dagger},
\qquad
\vec\nabla_\Phi B = A E ,
$$

so that the two fields no longer share one mass: the second-order equations become eigenvalue equations for it. This is the smallest case in which a parameter of the standard theory is replaced by an element of the algebra, and it is therefore the case in which the component count rises for the second time.

**The two standard interpretations, and the algebraic facts that make both available.** When $E E^{\dagger} = m^2$ the pair is degenerate and reads as a **proton–neutron** isospin doublet, and with a pseudoscalar $E$ the charge-independent theory of nuclear forces; when $E E = 0$ one of the two masses necessarily vanishes and the pair reads as an **electron–neutrino** doublet, and with a parity-violating $SU(2)$ gauge the low-energy weak phenomenology is equivalent to the Standard Model's. Two algebraic facts make both available, and both are checked in the corpus: the product of a biquaternion with its quaternion conjugate is central and equals $\sum_i q_i^2$, so a real scalar coefficient $E=s$ gives the same mass $m^2=s^2$ to both members of the pair; and the null equation $E\circ E=0$ has nonzero solutions — the zero divisors, of which $E=\vec e_x+i\vec e_y$ is one.

**Carried further.** If $E$ is derivatively coupled, $\vec\nabla_\Phi E = AB$, the system gives Petiau's double-periodic waves, interpolating between de Broglie and solitonic solutions — the construction is worked in [The Petiau System and the Quantisation of Mass in Biquaternionic Form](the-petiau-system-and-the-quantisation-of-mass-in-biquaternionic-form.html). If $E$ is read as the Higgs field,

$$
\Box_\Phi E = -\mu E + \lambda E E^{\dagger} E
$$

is invariant under $E \to G^{*} E H$ and carries the manifest $SU(2)_L\times SU(2)_R$ symmetry of the sigma model that leads to the electroweak theory after the $SU(2)_R$ breaking. The reader will meet that reading again in [The Higgs Mechanism in Biquaternionic Form](the-higgs-mechanism-in-biquaternionic-form.html), where the external claim and its limits are examined.

**Why the instance matters beyond itself.** It is the model for every later promotion in the corpus: a coupling, a mass, an order parameter written as an element instead of a number, with the surplus components read by the default above and the result checked against a standard theory. It is also the instance that shows the honest limit of the method, because the source's own verdict on it is that its outputs are Standard Model **re-descriptions** and not derivations.

## The Legitimacy Test

**The requirement.** The source states the condition under which such a formulation is to be trusted: every field must be an **irreducible representation of the full Poincaré group, including the discrete space and time reversal symmetries**, and must be **covariant under reversion** — a requirement the authors call specific to any theory written with numbers of this kind. This is a checkable filter with two halves, and both are used.

**Irreducibility under the full Poincaré group.** A field that is reducible under the connected group, or that fails under parity or time reversal, is not a physical field of the standard kind whatever its equation says. The corpus's discrete-symmetry material supplies the test in operational form: [The CPT Theorem in Biquaternionic Form](the-cpt-theorem-in-biquaternionic-form.html) states which combinations of the conjugations the discrete operations correspond to, and the conjugations and their fixed spaces are catalogued in [Comparison of the Remarkable Subspaces](../articles_maths/comparison-of-the-remarkable-subspaces.html).

**Covariance under reversion.** Reversion is one of the algebra's conjugations, and the general identification of reversal with it is in [Matrix Representations Conventions](matrix-representations-conventions.html), §*The Clifford Structure*. A formulation is covariant under reversion when the reversal of an equation is the equation with every reversed object replaced; an equation that holds only in one reversion class is a formulation of half the object.

**The qualifier, and it is the source's own.** The test is a **condition** a formulation in numbers of this kind must meet, and not a theorem that every biquaternion equation meets. Passing it does not certify a formulation as new or as correct; failing it disqualifies one. That asymmetry is why the filter is used as a screen and never as a result.

## The Prior-Art Warning

**The conclusion of the source.** Under the two conditions above, many of the difficulties of noncommutative numbers of this kind can be overcome, and most if not all apparently new results can be interpreted using standard concepts and without introducing new physics. The authors are sympathetic to the programme and state this in the same four pages as its defence, which is what makes the sentence usable.

**Why the corpus records it.** It is the corpus's own standing caution, stated externally and twenty years earlier, and it is recorded for exactly that reason: the framework's discipline should be citable from outside the framework. The same authors' review work argues the opposite side — that the physics can reside in the mathematical structure — and both are recorded, because a programme's value and its novelty are different questions and neither settles the other.

**What it costs an article.** An article in this category that reports a biquaternion result is expected to say which of the two it has: a re-description, which is the default and the common case, or a derivation, which needs a prediction. [The Empirical Status of the Biquaternion Framework](the-empirical-status-of-the-biquaternion-framework.html) applies the same test domain by domain and reaches the same answer in every domain developed so far.

## What the Criteria Do Not Do

**They do not select between plural readings.** The default reading says that an extra component is a multiplicity; it does not say which multiplicity. Where two readings are available — an isospin doublet or two particle species, a pseudoscalar mass or a chiral one — the criteria are silent and the algebra alone does not choose. The corpus states both and says that it chooses neither.

**They do not turn a reformulation into a prediction.** A formulation that passes the legitimacy test is well formed; nothing in the test compares it with experiment. The framework's empirical position, stated in [The Empirical Status of the Biquaternion Framework](the-empirical-status-of-the-biquaternion-framework.html), is agreement with the standard theory on every domain developed, and no criterion here changes that.

**They do not license a new sector.** The Einstein–Mayer instance shows that a scalar sector can be written on paper, not that the framework supplies one. The corpus records the paper route and its verdict side by side, and the article that needs the scalar — [The Standard Model as the Low-Energy Phase: The U(2) Ceiling and the Four Unbuilt Sectors](the-standard-model-in-the-biquaternion-framework-the-u2-ceiling-and-the-four-unbuilt-sectors.html) — marks the sector as *no route yet* even while citing the paper route.

## Summary

**Three criteria and one warning, recorded once.** A noncommutative formulation of a standard equation loses index information, gains ambiguities and gains components; the surplus components are read by the Gürsey default, as a spin or isospin multiplicity; a formulation is legitimate when every field is irreducible under the full Poincaré group and the equation is covariant under reversion; and the prior-art expectation is that a result of this kind is a re-description of standard physics until a prediction says otherwise.

**The worked instance is the promoted mass.** The Einstein–Mayer pair replaces one scalar mass by an element and produces the degenerate isospin case, the null case with one vanishing mass, Petiau's waves under derivative coupling, and a sigma-model route to electroweak breaking, with the source's own verdict that these are re-descriptions.

**The limit.** The criteria screen formulations; they do not choose between plural readings, do not supply a prediction, and do not build the sector an article may need. Each of the three is stated where the corpus uses it.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$, $B$ | the two biquaternion fields of Lanczos's fundamental system |
| $D_+$, $D_-$ | the two superpositions of §*The Default Reading*, read as an isospin doublet |
| $E$ | the Einstein–Mayer hypercomplex mass, an element of $\mathbb{B}$ |
| $E^{\dagger}$ | its Hermitian conjugate, the dagger of *Operator and Calculus Conventions* |
| $G$ | a $*$-unitary element, the gauge freedom of the Lanczos system |
| $\vec\nabla_\Phi$ | the gradient of the $\mathbb{B}$ frame, unhalved, as in *Frame and Metric Conventions* |
| $G$, $H$ | the two factors of the sigma-model invariance $E\mapsto G^{*}EH$ |

## Further Reading

- A. Gsponer and J.-P. Hurni, "Comment on Formulating and Generalizing Dirac's, Proca's, and Maxwell's Equations with Biquaternions or Clifford Numbers", *Foundations of Physics Letters* **14**(1) (2001) 77–85 (arXiv:math-ph/0201049), for the list of difficulties, the Gürsey isospin interpretation of the doubled solutions, the Poincaré-and-reversion legitimacy test, and the Einstein–Mayer equation with its proton–neutron, electron–neutrino, Petiau-wave and Higgs interpretations.
- A. Gsponer and J.-P. Hurni, "Lanczos's Equation to Replace Dirac's Equation?", *Proceedings of the Cornelius Lanczos International Centenary Conference* (SIAM, 1994) 509–512 (arXiv:hep-ph/0112317), the same authors' stronger and earlier claim, for the Lanczos quaternionic equation as a replacement for Dirac's, for spins $0,\tfrac12,1,\tfrac32$ in one framework, for quarks and leptons with electric and baryonic charge read from the equations (neutrino and u-quark masses zero by eigenvalue equations), for extended hadrons with a non-local strong interaction, and for an electroweak sector claimed identical to the Standard Model's with no Higgs mechanism. Recorded as a claim: four pages, no derivation exhibited, and the title is a question.
- C. Lanczos, "Die tensoranalytischen Beziehungen der Diracschen Gleichung", *Zeitschrift für Physik* **57** (1929) 447–473 and 474–483, for Lanczos's fundamental equation and the doubling it implies.
- F. Gürsey, *Il Nuovo Cimento* **7** (1958) 411–415, for the isospin interpretation of the doubling.
- A. Einstein and W. Mayer, "Semi-Vektoren und Spinoren," *Sitzungsberichte der Preussischen Akademie* (1932) 522–550, for the generalization in which the mass becomes a coefficient of the algebra. This is **not** the same paper as "Die Diracgleichung für Semivektoren," *Proceedings of the Royal Academy of Amsterdam* **36** (1933) 497–516, 615–619, which is the **Lagrangian formulation** the centenary contribution and the companion article *The Petiau System and the Quantisation of Mass in Biquaternionic Form* use; the two are distinct items of the same authors and a reader checking one against the other should keep them apart.
- [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html), for the doubling worked on the corpus's own carrier.
- [The Petiau System and the Quantisation of Mass in Biquaternionic Form](the-petiau-system-and-the-quantisation-of-mass-in-biquaternionic-form.html), for the derivatively coupled case and its double-periodic waves.
- [The Higgs Mechanism in Biquaternionic Form](the-higgs-mechanism-in-biquaternionic-form.html), for the sigma-model reading of $E$ and its limits.
- [The Standard Model as the Low-Energy Phase: The U(2) Ceiling and the Four Unbuilt Sectors](the-standard-model-in-the-biquaternion-framework-the-u2-ceiling-and-the-four-unbuilt-sectors.html), for the scalar sector marked *no route yet* alongside the paper route.
- [The Empirical Status of the Biquaternion Framework](the-empirical-status-of-the-biquaternion-framework.html), for the domain-by-domain agreement that makes the prior-art warning the corpus's default expectation.
- [Comparison of the Remarkable Subspaces](../articles_maths/comparison-of-the-remarkable-subspaces.html), for the conjugations and their fixed spaces.
- [The CPT Theorem in Biquaternionic Form](the-cpt-theorem-in-biquaternionic-form.html), for the discrete symmetries the legitimacy test requires.
