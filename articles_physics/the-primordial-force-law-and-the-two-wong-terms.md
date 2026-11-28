# The Primordial Force Law: Differentiating the Guidance Equation, and the Two Wong Terms

*An article of the Biquaternion Universe — this rung's instance of *From the Field Equation to the Force*, the force section of *Biquaternion Universe Action*. It takes the step the corpus takes at every charged rung — differentiate the first-order statement and read the force — and takes it at the primordial rung, where the first-order statement is not a mass shell but a guidance equation for the internal frame. The result is an exact identity, checked numerically to $5\times10^{-8}$ on $O(1)$ data, and a verdict that splits: the fluid's force slot has the shape of Wong's force term, with four differences the article names, the deepest being that the object acted on is a matrix; its precession lives on the frame in the fundamental and on the vorticity in the adjoint; and neither is on the densities, where it cannot be.*

## Introduction

**Every charged rung of this block derives its force the same way, and the move is one line.** The action gives a second-order equation for the amplitude; the amplitude's polar form turns one combination of it into a first-order statement — a mass shell, an eikonal, a guidance equation — and **differentiating that statement produces the Lorentz force as something that was not in the action.** *Relativistic Mechanics from the Dirac Wave* states it in one sentence: "The gradient is the Lorentz force." *Charged Klein–Gordon* states the same from the other side: "A reader who wants the Lorentz force as a displayed term will not find it here, and the reason is that it is not a term: it is what the mechanical momentum does when the mass shell is differentiated."

**At the primordial rung the chain has no mass shell, and this article's first job is to find what replaces it.** The action is second order in the four eigenvalues, so their equations are already second order and carry no first integral of the mass-shell kind. What *is* first order is the transport identity of the eigenvalue chart: the off-diagonal part of the frame-covariant derivative of $\Xi$ is the frame's velocity times the density splitting,

$$
\Omega_{\imath,kl}=\frac{\bigl[U_{\mathrm{frm}}^{\dagger}D_{\imath}\Xi\,U_{\mathrm{frm}}\bigr]_{kl}}{\rho_{l}-\rho_{k}},\qquad k\ne l,
$$

and that is the guidance equation of this rung. **It says what the Madelung guidance equation says**: the velocity is the field's own covariant gradient, divided by an inertia. The inertia here is the splitting $\rho_{k}-\rho_{l}$, and this article calls it the pair's charge.

**The second job is the differentiation, and it does not go the way the abelian rungs go.** There the second-derivative terms cancel because partials commute; here they do not, and **what survives the attempted cancellation is the curvature** — the non-abelian force term, which the article shows to be a *three-species* effect: exact at two species to $5.6\times10^{-17}$, present at three.

**The third job is the comparison with Wong, and it splits in two.** Wong's equations are a force and a precession:

$$
m\frac{dv^{\mu}}{d\tau}=g\,F^{\mu\nu}_{a}q^{a}v_{\nu},\qquad \frac{dq_{a}}{d\tau}=-g\,f_{abc}\,v^{\mu}A_{\mu}^{b}q^{c}.
$$

**The fluid has the first**, as the commutator term, with the pair label as the charge. **The fluid has the second in the fundamental representation and not the adjoint**: the object carrying the pair's charge is the frame's column, and the frame is parallel-transported, so the charge's transport is the precession. **The adjoint version exists too, on the vorticity**, whose ordinary divergence fails by $-g_{4}f_{abc}A_{b,\imath}F_{c,\imath\jmath}$ — Wong's structure with the vorticity as the charge. **Neither Wong equation lives on the densities**, which are gauge-invariant eigenvalues and cannot precess — **though they are not inert, because the diagonal sector carries a centrifugal force**; the sector split is §*The Two Wong Terms*' central result.

**What this article is not.** It is not a derivation of Wong's equation from the primordial action, and it is not a claim that the primordial fluid *is* a test particle. Wong's equations are those of a point charge with a colour label moving in a background; the primordial fluid is the background. What is derived is the fluid's own pair-momentum balance, and the finding is how much of Wong's structure that balance contains, and where it stops.

## The Chain, and the Step That Changes

**At the charged rungs the chain has four links, and the corpus has all four.** The action; the field equation; the polar decomposition, which splits the field equation into a density equation and a phased statement; and the derivative of the phased statement, which is the force. *Charged Schrödinger* and *Charged Klein–Gordon* run all four, and both end with the same honesty: the force is not a term in the action but a consequence of differentiating.

**The primordial rung has the first three links and lacks the fourth's starting point.** Its action is *The Lagrangian and the Primordial Force*'s, seven terms on one coupling; its field equation is three equations — the connection's, the fermions', and $\Xi$'s; and its polar decomposition is the eigenvalue chart, $\Xi=U_{\mathrm{frm}}PU_{\mathrm{frm}}^{\dagger}$ with four densities and a frame. **What it does not have is a phased statement to differentiate**, and the reason is structural rather than technical: the phase is not a coordinate at this rung.

**The phase is quotiented, not merely awkward.** The word's stabiliser is $\mathrm{U}(1)^{4}$ — the four diagonal phases leave $\Xi$ unchanged — so the frame has twelve physical parameters and not sixteen, and there is no phase coordinate whose variation could give a guidance equation of the Madelung kind. **This is the same fact that makes continuity an identity at this rung**, stated in *What Is a Fluid Equation in the Biquaternion Universe* among the two collapses of the phase: Proca's collapse is discrete, this one is a quotient, and both remove the coordinate.

**So the first-order statement has to be found elsewhere, and it is already in the chart.** The chart's computation reads, in one line,

$$
U_{\mathrm{frm}}^{\dagger}\bigl(D_{\imath}\Xi\bigr)U_{\mathrm{frm}}=\partial_{\imath}P+[\Omega_{\imath},P],
\qquad
\Omega_{\imath}=U_{\mathrm{frm}}^{\dagger}D_{\imath}U_{\mathrm{frm}},
$$

and with $[\Omega_{\imath},P]_{kl}=\Omega_{\imath,kl}(\rho_{l}-\rho_{k})$ the identity separates into a diagonal part, the densities' gradients, and an off-diagonal part, the flow times the splitting. **The diagonal part is the density equation's gradient; the off-diagonal part carries no derivative of $\Xi$ and can be solved for $\Omega$.** That solution is a guidance equation, and it is first order.

**Why the diagonal part cannot serve.** $\partial_{\imath}\rho_{k}$ is not a velocity and cannot be one: it is the gradient of a scalar, so it is a covector of the base, and at this rung the flow is internal. **The matrix identity assigns the base-derivative to the densities and the internal rotation to the off-diagonal entries**, and that assignment is the chart's own statement that the fluid's flow is not a vector of the material sector but a rotation of the frame over it.

## The Guidance Equation of the Primordial Rung

**The equation, and its two readings.**

$$
\Omega_{\imath,kl}=\frac{\bigl[U_{\mathrm{frm}}^{\dagger}D_{\imath}\Xi\,U_{\mathrm{frm}}\bigr]_{kl}}{\rho_{l}-\rho_{k}},\qquad k\ne l .
$$

