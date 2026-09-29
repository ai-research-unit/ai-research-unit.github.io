# __Completely Positive Maps of the Biquaternion Algebra with Hermitian Adjoint__

## Introduction

This is the physics companion of *Completely Positive Maps of the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/completely-positive-maps-of-the-biquaternion-algebra-with-hermitian-adjoint.md`). The mathematics has one theorem: **the completely positive maps of the biquaternion algebra are exactly the sums of at most four two-sided operators**, $\Phi=\sum_{k=1}^{r}\Theta_{\tilde{Q}_{k}}$, $r=\mathrm{rank}\,C_{\Phi}\le4$, by Choi and Kraus. In the physics this is the framework's statement about **channels**: a channel is a sum of **sandwiches**, and a single sandwich is the rank-one channel that prepares the state of an amplitude. The article's business is to read the Kraus theorem physically, to identify the reversible channels with the unitary conjugations, and to explain why the transposition — positive on the cone — is **not** a physical process.

The four physical points are:

1. the sandwich $\Theta_{\tilde{Q}}$ is the map $\tilde R\mapsto \tilde{Q}\tilde R\tilde{Q}^{\dagger}$, i.e. the **amplitude-to-state** map; the Born rule is its diagonal;
2. a general channel is a sum of sandwiches, so **noise is a sum of amplitude preparations**;
3. the **reversible** channels are exactly the sandwiches of unitary elements, i.e. the automorphisms of the framework; every other channel is irreversible even when invertible as a linear map;
4. **positivity of the map on the cone is not enough**: the transposition is positive and not completely positive, and complete positivity is the physical criterion.

## The Sandwich as the Amplitude-to-State Channel

**The physical reading of $\Theta_{\tilde{Q}}$.** The sandwich is the map

$$
\tilde R\longmapsto \tilde{Q}\,\tilde R\,\tilde{Q}^{\dagger},
$$

and it is the framework's **state preparation**: applied to the identity it returns $\tilde{Q}\tilde{Q}^{\dagger}$, the positive element of the amplitude $\tilde{Q}$, and its normalised trace-one version is the state. Its Choi matrix is positive semidefinite of **rank one**: the sandwich is a channel of rank one, and the rank-one channels are the "pure" ones, with no mixture. The positivity of the sandwich on the cone is the statement that **state preparation carries states to states**, and the complete positivity is the statement that it does so also when the channel is applied to one half of an entangled pair — the physical content of the amplification.

**Remark (the Born rule).** The diagonal of $\Theta_{\tilde{Q}}(e_{0})=\tilde{Q}\tilde{Q}^{\dagger}$ is the Hermitian squares of the amplitudes: the Born rule. The off-diagonal entries of the same element are the coherences of *The Spectra of the Operators on the Biquaternion Algebra with Hermitian Adjoint*, and the whole matrix is the density matrix prepared by the amplitude, up to the trace normalisation. The map $\tilde{Q}\mapsto \tilde{Q}\tilde{Q}^{\dagger}$ is precisely the sandwich, and the whole Kraus theory is the statement that a channel is a **convex mixture of such preparations**.

## A Channel is a Sum of Sandwiches

**Proposition (the physical form of the Kraus theorem).** A channel of the framework, i.e. a completely positive trace-preserving map, is

$$
\Phi(\tilde R)=\sum_{k=1}^{r}\tilde{Q}_{k}\,\tilde R\,\tilde{Q}_{k}^{\dagger},\qquad r\le4,
$$

with the **trace preservation** condition $\sum_{k}\tilde{Q}_{k}^{\dagger}\tilde{Q}_{k}=e_{0}$ and the **unitality** condition $\sum_{k}\tilde{Q}_{k}\tilde{Q}_{k}^{\dagger}=e_{0}$. The elements $\tilde{Q}_{k}$ are the framework's **Kraus amplitudes**, and the Choi rank $r$ is the number of independent amplitudes in the mixture.

**Physical reading.** The trace preservation is the statement that the channel preserves the normalisation of a state, i.e. it is a **physical evolution**; unitality is the statement that it preserves the identity, i.e. it does not change the "unpolarised" state, and a channel that is both is a **bistochastic** channel of the framework, preserving the state space as a set. A single amplitude gives a **pure** channel (rank one), two amplitudes give the dephasing-like channels, and the generic channel is a mixture.

**Example (dephasing).** $\Phi=\frac12 \Theta_{e_{0}}+\frac12 \Theta_{ie_{3}}$ is unital and trace preserving, and in the matrix model it is $\Phi(\tilde R)=\frac12(\tilde R+\sigma_{3}\tilde R\sigma_{3})=\mathrm{diag}(\tilde R)$: the **dephasing channel** in the basis of the Hermitian sector $\mathbb{M}_+$, which kills the coherences and keeps the populations. It is the reference channel of *Exercise: Quantum Channels and Dephasing in M+*, and it is exactly the framework's statement that a measurement in the $\mathbb{M}_+$ basis is a channel that is not an automorphism.

## Reversible and Irreversible Channels

**Theorem (the reversible channels are the unitary conjugations).** A channel of a single amplitude, $\Phi=\Theta_{\tilde{Q}}$, is **reversible** — its inverse is again a channel — exactly when $\tilde{Q}\in U$, i.e. exactly when the amplitude is a unitary of the framework. Then the channel is the **conjugation** $\tilde R\mapsto \tilde{Q}\tilde R\tilde{Q}^{\dagger}$, an automorphism of the algebra, and its inverse is $\Theta_{\tilde{Q}^{\dagger}}$. For an invertible amplitude $\tilde{Q}\notin U$ the map is invertible as a linear map but its inverse is **not** a channel: the evolution is irreversible.

**Physical reading.** This is the precise algebraic form of the **reversible/irreversible dichotomy** of *Quantum Channels and the Reversible/Irreversible Dichotomy*: the reversible evolutions are the unitary conjugations, which are exactly the framework's automorphisms (the internal rotations and the symmetric presentations of the Lorentz transformations), and every other channel loses information. The distinction is not "invertible or not" but "the inverse is a physical operation or not"; the mathematics article's criterion $\tilde{Q}\in U$ is the exact dividing line.

**Proof of the theorem.** The mathematics companion: $\Theta_{\tilde{Q}}$ has the inverse $\Theta_{\tilde{Q}^{-1}}$, and $\Theta_{\tilde{Q}^{-1}}$ is a channel (indeed a single-sandwich channel) exactly when $\tilde{Q}^{-1}$ exists in the slice $U$, i.e. exactly when $\tilde{Q}\in U$, since $\Theta_{\tilde{Q}}$ is unital and trace preserving exactly for $\tilde{Q}\in U$.

## Positivity is Not Enough: The Transposition

**Proposition (the transposition is the canonical non-physical map).** The transposition $\Phi(\tilde R)=\tilde R^{T}$ is **positive** — it carries the positive cone into itself — and it is **not completely positive**: its Choi matrix is the flip, with the eigenvalues $(1,1,1,-1)$ and the single negative eigenvalue on the antisymmetric part. Consequently the transposition is not a physical process of the framework.

**Physical reading.** The physical content of complete positivity is that a channel must be **extendable to an entangled partner**: acting on one half of an entangled pair it must still be positive. The transposition passes the test of positivity on a single algebra and fails the test of the amplification; the single negative eigenvalue of the flip is the obstruction. Complete positivity, not positivity, is the framework's criterion for a physical process, and the Choi matrix is the object that decides it. This is the operator-level statement of the framework's insistence that its channels are the **completely** positive ones.

## The Cone of Channels and the State Space

**Proposition (the cone, the state space and the flow).** The completely positive maps form a cone generated by the sandwiches; the channel cone is its unital-plus-trace-preserving subcone; and the state space of the framework — the Bloch ball of the trace-one slice of the positive cone — is the **orbit of the identity under the unital channels**: $\Phi(e_{0})=\sum_{k}\tilde{Q}_{k}\tilde{Q}_{k}^{\dagger}\succeq0$. The trace-preserving channels are the **evolutions** of the state space, and the unital ones are the **symmetries** of the reference state.

**Physical reading.** One sentence contains the article: **the states are the images of the identity under the amplitude sums, the evolutions are the trace-preserving sums, and the symmetries are the unital ones**. The framework's entire channel picture is the statement that these three words mean the same three conditions of the mathematics companion.

## Worked Examples

**The identity channel.** $\Theta_{e_{0}}=\mathrm{id}$: the trivial preparation, unital and trace preserving, reversible, the identity of the composition of channels.

**A pure channel that is not normalised.** $\Theta_{e_{0}+ie_{3}}$: Choi rank one, but $\tilde{Q}\tilde{Q}^{\dagger}=\tilde{Q}^{2}=2\tilde{Q}$ has trace four times the amplitude trace, so the map is neither unital nor trace preserving; it is the framework's example that **a rank-one channel need not be a state channel** — the normalisation is an independent condition, and the null amplitude collapses the cone.

**A mixture.** $\frac12\Theta_{e_{0}}+\frac12\Theta_{e_{3}}$ is unital and trace preserving, hence a channel, with Choi rank two: it is the framework's two-amplitude channel, and its image is a two-dimensional subspace of the state space. Physically it is a **noisy** channel whose Choi rank counts the independent noise amplitudes.

**The transposition composed with a preparation.** The map $\tilde R\mapsto (\tilde{Q}\tilde R\tilde{Q}^{\dagger})^{T}$ is positive and not completely positive; its Choi matrix has the negative eigenvalue of the flip transported by the sandwich, and it is the framework's example that **composing a physical preparation with the transposition gives a non-physical map** — the obstruction lives in the transposition and not in the preparation.

## Summary

The completely positive maps of the biquaternion algebra are the sums of at most four sandwiches, $\Phi=\sum_{k=1}^{r}\Theta_{\tilde{Q}_{k}}$, $r\le4$; physically a channel is a mixture of amplitude preparations, with the Kraus amplitudes $\tilde{Q}_{k}$, and the trace preservation and unitality are $\sum_{k}\tilde{Q}_{k}^{\dagger}\tilde{Q}_{k}=e_{0}$ and $\sum_{k}\tilde{Q}_{k}\tilde{Q}_{k}^{\dagger}=e_{0}$. A single sandwich is the rank-one channel $\tilde R\mapsto \tilde{Q}\tilde R\tilde{Q}^{\dagger}$ preparing the state $\tilde{Q}\tilde{Q}^{\dagger}$, i.e. the Born rule as a map; the reversible channels are exactly the unitary conjugations $\tilde{Q}\in U$, which are the framework's automorphisms, and every other channel is irreversible. The transposition is positive on the cone and not completely positive, with the flip and its single negative eigenvalue, and complete positivity — the positivity of the Choi matrix — is the physical criterion. The state space is the orbit of the identity under the unital channels, the evolutions are the trace-preserving ones, and the symmetries are the automorphisms.

## Summary of Notation

| Symbol | Physical reading |
|---|---|
| $\Theta_{\tilde{Q}}(\tilde R)=\tilde{Q}\tilde R\tilde{Q}^{\dagger}$ | Amplitude-to-state channel; the Born rule as a map |
| $\Phi=\sum_{k=1}^{r}\Theta_{\tilde{Q}_{k}}$ | A channel; $r$ independent Kraus amplitudes; $r\le4$ |
| $C_{\Phi}\succeq0$ | Choi criterion; the physical (CP) condition |
| $\sum_{k}\tilde{Q}_{k}^{\dagger}\tilde{Q}_{k}=e_{0}$ | Trace preservation; the evolution of a normalised state |
| $\sum_{k}\tilde{Q}_{k}\tilde{Q}_{k}^{\dagger}=e_{0}$ | Unitality; the symmetry of the reference state |
| $\tilde{Q}\in U$ | Reversible channel; a unitary conjugation; an automorphism |
| $\Phi(\tilde R)=\tilde R^{T}$ | The transposition; positive, not CP, not physical |
| $\sum_{ij}E_{ij}\otimes E_{ji}$ | The flip; eigenvalues $(1,1,1,-1)$; the obstruction |
| $\Phi(e_{0})=\sum_{k}\tilde{Q}_{k}\tilde{Q}_{k}^{\dagger}$ | The image of the identity; a state of the Bloch ball |

## Further Reading

- *Completely Positive Maps of the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/completely-positive-maps-of-the-biquaternion-algebra-with-hermitian-adjoint.md`), the mathematical companion.
- *Quantum Channels and the Reversible/Irreversible Dichotomy* (`articles_physics/quantum-channels-and-the-reversible-irreversible-dichotomy.md`), for the physical dichotomy whose algebraic form this article gives.
- *Exercise: Quantum Channels and Dephasing in M+* (`articles_physics/exercise-quantum-channels-and-dephasing-in-m.md`), for the dephasing channel and its computations.
- *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* (`articles_physics/the-hermitian-subspace-m-plus-as-the-informational-sector.md`), for the state cone, the Bloch ball and the trace-one slice.
- *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint* (`articles_physics/two-sided-operators-on-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the sandwich as the framework's transformation and its phase blindness.
- *The Spectra of the Operators on the Biquaternion Algebra with Hermitian Adjoint* (`articles_physics/the-spectra-of-the-operators-on-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the populations, the coherences and the contraction of the Bloch ball.
- *The Material/Informational Split as a Superselection Structure in Biquaternionic Form* (`articles_physics/the-material-informational-split-as-a-superselection-structure-in-biquaternionic-form.md`), for the two-sector reading of the channels.
- *Landauer's Principle and the Material–Informational Exchange in Biquaternionic Form* (`articles_physics/landauers-principle-and-the-material-informational-exchange-in-biquaternionic-form.md`), for the information-theoretic side of the irreversible channels.
- *Maxwell's Demon and the Informational Sector in Biquaternionic Form* (`articles_physics/maxwells-demon-and-the-informational-sector-in-biquaternionic-form.md`), for a physical instance of an information-processing channel.
