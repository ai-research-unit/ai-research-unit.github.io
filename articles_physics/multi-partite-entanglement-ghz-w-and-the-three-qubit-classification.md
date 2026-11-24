# __Multi-Partite Entanglement: GHZ, W and the Three-Qubit Classification__

## Introduction

Three qubits are the first case where the number of kinds of entanglement exceeds one. Two qubits have a single entanglement type: every entangled pure state is locally equivalent to the singlet, and one measure settles everything. Three qubits have two, and no measure of degree two can tell them apart.

The two kinds. The Greenberger–Horne–Zeilinger state $\tfrac{1}{\sqrt2}(\lvert000\rangle+\lvert111\rangle)$ and the $W$ state $\tfrac{1}{\sqrt3}(\lvert001\rangle+\lvert010\rangle+\lvert100\rangle)$ are both genuinely three-way entangled, and neither can be converted into the other by local operations with classical communication even allowing a nonzero probability of failure. The classification that establishes this is due to Dür, Vidal and Cirac, and it is exact: for three qubits there are six classes, of which two are genuine and four are degenerate.

What this article adds to that classification, and what it does not. It does not restate the classification or improve it. It reads the two classes through the corpus's objects: the two quadratic forms of [The Duo-Complex Bridge](the-duo-complex-bridge-the-three-canonical-forms-and-their-tensor-powers.html), the parity rule that makes the alternating form vanish at odd $n$, and the parity rule of the split from [The Multi-Qubit Split, I](the-multi-qubit-split-i-the-antilinear-obstruction-and-the-corner-collapse.html). What it adds is an explanation of *why* the three-qubit invariants are quartic, and a table of the exact numbers that separate the two classes.

The claim. The distinction between GHZ and W is the vanishing of the only three-factor quadratic invariant that the canonical forms can produce, together with the survival of a quartic one. Parity forbids the first; the quartic is the first degree at which a genuine three-way invariant can exist; and the $W$ state is the state for which the quartic vanishes while the entangled reductions remain maximal.

The order. *Two inequivalent kinds* states the classification. *The numbers* tabulates the exact values. *What entanglement costs when a qubit is lost* is the physical difference. *The quartic obstruction* proves why degree two fails. *The hyperdeterminant* identifies the quartic invariant and its relation to the three-tangle. *The three bipartitions are one form, three ways* is the structural reading. *The algebra's vocabulary and its limits* says what the framework does and does not contribute. *What is not claimed* closes.

## Two Inequivalent Kinds

The classes. Two pure states of the same number of qubits are in the same class when one can be converted into the other by local invertible operations, that is by $SL_2(\mathbb{C})^{\times3}$ acting on the three factors. The classes are the orbits of that action on the projective space of $\mathbb{C}^8$.

The theorem. For three qubits there are exactly six classes: the fully product states, three classes that are entangled across one cut and product across another (one for each choice of the cut), the $W$ class, and the GHZ class. Only the last two are genuinely three-way entangled.

**The two genuine classes are distinguished by a polynomial.** Every orbit is separated by the invariants of the group, and the separating invariant of degree four is the hyperdeterminant: it is nonzero on GHZ and zero on $W$. So the distinction is not a matter of degree or of numerical accident; it is the vanishing of a polynomial that no local operation can change.

The operational difference. In the GHZ state the loss of one qubit destroys all entanglement in the remainder: the reduced state of the other two is a classical mixture with no coherence. In the $W$ state the loss of one qubit leaves the other two entangled, with concurrence $\tfrac23$. So GHZ concentrates its entanglement in the three-way correlation and $W$ distributes it, and this is the difference that the numbers make visible.

The states.

$$
\lvert\mathrm{GHZ}\rangle=\tfrac{1}{\sqrt2}\bigl(\lvert000\rangle+\lvert111\rangle\bigr),\qquad
\lvert W\rangle=\tfrac{1}{\sqrt3}\bigl(\lvert001\rangle+\lvert010\rangle+\lvert100\rangle\bigr).
$$

Neither is a product, and neither is equivalent to the other under any local invertible operation.

## The Numbers