**That $\Omega_{\imath}$ is anti-Hermitian is one line, and the article gives it rather than asserting it.** From $U_{\mathrm{frm}}^{\dagger}U_{\mathrm{frm}}=\mathbb{1}$, differentiating gives $\partial_{\imath}U_{\mathrm{frm}}^{\dagger}\,U_{\mathrm{frm}}=-U_{\mathrm{frm}}^{\dagger}\partial_{\imath}U_{\mathrm{frm}}$, so $\bigl(U_{\mathrm{frm}}^{\dagger}\partial_{\imath}U_{\mathrm{frm}}\bigr)^{\dagger}=-U_{\mathrm{frm}}^{\dagger}\partial_{\imath}U_{\mathrm{frm}}$; and $-ig_{4}U_{\mathrm{frm}}^{\dagger}A_{\imath}U_{\mathrm{frm}}$ is anti-Hermitian because $A_{\imath}$ is Hermitian and conjugation preserves that. Summing the two, $\Omega_{\imath}^{\dagger}=-\Omega_{\imath}$. **The consequence used throughout is that $\Omega_{\imath,kk}$ is purely imaginary and $\Omega_{\imath,kl}$ and $\Omega_{\imath,lk}$ are conjugates up to sign**, which is why the twelve off-diagonal entries carry twelve real conditions and not twenty-four.

*As a guidance equation.* The frame's rotation in the $\imath$ direction is the field's own covariant derivative in that direction, resolved in the eigenbasis and divided by the splitting. **The numerator is a momentum and the denominator an inertia**, exactly as $\vec v=\vec\pi/m$ is, and the analogy is not decorative: the splitting is what the action weighs the flow's kinetic energy by, $g_{4}^{2}(\rho_{k}-\rho_{l})^{2}\lvert\Omega_{\imath,kl}\rvert^{2}$, so the splitting *is* the inertial coefficient of the pair's motion.

*As a count.* Twelve entries $k\ne l$, each complex — one complex entry per unordered pair, six pairs, two real conditions each, twelve. **The four diagonal phases are not determined**, and cannot be, being quotiented. So the guidance equation fixes exactly the twelve physical frame parameters and leaves the four quotiented ones free, and **what agrees with the stabiliser is the equation's domain, not its output**: twelve entries to fill, twelve parameters to fix, one number from two directions. The equation does not *derive* $16-4$; it *consumes* it, and the fact that it can consume exactly it is the cross-check. **Said plainly: $16-4=12$ is the stabiliser's count, the equation's domain is the same twelve, and the agreement is a consistency check rather than a proof of either.**

**One warning about the word "equation", because the analogy with Madelung earns it and then overspends it.** The Madelung guidance equation is *derived*: the wave equation is factored and one combination of it becomes first order. Here nothing is factored — the display above *is* the chart's transport identity, solved for $\Omega$, and it holds whether or not $\Xi$ satisfies any field equation. **So it is a definition, not an equation to solve**: it determines the off-diagonal flow in terms of the field and the frame, and its work in this article is the count below and the starting point for the differentiation. The equation of motion is the differentiated balance of §*The Differentiated Guidance Equation*; that is where the content is.

**Two consequences, and the second is a warning.**

*First, a degenerate pair has no flow.* If $\rho_{k}=\rho_{l}$ the denominator vanishes while the numerator need not, so $\Omega_{\imath,kl}$ is undetermined and the identity's off-diagonal entry becomes a constraint rather than a definition: **a species with an exactly degenerate partner has no flow of its own, because the frame's labelling of the pair is not physical.** *Second, the equation is singular exactly where the theory is most symmetric* — the vacuum $P_{0}=\mathrm{diag}(v,v,v,-3v)$ has three degenerate pairs, so six of the twelve parameters are fixed and six are left to the constraint. **The chart's "six heavy vectors and six eaten directions" is therefore not an accident of the potential but the guidance equation's rank deficiency at the vacuum**, and the two counts agree because they are one fact.

**What the equation does not say.** It does not say the flow is a gradient of anything, and it does not say the flow is curl-free. $\Omega_{\imath}$ is a connection, its curl is a curvature, and the next two sections are about what happens when that curvature is differentiated.

## The Lemma: Differentiating the Momentum

**Define the frame-covariant momentum of the $\imath$ direction,**

$$
M_{\imath}:=U_{\mathrm{frm}}^{\dagger}\,D_{\imath}\Xi\,U_{\mathrm{frm}}=\partial_{\imath}P+[\Omega_{\imath},P],
\qquad
M_{\imath,kl}=-\bigl(\rho_{k}-\rho_{l}\bigr)\Omega_{\imath,kl},
$$

**and write the pair's momentum per unit charge as $\Pi_{\imath,kl}:=(\rho_{k}-\rho_{l})\Omega_{\imath,kl}=-M_{\imath,kl}$.** The diagonal of $M$ is the density's gradient, $\partial_{\imath}\rho_{k}$; the off-diagonal is minus the pair momentum; nothing is left over.

**The lemma, one line of algebra with a two-line proof.**

$$
\partial_{\jmath}M_{\imath}=U_{\mathrm{frm}}^{\dagger}\,D_{\jmath}D_{\imath}\Xi\,U_{\mathrm{frm}}-[\Omega_{\jmath},M_{\imath}].
$$

*Proof.* Write $\Gamma_{\imath}:=U_{\mathrm{frm}}^{\dagger}\partial_{\imath}U_{\mathrm{frm}}$ and $B_{\imath}:=U_{\mathrm{frm}}^{\dagger}A_{\imath}U_{\mathrm{frm}}$, so $\Omega_{\imath}=\Gamma_{\imath}-ig_{4}B_{\imath}$. Differentiating the definition of $M_{\imath}$ and using $\partial_{\jmath}U_{\mathrm{frm}}=U_{\mathrm{frm}}\Gamma_{\jmath}$ gives

$$
\partial_{\jmath}M_{\imath}=U_{\mathrm{frm}}^{\dagger}\,\partial_{\jmath}\bigl(D_{\imath}\Xi\bigr)U_{\mathrm{frm}}-\Gamma_{\jmath}M_{\imath}+M_{\imath}\Gamma_{\jmath},
$$

and $\partial_{\jmath}D_{\imath}\Xi=D_{\jmath}D_{\imath}\Xi+ig_{4}[A_{\jmath},D_{\imath}\Xi]$. Conjugating that commutator gives $ig_{4}[B_{\jmath},M_{\imath}]$, so the last three pieces are $ig_{4}[B_{\jmath},M_{\imath}]-[\Gamma_{\jmath},M_{\imath}]=-[\Omega_{\jmath},M_{\imath}]$. $\square$

**The lemma says what a derivative of a frame component costs.** The rate of the momentum, measured in the frame, is the field's own second covariant derivative plus the frame's rotation acting on the momentum. **The second term is the price of differentiating in a basis that moves**, and at the abelian rungs the analogous term is the connection acting on the charge.

**It is checked, not asserted.** Nine identities were tested on random $4\times4$ data — a random Hermitian $\Xi$, a frame trajectory $U_{\mathrm{frm}}(t)=e^{tK}$ with $K$ random anti-Hermitian, a connection linear in $t$, and $g_{4}=0.7$ — by centred differences at step $10^{-4}$ on both nested levels:

