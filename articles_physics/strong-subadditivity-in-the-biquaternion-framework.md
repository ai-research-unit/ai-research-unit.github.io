# __Strong Subadditivity in the Biquaternion Framework__

## Introduction

**Strong subadditivity** is the fundamental inequality of quantum entropy theory. For a state of three subsystems $A$, $B$, $C$ it reads
$$
S(\rho_{ABC})+S(\rho_B)\ \le\ S(\rho_{AB})+S(\rho_{BC}),
$$
and it says that the entropy of a composite is subadditive in a way that survives the overlap of the two pairs. It is stronger than the ordinary subadditivity $S(\rho_{AB})\le S(\rho_A)+S(\rho_B)$, and it is the one inequality from which the monotonicity of relative entropy under every physical process follows — or, in the direction that is usually used, from which it follows. It was proved by Lieb and Ruskai in 1973, and it remains the sharpest general statement of its kind: no inequality stronger than strong subadditivity holds for all tripartite states.

This article asks what strong subadditivity is in the biquaternion framework. The answer has the same three-part shape as the companion article on relative entropy.

1. **The inequality is standard and is inherited unchanged.** The biquaternion algebra's tensor powers $\mathbb{B}^{\otimes n}$ are matrix algebras, the states are density matrices, the reduced states are partial traces, and the entropies are von Neumann entropies of the reduced density matrices. Strong subadditivity therefore holds for biquaternion states by the theorem that holds for all density matrices. The framework neither strengthens nor weakens it.

2. **The framework makes the structure explicit.** The article derives the inequality from the monotonicity of the biquaternion relative entropy of the preceding article, exhibits the Schmidt decomposition of the states it needs, and computes the three distinguishing tripartite examples — the GHZ state, the W state, and a Markov (equality) state — directly on the tensor product of algebras.

3. **The framework has a specific limitation, and it is the same one as the Fock-space article's.** The tensor power $\mathbb{B}^{\otimes n}$ is not contained in $\mathbb{B}$: it is $M_{2^n}(\mathbb{C})$, of complex dimension $4^n$. The partial trace and the inequality therefore live outside the four-dimensional algebra, on its modules and their tensor products. Strong subadditivity is a statement about the many-mode states the framework builds, not about the algebra itself.

The article proceeds as follows. The inequality and its equivalent forms are recalled. The tensor-product setting in the biquaternion algebra is fixed, with the partial trace written explicitly. The inequality is derived from monotonicity of relative entropy. The three examples are computed. The equality condition is stated as the quantum Markov property. The field-theoretic setting is recalled, and the article closes with the established/interpretation/open split.

**Conventions.** Those of the companion articles. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with quaternion basis $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, scalar imaginary $i$, and isomorphism $\Phi(e_k)=-i\sigma_k$, $\Phi(i)=iI_2$, so that $\mathbb{B}\cong M_2(\mathbb{C})$. The material and informational subspaces are $\mathbb{M}_-$ and $\mathbb{M}_+$, with $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ and $i\mathbb{M}_\pm=\mathbb{M}_\mp$. The trace is normalized by the matrix representation, $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$, with $\mathrm{Tr}(e_0)=2$. The relative entropy and its monotonicity are those of *Relative Entropy and the Biquaternion Framework*. The single-mode states and the vacuum idempotent are those of *The GNS Construction in the Biquaternion Framework* and *The Biquaternion Vacuum as a Minimal Idempotent*.

## The Inequality

### Statement

