# __Biorthogonal Quantum Mechanics and the Biquaternion Spectrum__

## Introduction

A non-normal element still has a spectral decomposition. What it loses is the orthogonality of the two pieces. The eigenvalues stay distinct, the two idempotents stay complete and orthogonal as idempotents, but the idempotents are no longer Hermitian, and the two eigendirections are no longer orthogonal in the Hilbert space of the algebra.

The standard language for this situation is **biorthogonal quantum mechanics**. The right eigenvectors of the element and the left eigenvectors of the same element form two bases that are dual to each other, not two orthonormal bases. The spectral projectors are built from one right vector and one left vector, and the probability rule uses the left pairing. When the element is normal, the two bases coincide, the projectors become Hermitian, and the rule reduces to the Born rule.

This article reads that structure in the biquaternion algebra. The spectral decomposition and the normality criterion are those of *Eigenvalue Decomposition of a Biquaternion*. The left and right eigenvalue problem is that of *Biquaternion Spectral Theory*. The article owns the reading and its limits; it proves no spectral theorem.

**Placement.** The article belongs to the informational block of the non-relativistic quantum theory, after *Exceptional Points and the Nilpotent Regime in the Biquaternion Spectrum* and before *Quantum Channels and the Reversible/Irreversible Dichotomy*. It uses the matrix model $\mathsf M_2$ and the eigenprojections of the eigenvalue decomposition.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_t,\vec e_x,\vec e_y,\vec e_z$, central imaginary $i$, and $\tilde Q=Q_te_t+\vec Q$ with $Q_\mu\in\mathbb{C}$. The star is Hermitian conjugation, $\tilde Q^{*}=\overline{Q_t}e_t-\overline{\vec Q}$, and $\operatorname{Sc}$ is the scalar part, so that $\operatorname{Tr}\tilde X=2\operatorname{Sc}\tilde X$. The matrix model is $\mathsf M_2(e_t)=I_2$, $\mathsf M_2(\vec e_k)=-i\sigma_k$, with $\mathsf M_2(\tilde Q^{*})=\mathsf M_2(\tilde Q)^{\dagger}$ and $\det\mathsf M_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}$. The eigenvalues are complex and central, so the left and right **eigenvalue** problems coincide; the biorthogonal structure below is a statement about left and right **eigenvectors**, not about a non-commutative spectrum.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The spectrum, the eigenprojections and the two-term writing | [Eigenvalue Decomposition of a Biquaternion](../articles_maths/eigenvalue-decomposition-of-a-biquaternion.html) |
| The normality criterion and the Hermitian case | [Eigenvalue Decomposition of a Biquaternion](../articles_maths/eigenvalue-decomposition-of-a-biquaternion.html) |
| Left and right eigenvalues, and the central-spectrum convention | [Biquaternion Spectral Theory](../articles_maths/biquaternion-spectral-theory.html) |
| The spectral theorem for a normal element | [Biquaternion Spectral Theory](../articles_maths/biquaternion-spectral-theory.html) |
| The matrix model and the determinant | [The Element and Operator Representations](the-element-and-operator-representations.html) |
| The Jordan and nilpotent regimes | [Eigenvalue Decomposition of a Biquaternion](../articles_maths/eigenvalue-decomposition-of-a-biquaternion.html) |

## The Two Eigenbases

Let $A=\mathsf M_2(\tilde Q)$ and let $B\neq0$, so that $A$ has distinct eigenvalues $\lambda_\pm=Q_t\pm iB$. A **right eigenvector** $r_\sigma\in\mathbb{C}^2$ and a **left eigenvector** $\ell_\sigma\in\mathbb{C}^2$ satisfy

$$
Ar_\sigma=\lambda_\sigma r_\sigma,
\qquad
\ell_\sigma^{\dagger}A=\lambda_\sigma\ell_\sigma^{\dagger},
\qquad
\sigma\in\{+,-\}.
$$

The two bases are dual, not orthonormal:

$$
\ell_\sigma^{\dagger}r_\tau=\delta_{\sigma\tau},
$$

after the normalization $\ell_\sigma^{\dagger}r_\sigma=1$. The spectral projectors are

$$
P_\sigma=r_\sigma\ell_\sigma^{\dagger},
\qquad
P_\sigma P_\tau=\delta_{\sigma\tau}P_\sigma,
\qquad
P_++P_-=I_2,
\qquad
A=\lambda_+P_++\lambda_-P_-.
$$

These are the Riesz projectors of $A$, and they are exactly the matrix images of the biquaternion eigenprojections:

$$
P_\pm=\mathsf M_2(\tilde\Pi_\pm),
\qquad
\tilde\Pi_\pm=\frac12\left(e_t\pm\vec\Xi\right),
\qquad
\vec\Xi=-\frac{i\vec Q}{B}.
$$

