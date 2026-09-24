# __Relative Entropy and the Biquaternion Framework__

## Introduction

**Relative entropy** is the basic information-theoretic quantity of quantum theory. Given two states $\rho$ and $\sigma$ of a system, it measures how well the two can be told apart, and it does so in a way that is monotone under every physical process: discarding information never increases it. In the finite-dimensional setting it is Umegaki's quantity
$$
S(\rho\|\sigma)=\mathrm{Tr}(\rho\log\rho)-\mathrm{Tr}(\rho\log\sigma),
$$
and every information-theoretic inequality of consequence — monotonicity, the data-processing inequality, strong subadditivity, the first law of entanglement — is a statement about it or a consequence of one. This article asks what relative entropy is in the biquaternion framework.

The answer has three parts, and they should be separated at the outset.

1. **The quantity is standard.** The states of the biquaternion algebra $\mathbb{B}\cong M_2(\mathbb{C})$ are, by the GNS companion article, the elements $\tilde\rho\in\mathbb{M}_+$ that are Hermitian, positive and of trace one, parametrized by the Bloch ball. Relative entropy on these states is Umegaki's. The framework does not modify it, and no new inequality is claimed for it.

2. **The quantity is exactly computable.** Because $\mathbb{B}$ is four-real-dimensional, both the state and its logarithm are elements of the algebra, and the trace is the identically real pairing $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$. The relative entropy of two biquaternion states therefore collapses to a closed expression in their Bloch vectors, which is derived and verified below.

3. **The quantity has a framework-specific boundary.** The logarithm of a state is an element of $\mathbb{B}$ exactly when the state is faithful, that is, in the interior of the Bloch ball; on the pure boundary the state is a zero divisor and $\log\tilde\rho$ does not exist as an algebra element. The relative entropy nevertheless extends continuously to the boundary, and it diverges there only in the one standard way, when the support of the first state is not contained in the support of the second. The zero-divisor cone is the locus on which the algebra's own logarithm fails and the imported logarithm is required.

The article proceeds as follows. Relative entropy is recalled with the properties that make it basic. The states of $\mathbb{B}$ and their logarithms are fixed. The closed form is derived. It is checked numerically on states that are generic superpositions, not axis-aligned ones. Positivity, asymmetry and monotonicity are read off in the Bloch geometry. Araki's relative modular operator is identified, because it is the object the modular companions generalize. The field-theoretic setting, in which relative entropy is the right quantity precisely where entanglement entropy is not, is recalled. The article closes with the established/interpretation/open split.

**Conventions.** Those of the companion articles. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with quaternion basis $e_0=1,e_1,e_2,e_3$ satisfying $e_k^2=-e_0$, scalar imaginary $i$ with $i^2=-1$, and isomorphism $\Phi(e_k)=-i\sigma_k$, $\Phi(i)=iI_2$, so that $\mathbb{B}\cong M_2(\mathbb{C})$. The material (anti-Hermitian) subspace is $\mathbb{M}_-$ and the informational (Hermitian) subspace is $\mathbb{M}_+$, with $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ and $i\mathbb{M}_\pm=\mathbb{M}_\mp$. Hermitian conjugation is $\dagger$, and the trace is normalized by the matrix representation, $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$, so that $\mathrm{Tr}(e_0)=2$. A state is $\tilde\rho\in\mathbb{M}_+$ with $\tilde\rho\ge0$ and $\mathrm{Tr}(\tilde\rho)=1$; the GNS data are those of *The GNS Construction in the Biquaternion Framework*.

## Relative Entropy: The Standard Quantity

### Definition

