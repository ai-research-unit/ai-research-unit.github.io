
# __Holography under the Biquaternion Framework — A Speculative Note__

## Introduction

**This is a speculative note.** Its genre is the proposal of an identification that is not derived; that licence is the point of it. Its discipline is a different and stricter matter: a reader must be able to see, in the sentence where it is made, which statements are proposals and which are established.

The note therefore fixes one convention at the start and keeps to it throughout. Any claim that is proposed and not derived begins with the marker **Proposal —**. A sentence not so marked is one of three things: established physics, an established algebraic fact about $\mathbb{B}$, or an explicit open question. Where a proposal is followed immediately by the obstruction that limits it, the obstruction is stated plainly and without the marker.

The question is whether the framework's split of the biquaternion algebra into a material sector $\mathbb{M}_-$ and an informational sector $\mathbb{M}_+$ — complementary subspaces exchanged by multiplication by the scalar imaginary, $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ with $i\mathbb{M}_\pm=\mathbb{M}_\mp$ — can be read as a **holographic correspondence**: one sector living on, or encoding, the other.

Three features of the corpus make the question worth asking, and they organize everything that follows.

1. **A boundary and entropy story.** The black-hole-thermodynamics article associates a horizon with an entropy proportional to its area, $S=k_B A/(4\ell_P^2)=A/4$ in Planck units; the Hawking article fixes the temperature by the period of the horizon flow, and reads the horizon-generating flow as the modular flow, whose Hamiltonian $K=-\log\rho$ is a Hermitian element of $\mathbb{M}_+$.
2. **An area-scaling law.** The entropy is the horizon **area**, not its volume: $S\propto A$, a codimension-two scaling.
3. **A KMS condition.** The KMS article states $F_{\tilde A\tilde B}(t+i\beta)=F_{\tilde B\tilde A}(-t)$ for operators in the algebra, ties the imaginary-time strip to the intrinsic imaginary time $ict$ of $\mathbb{M}_-$, and locates the modular generator in $\mathbb{M}_+$; the Bisognano–Wichmann article identifies the wedge modular flow with the boost.

**Proposal —** the reading to be examined is that $\mathbb{M}_-$ is the "bulk" sector and $\mathbb{M}_+$ the "boundary" sector, so that the geometric and thermodynamic data of the material sector are encoded in the informational sector. This identification is proposed and not derived; no equation in the corpus yields it.

The note then does two things. It states what a holographic correspondence would actually require — a bulk gravitational background, a lower-dimensional boundary theory, and a dictionary — and records the framework's status on each requirement. And it argues, using the framework's own algebra, that the three features above do less than they appear to do: area scaling is a hint and not a correspondence, a KMS condition is satisfied by any thermal system and is not a duality, and the name "informational" — which the parent article attaches as a hypothesis, not a result — cannot do evidential work.

The conclusion is stated here, so that the reader can hold it while reading: **on the present state of the framework, the $\mathbb{M}_-/\mathbb{M}_+$ split is a suggestive collision of names and structures with holography, not a holographic correspondence.** That is a legitimate and useful result. It tells the reader what would have to be built for the reading to become a correspondence, and it keeps the framework from borrowing the authority of AdS/CFT for a structure that does not have AdS/CFT's ingredients. If the conclusion were the opposite it would carry the **Proposal —** marker, because the note has no derivation of it either way.

**Conventions.** Those of the read list, inherited unchanged. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}\cong M_2(\mathbb{C})$; the quaternion basis is $e_0=1,e_1,e_2,e_3$ with $e_k^2=-e_0$; the scalar imaginary is $i$, $i^2=-1$, commuting with every $e_k$. The material (anti-Hermitian) subspace is $\mathbb{M}_-$ and the informational (Hermitian) subspace is $\mathbb{M}_+$, with $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ and $i\mathbb{M}_\pm=\mathbb{M}_\mp$; $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace and $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ the complex scalars. The material coordinate is $\tilde X=ict\,e_0+x\,e_1+y\,e_2+z\,e_3$, with norm form $N(\tilde X)=\tilde X\bar{\tilde X}$, and the trace formula is $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$. Nothing in this list is renamed or rederived. The KMS condition is the parent's, $F_{\tilde A\tilde B}(t+i\beta)=F_{\tilde B\tilde A}(-t)$ with the strip $0<\mathrm{Im}\,t<\beta$, and the modular Hamiltonian $K=-\log\rho$ is the parent's Hermitian element of $\mathbb{M}_+$. The entropy and area statements are those of the Hawking and black-hole-thermodynamics articles, imported there and re-imported here; none is derived in this note. Throughout, $G$ is Newton's constant and $\ell_P^2=\hbar G/c^3$ the Planck area. The AdS/CFT template below is used as a **yardstick for the requirements**, not as a source of claims about the framework.

