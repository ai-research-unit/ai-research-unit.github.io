# __The Modular Hamiltonian and the First Law of Entanglement in Biquaternionic Form__

## Introduction

The **modular Hamiltonian** of a state is the negative logarithm of its modular operator, $K=-\log\Delta$; in finite dimension, where the state is a density matrix, it is $K=-\log\rho$. It is the generator of the modular flow of the preceding article, and in the entanglement literature it is called the **entanglement Hamiltonian**, because for a reduced state it is the operator whose correlations reproduce the entanglement of the region. The **first law of entanglement** is the statement that a small perturbation of a state changes its entropy and its modular energy by equal amounts:
$$
\delta S=\delta\langle K_0\rangle
$$
to first order in the perturbation, where $K_0$ is the modular Hamiltonian of the reference state. It is the entanglement analogue of the first law of thermodynamics, and it is the relation from which the linearized Einstein equations, the first law of black-hole mechanics, and the entanglement-equilibrium programme are derived.

This article asks what the modular Hamiltonian and the first law of entanglement are in the biquaternion framework. The answer is exact, and the exactness is the framework's contribution.

1. **The modular Hamiltonian is a closed-form element of the informational sector.** For a faithful biquaternion state, $K_0=-\log\tilde\rho_0=\tfrac12\log\frac{4}{1-r_0^2}e_0-i\,b\gamma_0$ with $b=\mathrm{artanh}(r_0)$ and $\gamma_0=\hat{\mathbf r}_0\cdot\mathbf e$, so $K_0\in\mathbb{M}_+$. Its expectation in any state is a closed-form real number, computed below.

2. **The first law is the vanishing of a relative entropy to first order, and the framework writes it exactly.** For any two faithful biquaternion states,
$$
\delta S=\delta\langle K_0\rangle-S(\tilde\rho\|\tilde\rho_0),
$$
where $\delta S=S(\tilde\rho)-S(\tilde\rho_0)$ and $\delta\langle K_0\rangle=\mathrm{Tr}((\tilde\rho-\tilde\rho_0)K_0)$. The deficit is exactly the relative entropy, which is quadratic in the perturbation and non-negative. The first law $\delta S=\delta\langle K_0\rangle$ is therefore exact to first order, and the framework's closed-form relative entropy makes the correction term explicit at every order.

3. **The relation is verified on a perturbation.** Taking the reference state $\mathbf r_0=(0.3,-0.2,0.4)$ and the displacement $\mathbf v=(0.12,0.18,-0.07)$, at $s=0.05$ the two sides of the law differ by the relative entropy $-7.314\times10^{-5}$, and at $s=0.3$ by $-2.619\times10^{-3}$; the identity $\delta S-\delta\langle K_0\rangle=-S(\tilde\rho\|\tilde\rho_0)$ holds to machine precision at both steps, the discrepancy being below $2\times10^{-15}$.

The article proceeds as follows. The modular Hamiltonian is defined and its biquaternion closed form is given. The first law is stated, and the exact identity from which it follows is derived. The identity is verified on the explicit perturbation. The linearity that makes the law exact to first order is explained in the framework's terms, and the entanglement Hamiltonian of a subsystem is discussed. The standard applications are recalled, and the article closes with the established/interpretation/open split.

**Conventions.** Those of the companion articles. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with quaternion basis $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, scalar imaginary $i$, and isomorphism $\Phi(e_k)=-i\sigma_k$, $\Phi(i)=iI_2$, so that $\mathbb{B}\cong M_2(\mathbb{C})$. The material (anti-Hermitian) subspace is $\mathbb{M}_-$ and the informational (Hermitian) subspace is $\mathbb{M}_+$, with $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ and $i\mathbb{M}_\pm=\mathbb{M}_\mp$. The trace is $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$, with $\mathrm{Tr}(e_0)=2$. States are $\tilde\rho=\tfrac12(e_0+i\mathbf r\cdot\mathbf e)\in\mathbb{M}_+$ with $|\mathbf r|\le1$; the logarithms, entropies and relative entropies are the closed forms of *Relative Entropy and the Biquaternion Framework*, and the modular operator, flow and generator are those of *The Modular Theory of Tomita–Takesaki under the Biquaternion Framework* and *Thermal Time and the Modular Flow in the Biquaternion Framework*.

