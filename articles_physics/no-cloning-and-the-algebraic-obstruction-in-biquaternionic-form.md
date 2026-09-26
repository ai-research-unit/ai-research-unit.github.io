# __No-Cloning and the Algebraic Obstruction in Biquaternionic Form__

## Introduction

The no-cloning theorem states that an unknown quantum state cannot be copied: there is no physical process that takes one copy of an arbitrary state and produces two, each identical to the original. The theorem is the reason quantum information is not merely classical information carried by quantum systems, and it is the origin of quantum key distribution, of the security of quantum money, and of the impossibility of amplifying a quantum signal by copying it.

The theorem is usually proved by an inner-product argument: a cloning transformation that worked for all states would have to be unitary, unitarity preserves inner products, but the inner product of two cloned outputs is the square of the input inner product, and a number equals its own square only when it is zero or one. This article presents the theorem in the biquaternion framework and isolates the operational meaning of "inner product" there. In the algebra the inner product of two rays is carried by the **trace pairing of their idempotents**,

$$
\bigl|\langle\psi|\phi\rangle\bigr|^2 = \mathrm{Tr}\bigl(\tilde{P}(\psi)\tilde{P}(\phi)\bigr) = 2\,\mathrm{Sc}\bigl(\tilde{P}(\psi)\tilde{P}(\phi)\bigr) \in [0,1],
$$

whose endpoints are the orthogonal and coincident cases. A cloning transformation must preserve this pairing, because it is an overlap and overlaps are preserved by the unitary evolution of the algebra; and it must simultaneously replace the pairing by its square, because two independent copies have an overlap that is the product of the two single-copy overlaps. The obstruction is therefore

$$
\mathrm{Tr}\bigl(\tilde{P}(\psi)\tilde{P}(\phi)\bigr) = \Bigl(\mathrm{Tr}\bigl(\tilde{P}(\psi)\tilde{P}(\phi)\bigr)\Bigr)^{2},
$$

which forces the pairing to be $0$ or $1$: **cloning is possible exactly for sets of mutually orthogonal states, and for no others.** The two states are then perfectly distinguishable, and copying them is a classical operation.

A second, equivalent reading is that the cloning map on states is quadratic, $\tilde{\rho}\mapsto\tilde{\rho}\otimes\tilde{\rho}$, while every physical evolution is affine on the state space. This is the algebraic statement that the obstruction is the linearity of quantum dynamics, and it is the version that extends to mixed states and to channels.

The article develops both readings, then treats approximate cloning, where the obstruction is quantified: the optimal universal qubit cloner achieves a fidelity of $5/6$, and the measurement-based alternative achieves only $2/3$. The universal cloner is constructed in explicit tensor-product form and its fidelity verified on a family of superposition states. The related no-go theorems — no-deleting, no-broadcasting, and the failure of cloning for mixed states — are stated in the framework's terms. The article closes by separating what is algebraic from what is standard.

## The Cloning Requirement

### Cloning as a map on states

A **cloning machine** for a family of states $\{\tilde{\rho}_x\}$ is a physical process, described in the framework by a completely positive trace-preserving map

$$
\Phi : \mathbb{M}_+ \otimes \mathbb{M}_+ \longrightarrow \mathbb{M}_+ \otimes \mathbb{M}_+ ,
\qquad
\Phi\bigl(\tilde{\rho}_x \otimes \tilde{\rho}_0\bigr) = \tilde{\rho}_x \otimes \tilde{\rho}_x
\ \text{ for all } x,
$$

where $\tilde{\rho}_0$ is a fixed blank state. The process is required to be **universal** if it works for every state of the defining module, and **state-independent** in the sense that the same $\Phi$ and the same blank serve every input.

Two features of $\Phi$ are immediate from the framework. It is **affine on the state space**: a convex combination of inputs maps to the corresponding convex combination of outputs, because a channel is linear on the cone and preserves the trace,

$$
\Phi\bigl((t\tilde{\rho}_1+(1-t)\tilde{\rho}_2)\otimes\tilde{\rho}_0\bigr)
= t\,\Phi(\tilde{\rho}_1\otimes\tilde{\rho}_0) + (1-t)\,\Phi(\tilde{\rho}_2\otimes\tilde{\rho}_0).
$$

