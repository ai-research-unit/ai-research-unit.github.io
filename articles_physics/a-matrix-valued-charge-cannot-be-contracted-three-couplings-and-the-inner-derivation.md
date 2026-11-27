# __A Matrix-Valued Charge Cannot Be Contracted: Three Couplings and the Operation the Matrix Rung Uses Instead__

## Introduction

**Three couplings of a particle to a field appear in the corpus and in the literature around it, and all three are usually written as contractions.** Wong's equations contract an algebraic charge with an algebra-valued field strength and get a force. The classical spinning-particle literature contracts an internal two-form with the field's two-form and gets a coupling. **The corpus's matrix rung does neither, and this article's claim is that it cannot: at that rung there is no charge to contract, and what appears in place of a contraction is a commutator.**

**Why a contraction is unavailable, in one sentence.** A contraction consumes an index — it takes two objects and returns one with fewer indices — and at the matrix rung the object the field acts on is the pair momentum, which must come back matrix-valued. **An operation that consumes the matrix index cannot return a matrix**, so the rung needs an operation that *acts on* an algebra element and returns one, and the only such operation the algebra supplies is its own commutator.

**The article's second subject, and the reason it is not a footnote.** The matrix rung has *two* eigenvalue splittings, and confusing them is the error this article is written to prevent. The pair's inertia is $q_{kl}=\rho_{k}-\rho_{l}$, the difference of two *density* eigenvalues; the force weight is $f_{k}-f_{l}$, the difference of two *field* eigenvalues. **They enter different places in the balance, they are computed from different objects, and one of them divides where the other does not.**

**What the article is not.** It is not a claim that Wong's equations are wrong, or that the trace pairing is illegitimate. **Wong's equations are correct and the trace pairing is the right contraction where a contraction exists.** The article's claim is about the rung where no contraction exists, and the trichotomy is what makes the claim precise.

**The article's place in the chain.** It is one of the two articles in *From the Field Equation to the Force* — the force section of *Biquaternion Universe Action* — that state the general form of a force block, and it is the one that carries the matrix-valued case. [Five Steps from a Lagrangian to Fluid Equations](five-steps-from-a-lagrangian-to-fluid-equations.html) states the skeleton; this article states what the matrix rung's force slot is filled by.

## The Column This Article Works, and the Columns It Does Not

**The trichotomy is general and the worked case is the matrix column.** The three couplings are classified by what each consumes, and the classification holds at every rung; what the article computes is the rung at which the first two are unavailable, because that is where the classification has content. **The other columns are named here and not worked**, and the naming is what keeps the article from reading as a statement about matrices dressed as a statement about couplings.

- **The scalar and Proca rungs.** The force is a contraction of the field strength with the velocity — one free spacetime index returned from two consumed — and the Proca rung adds the polarization term, a second contraction of the same kind. Both are the trichotomy's second entry with an internal index attached, and neither needs the commutator, because the object acted on is a number or a vector and a contraction returns one.
- **The Dirac rung.** The same contraction, with the spin tensor in place of one of the velocity factors: the Lorentz force plus the Pauli term, again two indices consumed and one returned. The spin is a rotor, and the rotor's equation is a transport and not a force — which is why the Dirac rung's spin term is written beside the force block and not in it.
- **The matrix rung, worked here.** The object the field acts on must come back matrix-valued, so the operation that consumes the matrix index cannot be used. That is the whole of the article's claim, and it is why the commutator appears where the contraction was.

**What this does not say.** It does not say that the lower rungs' forces are the matrix one's limit — they are not, and the article's own finding is that a two-density truncation reproduces the abelian force law exactly and the non-abelian one not at all. **It says that the slot has a different filler at each rung, and that the filler is forced by what the balance must return.**

## Conventions

The algebra is $\mathbb{B}$ with its commutator, and at the matrix rung the field is $\Xi=U_{\mathrm{frm}}PU_{\mathrm{frm}}^{\dagger}$ with $P=\mathrm{diag}(\rho_{1},\dots,\rho_{4})$ and $U_{\mathrm{frm}}\in\mathrm{SU}(4)$. The field strength is $\mathbb{F}$, a Hermitian element of the algebra — **Hermitian, with real eigenvalues, in the corpus's convention**, and this is stated because the sign of every subsequent difference depends on it.