## The Modular Hamiltonian

### Definition

Let $\sigma$ be a faithful state of a von Neumann algebra $M$, with modular operator $\Delta_\sigma$. The **modular Hamiltonian** is
$$
K_\sigma=-\log\Delta_\sigma,
$$
a self-adjoint (generally unbounded) operator affiliated with $M$, so that the modular flow of the preceding article is formally $\sigma_t(\tilde A)=e^{-itK_\sigma}\tilde A e^{itK_\sigma}$. In finite dimension, with $\Delta_\sigma$ acting as $\sigma\,\cdot\,\sigma^{-1}$ and $\sigma$ a density matrix,
$$
K_\sigma=-\log\sigma,
$$
a Hermitian element of the algebra, so that $\sigma=e^{-K_\sigma}$ and $\mathrm{Tr}(e^{-K_\sigma})=1$. Three properties are used below.

- **It is the state's logarithm.** $\sigma$ and $K_\sigma$ carry the same information; the entropy is $S(\sigma)=\mathrm{Tr}(\sigma K_\sigma)=\langle K_\sigma\rangle_\sigma$, the state's modular energy.
- **It is defined by the state.** Different states have different modular Hamiltonians, and the difference of two modular Hamiltonians is the logarithm of the relative modular operator of the relative-entropy companion article.
- **It generates the modular flow.** The commutation relation $\frac{d}{dt}\sigma_t(\tilde A)|_{t=0}=-i[K_\sigma,\tilde A]$ of the thermal-time companion article makes $K_\sigma$ the generator of the state's own time.

### The Modular Hamiltonian of a Biquaternion State

Let $\tilde\rho_0=\tfrac12(e_0+i\mathbf r_0\cdot\mathbf e)$ be faithful, with $r_0=|\mathbf r_0|<1$, $\hat{\mathbf r}_0=\mathbf r_0/r_0$, $\gamma_0=\hat{\mathbf r}_0\cdot\mathbf e$, and $b=\mathrm{artanh}(r_0)$. The biquaternion logarithm of the relative-entropy companion article gives immediately
$$
K_0=-\log\tilde\rho_0
=\tfrac12\log\frac{4}{1-r_0^2}\,e_0-i\,b\,\gamma_0
\ \in\ \mathbb{M}_+ .
$$
Each term is Hermitian — the scalar part is real, and the vector part $-i\,b\,\gamma_0$ has $(-i\,b\,\gamma_0)^\dagger=i\,b\,\gamma_0^\dagger=i\,b\,(-\gamma_0)=-i\,b\,\gamma_0$, using $\gamma_0^\dagger=-\gamma_0$ — so the modular Hamiltonian lies in the informational sector, as the KMS and thermal-time companion articles require. It is the difference of a purely informational scalar term and an element of $i\mathbb{M}_-$.

The expectation of $K_0$ in an arbitrary state $\tilde\rho=\tfrac12(e_0+i\mathbf r\cdot\mathbf e)$ is the biquaternion trace of a product. With $\cos\gamma=\hat{\mathbf r}\cdot\hat{\mathbf r}_0$,
$$
\langle K_0\rangle_{\tilde\rho}
=\mathrm{Tr}\big(\tilde\rho\,K_0\big)
=-\tfrac12\log\frac{1-r_0^2}{4}
-r\,\mathrm{artanh}(r_0)\cos\gamma ,
$$
which is identically real, as every trace is. At $\tilde\rho=\tilde\rho_0$ it reduces to
$$
S(\tilde\rho_0)=\langle K_0\rangle_{\tilde\rho_0}
=-\tfrac12\log\frac{1-r_0^2}{4}
-r_0\,\mathrm{artanh}(r_0),
$$
which is the entropy of the state, as the first property requires. The derivation is the product formula of the biquaternion algebra: the scalar part of $(\tfrac12e_0+i\tfrac{\mathbf r}{2}\cdot\mathbf e)(c_0e_0+i\mathbf c\cdot\mathbf e)$ is $\tfrac12c_0-\mathbf A\cdot\mathbf C$ with $\mathbf A=i\tfrac{\mathbf r}{2}$, $\mathbf C=i\mathbf c$, and $\mathbf A\cdot\mathbf C=-\tfrac12\mathbf r\cdot\mathbf c$, which gives the two terms above.