And the target map $\tilde{\rho}_x\mapsto\tilde{\rho}_x\otimes\tilde{\rho}_x$ is **quadratic**: doubling the deviation of $\tilde{\rho}_x$ from the maximally mixed state quadruples it in the tensor product, since the Bloch vector of the product is $\mathbf{r}\otimes\mathbf{r}$. The two requirements cannot both hold for a set of states that includes a non-orthogonal pair.

### The unitary form of the requirement

The original statement of the theorem concerns a unitary evolution of a composite. A cloning unitary on the tensor-product algebra $\mathbb{B}\otimes\mathbb{B}$ would satisfy

$$
\tilde{U}\bigl(|\psi\rangle\otimes|0\rangle\bigr) = |\psi\rangle\otimes|\psi\rangle
\qquad \text{for every normalized } |\psi\rangle\in S ,
$$

with $\tilde{U}\tilde{U}^\dagger = \tilde{U}^\dagger\tilde{U} = e_0\otimes e_0$. The blank $|0\rangle$ is a fixed unit vector of the second factor, and the requirement is that the same $\tilde{U}$ clones every input. This is the form in which the obstruction is transparent.

## The Algebraic Obstruction

### Overlaps are preserved

Unitary evolution preserves inner products. For two inputs $|\psi\rangle,|\phi\rangle\in S$ and the blank $|0\rangle$,

$$
\bigl\langle \psi\otimes 0 \,\big|\, \phi\otimes 0 \bigr\rangle
= \langle\psi|\phi\rangle\,\langle 0|0\rangle
= \langle\psi|\phi\rangle ,
$$

and since $\tilde{U}$ is unitary this equals $\langle \psi\otimes\psi\,|\,\phi\otimes\phi\rangle$, the overlap of the two outputs.

### Overlaps are squared

Two independent copies have an overlap that factorizes:

$$
\bigl\langle \psi\otimes\psi \,\big|\, \phi\otimes\phi \bigr\rangle
= \langle\psi|\phi\rangle\,\langle\psi|\phi\rangle
= \langle\psi|\phi\rangle^2 .
$$

Equating the two evaluations gives $\langle\psi|\phi\rangle = \langle\psi|\phi\rangle^2$, so $\langle\psi|\phi\rangle\in\{0,1\}$. In terms of the **trace pairing of the idempotents**, which is the modulus squared of the inner product,

$$
\mathrm{Tr}\bigl(\tilde{P}(\psi)\tilde{P}(\phi)\bigr)
= \Bigl(\mathrm{Tr}\bigl(\tilde{P}(\psi)\tilde{P}(\phi)\bigr)\Bigr)^{2}
\qquad\Longrightarrow\qquad
\mathrm{Tr}\bigl(\tilde{P}(\psi)\tilde{P}(\phi)\bigr)\in\{0,1\}.
$$

The pairing is $1$ only for $\psi=\phi$ up to phase, and $0$ only for orthogonal states.

### The obstruction

The conclusion is the no-cloning theorem in the framework's terms:

> A deterministic, universal cloning process exists for a set of pure states if and only if the states are pairwise orthogonal. For any two non-orthogonal rays of the defining module, no unitary $\tilde{U}$ on $\mathbb{B}\otimes\mathbb{B}$ maps $|\psi\rangle\otimes|0\rangle$ to $|\psi\rangle\otimes|\psi\rangle$ for both.

The trace pairing is the algebra's measure of distinguishability: it is $1$ for coincident rays, $0$ for orthogonal rays, and strictly between for all others. Cloning would require it to be idempotent under squaring, and on the interval $[0,1]$ only the endpoints satisfy $x=x^2$. The obstruction is thus a statement about the range of the trace pairing: **a state space whose distinguishability takes intermediate values cannot be cloned.** The maximally mixed state and the pure states are the endpoints of the pairing's range; it is precisely the interior of the range that forbids cloning.

### A concrete pair

The smallest illustration uses the computational ray and the diagonal ray,

$$
|\psi\rangle = |0\rangle, \qquad |\phi\rangle = \tfrac{1}{\sqrt2}\bigl(|0\rangle + |1\rangle\bigr),
\qquad
\langle\psi|\phi\rangle = \tfrac{1}{\sqrt2}, \qquad
\bigl|\langle\psi|\phi\rangle\bigr|^2 = \tfrac12 .
$$