## What a Holographic Correspondence Would Require

A holographic correspondence, in the canonical sense of the anti-de Sitter/conformal-field-theory (AdS/CFT) correspondence of Maldacena and Witten, is a specific package of four items. They are worth naming separately, because the framework has to be checked against each.

**1. A bulk theory of gravity on a fixed background.** The bulk is a $(d+1)$-dimensional spacetime, asymptotically anti-de Sitter, so that the cosmological constant is negative and the spacetime has a timelike **conformal boundary** at infinity. The gravitational field is dynamical in the bulk, with a semiclassical limit.

**2. A boundary theory.** On that conformal boundary lives a $d$-dimensional conformal field theory — a genuine local quantum field theory, with infinitely many degrees of freedom, its own algebra of local operators, and a Hilbert space of states.

**3. A dictionary.** There is a map between the two descriptions: a bulk field corresponds to a boundary operator, and boundary correlation functions are computed by the on-shell bulk action with prescribed boundary data. The dictionary is what makes the correspondence a correspondence rather than a resemblance.

**4. A regime in which the bulk is classical and the boundary is strongly coupled.** In the large-$N$ limit the bulk becomes semiclassical, and the leading entropy of a boundary region is geometric: the Ryu–Takayanagi formula gives the entanglement entropy of a boundary region as the area of the minimal bulk surface homologous to it, divided by $4G_N$.

The four items are a package. Any one of them alone is not holography, and the presence of an area-scaling entropy is a *consequence* of the package in this setting rather than a criterion for it. Two cautions belong here, because they are the standard errors. First, holography is not defined by an entropy's scaling with area; a theory whose entropy happens to scale that way is not thereby holographic. Second, the correspondence is not a general claim about information; it is a duality between two specific descriptions, and it stands or falls with the dictionary.

That is the yardstick, and it is used in this note only to ask what the framework would need. **No result of AdS/CFT is imported as evidence for anything about the framework.** The correspondence is invoked to say what is missing, not to supply what is missing.

## What the Framework Actually Has

The algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, of real dimension eight, split as $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$; $\mathbb{M}_+$ is the Hermitian subspace, $\mathbb{M}_-$ the anti-Hermitian one, and multiplication by $i$ exchanges them. In the matrix representation ($e_0\mapsto I$, $e_k\mapsto-i\sigma_k$, $i\mapsto iI$) both subspaces have **real dimension four** (recomputed from the bases $\{ie_0,e_1,e_2,e_3\}$ and $\{e_0,ie_1,ie_2,ie_3\}$), so the split is a split of one eight-dimensional algebra into two halves of equal dimension.

The material sector carries the coordinate $\tilde X=ict\,e_0+x\,e_1+y\,e_2+z\,e_3$, whose norm form is $N(\tilde X)=-c^2t^2+x^2+y^2+z^2$, with the zero-divisor cone $N=0$ as the light cone. The informational sector carries the Hermitian elements, among them the modular Hamiltonian $K=-\log\rho$ and the wedge boost generator $G_1=ie_1$ with $K_W=2\pi G_1$. The trace formula $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$ is inherited. The algebraic relation between the sectors is that $\mathbb{M}_+$ acts on $\mathbb{M}_-$ by rotor conjugation, $\tilde X\mapsto\tilde\Lambda\tilde X\tilde\Lambda^\dagger$ — the structure of operators acting on states.

Now the three items that motivate the holographic reading.

**The boundary and entropy story.** A horizon has a temperature $T=\hbar\kappa/(2\pi c k_B)$ and an entropy $S=k_Bc^3A/(4G\hbar)=k_B A/(4\ell_P^2)$; the entropy is the horizon **area**, forced by the first law, by dimensions, by the Euclidean section, and by the second law. The horizon-generating flow is read as the modular flow, and its modular Hamiltonian $K=-\log\rho$ is a Hermitian element of $\mathbb{M}_+$. Two facts limit how far this goes. The entropy is **geometric and imported** — obtained from the first law and the Euclidean action, not from a count of states — and the framework supplies **no horizon Hilbert space and no microstate count**. The central open question recorded in the thermodynamics article is whether an $\mathbb{M}_+$ state exists whose von Neumann entropy is $A/4G$; it is left open there because the framework provides no such state. The framework's own entropy functional on $\mathbb{M}_+$, $S(\tilde\rho)=-2\,\mathrm{Sc}(\tilde\rho\log\tilde\rho)$, is the entropy of a **qubit**, a different object from the black-hole entropy.

