# __The Adjoint of the Left and the Right Multiplication__

## Introduction

The adjoint of the left multiplication of a Hermitian algebra is the left multiplication by the involution, $L_x^{*} = L_{x^{\dagger}}$, and the adjoint of the right multiplication is the right multiplication by the involution, $R_x^{*} = R_{x^{\dagger}}$. Both identities are the adjoint axiom in operator form, and together they say that the two regular representations are $\ast$-representations up to the passage from left to right. The content of the article is the explicit form of these adjoints and the way the modular conjugation ties them together.

The two representations are exchanged by the **modular conjugation**, and the exchange $\jmath\bar L_x\jmath = \bar R_{x^{\dagger}}$, whence $\jmath\bar L_x^{*}\jmath = \bar R_x$, is operator theory on the completion; it is proved in *The Modular Structure of a Hermitian Algebra*.

This article fixes the adjoints of the one-sided multiplications and their explicit form.

The adjoint axiom and the involution are *Hermitian Adjoints on a Hermitian Algebra* and *Hermitian Algebras*; the two representations are *The Left and the Right Regular Representation*; the modular conjugation and the standard form are *The Modular Structure of a Hermitian Algebra*. Those are cited. The algebra is $A$ and the completion $H$.

## The Adjoint of the Left Multiplication

**Theorem.** For every $x\in A$ the extended left multiplication satisfies

$$
\bar L_x^{*} = \bar L_{x^{\dagger}} \qquad \text{on } H .
$$

So the adjoint of the left multiplication by $x$ is the left multiplication by the involution of $x$, and the map $x\mapsto\bar L_x$ is a $\ast$-representation with the involution on the algebra and the Hermitian adjoint on the operators.

**Proof.** On $A$ the identity is the adjoint axiom, $\langle L_xy,z\rangle = \langle y,L_{x^{\dagger}}z\rangle$; both sides are bounded and agree on the dense set $A$, hence extend to the same operator on $H$.

**Proposition (the action on the cyclic vector).** With $\xi = \iota(1)$ the adjoint is determined at $\xi$: $\bar L_x^{*}\xi = \iota(x^{\dagger})$, whereas $\bar L_x\xi = \iota(x)$. So the adjoint moves the cyclic vector to the involution, which is the reason the involution is not a bounded map of $H$ in general.

**Proof.** $\bar L_{x^{\dagger}}\xi = \iota(x^{\dagger})$ and $\bar L_x\xi = \iota(x)$; the difference between the two orbits is the closure of the involution.

**Proposition (positivity of the adjoint pairing).** For every $x$ one has $\langle\bar L_x\bar L_x^{*}u,u\rangle = \|\bar L_x^{*}u\|^{2}\geq0$; so the operators $\bar L_x\bar L_x^{*}$ and $\bar L_x^{*}\bar L_x$ are positive, and the left multiplications form a $\ast$-closed family of operators whose positive parts are the ones of *Self-Adjoint Elements and the Positive Cone*.

**Proof.** The displayed identity is the definition of the Hermitian adjoint and the positivity of the norm.

## The Adjoint of the Right Multiplication

**Theorem.** For every $x\in A$ the extended right multiplication satisfies

$$
\bar R_x^{*} = \bar R_{x^{\dagger}} \qquad \text{on } H .
$$

**Proof.** The same computation read from the other side: $\langle R_xy,z\rangle = \langle yx,z\rangle = \langle y,zx^{\dagger}\rangle$ by the adjoint axiom applied with the roles of the two arguments exchanged, which is $\langle y,R_{x^{\dagger}}z\rangle$.

**Proposition (the adjoint is an antirepresentation).** The map $x\mapsto\bar R_x$ is an anti-$\ast$-representation: $\bar R_{xy} = \bar R_y\bar R_x$ and $\bar R_{x^{\dagger}} = \bar R_x^{*}$, so the adjoint operation reverses the order of the representation and of the product in the same way.

**Proof.** $R_{xy}z = zxy = R_yR_xz$ and the adjoint identity is the theorem.