**The conventions that matter and where they come from.** [The Algebraic Vocabulary](the-algebraic-vocabulary-element-conjugations-six-subspaces-and-two-ledgers.html) fixes the commutator and the two pairings; [The Yang–Mills Equation](the-yang-mills-equation-in-biquaternionic-form.html) fixes why the trace pairing is used there; [The Primordial Force Law](the-primordial-force-law-and-the-two-wong-terms.html) fixes the balance this article's operation appears in.

**The pair basis, which is the article's working chart.** For a diagonal $P$, the pair basis consists of the off-diagonal entries $kl$ with $k\neq l$, and in that basis a commutator with a diagonal element is diagonal:

$$
\bigl[\mathbb{F},\Xi\bigr]_{kl}=\bigl(f_{k}-f_{l}\bigr)\Xi_{kl},
$$

where $f_{k}$ are $\mathbb{F}$'s eigenvalues. **This identity is the article's technical centrepiece**, and the corpus's verification check H tests it directly: the residual is $9.2\times10^{-16}$ on data of order unity, which is round-off. **The identity is exact and the check confirms the implementation, not the mathematics** — the article says which, because the distinction is the corpus's rule.

**The three residual numbers the article quotes, so that they are not confused.** Check C: $\lVert M-(\mathrm{diag}\,dP+\Omega_{kl}(\rho_{l}-\rho_{k}))\rVert=3.7\times10^{-8}$. Check H: the commutator's eigenvalue-difference identity to $9.2\times10^{-16}$. Check I: $\mathbb{F}$'s Hermiticity, $\lVert F-F^{\dagger}\rVert=0$ and $\max\lvert\mathrm{Im}\,f\rvert=0$. **Each is a witness to one mathematical statement and none to another**, and the article assigns them one by one.

## Three Couplings and What Each Contracts

**The trichotomy is the article's frame, and the three couplings differ in what they consume.**

| coupling | the object acted on | the operation | what it consumes | the result |
| --- | --- | --- | --- | --- |
| Wong's equations | a charge $Q$ in the algebra | $\langle Q,\mathbb F(u)\rangle$ — the trace pairing | one algebra index from each factor | a covector force |
| the classical spinning particle | an internal two-form $S^{\mu\nu}$ | $\tfrac12 S^{\mu\nu}\mathbb F_{\mu\nu}$ | two spacetime indices from each factor | a scalar coupling |
| the matrix rung | the pair momentum $\Pi_{\imath}$ | $[\mathbb F,\Pi_{\imath}]$ | **nothing** | a matrix-valued source |

**Wong's contraction consumes an algebra index and returns a covector, and that is exactly what a force law needs.** The left side of $\mathrm{D}u^{\imath}/\mathrm{D}\tau=g\langle Q,\mathbb F^{\imath}{}_{\jmath}\rangle u^{\jmath}$ is a covector; the right side must be one; and the trace pairing is the operation that produces a covector from two algebra elements and a base vector. **The contraction and the force law's form match, and that match is why Wong's equations look the way they do.**

**The spinning particle's contraction consumes spacetime indices and returns a scalar, and that is exactly what a Lagrangian coupling needs.** $\tfrac12 S^{\mu\nu}\mathbb F_{\mu\nu}$ is a scalar density, it can be added to an action, and its variation produces the spin's equation. **No algebra index is consumed, because the spin is a spacetime two-form and not an algebra element** — and the corpus's spin-half and spin-one rungs' spin currents are of this kind.

**The matrix rung's operation consumes nothing and returns a matrix, and that is exactly what a balance needs.** The balance's left side is matrix-valued — it carries the pair index $kl$ — and its right side must be too. **Any operation that consumed the pair index would produce a scalar or a covector and could not stand where the source stands.** That is the article's first claim, and it is a claim about index counting rather than about groups.

## Why the Trace Pairing Needs Cyclicity

**Wong's contraction is not "multiply the two matrices"; it is "pair them with an invariant form", and the invariance is a condition the form must satisfy.** The force is $g\langle Q,\mathbb F^{\imath}{}_{\jmath}\rangle u^{\jmath}$, and for the force to be gauge-covariant the pairing must be invariant under the gauge group's action on both factors:

$$
\bigl\langle [A,Q],\mathbb F\bigr\rangle+\bigl\langle Q,[A,\mathbb F]\bigr\rangle=0 .
$$