**The area-scaling law.** $S\propto A$ is a codimension-two scaling of the entropy. It is imported with the horizon geometry; it is not produced by the algebra. For the Kerr–Newman family, with $A=4\pi(r_+^2+a^2)$ and $\kappa=(r_+-r_-)/(2(r_+^2+a^2))$, the first-law identity $(\kappa/8\pi)\,\partial A/\partial M=1$ holds (recomputed symbolically on the general family and at a generic point with both rotation and charge), and $A\to\lambda^2A$ under the scaling of the family — both are geometric facts about the imported metric.

**The KMS condition.** $F_{\tilde A\tilde B}(t+i\beta)=F_{\tilde B\tilde A}(-t)$ holds on the algebra for a thermal state at inverse temperature $\beta$; the shift is along the intrinsic imaginary time $ict$ of $\mathbb{M}_-$, and the generator of the flow, $K=-\log\rho$, is Hermitian, hence in $\mathbb{M}_+$. The Bisognano–Wichmann article adds that for the wedge the modular flow is the boost, with generator $G_1=ie_1\in\mathbb{M}_+$ and rapidity $2\pi s$; that theorem is imported. It is worth recording what the KMS condition is and is not: it is the abstract characterization of thermal equilibrium, it holds for ordinary thermal systems, and it is not by itself a statement about two dual descriptions.

**What the name "informational" is.** The parent article on $\mathbb{M}_+$ identifies the Hermitian subspace algebraically with the operator algebra of a two-state system, and states plainly that whether this structure is *physically realised* as an informational sector is not known: the algebraic identification is established, the physical realisation is a hypothesis. The name is that hypothesis's name, and not a result.

## The Speculative Identification and Its Immediate Obstruction

**Proposal —** the holographic reading proposes that $\mathbb{M}_-$ is the bulk and $\mathbb{M}_+$ the boundary: the material sector provides the spacetime and its geometry, and the informational sector provides the theory that encodes it. The opposite direction is available as a proposal too — $\mathbb{M}_+$ as the "informational bulk" and $\mathbb{M}_-$ as the "material boundary" — and the two proposals are not equivalent, since the sectors are not symmetric. Whichever direction is proposed, the same three established facts meet it.

**Neither sector is lower-dimensional.** $\dim_\mathbb{R}\mathbb{M}_-=\dim_\mathbb{R}\mathbb{M}_+=4$ and $\dim_\mathbb{R}\mathbb{B}=8$ (recomputed). A boundary of a four-dimensional bulk is three-dimensional. The two-sector split does not have the dimensions of a bulk and its boundary; it is a split of one eight-real-dimensional algebra into two four-real-dimensional halves. This is the first and simplest obstruction, and it is an algebraic fact, not a matter of interpretation.

**The two sectors are complementary, not separated.** Bulk and boundary in a holographic correspondence are different spaces, related by a map; they are not the two halves of one algebra. Here $\mathbb{M}_+$ and $\mathbb{M}_-$ are the Hermitian and anti-Hermitian parts of the same $\mathbb{B}$, and every element of $\mathbb{B}$ is a sum of one of each. There is no "distance" between them along which a boundary could sit, and no asymptotic region.

**The relation that does exist runs the wrong way.** The algebraic relation between the sectors is that $\mathbb{M}_+$ acts on $\mathbb{M}_-$ by rotor conjugation, $\tilde X\mapsto\tilde\Lambda\tilde X\tilde\Lambda^\dagger$ — operators acting on states. A boundary theory does not act on its bulk in this sense; it is dual to it. The action is an automorphism of $\mathbb{M}_-$, not a map from a boundary algebra into a bulk.

**The framework's own boundary objects lie inside $\mathbb{M}_-$.** The zero-divisor cone, the wedge boundary, and the horizon are all null or codimension-two loci in $\mathbb{M}_-$; none of them is $\mathbb{M}_+$. If the framework contains a bulk/boundary pair at all, the natural candidate is therefore a pair *within* the material sector — a region and its boundary — not the material/informational pair. **Proposal —** one could speculate that $\mathbb{M}_-$ supplies both the bulk and the boundary, and $\mathbb{M}_+$ supplies the dictionary data that relates them; but then $\mathbb{M}_+$ is not the boundary theory, and calling its elements a "dictionary" does not produce one.

The obstruction is not a technicality to be repaired by a better choice of words. A correspondence in which the two sides have the same dimension, are complementary subspaces of one algebra, and are related by the action of one on the other is not a holographic correspondence in the sense of the template. It is a different structure that shares part of the vocabulary.

## Why Area Scaling Is a Hint and Not a Correspondence