**Remark (left and right adjoints are different operators).** The adjoint of the left multiplication is a left multiplication and the adjoint of the right multiplication is a right multiplication: adjunction respects the side. The exchange between the sides is not adjunction but conjugation by the modular operator, taken up next.

The **modular conjugation** and the exchange between the left and the right representation are operator theory on the completion and are in *The Modular Structure of a Hermitian Algebra* (Part II).

## Worked Cases

### The Group Algebra

For $A = \mathbb{C}[G]$ the adjoint of the left multiplication by $g$ is the left multiplication by $g^{-1}$, and the modular conjugation exchanges the left and the right regular representations, $\jmath L_g\jmath = R_{g^{-1}}$.

### Matrices

For $A = M_n(\mathbb{C})$ with the Hilbert–Schmidt form, $\bar L_a^{*} = \bar L_{a^{*}}$ with $a^{*}$ the conjugate transpose, and the modular conjugation $J(u) = u^{*}$, the conjugate transpose, satisfies $JL_aJ = R_{a^{*}}$, which is the passage from the left-action copy of $M_n(\mathbb{C})$ to the right-action copy. The smallest witness of $JL_aJ = R_{a^{*}}$ is the matrix unit $a = E_{12}$, for which

$$
a=E_{12}=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad a^{*}=E_{21},\qquad (JL_aJ)(E_{12})=(E_{12}E_{12}^{*})^{*}=E_{11}=E_{12}E_{21}=R_{a^{*}}(E_{12}) .
$$

### The Tracial Case

When the form is tracial the modular conjugation is the operator $x\xi\mapsto x^{*}\xi$ extended, and the exchange theorem reads $JL_xJ = R_{x^{\dagger}}$ with $J$ simultaneously the modular conjugation and the involution: the two operations coincide and the symmetry is transparent.

## Summary

The adjoint of the **left multiplication** is the left multiplication by the involution, $\bar L_x^{*} = \bar L_{x^{\dagger}}$, and the adjoint of the **right multiplication** is the right multiplication by the involution, $\bar R_x^{*} = \bar R_{x^{\dagger}}$; both are the adjoint axiom in operator form, they show that the involution is simultaneously the adjoint operation and the product reversal $\bar R_{xy} = \bar R_y\bar R_x$, and they keep adjunction on the same side. The exchange between the sides by the **modular conjugation**, $\jmath\bar L_x\jmath = \bar R_{x^{\dagger}}$ and $\jmath\bar L_x^{*}\jmath = \bar R_x$, is operator theory and is in *The Modular Structure of a Hermitian Algebra*. The involution and the adjoint axiom are *Hermitian Adjoints on a Hermitian Algebra* and the representations are *The Left and the Right Regular Representation*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\bar L_x^{*} = \bar L_{x^{\dagger}}$ | Adjoint of the left multiplication |
| $\bar R_x^{*} = \bar R_{x^{\dagger}}$ | Adjoint of the right multiplication |
| $\bar L_x^{*}\xi = \iota(x^{\dagger})$ | The adjoint on the cyclic vector |
| $\bar L_x\bar L_x^{*}\geq0$ | Positivity of the adjoint products |
| $\jmath\bar L_x^{*}\jmath = \bar R_x$ | Adjunction plus conjugation = passage to the right |

## Further Reading

- Jacques Dixmier, *Von Neumann Algebras* (North-Holland, 1981), for the adjoints of the regular representations.
- Serban Stratila and László Zsidó, *Lectures on von Neumann Algebras* (Abacus Press, 1979), for the left and right representations and their adjoints.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 2 (Academic Press, 1986), for the modular conjugation and the standard form.
- Masamichi Takesaki, *Tomita's Theory of Modular Hilbert Algebras and its Applications*, Lecture Notes in Mathematics 128 (Springer, 1970), for the exchange between the two regular representations.
- Ola Bratteli and Derek W. Robinson, *Operator Algebras and Quantum Statistical Mechanics*, vol. 1 (Springer, 1987), for the standard form as a left–right symmetry.