Note that $\langle K_0\rangle_{\tilde\rho}$ is **linear** in the state $\tilde\rho$: it is $\mathrm{Tr}(\tilde\rho K_0)$, the trace pairing of $\tilde\rho$ with the fixed element $K_0$. This linearity is the algebraic reason the first law is exact to first order, and it is stated again below.

## The First Law of Entanglement

### Statement

Let $\sigma$ be a reference state with modular Hamiltonian $K_\sigma=-\log\sigma$, and let $\rho$ be a state in a neighbourhood of $\sigma$, with $\delta\rho=\rho-\sigma$ of trace zero. Define
$$
\delta S=S(\rho)-S(\sigma),\qquad
\delta\langle K_\sigma\rangle
=\mathrm{Tr}\big(\rho K_\sigma\big)-\mathrm{Tr}\big(\sigma K_\sigma\big)
=\mathrm{Tr}\big(\delta\rho\,K_\sigma\big).
$$
The **first law of entanglement** is the statement
$$
\delta S=\delta\langle K_\sigma\rangle+O\big(\delta\rho^2\big),
$$
that is, to first order in the perturbation the entropy change equals the change in the expectation of the modular Hamiltonian of the reference state. It holds for every state and every perturbation, in every dimension; it is the entanglement analogue of the first law of thermodynamics, with the modular Hamiltonian playing the role of the energy conjugate to the entropy.

### The Exact Identity

The assertion is the first-order shadow of an identity that is exact and, in the framework, closed-form. For two faithful states $\rho$ and $\sigma$,
$$
S(\rho\|\sigma)
=\mathrm{Tr}\big(\rho\log\rho\big)-\mathrm{Tr}\big(\rho\log\sigma\big)
=-S(\rho)+\mathrm{Tr}\big(\rho K_\sigma\big),
$$
using $\log\sigma=-K_\sigma$ and $S(\rho)=-\mathrm{Tr}(\rho\log\rho)$. Subtracting the same quantity in the reference state, $S(\sigma)=\mathrm{Tr}(\sigma K_\sigma)$, gives
$$
S(\rho\|\sigma)
=-\big[S(\rho)-S(\sigma)\big]+\mathrm{Tr}\big((\rho-\sigma)K_\sigma\big),
$$
and therefore
$$
\boxed{\ \delta S=\delta\langle K_\sigma\rangle-S(\rho\|\sigma)\ }
$$
for all faithful $\rho,\sigma$. Since $S(\rho\|\sigma)\ge0$ with equality if and only if $\rho=\sigma$, the exact identity gives
$$
\delta S\ \le\ \delta\langle K_\sigma\rangle,
$$
with equality exactly at the reference state. The first law is the statement that the relative entropy — the gap — has no linear term, so the inequality is saturated to first order.

The proof is two lines and uses only that $K_\sigma=-\log\sigma$ and that $S(\rho\|\sigma)=\mathrm{Tr}(\rho\log\rho)-\mathrm{Tr}(\rho\log\sigma)$. In the biquaternion framework every quantity in it is computable in closed form: $\delta S$ from the entropy formula, $\delta\langle K_\sigma\rangle$ from the expectation above, and $S(\tilde\rho\|\tilde\rho_0)$ from the boxed relative-entropy formula of the companion article.

### Verification on a Perturbation

Take the reference state
$$
\mathbf r_0=\big(0.3,-0.2,0.4\big),
\qquad
r_0=0.538516,
$$
and displace it along $\mathbf v=(0.12,0.18,-0.07)$, so that $\mathbf r_s=\mathbf r_0+s\mathbf v$. Two values of $s$ were checked; all quantities are in nats.

| $s$ | $\delta S$ | $\delta\langle K_0\rangle$ | $\delta S-\delta\langle K_0\rangle$ | $-S(\tilde\rho_s\|\tilde\rho_0)$ |
|---|---|---|---|---|
| $0.05$ | $0.0014920634$ | $0.0015652061$ | $-0.0000731427$ | $-0.0000731427$ |
| $0.30$ | $0.0067718504$ | $0.0093912368$ | $-0.0026193864$ | $-0.0026193864$ |