The trace pairing is $\mathrm{Tr}(\tilde{P}(\psi)\tilde{P}(\phi)) = \tfrac12$, strictly inside $(0,1)$. A cloning unitary would have to send both $|\psi\rangle|0\rangle\mapsto|\psi\rangle|\psi\rangle$ and $|\phi\rangle|0\rangle\mapsto|\phi\rangle|\phi\rangle$, preserving the overlap $\tfrac{1}{\sqrt2}$ while the two-copy overlap would be $\tfrac12$; the unitarity would demand $\tfrac{1}{\sqrt2} = \tfrac12$, which is false. In the idempotent form, it would demand $\tfrac12 = \tfrac14$. Hence no unitary clones even this elementary pair. This computation was verified directly: the two-copy overlap was computed as $1/2$ against the one-copy overlap $1/\sqrt2\approx 0.7071$, and they differ.

### Cloning versus copying

For an orthogonal family — for instance the two states of any idempotent basis $\{\tilde{P}_+(\hat{\mu}),\tilde{P}_-(\hat{\mu})\}$ — cloning is possible: the unitary that copies in that basis, $\tilde{U}(|0\rangle\otimes|0\rangle)=|0\rangle\otimes|0\rangle$, $\tilde{U}(|1\rangle\otimes|0\rangle)=|1\rangle\otimes|1\rangle$, does the job. This is not quantum cloning but classical copying in a known basis, and it uses no information about the state beyond the bit that distinguishes the two orthogonal alternatives. The theorem's content is that the ability to copy in one basis confers no ability to copy in any other.

## The Obstruction is Linearity

The unitary argument applies to pure states and to a single input. There is a second form of the obstruction, which applies directly to channels and to mixed states, and which is the reason the theorem survives when the machine is allowed to be noisy.

A channel is affine on the state space. If a channel $\Phi$ cloned all pure states,

$$
\Phi\bigl(\tilde{\rho}\otimes\tilde{\rho}_0\bigr) = \tilde{\rho}\otimes\tilde{\rho}
\qquad \text{for all pure } \tilde{\rho},
$$

then by affinity it would clone every state, pure or mixed, with the same formula; but the map $\tilde{\rho}\mapsto\tilde{\rho}\otimes\tilde{\rho}$ is not affine. For two states and $0<t<1$,

$$
\bigl(t\tilde{\rho}_1+(1-t)\tilde{\rho}_2\bigr)\otimes\bigl(t\tilde{\rho}_1+(1-t)\tilde{\rho}_2\bigr)
\neq t\,\tilde{\rho}_1\otimes\tilde{\rho}_1 + (1-t)\,\tilde{\rho}_2\otimes\tilde{\rho}_2
$$

whenever the cross terms do not cancel, i.e. whenever the states are not orthogonal. The two sides agree only if $t(1-t)(\tilde{\rho}_1\otimes\tilde{\rho}_2+\tilde{\rho}_2\otimes\tilde{\rho}_1 - \tilde{\rho}_1\otimes\tilde{\rho}_1-\tilde{\rho}_2\otimes\tilde{\rho}_2) = 0$, which for non-commuting or non-orthogonal states fails. Hence no affine map clones a non-orthogonal family.

**Linearity is the algebraic content of no-cloning.** The state space of the framework is a convex set, the cone slice of $\mathbb{M}_+$; physical evolution is affine on it; and the cloning target is quadratic. The obstruction is the mismatch of degrees: an affine map is determined by its values on the extreme points with a linearity constraint, while the cloning target imposes a quadratic relation among those values.

## Approximate Cloning

The obstruction is absolute for perfect cloning, so the useful question is how well one can do. For the qubit the optimal universal cloner is known: it takes one copy of an arbitrary state and produces two, each with fidelity

$$
F = \langle\psi|\tilde{\rho}_{\text{out},1}|\psi\rangle = \frac{5}{6} = 0.8333\ldots ,
$$

uniformly in $|\psi\rangle$, and no cloner does better. This is the **Bužek–Hillery bound**, and the machine that attains it is the Bužek–Hillery cloner.

### The cloner in the framework's notation

Let the composite consist of the input qubit $A$, an output qubit $B$ initially in the blank $|0\rangle$, and an ancilla $C$ initially in $|0\rangle$. The standard form of the cloner is defined on two basis inputs by

