# __Von Neumann Entropy and the Biquaternion Norm Form__

## Introduction

The von Neumann entropy of a state is the fundamental quantitative measure of the information a quantum state fails to hold: it vanishes on the pure states, is maximal on the maximally mixed state, and quantifies the compression achievable in the quantum source coding theorem. In the biquaternion framework the state space of a qubit is the trace-one slice of the positive cone of $\mathbb{M}_+$, and the cone is defined by the algebra's norm form. The question this article answers is what the entropy is, in that geometry.

The answer is a single clean statement: on the state space of the framework, the von Neumann entropy is a function of the norm form alone. For a state $\tilde{\rho} = \tfrac12(e_0 + i\mathbf{r})$ one has

$$
N(\tilde{\rho}) = \tfrac{1}{4}\bigl(1 - |\mathbf{r}|^2\bigr)e_0 ,
$$

so the norm form carries exactly one real number, the Bloch radius squared; and the spectrum of the state depends on the state only through that number, $\lambda_\pm = \tfrac12(1\pm|\mathbf{r}|)$. The entropy is therefore

$$
S(\tilde{\rho}) = h\!\left(\frac{1+|\mathbf{r}|}{2}\right)
= h\!\left(\frac{1+\sqrt{1-4N(\tilde{\rho})}}{2}\right),
\qquad h(p) = -p\log p - (1-p)\log(1-p),
$$

a function of $N$ and nothing else. Equivalently, since the deviation of a state from idempotency is

$$
\tilde{\rho}^2 - \tilde{\rho} = -N(\tilde{\rho})\,e_0 ,
$$

the entropy is a function of the single scalar by which the state fails to be idempotent. Pure states are the zero divisors of the norm form, maximally mixed is its maximum on the state space, and entropy measures the position of the state between them.

This is the informational reading of a geometric fact. The article does not claim that entropy is *derived* from the norm form in the sense of being forced by it — the function $h$ is the standard one, and its form is a theorem of information theory, not of the algebra — but it makes precise which algebraic invariant the entropy sees. The norm form supplies the number; information theory supplies the function. Two invariants of the algebra are in play throughout the framework and must not be conflated: the **trace pairing** $\mathrm{Tr}(\tilde{P}\tilde{H})$, which is positive definite and gives the Born rule, and the **norm form** $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$, which is indefinite of signature $(1,3)$ and gives the cone. Entropy belongs to the second.

The article proceeds as follows. The state, its purity, and the norm form are recalled and the identities connecting them are derived. Then the spectral decomposition is used to compute the entropy and to write it as a function of the norm form, and the logarithm is exhibited as an element of the algebra. Then the consequences are collected: monotonicity, bounds, concavity, unitary invariance, and the behaviour at the two ends of the cone slice. Then the relation to the standard matrix formula is stated, and a section separates what the norm-form description adds from what it merely restates. Open questions and the usual closing sections follow.

## The State, Its Purity, and the Norm Form

### The state space

A state of the informational sector is an element of the Hermitian subspace

$$
\tilde{\rho} = \tfrac{1}{2}\bigl(e_0 + i\,\mathbf{r}\bigr), \qquad \mathbf{r} = r_1e_1 + r_2e_2 + r_3e_3, \quad r_k\in\mathbb{R},
$$

with trace $\mathrm{Tr}(\tilde{\rho}) = 2\,\mathrm{Sc}(\tilde{\rho}) = 1$. Its matrix image is

$$
M(\tilde{\rho}) = \tfrac{1}{2}\bigl(I_2 + \mathbf{r}\cdot\boldsymbol{\sigma}\bigr),
$$

whose eigenvalues are $\tfrac12(1\pm|\mathbf{r}|)$. Positivity, $M(\tilde{\rho})\geq0$, is therefore equivalent to $|\mathbf{r}|\leq1$, and the states form the Bloch ball. The boundary $|\mathbf{r}|=1$ is the set of pure states; the center $\mathbf{r}=0$ is the maximally mixed state $\tilde{\rho} = \tfrac12 e_0$.

### Purity and the deviation from idempotency