| check | what it tests | residual |
| --- | --- | --- |
| A | the chart identity, $M_{\imath}=\partial_{\imath}P+[\Omega_{\imath},P]$ | $5.6\times10^{-8}$ |
| B | the lemma, $\partial_{\jmath}M_{\imath}=\widehat{D_{\jmath}D_{\imath}\Xi}-[\Omega_{\jmath},M_{\imath}]$, on $O(1)$ data | $1.2\times10^{-7}$ |
| C | the entry form, $M_{\imath,kl}=(\rho_{l}-\rho_{k})\Omega_{\imath,kl}$ | $3.7\times10^{-8}$ |
| D | the pair support of $[\Omega_{\jmath},M_{\imath}]_{kl}$ at **two** species | $5.6\times10^{-17}$ |
| E | the same at **three** species | $1.4\times10^{-9}$, on $0.48$ of structure |
| F | the differentiated guidance equation, on data of size $0.6$ | $4.5\times10^{-8}$ |
| G | gauge invariance of the composite connection, $U_{\mathrm{frm}}\to VU_{\mathrm{frm}}$ with $A_{\imath}\to VA_{\imath}V^{\dagger}-\tfrac{i}{g_{4}}(\partial_{\imath}V)V^{\dagger}$ | $8.6\times10^{-9}$ |
| H | the spectral face of the force term, $-ig_{4}[\mathbb{F},\Xi]_{kl}=-ig_{4}(f_{k}-f_{l})\Xi_{kl}$ in the eigenbasis of $\mathbb{F}$ | $9.2\times10^{-16}$ |
| I | the **premise** of H: $\mathbb{F}$ built from $A$ is Hermitian, $[D_{\jmath},D_{\imath}]\Xi=-ig_{4}[\mathbb{F}_{\jmath\imath},\Xi]$, and its eigenvalues are real | $0$ (Hermiticity), $2.8\times10^{-12}$ (commutator) |

**Rows D and E are the interesting ones and are the subject of §*The Residue Is a Three-Species Effect***; A–C and F are the algebra of this section, and G is the statement that makes $\Pi$ an invariant rather than a covariant object — **the point on which §*The Two Wong Terms, in Two Sectors* turns**.

**The residuals are $\max_{k<l}\lvert(\text{left side})-(\text{right side})\rvert$ over the pair entries, evaluated at one point of the random data** — a maximum modulus and not a Frobenius norm, so a residual of $5.6\times10^{-8}$ on data of size $O(1)$ is eight digits of agreement in every entry separately. **Row E's $0.48$ is not a ratio: it is $\max_{k<l}\bigl\lvert[\Omega_{\jmath},M_{\imath}]_{kl}\bigr\rvert$ itself**, the size of the object whose pair support is under test. The misclosure is therefore $1.4\times10^{-9}$ against an object of magnitude $0.48$, a relative $3\times10^{-9}$ — nine digits — and the row is a statement that the third-species contribution is present at the $10^{-9}$ relative level and not absent at the $10^{-16}$ level of row D.

**The honesty about the check, in the three places it earns the word.**

*The first is numerical, and the first attempt failed for a reason worth naming.* Checks B and F differentiate a quantity that is itself a derivative, so the outer central difference divides by $h_{\mathrm{out}}$ a difference of two inner differences taken at step $h_{\mathrm{in}}$. **If $h_{\mathrm{in}}\ll h_{\mathrm{out}}$ the inner round-off, $\epsilon/h_{\mathrm{in}}$, is amplified by $1/h_{\mathrm{out}}$ and lifts the residual floor to $O(h_{\mathrm{in}}/h_{\mathrm{out}})$** — which is what the first version of the script did, returning $O(1)$ on the lemma. **Both steps are now $10^{-4}$**: outer truncation $O(h^{2})\sim10^{-8}$, inner round-off $\epsilon/h\sim10^{-12}$, four decades apart, and the table's residuals sit at that floor and not at a physics scale.

*The second is a convention trap that check G caught, and it is the same trap as check F's.* The first attempt had the wrong sign in $A$'s transformation — $+\tfrac{i}{g_{4}}(\partial_{\imath}V)V^{\dagger}$ instead of $-\tfrac{i}{g_{4}}(\partial_{\imath}V)V^{\dagger}$ — and it returned $8.0\times10^{-1}$, an $O(1)$ failure of a statement about invariance; **the correct sign follows from $D_{\imath}=\partial_{\imath}-ig_{4}A_{\imath}$ and from nothing else.** That is worth reporting because the reader should know the invariance was checked **against a plausible alternative** and not merely asserted, and because it is the second time the same convention produced the same trap: **a sign that inverts an invariance test is always the transformation's, never the object's.** Both F and G now stand at their noise floors, which is the evidence that the signs are right.

*The third is what the check does not test.* It tests that the displays are one statement in different clothes, on data satisfying no field equation — a check of the algebra, not of the theory. **A reader who wants a check of the physics will not find it here**, because the physics claim is that the fluid's force slot is this term, and no finite difference can test a claim about which slot a term belongs in.

## The Differentiated Guidance Equation

**Differentiate the pair momentum, use the lemma, and split $M_{\imath}$ into its diagonal and off-diagonal parts.** The result, verified as the fourth row above:

$$
\partial_{\jmath}\Pi_{\imath,kl}
=-\bigl[U_{\mathrm{frm}}^{\dagger}D_{\jmath}D_{\imath}\Xi\,U_{\mathrm{frm}}\bigr]_{kl}
-\bigl[\Omega_{\jmath},\Pi_{\imath}\bigr]_{kl}
-\Omega_{\jmath,kl}\,\partial_{\imath}q_{kl},
$$

**with $q_{kl}:=\rho_{k}-\rho_{l}$ the pair's charge.** The pair is **ordered**: $q_{lk}=-q_{kl}$, so the sign of a pair's charge is a convention about which member is written first, and the article's convention is $k<l$ where an unordered pair is meant. **The sign is not a physical asymmetry of the pair, and the crossing is what makes that plain**: at $\rho_{k}=\rho_{l}$ both orderings vanish together. What the sign does carry is orientation — which member gains and which loses — and the force follows it.

**Three terms, and each has a reading.**

| term | what it is | the fluid's word for it |
| --- | --- | --- |
| $-\bigl[\widehat{D_{\jmath}D_{\imath}\Xi}\bigr]_{kl}$ | the field's own second covariant derivative, off-diagonal in the eigenbasis | **the force** — on shell, the $\Xi$ equation's off-diagonal part |
| $-\bigl[\Omega_{\jmath},\Pi_{\imath}\bigr]_{kl}$ | the frame's rotation acting on the pair's momentum | **the transport**, and the only place the non-abelian structure enters |
| $-\Omega_{\jmath,kl}\,\partial_{\imath}q_{kl}$ | the flow times the gradient of the splitting | **bookkeeping** — the product rule in $p=qv$, and the article says so rather than dressing it as a force |

**The third term is not physics and the article does not pretend otherwise.** $\Pi=q\Omega$, so differentiating it gives $q\,\partial\Omega+\Omega\,\partial q$; the second piece is the term written above, a statement about a varying inertial coefficient and not about a force. **What it does say is worth one sentence**: a pair whose splitting varies along a direction has a momentum that varies even at constant flow, so a stratified fluid's internal motion is not inertial in the flat sense. That is the mass formula's $g_{4}^{2}q^{2}$, read as a variation.

**And $\Pi$ is an off-diagonal object only.** On the diagonal $M_{\imath,kk}=\partial_{\imath}\rho_{k}$ while $q_{kk}\equiv0$, so $\Pi$ is defined on $k\ne l$ and is zero wherever it is extended by symmetry. The article uses $\Pi$ only in entries with $k\ne l$, and the notation table says so.

**The first term is the force, and on shell the $\Xi$ equation constrains it — constrains, not equals, and the difference is the honest part of this section.** The display's force term is the *individual* component $\bigl[U_{\mathrm{frm}}^{\dagger}D_{\jmath}D_{\imath}\Xi U_{\mathrm{frm}}\bigr]_{kl}$ at fixed $\jmath,\imath$; *The Lagrangian and the Primordial Force*'s matrix equation contracts the indices, $\sum_{\imath}\varepsilon_{\imath}D_{\imath}D^{\imath}\Xi=\partial V/\partial\Xi+\text{(fermion bilinear)}$ in the chart's variables. **The object in the display is the trace's summand and not the trace**, so the two are not the same object and cannot be substituted into one another by inspection.

