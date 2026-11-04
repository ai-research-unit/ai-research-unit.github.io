# __Chiral Fermions in the Biquaternion Framework__

## Introduction

A **chiral fermion** is a fermion whose left and right parts carry *inequivalent* representations of the gauge group. The **vector-like** alternative is a fermion whose two parts carry the same representation; a vector-like fermion may have a mass term that pairs the two parts, and a chiral fermion may not. The distinction is not a technicality: the matter content of the Standard Model is chiral, with the left-handed quarks and leptons in $SU(2)$ doublets and their right-handed partners in singlets, and the immediate kinematic consequence is that no bare fermion mass is gauge invariant. The electron mass appears only after electroweak symmetry breaking, through the coupling of the two parts to the Higgs field, whose vacuum expectation value carries the charge that the mass term lacks.

This article asks what the biquaternion framework, in the notation of the companion articles, supplies for that structure. The presentation is organized around one question — *can the framework distinguish the two parts in a gauge interaction?* — and the answer is split, at the outset, into the three categories the corpus uses.

- **Established, and recomputed below.** The state of a fermion is an element of $\mathbb{B}$, and its chirality is a subscript with two values. The two values are read from one cell, the chirality cell $\chi=-iR_{\vec e_z}^{\mathrm{axf}}$, which carries the $L$ part to minus itself and the $R$ part to plus itself. The mass bilinear of the corpus pairs one part of each value and vanishes on an element of one value. A *chiral* abelian gauge symmetry with independent charges $ϙ_L,ϙ_R$ is consistent: the action $Q\mapsto Qb$ by the charge element $b=\tfrac{ϙ_L+ϙ_R}{2}e_t-\tfrac{i}{2}(ϙ_R-ϙ_L)\vec e_z$ multiplies the two parts by the two charges, the covariant derivative is covariant for arbitrary charges, and the curvature is $\tfrac{i}{\hbar}F_{\mu\nu}Qb$. The mass bilinear is gauge invariant if and only if $ϙ_L=ϙ_R$: a chiral fermion cannot carry a bare Dirac mass.
- **Established from the read list, and sharpened here.** The gauge group of the biquaternionic abelian gauge principle is the $*$-unitary part of the centre $\mathbb{C}_{\mathbb{B}}$. A group drawn from the centre multiplies the two values alike, so it assigns them equal charges: it is vector-like and cannot be chiral. A chiral abelian group needs an element off the centre, and $b$ is that element whenever $ϙ_L\neqϙ_R$ — the structure whose algebraic status the gauge article leaves open.
- **Gap, left visible.** The algebra's real structure $\flat=-{}^{*}$ supplies the shape of a conjugate pairing with the quantum numbers of a Majorana-type mass, but the single-field equation built on it is not a physical mass: its central-phase plane waves sit on the spacelike locus (the companion *Antilinear Structure and the Two Kinds of Mass* shows this). The operation that exchanges the two values is the coefficient bar, and a physical Majorana pairing must be built on a conjugation of that kind. The parent's own mass term is the linear chiral pair, through which the continuous central phase passes and which conserves the vector $\mathrm{U}(1)$; it is not the antilinear pairing. Whether a given fermion uses the bar is the question of the companion *The Neutrino and Majorana Fermions in Biquaternionic Form*. It is recorded here only for its consequence: the framework's vector-like gauge structure and the real structure's antilinear pairing do not naturally meet.

The article is organized as follows. The next section fixes the two values of the subscript and what they cost. The section after that writes the chiral gauge symmetry on the element and derives the mass selection rule. A section then determines what the algebra's centre supplies, and why it is vector-like; a section treats the mass term and the algebra's real structure; a section records an external reading of the Majorana condition and the spacetime signature; and a section separates the two values from the material/informational sector split, and what the framework supplies from what it only transcribes. Open questions close the argument, and a last section writes out the matrix display of the five frame cells once, for comparison with the literature.

No statement of the body is written with an array. The argument is carried by elements, their products and one cell, and an array appears only where the array is the object.

## The Two Values of the Subscript

**The state is an element.** In this framework the state of a fermion is an element of $\mathbb{B}$, written $\psi$, and a general element is written $Q$. Every statement below is a statement about elements, their products, and one cell.

**The chirality is the subscript.** It takes two values, $L$ and $R$: $\psi_L$ and $\psi_R$ for a state, $Q_L$ and $Q_R$ for a general element. The letters are the Dirac ones. The value $L$ is the minus one and the value $R$ the plus one, as the corpus fixes them (*Matrix Representations Conventions*, §*The Subscript on an Element*); this article uses the convention and does not restate it.

**One cell carries the value.** The chirality cell is

$$
\chi=-iR_{\vec e_z}^{\mathrm{axf}},
\qquad
\chi\,Q=-i\,Q\,\vec e_z ,
$$

and it carries the $L$ part to $-Q_L$ and the $R$ part to $+Q_R$. No scalar is computed to read a value: the cell carries each part to a multiple of itself, and the sign of that multiple is the value. The two parts are of two complex dimensions each, every element is one part of each value, and only the zero element is both.

