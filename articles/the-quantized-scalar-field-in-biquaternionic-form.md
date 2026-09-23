# __The Quantized Scalar Field in Biquaternionic Form__

## Introduction

The companion article *Canonical Quantization of the Biquaternion Klein–Gordon Field* promotes the classical central-valued field $\tilde{\Phi}=\phi\,e_0$ to an operator, imposes the equal-time commutators, expands it in the parent's plane waves, and obtains the mode algebra, the Fock space and the Hamiltonian. It leaves one object unexamined for its own sake: the **field operator** $\hat{\tilde{\Phi}}(\tilde{X})$ itself. This article is about that object — what kind of thing it is, how it splits, what its algebra is, how it transforms, and what its correlation functions are.

The distinction from the companion quantization is the same as the distinction between the Dirac equation article and the *solutions* article of the spin-$\tfrac12$ sector. There the field equation was one subject and the space of its solutions, with the plane waves, normalizations and spin sums, was another. Here the mode algebra was one subject, and the field operator built from it is another. The article's question is exact:

> In what sense is the operator-valued field of the framework a **biquaternionic** object, and in what sense is it merely an operator constructed on a module?

Three answers organise the article, and they are not the same answer.

1. **Its value space.** The field is central-valued: at each event it is an operator times $e_0$, so its value-space indices are trivial, its Lorentz transformation has no spin part, and it commutes with every element of the algebra. This is the operator form of the statement that spin $0$ lives in the center.
2. **Its algebra.** The field is an operator-valued distribution, unbounded, and its commutator with its adjoint is a **multiple of the identity**, the commutator function. The field therefore generates a CCR algebra whose brackets are central; the non-commutativity of the field is a fixed c-number function, not an operator. This is what makes the scalar field bosonic, and it is the structure $\mathbb{B}$ cannot host, as the companion article *Fock Space and Creation/Annihilation Operators in Biquaternionic Form* proves.
3. **Its phases.** The only biquaternion structure the field carries is the transport of the central phase $e^{\pm i\,\mathrm{Sc}(\tilde{K}\bar{\tilde{X}})}$ and the centrality of that phase. The mass shell is a level set of the norm form; the exponentials are central unitaries; the Lorentz rotors act trivially on them.

The article is organised as follows. The next section treats the field as an operator-valued distribution and fixes its value space. The following section separates its positive- and negative-frequency parts. The next section treats the real and complex cases and charge conjugation. The section after that establishes the c-number character of the field commutator. The next section gives the two-point functions and the propagator, read through the norm form. A section treats the transformation of the field operator under the Poincaré group and the central phase. The final section separates what is standard from what is open.

- Companion article *Canonical Quantization of the Biquaternion Klein–Gordon Field*, for the Lagrangian, the equal-time commutators, the mode algebra, and the Hamiltonian.
- Companion article *The Klein–Gordon Equation in Biquaternionic Form*, for the field equation, its two branches, and the mass-shell condition.
- Companion article *Noether's Theorem in Biquaternionic Form*, for the $U(1)$ current $\tilde J\in\mathbb{M}_-$ and the energy–momentum tensor.
- Companion article *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, for the material four-wavevector, the norm form, and the plane-wave phase.
- Companion article *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*, for the trace argument that excludes a bosonic mode from $\mathbb{B}$ and for the Fock construction the field acts on.
- Companion article *The Spin–Statistics Theorem in Biquaternionic Form*, for the connection between spin and the c-number commutator.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0=1,e_1,e_2,e_3$ with $e_k^2=-e_0$, and $i$ is the central scalar imaginary. The material and informational sectors are $\mathbb{M}_-$ and $\mathbb{M}_+$, with $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ and $i\mathbb{M}_\pm=\mathbb{M}_\mp$; the center is $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_0,ie_0\}$. The conjugations are $\bar{\cdot}$ (quaternion), ${}^*$ (complex), ${}^\dagger=\bar{\cdot}^{\,*}$ (Hermitian) and ${}^\flat=-\dagger$. The gradient is $\tilde{\nabla}=e_0\partial_{ict}+e_1\partial_x+e_2\partial_y+e_3\partial_z$, and $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}=\partial_{ict}^2+\Delta$. The trace formula is $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$. Natural units $\hbar=c=1$ are used where the algebra is at issue, with $E_{\mathbf{p}}=\sqrt{\mathbf{p}^2+\mu^2}$ and $\mu=mc/\hbar$, and dimensionful factors are restored where they carry meaning. Physical components are written $x=(t,\mathbf{x})$ and $p=(\omega,\mathbf{p})$; the material four-wavevector is $\tilde{K}=i\omega\,e_0+\mathbf{p}$ in these units.

