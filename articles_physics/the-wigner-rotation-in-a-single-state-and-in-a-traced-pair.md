# __The Wigner Rotation in a Single State and in a Traced Pair__

## Introduction

The polar split of a frame change writes it as $\tilde U=\tilde L\tilde R$ with $\tilde L$ Hermitian and $\tilde R$ unitary. The companion establishes that $\tilde R$ is the Wigner rotation, that it is an isometry of the Bures angle while $\tilde L$ is not, and that $\tilde R$ is the part of a frame change the Bures geometry cannot see. This article takes the next step and asks what $\tilde R$ is *about*. The answer is short and it closes a door: **no single state registers $\tilde R$, and only a comparison does.**

The claim is not that the rotation is unobservable. It is that the rotation is unobservable *in a single state*, and everything that has been said about it — including the frame dependence of entanglement — needs a second object or a discarded label to have any content at all.

The findings are stated in advance.

1. A rotation of one state moves the vector and changes no invariant. $\lvert\vec s\rvert$ and $N$ are unchanged to $0$ and to $1.0\times10^{-15}$ over three angles spanning $0.4$ to $3.0$; a rotation is an isometry of the ball and the ball is homogeneous under it.
2. State and axes rotated together change nothing. The image vector is the rotated vector to $1.7\times10^{-16}$, and $\lvert\vec s'\rvert-\lvert\vec s\rvert=0$. So $\tilde R$ is data only relative to something that does not rotate with it.
3. A common rotation of every branch of a traced label changes nothing. With weights $0.7$ and $0.3$ the reduced vector has $\lvert\vec s\rvert=1.000000000000000$ for every angle.
4. Unequal rotations on the branches are registered. The same state with $\tilde R(0)$ on one branch and $\tilde R(\omicron_{\mathrm{ang}})$ on the other has $\lvert\vec s\rvert=1$, $0.973953117965$, $0.898291137919$, $0.761577310586$, $0.400000000000$ at $\omicron_{\mathrm{ang}}=0$, $0.5$, $1$, $\pi/2$, $\pi$, matching the closed form $\sqrt{(1-w)^{2}\sin^{2}\omicron_{\mathrm{ang}}+(w+(1-w)\cos\omicron_{\mathrm{ang}})^{2}}$ to twelve digits; the impurity moves from $0$ to $0.210000000000$.
5. A pure pair's entanglement is untouched by any local unitary. The concurrence of a state with $C=0.96$ is $0.960000000000000$ after three arbitrary local rotations, including unequal ones on the two factors.
6. A pair's entanglement is changed only by a rotation that varies over a discarded label. With two branches carrying the same Bell pair and relative rotation $\omicron_{\mathrm{ang}}$, the concurrence is $\lvert\cos\omicron_{\mathrm{ang}}\rvert$ exactly and the purity is $(1+\cos^{2}\omicron_{\mathrm{ang}})/2$, both to twelve digits.
7. So frame-dependent entanglement is a statement about the trace, not about the frame. $\tilde R$ contributes to entanglement only when it is distributed unequally across a label that is then summed out.

The notation is that of the companions. The state is $\tilde{Ϛ}_{\Psi}=\tfrac12(e_t+i\vec s_{\Psi})$; the impurity is $N=\tfrac14(1-\lvert\vec s\rvert^{2})$; the congruence is $\mathrm{Cg}_{\tilde U}:\tilde Q\mapsto\tilde U\tilde Q\tilde U^{*}$. A rotation by angle $\omicron_{\mathrm{ang}}$ about the unit vector $\vec n$ is written $\mathrm{SU}(2)_{\vec n}(\omicron_{\mathrm{ang}})$, with $\tilde R=\mathrm{SU}(2)_{\vec n}(\omicron_{\mathrm{ang}})$ the unitary rotor of the same angle. The polar split is $\tilde U=\tilde L\tilde R$. The concurrence of a two-qubit pure state $Ξ_{\mathrm{wfn}}=(a,b,c,d)$ is $C=2\lvert ad-bc\rvert$, and of a mixed state is the usual $\max(0,\eta_{1}-\eta_{2}-\eta_3-\eta_4)$ over the roots of $\rho\tilde\rho$.

## What the Rotation Does to One State

### It moves the vector and nothing else