$$
\begin{aligned}
\tilde{U}\bigl(|0\rangle_A|0\rangle_B|0\rangle_C\bigr)
&= \sqrt{\tfrac23}\,|0\rangle_A|0\rangle_B|0\rangle_C
+ \sqrt{\tfrac16}\bigl(|0\rangle_A|1\rangle_B+|1\rangle_A|0\rangle_B\bigr)|1\rangle_C,\\[4pt]
\tilde{U}\bigl(|1\rangle_A|0\rangle_B|0\rangle_C\bigr)
&= \sqrt{\tfrac23}\,|1\rangle_A|1\rangle_B|1\rangle_C
+ \sqrt{\tfrac16}\bigl(|0\rangle_A|1\rangle_B+|1\rangle_A|0\rangle_B\bigr)|0\rangle_C .
\end{aligned}
$$

The two images are orthonormal, so $\tilde{U}$ extends to a unitary on the three-qubit space. For a general input $|\psi\rangle = a|0\rangle+b|1\rangle$ the linear extension gives the output state; tracing out the ancilla $C$ yields the two-qubit state of the clones, and the two single-clone states are equal by the symmetry of the construction. Direct computation of the fidelity over a family of superposition inputs,

$$
|\psi(\theta,\varphi)\rangle = \cos\tfrac{\theta}{2}\,|0\rangle + e^{i\varphi}\sin\tfrac{\theta}{2}\,|1\rangle ,
$$

gives $\langle\psi|\tilde{\rho}_{\text{out},1}|\psi\rangle = 5/6$ for every $\theta$ and $\varphi$, to machine precision. This was verified numerically on a sample of twenty superpositions; the fidelity was constant at $0.833333$.

### Comparison with measurement and preparation

A classical strategy is to measure the input and prepare two copies of the best guess of the state. For a qubit the optimal single-shot estimate of a uniformly random pure state has fidelity $2/3$, so this strategy achieves $F = 2/3 = 0.6667$, strictly below $5/6$. The quantum cloner's advantage is real and comes from producing clones that are correlated with the input more strongly than any measurement allows. The numbers $5/6$ and $2/3$ are standard; the framework transcribes the cloner into its tensor-product notation, and the reduction of the fidelity to the trace pairing is the only translation involved.

### The fidelity as a trace pairing

The fidelity is a trace pairing: for a pure target state $\tilde{P}(\psi)$ and an output state $\tilde{\rho}_{\text{out}}$,

$$
F = \langle\psi|\tilde{\rho}_{\text{out}}|\psi\rangle = \mathrm{Tr}\bigl(\tilde{P}(\psi)\,\tilde{\rho}_{\text{out}}\bigr) = 2\,\mathrm{Sc}\bigl(\tilde{P}(\psi)\tilde{\rho}_{\text{out}}\bigr),
$$

the same pairing that gives the Born rule. The no-cloning obstruction and its approximate version are therefore both statements about this pairing: perfect cloning would require the pairing of input and clone to attain its maximum $1$ for every input, while the optimal cloner attains $5/6$ uniformly.

## No-Cloning and No-Signalling

There is a physical argument for the obstruction that complements the algebraic one and explains why the theorem must hold if relativity does. Suppose a universal cloner existed. Given one copy of a state drawn from a set of non-orthogonal alternatives, one could produce many copies and then measure a different observable on each copy; with enough copies the state could be identified with arbitrarily small error. Cloning would thus convert a single copy into a statistical sample, making non-orthogonal states distinguishable. But distinguishability of non-orthogonal states, combined with shared entanglement, gives faster-than-light signalling: Alice, sharing an entangled pair with Bob, could choose which of two non-orthogonal ensembles to prepare on her half, and Bob could then determine her choice from his half alone. The algebraic obstruction of this article is therefore not an accident of the framework; it is a necessary feature of any theory whose joint distributions on spacelike-separated systems are consistent, which is exactly the content of the companion articles on the correlation function and the CHSH inequality. In the framework's terms: the trace pairing of the algebra is a **relational** quantity between two subsystems, and no local operation on one subsystem alone may convert it into information about which state the other holds.

## Related No-Go Theorems

The obstruction has companions, all of which are statements about the affine structure of the state space and the trace pairing.

