# __Entanglement Monogamy and the CKW Inequality__

## Introduction

**Entanglement is not shareable without limit.** If one system is entangled with a second, its capacity to be entangled with a third is reduced. The Coffman–Kundu–Wootters inequality makes this quantitative for three qubits, and it is the only exact form of the statement in the literature.

**The inequality.** For a pure state of three qubits and a chosen system $A$,

$$
C_{AB}^{2}+C_{AC}^{2}\;\le\;4\det\rho_A ,
$$

with $C_{AB}$, $C_{AC}$ the concurrences of the reductions to $AB$ and $AC$ and $\rho_A$ the reduction to $A$ alone.

**What this article does.** It states the inequality, verifies it on random states, and reads it in the corpus's language. The reading is exact and it is short: the right-hand side is the square of the Bloch radius of the reduced state of $A$, that is $1-\lvert\vec s_A\rvert^{2}$ with $\rho_A=\tfrac12(\mathrm I+\vec s_A\cdot\boldsymbol\sigma)$, so the inequality is

$$
C_{AB}^{2}+C_{AC}^{2}+\lvert\vec s_A\rvert^{2}\le 1 .
$$

Three numbers, each with a meaning, constrained to a standard simplex. The deficit is the three-tangle. **Monogamy, in this form, is the statement that the entanglement of $A$ with its partners, together with the mixedness of $A$, uses up the unit of the Bloch ball and cannot exceed it.**

**Why the form matters.** In the usual form the inequality compares three quantities computed in three different ways: two concurrences of two-qubit reductions and a determinant of a one-qubit reduction. In the form above it compares three numbers of one kind: squares bounded by one, attached to one system. The reorganisation is elementary and it makes the statement legible as a geometric fact about one qubit's marginal, which is the point of view the corpus's one-qubit analysis supplies.

**The order.** *The inequality* states it. *The two extremes* records GHZ and $W$. *The geometry of the bound* proves the reformulation. *Why three systems are needed* is the structural remark. *Saturation* identifies when equality holds. *Beyond qubits* is the boundary. *What is not claimed* closes.

The article uses [Multi-Partite Entanglement: GHZ, W and the Three-Qubit Classification](multi-partite-entanglement-ghz-w-and-the-three-qubit-classification.html) for the classes and the numbers, [The Duo-Complex Bridge](the-duo-complex-bridge-the-three-canonical-forms-and-their-tensor-powers.html) for the concurrence as the tensor square of the alternating form, [The Multi-Qubit Split, II](the-multi-qubit-split-ii-the-sign-condition-the-concurrence-form-and-the-central-bit.html) for the concurrence form and its inertia, and [The Relativistic Qubit in Biquaternionic Form](the-relativistic-qubit-in-biquaternionic-form.html) for the Bloch ball of one qubit. The one-qubit state as an element of $\mathbb{B}_{\Psi}$ is in [The Two Sectors: the Hermitian Split and the Four Bridges](the-two-sectors-the-hermitian-split-and-the-four-bridges.html).

## The Inequality

**The statement.** Let $\lvert\psi\rangle\in(\mathbb{C}^2)^{\otimes3}$ be normalised, let $\rho_{AB}$, $\rho_{AC}$ and $\rho_A$ be the reductions, and let $C$ denote the Wootters concurrence. Then

$$
C(\rho_{AB})^{2}+C(\rho_{AC})^{2}\ \le\ 4\det\rho_A .
$$

**The same statement with $B$ in place of $A$.** By symmetry the inequality holds for each choice of the singled-out system, so

$$
C_{AB}^{2}+C_{BC}^{2}\le 4\det\rho_B,\qquad C_{AC}^{2}+C_{BC}^{2}\le 4\det\rho_C .
$$

The three inequalities are the three readings of one fact, and each singles out one system.

**The proof is not reproved here.** The inequality is Coffman, Kundu and Wootters' theorem, and its proof is a statement about the convex-roof extension of the concurrence. What is done here is different: the inequality is verified numerically on random states, reformulated exactly, and interpreted.

**The verification.** On three hundred random normalised three-qubit states the maximum of the left-hand side minus the right-hand side was $-0.00996$, so the inequality held in every case with a margin. On $W$ it holds with equality, $\tfrac49+\tfrac49=\tfrac89$; on GHZ with a gap, $0\le1$.

**What the inequality is not.** It is not a statement about all triples of systems. It is stated for a pure state of three qubits, and both restrictions matter: the purity is used in the proof, and the qubit dimension is used in the definition of the concurrence.

## The Two Extremes