## The Field Operator and Its Value Space

Quantization replaces the classical field by an operator-valued distribution. For a test function $f$ on spacetime, the smeared field is

$$
\hat{\tilde{\Phi}}(f)=\int d^4x\,f(x)\,\hat{\tilde{\Phi}}(\tilde{X}),
\qquad
\hat{\tilde{\Phi}}(f)^\dagger=\int d^4x\,f^*(x)\,\hat{\tilde{\Phi}}(\tilde{X})^\dagger,
$$

and it is this smeared object, not the point value, that is a well-defined operator on the Fock space. The point value is recovered formally as $f\to\delta^{(4)}(x-X)$. The field is unbounded, as any field with an infinite ladder must be, and its domain is the finite-particle subspace of the Fock space.

The value space of the field is the center. In the mode expansion

$$
\hat{\tilde{\Phi}}(\tilde{X})=\hat{\phi}(x)\,e_0,
\qquad
\hat{\phi}(x)=\int\!\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf{p}}}}
\left(\hat a_{\mathbf{p}}e^{-ip\cdot x}+\hat b_{\mathbf{p}}^\dagger e^{+ip\cdot x}\right),
$$

every coefficient multiplies the central unit $e_0$. Three consequences follow immediately and are worth stating separately.

- **The field commutes with the algebra.** For every $\tilde A\in\mathbb{B}$ and every test function, $[\hat{\tilde{\Phi}}(f),\tilde A]=0$ in the sense that the field carries no value-space index on which $\tilde A$ could act. The algebra's action on the state module and the field's action on the Fock space are independent; the field is a scalar with respect to $\mathbb{B}$.
- **There is no spin part to its Lorentz transformation.** A field in a nontrivial representation of the Lorentz group transforms by a rotor $\tilde\Lambda\in\mathbb{M}_+$ acting on its indices. A central element is fixed by rotor conjugation, $\tilde\Lambda\tilde\Phi\tilde\Lambda^\dagger=\tilde\Phi$, because $\tilde\Phi$ commutes with $\tilde\Lambda$ and $\tilde\Lambda\tilde\Lambda^\dagger=e_0$. The triviality of the spin-$0$ representation is thus an algebraic identity about the center, not an assumption.
- **The field is not an element of $\mathbb{B}$.** Its coefficients $\hat a_{\mathbf{p}},\hat b_{\mathbf{p}}$ are not in the algebra, as the trace argument below shows; the field is an operator on the Fock space built from a module, and the center is only its value space.

## The Positive- and Negative-Frequency Parts

The decomposition of the field into its two exponential branches is the operator form of the two-branch structure of the parent equation. Define

$$
\hat{\phi}^{(+)}(x)=\int\!\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf{p}}}}\,\hat a_{\mathbf{p}}\,e^{-ip\cdot x},
\qquad
\hat{\phi}^{(-)}(x)=\int\!\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf{p}}}}\,\hat b_{\mathbf{p}}^\dagger\,e^{+ip\cdot x},
$$

so that $\hat{\phi}=\hat{\phi}^{(+)}+\hat{\phi}^{(-)}$ and $\hat{\phi}^\dagger=\hat{\phi}^{(+)\dagger}+\hat{\phi}^{(-)\dagger}$, with $\hat{\phi}^{(+)\dagger}$ containing $\hat a_{\mathbf{p}}^\dagger$ and $\hat{\phi}^{(-)\dagger}$ containing $\hat b_{\mathbf{p}}$. Two facts fix the interpretation.

**The positive-frequency part annihilates the vacuum.** Because $\hat a_{\mathbf{p}}|0\rangle=0$ for every $\mathbf{p}$,

$$
\hat{\phi}^{(+)}(x)|0\rangle=0,
\qquad
\langle0|\hat{\phi}^{(-)}(x)=0 ,
$$