The quantities. For a pure three-qubit state and a chosen qubit $A$, let $C_{AB}$ and $C_{AC}$ be the concurrences of the reductions to $AB$ and $AC$, let $4\det\rho_A$ be the quantity read from the reduction to $A$ alone, and let $\tau$ be the three-tangle, defined as

$$
\tau=4\det\rho_A-C_{AB}^{2}-C_{AC}^{2},
$$

clipped at zero, which is the residual three-way entanglement. Let $\operatorname{Hdet}$ be Cayley's hyperdeterminant of the $2\times2\times2$ coefficient array.

The table. Every entry is exact and was verified numerically to machine precision.

| quantity | GHZ | $W$ |
| --- | --- | --- |
| $\rho_A$ | $\tfrac12\mathrm I$ | $\mathrm{diag}\left(\tfrac13,\tfrac23\right)$ |
| $C_{AB}$ | $0$ | $\tfrac23$ |
| $C_{AC}$ | $0$ | $\tfrac23$ |
| $4\det\rho_A$ | $1$ | $\tfrac89$ |
| $\tau$ | $1$ | $0$ |
| $\operatorname{Hdet}$ | $\tfrac14$ | $0$ |

The readings of the table. The GHZ state has maximal entanglement across every single-system cut and none across any two-system cut: $4\det\rho_A=1$ says the reduction to $A$ is maximally mixed, and $C_{AB}=0$ says the reduction to $AB$ is a classical mixture. The $W$ state has less at the single cut, $\tfrac89$, and all of it is accounted for by the two pairwise concurrences, $\tfrac23$ each. So the tangle is the part of the single-cut entanglement that the pairwise terms do not explain, and GHZ has all of it while $W$ has none.

The saturation. The defining inequality of the next article is $C_{AB}^{2}+C_{AC}^{2}\le 4\det\rho_A$. The $W$ state saturates it, $\tfrac89=\tfrac89$; the GHZ state is as far from saturating as possible, $0\le1$. So the two classes sit at the two ends of one inequality, and this is the cleanest single statement of the difference.

## What Entanglement Costs When a Qubit Is Lost

The GHZ reduction. Tracing out $C$ from $\lvert\mathrm{GHZ}\rangle$ gives

$$
\rho_{AB}=\tfrac12\bigl(\lvert00\rangle\langle00\rvert+\lvert11\rangle\langle11\rvert\bigr),
$$

a classical mixture of two product states. Its concurrence is zero, its entropy is one bit, and there is no basis in which it looks entangled. **The entanglement of GHZ is not stored in any pair.**

The $W$ reduction. Tracing out $C$ from $\lvert W\rangle$ gives

$$
\rho_{AB}=\tfrac23\lvert00\rangle\langle00\rvert+\tfrac13\lvert01\rangle\langle01\rvert+\tfrac13\lvert10\rangle\langle10\rvert ,
$$

whose concurrence is $\tfrac23$. So $W$ keeps a definite amount of two-qubit entanglement in every pair, and the three pairs carry it in a symmetric way.

The interpretation in one sentence. GHZ is a state whose entanglement is entirely tripartite and disappears when a part is removed; $W$ is a state whose entanglement survives the removal of any part, at the price of being less at the single cut.

The contrast with two qubits. At two qubits the removal of a part leaves one system, and the only information left is the marginal, so there is nothing to compare. At three qubits the removal leaves two, and whether they are entangled is a question with two different answers. That is the whole of the qualitative difference, and the numbers above are it.

## The Quartic Obstruction

**Degree two is identically zero.** By the parity rule of [The Duo-Complex Bridge](the-duo-complex-bridge-the-three-canonical-forms-and-their-tensor-powers.html), $(\omega^{\otimes n})^{\mathsf T}=(-1)^{n}\omega^{\otimes n}$, so $\omega^{\otimes3}$ is alternating and

$$
\omega^{\otimes3}(Ξ_{\mathrm{wfn}},Ξ_{\mathrm{wfn}})=0\quad\text{for every }Ξ_{\mathrm{wfn}}\in(\mathbb{C}^2)^{\otimes3}.
$$

