# __The Spectra of the Operators on the Biquaternion Algebra with Hermitian Adjoint__

## Introduction

This is the physics companion of *The Spectra of the Operators on the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/the-spectra-of-the-operators-on-the-biquaternion-algebra-with-hermitian-adjoint.md`). The spectra are the same four rules; the reading is physical. The four rules are:

- the left multiplication $L_{\tilde A}$ has the spectrum of $\tilde A$, each eigenvalue twice;
- the inner derivation $\mathrm{ad}_{\tilde A}=[\tilde A,\cdot\,]$ has the pairwise differences $\lambda_{i}-\lambda_{j}$: the **charges**;
- the sandwich $\Theta_{\tilde{Q}}$ has the pairwise products $\lambda_{i}\overline{\lambda_{j}}$: the **populations and the coherences**;
- the Sylvester operator $L_{\tilde A}+R_{\tilde B}$ has the pairwise sums $\lambda_{i}+\mu_{j}$: the **energies of the coupled pair**.

The element-level spectral theory of the framework is *Biquaternion Spectral Theory*; this article is the operator-level theory, and the physics is stated in the language of states, amplitudes, populations and coherences. The one sentence that carries the article: **the sandwich of an amplitude is the density matrices it prepares, and its spectrum is the Born rule together with the coherences.**

## The Sandwich as the Preparation of a State

**The Born rule as a spectrum.** Let $\tilde{Q}$ be an amplitude, $\Phi(\tilde{Q})$ its matrix model with eigenvalues $\lambda_{1},\lambda_{2}$. The sandwich $\Theta_{\tilde{Q}}$ has the four eigenvalues

$$
\lvert\lambda_{1}\rvert^{2},\quad \lambda_{1}\overline{\lambda_{2}},\quad \lambda_{2}\overline{\lambda_{1}},\quad \lvert\lambda_{2}\rvert^{2},
$$

which are exactly the matrix elements of the **density matrix of the pure state prepared by $\tilde{Q}$**: the two **populations** $\lvert\lambda_{i}\rvert^{2}$ and the two **coherences** $\lambda_{i}\overline{\lambda_{j}}$. The Born rule is the statement that the populations are the Hermitian squares of the amplitudes; the off-diagonal coherences are the interference terms; and the trace of the sandwich is $\lvert\operatorname{tr}\Phi(\tilde{Q})\rvert^{2}$ while its rank is $(\mathrm{rank}\,\Phi(\tilde{Q}))^{2}$, so a classical (rank-one, singular) amplitude prepares a rank-one state.

**Remark (why the phase does not show in the state).** $\Theta_{\omega\tilde{Q}}=\Theta_{\tilde{Q}}$ for every phase $\omega$; the phase of the amplitude is the standard gauge redundancy of state preparation, and the physics of the framework says it in one line: **the two-sided operator sees the state and not the amplitude**, which is why the sandwich is the physically natural, and the only phase-blind, operator of the pair with the one-sided article.

**Remark (the amplitude is not a state).** The element $\tilde{Q}$ is not Hermitian in general, and the sandwich is not self-adjoint for general $\tilde{Q}$: the spectrum is not real. The physical diagnostic is the one derived in the mathematics article: $\Theta_{\tilde{Q}}$ is self-adjoint exactly when $\tilde{Q}$ is Hermitian up to a central phase, that is, exactly when the amplitude is **parallel to a Hermitian element**; and only then do the four eigenvalues become the real entries of a Hermitian density matrix in the two-level reading.

## The One-Sided Spectrum and the Internal Charges

**The left multiplication as a charge operator.** $L_{\tilde A}$ has the spectrum of $\tilde A$ twice. If $\tilde A$ is the generator of an internal rotation, $\tilde A\in\mathbb{M}_-$, its spectrum is purely imaginary and $L_{\tilde A}$ is skew-adjoint: the spectrum on the imaginary axis is the **list of internal charges** of the module, each charge occurring twice because the algebra as a module is two copies of the standard spinor module, as in *One-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*.

**The inner derivation as the charge differences.** The derivation $\mathrm{ad}_{\tilde A}=L_{\tilde A}-R_{\tilde A}$ has the pairwise differences $\lambda_{i}-\lambda_{j}$: the **differences of the charges** are the weights by which the derivation acts, which is the framework's operator-level version of the **selection rules**. For the internal rotation generators $e_{k}\in\mathbb{M}_-$ the weights are $\pm2i$, the quantised half-angle, and the exponentiated derivation has period $\pi$: the factor two of the half-angle spinor representation appears here as the difference of the eigenvalues.

**Proposition (the charge pairing).** For a Hermitian element $\tilde A$, the derivation $\mathrm{ad}_{\tilde A}$ is self-adjoint with real spectrum; for an anti-Hermitian element it is skew-adjoint with imaginary spectrum. In the physics the two cases are the **observable** (Hermitian generator, self-adjoint, real charges) and the **rotation generator** (anti-Hermitian, skew-adjoint, imaginary exponential). The framework's internal group uses the second and its observables the first, and the two are related by multiplication by $i$.

## The Sandwich as a Positive Semidefinite Operator

**Proposition (the positivity criteria in physical terms).** For $\tilde{Q}$ Hermitian up to a central phase, the sandwich is self-adjoint and its spectrum is real; for $\tilde{Q}$ **positive semidefinite** the sandwich is positive semidefinite; for $\tilde{Q}$ **definite** the sandwich is positive definite. If $\tilde{Q}$ has inertia $(p,q)$, the signature of the sandwich is $(p^{2}+q^{2},2pq)$: a **definite** amplitude gives a definite state and an **indefinite** Hermitian amplitude (inertia $(1,1)$) gives a sandwich with two positive and two negative eigenvalues.

**Remark (a sandwich is never negative).** For any nonzero Hermitian $\tilde{Q}$ the two populations $\lvert\lambda_{i}\rvert^{2}$ are positive, so the sandwich is never negative semidefinite. In the physics this is the statement that **state preparation cannot produce an anti-state**: the positivity of the populations is structural, and the "negative populations" of the indefinite cases come only in pairs with positive ones, which is the signature $(2,2)$ and the reason the framework's signed and graded structures are balanced.

**Remark (the operator norm and the contraction).** The norm of the sandwich is the square of the norm of the amplitude, $\lVert \Theta_{\tilde{Q}}\rVert=\lVert\Phi(\tilde{Q})\rVert^{2}$; a channel of a single amplitude therefore contracts the algebra by the square of its norm and preserves it only for the unitaries. This is the spectral statement behind the **contraction of the Bloch ball** under the noisy channels of the CP-maps article and of *Quantum Channels and the Reversible/Irreversible Dichotomy*.

## The Sylvester Spectrum and the Coupled Energies

**The pairwise sums.** The Sylvester operator $L_{\tilde A}+R_{\tilde B}$ has the spectrum $\{\lambda_{i}+\mu_{j}\}$: in the physics this is the **energy of a pair** whose free energies are the two spectra, and the singularity of the operator — an eigenvalue of $\tilde A$ equal to the negative of an eigenvalue of $\tilde B$ — is the **resonance** of the pair. The framework's double-well and coupled-mode problems are this operator, and the resonance condition is exactly the failure of unique solvability of the mathematics article.

**Proposition (the Hermitian case is the physical one).** For Hermitian $\tilde A,\tilde B$ the spectrum is real and the operator is self-adjoint; for anti-Hermitian parameters it is skew-adjoint with imaginary spectrum. The physical reading: the Sylvester operator of Hermitian parameters is an **observable** (the anticommutator, the energy), while the Sylvester operator of anti-Hermitian parameters is a **rotation generator** (the commutator, the derivation). The framework's Heisenberg-type equations use the first, its internal rotations the second.

## Worked Examples

**A two-level amplitude.** $\tilde{Q}=e_{0}+e_{1}$ has the matrix $I-i\sigma_{1}$ with eigenvalues $\{1+i,1-i\}$, so the sandwich has the spectrum $\{2,2i,-2i,2\}$: not real, because the amplitude is not Hermitian up to phase, and the imaginary pair is the coherence. The example is the framework's warning that **a real-looking amplitude need not prepare a real state**.

**A pure state.** $\tilde{Q}=e_{0}+ie_{3}$ is Hermitian with eigenvalues $\{2,0\}$: the sandwich has the spectrum $\{4,0,0,0\}$, positive semidefinite of rank one, and it is **not** normalised: it is a pure direction blown up by the trace. The normalised state is the trace-one multiple, and the null eigenvalue is the lightlike direction lost by the preparation.

**An internal rotation.** For $\tilde A=e_{3}\in\mathbb{M}_-$, $L_{e_{3}}$ has the spectrum $\{i,-i,i,-i\}$ (purely imaginary, the charges) and $\mathrm{ad}_{e_{3}}$ has the spectrum $\{0,2i,-2i,0\}$ (the weights on the off-diagonal entries, the selection rules of the internal rotation). The exponentials are the rotations of *The Reflection and the Rotation in Biquaternionic Form*, of period $\pi$.

**The identity.** $L_{e_{0}}=\mathrm{id}$ has the spectrum $\{1,1,1,1\}$ and $\mathrm{ad}_{e_{0}}=0$: the identity has no charges and generates no internal rotation.

## Summary

The spectra of the operators of the framework have direct physical content: the sandwich $\Theta_{\tilde{Q}}$ has the spectrum of the density matrix prepared by the amplitude $\tilde{Q}$, with the populations $\lvert\lambda_{i}\rvert^{2}$ and the coherences $\lambda_{i}\overline{\lambda_{j}}$, and it is phase-blind, so the phase of the amplitude is a gauge redundancy; the left multiplication has the spectrum of the element twice, the internal charges of the two copies of the spinor module; the inner derivation has the differences of the charges, i.e. the selection rules and the half-angle factor of the internal rotations; the Sylvester operator has the sums, i.e. the energies and the resonances of a coupled pair. The sandwich is self-adjoint exactly for the amplitudes Hermitian up to phase and positive semidefinite exactly for the positive semidefinite ones; it is never negative, its norm is the square of the norm of the amplitude, and it is trace preserving exactly for the unitaries. All statements are proved and verified in the mathematics companion.

## Summary of Notation

| Symbol | Physical reading |
|---|---|
| $\Theta_{\tilde{Q}}$ | The state prepared by the amplitude $\tilde{Q}$; populations and coherences |
| $\lvert\lambda_{i}\rvert^{2}$ | Born rule; the populations |
| $\lambda_{i}\overline{\lambda_{j}}$ | The coherences; the interference terms |
| $L_{\tilde A}$ | Charge operator; the spectrum of $\tilde A$ twice |
| $\mathrm{ad}_{\tilde A}=L_{\tilde A}-R_{\tilde A}$ | Selection rules; the differences of the charges |
| $L_{\tilde A}+R_{\tilde B}$ | Coupled energies; the sums of the spectra; the resonance |
| $\tilde{Q}^{\dagger}=\omega\tilde{Q}$ | Hermitian up to phase; the self-adjoint case |
| $\lVert \Theta_{\tilde{Q}}\rVert=\lVert\Phi(\tilde{Q})\rVert^{2}$ | Contraction of the Bloch ball by the amplitude norm |
| $\tilde{Q}\in U$ | Unitary; the trace-preserving and reversible case |

## Further Reading

- *The Spectra of the Operators on the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/the-spectra-of-the-operators-on-the-biquaternion-algebra-with-hermitian-adjoint.md`), the mathematical companion.
- *Biquaternion Spectral Theory* (`articles_physics/biquaternion-spectral-theory.md`), for the element spectra that enter here.
- *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* (`articles_physics/the-hermitian-subspace-m-plus-as-the-informational-sector.md`), for the Bloch ball, the states and the trace-one slice.
- *The Spinor Module in Biquaternionic Form and Its Lorentz Action* (`articles_physics/the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.md`), for the two copies of the spinor module behind the doubled one-sided spectrum.
- *Angular Momentum and Spin in Biquaternionic Form* (`articles_physics/angular-momentum-and-spin-in-biquaternionic-form.md`), for the internal generators and their half-angle.
- *Quantum Channels and the Reversible/Irreversible Dichotomy* (`articles_physics/quantum-channels-and-the-reversible-irreversible-dichotomy.md`), for the contraction of the Bloch ball and the channels.
- *Biquaternion Spin Geometry* (`articles_physics/biquaternion-spin-geometry.md`), for the spinor operators and their spectra.
- *The Reflection and the Rotation in Biquaternionic Form* (`articles_physics/the-reflection-and-the-rotation-in-biquaternionic-form.md`), for the exponentials of the internal generators.
- *Biquaternion Rotations and Lorentz Transformations* (`articles_physics/biquaternion-rotations-and-lorentz-transformations.md`), for the geometry of the generators.