Let $\rho$ and $\sigma$ be density matrices on a finite-dimensional Hilbert space, with $\rho$ a state and $\sigma$ positive of trace one. The **relative entropy** (Umegaki, 1962) is
$$
S(\rho\|\sigma)=
\begin{cases}
\mathrm{Tr}\big(\rho\log\rho\big)-\mathrm{Tr}\big(\rho\log\sigma\big), & \mathrm{supp}\,\rho\subseteq\mathrm{supp}\,\sigma,\\[2pt]
+\infty, & \text{otherwise}.
\end{cases}
$$
Writing $\rho=\sum_i\lambda_i|i\rangle\langle i|$ and $\sigma=\sum_j\mu_j|j\rangle\langle j|$, the finite value is
$$
S(\rho\|\sigma)=\sum_{i,j}|\langle i|j\rangle|^2\,\lambda_i\big(\log\lambda_i-\log\mu_j\big),
$$
the sum being restricted to $\mu_j>0$. The definition is basis-independent and invariant under unitary conjugation of both arguments. It is not symmetric, $S(\rho\|\sigma)\neq S(\sigma\|\rho)$ in general, and it is not a metric: it belongs to the family of statistical divergences rather than to the metrics.

### The Properties That Make It Basic

Four properties are used throughout the corpus and are stated once here.