The area scaling of entropy is the most tempting of the three features, and the one most often misread. The standard error is to treat "the entropy scales with the area" as equivalent to, or as evidence for, holography. It is neither.

**Area scaling appears where there is no holographic dual.** The Bekenstein bound limits the entropy of a region by an energy times a size, and the holographic principle of 't Hooft and Susskind is the conjecture that the information in a region is bounded by its boundary area; that conjecture is the *motivation* for holography, not a derivation of a dual description. Separately, the ground states of gapped local quantum field theories obey entanglement-entropy area laws — the entanglement of a region scales with the area of its boundary — with no gravitational dual anywhere in sight. So $S\propto A$ is a property that holographic and non-holographic systems share, and it cannot distinguish them.

**In holography the area law has a specific origin that the framework does not reproduce.** The Ryu–Takayanagi formula states that the entanglement entropy of a boundary region equals the area of the minimal bulk surface homologous to it, divided by $4G_N$. The area that appears is the area of a *bulk* surface, and the entropy is that of a *boundary* region; the formula is a statement about a minimisation problem and about a region of the boundary theory. In the framework the area is the area of a horizon in $\mathbb{M}_-$, and the entropy is the horizon's own geometric entropy. There is no boundary region, no bulk minimal surface, and no minimisation. Even the two-sided structure of the holographic area law is not reproduced.

**And the framework's area law is imported.** The algebra does not produce a horizon or an area; the metric is an imported frame field, and the entropy is obtained from the first law and the Euclidean action. The scaling was checked (for Kerr–Newman, $(\kappa/8\pi)\partial A/\partial M=1$ and $A\to\lambda^2A$ under the scaling of the family), but a check of an imported law is not a derivation of it, and it is certainly not a holographic dual.

**Proposal —** area scaling could be read as a *necessary condition* that any holographic reading must meet, and on that reading the framework passes it. Passing a necessary condition is not satisfying it. The note records the pass and declines to read more into it; this is exactly the conflation the note is written to avoid.

## What the Name "Informational" Does and Does Not Do

The word "informational" is a name for the Hermitian subspace. The algebraic content of that name is real: $\mathbb{M}_+$ is, as an algebra, the operator algebra of a two-state system — a qubit — and that identification is established. But a finite-dimensional qubit algebra is not a boundary field theory. In holography the boundary theory is a local quantum field theory with infinitely many degrees of freedom, and its rank or central charge is what allows the bulk to become semiclassical. A single qubit has two states and an entropy bounded by $\log 2$; it cannot encode degrees of freedom that grow with a horizon's area.

The parent article is explicit about the status. It records that the algebraic identification of $\mathbb{M}_+$ with the operator algebra of a two-state system is established and not a conjecture, and it says that what remains a **hypothesis** is whether this structure is physically realised as a distinct sector of the world; its stated position is that this is not yet known. So the note says plainly: **calling $\mathbb{M}_+$ "informational" does not make it a boundary theory.** Reasoning of the form "$\mathbb{M}_+$ is informational, holography is about information, therefore the split is holographic" is invalid, because the first premise names a hypothesis and the second names a different subject. The name does no evidential work. It motivates a research program — which is how the parent presents it — and it is not a premise from which a correspondence can be deduced.

The one place where "information" and "entropy" meet inside the framework is the entropy functional $S(\tilde\rho)=-2\,\mathrm{Sc}(\tilde\rho\log\tilde\rho)$ on states of $\mathbb{M}_+$. It is the qubit von Neumann entropy, and the corpus treats it as a different object from the black-hole entropy $A/4G$; the thermodynamics article records that reading $A/4G$ as the von Neumann entropy of an $\mathbb{M}_+$ state would require a horizon state the framework does not provide. So even the terminological meeting point is a distinction, not a bridge.

**Proposal —** the name might still be *suggestive*: a Hermitian operator algebra acting on the material sector is the kind of object out of which a boundary dictionary is built. Suggestiveness is not support. The note records the suggestion and does not upgrade it.

## Why AdS/CFT Cannot Be Imported

The temptation, once the reading is proposed, is to borrow the results of AdS/CFT to support it. The note declines, and says why.

The correspondence presupposes the four items of the opening template: an asymptotically anti-de Sitter bulk, a conformal boundary, a lower-dimensional conformal field theory on it, and a dictionary. The framework has **no negative cosmological constant**: it has no cosmological constant at all. Every cosmological-constant $\Lambda$ in the corpus is imported standard physics — the parameter of the imported Schwarzschild–AdS metric used to illustrate the extended first law of black-hole thermodynamics, and the cosmological-constant term of the Friedmann equations in the cosmology agenda — and none is framework-native. With no negative $\Lambda$ there is no anti-de Sitter background, hence no conformal boundary at infinity, hence nowhere for a boundary theory to live.