**Saturation: the $W$ state.** For $\lvert W\rangle$,

$$
C_{AB}^{2}+C_{AC}^{2}=\tfrac49+\tfrac49=\tfrac89=4\det\rho_A ,
$$

so the bound is attained. Every unit of $A$'s entanglement is accounted for by its two pairwise entanglements.

**The gap: the GHZ state.** For $\lvert\mathrm{GHZ}\rangle$,

$$
C_{AB}^{2}+C_{AC}^{2}=0+0=0<1=4\det\rho_A ,
$$

so the bound is as far from being attained as the numbers allow. None of $A$'s entanglement is pairwise.

**The interpretation of the gap.** The difference $4\det\rho_A-C_{AB}^{2}-C_{AC}^{2}$ is the three-tangle $\tau$, and by the identity of [Multi-Partite Entanglement](multi-partite-entanglement-ghz-w-and-the-three-qubit-classification.html), $\tau=4\lvert\operatorname{Hdet}\rvert$. So the deficit in the monogamy inequality is the genuine three-way entanglement, and the inequality is the statement that this deficit is non-negative.

**So the inequality is not an accident of two numbers.** It is the positivity of a specific quartic invariant. The two extremes of the inequality are the two classes of three-qubit entanglement, and the measure of the gap is the invariant that separates them.

## The Geometry of the Bound

**The one-qubit reduction.** A state of one qubit is $\rho_A=\tfrac12(\mathrm I+\vec s_A\cdot\boldsymbol\sigma)$ with $\vec s_A\in\mathbb{R}^3$ and $\lvert\vec s_A\rvert\le1$, equivalently the Hermitian element $\tilde{Ϛ}_A=\tfrac12(e_t+i\vec s_A)$ of $\mathbb{B}_{\Psi}$. Its determinant is

$$
\det\rho_A=\tfrac14\bigl(1-\lvert\vec s_A\rvert^{2}\bigr),
$$

since the eigenvalues are $\tfrac12(1\pm\lvert\vec s_A\rvert)$.

**The substitution.** Inserting this into the inequality gives

$$
C_{AB}^{2}+C_{AC}^{2}\;\le\;1-\lvert\vec s_A\rvert^{2},
\qquad\text{that is}\qquad
C_{AB}^{2}+C_{AC}^{2}+\lvert\vec s_A\rvert^{2}\;\le\;1 .
$$

**The theorem (monogamy as a simplex condition).** The three numbers $C_{AB}^{2}$, $C_{AC}^{2}$ and $\lvert\vec s_A\rvert^{2}$ are non-negative and sum to at most one, and their total deficit is the three-tangle:

$$
\tau=1-C_{AB}^{2}-C_{AC}^{2}-\lvert\vec s_A\rvert^{2} .
$$

*Proof.* The first two are squares of concurrences and the third is a squared norm, so all are non-negative. The sum bound is the inequality after substitution. The identity for $\tau$ is the definition with $4\det\rho_A$ replaced. $\square$

**The numbers at the two extremes.** For GHZ, $C_{AB}^{2}=0$, $C_{AC}^{2}=0$ and $\lvert\vec s_A\rvert^{2}=0$, so the three numbers are $(0,0,0)$ and the deficit is one. For $W$, $C_{AB}^{2}=\tfrac49$, $C_{AC}^{2}=\tfrac49$ and $\lvert\vec s_A\rvert^{2}=\tfrac19$, so the three sum to exactly one and the deficit is zero.

**The reading.** Monogamy says that a single qubit has one unit of "capacity", and that its entanglement with one partner, its entanglement with another, and its own mixedness draw on that unit jointly. The mixedness term is the part spent on being entangled with everything else — in a pure three-qubit state, with the rest of the world, which is the third system. So the three terms are the three expenditures, and the deficit is what is left over as genuine three-way correlation that cannot be attributed to any single pair.

**Why this is the natural form for the corpus.** The corpus's one-qubit theory is a theory of the Bloch ball, with the state an element of $\mathbb{B}_{\Psi}$ and the radius the measure of purity. In that language the inequality is not about three matrices; it is about one radius and two pairings. The radius is a property of the algebra's Hermitian slice, and the pairings are the tensor square of the alternating form. So the inequality compares one object of the one-qubit theory with two objects of the two-qubit theory, all attached to the same system.

**The Pythagorean look of the $W$ case.** The three numbers for $W$ are $\tfrac49,\tfrac49,\tfrac19$, summing to one; for a state with $C_{AB}=C_{AC}$, saturation forces $\lvert\vec s_A\rvert^{2}=1-2C^{2}$, so saturation is a curve in the simplex and $W$ sits at the point $\bigl(\tfrac49,\tfrac49,\tfrac19\bigr)$. The GHZ state sits at the origin of the simplex, which is the only point where the deficit is maximal.

