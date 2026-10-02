# __The Modular Group and the KMS Condition__

## Introduction

The **KMS condition** is an analytic condition on a state and a one-parameter group of automorphisms: the function $t\mapsto\omega(x\sigma_t(y))$ must extend holomorphically to a strip and its boundary values must be $\omega(\sigma_t(y)x)$ at the other edge. It is a condition of commutativity up to an analytic continuation, and it is the exact condition that identifies the modular group: for a state $\omega$ with a cyclic and separating vector, the modular group of *The Modular Operator and Tomita-Takesaki Theory* is the unique group of automorphisms satisfying the condition.

The **modular automorphism group** is therefore not an extra structure but the canonical flow attached to a state: change the state and the flow changes, and the cocycle relating two flows is the derivative of a unitary. The theory of KMS states is the theory of the states whose modular group is a prescribed flow, and the passage between two states is the passage between two flows related by a cocycle.

This article fixes the KMS condition, the theorem that the modular group satisfies it and is characterised by it, the modular automorphism attached to a state, and the relation between the flows of different states.

The modular operator and the Tomita–Takesaki theorem are *The Modular Operator and Tomita-Takesaki Theory*; the states and their representations are *The GNS Construction*; the positive elements are *Self-Adjoint Elements and the Positive Cone*; the indefinite version is *Krein–Tomita–Takesaki Theory*. Those are cited. The algebra is $\mathcal{M}$ with a state $\omega$, the flow is $\sigma$, and $\beta>0$ is the parameter.

## The KMS Condition

**Definition.** Let $\omega$ be a state on a von Neumann algebra $\mathcal{M}$ and $\sigma$ a strongly continuous group of automorphisms of $\mathcal{M}$. Then $\omega$ is **KMS at $\beta>0$ with respect to $\sigma$** when for every $x, y\in\mathcal{M}$ there is a function $F_{x,y}$ bounded and continuous on the closed strip $\{z : 0\leq\mathrm{Im}\,z\leq\beta\}$ and holomorphic in the open strip, with

$$
F_{x,y}(t) = \omega\big(x\,\sigma_t(y)\big), \qquad F_{x,y}(t+i\beta) = \omega\big(\sigma_t(y)\,x\big)
$$

for all real $t$. The state is **KMS with respect to $\sigma$** when it is KMS at some $\beta$; the normalisation $\beta = 1$ is a rescaling of the group.

**Proposition (the boundary values are a commutativity relation).** The KMS condition can be read as the statement that the two sesquilinear forms

$$
(x,y)\mapsto\omega(x\sigma_t(y)), \qquad (x,y)\mapsto\omega(\sigma_t(y)x)
$$

are the two boundary values of one analytic family, so the KMS condition is a "commutativity up to analytic continuation" of the state with the flow.

**Proof.** The definition is exactly the displayed property; the reading is the standard reformulation used below.

**Proposition (the trace is KMS for the trivial flow).** If $\omega$ is a trace then $\omega$ is KMS at every $\beta$ with respect to the trivial flow $\sigma_t = \mathrm{id}$.

**Proof.** $\omega(xy) = \omega(yx)$ makes $F_{x,y}$ constant and equal on both edges.

**Remark (the role of the holomorphy).** The condition is an analytic one and cannot be seen from the algebraic relations of $\mathcal{M}$ alone: it is the statement that a certain function of $t$ has an analytic continuation across a strip of width $\beta$, and the width is an invariant of the pair $(\omega,\sigma)$.

## The Modular Automorphism Group

**Theorem (the modular group is KMS).** Let $\mathcal{M}$ have a cyclic and separating vector $\xi$ with vector state $\omega$, and let $\sigma_t = \mathrm{Ad}\,\Delta^{it}$ be the modular group of the pair. Then $\omega$ is KMS at $\beta = 1$ with respect to $\sigma$.

**Proof.** The KMS statement is the analytic continuation of the identity $\Delta = S^{*}S$: with $S(x\xi) = x^{*}\xi$ one has, for $t$ real, $\omega(x\sigma_t(y)) = \langle \Delta^{it}y\xi, x^{*}\xi\rangle$-type and the function of $t$ continues to the strip with the second boundary value $\omega(\sigma_t(y)x) = \langle x\xi,\Delta^{it}y\xi\rangle$; the two expressions are the two boundary values of the same analytic function because $\Delta^{it}$ extends to the strip and the vector $\xi$ lies in the domains of $\Delta^{z}$ there.

**Theorem (characterisation of the modular group).** If $\omega$ is a faithful normal state and $\sigma$ a strongly continuous group of automorphisms of $\mathcal{M}$ such that $\omega$ is KMS at $\beta = 1$ with respect to $\sigma$, then there is a cyclic and separating vector $\xi$ for $\mathcal{M}$ with vector state $\omega$, and $\sigma$ is the modular group of the pair $(\mathcal{M},\xi)$. So the modular group is the unique group of automorphisms for which the state is KMS.

**Proof.** By the GNS construction *The GNS Construction*, fidelity and normality give a faithful normal representation with a cyclic and separating vector $\xi$ for the vector state $\omega$; the KMS condition with respect to $\sigma$ is then checked to agree with the modular condition of the Tomita–Takesaki theorem, and the uniqueness follows because the polar decomposition of the Tomita operator is unique and determines $\Delta$ and hence the group.