Importing the results of AdS/CFT — Ryu–Takayanagi, the bulk-to-boundary dictionary, large-$N$ counting, central charges — would be importing the conclusions of a structure whose hypotheses the framework does not satisfy. The note does not do it, and no displayed statement about the framework rests on it. The references to the correspondence are made only as the yardstick of the second section, never as evidence.

The near-horizon geometry of the extremal Reissner–Nordström hole, $\mathrm{AdS}_2\times S^2$, mentioned in the thermodynamics article, is likewise an external geometry imported into a framework that does not generate it. Its appearance is a fact about the standard solution, not a sign that the algebra contains an AdS factor.

## The Checklist: What Would Have to Be True

The strongest honest version of the holographic reading is not an assertion but a list: the conditions under which the reading would be a correspondence, with the framework's present status on each. The template supplies the requirements; the status column records what the corpus actually contains. This list is the note's principal deliverable, because it converts the question "is this holography?" into a set of specific, checkable absences.

| Requirement | What it means | Framework status |
|---|---|---|
| A bulk theory with a fixed background | A dynamical metric on a chosen (asymptotically AdS) background, with a semiclassical limit | **Absent.** No dynamics and no metric of its own; the frame field is imported, and the algebra's local-scale class cannot carry a black-hole exterior |
| An asymptotic conformal boundary | A timelike boundary at infinity on which the dual description lives | **Absent.** No cosmological constant, no background, no asymptotic region |
| A lower-dimensional boundary theory | A local quantum field theory on the boundary, with its own local operator algebra and Hilbert space | **Absent.** $\mathbb{M}_+$ is four-real-dimensional and finite-dimensional (a qubit), not a lower-dimensional local field theory |
| A dictionary | A map between bulk fields and boundary operators, fixing correlation functions | **Absent.** The only relation is the action of $\mathbb{M}_+$ on $\mathbb{M}_-$ inside the same algebra — an automorphism, not a bulk–boundary map |
| A large-$N$ / semiclassical regime | Many boundary degrees of freedom, so that the bulk becomes classical | **Absent.** The algebra is fixed and finite ($\mathbb{B}\cong M_2(\mathbb{C})$); there is no $N$ to take large |
| Entropy from boundary entanglement | Ryu–Takayanagi: the entropy of a boundary region equals the area of a bulk minimal surface over $4G_N$ | **Absent.** The entropy is the horizon area, geometric and imported; there is no boundary region, no minimal surface, and no boundary state |
| A boundary state whose entropy is the area | A state in the "boundary" sector with von Neumann entropy $A/4G$ | **Absent / open.** The framework's entropy functional on $\mathbb{M}_+$ is a qubit entropy; the existence of such a state is the thermodynamics article's central open question |
| A thermal/KMS link between the sides | The generator of the bulk flow is an element of the other sector | **Present but not sufficient.** $K=-\log\rho\in\mathbb{M}_+$ and the KMS condition hold; but KMS is satisfied by any thermal system, including a single qubit (recomputed), and does not imply a dual |

Seven of the eight rows record a required ingredient that the framework does not have, and the eighth — the KMS link — is present but is generic to thermal physics. **Proposal —** the reading would become a correspondence on the day a computation on one side reproduced a nontrivial result on the other; no such computation exists, and the note proposes none.

## What the Two-Sector Split Shares with Holography, Honestly

The verdict below should not be a strawman, so it is worth recording what the two-sector split genuinely shares with a holographic correspondence. Each item is a **resemblance or analogy**, and none is evidence.

**A distinguished split produced by an operation.** The algebra falls into two parts exchanged by multiplication by $i$. Holography also joins two descriptions, but by a duality between different spaces, not by an involution of one algebra. *Analogy.*

**An asymmetry of action.** One part acts on the other: $\mathbb{M}_+$ on $\mathbb{M}_-$ by rotor conjugation. Holography has an asymmetry of scale — the bulk is semiclassical while the boundary is strongly coupled — but not an action of one side on the other. *Analogy; and in the framework it is the operator/state asymmetry of a finite-dimensional algebra.*

**A thermal and modular structure with the generator on the other side.** The modular Hamiltonian $K=-\log\rho$ is Hermitian and so lies in $\mathbb{M}_+$, while the fields it evolves lie in $\mathbb{M}_-$, and the wedge modular flow is the boost. This is a real structural fact, and it is the closest the framework comes to a statement that one sector encodes the other. *Analogy* — but it is the structure of thermal equilibrium in any quantum system, not of a duality.