**The value is not a property of the massless limit.** The chirality cell commutes with each of the six Lorentz cells, so the value is Lorentz invariant with or without a mass; what the mass does is make the two parts visible to each other, and that is a statement about the equation and not about the invariance of the label. The warrant is one line: $\chi$ is a right multiplication by a unit, so it commutes with every left multiplication, and each of the six Lorentz cells is either a left multiplication or a left multiplication followed by $R_{\vec e_z}$, with which $\chi$ commutes because $\vec e_z$ commutes with itself.

**What the pair costs.** The cell names one unit, $\vec e_z$, because a cell is a multiplication by a unit. A right multiplication by another unit gives another cell and another pair of values, so the pair is a property of the declared frame and not a direction in space; the article uses the pair the corpus fixes, and no statement below needs a second one.

**The two conjugations and the two values.** The coefficient bar exchanges them: $\chi(\overline Q)=-\overline{\chi(Q)}$, so $\overline{Q_L}$ has the value $R$ and $\overline{Q_R}$ the value $L$. The warrant is the definition of $\chi$: the bar conjugates its $i$ and leaves its unit alone, so the two signs are opposite. The Hermitian conjugation preserves neither value: it fixes $e_t+i\vec e_z$, whose value is $L$, and it carries $\vec e_x-i\vec e_y$, whose value is $L$, into $-\vec e_x-i\vec e_y$, whose value is $R$. One conjugation exchanges the two values, the other mixes them, and the sections below use both facts.

## Chiral Gauge Symmetry on the Element

**The charge element.** A chiral abelian symmetry assigns two charges, $ϙ_L$ and $ϙ_R$. The element that carries them is

$$
b=\tfrac{ϙ_L+ϙ_R}{2}\,e_t-\tfrac{i}{2}(ϙ_R-ϙ_L)\,\vec e_z ,
$$

and the symmetry acts by the right multiplication

$$
Q\longmapsto Q\,e^{\frac{i}{\hbar}\Gamma b},
\qquad
Q_L\,e^{\frac{i}{\hbar}\Gamma b}=e^{\frac{i}{\hbar}ϙ_L\Gamma}\,Q_L,
\qquad
Q_R\,e^{\frac{i}{\hbar}\Gamma b}=e^{\frac{i}{\hbar}ϙ_R\Gamma}\,Q_R .
$$

The two identities are two lines. The value of a part fixes its multiplication by $\vec e_z$, $Q_L\vec e_z=-iQ_L$ and $Q_R\vec e_z=+iQ_R$, so the $\vec e_z$ term of $b$ acts with opposite signs on the two parts, and the exponential is the two phases. No matrix and no charge symbol is needed: the two charges enter through the two coefficients of one element.

**Vector-like is the central case.** The element $b$ is central if and only if its $\vec e_z$ coefficient vanishes, that is, if and only if $ϙ_L=ϙ_R$; the action is then a central phase and multiplies the two parts alike.

**The covariant derivative.** With the connection $A_\mu$ and the transformation

$$
D_\mu Q=\frac{\partial Q}{\partial Q_\mu}+\frac{i}{\hbar}A_\mu\,Q\,b,
\qquad
A_\mu\longmapsto A_\mu-\frac{\partial\Gamma}{\partial Q_\mu},
$$

one has $(D_\mu Q)'=(D_\mu Q)\,e^{\frac{i}{\hbar}\Gamma b}$ for arbitrary $ϙ_L,ϙ_R$. The warrant is that the derivative of the transformation is $\frac{i}{\hbar}\frac{\partial\Gamma}{\partial Q_\mu}b$ times the same factor, so the two terms that would spoil the covariance cancel against the shift of $A_\mu$.

**The curvature.** The element $b$ is constant, and left and right multiplications commute, so $b$ factors out on the right and the commutator acts on the scalar alone:

$$
[D_\mu,D_\nu]Q=\frac{i}{\hbar}F_{\mu\nu}\,Q\,b,
\qquad
F_{\mu\nu}=\frac{\partial A_\nu}{\partial Q_\mu}-\frac{\partial A_\mu}{\partial Q_\nu},
$$

an identity for arbitrary $ϙ_L,ϙ_R$.

**The side of the multiplication.** The charge element multiplies on the right, and the connection of the parent gauge principle multiplies on the left; the two coincide only in the central case, that is, only when $ϙ_L=ϙ_R$. A reader who compares the two forms compares them at equal charges.

**One connection per charge.** The curvature of this construction is the single two-form $F_{\mu\nu}$ of the parent gauge principle. The construction therefore supplies one abelian connection per independent charge and does not unify the two into a simple group: the algebra supplies the element $b$ and the two connections, not a group that contains both.

## What the Centre Supplies: A Vector-Like Abelian Sector

The gauge group of the biquaternionic abelian gauge principle is not chosen; it is the **$*$-unitary part of the centre** of the algebra (*The Gauge Principle in Biquaternionic Form*), the complex line $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_t,ie_t\}$ whose $*$-unitary part is a circle. The article takes that result as given and reads its consequence for the two values.