so $\hat\phi^{(+)}$ is the **annihilation part** and $\hat\phi^{(-)}$ the **creation part**. The same statement in the biquaternion notation is that the annihilation part is the transport of the vacuum by the positive-frequency central phase.

**The frequency split is Lorentz invariant.** The split is defined by the sign of the energy, and the sign of the energy is preserved by orthochronous Lorentz transformations; equivalently, the positive-frequency part continues analytically in the upper half of the complex time plane when the phase is written $e^{-iE_{\mathbf{p}}t}$. This is the standard statement that the Wightman function is the boundary value of an analytic function, and the framework's central phase $e^{\,i\,\mathrm{Sc}(\tilde{K}\bar{\tilde{X}})}$ is the phase in which the statement is made.

**Verification.** The annihilation property was checked on the explicit truncated Fock space: with $\hat\phi^{(+)}$ represented by the lowering operator on the span of $|0\rangle,\dots,|6\rangle$, the vector $\hat\phi^{(+)}|0\rangle$ vanished exactly, and the number operator $\hat N=\hat a^\dagger\hat a$ returned $0$ on the vacuum state.

## Real and Complex Scalar Fields

The framework admits both cases, and their difference is the standard one, sharpened by the algebra's conjugation structure.

**The complex (charged) field.** Here $\hat\phi^\dagger\ne\hat\phi$, and the expansion contains two independent operator sets, $\hat a_{\mathbf{p}}$ and $\hat b_{\mathbf{p}}$. The field carries a conserved $U(1)$ charge, with $[\hat Q,\hat\phi]=-\hat\phi$ and $[\hat Q,\hat\phi^\dagger]=+\hat\phi^\dagger$, so the field operator has a definite charge and its conjugate has the opposite one. The charge is the Noether charge of the current $\tilde J\in\mathbb{M}_-$ of the companion article *Noether's Theorem in Biquaternionic Form*.

**Charge conjugation.** The map that exchanges particles and antiparticles is

$$
\mathcal{C}:\ \hat\phi\ \longmapsto\ \hat\phi^{\mathcal{C}}=\hat\phi^\dagger ,
\qquad
\hat a_{\mathbf{p}}\leftrightarrow\hat b_{\mathbf{p}},
\qquad
\hat Q\longmapsto-\hat Q ,
$$

and it leaves the commutators and the Hamiltonian invariant. It is an antiunitary-or-unitary operation according to the convention for the mode operators; the corpus's concern is only that it is the map that reverses the charge, and it is the standard one.

**The real (neutral) field.** Imposing $\hat\phi^\dagger=\hat\phi$ forces $\hat b_{\mathbf{p}}=\hat a_{\mathbf{p}}$ and reduces the expansion to a single set of modes,

$$
\hat\phi(x)=\int\!\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf{p}}}}
\left(\hat a_{\mathbf{p}}e^{-ip\cdot x}+\hat a_{\mathbf{p}}^\dagger e^{+ip\cdot x}\right),
$$

in which the field creates and destroys its own antiparticle. The charge vanishes identically, and the $U(1)$ symmetry of the complex case is not present. In the framework's terms the real field is a **Hermitian central-valued** operator field, while the complex field is a central-valued field whose conjugate is a distinct operator.

**The real structure is not charge conjugation.** The algebra carries the anti-Hermitian conjugation $\tilde{\Phi}^\flat=-\tilde{\Phi}^\dagger$, which on a central element is $\phi\,e_0\mapsto-\phi^*e_0$. This is the algebra's real structure; it is not the particle–antiparticle exchange, because it acts on the value space rather than on the mode operators and it carries a minus sign. The two operations coincide only after a further convention is fixed, and the framework does not fix one. What the framework does supply is the **central phase** $e^{i\alpha}$ under which $\hat\phi\to e^{-i\alpha}\hat\phi$, generated by the charge; this $U(1)$ is the group that the companion articles *Goldstone's Theorem in Biquaternionic Form* and *The Higgs Mechanism in Biquaternionic Form* take as the framework's canonical continuous symmetry.

## The Field Algebra: Commutators as c-Numbers

The defining property of a bosonic field is that its commutator is a c-number. From the mode algebra,