Squaring the state gives, using $e_ke_l = -\delta_{kl}e_0 + \epsilon_{klm}e_m$ and the vanishing of the cross terms for the pure scalar part,

$$
\tilde{\rho}^2 = \tfrac{1}{4}\bigl(e_0 + i\mathbf{r}\bigr)^2
= \tfrac{1}{4}\bigl((1+|\mathbf{r}|^2)e_0 + 2i\mathbf{r}\bigr).
$$

Hence the **purity** is

$$
\mathrm{Tr}(\tilde{\rho}^2) = \tfrac{1}{2}\bigl(1 + |\mathbf{r}|^2\bigr),
$$

and the **deviation from idempotency** is a pure scalar multiple of the identity,

$$
\tilde{\rho}^2 - \tilde{\rho} = \tfrac{1}{4}\bigl(|\mathbf{r}|^2 - 1\bigr)e_0 .
$$

The state is pure, $\tilde{\rho}^2 = \tilde{\rho}$, exactly when $|\mathbf{r}|=1$; it is idempotent exactly when its purity is one. Everything that follows is a statement about the single real number $\mathrm{Sc}(\tilde{\rho}^2-\tilde{\rho}) = \tfrac14(|\mathbf{r}|^2-1)\leq0$.

### The norm form on $\mathbb{M}_+$

The norm form of the algebra is $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$. On a Hermitian element $\tilde{H} = h_0e_0 + i\mathbf{h}$ with real coefficients it is the real scalar

$$
N(\tilde{H}) = h_0^2 - |\mathbf{h}|^2 ,
$$

so it has signature $(1,3)$; the cone $N(\tilde{H})\geq0$ with $h_0\geq0$ is the positive cone of the Hermitian subspace, and positivity of the operator is exactly $N(\tilde{H})\geq0$ together with $h_0\geq0$. Equivalently, the norm form is the determinant of the matrix image,

$$
N(\tilde{H}) = \det M(\tilde{H}) ,
$$

which is why it is the natural scalar for the cone: a Hermitian matrix is positive semidefinite precisely when its trace and determinant are both non-negative.

For a state the norm form is

$$
N(\tilde{\rho}) = \tfrac{1}{4}\bigl(1 - |\mathbf{r}|^2\bigr)e_0 ,
$$

a scalar element of the center. Three readings of this single identity organize the rest of the article:

- $N(\tilde{\rho})\geq0$ is positivity, with equality exactly on the pure states; the norm form's zero set is the boundary of the Bloch ball, the zero-divisor cone of $\mathbb{M}_+$.
- Comparing with the deviation from idempotency, $\tilde{\rho}^2-\tilde{\rho} = -N(\tilde{\rho})e_0$: **the mixedness of a state is minus its norm form**. There is no other mixedness parameter.
- The purity is an affine function of the norm form, $\mathrm{Tr}(\tilde{\rho}^2) = 1 - 2N(\tilde{\rho})$.

The norm form therefore measures the failure of a state to be a zero divisor of the algebra, and it does so with one number. On the trace-one slice it takes its minimum $0$ on the pure states and its maximum $\tfrac14$ at the maximally mixed state.

## The Spectral Decomposition and the Entropy

### The spectrum

The state has a spectral decomposition into the two complementary idempotents along its Bloch direction. Writing $\hat{\mathbf{r}} = \mathbf{r}/|\mathbf{r}|$ for $\mathbf{r}\neq0$,

$$
\tilde{\rho} = \lambda_+\,\tilde{P}_+(\hat{\mathbf{r}}) + \lambda_-\,\tilde{P}_-(\hat{\mathbf{r}}),
\qquad
\tilde{P}_\pm(\hat{\mathbf{r}}) = \tfrac{1}{2}\bigl(e_0 \pm i\hat{\mathbf{r}}\bigr),
\qquad
\lambda_\pm = \tfrac{1}{2}\bigl(1 \pm |\mathbf{r}|\bigr).
$$