A central element multiplies the two values alike — it is one action and not two — so every group drawn from the centre assigns the two parts the same charge. Such a group cannot distinguish $\psi_L$ from $\psi_R$, and the abelian sector the framework supplies canonically is **vector-like**.

**The axial rotation is off the centre.** The chirality cell generates a rotation of its own: $\psi\mapsto e^{i\alpha\chi}\psi$, which is the right multiplication $\psi\mapsto\psi\,e^{\alpha\vec e_z}$ (*Anomalies and Anomaly Cancellation in Biquaternionic Form*, where the identity is used). It multiplies the $L$ part by $e^{-i\alpha}$ and the $R$ part by $e^{+i\alpha}$, so it is genuinely axial, and its generator $\vec e_z$ is not central: the group it generates is not a subgroup of the centre.

**The qualification.** The centre can act axially, but only with the two charges locked. A central phase $\lambda$ applied after the bar multiplies $\bar Q$ by $\bar\lambda$, and the bar exchanges the two values, so the two parts receive opposite phases: the ratio $ϙ_R=-ϙ_L$, and no other. Independent charges need the element $b$ off the centre. The implication is what the article uses: the centre can act axially, but never with independent charges, so a non-central element is the prerequisite for a general chiral gauge sector. There the gap of the gauge article is that the Lie algebra of $\mathbb{B}$ read as an associative algebra is $\mathfrak{gl}(2,\mathbb{C})$, whose traceless part is not compact, so that a reality and tracelessness condition must select a compact gauge algebra before a Yang–Mills structure can be claimed. The present article inherits that gap and sharpens its meaning: without those conditions the framework has no chiral gauge group at all, because the only gauge group it supplies canonically is the scalar centre.

## The Mass Term and the Real Structure

The biquaternion Dirac equation of the parent is a pair of one-sided equations,

$$
\tilde{\nabla}\tilde{\Psi}_R=m\,\tilde{\Psi}_L,
\qquad
\tilde{\nabla}^{\natural}\tilde{\Psi}_L=m\,\tilde{\Psi}_R .
$$

The first is the equation of the $R$ part and the second of the $L$ part. They are the two lines of one chiral pair, not two independent dynamics: eliminating one part gives the massive Klein–Gordon equation, and in the massless case the lines decouple into $\tilde{\nabla}\tilde{\Psi}_R=0$ and $\tilde{\nabla}^{\natural}\tilde{\Psi}_L=0$. The pair is complete as written, both lines acting from the left, and $\natural$ is the conjugation that separates them (*Operator and Calculus Conventions*, §*The Two Sides and the Renaming Theorem*).

The mass term is **linear** in the field and it **pairs the two values**, one part of each. The same equation, read on the whole algebra, has the two-sided form

$$
\tilde{\nabla}^{\natural}F=m\,\chi(\bar F)=-im\,\bar F\,\vec e_z ,
$$