**An area-scaling entropy.** The horizon entropy is the area. *Analogy only; imported, and shared by non-holographic systems, as the section on area scaling showed.*

**The vocabulary of information.** The names "material" and "informational", and the presence of an entropy functional. *Name, not structure.*

A collision of names plus a handful of genuine analogies can be a heuristic — a reason to look for a real correspondence. It is not a reason to believe one is already there. The framework does not, at present, cash the heuristic.

## The Verdict: A Suggestive Collision of Names

The conclusion of the note is the one stated at the outset. **On the present state of the framework, the split $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ is a suggestive collision of names and structures with holography, not a holographic correspondence.** This is a result, and a useful one: it names exactly what would have to be built for the reading to change status, and it prevents the framework from claiming the authority of a correspondence whose ingredients it lacks.

The reasoning can be put in three lines, matching the three temptations.

- **Area scaling is not holography.** It is a consequence of holography in the AdS setting, and it occurs in systems with no dual. The framework's area law is imported and geometric. It is a hint at most, and a hint that has been independently explained elsewhere.
- **A KMS condition is not a duality.** It is the characterization of thermal equilibrium, satisfied by ordinary thermal systems; the note recomputed that a single thermal qubit with generic observables satisfies it exactly. Its appearance in the framework, with the generator in $\mathbb{M}_+$, is a genuine structural fact about temperature, not a signal of two dual descriptions.
- **The name "informational" does no evidential work.** It is attached to the Hermitian subspace as part of a hypothesis that the parent article states is not known to be physically realised, and the algebraic object it names is a qubit, not a boundary field theory. Using the name to argue for a boundary theory is circular.

The decisive obstruction, however, is not any of the three but the algebra itself: the two sectors have **equal dimension**, are **complementary subspaces of one algebra**, and are related by the **action of one on the other**. A holographic correspondence has none of those properties; its two sides are different spaces, of different dimension, joined by a dictionary.

**Proposal —** the framework's natural bulk/boundary pair, if it has one, is a region of $\mathbb{M}_-$ and its boundary — the zero-divisor cone, the wedge, or a horizon — not the material/informational pair. Exploring that pair would be a different research program, and it would not make $\mathbb{M}_+$ a boundary theory.

What would change the verdict is a short and specific list: a framework-native lower-dimensional field theory built on $\mathbb{B}$-modules; a dictionary with checkable content; a large-$N$-like limit; and, most concretely, an $\mathbb{M}_+$ state whose von Neumann entropy is the horizon area, which is the central open question of the thermodynamics article. None of these exists. Until one does, the honest description of the $\mathbb{M}_-/\mathbb{M}_+$ split is a structural analogy to holography — and the note leaves it as one.

## Open Questions

1. **A framework-native boundary theory.** Is there a lower-dimensional local field theory built on $\mathbb{B}$-modules — with its own local operator algebra and infinitely many degrees of freedom — that could play the role of a boundary theory? At present the only algebra available is the finite-dimensional $\mathbb{B}\cong M_2(\mathbb{C})$.
2. **A horizon state in $\mathbb{M}_+$.** Does a state of $\mathbb{M}_+$ exist whose von Neumann entropy is the horizon area $A/4G$? This is the thermodynamics article's central open question, and it is also the most concrete requirement of the holographic dictionary; if such a state existed, the area law would become a statement about the algebra.
3. **Bulk reconstruction.** Can the material-sector state be reconstructed from the informational sector? For the finite-dimensional algebra the answer is no: the modular theory requires a faithful state and the algebra does not select one, so the flow is not determined by the algebra alone. Is there an extension in which reconstruction becomes possible?
4. **A different split.** Is the framework's natural bulk/boundary pair a region of $\mathbb{M}_-$ and its boundary — the zero-divisor cone, the wedge, or a horizon — rather than the material/informational pair? That program would leave $\mathbb{M}_+$ out of the boundary role entirely.
5. **An algebraic extremal surface.** Holographic entropy is a minimisation over bulk surfaces. Is there any algebraic quantity — a trace over a boundary of the algebra, a limit of the modular operator, a geometric entropy of a subalgebra — that reduces to an area in an appropriate limit, and is there a variational principle selecting it?
6. **The entropy functional and the area law.** The functional $S(\tilde\rho)=-2\,\mathrm{Sc}(\tilde\rho\log\tilde\rho)$ on $\mathbb{M}_+$ is bounded by $\log 2$ for the qubit. Can a limit of such functionals, over an infinite-dimensional extension of the algebra, approach an area law, or is the geometric entropy the framework's final word?
7. **Empirical contact.** Is there any regime in which a holographic reading of the split would give a prediction distinguishing it from the standard account? No such regime is known, and the framework currently supplies no discriminator for any of its readings.
8. **Heuristic or collision?** Is the analogy useful as a guide for building the missing boundary theory, or is it only a collision of names? The note's verdict is the second, but the question is what would test it.