1. **Positivity (Klein's inequality).** $S(\rho\|\sigma)\ge0$, with equality if and only if $\rho=\sigma$. This is the quantum form of the Gibbs inequality.
2. **Joint convexity.** For $0\le p\le1$, $S\big(p\rho_1+(1-p)\rho_2\,\big\|\,p\sigma_1+(1-p)\sigma_2\big)\le p\,S(\rho_1\|\sigma_1)+(1-p)\,S(\rho_2\|\sigma_2)$.
3. **Monotonicity (the data-processing inequality).** For any completely positive trace-preserving map $\Lambda$, $S(\Lambda\rho\|\Lambda\sigma)\le S(\rho\|\sigma)$. Partial trace is such a map, so discarding a subsystem cannot increase distinguishability.
4. **Additivity and the chain rule.** $S(\rho_A\otimes\rho_B\|\sigma_A\otimes\sigma_B)=S(\rho_A\|\sigma_A)+S(\rho_B\|\sigma_B)$, and for a three-part split $ABC$,
$$
S(\rho_{ABC}\|\sigma_{ABC})=S(\rho_A\|\sigma_A)+S(\rho_{B|A}\|\sigma_{B|A})+S(\rho_{C|AB}\|\sigma_{C|AB}),
$$
with conditional relative entropies defined recursively.

The monotonicity property is the one that carries the most weight: applied to the partial trace it yields, by a standard argument, the strong subadditivity of the von Neumann entropy. That is the subject of the companion article *Strong Subadditivity in the Biquaternion Framework*, where the implication is carried out.

### Why Relative Entropy Rather Than Von Neumann Entropy

The von Neumann entropy $S(\rho)=-\mathrm{Tr}(\rho\log\rho)=\log\dim-S(\rho\|I/\dim)$ is the special case in which the second argument is the maximally mixed state; it is not monotone and is defined only for states with $\mathrm{supp}\,\rho$ of finite-dimensional type. Relative entropy is the more basic object, and in quantum field theory it is the only one of the two that is well defined for the local algebras: the local algebras are type III factors, which carry no trace and no density matrix, while the relative entropy of two states on a von Neumann algebra is defined by the Araki formula recalled below. This is the reason the informational reading of quantum field theory is written in the language of relative entropy, and it is the reason this article opens the subcategory.

## The States of the Biquaternion Algebra

### Density Matrices in $\mathbb{M}_+$

By the GNS companion article, every state on $\mathbb{B}$ is of the form $\omega(\tilde A)=\mathrm{Tr}(\tilde\rho\tilde A)$ with $\tilde\rho\in\mathbb{M}_+$ positive and of trace one. Writing
$$
\tilde\rho=\tfrac12\big(e_0+i\mathbf r\cdot\mathbf e\big),\qquad
\mathbf r\in\mathbb{R}^3,\qquad \mathbf e=(e_1,e_2,e_3),
$$
the eigenvalues are
$$
\lambda_\pm=\tfrac12\big(1\pm|\mathbf r|\big),
$$
and positivity plus the trace condition give exactly
$$
\tilde\rho\ \text{a state}\iff |\mathbf r|\le1 .
$$
The state is **pure** on the Bloch sphere $|\mathbf r|=1$, where $\tilde\rho=P_+(\hat{\mathbf r})=\tfrac12(e_0+i\hat{\mathbf r})$ is a minimal idempotent and $\tilde\rho^2=\tilde\rho$; it is **faithful** on the open Bloch ball $|\mathbf r|<1$, where both eigenvalues are positive; and it is the **trace state** at $\mathbf r=0$, where $\tilde\rho=\tfrac12e_0$ and $\omega$ is the normalized algebra trace.

The parameter is a genuine superposition coordinate: $\mathbf r$ is the Bloch vector of the state in the basis of the Pauli matrices, and a generic state has all three components nonzero. The computations below are performed on such generic vectors.

### The Logarithm of a Biquaternion State

The logarithm of a positive element of $\mathbb{B}$ is again an element of $\mathbb{B}$, and for the state above it takes a closed form. Two ingredients give it. First, the exponential of an element in the plane of a unit direction: for a unit pure quaternion $\hat{\mathbf r}$ one has $(i\hat{\mathbf r})^2=e_0$, so
$$
\exp\big(\theta\,i\hat{\mathbf r}\big)=\cosh\theta\,e_0+i\sinh\theta\,\hat{\mathbf r}.
$$
Second, the determinant of the state, $\det\Phi(\tilde\rho)=\lambda_+\lambda_-=\tfrac14(1-|\mathbf r|^2)=N(\tilde\rho)$, which vanishes exactly on the pure boundary. Writing the logarithm in the same form as the state,
$$
\log\tilde\rho=b_0\,e_0+i\,\mathbf b\cdot\mathbf e,
$$
the scalar part is fixed by the product of eigenvalues and the vector part by their ratio,
$$
b_0=\tfrac12\log\det\tilde\rho=\tfrac12\log\frac{1-|\mathbf r|^2}{4},\qquad
\mathbf b=\mathrm{artanh}\big(|\mathbf r|\big)\,\hat{\mathbf r},
$$
so that
$$
\log\tilde\rho=\tfrac12\log\frac{1-|\mathbf r|^2}{4}\,e_0
+i\,\mathrm{artanh}\big(|\mathbf r|\big)\,\hat{\mathbf r},
\qquad |\mathbf r|<1 .
$$
The formula was checked by exponentiating it and recovering $\tilde\rho$ coefficient by coefficient: with $b_0=\tfrac12\log\frac{1-r^2}{4}$ and $|\mathbf b|=\mathrm{artanh}(r)$ one has $e^{b_0}\cosh|\mathbf b|=\tfrac12$ and $e^{b_0}\sinh|\mathbf b|=r/2$, which is the state. The logarithm is **real**: $\log\tilde\rho\in\mathbb{M}_+$, as the modular-theory companion requires, since $b_0$ is real and the vector part is imaginary. Its scalar part is negative and tends to $-\infty$ as the state approaches the pure boundary, while its vector part has magnitude $\mathrm{artanh}(|\mathbf r|)$, which diverges on the boundary in every direction.

The domain is the open Bloch ball. On the pure boundary the state is a **zero divisor**, $N(\tilde\rho)=0$, and $\log\tilde\rho$ does not exist as an element of $\mathbb{B}$; the formal expression above diverges. This is not a defect of the framework but its zero-divisor structure appearing in the logarithm, and it is the reason the relative entropy is handled in two steps below: first as a finite expression in the interior, then by its continuous extension to the boundary.

## The Relative Entropy of Two Biquaternion States

### The Closed Form

Let
$$
\tilde\rho=\tfrac12\big(e_0+i\mathbf r\cdot\mathbf e\big),\qquad
\tilde\sigma=\tfrac12\big(e_0+i\mathbf s\cdot\mathbf e\big)
$$
be two states, with $|\mathbf r|,|\mathbf s|\le1$ and $\log\tilde\sigma$ existing, so that $|\mathbf s|<1$. The von Neumann entropy of a biquaternion state follows from the logarithm above and the trace formula,
$$
2\,\mathrm{Sc}\big(\tilde\rho\log\tilde\rho\big)
=\tfrac12\log\frac{1-|\mathbf r|^2}{4}+|\mathbf r|\,\mathrm{artanh}|\mathbf r|,
$$
so that
$$
S(\tilde\rho)=-\tfrac12\log\frac{1-|\mathbf r|^2}{4}-|\mathbf r|\,\mathrm{artanh}|\mathbf r| .
$$
At $\mathbf r=0$ this returns $\log2$, the entropy of the maximally mixed qubit state, and at $|\mathbf r|\to1$ it tends to $0$, the entropy of a pure state. For the cross term, the trace formula gives
$$
\mathrm{Tr}\big(\tilde\rho\log\tilde\sigma\big)
=\tfrac12\log\frac{1-|\mathbf s|^2}{4}
+|\mathbf r|\,\mathrm{artanh}|\mathbf s|\,\cos\gamma,
\qquad
\cos\gamma=\frac{\mathbf r\cdot\mathbf s}{|\mathbf r|\,|\mathbf s|},
$$
and therefore
$$
\boxed{\,S(\tilde\rho\|\tilde\sigma)
=\tfrac12\log\frac{1-|\mathbf r|^2}{1-|\mathbf s|^2}
+|\mathbf r|\Big(\mathrm{artanh}|\mathbf r|
-\mathrm{artanh}|\mathbf s|\,\cos\gamma\Big)\,}
$$
for $|\mathbf r|,|\mathbf s|<1$. The derivation is the whole content of the section: the two appearances of $\log$ are biquaternion logarithms, each computed by the closed form of the previous section, and their traces are the real pairing $2\,\mathrm{Sc}$. The factors of $\tfrac12\log\tfrac14$ cancel between the two terms, which is why the boxed expression contains only the ratio of determinants, $\frac{1-|\mathbf r|^2}{1-|\mathbf s|^2}$, and the relative angle.

Two features are worth naming. First, the relative entropy of two biquaternion states is **not** a function of the Bloch distance $|\mathbf r-\mathbf s|$ alone; it depends on the two radii and the angle, and is therefore sensitive to the direction of the Bloch vectors and not only to their separation. Second, it is manifestly **asymmetric** in the exchange $\mathbf r\leftrightarrow\mathbf s$, because the coefficient in front of the bracket is $|\mathbf r|$ and the bracket is not symmetric.

The limits are the expected ones. If $\tilde\rho=\tilde\sigma$ the two radii and the angle give $\tfrac12\log1+|\mathbf r|(\mathrm{artanh}|\mathbf r|-\mathrm{artanh}|\mathbf r|)=0$. If $|\mathbf r|\to0$, then
$$
S\big(\tfrac12e_0\big\|\tilde\sigma\big)=-\tfrac12\log\big(1-|\mathbf s|^2\big),
$$
the relative entropy of the trace state from $\tilde\sigma$, which is finite for every faithful $\tilde\sigma$ and tends to $+\infty$ only as $\tilde\sigma$ itself approaches the pure boundary. If $|\mathbf r|\to1$ with $|\mathbf s|<1$ the expression tends to the finite limit
$$
S\big(P_+(\hat{\mathbf r})\big\|\tilde\sigma\big)
=-\tfrac12\log\frac{1-|\mathbf s|^2}{4}
-\mathrm{artanh}\big(|\mathbf s|\big)\cos\gamma',
\qquad \cos\gamma'=\hat{\mathbf r}\cdot\hat{\mathbf s},
$$
which is the direct computation $-\mathrm{Tr}(P_+(\hat{\mathbf r})\log\tilde\sigma)$ in the pure case: the entropy of a pure state vanishes, and the whole value is the cross term.

### Verification on Generic Superpositions

The closed form was checked against the explicit $2\times2$ complex matrices in the representation $\Phi$, with the matrix logarithm computed from the spectral decomposition and the entropy from the eigenvalues. The state pair
$$
\mathbf r=\big(\tfrac35,-\tfrac{3}{10},\tfrac25\big),\qquad
\mathbf s=\big(\tfrac15,\tfrac12,-\tfrac{1}{10}\big),
$$
with $|\mathbf r|^2=\tfrac{61}{100}$, $|\mathbf s|^2=\tfrac{3}{10}$ and $\cos\gamma=-0.163633\ldots$, is a generic superposition with no component vanishing. The results are
$$
S(\tilde\rho\|\tilde\sigma)=0.6046559092,\qquad
S(\tilde\sigma\|\tilde\rho)=0.7233102495,
$$
the first from the boxed formula and the second by exchanging the arguments; both agree with the matrix computation to twelve decimal places, and the asymmetry is $0.118654\ldots$, nonzero as it must be. The same check was run at five further pairs, including pairs on the boundary of the Bloch ball and pairs with one argument at the centre: all agree, and all are non-negative.

### Positivity in the Bloch Geometry

Klein's inequality is not re-derived here; it is a theorem about density matrices, and the states of $\mathbb{B}$ are density matrices. What the framework adds is a geometric reading of where the inequality is tight. The boxed formula vanishes if and only if $|\mathbf r|=|\mathbf s|$ and $\cos\gamma=1$, that is, if and only if $\mathbf r=\mathbf s$, so the relative entropy separates the states of $\mathbb{B}$ as well as it separates arbitrary qubit states. Near coincidence $\mathbf s=\mathbf r+\delta\mathbf r$ the boxed formula has no linear term, as it must, and its quadratic term is the Kubo–Mori–Bogoliubov metric of the state. For a displacement that changes the purity, $\delta\mathbf r\parallel\mathbf r$, the coefficient is exact,
$$
S(\tilde\rho\|\tilde\sigma)=\frac{|\delta\mathbf r|^2}{2\,(1-|\mathbf r|^2)}+O\big(|\delta\mathbf r|^3\big),
$$
verified by recomputation at small displacements. The coefficient is finite throughout the interior of the Bloch ball and diverges as the pure boundary is approached, where the eigenvalue gap $1-|\mathbf r|^2$ closes. This is the framework's form of the statement that the purity of a nearly pure state is distinguished divergingly well.

## Araki's Relative Modular Operator

The definition used so far is the finite-dimensional one. The general definition, which the modular companions use and which is the one available for a field, is Araki's. On a von Neumann algebra $M$ with faithful normal states $\omega$ and $\varphi$, the **relative modular operator** $\Delta_{\omega,\varphi}$ is the positive operator whose polar decomposition produces the relative Tomita operator, and Araki's relative entropy is
$$
S(\omega\|\varphi)=\big\langle\Omega_\omega,\log\Delta_{\omega,\varphi}\,\Omega_\omega\big\rangle .
$$
It agrees with Umegaki's $S(\rho\|\sigma)$ when $M$ is a finite-dimensional matrix algebra and the two states are given by density matrices, and it is defined for the type III algebras of local quantum field theory, where no density matrix exists. The relative modular operator satisfies the **relative modular condition**, a two-point KMS-type boundary relation for the function
$$
(t,\tilde A,\tilde B)\longmapsto
\omega\big(\tilde A\,\sigma_t^{\varphi,\omega}(\tilde B)\big),
$$
where $\sigma^{(\varphi,\omega)}$ is the **Connes cocycle** flow relating the modular flows of the two states. Two facts connect this object to the rest of the subcategory: the relative modular operator of $\omega$ with itself is the modular operator $\Delta_\omega$ of the Tomita construction, and the modular Hamiltonian $K_\omega=-\log\Delta_\omega$ of the modular companions is the $(\omega,\omega)$ case of the object defined here. The relative entropy is thus the expectation of the logarithm of the relative modular operator in the state's own GNS vector, and the modular Hamiltonian is its diagonal.

Within the finite-dimensional algebra the relative modular operator is explicit. On the Hilbert–Schmidt space of the algebra, with the state $\omega$ fixing the vector $\Omega_\omega=\tilde\rho_\omega^{1/2}$, the relative Tomita operator is $\tilde A\Omega_\varphi\mapsto\tilde A^\dagger\Omega_\omega$ and its polar decomposition gives
$$
\Delta_{\omega,\varphi}\big(\tilde A\big)
=\tilde\rho_\omega\,\tilde A\,\tilde\rho_\varphi^{-1},
\qquad
\log\Delta_{\omega,\varphi}\big(\tilde A\big)
=\log\tilde\rho_\omega\,\tilde A-\tilde A\,\log\tilde\rho_\varphi
=\tilde A\,\tilde K_\varphi-\tilde K_\omega\,\tilde A,
\qquad
\tilde K_\omega=-\log\tilde\rho_\omega\in\mathbb{M}_+ .
$$
Araki's formula evaluated on $\Omega_\omega=\tilde\rho_\omega^{1/2}$ then returns
$$
S(\omega\|\varphi)
=\mathrm{Tr}\Big[\tilde\rho_\omega^{1/2}\Big(\log\tilde\rho_\omega\,\tilde\rho_\omega^{1/2}-\tilde\rho_\omega^{1/2}\log\tilde\rho_\varphi\Big)\Big]
=\mathrm{Tr}\big(\tilde\rho_\omega\log\tilde\rho_\omega\big)-\mathrm{Tr}\big(\tilde\rho_\omega\log\tilde\rho_\varphi\big),
$$
which is the boxed expression; the two were checked against each other on the generic pair above. The operator is the algebra-level form of the closed expression, and it is the object that survives when the finite-dimensional state is replaced by a state of a local algebra.

## Relative Entropy in Quantum Field Theory

The framework's finite-dimensional states are a truncation of a field theory, and the reasons relative entropy rather than entanglement entropy is the primary quantity appear already at the level of the local algebras.

**Entanglement entropy is not defined for a local algebra.** The algebra of observables of a region of Minkowski space is a type III von Neumann algebra, which admits no trace and hence no density matrix. The von Neumann entropy of a reduced state, $-\mathrm{Tr}(\rho_A\log\rho_A)$, is therefore not available. The relative entropy of two states of the region is available, is finite under mild conditions, and reduces to the familiar quantity when a regulator is introduced and removed. This is why the modern algebraic treatment of entanglement in quantum field theory is written in terms of relative entropy.

**Relative entropy is finite for states that differ by a local excitation.** If $\omega$ is the vacuum and $\varphi$ is a state obtained from it by a local excitation, the relative entropy $S(\varphi\|\omega)$ is finite and has the interpretation of the expected modular energy of the excitation. The classic case is the relative entropy between the Minkowski vacuum and a coherent state of a free field, which is finite and equals the number of quanta of the excitation in the appropriate normalization. This finiteness is what makes the first law of entanglement, treated in the companion article *The Modular Hamiltonian and the First Law of Entanglement in Biquaternionic Form*, a statement about a finite quantity.

**Relative entropy and the vacuum distinguishability.** The **Reeh–Schlieder** property, treated in the companion article *The Reeh–Schlieder Theorem under the Biquaternion Framework*, is the statement that the vacuum is cyclic and separating for every local algebra, and the relative modular operator of a pair of states of a local algebra is the technical object whose existence the property guarantees. The argument that the modular flow of a wedge is the boost, due to Bisognano and Wichmann, is an argument about the relative modular operator of the vacuum.

None of these facts is derived here; they are standard quantum field theory, and the framework transcribes their finite-dimensional shadow.

## What Is Established and What Is Interpretation

**Established (theorem, imported).** The Umegaki relative entropy and the properties of positivity, joint convexity, monotonicity and additivity; the Araki relative entropy and the relative modular operator for general von Neumann algebras; the finiteness of the relative entropy of a local excitation of the vacuum; the role of the relative modular operator in the Bisognano–Wichmann theorem. All of this is standard.

**Established (recomputed here).** The states of $\mathbb{B}$ are the Bloch ball $|\mathbf r|\le1$; the logarithm of a faithful state is $\log\tilde\rho=\tfrac12\log\frac{1-|\mathbf r|^2}{4}e_0+i\,\mathrm{artanh}(|\mathbf r|)\hat{\mathbf r}$; the entropy of a state is $-\tfrac12\log\frac{1-|\mathbf r|^2}{4}-|\mathbf r|\,\mathrm{artanh}|\mathbf r|$; and the relative entropy of two states is the boxed closed form, verified at twelve decimal places against the matrix computation on generic Bloch vectors and on states with one argument at the centre.

**Interpretation.** That the closed form, the identity of the trace, and the zero-divisor boundary give a biquaternion reading of relative entropy in which the algebra's own conjugation supplies the logarithm and the relative modular operator. The algebra houses the reading; it does not force it.

**Gaps, left visible.** The logarithm exists only on the faithful states, so the framework's own algebra carries the relative entropy of a pair only when the second state is in the interior; on the pure boundary the quantity is an imported limit. The framework supplies no state selection and no dynamics, and the field-theoretic relative entropy lives on a module over $\mathbb{B}$ and not in $\mathbb{B}$. No empirical consequence is derived.

## Open Questions

**1. The relative entropy of a field state.** The biquaternion module carries the one-mode truncation of a field. Is there a preferred modular structure on the module, in the sense of a faithful state of the module algebra, whose relative entropy reproduces the finite field-theoretic answer?

**2. The boundary value.** The relative entropy extends continuously to the pure boundary only when the second state is faithful. Is there a framework reading of the divergent case, in which the supports fail to nest, in terms of the zero-divisor cone? The divergent case is the one in which the second state is pure and differs from the first: a pure $\tilde\sigma$ has one-dimensional support, which contains the support of $\tilde\rho$ only when $\tilde\rho=\tilde\sigma$, and the antipodal pair $\mathbf r=-\mathbf s$ on the sphere is its extreme instance.

**3. The cocycle.** The Connes cocycle flow, which governs the relative modular operator, has a finite-dimensional realization as the flow that multiplies by $\tilde\rho_\omega^{it}\tilde\rho_\varphi^{-it}$. Whether that flow has an $\mathbb{M}_+$-valued generator in the framework, as the modular flow does, is not worked out here.

**4. The relation to the first law.** The expansion of the relative entropy near coincidence, which is the quantum Fisher information, is the quadratic form whose vanishing controls the first law of entanglement. Whether the framework's closed form makes that law exact, rather than asymptotic, is the subject of the companion article on the modular Hamiltonian.

**5. Empirical contact.** As everywhere in the subcategory, no prediction distinguishing the reading from standard quantum information theory is derived.

## Summary

Relative entropy is Umegaki's $S(\rho\|\sigma)=\mathrm{Tr}(\rho\log\rho)-\mathrm{Tr}(\rho\log\sigma)$, extended to general von Neumann algebras by Araki's relative modular operator. It is the basic quantity of the information-theoretic reading of quantum theory because it is monotone under every physical process, and in quantum field theory it is the only one of the two entropic quantities that is defined, the local algebras being type III and carrying no density matrix.

The states of the biquaternion algebra are the elements of $\mathbb{M}_+$ of the form $\tilde\rho=\tfrac12(e_0+i\mathbf r\cdot\mathbf e)$ with $|\mathbf r|\le1$, and the logarithm of a faithful state is the biquaternion element $\log\tilde\rho=\tfrac12\log\frac{1-|\mathbf r|^2}{4}e_0+i\,\mathrm{artanh}(|\mathbf r|)\hat{\mathbf r}$. The relative entropy of two biquaternion states is therefore a closed expression in their Bloch vectors,
$$
S(\tilde\rho\|\tilde\sigma)
=\tfrac12\log\frac{1-|\mathbf r|^2}{1-|\mathbf s|^2}
+|\mathbf r|\Big(\mathrm{artanh}|\mathbf r|-\mathrm{artanh}|\mathbf s|\,\cos\gamma\Big),
$$
verified against the explicit matrix computation on generic superpositions and non-negative throughout the Bloch ball. The quantity is asymmetric, reduces to $-\tfrac12\log(1-|\mathbf s|^2)$ when the first argument is the trace state, tends to $-\tfrac12\log\frac{1-|\mathbf s|^2}{4}-\mathrm{artanh}(|\mathbf s|)\cos\gamma'$ when the first state becomes pure, and has the Kubo–Mori–Bogoliubov metric as its second-order expansion near coincidence.

The framework-specific feature is the boundary. The logarithm is an element of $\mathbb{B}$ exactly on the faithful states; on the pure boundary the state is a zero divisor and $\log\tilde\rho$ is not an algebra element, while the relative entropy itself remains finite and continuous. Araki's relative modular operator, whose $(\omega,\omega)$ case is the modular operator of the Tomita–Takesaki companions, is the algebra-level object of which the boxed formula is the finite-dimensional value.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Scalar imaginary, central, $i^2=-1$ |
| $\mathbb{M}_+,\mathbb{M}_-$ | Informational (Hermitian) and material (anti-Hermitian) subspaces |
| $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$ | Trace pairing; $\mathrm{Tr}(e_0)=2$ |
| $\Phi(e_k)=-i\sigma_k$, $\Phi(i)=iI_2$ | Matrix isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$ |
| $\tilde\rho=\tfrac12(e_0+i\mathbf r\cdot\mathbf e)$ | State of $\mathbb{B}$; Bloch vector $\mathbf r$ |
| $\lambda_\pm=\tfrac12(1\pm|\mathbf r|)$ | Eigenvalues of the state |
| $S(\tilde\rho)=-\tfrac12\log\frac{1-|\mathbf r|^2}{4}-|\mathbf r|\,\mathrm{artanh}|\mathbf r|$ | von Neumann entropy of a biquaternion state |
| $S(\tilde\rho\|\tilde\sigma)$ | Relative entropy; boxed closed form |
| $\cos\gamma=\mathbf r\cdot\mathbf s/(|\mathbf r||\mathbf s|)$ | Bloch-vector angle |
| $\Delta_{\omega,\varphi}$ | Araki relative modular operator |
| $\log\tilde\rho\in\mathbb{M}_+$ | Biquaternion logarithm of a faithful state |
| $|0\rangle\langle0|=P_+(e_3)$ | Vacuum idempotent (pure state) |
| $\tfrac12 e_0$ | Trace state (maximally mixed) |

## Further Reading

- H. Umegaki, "Conditional expectation in an operator algebra. IV. Entropy and information," *Kodai Mathematical Seminar Reports* **14** (1962) 59–85, for the original definition of relative entropy for density matrices.
- H. Araki, "Relative entropy of states of von Neumann algebras," *Publications of the Research Institute for Mathematical Sciences* **11** (1976) 809–833, and "Relative entropy for states of von Neumann algebras II," **13** (1977) 173–192, for the general definition and the relative modular operator.
- M. Ohya and D. Petz, *Quantum Entropy and Its Use* (Springer, 1993), for relative entropy, the data-processing inequality, and the quantum Fisher information.
- G. Lindblad, "Completely positive maps and entropy inequalities," *Communications in Mathematical Physics* **40** (1975) 147–151, for the monotonicity of relative entropy under completely positive maps.
- E. H. Lieb and M. B. Ruskai, "Proof of the strong subadditivity of quantum-mechanical entropy," *Journal of Mathematical Physics* **14** (1973) 1938–1941, for the inequality that monotonicity of relative entropy implies.
- M. A. Nielsen and I. L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the finite-dimensional theory and the Bloch-ball picture.
- R. Haag, *Local Quantum Physics: Fields, Particles, Algebras* (Springer, 1996), for the algebraic setting and the type III character of local algebras.
- H. Araki, "Relative entropy of states of von Neumann algebras," and E. Witten, "Notes on some entanglement properties of quantum field theory," *Reviews of Modern Physics* **90** (2018) 045003, for the finiteness of the relative entropy of a local excitation of the vacuum.
- M. Takesaki, *Theory of Operator Algebras II* (Springer, 2003), for the Connes cocycle and the relative modular condition.
- Companion article *The GNS Construction in the Biquaternion Framework*, for the states of $\mathbb{B}$, the Bloch ball, and the modular Hamiltonian.
- Companion article *The Modular Theory of Tomita–Takesaki under the Biquaternion Framework*, for the modular operator $\Delta$ and the modular flow.
- Companion article *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, for the state space, the trace formula, and the pure-state projectors.
- Companion article *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, for the material sector and its zero-divisor cone.