The last two columns agree to machine precision in both rows, the discrepancy being below $2\times10^{-15}$: the exact identity holds. The agreement is limited only by the cancellation in forming the deficit, which is a difference of quantities an order of magnitude larger. At the smaller step the gap between $\delta S$ and $\delta\langle K_0\rangle$ is $7.3\times10^{-5}$, while at ten times the step it is $2.6\times10^{-3}$, a factor of about $36$ — the quadratic scaling of the relative entropy, which is the content of the first law. The deficit is negative, $\delta S<\delta\langle K_0\rangle$, as the positivity of relative entropy requires.

The scaling was checked further at a step of $10^{-4}$, where $\delta S-\delta\langle K_0\rangle=-2.93\times10^{-10}$, consistent with a quadratic coefficient of order $0.03$. The first law $\delta S=\delta\langle K_0\rangle$ is therefore recovered as the $s\to0$ limit, and the correction is the closed-form relative entropy.

## The Relative Modular Hamiltonian

The deficit in the exact identity has its own operator, and it is the one introduced in the relative-entropy companion article. On the algebra the relative modular operator of two states is
$$
\Delta_{\tilde\rho,\tilde\sigma}\big(\tilde A\big)
=\tilde\rho\,\tilde A\,\tilde\sigma^{-1},
\qquad
\log\Delta_{\tilde\rho,\tilde\sigma}\big(\tilde A\big)
=\log\tilde\rho\,\tilde A-\tilde A\log\tilde\sigma,
$$
with relative modular Hamiltonian $K_{\tilde\rho,\tilde\sigma}=-\log\Delta_{\tilde\rho,\tilde\sigma}$. Evaluated on the GNS vector $\Omega_{\tilde\rho}=\tilde\rho^{1/2}$, the logarithm of the relative modular operator has expectation the relative entropy,
$$
S(\tilde\rho\|\tilde\sigma)
=\big\langle\Omega_{\tilde\rho},\log\Delta_{\tilde\rho,\tilde\sigma}\Omega_{\tilde\rho}\big\rangle,
$$
as the relative-entropy companion article established, which in terms of the relative modular Hamiltonian reads
$$
\big\langle K_{\tilde\rho,\tilde\sigma}\big\rangle_{\tilde\rho}
=-S(\tilde\rho\|\tilde\sigma).
$$
The exact form of the first law therefore reads
$$
\delta S=\delta\langle K_{\tilde\sigma}\rangle+\big\langle K_{\tilde\rho,\tilde\sigma}\big\rangle_{\tilde\rho},
$$
so the first law's deficit is exactly the negative of the expectation of the **relative** modular Hamiltonian. When the two states commute — which in the biquaternion framework means that their Bloch vectors are collinear, $\hat{\mathbf r}=\pm\hat{\mathbf r}_0$ — the relative modular Hamiltonian reduces to the difference of the two modular Hamiltonians acting on the shared axis, and the relative entropy becomes the classical relative entropy of the two eigenvalue pairs. The general case is the non-commuting rotation captured by the angle $\gamma$ of the closed form.

## The Entanglement Hamiltonian of a Qubit

The modular Hamiltonian of a biquaternion state is a concrete two-level operator, and its spectrum is worth recording because it displays the state dependence of the entanglement energy. The eigenvalues of $\tilde\rho_0$ are $\lambda_\pm=\tfrac12(1\pm r_0)$, so the eigenvalues of $K_0=-\log\tilde\rho_0$ are
$$
\varepsilon_\pm=-\log\tfrac12\big(1\pm r_0\big),
$$
and the **level splitting** of the entanglement Hamiltonian is
$$
\varepsilon_--\varepsilon_+=\log\frac{1+r_0}{1-r_0}=2\,b=2\,\mathrm{artanh}(r_0).
$$
The splitting vanishes at the trace state, where the entanglement Hamiltonian is trivial up to a constant, and diverges on the pure boundary, where the state is a zero divisor and $K_0$ ceases to be an algebra element. At the reference state of the previous section, $r_0=0.538516$, the eigenvalues are $\varepsilon_+=0.262329$ and $\varepsilon_-=1.466456$, with splitting $1.204128=2\,b$, all checked against the matrix logarithm. The identity
$$
\tilde\rho_0=e^{-K_0}
$$
holds exactly, so the state is the thermal state of its own entanglement Hamiltonian at unit modular temperature, and the trace condition $\mathrm{Tr}\,\tilde\rho_0=1$ is the normalisation of that thermal state. The framework's entanglement Hamiltonian is thus an ordinary $\mathbb{M}_+$ element with a two-point spectrum, and the first law relates the entropy of the state to its expectation; the field-theoretic entanglement Hamiltonian of a region is the infinite-dimensional analogue of this object, with continuous spectrum and a geometric generator.