A rotation sends $\vec s$ to $\mathrm{SU}(2)_{\vec n}(\omicron_{\mathrm{ang}})\vec s$ and leaves every invariant of the single state alone. At $\vec s=(0.3,-0.5,0.6)$, $\lvert\vec s\rvert=0.836660026534076$ and $N=0.075000000000000$ in the original and after rotations of $0.4$, $1.7$ and $3.0$; the worst deviation in $\lvert\vec s\rvert$ is $1.0\times10^{-15}$ and in $N$ it is $0$.

The reason is that a rotation is an isometry of the ball and the ball is homogeneous under rotations. Every point of a sphere can be moved to every other by a rotation, so the orbit is the whole sphere, and a sphere has no marked point. There is no functional of one state that a rotation can change, because a rotation generates the whole space of states of a given radius.

### So the statement "$\tilde R$ was applied" has no truth value for one state

This is the sharp form of the claim, and it is not the weak one. The weak form would say that a rotation is hard to detect. The sharp form says that a single state does not carry the information, so there is nothing to detect: a state is a vector in a space whose symmetry group is the rotations, and the question of whether a symmetry was applied before the state was written in the frame is a question about the writing and not about the state.

Care is needed with the word "unobservable". A rotation of a spin is observable as a phase in an interference experiment, and the Wigner rotation is observable in the interference between momentum branches. What is not observable is a rotation *of a state on its own*, and the two statements differ by the presence of a second branch. The rest of the article is about that second branch.

## The Gauge Statement

**Rotating the state and the axes together changes nothing at all.** The image of $\vec s$ under a rotation of $0.9$ about $\vec n=(1,1,0)/\sqrt2$ is the rotated vector to $1.7\times10^{-16}$, and the modulus is unchanged to $0$. That is the content of "orientation is relational" in one line: only the angle between the state and something else is data.

So $\tilde R$ has content exactly when something fails to rotate with it. Two cases exhaust the possibilities. Either there is a second object that does not rotate — a reference state, a second spin, a Hamiltonian with a fixed axis — and then $\tilde R$ is registered as a *relative* orientation. Or there is a label over which the rotation varies and which is then discarded, and then $\tilde R$ is registered in the reduced state. Both cases need two things; neither needs one.

## What a Comparison Registers

### A rotation that varies over a discarded label

Take one spin, two branches, unequal weights, and a different rotation on each branch. The state is $\sqrt{w}\,\lvert\uparrow\rangle\lvert p_a\rangle+\sqrt{1-w}\,\lvert\uparrow\rangle\lvert p_b\rangle$ with $w=0.7$, the branch $a$ is left alone, and branch $b$ is rotated by $\omicron_{\mathrm{ang}}$ about $\hat x$; the label is then traced out.

| $\omicron_{\mathrm{ang}}$ | $\lvert\vec s\rvert$ | $N$ |
| --- | --- | --- |
| $0$ | $1.000000000000$ | $0$ |
| $0.5$ | $0.973953117965$ | $0.012853831002$ |
| $1.0$ | $0.898291137919$ | $0.048268257884$ |
| $\pi/2$ | $0.761577310586$ | $0.105000000000$ |
| $\pi$ | $0.400000000000$ | $0.210000000000$ |

The closed form is $\lvert\vec s\rvert^{2}=(1-w)^{2}\sin^{2}\omicron_{\mathrm{ang}}+\bigl(w+(1-w)\cos\omicron_{\mathrm{ang}}\bigr)^{2}$, matched to twelve digits at all five angles. Nothing in it refers to the rotation as an absolute object; it refers to the *difference* between the rotation applied on one branch and the rotation applied on the other.

A common rotation moves nothing. With $\omicron_{\mathrm{ang}}$ the same on both branches, $\lvert\vec s\rvert=1.000000000000000$ at $\omicron_{\mathrm{ang}}=0$, $0.7$ and $2.2$. The state is a pure state whose vector has merely rotated inside the frame, and the impurity does not move, which is the previous section's statement in the reduced language.

### The pattern

**What the reduced state registers is the variance of $\tilde R$ over the discarded label, and only that.** A constant $\tilde R$ is a relabelling; a varying $\tilde R$ is a physical operation, because it correlates the spin with the label. This is decoherence with a unitary cause, and it is the only mechanism by which a frame change reaches a reduced state.

## What Follows for Frame-Dependent Entanglement

### A local unitary cannot change a pure pair's concurrence