**No-deleting.** Given two copies of an unknown state there is no process that deletes one and leaves the other, unless the two are orthogonal. The proof is the mirror of the cloning proof: a deleting unitary would satisfy $\tilde{U}(|\psi\rangle|\psi\rangle)=|\psi\rangle|0\rangle$ for all $|\psi\rangle$, and the overlap of two outputs is $\langle\psi|\phi\rangle$ while the overlap of two inputs is $\langle\psi|\phi\rangle^2$.

**No-broadcasting.** A mixed state cannot be broadcast: there is no process that takes one copy of a state to two copies for a set of states that do not commute. This is the mixed-state generalization, and it shows that the obstruction is not about purity but about the affine structure of the state space; the framework's state space is the cone slice, and the argument is the same affinity argument as above.

**No-cloning of non-orthogonal states in a known basis.** Even if the family is finite and known, non-orthogonality prevents perfect cloning; the optimal fidelity for cloning a pair of states with overlap $c$ is less than one and depends on $c$. Perfect cloning is recovered only in the orthogonal limit.

In the framework's terms, all three are the statement that the trace pairing cannot be rescaled to its endpoints by an affine map of the cone: physical processes move states within the cone along affine images, and the pairing's interior values are precisely those that cannot be mapped to $0$ or $1$ for an unknown state.

## What the Framework Adds and What It Does Not

**What it does.**

- It expresses the distinguishability of two rays as the trace pairing of their idempotents and shows that it lies in $[0,1]$, with the endpoints corresponding to orthogonal and coincident states.
- It gives the algebraic obstruction as the requirement $\mathrm{Tr}(\tilde{P}_\psi\tilde{P}_\phi) = (\mathrm{Tr}(\tilde{P}_\psi\tilde{P}_\phi))^2$, whose only solutions on the pairing's range are $0$ and $1$; that is, universal cloning is possible exactly for orthogonal families.
- It identifies the deeper obstruction as linearity: physical evolution is affine on the cone slice of $\mathbb{M}_+$, while the cloning target is quadratic.
- It expresses the fidelity of approximate cloning as a trace pairing and transcribes the optimal cloner into the tensor-product algebra, verifying the value $5/6$.

**What it does not.**

- It does not prove the Bužek–Hillery optimality bound; the value $5/6$ is cited as standard, and the construction's fidelity is what was verified here.
- It does not construct all optimal cloners, nor the phase-covariant and state-dependent variants; those are standard and cited.
- It does not extend the analysis to continuous-variable systems or to the tensor-product questions of many qubits beyond the two-clone case.
- It does not predict anything new; the theorem and the optimal fidelity are standard quantum information theory.

## Open Questions

**1. The obstruction and the norm form.** No-cloning is an obstruction about the trace pairing. Is there a formulation in terms of the norm form of the tensor product, and does the norm form's multiplicativity, $N(\tilde{A}\tilde{B}) = N(\tilde{A})N(\tilde{B})$, play the role that the squared inner product plays in the unitary argument?

**2. Cloning and the two sectors.** The algebra splits into $\mathbb{M}_-$ and $\mathbb{M}_+$; the obstruction is stated entirely in $\mathbb{M}_+$. Does the material sector constrain the class of admissible cloning machines, or is it inert here?

**3. Correlated inputs.** The theorem forbids cloning an unknown state. What is the algebraic characterization of the correlations that a cloning machine can exploit, and does the entanglement of the blank with the input modify the bound?

**4. Many copies.** The asymptotic cloning of $n$ copies to $m>n$ copies approaches perfect cloning as $n\to\infty$, with a rate given by the entropy. Does the norm-form reading of the single-qubit entropy extend to the asymptotic cloning rate?

**5. Empirical content.** The no-cloning theorem in biquaternion form is the standard theorem transcribed; it predicts nothing new.

## Summary

The no-cloning theorem states that no physical process copies an unknown quantum state. In the biquaternion framework the distinguishability of two rays is the trace pairing of their idempotents,

$$
\bigl|\langle\psi|\phi\rangle\bigr|^2 = \mathrm{Tr}\bigl(\tilde{P}(\psi)\tilde{P}(\phi)\bigr) \in [0,1],
$$

and a cloning unitary would have to preserve this pairing, because it is an overlap, while the pairing of two independent copies is its square. Equating the two requires