## Why the Law Is Exact to First Order

The framework's terms make the mechanism transparent, and it is worth stating because it is the reason the law is universal.

**The modular energy is linear in the state.** The quantity $\delta\langle K_0\rangle=\mathrm{Tr}(\delta\rho\,K_0)$ is the trace pairing of the perturbation with a fixed algebra element. It has no quadratic or higher terms. All nonlinearity in the relation therefore resides in $\delta S$, and the identity $\delta S=\delta\langle K_0\rangle-S(\rho\|\rho_0)$ says that $\delta S$ departs from the linear form by exactly the relative entropy.

**The relative entropy has no linear term.** As the relative-entropy companion article records, the second-order term of $S(\rho\|\rho_0)$ near $\rho=\rho_0$ is the Kubo–Mori–Bogoliubov metric of the reference state. There is no linear term, by the positivity and the stationarity of the relative entropy at coincidence. The first law is the statement of that vanishing, and the framework's closed form exhibits it: the boxed relative entropy is quadratic in $\delta\mathbf r$ near $\mathbf r=\mathbf r_0$.

**The deficit is a metric distance.** Because $-S(\rho\|\sigma)$ is, to second order, the negative of a metric form, the gap in the first law is the squared "distance" of the perturbation from the reference state in the state space. The inequality $\delta S\le\delta\langle K_0\rangle$ is therefore the statement that entropy changes are bounded by modular-energy changes, with the bound saturated only at the reference state — the framework's form of the entanglement first law and of its positivity.

## The Entanglement Hamiltonian of a Subsystem

The name "entanglement Hamiltonian" comes from the case in which $\sigma=\mathrm{Tr}_{\bar A}\,\Psi$ is the reduced state of a subsystem $A$ of a larger system. Then $K_A=-\log\sigma_A$ is an operator on $A$'s Hilbert space, and
$$
\sigma_A=\frac{e^{-K_A}}{\mathrm{Tr}\,e^{-K_A}},
$$
so the reduced state is the thermal state of its own entanglement Hamiltonian. In the biquaternion framework the reduced states of the tensor powers $\mathbb{B}^{\otimes n}$ are the partial traces of the strong-subadditivity companion article, and the entanglement Hamiltonian of a subsystem is
$$
K_A=-\log\tilde\rho_A\in\mathbb{M}_+^{\otimes n_A},
$$
an informational-sector element of the subsystem's algebra, obtained from the biquaternion logarithm of the reduced state. The first law for the reduced state, $\delta S_A=\delta\langle K_A\rangle-S(\tilde\rho_A\|\tilde\rho_{A,0})$, is then the statement that the subsystem's entropy and its entanglement energy move together at first order — the local form of the law that the applications in the next section use.

The finite framework cannot supply the field-theoretic entanglement Hamiltonian of a region: the local algebra is type III, its reduced state does not exist as a density matrix, and $K_A$ is a formal operator affiliated with the algebra rather than an element of it. What the framework supplies is the exact finite model, in which the entanglement Hamiltonian is an element and the first law is an identity.

## Applications

The first law of entanglement is used in three standard ways, none of them derived here.

- **Linearized gravity from entanglement.** Demanding that the first law hold for the vacuum entanglement of all small balls in a perturbed geometry yields the linearized Einstein equations about a maximally symmetric background. The modular Hamiltonian of a ball in the vacuum is the boost generator smeared with the appropriate weight, by the Bisognano–Wichmann theorem, and the first law converts its variation into the stress tensor.
- **The first law of black-hole mechanics.** The variation of the entanglement entropy of the degrees of freedom outside a horizon, weighted by the modular Hamiltonian of the horizon algebra, reproduces the first law $\delta M=\frac{\kappa}{2\pi}\delta S+\ldots$ for perturbations of a stationary black hole.
- **Entanglement equilibrium.** Requiring the vacuum to extremize the entanglement entropy of a small region subject to a fixed volume reproduces the Einstein equations with a cosmological constant, again through the first law.