The concurrence of a pure two-qubit state is $C=2\lvert ad-bc\rvert$, which is invariant under $U_1\otimes U_2$ for any unitaries. Starting from $(0.8,0,0,0.6)$ with $C=0.960000000000000$, three arbitrary pairs of local rotations — including the unequal pair $(2.1,0.4)$ — return $0.960000000000000$ exactly. This is the Schmidt decomposition's statement, and it holds for rotations as for any other unitaries.

So a Wigner rotation applied to one spin, or to both with the same angle, does nothing to the entanglement. A claim that a boost changes the entanglement of a pair must therefore explain how the boost does something other than apply one unitary to each factor.

### The pair that does change

Distribute the rotation over a label and discard the label. The state is $\bigl(\lvert\digamma_{\mathrm{st}}\rangle\lvert p_a\rangle+\lvert\digamma_{\mathrm{st}}\rangle\lvert p_b\rangle\bigr)/\sqrt2$ with $\lvert\digamma_{\mathrm{st}}\rangle=(\lvert\uparrow\uparrow\rangle+\lvert\downarrow\downarrow\rangle)/\sqrt2$; branch $a$ gets the identity on both spins and branch $b$ gets $\mathrm{SU}(2)_{\hat z}(\omicron_{\mathrm{ang}})$ on both; the label is traced out.

| $\omicron_{\mathrm{ang}}$ | concurrence | purity |
| --- | --- | --- |
| $0$ | $1.000000000000$ | $1.000000000000$ |
| $0.3$ | $0.955336489126$ | $0.956333903727$ |
| $0.6$ | $0.825335614910$ | $0.840589438619$ |
| $1.0$ | $0.540302305868$ | $0.645963290863$ |
| $\pi/2$ | $0.000000000000$ | $0.500000000000$ |
| $\pi$ | $1.000000000000$ | $1.000000000000$ |

Both closed forms are exact: the concurrence is $\lvert\cos\omicron_{\mathrm{ang}}\rvert$ and the purity is $(1+\cos^{2}\omicron_{\mathrm{ang}})/2$, matched to twelve digits. The state is a mixture of two Bell states related by a relative rotation, and the mixture of two orthogonal Bell states at $\omicron_{\mathrm{ang}}=\pi/2$ is the maximally mixed state, which has neither entanglement nor purity.

The recovery at $\omicron_{\mathrm{ang}}=\pi$ is not an error. A rotation by $\pi$ on a spin is $-i\sigma_{z}$, so on both factors it is $-\sigma_{z}\otimes\sigma_{z}$, and $\sigma_{z}\otimes\sigma_{z}$ acts as $+1$ on $\lvert\digamma_{\mathrm{st}}\rangle$; the two branches are then the same ray and the state is pure again. The concurrence is therefore not monotone in the frame's rotation, and a reader who expects monotonicity will misread the table.

### The corrected statement about frames

**Frame-dependent entanglement is a property of the trace, not of the frame.** In the table the frame change is a rotation applied to both spins of a branch, which is a local unitary and cannot change entanglement on its own; what changes the entanglement is that the rotation differs between branches while the branch label is summed out. The frame supplies the variation and the trace supplies the loss. Both are needed, and neither alone is enough.

This matters for how the result is stated in the literature. A boost is momentum dependent, and the Wigner rotation inherits the dependence; the spin state of a moving particle is entangled with its momentum, and a boost therefore applies different rotations to different momentum components. The entanglement that changes is the entanglement of the reduced spin state, and the momentum is what is discarded. The phrase "entanglement depends on the frame" is thus elliptical for "entanglement depends on the frame *and* on which degrees of freedom are traced out", and the second clause is the one that does the work.

## Objections

The objection is that this makes the Wigner rotation pure gauge, and it is observed. It is not pure gauge, and the objection conflates two absences. The rotation is unregistered by a single state, and it is registered by any comparison. Interference between two momentum branches is a comparison: the relative phase between them carries the rotation, and the corpus's Wigner angle is measured exactly there.

A second objection is that the $\lvert\cos\omicron_{\mathrm{ang}}\rvert$ result is about tracing and not about frames. That is what the article claims, and it is the reason the section exists. The rotation alone cannot change a concurrence; a rotation plus a discarded label can; the physics of frame-dependent entanglement is in the second term.

A third objection is that a state which registers nothing is not worth calling oriented. Agreed, and the objection names the point. Orientation is not a property a state has; it is a relation between a state and something else, and the article's contribution is to say what the something else has to be.

## What Is Not Claimed