The two projectors are idempotent, Hermitian, orthogonal, and sum to the identity: $\tilde{P}_\pm^2 = \tilde{P}_\pm$, $\tilde{P}_+\tilde{P}_- = 0$, $\tilde{P}_+ + \tilde{P}_- = e_0$. Their traces are one, and the trace pairing gives $\mathrm{Tr}(\tilde{P}_\pm\tilde{\rho}) = \lambda_\pm$. This is the module-level spectral decomposition recalled in the article on the native qubit; the eigenvalues are read from the Bloch radius by $\lambda_+ - \lambda_- = |\mathbf{r}|$ and $\lambda_+ + \lambda_- = 1$.

### Entropy as a function of the norm form

The **von Neumann entropy** is

$$
S(\tilde{\rho}) = -\lambda_+\log\lambda_+ - \lambda_-\log\lambda_-
= h\!\left(\lambda_+\right).
$$

Since $|\mathbf{r}| = \sqrt{1-4N(\tilde{\rho})}$ on the trace-one slice, this is a function of the norm form alone:

$$
S(\tilde{\rho}) = H\!\left(N(\tilde{\rho})\right),
\qquad
H(N) = h\!\left(\frac{1+\sqrt{1-4N}}{2}\right).
$$

The function $H$ is defined on the interval $N\in[0,\tfrac14]$ that the norm form takes on the state space. At the pure-state end $N=0$ it gives $H(0) = h(1) = 0$; at the maximally mixed end $N=\tfrac14$ it gives $H(\tfrac14) = h(\tfrac12) = \log 2$. On the interior it is smooth and strictly increasing, because $h$ is increasing on $[\tfrac12,1]$ and $\sqrt{1-4N}$ is decreasing. Its derivative,

$$
\frac{dS}{dN} = -\frac{1}{\sqrt{1-4N}}\log\!\left(\frac{1-\sqrt{1-4N}}{1+\sqrt{1-4N}}\right) > 0 .
$$

As $N\to0$ this derivative diverges to $+\infty$: the entropy leaves the pure states — the zero-divisor cone — with infinite slope in the norm-form coordinate. As $N\to\tfrac14$ it tends to the finite value $2$, matching the expansion $S\approx\log2-\tfrac12+2N$ near the maximally mixed state. The entropy is thus a monotone function of the norm form, and the norm form is its argument.

### The logarithm as an element of the algebra

The standard formula can also be written algebraically. On the interior of the Bloch ball the state has full rank, so its real logarithm exists and lies in $\mathbb{M}_+$:

$$
\log \tilde{\rho} = \log\lambda_+\, \tilde{P}_+(\hat{\mathbf{r}}) + \log\lambda_-\, \tilde{P}_-(\hat{\mathbf{r}}) .
$$

Multiplying by $\tilde{\rho}$ and taking the scalar part,

$$
-2\,\mathrm{Sc}\bigl(\tilde{\rho}\log\tilde{\rho}\bigr)
= -\lambda_+\log\lambda_+ - \lambda_-\log\lambda_-
= S(\tilde{\rho}) ,
$$

because the projectors are orthogonal and each has scalar part $\tfrac12$. Equivalently, in the trace notation,

$$
S(\tilde{\rho}) = -\mathrm{Tr}\bigl(\tilde{\rho}\log\tilde{\rho}\bigr),
$$

which is the ordinary matrix formula read in the algebra. The derivation uses only $\mathrm{Tr}(\tilde{\rho}) = 1$, the spectral decomposition, and the trace formula $\mathrm{Tr}(\tilde{Q}) = 2\,\mathrm{Sc}(\tilde{Q})$; no property of the module beyond the spectral theorem is required.

Two caveats belong here. First, the expression requires the logarithm, whose value on the rank-one idempotents is unbounded below; the convention $0\log 0 = 0$ removes the boundary points and assigns the pure states entropy zero as a limit. In the interior the formula is exact; at the boundary it is a limiting statement. Second, the base of the logarithm is conventional; with the natural logarithm the maximal entropy is $\log 2$, and with base two it is one bit. The article uses the natural logarithm and states when a base-two value is quoted.

### The entropy of a state as a function of its purity

