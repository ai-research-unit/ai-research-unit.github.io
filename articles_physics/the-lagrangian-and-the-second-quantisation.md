# __The Lagrangian and the Second Quantisation: From the Action to the Commutator__

## Introduction

The sentence this article exists to explain. The corpus's one-particle field articles state it: *it does not quantise: the fields are one-particle fields, and the second quantisation is the next category.* The Klein–Gordon, Dirac and Proca actions are one-particle actions; their fields are wavefunctions and not operators; there is no Fock space, no creation or annihilation operator, no interacting quantum field theory and no Standard Model. This article describes the route from the one-particle action to the quantised theory, states exactly which step the corpus takes and which it does not, and stops where the corpus stops.

Why a bridge article at all. Because an absence that is not described is indistinguishable from an oversight, and because a reader who has the actions and not the quantisation is entitled to know what the missing step consists of. The bridge is not a derivation of a quantum field theory. It is a map of the step, with its two classical ingredients and its one quantum postulate, and with an honest ledger of what the corpus would need to build before any of the field articles' results could be called quantum.

The route in four steps. First, the action's quadratic form is inverted: its retarded and advanced Green functions exist and their difference defines the Peierls bracket, a classical bracket on the space of solutions. Second, when the action has constraints — the Proca field, the first-order Dirac field, every connection theory — the bracket is replaced by the Dirac bracket, which is the same construction after the constraints are solved. Third, the promotion: the bracket is replaced by a commutator, $\{\,,\,\}\to\frac{1}{i \frac{h}{2\pi}}[\,,\,]$, and the field becomes an operator. Fourth, the completion: the operator algebra is represented on a Fock space, and that representation is where particles, the vacuum and the $S$-matrix live.

Which step this family takes. The first, in the sense that every action in the family is quadratic and its Green functions are computable; and part of the second, in the sense that the constraints are counted and stated in the spin-one and first-order articles. It does not take the third and it does not take the fourth. No article of the family promotes a bracket; none writes a commutator between fields as a postulate; none constructs a Fock space.

What the corpus has elsewhere, stated so that this article is not read as a denial. The corpus carries a separate quantum-fields category, whose articles do perform the promotion, write the commutators and construct the Fock space, and a particle-physics category that transcribes the Standard Model. Those articles import the quantisation and apply it to the biquaternion form; they do not derive it from this family's actions, and none of them is an article of this family. So the boundary drawn here is a boundary of the variational series and not of the corpus, and the distinction is the subject of `articles_internal/internal-note-on-quantum-field-theory-in-the-corpus.md`.

What this article is not. It is not a derivation of the promotion — the promotion is a postulate and Dirac's, not this corpus's. It is not a path integral — the corpus's path integral is sketched elsewhere and this article does not use it. And it is not a shortcut: a reader who wants a scattering amplitude will not find one here, because a bridge is not a destination.

## Conventions

The conventions are the family's, and one more. The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$; the actions are the family's, element-form or chart-form as the article in question writes them; $\frac{h}{2\pi}$ is the constant that converts an action's units into a rate; $\nu_m=\frac{mc}{h}$; the measure is $\mathrm{d}^{4}r$; the pairing is the one the field's article uses.