**For the trace pairing this is cyclicity**, $\mathrm{tr}([A,Q]\mathbb F)+\mathrm{tr}(Q[A,\mathbb F])=0$, and cyclicity is what makes the two terms cancel. **A pairing that is not cyclic does not give a gauge-covariant force**, and that is the whole of the requirement.

**The corpus has one pairing that fails cyclicity and the failure is recorded.** The informational scalar $2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ is a pairing on the algebra, and it is not cyclic. **The Yang–Mills action therefore cannot be written with it** — the action's invariance would fail — and [The Yang–Mills Equation](the-yang-mills-equation-in-biquaternionic-form.html) states the trace as the pairing chosen for exactly this reason. **The article's point is not that the informational scalar is defective; it is that the cyclicity condition is a real constraint that a pairing can fail, and the corpus has the case.**

**Three consequences, and the article states all three because they are often conflated.** *First*, the trace pairing is legitimate at any rung whose group is finite-dimensional and whose action is invariant under it. *Second*, the informational scalar is not, for the Yang–Mills action. *Third* — and this is the article's subject — **at the matrix rung the question does not arise**, because no pairing is used at all: the operation is a commutator, and a commutator is gauge-covariant by construction, for every gauge group, without any cyclicity condition.

**Why the commutator is automatically covariant, in one line.** Under $Q\to gQg^{-1}$ and $\mathbb F\to g\mathbb F g^{-1}$, the commutator transforms as $[\mathbb F,\Pi]\to g[\mathbb F,\Pi]g^{-1}$. **The conjugation cancels because the commutator is built from the algebra's own product and its reverse**, and the cancellation requires no invariant form. **That is why the matrix rung can do without the trace where the Yang–Mills action cannot.**

**The asymmetry, stated so it is not read as a defect of the trace.** The Yang–Mills action integrates a *scalar*, so it needs a pairing that produces one and an invariant form to make the scalar invariant. **The matrix rung's balance equates a matrix to a matrix**, so it needs no scalar and no invariant form. **Different objects, different requirements, and the trace's cyclicity is a requirement of the first and not of the second.**

## What the Commutator Is, and Why It Is the Only Candidate

**The algebra supplies one bilinear operation that takes two elements and returns one: its product. The commutator is the antisymmetric part of that product.** The article's claim is that this makes the commutator the unique candidate for an operation acting on the pair momentum, and the claim is worth stating precisely.

**A bilinear operation $B(\mathbb F,\Pi)$ that takes two algebra elements and returns an algebra element, and that is derivable from the algebra's own structure, must be built from the product.** The product $\mathbb F\Pi$ is one such operation and it is not antisymmetric; $\Pi\mathbb F$ is another. **Their difference is the commutator, their sum is the anticommutator, and the algebra's derivations are generated by the commutator** — an *inner derivation* is $D_{\mathbb F}\Pi=[\mathbb F,\Pi]$, and it is the algebra acting on itself.

**Why the derivation and not the product is the right operation, and the reason is the balance's meaning.** The commutator is the algebra's action on itself — the infinitesimal transformation $\Pi\to\Pi+\epsilon[\mathbb F,\Pi]$ is what a gauge transformation does to the momentum. **The force term in the balance should be the momentum's change under the field's transformation**, and that change is the commutator. **The product $\mathbb F\Pi$ would be a change under multiplication, which is not a transformation of the algebra into itself.**

**The anticommutator's exclusion, stated because a reader will ask.** $\{\mathbb F,\Pi\}$ is also bilinear and returns an algebra element. **It is not a derivation**: it does not satisfy the Leibniz rule, so it does not generate a transformation, and the balance's source must generate the field's action on the momentum. **The commutator is the antisymmetric combination precisely because transformations are generated by the antisymmetric part of the algebra's product.**

**The commutator's action in the pair basis, which is the identity the article opened with.** With $\mathbb F$ diagonal in the pair basis, $[\mathbb F,\Xi]_{kl}=(f_{k}-f_{l})\Xi_{kl}$. **The derivation acts diagonally, with an eigenvalue that is the difference of the two field eigenvalues**, and each pair is transported by its own weight. **The corpus's check H confirms the identity to round-off**, and the article's reading of the identity is the subject of the next section.