Combining the two scalar invariants, the entropy depends on the state through the purity or through the norm form, and the two are affinely related:

$$
\mathrm{Tr}(\tilde{\rho}^2) = 1 - 2N(\tilde{\rho}) , \qquad
S = h\!\left(\frac{1+\sqrt{2\,\mathrm{Tr}(\tilde{\rho}^2)-1}}{2}\right).
$$

On the state space the purity ranges over $[\tfrac12,1]$ and the norm form over $[0,\tfrac14]$; the entropy is a concave function of the purity and an increasing function of the norm form. For a qubit the three invariants — Bloch radius, purity, norm form — carry exactly the same information, and the entropy is a function of any one of them. This degeneracy is special to two dimensions; for a $d$-level system the norm form is no longer a single number, and the entropy depends on the full spectrum rather than on one scalar.

## Consequences of the Norm-Form Dependence

### Bounds

Since $N(\tilde{\rho})\in[0,\tfrac14]$ and $H$ is increasing,

$$
0 \;\leq\; S(\tilde{\rho}) \;\leq\; \log 2 ,
$$

with $S=0$ exactly on the pure states (the zero divisors of the norm form) and $S=\log 2$ exactly at the maximally mixed state, the unique maximizer. The upper bound is the dimension of the module in nats, $\log\dim_{\mathbb{C}}S = \log2$, and it is attained at the center of the Bloch ball, which is also the point where the norm form takes its maximal value $\tfrac14$ on the trace-one slice.

### Monotonicity and the cone

Define the "radial" coordinate $\rho_{\mathrm{B}} = |\mathbf{r}| = \sqrt{1-4N}$. Radial contraction of the state toward the center — the operation $\mathbf{r}\mapsto(1-p)\mathbf{r}$ for $0\leq p\leq1$, which is depolarization — strictly increases $N$ and strictly increases $S$ for any state with $\mathbf{r}\neq0$. Radial expansion toward the boundary strictly decreases both. In the language of the cone, moving the state deeper into the positive cone (larger $N$) increases its entropy; approaching the zero-divisor cone ($N\to0$) decreases it to zero. Entropy is thus a monotone coordinate on the cone slice, and the pure states form its boundary.

### Concavity

The entropy is concave. For two states and $0\leq t\leq1$,

$$
S\bigl(t\tilde{\rho}_1 + (1-t)\tilde{\rho}_2\bigr) \;\geq\; t\,S(\tilde{\rho}_1) + (1-t)\,S(\tilde{\rho}_2).
$$

In the norm-form description this is the statement that the composition $H\circ N$ is concave along convex combinations of states. Since $N$ is a quadratic (and hence not affine) function of the state, the concavity of $H\circ N$ is not a trivial consequence of the concavity of $H$; it is the statement that mixing cannot decrease information, verified spectrum by spectrum. The maximally mixed state is the unique fixed point of the mixing map $\tilde{\rho}\mapsto\tfrac12\tilde{\rho}+\tfrac14 e_0$ and is the state of largest entropy.

### Unitary invariance

Rotor conjugation by a matrix-unitary biquaternion, $\tilde{\rho}\mapsto\tilde{U}\tilde{\rho}\tilde{U}^\dagger$ with $\tilde{U}\tilde{U}^\dagger = e_0$, rotates the Bloch vector without changing its length. It therefore preserves $N(\tilde{\rho})$, the purity, the spectrum, and the entropy. This is the statement that the entropy is a unitary invariant, as it must be; in the framework it is the statement that $S$ is a function of the norm form, which the inner automorphisms of the algebra preserve.

## Relation to the Standard Formula

The standard von Neumann entropy of a density operator is $S = -\mathrm{Tr}(\rho\log\rho)$ with eigenvalues $\lambda_i$. For a qubit with Bloch vector $\mathbf{r}$, the eigenvalues are $\tfrac12(1\pm|\mathbf{r}|)$ and the entropy is $h\!\left(\tfrac{1+|\mathbf{r}|}{2}\right)$. This is exactly the formula derived above, so the framework's entropy is the standard entropy. Nothing here changes a numerical prediction.