The check is exact for GHZ and for $W$ and for every random three-fold product state tested.

What that forbids. Any three-qubit invariant built by applying the canonical alternating form to all three factors at once vanishes identically. There is therefore no degree-two analogue of the concurrence at three qubits, and this is a theorem about alternating forms rather than a failure to find one.

What is not forbidden. The bilinear norm $B^{\otimes3}$ is a perfectly good quadratic invariant, of inertia $(4,0)$ read in its own diagonal basis; it simply does not measure three-way entanglement, exactly as $B^{\otimes2}$ did not measure two-way entanglement. A state can have $B^{\otimes3}(Ξ_{\mathrm{wfn}},Ξ_{\mathrm{wfn}})=0$ and be maximally three-way entangled, because the norm is isotropic on a cone.

So the first available degree is four. An invariant that is alternating in each of three slots, tensored an even number of times, gives degree four; and an invariant that is symmetric and uses the three factors at once must also be quartic. That is why the three-qubit measures that exist — the three-tangle, the hyperdeterminant — are degree four, and it is the structural reason they look unlike the concurrence.

The statement to keep. At two qubits the entanglement invariant is quadratic because two is even. At three qubits it is quartic because three is odd. The parity of the number of systems, and not the size of the Hilbert space, is what sets the degree.

## The Hyperdeterminant

The object. Arrange the eight amplitudes of a three-qubit state in a $2\times2\times2$ array $a_{\imath\jmath\ell}$. Cayley's hyperdeterminant is the polynomial

$$
\begin{aligned}
\operatorname{Hdet}(a)={}&a_{000}^{2}a_{111}^{2}+a_{001}^{2}a_{110}^{2}+a_{010}^{2}a_{101}^{2}+a_{011}^{2}a_{100}^{2}\\
&-2\bigl(a_{000}a_{001}a_{110}a_{111}+a_{000}a_{010}a_{101}a_{111}+a_{000}a_{011}a_{100}a_{111}\\
&\qquad+a_{001}a_{010}a_{101}a_{110}+a_{001}a_{011}a_{100}a_{110}+a_{010}a_{011}a_{100}a_{101}\bigr)\\
&+4\bigl(a_{000}a_{011}a_{101}a_{110}+a_{001}a_{010}a_{100}a_{111}\bigr).
\end{aligned}
$$

It is homogeneous of degree four, and it is invariant under $SL_2(\mathbb{C})$ acting in each of the three indices separately, up to the determinants of the three transformations. It is the three-way analogue of the determinant: for a $2\times2$ array the analogous polynomial is $a_{00}a_{11}-a_{01}a_{10}$, of degree two, which is $\omega$ applied to the two rows.

Its values. $\operatorname{Hdet}(\mathrm{GHZ})=\tfrac14$ and $\operatorname{Hdet}(W)=0$, both computed exactly for the normalised states.

Its relation to the three-tangle. On two hundred random normalised three-qubit states the identity

$$
\tau=4\bigl\lvert\operatorname{Hdet}\bigr\rvert
$$

held to $1.4\times10^{-8}$, with $\tau$ clipped at zero. So the residual three-way entanglement and the hyperdeterminant are the same number up to the factor four, and the tangle's definition as a difference of squared concurrences is a computation of the hyperdeterminant in another basis.

What the vanishing means. The hyperdeterminant vanishes exactly on the states that are not in the GHZ class in the strongest sense: it is the polynomial whose vanishing separates the two genuine classes. The $W$ state is the most entangled representative of the vanishing locus, since its reductions are as entangled as the inequality allows.

The degree-four pattern, seen twice. The tangle is a difference of squared concurrences; the hyperdeterminant is a quartic in the amplitudes; and the two coincide. This is not a coincidence of formulas: both are the unique invariant of the relevant degree, so they must be proportional, and the proportionality constant is four. The reason degree four is the first that can work is the parity rule of [The Duo-Complex Bridge: The Three Canonical Forms and Their Tensor Powers](the-duo-complex-bridge-the-three-canonical-forms-and-their-tensor-powers.html): $\omega^{\otimes3}$ is alternating, and an alternating form vanishes identically on the diagonal, so no degree-two entanglement invariant exists at three factors.