**Corollary (the modular automorphism of a state).** Every faithful normal state on a von Neumann algebra has a canonical one-parameter group of automorphisms, its **modular automorphism group**, and two states have the same modular group exactly when one is a positive multiple of the other; in general the modular groups of two states are related by the cocycle of the Radon–Nikodym derivatives.

**Proof.** Existence and uniqueness are the two theorems; the comparison of two states is the standard cocycle computation for the two vector states and their modular operators.

## The KMS States

**Definition.** A state $\omega$ is a **KMS state** with respect to a given flow $\sigma$ when it satisfies the KMS condition of the first section with respect to $\sigma$.

**Proposition (the set of KMS states is convex).** For a fixed flow $\sigma$ the KMS states at a fixed $\beta$ form a convex set, and its extreme points are the states whose GNS representations are factors.

**Proof.** The KMS condition is linear in $\omega$, giving convexity; purity and extremality are the irreducibility criterion of *The GNS Construction*, and a state is extreme exactly when its representation is a factor representation.

**Proposition (the modular group of a KMS state is the flow).** If $\omega$ is a KMS state with respect to a flow $\sigma$ and $\omega$ is faithful and normal, then the modular group of $\omega$ is exactly $\sigma$.

**Proof.** The characterisation theorem.

**Remark (the KMS condition is a characterisation, not a definition).** The modular group of a state can be defined entirely algebraically from the Tomita operator; the KMS condition gives it an external characterisation as the unique flow making the state analytic, and it is through this characterisation that the modular group is recognised when it appears in a computation.

## Worked Cases

### The Trace

For a trace the modular group is trivial and the state is KMS at every $\beta$; the modular operator is the identity, and the condition degenerates to the commutativity of the state with everything.

### The Temperature Parameter

On a type $\mathrm{I}$ factor with the state $\omega(x) = \mathrm{tr}(\rho_{\beta}x)$, $\rho_{\beta} = e^{-\beta h}/Z$, the modular group is $\sigma_t(x) = e^{ith}xe^{-ith}$ and the state is KMS at the given $\beta$ with respect to it: this is the model computation that shows the KMS condition at a general $\beta$ and the modular group of an exponential density matrix.

### A General Modular Group

For an arbitrary faithful normal state, the modular automorphism group exists by the corollary and its generator, when finite, is a derivation of the algebra; the one-parameter family of states obtained by pushing $\omega$ along the modular group has constant modular group, which is why the flow is called the flow of the state.

## Summary

The **KMS condition** for a state $\omega$ and a strongly continuous group $\sigma$ of automorphisms asks that $t\mapsto\omega(x\sigma_t(y))$ extend holomorphically across the strip of width $\beta$ and that the second boundary value be $\omega(\sigma_t(y)x)$; it is a commutativity condition of the state with the flow, up to analytic continuation, and a trace is KMS for the trivial flow at every $\beta$. The **modular automorphism group** $\sigma_t = \mathrm{Ad}\,\Delta^{it}$ of a cyclic and separating vector is KMS at $\beta = 1$, and conversely the KMS condition with respect to a strongly continuous group characterises the modular group, so every faithful normal state has a canonical flow, its **modular automorphism group**, and the flow determines the state up to a positive multiple. The **KMS states** for a fixed flow form a convex set whose extreme points are the states with factor representations, and the modular group of a faithful normal KMS state is the flow itself. The modular data is *The Modular Operator and Tomita-Takesaki Theory*, the states are *The GNS Construction*, the positive cone is *Self-Adjoint Elements and the Positive Cone*, and the indefinite version is *Krein–Tomita–Takesaki Theory*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F_{x,y}(t) = \omega(x\sigma_t(y))$ | The KMS function |
| $F_{x,y}(t+i\beta) = \omega(\sigma_t(y)x)$ | The second boundary value |
| KMS at $\beta$ | Holomorphy in the strip $0<\mathrm{Im}\,z<\beta$ |
| $\sigma_t = \mathrm{Ad}\,\Delta^{it}$ | The modular automorphism group |
| $\omega$ KMS $\Rightarrow$ $\sigma$ modular | The characterisation theorem |
| Cocycle of two states | The relation between their modular groups |
| Convex set of KMS states | Extreme points are factor states |

## Further Reading

- Rudolf Haag, N. M. Hugenholtz and Marinus Winnink, "On the equilibrium states in quantum statistical mechanics", *Communications in Mathematical Physics* **5** (1967), 215–236, for the KMS condition and its characterisation of the modular group.
- Masamichi Takesaki, *Tomita's Theory of Modular Hilbert Algebras and its Applications*, Lecture Notes in Mathematics 128 (Springer, 1970), for the modular automorphism group.
- Ola Bratteli and Derek W. Robinson, *Operator Algebras and Quantum Statistical Mechanics*, vol. 1 (Springer, 1987), for the KMS condition and the modular theory of states.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 2 (Academic Press, 1986), for the modular group and the standard form.
- Alain Connes, "Une classification des facteurs de type III", *Annales Scientifiques de l'École Normale Supérieure* **6** (1973), 133–252, for the cocycle relating the modular groups of two states.