$$
\big[\hat{\phi}(x),\hat{\phi}^\dagger(y)\big]
=\int\!\frac{d^3p}{(2\pi)^3\,2E_{\mathbf{p}}}
\left(e^{-ip\cdot(x-y)}-e^{+ip\cdot(x-y)}\right)
\equiv i\Delta(x-y),
$$

while

$$
\big[\hat{\phi}(x),\hat{\phi}(y)\big]=0,
\qquad
\big[\hat{\phi}^\dagger(x),\hat{\phi}^\dagger(y)\big]=0 .
$$

The right-hand side of the first relation is a multiple of the identity, so the field generates a **CCR algebra** whose brackets are central; the field is an operator, but the failure of its operators at two events to commute is a fixed function of the separation and not an operator. This is the precise sense in which the scalar field is a classical field with operator coefficients. For the Dirac field the analogous object is an operator-valued matrix, and the difference is exactly the difference between bosonic and fermionic quantization.

**Verification on the truncated space.** On a two-mode truncation with $\hat\phi(f)=f_1\hat a_1+f_2\hat b_2^\dagger$ and $\hat\phi(g)=g_1\hat a_1+g_2\hat b_2^\dagger$, the abstract commutators give $[\hat\phi(f),\hat\phi(g)^\dagger]=(f_1g_1^*-f_2g_2^*)e_0$; the explicit matrices for $\hat a|n\rangle=\sqrt n|n-1\rangle$ reproduce the diagonal values $+1$ and $-1$ for the two modes on the low-lying states, with the expected boundary entry at the top level of the truncation. The central conclusion — that the bracket is a scalar and not an operator — is the content of the identity $0=\mathrm{Tr}[\tilde A,\tilde B]$ applied to the algebra, and it is what forbids the ladder from living in $\mathbb{B}$: a canonical commutator $[\tilde a,\tilde a^\dagger]=c\,e_0$ would have trace $2c\ne0$, so $c=0$.

The field commutator has the two physical properties recorded for it in the companion quantization. At equal times it vanishes, because the momentum integrand is odd; for spacelike separation it vanishes, which is microcausality; and its support is the light cone and its interior, which is the causal structure the quantization preserves.

## The Two-Point Functions and the Propagator

The field operator's content is exhausted by its correlation functions. The basic one is the **Wightman function**

$$
W(x-y)=\langle0|\hat{\phi}(x)\hat{\phi}^\dagger(y)|0\rangle
=\int\!\frac{d^3p}{(2\pi)^3\,2E_{\mathbf{p}}}\,e^{-ip\cdot(x-y)},
$$

which is precisely the positive-frequency part of the commutator function and is annihilated by the Klein–Gordon operator in each variable,

$$
\left(\Box_x-\mu^2\right)W(x-y)=0,
$$

because every mode in the integral is on shell. The Feynman propagator is the time-ordered combination

$$
\Delta_F(x-y)=\langle0|T\,\hat{\phi}(x)\hat{\phi}^\dagger(y)|0\rangle
=\theta(x^0-y^0)W(x-y)+\theta(y^0-x^0)W(y-x),
$$

whose momentum-space form is

$$
\Delta_F(p)=\frac{i}{p^2-\mu^2+i\epsilon},
\qquad
p^2=\omega^2-\mathbf{p}^2 ,
$$

with the $i\epsilon$ prescription that selects the positive-frequency part for the forward propagation. Its scalar two-point function is the Green's function of the parent equation; the companion article *The Feynman Propagator in Biquaternionic Form* constructs the analogous object for the spin-$\tfrac12$ field, and the scalar case is the standard one.

The biquaternion reading of the propagator is a rewriting of the denominator. With the material four-wavevector $\tilde{K}=i\omega\,e_0+\mathbf{p}$, the norm form is $N(\tilde{K})=(-\omega^2+\mathbf{p}^2)e_0$, so that $p^2=-N(\tilde{K})$ and

$$
p^2-\mu^2=-\left(N(\tilde{K})+\mu^2\right),
\qquad
\Delta_F(\tilde{K})=-\frac{i}{N(\tilde{K})+\mu^2-i\epsilon}.
$$