The addition is the bracket's notation. For a field $\xi_{\mathrm{pot}}$ and its conjugate $\pi$ — in the corpus's terms the two members of the conjugate pair — the equal-time bracket is written $\{\xi_{\mathrm{pot}}(\vec r),\pi(\vec r')\}=\delta^{3}(\vec r-\vec r')$, and the general bracket of two functionals is written $\{F,G\}$. The Green functions are $G_{R}$ (retarded: support in the forward cone) and $G_{A}$ (advanced: support in the backward cone), and the fundamental object of the Peierls construction is their difference $G=G_{R}-G_{A}$, whose support is the full light cone.

**One symbol is a postulate and is marked.** The promotion's symbol is $\frac{1}{i \frac{h}{2\pi}}[\,,\,]$. Everything to its left is classical and derivable from the actions the corpus has; everything to its right is a new axiom. The article marks the boundary once, here, and does not blur it below.

## The Action in Element Form: The Point of Departure

The starting point is a quadratic action, and the family has ten of them. Each is of the form

$$
S[\xi_{\mathrm{pot}}]=\tfrac12\int\mathrm{d}^{4}r\;\xi_{\mathrm{pot}}\,\mathcal{D}\,\xi_{\mathrm{pot}}+\text{(linear terms in the sources)},
$$

with $\mathcal{D}$ a differential operator: $\Box_\Phi-4\pi^{2}\nu_m^{2}$ for the scalar, the first-order Dirac operator for the spinor, the Proca operator $\Box_\Phi-4\pi^{2}\nu_m^{2}$ on the transverse part for the vector, and their coupled versions with the connection inside the covariant derivative.

What quadratic means here, and why it is the whole of the family's classical content. A quadratic action has linear equations, so its solutions superpose; it has a Green function, so its response to a source is computable; and it has a bracket, so its symplectic structure is well defined. All three are classical and all three are in the corpus. What a quadratic action does *not* have is a scattering: with no interaction there is nothing to scatter, and the corpus's interacting article stops at the exact classical equation for the same reason.

**What the action supplies and what it does not.** It supplies the operator $\mathcal{D}$, its Green functions, its constraints and its Noether currents. It does not supply a Hilbert space, an operator algebra, a vacuum or a particle. Those are the quantisation's, and the next three sections say what they would consist of.

The first-order case. For the Dirac action the operator is first order and the conjugate momentum is a bilinear of the field rather than its own derivative; the article's *The Conjugate Pair* is the classical statement of that, and it is why the promotion of a first-order action needs the Dirac bracket rather than the Poisson one.

## The Variation: The Peierls Bracket

The construction, in three lines. Let $G_{R}$ and $G_{A}$ be the retarded and advanced Green functions of $\mathcal{D}$, fixed by the boundary conditions that a source switched on at a time affects the field only after it (retarded) or before it (advanced). Then

$$
G=G_{R}-G_{A},
\qquad
\{\xi_{\mathrm{pot}}(x),\xi_{\mathrm{pot}}(y)\}=G(x,y),
$$

is the Peierls bracket: the difference of the two Green functions is the classical bracket of the field with itself. For a conjugate pair the same construction gives $\{\xi_{\mathrm{pot}}(x),\pi(y)\}=\partial_{y_0}G(x,y)$, and at equal times that is a delta function.

The hand check for the scalar. For $\mathcal{D}=\Box_\Phi-4\pi^{2}\nu_m^{2}$ the difference of the Green functions is the Pauli–Jordan function,

$$
G(x,y)=\int\mathrm{d}^{3}\nu_{\Phi}\;\frac{\sin\bigl(\omega_{\mathrm{mode},m}\,\Delta r'{}^{0}/c\bigr)}{\omega_{\mathrm{mode},m}}\,e^{2\pi i\vec\nu_{\Phi}\cdot(\vec r-\vec r')},
\qquad
\omega_{\mathrm{mode},m}=c\sqrt{4\pi^{2}\nu_{\Phi}^{2}+4\pi^{2}\nu_m^{2}},
$$

which vanishes at $\Delta r'{}^{0}=0$ and whose time derivative there is $\delta^{3}(\vec r-\vec r')$. So $\{\xi_{\mathrm{pot}}(\vec r),\xi_{\mathrm{pot}}(\vec r')\}=0$ and $\{\xi_{\mathrm{pot}}(\vec r),\pi(\vec r')\}=\delta^{3}(\vec r-\vec r')$: the canonical bracket is *derived* from the action's Green functions, not assumed. That derivation is the first step of the route, and it is the one the corpus's quadratic actions make available.

**Why the bracket and not the Poisson bracket of the momenta.** The Peierls bracket is defined on solutions and not on initial data, so it is invariant under field redefinitions and it exists even when the naive Legendre transform is degenerate. For the corpus's first-order actions that is not a convenience but a necessity: the momenta are constrained, and the naive bracket would be inconsistent.

What the construction needs that the corpus has. The Green functions of each action. The family's articles compute them or state their form in momentum space; the momentum-space articles are where the propagators appear, and they appear there as Green functions and not as quantum propagators. The distinction is the whole of this article.

## The Constraints the Action Imposes: The Dirac Bracket

Constraints, and the bracket they force. When the action is first order or has a local symmetry, the Legendre transform does not invert and the naive bracket is inconsistent on the constraint surface. Dirac's construction replaces it: solve the constraints, or fix their representatives, and define

$$
\{F,G\}_{D}=\{F,G\}-\{F,\chi_a\}\,(C^{-1})_{ab}\,\{\chi_b,G\},
$$

with $\chi_a$ the constraints and $(C^{-1})_{ab}$ the inverse of their bracket matrix. The result is a bracket that is consistent on the reduced space.

**Where the family's constraints are.** Three places. The Proca field's Lorenz condition, which is a constraint on the vector's longitudinal part and is what removes it. The Dirac field's first-order structure, whose conjugate momenta are bilinears and whose bracket is the Dirac bracket of the spinor's components. And every connection theory's Gauss law, which is the constraint in the Maxwell, the electroweak and the linearised-gravity articles.

What the bracket does to the count. It removes the constrained pairs from the phase space, so the count of degrees of freedom becomes the count the field articles state: two for the massless vector, three for the massive one, two for the graviton, one for the scalar. The bracket's job is to make the count a *phase-space* statement and not just a component count, and that is what a quantisation needs.

What this family does with this step. It states the constraints and counts with them; it does not construct the Dirac bracket. So the second step is half-taken: the inventory is complete, the construction is not performed. A reader should read the constraints articles as the prerequisites of this step and not as its execution.

## The Structural Consequence: The Promotion Is One Substitution, and It Changes What the Symbols Mean

The claim. The step from classical to quantum is a substitution of the bracket, $\{\,,\,\}\to\frac{1}{i \frac{h}{2\pi}}[\,,\,]$, applied to the fields themselves. It is one line, and it changes every symbol it touches: a field that was a function of position becomes an operator-valued distribution; a bracket that was a classical product becomes a commutator; a solution becomes a state.

The hand check. Take the scalar's derived bracket and substitute:

$$
\{\xi_{\mathrm{pot}}(\vec r),\pi(\vec r')\}=\delta^{3}(\vec r-\vec r')
\quad\longrightarrow\quad
[\hat\xi_{\mathrm{pot}}(\vec r),\hat\pi(\vec r')]=i \frac{h}{2\pi}\,\delta^{3}(\vec r-\vec r').
$$

Then expand $\hat\xi_{\mathrm{pot}}$ in the modes of the free action, $\hat\xi_{\mathrm{pot}}=\sum_{\imath}(a_{\imath} u_{\imath}+a_{\imath}^{\dagger}u_{\imath}^{*})$, and the commutator forces $[a_{\imath},a_{k'}^{\dagger}]=\delta_{kk'}$: the mode coefficients become creation and annihilation operators. The Fock space is the representation of that algebra, and the vacuum is the state annihilated by every $a_{\imath}$. Four lines, and every one of them is absent from the corpus.

Why the substitution is a postulate and not a theorem. No classical statement forces it: the bracket's algebraic properties are consistent with many deformations, and the promotion is selected by its agreement with experiment and by its consistency, not by a derivation from the action. A reader who expects the promotion to follow from the variational principle will not find it there, and the corpus would be wrong to pretend otherwise.

What the substitution does not do by itself. It does not define the Hilbert space's inner product, does not order the operators in an interacting theory, does not remove the ultraviolet divergences, and does not produce the $S$-matrix. Those are the fourth step's problems, and the corpus has none of them in any form.

What the claim forbids. **It forbids calling the family's articles quantum.** An action whose bracket has not been promoted is classical, however quantum its notation looks; a propagator that is a Green function of a classical operator is not a Feynman propagator until the time ordering is imposed by the promotion; and a current that is a bilinear of a classical field is not an operator until the field is. The corpus's language is careful about this, and this article is where the care is explained.

## The Noether Currents After Promotion

What would become an operator. The charge, $Q=\int\mathrm{d}^{3}r\,j_{r'_t}$, becomes an operator on the Fock space, and its eigenvalues are the integers — for the complex scalar and the Dirac field, whose phase symmetry is compact. The corpus's free articles compute the current and its sign; the promotion would make the sign a label on a state and the current an operator whose commutator with the field shifts the phase.

**The statement this family can make and does not.** That the charge's quantisation to integers is a consequence of the compactness of the phase symmetry and of the promotion, and not an independent postulate. It is a one-line consequence of the mode expansion above, and it is not in the corpus because the mode expansion is not.

What the stress becomes. An operator whose expectation value in a state is the state's energy. The family's stress is a classical bilinear; the promotion would make its normal ordering a new problem, because the vacuum's energy is infinite without it. That problem is the first of the renormalisation's, and the corpus does not have it.

The sign of the charge, one more time. The family fixes the sign convention in the conventions sections and never in a result: the sign is a convention on $q$ and on the phase's orientation. After promotion the sign becomes a physical label, but the convention that fixes it remains the convention. A reader who confuses the two will think the corpus derived a sign it merely fixed.

The honest ledger. Nothing in this section is a result of this family. It is the shape of what the next category would produce, stated so that the family's articles' silence on it is legible as a boundary and not as an omission.

## What the Principle Adds and What It Relabels: The Bridge

Adds. A name for the gap, a four-step map of it, and the identification of the classical half the family actually completes: the Green functions, the constraints, the count. That identification is the article's value. A reader can now say exactly what is missing — the promotion and the representation — instead of saying that the corpus "does not quantise".

Relabels. Nothing in the family's results. The classical brackets, once derived, are the same brackets the articles use implicitly when they state a conjugate pair; the constraints are the articles' constraints; the counts are the articles' counts.

What a quantised theory would add, item by item. The Fock space and its vacuum; the mode expansions with their creation and annihilation operators; the time-ordered propagators, which differ from the corpus's Green functions by the ordering; the interaction picture and the perturbative expansion; the $S$-matrix; the ultraviolet divergences and their renormalisation; the running couplings; and, for the connection theories, the ghosts and the BRST structure. Each item is a chapter of a textbook and a sentence of this article, and the disproportion is the point.

**The boundary, stated once.** This family is a series of classical one-particle actions with an exact variational structure. It is not a quantum field theory, it does not claim to be, and its articles say so in their first sections. This article is the longest statement of that sentence, and its length is a measure of how much a reader is entitled to know about a gap.

## Summary

The route from a one-particle action to a quantum field theory has four steps: the Peierls bracket from the action's Green functions, the Dirac bracket for the constrained cases, the promotion of the bracket to a commutator, and the representation on a Fock space. This family completes the first, inventories the second, and takes neither the third nor the fourth. The classical brackets it can derive are the ones its articles use; the fields it writes are wavefunctions and not operators; the propagators it computes are Green functions and not Feynman propagators. The absence is stated in the family's own words and mapped here, so that it is a boundary with a name.

$$
\{\xi_{\mathrm{pot}}(\vec r),\pi(\vec r')\}=\delta^{3}(\vec r-\vec r')
\qquad\longrightarrow\qquad
[\hat\xi_{\mathrm{pot}}(\vec r),\hat\pi(\vec r')]=i \frac{h}{2\pi}\,\delta^{3}(\vec r-\vec r')
\qquad\longrightarrow\qquad
[a_{\imath},a_{k'}^{\dagger}]=\delta_{kk'} .
$$

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\xi_{\mathrm{pot}},\ \pi$ | Field and its conjugate |
| $\mathcal{D}$ | The quadratic action's differential operator |
| $G_{R},\ G_{A}$ | Retarded and advanced Green functions |
| $G=G_{R}-G_{A}$ | Pauli–Jordan function, the bracket's kernel |
| $\{\,,\,\}$ | Classical bracket (Peierls, or Dirac when constrained) |
| $\chi_a,\ (C^{-1})_{ab}$ | Constraints and the inverse of their bracket matrix (Dirac bracket) |
| $\frac{1}{i \frac{h}{2\pi}}[\,,\,]$ | The promotion's commutator |
| $a_{\imath},\ a_{\imath}^{\dagger}$ | Annihilation and creation operators, after promotion |
| $\lvert 0\rangle$ | The vacuum, annihilated by every $a_{\imath}$ |
| $Q=\int j_{r'_t}$ | Charge, an operator after promotion |

## Further Reading

- The family's spin-one articles — *The Lagrangian and the Proca Equation* and *The Lagrangian and the Electromagnetic Field* — for the constraints the Dirac bracket would use.
- *The Lagrangian and the Dirac Equation* and its polar companion, for the first-order structure and the conjugate pair.
- The momentum-space articles of each field, for the Green functions that the Peierls construction inverts.
- Paul A. M. Dirac, *The Principles of Quantum Mechanics*, for the promotion as a postulate and for the bracket.
- Bryce S. DeWitt, *Dynamical Theory of Groups and Fields*, for the Peierls bracket and its covariance.
- Rudolf Peierls, *The commutation laws of relativistic field theory*, Proc. R. Soc. A 214 (1952), for the original construction.
- Michael E. Peskin and Daniel V. Schroeder, *An Introduction to Quantum Field Theory*, for the four steps and for everything the corpus does not have.
- The corpus's six canonical-quantisation articles — [Klein–Gordon](canonical-quantization-of-the-biquaternion-klein-gordon-field.html), [Dirac](canonical-quantization-of-the-biquaternion-dirac-field.html), [Proca](canonical-quantization-of-the-biquaternion-proca-field.html), [Maxwell](canonical-quantization-of-the-biquaternion-maxwell-field.html), [Rarita–Schwinger](canonical-quantization-of-the-biquaternion-rarita-schwinger-field.html) and [graviton](canonical-quantization-of-the-biquaternion-graviton-field.html) — for the imported promotion this article locates and does not perform.