The biquaternion relations $\tilde\Pi_\sigma\tilde\Pi_\tau=\delta_{\sigma\tau}\tilde\Pi_\sigma$ and $\tilde\Pi_++\tilde\Pi_-=e_t$ are the same statement as the biorthogonality and the completeness of the two eigenbases. The translation is exact because the matrix model is an isomorphism.

| Biorthogonal object | Matrix form | Biquaternion form |
| --- | --- | --- |
| right eigenvector | column of $P_\sigma$ | a nonzero column of $\mathsf M_2(\tilde\Pi_\sigma)$ |
| left eigenvector | row of $P_\sigma$ | a nonzero row of $\mathsf M_2(\tilde\Pi_\sigma)$ |
| pairing | $\ell_\sigma^{\dagger}r_\tau=\delta_{\sigma\tau}$ | $P_\sigma P_\tau=\delta_{\sigma\tau}P_\sigma$ |
| completeness | $P_++P_-=I_2$ | $\tilde\Pi_++\tilde\Pi_-=e_t$ |
| spectral writing | $A=\sum_\sigma\lambda_\sigma P_\sigma$ | $\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-$ |
| dual family | $P_\sigma^{\dagger}$ | $\tilde\Pi_\sigma^{*}$ |

The last row is the whole difference from the Hermitian case. When $P_\sigma=P_\sigma^{\dagger}$ the dual family is the family itself and the two bases coincide. When it is not, the dual family is a second, different family.

## The Non-Orthogonality

The two eigendirections are orthogonal as idempotents, because $P_+P_-=0$. They are not orthogonal in the Hilbert space, because the Hermitian inner product of the two projectors is

$$
\operatorname{tr}\left(P_+^{\dagger}P_-\right)\neq0
$$

in general. In the biquaternion this number is $2\operatorname{Sc}\left(\tilde\Pi_+^{*}\tilde\Pi_-\right)$, and it vanishes exactly when the two idempotents are Hermitian, that is, when $\tilde Q$ is normal.

The size of the non-orthogonality is measured by the **Petermann factor** of each projector,

$$
\kappa_\sigma=\operatorname{tr}\left(P_\sigma^{\dagger}P_\sigma\right)
=2\operatorname{Sc}\left(\tilde\Pi_\sigma^{*}\tilde\Pi_\sigma\right).
$$

For a rank-one projector $P=r\ell^{\dagger}/(\ell^{\dagger}r)$,

$$
\kappa=\frac{(r^{\dagger}r)(\ell^{\dagger}\ell)}{\lvert\ell^{\dagger}r\rvert^{2}}\ge1,
$$

by the Cauchy–Schwarz inequality, with equality exactly when $r$ and $\ell$ are proportional. The factor is therefore one precisely in the normal case, and it grows as the two bases turn away from each other. It is the standard measure of the excess of a non-normal mode over an orthogonal one.

| Quantity | Normal element | Non-normal element |
| --- | --- | --- |
| eigenbases | $r_\sigma\propto\ell_\sigma$ | two distinct dual bases |
| projectors | $P_\sigma=P_\sigma^{\dagger}$ | $P_\sigma\neq P_\sigma^{\dagger}$ |
| cross inner product $\operatorname{tr}(P_+^{\dagger}P_-)$ | $0$ | nonzero in general |
| Petermann factor $\kappa_\sigma$ | $1$ | $>1$ |
| spectral theorem | orthogonal | biorthogonal |
| Born rule | available | replaced by the biorthogonal rule |

## The Biorthogonal Probability Rule

The spectral writing gives the decomposition of a vector, but not yet a probability. For a vector $\psi\in\mathbb{C}^2$, expand it in the right basis,

$$
\psi=\sum_\sigma c_\sigma r_\sigma,
\qquad
c_\sigma=\ell_\sigma^{\dagger}\psi.
$$

The coefficient is the left pairing, not the orthogonal projection. The norm is computed with the metric built from the left basis,

$$
\eta=\sum_\sigma\ell_\sigma\ell_\sigma^{\dagger},
\qquad
\langle\psi,\eta\psi\rangle=\sum_\sigma\lvert c_\sigma\rvert^{2},
$$

and the normalized weights are

$$
p_\sigma=\frac{\lvert c_\sigma\rvert^{2}}{\sum_\tau\lvert c_\tau\rvert^{2}}
=\frac{\lvert\ell_\sigma^{\dagger}\psi\rvert^{2}}{\langle\psi,\eta\psi\rangle}.
$$