The denominator is the mass-shell function of the parent article: the pole of the propagator is the level set $N(\tilde{K})=-\mu^2$, and the $i\epsilon$ prescription displaces the pole off the real axis. The two-point function is thus the norm form's inverse, shifted by the mass; the companion article *The Scalar Field Path Integral in Biquaternionic Form* makes the same statement for the free Gaussian, whose width is the shifted norm form, and this identification of the pole with the mass-shell level set is the only place where the propagator's biquaternion form is more than a rewriting.

## Transformation of the Field Operator

The Poincaré group acts on the field by

$$
U(\Lambda,a)\,\hat{\tilde{\Phi}}(\tilde{X})\,U(\Lambda,a)^{-1}
=\hat{\tilde{\Phi}}\big(\Lambda\tilde{X}+a\big),
$$

the defining property of a scalar field: no matrix acts on the value space, and the argument is transported by the Lorentz transformation and the translation. In the framework's notation the Lorentz part is a rotor $\tilde\Lambda\in\mathbb{M}_+$ acting on the material coordinate by conjugation, $\tilde{X}\mapsto\tilde\Lambda\tilde{X}\tilde\Lambda^\dagger$, and the rotor acts trivially on the central value, $\tilde\Lambda e_0\tilde\Lambda^\dagger=e_0$. The spin-$0$ representation is thus the trivial representation of the rotor group on the center.

The internal symmetry acts by the central phase,

$$
\hat U_\alpha=e^{\,i\alpha\hat Q},
\qquad
\hat U_\alpha\,\hat{\tilde{\Phi}}\,\hat U_\alpha^{-1}
=e^{-i\alpha}\,\hat{\tilde{\Phi}},
\qquad
\hat U_\alpha\,\hat{\tilde{\Phi}}^\dagger\,\hat U_\alpha^{-1}
=e^{+i\alpha}\,\hat{\tilde{\Phi}}^\dagger ,
$$

and it commutes with the Poincaré action. The generator $\hat Q$ is the Noether charge of the current $\tilde J\in\mathbb{M}_-$; the phase is central, so it multiplies the field by a central unitary and does not act on the state module's spinor structure. In this sense the framework's canonical internal symmetry is the group of central phases, and the scalar field is its simplest charged representation.

Two statements must be kept apart, because the corpus uses both. The phase $e^{-i\alpha}$ is the **active** $U(1)$ transformation of the field operator, generated by the charge. The Wick-rotated weight $e^{-S_E/\hbar}$ is a **weight** in a functional integral on the center, not a transformation of the field; the two are distinct and are not to be identified. The former is a symmetry, the latter is a convergence factor.

## The Schrödinger Functional and the Field Basis

The field operator's representation on states can be made explicit with the field-basis wave functionals, and the connection to the functional-integral formulation of the scalar sector becomes transparent. A state is a functional $\Psi[\phi]$ of configurations; the field acts by multiplication and the momentum by differentiation,

$$
\langle\phi|\hat{\phi}(\mathbf{x})|\Psi\rangle=\phi(\mathbf{x})\,\Psi[\phi],
\qquad
\langle\phi|\hat{\pi}(\mathbf{x})|\Psi\rangle=-i\hbar\,\frac{\delta\Psi}{\delta\phi(\mathbf{x})},
$$

so the canonical commutator is the identity $\delta\phi(\mathbf{x})/\delta\phi(\mathbf{y})=\delta^{(3)}(\mathbf{x}-\mathbf{y})$ and the field-basis representation is the functional analogue of the coordinate representation of quantum mechanics. In this representation the Hamiltonian is a differential operator and the Schrödinger equation is a functional differential equation.

For the free scalar the ground-state functional is an explicit Gaussian. With the Hamiltonian of the companion quantization and the real field for economy,

$$
\Psi_0[\phi]\;\propto\;\exp\!\left(-\frac{1}{2}\int\frac{d^3p}{(2\pi)^3}\,E_{\mathbf{p}}\,\big|\tilde{\phi}(\mathbf{p})\big|^2\right)
=\exp\!\left(-\frac{1}{2}\int d^3x\,d^3y\;\phi(\mathbf{x})\,K(\mathbf{x}-\mathbf{y})\,\phi(\mathbf{y})\right),
$$