**What relating them costs, stated exactly.** Decompose $D_{\jmath}D_{\imath}\Xi$ into its trace part (the $\Xi$ equation), its antisymmetric part (the curvature, fixed by the Bianchi identity), and its symmetric traceless part (the off-diagonal constraint). **All three pieces are then fixed**: the trace by the equation of motion, the antisymmetric part by $[\mathbb{F}_{\jmath\imath},\Xi]$, the traceless part by the chart's off-diagonal algebra. That decomposition is the step that turns the force term's display into a momentum balance with a source, **and this article does not carry it out** — writing "substituting it turns the display into" would imply a substitution that does not exist in that form.

**So the claim is the weaker and true one, and it is enough for the section's purpose.** The force term is *not free*: every one of its three irreducible pieces is fixed on shell, two of them by identities and one by the equation of motion. **The residual freedom is the fermion current**, and that is where a future article's momentum balance has to get its source. A reader who wants the closed pair equation will find its ingredients here and its assembly elsewhere.

**And this is where the abelian derivation's cancellation no longer happens.**

## Where the Abelian Cancellation Used to Happen

**One sentence, and everything after it is that sentence's unfolding: the abelian Lorentz force is a cancellation of second derivatives, and the non-abelian force is the failure of that cancellation.** At the abelian rungs the differentiated eikonal gives $\pi^{\mu}F_{\mu\nu}=0$ — in the convention $\pi_{\mu}=\partial_{\mu}S-eA_{\mu}$, $F_{\mu\nu}=\partial_{\mu}A_{\nu}-\partial_{\nu}A_{\mu}$, where the overall sign is a matter of $F$'s orientation and not of the content — and the content of that identity is $\partial_{[\nu}\partial_{\mu]}S=0$: **the antisymmetrised Hessian *is* the cancellation.** Here the same step meets a Hessian that does not antisymmetrise to zero,

$$
\bigl[D_{\jmath},D_{\imath}\bigr]\Xi=-ig_{4}\bigl[\mathbb{F}_{\jmath\imath},\Xi\bigr],
$$

**so this is not a different derivation with a different outcome; it is the same derivation with a non-commuting Hessian, and the failure is the curvature.** Antisymmetrising the differentiated guidance equation separates the two halves — the symmetric part, which the abelian derivation would have cancelled, pairs with itself, while the antisymmetric part stands:

$$
\partial_{[\jmath}\Pi_{\imath],kl}\;\ni\;-ig_{4}\bigl[U_{\mathrm{frm}}^{\dagger}\bigl[\mathbb{F}_{\jmath\imath},\Xi\bigr]U_{\mathrm{frm}}\bigr]_{kl}.
$$

**So the primordial rung's acceleration slot is a field equation while the lower rungs' were gradients**, which is the strengthening *What Is a Fluid Equation in the Biquaternion Universe* records: at the abelian rungs the differentiated first-order statement *is* the force and nothing else survives; here something else survives by construction.

## The Residue Is a Three-Species Effect

**The commutator's pair entry does not need a third species, and its three-species part is exactly the non-abelian piece.** With the momentum resolved on the pair,

$$
\bigl[\Omega_{\jmath},\Pi_{\imath}\bigr]_{kl}=\Pi_{\imath,kl}\bigl(\Omega_{\jmath,kk}-\Omega_{\jmath,ll}\bigr)+\sum_{m\ne k,l}\bigl(\Omega_{\jmath,km}\Pi_{\imath,ml}-\Pi_{\imath,km}\Omega_{\jmath,ml}\bigr),
$$

**and the two terms are of different kinds.** The first multiplies the pair's momentum by the connection's *diagonal* entries — the pair's relative $\mathrm{U}(1)$ phase — and needs only two species. The second sums over a **third** label, and is the only place a commutator of two off-diagonal flows can appear: **the third label is the commutator's intermediate state**, which is why a commutator of two matrices supported on one pair has no off-diagonal entry there — and the same reason the six heavy vectors come as pairs of frame directions.

**The verification makes the distinction sharp, and it is the article's most surprising number.**

| configuration | the pair entry of $[\Omega_{\jmath},M_{\imath}]$ against the pair-only sum |
| --- | --- |
| frame and connection supported on one pair | $5.6\times10^{-17}$ — **exact** to the last bit double precision resolves, so the difference of two expressions that are algebraically equal |
| the same, with one further species mixed in | $1.4\times10^{-9}$, against a pair entry of magnitude $0.48$ |

**So a two-species truncation of this fluid is abelian in its pair sector exactly, and not approximately.** The non-abelian term is not a small correction that a two-level model captures; it is absent at two levels and present at three. **That has consequences for model-building, and they have to be stated carefully or they overreach.** An **exact** two-density truncation of the primordial fluid — the obvious thing to write down — reproduces the abelian force law and misses the curvature term entirely, and **no amount of care in an exact truncation recovers it**, because the commutator's pair entry is identically zero on two-species support. **A matched truncation is a different object and the article does not exclude it**: keep a third species, integrate it out, and an effective curvature term with a coefficient can appear — this is ordinary effective-field-theory matching, and it is what happens in the two-flavour-to-three-flavour matching in QCD. **What the check rules out is the exact two-species model, not the matched three-species one**; what the check does not supply is the matching coefficient. The sentence "three species or nothing" is therefore about exactness, and a reader who wants an effective two-species description needs a third species heavy and a matching procedure, not a smaller matrix.

## The Force on a Pair Is a Commutator, and Its Weight Is a Splitting

**The force term is the curvature acting, and in the curvature's own eigenbasis the action is a multiplication.** Over $\mathbb{C}$ the **Hermitian** $\mathbb{F}$ — $A$ is Hermitian in the verified convention, so $\mathbb{F}$ is too — is unitarily diagonalisable with **real** eigenvalues $f_{1},\dots,f_{4}$, and in that basis

$$
-ig_{4}\,[\mathbb{F},\Xi]_{kl}=-ig_{4}\,(f_{k}-f_{l})\,\Xi_{kl},
\qquad\text{check H: }9.2\times10^{-16}.
$$

**Check I is what makes that line legitimate rather than convenient**: built from the connection, $\mathbb{F}$ is Hermitian to the last bit, its eigenvalues are real to $0$, and $[D_{\jmath},D_{\imath}]\Xi=-ig_{4}[\mathbb{F}_{\jmath\imath},\Xi]$ holds to $2.8\times10^{-12}$ — so the spectral form is a theorem about this $\mathbb{F}$ and not a convention imported with a sign. **The whole of the residue is in that line.** The force on the pair $(k,l)$ is the field's own eigenvalue splitting times the pair's amplitude, in the direction of the pair's amplitude: **a curvature that is a single number in every direction cannot push a pair, and a curvature that is not cannot help it.**

**Two splittings, two roles, and the article must not let them merge.** The density splitting $q_{kl}=\rho_{k}-\rho_{l}$ is **inertia**: it sits in the denominator of the guidance equation, $\Omega_{kl}=M_{kl}/q_{kl}$, and it vanishes at a crossing to make a species massless. The field-strength splitting $f_{k}-f_{l}$ is **weight**: it sits in the numerator of the balance, multiplying the amplitude. **Same form, opposite position, and two different operators** — $\Xi$'s spectrum and $\mathbb{F}$'s. That is why a degenerate vacuum is a fixed point of the guidance equation and not of the force: a vacuum can degenerate one splitting without touching the other, and the article states it because the conflation of the two is the natural misreading of "the force is a splitting".