**It does not claim that the Wigner rotation is unobservable.** It claims that one state does not register it. Interference, and the relative orientation of two states, do.

It does not claim that entanglement is subjective. The concurrence in the table is a property of the reduced density matrix and is as objective as any other number. What is frame-dependent is which reduced density matrix one is discussing.

It does not re-derive the Wigner angle. The companion has the closed form, the axis and the numerical checks; this article takes the angle as given and asks what it is about.

It does not settle which degrees of freedom a real experiment traces out. That is a question about the apparatus, and the article's formulas hold for any choice.

## Summary

A rotation of one state is an isometry of the ball and changes no invariant: $\lvert\vec s\rvert$ and $N$ are fixed, to $1.0\times10^{-15}$ and to $0$. A single state therefore does not register $\tilde R$, and the statement "$\tilde R$ was applied" has no truth value for it.

Rotating the state and the axes together changes nothing — the image vector is the rotated vector to $1.7\times10^{-16}$ — so only a relative orientation is data.

A rotation that varies over a discarded label is registered. With weights $0.7$ and $0.3$ the reduced modulus runs from $1$ to $0.400000000000$ and the impurity from $0$ to $0.210000000000$ as the relative angle runs from $0$ to $\pi$, matching a closed form to twelve digits; a common rotation moves nothing.

A pure pair's concurrence is untouched by any local unitary, $0.960000000000000$ after three arbitrary local rotations, so a boost that acts as one unitary per factor cannot change entanglement.

A pair's concurrence does change when the rotation varies over a traced label: $\lvert\cos\omicron_{\mathrm{ang}}\rvert$ exactly, with purity $(1+\cos^{2}\omicron_{\mathrm{ang}})/2$, recovering to one at $\omicron_{\mathrm{ang}}=\pi$ because the two branches become the same ray.

Frame-dependent entanglement is a statement about the trace. The frame supplies the variation of $\tilde R$; the trace supplies the loss; neither alone is enough.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\tilde U=\tilde L\tilde R$ | the polar split of a frame change |
| $\tilde R=\mathrm{SU}(2)_{\vec n}(\omicron_{\mathrm{ang}})$ | the unitary factor; the Wigner rotation |
| $\vec s\mapsto\mathrm{SU}(2)_{\vec n}(\omicron_{\mathrm{ang}})\vec s$ | the action on one state |
| $N=\tfrac14(1-\lvert\vec s\rvert^{2})$ | the impurity; unchanged by any rotation |
| $w$ | the weight of the first branch in the traced example |
| $\omicron_{\mathrm{ang}}$ | the relative rotation between two branches |
| $C=2\lvert ad-bc\rvert$ | the concurrence of a pure two-qubit state |
| $\eta_i$ | the roots of $\rho\tilde\rho$ in the mixed concurrence |

## Further Reading

- E. P. Wigner, "On unitary representations of the inhomogeneous Lorentz group", *Annals of Mathematics* **40** (1939) 149–204 — the little group and the rotation a boost induces
- A. Peres and D. R. Terno, "Quantum information and relativity theory", *Reviews of Modern Physics* **76** (2004) 93–123 — frame dependence of entanglement, and what a boost does to a reduced state
- R. M. Gingrich and C. Adami, "Quantum entanglement of moving bodies", *Physical Review Letters* **89** (2002) 270402 — the spin-momentum entanglement that a boost redistributes
- P. M. Alsing and G. J. Milburn, "Lorentz invariance of entanglement", *Quantum Information and Computation* **2** (2002) 487–512 — the invariance under a common unitary and its failure under a varying one
- M. A. Nielsen and I. L. Chuang, *Quantum Computation and Quantum Information*, Cambridge University Press, 2000 — the Schmidt decomposition, local unitaries and concurrence
- W. K. Wootters, "Entanglement of formation of an arbitrary state of two qubits", *Physical Review Letters* **80** (1998) 2245–2248 — the concurrence
- *The Wigner Angle of Two Boosts* — the Wigner angle, its axis and the two readings
- *Bures Isometries of the Bloch Ball: Rotations, the Slice and the Conformal Boundary* — the polar split and $\tilde R$ as the Bures isometry
- *Impurity in a Boosted Frame: The Invariant and the Read Value* — the trace condition, the projection and the read impurity
- *Frame-Dependent Entanglement and Relativistic Quantum Information in Biquaternionic Form* — the corpus's treatment of the boosted pair