in which the derivative acts from the left and the mass from the right through the chirality cell, the conjugation supplying the antilinear part (Kravchenko's dictionary; the companion *The Dirac Equation in Biquaternionic Form*). The pair is linear in the field and the two-sided equation is antilinear in its mass term, so they are different operators, and the pair is the definition.

**The bilinear.** The mass bilinear of the corpus is the Dirac bilinear $\psi^{\dagger}iR_{\vec e_x}^{\mathrm{axf}}\psi$. The cell in it is the timelike frame cell, which anticommutes with $\chi$: it carries each part into the other, so the bilinear pairs the $L$ part with the $R$ part and never a part with itself. Two consequences are one line each. Under the discrete transformation $\psi\mapsto\chi\psi$ the bilinear changes sign, so it is odd in the value; and on an element of one value it vanishes, because the second value is absent. A single-valued element has no Dirac mass bilinear at all, which is the precise sense in which a lone Weyl field cannot carry a **Dirac** mass. It is not a statement that such a field is massless: a Majorana mass pairs the field with its own conjugate and needs no second value.

**The vector phase and the axial rotation.** Both parts carry the phase $\lambda$ under the central phase $Q\mapsto\lambda Q$, and the phases $e^{-i\alpha}$ and $e^{+i\alpha}$ under the axial rotation $Q\mapsto Qe^{\alpha\vec e_z}$. The bilinear pairs one part with the other, so the two phases enter it as a product: the amplitude the mass term is built from carries the phase $e^{2i\alpha}$, and the term is invariant exactly when $e^{2i\alpha}=1$, that is for $\alpha\in\pi\mathbb{Z}$, the sign $\psi\mapsto-\psi$. The mass term therefore conserves the vector $\mathrm{U}(1)$ and breaks the axial one; at a quarter turn it is carried into its axial partner, and the axial current has a divergence proportional to the mass bilinear and vanishes only at $m=0$. The companion *Anomalies and Anomaly Cancellation in Biquaternionic Form* builds the axial density from $\chi$; the vector current is conserved at every $m$.

**The real structure.** The algebra's antilinear involution is the real structure $\tilde{\Psi}^{\flat}=-\tilde{\Psi}^{*}$. It pairs an element with its conjugate, it is $\mathbb{C}$-antilinear and order-reversing with a sign, its fixed space is $\mathbb{M}_-$, and a central scalar multiplies it by the conjugate, $(\lambda F)^{\flat}=\bar\lambda F^{\flat}$. Its single-field equation $\tilde{\nabla}\tilde{\Psi}=m\tilde{\Psi}^{\flat}$ is therefore not invariant under the continuous central phase, and its plane waves are spacelike, so it is retired as a physical mass (the companion *Antilinear Structure and the Two Kinds of Mass*). It neither preserves nor exchanges the two values — it mixes them, as the star does — and it preserves the sector split, so the operation that exchanges the values is the bar and not $\flat$. That is the precise difference between a Majorana-type pairing and an ordinary Dirac mass.

**The price of the antilinear mass term.** Under $F\mapsto\lambda F$ the derivative term is multiplied by $\lambda$ and the conjugated term by $\bar\lambda$, so the two-sided equation holds for every field only for real $\lambda$. The two-sided form is thus the place where the continuous central phase is broken to a sign, and the one-sided pair, which is linear, is the place where it is conserved.

## An External Reading of the Majorana Condition and the Spacetime Signature

An external source reaches this article's own question — which mass terms the algebra allows, and on which signature — from a direction that shares none of the corpus's conventions, and it is worth recording because it exhibits the signature-dependence independently. D. J. Cirilo-Lombardo (*Algebraic structures, physics and geometry from a Unified Field Theoretical framework*, arXiv:1411.5493v3 [hep-th], 2015) performs Majorana's 1937 transformation on the structural group of his own unified field theory, and states his aim in the terms this article uses: to obtain a transformation for which the Dirac equation becomes real-coefficient and symmetric "for both: fermions and antifermions."

**The algebraic core is one sign flip.** The input of that construction is a triple with one square flipped. In the framework's language the three elements $i\vec e_x$, $\vec e_y$ and $i\vec e_z$ have the squares $+e_t$, $-e_t$ and $+e_t$, and they close on one another up to signs, $(i\vec e_x)\vec e_y=i\vec e_z$, $\vec e_y(i\vec e_z)=i\vec e_x$ and $(i\vec e_z)(i\vec e_x)=-\vec e_y$; that is the split form of the three-dimensional triple, and it is what the source's transformation uses. The move is a change of the sign of one unit in the norm condition, from $a_0^2+a_1^2+a_2^2+a_3^2=1$ to $a_0^2+a_1^2-a_2^2+a_3^2=1$, and it is a structural choice and not a consequence of the algebra. What the source derives from it — that the transformed group is real and symmetric, hence that a Majorana condition is available — is recorded as the source's result and not re-derived here.

**What was verified, and what was not.** Three printed slips are recorded with it, and all three concern the source's own displays rather than the transformation: the source's set of four is not a quaternionic set until a sign is restored, the time-like member being opposite to the scalar one; one entry of the printed transformed group carries the wrong sign in one of its combinations; and the sentence that the transformed group and its transpose multiply to the identity does not reproduce — the identity that holds is the quaternionic one *before* the transformation. The full record is in *The Biquaternion Basis of a Unified-Field Fibre Bundle*.

**The signature dependence, and what it does not add.** The source asserts that the availability of a Majorana representation is tied to the spacetime signature, and here the corpus has already said more: in *Real Spinors and Reality Conditions on the Biquaternion Algebra with Hermitian Adjoint* the reality type of the spinor representation is a function of the signature modulo eight, and the four-dimensional carrier does carry a real structure in this signature. That classification is what this article's third open question reflects: a Majorana-type coupling must be built on an antilinear structure of the carrier, and cannot be manufactured inside one value. The source states the dependence and gives no table; the corpus's table is the contribution, and the source's Section V is an external worked instance of it.

**The non-Hermitian claim, kept apart.** The source also reports **non-Hermitian** dynamic operators as a structural feature. The corpus's translation separates two things: the source's own structural object is Hermitian — it is an element of $\mathbb{M}_+$ — and the non-Hermiticity the paper flags belongs to the *generalized momentum* of its second sector, where the paper itself notes that $E^2+H^2$ can be negative. So the claim does not put a non-Hermitian generator into the chirality structure this article uses; the Born weight here is still the Hermitian form of a Hermitian element, read through the trace, and the assertion is recorded as one about that other sector rather than about the algebra. Its algebraic engine is the same one-sign flip of the triple, and it is the same move that separates the algebra's real structure $\flat$ from its compact conjugations.

Nothing here changes this article's findings or its open questions. The source is recorded as an independent instance of the same signature-dependent classification, not as support for any interpretation of the framework.

## Chirality Is Not the Sector Split

Two decompositions of the framework are in play in this article and its parents, and they must not be conflated.

- The **value decomposition** is the split of an element by the chirality cell into its $L$ and $R$ parts, one of two complex dimensions each. It is the subject of this article.
- The **sector decomposition** is the split of the algebra by the Hermitian conjugation into the anti-Hermitian $\mathbb{M}_-$ and the Hermitian $\mathbb{M}_+$.

Neither decomposition contains the other, and each direction has a one-line witness.

The sector decomposition does not refine the value decomposition: $e_t+i\vec e_z$ is fixed by the star — it is Hermitian — and its value is $L$, so an element of one sector is not a sum of parts of one sector. The value decomposition does not refine the sector decomposition either: the star carries $\vec e_x-i\vec e_y$, whose value is $L$, into $-\vec e_x-i\vec e_y$, whose value is $R$, so the star does not act within the two values.

A statement about the two values is therefore not a statement about the sectors, and the temptation to read the material/informational split as a chirality is without algebraic support. This is the electron article's two findings, "chirality is not the same as the sector split" and "the two decompositions share no part", in the form the subscript gives them, and this article inherits them unchanged.

## What the Framework Supplies, Transcribes, and Does Not Supply

**What it supplies.**

- *The two-valued structure and its invariance.* Every element carries the subscript; the value is Lorentz invariant with or without a mass; the bar exchanges the two values and the star does not preserve them.
- *The oddness of the mass.* The Dirac bilinear is odd in the value and vanishes on an element of one value; the parent's mass term is the linear chiral pair, the operation that exchanges the values is the bar, and $\flat$ neither preserves nor exchanges them. This is established.
- *The chiral gauge covariant derivative on the element.* For independent charges $ϙ_L,ϙ_R$ the action $Q\mapsto Qe^{\frac{i}{\hbar}\Gamma b}$ and the derivative $D_\mu Q=\partial Q/\partial Q_\mu+\tfrac{i}{\hbar}A_\mu Qb$ are covariant, with curvature $\tfrac{i}{\hbar}F_{\mu\nu}Qb$. The charge element multiplies on the right, so the parent's left-multiplied form is recovered only in the vector-like case.
- *The mass selection rule.* A bare Dirac mass is gauge invariant if and only if $ϙ_L=ϙ_R$; a chiral fermion is massless in the unbroken phase. This is established by direct computation and is the algebraic content of the Standard Model's need for a Higgs field.
- *The vector-like character of the centre.* The only canonically available abelian gauge group is the scalar centre, which cannot be chiral.

**What it only transcribes.**

- *The global-to-local gauge argument itself.* The localization of a phase and the appearance of a connection are the read-list gauge principle's; the chiral variation above is that argument run with the charge element $b$ instead of a scalar charge $ϙ$.
- *The Higgs requirement.* That a chiral fermion needs a compensating scalar field is read off the selection rule; the mechanism by which the scalar acquires its expectation value is the subject of the companion *The Higgs Mechanism in Biquaternionic Form*, for the abelian case. The Yukawa coupling that would convert the vacuum value into a fermion mass is not constructed there either, so the fermion mass itself is not supplied.
- *The Weyl/Dirac split.* The two-component equations of the massless limit, and the helicity–chirality locking, are worked in the exercise articles of the read list; this article uses them and does not re-derive them.

**What it does not supply.**

- *A chiral gauge group.* The centre is scalar and vector-like; a non-central gauge structure, and with it the reality and compactness conditions that would select a compact gauge algebra, are not derived. This is the principal gap.
- *The value of the charges.* $ϙ_L$ and $ϙ_R$ are parameters, exactly as $ϙ$ is in the abelian gauge principle; the algebra does not fix them.
- *The resolution of the real structure's pairing.* The parent's mass term is the linear chiral pair and conserves fermion number. The algebra's $\flat$ supplies the shape of a conjugate pairing of Majorana type, but its single-field equation is not a physical mass; whether a given fermion uses the bar is open, and is the pivot on which the framework's chiral sector turns.
- *Anomaly cancellation for a chiral spectrum.* The framework's own gauge structure is anomaly-free, and not by a nontrivial cancellation: it is vector-like, so the left and right spectra coincide and the triangle coefficients vanish identically. The axial density itself is computed from the chirality cell in the companion *Anomalies and Anomaly Cancellation in Biquaternionic Form*. What is not supplied here is a cancellation condition for a chiral non-central group, since no such group is supplied.
- *Empirical contact.* As everywhere in the framework, no prediction distinguishing it from the standard chiral gauge theory is offered.

## Open Questions

1. **Can the framework host a chiral gauge group?** The centre supplies only a scalar, vector-like abelian group. The two values need a non-central action, hence a gauge group beyond the scalar centre; the read-list gauge article's reality and tracelessness conditions are the prerequisite, and whether they admit a compact simple algebra inside the biquaternion algebra is not settled.

2. **Which interpretation of the phase is physical?** A central phase multiplies the two values alike; applied after the bar it multiplies them with opposite signs. Whether the physical field is read as it stands or through the bar decides between the vector-like and the axial reading, and this article does not decide it.

3. **What is the physical status of the real structure's pairing?** The parent's mass term is the linear chiral pair, through which the continuous central phase passes, so the framework's fermion number is conserved by it. The algebra's $\flat=-{}^{*}$ gives the shape of a conjugate pairing of Majorana type, but the single-field equation $\tilde{\nabla}\tilde{\Psi}=m\tilde{\Psi}^{\flat}$ has spacelike plane waves and is retired as a physical mass (the companion *Antilinear Structure and the Two Kinds of Mass*). A physical Majorana mass must be carried by an antilinear conjugation that exchanges the two values, which in this article's language is the coefficient bar; whether a given fermion — the neutrino in particular — uses it is the companion's question.

4. **Where does the Higgs field enter?** The selection rule identifies the quantum numbers a compensating scalar must carry, and the companion *The Higgs Mechanism in Biquaternionic Form* carries out the abelian mechanism: the central scalar, its circle of minima, and the gauge-boson mass from the scalar kinetic term. The Yukawa coupling of that scalar to the two parts — the step that would give the fermion its mass — is not constructed there, and is the open end of this question.

5. **Anomalies.** The companion *Anomalies and Anomaly Cancellation in Biquaternionic Form* computes the axial density from the chirality cell and states the cancellation as a condition on the spectrum, and it shows that the framework's own gauge structure passes the test identically because it is vector-like. What remains open is the conditional: if a non-central chiral gauge group is ever supplied (question 1), whether the algebra's representation theory would make any of the cancellation conditions automatic.

6. **The two decompositions.** The value decomposition and the sector decomposition are genuinely different splits of one algebra, and each witnesses the other's independence. The group acting on the elements and the algebra's own structure are both built from $\mathbb{B}$: is there a deeper relation, or are they independent structures that happen to coexist in one algebra?

7. **Which value is left.** The coefficient bar exchanges the two values, and it commutes with the axial rotation, so the two names enter the algebra symmetrically; the naming of $L$ as the minus value is the corpus's convention. Whether a physical process fixes the naming independently of that convention is not decided here.

8. **Empirical contact.** Does any of the chiral structure above yield a prediction distinguishing the framework from standard chiral gauge theory? As always, this is the central unresolved question.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The bracket is the frame, on the generators as on the metric, $\gamma_\mu[\mathbb{M}_-]$ or $\gamma_\mu[\mathbb{B}]$, so that a glyph names a display and not an object of the algebra.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})\cong M_4(\mathbb{C})$, not a different algebra. In cell notation,