Let $\rho_{ABC}$ be a density matrix on a tensor product $\mathcal H_A\otimes\mathcal H_B\otimes\mathcal H_C$ of finite-dimensional Hilbert spaces, and let
$$
\rho_{AB}=\mathrm{Tr}_C\,\rho_{ABC},\qquad
\rho_{BC}=\mathrm{Tr}_A\,\rho_{ABC},\qquad
\rho_B=\mathrm{Tr}_{AC}\,\rho_{ABC},
$$
be the reduced states. **Strong subadditivity** is the inequality
$$
S(\rho_{ABC})+S(\rho_B)\ \le\ S(\rho_{AB})+S(\rho_{BC}),
$$
with $S(\rho)=-\mathrm{Tr}(\rho\log\rho)$. Equivalently, in terms of the **conditional entropy** $S(A|B):=S(\rho_{AB})-S(\rho_B)$,
$$
S(A|BC)\ \le\ S(A|B),
$$
the conditional entropy is non-increasing as more conditioning is added. The equivalence is immediate:
$$
S(A|BC)-S(A|B)
=\big[S(\rho_{ABC})-S(\rho_{BC})\big]-\big[S(\rho_{AB})-S(\rho_B)\big]
=S(\rho_{ABC})+S(\rho_B)-S(\rho_{AB})-S(\rho_{BC}),
$$
which is the negative of the deficit in the first form.

### Equivalent Forms

Three forms are used below, and their equivalence is standard.

1. **Monotonicity of relative entropy.** For any completely positive trace-preserving map $\Lambda$, $S(\Lambda\rho\|\Lambda\sigma)\le S(\rho\|\sigma)$. Taking $\Lambda=\mathrm{Tr}_C$ gives the partial-trace form, and the partial-trace form is equivalent to strong subadditivity when applied to the state built below. Lieb and Ruskai's proof of strong subadditivity is the proof that relative entropy is monotone.
2. **Joint convexity of relative entropy.** The joint convexity
$$
S\big(p\rho_1+(1-p)\rho_2\,\big\|\,p\sigma_1+(1-p)\sigma_2\big)
\le p\,S(\rho_1\|\sigma_1)+(1-p)\,S(\rho_2\|\sigma_2)
$$
is equivalent to the monotonicity, hence to strong subadditivity.
3. **Positivity of a relative entropy.** For the positive operator
$$
\sigma_{ABC}:=\exp\Big(\log\rho_{AB}\otimes I_C+I_A\otimes\log\rho_{BC}-I_{AC}\otimes\log\rho_B\Big),
$$
built from the $AB$, $BC$ and $B$ marginals of $\rho_{ABC}$, strong subadditivity is the statement $S(\rho_{ABC}\|\sigma_{ABC})\ge0$. The operator is subnormalized rather than normalized, $\mathrm{Tr}\,\sigma_{ABC}\le1$, with equality whenever the three marginal-built operators commute — that is, whenever $\rho_{AB}$, $\rho_{BC}$ and $\rho_B$ are simultaneously diagonal in a product basis, which is the classical case in which the construction reduces to the conditional product $p_{ab}p_{bc}/p_b$. What holds for every faithful $\rho_{ABC}$ is the identity
$$
\mathrm{Tr}\big(\rho_{ABC}\log\sigma_{ABC}\big)
=-S(\rho_{AB})-S(\rho_{BC})+S(\rho_B),
$$
so that $S(\rho_{ABC}\|\sigma_{ABC})$ equals the deficit identically.

The third form is the one used in the examples below, because $\log\sigma_{ABC}$ is built from the closed-form biquaternion logarithms of the companion article; the proof of the inequality itself is the product-state form of the section on monotonicity.

### Why It Is the Fundamental Inequality

Strong subadditivity is fundamental for three reasons, none of them special to the framework.

- **It implies the other entropic inequalities.** Subadditivity $S(\rho_{AB})\le S(\rho_A)+S(\rho_B)$, the Araki–Lieb triangle inequality $|S(\rho_A)-S(\rho_B)|\le S(\rho_{AB})$, and the concavity of entropy all follow from it or from its relatives, while it does not follow from them.
- **It is equivalent to data processing.** The monotonicity of relative entropy under every completely positive trace-preserving map — the statement that no physical process can make two states more distinguishable — is equivalent to strong subadditivity. The inequality is therefore not merely an entropy inequality: it is the statement that information is not created by local operations.
- **It is sharp.** No inequality stronger than strong subadditivity holds for all tripartite states; the equality case is characterized completely, and it is the quantum Markov property stated below.

## The Biquaternion Tensor Product

### States of the Tensor Power