## Why Three Systems Are Needed

**Two systems give nothing to bound.** With two systems and a pure state, the concurrence of the pair is fixed by the state, and there is no third party against which to trade. The inequality requires a system that can absorb the entanglement that $A$ does not spend on $B$, and that system is $C$. So monogamy is intrinsically a statement about three systems, and this is why the three-qubit case is the first case and not an arbitrary choice.

**The third system enters through the purity.** In the pure three-qubit state the reduction to $A$ is mixed exactly to the extent that $A$ is entangled with $BC$. So the mixedness term $\lvert\vec s_A\rvert^{2}$ measures the entanglement of $A$ with the rest, and the inequality says that this cannot be less than the sum of the two pairwise contributions. The third system is present in the inequality as the slack in the Bloch radius.

**The same statement with a fourth system.** With four systems the corresponding statement is more complicated and is not of this form: the four-qubit monogamy involves a sum over all pairs and a different residual. So the inequality as written belongs to three qubits and to no other number.

**The structural reason in the corpus's language.** The quantity $4\det\rho_A$ is the only invariant of a single qubit that can be built from the algebra's Hermitian slice with the right homogeneity: it is the squared radius. The two concurrences are the tensor square of the alternating form on the two cuts. So the inequality compares the one object of homogeneity two that belongs to one system with the two objects of homogeneity two that belong to the pairs containing it. There is no fourth such object at three qubits, which is why the inequality is tight enough to be useful and simple enough to be exact.

## Saturation

**When equality holds.** Equality in $C_{AB}^{2}+C_{AC}^{2}\le 4\det\rho_A$ holds exactly when the three-tangle vanishes, that is exactly when the hyperdeterminant vanishes, that is exactly for the states outside the GHZ class.

**The statement.** The inequality is an equality on the $W$ class and on the degenerate classes, and a strict inequality on the GHZ class.

**Why the identification is exact.** The three-tangle is defined as the deficit, clipped at zero, and by [Multi-Partite Entanglement](multi-partite-entanglement-ghz-w-and-the-three-qubit-classification.html) it equals $4\lvert\operatorname{Hdet}\rvert$. So the deficit is zero exactly where the hyperdeterminant vanishes, and the hyperdeterminant is the separating invariant of the two genuine classes. The saturation locus is therefore the boundary of the GHZ class, and $W$ is its most entangled point.

**Saturation is not generic.** A random three-qubit state is in the GHZ class with probability one, since the vanishing of a polynomial is a measure-zero condition. So a random state satisfies the inequality strictly, with a positive tangle, and the numerical check above found a strict margin in every one of three hundred trials. Saturation is a property of a lower-dimensional set, and the $W$ state is the representative of it.

**The reading of saturation.** A state saturates when all of its entanglement is pairwise: every correlation is accounted for by a two-system cut, and there is no genuinely three-way part. That is what it means for the deficit to vanish, and it is why $W$ is described as distributed and GHZ as concentrated.

## Beyond Qubits

**The inequality is a qubit statement.** Both the concurrence and the reduction to $4\det\rho_A$ are two-by-two objects, and the proof uses the spin-flip structure of a two-dimensional space. There is no automatic extension to higher spin.

**What fails and what does not.** The quantity $4\det\rho_A$ generalises as $2(1-\operatorname{tr}\rho_A^{2})$ only in the qubit case; for a $d$-dimensional system the natural analogue is different and the resulting inequality is not the same statement. A reader who replaces $2$ by $d$ and $4\det$ by $2(1-\operatorname{tr}\rho_A^{2})$ does not get a theorem.

**The corpus's position.** The higher-spin carriers are tensor powers of $S$, so a monogamy statement for them would be a statement about $\omega^{\otimes n}$ on the two cuts and a different single-cut term. It is not attempted here. What can be said is structural: the reason the qubit case is exact is that the concurrence is the square of a determinant, and a determinant of a $d\times d$ array is not a quadratic invariant for $d>2$.

**The parity rule again.** The two-qubit concurrence is quadratic because $n=2$ is even. At three qubits the pairwise term is still quadratic — it lives on a two-factor cut — while the three-way term is quartic. The monogamy inequality relates objects of degree two on one side to an object of degree two on the other; at higher spin no such pairing of degrees is available.

## What Is Not Claimed