where $K$ has Fourier symbol $E_{\mathbf{p}}=\sqrt{\mathbf{p}^2+\mu^2}$; the vacuum wave functional is the exponential of a positive quadratic form, and its width is the norm form's square root. The Gaussian integral of this functional over configurations is the vacuum-to-vacuum amplitude of the scalar functional integral, and the transition functional $\Psi[\phi_f,t_f]=\int\mathcal{D}\phi_i\,K(\phi_f,t_f;\phi_i,t_i)\Psi[\phi_i,t_i]$ is its kernel. The framework's reading is that the wave functional is a functional of **central-valued** configurations, $\Psi[\phi]=\Psi[\phi\,e_0]$, and that it is a complex number for each configuration rather than an element of $\mathbb{B}$; the informational sector's density operators are recovered only in finite-dimensional truncations, as the Fock-space companion records.

## What Is Standard and What Is Open

**Standard, and transcribed.** The operator-valued-distribution status of the field and its smearing; the positive/negative frequency split and the vacuum annihilation property; the real and complex cases and charge conjugation; the c-number commutator, microcausality and the support of the commutator function; the Wightman function, the Feynman propagator and the $i\epsilon$ prescription; the Poincaré transformation law of a scalar field and the $U(1)$ phase. None of this is new, and none of it depends on the biquaternion structure beyond the kinematical conventions.

**Open in the biquaternion framework.**

- **The intrinsic operator field.** The field is central-valued because the classical field is. Whether a genuinely algebra-valued operator field, transforming in a representation of $\mathbb{B}$ rather than trivially, is available for spin $0$, is not decided; the center is the only value space that carries no spinor index.
- **The real structure and charge conjugation.** The algebra's $\flat=-\dagger$ and the particle–antiparticle exchange are distinct operations, and whether the framework prefers one over the other as the real structure of the scalar sector is a convention it does not fix.
- **The propagator's intrinsic derivation.** The scalar propagator is the inverse of the norm form shifted by the mass, but whether the framework derives the $i\epsilon$ prescription from its own complex structure — rather than importing it from the time-ordering of the operator formalism — is open, as the companion article *The Feynman Propagator in Biquaternionic Form* records for the spin-$\tfrac12$ case.
- **The bosonic gap.** The field's CCR algebra is not an object of $\mathbb{B}$: no pair in the algebra realizes $[\tilde a,\tilde a^\dagger]=e_0$. Whether an infinite-dimensional module canonically attached to $\mathbb{B}$ can carry the scalar ladder is the structural question, and it is not answered here.
- **Empirical content.** Whether the operator field as constructed yields a prediction distinguishing the framework from standard scalar field theory is open.

## Summary

The quantized scalar field of the framework is an operator-valued distribution whose value space is the center $\mathbb{C}_{\mathbb{B}}$: at each event it is an operator times $e_0$, it commutes with every element of $\mathbb{B}$, and the Lorentz rotors act on it trivially, which is the algebraic content of spin $0$. It splits into an annihilation part $\hat\phi^{(+)}$, which annihilates the vacuum and is the positive-frequency transport of the central phase, and a creation part $\hat\phi^{(-)}$, its adjoint; the split is Lorentz invariant because the sign of the energy is. The complex field carries a $U(1)$ charge, with $[\hat Q,\hat\phi]=-\hat\phi$, and charge conjugation is the exchange $\hat a\leftrightarrow\hat b$; the real field is the Hermitian case $\hat b=\hat a$ with vanishing charge. The algebra's real structure $\flat=-\dagger$ is not charge conjugation.

The defining property of the field is that its commutator is a c-number,

$$
\big[\hat{\phi}(x),\hat{\phi}^\dagger(y)\big]=i\Delta(x-y),
\qquad
\big[\hat{\phi}(x),\hat{\phi}(y)\big]=0,
$$

so the field generates a CCR algebra with central brackets; at equal times the commutator vanishes, and for spacelike separation it vanishes as well, which is microcausality. The two-point function is the positive-frequency Wightman function, annihilated by the Klein–Gordon operator, and the Feynman propagator is its time-ordered continuation with $\Delta_F(\tilde{K})=-i/(N(\tilde{K})+\mu^2-i\epsilon)$; its pole is the mass-shell level set of the norm form. The field transforms as a scalar under the Poincaré group and by the central phase under the $U(1)$, and the phase is central because the field's value space is.