The biquaternion framework's role is to make the finite-dimensional prototype of the law exact and closed-form. It does not supply the geometric modular Hamiltonians that the applications need; those are the field-theoretic ones of the Bisognano–Wichmann companion article.

## What Is Established and What Is Interpretation

**Established (theorem, imported).** The first law of entanglement; its derivation from the vanishing of the linear term of relative entropy; the identification of the modular Hamiltonian as the entanglement Hamiltonian of a reduced state; the applications to linearized gravity, black-hole mechanics, and entanglement equilibrium; the Kubo–Mori–Bogoliubov form of the second-order term. All standard.

**Established (recomputed here).** The closed form $K_0=\tfrac12\log\frac{4}{1-r_0^2}e_0-i\,b\,\gamma_0\in\mathbb{M}_+$; its expectation $\langle K_0\rangle_{\tilde\rho}=-\tfrac12\log\frac{1-r_0^2}{4}-r\,\mathrm{artanh}(r_0)\cos\gamma$; the exact identity $\delta S=\delta\langle K_0\rangle-S(\tilde\rho\|\tilde\rho_0)$; and its verification to machine precision on the explicit perturbation, with the quadratic scaling of the deficit.

**Interpretation.** That the modular Hamiltonian's being an element of $\mathbb{M}_+$ is read as the first law's being a relation between an entropy (a scalar) and the expectation of an informational-sector element, and that the exact identity is read as the framework's sharp form of the law.

**Gaps, left visible.** The finite algebra cannot supply a field-theoretic entanglement Hamiltonian or a geometric region; the applications are to type III local algebras. The framework supplies no dynamics and no state selection, and no empirical consequence is derived.

## Open Questions

**1. The entanglement Hamiltonian in the tensor power.** For a reduced state of $\mathbb{B}^{\otimes n}$, $K_A=-\log\tilde\rho_A$ is a biquaternion element by the closed form of the companion article. Is the map from the region $A$ to $K_A$ compatible with the partial-trace structure, in the sense of a conditional modular Hamiltonian?

**2. The modular Hamiltonian of the vacuum module.** The Reeh–Schlieder companion article locates the vacuum in the minimal left ideal. Is there a natural entanglement Hamiltonian on the module whose finite restriction is $K_0$ above, and whose field limit is the boost generator?

**3. The second law of entanglement.** The exact identity gives $\delta S\le\delta\langle K_0\rangle$. Does the framework's closed form give a similarly exact monotonicity under partial trace or under coarse-graining, refining the strong-subadditivity companion article?