$$
\mathrm{Tr}\bigl(\tilde{P}(\psi)\tilde{P}(\phi)\bigr) = \Bigl(\mathrm{Tr}\bigl(\tilde{P}(\psi)\tilde{P}(\phi)\bigr)\Bigr)^{2},
\qquad\text{hence}\qquad
\mathrm{Tr}\bigl(\tilde{P}(\psi)\tilde{P}(\phi)\bigr)\in\{0,1\}.
$$

Perfect universal cloning is therefore possible exactly for pairwise orthogonal families, where the states are classical alternatives; for any two non-orthogonal rays of the defining module it is impossible. Equivalently, the cloning target $\tilde{\rho}\mapsto\tilde{\rho}\otimes\tilde{\rho}$ is quadratic while every physical evolution is affine on the cone slice of $\mathbb{M}_+$, and the mismatch is the obstruction.

Approximate cloning quantifies the failure. The optimal universal qubit cloner — the Bužek–Hillery machine, transcribed into the tensor-product algebra and verified here — clones every state with fidelity $5/6$, above the best measurement-and-preparation fidelity $2/3$; the fidelity is the trace pairing $\mathrm{Tr}(\tilde{P}(\psi)\tilde{\rho}_{\text{out}})$ of input and output. The companion no-go theorems (no-deleting, no-broadcasting) are the same obstruction in the mirror or in the mixed-state setting.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$ | Two-qubit algebra (input and blank) |
| $\mathbb{M}_+$ | Hermitian subspace (states) |
| $e_0=1,e_1,e_2,e_3$; $i$ | Quaternion units; central imaginary |
| $\tilde{P}(\psi)$ | Rank-one idempotent of a pure state |
| $\mathrm{Tr}(\tilde{P}(\psi)\tilde{P}(\phi)) = |\langle\psi|\phi\rangle|^2$ | Trace pairing (distinguishability) |
| $\tilde{U}$ | Cloning unitary, $\tilde{U}\tilde{U}^\dagger = e_0\otimes e_0$ |
| $\Phi$ | Cloning channel, completely positive trace preserving |
| $\Phi(\tilde{\rho}\otimes\tilde{\rho}_0) = \tilde{\rho}\otimes\tilde{\rho}$ | Cloning requirement |
| $\mathrm{Tr}(P_\psi P_\phi) = (\mathrm{Tr}(P_\psi P_\phi))^2$ | Algebraic obstruction |
| $F = \mathrm{Tr}(\tilde{P}(\psi)\tilde{\rho}_{\text{out}})$ | Cloning fidelity |
| $F = 5/6$ | Bužek–Hillery optimal universal fidelity |
| $F = 2/3$ | Measurement-and-preparation fidelity |
| $|\psi(\theta,\varphi)\rangle$ | Test superposition family |

## Further Reading

- W. K. Wootters and W. H. Zurek, "A single quantum cannot be cloned," *Nature* **299** (1982) 802–803, for the no-cloning theorem.
- D. Dieks, "Communication by EPR devices," *Physics Letters A* **92** (1982) 271–272, for the independent statement of the theorem.
- V. Bužek and M. Hillery, "Quantum copying: beyond the no-cloning theorem," *Physical Review A* **54** (1996) 1844–1852, for the optimal universal cloner and the fidelity $5/6$.
- V. Scarani, S. Iblisdir, N. Gisin, and A. Acín, "Quantum cloning," *Reviews of Modern Physics* **77** (2005) 1225–1256, for the comprehensive review of approximate cloning.
- A. K. Pati and S. L. Braunstein, "Impossibility of deleting an unknown quantum state," *Nature* **404** (2000) 164–165, for no-deleting.
- H. Barnum, C. M. Caves, C. A. Fuchs, R. Jozsa, and B. Schumacher, "Noncommuting mixed states cannot be broadcast," *Physical Review Letters* **76** (1996) 2818–2821, for no-broadcasting.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the inner-product proof and the operational setting.
- The companion articles of this series: *Quantum Mechanics in Biquaternionic Form*, *The Born Rule as a Trace Formula — Derivation and Comparison*, *Quantum Channels and the Reversible/Irreversible Dichotomy*, and *Entangled Subsystems in the Biquaternion Framework*.