The framework's many-mode states live in the tensor power
$$
\mathbb{B}^{\otimes n}=\underbrace{\mathbb{B}\otimes_\mathbb{C}\cdots\otimes_\mathbb{C}\mathbb{B}}_{n}
\;\cong\;M_2(\mathbb{C})^{\otimes n}\;\cong\;M_{2^n}(\mathbb{C}),
$$
of complex dimension $4^n$. The trace on the tensor power is the product of the single-algebra traces,
$$
\mathrm{Tr}\big(\tilde A_1\otimes\cdots\otimes\tilde A_n\big)
=\mathrm{Tr}(\tilde A_1)\cdots\mathrm{Tr}(\tilde A_n),
\qquad
\mathrm{Tr}\big(e_0^{\otimes n}\big)=2^n,
$$
and a state is an element
$$
\tilde\rho_n\in\big(\mathbb{M}_+^{\otimes n}\big),\qquad
\tilde\rho_n\ge0,\qquad
\mathrm{Tr}(\tilde\rho_n)=1 .
$$
For $n=1$ this is the Bloch ball of the GNS companion article; for $n\ge2$ it is the set of $2^n\times2^n$ density matrices, and the entropy functional is
$$
S(\tilde\rho_n)=-\mathrm{Tr}\big(\tilde\rho_n\log\tilde\rho_n\big),
$$
the ordinary von Neumann entropy with the product trace. Every state of the tensor power is a density matrix, so every theorem about density matrices applies to it. This is the sense in which the framework inherits strong subadditivity.

The tensor power is not a subalgebra of $\mathbb{B}$. The dimension already says so: $\dim_\mathbb{C}\mathbb{B}^{\otimes n}=4^n$ while $\dim_\mathbb{C}\mathbb{B}=4$, and the two agree only at $n=1$. This is the same capacity statement as in the Fock-space companion article, where the algebra carries exactly one fermionic mode: everything beyond one mode is built on the outside, on modules over $\mathbb{B}$, and the many-mode states are states of those modules.

### Partial Trace and Reduced States

The partial trace is the map that discards a factor. In the matrix representation, for a bipartite state $M$ on the basis $|ij\rangle$,
$$
\big(\mathrm{Tr}_B M\big)_{ii'}=\sum_j M_{ij,i'j},
$$
and it is completely positive and trace preserving. Its image is a state of the remaining factor: if $M\ge0$ and $\mathrm{Tr}M=1$ then $\mathrm{Tr}_B M\ge0$ with trace one. Applied twice it gives the single-subsystem marginals. The biquaternion content of the operation is only the trace that enters it: on a factor, $\mathrm{Tr}_B(\tilde A\otimes\tilde B)=\tilde A\,\mathrm{Tr}(\tilde B)=\tilde A\cdot2\,\mathrm{Sc}(\tilde B)$, so the biquaternion trace $2\,\mathrm{Sc}$ is exactly the normalization that makes the discarded factor contribute its expectation.

Two structural facts are worth recording at this point, both consequences of the GNS companion article's trace. First, on a product the partial trace is the identity on the rest, $\mathrm{Tr}_B(\tilde A\otimes\tilde B)=\tilde A\,\mathrm{Tr}(\tilde B)=\tilde A$ for every normalized $\tilde B$, so discarding a factor that is in a state of its own produces no entanglement across the cut. Second, the discarded factor's entropy is nevertheless part of the entropy of the whole, $S(\tilde A\otimes\tilde B)=S(\tilde A)+S(\tilde B)$, and its two extreme values are $0$ on the **pure** boundary and $\log2$ at the **trace state** $\tfrac12 e_0$. The pure boundary and the trace state are therefore the two ends of the Bloch ball that agree in what they contribute to the reduced state of the rest and differ in what they contribute to the entropy of the whole, and they are the two ends that appear in the examples below.

## Strong Subadditivity from Monotonicity of Relative Entropy

The derivation is standard and is transcribed here in the biquaternion notation, because it is the bridge between the two articles of this subcategory.