The weights are positive and sum to one for every $\psi$, because $\eta$ is a sum of rank-one positive operators and the left eigenvectors form a basis. The rule is therefore available for every diagonalizable element with distinct eigenvalues, normal or not. What it is not is the Born rule: the denominator is not one in the original Hilbert norm, and the coefficients are not the orthogonal projections.

The rule has a price. The metric $\eta$ depends on the element, because the left eigenvectors do. Two different observables therefore define two different inner products on the same vector space, and a state has no element-independent norm. That is the sense in which the biorthogonal formulation is a formulation per observable, not a replacement for the Hilbert-space formulation.

## The Density Matrix as the Contrast Class

A density matrix is the case in which the whole apparatus collapses. A state $\tilde\varrho$ is Hermitian, positive and of trace one; it is normal, its eigenprojections are Hermitian, and its eigenbasis is orthonormal. In the matrix model $\eta=I$, the coefficients are the ordinary projections, and the rule becomes the Born rule,

$$
p_\sigma=\operatorname{tr}\left(\varrho P_\sigma\right)
=2\operatorname{Sc}\left(\tilde\varrho\tilde\Pi_\sigma\right),
\qquad
\tilde\Pi_\sigma=\tilde\Pi_\sigma^{*}.
$$

The contrast is the conceptual content of the article. The spectral decomposition alone does not give a probability; **normality** gives it. The density matrix is normal by construction, so the Born rule is the orthogonal case of the biorthogonal rule. A non-normal element is not a state: it is an operator, an effective Hamiltonian or a generator, and its biorthogonal weights are a reading of its modes, not the probabilities of a measurement of that element.

| Case | Element | Metric | Weights |
| --- | --- | --- | --- |
| quantum state | $\tilde\varrho$ Hermitian, positive, trace one | $\eta=I$ | $p_\sigma=2\operatorname{Sc}(\tilde\varrho\tilde\Pi_\sigma)$ |
| normal observable | $\tilde H$ normal, distinct spectrum | $\eta=I$ on the eigenbasis | $p_\sigma=\lvert c_\sigma\rvert^{2}$ |
| non-normal operator | $\tilde Q$ with $B\neq0$ | $\eta=\sum_\sigma\ell_\sigma\ell_\sigma^{\dagger}$ | $p_\sigma=\lvert c_\sigma\rvert^{2}/\langle\psi,\eta\psi\rangle$ |
| exceptional point | $B=0$, $\vec Q\neq0$ | no eigenbasis | no rule |

The last row is the boundary of the whole construction. At an exceptional point the two right eigenvectors coalesce, the left eigenvectors coalesce, and the metric degenerates; the biorthogonal rule has no limit. The exceptional point is treated in *Exceptional Points and the Nilpotent Regime in the Biquaternion Spectrum*, and the two articles meet exactly at that row.

## Physical Readings

- **The right modes are the physical modes and the left modes are their duals.** In an open system with an effective non-Hermitian Hamiltonian, the right eigenvectors are the mode shapes that decay or grow, and the left eigenvectors are the duals that extract the amplitude. The reading is the standard one of non-Hermitian photonics and of resonance theory.
- **The Petermann factor is excess noise.** A mode with $\kappa>1$ has more spontaneous emission than an orthogonal mode of the same linewidth. The reading is the standard Petermann excess-noise factor of a laser mode, and $\kappa=1$ is the orthogonal limit.
- **The metric is an element-dependent inner product.** The biorthogonal rule says that the probability of a mode is measured with the dual basis. The reading is that the inner product is tied to the observable, not fixed once for the whole theory.
- **The density matrix is the contrast class.** The ordinary quantum state is Hermitian, so its spectral decomposition is orthogonal and its Born rule is the orthogonal case. The reading is that the non-Hermitian apparatus is an extension of the operator side, not a replacement of the state side.
- **The exceptional point is the degenerate limit.** As $B\to0$ the two right vectors and the two left vectors coalesce, the Petermann factor diverges, and the probability rule loses its basis. The reading is the standard divergence of the Petermann factor at an exceptional point.

## Limits

The biquaternion supplies the spectral decomposition and the projectors; it does not supply the metric. The choice $\eta=\sum_\sigma\ell_\sigma\ell_\sigma^{\dagger}$ is the standard one, but it is a choice, and a different physical normalization gives a different metric. The article states the standard choice and does not claim uniqueness.

The eigenvalues are central, so the left and right **eigenvalue** problems coincide. The biorthogonal structure is a statement about eigenvectors. The non-commutative left/right eigenvalue problem of *Biquaternion Spectral Theory* is a different subject, and it is not used here.

A conserved probability needs a real spectrum. With complex eigenvalues the $\eta$-norm of an evolving state grows or decays, and the weights $p_\sigma$ are not conserved. The biorthogonal rule gives positive weights at one instant, not a conserved distribution in time. The dynamics of a non-Hermitian element is outside this article.