**The abelian limit, and it is the trichotomy's closure.** In a commutative algebra the commutator vanishes identically, so the matrix rung's operation reduces to zero and the balance loses its source. **That is the statement that a commutative algebra has no inner derivations**, and it is why the matrix rung cannot be abelian: an abelian matrix rung would have no force term at all. **The corpus's non-abelian structure is not an embellishment at this rung; it is what makes the force term nonzero.**

## Two Eigenvalue Splittings, and Why They Are Not the Same

**The matrix rung's balance contains two differences of eigenvalues, and they are computed from different matrices and play different roles.** The article states both with the corpus's symbols and then states what each is for.

| the splitting | from which matrix | its value | its role | where it appears |
| --- | --- | --- | --- | --- |
| inertia | the density $P=\mathrm{diag}(\rho_{k})$ | $q_{kl}=\rho_{k}-\rho_{l}$ | the guidance relation's denominator; the pair's inertia | $\Omega_{kl}=M_{kl}/q_{kl}$; the product-rule term $\Omega_{kl}\partial_{\imath}q_{kl}$ |
| force weight | the field strength $\mathbb F$ | $f_{k}-f_{l}$ | the commutator's eigenvalue; the weight the field applies to the pair | the source $[\mathbb F,\Pi]_{kl}=(f_{k}-f_{l})\Pi_{kl}$ |

**The inertia is a difference of densities and it divides; the force weight is a difference of field eigenvalues and it multiplies.** That sentence is the article's second claim, and it is worth dwelling on because the two splittings look alike and behave oppositely. **The guidance relation divides by the inertia because the inertia is what resists motion; the commutator multiplies by the force weight because the weight is what the field applies.** **A reader who swaps them gets a guidance relation that multiplies and a source that divides, and both are wrong.**

**Why the two cannot coincide, stated as a structural fact.** The densities $\rho_{k}$ are the field's eigenvalues at the matrix rung — the field is $\Xi=UPU^{\dagger}$ — and the field strength $\mathbb F$ is a *different* matrix, built from the connection's curvature and not from $\Xi$'s eigenvalues. **So $q_{kl}$ and $f_{k}-f_{l}$ are differences of eigenvalues of two different Hermitian matrices**, and there is no reason for them to be equal. **In a configuration where $\mathbb F$ happens to be diagonal in the same basis as $P$, the two splittings are two different functions of the same four labels**, and the article says so because it is the configuration in which a reader is most likely to conflate them.

**The corpus's check C witnesses the first splitting, and it is the one that involves no commutator.** The check tests $\lVert M-(\mathrm{diag}\,dP+\Omega_{kl}(\rho_{l}-\rho_{k}))\rVert=3.7\times10^{-8}$, i.e., that the pair momentum's variation is the diagonal part plus the inertia-weighted guidance. **The check involves the density's eigenvalues and the connection, and no field strength.** So check C is a witness to the *inertia* splitting and check H is a witness to the *force weight* splitting, and the article assigns them accordingly. **Neither check tests the other, and a reader who treats them as one verification has conflated the two splittings the article exists to separate.**

**The signs, which the with-convention statement fixes.** $q_{kl}=\rho_{k}-\rho_{l}$ appears in check C as $(\rho_{l}-\rho_{k})$ with the opposite sign, because the check's display has the guidance's term on the momentum's side. **The article does not attempt to reconcile the signs in one display** — the corpus's displays are the authority for their own signs, and the article's claim is only that the two splittings are different objects, not that they appear with a particular sign. **The convention's Hermiticity of $\mathbb{F}$ is what makes $f_{k}-f_{l}$ real**, and check I confirms that $\mathbb F$ is Hermitian with $\lVert F-F^{\dagger}\rVert=0$ and no imaginary eigenvalue.

## The Four Differences from Wong, Tabulated

**The corpus's comparison with Wong's equations is four statements, and the article states them in one place because they are usually scattered.** The comparison is not a ranking; it is a list of what changes when the charge stops being a separate object.

| | Wong's equations | the matrix rung's balance |
| --- | --- | --- |
| **the charge** | a separate algebra element $Q$, carried by the particle | **none**; the field's own matrix structure supplies the pair index |
| **the operation** | the trace pairing $\langle Q,\mathbb F(u)\rangle$ | the commutator $[\mathbb F,\Pi]$, the algebra's inner derivation |
| **the output** | a covector force, equated to an acceleration | a matrix-valued source, equated to a divergence |
| **the cyclicity requirement** | needed, and failed by the informational scalar | **not needed**; the commutator is covariant without an invariant form |