**And the operation is a commutator rather than a pairing, because the object acted on is a matrix — the deepest difference between this balance and Wong's, and the one the table's first row cannot show.** Wong's force is the contraction $F^{\mu\nu}_{a}q^{a}v_{\nu}$: a **pairing** of a charge with a curvature, returning a *number*, and available only because what it produces is a number. Here $\Pi_{\imath,kl}$ is a matrix entry and the balance's output is a matrix; the invariant pairing $\operatorname{tr}(\mathbb{F}\Pi)$ returns a scalar and cannot serve, so the only canonical bilinear map $\mathrm{Mat}\times\mathrm{Mat}\to\mathrm{Mat}$ that remains is the **commutator**. **The corpus's force-slot term is therefore commutator-shaped — the shape of Wong's *second* equation, not his first** — and the word "force" names the slot it fills in the balance, not the operation that fills it. **The matrix-valued charge is the generative fact; the commutator is its consequence, and the three differences in the factors are what the commutator acts on.**

**What *is* a pairing is the diagonal, and that is why the table's last row is not "absent".** The centrifugal term $+2q_{kl}\sum_{\imath}\varepsilon_{\imath}\lvert\Omega_{\imath,kl}\rvert^{2}$ is a pairing — of the charge $q_{kl}$ with the flow's modulus $\lvert\Omega_{kl}\rvert^{2}$ — but a **self**-pairing, degenerate because on the diagonal $k=l$ it has one index and not two. So the block contains one force-shaped object and one only, it is a self-interaction, and **no term anywhere in it is a pairing of a curvature with a momentum, which is what Wong's force is.** **The block's force is Wong's force's twin in the index structure and Wong's precession's twin in the operation; a reader who hears one of those and not the other has heard half the sentence.**

**The abelian limit, in this language, is the splitting's vanishing rather than a cancellation.** $\mathbb{F}$ central means all four $f_{k}$ equal, so every $f_{k}-f_{l}$ is zero and the bracket vanishes *entrywise* — nothing is there and then removed. **That is the third face of the one fact §*Is This a General Force Law?* names first, and it is the face a reader is most likely to get wrong**, because "the commutator vanishes for a central field" sounds like a convention about derivatives, while "the eigenvalue splitting vanishes for a central field" is visibly a statement about a spectrum.

## The Two Wong Terms, in Two Sectors

**Wong's equations, and the object they belong to.**

$$
m\frac{dv^{\mu}}{d\tau}=g\,F^{\mu\nu}_{a}q^{a}v_{\nu},
\qquad
\frac{dq_{a}}{d\tau}=-g\,f_{abc}\,v^{\mu}A_{\mu}^{b}q^{c},
$$

**in the convention where $F_{\mu\nu a}=\partial_{\mu}A_{\nu a}-\partial_{\nu}A_{\mu a}+gf_{abc}A_{\mu b}A_{\nu c}$ and the covariant derivative is $\partial_{\mu}-igA_{\mu}$.** The relative sign of the two equations is convention-independent once $F$ and $D$ are fixed this way; the overall sign of the force is not, and the standard literature contains both, because some authors write $+gFqv$ with $F$ defined from $A$ with the opposite sign. **The corpus uses one convention throughout**, the one displayed here and in *The SU(4) Fluid Equations*, so no sign in this article has to be translated.

**The first is a force with a curvature, a charge and a velocity; the second is the charge's precession, which is the statement that the charge is parallel-transported.** Both are the equations of a *probe*: a point particle carrying a colour label through a background. **The primordial fluid is not a probe**, so the comparison has to be made object by object rather than by assertion.

**"Exact" is a word this table does not use, and the reason is worth stating before the table: nothing here is Wong's equation, and every row that is not "absent" is a sameness of *structure* rather than of *equation*.** What can be exact is a relation between two objects in the corpus; what cannot be exact is an identification with Wong's, because Wong's objects are a probe's and the corpus's are the background's. The column therefore grades the match, with the scale defined under the table.

| Wong's structure | the fluid's counterpart | where it lives | how close |
| --- | --- | --- | --- |
| $F^{\mu\nu}_{a}q^{a}v_{\nu}$: curvature × charge × velocity | the antisymmetrized $\widehat{D_{[\jmath}D_{\imath]}\Xi}$, with the pair label as the charge | the pair's momentum balance | **same shape**, four differences — the deepest being that the object acted on is a matrix |
| $\dot q_{a}=-gf_{abc}v^{\mu}A_{\mu}^{b}q^{c}$: precession of an adjoint charge | the frame's parallel transport, $D_{\imath}U_{\mathrm{frm}}$: the pair label rides the frame's column | the frame, **fundamental** ($\mathbf{4}$) | **same structure, different representation** |
| the same precession, adjoint-valued | $-g_{4}f_{abc}A_{b,\imath}F_{c,\imath\jmath}$: the vorticity's ordinary divergence fails by it | the vorticity, **adjoint** | **the closest match**: the same equation with the vorticity as the charge |
| a charge that precesses | nothing | the densities | **absent**: $\rho_{k}$ are eigenvalues, hence singlets |
| the same operation as row 1 — a charge-contraction, here against the flow's modulus | $+2q_{kl}\sum_{\imath}\varepsilon_{\imath}\lvert\Omega_{\imath,kl}\rvert^{2}$, the centrifugal push a split pair feels | the densities, **diagonal** | **force-shaped and still not Wong's**: it *is* a pairing, but a **self**-pairing of $q_{kl}$ with $\lvert\Omega_{kl}\rvert^{2}$ — the closest object in the block to Wong's first equation, and a self-interaction |

**The scale.** *Same shape*: the same product of three kinds of factor with the same index structure, differing in what each factor *is*. *Same structure, different representation*: the same transport statement in the $\mathbf{4}$ rather than the algebra. *Closest match*: the same equation, a different carrier of the charge. *Force-shaped, still not it*: a pairing, but a self-pairing. *Absent*: no counterpart, for a stated reason. **No row is "yes"**, and the prose elsewhere is on this scale.

**The first row's four differences, named, because "same shape" is doing work, and they are of two kinds.** Three are about *what each factor is*. *The field is the fluid's own* — Wong's $F$ is a background's, while $\mathbb{F}_{\jmath\imath}$ is the field strength of the very connection whose condensate defines the fluid. *The charge is not conserved* — $q_{kl}=\rho_{k}-\rho_{l}$ vanishes at a crossing and obeys no conservation equation; it is a charge in that the force is linear in it and the inertia quadratic. *The velocity is not a vector* — $\Omega_{\imath,kl}$ is internal, not a section of $TB_{\Phi}$. **The fourth is about the operation, and it is the deepest**: the object acted on is a matrix, so the output is a matrix, so the force is a **commutator** and not Wong's **pairing** — §*The Force on a Pair* proves it, and it is forced by what the charge is rather than chosen. **None is a defect: each is the fluid being a field where Wong's object is a probe.** Within all four the derivation is real: the antisymmetric part of the differentiated guidance equation *is* the curvature acting in the eigenbasis, and its $(k,l)$ entry with $m$ intermediate carries Wong's force's index contraction — **which is why the row says "same shape" and not "resembles".**

**The sector split, stated as a fact about the chart and not as the resolution of a conjecture.** The diagonal sector of the differentiated guidance equation is **centrifugal**: there $\Omega$ enters only as $\lvert\Omega\rvert^{2}$, weighted by the splitting, $+2q_{kl}\sum_{\imath}\varepsilon_{\imath}\lvert\Omega_{\imath,kl}\rvert^{2}$. The off-diagonal sector is **Lorentz-plus-precessional**: there $\Omega$ enters linearly, through $-\widehat{\bigl[D_{[\jmath}D_{\imath]}\Xi\bigr]}$ and $-[\Omega_{\jmath},\Pi_{\imath}]$. **The two sectors are disjoint**: differentiating the eigenvalue equations cannot produce the Lorentz or precession terms, and differentiating the off-diagonal guidance equation cannot produce a centrifugal term. **The eigenvalues are gauge singlets; the off-diagonal $\Pi$ carries the frame's basis orientation.**