What the norm-form reading adds is the *location* of the entropy's argument. In the matrix formulation the entropy is a function of the spectrum, and the spectrum is obtained by diagonalizing a matrix. In the biquaternion formulation the state carries a norm form, and on the trace-one slice the norm form is the deviation from idempotency; the entropy is a function of that scalar. The operative content is that:

- purity is an affine function of the norm form, $\mathrm{Tr}(\tilde{\rho}^2) = 1-2N(\tilde{\rho})$;
- the mixedness scalar is exactly the norm form up to sign, $\tilde{\rho}^2-\tilde{\rho} = -N(\tilde{\rho})e_0$;
- the entropy is a monotone function of the position of the state in the cone of the norm form.

None of this is available in the same form for a general $d$-level system, where the norm form is not a single number; the qubit is special because its state space is the cone slice of a single quadratic form.

## What the Norm-Form Description Does and Does Not Claim

**What it does.**

- It exhibits the entropy as a function of the norm form, $S = H(N)$, on the whole state space, with $H$ explicit.
- It identifies the pure states as the zero divisors of the norm form and the maximally mixed state as its maximum on the trace-one slice.
- It gives the algebraic identity $\tilde{\rho}^2-\tilde{\rho} = -N(\tilde{\rho})e_0$ relating mixedness to the norm form.
- It reproduces the standard qubit entropy and its bounds $0\leq S\leq\log2$.

**What it does not.**

- It does not derive the Shannon function $h$; the functional form of the entropy is a theorem of information theory, imported as standard.
- It does not extend the "entropy is a function of the norm form" statement beyond the qubit. For larger systems the norm form is not a single real number, and the argument fails.
- It does not by itself give the entropy of a *reduced* state of a composite system except through the partial trace, which is an additional structure on $\mathbb{B}\otimes\mathbb{B}$ and is treated in the companion articles on entanglement.
- It does not supply data-processing inequalities, monotonicity under channels, or strong subadditivity; those are properties of the entropy under maps and are developed with the channel formalism.

## Open Questions

**1. Entropy from the algebra alone.** The entropy is a function of the norm form, but the function $h$ is not algebraic. Is there a characterization of the entropy as the unique (up to scale) quantity on the cone slice that is monotone, concave, and unitary invariant? For the qubit this is plausible; a derivation from algebraic axioms alone has not been given.

**2. The many-qubit case.** For $n$ qubits the state space is the positive cone slice of $\mathbb{M}_+^{\otimes n}$, and the norm form is replaced by a family of invariants. Which algebraic data determine the entropy there, and does the norm form of the tensor product play the role the single norm form plays here?

**3. Entropy and the trace pairing.** Entropy is a function of the norm form; the Born rule is a function of the trace pairing. Is there an algebraic relation between the two pairings that makes this division of labour inevitable, or is it an accident of the qubit?

**4. Relative entropy.** The quantum relative entropy $S(\rho\|\sigma)$ measures distinguishability and underlies the Holevo bound. Its biquaternion form, and whether it admits a norm-form expression in the qubit case, is the natural continuation of this article.

**5. Empirical content.** As elsewhere in the framework, the entropy in biquaternion form is the standard entropy transcribed. It predicts nothing new; its value is structural.

## Summary

The state space of the qubit is the trace-one slice of the positive cone of the Hermitian subspace $\mathbb{M}_+$, and the cone is defined by the algebra's norm form

$$
N(\tilde{H}) = h_0^2 - |\mathbf{h}|^2 = \det M(\tilde{H}), \qquad
N(\tilde{\rho}) = \tfrac{1}{4}\bigl(1-|\mathbf{r}|^2\bigr)e_0 .
$$

The norm form of a state is a single real number taking values in $[0,\tfrac14]$ on the state space. The deviation of the state from idempotency is minus that number, $\tilde{\rho}^2-\tilde{\rho} = -N(\tilde{\rho})e_0$, and the purity is affine in it, $\mathrm{Tr}(\tilde{\rho}^2) = 1-2N(\tilde{\rho})$. The spectrum is $\lambda_\pm = \tfrac12(1\pm\sqrt{1-4N})$, so the von Neumann entropy is a function of the norm form and nothing else,