Write $a=\rho_{AB}\otimes I_C$, $b=I_A\otimes\rho_{BC}$, $c=I_{AC}\otimes\rho_B$ for the three operators built from the marginals, and let
$$
\tilde\sigma_{ABC}:=\exp\big(\log a+\log b-\log c\big).
$$
The three operators do not commute in general — $a$ is nontrivial on $AB$, $b$ on $BC$, and the two share $B$ — so $\log a+\log b-\log c$ is not the logarithm of the product $abc$. It is the logarithm of $\tilde\sigma_{ABC}$ by construction: the exponential of a Hermitian algebra element is positive and nonsingular, and its logarithm is that element. Hence
$$
\mathrm{Tr}\big[\tilde\rho_{ABC}\log\tilde\sigma_{ABC}\big]
=\mathrm{Tr}\big[\tilde\rho_{ABC}\log a\big]
+\mathrm{Tr}\big[\tilde\rho_{ABC}\log b\big]
-\mathrm{Tr}\big[\tilde\rho_{ABC}\log c\big],
$$
and each term is a marginal identity,
$$
\mathrm{Tr}\big[\tilde\rho_{ABC}\log a\big]
=\mathrm{Tr}_{AB}\big[\rho_{AB}\log\rho_{AB}\big]=-S(\rho_{AB}),
$$
and its analogues, which use only that the $AB$ marginal of $\rho_{ABC}$ is $\rho_{AB}$ and that $\log a$ acts trivially on $C$. With these,
$$
S(\tilde\rho_{ABC}\|\tilde\sigma_{ABC})
=\mathrm{Tr}\big[\tilde\rho_{ABC}\log\tilde\rho_{ABC}\big]
-\mathrm{Tr}\big[\tilde\rho_{ABC}\log\tilde\sigma_{ABC}\big]
=-S(\rho_{ABC})+S(\rho_{AB})+S(\rho_{BC})-S(\rho_B).
$$
The right-hand side is the deficit itself, so the third form is exactly equivalent to the inequality rather than an independent route to it: $S(\tilde\rho_{ABC}\|\tilde\sigma_{ABC})\ge0$ **is** strong subadditivity. The operator $\tilde\sigma_{ABC}$ is subnormalized rather than normalized, $\mathrm{Tr}\,\tilde\sigma_{ABC}\le1$ — the value one is attained on the classical states diagonal in the product basis, where the construction is the classical conditional product $p_{ab}p_{bc}/p_b$, and it is strictly below one on the non-commuting states tested here — so the quantity is not the relative entropy of a pair of states, and Klein's inequality is not what makes it non-negative.

The proof is cleanest in the form in which both reference states are products. Partial trace is a completely positive trace-preserving map, so by the monotonicity of relative entropy the pair $(\rho_{ABC},\rho_{AB}\otimes\rho_C)$ dominates its image $(\rho_{BC},\rho_B\otimes\rho_C)$ under $\mathrm{Tr}_A$:
$$
S(\rho_{ABC}\|\rho_{AB}\otimes\rho_C)\ \ge\ S(\rho_{BC}\|\rho_B\otimes\rho_C).
$$
Each side is evaluated by the same marginal identities,
$$
S(\rho_{ABC}\|\rho_{AB}\otimes\rho_C)=-S(\rho_{ABC})+S(\rho_{AB})+S(\rho_C),
\qquad
S(\rho_{BC}\|\rho_B\otimes\rho_C)=-S(\rho_{BC})+S(\rho_B)+S(\rho_C),
$$
and their difference is $S(\rho_{AB})+S(\rho_{BC})-S(\rho_{ABC})-S(\rho_B)$, the deficit. The inequality is therefore strong subadditivity, and the only inputs are the companion article's relative entropy and the completely positive trace-preserving character of the partial trace, both of which hold for the framework's states by the general theory. The chain of reasoning is:

> relative entropy is monotone under the partial trace (the data-processing inequality) $\Longrightarrow$ the difference of the two relative entropies in the product-state form is non-negative $\Longrightarrow$ strong subadditivity.

## Three Tripartite States