$$
\gamma_0[\mathbb{M}_-]=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\qquad
\gamma_1[\mathbb{M}_-]=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},
$$

The same in the axis-free display:

$$
\gamma_0[\mathbb{M}_-]=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\qquad
\gamma_1[\mathbb{M}_-]=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},
$$

$$
\gamma_2[\mathbb{M}_-]=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\qquad
\gamma_3[\mathbb{M}_-]=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\qquad
\gamma_5=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}=\chi .
$$

In the axis-free display:

$$
\gamma_2[\mathbb{M}_-]=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad
\gamma_3[\mathbb{M}_-]=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad
\gamma_5=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}=\chi .
$$

A single cell $L_aR_b$ is a pure tensor of $\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}$, of tensor rank one; as an operator on $\Delta$ its rank is four whenever $a$ and $b$ are invertible, so the two ranks must not be confused. The pure cells form the seven-dimensional cone of rank at most one, and a general element is a sum of at most four of them. Two cells multiply by $L_aR_b\,L_cR_d=L_{ac}R_{db}$, the right factors in reverse order, and the products of the four frame cells $\gamma_0[\mathbb{M}_-],\dots,\gamma_3[\mathbb{M}_-]$ give the usual sixteen-element Clifford basis. Every sign among them comes from $i^2=-1$ together with $\vec e_k^2=-e_t$: for instance $\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]=i^2L_{e_t\vec e_x}^{\mathrm{pau}}R_{\vec e_y\vec e_x}^{\mathrm{pau}}=-L_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y\vec e_x}^{\mathrm{pau}}$, and the same four steps give $\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]=-i\chi$, that is $\gamma_5=i\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]$.

