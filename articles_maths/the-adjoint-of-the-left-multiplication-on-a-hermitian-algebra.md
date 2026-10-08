# __The Adjoint of the Left Multiplication on a Hermitian Algebra__

## Introduction

The adjoint of the left multiplication of a Hermitian algebra is the left multiplication by the involution, $L_x^{*} = L_{x^{\dagger}}$, and everything the adjoint does can be read off from that single identity. This article fixes that identity, the fact that it is the adjoint axiom in operator form, and the fact that it determines the involution. Its consequences on the completion — the adjoint at the cyclic vector, the **Tomita operator**, the **polar decomposition** and the completion-level self-adjointness and unitarity criteria — are operator theory and are in *The Modular Structure of a Hermitian Algebra*.

Two facts organise the computation. The first is that the adjoint of the left multiplication is again a left multiplication, so the adjoint of a one-sided operator stays on its own side; the passage to the other side is not adjunction but conjugation by the modular conjugation, and that is operator theory. The second is that the identity $L_x^{*} = L_{x^{\dagger}}$ determines the involution: evaluating at $1$ recovers $x^{\dagger}$ from $L_x^{*}$, so form and involution determine each other.

This article fixes the adjoint of the left multiplication, its form as the adjoint axiom, and the fact that it determines the involution.

The involution and the adjoint axiom are *Hermitian Adjoints on a Hermitian Algebra* and *Hermitian Algebras*; the two representations and the adjoint of the right multiplication are *The Left and the Right Regular Representation* and *The Adjoint of the Left and the Right Multiplication*; the Tomita operator, the polar decomposition and the modular objects are *The Modular Structure of a Hermitian Algebra*. Those are cited. The algebra is $A$ with involution $\dagger$ and form $\langle\cdot,\cdot\rangle$.

## The Adjoint of the Left Multiplication

**Definition.** For $x\in A$ the **left multiplication** is $L_x(y) = xy$ on $A$, and $\bar L_x$ is its extension to the completion $H$; the **adjoint** $\bar L_x^{*}$ is the Hermitian adjoint on $H$.

**Theorem.** For every $x$ the left multiplication is bounded on the completion and

$$
\bar L_x^{*} = \bar L_{x^{\dagger}} .
$$

**Proof.** On the algebra the identity is the adjoint axiom, $\langle L_xy,z\rangle = \langle xy,z\rangle = \langle y,x^{\dagger}z\rangle = \langle y,L_{x^{\dagger}}z\rangle$; the operator $L_x$ is bounded on $A$ for the form norm, so it extends to $H$ with the same adjoint; both sides of the identity are bounded and agree on the dense subspace $A$, hence on $H$.

**Proposition (the adjoint at the cyclic vector).** With $\xi = \iota(1)$,

$$
\bar L_x\xi = \iota(x) , \qquad \bar L_x^{*}\xi = \iota(x^{\dagger}) ,
$$

so the adjoint is the map of the cyclic vector to the involution, and the deviation of the involution from the identity on $\iota(A)$ is the deviation of $\bar L_x^{*}$ from $\bar L_x$.

**Proof.** $L_x1 = x$ gives the first identity; the second is the theorem applied to $1$.

**Proposition (positivity of the adjoint products).** For every $x$ and every $u\in H$,

$$
\langle\bar L_x\bar L_x^{*}u,u\rangle = \|\bar L_x^{*}u\|^{2}\geq0 , \qquad \langle\bar L_x^{*}\bar L_xu,u\rangle = \|\bar L_xu\|^{2}\geq0 ,
$$

so $\bar L_x\bar L_x^{*}$ and $\bar L_x^{*}\bar L_x$ are positive operators, and the left multiplications form a $\ast$-closed family.

**Proof.** The two displays are the definition of the Hermitian adjoint.

**Proposition (the adjoint is determined by the form).** If an antilinear map $\Phi$ of $A$ satisfies $L_{\Phi(x)} = L_x^{*}$ for every $x$ then $\Phi = \dagger$; the adjoint axiom therefore determines the involution and conversely.

**Proof.** Evaluating at $1$ gives $\Phi(x) = \Phi(x)\cdot 1 = L_{\Phi(x)}1 = L_x^{*}1 = x^{\dagger}$ by the previous proposition.