**The first difference is the deepest, and it is the one the article's title names.** Wong's particle carries a charge that is *not* the field; the matrix rung's fluid carries no charge because its "charge" is the field's own basis. **A charge that is the field's basis cannot be contracted with the field**, and the article's claim is that this is a statement about the rung's structure and not about a choice of variables.

**The second difference follows from the first and not the other way round.** If there is no separate charge, there is nothing to pair; what remains is the field acting on the momentum, and the field's action on an algebra element is its commutator. **The article states the logical order because a reader might think the commutator was chosen for convenience. It was forced.**

**The third difference is a consequence of the index counting, and it is why the matrix rung's equation is a balance.** Wong's output is a covector because its left side is a covector; the matrix rung's output is a matrix because its left side is a matrix. **Nothing about the group's size or the algebra's structure enters the argument; only the index count does.**

**The fourth difference is the one that makes the matrix rung self-sufficient.** Wong's equations need the trace's cyclicity to be gauge-covariant; the matrix rung needs nothing, because the commutator's conjugation cancels. **So the matrix rung does not inherit the Yang–Mills action's pairing problem**, and [The Yang–Mills Equation's](the-yang-mills-equation-in-biquaternionic-form.html) discussion of the trace is not a premise of this article.

## What a Force Block Owes Its Reader

**The article's second half is an inventory, and it is written for the corpus's authors rather than for its readers.** Every sector block in the corpus — strong, electroweak, electromagnetism — ends in a force article, and each force article owes the reader the same six statements. **The inventory is the general form of a force block, and the matrix rung's case is one instantiation of it.**

| what the force article owes | the question it answers | the matrix rung's answer |
| --- | --- | --- |
| **the object** | what does the force act on? | the pair momentum $\Pi_{\imath,kl}$ |
| **the source** | what produces the force? | the commutator with the field strength, $[\mathbb F,\Pi]$ |
| **the operation** | how are the two combined? | a commutator; a contraction where a charge exists |
| **the weights** | what multiplies what? | inertia $q_{kl}$ divides, force weight $f_{k}-f_{l}$ multiplies |
| **the singular set** | where does the force law fail? | where $q_{kl}=0$: equal densities, the eigenvalue crossing |
| **the verdict** | is it a law or a balance? | a balance; the velocity is internal |

**The first three lines are the trichotomy's, and the fourth is the article's two-splittings section.** The fifth is the corpus's obligation to state where its charts fail, and at the matrix rung the failure is the eigenvalue crossing — $q_{kl}=0$, the guidance relation's denominator, the point where the pair's inertia vanishes and the whole pair description degenerates. **The sixth is [S5's](base-valued-versus-internal-flow-velocity-a-test-separating-force-laws-from-momentum-balances.html)**, and it is last because it is a verdict on the other five rather than a sixth object.

**Why an inventory and not a template.** A template would be filled in mechanically and would produce force articles that state the six lines without deriving them. **An inventory states what must be *derivable*, and the corpus's rule is that each line be obtained from the rung's action and not asserted.** The matrix rung's six lines are all obtained: the object and source from the balance, the operation from the algebra, the weights from the two eigenvalue splittings, the singular set from the guidance relation, and the verdict from the velocity's type.

**The sixth line's honesty, which the article states plainly.** "A balance" is a verdict and not a demotion, and a force article that ends with it has completed its obligation. **The corpus's ladder table records the verdict for every rung, and a reader comparing rows should not read the matrix rung's row as an unfinished entry.** It is a finished entry with a different verdict.

## The Honest Limitations of the Trichotomy

**The trichotomy is a frame and not a theorem, and the article says where it is thin.** Three couplings are named; a fourth is not excluded; and the frame's content is that the three differ in what they consume.

**The spinning-particle coupling is the frame's weakest entry.** It couples two spacetime two-forms and produces a scalar, and its relation to the algebra-valued cases is a relation of analogy rather than of structure. **The article includes it because it is the literature's other standard coupling and because its contraction is genuinely different — spacetime indices rather than algebra indices — but it does not claim the three are three instances of one operation.** They are three operations with one thing in common: two are contractions and the third is not.