**"Precesses" means change under parallel transport along the base, and the word is available only because $\Pi$ is invariant.** The statement is $\Pi(x+dx)-\Pi(x)\sim-[\Omega\,dx,\Pi]$ — a change in the resolved components as the frame is carried along the base — and **not** a change under a gauge transformation; check G is the verification that $\Pi$ is unchanged by one, and that invariance is what makes "precession" a physical statement rather than a relabelling. **$q_{kl}$ is a number and has no such transport; $\Pi_{\imath,kl}$ is a matrix entry and does.** Wong's $q^{a}$ is a number in the adjoint and $\Pi_{kl}$ a matrix entry in the fundamental, and **both precess for the same reason: both are components in a moving basis.**

**Where the precession is, and why in the fundamental.** The pair's charge $q_{kl}$ is carried by the frame's entry $U_{\mathrm{frm},kl}$; the frame is parallel-transported, $D_{\imath}U_{\mathrm{frm}}=\partial_{\imath}U_{\mathrm{frm}}-ig_{4}A_{\imath}U_{\mathrm{frm}}$; so along a flow the pair label is rotated by the connection. **That is Wong's second equation with the adjoint action replaced by the fundamental one**, because the label lives in the $\mathbf{4}$ and not in the algebra: Wong's charge is real and adjoint, this one complex and fundamental. **Same structure, different representation, and the representation is forced by what carries the label.**

**The precession is also in the balance itself, written in a frame where it is not recognisable as a gauge rotation — and this is the table's subtlest point.** The pair momentum $\Pi_{\imath,kl}=-M_{\imath,kl}$ with $M_{\imath}=U_{\mathrm{frm}}^{\dagger}D_{\imath}\Xi U_{\mathrm{frm}}$ is **invariant**, not adjoint-covariant: check G below confirms that $U_{\mathrm{frm}}^{\dagger}D_{\imath}\Xi U_{\mathrm{frm}}$ is unchanged under $U_{\mathrm{frm}}\to VU_{\mathrm{frm}}$. **So the commutator term $-[\Omega_{\jmath},\Pi_{\imath}]$ is not a gauge rotation of a charged object; it is the rotation of the eigenbasis relative to the frame.** That is the same content as Wong's precession seen from the frame in which the charge is diagonal: in a generic basis the charge matrix is acted on by $A$ through the adjoint action $[A,\cdot]$; in the eigenbasis the charge matrix *is* diagonal, its entries are the $q_{kl}$, and the connection appears as $\Omega$. **The two statements — $D_{\imath}U_{\mathrm{frm}}$ in the fundamental and $[\Omega_{\jmath},\Pi_{\imath}]$ on the invariant momentum — are one fact, because $\Omega$ is exactly what the frame's carrying looks like once resolved in the eigenbasis.** The invariance is why the term reads as a basis rotation; the physics is why it reads as a precession; and the reason both readings are available is that the frame is doing the carrying.

**The sector census, stated once, because three of this section's statements are the same statement in three sectors and the article should not let them look like three.**

| sector | the object | the term | what it is |
| --- | --- | --- | --- |
| **singlet** | $\rho_{k}$ | $+2q_{kl}\sum_{\imath}\varepsilon_{\imath}\lvert\Omega_{\imath,kl}\rvert^{2}$ | **centrifugal**: a force, no transport, no precession |
| **fundamental** | $U_{\mathrm{frm}}$, i.e. the pair label | $D_{\imath}U_{\mathrm{frm}}=\partial_{\imath}U_{\mathrm{frm}}-ig_{4}A_{\imath}U_{\mathrm{frm}}$ | **precession**: Wong's second equation, in the $\mathbf{4}$ |
| **adjoint** | $A_{\imath}$, $F_{a,\imath\jmath}$ | $-g_{4}f_{abc}A_{b,\imath}F_{c,\imath\jmath}$ | **precession again**: the same structure on the vorticity |
| **eigenbasis** | $\Pi_{\imath}$, $\Omega_{\jmath}$ | $-\bigl[\Omega_{\jmath},\Pi_{\imath}\bigr]$ | the fundamental and adjoint rows, seen from the frame the charge is diagonal in |

**So "the densities are inert" is half true, and the half that is false is the interesting half.** They are inert **to the connection** — no linear term, no rotation — and they are **not** inert to the flow: the centrifugal term is what a stratified fluid does when its internal rotation is nonzero, and it is a genuine force on the diagonals. **A reader who takes "eigenvalues are singlets, so nothing built from them can precess" as "the densities feel nothing" has read one row of the table and missed the fifth.**

**The adjoint version exists on the other object.** The vorticity's equation in *The SU(4) Fluid Equations* reads

$$
\sum_{\imath}\varepsilon_{\imath}\partial_{\imath}F_{a,\imath\jmath}
=-\sum_{\imath}\varepsilon_{\imath}g_{4}f_{abc}A_{b,\imath}F_{c,\imath\jmath}+g_{4}j_{a,\jmath},
$$

**and the middle term is Wong's precession with the vorticity as the charge**: a sum over the adjoint index, the structure constants, the connection contracted with a summed direction, and the charged object to the right of the structure constants. **So the block contains both of Wong's equations and neither of them on the densities** — the force on the frame's curvature, the precession on the frame in the fundamental and on the vorticity in the adjoint.

## The Crossing

**At $\rho_{k}=\rho_{l}$ four statements become one, and they are one because they are four readings of one weight.**

*The guidance equation is singular* — the denominator vanishes while the numerator need not, so the pair's flow is undetermined and the frame's labelling of the pair is unphysical. *The mass vanishes* — the gauge-kinetic weight is $g_{4}^{2}(\rho_{k}-\rho_{l})^{2}$, so that pair's off-diagonal connection component is massless. *The pair's charge vanishes* — $q_{kl}=0$, so $\Pi=q\Omega$ is zero even at nonzero flow: **a species cannot respond to a field it cannot be distinguished from.** *A mode becomes eaten rather than heavy* — the two directions mixing the pair at fixed splitting are the eaten ones, and the degeneracy is what makes them eaten.

**What the crossing is not.** It is not a singularity of the theory but of the *chart* — of labelling species by eigenvalue — and the physics there is a $\mathrm{U}(2)$ rotation that no observable can label. **The article says so because the temptation is to read the divergence as a discovery.**

## Is This a General Force Law?

**A reader is entitled to ask whether this is the general force law — the one from which the Lorentz force, the strong force and the weak force are limits — and the answer is no in four ways, and each "no" is a different "no".**

**First, what is general is a method, not an equation.** The unifier in this block is one sentence: *the force is what the momentum does when the first-order statement is differentiated.* That sentence holds at every rung, and the article has used it at eight. **But the object it produces is not the same object at every rung**, because the first-order statement is not the same: a mass shell at the gradient rungs, an eikonal at the spinor rung, a guidance equation at this one. A method that produces different equations on different data is a method and not a master law, and calling it a master law would be claiming a universality the derivation does not have.