## Summary

This is a speculative note, and it keeps its licence and its limit separate. **Proposal —** the reading examined is that the framework's material sector $\mathbb{M}_-$ is a "bulk" and its informational sector $\mathbb{M}_+$ a "boundary", so that one sector encodes the other. That identification is proposed, not derived; every speculative claim in the note carries the marker where it is made, and every established statement is either established physics or established algebra.

The framework does have three things that a holographic reading would want: a boundary and entropy story (the horizon, the Bekenstein–Hawking area law $S=k_BA/(4\ell_P^2)$, the modular flow with $K=-\log\rho\in\mathbb{M}_+$); an area-scaling law; and a KMS condition $F_{\tilde A\tilde B}(t+i\beta)=F_{\tilde B\tilde A}(-t)$ tied to the intrinsic imaginary time $ict$ of $\mathbb{M}_-$.

None of the three establishes a correspondence, and the note says so at each point. Area scaling is a consequence of holography in the AdS setting and occurs in systems with no dual, such as gapped field theories obeying entanglement area laws; conflating the two is the standard error, and the framework's own area law is geometric and imported. The KMS condition characterizes thermal equilibrium in any quantum system — the note recomputed that a single thermal qubit with generic observables satisfies it exactly — and a thermal condition is not a duality. The name "informational" is attached to the Hermitian subspace as part of a hypothesis that the parent article states is not known to be physically realised, and the object it names is the operator algebra of a qubit, not a boundary field theory; the name does no evidential work.

The decisive obstruction is algebraic. The two sectors have equal real dimension ($4$ each, in an algebra of real dimension $8$), so the split is not a dimensional reduction; they are the Hermitian and anti-Hermitian halves of one algebra, so they are complementary rather than separated and there is no asymptotic region between them; and the relation between them is the action of one on the other, $\tilde X\mapsto\tilde\Lambda\tilde X\tilde\Lambda^\dagger$, which is an automorphism of $\mathbb{M}_-$ rather than a bulk–boundary map. The framework's own boundary objects — the zero-divisor cone, the wedge boundary, the horizon — lie inside $\mathbb{M}_-$.

AdS/CFT is not imported. The framework has no negative cosmological constant (none at all), no conformal boundary, no boundary field theory, and no dictionary, so the results of the correspondence cannot be used as evidence for the reading; the correspondence appears in the note only as the yardstick of what a correspondence requires. The strongest honest form of the proposal is the checklist of the eighth section: eight requirements, seven absent and the eighth (the KMS link) present but generic.

The conclusion is that the $\mathbb{M}_-/\mathbb{M}_+$ split is a **suggestive collision of names and structures with holography, not a holographic correspondence.** That is a legitimate result. It converts the question into a list of specific, checkable absences — a boundary theory, a dictionary, a large-$N$ limit, and, above all, an $\mathbb{M}_+$ state whose entropy is the horizon area — and it keeps the framework from borrowing the authority of a structure it does not have.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}\cong M_2(\mathbb{C})$ | Biquaternion algebra, real dimension $8$ |
| $\mathbb{M}_-$ | Material sector: imaginary time, real space; anti-Hermitian; real dimension $4$ |
| $\mathbb{M}_+$ | Informational sector: real time, imaginary space; Hermitian; real dimension $4$ |
| $\mathbb{H}_{\mathbb{B}}$, $\mathbb{C}_{\mathbb{B}}$ | Real-quaternion subspace; complex scalars |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Scalar imaginary, $i^2=-1$; $i\mathbb{M}_\pm=\mathbb{M}_\mp$ |
| $\tilde X=ict\,e_0+x\,e_1+y\,e_2+z\,e_3$ | Material coordinate |
| $N(\tilde X)=\tilde X\bar{\tilde X}$ | Norm form; $N=0$ is the zero-divisor cone |
| $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$ | Trace formula (inherited) |
| $K=-\log\rho$ | Modular Hamiltonian, Hermitian, hence in $\mathbb{M}_+$ |
| $F_{\tilde A\tilde B}(t+i\beta)=F_{\tilde B\tilde A}(-t)$ | KMS condition; $F$ is complex-valued |
| $G_1=ie_1\in\mathbb{M}_+$ | Wedge boost generator; $K_W=2\pi G_1$ |
| $T=\hbar\kappa/(2\pi c k_B)$ | Hawking temperature of the horizon flow |
| $S=k_Bc^3A/(4G\hbar)=k_B A/(4\ell_P^2)$ | Bekenstein–Hawking entropy (area law) |
| $A$, $\kappa$, $\ell_P^2=\hbar G/c^3$ | Horizon area; surface gravity; Planck area |
| $d+1$ | Bulk dimension of a holographic correspondence; boundary dimension $d$ |
| $N$ | Rank / number of colours of the boundary theory, taken large in the semiclassical limit |
| Ryu–Takayanagi | $S_{\text{boundary region}}=\mathrm{Area}(\text{bulk minimal surface})/(4G_N)$ |
| GKPW | Bulk-to-boundary dictionary fixing correlation functions |