**The frame does not cover a coupling to a background that is itself an algebra element times a two-form.** Such a coupling would contract an algebra index and a spacetime index at once — a "twisted" contraction — and the corpus does not have one. **Whether it would behave like Wong's case or like the matrix rung's is not stated**, and the article flags the possibility rather than resolving it.

**The frame's claim about the matrix rung is strong and narrow.** It is strong: no contraction is available, and the commutator is forced. **It is narrow: it holds at the matrix rung's object — a matrix-valued momentum acted on by a matrix-valued field — and it says nothing about a rung whose momentum is scalar-valued and whose field is matrix-valued.** At such a rung a contraction would exist and the frame would predict Wong's case. **The corpus has no such rung, and the prediction is untested.**

## What This Article Does Not Claim

**That the commutator is a force.** It is the balance's *source*, and the corpus's shorthand calls the source the force. **The article keeps the shorthand and states its limit**: at the matrix rung there is no trajectory to accelerate, so "force" names the momentum's rate of change and not a mass times an acceleration. **Calling it a force is a continuation of the classical vocabulary by analogy, and the analogy is exact in form and not in content.**

**That the trace pairing is unavailable in the algebra.** It is available, it is cyclic, and it is the right pairing for the Yang–Mills action. **The claim is that the matrix rung does not use it, because the matrix rung has nothing to pair.** A reader who concludes the article is arguing against the trace has misread it.

**That the two eigenvalue splittings are unrelated.** They are both differences of eigenvalues of Hermitian matrices, and in configurations where the two matrices are simultaneously diagonal the splittings are two functions of the same four labels. **What the article claims is that they are different functions with opposite roles**, not that they are unrelated.

**That the four differences from Wong are independent.** The first forces the second, the second produces the third, and the fourth follows from the second. **The table is a logical chain and not a list of four independent observations**, and the article's ordering of it is the chain's order.

**That the inventory is exhaustive for every sector block.** It is the inventory of a *force* article, and a sector block's other articles owe other things. **A block whose force article answers the six lines has discharged this article's requirement and not the block's.**

**That the numerics establish the mathematics.** Check C, check H and check I are witnesses to implementations of statements that are exact. **The article says which is which for each**, because a residual of $10^{-16}$ that confirms an identity is a different kind of evidence from a residual of $10^{-8}$ that confirms a finite-difference scheme.

## Open Questions

**Is there an operation other than the commutator that acts on an algebra element, returns one, and is derivable from the algebra's product?** The commutator and the anticommutator are the product's antisymmetric and symmetric parts, and both return algebra elements. **The article excludes the anticommutator by the derivation requirement**, which is a requirement the balance's meaning imposes and not one the algebra imposes. **Whether a balance could be written with an anticommutator source — and what it would describe — is not settled.**

**What replaces the commutator when the momentum is not in the algebra but in a module?** A spinor's momentum lives in a module over the algebra, and the algebra acts on it by multiplication rather than by commutation. **The corpus's spinor rung has a transport whose form is the covariant derivative's**, and whether that is the module's version of the same operation is a question the article does not answer.

**Does the guidance relation's denominator vanishing have a physical reading at the matrix rung?** $q_{kl}=0$ means equal densities, and the guidance relation diverges. **The corpus's singular sets are stated one by one, and the matrix rung's is the eigenvalue crossing**; whether the crossing is a genuine physical degeneration or a chart artefact of the pair description is not settled. **The article notes that the field equation survives the crossing** — it is the pair chart that fails — **and leaves the reading open.**

**Can the two splittings be related by a single object?** A matrix that is diagonal in the pair basis with entries $f_{k}-f_{l}$ is the commutator's action; a matrix with entries $\rho_{k}-\rho_{l}$ is the inertia. **Both are of the form "difference of eigenvalues", and a single map from diagonal matrices to pair-indexed matrices would produce both.** Whether such a map has a name and a use in the corpus is open.

## What This Article Adds and What It Relabels

**Adds.** The **trichotomy of couplings** by what each consumes — an algebra index, two spacetime indices, or nothing — with the index count as the discriminator; the **index-counting argument** that a contraction cannot return a matrix and therefore cannot stand where the balance's source stands; the **commutator as the unique candidate** among operations acting on an algebra element and returning one, with the anticommutator excluded by the derivation requirement and the abelian limit stated; the **cyclicity requirement** on the trace pairing, with the informational scalar's failure recorded and the commutator's automatic covariance as the contrast; the **two eigenvalue splittings** with the "inertia divides, force weight multiplies" rule and the explicit assignment of check C to one and check H to the other; the **four differences from Wong** as a logical chain; and the **six-line inventory** that a force block owes its reader.