**Second, the Lorentz force is not *deduced* from the term derived here, and the reason is decisive rather than diplomatic: the residue's abelian limit is *exactly* zero, and it is zero for three reasons that are one reason.** *Centrality* — $\mathbb{F}_{\jmath\imath}=F_{\jmath\imath}\mathbb{1}$ commutes with every $\Xi$, so the bracket vanishes. *Spectral degeneracy* — a central element has all its eigenvalues equal, so in the eigenbasis of $\mathbb{F}$ every field-strength splitting $f_{k}-f_{l}$ is zero and the force on every pair is zero entrywise. *Left equals right* — a central element commutes, so the commutator in $D_{\imath}\Xi=\partial_{\imath}\Xi-ig_{4}[A_{\imath},\Xi]$ degenerates to a plain derivative with nothing left to act on. **Centrality, spectral degeneracy and left-equals-right are three languages for one fact — an element of the centre — and any one of them alone kills the residue**, which is why the limit is an exact zero and not a small number. In a theory whose derivative acted by left multiplication the abelian curvature would survive as a multiple of the identity; **the corpus's derivative acts by commutation, and that is what makes the limit vanish exactly.**

**So the relation is not "general law, special case".** The abelian rungs *solve* the differentiated identity for the force using the commutativity of partials; here it cannot be solved that way, because the antisymmetric part no longer vanishes. **Both are one step applied to different data; neither is a limit of the other's equation.**

**Third, this model does not have a strong force law and a weak force law to derive.** It has one connection, one coupling $g_{4}$, and fifteen generators — one $\mathrm{SU}(4)$, not a product. **"Strong" and "weak" are not separate sectors here** but features of a broken phase, where the vacuum's splitting pattern makes six directions heavy and six eaten; whether the Standard Model's two sectors emerge from that pattern is a question about the breaking and the fermion content, and no article in the block claims it is answered. **A reader who wants the derivation of the strong force's law will find it in the comparison with Wong, which is exactly the classical colour-charge force law** — and the verdict there was "same shape, three differences, different sector", not "derived".

**Fourth, and deepest: a force law requires a material derivative; a material derivative requires a base velocity; the primordial fluid has none; therefore it has a balance, not a law.** Wong's equation is $d/d\tau$ along a trajectory, and computing it needs $dx^{\mu}/d\tau$. **The primordial flow is $\Omega_{\imath}$, which is $\mathfrak{u}(4)$-valued and not a section of $TB_{\Phi}$**, so there is no $\Omega^{\imath}\partial_{\imath}$ and no $D/D\tau$; **the object computed here is $\partial_{\jmath}\Pi_{\imath}$ — a base-gradient of momentum, not a material rate of change.** That is why it is a balance and not a law.

**And it is the structural answer to this section's title, not a defect in the derivation.** The eight lower rungs have a force law because their velocity is a base vector: those fluids move *in* the material sector, where a material derivative exists. **The primordial rung has a balance because its motion is internal: this fluid is *on* the material sector.** So the base-and-fibre distinction decides whether the chain of §*The Chain, and the Step That Changes* terminates in $F=ma$ or in a balance — **one Lagrangian, three readings, and the third reading's *form* is set by where the fluid lives.**

**What does generalise, and can be said without hedging, is the shape of the balance.** Any fluid whose momentum is a charge times a velocity has a differentiated balance of three terms — force, transport, product rule — and any fluid whose velocity is a connection has a transport term that is a commutator and hence needs three species to be non-abelian. The three kinds are not this rung's; they are what one differentiation of a transport law produces, and they are stated with the tests that separate a product-rule term from a force term in [Differentiating a First-Order Transport Law](differentiating-a-first-order-transport-law-force-transport-and-product-rule-terms.html). The trichotomy that puts the commutator where a pairing would stand is in [A Matrix-Valued Charge Cannot Be Contracted](a-matrix-valued-charge-cannot-be-contracted-three-couplings-and-the-inner-derivation.html). **Those two sentences are general; the equation is not.** The block's claim, stated at its true strength, is that the force slot is one rule applied at nine rungs, and that the rule's output at the ninth is a curvature term whose structure the classical colour-charge equation shares.

## What This Article Does Not Claim

**That the primordial fluid obeys Wong's equations.** It does not, and the difference is the whole of §*The Two Wong Terms, in Two Sectors*: Wong describes a probe with a charge, and every term of the fluid's balance is a statement about the field the probe would move in. **What is shown is that the balance's force term has Wong's force's shape with three named differences — the field is the fluid's own, the charge is not conserved, the velocity is internal — and that Wong's precession appears in a different representation, and that neither appears on the densities.**

**That any of this is new field theory.** The antisymmetrized second covariant derivative is the curvature; that the curvature acts on a matter field in the representation it lives in is textbook. **What is new here is the location**: that the fluid's acceleration slot is the curvature term, that the term needs three species, and that the densities are excluded from it by gauge invariance. These are statements about the fluid reading, not about the Yang–Mills action.

**That the derivation is a solution.** Nothing here solves the field equations; the checks are algebraic identities on data satisfying no equation of motion. **A reader who wants the force law evaluated on a configuration will not find it here**, because no primordial configuration is known in closed form.

**That a commutator-shaped force is Wong's precession.** The *operation* is Wong's second equation's; the *content* is a force, because the term is the antisymmetrised second covariant derivative of the order parameter and it fills the balance's force slot. **Shape and role are different questions, and the article answers them separately rather than letting one answer both.**

**That the pair truncation is a controlled approximation.** It is exact at two species — the $5.6\times10^{-17}$ — and the exactness is a trap rather than a comfort: a two-density model reproduces the abelian force law exactly and the non-abelian one not at all, so its agreement is evidence of nothing.

**That the pair's charge is a charge in the quantum-number sense.** $q_{kl}=\rho_{k}-\rho_{l}$ is a difference of two eigenvalues, signed, vanishing on a crossing. **It is a charge in that the force is linear in it and the inertia quadratic**; it is not conserved and nothing here says it should be. The corpus's branch with a negative eigenvalue makes the sign concrete: there a pair's charge can have either sign, and the force follows it.

## Open Questions

**Whether the off-diagonal $\Xi$ equation closes the pair balance into a closed system.** The force term is the field's second covariant derivative, and on shell its trace, antisymmetric and symmetric-traceless pieces are each fixed — by the equation of motion, the Bianchi identity, and the off-diagonal algebra. **Assembling them into a closed pair equation is the step this article does not take**; the residual freedom is the fermion current, and whether the three close in the chart is not settled here.

**Whether the curvature term survives a truncation that keeps a third species heavy.** The check says the pair entry of the commutator needs a third label. A truncation that keeps three species and treats the third as heavy might produce an effective curvature term with a coefficient — a matched truncation rather than an exact one — and that is the model-building question this section raises and does not answer.

**Whether the precession's representation is observable.** The fundamental and adjoint precessions differ in which object rotates, and any fluid observable built from $\lvert\Omega\rvert$ sees neither. **Whether a gauge-invariant observable at this rung is sensitive to the precession is the question the corpus has not asked**, and it decides whether the second Wong term is physics here or bookkeeping.

**Whether the crossing's four statements stay one statement beyond the classical chart.** Mass, flow and charge vanish together classically; whether loop corrections split them — a mass that does not vanish where the splitting does — is the question *The Machinery Under the Primordial Action* raises about the one-loop trace, and this article takes it no further.

## What This Article Adds and What It Relabels

**Adds.** The guidance equation with its count ($12$ filled, $4$ quotiented, agreeing with $16-4$ as a cross-check); the momentum lemma with proof and check; the pair balance with three terms assigned; **the sector split as a theorem** — diagonal centrifugal, off-diagonal Lorentz-plus-precessional, disjoint by what enters linearly; the three-species result; the **spectral face** of the force term, with the two splittings kept apart; the **four-difference grading** of the Wong table (three in the factors, one in the operation); and Wong's equations placed by sector.