The Born rule is not derived. The article shows that it is the normal case of a biorthogonal rule; it does not derive the rule from the algebra, and it does not claim that a non-normal element is observable. The measurement postulate remains where *The Measurement Problem in Algebraic Form* leaves it.

No dynamics, no arrow of time and no preferred metric are supplied. The article is a spectral reading of a non-normal element, not a quantum theory of open systems.

## Summary

- For $B\neq0$ a biquaternion has distinct eigenvalues $\lambda_\pm=Q_t\pm iB$ and a spectral decomposition with idempotents $\tilde\Pi_\pm$.
- The idempotents need not be Hermitian; the right and left eigenvectors then form two dual bases, and the projectors are $P_\sigma=r_\sigma\ell_\sigma^{\dagger}$.
- The biquaternion relations $\tilde\Pi_\sigma\tilde\Pi_\tau=\delta_{\sigma\tau}\tilde\Pi_\sigma$ and $\tilde\Pi_++\tilde\Pi_-=e_t$ are the biorthogonality and completeness of the two bases.
- The two eigendirections are orthogonal as idempotents and non-orthogonal in the Hilbert space; the cross inner product $2\operatorname{Sc}(\tilde\Pi_+^{*}\tilde\Pi_-)$ measures the failure.
- The Petermann factor $\kappa_\sigma=2\operatorname{Sc}(\tilde\Pi_\sigma^{*}\tilde\Pi_\sigma)$ is at least one and equals one exactly when the element is normal.
- The biorthogonal probability rule is $p_\sigma=\lvert\ell_\sigma^{\dagger}\psi\rvert^{2}/\langle\psi,\eta\psi\rangle$ with $\eta=\sum_\sigma\ell_\sigma\ell_\sigma^{\dagger}$; it is not the Born rule unless $\eta=I$.
- A density matrix is normal, so its eigenprojections are Hermitian and the biorthogonal rule reduces to the Born rule $p_\sigma=2\operatorname{Sc}(\tilde\varrho\tilde\Pi_\sigma)$.
- At an exceptional point the two bases coalesce and the metric degenerates; the probability rule has no limit there.
- The algebra supplies the decomposition and the projectors, not the metric, the dynamics or the arrow of time.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde Q=Q_te_t+\vec Q$ | a general biquaternion, $Q_t\in\mathbb{C}$, $\vec Q\in\mathbb{C}^3$ |
| $B^2=(\vec Q,\vec Q)$ | the complex norm squared of the vector part |
| $\lambda_\pm=Q_t\pm iB$ | the two eigenvalues |
| $\tilde\Pi_\pm=\tfrac12(e_t\pm\vec\Xi)$ | the eigenprojections, $\vec\Xi=-i\vec Q/B$ |
| $A=\mathsf M_2(\tilde Q)$ | the $2\times2$ matrix image |
| $r_\sigma$, $\ell_\sigma$ | right and left eigenvectors, $\ell_\sigma^{\dagger}r_\tau=\delta_{\sigma\tau}$ |
| $P_\sigma=r_\sigma\ell_\sigma^{\dagger}$ | the spectral projector, $\mathsf M_2(\tilde\Pi_\sigma)$ |
| $\kappa_\sigma$ | the Petermann factor $\operatorname{tr}(P_\sigma^{\dagger}P_\sigma)$ |
| $\eta=\sum_\sigma\ell_\sigma\ell_\sigma^{\dagger}$ | the metric of the biorthogonal basis |
| $\tilde\varrho$ | a density matrix, Hermitian, positive, trace one |

## Further Reading

- [Eigenvalue Decomposition of a Biquaternion](../articles_maths/eigenvalue-decomposition-of-a-biquaternion.html), for the spectrum, the eigenprojections and the normality criterion.
- [Biquaternion Spectral Theory](../articles_maths/biquaternion-spectral-theory.html), for the left and right eigenvalue problems and the spectral theorem.
- [The Element and Operator Representations](the-element-and-operator-representations.html), for the matrix model used throughout.
- [Exceptional Points and the Nilpotent Regime in the Biquaternion Spectrum](exceptional-points-and-the-nilpotent-regime-in-the-biquaternion-spectrum.html), for the degenerate limit of the two bases.
- [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html), for the Hermitian state space and the Born rule.
- [The Measurement Problem in Algebraic Form](the-measurement-problem-in-algebraic-form.html), for the measurement postulate that this article does not derive.
- [Quantum Channels and the Reversible/Irreversible Dichotomy](quantum-channels-and-the-reversible-irreversible-dichotomy.html), for the dynamics that a non-normal generator would have to supply.