The inequality is checked on three states that between them display strictness, and equality. All entropies are computed from the reduced density matrices by partial trace; the numbers are given to six decimals.

### The GHZ State

Take the three-qubit state
$$
|GHZ\rangle=\frac{1}{\sqrt2}\big(|000\rangle+|111\rangle\big).
$$
It is pure, so $S(\rho_{ABC})=0$. Its single-subsystem marginals are maximally mixed, $\rho_A=\rho_B=\rho_C=\tfrac12 I$, each of entropy $\log2=0.693147$, and its pair marginals are the classically correlated states
$$
\rho_{AB}=\rho_{BC}=\tfrac12\big(|00\rangle\langle00|+|11\rangle\langle11|\big),
$$
each of entropy $\log2$ as well. The inequality reads
$$
S(\rho_{ABC})+S(\rho_B)=0+\log2=0.693147,
\qquad
S(\rho_{AB})+S(\rho_{BC})=2\log2=1.386294,
$$
so the deficit is $\log2=0.693147$: strong subadditivity is strict by one full bit. The state is not a Markov chain.

### The W State

Take
$$
|W\rangle=\frac{1}{\sqrt3}\big(|001\rangle+|010\rangle+|100\rangle\big).
$$
It is pure, so $S(\rho_{ABC})=0$. Each single-subsystem marginal is
$$
\rho_A=\rho_B=\rho_C=\mathrm{diag}\big(\tfrac23,\tfrac13\big),
\qquad
S=\tfrac23\log\tfrac32+\tfrac13\log3=0.636514,
$$
and each pair marginal is obtained by tracing the third factor; for $AB$, the $|01\rangle$ and $|10\rangle$ components carry the same value of $C$ and their cross term survives, so
$$
\rho_{AB}=\tfrac13|00\rangle\langle00|
+\tfrac13\big(|01\rangle+|10\rangle\big)\big(\langle01|+\langle10|\big),
$$
with eigenvalues $\tfrac23,\tfrac13,0$ and entropy
$$
S(\rho_{AB})=\tfrac13\log3+\tfrac23\log\tfrac32=h\big(\tfrac13\big)=0.636514,
$$
the same value as the single-subsystem entropy, as the purity of $\rho_{ABC}$ requires. The inequality reads
$$
S(\rho_{ABC})+S(\rho_B)=0.636514,
\qquad
S(\rho_{AB})+S(\rho_{BC})=1.273028,
$$
so the deficit is $h(1/3)=0.636514$. It is smaller than the GHZ deficit, and the reason is arithmetic: for a pure tripartite state the deficit is $S(\rho_{AB})+S(\rho_{BC})-S(\rho_B)$, and the W marginals carry strictly less entropy than the maximally mixed GHZ marginals.

### A Markov State, Where the Inequality Is Tight

Take a state in which $C$ is decoupled from a correlated pair $AB$,
$$
\rho_{ABC}=\rho_{AB}\otimes|0\rangle\langle0|_C,
\qquad
\rho_{AB}=\cos^2\theta\,|00\rangle\langle00|+\sin^2\theta\,|11\rangle\langle11| .
$$
The pair $AB$ is classically correlated — the ensemble of $|\psi_\theta\rangle=\cos\theta|00\rangle+\sin\theta|11\rangle$ with its coherence removed — and $C$ is attached as an independent record. Then $\rho_B=\cos^2\theta|0\rangle\langle0|+\sin^2\theta|1\rangle\langle1|$ and $\rho_{BC}=\rho_B\otimes|0\rangle\langle0|_C$, and because $C$ is in a pure state the entropies are those of $AB$ and $B$,
$$
S(\rho_{ABC})=S(\rho_{AB})=h(\cos^2\theta),\qquad
S(\rho_{BC})=S(\rho_B)=h(\cos^2\theta),
$$
with $h(p)=-p\log p-(1-p)\log(1-p)$ the binary entropy. Both sides of the inequality equal $2h(\cos^2\theta)$, so it holds with equality for every $\theta$. At $\theta=0.3$, $2h(\cos^2\theta)=0.592643$; at $\theta=0.7$, it is $1.357265$; the deficit is zero in both cases. The state is the simplest quantum Markov chain, $C$ being attached to a classical record, and it exhibits the equality condition exactly.

