# __The Lagrangian and the Rarita–Schwinger Equation__

## Introduction

The plain statement, first. This family has the Rarita–Schwinger equation and it does not have the Rarita–Schwinger action. The parent, *The Rarita–Schwinger Equation: Spin 3/2 in Biquaternionic Form*, writes the equation, its two constraints, its rest-frame reduction and its redundancy; this article names the action that the literature uses, states what it must contain for the parent's results to follow from it, and records that the corpus does not write it.

Why an article about an absence. Because an absence that is not recorded is read as an oversight. A reader who has seen the Klein–Gordon, Dirac and Proca actions will expect the spin-$\tfrac32$ action to be the next article in the family, and it is not. This article says so, gives the reason, and states exactly what would have to be built for it to be written.

The reason, in one sentence. The algebra supplies a vector index as a family of four elements and it supplies the mass mixing through a fixed direction and a frame; the standard action's trace constraint needs a multiplier that contracts the vector index with the spinor structure, and no element of the algebra has been shown to do that job. Writing the action would require constructing that object, and this family has not constructed it.

What the article still does. It states the action's standard form by name; it lists the two multipliers the constraints require; it states the invariance the massless case demands; and it states what the action's Noether procedure would give, since those currents are known from the parent's equation and the action would have to reproduce them.

## Conventions

The conventions are the parent's, unchanged. The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_t=1$ and $\vec e_{\imath}^{2}=-e_t$; the field is a family $\tilde\Xi_{\imath}\in\mathbb{B}$ with $\mu=0,1,2,3$, each split into its two chiral parts; the gradient is $\tilde\nabla_\Phi$, its quaternion conjugate $(\tilde\nabla_\Phi)^{\natural}$, the d'Alembertian $\Box_\Phi$; $\nu_m=\frac{mc}{h}$; the sign vector of the frame is $\varepsilon=(1,-1,-1,-1)$; the fixed direction of the trace constraint is $\vec e_z$.

One symbol is used and not defined by this article. The literature's action is written with matrices that act on the spinor index. The parent's equation has no matrix, because the algebra's left and right multiplication supplies the action of the frame directly. Where this article names the standard action, it does so in the literature's notation and marks the matrices as unnamed, since their biquaternionic counterparts are the object the corpus has not built.

## The Action in Element Form: Named and Not Written

The standard action, named. In the literature the massive spin-$\tfrac32$ field's action is written with a vector-spinor $Ξ_{\mathrm{wfn},\imath}$, the Dirac matrices, and the object $\gamma_{\imath\jmath}=\frac{i}{2}[\gamma_{\imath},\gamma_{\jmath}]$:

$$
S_{\mathrm{RS}}=\int\mathrm{d}^{4}x\;\barΞ_{\mathrm{wfn},\imath}\Bigl(i\gamma_{\imath\jmath\rho}\partial_\rho-m\,\gamma_{\imath\jmath}\Bigr)Ξ_{\mathrm{wfn},\jmath} ,
$$

with the antisymmetrised product $\gamma_{\imath\jmath\rho}$. The literature prints these matrices with the index raised and this article prints every index low: the metric is the identity, so the two spellings name the same array and the action is the same functional. It is not written here in the algebra, and the box is a quotation of the literature's form rather than a formula of this corpus. The biquaternionic counterpart would replace $Ξ_{\mathrm{wfn},\imath}$ by $\tilde\Xi_{\imath}$, $\partial_\rho$ by $\tilde\nabla_\Phi$, and the matrices by elements of the algebra acting by multiplication — and it is the last replacement that has not been made.

What the action must contain for the parent's results to follow.

*First, the mass mixing between neighbouring vector indices.* The parent's massive equation couples the two chiralities of each component; the action's mass term must therefore contract the vector index with the spinor structure, and that contraction is the matrix's job.

*Second, two multipliers.* The parent's trace constraint and its divergence constraint are primary and secondary conditions of the equation; an action that reproduces them must carry a multiplier for each, and the multipliers are the object the corpus has not built.

*Third, the massless invariance.* The parent records the redundancy $\tilde\Xi_{\imath}\mapsto\tilde\Xi_{\imath}+\partial_{\imath}\epsilon$ at $\nu_m=0$. An action for the massless field must be invariant under it, which requires the field's trace to be absent from the action or removed by the first multiplier.