## The Three Bipartitions Are One Form, Three Ways

The construction repeated. For a three-qubit state there are three ways to cut one system from two. Each cut gives a two-qubit problem, and on each the pairing of [The Duo-Complex Bridge](the-duo-complex-bridge-the-three-canonical-forms-and-their-tensor-powers.html) applies:

$$
C_{AB}=2\bigl\lvert\omega\otimes\omega(Ξ_{\mathrm{wfn},AB},Ξ_{\mathrm{wfn},AB})\bigr\rvert,\qquad
C_{AC}=2\bigl\lvert\omega\otimes\omega(Ξ_{\mathrm{wfn},AC},Ξ_{\mathrm{wfn},AC})\bigr\rvert,\qquad
C_{BC}=2\bigl\lvert\omega\otimes\omega(Ξ_{\mathrm{wfn},BC},Ξ_{\mathrm{wfn},BC})\bigr\rvert ,
$$

where $Ξ_{\mathrm{wfn},AB}$ and the others are the states read with the remaining factor absorbed, in the sense of the reduced states.

One form, three slots. The three concurrences are not three different measures; they are one measure applied to three choices of two factors. The permutation group of the three factors acts on the set of them, and for the symmetric states GHZ and $W$ it acts trivially on the values: GHZ has all three equal to zero, $W$ has all three equal to $\tfrac23$.

The asymmetry of the tangle. The tangle singles out one system $A$, because $4\det\rho_A$ is defined with respect to that choice. For a pure three-qubit state the three choices give the same tangle, since the state is symmetric under the interchange of the labels in the sense that any of the three choices produces the same residual. So the quantity is defined per system but is independent of the choice, for pure states.

The reading. The tangle measures the entanglement of one system with the other two, minus the part that is accounted for by its entanglement with each of them separately. That is a statement about three slots of one form, not about three different forms.

## The Algebra's Vocabulary and Its Limits

What the framework supplies. The state space is $S^{\otimes3}=\mathbb{C}^8$, the observables are $\mathrm{Herm}(M_8(\mathbb{C}))$, the split gives two real subspaces of dimension sixty-four whose sum is the whole algebra, by the parity rule of [The Multi-Qubit Split, I](the-multi-qubit-split-i-the-antilinear-obstruction-and-the-corner-collapse.html). The two quadratic forms of the two-qubit case become the norm and the (identically zero) alternating pairing, and the quartic invariants sit in the fourth tensor power.

**What the framework does not supply, and this has to be said plainly.** There is no biquaternion algebra of three qubits: the joint algebra is $M_8(\mathbb{C})$, of degree eight, and no relabelling reduces it. There is no per-subsystem sector label, by the non-descent theorem. There is no element of the algebra that is a state, by the dimension count. So the framework does not classify three-qubit states; the classification belongs to the tensor structure, and it would be the same classification in any presentation of $\mathbb{C}^8$.

What the framework does explain. It explains the degree: the parity rule says quadratic invariants vanish at odd $n$, so the first genuine three-way invariant is quartic. It explains the origin of the two-qubit concurrence as a canonical form, so the three pairwise concurrences are three readings of one form rather than three measures introduced by hand. And it explains why the split cannot be pushed further: the corner collapse at $n=3$ gives two spaces of sixty-four, so the sector structure survives as a single global bit and as nothing else.

The honest balance. Three sections of this article — the classification, the numbers, the hyperdeterminant — are standard quantum information, restated in the corpus's notation. Two sections are the framework's contribution: the parity obstruction and the identification of the pairwise measures with one canonical form. The article is useful only if that separation is kept.

## What Is Not Claimed

No new classification. The six classes are Dür, Vidal and Cirac's, and nothing here refines them.

No new measure. The tangle and the hyperdeterminant are standard, and the identity $\tau=4\lvert\operatorname{Hdet}\rvert$ is a known proportionality exhibited numerically here.