The **Tomita operator**, the **polar decomposition** $\bar S=J\Delta^{1/2}$, the **modular operator** and the completion-level self-adjointness and unitarity criteria are operator theory and are in *The Modular Structure of a Hermitian Algebra* (Part II).

## Worked Cases

### The Group Algebra

For $A = \mathbb{C}[G]$ with the standard form, $L_g^{*} = L_{g^{-1}}$, the Tomita operator is $S(g\xi) = g^{-1}\xi$, and the form is tracial, so $\Delta = \mathrm{id}$ and $S = J$ is a bounded antiunitary involution with $J\bar L_gJ = \bar R_{g^{-1}}$.

### Matrices

For $A = M_n(\mathbb{C})$ with the Hilbert–Schmidt form, $\bar L_a^{*} = \bar L_{a^{*}}$ with $a^{*}$ the conjugate transpose, the Tomita operator is $S(a\xi) = a^{*}\xi$ extended, the polar decomposition is $S = J$ with $\Delta = \mathrm{id}$, and every left multiplication is normal.

### A Non-Tracial Case

For the group von Neumann algebra of an infinite non-abelian group with a non-tracial vector state, the Tomita operator is unbounded, $\Delta\neq\mathrm{id}$, and the adjoint of the left multiplication is the $\Delta$-twisted right multiplication; this is the case in which the three descriptions — involution, adjoint, modular operator — visibly differ.

## Summary

The adjoint of the **left multiplication** of a Hermitian algebra is the left multiplication by the involution, $\bar L_x^{*} = \bar L_{x^{\dagger}}$, and it is computed at the cyclic vector by $\bar L_x^{*}\xi = \iota(x^{\dagger})$; the adjoint axiom is exactly this identity, so the form determines the involution and conversely. The **Tomita operator** $S(x\xi) = x^{\dagger}\xi$ is the closure of the involution, it is antilinear with $S^{2} = \mathrm{id}$ on its domain, it exchanges the sides through $SL_xS = R_{x^{\dagger}}$, and it converts an adjoint into a conjugation of the other side, $L_x^{*} = SR_xS$. Its **polar decomposition** $\bar S = J\Delta^{1/2}$ produces the modular conjugation $J$, the modular operator $\Delta = \bar S^{*}\bar S$, the inversion $J\Delta J = \Delta^{-1}$ and the modular group, so the adjoint of the left multiplication already carries the modular structure and the deviation of the form from being tracial is exactly $\Delta\neq\mathrm{id}$. The **criteria** are: $\bar L_x$ self-adjoint exactly when $x = x^{\dagger}$, normal exactly when $xx^{\dagger} = x^{\dagger}x$, unitary exactly when $x$ is a unitary element, positive exactly when $x$ is in the positive cone; the modular group acts by $\Delta^{it}\bar L_x\Delta^{-it} = \bar L_{\sigma_t(x)}$. The involution and the adjoint axiom are *Hermitian Adjoints on a Hermitian Algebra*, the two-sided adjoint identities are *The Adjoint of the Left and the Right Multiplication*, the modular objects are *The Modular Operator and Tomita-Takesaki Theory*, and the unbounded spectral theory is deferred to Part III with *Analysis on Linear Spaces*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_x(y) = xy$, $\bar L_x$ | Left multiplication and its extension to $H$ |
| $\bar L_x^{*} = \bar L_{x^{\dagger}}$ | The adjoint |
| $S^{2} = \mathrm{id}$, $SL_xS = R_{x^{\dagger}}$ | Involutivity and the exchange of sides |
| $L_x^{*} = SR_xS$ | Adjoint as a conjugation of the right multiplication |

## Further Reading

- Jacques Dixmier, *Von Neumann Algebras* (North-Holland, 1981), for the left multiplication, its adjoint and the standard form.
- Serban Stratila and László Zsidó, *Lectures on von Neumann Algebras* (Abacus Press, 1979), for the Tomita operator of a Hermitian algebra.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 2 (Academic Press, 1986), for the polar decomposition of the Tomita operator.
- Masamichi Takesaki, *Tomita's Theory of Modular Hilbert Algebras and its Applications*, Lecture Notes in Mathematics 128 (Springer, 1970), for the modular operator from the involution.
- Ola Bratteli and Derek W. Robinson, *Operator Algebras and Quantum Statistical Mechanics*, vol. 1 (Springer, 1987), for the standard form and the modular group.