**Does not add.** No new equation and no new residual. Checks C, H and I are the corpus's, and their assignments to statements are this article's reading.

**Relabels.** *"The matrix rung's force is a commutator with the field strength"* — it is a *source* in a balance, and "force" is the classical vocabulary continued by analogy. *"The charge is matrix-valued"* — there is no charge; the field's basis is the pair index, and that is why nothing can be contracted. *"The guidance weight and the force weight are the same splitting"* — one is the density's difference and divides, the other is the field's difference and multiplies.

## Summary

**Three couplings appear in and around the corpus, and they differ in what they consume.** Wong's equations contract an algebraic charge with the field strength by the trace pairing and get a covector force; the classical spinning particle contracts an internal two-form with the field's two-form and gets a scalar coupling; **the matrix rung contracts nothing, because its "charge" is the field's own basis, and what it uses instead is the commutator.**

**The contraction is unavailable for an index-counting reason.** The balance's source must be matrix-valued, and an operation that consumes the pair index cannot return a matrix. **The commutator consumes nothing: it takes two algebra elements and returns one, it is the algebra's inner derivation, and it is the only such operation the algebra supplies.** Its abelian limit is zero, which is why the matrix rung must be non-abelian for its source to be nonzero.

**The trace pairing's cyclicity is a real constraint, and the matrix rung does not face it.** Wong's force is covariant only if the pairing is invariant; the informational scalar fails and the Yang–Mills action therefore uses the trace; **the commutator is covariant by construction, because conjugation cancels in the product and its reverse.**

**Two eigenvalue splittings appear at the matrix rung, and they are not the same.** The inertia $q_{kl}=\rho_{k}-\rho_{l}$ is the density's difference and it divides; the force weight $f_{k}-f_{l}$ is the field's difference and it multiplies. **Check C witnesses the first and check H the second, and neither check tests the other.**

**The four differences from Wong form a chain — no charge, therefore no pairing, therefore a matrix source, therefore no cyclicity requirement — and the six-line inventory is what a force block owes its reader.** The matrix rung answers all six, and its verdict is a balance.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $Q$ | Wong's charge: a separate algebra element carried by the particle |
| $\mathbb F$, $f_{k}$ | the field strength, Hermitian, and its real eigenvalues |
| $\Xi=U_{\mathrm{frm}}PU_{\mathrm{frm}}^{\dagger}$, $P=\mathrm{diag}(\rho_{k})$ | the matrix rung's field and its density eigenvalues |
| $q_{kl}=\rho_{k}-\rho_{l}$ | the pair's inertia; the guidance relation's denominator |
| $f_{k}-f_{l}$ | the force weight; the commutator's eigenvalue |
| $[\mathbb F,\Pi]_{kl}=(f_{k}-f_{l})\Pi_{kl}$ | the inner derivation acting in the pair basis |
| $\langle\cdot,\cdot\rangle$ | a pairing; the trace where cyclicity is required |
| $S^{\mu\nu}$ | a classical spinning particle's internal two-form |

## Further Reading

- [The Primordial Force Law and the Two Wong Terms](the-primordial-force-law-and-the-two-wong-terms.html), where the balance is derived and the four differences are first stated.
- [The Yang–Mills Equation in Biquaternionic Form](the-yang-mills-equation-in-biquaternionic-form.html), the trace pairing and why the informational scalar is not cyclic.
- [The Algebraic Vocabulary](the-algebraic-vocabulary-element-conjugations-six-subspaces-and-two-ledgers.html), the commutator and the two pairings.
- [Differentiating a First-Order Transport Law](differentiating-a-first-order-transport-law-force-transport-and-product-rule-terms.html), where the commutator is identified as the transport term's general form.
- [Base-Valued versus Internal Flow Velocity](base-valued-versus-internal-flow-velocity-a-test-separating-force-laws-from-momentum-balances.html), the verdict that makes the matrix rung's equation a balance and not a law.
- [Five Steps from a Lagrangian to Fluid Equations](five-steps-from-a-lagrangian-to-fluid-equations.html), where this article's operation fills S4's force slot at the matrix rung.