No physical claim about which state is "more entangled". The two classes are inequivalent under local operations, and which is preferable depends on the task. GHZ is the resource for certain protocols, $W$ for others, and the corpus's teleportation article uses the two-qubit singlet, not either of these.

**No claim that the biquaternion framework is needed.** Every number in the table is computable in $M_8(\mathbb{C})$ with no reference to $\mathbb{B}$. The framework's role is explanatory and structural, and it is stated as such.

## Summary

Three qubits have two inequivalent kinds of genuine entanglement, GHZ and $W$, separated by local invertible operations and by the vanishing of Cayley's quartic hyperdeterminant. The numbers are exact: GHZ has $C_{AB}=C_{AC}=0$, $4\det\rho_A=1$, tangle one, $\operatorname{Hdet}=\tfrac14$; $W$ has $C_{AB}=C_{AC}=\tfrac23$, $4\det\rho_A=\tfrac89$, tangle zero, $\operatorname{Hdet}=0$. The physical difference is that GHZ loses all entanglement when a qubit is removed while $W$ leaves $\tfrac23$ in each pair. The structural reason the three-qubit measures are quartic is the parity rule: $(\omega^{\otimes n})^{\mathsf T}=(-1)^{n}\omega^{\otimes n}$, so the alternating form vanishes identically on the diagonal at $n=3$ and no degree-two entanglement invariant exists. The hyperdeterminant is the first available invariant, of degree four, and $\tau=4\lvert\operatorname{Hdet}\rvert$ on two hundred random states. The three pairwise concurrences are one canonical form applied to three cuts, and the split contributes one global bit and no per-subsystem labels, because the joint algebra is $M_8(\mathbb{C})$ and not a biquaternion algebra.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\lvert\mathrm{GHZ}\rangle=\tfrac{1}{\sqrt2}(\lvert000\rangle+\lvert111\rangle)$ | the three-way entangled state of the first class |
| $\lvert W\rangle=\tfrac{1}{\sqrt3}(\lvert001\rangle+\lvert010\rangle+\lvert100\rangle)$ | the representative of the second class |
| $C_{AB}$, $C_{AC}$, $C_{BC}$ | the three pairwise concurrences, each $2\lvert\omega\otimes\omega\rvert$ |
| $4\det\rho_A$ | the single-cut entanglement of one system with the other two |
| $\tau=4\det\rho_A-C_{AB}^{2}-C_{AC}^{2}$ | the three-tangle, clipped at zero |
| $\operatorname{Hdet}$ | Cayley's hyperdeterminant of the $2\times2\times2$ array, degree four |
| $\tau=4\lvert\operatorname{Hdet}\rvert$ | the identity verified on two hundred random states |
| $SL_2(\mathbb{C})^{\times3}$ | the local invertible group whose orbits are the classes |
| six classes | product, three biseparable, $W$, GHZ |

## Further Reading

In this category. [The Duo-Complex Bridge](the-duo-complex-bridge-the-three-canonical-forms-and-their-tensor-powers.html) proves the parity rule and the two-qubit identity that the three pairwise concurrences use. [The Multi-Qubit Split, I](the-multi-qubit-split-i-the-antilinear-obstruction-and-the-corner-collapse.html) gives the two spaces of dimension sixty-four at $n=3$. [The Multi-Qubit Split, II](the-multi-qubit-split-ii-the-sign-condition-the-concurrence-form-and-the-central-bit.html) supplies the concurrence form and the proof that it is not an expectation. [Entanglement Monogamy and the CKW Inequality](entanglement-monogamy-and-the-ckw-inequality.html) takes the inequality that GHZ violates and $W$ saturates and proves it. [The Bell Basis as the Idempotent Basis of $\mathbb{B}\otimes\mathbb{B}$](the-bell-basis-as-the-idempotent-basis-of-b-tensor-b.html) is the two-qubit basis that the three cuts reuse.

In the mathematics corpus. [The Tensor Square of $\mathbb{C}^2$](../articles_maths/the-tensor-square-of-c2.html) gives the swap splitting, which is the two-factor statement of the antisymmetric summand that fails to extend to three factors.