### The Three Cases Together

| State | $S(\rho_{ABC})$ | $S(\rho_B)$ | $S(\rho_{AB})$ | $S(\rho_{BC})$ | Deficit |
|---|---|---|---|---|---|
| GHZ | $0$ | $0.693147$ | $0.693147$ | $0.693147$ | $0.693147$ |
| W | $0$ | $0.636514$ | $0.636514$ | $0.636514$ | $0.636514$ |
| Markov | $h$ | $h$ | $h$ | $h$ | $0$ |

The table is the article's quantitative content. The GHZ deficit is one full bit, the value $\log2$; the W deficit is $h(1/3)=0.636514$, smaller because the W marginals are not maximally mixed; and the Markov state saturates for every value of its parameter. All rows were recomputed from the partial traces of the explicit $8\times8$ density matrices in the matrix representation, and all satisfy the inequality.

## The Equality Condition

The equality case is completely characterized, and the characterization is worth stating because the framework's Markov examples are its instances.

> **Theorem (Hayden–Jozsa–Petz–Winter).** Strong subadditivity is saturated for $\rho_{ABC}$ if and only if the Hilbert space of $B$ decomposes as $\mathcal H_B=\bigoplus_k\mathcal H_{b_k^L}\otimes\mathcal H_{b_k^R}$ in such a way that
> $$
> \rho_{ABC}=\bigoplus_k p_k\ \rho_{A b_k^L}\otimes\rho_{b_k^R C},
> \qquad p_k\ge0,\quad \sum_k p_k=1 .
> $$
> The state is then a **quantum Markov chain**: $B$ is a "bridge" whose left part $b_k^L$ carries the correlation to $A$ and whose right part $b_k^R$ carries it to $C$, with no correlation between $A$ and $C$ conditional on $B$.

The Markov state of the previous section is the special case in which the decomposition of $\mathcal H_B$ is trivial and $\rho_{ABC}=\rho_{AB}\otimes\rho_C$ with $C$ attached as a record. The information-theoretic reading is that strong subadditivity measures the failure of the chain condition: the deficit $S(\rho_{AB})+S(\rho_{BC})-S(\rho_{ABC})-S(\rho_B)$ is the "conditional mutual information" $I(A:C|B)$, which is the amount of correlation between $A$ and $C$ that survives conditioning on $B$ and is therefore the obstruction to the Markov property. That the conditional mutual information is non-negative **is** strong subadditivity, and it is the quantity the framework's entropies compute.

## Strong Subadditivity in Quantum Field Theory

The inequality is inherited by the framework's many-mode states because they are density matrices. In the field setting it is inherited in a more delicate sense, and the delicacy is standard.

**For a regulator, the inequality holds exactly.** Lattice or otherwise regularized field theories have finite-dimensional local Hilbert spaces, and strong subadditivity holds for every state of the regulated theory, including the vacuum. It is the inequality that controls the monotonicity of entanglement entropy under coarse-graining and under the renormalization group.

**In the continuum, the region statement requires care.** The entropies of regions are divergent and the local algebras are type III, so the inequality as written for regions must be regulated or restated in terms of relative entropies. The version that survives is the **monotonicity of relative entropy** under the inclusion of regions, and it is the relative-entropy form — the first equivalent form above — that the algebraic treatments use. This is the same reason the companion article on relative entropy treats relative entropy rather than entanglement entropy as the primary quantity.

**The consequences are standard.** Strong subadditivity gives the monotonicity of entanglement entropy under the renormalization group, the entropic proofs of the $c$-theorem in two dimensions and of its higher-dimensional relatives, and the inequalities that constrain the entanglement structure of the vacuum. These are cited as standard and are not re-derived here.

The framework's contribution to this is exactly its contribution to the finite-dimensional case: it supplies the tensor powers $\mathbb{B}^{\otimes n}$, the partial traces on them, and the entropy functional, and it computes the finite models in which the inequality can be checked by hand. It supplies no field-theoretic strengthening of the inequality.