**What is missing, precisely.** One object: an element or a pair of elements of $\mathbb{B}$ that contracts the vector index with the field's chiral structure and is not simply the frame. The frame gives $\vec e_{\imath}$, which contracts a vector index with a direction; the trace constraint needs a contraction that mixes the two chiralities of the vector index itself, and this family has not exhibited one.

## The Variation That Cannot Be Performed Here

**The honest statement.** Since the action is not written in the algebra, its variation is not performed in the algebra. What can be stated is the shape the variation would have and the check it would have to pass.

The shape. Three variations: with respect to the field (giving the parent's pair of equations), with respect to the conjugate (giving the conjugate pair), and with respect to each multiplier (giving the two constraints). The first and second would be first order in the derivative, matching the parent's first-order form; the third would be algebraic, matching the constraints' algebraic character.

The check it would have to pass. The variation with respect to the field must produce the parent's pair *and* the parent's two constraints as its own consequences, not as extra postulates. If a candidate action produced the pair and left the constraints to be imposed by hand, it would not be the action of the parent's theory; it would be an action for a different theory whose solutions happen to satisfy the parent's equation.

Why the check is not optional. The spin-$\tfrac32$ equation has the well-known pathology that its constraints are needed to remove the lower-spin content, and an action that does not produce them describes more degrees of freedom than the parent's equation does. So the missing object is not a convenience: without it the count of degrees of freedom is wrong, and the count is what the next section but one is about.

## The Constraints the Action Imposes: The Constraints the Action Would Impose

**Two constraints, and they are the parent's.** The trace constraint $\tilde\Xi_0+\sum_{\imath\in\{x,y,z\}}\vec e_{\imath}\tilde\Xi_{\imath}\vec e_z=0$ and the divergence constraint $\sum_{\imath}\varepsilon_{\imath}\partial_{\imath}\tilde\Xi_{\imath}=0$ are the parent's statements. This section records what they do to the count, because the action's job is to produce them.

The count, in one line. Four vector components, each with two chiralities: eight complex data. The trace constraint removes two, the divergence constraint removes two, and the pair of first-order equations removes half of the rest; the rest frame leaves four complex parameters, the quartet the parent exhibits. An action that produced only the pair would leave the quartet's neighbours in place, and the count would be four higher.

The massless case. At $\nu_m=0$ the redundancy removes two more, and the physical count is the two helicities of a massless spin-$\tfrac32$ particle. The action's invariance under the phase shift is what makes the count come out right, and it is the third item in the action's list of debts.

What the constraints are not. They are not the Lorenz condition of the Proca article and not the phase continuity of the scalar: those remove a longitudinal mode of a vector, and these remove a vector-index trace. The difference is why the spin-$\tfrac32$ constraints need their own multipliers and cannot be inherited from the spin-one article.

## The Structural Consequence: The Absence Is the Article's Content

**The claim.** The family's ability to write an action is not uniform across the spins, and the boundary is at $\tfrac32$. For spins $0$, $\tfrac12$ and $1$ the corpus writes the action and derives everything from it. For spin $\tfrac32$ it writes the equation and not the action, and the reason is a missing contraction in the algebra and not a missing computation.

The hand check of the boundary. Compare the three actions this family has. The scalar's term is $\mathrm{Sc}[(\partial\tilde\Xi)^{*}\partial\tilde\Xi]$: one element, no index. The spinor's is $\mathrm{Sc}[\tilde\Xi_R^{*}\tilde\nabla\tilde\Xi_L]$: two chiral parts, still no index. The vector's is $\mathrm{Re}\,\mathrm{Sc}[\tilde F\tilde F]$, with $\tilde F$ built from the potential by the conjugate gradient: the index is carried by the gradient's vector part, and the contraction is the scalar part of a product. In each case the index is contracted by the algebra's own multiplication. For the vector-spinor the index must be contracted with a *fixed* direction and the chirality with a mass, and the algebra's multiplication cannot do both at once with the elements the corpus has.

What that means for the family's claims. Every statement of the form "the action has this equation as its Euler–Lagrange equation" is a statement about spins up to one. The spin-$\tfrac32$ article is the first member of the family for which the statement is not made, and saying so is more valuable than making it by analogy.

What the absence does not affect. The parent's equation, its constraints, its rest-frame reduction, its redundancy, and its comparison with spins one and one-half are independent of the action and remain. The family loses the variational derivation of those results, not the results.

## The Noether Currents That Are Known

Known from the equation, not from the action. The parent's comparison section records the currents the theory carries: the energy–momentum, which every relativistic field has, and the spin current of the vector index, which is the spin-$\tfrac32$ field's own. Their forms are the standard ones — the stress as the translation current and the spin as the antisymmetric moment — and the corpus can state them because they are fixed by the equation's symmetries and not by the action's details.

What the action would add. The Noether procedure would produce the same currents and would fix their normalisation relative to the action's normalisation. That is the one thing the equation cannot supply: a current is defined up to a constant, and the constant is the coupling in the action. So the currents are known in form and not in normalisation, and the corpus says so.

**The sign of the charge.** At $\nu_m=0$ the massless field's local symmetry is not a phase symmetry, so there is no charge and no sign to fix; the massive field has no redundancy and no charge either. The spin-$\tfrac32$ field is neutral in this corpus, and the sign question does not arise — which is one more respect in which it resembles the Proca field and not the Dirac field.

Why the section exists at all. Because a reader is entitled to know what survives the absence. The currents survive in form; the normalisation, the multiplier structure and the variational derivation do not.

## What the Principle Adds and What It Relabels: The Absence

It does not change the physics of the parent. The equation, the constraints, the quartet, the redundancy: all of it stands, and none of it was derived from an action.

**It changes the family's uniformity.** The claim "every member of this family is an Euler–Lagrange equation of a written action" is false, and the falsehood is at spin $\tfrac32$. The family hub records it in the completeness table, and the bridge article does not pretend otherwise.

It changes the ledger's honesty. An article that names an action it has not written, and states why, is more useful than an article that writes a plausible action by analogy and leaves the constraints unproduced. The second would look complete and be wrong at the degree-of-freedom count; the first looks incomplete and is right.

What would close it. One construction: an element of $\mathbb{B}$ that contracts the vector index with the chiral structure, with the trace constraint's multiplier expressed through it. Whether such an element exists is an open question, and the corpus does not answer it.

## Summary

This family has the Rarita–Schwinger equation and not its action. The standard action is named; its three debts are the index-chirality contraction, the two multipliers and the massless invariance; and the count of degrees of freedom is what those debts control. The currents survive in form and not in normalisation, and the spin-$\tfrac32$ field is neutral. The absence is the article's content, and it marks the boundary of the family's variational method at spin $\tfrac32$.

$$
\tilde\nabla_\Phi\tilde\Xi_{\imath,R}=2\pi\nu_m\tilde\Xi_{\imath,L},
\qquad
(\tilde\nabla_\Phi)^{\natural}\tilde\Xi_{\imath,L}=2\pi\nu_m\tilde\Xi_{\imath,R},
\qquad
\tilde\Xi_0+\sum_{\imath\in\{x,y,z\}}\vec e_{\imath}\tilde\Xi_{\imath}\vec e_z=0 .
$$

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\ \vec e_{\imath}^{2}=-e_t$ | Basis and its squares |
| $\tilde\Xi_{\imath}$ | Rarita–Schwinger field, four elements of $\mathbb{B}$ |
| $\tilde\Xi_{\imath,R},\ \tilde\Xi_{\imath,L}$ | The two chiral parts of each component |
| $\nu_m=\frac{mc}{h}$ | Mass wave number |
| $\vec e_z$ | Fixed direction of the trace constraint |
| $\varepsilon=(1,-1,-1,-1)$ | Sign vector of the frame |
| $Ξ_{\mathrm{wfn},\imath},\ \gamma_{\imath},\ \gamma_{\imath\jmath}$ | The literature's matrices, printed low and not adopted |
| $S_{\mathrm{RS}}$ | The standard action, named and not written |

## Further Reading

- *The Rarita–Schwinger Equation: Spin 3/2 in Biquaternionic Form*, the parent, for the equation, the constraints, the rest-frame reduction and the redundancy.
- *The Lagrangian and the Proca Equation*, for the spin-one action, whose index is contracted by the algebra's own multiplication and not by a multiplier.
- *The Lagrangian and the Dirac Equation*, for the spin-half action, whose mass needs the fixed direction and no index.
- William Rarita and Julian Schwinger, *On a theory of particles with half-integral spin*, Phys. Rev. 60 (1941), for the equation and the action.
- Pierre van Nieuwenhuizen, *Supergravity*, Phys. Rep. 68 (1981), for the constraints and the degree-of-freedom count.