## Further Reading

**Companion articles (this series).** All of the following exist in `articles/`.

- *Introduction to the Biquaternion Universe*, for the algebra $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ and the two-sector split.
- *$\mathbb{M}_-$ as the Material Space*, for the material sector, the four-vectors, the norm form, and the zero-divisor cone.
- *$\mathbb{M}_+$ as the Informational Space*, for the Hermitian sector, the operator algebra of a two-state system, the action on $\mathbb{M}_-$, and the informational hypothesis with its stated limits.
- *Hawking Radiation in Biquaternionic Form*, for the horizon temperature, the Euclidean period, and the mode-mixing derivation.
- *Black Hole Thermodynamics in Biquaternionic Form*, for the area law $S=A/4$, the first law, the geometric (non-counted) entropy, and the open question of a horizon state in $\mathbb{M}_+$.
- *The Modular Hamiltonian in Biquaternionic Form*, for the modular generator, its spectral form, and the Gibbs structure.
- *The KMS Condition and the Biquaternion Framework*, for the imaginary-time strip, the intrinsic imaginary time of $\mathbb{M}_-$, and the modular Hamiltonian in $\mathbb{M}_+$.
- *The Bisognano–Wichmann Theorem under the Biquaternion Framework*, for the wedge modular flow as the boost, and the anti-unitarity of the modular conjugation.
- *The Unruh Effect in Biquaternionic Form*, for the Rindler wedge and the KMS character of the accelerated vacuum.
- *Curved Spacetime and the Biquaternion Framework*, for the imported frame field and the negative result that the algebra's local-scale metric class cannot carry black-hole exteriors.
- *Quantum Thermodynamics in Biquaternionic Form*, for the standard thermodynamic functionals on $\mathbb{M}_+$ and the Gibbs state of a qubit.
- *Exercise: Entanglement Entropy and the Partial Trace*, for the entropy functional on $\mathbb{M}_+$ and the partial trace.
- *The Modular Theory of Tomita–Takesaki under the Biquaternion Framework*, for the Tomita operator, the modular flow, and the state-selection gap.
- *Why Complexify Spacetime?*, for an earlier structural analogy to holography and its explicit labelling as an analogy rather than a derivation.

**Standard references.**

- G. 't Hooft, "Dimensional reduction in quantum gravity," in *Salamfest* (1993), for the origin of the holographic principle.
- L. Susskind, "The world as a hologram," *Journal of Mathematical Physics* **36** (1995) 6377–6396, for the holographic principle.
- J. D. Bekenstein, "A universal upper bound on the entropy to energy ratio for bounded systems," *Physical Review D* **23** (1981) 287–298, for the bound that motivates area scaling of entropy.
- J. Maldacena, "The large $N$ limit of superconformal field theories and supergravity," *Advances in Theoretical and Mathematical Physics* **2** (1998) 231–252, for the correspondence.
- E. Witten, "Anti de Sitter space and holography," *Advances in Theoretical and Mathematical Physics* **2** (1998) 253–291, for the dictionary and the correspondence.
- S. Ryu and T. Takayanagi, "Holographic derivation of entanglement entropy from the anti-de Sitter space/conformal field theory correspondence," *Physical Review Letters* **96** (2006) 181602, for the minimal-surface formula and the area law's holographic origin.
- R. Bousso, "The holographic principle," *Reviews of Modern Physics* **74** (2002) 825–874, for the covariant entropy bound and a review of what holography does and does not claim.
- V. E. Hubeny, "The AdS/CFT correspondence," *Classical and Quantum Gravity* **32** (2015) 124010, for a review of the correspondence and its ingredients.
- H. Casini, M. Huerta, and R. C. Myers, "Towards a derivation of holographic entanglement entropy," *Journal of High Energy Physics* **05** (2011) 036, for the ball modular Hamiltonian and the entanglement route to the area law.
- M. Van Raamsdonk, "Building up spacetime with quantum entanglement," *General Relativity and Gravitation* **42** (2010) 2323–2329, for the entanglement/geometry idea that a biquaternionic reading would have to imitate, and does not.