$$
S(\tilde{\rho}) = h\!\left(\frac{1+\sqrt{1-4N(\tilde{\rho})}}{2}\right) = -\mathrm{Tr}\bigl(\tilde{\rho}\log\tilde{\rho}\bigr),
$$

with $S=0$ exactly on the pure states (the zero divisors of the norm form) and $S=\log2$ exactly at the maximally mixed state (the maximum of the norm form on the slice). Entropy is monotone in the norm form, concave, and invariant under the unitary inner automorphisms that preserve the norm form.

The description is the standard qubit entropy, and it predicts nothing new. What it makes precise is which invariant the entropy measures: not the trace pairing of the Born rule, but the norm form whose cone is the state space, and, on that cone slice, the distance of the state from the zero-divisor boundary.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $\mathbb{M}_+$ | Hermitian subspace (states and observables) |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion units, $e_k^2 = -e_0$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $\tilde{\rho} = \tfrac12(e_0 + i\mathbf{r})$ | State with Bloch vector $\mathbf{r}$, $|\mathbf{r}|\le1$ |
| $\tilde{P}_\pm(\hat{\mathbf{r}}) = \tfrac12(e_0\pm i\hat{\mathbf{r}})$ | Spectral idempotents of the state |
| $\lambda_\pm = \tfrac12(1\pm|\mathbf{r}|)$ | Eigenvalues |
| $\mathrm{Tr}(\tilde{Q}) = 2\,\mathrm{Sc}(\tilde{Q})$ | Trace |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$ | Norm form |
| $N(\tilde{H}) = h_0^2 - |\mathbf{h}|^2 = \det M(\tilde{H})$ | Norm form of a Hermitian element |
| $N(\tilde{\rho}) = \tfrac14(1-|\mathbf{r}|^2)e_0$ | Norm form of a state |
| $\tilde{\rho}^2 - \tilde{\rho} = -N(\tilde{\rho})e_0$ | Deviation from idempotency |
| $\mathrm{Tr}(\tilde{\rho}^2) = 1-2N(\tilde{\rho})$ | Purity |
| $h(p) = -p\log p-(1-p)\log(1-p)$ | Binary entropy |
| $S(\tilde{\rho}) = -\mathrm{Tr}(\tilde{\rho}\log\tilde{\rho})$ | Von Neumann entropy |
| $S = H(N) = h\!\left(\tfrac{1+\sqrt{1-4N}}{2}\right)$ | Entropy as a function of the norm form |
| $0 \le S \le \log 2$ | Entropy bounds |

## Further Reading

- J. von Neumann, *Mathematical Foundations of Quantum Mechanics* (Princeton, 1955), for the original definition of the entropy of a density operator.
- A. Wehrl, "General properties of entropy," *Reviews of Modern Physics* **50** (1978) 221–260, for concavity, monotonicity, and the standard properties of the von Neumann entropy.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the entropy of a qubit, the Bloch-ball parametrization, and the bounds $0\leq S\leq\log2$.
- A. Peres, *Quantum Theory: Concepts and Methods* (Kluwer, 1995), for the spectral decomposition of a qubit state and the geometry of the Bloch ball.
- I. Bengtsson and K. Życzkowski, *Geometry of Quantum States* (Cambridge, 2006), for the state space as a cone slice and for the geometric meaning of positivity and purity.
- M. Ohya and D. Petz, *Quantum Entropy and Its Use* (Springer, 1993), for the axiomatic characterization of entropy and the relative entropy.
- T. M. Cover and J. A. Thomas, *Elements of Information Theory* (Wiley, 2006), for the Shannon function $h$ and the source-coding interpretation of the entropy.
- The companion articles of this series: *Quantum Mechanics in Biquaternionic Form*, *The Born Rule as a Trace Formula — Derivation and Comparison*, *The Bloch Ball as the Trace-One Slice of the Future Light Cone*, *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, and *Decoherence as Idempotent Projection*.