## What Is Established and What Is Interpretation

**Established (theorem, imported).** Strong subadditivity (Lieb–Ruskai); its equivalence to the monotonicity and to the joint convexity of relative entropy; the data-processing interpretation; the Hayden–Jozsa–Petz–Winter equality condition; the monotonicity of entanglement entropy under coarse-graining that strong subadditivity implies. All standard.

**Established (recomputed here).** The tensor power $\mathbb{B}^{\otimes n}\cong M_{2^n}(\mathbb{C})$ with the product trace; the partial trace as a completely positive trace-preserving map on the framework's states; the derivation of strong subadditivity from the monotonicity of the biquaternion relative entropy, with the reference-operator identity $S(\rho_{ABC}\|\sigma_{ABC})=S(\rho_{AB})+S(\rho_{BC})-S(\rho_B)-S(\rho_{ABC})$; and the three tripartite examples, with the tabulated entropies and deficits.

**Interpretation.** That the biquaternion algebra's tensor powers give an information-theoretic reading of the inequality in which the conditional mutual information $I(A:C|B)$ is the arithmetic quantity computed from the framework's entropies, and that the Markov saturation is the framework's equality case.

**Gaps, left visible.** The tensor power is not a subalgebra of $\mathbb{B}$; the inequality lives on the many-mode modules. The framework supplies no state selection and no dynamics, and no field-theoretic strengthening. No empirical consequence is derived.

## Open Questions

**1. A biquaternion witness for the deficit.** The deficit is the conditional mutual information. Is there a biquaternion observable whose expectation is this quantity, in the way that the modular Hamiltonian's expectation is the relative entropy? The trace formula gives the expectation of any Hermitian element, so the question is whether $I(A:C|B)$ can be written as $2\,\mathrm{Sc}$ of a single algebra element of $\mathbb{B}^{\otimes3}$.

**2. The Markov decomposition in the algebra.** The equality condition is an algebraic decomposition of $\mathcal H_B$. Does the decomposition have a reading in terms of the idempotent structure of $\mathbb{B}^{\otimes3}$, the minimal idempotents of the GNS companion article, and the partial traces between them?

**3. The continuum limit.** The region statement is a relative-entropy statement. Does the framework's closed-form relative entropy, applied to a regulated lattice and continued to the continuum, reproduce the standard monotonicity of entanglement entropy under region inclusion?

**4. The operation count.** The partial trace is one completely positive map; the data-processing inequality holds for all of them. Which completely positive maps on $\mathbb{B}^{\otimes n}$ are native to the framework's sector structure, in the sense of the reversible/irreversible dichotomy of $\mathbb{M}_+$?

**5. Empirical contact.** As everywhere in the subcategory, no prediction distinguishing the reading from standard quantum information theory is derived.

## Summary

Strong subadditivity, $S(\rho_{ABC})+S(\rho_B)\le S(\rho_{AB})+S(\rho_{BC})$, is the fundamental inequality of quantum entropy theory. It is equivalent to the monotonicity of relative entropy under every completely positive trace-preserving map — the statement that information is never created by local operations — and it is sharp, its equality case being the quantum Markov property.

In the biquaternion framework the many-mode states live in the tensor powers $\mathbb{B}^{\otimes n}\cong M_{2^n}(\mathbb{C})$, with the product trace and the partial trace as the completely positive map that discards a factor. The inequality follows from the monotonicity of the biquaternion relative entropy of the companion article, applied to reference states built from the $AB$, $BC$ and $B$ marginals. The derivation is the framework's transcription of the standard argument, and the arithmetic is the framework's own: on the GHZ state the deficit is $0.693147$; on the W state it is $0.636514$; on the Markov state it is zero, and it is zero for every parameter.