$\gamma_5$ is the reference-frame representative of the chirality operator. The abstract central grading $\chi_{\mathrm{ad}}=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, with $\chi_{\mathrm{ad}}^2=e_t$ — is a different object; on the Dirac module it is represented by the frame cell $\gamma_5=\chi$. The distinction is the one between the abstract central sign and its representative.

The cell dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The identities the bodies cite.** In the $\gamma$ reading, with $\varepsilon=(1,-1,-1,-1)$ the sign vector of the cells,
$$
\{\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,\qquad
(\gamma_k[\mathbb{M}_-])^2=-I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu[\mathbb{M}_-],\gamma_5\}=0,
$$
$$
[\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]]=2\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\quad(\mu\ne\nu),\qquad
[\gamma_a[\mathbb{M}_-],S_{cd}]=\varepsilon_a\delta_{ac}\gamma_d[\mathbb{M}_-]-\varepsilon_a\delta_{ad}\gamma_c[\mathbb{M}_-],\qquad
S_{cd}=\tfrac14[\gamma_c[\mathbb{M}_-],\gamma_d[\mathbb{M}_-]],
$$
$$
\mathrm{tr}(\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-])=4\varepsilon_\mu\delta_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\gamma_\rho[\mathbb{M}_-]\gamma_\sigma[\mathbb{M}_-])=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$
$$
\mathrm{tr}(\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\gamma_\rho[\mathbb{M}_-]\gamma_\sigma[\mathbb{M}_-])
=4\bigl(\varepsilon_\mu\delta_{\mu\nu}\varepsilon_\rho\delta_{\rho\sigma}
-\varepsilon_\mu\delta_{\mu\rho}\varepsilon_\nu\delta_{\nu\sigma}
+\varepsilon_\mu\delta_{\mu\sigma}\varepsilon_\nu\delta_{\nu\rho}\bigr).
$$
The contraction sums follow from the squares. With one index raised, $\gamma^\mu[\mathbb{M}_-]=-\varepsilon_\mu\gamma_\mu[\mathbb{M}_-]$, so that $\sum_\mu\gamma^\mu[\mathbb{B}]\gamma_\mu[\mathbb{B}]=-4I_4$, $\sum_\mu\gamma^\mu[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=2\gamma_\alpha[\mathbb{M}_-]$, $\sum_\mu\gamma^\mu[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=-4\varepsilon_\alpha\delta_{\alpha\beta}I_4$ and $\sum_\mu\gamma^\mu[\mathbb{M}_-]\gamma_\gamma[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=2\gamma_\gamma[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]$.

## Summary

A chiral fermion is one whose two parts carry inequivalent gauge representations. In the biquaternion framework the two parts are read from one cell and named by one subscript. The state is an element of $\mathbb{B}$; the subscript takes the values $L$ and $R$, $L$ being the minus value and $R$ the plus one; and the cell is the chirality cell $\chi=-iR_{\vec e_z}^{\mathrm{axf}}$, acting $\chi Q=-iQ\vec e_z$ and carrying $Q_L$ to $-Q_L$ and $Q_R$ to $+Q_R$. Every element is one part of each value and only zero is both; the value is Lorentz invariant with or without a mass, because $\chi$ commutes with the six Lorentz cells; the coefficient bar exchanges the two values, and the Hermitian conjugation preserves neither of them.

The Dirac mass bilinear pairs one part of each value, because the timelike frame cell it carries anticommutes with $\chi$; it changes sign under $\psi\mapsto\chi\psi$ and vanishes on an element of one value. The gauge phases enter it as a product, so the mass term is invariant under the central phase and, under the axial rotation, only for $\alpha\in\pi\mathbb{Z}$: it conserves the vector $\mathrm{U}(1)$ and breaks the axial one.

A chiral abelian gauge symmetry with independent charges is consistent. The charge element $b=\tfrac{ϙ_L+ϙ_R}{2}e_t-\tfrac{i}{2}(ϙ_R-ϙ_L)\vec e_z$ multiplies the two parts by the two charges; the action $Q\mapsto Qe^{\frac{i}{\hbar}\Gamma b}$ and the covariant derivative $D_\mu Q=\partial Q/\partial Q_\mu+\tfrac{i}{\hbar}A_\mu Qb$ satisfy $(D_\mu Q)'=(D_\mu Q)e^{\frac{i}{\hbar}\Gamma b}$ for arbitrary charges, with curvature $[D_\mu,D_\nu]Q=\tfrac{i}{\hbar}F_{\mu\nu}Qb$. The element $b$ is central only when $ϙ_L=ϙ_R$, and then the action coincides with the parent's left multiplication. That is also the condition for the mass bilinear to be gauge invariant, and the two occurrences of it — one for the mass, one for the side of the connection — are one statement seen twice.

The framework's own abelian gauge group is the $*$-unitary part of the centre, and a central element multiplies the two parts alike. The canonically available abelian sector is therefore **vector-like** and cannot be chiral; a chiral gauge group needs the element off the centre. The axial rotation $e^{\alpha\vec e_z}$ is such an element, but it is not central, and the centre can act axially only with the charges locked in the ratio $ϙ_R=-ϙ_L$.

Two gaps are left visible. Without a non-central gauge structure the framework has no chiral gauge group. And the algebra's $\flat$ supplies the shape of a conjugate pairing, but its single-field equation is spacelike and not a physical mass; whether a given fermion uses the bar is open. The chiral structure itself — the two values, the oddness of the mass, the selection rule — is established and exact.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t=1,\ \vec e_x,\ \vec e_y,\ \vec e_z$ | Quaternion basis, $\vec e_k^2=-e_t$, $\vec e_x\vec e_y=\vec e_z$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_+,\ \mathbb{M}_-$ | Informational (Hermitian) and material (anti-Hermitian) sectors |
| $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_t,ie_t\}$ | The centre of the algebra; its $*$-unitary part is the abelian gauge group |
| $\psi,\ Q$ | The state, an element of $\mathbb{B}$, and a general element |
| $Q_L,\ Q_R$; $\psi_L,\ \psi_R$ | The two values of the chirality subscript; $L$ is the minus value |
| $\chi=-iR_{\vec e_z}^{\mathrm{axf}}$ | Chirality cell, $\chi Q=-iQ\vec e_z$, $\chi^2=I$; a right multiplier, so Lorentz invariant; not central |
| $\bar Q$ | Coefficient conjugation; exchanges the two values |
| $\psi^{\dagger}iR_{\vec e_x}^{\mathrm{axf}}\psi$ | Dirac mass bilinear; pairs one part of each value; odd in the value |
| $\natural$ | Quaternion conjugation; the conjugation that separates the two lines of the pair |
| $\tilde{\nabla},\ \tilde{\nabla}^{\natural}$ | Biquaternionic gradient and its quaternion conjugate |
| $ϙ_L,\ ϙ_R$ | The two charges (parameters) |
| $b=\tfrac{ϙ_L+ϙ_R}{2}e_t-\tfrac{i}{2}(ϙ_R-ϙ_L)\vec e_z$ | Charge element; central if and only if $ϙ_L=ϙ_R$ |
| $Q\mapsto Qe^{\frac{i}{\hbar}\Gamma b}$ | Chiral gauge transformation, a right multiplication |
| $D_\mu Q=\partial Q/\partial Q_\mu+\tfrac{i}{\hbar}A_\mu Qb$ | Chiral covariant derivative |
| $A_\mu\mapsto A_\mu-\partial\Gamma/\partial Q_\mu$ | Transformation of the abelian connection |
| $F_{\mu\nu}=\partial A_\nu/\partial Q_\mu-\partial A_\mu/\partial Q_\nu$ | Abelian curvature |
| $[D_\mu,D_\nu]Q=\tfrac{i}{\hbar}F_{\mu\nu}Qb$ | Chiral curvature identity |
| $e^{\alpha\vec e_z}$ | Axial rotation; $L\mapsto e^{-i\alpha}$, $R\mapsto e^{+i\alpha}$ |
| $\tilde{\Psi}^{\flat}=-\tilde{\Psi}^{*}$ | Anti-Hermitian conjugation; the algebra's real structure, which preserves $\mathbb{M}_\pm$ and mixes the two values |
| $iR_{\vec e_x}^{\mathrm{axf}}$ | Timelike frame cell; anticommutes with $\chi$, so it carries each value into the other |
## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the two-component spinor calculus, the Weyl spinors, and the chiral decomposition of the Dirac field.
- Steven Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the construction of the Dirac spinor from two Weyl spinors, the chiral gauge interactions, and the Standard Model's need for a Higgs field to give mass to chiral fermions.
- Michael E. Peskin and Daniel V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the $V-A$ structure, the mass selection rule, and the electroweak chiral assignments.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the Clifford-algebra construction of spinors from idempotents and the chirality operator.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor formulation of the Lorentz group and the relation between spinors and four-vectors.
- Walter Greiner and Berndt Müller, *Gauge Theory of Weak Interactions* (Springer, 2000), for the chiral structure of the electroweak theory and the generation of fermion masses.
- D. J. Cirilo-Lombardo, "Algebraic structures, physics and geometry from a Unified Field Theoretical framework," arXiv:1411.5493v3 [hep-th] (2015), for the external interpretation recorded in *An External Reading of the Majorana Condition and the Spacetime Signature*: Majorana's 1937 transformation applied to a structural group, the verified real-symmetric result, the assertion that a Majorana representation is tied to the signature, and the non-Hermitian operators of the source's separate $(2{+}2)$ sector. Cited for the independent instance of the signature-dependent classification, with the source's printed slips noted and its programme not endorsed.
- Companion articles: [The Spinor Module in Biquaternionic Form and Its Lorentz Action](the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.html); [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html); [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html); [Anomalies and Anomaly Cancellation in Biquaternionic Form](anomalies-and-anomaly-cancellation-in-biquaternionic-form.html); [Exercise: Chirality and the Weyl Spinors](exercise-chirality-and-the-weyl-spinors.html); [Exercise: Plane-Wave Solutions of the Biquaternion Dirac Equation](exercise-plane-wave-solutions-of-the-biquaternion-dirac-equation.html); [The Electron in Biquaternionic Form](the-electron-in-biquaternionic-form.html); [The Lorentz Group in Biquaternionic Form — Structure and Representations](the-lorentz-group-in-biquaternionic-form-structure-and-representations.html); [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html); [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html); [Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form](antilinear-structure-and-the-two-kinds-of-mass-in-biquaternionic-form.html); [The Neutrino and Majorana Fermions in Biquaternionic Form](the-neutrino-and-majorana-fermions-in-biquaternionic-form.html); [The Higgs Mechanism in Biquaternionic Form](the-higgs-mechanism-in-biquaternionic-form.html); [The Biquaternion Basis of a Unified-Field Fibre Bundle](the-biquaternion-basis-of-a-unified-field-fibre-bundle.html).