**4. The geometry of the deficit.** The deficit is the Kubo–Mori metric distance to the reference state. On the Bloch ball this is a computable Riemannian geometry; does its completion, continued to a regulated many-mode model, reproduce the geometric data of the applications (the ball's modular Hamiltonian and the stress-tensor response)?

**5. Empirical contact.** As everywhere in the subcategory, no prediction distinguishing the reading from standard quantum information theory is derived.

## Summary

The modular Hamiltonian is $K=-\log\Delta$, the generator of the modular flow; in finite dimension it is $K=-\log\rho$, the logarithm of the state, and its expectation is the state's modular energy. The first law of entanglement states that a small perturbation of a state changes its entropy and its modular energy by equal amounts, $\delta S=\delta\langle K_0\rangle$, to first order.

In the biquaternion framework the modular Hamiltonian of a faithful state is the closed-form informational-sector element $K_0=\tfrac12\log\frac{4}{1-r_0^2}e_0-i\,b\,\gamma_0$, with $b=\mathrm{artanh}(r_0)$, and its expectation in any state is $-\tfrac12\log\frac{1-r_0^2}{4}-r\,\mathrm{artanh}(r_0)\cos\gamma$. The first law is the first-order shadow of the exact identity
$$
\delta S=\delta\langle K_0\rangle-S(\tilde\rho\|\tilde\rho_0),
$$
which follows from $K_0=-\log\tilde\rho_0$ and the definition of relative entropy, and which gives $\delta S\le\delta\langle K_0\rangle$ by the positivity of relative entropy. The identity was verified to machine precision on the reference state $\mathbf r_0=(0.3,-0.2,0.4)$ displaced along $\mathbf v=(0.12,0.18,-0.07)$, with the deficit scaling quadratically in the step and equal to the closed-form relative entropy.

The mechanism is that the modular energy is linear in the state while the relative entropy has no linear term, its second-order part being the Kubo–Mori–Bogoliubov metric. The first law is therefore the statement that the relative entropy is positive and quadratic at the reference state, and the framework writes the correction term exactly at every order. The entanglement Hamiltonian of a subsystem is the modular Hamiltonian of the reduced state, an element of the subsystem's informational sector in the finite framework and a formal operator in the field.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_+,\mathbb{M}_-$ | Informational (Hermitian) and material (anti-Hermitian) subspaces |
| $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$ | Trace pairing; $\mathrm{Tr}(e_0)=2$ |
| $\Delta_\sigma=S^*S$ | Modular operator of the state $\sigma$ |
| $K_\sigma=-\log\Delta_\sigma$ | Modular Hamiltonian |
| $K_0=-\log\tilde\rho_0$ | Modular Hamiltonian of a biquaternion state $\in\mathbb{M}_+$ |
| $r_0=|\mathbf r_0|$, $b=\mathrm{artanh}(r_0)$, $\gamma_0=\hat{\mathbf r}_0\cdot\mathbf e$ | Reference-state data |
| $\langle K_0\rangle_{\tilde\rho}=\mathrm{Tr}(\tilde\rho K_0)$ | Modular energy of $\tilde\rho$ |
| $\delta S=S(\tilde\rho)-S(\tilde\rho_0)$ | Entropy change |
| $\delta\langle K_0\rangle=\mathrm{Tr}((\tilde\rho-\tilde\rho_0)K_0)$ | Modular-energy change |
| $\delta S=\delta\langle K_0\rangle-S(\tilde\rho\|\tilde\rho_0)$ | Exact identity; first law to first order |
| $K_A=-\log\tilde\rho_A$ | Entanglement Hamiltonian of the subsystem $A$ |

## Further Reading

- R. Kubo, "Statistical-mechanical theory of irreversible processes I," *Journal of the Physical Society of Japan* **12** (1957) 570–586, for the modular correlation functions.
- M. Takesaki, *Tomita's Theory of Modular Hilbert Algebras and Its Applications* (Springer, 1970), for the modular operator and the modular Hamiltonian.
- H. Araki, "Relative entropy of states of von Neumann algebras," *Publications of the Research Institute for Mathematical Sciences* **11** (1976) 809–833, for the relative entropy whose positivity makes the law an inequality.
- T. Faulkner, M. Guica, T. Hartman, R. C. Myers, and M. Van Raamsdonk, "Gravitation from entanglement in holographic CFTs," *Journal of High Energy Physics* **03** (2014) 051, for the first law of entanglement and its use in deriving linearized gravity.
- T. Jacobson, "Thermodynamics of spacetime: the Einstein equation of state," *Physical Review Letters* **75** (1995) 1260–1263, for the thermodynamic derivation of the Einstein equations.
- J. D. Bekenstein, "Black holes and entropy," *Physical Review D* **7** (1973) 2333–2346, and S. W. Hawking, "Particle creation by black holes," *Communications in Mathematical Physics* **43** (1975) 199–220, for the entropy and the first law of black-hole mechanics.
- R. M. Wald, "Black hole entropy is the Noether charge," *Physical Review D* **48** (1993) R3427, for the first law in its geometric form.
- M. Van Raamsdonk, "Building up spacetime with quantum entanglement," *General Relativity and Gravitation* **42** (2010) 2323–2329, for the entanglement-equals-geometry reading.
- M. Ohya and D. Petz, *Quantum Entropy and Its Use* (Springer, 1993), for the Kubo–Mori–Bogoliubov metric and the second-order expansion of relative entropy.
- Companion article *Relative Entropy and the Biquaternion Framework*, for the closed-form relative entropy and its second-order term.
- Companion article *Thermal Time and the Modular Flow in the Biquaternion Framework*, for the modular Hamiltonian as the generator of the flow.
- Companion article *The Modular Theory of Tomita–Takesaki under the Biquaternion Framework*, for the modular operator and conjugation.
- Companion article *Strong Subadditivity in the Biquaternion Framework*, for the reduced states and partial traces of the tensor powers.
- Companion article *The Bisognano–Wichmann Theorem under the Biquaternion Framework*, for the geometric modular Hamiltonian of a wedge.