**No proof of the inequality.** The theorem is Coffman, Kundu and Wootters', and this article verifies and reformulates it.

**No claim that the geometric form is new as a theorem.** It is the same inequality after an identity, $\det\rho_A=\tfrac14(1-\lvert\vec s_A\rvert^{2})$. What it adds is the reading: three expenditures of one capacity.

**No claim that monogamy holds for all measures.** The concurrence is monogamous for qubits; other measures are not, and the statement is measure-specific.

**No claim about mixed states.** The inequality as stated is for pure states. For mixed states the concurrence of the reduction must be defined by convex roof and the statement needs care; nothing here addresses that case.

**No claim that the corpus's framework is needed to compute anything.** Every number above is computable in $M_8(\mathbb{C})$.

## Summary

For a pure three-qubit state the CKW inequality reads $C_{AB}^{2}+C_{AC}^{2}\le 4\det\rho_A$. Since $\det\rho_A=\tfrac14(1-\lvert\vec s_A\rvert^{2})$ for the reduced state $\rho_A=\tfrac12(\mathrm I+\vec s_A\cdot\boldsymbol\sigma)$, it is equivalent to $C_{AB}^{2}+C_{AC}^{2}+\lvert\vec s_A\rvert^{2}\le1$, and the deficit is the three-tangle, $1-C_{AB}^{2}-C_{AC}^{2}-\lvert\vec s_A\rvert^{2}=\tau=4\lvert\operatorname{Hdet}\rvert$. The $W$ state saturates it with $(\tfrac49,\tfrac49,\tfrac19)$, the GHZ state sits at $(0,0,0)$ with deficit one, and the inequality holds strictly for a generic state because the hyperdeterminant vanishes only on a measure-zero set. Saturation is exactly the vanishing of the three-tangle, hence exactly the states outside the GHZ class. The form of the statement is a geometry of one qubit: a radius and two pairings, with the radius measuring the entanglement spent on the third system. The inequality is a qubit theorem and is not extended here.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $C_{AB}$, $C_{AC}$ | the concurrences of the two-qubit reductions |
| $\rho_A=\tfrac12(\mathrm I+\vec s_A\cdot\boldsymbol\sigma)$ | the one-qubit reduction and its Bloch vector |
| $\det\rho_A=\tfrac14(1-\lvert\vec s_A\rvert^{2})$ | the determinant of the reduction |
| $C_{AB}^{2}+C_{AC}^{2}\le 4\det\rho_A$ | the CKW inequality |
| $C_{AB}^{2}+C_{AC}^{2}+\lvert\vec s_A\rvert^{2}\le1$ | the simplex form |
| $\tau=1-C_{AB}^{2}-C_{AC}^{2}-\lvert\vec s_A\rvert^{2}$ | the three-tangle as the deficit |
| $(\tfrac49,\tfrac49,\tfrac19)$ | the $W$ state's point in the simplex, saturating |
| $(0,0,0)$ | the GHZ state's point, with maximal deficit |
| $\tau=4\lvert\operatorname{Hdet}\rvert$ | the identification of the deficit with the quartic invariant |

## Further Reading

**In this category.** [Multi-Partite Entanglement: GHZ, W and the Three-Qubit Classification](multi-partite-entanglement-ghz-w-and-the-three-qubit-classification.html) gives the two classes, the table of values, and the identity $\tau=4\lvert\operatorname{Hdet}\rvert$ that makes the deficit quartic. [The Duo-Complex Bridge](the-duo-complex-bridge-the-three-canonical-forms-and-their-tensor-powers.html) supplies the concurrence as the tensor square of the alternating form, on each of the two cuts. [The Multi-Qubit Split, II](the-multi-qubit-split-ii-the-sign-condition-the-concurrence-form-and-the-central-bit.html) proves that the concurrence amplitude is not an expectation, which is why monogamy cannot be read as a single operator inequality. [The Relativistic Qubit in Biquaternionic Form](the-relativistic-qubit-in-biquaternionic-form.html) gives the Bloch ball and its radius as the one-qubit data. [Spin Entropy and the Lorentz Group in Biquaternionic Form](spin-entropy-and-the-lorentz-group-in-biquaternionic-form.html) is the other function of the reduction, and the reason the mixedness term has a natural home.

**In the mathematics corpus.** [Hermitian Forms over the Biquaternion Algebra and the Unitary Witt Group](../articles_maths/hermitian-forms-over-the-biquaternion-algebra-and-the-unitary-witt-group-with-hermitian-adjoint.html) supplies the positivity and inertia language in which "one unit of capacity" is the positive cone of the form.