**Does not add.** No new action, coupling, solution or loop. Every display is a sibling's or an identity of the chart; the article supplies where they sit.

**Relabels three phrases.** *"The primordial fluid obeys the Wong equation"* — it shares the force's shape with three named differences and the precession's structure in two other sectors, graded row by row. *"The differentiated eigenvalue equation gives a force law"* — it gives a momentum balance whose force term is the field's curvature. *"The two-density truncation captures the essence"* — it captures the abelian force exactly and the non-abelian term not at all.

## Summary

**The chain is the charged rungs' chain with one link replaced.** There, the polar form gives a mass shell and differentiating it gives the Lorentz force by cancelling second derivatives. Here, the chart's transport identity gives a guidance equation, and differentiating it gives a momentum balance in which the second derivatives do not cancel.

**The guidance equation is $\Omega_{\imath,kl}=[U_{\mathrm{frm}}^{\dagger}D_{\imath}\Xi U_{\mathrm{frm}}]_{kl}/(\rho_{l}-\rho_{k})$**: velocity equals covariant gradient over inertia, with the splitting as the inertia. It fills twelve entries and leaves four diagonal phases quotiented — **consuming the count $16-4$ rather than deriving it**, and agreeing with the stabiliser as a cross-check.

**The lemma is $\partial_{\jmath}M_{\imath}=U_{\mathrm{frm}}^{\dagger}D_{\jmath}D_{\imath}\Xi U_{\mathrm{frm}}-[\Omega_{\jmath},M_{\imath}]$**, checked to $1.2\times10^{-7}$. The differentiated guidance equation follows, and its force term is the field's own second covariant derivative.

**The abelian force is a cancellation of second derivatives and the non-abelian force is the failure of that cancellation**, and the residue's abelian limit is an *exact* zero in three languages — central field strength, degenerate spectrum, left equals right. The residue is $-ig_{4}[\mathbb{F}_{\jmath\imath},\Xi]$ — the curvature — and it is a three-species effect: exact at two species to $5.6\times10^{-17}$, present at three.

**Wong's force's shape is in the fluid and Wong's precession's structure is in the fluid, but not where the block said, and not as Wong's equations.** The force term is the curvature acting on a pair — the fluid's own curvature, a non-conserved charge, an internal velocity; the precession is the frame's parallel transport in the fundamental and the vorticity's adjoint failure; the densities have neither transport nor precession, because eigenvalues are singlets — **and they are not inert, because the diagonal sector carries a centrifugal force.**

**The deepest difference from Wong is that the object acted on is a matrix**, so the force is a **commutator** and not a pairing — the shape of Wong's *second* equation filling the slot of his first — and the weight it carries is the **field-strength splitting**, which is not the density splitting that divides the guidance equation. **The centrifugal diagonal is the one force-shaped object in the block, and it is a self-pairing.**

**The crossing makes the mass, the flow and the charge vanish together**, and that is one statement about one weight rather than three coincidences.

## Summary of Notation

| symbol | what it is |
| --- | --- |
| $\Xi$, $P$, $\rho_{k}$ | the scalar matrix (Hermitian, sixteen real), its diagonal of densities, and its eigenvalues — scalars on the base and gauge singlets |
| $U_{\mathrm{frm}}$ | the polar frame, twelve physical parameters; a decomposition, not a symmetry, absent from $D_{\imath}$ |
| $D_{\imath}$ | $\partial_{\imath}-ig_{4}A_{\imath}$, with $A_{\imath}\in\mathfrak{su}(4)$ |
| $\Omega_{\imath}$ | $U_{\mathrm{frm}}^{\dagger}D_{\imath}U_{\mathrm{frm}}=\Gamma_{\imath}-ig_{4}B_{\imath}$, the internal flow; $\mathfrak{u}(4)$-valued, not a vector of the base |
| $\Gamma_{\imath}$, $B_{\imath}$ | the frame's bare rotation $U_{\mathrm{frm}}^{\dagger}\partial_{\imath}U_{\mathrm{frm}}$ and the gauge field in the frame |
| $M_{\imath}$ | $U_{\mathrm{frm}}^{\dagger}D_{\imath}\Xi U_{\mathrm{frm}}=\partial_{\imath}P+[\Omega_{\imath},P]$, the frame-covariant momentum |
| $q_{kl}$, $\Pi_{\imath,kl}$ | $\rho_{k}-\rho_{l}$, the pair's charge (signed, vanishing at a crossing), and $q_{kl}\Omega_{\imath,kl}$ its momentum — equal to $-M_{\imath,kl}$ |
| $\mathbb{F}_{\imath\jmath}$, $g_{4}$ | the field strength $\mathbb{F}_{\imath\jmath}=F_{a,\imath\jmath}t_{a}$ and the one coupling |

## Further Reading

- [The SU(4) Fluid Equations from the Primordial Action](su4-fluid-equations-from-the-primordial-action.html). The chart this article differentiates: the transport identity, the four densities, the six heavy vectors, and the vorticity whose divergence fails by Wong's precession.
- [The Lagrangian and the Primordial Force](the-lagrangian-and-the-primordial-force.html). The action and the one matrix equation whose off-diagonal part this article's force term becomes on shell.
- [Criterion for a Fluid Equation: One Polar Coordinate's Euler–Lagrange Equation, Not a Combination](criterion-for-a-fluid-equation-one-polar-coordinates-euler-lagrange-equation.html). The criterion, the six slots, and the base-and-fibre distinction that makes "the flow is internal" a precise statement.
- [Relativistic Mechanics from the Dirac Wave](relativistic-mechanics-from-the-dirac-wave.html). The abelian cancellation whose non-abelian failure this article identifies: "The gradient is the Lorentz force."
- [Charged Klein–Gordon Fluid Equations from the Polar Action](charged-klein-gordon-fluid-equations-from-the-polar-action.html). The same move at a gradient rung, with the honesty paragraph that says the force is not a term.
- [The Charged Spin-Half Fluid: Charge Couples to the Lorentz Force, Spin Does Not](the-charged-spin-half-fluid-charge-couples-to-the-lorentz-force-spin-does-not.html). The rung where the force's structure is separated from the spin's.
- [The Restructuring of the Primordial Force and the Mass of the Six Leptoquarks](the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.html). The other sign of $\mu_{\Phi}^{2}$, where the splitting pattern and hence the crossing structure differ.
- [The Machinery Under the Primordial Action: Trace, Curvature, Ghosts and One Loop](the-machinery-under-the-primordial-action-trace-curvature-ghosts-and-one-loop.html). Where the question of whether loop corrections split the crossing's statements is posed.
- [Differentiating a First-Order Transport Law: Force, Transport and Product-Rule Terms](differentiating-a-first-order-transport-law-force-transport-and-product-rule-terms.html). The general form delegated: the three kinds of term, the three tests that separate them, and the checklist whose fifth line asks that a display state each term's kind and not only its position.
- [A Matrix-Valued Charge Cannot Be Contracted: Three Couplings and the Operation the Matrix Rung Uses Instead](a-matrix-valued-charge-cannot-be-contracted-three-couplings-and-the-inner-derivation.html). Why this rung's source is a commutator and not a pairing, and the two eigenvalue splittings — inertia divides, force weight multiplies — that the balance keeps apart.
- [Base-Valued versus Internal Flow Velocity: A Test Separating Force Laws from Momentum Balances](base-valued-versus-internal-flow-velocity-a-test-separating-force-laws-from-momentum-balances.html). The test behind this article's fourth "no": why an internal velocity costs the material derivative and leaves a balance.