The biquaternion content of the field operator is therefore confined to its value space and its phases: central-valuedness, the trivial rotor action, and the norm-form reading of the mass shell and the propagator pole. The ladder, the Fock space and the correlation functions are the standard bosonic construction on an imported module, and the algebra supplies no part of them; the companion article *Fock Space and Creation/Annihilation Operators in Biquaternionic Form* proves the exclusion by the trace of a commutator. The field is a scalar with respect to $\mathbb{B}$ and a standard bosonic operator field on the outside.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Central scalar imaginary |
| $\mathbb{M}_-,\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_0,ie_0\}$ | Center; the field's value space |
| $\tilde{X}=ict\,e_0+\mathbf{x}$ | Material coordinate |
| $\tilde{\nabla}=e_0\partial_{ict}+\sum_k e_k\partial_k$, $\Box=\partial_{ict}^2+\Delta$ | Gradient and d'Alembertian |
| $\hat{\tilde{\Phi}}(\tilde{X})=\hat{\phi}(x)e_0$ | Quantized scalar field (central-valued) |
| $\hat\phi^{(+)},\hat\phi^{(-)}$ | Annihilation (positive-frequency) and creation parts |
| $\hat a_{\mathbf{p}},\hat b_{\mathbf{p}}$ | Particle and antiparticle annihilation operators |
| $\hat Q$ | Conserved $U(1)$ charge; $[\hat Q,\hat\phi]=-\hat\phi$ |
| $\mathcal{C}:\hat\phi\mapsto\hat\phi^\dagger$ | Charge conjugation, $\hat a\leftrightarrow\hat b$, $\hat Q\mapsto-\hat Q$ |
| $i\Delta(x-y)=[\hat\phi(x),\hat\phi^\dagger(y)]$ | Commutator function (c-number) |
| $W(x-y)=\langle0|\hat\phi(x)\hat\phi^\dagger(y)|0\rangle$ | Wightman function (positive frequency) |
| $\Delta_F=\theta(x^0-y^0)W(x-y)+\theta(y^0-x^0)W(y-x)$ | Feynman propagator (time-ordered Wightman function) |
| $\Delta_F(\tilde{K})=-i/(N(\tilde{K})+\mu^2-i\epsilon)$ | Propagator in material notation; pole at $N(\tilde{K})=-\mu^2$ |
| $\tilde{K}=i\omega\,e_0+\mathbf{p}$, $N(\tilde{K})=\tilde{K}\bar{\tilde{K}}$ | Material four-wavevector and norm form |
| $\hat U_\alpha=e^{i\alpha\hat Q}$, $\hat\phi\to e^{-i\alpha}\hat\phi$ | Central $U(1)$ phase |
| $\tilde\Lambda\in\mathbb{M}_+$, $\tilde\Lambda e_0\tilde\Lambda^\dagger=e_0$ | Lorentz rotor; trivial action on the center |
| $\mathrm{Tr}(e_0)=2$, $\mathrm{Tr}[\tilde A,\tilde B]=0$ | Trace identity; no bosonic mode in $\mathbb{B}$ |

## Further Reading

- P. Jordan and W. Pauli, "Zur Quantenelektrodynamik ladungsfreier Felder," *Zeitschrift für Physik* **47** (1928) 151–173, for the commutator formulation of the quantized scalar field.
- W. Pauli and V. F. Weisskopf, "Über die Quantisierung der skalaren relativistischen Wellengleichung," *Helvetica Physica Acta* **7** (1934) 709–731, for the charged scalar field and the particle–antiparticle interpretation.
- A. S. Wightman, "Quantum field theory in terms of vacuum expectation values," *Physical Review* **101** (1956) 860–866, for the two-point function as the basic object of the theory.
- R. F. Streater and A. S. Wightman, *PCT, Spin and Statistics, and All That* (Benjamin, 1964), for the analyticity and positivity properties of the Wightman functions.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Fields* (McGraw-Hill, 1965), for the field operator, its smearing, and the commutator function.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), and M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the real and complex scalar fields, charge conjugation, and the Feynman propagator.
- R. Haag, *Local Quantum Physics: Fields, Particles, Algebras* (Springer, 1996), for the field as an operator-valued distribution and the algebraic formulation of the field net.