The tensor power is not a subalgebra of $\mathbb{B}$, whose complex dimension is four. The inequality is therefore a statement about the many-mode states built from the algebra's modules, not about the algebra itself, and the framework's contribution is the finite-dimensional realization and the explicit arithmetic rather than any strengthening of the theorem.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Scalar imaginary, central, $i^2=-1$ |
| $\mathbb{M}_+,\mathbb{M}_-$ | Informational (Hermitian) and material (anti-Hermitian) subspaces |
| $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$ | Trace pairing; $\mathrm{Tr}(e_0)=2$ |
| $\mathbb{B}^{\otimes n}\cong M_{2^n}(\mathbb{C})$ | Tensor power; many-mode algebra |
| $\mathrm{Tr}(\tilde A_1\otimes\cdots\otimes\tilde A_n)=\prod_i\mathrm{Tr}(\tilde A_i)$ | Product trace; $\mathrm{Tr}(e_0^{\otimes n})=2^n$ |
| $\rho_{AB},\rho_{BC},\rho_B$ | Reduced states (partial traces) |
| $S(\rho)=-\mathrm{Tr}(\rho\log\rho)$ | von Neumann entropy |
| $S(\rho_{ABC})+S(\rho_B)\le S(\rho_{AB})+S(\rho_{BC})$ | Strong subadditivity |
| $S(A|B)=S(\rho_{AB})-S(\rho_B)$ | Conditional entropy |
| $I(A:C|B)$ | Conditional mutual information; the deficit |
| $\sigma_{ABC}=\exp(\log\rho_{AB}+\log\rho_{BC}-\log\rho_B)$ | Reference operator ($\mathrm{Tr}\,\sigma_{ABC}\le1$) |
| $\Lambda$ | Completely positive trace-preserving map (e.g. $\mathrm{Tr}_C$) |
| $\rho_{ABC}=\bigoplus_k p_k\,\rho_{Ab_k^L}\otimes\rho_{b_k^R C}$ | Quantum Markov chain (equality case) |

## Further Reading

- E. H. Lieb and M. B. Ruskai, "Proof of the strong subadditivity of quantum-mechanical entropy," *Journal of Mathematical Physics* **14** (1973) 1938–1941, for the theorem.
- E. H. Lieb, "Convex trace functions and the Wigner–Yanase–Dyson conjecture," *Advances in Mathematics* **11** (1973) 267–288, for the convexity results the proof uses.
- H. Araki and E. H. Lieb, "Entropy inequalities," *Communications in Mathematical Physics* **18** (1970) 160–170, for subadditivity, the triangle inequality, and their consequences.
- A. Uhlmann, "Relative entropy and the Wigner–Yanase–Dyson–Lieb concavity in an interpolation theory," *Communications in Mathematical Physics* **54** (1977) 21–32, for the monotonicity of relative entropy under completely positive maps.
- G. Lindblad, "Completely positive maps and entropy inequalities," *Communications in Mathematical Physics* **40** (1975) 147–151, for the same result and its data-processing reading.
- P. Hayden, R. Jozsa, D. Petz, and A. Winter, "Structure of states which satisfy strong subadditivity of quantum entropy with equality," *Communications in Mathematical Physics* **246** (2004) 359–374, for the quantum Markov equality condition.
- M. A. Nielsen and I. L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the finite-dimensional proof and the standard examples.
- M. Ohya and D. Petz, *Quantum Entropy and Its Use* (Springer, 1993), for the convexity and monotonicity theory.
- R. Haag, *Local Quantum Physics: Fields, Particles, Algebras* (Springer, 1996), for the algebraic setting of the region statement.
- H. Casini and M. Huerta, "A finite entanglement entropy and the c-theorem," *Physics Letters B* **600** (2004) 142–150, for the entropic monotonicity in two dimensions.
- Companion article *Relative Entropy and the Biquaternion Framework*, for the relative entropy, Klein's inequality, and the closed form.
- Companion article *The GNS Construction in the Biquaternion Framework*, for the states of $\mathbb{B}$, the Bloch ball, and the trace state.
- Companion article *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*, for the capacity statement: one fermionic mode and no more.
- Companion article *The Biquaternion Vacuum as a Minimal Idempotent*, for the minimal idempotents and the pure boundary.
- Companion article *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, for the Hermitian subspace and the trace pairing.
